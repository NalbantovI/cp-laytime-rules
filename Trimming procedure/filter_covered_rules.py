#!/usr/bin/env python3
"""
Simple approach: Remove covered rules from CP_RULES_CONSOLIDATED.md
Creates CP_RULES_UNCOVERED.md with only rules NOT covered by GRULE.
"""

import os
import re

def scan_grule_for_concepts(rule_dir):
    """Extract all SOF events and stoppage concepts from GRULE files."""
    all_concepts = set()
    
    for root, dirs, files in os.walk(rule_dir):
        for file in files:
            if file.endswith('.grl'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # Extract SOF event names from IsOneOf
                        events_in_isone_of = re.findall(r'Event\.IsOneOf\((.*?)\)', content, re.DOTALL)
                        for match in events_in_isone_of:
                            event_names = re.findall(r'"([^"]+)"', match)
                            all_concepts.update(event_names)
                        
                        # Extract stoppage names
                        stoppages = re.findall(
                            r'LaytimeClock\.Schedule\w+\([^,]+,\s*"([^"]+)"',
                            content
                        )
                        all_concepts.update(stoppages)
                        
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
    
    return all_concepts

def is_covered(rule_text, grule_concepts):
    """Check if rule text contains covered concepts."""
    text_upper = rule_text.upper()
    
    # Check GRULE concepts
    for concept in grule_concepts:
        # Try exact match and with spaces instead of underscores
        variants = [
            concept.upper(),
            concept.upper().replace('_', ' '),
            # Remove _COMMENCED, _COMPLETED, _START, _END suffixes
            re.sub(r'_(COMMENCED|COMPLETED|START|END|STARTED|ENDED)$', '', concept.upper()),
            re.sub(r'_(COMMENCED|COMPLETED|START|END|STARTED|ENDED)$', '', concept.upper()).replace('_', ' ')
        ]
        
        for variant in variants:
            if variant in text_upper:
                return True
    
    # Additional common laytime concepts that are definitely covered
    covered_patterns = [
        r'LOADING\s+(COMMENCED|COMPLETED|START)',
        r'DISCHARGING\s+(COMMENCED|COMPLETED|START)',
        r'OPERATIONS\s+(COMMENCED|COMPLETED)',
        r'NOR\s+(TENDERED|ACCEPTED)',
        r'NOTICE\s+OF\s+READINESS',
        r'WIBON',
        r'WIPON',
        r'WIFPON',
        r'WICCON',
        r'WEATHER\s+(PERMITTING|INTERRUPTION)',
        r'(MOORING|UNMOORING|SHIFTING)',
        r'FREE\s+PRATIQUE',
        r'CUSTOMS\s+CLEARANCE',
    ]
    
    for pattern in covered_patterns:
        if re.search(pattern, text_upper):
            return True
    
    return False

def process_file(input_file, output_file, grule_concepts):
    """Process the consolidated file and create filtered version."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    output_lines = []
    current_rule = []
    in_rule = False
    in_rule_text = False
    backtick_count = 0
    rule_text_content = ""
    
    stats = {'total': 0, 'kept': 0, 'removed': 0}
    current_type_stats = {}
    current_rule_type = None
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Track rule type sections
        if line.startswith('## RULE TYPE:'):
            if current_rule_type and current_type_stats:
                print(f"  {current_rule_type}: {current_type_stats['kept']}/{current_type_stats['total']} kept")
            current_rule_type = line.strip().replace('## RULE TYPE: ', '')
            current_type_stats = {'total': 0, 'kept': 0}
            output_lines.append(line)
            i += 1
            continue
        
        # Start of a rule
        if line.startswith('####') and 'Rule' in line:
            stats['total'] += 1
            if current_rule_type:
                current_type_stats['total'] += 1
            
            in_rule = True
            current_rule = [line]
            rule_text_content = ""
            backtick_count = 0
            in_rule_text = False
            i += 1
            continue
        
        # Inside a rule
        if in_rule:
            current_rule.append(line)
            
            # Check if we're in the Rule Text section
            if '**Rule Text:**' in line:
                in_rule_text = True
                i += 1
                continue
            
            # Count backticks to track code blocks
            if in_rule_text:
                if '```' in line:
                    backtick_count += line.count('```')
                else:
                    # Collect rule text content between backticks
                    if backtick_count >= 2:
                        rule_text_content += line
            
            # End of rule (marked by ---  or new rule or new section)
            if line.strip() == '---' and backtick_count >= 3:
                # Decide whether to keep this rule
                if rule_text_content.strip():
                    if is_covered(rule_text_content, grule_concepts):
                        stats['removed'] += 1
                        # Don't add to output
                    else:
                        stats['kept'] += 1
                        if current_rule_type:
                            current_type_stats['kept'] += 1
                        output_lines.extend(current_rule)
                else:
                    # No text to analyze, keep it
                    stats['kept'] += 1
                    if current_rule_type:
                        current_type_stats['kept'] += 1
                    output_lines.extend(current_rule)
                
                in_rule = False
                current_rule = []
                rule_text_content = ""
                i += 1
                continue
        
        # Not in a rule, just pass through
        if not in_rule:
            output_lines.append(line)
        
        i += 1
    
    # Print final type stats
    if current_rule_type and current_type_stats:
        print(f"  {current_rule_type}: {current_type_stats['kept']}/{current_type_stats['total']} kept")
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)
    
    return stats

def main():
    base_dir = '/Users/ivelinnalbantov/Work/cp-laytime/cp-laytime-rules'
    rule_dir = os.path.join(base_dir, 'CP library', 'rule')
    input_file = os.path.join(base_dir, 'CP_RULES_CONSOLIDATED.md')
    output_file = os.path.join(base_dir, 'CP_RULES_UNCOVERED.md')
    
    print("=" * 80)
    print("FILTERING RULES BASED ON GRULE COVERAGE")
    print("=" * 80)
    
    print("\n1. Scanning GRULE files...")
    grule_concepts = scan_grule_for_concepts(rule_dir)
    print(f"   ✓ Found {len(grule_concepts)} GRULE concepts")
    
    print("\n2. Processing consolidated file...")
    stats = process_file(input_file, output_file, grule_concepts)
    
    print("\n" + "=" * 80)
    print("RESULTS")
    print("=" * 80)
    print(f"\n📊 Total rules processed: {stats['total']}")
    print(f"✓ Rules kept (uncovered): {stats['kept']}")
    print(f"✗ Rules removed (covered): {stats['removed']}")
    if stats['total'] > 0:
        print(f"📉 Reduction: {stats['removed'] / stats['total'] * 100:.1f}%")
    
    print(f"\n✅ Filtered file created: {output_file}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Remove rules from CP_RULES_CONSOLIDATED.md that are already covered in GRULE files.
This will create a new file with only uncovered rules.
"""

import os
import re
from collections import defaultdict

def extract_sof_events_from_grule(grule_file_path):
    """Extract all SOF event names referenced in GRULE files."""
    events = set()
    try:
        with open(grule_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Pattern 1: Event.IsOneOf("EVENT_NAME", "EVENT_NAME2", ...)
            pattern1 = r'Event\.IsOneOf\((.*?)\)'
            matches = re.findall(pattern1, content, re.DOTALL)
            for match in matches:
                # Extract quoted strings
                event_names = re.findall(r'"([^"]+)"', match)
                events.update(event_names)
            
            # Pattern 2: Event.Name == "EVENT_NAME"
            pattern2 = r'Event\.Name\s*==\s*"([^"]+)"'
            matches = re.findall(pattern2, content)
            events.update(matches)
    
    except Exception as e:
        print(f"Error reading {grule_file_path}: {e}")
    
    return events

def extract_stoppage_keywords_from_grule(grule_file_path):
    """Extract stoppage types and rule names from GRULE files."""
    stoppages = set()
    try:
        with open(grule_file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Extract stoppage names
            pattern = r'LaytimeClock\.Schedule(?:Stoppage|CargoOperations|Commencement|Laytime)(?:Start|End|Pause|Resumption|Completed|AtHour)?\([^,]+,\s*"([^"]+)"'
            matches = re.findall(pattern, content)
            stoppages.update(matches)
            
            # Extract rule names for context
            rule_pattern = r'rule\s+(\w+)\s+"([^"]*)"'
            rule_matches = re.findall(rule_pattern, content)
            for rule_id, rule_desc in rule_matches:
                stoppages.add(rule_id.upper())
    
    except Exception as e:
        print(f"Error reading {grule_file_path}: {e}")
    
    return stoppages

def scan_grule_directory(rule_dir):
    """Scan all GRULE files in the rule directory."""
    all_events = set()
    all_stoppages = set()
    
    for root, dirs, files in os.walk(rule_dir):
        for file in files:
            if file.endswith('.grl'):
                file_path = os.path.join(root, file)
                events = extract_sof_events_from_grule(file_path)
                stoppages = extract_stoppage_keywords_from_grule(file_path)
                all_events.update(events)
                all_stoppages.update(stoppages)
    
    return all_events, all_stoppages

def is_rule_covered(rule_text, covered_events, covered_stoppages):
    """Check if a rule is covered by GRULE concepts."""
    rule_text_upper = rule_text.upper()
    
    # Check against SOF events
    for event in covered_events:
        event_variants = [
            event,
            event.replace('_', ' '),
            event.replace('_COMMENCED', '').replace('_COMPLETED', '').replace('_START', '').replace('_END', '')
        ]
        
        for variant in event_variants:
            if variant in rule_text_upper or variant.replace('_', ' ') in rule_text_upper:
                return True
    
    # Check against stoppages
    for stoppage in covered_stoppages:
        stoppage_variants = [
            stoppage,
            stoppage.replace('_', ' ')
        ]
        
        for variant in stoppage_variants:
            if variant in rule_text_upper:
                return True
    
    # Check for key laytime concepts covered in common rules
    laytime_concepts = [
        'LOADING COMMENCED',
        'LOADING COMPLETED',
        'DISCHARGING COMMENCED',
        'DISCHARGING COMPLETED',
        'OPERATIONS COMMENCED',
        'OPERATIONS COMPLETED',
        'NOR TENDERED',
        'NOR ACCEPTED',
        'NOTICE OF READINESS',
        'WEATHER INTERRUPTION',
        'WEATHER PERMITTING',
        'SHIFTING',
        'MOORING',
        'UNMOORING',
        'WIBON',
        'WIPON',
        'WIFPON',
        'WICCON',
        'BERTHED',
        'ALONGSIDE',
        'FREE PRATIQUE',
        'CUSTOMS CLEARANCE',
    ]
    
    for concept in laytime_concepts:
        if concept in rule_text_upper:
            return True
    
    return False

def filter_consolidated_file(input_file, output_file, covered_events, covered_stoppages):
    """Filter CP_RULES_CONSOLIDATED.md to keep only uncovered rules."""
    
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split content into sections
    lines = content.split('\n')
    
    # Find where the actual rules start (after statistics table)
    rules_start_idx = 0
    for i, line in enumerate(lines):
        if line.strip().startswith('## RULE TYPE:'):
            rules_start_idx = i
            break
    
    # Keep header and statistics
    header_lines = lines[:rules_start_idx]
    
    # Process rules section
    rules_content = '\n'.join(lines[rules_start_idx:])
    
    # Split by rule type sections
    rule_type_sections = re.split(r'(?=^## RULE TYPE:)', rules_content, flags=re.MULTILINE)
    
    new_rule_type_sections = []
    stats = {'total_before': 0, 'total_after': 0, 'removed': 0}
    type_stats = defaultdict(lambda: {'before': 0, 'after': 0})
    
    for section in rule_type_sections:
        if not section.strip():
            continue
        
        # Extract rule type name
        type_match = re.search(r'## RULE TYPE: (.+)', section)
        if not type_match:
            new_rule_type_sections.append(section)
            continue
        
        rule_type = type_match.group(1).strip()
        
        # Split section into individual rules
        rule_pattern = r'(####\s+.+?\s+-\s+Rule\s+\d+:.+?(?=(?:####|^---\s*$|^## RULE TYPE:|$)))'
        individual_rules = re.findall(rule_pattern, section, re.DOTALL | re.MULTILINE)
        
        stats['total_before'] += len(individual_rules)
        type_stats[rule_type]['before'] = len(individual_rules)
        
        # Filter rules
        kept_rules = []
        for rule in individual_rules:
            # Extract rule text
            text_match = re.search(r'\*\*Rule Text:\*\*\s*\n```\s*\n```(.+?)```', rule, re.DOTALL)
            if text_match:
                rule_text = text_match.group(1).strip()
                if not is_rule_covered(rule_text, covered_events, covered_stoppages):
                    kept_rules.append(rule)
            else:
                # Keep rules where we can't extract text (edge case)
                kept_rules.append(rule)
        
        type_stats[rule_type]['after'] = len(kept_rules)
        stats['total_after'] += len(kept_rules)
        
        if kept_rules:
            # Reconstruct section with updated count
            section_header = section.split('\n')[0:3]
            section_header[1] = f"**Total Rules:** {len(kept_rules)}"
            
            new_section = '\n'.join(section_header) + '\n\n'
            new_section += '\n\n'.join(kept_rules)
            new_section += '\n\n---\n\n'
            new_rule_type_sections.append(new_section)
    
    stats['removed'] = stats['total_before'] - stats['total_after']
    
    # Reconstruct file
    # Update TOC and summary
    new_header = []
    toc_started = False
    toc_ended = False
    
    for line in header_lines:
        if '**Total Rules Extracted:**' in line:
            new_header.append(f"**Total Rules Extracted:** {stats['total_after']}\n")
        elif line.strip().startswith('## TABLE OF CONTENTS'):
            toc_started = True
            new_header.append(line + '\n')
        elif toc_started and not toc_ended:
            if line.strip().startswith('---'):
                toc_ended = True
                # Build new TOC
                for rule_type, counts in sorted(type_stats.items()):
                    if counts['after'] > 0:
                        type_slug = rule_type.lower().replace('/', '-').replace(' ', '-')
                        new_header.append(f"- [{rule_type}](#rule-type-{type_slug}) ({counts['after']} rules)\n")
                new_header.append('\n' + line + '\n')
        else:
            new_header.append(line + '\n')
    
    # Write output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(new_header))
        f.write('\n'.join(new_rule_type_sections))
    
    return stats, type_stats

def main():
    # Paths
    base_dir = '/Users/ivelinnalbantov/Work/cp-laytime/cp-laytime-rules'
    rule_dir = os.path.join(base_dir, 'CP library', 'rule')
    input_file = os.path.join(base_dir, 'CP_RULES_CONSOLIDATED.md')
    output_file = os.path.join(base_dir, 'CP_RULES_UNCOVERED.md')
    
    print("=" * 80)
    print("REMOVING COVERED RULES FROM CONSOLIDATED FILE")
    print("=" * 80)
    
    # Step 1: Scan GRULE files
    print("\n1. Scanning GRULE files...")
    covered_events, covered_stoppages = scan_grule_directory(rule_dir)
    print(f"   ✓ Found {len(covered_events)} SOF events")
    print(f"   ✓ Found {len(covered_stoppages)} stoppages/concepts")
    
    # Step 2: Filter consolidated file
    print("\n2. Filtering consolidated file...")
    stats, type_stats = filter_consolidated_file(input_file, output_file, covered_events, covered_stoppages)
    
    # Step 3: Report results
    print("\n" + "=" * 80)
    print("RESULTS")
    print("=" * 80)
    print(f"\n📊 Rules before filtering: {stats['total_before']}")
    print(f"✓ Rules after filtering: {stats['total_after']}")
    print(f"✗ Rules removed (covered): {stats['removed']}")
    print(f"📉 Reduction: {stats['removed'] / stats['total_before'] * 100:.1f}%")
    
    print("\n📋 Breakdown by Rule Type:")
    for rule_type, counts in sorted(type_stats.items(), key=lambda x: x[1]['before'], reverse=True):
        if counts['before'] > 0:
            removed = counts['before'] - counts['after']
            print(f"  {rule_type:30} {counts['before']:4} → {counts['after']:4}  ({removed} removed)")
    
    print(f"\n✅ Uncovered rules written to: {output_file}")
    print(f"   Original file preserved at: {input_file}")

if __name__ == "__main__":
    main()

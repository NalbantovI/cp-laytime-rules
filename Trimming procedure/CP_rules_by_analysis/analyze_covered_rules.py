#!/usr/bin/env python3
"""
Analyze which rules from CP_RULES_CONSOLIDATED.md are already covered in GRULE files.
This script will identify rules that can be removed from the consolidated file.
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
            
            # Extract stoppage names: LaytimeClock.ScheduleStoppageStart/End(Event.PointInTime(), "STOPPAGE_NAME")
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
                print(f"Scanning: {file_path}")
                
                events = extract_sof_events_from_grule(file_path)
                stoppages = extract_stoppage_keywords_from_grule(file_path)
                
                all_events.update(events)
                all_stoppages.update(stoppages)
                
                print(f"  - Found {len(events)} SOF events")
                print(f"  - Found {len(stoppages)} stoppages/concepts")
    
    return all_events, all_stoppages

def read_sof_merge_csv(csv_path):
    """Read the SOF Merge.csv to get event mappings."""
    event_mappings = {}
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[1:]:  # Skip header
                parts = line.strip().split(',')
                if len(parts) >= 2:
                    old_name = parts[0].strip()
                    new_name = parts[1].strip()
                    if old_name and new_name:
                        # Normalize: replace spaces with underscores, convert to uppercase
                        old_normalized = old_name.upper().replace(' ', '_')
                        new_normalized = new_name.upper().replace(' ', '_')
                        event_mappings[old_normalized] = new_normalized
                        event_mappings[new_normalized] = new_normalized  # Map to itself too
    except Exception as e:
        print(f"Error reading SOF Merge CSV: {e}")
    
    return event_mappings

def analyze_consolidated_rules(consolidated_file, covered_events, covered_stoppages, event_mappings):
    """Analyze CP_RULES_CONSOLIDATED.md and identify covered vs uncovered rules."""
    
    covered_rules = []
    uncovered_rules = []
    
    try:
        with open(consolidated_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split by rule sections
        rule_pattern = r'####\s+([A-Z_\s]+)\s+-\s+Rule\s+(\d+):\s+Extract\s+(\d+)\s*\n\n\*\*Rule Types:\*\*\s+([^\n]+)\s*\n\n\*\*Rule Text:\*\*\s*\n```\s*\n```([^`]+)```'
        
        matches = re.findall(rule_pattern, content, re.DOTALL)
        
        print(f"\nFound {len(matches)} rule entries in consolidated file")
        
        for charter, rule_num, extract_num, types, rule_text in matches:
            charter = charter.strip()
            types = types.strip()
            rule_text = rule_text.strip()
            
            # Check if rule text contains covered keywords
            is_covered = False
            matched_concepts = []
            
            # Normalize rule text for comparison
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
                        is_covered = True
                        matched_concepts.append(f"SOF:{event}")
                        break
            
            # Check against stoppages
            for stoppage in covered_stoppages:
                stoppage_variants = [
                    stoppage,
                    stoppage.replace('_', ' ')
                ]
                
                for variant in stoppage_variants:
                    if variant in rule_text_upper or variant.replace('_', ' ') in rule_text_upper:
                        is_covered = True
                        matched_concepts.append(f"STOPPAGE:{stoppage}")
                        break
            
            # Check for key laytime concepts covered in common rules
            laytime_concepts = [
                ('LOADING', 'LOADING'),
                ('DISCHARGING', 'DISCHARGING'),
                ('OPERATIONS COMMENCED', 'OPERATIONS_COMMENCED'),
                ('OPERATIONS COMPLETED', 'OPERATIONS_COMPLETED'),
                ('NOR TENDERED', 'NOR_TENDERED'),
                ('NOR ACCEPTED', 'NOR_ACCEPTED'),
                ('NOTICE OF READINESS', 'NOR'),
                ('LAYTIME COMMENCE', 'LAYTIME_COMMENCEMENT'),
                ('WEATHER', 'WEATHER'),
                ('SHIFTING', 'SHIFTING'),
                ('MOORING', 'MOORING'),
                ('WIBON', 'WIBON'),
                ('WIPON', 'WIPON'),
                ('WIFPON', 'WIFPON'),
                ('WICCON', 'WICCON'),
            ]
            
            for concept_text, concept_key in laytime_concepts:
                if concept_text in rule_text_upper:
                    is_covered = True
                    matched_concepts.append(f"CONCEPT:{concept_key}")
            
            rule_entry = {
                'charter': charter,
                'rule_num': rule_num,
                'extract_num': extract_num,
                'types': types,
                'text_preview': rule_text[:200] + '...' if len(rule_text) > 200 else rule_text,
                'matched_concepts': matched_concepts
            }
            
            if is_covered:
                covered_rules.append(rule_entry)
            else:
                uncovered_rules.append(rule_entry)
    
    except Exception as e:
        print(f"Error analyzing consolidated file: {e}")
        import traceback
        traceback.print_exc()
    
    return covered_rules, uncovered_rules

def main():
    # Paths
    base_dir = '/Users/ivelinnalbantov/Work/cp-laytime/cp-laytime-rules'
    rule_dir = os.path.join(base_dir, 'CP library', 'rule')
    consolidated_file = os.path.join(base_dir, 'CP_RULES_CONSOLIDATED.md')
    sof_merge_csv = os.path.join(base_dir, 'SOF Merge.csv')
    
    print("=" * 80)
    print("ANALYZING GRULE COVERAGE OF CONSOLIDATED RULES")
    print("=" * 80)
    
    # Step 1: Scan GRULE files
    print("\n1. Scanning GRULE files...")
    covered_events, covered_stoppages = scan_grule_directory(rule_dir)
    
    print(f"\n✓ Total SOF events found: {len(covered_events)}")
    print(f"✓ Total stoppages/concepts found: {len(covered_stoppages)}")
    
    # Step 2: Read SOF Merge mappings
    print("\n2. Reading SOF Merge mappings...")
    event_mappings = read_sof_merge_csv(sof_merge_csv)
    print(f"✓ Total event mappings: {len(event_mappings)}")
    
    # Step 3: Analyze consolidated file
    print("\n3. Analyzing consolidated rules file...")
    covered_rules, uncovered_rules = analyze_consolidated_rules(
        consolidated_file, covered_events, covered_stoppages, event_mappings
    )
    
    # Step 4: Report results
    print("\n" + "=" * 80)
    print("RESULTS")
    print("=" * 80)
    print(f"\n✓ Rules covered by GRULE: {len(covered_rules)}")
    print(f"✗ Rules NOT covered by GRULE: {len(uncovered_rules)}")
    print(f"📊 Coverage: {len(covered_rules) / (len(covered_rules) + len(uncovered_rules)) * 100:.1f}%")
    
    # Write detailed report
    report_file = os.path.join(base_dir, 'GRULE_COVERAGE_ANALYSIS.md')
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# GRULE Coverage Analysis Report\n\n")
        f.write(f"**Generated:** {os.path.basename(__file__)}\n\n")
        f.write("---\n\n")
        
        f.write("## Summary\n\n")
        f.write(f"- **Total Rules Analyzed:** {len(covered_rules) + len(uncovered_rules)}\n")
        f.write(f"- **Rules Covered by GRULE:** {len(covered_rules)}\n")
        f.write(f"- **Rules NOT Covered:** {len(uncovered_rules)}\n")
        f.write(f"- **Coverage Percentage:** {len(covered_rules) / (len(covered_rules) + len(uncovered_rules)) * 100:.1f}%\n\n")
        
        f.write("---\n\n")
        
        f.write("## GRULE Concepts Found\n\n")
        f.write(f"### SOF Events ({len(covered_events)})\n\n")
        for event in sorted(covered_events):
            f.write(f"- `{event}`\n")
        f.write("\n")
        
        f.write(f"### Stoppages and Concepts ({len(covered_stoppages)})\n\n")
        for stoppage in sorted(covered_stoppages):
            f.write(f"- `{stoppage}`\n")
        f.write("\n")
        
        f.write("---\n\n")
        
        f.write("## Covered Rules (Can Be Removed)\n\n")
        f.write(f"**Total:** {len(covered_rules)}\n\n")
        
        for rule in covered_rules[:50]:  # Show first 50
            f.write(f"### {rule['charter']} - Rule {rule['rule_num']}: Extract {rule['extract_num']}\n\n")
            f.write(f"**Types:** {rule['types']}\n\n")
            f.write(f"**Matched Concepts:** {', '.join(rule['matched_concepts'])}\n\n")
            f.write(f"**Preview:** {rule['text_preview']}\n\n")
            f.write("---\n\n")
        
        if len(covered_rules) > 50:
            f.write(f"\n*... and {len(covered_rules) - 50} more covered rules*\n\n")
        
        f.write("---\n\n")
        
        f.write("## Uncovered Rules (Keep in Consolidated File)\n\n")
        f.write(f"**Total:** {len(uncovered_rules)}\n\n")
        
        for rule in uncovered_rules:
            f.write(f"### {rule['charter']} - Rule {rule['rule_num']}: Extract {rule['extract_num']}\n\n")
            f.write(f"**Types:** {rule['types']}\n\n")
            f.write(f"**Preview:** {rule['text_preview']}\n\n")
            f.write("---\n\n")
    
    print(f"\n✅ Detailed report written to: {report_file}")
    
    # Print some examples
    if covered_rules:
        print("\n📋 Sample Covered Rules (first 5):")
        for rule in covered_rules[:5]:
            print(f"  - {rule['charter']} Rule {rule['rule_num']}: {rule['matched_concepts'][:3]}")
    
    if uncovered_rules:
        print("\n📋 Sample Uncovered Rules (first 5):")
        for rule in uncovered_rules[:5]:
            print(f"  - {rule['charter']} Rule {rule['rule_num']}")

if __name__ == "__main__":
    main()

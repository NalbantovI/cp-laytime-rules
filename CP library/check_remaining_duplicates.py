#!/usr/bin/env python3
import re

def normalize_text(text):
    """Normalize text for comparison."""
    return ' '.join(text.split())

def extract_rules_by_charter(filepath):
    """Extract all rules grouped by charter."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    charters = {}
    current_charter = None
    
    # Find all charter sections
    charter_pattern = r'^## ([A-Z0-9_ /]+)$'
    rule_pattern = r'^### ([A-Z0-9_ /]+) - Rule (\d+)\n\n```\n(.*?)\n```'
    
    lines = content.split('\n')
    for line in lines:
        match = re.match(charter_pattern, line)
        if match:
            current_charter = match.group(1)
            charters[current_charter] = []
    
    # Extract rules with their content
    for match in re.finditer(rule_pattern, content, re.MULTILINE | re.DOTALL):
        charter_name = match.group(1)
        rule_num = match.group(2)
        rule_text = match.group(3)
        
        if charter_name in charters:
            charters[charter_name].append({
                'num': rule_num,
                'text': rule_text,
                'normalized': normalize_text(rule_text)
            })
    
    return charters

def find_duplicates_within_charters(charters):
    """Find duplicate paragraphs within each charter's rules."""
    duplicates_found = []
    
    for charter_name, rules in charters.items():
        if len(rules) < 2:
            continue
        
        # Check if any rule's content appears in another rule
        for i, rule1 in enumerate(rules):
            for j, rule2 in enumerate(rules):
                if i >= j:
                    continue
                
                # Check if rule1 is completely contained in rule2
                if rule1['normalized'] in rule2['normalized'] and rule1['normalized'] != rule2['normalized']:
                    duplicates_found.append({
                        'charter': charter_name,
                        'subset_rule': rule1['num'],
                        'superset_rule': rule2['num'],
                        'type': 'complete_subset'
                    })
                # Check if rule2 is completely contained in rule1
                elif rule2['normalized'] in rule1['normalized'] and rule1['normalized'] != rule2['normalized']:
                    duplicates_found.append({
                        'charter': charter_name,
                        'subset_rule': rule2['num'],
                        'superset_rule': rule1['num'],
                        'type': 'complete_subset'
                    })
    
    return duplicates_found

def main():
    filepath = 'MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md'
    
    print("🔍 Checking for remaining duplicate paragraphs...\n")
    
    charters = extract_rules_by_charter(filepath)
    duplicates = find_duplicates_within_charters(charters)
    
    if not duplicates:
        print("✅ No remaining duplicate paragraphs found!")
        print(f"\n📊 Verified {sum(len(rules) for rules in charters.values())} rules across {len(charters)} charters.")
    else:
        print(f"⚠️  Found {len(duplicates)} potential duplicate(s):\n")
        for dup in duplicates:
            print(f"   • {dup['charter']}: Rule {dup['subset_rule']} is a {dup['type']} of Rule {dup['superset_rule']}")

if __name__ == '__main__':
    main()

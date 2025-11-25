#!/usr/bin/env python3
"""
Fix the MASTER file by keeping ONLY the rules identified as UNCOVERED in the analysis.
"""

import re

def parse_uncovered_rules(analysis_file):
    """Extract the rule identifiers that should be KEPT."""
    with open(analysis_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the UNCOVERED section
    uncovered_section = content.split('## UNCOVERED RULES (KEEP in MASTER)')[1]
    
    # Extract charter and rule numbers
    keep_rules = {}
    pattern = r'^### ([A-Z_\s]+) - Rule (\d+)$'
    
    for line in uncovered_section.split('\n'):
        match = re.match(pattern, line)
        if match:
            charter = match.group(1).strip()
            rule_num = match.group(2)
            if charter not in keep_rules:
                keep_rules[charter] = []
            keep_rules[charter].append(rule_num)
    
    return keep_rules

def extract_rule_content(filepath, charter, rule_num):
    """Extract the full content of a specific rule from the backup file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find the rule
    rule_pattern = f"### {charter} - Rule {rule_num}\n"
    collecting = False
    rule_content = []
    
    for i, line in enumerate(lines):
        if line == rule_pattern:
            collecting = True
            rule_content.append(line)
            continue
        
        if collecting:
            # Stop at next rule or charter
            if line.startswith('### ') or line.startswith('## '):
                break
            rule_content.append(line)
    
    return ''.join(rule_content)

def main():
    backup_file = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES_BACKUP.md'
    analysis_file = '/Users/ivelinnalbantov/Work/CP library/RULE_COVERAGE_ANALYSIS.md'
    output_file = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES.md'
    
    print("📖 Parsing UNCOVERED rules from analysis...")
    keep_rules = parse_uncovered_rules(analysis_file)
    
    total_to_keep = sum(len(rules) for rules in keep_rules.values())
    print(f"   Found {total_to_keep} rules to KEEP across {len(keep_rules)} charters")
    
    print("\n�� Building new MASTER file with ONLY uncovered rules...")
    
    # Read backup file header
    with open(backup_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Build output
    output_lines = []
    
    # Add header (everything before first charter)
    for line in lines:
        if line.startswith('## ') and not line.startswith('##'):
            break
        output_lines.append(line)
    
    # Now add only the uncovered rules
    for charter, rule_nums in sorted(keep_rules.items()):
        # Add charter header
        output_lines.append(f"## {charter}\n")
        output_lines.append("\n")
        output_lines.append(f"**Rules extracted:** {len(rule_nums)}\n")
        output_lines.append("\n")
        
        # Add each rule with renumbering
        for new_num, old_num in enumerate(sorted(rule_nums, key=int), 1):
            rule_content = extract_rule_content(backup_file, charter, old_num)
            if rule_content:
                # Replace old rule number with new sequential number
                rule_content = rule_content.replace(
                    f"### {charter} - Rule {old_num}\n",
                    f"### {charter} - Rule {new_num}\n"
                )
                output_lines.append(rule_content)
                output_lines.append("\n")
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)
    
    print(f"✅ Created new MASTER file with {total_to_keep} uncovered rules")
    print(f"📄 Written to: {output_file}")
    
    # Verify
    with open(output_file, 'r') as f:
        verify_content = f.read()
    
    rule_count = len(re.findall(r'^### .+ - Rule \d+$', verify_content, re.MULTILINE))
    print(f"✓ Verified: {rule_count} rules in final MASTER file")

if __name__ == '__main__':
    main()

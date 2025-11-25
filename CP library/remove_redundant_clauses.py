#!/usr/bin/env python3
"""
Remove clauses that are:
1. Already covered in .grl files (gangway, surveys, NOR, shifting, etc.)
2. Configuration/settings (rates, holidays, payment terms)
3. General info without laytime logic
4. Certificate/compliance requirements
"""

import re
from datetime import datetime

def is_redundant_clause(text):
    """Check if clause is redundant (covered in .grl or not laytime-affecting)"""
    
    # Configuration/Settings patterns (no laytime logic, just values)
    config_patterns = [
        r'demurrage.*rate.*per day',
        r'despatch.*rate',
        r'freight.*payable',
        r'freight is.*per cent',
        r'superholidays to be excluded',
        r'holidays.*listed as follows',
        r'payment.*within.*days',
        r'debit note',
        r'overtime to be for account',
        r'crew/officers overtime',
    ]
    
    # Covered in .grl files - these are handled by rules engine
    grl_covered_patterns = [
        r'gangway.*placed',
        r'safe.*gangway',
        r'accessibility.*safe and secure',
        r'no people.*board.*without.*gangway',
        r'survey.*conducted',
        r'draft survey',
        r'on-?hire.*off-?hire survey',
        r'joint.*survey',
        r'inspection.*commenced',
        r'holds inspection',
        r'safety inspection',
        r'vessel.*inspection',
        r'nor.*tendered',
        r'notice of readiness',
        r'shifting.*berth',
        r'warping.*berth',
        r'moving.*berth',
        r'pilot.*board',
        r'time.*moving from.*waiting place',
    ]
    
    # Certificate/Compliance (admin requirements, not laytime calculation)
    cert_patterns = [
        r'certificate.*valid',
        r'certificate.*efficiency',
        r'fumigation.*certificate',
        r'deratization certificate',
        r'isps code',
        r'international ship security',
        r'crew.*vaccinated',
        r'pollution.*act',
        r'water quality improvement act',
        r'comply with.*regulations',
    ]
    
    # General info without laytime impact
    general_info_patterns = [
        r'hague rules',
        r'carrier.*entitled to',
        r'this clause.*applicable',
        r'entire contract',
        r'notices.*shall be in writing',
        r'mortgage',
        r'deed.*covenant',
        r'headings.*included for convenience',
        r'confidential',
        r'restricted group',
    ]
    
    # Vessel specifications (no laytime logic)
    vessel_spec_patterns = [
        r'vessel.*plan.*deadweight scale',
        r'portable bulkheads',
        r'consumption.*warranted',
        r'speed.*warranted',
        r'fuel consumption.*litres per day',
    ]
    
    text_lower = text.lower()
    
    # Check all pattern categories
    all_patterns = (
        config_patterns +
        grl_covered_patterns +
        cert_patterns +
        general_info_patterns +
        vessel_spec_patterns
    )
    
    for pattern in all_patterns:
        if re.search(pattern, text_lower):
            return True
    
    return False

def has_laytime_logic(text):
    """Check if clause contains actual laytime calculation logic"""
    
    laytime_logic_keywords = [
        r'time.*not count',
        r'time.*shall not count',
        r'laytime.*not',
        r'demurrage.*if',
        r'time lost',
        r'time used',
        r'time.*excluded',
        r'laytime.*commence',
        r'laytime.*suspend',
        r'shall count as',
        r'not.*count.*laytime',
        r'time.*for.*account',
        r'additional time',
        r'delay.*time',
    ]
    
    text_lower = text.lower()
    for pattern in laytime_logic_keywords:
        if re.search(pattern, text_lower):
            return True
    
    return False

def extract_rules(text):
    """Extract individual rules from text"""
    lines = text.split('\n')
    rules = []
    current_rule = []
    in_rule = False
    current_charter = 'UNKNOWN'
    
    for line in lines:
        # Track charter name
        if line.startswith('## ') and not line.startswith('## MASTER'):
            current_charter = line.replace('## ', '').strip()
            continue
        
        # Rule header
        if line.startswith('### '):
            if current_rule:
                rules.append({
                    'charter': current_charter,
                    'lines': current_rule
                })
            current_rule = [line]
            in_rule = True
        elif in_rule:
            current_rule.append(line)
    
    # Add last rule
    if current_rule:
        rules.append({
            'charter': current_charter,
            'lines': current_rule
        })
    
    return rules

def clean_laytime_file(input_file, output_file):
    """Remove redundant clauses from laytime file"""
    
    print(f"📖 Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract header
    parts = content.split('---', 2)
    if len(parts) >= 3:
        header = parts[0] + '---' + parts[1] + '---'
        body = parts[2]
    else:
        header = ''
        body = content
    
    # Extract rules
    rules = extract_rules(body)
    print(f"📊 Found {len(rules)} rules to analyze")
    
    # Filter rules
    kept_rules = []
    removed_rules = []
    
    for rule in rules:
        rule_text = '\n'.join(rule['lines'])
        
        # Skip if redundant
        if is_redundant_clause(rule_text):
            removed_rules.append(rule)
            continue
        
        # Keep if has laytime logic
        if has_laytime_logic(rule_text):
            kept_rules.append(rule)
        else:
            # If no clear laytime logic but not redundant, be conservative and keep
            # (unless it's clearly just admin stuff)
            if not any(keyword in rule_text.lower() for keyword in [
                'demurrage rate', 'despatch rate', 'freight payable',
                'holiday list', 'payment term', 'overtime rate',
                'certificate valid', 'hague rule', 'mortgage'
            ]):
                kept_rules.append(rule)
            else:
                removed_rules.append(rule)
    
    print(f"✅ Keeping {len(kept_rules)} rules with laytime logic")
    print(f"🗑️  Removing {len(removed_rules)} redundant/config rules")
    
    # Rebuild document
    output_lines = []
    if header:
        output_lines.append(header)
    
    # Group by charter
    charters = {}
    for rule in kept_rules:
        charter = rule['charter'] or 'UNKNOWN'
        if charter not in charters:
            charters[charter] = []
        charters[charter].append(rule)
    
    # Write charters
    for charter_name in sorted(charters.keys()):
        charter_rules = charters[charter_name]
        output_lines.append(f'\n## {charter_name}\n')
        output_lines.append(f'**Laytime rules:** {len(charter_rules)}\n')
        
        for rule in charter_rules:
            output_lines.extend(rule['lines'])
            output_lines.append('')  # Blank line between rules
    
    # Write output
    output_content = '\n'.join(output_lines)
    
    print(f"✍️  Writing cleaned file to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_content)
    
    # Statistics
    with open(output_file, 'r', encoding='utf-8') as f:
        output_lines_count = len(f.readlines())
    
    print(f"\n📊 Cleanup Results:")
    print(f"   Original rules: {len(rules)}")
    print(f"   Kept rules: {len(kept_rules)}")
    print(f"   Removed rules: {len(removed_rules)}")
    print(f"   Output lines: {output_lines_count}")
    
    # Show examples of removed rules
    if removed_rules:
        print(f"\n🗑️  Examples of removed rules:")
        for i, rule in enumerate(removed_rules[:5], 1):
            rule_header = rule['lines'][0] if rule['lines'] else 'Unknown'
            print(f"   {i}. {rule['charter']} - {rule_header}")
            # Show why it was removed
            rule_text = '\n'.join(rule['lines'])
            if 'gangway' in rule_text.lower():
                print(f"      Reason: Gangway safety (covered in .grl)")
            elif 'survey' in rule_text.lower() or 'inspection' in rule_text.lower():
                print(f"      Reason: Survey/inspection (covered in .grl)")
            elif 'certificate' in rule_text.lower():
                print(f"      Reason: Certificate requirement (admin)")
            elif any(x in rule_text.lower() for x in ['rate', 'payment', 'freight']):
                print(f"      Reason: Configuration/settings")
            else:
                print(f"      Reason: No laytime logic")
    
    return len(kept_rules), len(removed_rules)

if __name__ == '__main__':
    input_file = 'MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md'
    output_file = 'MASTER_CP_LAYTIME_RULES_LOGIC_ONLY.md'
    
    kept, removed = clean_laytime_file(input_file, output_file)
    
    print(f"\n✅ Cleanup complete!")
    print(f"   Clean file: {output_file}")
    print(f"   Rules kept: {kept}")
    print(f"   Rules removed: {removed}")

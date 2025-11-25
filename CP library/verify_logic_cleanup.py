#!/usr/bin/env python3
"""Verify the logic-only cleanup"""

import re

def count_charters_and_rules(filename):
    """Count charters and rules in file"""
    with open(filename, 'r') as f:
        content = f.read()
    
    charters = re.findall(r'^## ([A-Z][^\n]+)$', content, re.MULTILINE)
    rules = re.findall(r'^### ', content, re.MULTILINE)
    
    return len(charters), len(rules)

def check_for_redundant_patterns(filename):
    """Check if any redundant patterns remain"""
    with open(filename, 'r') as f:
        content = f.read().lower()
    
    redundant_patterns = {
        'Gangway/Safety': [r'gangway', r'safe.*accessibility'],
        'Surveys (covered in .grl)': [r'draft survey', r'joint.*survey', r'on-?hire.*off-?hire'],
        'Certificates': [r'certificate.*valid', r'fumigation.*certificate'],
        'Settings/Rates': [r'demurrage.*rate.*per day', r'despatch.*rate'],
        'General Info': [r'hague rules', r'mortgage', r'entire contract'],
        'Vessel Specs': [r'consumption.*warranted', r'portable bulkheads'],
    }
    
    found = {}
    for category, patterns in redundant_patterns.items():
        matches = []
        for pattern in patterns:
            if re.search(pattern, content):
                matches.append(pattern)
        if matches:
            found[category] = matches
    
    return found

def check_laytime_logic_presence(filename):
    """Verify all rules have laytime logic"""
    with open(filename, 'r') as f:
        content = f.read()
    
    # Extract rules
    rules = re.split(r'^### ', content, flags=re.MULTILINE)[1:]
    
    laytime_keywords = [
        'time', 'laytime', 'demurrage', 'count', 'lost', 'used',
        'excluded', 'commence', 'suspend', 'account', 'delay'
    ]
    
    rules_without_logic = []
    for i, rule in enumerate(rules, 1):
        has_logic = any(keyword in rule.lower() for keyword in laytime_keywords)
        if not has_logic:
            rule_header = rule.split('\n')[0][:80]
            rules_without_logic.append(f"Rule {i}: {rule_header}")
    
    return rules_without_logic

# Run verification
print("🔍 VERIFICATION REPORT: LOGIC-ONLY CLEANUP\n")
print("="*60)

# Original vs Cleaned
orig_charters, orig_rules = count_charters_and_rules('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md')
clean_charters, clean_rules = count_charters_and_rules('MASTER_CP_LAYTIME_RULES_LOGIC_ONLY.md')

print(f"\n📊 Rule Count Comparison:")
print(f"   Original: {orig_charters} charters, {orig_rules} rules")
print(f"   Cleaned:  {clean_charters} charters, {clean_rules} rules")
print(f"   Removed:  {orig_rules - clean_rules} rules ({((orig_rules - clean_rules)/orig_rules*100):.1f}%)")

# Check for redundant patterns
print(f"\n🔍 Checking for Redundant Patterns...")
redundant = check_for_redundant_patterns('MASTER_CP_LAYTIME_RULES_LOGIC_ONLY.md')

if redundant:
    print("   ⚠️  Found some redundant patterns:")
    for category, patterns in redundant.items():
        print(f"      - {category}: {len(patterns)} pattern(s)")
else:
    print("   ✅ No redundant patterns found!")

# Check laytime logic
print(f"\n🔍 Checking Laytime Logic Presence...")
no_logic = check_laytime_logic_presence('MASTER_CP_LAYTIME_RULES_LOGIC_ONLY.md')

if no_logic:
    print(f"   ⚠️  Found {len(no_logic)} rules without clear laytime keywords:")
    for rule in no_logic[:5]:
        print(f"      - {rule}")
else:
    print("   ✅ All rules contain laytime logic keywords!")

# File sizes
import os
orig_size = os.path.getsize('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md')
clean_size = os.path.getsize('MASTER_CP_LAYTIME_RULES_LOGIC_ONLY.md')

print(f"\n📁 File Size Comparison:")
print(f"   Original: {orig_size:,} bytes")
print(f"   Cleaned:  {clean_size:,} bytes")
print(f"   Reduced:  {orig_size - clean_size:,} bytes ({((orig_size - clean_size)/orig_size*100):.1f}%)")

# Line count
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md') as f:
    orig_lines = len(f.readlines())
with open('MASTER_CP_LAYTIME_RULES_LOGIC_ONLY.md') as f:
    clean_lines = len(f.readlines())

print(f"\n📄 Line Count Comparison:")
print(f"   Original: {orig_lines:,} lines")
print(f"   Cleaned:  {clean_lines:,} lines") 
print(f"   Reduced:  {orig_lines - clean_lines:,} lines ({((orig_lines - clean_lines)/orig_lines*100):.1f}%)")

print(f"\n" + "="*60)
print(f"✅ VERIFICATION COMPLETE\n")

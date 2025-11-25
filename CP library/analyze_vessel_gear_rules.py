import re

# Read the file
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'r') as f:
    content = f.read()

# Extract all charters and their rules
charter_pattern = r'^## ([A-Z0-9_ /]+)$'
rule_pattern = r'### ([A-Z0-9_ /]+) - Rule (\d+)\n\n```\n(.*?)\n```'

charters = []
charter_matches = list(re.finditer(charter_pattern, content, re.MULTILINE))

for charter_match in charter_matches:
    charter_name = charter_match.group(1)
    charter_start = charter_match.start()
    
    # Find next charter or end of file
    next_charter_idx = charter_matches.index(charter_match) + 1
    if next_charter_idx < len(charter_matches):
        charter_end = charter_matches[next_charter_idx].start()
    else:
        charter_end = len(content)
    
    charter_content = content[charter_start:charter_end]
    
    # Find all rules for this charter
    rules = list(re.finditer(rule_pattern, charter_content, re.DOTALL))
    
    for rule in rules:
        rule_charter = rule.group(1)
        rule_number = rule.group(2)
        rule_text = rule.group(3)
        
        # Check for vessel gear breakdown patterns
        patterns = [
            (r'breakdown.*vessel.*crane', 'vessel crane breakdown'),
            (r'breakdown.*vessel.*gear', 'vessel gear breakdown'),
            (r'vessel.*gear.*breakdown', 'vessel gear breakdown'),
            (r'ship.*crane.*breakdown', 'ship crane breakdown'),
            (r'gantry crane.*breakdown', 'gantry crane breakdown'),
            (r'failure to supply sufficient power', 'power supply failure'),
            (r'pro.?rata.*number of.*cranes', 'pro-rata crane calculation'),
            (r'pro.?rata.*workable.*gear', 'pro-rata workable gear calculation'),
        ]
        
        found_patterns = []
        for pattern, description in patterns:
            if re.search(pattern, rule_text.lower()):
                found_patterns.append(description)
        
        if found_patterns:
            charters.append({
                'charter': charter_name,
                'rule': rule_number,
                'patterns': found_patterns,
                'text': rule_text[:200] + '...' if len(rule_text) > 200 else rule_text
            })

print("=" * 80)
print("VESSEL GEAR/CRANE BREAKDOWN RULES ANALYSIS")
print("=" * 80)
print()
print(f"Found {len(charters)} rules containing vessel gear/crane breakdown provisions:")
print()

for item in charters:
    print(f"## {item['charter']} - Rule {item['rule']}")
    print(f"   Patterns found: {', '.join(item['patterns'])}")
    print(f"   Preview: {item['text'][:150]}...")
    print()

print("=" * 80)
print("COMPARISON WITH EXISTING RULES ENGINE")
print("=" * 80)
print()
print("The rules engine already handles vessel gear breakdowns via:")
print("  1. SHIP_CRANE_BREAKDOWN event type")
print("  2. SHIP_BREAKDOWN event type (general vessel equipment failure)")
print("  3. Default stoppage configuration:")
print("     - ModifierNotUsed: 0.0 (time does NOT count)")
print("     - Owner's fault - laytime suspended")
print()
print("These charter party clauses are REDUNDANT because:")
print("  - The default behavior already excludes breakdown time")
print("  - Pro-rata calculations are implementation details, not rules")
print("  - Power supply failures are covered under SHIP_BREAKDOWN")
print()
print("=" * 80)
print("RECOMMENDATION")
print("=" * 80)
print()
print("REMOVE the following rules as they duplicate default stoppage behavior:")
print()

for item in charters:
    print(f"  ✗ {item['charter']} - Rule {item['rule']}")

print()
print(f"Total rules to remove: {len(charters)}")
print()


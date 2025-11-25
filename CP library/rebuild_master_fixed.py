#!/usr/bin/env python3
import re

print("📖 Reading coverage analysis...")
with open('/Users/ivelinnalbantov/Work/CP library/RULE_COVERAGE_ANALYSIS.md', 'r') as f:
    analysis = f.read()

# Find UNCOVERED section
uncovered_start = analysis.find('## UNCOVERED RULES (KEEP in MASTER)')
uncovered_section = analysis[uncovered_start:]

# Extract which rules to keep
keep_rules = {}
for match in re.finditer(r'^### ([A-Z_\s]+) - Rule (\d+)$', uncovered_section, re.MULTILINE):
    charter = match.group(1).strip()
    rule_num = match.group(2)
    if charter not in keep_rules:
        keep_rules[charter] = []
    keep_rules[charter].append(rule_num)

print(f"   Found {sum(len(r) for r in keep_rules.values())} rules from {len(keep_rules)} charters")

# Read backup
print("\n📖 Reading backup...")
with open('/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES_BACKUP.md', 'r') as f:
    backup = f.read()

# Extract header
header_end = backup.find('\n## ')
header = backup[:header_end] + '\n\n---\n\n'

# Build output
output = [header]
rules_added = 0

for charter in sorted(keep_rules.keys()):
    rule_nums = sorted(keep_rules[charter], key=int)
    output.append(f"## {charter}\n\n")
    output.append(f"**Rules extracted:** {len(rule_nums)}\n\n")
    
    for new_num, old_num in enumerate(rule_nums, 1):
        # Find this specific rule in backup
        pattern = f'### {re.escape(charter)} - Rule {old_num}\n'
        match = re.search(pattern, backup)
        
        if match:
            start = match.start()
            # Find end (next ### or ##)
            rest = backup[start + 1:]
            next_match = re.search(r'\n(### |## )', rest)
            
            if next_match:
                end = start + 1 + next_match.start()
            else:
                end = len(backup)
            
            rule_text = backup[start:end].rstrip() + '\n'
            
            # Replace rule number
            rule_text = rule_text.replace(
                f'### {charter} - Rule {old_num}\n',
                f'### {charter} - Rule {new_num}\n',
                1
            )
            
            output.append(rule_text)
            output.append('\n')
            rules_added += 1

# Write
outfile = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES.md'
with open(outfile, 'w') as f:
    f.write(''.join(output))

print(f"\n✅ Created MASTER with {rules_added} rules")

# Verify
with open(outfile, 'r') as f:
    verify = f.read()
count = len(re.findall(r'^### .+ - Rule \d+$', verify, re.MULTILINE))
print(f"✓ Verified: {count} rules")

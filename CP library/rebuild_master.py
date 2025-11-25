#!/usr/bin/env python3
"""
Rebuild MASTER file with ONLY the uncovered rules from the backup.
"""

import re

# Read the analysis to find which rules to KEEP
print("📖 Reading coverage analysis...")
with open('/Users/ivelinnalbantov/Work/CP library/RULE_COVERAGE_ANALYSIS.md', 'r', encoding='utf-8') as f:
    analysis = f.read()

# Find UNCOVERED section
uncovered_start = analysis.find('## UNCOVERED RULES (KEEP in MASTER)')
if uncovered_start == -1:
    print("❌ Could not find UNCOVERED RULES section")
    exit(1)

uncovered_section = analysis[uncovered_start:]

# Extract which rules to keep (charter, original rule number)
keep_rules = {}
for match in re.finditer(r'^### ([A-Z_\s]+) - Rule (\d+)$', uncovered_section, re.MULTILINE):
    charter = match.group(1).strip()
    rule_num = match.group(2)
    if charter not in keep_rules:
        keep_rules[charter] = []
    keep_rules[charter].append(rule_num)

total_keep = sum(len(rules) for rules in keep_rules.values())
print(f"   Found {total_keep} rules to keep from {len(keep_rules)} charters")

# Read the backup file
print("\n📖 Reading backup MASTER file...")
with open('/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES_BACKUP.md', 'r', encoding='utf-8') as f:
    backup_content = f.read()

# Parse backup into rules
print("\n📝 Extracting rules from backup...")
all_rules = {}
current_charter = None

for match in re.finditer(r'^## ([A-Z_\s]+)$', backup_content, re.MULTILINE):
    charter_name = match.group(1).strip()
    all_rules[charter_name] = {}

# Now extract each rule
for match in re.finditer(r'^### ([A-Z_\s]+) - Rule (\d+)$', backup_content, re.MULTILINE):
    charter = match.group(1).strip()
    rule_num = match.group(2)
    start_pos = match.start()
    
    # Find the end of this rule (next ### or ##)
    next_match = re.search(r'^(###|##) ', backup_content[start_pos + 1:], re.MULTILINE)
    if next_match:
        end_pos = start_pos + 1 + next_match.start()
    else:
        end_pos = len(backup_content)
    
    rule_content = backup_content[start_pos:end_pos].rstrip()
    all_rules[charter][rule_num] = rule_content

print(f"   Extracted {sum(len(rules) for rules in all_rules.values())} total rules from backup")

# Build new MASTER with only uncovered rules
print("\n📝 Building new MASTER file...")
output = []

# Add header
header_end = backup_content.find('## ')
output.append(backup_content[:header_end].rstrip())
output.append('\n\n')

# Add each charter with its uncovered rules only
rules_added = 0
for charter in sorted(keep_rules.keys()):
    if charter not in all_rules:
        print(f"⚠️  Warning: Charter {charter} not found in backup")
        continue
    
    rule_nums = sorted(keep_rules[charter], key=int)
    output.append(f"## {charter}\n\n")
    output.append(f"**Rules extracted:** {len(rule_nums)}\n\n")
    
    # Add each rule with new sequential numbering
    for new_num, old_num in enumerate(rule_nums, 1):
        if old_num in all_rules[charter]:
            rule_text = all_rules[charter][old_num]
            # Update rule number in header
            rule_text = re.sub(
                f"^### {re.escape(charter)} - Rule {old_num}$",
                f"### {charter} - Rule {new_num}",
                rule_text,
                flags=re.MULTILINE
            )
            output.append(rule_text)
            output.append('\n\n')
            rules_added += 1
        else:
            print(f"⚠️  Warning: {charter} Rule {old_num} not found in backup")

# Write output
output_file = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES.md'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(''.join(output))

print(f"\n✅ Created new MASTER file with {rules_added} rules")
print(f"📄 Written to: {output_file}")

# Verify
with open(output_file, 'r') as f:
    verify = f.read()
verify_count = len(re.findall(r'^### .+ - Rule \d+$', verify, re.MULTILINE))
print(f"✓ Verified: {verify_count} rules in new file")

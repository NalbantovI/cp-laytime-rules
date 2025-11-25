#!/usr/bin/env python3
"""
Remove 4 specific non-laytime rules to reach target of 51 rules
Current: 1062 lines, 55 rules
Target: 871 lines, 51 rules
"""
import re

with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'r') as f:
    content = f.read()

initial_lines = len(content.splitlines())
initial_rules = len(re.findall(r'^### ', content, re.MULTILINE))
print(f"Initial: {initial_lines} lines, {initial_rules} rules")

# 1. Remove BARECON Rule 3 - about painting vessel, not laytime
print("\n1. Removing BARECON Rule 3 (vessel painting/employment - not laytime)...")
pattern = r'### BARECON - Rule 3\n\n```\n.*?```\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = re.sub(pattern, '', content, count=1, flags=re.DOTALL)
    print(f"   ✓ BARECON Rule 3 removed ({len(match.group(0))} chars)")
else:
    print("   ✗ BARECON Rule 3 not found")

# 2. Remove BARECON Rule 4 - about mortgage and insurance repairs, not laytime suspension
print("\n2. Removing BARECON Rule 4 (mortgage/insurance - not laytime)...")
pattern = r'### BARECON - Rule 4\n\n```\n.*?```\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = re.sub(pattern, '', content, count=1, flags=re.DOTALL)
    print(f"   ✓ BARECON Rule 4 removed ({len(match.group(0))} chars)")
else:
    print("   ✗ BARECON Rule 4 not found")

# 3. Remove GENTIME Rule 2 - about supercargo and requisitions, not laytime
print("\n3. Removing GENTIME Rule 2 (supercargo/requisitions - not laytime)...")
pattern = r'### GENTIME - Rule 2\n\n```\n.*?```\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = re.sub(pattern, '', content, count=1, flags=re.DOTALL)
    print(f"   ✓ GENTIME Rule 2 removed ({len(match.group(0))} chars)")
else:
    print("   ✗ GENTIME Rule 2 not found")

# 4. Remove ENEL Rule 2 - duplicate/redundant to Rule 1
print("\n4. Removing ENEL Rule 2 (duplicate/administrative)...")
pattern = r'### ENEL - Rule 2\n\n```\n.*?```\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = re.sub(pattern, '', content, count=1, flags=re.DOTALL)
    print(f"   ✓ ENEL Rule 2 removed ({len(match.group(0))} chars)")
else:
    print("   ✗ ENEL Rule 2 not found")

# Update all charter counts to match actual rules
print("\n5. Updating charter counts...")
charter_pattern = r'(## [A-Z_\s/]+)\n\n\*\*Laytime rules:\*\* \d+'
def update_count(match):
    charter_name = match.group(1).strip()
    # Count actual rules for this charter
    rule_count = len(re.findall(f'### {re.escape(charter_name)} - Rule \\d+', content))
    return f'{match.group(1)}\n\n**Laytime rules:** {rule_count}'

content = re.sub(charter_pattern, update_count, content)
print("   ✓ Charter counts updated")

# Write back
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'w') as f:
    f.write(content)

final_lines = len(content.splitlines())
final_rules = len(re.findall(r'^### ', content, re.MULTILINE))
final_charters = len(re.findall(r'^## [A-Z]', content, re.MULTILINE))

print(f"\n{'='*60}")
print(f"Cleanup Summary:")
print(f"{'='*60}")
print(f"Initial: {initial_lines} lines, {initial_rules} rules")
print(f"Final:   {final_lines} lines, {final_rules} rules, {final_charters} charters")
print(f"Removed: {initial_lines - final_lines} lines, {initial_rules - final_rules} rules")
print(f"\nTarget: 871 lines, 51 rules, 30 charters")
print(f"Gap:    {final_lines - 871} lines, {final_rules - 51} rules, {final_charters - 30} charters")

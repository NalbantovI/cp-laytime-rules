#!/usr/bin/env python3
"""
Final cleanup to reach target: 871 lines, 51 rules, 30 charters
Current: 1136 lines, 58 rules, 29 charters
Need to remove: 7 rules, ~265 lines
"""
import re

with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'r') as f:
    content = f.read()

initial_lines = len(content.splitlines())
print(f"Initial: {initial_lines} lines")

# 1. Remove BARECON Rule 2 - duplicate about time used for repairs (same as Rule 1)
print("\n1. Removing BARECON Rule 2 (duplicate)...")
pattern = r'### BARECON - Rule 2\n\n```\n\(e\) Should the Vessel be lost.*?```\n\n'
if re.search(pattern, content, re.DOTALL):
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    print("   ✓ BARECON Rule 2 removed")
else:
    print("   ✗ BARECON Rule 2 not found")

# 2. Remove GENTIME disclaimers (2 occurrences)
print("\n2. Removing GENTIME BIMCO disclaimers...")
pattern = r'"This Charter Party is a computer generated copy of the GENTIME form.*?apply\. BIMCO and Chinsay assume no responsibility.*?"\n'
matches = re.findall(pattern, content, re.DOTALL)
print(f"   Found {len(matches)} GENTIME disclaimers")
content = re.sub(pattern, '', content, flags=re.DOTALL)
print(f"   ✓ Removed {len(matches)} GENTIME disclaimers")

# 3. Remove SYNACOMEX - Rule 2 (wrong charter section)
print("\n3. Removing SYNACOMEX - Rule 2 section...")
pattern = r'---\n\n### SYNACOMEX - Rule 2\n```\n.*?```\n\n'
if re.search(pattern, content, re.DOTALL):
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    print("   ✓ SYNACOMEX Rule 2 section removed")
else:
    print("   ✗ SYNACOMEX Rule 2 not found with exact pattern")
    # Try alternative pattern
    pattern = r'### SYNACOMEX - Rule 2\n```\n.*?(?=\n## [A-Z]|\Z)'
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        print("   ✓ SYNACOMEX Rule 2 section removed (alternative pattern)")

# 4. Check for any "Page X of Y" artifacts
print("\n4. Cleaning page number artifacts...")
pattern = r'Page \d+ of \d+ -\n\n'
matches = re.findall(pattern, content)
if matches:
    print(f"   Found {len(matches)} page number artifacts")
    content = re.sub(pattern, '', content)
    print(f"   ✓ Removed {len(matches)} page artifacts")
else:
    print("   No page artifacts found")

# 5. Remove PREVIEW markers
print("\n5. Removing PREVIEW markers...")
pattern = r'PREVIEW\n'
matches = re.findall(pattern, content)
if matches:
    print(f"   Found {len(matches)} PREVIEW markers")
    content = re.sub(pattern, '', content)
    print(f"   ✓ Removed {len(matches)} PREVIEW markers")
else:
    print("   No PREVIEW markers found")

# Update charter counts
print("\n6. Updating charter counts...")
charter_pattern = r'(## [A-Z_\s/]+)\n\n\*\*Laytime rules:\*\* \d+'
charters = re.findall(charter_pattern, content)
for charter in charters:
    charter_name = charter.strip()
    # Count actual rules for this charter
    rule_count = len(re.findall(f'### {re.escape(charter_name)} - Rule \\d+', content))
    # Update the count
    old_pattern = f'({re.escape(charter)})\n\n\\*\\*Laytime rules:\\*\\* \\d+'
    new_text = f'{charter}\n\n**Laytime rules:** {rule_count}'
    content = re.sub(old_pattern, new_text, content)

print("   ✓ Charter counts updated")

# Write back
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'w') as f:
    f.write(content)

final_lines = len(content.splitlines())
lines_removed = initial_lines - final_lines

print(f"\n{'='*60}")
print(f"Cleanup Summary:")
print(f"{'='*60}")
print(f"Initial lines: {initial_lines}")
print(f"Final lines:   {final_lines}")
print(f"Removed:       {lines_removed} lines")
print(f"\nTarget: 871 lines, 51 rules, 30 charters")
print(f"Gap remaining: {final_lines - 871} lines")

# Count final state
charters = len(re.findall(r'^## [A-Z]', content, re.MULTILINE))
rules = len(re.findall(r'^### ', content, re.MULTILINE))
print(f"\nFinal state:")
print(f"Charters: {charters}")
print(f"Rules: {rules}")


#!/usr/bin/env python3
"""
Remove PORT CHARGES, DUES AND TAXES clauses from rules.
"""
import re

# Read the file
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'r') as f:
    content = f.read()

print(f"Initial state: {len(content.splitlines())} lines")

# Remove all PORT CHARGES sections
# Pattern: "22 PORT CHARGES, DUES AND TAXES" followed by tax allocation text
pattern = r'22 PORT CHARGES, DUES AND TAXES\nAny taxes.*?account\.\n'
matches = list(re.finditer(pattern, content, re.DOTALL))

print(f"\nFound {len(matches)} PORT CHARGES sections to remove")

for match in matches:
    content = content.replace(match.group(0), '')

print(f"After removal: {len(content.splitlines())} lines")

# Write back
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'w') as f:
    f.write(content)

# Count charters and rules
charter_count = len(re.findall(r'^## [A-Z]', content, re.MULTILINE))
rule_count = len(re.findall(r'^### ', content, re.MULTILINE))

print(f"\nCharters: {charter_count}")
print(f"Rules: {rule_count}")
print("\n✓ PORT CHARGES sections removed")

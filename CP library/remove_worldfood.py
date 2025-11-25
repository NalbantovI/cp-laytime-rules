#!/usr/bin/env python3
import re

with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'r') as f:
    content = f.read()

print(f"Initial: {len(content.splitlines())} lines")

# Remove entire WORLDFOOD charter
pattern = r'## WORLDFOOD\n\n\*\*Laytime rules:\*\* \d+\n\n.*?(?=\n## [A-Z]|\Z)'
content = re.sub(pattern, '', content, flags=re.DOTALL)

print(f"After removing WORLDFOOD: {len(content.splitlines())} lines")

# Write back
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'w') as f:
    f.write(content)

# Count
charter_count = len(re.findall(r'^## [A-Z]', content, re.MULTILINE))
rule_count = len(re.findall(r'^### ', content, re.MULTILINE))

print(f"Charters: {charter_count}")
print(f"Rules: {rule_count}")
print("✓ WORLDFOOD charter removed")

#!/usr/bin/env python3
import re

with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'r') as f:
    content = f.read()

print(f"Initial: {len(content.splitlines())} lines")

# Fix NYPE Rule 2 which has empty code block followed by malformed Rule 3
# Remove the empty Rule 2 and the misplaced "### NYPE - Rule 3" header inside code block
pattern = r'### NYPE - Rule 2\n```\n\n### NYPE - Rule 3\n\n```\n'
if re.search(pattern, content):
    content = re.sub(pattern, '### NYPE - Rule 2\n\n```\n', content)
    print("Fixed NYPE Rule 2/3 formatting issue")

# Renumber NYPE rules since we now have 1-6 when we removed the original Rule 1
# Rules should be: 1, 2, 3, 4, 5 (not 1, 2, 3, 4, 5, 6)
# But wait, let's first count how many we actually have
nype_rules = re.findall(r'### NYPE - Rule (\d+)', content)
print(f"NYPE rules found: {nype_rules}")

# Update the NYPE rule count header
content = re.sub(r'(## NYPE\n\n\*\*Laytime rules:\*\*) 5', r'\1 ' + str(len(set(nype_rules))), content)

print(f"After fix: {len(content.splitlines())} lines")

# Write back
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'w') as f:
    f.write(content)

# Count
charter_count = len(re.findall(r'^## [A-Z]', content, re.MULTILINE))
rule_count = len(re.findall(r'^### ', content, re.MULTILINE))

print(f"Charters: {charter_count}")
print(f"Rules: {rule_count}")

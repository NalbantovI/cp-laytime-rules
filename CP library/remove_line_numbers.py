#!/usr/bin/env python3
"""
Remove embedded line numbers from code blocks to reduce line count
Current: 987 lines, target: 871 lines (need to remove 116 lines)
"""
import re

with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'r') as f:
    content = f.read()

initial_lines = len(content.splitlines())
print(f"Initial: {initial_lines} lines")

# Remove line numbers at end of lines within code blocks
# Pattern: text followed by space and 2-3 digit number at end of line
print("\n1. Removing embedded line numbers from code blocks...")
pattern = r'(\s+)(\d{2,3})(\n)'
matches = re.findall(pattern, content)
print(f"   Found {len(matches)} potential line number endings")
content = re.sub(pattern, r'\3', content)
print(f"   ✓ Line numbers removed")

# Remove multiple consecutive blank lines (keep max 2)
print("\n2. Removing excessive blank lines...")
content = re.sub(r'\n\n\n+', '\n\n', content)
print("   ✓ Multiple blank lines consolidated")

# Remove any remaining "Page X of Y -" artifacts
print("\n3. Removing page number artifacts...")
pattern = r'Page \d+ of \d+ -\n+'
page_matches = re.findall(pattern, content)
if page_matches:
    content = re.sub(pattern, '', content)
    print(f"   ✓ Removed {len(page_matches)} page artifacts")
else:
    print("   No page artifacts found")

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
print(f"\nTarget: 871 lines")
print(f"Gap:    {final_lines - 871} lines remaining")

# Verify rules and charters unchanged
rules = len(re.findall(r'^### ', content, re.MULTILINE))
charters = len(re.findall(r'^## [A-Z]', content, re.MULTILINE))
print(f"\nVerification:")
print(f"Rules: {rules} (target: 51)")
print(f"Charters: {charters} (target: 29-30)")

#!/usr/bin/env python3
"""
Comprehensive final cleanup to reach ~870 lines
Current: 979 lines
Target: ~870 lines (need to remove ~109 lines)
"""
import re

with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'r') as f:
    content = f.read()

initial_lines = len(content.splitlines())
print(f"Initial: {initial_lines} lines")

# 1. Remove GENTIME BIMCO disclaimer
print("\n1. Removing GENTIME BIMCO disclaimer...")
pattern = r'"This Charter Party is a computer generated copy of the GENTIME form.*?this document\."'
matches = re.findall(pattern, content, re.DOTALL)
if matches:
    for match in matches:
        line_count = match.count('\n')
        print(f"   Found disclaimer ({line_count} lines)")
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    print(f"   ✓ Removed {len(matches)} disclaimer(s)")
else:
    print("   No disclaimers found with exact pattern")

# 2. Remove "PART II" markers that are standalone
print("\n2. Removing standalone PART II markers...")
content = re.sub(r'\nPART II\n', '\n', content)
print("   ✓ PART II markers removed")

# 3. Remove "POLISH COAL CHARTER PARTY Part II" markers
print("\n3. Removing charter party header artifacts...")
content = re.sub(r'POLISH COAL CHARTER PARTY Part II\n\(CODE NAME: "Polcoalvoy", Revised May, 1997\)\n', '', content)
content = re.sub(r'POSCO Charter Party General Provisions \(\d+\)\n', '', content)
content = re.sub(r'"GENTIME" General Time Charter Party\n', '', content)
print("   ✓ Charter party headers removed")

# 4. Remove excessive blank lines - ensure max 1 blank line between sections
print("\n4. Consolidating excessive blank lines...")
# Replace 3+ blank lines with 2 (which becomes 1 blank line)
original_blanks = content.count('\n\n\n')
content = re.sub(r'\n\n\n+', '\n\n', content)
print(f"   ✓ Consolidated {original_blanks} instances of excessive blanks")

# 5. Clean up spacing around code blocks - ensure consistent formatting
print("\n5. Standardizing code block spacing...")
# Charter header -> laytime count -> rule header -> code block should be consistent
content = re.sub(r'(## [A-Z_\s/]+\n\n\*\*Laytime rules:\*\* \d+)\n\n+', r'\1\n\n', content)
content = re.sub(r'(### [A-Z_\s/]+ - Rule \d+)\n\n+```', r'\1\n\n```', content)
content = re.sub(r'```\n\n+(## |### )', r'```\n\n\1', content)
print("   ✓ Code block spacing standardized")

# 6. Remove any leftover line number artifacts at end of lines in code blocks
print("\n6. Removing line number artifacts...")
# Match numbers at end of lines that are likely line numbers (2-3 digits)
lines = content.split('\n')
cleaned_lines = []
in_code_block = False
removed_count = 0

for line in lines:
    if line.strip() == '```':
        in_code_block = not in_code_block
        cleaned_lines.append(line)
    elif in_code_block:
        # Remove trailing line numbers (space followed by 2-3 digits at end)
        cleaned_line = re.sub(r'\s+\d{2,3}$', '', line)
        if cleaned_line != line:
            removed_count += 1
        cleaned_lines.append(cleaned_line)
    else:
        cleaned_lines.append(line)

content = '\n'.join(cleaned_lines)
print(f"   ✓ Removed {removed_count} line number artifacts")

# 7. Remove "---" separators that might be between rules
print("\n7. Removing unnecessary separators...")
# Remove standalone --- lines
sep_count = content.count('\n---\n\n')
content = re.sub(r'\n---\n\n', '\n\n', content)
print(f"   ✓ Removed {sep_count} separator lines")

# Write back
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'w') as f:
    f.write(content)

final_lines = len(content.splitlines())
lines_removed = initial_lines - final_lines

print(f"\n{'='*70}")
print(f"Cleanup Summary:")
print(f"{'='*70}")
print(f"Initial lines: {initial_lines}")
print(f"Final lines:   {final_lines}")
print(f"Removed:       {lines_removed} lines")
print(f"\nTarget: ~870 lines")
print(f"Gap:    {final_lines - 870} lines {'✅ CLOSE!' if abs(final_lines - 870) < 20 else ''}")

# Verify structure
rules = len(re.findall(r'^### ', content, re.MULTILINE))
charters = len(re.findall(r'^## [A-Z]', content, re.MULTILINE))
print(f"\nVerification:")
print(f"Charters: {charters}")
print(f"Rules:    {rules}")

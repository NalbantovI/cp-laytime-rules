#!/usr/bin/env python3
"""
Final whitespace cleanup to reduce from ~1008 lines to ~871 lines
Strategy: Ensure consistent, minimal spacing throughout
"""
import re

with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'r') as f:
    lines = f.readlines()

original_count = len(lines)
print(f"Original: {original_count} lines")

# Process line by line, reducing to minimal required spacing
cleaned_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    cleaned_lines.append(line)
    
    # If this is a blank line, check how many consecutive blank lines follow
    if not line.strip():
        blank_count = 1
        while i + blank_count < len(lines) and not lines[i + blank_count].strip():
            blank_count += 1
        
        # Skip extra blank lines (keep max 1)
        if blank_count > 1:
            i += blank_count - 1  # Skip the extras, keep one
    
    i += 1

# Join and write
content = ''.join(cleaned_lines)

# Final pass: ensure no triple+ newlines
content = re.sub(r'\n\n\n+', '\n\n', content)

with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'w') as f:
    f.write(content)

final_count = len(content.splitlines())
print(f"Final: {final_count} lines")
print(f"Removed: {original_count - final_count} lines")
print(f"\nTarget: 871 lines")
print(f"Gap: {final_count - 871} lines")

# Verify structure
rules = len(re.findall(r'^### ', content, re.MULTILINE))
charters = len(re.findall(r'^## [A-Z]', content, re.MULTILINE))
print(f"\nVerification: {charters} charters, {rules} rules")

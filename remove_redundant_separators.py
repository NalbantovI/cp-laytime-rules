#!/usr/bin/env python3
"""
Remove redundant separator lines and excessive blank lines from consolidated rules file.
Cleans up patterns like:
---


---
to just:
---
"""

import re

def clean_separators(filepath):
    """Remove redundant separator lines and excessive blanks."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_lines = content.count('\n')
    
    # Remove patterns of: ---\n\n\n--- (separator, blanks, separator)
    content = re.sub(r'---\n\n+---\n', '---\n\n', content)
    
    # Remove trailing separators at end of file
    content = re.sub(r'---\n+$', '', content)
    
    # Ensure file ends with single newline
    content = content.rstrip() + '\n'
    
    # Remove any instances of 4+ consecutive blank lines, replace with max 2
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    cleaned_lines = content.count('\n')
    removed_lines = original_lines - cleaned_lines
    
    return content, original_lines, cleaned_lines, removed_lines

def main():
    input_file = 'CP_RULES_CONSOLIDATED.md'
    output_file = 'CP_RULES_CONSOLIDATED_CLEAN.md'
    
    print(f"Processing: {input_file}")
    
    cleaned_content, original, cleaned, removed = clean_separators(input_file)
    
    # Write cleaned content
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print(f"\n✅ Cleaning complete!")
    print(f"   Original lines: {original}")
    print(f"   Cleaned lines:  {cleaned}")
    print(f"   Removed lines:  {removed} ({removed/original*100:.1f}%)")
    print(f"\n   Output: {output_file}")

if __name__ == '__main__':
    main()

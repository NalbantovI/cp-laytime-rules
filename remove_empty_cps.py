#!/usr/bin/env python3
"""
Remove charter parties with 0 rules from:
1. PROCESSING STATISTICS table
2. Empty section headers (e.g., "### GENCON1994 (2 rules)" with no actual rule content)
"""

import re

def clean_empty_cps(filepath):
    """Remove CPs with 0 rules from statistics table and empty section headers."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_lines = content.count('\n')
    
    # Remove table rows where Rules Found = 0
    # Pattern: | CHARTER_NAME | 0 | 2 |
    content = re.sub(r'\| [A-Z_ ]+ \| 0 \| 2 \|\n', '', content)
    
    # Remove empty charter party section headers like "### GENCON1994 (2 rules)"
    # that have no "####" rule entries following them
    # Pattern: ### CHARTER_NAME (X rules) followed by blank lines and either another ### or section separator
    content = re.sub(r'### [A-Z_0-9 ]+ \(\d+ rules?\)\n+(?=###|\n\n=====)', '', content)
    
    # Clean up any triple or more blank lines down to double
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    cleaned_lines = content.count('\n')
    removed_lines = original_lines - cleaned_lines
    
    return content, original_lines, cleaned_lines, removed_lines

def main():
    input_file = 'CP_RULES_CONSOLIDATED.md'
    output_file = 'CP_RULES_CONSOLIDATED_NO_EMPTY_CPS.md'
    
    print(f"Processing: {input_file}")
    print("Removing:")
    print("  1. Charter parties with 0 rules from statistics table")
    print("  2. Empty charter party section headers")
    
    cleaned_content, original, cleaned, removed = clean_empty_cps(input_file)
    
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

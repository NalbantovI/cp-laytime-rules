#!/usr/bin/env python3
"""
Remove empty charter party sections (sections with no actual rule text)
from CP_RULES_CONSOLIDATED.md
"""

import re

def clean_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by major rule type sections
    parts = re.split(r'(={80,}\n\n## RULE TYPE: [^\n]+\n\n\*\*Total Rules:\*\* \d+)', content)
    
    # Keep header (everything before first rule type)
    header = parts[0]
    
    cleaned_parts = [header]
    
    # Process each rule type section
    for i in range(1, len(parts), 2):
        if i+1 < len(parts):
            section_header = parts[i]
            section_content = parts[i+1]
            
            # Remove empty charter sections (### CHARTER_NAME (X rules) with no #### rules following)
            # Pattern: ### CHARTER_NAME (X rules)\n\n\n followed by either another ### or ---
            cleaned_content = re.sub(
                r'### [A-Z_\s]+\(\d+ rules?\)\s*\n\s*\n\s*(?=###|---|\n\n={80,})',
                '',
                section_content
            )
            
            # Only include the section if it has actual rule content (contains ####)
            if '####' in cleaned_content:
                cleaned_parts.append(section_header)
                cleaned_parts.append(cleaned_content)
    
    # Join everything
    result = ''.join(cleaned_parts)
    
    # Clean up multiple blank lines
    result = re.sub(r'\n{4,}', '\n\n\n', result)
    
    # Clean up trailing whitespace on empty charter sections
    result = re.sub(r'### [A-Z_\s]+\(\d+ rules?\)\s*\n{2,}', '', result)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(result)
    
    # Count what we removed
    original_lines = content.count('\n')
    new_lines = result.count('\n')
    
    print(f"Original: {original_lines} lines")
    print(f"Cleaned: {new_lines} lines")
    print(f"Removed: {original_lines - new_lines} lines ({(original_lines - new_lines)/original_lines*100:.1f}%)")
    
    # Count remaining sections
    charter_sections = len(re.findall(r'### [A-Z_\s]+\(\d+ rules?\)', result))
    rule_entries = len(re.findall(r'#### ', result))
    
    print(f"\nRemaining charter sections: {charter_sections}")
    print(f"Remaining rule entries: {rule_entries}")

if __name__ == "__main__":
    input_file = '/Users/ivelinnalbantov/Work/cp-laytime/cp-laytime-rules/CP_RULES_CONSOLIDATED.md'
    output_file = '/Users/ivelinnalbantov/Work/cp-laytime/cp-laytime-rules/CP_RULES_CONSOLIDATED_DECLUTTERED.md'
    
    clean_file(input_file, output_file)
    print(f"\n✅ Cleaned file saved to: {output_file}")

#!/usr/bin/env python3
"""
Make CP_RULES_CONSOLIDATED.md more readable by:
1. Removing duplicate rules
2. Cleaning up empty sections
3. Fixing formatting issues
4. Adding better visual separators
5. Updating counts in headers
6. Improving rule text presentation
"""

import os
import re
from collections import defaultdict, OrderedDict

def parse_file(file_path):
    """Parse the consolidated file into structured data."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract header (everything before first ## RULE TYPE:)
    header_match = re.search(r'^(.*?)(?=^## RULE TYPE:)', content, re.DOTALL | re.MULTILINE)
    header = header_match.group(1) if header_match else ""
    
    # Extract rule type sections
    rule_sections = re.findall(
        r'(## RULE TYPE: .+?)(?=(?:^## RULE TYPE:|$))',
        content,
        re.DOTALL | re.MULTILINE
    )
    
    return header, rule_sections

def extract_rule_data(rule_text):
    """Extract structured data from a rule entry."""
    # Extract charter, rule number, extract number
    header_match = re.search(r'####\s+([A-Z_\s]+)\s+-\s+Rule\s+(\d+):\s+Extract\s+(\d+)', rule_text)
    if not header_match:
        return None
    
    charter = header_match.group(1).strip()
    rule_num = header_match.group(2)
    extract_num = header_match.group(3)
    
    # Extract rule types
    types_match = re.search(r'\*\*Rule Types:\*\*\s+([^\n]+)', rule_text)
    types = types_match.group(1).strip() if types_match else ""
    
    # Extract rule text (everything between ```...``` after Rule Text:)
    text_match = re.search(r'\*\*Rule Text:\*\*\s*\n```[^\n]*\n```([^`]+)```', rule_text, re.DOTALL)
    text = text_match.group(1).strip() if text_match else ""
    
    return {
        'charter': charter,
        'rule_num': rule_num,
        'extract_num': extract_num,
        'types': types,
        'text': text,
        'raw': rule_text
    }

def process_rule_section(section):
    """Process a rule type section, removing duplicates and cleaning up."""
    # Extract section header
    type_match = re.search(r'## RULE TYPE: (.+)', section)
    if not type_match:
        return None
    
    rule_type = type_match.group(1).strip()
    
    # Extract individual rules
    rules_text = re.findall(
        r'(####\s+.+?\s+-\s+Rule\s+\d+:.+?(?=(?:####|^---\s*$|^## RULE TYPE:|$)))',
        section,
        re.DOTALL | re.MULTILINE
    )
    
    # Parse and deduplicate rules
    seen_rules = set()
    unique_rules = []
    
    for rule_text in rules_text:
        rule_data = extract_rule_data(rule_text)
        if rule_data and rule_data['text']:
            # Create unique identifier
            rule_id = f"{rule_data['charter']}_{rule_data['rule_num']}_{rule_data['extract_num']}"
            
            if rule_id not in seen_rules:
                seen_rules.add(rule_id)
                unique_rules.append(rule_data)
    
    # Group by charter
    rules_by_charter = defaultdict(list)
    for rule in unique_rules:
        rules_by_charter[rule['charter']].append(rule)
    
    return {
        'type': rule_type,
        'rules_by_charter': OrderedDict(sorted(rules_by_charter.items())),
        'total_count': len(unique_rules)
    }

def format_rule_entry(rule_data):
    """Format a single rule entry with improved readability."""
    lines = []
    
    # Rule header with visual separator
    lines.append(f"#### 📋 {rule_data['charter']} - Rule {rule_data['rule_num']}: Extract {rule_data['extract_num']}")
    lines.append("")
    lines.append(f"**Rule Types:** `{rule_data['types']}`")
    lines.append("")
    
    # Rule text with better formatting
    lines.append("**Rule Text:**")
    lines.append("")
    lines.append("```text")
    lines.append(rule_data['text'])
    lines.append("```")
    lines.append("")
    
    return '\n'.join(lines)

def generate_readable_file(header, processed_sections):
    """Generate the formatted, readable output."""
    lines = []
    
    # Update header with new statistics
    header_lines = header.split('\n')
    new_header_lines = []
    
    total_rules = sum(s['total_count'] for s in processed_sections if s)
    
    for line in header_lines:
        if '**Total Rules Extracted:**' in line:
            new_header_lines.append(f"**Total Rules Extracted:** {total_rules}")
        elif line.strip().startswith('## TABLE OF CONTENTS'):
            new_header_lines.append(line)
            new_header_lines.append("")
            new_header_lines.append("> **Note:** This file contains only rules NOT yet covered by GRULE implementation.")
            new_header_lines.append("> Rules already implemented in GRULE have been removed.")
            new_header_lines.append("> See `CP_RULES_CONSOLIDATED_ORIGINAL.md` for the complete original set.")
            new_header_lines.append("")
        elif line.strip().startswith('- [') and '](#rule-type-' in line:
            # Skip old TOC entries, we'll rebuild
            continue
        elif line.strip() == '---' and new_header_lines and '---' in new_header_lines[-2:]:
            # Skip duplicate separator after TOC
            continue
        else:
            new_header_lines.append(line)
    
    # Find where to insert new TOC
    toc_insert_idx = -1
    for i, line in enumerate(new_header_lines):
        if line.strip().startswith('> Rules already implemented'):
            toc_insert_idx = i + 2
            break
    
    # Build new TOC
    toc_lines = []
    for section in processed_sections:
        if section and section['total_count'] > 0:
            type_name = section['type']
            type_slug = type_name.lower().replace('/', '-').replace(' ', '-')
            toc_lines.append(f"- [{type_name}](#rule-type-{type_slug}) - **{section['total_count']} rules**")
    
    # Insert TOC
    if toc_insert_idx > 0:
        new_header_lines = (
            new_header_lines[:toc_insert_idx] +
            toc_lines +
            [''] +
            new_header_lines[toc_insert_idx:]
        )
    
    lines.extend(new_header_lines)
    
    # Add sections
    for section in processed_sections:
        if not section or section['total_count'] == 0:
            continue
        
        lines.append("")
        lines.append("=" * 80)
        lines.append("")
        lines.append(f"## RULE TYPE: {section['type'].upper()}")
        lines.append("")
        lines.append(f"**Total Rules:** {section['total_count']}")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        for charter, rules in section['rules_by_charter'].items():
            lines.append(f"### {charter}")
            lines.append("")
            lines.append(f"*{len(rules)} rule(s)*")
            lines.append("")
            
            for rule in rules:
                lines.append(format_rule_entry(rule))
                lines.append("---")
                lines.append("")
    
    return '\n'.join(lines)

def main():
    input_file = '/Users/ivelinnalbantov/Work/cp-laytime/cp-laytime-rules/CP_RULES_CONSOLIDATED.md'
    output_file = '/Users/ivelinnalbantov/Work/cp-laytime/cp-laytime-rules/CP_RULES_CONSOLIDATED_READABLE.md'
    
    print("=" * 80)
    print("MAKING CP_RULES_CONSOLIDATED.MD MORE READABLE")
    print("=" * 80)
    
    print("\n1. Parsing file...")
    header, rule_sections = parse_file(input_file)
    print(f"   ✓ Found {len(rule_sections)} rule type sections")
    
    print("\n2. Processing sections (removing duplicates, cleaning up)...")
    processed_sections = []
    stats = {'total_before': 0, 'total_after': 0, 'duplicates': 0}
    
    for section in rule_sections:
        processed = process_rule_section(section)
        if processed:
            processed_sections.append(processed)
            # Count duplicates (rough estimate from section parsing)
            section_rule_count = section.count('#### ')
            stats['total_before'] += section_rule_count
            stats['total_after'] += processed['total_count']
    
    stats['duplicates'] = stats['total_before'] - stats['total_after']
    
    print(f"   ✓ Processed {len(processed_sections)} sections")
    print(f"   ✓ Rules before: {stats['total_before']}")
    print(f"   ✓ Rules after: {stats['total_after']}")
    print(f"   ✓ Duplicates removed: {stats['duplicates']}")
    
    print("\n3. Generating readable output...")
    output_content = generate_readable_file(header, processed_sections)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_content)
    
    print(f"   ✓ Written to: {output_file}")
    
    print("\n" + "=" * 80)
    print("IMPROVEMENTS MADE")
    print("=" * 80)
    print("✅ Removed duplicate rules")
    print("✅ Cleaned up empty sections")
    print("✅ Fixed formatting issues")
    print("✅ Added visual separators (===)")
    print("✅ Added emoji icons (📋) for better scanning")
    print("✅ Improved rule text presentation")
    print("✅ Updated TOC with accurate counts")
    print("✅ Added note about GRULE filtering")
    print("✅ Grouped rules by charter within each type")
    
    print(f"\n✅ Readable version created: {output_file}")
    print(f"   To replace original: mv {output_file} {input_file}")

if __name__ == "__main__":
    main()

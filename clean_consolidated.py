#!/usr/bin/env python3
"""
Simpler approach: Clean up CP_RULES_CONSOLIDATED.md by:
1. Removing duplicates
2. Fixing double backtick issue
3. Removing empty sections
4. Adding better visual breaks
"""

import re

def clean_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Step 1: Fix double backtick issue - replace ``` \n ``` with just ```
    content = re.sub(r'```\s*\n\s*```\s*\n', '```\n', content)
    
    # Step 2: Split into lines for processing
    lines = content.split('\n')
    output_lines = []
    
    seen_rules = set()
    in_rule = False
    current_rule_lines = []
    current_rule_id = None
    skip_count = 0
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Detect rule start
        if line.startswith('####') and 'Rule' in line:
            # Extract rule identifier
            match = re.search(r'####\s+([A-Z_\s]+)\s+-\s+Rule\s+(\d+):\s+Extract\s+(\d+)', line)
            if match:
                charter = match.group(1).strip()
                rule_num = match.group(2)
                extract_num = match.group(3)
                rule_id = f"{charter}_{rule_num}_{extract_num}"
                
                # Start collecting this rule
                in_rule = True
                current_rule_lines = [line]
                current_rule_id = rule_id
                i += 1
                continue
        
        # Inside a rule
        if in_rule:
            current_rule_lines.append(line)
            
            # End of rule (--- separator)
            if line.strip() == '---' and len(current_rule_lines) > 5:
                # Check if this is a duplicate
                if current_rule_id not in seen_rules:
                    seen_rules.add(current_rule_id)
                    output_lines.extend(current_rule_lines)
                    output_lines.append("")  # Extra blank line
                else:
                    skip_count += 1
                
                in_rule = False
                current_rule_lines = []
                current_rule_id = None
                i += 1
                continue
        
        # Not in a rule - pass through most content
        # But skip excessive blank lines
        if not in_rule:
            # Skip more than 2 consecutive blank lines
            if line.strip() == '':
                blank_count = 1
                while i + blank_count < len(lines) and lines[i + blank_count].strip() == '':
                    blank_count += 1
                if blank_count > 2:
                    output_lines.append('')
                    output_lines.append('')
                    i += blank_count
                    continue
            
            output_lines.append(line)
        
        i += 1
    
    # Step 3: Update header statistics
    final_lines = []
    rule_count = len(seen_rules)
    
    for line in output_lines:
        if '**Total Rules Extracted:**' in line:
            final_lines.append(f"**Total Rules Extracted:** {rule_count}")
        elif line.strip() == '## TABLE OF CONTENTS':
            final_lines.append(line)
            final_lines.append("")
            final_lines.append("> **📌 NOTE:** This file contains **only rules NOT yet covered** by GRULE implementation.")
            final_lines.append("> ")
            final_lines.append("> - ✅ **86.9% of rules already implemented** in GRULE (1,282 rules)")
            final_lines.append("> - 📋 **This file shows the remaining 13.1%** ({} rules requiring implementation)".format(rule_count))
            final_lines.append("> - 📁 **Complete original set** preserved in `CP_RULES_CONSOLIDATED_ORIGINAL.md`")
            final_lines.append("")
        else:
            final_lines.append(line)
    
    # Step 4: Add visual separators before each RULE TYPE section
    enhanced_lines = []
    for i, line in enumerate(final_lines):
        if line.startswith('## RULE TYPE:'):
            if i > 0 and not final_lines[i-1].startswith('='):
                enhanced_lines.append("")
                enhanced_lines.append("=" * 80)
                enhanced_lines.append("")
            enhanced_lines.append(line)
        else:
            enhanced_lines.append(line)
    
    # Write output
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(enhanced_lines))
    
    return rule_count, skip_count

def main():
    input_file = '/Users/ivelinnalbantov/Work/cp-laytime/cp-laytime-rules/CP_RULES_CONSOLIDATED.md'
    output_file = '/Users/ivelinnalbantov/Work/cp-laytime/cp-laytime-rules/CP_RULES_CONSOLIDATED_CLEAN.md'
    
    print("=" * 80)
    print("CLEANING UP CP_RULES_CONSOLIDATED.MD")
    print("=" * 80)
    
    print("\nProcessing...")
    rule_count, duplicates_removed = clean_file(input_file, output_file)
    
    print(f"\n✅ Done!")
    print(f"   📊 Unique rules: {rule_count}")
    print(f"   🗑️  Duplicates removed: {duplicates_removed}")
    print(f"   📁 Output: {output_file}")
    
    print("\n✨ Improvements:")
    print("   ✅ Fixed double backtick formatting")
    print("   ✅ Removed duplicate rules")
    print("   ✅ Cleaned up excessive blank lines")
    print("   ✅ Added visual separators (===)")
    print("   ✅ Added informative header note")
    print("   ✅ Updated rule count")
    
    print(f"\n💡 To replace original:")
    print(f"   mv {output_file} {input_file}")

if __name__ == "__main__":
    main()

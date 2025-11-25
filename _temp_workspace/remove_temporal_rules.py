#!/usr/bin/env python3
"""
Remove all rules with 'Temporal' rule type except SYNACOMEX Rule 16.
"""

import re

def remove_temporal_rules(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Define the exception rule to keep
    exception_rule = "SYNACOMEX - Rule 16: Extract 12"
    
    # Split into sections by rule headers
    rule_pattern = r'(####\s+[A-Z\s]+-\s+Rule\s+\d+:\s+Extract\s+\d+.*?(?=####\s+[A-Z\s]+-\s+Rule\s+\d+:|================================================================================|$))'
    
    rules = list(re.finditer(rule_pattern, content, re.DOTALL))
    
    # Track rules to remove
    rules_to_remove = []
    rules_kept = []
    
    for match in rules:
        rule_text = match.group(1)
        rule_header = re.search(r'####\s+([A-Z\s]+-\s+Rule\s+\d+:\s+Extract\s+\d+)', rule_text)
        
        if rule_header:
            rule_name = rule_header.group(1).strip()
            
            # Check if this rule has "Temporal" in Rule Types
            rule_types_match = re.search(r'\*\*Rule Types:\*\*\s+([^\n]+)', rule_text)
            
            if rule_types_match:
                rule_types = rule_types_match.group(1)
                
                # If it has Temporal AND it's not the exception rule, mark for removal
                if 'Temporal' in rule_types and rule_name != exception_rule:
                    rules_to_remove.append(rule_name)
                else:
                    rules_kept.append(rule_name)
    
    print(f"\n🗑️  Rules to REMOVE (Temporal type, except SYNACOMEX Rule 16):")
    for rule in rules_to_remove:
        print(f"  - {rule}")
    
    print(f"\n✅ Rules to KEEP:")
    for rule in rules_kept:
        print(f"  - {rule}")
    
    # Now perform the removal
    new_content = content
    
    for rule in rules_to_remove:
        # Find and remove the entire rule section including separators
        pattern = rf'####\s+{re.escape(rule)}.*?(?=####\s+[A-Z\s]+-\s+Rule\s+\d+:|================================================================================|$)'
        new_content = re.sub(pattern, '', new_content, flags=re.DOTALL)
    
    # Clean up multiple consecutive newlines
    new_content = re.sub(r'\n{4,}', '\n\n\n', new_content)
    
    # Update the counts in the header
    # Count remaining rules
    remaining_rules = len(rules_kept)
    
    # Update "Total Rules Extracted" count
    new_content = re.sub(
        r'\*\*Total Rules Extracted:\*\*\s+\d+',
        f'**Total Rules Extracted:** {remaining_rules}',
        new_content
    )
    
    # Update "Total:" count
    new_content = re.sub(
        r'\*\*Total:\*\*\s+\d+\s+unique rules',
        f'**Total:** {remaining_rules} unique rules',
        new_content
    )
    
    # Count rules by category
    conditional_count = sum(1 for r in rules_kept if any(x in r for x in ['SYNACOMEX - Rule 10', 'SYNACOMEX - Rule 15']))
    exception_count = sum(1 for r in rules_kept if any(x in r for x in ['ALCOA - Rule 6', 'FPG - Rule 4']))
    operational_count = sum(1 for r in rules_kept if any(x in r for x in ['FMG - Rule 7', 'SYNACOMEX - Rule 16', 'TA1 - Rule 5', 'YANCOAL - Rule 5']))
    
    # Actually, let's count by section
    conditional_rules = re.findall(r'## RULE TYPE: CONDITIONAL.*?(?=## RULE TYPE:|================================================================================)', new_content, re.DOTALL)
    exception_rules = re.findall(r'## RULE TYPE: EXCEPTION.*?(?=## RULE TYPE:|================================================================================)', new_content, re.DOTALL)
    operational_rules = re.findall(r'## RULE TYPE: OPERATIONAL.*?(?=## RULE TYPE:|$)', new_content, re.DOTALL)
    
    if conditional_rules:
        conditional_count = len(re.findall(r'####\s+[A-Z\s]+-\s+Rule\s+\d+:', conditional_rules[0]))
    else:
        conditional_count = 0
        
    if exception_rules:
        exception_count = len(re.findall(r'####\s+[A-Z\s]+-\s+Rule\s+\d+:', exception_rules[0]))
    else:
        exception_count = 0
        
    if operational_rules:
        operational_count = len(re.findall(r'####\s+[A-Z\s]+-\s+Rule\s+\d+:', operational_rules[0]))
    else:
        operational_count = 0
    
    # Update category counts in TOC
    new_content = re.sub(
        r'- \[Conditional\]\(#rule-type-conditional\) \(\d+ rules\)',
        f'- [Conditional](#rule-type-conditional) ({conditional_count} rules)' if conditional_count > 0 else '',
        new_content
    )
    
    new_content = re.sub(
        r'- \[Exception\]\(#rule-type-exception\) \(\d+ rules\)',
        f'- [Exception](#rule-type-exception) ({exception_count} rules)',
        new_content
    )
    
    new_content = re.sub(
        r'- \[Operational\]\(#rule-type-operational\) \(\d+ rules\)',
        f'- [Operational](#rule-type-operational) ({operational_count} rules)',
        new_content
    )
    
    # Remove empty sections if Conditional is now empty
    if conditional_count == 0:
        new_content = re.sub(
            r'================================================================================\n+## RULE TYPE: CONDITIONAL\n+\*\*Total Rules:\*\*\s+\d+\n+================================================================================',
            '',
            new_content,
            flags=re.DOTALL
        )
    
    # Write the updated content
    with open(file_path, 'w') as f:
        f.write(new_content)
    
    print(f"\n✅ Successfully removed {len(rules_to_remove)} temporal rules")
    print(f"✅ Kept {len(rules_kept)} rules (including SYNACOMEX Rule 16)")
    print(f"\n📊 Final counts:")
    print(f"  - Conditional: {conditional_count}")
    print(f"  - Exception: {exception_count}")
    print(f"  - Operational: {operational_count}")
    print(f"  - Total: {remaining_rules}")

if __name__ == '__main__':
    file_path = '/Users/ivelinnalbantov/Work/cp-laytime/cp-laytime-rules/Rules to consider/CP_RULES_CONSOLIDATED.md'
    remove_temporal_rules(file_path)

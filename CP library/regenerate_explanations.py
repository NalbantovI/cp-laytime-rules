#!/usr/bin/env python3
"""
Regenerate LAYTIME_RULES_EXPLANATIONS.md for the remaining 97 rules.
"""

import re
from datetime import datetime

def parse_master_file(filepath: str):
    """Parse the MASTER file and extract all rules."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    rules = []
    lines = content.split('\n')
    current_charter = None
    current_rule_num = None
    current_rule_text = []
    in_rule = False
    
    for line in lines:
        # Charter header
        charter_match = re.match(r'^## ([A-Z_\s]+)$', line)
        if charter_match:
            current_charter = charter_match.group(1).strip()
            continue
        
        # Rule header
        if current_charter:
            rule_match = re.match(r'^### ' + re.escape(current_charter) + r' - Rule (\d+)$', line)
            if rule_match:
                # Save previous rule if exists
                if current_rule_num and current_rule_text:
                    rules.append({
                        'charter': current_charter,
                        'rule_num': current_rule_num,
                        'text': '\n'.join(current_rule_text).strip()
                    })
                
                current_rule_num = rule_match.group(1)
                current_rule_text = []
                in_rule = True
                continue
        
        # Collect rule text
        if in_rule and current_rule_num:
            if line.startswith('##'):
                # End of current rule
                in_rule = False
                if current_rule_text:
                    rules.append({
                        'charter': current_charter,
                        'rule_num': current_rule_num,
                        'text': '\n'.join(current_rule_text).strip()
                    })
                current_rule_num = None
                current_rule_text = []
                # Process this line as a new charter
                charter_match = re.match(r'^## ([A-Z_\s]+)$', line)
                if charter_match:
                    current_charter = charter_match.group(1).strip()
            else:
                current_rule_text.append(line)
    
    # Save last rule
    if current_rule_num and current_rule_text:
        rules.append({
            'charter': current_charter,
            'rule_num': current_rule_num,
            'text': '\n'.join(current_rule_text).strip()
        })
    
    return rules

def generate_explanation(rule):
    """Generate a concise explanation for a rule."""
    text = rule['text'].lower()
    
    # Identify key topics in the rule
    topics = []
    
    # Rate-related
    if 'ton' in text and ('per' in text or 'rate' in text):
        if 'loading' in text:
            topics.append("loading rate")
        if 'discharg' in text:
            topics.append("discharging rate")
    
    # Demurrage/Despatch
    if 'demurrage' in text:
        topics.append("demurrage rate or provisions")
    if 'despatch' in text or 'dispatch' in text:
        topics.append("despatch rate or provisions")
    
    # Time counting
    if 'time' in text and ('count' in text or 'not count' in text):
        topics.append("time counting provisions")
    
    # Notice/Documentation
    if 'notice' in text and 'readiness' in text:
        topics.append("NOR tendering requirements")
    
    # Equipment/Crane
    if 'crane' in text or 'gear' in text:
        topics.append("cargo gear requirements")
    
    # Costs
    if 'expense' in text or 'cost' in text or 'account' in text:
        topics.append("cost allocation")
    
    # Certificates/Documentation
    if 'certificate' in text or 'document' in text:
        topics.append("documentation requirements")
    
    # Generate explanation
    if topics:
        return f"Charter-specific provision covering {', '.join(topics)}."
    else:
        return "Charter-specific laytime provision."

def main():
    input_file = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES.md'
    output_file = '/Users/ivelinnalbantov/Work/CP library/LAYTIME_RULES_EXPLANATIONS.md'
    
    print("📖 Parsing MASTER file...")
    rules = parse_master_file(input_file)
    print(f"   Found {len(rules)} rules")
    
    print("\n📝 Generating explanations...")
    
    # Generate output
    output = []
    output.append("# LAYTIME RULES EXPLANATIONS")
    output.append("")
    output.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    output.append(f"**Total Rules:** {len(rules)}")
    output.append("")
    output.append("This document provides concise explanations for each unique laytime rule.")
    output.append("These rules represent charter-specific provisions that are not covered by the automated .grl rules engine.")
    output.append("")
    output.append("---")
    output.append("")
    
    current_charter = None
    for rule in rules:
        if rule['charter'] != current_charter:
            current_charter = rule['charter']
            output.append(f"## {current_charter}")
            output.append("")
        
        output.append(f"### {current_charter} - Rule {rule['rule_num']}")
        output.append("")
        output.append(f"**Explanation:** {generate_explanation(rule)}")
        output.append("")
        output.append("**Rule Text:**")
        output.append("```")
        output.append(rule['text'])
        output.append("```")
        output.append("")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))
    
    print(f"✅ Generated explanations for {len(rules)} rules")
    print(f"📄 Written to: {output_file}")

if __name__ == '__main__':
    main()

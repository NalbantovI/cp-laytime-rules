#!/usr/bin/env python3
"""
Remove duplicate rules/paragraphs within each charter.
If a rule's content is a complete subset of another rule, remove the shorter one.
"""

import re
from datetime import datetime

def normalize_text(text):
    """Normalize text for comparison."""
    return ' '.join(text.split())

def extract_charters(content):
    """Extract all charters with their rules."""
    # Split content by charter headers
    charter_pattern = r'\n## ([A-Z_\s]+)\n'
    parts = re.split(charter_pattern, content)
    
    header = parts[0]
    charters = {}
    
    for i in range(1, len(parts), 2):
        if i+1 >= len(parts):
            break
            
        charter_name = parts[i].strip()
        charter_content = parts[i+1]
        
        # Extract rules
        rule_pattern = r'### ' + re.escape(charter_name) + r' - Rule (\d+)\n\n```\n(.*?)\n```'
        rules = re.findall(rule_pattern, charter_content, re.DOTALL)
        
        if rules:
            charters[charter_name] = [
                {'num': num, 'text': text.strip()} 
                for num, text in rules
            ]
    
    return header, charters

def deduplicate_rules(charter_rules):
    """Remove rules that are complete substrings of other rules."""
    if len(charter_rules) <= 1:
        return charter_rules
    
    # Normalize all rules
    normalized_rules = [
        {'num': r['num'], 'text': r['text'], 'normalized': normalize_text(r['text'])}
        for r in charter_rules
    ]
    
    # Find duplicates/subsets
    to_keep = []
    
    for i, rule in enumerate(normalized_rules):
        is_subset = False
        
        # Check if this rule is a complete subset of any other rule
        for j, other in enumerate(normalized_rules):
            if i != j:
                # If rule i is completely contained in rule j, mark as subset
                if rule['normalized'] in other['normalized'] and rule['normalized'] != other['normalized']:
                    is_subset = True
                    print(f"      Rule {rule['num']} is subset of Rule {other['num']}")
                    break
        
        if not is_subset:
            to_keep.append({'num': rule['num'], 'text': rule['text']})
    
    return to_keep

def rebuild_content(header, charters):
    """Rebuild the markdown file."""
    lines = [header]
    
    for charter_name in sorted(charters.keys()):
        rules = charters[charter_name]
        
        if not rules:
            continue
            
        lines.append(f"## {charter_name}\n\n")
        lines.append(f"**Laytime rules:** {len(rules)}\n\n")
        
        for rule in rules:
            lines.append(f"### {charter_name} - Rule {rule['num']}\n\n")
            lines.append("```\n")
            lines.append(rule['text'])
            lines.append("\n```\n\n")
    
    return ''.join(lines)

def main():
    input_file = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md'
    
    print("📖 Reading file...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("🔍 Extracting charters and rules...")
    header, charters = extract_charters(content)
    
    # Count before
    total_before = sum(len(rules) for rules in charters.values())
    print(f"   Total rules before: {total_before}")
    
    print("\n🧹 Removing duplicate/subset rules...")
    duplicates_removed = 0
    
    for charter_name in sorted(charters.keys()):
        rules = charters[charter_name]
        original_count = len(rules)
        
        deduped = deduplicate_rules(rules)
        charters[charter_name] = deduped
        
        removed = original_count - len(deduped)
        if removed > 0:
            print(f"   {charter_name}: Removed {removed} duplicate/subset rules")
            duplicates_removed += removed
    
    # Count after
    total_after = sum(len(rules) for rules in charters.values())
    
    print(f"\n📊 Summary:")
    print(f"   Rules: {total_before} → {total_after} (-{duplicates_removed})")
    
    # Update timestamp
    header = re.sub(
        r'\*\*Generated:\*\* \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',
        f'**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
        header
    )
    
    print("\n✍️  Writing deduplicated file...")
    output = rebuild_content(header, charters)
    
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"✅ Deduplication complete!")

if __name__ == '__main__':
    main()

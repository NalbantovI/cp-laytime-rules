#!/usr/bin/env python3
"""
Remove duplicate paragraphs that appear in multiple rules within the same charter.
"""

import re
from datetime import datetime

def extract_rules_structure(content):
    """Parse the file and extract charter/rule structure with paragraphs."""
    charters = {}
    
    # Split by charter sections
    charter_pattern = r'\n## ([A-Z_\s]+)\n'
    charter_splits = re.split(charter_pattern, content)
    
    # Get header
    header = charter_splits[0]
    
    # Process each charter
    i = 1
    while i < len(charter_splits) - 1:
        charter_name = charter_splits[i].strip()
        charter_content = charter_splits[i + 1]
        
        # Extract rules for this charter
        rule_pattern = r'### ' + re.escape(charter_name) + r' - Rule (\d+)\n\n```\n([\s\S]*?)\n```'
        rules = re.findall(rule_pattern, charter_content)
        
        charter_rules = []
        for rule_num, rule_text in rules:
            # Split rule into paragraphs (by double newline or clause markers)
            paragraphs = []
            current = []
            
            for line in rule_text.split('\n'):
                if line.strip() == '':
                    if current:
                        paragraphs.append('\n'.join(current).strip())
                        current = []
                else:
                    current.append(line)
            
            if current:
                paragraphs.append('\n'.join(current).strip())
            
            charter_rules.append({
                'rule_num': rule_num,
                'paragraphs': paragraphs
            })
        
        if charter_rules:
            charters[charter_name] = charter_rules
        
        i += 2
    
    return header, charters

def deduplicate_charter_rules(charter_rules):
    """Remove duplicate paragraphs within a charter's rules."""
    seen_paragraphs = set()
    deduped_rules = []
    
    for rule in charter_rules:
        unique_paragraphs = []
        
        for para in rule['paragraphs']:
            # Normalize whitespace for comparison
            normalized = ' '.join(para.split())
            
            if normalized not in seen_paragraphs:
                seen_paragraphs.add(normalized)
                unique_paragraphs.append(para)
        
        if unique_paragraphs:  # Only keep rule if it has unique paragraphs
            deduped_rules.append({
                'rule_num': rule['rule_num'],
                'paragraphs': unique_paragraphs
            })
    
    return deduped_rules

def rebuild_file(header, charters):
    """Rebuild the markdown file with deduplicated rules."""
    lines = [header]
    
    for charter_name, rules in charters.items():
        lines.append(f"## {charter_name}\n\n")
        lines.append(f"**Laytime rules:** {len(rules)}\n\n")
        
        for rule in rules:
            lines.append(f"### {charter_name} - Rule {rule['rule_num']}\n\n")
            lines.append("```\n")
            lines.append('\n\n'.join(rule['paragraphs']))
            lines.append("\n```\n\n")
    
    return ''.join(lines)

def main():
    input_file = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md'
    
    print("📖 Reading file...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("�� Analyzing rule structure...")
    header, charters = extract_rules_structure(content)
    
    # Count before
    total_rules_before = sum(len(rules) for rules in charters.values())
    total_paragraphs_before = sum(
        len(para) for rules in charters.values() 
        for rule in rules 
        for para in rule['paragraphs']
    )
    
    print(f"   Rules before: {total_rules_before}")
    print(f"   Paragraphs before: {total_paragraphs_before}")
    
    print("\n🧹 Deduplicating paragraphs...")
    duplicates_found = 0
    rules_removed = 0
    
    for charter_name, rules in list(charters.items()):
        original_count = len(rules)
        original_para_count = sum(len(r['paragraphs']) for r in rules)
        
        deduped = deduplicate_charter_rules(rules)
        charters[charter_name] = deduped
        
        new_para_count = sum(len(r['paragraphs']) for r in deduped)
        para_removed = original_para_count - new_para_count
        rules_removed_charter = original_count - len(deduped)
        
        if para_removed > 0:
            print(f"   {charter_name}: Removed {para_removed} duplicate paragraphs")
            duplicates_found += para_removed
            rules_removed += rules_removed_charter
    
    # Count after
    total_rules_after = sum(len(rules) for rules in charters.values())
    total_paragraphs_after = sum(
        len(para) for rules in charters.values() 
        for rule in rules 
        for para in rule['paragraphs']
    )
    
    print(f"\n📊 Summary:")
    print(f"   Rules: {total_rules_before} → {total_rules_after} (-{total_rules_before - total_rules_after})")
    print(f"   Paragraphs: {total_paragraphs_before} → {total_paragraphs_after} (-{duplicates_found})")
    
    # Update generation timestamp in header
    header = re.sub(
        r'\*\*Generated:\*\* \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',
        f'**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
        header
    )
    
    print("\n✍️  Writing deduplicated file...")
    output = rebuild_file(header, charters)
    
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"✅ Deduplication complete!")
    print(f"   File: {input_file}")

if __name__ == '__main__':
    main()

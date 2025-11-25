#!/usr/bin/env python3
"""
Comprehensive cleanup of MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md
Fixes: 
1. Corrupted/garbled text with missing spaces
2. Duplicate paragraphs within rules
3. Incomplete sentences (fragments)
4. Non-laytime administrative content
5. Excessive whitespace
"""

import re
from datetime import datetime
from collections import defaultdict

def fix_corrupted_text(text):
    """Fix common OCR/corruption patterns"""
    # Fix missing spaces before "The" with capital letter before it
    text = re.sub(r'([a-z])([A-Z][a-z]+\s+[A-Z][a-z])', r'\1 \2', text)
    
    # Fix missing spaces between lowercase and capital letters (camelCase issues)
    text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    
    # Fix common corrupted words
    text = text.replace('StevedormThe', 'Stevedore The')
    text = text.replace('bconstruction', 'be constructed')
    text = text.replace('liged to force', 'obliged to force')
    text = text.replace('therebymen', 'thereby. Men')
    
    # Fix multiple spaces
    text = re.sub(r'  +', ' ', text)
    
    return text

def is_complete_sentence(text):
    """Check if text forms complete sentence(s)"""
    text = text.strip()
    
    # Too short to be meaningful
    if len(text) < 20:
        return False
    
    # Starts mid-sentence (lowercase or conjunction)
    if text and text[0].islower():
        return False
    
    # Common starting words that indicate fragment
    fragment_starts = ['and all excepted', 'or if the', 'and if the', 'unless the', 
                       'provided that', 'subject to', 'except that']
    for start in fragment_starts:
        if text.lower().startswith(start):
            return False
    
    return True

def is_laytime_relevant(text):
    """Check if text directly affects laytime calculation"""
    text_lower = text.lower()
    
    # Strong laytime keywords
    laytime_keywords = [
        'laytime',
        'demurrage',
        'despatch',
        'time lost',
        'time used',
        'time occupied',
        'time spent',
        'time taken',
        'shall not count',
        'will not count',
        'not count as',
        'time running',
        'time shall cease',
        'time shall not',
        'waiting time',
        'time allowed',
        'time to count',
        'count as time',
    ]
    
    # Check for laytime keywords first
    has_laytime_keyword = False
    for keyword in laytime_keywords:
        if keyword in text_lower:
            has_laytime_keyword = True
            break
    
    # If no laytime keywords at all, it's not relevant
    if not has_laytime_keyword:
        return False
    
    # Check for non-laytime administrative content
    # Even if laytime words appear, these are purely administrative
    admin_only_patterns = [
        r'notice.*given.*treated as.*received.*business day',  # Notice procedures (ANGLO AMERICAN Rule 2)
        r'delivered by hand.*business hours.*commencement.*next.*business day',
        r'transmitted by fax.*transmission.*business day.*transmitted by e-?mail',
        r'ISPS Code.*Security certificate.*(?!.*time.*count)',  # Just certificate mentions
        r'Hague rules.*entitled to.*benefit.*privileges.*immunities',  # Just legal references
    ]
    
    for pattern in admin_only_patterns:
        if re.search(pattern, text_lower, re.IGNORECASE):
            return False
    
    return True  # Has laytime keywords and not purely administrative

def remove_duplicate_paragraphs(text):
    """Remove duplicate paragraphs within a rule"""
    # Split into paragraphs
    paragraphs = re.split(r'\n\n+', text)
    
    # Track seen paragraphs (normalized)
    seen = set()
    unique_paras = []
    
    for para in paragraphs:
        normalized = ' '.join(para.split())  # Normalize whitespace
        if normalized and normalized not in seen:
            seen.add(normalized)
            unique_paras.append(para)
    
    return '\n\n'.join(unique_paras)

def clean_rule_text(rule_text):
    """Clean a single rule's text"""
    # Fix corrupted text first
    rule_text = fix_corrupted_text(rule_text)
    
    # Remove duplicate paragraphs
    rule_text = remove_duplicate_paragraphs(rule_text)
    
    # Split into logical paragraphs and filter
    paragraphs = re.split(r'\n\n+', rule_text)
    cleaned_paragraphs = []
    
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        
        # Check if complete and laytime-relevant
        if is_complete_sentence(para) and is_laytime_relevant(para):
            cleaned_paragraphs.append(para)
    
    return '\n\n'.join(cleaned_paragraphs)

def extract_charters(content):
    """Extract all charters with their rules"""
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
            cleaned_rules = []
            for num, text in rules:
                cleaned_text = clean_rule_text(text)
                if cleaned_text:  # Only keep if there's content after cleaning
                    cleaned_rules.append({'num': num, 'text': cleaned_text})
            
            if cleaned_rules:  # Only add charter if it has valid rules
                charters[charter_name] = cleaned_rules
    
    return header, charters

def rebuild_content(header, charters):
    """Rebuild the markdown file"""
    lines = []
    
    # Update header with new timestamp
    header = re.sub(
        r'\*\*Generated:\*\* \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}',
        f'**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
        header
    )
    
    lines.append(header)
    
    for charter_name in sorted(charters.keys()):
        rules = charters[charter_name]
        
        if not rules:
            continue
        
        lines.append(f"## {charter_name}\n\n")
        lines.append(f"**Laytime rules:** {len(rules)}\n\n")
        
        for idx, rule in enumerate(rules, 1):
            lines.append(f"### {charter_name} - Rule {idx}\n\n")
            lines.append("```\n")
            lines.append(rule['text'])
            lines.append("\n```\n\n")
    
    return ''.join(lines)

def main():
    input_file = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md'
    backup_file = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY_BEFORE_CLEANUP.md.bak'
    
    print("📖 Reading file...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Create backup
    print(f"💾 Creating backup at {backup_file}...")
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("🔍 Extracting and cleaning charters and rules...")
    header, charters = extract_charters(content)
    
    # Count before
    total_before = sum(len(rules) for rules in charters.values())
    charter_count = len(charters)
    
    print(f"\n📊 Statistics:")
    print(f"   Charters: {charter_count}")
    print(f"   Rules: {total_before}")
    print(f"\n🧹 Issues Fixed:")
    print(f"   ✓ Corrupted text patterns")
    print(f"   ✓ Duplicate paragraphs within rules")
    print(f"   ✓ Incomplete sentence fragments")
    print(f"   ✓ Non-laytime administrative content")
    print(f"   ✓ Excessive whitespace")
    
    print("\n✍️  Rebuilding file...")
    output = rebuild_content(header, charters)
    
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(output)
    
    # Final stats
    final_lines = len(output.splitlines())
    print(f"\n✅ Cleanup complete!")
    print(f"   Final line count: {final_lines}")
    print(f"   Backup saved: {backup_file}")

if __name__ == '__main__':
    main()

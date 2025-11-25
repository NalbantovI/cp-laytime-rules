#!/usr/bin/env python3
"""
Extract clean laytime-only provisions from MASTER_CP_LAYTIME_RULES.md
This properly extracts from the clean source instead of trying to fix corrupted data
"""

import re
from datetime import datetime

def is_laytime_relevant(text):
    """Check if paragraph directly affects laytime calculation"""
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
        'time saved',
        'shall not count',
        'will not count',
        'not count as',
        'not to count',
        'time running',
        'time shall cease',
        'time shall not',
        'waiting time',
        'time allowed',
        'count as time',
        'time to count',
    ]
    
    # Must have at least one laytime keyword
    has_laytime = any(kw in text_lower for kw in laytime_keywords)
    if not has_laytime:
        return False
    
    # Exclude purely administrative content even if it mentions time
    admin_patterns = [
        r'notice.*given.*party.*treated as.*received.*business day',
        r'delivered by hand.*business hours.*next business day.*courier.*fax.*e-?mail',
        r'transmitted by fax.*transmission.*business day.*transmitted by e-?mail',
    ]
    
    for pattern in admin_patterns:
        if re.search(pattern, text_lower, re.DOTALL):
            return False
    
    return True

def is_complete_sentence(text):
    """Check if text is a complete, meaningful sentence"""
    text = text.strip()
    
    if len(text) < 30:  # Too short to be meaningful
        return False
    
    # Starts with lowercase (likely fragment)
    if text and text[0].islower():
        return False
    
    # Starts with common fragment indicators
    fragment_starts = [
        'and all excepted', 'or if the', 'and if the', 
        'unless the', 'provided that', 'subject to',
        'except that', 'failing which', 'otherwise'
    ]
    
    for start in fragment_starts:
        if text.lower().startswith(start):
            return False
    
    # Ends abruptly without proper punctuation or clause ending
    if not text[-1] in '.!?:':
        # Check if it's a numbered list item or clause that continues
        if not re.search(r'\d+\.\d+$|\([a-z]\)$|[a-z]\.$', text):
            # Doesn't end properly
            pass  # Allow for now, some clauses are legitimately continuous
    
    return True

def extract_laytime_paragraphs(rule_text):
    """Extract laytime-relevant paragraphs from a rule"""
    # Split by clause numbering patterns
    # Match patterns like "20.3", "21.2", "(a)", "c.", etc.
    clause_pattern = r'((?:^|\n)(?:\d+\.\d+|\([a-z]\)|[a-z]\.)\s)'
    parts = re.split(clause_pattern, rule_text, flags=re.MULTILINE)
    
    # Reconstruct clauses
    clauses = []
    i = 0
    while i < len(parts):
        if i == 0 and parts[i].strip():
            # First part before any numbering
            clauses.append(parts[i])
            i += 1
        elif i + 1 < len(parts):
            # Numbered clause
            clause = parts[i] + parts[i+1]
            clauses.append(clause)
            i += 2
        else:
            i += 1
    
    # Filter for laytime-relevant complete clauses
    laytime_clauses = []
    for clause in clauses:
        clause = clause.strip()
        if not clause:
            continue
        
        # Remove section headers that have no content after them
        # Pattern: ends with just a section title like "21 Accessible Space/Grab Discharge"
        if re.search(r'\n\d+[\.\s]+[A-Z][A-Za-z\s/]+$', clause):
            # Remove the trailing header
            clause = re.sub(r'\n\d+[\.\s]+[A-Z][A-Za-z\s/]+$', '', clause)
        
        clause = clause.strip()
        if clause and is_complete_sentence(clause) and is_laytime_relevant(clause):
            laytime_clauses.append(clause)
    
    return laytime_clauses

def process_master_file(input_file, output_file):
    """Extract laytime-only provisions from MASTER file"""
    print("📖 Reading MASTER file...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse by charter sections
    charter_pattern = r'\n## ([A-Z_\s]+)\n'
    parts = re.split(charter_pattern, content)
    
    # Extract header
    header_lines = [
        "# MASTER CP LAYTIME RULES - LAYTIME CALCULATION ONLY\n\n",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        "**Source:** MASTER_CP_LAYTIME_RULES.md\n",
        "**Processing:** Extracted only complete clauses affecting laytime calculation\n\n",
        "This document contains only the specific provisions from charter party clauses\n",
        "that directly affect laytime counting, suspension, or calculation.\n",
        "Full commercial context has been removed.\n\n",
        "---\n\n"
    ]
    
    output_lines = []
    total_charters = 0
    total_rules = 0
    
    # Process each charter (skip intro - first element)
    i = 1
    while i < len(parts) - 1:
        charter_name = parts[i].strip()
        charter_content = parts[i + 1]
        
        # Extract rules for this charter
        rule_pattern = r'### ' + re.escape(charter_name) + r' - Rule (\d+)\n\n```\n([\s\S]*?)\n```'
        rules = re.findall(rule_pattern, charter_content, re.DOTALL)
        
        # Extract laytime paragraphs from each rule
        charter_laytime_rules = []
        for rule_num, rule_text in rules:
            laytime_paras = extract_laytime_paragraphs(rule_text)
            if laytime_paras:
                charter_laytime_rules.append(laytime_paras)
        
        # Write charter section if it has laytime content
        if charter_laytime_rules:
            output_lines.append(f"## {charter_name}\n\n")
            output_lines.append(f"**Laytime rules:** {len(charter_laytime_rules)}\n\n")
            
            for idx, paragraphs in enumerate(charter_laytime_rules, 1):
                output_lines.append(f"### {charter_name} - Rule {idx}\n\n")
                output_lines.append("```\n")
                output_lines.append('\n\n'.join(paragraphs))
                output_lines.append("\n```\n\n")
            
            total_charters += 1
            total_rules += len(charter_laytime_rules)
        
        i += 2
    
    # Write output
    print(f"✍️  Writing output file...")
    final_content = ''.join(header_lines + output_lines)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print(f"\n📊 Extraction Results:")
    print(f"   Charters with laytime rules: {total_charters}")
    print(f"   Total laytime rules: {total_rules}")
    print(f"   Lines in output: {len(final_content.splitlines())}")
    print(f"\n✅ Clean extraction complete!")
    print(f"   Output: {output_file}")

if __name__ == '__main__':
    input_file = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES.md'
    output_file = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md'
    
    # Backup current file
    backup_file = output_file + '.corrupted.bak'
    try:
        import shutil
        shutil.copy(output_file, backup_file)
        print(f"💾 Backed up corrupted file to: {backup_file}\n")
    except:
        pass
    
    process_master_file(input_file, output_file)

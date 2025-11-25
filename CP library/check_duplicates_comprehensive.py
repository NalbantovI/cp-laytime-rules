#!/usr/bin/env python3
"""
Comprehensive duplicate detection across MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md
"""

import re
from collections import defaultdict

def extract_rules_content(filepath):
    """Extract all rule contents with their locations"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    rules = []
    # Match charter sections with their rules
    charter_pattern = r'^## (.+?)$'
    rule_pattern = r'^### (.+?) - Rule (\d+)$'
    
    lines = content.split('\n')
    current_charter = None
    current_rule = None
    current_content = []
    in_code_block = False
    
    for i, line in enumerate(lines, 1):
        # Check for charter header
        charter_match = re.match(charter_pattern, line)
        if charter_match and not in_code_block:
            current_charter = charter_match.group(1)
            continue
        
        # Check for rule header
        rule_match = re.match(rule_pattern, line)
        if rule_match and not in_code_block:
            # Save previous rule if exists
            if current_rule and current_content:
                rules.append({
                    'charter': current_charter,
                    'rule': current_rule,
                    'content': '\n'.join(current_content).strip(),
                    'line': current_rule_start
                })
            current_rule = f"{rule_match.group(1)} - Rule {rule_match.group(2)}"
            current_rule_start = i
            current_content = []
            continue
        
        # Track code blocks
        if line.startswith('```'):
            in_code_block = not in_code_block
            if in_code_block and current_rule:
                continue  # Skip opening ```
            elif not in_code_block and current_rule:
                continue  # Skip closing ```
        
        # Collect content within rules
        if current_rule and in_code_block:
            current_content.append(line)
    
    # Save last rule
    if current_rule and current_content:
        rules.append({
            'charter': current_charter,
            'rule': current_rule,
            'content': '\n'.join(current_content).strip(),
            'line': current_rule_start
        })
    
    return rules

def normalize_text(text):
    """Normalize text for comparison"""
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove line numbers if present
    text = re.sub(r'\b\d{1,4}\b', '', text)
    return text.strip().lower()

def find_duplicates(rules):
    """Find duplicate or very similar text across rules"""
    duplicates = []
    
    # Check for exact duplicates
    content_map = defaultdict(list)
    for rule in rules:
        normalized = normalize_text(rule['content'])
        if len(normalized) > 50:  # Only check substantial content
            content_map[normalized].append(rule)
    
    for content, rule_list in content_map.items():
        if len(rule_list) > 1:
            duplicates.append({
                'type': 'exact',
                'rules': rule_list,
                'sample': rule_list[0]['content'][:200]
            })
    
    # Check for paragraph-level duplicates (sentences appearing in multiple rules)
    sentence_map = defaultdict(list)
    for rule in rules:
        # Split into sentences (approximate)
        sentences = re.split(r'[.!?]\s+', rule['content'])
        for sentence in sentences:
            normalized = normalize_text(sentence)
            if len(normalized) > 30:  # Only check substantial sentences
                sentence_map[normalized].append({
                    'rule': rule,
                    'sentence': sentence.strip()
                })
    
    paragraph_duplicates = []
    for sentence, occurrences in sentence_map.items():
        if len(occurrences) > 1:
            # Check if from different charters
            charters = set(occ['rule']['charter'] for occ in occurrences)
            if len(charters) > 1 or len(occurrences) > 2:  # Cross-charter or many occurrences
                paragraph_duplicates.append({
                    'type': 'paragraph',
                    'occurrences': occurrences,
                    'sample': occurrences[0]['sentence'][:150]
                })
    
    return duplicates, paragraph_duplicates

def check_specific_patterns(rules):
    """Check for specific common patterns that might be duplicated"""
    patterns = {
        'grab_discharge': r'grab.{0,50}discharge.{0,50}deeptank',
        'time_not_count': r'time.{0,30}not.{0,10}count.{0,30}laytime',
        'owners_account': r"owner['\u2019s]{0,3}\s+account",
        'certificates': r'certificate.{0,50}vessel',
        'lighterage': r'lighterage.{0,50}lightening.{0,50}vessel',
    }
    
    pattern_matches = defaultdict(list)
    for pattern_name, pattern in patterns.items():
        for rule in rules:
            if re.search(pattern, rule['content'], re.IGNORECASE):
                pattern_matches[pattern_name].append({
                    'charter': rule['charter'],
                    'rule': rule['rule'],
                    'line': rule['line']
                })
    
    return pattern_matches

def main():
    filepath = 'MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md'
    
    print("=" * 80)
    print("COMPREHENSIVE DUPLICATE TEXT ANALYSIS")
    print("=" * 80)
    print()
    
    # Extract all rules
    rules = extract_rules_content(filepath)
    print(f"✓ Analyzed {len(rules)} rules across all charters\n")
    
    # Find duplicates
    exact_duplicates, paragraph_duplicates = find_duplicates(rules)
    
    print("=" * 80)
    print("1. EXACT DUPLICATE RULES")
    print("=" * 80)
    if exact_duplicates:
        for i, dup in enumerate(exact_duplicates, 1):
            print(f"\n[{i}] Found {len(dup['rules'])} rules with identical content:")
            for rule in dup['rules']:
                print(f"    • {rule['charter']} - {rule['rule']} (line {rule['line']})")
            print(f"    Sample: {dup['sample']}...")
    else:
        print("✓ No exact duplicate rules found")
    
    print("\n")
    print("=" * 80)
    print("2. DUPLICATE PARAGRAPHS/SENTENCES")
    print("=" * 80)
    if paragraph_duplicates:
        # Filter to show most significant (>3 occurrences or cross-charter)
        significant = [p for p in paragraph_duplicates if len(p['occurrences']) > 3]
        if significant:
            print(f"\nFound {len(significant)} significant duplicate paragraphs:\n")
            for i, dup in enumerate(significant[:10], 1):  # Show top 10
                print(f"[{i}] Appears in {len(dup['occurrences'])} rules:")
                charters = set()
                for occ in dup['occurrences'][:5]:  # Show first 5
                    charter = occ['rule']['charter']
                    rule = occ['rule']['rule']
                    print(f"    • {charter} - {rule}")
                    charters.add(charter)
                print(f"    Charters: {', '.join(sorted(charters))}")
                print(f"    Text: {dup['sample']}...")
                print()
        else:
            print("✓ No significant duplicate paragraphs found")
    else:
        print("✓ No duplicate paragraphs found")
    
    print()
    print("=" * 80)
    print("3. COMMON PATTERN ANALYSIS")
    print("=" * 80)
    pattern_matches = check_specific_patterns(rules)
    
    for pattern_name, matches in sorted(pattern_matches.items()):
        if len(matches) > 3:  # Only show if appears frequently
            print(f"\n'{pattern_name}' pattern appears in {len(matches)} rules:")
            # Group by charter
            by_charter = defaultdict(list)
            for match in matches:
                by_charter[match['charter']].append(match['rule'])
            for charter in sorted(by_charter.keys())[:5]:  # Show top 5
                rules_list = by_charter[charter]
                print(f"    • {charter}: {len(rules_list)} rule(s)")
    
    print("\n")
    print("=" * 80)
    print("4. SPECIFIC DUPLICATION CHECKS")
    print("=" * 80)
    
    # Check for lighterage duplicates specifically
    lighterage_rules = [r for r in rules if 'lighterage' in r['content'].lower() 
                       and 'lightening' in r['content'].lower()]
    
    if len(lighterage_rules) > 1:
        print(f"\nFound {len(lighterage_rules)} rules about lighterage/lightening:")
        lighterage_groups = defaultdict(list)
        for rule in lighterage_rules:
            # Normalize content for grouping
            normalized = normalize_text(rule['content'])
            lighterage_groups[normalized].append(rule)
        
        for content, group in lighterage_groups.items():
            if len(group) > 1:
                print(f"\n  Identical lighterage text in {len(group)} rules:")
                for rule in group:
                    print(f"    • {rule['charter']} - {rule['rule']} (line {rule['line']})")
    
    # Check RTM rules specifically
    rtm_rules = [r for r in rules if r['charter'] == 'RTM']
    if len(rtm_rules) >= 2:
        print(f"\n\nRTM Charter has {len(rtm_rules)} rules - checking for duplicates:")
        for i, rule1 in enumerate(rtm_rules):
            for rule2 in rtm_rules[i+1:]:
                similarity = len(set(normalize_text(rule1['content']).split()) & 
                               set(normalize_text(rule2['content']).split()))
                if similarity > 10:  # Significant word overlap
                    print(f"  ⚠ {rule1['rule']} and {rule2['rule']} have {similarity} words in common")
                    print(f"     Line {rule1['line']} vs Line {rule2['line']}")
    
    print("\n")
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total rules analyzed: {len(rules)}")
    print(f"Exact duplicates found: {len(exact_duplicates)}")
    print(f"Paragraph duplicates: {len(paragraph_duplicates)}")
    print()

if __name__ == '__main__':
    main()

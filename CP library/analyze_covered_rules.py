#!/usr/bin/env python3
"""
Analyze rules that are covered by default stoppages in the rules engine.
These are Owner's fault scenarios where time automatically does NOT count.
"""

import re

def analyze_covered_rules(filepath):
    """Identify rules covered by default stoppage configurations."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=" * 100)
    print("ANALYZING RULES COVERED BY DEFAULT STOPPAGES")
    print("=" * 100)
    print()
    
    # Pattern categories covered by rules engine
    covered_patterns = {
        'SAFETY_INSPECTION': [
            r'safety.*inspection',
            r'safety.*meeting',
            r'safety.*requirements',
        ],
        'GANGWAY_UNSAFE': [
            r'gangway.*unsafe',
            r'safe.*gangway',
            r'gangway.*placed',
            r'accessibility.*safe',
        ],
        'WAITING_FOR_CERTIFICATE': [
            r'certificate.*efficiency',
            r'valid.*certificate',
            r'up.*to.*date.*certificate',
            r'possession.*certificate',
        ],
        'VESSEL_NOT_READY': [
            r'lights on board',
            r'sufficient lights',
            r'cargo handling gear.*comply',
            r'vessel.*not.*ready',
            r'equipment.*comply.*regulations',
        ],
    }
    
    # Find all rules
    rule_pattern = r'### ([A-Z_\s]+) - Rule (\d+)\n\n```\n(.*?)```'
    rules = re.findall(rule_pattern, content, re.DOTALL)
    
    covered_rules = []
    
    for charter, rule_num, rule_text in rules:
        charter = charter.strip()
        matches = []
        
        for stoppage_type, patterns in covered_patterns.items():
            for pattern in patterns:
                if re.search(pattern, rule_text, re.IGNORECASE):
                    matches.append((stoppage_type, pattern))
        
        if matches:
            # Check if rule has time-counting language
            has_time_language = bool(re.search(
                r'time.*(?:lost|count|used)|shall not count|not to count|time.*owner.*account',
                rule_text,
                re.IGNORECASE
            ))
            
            if has_time_language:
                covered_rules.append({
                    'charter': charter,
                    'rule': rule_num,
                    'matches': matches,
                    'text_preview': rule_text[:200].replace('\n', ' ')
                })
    
    print(f"Found {len(covered_rules)} rules with provisions covered by default stoppages:\n")
    
    for rule in covered_rules:
        print(f"## {rule['charter']} - Rule {rule['rule']}")
        print(f"   Preview: {rule['text_preview']}...")
        print(f"   Covered by:")
        for stoppage, pattern in rule['matches']:
            print(f"      → {stoppage} (pattern: '{pattern}')")
        print()
    
    print("=" * 100)
    print("RULES ENGINE COVERAGE")
    print("=" * 100)
    print()
    print("These scenarios are already handled by default stoppages:")
    print()
    print("1. SAFETY_INSPECTION:")
    print("   - Safety inspections, meetings, requirements")
    print("   - ModifierNotUsed: 1.0 (time counts, routine operation)")
    print()
    print("2. GANGWAY_UNSAFE:")
    print("   - Unsafe gangway/access conditions")
    print("   - ModifierNotUsed: 0.0 (Owner's fault, time does NOT count)")
    print()
    print("3. WAITING_FOR_CERTIFICATE:")
    print("   - Missing/invalid certificates")
    print("   - ModifierNotUsed: 0.0 (Owner's fault, time does NOT count)")
    print()
    print("4. VESSEL_NOT_READY scenarios:")
    print("   - Insufficient lights")
    print("   - Equipment not complying with regulations")
    print("   - Vessel not meeting requirements")
    print("   - ModifierNotUsed: 0.0 (Owner's fault, time does NOT count)")
    print()
    print("=" * 100)
    print()
    print(f"RECOMMENDATION: Review {len(covered_rules)} rules for potential removal")
    print("These charter provisions describe Owner's responsibility (WHO PAYS)")
    print("but do NOT add unique laytime calculation logic (WHEN TIME COUNTS)")
    print()

if __name__ == '__main__':
    filepath = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md'
    analyze_covered_rules(filepath)

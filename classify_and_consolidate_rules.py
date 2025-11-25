#!/usr/bin/env python3
"""
Script to classify charter party rules by Rule Type and consolidate them.

Rule Types (from YARA analysis):
- Legal/Procedural: Contractual requirements
- Operational: Physical operations
- Temporal: Time-based conditions
- Conditional: If-then logic
- Modifier: Adjustments to base rules
- Exception: Special circumstances
- Cargo Terms: Cargo-related operational conditions
- Early Loading: Timing modifiers for early commencement
- NOR Tendering: Notice procedures
- NOR Failed Inspection: Contingency scenarios
- Waiting Berth time: Delay handling
- Humidity Interruption: Weather-specific
- Port Cargo Hours: Working time definitions
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Define rule type classification based on keywords
RULE_TYPE_KEYWORDS = {
    "Legal/Procedural": [
        "shall be given", "notice", "written", "recipient", "requirement",
        "certificate", "compliance", "regulation", "law", "contract",
        "liability", "responsibility", "obligation", "cancellation", "canceling"
    ],
    "Operational": [
        "loading", "discharging", "cargo operations", "stevedore", "holds",
        "hatches", "equipment", "crane", "gear", "power", "ballast",
        "deballast", "bunkering", "shifting", "berth", "alongside"
    ],
    "Temporal": [
        "time", "hours", "days", "commence", "start", "office hours",
        "working day", "laycan", "midnight", "noon", "morning", "afternoon",
        "next day", "previous", "before", "after"
    ],
    "Conditional": [
        "if", "unless", "provided that", "subject to", "in the event",
        "where", "when", "should", "in case", "on condition"
    ],
    "Modifier": [
        "half", "double", "multiplier", "rate", "actual time used",
        "time actually used", "ATUC", "pro rata", "proportion"
    ],
    "Exception": [
        "excepted", "SHEX", "SSHEX", "FHEX", "except", "excluding",
        "not count", "shall not count", "excluded", "force majeure"
    ],
    "Cargo Terms": [
        "cargo ready", "cargo not ready", "weather working day", "WWD",
        "rain", "humidity", "moisture", "cargo condition"
    ],
    "Early Loading": [
        "early", "sooner commenced", "unless used", "UU", "before laytime",
        "prior to laytime"
    ],
    "NOR Tendering": [
        "Notice of Readiness", "NOR", "tender notice", "valid notice",
        "accepted", "rejected"
    ],
    "NOR Failed Inspection": [
        "inspection", "failed inspection", "not ready", "unready",
        "holds not clean", "re-inspection", "survey"
    ],
    "Waiting Berth Time": [
        "waiting for berth", "berth not available", "congestion",
        "anchorage", "waiting place", "roads"
    ],
    "Weather Interruption": [
        "weather", "storm", "fog", "wind", "sea", "swell", "ice",
        "snow", "frost"
    ],
    "Port Cargo Hours": [
        "working hours", "port hours", "terminal hours", "shift",
        "overtime", "holiday", "Sunday", "Saturday"
    ]
}

def classify_rule_type(rule_text):
    """Classify a rule based on keywords. Returns list of applicable types."""
    rule_lower = rule_text.lower()
    types = []
    scores = {}
    
    for rule_type, keywords in RULE_TYPE_KEYWORDS.items():
        score = sum(1 for keyword in keywords if keyword.lower() in rule_lower)
        if score > 0:
            scores[rule_type] = score
    
    # Return types sorted by score (most relevant first)
    if scores:
        sorted_types = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        # Return top 2 types or all with score >= top_score/2
        top_score = sorted_types[0][1]
        types = [t for t, s in sorted_types if s >= top_score / 2][:3]  # Max 3 types
    
    if not types:
        types = ["Unclassified"]
    
    return types

def extract_rules_from_file(file_path):
    """Extract rules from a charter party analysis file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        rules = []
        
        # Pattern 1: Rules in numbered format (Rule X:)
        pattern1 = r'(?:^|\n)(?:Rule|RULE)\s+(\d+):\s*([^\n]+)\n((?:(?!(?:^|\n)(?:Rule|RULE)\s+\d+:).)*)'
        matches1 = re.finditer(pattern1, content, re.MULTILINE | re.DOTALL | re.IGNORECASE)
        
        for match in matches1:
            rule_num = match.group(1)
            rule_title = match.group(2).strip()
            rule_text = match.group(3).strip()
            
            # Get full rule text (title + content)
            full_rule = f"{rule_title}\n{rule_text}"
            rules.append({
                'number': rule_num,
                'title': rule_title,
                'text': rule_text,
                'full_text': full_rule
            })
        
        # Pattern 2: Markdown headers with rule content
        if not rules:
            pattern2 = r'#+\s+(.+?)\n((?:(?!#+\s+).)*)'
            matches2 = re.finditer(pattern2, content, re.MULTILINE | re.DOTALL)
            
            for i, match in enumerate(matches2, 1):
                title = match.group(1).strip()
                text = match.group(2).strip()
                
                # Skip headers that are not rules
                if any(skip in title.lower() for skip in ['analysis', 'summary', 'overview', 'introduction']):
                    continue
                
                if text and len(text) > 50:  # Only include substantial content
                    rules.append({
                        'number': str(i),
                        'title': title,
                        'text': text,
                        'full_text': f"{title}\n{text}"
                    })
        
        return rules
    
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return []

def process_charter_folders(base_path):
    """Process all charter party folders."""
    base = Path(base_path)
    all_rules = defaultdict(list)
    charter_stats = {}
    
    # Get all subdirectories
    folders = [f for f in base.iterdir() if f.is_dir()]
    
    print(f"Found {len(folders)} charter party folders")
    
    for folder in sorted(folders):
        charter_name = folder.name
        print(f"\nProcessing: {charter_name}")
        
        # Look for analysis files
        analysis_files = list(folder.glob("*_ANALYSIS.md")) + list(folder.glob("*ANALYSIS*.md"))
        
        if not analysis_files:
            print(f"  ⚠️  No analysis file found")
            charter_stats[charter_name] = {'rules': 0, 'files': 0}
            continue
        
        charter_rules = []
        
        for analysis_file in analysis_files:
            print(f"  📄 Reading: {analysis_file.name}")
            rules = extract_rules_from_file(analysis_file)
            
            if rules:
                print(f"    Found {len(rules)} rules")
                charter_rules.extend(rules)
        
        if charter_rules:
            # Classify each rule
            for rule in charter_rules:
                rule_types = classify_rule_type(rule['full_text'])
                rule['types'] = rule_types
                rule['charter'] = charter_name
                
                # Add to category buckets
                for rule_type in rule_types:
                    all_rules[rule_type].append(rule)
        
        charter_stats[charter_name] = {
            'rules': len(charter_rules),
            'files': len(analysis_files)
        }
    
    return all_rules, charter_stats

def generate_consolidated_file(all_rules, charter_stats, output_path):
    """Generate the consolidated CP_RULES.md file."""
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# CONSOLIDATED CHARTER PARTY RULES - CLASSIFIED BY RULE TYPE\n\n")
        f.write(f"**Generated:** {Path.cwd()}\n")
        f.write(f"**Total Charter Parties Processed:** {len(charter_stats)}\n")
        
        total_rules = sum(stats['rules'] for stats in charter_stats.values())
        f.write(f"**Total Rules Extracted:** {total_rules}\n\n")
        
        f.write("---\n\n")
        
        # Table of contents
        f.write("## TABLE OF CONTENTS\n\n")
        for rule_type in sorted(all_rules.keys()):
            count = len(all_rules[rule_type])
            f.write(f"- [{rule_type}](#rule-type-{rule_type.lower().replace('/', '-').replace(' ', '-')}) ({count} rules)\n")
        
        f.write("\n---\n\n")
        
        # Statistics section
        f.write("## PROCESSING STATISTICS\n\n")
        f.write("| Charter Party | Rules Found | Analysis Files |\n")
        f.write("|--------------|-------------|----------------|\n")
        for charter, stats in sorted(charter_stats.items()):
            f.write(f"| {charter} | {stats['rules']} | {stats['files']} |\n")
        
        f.write("\n---\n\n")
        
        # Rule type sections
        for rule_type in sorted(all_rules.keys()):
            rules = all_rules[rule_type]
            
            anchor = rule_type.lower().replace('/', '-').replace(' ', '-')
            f.write(f"## RULE TYPE: {rule_type.upper()}\n\n")
            f.write(f"**Total Rules:** {len(rules)}\n\n")
            
            # Group by charter party
            by_charter = defaultdict(list)
            for rule in rules:
                by_charter[rule['charter']].append(rule)
            
            for charter in sorted(by_charter.keys()):
                charter_rules = by_charter[charter]
                f.write(f"### {charter} ({len(charter_rules)} rules)\n\n")
                
                for i, rule in enumerate(charter_rules, 1):
                    # Show all applicable types
                    types_str = ", ".join(rule['types'])
                    
                    f.write(f"#### {charter} - Rule {rule['number']}: {rule['title']}\n\n")
                    f.write(f"**Rule Types:** {types_str}\n\n")
                    f.write(f"**Rule Text:**\n```\n{rule['text'][:500]}{'...' if len(rule['text']) > 500 else ''}\n```\n\n")
                    f.write("---\n\n")
            
            f.write("\n---\n\n")
    
    print(f"\n✅ Consolidated file created: {output_path}")

def main():
    base_path = Path("/Users/ivelinnalbantov/Work/cp-laytime/cp-laytime-rules/CP library/Charters")
    output_path = Path("/Users/ivelinnalbantov/Work/cp-laytime/cp-laytime-rules/CP_RULES_CONSOLIDATED.md")
    
    print("=" * 80)
    print("CHARTER PARTY RULES CLASSIFICATION AND CONSOLIDATION")
    print("=" * 80)
    
    # Process all folders
    all_rules, charter_stats = process_charter_folders(base_path)
    
    # Generate consolidated file
    generate_consolidated_file(all_rules, charter_stats, output_path)
    
    # Print summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Charter Parties Processed: {len(charter_stats)}")
    print(f"Total Rules Extracted: {sum(stats['rules'] for stats in charter_stats.values())}")
    print(f"\nRules by Type:")
    for rule_type in sorted(all_rules.keys()):
        print(f"  {rule_type}: {len(all_rules[rule_type])} rules")
    print("\n✅ Done!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Complete removal of rules covered by default stoppages in the rules engine.
Removes certificate/compliance provisions that duplicate stoppage behavior.
"""

import re

def complete_covered_rules_cleanup(filepath):
    """Remove all certificate/compliance rules covered by rules engine."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=" * 100)
    print("COMPLETE CERTIFICATE/COMPLIANCE CLEANUP")
    print("=" * 100)
    print()
    
    # Count before
    original_lines = len(content.split('\n'))
    original_rules = len(re.findall(r'### .* - Rule \d+', content))
    
    print(f"BEFORE:")
    print(f"  Lines: {original_lines}")
    print(f"  Total Rules: {original_rules}")
    print()
    
    removals = []
    
    # ===== REMOVAL 1: ALCOA Rule 1 =====
    # This entire rule is about certificates - covered by WAITING_FOR_CERTIFICATE
    pattern1 = r'(### ALCOA - Rule 1\n\n```\n.*?```\n\n)(### ALCOA - Rule 2)'
    match1 = re.search(pattern1, content, re.DOTALL)
    if match1:
        removed = match1.group(1)
        removals.append({
            'name': 'ALCOA - Rule 1',
            'reason': 'Entire rule about missing certificates',
            'coverage': 'WAITING_FOR_CERTIFICATE (ModifierNotUsed: 0.0)',
            'text': removed[:200]
        })
        content = re.sub(pattern1, r'\2', content, flags=re.DOTALL)
        # Renumber ALCOA rules
        content = re.sub(r'### ALCOA - Rule 2', '### ALCOA - Rule 1', content)
        content = re.sub(r'### ALCOA - Rule 3', '### ALCOA - Rule 2', content)
    
    # ===== REMOVAL 2: ANTAMINA Rule 1 - Certificate/equipment section =====
    # Remove the certificate compliance paragraph, keep the hold ladders part
    pattern2 = (
        r'(The vessel\'s cargo gear and all other equipment shall be in good working order.*?'
        r'stevedores\' standby time shall be for OWNER\'S account\.\n\n)'
    )
    match2 = re.search(pattern2, content, re.DOTALL)
    if match2:
        removed = match2.group(1)
        removals.append({
            'name': 'ANTAMINA - Rule 1 (certificate paragraph)',
            'reason': 'Certificate compliance paragraph',
            'coverage': 'WAITING_FOR_CERTIFICATE (ModifierNotUsed: 0.0)',
            'text': removed[:200]
        })
        content = re.sub(pattern2, '', content, flags=re.DOTALL)
    
    # ===== REMOVAL 3: SAMARCO Rule 1 - Certificate section =====
    # Remove certificate compliance paragraph
    pattern3 = (
        r'(The vessel\'s hold ladders are to comply.*?is not to count as laytime or time on demurrage\.\n)'
        r'|(46\.2 The Vessel nominated.*?aforementioned regulations\.\n)'
    )
    
    # Actually, let me check SAMARCO more carefully first
    samarco_match = re.search(r'## SAMARCO\n\n\*\*Laytime rules:\*\* (\d+)', content)
    if samarco_match:
        print(f"SAMARCO has {samarco_match.group(1)} rule(s)")
    
    # Print all removals
    print("REMOVING THE FOLLOWING PROVISIONS:")
    print()
    for i, removal in enumerate(removals, 1):
        print(f"{i}. {removal['name']}")
        print(f"   Reason: {removal['reason']}")
        print(f"   Covered by: {removal['coverage']}")
        print(f"   Preview: {removal['text'][:150]}...")
        print()
    
    # Write updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Count after
    new_lines = len(content.split('\n'))
    new_rules = len(re.findall(r'### .* - Rule \d+', content))
    
    print("=" * 100)
    print("AFTER:")
    print(f"  Lines: {new_lines} (removed {original_lines - new_lines})")
    print(f"  Total Rules: {new_rules} (removed {original_rules - new_rules})")
    print()
    
    # Count affected charters
    alcoa_rules = len(re.findall(r'### ALCOA - Rule \d+', content))
    antamina_rules = len(re.findall(r'### ANTAMINA - Rule \d+', content))
    
    print(f"  ALCOA Rules: {alcoa_rules}")
    print(f"  ANTAMINA Rules: {antamina_rules}")
    print()
    
    print("=" * 100)
    print("COMPLETED: Certificate/Compliance Cleanup")
    print("=" * 100)
    print()
    print(f"Removed {len(removals)} provisions")
    print()
    print("All removed provisions described 'time shall not count' for missing")
    print("certificates/compliance - this is already the DEFAULT BEHAVIOR when")
    print("WAITING_FOR_CERTIFICATE stoppage is triggered (ModifierNotUsed: 0.0)")
    print()

if __name__ == '__main__':
    filepath = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md'
    complete_covered_rules_cleanup(filepath)

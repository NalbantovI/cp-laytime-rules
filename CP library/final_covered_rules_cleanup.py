#!/usr/bin/env python3
"""
Final cleanup of rules covered by default stoppages in the rules engine.
Removes certificate/compliance provisions that duplicate stoppage behavior.
"""

import re

def final_covered_rules_cleanup(filepath):
    """Remove all certificate/compliance rules covered by rules engine."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=" * 100)
    print("FINAL CERTIFICATE/COMPLIANCE CLEANUP")
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
    
    # ===== REMOVAL 2: ANTAMINA Rule 1 - Certificate/equipment paragraph =====
    # Remove the certificate compliance paragraph only
    pattern2 = (
        r'The vessel\'s cargo gear and all other equipment shall be in good working order and comply with the\n'
        r'regulations and/or requirements in effect at load and discharge port\(s\)\. The OWNER also guarantees\n'
        r'that the vessel shall be at all times in possession of valid and up­to­date certificates on board to\n'
        r'comply with such regulations and/or requirements\.\n'
        r'If the stevedores or other laborers are not permitted to work by reason of any failure of the Master, the\n'
        r'OWNER and/or their Agents to comply with such regulations or by reason that the vessel is not in\n'
        r'possession of such valid and up­to­date certificates, then the OWNER shall make immediate\n'
        r'corrective measures\.\n'
        r'Any time lost due to non compliance with the above shall not count as laytime or time on demurrage\n'
        r'and any extra expenses incurred including stevedores\' standby time shall be for OWNER\'S account\.\n\n'
    )
    match2 = re.search(pattern2, content, re.DOTALL)
    if match2:
        removed = match2.group(0)
        removals.append({
            'name': 'ANTAMINA - Rule 1 (certificate paragraph)',
            'reason': 'Certificate compliance paragraph',
            'coverage': 'WAITING_FOR_CERTIFICATE (ModifierNotUsed: 0.0)',
            'text': removed[:200]
        })
        content = re.sub(pattern2, '', content, flags=re.DOTALL)
    
    # ===== REMOVAL 3: SAMARCO Rule 1 - Paragraph 46.2 =====
    # Remove certificate compliance paragraph 46.2, keep 46.1
    pattern3 = (
        r'46\.2 The Vessel nominated under this Charter Party shall have equipment in good working\n'
        r'order and in compliance with the regulations of the countries in which the Vessel can\n'
        r'be nominated under this Charter Party\. The Owners are to ensure that the Vessel is\n'
        r'at all times in possession of valid and up­to­date certificates of efficiency to comply\n'
        r'with such regulations known on the date of this Charter Party\. If stevedores,\n'
        r'longshoremen or other workmen are not permitted to work due to failure of the\n'
        r'Master and/or the Owners\' agents to comply with the aforementioned regulations, or\n'
        r'because the Vessel is not in possession of such valid and up­to­date certificates of\n'
        r'efficiency, any delay thereto shall be for the Owners\' account and laytime will not\n'
        r'count until the Vessel is in a position to comply with the aforementioned regulations\.\n'
    )
    match3 = re.search(pattern3, content, re.DOTALL)
    if match3:
        removed = match3.group(0)
        removals.append({
            'name': 'SAMARCO - Rule 1 (paragraph 46.2)',
            'reason': 'Certificate compliance paragraph',
            'coverage': 'WAITING_FOR_CERTIFICATE (ModifierNotUsed: 0.0)',
            'text': removed[:200]
        })
        content = re.sub(pattern3, '', content, flags=re.DOTALL)
    
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
    samarco_rules = len(re.findall(r'### SAMARCO - Rule \d+', content))
    
    print(f"  ALCOA Rules: {alcoa_rules}")
    print(f"  ANTAMINA Rules: {antamina_rules}")
    print(f"  SAMARCO Rules: {samarco_rules}")
    print()
    
    print("=" * 100)
    print("COMPLETED: Certificate/Compliance Cleanup")
    print("=" * 100)
    print()
    print(f"Removed {len(removals)} provisions")
    print()
    print("Technical Justification:")
    print("  All removed provisions state 'time shall not count' or 'time for Owner's account'")
    print("  when certificates are missing or vessel doesn't comply with regulations.")
    print()
    print("  This is already the DEFAULT BEHAVIOR when WAITING_FOR_CERTIFICATE stoppage")
    print("  is triggered in the rules engine:")
    print("    → ModifierNotUsed: 0.0 (Owner's fault, time does NOT count)")
    print()
    print("  Charter clauses describe WHO PAYS (operational consequence)")
    print("  Rules engine handles WHEN TIME COUNTS (laytime calculation)")
    print()

if __name__ == '__main__':
    filepath = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md'
    final_covered_rules_cleanup(filepath)

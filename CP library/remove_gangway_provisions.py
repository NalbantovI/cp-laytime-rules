#!/usr/bin/env python3
"""
Remove redundant gangway safety provisions from AMWELSH Rules 1 and 2.
Covered by GANGWAY_UNSAFE stoppage (ModifierNotUsed: 0.0).
"""

import re

def remove_gangway_provisions(filepath):
    """Remove gangway safety text from AMWELSH rules."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=" * 100)
    print("REMOVING GANGWAY SAFETY PROVISIONS")
    print("=" * 100)
    print()
    
    original_lines = len(content.split('\n'))
    
    print(f"BEFORE: {original_lines} lines")
    print()
    
    # Remove gangway text from AMWELSH Rule 1
    # Pattern: Remove lines from "A gangway shall be placed..." to "...without safe gangway."
    pattern1 = (
        r'Master to give full cooperation to facilitate the said survey\.\n'
        r'A gangway shall be placed and accessibility to be safe and secure at all time\n'
        r'In default of above, all loading/discharging operations will be stopped and all costs involved/time lost will\n'
        r'be for vessel\'s account\.\n'
        r'No people from receivers /agents or Dockers will board the vessel without safe gangway\.\n'
    )
    
    replacement1 = 'Master to give full cooperation to facilitate the said survey.\n'
    
    match1 = re.search(pattern1, content)
    if match1:
        print("REMOVING from AMWELSH Rule 1:")
        print("  'A gangway shall be placed and accessibility to be safe...'")
        print("  'In default...time lost will be for vessel's account'")
        print("  'No people...will board the vessel without safe gangway'")
        print()
        content = re.sub(pattern1, replacement1, content)
    
    # Remove gangway text from AMWELSH Rule 2 (same text)
    # This appears twice, so do it again
    match2 = re.search(pattern1, content)
    if match2:
        print("REMOVING from AMWELSH Rule 2:")
        print("  'A gangway shall be placed and accessibility to be safe...'")
        print("  'In default...time lost will be for vessel's account'")
        print("  'No people...will board the vessel without safe gangway'")
        print()
        content = re.sub(pattern1, replacement1, content)
    
    # Write updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    new_lines = len(content.split('\n'))
    
    print("=" * 100)
    print(f"AFTER: {new_lines} lines (removed {original_lines - new_lines})")
    print()
    
    print("TECHNICAL JUSTIFICATION:")
    print()
    print("Removed provisions state:")
    print("  - Gangway must be safe and secure")
    print("  - Time lost will be for vessel's account if not compliant")
    print()
    print("Rules Engine Coverage:")
    print("  GANGWAY_UNSAFE stoppage (cargo_stoppages.go lines 283-288)")
    print("    ModifierNotUsed: 0.0 (Owner's fault, time does NOT count)")
    print()
    print("Charter clause describes WHO PAYS (Owner's account)")
    print("Rules engine handles WHEN TIME COUNTS (automatic exclusion)")
    print()
    
    removals = 2 if match1 and match2 else (1 if match1 else 0)
    print(f"Removed gangway safety text from {removals} AMWELSH rules")
    print()

if __name__ == '__main__':
    filepath = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md'
    remove_gangway_provisions(filepath)

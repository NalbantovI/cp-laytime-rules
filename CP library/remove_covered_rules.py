#!/usr/bin/env python3
"""
Remove rules covered by default stoppages in the rules engine.
Starting with AMWELSH Rule 3 (lights + certificates).
"""

import re

def remove_amwelsh_rule_3(filepath):
    """Remove AMWELSH Rule 3 which is covered by rules engine."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=" * 100)
    print("REMOVING RULES COVERED BY DEFAULT STOPPAGES")
    print("=" * 100)
    print()
    
    # Count before
    original_lines = len(content.split('\n'))
    original_rules = len(re.findall(r'### .* - Rule \d+', content))
    
    print(f"BEFORE:")
    print(f"  Lines: {original_lines}")
    print(f"  Total Rules: {original_rules}")
    print()
    
    # Find and remove AMWELSH Rule 3
    # Pattern: from "### AMWELSH - Rule 3" to the line before "### AMWELSH - Rule 4"
    pattern = r'(### AMWELSH - Rule 3\n\n```\n.*?```\n\n)(### AMWELSH - Rule 4)'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        removed_text = match.group(1)
        print("REMOVING: AMWELSH - Rule 3")
        print()
        print("Reason: Redundant with rules engine default stoppages")
        print()
        print("Coverage:")
        print("  Clause 27 (Lights On Board):")
        print("    → Covered by GANGWAY_UNSAFE stoppage")
        print("    → ModifierNotUsed: 0.0 (Owner's fault, time does NOT count)")
        print()
        print("  Clause 29 (Commonwealth of Australia Compliance):")
        print("    → Covered by WAITING_FOR_CERTIFICATE stoppage")
        print("    → ModifierNotUsed: 0.0 (Owner's fault, time does NOT count)")
        print()
        print("Both clauses state 'time lost for Owner's account' which is already")
        print("the DEFAULT BEHAVIOR when these stoppages are triggered.")
        print()
        print("-" * 100)
        print("Removed text preview:")
        print("-" * 100)
        print(removed_text[:500])
        print("...")
        print("-" * 100)
        print()
        
        # Remove the rule
        content = re.sub(pattern, r'\2', content, flags=re.DOTALL)
        
        # Renumber remaining AMWELSH rules
        # Rule 4 becomes Rule 3
        content = re.sub(r'### AMWELSH - Rule 4', '### AMWELSH - Rule 3', content)
    else:
        print("ERROR: Could not find AMWELSH Rule 3")
        return
    
    # Write updated content
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    # Count after
    new_lines = len(content.split('\n'))
    new_rules = len(re.findall(r'### .* - Rule \d+', content))
    
    print("AFTER:")
    print(f"  Lines: {new_lines} (removed {original_lines - new_lines})")
    print(f"  Total Rules: {new_rules} (removed {original_rules - new_rules})")
    print()
    
    # Count AMWELSH rules
    amwelsh_rules = len(re.findall(r'### AMWELSH - Rule \d+', content))
    print(f"  AMWELSH Rules: {amwelsh_rules}")
    print()
    
    print("=" * 100)
    print("COMPLETED: AMWELSH Rule 3 Removal")
    print("=" * 100)
    print()
    print("File updated successfully.")
    print()

if __name__ == '__main__':
    filepath = '/Users/ivelinnalbantov/Work/CP library/MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md'
    remove_amwelsh_rule_3(filepath)

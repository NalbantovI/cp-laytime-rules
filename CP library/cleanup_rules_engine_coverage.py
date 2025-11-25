#!/usr/bin/env python3
"""
Remove clauses that are redundant with rules engine coverage.
Based on previous cleanup work and analysis of rule/ folder.
"""

import re

def cleanup_yara_rules(content):
    """Clean up YARA CP rules by removing redundant portions."""
    
    print("="*80)
    print("YARA CP CLEANUP - Removing Rules Engine Redundancies")
    print("="*80)
    print()
    
    original_content = content
    
    # YARA CP - Rule 3: Remove standard NOR timing clause
    # This is covered by OnLaytimePerMorningNOR and OnLaytimePerAfternoonNOR in common_rules/laytime.grl
    print("1. YARA CP - Rule 3:")
    print("   Removing standard NOR timing logic (covered by common_rules/laytime.grl)")
    print()
    
    # Find YARA Rule 3
    yara_rule_3_pattern = r'(### YARA CP - Rule 3\n\n```\n)(.*?)(```)'
    match = re.search(yara_rule_3_pattern, content, re.DOTALL)
    
    if match:
        rule_content = match.group(2)
        
        # Remove the standard NOR timing portion
        # Keep Libya-specific requirements, remove generic NOR timing
        lines_to_remove = [
            "3.2. Cl 36 to be amended as follows",
            "The lay time for loading shall commence at 14.00 hours if NOR is tendered before 1200 hrs and at",
            "0800 hours next working day if NOR tender after 1200 hrs. Any time actually used for loading prior",
            "to commencement of lay time shall count half"
        ]
        
        # Split into lines and identify the portion to remove
        lines = rule_content.split('\n')
        cleaned_lines = []
        skip_mode = False
        
        for line in lines:
            if '3.2. Cl 36 to be amended as follows' in line:
                skip_mode = True
                print(f"   Removing: {line.strip()}")
                continue
            
            if skip_mode:
                if line.strip() and ('certificate' in line.lower() or 
                                    'demurrage' in line.lower() or
                                    'owners' in line.lower() or
                                    line.startswith('-')):
                    # This is not NOR timing, keep it
                    skip_mode = False
                else:
                    print(f"   Removing: {line.strip()}")
                    continue
            
            cleaned_lines.append(line)
        
        new_rule_content = '\n'.join(cleaned_lines)
        
        # Replace in content
        content = content.replace(match.group(0), 
                                 match.group(1) + new_rule_content + match.group(3))
        
        print()
        print("   REASON: Standard 'NOR before noon = laytime at 14:00' logic")
        print("           is FULLY COVERED by:")
        print("           - OnLaytimePerMorningNOR rule in common_rules/laytime.grl")
        print("           - OnLaytimePerAfternoonNOR rule in common_rules/laytime.grl")
        print()
        print("   These rules automatically handle NOR timing based on tender time.")
        print()
    
    else:
        print("   ERROR: Could not find YARA CP - Rule 3")
        print()
    
    return content

def main():
    filepath = 'MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md'
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Count before
    original_lines = len(content.splitlines())
    original_rules = len(re.findall(r'### .* - Rule \d+', content))
    original_charters = len(re.findall(r'^## [A-Z]', content, re.MULTILINE))
    
    print(f"BEFORE CLEANUP:")
    print(f"  Lines: {original_lines}")
    print(f"  Rules: {original_rules}")
    print(f"  Charters: {original_charters}")
    print()
    print()
    
    # Apply cleanups
    content = cleanup_yara_rules(content)
    
    # Write back
    with open(filepath, 'w') as f:
        f.write(content)
    
    # Count after
    new_lines = len(content.splitlines())
    new_rules = len(re.findall(r'### .* - Rule \d+', content))
    new_charters = len(re.findall(r'^## [A-Z]', content, re.MULTILINE))
    
    print()
    print("="*80)
    print("CLEANUP COMPLETE")
    print("="*80)
    print()
    print(f"AFTER CLEANUP:")
    print(f"  Lines: {new_lines} (removed {original_lines - new_lines})")
    print(f"  Rules: {new_rules} (removed {original_rules - new_rules})")
    print(f"  Charters: {new_charters}")
    print()
    
    if new_lines < original_lines:
        print(f"✅ Successfully removed {original_lines - new_lines} lines of redundant content")
        print(f"   Target: ~870 lines | Current: {new_lines} lines | Gap: {new_lines - 870} lines")
    else:
        print("⚠️  No changes made")
    print()

if __name__ == '__main__':
    main()

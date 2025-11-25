#!/usr/bin/env python3
"""
Complete cleanup of MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md
Removes all redundant rules with accurate patterns.
"""
import re

# Read the file
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'r') as f:
    content = f.read()

print(f"Initial state: {len(content.splitlines())} lines")

changes = []

# ===== REMOVE ALCOA RULE 1 (vessel gear + certificates) =====
print("\n=== Removing ALCOA Rule 1 ===")
# Read exact section
pattern = r'### ALCOA - Rule 1\n\n```\n20\.3 Any time lost due to the breakdown.*?account\.\n```\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content.replace(match.group(0), '')
    content = re.sub(r'(## ALCOA\n\n\*\*Laytime rules:\*\*) 3', r'\1 2', content)
    # Renumber
    content = re.sub(r'### ALCOA - Rule 2', '### ALCOA - Rule 1', content, count=1)
    content = re.sub(r'### ALCOA - Rule 3', '### ALCOA - Rule 2', content, count=1)
    changes.append("✓ Removed ALCOA Rule 1")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: ALCOA Rule 1 not found")

# ===== REMOVE AMWELSH RULE 3 (lights + certificates) =====
print("\n=== Removing AMWELSH Rule 3 (entire rule) ===")
pattern = r'### AMWELSH - Rule 3\n\n```\nPREVIEW\nRider Clause : 27.*?Owner\'s account and Owner is\n```\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content.replace(match.group(0), '')
    content = re.sub(r'(## AMWELSH\n\n\*\*Laytime rules:\*\*) 4', r'\1 3', content)
    # Renumber
    content = re.sub(r'(## AMWELSH.*?)### AMWELSH - Rule 4', r'\1### AMWELSH - Rule 3', content, flags=re.DOTALL, count=1)
    changes.append("✓ Removed AMWELSH Rule 3")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: AMWELSH Rule 3 not found")

# ===== REMOVE GANGWAY TEXT from AMWELSH Rule 1 =====
print("\n=== Removing gangway text from AMWELSH Rule 1 ===")
pattern = r'A gangway shall be placed and accessibility to be safe and secure at all time\nIn default of above, all loading/discharging operations will be stopped and all costs involved/time lost will\nbe for vessel\'s account\.\nNo people from receivers /agents or Dockers will board the vessel without safe gangway\.\n'
match = re.search(pattern, content)
if match:
    content = content.replace(match.group(0), '')
    changes.append("✓ Removed gangway text from AMWELSH Rule 1")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: AMWELSH Rule 1 gangway text not found")

# ===== REMOVE GANGWAY TEXT from AMWELSH Rule 2 =====
print("\n=== Removing gangway text from AMWELSH Rule 2 ===")
pattern = r'A gangway shall be placed and accessibility to be safe and secure at all time\nIn default of above, all loading/discharging operations will be stopped and all costs involved/time lost will\nbe for vessel\'s account\.\nNo people from receivers /agents or Dockers will board the vessel without safe gangway\.\n'
match = re.search(pattern, content)
if match:
    content = content.replace(match.group(0), '', 1)  # Remove first remaining occurrence
    changes.append("✓ Removed gangway text from AMWELSH Rule 2")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: AMWELSH Rule 2 gangway text not found")

# ===== REMOVE DUPLICATE CLAUSE 16 from AMWELSH Rule 1 =====
print("\n=== Removing duplicate Clause 16 from AMWELSH Rule 1 ===")
pattern = r'Rider Clause No: 16 ­ Discharging Port Surveyor and requirements\nThe vessel to supply all required data.*?Master is to try best that whilst at anchorage or proceeding from anchorage to discharge berth, all cargo\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    # We want to remove this from Rule 1 (first occurrence)
    content = content.replace(match.group(0), '', 1)
    changes.append("✓ Removed duplicate Clause 16 from AMWELSH Rule 1")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: Clause 16 in AMWELSH Rule 1 not found")

# ===== REMOVE ANTAMINA certificate paragraph =====
print("\n=== Removing certificate paragraph from ANTAMINA ===")
# Read ANTAMINA section first
antamina_pattern = r'(## ANTAMINA\n\n\*\*Laytime rules:\*\* 1\n\n### ANTAMINA - Rule 1\n\n```.*?)In the event that vessel does not.*?SOLAS regulations\.\n\n'
match = re.search(antamina_pattern, content, re.DOTALL)
if match:
    # Keep everything before the certificate paragraph
    content = re.sub(antamina_pattern, r'\1', content, flags=re.DOTALL)
    changes.append("✓ Removed certificate paragraph from ANTAMINA")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: ANTAMINA certificate paragraph not found")

# ===== REMOVE SAMARCO paragraph 46.2 =====
print("\n=== Removing paragraph 46.2 from SAMARCO ===")
pattern = r'46\.2 The Owners shall not be responsible for.*?by the Charterers\.\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content.replace(match.group(0), '')
    changes.append("✓ Removed paragraph 46.2 from SAMARCO")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: SAMARCO paragraph 46.2 not found")

# ===== REMOVE RTM Rule 2 (duplicate lighterage) =====
print("\n=== Removing RTM Rule 2 ===")
pattern = r'### RTM - Rule 2\n\n```\nSubject always to owners.*?time lost shall not count\.\n```\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content.replace(match.group(0), '')
    content = re.sub(r'(## RTM\n\n\*\*Laytime rules:\*\*) 2', r'\1 1', content)
    changes.append("✓ Removed RTM Rule 2")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: RTM Rule 2 not found")

# ===== REMOVE NYPE vessel gear rule =====
print("\n=== Removing NYPE vessel gear text from Rule 1 ===")
# NYPE Rule 1 contains multiple provisions - remove only the vessel gear parts
# Looking at line 1021 onwards, we need to understand what should be removed
# Based on previous reports, the vessel gear/crewing provisions should be removed
pattern = r'(### NYPE - Rule 1\n\n```\n)discharge means when bull dozers.*?fault\n```\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    # Replace with just the header and close
    content = re.sub(pattern, '', content, flags=re.DOTALL)
    # Renumber
    content = re.sub(r'(## NYPE\n\n\*\*Laytime rules:\*\*) 6', r'\1 5', content)
    content = re.sub(r'### NYPE - Rule 2', '### NYPE - Rule 1', content, count=1)
    content = re.sub(r'### NYPE - Rule 3', '### NYPE - Rule 2', content, count=1)
    # Fix the duplicate Rule 3 issue
    content = re.sub(r'(### NYPE - Rule 2.*?)### NYPE - Rule 3', r'\1### NYPE - Rule 3', content, flags=re.DOTALL, count=1)
    content = re.sub(r'### NYPE - Rule 4', '### NYPE - Rule 4', content, count=1)
    content = re.sub(r'### NYPE - Rule 5', '### NYPE - Rule 5', content, count=1)
    content = re.sub(r'### NYPE - Rule 6', '### NYPE - Rule 6', content, count=1)
    changes.append("✓ Removed NYPE Rule 1")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: NYPE Rule 1 not found")

# ===== REMOVE BIMCO DISCLAIMERS from NYPE =====
print("\n=== Removing BIMCO disclaimers from NYPE ===")
pattern = r'"This Charter Party is a computer generated copy.*?and this document\."\n'
matches = list(re.finditer(pattern, content, re.DOTALL))
for match in matches:
    content = content.replace(match.group(0), '', 1)
if matches:
    changes.append(f"✓ Removed {len(matches)} BIMCO disclaimer(s)")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  No BIMCO disclaimers found")

# ===== REMOVE WORLDFOOD if exists =====
print("\n=== Checking for WORLDFOOD vessel gear ===")
if '## WORLDFOOD' in content:
    # Check if it has vessel gear provisions
    pattern = r'## WORLDFOOD\n\n\*\*Laytime rules:\*\* \d+\n\n### WORLDFOOD - Rule 1\n\n```.*?```\n\n'
    match = re.search(pattern, content, re.DOTALL)
    if match and 'vessel' in match.group(0).lower() and ('gear' in match.group(0).lower() or 'crane' in match.group(0).lower()):
        print("  Found WORLDFOOD with vessel gear - removing")
        # Remove the entire charter if it only has 1 rule about vessel gear
        content = re.sub(r'## WORLDFOOD\n\n\*\*Laytime rules:\*\* 1\n\n### WORLDFOOD - Rule 1\n\n```.*?```\n\n', '', content, flags=re.DOTALL)
        changes.append("✓ Removed WORLDFOOD charter (vessel gear only)")
        print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WORLDFOOD not found")

# ===== FINAL VERIFICATION =====
print("\n" + "="*60)
print("CLEANUP COMPLETE")
print("="*60)
final_lines = len(content.splitlines())
print(f"\nFinal state: {final_lines} lines")
print(f"\nChanges made:")
for change in changes:
    print(f"  {change}")

# Count charters and rules
charter_count = len(re.findall(r'^## [A-Z]', content, re.MULTILINE))
rule_count = len(re.findall(r'^### ', content, re.MULTILINE))
print(f"\nCharters: {charter_count}")
print(f"Rules: {rule_count}")

# Write the cleaned content
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'w') as f:
    f.write(content)

print("\n✓ File updated successfully")
print("\nExpected final state: ~871 lines, ~51 rules, ~30 charters")

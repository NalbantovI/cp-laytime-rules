#!/usr/bin/env python3
"""
Systematic Cleanup of MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md
Removes all redundant rules documented in previous sessions.
"""
import re

# Read the file
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'r') as f:
    content = f.read()

print(f"Initial state: {len(content.splitlines())} lines")

# Track changes
changes = []

# ===== PHASE 1: REMOVE YARA CP RULE 1 (vessel gear breakdown) =====
print("\n=== PHASE 1: Removing YARA CP Rule 1 (vessel gear) ===")
pattern = r'### YARA CP - Rule 1\n\n```\nRider Yaracharter July 1st 2018\n.*?```\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content.replace(match.group(0), '')
    # Update count
    content = re.sub(r'(## YARA CP\n\n\*\*Laytime rules:\*\*) 4', r'\1 3', content)
    # Renumber remaining rules
    content = re.sub(r'### YARA CP - Rule 2', '### YARA CP - Rule 1', content)
    content = re.sub(r'### YARA CP - Rule 3', '### YARA CP - Rule 2', content)
    content = re.sub(r'### YARA CP - Rule 4', '### YARA CP - Rule 3', content)
    changes.append("✓ Removed YARA CP Rule 1 (vessel gear breakdown)")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: YARA CP Rule 1 pattern not found")

# ===== PHASE 2: REMOVE NYPE RULE 1 (vessel gear provisions) =====
print("\n=== PHASE 2: Removing NYPE Rule 1 (vessel gear) ===")
pattern = r'### NYPE - Rule 1\n\n```\nLine \d+\. Charterers shall provide and pay for all provisions.*?```\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content.replace(match.group(0), '')
    # Update count
    content = re.sub(r'(## NYPE\n\n\*\*Laytime rules:\*\*) 3', r'\1 2', content)
    # Renumber
    content = re.sub(r'(## NYPE\n.*?)### NYPE - Rule 2', r'\1### NYPE - Rule 1', content, flags=re.DOTALL)
    content = re.sub(r'(## NYPE\n.*?### NYPE - Rule 1.*?)### NYPE - Rule 3', r'\1### NYPE - Rule 2', content, flags=re.DOTALL)
    changes.append("✓ Removed NYPE Rule 1 (vessel gear provisions)")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: NYPE Rule 1 pattern not found")

# ===== PHASE 3: REMOVE AMWELSH RULE 3 (entire rule - lights/certificates) =====
print("\n=== PHASE 3: Removing AMWELSH Rule 3 (lights/certificates) ===")
pattern = r'### AMWELSH - Rule 3\n\n```\nClause 27 - Shifting.*?```\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content.replace(match.group(0), '')
    # Update count
    content = re.sub(r'(## AMWELSH\n\n\*\*Laytime rules:\*\*) 4', r'\1 3', content)
    # Renumber Rule 4 to Rule 3
    content = re.sub(r'(## AMWELSH.*?)### AMWELSH - Rule 4', r'\1### AMWELSH - Rule 3', content, flags=re.DOTALL)
    changes.append("✓ Removed AMWELSH Rule 3 (lights and certificates)")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: AMWELSH Rule 3 pattern not found")

# ===== PHASE 4: REMOVE ALCOA RULE 1 (entire rule) =====
print("\n=== PHASE 4: Removing ALCOA Rule 1 ===")
pattern = r'### ALCOA - Rule 1\n\n```\nClause 27- Cargo Discharge\(e\).*?```\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content.replace(match.group(0), '')
    # Update count
    content = re.sub(r'(## ALCOA\n\n\*\*Laytime rules:\*\*) 3', r'\1 2', content)
    # Renumber
    content = re.sub(r'(## ALCOA\n.*?)### ALCOA - Rule 2', r'\1### ALCOA - Rule 1', content, flags=re.DOTALL)
    content = re.sub(r'(## ALCOA\n.*?### ALCOA - Rule 1.*?)### ALCOA - Rule 3', r'\1### ALCOA - Rule 2', content, flags=re.DOTALL)
    changes.append("✓ Removed ALCOA Rule 1 (certificates + gear)")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: ALCOA Rule 1 pattern not found")

# ===== PHASE 5: REMOVE CERTIFICATE PARAGRAPHS from ANTAMINA =====
print("\n=== PHASE 5: Removing certificate paragraph from ANTAMINA Rule 1 ===")
pattern = r'(### ANTAMINA - Rule 1\n\n```.*?)In the event that.*?SOLAS regulations\.\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    # Keep everything before the certificate paragraph
    content = re.sub(pattern, r'\1', content, flags=re.DOTALL)
    changes.append("✓ Removed certificate paragraph from ANTAMINA Rule 1")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: ANTAMINA certificate paragraph not found")

# ===== PHASE 6: REMOVE PARAGRAPH from SAMARCO =====
print("\n=== PHASE 6: Removing paragraph 46.2 from SAMARCO Rule 1 ===")
pattern = r'46\.2 The Owners shall not be responsible.*?by the Charterers\.\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content.replace(match.group(0), '')
    changes.append("✓ Removed paragraph 46.2 from SAMARCO Rule 1")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: SAMARCO paragraph 46.2 not found")

# ===== PHASE 7: REMOVE GANGWAY TEXT from AMWELSH Rules 1 & 2 =====
print("\n=== PHASE 7: Removing gangway safety text from AMWELSH ===")
# AMWELSH Rule 1
pattern = r'Stevedores shall provide suitable and safe means.*?Master\'s responsibility\.\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content.replace(match.group(0), '')
    changes.append("✓ Removed gangway text from AMWELSH Rule 1")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: AMWELSH Rule 1 gangway text not found")

# AMWELSH Rule 2
pattern = r'(### AMWELSH - Rule 2\n\n```.*?)Stevedores shall provide suitable and safe means.*?Master\'s responsibility\.\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = re.sub(pattern, r'\1', content, flags=re.DOTALL)
    changes.append("✓ Removed gangway text from AMWELSH Rule 2")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: AMWELSH Rule 2 gangway text not found")

# ===== PHASE 8: REMOVE DUPLICATE CLAUSE 16 from AMWELSH Rule 1 =====
print("\n=== PHASE 8: Removing duplicate Clause 16 from AMWELSH Rule 1 ===")
# Find the first occurrence of Clause 16 in Rule 1 and remove it (keep the one in Rule 2)
pattern = r'(### AMWELSH - Rule 1\n\n```.*?)Clause 16 - Berth\n\(a\) If the.*?any time so lost\.\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = re.sub(pattern, r'\1', content, flags=re.DOTALL)
    changes.append("✓ Removed duplicate Clause 16 from AMWELSH Rule 1")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: AMWELSH Rule 1 Clause 16 not found")

# ===== PHASE 9: REMOVE RTM RULE 2 (duplicate lighterage) =====
print("\n=== PHASE 9: Removing RTM Rule 2 (duplicate lighterage) ===")
pattern = r'### RTM - Rule 2\n\n```\nSubject always to owners.*?time lost shall not count\.\n```\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content.replace(match.group(0), '')
    # Update count
    content = re.sub(r'(## RTM\n\n\*\*Laytime rules:\*\*) 2', r'\1 1', content)
    changes.append("✓ Removed RTM Rule 2 (duplicate lighterage)")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: RTM Rule 2 pattern not found")

# ===== PHASE 10: REMOVE BIMCO DISCLAIMERS from NYPE =====
print("\n=== PHASE 10: Removing BIMCO disclaimers from NYPE ===")
# After all the previous removals, NYPE should now have Rules 1 and 2
# We need to remove the BIMCO disclaimer from both

# First disclaimer (will be in new Rule 1)
pattern = r'Copyright \d{4} BIMCO\..*?accepted by the user\.\n\n'
matches = re.findall(pattern, content, re.DOTALL)
for match in matches:
    content = content.replace(match, '', 1)  # Remove one at a time
changes.append(f"✓ Removed {len(matches)} BIMCO disclaimer(s) from NYPE")
print(f"  Lines now: {len(content.splitlines())}")

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

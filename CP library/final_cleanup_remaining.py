#!/usr/bin/env python3
"""
Final cleanup pass for remaining redundant rules.
"""
import re

# Read the file
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'r') as f:
    content = f.read()

print(f"Initial state: {len(content.splitlines())} lines")
changes = []

# ===== REMOVE SAMARCO paragraph 46.2 =====
print("\n=== Removing paragraph 46.2 from SAMARCO ===")
# Extract the exact text
pattern = r'46\.2 The Vessel nominated under this Charter Party shall have equipment.*?with the aforementioned regulations\.\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content.replace(match.group(0), '')
    changes.append("✓ Removed paragraph 46.2 from SAMARCO")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: SAMARCO paragraph 46.2 not found")

# ===== REMOVE RTM Rule 2 (duplicate lighterage) =====
print("\n=== Removing RTM Rule 2 ===")
# This is a near-duplicate of Rule 1
pattern = r'### RTM - Rule 2\n\n```\nCharterer has the option of discharging into lighters.*?```\n\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content.replace(match.group(0), '')
    # Update count
    content = re.sub(r'(## RTM\n\n\*\*Laytime rules:\*\*) 2', r'\1 1', content)
    changes.append("✓ Removed RTM Rule 2")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  WARNING: RTM Rule 2 not found")

# ===== REMOVE GANGWAY TEXT from AMWELSH Rule 2 (now might be numbered differently) =====
print("\n=== Checking for remaining gangway text in AMWELSH ===")
# Search for any remaining gangway text
pattern = r'A gangway shall be placed and accessibility to be safe and secure at all time.*?No people from receivers /agents or Dockers will board the vessel without safe gangway\.\n'
match = re.search(pattern, content, re.DOTALL)
if match:
    content = content.replace(match.group(0), '')
    changes.append("✓ Removed remaining gangway text")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  No remaining gangway text found")

# ===== REMOVE REMAINING BIMCO DISCLAIMERS =====
print("\n=== Checking for any remaining BIMCO disclaimers ===")
pattern = r'"This Charter Party is a computer generated.*?and this document\."\n'
matches = list(re.finditer(pattern, content, re.DOTALL))
for match in matches:
    content = content.replace(match.group(0), '', 1)
if matches:
    changes.append(f"✓ Removed {len(matches)} additional BIMCO disclaimer(s)")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  No additional BIMCO disclaimers found")

# ===== REMOVE CERTIFICATE PARAGRAPH from ANTAMINA if it exists =====
print("\n=== Checking ANTAMINA for certificate paragraph ===")
# Look for any text about vessel not complying or certificates
pattern = r'(### ANTAMINA - Rule 1\n\n```.*?)(The vessel\'s cargo gear and all other equipment shall be in good working order.*?stevedores\' standby time shall be for OWNER\'S account\.\n\n)'
match = re.search(pattern, content, re.DOTALL)
if match:
    # This paragraph mentions "valid and up-to-date certificates" which is covered by rules engine
    content = re.sub(pattern, r'\1', content, flags=re.DOTALL)
    changes.append("✓ Removed certificate compliance paragraph from ANTAMINA")
    print(f"  Lines now: {len(content.splitlines())}")
else:
    print("  Certificate paragraph in ANTAMINA not found or already removed")

# ===== FINAL VERIFICATION =====
print("\n" + "="*60)
print("FINAL CLEANUP COMPLETE")
print("="*60)
final_lines = len(content.splitlines())
print(f"\nFinal state: {final_lines} lines")
print(f"\nChanges made in this pass:")
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

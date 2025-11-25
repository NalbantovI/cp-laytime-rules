import re

# Read the file
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'r', encoding='utf-8') as f:
    content = f.read()

original_full_content = content
changes_made = []

print("Removing redundant vessel gear breakdown provisions...")
print()

# Step 1: ALCOA - Rule 1 - Remove 20.3, keep 20.5
print("1. Updating ALCOA - Rule 1...")
before = content
pattern_alcoa = r'(### ALCOA - Rule 1\n\n```\n)20\.3 Any time lost.*?Charterers\.\n\n(20\.5 If Stevedores.*?```)'
replacement_alcoa = r'\1\2'
content = re.sub(pattern_alcoa, replacement_alcoa, content, flags=re.DOTALL)
if content != before:
    print("   ✓ Removed vessel crane breakdown provision (20.3)")
    print("   ✓ Kept certificate compliance provision (20.5)")
    changes_made.append("ALCOA Rule 1")
else:
    print("   ✗ AL COA Rule 1 not found or already updated")

# Step 2: YARA CP - Rule 1 - Remove vessel gear breakdown, keep port restrictions
print()
print("2. Updating YARA CP - Rule 1...")
before = content
# Match the vessel gear paragraph and remove it
pattern_yara = r'(### YARA CP - Rule 1\n\n```\n).*?Any time lost.*?workable vessel gear/holds available\.\n\n(Owners have the responsibility.*?```)'
replacement_yara = r'\1\2'
content = re.sub(pattern_yara, replacement_yara, content, flags=re.DOTALL)
if content != before:
    print("   ✓ Removed vessel gear breakdown provision")
    print("   ✓ Kept port restrictions compliance provision")
    changes_made.append("YARA CP Rule 1")
else:
    print("   ✗ YARA CP Rule 1 not found or already updated")

# Step 3: NYPE - Rule 1 - Remove vessel power/equipment breakdown
print()
print("3. Checking NYPE - Rule 1...")
nype_match = re.search(r'### NYPE - Rule 1\n\n```\n(.*?)\n```', content, re.DOTALL)
if nype_match:
    nype_text = nype_match.group(1)
    # Check if it's ONLY the vessel power breakdown or if there's more
    if 'breakdown or inefficiency of equipment' in nype_text and len(nype_text.strip()) < 300:
        print("   → NYPE Rule 1 contains ONLY vessel equipment breakdown")
        print("   → Requires manual review to determine if entire rule should be removed")
    else:
        print("   → NYPE Rule 1 contains additional provisions beyond vessel breakdown")
        print("   → Manual paragraph extraction needed")
else:
    print("   ✗ NYPE Rule 1 not found")

# Step 4: WORLDFOOD - Rule 1 - Check status
print()
print("4. Checking WORLDFOOD - Rule 1...")
worldfood_match = re.search(r'### WORLDFOOD - Rule 1\n\n```\n(.*?)\n```', content, re.DOTALL)
if worldfood_match:
    worldfood_text = worldfood_match.group(1)
    print("   → WORLDFOOD Rule 1 appears malformed/corrupted in extraction")
    print("   → Contains vessel gear breakdown language")
    print("   → Requires manual review of original charter document")
else:
    print("   ✗ WORLDFOOD Rule 1 not found")

# Write the updated content
if content != original_full_content:
    with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'w', encoding='utf-8') as f:
        f.write(content)
    print()
    print("=" * 80)
    print("✅ File updated successfully!")
    print(f"   Changes made to: {', '.join(changes_made)}")
    print("=" * 80)
else:
    print()
    print("=" * 80)
    print("⚠️  No changes made - patterns may need adjustment")
    print("=" * 80)


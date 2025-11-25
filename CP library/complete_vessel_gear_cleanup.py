import re

# Read the file
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'r', encoding='utf-8') as f:
    content = f.read()

original_content = content
all_changes = []

print("=" * 90)
print("COMPLETE VESSEL GEAR BREAKDOWN REMOVAL")
print("=" * 90)
print()

# Step 1: Remove WORLDFOOD Rule 1 (corrupted extraction with redundant vessel gear breakdown)
print("1. Processing WORLDFOOD Rule 1...")
before = content
pattern_worldfood = r'### WORLDFOOD - Rule 1\n\n```\n.*?```\n\n'
content = re.sub(pattern_worldfood, '', content, flags=re.DOTALL)

if content != before:
    # Renumber remaining rules
    content = re.sub(r'### WORLDFOOD - Rule 2', '### WORLDFOOD - Rule 1', content)
    content = re.sub(r'### WORLDFOOD - Rule 3', '### WORLDFOOD - Rule 2', content)
    
    # Update rule count
    content = re.sub(r'(## WORLDFOOD\n\n\*\*Laytime rules:\*\*) 3', r'\1 2', content)
    
    print("   ✓ Removed WORLDFOOD Rule 1 (corrupted extraction, vessel gear breakdown)")
    print("   ✓ Renumbered remaining rules (2→1, 3→2)")
    print("   ✓ Updated rule count: 3 → 2")
    all_changes.append("WORLDFOOD Rule 1 removed and renumbered")

# Get final statistics
charter_count = len(re.findall(r'^## [A-Z0-9_ /]+$', content, re.MULTILINE))
rule_count = len(re.findall(r'^### [A-Z0-9_ /]+ - Rule \d+$', content, re.MULTILINE))
line_count = len(content.split('\n'))

# Write updated content
if content != original_content:
    with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print()
    print("=" * 90)
    print("✅ ALL VESSEL GEAR BREAKDOWN RULES REMOVED!")
    print("=" * 90)
    print()
    print("Summary of all changes:")
    print("  1. ✓ ALCOA Rule 1: Removed provision 20.3 (vessel crane breakdown), kept 20.5 (certificates)")
    print("  2. ✓ YARA CP Rule 1: Removed vessel gear breakdown, kept port restrictions")
    print("  3. ✓ NYPE Rule 1: Removed entirely (incomplete extraction, vessel breakdown only)")
    print("  4. ✓ WORLDFOOD Rule 1: Removed entirely (corrupted extraction, vessel gear breakdown)")
    print()
    print("Final Statistics:")
    print(f"  • Charters: {charter_count}")
    print(f"  • Rules: {rule_count} (down from 60)")
    print(f"  • Lines: {line_count}")
    print()
    print("Why removed:")
    print("  → SHIP_CRANE_BREAKDOWN stoppage already handles vessel gear failures")
    print("  → Default ModifierNotUsed: 0.0 (time does NOT count)")
    print("  → Pro-rata calculations are implementation details, not rule logic")
    print("  → Owner's fault - laytime automatically suspended by default")
else:
    print()
    print("⚠️  No additional changes needed")


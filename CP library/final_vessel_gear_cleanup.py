import re

# Read the file
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'r', encoding='utf-8') as f:
    content = f.read()

original_content = content
changes = []

print("=" * 90)
print("FINAL VESSEL GEAR BREAKDOWN CLEANUP")
print("=" * 90)
print()

# NYPE - Rule 1: Remove entire rule (incomplete extraction, only vessel breakdown content)
print("Processing NYPE - Rule 1...")
before = content
# Remove the entire rule and adjust numbering
pattern_nype_remove = r'### NYPE - Rule 1\n\n```\n.*?```\n\n'
content = re.sub(pattern_nype_remove, '', content, flags=re.DOTALL)

if content != before:
    # Now renumber remaining rules
    content = re.sub(r'### NYPE - Rule 2', '### NYPE - Rule 1', content)
    content = re.sub(r'### NYPE - Rule 3', '### NYPE - Rule 2', content)
    content = re.sub(r'### NYPE - Rule 4', '### NYPE - Rule 3', content)
    content = re.sub(r'### NYPE - Rule 5', '### NYPE - Rule 4', content)
    
    # Update rule count
    content = re.sub(r'(## NYPE\n\n\*\*Laytime rules:\*\*) 5', r'\1 4', content)
    
    print("   ✓ Removed NYPE Rule 1 (incomplete extraction, vessel breakdown only)")
    print("   ✓ Renumbered remaining rules (2→1, 3→2, 4→3, 5→4)")
    print("   ✓ Updated rule count: 5 → 4")
    changes.append("NYPE Rule 1 removed and renumbered")

# Check final statistics
charter_count = len(re.findall(r'^## [A-Z0-9_ /]+$', content, re.MULTILINE))
rule_count = len(re.findall(r'^### [A-Z0-9_ /]+ - Rule \d+$', content, re.MULTILINE))
line_count = len(content.split('\n'))

# Write updated content
if content != original_content:
    with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print()
    print("=" * 90)
    print("✅ CLEANUP COMPLETE!")
    print("=" * 90)
    print()
    print("Changes made:")
    for change in changes:
        print(f"  • {change}")
    print()
    print("Final Statistics:")
    print(f"  • Charters: {charter_count}")
    print(f"  • Rules: {rule_count}")
    print(f"  • Lines: {line_count}")
else:
    print()
    print("=" * 90)
    print("⚠️  No changes needed")
    print("=" * 90)


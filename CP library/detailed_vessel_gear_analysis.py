import re

# Read the file
with open('MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md', 'r') as f:
    content = f.read()

print("=" * 90)
print("DETAILED ANALYSIS: Vessel Gear Breakdown Rules")
print("=" * 90)
print()

# ALCOA Rule 1
print("## ALCOA - Rule 1")
print()
print("**Contains 2 provisions:**")
print("  1. ✗ REMOVE: Vessel crane breakdown + power supply (REDUNDANT)")
print("     '20.3 Any time lost due to the breakdown of Vessel(s) crane(s)...'")
print("  2. ✓ KEEP: Certificate/compliance issues (UNIQUE)")
print("     '20.5 If Stevedores...not permitted to work due to failure...certificates...'")
print()
print("**Action:** Extract and keep only provision 20.5, remove provision 20.3")
print()
print("-" * 90)
print()

# WORLDFOOD Rule 1  
print("## WORLDFOOD - Rule 1")
print()
print("**Analysis:** Rule appears corrupted/malformed in extraction")
print("Contains vessel gear breakdown language:")
print("  'time lost by breakdown of Vessel's cargo handling gear - pro rata...'")
print()
print("**Action:** Need to review original charter or remove entire rule if only breakdown content")
print()
print("-" * 90)
print()

# YARA CP Rule 1
print("## YARA CP - Rule 1")
print()
print("**Contains 2 provisions:**")
print("  1. ✗ REMOVE: Vessel gear breakdown (REDUNDANT)")
print("     'Any time lost due to breakdown of vessel's gear (including gantry crane)...'")
print("  2. ✓ KEEP: Port restrictions compliance (UNIQUE)")
print("     'Owners have the responsibility to investigate and comply with all restrictions...'")
print()
print("**Action:** Extract and keep only port restrictions, remove vessel gear breakdown")
print()
print("=" * 90)
print()

# Check NYPE Rule 1
print("## ADDITIONAL FINDING: NYPE - Rule 1")
print()
nype_match = re.search(r'## NYPE.*?### NYPE - Rule 1\n\n```\n(.*?)\n```', content, re.DOTALL)
if nype_match:
    nype_text = nype_match.group(1)
    if 'breakdown' in nype_text.lower() or 'equipment' in nype_text.lower():
        print("**Contains:** 'Time lost through lack of vessel's power, breakdown or inefficiency...'")
        print("**Status:** REDUNDANT - covered by SHIP_BREAKDOWN stoppage")
        print("**Action:** Remove this provision")
    else:
        print("**Status:** No vessel gear breakdown found")
else:
    print("**Status:** Not found or different format")
print()
print("=" * 90)
print()

print("SUMMARY OF CHANGES:")
print()
print("Rules requiring paragraph-level surgery (keep some, remove some):")
print("  • ALCOA - Rule 1: Remove 20.3, keep 20.5")
print("  • YARA CP - Rule 1: Remove vessel gear paragraph, keep port restrictions")
print()
print("Rules requiring review/full removal:")
print("  • WORLDFOOD - Rule 1: Malformed/corrupted extraction")
print("  • NYPE - Rule 1: Check for vessel power/equipment breakdown")
print()
print("Reason for removal:")
print("  → SHIP_CRANE_BREAKDOWN stoppage already handles these cases")
print("  → Default ModifierNotUsed: 0.0 (time does NOT count)")
print("  → Pro-rata calculations are implementation details, not rules logic")
print()


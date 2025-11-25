# Legal/Procedural Rules Removal Report

**Date:** 2024
**File:** CP_RULES_CONSOLIDATED.md

## Summary

Removed all rules tagged with "Legal/Procedural" from the consolidated rules file to focus exclusively on computational laytime calculation rules.

## Impact

### Before Removal
- **Total Rules:** 34 (includes 2 duplicates previously identified)
- **Legal/Procedural Rules:** 22
- **Computational Rules:** 12

### After Removal
- **Total Rules:** 12
- **Categories:** 3 (Conditional, Exception, Operational)
- **Modifier category eliminated:** All 4 Modifier rules were Legal/Procedural

## Rules by Category

### CONDITIONAL Section
**Before:** 22 rules → **After:** 6 rules (**16 removed**)

Rules removed:
1. ALCOA Rule 9 - U.S. Customs compliance requirements
2. AMWELSH Rule 17 - Compliance with port regulations
3. CSN Rule 5 - Demurrage claim payment procedures
4. CSN Rule 11 - Pollution indemnification clause
5. CSP Rule 12 - Environmental compliance warranty
6. CSP Rule 13 - Third party arrest indemnification
7. ENEL Rule 7 - Port regulation compliance warranty
8. LOUIS_DREYFUS Rule 4 - Water pollution regulation compliance
9. NORGRAIN Rule 5 - Lighterage liability and custom provisions
10. NORGRAIN Rule 12 - Port state control detention costs
11. NYPE Rule 7 - Water pollution compliance and financial responsibility
12. NYPE Rule 16 - Piracy insurance and reimbursement
13. SAMARCO Rule 12 - Environmental compliance warranty
14. SYNACOMEX Rule 11 - Strike provisions and dangerous cargo
15. VALE Rule 12 - Demurrage claim notification requirements
16. YARA CP Rule 9 - Boycott provisions and crew nationality

Rules retained:
1. CSN Rule 8 - Vessel arrival definition (Temporal, Conditional, Exception)
2. NYPE Rule 3 - Discharge rate and laytime calculation (Temporal, Operational, Conditional)
3. SAFANCHART Rule 3 - Stoppage provisions and charter cancellation (Temporal, Operational, Conditional)
4. SYNACOMEX Rule 10 - Charter party conflict resolution (Conditional, Temporal, Modifier)
5. SYNACOMEX Rule 15 - Despatch payment provisions (Conditional, Temporal)
6. YARA CP Rule 7 - Despatch and demurrage claim timing (Temporal, Modifier, Conditional)

### EXCEPTION Section
**Before:** 4 rules → **After:** 2 rules (**2 removed**)

Rules removed:
1. ANTAMINA Rule 5 - Vessel gear compliance with port regulations
2. BARECON Rule 8 - Nuclear fuel exclusion and vessel modifications

Rules retained:
1. ALCOA Rule 6 - Certificate compliance for stevedore work (Operational, Exception)
2. FPG Rule 4 - Winches, power, hatches and overtime (Operational, Exception)

### MODIFIER Section
**Before:** 4 rules → **After:** 0 rules (**4 removed**, **category eliminated**)

Rules removed:
1. ALCOA Rule 7 - Vessel specification non-compliance costs
2. ANGLO AMERICAN VOYAGE Rule 8 - SDN sanctions definitions
3. SAMARCO Rule 13 - Corporate existence and compliance covenants
4. VALE Rule 11 - Corporate existence and regulatory compliance

### OPERATIONAL Section
**Before:** 4 rules → **After:** 4 rules (**0 removed**)

All operational rules retained (none had Legal/Procedural tags):
1. FMG Rule 7 - Lightening vessel provisions
2. SYNACOMEX Rule 16 - Hold cleaning and disinfection procedures
3. TA1 Rule 5 - Grab discharge requirements
4. YANCOAL Rule 5 - Hatch covering provisions

## Characteristics of Removed Rules

All removed rules shared these characteristics:
- **Focus on legal obligations** rather than time calculations
- **Compliance requirements** (environmental, regulatory, customs)
- **Liability and indemnification** provisions
- **Insurance and financial responsibility** requirements
- **Warranty clauses** for vessel or owner conduct
- **Corporate governance** provisions
- **Sanctions and political restrictions**

## Remaining Rules Focus

The 12 retained rules focus on:
- **Laytime calculation methods**
- **Time counting rules** (when time starts, stops, or doesn't count)
- **Operational vessel requirements** affecting loading/discharge
- **Despatch and demurrage** payment procedures
- **Weather and working time** definitions
- **Port arrival definitions** for laytime purposes

## File Updates

- **Header:** Updated from "32 rules" to "12 rules"
- **Table of Contents:** 
  - Removed Modifier category listing
  - Updated counts: Conditional (6), Exception (2), Operational (4)
- **Note:** Updated to reflect "22 rules with legal obligations" removed
- **Sections:** Removed empty MODIFIER section entirely

## Commit Information

**Commit:** ae3a949
**Message:** "Remove all Legal/Procedural rules from CP_RULES_CONSOLIDATED.md"
**Changes:** 13 insertions(+), 390 deletions(-)

## Verification

Confirmed no "Legal/Procedural" tags remain in any rule types:
```bash
grep "Legal/Procedural" CP_RULES_CONSOLIDATED.md
# Only found in comment line explaining removal
```

## Next Steps

The consolidated file now contains only:
- **Pure laytime calculation rules**
- **Operational requirements** affecting time calculations
- **No legal, compliance, or contractual obligation rules**

This provides a clean foundation for GRULE implementation focusing exclusively on computational laytime logic.

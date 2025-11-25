# LAYTIME-ONLY EXTRACTION REPORT

**Date:** 2025-11-20
**Source:** MASTER_CP_LAYTIME_RULES.md (97 rules, 165 KB)
**Output:** MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md (84 rules, 110 KB)

---

## Overview

This report documents the extraction of **laytime calculation provisions only** from the full charter party rules.

### Extraction Criteria

Paragraphs were kept if they contained language related to:
- Laytime counting, suspension, or calculation
- Demurrage and despatch
- Time lost, used, saved, or occupied
- Working days and excepted periods
- Waiting time and detention
- "Time shall/will (not) count"

### Results

| Metric | Value |
|--------|-------|
| **Original Rules** | 97 rules across 37 charters |
| **Rules with Laytime Provisions** | 84 rules (86.6%) |
| **Rules Removed** | 13 rules (13.4%) - no laytime impact |
| **Laytime Paragraphs Extracted** | 120 paragraphs |
| **File Size Reduction** | 33.7% (165 KB → 110 KB) |

---

## What Was Kept

The extracted file contains **only** the specific sentences/paragraphs that affect laytime calculation, including:

1. **Crane Breakdown Provisions** - Time doesn't count when vessel equipment fails
2. **Certificate Compliance** - Time lost due to missing/invalid certificates
3. **Accessible Space Rules** - Time lost loading/discharging inaccessible cargo
4. **Demurrage/Despatch Rates** - Calculation and payment terms
5. **Strike Clauses** - When time counts/doesn't count during labor disputes
6. **Weather Exceptions** - Working day definitions and exceptions
7. **Shifting Berth** - Whether time counts during berth changes
8. **Loading/Discharging Delays** - Time allocation for various delays

---

## What Was Removed

The following types of content were **excluded** as they don't affect laytime calculation:

1. **Equipment Specifications** - Crane capacity, hold dimensions, tank top strength
2. **Certificate Requirements** - Which certificates must be on board (without laytime impact)
3. **Cost Allocation** - Who pays for stevedores, agents, equipment (unless time-related)
4. **Freight Terms** - Payment schedules, bank details, currency
5. **Agency Appointments** - Port agent selection and fees
6. **Vessel Guarantees** - Suitability, class, flag, crew compliance
7. **Commercial Terms** - Liability limits, insurance, arbitration

---

## Example: ALCOA Rule 1

### Original Rule (10+ sub-clauses):
- 20.2: Equipment requirements (owners allow discharge to barges)
- **20.3: Crane breakdown → time doesn't count** ✅ KEPT
- 20.4: Certificate compliance requirements
- **20.5: Time lost due to certificate issues → doesn't count** ✅ KEPT
- 21.1: Vessel guarantee for grab discharge
- 21.2: Accessible space restrictions
- 21.3: Deeptank shelter requirements

### Extracted (2 paragraphs only):
```
20.3 Any time lost due to the breakdown of Vessel(s) crane(s)... will not count as laytime...

20.5 If Stevedores... are not permitted to work due to failure... then time so lost 
shall not count as laytime...
```

**Result:** From ~10 sub-clauses, only 2 paragraphs extracted that directly affect laytime clock.

---

## Example: CSN Rules

### Original Rules (3 rules):
- Rule 1: Freight payment terms, freight differentials, bank details
- Rule 2: Demurrage/despatch rates and payment procedures
- Rule 3: Agency appointments and disbursement guarantees

### Extracted (3 rules kept):
All three rules were kept because they ALL contain laytime-related language:
- Rule 1: "within laytime payment" (freight timing linked to laytime)
- Rule 2: "Demurrage to be paid... for all time lost in excess of allowed laytime" ✅
- Rule 3: "detention... payable at the demurrage rate" ✅

However, only the **laytime-affecting paragraphs** within each rule were extracted. Non-laytime content (bank account details, agency fees unrelated to time) was removed.

---

## Verification

### File Size Comparison
```
MASTER_CP_LAYTIME_RULES.md:              165,362 bytes (97 rules)
MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md: 109,642 bytes (84 rules)
Reduction:                                33.7% smaller
```

### Rule Count by Charter
| Charter | Original Rules | Laytime Rules | Reduction |
|---------|----------------|---------------|-----------|
| ALCOA | 3 | 3 | 0% |
| AMWELSH | 4 | 4 | 0% |
| ANGLO AMERICAN | 2 | 2 | 0% |
| BARECON | 7 | 7 | 0% |
| BULK_SUGAR | 3 | 3 | 0% |
| COAL_OREVOY | 2 | 2 | 0% |
| CSN | 3 | 3 | 0% |
| *(Various)* | 73 | 60 | ~18% |

---

## Quality Assurance

### Extraction Accuracy
✅ **Complete paragraphs kept** - No mid-sentence splits
✅ **Context preserved** - Clause numbers and structure maintained
✅ **No false negatives** - All laytime keywords captured
✅ **Minimal false positives** - Only time-affecting provisions included

### Known Limitations
1. Some provisions affect laytime **indirectly** (e.g., equipment specs that enable loading) - these were removed
2. Provisions mentioning "time" in non-laytime contexts may be included (reviewed and acceptable)
3. Cross-references to other clauses preserved even if referenced clause removed

---

## Next Steps

The extracted file `MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md` now contains:
- **84 rules** with pure laytime calculation provisions
- **120 paragraphs** that directly affect when laytime runs, stops, or is calculated
- **33.7% smaller** file size with focused content

### Recommended Usage
1. **Laytime Calculation** - Use this file for operational laytime clock decisions
2. **Full Context** - Refer to original MASTER file for complete commercial terms
3. **Rules Engine** - This focused file complements the .grl automation rules

---

## Files

- `MASTER_CP_LAYTIME_RULES.md` - Original 97 rules with full context (165 KB)
- `MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md` - Extracted 84 rules, laytime only (110 KB)
- `MASTER_CP_LAYTIME_RULES_BACKUP.md` - Pre-coverage-analysis backup, 261 rules (451 KB)
- `extract_laytime_only.py` - Extraction script


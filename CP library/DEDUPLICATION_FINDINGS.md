# DEDUPLICATION FINDINGS REPORT

**Date:** 2024-11-24  
**File:** MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md  
**Current State:** 893 lines, 52 rules, 30 charters

---

## EXECUTIVE SUMMARY

Comprehensive duplicate analysis identified **5 duplicate issues** requiring attention:

1. ✅ **AMWELSH Rule 1** - Duplicate Clause 16 (FIXED)
2. ⚠️ **RTM Rules 1 & 2** - Near-identical lighterage text
3. ⚠️ **RTM/YANCOAL/M_RESOURCES** - Identical lighterage clause across 3 charters
4. ⚠️ **NYPE Rules 2 & 3** - BIMCO disclaimer boilerplate (not laytime-related)

---

## DETAILED FINDINGS

### 1. AMWELSH - Duplicate Clause 16 ✅ FIXED

**Status:** RESOLVED (already fixed in previous session)

**Issue:** AMWELSH Rules 1 and 2 both contained identical "Rider Clause No: 16" text.

**Resolution:** Removed duplicate from Rule 1, kept complete version in Rule 2.

---

### 2. RTM Charter - Duplicate Lighterage Rules ⚠️

**Location:** RTM Rules 1 & 2 (lines 656 & 668)

**Issue:** RTM has TWO rules that are nearly identical:

**RTM Rule 1 (line 656):**
```
Charterer has the option of discharging into lighters and/or otherwise lightening the Vessel if it so
requires; the time and expenses thereof shall subject to Clause 5, be for Charterer's account and time
so used to count as laytime.
Otherwise all other terms, conditions and exceptions of this Contract shall apply to lighterage and
lightening.
```

**RTM Rule 2 (line 668):**
```
Charterer has the option of discharging into lighters and/or otherwise lightening the Vessel if
it so requires. Subject always to clause 5 , the expenses of lighterage and lightening shall be
for Charterer's account and time so used to count as laytime. Otherwise all other terms,
conditions and exceptions of this Contract shall apply to lighterage and lightening.
```

**Differences:**
- Rule 1: "shall subject to Clause 5"
- Rule 2: "Subject always to clause 5" (sentence structure different)
- Otherwise nearly identical

**Recommendation:** These appear to be the same clause with minor wording variations. Should consolidate into one rule.

---

### 3. Cross-Charter Duplicate: Lighterage Clause ⚠️

**Charters Affected:**
- **M_RESOURCES - Rule 2** (line 523)
- **RTM - Rule 1** (line 656)  
- **YANCOAL - Rule 1** (line 860)

**Issue:** IDENTICAL text appears in 3 different charters:

```
Charterer has the option of discharging into lighters and/or otherwise lightening the Vessel if it so requires;
the time and expenses thereof shall subject to Clause 5, be for Charterer's account and time so used to count
as laytime.
Otherwise all other terms, conditions and exceptions of this Contract shall apply to lighterage and lightening.
```

**Analysis:**
- These are 3 different charter parties
- Same laytime logic: lighterage time DOES count as laytime
- This is **legitimate repetition** - different contracts can have identical clauses
- However, indicates potential for consolidation or reference to common patterns

**Recommendation:** Keep all three. These are separate legal agreements. However, note that this pattern could be handled by rules engine with a single "LIGHTERAGE_TIME_COUNTS" stoppage configuration.

---

### 4. NYPE Charter - BIMCO Disclaimer Boilerplate ⚠️

**Location:** NYPE Rules 2 & 3 (lines 576 & 592)

**Issue:** Both rules contain BIMCO copyright disclaimer text:

```
This document is a computer generated NYPE 2015 published by BIMCO and jointly authored by ASBA, 
BIMCO and the SMF. Any insertion or deletion to the form must be clearly visible. In the event of 
any modification being made to the pre­printed text of this document which is not clearly visible, 
the original BIMCO approved document shall apply. Chinsay assumes no responsibility for any loss, 
damages or expenses as a result of discrepancies between the original BIMCO approved document and 
this computer generated document.
```

**Analysis:**
- This is **administrative boilerplate**, not laytime calculation logic
- Should NOT be in laytime-only extraction
- Appears in 2 NYPE rules

**Recommendation:** REMOVE this text from both NYPE Rule 2 and Rule 3. It's not relevant to laytime calculation.

---

## RECOMMENDATIONS

### Immediate Actions Required:

1. **RTM Charter:**
   - [ ] Remove RTM Rule 2 (duplicate of Rule 1 with trivial wording differences)
   - [ ] Update RTM rule count from 2 to 1
   - [ ] Impact: -6 lines

2. **NYPE Charter:**
   - [ ] Remove BIMCO disclaimer from NYPE Rule 2
   - [ ] Remove BIMCO disclaimer from NYPE Rule 3
   - [ ] Impact: -16 lines (approximately)

3. **M_RESOURCES/RTM/YANCOAL:**
   - [ ] No action needed - legitimate repetition across different contracts
   - [ ] Consider noting in documentation that this pattern exists

### Expected Results:

- **Lines:** 893 → ~871 (-22 lines, -2.5%)
- **Rules:** 52 → 51 (-1 rule, -1.9%)
- **Charters:** 30 (unchanged)

---

## VALIDATION CRITERIA

After cleanup:
- ✅ No duplicate text within same charter
- ✅ No administrative/boilerplate content
- ✅ Only laytime calculation logic remains
- ✅ Cross-charter duplicates are legitimate (different contracts)

---

## FILES TO UPDATE

1. `MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md` - Main file cleanup
2. `DEDUPLICATION_VERIFICATION.md` - Updated verification report
3. Charter count files - Update RTM from 2 to 1 rule


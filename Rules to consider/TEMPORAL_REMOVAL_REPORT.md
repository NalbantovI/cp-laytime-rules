# TEMPORAL RULES REMOVAL REPORT

**Date:** 2025-11-25
**Action:** Removed all rules with "Temporal" rule type except SYNACOMEX Rule 16
**File:** CP_RULES_CONSOLIDATED.md

---

## SUMMARY

- **Rules Before:** 12
- **Rules Removed:** 7
- **Rules Remaining:** 5
- **Exception Kept:** SYNACOMEX - Rule 16: Extract 12 (has Temporal type but was explicitly kept)

---

## RULES REMOVED (7 TEMPORAL RULES)

### 1. CSN - Rule 8: Extract 6
- **Rule Types:** Temporal, Conditional, Exception
- **Category:** CONDITIONAL
- **Summary:** Vessel arrival definitions and laytime calculation including Turn Time periods
- **Clause Reference:** Clauses 29.4 and 30.1-30.2

### 2. NYPE - Rule 3: Extract 1
- **Rule Types:** Temporal, Operational, Conditional
- **Category:** CONDITIONAL
- **Summary:** Discharge rates, laytime commencement, and NOR conditions
- **Clause Reference:** Sections A1-A3, B.B1

### 3. SAFANCHART - Rule 3: Extract 1
- **Rule Types:** Temporal, Operational, Conditional
- **Category:** CONDITIONAL
- **Summary:** Stoppage provisions and charter cancellation after 6 running days
- **Clause Reference:** Clause 3 stoppage provisions

### 4. SYNACOMEX - Rule 10: Extract 6
- **Rule Types:** Conditional, Temporal, Modifier
- **Category:** CONDITIONAL
- **Summary:** Charter party conflict resolution between Part I and Part II
- **Clause Reference:** Conflict of conditions clause

### 5. SYNACOMEX - Rule 15: Extract 11
- **Rule Types:** Conditional, Temporal
- **Category:** CONDITIONAL
- **Summary:** Despatch payment provisions and deductibility
- **Clause Reference:** Box 20 despatch provisions

### 6. YARA CP - Rule 7: Extract 5
- **Rule Types:** Temporal, Modifier, Conditional
- **Category:** CONDITIONAL
- **Summary:** Demurrage claim timing (25-day deadline) and despatch payment timing
- **Clause Reference:** Demurrage claim deadline clause

### 7. YANCOAL - Rule 5: Extract 3
- **Rule Types:** Operational, Weather Interruption, Temporal
- **Category:** OPERATIONAL
- **Summary:** Despatch money calculation and hatch covering procedures
- **Clause Reference:** Clauses 18.1-18.2

---

## RULES RETAINED (5 RULES)

### Exception Rules (2)

#### 1. ALCOA - Rule 6: Extract 4
- **Rule Types:** Operational, Exception
- **Summary:** Vessel certification requirements and work stoppage consequences
- **Reason Kept:** No Temporal type

#### 2. FPG - Rule 4: Extract 2
- **Rule Types:** Operational, Exception
- **Summary:** Winches, power, hatches and overtime provisions
- **Reason Kept:** No Temporal type

### Operational Rules (3)

#### 3. FMG - Rule 7: Extract 5
- **Rule Types:** Operational
- **Summary:** Hold accessibility requirements for grab discharge
- **Reason Kept:** No Temporal type

#### 4. SYNACOMEX - Rule 16: Extract 12
- **Rule Types:** Operational, Temporal
- **Summary:** Hold cleaning and disinfection procedures
- **Reason Kept:** **EXPLICITLY REQUESTED TO KEEP** despite having Temporal type

#### 5. TA1 - Rule 5: Extract 3
- **Rule Types:** Operational
- **Summary:** Grab discharge requirements and vessel suitability
- **Reason Kept:** No Temporal type

---

## RATIONALE FOR REMOVAL

**Temporal Rules** typically define:
- Time-based deadlines and periods (e.g., "25 days after completion")
- Sequence of events and trigger conditions
- Time calculations and Turn Time periods
- Deadlines for claims and payments

These rules were removed to focus on **computational laytime rules** that directly affect:
- Laytime counting mechanisms
- Exception handling during operations
- Operational requirements and constraints

**Exception:** SYNACOMEX Rule 16 was retained despite having "Temporal" type because it was explicitly requested to be kept by the user.

---

## FILE CHANGES

**Before:**
- Total Rules: 12
- Categories: Conditional (6), Exception (2), Operational (4)

**After:**
- Total Rules: 5
- Categories: Exception (2), Operational (3)
- Conditional category completely removed

**Impact:**
- Removed entire CONDITIONAL section from file
- Reduced file from ~285 lines to ~130 lines
- Focused remaining rules on operational constraints and exceptions

---

## NEXT STEPS

The remaining 5 rules should be analyzed for:
1. **Text completion** - Some rules may still have truncated text
2. **GRULE implementation** - Convert to computational rules
3. **Testing** - Verify rules work correctly in the engine

**Remaining Rules Focus:**
- **Exception handling** (2 rules): Vessel certification and equipment failures
- **Operational requirements** (3 rules): Hold accessibility, cleaning procedures, grab discharge requirements

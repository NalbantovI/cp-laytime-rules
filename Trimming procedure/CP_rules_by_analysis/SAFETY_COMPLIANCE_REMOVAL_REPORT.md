# SAFETY/COMPLIANCE RULES REMOVAL REPORT

**Date:** 2025-11-25
**Action:** Removed safety/compliance prerequisite rules with no corresponding SOF events
**File:** CP_RULES_CONSOLIDATED.md

---

## SUMMARY

- **Rules Before:** 5
- **Rules Removed:** 2
- **Rules Remaining:** 3
- **Reason:** Safety compliance prerequisites and vessel specification formalities, not computational laytime rules

---

## RULES REMOVED (2 SAFETY/COMPLIANCE & VESSEL SPECIFICATION RULES)

### 1. ALCOA - Rule 6: Extract 4

**Rule Types:** Operational, Exception

**Category:** EXCEPTION

**Rule Text:**
```
which the Vessel(s) will be employed, and Owners are to ensure that Vessel(s) are at all times in
possession of valid and up to date certificates of efficiency and safety to comply with such regulations.
20.5 If Stevedores, Longshoremen or other workmen are not permitted to work due to the failure of Master
and/or Owners Agents to comply with the aforementioned regulations, or because Vessel is not in
possession of such valid and up to date certificates of efficiency and safety, then time so lost shall not
count as laytime, even if Vessel is on demurrage and any Stevedore standby time to be for Owners
account.
```

**Summary:** Vessel safety certificate requirements preventing stevedore/workmen from working

**Clause Reference:** Clause 20.4-20.5 - Vessel certificates and regulatory compliance

---

### 2. TA1 - Rule 5: Extract 3

**Rule Types:** Operational

**Category:** OPERATIONAL

**Rule Text:**
```
429
GRAB 18. Vessel is guaranteed to have steel floors, tank tops and ceilings and to be suitable in all respects for 430
DISCHARGE grab discharge. No cargo shall be loaded in deep tanks, in bridge space, nor in any other place not 431
accessible for discharge by means of mechanical grabs. Nevertheless, should any cargo be loaded by the 432
Vessel in places not accessible to grabs, any time lost removing cargo from such places shall not count as 433
laytime or time on demurrage, and all expenses...
```

**Summary:** Vessel specification warranty for grab discharge suitability

**Clause Reference:** Clause 18 - Grab Discharge vessel requirements

---

## RATIONALE FOR REMOVAL

### Why This Rule Was Removed:

1. **No Corresponding SOF Event**
   - SOF Merge.csv contains no events like "Workers not permitted to work", "Certificate deficiency", or "Safety compliance failure"
   - This is a **condition/consequence**, not a discrete operational event
   - Statement of Facts records events like "Waiting for certificate" or "Hold inspection failed", not abstract compliance failures

2. **Prerequisite/Warranty, Not Operational Rule**
   - This is a **vessel readiness warranty** - the vessel must have valid safety certificates
   - Similar to warranties about vessel being seaworthy, cargo-worthy, or having working equipment
   - Not a laytime calculation rule, but a contractual obligation

3. **Already Covered by Existing Stoppages**
   - If this situation occurs, it would be recorded as:
     - `WAITING_FOR_CERTIFICATE` (already exists in GRULE)
     - `WAITING_FOR_VESSEL_READINESS` (already exists in GRULE)
     - `HOLD_INSPECTION_FAILED` (already exists in GRULE)
     - `SAFETY_INSPECTION` (already exists in GRULE)
   - The **consequence** (time doesn't count) is handled by the stoppage modifier (0.0 for Owner's fault)

4. **Legal/Compliance Nature**
   - This is about **regulatory compliance** and **Owner warranties**
   - Similar to the 22 Legal/Procedural rules already removed
   - Defines **what should be true** (vessel has certificates) rather than **what laytime calculation to perform**

5. **Not Implementable in GRULE**
   - GRULE rules respond to **SOF events** (e.g., "Safety inspection commenced")
   - This rule describes a **failure state** that would need manual determination
   - Cannot be automated without subjective judgment about "compliance failure"

### Why TA1 Rule 5 Was Removed:

**TA1 Rule 5** is a **vessel specification warranty/formality**, similar to ALCOA Rule 6:

1. **Warranty Language:** "Vessel is guaranteed to have steel floors... and to be suitable in all respects for grab discharge"
   - This is a **vessel suitability requirement**, not an operational event
   - Similar to saying "Vessel shall be seaworthy" - it's a prerequisite, not a calculation

2. **Formality, Not Operational Rule:**
   - Defines **what the vessel must be** (suitable for grabs)
   - Not **what happens during operations** (a stoppage, event, or time calculation)
   - This is a **contractual formality** about vessel specifications

3. **Already Covered:**
   - If cargo is loaded in inaccessible places, it would be recorded as operational delays
   - The time impact would be captured through existing stoppages
   - Similar to FMG Rule 7 but FMG is about **physical constraints**, while TA1 is about **warranties**

4. **No Discrete SOF Event:**
   - No event like "Cargo loaded in inaccessible location detected"
   - The consequence (time doesn't count) would be determined post-facto during laytime calculation disputes
   - Not something that appears in a Statement of Facts as an event

---

## COMPARISON: ALCOA Rule vs. Existing GRULE Rules

| Aspect | ALCOA Rule 6 | Existing GRULE Rules |
|--------|--------------|---------------------|
| **Trigger** | Vessel lacks safety certificates OR workers prevented from working | Discrete SOF events (commenced/completed) |
| **Detection** | Manual/subjective determination | Event-based from Statement of Facts |
| **Nature** | Contractual warranty/prerequisite | Operational stoppage |
| **SOF Event** | None exists in nomenclature | `WAITING_FOR_CERTIFICATE`, `SAFETY_INSPECTION` |
| **Implementation** | Cannot be automated | Already implemented |
| **Purpose** | Define Owner obligations | Calculate laytime impact |

---

## EXISTING GRULE COVERAGE

The following existing stoppages already handle scenarios related to ALCOA Rule 6:

### 1. **WAITING_FOR_CERTIFICATE**
- **Event:** `WAITING_FOR_CERTIFICATE_COMMENCED` / `COMPLETED`
- **Default Modifier:** 0.0 (time does NOT count when not used)
- **Responsibility:** Owner's fault
- **Use Case:** Waiting for vessel to obtain required certificates

### 2. **WAITING_FOR_VESSEL_READINESS**
- **Event:** `WAITING_FOR_VESSEL_READINESS_COMMENCED` / `COMPLETED`
- **Default Modifier:** 0.0 (time does NOT count when not used)
- **Responsibility:** Owner's responsibility
- **Use Case:** Vessel not ready for operations due to internal issues

### 3. **HOLD_INSPECTION_FAILED**
- **Event:** `HOLD_INSPECTION_FAILED`
- **Default Modifier:** 0.0 (time does NOT count when not used)
- **Responsibility:** Owner's fault (vessel failed inspection)
- **Use Case:** Holds rejected, preventing cargo operations

### 4. **SAFETY_INSPECTION**
- **Event:** `SAFETY_INSPECTION_COMMENCED` / `COMPLETED`
- **Default Modifier:** 1.0 (routine operational requirement)
- **Use Case:** Normal safety inspection process

### 5. **SAFETY_MEETING**
- **Event:** `SAFETY_MEETING_COMMENCED` / `COMPLETED`
- **Default Modifier:** 1.0 (routine operational requirement)
- **Use Case:** Safety briefings and meetings

### 6. **GANGWAY_UNSAFE**
- **Event:** `GANGWAY_UNSAFE_START` / `END`
- **Default Modifier:** 1.0
- **Use Case:** Specific safety issue (ArcelorMittal charter)
- **Comment:** "Ship reasons (lighting, gangway safety per port regulations)"

---

## RULES RETAINED (3 RULES)

### Exception Rules (1)

#### FPG - Rule 4: Extract 2
- **Rule Types:** Operational, Exception
- **Summary:** Winches, power, hatches and overtime provisions
- **Reason Kept:** Operational equipment requirements with laytime impact

### Operational Rules (2)

#### FMG - Rule 7: Extract 5
- **Rule Types:** Operational
- **Summary:** Hold accessibility requirements for grab discharge
- **Reason Kept:** Physical cargo handling constraints

#### SYNACOMEX - Rule 16: Extract 12
- **Rule Types:** Operational, Temporal
- **Summary:** Hold cleaning and disinfection procedures
- **Reason Kept:** Required cargo preparation steps

---

## KEY INSIGHT: SOF Event Nomenclature Matters

**Critical Finding:** Rules must correspond to discrete SOF events that can be recorded in a Statement of Facts.

**Events that DO exist in SOF nomenclature:**
- `Holds inspection failed`
- `Waiting for certificate commenced/completed`
- `Safety inspection commenced/completed`
- `Vessel detained`
- `Waiting for vessel readiness`

**Events that DO NOT exist:**
- "Workers not permitted to work due to certificates"
- "Vessel safety compliance failure"
- "Stevedore work prevented"
- "Certificate deficiency detected"

**Implication:** ALCOA Rule 6 describes a **legal consequence of a condition**, not an **operational event** that would be recorded in a Statement of Facts.

---

## FILE CHANGES

**Before:**
- Total Rules: 5
- Categories: Exception (2), Operational (3)

**After:**
- Total Rules: 3
- Categories: Exception (1), Operational (2)

**Impact:**
- Removed 1 safety/compliance prerequisite rule (ALCOA)
- Removed 1 vessel specification formality rule (TA1)
- All remaining rules have operational laytime impact
- All remaining rules can be triggered by SOF events

---

## HISTORICAL CONTEXT

This is the **third cleanup phase** for CP_RULES_CONSOLIDATED.md:

1. **Phase 1:** Removed rules already covered by GRULE (1,282 rules → 34 rules)
2. **Phase 2:** Removed Legal/Procedural rules (34 rules → 12 rules)
3. **Phase 3:** Removed Temporal rules except SYNACOMEX Rule 16 (12 rules → 5 rules)
4. **Phase 4 (This):** Removed Safety/Compliance prerequisites and Vessel Specifications (5 rules → 3 rules)

**Remaining:** 3 operational rules requiring GRULE implementation

---

## NEXT STEPS

The remaining 3 rules should be analyzed for:

1. **SOF Event Mapping** - Identify which SOF events trigger each rule
2. **Stoppage Configuration** - Determine modifier values (time counts or not)
3. **GRULE Implementation** - Convert to computational rules
4. **Testing** - Verify rules work correctly with actual SOF data

**Remaining Rules Focus:**
- **Exception handling** (1 rule): Equipment failures and alternative procedures
- **Operational requirements** (2 rules): Hold accessibility, cleaning procedures

All remaining rules describe **operational constraints** that can be detected from **SOF events** and have **direct laytime calculation impact**.

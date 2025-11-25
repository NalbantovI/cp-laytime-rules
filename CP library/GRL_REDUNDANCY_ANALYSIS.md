# .GRL REDUNDANCY ANALYSIS REPORT

**Date:** November 24, 2025  
**Analysis:** Cross-reference between MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md and rule/*.grl files  
**Status:** ⚠️  PENDING USER CONFIRMATION

---

## �� Objective

Identify and remove rules from MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md that are already covered by stoppage rules in the `.grl` files, particularly `stoppages.grl`.

---

## 📊 Summary Statistics

| Metric | Count |
|--------|-------|
| **Total rules in MASTER file** | 54 |
| **Redundant with .grl files** | 9 |
| **Unique rules to keep** | 45 |
| **Reduction percentage** | 16.7% |

---

## 🔍 .GRL Files Coverage

The `rule/common_rules/stoppages.grl` file contains **194 stoppage types** that handle:
- Vessel movements (shifting, maneuvering, warping)
- Hold operations (opening, closing, inspection)
- Equipment breakdowns (ship cranes, shore equipment)
- Inspections and surveys (draft surveys, hold inspections)
- Gangway and access safety
- Weather conditions
- Labor and personnel issues
- And many more...

---

## ❌ PROPOSED RULES FOR REMOVAL

### 1. ALCOA - Rule 1: Crane Breakdown
**Content:**
```
20.3 Any time lost due to the breakdown of Vessel(s) crane(s) or failure to supply 
sufficient power will not count as laytime pro-rata according to the number of 
workable cranes available.
```

**Redundant with:**
- `SHIP_CRANE_BREAKDOWN` stoppage in stoppages.grl
- `EQUIPMENT_BREAKDOWN` stoppage in stoppages.grl

**Reason:** Equipment breakdowns are already tracked by the rules engine.

---

### 2. AMWELSH - Rule 1: Gangway Safety (ISPS)
**Content:**
```
During the currency of this charter party, the owners shall comply with the 
requirements of the ISPS Code... A gangway shall be placed and accessibility 
to be safe and secure at all time. In default of above, all loading/discharging 
operations will be stopped and all costs involved/time lost will be for vessel's 
account.
```

**Redundant with:**
- `GANGWAY_UNSAFE` stoppage in stoppages.grl
- `WAITING_FOR_GANGWAY` stoppage in stoppages.grl

**Reason:** Gangway safety stoppages are already handled.

---

### 3. AMWELSH - Rule 2: Gangway Safety (Surveyor Access)
**Content:**
```
Rider Clause No: 16 - Discharging Port Surveyor and requirements
...A gangway shall be placed and accessibility to be safe and secure at all time
In default of above, all loading/discharging operations will be stopped and all 
costs involved/time lost will be for vessel's account.
```

**Redundant with:**
- `GANGWAY_UNSAFE` stoppage in stoppages.grl
- `WAITING_FOR_GANGWAY` stoppage in stoppages.grl

**Reason:** Duplicate of AMWELSH Rule 1, same gangway coverage.

---

### 4. ATLAS - Rule 1: Shifting/Warping
**Content:**
```
The Vessel shall move along any one berth or installation... Time used for warping 
shall not count as laytime or time on demurrage and warping to be done by Vessel's 
crew, where local regulations permit.
Should the load/discharge port order the vessel to shift to another berth prior to 
or during loading or discharging, then such time used for shifting shall not count 
as laytime even if vessel is on demurrage...
```

**Redundant with:**
- `SHIFTING` stoppage in stoppages.grl
- `WARPING` stoppage in stoppages.grl
- `MANOEUVRING` stoppage in stoppages.grl

**Reason:** All vessel repositioning operations are covered.

---

### 5. ENEL - Rule 1: Opening/Closing Hatches
**Content:**
```
12. OPENING & CLOSING HATCHES
12.1 Time used for opening and closing of hatches at loading and discharging ports 
shall be for Owners' account and time so used is not to count as laytime or as time 
on demurrage, if the Vessel is already on demurrage, unless such an operation is 
effected by crew prior to the port working hours.
```

**Redundant with:**
- `OPENING_HOLDS` stoppage in stoppages.grl
- `CLOSING_HOLDS` stoppage in stoppages.grl

**Reason:** Hatch operations are already tracked.

---

### 6. FERTIVOY - Rule 1: Vessel Not Ready After Berthing
**Content:**
```
If after berthing the Vessel is found not to be ready in all respects to load/
discharge and/or fails to pass inspection as per Clause 12, lines 207...
```

**Redundant with:**
- `HOLD_INSPECTION_REJECTION` stoppage in stoppages.grl
- `WAITING_FOR_VESSEL_READINESS` stoppage in stoppages.grl

**Reason:** Vessel readiness failures are handled by inspection rejection rules.

---

### 7. NORGRAIN - Rule 1: Asian Gypsy Moth Inspection Failure
**Content:**
```
Owners guarantee the vessel is free of any Asian Gypsy Moth eggs or larvae or any 
form of Gypsy Moth life. Should vessel to be found to have the same after tendering 
NOR, the NOR to be considered invalid. NOR to be re-tendered after vessel is cleared 
by authorities. Time not to count from the moment of the discovery of Gypsy Moth 
until vessel re-tenders NOR and vessel is cleared by govern authorities.
```

**Redundant with:**
- `HOLD_INSPECTION_REJECTION` stoppage in stoppages.grl
- `INSPECTION_IN_PROGRESS` stoppage in stoppages.grl
- `WAITING_FOR_VESSEL_READINESS` stoppage in stoppages.grl

**Reason:** Inspection failures (including pest inspections) are covered.

---

### 8. YARA CP - Rule 1: Gear Breakdown
**Content:**
```
The vessel shall give free use of all gear, grabs and lights. When required by 
Charterers, Shippers or Receivers and permitted by Port Authorities, the vessel's 
crew to operate the cranes free of charge to Charterers.
Any time lost due to breakdown of vessel's gear (including gantry crane) shall not 
count as lay time or time on demurrage, and Owners shall be liable for any costs 
and expenses incurred by the Charterers as a consequence of such breakdown.
```

**Redundant with:**
- `SHIP_CRANE_BREAKDOWN` stoppage in stoppages.grl
- `EQUIPMENT_BREAKDOWN` stoppage in stoppages.grl

**Reason:** Equipment breakdown stoppages are already implemented.

---

### 9. YARA CP - Rule 2: Vessel Not Ready/Fails Inspection
**Content:**
```
If vessel is found not to be ready in all respects to load/discharge and/or fails 
to pass inspection, any time lost from the discovery thereof until the Vessel is 
ready in all respects to load/discharge shall not count as lay time or time on 
demurrage.
```

**Redundant with:**
- `HOLD_INSPECTION_REJECTION` stoppage in stoppages.grl
- Rule triggered by `HOLD_INSPECTION_FAILED` event
- Cleared by `HOLD_INSPECTION_PASSED` event

**Reason:** **EXACT MATCH** - This is precisely what stoppages.grl handles with:
```grule
rule OnHoldInspectionFailed "Hold inspection rejection stops laytime" salience 10 {
    when
        Event.Type() == "SOFEvent" && Event.Name == "HOLD_INSPECTION_FAILED"
    then
        LaytimeClock.ScheduleStoppageStart(Event.PointInTime(), "HOLD_INSPECTION_REJECTION");
}
```

---

## 📋 Removal Impact Analysis

### By Category:
- **Equipment Breakdowns:** 2 rules (ALCOA-1, YARA CP-1)
- **Gangway Safety:** 2 rules (AMWELSH-1, AMWELSH-2)
- **Shifting/Warping:** 1 rule (ATLAS-1)
- **Hatch Operations:** 1 rule (ENEL-1)
- **Inspection Failures:** 3 rules (FERTIVOY-1, NORGRAIN-1, YARA CP-2)

### By Charter:
- **AMWELSH:** 2 rules removed
- **YARA CP:** 2 rules removed
- **ALCOA, ATLAS, ENEL, FERTIVOY, NORGRAIN:** 1 rule each

---

## ✅ What Will Remain

After removing these 9 redundant rules, the MASTER file will contain:
- **45 unique laytime calculation rules**
- Rules covering:
  - Accessible cargo space issues
  - Vessel construction suitability
  - Cargo-specific handling requirements
  - Dead freight laytime adjustments
  - Boycott time suspensions
  - Third-party arrest time suspension
  - Pollution compliance failures
  - Port restriction delays
  - Strike/force majeure (with specific nuances)
  - Lighterage time counting
  - Other charter-specific calculation logic

---

## 🎯 Recommendation

**REMOVE all 9 rules listed above** because:

1. ✅ **Already Implemented:** All functionality exists in `.grl` files
2. ✅ **Maintainability:** Single source of truth in `.grl` rules
3. ✅ **Consistency:** Events trigger stoppage rules automatically
4. ✅ **No Loss:** No unique laytime calculation logic will be lost

**The MASTER file should only contain:**
- Charter-specific laytime calculation nuances not covered by generic stoppages
- Unique time attribution rules
- Special calculation formulas
- Charter-specific time consequences

**The .GRL files handle:**
- All standard operational stoppages
- Common vessel state changes
- Standard equipment failures
- Standard inspection procedures

---

## ⚠️  USER CONFIRMATION REQUIRED

Before proceeding with removal, please confirm:

1. ✅ Do you want to remove all 9 rules?
2. ✅ Should I create backups before removal?
3. ✅ Do you want a detailed diff showing what will be removed?
4. ✅ Are there any specific rules you want to keep despite redundancy?

---

**Next Steps:**
1. User reviews this analysis
2. User confirms removal
3. Create backup (Phase 6)
4. Remove redundant rules
5. Update statistics
6. Create final report

---

**End of Analysis Report**

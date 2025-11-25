# Comparison: YARA Excel Analysis vs. LAYTIME_RULE_CATEGORIES.md

## Date: 2025
## Purpose: Analyze existing methodology and refine categorization framework

---

## EXECUTIVE SUMMARY

The YARA Excel analysis reveals a **more granular, implementation-focused** approach compared to the initial `LAYTIME_RULE_CATEGORIES.md` framework. Key differences:

1. **Clause Decomposition**: YARA breaks single clauses into 8-10 separate rules
2. **Implementation Focus**: Each rule includes pseudo-code, SOF events, and timeline context
3. **Hierarchy**: Uses numbered categories (1.x, 2.x, 3.x, 4.x) similar to our framework
4. **Computational Ready**: Designed for software implementation, not just classification

---

## COMPARISON TABLE

### Clause C Example: Notice of Readiness & Laytime Commencement

| YARA Approach | Our Framework | Analysis |
|--------------|---------------|----------|
| **9 separate rules** from one clause | Would classify as 1-2 rules | ❌ Too coarse |
| Numbered categories: 1, 2, 3, 4 | 12 numbered categories | ✅ Similar structure |
| Includes pseudo-code functions | No implementation details | ❌ Missing computational aspect |
| Links to SOF events | No event mapping | ❌ Missing operational context |
| "Timeline Flow" column | No timeline context | ❌ Missing temporal sequencing |

---

## DETAILED ANALYSIS: YARA METHODOLOGY

### Sheet 1: YARA CP - Full Analysis (27 rules)

**Columns:**
1. **Governing Clause** - Full clause text from charter party
2. **Category** - Primary category number
3. **Rule Header** - Descriptive name
4. **Governing Rule from Documents** - Exact quote
5. **Rule Type** - Nature (Legal, Cargo Terms, Early Loading, etc.)
6. **Operation Type** - Loading/Discharging/Both
7. **Category.1** - Secondary categorization
8. **Timeline Flow** - Temporal context
9. **Function** - Pseudo-code implementation
10. **Comments** - Implementation notes
11. **Associated Events** - SOF event triggers
12-15. **Additional columns** - Various metadata

**Categories Used:**
- **1. NOR CP Rules** - Notice of Readiness procedures
- **2. Laytime Start** - When laytime commences
- **3. Interruption** - Events that stop/pause laytime
- **4. Allowed Laytime** - Time that counts as laytime
- **5. Exceptions** - Weather, holidays, etc.
- **6. Shifting** - Vessel movements between berths

### Sheet 2: YARA CP - Decomposed (34 rows)

Shows **granular breakdown** of how complex clauses are split:

**Example: Clause C (NOR & Laytime Start)**

1. **NOR Recipients (Loading)** - "Notice... shall be given to Shippers, Charterers..."
2. **NOR Recipients (Discharging)** - "Notice... shall be given to Receivers, Charterers..."
3. **NOR Tender Prerequisites** - "Notice... not be given before vessel has berthed..."
4. **NOR Timing** - "Notice... during office hours only"
5. **Laytime Commencement Times** (Row 1) - "...14.00 hours if NOR given up to 12.00 hours..."
6. **Laytime Commencement Times** (Row 2) - "...08.00 hours next working day if NOR given after 12.00..."
7. **Laytime Commencement Times** (Row 3) - "...after office hours, next working day 14:00..."
8. **Early Work Commencement** (Part 1) - "unless work commenced earlier"
9. **Early Work Commencement** (Part 2) - "time actually used shall count half"
10. **Laycan Start Restriction** (Part 1) - "lay time shall in no event commence prior to 14.00 hours on first day of laycan"
11. **Laycan Start Restriction** (Part 2) - "unless work commenced earlier"
12. **Laycan Start Restriction** (Part 3) - "time actually used shall count half"
13. **NOR per Port** - "Notice of Readiness is to be given at each port"

**Insight:** One clause → 13 distinct rules!

### Sheet 3: Related SOF events (24 event types)

**Event Categories:**
- NOR events (4 types)
- Operations events (10 types)
- Inspection events (4 types)
- Weather events (30+ types)
- Port events (5 types)
- Shifting events (8 types)
- Ballast/bunkering events (6 types)
- Strike events (3 types)

---

## KEY INSIGHTS FOR FRAMEWORK REFINEMENT

### 1. **Granularity Level**

**YARA Approach:**
- Breaks every sentence/paragraph into separate rule
- Each rule has specific implementation logic
- Average: 8-10 rules per clause

**Our Framework:**
- Groups related concepts together
- Focuses on categorization, not implementation
- Average: 1-2 categories per clause

**Recommendation:** 
✅ Maintain our categorization level (easier to understand)
✅ Add sub-numbering for implementation details when needed
✅ Create separate "implementation guide" for computational logic

### 2. **New Categories Discovered in YARA**

Categories **present in YARA** but **missing or unclear** in our framework:

| YARA Category | Our Equivalent | Status |
|--------------|----------------|--------|
| NOR CP Rules | 1.x Notice of Readiness | ✅ Covered |
| Laytime Start | 2.x Laytime Commencement | ✅ Covered |
| Interruption | 3.x Suspension/Exclusion | ✅ Covered |
| Allowed Laytime | No direct equivalent | ⚠️ **NEW CATEGORY NEEDED** |
| Early Start modifiers (HT/AT) | 9.x Special Time Counting | ⚠️ Needs refinement |
| Timeline Flow | No equivalent | ⚠️ **NEW METADATA NEEDED** |
| Associated SOF Events | No equivalent | ⚠️ **NEW MAPPING NEEDED** |

### 3. **Implementation-Ready Features**

**YARA includes:**
- **Pseudo-code functions**: 
  ```
  def LaytimeStart(WorkingSchedule, NORAcceptedPerCP, Noon):
      if NORAcceptedPerCP <= Noon:
          return AfternoonStart
      else:
          return NextWorkingDay
  ```

- **Conditional logic**:
  ```
  ifs(NOR tendered time <= MiddayPoint, set laytime_start = 14:00)
  ```

- **Timeline sequencing**:
  - "Laytime timeline"
  - "Interruption timeline"
  - "NOR tendering CP rules"

- **Event mapping**:
  - Each rule links to specific SOF events
  - Example: "Inspection failed, Inspection passed, Holds accepted, Holds rejected"

**Our Framework lacks:**
- ❌ Computational logic
- ❌ Timeline context
- ❌ Event triggers
- ❌ Pseudo-code examples

### 4. **Rule Type Classification**

**YARA uses:**
- Legal (procedural requirements)
- Cargo Terms (operational conditions)
- Early Loading (timing modifiers)
- NOR Tendering (notice procedures)
- NOR Failed Inspection (contingency scenarios)
- Waiting Berth time (delay handling)
- Humidity Interruption (weather-specific)
- Port Cargo Hours (working time definitions)

**Our Framework uses:**
- Descriptive category names
- No "rule type" metadata

**Recommendation:**
✅ Add "Rule Type" as metadata field
✅ Use YARA's types as starting point
✅ Extend with additional types as needed

---

## PROPOSED FRAMEWORK ENHANCEMENTS

### Enhancement 1: Add "Rule Type" Metadata

For each rule in our framework, add:
- **Legal/Procedural**: Contractual requirements
- **Operational**: Physical operations
- **Temporal**: Time-based conditions
- **Conditional**: If-then logic
- **Modifier**: Adjustments to base rules
- **Exception**: Special circumstances

### Enhancement 2: Add "Timeline Context"

Categories:
- **Pre-NOR**: Before notice given
- **NOR Stage**: Notice tendering and acceptance
- **Pre-Laytime**: After NOR, before laytime starts
- **Laytime Active**: While laytime is counting
- **Interruption**: Laytime paused
- **Demurrage**: After laytime expired
- **Post-Operations**: After loading/discharging complete

### Enhancement 3: Create New Category

**4. ALLOWED LAYTIME / TIME CREDITING**

Rules about what time **counts towards laytime** even when vessel isn't operating:

**4.1 Waiting for Berth**
- Time lost waiting for berth to count as laytime
- Keywords: "waiting for berth", "time to count", "berth availability"

**4.2 Port Delays (Charterers' Account)**
- Delays caused by charterers count as laytime
- Keywords: "charterers' account", "time to count", "delays attributable"

**4.3 Early Completion Credits**
- Time saved by early completion
- Keywords: "time saved", "despatch", "early completion bonus"

### Enhancement 4: Add "Associated SOF Events" Column

For each rule, list SOF (Statement of Facts) events that trigger it:

Example from YARA:
- **Rule**: "Time Lost to Failed Inspection"
- **SOF Events**: "Inspection failed, Inspection passed, Holds accepted, Holds rejected"

This helps with:
- Implementation in software
- Understanding operational triggers
- Mapping charter party to vessel operations

### Enhancement 5: Add "Implementation Notes" Section

For each rule, include:
- Pseudo-code (optional)
- Calculation method
- Edge cases
- Dependencies on other rules
- Example scenarios

---

## YARA-SPECIFIC PATTERNS OBSERVED

### Pattern 1: Multi-Step NOR/Laytime Rules

YARA breaks NOR acceptance into steps:

1. **NOR Tendered** → validates against office hours → **NOR Tendered per CP**
2. **NOR Tendered per CP** → checks prerequisites → **NOR Accepted per CP**
3. **NOR Accepted per CP** → applies timing rules → **Laytime Start**
4. **Laytime Start** → checks for early work → **Actual Laytime Start**

**Our Framework**: Treats this as single "Laytime Commencement" category

**Recommendation**: 
- Keep high-level category
- Add sub-categories (2.1, 2.2, 2.3, 2.4) for detailed steps

### Pattern 2: Interruption With Resume Logic

YARA handles interruptions with **three-part logic**:

1. **Start of Interruption**: Event that pauses laytime
2. **During Interruption**: What happens while paused
3. **End of Interruption**: Conditions to resume

Example: Failed Inspection
- **Start**: Inspection failed event
- **During**: Repairs, cleaning, re-inspection
- **End**: MIN(Operations commenced, Inspection passed + 6 hours)

**Our Framework**: Only captures "interruption event"

**Recommendation**:
- Add sub-structure: Start / Duration / End
- Specify resume conditions explicitly

### Pattern 3: Conditional Time Counting (Multipliers)

YARA uses **laytime multipliers**:

- `laytime_multiplier = 1.0` → Time counts normally
- `laytime_multiplier = 0.5` → Half-time (early start, ATUC)
- `laytime_multiplier = 0.0` → Time doesn't count (interruption)
- `laytime_multiplier = 2.0` → Double-time (rare, penalty scenarios)

**Our Framework**: Describes conditions but no mathematical model

**Recommendation**:
- Add "Time Counting Rate" field
- Specify multiplier for each rule
- Document special cases (ATUC, SHEX, EIU)

### Pattern 4: Flags and State Variables

YARA uses boolean flags:

- `UU` (Unless Used) - indicates early work possibility
- `ATUC` (Actual Time Used to Count) - tracks early start counting
- `SHEX`, `FHEX`, `SHINC` - working time regime flags

**Our Framework**: No state tracking

**Recommendation**:
- Document state variables needed for implementation
- Create glossary of flags/variables
- Specify when flags are set/cleared

---

## REFINED CATEGORY STRUCTURE

Based on YARA analysis, here's the **enhanced framework**:

### **1. NOTICE OF READINESS (NOR)**

**1.1 NOR Prerequisites**
- Vessel conditions required before tendering
- Examples: Berthed, all fast, holds clean, ready in all respects

**1.2 NOR Tendering Procedures**
- Who to notify, when, how
- Office hours restrictions
- Document requirements

**1.3 NOR Timing & Validity**
- When NOR can be tendered
- Valid vs invalid NOR
- Acceptance conditions

**1.4 NOR at Multiple Ports**
- Per-port NOR requirements
- Separate NOR for loading/discharging

**1.5 Failed NOR / Re-tendering**
- Conditions for NOR rejection
- Re-tendering procedures

### **2. LAYTIME COMMENCEMENT**

**2.1 Standard Commencement Times**
- Office hours-based start times
- Noon cutoffs
- Next-day start rules

**2.2 Early Work Commencement**
- "Unless used" provisions
- "Time actually used to count"
- Half-time counting (ATUC)

**2.3 Laycan Restrictions**
- Earliest possible laytime start
- First day of laycan rules
- Canceling date implications

**2.4 Delayed Commencement**
- Waiting for berth
- Port congestion
- Causes beyond vessel's control

**2.5 Conditional Starts**
- Inspection-dependent start
- Documentation-dependent start
- Cargo readiness-dependent start

### **3. LAYTIME INTERRUPTIONS & SUSPENSIONS**

**3.1 Weather Interruptions**
- Weather working day definitions
- Specific weather events (rain, fog, high winds)
- Humidity stoppages

**3.2 Holiday & Non-Working Time**
- SHEX, SSHEX, FHEX variations
- EIU (Even If Used) vs UU (Unless Used)
- Holiday definitions

**3.3 Inspection Failures**
- Failed inspection consequences
- Time lost until ready
- Re-inspection procedures

**3.4 Equipment/Facility Failures**
- Shore equipment breakdown
- Terminal delays
- Berth unavailability

**3.5 Cargo/Documentation Issues**
- Missing documents
- Cargo not ready
- Quality issues

**3.6 Shifting & Vessel Movements**
- Time shifting between berths
- Anchorage to berth movements
- "Time not to count" provisions

**3.7 Third-Party Delays**
- Stevedore delays
- Receiver delays
- Customs/immigration delays

**3.8 Force Majeure**
- Strike, lockout, riot
- War, civil commotion
- Acts of God

### **4. ALLOWED LAYTIME (NEW CATEGORY)**

**4.1 Waiting for Berth Time**
- Time waiting counts as laytime
- Port congestion provisions

**4.2 Charterers' Delays**
- Delays attributable to charterers count
- Examples: cargo not ready, documents missing

**4.3 Early Completion Bonuses**
- Despatch calculations
- Time saved provisions

**4.4 Concurrent Operations**
- Multiple operations counting simultaneously
- Parallel loading/ballasting

### **5. SHIFTING & VESSEL MOVEMENTS**

**5.1 Shifting Between Berths**
- Time to count or not to count
- Charterers' vs Owners' orders

**5.2 Anchorage to Berth**
- Approach time
- Pilot delays

**5.3 Shifting for Vessel's Purposes**
- Bunkering shifts
- Repairs
- Crew changes

### **6. CARGO OPERATIONS PROCEDURES**

**6.1 Cargo Readiness**
- Cargo availability requirements
- Staging requirements

**6.2 Loading/Discharging Rates**
- Rate specifications
- Rate variations by cargo

**6.3 Operational Restrictions**
- Night work restrictions
- Weekend work restrictions
- Safety restrictions

**6.4 Ballast/De-ballast Requirements**
- Simultaneous operations
- Time counting rules

**6.5 Cargo Inspections**
- Quality inspections
- Quantity surveys
- Sampling procedures

### **7. VESSEL READINESS REQUIREMENTS**

**7.1 Physical Readiness**
- Holds clean and dry
- Hatches weathertight
- Equipment operational

**7.2 Documentation Readiness**
- Certificates valid
- Permits obtained
- Declarations completed

**7.3 Inspection Requirements**
- Pre-loading inspections
- Hold inspections
- ULD tests

**7.4 Acceptance Procedures**
- Surveyor acceptance
- Charterer approval
- Time to re-inspect

### **8. THIRD-PARTY DEPENDENCIES**

**8.1 Stevedore Issues**
- Stevedore availability
- Stevedore equipment
- Stevedore delays

**8.2 Port Authority Delays**
- Customs clearance
- Immigration
- Port health

**8.3 Terminal/Facility Delays**
- Terminal readiness
- Equipment availability
- Queue management

### **9. SPECIAL TIME COUNTING RULES**

**9.1 Working Day Definitions**
- 24-hour day
- Conventional day
- Weather working day

**9.2 Time Counting Modifiers**
- Half-time (ATUC)
- Double-time (penalties)
- No counting (interruptions)

**9.3 Reversibility**
- Reversible vs non-reversible
- Port-to-port calculations

**9.4 Turn Time Provisions**
- Turn lost penalties
- Turn regained provisions

### **10. LEGAL & ADMINISTRATIVE**

**10.1 Notice Requirements**
- Written notices
- Recipients
- Timing

**10.2 Cost Allocation**
- Charterers' account
- Owners' account
- Shared costs

**10.3 Liability & Exemptions**
- Owners' liability limits
- Charterers' responsibilities
- Force majeure exemptions

**10.4 Cancellation Rights**
- Canceling date provisions
- Failed inspection cancellation
- Force majeure cancellation

### **11. CALCULATION & FINANCIAL**

**11.1 Laytime Calculation**
- Allowed laytime formulas
- Calculation methods

**11.2 Demurrage**
- Demurrage rate
- Demurrage calculation
- Demurrage caps

**11.3 Despatch**
- Despatch rate
- Despatch calculation
- Despatch conditions

**11.4 Exception Clause Impacts**
- "Time that would have been lost"
- Concurrent exception handling

### **12. MULTI-PORT OPERATIONS**

**12.1 Per-Port Rules**
- NOR at each port
- Separate laytime calculations

**12.2 Reversibility Between Ports**
- Reversible provisions
- Non-reversible provisions

**12.3 Port Rotation**
- Rotation order
- Rotation flexibility

---

## IMPLEMENTATION RECOMMENDATIONS

### For Immediate Use (Classification):

1. **Use existing LAYTIME_RULE_CATEGORIES.md** for high-level categorization
2. **Add "Rule Type" tag** to each rule (Legal, Operational, Temporal, etc.)
3. **Add "Timeline Context"** to show when rule applies
4. **Create index** linking categories to charter party clauses

### For Software Implementation:

1. **Create separate document**: "LAYTIME_RULES_IMPLEMENTATION.md"
2. **Include pseudo-code** for each computational rule
3. **Map SOF events** to rule triggers
4. **Define state variables** and flags needed
5. **Specify time multipliers** for each scenario
6. **Document resume conditions** for interruptions

### For Future Enhancement:

1. **Build rule dependencies graph** (which rules depend on others)
2. **Create test scenarios** for each rule category
3. **Develop calculation examples** with worked examples
4. **Map to standard charter party forms** (GENCON, NYPE, etc.)
5. **Create visual timeline diagrams** showing rule application flow

---

## CONCLUSION

The YARA Excel analysis demonstrates a **highly sophisticated, implementation-ready** approach to laytime rules. Key takeaways:

### ✅ Strengths of YARA Approach:
- Extremely granular (every sentence is a rule)
- Implementation-ready with pseudo-code
- Maps to operational events (SOF)
- Includes timeline context
- Computational model with multipliers

### ✅ Strengths of Our Framework:
- Easier to understand and navigate
- Better for learning and classification
- Comprehensive coverage of rule types
- Good hierarchical structure
- Focused on categorization vs implementation

### ✅ Recommended Hybrid Approach:
1. **Keep our category structure** (12 major categories) for classification
2. **Add YARA's implementation features** as metadata:
   - Rule Type
   - Timeline Context
   - SOF Event Triggers
   - Time Counting Multipliers
   - Implementation Notes
3. **Create two-tier system**:
   - **Tier 1**: Human-readable categorization (our framework)
   - **Tier 2**: Machine-readable implementation (YARA style)
4. **Add "Allowed Laytime"** as new major category (Category 4)
5. **Enhance existing categories** with sub-numbering where needed

### Next Steps:

1. ✅ Update LAYTIME_RULE_CATEGORIES.md with new Category 4
2. ✅ Add metadata fields to existing categories
3. ✅ Create LAYTIME_RULES_IMPLEMENTATION.md for computational logic
4. ✅ Map SOF events to each rule category
5. ✅ Develop worked examples for complex scenarios

---

## APPENDIX: YARA Category Mapping

| YARA Category | Our Category | Mapping Quality |
|--------------|--------------|-----------------|
| 1. NOR CP Rules | 1.x Notice of Readiness | ✅ Direct match |
| 2. Laytime Start | 2.x Laytime Commencement | ✅ Direct match |
| 3. Interruption | 3.x Suspension/Exclusion Events | ✅ Direct match |
| 4. Allowed Laytime | ⚠️ NOT COVERED | ❌ **New category needed** |
| Early Loading | 9.x Special Time Counting | ⚠️ Partial match |
| NOR Failed Inspection | 1.5 + 3.3 | ✅ Covered across categories |
| Weather Stoppage | 3.1 | ✅ Direct match |
| Waiting for Berth | 4.1 (NEW) | ⚠️ New subcategory |

---

**Document Status**: DRAFT for review and refinement
**Next Action**: Update LAYTIME_RULE_CATEGORIES.md with findings

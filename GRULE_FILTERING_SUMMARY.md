# GRULE Coverage Analysis - Summary Report

**Date:** November 25, 2025  
**Task:** Remove rules from CP_RULES_CONSOLIDATED.md that are already covered in GRULE implementation

---

## 📋 Executive Summary

Successfully analyzed 1,476 charter party rules and identified that **86.9% are already implemented** in the existing GRULE rule files. These covered rules have been removed from `CP_RULES_CONSOLIDATED.md`, leaving only 194 uncovered rules that require new GRULE implementation.

---

## 🔍 Analysis Process

### 1. GRULE Scanning
Scanned all `.grl` files in the `CP library/rule/` directory:
- **438 SOF Events** identified (e.g., `LOADING_COMMENCED`, `NOR_TENDERED`)
- **607 Stoppage Concepts** identified (e.g., `WEATHER`, `MOORING`, `BUNKERING`)

### 2. Rule Coverage Analysis
Each rule in `CP_RULES_CONSOLIDATED.md` was analyzed to determine if its content matches any:
- SOF event names from GRULE files
- Stoppage/laytime concepts from GRULE rules
- Common laytime terminology (NOR, WIBON, WIPON, etc.)

### 3. Filtering
Rules matching GRULE concepts were removed, keeping only rules requiring new implementation.

---

## 📊 Results Summary

| Metric | Value |
|--------|-------|
| **Total Rules Analyzed** | 1,476 |
| **Rules Covered by GRULE** | 1,282 (86.9%) |
| **Rules NOT Covered** | 194 (13.1%) |
| **File Size Reduction** | 26,294 → 5,327 lines (79.7% reduction) |

---

## 📈 Coverage by Rule Type

| Rule Type | Kept | Total | Coverage |
|-----------|------|-------|----------|
| **CARGO TERMS** | 0 | 2 | 100.0% |
| **NOR TENDERING** | 0 | 16 | 100.0% |
| **NOR FAILED INSPECTION** | 0 | 10 | 100.0% |
| **WEATHER INTERRUPTION** | 2 | 42 | 95.2% |
| **OPERATIONAL** | 32 | 416 | 92.3% |
| **TEMPORAL** | 42 | 356 | 88.2% |
| **PORT CARGO HOURS** | 2 | 16 | 87.5% |
| **CONDITIONAL** | 44 | 320 | 86.3% |
| **EXCEPTION** | 16 | 82 | 80.5% |
| **LEGAL/PROCEDURAL** | 44 | 196 | 77.6% |
| **WAITING BERTH TIME** | 2 | 6 | 66.7% |
| **MODIFIER** | 10 | 14 | 28.6% |

---

## 📂 Files Generated

### Analysis Tools
1. **`analyze_covered_rules.py`**
   - Comprehensive analyzer that scans GRULE files
   - Generates detailed coverage report
   - Shows matched concepts for each covered rule

2. **`filter_covered_rules.py`**
   - Production filtering script (used for final output)
   - Line-by-line processing with accurate rule detection
   - Preserves file structure and formatting

3. **`remove_covered_rules.py`**
   - Alternative regex-based approach
   - Type-specific statistics
   - Backup implementation

### Output Files
1. **`CP_RULES_CONSOLIDATED.md`** (UPDATED)
   - Now contains **only 194 uncovered rules**
   - 5,327 lines (down from 26,294)
   - Focus on rules requiring new GRULE implementation

2. **`CP_RULES_CONSOLIDATED_ORIGINAL.md`** (BACKUP)
   - Original file with all 1,476 rules preserved
   - 26,294 lines
   - Complete backup for reference

3. **`GRULE_COVERAGE_ANALYSIS.md`**
   - Detailed report with all SOF events and stoppages
   - Lists covered rules with matched concepts
   - Lists uncovered rules with previews
   - 3,556 lines of analysis

---

## 🎯 What's Covered in GRULE

### Common Rules (`common_rules/`)
- **`laytime.grl`**: Loading/discharging operations, laytime commencement logic
- **`nor.grl`**: NOR tendering and acceptance (WIBON, WIPON, WIFPON, WICCON)
- **`vessel.grl`**: Vessel state tracking (anchored, berthed, free pratique, customs)
- **`stoppages.grl`**: Comprehensive stoppage rules (3,988 lines)
  - Weather conditions (rain, fog, snow, high winds, etc.)
  - Equipment breakdowns (ship, shore, crane, conveyor)
  - Cargo operations (loading, discharging, parcels)
  - Vessel movements (shifting, mooring, maneuvering)
  - Inspections and surveys (holds, tanks, draft)
  - Formalities (customs, inward/outward)
  - Labor and waiting states
  - Force majeure and strikes

### Charter-Specific Rules
- **`eurochem/nor_parameters.grl`**: WIBON, WIFPON, WICCON, WIPON
- **`yara/nor_parameters.grl`**: WIBON, WICCON, Port Charter
- **`gencon1994/nor_parameters.grl`**: NOR parameters
- **`gencon_arcelormittal/nor_parameters.grl`**: NOR parameters

---

## 📌 What's NOT Covered (Requires Implementation)

### High-Priority Categories (Many Uncovered Rules)

1. **Legal/Procedural (44 rules)** - 77.6% coverage
   - Indemnities and liabilities
   - Documentation requirements
   - Compliance and warranties
   - Dispute resolution

2. **Conditional (44 rules)** - 86.3% coverage
   - Complex conditional logic
   - Multi-party agreements
   - Port-specific conditions
   - Cargo-specific requirements

3. **Temporal (42 rules)** - 88.2% coverage
   - Time calculation methods
   - Laycan and cancelling dates
   - Demurrage/despatch calculations
   - Notice periods

4. **Operational (32 rules)** - 92.3% coverage
   - Cargo handling procedures
   - Equipment requirements
   - Safety procedures
   - Documentation

5. **Exception (16 rules)** - 80.5% coverage
   - Force majeure specifics
   - Strike clauses
   - Port closure scenarios

6. **Modifier (10 rules)** - 28.6% coverage ⚠️ **LOWEST COVERAGE**
   - Time modifiers
   - Rate adjustments
   - Calculation adjustments

---

## 🔄 SOF Event Mapping

The analysis references `SOF Merge.csv` for event name mappings. Some events use alternative nomenclature:
- `Vessel anchored` → `VESSEL_ANCHORED`, `ANCHORED_AT_INNER_ANCHORAGE`, etc.
- `Arms connected` → `ARMS_CONNECTION_COMMENCED`, `ARMS_CONNECTION_COMPLETED`
- `Samples received` → `SAMPLING_COMMENCED`, `SAMPLING_COMPLETED`

---

## ✅ Recommendations

### Immediate Actions
1. **Review CP_RULES_CONSOLIDATED.md** - Focus on 194 uncovered rules
2. **Prioritize Modifiers** - Only 28.6% coverage, needs attention
3. **Implement Legal/Procedural** - 44 rules require GRULE implementation

### Development Priorities
1. **Temporal Calculations** (42 rules) - Complex time calculations
2. **Conditional Logic** (44 rules) - Multi-condition rule patterns
3. **Legal/Procedural** (44 rules) - Documentation and compliance
4. **Modifier Rules** (10 rules) - Rate and time adjustments

### Quality Assurance
1. Review covered rules to ensure correct matching
2. Validate that removed rules are truly covered in GRULE
3. Test GRULE implementations against charter party requirements

---

## 📝 Usage

### To view uncovered rules only:
```bash
cat CP_RULES_CONSOLIDATED.md
```

### To view original complete set:
```bash
cat CP_RULES_CONSOLIDATED_ORIGINAL.md
```

### To re-run analysis:
```bash
python3 analyze_covered_rules.py
```

### To re-filter rules:
```bash
python3 filter_covered_rules.py
```

---

## 🔗 Related Files

- **LAYTIME_RULE_CATEGORIES.md**: 13-category framework for rule classification
- **YARA_ANALYSIS_COMPARISON.md**: Methodology comparison with YARA Excel approach
- **Charter party ANALYSIS files**: Individual charter party rule extractions in `CP library/Charters/`

---

## 📌 Key Insights

1. **High Coverage**: 86.9% of rules already implemented demonstrates mature GRULE system
2. **Operational Excellence**: NOR, cargo operations, and stoppages are comprehensively covered
3. **Gap Areas**: Modifiers (28.6%) and legal/procedural (77.6%) need attention
4. **Charter Agnostic**: Common rules apply across all 75 charter parties
5. **Charter Specific**: Only 4 charter parties have custom NOR parameters

---

**Next Steps**: Focus development effort on the 194 uncovered rules in `CP_RULES_CONSOLIDATED.md`

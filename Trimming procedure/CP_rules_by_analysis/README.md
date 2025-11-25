# Trimming Procedure - File Inventory

This folder contains all scripts, backups, and documentation for the complete process of consolidating 75 charter party laytime rules and identifying GRULE coverage gaps.

## 📋 Main Documentation

**[COMPLETE_TRIMMING_PROCEDURE.md](./COMPLETE_TRIMMING_PROCEDURE.md)** (18 KB)
- Complete walkthrough of the entire process
- Phase-by-phase explanation
- Key findings and recommendations
- Usage instructions for regeneration

## 🔧 Processing Scripts (Sequential Order)

### Phase 1: Extraction & Classification
1. **classify_and_consolidate_rules.py** (11 KB)
   - Extracts rules from 75 charter party analysis files
   - Classifies into 13 rule types
   - Output: CP_RULES_CONSOLIDATED_ORIGINAL.md (26,294 lines)

### Phase 2: GRULE Coverage Analysis
2. **analyze_covered_rules.py** (12 KB)
   - Scans GRULE .grl files for existing coverage
   - Identifies 438 SOF events and 607 stoppage concepts
   - Output: GRULE_COVERAGE_ANALYSIS.md

3. **filter_covered_rules.py** (7.5 KB)
   - Filters out rules already covered by GRULE
   - Removes 1,282 covered rules (86.9%)
   - Output: Filtered file (5,328 lines)

### Phase 3: Deduplication
4. **clean_consolidated.py** (5.4 KB)
   - Identifies and removes duplicate rules
   - Removes 155 duplicates across charter parties
   - Output: Deduplicated file (1,859 lines, 37 unique rules)

### Phase 4: Formatting & Cleanup
5. **make_readable.py** (9.1 KB)
   - First formatting pass
   - Standardizes headers and structure

6. **remove_empty_sections.py** (2.6 KB)
   - Removes charter party sections with no rules
   - Reduces from 1,859 → 870 lines (53.2% reduction)

7. **remove_redundant_separators.py** (1.6 KB)
   - Cleans up double separator patterns `---\n\n\n---`
   - Reduces from 870 → 848 lines (2.5% reduction)

8. **remove_empty_cps.py** (2.0 KB)
   - Removes CPs with 0 rules from statistics table
   - Reduces from 848 → 800 lines (5.7% reduction)
   - Final output: CP_RULES_CONSOLIDATED.md

## 📁 Backup Files (Chronological)

### Stage 1: Original Extraction
**CP_RULES_CONSOLIDATED_ORIGINAL.md** (904 KB, 26,294 lines)
- All 1,476 rules from 75 charter parties
- Organized by rule type and charter party
- Starting point before any filtering

### Stage 2: After GRULE Filtering
**CP_RULES_CONSOLIDATED_BEFORE_CLEANUP.md** (128 KB, 5,328 lines)
- 194 rules remaining after GRULE coverage filter
- 1,282 rules removed (86.9% coverage)
- Still contains many duplicates

### Stage 3: After Deduplication
**CP_RULES_CONSOLIDATED_BEFORE_DECLUTTER.md** (34 KB, 1,859 lines)
- 37 unique rules remaining
- 155 duplicates removed
- Still has empty charter sections

**CP_RULES_CONSOLIDATED_READABLE.md** (2.1 KB)
- Early formatting attempt (appears incomplete)

### Stage 4: After Empty Section Removal
**CP_RULES_CONSOLIDATED_BEFORE_SEPARATOR_CLEANUP.md** (27 KB, 870 lines)
- Empty charter sections removed
- 989 lines of clutter removed

### Stage 5: After Separator Cleanup
**CP_RULES_CONSOLIDATED_WITH_EMPTY_CPS.md** (27 KB, 848 lines)
- Redundant separators removed
- 22 lines cleaned up

### Final Output
**→ Moved to:** `../Rules to consider/CP_RULES_CONSOLIDATED.md` (800 lines)
- Empty CPs removed from statistics table
- Final clean version with 37 unique uncovered rules

## 📊 Analysis Documents

**GRULE_COVERAGE_ANALYSIS.md** (107 KB, 3,556 lines)
- Comprehensive analysis of GRULE implementation
- Lists all 438 SOF event types
- Lists all 607 stoppage/laytime concepts
- Documents coverage patterns

**GRULE_FILTERING_SUMMARY.md** (7.3 KB)
- Summary of filtering process
- Statistics on coverage rates
- Examples of covered vs uncovered rules

## 📈 File Size Progression

| Stage | File | Size | Lines | Reduction |
|-------|------|------|-------|-----------|
| Original | CP_RULES_CONSOLIDATED_ORIGINAL.md | 904 KB | 26,294 | - |
| GRULE Filtered | BEFORE_CLEANUP.md | 128 KB | 5,328 | 79.7% |
| Deduplicated | BEFORE_DECLUTTER.md | 34 KB | 1,859 | 92.9% |
| Decluttered | BEFORE_SEPARATOR_CLEANUP.md | 27 KB | 870 | 96.7% |
| Sep. Cleaned | WITH_EMPTY_CPS.md | 27 KB | 848 | 96.8% |
| **Final** | **CP_RULES_CONSOLIDATED.md** | **27 KB** | **800** | **97.0%** |

## 🎯 Key Results

- **Starting Point:** 1,476 rules from 75 charter parties
- **GRULE Coverage:** 86.9% (1,282 rules already implemented)
- **Unique Uncovered Rules:** 37 (after deduplication)
- **Final File Size:** 800 lines (97% reduction)

## 🔄 Regeneration Instructions

To regenerate the entire process from scratch:

```bash
# Navigate to project root
cd /path/to/cp-laytime-rules

# Phase 1: Extract rules
python3 "Trimming procedure/classify_and_consolidate_rules.py"

# Phase 2: Analyze GRULE coverage
python3 "Trimming procedure/analyze_covered_rules.py"
python3 "Trimming procedure/filter_covered_rules.py"

# Phase 3: Remove duplicates
python3 "Trimming procedure/clean_consolidated.py"

# Phase 4: Format and clean
python3 "Trimming procedure/make_readable.py"
python3 "Trimming procedure/remove_empty_sections.py"
python3 "Trimming procedure/remove_redundant_separators.py"
python3 "Trimming procedure/remove_empty_cps.py"
```

## 📝 Notes

- All scripts are designed to run independently
- Each script preserves the input file (no destructive edits)
- Backups allow rollback to any previous stage
- Scripts assume working directory is project root
- Some scripts may need path adjustments if file locations change

## 🔗 Related Files

- **Input Data:** `../CP library/Charters/` (75 charter party folders)
- **GRULE Rules:** `../CP library/rule/` (.grl files)
- **Final Output:** `../Rules to consider/CP_RULES_CONSOLIDATED.md`
- **Laytime-Only Rules:** `../Rules to consider/MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md`

---

**Created:** November 25, 2025  
**Purpose:** Document complete trimming procedure for CP laytime rules consolidation  
**Status:** Complete ✅

# Charter Party Laytime Rules Library

A comprehensive library of laytime calculation rules extracted from charter party forms, cleaned and organized for integration with rules engines.

## 🌟 Repository Highlights

- **Production-Ready File:** `MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md` - 20 rules across 18 charters (328 lines)
- **Complete Collection:** 261 unique laytime rules from 75 charter party families
- **Grule Integration:** Ready-to-use `.grl` files for rules engine
- **9-Phase Cleanup:** Comprehensive documentation of extraction and cleanup process

## 📁 Files

### Main Documents

- **MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md** (18 KB) ⭐ **PRODUCTION READY**
  - **20 charter-specific rules** across **18 charter parties**
  - **328 lines** of pure laytime calculation logic
  - **Zero** legal/financial/administrative content
  - **Verified clean** - ready for rules engine integration
  - Result of 9-phase comprehensive cleanup (see Phase 9 report)

- **MASTER_CP_LAYTIME_RULES.md** (451 KB)
  - Complete collection of 261 unique laytime rules
  - Organized by charter party family (52 charters)
  - All duplicates removed (within-charter and cross-charter)
  - 100% laytime-relevant content only

- **LAYTIME_RULES_EXPLANATIONS.md** (130 KB)
  - Detailed explanations for all 261 rules
  - Each rule includes: Purpose, Covers, Effect, Conditions, Text Preview
  - Organized by charter party
  - Numbered 1-261 for easy reference

- **LAYTIME_RULES_SUMMARY.md** (10 KB)
  - Categorical overview of all rules
  - 20 rule categories (e.g., Time NOT Counting, Laytime Commencement, Surveys, etc.)
  - Top 10 charter parties by rule count
  - Common rule patterns and structures
  - Quick reference guide

### Documentation & Reports

- **PHASE_9_COMPREHENSIVE_CLEANUP_REPORT.md** ⭐ **LATEST**
  - Comprehensive legal/copyright/metadata cleanup
  - Analysis of Phase 8 failures (13 rules with issues)
  - Rule-by-rule cleanup documentation
  - Final verification results

- **FINAL_MASTER_DEDUPLICATION_REPORT.md**
  - Complete processing history
  - 5-phase pipeline documentation (22,412 → 261 rules)
  - Methodology and statistics
  - Quality assurance details

- **Additional Phase Reports:**
  - PHASE_8_FINAL_LEGAL_CLEANUP_REPORT.md
  - PHASE_7B_CONFIGURATION_FILTERING_REPORT.md
  - RULES_ENGINE_INTEGRATION_REPORT.md
  - PROJECT_COMPLETION_SUMMARY.md
  - And more...

### Charter Party Folders

- **Charters/** - 75 subdirectories containing individual charter party laytime rules
  - Each folder contains cleaned, deduplicated, laytime-only rules
  - Examples: ALCOA, AMWELSH, NORGRAIN, VALE, CSP, etc.

## 📊 Statistics

### Production File (MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md)
- **Starting Point:** 1,002 lines, 63 rules (corrupted file)
- **Final Result:** 328 lines, 20 rules (production ready)
- **Reduction:** 67.3% lines, 68.3% rules
- **9-Phase Cleanup:**
  1. Corruption removal
  2. .grl-covered operations removal
  3. Legal warranties removal
  4. Financial/legal terms cleanup
  5. Administrative settings removal
  6. Stevedore liability cleanup
  7. Port charges removal
  8. Certificate compliance cleanup
  9. Comprehensive legal/copyright/metadata cleanup (Phase 9)

### Complete Collection (MASTER_CP_LAYTIME_RULES.md)
- **Starting Point:** 22,412 raw extracts from 75 charter parties
- **Final Result:** 261 unique laytime rules from 52 charter parties
- **Reduction:** 98.8% (removed duplicates and non-laytime content)
- **Processing Phases:**
  1. Basic deduplication (22,412 → 14,445)
  2. Semantic deduplication (14,075 → 2,464)
  3. Topic filtering (2,464 → 292)
  4. Cross-charter deduplication (292 → 261)
  5. Explanation generation (261 rules explained)

## 🎯 Content Quality

- ✅ ZERO exact duplicates
- ✅ ZERO semantic duplicates
- ✅ ZERO non-laytime clauses
- ✅ 100% laytime-calculation-relevant rules only
- ✅ All rules from post-arrival operations (no voyage/scheduling clauses)

## 📖 How to Use

1. **Browse All Rules:** Open `MASTER_CP_LAYTIME_RULES.md`
2. **Understand Rules:** Read `LAYTIME_RULES_EXPLANATIONS.md` for detailed explanations
3. **Find by Category:** Use `LAYTIME_RULES_SUMMARY.md` to find rules by topic
4. **Charter-Specific:** Browse individual folders in `Charters/` directory

## 🔍 Rule Categories

Top categories by frequency:
1. **Time NOT Counting** (~100 rules) - Exclusions from laytime
2. **Laytime Commencement** (~40 rules) - When time starts
3. **Time Counting** (~30 rules) - Inclusions in laytime
4. **Loading/Discharging Rates** (~25 rules) - Cargo handling rates
5. **Surveys & Inspections** (~20 rules) - Draft surveys, hold inspections
6. **Interruptions & Force Majeure** (~20 rules) - Strikes, weather, etc.
7. **Shifting Time** (~20 rules) - Vessel movements
8. **And 13 more categories...**

## 📋 Top Charter Parties (by rule count)

1. NORGRAIN - 17 rules
2. NYPE - 16 rules
3. RTS - 16 rules
4. AMWELSH - 15 rules
5. VALE - 14 rules
6. SYNACOMEX - 14 rules
7. CSP - 11 rules
8. SAMARCO - 11 rules
9. CSN - 9 rules
10. ANGLO AMERICAN VOYAGE - 9 rules

## 🛠️ Processing Methodology

- **Text Normalization:** Aggressive whitespace/formatting removal
- **Hash-Based Deduplication:** MD5 for exact duplicates
- **Semantic Analysis:** Multi-criteria duplicate detection (70% overlap threshold)
- **Topic Classification:** Pattern-based filtering (14 exclude patterns, 18 include patterns)
- **Cross-Charter Comparison:** N² semantic matching across all charters
- **Natural Language Analysis:** Purpose identification, effect analysis, condition extraction

## 📅 Last Updated

November 20, 2025

---

**Note:** This library is the result of comprehensive processing to extract, clean, deduplicate, and explain all unique laytime rules from 75 charter party families. All intermediate processing files have been removed to keep the library clean and focused on the final deliverables.
# cp-laytime-rules

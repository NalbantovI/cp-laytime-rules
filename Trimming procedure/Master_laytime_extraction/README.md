# Master Laytime Extraction - Files Inventory

This folder contains all files related to the extraction and cleaning of pure laytime calculation rules from the master charter party rulebook.

## Purpose

Extract laytime-affecting provisions from comprehensive charter party rules, excluding all legal, procedural, and administrative content that doesn't directly impact time counting.

## Final Output Location

**Production File:** `Rules to consider/MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md`
- 23 charter parties covered
- ~25 pure laytime calculation rules
- Focused on time counting/suspension/exclusion logic

---

## File Inventory

### 1. Source Documents

#### MASTER_CP_LAYTIME_RULES.md
- **Type:** Source document
- **Content:** Comprehensive master rulebook with all rule types
- **Size:** Complete charter party rules (laytime + legal + admin)
- **Status:** Master reference

#### MASTER_CP_LAYTIME_RULES_BACKUP.md
- **Type:** Backup
- **Content:** Safety copy of original master document
- **Purpose:** Preserve original before extraction
- **Status:** Archived

---

### 2. Intermediate Files (Extraction Journey)

#### MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY_CORRUPTED.md
- **Type:** Initial extraction (failed)
- **Issues:**
  - Rules misplaced under wrong charter parties
  - Inconsistent numbering
  - Truncated rule text
  - Empty sections
- **Purpose:** Preserved for debugging reference
- **Status:** Superseded by later versions

#### MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY_BEFORE_FIX.md
- **Type:** Pre-correction version
- **Content:** Extracted laytime rules before structure cleanup
- **Issues:**
  - Needed rule repositioning
  - Required numbering fixes
  - Formatting inconsistencies
- **Purpose:** Backup before final corrections
- **Status:** Superseded by final version

---

### 3. Related Documents

#### MASTER_CP_LAYTIME_RULES_LOGIC_ONLY.md
- **Type:** Experimental extraction
- **Content:** Alternative approach focusing on pure logic rules
- **Difference:** May include non-laytime logic rules
- **Status:** Experimental, not used in final output

---

### 4. Processing Scripts

#### extract_laytime_only.py
- **Purpose:** Initial extraction of laytime-affecting rules
- **Process:**
  1. Read MASTER_CP_LAYTIME_RULES.md
  2. Identify laytime-affecting keywords
  3. Extract complete rule clauses
  4. Preserve charter party context
- **Output:** Initial LAYTIME_ONLY file
- **Status:** First-pass extraction

#### extract_clean_laytime_from_master.py
- **Purpose:** Structure correction and cleaning
- **Process:**
  1. Fix misplaced rules
  2. Renumber rules sequentially per charter
  3. Remove or annotate empty sections
  4. Validate rule completeness
  5. Clean formatting
- **Output:** MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY_BEFORE_FIX.md
- **Status:** Correction pass

#### comprehensive_cleanup_laytime.py
- **Purpose:** Final comprehensive cleanup
- **Process:**
  1. Standardize whitespace
  2. Validate section headers
  3. Ensure consistent formatting
  4. Update metadata
  5. Finalize document structure
- **Output:** Final MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md
- **Status:** Finalization pass

---

## Processing Pipeline

```
MASTER_CP_LAYTIME_RULES.md (source)
           ↓
   [extract_laytime_only.py]
           ↓
MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY_CORRUPTED.md (initial extraction)
           ↓
   [extract_clean_laytime_from_master.py]
           ↓
MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY_BEFORE_FIX.md (corrected structure)
           ↓
   [comprehensive_cleanup_laytime.py]
           ↓
MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md (final ✅)
           ↓
   [Moved to: Rules to consider/]
```

---

## Charter Parties Covered

**Total:** 23 charter parties
**With Rules:** 19 charter parties
**Without Rules:** 4 charter parties (RTM, TRAFIGURA, YANCOAL, noted as having no specific laytime rules)

### Key Charter Parties with Laytime Rules:
- ALCOA (1 rule)
- ANGLO AMERICAN VOYAGE (1 rule)
- BULK_SUGAR (1 rule)
- COAL_OREVOY (2 rules)
- CSP (2 rules)
- ENEL (1 rule)
- FERTIVOY (1 rule)
- GTA (1 rule)
- NYPE (1 rule)
- POLCOALVOY (1 rule)
- POSCO (2 rules)
- SHELLTIME (2 rules)
- SYNACOMEX (1 rule)
- VALE (1 rule)
- WORLDFOOD (2 rules)
- YARA CP (1 rule)

---

## Usage Instructions

### To Regenerate from Source

```bash
# Navigate to this folder
cd "Trimming procedure/Master_laytime_extraction"

# Step 1: Extract laytime rules
python3 extract_laytime_only.py

# Step 2: Clean and correct structure
python3 extract_clean_laytime_from_master.py

# Step 3: Final cleanup
python3 comprehensive_cleanup_laytime.py
```

### To Update with New Charter Parties

1. Add new rules to `MASTER_CP_LAYTIME_RULES.md`
2. Re-run processing scripts
3. Manually verify extracted rules for laytime impact
4. Update validation checks

---

## Key Differences from CP Rules Consolidation

**MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md:**
- Focus: Pure laytime calculation only
- Source: Single master document
- Charter Parties: 23
- Rules: ~25 laytime-affecting provisions
- Content: Complete charter party clauses as written

**CP_RULES_CONSOLIDATED.md:**
- Focus: All rule types (13 categories)
- Source: 75 individual charter parties
- Charter Parties: 75
- Rules: 37 unique uncovered rules (post-GRULE filtering)
- Content: Rules not yet in GRULE implementation

---

## File Statistics

### Source Documents: 2 files
- MASTER_CP_LAYTIME_RULES.md
- MASTER_CP_LAYTIME_RULES_BACKUP.md

### Intermediate Files: 2 files
- MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY_CORRUPTED.md
- MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY_BEFORE_FIX.md

### Related Files: 1 file
- MASTER_CP_LAYTIME_RULES_LOGIC_ONLY.md

### Processing Scripts: 3 files
- extract_laytime_only.py
- extract_clean_laytime_from_master.py
- comprehensive_cleanup_laytime.py

**Total Files in Folder:** 8 files

---

## Documentation

**Main Documentation:** `../MASTER_LAYTIME_EXTRACTION_PROCEDURE.md`

This comprehensive document explains:
- Complete extraction methodology
- Phase-by-phase process
- Extraction vs exclusion criteria
- Charter party coverage
- Rule patterns identified
- Implementation guidance
- Validation procedures

---

## Related Projects

**CP Rules Consolidation:**
- Folder: `CP_rules_by_analysis/`
- Documentation: `COMPLETE_TRIMMING_PROCEDURE.md`
- Output: `Rules to consider/CP_RULES_CONSOLIDATED.md`

**GRULE Coverage:**
- Analysis: Various coverage reports in CP library/
- Implementation: 5 .grl files (438 SOF events, 607 stoppage concepts)

---

**Last Updated:** November 25, 2025  
**Folder Created:** November 25, 2025  
**Status:** Complete ✅

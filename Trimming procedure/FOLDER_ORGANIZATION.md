# Folder Organization Strategy

**Created:** November 25, 2025  
**Purpose:** Document file organization rules for all work on consolidated rules

---

## Organization Rules

### 1. CP_rules_by_analysis/

**Purpose:** All files related to CP_RULES_CONSOLIDATED.md processing and analysis

**Store here:**
- ✅ Processing scripts for CP_RULES_CONSOLIDATED.md
- ✅ Backup versions showing transformation journey
- ✅ Analysis reports (GRULE coverage, filtering summaries)
- ✅ Any tools/scripts needed for future CP rules work
- ✅ README.md with file inventory

**Currently contains:** 17 files
- 8 Python processing scripts
- 6 backup files (transformation journey)
- 2 analysis documents
- 1 README.md

---

### 2. Master_laytime_extraction/

**Purpose:** All files related to MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md extraction and processing

**Store here:**
- ✅ Extraction scripts for laytime-only rules
- ✅ Source documents (MASTER_CP_LAYTIME_RULES.md + backup)
- ✅ Intermediate files showing extraction journey
- ✅ Any tools/scripts needed for future master laytime work
- ✅ README.md with file inventory

**Currently contains:** 8 files
- 3 Python processing scripts
- 5 source/intermediate files
- 1 README.md

---

### 3. _temp_workspace/

**Purpose:** Temporary working files that will be deleted after use

**Store here:**
- 🗑️ Temporary analysis outputs
- 🗑️ Experimental scripts (one-time use)
- 🗑️ Intermediate processing files (not needed for reproduction)
- 🗑️ Test outputs
- 🗑️ Scratch work files

**Lifecycle:**
1. Create temporary files here during work
2. When finished, either:
   - **Move to appropriate folder** (CP_rules_by_analysis/ or Master_laytime_extraction/) if needed for future
   - **Delete immediately** if one-time use only
3. Periodically clean this folder (review and delete all contents)

**Currently contains:** Empty (just created)

---

## Decision Tree: Where Should This File Go?

```
Is this file related to CP_RULES_CONSOLIDATED.md?
├─ YES → Will you need it in the future?
│  ├─ YES → Move to CP_rules_by_analysis/
│  └─ NO → Put in _temp_workspace/ → Delete when done
│
└─ NO → Is it related to MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY.md?
   ├─ YES → Will you need it in the future?
   │  ├─ YES → Move to Master_laytime_extraction/
   │  └─ NO → Put in _temp_workspace/ → Delete when done
   │
   └─ NO → Is it general documentation?
      ├─ YES → Keep in Trimming procedure/ root
      └─ NO → Put in _temp_workspace/ → Delete when done
```

---

## Examples

### Files to Keep in CP_rules_by_analysis/
```
✅ classify_and_consolidate_rules.py (may need to re-run)
✅ filter_covered_rules.py (reproducible processing)
✅ CP_RULES_CONSOLIDATED_ORIGINAL.md (shows starting point)
✅ GRULE_COVERAGE_ANALYSIS.md (reference for what's implemented)
```

### Files to Keep in Master_laytime_extraction/
```
✅ extract_laytime_only.py (may need to re-run)
✅ MASTER_CP_LAYTIME_RULES.md (source document)
✅ MASTER_CP_LAYTIME_RULES_LAYTIME_ONLY_CORRUPTED.md (shows issues encountered)
```

### Files to Delete After Use (_temp_workspace/)
```
🗑️ test_analysis.py (one-time test)
🗑️ temp_output.txt (temporary result)
🗑️ debug_log.txt (debugging artifact)
🗑️ scratch_work.md (exploratory notes)
```

---

## Maintenance Guidelines

### Daily Workflow
1. **Create files** in _temp_workspace/ for any new work
2. **Test and validate** the work
3. **Decide immediately**: keep or delete?
4. **Move keepers** to appropriate subfolder with clear naming
5. **Delete one-time files** right after task completion

### Weekly Review
- Review _temp_workspace/ contents
- Verify all files are either moved or deleted
- Clean out any forgotten temporary files

### Monthly Audit
- Review CP_rules_by_analysis/ - are all files still needed?
- Review Master_laytime_extraction/ - are all files still needed?
- Update README.md files in each subfolder if contents change

---

## Current Folder Structure

```
Trimming procedure/
├── COMPLETE_TRIMMING_PROCEDURE.md (18 KB)
├── MASTER_LAYTIME_EXTRACTION_PROCEDURE.md (19 KB)
├── FOLDER_ORGANIZATION.md (this file)
│
├── CP_rules_by_analysis/ (17 files)
│   ├── 8 processing scripts (.py)
│   ├── 6 backup files (.md)
│   ├── 2 analysis documents (.md)
│   └── README.md
│
├── Master_laytime_extraction/ (8 files)
│   ├── 3 processing scripts (.py)
│   ├── 5 source/intermediate files (.md)
│   └── README.md
│
└── _temp_workspace/ (0 files - for temporary work)
    └── (empty - clean regularly)
```

---

## Benefits of This Organization

✅ **Clear separation** between permanent and temporary files
✅ **Easy cleanup** - just delete _temp_workspace/ contents periodically
✅ **Reproducible work** - all needed files preserved in topic-specific folders
✅ **No clutter** - temporary files don't pollute important folders
✅ **Quick decisions** - simple rules for where files belong
✅ **Git friendly** - can .gitignore _temp_workspace/ folder

---

**Last Updated:** November 25, 2025  
**Status:** Active organizational structure ✅

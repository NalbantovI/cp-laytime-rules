# LEGAL WARRANTY CLEANUP REPORT

**Date:** 2025-11-24  
**Operation:** Removed legal warranty clauses without laytime calculation impact

---

## Overview

This cleanup removed **legal warranty and representation clauses** that contain no laytime calculation logic. These are purely administrative/legal compliance statements.

---

## Removed Content

### 1. YARA CP - Sanctions Section (Complete Removal)
**Clause 58: Sanctions**

Removed entire section:
```
58. Sanctions
Owners represent and warrant to Charterer:
(a) that the vessel, Owners and Disponent Owners are not sanctioned under the U.S., English,
    European Union or Swiss Economic Sanctions Laws relating to transactions with restricted 
    countries, persons and entities (the "Sanctions Laws")...
(b) that the vessel is not registered by, and that the vessel, Owners and Disponent Owners 
    are not in a way, directly or indirectly, owned by, controlled by, or related to any country...
(c) that the above representations and guarantees are continuing throughout the duration...
```

**Reason:** Pure legal warranty with no laytime impact. No time counting, suspension, or calculation logic.

---

### 2. YARA CP - Blacklist Warranty (Single Line)
**Removed:**
```
Owners warrant that vessel is not blacklisted by the Arab League.
```

**Reason:** Legal warranty without laytime consequence. No time implications.

**Note:** The **boycott clause** immediately above this was **KEPT** because it states:
```
time lost as a consequence thereof not to count as lay time or time on demurrage
```
This has clear laytime calculation impact.

---

### 3. VALE - Sanctions Warranty (Clause 11 excerpt)
**Removed:**
```
(11) Vessel shall not be owned, chartered, operated or controlled by either a person or entity
     who is the subject or target of an economic or trade sanction or by a person or entity
     registered or managed in or a citizen or resident or located in a country the subject of
     sanctions imposed by any of the United Nations, the European Union, the United States
     Department of Treasury's Office of Foreign Assets Control or any other regulatory body
     enforcing economic and trade sanctions legislation...
```

**Reason:** Legal warranty/representation. No laytime calculation impact.

**Note:** VALE's other clauses with actual laytime logic (grab discharge, time lost for owner's account) were preserved.

---

## What Was Preserved

### YARA CP - Boycott Clause ✅ KEPT
```
57. Boycott
In the event of a boycott (whether legal or not) being imposed or threatened to be imposed due to
the vessel's flag, ownership, nationality of the crew, terms under which the crew is employed or labor
conditions onboard, previous port calls, time lost as a consequence thereof not to count as lay time or
time on demurrage and Owners to be responsible for all costs and consequences resulting thereof.
```

**Reason:** Contains laytime calculation logic:
- "time lost... not to count as lay time or time on demurrage"
- Clear time suspension trigger (boycott)
- Cost attribution (owner's responsibility)

---

## Results

### Statistics
- **Lines removed:** 26 lines
- **Sections removed:** 3 (YARA sanctions, YARA blacklist warranty, VALE sanctions)
- **Laytime logic preserved:** 100%

### Before/After
- **Before:** 1,281 lines
- **After:** 1,255 lines
- **Reduction:** 2.0%

### Charters & Rules
- **Charters:** 30 (unchanged)
- **Rules:** 57 (unchanged - removed content within existing rules)

---

## Verification

### ✅ Confirmed Removed:
- ❌ "Sanctions Laws" - Not found
- ❌ "OFAC" references - Not found
- ❌ "blacklisted by Arab League" - Not found
- ❌ "economic or trade sanction" warranties - Not found

### ✅ Confirmed Preserved:
- ✅ "boycott" clause with time impact - Present
- ✅ "time lost" references - Present
- ✅ All other laytime calculation logic - Intact

---

## Category Classification

These removed clauses fall under:

**Category:** Legal Warranties & Representations  
**Type:** Administrative/Compliance  
**Laytime Impact:** None  
**Similar to:** 
- Certificate requirements
- Hague Rules clauses
- Mortgage information
- Insurance warranties

---

## Recommendation

This cleanup successfully removes **legal boilerplate** that has no bearing on laytime calculations, further focusing the document on pure **calculation logic**.

The file now contains:
- ✅ Time counting/suspension rules
- ✅ Cost attribution logic
- ✅ Delay consequence clauses
- ✅ Laytime trigger conditions
- ❌ Legal warranties (removed)
- ❌ Compliance statements (removed)

---

**Status:** ✅ COMPLETE - Legal warranties removed, laytime logic preserved


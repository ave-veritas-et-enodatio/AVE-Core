# KB Structure Review — Phase 4 Iteration 3 (Final)

**Date:** 2026-04-03
**Scope:** `ave-kb/` — 814 files

---

## Summary

Two prior iterations confirmed clean. Two new Warnings found: (1) four pointer/reference index files lack Key Results sections; (2) all four vol3 domain indexes use bulleted `## Contents` instead of the KB-standard `## Derivations and Detail` table. All iter-1 and iter-2 fixes verified clean.

---

## Findings

### W-1: Four index files lack Key Results sections

**Files:**
- `ave-kb/common/index.md` — no Key Results, only `## Contents` table
- `ave-kb/common/translation-tables/index.md` — no Key Results, only `## Contents` table
- `ave-kb/vol5/common/index.md` — no Key Results, only `## Contents` bulleted list
- `ave-kb/vol8/appendix/index.md` — no Key Results, explanation is in prose not table

**Navigation impact:** Agents arriving at `common/index.md` (direct entry-point target) find no synthesized result — must visit all children to assess relevance. The vol8/appendix fact ("Vol 8 contributes no experiments") exists in prose, not a scannable Key Results row.

**Fix:** Add `## Key Results` section to each. For pointer-only indexes (vol8/appendix), a single row making the null-result explicit: e.g., "Vol 8 contributes no experimental programme — see unified index."

---

### W-2: Vol3 domain indexes use `## Contents` bullet list instead of `## Derivations and Detail` table

**Files:**
- `vol3/gravity/index.md`
- `vol3/condensed-matter/index.md`
- `vol3/cosmology/index.md`
- `vol3/applied-physics/index.md`

All four have `## Key Results` (correct) then `## Contents` (bulleted list). Every other volume's domain indexes use `## Derivations and Detail` with Document | Contents columns.

**Navigation impact:** Agents calibrated to scan for `## Derivations and Detail` must fall back to full-document parsing for vol3. Vol3 is the only volume with this divergence.

**Fix:** Convert `## Contents` to `## Derivations and Detail` table with Document | Contents columns in all four vol3 domain indexes.

---

### N-1: CLAUDE.md silent on whether index.md files may carry leaf marker

**File:** `vol2/appendices/app-c-derivations/index.md` (the only file in its directory, carrying `<!-- leaf: verbatim -->` on line 2)

**Fix:** Add one sentence to CLAUDE.md INVARIANT-S5 or INVARIANT-S6 explicitly permitting leaf content in `index.md` for single-file directories.

---

### N-2: vol8/appendix/index.md uplink text truncates parent title

**File:** `vol8/appendix/index.md` line 1: `[↑ Vol 8: Virtual Media](../index.md)` — parent title is "Vol 8: Virtual Media and Informational Topology".

**Fix:** Either correct the uplink text to match exactly, or document a short-title convention in CLAUDE.md.

---

## Confirmed Clean (All Prior Fixes)

- iter-2 ITEM-1: `vol6/framework/computational-mass-defect/abcd-transfer-matrix.md` line 3 = `<!-- path-stable: referenced from vol6 as sec:abcd_cascade -->` ✓
- iter-2 ITEM-2: vol8/ch1 and vol8 Key Results rows differentiated (framing vs derivation) ✓
- vol5/common/ children all listed ✓
- vol2/appendices/ all 6 subdirectories in Derivations table ✓
- vol1/operators-and-regimes/ all 3 chapters in Derivations table ✓
- entry-point all 9 links (8 volumes + common/) resolve ✓
- Cross-volume Primary links: 6 samples all exist ✓
- No unexplained missing children in any subject-domain Derivations table ✓

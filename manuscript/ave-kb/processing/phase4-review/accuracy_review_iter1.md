# KB Accuracy Review — Phase 4 Iteration 1

**Date:** 2026-04-03
**Scope:** `ave-kb/` — spot-check of 10+ leaf documents against LaTeX source; 7 known issues investigated

---

## Summary

4 Critical findings, 2 Warnings, 3 Notes.

The most significant finding is system-wide: Chapter Summary (`\section*{Chapter Summary}`, `\begin{summarybox}`) and Exercises (`\section*{Exercises}`, `\begin{exercisebox}`) sections are absent from virtually all leaf documents. 34+ source chapters contain these endings; the KB captures them in only 1 file. Every leaf covering the final section of a chapter is systematically incomplete. This is a Critical leaf-fidelity violation.

---

## Critical Findings

---

### FINDING-001 (CRITICAL, system-wide): Chapter Summary and Exercises sections absent from virtually all leaves

**Issue:** `\section*{Chapter Summary}`, `\section*{Exercises}`, `\begin{summarybox}`, and `\begin{exercisebox}` blocks appear at the end of 34+ chapters across all volumes. The distilled KB captures these sections in only 1 file. Every leaf document covering the terminal section of its chapter is missing this content.

**Scope:** System-wide — affects ~34+ chapters across all 8 volumes.

**Leaf fidelity impact:** Per protocol invariant, a leaf document must contain verbatim LaTeX→Markdown translation of its source section. Any leaf covering the final chapter section that omits the summarybox/exercisebox is incomplete and does not meet the leaf fidelity standard.

**Fix guidance:** Identify all chapter-final leaf documents. Append the Chapter Summary and Exercises content from the corresponding LaTeX source. This must be done per leaf, not per chapter index.

---

### FINDING-002 (CRITICAL): mond-hoop-stress.md missing "Dark Sector Comparison" table

**Issue:** `ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md` is missing the "Dark Sector Comparison: AVE vs. Observation" subsection table (4 rows: $H_\infty$, $a_0$, dark matter, dark energy). This content appears at source lines 240–254 of `04_continuum_electrodynamics.tex`.

**Location:** `vol1/dynamics/ch4-continuum-electrodynamics/mond-hoop-stress.md` — table absent.

**Source:** `manuscript/volumes/01_foundations/04_continuum_electrodynamics.tex` lines 240–254.

**Leaf fidelity impact:** The leaf is incomplete; source content not present.

---

### FINDING-003 (CRITICAL): vol8/ch1 leaves omit opening paragraph and Hardware/Software Isomorphism Inversion subsection

**Issue:** `ave-kb/vol8/foundations/ch1-llm-topology/` leaves omit the chapter's opening paragraph and "Hardware/Software Isomorphism Inversion" subsection (source lines 3–17 of `01_llm_topology.tex`), including the saturation operator $S(r) = \sqrt{1 - (A/A_c)^2}$ and the $Z \propto A$ vs $Z \propto 1/A$ inversion analysis.

**Location:** `vol8/foundations/ch1-llm-topology/` — first leaf(s) missing opening content.

**Source:** `manuscript/volumes/08_virtual_media/01_llm_topology.tex` lines 3–17.

**Leaf fidelity impact:** Verbatim extraction did not capture the chapter opening.

---

### FINDING-004 (CRITICAL): Vol2 App A pointer leaves state wrong canonical KB location

**Issue:** `vol2/appendices/app-a-translation-matrix/translation-protein.md` and `translation-protein-solver.md` claim canonical KB location is `ave-kb/common/`. The actual distilled location is `ave-kb/vol5/common/translation-protein.md` and `ave-kb/vol5/common/translation-protein-solver.md`. No protein translation files exist in `ave-kb/common/`.

**Location:**
- `vol2/appendices/app-a-translation-matrix/translation-protein.md` body
- `vol2/appendices/app-a-translation-matrix/translation-protein-solver.md` body
- `vol2/appendices/app-a-translation-matrix/index.md` "Canonical Location" column

**Fix:** Update canonical location references from `ave-kb/common/` to `ave-kb/vol5/common/`. Add direct hyperlinks to `../../../vol5/common/translation-protein.md` and `../../../vol5/common/translation-protein-solver.md`.

*Note: Also flagged as CRITICAL-1 by structure reviewer.*

---

## Warning Findings

---

### FINDING-005 (WARNING): 39 instances of `**[Result]**` instead of `**[Resultbox]**` in vol3 cosmology leaves

**Issue:** INVARIANT-S1 specifies that resultbox tcolorbox content must render as `**[Resultbox]**`. 39 leaf documents in `vol3/cosmology/` use `**[Result]**` instead.

**Location:** `vol3/cosmology/` — dark-sector and orbital-regimes subdirectories, approximately 39 instances across ~15 files.

**Fix:** Global replace `**[Result]**` → `**[Resultbox]**` in affected vol3 cosmology leaves.

---

### FINDING-006 (WARNING): vol1/ch1 index Key Results uses `\|...\|` instead of `|...|`

**Issue:** `ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/index.md` Key Results table uses `\|...\|` (LaTeX norm delimiter) for the Macroscopic Hardware Action formula; the source uses `|...|` (single-pipe absolute value).

**Location:** `vol1/axioms-and-lattice/ch1-fundamental-axioms/index.md` Key Results table.

**Fix:** Replace `\|...\|` with `|...|` in the affected formula.

---

## Notes (Non-Actionable)

---

### NOTE-1: Vol6 neon $81.181d$ / $81.158d$ discrepancy is source-level

Both values appear in the source LaTeX. The KB correctly preserves both. No action required.

---

### NOTE-2: Vol6 fluorine $398.5d$ / $398.478d$ discrepancy is source-level

Both values appear in the source LaTeX. The KB correctly preserves both. No action required.

---

### NOTE-3: sec:membrane_phase_buffering path resolves

The cross-reference `sec:membrane_phase_buffering` resolves to `ave-kb/vol5/molecular-foundations/organic-circuitry/membrane-phase-buffering.md`. No broken link; pointer is informative.

---

## Out of Scope

- Exhaustive leaf-by-leaf source comparison across all 813 files (10+ spot-checked)
- Structure and navigation (covered by structure reviewer)
- Notation macro translations not involving resultbox/exercisebox markers

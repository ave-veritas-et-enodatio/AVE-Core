# Phase 4 Accuracy Review — Iteration 2

**Date:** 2026-04-03
**Scope:** Verification of iter-1 fixes (C-4, C-5, W-3) plus new scans of vol4/index.md Key Results, W-5 resolved link, and spot-checks from vol6 and vol7.

---

## Summary

The two highest-priority iter-1 fixes are confirmed clean: the C-4 new leaf (`llm-topology-intro.md`) is verbatim from source lines 5–17 with no deviations, and the C-5 Dark Sector Comparison table is exact. One Warning: three subsections from `01_llm_topology.tex` lines 19–46 may have no KB representation (though existing ch1 leaves may cover them — needs verification). One Note: source-internal H_∞ inconsistency (69.32 vs 69.33) faithfully preserved — no action.

---

## Confirmed Clean

**C-4 verbatim check:** `llm-topology-intro.md` is word-for-word from source lines 5–17. Heading translations correct. $S(r) = \sqrt{1-(A/A_c)^2}$ typeset correctly. ✓

**C-5 verbatim check:** `mond-hoop-stress.md` Dark Sector Comparison table — all four rows verified against source lines 248–253. $H_\infty$ = 69.32 km/s/Mpc, $a_0 = 1.07 \times 10^{-10}$ m/s², Dark Matter (metric drag), Dark Energy (lattice genesis latent heat). ✓

**W-3 spot-check:** Zero `**[Result]**` found anywhere in KB. Vol3 cosmology leaves correctly use `**[Resultbox]**`. ✓

**W-5 link target:** `vol2/particle-physics/ch02-baryon-sector/index.md` exists and correctly covers baryon sector derivations. ✓

**vol6 spot-check (ABCD Transfer Matrix):** `abcd-transfer-matrix.md` verified verbatim against `01_computational.tex` §"Transfer Matrix Cascade" lines 196–210. ✓

**vol7 spot-check (HOH Bond Angle):** `s04-hoh-bond-angle.md` verified verbatim against `03_melting_eigenmode.tex` §"The H--O--H Bond Angle" lines 297–408. Resultbox, degree symbol, comparison table, all present. ✓

**vol4/index.md Key Results provenance:** All entries trace to subdomain index content already in the KB. No externally injected or derived-as-given content. ✓

---

## Findings

### FINDING-002 (WARNING): C-4 leaf may cover only 2 of 5 source subsections

**Issue:** `llm-topology-intro.md` covers source lines 5–17 (chapter opening + Hardware/Software Isomorphism Inversion). Source `01_llm_topology.tex` also contains:
- Lines 19–26: `\subsection{Axiom 1: The SwiGLU Two-Port Node...}` — coupled RMS amplitude formula
- Lines 28–35: `\subsection{The Thermodynamic Emergence of $A_c$}` — critical boundary derivation
- Lines 37–44: `\subsection{Axiom 3: Least Reflected Action in Pruning}` — pruning reflection coefficient

**Note for synthesizer:** The ch1 directory contains pre-existing leaves `swiglu-twoport.md`, `ac-thermodynamic.md`, and `axiom3-pruning.md` — whose names exactly match the three "missing" subsections. Verify whether these leaves cover source lines 19–46 before flagging as unaddressed. If they do, FINDING-002 is a false alarm.

**Location:** `vol8/foundations/ch1-llm-topology/llm-topology-intro.md` (scope question)

---

### FINDING-003 (NOTE): Source-internal $H_\infty$ inconsistency faithfully preserved — no action

Both values (69.32 and 69.33 km/s/Mpc) appear in the source; the KB correctly preserves both. No distillation error. Future passes must not normalize. Recorded for maintainability.

---

## Out of Scope

Volumes 2, 5; most vol3/vol4/vol8 leaves not sampled in iter-2.

# Phase 4 Accuracy Review — Iteration 3 (Final)

**Date:** 2026-04-03
**Scope:** New volumes sampled: vol2/ch02 baryon sector, vol4/ch3 HOPF-01, vol5 molecular-foundations, common/translation-gravity.

---

## Summary

2 Critical, 1 Warning. Both Criticals are leaf fidelity violations (verbatim requirement broken). All other checks clean.

---

## Findings

### FINDING-ITA-01 (CRITICAL): vol2/ch02 baryon leaves normalize script ell to roman ell

**Files:**
- `vol2/particle-physics/ch02-baryon-sector/thermal-softening.md`
- `vol2/particle-physics/ch02-baryon-sector/self-consistent-mass-oscillator.md`

**Issue:** Source `vol_2_subatomic/chapters/02_baryon_sector.tex` uses script ell `\ell_{node}` at lines 121, 131, and 160 (inside resultbox content: "Orthogonal Flux Tube Mutual Coupling," "Topological Inductive Density Threshold" resultbox equation, and "Cinquefoil Confinement Bound" resultbox). The KB leaves normalize these to roman `$l_{node}$`. Verbatim extraction forbids normalization — each occurrence must be reproduced as-is in the source.

**Note:** The source has internal inconsistency (roman ell at line 103). The KB must preserve the inconsistency verbatim.

**Fix:** In the two affected leaves, find all `$l_{node}$` occurrences that correspond to source lines 121, 131, 160. Change those specific instances to `$\ell_{node}$`. Do not globally replace — only the instances corresponding to those source lines.

---

### FINDING-ITA-02 (CRITICAL): vol4/ch3 `n-ave-derivation.md` truncated — missing sentences and ppm formula

**File:** `vol4/hardware-programs/ch3-hopf-01-chiral-verification/n-ave-derivation.md`

**Issue:** The "Predicted Shifts" paragraph ends after the second sentence. Three sentences present in source before the `\section{The Falsification Protocol}` heading are absent:
1. The six-measurement context statement
2. The mineral oil frequency range statement
3. The exact ppm formula: `$\Delta f/f = \alpha\,pq/(p+q)\,/\,(1 + \alpha\,pq/(p+q))$`

The ppm formula appears nowhere else in the ch3 leaf set.

**Fix:** Append the three missing sentences (verbatim translation from source) to the "Predicted Shifts" paragraph in the leaf.

---

### FINDING-ITA-03 (WARNING): CLAUDE.md INVARIANT-N2 wrong — incorrectly claims vol5 uses roman ell

**File:** `manuscript/ave-kb/CLAUDE.md`

**Issue:** INVARIANT-N2 states "all volumes except vol1 use roman ell $l_{node}$." This is incorrect: vol5 source uses script ell `\ell_{node}` throughout. The vol5 KB leaves are correct (they faithfully reproduce vol5 source). The INVARIANT documentation must be corrected to prevent future distillers from wrongly normalizing vol5 content.

**Fix:** Update INVARIANT-N2 to accurately state which volumes use which convention (vol1 = script, vol2 = mixed per source, vol5 = script, others = roman — verify exact per-volume convention before editing).

---

## Confirmed Clean

- **vol2/ch02 topological fractionalization** (`topological-fractionalization.md`): verbatim fidelity confirmed ✓
- **vol4/ch3 Key Results provenance**: entries trace to subdomain content ✓
- **vol5/molecular-foundations** (`derivation-chain-lattice-pitch.md`): verbatim fidelity confirmed ✓
- **common/translation-gravity** (`translation-gravity.md`): all 10 rows verified against source ✓
- **vol1/ch1 axioms** (`axiom-definitions.md`): axioms presented as axioms, no derived-as-given contamination ✓
- **tcolorbox rendering** (334 Resultbox instances, 21 other-environment instances): all correct ✓

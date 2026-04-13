# Burn-Down List — Phase 4 Iter-2

**Date:** 2026-04-03
**Source findings:** Structure Review Iter-2 (WARNING-1, WARNING-2); Accuracy Review Iter-2 (FINDING-002, FINDING-003)

---

## FINDING-002 RETRACTION

**FINDING-002 is a false alarm — retracted.**

Verification against source `01_llm_topology.tex` lines 19–46 confirms that all three subsections are present in the KB:

- Lines 19–26 (Axiom 1: SwiGLU Two-Port) → `vol8/foundations/ch1-llm-topology/swiglu-twoport.md` — verbatim content matches exactly, including the $A_j^2$ equation and the $w_{\text{down}}$ exclusion note.
- Lines 28–35 (Thermodynamic Emergence of $A_c$) → `vol8/foundations/ch1-llm-topology/ac-thermodynamic.md` — verbatim content matches exactly, including the $A_c^2 \equiv \overline{A^2}$ equation.
- Lines 37–44 (Axiom 3: Least Reflected Action) → `vol8/foundations/ch1-llm-topology/axiom3-pruning.md` — verbatim content matches exactly, including $\Gamma_{\text{prune}}$ formula and the $|\Gamma|^2 \ll 0.25$ constraint.

The accuracy reviewer correctly flagged the scope question and correctly noted these files might cover it. They do. No action required.

---

## FINDING-003 CONFIRMATION

**No action required.** Source inconsistency ($H_\infty$ = 69.32 vs 69.33 km/s/Mpc) is faithfully preserved in the KB. Future distillers and reviewers must not normalize these values — they reflect source-internal variation.

---

## Active Burn-Down Items

---

### ITEM-1 (WARNING-1): Six vol6 PATH-STABLE annotations missing source volume

**Priority:** Warning — INVARIANT-S6 violation across six leaves.

**Volume identification:** All six labels (`sec:abcd_cascade`, `sec:K_derivation`, `sec:operating_regimes`, `sec:pn_junction`, `sec:semiconductor_nuclear`, `sec:d_derivation`) are defined in `vol_6_periodic_table/chapters/01_computational.tex` and are `\ref`-called exclusively from within vol6 source files (`16_silicon.tex`, `02_chemistry.tex`, `00_introduction.tex`). No other volume references any of these labels. The referencing volume is **vol6** for all six.

**Files and changes:**

**File 1:** `ave-kb/vol6/framework/computational-mass-defect/abcd-transfer-matrix.md` line 3

- Current: `<!-- path-stable: referenced as sec:abcd_cascade -->`
- Replace with: `<!-- path-stable: referenced from vol6 as sec:abcd_cascade -->`

**File 2:** `ave-kb/vol6/framework/computational-mass-defect/mutual-coupling-constant.md` line 3

- Current: `<!-- path-stable: referenced as sec:K_derivation -->`
- Replace with: `<!-- path-stable: referenced from vol6 as sec:K_derivation -->`

**File 3:** `ave-kb/vol6/framework/computational-mass-defect/operating-regimes.md` line 3

- Current: `<!-- path-stable: referenced as sec:operating_regimes -->`
- Replace with: `<!-- path-stable: referenced from vol6 as sec:operating_regimes -->`

**File 4:** `ave-kb/vol6/framework/computational-mass-defect/pn-junction-coupling.md` line 3

- Current: `<!-- path-stable: referenced as sec:pn_junction -->`
- Replace with: `<!-- path-stable: referenced from vol6 as sec:pn_junction -->`

**File 5:** `ave-kb/vol6/framework/computational-mass-defect/semiconductor-nuclear-analysis.md` line 3

- Current: `<!-- path-stable: referenced as sec:semiconductor_nuclear -->`
- Replace with: `<!-- path-stable: referenced from vol6 as sec:semiconductor_nuclear -->`

**File 6:** `ave-kb/vol6/framework/computational-mass-defect/nucleon-spacing-derivation.md` line 3

- Current: `<!-- path-stable: referenced as sec:d_derivation -->`
- Replace with: `<!-- path-stable: referenced from vol6 as sec:d_derivation -->`

**Structural type:** Addendum — annotation text only, no structural changes.

---

### ITEM-2 (WARNING-2): vol8 ch1 and vol8 top-level Key Results both claim Z-inversion as primary result of different leaves

**Priority:** Warning — ambiguous routing signal; an agent reading either index cannot determine which leaf is the canonical derivation.

**Analysis:** The content in the two leaves is substantively different:
- `llm-topology-intro.md` presents the Z-inversion as part of the chapter opening frame (lines 5–17 of source), introducing the contrast alongside the saturation operator $S(r)$.
- `inversion-split.md` (ch2) contains the full structural decomposition: a comparison table across biological vs virtual properties (hardware/software/training/inference dimensions), which is the detailed derivation establishing *why* the inversion holds.

The ch1 Key Results row should describe the framing role; the vol8 top-level row should describe the full derivation.

**Files and changes:**

**File:** `ave-kb/vol8/foundations/ch1-llm-topology/index.md` line 11

- Current: `| Z-A inversion: biological $Z \propto 1/A$ vs virtual $Z \propto A$; universal saturation $S(r) = \sqrt{1-(A/A_c)^2}$ | [LLM Topology Introduction](llm-topology-intro.md) |`
- Replace with: `| Z-A inversion introduced: biological $Z \propto 1/A$ vs virtual $Z \propto A$; saturation $S(r) = \sqrt{1-(A/A_c)^2}$ (framing; full derivation in Ch.2) | [LLM Topology Introduction](llm-topology-intro.md) |`

**File:** `ave-kb/vol8/index.md` line 14

- Current: `| Virtual $Z \propto A$ vs biological $Z \propto 1/A$: the hardware/software isomorphism inversion | [Inversion Split](foundations/ch2-hw-sw-inversion/inversion-split.md) |`
- Replace with: `| Hardware/software isomorphism inversion derivation: biological vs virtual property table; $Z \propto A$ established from first principles | [Inversion Split](foundations/ch2-hw-sw-inversion/inversion-split.md) |`

**Structural type:** Addendum — Key Results table text only, no structural changes.

---

## Summary

| Item | Type | Files | Action |
|---|---|---|---|
| FINDING-002 | Retracted — false alarm | — | None |
| FINDING-003 | Confirmed no-action | — | None |
| ITEM-1 (WARNING-1) | Addendum | 6 vol6 leaves | Add `from vol6` to PATH-STABLE annotation on each |
| ITEM-2 (WARNING-2) | Addendum | vol8/ch1/index.md, vol8/index.md | Differentiate Z-inversion row text to distinguish framing (ch1) from derivation (ch2) |

Total files to edit: 8. No structural changes required. No new files.

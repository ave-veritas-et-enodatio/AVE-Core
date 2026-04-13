# KB Structure Review — Phase 4 Iteration 2

**Date:** 2026-04-03
**Scope:** `ave-kb/` — 814 files across 8 volumes plus common/
**Purpose:** Verify iter-1 fixes applied correctly; adversarial scan for surviving and new issues.

---

## Structure Review Summary

All seven Critical and Warning findings from iter-1 have been applied correctly at their stated targets. The most critical surviving issue is that six `vol6/framework/computational-mass-defect/` PATH-STABLE leaves carry `<!-- path-stable: referenced as sec:X -->` — the source volume is omitted from all six, and the format was not corrected in the iter-1 fix pass (only three vol4 leaves were in scope for W-1; the vol6 cluster was not on the iter-1 radar). One new structural issue was introduced by the C-4 fix: the `vol8/ch1` Key Results table now claims the Z-proportionality inversion result for `llm-topology-intro.md`, but the vol8-level Key Results table attributes that same result to `ch2/inversion-split.md` — creating an ambiguous routing signal for agents navigating from either level. No orphaned documents were created by the iter-1 fixes.

---

## Findings

---

### WARNING-1 (SURVIVING FROM ITER-1 W-1): Six vol6 PATH-STABLE leaves missing source volume

**Issue:** Six leaves in `vol6/framework/computational-mass-defect/` carry PATH-STABLE annotations in the form `<!-- path-stable: referenced as sec:X -->` without specifying the referencing volume. INVARIANT-S6 requires the form `referenced from {vol} as {label}`. These six leaves were not in the iter-1 W-1 fix scope (which targeted only the three vol4 falsification leaves).

**Location:**
- `vol6/framework/computational-mass-defect/abcd-transfer-matrix.md` line 3: `<!-- path-stable: referenced as sec:abcd_cascade -->`
- `vol6/framework/computational-mass-defect/mutual-coupling-constant.md` line 3: `<!-- path-stable: referenced as sec:K_derivation -->`
- `vol6/framework/computational-mass-defect/operating-regimes.md` line 3: `<!-- path-stable: referenced as sec:operating_regimes -->`
- `vol6/framework/computational-mass-defect/pn-junction-coupling.md` line 3: `<!-- path-stable: referenced as sec:pn_junction -->`
- `vol6/framework/computational-mass-defect/semiconductor-nuclear-analysis.md` line 3: `<!-- path-stable: referenced as sec:semiconductor_nuclear -->`
- `vol6/framework/computational-mass-defect/nucleon-spacing-derivation.md` line 3: `<!-- path-stable: referenced as sec:d_derivation -->`

**Avoidance requirement:** Every PATH-STABLE annotation must include the referencing volume.

---

### WARNING-2 (NEW): vol8/ch1 Key Results Z-inversion row duplicates primary result attributed to vol8/ch2

**Issue:** `vol8/foundations/ch1-llm-topology/index.md` Key Results (line 11) attributes "Z-A inversion: biological $Z \propto 1/A$ vs virtual $Z \propto A$; universal saturation $S(r) = \sqrt{1-(A/A_c)^2}$" to `llm-topology-intro.md`. `vol8/index.md` Key Results (line 14) attributes "Virtual $Z \propto A$ vs biological $Z \propto 1/A$: the hardware/software isomorphism inversion" to `foundations/ch2-hw-sw-inversion/inversion-split.md`. Both tables claim the Z-inversion as the primary result of different leaves.

**Location:**
- `vol8/foundations/ch1-llm-topology/index.md` lines 10–11
- `vol8/index.md` line 14

**Navigation impact:** Agent has no structural signal to determine which leaf is the canonical derivation vs. introduction.

**Avoidance requirement:** Differentiate the two rows textually so the routing signal is unambiguous. The ch1 entry should describe the framing/introduction; the ch2 entry should describe the full derivation.

---

## Confirmed Clean (All Iter-1 Fixes Verified)

- **C-1**: Protein pointer leaves → `vol5/common/` with working relative links. ✓
- **C-2**: `vol4/index.md` has fully populated Key Results table (6 domains). ✓
- **C-3**: `vol2/app-c-derivations/index.md` line 2 = `<!-- leaf: verbatim -->`. ✓
- **C-4**: `llm-topology-intro.md` exists, correct content, line 2 = `<!-- leaf: verbatim -->`, uplink = `index.md`, in Derivations table. ✓
- **C-5**: `mond-hoop-stress.md` lines 43–50 contain Dark Sector Comparison table. ✓
- **W-1**: Three vol4 falsification PATH-STABLE annotations = `referenced from vol3 as sec:X`. ✓
- **W-2/W-4**: `vol8/NOTES.md` line 2 = `<!-- leaf: verbatim -->`; Appendix + NOTES in Derivations table. ✓
- **W-3**: Zero instances of `**[Result]**` found anywhere in KB. ✓
- **W-5**: No bare LaTeX labels in any See-also ref across entire KB. ✓
- **N-1 through N-4**: All confirmed. ✓
- **Bonus (App A non-protein)**: Working `→ Primary:` links in all 6 files. ✓
- **Bonus (vol8/ch1 uplinks)**: `ac-thermodynamic.md` and `llm-topology-intro.md` use `index.md`. ✓
- **Orphan scan**: `llm-topology-intro.md` (only new file) is in parent Derivations table. ✓

---

## Out of Scope

- Content accuracy — structure and navigation only.
- Which volume cross-references the six vol6 PATH-STABLE leaves.
- Whether `llm-topology-intro.md` and `inversion-split.md` differ in substantive content.

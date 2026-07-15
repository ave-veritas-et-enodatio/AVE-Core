# THE 1/4 MAP — Quarter-Power Families, the One-Contour Test, and the Knee Ladder

> **Map-and-document research doc. Landed 2026-07-14 (Grant-authorized: "do the sweep
> regardless and paint the full circuit/picture/map and document").** Synthesized from a
> four-modality corpus sweep (prose/KB, adjudication-trail, git-history, operative-code);
> **every file:line anchor re-verified two-method against `AVE-Core @ bb58727f`** before
> landing. Anchors that failed re-verification were dropped or corrected — see the
> `## Re-verification corrections` appendix at the end. All numerics recomputed this
> session (CODATA `ALPHA = 7.2973525693e-3`; `2*ALPHA = 0.0145947051386`).
>
> **Base note:** branched from `bb58727f` (the synthesis's verification HEAD); `origin/main`
> had advanced to `c50a997f` when this landed — line-anchors are pinned to `bb58727f`.
>
> **Epistemic posture:** report-only map. The `r_knee` VALUE stays echo-classified per the
> knee-NOTE's own ruling (it rides the α-echo). No new KB claim; KB candidacy is routed to
> the auditor lane. All defect rows are **FLAGGED-NOT-FIXED** (flag-don't-fix): the hygiene
> burn-down is a QUEUED follow-on, not this doc's work.

## Kernel and contour conventions (the single largest source of historical churn)

- **Kernel:** `S(A) = (1 − A²)^{1/2}` (Op2, `src/ave/core/universal_operators.py:112`).
  **"Half-in-S = quarter-in-A²":** `√S = (1−A²)^{1/4}` but `S^{1/4} = (1−A²)^{1/8}`. The
  eighth-power `S^{1/4}` is the historical DEFECT (Family E); the quarter-power `√S =
  (1−A²)^{1/4}` is the physical register.
- **Knee contour:** `A² = 2α` (deficit `ΔS = 1−S = α + α²/2 ≈ α`). Coordinate authority
  `src/ave/core/chiral_lattice_v10.py:30` (`A_YIELD_SQ = 2.0 * float(ALPHA)`),
  `src/ave/core/constants.py:525` (`R_I = np.sqrt(2.0 * ALPHA)`). Ruled the **deficit knee /
  LOADING BC**, not the wall (`_orchestration/2026-07-10_rulings-docket.md:540,556`; Grant
  "accept!" :553).

---

## 1. MASTER TABLE — the nine families

<!-- filled per-commit -->

## 2. THE ONE-CONTOUR TEST

<!-- filled per-commit -->

## 3. c_shear ADJUDICATION INPUT (present-both, no ruling)

<!-- filled per-commit -->

## 4. THE CIRCUIT MAP — radial ladder with the quarter-power identity overlaid

<!-- filled per-commit -->

## 5. PHASE-SPACE READING (WALK-LEVEL)

<!-- filled per-commit -->

## 6. BIQUATERNION BINDING

<!-- filled per-commit -->

## 7. DISCRIMINATION CHECK (symmetric standard)

<!-- filled per-commit -->

## 8. GRANT'S OPEN QUESTIONS (ranked)

<!-- filled per-commit -->

## Re-verification corrections

<!-- filled per-commit -->

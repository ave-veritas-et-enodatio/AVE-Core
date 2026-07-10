# Tethered-pivot RE-RUN (x34b) — the control-subtracted detector FROZEN A PRIORI · does the anchored (2,3) traversal MODE-LOCK, read on ONE frozen axis?

**Status:** **FROZEN PRE-REG.** Frozen BEFORE any driver change. This document is committed and
PUSHED before the x34b driver exists — the freeze is claimed by commit ordering (the standing rule).
**Date:** 2026-07-10 · **Test id:** x34b (re-run of x34 / PR #612).
**Sector header (mandatory):** MODE = driven traversal on the anchored (2,3); REGIME = sub-yield,
lossless-reactive (the clamp is a lossy-Dirichlet Γ=−1 wall, removed-norm budget tracked, never
pumping); SECTOR = T2 / Cosserat winding host `b_ω` vs the A1 mass-carrier `a_A1` (the two Clifford
global phases). PHASE-STATE = seeded already-formed electron (SEED never FORM), conservative evolver.
**Class:** CONSISTENCY. A LOCK would deliver a DERIVED protection mechanism (boundary-condition
quantization) for the IMPORTED (2,3) SELECTION; a TRACK banks the pivot picture negative next to #417.
The observable is a pure `arg()` ratio — α-free / Q=137 EMPTY / mass=A1 (#260) UNTOUCHED / the (2,3)
SELECTION stays IMPORTED either way. Not an emergence claim.
**Base:** `analysis/x34b-pivot-rerun` off main `93e928ac`.

---

## §0 WHY THE RE-RUN — the #612 outcome this test must convert to a single-axis bank

`research/2026-07-09_tethered-pivot-mode-locking_result.md` (x34, PR #612 MERGED) returned a
**KEEP-BOTH two-axis** verdict:

- **Frozen prereg-§6 ABSOLUTE detector → PARTIAL.** `staircase_fraction = 0.4286` **EQUAL** to the
  free (clamp-off) control's own `0.4286` — the absolute metric is confounded by a sweep-saturation
  artifact common to anchored AND free (the coupled tank's ρ(ω_s) saturates near 1.0 at high ω_s), so
  it fails BOTH the LOCK bar (≥0.5) and the TRACK bar (<0.2) → unresolved PARTIAL.
- **Post-hoc CONTROL-SUBTRACTED axis → TRACK.** `excess_staircase = 0.0714` (< 0.2) with
  `track_R² = 0.9799` (≥ 0.9) — the anchor adds essentially no plateaus the free control lacks.

The #612 verdict therefore rested on a **post-hoc** amended axis. The #612 adversarial review's
**consequence 2** prescribed exactly this re-run: **freeze the control-subtracted detector as THE
preregistered rule** and **extend validation with the saturating-control plant**, so the negative is
banked honestly on ONE axis chosen a priori — with the detector's known blind spot disclosed UP FRONT
and designed around, not discovered after the fact.

This re-run changes NOTHING about the physics, the seed, the evolver, the clamp, or the read. The ONLY
change vs #612 is **methodological ordering**: the excess (control-subtracted) detector is frozen as
the primary rule BEFORE the run, its saturation-zone bias is stated a priori, and the sweep is designed
so the banked verdict does not rest on the detector's blind zone. Substrate-native / A46 phase-space
coordinate discipline is INHERITED from #612 (both Grant gut-checks ruled; read is in phase-space
Clifford global-phase coordinates) — no new numerical physics is introduced, so no fresh substrate walk
is required; the walk is inherited and re-cited in §4.

---

## §1 THE FROZEN PRIMARY DETECTOR (the whole point — ONE axis, chosen a priori)

**PRIMARY = the CONTROL-SUBTRACTED EXCESS axis** (the #612 amended thresholds, now frozen a priori,
with NO preferred outcome):

- **LOCK** ⇔ `excess_staircase ≥ 0.4` AND `excess_jumps ≥ 1`.
- **TRACK** ⇔ `track_R² ≥ 0.9` AND `excess_staircase < 0.2`.
- **PARTIAL** otherwise (report per-signature).
- **INCONCLUSIVE** (Rule 11) if a validation gate fails (dead actuator / pumping clamp / detector
  cannot separate the planted controls / Nyquist-unresolved). Report; re-scope; NO rescue.

where (verbatim from the merged solver `lock_detector`, `tethered_pivot_winding.py`):
- `excess_staircase` = fraction of adjacent sweep intervals where the **anchored** ρ is flat
  (`|Δρ_anch| < 0.03`) AND the **free control** ρ is NOT flat — i.e. the plateaus the anchor ADDS that
  the free control lacks (baseline-subtracted, so the shared saturation artifact is removed);
- `excess_jumps` = intervals where anchored jumps (`|Δρ_anch| > 0.15`) and the free control does not;
- `track_R²` = R² of ρ_anchored vs ρ_free over the sweep.

**LABEL PROVENANCE (flag-don't-fix, so no auditor conflates the two docs).** In the merged solver the
excess axis is returned under the key `amended_verdict` and the absolute axis under `frozen_verdict` —
those names are HISTORICAL to #612 (where the ABSOLUTE axis was the prereg-frozen one). In **x34b the
roles are deliberately inverted**: the **x34b-frozen PRIMARY rule is the EXCESS axis** (solver key
`amended_verdict`); the ABSOLUTE axis (solver key `frozen_verdict`) is demoted to a **complementary
disclosure read** used only in the saturation zone (§2c). The x34b driver re-labels explicitly; the
solver is NOT redefined-in-place (KEEP-BOTH — the #612 two-axis output is preserved intact).

---

## §2 MANDATORY VALIDATION GATES (frozen WITH the detector — the verdict is void without all three)

**(a) Tracking-zone planted LOCK/TRACK separation.** The excess detector must read a PLANTED genuine
staircase (rational plateaus + a discrete jump) as **LOCK** and a PLANTED linear (tracking) rotation
number as **TRACK**, in the tracking zone (`validate_lock_detector` → `planted_locked_verdict==LOCK`,
`planted_tracking_verdict==TRACK`, `ok==True`). If it cannot separate the two synthetic controls the
detector is broken → HALT.

**(b) Saturation-zone planted-lock disclosure — the bias direction is stated UP FRONT.** The excess
axis is **LOCK-SUPPRESSING where the free control saturates**: a genuine rational plateau that
coincides with a flat free control has `excess_staircase → 0` (the plateau is subtracted out with the
baseline). The prereg states this a priori: **in the saturation zone the excess detector is BIASED
toward the TRACK / negative read.** Certified by a planted gate — a genuine lock placed entirely in the
free-control saturation zone must read **LOCK on the complementary absolute axis** yet **NOT-LOCK on the
frozen excess axis** (`validate_lock_detector` → `saturation_zone.lock_suppressed_by_excess == True`).
**Verdict-scoping consequence (frozen):** a TRACK verdict is **bankable only where the detector can see
a lock — i.e. the NON-saturated zone.** A TRACK read inside the saturation zone alone is NOT bankable.

**(c) NON-SATURATED-ZONE restriction — the banked verdict does not rest on the blind zone.** The
banked x34b verdict is the excess-axis verdict computed on the **non-saturated window** (ω_s below the
free-control saturation onset), reported ALONGSIDE the full-sweep excess verdict AND a complementary
absolute-axis read in the saturation zone (the disclosure). **Saturation-onset rule (frozen a priori):**
using the clamp-off free control ρ_free(ω_s) on the ascending sweep grid, with flat-mask
`f_flat[i] = |Δρ_free[i]| < 0.03`, the saturation-onset interval index `i_sat` = the smallest `i` such
that `f_flat[j]` is True for **every** interval `j ≥ i` (the onset of the terminal flat plateau). The
NON-saturated window = sweep points with interval index `< i_sat` (i.e. ω_s up to and including the
onset point). If no terminal flat run exists (`i_sat = n`, the free control never saturates within the
grid) the full sweep IS the non-saturated window (no blind zone to exclude — conservative). The
**banked verdict** = the excess-axis LOCK/TRACK/PARTIAL applied to the non-saturated window; the
full-sweep excess verdict and the saturation-zone absolute read are reported as companions, not as the
bank.

---

## §3 THE SWEEP (frozen) — fresh grid primary + #612 reproduction leg

- **PRIMARY (fresh) grid:** ω_b = 1 fixed, ω_s ∈ [0.70, 1.40] at step **0.025** → **29 points** (a
  grid REFINEMENT of #612's 15-point step-0.05 grid; the #612 points are a subset, so per-point
  reproduction is checkable and the verdict is shown stable under grid refinement — not tuned to the
  exact #612 grid). Branch = capacitive (the primary μ-quadrature); free control = clamp OFF.
- **REPRODUCTION leg:** the exact #612 config (`TetheredPivotConfig()` default: N=20, 500 steps,
  15-point step-0.05 grid) run through the full frozen protocol; the excess-axis metrics must
  reproduce the #612 marks (§7).
- The solver `build_seeded_sim` is deterministic (no RNG); "fresh" = an independent grid draw, not a
  fresh random seed. The gates (dead-actuator, energy ledger) are config-level and grid-independent, so
  the reproduction leg's gate reads apply to the fresh leg (stated, not silently assumed).

---

## §4 THE READ (frozen — reused VERBATIM from #612 / #417; A46-faithful)

Toroidal `φ(t) = arg(Σ a_A1)` ("2"); poloidal `ψ(t) = arg(Σ b_ω)` ("3"); traversal rotation number
`ρ = (φ-winding-rate)/(ψ-winding-rate)` read by the **slope estimator** (least-squares winding rate,
window-noise-immune — the pre-reg-§4 load-bearing "DETUNING RESPONSE of ρ" discriminator; the same
instrument #612 used post-repair). Two-method endpoint read (unwrap + circulation) reported with the F4
caveat honored (same wrapped-increment estimator; NOT the discriminator). **A46 phase-space coordinate
discipline:** the corpus claim is a phase-space TRAVERSAL rotation number and the read is in matching
phase-space Clifford global-phase coordinates; the clamp acts on the real-space field but the VERDICT is
read in phase-space and the CONTROL (clamp off) reproduces #417's phase-space tracking values.

---

## §5 GATES (frozen — reused verbatim from the merged solver)

- **dead-actuator:** the pinned quadrature's variance over the anchor set `M` COLLAPSES vs unclamped
  (`var_clamped/var_unclamped < 0.05`) for BOTH branches — the clamp demonstrably constrains (live
  actuator). A clamp that does not collapse the variance → INCONCLUSIVE.
- **energy ledger:** clamp OFF conserves the joint norm to #417 standard (`< 1e-6`); clamp ON is
  monotone NON-PUMPING (`max_t E(t) ≤ E(0)·(1+1e-9)`) with the removed-norm budget reported. A clamp
  that PUMPS → INCONCLUSIVE (a pumped lock is an artifact).
- **validate-on-known:** §2(a) + §2(b) above.

## §6 BRANCHES (no preferred outcome — substrate adjudicates)

- **LOCK:** the (2,3) gains a DERIVED protection mechanism (BC quantization); the SELECTION stays
  IMPORTED (FORM derived, VALUE still adopted-by-geometry). Register note: the #260 selector is a live
  engine observable if the termination flip also fires.
- **TRACK:** the pivot picture DIES; banked next to #417. The carrier-set global-phase mechanism is
  ROBUST to anchoring. (This is the outcome the #612 excess axis leaned to; the re-run tests whether it
  banks cleanly on the a-priori-frozen single axis, scoped to the non-saturated zone.)
- **PARTIAL:** report per-signature; name what held and what did not.
- **INCONCLUSIVE** (Rule 11): a gate fails; report, re-scope, NO rescue.

## §7 ANALYTIC EXPECTATIONS (frozen — the reproduction marks + the control)

- **CONTROL (clamp OFF) MUST reproduce #417** (else the harness is broken → HALT): ρ(1:1)≈1,
  ρ(2:3)≈0.65, ρ(3:2)≈1.55, ρ(1:2)≈0.48; ρ_free(ω_s) a CONTINUOUS curve tracking ω_b/ω_s that saturates
  near 1.0 at high ω_s.
- **REPRODUCTION marks (from #612 `..._result.md` §3):** on the #612 config the excess axis gives
  `excess_staircase ≈ 0.0714`, `excess_jumps = 0`, `track_R² ≈ 0.9799`, and the ABSOLUTE axis gives
  `staircase_fraction ≈ 0.4286` == `free_staircase_fraction ≈ 0.4286`. Signature-2 excess width ≈ 0.004
  (not seen), Signature-3 termination flips 0/4. The reproduction leg must hit these to ~sig-fig.
- **Expected direction (NOT preferred — stated for falsifiability):** if the pivot picture is dead as
  #417 found, the frozen excess axis reads **TRACK** on the non-saturated window (excess_staircase < 0.2,
  track_R² ≥ 0.9). If the anchor genuinely mode-locks, the excess axis reads **LOCK** (excess_staircase
  ≥ 0.4, excess_jumps ≥ 1) — the detector CAN see this in the tracking zone (§2a proves it), so a TRACK
  read there is a real negative, not a blind one.

## §8 PLANTED-VIOLATION PROOFS (frozen requirement — every gate must be shown to CATCH a violation)

Each gate ships a planted-violation proof in the x34b driver + test:
- **detector separation (§2a):** planted staircase → LOCK; planted line → TRACK; planted flat-shared
  (anchored == free, both flat) → the excess axis returns TRACK (NOT LOCK) — the shared-flatness case
  the control-blind detector mis-binned.
- **saturation disclosure (§2b):** planted lock in the saturation zone → absolute LOCK, excess NOT-LOCK,
  `lock_suppressed_by_excess == True`.
- **dead-actuator:** a degenerate clamp (`branch="off"` compared to itself) → `actuator_live == False`
  (the gate catches a dead actuator).
- **energy:** a planted PUMPING energy trace (monotone-growing E) → the non-pumping criterion returns
  False (the gate catches a pump).

## §9 REUSE (Rule 14) — NO fork-copy

Reuse VERBATIM from the merged `src/ave/solvers/tethered_pivot_winding.py`: `TetheredPivotConfig`,
`trace_orbit_clamped`, `detuning_sweep`, `lock_detector`, `hysteresis_ramp`, `termination_flip`,
`dead_actuator_gate`, `energy_ledger`, `validate_lock_detector`, `run_tethered_pivot`. NEW = a THIN
x34b driver (`tethered_pivot_x34b.py`) that: (i) freezes the excess axis as primary + re-labels;
(ii) applies the saturation-onset non-saturated-zone restriction (§2c); (iii) runs the fresh-grid
primary + the #612 reproduction leg; (iv) collects the planted-violation proofs; (v) emits the JSON +
WHITE figure. No new engine, no new physics.

## §10 CONSEQUENCE (flagged as follow-on — NOT landed in this session)

If the frozen excess axis banks **TRACK** cleanly on the non-saturated window:
- the orchestrator miss-ledger for tethered-pivot BC-quantization increments **0-for-6 → 0-for-7**
  (Grant-gated skill touches are queued SEPARATELY — not edited here);
- the W5-iii retraction caveat in
  `research/2026-07-09_fast-sector-settling-boundary-conditions_walked-framing.md:159` can be upgraded
  from **"unsupported-at-prereg-strength"** to **"banked negative"**.

Both are flagged as follow-ons for the auditor/orchestrator to land; this session does NOT edit any
skill file or the settling note.

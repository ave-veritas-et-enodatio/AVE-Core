# Tethered-pivot RE-RUN (x34b) — RESULT: **TRACK** on the CONTROL-SUBTRACTED excess detector FROZEN A PRIORI · the pivot picture banks a clean negative on ONE axis

**Status:** **RESULT (committed).** Frozen-pre-reg re-run per
`research/2026-07-10_tethered-pivot-rerun_prereg.md` — detector frozen and PUSHED (SHA
`6dbf6b26`) BEFORE the driver existed.
**Date:** 2026-07-10 · **Test id:** x34b (re-run of x34 / PR #612).
**Sector header:** MODE = driven traversal on the anchored (2,3); REGIME = sub-yield
lossless-reactive (lossy-Dirichlet Γ=−1 wall, removed-norm 13.8% tracked, never pumping);
SECTOR = T2/Cosserat winding host `b_ω` vs the A1 mass-carrier `a_A1` (the two Clifford
global phases). PHASE-STATE = seeded already-formed electron (SEED never FORM).
**Module:** `src/ave/solvers/tethered_pivot_x34b.py` (thin driver) over the merged
`src/ave/solvers/tethered_pivot_winding.py` (Rule 14 — NO fork-copy). **Test:**
`src/tests/test_tethered_pivot_x34b.py`.
**Class:** CONSISTENCY. A LOCK would have delivered a DERIVED protection mechanism (BC
quantization) for the IMPORTED (2,3) SELECTION; the TRACK banks the pivot picture negative
next to #417. α-free / Q=137 EMPTY / mass=A1 (#260) UNTOUCHED / (2,3) SELECTION stays IMPORTED.

---

## 0. HEADLINE

> **VERDICT: TRACK — banked on ONE a-priori-frozen axis (the control-subtracted excess
> detector), scoped to the non-saturated window.** This is the x34 re-run the #612
> adversarial-review consequence 2 prescribed: the KEEP-BOTH two-axis dispute is gone — the
> excess detector was frozen as THE primary rule BEFORE the run, its saturation-zone blindness
> was disclosed UP FRONT, and the sweep was designed so the banked verdict does not rest on the
> blind zone.
>
> **The single frozen axis (prereg §1):** LOCK ⇔ `excess_staircase ≥ 0.4 ∧ excess_jumps ≥ 1`;
> TRACK ⇔ `track_R² ≥ 0.9 ∧ excess_staircase < 0.2`. On the fresh 29-point refined grid, banked
> on the **non-saturated window (24 of 29 points, ω_s ≤ 1.275)**: **excess_staircase = 0.0435**
> (< 0.2), **track_R² = 0.9901** (≥ 0.9), **excess_jumps = 0** → **TRACK.** The anchor adds
> essentially no rotation-number plateaus the free (clamp-off) control lacks; the anchored ρ
> follows the carrier detuning knob just as #417's free orbit did. **The pivot picture — that a
> wall-anchored (2,3) traversal would BC-quantize the integers into knobless mode indices —
> reads NEGATIVE, banked next to #417.**
>
> **Reproduction leg (the #612 config, exact):** every #612 excess-axis mark reproduced to
> Δ = 0.0000 — `excess_staircase 0.0714`, `excess_jumps 0`, `track_R² 0.9799`, and the absolute
> `staircase_fraction 0.4286 == free 0.4286`. The re-run is the same physics; only the detector
> freeze-ordering changed.
>
> **All gates hold and all planted-violation proofs fire:** control (clamp OFF) reproduces #417
> (2:3→0.650, 3:2→1.532, 1:2→0.478); dead-actuator live both branches; energy OFF conserved
> (drift 9.1×10⁻¹⁰), ON monotone non-pumping (removed-norm 13.8%); detector separates a planted
> staircase (LOCK) from a planted line (TRACK); the saturation-zone plant is seen by the
> absolute axis (LOCK) but suppressed by the frozen excess axis (the disclosed asymmetry);
> `branch="off"` is caught as a dead actuator; a planted energy pump is caught. Supporting
> nulls fire clean: **no excess hysteresis, no cap↔mag termination flip.**

---

## 1. WHAT CHANGED FROM #612 — nothing physical, only the detector freeze-ordering

x34 (#612) returned a **KEEP-BOTH two-axis** verdict — frozen-§6 ABSOLUTE detector = PARTIAL
(confounded by a sweep-saturation artifact common to anchored AND free), post-hoc
control-subtracted axis = TRACK — because the control-subtracted detector was formulated
*after* the freeze. The #612 verdict therefore rested on a post-hoc axis. The adversarial-review
consequence 2 prescribed this re-run: **freeze the control-subtracted detector as THE
preregistered rule** and **extend validation with the saturating-control plant**.

x34b does exactly that and nothing else: same seed, same conservative evolver, same clamp, same
phase-space Clifford global-phase read, same slope-rate rotation-number estimator. The ONLY
change is methodological — the excess axis is the a-priori primary, its bias is disclosed before
the run, and the verdict is scoped to the zone where the detector can see a lock. The physics
result is therefore identical to #612's amended-axis read; what the re-run buys is that the
**negative is now banked on an axis chosen a priori, not one reached for after seeing the
confound.**

**LABEL PROVENANCE (flag-don't-fix — so no auditor conflates the two docs).** The merged solver
returns the excess axis under the key `amended_verdict` and the absolute axis under
`frozen_verdict` — HISTORICAL to #612 (where the ABSOLUTE axis was the prereg-frozen one). In
x34b the roles are **deliberately inverted**: the x34b-frozen PRIMARY is the EXCESS axis (solver
key `amended_verdict`); the ABSOLUTE axis (solver key `frozen_verdict`) is a **complementary
disclosure read** used only in the saturation zone. The merged solver's two-axis output is
preserved intact (KEEP-BOTH — not redefined-in-place); the driver only re-labels which axis is
banked.

---

## 2. THE NUMBERS

### 2.1 Reproduction leg (#612 config: N=20, 500 steps, 15-pt step-0.05 grid)

| Mark | x34b | x34 (#612) | Δ |
|---|---|---|---|
| excess_staircase | **0.0714** | 0.0714 | 0.0000 |
| excess_jumps | 0 | 0 | 0 |
| track_R² | **0.9799** | 0.9799 | 0.0000 |
| staircase_fraction (absolute) | 0.4286 | 0.4286 | 0.0000 |
| free_staircase_fraction | 0.4286 | 0.4286 | 0.0000 |

Deterministic solver, exact reproduction. Excess-axis TRACK, absolute-axis PARTIAL — the #612
two-axis picture, reproduced.

### 2.2 Fresh leg (29-pt refined grid, step 0.025) — the FROZEN excess axis, single-axis bank

| Read | Value | Note |
|---|---|---|
| saturation onset ω_s (free control) | **1.275** (i_sat = 23) | terminal flat plateau of ρ_free |
| non-saturated window | **24 / 29 pts** (ω_s ≤ 1.275) | where the excess axis CAN see a lock |
| **BANKED excess_staircase** (non-sat window) | **0.0435** | < 0.2 ⇒ TRACK |
| **BANKED track_R²** (non-sat window) | **0.9901** | ≥ 0.9 ⇒ TRACK |
| BANKED excess_jumps | 0 | — |
| full-sweep excess verdict (companion) | **TRACK** | excess_staircase 0.0357 |
| control (clamp-off) 2:3 / 3:2 / 1:2 | 0.650 / 1.532 / 0.478 | reproduces #417 ✓ |
| anchored 2:3 / 3:2 / 1:2 | 0.895 / 1.546 / 0.809 | weak lossy pull at 2:3, 1:2 (§4, as #612) |

### 2.3 Gates and nulls (all pass)

| Gate / null | Result |
|---|---|
| validate-on-known (tracking-zone separation) | PASS (planted staircase→LOCK, line→TRACK) |
| dead-actuator (cap / mag) | live / live (var-ratio collapses) |
| energy OFF conserved | drift 9.1×10⁻¹⁰ (#417 standard) |
| energy ON non-pumping / removed-norm | non-pumping / 0.138 (lossy-Dirichlet) |
| Signature-2 excess hysteresis | not seen (clean null) |
| Signature-3 cap↔mag termination flip | 0/4 (clean #260 null) |
| planted-violation proofs (all 4 gates) | all catch their planted violation |

---

## 3. A FLAG (surfaced, not resolved) — the absolute axis is GRID-FRAGILE; the excess axis is GRID-STABLE

This re-run exposes, incidentally, a concrete reason the excess axis is the right detector to
freeze — and it is surfaced here per flag-don't-fix rather than buried:

- On the **15-pt** #612 grid the ABSOLUTE `staircase_fraction` = **0.4286 → PARTIAL** (fails the
  ≥0.5 LOCK bar).
- On the **29-pt refined** grid the ABSOLUTE `staircase_fraction` = **0.5714 → LOCK** — a
  **spurious flip PARTIAL→LOCK from grid refinement alone, with no physics change.** The
  mechanism: halving the ω_s step halves the per-interval |Δρ|, so more intervals fall below the
  fixed flat-tolerance 0.03, inflating the absolute flat-fraction. Tellingly the free control's
  own absolute flat-fraction on the same grid is **0.6071 — even HIGHER than the anchored 0.5714**,
  so the absolute "LOCK" is entirely the shared saturation artifact (the anchor is *less* flat
  than its own control).
- The **excess** (control-subtracted) axis is **grid-STABLE: TRACK at 15-pt (0.0714 / 0.0357) and
  TRACK at 29-pt (0.0435 banked)** — because it measures only the plateaus the anchor adds *beyond*
  the free control, which grid refinement does not manufacture.

This is not a new lock; it is a demonstration that the absolute detector reports a grid-dependent
artifact, which is exactly why the a-priori freeze went to the excess axis. It is reported as the
**saturation-zone complementary disclosure read** in the JSON (`full_sweep_absolute_verdict =
LOCK`), explicitly labeled confounded — the banked verdict rests on the excess axis, never on it.

---

## 4. THE MECHANISM (single-mechanism explanation of the TRACK-direction, inherited from #417/#612)

The two Clifford-torus angles are the GLOBAL PHASES of the two coupled LC sectors (φ = arg Σ a_A1,
ψ = arg Σ b_ω). #417 established that under the unitary evolution these global phases precess at
their carrier frequencies, so ρ = (φ-rate)/(ψ-rate) = the carrier ratio, and ρ tracks the detuning
knob. A Γ=−1 Dirichlet wall pins one quadrature of `b_ω` on a measure-limited node-plane, but the
**global-phase winding of a coherently-driven sector is set by its carrier**; a boundary condition
on a sub-region does not re-quantize that global winding — the freely-precessing bulk of the tube
dominates Σ b_ω. So ρ tracks ω_b:ω_s, anchored or not. **The same carrier-set-global-phase
mechanism as #417, now shown ROBUST to anchoring — one mechanism, both negatives.**

The one genuine anchor effect is a weak lossy-wall pull at the two ω_s > ω_b rational points
(2:3, 1:2), IDENTICAL at the capacitive and magnetic clamps and confounded with the lossy
Dirichlet wall (removes 13.8% of the norm) — a dissipation artifact, not a mode-lock (smooth, no
discrete plateau/jump; the fine sweep tracks at R² = 0.99 with zero excess jumps). Pre-named as a
confound in the prereg; it does not rescue the pivot picture.

---

## 5. WHAT THIS RETRACTS — AND WHAT IT DOES NOT (Rule 12 substitution-not-retraction)

**Retracts (preserve body, demote scope) — now at BANKED-NEGATIVE strength (not merely
unsupported-at-prereg-strength as #612 left it):** the W5 tethered-pivot proposal
(`research/2026-07-09_fast-sector-settling-boundary-conditions_walked-framing.md:159`, W5-iii)
that boundary-condition quantization — the anchored poloidal loop — would make the (2,3) integers
discrete, knobless BC mode indices so that #417's ratio-tracks-detuning kill "structurally cannot
fire." On the a-priori-frozen single axis, scoped to the zone where the detector can see a lock,
the anchored ρ tracks the carrier knob (track_R² 0.9901) with no excess plateaus (0.0435), no
excess hysteresis, and no termination flip. W5-iii is **banked negative** next to #417.

**Does NOT retract (independently grounded):** charge = Link(∂Ω, F) ∈ ℤ (static real-space linking
integer, separate coordinate); mass = A1 (#260); the (2,3) as a geometric Clifford-torus embedding
(the rigid template's static texture IS a (2,3), untouched by the anchor). What is null is that a
wall-anchored traversal PROMOTES it to a knobless dynamical mode index.

**Substitution-not-retraction discipline:** no successor hypothesis is refilled into the
tested-negative slot. A strictly-conservative (reflectionless) reflecting wall, or a SPATIAL
standing-mode-index read (distinct from the temporal global-phase traversal tested here and in
#417), would each be a NEW pre-reg with its own verification chain — not a refill here.

---

## 6. HONEST FLAGS / CAVEATS

1. **Saturation-zone blindness is disclosed and designed around, not discovered post-hoc.** The
   frozen excess axis is LOCK-suppressing where the free control saturates (a plateau coinciding
   with a flat free control has excess → 0; the planted-lock-in-saturation gate certifies this,
   `lock_suppressed_by_excess = True`). The bank is therefore scoped a priori to the non-saturated
   window (24 of 29 pts). A genuine lock that appeared ONLY in the top-5 saturated points (ω_s ≥
   1.30) would be invisible to this detector — but there is no physical reason to expect a
   BC-quantized lock to switch on only at the highest ω_s while the broad tracking zone shows
   clean carrier-tracking with the detector fully able to see a lock. The negative is bankable in
   the zone where it is measured.
2. **Lossy-Dirichlet wall (not strictly conservative).** The clamp removes 13.8% of the norm
   (monotone, never pumping). The ideal Γ=−1 wall is reflectionless; this is its lossy stand-in.
   The result stands for both readings: any weak locking-toward-1:1 pull is a lossy-wall artifact
   a reflectionless wall would REDUCE — so a conservative wall would not produce MORE locking than
   the lossy one that produced none.
3. **Temporal traversal read (not a spatial mode-index read).** The pivot claim is a phase-space
   traversal rotation number (θ = 2φ + 3ψ); this reads exactly that (the #417 global-phase
   coordinate; A46-faithful). A spatial standing-mode-index count is a different coordinate,
   untested here — a candidate successor, not a rescue.
4. **Host-stencil caveat (inherited from #417/#612).** Native diamond `TETRA_OFFSETS` stencil
   (achiral z=4); chiral-(2,3) template on an achiral host. The discriminator (does ρ track or
   lock under detuning) is carrier/BC-based and stencil-chirality-independent, as in #417. No
   parity conclusion drawn (sector fence).
5. **Sector fence (mandatory).** The texture/spin weld stays DEAD (#585). No spin/parity
   conclusion — only mode-existence (no mode-lock) and the quadrature-selector (μ-sign) null. The
   3/2 q-odd structure is TEXTURE, not spin.

---

## 7. CONSEQUENCE NOTE (flagged as follow-on — NOT landed in this session)

The banked TRACK is clean on the a-priori-frozen single axis. Two downstream updates follow, both
flagged here for the auditor/orchestrator to land (this session edits no skill file and no
settling note):

- **Miss-ledger.** The orchestrator's tethered-pivot BC-quantization miss-ledger increments
  **0-for-6 → 0-for-7.** The Grant-gated skill touches are queued SEPARATELY — not edited here.
- **W5-iii settling-note caveat.** In
  `research/2026-07-09_fast-sector-settling-boundary-conditions_walked-framing.md:159`, the W5-iii
  retraction caveat can be upgraded from **"unsupported-at-prereg-strength"** to **"banked
  negative"** (this result is the support). Flagged; not landed.

Register note (for the auditor to land): the #260 magnetic-vs-capacitive Γ=−1 wall μ-sign selector
returns the same NULL in this coordinate on the refined grid (0/4 flips; ρ_cap ≈ ρ_mag) — the
selector, if live, does not manifest in the temporal-winding orientation, consistent with #260's
B3-DEGENERATE verdict and the chirality→spin OPEN-SEAM staying open.

---

## 8. REPRODUCE

```
cd <worktree> && PYTHONPATH=<worktree>/src \
  /Users/grantlindblom/AVE-staging/AVE-Core/.venv/bin/python \
  -m ave.solvers.tethered_pivot_x34b
```

Emits `research/2026-07-10_tethered-pivot-rerun_result.json` +
`research/figures/2026-07-10-tethered-pivot-rerun/x34b_frozen_excess_axis.png` (WHITE house
style). Tests:

```
PYTHONPATH=<worktree>/src <venv>/python -m pytest src/tests/test_tethered_pivot_x34b.py -q             # fast pure-logic units
PYTHONPATH=<worktree>/src <venv>/python -m pytest src/tests/test_tethered_pivot_x34b.py -q -m engine_sim  # + live engine reads
```

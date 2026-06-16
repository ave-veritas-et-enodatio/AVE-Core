# PRE-REG (FROZEN, Rule-11) — Keystone bug-vs-substrate discriminator: PIECE 2 nested conservation ladder

**Date:** 2026-06-16 · **Lane:** implementer (engine) · **Branch:** `analysis/2026-06-16-keystone-discriminator-ladder`
**Base:** `analysis/2026-06-16-stage16-k4tlm-bounded-wall` @ `c5595558` (the wired energize-LOCK loop, the K4-TLM unitary wall, the tetra coupling stencil).
**Spec (authoritative):** `_orchestration/2026-06-16_keystone-discriminator-spec.md` (branch `analysis/2026-06-16-keystone-discriminator-spec`), PIECE 2 + Frozen-bins + Prior.
**Builds on result:** `research/2026-06-16_stage16-k4tlm-bounded-wall_result.md` — Phase-22 returned `PUMPS` (H: 856→8.2×10⁹), reattributed (auditor-EARNED) to a pre-existing pump in the energize-LOCK coupling + two-grid integration, NOT the wall.

This prereg is banked **BEFORE** any ladder measurement, freezing the 5 bins, the
dt-sweep grid, and the climb-rate-fit method. Per Rule 11: a clean negative with a
named mechanism is the discipline working — this prereg does NOT license a rescue,
and the bins/grid/fit-method below are NOT editable after the run.

---

## §0 — The question (one fork)

Phase-22's `PUMPS` is now attributed to the energize-LOCK COUPLING + the two-grid
integration (K-independent ~800%, present wall-OFF 4.86×, |ω| bounded by the unitary
wall). The fork: **a fixable discretization artifact, or a genuine substrate
negative?**

A naive single-grid known-positive is **DEGENERATE** — ≥4 confounds (the alive-mask
projection, the wall, the PML, the two-grid Cosserat sub-cycle roll) all survive it,
so "H climbs at matched centering ⇒ substrate" does not follow. The nested ladder
strips the confounds one rung at a time, measuring conservation on a **closed
interior box `B_int`** where no boundary/confound can leak in within the run.

---

## §1 — The H-witness box `B_int` (the key fix)

A **closed cubic interior box `B_int`** sitting entirely inside `mask_alive`, with a
**guard band** to the nearest domain edge / PML / wall / roll cell of

> `guard ≥ stencil_radius + c · dt · nsteps_window`

so NO roll/wall/PML cell can influence any `B_int` cell within the recording window
(information propagates at the shear speed `c_T = √(G/ρ) = 1` per `dt`; the bare
energy-gradient + tetrahedral-curl stencils have radius ≤ 2). The conserved witness

> `H = E_bulk + H_cosserat + H_c`

is summed **only over `B_int`** (PML-excluded by construction). `E_bulk` =
`bulk_energy_conserved` density restricted to `B_int`; `H_cosserat` =
`kinetic_energy + total_energy` density restricted to `B_int ∩ mask_alive`; `H_c` =
`κ̃·g·V·Ξ` density restricted to `B_int`. The density formulas are byte-identical to
the engine's existing energy methods — only the summation region changes (no new
physics in the witness).

**Box geometry (FROZEN):** `B_int` = the central cube `[c−h, c+h]³` (cell-inclusive)
with `c = N/2`, half-extent `h` chosen so the guard band to the domain edge is
`≥ guard` for the run's longest window. The seed (compact, sub-yield, smooth) is
placed at the center, strictly inside `B_int`, with its >1%-peak support contained in
`B_int` at t=0. The exact `h`, `guard`, `N`, and the per-rung window `nsteps` are
RECORDED in the results JSON `b_int_geometry` block (declared here; their VALUES are
set by the geometry constraint above, not tuned to a verdict).

---

## §2 — The 3-rung confound-stripping ladder (FROZEN)

All rungs use a **compact, sub-yield, smooth** Cosserat ω-photon seed strictly inside
`B_int` (sub-yield = peak |ω| below `omega_yield = π`, so the bare integrator is in its
conservative regime — a super-yield steep seed creates a t=0 nonlinear-regime transient
that is projection-INDEPENDENT and would confound the RUNG-0 gate; verified pre-reg).
α-free throughout (`wall_on` uses the kappa_chiral=0 geometric Γ; no ALPHA/KAPPA in the
update path). The (2,3) readout is untouched.

### RUNG-0 — BASELINE-CLEAN (the load-bearing gate; Phase-22 SKIPPED this)
- `couple_on=False`, `wall_on=False`, **PML off** (`pml_thickness=0` ⇒ `damping≡1.0`,
  `cos_pml_mask≡1.0`), single grid (`n_sub_cos=1`), **projection OFF**
  (`project_alive=False`: `_zero_outside_alive` / `_zero_velocities_outside_alive`
  are no-ops), compact sub-yield smooth seed strictly inside `B_int`.
- **GATE:** H over `B_int` must conserve to **O(dt²)** and stay **FLAT** over the window.
- **FAIL (drift):** the harness/projection is dirty → bin = `HARNESS-DIRTY` →
  **STOP and report**; the whole discriminator is uncalibrated, do NOT proceed to
  RUNG-1/2. This gate licenses every downstream rung.

### RUNG-1 — +PROJECTION (the prime suspect, genesis-24 prior)
- Identical to RUNG-0 EXCEPT **projection ON** (`project_alive=True`: the alive-mask
  `_zero_outside_alive` / `_zero_velocities_outside_alive` applied between the two
  half-kicks every substep — the mid-Verlet mask projection).
- **READ:** if H was FLAT at RUNG-0 but **DRIFTS** at RUNG-1 → bin = `PROJECTION-PUMP`
  (the mid-Verlet mask projection is the pump = a fixable harness bug, isolated). If H
  stays flat → the projection is NOT the pump; proceed to RUNG-2 to read the coupling.

### RUNG-2 — +COUPLING, FORCED-OVERLAP, dt→0 (the actual bug-vs-substrate read)
- Coupling on (`couple_on=True`), wall off, projection ON, supports **forced to
  overlap** (`coupling_support='saturated_interior'` so the front window `g` overlaps
  the winding curl `Ξ` at the trap interior — the engine's labeled overlap variant;
  the `'front'` shell has disjoint support and `f_V≡0`, which would make RUNG-2 vacuous).
  A sub-yield bulk blob co-located with the ω-seed provides the V the coupling needs.
- Sweep **dt → 0** over the FROZEN grid (§3). Measure the **H-climb RATE** = `dH/dt` of
  the `B_int` witness (per-unit-physical-time slope of H over the window).
- **READ (FROZEN, §4):** climb-rate **→ 0** as dt→0 ⇒ bin = `INTEGRATOR-ARTIFACT`
  (BUG; keystone stays OPEN, fix + re-test loop-closure). Climb-rate **plateaus** at a
  finite value as dt→0 ⇒ bin = `SUBSTRATE-PUMP` (continuum coupling pumps; keystone
  leans NEGATIVE).

---

## §3 — The dt-sweep grid (FROZEN — declared before the run)

The dt→0 extrapolation is the decider. The grid is set by **halving the base dt** so the
fit has clean leverage and the geometric guard band (§1) is recomputed per dt (a smaller
dt → a smaller per-step front travel, so the window can be longer in steps at the same
physical duration). Each dt holds the SAME physical recording window `T_win` (so the
H-climb is dH/dt over the SAME physical interval, not a per-step artifact).

> **dt grid:** `dt_k = dt_base / 2^k`, for `k = 0, 1, 2, 3` (four values: ×1, ×½, ×¼, ×⅛),
> where `dt_base = engine.dt` (the CFL-set bulk outer dt at the frozen N, dx).
> Physical window `T_win` is FROZEN; `nsteps_k = ceil(T_win / dt_k)` (so the finest dt runs
> the most steps over the same physical duration).

The climb-rate `R_k = dH/dt` is measured for each `dt_k`. (If a run diverges before
`T_win`, the climb-rate is measured over the realized sub-window and that is recorded;
a diverged-before-window run does NOT silently drop from the fit.)

---

## §4 — The climb-rate-fit method (FROZEN — the →0 vs plateau decider)

The H-climb rate `R_k` (units: H per unit physical time) is extracted per dt as the
**ordinary-least-squares slope** of the `B_int` witness `H(t)` vs physical time `t` over
the recording window (after the t=0 transient: the first recorded sample is excluded so a
one-step discretization offset is not fit as a rate). The fit is to the model

> `R(dt) = R_∞ + a · dt^p`   (p = 1 declared; a first-order integrator-pump scales ∝ dt)

via a **two-point Richardson + a 4-point OLS cross-check**:
- **Richardson (primary):** from the two finest dt (`dt_3, dt_2`), the dt→0 extrapolant is
  `R_∞ ≈ R_3 − (R_2 − R_3)·dt_3/(dt_2 − dt_3)` (linear-in-dt extrapolation to dt=0).
- **OLS cross-check (secondary):** fit `R_k` vs `dt_k` (all 4 points) by OLS line; the
  intercept is `R_∞^OLS`. The two estimates must AGREE in sign for the verdict to stand.

**Decision thresholds (FROZEN):**
- `INTEGRATOR-ARTIFACT` (climb-rate → 0): `|R_∞| / |R_0| < 0.10` AND the sequence `|R_k|`
  is **monotonically decreasing** in `k` (each halving cuts the rate) AND `R_∞` is within
  one extrapolation-uncertainty of 0. (A first-order integrator pump must visibly shrink
  as dt halves and extrapolate to ≈0.)
- `SUBSTRATE-PUMP` (climb-rate plateaus): `|R_∞| / |R_0| ≥ 0.10` AND `|R_k|` does NOT
  collapse toward 0 (the finest two dt agree on a finite `R_∞` to within their spread).
  (A continuum pump survives dt→0: halving dt does not kill it.)

**Extrapolation uncertainty (recorded):** the spread between the Richardson and OLS
intercepts, `Δ = |R_∞^Rich − R_∞^OLS|`, is reported as the fit uncertainty; the verdict is
flagged AMBIGUOUS-REPORT (not silently binned) if `Δ` exceeds `|R_∞|` (the two methods
disagree on the intercept by more than the intercept itself).

---

## §5 — Frozen bins (Rule-11 — the 5 bins; NOT edited after the run)

1. `HARNESS-DIRTY` — RUNG-0 H over `B_int` drifts (not flat to O(dt²)) → **STOP**;
   the discriminator is uncalibrated.
2. `PROJECTION-PUMP` — RUNG-0 flat but RUNG-1 (+projection) drifts → the mid-Verlet
   mask projection is the pump = a fixable harness bug, isolated.
3. `INTEGRATOR-ARTIFACT` — RUNG-2 H-climb-rate → 0 as dt→0 (per §4) → a BUG; the
   keystone stays OPEN (fix + re-test loop-closure).
4. `SUBSTRATE-PUMP` — RUNG-2 H-climb-rate plateaus at finite as dt→0 (per §4) → the
   continuum coupling pumps; the keystone leans NEGATIVE.
5. `BOUNDARY-INJECTION` — PIECE-1's domain (bulk-cancels-but-boundary-pumps). If the
   ladder sees boundary-flux behavior (e.g. H over `B_int` flat but H over the full
   interior climbs from edge injection), it is FLAGGED for the proof agent who owns it,
   not adjudicated here.

---

## §6 — The genesis-24 prior (load-bearing — must NOT bias the measurement)

The prior LEANS fixable-artifact (prime suspect = the mid-Verlet mask projection; a
conservative-potential `V·Ξ` coupling *should* conserve in continuum). BUT this would be
the **2nd** time this pump-family is called "a bug," so the ladder must **FORCE** the
verdict, not confirm the prior:

- The dt-grid (§3) + the climb-rate-fit method (§4) + the →0/plateau thresholds are
  declared HERE, before any RUNG-2 run. They are NOT re-tuned to land "bug."
- The dt→0 extrapolation is the decider; the Richardson + OLS cross-check + the Δ
  uncertainty are made explicit so the auditor can re-check the fit independently.
- No tuning of dt / box / seed to get the "bug" answer. The seed is fixed across the dt
  sweep (only dt varies) so the t=0 nonlinear transient is constant and only the
  integrator's dt-scaling moves the rate.

---

## §7 — Discipline + α-free

- **α-free (load-bearing):** no ALPHA/KAPPA in the update path. The `wall_on` Γ routes
  through the kappa_chiral=0 geometric override; RUNG-0/1 have `wall_on=False`. The
  α-free provenance gate (engine-module token scan) runs before the ladder.
- **PML exclusion (A-Rule 10):** `B_int` is interior-by-construction; RUNG-0 runs
  `pml_thickness=0` (PML genuinely off) so the baseline conservation is not masked by
  absorption.
- **Reactance-pair (A-Rule 10):** the witness records both the C-state (|ω|) AND the
  L-state (|ω̇|) over the window at every recorded step.
- **The projection toggle** (`project_alive` on `CosseratField3D`, default True =
  byte-identical) gates the four mask-projection calls so RUNG-0 (off) and RUNG-1 (on)
  differ ONLY in the projection.

---

## §8 — Deliverables

- this prereg (FROZEN) → engine `project_alive` toggle + `B_int` box-witness methods →
  the ladder driver (extends the Phase-22 infra) → run all rungs → committed results
  JSON (the durable record) → result doc
  `research/2026-06-16_keystone-discriminator-ladder_result.md` with the bin verdict +
  the deciding numbers (RUNG-0 flat to what O(dt²)? RUNG-1 drift magnitude? RUNG-2
  climb-rate at each dt + the dt→0 extrapolation + the fit uncertainty).
- Push the branch; do NOT merge (the auditor re-verifies the rung verdicts + the dt→0
  fit before anything banks; the bug-vs-substrate fork goes to Grant with the numbers).

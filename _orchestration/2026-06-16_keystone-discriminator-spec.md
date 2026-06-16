# Keystone Bug-vs-Substrate Discriminator — Corrected Spec (GO-WITH-ADDED-CONTROL)

**2026-06-16 · audit lane → engine lane · gated on Grant authorization**
**Source:** pre-flight discrimination audit `wyxd80ct2` (genesis-24 anchor + discriminator-design; grep- + numerically-grounded).

## Verdict: GO-WITH-ADDED-CONTROL

The Phase-22 bounded-wall build (branch `analysis/2026-06-16-stage16-k4tlm-bounded-wall`, banked `b074adb0`) returned **PUMPS** — but with the energize→LOCK loop **genuinely wired** (two-sided fire `f_V=133`, `f_ω_alive=1.5` on the alive sublattice, reproduced) and an **honest K4-TLM unitary wall** (|ω| bounded at 279.9). The residual pump (H: 856→8.2e9) is reattributed (auditor-EARNED) to a **pre-existing pump in the energize-LOCK coupling + two-grid integration**, NOT the wall (K-independent ~800%; present wall-OFF 4.86×). The open question: **fixable discretization artifact, or genuine substrate negative?** The proposed discriminator (continuum `dH_c/dt=0` proof + single-grid time-centering known-positive) is **degenerate as posed** — replace it with the spec below.

## Prior (genesis-24, grep-corrected)
- Genesis-24's pump = the **EMF-reciprocal** channel (velocity-rotation, `emf=+2·V_inc·∂L/∂V_sq`, engine-docstring-confessed "wrong direction", `k4_cosserat_coupling.py:242/703`) — **mechanistically distinct** from Phase-22's **position-like conservative-potential** coupling (`V·Ξ`, `Ξ=(∇×ω)·ẑ`, a spatial derivative). It is NOT the "double-count" (that's a *separate*, since-fixed genesis-24 winder gap).
- Genesis-24 **never** adjudicated its pump as substrate — flagged Outcome-B, recorded **OPEN**, in a family later ruled *"coordinate error, not a physics wall"* (`2026-06-09_tracereversal-pump-derivation_result.md`).
- So the prior **leans fixable-artifact** (reinforced: a conservative-potential coupling *should* conserve continuum). **Prime suspect:** the mid-Verlet **mask projection** (`_zero_outside_alive` / `_zero_velocities_outside_alive`, applied *between* the two half-kicks every substep) — non-canonical, can pump independent of substrate.
- BUT genesis-24 ran **neither** the proof nor a real known-positive — the burden is **undischarged**. This would be the **2nd** time this family of pump is called "a bug"; the proof + ladder must **force** the verdict, not assume it.

## PIECE 1 — continuum `dH_c/dt` proof, WITH the boundary term
The integration-by-parts that produces `f_ω` generates a boundary flux `∮(gV)(ω×n̂)dS`. It does **not** cleanly vanish: `g_front` is a Gaussian shell **at the saturation front — where Γ=−1 lives** — so the boundary term is on the **active wall**, and the domain is mixed periodic (`np.roll` forces) / bounded (energy integral). **REQUIRED:** show the boundary flux vanishes, or account it explicitly. **Bulk cancellation is necessary, NOT sufficient.** If the bulk cancels but the boundary flux is nonzero → the verdict is **BOUNDARY-INJECTION** (a wall/boundary effect), neither clean-bug nor clean-substrate — the third outcome the binary misses.

## PIECE 2 — the NESTED CONSERVATION LADDER (replaces the single-grid known-positive)
The naive single-grid known-positive is **degenerate** — ≥4 confounds (mask projection, wall, PML, two-grid roll) all survive it, so "H climbs at matched centering ⇒ substrate" does not follow. Instead, measure on a **closed interior box `B_int`** sitting entirely inside `mask_alive` with a guard band `≥ stencil_radius + n_sub_cos·c·dt` (so no roll/wall/PML cell enters `B_int` within the run). H-witness `= E_bulk + H_cosserat + H_c`, summed **only over `B_int`**. Strip confounds one rung at a time:

- **RUNG-0 — BASELINE-CLEAN** *(the build SKIPPED this; load-bearing gate)*: `couple_on=False`, `wall_on=False`, `damping=1.0` (PML off), single grid `n_sub_cos=1`, compact seed strictly inside `B_int`. **H must conserve to O(dt²) and stay FLAT.** If it drifts → the harness/projection is dirty → the **whole discriminator is uncalibrated → STOP**. This gate licenses every downstream rung.
- **RUNG-1 — +PROJECTION**: turn the alive-mask projection back on. Drifts at RUNG-1 but was flat at RUNG-0 → the **projection** is the pump (fixable harness bug), isolated.
- **RUNG-2 — +COUPLING, FORCED-OVERLAP, dt→0**: the actual bug-vs-substrate read. Coupling on, supports forced to overlap, sweep `dt→0`, measure the **H-climb RATE**. Climb-rate **→ 0** as `dt → 0` ⇒ **integrator artifact** (BUG; keystone stays open, fix + re-test loop-closure). Climb-rate **plateaus** at finite value as `dt → 0` ⇒ **SUBSTRATE** (continuum coupling pumps; keystone leans negative).

## Frozen bins (Rule-11, declare before the run)
`HARNESS-DIRTY` (RUNG-0 fails → STOP) · `PROJECTION-PUMP` (RUNG-1 drifts → fixable harness bug) · `INTEGRATOR-ARTIFACT` (RUNG-2 climb-rate→0 → bug, keystone open) · `SUBSTRATE-PUMP` (RUNG-2 climb-rate plateaus → keystone negative) · `BOUNDARY-INJECTION` (piece-1 bulk-cancels-but-boundary-pumps → wall/boundary effect).

## Gate
Engine lane builds the ladder + the boundary-term proof → runs → **auditor lane re-verifies** the rung verdicts + the `dt→0` fit before anything banks (auditor-not-exempt; a false keystone-verdict is the one outcome worse than the wait) → the bug-vs-substrate fork goes to Grant **with the deciding numbers** (RUNG-0 flat? RUNG-1 drift? RUNG-2 `dt→0` climb-rate?). No Phase-23 bank, no merge, until those clear.

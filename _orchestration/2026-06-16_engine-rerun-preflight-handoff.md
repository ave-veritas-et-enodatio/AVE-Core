# Engine Re-Run — Pre-Flight Correction (FIX-BEFORE-DISPATCH)

**2026-06-16 · audit lane → engine lane · gated on Grant Q3 (re-run authorization)**
**Source:** pre-flight discrimination audit `ww8x96sci` (4 adversarial agents; every finding grep- + numerically-reproduced against branch tip `a233f9ed`).

## Verdict: **FIX-BEFORE-DISPATCH**

The corrected-stencil keystone re-run **as framed in the dispatch brief** (curl-only swap + un-bounded `K_wall=400` + a renamed 3-bin set) can bank a **FALSE LOOP-CLOSES** on the keystone's first real test. Three verified gaps (2 blockers) + a dropped 4th bin. Apply the 5 amendments below, **re-run this pre-flight (`ww8x96sci`) to confirm clearance, then dispatch on Grant's Q3 go.** The hold is cheap — all 5 are grep-anchored implementer fixes, not new physics.

> **Provenance fix first:** the dispatch cited commit `230579b6`, but the engine/driver/prereg/results live only on tip **`a233f9ed`** (branch `analysis/2026-06-16-boundary-mqj-stage16-moving-wall-sectorB`); `230579b6` is **not** an ancestor and does not contain these files. Same phantom-hash slip as `aebbc99dbd` earlier — re-cite from `a233f9ed`.

## The gaps

### GAP 1 — the curl swap must be **TWO-SIDED** (verified, reproduced)
The brief swaps only the forward curl (`_coupling_forces:366` / `_coupling_energy:379`). But the **reciprocal back-reaction** `f_omega` (`a1_cosserat_convergence_engine.py:369-372`) computes `dgV_dx/dgV_dy` with the **same** Cartesian single-axis `np.roll±1` on the alive-masked `gV` → it **self-zeros on alive** (numerically: `max|dgV_dx| = max|dgV_dy| = 0` on alive, `1.648` on dead). A curl-only swap restores `f_V` but leaves `f_omega≡0` on the alive sublattice → a **source-only half-loop**, not the reciprocal energize-LOCK the docstring claims. (The earlier breadth check was right about the *curl function* but missed this *second* dead-straddle site — it is an inline gradient, not the curl.)

### GAP 2 — `coupling_work` can't distinguish real exchange from wall-work (BLOCKER)
`coupling_work` (`a1_cosserat_moving_wall_engine.py:298`) is a **signed running sum of an instantaneous energy-functional**, not a measured sector-to-sector transfer. The wall mutates ω every sub-step and `Ξ=curl(ω)` feeds the integrand → the same geometric confinement the tetra-swap exploits makes `H_c` nonzero **whether or not** genuine reactive exchange occurred. The conserved ledger `coupling_hamiltonian_full()` **is computed (`:205`) but only traced (`driver:220`), never gated.** A bounded wall-pump that injects energy without diverging |ω| would read as LOOP-CLOSES.

### GAP 3 — the "Op17-bound" premise is false + a 4th bin was dropped (BLOCKER)
`_rotate_clamp` (`cosserat_field_3d.py:1760-1783`) is an **exact harmonic rotation with NO |ω| ceiling** — it does not bound amplitude. In the banked data the wall **fully forms (Γ→−0.993) WHILE H climbs 4.3×10⁶** (`2.36e3 → 1.02e10`) — it **forms AND pumps together** (wall-coupled, *not* "separable over-drive"). That is the **4th outcome: WALL-FORMS-AND-PUMPS**, which the **frozen prereg already has** (`research/2026-06-16_stage16-moving-wall-sectorB-prereg.md:108-114`, the **WALL-ALSO-FAILS** bin) but the dispatch brief renamed to 3 bins and dropped.

## Corrected dispatch spec — the 5 amendments

1. **Two-sided tetra swap.** Swap the curl in `_coupling_forces:366` + `_coupling_energy:379` **AND** replace the `f_omega` reciprocal gradient (`:369-372`) with the parity-correct **`adjoint_tetrahedral_divergence`** (`cosserat_field_3d.py:161`, the exact discrete adjoint of `_tetrahedral_gradient`) so the `H_c` reciprocity holds on the alive sublattice.
2. **Two-sided fire assertion.** Require `fV_live_max > 0` **AND** `f_omega_alive_max > 0` before any LOOP-CLOSES bin (the current `loop_fires` gate checks only the source).
3. **H-ledger bin gate.** LOOP-CLOSES requires `coupling_hamiltonian_full()` **flat/decaying** over the long window **AND** the ON-minus-OFF `coupling_work` excess matching a conserved redistribution (the prereg promises this in *prose* at `:137` — make it a *bin condition*, with `V_clamp` wall-storage held separable).
4. **K_wall sweep (no amplitude ceiling exists).** Sweep `K_wall` (e.g. 100/200/400/800) and report whether **any** K holds `H` flat **AND** preserves Γ→−1 + loc-held. If none separates pump-suppression from confinement-loss → verdict is **AMBIGUOUS-pending-stable-BC**, not a substrate statement.
5. **Known-null meter control + frozen bins.** Add a forced-zero coupling-meter null (matched Γ≈0 or the verified disjoint-support config) where `coupling_work` MUST read 0 — so a 0 at the operating point has a calibrated zero-reference distinct from a diverged-before-overlap 0; extend the known-positive window past where the wall stays bounded. **Report against the FROZEN prereg's 4 bins** — `LOOP-CLOSES / WALL-CONFINES-BUT-LOOP-INERT / WALL-ALSO-FAILS / PUMPS` (the driver code `driver:396-419` already uses these; only the brief's framing drifted) — **not** the brief's renamed 3.

## Run scope (unchanged from the brief, once corrected)
Same generic seed (CP8-clean); run **both** the no-wall Stage-1.5(c) config and the Stage-1.6 moving-wall config; the dual gate stays (parity-support restored AND supports dynamically co-locate). The Rule-12 retraction of Stage-1.5(c) rides this branch as before.

## Gate sequence
engine lane folds in amendments 1–5 → **re-run `ww8x96sci` pre-flight to confirm GO-AS-IS** → Grant authorizes Q3 → dispatch. Two false-positive paths are closed by this (the one-sided half-fix and the wall-forms-and-pumps with no ledger gate); a false keystone-advance is the one outcome worse than the delay.

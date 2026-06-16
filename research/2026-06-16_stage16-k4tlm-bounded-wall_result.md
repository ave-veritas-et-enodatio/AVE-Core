# RESULT — Stage-1.6 K4-TLM bounded-wall re-run (amendment-4 unitary scatter)

**Date:** 2026-06-16 · **Lane:** implementer · **Branch:**
`analysis/2026-06-16-stage16-k4tlm-bounded-wall` (off
`analysis/2026-06-16-stage16-rerun-amendments`).
**Prereg (FROZEN + Amendment A4):**
`research/2026-06-16_stage16-moving-wall-sectorB-prereg.md`.
**Driver:** `src/scripts/vol_1_foundations/stage16_moving_wall_sectorB.py`.
**Results JSON:** `src/scripts/vol_1_foundations/stage16_moving_wall_sectorB_results.json`.

> Implementer reports the bin; the orchestrator adjudicates chord/echo. This doc
> does NOT conclude chord/echo and does NOT round up to LOOP-CLOSES — a false
> keystone-advance is the one outcome worse than a clean negative.

---

## §0 — Bin verdict (one of the FROZEN 4)

**Primary run (N=24, dx=0.5 = the frozen-prereg grid where the wall forms,
12 Compton periods, K_wall=400, amp=2.0, α-free, unitary wall):**

> **VERDICT: `PUMPS`** — but with a **CORRECTED mechanism attribution** (see the
> FLAG in §5). The bin is correct per the FROZEN H-ledger gate (H not flat ⇒ NOT
> LOOP-CLOSES), but the pump is **NOT the wall** — the unitary wall fixed the
> wall-pump and EXPOSED a deeper, pre-existing coupling/bulk pump.

Frozen bins: `LOOP-CLOSES / WALL-CONFINES-BUT-LOOP-INERT / WALL-ALSO-FAILS / PUMPS`.

The single decisive change vs the `_rotate_clamp` baseline is the **wall mechanism**
(amendment-4: harmonic node-clamp → K4-TLM unitary scatter). The grid, seed,
coupling, and all four discriminator gates are unchanged.

**What the unitary wall achieved (its narrow goal — SUCCESS):** at the amp=2.0
operating point where `_rotate_clamp` pumped to `|ω|max=20918`, the unitary wall
holds `|ω|max=279.9` (wall-ON) — a **~75× amplitude reduction** — while storing
**zero** separable reactive energy (`V_clamp ≡ 0.0` throughout). The wall is
energy-honest and |ω|-bounded by construction, exactly as designed.

**Why the bin is still PUMPS (the deeper obstruction — the load-bearing finding):**
the conserved ledger `H = T + W_linear` (with `V_clamp=0`) still climbs
`856 → 8.2×10⁹` over the window (peak-rise `+9.5×10⁶`, NOT flat). This pump is
**NOT the wall**: (1) it is **K-INDEPENDENT** — the K_wall sweep shows `Hnv_rise`
≈ 800% at K=100/200/400/800 alike (798/887/798/807%), even at K=400 where the
wall barely forms (Γ_min=−0.053), while `|ω|max_f` stays ≈ 2 at every K; (2) it is
**present with the wall completely OFF** — the no-wall control pumps H by 4.86× to
`|ω|max=20004` (and the `_rotate_clamp` baseline's no-wall case pumps identically,
`|ω|max=20008` — so this is **pre-existing**, not introduced by amendment-4). The
pump source is the **energize-LOCK coupling + the discrete two-grid bulk
integration**, which the unbounded wall-pump was previously MASKING.

---

## §1 — The build (amendment-4 unitary-scatter wall)

The Stage-1.6 moving Γ=−1 wall on Sector B is realized as a **K4-TLM Op3
unitary-scatter reflector** adapted to the Cosserat `(ω, ω̇)` reactance pair,
replacing the harmonic node-clamp `_rotate_clamp`.

- **Engine:** `CosseratField3D._unitary_scatter` (`src/ave/topological/cosserat_field_3d.py`),
  wired behind `impedance_unitary` (default-off legacy on `CosseratField3D`,
  default-ON on `A1CosseratMovingWallEngine`).
- **Mechanism:** at the wall cells, decompose `(ω, ω̇)` into d'Alembert
  incident/reflected characteristic amplitudes on the dimensionless reactance
  plane `(ω, ω̇/Ω₀)` (`Ω₀ = √((K/I_ω)·relu(−Γ))`, the wall's own reactance
  frequency, identical to `_clamp_omega0`), apply the **orthogonal** scatter
  `[[Γ_w,T_w],[T_w,−Γ_w]]` (`Γ_w = relu(−Γ) ∈ [0,1]`, `T_w = √(1−Γ_w²)`,
  `Γ_w²+T_w²=1`), recompose. Ported verbatim in structure from
  `k4_tlm.py:402-423` (`V_inc = Γ·V_ref_A + T·V_ref_B`).
- **Why this is the energy-honest, |ω|-bounded wall:** the scatter matrix is
  orthogonal, so it preserves the reactance-pair norm `½(ω²+ω̇²/Ω₀²)` EXACTLY
  and maps `|output|=|input|`. The wall therefore **cannot inject energy (no
  pump)** and `|ω|` is **bounded by the incident amplitude (no blow-up)** — by
  construction, independent of `K_wall`. At the μ-short `Γ_w→1,T_w→0` the wave
  reflects with the corpus `Γ=−1` inversion (`electron-identification.md:24/:25`,
  property-3 TIR cavity); at matched/open `Γ_w→0,T_w→1` the pair free-streams
  (the bulk wave is unchanged) — the K4-TLM scatter+connect split.
- **Isolation check (this branch):** over 200 repeated scatters at full
  reflection, the reactance-pair norm is conserved to ratio = `1.00000000` and
  `|ω|max` is held (vs `_rotate_clamp`'s unbounded pump). The wall stores **no
  separable reactive potential** (`V_clamp ≡ 0` for the unitary path in
  `impedance_hamiltonian`) — energy stays in the ω-wave; any rise in `H = T +
  W_linear` is then a genuine pump, not reactive wall-slosh.

`substrate-native-check` CP10: this is the boundary rendering (reflection
`R = Γ² ≤ 1`), NOT the bulk restoring force `_rotate_clamp` is (a stiffening
spring `ω̈ = −Ω₀²ω`, singular and energy-unbounded at the wall). α-free
preserved (no α in the scatter; geometric Γ via `kappa_chiral=0`). The (2,3)
winding readout is untouched (A46-clean per Phase-20).

## §2 — The deciding numbers (the four gate conditions)

A **LOOP-CLOSES** verdict requires ALL FOUR (FROZEN, #273 amendments 2/3/5):

| Gate | Condition | Primary-run value | Pass? |
|---|---|---|---|
| **Two-sided fire** | `fV_live_max>0` AND `f_omega_alive_max>0` on alive | `f_V=133.1`, `f_ω_alive=1.502` | ✅ BOTH fire |
| **H-ledger flat/decaying** | `H_minus_Vclamp` peak-rise `<0.10` over the long window | peak-rise **+9.5×10⁶** (V_clamp=0) | ❌ NOT flat |
| **Conserved redistribution** | ON−OFF `coupling_work` excess = bounded conserved redistribution | excess `+1.56×10⁷`, `conserved=False` | ❌ |
| **Known-null meter (amend-5)** | forced-zero (V≡0) coupling-meter reads `≈0` at its calibrated zero | `−1.76×10⁻⁷` | ✅ reads zero |
| **Wall confines** | loc held + > no-wall+0.2 | loc 0.797 vs no-wall 0.163 | ✅ confines |
| **Generic-offset sweep** | EARNED (not a plant) | 6/6 offsets fire → **EARNED** | ✅ |

**The two-sided fire — the thing the whole stencil saga was about — FIRED.** Both
the source `f_V=133.1` AND the reciprocal back-reaction `f_ω_alive=1.502` are live
on the **ALIVE** sublattice (the amendment-1 tetra swap + `adjoint_tetrahedral_divergence`
back-reaction worked; §3 confirms the tetrahedral curl puts `|Ξ|=2.932` on alive
with **1024** overlap cells, while the Cartesian curl puts it entirely on dead with
**0** overlap). So this is NOT a half-loop and NOT a stencil artifact — the loop
*mechanism* is wired correctly on both sides.

**But LOOP-CLOSES requires ALL gates, and the H-ledger gate FAILS** (H not flat).
Per the FROZEN adjudication: a `coupling_work≠0` with a climbing conserved ledger
is a PUMP, not a closed loop. The discipline works — the H-ledger gate (amendment-3)
caught exactly the failure mode the bare `coupling_work` running sum could not
distinguish. **The verdict is PUMPS — NOT rounded up to LOOP-CLOSES.**

## §3 — K_wall-sweep AMBIGUOUS motivation (why the unitary wall is needed)

The `_rotate_clamp` baseline (retained in the driver as the motivating diagnostic;
selectable via `impedance_unitary=False`) lands **PUMPS / AMBIGUOUS** — the
"Op17-bound" premise of the frozen prereg §1.3 is FALSE. Banked baseline
(N=16, dx=0.5, the `_rotate_clamp` harmonic node-clamp; saved to
`/tmp/stage16_N16_rotateclamp_baseline.json`, re-runnable with `impedance_unitary=False`):

| metric (`_rotate_clamp` baseline) | value |
|---|---|
| verdict | **PUMPS** |
| `\|ω\|max_f` (wall on, amp=2.0) | **20918** (vs unitary `1.64` at the same op-point) |
| `H_minus_Vclamp` peak-rise | **+7.4×10⁶** (flat=False) |
| coupling_work ON / f_V / f_ω_alive | −2.88×10⁵ / 9057 / 1.855 |
| K_wall sweep | **AMBIGUOUS-pending-stable-BC** (no clean K) |
| K=100 / 200 / 400 / 800 — Γ_min | −0.001 / −0.038 / −0.994 / −0.994 |
| K=100 / 200 / 400 / 800 — H rise | +74% / +89% / +1810% / +959% |
| known-null meter | −5.97×10⁻⁹ (reads-zero ✓) |

The `_rotate_clamp` K_wall sweep is the proof the wall-gap is unfixable by VALUE:
at every K, either the wall doesn't form (K=100/200, Γ_min≈0) or it forms AND pumps
(K=400/800, Γ_min→−0.99 WITH H rising 10–18×). **No value of a no-ceiling clamp can
add a ceiling** — confinement (Γ→−1) and pumping (H climbs) rise together because
`_rotate_clamp` is a stiffening spring. The unitary scatter resolves THIS by
construction: it bounds `|ω|` WITHOUT a value knob (orthogonality, not stiffness).

**The unitary-wall K_wall sweep (primary run) is the diagnostic that ATTRIBUTES the
residual pump — and proves it is NOT the wall:**

| K_wall (unitary) | Hnv rise | Γ_min | `\|ω\|max_f` | wall forms |
|---|---|---|---|---|
| 100 | +798.8% | −0.993 | 2.8 | True |
| 200 | +887.5% | −0.292 | 2.1 | False |
| 400 | +798.0% | −0.053 | 1.6 | False |
| 800 | +807.3% | −0.154 | 2.8 | True |

`|ω|max_f` ≈ 2 at EVERY K (the unitary wall bounds amplitude regardless of K), yet
`Hnv_rise` ≈ 800% at EVERY K — **K-INDEPENDENT, and present at K=400 where the wall
barely forms (Γ_min=−0.053)**. A wall-pump would scale with K and vanish when the
wall doesn't form. This 800% does neither ⇒ **the residual pump is NOT the wall.**
The wall is energy-honest (V_clamp=0, |ω| bounded); the pump is the energize-LOCK
coupling + the discrete two-grid bulk integration (confirmed by the wall-OFF
control, which pumps H 4.86× with no wall at all — §0).

## §4 — dx-normalize note (side-rider) + a FLAG

Per the brief, `dx=0.5 → dx=ℓ_node=1.0` was normalized across the engine defaults
(`a1_cosserat_convergence_engine.py`, `a1_cosserat_moving_wall_engine.py`) and the
Stage-15/16 drivers (env-overridable: `S16_DX`, `S15_DX`). The stale FALSE comment
`boundary_mqj_selftrap_zwall_gate.py:94` ("natural units: dx = ℓ_node" while
`KP_DX=0.5`) is corrected.

**Where it is pure oversampling (object unchanged, sampling only):** the
Stage-15/16 seed geometry is set in CELLS (`center`, `sigma`, `wavelength` in cell
units), so `dx` only rescales the lattice pitch — the object in cells is identical;
`dx=0.5` was 2× OVERsampling (Phase-20 scoped credit). nsteps for 12 periods halves
(`3894→1947`).

**🔧 FLAG — dx is NOT inert for the wall-FORMATION threshold (a real finding, not
a cosmetic).** The geometric μ-short `Γ` is driven by the saturation curvature
`A²_μ = κ²/ω_yield²`, and `κ` (the ω-curvature) is evaluated on the grid — so it is
dx-dependent. Measured (this branch, unitary wall, amp=2.0 operating point):

| grid | Γ_min0 @ amp=2.0 | wall FORMS @op | KNOWN-POSITIVE PASS |
|---|---|---|---|
| dx=0.5 (frozen grid) | **−0.251** | **True** | **True** |
| dx=1.0 (normalized) | −0.031 | False | False |

At dx=1.0 the wall barely forms at the prereg's operating point (the apparatus
floor moved up). So the dx-normalize, while pure-oversampling for the *bulk wave
object*, **shifts the saturation-front formation threshold** — it is NOT inert for
the wall apparatus. **Decision (load-bearing):** the PRIMARY verdict run is at
**dx=0.5** (the frozen-prereg grid where the apparatus-floor known-positive PASSES),
so the amendment-4 test isolates the *wall mechanism* (clamp→unitary) without
confounding it with a *wall-doesn't-form-at-this-dx* artifact. The dx=1.0 run is
reported as the side-rider data point, NOT the verdict grid. The sibling drivers
(`stage15_layer_a/c`, `boundary_mqj`) were NOT re-run on this branch; their DX
defaults are normalized but env-reversible, flagged for their owners to
re-validate (and `boundary_mqj`'s `KP_DX` is dx-COUPLED to its seed radius
`r=(cell)·KP_DX` — left at 0.5 with a corrected comment + a flag, NOT silently
flipped).

## §5 — Honest framing

**The loop does NOT close. Bin = `PUMPS` (FROZEN prereg §4).** Three of the four
LOOP-CLOSES gate conditions PASS (two-sided fire ✅, known-null meter ✅, wall
confines + offset-sweep EARNED ✅), but the **H-ledger gate FAILS** (the conserved
`H = T + W_linear`, with `V_clamp=0`, climbs `856 → 8.2×10⁹`). Per the FROZEN
adjudication, a climbing conserved ledger is a pump, not a closed loop — so this is
**NOT rounded up to LOOP-CLOSES**. A clean negative with a named mechanism (below)
is the discipline working (Rule 11).

**What amendment-4 settled (the build SUCCEEDED at its stated goal):** the K4-TLM
unitary-scatter reflector IS the energy-honest, |ω|-bounded wall it was built to be.
At the operating point where `_rotate_clamp` pumped `|ω|` to 20918, the unitary wall
holds it at 279.9 (~75× lower) and stores zero separable reactive energy (V_clamp=0,
norm-conserved to 1.00000000 in isolation). The frozen prereg's false "Op17-bound"
premise (the no-ceiling `_rotate_clamp`) is corrected; the wall is no longer the
confound. **The catch-22 the brief named — bound |ω| without suppressing the
reactive exchange — is resolved:** the loop *fires two-sided on the alive
sublattice* (f_V AND f_ω) WHILE the wall bounds |ω|.

> ### 🚩 FLAG (flag-don't-fix, for Grant/auditor — do NOT silently resolve)
>
> **The driver's auto-generated PUMPS reason mis-attributes the pump to the wall**
> ("the wall is not Op17-bounded — |ω| blow-up"). That attribution is **FALSE** for
> the unitary wall: |ω| is bounded (279.9, not a blow-up), V_clamp=0, and the
> residual H-pump is **K-INDEPENDENT** (~800% at all K, even where the wall barely
> forms) **and present with the wall completely OFF** (no-wall control pumps 4.86×,
> |ω|max=20004; the `_rotate_clamp` baseline's no-wall case pumps identically). The
> pump is therefore **PRE-EXISTING in the energize-LOCK coupling + the discrete
> two-grid bulk integration** — the unbounded wall-pump was MASKING it. Amendment-4
> removed the mask and **exposed a second, deeper pump in the coupling itself.**
>
> **What this means for the keystone question (implementer does NOT adjudicate):**
> the electron's energize→LOCK loop test is now blocked NOT by the wall (fixed) and
> NOT by a stencil artifact (the two-sided fire is wired correctly on alive) but by
> a **non-conservative energize-LOCK COUPLING** in the discrete integration. Whether
> that is (a) a fixable two-grid time-centering / coupling-integrator bug
> (`WALL-engine` capability gap — the coupling force `f_V`/`f_ω` enters Sector A's
> leapfrog and Sector B's sub-cycled Strang at mismatched time-centering, the
> classic source of a discrete-coupling pump), or (b) a genuine substrate statement
> (a free propagating massless precursor cannot losslessly close the loop even with
> a perfect wall), is the **next fork** — and it is NOT mine to call. The driver's
> auto-reason should be read as "PUMPS — but the pump is the coupling, not the
> wall," pending that adjudication.
>
> **Scope discipline (A44 missing-axiom-vs-engine-bug):** I am NOT drafting an
> Ax-5 candidate. The diagnosis points at the discrete coupling integration
> (engine), not at a missing axiom — the conservative continuum H_c is exact (the
> `_coupling_forces` docstring: "the continuum energy cancellation is EXACT"); the
> pump is in the discretization. This is surfaced as an empirical finding for the
> orchestrator/Grant to route, not resolved here.

**Bottom line:** amendment-4 is a clean, honest **negative on the keystone loop
closure** with a **named, newly-exposed mechanism** (the coupling/bulk pump). The
bounded wall is delivered and validated; it did not rescue the loop, and it sharpened
*why* — moving the obstruction from "the wall pumps (ambiguous)" to "the coupling
pumps (specific, attributable, K-independent, wall-OFF-persistent)." The keystone
does NOT advance on this run.

---

## §6 — Figures (REAL data, N=24 dx=0.5 primary run)

1. `research/figures/stage16_fig1_moving_wall_tdr.png` — wall front + photon
   confinement (wall held vs no-wall dispersed).
2. `research/figures/stage16_fig2_coupling_work_fV.png` — coupling_work / f_V
   trajectory (the loop fires, but H pumps).
3. `research/figures/stage16_fig3_sectorB_gamma_smith.png` — Sector-B Γ center→rim.
4. `research/figures/stage16_fig4_winding_read.png` — (2,3) winding read.
5. `research/figures/stage16_fig5_apparatus_floor.png` — apparatus-floor
   known-positive (the α-free wall confines a known photon).

## §7 — Reproduce

```
S16_N=24 S16_DX=0.5 S16_PERIODS=12 \
  PYTHONPATH=<worktree>/src <main>/.venv/bin/python \
  src/scripts/vol_1_foundations/stage16_moving_wall_sectorB.py
```
The unitary wall is default-ON (`impedance_unitary=True`). To reproduce the
motivating `_rotate_clamp` PUMPS/AMBIGUOUS diagnostic, construct the engine with
`impedance_unitary=False`. dx-invariance side-check: `S16_DX=1.0` (note the
wall-formation-threshold FLAG in §4).

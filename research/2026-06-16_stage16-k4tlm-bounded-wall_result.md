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

> **VERDICT: `_VERDICT_` ** — _filled from the run._

Frozen bins: `LOOP-CLOSES / WALL-CONFINES-BUT-LOOP-INERT / WALL-ALSO-FAILS / PUMPS`.

The single decisive change vs the `_rotate_clamp` baseline is the **wall mechanism**
(amendment-4: harmonic node-clamp → K4-TLM unitary scatter). The grid, seed,
coupling, and all four discriminator gates are unchanged.

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

| Gate | Condition | Primary-run value |
|---|---|---|
| **Two-sided fire** | `fV_live_max>0` AND `f_omega_alive_max>0` on alive | _PENDING_ |
| **H-ledger flat/decaying** | `H_minus_Vclamp` peak-rise `<0.10` over the long window | _PENDING_ |
| **Conserved redistribution** | ON−OFF `coupling_work` excess = bounded conserved redistribution (V_clamp separable) | _PENDING_ |
| **Known-null meter (amend-5)** | forced-zero (V≡0) coupling-meter reads `≈0` at its calibrated zero | _PENDING_ |

Plus the wall-confinement + generic-offset-sweep (EARNED, not a plant) gates.

_The two-sided fire is the thing the whole stencil saga was about: f_omega must
be live on the ALIVE sublattice (the amendment-1 tetra swap + adjoint
back-reaction), not self-zeroing. Reported explicitly below._

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

The K_wall sweep is the proof the gap is unfixable by VALUE: at every K, either the
wall doesn't form (K=100/200, Γ_min≈0) or it forms AND pumps (K=400/800, Γ_min→−0.99
WITH H rising 10–18×). **No value of a no-ceiling clamp can add a ceiling** —
confinement (Γ→−1) and pumping (H climbs) rise together because `_rotate_clamp` is
a stiffening spring. The unitary scatter resolves this by construction: it bounds
`|ω|` WITHOUT a value knob (orthogonality, not stiffness), and WITHOUT suppressing
the reactive sector-to-sector exchange the loop test measures (the posable-vs-
meaningful catch-22 the frozen prereg's bounded-wall premise tried and failed to
thread).

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

_PENDING the primary verdict. Will state plainly which of the four FROZEN bins the
loop lands in, and will NOT round up to LOOP-CLOSES unless all four §2 gate
conditions hold._

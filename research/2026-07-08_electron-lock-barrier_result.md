# Electron-lock RECONNECTION-BARRIER — RESULT: genuine confinement does NOT rescue the (2,3); the phase-space winding STILL tracks the carrier ratio, there is NO barrier against unwinding, and the confined winding disperses like the free one

**Status:** **RESULT (committed).** Full 4-arm run per the frozen pre-reg (this doc post-dates the prereg-freeze commit; timestamp-ordered).
**Date:** 2026-07-08
**Pre-reg:** `research/2026-07-08_electron-lock-barrier_prereg.md` (frozen commit `576af2ac`) — followed exactly (4 arms + all discipline gates frozen before the run).
**Module:** `src/ave/solvers/electron_lock_barrier.py` · **Test:** `src/tests/test_electron_lock_barrier.py` (12 tests, all green) · **Run:** `src/scripts/vol_2_particle_physics/electron_lock_barrier_run.py` · **Results:** `results/electron_lock_barrier_results.json` · **Figure:** `research/figures/2026-07-08-electron-lock-barrier/electron_lock_barrier.png`
**Class:** CONSISTENCY (does confinement install a topological barrier that rescues the charge-winding — NOT a novel-value chord). Q=137 stays EMPTY. mass=A1 (PR#260) UNTOUCHED. charge = Link(∂Ω,F) ∈ ℤ (static topology) UNTOUCHED.
**Reuse (Rule 14):** `coupled_cage_winding.step()` (the conservative UNITARY S3 evolver), `seed_A1_sech`/`seed_winding` (the electron seed), `front_gate` (the α-free R_II=4/7 saturation-front gate), `compute_Q_link` (the real-space winding reader). New code = the moving-Γ=−1 reactive confinement wall (Hermitian on-site potential), the readers, the 4 arms, the barrier homotopy, the discipline gates.

---

## 0. HEADLINE

> **VERDICT: ECHO.** With a GENUINE, lossless (energy-conserving, unitary) moving-Γ=−1 confinement
> wall ON, and a RECONNECTION-CAPABLE (`dispersive_vector`) director — so unwinding is physically
> possible — the electron-lock's last un-run test reads NEGATIVE on all three counts:
>
> 1. **The phase-space (2,3) STILL tracks the LC carrier ratio ω_b:ω_s** (the DECISIVE kill-gate).
>    Confinement compresses the ratio SLOPE but cannot kill the carrier-DEPENDENCE — the winding
>    ratio stays monotonic in ω_b/ω_s (correlation **0.90** dispersive / **0.92** rigid wall-ON /
>    **0.97** rigid wall-OFF). A topological charge would be carrier-INVARIANT (flat); it is not.
> 2. **There is NO energy barrier against unwinding.** The adiabatic forced-unwind is DOWNHILL
>    (H_conf 9693.6 → 8844.6; barrier height **0.0** vs a wall-fluctuation budget of **540**).
> 3. **The confined winding disperses like the free one** (real-space |Q_link,raw| drop **2.988**
>    confined vs **2.993** free) — confinement holds neither the core nor the winding.
>
> All done under the UNITARY evolver (joint-norm H-drift **≤ 1.3×10⁻¹⁰** every arm — no damping
> faked a hold). **Confinement does NOT rescue the topology. Reading B closes NEGATIVE.** Per Rule 12
> this RETRACTS to *"confinement installs no reconnection barrier"* — it does **NOT** walk back
> charge = Link(∂Ω,F) (static topology, independently grounded) nor mass = A1 (#260).

## 1. THE DECISIVE detuning kill-gate (Arm 3, phase-space Clifford torus) — VERBATIM

The winding ratio = (toroidal net turns Δφ)/(poloidal net turns Δψ), swept over ω_b:ω_s. A carrier
ratio TRACKS ω_b/ω_s (the #417 echo signature); a topological charge is carrier-INVARIANT.

| ω_b:ω_s | carrier ω_b/ω_s | winding ratio (dispersive, wall ON) | winding ratio (rigid, wall ON) | winding ratio (rigid, wall OFF = #417 ref) |
|---|---|---|---|---|
| 1:1 | 1.000 | 0.546 | 0.733 | 1.273 |
| 2:3 | 0.667 | 0.600 | 0.692 | 0.634 |
| 3:2 | 1.500 | 0.821 | 0.828 | 1.589 |
| 1:2 | 0.500 | 0.435 | 0.537 | 0.460 |
| **classification** | — | **tracks** (corr **0.900**, slope 0.332) | **tracks** (corr **0.920**, slope 0.253) | **tracks** (corr **0.972**, slope 1.171) |

**Read the slopes:** wall-OFF has slope **1.171** (≈ perfect echo y=x — the clean #417 reproduction).
Turning the confinement wall ON COMPRESSES the slope to ~0.25–0.33 — BUT the CORRELATION stays
~0.90–0.92: the wall damps how steeply the ratio follows the carrier, yet the carrier-DEPENDENCE (the
echo signature) is fully intact. **The wall cannot convert the carrier-ratio Lissajous into a
topological pin.** (The classifier is correlation-based precisely to be masquerade-proof: a strong
wall adds its own frequency to the ω-sector, shrinking `ratio_spread` — a spread-only test could be
fooled into a false "pinned"; the correlation cannot.)

## 2. THE BARRIER (Arm 4) — VERBATIM

Adiabatic homotopy θ_λ = (1−λ)·(2φ+3ψ), λ: 0 (fully wound) → 1 (unwound). H_conf(λ) = elastic
gradient energy (native K4 L_D) + reactive wall storage V_clamp.

- H_conf(wound) = **9693.6** → H_conf(unwound) = **8844.6** (engine units) — unwinding is **DOWNHILL**.
- **barrier height = 0.0** (max climb along the path) · **budget = 540.1** (free-evolution wall fluctuation) · **barrier > budget = False** · **downhill = True**.

There is no energy hump to climb; untying the knot is energetically FAVORABLE, not costly. The
reactive confinement wall stores energy losslessly but installs **no** topological protection.

## 3. THE HOLD (Arms 1, 2) — VERBATIM

- **Arm 1 (free, wall OFF, winding OFF):** real-space |Q_link,raw| 2.993 → ~0 (drop **2.993**), `channel_open = True`. The reconnection channel is demonstrably OPEN — the test is NOT vacuous.
- **Arm 2 (confined, wall ON, winding ON):** |Q_link,raw| 2.993 → −0.005 (drop **2.988**), `holds = False`, `integer_stable = False`. The confined winding disperses essentially as much as the free one.

## 4. THE SINGLE MECHANISM (why all three failed together)

On a lossless (unitary) evolver a reconnection-CAPABLE director's winding is carried by the
OFF-DIAGONAL spatial-hopping operator `L_D` (the native K4 Laplacian), which necessarily SMEARS the
direction field (dispersion). A reactive confinement potential is a REAL DIAGONAL term — it adds an
on-site frequency but **cannot counteract the off-diagonal hopping** that smears the winding.
Therefore:
- it installs **no barrier** (unwinding lowers the gradient energy — downhill),
- it does **not hold** the real-space winding (the hopping smears it regardless), and
- it does **not pin** the phase-space ratio (a spatial potential shifts the ω-sector frequency but
  leaves it carrier-dependent — the ratio stays monotonic in ω_b/ω_s).

The only "hold" available is the `rigid_template` FROZEN-ê_w tautology (conserved by construction),
which is a data-structure artifact, not physics. **There is no middle regime "confined-but-
reconnection-capable holds" — that is the deep result.** Confinement does not rescue the (2,3) from
being either a frozen bookkeeping label OR a carrier-ratio Lissajous.

## 5. THE IMMUNE SYSTEM (every discipline gate — reported honestly)

| Gate | Status | Evidence |
|---|---|---|
| Arm-1 liveness | **PASS** | channel_open=True (drop 2.993); the test is not vacuous |
| Energy conservation (H-drift < 1e-5) | **PASS** | Arm 1 = 7.5×10⁻¹¹, Arm 2 = 1.3×10⁻¹⁰, Arm 3 all conserved (~1e-11–1e-10). No damping faked a hold. |
| Firewall (no α/m_e on verdict path) | **PASS** | AST scan of 11 verdict-path functions — 0 hits |
| Scale-invariance (V_yield vs 2×V_yield) | **PASS** | tracks/tracks; correlation bitwise-identical (0.9002405452289725 both) — the whole seed scales with V_yield ⇒ every arg() is scale-invariant; V_yield's Volts divide out |
| BC-not-bulk | **PASS** | wall = Op17-bounded moving-front reactive V_clamp analog (Hermitian on-site potential), `wall_form="omega_front"`; NOT the singular bulk `_reflection_density` term |
| Phase-space locus | **PASS** | Clifford-torus reader: toroidal arg(Σ a_A1), poloidal arg(Σ ê_w·a_w) |
| Bin-liveness | **PASS** | ECHO / PROTECTED / NOT-PROTECTED all reachable by the routing (synthetic-barrier control routes PROTECTED; wall-off routes NOT-PROTECTED) |
| Detuning-can-fire | **PASS** | gate reports "tracks" on the #417 config AND "pinned" on a synthetic phase-locked config |

## 6. HONEST WOBBLES (reported, not smoothed)

- **Dispersive-primary read is noisier than the rigid read.** The `dispersive_vector` poloidal phase
  arg(Σ ê_w·a_w) involves vector-field cancellations, so its detuning points are slightly
  non-monotonic (1:1 → 0.546 sits below 2:3 → 0.600) and `track_residual`=0.316. The classification
  is nonetheless unambiguous (correlation 0.900 > 0.7) and is corroborated by the two CLEAN rigid
  reads (corr 0.972 wall-off, 0.920 wall-on). The verdict does not hinge on the noisy read.
- **Wall realization (BC-not-bulk flag, from the prereg).** The literal
  `CosseratField3D.use_impedance_boundary` is a velocity-Verlet clamp on a different (JAX Cosserat
  u/ω) representation whose Meissner Γ=−1 needs the asymmetric (S_μ,S_ε) split, and whose hard-clamp
  cannot pass the "energy-conserving (unitary)" HARD gate (its own docstring reports ~1e4–1e5×
  runaway at default dt). On the unitary spine the wall is the reactive V_clamp analog
  (`cosserat_field_3d.py:1920`) keyed on the |ω|-front proxy — the correspondence is the V_clamp
  term; the μ/ε provenance is replaced. Stated, not smoothed.

## 7. DISPOSITION

The electron-lock effort is now closed across BOTH loci and the barrier:
- REAL-SPACE winding HOLDS-but-INERT (S1) / DISPERSE-FALSIFIED coupling (S3);
- PHASE-SPACE winding = carrier ratio (#417);
- **BARRIER: genuine confinement installs no lossless topological barrier (this doc).**

**Reading B closes NEGATIVE.** The electron's mass-persistence is NOT rescued as a confinement-
pinned reconnection barrier on this engine. Per Rule 12 / substitution-not-retraction: the slot is
RETRACTED, not refilled — no new pinning hypothesis is minted here. mass = A1 (#260) and charge =
Link(∂Ω,F) ∈ ℤ (static topology) stand un-walked-back.

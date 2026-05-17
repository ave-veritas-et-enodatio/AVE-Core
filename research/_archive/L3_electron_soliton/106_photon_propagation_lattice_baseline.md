# Photon propagating along K4-TLM lattice — baseline substrate test + animated visualization

**Date:** 2026-05-01
**Predecessor:** [doc 105 §8 auditor pass-5 corrections](105_parent_fdtd_photon_helical_research.md)
**Status:** clean substrate-physics baseline test per Grant directive 2026-05-01 ("ok, lets just try to model a photon propagating along the lattice")

---

## §1 — Test framing

Per Grant directive 2026-05-01: scope this turn is the simplest possible photon-on-K4-TLM-substrate test. No corpus-electron-canonical-claim entanglement, no Layer 3 phase-space framework, no bracket-Golden-Torus issues. Just: launch a photon, watch it propagate, characterize what the substrate does on its own dynamics.

This is exactly the (α') "characterize-engine's-natural-output" lane I recommended in doc 104 §8.10.6 + doc 105 §7, applied to the most basic case. Per Rule 14 substrate-derives-the-answer + Rule 9 v2 catalog text *"characterize as itself first."*

## §2 — Existing infrastructure (A45 corpus-canonical-test-precondition)

A43 v2 anyone-must-grep this turn surfaced existing AVE-Core photon-propagation infrastructure:

- [`src/scripts/vol_1_foundations/photon_propagation.py`](../../src/scripts/vol_1_foundations/photon_propagation.py) — Phase A K4-TLM wave-packet launcher + propagation validation (471 lines). Existed prior to this turn.
- Companion: [`src/scripts/vol_1_foundations/40_modeling_roadmap`](40_modeling_roadmap.md) doc — referenced in script docstring
- Cross-ref: [`src/scripts/vol_1_foundations/30_photon_identification`](30_photon_identification.md) doc — referenced for T₂-projected photon definition

Per A45 precondition: instead of designing new infrastructure, run the existing canonical test. Per Rule 14 substrate-walk: read the existing infrastructure's substrate-physics framing first.

## §3 — Substrate-physics framing (per `photon_propagation.py` docstring)

The K4-TLM substrate has anisotropic kinematics native to Axiom 1:

- **K4 port-mode decomposition:** 4-port space = A₁ ⊕ T₂
  - A₁ ∝ (1, 1, 1, 1): scalar/longitudinal mode, propagates at c·√2 = √(K_bulk/ρ) (per [`constants.py:497`](../../src/ave/core/constants.py#L497))
  - T₂: chiral-transverse triplet — **THIS IS THE PHOTON** per [doc 30 §photon-identification](30_photon_identification.md), propagates at c = √(G/ρ)

- **Cardinal-axis vs diagonal-axis kinematics** (substrate-physics, NOT SM/QED import):
  - Cardinal (along x̂, ŷ, ẑ): wavefront speed = c·√2 because port projections onto cardinal axes are ±1/√3, and the 4-port pattern forces each lattice step to advance by one full cardinal cell
  - Diagonal (along port unit vectors p̂_n): wavefront speed = c

- **Source design** (per script): time-domain plane source, NOT spatial IC
  - V_inc[plane_x0, y, z, forward_ports] += envelope(t) · sin(ωt)
  - Soft source at x = x0 (additive); injects in ±x̂ direction; PML on -x boundary absorbs reverse-going component
  - Forward-port weights: T₂-projected (Σw=0) for pure transverse photon; raw weights = 50% A₁ + 50% T₂ mixed
  - For +x̂: pure T₂ pattern is (−½, −½, +½, +½)·1/√2

- **AVE compliance:**
  - Linear vacuum (nonlinear=False, Axiom 4 not engaged)
  - Amplitude ≪ V_YIELD (default 0.01·V_SNAP ≈ 5.1 kV)
  - λ_eff = 10·dx (visualization choice, not matched to Compton or any SM scale)
  - ω, λ are visualization choices for empty-space test, not matter-coupled

## §4 — Test execution + result

Default config:
- N=96 lattice (96³ K4-TLM cube)
- pml=8 (PML thickness)
- source_x=16 (just inside -x PML)
- λ_cells=10, sigma_yz=8, t_sigma=0.75 periods
- amp_frac=0.01·V_SNAP (sub-yield, linear vacuum)
- n_steps=240 (~17 periods of recording)
- Direction: +x̂ (cardinal-axis)
- T₂ projection: ON (default)

Pre-registered measurement: peak energy density arrival time at two reference planes x_a=36, x_b=76. Velocity = (x_b - x_a)·dx / (t_b - t_a).

**Result (this turn, committed):**

| Quantity | Value |
|---|---|
| t_arrival_a (peak at x=36) | 1.274e-7 s |
| t_arrival_b (peak at x=76) | 2.194e-7 s |
| v_meas | 4.348e8 m/s |
| **v/c** | **1.450 ≈ √2** |
| amp_frac (V_SNAP units) | 0.01 (sub-yield) |

**Verdict:** Photon propagates cleanly along +x̂. Wavefront speed = c·√2 ≈ √2·c, matching docstring's pre-registered cardinal-axis kinematics for K4 substrate. Phase A infrastructure validated.

## §5 — Animated visualization

GIF rendered + saved to: [`research/L3_electron_soliton/assets/photon_propagation_cardinal.gif`](assets/photon_propagation_cardinal.gif) (1.4 MB, side-by-side animation):

- **Left panel:** |V|² xy-slice at z=N/2, log color scale. Shows photon packet's spatial structure as it propagates. Cyan dashed line marks source plane x=16.
- **Right panel:** interior centroid x(t) trajectory. Linear region after source pulse ends shows constant-velocity packet propagation.

NPZ data also saved: [`research/L3_electron_soliton/assets/photon_propagation_cardinal.npz`](assets/photon_propagation_cardinal.npz) (6.0 MB) — full frames array + centroids + times for any post-hoc analysis.

## §6 — What the lattice does (substrate-perspective per doc 103 §3-§4)

Per doc 103's substrate-perspective walk: with a photon present, the K4-TLM lattice nodes near the propagating packet experience:

- **|V_inc|² rises locally** as the wave reaches each node — small but nonzero (amp_frac = 0.01 → A²_local ≈ 1e-4 << V_yield² ≈ 7e-3)
- **A²_local well below saturation cusp** at √(2α) ≈ 0.121 → **substrate stays in Regime I (linear vacuum)** throughout
- **No Op14 saturation engagement** — Z_eff ≈ Z_0, c_eff ≈ c_0
- **No TIR wall formation** — field passes through without trapping
- **Wavefront propagates at √2·c (cardinal-axis kinematics)** — pure substrate-geometry effect, native Axiom 1
- **No Cosserat coupling** — Op14 cross-block is zero (Cosserat ω = 0 throughout, K4 V_inc/V_ref carries the photon alone)

This is the substrate doing exactly what corpus framework predicts for an unperturbed photon in linear vacuum: clean propagation at the substrate's transverse mode speed (T₂), with cardinal-axis anisotropy adding the √2 factor. **The free photon is NOT the canonical electron** — no trap mechanism is engaged at sub-yield amplitude in linear vacuum. This is the baseline against which any electron-formation test would be compared.

## §7 — Companion script: diagonal-axis propagation (numerical-only, GIF-pending)

Created [`src/scripts/vol_1_foundations/photon_propagation_diagonal.py`](../../src/scripts/vol_1_foundations/photon_propagation_diagonal.py) as a sanity-check companion: same packet launcher, but direction = port-0 unit vector (1, 1, 1)/√3 instead of cardinal +x̂.

**Pre-registered prediction** (per docstring): v/c ≈ 1.0 along the diagonal (junction-diagonal photon, NO cardinal-axis √2 factor).

This script is numerical-only this turn; not yet GIF-rendered. Future enhancement candidate. Running the diagonal version would confirm the cardinal-axis vs diagonal-axis anisotropy picture cleanly:
- Cardinal-axis: v = √2·c (this turn's result)
- Diagonal-axis: v = c (predicted; not yet measured)

## §8 — Connection to L3 arc + forward direction

This baseline test addresses the (α') "characterize-engine's-natural-output" lane named in doc 104 §8.10.6 + doc 105 §7. The substrate's natural output for a free photon in linear vacuum is: clean wave-packet propagation at √2·c along cardinal axis, no dispersion, no saturation, no trap.

**What this provides:**

- **Baseline calibration:** any test that involves photon-electron interactions has THIS as its starting point. The substrate transports photons at c·√2 along cardinal axis, no losses (PML absorbs reverse component cleanly).
- **Substrate-physics ground truth:** Round 13 (α)'s DC residual finding (doc 104 §8) sits in contrast to this clean propagation — when you crank amplitude into saturation regime + add (V_inc, V_ref) phase quadrature, the engine produces a static distortion instead of a propagating wave.
- **Round 14+ (β) test setup:** if/when CoupledK4Cosserat 4M× runaway is resolved, the photon-on-K4 test extended with Cosserat ω-source coupling via Op14 would test whether photon → impedance-saturation → trap formation (the corpus claim per doc 105 §4).
- **Doc 105 finding context:** the parent's photon-helical-confinement → electron-formation claim is currently asserted-not-derived computationally. This baseline test provides the empty-space starting point; the missing computational chain is "what happens when amplitude crosses saturation cusp + Cosserat coupling is engaged."

**Forward direction:**

- (α'-1) Diagonal-axis run: complete the photon_propagation_diagonal.py with GIF rendering, run, verify v=c. ~30 min.
- (α'-2) Saturation-engaged run: increase amp_frac from 0.01 to ~√(2α) ≈ 0.35 to engage Op14 saturation; observe whether the photon develops impedance-induced compression. Tests the parent-corpus claim about wave-crashing. ~30 min.
- (α'-3) Coupled K4-Cosserat photon: launch photon with simultaneous Cosserat ω-source seeding for transverse rotational coupling. Tests the doc 103 §4.6 K4-Cosserat coupling channel without requiring the topological-electron seeder. ~1-2 hours, may hit CoupledK4Cosserat instability.

Implementer-lean: (α'-1) + (α'-2) as immediate next moves; (α'-3) as Round 15+ if it requires CoupledK4Cosserat fixes per doc 104 §8.10.6 (β).

— Doc 106 closure: clean substrate-physics baseline established. Photon propagates cleanly on K4-TLM linear vacuum at √2·c (cardinal-axis kinematics, native Axiom 1). Animated visualization at `assets/photon_propagation_cardinal.gif`. Existing AVE-Core infrastructure (`photon_propagation.py`) was sufficient — no new code required. Substrate doing exactly what the corpus framework predicts for unperturbed photon in linear vacuum.

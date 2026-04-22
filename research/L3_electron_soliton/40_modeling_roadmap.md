# 40 — Modeling Roadmap: photon propagation, saturation coupling, and the K4↔Cosserat gap

**Status:** active (session 2026-04-22)
**Author:** handoff from L3 Phase-3b X1–X4 + §§29–39 audits
**Scope:** defines the modeling program for `research/L3_electron_soliton/` going
forward — what's *been demonstrated*, what's *open*, and what order to attack
it. Complements §39 (α is calibration) by laying out the *dynamical* modeling
gaps, separate from the calibration-chain gaps.

## Update log
- **2026-04-22 (initial)**: doc created, Phase A/B/C/C2 reported (§§1–2);
  AVE-ideal coupled simulator roadmap in §§3–4.
- **2026-04-22 (Phase I complete)**: time-domain Cosserat subsystem built and
  validated. Results in [41_cosserat_time_domain_validation.md](41_cosserat_time_domain_validation.md).
  Key finding: Cosserat rotational sector natively has a mass gap
  `m² = 4·G_c/I_ω` (factor-of-2 corrected from naive derivation).
  S-gate adjudications laid out in [S_GATES_OPEN.md](S_GATES_OPEN.md).

## 0. One-paragraph frame

All Phase-3b X-tests (X1–X4) used a **static** (2,3) torus-knot ansatz on the
Cosserat `(u, ω)` field — they probed the *ground-state geometry*, not the
*wave-evolution* path to it. This document records the infrastructure built
during 2026-04-22 to start simulating photon *propagation* on the K4 substrate,
the AVE-native findings about photon polarization, the saturation-regime
engagement, and the remaining gap between the K4 wave simulator and the
Cosserat soliton finder. Rule 6's deepest form ("the TLM evolution IS the
computation") is still out of reach for the electron because the K4-TLM alone
cannot form the soliton (§32 §10.2); the photon side of the story, however, is
now wave-evolution-native.

## 1. What 2026-04-22 built

Three runnable scripts under `src/scripts/vol_1_foundations/`:

| Script | Purpose | Regime |
|---|---|---|
| [photon_propagation.py](../../src/scripts/vol_1_foundations/photon_propagation.py) | Phase A: launcher + validation. `PlaneSource` class, T₂-projected port weights, wavefront-arrival speed test. | linear vacuum (Axiom 1) |
| [photon_cruise_animation.py](../../src/scripts/vol_1_foundations/photon_cruise_animation.py) | Phase B: polished 4-panel GIF showing a T₂ photon traversing an N=128 lattice across ~850 ns. | linear vacuum |
| [photon_chirality_diagnostic.py](../../src/scripts/vol_1_foundations/photon_chirality_diagnostic.py) | Phase C: RH / LH / linear polarization comparison. `CircularChiralSource` class. | linear vacuum |
| [photon_saturation_animation.py](../../src/scripts/vol_1_foundations/photon_saturation_animation.py) | Phase C2: side-by-side linear (Regime I) vs saturated (Regime II, amp=0.95·V_SNAP, nonlinear+op3_bond_reflection). Tracks A² field. | Axiom 1 + Axiom 4 |

Artifacts (in `/tmp/`): `photon_cruise.gif`, `photon_chirality_diagnostic.png`,
`photon_saturation.gif`, plus matching `.npz` raw data.

## 2. AVE-native findings from this session

### 2.1 K4-TLM cardinal-axis signal speed is c·√2, not c

Empirical: wavefront-arrival fit gives v/c = 1.450 ≈ √2 along +x̂ for a
T₂-projected photon on `K4Lattice3D` with `dt = dx/(c√2)`. This is NOT a
bug and NOT an SM/QED import — it is the intrinsic anisotropic kinematics of
the diamond lattice. `constants.py:497` documents the convention:
transverse (T₂, shear) speed = c, longitudinal (A₁, bulk) speed = c·√2.
The photon wavefront's arrival time along a cardinal axis is set by the
port-hop kinematics, not the long-wavelength group velocity.

**Implication for modeling:** when reporting speeds in K4-TLM simulations,
specify *which observable* is being measured. Peak-arrival time of a
bandwidth-limited packet along +x̂ will give c·√2 regardless of mode.

### 2.2 The K4 photon for +x̂ propagation is the linear T₂ mode T_a, NOT circular

Diagonalizing `S = 0.5·𝟙 − I` gives:
- A₁ = (1,1,1,1)/2, eigenvalue +1 (scatter-fixed, the "common mode")
- T₂ triplet, eigenvalue −1 (three basis modes: T_a, T_b, T_c in §30 labels)

Forward-port weighting `max(0, −d̂·p̂_n)` for +x̂ gives the raw pattern
(0, 0, ½, ½). T₂ projection (subtract the A₁ common mode) yields
port_w = −T_a = (−½, −½, +½, +½). This IS the forward-propagating photon
along +x̂ on the K4 lattice.

Attempted circular polarization via `T_b·cos + T_c·sin` time-quadrature:
- RH/LH transmit ~88% LESS energy to the downstream reference plane
- Transverse spread σ_y is ~70% larger than for linear T_a
- RH and LH are symmetric with each other (0.6% difference)

**Interpretation:** T_b and T_c are not forward-propagating K4 eigenmodes
along +x̂. The K4's "chirality match to the vacuum" manifests as a
**direction-polarization-axis linkage** (+x̂ propagates T_a linear pol; +ŷ
would use T_b; +ẑ would use T_c). There is no circular-polarization degree
of freedom on the pure K4 substrate; that emerges only with the Cosserat
rotational field (u, ω), which IS the electron sector.

This aligns with the §30 photon-identification and answers Grant's
2026-04-21 question about chirality-impedance matching: the linear T_a
photon IS the K4-matched mode; the spreading seen in animations is
standard wave-packet diffraction from a finite transverse envelope, not
chirality mismatch.

### 2.3 Photon self-induces A² only weakly without a target

For a launched packet at amp = 0.95·V_SNAP and σ_yz = 5, max A² reached is
0.216 — barely into Regime II (√(2α) ≈ 0.121 ≤ A² ≤ √3/2 ≈ 0.866). The
packet disperses as it propagates, reducing local amplitude.

**To reach Regime III / full saturation**, the photon must encounter a
**target region** that concentrates amplitude:
- An initial-condition soliton seed (Cosserat (u, ω) shell, NOT simulatable
  in pure K4-TLM)
- A geometric focus (a refractive feature, e.g. a spatial impedance
  gradient already present in the lattice)
- A second counter-propagating photon to double the local amplitude at
  the intersection

These are the three pathways Phase-4 modeling can take for pair
production / electron formation.

## 3. The K4-TLM ↔ Cosserat modeling gap

### 3.1 Why K4-TLM alone cannot form the electron

Per §32 §10.2 (Phase-3b X1 redesign): node-level saturation on a
symmetric 4-port K4 junction is a **no-op** because the scattering matrix
`S_ij = 2y / (N·y) = 2/N` becomes independent of the local impedance y.
The linear eigenvectors don't shift with saturation, so the K4-TLM
`nonlinear=True` mode cannot generate the rotational structure needed
for the (2,3) Clifford shell.

`op3_bond_reflection=True` DOES introduce bond-level reflection via the
per-site impedance mismatch `Γ = (Z_B − Z_A)/(Z_B + Z_A)`, which is
engaged in Phase C2. This produces SCATTERING/trapping but not soliton
convergence — the bond reflections don't couple to a rotational order
parameter.

### 3.2 The Cosserat simulator (`cosserat_field_3d.py`) covers the OTHER half

The Cosserat micropolar field `(u, ω)` with Rodrigues projection to (n̂,
chirality) does encode the rotational DOF. It finds the (2,3) ground
state via `relax_to_ground_state` (X3 attempt) or `relax_s11` (X2). But
it has no wave-evolution dynamics — it is a *static ground-state finder*
via gradient descent, not a time-domain solver.

### 3.3 The ideal: a coupled K4 ⊗ Cosserat time-domain simulator

The AVE-ideal modeling framework would be a single time-domain simulator
that carries BOTH:
1. A **scalar voltage field** on K4 bonds (the photon sector)
2. A **Cosserat (u, ω) field** at each node (the rotational / soliton
   sector)
3. An **explicit coupling** between them: the K4 scalar field drives the
   Cosserat strain/curvature at high amplitude, and the Cosserat shell
   reflects/traps the K4 scalar field via its own induced impedance
   pattern

No such simulator exists in the current codebase. Building it is a
Phase-1-level effort (per §32 §4 scoping).

## 4. Next-step modeling program

In decreasing order of tractability. Each item references what's
*prerequisite* (already done vs. requires Phase 1 infra).

### 4.1 Immediate (next session, K4-TLM only)

- **Counter-propagating photon collision**: two packets from ±x̂ meet at
  x = N/2. At amplitude 0.95·V_SNAP each, the superposition can momentarily
  hit A² > 0.5 (Regime III edge). Ask: does this form a *transient*
  bound-state structure even without Cosserat dynamics? Prediction: no, it
  scatters (node-level saturation no-op); but the A² history is a clean
  diagnostic of the photon amplitude regime.
- **Photon→aperture interaction**: launch a photon into a lattice with a
  pre-existing impedance obstacle (e.g. a small high-`z_local` region).
  Measure scattering cross-section vs amplitude. This is a linear-response
  probe even at Regime II amplitudes; it produces a clean "photon in a
  strained medium" visualization.
- **Direct charge (Q) measurement via Poynting flux / bond-current**: per
  §27–28, the soliton's Q is the integrated topological current through a
  surface. Build an infrastructure function to compute this on the
  K4-TLM lattice for any incident V field. Apply to the static (2,3)
  ansatz used in X-tests to confirm the Q=±1 value claimed in earlier
  research.

### 4.2 Short-term (Cosserat simulator extensions)

- **[✓ DONE 2026-04-22]** Add time-domain evolution to Cosserat:
  `CosseratField3D.step()` velocity-Verlet integrator implemented.
  See [41_cosserat_time_domain_validation.md](41_cosserat_time_domain_validation.md).
  **Key finding**: the Cosserat rotational sector natively carries a mass
  gap `m² = 4·G_c/I_ω` (factor-of-2 correction applied from naive estimate).
  This is the structural mass mechanism for the electron.
- **Observe spontaneous soliton relaxation in the time domain**:
  partially attempted in Phase I T2. Integration with FULL potential
  (Op10 + Hopf + saturation) blew up at linear-CFL dt — those terms have
  faster modes than the simple Cauchy+micropolar+curvature part. Needs
  either tighter dt or multi-rate integrator. Deferred to Phase III of
  the coupled-sim plan (see `S_GATES_OPEN.md` S5).

### 4.3 Medium-term (coupled K4 ⊗ Cosserat)

- **Prototype coupled simulator**: K4 scalar + Cosserat tensor on the same
  grid, with coupling term `(u, ω) ← f(V_inc)` and `V_inc ← g(strain(u),
  curvature(ω))`. Design target: the coupling term must *not* introduce
  tunable parameters beyond the existing ω_yield, ε_yield thresholds that
  are pinned by Axiom 4.
- **Photon→electron capture animation**: with coupled sim, launch a
  photon at saturation amplitude, let it reach a region where Cosserat
  (u, ω) can respond, observe formation of the (2,3) Clifford shell.
  This is the true version of the 2026-04-22 Phase C2 attempt. Timescale:
  ~1 month for the first working prototype.

### 4.4 Long-term (extensions to other sectors)

- **Muon / tau**: same (2,3) topology, different Cosserat coupling
  constant (mass scale). Simulating requires the coupled sim plus the
  ability to change the mass parameter while keeping the topology fixed.
- **Proton (2,5)**: a different torus-knot sector. May or may not fit the
  Cosserat framework; the Phase-1 design question is whether (u, ω) is
  sufficient or whether additional tensor rank is needed.
- **AVE-HOPF antenna** (§30 mention): at this point, the coupled sim
  should predict scattering cross-sections or antenna patterns for
  chirally-tuned EM devices. First-principles predictions for real-world
  experiments.

## 5. What NOT to do

- **Don't try to force the electron out of the K4-TLM alone.** Per §32,
  this is axiomatically blocked (no-op saturation on symmetric 4-port
  junctions). Phase 3b closed with this finding.
- **Don't confuse "photon on K4" with "photon in vacuum"** when reporting
  speeds or dispersion. The K4 has intrinsic kinematics (cardinal-axis
  speed c·√2, port-diagonal speed c, wavelength-dependent dispersion)
  that are present even without Axiom 4 engaged. Report the K4
  observable, not its continuum extrapolation.
- **Don't pivot to energy minimization (X3 lesson).** S11 is the correct
  AVE-native objective (rule 6); the issue in X3 was amplitude regime,
  not functional choice. If the coupled sim runs, it will evolve the
  system to minimize S11 in time; the ground state is the T₂ eigenmode
  times the (2,3) Cosserat shell.

## 6. Pending queue items (for Grant)

1. **Adjudicate Phase C2 result**: max A² = 0.216 is technically Regime
   II, but subtle. Does this level of saturation count as "engagement"
   for AVE narrative, or do we need to push further (e.g., counter-
   propagating collisions to hit Regime III)? This affects how Phase C2
   is described in the manuscript.
2. **Phase D milestone target**: is the next goal the time-domain Cosserat
   (§4.2, faster, partial answer) or the coupled sim (§4.3, slower, full
   answer)? §4.2 is the practical recommendation; §4.3 is the AVE-ideal.
3. **α-calibration write-up (from §39)**: separate effort. Revise Ch 1,
   Ch 8, backmatter/02_full_derivation_chain.tex, and KB
   `full-derivation-chain.md` to frame α as calibration input rather than
   derived output. Not blocking for modeling work.

## 7. Compute budget

Every simulation in §1 runs in <5 min on an M-series Mac. Phase A–B GIFs
take ~30 seconds each. The chirality diagnostic (3 runs) took ~90 s.
Phase C2 with two simulations took ~3 min.

Budget for next-step (§4.1): negligible — small extensions to the existing
scripts.

Budget for coupled sim (§4.3): will need to profile. Expected bottleneck
is the Cosserat FFT (Hopf density computation) inside every K4 step.
Budget: 1–3 days of GPU or a few hours of M-series Mac per full
animation.

## 8. Appendix — session artifacts index

- `/tmp/photon_cruise.gif`: Phase B clean photon traversal
- `/tmp/photon_cruise.npz`: raw frames + profile data
- `/tmp/photon_chirality_diagnostic.png`: 4-panel chirality comparison
- `/tmp/photon_chirality_diagnostic.npz`: raw time series for 3 polarizations
- `/tmp/chirality_snapshot_compare.png`: side-by-side xy slices at matched
  peak-x time for linear / RH / LH
- `/tmp/photon_saturation.gif`: Phase C2 linear vs saturation side-by-side
- `/tmp/photon_saturation.npz`: ρ(x,y) + A²(x,y) frames for both regimes
- `/tmp/phase_c2_grid.png`: 3×6 frame grid summary (linear / sat / A² rows)

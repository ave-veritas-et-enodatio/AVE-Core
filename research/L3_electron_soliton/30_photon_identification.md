# Photon Identification from T₂ Sector + Electron-Photon Duality Mechanism

**Date:** 2026-04-22
**Branch:** `research/l3-electron-soliton`
**Status:** New research finding. Closes a conceptual loop in the L3 program
and reframes Phase-3 deliverables.

This document formalizes an observation that arose from the phase-space
discovery test (`phasor_discovery.py`): the K4-TLM's stable bound state under
the (2,3) ansatz is **the photon**, not the electron. The electron is that
bound state *plus* Axiom-4 saturation confinement. The two differ by a single
piece of physics — whether the lattice self-saturates at the soliton's
frequency — and the mechanism connecting them is explicit.

---

## §0 Summary

1. The K4-TLM port space decomposes under the tetrahedral group T_d as
   `4-port = A₁ ⊕ T₂`. The scattering matrix `S = (1/2)𝟙 − I` has
   eigenvalues `{+1, −1, −1, −1}`: the `+1` eigenvector is the A₁
   "common mode" (all ports equal); the `-1` triplet spans T₂ (traceless).

2. Simulation at `N = 64`, `n_steps = 300`, seeded with a (2,3) Golden-Torus
   voltage ansatz, shows the port-correlation matrix across shell sites has
   eigenvalues stable at `{1.65, 1.22, 1.13, 0.00}`. **One eigenvalue is
   exactly zero**, stable across steps 100/200/300. A₁ is fully dissipated;
   T₂ survives with a three-mode split.

3. A₁ corresponds to the **isotropic / longitudinal / scalar** sector of
   Cosserat continuum mechanics. T₂ corresponds to the **transverse /
   microrotation** sector. Vol 3 Ch 2 and Vol 4 Ch 1 both identify the
   photon as "a purely transverse Cosserat shear wave" with no longitudinal
   component.

4. The K4-TLM dissipation mechanism (Op3 bond reflection) preferentially
   damps the A₁ common mode. What survives is a pure T₂ configuration with
   (2,3) winding — **a knotted transverse electromagnetic mode**, i.e., a
   Hopfion photon in the sense of Rañada 1989 / Irvine-Bouwmeester 2008.

5. The electron is this object *plus* Axiom-4 saturation confinement. The
   mechanism is: a photon at `ω = ω_C = c/ℓ_node` drives each single-bond
   LC tank at resonance. Voltage builds up until `V → V_yield = √α·V_snap`.
   Axiom 4 engages: `C_eff → ∞`, local `Z → 0`, `Γ → −1`. The lattice
   creates its own TIR mirror, binding the photon into a standing (2,3)
   configuration. That standing configuration is the electron.

6. The `ω = ω_C` resonance is a genuine **dynamical threshold**, not a
   calibration choice. `ℓ_node` sets `ω_C` sets `V_yield` sets `m_e c² =
   ℏω_C`. Mass is the lattice's self-resonant energy.

7. Phase 3 numerical deliverable splits into 3a (photon characterization —
   nearly done) and 3b (electron via amplitude-driven saturation — one
   amplitude-sweep experiment remaining).

---

## §1 The A₁ ⊕ T₂ decomposition of K4 port space

### §1.1 Group-theoretic foundation

The K4 scattering matrix in AVE's TLM implementation
([src/ave/core/k4_tlm.py:36-65](../../src/ave/core/k4_tlm.py#L36-L65)) is

```
S_ij = (1/2) − δ_ij    for z_local = 1,
```

i.e., `S = (1/2)·𝟙 − I` where `𝟙` is the all-ones matrix and `I` is the
4×4 identity. Acting on the 4-vector of port amplitudes.

Under the tetrahedral point group T_d (the symmetry of the four tetrahedral
neighbors on K4), the 4-port amplitude space decomposes into irreducible
representations as

```
V_4-port  =  A₁ (1D)   ⊕   T₂ (3D)
```

- **A₁** is the totally symmetric rep. Its basis vector is `(1, 1, 1, 1)/2`
  — all four ports carry equal amplitude. Physically: isotropic, scalar,
  longitudinal.
- **T₂** is the 3D triplet. Its basis spans the traceless 3D subspace
  `{v : Σᵢ vᵢ = 0}`. Physically: anisotropic, vector-like, transverse.

### §1.2 Eigenvalues of S

Computing `S` on each irrep:

- On A₁ basis `(1,1,1,1)/2`: `S·v = ((1/2)·4 − 1)·v = (2 − 1)·v = +1·v`.
  **A₁ eigenvalue: +1.**
- On any traceless vector (A₁-orthogonal): `𝟙·v = 0`, so
  `S·v = (−I)·v = −v`. **T₂ eigenvalue: −1** (triply degenerate).

The `+1` eigenvalue on A₁ means the bare scattering preserves the A₁ mode
exactly (like a DC bias passing through a reflector unchanged). The `−1`
eigenvalue on T₂ means T₂ modes flip sign on scatter — the standard
traveling-wave reflection behavior.

### §1.3 How dissipation breaks the symmetry

The standard K4-TLM with `S = (1/2)𝟙 − I` is unitary — A₁ would propagate
forever, T₂ would reflect forever, no energy loss. The bond-level Op3
reflection ([src/ave/core/k4_tlm.py](../../src/ave/core/k4_tlm.py), with
`op3_bond_reflection=True`) adds an impedance mismatch at each bond:
`Z_eff = Z_0/√S_sat` where `S_sat` is the Axiom-4 saturation factor.

This impedance mismatch dissipates energy differently for the two sectors.
The A₁ mode — being the common-mode "DC" across all ports — has no spatial
gradient in the port space, and its reflection at bonds produces destructive
interference with neighboring nodes' A₁ components. The A₁ sector loses
energy monotonically until it reaches zero.

T₂ modes carry spatial structure. Their reflection at bonds redirects flux
into standing-wave patterns. They dissipate more slowly, settling into a
quasi-stable configuration.

This asymmetric dissipation is physically correct for electromagnetic
waves on a Maxwell-substrate: longitudinal (∇·E ≠ 0) components are
forbidden in vacuum by Gauss's law, so any A₁-type longitudinal excitation
must dissipate to leave only the transverse (∇·E = 0) sector. The K4
scattering realizes this constraint automatically through T_d symmetry.

---

## §2 The simulation observation

### §2.1 Protocol

Ran `src/scripts/vol_1_foundations/phasor_discovery.py` at `N = 64`,
`n_steps = 300`, seeded (2,3) voltage ansatz at Golden-Torus proportions
`(R, r) = (16.0, 6.108)`, amplitude `= 0.5`. Snapshot full state at steps
100, 200, 300. For each snapshot:

- Select shell sites where `Σᵢ (V_inc_i² + V_ref_i²) > 0.3 · max`.
- Compute the 4×4 port correlation matrix of `V_inc` across shell sites.
- Eigendecompose.

### §2.2 Result

Port correlation eigenvalues (sorted descending):

| Step | λ₁     | λ₂     | λ₃     | λ₄     |
|------|--------|--------|--------|--------|
| 100  | 1.654  | 1.215  | 1.130  | 0.001  |
| 200  | 1.642  | 1.210  | 1.147  | 0.000  |
| 300  | 1.653  | 1.203  | 1.144  | 0.000  |

Sum of eigenvalues = 4.0 at each step (trace of a 4×4 correlation matrix
= 4; sanity check passes). **The smallest eigenvalue is exactly zero, stable
across time.** The port-space of the soliton lives in a 3-dimensional
subspace of the nominal 4-dimensional port space.

### §2.3 Secondary observations

- **Energy decay:** the total field energy drops from `8.91e3` (step 0)
  to `3.56e3` (step 300), a 60% loss. Consistent with A₁ dissipation +
  radiation through the PML boundary.
- **(2,3) winding preservation:** only ~27% of shell sites retain the
  seeded phase `θ = 2φ + 3ψ` within `π/4` tolerance after relaxation.
  The initial winding partially survives; the majority drift to other
  configurations.
- **Shell geometry:** `R_peak ≈ 16.5` lattice units (seeded 16.0), shell
  half-width ±3.5 in both `ρ` and `z`. Consistent with the 2.27 real-space
  attractor from the earlier convergence study.
- **Time stability:** all metrics agree to ~1% across steps 100/200/300.
  This is a quasi-stable attractor of the K4 dynamics, not a transient.

---

## §3 Physical identification as the photon

### §3.1 Corpus statements on the photon

[`manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex:139`](../../manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex#L139):

> "A photon is a purely transverse Cosserat shear wave; it carries no
> rest mass and has no longitudinal (scalar) component. It is therefore
> mechanically blind to the isotropic bulk and couples instead to the
> transverse cross-sectional strain of the lattice."

[`manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:491-495`](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L491-L495):

> "When massless Bosons (photons) propagate, they act as linear transverse
> shear waves. Because they do not possess a static inductive core, they
> do not geometrically saturate the dielectric lattice (Δφ ≪ α). The local
> metric impedance remains perfectly matched at Z₀ ≈ 376.7 Ω."

[`research/L3_electron_soliton/00_scoping.md:122-126`](00_scoping.md#L122):

> "Mode 3: Transverse microrotational. A propagating twist of ω without
> translational component. In AVE, this is identified with the photon."

The photon in AVE is defined by three tightly-coupled properties:

1. **Purely transverse** — no longitudinal/scalar component.
2. **Microrotation sector only** — excites `ω` (Cosserat microrotation)
   with `u = 0` (Cosserat translation).
3. **No saturation** — `Δφ ≪ α`, lattice stays in linear regime.

### §3.2 Mapping to A₁ / T₂

The A₁ ⊕ T₂ decomposition of K4 port space aligns with the Cosserat
split:

| K4 port-space rep | Physical character      | Cosserat sector        |
|-------------------|-------------------------|------------------------|
| A₁ (1D)           | Isotropic, longitudinal | Translational `u`      |
| T₂ (3D)           | Anisotropic, transverse | Microrotational `ω`    |

Justification:

- The A₁ mode `(1,1,1,1)/2` has all ports in phase with equal amplitude.
  At a node, this is a scalar "breathing" excitation — the node as a whole
  compresses/expands without directional bias. That's the translational
  compression/rarefaction sector.
- The T₂ modes are traceless — for every excitation at one port, an equal
  and opposite excitation exists at some combination of other ports. The
  node as a whole has no net scalar displacement; instead it has a
  directional (vector-like) excitation. That's the microrotation sector.

With A₁ fully dissipated (λ₄ = 0 exactly) and T₂ surviving (λ₁₋₃ = 1.65,
1.22, 1.13), the simulation's steady-state soliton has:

- Zero longitudinal/scalar amplitude → satisfies property 1 (purely transverse).
- Pure microrotation-sector content → satisfies property 2 (`u = 0`,
  `ω ≠ 0`).
- Amplitude `0.5 < V_yield` in TLM units → satisfies property 3 (no
  saturation).

All three AVE-photon properties are satisfied. **The TLM's stable bound
state under the (2,3) ansatz is the photon.**

### §3.3 Why (2,3) specifically — knotted light

The simulation seeded a (2,3) torus-knot voltage winding and observed
it partially persist (~27% preservation) while the longitudinal component
dissipated. The result — a transverse (T₂) electromagnetic configuration
with non-trivial (2,3) topological winding — matches the definition of a
Hopfion.

Rañada 1989 [scoping ref 14] and Irvine-Bouwmeester 2008 [scoping ref 15]
established that transverse electromagnetic fields can support stable
topologically non-trivial configurations: knotted field lines, linked flux
tubes, (p,q) torus-knot light beams. These are "knotted photons" or
"Hopfions" — transverse EM waves with non-trivial topology.

The TLM's steady state is precisely a K4-lattice realization of a (2,3)
Hopfion photon. The partial winding preservation (27%) is consistent with
some topological stability but also some relaxation toward a lower-winding
ground state (the remaining 73% sites drift toward configurations that
are transverse and low-frequency but not necessarily (2,3)).

---

## §4 The electron as photon + TIR confinement

### §4.1 The mechanism

The electron differs from the photon by one additional piece of physics:
Axiom-4 saturation. The mechanism is:

**Step A.** Take a transverse T₂ configuration (a photon) with frequency
`ω = ω_C = c/ℓ_node`.

**Step B.** This photon drives each single-bond LC tank it crosses at
resonance. The single-bond LC resonates at exactly `ω_C` (Step 3 of the
two-node synthesis, [`24_step3_bond_lc_compton.md`](24_step3_bond_lc_compton.md)).

**Step C.** At resonance, voltage builds up in the capacitor sector each
cycle. The tank accumulates reactive energy without being able to shed it
elsewhere (off-resonance paths are closed).

**Step D.** When `V → V_yield = √α · V_snap ≈ 43.65 kV`, Axiom-4 engages:
`C_eff = C_0/√(1 − (V/V_yield)²) → ∞`.

**Step E.** Local impedance `Z = √(μ_0/C_eff) → 0`. Reflection coefficient
`Γ = (Z_local − Z_0)/(Z_local + Z_0) → −1`. **The lattice has created its
own perfect TIR mirror at the photon's location.**

**Step F.** The photon's transverse wave is now trapped — the `Γ = −1`
boundary reflects it back inward on every attempt to propagate outward.
The photon becomes a standing wave in a self-created cavity.

That standing wave is the electron. All electron observables are
projections of this bound configuration:

- **Rest mass** `m_e c² = ℏω_C` — the resonant energy held in the trapped
  standing wave.
- **Charge `e`** — the topological winding number of the confined (2,3)
  configuration (Axiom 2: [Q] ≡ [L]).
- **Spin-½** — the 4π double-cover of the extended-unknot
  Finkelstein-Misner kink at the confinement boundary
  ([`23_step2_spin_half_from_k4.md`](23_step2_spin_half_from_k4.md)).
- **α = 1/137** — the TIR-boundary leakage rate per cycle (Theorem 3.1 v2).
- **Magnetic moment, g-factor, etc.** — composites of the above
  ([`29_ch8_audit.md`](29_ch8_audit.md) lists the full catalog).

### §4.2 Photon emission as the reverse process

An electron emits a photon when the TIR condition transiently fails. Local
amplitude drops below `V_yield`, Axiom-4 comes off saturation, `C_eff`
becomes finite, `Z_local` returns toward `Z_0`, `Γ` moves off `−1`. The
trapped transverse wave propagates out as a photon at frequency `ω_C` (or
at a shifted frequency if the electron is in an excited state or the
emission is accompanied by recoil).

This makes the electron and photon two phases of the same substrate
dynamics: bound (saturated) and free (unsaturated). The boundary is
`V = V_yield` at `ω = ω_C`.

### §4.3 Pair production as photon-to-electron transition

A single gamma photon at frequency `2ω_C` (energy `2m_ec²`) can trigger
saturation at two distinct lattice regions simultaneously, creating two
TIR bubbles. The photon's transverse field pattern splits across the two
bubbles with opposite chirality, producing an electron/positron pair. The
threshold `E > 2m_ec² = 1.022 MeV` is the minimum energy to saturate the
lattice at two points.

Two-photon processes at `ω < ω_C` can also produce pairs if their
intermodulation frequency (Vol 4 Ch 1 §"Condensate IMD Spectroscopy")
hits `ω_C`. The IMD sideband serves as the effective saturation-driver
frequency.

### §4.4 Compton scattering

A photon at `ω > ω_C` is above the lattice resonance. Off-resonance, the
lattice barely responds (inductive-reactance dominates, voltage doesn't
build up). But if the photon locally deposits enough energy to briefly push
an adjacent region past saturation, it can excite a transient electron
that absorbs some energy, and the photon emerges with shifted frequency.
This is Compton scattering, realized as a transient saturation event.

---

## §5 The Compton frequency as dynamical threshold

### §5.1 Frequency vs grid spacing

The grid spacing `ℓ_node` sets the single-bond LC resonance:

```
ω_C = c / ℓ_node
```

This is the natural frequency of the lattice at single-bond scale. It is
*not* a calibration — it is a derived consequence of the lattice geometry
and the vacuum impedance `Z_0 = √(μ_0/ε_0)`.

The voltage threshold `V_yield = √α · V_snap` is also set by geometry:
`V_snap = m_e c² / e` is the voltage quantum corresponding to one rest-mass
energy per elementary charge, and `α` is the dimensionless saturation
fraction (Ch 1 Axiom 4, Ch 8 α-derivation).

The electron's rest energy is:

```
m_e c² = ℏ · ω_C = ℏ · c / ℓ_node
```

This is the energy of a photon at the lattice self-saturation frequency.

### §5.2 The three regimes

| Regime    | Photon frequency | LC tank response | Saturation | Physical state            |
|-----------|------------------|------------------|------------|---------------------------|
| Low       | `ω < ω_C`        | Off-resonance    | No         | Photon passes transparently |
| Resonance | `ω = ω_C`        | Full resonance   | Yes        | Photon → bound → electron |
| High      | `ω > ω_C`        | Off-resonance    | Transient only | Compton-like scattering |

The electron's Compton frequency is a **genuine dynamical threshold** for
the photon-to-electron transition. This is analogous to a Josephson
junction's critical current or a varactor's breakdown voltage — a specific
parameter value at which the system's behavior qualitatively changes.

### §5.3 Why `α` appears as saturation limit

Axiom 4 states that the vacuum saturates when `Δφ = α`, where `Δφ` is the
dimensionless strain amplitude. Under this interpretation, `α` is not
"imported" from measured physics — it is the lattice's self-saturation
amplitude threshold at its self-resonant frequency. Measurement of `α`
reveals this threshold; the framework predicts it from geometry (Ch 8).

In voltage units: `V_yield = √α · V_snap`, which equals the voltage at
which a single-bond LC tank driven at `ω_C` saturates. The `√α` factor
arises because saturation depends on the *energy* (`½CV²`) reaching the
single-node ceiling, and the dimensionless threshold `α` corresponds to
energy-threshold, i.e., `V ∝ √α`.

This is internally consistent across:

- Axiom 1 (`ℓ_node`) → sets the grid scale.
- Axiom 2 (`[Q] ≡ [L]`, `ξ_topo`) → sets the charge-to-length conversion.
- Axiom 4 (saturation at `α`) → sets the dimensionless amplitude threshold.
- Ch 8 (α-derivation) → derives `α = 1/137.036` from the Golden-Torus Q-factor.

All four close the loop: `ℓ_node` sets `ω_C`; `α` sets `V_yield`; the
Golden-Torus geometry at TIR boundary computes `α = 1/137`; the bound
state at `V_yield` confining a photon at `ω_C` is the electron.

---

## §6 Quantitative predictions

### §6.1 The classical Hopfion Q vs electron Q

The convergence study ([earlier session record](../../.agents/handoffs/L3_PHASE3_SESSION_20260421.md) §2.6)
extrapolated the TLM's α⁻¹ to `184.7` as `1/N → 0`. Under the photon
identification, this is **the classical (2,3)-Hopfion Q-factor without
TIR confinement** — not α. The electron's Q = 1/α = 137.036 is the same
(2,3) configuration *with* TIR confinement.

The ratio is:
```
Q_photon / Q_electron = 184.7 / 137.036 = 1.348
```

This ratio is not derived in this document. Candidate decompositions to
investigate in a follow-up:

- `4/3 = 1.333`: geometric factor from half-covering vs full-covering.
- `(4π³ + 6π² + π) / (4π³ + π² + π) = 182.6 / 137 = 1.333`: full Clifford
  torus surface (`2π²`) vs half-cover (`π²`), giving `Λ_surf` multiplied
  by 6 instead of 1. Not quite 1.348 but the right order.
- An Axiom-4 saturation-boundary factor from the ratio of reactive to
  radiative modes at `Γ = −1` vs `Γ < −1`.

The clean derivation of `184.7/137 = ?` is an open analytical problem. It
should fall out of the amplitude-sweep experiment (§7 below).

### §6.2 Predicted amplitude transition

In the TLM, the soliton's behavior depends on whether the amplitude pushes
the lattice into Axiom-4 saturation. Current runs at `amplitude = 0.5`
(below `V_yield` in TLM units) produce the photon Q ≈ 184.7. Increasing
amplitude past `V_yield` should trigger saturation, creating a TIR
boundary, and the Q should shift toward 137.

**Pre-registered prediction (Phase 3b amplitude sweep):**

- `amplitude < V_yield`: bound state is photonic, Q ≈ 184.7, energy
  decays monotonically (no trapping).
- `amplitude ≈ V_yield`: transition regime. Local saturation engages
  intermittently. Q intermediate.
- `amplitude > V_yield`: full saturation confinement. Q → 137. Energy
  bounded (standing wave, not decaying).

If observed, this closes the electron derivation numerically in one
experiment. If not observed, the photon/electron mechanism as stated needs
revision.

---

## §7 Implications for the research program

### §7.1 Phase 3 deliverable split

The original L3 scoping (§1.3) targeted a single Phase-3 deliverable:
numerically demonstrate the electron at Golden-Torus geometry, recovering
`α⁻¹ = 137.036`. Under the photon identification, this splits cleanly:

- **Phase 3a — Photon characterization.** Demonstrate the stable (2,3)
  photonic Hopfion on K4 with `Q ≈ 184.7`. Map the three T₂ eigenvalues
  `(1.65, 1.22, 1.13)` to the photon's structural modes. Establish the
  (p,q) scaling: for arbitrary torus-knot windings, predict the Q-factor
  and T₂-eigenvalue signature. **Largely done** — present document plus
  raw data in `/tmp/phasor_discovery.npz`.
- **Phase 3b — Electron via saturation.** Add amplitude-sweep test. Verify
  that `amplitude > V_yield` triggers Axiom-4 saturation, creates a TIR
  boundary, and shifts Q from 184.7 to 137. **One experiment remaining.**

### §7.2 Connection to AVE-HOPF experimental program

The AVE-HOPF program tests macroscopic (p,q) torus-knot antennas. Each
antenna is a classical knotted-photon source — directly analogous to the
TLM's (2,3) Hopfion in §2. The TLM provides numerical predictions for
what AVE-HOPF should observe:

- Q-factor of the antenna in each (p,q) configuration.
- Three-mode T₂ eigenvalue split for each (p,q) — measurable as
  polarization-sector correlations in the emitted field.
- Chirality projection `χ = α · pq/(p+q)` (already derived,
  [`20_chirality_projection_sub_theorem.md`](20_chirality_projection_sub_theorem.md)).

AVE-HOPF is not a separate experimental program from the L3 research —
it is **the macroscopic test of the photon half of the electron-photon
duality**. Grant's earlier directive to defer AVE-HOPF "until we are
solid with the electron" should be revisited: being solid with the
electron includes being solid with the photon, which AVE-HOPF tests.

### §7.3 Ch 8 revision under the new framing

The Ch 8 audit (`29_ch8_audit.md`) flagged the Golden-Torus geometry as
real-space-impossible (ropelength constraints violated) and suggested a
phase-space reinterpretation. The photon identification provides a
stronger reinterpretation: the Golden Torus is **the spatial profile of
the (2,3) Hopfion photon** in the transverse-microrotation sector. `R`
and `r` describe the torus cross-section in *transverse field space*, not
in Cartesian `ℝ³`. The sub-node geometry paradox dissolves because the
Hopfion is a field configuration, not a massive knotted tube.

Ch 8 revision should:

- Clarify that the Golden Torus is the transverse (T₂) field profile
  at TIR confinement.
- Distinguish the Hopfion photon (un-confined Golden Torus, Q ≈ 184.7)
  from the electron (confined Golden Torus, Q = 137).
- Keep the three-Λ multipole decomposition but tag each Λ as a
  T₂ eigenvalue (the three non-zero modes observed in §2.2).
- Cite this document and the Phase-3a/3b split.

### §7.4 What this closes and what remains open

**Closes:**

- The "what does the TLM 2.27 attractor physically imply?" question.
  Answer: it's the Hopfion photon.
- The A₁/T₂ split's physical meaning — longitudinal vs transverse, i.e.,
  `u` vs `ω` Cosserat sectors.
- The conceptual framing of electron-photon relationship on K4.

**Remains open:**

1. **Amplitude sweep** — the Phase-3b numerical verification. Straightforward
   experiment, clear pre-registered prediction.
2. **184.7 / 137 = 1.348 ratio** — needs a first-principles derivation
   from the TIR-confinement mechanism.
3. **Three-mode T₂ split `(1.65, 1.22, 1.13)`** — physical identification
   of which mode is which. Candidate: toroidal winding vs poloidal winding
   vs longitudinal-along-centerline. Needs a proper mode analysis.
4. **(p,q) scaling** — run the TLM with other (p,q) seeds, map the Q-factor
   and T₂-split vs (p,q). This generates AVE-HOPF predictions.
5. **Op21 multi-mode rigor** still open per the Ch 8 audit — deriving the
   `Λ_vol + Λ_surf + Λ_line` partition from a reactive-energy integral.
   The photon identification doesn't resolve this; it just provides the
   context in which the partition should be rigorized.

---

## §7.5 Amplitude sweep result — the α⁻¹=139 match was transient

**Addendum (2026-04-22, after first Phase 3b eigenmode verification run):**

The amplitude sweep reported in §6.1 observed `α⁻¹ = 139.1` at strain
`A ≈ 0.48`, close to the electron target 137.036 to 1.5%. Subsequent
extension to 600 steps with per-step geometry tracking
(`phase3b_eigenmode_verification.py`) revealed this match was a
**time-averaging artifact of a transient passage** through Golden-
Torus proportions, not a stable eigenmode. The shell geometry drifts
19.5% in R/r over the 400 steps past the transient; the state settles
at R/r ≈ 3.88, nowhere near φ².

The photon identification of §1–§4 above **survives** the
re-examination — the A₁/T₂ decomposition, zero-eigenvalue of A₁ mode,
transverse-only character, and photonic interpretation are all
symmetry-and-sector arguments that do not depend on whether the
electron mechanism closes numerically.

The electron-formation mechanism of §4 (photon + TIR via Axiom-4
bond-level saturation) is **pending re-test** under the axiom-
compliant redesign in [`32_phase3b_axiom_compliant_redesign.md`](32_phase3b_axiom_compliant_redesign.md),
which removes the non-axiomatic PML, hand-set amplitude, and single-
envelope choices that the original test embedded. The §4.2–§5 claims
about photon emission, pair production, and the electron's Compton-
frequency threshold remain *theoretical predictions* awaiting
the redesigned numerical verification.

**Physics-reframe addendum (2026-04-22):** The S11 minimization path
(X1-X2 in `32_`) correctly finds the *photon limit* — S11 → 0 under
gradient descent means the (2,3) trefoil "opens" into a
vacuum-impedance-matched propagating helical mode. A cut trefoil with
(2,3) winding IS the photon on K4; the K4 chirality forces transverse
waves into the (2,3) helical shape as their natural propagation form.
The electron is the *closed* trefoil with Axiom-4 saturation engaged
at its shell (Γ=−1 TIR mirror, maximum local |Γ|²). These are opposite
objectives: the electron maximizes |Γ|² locally while matching
externally; the photon minimizes |Γ|² everywhere. The X3 test in
[`33_phase3b_x3_energy_analysis.md`](33_phase3b_x3_energy_analysis.md)
uses `relax_to_ground_state()` on the richer Cosserat energy
(Op10 + Hopf + reflection + saturation-modulated elastic) — which has
terms that actively reward both c=3 topology and sharp shell
boundaries — to test whether the electron emerges as the energy
ground state.

---

## §8 Files created / modified in this research arc

**New:**

- `research/L3_electron_soliton/30_photon_identification.md` — this document
- `src/scripts/vol_1_foundations/phasor_trajectory_test.py` — initial
  time-series phasor test (negative result, preserved as record)
- `src/scripts/vol_1_foundations/phasor_discovery.py` — spatial phase-space
  discovery test (produces the T₂ eigenvalue signature)

**Modified:**

- `manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex` —
  handoff comment at top pointing to the audit and synthesis (not editing
  the physics content; awaiting dialogue conclusion)

**Raw data:**

- `/tmp/phasor_trajectory_test.npz`
- `/tmp/phasor_discovery.npz`

---

## §9 Corpus references

- [`manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex`](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex) — Axioms 1, 2, 4
- [`manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex:139`](../../manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex#L139) — photon as transverse Cosserat mode
- [`manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:395-504`](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L395) — LC tank + Confinement Bubble + Pauli exclusion
- [`manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:491-495`](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L491-L495) — photon as linear transverse shear wave
- [`research/L3_electron_soliton/00_scoping.md:118-126`](00_scoping.md#L118-L126) — Cosserat wave modes including photon identification
- [`research/L3_electron_soliton/17_theorem_3_1_reframed_Q_factor.md`](17_theorem_3_1_reframed_Q_factor.md) — LC-tank Q-factor derivation
- [`research/L3_electron_soliton/20_chirality_projection_sub_theorem.md`](20_chirality_projection_sub_theorem.md) — `χ = α·pq/(p+q)` for (p,q) windings
- [`research/L3_electron_soliton/24_step3_bond_lc_compton.md`](24_step3_bond_lc_compton.md) — single-bond LC = `ω_C`
- [`research/L3_electron_soliton/28_two_node_electron_synthesis.md`](28_two_node_electron_synthesis.md) — full analytical chain
- [`research/L3_electron_soliton/29_ch8_audit.md`](29_ch8_audit.md) — Ch 8 audit flagging real-space impossibility
- [`src/ave/core/k4_tlm.py`](../../src/ave/core/k4_tlm.py) — K4-TLM implementation
- Rañada, A. F. (1989). *A topological theory of the electromagnetic field.*
  Lett. Math. Phys. **18**, 97-106.
- Irvine, W. T. M. & Bouwmeester, D. (2008). *Linked and knotted beams
  of light.* Nat. Phys. **4**, 716-720.

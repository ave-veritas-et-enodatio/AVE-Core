# Phase 3b Eigenmode Verification — Simulation Setup

> **SUPERSEDED by [`32_phase3b_axiom_compliant_redesign.md`](32_phase3b_axiom_compliant_redesign.md)**
> (2026-04-22 later same day). This document's setup used PML boundaries,
> hand-set amplitude, a single Lorentzian ansatz, and the Ch 8 multipole
> formula for Q extraction — all non-axiomatic. The eigenmode test run
> against this setup produced a negative result (19.5% R/r drift over
> 400 steps past transient); the amplitude-sweep's earlier α⁻¹=139 match
> was a time-averaging artifact of a transient passage through Golden-
> Torus proportions, not a stable bound state. The redesign in `32_`
> replaces non-axiomatic choices with periodic BCs, Op6 self-consistency,
> envelope-independence testing, and tiered Q-factor reporting. Read
> this document for the audit of why each choice was problematic;
> read `32_` for the axiom-compliant redesign.

**Date:** 2026-04-22
**Purpose:** Rigorously document every parameter and procedural choice for
the time-resolved eigenmode-vs-transient test. This document is the
"why" for each setting; the companion script
`src/scripts/vol_1_foundations/phase3b_eigenmode_verification.py` is
the "what."

**Test question:** At the empirically-observed electron-forming strain
(`A ≈ 0.48`), is the shell geometry `R/r ≈ 2.60` a stable eigenmode of
the K4-TLM dynamics, or a transient passage through Golden-Torus
proportions on the way to a different attractor?

**Outcome interpretation:**
- If eigenmode: the R/r = φ², α⁻¹ = 137 match observed in the amplitude
  sweep (30_photon_identification.md + phase3b_amplitude_sweep) is a
  real physical bound state. Phase 3b is numerically closed.
- If transient: the match is a coincidence from time-averaged geometry
  during drift. The PML likely absorbs the wavefunction before
  self-generated TIR can confine it. Need to revisit boundary-condition
  design.

---

## §1 The physics this is testing

The hypothesis under test (from 30_photon_identification.md):

1. The K4-TLM with `op3_bond_reflection=True` implements Axiom-4
   saturation at the bond level: `Z_eff = Z_0/√S` with
   `S = √(1 − A²)` where `A = |V_inc|/V_SNAP` is the dimensionless strain.
2. When drive amplitude is large enough that shell-peak strain reaches
   Regime II (`√(2α) < A < √3/2`), Axiom 4 engages locally, producing
   `C_eff → ∞`, `Z_local → 0`, `Γ → −1` (TIR mirror).
3. The TIR mirror confines the transverse T₂ wavepacket into a standing
   (2,3) configuration — the electron.
4. If true: the bound state should be a **stable eigenmode** (R/r and
   energy settle to a plateau, not drift).

The amplitude sweep (phase3b_amplitude_sweep) produced α⁻¹ = 139.1 at
strain A_max ≈ 0.48, matching the electron's target α⁻¹ = 137.036 to
1.5%. But that measurement used time-averaged shell geometry over
steps 200-300. Without per-step tracking, we cannot distinguish:

- **(E)** The geometry settled at R/r ≈ 2.60 early and stayed there
  → genuine eigenmode.
- **(T)** The geometry drifted through R/r ≈ 2.60 en route to collapse
  → transient, average happened to hit Golden Torus.

---

## §2 Simulation parameters with derivation

Each parameter below lists: **value**, **origin / derivation**,
**physical justification**, and **flag** if not derivable from axioms.

### §2.1 Fundamental scales

**`ℓ_node`** (lattice pitch): `dx = 1.0` in TLM-internal units; physical
value `ℏ/(m_e c) ≈ 3.862 × 10⁻¹³ m`.

Origin: Axiom 1 + Ch 1 §1.1 Eq(Axiom 1 calibration line 18). The
smallest topologically stable soliton (unknot ground state) sets the
lattice resolution. In TLM internals, all lengths are in units of `ℓ_node`.

Not tunable — axiomatic.

**`c`** (propagation speed): `C_0 = 299,792,458 m/s`.

Origin: SI definition of the speed of light. TLM uses this via
`self.c = float(C_0)`.

Not tunable.

**`ω_C`** (Compton angular frequency): `c/ℓ_node`.

Origin: single-bond LC resonance frequency (synthesis Step 3,
`24_step3_bond_lc_compton.md`).

Derivation:
```
ω_C = 1/√(L_e C_e)
    = 1/√((ξ_topo⁻² m_e)·(ξ_topo² k⁻¹))
    = √(k/m_e)   where k = m_e c²/ℓ_node²
    = c/ℓ_node
```
In TLM internal units with `ℓ_node = 1` and `c = C_0`: `ω_C = C_0 rad/s`.

Not tunable — derived from axioms.

**`V_SNAP`** (rupture voltage): `m_e c²/e = 510,999 V`.

Origin: Axiom 2 topo-kinematic identity `V = ξ_topo⁻¹ F` applied to the
lattice string tension `F = T_EM = m_e c²/ℓ_node`. This is the voltage
at which `V·e = m_e c²` — one rest-mass energy per elementary charge.
Vol 4 Ch 1 Row 3 of the translation table.

Not tunable — axiomatic.

**`V_YIELD`** (saturation-onset voltage): `√α · V_SNAP ≈ 43,652 V`.

Origin: Vol 4 Ch 1 Eq(varactor). The Axiom-4 saturation engages at the
strain at which `V/V_yield = 1`, i.e., `V = √α · V_SNAP`. The `√α`
scaling arises because saturation is an energy (`½CV²`) threshold,
so voltage scales as `√α` of snap.

Not tunable — derived from axioms.

### §2.2 Time-step geometry

**`dt`** (TLM step): `dx / (c · √2)`.

Origin: K4-TLM CFL-like stability condition, [k4_tlm.py:115](../../src/ave/core/k4_tlm.py#L115).
The √2 is the tetrahedral geometric factor — a wave crossing one K4
4-port junction traverses the diagonal of a tetrahedron, which is
`√2` times the port-to-port hop.

Derivation: for a 4-port TLM junction with isotropic scattering, the
effective group velocity equals `c` only if `dt ≤ dx/(c·√d)` where
`d` is the spatial dimensionality; for the K4 diamond lattice
embedding in 3D with tetrahedral geometry, the effective `d` is 2
(the 4-port scattering is 2D-like per junction), giving `dt = dx/(c·√2)`.

Not tunable — CFL hardware constraint.

**Compton period in steps**: `T_C / dt = (2π/ω_C)/dt = 2π · √2 ≈ 8.886`.

Derivation:
```
T_C / dt = (2π/ω_C) / (dx/(c·√2))
        = (2π·dx/c) / (dx/(c·√2))
        = 2π · √2
        ≈ 8.886 steps per Compton period
```

**Run length for eigenmode test**: 600 steps ≈ 67.5 Compton periods.

Justification: prior runs used 300 steps (~34 periods). For eigenmode
verification we want enough cycles that any slow drift is visible. 67
periods gives a drift-visibility threshold of ≈ 1/67 ≈ 1.5% per period
for a visible monotonic trend. Cheap (~2 min compute at N=64).

Chosen for diagnostic resolution, not derived.

### §2.3 Lattice size and boundary conditions

**`N`** (lattice cells per side): 64.

Origin: must accommodate the soliton (R ≈ 16, shell thickness ≈ 4)
plus the PML (thickness 6) with buffer. Minimum N ≈ 2·(R + r + PML) ≈
2·(16 + 6 + 6) = 56. N=64 gives margin. Convergence study showed
R/r stable across N=48, 96 (within 1%), so N=64 is adequate.

Compute scales as N³ per step; N=64 is a pragmatic balance between
resolution and wall-clock time.

**Flag:** not uniquely derived. N could be smaller (48) or larger (96)
without changing physics. Chosen for speed × precision.

**`pml_thickness`** (PML layer depth): 6 cells.

Origin: Vol 4 Ch 1 §6 "Boundary Conditions" recommends PML with
cubic-graded conductivity `σ(d) = σ_max (d/d_pml)³`, `σ_max = (m+1)/(150π·Δx)`.
Implementation default in [k4_tlm.py](../../src/ave/core/k4_tlm.py).

**Flag — critical concern for this test.** PML is the correct boundary
for *propagating* photons — it absorbs outgoing radiation without
spurious reflection. But for a *bound* electron, PML is actively
destructive: the electron's wavefunction extends slightly beyond the
shell, and PML absorbs any excursion. If the test shows energy decay
concurrent with R/r evolution, we can't distinguish:

- Physical dissipation (real electron radiating) — should be negligible
  in pure bound state
- PML absorption (simulation artifact) — absorbs any near-boundary
  amplitude regardless of physics

**Mitigation for this test:** run TWO variants at strain A ≈ 0.48:
1. PML boundary (current default) — same as amplitude sweep
2. Periodic boundary (no PML) — forbids the absorption artifact,
   but introduces self-interaction through wrap-around

If both show the same eigenmode behavior, the eigenmode claim is robust.
If PML variant drifts but periodic variant is stable, PML is
destroying the physics and we need reflecting boundaries with a larger
domain.

### §2.4 Physics flags

**`op3_bond_reflection`**: `True`.

Origin: Axiom 4 implementation at bond level. When True, each bond
applies `Z_eff = Z_0/√S` where `S = √(1 − A²)` is the saturation
factor from universal_saturation, [k4_tlm.py:201-265](../../src/ave/core/k4_tlm.py#L201).
This is the LOAD-BEARING confinement mechanism — without it, no TIR,
no electron.

Mandatory for this test.

**`nonlinear`**: `False`.

Origin: TLM construction flag controlling whether saturation is also
applied at *node* scattering (not just bonds). When False, the 4-port
scatter uses the linear `S_linear = (1/2)𝟙 − I`. When True, it would
apply a strain-dependent scatter.

Justification for False: the bond-level Op3 reflection is the
physical location of Axiom-4 saturation — between adjacent impedance
cells. Node-level nonlinearity would represent a different physics
(per-node capacitor saturation independent of bond propagation).
Vol 4 Ch 1's varactor model places the saturation at *cells*, which
in K4-TLM terms is at bonds (LC cells are the bonds, not the nodes).

**Flag:** this deserves more corpus research. The "bonds as LC cells"
vs "nodes as LC cells" distinction may have a preferred answer in the
manuscript that I haven't traced fully. For now, `False` matches the
convention used in the amplitude sweep, so comparison is clean.

### §2.5 Initial ansatz

**Winding pattern**: (2,3) torus knot, phase `θ = 2φ + 3ψ`.

Origin: synthesis Step 4 (`25_step4_23_winding_selection.md`).
(2,3) is the smallest non-trivial coprime torus knot (lowest
crossing count c = 3).

Mandatory for electron identification.

**Envelope shape**: `envelope = A · π / (1 + (ρ_tube/r_opt)²)`,
Lorentzian in tube-distance from the torus centerline, `r_opt = max(r, 1.0)`.

Origin: [tlm_electron_soliton_eigenmode.py:76-77](../../src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py#L76-L77).
Phenomenological — smooth, peaked at centerline, decays outside. NOT
derived from axioms.

**Flag:** this is the weakest part of the setup. A truly axiom-derived
seed would solve the Cosserat-Lagrangian equations on K4 and use the
resulting ground state. That's the Phase-1+2 deliverable that hasn't
been completed. The Lorentzian is a reasonable placeholder, and if an
eigenmode exists, dynamics should relax *from* any sufficient seed *to*
the true eigenmode shape. If the eigenmode test fails because of seed
choice, that's a relevant negative result.

**Port quadrature**: cos(θ) on ports {0, 1}; sin(θ) on ports {2, 3}.

Origin: [tlm_electron_soliton_eigenmode.py:112-121](../../src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py#L112-L121).
Encodes the complex phase θ in real port amplitudes via Euler
decomposition across the 4-port space.

**Flag:** the choice of WHICH ports carry cos vs sin is partially
arbitrary. Ports 0 and 2 happen to be "diagonal" tetrahedral
directions (`+1,+1,+1` and `−1,+1,−1`). A different pairing (0,2 vs
1,3) might seed a different phase winding. For this test, keep the
canonical (0,1) vs (2,3) split for consistency with prior runs.

**Chirality weighting**: `w_k = (p_k · t̂) / √3` where `p_k` is the
tetrahedral port direction and `t̂` is the (2,3) knot tangent.

Origin: [tlm_electron_soliton_eigenmode.py:105-120](../../src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py#L105-L120).
Projects each port onto the winding tangent to encode handedness.

Mandatory for consistent (2,3) chirality.

**Target radii**: `R = 16.0`, `r = 6.108` lattice units. `R/r = φ² = 2.618`.

Origin: Golden-Torus proportions scaled to N=64. Seeded AT the expected
eigenmode geometry so the system doesn't have far to travel if the
eigenmode exists.

### §2.6 Drive amplitude

**`amplitude`** parameter: chosen so shell-peak strain `A_max =
v_total_max / V_SNAP ≈ 0.48`.

Origin: *empirical* from phase3b_amplitude_sweep — the strain value
at which α⁻¹ came closest to 137.036.

**Flag — major open question.** This value is NOT derivable from
axioms. Candidates we haven't confirmed:
- `A_electron = 1/2`? Observed 0.48. Close to 1/2 but not exact.
- `A_electron = √(1 − 1/φ²) = √(1 − 0.382) = 0.786`? Observed 0.48,
  doesn't match.
- `A_electron = π/2 · V_YIELD/V_SNAP = (π/2)·√α ≈ 0.134`? Doesn't match.
- Some relation involving the (2,3) winding numbers? Unknown.

For the eigenmode test, set `amplitude` so `A_max = 0.48` (matching the
amplitude-sweep sweet spot). If the state is a stable eigenmode, this
value should correspond to a physical invariant and its analytical form
becomes a dedicated follow-up research item.

In script terms: `amplitude = 0.48 · V_SNAP / π ≈ 78,100`.

### §2.7 Sampling strategy

**Sampling interval**: record shell geometry at **every step**.

Change from amplitude-sweep default (every 50 steps). Required for
visibility of drift vs stability. Minor compute overhead (shell_envelope
is cheap — histogram over ~50,000 active lattice cells).

**Shell-selection threshold for port-correlation analysis**:
`V_phys² > 0.3 · max` — same as prior runs.

Not derived — empirical choice. A value too low includes boundary
noise; too high misses real structure. 0.3 is held constant for
consistency with the amplitude sweep comparison.

### §2.8 Extraction methods

**R, r extraction** — `shell_envelope` from
[tlm_electron_soliton_eigenmode.py:128-165](../../src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py#L128-L165):

Radial histogram of `V_magnitude` at z = center. Peak bin → R; FWHM/2
of the peak → r. Converts a 3D toroidal field into (R, r) pair via
radial projection.

Assumptions:
- Torus is centered on the lattice center (cx, cy, cz) ✓ by construction
- Torus is symmetric under z → −z (z=center is the equator) ✓
- Peak bin identifies the major axis unambiguously — ✓ if single-peaked
- FWHM/2 = minor axis — approximate; Lorentzian vs Gaussian profile
  differences could introduce 5-10% bias in r

**α⁻¹ extraction** — `extract_alpha_inverse(R, r, c=3)` at
[tlm_electron_soliton_eigenmode.py:522-556](../../src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py#L522-L556):

```
d = 2(R − r)
α⁻¹ = 16π³·(R·r/d²) + (c/3)·4π²·(R·r/d²) + π
    = Λ_vol + Λ_surf + Λ_line  (Ch 8 multipole decomposition)
```

**Flag — this is Ch 8 formula, which 29_ch8_audit.md §4 flagged as
asserted rather than derived from Q-factor first principles.** If the
formula is geometrically valid but physically misidentified, then
"α⁻¹ = 137 at Golden Torus" is a geometric identity, not a Q-factor
derivation. The amplitude-sweep finding that saturation drives
geometry *to Golden Torus* is still interesting independent of the
Q-factor interpretation — but the link between geometry and α needs
the Op21 multi-mode rigorization.

Using this formula here for consistency with prior runs.

---

## §3 Pre-registered predictions

At strain A ≈ 0.48, expect to see:

**If eigenmode (hypothesis E):**
- R/r reaches a plateau at ≈ 2.60 by ~step 100 and stays there through
  step 600. Fluctuations under 2%.
- Energy may decay but energy-per-unit-volume inside the shell should
  stabilize — soliton doesn't thin out.
- α⁻¹ (continuously computed from R(t), r(t)) plateaus at ≈ 139 ± 2.
- T₂ port eigenvalues stable.
- Comparison run at smaller strain (A = 0.05, photon regime) should
  drift to a different R/r and hold there.

**If transient (hypothesis T):**
- R/r passes through 2.60 en route to some other value. Drift is
  monotonic.
- α⁻¹ passes through 139 on its way elsewhere. The amplitude-sweep
  time-averaged value was a fluke of timing.
- Energy dissipates fully (PML absorbs everything).

**Ambiguous (hypothesis A):**
- R/r is stable AND energy is still decaying. Requires PML-vs-periodic
  comparison to resolve whether the dissipation is physical or
  simulation artifact.

### §3.1 Decision thresholds

- R/r at step 600 within 3% of R/r at step 200 → eigenmode candidate
- R/r at step 600 differs from step 200 by > 5% → transient
- α⁻¹(t) standard deviation (steps 200-600) < 5 → stable Q
- Energy trace: linear decay with slope that differs between PML and
  periodic runs → PML absorption dominant
- Linear decay with same slope → physical dissipation (unexpected, but
  would indicate the "electron" at strain 0.48 still radiates somehow)

---

## §4 Known limitations and open questions

1. **PML vs self-generated TIR.** The theoretical picture says the
   electron is confined by its own Γ = −1 mirror; the simulation uses
   PML at the outer boundary. These are different physical mechanisms.
   The test addresses this by running both PML and periodic boundary
   variants.

2. **Lorentzian envelope in the initial ansatz is not axiom-derived.**
   A stable eigenmode should be reachable from any seed in its basin
   of attraction. If the test passes, the Lorentzian was adequate; if
   it fails at strain 0.48 but succeeds at some nearby strain, seed
   sensitivity should be tested separately.

3. **`A_electron = 0.48` is empirical, not derived.** A first-principles
   derivation of this value is an open analytical problem. Candidates
   noted in §2.6.

4. **The α⁻¹ extraction formula is Ch 8's multipole sum, which audit
   F4 flagged as asserted not derived.** Geometric match at Golden
   Torus holds regardless, but the "Q-factor" interpretation is still
   pending Op21 multi-mode rigorization.

5. **`nonlinear=False` choice needs corpus verification.** Bonds vs
   nodes as LC cells is a Vol 4 Ch 1 framing detail I haven't fully
   traced.

6. **This test doesn't address the 184.7 vs 103.6 photon-regime
   discrepancy** — the low-strain convergence-study extrapolation
   gives Q ≈ 184.7 but our N=64 low-strain value is 103.6. Different
   seed, different runtime, or different dissipation regime; worth
   dedicated investigation but not blocking for the eigenmode test.

---

## §5 Companion script

`src/scripts/vol_1_foundations/phase3b_eigenmode_verification.py` implements
the test.

Summary of procedure:
1. Run TLM at N=64, strain A=0.48, PML thickness 6, 600 steps.
2. At EVERY step: record total energy, shell (R, r), α⁻¹, peak strain.
3. Run a baseline at strain A=0.05 (photon regime) for comparison.
4. Run a periodic-boundary variant at A=0.48 (pml_thickness=0) to
   isolate PML effect.
5. Plot all four traces (R/r(t), α⁻¹(t), energy(t), A_max(t)) on a
   shared time axis.
6. Apply decision thresholds from §3.1.

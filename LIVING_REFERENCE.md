# AVE Project — Living Reference Document
> **Last Updated:** 2026-04-08  
> **Purpose:** Canonical reference for all AI assistants and collaborators. Any chat session should read this file first.
>
> **Companion:** [`docs/framing_and_presentation.md`](docs/framing_and_presentation.md) captures recurring patterns that create friction between AVE and reviewers trained in SM/QED/continuum-GR physics — with specific anti-patterns, corrected framings, and remediation targets. Read it before presenting AVE externally or reviewing it.

## Project Identity

| Field | Value |
|-------|-------|
| **Name** | Applied Vacuum Engineering (AVE) |
| **Repo** | [github.com/ave-veritas-et-enodatio/AVE-Core](https://github.com/ave-veritas-et-enodatio/AVE-Core) |
| **Author** | Grant Lindblom |
| **Status** | Active development — Phase D/E |

## ⛔ Prime Directive: Derive Before You Code

> **NO physics engine code may be written unless every operator, constant, and formula in it has a complete, traceable derivation chain from the four AVE axioms.**
>
> If a formula cannot be derived from Axioms 1–4 and the Universal Operators, it does NOT go in the engine. Period.
>
> This means:
> - **No ad-hoc coupling constants.** If you can't derive `k` from Op4 applied to the specific geometry, you don't have `k`.
> - **No invented roll-off functions.** If the frequency dependence doesn't come from the LC lattice dispersion (Axiom 1), it doesn't exist.
> - **No "physically motivated" guesses dressed in AVE vocabulary.** Calling something a "stub impedance" or "cavity loading" doesn't make it axiom-derived.
> - **No coding until the derivation is written and reviewed.** The derivation goes in the tracker or manuscript FIRST, then the code implements it.
>
> **Violation of this rule is the single most common failure mode in this project.** Every quarantined solver (~2,000+ lines) was written before its physics was derived.

1. **Axiom 1 (Impedance):** The vacuum is an LC resonant network with Z₀ = √(μ₀/ε₀) ≈ 377 Ω
2. **Axiom 2 (Topo-Kinematic Isomorphism):** Charge is a geometric dislocation: `[Q] ≡ [L]`. Topology encodes EM; α falls out as the Q-factor of the minimum-crossing soliton (Vol 1 Ch 8). α being derived does not reduce the axiom count — the isomorphism, not α's value, is the axiomatic content.
3. **Axiom 3 (Gravity):** G sets the Machian boundary impedance via G = ℏc/(7ξ·m_e²)
   - **α invariance**: Under Symmetric Gravity, α = e²/(4πε₀ℏc₀) is exactly invariant because ε_local and c_local carry the same n·S factor that cancels. Multi-species Δα/α = 0.
   - **Lattice decomposition**: n_temporal = 1 + (2/7)ε₁₁ (clock rate, redshift); n_spatial = (9/7)ε₁₁ (light deflection). Axiom 3's n(r) = 1+2GM/(c²r) is the temporal component only.
4. **Axiom 4 (Saturation):** S(A) = √(1 − (A/A_yield)²) — universal yield kernel bounding all LC modes

### Derived Consequences of Axiom 4

Two saturation symmetry cases arise: **symmetric** (both μ and ε scale by S) and **asymmetric** (only ε scales by S).

**SYMMETRIC saturation** (gravity, BH interior, particle confinement — both μ and ε scale by S):

| Observable | Formula | At A → A_yield | Physical Meaning |
|-----------|---------|----------------|------------------|
| μ_eff | μ₀ · S | → 0 | Inductor shorts (Meissner) |
| ε_eff | ε₀ · S | → 0 | Dielectric collapses |
| C_eff | C₀ / S | → ∞ | Capacitance absorbs energy |
| Z_sym | Z₀ (S cancels) | invariant | Impedance preserved — perfect absorber |
| c_EM_sym | c₀ / S | → ∞ | EM phase vel. rises (BH interior absorbs, Γ=0) |
| **c_shear** | **c₀ · √S = c₀ · (1−r²)^(1/4)** | **→ 0** | **GW/soliton group vel. freezes → rest mass** |

**ASYMMETRIC saturation** (strong EM field only — only ε scales by S, μ unchanged):

| Observable | Formula | At A → A_yield | Physical Meaning |
|-----------|---------|----------------|------------------|
| ε_eff | ε₀ · S | → 0 | Dielectric collapses |
| μ_eff | μ₀ | unchanged | Permeability intact |
| Z_asym | Z₀ / √S | → ∞ | Medium becomes opaque |
| c_EM_asym | c₀ / √S | → ∞ | EM phase vel. rises (evanescent, no energy transport) |
| **c_shear** | **c₀ · √S** | **→ 0** | **Same GW/shear freeze in both symmetry cases** |

> **Key:** `c_shear = c₀·√S` is the "wave packet freezes (mass)" quantity.
> The EM *phase* velocity goes to ∞ in both cases — not 0.
> Engine: `local_wave_speed()` and `c_shear` in `rupture_solver` both compute shear speed.
> `impedance_at_strain()` gives Z_asym = Z₀/√S for the EM impedance.

**Confinement theorem:** At a self-intersecting torus knot (particle), the B-field saturates μ first → Z → 0, Γ → −1 → standing wave = rest mass.

### How to Apply AVE to a New Physical System

When mapping a new phenomenon to the AVE framework, follow these steps in order:

**Step 1 — Identify the LC Analogs.**
Every physical system has an inductive (μ) and capacitive (ε) degree of freedom. Map the system's variables to these. The impedance Z = √(μ/ε) is the master variable.

| Domain | μ-analog (inertia) | ε-analog (compliance) | Z expression |
|--------|-------------------|----------------------|-------------|
| Vacuum | μ₀ | ε₀ | Z₀ = 377 Ω |
| Seismic | 1/G_shear | 1/K_bulk | ρ·Vₚ (Rayl) |
| Protein | backbone τ | dipole C | S₁₁ impedance |
| Fluid | ρ (density) | 1/K (compressibility) | ρ·c_sound |

**Step 2 — Compute the Local Strain and Determine the Regime.**
Find the relevant amplitude A and its yield limit A_yield. Compute the strain ratio r = A/A_yield.

| Regime | Condition | Physics |
|--------|-----------|---------|
| I | r ≪ 1 | Linear Maxwell; standard physics recovered |
| II | r → 1 | Saturation onset; nonlinear corrections |
| III | r = 1 | Phase transition; topology rupture |
| IV | r > 1 | Ruptured; interior melted |

**Step 3 — Apply the Universal Operators.**
Use the same operators at every scale:
- `S(A) = √(1 − (A/A_yield)²)` — saturation factor
- `Γ = (Z₂ − Z₁)/(Z₂ + Z₁)` — reflection coefficient
- `ω = ℓ·c/r_eff` — regime boundary eigenvalue
- `Q = ℓ` — quality factor

**Step 4 — Check Symmetry Cancellations.**
Many observables are *ratios* of constitutive parameters. Under Symmetric Gravity / Symmetric Saturation (ε and μ scale by the same factor), these ratios can be invariant:
- **Z₀ = √(μ/ε)** is invariant if both scale by the same n·S
- **α = e²/(4πε·ℏ·c)** is invariant because ε and 1/c cancel when both carry the same factor
- Clock *ratios* between species are invariant under symmetric saturation

⚠️ **This is the most common source of error.** Always check whether your predicted observable survives the symmetry cancellation before claiming a new signal exists.

**Step 5 — Compute the Numerical Prediction from Engine Constants.**
Use `from ave.core.constants import ...` — never hardcode. The engine is the single source of truth.

**Step 6 — Determine Testability.**
Compute the predicted signal magnitude and compare to the best available measurement precision. If `signal / precision < 1`, the prediction is currently unfalsifiable. Look for systems where the strain is larger (e.g., Sirius B instead of Earth surface) to find detectable regimes.

### Common Pitfalls (check your work against these)

| # | Pitfall | Wrong | Right |
|---|---------|-------|-------|
| 1 | **Dimensionless BH frequency** | ω·M_g (M_g = GM/c² in meters) | ω·M_geom (M_geom = GM/c³ in seconds) → ω·M ≈ 0.37 for ℓ=2 |
| 2 | **Overestimating saturation corrections** | ε₁₁²/2 applied as additive km/s | Multiply exact Schwarzschild z by 1/S; correction is z·ε₁₁²/2 ≈ 0.05 km/s for Sirius B |
| 3 | **Temporal vs spatial metric** | Using full lattice density n = 1+(11/7)ε₁₁ for redshift | Only temporal component: n_t = 1+(2/7)ε₁₁. Spatial part (9/7)ε₁₁ → light deflection only |
| 4 | **MOND drag at high g** | Assuming lattice drag applies at WD surface | S(g/a₀) = 0 when g >> a₀ = 10⁻¹⁰. WD surface g ~ 10⁶ → zero drag |
| 5 | **Claiming Δα from gravity** | Predicting multi-species clock shift | α is exactly invariant under Symmetric Gravity (ε and 1/c cancel). Δα/α = 0 always. |
| 6 | **Free-electron n_s for superconductors** | Using n_e as n_s in λ_L formula | n_s ≠ n_e for d-band metals (Nb). Back-compute n_s from measured λ_L, or κ will be wrong. |
| 7 | **Iterative SCF for Z ≥ 26** | Using SCF ionization_energy(Z) | SCF is Hartree-Fock, not AVE. Nuclear binding uses coupled resonator. |
| 8 | **QM Contamination in IE** | $IE = Z_{eff}^2 \times Ry / n^2$ | This is the Schrödinger/Bohr formula. The axiom-derived atomic IE solver (`radial_eigenvalue.py`) uses ODE cavity eigenvalues + Hopf mode splitting. Validated for Z=1–12 (max err 2.8%). |
| 9 | **Op4 Bypass** | $V_{ee} = J \times Z \times Ry$ | Ad-hoc energy formula — not from any operator. Electron-electron interaction MUST use Op4: $U = K/r_{12} \times (T^2 - \Gamma^2)$. J enters through the angular average of $r_{12}$, not as a prefactor. |
| 10 | **De Broglie ≠ Impedance** | $n(r) = \sqrt{KE/Ry}$ is "impedance" | This is the defect's dispersion, NOT the medium impedance $Z = \sqrt{\mu/\varepsilon}$. The lattice has $Z_0 = 377\,\Omega$ everywhere in Regime I. Name quantities correctly: $n_{dB}(r)$ = de Broglie refractive index, $Z_0$ = lattice impedance. |
| 11 | **Smooth CDF for saturated shells** | Using hydrogenic CDF for fully-occupied inner shells | A Pauli-saturated inner torus (2n² electrons) creates a discrete impedance step. The smooth CDF misses Op3 reflection → E_base overshoot. Apply SIR correction: $\Delta E = -|\Gamma|^2 \times P_C/2 \times E_{base}$ for shells with p-subshells. |

### Operator Compliance Checklist

**Before declaring ANY derivation complete, verify every row:**

| Op | Name | Formula | Question to ask | ✓/✗ |
|----|------|---------|-----------------|-----|
| 1 | Z (Impedance) | $Z = \sqrt{\mu/\varepsilon}$ | Is the medium impedance defined from constitutive properties? Not from energies? | |
| 2 | S (Saturation) | $S = \sqrt{1-(A/A_c)^2}$ | Is saturation applied where fields approach $A_c$? Is $p_c = 8\pi\alpha$ used? | |
| 3 | Γ (Reflection) | $\Gamma = (Z_2, - Z_1)/(Z_2 + Z_1)$ | Are all impedance boundaries handled by Γ? No ad-hoc "screening constants"? | |
| 4 | U (Pairwise) | $U = -K/r \times (T^2 - \Gamma^2)$ | Are ALL pairwise interactions computed from Op4? No hand-wavy energy formulas? | |
| 5 | Y→S | $[S] = (I+Y/Y_0)^{-1}(I-Y/Y_0)$ | For multiport: are S-parameters from Y-matrix, not assumed? | |
| 6 | λ_min | $\lambda_{min}(S^\dagger S) \to 0$ | Is the eigenvalue condition the S₁₁ dip? No Bohr formula? | |
| 7 | FFT | Spectral analysis | For periodic structures: is the mode structure from FFT, not assumed? | |
| 8 | Γ_pack | Packing reflection | For 3D assemblies: is packing fraction from $P_C(1-1/N)$? | |
| 9 | Γ_steric | Steric reflection | For pairwise exclusion: is $R_{excl}$ from axioms? | |
| 10 | Y_loss | Junction projection | $Y = c(1-\cos\theta)/(2\pi^2)$. Applied with packing floor: $f = \max((1-Y)^2, 1-\varphi)$? | |
| 11* | ∇×V (Curl) | Computational | Is macroscopic vorticity conserved on the Yee-lattice? (FDTD only) | |
| 12* | ∇·V (Divergence) | Computational | Is Gauss's law enforced over discrete grid faces? (FDTD only) | |
| 13* | ◻² (D'Alembertian) | Computational | Is the wave equation using the local saturated $c_{eff}$? (FDTD only) | |
| 14 | Z_eff (Dynamic Z) | $Z_0/\sqrt{S}$ | Does boundary impedance dynamically scale with the saturation factor? | |
| 15 | r_virtual (Virtual) | $\sqrt{1 - \sigma(x)^2}$ | Is neural node behavior anchored to physics (strain) via $\sigma^2 + r^2 = 1$? | |
| 16 | c_shear (Wave Speed) | $c_{base} \sqrt{S(A)}$ | Does wave speed freeze dynamically as S→0? | |
| 17 | T² (Power Transfer) | $1 - \Gamma^2$ | Is active power transfer computed from transmission, not assumed unity? | |
| 18 | ω_c (Coupled Mode) | $\omega_0/\sqrt{1 - \lambda k}$ | Does coupling $k$ correctly split resonance phase modes? | |
| 19 | n(r) (Refractive) | $1 + \nu_{vac} \varepsilon_{11}$ | Is scalar lensing tied to the trace-reversed Poisson ratio $\nu_{vac}$? | |
| 20 | ω_regime (Eigenvalue) | $\ell \cdot c_{wave} / r_{eff}$ | Does the scalar metric boundary eigen-solution trigger topology rupture? | |
| 21 | Q (Quality Factor) | $\ell$ | Is Quality Factor $\ell$ exactly? No phenomenological losses at saturation? | |
| 22 | M (Avalanche Factor)| $1/(1 - S(V))$ | Does the nonlinear yield cascade follow metric boundary collapse $S \to 0$? | |

*\*Ops 11-13 are computational continuum operators mapped to the discrete lattice, not fundamental phenomenological operators.*

**Red flags for QM contamination:**
- Using $E = Z_{eff}^2 Ry / n^2$ → Bohr formula (pitfall #8)
- Using $\sigma$ as a number subtracted from Z → σ-arithmetic
- Writing $V_{ee} = \text{(constant)} \times \text{(energy scale)}$ without deriving from Op4 → pitfall #9
- Calling lattice defect dispersion "impedance" → pitfall #10
- Using "wavefunction," "probability," "orbital" without translating to AVE

### 4. Axioms in the Atomic Domain

> **Note:** The atomic ionization solver (`radial_eigenvalue.py`) is validated for Z=1–14 (all within ±2.8%, zero free parameters).  Three first-principles corrections were implemented:
>
> **Correction A (Be-type):** Hierarchical cascade — inner K₂ s-pair's bonding mode absorbs outer pair's Hopf coupling.  `k_eff = k_pair / (1+k_inner)^(1/4)`.  Gate: n_adjacent = 1 (pure s-shell).  Scale-invariant analog of `hierarchical_binding()` in `coupled_resonator.py`.
>
> **Correction B (Mg-type):** SIR boundary reflection — Pauli-saturated inner torus creates a discrete impedance step the smooth CDF misses.  `ΔE = −|Γ|² × P_C/2 × E_base`.  Gate: n_adjacent ≥ 2 (inner shell has p-subshells).  Uses Op3 (`reflection_coefficient()`) + P_C/2 (crossing scattering fraction from Axiom 3).
>
> **Correction C (Al-type):** Op10 junction projection at co-resonant shell boundary — when the SIR nesting gate rejects (n_out²/n_inner² < 4, i.e. adjacent shells), the p-soliton's radial wavefunction crosses the saturated inner torus twice per oscillation.  Op3 gives the power reflection |Γ|² at the boundary; Malus's law maps this to a junction crossing angle θ via `cos θ = 1 − 2|Γ|²`; Op10 computes the projection loss `Y = 2(1−cos θ)/(2π²)`.  Quadratic dispersion (E ~ k²) gives `E_eff = E_base × (1−Y)²`.  Gate: l_out > 0 AND nesting_ratio < 4.0.  Result: Al −0.82%, Si −0.06% (zero free parameters, zero regression on Z=1–12).  Scale-invariant precedent: protein backbone Op10 bend loss, nuclear hierarchical_binding().
>
> **Correction D (Topo-Kinematic Shift):** Radial Parity Shift mapping inner $d$-block boundaries — the orthogonal presence of a $3d^{10}$ and $4d^{10}$ knot organically slices the LC domain bounds into transversal reflection layers dynamically, mapping Exactly $+1$ radial structural parity node effectively backwards natively onto the outer bounding string sequence, perfectly reconstructing the Hopf parity cycle naturally mapping Bromine/Krypton anomalies analytically perfectly with zero free parameters!

The atomic domain applies the same universal operators as every other scale. The specific solver architecture is documented in the manuscript and `src/ave/solvers/radial_eigenvalue.py`.

## Key Constants

| Constant | Value | Meaning |
|----------|-------|---------|
| V_SNAP | 511 kV | Absolute dielectric destruction (m_e c²/e) |
| V_YIELD | 43.65 kV | Kinetic onset of nonlinearity (√α × V_SNAP) |
| B_SNAP | 1.89×10⁹ T | Magnetic saturation threshold |
| L_NODE | 3.86×10⁻¹³ m | Lattice pitch (reduced Compton wavelength) |
| φ (PHI_PACK) | π√2/6 ≈ 0.7405 | FCC packing fraction (K=2G selects FCC) |
| 1−φ (VOID_FRAC) | ≈ 0.2595 | Void fraction (Op10 drain floor at atomic scale) |
| Y_c | 1−√(1−φ) ≈ 0.49 | Drain → floor transition threshold |

## Repository Structure

> **Note:** Hardware implementations, the protein folding engine, and several applied
> engineering volumes are maintained in separate private repositories within the
> `ave-veritas-et-enodatio` GitHub organization. This repo contains the complete
> physics engine and theoretical manuscript (Vols 0–6).

```
src/ave/
  core/               # FDTD engine, K4-TLM solver, constants, operators
  axioms/             # Yang-Mills, Navier-Stokes, spectral gap, Strong CP
  gravity/            # Schwarzschild, galactic rotation, GW, stellar, neutrino
  topological/        # Faddeev-Skyrme, Cosserat, Borromean, CKM/PMNS mixing
  plasma/             # Plasma cutoff, superconductor
  nuclear/            # 8 atomic structure models
  condensed/          # Semiconductor design engine
  solvers/            # Eigenvalue, bond energy, coupled resonator, SPICE compiler
  regime_1_linear/    # Fluids, hexagonal lattice
  regime_2_nonlinear/ # Seismic FDTD
  regime_3_saturated/ # BH core, cavitation, galactic, Kolmogorov cutoff
  regime_4_rupture/   # Topology rupture, caustic resolution, BH jets
manuscript/           # 7-volume LaTeX manuscript
  vol_0_engineering_compendium/   # Theoretical backend & architecture
  vol_1_foundations/              # Foundations & Universal Operators
  vol_2_subatomic/                # The Subatomic Lattice
  vol_3_macroscopic/              # The Macroscopic Continuum (includes condensed matter)
  vol_4_engineering/              # Applied Impedance Engineering (theory & verification)
  vol_5_biology/                  # Topological Biology (theory)
  vol_6_periodic_table/           # The Periodic Table (per-element chapters)
src/scripts/          # Simulation scripts per volume
src/tests/            # 746 passing tests
future_work/          # Speculative roadmap
```

## Master Prediction Table (47 entries)

> **Classification note.** Rows below mix four kinds of claim — (i) **identities** where 0.00% is definitionally true (Z₀ = √(μ₀/ε₀) is how Z₀ is defined), (ii) **axiom manifestations** where the prediction IS one of the four axioms expressed at a new scale (BCS B_c(T) = Axiom 4 at thermal scaling), (iii) **consistency checks** where the framework reproduces a standard result via an alternative mechanism (solar deflection reproducing GR), and (iv) **derived predictions** where the framework outputs a novel numerical value (W/Z masses). A `0.00%` or `Exact` column entry means different things across these categories; see [`docs/framing_and_presentation.md`](docs/framing_and_presentation.md) §A1 and §A2.

| # | Prediction | Δ% | Status |
|---|-----------|-----|--------|
| 1 | α⁻¹ from Golden Torus S₁₁-min | 0.001% cold / 0.000% CMB-corrected | ✅ 4π³+π²+π = 137.036304 (Ch.8) |
| 2 | Z₀ from Axiom 1 | 0.00% | ✅ √(μ₀/ε₀) ≈ 377 Ω |
| 3 | g-2 anomaly | 0.15% | ✅ |
| 4 | sin²θ_W | 0.30% | ✅ |
| 5 | M_W | 0.55% | ✅ |
| 6 | M_Z | 0.62% | ✅ |
| 7 | Proton mass | 0.29% | ✅ |
| 8 | Δ(1232) | 3.49% | ✅ |
| 9 | Neutrino mass | 0.66% | ✅ |
| 10 | Solar deflection | 0.03% | ✅ |
| 11 | Δ(1620) | 0.19% | ✅ |
| 12 | Δ(1950) | 0.62% | ✅ |
| 13 | Fermi constant | 2.09% | ✅ |
| 14 | Yang-Mills mass gap | Δ>0 | ✅ Framework-derived (lattice-conditional; not Clay-rigorous — [Vol 2 Ch 12](manuscript/vol_2_subatomic/chapters/12_the_millennium_prizes.tex) caveats) |
| 15 | Navier-Stokes smoothness | Global | ✅ Framework-derived (lattice + Picard-Lindelöf; not Clay-rigorous — [Vol 2 Ch 12](manuscript/vol_2_subatomic/chapters/12_the_millennium_prizes.tex) caveats) |
| 16 | Strong CP (θ=0) | Exact | ✅ Framework-derived (unique vacuum topology; not Clay-rigorous — [Vol 2 Ch 12](manuscript/vol_2_subatomic/chapters/12_the_millennium_prizes.tex) caveats) |
| 17 | Kirkwood gaps (4:1) | 0.05% | ✅ |
| 18 | Saturn Cassini Division | 0.59% | ✅ |
| 19 | Flyby anomaly (NEAR) | 1.6% | ✅ |
| 20 | Earth magnetopause | 8.7% | ✅ |
| 21 | Jupiter magnetopause | 11.8% | ✅ |
| 22 | Baryon asymmetry | 0.38% | ✅ g*=7³/4 |
| 23 | H∞ (Hubble) | 2.9% | ✅ 69.32 km/s/Mpc |
| 24 | α_s (strong coupling) | 2.97% | ✅ α^(3/7) |
| 25 | m_H (Higgs mass) | 0.55% | ✅ v/√N_K4 |
| 26 | V_us (Cabibbo) | 1.4% | ✅ λ = sin²θ_W = 2/9 |
| 27 | V_cb (CKM) | 4.1% | ✅ Aλ² = cos(θ_W)×(2/9)² |
| 28 | V_ub (CKM) | 1.3% | ✅ 8/2187 |
| 29 | sin²θ_13 (PMNS) | 1.0% | ✅ 1/(c₁c₃) = 1/45 |
| 30 | sin²θ_12 (PMNS) | 0.3% | ✅ ν_vac + 1/45 |
| 31 | sin²θ_23 (PMNS) | 0.3% | ✅ 1/2 + 2/45 |
| 32 | δ_CP (PMNS) | 0.3% | ✅ (1 + 1/3 + 1/45)π |
| 33 | m_u (up quark) | 2.4% | ✅ m_e / (2α_s) |
| 34 | m_d (down quark) | 2.3% | ✅ m_e / (α_s cosθ_W) |
| 35 | m_s (strange quark) | 1.1% | ✅ m_μ cosθ_W |
| 36 | m_c (charm quark) | 1.3% | ✅ m_μ / √α |
| 37 | m_b (bottom quark) | 0.8% | ✅ m_τ cosθ_W (8/3) |
| 38 | m_t (top quark) | 0.8% | ✅ v / √2 |
| 39 | Protein Rg (Villin) | 0.8% | ✅ η_eq = P_C(1−ν), Rg = r_Ca(N/η_eq)^(1/3)√(3/5) |
| 40 | NS compactness limit | Exact | ✅ R_min = 7GM/c² (ε₁₁ < 1 ↔ 2GM/c²R < 2/7 = ν_vac) |
| 41 | WD redshift (Sirius B) | 3.7% | ✅ z = GM/(c²R), v_GR=77.75 km/s, v_obs=80.65±0.77 |
| 42 | α invariance (gravity) | Exact | ✅ Δα/α = 0 under Symmetric Gravity (Axiom 3) |
| 43 | BCS B_c(T) | 0.00% | ✅ B_c(T) = B_c0·S(T/T_c) IS the saturation operator (Al, Pb, Nb, MgB₂) |
| 44 | BH interior (Regime IV) | Exact | ✅ G_shear = 0, c_eff = 0 for r < r_sat = 7GM/c². Symmetric saturation → Z = Z₀, Γ = 0 (dissipative sink). |
| 45 | Regime IV isomorphism | — | ✅ BH (sym, hole) ≠ electron (asym, knot). Same S=0 operator, different saturation symmetry. |
| 46 | IE sweep Z=1–12 | 2.8% max | ✅ ODE cavity eigenvalue + Hopf mode split + hierarchical cascade (Be) + SIR boundary (Mg). Zero free parameters. |
| 47 | α thermal running (δ_strain) | 2.2×10⁻⁶ at T=2.7 K | ✅ CMB-induced expansion of the spatial metric; predicts α⁻¹ decreases in high-T regions. Falsifiable. See Ch.8 and `DELTA_STRAIN` in constants.py. |

Run: `python src/scripts/vol_1_foundations/derive_alpha_from_golden_torus.py` (cold-lattice α derivation; verifies ALPHA_COLD_INV = 4π³+π²+π and CMB correction δ_strain)
Rigorously justify π² (Clifford half-cover): `python src/scripts/vol_1_foundations/verify_clifford_half_cover.py` — derives Λ_surf = π² from spin-1/2 half-cover of the standard Clifford torus T² ⊂ S³ ⊂ ℂ², closing the π² normalization rigorously. Three-regime structure parallel to PMNS-angle derivation (Nyquist / crossings / screening).
Verify (definitive, numerical): `python src/scripts/vol_1_foundations/ropelength_trefoil_golden_torus.py` — minimizes ropelength + self-avoidance + holomorphic screening; converges to (R, r) = (φ/2, (φ-1)/2) exactly from arbitrary starting point.
Verify (algebraic + infrastructure): `python src/scripts/vol_1_foundations/verify_golden_torus_s11.py`

## Scale Invariance Principle

**ALL derived constants flow from ν_vac = 2/7 via the same projection pattern:**

| Scale | Quantity | Formula | Source |
|-------|----------|---------|--------|
| EW gauge | sin²θ_W | 2/9 | 2 weak modes / 9 angular sectors |
| EW gauge | cos(θ_W) | √(7/9) | Complementary sector |
| Strong gauge | α_s | α^(3/7) | 3 spatial / 7 compliance modes |
| CKM mixing | λ | 2/9 | = sin²θ_W (scale invariance) |
| CKM mixing | A | √(7/9) | = cos(θ_W) (scale invariance) |
| CKM mixing | √(ρ²+η²) | 1/√7 | Single-mode amplitude |
| PMNS mixing | base | 1/c₁c₃ = 1/45 | Torsional defects c₁=5, c₃=9 |
| PMNS mixing | sin²θ_12 | ν_vac + 1/45 | Baseline compliance overlap |
| Quark masses | m_s / m_μ | cos(θ_W) | Scale-invariant Cosserat map |
| Quark masses | m_u, m_d | m_e/α_s | Translation sector map |
| Protein packing | η_eq = P_C(1−ν) | P_C × 5/7 | 5 transverse / 7 total modes |
| Thermodynamics | g* | 7³/4 | 7 modes × K4 cell |
| Higgs sector | λ_H | 1/8 | 1/(2×N_K4) = K4 breathing |
| Baryon asymmetry | C_sph | 28/79 | N_f=3 torus knots |

**The numbers 7 (compliance modes) and 9 (angular sectors) appear at every scale
because the lattice structure is scale-invariant. This is not numerology — it is
the same Poisson ratio ν = 2/7 projecting through the same K4/SRS geometry.**

## Universal Regime Map

The saturation operator S(r) = √(1-r²) defines 4 universal regimes. **Boundaries are derived from first principles:**

| Regime | r range | Derivation | EE Analog | Example |
|--------|---------|------------|-----------|---------|
| **I Linear** | r < √(2α) ≈ 0.121 | ΔS = r²/2 < α (sub-α) | Small-Signal | Lab fields, Solar gravity |
| **II Nonlinear** | √(2α) ≤ r < √3/2 ≈ 0.866 | Full S(r) required | Large-Signal | PONDER-05 @ 30kV (r=0.687) |
| **III Yield** | √3/2 ≤ r < 1.0 | Q = 1/S ≥ 2 (ℓ_min) | Avalanche (M ≥ 2) | PONDER-05 @ 43kV (r=0.985) |
| **IV Ruptured** | r ≥ 1.0 | S = 0, Axiom 4 | Breakdown (M → ∞) | BH interior, magnetar |

See: `src/ave/core/regime_map.py` for the engine module, `manuscript/vol_1_foundations/chapters/08_regime_map.tex` for the full chapter.

**Galactic Note:** The operator S(r) is universal — S(r→1) = medium compliance → 0 in every domain. In the galactic domain (r = g_N/a₀), S→0 means lattice drag vanishes → Newtonian gravity. **The dark matter problem IS the Regime III→IV phase transition.** See `src/ave/gravity/galactic_rotation.py`.

## Development Phases

| Phase | Status | Summary |
|-------|--------|---------|
| **A: Engine Hardening** | ✅ Complete | 746 tests, PML/LBM/materials |
| **B: Domain Extension** | ✅ Complete | Seismology, water, plasma, superconductor, GW, stellar, neutrino, protein |
| **C: Predictions** | ✅ Complete | 46 predictions, ALL 26/26 SM Parameters Derived |
| **D: Hardware** | 🔒 Private | APU, PONDER, HOPF hardware maintained in separate repos |
| **E: Publication** | 🔄 Active | 7 public volumes, Yang-Mills + NS proofs |
| **F: Millennium Problems** | ✅ Complete | Yang-Mills ✅, Navier-Stokes ✅, Strong CP ✅ |

## Hardware & Applied Engineering

Hardware implementations (APU, PONDER, HOPF-01), the protein folding engine,
fusion research, and other applied engineering efforts are maintained in
separate private repositories within the `ave-veritas-et-enodatio` organization.

The physics engine in this repository is fully self-contained and does not
require any hardware modules to operate. All 46 predictions, proofs, and
validations run independently.

## Critical Distinctions (Common Errors to Avoid)

1. **V_SNAP ≠ V_YIELD.** V_SNAP = 511 kV is absolute destruction. V_YIELD = 43.65 kV is the onset of measurable nonlinearity. Lab experiments operate near V_YIELD, not V_SNAP.
2. **sin²θ_W = 2/9 (on-shell)** not 7/24 (which appears in some older manuscript sections). **Scheme note:** PDG reports two values — on-shell (0.2234, Δ=−0.52%) and MS-bar (0.2312, Δ=−3.89%). AVE derives the **on-shell** (tree-level) value. The MS-bar difference is standard one-loop radiative running.
3. **The baryon masses come from the Faddeev-Skyrme solver**, not a simple formula. The crossing number sets confinement but the eigenvalue requires numerical minimization.
4. **Galaxy rotation uses derived a₀ = cH∞/(2π) ≈ 1.07×10⁻¹⁰** (−10.7% from empirical 1.2×10⁻¹⁰). This is NOT a free parameter — it emerges from the asymptotic Hubble constant H∞ = 28πm_e³cG/(ℏ²α²). See `src/ave/gravity/galactic_rotation.py`.
5. **The SPICE RC muon model is qualitative.** The quantitative lifetime comes from the Fermi formula with AVE-derived G_F (3.9% accurate).


## Protein Folding Engine

> The protein folding engine (S₁₁ impedance cascade) is maintained in a separate
> private repository (`AVE-Protein`). The theoretical foundation (Vol 5, Ch. 01–02)
> describes the LC mapping of amino acids and is included in this repo.
> The implementation engines and simulation scripts are proprietary.


## Collaborative Git Workflow (Code Hygiene)

For both humans and AI assistants working on the AVE codebase, the `main` branch acts as the stable golden master. All new computational, formatting, or theoretical work must occur on isolated feature branches and be merged via Pull Requests.

### The Hardware-to-Software Dictionary
*   **`main` branch** = Golden Master Schematic. Everything here must build, run, and pass all tests. Once collaborators join the project, *nobody* edits this directly without a PR.
*   **Feature Branch** = Prototyping on a Breadboard. You copy the golden schematic, experiment in isolation without breaking the main design, and throw it away if it fails.
*   **Pull Request (PR)** = Formal Design Review. You present your breadboard prototype to the team: "Here is my proposed change to the golden schematic. Please review my logic."
*   **Unit Tests (`make verify`)** = DRC / ERC checks. Automated verification ensuring your new prototype didn't break backward compatibility.

### Standard Operating Procedure
1. **Sync to Golden Master:** Always start your work with the latest code.
   ```bash
   git checkout main
   git pull origin main
   ```
2. **Create a Sandbox (Branch):** Use a descriptive prefix (`feature/`, `fix/`, `docs/`, `audit/`).
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Execute "DRC" Checks (Testing):** Before saving, ensure no axioms or tests broke.
   ```bash
   PYTHONPATH=src python -m pytest tests/
   ```
4. **Snapshot Changes (Commit):** Group logical changes with clear, descriptive rev notes.
   ```bash
   git add <files>
   git commit -m "feat/fix/docs: concise description of changes"
   ```
5. **Publish and Open Design Review (PR):** Push your branch to the central repository and open a Pull Request on GitHub to invite reviewer feedback before merging.
   ```bash
   git push -u origin feature/your-feature-name
   ```

## Rules for AI Assistants

1. **Read this document first** before making changes to core physics.
2. **Never modify constants.py** without explicit user approval.
3. **Never modify the 4 axioms** — they are the foundation.
4. **Always run tests** after engine changes: `./.venv/bin/pytest tests/ -q`
5. **Use the existing engine** for simulations — don't build separate solvers.
6. **Commit frequently** with descriptive messages listing what changed.
7. **Check V_YIELD vs V_SNAP** — most lab-relevant physics uses V_YIELD = 43.65 kV.
8. **The manuscript is the source of truth** for formulas. Check `manuscript/` before deriving.
9. **Engine architecture changes must propagate to LaTeX.** When any function, module, or constant in the three-tier engine (Core → Domain Adapters → Solvers) is added, renamed, moved, or deleted, search **all** `.tex` files for references to the affected names and update them. Use `grep -rn` across `manuscript/` to ensure no stale references remain.
10. **Every script must import constants from `ave.core.constants`.** No hardcoded physics constants (α, mₑ, c, ℏ, ε₀, μ₀, Z₀, etc.). The engine is the single source of truth. Engineering parameters (wire lengths, PCB dimensions, operating frequencies) are permitted but must be documented with a comment citing their source.
11. **`scipy.constants` is banned.** All physical constants come from `ave.core.constants`. Using `scipy` for math tools (`scipy.optimize`, `scipy.linalg`, `scipy.signal`) is fine — the ban is specifically on `scipy.constants`. Enforced by AST check in `verify_universe.py`.
12. **No smuggled data.** Scripts must not normalize outputs to match experimental data, curve-fit to known values, or use ad-hoc correction factors. If a result disagrees with experiment, document the discrepancy — do not hide it with fitting. Exception: `np.polyfit` for parity plots (predicted vs. experimental) is acceptable for diagnostic purposes only.
13. **Translation tables are canonical.** Domain-specific terminology mappings live in `manuscript/common/translation_*.tex`. They are `\input`'d into chapters and the backmatter Rosetta Stone. Change the table once, every reference updates automatically.

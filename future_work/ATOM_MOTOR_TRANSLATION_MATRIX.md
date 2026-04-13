# Atom ↔ AVE Axiom ↔ EE Circuit: Translation Matrix

> **Status:** Working document. Each term audited against AVE first principles.
> **Purpose:** Map every component of the atomic IE solver to AVE axioms and EE
> circuit terminology. Where motor/EE terms don't map exactly to the lattice,
> AVE-native names are provided.

## The VCA Dictionary (Reference)

| Electrical | Mechanical | Mapping |
|-----------|-----------|---------|
| Charge Q | Displacement x | Q = ξ_topo · x |
| Current I | Velocity v | I = ξ_topo · v |
| Voltage V | Force F | V = F / ξ_topo |
| Inductance L | Mass m | L = m / ξ_topo² |
| Capacitance C | Compliance κ | C = ξ_topo² · κ |
| Resistance R | Viscosity η | R = η / ξ_topo² |

---

## Motor → AVE Terminology Corrections

> Not all motor terms translate literally. The atom is embedded IN the lattice
> medium, not sitting in free space like a motor on a bench. This changes
> several concepts fundamentally.

| Motor/EE Term | AVE-Native Term | Why the rename |
|--------------|----------------|---------------|
| Stator excitation | **Nuclear strain source** | No rotation — static topological charge (Ax2) |
| Stator MMF profile | **Net Coulomb bias** Z_net(r) | Gauss law superposition, not winding geometry |
| Rotor winding | **Orbital soliton** | Self-sustaining topological defect (Ax2+4), not induced |
| Rotor speed ω_r | **Cavity resonant frequency** | Standing wave eigenfrequency, not mechanical RPM |
| Back-EMF | **Lattice strain density** | Not a voltage — the medium itself deforms (Ax4) |
| Rotor slot leakage X_l | **Centrifugal barrier** l(l+1)/r² | Angular winding number (Ax1), not parasitic flux |
| Core saturation | **Metric strain saturation** S(A) | Identical math (Ax4 kernel), identical physics |
| Slip s = (ω_s−ω_r)/ω_s | **Strain modulation frequency** | Beat between cavity modes — no rotating frame |
| Slip I²R loss | **Metric relaxation drag** | Energy → lattice rearrangement, not resistive heating |
| Armature reaction | **Cross-shell strain coupling** | Valence soliton's field modifies core lattice properties |
| Motor Q-factor | **Cavity finesse** | Q = n²/(Z_eff·α) — resonator quality |
| Transformer coupling M | **Hopf mutual inductance** | Topological linking number (Ax3), not magnetic circuit |
| Stator-rotor M_sr | **Cross-shell Hopf coupling** | Same-l solitons on different n linked by torus topology |
| Locked rotor (s≈1) | **Maximally asynchronous regime** | All slip ratios near unity for atom |

---

## Layer 0: The Static Structure

| Atomic Physics | AVE Axiom | EE Circuit (approximate) | AVE-native term |
|---------------|-----------|------------------------|----------------|
| Nucleus (Z protons) | Ax2: Z topological dislocations | DC voltage source | **Nuclear strain source** |
| V = −Ze²/(4πε₀r) | Ax2: capacitive bias on LC lattice | Supply voltage V_bus | **Nuclear Coulomb bias** |
| a₀ = ℏ/(m_e·c·α) | Ax1+2: LC resonant length | Characteristic impedance reference | **Lattice resonant scale** |
| Electron soliton | Ax2+4: standing wave, m=ℏω/c² | LC resonator | **Orbital soliton** |
| m_e | Ax4: L_e = m_e/ξ² ≈ 5.3 aH | Inductor | **Soliton inductance** |
| ω = Z²Ry/(ℏn²) | Ax1: ω = 1/√(LC) | Resonant frequency | **Cavity resonant frequency** |
| α = e²/(4πε₀ℏc) | Ax2: Z_soliton/Z₀ | Coupling coefficient k | **Impedance ratio** (exact) |

---

## Layer 1: Single-Soliton Eigenvalue (Phase A)

| Physics | Axiom | Solver | Status | Audit Note |
|---------|-------|--------|--------|------------|
| Helmholtz ψ'' = k²ψ | Ax1: LC wave equation | `_radial_ode()` | ✅ | Correct — the Helmholtz equation IS the LC lattice wave equation |
| V(r) = −Z_net/r | Ax2: Gauss CDF screening | `_z_net()` | ✅ | Correct — net field drives force on soliton. CDF is exact for spherically-averaged charge |
| l(l+1)/r² barrier | Ax1: angular winding quanta | `_radial_ode()` L435 | ✅ | Correct — angular momentum is a lattice topological invariant |
| E eigenvalue | Ax3: S₁₁ = 0 (least reflection) | `brentq` root search | ✅ | Correct — eigenvalue = zero-reflection resonance |
| **S_r = S(V_strain)** | **Ax4: metric varactor** | `universal_saturation()` L445 | **⚠️ AUDIT FLAG** | **V_strain uses Z_net. See GAP A below** |
| Quantum defect δ | Ax1+2: graded profile | ODE integration | ✅ | Naturally resolved — no separate operator needed |
| **Cross-shell strain** | **Ax3+4 (unimplemented)** | — | ❌ | **GAP B: lattice strain density from inner solitons** |
| **Metric relaxation** | **Ax1+4 (unimplemented)** | — | ❌ | **GAP C: time-varying lattice at beat frequency** |

---

## Layer 2: Same-Shell Multi-Soliton (Phase B)

| Physics | Axiom | Solver | Status | Audit Note |
|---------|-------|--------|--------|------------|
| k_pair = (2/Z_eff)(1−P_c/2) | Ax3+4: Hopf mutual inductance | coupled resonator | ✅ | Derived from Hopf linking — verified on He |
| K_N graph eigenvalue | Ax1: N-resonator complete graph | eigenvalue formula | ✅ | Standard circuit theory on LC network |
| MCL T² = 4N/(1+N)² | Ax1: impedance match at boundary | `_cavity_transmission_sq()` | ✅ | Single-port impedance match — derived |
| p-weight = 0.5 = (1+cos90°)/2 | Ax1: torus crossing geometry | MCL weight | ✅ | Derived from K=2G and crossing angle |
| d/f weights = 0.0 | ??? | placeholder | ⚠️ | **GAP D: need derivation from crossing angle** |
| **Cross-n coupling** | **SCF iteration (speed ↔ torque)** | ??? | ❌ |

---

## FOC Diagnosis: Scalar Control vs Vector Control

### Phase A/B/C = Scalar Control (WRONG for coupled systems)

The current solver decomposes the atom into sequential, uncoupled phases:
1. Phase A: One soliton in mean field (CDF screening, no feedback)
2. Phase B: Same-shell coupling correction (Hopf mode splitting)
3. Phase C: Symmetry penalty (crossing scattering)

This is the EE equivalent of **scalar V/f control** — it works when
cross-coupling is weak (l≥1, p-orbitals) but fails when:
- The screening and exchange axes are strongly coupled (s-orbital core penetration)
- The operating point changes rapidly (ionization = removing a resonator)

### FOC Prescription: Simultaneous Coupled Solve

FOC solves the COUPLED dq equations simultaneously:
```
[V_d]   [R    -ω·L_q] [I_d]   [  0  ]
[V_q] = [ω·L_d    R ] [I_q] + [ω·λ  ]
```

The cross terms `ω·L·I` couple the axes. Dropping them (= scalar control) 
gives 7-15% error — matching our IE error exactly.

### Minimum viable fix: Feed-Forward Decoupling

Instead of full SCF iteration, add an analytical correction from the
cross-shell stub reflected impedance (Op4 Coulomb coupling, not Hopf):
```
ΔE = k²_cross × E_val × E_inner / (E_inner − E_val) × (residual fraction)
```
This cancels the cross-coupling at first order.

### Why s-orbitals fail and p-orbitals work

- l=0 (s): no centrifugal barrier → deep core penetration → large cross-coupling → scalar control fails
- l≥1 (p,d): centrifugal barrier → no penetration → cross-coupling negligible → scalar control sufficient

---

## Layer 3: Symmetry (Phase C)

| Physics | Axiom | Solver | Status | Audit Note |
|---------|-------|--------|--------|------------|
| Crossing count | Ax1: 2 crossings/rev × 2 electrons | `_pairing()` | ✅ | Torus topology gives exactly 2 intersections/revolution |
| Scattering α per crossing | Ax2: α = impedance ratio | `_pairing()` | ✅ | Each crossing scatters Z_soliton/Z₀ = α fraction |
| Saturation cap at 6 | Ax1: 3 axes × 2 intersections | `_pairing()` | ✅ | Geometric maximum from torus topology |

---

## The Gaps (AVE-native framing)

### GAP A: Strain saturation input — screened or total?

**Current code (L439-445):**
```python
V_strain_J = Z_net * ALPHA * HBAR * C_0 / r     # ← uses Z_NET
local_strain_amplitude = V_strain_J / (M_E * C_0**2)
S_r = universal_saturation(local_strain_amplitude, 1.0)
```

**The question:** The metric varactor (Ax4) saturates based on the LOCAL lattice strain. But what determines the strain?

**Option 1 — Net field (current code):** V_strain = Z_net × αℏc/r. The screening cancels part of the nuclear strain. The lattice sees only the resultant.

**Option 2 — Total field energy:** The lattice strain is the energy density u = ½ε₀E². For superposed fields, E²_total = (E_nuc + E_el)² = E²_net. So this equals Option 1 for classical superposition.

**Option 3 — Strain density (user's insight):** The inner solitons each create their own lattice deformation. These deformations don't fully cancel because the solitons are DISCRETE — they LOCALLY strain the lattice at their instantaneous positions. The TIME-AVERAGED strain includes a variance term:

⟨E²⟩ = E²_mean + Var(E) > E²_mean

The variance comes from the discrete, time-varying positions of inner solitons. This term IS the "lattice strain density" beyond the mean-field.

**Under AVE:** The lattice responds to the INSTANTANEOUS field (Axiom 1: LC lattice, no averaging). The discreteness of solitons creates fluctuations. The saturation S should use the RMS field, not the mean field. This connects directly to the user's RMS insight.

### GAP B: Cross-shell strain coupling

When the 3s soliton enters the n=2 region, it experiences a lattice that's ALREADY strained by the 8 n=2 electrons. This pre-existing strain modifies ε_eff and μ_eff, changing:
- c_local = S × c (phase velocity drops)
- Z_local = Z₀ (impedance invariant — gravitational stealth)
- ω_local shifts (C_eff and L_eff both increase)

The current ODE accounts for the FORCE (Z_net) but NOT for the medium change (S from inner-shell strain). The inner shells strain the lattice independently of whether they screen the Coulomb field.

### GAP C: Metric relaxation drag

The inner solitons orbit at frequencies ω_inner >> ω_valence. Their charge density at any point oscillates at ω_inner. This creates a time-varying ε_eff(r, t) and μ_eff(r, t).

The valence soliton propagates through this oscillating medium. Under Axiom 1 (LC lattice), a time-varying C or L creates PARAMETRIC coupling — energy transfers between the soliton and the lattice modulation.

This is NOT friction (no energy leaves the system). It's a REACTIVE redistribution that shifts the eigenfrequency. In EE terms: parametric oscillation in a varactor-tuned LC circuit.

### GAP D: d/f shell loading weights

Derivation path: Op10 junction projection at the d-orbital crossing angle. The crossing angle between s and d tracks on the torus is θ_sd. The weight should be:

w_d = (1 + cos θ_sd)/2

Need to determine θ_sd from torus geometry (Axiom 1).

### GAP E: Cross-n topology — RESOLVED (no Hopf)

**Q1 research result (2026-04-07):** geometry-pipeline.md, line 27, explicitly
classifies different-shell solitons as "None (concentric), 0 crossings,
topology factor = 1." Cross-shell solitons have NO Hopf link. Their coupling
is purely Coulomb (Op4), not topological (Op2). The cross-n coupling is the
orbit-averaged Coulomb integral via complete elliptic integral K(R_a/R_b):

```
k_cross = ⟨V_ab⟩ / √(E_0,a × E_0,b)
⟨V_ab⟩ = (2αℏc)/(πR_b) × K(R_a/R_b)
```

This coupling enters as stub reflected impedance, not Hopf back-EMF.

---

## Strain Budget (Na Example)

| Source | Strain at r=0.01a₀ | Strain at r=0.5a₀ | Strain at r=9a₀ |
|--------|-------------------|-------------------|-----------------|
| Nuclear (Z=11) | 0.059 | 0.0012 | 0.00007 |
| Inner 1s² (Z_eff=11) | -0.059 × σ₁ₛ | -0.0012 × 0.998 | ~0 |
| Inner 2s²2p⁶ (Z_eff=9) | ~0 (σ₂≈0) | -0.0012 × 0.415 | ~0 |
| **Net (Z_net)** | **0.059** | **0.00068** | **0.00007** |
| **Inner self-strain** | **???** | **???** | **0** |

The "inner self-strain" row is the VARIANCE term — the strain from inner electron charge density that doesn't cancel in the net. This is the missing term. Its magnitude in the core penetration zone (0.1–2 a₀) determines the size of the eigenvalue shift.

---

## Summary: Solver Coverage vs First-Principles Requirements

| AVE Requirement | What we compute | What we should compute | Gap |
|----------------|----------------|----------------------|-----|
| Force on valence (Ax2) | Z_net(r) — net Coulomb | Z_net(r) — net Coulomb | ✅ None |
| Medium properties (Ax4) | S(Z_net·α/r) — net strain | S(⟨E²⟩_rms) — total strain density | ❌ **GAP A** |
| Cross-shell topology (Ax3) | None | Hopf phase constraint across n | ❌ **GAP E** |
| Time-varying medium (Ax1) | None | Parametric coupling at ω_beat | ❌ **GAP C** |
| Inner soliton locality (Ax2) | σ(r) average | σ(r) + variance (discrete solitons) | ❌ **GAP A** |

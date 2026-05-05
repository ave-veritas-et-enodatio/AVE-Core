[↑ Quantum Orbitals](../index.md)
<!-- path-stable: referenced from vol5 as ch:quantum_mechanics (source label in vol2: ch:quantum_orbitals) -->
<!-- claim-quality (subtree): ak97cb, oltvwy, qde5gn, w6kk5y -->

# Ch. 7: Quantum Mechanics and Atomic Orbitals

Chapter 7 reinterprets the Schrödinger wave equation as the continuous Helmholtz acoustic resonance of a discrete 3D topological LC cavity. It derives exact hydrogen energy levels, the Bohr radius, angular momentum quantization, and multi-electron ionization energies through a mutual cavity loading architecture and Y-matrix eigenvalue solver — all from the four AVE axioms with zero free parameters.

## Key Results

| Result | Statement |
|---|---|
| Helmholtz-Schrödinger isomorphism | $\nabla^2 \Psi + k^2(r)\Psi = 0$ with $k^2(r) = \frac{2m}{\hbar^2}(E - V(r))$ |
| Hydrogen ground state energy | $E_n = -\frac{m_e c^2 \alpha^2}{2n^2} = -13.606$ eV for $n=1$ |
| Bohr radius | $a_0 = \frac{l_{node}}{\alpha} \approx 5.29 \times 10^{-11}$ m ($137 \times l_{node}$) |
| Angular momentum | $L = \hbar\sqrt{l(l+1)}$, $l = 0, 1, \ldots, n-1$ |
| De Broglie refractive index | $n(r, \xi) = \sqrt{2\,Z_{\text{eff}}(r)\,a_0/r - \xi}$ |
| AVE screening rule | $\sigma_{\text{total}} = N_{\text{inner}} + (N_{\text{same}} - 1) \times J_{\text{shell}}$ |
| Helium IE (mutual cavity loading) | $IE_{\text{He}} = 24.19$ eV ($\Delta = -1.6\%$ from 24.587 eV target) |
| Bonding mode formula | $E_{n,\text{bond}} = \frac{Z^2 R_y / n^2}{\sqrt{1 + k_n(N_n - 1)}}$ |
| Complete solver pipeline | Op4 $\to$ Y-matrix (Op5) $\to$ S-parameters $\to$ Op6 eigenvalue |
| Atom as radial waveguide | ABCD cascade through graded impedance profile |
| Radial eigenvalue solver | Eigenvalues at $S_{11}$ dips via ABCD cascade |
| Dual-formalism architecture | Knot-topology operators (Op2, Op4) + orbital-geometry operators (Y-matrix, ABCD) |
| Scale separation | Knot topology at $l_{node}$ scale vs orbital geometry at $a_0$ scale |
| Helium coupling $J_{s^2}$ | $J_{s^2} = \frac{1}{2}(1 + p_c) = 0.5917$ |
| Chiral factor $p_c$ | $p_c = 8\pi\alpha$ as topological coupling |
| Orbital penetration (1/d) | $l$-degeneracy splitting from deterministic impedance mismatch, not probabilistic Born rule |

## Derivations and Detail

| Document | Contents |
|---|---|
| [De Broglie Standing Wave](./de-broglie-standing-wave.md) | Helmholtz-Schrödinger isomorphism, acoustic cavity interpretation, hydrogen ground state, Bohr radius, angular momentum quantization, Steps 1a-1h single-electron eigenvalue derivation |
| [De Broglie Refractive Index](./de-broglie-n.md) | Energy-dependent refractive index $n(r,\xi)$ on the AVE lattice |
| [Screening Rule](./screening-rule.md) | Cross-shell (Gauss/Axiom 2) and same-shell (lattice/Axiom 4) screening |
| [ODE Verification](./ode-verification.md) | Numerical ODE shooting-method verification of hydrogen eigenvalues |
| [Helium Symmetric Cavity](./helium-symmetric-cavity.md) | Multi-electron mutual cavity loading architecture, FOC orthogonality |
| [QM-AVE Translation](./qm-ave-translation.md) | Pointer to QM $\leftrightarrow$ AVE translation dictionary |
| [Analog Ladder Filter](./analog-ladder-filter.md) | Atom as passive analog ladder network, multi-shell filter cascade |
| [Macro Cavity Saturation](./macro-cavity-saturation.md) | Supersession of N-port Y-matrix by mutual cavity loading |
| [Geometry Pipeline](./geometry-pipeline.md) | Complete geometry-to-solver pipeline (Stages A-E) |
| [Bonding Mode Formula](./bonding-mode-formula.md) | Same-shell bonding mode eigenvalue derivation (Stage E1) |
| [Complete Solver Architecture](./complete-solver-architecture.md) | Five-step solver: Op4 $\to$ Op5 $\to$ Op6 pipeline |
| [Atom as Radial Waveguide](./atom-as-radial-waveguide.md) | Radial transmission line interpretation connecting Steps 1+2 |
| [Radial Eigenvalue Solver](./radial-eigenvalue-solver.md) | ABCD cascade radial eigenvalue solver |
| [Dual-Formalism Architecture](./dual-formalism-architecture.md) | E2 summary combining knot-topology and orbital-geometry operators |
| [Scale Separation](./scale-separation.md) | Knot topology vs orbital geometry two-scale framework |
| [Subshell Junction Scattering](./subshell-junction-scattering.md) | Phase 5: Op10 boron drop derivation at sub-shell junctions |
| [Knot vs Orbital Table](./knot-vs-orbital-table.md) | Tabular comparison of knot topology and orbital geometry |
| [Operator Domain Table](./operator-domain-table.md) | Operator domain assignment for the IE solver |
| [Helium Coupling First Principles](./helium-coupling-first-principles.md) | Helium $J_{s^2}$ derivation from lattice geometry |
| [Chiral Factor](./chiral-factor.md) | $p_c$ as topological coupling between knot and orbital sectors |
| [Stepped Impedance Resonator](./stepped-impedance-resonator.md) | Atom as a Stepped Impedance Resonator |
| [Hierarchical Cascade Correction](./hierarchical-cascade-correction.md) | Hierarchical Cascade Correction for Be |
| [Ionization Energy Validation](./ionization-energy-validation.md) | Ionization Energy Validation: Z = 1 to 14 |
| [Orbital Penetration Penalties](./orbital-penetration-penalties.md) | 1/d ABCD impedance mismatch breaks $l$-degeneracy; Lithium 2s/2p splitting validation |

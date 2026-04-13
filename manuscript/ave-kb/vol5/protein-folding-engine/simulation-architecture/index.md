[↑ Protein Folding Engine](../index.md)

# Simulation Architecture: $S_{11}$ Protein Folding Engine

This chapter documents the complete computational architecture of the axiom-derived protein folding engine. Every equation is mapped to the corresponding implementation in the physics engine. The engine uses a torsion-angle parameterisation: the backbone is a fixed-length conductor where bond lengths and angles are enforced by construction (NERF algorithm). Only the Ramachandran torsion angles $(\varphi_i, \psi_i)$ are free parameters, giving $2N$ degrees of freedom.

## Key Results

| Result | Statement |
|---|---|
| Total objective function | $\mathcal{L}(\varphi, \psi) = \overline{\|S_{11}\|^2} + \frac{\lambda_s}{N} \sum_{\|i-j\|\geq 3} \max(0, r_{\text{steric}} - d_{ij})^2 + \mathcal{L}_{\text{port}} + \mathcal{L}_{\text{Rama}} + \mathcal{L}_{\text{xtalk}}$ |
| Segment characteristic impedance | $Z_\text{seg} = \sqrt{m_\text{Da}/n_e}$; N--C$_\alpha$: 3.606, C$_\alpha$--C: 3.464, C--N: 2.944 |
| Eigenvalue root target | Find $\boldsymbol{\theta}$ such that $f(\boldsymbol{\theta}) = \lambda_{\min}(S^\dagger S) \cdot S_\text{pack} + \mathcal{P}_\text{steric} = 0$ |
| SPICE transient integration | $v_i(t + \Delta t) = v_i(t) + (-\nabla_i f - R \cdot v_i)/L \cdot \Delta t$; physical ring-down, not gradient descent |
| Zero-parameter count | 0 trainable parameters, 21 derived constants, 7 universal operators, 1 objective function |
| 20-sequence stress test (v3) | 19/20 pass; Poly-D fails (expected: homopolyanion self-repulsion) |
| Villin HP35 validation | SS = 88%, $R_g$ = 5.1 \AA, 100% correct $\phi$ chirality |
| Four-protein equilibrium size | $R_g$ matches $\eta_\text{eq}$-predicted values to 0.5--7.6% across 20--76 residues |
| Y-shunt balance theorem | Additional admittance at C$_\alpha$ junctions over-damps resonant modes from which SS emerges |
| 1D cascade SS ceiling | $Y_\text{shunt}$ (scalar admittance) provides damping only; TL stub provides resonance |
| Architectural ceiling | Q-decay SS = 22.8% is maximum achievable within 1D cascade axiom compliance |
| v7 multi-scale results | Trp-cage: $R_g$ err 0.0%, SS 39%; Villin: $R_g$ err 4.1%, SS 24% |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Axiom-Derived Constants](./axiom-derived-constants.md) | Tier 1: 17 engine constants with full axiom derivation chains, including v4 upgrades |
| [Complex $Z_{topo}$ Table](./z-topo-complex-table.md) | Tier 2: complex topological impedance $Z_i = R_i + jX_i$ for all 20 amino acids, charge reactance formula |
| [Dielectric Saturation Amplification](./dielectric-saturation-amplification.md) | Layers 1--2: conjugate shunt admittance, Axiom 4 dielectric saturation amplification |
| [Physics Layers 3, 3b, 3c](./physics-layers-1-4.md) | Layer 3: solvent impedance boundary; Layer 3b: backbone H-bond coupling (TL node mutual inductance); Layer 3c: adjacent peptide-plane coupling |
| [Segment Characteristic Impedance](./segment-characteristic-impedance.md) | Layer 4: full backbone ABCD cascade, segment impedances from nuclear mass and shared electrons, per-residue $\mu$ enhancement, lossy propagation, ABCD matrix |
| [Physics Layers 5--8](./physics-layers-5-8.md) | Layer 5: multi-frequency integration; Layer 6: non-reciprocal chirality phase; Layer 7: cross-coupled cavity filter; Layer 8: bond integrity and steric exclusion |
| [Solver Architecture](./solver-architecture.md) | Newton-Raphson eigenvalue root-finding, SPICE transient integration, cotranslational cascade (v7), Ramachandran-basin initialisation |
| [Script Reproduction Procedure](./script-reproduction-procedure.md) | Reproduction commands, code--equation map, dependency table |
| [Zero-Parameter Count](./zero-parameter-count.md) | Zero-parameter summary, universal operator cross-reference (7 operators), Axiom 4 saturation operators, regime boundaries |
| [Stress Test v3](./stress-test-v3.md) | 20-sequence homopolymer stress test, Poly-D failure analysis |
| [Villin HP35 Validation](./validation-villin-hp35.md) | Villin HP35 benchmark, 5-atom backbone steric (Upgrade 10), H-bond mutual inductance (Upgrade 8), constraint layers table |
| [Three-Protein Validation](./validation-three-protein.md) | Four-protein validation table, equilibrium packing $\eta_\text{eq}$, 5-atom steric validation, coupled 2D Ramachandran basins, Y-shunt balance diagnostic, Q-decay weighting results |
| [Limitations of the 1D Cascade](./limitations-1d-cascade.md) | Y-shunt balance theorem, coupling modification audit, architectural ceiling (three fundamental limitations) |
| [SS Recovery Design Path](./ss-recovery-design-path.md) | Mode projection ($\nu_\text{vac} = 2/7$), semiconductor depletion region analysis, MOSFET--backbone mapping, per-residue saturation, SPICE model analysis |
| [Architectural Ceiling Theorem](./architectural-ceiling-theorem.md) | Formal theorem and proof (by construction), ceiling evidence table (6 approaches tested) |
| [Multi-Scale Impedance Architecture](./multiscale-impedance-architecture.md) | Lumped/distributed/network hierarchy, segmentation at impedance discontinuities, nodal $Y$-matrix $S_{11}$ energy function, v7 results table |

---

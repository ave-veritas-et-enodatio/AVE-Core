[↑ Vol 5 — Topological Biology](../index.md)

# Protein Folding Engine

The protein folding engine reformulates the folding problem as deterministic impedance matching on a transmission-line backbone, progressing through three chapters: per-residue $Z_\text{topo}$ definition and secondary structure prediction (Ch.3), an 8-tier simulation architecture with SPICE transient integration (Ch.4), and a multi-path 2D TL network solver with folding timescale derivation and 20-protein PDB validation (Ch.5). Zero empirical parameters throughout.

## Key Results

| Result | Statement |
|---|---|
| Topological Impedance | $Z_\text{topo} = R + jX$ per residue, range $[0.30, 0.96]$; derived from $\sqrt{M/n_e}$ |
| $S_{11}$ Objective Function | $E(\mathbf{r}) = |S_{11}(\mathbf{r})|^2$; folding $\equiv$ impedance matching |
| Backbone eigenfrequency | $f_0 = 21.7$ THz ($+0.1\%$ vs IR amide-V); $Q = 7$ from universal eigenvalue method |
| Eigenvalue Root Target (v5) | $f(\boldsymbol{\theta}) = \lambda_{\min}(S^\dagger S) \cdot S_\text{pack}(\eta) + \mathcal{P}_\text{steric}$ |
| SPICE Transient Integration | Physical ring-down with derived damping $R \approx 0.887$; not gradient descent |
| Full Kramers Folding Time | $\tau_\text{fold} = Q^2 N \tau_\text{water} \exp(0.471 \cdot N \cdot \text{CO})$; $\beta = 0.471$ matches empirical $0.452$ within 4.1% |
| Folding Speed Limit | $\tau_\text{min} = 7N/(23\;\text{THz})$; falsifiable lower bound |
| 20-Protein PDB Validation | $R_g$ median error 3.5%, mean SS 21%, zero crashes |
| $\tau_\text{fold}$ Validation | $R = 0.87$, MAE $= 1.4$ decades, 15 two-state folders, zero fitted parameters |
| v7 Segmented Cascade | 3-phase cotranslational solver; Protein G 9.91 Å (vs 18.62 Å v4) |
| Zero-Parameter Count | 0 trainable parameters, 21 derived constants, 7 universal operators |
| Chignolin RMSD | 2.59 Å, zero adjustable parameters |
| Derived Ramachandran Basins | $\varphi_\alpha = -60^\circ$, $\psi_\alpha = -37.3^\circ$, $\varphi_\beta \approx -125.3^\circ$, $\psi_\beta = +125.3^\circ$ |
| Backbone Y-Parameters | $y^\text{mutual} = -\operatorname{csch}(\gamma\ell)/Z_\text{eff}$, $y^\text{self} = \coth(\gamma\ell)/Z_\text{eff}$ |
| Architectural Ceiling | Q-decay SS = 22.8% is maximum achievable within 1D cascade axiom compliance |
| Op2 Crossing Correction | $\delta E_\text{knot} = c_\min \times 2\pi\alpha \times E_\text{coupling}$; predicts $\sim$99% unknotted |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Deterministic Folding (Ch.3)](./deterministic-folding/index.md) | $Z_\text{topo}$ definition, $S_{11}$ objective function, backbone eigenvalue solver, 20-sequence stress test, Chignolin RMSD, Ramachandran derivation, Op2 crossing correction, dual-formalism architecture |
| [Simulation Architecture (Ch.4)](./simulation-architecture/index.md) | 8-tier simulation architecture, axiom-derived constants, segment impedances, solver architecture (Newton-Raphson + SPICE transient), zero-parameter count, Villin HP35 validation, 1D cascade limitations, architectural ceiling theorem |
| [Network Solver (Ch.5)](./network-solver/index.md) | 2D TL network, Y-matrix gradient architecture, compaction physics, folding timescale derivation, 20-protein PDB validation, v7 segmented cascade, allostery, $\beta$-sheet coupler, bend admittance, frequency-domain analysis, neural TL extensions |

---

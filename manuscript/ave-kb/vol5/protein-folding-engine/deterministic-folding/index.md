[↑ Protein Folding Engine](../index.md)

# Deterministic Protein Folding

This chapter reformulates protein secondary structure prediction as deterministic impedance matching on a transmission line backbone, using $Z_{topo}$ derived from first principles with zero empirical structural data.

## Key Results

| Result | Statement |
|---|---|
| Topological Impedance | $Z_{topo} \equiv |Z_{\text{backbone}}(\omega_0)| / |Z_R(\omega_0)|$; per-residue complex impedance $Z_{topo} = R + jX$ for all 20 amino acids, range $[0.30, 0.96]$ |
| $S_{11}$ Objective Function | $E(\mathbf{r}) = |S_{11}(\mathbf{r})|^2$ where $S_{11} = (A + B/Z_0 - CZ_0 - D)/(A + B/Z_0 + CZ_0 + D)$ |
| Backbone eigenfrequency | $f = \ell \cdot v / (2\pi\, r_\mathrm{eff}) = 21.7$ THz (error: $+0.1\%$ vs IR); $Q = \ell = 7$ from universal eigenvalue method |
| 20-sequence stress test | 19/20 (95%) correct secondary structure classification, zero free parameters |
| Chignolin RMSD | 2.82 Å ($S_{11}$ minimiser), $R_g$ 96% of PDB value, zero adjustable parameters |
| Chou--Fasman correlation | Pearson $r = +0.61$, classification 15/20, from first-principles Ramachandran derivation |
| Op2 crossing correction | $\delta E_{\rm knot} = c_{\min} \times 2\pi\alpha \times E_{\rm coupling}$; predicts $\sim 99\%$ of proteins unknotted |
| Dual-formalism architecture | ABCD cascade (secondary) + Y$\to$S network (tertiary) + Op2 crossing penalty (topological) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [AVE Topological Impedance](./ave-topological-impedance.md) | $Z_{topo}$ definition, SPICE backbone impedance ratio, full 20-amino-acid table |
| [Multiplexed Basis States](./multiplexed-basis-states.md) | Helix/sheet basis state superposition and deterministic collapse |
| [3D Gradient Descent Engine](./gradient-descent-engine.md) | 8-channel force architecture: excluded volume, backbone springs, bend-angle, chirality, H-bond pairing, hydrophobic coupling, helix $i{\to}i{+}4$ springs, $S_{11}$ feedback gain |
| [SPICE TL Mismatch](./s11-strain-transmission-line.md) | Cascaded SPICE AC simulation validating $S_{11}$ strain as folding driver |
| [20-Sequence Stress Test](./stress-test-20-sequence.md) | Full 20-protein validation table across helices, sheets, mixed, edge cases |
| [Backbone Eigenvalue Solver](./backbone-eigenvalue-solver.md) | 5-step universal eigenvalue derivation of $f_0 = 21.7$ THz, $Q = 7$ |
| [Comparison with Statistical Approaches](./s11-feedback-gain.md) | AVE zero-parameter architecture vs AlphaFold statistical interpolation |
| [$S_{11}$ Objective Function](./s11-objective-function.md) | Single-criterion impedance matching, chirality phase, cross-coupled cavity filter, autodiff acceleration |
| [Ramachandran Derivation](./ramachandran-derivation.md) | First-principles $Z_{topo}$ from steric exclusion + H-bond competition; Chou--Fasman validation |
| [RMSD Benchmark](./rmsd-benchmark-pdb.md) | Kabsch RMSD against PDB for Chignolin, Trpzip2, Trp-cage, Villin |
| [Dual-Formalism Architecture](./dual-formalism-architecture.md) | Atom $\leftrightarrow$ protein operator mapping; ABCD + Y$\to$S duality |
| [Op2 Crossing Correction](./op2-crossing-correction.md) | Topological crossing penalty derivation, knot type predictions, Gauss linking integral |
| [Op2 vs Op9](./op2-vs-op9.md) | Geometric (Op9) vs topological (Op2) exclusion comparison |
| [Terminology Translation](./terminology-translation.md) | Biology $\leftrightarrow$ EE dictionary; current limitations |
| [Predicted Extensions](./predicted-extensions.md) | Disulfide bridges, frequency-dependent solvent, Axiom 4 coupling, sequence context |

---

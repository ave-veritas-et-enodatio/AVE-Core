[↑ Vol 5 Translation Tables](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [enjq28]
-->

---

## Table: Protein Solver Domain Translation (tab:trans_protein_solver)

Protein solver domain translation. Every row maps one biological concept through EE to the axiomatic source and its codebase implementation.

| **Biology** | **EE / RF** | **AVE Axiom** | **Script Reference** |
|---|---|---|---|
| Peptide bond | TL segment | Axiom 1: $Z = \sqrt{\mu/\varepsilon}$ | `backbone_segments` |
| Amino acid sidechain | Impedance stub ($Z_\text{topo}$) | Axiom 1: $\sqrt{M/n_e}$ | `protein_bond_constants` |
| H-bond | Mutual inductance ($\kappa$) | Axiom 1: transformer coupling | `dc_analysis()` |
| $\beta$-sheet | Backward-wave coupler | Axiom 1: antiparallel TL | `dc_analysis()` |
| Hydrophobic core | Conjugate impedance match | Axiom 1: $\operatorname{Re}(Z_iZ_j^*)$ | `dc_analysis()` |
| Salt bridge | Reactive LC resonance | Axiom 1: $+jX \times -jX$ | `dc_analysis()` |
| Disulfide bond | Near-infinite admittance | Axiom 4: $Z \to \infty$ wall | `dc_analysis()` |
| Solvent exposure | Shunt to ground via $Z_\text{water}$ | Axiom 2: Debye relaxation | `dc_analysis()` |
| Steric clash | Pauli exclusion ($r < r_\text{steric}$) | Axiom 4: saturation wall | `dc_analysis()` |
| Protein compaction | Standing wave pattern | Axiom 4: $\eta_\text{eq} = P_C(1-\nu)$ | `ac_analysis()` |

*Solver Methods:*

| **Biology** | **EE / RF** | **AVE Axiom** | **Script Reference** |
|---|---|---|---|
| Native fold | Eigenstate ($\lambda_{\min}(S^\dagger S) = 0$) | 5-step eigenvalue method | `_eigenvalue_target()` |
| Folding kinetics | SPICE transient ring-down | Axiom 1: $L/C/R$ network | `explicit_spice_step()` |
| Cotranslational folding | Segmented cascade | Axiom 1: $Q$-coherence length | `fold_cascade_v7()` |
| Allostery | Tuning stub injection | Axiom 3: $\Gamma$ perturbation | `s15_allosteric_yield.py` |

---

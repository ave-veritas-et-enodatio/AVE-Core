[↑ Vol 5 Translation Tables](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-enjq28]
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

> **Reconciliation note (collapse-batch T19, drift-grade).** The "Conjugate impedance match" label above (`:20`, Hydrophobic core) and "Reactive LC resonance" (`:21`, Salt bridge) attach to *different* residue pairs than `vol5/common/translation-protein.md:28` (which labels the **salt bridge** the conjugate-impedance match). The solver ground truth `common/solver-toolchain.md:477` uses **one** term — Conjugate Matching, $Y_{shunt}\propto \operatorname{Re}(Z_iZ_j^*)/d_{ij}^2$ — for **BOTH** salt bridges AND hydrophobic pairs. **FLAG, not asserted (kill-test caveat):** whether the salt bridge is genuinely a *distinct* $+jX/-jX$ LC-resonance term or the same conjugate-matching term depends on the production `dc_analysis()` internals, which are **NOT visible from this checkout** (the solver lives out-of-repo). The solver-toolchain lump-row is itself physically odd — two hydrophobics should have *similar*, not opposite, reactances — so that grouping may be loose. Resolve against the live `dc_analysis()` before hardening either label.

*Solver Methods:*

| **Biology** | **EE / RF** | **AVE Axiom** | **Script Reference** |
|---|---|---|---|
| Native fold | Eigenstate ($\lambda_{\min}(S^\dagger S) = 0$) | 5-step eigenvalue method | `_eigenvalue_target()` |
| Folding kinetics | SPICE transient ring-down | Axiom 1: $L/C/R$ network | `explicit_spice_step()` |
| Cotranslational folding | Segmented cascade | Axiom 1: $Q$-coherence length | `fold_cascade_v7()` |
| Allostery | Tuning stub injection | Axiom 3: $\Gamma$ perturbation | `s15_allosteric_yield.py` |

---

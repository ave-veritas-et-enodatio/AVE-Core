[↑ Translation Tables](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [fy05jc]
-->

# Biology / Biophysics ↔ AVE Translation

<!-- label: tab:trans_biology -->

Biological structures are LC resonant circuits; folding is impedance minimisation. All mappings trace to the electromechanical transduction constant $\xi_{topo} = e/\ell_{node}$.

> → Primary: [Protein Folding Terminology Translation](../../vol5/common/translation-protein.md) — detailed 18-row mapping
> → Primary: [Protein Solver Domain Translation](../../vol5/common/translation-protein-solver.md) — 14-row solver mapping with code references

| **Biology / Biophysics** | **AVE Equivalent** | **Relationship** |
|---|---|---|
| Amino acid | SPICE subcircuit ($L$-$C$ stub) | Mass → inductance, stiffness → capacitance via $\xi_{topo}$ |
| Peptide backbone | Cascaded transmission line | $L$-$C$ ladder from C-N-C$_\alpha$ bond stiffness |
| Sidechain R-group | Shunt stub impedance $Z_R(\omega)$ | Stub length/impedance sets helix vs sheet propensity |
| Hydrogen bond | Series mutual inductance ($\kappa$) | $d_{HB} = 1.754$ Å, $E_{HB} = 4.98$ kcal/mol (zero parameters) |
| Protein fold | Impedance-matched load ($\Gamma \to 0$) | Global minimum of $U_{total}$; no Levinthal paradox |
| Ramachandran map | Smith chart | Allowed reflection coefficient trajectories on backbone |
| Steric clash | Short-circuit ($\Gamma = -1$) | Pauli exclusion: $d < r_A + r_B$ |
| $\alpha$-helix | Helical slow-wave structure | Right-handed coiled delay line (Axiom 1) |
| $\beta$-sheet | Coupled antiparallel stripline | Backward-wave coupler; $d_\beta = 4.7$ Å |
| Hydrophobic effect | Impedance mismatch with water | $h_i \cdot h_j$ coupling; water $\varepsilon_r \approx 80$ |
| Membrane bilayer | Dual-dielectric waveguide | Phase transition at $T_c \approx 278.3$ K |
| L-amino acid chirality | Non-reciprocal waveguide | $\beta_{eff} = \beta_0 - \delta_\chi \tanh(\chi/\chi_0)$ |
| Cancer (uncontrolled growth) | Impedance decoupling (loss of $Z$-match) | Oncogenic mutation → stub impedance shift |
| Red-light therapy (PBM) | RF injection at resonant stub | $\lambda = 630$–$670$ nm matches cytochrome $c$ oxidase stub |
| Anesthesia | Broadband damping ($R \to \infty$) | Membrane lipid impedance modification |
| Water ($T_m = 273$ K) | O-H···O bridge eigenmode | $T_m = 279.5$ K from LC lattice (zero parameters) |
| HOH bond angle | Tetrahedral acoustic mode | $\theta = \arccos(-1/4) = 104.48°$ (zero parameters) |

---

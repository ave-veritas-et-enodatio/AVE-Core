[↑ Simulation Architecture](./index.md)
<!-- leaf: verbatim -->

# Tier 1: Axiom-Derived Constants

Every physical constant in the engine traces to the four AVE axioms through the physics engine module `ave.solvers.protein_bond_constants`.

| **Symbol** | **Value** | **Derivation** | **Source** |
|---|---|---|---|
| $d_0$ | 3.8 Å | $C_\alpha$--$C_\alpha$ peptide geometry | Axioms 1--2 $\to$ covalent radii |
| $r_{C_\alpha}$ | 1.298 Å | Topological node radius (Carbon AC boundary) | Axioms 1--2 $\to$ periodic table |
| $Q$ | $0.75\pi^2 \approx 7.402$ | $\xi_\text{bend}/(1 - \cos\theta_{sp^3}) \div 2$ | Axiom 1 $\to$ bend loss $\to$ amide-V |
| $Z_0$ | 1.0 | Normalised backbone impedance | Definition |
| $\kappa_\text{HB}$ | $1/(2Q) \approx 0.0675$ | Half-bandwidth coupling | Resonator $Q$ factor |
| $R_\text{burial}$ | $d_0\sqrt{2} = 5.37$ Å | FCC coordination shell | Axiom-derived geometry |
| $D_{\mathrm{H_2O}}$ | 3.062 Å | $2 \times R_{\text{O},sp^3}$ (topological oxygen radius) | Axiom 2 $\to$ O $p$-shell AC boundary |
| $\beta_\text{burial}$ | $4.4/D_{\mathrm{H_2O}} \approx 1.437$ Å$^{-1}$ | Sigmoid scale from water diameter | Derived |
| $r_\text{steric}$ | $2 \times r_{C_\alpha} \approx 2.596$ Å | Pauli exclusion diameter | Axiom-derived node radii |
| $\delta_\chi$ | 0.05 rad | Ramachandran asymmetry / $Q$ | $\frac{1}{Q} \times 0.35$ |
| $\chi_0$ | 5.0 Å$^3$ | $d_0^3 / 11$ (helix geometry) | Derived from $d_0$ |
| | *Extended physics (v4 upgrades):* | | |
| $d_\text{SS}$ | 2.05 Å | Sulfur covalent radius $\times 2$ | Axioms 1--2 $\to$ S radii |
| $\eta_\text{NN}$ | 0.071 | $1/(2Q)$ (nearest-neighbour coupling) | Axiom 1 $\to$ amide-V |
| $d_\pi$ | 3.4 Å | $2 \times r_\text{Slater}(\text{C})$ ($\pi$-stack) | Axiom 2 $\to$ Slater radii |
| $\alpha_\pi$ | 0.53 | $A_\text{ring} / A_\text{backbone}$ | Ring geometry |
| $\tau_\text{w}$ | 8.3 ps | Debye relaxation of water | Axiom 2 $\to$ O--H bond |
| $\varepsilon_\infty$ | 1.77 | Optical permittivity ($n^2 = 1.33^2$) | Axiom 1 $\to$ bond polarisability |

*Engine constants and their derivation chain. No empirical structural data enters.*

---

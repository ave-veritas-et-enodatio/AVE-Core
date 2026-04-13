[↑ Simulation Architecture](./index.md)
<!-- leaf: verbatim -->

# Limitations of the 1D Cascade

## The Y-Shunt Balance Theorem

The ABCD cascade produces secondary structure via standing-wave resonances in the backbone transmission line. These resonances require a junction quality factor $Q_\text{jn} > 1$. The shunt admittance $Y$ at each C$_\alpha$ junction damps these resonances:

$$Q_\text{jn} \propto \frac{1}{Y_\text{shunt,total}}$$

The current $Y_\text{shunt}$ comprises four physically-derived contributions:

1. **Backbone coupling**: $\kappa \cdot Z^*$-match $\cdot C_\text{sat} / d^2$ (Axiom 4 saturated)
2. **H-bond mutual inductance**: $\kappa_\text{HB} \cdot \cos\theta \cdot e^{-d/d_0}$ (Layer 3b)
3. **Peptide-plane coupling**: $\kappa_\text{HB} \cdot \cos(\hat{n}_i \cdot \hat{n}_{i+1})$ (Layer 3c)
4. **Solvent**: exposure$/Z_\text{water}(\omega)$ (Debye relaxation)

Five additional coupling mechanisms were tested --- all *improved* RMSD but *degraded* secondary structure:

| Modification | SS | RMSD | Failure mode |
|---|---|---|---|
| Torsion penalty ($-\log S$) | 12% | 7.04 | Additive penalty fights S$_{11}$ |
| $\sqrt{1-x^2}$ chirality | 12% | 6.58 | Energy sat. $\neq$ phase sat. |
| Bilateral H-bond (donor+acceptor) | --- | --- | Loss diverged ($0.82 \to 4.3$) |
| C$_\beta$--C$_\beta$ stub coupling | 9% | 7.03 | Over-damps Y$_\text{shunt}$ |
| 3-frequency S$_{11}$ | 9% | --- | Sub-resonance sampling lost |

The consistent pattern reveals a *theorem*: the 1D cascade Y$_\text{shunt}$ balance is set by the axiom-derived constants---any additional admittance at the C$_\alpha$ junctions over-damps the resonant modes from which secondary structure emerges.

## Architectural Ceiling

The 1D cascade model has three fundamental limitations:

1. **Single propagation path**: The ABCD cascade models the backbone as a single cascaded TL. In reality, a folded protein has multiple propagation paths between distant residues (through H-bonds, sidechain contacts, and disulfide bonds). These create a *network*, not a cascade.

2. **2N degrees of freedom**: Only $(\varphi, \psi)$ are optimised. Sidechain rotamers ($\chi_1, \chi_2, \ldots$) are geometrically determined but do not enter the S$_{11}$ loss --- they affect only steric exclusion. In a 2D/3D network, sidechain contacts would create additional TL segments with their own S-parameters.

3. **Scalar junction admittance**: Y$_\text{shunt}$ at each C$_\alpha$ is a scalar. In a full network, each junction would be characterised by an $n$-port S-parameter matrix, allowing mode-selective coupling.

The path forward is a 2D/3D TL network where H-bonds and sidechain contacts are modelled as *additional TL segments* (with their own $Z$, $\gamma$, ABCD), not as shunt admittances on a single cascade. This is the subject of the next chapter.

---

[↑ Protein Folding](../index.md)
<!-- leaf: verbatim -->
<!-- sec:protein_bridge — DUPLICATE LABEL: also used in Ch.1 (vol5/molecular-foundations/biophysics-intro/protein-backbone-proton-radius.md) -->

# Predicted Extensions

The eight-force gradient descent framework suggests several concrete next steps:

- **Disulfide Bridge Formation.** Cysteine ($Z_{topo} \approx 1.74$) pairs separated by a loop should form a spontaneous topological short-circuit when both sites impedance-match---creating a non-local constraint that could drive tertiary folding.
- **Frequency-Dependent Solvent.** The current solvent boundary uses a static $Z_{\text{H}_2\text{O}} = \sqrt{\varepsilon_r}$; extending to a frequency-dependent $Z_{\text{solvent}}(\omega) = R(\omega) + j\omega L(\omega)$, where water's O--H stretching modes ($\sim$3400 cm$^{-1}$) define the loss tangent, would capture dielectric dispersion.
- **Axiom 4 Non-Linear Coupling.** Dielectric saturation ($C_{eff} = C_0/\sqrt{1-(\Delta\phi/\alpha)^2}$) creates stronger packing at close range. This could resolve the Villin tertiary gap by enhancing inter-helix coupling within $2d_0$ contact distance.
- **Sequence-Context $Z_{topo}$.** A nearest-neighbour modulation $Z_i \cdot g(Z_{i\pm1})$ could capture helix-capping, $\beta$-sheet nucleation, and turn propensities that emerge from cooperative sequence effects.

## Engine Validation Summary

| **Benchmark** | **Metric** | **Result** | **Free Params** |
|---|---|---|---|
| 20-sequence stress test | Secondary structure | 19/20 (95%) | 0 |
| Chou--Fasman correlation | Pearson $r$ | $+0.61$ | 0 |
| Chignolin RMSD (5AWL) | Kabsch RMSD | 2.82 Å | 0 |
| $R_g$ accuracy (Chignolin) | $R_g^{AVE}/R_g^{PDB}$ | 96% | 0 |
| JAX autodiff speedup | Wall-clock | $33\times$ | --- |

---

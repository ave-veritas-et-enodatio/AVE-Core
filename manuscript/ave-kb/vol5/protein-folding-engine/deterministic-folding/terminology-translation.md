[↑ Protein Folding](../index.md)
<!-- leaf: verbatim -->

# Translation of Terminology: Biology $\leftrightarrow$ Electrical Engineering

A central claim of the AVE framework is that biological structure is governed by the same impedance mathematics as electrical networks. The table below provides a formal dictionary mapping between the vocabularies of structural biology and transmission line engineering.

> → Primary: [Protein Folding Translation Table](../../common/translation-protein.md) — canonical Biology $\leftrightarrow$ EE $\leftrightarrow$ AVE mapping (tab:trans_protein)

## Current Limitations

1. **Boundary-Zone Residues.** Five amino acids (W, H, R, Y, G) produce ambiguous secondary structure predictions. These require corrections for $\pi$-stacking (W, H, Y), multi-conformer sampling (R), and conformational entropy (G).
2. **RMSD $\sim 6$ Å.** The model correctly predicts secondary structure type and produces physically realistic $R_g$ values (Chignolin $R_g$ within 4% of PDB), but per-residue coordinate accuracy (mean RMSD $\approx 6.2$ Å) lags behind empirical methods. The remaining error is dominated by tertiary topology: Villin's 3-helix bundle ($10.1$ Å) requires Axiom 4 non-linear coupling to resolve.
3. **Solvent Model Is Implicit.** The sigmoid burial function provides a differentiable approximation to solvent-accessible surface area, but explicit solvent-mediated hydrogen bonding and dielectric screening at the protein--water interface would improve accuracy for charged and polar surfaces.
4. **$O(N^2)$ Scaling.** The pairwise coupling scans scale quadratically. Spatial hashing or cell lists would be needed for proteins $> 200$ residues.
5. **Cooperative Effects.** Per-residue $Z_{topo}$ does not account for sequence context. A nearest-neighbour correction $Z_i \to Z_i \cdot g(Z_{i-1}, Z_{i+1})$ could capture cooperativity.

---

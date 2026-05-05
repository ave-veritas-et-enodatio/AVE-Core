[↑ Organic Circuitry](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [4jy0t8]
-->

---

## Simulation Results: Zero-Parameter Prediction

Using Equations eq:L_atom and eq:C_bond, the full transfer function $H(f) = V_\text{out}/V_\text{in}$ of the amino acid ladder network is solved for a representative six-molecule subset. The driving frequency sweeps from 100 GHz to 300 THz.

**Figure: fig:amino_resonance** — Transfer function $|H(f)|^2$ of six amino acids, computed from the zero-parameter AVE derivation ($L = m/\xi^2$, $C = \xi^2/k$). The backbone passband peaks in the 750--880 cm$^{-1}$ region (amide V / skeletal C--C--N bending), consistent with experimental IR spectroscopy. R-group differentiation is clearly visible: heavier or branched side chains (Valine, Phenylalanine) shift and reshape the passband relative to minimal stubs (Glycine). Vertical markers indicate known IR absorption bands.

The backbone passband peaks land at:

- Glycine: 789 cm$^{-1}$ (23.6 THz)
- Alanine: 781 cm$^{-1}$ (23.4 THz)
- Valine: 751 cm$^{-1}$ (22.5 THz)
- Serine: 782 cm$^{-1}$ (23.5 THz)
- Cysteine: 878 cm$^{-1}$ (26.3 THz)
- Phenylalanine: 854 cm$^{-1}$ (25.6 THz)

These frequencies correspond to the **amide V band** and **skeletal C--C--N bending modes** observed in real amino acid IR spectra ($\sim$700--900 cm$^{-1}$). The model predicts the correct frequency region *without any tunable parameters* — the absolute scale is locked by $\xi_\text{topo}$, and the relative differentiation between amino acids arises purely from the topological mass and stiffness of each R-group.

---

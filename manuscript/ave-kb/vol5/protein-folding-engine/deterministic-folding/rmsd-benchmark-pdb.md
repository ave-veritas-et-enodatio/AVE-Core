[↑ Protein Folding](../index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol5 as sec:rmsd_benchmark -->

# RMSD Benchmarking Against PDB

To test the eight-force engine against experimental 3D structures, backbone $C_\alpha$ coordinates were downloaded from the RCSB Protein Data Bank for four well-characterised peptides. The AVE prediction chain is entirely first-principles:

$$\text{Axioms 1--2} \;\to\; d_{\text{eq}},\, r_{\text{Slater}} \;\to\; Z_{topo} \;\to\; \text{8-force engine} \;\to\; \text{predicted 3D coords}$$

PDB data enters **only** as the comparison target---never as input to the prediction.

| **Peptide** | **PDB** | $N$ | **RMSD (Å)** | $R_g^{\text{AVE}}$ | $R_g^{\text{PDB}}$ | $\langle\angle\rangle^{\text{AVE}}$ | $\langle\angle\rangle^{\text{PDB}}$ |
|---|---|---|---|---|---|---|---|
| Chignolin ($\beta$-hairpin) | 5AWL | 10 | 4.34 | 4.3 | 4.8 | $71°$ | $72°$ |
| Trpzip2 ($\beta$-hairpin) | 1LE1 | 12 | 5.58 | 4.6 | 5.8 | $86°$ | $62°$ |
| Trp-cage TC5b | 1L2Y | 20 | 6.56 | 5.2 | 7.0 | $90°$ | $80°$ |
| Villin HP35 (3-helix) | 1YRF | 35 | 7.31 | 6.5 | 8.9 | $102°$ | $82°$ |
| | | | **Mean: 5.95** | | | | |

*Kabsch RMSD between AVE first-principles predictions and PDB experimental structures. $R_g$ = radius of gyration; $\langle\angle\rangle$ = mean $C_\alpha$--$C_\alpha$--$C_\alpha$ angle. PDB coordinates are from NMR model 1 or X-ray asymmetric unit.*

---

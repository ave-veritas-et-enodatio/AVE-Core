[↑ Protein Folding](../index.md)
<!-- leaf: verbatim -->

# AVE Topological Impedance

Historically, biologists rely on statistical methods, like Chou-Fasman propensities, to estimate whether a sequence will form an Alpha-Helix or a Beta-Sheet. In Variable Spacetime Mechanics, these arbitrary sequence "propensities" are recognised as a physical property: **Topological Impedance**.

Each amino acid sidechain maps to a complex topological impedance coefficient $Z_{topo} = R + jX$, where $R$ encodes the sidechain's hydrophobic coupling strength and $X$ encodes its charge reactance. The *secondary structure* of a sequence does not follow from a simple per-residue threshold; it emerges from the multi-frequency $S_{11}$ response of the full ABCD transmission line cascade. Small, symmetric sidechains (Ala, Gly) present minimal shunt loading on the backbone waveguide, allowing smooth helical winding. Branched, bulky, or rigid sidechains (Pro, Trp, His) create impedance discontinuities that flatten the backbone into extended Beta-Sheet or rigid kink conformations.

## Quantitative $Z_{topo}$ from SPICE Backbone Impedance

The topological impedance coefficient is not an arbitrary propensity score. It is a direct physical ratio derived from the Chapter 2 SPICE transfer function analysis. For a given amino acid with R-group shunt impedance $Z_R(\omega)$ at the backbone passband frequency $\omega_0 \approx 2\pi \times 23$ THz (the backbone amide V resonance from Table batch_resonance):

> **[Resultbox]** *Topological Impedance*
>
> $$Z_{topo} \;\equiv\; \frac{|Z_{\text{backbone}}(\omega_0)|}{|Z_R(\omega_0)|}$$

where $Z_{\text{backbone}}$ is the characteristic impedance of the N--C$_\alpha$--C repeating unit. When $|Z_R| \gg |Z_{\text{backbone}}|$, the sidechain is effectively invisible to the backbone wave and the chain curls freely (helix). When $|Z_R| \lesssim |Z_{\text{backbone}}|$, the sidechain mass loads the junction node, creating destructive interference and steric clashes that force the chain to flatten (sheet).

The *ab initio* derived complex $Z_{topo}$ values are listed below. The resistive component $R$ is computed from the ratio of R-group to backbone characteristic impedance:

$$R_i = \frac{Z_{\text{R-group},i}}{Z_{\text{backbone}}} = \frac{\sqrt{L_{R,i} / C_{R,i}}}{\sqrt{L_{\text{bb}} / C_{\text{bb}}}}, \qquad L = \frac{m}{\xi^2},\quad C = \frac{\xi^2}{k}$$

where $L_{R,i} = \sum_{\text{atoms}} m_a / \xi^2$ and $C_{R,i} = \sum_{\text{bonds}} \xi^2 / k_b$ for each sidechain. The backbone impedance $Z_{\text{bb}} = \sqrt{L_{\text{bb}}/C_{\text{bb}}} \approx 17.0~\Omega$ uses the peptide unit C$_\alpha$--C'(=O)--N(--H)--C$_\alpha$ (three atoms, three bonds). **No empirical fits or structural data enter.**

| **Amino Acid** | $R$ | $X$ | $|Z|$ | **Type** | **Preferred Structure** |
|---|---|---|---|---|---|
| Glycine (G) | 0.304 | 0.000 | 0.30 | Hydrophobic | Coil (minimal stub) |
| Alanine (A) | 0.568 | 0.000 | 0.57 | Hydrophobic | Alpha-Helix |
| Valine (V) | 0.605 | 0.000 | 0.61 | Hydrophobic | Alpha-Helix |
| Isoleucine (I) | 0.610 | 0.000 | 0.61 | Hydrophobic | Alpha-Helix |
| Leucine (L) | 0.610 | 0.000 | 0.61 | Hydrophobic | Alpha-Helix |
| Proline (P) | 0.632 | 0.000 | 0.63 | Hydrophobic | Turn / Rigid Kink |
| Lysine (K) | 0.639 | $+0.091$ | 0.65 | Pos. charge | Alpha-Helix |
| Methionine (M) | 0.723 | 0.000 | 0.72 | Hydrophobic | Alpha-Helix |
| Threonine (T) | 0.713 | $+0.051$ | 0.71 | Polar | Moderate |
| Arginine (R) | 0.740 | $+0.106$ | 0.75 | Pos. charge | Alpha-Helix |
| Serine (S) | 0.764 | $+0.055$ | 0.77 | Polar | Moderate |
| Glutamine (Q) | 0.782 | $+0.056$ | 0.78 | Polar | Alpha-Helix |
| Phenylalanine (F) | 0.786 | 0.000 | 0.79 | Hydrophobic | Moderate |
| Cysteine (C) | 0.824 | $-0.059$ | 0.83 | Polar | Moderate |
| Tyrosine (Y) | 0.833 | $-0.060$ | 0.84 | Polar | Moderate |
| Asparagine (N) | 0.840 | $+0.060$ | 0.84 | Polar | Moderate |
| Glutamate (E) | 0.849 | $-0.121$ | 0.86 | Neg. charge | Alpha-Helix |
| Histidine (H) | 0.862 | $+0.062$ | 0.86 | Polar (half) | Moderate |
| Tryptophan (W) | 0.895 | 0.000 | 0.89 | Hydrophobic | Beta-Sheet |
| Aspartate (D) | 0.949 | $-0.136$ | 0.96 | Neg. charge | Moderate |

*Complex topological impedance $Z_{topo} = R + jX$ for all 20 standard amino acids, computed ab initio via the impedance ratio equation. $R$ encodes the sidechain's characteristic impedance normalised to the backbone; $X$ encodes charge reactance scaled by $1/Q$ ($Q \approx 7$). All values in the range $[0.30, 0.96]$, as expected from the bounded impedance ratio. Secondary structure emerges from the full ABCD cascade $S_{11}$ response.*

The critical observation is that $Z_{topo}$ is not a fitted parameter---it is a deterministic output of the RLC transmission line model established in Chapter 2. Different amino acids produce different $Z_{topo}$ values because their R-group stub networks present different shunt impedances at the backbone resonant frequency. The mapping from molecular topology to folding geometry is therefore a direct consequence of the vacuum lattice axioms.

---

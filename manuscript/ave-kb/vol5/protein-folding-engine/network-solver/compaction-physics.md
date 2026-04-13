[↑ Network Solver](./index.md)
<!-- leaf: verbatim -->

# Compaction Physics

The through-space C$\alpha$--C$\alpha$ TL segments provide the compaction driving force. Their impedance encodes three physical layers:

## Conjugate Impedance Matching

For residues $i, j$ with complex impedances $Z_i, Z_j$:

$$m_{ij} = \max\!\left(0,\; \frac{\operatorname{Re}(Z_i Z_j^*)}{|Z_i||Z_j|}\right) \in [0, 1]$$

Hydrophobic pairs ($m_{ij} \to 1$) create low-impedance through-space paths that attract. Like-charged pairs ($m_{ij} = 0$) create no path---repulsion emerges from the $S_{11}$ gradient at close range.

## Axiom 4 Dielectric Saturation

Close-contact amplification:

$$C_\text{sat} = 1 + \frac{m_{ij}}{\sqrt{1 - (d_0/d_{ij})^2}}$$

Well-matched close pairs get amplified coupling; mismatched close pairs do not.

## Long-Range Saturation Envelope

Same Axiom 4 operator as galactic rotation:

$$S_\text{env}(d) = \sqrt{1 - (d/R_\text{burial})^2}, \qquad R_\text{burial} = d_0\sqrt{2} \approx 5.37\;\text{\AA}$$

Beyond $R_\text{burial}$, coupling decays to zero---preventing the "dark matter halo" of over-compaction.

---

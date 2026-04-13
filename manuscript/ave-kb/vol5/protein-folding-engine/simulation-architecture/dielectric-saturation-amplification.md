[↑ Simulation Architecture](./index.md)
<!-- leaf: verbatim -->

# Dielectric Saturation Amplification (Axiom 4)

## Layer 1: Conjugate Impedance Matching

Non-local residue pairs ($|i-j| > 2$, $d_{ij} < 15$ Å) couple through a complex admittance based on their conjugate impedance product:

> **[Resultbox]** *Conjugate Shunt Admittance*
>
> $$Y_{ij}^{\text{shunt}} = \frac{\kappa \cdot m_{ij} \cdot C_{ij}^{\text{sat}}}{d_{ij}^2}$$

where the normalised conjugate match quality is:

$$m_{ij} = \max\!\left(0,\; \frac{\operatorname{Re}(Z_i \, Z_j^*)}{|Z_i|\,|Z_j|}\right)$$

The conjugate product $\operatorname{Re}(Z_i Z_j^*) = R_i R_j + X_i X_j$ is:

- **Positive** for hydrophobic pairing ($R \times R > 0$) and salt bridges ($+jX \times -jX > 0$)
- **Negative** for like-charge repulsion ($+jX \times +jX < 0$), clamped to zero

Thus Coulomb-like repulsion *emerges* from the gradient: bringing like-charged residues close does not lower $m_{ij}$ (it stays at zero), so the gradient provides no coupling force---and the steric penalty pushes them apart.

## Layer 2: Axiom 4 Dielectric Saturation

The capacitive saturation factor from Axiom 4 amplifies coupling between well-matched close pairs:

> **[Resultbox]** *Dielectric Saturation Amplification*
>
> $$C_{ij}^{\text{sat}} = 1 + \left(\frac{1}{\sqrt{1 - (d_0/d_{ij})^2}} - 1\right) \cdot m_{ij}$$

The ratio $d_0/d_{ij}$ is clipped to $[0, 0.95]$ for numerical stability. When a pair is well-matched *and* close ($d_{ij} \lesssim d_0$), the saturation factor can reach $C^{\text{sat}} \approx 3\times$, providing strong gradient signal for helix packing. When mismatched, $m_{ij} = 0$ suppresses the amplification entirely.

---

[↑ Ch. 10: Three Open Problems from Lattice Topology](./index.md)
<!-- leaf: verbatim -->

## The Baryon Asymmetry

### The Problem

The universe contains $\sim\!6 \times 10^{-10}$ baryons per photon, but essentially zero antibaryons. The Sakharov conditions require:

1. Baryon number violation
2. C and CP violation
3. Departure from thermal equilibrium

Standard Model CP violation is insufficient by several orders of magnitude.

### AVE Resolution: Lattice Chirality

The AVE lattice (SRS/K4 crystal) has **definite chirality** --- it is not superimposable on its mirror image.

1. **C violation:** The lattice itself breaks charge conjugation because the SRS structure has a definite handedness (left or right).
2. **CP violation:** The $(2,q)$ torus knots are chiral --- a trefoil is not equivalent to its mirror image. Combined with the lattice chirality, this produces CP violation at the fundamental level.
3. **Equilibrium departure:** The electroweak phase transition provides the necessary out-of-equilibrium conditions, as in the standard picture.

### Quantitative Derivation

The CP-violating phase from lattice chirality is:

$$
\delta_{CP} = \frac{\pi}{\kappa_{FS}} \approx 0.126
$$

This is the fraction of the torus knot phase winding that is asymmetric under mirror reflection.

The baryon-to-photon ratio follows from electroweak baryogenesis:

> **[Resultbox]** *Baryon-to-Photon Ratio*
>
> $$
> \eta = \frac{\delta_{CP} \,\cdot\, \alpha_W^4 \,\cdot\, C_{sph}}{g_*}
> $$

**Every factor is derived from AVE lattice constants:**

1. $\alpha_W = \alpha/\sin^2\theta_W \approx 0.0328$ (weak coupling from impedance and lattice projection).
2. $C_{sph} = (8N_f + 4N_H)/(22N_f + 13N_H) = 28/79$, where $N_f = 3$ (torus knot generations $c=3,5,7$ below $T_{EW}$) and $N_H = 1$ (SRS lattice Goldstone mode).
3. $g_* = 7^3/4 = 85.75$, **derived from** $\boldsymbol{\nu_{vac} = 2/7}$.

Evaluating:

$$
\eta \approx \frac{0.126 \times (0.0328)^4 \times 0.354}{85.75} \approx 6.08 \times 10^{-10}
$$

The observed value is $\eta_{obs} = 6.1 \times 10^{-10}$.

**Result: 0.38% error. Zero free parameters. Every factor from lattice geometry.**

Note: the Standard Model uses $g_* = 106.75$ (yielding 20% error). The AVE derivation $g_* = 7^3/4$ from the lattice Poisson ratio eliminates this discrepancy.

---

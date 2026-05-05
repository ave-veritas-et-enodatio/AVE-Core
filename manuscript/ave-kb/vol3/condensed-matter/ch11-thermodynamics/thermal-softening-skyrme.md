[↑ Ch.11: Thermodynamics and The Arrow of Time](../index.md)

<!-- kb-frontmatter
kind: leaf
claims: [uu6dl5]
-->

---

## Thermal Softening of Topological Structures

The preceding sections treated the lattice as a passive thermal reservoir. Consider now the back-reaction: how does ambient thermal noise modify the internal structure of a topological defect (particle)?

### The Thermal Correction to the Skyrme Coupling

The proton is a $6_2^3$ Borromean linkage confined by the $(2,5)$ cinquefoil torus knot. Its internal tension is governed by the Faddeev-Skyrme coupling constant $\kappa_{FS} = 8\pi$ (the cold, zero-temperature value). The proton's core exists at an effective temperature $T_{core} \sim m_p c^2 / k_B \approx 10^{13}\;\text{K}$.

At this temperature, the baseline RMS thermal noise of the vacuum partially averages out the sharp gradient tensor $(\partial_\mu \mathbf{n} \times \partial_\nu \mathbf{n})^2$ that stabilises the quartic Skyrme repulsion. The thermally corrected coupling is:

> **[Resultbox]** *Thermal Softening Correction*
>
> $$\kappa_{FS}^{(T)} = \kappa_{FS}^{(cold)} (1 - \delta_{th}) = 8\pi \left(1 - \frac{1}{14\pi^2}\right)$$

### Gradient Saturation and the Residual $\delta_{th}$

The thermal softening of the Skyrme coupling arises from two distinct physical effects, now handled separately:

**Effect 1: Lattice Gradient Saturation (Axiom 4).** The continuous Faddeev-Skyrme solver assumes arbitrarily steep phase gradients $\partial_r \phi$. But the discrete lattice has a maximum resolvable gradient: one half-rotation per cell,

$$\left|\frac{\partial\phi}{\partial r}\right|_{yield} = \frac{\pi}{\ell_{node}}\,.$$

At each radius, the solver now applies the Axiom 4 saturation kernel to the gradient:

> **[Resultbox]** *Axiom 4 Gradient Saturation Kernel*
>
> $$\left(\frac{\partial\phi}{\partial r}\right)_{\!eff} = \frac{\partial\phi}{\partial r}\;\sqrt{1 - \left(\frac{|\partial_r\phi|}{\pi/\ell_{node}}\right)^{\!2}}\,.$$

This is the **same** operator used in the FDTD field updates, plasma cutoff, and galactic rotation drag---applied inside the energy functional itself. It naturally reduces the energy at high crossing numbers where the soliton profile approaches the lattice resolution limit.

**Effect 2: RMS Noise Averaging (Residual $\delta_{th}$).** The soliton core sits at temperature $T_{core} \sim m_p c^2/k_B$. Thermal fluctuations partially average the gradient tensor $(\partial_\mu \mathbf{n} \times \partial_\nu \mathbf{n})^2$. With the peak gradient already saturated by Axiom 4, the residual averaging operates on the mean-to-peak ratio of the rectified sinusoidal noise, which is $2/\pi$:

> **[Resultbox]** *Residual Thermal RMS Correction*
>
> $$\delta_{th} = \frac{\nu_{vac}}{\kappa_{cold}} \times \frac{2}{\pi} = \frac{2/7}{8\pi} \times \frac{2}{\pi} = \frac{1}{14\pi^2} \approx 0.00721$$

### Physical Interpretation

$\delta_{th}$ is not a free parameter. It is built from three independently derived geometric constants:

- $\nu_{vac} = 2/7$ --- the lattice Poisson ratio (shear compliance),
- $\kappa_{cold} = 8\pi$ --- the Skyrme stiffness (Faddeev coupling),
- $2/\pi$ --- the mean-to-peak ratio of rectified sinusoidal noise.

The previous value $\delta_{th} = 1/(28\pi) \approx 0.01137$ implicitly combined Effects 1 and 2 into a single correction. The factorisation makes the physics transparent: the lattice resolution limit is an Axiom 4 structural identity, while the residual $\delta_{th}$ captures purely thermodynamic noise averaging.

Both $\nu_{vac}$ and $\kappa_{cold}$ are pure geometric constants derived independently from the lattice axioms. The thermal correction to the proton mass is therefore a **zero-parameter result**: it depends only on the topology of the vacuum, not on any empirical measurement of temperature or coupling strength.

---

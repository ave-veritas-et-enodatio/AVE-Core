[↑ Ch.7 Regime Map](index.md)
<!-- leaf: verbatim -->

## Section 7.3: Regime-Specific Equation Sets

For each regime, the constitutive parameters simplify. Two saturation symmetries arise (per LIVING_REFERENCE Axiom 4 derived consequences); each gets its own table.

### Symmetric saturation (gravity, BH interior, GW shear)

Both $\varepsilon$ and $\mu$ scale by $S = \sqrt{1-r^2}$. The EM impedance ratio cancels, so $Z = Z_0$ is invariant; the EM phase velocity diverges; the shear (GW / soliton group) velocity freezes.

| **Quantity** | **I (Linear)** | **II (Nonlinear)** | **III (Yield)** | **IV (Ruptured)** |
|---|---|---|---|---|
| $\varepsilon_{eff}$ | $\varepsilon_0$ | $\varepsilon_0 \sqrt{1-r^2}$ | $\to 0$ | 0 |
| $\mu_{eff}$ | $\mu_0$ | $\mu_0 \sqrt{1-r^2}$ | $\to 0$ | 0 |
| $Z_{sym}$ | $Z_0$ | $Z_0$ (invariant) | $Z_0$ | $Z_0$ |
| $c_{EM,sym}$ | $c_0$ | $c_0 / \sqrt{1-r^2}$ | $\to \infty$ | $\infty$ |
| $c_{shear}$ | $c_0$ | $c_0(1-r^2)^{1/4}$ | $\to 0$ | 0 |
| $C_{eff}$ | $C_0$ | $C_0 / \sqrt{1-r^2}$ | $\to \infty$ | $\infty$ |
| $Q$ | $\sim 1$ | $1/\sqrt{1-r^2}$ | $\gg 1$ | $\infty$ |

### Asymmetric (electric-only) saturation (strong EM fields, dielectric rupture)

Only $\varepsilon$ scales by $S$; $\mu$ is unchanged. The EM impedance diverges and the medium becomes opaque (evanescent). $c_{shear}$ freezes identically to the symmetric case.

| **Quantity** | **I (Linear)** | **II (Nonlinear)** | **III (Yield)** | **IV (Ruptured)** |
|---|---|---|---|---|
| $\varepsilon_{eff}$ | $\varepsilon_0$ | $\varepsilon_0 \sqrt{1-r^2}$ | $\to 0$ | 0 |
| $\mu_{eff}$ | $\mu_0$ | $\mu_0$ (unchanged) | $\mu_0$ | $\mu_0$ |
| $Z_{asym}$ | $Z_0$ | $Z_0 / (1-r^2)^{1/4}$ | $\to \infty$ | $\infty$ |
| $c_{EM,asym}$ | $c_0$ | $c_0/(1-r^2)^{1/4}$ | $\to \infty$ | $\infty$ |
| $c_{shear}$ | $c_0$ | $c_0(1-r^2)^{1/4}$ | $\to 0$ | 0 |
| $C_{eff}$ | $C_0$ | $C_0 / \sqrt{1-r^2}$ | $\to \infty$ | $\infty$ |
| $Q$ | $\sim 1$ | $1/\sqrt{1-r^2}$ | $\gg 1$ | $\infty$ |

**Particle confinement** proceeds via the magnetic branch (a third sub-case of the symmetric sector): at a torus-knot self-intersection, the magnetic field saturates $\mu$ first, driving $Z = \sqrt{\mu_{eff}/\varepsilon_0} \to 0$ and $\Gamma \to -1$ (short-circuit). The standing wave that results is rest mass.

---

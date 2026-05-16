[↑ Ch.8 Gravitational Waves](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-07kd5v]
path-stable: "referenced from vol3 as sec:gw_propagation"
-->

---

## GW Propagation as Impedance Modulation

Gravitational waves are transverse inductive shear waves in the LC lattice---the same medium governed by the same operators. In accordance with the **Symmetric Scaling** axiom required to preserve a uniform optical vacuum, gravity scales both the local permittivity and permeability symmetrically via the refractive metric $n(r) = (1 - r_s/r)^{-1}$:

$$
\begin{align}
\varepsilon_{eff}(r) &= \varepsilon_0 \cdot n(r) \\
\mu_{eff}(r) &= \mu_0 \cdot n(r)
\end{align}
$$

where $r_s = 2GM/c^2$. Because both components scale proportionally, the macroscopic gravitational impedance remains invariant everywhere:

> **[Resultbox]** *Invariant Gravitational Impedance*
>
> $$
> Z(r) = \sqrt{\frac{\mu_{eff}(r)}{\varepsilon_{eff}(r)}} = \sqrt{\frac{\mu_0 \cdot n}{\varepsilon_0 \cdot n}} \equiv Z_0
> $$

Therefore, the reflection coefficient $\Gamma$ across any gravitational gradient evaluates identically to zero ($\Gamma = 0$). While the local speed of light slows down near mass ($c_l = c/n$), the impedance matching remains perfect. Gravitational waves experience zero reflection and zero scattering as they traverse deep gravitational wells, propagating seamlessly.

### Lossless Propagation

LIGO gravitational waves have strain $h \sim 10^{-21}$. The equivalent voltage per lattice cell is $V_{GW} = h \cdot c \cdot \ell_{\text{node}} \cdot 2\pi f \sim 10^{-19}$ V, which is $\sim 10^{-24}$ times smaller than $V_{\text{snap}} \approx 511$ kV. Far below the saturation threshold, the lattice acts as a perfect lossless linear transmission line. Gravitational waves propagate to cosmological distances without dissipation---matching LIGO observations exactly, with zero free parameters.

---

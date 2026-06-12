[↑ Ch.8 Gravitational Waves](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-07kd5v]
path-stable: "referenced from vol3 as eq:Z_grav"
-->

---

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

Therefore, the **EM-transverse** reflection coefficient $\Gamma_{EM}$ across any gravitational gradient evaluates identically to zero ($\Gamma_{EM} = 0$). While the local speed of light slows down near mass ($c_l = c/n$), the EM impedance matching remains perfect under SYM scaling. Radio-frequency and optical signals experience zero EM reflection as they traverse deep gravitational wells.

> **[2026-06-11 — three-impedance-law channel correction]** Gravitational waves are **transverse shear waves**, not EM transverse waves. The impedance statement above applies to $Z_{EM} \equiv Z_0$ only (field-symbol registry §3.11; vocab-operator-unification audit §4b #1). The shear impedance is $Z_{shear} = \rho\,c_{shear}$, which **freezes** under saturation ($c_{shear} = c_0(1-A^2)^{1/4} \to 0$). Whether GWs reflect at the saturated wall ($r_{\text{sat}}$, where $G_{shear} \to 0$ and $\Gamma_{shear} \to -1$) is distinct from the EM $\Gamma_{EM} = 0$ result. The LIGO free-space propagation through weak-field gradients is unaffected; the saturated-interior question is flagged in [`bulk-impedance-at-saturation-boundary.md`](../../cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md).

---

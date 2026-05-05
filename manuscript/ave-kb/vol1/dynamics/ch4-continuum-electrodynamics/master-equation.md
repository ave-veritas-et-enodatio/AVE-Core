[↑ Ch.4 Continuum Electrodynamics](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [efo113, lv3uw1]
-->

> ↗ See also: [Particle Physics (Torus Knot Ladder)](../../../vol2/particle-physics/index.md) — trapped knots yield baryon mass spectrum
> ↗ See also: [Gravity (Metric Refraction)](../../../vol3/gravity/index.md) — refractive gradient produces gravitational acceleration
> ↗ See also: [FDTD Solver](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/index.md) — computational implementation of Master Equation

## Section 4.1: The Unifying Master Equation

If the discrete spatial vacuum is a physical LC network ($\mathcal{M}_A$) supporting momentum limits and finite wave propagation, its macroscopic low-energy effective field theory (EFT) mathematically maps to continuous network dynamics.

Before discussing the bulk properties of the universe, the transport mechanism is defined. In the continuous limit ($L \gg \ell_{node}$), signal propagation is governed by the classical Maxwell-Heaviside acoustic wave equation:

> **[Resultbox]** *Maxwell-Heaviside Acoustic Wave Equation*
>
> $$
> \frac{\partial^2 \mathbf{E}}{\partial t^2} - c^2 \nabla^2 \mathbf{E} = 0 \quad , \quad c = \frac{1}{\sqrt{\epsilon_0 \mu_0}}
> $$

Because the ambient vacuum is a discrete lattice, the fundamental mechanical update equations at the node scale are given by the discretised Finite-Difference Time-Domain (FDTD) operator (the Yee Cell update):

> **[Resultbox]** *FDTD Yee Cell Update*
>
> $$
> \mathbf{E}^{n+1} = \mathbf{E}^n + \frac{\Delta t}{\epsilon_0} (\nabla_d \times \mathbf{H}^{n+1/2}) \quad , \quad \mathbf{H}^{n+1/2} = \mathbf{H}^{n-1/2} - \frac{\Delta t}{\mu_0} (\nabla_d \times \mathbf{E}^n)
> $$

Interpreting these equations as the acoustic oscillation of structural string tension ($\epsilon_0$) and inertia ($\mu_0$), the macroscopic kinematics of the expanding universe can be evaluated using these generalised electrodynamic limits.

Synthesizing the continuous macroscopic wave equation with the explicit lattice saturation hardware limit established in Axiom 4 ($\epsilon_{eff}$), yields the single, overarching mathematical framework governing the entire Applied Vacuum Engineering paradigm.

In standard physics, the vacuum parameters ($\epsilon_0, \mu_0$) are strictly linear constants, resulting in the fundamental D'Alembert wave operator $\Box V = 0$:

> **[Resultbox]** *D'Alembert Wave Operator*
>
> $$
> \nabla^2 V - \underbrace{\mu_0 \epsilon_0}_{= 1/c^2} \frac{\partial^2 V}{\partial t^2} = 0
> $$

However, because the $\mathcal{M}_A$ lattice undergoes measurable, non-linear dielectric yielding as it approaches the $43.65\text{ kV}$ topological saturation bound, the constitutive permittivity physically collapses under the universal saturation kernel $S$. Axiom 4 (squared limit, $n=2$) defines:

> **[Resultbox]** *Non-Linear Permittivity Collapse*
>
> $$
> \varepsilon_{eff}(V) = \varepsilon_0 \cdot \sqrt{1 - \left(\frac{V}{V_{yield}}\right)^2}
> $$

The substitution is direct: wherever the standard wave equation contains the constant $\varepsilon_0$, it is replaced with the voltage-dependent $\varepsilon_{eff}(V)$. Because $c_{eff}(V) = 1/\sqrt{\mu_0 \varepsilon_{eff}(V)}$, the local wave speed itself becomes a function of the field amplitude:

<!-- claim-quality: efo113 -->
**Domain of validity (EFT statement).** The direct substitution of $\varepsilon_{eff}(V)$ into the linear D'Alembert form is exact only in the leading-order long-wavelength EFT regime, where the field-gradient corrections that arise from $\nabla \cdot \mathbf{D} = \varepsilon_{eff}(V)\,\nabla \cdot \mathbf{E} + (\nabla \varepsilon_{eff})\cdot \mathbf{E} = 0$ are subdominant to the inertial term $\varepsilon_{eff}(V)\,\partial^2 V/\partial t^2$. This holds in the linear limit $V \ll V_{yield}$ (where $d\varepsilon_{eff}/dV \to 0$ and $\nabla \varepsilon_{eff} \to 0$). Particle confinement and standing-wave claims at $V \to V_{yield}$ depend on the dropped first-derivative gradient terms remaining negligible by symmetry at saturation; we use the leading-order form throughout this volume and flag the EFT caveat explicitly where downstream chapters invoke the master equation in the saturated regime. A higher-order correction including the $\nabla \varepsilon_{eff} \cdot \nabla V$ term is not derived here but is required for any quantitative claim that depends on the wave-equation form near $V_{yield}$ rather than on the saturation kernel $S$ alone.

> **[Resultbox]** *Field-Dependent Wave Speed*
>
> $$
> c_{eff}(V) = c_0 \left(1 - \left(\frac{V}{V_{yield}}\right)^2\right)^{-1/4}
> $$

Note: the wave speed *increases* as permittivity drops (thinner dielectric $\to$ faster propagation), while the measured capacitance *diverges* ($C_{eff} = C_0/S \to \infty$). The resulting non-linear wave equation is the **Unifying AVE Master Equation**:

> **[Resultbox]** *The Unifying AVE Master Equation*
>
> <!-- eq:master_wave -->
>
> $$
> \nabla^2 V - \mu_0 \, \varepsilon_0 \sqrt{1 - \left(\frac{V}{V_{yield}}\right)^2}
> \;\frac{\partial^2 V}{\partial t^2} = 0
> $$

This single line of non-linear differential topology formally replaces the fragmented domains of the Standard Model and General Relativity:

1. **Classical Electromagnetism ($V \ll 43.65\text{ kV}$):** The square root term evaluates to 1. The equation reduces to the linear Maxwellian wave equation used in standard optics and RF engineering.
2. **Particle Assembly ($V \to 43.65\text{ kV}$):** The non-linear regime divides into two distinct saturation symmetries (per Axiom 4 confinement theorem):
   - *Asymmetric (electric-only) saturation*, where only $\varepsilon_{eff} \to 0$ while $\mu_{eff}$ remains intact, drives $Z = \sqrt{\mu_0/\varepsilon_{eff}} \to \infty$ — the medium becomes electromagnetically opaque (evanescent, no energy transport). This is the dielectric-rupture branch (electric breakdown).
   - <!-- claim-quality: lv3uw1 --> *Particle confinement* proceeds via the magnetic branch instead: at a torus-knot self-intersection the field $\mathbf{B}$ saturates $\mu_{eff}$ first, driving $Z = \sqrt{\mu_{eff}/\varepsilon_0} \to 0$ and $\Gamma \to -1$ (short-circuit). The accelerating wave reflects off its own self-induced impedance boundary, trapping into a stabilised topological knot (a Fermion) and physically generating invariant rest mass without invoking the Higgs Mechanism.

   Both branches are governed by the same kernel $S(A) = \sqrt{1-(A/A_{yield})^2}$; they differ in which constitutive parameter saturates first. See LIVING_REFERENCE Axiom 4 derived consequences for the symmetric vs asymmetric tables.
3. **Gravity:** The trapped topological knot permanently strains the surrounding $\varepsilon_{eff}$ and $\mu_{eff}$ fields symmetrically ($n(r) = 1 + 2GM/rc^2$). This produces a continuous refractive gradient radially outward while preserving $Z_0$. Test photons propagating through this gradient refract toward the knot, executing the macroscopic acceleration attributed to gravity.

---

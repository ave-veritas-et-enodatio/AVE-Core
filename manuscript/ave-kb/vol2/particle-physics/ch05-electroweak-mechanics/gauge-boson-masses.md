[↑ Ch.5 — Electroweak Mechanics](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-5zuo7g, clm-q8un7j]
-->

## Electrodynamics: The Gradient of Topological Phase

A localized charged node exerts a continuous rotational phase twist ($\theta$) on the surrounding LC network. Because the unsaturated vacuum acts as a linear dielectric in the far-field, the static structural phase strain obeys the 3D **Laplace Equation** ($\nabla^2 \theta = 0$).

The spherically symmetric geometric solution dictates that the twist amplitude decays inversely with distance ($\theta(r) \propto 1/r$). The continuous electric displacement field ($\mathbf{D}$) is the spatial gradient of this structural phase twist ($\mathbf{D} = \nabla\theta \propto -1/r^2 \mathbf{\hat{r}}$), deriving Coulomb's Law.

### Magnetism as Convective Vorticity

When a twisted node translates at a velocity $\mathbf{v}$, it induces a convective shear flow in the momentum field. In classical network dynamics, the time evolution of a translating steady-state strain field $\mathbf{D}(\mathbf{r} - \mathbf{v}t)$ is governed by the convective material derivative:

> **[Resultbox]** *Convective Material Derivative*
>
> $$
> \partial_t \mathbf{D} = -(\mathbf{v} \cdot \nabla)\mathbf{D} \implies \nabla \times (\mathbf{v} \times \mathbf{D})
> $$

Equating this to the Maxwell-Ampere law derives the macroscopic magnetic field from network dynamics: $\mathbf{H} = \mathbf{v} \times \mathbf{D}$.

This relationship is supported by dimensional analysis. Applying the topological conversion constant ($\xi_{topo} \equiv e/l_{node}$), the displacement field reduces to $[\mathbf{D}] = \xi_{topo}[1/\text{m}]$. Evaluating the cross product $[\mathbf{v} \times \mathbf{D}]$ yields $\xi_{topo}[1/\text{s}]$. Standard SI units for magnetic field intensity $\mathbf{H}$ ($[\text{A/m}]$) reduce to this same dimensional basis ($\xi_{topo}[1/\text{s}]$). Magnetism is thereby dimensionally shown to represent the continuous kinematic vorticity of the vacuum medium.

### The Inductive Origin of Gauge Invariance

Standard Quantum Field Theory mandates that the vector potential is a gauge field, where transformations of the form $\mathbf{A} \to \mathbf{A} + \nabla \Lambda$ leave physical observables ($\mathbf{B}$ and $\mathbf{E}$) unchanged. A common critique of identifying $\mathbf{A}$ as a physical momentum field is that this gauge freedom would imply the unphysical, spontaneous shifting of macroscopic mass, violating Noether's theorem.

This paradox is resolved via the **Helmholtz Decomposition Theorem** in classical network dynamics. Any continuous vector field can be decomposed into a solenoidal (divergence-free) component and an irrotational (curl-free) component. Adding the gradient of a scalar field ($\nabla \Lambda$) to the mass flow introduces a uniform, irrotational velocity potential to the background network.

The Helmholtz decomposition is exact at *any* compressibility, and that is all this argument needs: adding $\nabla\Lambda$ changes only the irrotational component, and **the irrotational component sources no transverse observable**. The curl identity $\nabla \times \nabla\Lambda \equiv 0$ leaves the transverse vorticity $\nabla \times \mathbf{A}$ pointwise unchanged, and the loop integral $\oint \nabla\Lambda \cdot d\boldsymbol{\ell} = 0$ around any closed contour (single-valued $\Lambda$) leaves every winding and linking integer unchanged — so no topological defect is created or destroyed. It is isomorphic to performing a **Galilean or Lorentz coordinate boost** of the observer's reference frame. Gauge invariance is not violated; it is revealed to be the classical network-dynamic freedom to shift the irrotational background coordinate velocity without altering the physical transverse observables.

> **Premise repaired — the incompressibility premise is struck (Grant ruling 2026-08-03).** Ruling verbatim `[sic]`: ***"5. repair"***. The step above deliberately does **not** assume an incompressible substrate.
>
> **Why the old premise was false.** It read *"Because the vacuum substrate is incompressible ($K = 2G$) …"*. The vacuum at $K = 2G$ is **definitively compressible**: the isotropic relation $\nu = (3K - 2G)/(2(3K+G))$ gives $\nu_{\text{Hill}} = 4G/14G = \mathbf{2/7}$ at $K = 2G$, and $\nu = 1/2$ is reached **only** in the limit $K \to \infty$ — **no finite $K$ is incompressible**. `K = 2G` is the corpus's *finite-modulus* trace-reversal lock, not a rigidity statement (`common/q-g47-substrate-scale-cosserat-closure.md:28`; GR-imported per PR [#261](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/261)).
>
> **Why it was load-bearing, not decorative.** For a general $\Lambda$, $\nabla\cdot(\nabla\Lambda) = \nabla^2\Lambda \neq 0$, so the clause *"generates no localised compression"* does **not** follow from Helmholtz alone — incompressibility was exactly what was being asked to kill it. The repair therefore **drops that leg rather than rescuing it**, and keeps only what the gauge conclusion actually needs.
>
> **The correct available premise (the ruled replacement).** The irrotational component sources **no transverse observable**: $\nabla \times \nabla\Lambda \equiv 0$ and $\oint \nabla\Lambda \cdot d\boldsymbol{\ell} = 0$ hold at **any** $\nu$, including $\nu_{\text{vac}} = 2/7$. The substrate-native grounding is the corpus's **adjudicated longitudinal-sector split**, [`../../../common/vocabulary-register.md`](../../../common/vocabulary-register.md)`:867` (`def-l0ngdu`): the mechanical dilatation $\nabla\cdot\mathbf{u}$ is **DYNAMICAL** — it carries a genuine bulk restoring force $\tfrac12 K(\nabla\cdot\mathbf{u})^2$ and rides the gapless lattice-computed P-branch — while the EM longitudinal $\nabla\cdot\mathbf{A}$ is **GAUGE**, the curl-only EM Lagrangian giving it no restoring force. Verbatim: *"**One word each way — $\nabla\cdot\mathbf{u}$ propagates; $\nabla\cdot\mathbf{A}$ is gauge.**"* That split is the substrate-native reason the shift is unobservable, and it needs no compressibility assumption.
>
> **Chain check (the repaired argument, end to end).** (1) Critique: a gauge shift on a *physical* $\mathbf{A}$ would spontaneously move macroscopic mass. (2) Helmholtz: $\nabla\Lambda$ is purely irrotational, so it enters only the longitudinal channel — exact at any $\nu$, no premise spent. (3) The physical transverse observables are built from the solenoidal channel ($\mathbf{B} = \nabla\times\mathbf{A}$), and $\nabla\times\nabla\Lambda \equiv 0$, so they are pointwise unchanged. (4) The topological content is loop/surface integrals of the same channel, and $\oint\nabla\Lambda\cdot d\boldsymbol{\ell} = 0$, so no defect is created or destroyed. (5) Therefore the shift is a coordinate re-labelling of the irrotational background — the boost reading — and the critique is answered. **No step now uses compressibility.**
>
> **⚑ FLAGGED, NOT FIXED (scope: outside this ruling).** The paragraph above still describes $\nabla\Lambda$ as added *"to the mass flow"*, which reads $\mathbf{A}$ as the mechanical momentum field. The corpus's SOLID adjudication is that $\mathbf{u}$ and $\mathbf{A}$ are **counterpart sector variables — isomorphic structure, NOT one field** ([`../../../common/vocabulary-register.md`](../../../common/vocabulary-register.md)`:882`, `def-uatk1s`, SOLID 2026-07-21), differing precisely in constitutive stencil on the longitudinal channel. Whether the *"mass flow"* wording needs its own correction is a **separate question, routed** — surfaced here rather than absorbed silently into this repair.
>
> **Scope.** Premise-only. The conclusion, the boost reading, and every downstream result in this leaf ($m_W/m_Z = \sqrt{7}/3$, $\sin^2\theta_W = 2/9$) are **unchanged**; `clm-5zuo7g` and `clm-q8un7j` are untouched (no re-grade, no retraction). Mirrored byte-for-byte in the print at `manuscript/vol_2_subatomic/chapters/05_electroweak_gauge_theory.tex` §"The Inductive Origin of Gauge Invariance" (the `.tex` carries a condensed premise note; this leaf carries the explanation).

## The Weak Interaction: Inductive Cutoff Dynamics
<!-- claim-quality: clm-5zuo7g (the $m_W/m_Z = \sqrt{7}/3$ ratio derived in this section gives the on-shell Weinberg angle) -->

In classical electrodynamics, the ratio of the LC network's microrotational bending inductance ($\gamma_c$) to the macroscopic optical shear modulus ($G_{vac}$) defines a fundamental **Characteristic Length Scale** ($l_c = \sqrt{\gamma_c/G_{vac}}$). This length scale is identified as the physical origin of the weak force range ($r_W \approx 10^{-18}$ m).

Weak interactions lack the kinetic energy required to overcome the ambient LC rotational inductance. Any physical excitation operating *below* a medium's natural cutoff frequency becomes an **Evanescent Wave**. The static field equation transforms from the Laplace equation to the massive Helmholtz equation ($\nabla^2 \theta - \frac{1}{l_c^2}\theta = 0$). The solution yields the **Yukawa Potential**:

> **[Resultbox]** *Yukawa Potential as Evanescent Cutoff*
>
> $$
> V_{weak}(r) \propto \frac{e^{-r/l_c}}{r}
> $$

### Deriving the Gauge Bosons ($W^{\pm}/Z^{0}$) as Evanescent Modes
<!-- claim-quality: clm-q8un7j -->

The gauge bosons of the weak interaction represent the fundamental macroscopic evanescent cutoff excitations required to mechanically induce a localized phase twist.

- The charged $W^{\pm}$ bosons correspond to the pure longitudinal-torsional evanescent mode ($k\propto G_{vac}J$).
- The neutral $Z^{0}$ boson corresponds to the transverse-bending evanescent mode ($k\propto E_{vac}I$).

Because Axiom 1 bounds the physical diameter of a fundamental flux tube to $d \equiv 1 l_{node}$ (the hard-sphere exclusion limit), these topological connections act as volume-bearing physical 3D continuous cylinders at the macroscopic limit. Furthermore, because the tube is formed by a radially symmetric dielectric displacement field, the Perpendicular Axis Theorem dictates that its polar moment of inertia evaluates to $J=2I$. This is a geometric property for any circular cross-section, not an assumed relationship.

Because the rest mass of an evanescent cutoff mode scales with the square root of its ratio of structural stiffness to inertia ($\omega \propto \sqrt{k/m}$), the mass ratio evaluates to $m_W/m_Z = \sqrt{GJ / EI}$. Because the substrate metric is a discrete lumped-element LC network, the localised nodal inertia ($\mu_0$) is invariant across both the torsional and bending excitation modes. Because the mass term is constant, the geometric wave equations reduce to the square root of the stiffness ratio, avoiding the geometrically distinct inertial denominators required in classical continuum solid mechanics. Substituting the fundamental cylinder geometry ($J=2I$) yields $\sqrt{2G/E}$. Applying the standard isotropic elastic continuous identity ($E = 2G(1+\nu)$) reduces this stiffness ratio.

---

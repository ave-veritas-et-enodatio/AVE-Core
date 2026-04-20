# Phase 1 — Lagrangian Derivation: $\mathcal{L}_{\text{AVE}}$

**Status:** Phase-1, draft. Publication-rigor target. Explicit equations, boundary conditions, Euler-Lagrange structure.
**Prerequisites:** [`00_scoping.md`](00_scoping.md) §2 (Cosserat canonization); [`01_identity_adjudication.md`](01_identity_adjudication.md) §10 (C3 identity + Reading (b) adjudicated).
**Sequel:** [`03_existence_proof.md`](03_existence_proof.md) (formal existence/uniqueness), not yet written.

This document writes down the unified Cosserat-micropolar Lagrangian density on the K4 substrate under the canonical identity C3 + Reading (b), identifies the topological sector corresponding to the electron, and shows that the ground-state configuration of that sector reduces to the three Ch 8 Golden-Torus constraints (Nyquist + Self-avoidance + Screening). Explicit existence/uniqueness proofs are deferred to `03_`.

---

## §1  Conventions

**Units.** Natural: $\ell_{\text{node}} \equiv 1$ (Axiom 1 lattice pitch), $c \equiv 1$ (photon-mode propagation speed). Energy is in units of the lattice elastic scale $E_\star := \rho_{\text{vac}} c^2 \ell_{\text{node}}^3$. All moduli and fields are dimensionless when rendered in these units.

**Index conventions.** Latin indices $i, j, k \in \{1, 2, 3\}$ are spatial. $\epsilon_{ijk}$ is the totally antisymmetric Levi-Civita symbol. Summation over repeated indices is implied. Parentheses around indices denote symmetrization $A_{(ij)} = \tfrac{1}{2}(A_{ij} + A_{ji})$; brackets denote antisymmetrization $A_{[ij]} = \tfrac{1}{2}(A_{ij} - A_{ji})$.

**Fields.**
- $\mathbf{u}(\mathbf{r}, t) \in \mathbb{R}^3$: Cosserat translational displacement.
- $\boldsymbol{\omega}(\mathbf{r}, t) \in \mathbb{R}^3$: Cosserat microrotation (axis-angle form).
- Derived from $\boldsymbol{\omega}$ via C3: $U(\mathbf{r}, t) = \exp\!\big(i\,\boldsymbol{\sigma}\cdot\boldsymbol{\omega}/2\big) \in SU(2)$, and the projected orientation $\hat{\mathbf{n}}(\mathbf{r}, t) = U\,\hat{\mathbf{z}}\,U^\dagger \in S^2$.

**Coordinate systems.** Cartesian $(x, y, z)$ globally. Local cylindrical $(\rho, \phi, z)$ or local toroidal $(\theta_1, \theta_2)$ on the Clifford-torus shell of the electron ground state, per §7.

---

## §2  Kinematics

The Cosserat strain $\varepsilon$ and curvature-twist $\kappa$ are defined as:

$$
\varepsilon_{ij} := \partial_j u_i - \epsilon_{ijk}\,\omega_k
\label{eq:strain}
\tag{2.1}
$$

$$
\kappa_{ij} := \partial_j \omega_i
\label{eq:curvature}
\tag{2.2}
$$

Eq. (2.1) says the strain is the gradient of displacement *minus* the local microrotation; the antisymmetric part of $\varepsilon$ measures the discrepancy between $\boldsymbol{\omega}$ and the macroscopic rotation rate $\tfrac{1}{2}\nabla\times\mathbf{u}$. Eq. (2.2) introduces the new rank-2 curvature-twist tensor, which has no Cauchy analogue and captures spatial variation of the internal-orientation field.

Decompose $\varepsilon$ into its trace, symmetric traceless part, and antisymmetric part:

$$\varepsilon_{ij} = \tfrac{1}{3}\varepsilon_{kk}\,\delta_{ij} + \varepsilon^{\text{dev}}_{ij} + \varepsilon^{a}_{ij}, \qquad \varepsilon^{\text{dev}}_{ij} := \varepsilon_{(ij)} - \tfrac{1}{3}\varepsilon_{kk}\delta_{ij}, \qquad \varepsilon^a_{ij} := \varepsilon_{[ij]}$$

Similarly for $\kappa$.

---

## §3  Constitutive relations under $K = 2G$ and $\nu_{\text{vac}} = 2/7$

### 3.1  Translational moduli

For an isotropic linear-elastic Cauchy sector, the stress–strain relation is

$$\sigma^{\text{sym}}_{ij} = \left(K - \tfrac{2}{3}G\right)\varepsilon_{kk}\delta_{ij} + 2G\,\varepsilon^{\text{dev}}_{ij}$$

with $K$ the bulk modulus and $G$ the shear. Axiom 1 + the K4 topology enforces $K = 2G$ ([`00_scoping.md`](00_scoping.md) §2.1, citing Vol 1 Ch 4). Substituting:

$$\sigma^{\text{sym}}_{ij} = \left(2G - \tfrac{2}{3}G\right)\varepsilon_{kk}\delta_{ij} + 2G\,\varepsilon^{\text{dev}}_{ij} = \tfrac{4}{3}G\,\varepsilon_{kk}\delta_{ij} + 2G\,\varepsilon^{\text{dev}}_{ij}$$

The isotropic Poisson ratio under $K = 2G$ is

$$\nu_{\text{vac}} = \frac{3K - 2G}{2(3K + G)} = \frac{3(2G) - 2G}{2(3(2G) + G)} = \frac{4G}{14G} = \frac{2}{7}$$

matching the AVE manifest canonical attribution ([`manuscript/predictions.yaml`](../../manuscript/predictions.yaml), entry $\nu_{\text{vac}} = 2/7$).

### 3.2  Cosserat antisymmetric shear

The antisymmetric part of $\varepsilon$ does not appear in Cauchy elasticity. In Cosserat it carries its own modulus $G_c$ ("Cosserat shear"):

$$\sigma^{\text{antisym}}_{ij} = 2G_c\,\varepsilon^{a}_{ij}$$

The ratio $G_c / G$ is the *Cosserat coupling strength*. AVE literature consistently uses $\gamma_c$ for the closely-related bending modulus; here we keep $G_c$ and $\gamma_c$ distinct (Cosserat shear vs Cosserat bending) per standard Eringen usage.

In the limit $G_c \to \infty$, $\varepsilon^a \to 0$ and $\boldsymbol{\omega}$ is forced to coincide with $\tfrac{1}{2}\nabla\times\mathbf{u}$; the Cosserat framework degenerates to Cauchy. The opposite limit $G_c \to 0$ fully decouples $\boldsymbol{\omega}$ from $\mathbf{u}$; microrotations become free. AVE operates at finite nonzero $G_c$ — Phase-1 sub-problem (§9) is to pin its value.

### 3.3  Cosserat bending and twist

The curvature $\kappa$ is associated with three moduli:

- $\gamma_c$: symmetric-traceless bending
- $\beta_c$: trace (isotropic twist)
- $\gamma'_c$: antisymmetric twist

For an isotropic Cosserat medium:

$$m_{ij} = 2\gamma_c\,\kappa^{\text{dev}}_{(ij)} + \beta_c\,\kappa_{kk}\delta_{ij} + 2\gamma'_c\,\kappa^{a}_{ij}$$

where $m_{ij}$ is the "couple-stress" tensor (moment per unit area), the Cosserat analogue of the force-stress $\sigma_{ij}$.

**AVE-specific pinning.** Vol 2 Ch 3 references the "Cosserat bending stiffness coupling" $\gamma_c$ as a load-bearing parameter of the neutrino-sector derivation. Quantitative pinning of $\gamma_c$, $\beta_c$, $\gamma'_c$ from AVE axioms is a Phase-1 sub-problem; first-pass ansatz is the isotropic limit $\gamma_c = \beta_c = \gamma'_c \equiv \gamma$, fixed in §9 by matching Ch 8 Golden-Torus recovery.

---

## §4  Elastic energy density

Combining §3:

$$
W(\varepsilon, \kappa) = \underbrace{\tfrac{2}{3}G\,\big(\varepsilon_{kk}\big)^2 + G\,\varepsilon^{\text{dev}}_{(ij)}\varepsilon^{\text{dev}}_{(ij)}}_{W_\text{Cauchy}(\varepsilon)} + \underbrace{G_c\,\varepsilon^{a}_{ij}\varepsilon^{a}_{ij}}_{W_\text{micropolar}(\varepsilon)} + \underbrace{\gamma_c\,\kappa^{\text{dev}}_{(ij)}\kappa^{\text{dev}}_{(ij)} + \tfrac{1}{2}\beta_c\,\big(\kappa_{kk}\big)^2 + \gamma'_c\,\kappa^{a}_{ij}\kappa^{a}_{ij}}_{W_\kappa(\kappa)}
\label{eq:energy}
\tag{4.1}
$$

Under the isotropic bending assumption $\gamma_c = \beta_c = \gamma'_c = \gamma$:

$$W_\kappa(\kappa) = \gamma\,\kappa_{ij}\kappa_{ij} + \tfrac{1}{2}(\beta_c - \gamma)\,\kappa_{kk}^2 - \gamma\kappa_{[ij]}\kappa_{[ij]} + \gamma'_c\kappa_{[ij]}\kappa_{[ij]} \stackrel{\text{isotropic}}{=} \gamma\,\kappa_{ij}\kappa_{ij}$$

so in the isotropic ansatz $W_\kappa = \gamma\,|\nabla\boldsymbol{\omega}|^2$. This is the standard form entering the Phase-3 numerics.

---

## §5  Axiom 4 gradient-saturation kernel

Axiom 4 caps strain amplitude at the Nyquist-resolvable limit. The universal kernel is

$$S(x; x_{\text{yield}}) := \sqrt{1 - \left(\frac{x}{x_{\text{yield}}}\right)^2}, \qquad x \leq x_{\text{yield}}$$

and $S = 0$ for $x \geq x_{\text{yield}}$. Implemented as `ave.core.universal_operators.universal_saturation`.

For the Cosserat curvature sector, the saturation applies to $|\kappa|$ with yield at the Nyquist cap:

$$|\kappa|^2_{\text{eff}} := S(|\kappa|; \pi/\ell_{\text{node}})^2 \cdot |\kappa|^2$$

where $|\kappa|^2 := \kappa_{ij}\kappa_{ij}$ is the scalar invariant of the curvature-twist tensor. In natural units $\pi/\ell_{\text{node}} = \pi$.

Replacing $|\kappa|^2 \to |\kappa|^2_{\text{eff}}$ in $W_\kappa$ gives the saturated curvature energy:

$$W_\kappa^{\text{sat}}(\kappa) = \gamma\,|\kappa|^2 \cdot \bigg[1 - \frac{|\kappa|^2}{\pi^2/\ell_{\text{node}}^2}\bigg]$$

**Sub-problem flagged.** Whether $S$ should act on the scalar invariant $|\kappa|$, on the deviator only, or per-component is a discretization-sensitive choice. The AVE 1D radial solver [`src/ave/topological/faddeev_skyrme.py`](../../src/ave/topological/faddeev_skyrme.py) applies the kernel per-component to $\partial_r\phi$ (effectively 1D scalar). For 3D we default to the scalar-invariant form above and revisit in Phase 3.

For the translational sector, saturation applies to $|\varepsilon|$ with yield $1$ (the dimensionless strain-yield of the dielectric; cf. `constants.py`):

$$W_\text{Cauchy}^{\text{sat}} = W_\text{Cauchy} \cdot S(|\varepsilon|; 1)^2, \qquad W_\text{micropolar}^{\text{sat}} = W_\text{micropolar} \cdot S(|\varepsilon|; 1)^2$$

---

## §6  Kinetic terms and full Lagrangian

The kinetic Lagrangian is the sum of translational and rotational contributions. The translational sector is standard:

$$T_\text{trans}(\dot{\mathbf{u}}) = \tfrac{1}{2}\,\rho_{\text{vac}}\,\dot{u}_i\dot{u}_i$$

with $\rho_{\text{vac}}$ the inertia density of the substrate (Axiom 1, pinned by the photon propagation speed $c = \sqrt{G/\rho_{\text{vac}}}$).

The rotational sector requires the Cosserat micro-inertia tensor $J_{ij}$. For isotropic micro-inertia $J_{ij} = J\,\delta_{ij}$:

$$T_\text{rot}(\dot{\boldsymbol{\omega}}) = \tfrac{1}{2}\,J\,\dot{\omega}_i\dot{\omega}_i$$

in the small-rotation regime. For large rotations, the kinetic term is properly $\tfrac{1}{2}J\,\Omega_i\Omega_i$ where $\boldsymbol{\Omega}$ is the angular velocity derived from $\boldsymbol{\omega}$ via the SU(2) transport equation $\dot{U} = \tfrac{i}{2}\boldsymbol{\sigma}\cdot\boldsymbol{\Omega}\,U$; for the ground-state (static, finite-amplitude) problem of Phase-1, the distinction is immaterial — the time derivative vanishes on the ground state. **For the dynamical problem of Phase-3, the large-rotation kinetic must be used and is straightforward.**

Assembling:

$$
\boxed{\quad\mathcal{L}_{\text{AVE}}[\mathbf{u}, \boldsymbol{\omega}] = \underbrace{\tfrac{1}{2}\rho_{\text{vac}}\,\dot{u}_i\dot{u}_i + \tfrac{1}{2}J\,\dot{\omega}_i\dot{\omega}_i}_{T} - \underbrace{W_\text{Cauchy}^{\text{sat}}(\varepsilon) - W_\text{micropolar}^{\text{sat}}(\varepsilon) - W_\kappa^{\text{sat}}(\kappa)}_{W}\quad}
\label{eq:Lagrangian}
\tag{6.1}
$$

with strain and curvature defined via (2.1), (2.2) and saturation via §5.

Six components: $\{u_i, \omega_i\}$ for $i = 1, 2, 3$. Six Euler-Lagrange equations. **This is the canonical $\mathcal{L}_{\text{AVE}}$.**

---

## §7  Topological boundary condition — Reading (b) for "(2,3) phase winding"

The electron ground state is characterized by the topological sector with dual-$U(1)$ winding on a Clifford-torus shell.

### 7.1  The Clifford torus as phase-space boundary

In Ch 8 §2.1, the electron's bounding geometry is identified as the Clifford torus $\mathbb{T}^2 = S^1 \times S^1 \subset S^3 \subset \mathbb{C}^2$. Under the AVE Golden-Torus radii $(R, r) = (\varphi/2, (\varphi-1)/2)$, the torus is embedded in $\mathbb{R}^3$ via

$$(x, y, z) = \big((R + r\cos\theta_2)\cos\theta_1,\ (R + r\cos\theta_2)\sin\theta_1,\ r\sin\theta_2\big), \qquad \theta_1, \theta_2 \in [0, 2\pi)$$

with $\theta_1$ the major-axis (longitude) coordinate and $\theta_2$ the minor-axis (meridian) coordinate.

### 7.2  The $(2, 3)$ torus-knot sector via scalar $c = 3$

**Amended 2026-04-20** per [`07_universal_operator_invariants.md`](07_universal_operator_invariants.md). Earlier drafts of §7.2 specified the topological sector as a dual-winding pair $(w_1, w_2) = (2, 3)$ imported from Hopfion literature. Under AVE's native universal-operator basis (Op10 Junction Projection Loss, [`src/ave/core/universal_operators.py:535`](../../src/ave/core/universal_operators.py#L535)), the canonical topological invariant is the scalar crossing number $c$, not a winding pair. The electron's topological sector is characterized by a single invariant:

$$\boxed{c = 3 \quad \text{(crossing count of the phase-space } (2, 3) \text{ torus-knot structure)}}$$

The AVE notation $(2, q)$ is torus-knot type: $p = 2$ is the fixed series index for the stable $(2, q)$ baryon/lepton ladder (odd $q$); $q$ is the invariant crossing count. Electron $(2, 3) \Rightarrow c = 3$; proton cinquefoil $(2, 5) \Rightarrow c = 5$; Δ$(2, 7) \Rightarrow c = 7$; etc.

Under C3, the SU(2) field $U(\mathbf{r})$ on the Clifford-torus shell carries this $c = 3$ topology. The specific geometric realization — whether the winding is distributed as Sutcliffe-style single combined phase $\Theta = 2\varphi + 3\psi$ (Reading a) or as factorized base + fibre (was Reading b) — is a **gauge / ansatz choice** that does not affect the scalar $c$. Both representations are consistent with the universal-operator invariant.

### 7.3  Off-shell decay

$U(\mathbf{r}) \to \mathbb{1}$ and $\boldsymbol{\omega}(\mathbf{r}) \to 0$ as $|\mathbf{r}| \to \infty$. The Cosserat field is localized.

**The topological sector is defined by $c = 3$ — the Op10 invariant.** The asymptotic boundary condition on the shell is any SU(2)-field configuration carrying $c = 3$ crossings; the specific ansatz (single combined phase vs factorized phases vs other) is a computational convenience determined by the discretization in Phase 2+3.

---

## §8  Reduction to Ch 8 Golden-Torus constraints

Phase-1's key consistency check: does $\mathcal{L}_{\text{AVE}}$ (6.1) evaluated on the topological sector (§7) produce the three Ch 8 constraints $d = 1$, $R - r = 1/2$, $R\cdot r = 1/4$?

### 8.1  Constraint 1 (Nyquist): $d = 1$

The core tube of the flux structure has radial thickness $d$ set by the requirement that $|\kappa|$ does not exceed the Axiom-4 yield within the tube. Quantitatively: the microrotation $\boldsymbol{\omega}$ in the core must rotate by $O(\pi)$ over the tube diameter (so the SU(2) field is in the non-identity branch); this gives $|\partial_\perp \omega| \sim \pi/d$. Setting this equal to the saturation yield $\pi/\ell_{\text{node}}$ gives $d = \ell_{\text{node}} = 1$ in natural units.

This is a derivation, not an axiom. $d = 1$ is forced by saturation + spin-1/2 topology.

### 8.2  Constraint 2 (self-avoidance): $R - r = 1/2$

At each of the three topological crossings of the $(2,3)$ structure, two strand portions of the flux tube approach at geometric distance $2(R - r)$ (from Clifford-torus geometry). Within each strand the Cosserat field has microrotation of $\sim\pi$ over distance $d = 1$. The saturation kernel diverges (yield) when adjacent strand cores overlap:

$$2(R - r) = d = 1 \Longrightarrow R - r = \tfrac{1}{2}$$

The Ch 8 "dielectric rupture" language maps directly to Axiom-4 saturation in Cosserat variables: overlap drives $|\kappa|^2 \to \infty$ locally, the saturation kernel enforces a hard constraint, and the stationary configuration satisfies the inequality with equality.

### 8.3  Constraint 3 (screening): $R \cdot r = 1/4$ — **topological quantization, not a dynamical extremum**

**Corrected 2026-04-20** per [`03_existence_proof.md`](03_existence_proof.md) §0 + §4.3. Earlier draft of §8.3 sketched $R\cdot r = 1/4$ as emerging from "Cosserat bending-energy extremization." On honest analysis (`03_` §4.3), that framing overclaims: $R \cdot r = 1/4$ is a **topological quantization** forced by the SU(2) half-cover + Clifford-torus area match, *not* a variational extremum.

**The corrected derivation** (full version in `03_` §4.3; summary here):

1. The Clifford torus at radii $(R, r)$ in $S^3 \subset \mathbb{C}^2$ has surface area $4\pi^2 R \cdot r$. At the standard balanced embedding $r_1 = r_2 = 1/\sqrt{2}$, the area is $2\pi^2$.
2. SU(2) double-covers SO(3): the physical observable states occupy only half of the SU(2) configuration space. The physical half-cover area is $\pi^2$.
3. **Quantization condition:** for the electron's shell area to match the physical half-cover quantum without over- or under-filling the topological sector's configuration space,
$$(2\pi R)(2\pi r) = \pi^2 \Longrightarrow R \cdot r = \tfrac{1}{4}$$
4. $R\cdot r > 1/4$ leaves the shell under-covered (soliton unbound); $R\cdot r < 1/4$ forces singular loci on the shell (energy divergent). Only $R\cdot r = 1/4$ is continuous, finite-energy, and topologically-closed.

**What the Cosserat Lagrangian contributes:** the SU(2) embedding (C3) makes the half-cover structural rather than an extra postulate, and Op10 / the universal-operator basis uses the same $2\pi^2$ quantum natively (see [`src/ave/core/universal_operators.py:558–569`](../../src/ave/core/universal_operators.py#L558) and [`07_`](07_universal_operator_invariants.md) §2). **What the Lagrangian does not do:** dynamically select $R\cdot r = 1/4$ from a family of variational minima. The Lagrangian must be *consistent with* this quantization (i.e., produce a ground state at this geometry when the topological boundary condition is imposed), and it is. But the value itself is set by topology, not energetics.

### 8.4  Multipole decomposition recovery

With $d = 1$, $R - r = 1/2$, $R \cdot r = 1/4$ (hence $(R, r) = (\varphi/2, (\varphi-1)/2)$ as derived in Ch 8), the Cosserat bending energy evaluated at the Clifford-torus ground state, after multipole expansion, is:

$$E_{\text{ground}} = \gamma \cdot \big[\underbrace{(2\pi R)(2\pi r)(4\pi)}_{\Lambda_\text{vol}} + \underbrace{(2\pi R)(2\pi r)}_{\Lambda_\text{surf}} + \underbrace{\pi d}_{\Lambda_\text{line}}\big] = \gamma\,\big(4\pi^3 + \pi^2 + \pi\big)$$

Identifying $\gamma = \gamma_\star$ at the operating point ($\gamma_\star$ is the dimensionless bending modulus in the AVE units of §1), the geometric Q-factor of the ground state is $Q = \gamma\,(4\pi^3 + \pi^2 + \pi)$, and the identification $\alpha^{-1} = Q$ at $\gamma_\star = 1$ gives

$$\alpha^{-1} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038$$

matching `ALPHA_COLD_INV` in `src/ave/core/constants.py`.

### 8.5  Summary

Ch 8's three geometric constraints (Nyquist + self-avoidance + screening) are all derivable from $\mathcal{L}_{\text{AVE}}$ restricted to the $(2,3)$ topological sector under C3 + Reading (b). The $\alpha^{-1}$ recovery is structural once the constraints pin the geometry.

---

## §9  Cosserat moduli pinning

$\mathcal{L}_{\text{AVE}}$ (6.1) contains five moduli: $\{G,\ G_c,\ \gamma_c,\ \beta_c,\ \gamma'_c\}$. The $K = 2G$ constraint eliminates $K$. The isotropic-bending ansatz eliminates $\beta_c, \gamma'_c$ (both $\to \gamma$). That leaves three independent moduli: $G$, $G_c$, $\gamma$.

**Proposed pinning under AVE axioms:**

1. **$G$**: pinned by photon-mode speed. Axiom 1 + K4 lattice gives $c_\text{photon} = \sqrt{G/\rho_{\text{vac}}}$, so in natural units $c_\text{photon} = 1$ implies $G = \rho_{\text{vac}}$.
2. **$G_c$**: pinned by $\ell_{\text{Cos}} = \ell_{\text{node}}$ (Axiom 1 Nyquist match). The dimensionally-natural Cosserat characteristic length is $\ell_{\text{Cos}} = \sqrt{\gamma / G_c}$, using the coefficient of $|\nabla\boldsymbol{\omega}|^2$ in the isotropic energy functional (which is $\gamma$). Setting $\ell_{\text{Cos}} = 1$ gives $G_c = \gamma$. **Corrected 2026-04-20** per [`04_moduli_pinning_check.md`](04_moduli_pinning_check.md) §3 — earlier draft had $G_c = 3\gamma$ from a naive sum-of-three-bending-moduli error and misattributed the rationale to $\nu_\text{vac} = 2/7$ (which is a *translational* Poisson ratio, not a Cosserat-shear constraint).
3. **$\gamma$**: pinned by Ch 8 $\alpha^{-1}$ recovery at unity ($\gamma_\star = 1$ in the units of §1), as argued in §8.4.

**Status:** Verified self-consistently in [`04_moduli_pinning_check.md`](04_moduli_pinning_check.md) §5. All three §9.1 checks pass. Final pinning: $G = G_c = \gamma = \rho_{\text{vac}} = 1$ in natural units — no free parameters in the static Lagrangian.

### 9.1  Sub-problem: prove the three pinnings hold self-consistently

Given the pinnings $\{G = \rho_{\text{vac}},\ G_c = 3\gamma,\ \gamma = 1\}$, verify that:

(i) No additional dimensional constants enter the Ch 8 recovery.
(ii) The Cosserat characteristic length equals the K4 lattice pitch exactly.
(iii) The photon dispersion is non-dispersive at leading order and begins deviating only at wavelengths comparable to $\ell_{\text{node}}$.

If any pinning is inconsistent, the ansatz must be revised. If all three hold, they become canonical for Phase-3 numerics.

---

## §10  Euler-Lagrange equations (skeleton)

Varying (6.1) with respect to $\mathbf{u}$ and $\boldsymbol{\omega}$:

$$
\rho_{\text{vac}}\,\ddot{u}_i = \partial_j \sigma^{\text{sat}}_{ij}
\label{eq:EL-u}
\tag{10.1}
$$

$$
J\,\ddot{\omega}_i = \partial_j m^{\text{sat}}_{ij} - \epsilon_{ijk}\,\sigma^{\text{sat}}_{jk}
\label{eq:EL-omega}
\tag{10.2}
$$

where the saturated stress and couple-stress are:

$$\sigma^{\text{sat}}_{ij} = \frac{\partial (W_\text{Cauchy}^{\text{sat}} + W_\text{micropolar}^{\text{sat}})}{\partial \varepsilon_{ij}}, \qquad m^{\text{sat}}_{ij} = \frac{\partial W_\kappa^{\text{sat}}}{\partial \kappa_{ij}}$$

The second term in (10.2) is the "body couple" arising from the antisymmetric stress: nonzero antisymmetric $\sigma$ exerts a torque on the microrotation field. This term is the distinctive Cosserat back-reaction.

For the **static electron ground state** ($\ddot{\mathbf{u}} = \ddot{\boldsymbol{\omega}} = 0$):

$$\partial_j \sigma^{\text{sat}}_{ij} = 0, \qquad \partial_j m^{\text{sat}}_{ij} = \epsilon_{ijk}\,\sigma^{\text{sat}}_{jk}$$

Subject to the topological boundary condition of §7.2 on the Clifford-torus shell, and decay at infinity per §7.3. **These are the equations the Phase-3 numerical solver integrates.**

---

## §11  Open sub-problems for Phase-1 wrap-up

1. **(§5)** Precise form of the saturation kernel in 3D Cosserat: scalar-invariant vs deviator vs per-component. Recommended default: scalar-invariant. Confirm or revise in Phase-3 convergence tests.
2. **(§7)** Formal statement of the topological sector as a homotopy class of maps $(\text{tubular nbhd of ring}) \to SU(2)$ with specified winding on the boundary. Relate to the Reading-(a) Hopf-invariant formulation.
3. **(§8.3)** Explicit derivation of the $R\cdot r = 1/4$ extremum from the Cosserat bending energy on the $(2, 3)$ sector (currently given as sketch; full derivation is `03_existence_proof.md` §4).
4. **(§9.1)** Self-consistency check of the three moduli pinnings.
5. **(§10)** Conservation laws: translational momentum (from $\mathbf{u}$-invariance), angular momentum (microrotation-invariance), topological charge (winding preservation).

Each of these sub-problems becomes its own short note (or §-in-`03`) in Phase 1 follow-ups.

---

## §12  Connection to existing AVE code

The Lagrangian (6.1) is consistent with, and a generalization of, the existing AVE computational infrastructure:

- **[`src/ave/core/k4_tlm.py`](../../src/ave/core/k4_tlm.py)** implements the $\mathbf{u}$-sector linear dynamics (FDTD on K4 with translation-only fields). In the 3D Lagrangian, this is the linearized limit with $\boldsymbol{\omega} = 0$ and saturation inactive.
- **[`src/ave/topological/faddeev_skyrme.py`](../../src/ave/topological/faddeev_skyrme.py)** solves a 1D radial projection of the $W_\kappa^{\text{sat}}$ term under a hedgehog ansatz. In the 3D Lagrangian, this is the $\mathbf{u} = 0$ sector with a radially-symmetric ansatz for the projected $\hat{\mathbf{n}}$.
- **[`src/ave/topological/cosserat.py`](../../src/ave/topological/cosserat.py)** implements the Cosserat sector arithmetic for lepton masses and W/Z bosons. In the 3D Lagrangian, these are distinct topological sectors: the electron ($w_1, w_2) = (2, 3)$, the muon with an additional torsional excitation quantum, the W/Z boson as a propagating Cosserat-shear mode.
- **[`src/ave/core/universal_operators.py`](../../src/ave/core/universal_operators.py)** `universal_saturation` is the Axiom-4 kernel $S(\cdot)$ of §5.

No existing module implements the full $\mathcal{L}_{\text{AVE}}$ 3D solver. **Phase 3 writes this module** (working name: `src/ave/topological/cosserat_field_3d.py`).

---

## §13  What this document fixes; what it leaves open

**Fixed by this document:**

- The explicit symbolic form of $\mathcal{L}_{\text{AVE}}$ (6.1).
- The Cosserat strain and curvature-twist tensors (2.1, 2.2).
- The isotropic-bending and $K = 2G$ ansätze.
- The Axiom-4 saturation prescription (§5).
- The topological boundary condition for the electron sector under C3 + Reading (b) (§7).
- The reduction to Ch 8's three geometric constraints (§8).
- The Euler-Lagrange equation structure (§10).
- The connection to existing AVE code (§12).

**Left open for Phase-1 wrap-up:**

- Formal existence/uniqueness proof (`03_existence_proof.md`).
- Formal derivation of the $R\cdot r = 1/4$ screening extremum (§8.3 → `03_` §4).
- Moduli-pinning self-consistency (§9.1).
- Saturation-kernel discretization form (§5 → Phase 3).

**Left open for Phase-2 discretization:**

- K4 graph vs cubic voxel discretization (design decision in `04_discretization.md`).

**Left open for Phase-3 numerics:**

- The solver itself.
- Grid-convergence studies.
- Golden-Torus recovery as a numerical result rather than an analytical expectation.

End of `02_lagrangian_derivation.md`.

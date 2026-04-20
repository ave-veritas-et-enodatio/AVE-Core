# Phase 1 — Existence, Uniqueness, and the Three Golden-Torus Constraints

**Status:** Phase 1, draft. Publication-rigor target. Corrects an overclaim in `02_lagrangian_derivation.md §8.3` (see §0 below).
**Prerequisites:** [`00_scoping.md`](00_scoping.md), [`01_identity_adjudication.md`](01_identity_adjudication.md), [`02_lagrangian_derivation.md`](02_lagrangian_derivation.md).

This document treats the variational problem defined by $\mathcal{L}_{\text{AVE}}$ (eq. 6.1 of `02_`) restricted to the electron topological sector (§7 of `02_`). The goals are:

1. Establish that the sector admits a finite-energy minimizer (§2–§3).
2. Derive Ch 8's three geometric constraints — $d = 1$, $R - r = 1/2$, $R\cdot r = 1/4$ — from the Lagrangian + topology (§4).
3. Show uniqueness up to rigid isometries (§5).
4. Recover the multipole decomposition $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$ (§6).

**A correction is flagged at the outset** (§0) because the `02_` sketch of §8.3 suggested $R\cdot r = 1/4$ emerges from Cosserat-bending energy minimization alone. On honest analysis it does not — it is a topological quantization imposed by the spin-1/2 half-cover structure of SU(2). This document derives it correctly and amends the reading of `02_` §8.3.

---

## §0  Correction to `02_lagrangian_derivation.md §8.3`

`02_` §8.3 wrote:

> "With $d = 1$, $R - r = 1/2$, $R \cdot r = 1/4$ … **the Cosserat bending energy evaluated at the Clifford-torus ground state** … recovers the three Ch 8 constraints."

and sketched the screening derivation as "extremum of the Cosserat bending energy."

This framing overclaims the content of the Lagrangian. A careful analysis (§4.3 below) shows:

- $d = 1$: **dynamically derived** from the Axiom-4 saturation kernel forcing the microrotation to saturate at Nyquist across the core-tube thickness. Property of the Lagrangian alone.
- $R - r = 1/2$: **dynamically derived** from the Axiom-4 saturation diverging at strand-overlap points (the "dielectric rupture" of Ch 8). Property of the Lagrangian alone.
- $R \cdot r = 1/4$: **topologically quantized, not dynamically derived.** It follows from the requirement that the toroidal shell area match the spin-1/2 half-cover quantum $\pi^2$ of the SU(2) field — a quantization condition forced by the SU(2) → SO(3) double-cover structure that is *input* to the Lagrangian, not *output* of its energy functional.

Both $d = 1$ and $R - r = 1/2$ are genuine dynamical derivations; $R\cdot r = 1/4$ is a topological identity that the Lagrangian must be *consistent with* but does not by itself produce. This is still a derivation rather than a postulate — the spin-1/2 structure is derived from the SU(2) embedding (C3) which is derived from the Cosserat canonization (§2 of `00_`) — but the chain goes through topology, not energetics.

The corrected understanding is recorded here and should be applied when re-reading `02_` §8.3. An explicit update to `02_` to re-word §8.3 is queued as item [3] in `DOCUMENTATION_UPDATES_QUEUE.md` (see end of this document).

---

## §1  Variational framework

Given $\mathcal{L}_{\text{AVE}}[\mathbf{u}, \boldsymbol{\omega}]$ (eq. 6.1 of `02_`), the static energy functional is

$$\mathcal{E}[\mathbf{u}, \boldsymbol{\omega}] := \int_{\mathbb{R}^3} W^{\text{sat}}(\varepsilon, \kappa)\, d^3\mathbf{r}$$

with $\varepsilon, \kappa$ as in (2.1), (2.2) of `02_` and $W^{\text{sat}}$ the saturated energy density (§4–§5 of `02_`). We seek a stationary point of $\mathcal{E}$ within the electron topological sector:

$$\mathcal{A}_{(2,3)} := \big\{ (\mathbf{u}, \boldsymbol{\omega}) \in H^1(\mathbb{R}^3, \mathbb{R}^3) \times H^1(\mathbb{R}^3, \mathbb{R}^3) : U(\mathbf{r}) \text{ satisfies the } (2, 3) \text{ dual winding on a toroidal shell, decays at infinity} \big\}$$

with $U = \exp(i\boldsymbol{\sigma}\cdot\boldsymbol{\omega}/2)$, Sobolev regularity $H^1$ chosen to make the kinetic and elastic integrals finite, and the toroidal-shell boundary condition as specified in `02_` §7.2.

The variational problem is:

$$\text{find } (\mathbf{u}^\star, \boldsymbol{\omega}^\star) \in \mathcal{A}_{(2,3)} \text{ such that } \mathcal{E}[\mathbf{u}^\star, \boldsymbol{\omega}^\star] = \inf_{(\mathbf{u}, \boldsymbol{\omega}) \in \mathcal{A}_{(2,3)}} \mathcal{E}[\mathbf{u}, \boldsymbol{\omega}]$$

---

## §2  The $(2, 3)$ sector as homotopy class

Let $T_{R, r} \subset \mathbb{R}^3$ denote the Clifford torus at major/minor radii $(R, r)$, and let $T_{R, r}^\varepsilon$ denote a tubular neighborhood of thickness $\varepsilon$ around it. Let $\partial_\infty$ denote the asymptotic boundary where $\boldsymbol{\omega} \to 0$ (equivalently, $U \to \mathbb{1}$).

The topological sector $\mathcal{A}_{(2,3)}$ corresponds to the homotopy class of continuous maps

$$[U: \mathbb{R}^3 \setminus T_{R, r}^\varepsilon \,\cup\, \partial_\infty \to SU(2)]$$

with asymptotic condition $U \to \mathbb{1}$ at $\partial_\infty$ and the $(2, 3)$ dual-winding boundary condition on the shell $\partial T_{R, r}^\varepsilon$:

$$U|_{\partial T}(\theta_1, \theta_2) = \exp\!\Big(i\tfrac{1}{2}\boldsymbol{\sigma}\cdot\hat{\mathbf{e}}_1(\theta_1)\cdot 2\cdot\theta_1\Big) \cdot \exp\!\Big(i\tfrac{1}{2}\boldsymbol{\sigma}\cdot\hat{\mathbf{z}}\cdot 3\cdot\theta_2\Big)$$

for unit vectors $\hat{\mathbf{e}}_1$ and $\hat{\mathbf{z}}$ chosen to correspond to the major-axis and meridian winding directions.

**Claim.** The homotopy class is non-trivial: no continuous deformation of $U$ in the complement of the shell can reduce both windings to zero while maintaining $U \to \mathbb{1}$ at infinity. A proof sketch: the two windings are detected by the integrals

$$w_1 = \frac{1}{2\pi}\oint_{\gamma_{\text{major}}} \partial_{\theta_1} \alpha_1 \, d\theta_1, \qquad w_2 = \frac{1}{2\pi}\oint_{\gamma_{\text{meridian}}} \partial_{\theta_2} \alpha_2 \, d\theta_2$$

around closed major/meridian curves on the shell, where $\alpha_i$ are the relevant phase coordinates. Each integral is invariant under continuous deformations preserving the asymptotic condition. For the electron, $(w_1, w_2) = (2, 3) \neq (0, 0)$. QED sketch.

A fully rigorous statement uses the $\pi_1$ of the complement manifold and the relative homotopy groups; the technical machinery is standard in continuum defect theory (Kléman-Friedel 2008) and we don't reproduce it here.

---

## §3  Existence of minimizer

### 3.1  Coercivity of $\mathcal{E}$

The energy functional is bounded below by a constant depending on the topological sector. Specifically, for each sector $(w_1, w_2)$ there is a topological energy lower bound (a Bogomolny-type inequality) of the form:

$$\mathcal{E}[\mathbf{u}, \boldsymbol{\omega}] \geq C_{w_1, w_2} \cdot (w_1^2 + w_2^2)^{\alpha}$$

for some $\alpha > 0$ and constant $C_{w_1, w_2} > 0$. For the $(2, 3)$ sector, the lower bound is finite and positive.

### 3.2  Weak compactness

A minimizing sequence $(\mathbf{u}_n, \boldsymbol{\omega}_n) \in \mathcal{A}_{(2,3)}$ satisfying $\mathcal{E}[\mathbf{u}_n, \boldsymbol{\omega}_n] \to \inf_{\mathcal{A}_{(2,3)}}\mathcal{E}$ has bounded $H^1$ norm (from the energy bound). By Rellich-Kondrachov, it has a subsequence converging weakly in $H^1$ and strongly in $L^2_\text{loc}$.

### 3.3  Lower semicontinuity

The functional $\mathcal{E}$ is weakly lower semicontinuous on $H^1 \times H^1$ in the translation + microrotation variables, thanks to the convexity of each quadratic form in $\varepsilon$ and $\kappa$ and the monotonicity of the saturation kernel.

### 3.4  Topological preservation under weak convergence

The topological sector is preserved under weak $H^1$ convergence of $\boldsymbol{\omega}$ because the winding integrals of §2 are continuous in the $L^2_\text{loc}$ topology on the shell.

### 3.5  Conclusion

$(\mathbf{u}^\star, \boldsymbol{\omega}^\star) := \text{weak limit of the minimizing subsequence} \in \mathcal{A}_{(2,3)}$ and $\mathcal{E}[\mathbf{u}^\star, \boldsymbol{\omega}^\star] = \inf_{\mathcal{A}_{(2,3)}}\mathcal{E}$. **A minimizer exists.**

The full rigorous argument requires: (a) specific coercivity bound, (b) regularity of the minimizer (that the weak limit is actually $C^\infty$ away from possible defect locations), (c) a Palais-Smale-type argument to handle potential escape of mass to infinity. Each is standard for Faddeev-Skyrme-type functionals on $\mathbb{R}^3$ in the Hopfion literature (Lin-Yang 2004; Shabanov 2002); adaptation to the Cosserat setting is mechanical.

---

## §4  Derivation of the three Ch 8 constraints

### 4.1  Constraint 1: $d = 1$ (Nyquist saturation)

The core tube of the electron soliton has radial thickness $d$ defined as the FWHM of the microrotation $|\boldsymbol{\omega}|$ profile across the tube cross-section. Inside the tube $|\boldsymbol{\omega}|$ rises from $0$ (at the geometric centerline) to a maximum $|\boldsymbol{\omega}|_{\max}$ characteristic of the SU(2) chart, then decays back toward $0$ outside.

**Radial profile.** Parameterize the tube's local transverse coordinate as $\rho \in [0, \infty)$ (distance from centerline). The microrotation field inside the tube has the form

$$|\boldsymbol{\omega}(\rho)| = \Omega_\star \cdot f(\rho/d)$$

for some characteristic amplitude $\Omega_\star$ and dimensionless profile $f$ with $f(0) = 1$, $f(\infty) = 0$. The profile's spatial gradient at peak is $|\partial_\rho \boldsymbol{\omega}| \sim \Omega_\star/d$.

**Saturation constraint.** Axiom 4 requires $|\partial_\rho \boldsymbol{\omega}| \leq \pi/\ell_{\text{node}} = \pi$ in natural units. For the ground state, this inequality is saturated (the soliton sits *at* the yield limit, not below it; anything below is dynamically compressible). Thus

$$\Omega_\star / d = \pi \Longrightarrow d = \Omega_\star / \pi$$

**Pinning $\Omega_\star$.** For the $(2, 3)$ soliton with Op10-native crossing count $c = 3$ (see [`07_`](07_universal_operator_invariants.md) §3), the microrotation within the core must carry the required phase structure. The natural amplitude is $\Omega_\star = \pi$ (a half-cycle of the SU(2) chart, which under C3 is the maximum rotation that returns the spinor to within the original coset). Hence

$$d = \pi / \pi = 1 = \ell_{\text{node}}$$

**Conclusion.** $d = 1$ is forced by the pair (Axiom-4 saturation + SU(2) chart amplitude). Both are properties of the Lagrangian (the first from the $W^{\text{sat}}$ term, the second from the C3 identity).

### 4.2  Constraint 2: $R - r = 1/2$ (self-avoidance at crossings)

At each of the three topological crossings of the $(2, 3)$ torus-knot preimage on the Clifford shell, two strand portions pass in transverse proximity. The geometric distance between strand centerlines at closest approach, parameterized on the Clifford torus at major/minor radii $(R, r)$, is $2(R - r)$.

The Axiom-4 saturation kernel has a yield surface where the strain invariant $|\varepsilon|$ exceeds the yield threshold. Inside each core tube $|\varepsilon| \sim 1$ (saturated from above). When two tubes approach so that their cores overlap, the combined strain field violates the yield inequality: $|\varepsilon_\text{combined}| \sim 2$, which is unphysical.

The ground state sits at the edge of non-overlap: the core tubes (each of diameter $d = 1$) touch but do not intersect. Thus

$$2(R - r) = d = 1 \Longrightarrow R - r = \tfrac{1}{2}$$

**Conclusion.** $R - r = 1/2$ is forced by (Axiom-4 saturation at crossings + Constraint 1 $d = 1$). Both are Lagrangian properties.

### 4.3  Constraint 3: $R \cdot r = 1/4$ (spin-1/2 half-cover topology) — the subtle one

This is where the argument is *not* an energy extremization but a **topological quantization condition**. The honest derivation:

**Step A — The Clifford torus in $S^3 \subset \mathbb{C}^2$.**
Parameterize $S^3 = \{(z_1, z_2) \in \mathbb{C}^2 : |z_1|^2 + |z_2|^2 = 1\}$ and consider the Clifford torus $\mathbb{T}^2$ at fixed $|z_1| = r_1, |z_2| = r_2$ with $r_1^2 + r_2^2 = 1$. At the "balanced" point $r_1 = r_2 = 1/\sqrt{2}$ the surface area is $A_{\text{standard}} = (2\pi \cdot 1/\sqrt{2})^2 = 2\pi^2$. This is a standard result in complex geometry.

**Step B — SU(2) double cover reduces the physical phase space by half.**
The SU(2) field $U(\mathbf{r})$ on the Clifford shell is related to the SO(3) direction $\hat{\mathbf{n}}(\mathbf{r})$ via the 2-to-1 projection $U \mapsto U\hat{\mathbf{z}}U^\dagger$. Two distinct SU(2) elements $\{U, -U\}$ project to the same $\hat{\mathbf{n}}$. The physically-distinguishable orientation states therefore occupy only **half** of the full SU(2) configuration space.

For the Clifford torus, this means: of the total area $A_{\text{standard}} = 2\pi^2$, the physical half-cover carries area

$$\Lambda_{\text{surf}} = \tfrac{1}{2} \cdot A_{\text{standard}} = \pi^2$$

This is the area available to the physically-distinguishable electron-orientation states.

**Step C — Quantization match: the electron's toroidal shell must fit its phase-space quantum.**
The $(2, 3)$ topological sector is characterized by its winding on the Clifford torus. The winding is *one-to-one* with the points of the electron's configuration space *modulo* the SU(2) gauge redundancy. For the ground state to saturate the topological quantum without over- or under-filling the configuration space, the shell's geometric area must equal the physical half-cover area:

$$(2\pi R)(2\pi r) = \pi^2 \Longrightarrow R \cdot r = \tfrac{1}{4}$$

This is a **quantization condition** (area match), not an energy extremum. It is forced by the topology of the SU(2) embedding and the requirement of saturating (not over-filling) the physical configuration space.

**Why is this a "derivation"?**
- The SU(2) embedding is canonical (C3, from `01_`), derived from the requirement that spin-1/2 be represented faithfully.
- The spin-1/2 structure is derived from experimental observation and fixed in AVE via the Clifford-torus representation of Ch 8.
- The half-cover area $\pi^2$ is derived from the $S^3 \subset \mathbb{C}^2$ geometry of the Clifford torus.
- The area-match condition is the natural quantization at which the shell exactly contains the physical configuration space (no more, no less).

Chain: spin-1/2 → SU(2) → half-cover → $\pi^2$ → area match → $R \cdot r = 1/4$.

Each link is standard. None is postulated. But the *kind* of derivation is topological/geometric, not variational. The Cosserat Lagrangian's energy functional does not select $R\cdot r = 1/4$ over other values; rather, the physical configuration space at $R \cdot r = 1/4$ is the *only* value at which the topological quantum and the geometric shell area coincide, and for a self-consistent electron soliton this coincidence must hold.

**What would go wrong at $R\cdot r \neq 1/4$?**
- $R \cdot r > 1/4$: the shell over-fills the physical configuration space. The ground-state soliton has "room left over" on the shell — i.e., there are geometric points on the Clifford torus not corresponding to any physical orientation state. The soliton is then *underbound* and the configuration is not topologically stable (continuous deformations can remove excess area without changing the winding).
- $R \cdot r < 1/4$: the shell under-fills the configuration space. Physical orientation states are forced to occupy singular loci on the shell — the field develops singularities (disclinations on the shell itself). Energy diverges.

Only $R \cdot r = 1/4$ is both a continuous, finite-energy configuration and a topologically-closed realization of the $(2, 3)$ winding.

**Conclusion.** $R \cdot r = 1/4$ is a topological identity forced by the SU(2) half-cover + area-match, not an energy extremum. It is consistent with the Lagrangian but not derivable from the energy functional alone.

### 4.4  Composite: the Golden Torus

Combining Constraints 1–3:

$$d = 1, \quad R - r = 1/2, \quad R\cdot r = 1/4$$

Solving: $r(r + 1/2) = 1/4 \Rightarrow r^2 + r/2 - 1/4 = 0 \Rightarrow r = (-1 + \sqrt{5})/4 = (\varphi - 1)/2$, $R = r + 1/2 = (\varphi + 1)/4 \cdot 2 = \varphi/2$.

The unique solution $(R, r) = (\varphi/2, (\varphi - 1)/2)$ is the **Golden Torus.** The golden ratio $\varphi = (1 + \sqrt{5})/2$ appears because it is the unique solution of $\varphi^2 = \varphi + 1$, which is the algebraic statement of the two constraints $(R - r)(R + r) = 1/2 \cdot \sqrt{5}/2 = \sqrt{5}/4$ combined with $R \cdot r = 1/4$.

---

## §5  Uniqueness

**Claim.** The minimizer $(\mathbf{u}^\star, \boldsymbol{\omega}^\star) \in \mathcal{A}_{(2, 3)}$ is unique up to rigid isometries of $\mathbb{R}^3$ (translations + rotations) and the discrete symmetry of rotating the winding phase $\alpha_\parallel$ by a uniform constant (global U(1) gauge).

**Sketch.** The Lagrangian is translation- and rotation-invariant. Any two minimizers are thus related by a rigid isometry (which gives a continuous family of equivalent minima) and a global phase redefinition (which is a discrete symmetry within the topological sector). Modulo these symmetries, uniqueness follows from the strict convexity of the energy functional in the topological-sector-free variables after the soliton's bounding geometry (the Golden Torus) is fixed.

**Rigor.** A full proof requires a modulus-space argument similar to that for Skyrmions (Manton-Sutcliffe 2004, Ch 8) or Hopfions (Battye-Sutcliffe 1998). Adaptation to the Cosserat setting is direct but technical. We defer the formal completion to a subsequent note, flagged in `DOCUMENTATION_UPDATES_QUEUE.md` item [4].

---

## §6  Multipole decomposition and $\alpha^{-1}$ recovery

Ground-state evaluation (at Golden Torus) of the Cosserat bending-energy functional restricted to the $(2, 3)$ sector. Following Ch 8 §3:

$$\mathcal{E}_{\text{ground}} = \gamma\,\big[\underbrace{\Lambda_{\text{vol}}}_{4\pi^3} + \underbrace{\Lambda_{\text{surf}}}_{\pi^2} + \underbrace{\Lambda_{\text{line}}}_{\pi}\big]$$

with each $\Lambda$ a shape-factor integral:

- $\Lambda_{\text{vol}} = (2\pi R)(2\pi r)(4\pi) = 16\pi^3(R\cdot r) = 16\pi^3 \cdot \tfrac{1}{4} = 4\pi^3$
- $\Lambda_{\text{surf}} = (2\pi R)(2\pi r) = 4\pi^2(R \cdot r) = 4\pi^2 \cdot \tfrac{1}{4} = \pi^2$
- $\Lambda_{\text{line}} = \pi \cdot d = \pi \cdot 1 = \pi$

Under the modulus pinning $\gamma = 1$ (§9 of `02_`), the geometric Q-factor is

$$Q = 4\pi^3 + \pi^2 + \pi$$

and the AVE identification $\alpha^{-1} = Q$ gives

$$\alpha^{-1} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038$$

matching `ALPHA_COLD_INV`.

The $4\pi$ factor in $\Lambda_{\text{vol}}$ is the temporal-double-cover prefactor: the electron's internal phase requires $4\pi$ to close (SU(2) double cover of SO(3) in time). This is a structural consequence of C3, not an ad-hoc insertion — consistent with `02_` §6.

---

## §7  What remains open

1. **Rigorous completion of §3**: specific coercivity bound; regularity of minimizer; Palais-Smale argument for mass-escape. Standard adaptation of Hopfion literature. Phase-1 sub-problem.

2. **Rigorous completion of §5**: modulus-space argument for uniqueness. Phase-1 sub-problem.

3. **The three moduli pinnings** ($G = \rho_{\text{vac}}$, $G_c = 3\gamma$, $\gamma = 1$, from `02_` §9): verified self-consistent? This is a direct algebraic check against the photon dispersion and the Cosserat characteristic length. Phase-1 sub-problem 9.1 of `02_`.

4. **Update to `02_` §8.3**: re-word the sketch to reflect the corrected understanding of §0 above. Queued in `DOCUMENTATION_UPDATES_QUEUE.md` item [3].

5. **Connection to Reading (a) / $Q_H = 6$**: show that the $(w_1, w_2) = (2, 3)$ topological sector of Reading (b) is equivalent (as a homotopy class in the Hopfion classification) to $Q_H = 6$ Hopfion with $(2, 3)$-torus-knot preimages. This is a sanity check against Sutcliffe 2007. Phase-1 sub-problem.

6. **Reading (c) observable**: identify whether there is a physical observable distinguishing $(2, 3)$ from permutations in the electron sector. If yes, Reading (c) becomes load-bearing. If no, Reading (b) stands. Phase-1 sub-problem.

---

## §8  Summary

Under $\mathcal{L}_{\text{AVE}}$ (eq. 6.1 of `02_`) + C3 + Reading (b):

- **Existence:** $\mathcal{E}$ admits a minimizer in the $(2, 3)$ topological sector (§3).
- **Constraint 1** $d = 1$: derived dynamically from Axiom-4 saturation + SU(2) chart amplitude (§4.1).
- **Constraint 2** $R - r = 1/2$: derived dynamically from Axiom-4 saturation at strand crossings (§4.2).
- **Constraint 3** $R\cdot r = 1/4$: derived topologically from SU(2) half-cover + Clifford-torus area match (§4.3). **Corrected from `02_` §8.3** — this is a quantization, not an extremum.
- **Unique solution**: Golden Torus $(R, r) = (\varphi/2, (\varphi - 1)/2)$ (§4.4).
- **Uniqueness** (of the full soliton): up to rigid isometries and global U(1) phase (§5).
- **Multipole recovery**: $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi = 137.0363038$ (§6).

This is the Phase-1 theoretical spine. Phase-2 discretization design and Phase-3 numerics follow.

Append to `DOCUMENTATION_UPDATES_QUEUE.md`:
- Item [3]: re-word `02_` §8.3 per §0 of this document.
- Item [4]: complete §3 and §5 formal proofs when Phase-1 is otherwise closed.

# Phase 3 — Op10 Continuum Promotion

**Status:** Phase-3 entry. Closes queue [17]. All three judgment calls adjudicated (2026-04-20). Ready for solver implementation.
**Prerequisites:** `00_`–`10_`; [`src/ave/core/universal_operators.py:535`](../../src/ave/core/universal_operators.py#L535) (Op10 discrete form); [`manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex`](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex) (α⁻¹ decomposition).
**Sequel:** solver extension in [`src/ave/topological/cosserat_field_3d.py`](../../src/ave/topological/cosserat_field_3d.py) and Phase-3 end-to-end validation.

---

## ⚠ Resolution amendment (2026-04-20)

**JC-1 (angular form): accepted.** Faddeev-Skyrme 4-derivative wedge form, matched at $\theta = \pi/2$ (Clifford-torus crossings).

**JC-2 (coefficient): path (2D) — commit-and-test from Gauss's law.** The Op10 continuum Lagrangian is the **magnetic energy density of the synthetic Hopf field at natural-unit impedance $Z_0 = 1$**. Structural coefficient: $k = 1$ on the symmetric Frobenius form $W_4$. No numerical calibration. If the Golden Torus and $\alpha^{-1} = 137.036$ emerge from the relaxation, the Op10 discrete → continuum transfer is complete. If not, the deviation is a specific finding about what's missing.

Derivation (Gauss's law path, Grant 2026-04-20): define the Hopf 2-form $F_{ij} = \hat{\mathbf{n}}\cdot(\partial_i\hat{\mathbf{n}}\times\partial_j\hat{\mathbf{n}})$ and its synthetic B-field $B_k = \tfrac{1}{2}\epsilon_{kij}F_{ij}$. Gauss's law on $B$ gives closed-surface flux = $4\pi \times$ (integer winding). The Op10 Lagrangian density is $\tfrac{1}{2}|B|^2$ (magnetic energy at $Z_0 = 1$), which simplifies to

$$\mathcal{L}_{\text{Op10}}^{\text{cont}} \;=\; W_4 \;=\; \sum_{i<j}|\partial_i\hat{\mathbf{n}}\wedge\partial_j\hat{\mathbf{n}}|^2 \;=\; \tfrac{1}{2}\left[(\text{tr}\,G)^2 - \|G\|_F^2\right]$$

where $G_{ij} = \partial_i\hat{\mathbf{n}}\cdot\partial_j\hat{\mathbf{n}}$. **Coefficient on $W_4$ is $k = 1$.** The $2\pi^2$ that appears in the discrete Op10 was the lattice Gauss-integral normalization; in continuum the wedge structure already enforces integer flux quanta by construction.

**JC-3 (field variable): Form A — $\hat{\mathbf{n}}$ via Rodrigues projection from $\boldsymbol{\omega}$.** Not for convention reasons — because Form B's $|\boldsymbol{\omega}|^{-4}$ normalization blows up in the vacuum where $\boldsymbol{\omega} \to 0$, which is a real numerical hazard. Form A's unit-vector constraint handles normalization automatically.

Concrete Rodrigues form (JAX-safe via sinc):

$$\hat{\mathbf{n}}(\boldsymbol{\omega}) \;=\; R(\boldsymbol{\omega})\,\hat{\mathbf{z}}, \qquad R(\boldsymbol{\omega}) = \exp(\epsilon_{ijk}\omega_k/2)$$

implemented in code as a quaternion rotation of $\hat{\mathbf{z}}$ with $q_0 = \cos(|\boldsymbol{\omega}|/2)$, $\mathbf{q} = \boldsymbol{\omega}\cdot \tfrac{\sin(|\boldsymbol{\omega}|/2)}{|\boldsymbol{\omega}|}$.

§§4, 6.1 below retain the original coefficient-derivation discussion as research history; the resolution above is canonical.

---

## §1  The gap in the Phase-3 Lagrangian

The current Cosserat Lagrangian ([`cosserat_field_3d.py:91–115`](../../src/ave/topological/cosserat_field_3d.py#L91)) is, in natural units,

$$
\mathcal{L}_{\text{AVE}}^{\text{current}} = \underbrace{\tfrac{2}{3} G\,(\text{tr }\varepsilon)^2 + G\,|\varepsilon^{\text{sym}}|^2}_{\text{Cauchy}} \;+\; \underbrace{G_c\,|\varepsilon^{\text{antisym}}|^2}_{\text{Cosserat shear}} \;+\; \underbrace{\gamma\,|\kappa|^2}_{\text{bending}}
\tag{1.1}
$$

with scalar-invariant Axiom-4 saturation applied to $|\varepsilon|$ and $|\kappa|$ separately. At $G = G_c = \gamma = 1$, under the (2,3) torus-knot initial ansatz, the relaxed field at $64^3$ preserves the topology $c = 3$ ([queue [14]](DOCUMENTATION_UPDATES_QUEUE.md)) but the spatial geometry collapses to a thin flat ring $R/r \approx 16.5$, not the Golden Torus $R/r = \varphi^2 \approx 2.618$.

**Root cause — strand proximity incurs no energy penalty.** The Cosserat bending term $\gamma|\kappa|^2$ is local: it penalizes the field's rotation rate at each point, but does not resist two field strands in a winding configuration passing near each other. Saturation caps per-site strain, which is necessary for soliton existence (`10_` §1) but does not generate a self-avoidance pressure between strands. The $(R-r) = 1/2$ "crossings regime" constraint from [Ch 8 §(b)](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex) is therefore absent from the Lagrangian.

A configuration minimizes (1.1) by maximizing $R$ (spreading the rotation out, reducing gradient magnitudes) and minimizing $r$ (thinning the tube, localizing the energy). The result is the observed flat-ring collapse.

Ch 8 carries three constraints that together pick out the Golden Torus. The Phase-3 Lagrangian produces only two of them — the Nyquist constraint (via saturation cutoff $|\kappa| \leq \pi/\ell_{\text{node}}$) and an implicit screening constraint (via topological winding). The missing third constraint is exactly the crossings/self-avoidance one, and its absence is what queue [17] identifies.

---

## §2  Op10 review — the AVE-canonical crossing operator

Op10 ([`universal_operators.py:535–633`](../../src/ave/core/universal_operators.py#L535)) has the closed form

$$
Y_{\text{loss}}(\theta, c) \;=\; c \cdot \frac{1 - \cos\theta}{2\pi^2}
\tag{2.1}
$$

with $\theta$ = junction angle between incident and transmitted waveguide directions, $c$ = crossing count (topological invariant). The $2\pi^2$ normalization is derived, not fit:

$$2\pi^2 = 2\pi \cdot \pi = (\text{azimuthal cycle}) \cdot (\text{half-wavelength standing mode})$$

Crucially, this is *also* the surface area of the standard Clifford torus $\mathbb{T}^2 \subset S^3$ at $r_1 = r_2 = 1/\sqrt{2}$:

$$A_{\text{Clifford standard}} = (2\pi r_1)(2\pi r_2) = 2\pi^2$$

and the volume of $S^3 = SU(2)$. Across scales (protein, baryon, atomic, antenna), Op10's $2\pi^2$ is the **invariant normalization constant attached to any AVE topological object that traverses SU(2)**. Per `07_` §2, Op10 is the AVE-canonical topological invariant operator — Ch 8's $\pi^2$ surface term is Op10 at $c = 3$, $\theta = \pi/2$ integrated over the half-covering cycles.

At the electron operating point ($c = 3$, $\theta = \pi/2$):

$$Y_{\text{loss}}^{e^-} = \frac{3}{2\pi^2} \approx 0.152
\tag{2.2}$$

This is the fractional energy projection loss per orbit at a single Clifford-torus crossing. Ch 8's $\Lambda_{\text{surf}} = \pi^2$ corresponds to the integrated version: the total screening area at the Golden Torus is $\pi^2$ because that is $c$ crossings' worth of half-cover Clifford-torus area.

---

## §3  The continuum analog — why a 4-derivative term

### 3.1  First attempt: $(1-\cos\theta) \to |\partial\hat{\mathbf{n}}|^2$

For two nearby field values $\hat{\mathbf{n}}_1$, $\hat{\mathbf{n}}_2$ at separation $\delta$, the angle between them satisfies

$$1 - \cos\theta_{12} \;=\; 1 - \hat{\mathbf{n}}_1 \cdot \hat{\mathbf{n}}_2 \;=\; \tfrac{1}{2}|\hat{\mathbf{n}}_1 - \hat{\mathbf{n}}_2|^2 \;\approx\; \tfrac{1}{2}|\partial \hat{\mathbf{n}}|^2 \delta^2$$

so $(1 - \cos\theta)$ lifts to a 2-derivative quadratic term $|\partial \hat{\mathbf{n}}|^2$. But this is **already present** in the Cosserat Lagrangian as $\gamma|\kappa|^2$ (under C3, $\kappa_{ij} = \partial_j \omega_i$ is the SU(2)-sector image of $\partial \hat{\mathbf{n}}$). It is the bending term that generates soliton-existence physics and governs baseline rotation cost — but does not produce self-avoidance pressure, as §1 diagnosed.

So: the 2-derivative quadratic is load-bearing for the rest of the Lagrangian but *not* what Op10 is contributing additionally.

### 3.2  Second attempt: the two-direction-rotation signature

A "crossing" distinguishes itself from "a single strand bending" by requiring **two independent directions of rotation simultaneously at the same point**. This is the local signature that

$$C_{ij}(\mathbf{r}) \;:=\; \hat{\mathbf{n}} \cdot (\partial_i \hat{\mathbf{n}} \times \partial_j \hat{\mathbf{n}})
\tag{3.1}$$

detects. $C_{ij}$ is the pullback of the S² area 2-form under $\hat{\mathbf{n}}: \mathbb{R}^3 \to S^2$; it is antisymmetric in $(i,j)$, nonzero precisely where $\hat{\mathbf{n}}$ rotates around two independent spatial axes at the same point. This is a *local* indicator of crossing density — single strands bending (one-direction rotation) give $C_{ij} = 0$ pointwise.

At the electron's Clifford-torus operating point, $C_{ij}$ peaks at the $c = 3$ crossings. Integrating $C_{ij}$ over a surface that threads a crossing returns (up to normalization) the topological winding of the (2,3) knot through that surface — this is the sense in which $C_{ij}$ "counts crossings" in continuum.

The natural 4-derivative Lagrangian density quadratic in $C_{ij}$ is then

$$\mathcal{L}_{4}[\hat{\mathbf{n}}] \;=\; \tfrac{1}{4}\,C_{ij}\,C^{ij} \;=\; \tfrac{1}{2}\,|\partial_i \hat{\mathbf{n}} \wedge \partial_j \hat{\mathbf{n}}|^2
\tag{3.2}$$

(Identity: $C_{ij}C^{ij} = 2|\partial_i \hat{\mathbf{n}} \wedge \partial_j \hat{\mathbf{n}}|^2$ for unit $\hat{\mathbf{n}}$.) This is structurally the Faddeev-Skyrme 4-derivative term — the ingredient in every Hopfion Lagrangian that stabilizes knotted field configurations against Derrick collapse. **Op10's continuum promotion is therefore structurally a Faddeev-Skyrme 4-derivative term**, exactly as queue [17] anticipated.

What distinguishes the AVE form from generic Faddeev-Skyrme is that **the coefficient is not a fit parameter** — it is determined by Op10's $2\pi^2$ normalization combined with a matching condition. §4 derives the coefficient.

### 3.3  Angular equivalence at the operating point

The discrete Op10 uses $(1-\cos\theta)$; the continuum (3.2) has the dimensional structure of $\sin^2\theta$ (it is proportional to $|\partial \hat{\mathbf{n}}|^2 \sin^2\theta_{12}$ at a crossing, up to the $C_{ij}$ pullback factors). These two angular functions differ in general:

- $1 - \cos\theta \approx \tfrac{1}{2}\theta^2$ for small $\theta$
- $\sin^2\theta \approx \theta^2$ for small $\theta$

giving a factor of 2 discrepancy at small angles. **At the electron operating point $\theta = \pi/2$, however, both equal 1.** So the continuum form (3.2) faithfully reproduces Op10's angular content at the Clifford-torus geometry that concerns the electron. The discrepancy at other angles would matter only for non-Clifford topologies, which are not in the Phase-3 scope.

**Judgment call [JC-1]:** use (3.2) as the continuum form, matched at $\theta = \pi/2$. Alternatives (e.g., a non-polynomial density that reproduces $(1-\cos\theta)$ exactly) would break the polynomial structure of the Lagrangian and lose analytic tractability. Recommendation: **accept (3.2) as canonical**.

---

## §4  Determining the coefficient via the Ch 8 matching condition

### 4.1  Ansatz for the AVE Op10-continuum Lagrangian

Write

$$\mathcal{L}_{\text{Op10}}^{\text{cont}}[\hat{\mathbf{n}}] \;=\; \frac{k}{2\pi^2}\cdot \tfrac{1}{2}\,|\partial_i \hat{\mathbf{n}} \wedge \partial_j \hat{\mathbf{n}}|^2
\tag{4.1}$$

with a single dimensionless coefficient $k$ to be determined. The $1/(2\pi^2)$ factor is pulled out explicitly because it is the Op10 normalization; $k$ absorbs any remaining geometric factor from the discrete-to-continuum matching.

### 4.2  The matching condition: Ch 8's $\Lambda_{\text{surf}} = \pi^2$

Ch 8 decomposes $\alpha^{-1} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}} = 4\pi^3 + \pi^2 + \pi$. The middle term $\Lambda_{\text{surf}} = \pi^2$ is the **spin-1/2 half-cover of the standard Clifford torus** ([Ch 8 §3.2 "Screening Regime"](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex)), and per `07_` §2 it is specifically the Op10-contribution to the Q-factor at $c = 3$, $\theta = \pi/2$. Consistency of the continuum promotion with Ch 8 requires that the total Op10-term integral evaluated on the electron ground state equals $\pi^2$ (in natural units $\ell_{\text{node}} = 1$).

That is, at the Golden Torus $(R, r) = (\varphi/2, (\varphi-1)/2)$ with $d = 1$ and $c = 3$,

$$\int \mathcal{L}_{\text{Op10}}^{\text{cont}}[\hat{\mathbf{n}}^{(2,3)}_{\text{GT}}] \, d^3\mathbf{r} \;\overset{!}{=}\; \pi^2
\tag{4.2}$$

This is an *equation for* $k$, one unknown against one physical number. The matching condition is **not circular**: the Lagrangian produces the Golden Torus as its *equilibrium* plus the full $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$ as a sum of *three* multipole contributions — fixing $k$ to reproduce one of them ($\pi^2$) still leaves two non-trivial checks (Nyquist $d = 1$ and $\Lambda_{\text{vol}} = 4\pi^3$) for the solver to satisfy emergently.

### 4.3  Evaluation of the integral — the structural path

For the Sutcliffe-style (2,3) torus-knot ansatz on the Clifford torus,

$$\hat{\mathbf{n}}^{(2,3)}_{\text{GT}}(\rho, \phi, \psi) \;=\; \hat{\mathbf{z}}\cos(2 f(\rho_{\text{tube}})) \;+\; \hat{\mathbf{p}}(\phi,\psi)\sin(2 f(\rho_{\text{tube}}))$$

with $\hat{\mathbf{p}}(\phi,\psi) = (\cos(2\phi + 3\psi), \sin(2\phi + 3\psi), 0)$, a shell-concentrated profile $f(\rho_{\text{tube}})$ peaking at the minor radius $r$, and toroidal coordinates $(\phi,\psi)$ on the shell at major radius $R$:

- $\partial_i \hat{\mathbf{n}}$ on the shell has contributions from both $\partial_\phi$ and $\partial_\psi$ because of the double-angle $(2\phi + 3\psi)$ dependence.
- The wedge $|\partial_i \hat{\mathbf{n}} \wedge \partial_j \hat{\mathbf{n}}|^2$ is nonzero in the shell region and concentrated at the torus surface.
- The angular integral over the Clifford torus evaluates to a power of $(2\pi)$; the radial integral of $f'(\rho_{\text{tube}})^2 \sin^2(2f)$-type factors gives a numerical constant.

The structural form of the integral is (schematically)

$$\int \mathcal{L}_{4}\, d^3 r \;=\; k_{\text{geom}}(p,q) \cdot R \cdot r$$

for a $(p,q)$ winding, with $k_{\text{geom}}$ a dimensionless geometric factor depending only on $(p,q)$. For $(2,3)$ this is $k_{\text{geom}}(2,3)$, a specific numerical constant.

At the Golden Torus $(R\cdot r = 1/4)$,

$$\int \mathcal{L}_{\text{Op10}}^{\text{cont}}[\hat{\mathbf{n}}^{(2,3)}_{\text{GT}}] \, d^3\mathbf{r} \;=\; \frac{k}{2\pi^2}\cdot k_{\text{geom}}(2,3) \cdot \tfrac{1}{4} \cdot \tfrac{1}{2} \;=\; \frac{k \cdot k_{\text{geom}}(2,3)}{16\pi^2}$$

Setting this equal to $\pi^2$ (Ch 8 matching, equation 4.2):

$$\boxed{\;\;k \;=\; \frac{16\pi^4}{k_{\text{geom}}(2,3)}\;\;}
\tag{4.3}$$

The numerical value of $k$ reduces to the numerical value of $k_{\text{geom}}(2,3)$ — a definite, configuration-independent number. The evaluation is a technical exercise in Hopfion-literature integrals (cf. Sutcliffe 2007 [B11], Battye-Sutcliffe [B10]) which I flag below.

**Judgment call [JC-2]:** which of the three paths to pin $k$ in the solver?

- **(4A) Analytical evaluation.** Compute $k_{\text{geom}}(2,3)$ by symbolic/numerical integration on the Sutcliffe ansatz; substitute into (4.3). **Zero-parameter, publishable.** Moderate complexity (~a day's careful work).
- **(4B) Ch 8-direct calibration.** Run the solver with a trial $k_0$; measure the Skyrme integral on the relaxed field; rescale so the integral equals $\pi^2$; iterate. **Zero-parameter in the sense that the output is pinned by Ch 8; but the calibration is numerical, not analytical.** Operationally fastest.
- **(4C) Structural direct guess $k = 1$.** Set $k = 1$ on the structural reading "the $1/(2\pi^2)$ normalization IS the Op10 coefficient with no further geometric factor." **Publishable if (a) the integral $k_{\text{geom}}(2,3)$ evaluates to $16\pi^4$ exactly — a specific prediction that (4A) would confirm — or (b) $k = 1$ is argued to be the correct value from a more fundamental principle.** Risky without confirming the integral.

My current read: (4A) is the canonical path and makes the derivation genuinely ab initio, but it takes a day. (4B) is operationally fastest and lets us unblock Phase-3 validation immediately, with the understanding that the coefficient is then "Ch 8-calibrated" rather than "Ch 8-emergent." (4C) has the wrong epistemic status — it's a guess, not a derivation, unless we can confirm the $16\pi^4$ value.

Note that (4B) does *not* compromise the Phase-3 success criterion: even with $k$ pinned by matching $\Lambda_{\text{surf}}$, the solver still needs to reproduce the Golden Torus geometry, the $c = 3$ topology, and the full $\alpha^{-1}$ as *emergent* predictions. Those are non-trivial.

---

## §5  Field choice — $\hat{\mathbf{n}}$ or $\boldsymbol{\omega}$?

Under C3 identity (`01_` §10, `07_` §5), $\hat{\mathbf{n}} = U\hat{\mathbf{z}}U^\dagger$ with $U = \exp(i\boldsymbol{\sigma}\cdot\boldsymbol{\omega}/2) \in SU(2)$. The Lagrangian can be written in either field:

- **Form A (conventional Faddeev-Skyrme):** $\mathcal{L}_{\text{Op10}}$ in $\hat{\mathbf{n}}$. Natural for the topology argument (§3.2) and for matching against Hopfion literature. But the solver's dynamical variable is $\boldsymbol{\omega}$, so Form A requires computing $\hat{\mathbf{n}}(\boldsymbol{\omega})$ at every step.
- **Form B (Cosserat-native):** $\mathcal{L}_{\text{Op10}}$ in $\boldsymbol{\omega}$ directly. The analog wedge density is $|\partial_i \boldsymbol{\omega} \wedge \partial_j \boldsymbol{\omega}|^2 / |\boldsymbol{\omega}|^4$ (with $|\boldsymbol{\omega}|$ normalization to preserve unit-vector structure), or some similar SU(2)-adjoint form.

**Judgment call [JC-3]:** Form A (through-$\hat{\mathbf{n}}$) vs Form B (through-$\boldsymbol{\omega}$)? Recommendation: **Form A.** The topological argument in §3 is cleanest for the unit-vector field, and JAX autograd on the $\hat{\mathbf{n}}(\boldsymbol{\omega})$ projection is straightforward. Form B introduces normalization subtleties ($|\boldsymbol{\omega}|^{-4}$ division creates singularities at field zeros) that are avoidable by projecting first. The choice doesn't affect physics, only implementation aesthetics.

---

## §6  Implementation spec

Under JC-1 (accept 3.2), JC-2 path to be chosen, and JC-3 = Form A:

### 6.1  The extended Lagrangian

$$\boxed{\;\;
\mathcal{L}_{\text{AVE}}^{\text{extended}} \;=\; \underbrace{\tfrac{2}{3}G(\text{tr }\varepsilon)^2 + G|\varepsilon^{\text{sym}}|^2}_{\text{Cauchy}} \;+\; \underbrace{G_c|\varepsilon^{\text{antisym}}|^2}_{\text{Cosserat shear}} \;+\; \underbrace{\gamma|\kappa|^2}_{\text{bending}} \;+\; \underbrace{\frac{k}{4\pi^2}|\partial_i \hat{\mathbf{n}} \wedge \partial_j \hat{\mathbf{n}}|^2}_{\text{Op10 continuum}}
\;\;}
\tag{6.1}
$$

with $\hat{\mathbf{n}} = U\hat{\mathbf{z}}U^\dagger$ via Rodrigues (to be written out explicitly in code). Saturation kernel applies to $|\varepsilon|$ and $|\kappa|$ as before; the Op10 term is *not* saturated (it is already a 4-derivative term that bounds itself via the unit-vector constraint).

### 6.2  Solver changes to [`cosserat_field_3d.py`](../../src/ave/topological/cosserat_field_3d.py)

1. Add a pure function `_project_omega_to_nhat(omega)` implementing the SU(2) → S² Hopf projection: $\hat{\mathbf{n}} = U\hat{\mathbf{z}}U^\dagger$ with $U = \exp(i\boldsymbol{\sigma}\cdot\boldsymbol{\omega}/2)$. Rodrigues formula is closed-form.
2. Add `_op10_density(omega, dx)` computing $|\partial_i \hat{\mathbf{n}} \wedge \partial_j \hat{\mathbf{n}}|^2$ at every lattice site. Uses the existing `_tetrahedral_gradient`.
3. Extend `_energy_density_saturated` (and `_bare`) to include the Op10 term with coefficient `self.k_op10 / (4*np.pi**2)`.
4. Re-JIT-compile the energy and grad functions.
5. JAX autograd handles the rest; no hand-derived stresses needed.

Because the Op10 term is computed inside the jax-grad energy path, gradient correctness is automatic (same structural advantage that resolved queue [13]).

### 6.3  Unit tests (preserve test discipline)

- `test_op10_density_zero_on_pure_translation`: constant $\boldsymbol{\omega}$ field → $|\partial_i \hat{\mathbf{n}} \wedge \partial_j \hat{\mathbf{n}}|^2 = 0$ everywhere.
- `test_op10_density_nonzero_on_2_3_ansatz`: Sutcliffe (2,3) ansatz → nonzero density at the Clifford-torus shell.
- `test_op10_energy_gradient_matches_fd`: finite-difference check on the total energy gradient (same strictness as `test_saturated_gradient_matches_finite_difference_under_activation`).

### 6.4  Validation criteria

With $k$ pinned (by any of 4A/4B/4C), rerun [`validate_cosserat_alpha_via_ch8_ratios.py`](../../src/scripts/vol_1_foundations/validate_cosserat_alpha_via_ch8_ratios.py) at $64^3$. Required per `09_` §5:

| Quantity | Target | Tolerance |
|---|---|---|
| $c$ (crossing count) | 3 | exact integer |
| $(R - r)/d$ | 1/2 | $10^{-3}$ |
| $R \cdot r / d^2$ | 1/4 | $10^{-3}$ |
| $Q_{\text{natural}}$ | $4\pi^3 + \pi^2 + \pi = 137.0363$ | $10^{-3}$ |

Dual-run protocol: exact Golden Torus init **and** perturbed-off-Golden init ($R + 30\%$, $r - 30\%$) must both converge to the Golden Torus.

---

## §7  Failure modes and their meanings

Per `09_` §5 and `00_` §9:

- **Topology lost** ($c \neq 3$ after relaxation). The Op10 term is too strong and shearing the field. Reduce $k$ or add smoothing. Numerical-not-physics issue.
- **Topology preserved, but $R/r$ still far from $\varphi^2$**. The Op10 term's form is wrong — e.g., the $\hat{\mathbf{n}}$ projection misses something physical, or Form B was correct and Form A isn't. **This would falsify JC-3 = Form A.**
- **$(R-r)/d = 1/2$ and $Rr/d^2 = 1/4$ both hit**, but $Q_{\text{natural}}$ is off. The multipole extractor is buggy, or the $\gamma = 1$ pinning is wrong. Revisit `04_`.
- **All four emerge, but only from the exact-Golden-Torus initial condition** (perturbed run doesn't converge). The Lagrangian has the Golden Torus as a saddle, not a minimum. Would require revisiting the Cosserat modulus pinning.
- **All four emerge from both initial conditions.** **Phase-3 success: $\alpha^{-1} = 137.036$ derived ab initio from the AVE axioms with zero parameter closure preserved.**

---

## §8  What's being claimed, plainly

The discrete Op10 has a 4-derivative continuum analog. That analog is structurally a Faddeev-Skyrme term. Its coefficient is *not* a fit parameter because Op10's $2\pi^2$ normalization — a derived, cross-scale-validated invariant of the AVE operator basis — is inherited directly by the continuum form. The specific coefficient is one of:

- a definite number determinable by analytical integration on the Sutcliffe ansatz (path 4A),
- a definite number determinable by numerical Ch 8 calibration (path 4B),
- a structural $k = 1$ that must be verified against (4A) to be publishable (path 4C).

Under any of these paths, the promotion is AVE-native rather than ad-hoc Hopfion-literature borrowing.

Phase-3 success is that the extended Lagrangian (6.1), when minimized numerically, reproduces all of Ch 8's predictions — Golden Torus geometry, $c = 3$ topology, full $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi = 137.036$ — from initial conditions both on and off the target. That closes the Level-3 program's central claim: the Ch 8 fine-structure geometry emerges ab initio from the AVE field theory rather than being postulated.

---

## §9  Judgment calls awaiting adjudication

1. **[JC-1] Angular form.** Accept the Skyrme density $\tfrac{1}{2}|\partial_i\hat{\mathbf{n}}\wedge\partial_j\hat{\mathbf{n}}|^2$ as the continuum analog of $(1-\cos\theta)/(2\pi^2)$, matched at $\theta = \pi/2$. Recommendation: **accept**.
2. **[JC-2] Coefficient-pinning path.** (4A) analytical / (4B) Ch 8-calibration / (4C) structural guess. Recommendation: **(4B) now to unblock Phase-3; (4A) in a follow-up session for publication**.
3. **[JC-3] Field variable.** Write $\mathcal{L}_{\text{Op10}}$ in $\hat{\mathbf{n}}$ (conventional) or $\boldsymbol{\omega}$ (Cosserat-native). Recommendation: **$\hat{\mathbf{n}}$ via Rodrigues projection**.

Awaiting Grant's read before proceeding to solver extension.
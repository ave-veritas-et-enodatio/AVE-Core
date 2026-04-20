# L3 Electron Soliton — Phase 0 Scoping Document

**Status:** CANONICAL for AVE field-theory formalism (§2, §4).
**Branch:** `research/l3-electron-soliton`.
**Date opened:** 2026-04-19.
**Rigor target:** Publication-grade (full citations, formal existence/uniqueness posture, no hand-waving where hand-waving is dishonest).

This document opens the Level-3 research program: derive the AVE electron *ab initio* as a localized topological soliton of the Cosserat-micropolar K4 substrate, and recover the zero-parameter Golden-Torus prediction $\alpha^{-1} = 4\pi^{3} + \pi^{2} + \pi = 137.0363038$ without input from the measured value.

Phase 0 is prose-only. The formal Lagrangian, existence proofs, and numerical implementation are Phase-1+ deliverables.

---

## §1  Problem statement

Let $\mathcal{M}_{K_4}$ denote the three-dimensional discrete diamond (K4) lattice substrate of Axiom 1, equipped with node pitch $\ell_{\text{node}}$. Let $\boldsymbol{\omega}(\mathbf{r}, t)$ and $\mathbf{u}(\mathbf{r}, t)$ denote, respectively, the Cosserat microrotation and translational-displacement fields defined on $\mathcal{M}_{K_4}$.

The research question has three parts:

1. **Formalism.** Write down the unified Cosserat-micropolar Lagrangian density $\mathcal{L}_{\text{AVE}}(\mathbf{u}, \boldsymbol{\omega}, \nabla\mathbf{u}, \nabla\boldsymbol{\omega})$, including the Axiom 4 gradient-saturation kernel $S(\cdot)$ that enforces the Nyquist cutoff $|\nabla\boldsymbol{\omega}| \leq \pi / \ell_{\text{node}}$.

2. **Existence.** Show that the Euler-Lagrange equations derived from $\mathcal{L}_{\text{AVE}}$ admit a localized, finite-energy, topologically non-trivial ground-state solution with spatial flux-tube topology of an unknot $0_1$ and phase-winding $(2,3)$ on the toroidal-shell neighborhood. Call this solution the **electron soliton**.

3. **Uniqueness & recovery.** Show that this ground state is unique up to rigid isometries and minimizes the Cosserat free-energy functional at radii $(R, r) = (\varphi/2, (\varphi - 1)/2)$ — the Golden Torus of Vol 1 Ch 8 — yielding $\alpha^{-1} = 4\pi^{3} + \pi^{2} + \pi$ as the holomorphic multipole decomposition's Q-factor *at the solved geometry*, not as a geometric postulate.

**Success criterion.** An end-to-end derivation chain with no step relying on input of the measured $\alpha$, such that the Level-3 program reproduces — without fitting — the Ch 8 result from strictly more fundamental premises. Failure to converge constitutes a falsification pathway, not a setback to paper over.

**Out of scope (Phase 0).** The thermal-running correction $\delta_{\text{strain}} = 2.225\times 10^{-6}$ is *not* addressed here; its first-principles derivation (T_CMB + Cosserat bulk modulus + K4 phonon DoS) is tracked as a separate work-stream (see §9).

---

## §2  Why Cosserat — canonical evidence and commitment

**§2 is CANONICAL.** This section declares Cosserat micropolar field theory as the canonical formalism for AVE substrate dynamics and establishes the corpus-evidence base on which Phase 1 builds.

### 2.1  Corpus commitment (existing)

The AVE-Core manuscript and engine already commit to a Cosserat vacuum at structural, not decorative, load-bearing. The primary citations are:

- **[Vol 1 Ch 2, `02_macroscopic_moduli.tex`](../../manuscript/vol_1_foundations/chapters/02_macroscopic_moduli.tex)** establishes the *necessity* of Cosserat structure:

  > *"The vacuum must be a Micropolar (Cosserat) continuum to support transverse EM waves without the Implosion Paradox ($K < 0$)."*

  A pure Cauchy continuum satisfying the MacCullagh transverse-wave condition yields a negative bulk modulus $K = -\mu/3$, i.e., thermodynamic runaway collapse. Cosserat structure — independent microrotation DOFs per material point — resolves this.

- **[Vol 1 Ch 4, `04_continuum_electrodynamics.tex:16-26`](../../manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex)** establishes the *identity* linking K4 topology to Cosserat equilibrium:

  > *"The K4 graph topology (Axiom 1) enforces $K = 2G$ (trace-reversal identity), **which is the Cosserat equilibrium condition** for a network with 3 translational + 3 rotational modes per node, cross-coupled through the electromagnetic constitutive relations."*

- **[Vol 2 Ch 3, `03_neutrino_sector.tex`](../../manuscript/vol_2_subatomic/chapters/03_neutrino_sector.tex)** locks in the *connectivity identity*:

  > *"The screening threshold $\Delta c_{\text{crit}} = 3$ is simultaneously the K4 lattice connectivity, the trefoil crossing number, and the number of Cosserat sectors. These three facts are structurally identical."*

- **[Vol 2 Ch 6, `06_electroweak_and_higgs.tex`](../../manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex)** derives the lepton spectrum from three Cosserat sectors: translation (electron), rotation-torsion (muon), curvature-twist (tau).

- **[backmatter/02_full_derivation_chain.tex](../../manuscript/backmatter/02_full_derivation_chain.tex)** states Axiom 1 as the "Trace-Reversed Chiral LC Network (micropolar continuum)."

- **[backmatter/03_geometric_inevitability.tex](../../manuscript/backmatter/03_geometric_inevitability.tex)** argues the geometric uniqueness of K4 + $\nu_{\text{vac}} = 2/7$ as the operating point where $K = 2G$ and the fine-structure closure holds.

- **[src/ave/topological/cosserat.py](../../src/ave/topological/cosserat.py)** implements W/Z mass derivation and the three-generation lepton spectrum using Cosserat sector arithmetic (661 lines).

- **[manuscript/predictions.yaml](../../manuscript/predictions.yaml)** carries the entry $\nu_{\text{vac}} = 2/7$ attributed to "Axiom 1 (K4 lattice geometry) and Axiom 2 (Cosserat TKI); both are load-bearing."

Forty-nine files in the corpus reference Cosserat. The commitment is not rhetorical; it is the framework.

### 2.2  Canonical declaration

Accordingly, this document canonizes the following position for all subsequent AVE field-theory work:

> **The AVE vacuum substrate is a Cosserat (micropolar) continuum, discretized on the K4 diamond graph, with Axiom 4 gradient-saturation enforcing the Nyquist cutoff. All field-theoretic formalisms used in the framework — including the Faddeev-Skyrme σ-model used in [src/ave/topological/faddeev_skyrme.py](../../src/ave/topological/faddeev_skyrme.py) — must be interpretable as sectoral projections of the Cosserat field. Pure Skyrme, pure O(3) σ-model, or free-standing Faddeev-Niemi Hopfion formulations are not native to AVE and must not be treated as independent formalisms.**

This is the statement against which Phase 1 (§5) must be built.

---

## §3  Cosserat primer (self-contained)

*Intended audience: readers with standard EE / applied-physics background, no prior micropolar-elasticity exposure.*

### 3.1  Why Cosserat exists

Cauchy continuum mechanics — the standard framework for elasticity — assigns each material point a single vector-valued displacement $\mathbf{u}(\mathbf{r})$. Strain is the symmetric part of $\nabla\mathbf{u}$; stress is a symmetric rank-2 tensor; moduli are bulk $K$ and shear $G$. The antisymmetric part of $\nabla\mathbf{u}$ is interpreted as a rigid rotation and carries no elastic energy.

Cauchy-continuum physics cannot support every class of experimentally observed phenomenon. In particular, media composed of microstructured elements — granular solids, bone, liquid crystals, polymer networks — exhibit a local torque stiffness that Cauchy elasticity cannot describe. The Cosserat brothers (1909) generalized the framework by assigning each material point *two* independent field variables:

- $\mathbf{u}(\mathbf{r})$ — translational displacement (three components)
- $\boldsymbol{\omega}(\mathbf{r})$ — **microrotation**, an independent angular-orientation field (three components)

Six DOFs per point instead of three. "Independent" here means $\boldsymbol{\omega}$ is not constrained to equal $\tfrac{1}{2}\nabla \times \mathbf{u}$ (the macroscopic rotation rate); it evolves by its own equation of motion.

### 3.2  Cosserat kinematics

The kinematic quantities are:

- **Strain tensor** (non-symmetric in Cosserat):
  $$\varepsilon_{ij} = \partial_j u_i - \epsilon_{ijk}\omega_k$$
- **Curvature-twist tensor** (new, unique to Cosserat):
  $$\kappa_{ij} = \partial_j \omega_i$$

The strain $\varepsilon$ is a non-symmetric rank-2 tensor; its antisymmetric part measures the difference between macroscopic rotation $\tfrac{1}{2}\nabla\times\mathbf{u}$ and microrotation $\boldsymbol{\omega}$. The curvature $\kappa$ is a new rank-2 tensor that has no Cauchy analogue; it is the gradient of microrotation and captures how the internal orientation field twists and bends across space.

### 3.3  Cosserat constitutive relations

Energy density in a linear, isotropic Cosserat solid reads:

$$W(\varepsilon, \kappa) = \tfrac{1}{2}(K - \tfrac{2}{3}G)\,(\mathrm{tr}\,\varepsilon)^{2} + G\,\varepsilon_{(ij)}\varepsilon_{(ij)} + G_{c}\,\varepsilon_{[ij]}\varepsilon_{[ij]} + \tfrac{1}{2}\gamma_{c}\,\kappa_{(ij)}\kappa_{(ij)} + \tfrac{1}{2}\beta_{c}\,(\mathrm{tr}\,\kappa)^{2} + \tfrac{1}{2}\gamma'_{c}\,\kappa_{[ij]}\kappa_{[ij]}$$

where $(ij)$ and $[ij]$ denote symmetric and antisymmetric parts, and:

- $K$ — bulk modulus (Cauchy)
- $G$ — ordinary shear modulus (Cauchy)
- $G_c$ — micropolar ("Cosserat") shear modulus: resistance to $\boldsymbol{\omega} \neq \tfrac{1}{2}\nabla\times\mathbf{u}$
- $\gamma_c, \beta_c, \gamma'_c$ — micropolar bending/torsion moduli: resistance to spatial variation of $\boldsymbol{\omega}$

In AVE the constraint $K = 2G$ (Ch 1 Axiom 1, Vol 1 Ch 4) reduces the independent translational moduli to one. The $\gamma_c$ modulus enters the neutrino-sector derivation directly (Vol 2 Ch 3). The Poisson ratio $\nu_{\text{vac}} = 2/7$ is forced by $K = 2G$ under trace-reversal.

### 3.4  Cosserat wave modes

In an isotropic Cosserat medium, the dispersion relation admits four distinct wave modes:

1. **Longitudinal translational (P-wave).** Phase velocity $c_P = \sqrt{(K + \tfrac{4}{3}G)/\rho}$. Compressional.
2. **Transverse translational (S-wave).** Phase velocity $c_S = \sqrt{G/\rho}$. Shear.
3. **Transverse microrotational.** A propagating twist of $\boldsymbol{\omega}$ without translational component. In AVE, **this is identified with the photon.**
4. **Longitudinal microrotational.** A torsional wave carrying longitudinal angular momentum. In AVE, this is the load-bearing mode for the W/Z boson sector (Vol 2 Ch 6).

Mode 3 is the critical observation for AVE: a **photon is a transverse Cosserat shear wave** ([Vol 3 Ch 2, line 139](../../manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex)). It carries no rest mass because it excites only the $\boldsymbol{\omega}$ sector with $\mathbf{u} = 0$; the Cosserat substrate's transverse response is non-dispersive at leading order.

### 3.5  Topological defects in Cosserat media

Cosserat media natively support two classes of line defect that Cauchy media do not:

- **Dislocations** — defects in $\mathbf{u}$ (Burgers vector non-zero around the defect line)
- **Disclinations** — defects in $\boldsymbol{\omega}$ (Frank vector non-zero around the defect line)

The combined defect, a **dispiration**, has both Burgers and Frank content. In AVE, the electron is claimed to be a **closed dispiration loop** — a topological disclination ring with imposed phase winding on the toroidal shell around its flux-tube centerline.

The standard reference for continuum defect topology is Kleman & Friedel, *Rev. Mod. Phys.* **80**, 61–115 (2008). The standard reference for Cosserat-specific defect dynamics is Eringen, *Microcontinuum Field Theories I* (Springer, 1999), Ch 5.

---

## §4  The $\hat{\mathbf{n}} \leftrightarrow \boldsymbol{\omega}$ identity gap

**§4 is CANONICAL.** This section names the primary research gap whose closure is Phase 1's entry criterion.

The existing AVE 1D radial solver [src/ave/topological/faddeev_skyrme.py](../../src/ave/topological/faddeev_skyrme.py) works with a Faddeev-Skyrme orientation field $\hat{\mathbf{n}}(\mathbf{r}) \in S^{2}$, parameterized via a phase profile $\phi(r)$ with $\phi(0) = \pi$, $\phi(\infty) = 0$. The Cosserat substrate (§2) carries a microrotation field $\boldsymbol{\omega}(\mathbf{r}) \in \mathbb{R}^{3}$. Under the canonical commitment of §2, these are not two fields. They are two presentations of a single rotational sector.

**The formal identity mapping $\hat{\mathbf{n}}(\mathbf{r})$ to $\boldsymbol{\omega}(\mathbf{r})$ has not been written down anywhere in the AVE-Core corpus.** Until it is, the Ch 8 Golden-Torus derivation rests on a postulated geometry rather than an emergent one, and "the Faddeev-Skyrme electron on the Cosserat lattice" remains informal.

Candidate forms of the identity — to be adjudicated in Phase 1 — include:

1. **Unit-vector projection:**
   $$\hat{\mathbf{n}}(\mathbf{r}) = \boldsymbol{\omega}(\mathbf{r}) / |\boldsymbol{\omega}(\mathbf{r})|$$
   Simplest. Preserves direction, discards magnitude. Compatible with $\hat{\mathbf{n}} \in S^2$.

2. **Axis-angle with magnitude-as-phase:**
   $$\hat{\mathbf{n}}(\mathbf{r}) = \hat{\boldsymbol{\omega}}(\mathbf{r})\,\cos\theta(\mathbf{r}) + \ldots, \qquad \theta(\mathbf{r}) = |\boldsymbol{\omega}(\mathbf{r})|\,\ell_{\text{node}}$$
   The microrotation magnitude sets the phase; the direction sets the orientation.

3. **SU(2) embedding:**
   $\boldsymbol{\omega}(\mathbf{r})$ parameterizes a local SU(2) element $U(\mathbf{r}) = \exp(i\boldsymbol{\sigma}\cdot\boldsymbol{\omega}(\mathbf{r})/2)$, and $\hat{\mathbf{n}}$ is the standard O(3) image of $U$. Topologically cleanest for winding-number counting.

4. **Non-projective — $\boldsymbol{\omega}$ IS the primary field, $\hat{\mathbf{n}}$ is derived.** Under this posture the Faddeev-Skyrme formulation is a convenience, and the true dynamical variable is $\boldsymbol{\omega}$. This has the virtue of eliminating the "field" ambiguity entirely at the cost of requiring re-derivation of the existing FS energy functional in Cosserat variables.

The Phase-1 task is to (a) select among these on physical grounds, (b) prove that the chosen identity preserves the $(2,3)$ winding number under the imposed topological boundary condition, and (c) derive how the Cosserat couple modulus $\gamma_c$ relates to the Faddeev-Skyrme coupling $\kappa_{\text{FS}}$.

Without this identity resolved, Phase 1 cannot produce a Lagrangian at publication rigor. With it resolved, the Lagrangian follows mechanically.

---

## §5  Lagrangian skeleton (symbolic, prose-only)

Per the Phase-0 scope, the formal Lagrangian is a Phase-1 deliverable. The structure, however, is fixed by §2 and §4:

- A **translational kinetic** term $\tfrac{1}{2}\rho_{\text{vac}}\,\dot{\mathbf{u}}^2$ describing LC wave propagation on the K4 substrate (already implemented as [src/ave/core/k4_tlm.py](../../src/ave/core/k4_tlm.py) in the linear regime).
- A **rotational kinetic** term $\tfrac{1}{2}I_{\text{vac}}\,\dot{\boldsymbol{\omega}}^{2}$ describing microrotation dynamics. The microinertia $I_{\text{vac}}$ is a Cosserat parameter not yet pinned in the AVE corpus — Phase-1 task.
- A **translational elastic** term $W_{\varepsilon}(\mathbf{u}, \boldsymbol{\omega})$ with bulk and shear moduli $K = 2G$, including the non-symmetric-strain coupling to $\boldsymbol{\omega}$ via $\varepsilon_{ij} = \partial_j u_i - \epsilon_{ijk}\omega_k$.
- A **microrotation elastic** term $W_\kappa(\nabla\boldsymbol{\omega})$ with micropolar bending/torsion moduli $\gamma_c$, $\beta_c$, $\gamma'_c$. The $\gamma_c$ is the "Cosserat bending stiffness coupling" referenced in Vol 2 Ch 3.
- A **gradient-saturation kernel** $S(|\nabla\boldsymbol{\omega}|; \pi/\ell_{\text{node}})$ from Axiom 4, replacing $|\nabla\boldsymbol{\omega}|$ with $S(|\nabla\boldsymbol{\omega}|) \cdot |\nabla\boldsymbol{\omega}|$ in $W_\kappa$. This is the nonlinear "stabilization" term that prevents soliton collapse at finite radius.
- A **topological term** (possibly) enforcing the $(2,3)$ winding number as a constrained boundary condition, or introduced via a Chern-Simons-like addition. Phase-1 selection.

No explicit field-external coupling (no electromagnetic source term) — the electron soliton is an excitation of the Cosserat medium itself; there is no separate EM field to couple to in the Level-3 theory.

---

## §6  Discretization on K4 — design options

The K4 lattice is a 3-connected diamond graph. Standard FDTD codes assume cubic voxelization. Three discretization strategies:

- **(A) Direct discretization on the K4 graph.** Each K4 node carries $(\mathbf{u}, \boldsymbol{\omega})$. Gradient operators defined along the 4 bonds emanating from each node. Natural for Axiom 1; minimal interpolation loss; directly compatible with [src/ave/core/k4_tlm.py](../../src/ave/core/k4_tlm.py). Downside: non-standard FDTD; no off-the-shelf JAX/PyTorch support.

- **(B) Cubic voxelization with K4 as a coarse substrate.** Field lives on a regular $N^3$ cubic grid; K4 nodes impose boundary conditions at a subset of grid points; couplings reproduced via stencil design. Benefits: standard FDTD; JAX/PyTorch compatible; fast. Cost: $\ell_{\text{node}}$ becomes a multi-cell scale, reducing effective resolution; anisotropy artifacts possible.

- **(C) Hybrid.** Cubic voxelization for the FDTD inner loop, K4-aware stencils at topological-defect neighborhoods. Most complex; deferred unless (A) and (B) both fail convergence tests.

Phase 1 recommendation: **start with (A)** because it preserves the Cosserat-K4 identity rigorously; fall back to (B) if compute scaling demands it.

---

## §7  Phase-1 entry criteria

Phase 1 does not start until the following are delivered:

1. Adjudication of the $\hat{\mathbf{n}} \leftrightarrow \boldsymbol{\omega}$ identity among the four candidates of §4, with a written argument.
2. Resolution of the trefoil-vs-unknot convention in Ch 8 (pending — footnote to Vol 1 Ch 8 reconciling the spatial-unknot / phase-winding-trefoil distinction, so downstream readers do not re-encounter the confusion).
3. Bibliographic completeness: the references listed in §10 all located and skimmed; any gap in the Cosserat-defect or Hopfion numerical literature identified and queued.
4. Agreement between this scoping doc and Vol 1 Ch 4 on canonical Cosserat language. If Ch 4 needs any amendment to support the canonical declaration of §2, it is opened as a separate edit under this branch.

Exit criteria for Phase 1: the $\mathcal{L}_{\text{AVE}}$ Lagrangian written out explicitly, with every modulus named and its value or its pinning equation cited, and an existence argument for the winding-3 ground-state solution.

---

## §8  Compute budget

Target platform: **MacBook Pro M4, 32 GB unified memory.**

Realistic Phase-3 numerical grid sizes on this hardware:

- **$64^3$ voxel Cosserat field** (6 components per voxel, single precision): ~6 MB per field snapshot. Easily fits in memory; gradient-descent iteration at ~few seconds per step with NumPy + Numba. Appropriate for initial convergence experiments.
- **$96^3$ voxel Cosserat field**: ~20 MB per snapshot. Comfortable. Probably the working resolution for Phase-3 numerical validation.
- **$128^3$ voxel Cosserat field**: ~50 MB per snapshot. Fits, but the full iteration history (if retained for animation) balloons. Likely the upper bound on this hardware for the final publication-grade run.
- **$192^3$** and beyond: probably out of scope without cluster access.

Numerical-backend choices:

- **Primary:** NumPy + Numba (CPU, JIT-compiled). Reliable, debuggable, no Apple-Silicon tooling issues. First-pass development.
- **Secondary:** JAX with `jax.Array` on Metal backend (`jax_platform_name = 'metal'`). Offers GPU acceleration where Metal support is mature. Fall back to CPU for operations where Metal coverage is incomplete.
- **Tertiary:** PyTorch with MPS backend. Only if JAX-Metal hits a wall.

Compute budget is adequate for Phase 3 at the target grid sizes. No cluster rental necessary for the baseline derivation.

---

## §9  Kill criteria

**None preset.** Per the researcher's explicit posture, the program pivots or terminates when logical routes are demonstrably exhausted, not on schedule.

Tracked separately for honesty:

- Phase 1 failure modes: if no $\hat{\mathbf{n}} \leftrightarrow \boldsymbol{\omega}$ identity preserves the $(2,3)$ winding without introducing unphysical coupling terms, the canonical commitment of §2 may need refinement — possibly a richer tensorial structure than scalar projection.
- Phase 3 failure modes: if the numerical ground state fails to converge to the Golden Torus radii at $(R, r) = (\varphi/2, (\varphi - 1)/2)$ within numerical tolerance, the Ch 8 geometric postulates are falsified by the field theory and require revision.

Either failure is a finding, not a stop-work. Publication targets a *result*, whatever sign it carries.

**Separate work-stream (non-blocking for L3):** first-principles derivation of $\delta_{\text{strain}} = 2.225 \times 10^{-6}$ from $T_{\text{CMB}}$ + Cosserat bulk modulus + K4 phonon DoS. This is independent research; its outcome does not gate L3.

---

## §10  Literature landscape and citations

**Cosserat foundations.**

1. Cosserat, E. & Cosserat, F. *Théorie des corps déformables*. Hermann, Paris (1909). Original micropolar formulation.
2. Eringen, A. C. *Microcontinuum Field Theories I: Foundations and Solids*. Springer, New York (1999). Standard modern reference for Cosserat kinematics and constitutive relations (Ch 5 for defects).
3. Maugin, G. A. *Continuum Mechanics Through the Twentieth Century*. Springer (2013). Historical and conceptual overview, §4.
4. Nowacki, W. *Theory of Asymmetric Elasticity*. Pergamon Press (1986). Comprehensive wave-propagation treatment.

**Topological defects in continuum media.**

5. Kléman, M. & Friedel, J. *Disclinations, dislocations, and continuous defects: A reappraisal.* Rev. Mod. Phys. **80**, 61–115 (2008). Foundational.
6. Kleinert, H. *Gauge Fields in Condensed Matter*, vols. 1–2. World Scientific (1989). Dispiration defects and their gauge-theoretic interpretation.
7. Mermin, N. D. *The topological theory of defects in ordered media.* Rev. Mod. Phys. **51**, 591 (1979). Homotopy-group classification.

**Faddeev-Skyrme / Hopfion solitons.**

8. Faddeev, L. D. *Some comments on the many-dimensional solitons.* Lett. Math. Phys. **1**, 289 (1976). Introduces the knotted-soliton conjecture.
9. Faddeev, L. D. & Niemi, A. J. *Stable knot-like structures in classical field theory.* Nature **387**, 58–61 (1997). Hopfion Lagrangian foundations.
10. Battye, R. A. & Sutcliffe, P. M. *Knots as stable soliton solutions in a three-dimensional classical field theory.* Phys. Rev. Lett. **81**, 4798 (1998). First numerical Hopfions.
11. Sutcliffe, P. M. *Knots in the Skyrme-Faddeev model.* Proc. R. Soc. A **463**, 3001–3020 (2007). Torus-knot soliton spectrum for $(p,q)$ windings — directly relevant.
12. Hietarinta, J. & Salo, P. *Ground state in the Faddeev-Skyrme model.* Phys. Rev. D **62**, 081701 (2000). Numerical method for Hopfion relaxation on cubic grids.
13. Manton, N. & Sutcliffe, P. *Topological Solitons*. Cambridge Univ. Press (2004). Standard textbook; Ch 9 covers Hopfions in detail.

**Electron-as-soliton proposals (prior art).**

14. Rañada, A. F. *A topological theory of the electromagnetic field.* Lett. Math. Phys. **18**, 97–106 (1989). Hopfion electromagnetism.
15. Irvine, W. T. M. & Bouwmeester, D. *Linked and knotted beams of light.* Nat. Phys. **4**, 716–720 (2008). Experimentally realized Hopfion light configurations — relevant for Vol 4 Ch 11 / Ch 13 falsification-and-engineering pathways.
16. Trueba, J. L. & Rañada, A. F. *Electromagnetic knots.* Eur. J. Phys. **17**, 141 (1996).

**Lattice-discretization for micropolar field theories.**

17. Misra, A. & Poorsolhjouy, P. *Granular micromechanics based micromorphic model predicts frequency band gaps.* Continuum Mech. Thermodyn. **28**, 215–234 (2016). Discrete-to-continuum bridging for micropolar media.
18. Forest, S. & Sab, K. *Cosserat overall modeling of heterogeneous materials.* Mech. Res. Commun. **25**, 449–454 (1998). Graph-based discretization.

**AVE-internal references (already surveyed; load-bearing).**

19. [manuscript/vol_1_foundations/chapters/02_macroscopic_moduli.tex](../../manuscript/vol_1_foundations/chapters/02_macroscopic_moduli.tex) — Cosserat necessity
20. [manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex](../../manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex) — K = 2G identity
21. [manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex](../../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex) — Golden Torus derivation
22. [manuscript/vol_2_subatomic/chapters/03_neutrino_sector.tex](../../manuscript/vol_2_subatomic/chapters/03_neutrino_sector.tex) — Cosserat bending stiffness $\gamma_c$
23. [manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex](../../manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex) — Lepton spectrum from Cosserat sectors
24. [manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex](../../manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex) — Photon as Cosserat transverse mode
25. [manuscript/vol_4_engineering/chapters/11_experimental_falsification.tex](../../manuscript/vol_4_engineering/chapters/11_experimental_falsification.tex) — Falsification pathways
26. [manuscript/vol_4_engineering/chapters/13_future_geometries.tex](../../manuscript/vol_4_engineering/chapters/13_future_geometries.tex) — Cosserat torsion injection (engineering layer)
27. [manuscript/vol_4_engineering/chapters/15_autoresonant_breakdown_spice.tex](../../manuscript/vol_4_engineering/chapters/15_autoresonant_breakdown_spice.tex) — Autoresonant driving of Cosserat modes
28. [manuscript/backmatter/02_full_derivation_chain.tex](../../manuscript/backmatter/02_full_derivation_chain.tex) — Axiom 1 as micropolar continuum
29. [manuscript/backmatter/03_geometric_inevitability.tex](../../manuscript/backmatter/03_geometric_inevitability.tex) — K4 geometric uniqueness
30. [src/ave/topological/cosserat.py](../../src/ave/topological/cosserat.py) — Existing Cosserat sector implementation
31. [src/ave/topological/faddeev_skyrme.py](../../src/ave/topological/faddeev_skyrme.py) — 1D Faddeev-Skyrme radial solver

End of Phase-0 scoping.

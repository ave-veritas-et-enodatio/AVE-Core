[↑ Ch.2 — Baryon Sector](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-mnb3lt]
path-stable: "referenced from vol2 as sec:thermal_softening"
-->

## Thermal Lattice Softening ($\delta_{th}$)

The cold ($T=0$) Faddeev-Skyrme solver with $\kappa_{FS} = 8\pi$ evaluates the 1D scalar trace to $\mathcal{I}_{scalar}^{(cold)} \approx 1185\,m_e$, yielding a proton ratio of $\approx 1872$ (approximately $2\%$ above the empirical value). This systematic overestimate arises because the solver computes the ideal zero-temperature ground state, whereas the physical proton exists as a localized thermal hotspot within the LC condensate at an effective core temperature of $T_{core} \sim m_p c^2/k_B \approx 10^{13}\text{ K}$.

The baseline RMS thermal noise of the vacuum ("quantum foam") partially averages out the sharp gradient tensor $(\partial_\mu \mathbf{n} \times \partial_\nu \mathbf{n})^2$, effectively softening the quartic Skyrme repulsion. Additionally, the Faddeev-Skyrme energy functional includes Axiom 4 gradient saturation $S(|\partial_r\phi|,\,\pi/\ell_{node})$ inside the integrand, preventing the solver from resolving sub-lattice gradients. The thermally corrected coupling is:

> **[Resultbox]** *Thermal Lattice Softening*
>
> $$
> \kappa_{FS} = \kappa_{FS}^{(cold)} \left(1 - \delta_{th}\right) = 8\pi\left(1 - \frac{1}{14\pi^2}\right)
> $$

where the residual thermal correction factor $\delta_{th} = 1/(14\pi^2)$ captures the RMS noise averaging that remains after the gradient saturation is applied:

1. $\nu_{vac} = 2/7$ --- the Poisson ratio of the chiral LC lattice, which sets the anharmonic Gruneisen parameter governing the coupling between thermal fluctuations and elastic stiffness.
2. $\kappa_{cold} = 8\pi$ --- the Faddeev-Skyrme coupling (Skyrme stiffness).
3. $2/\pi$ --- the mean-to-peak ratio of rectified sinusoidal thermal noise. With the peak gradient already saturated by Axiom 4, the residual averaging acts on only the mean component.

The product evaluates to $\delta_{th} = \frac{\nu_{vac}}{\kappa_{cold}} \times \frac{2}{\pi} = \frac{2/7}{8\pi} \times \frac{2}{\pi} = \frac{1}{14\pi^2} \approx 0.00721$. Together with the gradient saturation inside the energy functional, this produces proton mass agreement to better than $0.1\%$ and validates the baryon ladder through crossing number $c = 15$ with maximum error $2.4\%$.

### The Faddeev-Skyrme Coupling Constant ($\kappa_{FS}$)

The quartic Skyrme stabilization term requires a dimensionless coupling constant $\kappa_{FS}$ that sets the relative strength of the fourth-order repulsive gradient against the second-order attractive gradient. In the AVE framework, this coupling is not a free parameter but is derived directly from the packing fraction:

> **[Resultbox]** *Faddeev-Skyrme Coupling Constant*
>
> $$
> \kappa_{FS}^{(cold)} = \frac{p_c}{\alpha} = \frac{8\pi\alpha}{\alpha} = \mathbf{8\pi}
> $$

This is a pure geometric constant: the solid-angle normalisation ($4\pi$) of the spherical energy integral, doubled by the two orthogonal principal strain axes of the LC condensate that jointly stabilize the defect against Derrick-type collapse.

### The 3D Orthogonal Tensor Trace ($\mathcal{I}_{tensor}$)

While the 1D scalar radial projection of the saturated topological Hamiltonian assumes spherical symmetry, the Proton is a $6^3_2$ Borromean linkage possessing $\mathbb{Z}_3$ discrete permutation symmetry. Because the three constituent flux tubes are mutually orthogonal, they cross over each other within the saturated structural core. In an LC resonant network, intersecting confined electromagnetic flux lines generate anisotropic *Transverse Polarization Strain*.

The total RMS energy integral is decomposed into two distinct geometric trace components: the continuous spherical scalar trace ($\mathcal{I}_{scalar}$), and the discrete orthogonal intersection trace ($\mathcal{I}_{tensor}$):

> **[Resultbox]** *Proton Mass Geometric Decomposition*
>
> $$
> m_p c^2 = \mathcal{I}_{scalar} \text{ (1D)} + \mathcal{I}_{tensor} \text{ (3D Orthogonal Crossings)}
> $$

The thermally corrected 1D solver, with Axiom 4 gradient saturation applied inside the integrand, evaluates the scalar component to $\mathcal{I}_{scalar} \approx 1162\,m_e$. The remaining mass generation is contained within the orthogonal topological interference vectors of the intersecting flux loops.

### Computational Proof: Skew-Lines and The Toroidal Halo

To analytically resolve the 3D orthogonal tensor trace ($\mathcal{I}_{tensor}$), the non-linear geometric frustration of the proton's spatial topology. The $6^3_2$ Borromean linkage is mathematically defined by exactly six orthogonal topological crossings.

By Axiom 1, the Full-Width at Half-Maximum (FWHM) of a fundamental flux tube is $1.0 l_{node}$. Furthermore, the hard-sphere exclusion principle dictates that orthogonal tubes cannot collide at a distance closer than $1.0 l_{node}$. To satisfy this constraint during 3D PDE integration, the flux tubes are modelled as **Skew Lines**, offset from one another by $1.0 l_{node}$ along their orthogonal axis.

When evaluated continuously across the discrete grid, this skew-line topology reveals a notable geometric symmetry:

1. At the exact 3D geometric midpoint between the two separated tubes, the Gaussian strain fields of the individual tubes evaluate to exactly $0.5$.
2. Their scalar sum peaks at $0.5 + 0.5 = \mathbf{1.0}$. The overlapping geometry reaches the Axiom 4 dielectric saturation limit without requiring arbitrary scaling coefficients.
3. Because the tubes are strictly orthogonal and geometrically symmetric, all transverse spatial gradients ($\partial_\mu n$) evaluate identically to zero at the exact geometric center.

Consequently, the cross-product vector ($\nabla V_1 \times \nabla V_2$) evaluates to zero. The topological metric bypasses the $0/0$ L'Hopital singularity. The mass generation cannot collapse into a point singularity; instead, the localised spatial metric is pushed outward, forming a stable, saturated 3D **Toroidal Halo** of tensor shear.

### Counting the Saturated Crossings

The $6^3_2$ Borromean linkage consists of three mutually orthogonal loops, each pair of which crosses exactly twice. The total number of pairwise orthogonal crossings is therefore $\binom{3}{2} \times 2 = 6$. By the $\mathbb{Z}_3$ permutation symmetry of the linkage, all six crossings are geometrically equivalent under discrete rotation.

### The Saturation Threshold (Under a Gaussian Flux-Tube Ansatz)

The critical advance in evaluating $\mathcal{V}_{total}$ is determining the density threshold at which the combined flux-tube field becomes topologically locked. This threshold is derived from the mutual inductance coupling between the orthogonal LC flux loops at their crossings, conditional on the radial profile of the flux tube.

**Profile ansatz (open derivation gap).** The σ derivation below assumes a **Gaussian flux-tube radial profile** with FWHM $= \ell_{node}$. Axiom 1 fixes the FWHM (Nyquist content: the smallest unambiguously-resolvable transverse feature is one lattice pitch), but it does not specify the functional form. The Gaussian is an *ansatz* for tractability; other LC-soliton profiles (sech² kink, Bessel $J_0$ waveguide fundamental, the algebraic Axiom 4 kernel $\sqrt{1-r^2}$) would yield different mutual-coupling kernels and a different $\rho_{threshold}$. Either deriving the Gaussian profile from Axiom 4 LC dynamics, or replacing it with the framework-consistent profile and re-evaluating $\rho_{threshold}$, is a documented outstanding rigour gap (see [`mathematical-closure.md`](../../../common/mathematical-closure.md) §Outstanding Rigour Gaps). The result below is internally consistent and parameter-free *conditional on the Gaussian ansatz*.

> **Do NOT fuse $\rho_{threshold}$ with $\mathcal{V}_{total} = 2$.** The Gaussian-ansatz gap binds the *saturation density threshold* $\rho_{threshold} \approx 1.1062$ (and the saturated-overlap-volume integral evaluated against it) — both profile-dependent. It does **NOT** bind $\mathcal{V}_{total} = 2$: that "2" is the **dual-reactance count** (the node's two reactance sectors $X_C + X_L$, Axiom 1), a profile-**independent** forced integer count, mass-confirmed via $m_p$ (canonical: [`dual-reactance-storage-taxonomy.md`](../../../common/dual-reactance-storage-taxonomy.md)). A channel count is *counted*, not integrated; it does not change if the flux-tube profile changes. That the Gaussian saturated-overlap-volume below also lands near 2.0 is a *property of the Gaussian ansatz*, NOT a derivation of the reactance count.

Each flux tube is taken as a Gaussian LC resonant loop with FWHM $= \ell_{node}$, giving a Gaussian dispersion $\sigma = \ell_{node}/(2\sqrt{2\ln 2})$. At a pairwise crossing, the tubes are separated by the skew offset $d = \ell_{node}/2$. The mutual inductance coupling coefficient between two perpendicular tubes at this separation is:

> **[Resultbox]** *Orthogonal Flux Tube Mutual Coupling*
>
> $$
> \frac{M}{L} = \exp\!\left(-\frac{d^2}{4\sigma^2}\right) = \exp\!\left(-\frac{\ln 2}{2}\right) = \frac{1}{\sqrt{2}} \quad \text{(exactly)}
> $$

The saturation threshold is where the combined inductive field density ($\rho_{total} = \rho_x + \rho_y + \rho_z$) exceeds the single-tube peak by the minimum mutual coupling required for topological coherence:

> **[Resultbox]** *Topological Inductive Density Threshold*
>
> $$
> \rho_{threshold} = 1 + \frac{\sigma}{4} = 1 + \frac{\ell_{node}}{8\sqrt{2\ln 2}} \approx 1.1062
> $$

The factor of 4 in $\sigma/4$ is not arbitrary: it is the *same* 4 appearing in the mutual inductance exponent $\exp(-d^2/4\sigma^2)$. When two Gaussians of dispersion $\sigma$ overlap mutually, their convolution kernel has effective width $\sqrt{2\sigma^2 + 2\sigma^2} = 2\sigma$, and the coupling integral evaluates against $4\sigma^2$. The threshold excess $\sigma/4$ is therefore the mutual field density contribution from two coplanar Gaussian modes overlapping at their natural convolution scale---a direct consequence of the Gaussian arithmetic, not a fitted parameter.

This is a **closed-form result with no fitted parameters**, conditional on the Gaussian flux-tube ansatz declared above. Axiom 1 fixes the FWHM; the Gaussian *profile* is the open derivation gap that, when closed, will determine whether the closed form remains $1.1062$ or shifts to a different value with the framework-consistent profile.

**Gaussian-ansatz saturated-overlap-volume integral (a $\rho_{threshold}$ consistency check, NOT the source of $\mathcal{V}_{total} = 2$).** The "3D FEM integration of the full Borromean topology yields $\mathcal{V}_{total} = 2.0$" narrative is **retired** — it was triply wrong: (1) the method is **not** finite-element — it is a uniform-Cartesian-grid Riemann sum (voxel quadrature: $V_{sat} = \sum \Theta(\rho_{total} > \rho_{threshold})\,\Delta x^3$); (2) it does **not** compute $\mathcal{V}_{total}$ the reactance count — it integrates the **Gaussian-ansatz** three-tube saturated overlap volume against the (profile-dependent) $\rho_{threshold}$ of the previous block; (3) it is therefore a *self-consistency check on the Gaussian ansatz*, not an independent geometric derivation of the integer 2. The script ([`src/scripts/vol_2_subatomic/fem_borromean_convergence.py`](../../../../../src/scripts/vol_2_subatomic/fem_borromean_convergence.py), misnamed "FEM"; JAX port `fem_borromean_convergence_jax.py`) does run and produces the figures below:

| $N$ (grid) | $\mathcal{V}_{sat}$ (Gaussian overlap volume) | $\Delta$ from 2.0 |
|---|---|---|
| 128 | 2.0002 | 0.01% |
| 256 | 2.0012 | 0.06% |
| $N\to\infty$ (Richardson) | 2.0027 | 0.13% |

That the Gaussian-ansatz saturated overlap volume lands near 2.0 is a *property of the Gaussian profile at this $\rho_{threshold}$* — it is corroborative of internal consistency, NOT the derivation of $\mathcal{V}_{total}$. The actual $\mathcal{V}_{total} = 2$ is the **dual-reactance count** (forced reactance-sector count $X_C + X_L$, Axiom 1; profile-independent; mass-confirmed via $m_p$), canonical at [`dual-reactance-storage-taxonomy.md`](../../../common/dual-reactance-storage-taxonomy.md). Do **NOT** read the near-2.0 overlap-volume result as a geometric identity confirming a topological bound — that conflates the profile-dependent $\rho_{threshold}$ integral with the profile-independent reactance count (the "don't-fuse-the-2's" hazard).

---

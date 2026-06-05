[↑ Ch.2: General Relativity and Gravitational Waves](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-zf8eah]
-->

# The Double Deflection: Why Light Bends Twice as Much as Matter

**Source:** `manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex` §sec:double_deflection

In 1801 Johann Georg von Soldner, treating light as a massive ballistic corpuscle, computed the Newtonian deflection of starlight grazing the Sun as $\delta_{\text{matter}} = 2GM/(bc^2)$. In 1915 Einstein showed the actual deflection is exactly twice this: $\delta_{\text{light}} = 4GM/(bc^2)$. The factor of 2 is the historically decisive signature of General Relativity.

Within the AVE framework this factor of 2 is neither geometric curvature nor a 4D manifold artefact. It is a direct consequence of how two different kinds of wave packet couple to the strained LC lattice $\mathcal{M}_A$, and it is fully determined by the trace-reversed vacuum Poisson ratio $\nu_{vac} \equiv 2/7$ derived in Ch.1 ([vacuum-poisson-ratio](../ch01-gravity-yield/vacuum-poisson-ratio.md)).

## Two Coupling Channels, Two Projections

A massive topological defect (Hopfion) and a massless photon share the same spatial gradient of the vacuum refractive index $n(\mathbf{r})$, but they couple to it through structurally distinct mechanical channels:

- **Matter (scalar coupling).** A fast-moving massive particle is an isotropic 3D volumetric wave packet carrying finite rest energy. It couples to the *scalar* (isotropic bulk) component of the lattice strain via the $1/7$ volumetric projection ([one-seventh-impedance-projection](../ch01-gravity-yield/one-seventh-impedance-projection.md), "The $1/7$ Isotropic Impedance Projection"):
  $$
  n_{\text{scalar}}(\mathbf{r}) = 1 + \tfrac{1}{7}\chi_{vol}(\mathbf{r})
  $$
  This is the projection a 1D uniaxial stress makes onto the isotropic spherical bulk tensor $\tfrac{1}{3}\theta\delta_{ij}$ of a medium with $\nu_{vac} = 2/7$.

- **Light (transverse coupling).** A photon is a purely transverse Cosserat shear wave; it carries no rest mass and has no longitudinal (scalar) component. It is therefore *mechanically blind* to the isotropic bulk and couples instead to the transverse cross-sectional strain of the lattice. In classical mechanics the relationship between axial and transverse strain is governed exactly by Poisson's ratio, giving the transverse-sector refractive index:
  $$
  n_{\perp}(\mathbf{r}) = 1 + \nu_{vac}\,\chi_{vol}(\mathbf{r}) = 1 + \tfrac{2}{7}\chi_{vol}(\mathbf{r})
  $$

## The Factor of 2 Falls Out of $2/7 : 1/7$

The deflection of a wave packet grazing a spherically symmetric refractive gradient is, in the eikonal limit, linear in the projection coefficient multiplying $\chi_{vol}$. Because the transverse Poisson coupling ($2/7$) is arithmetically exactly double the scalar bulk coupling ($1/7$), the photon refracts through a gradient exactly twice as severe as the ballistic matter soliton (a standing-resonance topological defect coupling to the isotropic bulk, *not* a longitudinal matter wave):

<!-- claim-quality: clm-zf8eah -->
> **[Resultbox]** *Double Deflection*
>
> $$
> \frac{\delta_{\text{light}}}{\delta_{\text{matter}}} = \frac{n_{\perp} - 1}{n_{\text{scalar}} - 1} = \frac{2/7}{1/7} = 2
> $$

With $\chi_{vol}(r) = 7GM/(c^2 r)$ ([gravitational-coupling-constant](../ch01-gravity-yield/gravitational-coupling-constant.md), "Gravitational Coupling Constant"), the two deflection integrals reduce to the canonical expressions:
$$
\delta_{\text{matter}} = \frac{2GM}{bc^2} \quad\text{(Newton / Soldner 1801)},
\qquad
\delta_{\text{light}} = \frac{4GM}{bc^2} \quad\text{(Einstein 1915)}
$$
For the Sun at grazing incidence ($b = R_\odot$), the predicted starlight deflection is the observed $1.75$ arcseconds.

## What This Derivation Replaces

The AVE Double Deflection replaces the "Rubber Sheet" metaphor and its requirement for a hidden fourth spatial dimension to accommodate curvature. The factor of 2 that distinguishes Einstein's prediction from Newton's is:

- **not** a general-relativistic signature of a curved 4-manifold,
- **not** the consequence of massless particles following null geodesics in a pseudo-Riemannian metric,
- **but** the mechanical fingerprint of a 3D Cosserat elastic solid with a Poisson ratio rigidly locked to $\nu_{vac} = 2/7$ by trace-reversal ($K = 2G$).

The $1.75$ arcsecond deflection of starlight, historically the decisive experimental validation of General Relativity, is here derived as the macroscopic mechanical signature of the same Chiral LC trace-reversal identity that sets the weak mixing angle $\sin^2\theta_W = 2/9$ and the neutrino mass-squared splitting ratio $\nu_{vac} = 2/7$. The factor of 2 in Einstein's $4GM/bc^2$ is not a feature of empty geometry; it is the ratio of the transverse to the isotropic Poisson projection of a strained 3D Cosserat continuum.

---

> → Primary: [Vacuum Poisson Ratio](../ch01-gravity-yield/vacuum-poisson-ratio.md) — the trace-reversed $\nu_{vac} = 2/7$ ($K = 2G$) that fixes both projection coefficients.

> ↗ See also: [Einstein Lensing Deflection](../ch03-macroscopic-relativity/einstein-lensing-deflection.md) — the $\delta = 4GM/(bc^2)$ result from the optical-metric route.

> ↗ See also: [K4-TLM Lensing Validation](k4-tlm-lensing-validation.md) — native Diamond-lattice cross-validation of the photon deflection.

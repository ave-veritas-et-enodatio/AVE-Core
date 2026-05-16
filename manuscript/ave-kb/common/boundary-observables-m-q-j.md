[↑ Common Resources](index.md)
<!-- leaf: verbatim -->
<!-- path-stable: referenced from vol1, vol2, vol3, vol4, vol5, vol6 as canonical M, Q, J boundary-observables reference -->

# The Three Canonical Boundary Observables: $\mathcal{M}$, $\mathcal{Q}$, $\mathcal{J}$

At every $\Gamma = -1$ saturation surface $\partial\Omega$ in the substrate — the boundary where Axiom 4's kernel reaches $S(A) \to 0$ locally — exactly **three integrated quantities are externally observable**. This leaf is the canonical AVE-Core reference; manuscript canonicalization lives at Common Foreword §"Three Boundary Observables and the Substrate-Observability Rule" + Vol 1 Ch 1 §sec:substrate_vocab_box_ch1.

## The three invariants

| Symbol | Canonical name | Operational definition | Dimensionality | EE projection | ME projection | QFT projection |
|---|---|---|---|---|---|---|
| $\mathcal{M}$ | Integrated strain integral | $\displaystyle\int_\Omega (n(\mathbf{r}) - 1)\, dV$ | **3D volume** | inductance $L$ | inertia (kg) | rest energy $m c^2$ |
| $\mathcal{Q}$ | Boundary linking number | $\mathrm{Link}(\partial\Omega, \mathbf{F}_{\text{substrate}}) \in \mathbb{Z}$ | **1D line/loop** | charge $Q$ | (no clean analog) | electromagnetic charge |
| $\mathcal{J}$ | Boundary winding number | $\mathrm{Wind}(\partial\Omega)$, half-integer per $SU(2)$ double-cover | **2D surface** | magnetic moment | rotation | spin $J$ |

**Stokes-theorem dimensional structure.** Each invariant uses one fewer integration dimension than the substrate's 3D bulk — $\mathcal{M}$ counts a volume, $\mathcal{J}$ counts a surface winding, $\mathcal{Q}$ counts a line/loop linking. The three dimensions are exhaustive: there is no fourth integrated boundary observable at this scale-invariant structure.

## The substrate-observability rule

For any localized region $\Omega \subset \mathcal{M}_A$ enclosed by a $\Gamma = -1$ saturation surface:

1. The boundary totally reflects substrate waves outside and totally traps them inside.
2. The interior is causally and impedance-disconnected from external observers.
3. **Only $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ are externally measurable.** Interior eigenmode wavelengths, microrotation profiles, soliton topology, and bond-stress distributions are invisible to the substrate.

This is the **no-hair theorem applied universally** — not as a black-hole-specific theorem but as the substrate's fundamental observability constraint at every scale.

## Same mechanism at all scales

The same three observables appear at every $\Gamma = -1$ saturation surface in the substrate hierarchy:

| Scale | Boundary | Internal solitons | Observables |
|---|---|---|---|
| Electron ($\ell \sim 10^{-13}$ m) | Horn-torus tube wall (TIR at saturation) | $0_1$ unknot single soliton | $m_e c^2$, $e$, $\hbar/2$ |
| Nucleus ($\ell \sim 10^{-15}$ m) | Borromean confinement on $(2,5)$ cinquefoil | 3-strand $SU(3)$ Borromean linkage | nucleon mass, electric charge, nuclear spin |
| Atom ($\ell \sim 10^{-10}$ m) | Outer shell saturation | Nucleus + $Z$ electrons | atomic mass, ionization, total angular momentum |
| Planetary magnetopause | Magnetosphere boundary | Planet + field-aligned solitons | planet mass, dipole moment, rotation |
| Black-hole event horizon ($r = 2GM/c^2$) | Schwarzschild horizon | All matter → pre-geodesic plasma | $M$ (ADM mass), $Q$, $J$ (Kerr-Newman) |
| Cosmic horizon ($R_H \sim 10^{26}$ m) | Parent-BH Schwarzschild radius | All observable matter + dark sector | $\mathcal{M}_{\text{cosmic}}$, $\mathcal{Q}_{\text{cosmic}}$, $\mathcal{J}_{\text{cosmic}}$ (CMB anomalies, LSS rotation, Hubble flow anisotropy) |

**The substrate observes integer/half-integer counts of relational observables; everything else is interior plumbing.**

## The fine-structure constant as electron-scale $\mathcal{M} + \mathcal{J} + \mathcal{Q}$

The Vol 1 Ch 8 canonical $\alpha^{-1}$ derivation decomposes into exactly three contributions corresponding to the three boundary-integral dimensionalities:

$$
\alpha^{-1} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}} = 4\pi^3 + \pi^2 + \pi \approx 137.036
$$

| Term | Value | Dimensionality | Maps to |
|---|---|---|---|
| $\Lambda_{\text{vol}} = 4\pi^3$ | volume integral | 3D | $\mathcal{M}$ (mass) |
| $\Lambda_{\text{surf}} = \pi^2$ | surface integral | 2D | $\mathcal{J}$ (spin) |
| $\Lambda_{\text{line}} = \pi$ | line integral | 1D | $\mathcal{Q}$ (charge) |

Each power of $\pi$ counts one dimension of boundary integration, as in Stokes-theorem dimensional reduction. The load-bearing $R \cdot r = 1/4$ normalization that makes $\Lambda_{\text{vol}} = 16\pi^3 \cdot R \cdot r$ evaluate to exactly $4\pi^3$ is derived from the spin-$\tfrac{1}{2}$ half-cover of the standard Clifford torus $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ (the half-cover is AVE-native via the $K_4 \to A_4 \to 2T \subset SU(2)$ chain + Finkelstein–Misner mechanism, not an imported QM postulate). **The decomposition is not coincidental** — it is the substrate's natural three-integral boundary-observability structure expressed at the electron-scale Q-factor.

## Operational analysis recipe

For any localized region $\Omega$ in the substrate:

1. **Identify the saturation surface** $\partial\Omega$ — the boundary where $S(A) \to 0$ locally.
2. **Compute $\mathcal{M}, \mathcal{Q}, \mathcal{J}$** as the three integrated invariants over the substrate fields ($\mathcal{M}$ from a 3D volume integral; $\mathcal{J}$ from a 2D surface integral; $\mathcal{Q}$ from a 1D line/loop integral).
3. **Compare against measured observables** (mass, charge, spin or angular momentum in the appropriate projection).
4. **The interior topology is invisible from outside** — only the boundary integrals matter.

## We sit inside the cosmic $\Gamma = -1$ boundary

The substrate-observability rule applies to ourselves. We are inside the cosmic $\Gamma = -1$ surface (the cosmic horizon = parent-black-hole Schwarzschild radius per the generative cosmology, [Vol 3 Ch 4 (Generative Cosmology)](../../vol_3_macroscopic/chapters/04_generative_cosmology.tex)). We measure $\mathcal{M}_{\text{cosmic}}, \mathcal{Q}_{\text{cosmic}}, \mathcal{J}_{\text{cosmic}}$ from inside via local-physics consequences: CMB anomalies, large-scale-structure rotation, Hubble flow anisotropy. The mechanism that set $\mathcal{J}_{\text{cosmic}}$ at lattice genesis is the universal Axiom 4 strain-snap mechanism (A-034) — directly observable at every smaller scale.

## Cross-references

- **Canonical manuscript anchors:**
  - Common Foreword §"Three Boundary Observables and the Substrate-Observability Rule"
  - [Vol 1 Ch 1 (Four Fundamental Axioms)](../../vol_1_foundations/chapters/01_fundamental_axioms.tex) §sec:substrate_vocab_box_ch1
  - [Vol 1 Ch 8 (Alpha Golden Torus)](../../vol_1_foundations/chapters/08_alpha_golden_torus.tex) — $\alpha^{-1}$ decomposition derivation
  - [Backmatter Ch 7 — Universal Saturation-Kernel Catalog](../../backmatter/07_universal_saturation_kernel.tex) — same-mechanism-at-all-scales empirical demonstration
- **KB cross-cutting:**
  - [trampoline-framework.md §4-§7](trampoline-framework.md) — picture-first multi-scale hierarchy
  - [glossary §2 boundary invariants matrix](../../../docs/glossary.md)
  - [axiom-homologation.md](axiom-homologation.md) — Axiom 3 (Minimum Reflection Principle) substrate-observability framing

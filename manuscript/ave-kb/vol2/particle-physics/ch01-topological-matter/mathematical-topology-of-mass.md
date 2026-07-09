[↑ Ch.1 — Topological Matter](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-oygz1i]
-->

## The Mathematical Topology of Mass

Before analyzing specific particle geometries, the text formally defines the foundational energy and topological constraints of the continuum. In a continuous non-linear substrate, stable particles are defined as finite-energy soliton solutions to the generalised **Faddeev-Skyrme Energy Functional**:

> **[Resultbox]** *Faddeev-Skyrme Energy Functional*
>
> $$
> E = \int \left( \frac{1}{2}\partial_\mu \vec{n} \cdot \partial^\mu \vec{n} + \frac{1}{4e^2}(\partial_\mu \vec{n} \times \partial_\nu \vec{n})^2 \right) d^3x
> $$

where $\vec{n}$ represents the normalised local LC displacement vector of the vacuum. The first term dictates the standard kinematic energy of the field, while the second non-linear term (scaled by the dielectric yield bound $e$) repels the strands, preventing the knot from collapsing into a singularity.

> **Peer + finiteness note.** The Faddeev-Skyrme energy functional is **standard soliton field theory** (Faddeev–Niemi / Skyrme), imported here as calculational scaffolding — **peer-with-standard**, not an AVE-distinct result. Its non-linear (Skyrme) term prevents *continuum* collapse; on the discrete K4 substrate (Axiom 1) the finite-energy floor is set concretely by the $\ell_{node}$ pitch cutoff, which is what makes the electron self-energy finite (integration over a 1D loop of ropelength $\sim \ell_{node}$, not a 0D point — see [Electron Unknot](electron-unknot.md) §"Resolution of the Electrostatic Point-Charge Singularity" and [Mass-Closure Theorem](mass-closure-theorem.md)).

The specific topological identity of any particle is classified by its **Hopf Charge** or **Gauss Linking Number** ($Q$), an invariant topological integer defining the number of times the internal magnetic flux lines intertwine:

> **[Resultbox]** *Gauss Linking Number (Hopf Charge)*
>
> $$
> Q = \frac{1}{16\pi^2} \int \epsilon_{ijk} \vec{n} \cdot (\partial_i \vec{n} \times \partial_j \vec{n}) \ d^3x
> $$

> **General functional vs the electron's actual topology (real-space / phase-space).** The Hopf charge / Gauss linking number above is the **general** classifier for the particle spectrum; it is NOT a statement that the electron carries non-trivial *real-space* linking. The **electron's real-space body is the $0_1$ unknot** ($Q_H = 0$ in real space — see [Electron Unknot](electron-unknot.md)); its $(2,3)$ winding is a **phase-space** Clifford-torus portrait, not a real-space knot (see [Torus-Knot Uniqueness](torus-knot-uniqueness.md) and CLAUDE.md INVARIANT-N1). Non-trivial Hopf/linking charges classify the phase-space-linked members of the spectrum; the real-space/phase-space distinction must be carried whenever $Q$ is applied to a specific particle.

Because this topological index $Q$ is conserved under continuous domain deformations, it derives the conservation laws (e.g., Baryon Number and Lepton Number) from geometric invariants.

---

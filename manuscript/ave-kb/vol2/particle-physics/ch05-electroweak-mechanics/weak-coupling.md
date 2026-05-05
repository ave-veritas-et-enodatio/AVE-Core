[↑ Ch.5 — Electroweak Mechanics](index.md)
<!-- leaf: verbatim -->
<!-- claim-quality: q8un7j -->

## The Absolute $W$ Boson Mass: Chirality Mismatch Self-Energy

A twist defect in the vacuum creates a torsional field that obeys the same 3D Laplace equation as the Coulomb field: $\nabla^2\theta = 0$, giving $\theta(r) \propto 1/r$ and $|\nabla\theta|^2 \propto 1/r^4$. The self-energy integral is:

> **[Resultbox]** *Torsional Self-Energy Integral*
>
> $$
> E_{\text{twist}} = \frac{T_{EM}^2}{4\pi\,\varepsilon_T\, r_0}
> $$

where $T_{EM}$ is the lattice tension (torsional "charge"), $r_0 = l_{node}/(2\pi)$ is the flux tube UV cutoff (Axiom 1), and $\varepsilon_T$ is the torsional permittivity of the chiral lattice.

The Chiral SRS net (Axiom 2) has an intrinsic handedness. A twist that *matches* the lattice chirality propagates freely (this is why left-handed neutrinos are nearly massless). A twist that *opposes* the chirality fights the LC ground state, incurring a stiffness penalty.

The factor $\alpha^2$ is derived from the interaction Lagrangian. The twist field $\phi$ couples to the EM background through the Axiom 4 dielectric susceptibility $\varepsilon(\phi) = \varepsilon_0(1 + \alpha f(\phi))$, giving:

> **[Resultbox]** *Torsional-EM Interaction Lagrangian*
>
> $$
> \mathcal{L}_{\text{int}} = \frac{\varepsilon_0 \alpha}{2}\,\phi\,|\mathbf{E}|^2
> $$

The self-energy is a **two-vertex process** (second-order perturbation theory):

> **[Resultbox]** *Second-Order Self-Energy*
>
> $$
> E_{\text{self}} = \iint \mathcal{L}_{\text{int}}(\mathbf{x})\, G(\mathbf{x}-\mathbf{x}')\, \mathcal{L}_{\text{int}}(\mathbf{x}')\, d^3x\, d^3x' \;\propto\; \alpha \times \alpha = \alpha^2
> $$

---

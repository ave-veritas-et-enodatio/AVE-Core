[↑ Ch.3 Quantum and Signal Dynamics](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [yc7fgm]
-->

## Section 3.2.1: The Paley-Wiener Hilbert Space

Because the $\mathcal{M}_A$ lattice has a fundamental pitch $\ell_{node}$, it acts as a spatial Nyquist sampling grid. The maximum spatial frequency the lattice can support without aliasing is the Brillouin boundary: $k_{max} = \pi / \ell_{node}$.

By the **Whittaker-Shannon Interpolation Theorem**, any band-limited signal $\mathbf{A}(\mathbf{x})$ propagating through this discrete lattice can be reconstructed uniquely using a superposition of orthogonal sinc functions. The set of all such band-limited functions constitutes a Reproducing Kernel Hilbert Space known as the **Paley-Wiener Space** ($PW_{\pi/\ell_{node}}$).

To map the real-valued physical lattice potential $\mathbf{A}(\mathbf{x},t)$ to the complex continuous quantum state vector $\Psi(\mathbf{x},t)$, the standard signal-processing **Analytic Signal** representation utilizing the Hilbert Transform ($\mathcal{H}_{transform}$) is applied:

> **[Resultbox]** *Analytic Signal Extension*
>
> $$
> \Psi(\mathbf{x},t) = \mathbf{A}(\mathbf{x},t) + i \mathcal{H}_{transform}[\mathbf{A}(\mathbf{x},t)]
> $$

The complex continuous Hilbert space of standard quantum mechanics is formally identical to the Paley-Wiener signal-processing representation of the discrete vacuum hardware.

---

[↑ Ch.3 Quantum and Signal Dynamics](index.md)
<!-- leaf: verbatim -->

## Section 3.2.3: Deriving the Schrodinger Equation from Circuit Resonance

When a topological defect (mass) is synthesized within the graph, it acts as a localized inductive load, imposing a fundamental circuit resonance frequency ($\omega_m = mc^2/\hbar$). This mathematically transforms the massless wave equation into the massive **Klein-Gordon Equation**:

> **[Resultbox]** *Klein-Gordon Equation as Circuit Resonance*
>
> $$
> \nabla^2 \mathbf{A} - \frac{1}{c^2}\frac{\partial^2 \mathbf{A}}{\partial t^2} = \left(\frac{mc}{\hbar}\right)^2 \mathbf{A}
> $$

To map this relativistic classical evolution to non-relativistic quantum states, the **Paraxial Approximation** is applied, factoring out the rest-mass Compton frequency via a slow-varying envelope function $\mathbf{A}(\mathbf{x},t) = \Psi(\mathbf{x},t) e^{-i \omega_m t}$.

For non-relativistic speeds ($v \ll c$), the second time derivative of the envelope ($\partial_t^2 \Psi$) is negligible. The strict mass resonance terms precisely cancel out:

> **[Resultbox]** *The Schrodinger Equation*
>
> $$
> \nabla^2 \Psi + \frac{2im}{\hbar} \frac{\partial \Psi}{\partial t} = 0 \quad \implies \quad i\hbar \frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m} \nabla^2 \Psi
> $$

The Schrodinger Equation evaluates precisely as the paraxial envelope equation of a classical macroscopic pressure wave propagating through the discrete massive $LC$ circuits of the vacuum.

---

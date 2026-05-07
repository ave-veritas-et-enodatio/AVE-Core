[↑ Ch.3 Quantum and Signal Dynamics](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [7zuwtm]
-->

## Section 3.2.3: Deriving the Schrodinger Equation from Circuit Resonance

When a topological defect (mass) is synthesized within the graph, it acts as a localized inductive load, imposing a fundamental circuit resonance frequency ($\omega_m = mc^2/\hbar$). This mathematically transforms the massless wave equation into the massive **Klein-Gordon Equation**:

> **[Resultbox]** *Klein-Gordon Equation as Circuit Resonance*
>
> $$
> \nabla^2 \mathbf{A} - \frac{1}{c^2}\frac{\partial^2 \mathbf{A}}{\partial t^2} = \left(\frac{mc}{\hbar}\right)^2 \mathbf{A}
> $$

To map this relativistic classical evolution to non-relativistic quantum states, the **Paraxial Approximation** is applied, factoring out the rest-mass Compton frequency via a slow-varying envelope function $\mathbf{A}(\mathbf{x},t) = \Psi(\mathbf{x},t) e^{-i \omega_m t}$.

For non-relativistic speeds ($v \ll c$), the second time derivative of the envelope ($\partial_t^2 \Psi$) is negligible. The strict mass resonance terms precisely cancel out:

> **[Resultbox]** *The Schrodinger Equation (free particle)*
>
> $$
> \nabla^2 \Psi + \frac{2im}{\hbar} \frac{\partial \Psi}{\partial t} = 0 \quad \implies \quad i\hbar \frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m} \nabla^2 \Psi
> $$

The Schrodinger Equation evaluates precisely as the paraxial envelope equation of a classical macroscopic pressure wave propagating through the discrete massive $LC$ circuits of the vacuum.

### Bound-State Form: Spatial Modulation of $\varepsilon_{eff}$ Produces $V(\mathbf{r})\Psi$

The free-particle form above assumes uniform $\varepsilon_0, \mu_0$ across the lattice. When an external defect (a stationary topological knot, an atomic core, an applied static field) imprints a **spatial modulation** on the local LC properties, $\varepsilon_{eff}(\mathbf{r}) = \varepsilon_0 [1 + \chi(\mathbf{r})]$ with $|\chi| \ll 1$ in the linear regime, the wave-speed becomes position-dependent: $c_{eff}(\mathbf{r}) = c_0 / \sqrt{1 + \chi(\mathbf{r})}$. The Klein-Gordon equation acquires the corresponding modulated coefficient:

$$
\nabla^2 \mathbf{A} - \frac{1}{c_{eff}^2(\mathbf{r})}\frac{\partial^2 \mathbf{A}}{\partial t^2} = \left(\frac{mc}{\hbar}\right)^2 \mathbf{A}
$$

Expanding $1/c_{eff}^2 = (1+\chi(\mathbf{r}))/c_0^2$ and applying the same paraxial factoring $\mathbf{A} = \Psi\,e^{-i\omega_m t}$, the modulation contributes an extra term proportional to $m c^2 \chi(\mathbf{r})/(2)$ in the envelope equation. Identifying the on-site interaction energy

$$
V(\mathbf{r}) \equiv \tfrac{1}{2}\, m c^2\, \chi(\mathbf{r})
$$

yields the **full Schrödinger equation** with external potential:

> **[Resultbox]** *Schrödinger Equation with External Potential*
>
> $$
> i\hbar\,\frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\Psi + V(\mathbf{r})\,\Psi
> $$

**Physical reading.** $V(\mathbf{r})$ is the spatially-dependent rest-energy shift induced by the local dielectric perturbation $\chi(\mathbf{r})$. A nuclear Coulomb well, an applied electric field, or another knot's strain field all enter through this same mechanism: by modulating the local lattice constitutive parameters, they shift the local Compton frequency seen by the propagating wave, which becomes a position-dependent potential in the paraxial envelope. Bound-state physics (atomic orbitals, potential wells, tunneling barriers) recovers from this form by standard separation of variables; the same impedance-matching condition $2\pi r = n\lambda$ that defines the unknot (here "unknot" = the de Broglie standing-wave *orbital path* satisfying Bohr quantization, i.e. an unknotted closed curve around the nucleus, *not* the electron's body topology — body-topology question tracked at `trf3bd`/`unk0bd`) reproduces the hydrogenic energy levels $E_n = -m_e c^2 \alpha^2 / (2 n^2)$ (Vol 2 Ch 7).

**Magnetic case.** A spatial modulation of $\mu_{eff}(\mathbf{r})$ contributes via the same paraxial argument to a vector-potential coupling $-(e/m c)\mathbf{A}\cdot\mathbf{p}$ at leading order; combined with the scalar $V(\mathbf{r})$ above, the full minimal-coupling Schrödinger Hamiltonian $\frac{1}{2m}(\mathbf{p} - e\mathbf{A}/c)^2 + V$ follows. The derivation is mechanically the same as the classical paraxial-wave-in-modulated-medium argument; no quantum postulates are imported.

---

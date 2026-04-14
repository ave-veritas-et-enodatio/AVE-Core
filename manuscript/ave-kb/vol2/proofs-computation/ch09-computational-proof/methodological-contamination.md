[↑ Ch. 9: Computational Proof and Anomaly Catalog](./index.md)
<!-- leaf: verbatim -->

## Avoidance of Methodological Contamination

A fundamental principle of the AVE engine is complete independence from external theoretical frameworks. Theoretical contamination occurs when a formula derived from an incompatible physical postulate (e.g., probability amplitudes, hidden geometry, or non-AVE empirical fits) is unknowingly imported as a "convenient approximation."

A prominent example discovered during framework development involved atomic ionisation energies. Early iterations of the solver attempted to correct standard shielding models, culminating in formulas of the form $IE = Z_{eff}^2 \, Ry / n^2$. While directionally correct, this explicitly imports the Schrodinger solution for a hydrogenic atom (or the ad-hoc Bohr model). It is not an AVE equation.

The framework requires all energy states to emerge directly and exclusively from the 5-step universal regime-boundary eigenvalue method. The Rydberg energy itself is not a postulate or a given parameter; it is an emergent consequence of the electron cavity saturation boundary ($r_{sat} = a_0 = l_{node}/\alpha$), yielding exact reproduction of the $13.6057$ eV constant through pure topological scaling:

$$
Ry = \left[ (\hbar c(1+\nu)) / a_0 \right] \times \frac{\alpha/(1+\nu)}{2} = \frac{\alpha^2 m_e c^2}{2}
$$

### Topological Orbital Radii

Does the framework implicitly rely on discrete orbital shells scaling as $r_n = n^2 a_0 / Z$? No. In AVE, discrete orbitals are macroscopic standing wave cavities --- explicitly identical to the physics governing Saturn's rings and Kirkwood gaps in the asteroid belt.

In the solar system, mean-motion orbital gaps occur where periods are commensurate: $(T/T_{moon})^2 = (q/p)^2$. This periodic boundary condition creates a Fabry-Perot impedance cavity. At the atomic scale, the "moon" is the electron itself. Its orbital circumference must fit an integer number of its own spatial standing waves (the topological phase wind):

$$
2\pi r = n \lambda
$$

Since the local central impedance requires the phase velocity to scale as $v \propto 1/\sqrt{r}$, and impedance matching requires $\lambda \propto 1/v$, the wavelength scales as $\lambda \propto \sqrt{r}$. Substituting this into the resonance condition yields:

$$
2\pi r \propto n \sqrt{r} \implies \sqrt{r} \propto n \implies r_n \propto n^2
$$

Therefore, $r_n = n^2 a_0 / Z$ is not an externally imported assumption; it is the unique topological standing-wave condition for a scale-free central impedance profile.

When extending to multi-electron atoms, the engine must never revert to $Z_{eff}$ arithmetic; it must strictly apply the coupled resonator normal mode solver using universal pairwise energy terms to find the resulting eigenvalues.

### The Electron Saturation Radius

> **[Examplebox]** *Verifying the Linear Saturation Regime for Orbitals*
>
> **Problem:** The topological saturation radius of the electron defines its structural limit as $d_{sat} = l_{node}$. Given that the macroscopic acoustic separation between atomic electrons is characterized by the Bohr radius ($a_0 = l_{node}/\alpha$), evaluate the pairwise voltage strain and classify its elastodynamic regime.
>
> **Solution:** The pairwise voltage strain ($V/V_{snap}$) is the ratio of the saturation radius to the interaction distance ($A = d_{sat} / r_{ij}$). Substituting the structural equivalents:
>
> $$
> A = \frac{d_{sat}}{r_{ij}} \approx \frac{l_{node}}{l_{node}/\alpha} = \alpha
> $$
>
> Evaluating the magnitude:
>
> $$
> \alpha \approx 0.007297
> $$
>
> Because $0.007 \ll \sqrt{2\alpha}$ (the $\approx 0.121$ boundary between Linear Regime I and Saturation Regime II), electron-electron repulsion operates deep within the perfectly linear, Hookean domain of the LC network. Non-linear saturated impedance corrections are entirely unnecessary; standard linear Coulomb electrostatics mapped onto topological geometries apply exactly.

### Multi-Electron Repulsion: Topological Subshell Impedance Cascade

In standard approaches, peer-electron Coulomb repulsion involves time-averaging spatial probability densities via $N$-body continuous integration. Introducing such integrals into AVE is a methodological contamination that artificially recovers the macroscopic shielding collapse.

The framework requires a strictly scale-invariant, 0-parameter resolution. By treating atomic orbitals as nested macroscopic cavities rather than overlapping probability clouds, peer interactions are dictated by the **Subshell Impedance Cascade** (see Chapter [Section Removed] for the complete derivation).

Instead of continuous integration, the discrete lattice geometry enforces:

1. **Cross-Shell Gauss Screening (Axiom 2):** Outer solitons perceive exact stepwise integer screening $Z_{\rm net}(r) = Z - N_{\rm inner}$.
2. **Same-Shell Topologic Node Sorting (Axiom 4):** Electrons within the same principal shell ($n$) couple exclusively as discrete geometric LC resonators subject to the $K = 2G$ topological limit and the $8\pi\alpha$ spatial packing fraction.

This pure discrete formalism flawlessly bounds multi-electron systems without resorting to empirical variables, $Z_{\rm eff}$ fitting, or continuous variational probability integrals.

> ↗ See also: [Ch. 7: Quantum Mechanics and Orbitals](../../quantum-orbitals/ch07-quantum-mechanics/index.md) --- complete derivation of the subshell impedance cascade

---

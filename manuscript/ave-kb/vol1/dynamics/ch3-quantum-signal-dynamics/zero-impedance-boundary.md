[↑ Ch.3 Quantum and Signal Dynamics](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-2dwzib, clm-lv3uw1, clm-b9eura]
-->

## Section 3.3: Wave-Particle Duality and The Zero-Impedance Boundary
<!-- claim-quality: clm-2dwzib -->

The framework asserts that subatomic particles are topological knots where the spatial LC metric reaches dielectric saturation. Two distinct thresholds govern this process:

- **The Kinetic Yield Limit** ($E_k = \sqrt{\alpha} \cdot m_e c^2 \approx 43.65 \text{ keV}$, equivalently the field threshold $V_{yield} = \sqrt{\alpha}\,V_{snap} \approx 43.65$ kV): the threshold where non-linear saturation effects become dominant and the soliton begins to self-confine.
- **The Absolute Snap Limit** ($V_{snap} = m_e c^2 / e \approx 511 \text{ kV}$): the maximum inter-node potential difference before the lattice structurally ruptures (derived in Chapter 2).

The kinetic yield governs mass assembly and confinement; the snap limit governs dielectric breakdown and pair production. The Transmission Line mathematics of the saturation boundary provide a derivation of the physical origin of solid matter and wave-particle duality.

> **Reconciliation with Ch.7 regime map.** Ch.7 places $r_3 = 1.0$ at this same $V_{yield} = 43.65$ kV boundary and describes it as ``Regime IV: topology destroyed.'' The two descriptions refer to the *same* phase transition viewed from opposite sides:
> - From a *trapped* mode below the boundary: the saturating LC reaches $Z \to 0$, $\Gamma \to -1$, the wave reflects inward → standing wave = stable rest mass (**matter assembly** picture).
> - From a *propagating* mode crossing the boundary: the lattice's dielectric ruptures, $\varepsilon_{eff} \to 0$, the topology of any existing knot is destroyed and the energy radiates as a transverse wave or a pair (**topology destroyed** picture).
>
> One transition, two faces: matter forms at $V_{yield}$ from sub-threshold trapping; matter dissolves at $V_{yield}$ when super-threshold coupling drives the local lattice through the same Axiom 4 saturation. There is no contradiction.

<!-- Figure: fig:double_slit_comparison — Wave-Particle Duality: SM vs AVE Interpretations. (Left) The Standard Model models the particle abstractly as a probability wave passing through both slits simultaneously. (Right) The AVE framework models the particle as an objective localized topological defect passing through one slit, while its physical macroscopic hydrodynamic strain (the "Dark Wake") passes through both, causing classic continuous mechanical interference at the detector. -->

### The $0 \ \Omega$ Boundary Condition

The surrounding relaxed vacuum has a characteristic impedance $Z_{vac} \approx 377 \ \Omega$. At the saturated core of the localised knot, the LC nodes can no longer support alternating transverse displacement, so the effective dynamic RF impedance drops to $0 \ \Omega$ (an RF short circuit).

In transmission line theory, when a wave hits an impedance boundary, the ratio of reflected energy is governed strictly by the Reflection Coefficient ($\Gamma$):

> **[Resultbox]** *Transmission Line Reflection*
>
> $$
> \Gamma = \frac{Z_{knot} - Z_{vacuum}}{Z_{knot} + Z_{vacuum}}
> $$

By evaluating the ratio at the saturated knot boundary ($Z_{knot} = 0 \ \Omega$):

> **[Resultbox]** *The Absolute Impedance Boundary*
>
> $$
> \Gamma = \frac{0 - 377}{0 + 377} = \mathbf{-1}
> $$

A Reflection Coefficient of $-1$ signifies total reflectance.

### Internal Confinement and Matter Assembly
<!-- claim-quality: clm-lv3uw1 -->

Because the boundary of the saturated knot represents a steep impedance gradient dropping to $0 \ \Omega$, any acoustic energy circulating *inside* the knot is fully reflected inward. A subatomic particle in this model is a stable, self-sustaining acoustic standing wave trapped inside a spherical $0 \ \Omega$ impedance boundary of its own geometric creation.

### Scattering and The Pauli Exclusion Principle
<!-- claim-quality: clm-b9eura -->

Conversely, when an external wave (such as a photon) travels through the $377 \ \Omega$ relaxed vacuum and encounters the knot, it meets the same $0 \ \Omega$ boundary. The photon cannot penetrate the saturated volume; it experiences total reflection.

This transmission line mismatch provides a mechanical basis for the **Pauli Exclusion Principle** and the concept of cross-sectional area in particle physics. Two saturated knots cannot occupy the same spatial coordinates because their respective $0 \ \Omega$ boundaries reflect each other's inductive phase energy. Solid matter emerges from vacuum wave mechanics through macroscopic impedance reflection.

---

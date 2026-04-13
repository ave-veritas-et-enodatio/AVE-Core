[↑ Ch.5: Geometric Triodes](./index.md)
<!-- leaf: verbatim -->

# Derivation of the Strain Superposition Rule from Axiom 1

## The LC Lattice Constitutive Equations

Axiom 1 establishes the vacuum as a distributed LC resonant network with impedance $Z_0 = \sqrt{\mu_0/\varepsilon_0}$. Each spatial volume element $dV$ supports an independent inductive degree of freedom (associated with $\mathbf{B}$) and a capacitive degree of freedom (associated with $\mathbf{D}$). The energy density of the medium is:

$$u = \frac{1}{2}\mu_0 |\mathbf{H}|^2 + \frac{1}{2}\varepsilon_0 |\mathbf{E}|^2$$

The two field components are *independent* in the linear regime: a longitudinal ($\hat{x}$-directed) propagating wave and an orthogonal transverse ($\hat{y}$-directed) static field coexist in the same spatial volume without direct coupling at the field-equation level.

## Scalar Amplitude and Metric Strain

For the purpose of evaluating Axiom 4, the relevant quantity is not the vectorial electric field but the total scalar *metric strain amplitude* $V_{total}$ at a point. This is defined as the effective amplitude that the Axiom 4 saturation kernel experiences. Because energy is a Lorentz scalar and the metric distortion depends on the total energy density at that point:

$$u_{total} = u_{lon} + u_{tr} = \frac{1}{2}\varepsilon_0 V_{lon}^2 + \frac{1}{2}\varepsilon_0 V_{gate}^2$$

Since both share the same $\frac{1}{2}\varepsilon_0$ prefactor, the total equivalent scalar strain amplitude driving Axiom 4 is:

$$\boxed{V_{total} = \sqrt{V_{lon}^2 + V_{gate}^2}}$$

This is the Pythagorean quadrature sum of two orthogonal field components. It follows from energy additivity of two perpendicular degrees of freedom — not from geometric intuition. The factor $\sqrt{2}$ does not appear because each component carries half the energy density of a single-axis field of magnitude $V_{total}$; the quadratic relationship is exact given the $|\mathbf{E}|^2$ energy dependence.

This equation is the foundational result of the Geometric Triode. It shows that a static transverse field $V_{gate}$ elevates the total metric strain at the channel intersection *without injecting any longitudinal current*, which is the direct axiom-derived analog of FET gate-capacitor action.

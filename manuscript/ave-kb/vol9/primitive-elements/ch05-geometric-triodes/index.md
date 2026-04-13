[↑ Primitive Elements](../index.md)

# Ch.5: The Geometric Triode (Vacuum Transistor)

Derives the strain-superposition rule governing the Geometric Triode rigorously from the Axiom 1 LC lattice and the Axiom 4 saturation kernel. Proves that purely transverse static strain is sufficient to drive the longitudinal impedance to infinity, replicating MOSFET pinch-off without chemical doping. Derives the transconductance $g_m$ analytically and establishes the three operating regimes.

## Key Results

| Result | Statement |
|---|---|
| Quadrature Strain Superposition | $V_{total} = \sqrt{V_{lon}^2 + V_{gate}^2}$ — from energy additivity of orthogonal Axiom 1 LC field components |
| Drain Current | $I_D(V_{gate}) = I_{D0}\sqrt{1 - (V_{lon}^2 + V_{gate}^2)/V_{snap}^2}$ — exact Axiom 4 kernel evaluation |
| Transconductance | $g_m = -I_{D0} V_{gate}/(V_{snap}^2 \cdot S)$ — zero free parameters, derived analytically |
| Pinch-Off Condition | $V_{gate}^2 + V_{lon}^2 \geq V_{snap}^2$ — universal yield from Axiom 4 (vs. doping-dependent $V_{th}$ in MOSFET) |
| Scale Invariance | $I_D \propto S(V_{total}/V_{snap})$ is mathematically identical to the quark confinement operator (Vol 2) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Quadrature Strain Superposition](./quadrature-strain-superposition.md) | Derivation from Axiom 1 LC constitutive equations; energy density argument; Pythagorean quadrature sum |
| [Transconductance Gain](./transconductance-gain.md) | Saturation kernel application, effective impedance/admittance, analytic $g_m$ formula, three operating regimes, MOSFET comparison |
| [Triode JAX Validation](./triode-jax-validation.md) | Transconductance curves for multiple $V_{lon}/V_{snap}$ ratios; simulation confirmation of analytic formulas |

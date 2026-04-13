[↑ Ch.8: Static Soliton Kinks](./index.md)
<!-- leaf: verbatim -->

# Sine-Gordon Derivation from Axiom 4

Starting from the 1D wave equation with a nonlinear restoring force $F_{nl}(\phi)$:

$$\frac{\partial^2 \phi}{\partial t^2} = \frac{\partial^2 \phi}{\partial x^2} - F_{nl}(\phi)$$

Axiom 4 demands that the nonlinear restoring force must satisfy two conditions:
1. **Periodicity:** The vacuum LC lattice has $2\pi$ phase periodicity; the restoring force must be periodic in $\phi$.
2. **Zero at equilibrium:** $F_{nl}(0) = 0$ (no restoring force at the vacuum ground state).

The unique smooth periodic function satisfying both conditions is the sine function, yielding the topological potential:

$$V_{topo}(\phi) = \omega_0^2 (1 - \cos\phi)$$

The corresponding equation of motion is the **sine-Gordon equation**:

$$\boxed{\frac{\partial^2 \phi}{\partial t^2} - c_0^2 \frac{\partial^2 \phi}{\partial x^2} + \omega_0^2 \sin\phi = 0}$$

## Static Kink Solution

Setting $\partial\phi/\partial t = 0$ for the static case and solving the resulting ODE yields the kink solution:

$$\phi(x) = 4\arctan(e^{\gamma x})$$

where $\gamma = \omega_0/c_0$ is the inverse kink width. This solution:
- Interpolates smoothly between $\phi = 0$ (vacuum) and $\phi = 2\pi$ (next vacuum)
- Has topological charge $Q = [\phi(+\infty) - \phi(-\infty)]/(2\pi) = 1$
- Is topologically stable: $Q$ is an integer invariant that cannot change via continuous deformations
- Satisfies the same sine-Gordon equation governing nuclear solitons (Vol 2), demonstrating Axiom 4 scale invariance

> **[Resultbox]** *Chapter 8 Summary*
>
> The sine-Gordon equation is derived from Axiom 4 applied to the 1D waveguide wave equation: the nonlinear restoring force must be periodic (matching the $2\pi$ phase periodicity of the vacuum LC lattice), and the unique smooth solution is the sine potential. Static kink solutions provide topologically stable, non-volatile memory states requiring discrete topology-flipping events to write or erase.

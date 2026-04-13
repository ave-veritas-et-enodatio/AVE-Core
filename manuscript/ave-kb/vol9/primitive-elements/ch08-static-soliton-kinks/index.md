[↑ Primitive Elements](../index.md)

# Ch.8: Static Soliton Kinks (Topological Memory)

Derives the sine-Gordon equation from Axiom 4 applied to the 1D waveguide wave equation. The nonlinear restoring force must be periodic (matching the $2\pi$ phase periodicity of the vacuum LC lattice), yielding the sine-Gordon potential. Static kink solutions $\phi(x) = 4\arctan(e^{\gamma x})$ provide topologically stable, non-volatile memory states bounded between total-reflection mirrors.

## Key Results

| Result | Statement |
|---|---|
| Sine-Gordon Equation | $\partial^2\phi/\partial t^2 - c_0^2\,\partial^2\phi/\partial x^2 + \omega_0^2\sin\phi = 0$ — from Axiom 4 |
| Topological Potential | $V_{topo}(\phi) = \omega_0^2 (1 - \cos\phi)$ — periodic restoring force |
| Static Kink Solution | $\phi(x) = 4\arctan(e^{\gamma x})$ — stable topological defect with $Q = 1$ |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Sine-Gordon Derivation](./sine-gordon-derivation.md) | Axiom 4 → nonlinear wave equation → sine-Gordon; topological potential; static kink |
| [Write-Read Protocol](./write-read-protocol.md) | Kink creation (writing), photon readout (reading), erasure (Landauer phonon) |
| [Soliton JAX Validation](./soliton-jax-validation.md) | Simulation of kink stability and scattering resilience |

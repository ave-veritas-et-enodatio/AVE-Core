[↑ Vol 9: Axiomatic Hardware](../index.md)

# Primitive Elements

The seven individual VCA hardware components derived from first principles. Each element replaces a classical semiconductor component with a passive waveguide topology governed exclusively by Axioms 1–4. Geometric Diodes replace P-N junctions via asymmetric trace saturation; Geometric Triodes replace MOSFETs via transverse strain superposition; Dielectric Delay Lines replace RC networks via corrugated slow-wave structures; Strain Reservoirs replace capacitors via expanded compliance cavities; Static Soliton Kinks replace Flash memory via sine-Gordon topological knots; Axiomatic Transducers match the $50\,\Omega$ external domain to the $376.73\,\Omega$ VCA vacuum; Topological Pumps replace DC power supplies with continuous-wave master oscillators.

## Key Results

| Result | Statement |
|---|---|
| Geometric Diode | Asymmetric trace: $\Gamma \to -1$ total reflection via $S(V) \to 0$ when constriction forces $V_2 > V_{snap}$ [Ch.4](./ch04-geometric-diodes/dielectric-rupture-gating.md) |
| Quadrature Strain Superposition | $V_{total} = \sqrt{V_{lon}^2 + V_{gate}^2}$ — energy additivity of orthogonal LC field components [Ch.5](./ch05-geometric-triodes/quadrature-strain-superposition.md) |
| Geometric Triode Transconductance | $g_m = -I_{D0} V_{gate} / (V_{snap}^2 \cdot S)$ — exact analytic, zero free parameters [Ch.5](./ch05-geometric-triodes/transconductance-gain.md) |
| Slow-Wave Phase Velocity | $v_{ph} = 1/\sqrt{L'C'}$ — corrugated waveguide retards phase without scattering [Ch.6](./ch06-dielectric-delay-lines/slow-wave-derivation.md) |
| Strain Reservoir Impedance | $Z_{res} = Z_0/\beta$ with $\beta = w_{res}/w_0$ — wide section stores energy at reduced impedance [Ch.7](./ch07-strain-reservoirs/klopfenstein-reservoir-profile.md) |
| Sine-Gordon Equation | $\partial^2\phi/\partial t^2 - c_0^2\,\partial^2\phi/\partial x^2 + \omega_0^2\sin\phi = 0$ — derived from Axiom 4 applied to 1D wave equation [Ch.8](./ch08-static-soliton-kinks/sine-gordon-derivation.md) |
| Transducer Step Reflection | $\Gamma_{step} = 0.766$, reflecting 58.7% of incident power; Klopfenstein taper reduces to $< 0.01\%$ [Ch.9](./ch09-axiomatic-transducers/impedance-matching-proof.md) |
| Topological Pump Power | $P_{pump} = \frac{1}{2}\int_A \rho_{inertia}\,\omega^2\,|S_{pump}|^2 \cdot v_{phase}\,dA$ [Ch.10](./ch10-topological-pumps/continuous-wave-injection.md) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Ch.4: Geometric Diodes](./ch04-geometric-diodes/index.md) | Dielectric rupture gating, bottleneck proof ($\Gamma \to -1$), forward/reverse bias regimes |
| [Ch.5: Geometric Triodes](./ch05-geometric-triodes/index.md) | Strain superposition from Axiom 1, transconductance from Axiom 4, three operating regimes, MOSFET comparison, scale invariance |
| [Ch.6: Dielectric Delay Lines](./ch06-dielectric-delay-lines/index.md) | Telegraphist equations, slow-wave derivation, group velocity preservation, dispersion analysis |
| [Ch.7: Strain Reservoirs](./ch07-strain-reservoirs/index.md) | Klopfenstein-tapered wide-section waveguide, energy density derivation, impedance design |
| [Ch.8: Static Soliton Kinks](./ch08-static-soliton-kinks/index.md) | Sine-Gordon derivation from Axiom 4, static kink solution, write/read protocol |
| [Ch.9: Axiomatic Transducers](./ch09-axiomatic-transducers/index.md) | $50\,\Omega \to 376.73\,\Omega$ impedance matching, Klopfenstein taper profile, passband design |
| [Ch.10: Topological Pumps](./ch10-topological-pumps/index.md) | Continuous-wave PDN replacement, master oscillator manifolds, structural power bounding |

[↑ Circuit Theory](../index.md)
<!-- claim-quality (subtree): i9l284, kezk9z, p5cf3t, pp3qwf, u462e4, v6ti0v, vjv4zf -->

# Ch.1 Vacuum Circuit Analysis

The Vacuum Circuit Analysis (VCA) framework establishes a single, exact dimensional isomorphism between continuum spatial mechanics and electrical network theory via the Topological Conversion Constant $\xi_{topo} \equiv e/\ell_{node}$. From this mapping, all six rows of the circuit-mechanical translation table are derived, the non-linear constitutive models for extreme-field regimes are established, and the characteristic impedance $Z_0 = 376.73\;\Omega$ is shown to emerge from the discrete LC ladder of the lattice.

## Key Results

| Result | Statement |
|---|---|
| Topological Conversion Constant | $\xi_{topo} \equiv e/\ell_{node} \approx 4.149 \times 10^{-7}$ C/m |
| Charge--Displacement | $Q = \xi_{topo}\, x$ |
| Current--Velocity | $I = \xi_{topo}\, v$; $I_{max} = \xi_{topo}\, c \approx 124.4$ A |
| Voltage--Force | $V = \xi_{topo}^{-1}\, F$; $V_{snap} = 511$ kV |
| Inductance--Mass | $L = \xi_{topo}^{-2}\, m$ |
| Capacitance--Compliance | $C = \xi_{topo}^{2}\, \kappa$ |
| Resistance--Viscosity | $R = \xi_{topo}^{-2}\, \eta$ |
| Vacuum Varactor | $C_{eff}(V) = C_0 / \sqrt{1 - (V/V_{yield})^2}$, $V_{yield} \approx 43.65$ kV |
| Relativistic Inductor | $L_{eff}(I) = L_0 / \sqrt{1 - (I/I_{max})^2}$ |
| TVS Transition | $\eta_{eff} = 0$ for $V \geq V_{yield}$ (zero-impedance slipstream) |
| Per-Cell Elements | $L_{cell} = \mu_0\, \ell_{node}$, $C_{cell} = \epsilon_0\, \ell_{node}$ |
| Scale-Invariant $Z_0$ | $Z_{cell} = \sqrt{\mu_0/\epsilon_0} \equiv Z_0 \approx 376.73\;\Omega$ |
| Propagation velocity | $v_g = 1/\sqrt{\mu_0 \epsilon_0} \equiv c$ |
| IM3 frequencies | $f_{IM3} = 2f_1 - f_2$ and $2f_2 - f_1$ |
| IP3 | $V_{IP3} = \sqrt{4/3}\; V_{yield} \approx 50.4$ kV |
| Particle confinement | $\Gamma = -1$ at saturated boundary ($Z_{core} \to 0\;\Omega$) |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Topological Kinematics](topological-kinematics.md) | Six-row topo-kinematic identity derivation; $\xi_{topo}$; self-consistency checks |
| [Nonlinear Vacuum Capacitance](nonlinear-vacuum-capacitance.md) | Metric varactor; vacuum memristor; thixotropic relaxation; skin depth |
| [Z0 Derivation](z0-derivation.md) | Discrete LC ladder; $Z_0$ scale invariance; gravitational stealth; black hole echoes |
| [Relativistic Inductor](relativistic-inductor.md) | Current-dependent inductance; $E = mc^2$ from inductor energy; SPICE enforcement of $c$ |
| [TVS Transition](tvs-transition.md) | Solid-to-slipstream phase transition as TVS Zener diode |
| [Resonant LC Solitons](resonant-lc-solitons.md) | Particles as LC tanks; Virial theorem; total internal reflection; Pauli exclusion |
| [Orbital Friction Paradox](orbital-friction-paradox.md) | Real vs. reactive power; lossless orbit as LC tank at $\theta = 90°$ |
| [Intermodulation Distortion](intermodulation-distortion.md) | Vacuum IMD spectroscopy; IM3 prediction; IP3 derivation; QED comparison |
| [Translation Circuit](translation-circuit.md) | Cross-reference to common translation table |
| [Solver Selection](solver-selection.md) | FDTD vs K4-TLM decision matrix, boundary conditions, default yield thresholds |

> **Note:** `summarybox` and `exercisebox` environments in the source chapter are not extracted as leaves in this KB.

---
| [Computational Solver Selection](./computational-solver-selection.md) | Computes Solvers FDTD vs TLM |

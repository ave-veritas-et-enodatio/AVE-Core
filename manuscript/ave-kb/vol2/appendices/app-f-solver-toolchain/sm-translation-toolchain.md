[↑ App F: Universal Solver Toolchain](./index.md)
<!-- leaf: verbatim -->

## Standard Model Translation

### General Relativity

| AVE Descriptor | Standard GR | Engine Function |
|---|---|---|
| $n(r) = 1/(1 - r_s/r)$ | Schwarzschild lapse | `gw_propagation.refractive_index` |
| $Z(r) \equiv Z_0$ | (No analogue) | `gw_propagation.gravitational_impedance` |
| $c_{\mathrm{local}} = c/n(r)$ | Coordinate speed | `gw_propagation.gw_local_speed` |
| $S_{\mathrm{grav}}(\varepsilon_{11})$ | (Not in GR) | `gravity.gravitational_saturation_factor` |
| $\nu_{\mathrm{vac}} = 2/7$ | (Not in GR) | `constants.NU_VAC` |
| $\varepsilon_{11} = 7M_g/r$ | (Not in GR) | `gravity.principal_radial_strain` |
| $V_{\mathrm{SNAP}}$ | Planck energy (approx) | `constants.V_SNAP` |

### Quantum Mechanics and Atomic Physics

| AVE Descriptor | Standard QM | Physical Origin / Engine Function |
|---|---|---|
| Acoustic Bulk Modulus Cavity | Atomic Orbital | The electron is an impedance mismatch ($\Gamma=-1$) that traps a longitudinal wave, bouncing at $E=V(r)$. |
| Phase-Locking Integer ($\int n\, dr$) | Principal Quantum Number ($n$) | The WKB resonance condition for a lossless acoustic standing-wave matching $n$ half-wavelengths. |
| $0_1$ Topological Unknot | Point-particle Electron | A closed flux loop at minimum ropelength (Axiom 1). The rest mass $m_e$ is its ground state tension. |
| $0_1$ Strain Field $\rho_{unknot}(r)$ | $1s$ Probability Cloud $\psi^*\psi(r)$ | The spatial deformation of the vacuum around the unknot. It is NOT probability; it is deterministic structural strain bounded by the Weak interaction ($M_W$). |
| Inner Impedance Bumps | Core Electron Shells ($Z_{eff}$) | Filled standing waves alter the background voltage gradient $V_{total}(r)$, perturbing the refractive index for outer valence electrons. |
| Outermost Mode Eigenvalue | Ionization Energy (IE) | Evaluated via `coupled_resonator.atomic_resonance` |

---

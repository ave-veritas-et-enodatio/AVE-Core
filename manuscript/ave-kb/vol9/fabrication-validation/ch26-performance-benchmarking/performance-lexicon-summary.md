[↑ Ch.26: Performance Benchmarking](./index.md)
<!-- leaf: verbatim -->

# Unified AVE Performance Lexicon

| Classical Metric | Classical Formula | AVE Name | AVE Symbol & Formula | Physical Meaning |
|---|---|---|---|---|
| Clock Speed | $f = f_{crystal}$ | Carrier Coherence Frequency | $f_{CC} = c_0 / 2L\sqrt{\kappa}$ | Cavity eigenfrequency; clock IS geometry |
| Power Dissipation | $P = I^2 R$ | Viscous Drag Loss | $P_{drag} = \omega\mu\kappa\tan\delta\int|S|^2 dV$ | Molecular rotational friction; scales with $\omega$ |
| IPC | Pipeline width | Spatial Opcode Multiplicity | $M_{GISA}$ = harmonic basis cardinality | Simultaneous diffracting opcode channels |
| Cache Latency | $\tau = RC$ | Focal Lock Time | $\tau_{lock} = 1/(\kappa_c|S_p|/|S_l|)$ | Adler convergence speed to focal node |
| Bit Error Rate | $P_{flip}$ | Phase Coherence Yield | $\eta_{PY} = 1 - P(\Delta\phi > \pi/10)$ | Fraction of paths inside coherence envelope |
| Memory Bandwidth | GB/s | Focal Refresh Rate | $\mathcal{F}_{snap} \leq f_{CC}$ | Phase scan rate across MUX perimeter |
| Transistor Count/mm² | Moore's Law | Topodynamic Node Density | $\rho_{kink} = 1/\xi_{kink}^2$ | Stable soliton kinks per unit area |
| Supply Voltage $V_{DD}$ | DC rail | Carrier Injection Fraction | $\xi_{inj} = |S_{pump}|/V_{snap}$ | Operating fraction of dielectric rupture limit |
| Leakage Current | $I_{sub-Vth}$ | Ambient Phase Bleed | $\delta\phi_{amb} = \int(\omega\Delta\kappa/2c_0\sqrt{\kappa})dx$ | Drift from substrate non-uniformity |
| Noise Margin | $V_{NM}$ | Adler Restoration Headroom | $\mathcal{H}_{lock} = \arcsin(\Delta k/\kappa_c)_{max}$ | Max corrupt phase self-correctable passively |

> **[Resultbox]** *Chapter 26 Summary*
>
> Every classical semiconductor performance metric is a degenerate special case of a deeper topological invariant. Power dissipation is not $I^2R$ — it is Viscous Drag, scaling with frequency, not amplitude. Clock speed is not an external crystal — it is the eigenfrequency of a geometric resonance cavity. IPC is not a pipeline width — it is the cardinality of the physical harmonic basis simultaneously diffracting through the Tensor Plate.

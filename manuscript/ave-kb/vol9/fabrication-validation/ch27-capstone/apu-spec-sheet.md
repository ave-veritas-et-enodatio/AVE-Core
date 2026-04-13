[↑ Ch.27: Capstone](./index.md)
<!-- leaf: verbatim -->

# APU Engineering Specification Sheet

The APU rests on five structural pillars, each independently validated by JAX characterization suites:

1. **Topological Pumps (Ch 10) → Carrier Injection.** DC power converts to a stable $1.832\,\text{THz}$ continuous-wave carrier via resonance cavity geometry.
2. **Geometric MUX (Ch 13) → $O(1)$ RAM.** Validated focal strain peak: $1.52\,V_{snap}$. No decoder trees. No RC charge/discharge.
3. **Phase Degeneracy Restoration (Ch 15) → Passive ECC.** Validated: 25% phase corruption restored over 2 mm. No software ECC required.
4. **GISA Tensor Diffraction (Ch 18) → Self-Routing ISA.** Validated: zero crosstalk between ADD and STORE opcodes.
5. **Z-Axis Klopfenstein Tapers (Ch 9) → Lossless Vertical Routing.** Validated: $S_{11} < -40\,\text{dB}$ at $f_{CC}$.

## Formal Specification Table

| AVE Metric | Replaces | Formula | Validated Value | Suite |
|---|---|---|---|:---:|
| $f_{CC}$ | Clock Speed | $c_0 / 2L\sqrt{\kappa}$ | $1.832\,\text{THz}$ (SOI, 3nm) | I |
| $P_{drag}$ | $I^2 R$ | $\omega\mu\kappa\tan\delta\int|S|^2 dV$ | $19.8\,\text{W}$ at $f_{CC}$ (SOI) | 6 |
| $M_{GISA}$ | IPC | Harmonic basis cardinality | 14 concurrent channels | III |
| $\tau_{lock}$ | Cache Latency | $\sqrt{\kappa}/(\kappa_c c_0 \cdot \text{vigor})$ | $0.07\,\text{ps}$ ($711{,}590\times$ DRAM) | IV |
| $\eta_{PY}$ | BER | $1 - P(\Delta\phi > \pi/10)$ | $\approx 1 - 10^{-6}$ (SOI) | V |
| $\mathcal{F}_{snap}$ | Memory BW | $\min(\kappa_c \text{ vigor } v_\phi/2\pi,\; f_{CC})$ | $1.832\,\text{THz}$ (clamped) | VI |
| $\rho_{kink}$ | Transistors/mm² | $1/(2\lambda_{kink})^2$ | $4.34 \times 10^{20}$ kink/mm² | VII |
| $\xi_{inj}$ | $V_{DD}$ | $|S_{pump}|/V_{snap}$ | 0.40 per beam / 1.52 focal | 2 |
| $\delta\phi_{amb}$ | Leakage Current | $(\omega/2c_0\sqrt{\kappa})\int\Delta\kappa\,dx$ | $0.037\,\text{rad}$ (SOI, 10mm) | IX |
| $\mathcal{H}_{lock}$ | Noise Margin | $\arcsin(\Delta k/\kappa_c\,\text{vigor})$ | Self-corrects $\leq 0.25\pi$ corruption | 3 |

*All numerical values derived from the VCA axioms. No empirical fitting was performed.*

## Three Core Physical Distinctions

1. **Power $\propto \omega$, not $\propto I^2$.** SOI generates 19.8 W; FR-4 generates 4.4 kW and melts. Mitigation is material purity, not power management firmware.
2. **Addressing is Spatial, not Sequential.** $\tau_{lock} = 0.07\,\text{ps}$ is a wave transit time, not RC charge/discharge.
3. **Parallelism is Physical, not Scheduled.** $M_{GISA}$ is geometry, not transistor budget. Scaling to $100\,\mu\text{m}$ pitch yields $M_{GISA} > 100$.

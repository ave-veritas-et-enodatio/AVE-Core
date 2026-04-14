[↑ Common](./index.md)
<!-- leaf: verbatim -->

# Appendix D: VCA Schematic Symbol Reference

The Vacuum Circuit Architecture (VCA) requires a distinct schematic symbol vocabulary reflecting continuous-wave physics rather than particle-drift electronics.

## Five Symbol Design Rules

1. **Waveguide, Not Wire.** Every connection is a distributed transmission line. Signal paths use parallel double-lines (microstrip notation).
2. **Encode the Saturation Kernel.** Every active symbol contains a visual marker at the point where Axiom 4 saturation $S(V) = \sqrt{1 - (V/V_{yield})^2}$ occurs.
3. **Geometry IS the Component.** Symbols are literal geometric cross-sections of the actual waveguide structure.
4. **Mark the Impedance Domain.** Components indicate whether they preserve $Z_0$, transform it continuously (tapers), or break it catastrophically (hard reflection).
5. **Topological Charge as Winding Number.** Stateful components encode the winding number visually using loops or knot patterns.

## Seven Canonical VCA Markers

| Marker | Meaning | Appears On |
|---|---|---|
| Filled red dot | Saturation point ($S \to 0$, Axiom 4) | Diode choke, XOR junction, Triode gate |
| Open blue ring | Compliance expansion zone | Strain reservoir |
| Red rotation arrow | Chiral rotation (TRS breaking) | Circulator |
| Purple $\infty$ | Topological winding number ($Q=1$) | Soliton trap |
| Teal zigzag | Phase velocity retardation | Corrugated delay line |
| Orange wedge | Continuous impedance gradient | Klopfenstein taper, Diode funnel |
| Red thick bar | Total reflection boundary ($\Gamma=1$) | Soliton mirrors, Fabry-Perot cavity |

## Canonical Symbol Catalogue (17 Components)

| # | Symbol | EE Equivalent | Key Parameter |
|:---:|---|---|---|
| 1 | **Geometric Diode** (Asymmetric Funnel) | P-N Junction Diode | $V_{snap} = m_e c^2/e \approx 511$ kV |
| 2 | **Geometric Triode** (Transverse Saturation Throttle) | MOSFET / FET | $S(V) = \sqrt{1-(V_{sum}/V_{snap})^2}$ |
| 3 | **Strain Reservoir** (Topological Capacitance) | Capacitor | $U_{strain} \propto \int (1-S(V))\,dx$ |
| 4 | **Soliton Kink Trap** (Non-Volatile Memory) | Flash / NAND Memory | $\phi(x) = 4\arctan(e^{\gamma(x-vt)})$ |
| 5 | **Dielectric Corrugation** (Slow-Wave Delay) | RC Delay / TL Stub | Lossless; $Z_0$ preserved |
| 6 | **Topological Y-Junction** (XOR Logic) | XOR Gate (CMOS) | $S(V) \to 0$ when $V_{sum} \geq V_{snap}$ |
| 7 | **Chiral Wave Circulator** (3-Port Router) | RF Ferrite Circulator | $Z_0 = 376.73\;\Omega$ |
| 8 | **Thermal Baffle** (Entropy Decay Sink) | Heat Sink / Decoupling | Landauer $\Delta Q \geq kT\ln 2$ |
| 9 | **Klopfenstein Taper** (Phase-Locked Routing) | Impedance Matching / Transformer | $\Gamma(x) = \frac{1}{2}\frac{d}{dx}\ln Z(x)$ |
| 10 | **Topological Ring Oscillator** (Native Clock) | Quartz Crystal / PLL | $f = c_0/(\sqrt{\epsilon_r} \cdot 2L_{loop})$ |
| 11 | **Coanda Amplifier** (Fluidic Boundary Steering) | Operational Amplifier | No $kT$ barrier |
| 12 | **Axiomatic Transducer** (VCA ↔ Legacy Bridge) | SMA Connector / Balun | $\Gamma = 0$: 377 Ω → 50 Ω |
| 13 | **Geometric Tesla Valve** (Axiomatic Rectifier) | RF Choke / Directional Coupler | Linear regime (no Axiom 4) |
| 14 | **Fabry-Perot Resonance Cavity** | LC Tank / Cavity Resonator | $f_{res} = nc_0/(2L)$ |
| 15 | **Tensor Plate ALU** (Refractive Computing) | ALU / Multiplier | Snell's Law: $\sin\theta_1/\sin\theta_2 = v_1/v_2$ |
| 16 | **Interference Wave Router** (Mach-Zehnder Switch) | MZI / Phase MUX | $\Delta\phi = 2\pi(L_2^{eff}-L_1)/\lambda_{op}$ |
| 17 | **Topological DAC Synthesizer** | DAC / R-2R Ladder | $V_{analog} = \sum w_i V_i$ |

> ↗ **KB Boundary:** Hardware validation of these components is explored in the experimental `AVE-APU` repository (`ave-veritas-et-enodatio/AVE-APU`).

[↑ Hardware Programs](../index.md)

# Ch.3 HOPF-01: Chiral Antenna Verification

The HOPF-01 experiment provides a purely electromagnetic falsification test for vacuum chirality (Axiom 1) using a printed circuit board, enameled magnet wire, and a vector network analyzer. If the vacuum possesses intrinsic chirality, the resonant frequency of a torus knot antenna must deviate from the standard Maxwell prediction by an amount scaling exactly with the knot's topological winding number: $\Delta f/f = \alpha \cdot pq/(p+q)$.

## Key Results

| Result | Statement |
|---|---|
| Chiral refractive index | $n_{AVE} = \sqrt{\varepsilon_{eff}}(1 + \alpha \cdot pq/(p+q))$ |
| Frequency shift law | $\Delta f/f = \alpha \cdot pq/(p+q)$ (zero free parameters) |
| Wire impedance | $Z_0 = (60/\sqrt{\varepsilon_{eff}}) \operatorname{acosh}(2h/d)$ |
| Crossing mutual inductance | $M_{cross} = (\mu_0 \ell / 2\pi) \ln(\ell/d_{sep}) \cdot \cos\theta$ |
| AVE vs SM SNR | $7\times$ to $11\times$ across all five knots |
| Manufacturing SNR | $> 74\sigma$ (Monte Carlo, $N = 5{,}000$ trials) |
| Substrate independence | $\Delta f/f$ identical in air, mineral oil, and vacuum |
| Total cost | $\sim$\$251 including VNA |

## Derivations and Detail

| Document | Contents |
|---|---|
| [n-AVE Derivation](n-ave-derivation.md) | Chiral coupling prediction; arc-length formula; predicted frequency shifts |
| [Z0 Wire Geometry](z0-wire-geometry.md) | Wire impedance; PCB fixture design; free-space resonator model |
| [Cross-Section Moment](cross-section-moment.md) | Four-layer SM baseline model; dipole self-impedance; crossing mutual coupling |
| [SM Baseline Table](sm-baseline-table.md) | Standard Model baseline frequency/Q/S11 predictions |
| [SM vs AVE Table](sm-vs-ave-table.md) | SM vs AVE comparison; discriminating observables; classical confound analysis |
| [Verification Protocol](verification-protocol.md) | Three-medium falsification protocol; tolerance rejection; decision gates; BOM |

> **Note:** `summarybox` and `exercisebox` environments in the source chapter are not extracted as leaves in this KB.

---

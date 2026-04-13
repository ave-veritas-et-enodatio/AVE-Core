[↑ Hardware Programs](../index.md)

# Ch.5 PONDER-05: DC-Biased Quartz Thruster

The PONDER-05 configuration accesses Axiom 4's nonlinear dielectric regime by applying a static 30 kV DC bias across a quartz cylinder, overlaid with a modest 500 V AC perturbation at 50 kHz. The DC bias holds the material at 68.7% of $V_{yield}$, where the effective vacuum permittivity has collapsed by 27.4% and the effective capacitance has risen by 37.7%. The $2V_{DC}V_{ac}$ cross-term provides $120\times$ linear amplification, yielding a predicted 469 $\mu$N thrust.

## Key Results

| Result | Statement |
|---|---|
| Saturation at 30 kV | $S = 0.726$; $\varepsilon_{eff}$ drops to 72.6%; $C_{eff}$ rises to 137.7% |
| DC cross-term amplification | $2V_{DC}/V_{ac} = 120\times$ |
| Predicted thrust | $469\;\mu$N at 30 kV DC + 500 V AC |
| Nonlinear phase velocity | $c_{phase}(V) \propto (1 - (V/V_{yield})^2)^{1/4}$ |
| Quarter-wave matching | Oil reduces reflected power from 12.9% to $\sim$0.03% |
| Thermal dissipation | $< 0.001$ mW (CW indefinite) |
| Total cost | $\sim$\$3,000 |

## Derivations and Detail

| Document | Contents |
|---|---|
| [DC Bias Mechanism](dc-bias-mechanism.md) | Nonlinear saturation regime; cross-term amplification derivation |
| [Quartz Resonator Model](quartz-resonator-model.md) | Quartz cylinder parameters; resonance frequency; drive configuration |
| [Nonlinear Permittivity](nonlinear-permittivity.md) | Rarefaction wave inversion; differential saturation parallax |
| [Drive Circuit Design](drive-circuit-design.md) | Mineral oil bath: corona suppression, impedance matching, thermal management |
| [Experimental Results](experimental-results.md) | Predicted thrust profile; bill of materials |

> **Note:** `summarybox` and `exercisebox` environments in the source chapter are not extracted as leaves in this KB.

---

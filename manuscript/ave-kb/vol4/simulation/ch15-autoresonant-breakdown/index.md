[↑ Vol 4: Simulation](../index.md)
<!-- claim-quality (subtree): 9sujp8 -->

# Ch.15: Autoresonant Dielectric Breakdown — Bypassing the Schwinger Limit

The $\mathcal{M}_A$ vacuum is a nonlinear dielectric LC lattice. Fixed-frequency high-intensity drives detune as the local capacitance drops under strain, reflecting power instead of breaching the yield limit. An autoresonant phase-locked loop (PLL) tracks the shifting resonance and pumps the metric past $60\,\text{kV}$ at a fraction of brute-force power.

## Key Results

| Result | Expression | Source |
|---|---|---|
| Nonlinear detuning | $C_{eff}(V) = C_0\sqrt{1 - (V/V_{yield})^2}$; fixed-frequency drive falls out of phase as $C_{eff}$ drops | theory |
| PLL bypass | Behavioral current source tracks instantaneous resonant frequency $f = 1/(2\pi\sqrt{LC_{eff}})$; maintains constructive interference through yield | theory |
| SPICE netlist | `pll_breakdown.cir` — behavioral capacitor + PLL integrator, $.param$ $V_{yield} = 60\,\text{kV}$ | netlist |

## Derivations and Detail

| Document | Contents |
|---|---|
| [Theory](theory.md) | Nonlinear $\mathcal{M}_A$ lattice detuning; fixed-frequency failure; autoresonant PLL solution |
| [SPICE Netlist](spice-netlist.md) | Verbatim `pll_breakdown.cir` netlist with behavioral sources |

> **Note:** `summarybox` and `exercisebox` environments in the source chapter are not extracted as leaves in this KB.

---

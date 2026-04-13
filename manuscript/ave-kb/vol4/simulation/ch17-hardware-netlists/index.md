[↑ Vol 4: Simulation](../index.md)

# Ch.17: Hardware Netlists — PONDER-01 and the EE Bench

Physical LTspice netlists for actual tabletop AVE hardware. These are engineering blueprints with component values derived directly from the zero-parameter framework. Ch.17 uses codebox environments only (no resultboxes).

## Key Results

| Result | Expression | Source |
|---|---|---|
| EE Bench capacitance rolloff | $C_{eff}(V) = C_0\sqrt{1 - (V/V_{yield})^2}$; anomaly window at $\sim 0.85 \times V_{yield}$ to $V_{yield}$; deviation $> 10\%$ from linear baseline | ee-bench |
| PONDER-01 boundary reflection | $\Gamma = (Z_{FR4} - Z_0)/(Z_{FR4} + Z_0) \approx -0.349$; $34.9\%$ reflection at every air/FR4 interface | ponder-01 |
| Component derivation | $V_{yield} = \sqrt{\alpha} \times m_e c^2/e$; $C_{AIR} = \varepsilon_0 A/d = 2.36\,\text{fF}$; $C_{FR4} = \varepsilon_r \varepsilon_0 A/d = 10.14\,\text{fF}$; $L_{AIR} = \mu_0 d/A = 0.33\,\text{nH}$ | ponder-01 |

## Derivations and Detail

| Document | Contents |
|---|---|
| [EE Bench Netlist](ee-bench-netlist.md) | Verbatim `ee_bench.cir` — behavioral charge equation for nonlinear vacuum capacitance under DC sweep to $45\,\text{kV}$ |
| [PONDER-01 Stack Netlist](ponder-01-stack-netlist.md) | Verbatim `ponder_01_stack.cir` — 20-layer alternating Air/FR4 LC ladder at $100\,\text{MHz}$, $30\,\text{kV}$ |

> **Note:** `summarybox` and `exercisebox` environments in the source chapter are not extracted as leaves in this KB.

---

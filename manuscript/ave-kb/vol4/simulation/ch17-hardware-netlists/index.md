[↑ Vol 4: Simulation](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [clm-vjv4zf]
subtree-experiments: []
-->

# Ch.17: Hardware Netlists — PONDER-01 and the EE Bench

Physical LTspice netlists for actual tabletop AVE hardware. These are engineering blueprints with component values derived directly from the zero-parameter framework. Ch.17 uses codebox environments only (no resultboxes).

> **🔴 SCOPE-CORRECTION (2026-06-15, zero-parameter register reconciliation; Rule 12 — the description above is preserved unedited).** "Derived directly from the zero-parameter framework" reads in the **downstream** sense: the netlist component values follow with **zero free parameters *beyond the 3 interlocked calibration inputs* $\{m_e, \alpha, G\}$ + 4 axioms** — they are not parameter-free outputs. Per the keystone register, $\alpha$, $m_e$, and $G$ are *retained inputs* (with $\alpha$ a Class-B named geometric identification, value-scoped echo), not derived values; AVE reduces the SM's $\sim$26 empirical parameters to those 3 inputs, which it does not yet lift to pure geometry. Canonical scope: `vol1/ch8-alpha-golden-torus.md:11` (manuscript `backmatter/03_geometric_inevitability.tex` Scope-correction 2026-06-14).

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

> **Note:** `summarybox` and `exercisebox` environments in the source chapter are not extracted as leaves in this KB.

---

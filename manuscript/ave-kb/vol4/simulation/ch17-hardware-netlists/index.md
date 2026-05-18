[↑ Vol 4: Simulation](../index.md)

# Ch.17: Hardware Netlists — EE Bench

Physical LTspice netlist for the EE Bench dielectric yield plateau measurement. Engineering blueprint with component values derived directly from the zero-parameter framework. Ch.17 uses codebox environments only (no resultboxes).

> **Note (REPO-ARCH-8, 2026-05-17 night)**: PONDER-01 cascaded stack netlist (20-layer Air/FR4 ladder, $100\,\text{MHz}$, $30\,\text{kV}$, $\Gamma = -0.349$ per boundary, asymmetric $\nabla|E|^2$ ponderomotive thrust) migrated to AVE-PONDER private repo per the `ave-ip-divide-discipline` skill. PONDER-01 hardware specifics live in `manuscript/vol_ponder/chapters/01_topological_thrust_mechanics.tex`, `03_high_voltage_vhf_drive.tex`, `05_vacuum_torsion_metrology.tex`, `07_hardware_build_guides.tex` + `src/scripts/simulate_hardware_netlists.py` (canonical PONDER-01 cascaded LC stack simulation). Substrate-physics anchors (saturation kernel, $V_{yield}$, $Z_0$ derivation) remain canonical in core; the EE Bench netlist below is the surviving general-purpose verification of the saturation kernel against a public bench measurement.

## Key Results

| Result | Expression | Source |
|---|---|---|
| EE Bench capacitance rolloff | $C_{eff}(V) = C_0\sqrt{1 - (V/V_{yield})^2}$; anomaly window at $\sim 0.85 \times V_{yield}$ to $V_{yield}$; deviation $> 10\%$ from linear baseline | ee-bench |
| Component derivation | $V_{yield} = \sqrt{\alpha} \times m_e c^2/e \approx 43.65\,\text{kV}$ | ee-bench |

## Derivations and Detail

| Document | Contents |
|---|---|
| [EE Bench Netlist](ee-bench-netlist.md) | Verbatim `ee_bench.cir` — behavioral charge equation for nonlinear vacuum capacitance under DC sweep to $45\,\text{kV}$ |

> **Note:** `summarybox` and `exercisebox` environments in the source chapter are not extracted as leaves in this KB.

---

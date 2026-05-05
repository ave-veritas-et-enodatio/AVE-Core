[↑ Simulation](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [vjv4zf]
-->

# Ch.18: Universal AVE Vacuum Cell

**Volume:** 4 (Applied Vacuum Engineering)
**Chapter:** 18 (Simulation Architecture)

All domain-specific SPICE models — nuclear decay, molecular bonds, protein folding, hardware thrust — are wiring topologies of a single canonical subcircuit: the `AVE_VACUUM_CELL`.  This cell implements the Axiom 4 saturation kernel $S(V) = \sqrt{1 - (V/V_{yield})^2}$ as ngspice behavioral sources.

## Key Results

| Result | Statement |
|---|---|
| Universal cell | `AVE_VACUUM_CELL` — single subcircuit for all AVE SPICE models |
| Metric Varactor | $Q = C_0 \cdot V / \sqrt{1 - (V/V_{YLD})^2}$ — Axiom 4, electric sector |
| Relativistic Inductor | $\Phi = L_0 \cdot I / \sqrt{1 - (I/I_{YMAX})^2}$ — Axiom 4, magnetic sector |
| TVS Zener | $R_{eff} = 0$ when $\|V\| \ge V_{YLD}$ — dielectric rupture |
| Linear variant | `AVE_VACUUM_CELL_LINEAR` — constant L, C, R for comparison runs |
| EE Bench cell | `AVE_EE_BENCH` — single varactor for DC sweep plateau verification |

## Subcircuit Architecture

### Three Constitutive Models in Parallel

The `AVE_VACUUM_CELL` contains three behavioral elements between nodes A and B:

1. **(a) Metric Varactor** (electric sector): Charge-based B-source with $Q = C_0 \cdot V / \sqrt{1 - (V/V_{YLD})^2}$.  As $V \to V_{YLD}$, $C_{eff} \to \infty$.
2. **(b) Relativistic Inductor** (magnetic sector): Flux-based behavioral voltage source with $\Phi = L_0 \cdot I / \sqrt{1 - (I/I_{YMAX})^2}$.  As $I \to I_{YMAX}$, $L_{eff} \to \infty$ and $dI/dt \to 0$ (velocity cannot exceed $c$).
3. **(c) TVS Zener** (optional damping): Linear resistance $R_0$ for material domains; $R_0 = 0$ for free vacuum.
4. **(d) Memristor** (placeholder): $\tau_{relax} \approx 1.29 \times 10^{-21}$ s — below any practical SPICE timestep.

### Parameters (from `ave.core.constants`)

| Parameter | Value | Origin |
|---|---|---|
| $V_{SNAP}$ | 510,998.95 V | $m_e c^2 / e$ |
| $V_{YIELD}$ | 43,653.7 V | $\sqrt{\alpha} \times V_{SNAP}$ |
| $I_{MAX}$ | 124.4 A | $\xi_{topo} \times c$ |
| $Z_0$ | 376.73 Ω | $\sqrt{\mu_0 / \varepsilon_0}$ |

### SPICE Netlist Compiler

The `spice_netlist_compiler.py` module translates AVE solver outputs (L, C, R, coupling) into cascaded `AVE_VACUUM_CELL` netlists:

```
Python solver → compile_* → .cir → ngspice → validation
```

Functions:
- `compile_ee_bench_dc_sweep()` — single-cell capacitance plateau test
- `compile_lcr_network()` — generic LCR network, AC or transient
- `compile_amino_acid_network()` — molecular topology from organic mapper
- `write_netlist()` — output to `.cir` file

## Derivations and Detail

| Document | Contents |
|---|---|
| [SPICE Subcircuit Specification](./spice-subcircuit.md) | Full behavioral source equations, numerical stability notes, usage examples |

*Cross-references*:
- `src/ave/hardware/spice_models/ave_vacuum_cell.lib`
- `src/ave/solvers/spice_netlist_compiler.py`
- Backmatter App 6 — SPICE Verification Manual
- [Nonlinear Constitutive Models](../../circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-constitutive-models.md) — varactor, inductor, TVS theory

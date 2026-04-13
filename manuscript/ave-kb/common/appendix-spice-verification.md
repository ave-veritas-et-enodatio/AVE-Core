[↑ Common Resources](index.md)
<!-- path-stable: referenced from vol4 as app:spice_verification -->

# Appendix: SPICE Verification Manual

**Backmatter:** Appendix 6

## Purpose

The SPICE Verification Manual establishes the industry-standard validation path for AVE physics:

$$\text{Python solver} \;\to\; \texttt{compile\_*} \;\to\; \texttt{.cir} \;\to\; \text{ngspice} \;\to\; \text{validation}$$

Every AVE domain — nuclear, molecular, protein, hardware — generates runnable ngspice netlists from the canonical `AVE_VACUUM_CELL` subcircuit library.  The Axiom 4 saturation kernel is implemented once and wired into domain-specific topologies.

## Architecture

### Tier Structure

| Tier | Role | Examples |
|---|---|---|
| **Tier 1** | Core axioms, constants, operators | `constants.py`, `universal_operators.py` |
| **Tier 2** | Domain solvers | `radial_eigenvalue.py`, `coupled_resonator.py` |
| **Tier 3** | SPICE compiler (consumes Tiers 1+2) | `spice_netlist_compiler.py` |

The compiler is Tier 3: it translates solver outputs into netlists but never re-derives operators.

### Canonical Library

The `ave_vacuum_cell.lib` file provides three subcircuits:

1. `AVE_VACUUM_CELL` — full nonlinear behavioral model
2. `AVE_VACUUM_CELL_LINEAR` — constant L, C, R (comparison baseline)
3. `AVE_EE_BENCH` — single varactor for DC sweep plateau verification

### Compiler Functions

| Function | Input | Output |
|---|---|---|
| `compile_ee_bench_dc_sweep()` | $C_0$, $V_{yield}$, $V_{max}$ | DC sweep netlist |
| `compile_lcr_network()` | Node/edge graph with L, C, R | AC or transient netlist |
| `compile_amino_acid_network()` | Bond topology from organic mapper | AC sweep netlist (1–100 THz) |
| `write_netlist()` | Compiled string | `.cir` file on disk |

## Verification Protocol

1. **Compile** the domain topology: `netlist = compile_lcr_network(...)`
2. **Write** the `.cir` file: `write_netlist(netlist, "output.cir")`
3. **Run** ngspice: `ngspice output.cir`
4. **Compare** SPICE output to Python solver predictions
5. Any deviation beyond numerical tolerance indicates a bug in either the solver or the netlist

## Dependencies

- ngspice ≥ 42 (behavioral B-source support required)
- Python ≥ 3.10

*Cross-references*:
- `src/ave/hardware/spice_models/ave_vacuum_cell.lib`
- `src/ave/solvers/spice_netlist_compiler.py`
- [Universal AVE Vacuum Cell](../vol4/simulation/ch18-universal-vacuum-cell/index.md)
- [Solver Toolchain](./solver-toolchain.md) — universal solver architecture

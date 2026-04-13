[↑ Simulation Architecture](./index.md)
<!-- leaf: verbatim -->

# Script Reproduction Procedure

The entire computation is reproduced in two commands from the repository root:

```
# Fold three test sequences (Polyalanine, Chignolin, Trpzip2)
python src/scripts/vol_5_biology/s11_fold_engine_v3_jax.py

# Generate SPICE transmission line strain plot
python src/scripts/vol_5_biology/ \
    simulate_protein_spice_transmission_line.py
```

## Code--Equation Map

Equation-to-code traceability. v3 physics layers are in `s11_fold_engine_v3_jax.py`; v4/v5 solver methods are in `s11_fold_engine_v4_ymatrix.py`.

| **Equation** | **Function / Module** | **Physics Layer** |
|---|---|---|
| *Physics Layers (v3/v4 shared):* | | |
| Eq. $\ref{eq:match\_quality}$ | `conjugate_match` (v3) | Conjugate impedance |
| Eq. $\ref{eq:c\_sat}$ | `C_sat` (v3) | Axiom 4 saturation |
| Eq. $\ref{eq:shunt\_admittance}$ | `dc_analysis()` (v4) | Shunt admittance |
| Eq. $\ref{eq:solvent\_shunt}$ | `dc_analysis()` (v4) | Solvent boundary |
| Eq. $\ref{eq:abcd\_section}$ | `abcd_to_y_3seg_jax()` (TL module) | ABCD cascade |
| Eq. $\ref{eq:s11\_from\_abcd}$ | `s11_from_y_matrix_jax()` (TL module) | $S_{11}$ extraction |
| Eq. $\ref{eq:multi\_freq}$ | `ac_analysis()` (v4) | Multi-frequency |
| Eq. $\ref{eq:chiral\_phase}$ | `chiral_correction` (v3) | Chirality phase |
| Eq. $\ref{eq:steric\_penalty}$ | `dc_analysis()` (v4) | Pauli exclusion |
| *Solver Architecture (v5/v7):* | | |
| Eq. $\ref{eq:eigenvalue\_target}$ | `_eigenvalue_target()` (v4) | Newton root target |
| Eq. $\ref{eq:newton\_step}$ | `fold_eigenvalue_v5()` (v4) | Newton-Raphson |
| Eq. $\ref{eq:spice\_velocity}$ | `explicit_spice_step()` (v7) | SPICE transient |
| Eq. $\ref{eq:spice\_position}$ | `explicit_spice_step()` (v7) | SPICE transient |

## Dependencies

External dependencies for the protein folding engine.

| **Package** | **Version** | **Purpose** |
|---|---|---|
| `jax` | $\geq 0.4$ | Automatic differentiation, JIT compilation |
| `numpy` | $\geq 1.24$ | Array manipulation, output analysis |

**Note:** The `optax` library (Adam optimiser) was a dependency of v3/v4 but has been **removed** as of the eigenvalue solver transition. All optimisation is now performed by the analytical Newton-Raphson and SPICE transient methods described in the [Solver Architecture](./solver-architecture.md).

---

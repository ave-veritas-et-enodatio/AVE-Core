[↑ Ch.1 VCA](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-u462e4]
-->

# Computational Solver Selection

## FDTD (Yee Grid) — `ave.core.fdtd_3d`

Cartesian staggered grid. Each cell = lumped LC element. CFL: $\Delta t \leq \Delta x/(c\sqrt{3})$.

**Use for**: bulk engineering where chirality averages out ($\Delta x \gg \ell_{node}$) — thrust, energy density, impedance matching, S-parameters, dark wakes, IMD, warp metric CFD.

**Cannot do**: anything chirality-sensitive.

JAX-accelerated variant: `ave.core.fdtd_3d_jax` — identical physics, GPU/TPU backend.

## K4-TLM — `ave.core.k4_tlm`

Diamond graph (K₄ complete graph). 4-port tetrahedral nodes with native chirality in scattering matrix.

**Use for**: chirality-dependent observables — HOPF-01 torus knot coupling, gravitational frame-dragging, topological Faraday rotation, vacuum birefringence.

**Trade-off**: ~4× more expensive per node, non-orthogonal BCs.

## Decision Matrix

| Observable | FDTD | K4-TLM |
|-----------|------|--------|
| Ponderomotive thrust | ✓ | — |
| Energy density / impedance | ✓ | — |
| Dark Wake ($\tau_{zx}$) | ✓ | — |
| IMD spectroscopy | ✓ | — |
| Warp metric CFD | ✓ | — |
| Chiral antenna coupling | — | ✓ |
| Gravitational lensing | — | ✓ |
| Topological Faraday rotation | — | ✓ |
| Vacuum birefringence | — | ✓ |

## Boundary Conditions

Both solvers support:
- **Mur 1st-order ABC** (default): $c_{abc} = (c\Delta t - \Delta x)/(c\Delta t + \Delta x)$
- **PML** (`use_pml=True`): cubic-graded $\sigma(d) = \sigma_{max}(d/d_{pml})^3$, $\sigma_{max} = (m+1)/(150\pi\Delta x)$. Use for <60 dB reflection.

## Default Yield Threshold

Both engines default to $V_{yield} = \sqrt{\alpha}\,V_{snap} \approx 43.65$ kV (macroscopic onset). Override with `v_yield=V_SNAP` for subatomic simulations.

## Source
- [01_vacuum_circuit_analysis.tex](../../../../../vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex) §7 (Solver Selection)
- Engine: `ave.core.fdtd_3d`, `ave.core.fdtd_3d_jax`, `ave.core.k4_tlm`

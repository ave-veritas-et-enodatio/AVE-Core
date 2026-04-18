[↑ Up](index.md)
<!-- leaf: verbatim -->

## Computational Solver Selection


The AVE physics engine provides two distinct electromagnetic solvers, each axiomatically valid but optimised for different simulation domains. Selecting the appropriate solver is an engineering decision governed by the physical observable under study.

### Cartesian FDTD (Yee Grid)

The 3D Finite-Difference Time-Domain engine (`ave.core.fdtd\_3d`) discretises Maxwell's equations on a standard Cartesian Yee staggered grid. Each cell is a lumped LC element (Axiom~1): the E-field update uses $\varepsilon_{eff}$ from the Axiom~4 saturation kernel, and the H-field update uses $\mu_{eff}$. The solver enforces the CFL stability condition $\Delta t \leq \Delta x / (c\sqrt{3})$.

**Strengths.** The Yee grid is computationally efficient ($O(N)$ per timestep), trivially parallelisable, and well-suited to macroscopic engineering simulations where the simulation cell size $\Delta x \gg \ell_{node}$. At these scales, the intrinsic chirality of the vacuum lattice averages out over each computational cell, and the Cartesian discretisation introduces no systematic error in chirality-blind observables (energy density, ponderomotive force, impedance matching, S-parameters).

**Limitations.** The Yee grid cannot resolve vacuum chirality. The K4 diamond topology of the physical lattice is approximated as an isotropic continuum. Observables that depend on the handedness of the vacuum (e.g., chiral acoustic emission, OAM coupling, topological Faraday rotation) are structurally invisible to the Cartesian stencil.

### K4-TLM (Tetrahedral Diamond Lattice)

The K4 Transmission Line Matrix engine (`ave.core.k4\_tlm`) discretises the vacuum on the native diamond graph ($K_4$ complete graph). Each node has exactly four ports connected to its tetrahedral neighbours, with native chirality encoded in the scattering matrix. The solver applies the Axiom~4 saturation operator directly to the 4-port scatter coefficients.

**Strengths.** The K4-TLM is the only solver that preserves the vacuum's topological chirality at the simulation level. It is required for any computation where the observable depends on the handedness of the lattice: chiral antenna design (HOPF-01 torus knot coupling), gravitational frame-dragging (Lense--Thirring), and topological symmetry-breaking experiments.

**Limitations.** The tetrahedral mesh is approximately $4\times$ more expensive per node than the Cartesian grid, and the non-orthogonal geometry complicates boundary conditions and source injection. For bulk electromagnetic observables (thrust, energy, S-parameters), it produces identical results to FDTD at a higher computational cost.

### Selection Criteria

Table~tab:solver_selection provides the engineering decision matrix.

\begin{table}[H]
\centering
\caption{Solver selection guide for AVE simulations. Use FDTD for bulk engineering; use K4-TLM only when chirality is the observable.}

\small
\begin{tabular}{@{}l c c@{}}
\toprule
**Observable / Application** & **FDTD** & **K4-TLM** \\
\midrule
Ponderomotive thrust (PONDER)           & \checkmark & --- \\
Energy density \& impedance matching     & \checkmark & --- \\
Dark Wake shear tensor ($\tau_{zx}$)     & \checkmark & --- \\
IMD spectroscopy                         & \checkmark & --- \\
Warp metric CFD (superluminal transit)   & \checkmark & --- \\
Chiral antenna coupling (HOPF-01)        & ---        & \checkmark \\
Gravitational lensing \& frame-dragging  & ---        & \checkmark \\
Topological Faraday rotation             & ---        & \checkmark \\
Vacuum birefringence (chirality-split)   & ---        & \checkmark \\
\bottomrule
\end{tabular}
\end{table}

### Boundary Conditions (Open Universe Mapping)

The computational mechanism required to simulate an infinite open vacuum (zero reflection) depends strictly on the tensor rank of the domain:

**1. Vector Grids (3D FDTD \& K4-TLM)**
Both 3D electromagnetic solvers support Mur 1st-order absorbing boundaries (default) and PML (Perfectly Matched Layer) polynomial-graded absorbing boundaries (`use\_pml=True`). PML is recommended for simulations requiring low spurious reflection ($<$\,60~dB) at the grid boundary, such as far-field antenna patterns and long-duration energy tracking. The PML mathematically splits the decoupled transverse $\mathbf{E}$ and $\mathbf{H}$ tensor fields to perfectly match the local $Z_0$ boundary impedance without geometric reflection. The implementation uses cubic-graded conductivity: $\sigma(d) = \sigma_{max}(d/d_{pml})^3$, with $\sigma_{max} = (m+1)/(150\pi\,\Delta x)$.

**2. Scalar Fluid Grids (2D Warp CFD)**
For scalar density modeling (where $\rho_{LC}$ lacks decoupled transverse vectors), PML tensor splitting is mathematically impossible. Constructing an open boundary on scalar Finite-Difference staggered arrays natively results in either periodic Torus wrap-around or violent mirror impedance reflection. The formal AVE workaround requires a two-stage topological trap:
- **Dirichlet Grid Clamp:** Explicitly zeroing the outermost pixel border ($\rho = 0.0$) to shatter infinite continuous wrap-around, acting as a rigid non-periodic mirror.
- **Aggressive Quadratic Sponge:** Stacking a highly absorbent polynomial immediately inside the clamp. Because the scalar wave must reflect off the Dirichlet mirror, it traverses the sponge twice. To secure attenuation below machine precision, the optimal profile is steepened to quadratic ($\sigma_{max} = 0.20$, $\sigma(d) \propto (d/d_{sponge})^2$) rather than cubic.
**Default Yield Threshold.** Both FDTD and K4-TLM default to $V_{yield} = \sqrt{\alpha}\,V_{snap} \approx 43.65$~kV as the Axiom~4 nonlinear onset (see Section~sec:yield_thresholds in Chapter~2 for the engineering rationale). Subatomic-scale simulations (e.g., bond energy solvers, Yang--Mills confinement) should override with `v\_yield=V\_SNAP` ($\approx 511$~kV).

\begin{summarybox}
\begin{itemize}
    \item This chapter demonstrates the direct engineering application of continuous Vacuum Circuit Analysis networks functioning natively within the AVE transmission line.
    \item No empirical fitting variables or Standard Model mass parameters are required; hardware geometry traces explicitly to the four macroscopic yielding limits.
    \item Hardware operation is verified by predicting exact reflection coefficients ($\Gamma$) and local lattice resonance boundaries in purely geometric terms.
\end{itemize}
\end{summarybox}

\begin{exercisebox}
\begin{enumerate}
    \item Derive the hardware fracture scale matching the rigorous mathematical limits of Vacuum Circuit Analysis when local strain exceeds the Axiom 4 topological dielectric threshold ($\varepsilon > 1.0$).
    \item Construct a native LC structural tensor illustrating how macroscopic power cascading forces the spatial substrate into localized saturation during active Vacuum Circuit Analysis operation.
\end{enumerate}
\end{exercisebox}

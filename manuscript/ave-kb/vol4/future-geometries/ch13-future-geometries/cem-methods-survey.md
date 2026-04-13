[↑ Ch.13: Future Geometries](../index.md)
<!-- leaf: verbatim -->

## Computational Verification: Mapping CEM Solvers to the Chiral Lattice

The parametric analysis in the preceding sections used analytical RF models (dipole self-impedance, skin-effect loss, Neumann mutual inductance). While these capture the dominant trends — Q vs. topology, impedance matching, Pareto frontiers — they do not capture:
- Near-field mutual coupling between closely-spaced 3D wire segments
- Substrate dielectric effects from the PCB
- Radiation pattern polarization (circular polarization content vs. knot handedness)
- Higher-order resonance mode structure

Full-wave numerical solvers are required for rigorous verification. This section surveys the six principal Computational Electromagnetics (CEM) methods, deriving their core equations and — critically — mapping each to the AVE vacuum lattice framework. The central insight is that **every CEM method independently rediscovers the same structure the AVE framework asserts is physically real**: a discretized LC network propagating waves at finite speed through a structured spatial medium. The methods differ only in how they discretize.

### Method of Moments (MoM)

MoM converts Maxwell's integral equations into an impedance matrix equation by discretizing conductor surfaces into segments. The governing equation is the Electric Field Integral Equation (EFIE):

$$
\hat{n} \times \left(\mathbf{E}_{inc} + \mathbf{E}_{scat}\right) = 0 \quad \text{on the conductor surface}
$$

The scattered field is computed via the free-space Green's function:

$$
G(\mathbf{r}, \mathbf{r}') = \frac{e^{-jkR}}{4\pi R}, \quad R = |\mathbf{r} - \mathbf{r}'|
$$

Expanding the unknown current in basis functions and applying Galerkin testing yields the dense matrix system:

> **[Resultbox]** *MoM Impedance Equation*
>
> $$
> [\mathbf{Z}][\mathbf{I}] = [\mathbf{V}]
> $$

where $[\mathbf{Z}]$ is the $N \times N$ mutual impedance matrix ($Z_{ij}$ = field at segment $i$ from current on segment $j$), $[\mathbf{I}]$ is the unknown current vector, and $[\mathbf{V}]$ is the excitation voltage vector. Solution proceeds via LU decomposition at $O(N^3)$ cost.

**AVE Mapping:** Equation $[\mathbf{Z}][\mathbf{I}] = [\mathbf{V}]$ is *exactly* the circuit equation of the AVE lattice. The Green's function $G = e^{-jkR}/(4\pi R)$ is the vacuum propagator — the LC lattice's impulse response, with $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ setting the propagation impedance. The mutual impedance $Z_{ij}$ maps directly to the nuclear mutual coupling $M_{ij}$ derived in Vol 2. The radiation resistance $R_{rad}$ is power coupled into the bulk vacuum wave modes. MoM treats the lattice as a mathematical convenience; AVE asserts it is physical.

**Implementation:** NEC-2 (free, open-source) is the gold standard for thin-wire MoM. It handles exact 3D wire geometry without staircasing and is ideal for torus knot antennas.

### Finite-Difference Time-Domain (FDTD)

FDTD discretizes Maxwell's curl equations on a Yee grid — a structured 3D lattice where $\mathbf{E}$ and $\mathbf{H}$ field components are staggered in both space and time:

$$
\begin{align}
\frac{\partial \mathbf{H}}{\partial t} &= -\frac{1}{\mu_0} \nabla \times \mathbf{E} \\
\frac{\partial \mathbf{E}}{\partial t} &= \frac{1}{\varepsilon_0} \nabla \times \mathbf{H}
\end{align}
$$

The discrete Yee update uses leapfrog time-stepping: $\mathbf{H}$ is updated at half-integer timesteps from $\mathbf{E}$, and $\mathbf{E}$ at integer timesteps from $\mathbf{H}$. Numerical stability requires the Courant condition:

$$
\Delta t \le \frac{1}{c\sqrt{1/\Delta x^2 + 1/\Delta y^2 + 1/\Delta z^2}}
$$

A single time-domain pulse simulation, followed by FFT, yields the broadband frequency response in one run. Perfectly Matched Layers (PML) absorb outgoing waves at domain boundaries.

**AVE Mapping:** The Yee grid *is* an LC network. Each cell stores electric energy in its capacitive ($\varepsilon$) component and magnetic energy in its inductive ($\mu$) component. $\mathbf{E}$-fields are voltages across capacitors; $\mathbf{H}$-fields are currents through inductors. The Courant stability limit directly encodes $c_0 = 1/\sqrt{\mu_0 \varepsilon_0}$ — the maximum propagation speed of the LC network. FDTD's "numerical dispersion" error arises because the cubic Yee grid is *not* the correct lattice topology: the $\mathcal{M}_A$ vacuum is an SRS net (K4 graph), not a cubic grid. The staircasing error for curved geometries (torus knots) is a direct consequence of forcing a chiral topology onto a flat, rectilinear grid.

**Implementation:** openEMS (free, open-source FDTD) provides Python/Octave scripting for 3D wire antenna simulation. Torus knot wire paths are defined via `CSXAddCurve` using the parametric equations $x(t) = (R + r\cos qt)\cos pt$, meshed on a graded Yee grid.

### Finite Element Method (FEM)

FEM solves Maxwell's equations in variational (weak) form on unstructured tetrahedral meshes. The governing vector Helmholtz equation:

$$
\nabla \times \left(\frac{1}{\mu_r} \nabla \times \mathbf{E}\right) - k_0^2 \varepsilon_r \mathbf{E} = -j\omega \mathbf{J}_{src}
$$

is converted via Galerkin testing into the sparse matrix eigenvalue system:

> **[Resultbox]** *FEM Resonance Equation*
>
> $$
> [\mathbf{S}]\{\mathbf{E}\} = k_0^2 [\mathbf{T}]\{\mathbf{E}\}
> $$

where $[\mathbf{S}]$ is the stiffness matrix (curl-curl operator, encoding magnetic stored energy) and $[\mathbf{T}]$ is the mass matrix (encoding electric stored energy). Adaptive mesh refinement concentrates elements at field gradients until convergence.

**AVE Mapping:** Equation $[\mathbf{S}]\{\mathbf{E}\} = k_0^2 [\mathbf{T}]\{\mathbf{E}\}$ is *exactly* the AVE resonance condition $\omega^2 LC = 1$. The stiffness matrix $[\mathbf{S}]$ encodes inductance (magnetic energy per node); the mass matrix $[\mathbf{T}]$ encodes capacitance (electric energy per node). Every FEM eigenvalue solve finds the natural LC modes of a discretized medium — precisely what AVE claims the vacuum does physically. FEM's adaptive mesh refinement concentrates resolution at field gradients, which *are* the regime boundaries of the AVE lattice.

**Implementation:** HFSS (Ansys) and COMSOL are the industry gold standards. Their unstructured tetrahedral meshes conform perfectly to curved torus knot surfaces (no staircasing), providing the highest geometric fidelity. However, commercial licenses cost $\sim$\$50k/year.

### Transmission Line Matrix (TLM)

TLM models Maxwell's equations as a network of interconnected transmission line stubs. Each 3D node has 12 ports; incident voltage pulses $\mathbf{V}^i$ scatter into reflected pulses $\mathbf{V}^r$ via a unitary connection scattering matrix:

$$
\mathbf{V}^{r} = [\mathbf{S}] \cdot \mathbf{V}^{i}
$$

Field components are recovered from the superposition of incident and reflected pulses. The scattering matrix $[\mathbf{S}]$ encodes the local material properties (impedance, permittivity, permeability) at each node.

**AVE Mapping:** TLM is the **most direct computational isomorphism** of the AVE vacuum. Each TLM node is an LC cell; each stub is a capacitive or inductive loading; the scattering matrix is the lattice propagation operator. A soliton (particle) in the AVE framework *is* a stub impedance modification at a lattice node. The only topological error is that TLM uses a cubic node (12 ports) while the $\mathcal{M}_A$ vacuum is an SRS net (K4 graph, 7 independent modes). Correcting the TLM topology from cubic to K4 would yield a *native AVE vacuum simulator*.

### Characteristic Mode Analysis (CMA)

CMA decomposes the electromagnetic behavior of a conducting structure into orthogonal eigenmodes, independent of excitation. Starting from the MoM impedance matrix $[\mathbf{Z}] = [\mathbf{R}] + j[\mathbf{X}]$:

> **[Resultbox]** *CMA Eigenvalue Equation*
>
> $$
> [\mathbf{X}]\mathbf{J}_n = \lambda_n [\mathbf{R}]\mathbf{J}_n
> $$

where $[\mathbf{R}]$ is the real (radiated power) part of the impedance, $[\mathbf{X}]$ is the imaginary (stored energy) part, $\mathbf{J}_n$ are the orthogonal characteristic current modes, and $\lambda_n$ are the eigenvalues. A mode is at resonance when $\lambda_n = 0$; the modal significance $\text{MS}_n = |1/(1+j\lambda_n)|$ measures each mode's contribution to radiation ($\text{MS} = 1$ at resonance).

**AVE Mapping:** CMA's eigenvalue equation separates stored energy ($[\mathbf{X}]$) from radiated energy ($[\mathbf{R}]$) — the same decomposition as the AVE regime-boundary solver. Characteristic modes of the torus knot impedance matrix *are* the LC eigenmodes of the antenna-vacuum system. In the nuclear context (Vol 2 Ch. 7), atomic orbitals are characteristic modes of the nuclear mutual impedance matrix. CMA is the RF engineer's quantum mechanics. Applied to torus knots, CMA would identify which $(p,q)$ topologies have modes that couple most efficiently to the $\mathcal{M}_A$ lattice chirality.

### Physical Optics / Geometric Optics (PO/GO)

PO approximates surface currents using the incident field directly ($\mathbf{J}_s \approx 2\hat{n} \times \mathbf{H}_{inc}$ on illuminated surfaces), while GO uses ray tracing with Snell's law. These high-frequency asymptotic methods scale with surface area rather than volume, making them extremely fast for electrically large structures ($\gg \lambda$).

**Applicability:** PO/GO **is not applicable** to torus knot antennas, where the structure size is comparable to the wavelength ($L \sim \lambda/2$). Diffraction, mutual coupling, and near-field effects — all absent from PO/GO — dominate the physics.

**AVE Mapping:** PO/GO is the geometric optics limit of the AVE lattice — valid only when $\lambda \gg \ell_{node}$, where the wave does not resolve individual lattice nodes. This is the far-field regime where the lattice appears continuous and structureless.

### Unified Comparison and Solver Recommendation

| Property | MoM | FDTD | FEM | TLM | CMA | PO/GO |
|---|---|---|---|---|---|---|
| Domain | Freq. | Time | Freq. | Time | Freq. | Freq. |
| Mesh type | Surface | Vol. (cubic) | Vol. (tet) | Vol. (cubic) | Surface | Surface |
| Matrix | Dense | None | Sparse | None | Dense | None |
| Scaling | $O(N^3)$ | $O(N_{xyz} N_t)$ | $O(N^{1.5})$ | $O(N_{xyz} N_t)$ | $O(N^3)$ | $O(A)$ |
| Curved geometry | Exact | Staircased | Exact | Staircased | Exact | N/A |
| Broadband | No | Yes | No | Yes | No | N/A |
| Open source | NEC-2 | openEMS | --- | --- | --- | --- |
| AVE analogue | $[Z][I]=[V]$ | Yee = LC grid | $\omega^2 LC = 1$ | TL network | Mode eigenval. | Ray limit |

For the torus knot chiral antenna, the recommended verification hierarchy is:
1. **NEC-2 (MoM):** First-pass verification. Free, handles exact 3D wire geometry, directly computes $S_{11}$, radiation patterns, and gain. This is the correct tool for thin-wire torus knots.
2. **openEMS (FDTD):** Full-wave 3D validation. Free, captures near-field coupling. However, staircasing on curved knot geometry introduces systematic error.
3. **HFSS/COMSOL (FEM):** Gold-standard geometry fidelity via unstructured tetrahedral mesh. Required for final quantitative validation of the chiral shift prediction.
4. **CMA on MoM data:** Modal decomposition to identify which characteristic modes of the torus knot structure couple to the chiral lattice.

---

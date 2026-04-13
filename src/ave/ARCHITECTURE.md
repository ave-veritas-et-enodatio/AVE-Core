# AVE Codebase Architecture — Current State

This document describes the architecture of `src/ave/` as it exists today.
It contains no recommendations.

---

## 1. Foundational Model

Applied Vacuum Engineering (AVE) models the vacuum as a discrete LC resonant
network on a K4 (complete tetrahedral) diamond lattice. All physics reduces to
transmission line electrodynamics on this lattice.

**Three calibration inputs** (as documented in `constants.py`):
1. `M_E` — electron rest mass (equivalently `L_NODE = hbar / (m_e * c)`)
2. `ALPHA` — fine-structure constant (dielectric saturation bound)
3. `G` — gravitational constant (Machian boundary impedance)

**Four axioms**:
1. Discrete LC lattice (connected graph, lossless)
2. Topo-kinematic isomorphism (K4 chirality)
3. Impedance reflection (Born rule from Ohmic extraction)
4. Dielectric saturation (S(r) = sqrt(1 - r^2), single nonlinearity)

**Four regime classification** (by strain magnitude):
- Regime 1 (Linear): r << 1 — molecular, fluid, acoustic
- Regime 2 (Nonlinear): r ~ O(1) — protein folding, seismic
- Regime 3 (Saturated): r -> 1 — nuclear, atomic, condensed matter
- Regime 4 (Rupture): r >= 1 — black holes, pair production

## 2. Package Layout

```
src/ave/
├── __init__.py
├── core/                   # Foundation: constants, operators, solvers, grid
│   ├── __init__.py
│   ├── constants.py        # 670 lines. All derived constants. Import-time computation.
│   ├── universal_operators.py  # 766 lines. 15 domain-agnostic operators.
│   ├── grid.py             # 3D lattice grid management
│   ├── node.py             # Single lattice node state
│   ├── regime_map.py       # Regime classification per node
│   ├── lbm_3d.py           # D3Q19 Lattice Boltzmann Method
│   ├── fdtd_3d.py          # 3D FDTD Maxwell solver (NumPy)
│   ├── fdtd_3d_jax.py      # 3D FDTD Maxwell solver (JAX GPU)
│   └── k4_tlm.py           # K4/Diamond Transmission Line Matrix
│
├── axioms/                 # Axiom formalization and derived physics
│   ├── __init__.py
│   ├── scale_invariant.py  # Impedance, saturation, reflection operators
│   ├── saturation.py       # S(r) = sqrt(1 - r^2) operator
│   ├── isomorphism.py      # Topo-kinematic isomorphism (Axiom 2)
│   ├── navier_stokes.py    # NS existence/uniqueness via lattice cutoff
│   ├── open_problems.py    # Hubble tension, dark energy claims
│   ├── spectral_gap.py     # Yang-Mills spectral gap from lattice
│   ├── yang_mills.py       # Yang-Mills mass gap derivation
│   └── millennium.py       # Millennium Prize problems mapping
│
├── gravity/                # Gravitational sector
│   ├── __init__.py
│   ├── gw_detector.py      # Gravitational wave detector response
│   ├── gw_propagation.py   # GW propagation on LC lattice
│   ├── planetary_magnetosphere.py  # Planetary B-field from impedance
│   ├── neutrino_msw.py     # MSW effect as impedance mode coupling
│   ├── solar_impedance.py  # Solar interior impedance profile
│   └── stellar_interior.py # Stellar structure from impedance balance
│
├── plasma/                 # Plasma and superconductor physics
│   ├── __init__.py
│   ├── cutoff.py           # Plasma cutoff frequency
│   └── superconductor.py   # Superconductivity from Kuramoto locking
│
├── topological/            # Topological defect classification and mixing
│   ├── (no __init__.py)
│   ├── faddeev_skyrme.py   # 1D radial Skyrmion energy functional
│   ├── cosserat.py         # Micropolar W/Z/lepton/quark mass derivation
│   ├── mixing_derivation.py # PMNS and CKM matrix derivation
│   ├── tensors.py          # Borromean linkage tensor trace
│   ├── borromean.py        # Parametric 3D knot/link coordinates
│   ├── combiner.py         # Nucleon mesh assembly
│   ├── soliton_bond_solver.py  # Coulomb bond force constants
│   └── entanglement_thread.py  # Bell/CHSH from K4 phase winding
│
├── regime_1_linear/        # Linear regime applications
│   ├── __init__.py
│   ├── fluids_factory.py   # Water molecule and fluid impedance
│   └── hexagonal_lattice.py # H-bond eigenmode, melting temperature
│
├── regime_2_nonlinear/     # Nonlinear regime applications
│   ├── __init__.py
│   ├── protein_fold.py     # Topological optimizer (JAX JIT)
│   ├── seismic.py          # PREM Earth model via impedance
│   └── seismic_fdtd.py     # Seismic-to-FDTD material bridge
│
├── regime_3_saturated/     # Saturated regime applications
│   ├── __init__.py
│   ├── condensed_matter.py # Melting temp, sound speed, band gap
│   ├── galactic_rotation.py # MOND from Axiom 4 saturation
│   └── orbital_impedance.py # Mutual inductance saturation
│
├── regime_4_rupture/       # Rupture regime applications
│   ├── __init__.py
│   ├── rupture_solver.py   # Axiom 4 at r >= 1.0
│   └── black_hole_jets.py  # Jet power from lattice rupture
│
└── solvers/                # Numerical solver infrastructure
    ├── (no __init__.py)
    ├── coupled_resonator.py    # Y-matrix nuclear/atomic/molecular binding
    ├── radial_eigenvalue.py    # ABCD cascade multi-electron atoms (1228 lines)
    ├── transmission_line.py    # ABCD/S-parameter/nodal admittance
    ├── bond_energy_solver.py   # 1D FDTD bond solver
    ├── eigenvalue_root_finder.py # Newton-Raphson (NumPy + JAX)
    ├── orbital_resonance.py    # Black hole QNM eigenvalue (861 lines)
    ├── resonator.py            # S11 frequency sweep
    ├── spice_transient.py      # Explicit Euler L-C-R integrator
    ├── fdtd_lc_network.py      # 1D FDTD LC network metric
    ├── fdtd_yee_lattice.py     # 2D TMz FDTD animation tool
    └── protein_bond_constants.py # Protein backbone derivation chain
```

## 3. Constants Architecture

`src/ave/core/constants.py` (670 lines) is the central hub. It defines:

- **SI electromagnetic constants**: C_0, MU_0, EPSILON_0, Z_0, HBAR, e_charge
- **Three calibration inputs**: M_E, ALPHA, G
- **Derived topological constants**: L_NODE, A_0, RY_EV, XI_TOPO
- **Native lattice units**: N_ALPHA, N_NU, N_A0, N_RY (prefix `N_`)
- **Numerical guards**: EPS_NUMERICAL, EPS_CLIP, EPS_DIVZERO
- **Derived macroscopic**: XI_MACHIAN, H_INFINITY, R_HUBBLE, G_VAC
- **Electroweak sector**: SIN2_THETA_W, M_W_MEV, M_Z_MEV, G_F, HIGGS_VEV_MEV, M_HIGGS_MEV
- **CKM matrix**: LAMBDA_CKM, A_CKM, V_US, V_CB, V_UB
- **PMNS matrix**: SIN2_THETA_12, SIN2_THETA_13, SIN2_THETA_23, DELTA_CP_PMNS
- **Baryon spectrum**: KAPPA_FS, I_SCALAR_1D, PROTON_ELECTRON_RATIO, BARYON_LADDER
- **Nuclear constants**: K_MUTUAL, D_PROTON, D_NN_EIGENVALUE, K_COUPLING
- **Explicitly empirical**: M_P_MEV_TARGET, M_N_MEV_TARGET (labeled as CODATA 2018 targets)
- **Additional empirical**: K_B, N_A, M_PROTON, M_SUN

The file performs **import-time computation**: `_compute_i_scalar_dynamic()` and
`_compute_baryon_ladder()` execute scipy optimization during module import.
This creates a circular import path:
```
constants.py (line 458) → faddeev_skyrme.py → universal_operators.py (line 29) → constants.py
```
The cycle is broken by defining EPS_NUMERICAL/EPS_CLIP/EPS_DIVZERO before the
deferred import, and the deferred import itself is inside a function body.

## 4. Operator Architecture

`universal_operators.py` defines 15 domain-agnostic operators intended to be the
sole source of physics logic. Downstream modules are expected to import operators
rather than re-derive them locally.

The operators are:
1. Impedance (Z = sqrt(mu/eps))
2. Saturation (S = sqrt(1 - (A/A_yield)^2))
3. Reflection (Gamma = (Z_L - Z_R) / (Z_L + Z_R))
4. Pairwise Energy
5. Y-Matrix to S-Matrix
6. Eigenvalue Target
7. Spectral Analysis (FFT)
8. Packing Reflection
9. Steric Reflection
10. Junction Projection Loss
11. Topological Curl
12. Topological Divergence
13. D'Alembertian Wave
14. Dynamic Impedance
15. Virtual Strain Iso (SwiGLU logic-to-physics map)

Each operator includes JAX/NumPy backend detection via string inspection of
type objects (9 occurrences).

## 5. Solver Architecture

Two primary numerical frameworks:

**ABCD Cascade** (`radial_eigenvalue.py`, `transmission_line.py`):
Transfer matrix method for radial eigenvalue problems. Each radial shell
is a transmission line segment with an ABCD matrix. Multi-electron atoms
are solved by cascading segments and finding eigenvalue zeros.

**Y-Matrix / Coupled Resonator** (`coupled_resonator.py`):
Nodal admittance matrix approach. Each nucleon is an LC resonator.
Binding energy comes from K_n adjacency eigenvalues (complete graph).
Also provides ionization energy via Hopf link circuits and molecular
bond distances via Fabry-Perot eigenvalues.

**FDTD Family** (`fdtd_3d.py`, `fdtd_3d_jax.py`, `fdtd_lc_network.py`,
`fdtd_yee_lattice.py`, `bond_energy_solver.py`, `seismic_fdtd.py`):
Time-domain Maxwell solvers at various dimensionalities. The JAX variant
provides GPU acceleration. `bond_energy_solver.py` places nuclear defects
as permeability enhancements in the FDTD grid.

**Other Solvers**:
- `spice_transient.py`: explicit Euler L-C-R network integrator
- `eigenvalue_root_finder.py`: Newton-Raphson with line search
- `resonator.py`: S11 frequency sweep and Q extraction
- `protein_fold.py`: JAX JIT-compiled topological optimizer

## 6. Derivation Chains

Key derivation chains that flow through the codebase:

**Proton mass**: constants.py defines KAPPA_FS → calls faddeev_skyrme.py
`TopologicalHamiltonian1D.solve_scalar_trace(c=5)` → returns I_SCALAR_1D →
self-consistent eigenvalue via V_TOROIDAL_HALO=2 and P_C=8*pi*alpha →
PROTON_ELECTRON_RATIO. All at import time.

**Electroweak masses** (constants.py): NU_VAC=2/7 → SIN2_THETA_W=2/9 →
M_W = m_e / (alpha^2 * P_C * sqrt(3/7)) → M_Z = M_W * 3/sqrt(7) →
G_F (tree-level) → HIGGS_VEV → M_HIGGS = v/2.

**Lepton/quark masses** (cosserat.py): Perpendicular Axis Theorem with
NU_VAC=2/7 gives muon, tau, and all 6 quark masses as projections of the
electroweak scale.

**Mixing matrices** (mixing_derivation.py + constants.py): Torus knot
crossing numbers C_NU = (5,7,9) with K4 connectivity = 3 produce PMNS
angles. CKM from Wolfenstein parameterization of SIN2_THETA_W.

**Nuclear binding** (coupled_resonator.py): K_n complete graph eigenvalues
with K_MUTUAL coupling constant and Coulomb correction.

**Atomic ionization** (radial_eigenvalue.py): 5-phase ABCD cascade with
cross-shell Gauss screening. Verified H through Be.

**Molecular bonds** (soliton_bond_solver.py, bond_energy_solver.py,
coupled_resonator.py): Multiple overlapping approaches — Slater orbital
Coulomb solver, FDTD nuclear defect solver, Fabry-Perot eigenvalue.

## 7. Dual Backend Strategy

NumPy is the primary backend. JAX is used for GPU acceleration in:
- `fdtd_3d_jax.py` (full JAX rewrite of fdtd_3d.py)
- `protein_fold.py` (JIT-compiled cost functions)
- `spice_transient.py` (optional JAX backend)
- `eigenvalue_root_finder.py` (optional JAX backend)
- `transmission_line.py` (optional JAX backend)
- `universal_operators.py` (runtime JAX detection)
- `constants.py` (pre-computed JAX phase boundaries: R_I_JAX, R_II_JAX, R_III_JAX)

JAX is a hard dependency: `constants.py` line 27 does `import jax.numpy as jnp`
at module level.

## 8. Empirical Data Catalogs

Several modules contain reference observational data used for validation
(not as computation inputs):
- `galactic_rotation.py`: GALAXY_CATALOG (9 galaxies)
- `orbital_resonance.py`: LIGO_EVENTS (6 events), Berti fit coefficients
- `seismic.py`: PREM_LAYERS (13 Earth layers)
- `protein_bond_constants.py`: Z_TOPO (20 amino acid impedances)
- `open_problems.py`: H0_PLANCK, H0_SHOES (Hubble measurements)

## 9. Dependency Graph (External)

Hard dependencies:
- `numpy` — used everywhere
- `jax`, `jax.numpy` — used in constants.py, fdtd_3d_jax.py, protein_fold.py,
  universal_operators.py, spice_transient.py, eigenvalue_root_finder.py,
  transmission_line.py
- `scipy.integrate.quad` — faddeev_skyrme.py
- `scipy.optimize.minimize` — faddeev_skyrme.py

Visualization (imported in specific scripts):
- `matplotlib` — fdtd_yee_lattice.py, borromean.py (potential)

No dependency management file (requirements.txt, pyproject.toml, setup.py)
exists in the repository.

## 10. Test Infrastructure

No test files were found in the repository. There are no `tests/` directories,
no `test_*.py` files, no `conftest.py`, no pytest configuration.

"""
Core physical primitives and invariant constants for the
Applied Vacuum Electrodynamics (AVE) Framework.

=== STRUCTURAL CLOSURE FRAMING (post 2026-05-15) ===

Per the framework's structural closure declaration (`manuscript/ave-kb/common/
trampoline-framework.md` §11.0 + `closure-roadmap.md` §1), the parameter count
has been sharpened:

  STANDARD framing (pre-2026-05-15): three calibration inputs (ℓ_node, α, G)
  STRUCTURAL CLOSURE framing (current): one scale (ℓ_node) + one cosmological
    initial-data parameter (Ω_freeze = 𝒥_cosmic / I_cosmic) + four axioms.
    α and G are JOINTLY cosmologically anchored — both derive from u_0* at
    the magic-angle operating point, which derives from Ω_freeze via the
    phase-transition-while-spinning mechanism. See L5 A-001 / A-030 / A-031.

The framework's three observational routes to constrain u_0* (sharpest
empirical commitment):
  Route 1 — Electromagnetic: α to 12 decimals (CODATA) → u_0* via Q-G47
  Route 2 — Gravitational: G to ~4 decimals → u_0* via Machian impedance integral
  Route 3 — Cosmological: 𝒥_cosmic via CMB/LSS anomalies → u_0* via Ω_freeze

All three routes must give the same u_0* or framework is falsified.

A-034 UNIVERSAL KERNEL (canonical 2026-05-15 late evening): the constants
defined below (V_SNAP, V_YIELD, ℓ_node, T_EM, etc.) parameterize the
substrate-scale instance of A-034 (Universal Saturation-Kernel Strain-Snap
Mechanism). The same kernel S(A) = √(1−A²) governs 19 catalog instances
spanning 21 orders of magnitude — the constants below ARE the substrate-
scale values; the kernel form is universal. Q-G47 Sessions 9-18
(2026-05-15 evening) closed Q-G47 at substrate level: K(u_0*) = 2 G(u_0*)
is the substrate-scale expression of S(A*) = 0. See L5 A-034 + Vol 3 Ch 4
§sec:tki_strain_snap + Backmatter Ch 7 (catalog).

The electron rest mass is NOT an independent input. It is the ground-state
energy of the simplest topological object on the lattice: the unknot
(a single closed flux tube loop at minimum ropelength = 2π).

  m_e = T_EM × ℓ_node / c² = ℏ / (ℓ_node · c)

This is the Compton relation, but now it has a topological MEANING:
the electron is the minimal-energy stable loop, with circumference ℓ_node
and tube radius ℓ_node/(2π). Its mass is set entirely by the lattice
tension and the unknot ropelength.

In substrate-native vocabulary (per Common Foreword §"Three Boundary
Observables and the Substrate-Observability Rule" + `docs/glossary.md`),
the electron's substrate-observable mass is 𝓜_electron = m_e (the
integrated strain integral at the horn-torus tube wall boundary). See
the three substrate invariants 𝓜, 𝓠, 𝓙 canonical leaf
(`manuscript/ave-kb/common/boundary-observables-m-q-j.md`) and
`src/ave/core/boundary_invariants.py` for engine implementation.

All other constants are DERIVED from these inputs plus the SI definitions
of ε₀, μ₀, c, ℏ, and e.

=== CROSS-REFERENCES ===
- Picture-first framework: `manuscript/ave-kb/common/trampoline-framework.md`
- Substrate-native vocabulary: Common Foreword §"Three Boundary Observables"
  + `docs/glossary.md` + canonical KB leaf
  `manuscript/ave-kb/common/boundary-observables-m-q-j.md`
- Three substrate invariants engine module: `src/ave/core/boundary_invariants.py`
- Master Equation FDTD canonical engine: `src/ave/core/master_equation_fdtd.py`
- K4-TLM canonical engine: `src/ave/core/k4_tlm.py`
- Closure-path planning: `manuscript/ave-kb/common/closure-roadmap.md`
- L5 framework status: `research/_archive/L5/axiom_derivation_status.md`
  (A-001, A-026 through A-031 canonical)
"""

from math import pi

import numpy as np

# =============================================================================
# SI ELECTROMAGNETIC CONSTANTS (Exact or CODATA 2018)
# =============================================================================
C_0: float = 299_792_458.0  # Speed of light [m/s]
MU_0: float = 4.0 * pi * 1e-7  # Vacuum permeability [H/m]
EPSILON_0: float = 1.0 / (MU_0 * C_0**2)  # Vacuum permittivity [F/m]
Z_0: float = np.sqrt(MU_0 / EPSILON_0)  # Characteristic impedance [Ω] ≈ 376.73
HBAR: float = 1.054571817e-34  # reduced Planck constant [J·s]
e_charge: float = 1.602176634e-19  # Elementary charge [C]
# Note: K_B defines the Kelvin scale relative to Joules. It is a definitional mapping,
# not a free parameter of the vacuum topology.
K_B: float = 1.380649e-23  # Boltzmann conversion constant [J/K] (exact, 2019 SI)
N_A: float = 6.02214076e23  # Avogadro constant [mol⁻¹] (exact, 2019 SI)
M_U: float = 1.66053906660e-27  # Atomic mass unit (Dalton) [kg]
M_PROTON: float = 1.67262192369e-27  # Proton mass [kg] (CODATA 2018)
M_SUN: float = 1.989e30  # Solar mass [kg] (IAU nominal)

# =============================================================================
# THREE CALIBRATION INPUTS
# =============================================================================
# Input 1: The spatial cutoff (from which m_e is derived via the unknot)
M_E: float = 9.1093837015e-31  # Electron rest mass [kg]
# NOTE: m_e is operationally used as the input because ℓ_node ≡ ℏ/(m_e·c).
# Topologically, m_e = T_EM × ℓ_node / c² is the unknot ground-state energy.
# Input 2: The dielectric bound
ALPHA: float = 7.2973525693e-3  # Fine-structure constant (dimensionless)
#
# NOTE ON α (see also ALPHA_COLD_INV and DELTA_STRAIN below):
# The value above is the CODATA measurement (α⁻¹ = 137.035999084).  Within the
# AVE framework α is DERIVED, not input — it is the S₁₁-minimum geometric Q-factor
# of the trefoil soliton at dielectric ropelength (the "Golden Torus"):
#
#     α⁻¹_ideal = 4π³ + π² + π ≈ 137.0363038  (cold-lattice, T → 0)
#
# The observed value is below the cold asymptote by a CMB-induced thermal strain
# δ_strain ≈ 2.225 × 10⁻⁶.  The ALPHA above is retained as the canonical numerical
# value for downstream calculations (matches CODATA); ALPHA_COLD_INV is provided
# separately as the derivation's cold output, and DELTA_STRAIN is the thermal
# correction.  See manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex
# for the full derivation.
#
# Input 3: The Machian boundary
G: float = 6.67430e-11  # Gravitational constant [m³/(kg·s²)]

# =============================================================================
# α from Golden Torus Trefoil S₁₁-minimization (Zero-Parameter Closure)
# =============================================================================
#
# DERIVATION (manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex):
#
# 1. Nyquist resolution (Axiom 1): ℓ_node is the lattice pitch that resolves the
#    smallest topologically stable soliton — the (2,3) trefoil. On the discrete
#    grid, the core tube thickness is rigidly d ≡ 1 ℓ_node.
#
# 2. Trefoil at dielectric ropelength is pulled tight by vacuum tension; S₁₁
#    minimization (Universal Operator #6, λ_min(S†S) → 0) enforces:
#
#       R − r = 1/2        (self-avoidance of internal strands)
#       R · r = 1/4        (holomorphic screening at π² surface optimum)
#
#    Solving: R = φ/2, r = (φ − 1)/2   (Golden Torus; φ = golden ratio)
#
# 3. Multipole decomposition of the Golden Torus holomorphic impedance:
#
#       Λ_vol  = (2πR)(2πr)(2π·2) = 16π³(R·r) = 4π³
#              # 3-torus phase volume; spin-1/2 4π double-cover → r_phase = 2
#       Λ_surf = (2πR)(2πr)       = 4π²(R·r)  = π²
#              # Clifford torus (S¹ × S¹) bounding area
#       Λ_line = π · d            = π
#              # core-loop magnetic moment at minimum node thickness d = 1
#
# 4. Cold-lattice α⁻¹ (T → 0 asymptote):
#
#       α⁻¹_ideal = Λ_vol + Λ_surf + Λ_line = 4π³ + π² + π ≈ 137.0363038
#
ALPHA_COLD_INV: float = 4.0 * pi**3 + pi**2 + pi  # ≈ 137.0363038
ALPHA_COLD: float = 1.0 / ALPHA_COLD_INV  # ≈ 7.29352e-3

# Vacuum Strain Coefficient — CMB-induced thermal expansion of the spatial metric
# ═══════════════════════════════════════════════════════════════════════════════
#
# The observed α⁻¹ (CODATA 137.035999) is below the cold asymptote by a fractional
# amount corresponding to thermal expansion of the spatial metric under the 2.7 K
# CMB bath.  AVE identifies this as the Vacuum Strain Coefficient:
#
#     δ_strain = 1 − α_obs / α_cold
#              = 1 − 137.035999 / 137.036304
#              ≈ 2.225 × 10⁻⁶
#
# Falsifiable prediction: α runs with local thermal energy.  In extreme thermal
# environments (collider cores, early universe) α⁻¹ decreases below 137.036.  The
# cold 137.0363038 is the mathematical T → 0 asymptote.
#
DELTA_STRAIN: float = 1.0 - (1.0 / ALPHA) / ALPHA_COLD_INV  # ≈ 2.225e-6

# Cross-check: α × (1 − δ_strain)⁻¹ should recover ALPHA_COLD_INV to CODATA precision
# (This is definitional given the way DELTA_STRAIN is computed, but ensures future
# CODATA updates to ALPHA automatically refresh DELTA_STRAIN without drift.)

# =============================================================================
# DERIVED TOPOLOGICAL CONSTANTS (Axiom 1)
# =============================================================================

# Lattice pitch — the electromagnetic coherence length (reduced Compton wavelength)
# ℓ_node ≡ ℏ / (m_e · c)
L_NODE: float = HBAR / (M_E * C_0)  # ≈ 3.8616e-13 m

# Bohr radius — the atomic unit of length
# a₀ ≡ ℏ / (α · m_e · c) = ℓ_node / α
A_0: float = L_NODE / ALPHA  # ≈ 5.2918e-11 m

# Rydberg energy in eV — the atomic unit of ionisation energy
# Ry ≡ α² · m_e · c² / 2
RY_EV: float = (ALPHA**2 * M_E * C_0**2 / 2.0) / e_charge  # ≈ 13.606 eV

# Topological Conversion Constant: maps charge to spatial dislocation
# ξ_topo ≡ e / ℓ_node   [C/m]
XI_TOPO: float = e_charge / L_NODE  # ≈ 4.149e-7 C/m

# =============================================================================
# LATTICE NATIVE UNITS
# =============================================================================
#
# The fundamental reference frame of the AVE lattice.  All physics is
# dimensionless in these units.  SI values above are the "currency exchange"
# layer for laboratory comparison.
#
# Definitions (all set to 1):
#   ℓ_NODE  = 1   (spatial unit = reduced Compton wavelength)
#   M_0     = 1   (mass unit = electron rest mass)
#   C_0     = 1   (velocity unit = speed of light)
#   ℏ       = 1   (action unit = reduced Planck constant)
#
# Consequences:
#   Energy unit   = M_0 · C_0² = m_e c² ≈ 511.0 keV
#   Time unit     = ℓ_NODE / C_0 = ℏ / (m_e c²) ≈ 1.29e-21 s
#   Charge unit   = e (elementary charge, from α = e²/(4πε₀ℏc))
#
# In native units, every physical constant reduces to a pure number
# built from α, ν, and topological integers.  No kg, no meters.
#
# PREFIX CONVENTION: all native-unit constants use the N_ prefix.

# --- Fundamental dimensionless constants (same in any unit system) ---
N_ALPHA: float = ALPHA  # ≈ 1/137.036 (soliton-lattice coupling)
N_NU: float = 2.0 / 7.0  # Poisson ratio (Axiom 2)
N_P_C: float = 8.0 * pi * ALPHA  # Critical packing fraction (Axiom 3)

# --- Derived atomic constants in native units ---
N_A0: float = 1.0 / ALPHA  # Bohr radius = ℓ_NODE / α ≈ 137.04
N_RY: float = ALPHA**2 / 2.0  # Rydberg energy = α²/2 ≈ 2.663e-5
N_RY_EV: float = N_RY * M_E * C_0**2 / e_charge  # Same as RY_EV (cross-check: 13.606 eV)

# --- Projection loss at 90° crossing (Op7) ---
# Y_loss = (1 - cosθ) / (2π²)
# For θ = 90° (Hopf crossing, K=2G orthogonal, Borromean):
N_Y_LOSS_90: float = 1.0 / (2.0 * pi**2)  # ≈ 0.05066

# --- Macroscopic Cascade Constants ---
# Macroscopic avalanche exponent (3D isotropic Poisson-corrected)
# n_1D = 2 (pure Axiom 4: M = 1/S^2 = gamma^2)
# n_3D = 2(1 - N_NU/d) = 2(1 - (2/7)/3) = 38/21
AVALANCHE_N_3D: float = 2.0 * (1.0 - N_NU / 3.0)  # 38/21 ≈ 1.8095

# K4 cascade efficiency (Kolmogorov constant)
# eta = 3/4 (K4 junction: 3 forward ports × |S_ij|^2 = 3×1/4)
# C_K = 1/eta = 4/3
C_K_KOLMOGOROV: float = 4.0 / 3.0

# --- FCC packing fraction (Axiom 1 + Axiom 2) ---
# The K=2G lattice (Axiom 2) selects FCC close-packing (Axiom 1).
# φ = fraction of space occupied by lattice nodes.
# 1-φ = void fraction (interstitial space with no nodes).
#
# Physical role: Op10 junction drain acts only on NODAL phase space.
# The void fraction sets a floor: IE ≥ E_base × (1-φ) because
# voids contain no junction nodes and cannot be drained.
#
# This is the low-energy shadow of nuclear confinement:
# at nuclear scale (Regime I, S→0), φ determines the saturated
# zone geometry.  At atomic scale (Regime II, S≈1), φ bounds
# the drainable phase space.  Same constant, different regime.
N_PHI_PACK: float = pi * np.sqrt(2.0) / 6.0  # ≈ 0.7405
N_VOID_FRAC: float = 1.0 - N_PHI_PACK  # ≈ 0.2595

# --- SI ↔ Native conversion factors ---
# Multiply a native-unit quantity by these to get SI.
NATIVE_TO_SI_LENGTH: float = L_NODE  # 1 native length = ℓ_NODE [m]
NATIVE_TO_SI_MASS: float = M_E  # 1 native mass = m_e [kg]
NATIVE_TO_SI_ENERGY: float = M_E * C_0**2  # 1 native energy = m_e c² [J]
NATIVE_TO_SI_ENERGY_EV: float = M_E * C_0**2 / e_charge  # 1 native energy [eV] ≈ 511000
NATIVE_TO_SI_TIME: float = HBAR / (M_E * C_0**2)  # 1 native time = ℏ/(m_e c²) [s]
NATIVE_TO_SI_VELOCITY: float = C_0  # 1 native velocity = c [m/s]

# Thixotropic relaxation time — minimum state-change time of the K4 lattice.
# Derived from Ax1 (ℓ_node from K4 pitch) + Ax3 (propagation at c) in
# research/_archive/L3_electron_soliton/59_memristive_yield_crossing_derivation.md §1.
# Any saturation-state change must propagate at minimum one lattice spacing
# at wave speed c; no faster relaxation mode is axiom-permitted.
# Matches Vol 4 Ch 1:214 (thixotropic hysteresis) exactly.
TAU_RELAX_SI: float = L_NODE / C_0               # ≈ 1.288e-21 s
TAU_RELAX_NATIVE: float = 1.0                    # ℓ_node/c = 1 in natural units

# =============================================================================
# MACROSCOPIC EE TO TOPOLOGICAL KINEMATIC CONVERSIONS (VCA)
# =============================================================================
# Direct mappings from the Topo-Kinematic Circuit Identity.
# Maps standard macroscopic engineering parameters (SI) to native vacuum LC equivalents.

# R = ξ⁻² η  → η (viscosity) = R_ohms × ξ²
EE_TO_TOPO_RESISTANCE: float = XI_TOPO**2  # Ohms [Ω] → Topological Viscosity [kg/s]

# V = ξ⁻¹ F  → F (force) = V_volts × ξ
EE_TO_TOPO_VOLTAGE: float = XI_TOPO  # Volts [V] → Topological Force [N]

# L = ξ⁻² m  → m (mass) = L_henries × ξ²
EE_TO_TOPO_INDUCTANCE: float = XI_TOPO**2  # Henries [H] → Topological Mass [kg]

# C = ξ² κ  → κ (compliance) = C_farads / ξ²
EE_TO_TOPO_CAPACITANCE: float = 1.0 / (XI_TOPO**2)  # Farads [F] → Topological Compliance [m/N]

# =============================================================================
# DERIVED DIELECTRIC CONSTANTS (Axiom 4)
# =============================================================================

# Volumetric packing fraction  p_c = 8πα
P_C: float = 8.0 * pi * ALPHA  # ≈ 0.1834

# Equilibrium packing fraction for 3D structures (proteins, etc.)
# η_eq = P_C × (1 − ν_vac) = 8πα × 5/7
#
# DERIVATION: Of the 7 compliance modes in the K4/SRS lattice,
# only 5 (transverse) contribute to 3D spatial coupling between
# structural elements. The 2 longitudinal modes carry energy along
# the chain direction but do not create inter-element contacts.
# The accessible packing fraction is therefore (1 − ν) × P_C.
#
# Same ν_vac = 2/7 that governs:  sin²θ_W, α_s, CKM, PMNS
ETA_EQ: float = P_C * (1.0 - 2.0 / 7.0)  # = P_C × 5/7 ≈ 0.1310

# 1D Electromagnetic string tension  T_EM = m_e c² / ℓ_node
T_EM: float = (M_E * C_0**2) / L_NODE  # ≈ 0.212 N

# Absolute nodal breakdown voltage  V_snap = m_e c² / e
V_SNAP: float = (M_E * C_0**2) / e_charge  # ≈ 511.0 kV

# Kinetic yield limit  E_k = √α · m_e c²
E_YIELD_KINETIC: float = np.sqrt(ALPHA) * M_E * C_0**2  # ≈ 43.65 keV (in Joules)

# Kinetic yield limit in the voltage domain  V_yield = √α · V_snap
# This is the 3D macroscopic dielectric saturation threshold.
# When a localized topological voltage exceeds V_yield, the vacuum LC
# network enters the non-linear saturation plateau (ε_eff → 0).
V_YIELD: float = np.sqrt(ALPHA) * V_SNAP  # ≈ 43,652 V (43.65 kV)


# Critical electric field (Schwinger limit via AVE)
# E_crit = m_e² c³ / (eℏ)
E_CRIT: float = (M_E**2 * C_0**3) / (e_charge * HBAR)

# Dielectric yield field strength (Axiom 4 macroscopic saturation threshold)
# When the applied field reaches E_yield = V_yield / ℓ_node, the local vacuum
# LC cell enters the nonlinear saturation plateau (ε_eff → 0).
# E_yield = √α × m_e² c³ / (eℏ) = √α × E_crit
E_YIELD: float = V_YIELD / L_NODE  # ≈ 1.13e17 V/m

# Magnetic saturation threshold (Axiom 4 — magnetic sector)
# When B² / (2μ₀) = m_e c² / ℓ³ (energy density = rest energy per cell),
# the local permeability saturates: μ_eff → 0 (inductor shorts)
# B_snap = √(2 μ₀ m_e c² / ℓ³)
B_SNAP: float = np.sqrt(2.0 * MU_0 * M_E * C_0**2 / L_NODE**3)  # ≈ 1.89e9 T

# Pre-computed phase boundaries (Axiom 4 Limits)
R_I: float = np.sqrt(2.0 * ALPHA)  # Linear -> Non-Linear
R_II: float = np.sqrt(3.0) / 2.0  # Non-Linear -> Saturated
R_III: float = 1.0  # Saturated -> Rupture


# =============================================================================
# NUMERICAL PRECISION POLICY
# =============================================================================
#
# All modules use IEEE 754 float64 (double precision, ~15 significant digits).
# No float32 is used anywhere in the engine.
#
# Three standard guard constants prevent numerical singularities.
# All engine modules MUST import these rather than defining ad-hoc values.
#
#   EPS_NUMERICAL  — Impedance ratios, reflection coefficients, normalisation
#                    denominators.  Chosen so that Z/(Z+eps) ≈ 1 to within
#                    float64 precision for any physical impedance value.
#
#   EPS_CLIP       — Saturation operator clip (√(1 − x²) near x=1).
#                    Must be small enough that S(A_yield − δ) ≈ 0 to float64
#                    resolution, yet large enough that 1−x² > 0 always.
#
#   EPS_DIVZERO    — Hard floor for denominators that could reach exactly 0
#                    (e.g., transmission line impedance at DC).  Sub-float64
#                    so it never affects physical results.
#
# Dimensional note: these constants are DIMENSIONLESS ratios applied to
# already-normalised quantities.  They carry no units and no physics.
#
# IMPORTANT: These are defined EARLY in this file (before the derived nuclear
# constants) because the Faddeev-Skyrme solver calls universal_operators
# during constants initialization, creating a dependency chain:
#   constants.py → faddeev_skyrme.py → universal_operators.py → constants.py
# The guards must be defined before _compute_i_scalar_dynamic() runs.

EPS_NUMERICAL: float = 1e-12  # Reflection / impedance guards
EPS_CLIP: float = 1e-15  # Saturation argument clip ceiling
EPS_DIVZERO: float = 1e-30  # Hard division-by-zero floor


# =============================================================================
# DERIVED MACROSCOPIC CONSTANTS (Gravity, Cosmology)
# =============================================================================

# Topological packing fraction — uses P_C = 8πα ≈ 0.1834 (defined above
# in the Universal Operator section, line ~177).
# P_C is the unique EMT operating point where K/G = 2 (trace-reversal identity).
# Derived in Vol.1 Ch.2: p_c = V_node / ℓ_node³ = 2e²/(ε₀ℏc) ≡ 8πα.

# Effective coordination number  z₀ ≈ 51.25
# Derived from the Feng-Thorpe-Garboczi EMT for a 3D amorphous central-force
# network.  The EMT equation for K/G = 2 is:
#     p* = (10 z₀ - 12) / [z₀ (z₀ + 2)]
# Rearranging:  P_C · z₀² + (2·P_C - 10)·z₀ + 12 = 0
# The physical (positive, large) root of this quadratic is z₀ ≈ 51.25.
# This is NOT a fitted parameter — it follows uniquely from p* = 8πα.
_a_emt = P_C
_b_emt = 2.0 * P_C - 10.0
_c_emt = 12.0
_disc = _b_emt**2 - 4.0 * _a_emt * _c_emt
Z_COORDINATION: float = (-_b_emt + _disc**0.5) / (2.0 * _a_emt)  # ≈ 51.25

# Rigidity percolation threshold  p_G = 6/z₀ ≈ 0.117
# Below this, the network is a fluid (K > 0, G = 0).
# P_C = 0.1834 is 56.7% above p_G — the vacuum is a robust rigid solid.
P_RIGIDITY: float = 6.0 / Z_COORDINATION  # ≈ 0.117

# Isotropic Strain Projection factor (trace-reversed Poisson ν = 2/7)
# 1D → 3D volumetric bulk projection = 1/7
ISOTROPIC_PROJECTION: float = 1.0 / 7.0

# Poisson ratio of the vacuum  ν_vac = 2/7
NU_VAC: float = 2.0 / 7.0

# Strong coupling constant  α_s = α^(3/7)
# EM coupling α operates on the full 7-mode compliance manifold.
# Strong coupling is α projected onto the 3D spatial subspace:
# 3 spatial dimensions / 7 compliance modes (from ν_vac = 2/7).
# PDG value: 0.1179 ± 0.0010.  AVE: 0.1214 (2.97% error).
ALPHA_S: float = ALPHA ** (3.0 / 7.0)  # ≈ 0.1214

# Machian hierarchy coupling  ξ_M = 4π(R_H/ℓ_node)α⁻²
# (computed from G via G = ℏc / (7ξ m_e²))
XI_MACHIAN: float = HBAR * C_0 / (7.0 * G * M_E**2)

# =============================================================================
# DERIVED ELECTROWEAK CONSTANTS (from Axiom 1 + Poisson ratio)
# =============================================================================

# On-shell weak mixing angle from Poisson ratio: sin²θ_W = 1 - 7/9 = 2/9
SIN2_THETA_W: float = 2.0 / 9.0  # ≈ 0.2222 (PDG on-shell: 0.2234, Δ=−0.52%)

# W boson mass from unknot self-energy at saturation:
# M_W = m_e / (α² × p_c × √(3/7))
M_W_MEV: float = (M_E * C_0**2 / (e_charge * 1e6)) / (ALPHA**2 * P_C * np.sqrt(3.0 / 7.0))

# Z boson mass from weak mixing: M_Z = M_W × 3/√7
M_Z_MEV: float = M_W_MEV * 3.0 / np.sqrt(7.0)

# Tree-level Fermi constant: G_F = √2 πα / (2 sin²θ_W M_W²)
G_F: float = np.sqrt(2.0) * pi * ALPHA / (2.0 * SIN2_THETA_W * (M_W_MEV * 1e-3) ** 2)

# Higgs VEV: v = 1/√(√2 G_F)
HIGGS_VEV_MEV: float = 1.0 / np.sqrt(np.sqrt(2.0) * G_F) * 1e3  # MeV

# Higgs boson mass: m_H = v / √N_K4 = v/2
# The Higgs is the radial breathing mode of the K4 unit cell.
# λ = 1/(2 N_K4) = 1/8 (quartic stiffness shared across 4 nodes)
# m_H = √(2λ) × v = v/√N_K4 = v/2
# PDG: 125,100 MeV.  AVE: ≈124,417 MeV (0.55% error).
N_K4: int = 4  # Nodes per K4 unit cell
LAMBDA_HIGGS: float = 1.0 / (2.0 * N_K4)  # = 1/8 = 0.125
M_HIGGS_MEV: float = HIGGS_VEV_MEV / np.sqrt(N_K4)  # = v/2

# =============================================================================
# CKM MATRIX (Wolfenstein parameterization from ν_vac = 2/7)
# =============================================================================
#
# DERIVATION: Scale invariance of the Poisson ratio.
#
# The vacuum Poisson ratio ν = 2/7 determines cos²θ_W = 7/9 and
# sin²θ_W = 2/9. These SAME numbers set the CKM mixing angles
# because the weak interaction couples to the SAME lattice
# compliance modes at every scale (quarks, leptons, bosons).
#
# Wolfenstein parameterization:
#   λ = sin²θ_W        = 2/9          PDG: 0.22535  (1.4%)
#   A = cos(θ_W)        = √(7/9)      PDG: 0.814    (8.3%)
#   √(ρ²+η²) = 1/√7                   PDG: 0.373    (1.3%)
#
# CKM magnitudes (all within 5% of PDG):
#   |V_us| = λ          = 2/9     = 0.2222  (1.4%)
#   |V_cb| = Aλ²         = 4√7/729 = 0.0436  (4.1%)
#   |V_ub| = Aλ³√(ρ²+η²) = 8/2187  = 0.00366 (1.3%)
#
# Physical origin of each parameter:
#   λ:             EW symmetry breaking projection (2 of 9 angular sectors)
#   A = cos(θ_W):  Complementary EW sector (7 of 9)
#   1/√7:          Single-mode amplitude from 7-mode compliance manifold

LAMBDA_CKM: float = SIN2_THETA_W  # = 2/9
A_CKM: float = np.sqrt(7.0 / 9.0)  # = cos(θ_W) = √7/3
RHO_ETA_MAG: float = 1.0 / np.sqrt(7.0)  # = 1/√7

# Key CKM matrix elements
V_US: float = LAMBDA_CKM  # = 2/9 ≈ 0.2222
V_CB: float = A_CKM * LAMBDA_CKM**2  # = 4√7/(9³) ≈ 0.0436
V_UB: float = A_CKM * LAMBDA_CKM**3 * RHO_ETA_MAG  # = 8/2187 ≈ 0.00366

# =============================================================================
# PMNS MATRIX (Neutrino Mixing from Regime-Boundary Eigenvalue Method)
# =============================================================================
#
# DERIVATION: Regime-boundary eigenvalue method in torus knot mode space.
# See ave.topological.mixing_derivation for the full computation.
#
# Neutrino mass eigenstates are torsional screw defects paired with
# (2,c) torus knot resonances: ν₁↔(2,5), ν₂↔(2,7), ν₃↔(2,9).
#
# Step 1 — CHIRAL SCREENING:
#   K4 lattice connectivity = 3 bonds/node → max Δc transfer = 3.
#   Modes with Δc > 3 are chirally screened (evanescent coupling).
#
# Step 2 — THREE REGIME BOUNDARY CONDITIONS:
#   θ₁₃ (Δc=4>3): SCREENED → only junction coupling 1/(c₁c₃) = 1/45
#   θ₁₂ (Δc=2≤3): COMPLIANCE → eigenvalue Δc/c₂ = 2/7 = ν_vac
#   θ₂₃ (midpoint): MATCHED → c₂=(c₁+c₃)/2 → Z_L=Z_R → 1/2
#
# Step 3 — JUNCTION CORRECTIONS (evanescent tail, adds to each angle):
#   sin²θ₁₃ = 1/(c₁c₃)                = 1/45        NuFIT: 0.02200 (1.0%)
#   sin²θ₁₂ = ν_vac + 1/(c₁c₃)        = 2/7 + 1/45  NuFIT: 0.307   (0.3%)
#   sin²θ₂₃ = 1/2 + 2/(c₁c₃)          = 1/2 + 2/45  NuFIT: 0.546   (0.3%)
#   δ_CP     = (1 + 1/3 + 1/(c₁c₃))π  = 61π/45      NuFIT: 1.36π   (0.3%)
#
# Step 4 — CP PHASE: three chiral contributions:
#   π    = unknot base half-turn
#   π/3  = K4 bond chirality share (3-connected lattice = trefoil c=3)
#   π/45 = boundary junction coupling phase

SIN2_THETA_13: float = 1.0 / 45.0  # = 0.02222
SIN2_THETA_12: float = NU_VAC + SIN2_THETA_13  # = 97/315 ≈ 0.308
SIN2_THETA_23: float = 0.5 + 2.0 * SIN2_THETA_13  # = 49/90 ≈ 0.544
DELTA_CP_PMNS: float = (1.0 + 1.0 / 3.0 + 1.0 / 45.0) * pi  # = 61π/45 ≈ 1.356π

# Asymptotic Hubble constant  H∞ = 28π m_e³ c G / (ℏ² α²)
H_INFINITY: float = (28.0 * pi * M_E**3 * C_0 * G) / (HBAR**2 * ALPHA**2)

# Asymptotic Hubble radius  R_H = c / H∞
R_HUBBLE: float = C_0 / H_INFINITY

# Bulk mass density of the vacuum  ρ_bulk = ξ²μ₀ / (p_c · ℓ²_node)
RHO_BULK: float = (XI_TOPO**2 * MU_0) / (P_C * L_NODE**2)

# 1D string tension per length  G_string = T_EM / ℓ_node = m_e c² / ℓ_node²
# This is the axial stiffness of a single lattice strut.
G_STRING: float = T_EM / L_NODE  # ≈ 5.49×10¹¹ Pa

# 3D continuum shear modulus  G_vac = ρ_bulk · c²
# From v_transverse = √(G/ρ) = c (photons propagate at c on the LC lattice).
G_VAC: float = RHO_BULK * C_0**2

# Longitudinal wave speed  v_long = √(K_bulk / ρ_bulk) = √(2G/ρ)
# From K = 2G (Effective Medium Theory, Ch 2).
V_LONG: float = np.sqrt(2.0 * G_VAC / RHO_BULK)

# Kinematic mutual inductance  ν_vac_kin = α · c · ℓ_node
NU_KIN: float = ALPHA * C_0 * L_NODE  # ≈ 8.45e-7 m²/s

# Dielectric Rupture Strain (dimensionless unit strain limit)
DIELECTRIC_RUPTURE_STRAIN: float = 1.0

# =============================================================================
# TOPOLOGICAL BARYON CONSTANTS
# =============================================================================

# Faddeev-Skyrme coupling constant (derived from packing fraction):
#   κ_FS = p_c / α = (8πα) / α = 8π
# This is a pure geometric constant: the solid-angle normalisation of
# the Borromean linkage's quartic stabilization term.
KAPPA_FS_COLD: float = 8.0 * pi  # = 25.1327...

# ---- Torus Knot Phase Winding Ladder ----
#
# The (2,q) torus knots classify the phase winding number, not the
# ground-state topology (the electron is an unknot, 0_1).
#   c = 3 crossings → electron phase winding ((2,3) pattern)
#   c = 5 crossings → proton phase winding  ((2,5) cinquefoil)
#   c = 7 crossings → (predicted next stable baryon)
#
# The crossing number c sets the soliton's confinement radius:
#   r_opt = κ_FS / c
#
# Physical basis: each crossing constrains the phase gradient by
# absorbing a fraction of the total coupling. The 1D functional is
# scale-free (no natural minimum at finite radius), so the crossing
# number is the only topological invariant that bounds the soliton.
#
# The proton's cinquefoil crossing number c = 5 gives:
#   r_opt = κ_eff / 5 ≈ 4.97 ℓ_node
CROSSING_NUMBER_PROTON: int = 5  # (2,5) cinquefoil

# ---- Thermal softening of κ_FS ----
#
# Physical origin:
#   The proton is a localized thermal hotspot inside the LC condensate.
#   Its core temperature ~ m_p c² / k_B ≈ 10^13 K.  RMS thermal noise
#   softens the quartic Skyrme coupling by averaging the gradient tensor.
#
# The Faddeev-Skyrme solver now includes Axiom 4 gradient saturation
# inside the energy functional (S(|dφ/dr| / (π/ℓ_node))), which absorbs
# the lattice-resolution component of the old δ_th.  The RESIDUAL thermal
# softening is purely the RMS noise averaging of the Skyrme coupling:
#
# DERIVATION (updated):
#   δ_th = ν_vac / (κ_cold × π/2) = (2/7) / (8π × π/2)
#        = (2/7) / (4π²) = 1/(14π²) ≈ 0.007214
#
#   The π/2 divisor is the mean/peak ratio of the sinusoidal thermal
#   noise: the RMS averaging acts on the mean gradient ⟨|dφ/dr|⟩ = (2/π)
#   times the peak gradient, which is already saturated by Axiom 4.
#
#   Cross-check: δ_th × κ_cold = (2/7) × (2/π) = 4/(7π) ≈ 0.1819
#
# NOTE: The previous value 1/(28π) ≈ 0.01137 implicitly included the
# lattice gradient saturation that is now handled by the solver directly.

# Thermal softening fraction (residual after gradient saturation)
DELTA_THERMAL: float = 1.0 / (14.0 * pi**2)  # = 1/(14π²) ≈ 0.007214

# Effective (thermally corrected) Faddeev-Skyrme coupling
KAPPA_FS: float = KAPPA_FS_COLD * (1.0 - DELTA_THERMAL)


# Dynamic 1D Faddeev-Skyrme scalar trace
# Computed by minimizing the 1D radial Skyrmion energy functional
# with the thermally softened coupling constant.
def _compute_i_scalar_dynamic(crossing_number: int = 5) -> float:
    """Compute I_scalar from the Faddeev-Skyrme solver at import time.

    Args:
        crossing_number: Torus knot crossing number.  Default 5 (proton).
    """
    from ave.topological.faddeev_skyrme import TopologicalHamiltonian1D

    solver = TopologicalHamiltonian1D(
        node_pitch=HBAR / (M_E * C_0),  # = L_NODE (avoid circular ref)
        scaling_coupling=KAPPA_FS,
    )
    return solver.solve_scalar_trace(crossing_number=crossing_number)


I_SCALAR_1D: float = _compute_i_scalar_dynamic(crossing_number=5)

# Toroidal halo geometric volume (Borromean link tensor crossing integral)
# ────────────────────────────────────────────────────────────────────────
# DERIVATION:
#   The proton is a Borromean link (6³₂) of 3 mutually linked flux tubes.
#   Each tube traces a great circle on S³.  The tensor volume of the
#   orthogonal crossing region — the 3D signed intersection integral of
#   3 mutually perpendicular great circles — evaluates to exactly 2:
#
#     V = ∫∫∫ sgn(det[τ₁, τ₂, τ₃]) dτ₁ dτ₂ dτ₃ = 2
#
#   This is a topological invariant: it counts the number of independent
#   chiral orientations of the Borromean linkage (left-handed + right-handed).
#
#   Manuscript references:
#     Book 3, Ch.6 §"Skew-Lines and The Toroidal Halo" — full proof
#     Appendix "Geometric Inevitability" §V_halo=2 — summary
#     FEM verification: 2.001 ± 0.003 (Richardson N→∞, 01_appendices)
#   See also: ave/topological/faddeev_skyrme.py
V_TOROIDAL_HALO: float = 2.0

# Proton mass eigenvalue (self-consistent structural feedback)
# x_core = I_scalar / (1 - V_total · p_c)   then x = x_core + 1.0
_X_CORE: float = I_SCALAR_1D / (1.0 - V_TOROIDAL_HALO * P_C)
PROTON_ELECTRON_RATIO: float = _X_CORE + 1.0

# Mass-stiffened nuclear tension  T_nuc = T_EM · (m_p/m_e)
T_NUC: float = T_EM * PROTON_ELECTRON_RATIO

# Macroscopic Baryonic Phase Shear Scalar (Sagnac geometric boundary bound)
# When translating 1D Fizeau kinematics to macroscopic Topo-Kinematic 3D
# boundaries (Geodynamo, Lunar Heating), the inductive spatial phase flow
# is amplified by the physical density of the baryonic bodies shearing the
# topological LC node field. This matches the exact proton mass eigenvalue.
MACROSCOPIC_BARYON_PHASE_SCALAR: float = PROTON_ELECTRON_RATIO

# MeV conversion factor: mass [kg] → energy [MeV]
_KG_TO_MEV: float = C_0**2 / (e_charge * 1e6)

# =============================================================================
# BARYON RESONANCE LADDER — (2,q) Torus Knot Spectrum
# =============================================================================
#
# Each (2,q) torus knot with crossing number c produces a baryon mass via
# the SAME eigenvalue equation used for the proton:
#   m(c)/m_e = I_scalar(κ_FS/c) / (1 - V_total · p_c) + 1
#
# No parameters are adjusted between states.  The same κ_FS, V_total = 2.0,
# and p_c = 8πα derive the entire spectrum.
#
# The ladder uses only odd q (odd crossing numbers):
#   c=5: Proton (938 MeV)
#   c=7: Δ(1232) resonance
#   c=9: Δ(1620) resonance
#   c=11: Δ(1950) resonance
#   c=13: N(2250) resonance

TORUS_KNOT_CROSSING_NUMBERS: list[int] = [5, 7, 9, 11, 13]


def _compute_baryon_ladder() -> dict[int, dict[str, float]]:
    """Compute the full baryon resonance ladder at import time."""
    ladder = {}
    for c in TORUS_KNOT_CROSSING_NUMBERS:
        if c == 5:
            # Proton already computed above
            i_scalar = I_SCALAR_1D
        else:
            i_scalar = _compute_i_scalar_dynamic(crossing_number=c)
        x_core = i_scalar / (1.0 - V_TOROIDAL_HALO * P_C)
        ratio = x_core + 1.0
        mass_mev = ratio * M_E * _KG_TO_MEV
        ladder[c] = {
            "i_scalar": i_scalar,
            "ratio": ratio,
            "mass_mev": mass_mev,
        }
    return ladder


BARYON_LADDER: dict[int, dict[str, float]] = _compute_baryon_ladder()

# =============================================================================
# NUCLEAR MUTUAL COUPLING CONSTANT (Periodic Table Solver)
# =============================================================================
#
# K_MUTUAL governs the pairwise binding energy between nucleons:
#   ΔE_ij = K_MUTUAL / d_ij
#
# where d_ij is the Euclidean distance between nucleon centres (in fm).
#
# DERIVATION:
#   The mutual inductance between two proton-class nucleons (6³₂ Borromean
#   links) is the vacuum's electromagnetic Coulomb coupling constant:
#
#     α·ℏc = e²/(4πε₀) ≈ 1.440 MeV·fm
#
#   amplified by the internal topological winding of the cinquefoil knot.
#   Each of the c=5 crossings in the proton's (2,5) torus knot contributes
#   a π/2 phase advance to the flux-linkage integral (one quarter-turn of
#   the field lines threading through each over/under crossing).
#
#   Tree-level coupling (ideal, infinite-Q nucleons):
#     K₀ = (c × π/2) × αℏc = (5π/2) × αℏc
#
#   Proximity correction (first-order radiative):
#     At nuclear separations (d ~ r_proton ~ 0.88 fm), the nucleon strain
#     fields deform into each other, concentrating flux and enhancing the
#     effective coupling beyond the geometric prediction.  This is the
#     nuclear analog of transformer proximity effect.
#
#     The correction is:  1/(1 − α/3)
#
#     Physical origin: the α/3 term is the first-order electromagnetic
#     self-energy correction to the mutual coupling, analogous to a
#     vertex correction in QED.  The factor of 1/3 arises from the
#     isotropic 3D spatial averaging of the dipole coupling tensor.
#
#   Full expression:
#     K_MUTUAL = (5π/2) × αℏc / (1 − α/3)
#
#   This yields K ≈ 11.337 MeV·fm, matching the He-4 calibrated value
#   to within 0.005%.  When applied to all 14 analytically-solved nuclei
#   (H through Si), the derived expression produces identical mass-defect
#   mapping errors (0.0000%) to the original calibrated constant.
#
# EE INTERPRETATION:
#   K_MUTUAL is the mutual inductance coefficient of two 5-turn coupled
#   coils (nucleon knots) in an LC medium (vacuum), with a proximity-
#   enhanced coupling factor for close-packed transformer geometry.

# Coulomb coupling constant  αℏc = e²/(4πε₀)  [MeV·fm]
ALPHA_HBAR_C: float = ALPHA * HBAR * C_0 / e_charge * 1e15 * 1e-6
# ℏc in MeV·fm
HBAR_C_MEV_FM: float = HBAR * C_0 / e_charge * 1e15 * 1e-6  # ≈ 197.327 MeV·fm

# Nuclear mutual coupling constant [MeV·fm]
K_MUTUAL: float = (CROSSING_NUMBER_PROTON * pi / 2.0) * ALPHA * HBAR_C_MEV_FM / (1.0 - ALPHA / 3.0)

# =============================================================================
# NUCLEON MASS CONSTANTS (CODATA 2018 empirical — used as binding energy targets)
# =============================================================================
# These are the experimentally measured isolated nucleon rest masses.
# They serve as the target boundary conditions for the topological binding engine.
M_P_MEV_TARGET: float = 938.272088  # Proton mass [MeV/c²]  (CODATA 2018)
M_N_MEV_TARGET: float = 939.565420  # Neutron mass [MeV/c²] (CODATA 2018)

# =============================================================================
# PROTON CHARGE RADIUS (Derived — Axiom 1 + standing wave confinement)
# =============================================================================
# The proton charge radius is the gyroscopic spin radius of the cinquefoil knot:
#   d = 4 × λ_p = 4 × ℏ/(m_p c)
# This is the RMS vibration amplitude of the center-of-mass standing wave
# confined within the 0Ω saturated cavity boundary of one lattice cell.
D_PROTON: float = 4.0 * HBAR / (PROTON_ELECTRON_RATIO * M_E * C_0) * 1e15  # ≈ 0.8412 fm

# Intra-alpha distance: nucleons at vertices of regular tetrahedron
# D_intra = d × √8  (tetrahedral edge from vertex ±(d,d,d))
D_INTRA_ALPHA: float = D_PROTON * np.sqrt(8.0)  # ≈ 2.379 fm

# =============================================================================
# NUCLEAR EIGENVALUE CONSTANTS (Derived — 5-Step Regime Boundary Method)
# =============================================================================
#
# Applying the universal 5-step regime-boundary eigenvalue method to the
# nucleon saturation boundary:
#
# Step 1-2: r_sat = D_PROTON (strain field saturates at proton radius)
# Step 3:   r_eff = D_PROTON / (1 + ν_vac) = D_PROTON × 7/9
# Step 4:   ω₁ = c / r_eff (fundamental ℓ=1 inter-nucleon mode)
# Step 5:   Q = ℓ = 1
#
# The EQUILIBRIUM DISTANCE between two nucleons is the half-wavelength
# of the fundamental standing wave at the saturation boundary:
#   d_nn = λ/2 = πc/ω₁ = π × r_eff = π × D_PROTON × 7/9
#
# The DEUTERON BINDING ENERGY is the eigenvalue energy scaled by α:
#   B_deuteron = ℏω₁ × α  (electromagnetic coupling of the cavity mode)

# NU_VAC already defined at line 127 — use that single definition

# Inter-nucleon eigenvalue distance [fm]
D_NN_EIGENVALUE: float = pi * D_PROTON * 7.0 / 9.0  # ≈ 2.056 fm

# Coulomb coupling constant αℏc [MeV·fm]
ALPHA_HC: float = ALPHA * HBAR_C_MEV_FM  # ≈ 1.440 MeV·fm

# Predicted deuteron binding [MeV]  (ℏω₁ × α where ω₁ = c/r_eff)
_OMEGA_1: float = C_0 / (D_PROTON * 1e-15 / (1.0 + NU_VAC))
B_DEUTERON_PREDICTED: float = HBAR * _OMEGA_1 / e_charge * 1e-6 * ALPHA  # ≈ 2.201 MeV

# =============================================================================
# COUPLED RESONATOR CONSTANTS (Lumped Circuit Nuclear Model)
# =============================================================================
#
# Each nucleon is an LC resonator at frequency ω₀ = c(1+ν)/d_p.
# The coupling coefficient k between two resonators is derived from
# the deuteron binding condition B_d = ℏω₀ × α:
#
#   B_d = ℏω₀(1 - 1/√(1+k)) = ℏω₀ × α
#   → k = 1/(1-α)² - 1 ≈ 2α + 3α² + ...
#
# This is the EE mutual inductance coefficient M/L between two
# nucleon LC tanks at the eigenvalue distance d_nn.

# Uncoupled resonant frequency [rad/s]
OMEGA_0_NUCLEAR: float = _OMEGA_1  # = c(1+ν)/d_p

# Uncoupled resonant energy [MeV]
E_0_NUCLEAR: float = HBAR * OMEGA_0_NUCLEAR / (e_charge * 1e6)  # ≈ 301.6 MeV

# Dimensionless coupling coefficient (from deuteron binding)
K_COUPLING: float = 1.0 / (1.0 - ALPHA) ** 2 - 1.0  # ≈ 0.01476 ≈ 2α

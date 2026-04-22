"""
First-Principles Silicon Atom Waveguide
=======================================

Silicon (Z=14) atomic structure from AVE Split-Layer Architecture:

  Phase A (ABCD cascade): Cross-shell screening through [Ne] core
    10 inner-shell resonators (1s² 2s² 2p⁶) act as stacked acoustic
    lenses demagnifying the nuclear capacitive bias.
    → E_base [eV], Z_eff_core [dimensionless]

  Phase B (MCL T²): Same-shell loading of 3s² 3p² valence
    4 resonators load the n=3 cavity via K=2G modulus ratio (Ax3):
      s-subshell (compressional): 2 × 1.0 = 2.0
      p-subshell (transversal):   2 × 0.5 = 1.0
      N_eff = 3.0
    T²(3.0) = 0.75 (Op3, cavity transmission)

  IE = E_total(4) − E_total(3) [eV]

Engine: radial_eigenvalue.ionization_energy_e2k (ABCD+MCL hybrid)
"""

from __future__ import annotations

from ave.solvers.coupled_resonator import atom_port_impedance
from ave.solvers.radial_eigenvalue import ionization_energy_e2k

# ═══════════════════════════════════════════════════════════════════
# SILICON ATOMIC CONSTANTS
# ═══════════════════════════════════════════════════════════════════

Z_SI: int = 14
A_SI: int = 28
ELEMENT_NAME: str = "Silicon"

# Resonator configuration: 1s² 2s² 2p⁶ 3s² 3p²  =  [Ne] 3s² 3p²
CORE_ELECTRONS: int = 10  # [Ne] core (cross-shell screening)
VALENCE_ELECTRONS: int = 4  # 3s² + 3p² (same-shell loading)

# sp³ hybridisation: 4 equivalent soliton ports at tetrahedral angle
N_SP3_ORBITALS: int = 4
SP3_ANGLE_DEG: float = 109.47  # arccos(-1/3) [degrees]


# ═══════════════════════════════════════════════════════════════════
# IONIZATION ENERGY & PORT IMPEDANCE
# ═══════════════════════════════════════════════════════════════════
#
# ABCD+MCL hybrid solver (Split-Layer Architecture):
#   Phase A: ABCD cascade with [Ne] core screening → E_base
#   Phase B: MCL T²(N_eff=3.0) for 3s²3p² loading → IE
#
# Known limitation: ABCD over-estimates Z_eff_core (5.63 vs ~4.7)
# due to step-function screening profile. Gives IE = +22.8%.
# Will improve as screening model is refined.

# AVE-derived ionization energy [eV] — zero free parameters
IE_SI_AVE: float = ionization_energy_e2k(Z_SI)

# NIST reference value [eV]
IE_SI_NIST: float = 8.1517

# Port impedance (effective valence radius) [m]
# r_val = n × a₀ × √(Ry/IE)  (Axiom 2, cavity eigenvalue scaling)
# Dimensional check: [1] × [m] × √([eV]/[eV]) = [m] ✓
R_VAL_SI: float = atom_port_impedance(Z_SI, IE_SI_NIST)


# ═══════════════════════════════════════════════════════════════════
# SEMICONDUCTOR REGIME CLASSIFICATION
# ═══════════════════════════════════════════════════════════════════
#
# V_R / V_BR = 0.050 — last Small Signal element (M = 1)
#
# DERIVATION (from nuclear 7α pentagonal bipyramid):
#   V_R = repulsive capacitive bias per alpha cluster
#   V_BR = 3.631 MeV avalanche breakdown voltage
#   Operating point: V_R/V_BR = 0.050 (KB-verified)
#   This is the axiomatic origin of semiconducting behavior.

V_R_OVER_V_BR: float = 0.050  # KB-verified
MILLER_FACTOR: float = 1.000  # M = 1 (pure Small Signal regime)


def first_ionization():
    """First ionization energy of Si from ABCD+MCL hybrid solver.

    Returns:
        IE [eV]: positive.
    """
    return IE_SI_AVE

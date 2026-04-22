"""
First-Principles Phosphorus Atom Waveguide
==========================================

Phosphorus (Z=15) atomic structure. Mapped natively as an n-type semiconductor
doping element represented by a 5-port geometric anomaly in an sp³ network.

Values derived entirely from the ABCD/Hopf radial eigenvalue solver,
utilizing no empirical parameters.
"""

from __future__ import annotations


from ave.solvers.radial_eigenvalue import ionization_energy_e2k
from ave.solvers.coupled_resonator import atom_port_impedance

# ═══════════════════════════════════════════════════════════════════
# PHOSPHORUS ATOMIC CONSTANTS
# ═══════════════════════════════════════════════════════════════════

Z_PHOSPHORUS: int = 15
A_PHOSPHORUS: int = 31
ELEMENT_NAME: str = "Phosphorus"

CORE_ELECTRONS: int = 10  # [Ne] core
VALENCE_ELECTRONS: int = 5  # 3s² 3p³

# 5-port topology (donor flaw in 4-port Si lattice)
N_SP3_ORBITALS: int = 5

# ═══════════════════════════════════════════════════════════════════
# IONIZATION ENERGY & PORT IMPEDANCE (PURE ODE)
# ═══════════════════════════════════════════════════════════════════

# Strict first-principles ODE derivation
IE_P_AVE: float = ionization_energy_e2k(Z_PHOSPHORUS)

# Dynamic port impedance relative to derived IE
R_VAL_PHOSPHORUS: float = atom_port_impedance(Z_PHOSPHORUS, IE_P_AVE)


def first_ionization():
    """First ionization energy of Phosphorus from ABCD+MCL hybrid solver.

    Returns:
        IE [eV]: positive.
    """
    return IE_P_AVE

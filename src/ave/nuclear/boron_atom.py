"""
First-Principles Boron Atom Waveguide
=====================================

Boron (Z=5) atomic structure. Mapped natively as a p-type semiconductor
doping element represented by a 3-port geometric anomaly in an sp³ network.

Values derived entirely from the ABCD/Hopf radial eigenvalue solver,
utilizing no empirical parameters.
"""
from __future__ import annotations


import numpy as np

from ave.solvers.radial_eigenvalue import ionization_energy_e2k
from ave.solvers.coupled_resonator import atom_port_impedance

# ═══════════════════════════════════════════════════════════════════
# BORON ATOMIC CONSTANTS
# ═══════════════════════════════════════════════════════════════════

Z_BORON: int = 5
A_BORON: int = 11
ELEMENT_NAME: str = "Boron"

CORE_ELECTRONS: int = 2     # [He] core
VALENCE_ELECTRONS: int = 3  # 2s² 2p¹

# 3-port topology (acceptor flaw in 4-port Si lattice)
N_SP3_ORBITALS: int = 3

# ═══════════════════════════════════════════════════════════════════
# IONIZATION ENERGY & PORT IMPEDANCE (PURE ODE)
# ═══════════════════════════════════════════════════════════════════

# Strict first-principles ODE derivation
IE_B_AVE: float = ionization_energy_e2k(Z_BORON)

# Dynamic port impedance relative to derived IE
R_VAL_BORON: float = atom_port_impedance(Z_BORON, IE_B_AVE)


def first_ionization():
    """First ionization energy of Boron from ABCD+MCL hybrid solver.

    Returns:
        IE [eV]: positive.
    """
    return IE_B_AVE

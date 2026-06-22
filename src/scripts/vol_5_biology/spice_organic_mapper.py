r"""
SPICE Organic Mapper — Zero-Parameter AVE Derivation
=====================================================
Maps organic chemical topologies (atomic nuclei and covalent bonds)
into absolute Inductance (L) and Capacitance (C) values for SPICE
circuit simulation.

DERIVATION (from AVE Axioms 1-4)
---------------------------------
The vacuum lattice is an LC transmission line with per-unit-length
parameters mu_0 [H/m] and eps_0 [F/m].  The topological conversion
constant xi_topo == e / l_node [C/m] maps charge dislocation to
spatial dislocation, providing the universal electromechanical
coupling of the lattice.

  1. Mass -> Inductance
     An atomic nucleus of mass m is a localized inertial defect.
     Inertia == Inductance.  Dimensional transduction via xi^2:

         L_atom = m / xi_topo^2          [H]

  2. Bond Stiffness -> Capacitance
     A covalent bond of stretching force constant k [N/m] is a
     region of dielectric compliance between two massive nodes.
     Compliance == Capacitance:

         C_bond = xi_topo^2 / k           [F]

  Self-consistency checks:
    * f_res = 1/(2 pi sqrt(LC)) = (1/2 pi) sqrt(k/m)   — mechanical resonance
    * Z = sqrt(L/C) = m sqrt(k/m) / xi^2 = sqrt(mk)/xi^2  — mechanical impedance
    * v = 1/sqrt(LC) = sqrt(k/m)               — bond sound speed

  NO FREE PARAMETERS.  All values trace to:
    * CODATA atomic masses  (measured)
    * AVE Soliton Bond Solver force constants  (derived from eps_0, m_e, hbar, e)
    * xi_topo = e / l_node  (derived from e, hbar, m_e, c)

Co-ported from the Applied-Vacuum-Engineering archive to support the Vol-5
FTIR comparison figure; imports resolved against AVE-Core's ave package.
"""

import numpy as np

from ave.core.constants import Z_0, XI_TOPO
from ave.topological.soliton_bond_solver import (
    compute_bond_curve,
    extract_force_constant,
    BOND_DEFS,
)

# =============================================================================
# TRANSDUCTION CONSTANT  xi_topo^2 = (e / l_node)^2  [C^2/m^2]
# =============================================================================
# This is the universal electromechanical coupling of the vacuum lattice.
# It converts mechanical impedance (kg, N/m) into electrical impedance (H, F).
XI_TOPO_SQ: float = XI_TOPO**2   # ~ 1.721e-13  [C^2/m^2]

# =============================================================================
# 1.  ATOMIC INDUCTANCE:  L = m / xi^2   [H]
# =============================================================================
# Atomic masses from CODATA 2018 (in kg).  1 Da = 1.66053906660e-27 kg
_DA = 1.66053906660e-27  # kg per Dalton

ATOMIC_MASS_DA = {
    "H": 1.00794,
    "C": 12.0107,
    "N": 14.0067,
    "O": 15.9994,
    "S": 32.065,
}

ATOMIC_INDUCTANCE = {
    elem: (mass_da * _DA) / XI_TOPO_SQ
    for elem, mass_da in ATOMIC_MASS_DA.items()
}

# =============================================================================
# 2.  BOND CAPACITANCE:  C = xi^2 / k   [F]
# =============================================================================
# Stretching force constants k [N/m] are derived purely from AVE axioms
# (eps_0, m_e, hbar, e) and lattice topology via the Soliton Bond Solver.
# No empirical or spectroscopic parameters are used.
BOND_FORCE_CONSTANTS = {}
for _bond, (_za, _zb, _ne) in BOND_DEFS.items():
    _d_range, _E_array = compute_bond_curve(_za, _zb, _ne, n_points=200)
    _, _k_pred, _ = extract_force_constant(_d_range, _E_array, _za, _zb, _ne)
    BOND_FORCE_CONSTANTS[_bond] = _k_pred

COVALENT_CAPACITANCE = {
    bond: XI_TOPO_SQ / k
    for bond, k in BOND_FORCE_CONSTANTS.items()
}

# =============================================================================
# 3.  FUNCTIONAL GROUP CONSTANTS
# =============================================================================
# Amino Group (NH3+) -> High-frequency source; the biological power supply is
# the ambient THz thermal noise floor.  Wien's law at 310 K: f_peak ~ 30 THz.
AMINO_SOURCE_FREQ = "30THz"
AMINO_SOURCE_VOLT = "1V"
# Carboxyl Group (COO-) -> Vacuum impedance termination (derived, not heuristic).
CARBOXYL_LOAD_R = f"{Z_0:.4f}Ohm"


def get_inductance(element: str) -> float:
    """Return geometric inductance [H] of an atomic node."""
    if element not in ATOMIC_INDUCTANCE:
        raise ValueError(f"Unknown element: {element}")
    return ATOMIC_INDUCTANCE[element]


def get_capacitance(bond: str) -> float:
    """Return dielectric capacitance [F] of a covalent bond."""
    if bond in COVALENT_CAPACITANCE:
        return COVALENT_CAPACITANCE[bond]
    rev = f"{bond[-1]}{bond[1:-1]}{bond[0]}"  # reverse lookup, e.g. 'H-C' -> 'C-H'
    if rev in COVALENT_CAPACITANCE:
        return COVALENT_CAPACITANCE[rev]
    raise ValueError(f"Unknown bond: {bond}")


def get_force_constant(bond: str) -> float:
    """Return stretching force constant [N/m] of a covalent bond."""
    if bond in BOND_FORCE_CONSTANTS:
        return BOND_FORCE_CONSTANTS[bond]
    rev = f"{bond[-1]}{bond[1:-1]}{bond[0]}"
    if rev in BOND_FORCE_CONSTANTS:
        return BOND_FORCE_CONSTANTS[rev]
    raise ValueError(f"Unknown bond: {bond}")


if __name__ == "__main__":
    import numpy as _np

    print("=" * 65)
    print("  AVE Organic SPICE Mapper — Zero-Parameter Derivation")
    print("=" * 65)
    print(f"\n  Transduction constant  xi_topo = {XI_TOPO:.6e} C/m")
    print(f"  Transduction squared   xi^2    = {XI_TOPO_SQ:.6e} C^2/m^2")

    print("\n  --- Atomic Inductances  L = m / xi^2  [fH] ---")
    for elem in ["H", "C", "N", "O", "S"]:
        L = ATOMIC_INDUCTANCE[elem]
        print(f"    {elem:2s}:  {L*1e15:10.3f} fH   (m = {ATOMIC_MASS_DA[elem]:.3f} Da)")

    print("\n  --- Bond Capacitances   C = xi^2 / k  [aF] ---")
    for bond in ["C-H", "C-C", "C=C", "C-N", "C=O", "C-O", "N-H", "O-H", "S-H", "C-S"]:
        C = COVALENT_CAPACITANCE[bond]
        k = BOND_FORCE_CONSTANTS[bond]
        print(f"    {bond:4s}: {C*1e18:10.3f} aF   (k = {k:6.0f} N/m)")

    from ave.core.constants import C_0
    L_C = ATOMIC_INDUCTANCE["C"]
    L_H = ATOMIC_INDUCTANCE["H"]
    C_CH = COVALENT_CAPACITANCE["C-H"]
    L_red = (L_C * L_H) / (L_C + L_H)
    f_res = 1.0 / (2 * _np.pi * _np.sqrt(L_red * C_CH))
    nu_cm = f_res / (C_0 * 100)
    print("\n  --- Self-consistency: C-H stretch ---")
    print(f"    f_res = {f_res:.3e} Hz  ~ {nu_cm:.0f} cm^-1  (expect ~3000 cm^-1)")
    print(f"\n  Carboxyl load: {CARBOXYL_LOAD_R}")

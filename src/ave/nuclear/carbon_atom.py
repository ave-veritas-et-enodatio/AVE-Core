"""
Carbon Atom Framework
=====================
Z=6, extreme amphoteric phase slip node in heavy matrices.
"""

from __future__ import annotations

from ave.solvers.radial_eigenvalue import ionization_energy_e2k

Z_CARBON: int = 6
IE_C_AVE: float = ionization_energy_e2k(Z_CARBON)

"""
Germanium Atom Framework
========================
Z=32, operates structurally past the avalanche linear threshold.
"""

from __future__ import annotations

from ave.solvers.radial_eigenvalue import ionization_energy_e2k

Z_GERMANIUM: int = 32
A_GERMANIUM: int = 72
ELEMENT_NAME: str = "Germanium"
IE_GE_AVE: float = ionization_energy_e2k(Z_GERMANIUM)

"""
Gallium Atom Framework
======================
Z=31, Amphoteric Matrix Acceptor.
"""
from __future__ import annotations

from ave.solvers.radial_eigenvalue import ionization_energy_e2k

Z_GALLIUM: int = 31
IE_GA_AVE: float = ionization_energy_e2k(Z_GALLIUM)

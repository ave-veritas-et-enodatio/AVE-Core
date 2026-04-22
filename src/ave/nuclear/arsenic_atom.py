"""
Arsenic Atom Framework
======================
Z=33, Amphoteric Matrix Donor.
"""

from ave.solvers.radial_eigenvalue import ionization_energy_e2k

Z_ARSENIC: int = 33
IE_AS_AVE: float = ionization_energy_e2k(Z_ARSENIC)

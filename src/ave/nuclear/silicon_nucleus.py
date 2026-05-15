"""
First-Principles Silicon Nucleus Model (Z=14)
=============================================

Derives the nuclear mass and total mesoscopic binding targets mapped
strictly to the generic Alpha-Coupled Resonator matrix derived
from Vacuum Circuit Analysis (VCA) axioms.

No curve fits. 14 Protons + 14 Neutrons inherently construct into
a topologically packed K_N graph of 7 localized alpha knots.
"""

from ave.solvers.coupled_resonator import nuclear_mass


def silicon_nucleus_binding() -> tuple[float, float]:
    """
    Computes the base assembly binding resonance for Z=14, A=28.

    Returns:
        mass_excess_MeV: The net defect against the continuous spectrum.
        Z_binding_target_MeV: The scalar binding energy from the Hop links.
    """
    # Z=14, A=28, forcing 7 discrete structural alphas directly
    mass_excess_MeV, Z_binding_target_MeV = nuclear_mass(14, 28, n_alphas=7)
    return mass_excess_MeV, Z_binding_target_MeV

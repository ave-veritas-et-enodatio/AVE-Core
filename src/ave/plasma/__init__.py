"""
AVE Plasma Physics Module
=========================
Plasma and superconductor implementations of the universal saturation operator.
"""

from __future__ import annotations


from ave.plasma.superconductor import (
    # Core saturation functions (magnetic dual of plasma)
    critical_field,
    meissner_mu_eff,
    superconducting_impedance,
    meissner_reflection,
    # London penetration depth
    london_penetration_depth,
    coherence_length,
    ginzburg_landau_kappa,
    # Data classes and catalog
    SuperconductorProperties,
    SC_CATALOG,
)

from ave.plasma.cutoff import (
    ave_plasma_frequency,
    dielectric_function_ave,
    electron_density_from_frequency,
)

__all__ = [
    # Superconductor
    "critical_field",
    "meissner_mu_eff",
    "superconducting_impedance",
    "meissner_reflection",
    "london_penetration_depth",
    "coherence_length",
    "ginzburg_landau_kappa",
    "SuperconductorProperties",
    "SC_CATALOG",
    # Plasma
    "ave_plasma_frequency",
    "dielectric_function_ave",
    "electron_density_from_frequency",
]

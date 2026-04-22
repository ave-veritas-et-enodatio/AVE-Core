"""
AVE Plasma Physics Module
=========================
Plasma and superconductor implementations of the universal saturation operator.
"""

from __future__ import annotations

from ave.plasma.cutoff import ave_plasma_frequency, dielectric_function_ave, electron_density_from_frequency
from ave.plasma.superconductor import (  # Core saturation functions (magnetic dual of plasma); London penetration depth; Data classes and catalog
    SC_CATALOG,
    SuperconductorProperties,
    coherence_length,
    critical_field,
    ginzburg_landau_kappa,
    london_penetration_depth,
    meissner_mu_eff,
    meissner_reflection,
    superconducting_impedance,
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

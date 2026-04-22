"""
AVE Axioms Package
-------------------
Computable implementations of the four fundamental AVE axioms.
"""

from __future__ import annotations


from .saturation import (
    epsilon_eff,
    capacitance_eff,
    reflection_coefficient,
    local_wave_speed,
    energy_density_nonlinear,
)
from .isomorphism import (
    charge_to_length,
    length_to_charge,
    ohms_to_kinematic,
    impedance_electrical_to_mechanical,
)

__all__ = [
    "epsilon_eff",
    "capacitance_eff",
    "reflection_coefficient",
    "local_wave_speed",
    "energy_density_nonlinear",
    "charge_to_length",
    "length_to_charge",
    "ohms_to_kinematic",
    "impedance_electrical_to_mechanical",
]

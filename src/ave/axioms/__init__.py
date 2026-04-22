"""
AVE Axioms Package
-------------------
Computable implementations of the four fundamental AVE axioms.
"""

from .isomorphism import charge_to_length, impedance_electrical_to_mechanical, length_to_charge, ohms_to_kinematic
from .saturation import capacitance_eff, energy_density_nonlinear, epsilon_eff, local_wave_speed, reflection_coefficient

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

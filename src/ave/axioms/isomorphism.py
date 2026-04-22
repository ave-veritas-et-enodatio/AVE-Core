"""
Axiom 2: The Topo-Kinematic Isomorphism
========================================
Charge q is defined identically as a discrete geometric dislocation
within the M_A electromagnetic network. Therefore, the fundamental
dimension of charge is strictly identical to length: [Q] ≡ [L].

The macroscopic scaling is rigidly defined by the Topological Conversion
Constant:
    ξ_topo ≡ e / ℓ_node   [Coulombs / Meter]

This module provides exact dimensional conversion functions between
electrical and mechanical domains.
"""

from __future__ import annotations

from ave.core.constants import XI_TOPO


def charge_to_length(charge_coulombs: float) -> float:
    """
    Convert an electrical charge [C] to its equivalent spatial dislocation [m].

    x = Q / ξ_topo

    Args:
        charge_coulombs: Charge in Coulombs.

    Returns:
        Spatial dislocation in meters.
    """
    return charge_coulombs / XI_TOPO


def length_to_charge(length_meters: float) -> float:
    """
    Convert a spatial dislocation [m] to its equivalent electrical charge [C].

    Q = ξ_topo · x

    Args:
        length_meters: Spatial dislocation in meters.

    Returns:
        Charge in Coulombs.
    """
    return XI_TOPO * length_meters


def ohms_to_kinematic(impedance_ohms: float) -> float:
    """
    Convert electrical impedance [Ω] to kinematic impedance [kg/s].

    Z_mech = ξ_topo² · Z_elec

    Derived from: 1 Ω = 1 V/A = 1 J·s/C² ≡ ξ⁻² [kg/s]
    Therefore: Z_mech = ξ² · Z_elec when using natural topological units.

    Note: The manuscript uses Z_elec = ξ⁻² Z_mech, which is equivalent
    to Z_mech = ξ² · Z_elec.

    Args:
        impedance_ohms: Electrical impedance in Ohms.

    Returns:
        Mechanical impedance in kg/s.
    """
    return XI_TOPO**2 * impedance_ohms


def impedance_electrical_to_mechanical(z_electrical: float) -> float:
    """
    Alias for ohms_to_kinematic. Maps electrical impedance to mechanical.

    Z_mech = ξ_topo² · Z_elec   [kg/s]
    """
    return ohms_to_kinematic(z_electrical)


def mechanical_to_electrical(z_mechanical: float) -> float:
    """
    Inverse: convert kinematic impedance [kg/s] to electrical impedance [Ω].

    Z_elec = Z_mech / ξ_topo²
    """
    return z_mechanical / XI_TOPO**2


def vector_potential_to_mass_flow(A_field: float) -> float:
    """
    The magnetic vector potential A has dimensions of [Wb/m] = [V·s/m].

    Under the topo-kinematic isomorphism:
    [A] = ξ_topo⁻¹ [kg/s]

    Physically: A is isomorphic to the mass flow rate (linear momentum density)
    of the vacuum lattice, scaled by 1/ξ_topo.

    Args:
        A_field: Magnitude of the magnetic vector potential [Wb/m].

    Returns:
        Equivalent mass flow rate [kg/s] (scaled by ξ_topo⁻¹).
    """
    return A_field * XI_TOPO

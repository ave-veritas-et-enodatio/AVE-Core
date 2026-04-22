"""
Galactic MOND Drag Engine
=========================

Derives the universal compliance bounds of the K4 metric.
Establishes the structural scale threshold a_0.
Computes effective velocity curves across the Regime III / Regime IV boundary
where the galactic metric either acts as an irrotational lossess fluid (Newtonian)
or an intact inductive compliance network (MOND/Dark Matter equivalent).
"""

import numpy as np

from ave.core.constants import ALPHA, C_0, HBAR, M_E, G


def get_hubble_infinity() -> float:
    """
    Computes the cosmological upper bound scaling constant H_infinity
    strictly from Axiom fundamentals.
    """
    numerator = 28.0 * np.pi * (M_E**3) * C_0 * G
    denominator = (HBAR**2) * (ALPHA**2)
    return numerator / denominator


def get_a0() -> float:
    """
    Computes the universally derived Phase Compliance boundary threshold a_0
    where the metric unsaturates into Regime III.

    Returns:
        a_0 [m/s^2]
    """
    H_inf = get_hubble_infinity()
    return (C_0 * H_inf) / (2.0 * np.pi)


def compliance_operator(g_n: float, a_0: float) -> float:
    """
    S(r = g_n/a_0)

    If g_n >= a_0 (r >= 1.0), local metric is Ruptured (Saturated). S = 0.
    If g_n < a_0 (r < 1.0), local metric is Intact (Unsaturated). S = sqrt(1 - r^2).
    """
    r = g_n / a_0
    if r >= 1.0:
        return 0.0
    return np.sqrt(1.0 - r**2)


def effective_galactic_acceleration(g_n: float, a_0: float) -> float:
    """
    Computes the total transverse acceleration equivalent
    binding galactic fluid orbits.

    g_eff = g_n + sqrt(g_n * a_0) * S(g_n/a_0)

    In the deep core (Regime IV), g_eff = g_n.
    At the extreme edges (Regime I), S -> 1, g_eff ~ sqrt(g_n * a_0).
    """
    S = compliance_operator(g_n, a_0)
    drag_equivalent = np.sqrt(g_n * a_0) * S
    return g_n + drag_equivalent


def calculate_rotation_velocity(radius_m: float, mass_enclosed_kg: float, a_0: float) -> tuple[float, float, str]:
    """
    Calculates the combined topological orbital velocity given a raw baryonic mass.

    Returns:
        v_eff [m/s]
        g_eff [m/s^2]
        Regime String
    """
    g_n = (G * mass_enclosed_kg) / (radius_m**2)

    r_ratio = g_n / a_0

    if r_ratio >= 1.0:
        regime = "Regime IV (Saturated/Keplerian)"
    else:
        regime = "Regime III-I (Intact/MOND)"

    g_eff = effective_galactic_acceleration(g_n, a_0)
    v_eff = np.sqrt(radius_m * g_eff)

    return v_eff, g_eff, regime

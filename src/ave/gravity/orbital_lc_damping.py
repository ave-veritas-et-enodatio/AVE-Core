"""
Orbital LC Damping
==================

Derives Gravitational Waves strictly as Real Power Transmission Line Damping.
Stable planetary orbits operate as Lossless LC Tanks (P = 0 Watts), trapping
orbital traversal energy fully in the Reactive Power domain (Q).

Due to strictly finite wave-speed propagation (c) of the topological metric,
binary configurations experience a retardation transit delay. This induces a
geometric phase slip (delta) between the Voltage and Current. 

Because linear dipole radiation is nullified by momentum conservation, the 
lowest mode coupling is the quadrupole, causing the slip to scale strictly as (v/c)^5.
"""

import numpy as np
from ave.core.constants import G, C_0


def orbital_reactive_power(m1: float, m2: float, a: float) -> float:
    """
    Computes the Reactive Apparent Power (Q) of the Keplerian LC Tank.
    This represents the total trapped energy flux alternating between
    radial displacement and tangential inertial velocity.

    Q = F_g * v_orb

    Args:
        m1, m2: Masses [kg]
        a: Semi-major axis [m]

    Returns:
        Q [VARs (Watts equivalent)]
    """
    M_total = m1 + m2
    F_g = (G * m1 * m2) / (a**2)
    v_orb = np.sqrt(G * M_total / a)
    return F_g * v_orb


def quadrupole_phase_slip(Q_base: float, e: float = 0.0) -> float:
    """
    Computes the irreversible angular phase slip (delta) caused by the
    topological transit delay of the vacuum metric between the masses.

    Delta evaluates to exactly the fraction of Reactive Power pushing
    against the absolute maximum Planck Luminosity (c^5 / G) of the vacuum.

    Args:
        Q_base: Reactive orbital power [VARs]
        e: Eccentricity

    Returns:
        delta [radians] (Apparent transmission line lag)
    """
    P_planck = (C_0**5) / G
    k_quad = 32.0 / 5.0
    f_e = (1.0 + (73.0 / 24.0) * e**2 + (37.0 / 96.0) * e**4) / (1.0 - e**2) ** 3.5

    delta = k_quad * (Q_base / P_planck) * f_e
    return delta


def real_power_damping(Q: float, delta: float) -> float:
    """
    Calculates the Real Power (Watts) dissipated continuously into the vacuum
    lattice as standard Transmission Line Damping.

    P_real = Q * sin(delta) ~ Q * delta

    Args:
        Q: Reactive Power [VARs]
        delta: Phase angle slip [rad]

    Returns:
        P_real [W] (Equivalent to traditional P_GW)
    """
    return Q * delta


def orbital_period_decay_rate(P_gw: float, m1: float, m2: float, a: float) -> float:
    """
    Computes the strictly geometric decay rate of the orbital period
    due to Real Power dissipation.

    Args:
        P_gw: Real Power radiated [W]
        m1, m2: Masses [kg]
        a: Semi-major axis [m]

    Returns:
        dP_b / dt [dimensionless s/s]
    """
    M_total = m1 + m2
    P_b = 2.0 * np.pi * np.sqrt((a**3) / (G * M_total))

    # Binding energy of the Keplerian LC well
    E_bind = (G * m1 * m2) / (2.0 * a)

    # dP_b/dt = - (3 P_b / 2 E_bind) * P_gw
    decay_rate = -3.0 * P_b * P_gw / (2.0 * E_bind)
    return decay_rate

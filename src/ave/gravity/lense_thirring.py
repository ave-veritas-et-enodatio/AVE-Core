"""
AVE First-Principles Lense-Thirring / Gravitomagnetic Module.

Under Axiom 1 and 3, a spinning mass acts as a rotating flux-ring in the
K4 vacuum lattice. The spin angular momentum J couples to the lattice in the
gravitomagnetic sector, creating frame-dragging (the Lense-Thirring effect).

Axiom chain:
    Axiom 1: Radial TL analogy -- J is the "magnetic flux" of the inductor
    Axiom 3: G = hbar c / (7 xi m_e^2) sets the Machian boundary impedance
    Op3:     Gamma = (Z2 - Z1)/(Z2 + Z1) -- reflection at lattice boundary

Dimensional audit (all formulas):
    B_gm = G J / (c^2 r^3)     [m^3/(kg s^2)] x [kg m^2/s] / [m^2/s^2 x m^3]
                                 = m^3 kg m^2 s^2 / (kg s^2 m^2 s m^5)
                                 = 1/s = [rad/s]  OK

    Omega_LT = 2 G J / (c^2 r^3)  -- same units [rad/s]  OK

    A_gm = B_gm / omega_Compton   -- [rad/s] / [rad/s] = dimensionless  OK
           where omega_Compton = M_E c^2 / hbar  (fundamental lattice rate)

    P_gw = 32 G / (5 c^5) * J^2 * omega^4
         = [m^3/(kg s^2)] x [kg m^2/s]^2 x [1/s]^4 / [m^5/s^5]
         = m^3 kg m^4 s^5 / (kg s^2 s^2 s^4 m^5)
         = kg m^2 / s^3 = [W]  OK

    J = I * omega  [kg m^2/s]  OK (always passed in, not recomputed here)
"""

import numpy as np
from ave.core.constants import G, C_0, HBAR, M_E


# ── Derived gravitomagnetic constants ────────────────────────────────────────

# Compton angular frequency of the electron (fundamental K4 lattice rate)
# omega_Compton = M_E c^2 / hbar  [rad/s]
# This is the reference frequency for the gravitomagnetic strain check (Axiom 4)
OMEGA_COMPTON = M_E * C_0**2 / HBAR  # ~ 7.76e20 rad/s

# Gravitational wave power denominator: Z_gw = 5 c^5 / (32 G)  [W]
# P_gw = J^2 * omega^4 / Z_gw
Z_GW = (5.0 * C_0**5) / (32.0 * G)  # ~ 1.80e52 W


def gravitomagnetic_vector(J_vec: np.ndarray, r_vec: np.ndarray) -> np.ndarray:
    """
    Computes the gravitomagnetic field vector at a given position.

    Gravitomagnetic dipole field (spin sector, linearised GR):
        B_gm = (G / c^2 r^3) * [3 (J.r_hat) r_hat - J]

    Dimensional analysis:
        G [m^3/(kg s^2)], J [kg m^2/s], r [m]
        G J / (c^2 r^3) = m^3/(kg s^2) * kg m^2/s / (m^2/s^2 * m^3)
                        = m^5/(s^3) / (m^5/s^2) = 1/s = [rad/s]  OK

    Args:
        J_vec: Spin angular momentum vector (3,) [kg m^2 / s]
        r_vec: Position vector from spinning body (3,) [m]

    Returns:
        B_gm_vec: Gravitomagnetic field vector (3,) [rad/s]
    """
    r_mag = np.linalg.norm(r_vec)
    if r_mag == 0.0:
        return np.zeros(3)
    r_hat = r_vec / r_mag
    prefactor = G / (C_0**2 * r_mag**3)
    B_gm_vec = prefactor * (3.0 * np.dot(J_vec, r_hat) * r_hat - J_vec)
    return B_gm_vec  # [rad/s]


def gravitomagnetic_field(J: float, r: float) -> float:
    """
    Scalar gravitomagnetic field on the spin axis.

    B_gm = G J / (c^2 r^3)   [rad/s]

    Args:
        J: Angular momentum magnitude [kg m^2 / s]
        r: Distance from centre [m]

    Returns:
        B_gm [rad/s]
    """
    return G * abs(J) / (C_0**2 * r**3)  # [rad/s]


def lense_thirring_precession(J: float, r: float) -> float:
    """
    Lense-Thirring precession rate for a satellite at orbital radius r.

    Omega_LT = 2 G J / (c^2 r^3)   [rad/s]

    Standard GR result; recovered exactly in AVE from Op3 reflection
    at the gravitomagnetic lattice boundary.

    Args:
        J: Angular momentum of the primary [kg m^2 / s]
        r: Orbital radius of the satellite [m]

    Returns:
        Omega_LT [rad/s]
    """
    return 2.0 * G * abs(J) / (C_0**2 * r**3)  # [rad/s]


def gravitational_wave_power(J: float, omega: float) -> float:
    """
    Gravitational wave emission power from a spinning non-spherical body.

    For a body with spin angular momentum J = I omega, the GW luminosity
    (quadrupole approximation, slowly rotating limit) is:

        P_gw = J^2 * omega^4 / Z_gw      where Z_gw = 5 c^5 / (32 G)

    Dimensional analysis:
        J [kg m^2/s], omega [rad/s], Z_gw [W]
        J^2 omega^4 / Z_gw = [kg m^2/s]^2 * [1/s]^4 / [W]
                           = [kg^2 m^4/s^2] * [1/s^4] / [kg m^2/s^3]
                           = [kg^2 m^4 s^3] / [s^6 kg m^2]
                           = [kg m^2 / s^3] = [W]  OK

    NOTE: For a perfectly spherical, uniformly spinning body the
    quadrupole moment is time-invariant and P_gw = 0 exactly.
    This formula applies to bodies with non-zero ellipticity.
    Planet-scale ellipticities are ~1e-3 to ~1e-5, so actual P_gw
    is further suppressed by epsilon^2.  The dominant coupling to the
    K4 lattice for spinning spheres is the Lense-Thirring precession
    (conservative, not dissipative).

    Args:
        J:     Angular momentum magnitude [kg m^2 / s]
        omega: Rotation rate [rad/s]

    Returns:
        P_gw [W]  (upper bound; multiply by epsilon^2 for real bodies)
    """
    return J**2 * omega**4 / Z_GW  # [W]


def strain_amplitude(B_gm: float) -> tuple:
    """
    Gravitomagnetic strain amplitude (Axiom 4 saturation check).

    The dimensionless strain is referenced to the Compton angular frequency
    of the electron -- the fundamental K4 lattice oscillation rate:

        A_gm = B_gm / omega_Compton

    where omega_Compton = M_E c^2 / hbar ~ 7.76e20 rad/s.

    Dimensional analysis:
        B_gm [rad/s] / omega_Compton [rad/s] = dimensionless  OK

    For all solar-system bodies: A_gm << sqrt(2 alpha) ~ 0.121 (Regime I).
    Linear Lense-Thirring holds; no saturation correction required.

    Args:
        B_gm: Gravitomagnetic field magnitude [rad/s]

    Returns:
        A_gm: Dimensionless strain amplitude
        regime: Regime classification string
    """
    A_gm = abs(B_gm) / OMEGA_COMPTON  # dimensionless
    # Regime boundaries from LIVING_REFERENCE Universal Regime Map
    R_I_BOUNDARY = (2.0 * 7.2973525693e-3) ** 0.5  # sqrt(2 alpha) ~ 0.121
    if A_gm < R_I_BOUNDARY:
        regime = "Regime I (Linear)"
    elif A_gm < (3.0**0.5 / 2.0):
        regime = "Regime II (Nonlinear)"
    elif A_gm < 1.0:
        regime = "Regime III (Yield)"
    else:
        regime = "Regime IV (Rupture)"
    return A_gm, regime


def fluid_spin_flux(rho_func, omega_func, r_max: float, n_steps: int = 200) -> float:
    """
    Integrates the total spin angular momentum for a stratified fluid body.

    J = integral rho(r) omega(r,theta) [r sin(theta)]^2 dV

    Used for the Sun and gas giants where omega varies with latitude (r, theta).
    For solid bodies, use J = I * omega directly.

    Args:
        rho_func:  callable(r) -> density [kg/m^3]
        omega_func: callable(r, theta) -> angular velocity [rad/s]
        r_max:     Maximum radius [m]
        n_steps:   Integration resolution

    Returns:
        J_total [kg m^2 / s]
    """
    r_edges = np.linspace(0.0, r_max, n_steps + 1)
    theta_edges = np.linspace(0.0, np.pi, n_steps + 1)
    r_centers = 0.5 * (r_edges[:-1] + r_edges[1:])
    theta_centers = 0.5 * (theta_edges[:-1] + theta_edges[1:])
    dr = r_max / n_steps
    dtheta = np.pi / n_steps

    J_total = 0.0
    for r in r_centers:
        rho = rho_func(r)
        if rho <= 0.0:
            continue
        for theta in theta_centers:
            omega = omega_func(r, theta)
            dV = 2.0 * np.pi * r**2 * np.sin(theta) * dr * dtheta  # [m^3]
            r_perp = r * np.sin(theta)  # [m]
            J_total += rho * dV * r_perp**2 * omega
    return J_total  # [kg m^2 / s]

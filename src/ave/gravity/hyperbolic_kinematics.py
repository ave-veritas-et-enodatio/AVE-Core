"""
AVE Topo-Kinematic Flyby Anomaly Integrator.

Simulates empirical spacecraft Earth-flyby transits through the rotating K4 lattice
(the "Gravitational AC Stator"). Evaluates the native Universal Operator for
gravitomagnetic induction:
    a_gm = lambda_op * (v_sc x B_gm)
"""

import numpy as np
import scipy.integrate as integrate

from ave.gravity.lense_thirring import gravitomagnetic_vector


def compute_hyperbolic_flyby_anomaly(
    r_periapsis: float,
    v_inf: float,
    inclination: float,
    G_M: float,
    J_vec: np.ndarray,
    lambda_op: float = 2.0,
    t_span: float = 20000.0,
    rotation_matrix: np.ndarray = None,
) -> dict:
    """
    Integrates the spacecraft trajectory numerically, coupling to the
    rotating vacuum LC metric via the a_gm phase-drag operator.

    To eliminate RK4 numeric drift from the conservative Newtonian potential,
    we compute the trajectory TWICE (once with lambda=0, once with lambda_op)
    and difference the asymptotic velocities.

    Args:
        r_periapsis: Periapsis radius from body center [m]
        v_inf: Asymptotic incoming velocity at infinity [m/s]
        inclination: Orbital plane inclination relative to equator [rad]
        G_M: Standard gravitational parameter of the primary [m^3 / s^2]
        J_vec: Spin angular momentum vector of the primary [kg m^2 / s]
        lambda_op: Topo-Kinematic strain operator (classic GR = 2.0)
        t_span: Total integration time +- seconds from periapsis [s]
        rotation_matrix: Optional 3x3 matrix to rotate the entire orbit.

    Returns:
        dict containing classical, empirical, and topological delta_V
    """
    mu = G_M
    v_peri = np.sqrt(v_inf**2 + 2.0 * mu / r_periapsis)

    # Initialize at periapsis on the x-axis.
    # Velocity is inclined to the equator (xy-plane).
    r_0 = np.array([r_periapsis, 0.0, 0.0])
    v_0 = np.array([0.0, v_peri * np.cos(inclination), v_peri * np.sin(inclination)])

    if rotation_matrix is not None:
        r_0 = rotation_matrix @ r_0
        v_0 = rotation_matrix @ v_0

    def get_derivatives(l_op):
        def derivatives(t, y):
            r_vec = y[0:3]
            v_vec = y[3:6]
            r_mag = np.linalg.norm(r_vec)

            # Newtonian core gravity
            a_newton = -mu / (r_mag**3) * r_vec

            # Gravitomagnetic Phase Slip / LC Induction
            if l_op == 0.0:
                a_gm = np.zeros(3)
            else:
                B_gm = gravitomagnetic_vector(J_vec, r_vec)
                a_gm = l_op * np.cross(v_vec, B_gm)

            return np.concatenate((v_vec, a_newton + a_gm))

        return derivatives

    results = {}
    for label, l_op in [("classical", 0.0), ("topo", lambda_op)]:
        derivs = get_derivatives(l_op)

        # Integrate backwards
        sol_in = integrate.solve_ivp(
            derivs,
            [0, -t_span],
            np.concatenate((r_0, v_0)),
            rtol=1e-11,
            atol=1e-11,
            method="DOP853",
        )
        v_in_vec = sol_in.y[3:6, -1]

        # Integrate forwards
        sol_out = integrate.solve_ivp(
            derivs, [0, t_span], np.concatenate((r_0, v_0)), rtol=1e-11, atol=1e-11, method="DOP853"
        )
        v_out_vec = sol_out.y[3:6, -1]

        v_in_mag = np.linalg.norm(v_in_vec)
        v_out_mag = np.linalg.norm(v_out_vec)
        results[label] = v_out_mag - v_in_mag

    net_anomaly = results["topo"] - results["classical"]

    return {
        "v_peri": v_peri,
        "delta_v_numeric_drift": results["classical"],
        "delta_v_topo_total": results["topo"],
        "net_anomaly_ms": net_anomaly,
        "net_anomaly_mms": net_anomaly * 1000.0,
    }


def compute_acoustic_sagnac_drag(
    v_inf: float,
    omega_stator: float,
    R_stator: float,
    declination_in: float,
    declination_out: float,
) -> float:
    """
    Computes the Earth Flyby Anomaly Delta-V by evaluating the
    Macroscopic Sagnac-RLVE Shear Layer crossing.

    This native AVE operator models the solid planet acting as a
    Gravitational Stator, whose saturated rigid boundary creates an
    acoustic phase-slip against the free K4 vacuum LC network.

    The derivation natively recovers Anderson's Empirical Formula:
        dV/V = 2 * (U_stator / C_0) * (cos(delta_in) - cos(delta_out))

    Dimensional Analysis:
        U_stator [m/s] / C_0 [m/s] = dimensionless multiplier.
        dV = dimensionless * v_inf [m/s] = [m/s]. OK.

    Args:
        v_inf: Asymptotic velocity of spacecraft [m/s]
        omega_stator: Stator angular velocity [rad/s]
        R_stator: Solid stator acoustic boundary radius [m]
        declination_in: Incoming velocity declination relative to equator [rad]
        declination_out: Outgoing velocity declination relative to equator [rad]

    Returns:
        Delta_V [m/s] phase anomaly
    """
    from ave.core.constants import C_0

    U_stator = omega_stator * R_stator
    phase_slip_factor = 2.0 * (U_stator / C_0)
    geometric_projection = np.cos(declination_in) - np.cos(declination_out)

    delta_v_ms = v_inf * phase_slip_factor * geometric_projection
    return delta_v_ms

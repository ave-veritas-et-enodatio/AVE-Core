"""
Simulate Galactic Rotation Curve (Milky Way Edge)

Plots the geometric rotation curve radially outwards from the Galactic Core.
Identifies the exact physical radius where fundamental metric Saturation (Regime IV)
decays, and the intact lattice imposes macroscopic "Dark Matter" MOND drag (Regimes I-III).
"""

import numpy as np

from ave.core.constants import M_SUN, G
from ave.gravity.galactic_mond_drag import calculate_rotation_velocity, get_a0

KPC_TO_M = 3.086e19

# Rough Milky Way mass models
M_BULGE = 2.0e10 * M_SUN
R_BULGE_KPC = 2.0

M_DISK = 6.0e10 * M_SUN
R_DISK_SCALE_KPC = 3.0


def enclosed_baryonic_mass(r_kpc: float) -> float:
    """
    Approximates the total raw baryonic mass enclosed at radius R.
    """
    # Simple Plummer bulge
    m_bd = M_BULGE * (r_kpc**3 / (r_kpc**2 + R_BULGE_KPC**2) ** 1.5)

    # Simple Exponential Disk
    # Mass = M_tot * (1 - e^(-r/h) * (1 + r/h))
    x = r_kpc / R_DISK_SCALE_KPC
    m_dd = M_DISK * (1.0 - np.exp(-x) * (1.0 + x))

    return m_bd + m_dd


def simulate_galactic_curve():
    print("=== AVE PHASE 4: GALACTIC EDGE AND MOND TRANSITION ===")

    a_0 = get_a0()
    print(f"Derived Universal Saturation Bound (a_0): {a_0:.4e} m/s^2\\n")

    radii_kpc = np.linspace(1.0, 50.0, 50)

    transition_boundary_kpc = None

    print(
        f"{'R (kpc)':<10} | {'M_enc (M_sun)':<15} | {'g_N (m/s^2)':<15}"
        f" | {'v_Newton (km/s)':<18} | {'v_Topo (km/s)':<18} | {'Regime'}"
    )
    print("-" * 105)

    for r_kpc in radii_kpc:
        r_m = r_kpc * KPC_TO_M
        m_enc = enclosed_baryonic_mass(r_kpc)

        # Purely Newtonian equivalent limits
        g_n_base = (G * m_enc) / (r_m**2)
        v_newton = np.sqrt(r_m * g_n_base)

        # AVE Topo-Kinematic Limits
        v_eff, g_eff, regime = calculate_rotation_velocity(r_m, m_enc, a_0)

        v_newt_km = v_newton / 1000.0
        v_eff_km = v_eff / 1000.0
        m_enc_s = m_enc / M_SUN

        # Track the exact boundary limit
        if "Regime III" in regime and transition_boundary_kpc is None:
            transition_boundary_kpc = r_kpc
            print("-" * 105)  # Mark the boundary graphically

        print(
            f"{r_kpc:<10.1f} | {m_enc_s:<15.2e} | {g_n_base:<15.2e} | {v_newt_km:<18.2f} | {v_eff_km:<18.2f} | {regime}"
        )

    print("\\n=== TRANSITION ANALYSIS ===")
    if transition_boundary_kpc:
        print(f"Metric Rupture Boundary (Dark Matter engagement): Exactly {transition_boundary_kpc:.1f} kpc.")
        print("Past this radius, the vacuum metric fundamentally unsaturates, regaining elasticity.")
        print(
            "This intact geometry actively resists macroscopic velocity vectors, naturally flattening the"
            " rotation curve without phantom particle halos."
        )
    else:
        print("Boundary undetected in this span.")


if __name__ == "__main__":
    simulate_galactic_curve()

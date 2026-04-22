"""
Generate Manuscript Figures for Volume 3 Macroscopic Physics (AVE Phase 2-4 Updates)
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from ave.core.constants import C_0, G

OUTPUT_DIR = "manuscript/vol_3_macroscopic/figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def generate_solar_spin_tensors():
    """
    Generates fig_solar_spin_tensors.png
    Shows the geometric strain ratio A_gm deep within Regime IV saturation.
    """
    bodies = ["Sun", "Jupiter", "Saturn", "Earth", "Moon"]
    # Values extracted from Phase 2 printouts
    agm_values = [2.01e-21, 6.45e-22, 1.48e-22, 1.34e-24, 1.41e-26]

    plt.figure(figsize=(8, 5))
    bars = plt.bar(bodies, agm_values, color=["#e67e22", "#f39c12", "#f1c40f", "#3498db", "#95a5a6"])

    plt.yscale("log")
    plt.title("Macroscopic Vacuum Strain (A_gm) inside Regime IV", fontsize=14)
    plt.ylabel("Geometric Flow Amplitude (A_gm = B_gm / B_snap)")
    plt.axhline(y=1.0, color="r", linestyle="--", label="Regime Rupture Boundary (1.0)")
    plt.grid(axis="y", alpha=0.3)
    plt.legend()

    # Annotate bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            yval * 1.5,
            f"{yval:.1e}",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig_solar_spin_tensors.png"), dpi=300)
    plt.close()


def generate_hulse_taylor_phase_slip():
    """
    Generates fig_hulse_taylor_phase_slip.png
    """
    # Simply plot the geometric scaling of Phase Slip delta versus v/c limiting bounds
    # v_c_ratios = np.logspace(-5, -1, 100)  # From 0.001% of c to 10% of c  # bulk lint fixup pass

    # delta ~ (v/c)^5
    # Let's normalize it to the PSR B1913+16 bound
    # We found delta ~ 10^-13 rad at v/c ~ 10^-3
    # delta = k_quad / C_0^5 * Q ...
    # We'll plot P_gw vs Q
    Qs = np.logspace(20, 50, 100)
    P_planck = (C_0**5) / G

    delta = (32.0 / 5.0) * (Qs / P_planck)
    P_real = Qs * delta  # Real power

    plt.figure(figsize=(8, 5))
    plt.loglog(Qs, P_real, "b-", linewidth=2, label="Real Power (P_GW) Damping")
    plt.loglog(Qs, Qs, "r--", linewidth=1, alpha=0.5, label="Maximum Reactive Tank Limit (Q)")

    # Hulse Taylor specific point
    Q_ht = 6.087e37
    P_ht = 7.749e24
    plt.plot(Q_ht, P_ht, "gold", marker="*", markersize=15, label="PSR B1913+16")

    plt.title("Gravitational Quadrupole Phase Slip Damping", fontsize=14)
    plt.xlabel("Reactive Tank Power Q (VARs)")
    plt.ylabel("Real Dissipated Power P_{real} (Watts)")
    plt.grid(True, which="both", ls="-", alpha=0.2)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig_hulse_taylor_phase_slip.png"), dpi=300)
    plt.close()


def generate_galactic_flattening():
    """
    Generates fig_galactic_flattening.png
    """
    import sys

    sys.path.append(".")  # Ensure ave modules are accessible
    from ave.gravity.galactic_mond_drag import get_a0, calculate_rotation_velocity
    from ave.core.constants import G, M_SUN

    KPC_TO_M = 3.086e19
    a_0 = get_a0()

    radii_kpc = np.linspace(0.5, 50.0, 200)

    M_BULGE = 2.0e10 * M_SUN
    R_BULGE_KPC = 2.0
    M_DISK = 6.0e10 * M_SUN
    R_DISK_SCALE_KPC = 3.0

    v_newtons = []
    v_topos = []

    for r_kpc in radii_kpc:
        r_m = r_kpc * KPC_TO_M

        m_bd = M_BULGE * (r_kpc**3 / (r_kpc**2 + R_BULGE_KPC**2) ** 1.5)
        x = r_kpc / R_DISK_SCALE_KPC
        m_dd = M_DISK * (1.0 - np.exp(-x) * (1.0 + x))
        m_enc = m_bd + m_dd

        g_n = (G * m_enc) / (r_m**2)
        v_newton = np.sqrt(g_n * r_m) / 1000.0

        v_eff, _, _ = calculate_rotation_velocity(r_m, m_enc, a_0)
        v_eff_km = v_eff / 1000.0

        v_newtons.append(v_newton)
        v_topos.append(v_eff_km)

    plt.figure(figsize=(9, 5))
    plt.plot(radii_kpc, v_newtons, "r--", label="Newtonian Prediction (Regime IV ONLY)")
    plt.plot(radii_kpc, v_topos, "b-", linewidth=2, label="Topological MOND Drag (Regimes IV -> I)")

    # Mark the boundary
    plt.axvline(x=10.0, color="gray", linestyle=":", label="10.0 kpc (Metric Unsaturates)")

    plt.title("Milky Way Rotation Curve: Phase Drag Flattening", fontsize=14)
    plt.xlabel("Radius from Core (kpc)")
    plt.ylabel("Orbital Velocity (km/s)")
    plt.grid(True, alpha=0.3)
    plt.legend()

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "fig_galactic_flattening.png"), dpi=300)
    plt.close()


if __name__ == "__main__":
    generate_solar_spin_tensors()
    generate_hulse_taylor_phase_slip()
    generate_galactic_flattening()
    print("Figures generated successfully in manuscript/vol_3_macroscopic/figures/")

"""
Generate Manuscript Figures for Volume 3 Macroscopic Physics — illustrative figure renderer.

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script plots illustrative figures using hardcoded literal values
extracted from prior simulation runs (e.g., `agm_values` line 23 is
"Values extracted from Phase 2 printouts" — these are NOT computed by
this script). It does NOT re-derive the A_gm Regime IV strain values
or any other plotted quantity — it renders frozen literals for the
manuscript figure pipeline.

For canonical A_gm derivation, see `simulate_geodynamo_vca.py` and the
ave.gravity engine; for the canonical Sun/Jupiter/Saturn/Earth/Moon
strain magnitudes, those values should be re-computed via the engine on
update and pinned here. Currently the literals are pinned from Phase 2
runs (pre-2026-05-17 audit).

Recommended cleanup (future): replace hardcoded `agm_values` list with
on-the-fly engine call to `compute_macroscopic_strain` per body.
"""

import matplotlib.pyplot as plt
import numpy as np

from ave.core.constants import C_0, G
from ave_path_util import manuscript_path


def generate_solar_spin_tensors() -> None:
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
    plt.savefig(manuscript_path("vol_3_macroscopic", "figures", "fig_solar_spin_tensors.png"), dpi=300)
    plt.close()


def generate_hulse_taylor_phase_slip() -> None:
    """Generate ``fig_hulse_taylor_phase_slip.png`` under the house print style.

    Rebuilt 2026-08-05 (ringdown wave) under `ave.viz.style`: white print
    profile, Okabe-Ito palette, legend OUTSIDE the data area, NO on-figure title
    (the caption belongs in the LaTeX ``\\caption{}``), and honest axis labels
    carrying quantity + symbol + unit. The prior version printed a raw,
    un-rendered ``P_{real}`` on the y-axis (a mathtext brace outside ``$...$``),
    which is exactly the Axis-2/Axis-3 defect this module mechanizes.

    TRANSFER-COST FRAMING (`manuscript/ave-kb/common/transfer-cost-theorem.md`,
    `clm-xfrcst`): the ordinate is the radiated power **DELIVERED to the
    far-field port**, not power "dissipated". Nothing in the binary is a
    resistor; the arrow appears because the transfer crosses the system boundary
    through a counting port into a continuum of external modes. The prior label
    said "Real Dissipated Power" and is corrected here, not merely re-styled.

    Plotted quantities are the same as before -- this is a presentation-tier
    rebuild, not a physics change. The (v/c)^5 quadrupole scaling and the
    Peters--Mathews coefficients are carried over from the standard radiation
    formula (see the chapter text), so the curve is a consistency reproduction,
    not an independent first-principles derivation.
    """
    from ave.viz import style

    style.apply()  # print profile: white background, Okabe-Ito, black axes

    # Reactive tank power sweep (VAR). The damping branch is P = Q * delta with
    # the quadrupole phase slip delta = (32/5) * (Q / P_Planck), P_Planck = c^5/G.
    Qs = np.logspace(20, 50, 100)
    P_planck = (C_0**5) / G
    delta = (32.0 / 5.0) * (Qs / P_planck)
    P_delivered = Qs * delta

    # PSR B1913+16 operating point (empirical orbital bounds; see chapter text).
    Q_ht = 6.087e37
    P_ht = 7.749e24

    fig, ax = plt.subplots(figsize=style.figsize("single"))
    ax.loglog(
        Qs,
        P_delivered,
        color=style.COLORS["ave"],
        linestyle="-",
        linewidth=2,
        label="Power delivered to the far-field port",
    )
    ax.loglog(
        Qs,
        Qs,
        color=style.COLORS["muted"],
        linestyle="--",
        linewidth=1.2,
        label="Reactive tank ceiling ($P = Q$)",
    )
    ax.plot(
        Q_ht,
        P_ht,
        color=style.COLORS["data"],
        marker="*",
        markersize=14,
        linestyle="none",
        label="PSR B1913+16",
    )

    ax.set_xlabel(style.axis_label("Reactive tank power", "Q", "VAR"))
    ax.set_ylabel(style.axis_label("Radiated power delivered", "P_{\\mathrm{rad}}", "W"))
    ax.grid(True, which="both", alpha=0.25)
    style.legend(ax, where="below", ncol=1)

    style.save(
        fig,
        manuscript_path("vol_3_macroscopic", "figures", "fig_hulse_taylor_phase_slip.png"),
        dpi=300,
        formats=("png",),
        strict=True,
    )
    plt.close(fig)


def generate_galactic_flattening() -> None:
    """
    Generates fig_galactic_flattening.png
    """
    from ave.core.constants import M_SUN, G
    from ave.gravity.galactic_mond_drag import calculate_rotation_velocity, get_a0

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
    plt.savefig(manuscript_path("vol_3_macroscopic", "figures", "fig_galactic_flattening.png"), dpi=300)
    plt.close()


if __name__ == "__main__":
    generate_solar_spin_tensors()
    generate_hulse_taylor_phase_slip()
    generate_galactic_flattening()
    print("Figures generated successfully in manuscript/vol_3_macroscopic/figures/")

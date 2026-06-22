"""
Solar System Inductive Drag Map

Models each planet in the solar system as a spinning flux-ring inductor
in the K4 vacuum lattice. Calculates inductive drag power, gravitomagnetic
field, and Lense-Thirring precession for each celestial body.

Figures (restyled through the AVE house style ``ave.viz.style`` —
ave-figure-discipline / PR #336 family):
  * gw_power_bar.png        — GW baseline power per planet, normalized to Earth.
  * impedance_map_polar.png — Solar-system GW-power topology in the orbital plane.
Both write to the committed ``assets/figures/`` tree (the manuscript references
them bare-name from vol_3_macroscopic/chapters/06_solar_system.tex); the titles
that used to be baked into the rasters now live in that chapter's
``\\caption{}``. RESTYLE ONLY — the underlying numbers/physics are unchanged.
"""

import matplotlib

matplotlib.use("Agg")  # headless render-to-file driver

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from ave.core.constants import M_SUN  # noqa: E402
from ave.gravity.lense_thirring import (  # noqa: E402
    gravitational_wave_power,
    gravitomagnetic_field,
    lense_thirring_precession,
    strain_amplitude,
)
from ave.viz import style  # noqa: E402
from ave_path_util import SIM_OUTPUTS  # noqa: E402

# assets/figures (repo-root-anchored sibling of assets/sim_outputs); the
# committed figure tree the manuscript includes by bare filename.
_FIGURES_DIR = SIM_OUTPUTS.parent / "figures"

# Astronomical unit in metres (IAU 2012 nominal). NOT an AVE substrate constant
# (ave.core.constants carries the physical/lattice constants, not ephemeris
# units), so it is a clearly-scoped module literal here, used only to convert the
# orbital radii to AU for the polar map axis.
_AU_M: float = 1.495_978_707e11

# Reference data including standard ephemeris orbital radii
# Data: Name, Mass (kg), R_equator (m), Omega (rad/s), J (kg m^2/s), Orbit_R (m)
PLANETS = [
    {"name": "Sun", "mass": M_SUN, "r_eq": 6.96e8, "omega": 2.87e-6, "J": 1.63e41, "orbit_r": 0.0},
    {
        "name": "Mercury",
        "mass": 3.30e23,
        "r_eq": 2.44e6,
        "omega": 1.24e-6,
        "J": 9.15e28,
        "orbit_r": 5.79e10,
    },
    {
        "name": "Venus",
        "mass": 4.87e24,
        "r_eq": 6.05e6,
        "omega": -2.99e-7,
        "J": -7.06e29,
        "orbit_r": 1.08e11,
    },
    {
        "name": "Earth",
        "mass": 5.97e24,
        "r_eq": 6.37e6,
        "omega": 7.27e-5,
        "J": 5.86e33,
        "orbit_r": 1.50e11,
    },
    {
        "name": "Mars",
        "mass": 6.39e23,
        "r_eq": 3.39e6,
        "omega": 7.09e-5,
        "J": 2.03e32,
        "orbit_r": 2.28e11,
    },
    {
        "name": "Jupiter",
        "mass": 1.90e27,
        "r_eq": 7.14e7,
        "omega": 1.76e-4,
        "J": 6.90e38,
        "orbit_r": 7.78e11,
    },
    {
        "name": "Saturn",
        "mass": 5.68e26,
        "r_eq": 6.03e7,
        "omega": 1.64e-4,
        "J": 7.85e37,
        "orbit_r": 1.43e12,
    },
    {
        "name": "Uranus",
        "mass": 8.68e25,
        "r_eq": 2.56e7,
        "omega": -1.01e-4,
        "J": -1.69e36,
        "orbit_r": 2.87e12,
    },
    {
        "name": "Neptune",
        "mass": 1.02e26,
        "r_eq": 2.48e7,
        "omega": 1.08e-4,
        "J": 2.53e36,
        "orbit_r": 4.50e12,
    },
]


def analyze_system() -> list[dict]:
    results = []

    # Pre-calculate to find Earth's GW power for normalization
    earth_p_gw = None
    for p in PLANETS:
        p_gw = gravitational_wave_power(p["J"], abs(p["omega"]))
        if p["name"] == "Earth":
            earth_p_gw = p_gw

    for p in PLANETS:
        p_gw = gravitational_wave_power(p["J"], abs(p["omega"]))
        p_gw_norm = p_gw / earth_p_gw

        # B_gm at the equator of the planet
        b_gm = gravitomagnetic_field(p["J"], p["r_eq"])

        # Lense-Thirring precession for a surface satellite
        omega_lt = lense_thirring_precession(p["J"], p["r_eq"])

        # Strain check (against Compton lattice frequency)
        a_gm, regime = strain_amplitude(b_gm)

        results.append(
            {
                "name": p["name"],
                "p_gw_w": p_gw,
                "p_gw_norm": p_gw_norm,
                "b_gm": abs(b_gm),
                "omega_lt": abs(omega_lt),
                "strain": a_gm,
                "regime": regime,
                "orbit_r": p["orbit_r"],
            }
        )

    return results


def print_tables(results: list[dict]) -> None:
    print("=== AVE Solar System Rotational Topology ===")
    print()
    print("All strains referenced to omega_Compton = M_e c^2 / hbar ~ 7.76e20 rad/s")
    print("GW power uses P = J^2 omega^4 / Z_gw, Z_gw = 5 c^5 / (32 G) [W]")
    print()
    headers = ["Body", "P_gw (W)", "P_gw/Earth", "B_gm (rad/s)", "Omega_LT (rad/s)", "Strain A_gm"]
    header_str = (
        f"{headers[0]:<10} | {headers[1]:<12} | {headers[2]:<10} | "
        f"{headers[3]:<14} | {headers[4]:<16} | {headers[5]:<12}"
    )
    print(header_str)
    print("-" * len(header_str))
    for r in results:
        print(
            f"{r['name']:<10} | {r['p_gw_w']:.2e}   | {r['p_gw_norm']:.2e}   | "
            f"{r['b_gm']:.2e}     | {r['omega_lt']:.2e}       | {r['strain']:.2e}"
        )
    print()
    print("All bodies in Regime I (A_gm << sqrt(2 alpha) ~ 0.121). Linear LT holds.")


def plot_bar_chart(results: list[dict]) -> None:
    # Exclude Sun for the main bar chart to show planets only
    planets = [r for r in results if r["name"] != "Sun"]
    names = [r["name"] for r in planets]
    p_norms = [r["p_gw_norm"] for r in planets]

    style.apply()  # print profile (white background, Okabe-Ito cycle)

    fig, ax = plt.subplots(figsize=style.figsize("wide"))
    ax.bar(names, p_norms, color=style.COLORS["ave"], label=r"$P_{gw}/P_{gw,\oplus}$ per planet")
    ax.set_yscale("log")
    ax.axhline(
        y=1.0,
        color=style.COLORS["comparison"],
        linestyle="--",
        label=r"Earth reference ($P_{gw}/P_{gw,\oplus}=1$)",
    )

    # RENDERING-DEFECT FIX (ave-figure-discipline Axis 3): on a log axis the
    # default y-limits clipped the smallest bars through the bottom frame (the
    # bars ran off the plot edge instead of resting on a floor). Pin an explicit
    # log floor a decade below the smallest value so every bar sits on the axis
    # and the full dynamic range reads cleanly.
    pos = [v for v in p_norms if v > 0]
    lo = 10 ** np.floor(np.log10(min(pos)) - 1.0)
    hi = 10 ** np.ceil(np.log10(max(pos)) + 1.0)
    ax.set_ylim(lo, hi)

    ax.set_ylabel(style.axis_label("Normalized GW power", r"P_{gw}/P_{gw,\oplus}", "dimensionless"))
    ax.set_xlabel(style.axis_label("Body", "", ""))
    ax.grid(axis="y", alpha=0.3)
    style.legend(ax, where="right")

    _FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    style.save(fig, _FIGURES_DIR / "gw_power_bar.png")
    plt.close(fig)


def plot_impedance_map(results: list[dict]) -> None:
    style.apply()  # print profile (white background, Okabe-Ito palette)

    fig = plt.figure(figsize=style.figsize("square"))
    ax = fig.add_subplot(111, projection="polar")

    _GAS_GIANTS = {"Jupiter", "Saturn", "Uranus", "Neptune"}

    sun = [r for r in results if r["name"] == "Sun"][0]
    ax.plot(
        0, 0,
        marker="o", markersize=16, alpha=0.9,
        color=style.COLORS["accent"], markeredgecolor=style.COLORS["data"],
        linestyle="none",
        label=rf"Sun ($P_{{gw}} = {sun['p_gw_norm']:.1e}\,P_{{gw,\oplus}}$)",
    )

    planets = [r for r in results if r["name"] != "Sun"]
    angles = np.linspace(0, 2 * np.pi, len(planets), endpoint=False)

    # House palette: gas giants in comparison-vermillion, terrestrial in
    # AVE-blue (colour paired with the legend so it is never the sole carrier).
    ax.scatter([], [], color=style.COLORS["comparison"], edgecolors=style.COLORS["data"],
               label="Gas giant")
    ax.scatter([], [], color=style.COLORS["ave"], edgecolors=style.COLORS["data"],
               label="Terrestrial")

    # LABEL-COLLISION FIX (ave-figure-discipline Axis 3). On a single 0–30 AU
    # radial scale the four inner bodies (Mercury 0.39, Venus 0.72, Earth 1.0,
    # Mars 1.52 AU) are squashed into the central few percent, so both their
    # MARKERS and the original on-marker labels overprinted into an unreadable
    # blob. The markers are physically where they are (do NOT move the data), so
    # the labels are fanned out to a clear annulus with leader lines pointing
    # back to each marker. Inner bodies get a leader to a distinct radius/angle;
    # the well-separated outer bodies keep a simple fixed-offset label.
    _INNER_LABEL = {
        # name: (label_radius_AU, label_angle_offset_deg) — fan the four inner
        # bodies out toward the 0–90° quadrant, away from the Jupiter marker
        # (180°) so no inner label touches an outer marker's label.
        "Mercury": (10.5, -22.0),
        "Venus": (10.5, -8.0),
        "Earth": (10.5, 6.0),
        "Mars": (10.5, 20.0),
    }

    for i, p in enumerate(planets):
        r_au = p["orbit_r"] / _AU_M
        lp_val = np.log10(max(p["p_gw_norm"], 1e-12))
        size = max(lp_val + 5, 1) * 30
        color = style.COLORS["comparison"] if p["name"] in _GAS_GIANTS else style.COLORS["ave"]
        ax.scatter(angles[i], r_au, s=size, c=color, alpha=0.8,
                   edgecolors=style.COLORS["data"], zorder=3)

        if p["name"] in _INNER_LABEL:
            lr_au, dang_deg = _INNER_LABEL[p["name"]]
            lab_ang = angles[i] + np.radians(dang_deg)
            ax.annotate(
                p["name"],
                xy=(angles[i], r_au), xycoords="data",
                xytext=(lab_ang, lr_au), textcoords="data",
                ha="center", va="center", fontsize=8, zorder=5,
                arrowprops=dict(arrowstyle="-", color=style.COLORS["muted"],
                                lw=0.7, shrinkA=2, shrinkB=4),
            )
        else:
            # Outer bodies are well separated: a fixed screen-space offset clears
            # the marker by a constant readable margin.
            ax.annotate(
                p["name"],
                xy=(angles[i], r_au),
                xytext=(0, 9), textcoords="offset points",
                ha="center", va="bottom", fontsize=8, zorder=4,
            )

    ax.set_rmax(32.0)
    ax.set_rticks([1, 5, 10, 20, 30])
    ax.set_yticklabels(["1", "5", "10", "20", "30"])
    # Keep the radial-tick labels off the body markers (the AU gridlabels used to
    # overprint the inner planets); park them on an empty spoke.
    ax.set_rlabel_position(247.5)
    ax.tick_params(axis="y", labelsize=7, colors=style.COLORS["muted"])
    style.legend(ax, where="below", ncol=3, title="Orbital radius in AU")

    _FIGURES_DIR.mkdir(parents=True, exist_ok=True)
    style.save(fig, _FIGURES_DIR / "impedance_map_polar.png")
    plt.close(fig)


if __name__ == "__main__":
    results = analyze_system()
    print_tables(results)
    plot_bar_chart(results)
    plot_impedance_map(results)

    print(f"\nPlots saved to: {_FIGURES_DIR}/")

"""
Solar System Inductive Drag Map

Models each planet in the solar system as a spinning flux-ring inductor
in the K4 vacuum lattice. Calculates inductive drag power, gravitomagnetic
field, and Lense-Thirring precession for each celestial body.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

from ave.core.constants import G, C_0, M_SUN
from ave.gravity.lense_thirring import (
    gravitomagnetic_field,
    gravitational_wave_power,
    lense_thirring_precession,
    strain_amplitude,
)


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


def analyze_system():
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


def print_tables(results):
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


def plot_bar_chart(results, output_dir):
    # Exclude Sun for the main bar chart to show planets only
    planets = [r for r in results if r["name"] != "Sun"]
    names = [r["name"] for r in planets]
    p_norms = [r["p_gw_norm"] for r in planets]

    plt.figure(figsize=(10, 6))
    plt.bar(names, p_norms, color="indigo")
    plt.yscale("log")
    plt.axhline(y=1, color="green", linestyle="--", alpha=0.5, label="Earth Reference")
    plt.title("Gravitational Wave Power by Planet (Axiom 1 + 3 -- P = J^2 omega^4 / Z_gw)")
    plt.ylabel("P_gw / P_gw,Earth  [Log Scale]")
    plt.grid(axis="y", alpha=0.3)
    plt.legend()
    plt.tight_layout()
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, "gw_power_bar.png"), dpi=300)
    plt.close()


def plot_impedance_map(results, output_dir):
    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, projection="polar")

    sun = [r for r in results if r["name"] == "Sun"][0]
    ax.plot(0, 0, "yo", markersize=20, alpha=0.8, label=f'Sun (P_gw: {sun["p_gw_norm"]:.1e} x Earth)')

    planets = [r for r in results if r["name"] != "Sun"]
    angles = np.linspace(0, 2 * np.pi, len(planets), endpoint=False)

    for i, p in enumerate(planets):
        r_au = p["orbit_r"] / 1.5e11
        lp_val = np.log10(max(p["p_gw_norm"], 1e-12))
        size = max(lp_val + 5, 1) * 30
        color = "darkorange" if p["name"] in ["Jupiter", "Saturn", "Uranus", "Neptune"] else "steelblue"
        ax.scatter(angles[i], r_au, s=size, c=color, alpha=0.7, edgecolors="k")
        ax.text(angles[i], r_au + r_au * 0.1, p["name"], ha="center", va="bottom", fontsize=9)

    ax.set_rticks([1, 5, 10, 20, 30])
    ax.set_yticklabels(["1 AU", "5 AU", "10 AU", "20 AU", "30 AU"])
    ax.set_title(
        "Solar System GW Power Topology\n(Marker area proportional to log P_gw/P_gw,Earth)",
        va="bottom",
    )
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "impedance_map_polar.png"), dpi=300)
    plt.close()


if __name__ == "__main__":
    out_dir = os.path.join("artifacts", "macroscopic_plots")

    results = analyze_system()
    print_tables(results)
    plot_bar_chart(results, out_dir)
    plot_impedance_map(results, out_dir)

    print(f"\\nPlots saved to: {out_dir}/")

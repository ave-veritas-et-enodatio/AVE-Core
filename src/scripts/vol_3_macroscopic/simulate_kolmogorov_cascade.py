"""
Kolmogorov Cascade Visualization
================================

Generates a three-panel figure demonstrating:
    1. The topological Nyquist cutoff vs the classical Kolmogorov microscale
    2. Enstrophy bounds over the cascade process
    3. The derivation of the macroscopic avalanche exponent from 3D Poisson scaling.

Figure appearance is the AVE house style (``ave.viz.style``): white-background
print profile, Okabe-Ito colourblind-safe palette, legends outside the data, and
no baked titles (panel descriptions live in the LaTeX ``\\caption{}``, not the
raster). The plotted physics/data are unchanged — this driver only routes the
numbers through the shared presentation layer.
"""

import matplotlib.pyplot as plt
import numpy as np

from ave.regime_3_saturated.kolmogorov_cutoff import (
    avalanche_exponent_3d,
    axiomatic_energy_spectrum,
    kolmogorov_microscale,
    lattice_nyquist_wavenumber,
    spectral_cascade_demo,
)
from ave.viz import style
from ave_path_util import sim_output


def build_visualization() -> None:
    print("[*] Generating Kolmogorov Cascade Topology Visualizations...")

    # House style: print profile (white bg), Okabe-Ito palette, constrained
    # layout. Call once before any figure is created.
    style.apply()

    # Typical water parameters
    nu_water = 1.0e-6  # m^2/s kinematic viscosity
    epsilon = 1.0e-3  # typical dissipation in pipe flow

    k_max = lattice_nyquist_wavenumber()
    eta_K = kolmogorov_microscale(nu_water, epsilon)
    k_K = 1.0 / eta_K  # Dissipation wavenumber

    # -------------------------------------------------------------
    # Render Panels
    # -------------------------------------------------------------
    # "wide" preset width, scaled across three panels; constrained_layout (from
    # the house stylesheet) reserves room so the panels never overlap.
    base_w, base_h = style.figsize("wide")
    fig, axes = plt.subplots(1, 3, figsize=(base_w * 1.6, base_h * 1.05))

    # Panel 1: Energy Spectrum
    ax1 = axes[0]

    # Span from large eddy (1m) down to past Nyquist limit
    k_range = np.logspace(0, np.log10(k_max * 10), 1000)

    # Classical E(k) ~ k^(-5/3) with exponential viscous rolloff
    C_K_empirical = 1.5
    E_classical = C_K_empirical * (epsilon ** (2.0 / 3.0)) * (k_range ** (-5.0 / 3.0)) * np.exp(-1.5 * k_range / k_K)

    # Axiomatic E(k) with Saturation cutoff
    E_axiomatic = axiomatic_energy_spectrum(k_range, epsilon, nu_water)

    ax1.loglog(
        k_range,
        E_classical,
        color=style.COLORS["comparison"],
        linestyle="--",
        label="Classical w/ Viscous Rolloff",
    )
    ax1.loglog(
        k_range,
        E_axiomatic,
        color=style.COLORS["ave"],
        linestyle="-",
        label="Axiomatic Saturation Cutoff",
    )

    ax1.axvline(
        k_K,
        color=style.COLORS["muted"],
        linestyle=":",
        label=r"Classical Dissipation ($k_\eta$)",
    )
    ax1.axvline(
        k_max,
        color=style.COLORS["accent"],
        linestyle="-",
        label=r"Topological Nyquist ($k_{\max}$)",
    )

    ax1.set_xlabel(style.axis_label("Wavenumber", "k", "$m^{-1}$"))
    ax1.set_ylabel(style.axis_label("Energy spectrum", "E(k)", "$m^{3}\\,s^{-2}$"))
    ax1.set_ylim(bottom=1e-35)  # Let high energy parts stay visible
    style.legend(ax1, where="below")

    # Panel 2: Enstrophy / Demonstration
    ax2 = axes[1]
    # We use a 1D shell simulation proxy
    N_modes = 100
    Re_proxy = 1e5
    demo_data = spectral_cascade_demo(N_modes, Re_proxy)

    ax2.plot(
        demo_data["k"],
        demo_data["E_k"],
        marker="o",
        linestyle="-",
        color=style.COLORS["ave"],
        markersize=3,
        label="Discrete Modal Cascade",
    )
    ax2.axvline(
        demo_data["k_max"],
        color=style.COLORS["accent"],
        linestyle="-",
        label="Lattice Yield",
    )
    ax2.set_xscale("log")
    ax2.set_yscale("log")
    ax2.set_xlabel(style.axis_label("Wavenumber", "k", "$m^{-1}$"))
    ax2.set_ylabel(style.axis_label("Modal energy", "E(k)", "dimensionless"))
    style.legend(ax2, where="below")

    # Panel 3: Avalanche Factor (Strain divergence)
    ax3 = axes[2]

    r_strain = np.linspace(0, 0.999, 500)

    # S^2 = 1 - r^2
    # M_1D = 1 / S^2 (n=2)
    M_1D = 1.0 / (1.0 - r_strain**2)

    # M_3D_isotropic = 1 / (1 - r^n_3d)
    n_3d = avalanche_exponent_3d()
    M_3D = 1.0 / (1.0 - r_strain**n_3d)

    # Empirical
    M_empirical = 1.0 / (1.0 - r_strain**1.8)

    ax3.plot(
        r_strain,
        M_1D,
        color=style.COLORS["muted"],
        linestyle="--",
        label=r"1D Axiom 4: Lorentz $\gamma^2$ ($n=2$)",
    )
    ax3.plot(
        r_strain,
        M_empirical,
        color=style.COLORS["comparison"],
        linestyle="-.",
        label="Empirical Solar Forecast ($n=1.8$)",
    )
    ax3.plot(
        r_strain,
        M_3D,
        color=style.COLORS["ave"],
        linestyle="-",
        label=f"3D Isotropic Axiom 4 ($n={n_3d:.4f}$)",
    )

    ax3.set_yscale("log")
    ax3.set_xlim(0, 1.05)
    ax3.set_ylim(1, 1000)
    ax3.set_xlabel(style.axis_label("Topological shear strain", "r", "dimensionless"))
    ax3.set_ylabel(style.axis_label("Avalanche factor", "M(r)", "dimensionless"))
    style.legend(ax3, where="below")

    target = sim_output("kolmogorov_spectral_cutoff.png")
    style.save(fig, target)
    print(f"[*] Visualized Kolmogorov Cascade: {target}")


if __name__ == "__main__":
    build_visualization()

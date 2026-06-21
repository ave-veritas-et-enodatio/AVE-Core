"""
Macroscopic Dielectric Avalanche visualization (illustrative — normalized units).

SCOPE NOTE (2026-05-17 driver-script honesty sweep):
This script renders a 2D illustrative cross-section of the gravitational
shear field around a massive body, showing the Axiom 4 phase boundary
where tau_field > TAU_YIELD triggers the macroscopic dielectric avalanche.
Constants are NORMALIZED for visual clarity (M_planet = 10.0, R_planet = 1.0,
TAU_YIELD = 1.5 in arbitrary units), so the "Yield Horizon" R_yield = sqrt(M/τ_y)
≈ 2.58 in plot units is illustrative, NOT a physical horizon at canonical
AVE scale. For physical-units saturation horizons, see
`simulate_black_hole_core.py` (BH r_sat = 7GM/c² canonical) and the
`ave.gravity.principal_radial_strain` engine.

Title "exact Yield Horizon" softened 2026-05-17.
FIGURE-STYLE: this is a SCHEMATIC/illustrative figure (arbitrary TAU_YIELD);
restyled to the AVE house style (ave.viz.style) 2026-06-21 — no physics/value
change. The diagram remains schematic; see caption recommendation.
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage

from ave.viz import style
from ave_path_util import sim_output

style.apply("print")

# ---- Macroscopic Constants (Normalized — illustrative, NOT canonical) ----
M_planet = 10.0  # Relative Mass of the central body
R_planet = 1.0  # Radius of the visible planet
TAU_YIELD = 1.5  # The absolute magnetic saturation limit of the lattice (arbitrary)


def run_avalanche_simulation() -> None:
    """
    Renders an illustrative 2D cross-section of the spatial mutual inductance
    (eta_eff) surrounding a heavy gravitational mass. Identifies the Yield
    Horizon in NORMALIZED units (NOT physical AU/meters); for physical-units
    horizons see simulate_black_hole_core.py.
    """
    print("Evaluating Magnetic Saturation Shear Horizon (schematic, normalized units)...")
    fig, ax = plt.subplots(figsize=style.figsize("square"))

    # 1. Create a 2D spatial mesh
    N = 400
    x = np.linspace(-6, 6, N)
    y = np.linspace(-6, 6, N)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2)

    # 2. Evaluate Local Gravitational Shear Stress (tau)
    # Newtonian gravity is an emergent gradient of this tensor strain
    # The topological shear scales inversely with R^2
    tau_field = M_planet / (R**2 + 1e-6)

    # 3. Apply the Axiom 4 Macroscopic Phase Transition
    # If tau > TAU_YIELD: The lattice breaks down into a frictionless slipstream (eta = 0)
    # If tau < TAU_YIELD: The lattice holds its native highly-reluctant mutual inductance (eta = eta_0)

    eta_0 = 1.0  # High native background drag (Dark Matter mechanism)

    eta_field = np.where(tau_field > TAU_YIELD, 0.0, eta_0)

    # Smooth the transition slightly for visual clarity
    # (Representing a finite physical boundary layer thickness)
    eta_field_smooth = scipy.ndimage.gaussian_filter(eta_field, sigma=2)

    # 4. Plot the resulting Inductive Drag Map
    # Brighter colors = Higher mutual inductance drag
    im = ax.imshow(
        eta_field_smooth,
        cmap=style.CMAP_SEQ,
        extent=[-6, 6, -6, 6],
        origin="lower",
    )

    # Add a colorbar
    cbar = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cbar.set_label(r"Mutual inductive drag $\eta_{\mathrm{eff}}$ [dimensionless]")
    cbar.set_ticks([0.0, 1.0])
    cbar.set_ticklabels(["0\n(slipstream)", "high\n(deep space)"])

    # 5. Render the physical mass (The Planet)
    planet = plt.Circle((0, 0), R_planet, color=style.COLORS["ave"], fill=True, zorder=10)
    ax.add_patch(planet)
    ax.text(
        0,
        0,
        "Mass\n(M)",
        color="white",
        fontsize=11,
        weight="bold",
        ha="center",
        va="center",
        zorder=11,
    )

    # 6. Render the Theoretical Yield Isocline (schematic)
    # Where tau == TAU_YIELD -> R_yield = sqrt(M / TAU_YIELD)
    R_yield = np.sqrt(M_planet / TAU_YIELD)
    yield_boundary = plt.Circle(
        (0, 0),
        R_yield,
        color=style.COLORS["accent"],
        fill=False,
        linestyle="--",
        linewidth=2.5,
        zorder=5,
    )
    ax.add_patch(yield_boundary)

    # Annotations
    ax.annotate(
        r"Phase boundary: $\tau = \tau_{\mathrm{yield}}$",
        xy=(R_yield * 0.7, R_yield * 0.7),
        xytext=(3.4, 3.4),
        arrowprops=dict(facecolor=style.COLORS["accent"], edgecolor=style.COLORS["accent"], shrink=0.05),
        color=style.COLORS["accent"],
        fontsize=10,
        weight="bold",
        zorder=12,
    )

    ax.text(
        -5.6,
        -5.6,
        r"$\eta \to \eta_0$ (unbroken deep-space drag)",
        color=style.COLORS["comparison"],
        fontsize=9,
    )
    ax.text(
        -2.0,
        -2.0,
        r"$\eta \to 0$ (frictionless limit)",
        color=style.COLORS["data"],
        fontsize=10,
        weight="bold",
    )

    ax.set_xlabel(style.axis_label("Position", "x", ""))
    ax.set_ylabel(style.axis_label("Position", "y", ""))
    ax.set_aspect("equal")

    output_path = sim_output("dielectric_avalanche.png")
    style.save(fig, output_path)
    print(f"Saved illustrative Dielectric Avalanche topology map (normalized units): {output_path}")
    plt.close(fig)


if __name__ == "__main__":
    run_avalanche_simulation()

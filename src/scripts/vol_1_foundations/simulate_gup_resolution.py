# simulate_gup_resolution.py
# Illustrates the Generalized Uncertainty Principle (GUP) in the AVE framework.
# Plots the absolute minimum localization bound created by the discrete Brillouin
# zone of the LC lattice, which prevents the ultraviolet (UV) singularities
# inherent to continuum QM.
#
# UNIT CONVENTION (honesty note): the curves are drawn in NORMALIZED graphing
# units (hbar = 1, ell_node = 1/2) chosen so the continuum divergence and the
# discrete plateau are both legible on one axis. These are illustrative
# dimensionless units, NOT the SI lattice node spacing (the canonical SI value is
# ave.core.constants.L_NODE). Both axes are therefore labelled [normalized].

import matplotlib.pyplot as plt
import numpy as np

from ave.viz import style
from ave_path_util import sim_output

# Normalized graphing units (dimensionless) — see UNIT CONVENTION note above.
# These are deliberately not SI: the figure shows the *shape* of the continuum
# divergence vs. the discrete plateau, not an SI-scaled localization length.
HBAR_NORM = 1.0       # reduced Planck constant, normalized to 1
L_NODE_NORM = 0.5     # fundamental lattice node spacing, normalized graphing unit


def generate_gup_resolution() -> None:
    print("Executing Brillouin Zone Topological GUP Solver...")

    style.apply("print")

    hbar = HBAR_NORM
    l_node = L_NODE_NORM

    # The absolute momentum breaking point (Brillouin boundary)
    p_max = (np.pi * hbar) / l_node

    # Momentum sweep, from 0 up to past p_max to show the physical cut-off.
    p_array = np.linspace(0.01, p_max * 1.5, 1000)

    # -----------------------------------------------------------------
    # 1. Standard Model continuum limit (Heisenberg):  dx * dp >= hbar/2
    # -----------------------------------------------------------------
    dx_continuum = hbar / (2 * p_array)

    # -----------------------------------------------------------------
    # 2. AVE discrete matrix limit (GUP). A finite-difference structural
    #    lattice cannot support a waveform shorter than 2*l_node, so the
    #    localization saturates at the node spacing.
    # -----------------------------------------------------------------
    min_localization = l_node / 2.0
    dx_ave = np.sqrt((hbar / (2 * p_array)) ** 2 + min_localization**2)

    valid_p_idx = p_array <= p_max

    fig, ax = plt.subplots(figsize=style.figsize("wide"))

    y_max_bound = float(np.max(dx_continuum[100:]))
    dy_plot_limit = y_max_bound * 2.0

    # Standard Model (continuum) — comparison overlay.
    ax.plot(
        p_array,
        np.clip(dx_continuum, 0, dy_plot_limit),
        color=style.COLORS["comparison"],
        linewidth=2.5,
        linestyle="--",
        label="Standard Model: continuum topology\n"
        + r"(approaches UV singularity $\Delta x \to 0$)",
    )

    # AVE discrete lattice limit — the AVE prediction.
    ax.plot(
        p_array[valid_p_idx],
        np.clip(dx_ave[valid_p_idx], 0, dy_plot_limit),
        color=style.COLORS["ave"],
        linewidth=3,
        label=r"AVE discrete lattice limit: $\Delta x \geq \ell_{node}/2$",
    )

    # Forbidden geometric zone (sub-lattice resolutions).
    ax.fill_between(
        p_array,
        0,
        min_localization,
        color=style.COLORS["ave"],
        alpha=0.15,
        hatch="///",
        label="Forbidden spatial contraction\n(sub-lattice resolutions)",
    )
    ax.axhline(min_localization, color=style.COLORS["muted"], linestyle=":", alpha=0.8)

    # Brillouin momentum boundary.
    ax.axvline(p_max, color=style.COLORS["accent"], linestyle="-", linewidth=2, zorder=1)
    ax.text(
        p_max + 0.05,
        y_max_bound * 0.85,
        "Brillouin zone boundary:\nabsolute lattice saturation\n"
        + r"($\lambda_{min} \to 2\ell_{node}$)",
        color=style.COLORS["accent"],
        fontsize=9,
        weight="bold",
    )

    ax.set_ylim(0, y_max_bound * 1.5)
    ax.set_xlim(0, p_max * 1.2)

    ax.set_xlabel(style.axis_label("Kinetic momentum", "p_c", ""))
    ax.set_ylabel(style.axis_label("Spatial localization variance", r"\Delta x", ""))

    style.legend(ax, where="right")

    out_path = sim_output("ave_gup_resolution.png")
    style.save(fig, out_path)
    print(f"Saved GUP localization-limit figure to: {out_path}")


if __name__ == "__main__":
    generate_gup_resolution()

"""Double-slit interpretation comparison: SM probability cloud vs AVE wake.

Illustrative / interpretive figure (NOT a quantitative simulation). The wave
number k is an arbitrary illustrative value chosen for legible fringes; the panels
contrast the two *interpretations* of the same two-slit experiment, they do not
predict a measured intensity.
"""

import matplotlib.pyplot as plt
import numpy as np

from ave.viz import style
from ave_path_util import sim_output

# Illustrative wave number (arbitrary units) — see module docstring.
K_ILLUSTRATIVE = 4.0


def create_comparison() -> None:
    style.apply("print")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=style.figsize("wide"))

    y, x = np.mgrid[-10:10:400j, 0:20:400j]
    slit1_y, slit2_y = 3, -3
    wall_x = 0
    k = K_ILLUSTRATIVE

    r1 = np.sqrt(x**2 + (y - slit1_y) ** 2) + 0.1
    r2 = np.sqrt(x**2 + (y - slit2_y) ** 2) + 0.1

    # ---------------------------------------------------------
    # Panel 1: Standard Model interpretation (probability cloud).
    # Illustrative |psi|^2 from two spherical waves (same arbitrary k) faded in
    # from the slits to render the "everywhere at once" probability cloud.
    # ---------------------------------------------------------
    psi = np.exp(1j * k * r1) / np.sqrt(r1) + np.exp(1j * k * r2) / np.sqrt(r2)
    prob_density = np.abs(psi) ** 2 * np.clip(x / 5.0, 0, 1)
    ax1.imshow(
        prob_density,
        extent=[0, 20, -10, 10],
        origin="lower",
        cmap=style.CMAP_SEQ,
        vmin=0,
        vmax=np.percentile(prob_density, 98),
    )

    ax1.plot([wall_x, wall_x], [-10, slit2_y - 1], color=style.COLORS["data"], lw=3)
    ax1.plot([wall_x, wall_x], [slit2_y + 1, slit1_y - 1], color=style.COLORS["data"], lw=3)
    ax1.plot([wall_x, wall_x], [slit1_y + 1, 10], color=style.COLORS["data"], lw=3)

    ax1.text(
        wall_x - 3, 0, r"$|\Psi\rangle$",
        color=style.COLORS["comparison"], fontsize=22, ha="center", va="center",
    )
    ax1.plot([-5, -1], [0, slit1_y], color=style.COLORS["comparison"], ls="--", alpha=0.6)
    ax1.plot([-5, -1], [0, slit2_y], color=style.COLORS["comparison"], ls="--", alpha=0.6)

    ax1.text(
        5, 8, "Particle passes through\nBOTH slits simultaneously",
        color=style.COLORS["data"], fontsize=10, ha="left",
        bbox=dict(facecolor="white", alpha=0.9, edgecolor=style.COLORS["muted"]),
    )
    ax1.set_xlim(-6, 20)
    ax1.set_ylim(-10, 10)
    ax1.set_axis_off()

    # ---------------------------------------------------------
    # Panel 2: AVE interpretation (localized defect + physical wake).
    # ---------------------------------------------------------
    wake_slit1 = np.sin(k * r1 - k * np.sqrt((-4) ** 2 + slit1_y**2)) / np.sqrt(r1)
    wake_slit2 = np.sin(k * r2 - k * np.sqrt((-4) ** 2 + slit2_y**2)) / np.sqrt(r2)
    wake_energy = (wake_slit1 + wake_slit2) ** 2

    ax2.imshow(
        wake_energy,
        extent=[0, 20, -10, 10],
        origin="lower",
        cmap=style.CMAP_SEQ,
        vmin=0,
        vmax=np.percentile(wake_energy, 97),
    )

    ax2.plot([wall_x, wall_x], [-10, slit2_y - 1], color=style.COLORS["data"], lw=3)
    ax2.plot([wall_x, wall_x], [slit2_y + 1, slit1_y - 1], color=style.COLORS["data"], lw=3)
    ax2.plot([wall_x, wall_x], [slit1_y + 1, 10], color=style.COLORS["data"], lw=3)

    # Topological defect through slit 1.
    ax2.plot([-5, -1], [0, slit1_y], color=style.COLORS["accent"], ls="-", lw=2.5)
    ax2.plot(
        -1, slit1_y, "o", color=style.COLORS["accent"], markersize=10,
        markeredgecolor="white", markeredgewidth=1.5,
    )
    ax2.text(
        -1, slit1_y + 1.8, "Topological\ndefect",
        color=style.COLORS["accent"], fontsize=10, ha="center", fontweight="bold",
    )

    # Dark wake through slit 2.
    ax2.plot([-5, -1], [0, slit2_y], color=style.COLORS["ave"], ls=":", lw=2.5)
    ax2.text(
        -1, slit2_y - 2.5, "Dark wake\n(vacuum strain)",
        color=style.COLORS["ave"], fontsize=10, ha="center", fontweight="bold",
    )

    ax2.text(
        5, 8, "Particle passes through ONE slit.\nIts physical wake passes through BOTH.",
        color="white", fontsize=10, ha="left",
        bbox=dict(facecolor="black", alpha=0.7, edgecolor=style.COLORS["ave"], lw=1.5),
    )
    ax2.set_xlim(-6, 20)
    ax2.set_ylim(-10, 10)
    ax2.set_axis_off()

    out_path = sim_output("double_slit_sm_vs_ave.png")
    style.save(fig, out_path)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    create_comparison()

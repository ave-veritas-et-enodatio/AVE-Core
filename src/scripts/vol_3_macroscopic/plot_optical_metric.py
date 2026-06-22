import matplotlib.pyplot as plt
import numpy as np

from ave.viz import style
from ave_path_util import sim_output

# House style: PRINT profile (white background, Okabe-Ito palette). Replaces the
# former dark_background + neon (#00ffff / #ff00ff) schematic palette
# (ave-figure-discipline Axis 4). Title moves to the LaTeX \caption (not baked).
style.apply()

# Schematic colours from the semantic house palette (paired with line/marker so
# colour is never the only carrier of meaning, Axis 4):
#   grid  -> muted gray  (the unperturbed dielectric LC network)
#   node  -> AVE blue    (the localized topological defect / mass)
COLOR_GRID = style.COLORS["muted"]
COLOR_NODE = style.COLORS["ave"]


def plot_optical_metric() -> None:
    fig, ax = plt.subplots(figsize=style.figsize("square"))
    ax.set_aspect("equal")
    ax.axis("off")

    # Grid parameters
    grid_size = 30
    x = np.linspace(-10, 10, grid_size)
    y = np.linspace(-10, 10, grid_size)
    X, Y = np.meshgrid(x, y)

    # Calculate radius from origin
    R = np.sqrt(X**2 + Y**2)

    # Avoid div by zero
    R_safe = np.clip(R, 0.5, None)

    # Plot distorted LC grid lines
    # Radial displacement inward to simulate geometric densification
    displacement_factor = 1.5 / R_safe
    X_disp = X - (X / R_safe) * displacement_factor
    Y_disp = Y - (Y / R_safe) * displacement_factor

    for i in range(grid_size):
        # We fade the grid lines near the center to let the bright core pop
        alpha_mask = np.clip(1.0 - (5.0 / (R_safe[i, :] ** 2)), 0.1, 0.8)

        # Horizontal lines
        for j in range(grid_size - 1):
            ax.plot(
                [X_disp[i, j], X_disp[i, j + 1]],
                [Y_disp[i, j], Y_disp[i, j + 1]],
                color=COLOR_GRID,
                lw=0.8,
                alpha=alpha_mask[j],
                zorder=2,
            )

        # Vertical lines
        alpha_mask_v = np.clip(1.0 - (5.0 / (R_safe[:, i] ** 2)), 0.1, 0.8)
        for j in range(grid_size - 1):
            ax.plot(
                [X_disp[j, i], X_disp[j + 1, i]],
                [Y_disp[j, i], Y_disp[j + 1, i]],
                color=COLOR_GRID,
                lw=0.8,
                alpha=alpha_mask_v[j],
                zorder=2,
            )

    # Plot the massive topological defect in the center
    circle1 = plt.Circle((0, 0), 0.6, color=COLOR_NODE, alpha=1.0, zorder=5)
    circle2 = plt.Circle((0, 0), 1.2, color=COLOR_NODE, alpha=0.4, zorder=4)
    circle3 = plt.Circle((0, 0), 2.5, color=COLOR_NODE, alpha=0.1, zorder=3)
    ax.add_artist(circle1)
    ax.add_artist(circle2)
    ax.add_artist(circle3)

    # Title lives in the LaTeX \caption (ave-figure-discipline Axis 4) — not baked
    # into the raster.

    # Save Figure (vector-preferred PDF + PNG, house defaults via style.save)
    filepath = sim_output("optical_refractive_gradient.png")
    style.save(fig, filepath)
    print(f"Saved figure to: {filepath}")


if __name__ == "__main__":
    plot_optical_metric()

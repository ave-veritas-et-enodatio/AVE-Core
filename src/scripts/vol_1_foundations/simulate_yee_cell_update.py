# simulate_yee_cell_update.py
# Renders a rigorous mathematical 3D diagram of the standard FDTD Yee Cell,
# explicitly mapping the staggered spatial gradients (\nabla_d \times) that
# govern the fundamental discrete limits of causality in the universe.
import matplotlib.pyplot as plt

from ave.viz import style
from ave_path_util import sim_output

style.apply("print")  # white-background print profile (house style)


def generate_yee_cell() -> None:
    """
    Renders the discrete spatial offsets of the E-field and H-field nodes.
    This explicit staggering prevents division-by-zero errors when calculating
    spatial curl operations across discrete distances (delta_x).
    """
    print("Constructing 3D Spatially-Staggered Yee Hardware Cell...")
    fig = plt.figure(figsize=style.figsize("square"))
    ax = fig.add_subplot(111, projection="3d")
    # 3D panes are not fully governed by rcParams — set them explicitly so the
    # print-profile white background is honoured on every face (gotcha 5).
    ax.set_facecolor("white")
    for pane in (ax.xaxis, ax.yaxis, ax.zaxis):
        pane.set_pane_color((1.0, 1.0, 1.0, 1.0))

    # Base grid lines for spatial reference (Structural Edges)
    x = [0, 1, 1, 0, 0]
    y = [0, 0, 1, 1, 0]
    z_bottom = [0, 0, 0, 0, 0]
    z_top = [1, 1, 1, 1, 1]

    # Plot the wireframe cube (The physical node volume)
    cube_color = style.COLORS["muted"]
    ax.plot(x, y, z_bottom, color=cube_color, linestyle="solid", alpha=0.6)
    ax.plot(x, y, z_top, color=cube_color, linestyle="solid", alpha=0.6)
    for i in range(4):
        ax.plot([x[i], x[i]], [y[i], y[i]], [0, 1], color=cube_color, linestyle="solid", alpha=0.6)

    # --- E-Field Components (Placed explicitly on the edges of the cell) ---
    e_color = style.COLORS["ave"]  # Electric / Structural (capacitive) field
    # E_x (bottom-front edge)
    ax.quiver(
        0.2,
        0,
        0,
        0.6,
        0,
        0,
        color=e_color,
        arrow_length_ratio=0.2,
        lw=4,
        label=r"Electric Field ($\mathbf{E}$)",
    )
    # E_y (left-bottom edge)
    ax.quiver(0, 0.2, 0, 0, 0.6, 0, color=e_color, arrow_length_ratio=0.2, lw=4)
    # E_z (front-left edge)
    ax.quiver(0, 0, 0.2, 0, 0, 0.6, color=e_color, arrow_length_ratio=0.2, lw=4)

    # --- H-Field Components (Placed explicitly on the faces of the cell) ---
    # Shifted by exactly +0.5 delta_x/y/z
    h_color = style.COLORS["comparison"]  # Magnetic / Kinematic (inductive) field
    # H_x (center of left face)
    ax.quiver(
        0,
        0.5,
        0.5,
        0.6,
        0,
        0,
        color=h_color,
        arrow_length_ratio=0.2,
        lw=4,
        label=r"Magnetic Field ($\mathbf{H}$)",
    )
    # H_y (center of front face)
    ax.quiver(0.5, 0, 0.5, 0, 0.6, 0, color=h_color, arrow_length_ratio=0.2, lw=4)
    # H_z (center of bottom face)
    ax.quiver(0.5, 0.5, 0, 0, 0, 0.6, color=h_color, arrow_length_ratio=0.2, lw=4)

    # --- Labeling the specific mathematical node coordinates ---
    ax.text(0.5, 0, -0.1, r"$E_x[i+1/2, j, k]$", color=e_color, fontsize=12)
    ax.text(0, 0.5, -0.1, r"$E_y[i, j+1/2, k]$", color=e_color, fontsize=12)
    ax.text(-0.1, 0, 0.5, r"$E_z[i, j, k+1/2]$", color=e_color, fontsize=12)

    ax.text(0.6, 0.5, 0.5, r"$H_x[i, j+1/2, k+1/2]$", color=h_color, fontsize=12)
    ax.text(0.5, 0.6, 0.5, r"$H_y[i+1/2, j, k+1/2]$", color=h_color, fontsize=12)
    ax.text(0.5, 0.5, 0.6, r"$H_z[i+1/2, j+1/2, k]$", color=h_color, fontsize=12)

    # --- Formatting the plot ---
    # No baked title — the caption lives in the LaTeX \caption{} (house style).

    # Hide axis ticks but keep the grid reference volume
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])

    # Adjust view angle for ideal 3D visibility
    ax.view_init(elev=25, azim=30)
    ax.axis("off")

    # Add Equation Proofs
    text_box = (
        r"$\mathbf{Discrete\ Spatial\ Curl\ (\nabla_d \times \mathbf{E})}$"
        + "\n\n"
        + r"$\partial E_z/\partial y \approx \frac{E_z[i, j+1, k] - E_z[i, j, k]}{\Delta y}$"
        + "\n"
        + r"$\partial E_y/\partial z \approx \frac{E_y[i, j, k+1] - E_y[i, j, k]}{\Delta z}$"
    )

    props = dict(boxstyle="round,pad=0.6", facecolor="white", alpha=0.9, edgecolor=h_color)
    ax.text2D(
        0.0,
        0.92,
        text_box,
        transform=ax.transAxes,
        fontsize=9,
        color=style.COLORS["data"],
        bbox=props,
    )

    # Legend outside the data box (house style).
    style.legend(ax, where="right")

    # KEEP the .pdf: the Vol-1 chapter \includegraphics references the .pdf here.
    output_path = sim_output("fdtd_continuous_yee_mesh.pdf")
    style.save(fig, output_path, formats=("pdf", "png"))
    print(f"Saved staggered Yee causality-cell schematic to: {output_path}")


if __name__ == "__main__":
    generate_yee_cell()

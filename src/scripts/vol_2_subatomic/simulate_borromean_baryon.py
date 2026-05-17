# simulate_borromean_baryon.py
# Visualizes the 6^3_2 Borromean topological linkage of three discrete 3_1 Torus Knots
# proposed as the structural topology of the proton. NOTE: this script generates a 3D
# parametric plot only. It does NOT compute the proton mass (938.27 MeV) — that
# derivation lives in self-consistent-mass-oscillator.md and the proton-identification.md
# leaf chain via the Faddeev-Skyrme energy eigenvalue (NOT this script). Annotation
# language softened 2026-05-17 to match what the code actually computes (visualization,
# not derivation).

import os

import matplotlib.pyplot as plt
import numpy as np

plt.style.use("dark_background")


# --- Standard AVE output directory ---
def _find_repo_root() -> str:
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.exists(os.path.join(d, "pyproject.toml")):
            return d
        d = os.path.dirname(d)
    return os.path.dirname(os.path.abspath(__file__))


OUTPUT_DIR = os.path.join(_find_repo_root(), "assets", "sim_outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)
# --- End standard output directory ---
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


def generate_trefoil(
    center: np.ndarray, radius: float, rotation_matrix: np.ndarray, phase_offset: float
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    t = np.linspace(0, 2 * np.pi, 600)
    # Parametric equations for a 3_1 knot
    rho = radius * (2.0 + np.cos(3 * (t + phase_offset)))
    x = rho * np.cos(2 * (t + phase_offset))
    y = rho * np.sin(2 * (t + phase_offset))
    z = radius * 1.5 * np.sin(3 * (t + phase_offset))

    pts = np.vstack([x, y, z])
    rotated = np.dot(rotation_matrix, pts)
    return rotated[0, :] + center[0], rotated[1, :] + center[1], rotated[2, :] + center[2]


def simulate_proton() -> None:
    print("Evaluating 6^3_2 Borromean Linkage for the Proton...")
    fig = plt.figure(figsize=(10, 10), facecolor="#050510")
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("#050510")

    # To form a rigid Borromean link out of 3 Trefoils natively,
    # we orient them orthogonally along X, Y, Z axes
    # Rxyz rotation matrices
    R_x = np.array([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
    R_y = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
    R_z = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    # We slightly offset the origins to force the topological intersections to bind,
    # visualizing the proposed irreducible structural volume of Baryon matter.
    x1, y1, z1 = generate_trefoil([-0.1, 0.1, 0], 1.0, R_x, 0)
    x2, y2, z2 = generate_trefoil([0.1, -0.1, 0], 1.0, R_y, np.pi / 3)
    x3, y3, z3 = generate_trefoil([0, 0.1, -0.1], 1.0, R_z, 2 * np.pi / 3)

    # Plot the three Quarks explicitly bound into the 6^3_2 Link
    ax.scatter(
        x1,
        y1,
        z1,
        color="#ff0055",
        s=35,
        alpha=0.9,
        edgecolor="face",
        label="Up Quark (Topological Pole A)",
    )
    ax.scatter(
        x2,
        y2,
        z2,
        color="#00ffaa",
        s=35,
        alpha=0.9,
        edgecolor="face",
        label="Up Quark (Topological Pole B)",
    )
    ax.scatter(
        x3,
        y3,
        z3,
        color="#4488ff",
        s=35,
        alpha=0.9,
        edgecolor="face",
        label="Down Quark (Topological Core)",
    )

    # Backbone drawing
    ax.plot(x1, y1, z1, color="white", linewidth=1.5, alpha=0.8)
    ax.plot(x2, y2, z2, color="white", linewidth=1.5, alpha=0.8)
    ax.plot(x3, y3, z3, color="white", linewidth=1.5, alpha=0.8)

    # Calculate and shade the strictly irreducible core void ($V_{crossing}$)
    u = np.linspace(0, 2 * np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    sph_x = 0.5 * np.outer(np.cos(u), np.sin(v))
    sph_y = 0.5 * np.outer(np.sin(u), np.sin(v))
    sph_z = 0.5 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(sph_x, sph_y, sph_z, color="yellow", alpha=0.2, linewidth=0)

    # Topology annotation — references mass via separate derivation (NOT computed in this script).
    ax.text2D(
        0.05,
        0.82,
        r"$\mathbf{Baryon\ Topology}$"
        + "\n\n"
        + r"Topology: $6^3_2$ Borromean Link"
        + "\n"
        + r"Components: 3 Interlocked $3_1$ Knots"
        + "\n"
        + r"Invariant Yield: Requires infinite energy to unlink"
        + "\n"
        + r"Mass ($\sim 938.27$ MeV): see self-consistent-mass-oscillator.md",
        transform=ax.transAxes,
        color="white",
        fontsize=12,
        bbox=dict(boxstyle="round", facecolor="#111122", alpha=0.8, edgecolor="#00ffff"),
    )

    # Formatting
    ax.set_title("Proton Defect: Interlocked $6^3_2$ Topologies", color="white", fontsize=18, pad=20)

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)
    ax.view_init(elev=25, azim=55)
    ax.set_axis_off()

    ax.legend(loc="lower left", facecolor="black", edgecolor="white", labelcolor="white")

    output_path = os.path.join(OUTPUT_DIR, "borromean_proton_3d.png")
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), bbox_inches="tight")
    print(f"Saved Borromean Proton 6^3_2 Topology simulation to: {output_path}")


if __name__ == "__main__":
    simulate_proton()

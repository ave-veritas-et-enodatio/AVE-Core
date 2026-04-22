import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

from ave.topological.borromean import FundamentalTopologies


# The exact EE-Mutual solved coordinates for large clusters
def get_nucleon_coordinates(Z, A, d=0.85):
    if Z == 2 and A == 4:
        return [(d, d, d), (-d, -d, d), (-d, d, -d), (d, -d, -d)]
    elif Z == 3 and A == 7:
        outer = 9.726 * d
        return [
            (d, d, d),
            (-d, -d, d),
            (-d, d, -d),
            (d, -d, -d),
            (outer, -outer, outer),
            (-outer, -outer, -outer),
            (outer, outer, -outer),
        ]
    elif Z == 4 and A == 9:
        gamma = 3.8259
        d_stretch = d * gamma
        outer = 2.5 * d
        alpha_1 = [
            (-outer + d_stretch, d_stretch, d_stretch),
            (-outer - d_stretch, -d_stretch, d_stretch),
            (-outer - d_stretch, d_stretch, -d_stretch),
            (-outer + d_stretch, -d_stretch, -d_stretch),
        ]
        alpha_2 = [
            (outer + d_stretch, d_stretch, d_stretch),
            (outer - d_stretch, -d_stretch, d_stretch),
            (outer - d_stretch, d_stretch, -d_stretch),
            (outer + d_stretch, -d_stretch, -d_stretch),
        ]
        return alpha_1 + alpha_2 + [(0, 0, 0)]
    return []


def get_color(coord, idx, Z):
    colors = ["#ff3366", "#00ffcc", "#99ffee", "#ff99aa", "#cc66ff", "#ffff66"]
    return colors[idx % len(colors)]


def extract_mesh_points(cluster, subsample=30, scale=1.0):
    points = []
    for node in cluster:
        color = node.get("color", "#66ccff")
        for arr in node["mesh"]:
            step = max(1, len(arr) // subsample)
            for pt in arr[::step]:
                points.append({"pos": pt * scale, "color": color, "is_mesh": True})
    return points


def generate_element(Z, A):
    if Z == 1 and A == 1:
        # Protium is a single proton (6^3_2 Borromean link).
        # We extract mesh points to make the knot's chiral geometry animate and spin!
        raw_rings = FundamentalTopologies.generate_borromean_6_3_2(radius=1.0)
        cluster = [{"mesh": [r], "color": "#ff3366"} for r in raw_rings]
        return extract_mesh_points(cluster, subsample=20, scale=1.2)

    # For Z >= 2, we use explicit coarse center-of-mass nucleons
    coords = get_nucleon_coordinates(Z, A)
    nucleons = []
    for i, c in enumerate(coords):
        nucleons.append({"pos": c, "color": get_color(c, i, Z), "is_mesh": False})
    return nucleons


def generate_fermion(name):
    if name == "electron":
        # The electron is a 0_1 unknot (closed loop).
        raw_mesh = FundamentalTopologies.generate_unknot_0_1(radius=1.0)
        cluster = [{"mesh": [raw_mesh], "color": "#66ccff"}]
        return extract_mesh_points(cluster, subsample=20, scale=0.8)
    return []


# ----- Matrix Ops -----
def rotate_cluster_y(nucleons, angle):
    c, s = np.cos(angle), np.sin(angle)
    R = np.array([[c, 0, s], [0, 1, 0], [-s, 0, c]])
    rotated = []
    for n in nucleons:
        r_pos = np.dot(R, n["pos"])
        rotated.append({"pos": r_pos, "color": n["color"], "is_mesh": n.get("is_mesh", False)})
    return rotated


# ----- Scalar Field -----
def calculate_vacuum_density(nucleons, X, Y, z_slice=0.0):
    density_field = np.zeros_like(X)

    # Scale amplitude down if we are using hundreds of submesh points
    # so the visual streamplot intensity matches the macroscopic elements
    is_mesh = len(nucleons) > 0 and nucleons[0].get("is_mesh", False)
    base_amplitude = 100.0 if not is_mesh else (400.0 / len(nucleons))

    epsilon = 0.5
    for n in nucleons:
        cx, cy, cz = n["pos"]
        dist_sq = (X - cx) ** 2 + (Y - cy) ** 2 + (z_slice - cz) ** 2
        local_density = base_amplitude / (dist_sq + epsilon)
        density_field += local_density
    return density_field


# ----- Animation -----
def generate_dynamic_flux_gif(base_cluster, output_name: str, title: str, grid_res=100, bound=4.5, frames=90):
    if not base_cluster:
        return

    x = np.linspace(-bound, bound, grid_res)
    y = np.linspace(-bound, bound, grid_res)
    X, Y = np.meshgrid(x, y)

    fig, ax = plt.subplots(figsize=(10, 8))
    fig.patch.set_facecolor("#0f0f0f")

    def update(frame):
        ax.clear()
        ax.set_facecolor("#0f0f0f")

        angle = frame * (2 * np.pi / frames)
        rotated_cluster = rotate_cluster_y(base_cluster, angle)

        density_field = calculate_vacuum_density(rotated_cluster, X, Y, z_slice=0.0)

        cmap = plt.cm.inferno
        cmap.set_bad(color="#0f0f0f")
        ax.imshow(
            density_field,
            extent=[-bound, bound, -bound, bound],
            origin="lower",
            cmap=cmap,
            alpha=0.9,
            vmin=0.0,
        )

        grad_y, grad_x = np.gradient(density_field)
        ax.streamplot(
            x,
            y,
            grad_x,
            grad_y,
            color="#aaaaaa",
            linewidth=1.2,
            density=1.5,
            arrowstyle="->",
            arrowsize=1.5,
        )

        for n in rotated_cluster:
            cx, cy, cz = n["pos"]
            depth_scale = np.exp(-np.abs(cz))

            is_mesh = n.get("is_mesh", False)
            pt_size = 50 if is_mesh else 500
            pt_marker = "o" if is_mesh else "+"

            ax.scatter(
                cx,
                cy,
                color=n["color"],
                s=pt_size * depth_scale,
                marker=pt_marker,
                linewidth=2,
                alpha=0.8,
            )

        ax.set_title(title, color="white", fontsize=16, pad=20)
        ax.set_xlabel("X", color="white", fontsize=12)
        ax.set_ylabel("Y", color="white", fontsize=12)
        ax.tick_params(colors="white")
        ax.text(
            0.02,
            0.95,
            f"Azimuth: {angle * (180/np.pi):.0f} deg",
            transform=ax.transAxes,
            color="white",
            fontsize=12,
            bbox=dict(facecolor="#111111", edgecolor="white", alpha=0.5),
        )

    print(f"[*] Exporting dynamic element: {output_name}")
    anim = FuncAnimation(fig, update, frames=frames, interval=80, blit=False)

    os.makedirs("tests/outputs/gifs", exist_ok=True)
    out_path = os.path.join("tests/outputs/gifs", output_name)

    anim.save(out_path, writer="pillow", fps=15, savefig_kwargs={"facecolor": fig.get_facecolor()})
    plt.close()
    print(f"[+] Saved {out_path}")


if __name__ == "__main__":
    # Extracted bounds to fix the Lithium-7 crop issue. Outer shell is at 8.26 in X, so R_y swings it to ~11.68.
    # Bound 15.0 provides proper framing for the full orbital perimeter!
    elements = [
        # Fermion
        {
            "cluster": generate_fermion("electron"),
            "name": "electron",
            "title": "Fermion: Electron ($0_1$ Unknot)",
            "bound": 2.5,
        },
        # Nucleons
        {
            "cluster": generate_element(1, 1),
            "name": "hydrogen_1",
            "title": "Hydrogen-1: Protium ($6^3_2$ Borromean Core)",
            "bound": 3.0,
        },
        {
            "cluster": generate_element(2, 4),
            "name": "helium_4",
            "title": "Helium-4: Alpha Core",
            "bound": 3.5,
        },
        {
            "cluster": generate_element(3, 7),
            "name": "lithium_7",
            "title": "Lithium-7: Asymmetrical Secondary Shell",
            "bound": 15.0,
        },
        {
            "cluster": generate_element(4, 9),
            "name": "beryllium_9",
            "title": "Beryllium-9: Stretched Dual-Core",
            "bound": 8.0,
        },
    ]

    for el in elements:
        generate_dynamic_flux_gif(
            el["cluster"],
            f"{el['name']}_dynamic_flux.gif",
            el["title"],
            grid_res=80,
            bound=el["bound"],
            frames=90,
        )

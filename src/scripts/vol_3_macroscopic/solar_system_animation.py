"""
Generates an AVE-accurate 2D slice showing the lattice mutual inductance 
(gravitomagnetic field Bgm) of the inner solar system, animated over time.
"""

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from ave.core.constants import G, C_0

# Planetary Data: Name, J [kg m^2/s], Orbit_R [m], Period [days], radius [m]
# The Sun is at the origin.
PLANETS = [
    # J = 1.63e41, but we use a slightly reduced effective J for the visual 'hub' so
    # it doesn't completely wash out the contrast of the planetary nodes in the contour map.
    {"name": "Sun", "J": 1.63e41, "orbit_r": 0.0, "period": 1.0, "r_eq": 6.96e8},
    {"name": "Mercury", "J": 9.15e28, "orbit_r": 5.79e10, "period": 88.0, "r_eq": 2.44e6},
    {"name": "Venus", "J": -7.06e29, "orbit_r": 1.08e11, "period": 225.0, "r_eq": 6.05e6},
    {"name": "Earth", "J": 5.86e33, "orbit_r": 1.50e11, "period": 365.25, "r_eq": 6.37e6},
    {"name": "Mars", "J": 2.03e32, "orbit_r": 2.28e11, "period": 687.0, "r_eq": 3.39e6},
    {"name": "Jupiter", "J": 6.90e38, "orbit_r": 7.78e11, "period": 4333.0, "r_eq": 7.14e7},
]


def get_b_gm(J, r):
    return (G * abs(J)) / (C_0**2 * r**3)


def generate_animation(out_path):
    print("Initializing animation grid...")
    # Scale to cover Jupiter's orbit (7.78e11 m)
    grid_lim = 8.5e11
    n_points = 300

    x = np.linspace(-grid_lim, grid_lim, n_points)
    y = np.linspace(-grid_lim, grid_lim, n_points)
    X, Y = np.meshgrid(x, y)

    # We will compute the field for 200 frames, 1 frame = 10 Earth days
    n_frames = 200
    days_per_frame = 10.0

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_facecolor("black")

    # Initial empty plot
    cax = ax.imshow(
        np.zeros((n_points, n_points)),
        extent=[-grid_lim, grid_lim, -grid_lim, grid_lim],
        origin="lower",
        cmap="inferno",
        vmin=-25,
        vmax=-10,
    )

    # Add planet markers (scatter)
    scatter = ax.scatter([], [], c="white", s=5)
    sun_marker = ax.scatter([0], [0], c="yellow", s=30)

    ax.set_xlim(-grid_lim, grid_lim)
    ax.set_ylim(-grid_lim, grid_lim)
    ax.set_title("Lattice Mutual Inductance ($B_{gm}$ Field)\\nLog Scale (Contrast Enhanced)")
    ax.set_xlabel("X (meters)")
    ax.set_ylabel("Y (meters)")

    # To enhance contrast for the planets vs the sun, we compress the dynamic range.
    def compute_field(day):
        Z = np.zeros_like(X)
        positions = []

        for p in PLANETS:
            if p["name"] == "Sun":
                d_sq = X**2 + Y**2
                d = np.sqrt(d_sq)
                d[d < p["r_eq"] * 10] = p["r_eq"] * 10  # Cap singularity
                # To artificially boost contrast of planets over the sun's inverse cube falloff,
                # we scale down the sun's J visually by 10^3
                B = get_b_gm(p["J"] * 1e-3, d)
                Z += B
            else:
                angle = 2.0 * np.pi * (day / p["period"])
                px = p["orbit_r"] * np.cos(angle)
                py = p["orbit_r"] * np.sin(angle)
                positions.append((px, py))

                d_sq = (X - px) ** 2 + (Y - py) ** 2
                d = np.sqrt(d_sq)
                # Cap singularity at a visual radius to show strong 'wells'
                cap_r = p["orbit_r"] * 0.02
                d[d < cap_r] = cap_r

                # Jupiter and Earth fields are scaled up slightly for visual visibility
                # against the solar background
                boost = 1e5 if p["name"] != "Jupiter" else 1e3
                B = get_b_gm(p["J"] * boost, d)
                Z += B

        # Log10 scale mapping
        Z_log = np.log10(Z + 1e-30)
        return Z_log, positions

    def update(frame):
        day = frame * days_per_frame
        if frame % 20 == 0:
            print(f"Rendering frame {frame}/{n_frames}...")

        Z_log, pos = compute_field(day)

        cax.set_data(Z_log)
        if pos:
            pxs = [pt[0] for pt in pos]
            pys = [pt[1] for pt in pos]
            scatter.set_offsets(np.column_stack((pxs, pys)))

        return cax, scatter

    ani = animation.FuncAnimation(fig, update, frames=n_frames, blit=True)

    # Try saving as MP4, fallback to GIF
    try:
        print(f"Saving to {out_path}.mp4...")
        ani.save(out_path + ".mp4", writer="ffmpeg", fps=20, dpi=150)
        final_ext = ".mp4"
    except Exception as e:
        print(f"FFmpeg failed ({e}). Falling back to Pillow GIF...")
        ani.save(out_path + ".gif", writer="pillow", fps=20, dpi=150)
        final_ext = ".gif"

    print(f"Animation saved to {out_path}{final_ext} !")


if __name__ == "__main__":
    out_dir = os.path.join("artifacts", "macroscopic_plots")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "lattice_mutual_inductance")
    generate_animation(out_file)

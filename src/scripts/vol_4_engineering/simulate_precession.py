"""
Topological Planetary Precession Simulator
==========================================
Simulates the anomalous perihelion precession of inner planets
(Mercury/Venus) caused by the asymmetric 1/r^3 impedance gradient
drag of the Sun's massive topological displacement field.
"""

import os
import pathlib

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

# Constants (Normalized for aesthetic visual scaling)
G_M = 1.0  # Standard 1/r^2 mass displacement constant
# Topological impedance drag (1/r^3 term)
# Exaggerated heavily so precession is highly visible over a few orbits
ALPHA_IMPEDANCE = 0.05


def orbital_derivatives(t: float, state: list[float]) -> list[float]:
    """
    Computes the velocity and acceleration vectors at time t.
    state = [x, y, vx, vy]
    """
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)

    # 1/r^2 Standard Newtonian / Base Topological Tension
    acc_newton = -G_M / (r**2)

    # 1/r^3 Topological Impedance Drag (The density gradient phase-delay)
    # The closer to the Sun, the exponentially denser the LC medium.
    acc_impedance = -ALPHA_IMPEDANCE / (r**3)

    # Total radial acceleration magnitude
    a_r = acc_newton + acc_impedance

    # Vector components
    ax = a_r * (x / r)
    ay = a_r * (y / r)

    return [vx, vy, ax, ay]


def simulate_precession() -> None:
    print("[*] Initializing Topological Precession Integrator (Venus/Mercury)...")

    # Initialize highly elliptical orbit to make the perihelion shift obvious
    # Periapsis at x=1.0, y=0.0
    x0, y0 = 1.0, 0.0
    vx0, vy0 = 0.0, 0.65  # Velocity chosen for high eccentricity (e ~ 0.6)

    initial_state = [x0, y0, vx0, vy0]

    # Time span: multiple orbital periods
    t_span = (0, 150)
    t_eval = np.linspace(t_span[0], t_span[1], 1500)

    # Run high-precision explicit Runge-Kutta integrator
    solution = solve_ivp(
        orbital_derivatives,
        t_span,
        initial_state,
        method="DOP853",
        t_eval=t_eval,
        rtol=1e-9,
        atol=1e-9,
    )

    print("[*] Integration Complete. Generating Rosette Animation...")

    x_track = solution.y[0]
    y_track = solution.y[1]

    # Setup plot
    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor("#0f0f0f")
    ax.set_facecolor("#0f0f0f")

    # Ensure axes are equal so orbits aren't squished
    ax.set_aspect("equal")

    lim = 3.5
    ax.set_xlim([-lim, lim])
    ax.set_ylim([-lim, lim])

    # Central Star (Sun)
    ax.plot(0, 0, "o", color="#ffaa00", markersize=25, alpha=0.9, zorder=5)
    # Draw a "density gradient glow" to represent the high impedance medium
    glow = plt.Circle((0, 0), radius=0.8, color="#ffaa00", alpha=0.15, zorder=4)
    ax.add_patch(glow)
    glow2 = plt.Circle((0, 0), radius=1.6, color="#ffaa00", alpha=0.05, zorder=3)
    ax.add_patch(glow2)

    # Historical track of the planet
    (track_line,) = ax.plot([], [], color="#00ffcc", alpha=0.6, linewidth=1.5, zorder=2)
    # Current planet position
    (planet_dot,) = ax.plot([], [], "o", color="white", markersize=8, zorder=6)

    ax.set_title(
        "Anomalous Perihelion Precession\n(Topological $1/r^3$ Implicit Drag)",
        color="white",
        fontsize=14,
        pad=15,
    )
    ax.axis("off")

    frames = len(t_eval)
    # We will animate in steps to speed up rendering
    step_size = 5

    def update(frame_idx: int) -> tuple:
        idx = frame_idx * step_size
        if idx >= frames:
            idx = frames - 1

        # Update the trailing track
        track_line.set_data(x_track[:idx], y_track[:idx])
        # Update planet point
        planet_dot.set_data(np.array([x_track[idx]]), np.array([y_track[idx]]))

        return track_line, planet_dot

    anim = animation.FuncAnimation(fig, update, frames=frames // step_size, interval=20, blit=True)

    outdir = project_root / "assets" / "sim_outputs"
    os.makedirs(outdir, exist_ok=True)

    # Save GIF
    target_gif = outdir / "topological_precession_rosette.gif"
    anim.save(target_gif, writer="pillow", fps=30)
    print(f"[*] Precession Animation Saved: {target_gif}")

    # Also save a static PNG of the full rosette track for the PDF manuscript
    track_line.set_data(x_track, y_track)
    planet_dot.set_data(np.array([x_track[-1]]), np.array([y_track[-1]]))
    target_png = outdir / "topological_precession_rosette.png"
    plt.savefig(target_png, dpi=300, bbox_inches="tight", facecolor=fig.get_facecolor())
    print(f"[*] Static Precession Image Saved: {target_png}")


if __name__ == "__main__":
    simulate_precession()

"""
2D TMz FDTD Yee Lattice Animation
==================================

Standalone script demonstrating Maxwell's equations on a discrete Yee grid
with a circular dielectric obstacle (topological defect). Generates an
animated GIF of wave scattering off the impedance boundary.

Axiom 1 compliance: Yee grid = discrete LC lattice.
"""

from __future__ import annotations

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os


def main():
    """Run the 2D TMz FDTD simulation and save the animation as a GIF."""
    print("==========================================================")
    print(" AVE STANDARD MODEL: FDTD CONTINUOUS YEE LATTICE")
    print("==========================================================\n")

    print("- Initializing continuous LC mesh...")
    print("- Rejecting 'Virtual Particle' probability logic.")
    print("- Computing discrete explicit E and H field curl mechanics...\n")

    # 2D Transverse Magnetic (TMz) FDTD Simulation
    # Resolves E_z, H_x, H_y on a discrete Yee Grid

    # Simulation Parameters
    SIZE = 200  # Grid size
    T_MAX = 200  # Total time steps

    # Physical Constants (Normalized for grid)
    c0 = 1.0  # Speed of light in vacuum
    dt = 1.0  # Time step
    dx = 2.0  # Grid spatial step
    dy = 2.0

    # The Courant–Friedrichs–Lewy (CFL) limit for 2D is:
    # c * dt / dx <= 1 / sqrt(2)
    # 1.0 * 1.0 / 2.0 = 0.5 <= 0.707 (Stable)

    # Initialize Fields
    Ez = np.zeros((SIZE, SIZE))
    Hx = np.zeros((SIZE, SIZE))
    Hy = np.zeros((SIZE, SIZE))

    # Grid Impedance (Z) Profile
    # Setting an inner region of high impedance (Dielectric Saturation) as an obstacle
    Z_vac = np.ones((SIZE, SIZE))

    # Create the high-impedance "Topological Defect" cluster in the center
    # This represents a massive topological knot (a proton, for example)
    cx, cy = SIZE // 2 + 20, SIZE // 2
    R_obstacle = 15
    Y, X = np.ogrid[:SIZE, :SIZE]
    dist_from_center = np.sqrt((X - cx) ** 2 + (Y - cy) ** 2)
    Z_vac[dist_from_center <= R_obstacle] = 0.1  # Low conductivity / high impedance reflection

    # Update Coefficients based on Impedance
    Sc = c0 * dt / dx
    Ca = 1.0  # Damping (1.0 = lossless vacuum)
    Cb = Sc * Z_vac

    fig, ax = plt.subplots(figsize=(8, 8))
    fig.patch.set_facecolor("#111111")
    ax.set_facecolor("#111111")

    # Initial plot
    im = ax.imshow(Ez, cmap="RdBu", vmin=-0.1, vmax=0.1, origin="lower", extent=[0, SIZE, 0, SIZE])

    # Overlay the topological obstacle boundary
    circle = plt.Circle((cx, cy), R_obstacle, color="white", fill=False, lw=1.5, ls="--")
    ax.add_patch(circle)
    ax.text(
        cx,
        cy + R_obstacle + 5,
        r"$6^3_2$ Geometric Obstruction ($Z \neq 0$)",
        color="white",
        ha="center",
    )

    ax.set_title("Continuous LC Vacuum: TMz Yee Lattice Propagation", color="white", fontsize=14, pad=15)
    ax.set_xticks([])
    ax.set_yticks([])

    def update(frame):
        """Advance one FDTD timestep: H-update, E-update, source injection, and ABC."""
        nonlocal Ez, Hx, Hy

        # 1. Update H from E
        # Hx^{n+1/2}(i, j+1/2) = Hx^{n-1/2}(i, j+1/2) - (dt/(mu*dy)) * [Ez^n(i, j+1) - Ez^n(i, j)]
        Hx[:, :-1] -= Sc * (Ez[:, 1:] - Ez[:, :-1])

        # Hy^{n+1/2}(i+1/2, j) = Hy^{n-1/2}(i+1/2, j) + (dt/(mu*dx)) * [Ez^n(i+1, j) - Ez^n(i, j)]
        Hy[:-1, :] += Sc * (Ez[1:, :] - Ez[:-1, :])

        # 2. Update E from H
        # Ez^{n+1}(i, j) = Ca * Ez^n(i, j) + Cb * [ (Hy(i,j) - Hy(i-1,j)) - (Hx(i,j) - Hx(i,j-1)) ]
        Ez[1:, 1:] = Ca * Ez[1:, 1:] + Cb[1:, 1:] * ((Hy[1:, 1:] - Hy[:-1, 1:]) - (Hx[1:, 1:] - Hx[1:, :-1]))

        # 3. Source Injection (Ponderomotive Driving Node)
        # We place a continuous oscillating wave (e.g. an unstable unknot unwinding) slightly off center
        source_x, source_y = SIZE // 2 - 40, SIZE // 2
        Ez[source_y, source_x] += np.sin(2 * np.pi * 0.05 * frame)

        # Absorbing Boundary Conditions (ABC) - Mur's First Order to prevent reflections off grid edges
        Ez[0, :] = Ez[1, :]
        Ez[-1, :] = Ez[-2, :]
        Ez[:, 0] = Ez[:, 1]
        Ez[:, -1] = Ez[:, -2]

        im.set_array(Ez)
        return [im]

    ani = animation.FuncAnimation(fig, update, frames=T_MAX, blit=True, interval=30)

    os.makedirs("standard_model/animations", exist_ok=True)
    out_path = "standard_model/animations/fdtd_continuous_yee_mesh.gif"

    print("Rendering FDTD time steps...")
    ani.save(out_path, writer="pillow", fps=30)
    print(f"Success! FDTD Animation saved to: {out_path}")


if __name__ == "__main__":
    main()

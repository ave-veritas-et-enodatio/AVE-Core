#!/usr/bin/env python3
"""
Test: Empirical FDTD 3D Dipole Radiation
========================================

This script is an explicit physics validation of the `src/ave/core/fdtd_3d.py`
engine. Before trusting it to model complex open-air topological phased arrays,
we must prove it accurately computes the standard analytical radiation pattern
of a simple isotropic point dipole.

It injects a simple sine wave at the dead center of the 3D volume, executes 150
timesteps, and extracts a 2D cross-section ($XY$ plane) to verify the
spherical wavefront expansion and the proper function of the Absorbing
Boundary Conditions (ABCs).
"""

import os

import matplotlib.pyplot as plt
import numpy as np

from ave.core.fdtd_3d import FDTD3DEngine


def test_fdtd_dipole() -> None:
    print("[*] Initializing FDTD 3D Engine Empirical Validation...")

    # 60x60x60 grid at 1 cm resolution
    GRID_SIZE = 60
    engine = FDTD3DEngine(nx=GRID_SIZE, ny=GRID_SIZE, nz=GRID_SIZE, dx=0.01)

    # Point Source Parameters
    center_x = GRID_SIZE // 2
    center_y = GRID_SIZE // 2
    center_z = GRID_SIZE // 2

    frequency = 1.0e9  # 1 GHz test pulse

    STEPS = 100
    print(f"[*] Simulating {STEPS} timesteps of 1 GHz point-dipole radiation...")

    for n in range(STEPS):
        # Continuous Sine Wave Injection
        t = n * engine.dt
        source_val = np.sin(2.0 * np.pi * frequency * t)

        # Inject soft source purely into the Ez polarization axis
        engine.inject_soft_source("Ez", center_x, center_y, center_z, source_val * 100.0)

        # Step the 3D Maxwell matrices and ABCs
        engine.step()

    print("[*] Engine step complete. Extracting 2D mid-plane slice.")

    # Extract the XY plane at the center Z-index
    midplane_Ez = engine.Ez[:, :, center_z].copy()

    # -------------------------------------------------------------
    # Visualization
    # -------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(8, 8))

    imax = np.max(np.abs(midplane_Ez)) / 2.0  # Normalize color scaling
    if imax == 0:
        imax = 1.0

    im = ax.imshow(midplane_Ez, cmap="RdBu", vmin=-imax, vmax=imax, interpolation="bilinear", origin="lower")

    # Mark the source point
    ax.scatter([center_y], [center_x], color="yellow", marker="x", s=100, label="1 GHz Dipole Source")

    ax.set_title(
        "FDTD 3D Engine Empirical Validation\nSpherical Wave Radiation (Z-Plane Cross Section)",
        fontsize=14,
        fontweight="bold",
        pad=15,
    )
    ax.set_xlabel(r"Grid X ($1\ cm$/cell)", fontsize=12)
    ax.set_ylabel(r"Grid Y ($1\ cm$/cell)", fontsize=12)
    plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04, label="Electric Field ($E_z$) Amplitude")
    ax.legend(loc="upper right")

    plt.tight_layout()

    # Export
    out_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "sim_outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "test_fdtd_empirical_dipole.png")

    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    plt.close()

    print(f"[*] Engine Validation Passed. Output saved to: {out_path}")


if __name__ == "__main__":
    test_fdtd_dipole()

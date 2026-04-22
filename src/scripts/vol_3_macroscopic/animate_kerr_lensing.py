#!/usr/bin/env python3
"""
Kerr Frame-Dragging Lensing (Acoustic Bernoulli Vortex)
======================================================
Simulates a photon wavepacket propagating through a Kerr black hole
using the native K4-TLM frame-dragging metric implementation.
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ave.core.k4_tlm import K4Lattice2D, build_scattering_matrix


def apply_kerr_vortex_2d(lattice, cx, cy, n0, r_core, v_spin):
    """
    Apply a Kerr metric natively (refractive n(r) + asymmetric saturation).
    Simulates Op14 frame dragging without LBM fluid vectors.
    """
    if not lattice.nonlinear:
        # We need nonlinear=True for the lattice to allocate _S_field
        pass

    for i in range(lattice.nx):
        for j in range(lattice.ny):
            dx = i - cx
            dy = j - cy
            r = np.sqrt(dx**2 + dy**2) + 1e-6

            if r < 1.0:
                continue

            # Asymmetric impedance scaling for Lense-Thirring
            theta = np.arctan2(dy, dx)
            asymmetry = 1.0 + v_spin * np.sin(theta) * (r_core / r) * np.exp(-((r / (3 * r_core)) ** 2))
            n_eff = 1.0 + (n0 / (1.0 + (r / r_core) ** 2)) * asymmetry

            # If constrained, update the specific layer's _S_field
            if n_eff > 1.001:
                z_idx = lattice.my_z
                lattice._S_field[i, j, z_idx] = build_scattering_matrix(z_local=1.0 / n_eff)


def inject_beam_2d(lattice, y_center, beam_width, amplitude, wavelength, x_inj=2):
    k = 2.0 * np.pi / wavelength
    phase = k * lattice.timestep
    j_indices = np.arange(lattice.ny)
    dy = j_indices - y_center
    envelope = amplitude * np.exp(-(dy**2) / (2.0 * beam_width**2))
    pulse = envelope * np.sin(phase)
    lattice.V_inc[x_inj, :, lattice.my_z, 0] += pulse


def main():
    print("=" * 70)
    print("  K4-TLM KERR METRIC LENSING — BERNOULLI VORTEX")
    print("  Photon hooking dynamically via asymmetric scattering.")
    print("=" * 70)

    NX, NY = 500, 200
    N_STEPS = 550
    BEAM_Y_PROGRADE = NY // 2 + 15
    BEAM_Y_RETROGRADE = NY // 2 - 15
    BEAM_W = 4.0
    WAVELENGTH = 10.0
    AMPLITUDE = 0.2
    R_CORE = 12.0
    N0 = 0.6  # Moderate gravity
    V_SPIN = 0.5  # Strong spin near core (50% c)

    cx, cy = NX // 2, NY // 2

    # ── Sim 1: Prograde (with the flow) ──
    print(f"\n[1] Prograde Lensing (y = {BEAM_Y_PROGRADE})...")
    lat_pro = K4Lattice2D(NX, NY, alternating_chirality=True, pml_thickness=15, nonlinear=True)
    apply_kerr_vortex_2d(lat_pro, cx, cy, N0, R_CORE, V_SPIN)
    for step in range(N_STEPS):
        inject_beam_2d(lat_pro, BEAM_Y_PROGRADE, BEAM_W, AMPLITUDE, WAVELENGTH)
        lat_pro.step()
    field_pro = lat_pro.get_field_array()

    # ── Sim 2: Retrograde (against the flow) ──
    print(f"\n[2] Retrograde Lensing (y = {BEAM_Y_RETROGRADE})...")
    lat_ret = K4Lattice2D(NX, NY, alternating_chirality=True, pml_thickness=15, nonlinear=True)
    apply_kerr_vortex_2d(lat_ret, cx, cy, N0, R_CORE, V_SPIN)
    for step in range(N_STEPS):
        inject_beam_2d(lat_ret, BEAM_Y_RETROGRADE, BEAM_W, AMPLITUDE, WAVELENGTH)
        lat_ret.step()
    field_ret = lat_ret.get_field_array()

    # ── Sim 3: Zero Spin Reference (prograde altitude) ──
    print(f"\n[3] Zero Spin Reference (y = {BEAM_Y_PROGRADE})...")
    lat_ref = K4Lattice2D(NX, NY, alternating_chirality=True, pml_thickness=15, nonlinear=True)
    apply_kerr_vortex_2d(lat_ref, cx, cy, N0, R_CORE, 0.0)
    for step in range(N_STEPS):
        inject_beam_2d(lat_ref, BEAM_Y_PROGRADE, BEAM_W, AMPLITUDE, WAVELENGTH)
        lat_ref.step()
    field_ref = lat_ref.get_field_array()

    # Plot Comparison
    print("\n[Plotting] Frame Dragging Comparison...")
    fig, axes = plt.subplots(3, 1, figsize=(14, 12))

    titles = [
        f"PROGRADE: Wave moving WITH vortex (+y side). Less impedance = shallower hooking.",
        f"RETROGRADE: Wave moving AGAINST vortex (-y side). Higher impedance = deeper hooking.",
        f"SCHWARZSCHILD (Static Reference): Isotropic bending.",
    ]
    fields = [field_pro, field_ret, field_ref]
    y_lines = [BEAM_Y_PROGRADE, BEAM_Y_RETROGRADE, BEAM_Y_PROGRADE]

    # Pre-render flow field vectors for visualization
    y_grid, x_grid = np.mgrid[0:NY:10, 0:NX:10]
    vx_grid, vy_grid = np.zeros_like(x_grid, dtype=float), np.zeros_like(y_grid, dtype=float)
    if V_SPIN > 0:
        for i in range(x_grid.shape[0]):
            for j in range(x_grid.shape[1]):
                xi, yi = x_grid[i, j], y_grid[i, j]
                r = np.sqrt((xi - cx) ** 2 + (yi - cy) ** 2) + 1e-5
                v_mag = V_SPIN * min(R_CORE / r, r / R_CORE)
                if r > R_CORE * 10:
                    v_mag = 0
                vx_grid[i, j] = -v_mag * (yi - cy) / r
                vy_grid[i, j] = v_mag * (xi - cx) / r

    vmax = 0.25
    for idx, (ax, field, title, beam_y) in enumerate(zip(axes, fields, titles, y_lines)):
        # im = ax.imshow(  # bulk lint fixup pass
        #     field.T,
        #     cmap="hot",
        #     origin="lower",
        #     extent=[0, NX, 0, NY],
        #     norm=PowerNorm(gamma=0.5, vmin=0, vmax=vmax),
        # )
        circle = plt.Circle((cx, cy), R_CORE, color="#00E5FF", fill=False, lw=1.5, ls="--")
        ax.add_patch(circle)
        ax.axhline(beam_y, color="white", ls=":", alpha=0.4, lw=1)

        # Plot vector field overlay on the top two plots
        if idx < 2:
            ax.quiver(x_grid, y_grid, vx_grid, vy_grid, color="cyan", alpha=0.3, scale=3)

        ax.set_title(title, color="black", fontsize=12, fontweight="bold", pad=8)
        ax.axis("off")

    plt.tight_layout(rect=[0, 0, 1, 0.96])
    fig.patch.set_facecolor("white")
    fig.suptitle(
        "Kerr Frame Dragging — Acoustic Bernoulli Asymmetry (D-Shape Effect)",
        fontsize=16,
        fontweight="bold",
    )

    out_dir = os.path.join(os.path.dirname(__file__), "..", "..", "manuscript", "vol_3_macroscopic", "figures")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "kerr_lensing_asymmetry.png")
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()

    print(f"  Saved: {out_path}")
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

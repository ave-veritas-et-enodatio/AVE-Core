#!/usr/bin/env python3
r"""
AVE Photon: Helical Torsional Wave on the Chiral Vacuum
========================================================

The single coolest visualization of the AVE framework:

A circularly polarized photon propagating through the 3D FDTD lattice.
In the AVE picture, this is a torsional wave — a twist propagating through
the chiral LC network at exactly c. The helicity (left/right circular
polarization) is realized geometrically: the E and H vectors rotate as
a helix, and the PITCH of the helix IS the wavelength.

The photon is perfectly impedance-matched: Z₀ = √(μ₀/ε₀) = 377 Ω at
every point along its path. This is why it propagates without loss — it
IS the lattice vibrating in its natural mode.

What you see:
    - Glowing helical streamlines of E (red) and H (blue) rotating in 3D
    - The wavefront expanding as a sphere ahead of the photon
    - The lattice mesh visible as a translucent grid
    - The photon IS a twist in the impedance of spacetime

Usage:
    python src/scripts/vol_1_foundations/visualize_photon_helicity.py
"""

import os
import sys

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.cm as cm
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

try:
    from ave.core.fdtd_3d_jax import FDTD3DEngineJAX as FDTD3DEngine
except ImportError:
    from ave.core.fdtd_3d import FDTD3DEngine

# ====================================================================
# Parameters
# ====================================================================
N = 60  # Grid size (60³)
DX = 0.01  # 1 cm per cell
FREQ = 1.5e9  # 1.5 GHz → λ ≈ 20 cm ≈ 20 cells (nice helix pitch)
SIGMA = 8.0  # Gaussian envelope width in cells

TOTAL_FRAMES = 50
STEPS_PER_FRAME = 4


def main():
    print("=" * 60)
    print("  AVE PHOTON: Helical Torsional Wave Visualization")
    print("=" * 60)

    # Initialize the FDTD engine (linear vacuum, PML boundaries)
    eng = FDTD3DEngine(N, N, N, dx=DX, linear_only=True, use_pml=True, pml_layers=8)

    c = eng.c
    wavelength = c / FREQ
    cells_per_lambda = wavelength / DX
    print(f"  Frequency: {FREQ/1e9:.1f} GHz")
    print(f"  Wavelength: {wavelength*100:.1f} cm ({cells_per_lambda:.1f} cells)")
    print(f"  Grid: {N}³ @ {DX*100:.1f} cm/cell ({N*DX*100:.0f} cm domain)")
    print(f"  Impedance: Z₀ = 377 Ω (perfectly matched)")

    # Inject a circularly polarized Gaussian pulse at one face
    # CP = E_y sin(ωt) + E_z cos(ωt) propagating in +x
    src_x = 12  # Source plane (past PML)
    omega = 2 * np.pi * FREQ

    print(f"\n  Injecting left-handed circularly polarized pulse...")
    print(f"  Source plane: x = {src_x}")

    # Pre-run to inject the pulse and let it propagate
    all_frames = []
    total_steps = TOTAL_FRAMES * STEPS_PER_FRAME

    for step in range(total_steps):
        t = step * eng.dt

        # Gaussian-windowed circularly polarized source
        t_center = 20 * eng.dt * STEPS_PER_FRAME  # Peak at frame 20
        gauss = np.exp(-0.5 * ((t - t_center) / (SIGMA * eng.dt * STEPS_PER_FRAME)) ** 2)

        # Circular polarization: E_y + iE_z
        amp = 500.0
        Ey_src = gauss * np.sin(omega * t) * amp
        Ez_src = gauss * np.cos(omega * t) * amp

        # Scaling law: R_helix = λ/(2π) = c/(2πf)
        # The helical radius IS the photon's transverse coherence length
        # Higher frequency → tighter helix → angular momentum polarizes
        # a smaller region of the grid
        R = max(3, int(cells_per_lambda / (2 * np.pi)))  # cells

        # Inject across a focused disk matching the helix radius
        cy, cz = N // 2, N // 2
        for dy in range(-R, R + 1):
            for dz in range(-R, R + 1):
                if dy**2 + dz**2 <= R**2:
                    # Hard source (overwrite, not additive)
                    eng.Ey = eng.Ey.at[src_x, cy + dy, cz + dz].set(Ey_src)
                    eng.Ez = eng.Ez.at[src_x, cy + dy, cz + dz].set(Ez_src)

        eng.step()

        # Capture frame
        if step % STEPS_PER_FRAME == 0:
            # Extract fields along the propagation axis
            frame_data = {
                "Ey": np.array(eng.Ey),
                "Ez": np.array(eng.Ez),
                "Hy": np.array(eng.Hy),
                "Hz": np.array(eng.Hz),
                "step": step,
                "t": t,
            }
            all_frames.append(frame_data)
            pct = 100.0 * step / total_steps
            energy = eng.total_field_energy()
            sys.stdout.write(f"\r  Simulating: {pct:5.1f}%  E={energy:.2e} J")
            sys.stdout.flush()

    print(f"\n  Simulation complete. {len(all_frames)} frames captured.")

    # ================================================================
    # RENDER THE ANIMATION
    # ================================================================
    print("  Rendering 3D helicity animation...")

    fig = plt.figure(figsize=(12, 8))
    fig.patch.set_facecolor("#0a0a1a")
    ax = fig.add_subplot(111, projection="3d")

    # Styling
    ax.set_facecolor("#0a0a1a")
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor("#1a1a3a")
    ax.yaxis.pane.set_edgecolor("#1a1a3a")
    ax.zaxis.pane.set_edgecolor("#1a1a3a")
    ax.tick_params(colors="#444466")
    ax.set_xlabel("X (propagation)", color="#666688", fontsize=9)
    ax.set_ylabel("Y", color="#666688", fontsize=9)
    ax.set_zlabel("Z", color="#666688", fontsize=9)

    # We'll plot:
    # 1. The E-field helix along the propagation axis (red/orange)
    # 2. The H-field helix along the propagation axis (cyan/blue)
    # 3. The wavefront as a translucent sphere
    # 4. Faint grid lines as the "lattice mesh"

    mid = N // 2
    x_range = np.arange(N)

    def update(frame_idx):
        ax.cla()
        ax.set_facecolor("#0a0a1a")
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.xaxis.pane.set_edgecolor("#1a1a3a")
        ax.yaxis.pane.set_edgecolor("#1a1a3a")
        ax.zaxis.pane.set_edgecolor("#1a1a3a")

        frame = all_frames[frame_idx]
        Ey = frame["Ey"]
        Ez = frame["Ez"]
        Hy = frame["Hy"]
        Hz = frame["Hz"]

        # Extract E and H along the central axis
        Ey_axis = Ey[:, mid, mid]
        Ez_axis = Ez[:, mid, mid]
        Hy_axis = Hy[:, mid, mid]
        Hz_axis = Hz[:, mid, mid]

        E_mag = np.sqrt(Ey_axis**2 + Ez_axis**2)
        H_mag = np.sqrt(Hy_axis**2 + Hz_axis**2)

        # Normalize for visualization
        E_max = max(np.max(E_mag), 1e-10)
        H_max = max(np.max(H_mag), 1e-10)

        scale = 8.0  # Visual scale factor

        # Plot E-field helix (red/orange)
        E_y_vis = mid + Ey_axis / E_max * scale
        E_z_vis = mid + Ez_axis / E_max * scale

        # Color by magnitude
        e_colors = cm.inferno(E_mag / E_max * 0.8 + 0.1)
        for i in range(len(x_range) - 1):
            if E_mag[i] > E_max * 0.02:  # threshold to avoid noise
                ax.plot(
                    [x_range[i], x_range[i + 1]],
                    [E_y_vis[i], E_y_vis[i + 1]],
                    [E_z_vis[i], E_z_vis[i + 1]],
                    color=e_colors[i],
                    linewidth=2.0,
                    alpha=min(E_mag[i] / E_max * 3, 0.95),
                )

        # Plot H-field helix (cyan/blue)
        # H is perpendicular to E and rotated 90° in the y-z plane
        H_y_vis = mid + Hy_axis / H_max * scale
        H_z_vis = mid + Hz_axis / H_max * scale

        h_colors = cm.cool(H_mag / H_max * 0.8 + 0.1)
        for i in range(len(x_range) - 1):
            if H_mag[i] > H_max * 0.02:
                ax.plot(
                    [x_range[i], x_range[i + 1]],
                    [H_y_vis[i], H_y_vis[i + 1]],
                    [H_z_vis[i], H_z_vis[i + 1]],
                    color=h_colors[i],
                    linewidth=1.5,
                    alpha=min(H_mag[i] / H_max * 3, 0.8),
                )

        # Draw field vectors at select points (quiver-like)
        sample_step = 3
        for i in range(src_x, N - 8, sample_step):
            if E_mag[i] > E_max * 0.05:
                # E vector from axis to helix
                ax.plot(
                    [i, i],
                    [mid, E_y_vis[i]],
                    [mid, E_z_vis[i]],
                    color="#ff4444",
                    linewidth=0.6,
                    alpha=E_mag[i] / E_max * 0.6,
                )
            if H_mag[i] > H_max * 0.05:
                ax.plot(
                    [i, i],
                    [mid, H_y_vis[i]],
                    [mid, H_z_vis[i]],
                    color="#4488ff",
                    linewidth=0.6,
                    alpha=H_mag[i] / H_max * 0.5,
                )

        # Propagation axis (faint gold line)
        ax.plot([0, N - 1], [mid, mid], [mid, mid], color="#aa8833", linewidth=0.5, alpha=0.3)

        # Wavefront indicator: find the leading edge of the pulse
        threshold = E_max * 0.05
        leading_edge = 0
        for i in range(N - 1, 0, -1):
            if E_mag[i] > threshold:
                leading_edge = i
                break

        if leading_edge > src_x + 2:
            # Draw a translucent circle at the wavefront
            theta_wf = np.linspace(0, 2 * np.pi, 30)
            wf_r = 6
            wf_y = mid + wf_r * np.cos(theta_wf)
            wf_z = mid + wf_r * np.sin(theta_wf)
            wf_x = np.full_like(theta_wf, leading_edge)
            ax.plot(wf_x, wf_y, wf_z, color="#ffcc44", linewidth=1.0, alpha=0.4)

        # Faint lattice grid lines (every 5 cells)
        grid_step = 5
        for gx in range(0, N, grid_step):
            ax.plot(
                [gx, gx],
                [mid - 10, mid + 10],
                [mid, mid],
                color="#222244",
                linewidth=0.3,
                alpha=0.2,
            )
            ax.plot(
                [gx, gx],
                [mid, mid],
                [mid - 10, mid + 10],
                color="#222244",
                linewidth=0.3,
                alpha=0.2,
            )

        ax.set_xlim(0, N)
        ax.set_ylim(mid - 12, mid + 12)
        ax.set_zlim(mid - 12, mid + 12)

        ax.set_title(
            "AVE Photon: Torsional Helix on the Chiral Vacuum\n"
            f"f = {FREQ/1e9:.1f} GHz  |  λ = {cells_per_lambda:.0f} cells  |  "
            r"$Z_0 = \sqrt{\mu_0/\varepsilon_0}$ = 377 Ω  |  "
            f"Frame {frame_idx+1}/{len(all_frames)}",
            color="#aaaacc",
            fontsize=10,
            pad=15,
        )

        # Rotate viewpoint slowly
        ax.view_init(elev=18, azim=-60 + frame_idx * 1.5)
        ax.tick_params(colors="#444466", labelsize=7)

        # Legend box
        props = {"boxstyle": "round", "facecolor": "#0a0a2a", "alpha": 0.9, "edgecolor": "#333366"}
        legend_text = (
            "━━ E-field helix (inferno)\n"
            "━━ H-field helix (cool)\n"
            "○  Wavefront\n"
            "Helicity = spin angular momentum\n"
            "Pitch = wavelength = c/f"
        )
        fig.text(
            0.02,
            0.02,
            legend_text,
            fontsize=8,
            color="#8888aa",
            verticalalignment="bottom",
            bbox=props,
            family="monospace",
        )

    print(f"  Assembling {len(all_frames)} frames...")
    ani = FuncAnimation(fig, update, frames=len(all_frames), blit=False)

    out_dir = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "sim_outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "ave_photon_helicity.gif")

    print(f"  Saving GIF to: {out_path}")
    ani.save(out_path, writer=PillowWriter(fps=12), dpi=120)
    plt.close(fig)

    print(f"\n  ✓ AVE Photon Helicity GIF complete!")
    print(f"    {out_path}")


if __name__ == "__main__":
    main()

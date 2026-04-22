#!/usr/bin/env python3
r"""
Photon → Electron Self-Trapping Transition
============================================

Visualizes the continuous transition from a free photon to a trapped
electron as frequency increases from f << f_C to f = f_C.

The helix radius R = c/(2πf) shrinks as frequency rises. When R → ℓ/(2π),
the photon's field wraps within one lattice cell, self-interferes, and
becomes topologically trapped: the unknot (electron).

The animation shows:
    Frame 1-20:  Low frequency → large helix → free photon propagating
    Frame 20-40: Frequency chirping upward → helix tightens
    Frame 40-50: Critical frequency → helix collapses → self-trapping
    Frame 50-60: Trapped state → glowing unknot ring oscillating on one node

Usage:
    python src/scripts/vol_2_subatomic/visualize_self_trapping.py
"""

import os

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.cm as cm  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.animation import FuncAnimation, PillowWriter  # noqa: E402

# ====================================================================
# Parameters
# ====================================================================
TOTAL_FRAMES = 60
LATTICE_SIZE = 40  # Visualization cells along propagation axis


def main():
    print("=" * 60)
    print("  PHOTON → ELECTRON: Self-Trapping Transition")
    print("=" * 60)

    fig, (ax_3d, ax_info) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={"width_ratios": [3, 1]})
    fig.patch.set_facecolor("#08081a")

    # Precompute all frames
    # Frequency chirps from f_low to f_Compton over the animation
    # In normalized units: λ goes from 30 cells down to 1 cell
    wavelengths = []
    for frame in range(TOTAL_FRAMES):
        if frame < 20:
            # Free photon: λ = 30 cells (large helix)
            lam = 30.0
        elif frame < 45:
            # Chirping: λ shrinks from 30 → 2π (≈6.28) → catches tail
            t = (frame - 20) / 25.0
            # Exponential chirp
            lam = 30.0 * np.exp(-t * np.log(30.0 / (2 * np.pi)))
        else:
            # Trapped: λ = 2π (one cell circumference = one lattice unit)
            lam = 2 * np.pi
        wavelengths.append(lam)

    def update(frame):
        ax_3d.cla()
        ax_info.cla()
        ax_3d.set_facecolor("#08081a")
        ax_info.set_facecolor("#08081a")

        lam = wavelengths[frame]
        R = lam / (2 * np.pi)  # Helix radius
        k = 2 * np.pi / lam  # Wavenumber

        # Phase: the "photon" propagates rightward
        if frame < 45:
            # Propagation phase
            phase_offset = frame * 0.3
            propagating = True
        else:
            # Trapped: oscillating in place
            phase_offset = frame * 0.8  # Faster oscillation
            propagating = False

        # Build the helix
        if propagating:
            # Propagating photon: helix along x
            n_points = 400
            x = np.linspace(0, LATTICE_SIZE, n_points)

            # Gaussian envelope (moves rightward)
            center = min(5 + frame * 0.6, LATTICE_SIZE - 5)
            sigma = max(lam * 0.8, 3.0)
            envelope = np.exp(-0.5 * ((x - center) / sigma) ** 2)

            # Circularly polarized E and H
            Ey = envelope * R * np.sin(k * x - phase_offset)
            Ez = envelope * R * np.cos(k * x - phase_offset)
            Hy = envelope * R * np.cos(k * x - phase_offset)  # 90° rotated
            Hz = -envelope * R * np.sin(k * x - phase_offset)

            mid = LATTICE_SIZE / 2

            # Plot E-helix
            e_mag = np.sqrt(Ey**2 + Ez**2)
            e_max = max(np.max(e_mag), 0.01)
            colors_e = cm.inferno(e_mag / e_max * 0.8 + 0.15)
            for i in range(0, len(x) - 1, 2):
                if e_mag[i] > e_max * 0.03:
                    ax_3d.plot(
                        [x[i], x[i + 1]],
                        [mid + Ey[i], mid + Ey[i + 1]],
                        color=colors_e[i],
                        linewidth=2.5,
                        alpha=min(e_mag[i] / e_max * 2, 0.95),
                    )

            # Plot H-helix
            h_mag = np.sqrt(Hy**2 + Hz**2)
            h_max = max(np.max(h_mag), 0.01)
            colors_h = cm.cool(h_mag / h_max * 0.7 + 0.2)
            for i in range(0, len(x) - 1, 2):
                if h_mag[i] > h_max * 0.03:
                    ax_3d.plot(
                        [x[i], x[i + 1]],
                        [mid + Hz[i], mid + Hz[i + 1]],
                        color=colors_h[i],
                        linewidth=1.8,
                        alpha=min(h_mag[i] / h_max * 2, 0.8),
                    )

            # Field vectors from axis
            for i in range(0, len(x) - 1, max(1, int(lam / 2))):
                if e_mag[i] > e_max * 0.1:
                    ax_3d.plot(
                        [x[i], x[i]],
                        [mid, mid + Ey[i]],
                        color="#ff4444",
                        linewidth=0.5,
                        alpha=e_mag[i] / e_max * 0.4,
                    )

            # Propagation axis
            ax_3d.axhline(y=mid, color="#aa8833", linewidth=0.4, alpha=0.3)

            # Wavefront
            if e_max > 0.05:
                leading = x[np.max(np.where(e_mag > e_max * 0.05))]
                ax_3d.axvline(x=leading, color="#ffcc44", linewidth=1, alpha=0.3, linestyle="--")

            ax_3d.set_xlim(0, LATTICE_SIZE)
            ax_3d.set_ylim(mid - 18, mid + 18)

        else:
            # TRAPPED STATE: the unknot ring
            mid = LATTICE_SIZE / 2
            theta = np.linspace(0, 2 * np.pi, 200)

            # Unknot ring oscillating at the trapped node
            ring_r = 1.5  # Tiny ring
            osc = np.sin(phase_offset)
            brightness = 0.5 + 0.5 * abs(osc)

            # Draw the glowing ring
            ring_x = mid + ring_r * np.cos(theta)
            ring_y = mid + ring_r * np.sin(theta) * osc * 0.3  # slight wobble

            # Multiple glow layers
            for glow in [4.0, 2.5, 1.5, 1.0]:
                alpha = brightness * (0.15 / glow)
                ax_3d.plot(
                    ring_x,
                    ring_y,
                    color="#ff6622",
                    linewidth=glow * 3,
                    alpha=alpha,
                    solid_capstyle="round",
                )
            ax_3d.plot(
                ring_x,
                ring_y,
                color="#ffaa44",
                linewidth=2.0,
                alpha=brightness * 0.9,
                solid_capstyle="round",
            )

            # Draw the lattice node it sits on
            ax_3d.scatter([mid], [mid], s=100, color="#333366", marker="s", zorder=0, alpha=0.5)

            # Radial field lines (the strain on the node)
            for angle in np.linspace(0, 2 * np.pi, 8, endpoint=False):
                r1 = ring_r * 1.2
                r2 = ring_r * 3.0 * brightness
                ax_3d.plot(
                    [mid + r1 * np.cos(angle), mid + r2 * np.cos(angle)],
                    [mid + r1 * np.sin(angle), mid + r2 * np.sin(angle)],
                    color="#ff4422",
                    linewidth=0.8,
                    alpha=0.3 * brightness,
                )

            # Label
            ax_3d.text(
                mid,
                mid - 8,
                "TRAPPED UNKNOT\n(electron)",
                ha="center",
                color="#ffaa44",
                fontsize=11,
                fontweight="bold",
                alpha=brightness,
            )

            ax_3d.set_xlim(mid - 12, mid + 12)
            ax_3d.set_ylim(mid - 12, mid + 12)

        # Faint lattice grid
        for gx in range(0, LATTICE_SIZE + 1, 2):
            ax_3d.axvline(x=gx, color="#151530", linewidth=0.3, alpha=0.3)

        ax_3d.set_aspect("equal")
        ax_3d.tick_params(colors="#444466", labelsize=7)
        ax_3d.spines["bottom"].set_color("#222244")
        ax_3d.spines["left"].set_color("#222244")
        ax_3d.spines["top"].set_visible(False)
        ax_3d.spines["right"].set_visible(False)

        # Title
        if frame < 45:
            state = "FREE PHOTON"
            state_color = "#44aaff"
        else:
            state = "TRAPPED ELECTRON"
            state_color = "#ff6622"

        ax_3d.set_title(f"{state}", color=state_color, fontsize=14, fontweight="bold", pad=10)

        # ---- Info panel ----
        ax_info.set_xlim(0, 1)
        ax_info.set_ylim(0, 1)
        ax_info.axis("off")

        f_ratio = 2 * np.pi / lam  # f/f_C in normalized units
        info_lines = [
            ("λ / ℓ_node", f"{lam:.1f}"),
            ("R_helix / ℓ", f"{R:.2f}"),
            ("f / f_C", f"{f_ratio:.3f}"),
            ("", ""),
            ("State", state.lower()),
        ]

        y_pos = 0.85
        for label, val in info_lines:
            if label:
                ax_info.text(
                    0.1,
                    y_pos,
                    label,
                    color="#8888aa",
                    fontsize=10,
                    fontfamily="monospace",
                    transform=ax_info.transAxes,
                )
                ax_info.text(
                    0.9,
                    y_pos,
                    val,
                    color="#ddddff",
                    fontsize=10,
                    fontfamily="monospace",
                    ha="right",
                    transform=ax_info.transAxes,
                )
            y_pos -= 0.08

        # Progress bar (frequency)
        bar_y = 0.35
        ax_info.text(
            0.1,
            bar_y + 0.05,
            "frequency →",
            color="#666688",
            fontsize=8,
            transform=ax_info.transAxes,
        )
        ax_info.barh(bar_y, f_ratio, height=0.03, color=state_color, alpha=0.7, left=0.1)
        ax_info.barh(bar_y, 1.0, height=0.03, color="#222244", alpha=0.3, left=0.1)

        # Scaling law
        ax_info.text(
            0.5,
            0.15,
            r"$R = \frac{c}{2\pi f}$",
            color="#aaaacc",
            fontsize=14,
            ha="center",
            transform=ax_info.transAxes,
        )
        ax_info.text(
            0.5,
            0.05,
            f"Frame {frame+1}/{TOTAL_FRAMES}",
            color="#444466",
            fontsize=8,
            ha="center",
            transform=ax_info.transAxes,
        )

    print(f"  Rendering {TOTAL_FRAMES} frames...")
    ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES, blit=False)

    out_dir = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "sim_outputs")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "photon_electron_transition.gif")

    ani.save(out_path, writer=PillowWriter(fps=10), dpi=120)
    plt.close(fig)

    print("\n  ✓ Self-trapping transition GIF complete!")
    print(f"    {out_path}")


if __name__ == "__main__":
    main()

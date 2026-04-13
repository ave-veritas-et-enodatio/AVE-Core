#!/usr/bin/env python3
r"""
AVE: Vacuum Phonon Propagation — 2D Lattice Slice
=====================================================

Animates a Gaussian wave packet ("photon") propagating through a 2D slice
of the vacuum LC lattice.  The heatmap shows the wave energy density P²
using the `hot` colormap — black = quiet vacuum, bright = wave energy.

This is what a photon looks like under AVE: a coherent phonon mode of the
vacuum lattice, propagating at c = 1/√(LC).

Two panels:
  TOP:    Instantaneous signed pressure P (shows wave oscillation)
  BOTTOM: Energy density P² (what a detector would measure)

Output:  assets/sim_outputs/vacuum_phonon_propagation_3d.gif
"""

import os
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import PowerNorm

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       '..', '..', 'assets', 'sim_outputs')
os.makedirs(OUT_DIR, exist_ok=True)


def main():
    print("═" * 70)
    print("  AVE: Vacuum Phonon Propagation — 2D Lattice Slice")
    print("  A photon is a lattice phonon at c = 1/√(LC)")
    print("═" * 70)

    # ─── Grid ───
    NX, NY = 1200, 300  # Wide, not tall — shows propagation distance
    dx = 1.0
    dt = 0.45  # CFL < 1/√2
    c = 1.0    # = 1/√(LC) in natural units

    TOTAL_STEPS = 2400
    STEPS_PER_FRAME = 6
    TOTAL_FRAMES = TOTAL_STEPS // STEPS_PER_FRAME

    # ─── Fields ───
    P = np.zeros((NX, NY))
    Vx = np.zeros((NX, NY))
    Vy = np.zeros((NX, NY))

    # ─── Sponge absorbing boundary ───
    sponge = 40
    damping = np.ones((NX, NY))
    for i in range(sponge):
        f = 1.0 - 0.04 * ((sponge - i) / sponge) ** 2
        damping[i, :] *= f
        damping[NX - 1 - i, :] *= f
        damping[:, i] *= f
        damping[:, NY - 1 - i] *= f

    # ─── Initial Gaussian Wave Packet ───
    # A "photon": Gaussian envelope × sinusoidal carrier frequency
    # Centered at x=150, propagating in +x direction
    x0 = 150.0
    y0 = NY / 2.0
    sigma_x = 30.0   # Envelope width along propagation direction
    sigma_y = 40.0    # Envelope width transverse
    k0 = 0.15         # Carrier wavenumber → sets wavelength λ ≈ 42 cells

    xx, yy = np.meshgrid(np.arange(NX), np.arange(NY), indexing='ij')
    envelope = np.exp(-((xx - x0) ** 2) / (2 * sigma_x ** 2)
                      - ((yy - y0) ** 2) / (2 * sigma_y ** 2))

    # Signed pressure: cosine carrier inside Gaussian envelope
    P[:] = envelope * np.cos(k0 * xx)

    # To make it propagate RIGHT, set initial velocity field
    # For a plane wave propagating in +x:  Vx = c * P (impedance matching)
    Vx[:] = c * envelope * np.cos(k0 * xx)

    # ─── Simulation ───
    print(f"  Grid: {NX}×{NY}, {TOTAL_STEPS} steps, {TOTAL_FRAMES} frames")
    print(f"  Wave packet: λ ≈ {2 * np.pi / k0:.0f} cells, σ_x = {sigma_x}")

    frames_P = []     # Signed pressure (shows oscillation)
    frames_P2 = []    # Energy density (what detector sees)

    for frame in range(TOTAL_FRAMES):
        for _ in range(STEPS_PER_FRAME):
            # Standard 2D acoustic FDTD update
            Vx[:-1, :] -= dt * (P[1:, :] - P[:-1, :]) / dx
            Vy[:, :-1] -= dt * (P[:, 1:] - P[:, :-1]) / dx

            P[1:-1, 1:-1] -= dt * c**2 * (
                (Vx[1:-1, 1:-1] - Vx[:-2, 1:-1]) / dx +
                (Vy[1:-1, 1:-1] - Vy[1:-1, :-2]) / dx
            )

            P *= damping
            Vx *= damping
            Vy *= damping

        frames_P.append(P.copy())
        frames_P2.append((P ** 2).copy())

        if frame % 40 == 0:
            print(f"    → Frame {frame}/{TOTAL_FRAMES}")

    print("  Simulation complete. Rendering animation...")

    # ─── Normalization ───
    p_max = max(np.percentile(np.abs(frames_P[10]), 99.9), 1e-6)
    e_max = max(np.percentile(frames_P2[10], 99.9), 1e-6)

    # ─── Figure ───
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(18, 7),
                                    gridspec_kw={'height_ratios': [1, 1]})
    fig.patch.set_facecolor('#050510')
    fig.suptitle(
        r"AVE: Vacuum Phonon Propagation  —  $c = 1/\sqrt{LC}$"
        "  —  A photon is a lattice phonon",
        color='white', fontsize=15, fontweight='bold', y=0.98)

    for ax in (ax1, ax2):
        ax.set_facecolor('#050510')
        ax.tick_params(colors='white', labelsize=7)
        for s in ax.spines.values():
            s.set_color('#334')

    # Panel 1: Signed pressure (blue-white-red diverging)
    im1 = ax1.imshow(frames_P[0].T, cmap='seismic', origin='lower',
                     extent=[0, NX, 0, NY], vmin=-p_max, vmax=p_max,
                     aspect='auto', interpolation='bilinear')
    ax1.set_title("Instantaneous Pressure P  (signed — shows wave oscillation)",
                  color='white', fontsize=12, pad=6)
    ax1.set_ylabel("y", color='white', fontsize=10)

    # Panel 2: Energy density P² (hot heatmap)
    im2 = ax2.imshow(frames_P2[0].T, cmap='hot', origin='lower',
                     extent=[0, NX, 0, NY],
                     aspect='auto', interpolation='bilinear',
                     norm=PowerNorm(gamma=0.4, vmin=0, vmax=e_max))
    ax2.set_title("Energy Density P²  (what a detector measures — the 'photon')",
                  color='white', fontsize=12, pad=6)
    ax2.set_ylabel("y", color='white', fontsize=10)
    ax2.set_xlabel("x  (lattice sites)", color='white', fontsize=10)

    # Propagation arrow
    ax2.annotate('', xy=(NX * 0.85, NY * 0.85), xytext=(NX * 0.6, NY * 0.85),
                 arrowprops=dict(arrowstyle='->', color='#ff6600', lw=2.5))
    ax2.text(NX * 0.72, NY * 0.91, 'propagation',
             color='#ff6600', fontsize=10, ha='center', family='monospace')

    time_text = fig.text(0.02, 0.01, '', color='white', fontsize=9,
                         family='monospace', alpha=0.6)

    plt.tight_layout(rect=[0, 0.02, 1, 0.95])

    def update(frame_idx):
        im1.set_data(frames_P[frame_idx].T)
        im2.set_data(frames_P2[frame_idx].T)
        time_text.set_text(f't = {frame_idx * STEPS_PER_FRAME * dt:.0f} · τ_LC'
                           f'    frame {frame_idx}/{TOTAL_FRAMES}')
        return [im1, im2, time_text]

    ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES, blit=True, interval=50)

    out_path = os.path.join(OUT_DIR, 'vacuum_phonon_propagation_3d.gif')
    print(f"  Saving animation to: {out_path}")
    ani.save(out_path, writer='pillow', fps=22, dpi=110)
    plt.close()

    print(f"  ✅ Vacuum phonon animation complete → {out_path}")


if __name__ == "__main__":
    main()

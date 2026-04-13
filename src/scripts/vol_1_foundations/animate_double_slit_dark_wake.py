#!/usr/bin/env python3
r"""
Animated Double Slit: High-Contrast Dark Wake Side-by-Side
============================================================

Two panels animated as a GIF:
  LEFT:   No observer  — particle through Slit 1, wake through both → fringes
  RIGHT:  Observer at slit 2 — wake thermalized → decoherence

AVE physics: the topological defect (particle) passes through ONE slit.
The continuous transverse inductive wake radiates from the particle's
trajectory and passes through BOTH slits, creating interference.
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap

OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'assets', 'sim_outputs')
os.makedirs(OUT_DIR, exist_ok=True)


class DoubleSlit2D:
    """Compact 2D FDTD wave solver for wake animation."""

    def __init__(self, nx=600, ny=400, observer_at_slit2=False):
        self.NX, self.NY = nx, ny
        self.dt, self.dx = 0.45, 1.0

        self.P  = np.zeros((nx, ny))
        self.Vx = np.zeros((nx, ny))
        self.Vy = np.zeros((nx, ny))

        # Sponge (absorbing boundary)
        sponge = 35
        self.damping = np.ones((nx, ny))
        for i in range(sponge):
            f = 1.0 - 0.06 * ((sponge - i) / sponge)**2
            self.damping[i, :] *= f
            self.damping[nx-1-i, :] *= f
            self.damping[:, i] *= f
            self.damping[:, ny-1-i] *= f

        # Double slit wall
        self.wall_x = int(nx * 0.38)
        wt = 4
        self.slit_w = 14
        slit_sep = 80
        self.slit_1 = ny // 2 - slit_sep // 2
        self.slit_2 = ny // 2 + slit_sep // 2
        self.wall = np.zeros((nx, ny), dtype=bool)
        self.wall[self.wall_x:self.wall_x+wt, :] = True
        self.wall[self.wall_x:self.wall_x+wt, self.slit_1-self.slit_w//2:self.slit_1+self.slit_w//2] = False
        self.wall[self.wall_x:self.wall_x+wt, self.slit_2-self.slit_w//2:self.slit_2+self.slit_w//2] = False

        # Observer = Ohmic load at slit 2 (AVE first principles)
        # In AVE, a detector thermalizes wave energy via Joule friction:
        # W ∝ |∂_t A|² / Z_det.  Direct energy extraction, not just reflection.
        self.obs_damping = np.zeros((nx, ny))
        if observer_at_slit2:
            ox, oy = self.wall_x, self.slit_2
            damping_strength = 0.85  # strong Ohmic load (real detector)
            for dxi in range(-4, 5):
                for dyi in range(-self.slit_w, self.slit_w):
                    xi, yi = ox + dxi, oy + dyi
                    if 0 <= xi < nx and 0 <= yi < ny:
                        r = np.sqrt(dxi**2 + (dyi / self.slit_w * 3)**2) / 3
                        if r < 1.0:
                            self.obs_damping[xi, yi] = damping_strength * (1.0 - r)**2

        self.freq = 0.055
        self.source_y = self.slit_1  # Particle aimed at Slit 1 (AVE physics)
        self.source_x_start = 50
        self.particle_speed = 0.22

    def step(self, t):
        P, Vx, Vy = self.P, self.Vx, self.Vy
        dt, dx = self.dt, self.dx

        Vx[:-1, :] -= dt * (P[1:, :] - P[:-1, :]) / dx
        Vy[:, :-1] -= dt * (P[:, 1:] - P[:, :-1]) / dx
        Vx[self.wall] = 0
        Vy[self.wall] = 0

        P[1:-1, 1:-1] -= dt * (
            (Vx[1:-1, 1:-1] - Vx[:-2, 1:-1]) / dx +
            (Vy[1:-1, 1:-1] - Vy[1:-1, :-2]) / dx
        )
        # Ohmic observer: thermalize ALL field components at detector
        P *= (1.0 - self.obs_damping)
        Vx *= (1.0 - self.obs_damping)
        Vy *= (1.0 - self.obs_damping)
        P *= self.damping
        Vx *= self.damping
        Vy *= self.damping

        # Moving particle source — travels through Slit 1 and continues
        # Wake tapers off past the wall (already launched)
        px = int(self.source_x_start + t * self.particle_speed)
        if 0 < px < self.wall_x + 40:
            if px > self.wall_x:
                taper = max(0, 1.0 - (px - self.wall_x) / 40.0)
            else:
                taper = 1.0
            amp = np.sin(2 * np.pi * self.freq * t) * 3.0 * taper
            P[px, self.source_y] += amp
            for dy in [-2, -1, 1, 2]:
                if 0 <= self.source_y + dy < self.NY:
                    P[px, self.source_y + dy] += amp * 0.3


def main():
    print("=" * 70)
    print("  Animated Double Slit: High-Contrast Dark Wake")
    print("=" * 70)

    NX, NY = 600, 400
    TOTAL_STEPS = 2000
    STEPS_PER_FRAME = 8
    TOTAL_FRAMES = TOTAL_STEPS // STEPS_PER_FRAME

    sim_no  = DoubleSlit2D(NX, NY, observer_at_slit2=False)
    sim_obs = DoubleSlit2D(NX, NY, observer_at_slit2=True)

    frames_no = []
    frames_obs = []

    print(f"  Computing {TOTAL_FRAMES} frames ({TOTAL_STEPS} FDTD steps)...")
    for frame in range(TOTAL_FRAMES):
        for _ in range(STEPS_PER_FRAME):
            t = frame * STEPS_PER_FRAME + _
            sim_no.step(t)
            sim_obs.step(t)

        # Store energy density P² for hot colormap (0 = black = quiet vacuum)
        frames_no.append((sim_no.P**2).copy())
        frames_obs.append((sim_obs.P**2).copy())

        if frame % 25 == 0:
            print(f"    -> Frame {frame}/{TOTAL_FRAMES}")

    print("  FDTD complete. Rendering animation...")

    # Global vmax for consistent normalization
    global_max = max(np.percentile(frames_no[-1], 99),
                     np.percentile(frames_obs[-1], 99))
    vmax = max(float(global_max), 1e-6)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    fig.patch.set_facecolor('#0a0a2e')
    fig.suptitle(
        r"AVE Double Slit: Particle Through Slit 1, Wake Through Both",
        color='white', fontsize=16, fontweight='bold', y=0.97)

    for ax in (ax1, ax2):
        ax.set_facecolor('#0a0a2e')
        ax.tick_params(colors='white', labelsize=8)
        for s in ax.spines.values():
            s.set_color('#334')

    im1 = ax1.imshow(frames_no[0].T, cmap='hot', origin='lower',
                     extent=[0, NX, 0, NY], vmin=0, vmax=vmax, aspect='auto')
    im2 = ax2.imshow(frames_obs[0].T, cmap='hot', origin='lower',
                     extent=[0, NX, 0, NY], vmin=0, vmax=vmax, aspect='auto')

    # Wall overlays
    wall_vis = np.ma.masked_where(~sim_no.wall, np.ones((NX, NY)))
    ax1.imshow(wall_vis.T, cmap='Greys', alpha=0.9, origin='lower',
               extent=[0, NX, 0, NY], aspect='auto')
    ax2.imshow(wall_vis.T, cmap='Greys', alpha=0.9, origin='lower',
               extent=[0, NX, 0, NY], aspect='auto')

    # Observer marker
    ax2.plot(sim_obs.wall_x, sim_obs.slit_2, 'o', color='#00ff00',
             markersize=10, markeredgecolor='white', markeredgewidth=2, zorder=10)
    ax2.annotate('OBSERVER', xy=(sim_obs.wall_x, sim_obs.slit_2),
                 xytext=(sim_obs.wall_x - 70, sim_obs.slit_2 + 50),
                 fontsize=9, color='#00ff00', fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color='#00ff00', lw=1.5))

    ax1.set_title("No Observer: Coherent Wake Interference",
                  color='white', fontsize=13, fontweight='bold', pad=8)
    ax2.set_title("Observer at Slit 2: Wake Decoherence",
                  color='white', fontsize=13, fontweight='bold', pad=8)

    # Slit labels
    for ax, sim in [(ax1, sim_no), (ax2, sim_obs)]:
        ax.annotate('Slit 1', xy=(sim.wall_x+6, sim.slit_1),
                    fontsize=8, color='white', alpha=0.7)
        ax.annotate('Slit 2', xy=(sim.wall_x+6, sim.slit_2),
                    fontsize=8, color='white', alpha=0.7)

    # Explanation box
    props = dict(boxstyle='round', facecolor='#111122', alpha=0.9, edgecolor='#ff6600')
    ax1.text(0.02, 0.97,
             "Particle passes through SLIT 1\n"
             "Wake radiates from trajectory\n"
             "and passes through BOTH slits",
             transform=ax1.transAxes, fontsize=9, color='white',
             verticalalignment='top', bbox=props)

    props2 = dict(boxstyle='round', facecolor='#111122', alpha=0.9, edgecolor='#00ff00')
    ax2.text(0.02, 0.97,
             "Particle still through Slit 1\n"
             "Detector at Slit 2 thermalizes\n"
             "wake phase → no interference",
             transform=ax2.transAxes, fontsize=9, color='white',
             verticalalignment='top', bbox=props2)

    plt.tight_layout(rect=[0, 0, 1, 0.94])

    def update(frame):
        im1.set_data(frames_no[frame].T)
        im2.set_data(frames_obs[frame].T)
        return [im1, im2]

    ani = FuncAnimation(fig, update, frames=TOTAL_FRAMES, blit=True)
    out_path = os.path.join(OUT_DIR, 'double_slit_dark_wake_animated.gif')
    ani.save(out_path, writer='pillow', fps=20)
    plt.close()

    print(f"  ✅ Animated dark wake saved: {out_path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
r"""
Double Slit: Dark Wake Visualization
======================================

Shows the INSTANTANEOUS pressure field, not time-averaged intensity.
This reveals the actual wave mechanics:

  - The soliton (particle) as a bright moving source aimed at SLIT 1
  - The radial WAKE expanding outward through the lattice
  - The particle passes through Slit 1; the wake reaches BOTH slits
  - Coherent interference fringes forming on the far side

Three panels:
  1. Instantaneous P (diverging colormap: dark wake visible)
  2. Instantaneous P with observer (wake disrupted at slit 2)
  3. Time-averaged |P|² comparison (far-field cross-section)

Usage:
    python src/scripts/vol_1_foundations/visualize_dark_wake.py
"""

import os
import sys
import numpy as np


import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "sim_outputs")
os.makedirs(OUT_DIR, exist_ok=True)


class DarkWakeSim:
    """2D FDTD showing the instantaneous dark wake of a soliton."""

    def __init__(self, nx=800, ny=500, observer_damping=0.0):
        self.NX = nx
        self.NY = ny
        self.dt = 0.45
        self.dx = 1.0

        self.P = np.zeros((nx, ny))
        self.Vx = np.zeros((nx, ny))
        self.Vy = np.zeros((nx, ny))
        self.intensity = np.zeros((nx, ny))

        # Sponge
        self.sponge = 45
        self.damping = self._sponge()

        # Wall
        self.wall_x = int(nx * 0.38)
        self.wall_t = 4
        self.slit_w = 16
        self.slit_sep = 85
        self.slit_1 = ny // 2 - self.slit_sep // 2
        self.slit_2 = ny // 2 + self.slit_sep // 2
        self.wall = self._wall()

        # Observer = Ohmic load at slit 2 (AVE first principles)
        # Detector thermalizes wave energy via Joule friction:
        # W ∝ |∂_t A|² / Z_det.  Direct energy extraction.
        self.obs_damping = np.zeros((nx, ny))
        if observer_damping > 0:
            ox, oy = self.wall_x, self.slit_2
            for dxi in range(-4, 5):
                for dyi in range(-self.slit_w, self.slit_w):
                    xi, yi = ox + dxi, oy + dyi
                    if 0 <= xi < nx and 0 <= yi < ny:
                        r = np.sqrt(dxi**2 + (dyi / self.slit_w * 3) ** 2) / 3
                        if r < 1.0:
                            self.obs_damping[xi, yi] = observer_damping * (1.0 - r) ** 2

        # Source: particle aimed at Slit 1 (AVE: particle through ONE slit)
        self.freq = 0.055
        self.source_y = self.slit_1  # Aimed at Slit 1
        self.particle_speed = 0.22  # Nodes per timestep
        self.source_x_start = 55

        # Store snapshots of instantaneous P
        self.snapshots = []
        self.snapshot_times = []

    def _sponge(self):
        d = np.ones((self.NX, self.NY))
        s = self.sponge
        for i in range(s):
            f = 1.0 - 0.07 * ((s - i) / s) ** 2
            d[i, :] *= f
            d[self.NX - 1 - i, :] *= f
            d[:, i] *= f
            d[:, self.NY - 1 - i] *= f
        return d

    def _wall(self):
        w = np.zeros((self.NX, self.NY), dtype=bool)
        wx, wt = self.wall_x, self.wall_t
        w[wx : wx + wt, :] = True
        sw = self.slit_w
        w[wx : wx + wt, self.slit_1 - sw // 2 : self.slit_1 + sw // 2] = False
        w[wx : wx + wt, self.slit_2 - sw // 2 : self.slit_2 + sw // 2] = False
        return w

    def run(self, steps=1800, snapshot_interval=150):
        P, Vx, Vy = self.P, self.Vx, self.Vy
        d, wall = self.damping, self.wall
        dt, dx = self.dt, self.dx

        integrate_start = steps // 3

        for t in range(steps):
            Vx[:-1, :] -= dt * (P[1:, :] - P[:-1, :]) / dx
            Vy[:, :-1] -= dt * (P[:, 1:] - P[:, :-1]) / dx
            Vx[wall] = 0
            Vy[wall] = 0

            P[1:-1, 1:-1] -= dt * ((Vx[1:-1, 1:-1] - Vx[:-2, 1:-1]) / dx + (Vy[1:-1, 1:-1] - Vy[1:-1, :-2]) / dx)
            # Ohmic observer: thermalize ALL field components at detector
            P *= 1.0 - self.obs_damping
            Vx *= 1.0 - self.obs_damping
            Vy *= 1.0 - self.obs_damping
            P *= d
            Vx *= d
            Vy *= d

            # Moving particle source — travels through Slit 1 and continues
            # Wake is generated as particle approaches and traverses the wall.
            # Source tapers off past the wall (wake already launched).
            px = int(self.source_x_start + t * self.particle_speed)
            if 0 < px < self.wall_x + 40:
                # Taper amplitude after passing through wall
                if px > self.wall_x:
                    taper = max(0, 1.0 - (px - self.wall_x) / 40.0)
                else:
                    taper = 1.0
                amp = np.sin(2 * np.pi * self.freq * t) * 3.0 * taper
                P[px, self.source_y] += amp
                # Small lateral spread to make wake visible
                for dy in [-2, -1, 1, 2]:
                    if 0 <= self.source_y + dy < self.NY:
                        P[px, self.source_y + dy] += amp * 0.3

            if t > integrate_start:
                self.intensity += P**2

            # Save snapshots — store ENERGY DENSITY |P|² for visible heatmap
            if t % snapshot_interval == 0 and t > 200:
                self.snapshots.append((P**2).copy())
                self.snapshot_times.append(t)

        self.intensity /= np.max(self.intensity) + 1e-30
        return self.snapshots, self.intensity


def main():
    print("=" * 70)
    print("  Double Slit: Dark Wake Visualization")
    print("  Showing instantaneous pressure field (not time-averaged)")
    print("=" * 70)

    steps = 2200

    # Run without observer
    print("\n  Simulating (no observer)...", flush=True)
    sim_no = DarkWakeSim(nx=800, ny=500, observer_damping=0.0)
    snaps_no, intensity_no = sim_no.run(steps=steps, snapshot_interval=180)
    print(f"  Done. {len(snaps_no)} snapshots captured.")

    # Run with observer
    print("  Simulating (observer at slit 2)...", flush=True)
    sim_obs = DarkWakeSim(nx=800, ny=500, observer_damping=0.85)
    snaps_obs, intensity_obs = sim_obs.run(steps=steps, snapshot_interval=180)
    print(f"  Done. {len(snaps_obs)} snapshots captured.")

    # ─────────────────────────────────────────────────
    # FIGURE 1: Instantaneous wave field snapshots (3 time steps)
    # ─────────────────────────────────────────────────
    # Pick 3 snapshots: early (wake forming), mid (hitting wall), late (interference)
    n_snaps = len(snaps_no)
    picks = [1, n_snaps // 2, n_snaps - 1]

    fig = plt.figure(figsize=(22, 14))
    fig.patch.set_facecolor("#050510")
    gs = GridSpec(2, 3, figure=fig, hspace=0.22, wspace=0.15)

    time_labels = ["Wake Expanding", "Wake Hitting Slits", "Interference Forming"]

    for col, pi in enumerate(picks):
        if pi >= len(snaps_no):
            pi = len(snaps_no) - 1

        snap = snaps_no[pi]
        t_val = sim_no.snapshot_times[pi]

        # Determine color range for heatmap
        vmax = np.percentile(snap, 99.5)
        if vmax < 1e-10:
            vmax = 1e-3

        # Top row: no observer — energy density heatmap
        ax = fig.add_subplot(gs[0, col])
        ax.set_facecolor("#050510")
        im = ax.imshow(
            snap.T,
            cmap="hot",
            origin="lower",
            extent=[0, sim_no.NX, 0, sim_no.NY],
            vmin=0,
            vmax=vmax,
            aspect="auto",
        )

        # Wall overlay
        wall_vis = np.ma.masked_where(~sim_no.wall, np.ones_like(snap))
        ax.imshow(
            wall_vis.T,
            cmap="Greys",
            alpha=0.95,
            origin="lower",
            extent=[0, sim_no.NX, 0, sim_no.NY],
            aspect="auto",
        )

        # Particle position
        px = int(sim_no.source_x_start + t_val * sim_no.particle_speed)
        if px < sim_no.wall_x:
            ax.plot(
                px,
                sim_no.source_y,
                "o",
                color="#00ff00",
                markersize=10,
                markeredgecolor="white",
                markeredgewidth=1.5,
                zorder=10,
            )
            ax.annotate(
                "PARTICLE",
                xy=(px, sim_no.source_y),
                xytext=(px, sim_no.source_y + 50),
                fontsize=8,
                color="#00ff00",
                fontweight="bold",
                ha="center",
                arrowprops=dict(arrowstyle="->", color="#00ff00", lw=1.5),
            )

        ax.set_title(
            f"No Observer: {time_labels[col]}\n(t = {t_val})",
            color="white",
            fontsize=11,
            fontweight="bold",
        )
        if col == 0:
            ax.set_ylabel("Transverse (nodes)", color="white", fontsize=10)
        ax.tick_params(colors="white", labelsize=8)
        for s in ax.spines.values():
            s.set_color("#333")

        # Bottom row: with observer
        if pi < len(snaps_obs):
            snap_o = snaps_obs[pi]
            t_val_o = sim_obs.snapshot_times[pi]
        else:
            snap_o = snaps_obs[-1]
            t_val_o = sim_obs.snapshot_times[-1]

        vmax_o = np.percentile(snap_o, 99.5)
        if vmax_o < 1e-10:
            vmax_o = 1e-3

        ax2 = fig.add_subplot(gs[1, col])
        ax2.set_facecolor("#050510")
        ax2.imshow(
            snap_o.T,
            cmap="hot",
            origin="lower",
            extent=[0, sim_obs.NX, 0, sim_obs.NY],
            vmin=0,
            vmax=vmax_o,
            aspect="auto",
        )

        wall_vis2 = np.ma.masked_where(~sim_obs.wall, np.ones_like(snap_o))
        ax2.imshow(
            wall_vis2.T,
            cmap="Greys",
            alpha=0.95,
            origin="lower",
            extent=[0, sim_obs.NX, 0, sim_obs.NY],
            aspect="auto",
        )

        # Observer marker
        ax2.plot(
            sim_obs.wall_x,
            sim_obs.slit_2,
            "s",
            color="#00ff00",
            markersize=10,
            markeredgecolor="yellow",
            markeredgewidth=2,
            zorder=10,
        )

        # Particle
        px_o = int(sim_obs.source_x_start + t_val_o * sim_obs.particle_speed)
        if px_o < sim_obs.wall_x:
            ax2.plot(
                px_o,
                sim_obs.source_y,
                "o",
                color="#00ff00",
                markersize=10,
                markeredgecolor="white",
                markeredgewidth=1.5,
                zorder=10,
            )

        ax2.set_title(
            f"Observer at Slit 2: {time_labels[col]}\n(t = {t_val_o})",
            color="white",
            fontsize=11,
            fontweight="bold",
        )
        ax2.set_xlabel("Propagation (nodes)", color="white", fontsize=10)
        if col == 0:
            ax2.set_ylabel("Transverse (nodes)", color="white", fontsize=10)
        ax2.tick_params(colors="white", labelsize=8)
        for s in ax2.spines.values():
            s.set_color("#333")

    # Annotations
    fig.text(
        0.01,
        0.75,
        "NO\nOBSERVER",
        rotation=90,
        color="#00ffcc",
        fontsize=16,
        fontweight="bold",
        ha="left",
        va="center",
    )
    fig.text(
        0.01,
        0.28,
        "OBSERVER\nAT SLIT 2",
        rotation=90,
        color="#ff6b6b",
        fontsize=16,
        fontweight="bold",
        ha="left",
        va="center",
    )

    fig.suptitle(
        "AVE Double Slit: The Dark Wake of a Soliton Propagating Through the Vacuum Lattice",
        color="white",
        fontsize=17,
        fontweight="bold",
        y=0.99,
    )

    # Colorbar
    cbar = fig.colorbar(im, ax=fig.axes, orientation="horizontal", fraction=0.02, pad=0.06, aspect=50)
    cbar.set_label("Wave Energy Density |P|² — Bright = High Wake Energy", color="white", fontsize=11)
    cbar.ax.tick_params(colors="white")

    out = os.path.join(OUT_DIR, "double_slit_dark_wake.png")
    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"\n  📊 Dark wake visualization: {out}")

    # ─────────────────────────────────────────────────
    # FIGURE 2: Single high-res snapshot at peak interference
    # ─────────────────────────────────────────────────
    fig2 = plt.figure(figsize=(16, 9))
    fig2.patch.set_facecolor("#050510")
    ax_big = fig2.add_subplot(111)
    ax_big.set_facecolor("#050510")

    # Use the last snapshot (maximum interference) — already energy density
    snap_final = snaps_no[-1]
    vmax_f = np.percentile(snap_final, 99.8)

    ax_big.imshow(
        snap_final.T,
        cmap="hot",
        origin="lower",
        extent=[0, sim_no.NX, 0, sim_no.NY],
        vmin=0,
        vmax=vmax_f,
        aspect="auto",
        interpolation="bilinear",
    )

    # Wall
    wall_big = np.ma.masked_where(~sim_no.wall, np.ones_like(snap_final) * vmax_f)
    ax_big.imshow(
        wall_big.T,
        cmap="Greys",
        alpha=0.9,
        origin="lower",
        extent=[0, sim_no.NX, 0, sim_no.NY],
        aspect="auto",
    )

    # Slit labels
    ax_big.annotate(
        "SLIT 1",
        xy=(sim_no.wall_x + 8, sim_no.slit_1),
        fontsize=12,
        color="white",
        fontweight="bold",
    )
    ax_big.annotate(
        "SLIT 2",
        xy=(sim_no.wall_x + 8, sim_no.slit_2),
        fontsize=12,
        color="white",
        fontweight="bold",
    )

    # Wake annotation
    props = dict(boxstyle="round", facecolor="#111122", alpha=0.9, edgecolor="#ff6666")
    ax_big.text(
        0.02,
        0.95,
        "BRIGHT = high wave energy density\n"
        "The PARTICLE passes through SLIT 1\n"
        "The radial WAKE reaches BOTH slits\n"
        "and creates interference fringes\n"
        "on the far side of the barrier",
        transform=ax_big.transAxes,
        fontsize=11,
        color="white",
        verticalalignment="top",
        bbox=props,
    )

    ax_big.set_title(
        "Particle Through Slit 1: Wake Energy Density Heatmap",
        color="white",
        fontsize=16,
        fontweight="bold",
        pad=12,
    )
    ax_big.set_xlabel("Propagation Axis (nodes)", color="white", fontsize=13)
    ax_big.set_ylabel("Transverse Axis (nodes)", color="white", fontsize=13)
    ax_big.tick_params(colors="white")
    for s in ax_big.spines.values():
        s.set_color("#333")

    out2 = os.path.join(OUT_DIR, "double_slit_dark_wake_hires.png")
    fig2.savefig(out2, dpi=250, bbox_inches="tight", facecolor=fig2.get_facecolor())
    plt.close(fig2)
    print(f"  📊 High-res dark wake: {out2}")


if __name__ == "__main__":
    main()

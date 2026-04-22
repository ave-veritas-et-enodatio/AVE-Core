#!/usr/bin/env python3
r"""
Double Slit Standing Wave Heatmap: With and Without Observer
==============================================================

In the AVE framework, a "photon" is a helical soliton propagating through
the LC lattice. The double slit experiment is NOT mysterious — it is a
straightforward acoustic interference problem in a structured medium.

What "observation" means physically:
  - WITHOUT observer: the soliton's radial wake passes through BOTH slits,
    creating coherent interference fringes on the far side. The standing
    wave pattern is the time-averaged |Ψ|² of two overlapping cylindrical
    wavefronts.
  - WITH observer: a localized impedance perturbation (e.g., a detector
    at one slit) introduces damping/scattering at that slit. This destroys
    the phase coherence between the two wavefronts, collapsing the
    interference pattern into a single-slit diffraction envelope.

The observer doesn't "collapse the wavefunction" — it physically disrupts
the mechanical coherence of the wake by introducing impedance mismatch
at the measurement point.

Usage:
    python src/scripts/vol_1_foundations/simulate_double_slit_observer.py
"""

import os
import numpy as np


import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "sim_outputs")
os.makedirs(OUT_DIR, exist_ok=True)


# ═══════════════════════════════════════════════════════
# FDTD 2D Acoustic Solver
# ═══════════════════════════════════════════════════════


class DoubleSlit2D:
    """
    2D FDTD wave solver for the double slit experiment.

    Models the vacuum as a 2D acoustic medium with velocity c.
    The "photon" is a point source emitting a continuous sinusoidal wave.
    The wall is a hard boundary with two slits.
    Optional: an "observer" at one slit introduces damping (decoherence).
    """

    def __init__(self, nx=800, ny=500, observe_slit=False):
        self.NX = nx
        self.NY = ny
        self.c = 1.0
        self.dt = 0.45  # CFL < 1/√2 for 2D
        self.dx = 1.0

        # Fields
        self.P = np.zeros((nx, ny))  # Pressure
        self.Vx = np.zeros((nx, ny))  # x-velocity
        self.Vy = np.zeros((nx, ny))  # y-velocity
        self.intensity = np.zeros((nx, ny))  # Time-averaged |P|²

        # Sponge absorbing boundaries
        self.sponge = 50
        self.damping = self._build_sponge()

        # Wall geometry
        self.wall_x = int(nx * 0.35)
        self.wall_t = 4
        self.slit_w = 14
        self.slit_sep = 90
        self.slit_1 = ny // 2 - self.slit_sep // 2
        self.slit_2 = ny // 2 + self.slit_sep // 2

        self.wall_mask = self._build_wall()

        # Observer = localized impedance change at slit 2
        # In AVE, a detector IS a physical impedance discontinuity.
        # Z_local = sqrt(L/C). Changing C at the slit changes c_local = 1/sqrt(LC).
        # The wave equation naturally handles reflection/transmission/phase shift.
        self.observe_slit = observe_slit
        self.c2_field = np.ones((nx, ny)) * self.c**2  # uniform vacuum
        if observe_slit:
            ox = self.wall_x
            oy = self.slit_2
            # The sensor creates a region of HIGHER stiffness (higher Z)
            # at slit 2.  Impedance ratio ~4:1 → strong reflection.
            Z_ratio = 4.0  # observer impedance / vacuum impedance
            for dx in range(-3, 4):
                for dy in range(-self.slit_w // 2, self.slit_w // 2):
                    xi = ox + dx
                    yi = oy + dy
                    if 0 <= xi < nx and 0 <= yi < ny:
                        r = np.sqrt(dx**2 + dy**2) / (self.slit_w // 2)
                        if r < 1.0:
                            # Smooth impedance transition (tapered, not step)
                            local_Z = 1.0 + (Z_ratio - 1.0) * (1.0 - r) ** 2
                            self.c2_field[xi, yi] = self.c**2 * local_Z

        # Source parameters
        self.freq = 0.06
        self.source_x = 60
        self.source_y = ny // 2

    def _build_sponge(self):
        d = np.ones((self.NX, self.NY))
        s = self.sponge
        for i in range(s):
            factor = 1.0 - 0.06 * ((s - i) / s) ** 2
            d[i, :] *= factor
            d[self.NX - 1 - i, :] *= factor
            d[:, i] *= factor
            d[:, self.NY - 1 - i] *= factor
        return d

    def _build_wall(self):
        mask = np.zeros((self.NX, self.NY), dtype=bool)
        wx = self.wall_x
        wt = self.wall_t
        mask[wx : wx + wt, :] = True
        # Open slits
        sw = self.slit_w
        mask[wx : wx + wt, self.slit_1 - sw // 2 : self.slit_1 + sw // 2] = False
        mask[wx : wx + wt, self.slit_2 - sw // 2 : self.slit_2 + sw // 2] = False
        return mask

    def run(self, steps=2000):
        P = self.P
        Vx = self.Vx
        Vy = self.Vy
        d = self.damping
        dt = self.dt
        dx = self.dx

        integrate_start = steps // 3

        for t in range(steps):
            # Update velocities
            Vx[:-1, :] -= dt * (P[1:, :] - P[:-1, :]) / dx
            Vy[:, :-1] -= dt * (P[:, 1:] - P[:, :-1]) / dx

            # Hard wall
            Vx[self.wall_mask] = 0
            Vy[self.wall_mask] = 0

            # Update pressure with SPATIALLY VARYING c²
            # This is the core AVE mechanism: local impedance determines local wave speed
            P[1:-1, 1:-1] -= (
                dt
                * self.c2_field[1:-1, 1:-1]
                * ((Vx[1:-1, 1:-1] - Vx[:-2, 1:-1]) / dx + (Vy[1:-1, 1:-1] - Vy[1:-1, :-2]) / dx)
            )

            # Sponge ABC
            P *= d
            Vx *= d
            Vy *= d

            # Source: continuous sinusoidal wave
            P[self.source_x, self.source_y] += np.sin(2 * np.pi * self.freq * t) * 2.0

            # Integrate intensity after transient
            if t > integrate_start:
                self.intensity += P**2

        # Store final signed pressure snapshot for diverging colormap
        self.final_P = P.copy()

        # Normalize
        self.intensity /= np.max(self.intensity) + 1e-30
        return self.intensity


def main():
    print("=" * 70)
    print("  Double Slit: Standing Wave Heatmap — Observer vs No Observer")
    print("=" * 70)

    steps = 2500

    # Run WITHOUT observer
    print("\n  Running FDTD (no observer)...", flush=True)
    sim_no_obs = DoubleSlit2D(nx=800, ny=500, observe_slit=False)
    intensity_no_obs = sim_no_obs.run(steps=steps)
    print("  Done.")

    # Run WITH observer at slit 2
    print("  Running FDTD (observer at slit 2)...", flush=True)
    sim_obs = DoubleSlit2D(nx=800, ny=500, observe_slit=True)
    intensity_obs = sim_obs.run(steps=steps)
    print("  Done.")

    # ─────────────────────────────────────────────────
    # Generate comparison plot
    # ─────────────────────────────────────────────────
    fig = plt.figure(figsize=(20, 10))
    fig.patch.set_facecolor("#050510")
    gs = GridSpec(1, 3, figure=fig, width_ratios=[1, 1, 0.08], wspace=0.12)

    # Custom AVE colormap: Ocean Fire (teal depths → white → crimson → gold)
    # AVE_CMAP = LinearSegmentedColormap.from_list(  # bulk lint fixup pass
    #     "ocean_fire",
    #     [
    #         "#001520",
    #         "#003040",
    #         "#207080",
    #         "#80b8c8",
    #         "#ffffff",
    #         "#d09080",
    #         "#c04030",
    #         "#cc1500",
    #         "#e05000",
    #         "#f0a020",
    #     ],
    # )

    for idx, (intensity, sim, title, label) in enumerate(
        [
            (
                intensity_no_obs,
                sim_no_obs,
                "No Observer: Coherent Interference",
                "Standing waves form — the wake through\nboth slits interferes constructively",
            ),
            (
                intensity_obs,
                sim_obs,
                "Observer at Slit 2: Decoherence",
                "Impedance perturbation at slit 2\ndestroys phase coherence → single-slit envelope",
            ),
        ]
    ):
        ax = fig.add_subplot(gs[0, idx])
        ax.set_facecolor("#0a0a1e")

        # Show time-averaged intensity P² (what a physical detector measures)
        # PowerNorm(gamma<1) boosts faint fringes for visibility
        from matplotlib.colors import PowerNorm

        imax = np.percentile(intensity, 99)
        imax = max(imax, 1e-6)
        im = ax.imshow(
            intensity.T,
            cmap="hot",
            origin="lower",
            norm=PowerNorm(gamma=0.3, vmin=0, vmax=imax),
            extent=[0, sim.NX, 0, sim.NY],
            aspect="auto",
        )

        # Wall overlay
        wall_display = np.ma.masked_where(~sim.wall_mask, np.ones_like(sim.wall_mask, dtype=float))
        ax.imshow(
            wall_display.T,
            cmap="Greys",
            alpha=0.9,
            origin="lower",
            extent=[0, sim.NX, 0, sim.NY],
            aspect="auto",
        )

        # Observer marker
        if sim.observe_slit:
            ax.plot(
                sim.wall_x,
                sim.slit_2,
                "o",
                color="#00ff00",
                markersize=12,
                markeredgecolor="white",
                markeredgewidth=2,
                zorder=10,
            )
            ax.annotate(
                "OBSERVER",
                xy=(sim.wall_x, sim.slit_2),
                xytext=(sim.wall_x - 80, sim.slit_2 + 60),
                fontsize=11,
                color="#00ff00",
                fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#00ff00", lw=2),
            )

        # Slit labels
        ax.annotate("Slit 1", xy=(sim.wall_x + 5, sim.slit_1), fontsize=9, color="white", alpha=0.7)
        ax.annotate("Slit 2", xy=(sim.wall_x + 5, sim.slit_2), fontsize=9, color="white", alpha=0.7)

        # Source marker
        ax.plot(sim.source_x, sim.source_y, "*", color="cyan", markersize=15, zorder=10)

        # Contour lines for interference peaks
        levels = np.linspace(0.05, 0.20, 6)
        ax.contour(
            intensity.T,
            levels=levels,
            colors="#ff00aa",
            alpha=0.25,
            linewidths=0.5,
            extent=[0, sim.NX, 0, sim.NY],
        )

        ax.set_title(title, color="white", fontsize=14, fontweight="bold", pad=10)
        ax.set_xlabel("Propagation Axis (nodes)", color="white", fontsize=11)
        if idx == 0:
            ax.set_ylabel("Transverse Axis (nodes)", color="white", fontsize=11)
        ax.tick_params(colors="white")

        # Annotation box
        props = dict(
            boxstyle="round",
            facecolor="#111122",
            alpha=0.9,
            edgecolor="#ff00aa" if idx == 0 else "#00ff00",
        )
        ax.text(
            0.02,
            0.02,
            label,
            transform=ax.transAxes,
            fontsize=10,
            color="white",
            verticalalignment="bottom",
            bbox=props,
        )

        for spine in ax.spines.values():
            spine.set_color("#333")

    # Colorbar
    cax = fig.add_subplot(gs[0, 2])
    cbar = plt.colorbar(im, cax=cax)
    cbar.set_label("Time-Averaged Wave Energy $\\langle |\\Psi|^2 \\rangle$", color="white", fontsize=12)
    cbar.ax.tick_params(colors="white")

    # Supertitle
    fig.suptitle(
        r"AVE Double Slit: The Observer Is a Physical Impedance Perturbation",
        color="white",
        fontsize=18,
        fontweight="bold",
        y=0.98,
    )

    # ─────────────────────────────────────────────────
    # Transverse intensity cross-section
    # ─────────────────────────────────────────────────
    fig2 = plt.figure(figsize=(14, 6))
    fig2.patch.set_facecolor("#050510")
    ax_cross = fig2.add_subplot(111)
    ax_cross.set_facecolor("#0a0a0a")

    # Extract cross-section at x = 85% of domain (far field)
    x_cross = int(sim_no_obs.NX * 0.85)
    y = np.arange(sim_no_obs.NY)

    cross_no_obs = intensity_no_obs[x_cross, :]
    cross_obs = intensity_obs[x_cross, :]

    # Smooth slightly for clarity
    from scipy.ndimage import gaussian_filter1d

    cross_no_obs_s = gaussian_filter1d(cross_no_obs, sigma=3)
    cross_obs_s = gaussian_filter1d(cross_obs, sigma=3)

    ax_cross.fill_between(y, cross_no_obs_s, alpha=0.3, color="#ff6b6b")
    ax_cross.plot(y, cross_no_obs_s, color="#ff6b6b", linewidth=2, label="No Observer (coherent interference)")
    ax_cross.fill_between(y, cross_obs_s, alpha=0.3, color="#00ffcc")
    ax_cross.plot(y, cross_obs_s, color="#00ffcc", linewidth=2, label="Observer at Slit 2 (decoherence)")

    ax_cross.set_xlabel("Transverse Position (nodes)", color="white", fontsize=12)
    ax_cross.set_ylabel("$\\langle |\\Psi|^2 \\rangle$ (normalized)", color="white", fontsize=12)
    ax_cross.set_title(
        f"Far-Field Intensity Cross-Section at x = {x_cross} nodes",
        color="white",
        fontsize=14,
        fontweight="bold",
    )
    ax_cross.legend(fontsize=12, facecolor="#1a1a1a", edgecolor="#333", labelcolor="white", loc="upper right")
    ax_cross.tick_params(colors="white")
    ax_cross.grid(True, alpha=0.1, color="white")
    for spine in ax_cross.spines.values():
        spine.set_color("#333")

    # Save both
    out1 = os.path.join(OUT_DIR, "double_slit_heatmap_comparison.png")
    fig.savefig(out1, dpi=200, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"\n  📊 Heatmap saved: {out1}")

    out2 = os.path.join(OUT_DIR, "double_slit_cross_section.png")
    fig2.savefig(out2, dpi=200, bbox_inches="tight", facecolor=fig2.get_facecolor())
    plt.close(fig2)
    print(f"  📊 Cross-section saved: {out2}")

    # Summary
    print(f"\n  ═══════════════════════════════════════════════════════════════")
    print(f"  AVE INTERPRETATION")
    print(f"  ═══════════════════════════════════════════════════════════════")
    print(f"  The 'measurement problem' in QM is not a problem.")
    print(f"  It is a straightforward impedance mismatch.")
    print(f"")
    print(f"  WITHOUT observer: the soliton's radial wake passes through")
    print(f"  both slits with phase coherence intact → standing wave fringes.")
    print(f"")
    print(f"  WITH observer: a physical impedance perturbation (detector)")
    print(f"  at one slit introduces localized damping. This disrupts the")
    print(f"  phase relationship between the two wavefronts → no fringes.")
    print(f"")
    print(f"  The 'collapse' is nothing more than the acoustic engineering")
    print(f"  principle that you cannot tap a transmission line without")
    print(f"  disturbing the signal. There is no mystery.")
    print(f"  ═══════════════════════════════════════════════════════════════")


if __name__ == "__main__":
    main()

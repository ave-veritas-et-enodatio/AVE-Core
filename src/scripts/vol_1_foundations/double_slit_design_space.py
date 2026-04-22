#!/usr/bin/env python3
r"""
Double Slit Design Space Explorer
===================================

Sweeps the key parameters of the double slit experiment to map
the complete design space, thinking like an EE.

AVE physics: the PARTICLE passes through one slit while its transverse
WAKE reaches all slits.  The source is aimed at the first slit.

Panel 1: Frequency sweep (wake wavelength → fringe spacing)
Panel 2: Slit spacing sweep (aperture separation → fringe density)
Panel 3: N-slit grating (2, 3, 5, 8 slits → peak sharpening)
Panel 4: Observer impedance sweep (0% → 100% damping → continuous decoherence)

The observer impedance sweep is the KEY AVE prediction:
  - Copenhagen says collapse is binary (observed or not)
  - AVE says decoherence is continuous (proportional to impedance perturbation)
  - This is a testable, falsifiable distinction

Usage:
    python src/scripts/vol_1_foundations/double_slit_design_space.py
"""

import os

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.ndimage import gaussian_filter1d

# JAX GPU acceleration (graceful fallback to numpy)
try:
    import jax
    import jax.numpy as jnp
    from jax import jit

    jax.config.update("jax_enable_x64", True)
    _HAS_JAX = True
except ImportError:
    _HAS_JAX = False

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "assets", "sim_outputs")
os.makedirs(OUT_DIR, exist_ok=True)


def run_fdtd_slit(
    nx=600,
    ny=400,
    steps=1800,
    freq=0.06,
    slit_sep=90,
    slit_width=14,
    n_slits=2,
    observer_damping=0.0,
    wall_frac=0.35,
):
    """
    Run a 2D FDTD double/N-slit simulation and return the
    far-field transverse intensity cross-section.
    """
    c = 1.0
    dt = 0.45
    dx = 1.0

    P = np.zeros((nx, ny))
    Vx = np.zeros((nx, ny))
    Vy = np.zeros((nx, ny))

    # Sponge ABC
    sponge = 40
    damping = np.ones((nx, ny))
    for i in range(sponge):
        f = 1.0 - 0.06 * ((sponge - i) / sponge) ** 2
        damping[i, :] *= f
        damping[nx - 1 - i, :] *= f
        damping[:, i] *= f
        damping[:, ny - 1 - i] *= f

    # Wall + slits
    wall_x = int(nx * wall_frac)
    wall_t = 4
    wall = np.zeros((nx, ny), dtype=bool)
    wall[wall_x : wall_x + wall_t, :] = True

    # Compute slit positions (centered)
    slit_positions = []
    center = ny // 2
    if n_slits == 1:
        slit_positions = [center]
    else:
        total_span = slit_sep * (n_slits - 1)
        for i in range(n_slits):
            slit_positions.append(center - total_span // 2 + i * slit_sep)

    for sy in slit_positions:
        wall[wall_x : wall_x + wall_t, max(0, sy - slit_width // 2) : min(ny, sy + slit_width // 2)] = False

    # Observer mask (damping at last slit)
    obs_mask = np.zeros((nx, ny))
    if observer_damping > 0 and n_slits >= 2:
        last_slit_y = slit_positions[-1]
        for dxi in range(-3, 4):
            for dyi in range(-slit_width, slit_width):
                xi = wall_x + dxi
                yi = last_slit_y + dyi
                if 0 <= xi < nx and 0 <= yi < ny:
                    r = np.sqrt(dxi**2 + (dyi / slit_width * 3) ** 2) / 3
                    obs_mask[xi, yi] = observer_damping * max(0, 1 - r)

    # Source — particle aimed at the first slit (AVE: particle through ONE slit)
    source_x_start = 50
    source_y = slit_positions[0]  # Aimed at first slit
    particle_speed = 0.22  # nodes per timestep

    integrate_start = steps // 3
    intensity = np.zeros((nx, ny))

    c2 = c**2

    if _HAS_JAX:
        # JAX-accelerated path
        P_j = jnp.array(P)
        Vx_j = jnp.array(Vx)
        Vy_j = jnp.array(Vy)
        damping_j = jnp.array(damping)
        wall_j = jnp.array(wall)
        obs_mask_j = jnp.array(obs_mask)
        intensity_j = jnp.zeros((nx, ny))

        @jit
        def _step(P, Vx, Vy, intensity, src_amp, source_x, do_integrate):
            Vx = Vx.at[:-1, :].add(-dt * (P[1:, :] - P[:-1, :]) / dx)
            Vy = Vy.at[:, :-1].add(-dt * (P[:, 1:] - P[:, :-1]) / dx)
            Vx = jnp.where(wall_j, 0.0, Vx)
            Vy = jnp.where(wall_j, 0.0, Vy)
            P = P.at[1:-1, 1:-1].add(
                -dt * c2 * ((Vx[1:-1, 1:-1] - Vx[:-2, 1:-1]) / dx + (Vy[1:-1, 1:-1] - Vy[1:-1, :-2]) / dx)
            )
            P = P * damping_j
            Vx = Vx * damping_j
            Vy = Vy * damping_j
            P = P * (1.0 - obs_mask_j)
            # Moving particle source with taper past wall
            in_range = (source_x > 0) & (source_x < wall_x + 40)
            taper = jnp.clip(1.0 - (source_x - wall_x) / 40.0, 0.0, 1.0)
            amp = src_amp * in_range * taper
            P = P.at[source_x, source_y].add(amp)
            P = P.at[source_x, jnp.clip(source_y - 1, 0, ny - 1)].add(amp * 0.3)
            P = P.at[source_x, jnp.clip(source_y + 1, 0, ny - 1)].add(amp * 0.3)
            intensity = intensity + do_integrate * P**2
            return P, Vx, Vy, intensity

        for t in range(steps):
            src_amp = np.sin(2 * np.pi * freq * t) * 2.0
            source_x = jnp.int32(source_x_start + t * particle_speed)
            do_integrate = 1.0 if t > integrate_start else 0.0
            P_j, Vx_j, Vy_j, intensity_j = _step(P_j, Vx_j, Vy_j, intensity_j, src_amp, source_x, do_integrate)

        intensity = np.array(intensity_j)
    else:
        # Numpy fallback path
        for t in range(steps):
            Vx[:-1, :] -= dt * (P[1:, :] - P[:-1, :]) / dx
            Vy[:, :-1] -= dt * (P[:, 1:] - P[:, :-1]) / dx
            Vx[wall] = 0
            Vy[wall] = 0

            P[1:-1, 1:-1] -= dt * c2 * ((Vx[1:-1, 1:-1] - Vx[:-2, 1:-1]) / dx + (Vy[1:-1, 1:-1] - Vy[1:-1, :-2]) / dx)
            P *= damping
            Vx *= damping
            Vy *= damping

            if observer_damping > 0:
                P *= 1.0 - obs_mask

            # Moving particle source with taper past wall
            px = int(source_x_start + t * particle_speed)
            if 0 < px < wall_x + 40:
                taper = max(0.0, 1.0 - (px - wall_x) / 40.0) if px > wall_x else 1.0
                amp = np.sin(2 * np.pi * freq * t) * 2.0 * taper
                P[px, source_y] += amp
                if source_y - 1 >= 0:
                    P[px, source_y - 1] += amp * 0.3
                if source_y + 1 < ny:
                    P[px, source_y + 1] += amp * 0.3

            if t > integrate_start:
                intensity += P**2

    # Extract far-field cross-section
    x_cross = int(nx * 0.82)
    cross = intensity[x_cross, :]
    cross = cross / (np.max(cross) + 1e-30)
    return gaussian_filter1d(cross, sigma=2), intensity


def main():
    print("=" * 70)
    print("  Double Slit Design Space Explorer")
    print("  Thinking Like an EE: Mapping the Parameter Space")
    print("=" * 70)

    fig = plt.figure(figsize=(22, 14))
    fig.patch.set_facecolor("#050510")
    gs = GridSpec(2, 2, figure=fig, hspace=0.30, wspace=0.25)

    ny = 400
    y = np.arange(ny)

    # ═══════════════════════════════════════════════════
    # PANEL 1: Frequency Sweep (wavelength → fringe spacing)
    # ═══════════════════════════════════════════════════
    print("\n  Panel 1: Frequency sweep...", flush=True)
    ax1 = fig.add_subplot(gs[0, 0])
    ax1.set_facecolor("#0a0a0a")

    freqs = [0.03, 0.06, 0.10, 0.15]
    colors1 = ["#6bcaff", "#00ffcc", "#ffd93d", "#ff6b6b"]
    for i, freq in enumerate(freqs):
        print(f"    f = {freq}...", flush=True)
        cross, _ = run_fdtd_slit(freq=freq, steps=1500)
        ax1.plot(y, cross + i * 0.15, color=colors1[i], linewidth=1.5, label=f"f = {freq}", alpha=0.9)
        ax1.fill_between(y, i * 0.15, cross + i * 0.15, alpha=0.15, color=colors1[i])

    ax1.set_title("Frequency Sweep: Wake λ → Fringe Spacing", color="white", fontsize=13, fontweight="bold")
    ax1.set_xlabel("Transverse Position", color="white")
    ax1.set_ylabel("Intensity (offset)", color="white")
    ax1.legend(fontsize=9, facecolor="#1a1a1a", edgecolor="#333", labelcolor="white", loc="upper right")
    ax1.tick_params(colors="white")
    ax1.grid(True, alpha=0.1, color="white")
    for s in ax1.spines.values():
        s.set_color("#333")

    # ═══════════════════════════════════════════════════
    # PANEL 2: Slit Spacing Sweep
    # ═══════════════════════════════════════════════════
    print("\n  Panel 2: Slit spacing sweep...", flush=True)
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.set_facecolor("#0a0a0a")

    spacings = [40, 70, 100, 140]
    colors2 = ["#ff6b6b", "#ffd93d", "#00ffcc", "#6bcaff"]
    for i, sep in enumerate(spacings):
        print(f"    d = {sep}...", flush=True)
        cross, _ = run_fdtd_slit(slit_sep=sep, steps=1500)
        ax2.plot(
            y,
            cross + i * 0.15,
            color=colors2[i],
            linewidth=1.5,
            label=f"d = {sep} nodes",
            alpha=0.9,
        )
        ax2.fill_between(y, i * 0.15, cross + i * 0.15, alpha=0.15, color=colors2[i])

    ax2.set_title(
        "Slit Spacing Sweep: Aperture d → Fringe Density",
        color="white",
        fontsize=13,
        fontweight="bold",
    )
    ax2.set_xlabel("Transverse Position", color="white")
    ax2.set_ylabel("Intensity (offset)", color="white")
    ax2.legend(fontsize=9, facecolor="#1a1a1a", edgecolor="#333", labelcolor="white", loc="upper right")
    ax2.tick_params(colors="white")
    ax2.grid(True, alpha=0.1, color="white")
    for s in ax2.spines.values():
        s.set_color("#333")

    # ═══════════════════════════════════════════════════
    # PANEL 3: N-Slit Grating (diffraction order sharpening)
    # ═══════════════════════════════════════════════════
    print("\n  Panel 3: N-slit grating...", flush=True)
    ax3 = fig.add_subplot(gs[1, 0])
    ax3.set_facecolor("#0a0a0a")

    n_slits_list = [1, 2, 3, 5]
    colors3 = ["#ff6b6b", "#ffd93d", "#00ffcc", "#6bcaff"]
    for i, ns in enumerate(n_slits_list):
        print(f"    N = {ns}...", flush=True)
        cross, _ = run_fdtd_slit(n_slits=ns, slit_sep=60, steps=1500)
        ax3.plot(
            y,
            cross + i * 0.15,
            color=colors3[i],
            linewidth=1.5,
            label=f'N = {ns} slit{"s" if ns > 1 else ""}',
            alpha=0.9,
        )
        ax3.fill_between(y, i * 0.15, cross + i * 0.15, alpha=0.15, color=colors3[i])

    ax3.set_title("N-Slit Grating: Peak Sharpening with N", color="white", fontsize=13, fontweight="bold")
    ax3.set_xlabel("Transverse Position", color="white")
    ax3.set_ylabel("Intensity (offset)", color="white")
    ax3.legend(fontsize=9, facecolor="#1a1a1a", edgecolor="#333", labelcolor="white", loc="upper right")
    ax3.tick_params(colors="white")
    ax3.grid(True, alpha=0.1, color="white")
    for s in ax3.spines.values():
        s.set_color("#333")

    # ═══════════════════════════════════════════════════
    # PANEL 4: Observer Impedance Sweep (THE MONEY SHOT)
    # ═══════════════════════════════════════════════════
    print("\n  Panel 4: Observer impedance sweep (continuous decoherence)...", flush=True)
    ax4 = fig.add_subplot(gs[1, 1])
    ax4.set_facecolor("#0a0a0a")

    impedances = [0.0, 0.03, 0.08, 0.15, 0.30]
    colors4 = ["#ff6b6b", "#ff9933", "#ffd93d", "#66cc66", "#00ffcc"]
    labels4 = [
        "0% (no observer)",
        "3% (weak probe)",
        "8% (moderate)",
        "15% (strong)",
        "30% (destructive)",
    ]

    for i, (z_obs, label) in enumerate(zip(impedances, labels4)):
        print(f"    Z_obs = {z_obs*100:.0f}%...", flush=True)
        cross, _ = run_fdtd_slit(observer_damping=z_obs, steps=1500)
        ax4.plot(y, cross + i * 0.12, color=colors4[i], linewidth=1.5, label=label, alpha=0.9)
        ax4.fill_between(y, i * 0.12, cross + i * 0.12, alpha=0.15, color=colors4[i])

    ax4.set_title(
        "Observer Impedance Sweep: Continuous Decoherence",
        color="white",
        fontsize=13,
        fontweight="bold",
    )
    ax4.set_xlabel("Transverse Position", color="white")
    ax4.set_ylabel("Intensity (offset)", color="white")
    ax4.legend(fontsize=9, facecolor="#1a1a1a", edgecolor="#333", labelcolor="white", loc="upper right")
    ax4.tick_params(colors="white")
    ax4.grid(True, alpha=0.1, color="white")
    for s in ax4.spines.values():
        s.set_color("#333")

    # Annotation on Panel 4
    props = dict(boxstyle="round", facecolor="#111122", alpha=0.9, edgecolor="#00ffcc")
    ax4.text(
        0.02,
        0.98,
        "Copenhagen: binary collapse\n" "AVE: continuous impedance\n" "→ testable distinction",
        transform=ax4.transAxes,
        fontsize=10,
        color="#00ffcc",
        verticalalignment="top",
        bbox=props,
    )

    fig.suptitle(
        "Double Slit Design Space: Thinking Like an EE",
        color="white",
        fontsize=20,
        fontweight="bold",
        y=0.98,
    )

    out = os.path.join(OUT_DIR, "double_slit_design_space.png")
    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)

    print(f"\n  📊 Design space plot saved: {out}")

    # ─────────────────────────────────────────────────
    # Fringe visibility vs observer impedance
    # ─────────────────────────────────────────────────
    print("\n  Generating visibility vs impedance curve...", flush=True)
    fig2 = plt.figure(figsize=(12, 6))
    fig2.patch.set_facecolor("#050510")
    ax_vis = fig2.add_subplot(111)
    ax_vis.set_facecolor("#0a0a0a")

    z_sweep = np.linspace(0, 0.5, 12)
    visibilities = []
    for z_obs in z_sweep:
        print(f"    Z_obs = {z_obs*100:.1f}%...", flush=True)
        cross, _ = run_fdtd_slit(observer_damping=z_obs, steps=1200, nx=500, ny=350)
        # Fringe visibility = (I_max - I_min) / (I_max + I_min) in central region
        center = len(cross) // 2
        region = cross[center - 80 : center + 80]
        if len(region) > 10:
            I_max = np.max(region)
            I_min = np.min(region[region > 0]) if np.any(region > 0) else 0
            vis = (I_max - I_min) / (I_max + I_min + 1e-30)
        else:
            vis = 0
        visibilities.append(vis)

    ax_vis.plot(z_sweep * 100, visibilities, "o-", color="#00ffcc", linewidth=2.5, markersize=8)
    ax_vis.fill_between(z_sweep * 100, visibilities, alpha=0.2, color="#00ffcc")

    # Copenhagen prediction (binary)
    ax_vis.axhline(
        visibilities[0],
        color="#ff6b6b",
        linestyle="--",
        alpha=0.5,
        label="Copenhagen: full fringes or none",
    )
    ax_vis.axhline(0, color="#ff6b6b", linestyle="--", alpha=0.5)

    ax_vis.set_xlabel("Observer Impedance Perturbation (%)", color="white", fontsize=13)
    ax_vis.set_ylabel("Fringe Visibility $\\mathcal{V}$", color="white", fontsize=13)
    ax_vis.set_title(
        "AVE Prediction: Decoherence Is Continuous, Not Binary",
        color="white",
        fontsize=15,
        fontweight="bold",
    )
    ax_vis.legend(fontsize=11, facecolor="#1a1a1a", edgecolor="#333", labelcolor="white")
    ax_vis.tick_params(colors="white")
    ax_vis.grid(True, alpha=0.1, color="white")
    for s in ax_vis.spines.values():
        s.set_color("#333")

    out2 = os.path.join(OUT_DIR, "double_slit_visibility_vs_impedance.png")
    fig2.savefig(out2, dpi=200, bbox_inches="tight", facecolor=fig2.get_facecolor())
    plt.close(fig2)
    print(f"  📊 Visibility curve saved: {out2}")

    print("\n  ═══════════════════════════════════════════════════════════")
    print("  DESIGN SPACE SUMMARY")
    print("  ═══════════════════════════════════════════════════════════")
    print("  Frequency ↑ → fringe spacing ↓ (same as λ = h/p)")
    print("  Slit spacing ↑ → fringe density ↑ (same as d·sin θ = nλ)")
    print("  N slits ↑ → peaks sharpen (grating resolution)")
    print("  Observer Z ↑ → visibility ↓ CONTINUOUSLY (not binary)")
    print("  ═══════════════════════════════════════════════════════════")
    print("  The last point is the falsifiable AVE prediction.")
    print("  An experiment measuring fringe visibility as a function")
    print("  of detector coupling strength at one slit would")
    print("  distinguish AVE from Copenhagen.")
    print("  ═══════════════════════════════════════════════════════════")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
K4-TLM Gravitational Lensing — High-Resolution 2D Simulation
===============================================================

A photon (Gaussian wavepacket) propagates through a 2D K4-TLM lattice
with a gravitational refractive lens: n(r) = 1 + n₀/(1 + (r/r_c)²).

The 2D version supports higher resolution (200×120 = 24,000 nodes)
and longer runs (400 steps) for clearly visible bending.

Three simulations are run side-by-side:
    1. LENSED:    Gaussian beam through n(r) gradient → bent path
    2. REFERENCE: Same beam, no lens → straight path
    3. STRONG:    Same beam, 2× stronger lens → more bending

DAG Compliance:
    Upstream: ave.core.constants → ave.core.k4_tlm
    Outputs: 12-panel time evolution + 6-panel analysis figure

Vol 3 Ch. 2 — Gravitational Lensing Cross-Validation
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import PowerNorm

from ave.core.k4_tlm import K4Lattice2D, build_k4_scattering_matrix


def apply_lens_2d(lattice, cx, cy, n0, r_core):
    """
    Apply a Lorentzian refractive lens to a 2D K4-TLM lattice.

    n(r) = 1 + n0 / (1 + (r/r_core)²)

    Modifies each node's scattering matrix with impedance z = 1/n(r),
    which slows the local wave speed: c_local = c₀/n.
    """
    for i in range(lattice.nx):
        for j in range(lattice.ny):
            r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2)
            n = 1.0 + n0 / (1.0 + (r / r_core) ** 2)
            if n > 1.001:
                chirality = lattice.nodes[i, j].chirality
                lattice.nodes[i, j].S_matrix = build_k4_scattering_matrix(z_local=1.0 / n, chirality=chirality)


def inject_beam_2d(lattice, y_center, beam_width, amplitude, wavelength, x_inj=2):
    """
    Inject a CW Gaussian beam in +x on a 2D lattice.

    Injects at x=x_inj with sinusoidal phase and Gaussian y-envelope.
    Port 0 = +x direction.
    """
    k = 2.0 * np.pi / wavelength
    phase = k * lattice.timestep

    for j in range(lattice.ny):
        dy = j - y_center
        envelope = amplitude * np.exp(-(dy**2) / (2.0 * beam_width**2))
        if envelope > 1e-8:
            lattice.nodes[x_inj, j].V_inc[0] += envelope * np.sin(phase)


def run_lensing_sim(nx, ny, n_steps, n0, r_core, beam_y, beam_w, wavelength, amplitude):
    """
    Run a complete 2D lensing simulation.

    Returns dict with snapshots, field arrays, and metadata.
    """
    cx, cy = nx // 2, ny // 2
    lattice = K4Lattice2D(nx, ny, alternating_chirality=True)

    if n0 > 0:
        apply_lens_2d(lattice, cx, cy, n0, r_core)

    # Collect snapshots
    snapshots = []
    n_frames = 12
    snap_every = max(1, n_steps // n_frames)

    for step in range(n_steps):
        inject_beam_2d(lattice, beam_y, beam_w, amplitude, wavelength)
        lattice.step()

        if step % snap_every == 0:
            snapshots.append(lattice.get_field_array().copy())

    # Final field
    final_field = lattice.get_field_array().copy()

    # Compute n(r) field for reference
    n_field = np.ones((nx, ny))
    for i in range(nx):
        for j in range(ny):
            r = np.sqrt((i - cx) ** 2 + (j - cy) ** 2)
            n_field[i, j] = 1.0 + n0 / (1.0 + (r / r_core) ** 2)

    return {
        "snapshots": snapshots,
        "final_field": final_field,
        "n_field": n_field,
        "n0": n0,
        "r_core": r_core,
        "cx": cx,
        "cy": cy,
        "beam_y": beam_y,
    }


def main():
    """Run three lensing simulations and produce publication-quality figures."""
    print("=" * 70)
    print("  K4-TLM GRAVITATIONAL LENSING — 2D HIGH-RESOLUTION")
    print("  Photon bending by refractive metric n(r) = 1 + n₀/(1+(r/r_c)²)")
    print("=" * 70)

    NX, NY = 200, 120
    N_STEPS = 400
    BEAM_Y = NY // 2 + 10  # Impact parameter = 10 cells above mass
    BEAM_W = 4.0  # Gaussian width
    WAVELENGTH = 10.0
    AMPLITUDE = 0.15
    R_CORE = 8.0

    print(f"\n  Lattice: {NX}×{NY} = {NX*NY:,} nodes")
    print(f"  Steps: {N_STEPS}")
    print(f"  Beam: y₀={BEAM_Y}, σ={BEAM_W}, λ={WAVELENGTH}")
    print(f"  Impact parameter b = {BEAM_Y - NY//2} cells")

    # ── Simulation 1: Moderate lens (n₀ = 0.5) ──
    print("\n[1] Moderate lens (n₀ = 0.5)...")
    result_mod = run_lensing_sim(
        NX,
        NY,
        N_STEPS,
        n0=0.5,
        r_core=R_CORE,
        beam_y=BEAM_Y,
        beam_w=BEAM_W,
        wavelength=WAVELENGTH,
        amplitude=AMPLITUDE,
    )
    print(f"    Done. {len(result_mod['snapshots'])} frames captured.")

    # ── Simulation 2: Reference (no lens) ──
    print("\n[2] Reference (flat space)...")
    result_ref = run_lensing_sim(
        NX,
        NY,
        N_STEPS,
        n0=0.0,
        r_core=R_CORE,
        beam_y=BEAM_Y,
        beam_w=BEAM_W,
        wavelength=WAVELENGTH,
        amplitude=AMPLITUDE,
    )
    print(f"    Done. {len(result_ref['snapshots'])} frames captured.")

    # ── Simulation 3: Strong lens (n₀ = 0.8) ──
    print("\n[3] Strong lens (n₀ = 0.8)...")
    result_strong = run_lensing_sim(
        NX,
        NY,
        N_STEPS,
        n0=0.8,
        r_core=R_CORE,
        beam_y=BEAM_Y,
        beam_w=BEAM_W,
        wavelength=WAVELENGTH,
        amplitude=AMPLITUDE,
    )
    print(f"    Done. {len(result_strong['snapshots'])} frames captured.")

    # ═══════════════════════════════════════════════════════════════════════
    # FIGURE 1: 12-Frame Time Evolution (moderate lens)
    # ═══════════════════════════════════════════════════════════════════════
    print("\n[Plotting] 12-frame time evolution...")

    snaps = result_mod["snapshots"][:12]
    cx, cy = result_mod["cx"], result_mod["cy"]
    n_field = result_mod["n_field"]
    snap_every = max(1, N_STEPS // 12)

    # Global max for consistent colormap
    vmax = max(np.max(s) for s in snaps)

    fig, axes = plt.subplots(3, 4, figsize=(24, 15))
    fig.suptitle(
        "K4-TLM Gravitational Lensing — Time Evolution\n"
        f"{NX}×{NY} lattice | n(0) = 1.5 | r_core = {R_CORE} | "
        f"b = {BEAM_Y - NY//2} cells | λ = {WAVELENGTH}",
        fontsize=15,
        fontweight="bold",
        y=0.98,
    )

    for idx, snap in enumerate(snaps):
        ax = axes[idx // 4, idx % 4]
        step_num = idx * snap_every

        # Use power-law normalization to bring out faint features
        im = ax.imshow(
            snap.T,
            cmap="hot",
            origin="lower",
            extent=[0, NX, 0, NY],
            norm=PowerNorm(gamma=0.4, vmin=0, vmax=vmax),
        )

        # Mass center + core radius
        circle = plt.Circle((cx, cy), R_CORE, color="#00E5FF", fill=False, lw=2, ls="--", alpha=0.7)
        ax.add_patch(circle)
        ax.plot(cx, cy, "+", color="#00E5FF", ms=12, mew=2.5)

        # Straight-line reference
        ax.axhline(BEAM_Y, color="white", ls=":", alpha=0.3, lw=1)
        ax.annotate(
            "un-lensed path",
            (NX - 5, BEAM_Y + 1.5),
            color="white",
            fontsize=7,
            ha="right",
            alpha=0.4,
        )

        # n(r) contours
        ax.contour(
            np.arange(NX),
            np.arange(NY),
            n_field.T,
            levels=[1.1, 1.2, 1.3],
            colors="#00E5FF",
            linewidths=0.5,
            alpha=0.25,
        )

        ax.set_title(f"t = {step_num}", fontsize=11, fontweight="bold")
        ax.set_xlim(0, NX)
        ax.set_ylim(0, NY)
        if idx // 4 == 2:
            ax.set_xlabel("x [cells]", fontsize=10)
        if idx % 4 == 0:
            ax.set_ylabel("y [cells]", fontsize=10)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    output_dir = os.path.join(os.path.dirname(__file__), "..", "assets", "sim_outputs")
    os.makedirs(output_dir, exist_ok=True)
    path1 = os.path.join(output_dir, "k4_tlm_gravitational_lensing.png")
    plt.savefig(path1, dpi=150, bbox_inches="tight", facecolor="black")
    print(f"  Saved: {path1}")
    plt.close()

    # ═══════════════════════════════════════════════════════════════════════
    # FIGURE 2: 6-Panel Comparison + Analysis
    # ═══════════════════════════════════════════════════════════════════════
    print("  [Plotting] 6-panel analysis...")

    fig2, axes2 = plt.subplots(2, 3, figsize=(22, 13))
    fig2.suptitle(
        "K4-TLM Gravitational Lensing — Comparative Analysis\n" "Photon deflection by refractive metric (Axiom 1)",
        fontsize=15,
        fontweight="bold",
        y=0.99,
    )

    # ── Panel 1: Refractive index field ──
    ax = axes2[0, 0]
    im = ax.imshow(n_field.T, cmap="viridis", origin="lower", extent=[0, NX, 0, NY])
    ax.plot(cx, cy, "w+", ms=14, mew=2.5)
    circle = plt.Circle((cx, cy), R_CORE, color="white", fill=False, lw=2, ls="--")
    ax.add_patch(circle)
    ax.axhline(BEAM_Y, color="red", ls="--", lw=1.5, alpha=0.5, label=f"Beam path y₀={BEAM_Y}")
    ax.set_title("Refractive Index n(r)\n(Gravitational Metric)", fontsize=12)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend(fontsize=9, loc="upper right")
    plt.colorbar(im, ax=ax, label="n(r)")

    # ── Panel 2: Reference beam (flat space) ──
    ax = axes2[0, 1]
    ref = result_ref["final_field"]
    im = ax.imshow(
        ref.T,
        cmap="hot",
        origin="lower",
        extent=[0, NX, 0, NY],
        norm=PowerNorm(gamma=0.4, vmin=0, vmax=vmax),
    )
    ax.axhline(BEAM_Y, color="white", ls=":", alpha=0.4)
    ax.set_title("Reference: Flat Space\n(no gravitational lens)", fontsize=12)
    ax.set_xlabel("x")

    # ── Panel 3: Moderate lens (n₀ = 0.5) ──
    ax = axes2[0, 2]
    mod = result_mod["final_field"]
    im = ax.imshow(
        mod.T,
        cmap="hot",
        origin="lower",
        extent=[0, NX, 0, NY],
        norm=PowerNorm(gamma=0.4, vmin=0, vmax=vmax),
    )
    circle = plt.Circle((cx, cy), R_CORE, color="#00E5FF", fill=False, lw=1.5, ls="--", alpha=0.6)
    ax.add_patch(circle)
    ax.plot(cx, cy, "+", color="#00E5FF", ms=10, mew=2)
    ax.axhline(BEAM_Y, color="white", ls=":", alpha=0.3)
    ax.set_title("Lensed: n(0) = 1.5\nBeam bends toward mass", fontsize=12)
    ax.set_xlabel("x")

    # ── Panel 4: Strong lens (n₀ = 0.8) ──
    ax = axes2[1, 0]
    strong = result_strong["final_field"]
    vmax_s = max(np.max(strong), 1e-6)
    im = ax.imshow(
        strong.T,
        cmap="hot",
        origin="lower",
        extent=[0, NX, 0, NY],
        norm=PowerNorm(gamma=0.4, vmin=0, vmax=vmax_s),
    )
    circle = plt.Circle((cx, cy), R_CORE, color="#00E5FF", fill=False, lw=1.5, ls="--", alpha=0.6)
    ax.add_patch(circle)
    ax.plot(cx, cy, "+", color="#00E5FF", ms=10, mew=2)
    ax.axhline(BEAM_Y, color="white", ls=":", alpha=0.3)
    ax.set_title("Strong Lens: n(0) = 1.8\nStronger bending", fontsize=12)
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    # ── Panel 5: Difference field (lensed - ref) ──
    ax = axes2[1, 1]
    diff = mod - ref
    vmax_d = max(np.max(np.abs(diff)), 1e-10)
    im = ax.imshow(
        diff.T,
        cmap="RdBu_r",
        origin="lower",
        extent=[0, NX, 0, NY],
        vmin=-vmax_d * 0.5,
        vmax=vmax_d * 0.5,
    )
    circle = plt.Circle((cx, cy), R_CORE, color="black", fill=False, lw=1, ls="--", alpha=0.4)
    ax.add_patch(circle)
    ax.axhline(BEAM_Y, color="gray", ls=":", alpha=0.3)
    ax.set_title("Field Difference (Mod − Ref)\nAsymmetric phase → bending", fontsize=12)
    ax.set_xlabel("x")
    plt.colorbar(im, ax=ax, label="ΔV")

    # ── Panel 6: y-profile at exit ──
    ax = axes2[1, 2]
    x_exit = NX - 10
    profile_ref = ref[x_exit, :]
    profile_mod = mod[x_exit, :]
    profile_str = strong[x_exit, :]
    y = np.arange(NY)

    max_p = max(np.max(profile_ref), np.max(profile_mod), np.max(profile_str), 1e-10)
    ax.fill_between(y, 0, profile_ref / max_p, alpha=0.2, color="blue", label="Reference")
    ax.plot(y, profile_ref / max_p, "b-", lw=2)
    ax.fill_between(y, 0, profile_mod / max_p, alpha=0.15, color="red")
    ax.plot(y, profile_mod / max_p, "r-", lw=2, label="n₀ = 0.5")
    ax.plot(y, profile_str / max_p, "orange", lw=2, ls="--", label="n₀ = 0.8")
    ax.axvline(BEAM_Y, color="blue", ls=":", alpha=0.5, label=f"y₀ = {BEAM_Y}")
    ax.axvline(cy, color="cyan", ls="--", alpha=0.5, label=f"Mass y = {cy}")
    ax.set_title(f"y-Profile at x = {x_exit}\nCentroid shift = deflection", fontsize=12)
    ax.set_xlabel("y [cells]")
    ax.set_ylabel("Normalized |V|")
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(BEAM_Y - 25, BEAM_Y + 15)

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    path2 = os.path.join(output_dir, "k4_tlm_lensing_summary.png")
    plt.savefig(path2, dpi=150, bbox_inches="tight")
    print(f"  Saved: {path2}")
    plt.close()

    # ── Summary ──
    print("\n" + "=" * 70)
    print("  GRAVITATIONAL LENSING SIMULATION COMPLETE")
    print("=" * 70)
    print(f"  Lattice: {NX}×{NY} = {NX*NY:,} nodes")
    print(f"  Steps: {N_STEPS}")
    print(f"  Three simulations: Reference, n₀=0.5, n₀=0.8")
    print(f"  Figures: 12-frame evolution + 6-panel analysis")
    print("=" * 70)

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

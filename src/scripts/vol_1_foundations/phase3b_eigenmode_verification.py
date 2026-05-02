"""
Phase 3b eigenmode verification + photon→electron visualization.

This script executes the design spec in
research/L3_electron_soliton/31_phase3b_simulation_setup.md.

Two aims:

  A. Scientific question — is the shell geometry at strain A ≈ 0.48 a
     stable eigenmode (R/r plateaus at ≈ 2.60), or a transient passage
     through Golden-Torus proportions?

  B. Visual — show the K4 lattice field at photon vs electron vs
     over-compressed drive, so the physical transformation is visible.

Runs:
  1. Electron-candidate: strain A=0.48, PML boundary (matches sweep)
  2. Photon baseline:    strain A=0.05, PML boundary (low-strain
                         comparison — no saturation should engage)
  3. Over-compressed:    strain A=0.95, PML boundary (geometry collapse
                         visual for contrast)

Per run: record R(t), r(t), R/r(t), α⁻¹(t), energy(t), A_max(t) at
every step. Save full V_inc state at steps 100, 300, 500 for spatial
visualization.

Outputs:
  /tmp/phase3b_eigenmode_timeseries.png  — time-series traces (Aim A)
  /tmp/phase3b_spatial_snapshots.png     — soliton field at all three
                                            strains (Aim B — the
                                            photon→electron visual)
  /tmp/phase3b_eigenmode.npz             — raw data
"""
from __future__ import annotations

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

from ave.core.k4_tlm import K4Lattice3D
from ave.core.constants import V_SNAP, V_YIELD, ALPHA
from tlm_electron_soliton_eigenmode import (
    initialize_2_3_voltage_ansatz, shell_envelope, extract_alpha_inverse,
)

PHI = (1.0 + np.sqrt(5.0)) / 2.0
ALPHA_INV_TARGET = 1.0 / ALPHA

# Full 3D snapshot step indices (for static comparison figure)
SNAPSHOT_STEPS = (100, 300, 500)
# xy-slice recording interval (for GIF animation)
FRAME_INTERVAL = 10


def run_timeresolved(strain_target: float, label: str,
                     N: int = 64, n_steps: int = 600,
                     R_seed: float = 16.0, r_seed: float = 6.108,
                     pml_thickness: int = 6) -> dict:
    """Run TLM recording shell geometry and α⁻¹ at every step.

    Parameters derived per 31_phase3b_simulation_setup.md:
      - N, R_seed, r_seed: from §2.3
      - amplitude: from §2.6 (strain_target · V_SNAP / π)
      - n_steps: from §2.2 (600 ≈ 67 Compton periods)
      - pml_thickness: from §2.3 (default 6; caller can override)
      - op3_bond_reflection=True: mandatory per §2.4
    """
    amplitude = strain_target * float(V_SNAP) / np.pi

    lattice = K4Lattice3D(
        N, N, N, dx=1.0,
        pml_thickness=pml_thickness,
        nonlinear=False,
        op3_bond_reflection=True,
    )
    initialize_2_3_voltage_ansatz(
        lattice, R=R_seed, r=r_seed, amplitude=amplitude,
    )

    cx = (lattice.nx - 1) / 2.0
    cy = (lattice.ny - 1) / 2.0
    cz = (lattice.nz - 1) / 2.0

    # Per-step arrays
    R_t = np.zeros(n_steps, dtype=float)
    r_t = np.zeros(n_steps, dtype=float)
    alpha_inv_t = np.zeros(n_steps, dtype=float)
    energy_t = np.zeros(n_steps, dtype=float)
    strain_max_t = np.zeros(n_steps, dtype=float)

    snapshots = {}
    # Animation frames: xy-slice of |V|^2 recorded every FRAME_INTERVAL steps
    xy_frames = []    # list of (step, 2D-array)

    V_sq_init = np.sum(lattice.V_inc ** 2, axis=-1)
    energy_init = float(np.sum(V_sq_init) + np.sum(lattice.V_ref ** 2))

    cz_int = int(cz)

    for step in range(n_steps):
        lattice.step()

        V_mag = np.sqrt(np.sum(lattice.V_inc ** 2, axis=-1))
        R_s, r_s = shell_envelope(V_mag, cx, cy, cz)
        alpha = extract_alpha_inverse(R_s, r_s, c=3)
        alpha_inv = alpha["alpha_inv"] if alpha["valid"] else float("nan")

        R_t[step] = R_s
        r_t[step] = r_s
        alpha_inv_t[step] = alpha_inv
        energy_t[step] = float(np.sum(lattice.V_inc ** 2) +
                               np.sum(lattice.V_ref ** 2))
        v_total = np.sqrt(np.sum(lattice.V_inc ** 2, axis=-1))
        strain_max_t[step] = float(v_total.max() / V_SNAP)

        # GIF frame: xy-slice at z=center every FRAME_INTERVAL
        if (step + 1) % FRAME_INTERVAL == 0:
            xy_frames.append((step + 1, V_mag[:, :, cz_int].copy()))

        # Save spatial snapshot at selected steps
        if (step + 1) in SNAPSHOT_STEPS:
            snapshots[step + 1] = {
                "V_inc": lattice.V_inc.copy(),
                "V_ref": lattice.V_ref.copy(),
                "mask_A": lattice.mask_A.copy(),
            }

    return {
        "label": label,
        "strain_target": strain_target,
        "amplitude": amplitude,
        "N": N,
        "n_steps": n_steps,
        "pml_thickness": pml_thickness,
        "energy_init": energy_init,
        "R_t": R_t,
        "r_t": r_t,
        "alpha_inv_t": alpha_inv_t,
        "energy_t": energy_t,
        "strain_max_t": strain_max_t,
        "snapshots": snapshots,
        "xy_frames": xy_frames,
        "cx": cx, "cy": cy, "cz": cz,
    }


def classify_eigenmode(result: dict, tolerance: float = 0.03) -> str:
    """Decision per 31_phase3b_simulation_setup.md §3.1.

    Compare R/r at step 200 vs step (n_steps - 1). If within tolerance,
    eigenmode candidate. Otherwise transient.
    """
    ratio = result["R_t"] / np.maximum(result["r_t"], 1e-9)
    # Averaging window to dampen bin-edge noise
    early = float(np.nanmean(ratio[180:220]))
    late = float(np.nanmean(ratio[-40:]))
    alpha_late_std = float(np.nanstd(result["alpha_inv_t"][200:]))

    rel_change = abs(late - early) / max(abs(early), 1e-9)

    verdict = []
    verdict.append(f"R/r early (200): {early:.3f}, late (end): {late:.3f}")
    verdict.append(f"relative change: {rel_change:.3%}")
    verdict.append(f"α⁻¹ std (steps 200-end): {alpha_late_std:.2f}")
    if rel_change < tolerance and alpha_late_std < 5.0:
        verdict.append("→ EIGENMODE candidate")
    elif rel_change > 0.05:
        verdict.append("→ TRANSIENT (R/r drifting)")
    else:
        verdict.append("→ AMBIGUOUS")
    return "\n  ".join(verdict)


def plot_timeseries(results: list, out_path: str) -> None:
    """Figure 1: time-series for eigenmode verification."""
    fig, axes = plt.subplots(2, 2, figsize=(13, 8))

    for res in results:
        t = np.arange(res["n_steps"])
        label = f"{res['label']} (A≈{res['strain_target']:.2f})"

        ax = axes[0, 0]
        ratio = res["R_t"] / np.maximum(res["r_t"], 1e-9)
        ax.plot(t, ratio, alpha=0.7, label=label)

        ax = axes[0, 1]
        ax.plot(t, res["alpha_inv_t"], alpha=0.7, label=label)

        ax = axes[1, 0]
        ax.plot(t, res["energy_t"] / res["energy_init"],
                alpha=0.7, label=label)

        ax = axes[1, 1]
        ax.plot(t, res["strain_max_t"], alpha=0.7, label=label)

    ax = axes[0, 0]
    ax.axhline(PHI ** 2, color="red", linestyle=":",
               label=f"φ² = {PHI**2:.3f} (Golden Torus)")
    ax.set_ylabel("R/r (shell aspect)")
    ax.set_xlabel("simulation step")
    ax.set_title("R/r vs time — eigenmode if plateau; transient if drift")
    ax.set_ylim(1, 4)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    ax = axes[0, 1]
    ax.axhline(ALPHA_INV_TARGET, color="red", linestyle=":",
               label=f"electron α⁻¹ = {ALPHA_INV_TARGET}")
    ax.set_ylabel("α⁻¹")
    ax.set_xlabel("simulation step")
    ax.set_title("α⁻¹ vs time")
    ax.set_ylim(50, 300)
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    ax = axes[1, 0]
    ax.set_ylabel("energy / energy(0)")
    ax.set_xlabel("simulation step")
    ax.set_title("Energy decay — PML vs physical confinement")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    ax = axes[1, 1]
    ax.axhline(np.sqrt(2 * ALPHA), color="gray", linestyle=":",
               label="√(2α) Regime II onset")
    ax.axhline(np.sqrt(3) / 2, color="gray", linestyle="--",
               label="√3/2 Regime III")
    ax.set_ylabel("max strain A = max|V_inc|/V_SNAP")
    ax.set_xlabel("simulation step")
    ax.set_title("Peak strain vs time — does saturation regime hold?")
    ax.grid(alpha=0.3)
    ax.legend(fontsize=8)

    plt.suptitle("Phase 3b — eigenmode verification (time-resolved)",
                 fontsize=13, y=0.99)
    plt.tight_layout()
    plt.savefig(out_path, dpi=110)
    plt.close()


def plot_spatial_snapshots(results: list, out_path: str) -> None:
    """Figure 2: the photon→electron transformation.

    Layout: rows = strain conditions, columns = (xy equatorial slice,
    xz polar slice, (2,3) phase on shell). Three strains visualized side
    by side so the geometry transformation is directly comparable.
    """
    n_runs = len(results)
    fig, axes = plt.subplots(n_runs, 3, figsize=(13, 4 * n_runs))
    if n_runs == 1:
        axes = np.array([axes])

    # Use the step-300 snapshot for every run (mid-sim, past transient)
    snap_step = 300

    for row_idx, res in enumerate(results):
        snap = res["snapshots"].get(snap_step)
        if snap is None:
            for col in range(3):
                axes[row_idx, col].text(0.5, 0.5,
                    f"no snapshot at step {snap_step}",
                    transform=axes[row_idx, col].transAxes,
                    ha="center", va="center")
            continue

        V_inc = snap["V_inc"]
        mask_A = snap["mask_A"]
        cx_i = int(res["cx"])
        cy_i = int(res["cy"])
        cz_i = int(res["cz"])

        V_mag = np.sqrt(np.sum(V_inc ** 2, axis=-1))

        # Pull the late-time R/r for titling
        R_late = float(np.nanmean(res["R_t"][-40:]))
        r_late = float(np.nanmean(res["r_t"][-40:]))
        ratio_late = R_late / max(r_late, 1e-9)
        alpha_late = float(np.nanmean(res["alpha_inv_t"][-40:]))

        row_title = (f"{res['label']} | strain A≈{res['strain_target']:.2f} | "
                     f"R/r={ratio_late:.2f}  α⁻¹={alpha_late:.1f}")

        # --- Column 1: xy slice at z = center (toroidal cross-section) ---
        ax = axes[row_idx, 0]
        xy_slice = V_mag[:, :, cz_i]
        im = ax.imshow(xy_slice.T, origin="lower", cmap="inferno",
                       extent=[0, res["N"], 0, res["N"]])
        ax.set_xlabel("x"); ax.set_ylabel("y")
        ax.set_title(f"{row_title}\nxy at z={cz_i} (toroidal)",
                     fontsize=9)
        plt.colorbar(im, ax=ax, shrink=0.7)
        # Circle at R_late on this slice
        theta_c = np.linspace(0, 2 * np.pi, 120)
        ax.plot(cx_i + R_late * np.cos(theta_c),
                cy_i + R_late * np.sin(theta_c),
                color="cyan", lw=1, alpha=0.7, ls=":")

        # --- Column 2: xz slice at y = center (polar cross-section) ---
        ax = axes[row_idx, 1]
        xz_slice = V_mag[:, cy_i, :]
        im = ax.imshow(xz_slice.T, origin="lower", cmap="inferno",
                       extent=[0, res["N"], 0, res["N"]])
        ax.set_xlabel("x"); ax.set_ylabel("z")
        ax.set_title(f"xz at y={cy_i} (polar) — "
                     f"shell cross-sections", fontsize=9)
        plt.colorbar(im, ax=ax, shrink=0.7)
        # Shell circles at ±R on the x-axis (poloidal minor circles)
        theta_c = np.linspace(0, 2 * np.pi, 120)
        ax.plot(cx_i + R_late + r_late * np.cos(theta_c),
                cz_i + r_late * np.sin(theta_c),
                color="cyan", lw=1, alpha=0.7, ls=":")
        ax.plot(cx_i - R_late + r_late * np.cos(theta_c),
                cz_i + r_late * np.sin(theta_c),
                color="cyan", lw=1, alpha=0.7, ls=":")

        # --- Column 3: phase on the shell (arg c) ---
        ax = axes[row_idx, 2]
        # Shell points: V_mag above threshold AND on mask_A
        peak = float(V_mag[mask_A].max()) if mask_A.sum() else 1.0
        shell = (V_mag > 0.3 * peak) & mask_A
        c_field = V_inc[..., 0] + 1j * V_inc[..., 2]
        phase = np.angle(c_field)
        xs, ys, zs = np.where(shell)
        if len(xs):
            # Project to a 2D map using (toroidal_angle, poloidal_angle)
            rho = np.sqrt((xs - cx_i) ** 2 + (ys - cy_i) ** 2)
            phi_tor = np.arctan2(ys - cy_i, xs - cx_i)
            R_peak_probe = float(np.median(rho))
            psi_pol = np.arctan2(zs - cz_i, rho - R_peak_probe)
            ph = phase[xs, ys, zs]
            sc = ax.scatter(phi_tor, psi_pol, c=ph,
                            cmap="hsv", s=12, alpha=0.8,
                            vmin=-np.pi, vmax=np.pi)
            ax.set_xlim(-np.pi, np.pi)
            ax.set_ylim(-np.pi, np.pi)
            plt.colorbar(sc, ax=ax, shrink=0.7, label="arg(V[p0] + i·V[p2])")
        ax.set_xlabel(r"toroidal angle $\phi$")
        ax.set_ylabel(r"poloidal angle $\psi$")
        ax.set_title(
            f"(2,3) winding: phase on shell\n"
            f"target: θ = 2φ + 3ψ  |  snap step {snap_step}", fontsize=9)

    plt.suptitle(
        "Photon → electron transformation — what the K4 lattice actually "
        "does as drive amplitude crosses Axiom-4 saturation",
        fontsize=13, y=1.00,
    )
    plt.tight_layout()
    plt.savefig(out_path, dpi=110)
    plt.close()


def plot_animation(results: list, out_path: str, fps: int = 8) -> None:
    """Side-by-side animated GIF of xy-slice |V_inc| at z=center across
    all three strain conditions, evolving in time.

    Each frame is one xy-slice per run at matched step indices. Shows
    the soliton's time evolution in all three regimes simultaneously.
    """
    n_runs = len(results)
    # All runs use the same FRAME_INTERVAL so frame counts match
    n_frames = min(len(r["xy_frames"]) for r in results)
    if n_frames == 0:
        print(f"  [animation] no frames recorded — skipping GIF")
        return

    fig, axes = plt.subplots(1, n_runs, figsize=(5 * n_runs, 5))
    if n_runs == 1:
        axes = [axes]

    # Per-run colormap scales: use initial-frame max as vmax to stabilize
    vmax_per_run = []
    for res in results:
        frame0 = res["xy_frames"][0][1]
        vmax_per_run.append(float(frame0.max()) if frame0.size else 1.0)

    # Image handles + annotation text per axis
    imshow_handles = []
    text_handles = []
    N = results[0]["N"]
    for idx, (res, ax) in enumerate(zip(results, axes)):
        frame0 = res["xy_frames"][0][1]
        im = ax.imshow(
            frame0.T, origin="lower", cmap="inferno",
            extent=[0, N, 0, N], vmin=0, vmax=vmax_per_run[idx],
        )
        imshow_handles.append(im)
        ax.set_title(
            f"{res['label']}\nstrain A≈{res['strain_target']:.2f}",
            fontsize=10,
        )
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        # Text annotation showing step + R/r + α⁻¹ updated per frame
        txt = ax.text(
            0.02, 0.98, "", transform=ax.transAxes, va="top", ha="left",
            color="white", fontsize=9, family="monospace",
            bbox={"facecolor": "black", "alpha": 0.5, "pad": 3},
        )
        text_handles.append(txt)

    plt.suptitle(
        "K4-TLM soliton evolution: photon (left) → electron (middle) "
        "→ over-compressed (right)",
        fontsize=12, y=1.02,
    )
    plt.tight_layout()

    def update(frame_idx):
        artists = []
        for idx, res in enumerate(results):
            step_i, slice_i = res["xy_frames"][frame_idx]
            imshow_handles[idx].set_data(slice_i.T)
            # Sample R/r, α⁻¹ at this step
            s = step_i - 1
            R_s = res["R_t"][s]
            r_s = res["r_t"][s]
            a_s = res["alpha_inv_t"][s]
            ratio = R_s / max(r_s, 1e-9)
            text_handles[idx].set_text(
                f"step {step_i:>3d}\n"
                f"R/r = {ratio:5.2f}\n"
                f"α⁻¹ = {a_s:6.1f}"
            )
            artists.append(imshow_handles[idx])
            artists.append(text_handles[idx])
        return artists

    anim = FuncAnimation(
        fig, update, frames=n_frames, interval=1000 // fps, blit=False,
    )
    writer = PillowWriter(fps=fps)
    anim.save(out_path, writer=writer, dpi=90)
    plt.close(fig)


def main():
    print("=" * 72)
    print("PHASE 3b EIGENMODE VERIFICATION + PHOTON→ELECTRON VISUAL")
    print("Per simulation setup: research/L3_electron_soliton/"
          "31_phase3b_simulation_setup.md")
    print("=" * 72)

    # Note: these are strain_TARGET values. Mapping to achieved strain
    # (measured as v_total_max/V_SNAP on the shell) is nonlinear because
    # the envelope formula's peak depends on lattice geometry and the
    # Op3 bond reflection modulates instantaneous v_total. Empirical map
    # from the amplitude sweep:
    #   target 0.3 → achieved 0.482 (α⁻¹=139 after 300 steps, R/r=2.60)
    #   target 0.48 → achieved ~0.78 (different regime)
    #   target 0.05 → achieved 0.080
    #   target 0.95 → achieved ~1.5 (rupture)
    runs = [
        ("electron-candidate (target 0.3 → A≈0.48)", 0.3, 6),
        ("photon baseline (target 0.05)", 0.05, 6),
        ("over-compressed (target 0.95)", 0.95, 6),
    ]

    results = []
    for i, (label, strain, pml) in enumerate(runs):
        print(f"\n[{i+1}/{len(runs)}] {label}")
        print(f"  strain_target = {strain}, pml = {pml}, n_steps = 600")
        res = run_timeresolved(strain_target=strain, label=label,
                               pml_thickness=pml, n_steps=600)
        results.append(res)

        # Summary
        ratio_t = res["R_t"] / np.maximum(res["r_t"], 1e-9)
        print(f"  achieved max strain: {res['strain_max_t'].max():.3e}")
        print(f"  R/r (late-window avg): "
              f"{float(np.nanmean(ratio_t[-40:])):.3f}")
        print(f"  α⁻¹ (late-window avg): "
              f"{float(np.nanmean(res['alpha_inv_t'][-40:])):.2f}")
        print(f"  energy final/init: "
              f"{res['energy_t'][-1] / res['energy_init']:.3f}")
        print(f"  eigenmode diagnostic:")
        print(f"    {classify_eigenmode(res)}")

    # Save raw data
    save_dict = {}
    for r in results:
        tag = r["label"].split()[0]
        save_dict[f"{tag}_R_t"] = r["R_t"]
        save_dict[f"{tag}_r_t"] = r["r_t"]
        save_dict[f"{tag}_alpha_inv_t"] = r["alpha_inv_t"]
        save_dict[f"{tag}_energy_t"] = r["energy_t"]
        save_dict[f"{tag}_strain_max_t"] = r["strain_max_t"]
    np.savez("/tmp/phase3b_eigenmode.npz", **save_dict)
    print(f"\nRaw data: /tmp/phase3b_eigenmode.npz")

    # Plots
    plot_timeseries(results, "/tmp/phase3b_eigenmode_timeseries.png")
    plot_spatial_snapshots(results, "/tmp/phase3b_spatial_snapshots.png")
    plot_animation(results, "/tmp/phase3b_evolution.gif", fps=8)

    print("\nFigures:")
    print("  /tmp/phase3b_eigenmode_timeseries.png  — time-resolved traces")
    print("  /tmp/phase3b_spatial_snapshots.png     — photon→electron visual")
    print("  /tmp/phase3b_evolution.gif             — animated evolution")


if __name__ == "__main__":
    main()

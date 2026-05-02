"""
Photon Rifling + Dark Wake — Full Deliverable
==============================================

Long-domain Yee FDTD with circularly polarized soft pulse + Axiom 4
saturation engaged + τ_zx-equivalent dark wake observation. Delivers
Grant's original request: stable rifled/chiral impedance-matched
propagation over long enough distance to see the dark wake.

Configuration:
  - Domain 320×64×64 cells, dx=1cm, λ = 20 cells (1.5 GHz)
  - Source amplitude pushes into Ax 4 saturation regime (amp >= V_yield)
    so ε_eff = ε₀·√(1−(V/V_yield)²) varies → Z_eff modulates → wake
  - Soft Gaussian-windowed CP pulse (~5 cycles)
  - 800 steps (~12 ns) → wavefront crosses domain
  - Nonlinear vacuum (linear_only=False)

τ_zx-equivalent observable for Yee Maxwell:
  τ_zx ≡ Z_eff(r) · ∂|E|²/∂x  along propagation axis
  where Z_eff = √(μ₀ / ε_eff(V)) per Ax 4 saturation kernel
  Mirror of K4-TLM DarkWakeObserver formula at the Yee field level.

Each animation frame: 4 panels —
  TL: 2D E_y(x, y) at z=center, percentile-99 vmax (rifling stripes)
  TR: 2D phase = arctan2(E_z, E_y) at z=center (HSV rifling cycle)
  BL: 1D τ_zx along central axis (the dark wake observable)
  BR: 1D |E_perp| log-scale + c·t marker (propagation-at-c verification)

Outputs:
  - assets/photon_rifling_dark_wake_RH.gif
  - assets/photon_rifling_dark_wake_LH.gif
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.gridspec import GridSpec

from ave.core.fdtd_3d import FDTD3DEngine
from ave.core.constants import V_YIELD, MU_0, EPSILON_0


def run_pulsed_saturation(handedness: str, nx=320, ny=64, nz=64, n_steps=800,
                           amp_factor: float = 0.7):
    """Long-domain Yee FDTD, NONLINEAR vacuum, soft Gaussian-windowed CP pulse.
    amp_factor=0.7: V_peak ≈ 0.7·V_yield → ε_eff/ε_0 = 0.71 at peak (significant
    saturation engagement) WITHOUT hitting V=V_yield singularity (ε_eff → 0)."""
    eng = FDTD3DEngine(nx, ny, nz, dx=0.01, linear_only=False,  # ← nonlinear
                       use_pml=True, pml_layers=10)
    c = eng.c
    dt = eng.dt
    freq = 1.5e9
    omega = 2.0 * np.pi * freq
    src_x = 18

    n_cycles = 5
    period = 1.0 / freq
    t_sigma = n_cycles * period * 0.5
    t_center = 3.0 * t_sigma

    amp_E = amp_factor * V_YIELD / eng.dx  # > yield → saturation engages
    sigma_yz = 5.0
    cy, cz = ny // 2, nz // 2
    j, k = np.indices((ny, nz), dtype=float)
    r2 = (j - cy) ** 2 + (k - cz) ** 2
    profile = np.exp(-r2 / (2.0 * sigma_yz ** 2))

    sign = +1.0 if handedness == "RH" else -1.0

    record_cadence = 8
    frames = []

    for step in range(1, n_steps + 1):
        t = step * dt
        env = np.exp(-((t - t_center) / t_sigma) ** 2)
        if env > 1e-7:
            Ey_inj = env * amp_E * np.sin(omega * t)
            Ez_inj = env * amp_E * sign * np.cos(omega * t)
            eng.Ey[src_x, :, :] += Ey_inj * profile
            eng.Ez[src_x, :, :] += Ez_inj * profile
        eng.step()
        if step % record_cadence == 0:
            wf = src_x + eng.c * t / eng.dx
            # τ_zx observable along axis
            E_perp_axis = np.sqrt(eng.Ey[:, cy, cz] ** 2 + eng.Ez[:, cy, cz] ** 2)
            V_axis = E_perp_axis * eng.dx
            # Ax 4 saturation: ε_eff = ε_0·√(1−(V/V_yield)²)
            sat_arg = np.maximum(1.0 - (V_axis / V_YIELD) ** 2, 1e-6)
            eps_eff = EPSILON_0 * np.sqrt(sat_arg)
            z_eff = np.sqrt(MU_0 / eps_eff)
            grad_E_sq = np.gradient(E_perp_axis ** 2, eng.dx)
            tau_zx_axis = z_eff * grad_E_sq

            frames.append({
                "t": t,
                "step": step,
                "Ey_slice": np.array(eng.Ey[:, :, cz]),
                "Ez_slice": np.array(eng.Ez[:, :, cz]),
                "E_perp_axis": E_perp_axis,
                "tau_zx_axis": tau_zx_axis,
                "V_over_yield_axis": V_axis / V_YIELD,
                "wavefront_x": wf,
            })

    print(f"  {handedness}: {len(frames)} frames; amp={amp_factor}·V_yield/dx; "
          f"expected wavefront at step {n_steps}: x = {src_x + eng.c*n_steps*dt/eng.dx:.1f}")
    return {
        "handedness": handedness,
        "nx": nx, "ny": ny, "nz": nz, "src_x": src_x,
        "frames": frames,
        "lambda_cells": (c / freq) / eng.dx,
        "amp_factor": amp_factor,
    }


def render_full_animation(result, out_gif):
    nx, ny, nz = result["nx"], result["ny"], result["nz"]
    src_x = result["src_x"]
    handedness = result["handedness"]
    frames = result["frames"]
    cy, cz = ny // 2, nz // 2

    fig = plt.figure(figsize=(18, 11), facecolor="#050510")
    gs = GridSpec(2, 2, figure=fig, hspace=0.32, wspace=0.20)

    ax_ey = fig.add_subplot(gs[0, 0])
    ax_phase = fig.add_subplot(gs[0, 1])
    ax_wake = fig.add_subplot(gs[1, 0])
    ax_axis = fig.add_subplot(gs[1, 1])

    for ax in [ax_ey, ax_phase, ax_wake, ax_axis]:
        ax.set_facecolor("#050510")
        for s in ax.spines.values():
            s.set_color("#444")
        ax.tick_params(colors="#cccccc", labelsize=8)

    # Find global tau_zx peak for stable wake panel scaling
    # Guard against NaN/Inf (can happen if Ax 4 saturation hits V=V_yield singularity)
    tau_global_max = 1e-30
    for f in frames:
        tau = f["tau_zx_axis"]
        finite_tau = np.abs(tau)[np.isfinite(tau)]
        if finite_tau.size > 0:
            local = float(finite_tau.max())
            if local > tau_global_max:
                tau_global_max = local

    def update(frame_idx):
        f = frames[frame_idx]

        # ── TL: E_y slice (rifling stripe pattern)
        ax_ey.cla()
        ax_ey.set_facecolor("#050510")
        Ey_s = f["Ey_slice"]
        vmax = np.percentile(np.abs(Ey_s), 99.0) or 1e-3
        ax_ey.imshow(Ey_s.T, aspect="auto", cmap="seismic",
                     vmin=-vmax, vmax=vmax, origin="lower")
        ax_ey.axvline(src_x, color="cyan", lw=1, ls="--", alpha=0.6)
        wf = min(nx - 1, f["wavefront_x"])
        ax_ey.axvline(wf, color="yellow", lw=1, ls=":", alpha=0.7)
        ax_ey.set_title(
            f"E_y(x, y) at z=center  |  vmax_99 = {vmax:.2e}",
            color="white", fontsize=10,
        )
        ax_ey.set_xlabel("x (cells)", color="#cccccc", fontsize=9)
        ax_ey.set_ylabel("y (cells)", color="#cccccc", fontsize=9)

        # ── TR: phase angle (rifling color cycle)
        ax_phase.cla()
        ax_phase.set_facecolor("#050510")
        E_perp_slice = np.sqrt(f["Ey_slice"] ** 2 + f["Ez_slice"] ** 2)
        phase_slice = np.arctan2(f["Ez_slice"], f["Ey_slice"])
        e_max_s = E_perp_slice.max()
        threshold = 0.02 * e_max_s if e_max_s > 1e-30 else 1.0
        mask = E_perp_slice > threshold
        phase_masked = np.where(mask, phase_slice, np.nan)
        ax_phase.imshow(phase_masked.T, aspect="auto", cmap="hsv",
                        vmin=-np.pi, vmax=np.pi, origin="lower")
        ax_phase.axvline(src_x, color="cyan", lw=1, ls="--", alpha=0.6)
        ax_phase.axvline(wf, color="yellow", lw=1, ls=":", alpha=0.7)
        ax_phase.set_title(
            "Phase = arctan2(E_z, E_y)  |  rifling = HSV color cycle",
            color="white", fontsize=10,
        )
        ax_phase.set_xlabel("x (cells)", color="#cccccc", fontsize=9)
        ax_phase.set_ylabel("y (cells)", color="#cccccc", fontsize=9)

        # ── BL: τ_zx along propagation axis (the DARK WAKE)
        ax_wake.cla()
        ax_wake.set_facecolor("#050510")
        tau = f["tau_zx_axis"]
        x_arr = np.arange(nx)
        ax_wake.plot(x_arr, tau, "-", color="#ff77aa", lw=1.4,
                     label="τ_zx = Z_eff · ∂|E|²/∂x")
        ax_wake.axhline(0, color="#666", lw=0.6, alpha=0.5)
        ax_wake.axvline(src_x, color="cyan", lw=1, ls="--", alpha=0.6, label="source")
        ax_wake.axvline(wf, color="yellow", lw=1, ls=":", alpha=0.7,
                        label=f"c·t (x={wf:.0f})")
        ax_wake.set_xlim(0, nx)
        ax_wake.set_ylim(-tau_global_max * 1.1, tau_global_max * 1.1)
        ax_wake.set_xlabel("x (cells)", color="#cccccc", fontsize=9)
        ax_wake.set_ylabel("τ_zx (Z_eff · ∂|E|²/∂x)", color="#cccccc", fontsize=9)
        ax_wake.set_title(
            "Dark Wake — τ_zx longitudinal shear strain  |  Ax 4 saturation engaged",
            color="white", fontsize=10,
        )
        ax_wake.legend(facecolor="#050510", edgecolor="#444",
                       labelcolor="#cccccc", fontsize=8, loc="upper right")
        ax_wake.grid(alpha=0.2, color="#444")

        # ── BR: |E_perp| log scale + V/V_yield secondary axis (saturation)
        ax_axis.cla()
        ax_axis.set_facecolor("#050510")
        E_perp_axis = f["E_perp_axis"]
        E_plot = np.where(E_perp_axis > 1e-30, E_perp_axis, 1e-30)
        ax_axis.semilogy(x_arr, E_plot, "-", color="#ffaa44", lw=1.4,
                         label="|E_⊥|")
        ax_axis.axvline(src_x, color="cyan", lw=1, ls="--", alpha=0.6, label="src")
        ax_axis.axvline(wf, color="yellow", lw=1, ls=":", alpha=0.7,
                        label=f"c·t (x={wf:.0f})")
        ax_axis.set_xlim(0, nx)
        ax_axis.set_ylim(1.0, 1e8)
        ax_axis.set_xlabel("x (cells)", color="#cccccc", fontsize=9)
        ax_axis.set_ylabel("|E_⊥| [V/m, log]", color="#ffaa44", fontsize=9)
        ax_axis.tick_params(axis="y", labelcolor="#ffaa44")

        # Secondary axis: V/V_yield (saturation indicator)
        ax_sat = ax_axis.twinx()
        ax_sat.set_facecolor("#050510")
        v_over_y = f["V_over_yield_axis"]
        # Guard NaN/Inf for axis limit
        finite_vy = v_over_y[np.isfinite(v_over_y)]
        sat_max = float(finite_vy.max()) if finite_vy.size > 0 else 1.0
        ax_sat.plot(x_arr, np.where(np.isfinite(v_over_y), v_over_y, 0.0),
                    "-", color="#aaff77", lw=1.0, alpha=0.8, label="V/V_yield")
        ax_sat.axhline(1.0, color="red", lw=0.8, ls="--", alpha=0.6,
                       label="yield onset")
        ax_sat.set_ylim(0, max(2.0, sat_max * 1.1))
        ax_sat.set_ylabel("V / V_yield", color="#aaff77", fontsize=9)
        ax_sat.tick_params(axis="y", labelcolor="#aaff77", labelsize=8)
        for s in ax_sat.spines.values():
            s.set_color("#444")
        ax_axis.set_title(
            "|E_⊥| log scale + V/V_yield (saturation marker)",
            color="white", fontsize=10,
        )
        # combined legend
        lines1, labels1 = ax_axis.get_legend_handles_labels()
        lines2, labels2 = ax_sat.get_legend_handles_labels()
        ax_axis.legend(lines1 + lines2, labels1 + labels2,
                       facecolor="#050510", edgecolor="#444",
                       labelcolor="#cccccc", fontsize=7, loc="upper right")
        ax_axis.grid(alpha=0.2, color="#444")

        fig.suptitle(
            f"Rifled Photon ({handedness}) + Dark Wake — Yee Maxwell FDTD with Axiom 4 saturation\n"
            f"λ={result['lambda_cells']:.0f} cells, amp={result['amp_factor']:.1f}·V_yield/dx  |  "
            f"t = {f['t']*1e9:.2f} ns, step = {f['step']}/{result['frames'][-1]['step']}",
            color="white", fontsize=12, fontweight="bold",
        )
        return ()

    print(f"  rendering {len(frames)} frames → {out_gif}")
    anim = FuncAnimation(fig, update, frames=len(frames), interval=80, blit=False)
    writer = PillowWriter(fps=12)
    anim.save(out_gif, writer=writer)
    plt.close(fig)


def main():
    repo_root = Path(__file__).resolve().parent.parent.parent.parent
    assets_dir = repo_root / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 72)
    print("Rifled Photon + Dark Wake — full deliverable (Ax 4 saturation engaged)")
    print("=" * 72)

    for hand in ("RH", "LH"):
        print(f"\n── {hand} (320×64×64, soft pulse, 800 steps, NONLINEAR amp=0.7·V_yield) ──")
        result = run_pulsed_saturation(hand, amp_factor=0.7)
        out_gif = assets_dir / f"photon_rifling_dark_wake_{hand}.gif"
        render_full_animation(result, str(out_gif))

    print(f"\nAll outputs in {assets_dir}/")


if __name__ == "__main__":
    main()

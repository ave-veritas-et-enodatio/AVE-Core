"""
Phase III-A — Single-photon self-saturation null control test.

Question
--------
Can a single high-amplitude traveling photon spontaneously excite the
Cosserat (u, ω) sector via Axiom-4 self-saturation?

Pre-registered predictions
--------------------------
  P_IIIa-null (expected):
      A²_K4 peaks briefly near 1.0 at the packet crest; A²_Cosserat
      stays at noise floor (< 1e-4); (u, ω) never organizes into
      localized structure; photon exits into PML cleanly.
  P_IIIa-anomaly:
      A²_Cosserat develops nontrivial structure even without a
      collision partner. Either a new AVE mechanism (strong-field
      vacuum condensation) or a numerical artifact; either way,
      informative.

AVE compliance
--------------
  S1 = D  coupling: (V²/V_SNAP²) · _reflection_density
  S4 = A  natural units: V_SNAP = 1.0; all amplitudes ∈ [0, 1]
  S5 = B  unified leapfrog (Cosserat sub-stepping per Phase II)
  S6 = A  Q measured (via extract_hopf_charge), not enforced
"""
from __future__ import annotations

import os
import sys
sys.path.insert(0, os.path.dirname(__file__))

import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib import colors as mcolors

from ave.core.constants import ALPHA
from ave.topological.k4_cosserat_coupling import CoupledK4Cosserat

from photon_propagation import PlaneSource
from saturation_heatmap import saturation_fields


def run(
    N: int = 48,
    pml: int = 6,
    lambda_cells: float = 6.0,
    sigma_yz: float = 4.0,
    amp: float = 0.95,           # units of V_SNAP (S4-A: V_SNAP = 1.0)
    V_SNAP: float = 1.0,
    source_x: int = 10,
    n_outer_steps: int = 200,
    record_every: int = 4,
) -> dict:
    sim = CoupledK4Cosserat(N=N, pml=pml, V_SNAP=V_SNAP)
    omega_carrier = 2.0 * np.pi * sim.k4.c / (lambda_cells * sim.k4.dx)
    period = 2.0 * np.pi / omega_carrier
    src = PlaneSource(
        x0=source_x, y_c=(N - 1) / 2.0, z_c=(N - 1) / 2.0,
        direction=(1.0, 0.0, 0.0), sigma_yz=sigma_yz,
        omega=omega_carrier,
        t_center=2.0 * period, t_sigma=0.5 * period,
        amplitude=amp,
    )

    history: list[dict] = []
    heatmap_frames: list[dict] = []

    print(f"Phase III-A: N={N}, amp={amp:.2f}·V_SNAP, {n_outer_steps} outer steps")
    print(f"  N_sub = {sim.n_sub}, outer_dt = {sim.outer_dt:.4f}")

    for step in range(n_outer_steps + 1):
        if step > 0:
            t = step * sim.outer_dt
            src.apply(sim.k4, t)
            sim.step()

        if step % record_every == 0:
            snap = sim.snapshot_scalars()
            snap["Q_hopf"] = sim.cos.extract_hopf_charge()
            snap["src_cum_energy"] = src.cumulative_energy_injected
            history.append(snap)

            # Store A² slice for animation (downsampled cadence)
            if step % (record_every * 2) == 0:
                fields = saturation_fields(sim)
                heatmap_frames.append({
                    "t": sim.time,
                    "A_sq_k4_slice": fields["A_sq_k4"][:, :, N // 2].copy(),
                    "A_sq_cos_slice": fields["A_sq_cos"][:, :, N // 2].copy(),
                    "A_sq_total_slice": fields["A_sq_total"][:, :, N // 2].copy(),
                })

    # ── Verdict ──
    max_A_sq_k4 = max(h["max_A_sq_k4"] for h in history)
    max_A_sq_cos = max(h["max_A_sq_cos"] for h in history)
    max_Q_hopf = max(abs(h["Q_hopf"]) for h in history)
    final_cosserat_centroids = sim.cos.find_soliton_centroids(threshold_frac=0.3)

    # Pre-registered acceptance criteria
    is_null = (max_A_sq_cos < 1e-4) and (len(final_cosserat_centroids) == 0)

    verdict = "P_IIIa-null" if is_null else "P_IIIa-anomaly"

    print(f"\n  max A²_K4   = {max_A_sq_k4:.4f}")
    print(f"  max A²_Cos = {max_A_sq_cos:.4e}")
    print(f"  max |Q_H|   = {max_Q_hopf:.3e}")
    print(f"  final soliton centroids: {len(final_cosserat_centroids)}")
    print(f"  → VERDICT: {verdict}")

    return {
        "N": N, "amp_frac": amp, "V_SNAP": V_SNAP,
        "n_outer_steps": n_outer_steps,
        "history": history,
        "heatmap_frames": heatmap_frames,
        "max_A_sq_k4": max_A_sq_k4,
        "max_A_sq_cos": max_A_sq_cos,
        "max_Q_hopf": max_Q_hopf,
        "final_centroids": final_cosserat_centroids,
        "verdict": verdict,
    }


def render_summary_plot(result: dict, out: str) -> None:
    h = result["history"]
    t = np.array([hh["t"] for hh in h])

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    ax = axes[0, 0]
    ax.plot(t, [hh["max_A_sq_k4"] for hh in h], "-", label="max A²_K4 (photon)", lw=1.4, color="#f77")
    ax.plot(t, [hh["max_A_sq_cos"] for hh in h], "-", label="max A²_Cos (rotational)", lw=1.4, color="#47c")
    ax.plot(t, [hh["max_A_sq_total"] for hh in h], "--", label="max A²_total", lw=1.0, color="#aaa")
    ax.axhline(2.0 * ALPHA, color="yellow", lw=0.6, alpha=0.5, ls=":")
    ax.axhline(0.75, color="orange", lw=0.6, alpha=0.5, ls=":")
    ax.axhline(1.0, color="red", lw=0.8, alpha=0.5, ls=":")
    ax.set_yscale("log"); ax.set_xlabel("t"); ax.set_ylabel("A² peak")
    ax.set_title(f"Peak A² evolution\nverdict = {result['verdict']}")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axes[0, 1]
    ax.plot(t, [hh["E_k4"] for hh in h], "-", label="E_K4", lw=1.3)
    ax.plot(t, [hh["E_cos"] for hh in h], "-", label="E_cos (potential)", lw=1.3)
    ax.plot(t, [hh["T_cos"] for hh in h], "-", label="T_cos (kinetic)", lw=1.3)
    ax.plot(t, [hh["E_coupling"] for hh in h], "-", label="E_coupling", lw=1.3)
    ax.plot(t, [hh["src_cum_energy"] for hh in h], "-", label="src cumulative", lw=1.3, color="#f90")
    ax.set_yscale("log"); ax.set_xlabel("t"); ax.set_ylabel("energy")
    ax.set_title("Energy partition"); ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axes[1, 0]
    ax.plot(t, [hh["Q_hopf"] for hh in h], "-", color="#c33", lw=1.4, label="Q_H (Hopf)")
    ax.set_xlabel("t"); ax.set_ylabel("Q_H")
    ax.set_title(f"Topological charge (Hopf)  max|Q_H| = {result['max_Q_hopf']:.2e}")
    ax.legend(fontsize=8); ax.grid(alpha=0.3); ax.axhline(0, color="#666", lw=0.5)

    ax = axes[1, 1]
    ax.plot(t, [hh["max_V_sq"] for hh in h], "-", label="max V²", lw=1.3, color="#f77")
    ax.set_xlabel("t"); ax.set_ylabel("max V² on lattice")
    ax.set_title(f"Photon amplitude\npeak A²_K4 = {result['max_A_sq_k4']:.3f}")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    plt.suptitle(f"Phase III-A Null Control: single photon (amp={result['amp_frac']:.2f}·V_SNAP)", fontsize=12)
    plt.tight_layout()
    plt.savefig(out, dpi=110)
    plt.close()
    print(f"Saved {out}")


def render_animation(result: dict, out: str, fps: int = 10) -> None:
    """Animate A²_K4 / A²_Cos / A²_total side-by-side in the z=N/2 slice."""
    frames = result["heatmap_frames"]
    if not frames:
        print("  (no heatmap frames to animate)")
        return

    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    fig.patch.set_facecolor("#111")
    for ax in axes:
        ax.set_facecolor("#1a1a1a")
        ax.tick_params(colors="#ccc")

    # Shared vmax from full dataset
    vmax_k4 = max(f["A_sq_k4_slice"].max() for f in frames) * 1.05
    vmax_cos = max(f["A_sq_cos_slice"].max() for f in frames) * 1.05
    vmax_tot = max(f["A_sq_total_slice"].max() for f in frames) * 1.05
    vmax_cos = max(vmax_cos, 1e-5)
    vmax_k4 = max(vmax_k4, 1e-5)
    vmax_tot = max(vmax_tot, 1e-5)

    im_k4 = axes[0].imshow(frames[0]["A_sq_k4_slice"].T, origin="lower",
                             cmap="inferno", vmin=0, vmax=vmax_k4)
    im_cos = axes[1].imshow(frames[0]["A_sq_cos_slice"].T, origin="lower",
                              cmap="viridis", vmin=0, vmax=vmax_cos)
    im_tot = axes[2].imshow(frames[0]["A_sq_total_slice"].T, origin="lower",
                              cmap="magma", vmin=0, vmax=vmax_tot)
    axes[0].set_title("A²_K4 (photon)", color="#eee")
    axes[1].set_title(f"A²_Cos (rotational, max = {vmax_cos:.1e})", color="#eee")
    axes[2].set_title("A²_total", color="#eee")
    for ax in axes:
        ax.set_xlabel("x", color="#ccc"); ax.set_ylabel("y", color="#ccc")
    suptitle = fig.suptitle("", color="#eee", fontsize=12)

    def update(i):
        f = frames[i]
        im_k4.set_data(f["A_sq_k4_slice"].T)
        im_cos.set_data(f["A_sq_cos_slice"].T)
        im_tot.set_data(f["A_sq_total_slice"].T)
        suptitle.set_text(f"Phase III-A — t = {f['t']:.3f}   ({i+1}/{len(frames)})")
        return im_k4, im_cos, im_tot, suptitle

    anim = FuncAnimation(fig, update, frames=len(frames), interval=1000 / fps, blit=False)
    writer = PillowWriter(fps=fps)
    anim.save(out, writer=writer, savefig_kwargs={"facecolor": "#111"})
    plt.close()
    print(f"Saved {out}")


if __name__ == "__main__":
    result = run()

    render_summary_plot(result, out="/tmp/phase_iiia_summary.png")
    render_animation(result, out="/tmp/phase_iiia_self_saturation.gif")

    print("\n── Phase III-A Summary ──")
    print(json.dumps({
        "verdict": result["verdict"],
        "max_A_sq_k4": result["max_A_sq_k4"],
        "max_A_sq_cos": result["max_A_sq_cos"],
        "max_Q_hopf": result["max_Q_hopf"],
        "n_final_centroids": len(result["final_centroids"]),
    }, indent=2))

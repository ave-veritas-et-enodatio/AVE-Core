"""
Phase III-B — Two-photon collision → pair creation (MAIN EVENT).

Question
--------
Do two counter-propagating photons driving A² → 1 at a collision
region produce a (2,3) Cosserat soliton pair emergent from the vacuum?

Per §37 (node-saturation-Pauli mechanism): "Two photons collide
locally, drive A²=1 at two adjacent nodes, form electron+positron.
Threshold: 2 m_e c²."

Pre-registered predictions
--------------------------
  P_IIIb-pair:  Electron-positron pair formed.
      • max A²_Cosserat ≥ 0.5 in collision region
      • ≥2 soliton centroids detected post-collision
      • Q_H (globally) remains near 0 (e+ and e- contribute opposite)
      • Transmitted |V|² drops significantly (energy absorbed)
  P_IIIb-partial:  Cosserat excited but no stable structure
  P_IIIb-no-response:  Coupling too weak at given amplitudes

Parameter sweep: amp ∈ {0.5, 0.7, 0.95} · V_SNAP (V_SNAP = 1.0 natural)
                 wavelength: 6 cells (matches III-A)

AVE compliance
--------------
  S1 = D  coupling term (V²/V_SNAP²) · W_refl(u, ω)
  S4 = A  natural units: V_SNAP = 1.0
  S5 = B  unified leapfrog
  S6 = A  Q measured globally AND per-centroid
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

from ave.topological.k4_cosserat_coupling import CoupledK4Cosserat

from photon_propagation import PlaneSource
from saturation_heatmap import saturation_fields


def run_single(
    amp: float,
    N: int = 64,
    pml: int = 8,
    lambda_cells: float = 6.0,
    sigma_yz: float = 5.0,
    V_SNAP: float = 1.0,
    source_offset: int = 10,        # source_x = source_offset and N - source_offset
    n_outer_steps: int = 400,
    record_every: int = 5,
    vacuum_noise_amplitude: float = 0.01,   # ⟨|ω|²⟩₀ seed (AVE vacuum zero-point)
    noise_seed: int = 42,
) -> dict:
    """One two-photon collision run at the given amplitude.

    IMPORTANT (2026-04-22, per Grant's observation): AVE's vacuum is NEVER
    at (u, ω) = 0 identically. Axiom 1's LC resonant network has zero-point
    oscillations, so the physical vacuum has small but nonzero ⟨|ω|²⟩₀.
    Without this seed, the S1-D coupling (quadratic in (u, ω)) has zero
    force at the origin and cannot bootstrap pair creation. WITH this seed,
    the coupling can amplify vacuum fluctuations near collision regions.

    The vacuum_noise_amplitude parameter sets the RMS of the initial ω
    Gaussian noise. 0.01 is small enough that initial A²_Cos ≲ 1e-4
    (still in Regime I passband) but large enough that the coupling
    force is nonzero.
    """
    sim = CoupledK4Cosserat(N=N, pml=pml, V_SNAP=V_SNAP)

    # Seed vacuum with small random ω fluctuations (Axiom-1 zero-point analog)
    if vacuum_noise_amplitude > 0:
        rng = np.random.default_rng(noise_seed)
        noise = rng.standard_normal(sim.cos.omega.shape) * vacuum_noise_amplitude
        noise *= sim.cos.mask_alive[..., None]
        sim.cos.omega = noise.astype(sim.cos.omega.dtype)
    omega_carrier = 2.0 * np.pi * sim.k4.c / (lambda_cells * sim.k4.dx)
    period = 2.0 * np.pi / omega_carrier

    # Two photons, counter-propagating, arriving at x = N/2 at same time.
    # t_center: both pulses peak so their source-to-collision travel equals
    # the pulse center time. Travel time = (N/2 − source_offset) · dx / c.
    x_mid = N / 2
    travel = (x_mid - source_offset) * sim.k4.dx / sim.k4.c
    t_center_target = travel + 2.0 * period     # some delay for smooth ramp-up

    src_left = PlaneSource(
        x0=source_offset, y_c=(N - 1) / 2.0, z_c=(N - 1) / 2.0,
        direction=(1.0, 0.0, 0.0), sigma_yz=sigma_yz,
        omega=omega_carrier,
        t_center=t_center_target, t_sigma=0.5 * period,
        amplitude=amp,
    )
    src_right = PlaneSource(
        x0=N - source_offset, y_c=(N - 1) / 2.0, z_c=(N - 1) / 2.0,
        direction=(-1.0, 0.0, 0.0), sigma_yz=sigma_yz,
        omega=omega_carrier,
        t_center=t_center_target, t_sigma=0.5 * period,
        amplitude=amp,
    )

    history: list[dict] = []
    heatmap_frames: list[dict] = []

    print(f"  Running amp={amp:.2f}: N={N}, {n_outer_steps} outer steps, collision at t≈{t_center_target:.2f}")

    for step in range(n_outer_steps + 1):
        if step > 0:
            t = step * sim.outer_dt
            src_left.apply(sim.k4, t)
            src_right.apply(sim.k4, t)
            sim.step()

        if step % record_every == 0:
            snap = sim.snapshot_scalars()
            snap["Q_hopf"] = sim.cos.extract_hopf_charge()
            snap["src_cum_energy"] = src_left.cumulative_energy_injected + src_right.cumulative_energy_injected
            snap["centroids"] = sim.cos.find_soliton_centroids(threshold_frac=0.3)
            history.append(snap)

            if step % (record_every * 2) == 0:
                fields = saturation_fields(sim)
                heatmap_frames.append({
                    "t": sim.time,
                    "A_sq_k4_slice": fields["A_sq_k4"][:, :, N // 2].copy(),
                    "A_sq_cos_slice": fields["A_sq_cos"][:, :, N // 2].copy(),
                    "A_sq_total_slice": fields["A_sq_total"][:, :, N // 2].copy(),
                    "omega_mag_slice": np.sqrt(np.sum(sim.cos.omega[:, :, N//2, :]**2, axis=-1)).copy(),
                    "n_centroids": len(snap["centroids"]),
                })

    # ── Verdict ──
    max_A_sq_cos = max(h["max_A_sq_cos"] for h in history)
    max_A_sq_total = max(h["max_A_sq_total"] for h in history)
    max_Q_hopf = max(abs(h["Q_hopf"]) for h in history)
    max_n_centroids = max(len(h["centroids"]) for h in history)

    # final (post-collision, with some delay)
    final_centroids = history[-1]["centroids"]

    # Adjudicate
    if max_A_sq_cos >= 0.5 and max_n_centroids >= 2:
        verdict = "P_IIIb-pair"
    elif max_A_sq_cos > 0.01:
        verdict = "P_IIIb-partial"
    else:
        verdict = "P_IIIb-no-response"

    print(f"    max A²_total = {max_A_sq_total:.3f}, max A²_cos = {max_A_sq_cos:.3e}")
    print(f"    max |Q_H| = {max_Q_hopf:.3e}, peak #centroids = {max_n_centroids}")
    print(f"    → VERDICT: {verdict}")

    return {
        "amp": amp, "N": N, "n_outer_steps": n_outer_steps,
        "history": history,
        "heatmap_frames": heatmap_frames,
        "max_A_sq_total": max_A_sq_total,
        "max_A_sq_cos": max_A_sq_cos,
        "max_Q_hopf": max_Q_hopf,
        "max_n_centroids": max_n_centroids,
        "final_centroids": final_centroids,
        "verdict": verdict,
    }


def render_summary(results: list[dict], out: str) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))
    colors = ["#47c", "#f90", "#c33"]

    ax = axes[0, 0]
    for r, c in zip(results, colors):
        t = np.array([h["t"] for h in r["history"]])
        ax.plot(t, [h["max_A_sq_total"] for h in r["history"]], "-",
                color=c, lw=1.4, label=f"amp={r['amp']:.2f}: {r['verdict']}")
    ax.axhline(1.0, color="red", lw=0.8, ls=":", label="A²=1 (TIR)")
    ax.axhline(0.75, color="orange", lw=0.6, ls=":")
    ax.set_yscale("log"); ax.set_xlabel("t"); ax.set_ylabel("max A²_total")
    ax.set_title("Collision A² evolution (all amps)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axes[0, 1]
    for r, c in zip(results, colors):
        t = np.array([h["t"] for h in r["history"]])
        ax.plot(t, [h["max_A_sq_cos"] for h in r["history"]], "-",
                color=c, lw=1.4, label=f"amp={r['amp']:.2f}")
    ax.axhline(0.5, color="green", lw=0.6, ls=":", label="P_IIIb-pair threshold")
    ax.set_yscale("symlog", linthresh=1e-8)
    ax.set_xlabel("t"); ax.set_ylabel("max A²_Cosserat")
    ax.set_title("Cosserat response")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axes[1, 0]
    for r, c in zip(results, colors):
        t = np.array([h["t"] for h in r["history"]])
        ax.plot(t, [len(h["centroids"]) for h in r["history"]], "-",
                color=c, lw=1.4, label=f"amp={r['amp']:.2f}")
    ax.axhline(2, color="green", lw=0.8, ls="--", label="pair threshold")
    ax.set_xlabel("t"); ax.set_ylabel("# soliton centroids")
    ax.set_title("Detected soliton count")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    ax = axes[1, 1]
    for r, c in zip(results, colors):
        t = np.array([h["t"] for h in r["history"]])
        ax.plot(t, [h["Q_hopf"] for h in r["history"]], "-",
                color=c, lw=1.4, label=f"amp={r['amp']:.2f}")
    ax.axhline(0, color="#666", lw=0.5)
    ax.set_xlabel("t"); ax.set_ylabel("Q_H (global)")
    ax.set_title("Global topological charge")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    plt.suptitle("Phase III-B: Two-Photon Collision → Pair Creation (amplitude sweep)", fontsize=12)
    plt.tight_layout()
    plt.savefig(out, dpi=110)
    plt.close()
    print(f"Saved {out}")


def render_animation(result: dict, out: str, fps: int = 10) -> None:
    """Animate the primary (highest-amp) run's collision dynamics."""
    frames = result["heatmap_frames"]
    if not frames:
        return

    fig, axes = plt.subplots(2, 2, figsize=(13, 10))
    fig.patch.set_facecolor("#111")
    for ax in axes.ravel():
        ax.set_facecolor("#1a1a1a")
        ax.tick_params(colors="#ccc")

    vmax_k4 = max(f["A_sq_k4_slice"].max() for f in frames) * 1.05
    vmax_cos = max(f["A_sq_cos_slice"].max() for f in frames) * 1.05
    vmax_tot = max(f["A_sq_total_slice"].max() for f in frames) * 1.05
    vmax_om = max(f["omega_mag_slice"].max() for f in frames) * 1.05
    for v in (vmax_k4, vmax_cos, vmax_tot, vmax_om):
        v = max(v, 1e-4)

    im_k4 = axes[0, 0].imshow(frames[0]["A_sq_k4_slice"].T, origin="lower",
                                cmap="inferno", vmin=0, vmax=max(vmax_k4, 1e-4))
    im_cos = axes[0, 1].imshow(frames[0]["A_sq_cos_slice"].T, origin="lower",
                                 cmap="viridis", vmin=0, vmax=max(vmax_cos, 1e-4))
    im_tot = axes[1, 0].imshow(frames[0]["A_sq_total_slice"].T, origin="lower",
                                 cmap="magma", vmin=0, vmax=max(vmax_tot, 1e-4))
    im_om = axes[1, 1].imshow(frames[0]["omega_mag_slice"].T, origin="lower",
                                cmap="plasma", vmin=0, vmax=max(vmax_om, 1e-4))
    axes[0, 0].set_title("A²_K4 (two photons)", color="#eee")
    axes[0, 1].set_title("A²_Cos (rotational)", color="#eee")
    axes[1, 0].set_title("A²_total (TIR when → 1)", color="#eee")
    axes[1, 1].set_title("|ω| (soliton structure)", color="#eee")
    for ax in axes.ravel():
        ax.set_xlabel("x", color="#ccc"); ax.set_ylabel("y", color="#ccc")
    suptitle = fig.suptitle("", color="#eee", fontsize=12)

    def update(i):
        f = frames[i]
        im_k4.set_data(f["A_sq_k4_slice"].T)
        im_cos.set_data(f["A_sq_cos_slice"].T)
        im_tot.set_data(f["A_sq_total_slice"].T)
        im_om.set_data(f["omega_mag_slice"].T)
        suptitle.set_text(
            f"Phase III-B (amp={result['amp']:.2f}·V_SNAP) — t = {f['t']:.3f}  "
            f"#centroids = {f['n_centroids']}"
        )
        return im_k4, im_cos, im_tot, im_om, suptitle

    anim = FuncAnimation(fig, update, frames=len(frames), interval=1000 / fps, blit=False)
    writer = PillowWriter(fps=fps)
    anim.save(out, writer=writer, savefig_kwargs={"facecolor": "#111"})
    plt.close()
    print(f"Saved {out}")


if __name__ == "__main__":
    print("── Phase III-B: Two-photon collision → pair creation ──\n")

    results = []
    # Quick-pass: N=48, 200 steps, 2 amps to verify vacuum-noise seed
    # unlocks the bootstrapping. If it does, rerun at N=64 production.
    for amp in [0.7, 0.95]:
        r = run_single(amp=amp, N=48, n_outer_steps=200,
                       vacuum_noise_amplitude=0.01)
        results.append(r)

    render_summary(results, out="/tmp/phase_iiib_summary.png")
    # Animate the highest-amp run
    render_animation(results[-1], out="/tmp/phase_iiib_pair_creation.gif")

    print("\n── Phase III-B Overall Summary ──")
    for r in results:
        print(f"  amp={r['amp']:.2f}: {r['verdict']}   "
              f"max_A²_cos={r['max_A_sq_cos']:.3e}, "
              f"peak #centroids={r['max_n_centroids']}")

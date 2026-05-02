"""
test_lattice_layer_1_dispersion.py
=====================================

Layer 1 emergence test — substrate dispersion (cardinal-axis verification +
diagonal infrastructure-pending caveat).

Per doc 108 §3 Layer 1: verify that the K4 substrate's wavefront velocity
along the cardinal axis EMERGES from K4 geometry alone (no α, m_e, or
other CODATA inputs in the velocity-extraction chain).

PHASE 1 SCOPE (this test): cardinal-axis emergence only. Reuses the
plane-source wave-packet infrastructure in `photon_propagation.py` which
correctly measures group velocity via peak-arrival between two reference
planes (per Phase A.1 finding, 2026-05-01).

DIAGONAL EMERGENCE: requires tilted-source plane infrastructure that
doesn't currently exist. Marked as INFRASTRUCTURE-PENDING per A47 v18
honest scope. A point-source approach would naively test diagonal
arrivals, but the K4 bipartite hopping graph doesn't propagate cleanly
along arbitrary (1,1,1)-line cells — only along port direction one-hop.

Pre-registered acceptance criteria (verbatim per A47 v11b):

  C-L1.1: cardinal-axis wavefront velocity v/c ∈ [1.35, 1.50]
          Closed-form prediction: √2 ≈ 1.4142 (K4 substrate anisotropy)
          Empirical reproduction of Phase A.1 finding (2026-05-01: 1.450)

  C-L1.2: diagonal-axis emergence — INFRASTRUCTURE-PENDING (deferred to
          Phase 1.5 follow-up driver with tilted source plane).

  C-L1.3: anisotropy ratio test deferred until both directions measurable.

If C-L1.1 PASSES: K4 cardinal-axis anisotropy emerges from lattice
geometry alone (no α/m_e inputs). Phase A.1 finding is reproducible
from clean-room test setup.

Outputs:
  - assets/lattice_layer1_dispersion_panels.png
  - results/lattice_layer1_dispersion.json
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from ave.core.k4_tlm import K4Lattice3D


PREREG = {
    "C-L1.1_v_cardinal_over_c_min": 1.35,
    "C-L1.1_v_cardinal_over_c_max": 1.50,
    "C-L1.1_target_value": float(np.sqrt(2.0)),
    "C-L1.2_diagonal_status": "INFRASTRUCTURE_PENDING",
    "C-L1.3_anisotropy_status": "DEFERRED_PENDING_C_L1_2",
}


def run_cardinal_dispersion(N: int = 96, n_steps: int = 240,
                              lambda_cells: float = 10.0,
                              amp_frac: float = 0.001) -> dict:
    """Plane-source wave packet along +x̂; measure peak-arrival velocity.

    This mirrors photon_propagation.py's run_validation() approach (per
    Phase A.1, which empirically gave v = 1.450·c at this configuration)
    but kept self-contained here for the emergence-test framing.

    All inputs are K4 substrate geometry + raw forward-port weights (NO
    T₂ projection, NO CODATA-derived constants in the velocity extraction
    chain). The c-ratio result is dimensionless and emerges from the
    K4 lattice's intrinsic dynamics.
    """
    lattice = K4Lattice3D(N, N, N, dx=1.0, nonlinear=False, pml_thickness=8)
    dt = lattice.dt
    c = lattice.c

    # Carrier frequency for the wave packet
    omega = 2.0 * np.pi * c / (lambda_cells * lattice.dx)
    period = 2.0 * np.pi / omega
    t_sigma_periods = 0.75
    t_sigma = t_sigma_periods * period
    t_center = 3.0 * t_sigma

    # Source amplitude (linear regime — well below V_yield by amp_frac)
    # Use a small amplitude; emergence test is dimensionless ratio
    # (we only care about v/c, not absolute amplitude)
    src_x = 16  # just inside PML
    cy, cz = (N - 1) / 2.0, (N - 1) / 2.0
    sigma_yz = 8.0

    # Forward-port weights (raw, no T₂ projection — measures the substrate
    # wavefront, not the photon T₂ mode specifically)
    direction = np.array([1.0, 0.0, 0.0])
    PORT_HAT = np.array([
        [+1, +1, +1], [+1, -1, -1], [-1, +1, -1], [-1, -1, +1],
    ], dtype=float) / np.sqrt(3.0)
    port_w = np.maximum(0.0, -PORT_HAT @ direction)
    if port_w.sum() > 0:
        port_w = port_w / port_w.sum()

    print(f"  Cardinal dispersion: N={N}, n_steps={n_steps}, λ={lambda_cells} cells")
    print(f"    src_x={src_x}, port_w={port_w}, dt={dt:.3e}")

    # Inject + record per Phase A.1 plane-source approach
    z_slice = N // 2
    frames: list[np.ndarray] = []
    times: list[float] = []

    j_idx, k_idx = np.indices((N, N), dtype=float)
    yz_profile = np.exp(
        -((j_idx - cy) ** 2 + (k_idx - cz) ** 2) / (2.0 * sigma_yz ** 2)
    )
    active_slice = lattice.mask_active[src_x]

    for step in range(1, n_steps + 1):
        t = step * dt
        env = np.exp(-((t - t_center) / t_sigma) ** 2)
        osc = np.sin(omega * (t - t_center))
        A_t = amp_frac * env * osc
        if abs(A_t) > 1e-30:
            injection = A_t * yz_profile * active_slice.astype(float)
            for n in range(4):
                if port_w[n] != 0:
                    lattice.V_inc[src_x, :, :, n] += port_w[n] * injection
        lattice.step()
        if step % 3 == 0:
            rho = lattice.get_energy_density()
            frames.append(rho[:, :, z_slice].copy())
            times.append(lattice.timestep * dt)

    frames_arr = np.stack(frames, axis=0)
    times_arr = np.asarray(times)

    # Peak-arrival measurement at two reference planes
    x_a, x_b = src_x + 20, src_x + 60
    rho_hist_a = np.array([frames_arr[i, x_a, :].sum() for i in range(len(frames_arr))])
    rho_hist_b = np.array([frames_arr[i, x_b, :].sum() for i in range(len(frames_arr))])

    def peak_arrival_time(series):
        if series.max() <= 0.0:
            return None
        idx = int(np.argmax(series))
        return float(times_arr[idx])

    t_a = peak_arrival_time(rho_hist_a)
    t_b = peak_arrival_time(rho_hist_b)
    if t_a is not None and t_b is not None and t_b > t_a:
        v_meas = (x_b - x_a) * lattice.dx / (t_b - t_a)
    else:
        v_meas = 0.0

    return {
        "N": N,
        "n_steps": n_steps,
        "lambda_cells": lambda_cells,
        "amp_frac": amp_frac,
        "src_x": src_x,
        "x_a": x_a,
        "x_b": x_b,
        "t_a_s": float(t_a) if t_a else 0.0,
        "t_b_s": float(t_b) if t_b else 0.0,
        "v_meas_mps": float(v_meas),
        "v_cardinal_over_c": float(v_meas / c) if c > 0 else 0.0,
        "frames": frames_arr,
        "times": times_arr,
        "rho_hist_a": rho_hist_a,
        "rho_hist_b": rho_hist_b,
    }


def evaluate_prereg(result: dict) -> dict:
    """Evaluate Layer 1 emergence criteria."""
    eval_result = {}
    eval_result["v_cardinal_over_c"] = result["v_cardinal_over_c"]
    eval_result["sqrt_2_target"] = float(np.sqrt(2.0))

    # C-L1.1: cardinal velocity emergence
    eval_result["pass_C_L1_1"] = (
        PREREG["C-L1.1_v_cardinal_over_c_min"]
        <= result["v_cardinal_over_c"]
        <= PREREG["C-L1.1_v_cardinal_over_c_max"]
    )

    # C-L1.2 + L1.3: deferred per A47 v18 honest scope
    eval_result["C_L1_2_status"] = "INFRASTRUCTURE_PENDING"
    eval_result["C_L1_3_status"] = "DEFERRED"

    eval_result["all_pass_at_phase_1_scope"] = eval_result["pass_C_L1_1"]
    return eval_result


def render_panels(result: dict, eval_result: dict, out_png: str) -> None:
    fig = plt.figure(figsize=(15, 10), facecolor="#050510")
    gs = GridSpec(2, 2, figure=fig, hspace=0.32, wspace=0.20)

    # Panel 0: |V|² spacetime
    ax = fig.add_subplot(gs[0, 0])
    ax.set_facecolor("#050510")
    frames = result["frames"]
    times = result["times"]
    extent = [0, result["N"], times[-1] * 1e9, 0]
    im = ax.imshow(frames.sum(axis=2), aspect="auto", cmap="hot", extent=extent)
    ax.axvline(result["src_x"], color="cyan", lw=1, ls="--", label=f"src x={result['src_x']}")
    ax.axvline(result["x_a"], color="lime", lw=1, ls=":", label=f"x_a={result['x_a']}")
    ax.axvline(result["x_b"], color="orange", lw=1, ls=":", label=f"x_b={result['x_b']}")
    ax.set_xlabel("x (cells)", color="#cccccc", fontsize=9)
    ax.set_ylabel("t (ns)", color="#cccccc", fontsize=9)
    ax.set_title("Energy density |V|² spacetime (cardinal axis +x̂)",
                 color="white", fontsize=10)
    plt.colorbar(im, ax=ax, fraction=0.04)
    ax.legend(facecolor="#050510", edgecolor="#444",
              labelcolor="#cccccc", fontsize=8)
    ax.tick_params(colors="#cccccc", labelsize=8)

    # Panel 1: Peak arrival at x_a and x_b
    ax = fig.add_subplot(gs[0, 1])
    ax.set_facecolor("#050510")
    ax.plot(np.array(times) * 1e9, result["rho_hist_a"], "-",
            color="lime", lw=1.4, label=f"|V|² at x_a={result['x_a']}")
    ax.plot(np.array(times) * 1e9, result["rho_hist_b"], "-",
            color="orange", lw=1.4, label=f"|V|² at x_b={result['x_b']}")
    ax.axvline(result["t_a_s"] * 1e9, color="lime", ls=":", lw=1)
    ax.axvline(result["t_b_s"] * 1e9, color="orange", ls=":", lw=1)
    ax.set_xlabel("t (ns)", color="#cccccc", fontsize=9)
    ax.set_ylabel("|V|² at reference plane", color="#cccccc", fontsize=9)
    ax.set_title(
        f"Peak-arrival times: t_a={result['t_a_s']*1e9:.2f} ns, "
        f"t_b={result['t_b_s']*1e9:.2f} ns",
        color="white", fontsize=10,
    )
    ax.legend(facecolor="#050510", edgecolor="#444",
              labelcolor="#cccccc", fontsize=8)
    ax.tick_params(colors="#cccccc", labelsize=8)
    ax.grid(alpha=0.2, color="#444")

    # Panel 2: cardinal velocity bar
    ax = fig.add_subplot(gs[1, 0])
    ax.set_facecolor("#050510")
    v = result["v_cardinal_over_c"]
    bar = ax.bar(["cardinal\n(+x̂)"], [v], color="#aaff77", edgecolor="white")
    ax.axhline(np.sqrt(2.0), color="orange", ls="--", lw=1.5,
               label=f"√2 target = {np.sqrt(2.0):.4f}")
    ax.axhline(1.0, color="green", ls=":", lw=1, label="c (continuum target)")
    ax.text(0, v + 0.04, f"{v:.4f}", ha="center", color="white", fontsize=12)
    ax.set_ylim(0, max(v * 1.2, 1.7))
    ax.set_ylabel("v / c", color="#cccccc", fontsize=10)
    ax.set_title(
        f"Cardinal-axis velocity emergence\n"
        f"v/c = {v:.4f}  vs  √2 = {np.sqrt(2.0):.4f}\n"
        f"{'✓ PASS C-L1.1' if eval_result['pass_C_L1_1'] else '✗ FAIL C-L1.1'}",
        color="white", fontsize=10,
    )
    ax.legend(facecolor="#050510", edgecolor="#444",
              labelcolor="#cccccc", fontsize=9)
    ax.tick_params(colors="#cccccc", labelsize=8)
    ax.grid(alpha=0.2, color="#444", axis="y")

    # Panel 3: pre-reg verdict
    ax = fig.add_subplot(gs[1, 1])
    ax.set_facecolor("#050510")
    ax.axis("off")
    summary_lines = [
        "Pre-reg evaluation (per doc 108 §3 Layer 1, Phase 1 scope):",
        "",
        f"C-L1.1 (cardinal v/c emergence):",
        f"   measured = {result['v_cardinal_over_c']:.4f}",
        f"   range    ∈ [1.35, 1.50]",
        f"   target   = √2 ≈ {np.sqrt(2.0):.4f}",
        f"   verdict  = {'✓ PASS' if eval_result['pass_C_L1_1'] else '✗ FAIL'}",
        "",
        f"C-L1.2 (diagonal emergence):    INFRASTRUCTURE-PENDING",
        f"   Requires tilted-source plane perpendicular to (1,1,1)/√3.",
        f"   Naive point-source approach doesn't propagate cleanly",
        f"   along arbitrary diagonal cells in K4 bipartite graph.",
        "",
        f"C-L1.3 (anisotropy ratio):      DEFERRED until C-L1.2 lands.",
        "",
        f"OVERALL Phase 1 scope: "
        f"{'✓ PASS' if eval_result['all_pass_at_phase_1_scope'] else '✗ FAIL'}",
        "",
        "Inputs: K4 4-port geometry + raw-forward port weights only.",
        "NO CODATA inputs in v/c extraction (just dimensionless ratio",
        "from t_a, t_b, x_a, x_b — all in lattice cells / engine seconds).",
    ]
    for i, line in enumerate(summary_lines):
        if "PASS" in line:
            color = "#aaff77"
        elif "FAIL" in line:
            color = "#ffaaaa"
        elif "PENDING" in line or "DEFERRED" in line:
            color = "#ffaa44"
        else:
            color = "#cccccc"
        ax.text(0.02, 0.95 - i * 0.045, line, transform=ax.transAxes,
                color=color, fontsize=9, family="monospace")

    fig.suptitle(
        "Layer 1 Emergence (Phase 1): Cardinal-Axis Wavefront Velocity\n"
        "doc 108 §3 Layer 1 — K4 substrate anisotropy from geometry alone",
        color="white", fontsize=12, fontweight="bold",
    )
    plt.savefig(out_png, dpi=110, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent.parent.parent
    assets_dir = repo_root / "assets"
    results_dir = repo_root / "results"
    assets_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 72)
    print("Layer 1 Emergence (Phase 1) — Cardinal-Axis Dispersion")
    print("=" * 72)

    result = run_cardinal_dispersion()

    print(f"\n  v_cardinal / c = {result['v_cardinal_over_c']:.4f}")
    print(f"  closed-form target √2 = {np.sqrt(2.0):.4f}")

    eval_result = evaluate_prereg(result)

    print(f"\n── Pre-reg evaluation ──")
    print(f"  C-L1.1 (cardinal v/c ∈ [1.35, 1.50]): "
          f"{'PASS' if eval_result['pass_C_L1_1'] else 'FAIL'}  "
          f"(got {result['v_cardinal_over_c']:.4f})")
    print(f"  C-L1.2 (diagonal):                   INFRASTRUCTURE_PENDING")
    print(f"  C-L1.3 (anisotropy):                 DEFERRED")
    print(f"  Overall Phase 1 scope:               "
          f"{'PASS' if eval_result['all_pass_at_phase_1_scope'] else 'FAIL'}")

    out_png = assets_dir / "lattice_layer1_dispersion_panels.png"
    render_panels(result, eval_result, str(out_png))

    out_json = results_dir / "lattice_layer1_dispersion.json"
    # Strip arrays for JSON
    result_serial = {
        k: (v.tolist() if isinstance(v, np.ndarray) else v)
        for k, v in result.items()
        if k not in ("frames",)  # frames too large
    }
    with open(out_json, "w") as f:
        json.dump(
            {"prereg": PREREG, "eval": eval_result, "result": result_serial},
            f, indent=2, default=str,
        )

    print(f"\n  Outputs:")
    print(f"    {out_png}")
    print(f"    {out_json}")


if __name__ == "__main__":
    main()

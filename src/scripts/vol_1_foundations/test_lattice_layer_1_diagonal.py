"""
test_lattice_layer_1_diagonal.py
===================================

Phase 1.5: tilted-source diagonal velocity emergence (completes L1).

Per doc 108 §11.5 Phase 1.5 plan: launch wave with tilted source plane
perpendicular to (1,1,1)/√3, measure peak-arrival velocity along the
(1,1,1) propagation axis. Closes C-L1.2 + C-L1.3 from doc 108 §3 Layer 1.

Per docstring of `photon_propagation.py:35-42`, the K4 substrate's
diagonal-axis (port direction) wave should propagate at v=c. Combined
with the cardinal-axis result (v=√2·c per Phase 1 Layer 1), this would
verify the K4 anisotropy ratio v_card/v_diag = √2 emerges from
substrate geometry alone.

Pre-registered acceptance criteria:
  C-L1.2: diagonal-axis (port direction) v/c ∈ [0.85, 1.15]  (target c)
  C-L1.3: anisotropy ratio v_cardinal/v_diagonal ∈ [1.30, 1.55]  (target √2)

Tilted-source-plane construction:
  - Source slab defined by `x + y + z = s0` (plane normal to (1,1,1)/√3)
  - For active K4 cells (parity all-even or all-odd), x+y+z is either even
    or odd depending on parity. Both A and B sublattices contribute.
  - Inject Gaussian wave packet at this slab; port_w aligned with port 0
    direction (1,1,1)/√3 to drive forward propagation along the diagonal.
  - Reference planes at `x+y+z = s_a` and `x+y+z = s_b` for peak-arrival.

Outputs:
  - assets/lattice_layer1_diagonal_panels.png
  - results/lattice_layer1_diagonal.json
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
    "C-L1.2_v_diagonal_over_c_min": 0.85,
    "C-L1.2_v_diagonal_over_c_max": 1.15,
    "C-L1.2_target_value": 1.0,
    "C-L1.3_anisotropy_ratio_min": 1.30,
    "C-L1.3_anisotropy_ratio_max": 1.55,
    "C-L1.3_target_value": float(np.sqrt(2.0)),
    "v_cardinal_over_c_phase_1": 1.4505,  # measured Phase 1 Layer 1 cardinal
}


def run_diagonal_dispersion(N: int = 96, n_steps: int = 240,
                              lambda_cells: float = 10.0,
                              amp_frac: float = 0.001) -> dict:
    """Tilted-plane wave packet propagating along (1,1,1)/√3 direction.

    Source plane: cells satisfying x+y+z = s0 (perpendicular to (1,1,1)).
    Reference planes for peak-arrival measurement: x+y+z = s_a, s_b.
    """
    lattice = K4Lattice3D(N, N, N, dx=1.0, nonlinear=False, pml_thickness=8)
    dt = lattice.dt
    c = lattice.c

    omega = 2.0 * np.pi * c / (lambda_cells * lattice.dx)
    period = 2.0 * np.pi / omega
    t_sigma = 0.75 * period
    t_center = 3.0 * t_sigma

    # Plane index along (1,1,1)/√3 (the "diagonal coordinate")
    # u = (x+y+z)·(1/√3) = projected position onto (1,1,1)/√3
    # u in lattice cells units: (x+y+z)/√3 ; range 0..3·N/√3 = N·√3
    # For source plane: pick s0 ≈ N/2 (centered), thickness ±half_width
    # Reference planes at s_a = s0 + 30·√3 cells, s_b = s0 + 60·√3 cells (along (1,1,1)/√3)
    # s = x+y+z, in raw integer units, so s_a, s_b are integers
    s0 = int(round(0.30 * (3 * N)))   # source slab at u ≈ 0.30·N·√3
    s_a = s0 + 30                      # 30/√3 ≈ 17.3 cells along (1,1,1)/√3
    s_b = s0 + 60                      # 60/√3 ≈ 34.6 cells along (1,1,1)/√3
    src_thickness = 2

    # Indices of all lattice cells
    i, j, k = np.indices((N, N, N))
    s_field = i + j + k

    src_mask = np.abs(s_field - s0) <= src_thickness
    src_active_mask = src_mask & lattice.mask_active

    print(f"  Diagonal dispersion: N={N}, n_steps={n_steps}, λ={lambda_cells} cells")
    print(f"    source slab: x+y+z ∈ [{s0-src_thickness}, {s0+src_thickness}] (s0={s0})")
    print(f"    reference planes: s_a = {s_a}, s_b = {s_b}")
    print(f"    source-active cells: {int(src_active_mask.sum())}")

    # Port weights aligned with (1,1,1)/√3 forward direction
    direction = np.array([1.0, 1.0, 1.0]) / np.sqrt(3.0)
    PORT_HAT = np.array([
        [+1, +1, +1], [+1, -1, -1], [-1, +1, -1], [-1, -1, +1],
    ], dtype=float) / np.sqrt(3.0)
    # forward port weights = max(0, -d̂·p̂) where d̂ is propagation direction
    # For propagation along (1,1,1)/√3, ports whose -p̂ component along (1,1,1) > 0
    # are the "forward" ports. -p̂_n · d̂ = -p̂_n · (1,1,1)/√3 = -(sum of p̂_n components)/√3
    # For port 0 (1,1,1)/√3: -p̂·d̂ = -1.0 (backward) → not forward
    # For port 1 (1,-1,-1)/√3: -p̂·d̂ = -((1-1-1)/3) = +1/3 → weight 1/3
    # For port 2 (-1,1,-1)/√3: -p̂·d̂ = -((-1+1-1)/3) = +1/3
    # For port 3 (-1,-1,1)/√3: -p̂·d̂ = -((-1-1+1)/3) = +1/3
    # So forward ports for (1,1,1)/√3 propagation are ports 1, 2, 3 (each weight 1/3)
    port_w_raw = np.maximum(0.0, -PORT_HAT @ direction)
    if port_w_raw.sum() > 0:
        port_w_raw = port_w_raw / port_w_raw.sum()
    # T₂ projection: subtract A₁ (mean) component to suppress longitudinal mode
    port_w = port_w_raw - port_w_raw.mean()
    norm = np.sqrt((port_w * port_w).sum())
    if norm > 0:
        port_w = port_w / norm  # unit T₂ amplitude
    print(f"    port_w (raw)         = {port_w_raw}")
    print(f"    port_w (T₂ projected) = {port_w}, Σw = {port_w.sum():+.6f}")

    # Run simulation; record |V|² at reference planes per timestep
    # Reference plane masks
    ref_a_mask = (np.abs(s_field - s_a) <= 1) & lattice.mask_active
    ref_b_mask = (np.abs(s_field - s_b) <= 1) & lattice.mask_active

    times = []
    rho_a_history = []
    rho_b_history = []

    # Track max along axis for visualization
    rho_axis_history = []  # |V|² vs s coordinate vs time

    for step in range(1, n_steps + 1):
        t = step * dt
        env = np.exp(-((t - t_center) / t_sigma) ** 2)
        osc = np.sin(omega * (t - t_center))
        A_t = amp_frac * env * osc
        if abs(A_t) > 1e-30:
            # Inject at source-active cells, port_w pattern
            for n in range(4):
                if port_w[n] != 0:
                    lattice.V_inc[..., n][src_active_mask] += port_w[n] * A_t
        lattice.step()

        if step % 3 == 0:
            rho = lattice.get_energy_density()
            rho_a_total = float(rho[ref_a_mask].sum())
            rho_b_total = float(rho[ref_b_mask].sum())
            rho_a_history.append(rho_a_total)
            rho_b_history.append(rho_b_total)
            times.append(lattice.timestep * dt)

            # Bin |V|² by s coordinate to visualize wavefront
            s_bins = np.arange(N // 4, 3 * N // 4 + 1)
            binned = np.zeros(len(s_bins))
            for idx, s_val in enumerate(s_bins):
                mask_s = (s_field == s_val) & lattice.mask_active
                binned[idx] = float(rho[mask_s].sum())
            rho_axis_history.append(binned)

    times_arr = np.asarray(times)
    rho_a_arr = np.asarray(rho_a_history)
    rho_b_arr = np.asarray(rho_b_history)

    def peak_arrival_time(series):
        if series.max() <= 0.0:
            return None
        idx = int(np.argmax(series))
        return float(times_arr[idx])

    t_a = peak_arrival_time(rho_a_arr)
    t_b = peak_arrival_time(rho_b_arr)

    # Distance between reference planes ALONG (1,1,1)/√3 propagation axis
    # In integer s = x+y+z units, distance = (s_b - s_a)
    # Converting to physical distance along (1,1,1)/√3: distance = (s_b - s_a) / √3 cells
    if t_a is not None and t_b is not None and t_b > t_a:
        distance_along_diag = (s_b - s_a) * lattice.dx / np.sqrt(3.0)
        v_meas = distance_along_diag / (t_b - t_a)
    else:
        v_meas = 0.0

    return {
        "N": N,
        "n_steps": n_steps,
        "lambda_cells": lambda_cells,
        "amp_frac": amp_frac,
        "s0": s0, "s_a": s_a, "s_b": s_b,
        "src_thickness": src_thickness,
        "t_a_s": float(t_a) if t_a else 0.0,
        "t_b_s": float(t_b) if t_b else 0.0,
        "distance_along_diag_m": (s_b - s_a) * lattice.dx / np.sqrt(3.0),
        "v_diagonal_mps": float(v_meas),
        "v_diagonal_over_c": float(v_meas / c) if c > 0 else 0.0,
        "rho_a_history": rho_a_arr.tolist(),
        "rho_b_history": rho_b_arr.tolist(),
        "rho_axis_history": np.stack(rho_axis_history) if rho_axis_history else np.zeros((0, 0)),
        "times": times_arr.tolist(),
        "port_w": port_w.tolist(),
    }


def evaluate_prereg(result: dict) -> dict:
    eval_result = {}
    eval_result["v_diagonal_over_c"] = result["v_diagonal_over_c"]
    eval_result["v_cardinal_over_c"] = PREREG["v_cardinal_over_c_phase_1"]
    eval_result["anisotropy_ratio"] = (
        eval_result["v_cardinal_over_c"] / eval_result["v_diagonal_over_c"]
        if eval_result["v_diagonal_over_c"] > 0 else 0.0
    )

    eval_result["pass_C_L1_2"] = (
        PREREG["C-L1.2_v_diagonal_over_c_min"]
        <= result["v_diagonal_over_c"]
        <= PREREG["C-L1.2_v_diagonal_over_c_max"]
    )
    eval_result["pass_C_L1_3"] = (
        PREREG["C-L1.3_anisotropy_ratio_min"]
        <= eval_result["anisotropy_ratio"]
        <= PREREG["C-L1.3_anisotropy_ratio_max"]
    )
    eval_result["all_pass"] = eval_result["pass_C_L1_2"] and eval_result["pass_C_L1_3"]
    return eval_result


def render_panels(result: dict, eval_result: dict, out_png: str) -> None:
    fig = plt.figure(figsize=(15, 10), facecolor="#050510")
    gs = GridSpec(2, 2, figure=fig, hspace=0.32, wspace=0.20)

    # Panel 0: |V|² spacetime along (1,1,1)/√3 axis
    ax = fig.add_subplot(gs[0, 0])
    ax.set_facecolor("#050510")
    rho_axis_h = np.asarray(result["rho_axis_history"])
    if rho_axis_h.size > 0:
        times = np.asarray(result["times"]) * 1e9
        s_bins = np.arange(result["N"] // 4, 3 * result["N"] // 4 + 1)
        extent = [s_bins[0], s_bins[-1], times[-1], 0]
        im = ax.imshow(rho_axis_h, aspect="auto", cmap="hot", extent=extent)
        ax.axvline(result["s0"], color="cyan", lw=1, ls="--", label=f"src s={result['s0']}")
        ax.axvline(result["s_a"], color="lime", lw=1, ls=":", label=f"s_a={result['s_a']}")
        ax.axvline(result["s_b"], color="orange", lw=1, ls=":", label=f"s_b={result['s_b']}")
        plt.colorbar(im, ax=ax, fraction=0.04)
    ax.set_xlabel("s = x+y+z (diagonal coordinate)", color="#cccccc", fontsize=9)
    ax.set_ylabel("t (ns)", color="#cccccc", fontsize=9)
    ax.set_title("Energy density along (1,1,1) projection",
                 color="white", fontsize=10)
    ax.legend(facecolor="#050510", edgecolor="#444",
              labelcolor="#cccccc", fontsize=8)
    ax.tick_params(colors="#cccccc", labelsize=8)

    # Panel 1: peak arrival at s_a, s_b
    ax = fig.add_subplot(gs[0, 1])
    ax.set_facecolor("#050510")
    times_ns = np.asarray(result["times"]) * 1e9
    ax.plot(times_ns, result["rho_a_history"], "-",
            color="lime", lw=1.4, label=f"|V|² at s_a={result['s_a']}")
    ax.plot(times_ns, result["rho_b_history"], "-",
            color="orange", lw=1.4, label=f"|V|² at s_b={result['s_b']}")
    ax.axvline(result["t_a_s"] * 1e9, color="lime", ls=":", lw=1)
    ax.axvline(result["t_b_s"] * 1e9, color="orange", ls=":", lw=1)
    ax.set_xlabel("t (ns)", color="#cccccc", fontsize=9)
    ax.set_ylabel("|V|² at reference plane", color="#cccccc", fontsize=9)
    ax.set_title(
        f"Peak-arrival times: t_a={result['t_a_s']*1e9:.2f}, "
        f"t_b={result['t_b_s']*1e9:.2f} (ns)",
        color="white", fontsize=10,
    )
    ax.legend(facecolor="#050510", edgecolor="#444",
              labelcolor="#cccccc", fontsize=8)
    ax.tick_params(colors="#cccccc", labelsize=8)
    ax.grid(alpha=0.2, color="#444")

    # Panel 2: v_card vs v_diag bars
    ax = fig.add_subplot(gs[1, 0])
    ax.set_facecolor("#050510")
    velocities = [eval_result["v_cardinal_over_c"], result["v_diagonal_over_c"]]
    labels = ["cardinal\n(+x̂)", "diagonal\n(1,1,1)/√3"]
    colors = ["#aaff77", "#ffaa44"]
    bars = ax.bar(labels, velocities, color=colors, edgecolor="white")
    ax.axhline(np.sqrt(2.0), color="orange", ls="--", lw=1, label="√2")
    ax.axhline(1.0, color="green", ls="--", lw=1, label="c (target diag)")
    for bar, val in zip(bars, velocities):
        ax.text(bar.get_x() + bar.get_width() / 2.0, val + 0.04,
                f"{val:.4f}", ha="center", color="white", fontsize=10)
    ax.set_ylim(0, max(max(velocities) * 1.2, 1.7))
    ax.set_ylabel("v / c", color="#cccccc", fontsize=10)
    ax.set_title(
        f"Layer 1 anisotropy: v_card/v_diag = "
        f"{eval_result['anisotropy_ratio']:.4f}  vs  √2 = {np.sqrt(2.0):.4f}",
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
        "Pre-reg evaluation (Phase 1.5 — completes Layer 1):",
        "",
        f"C-L1.2 (diagonal v/c):      {result['v_diagonal_over_c']:.4f}",
        f"   range ∈ [0.85, 1.15], target = c (= 1.0)",
        f"   verdict = {'PASS' if eval_result['pass_C_L1_2'] else 'FAIL'}",
        "",
        f"C-L1.3 (anisotropy ratio):  {eval_result['anisotropy_ratio']:.4f}",
        f"   range ∈ [1.30, 1.55], target = √2 ≈ {np.sqrt(2.0):.4f}",
        f"   verdict = {'PASS' if eval_result['pass_C_L1_3'] else 'FAIL'}",
        "",
        f"Phase 1 cardinal v/c:       {eval_result['v_cardinal_over_c']:.4f}  (PASS)",
        "",
        f"OVERALL Layer 1 emergence: "
        f"{'✓ PASS (cardinal+diagonal)' if eval_result['all_pass'] else '✗ PARTIAL'}",
        "",
        "Inputs: K4 4-port geometry + tilted-plane source perpendicular",
        "to (1,1,1)/√3. NO α/m_e/G/ℏ inputs in v/c extraction.",
        "Genuine geometric emergence per doc 108 §11.5 reframe.",
    ]
    for i, line in enumerate(summary_lines):
        if "PASS" in line and "PARTIAL" not in line:
            color = "#aaff77"
        elif "FAIL" in line or "PARTIAL" in line:
            color = "#ffaaaa"
        else:
            color = "#cccccc"
        ax.text(0.02, 0.95 - i * 0.05, line, transform=ax.transAxes,
                color=color, fontsize=9, family="monospace")

    fig.suptitle(
        "Layer 1 Emergence Phase 1.5 — Diagonal-Axis Velocity\n"
        "doc 108 §11.5 — tilted-source plane perpendicular to (1,1,1)/√3",
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
    print("Layer 1 Phase 1.5 — Diagonal-Axis Dispersion (tilted source)")
    print("=" * 72)

    result = run_diagonal_dispersion()

    print(f"\n  v_diagonal / c = {result['v_diagonal_over_c']:.4f}")
    print(f"  closed-form target c = 1.0")

    eval_result = evaluate_prereg(result)
    anisotropy = eval_result["anisotropy_ratio"]

    print(f"\n  v_cardinal / c (Phase 1) = {eval_result['v_cardinal_over_c']:.4f}")
    print(f"  anisotropy ratio = {anisotropy:.4f}  (target √2 = {np.sqrt(2.0):.4f})")

    print(f"\n── Pre-reg evaluation ──")
    print(f"  C-L1.2 diagonal v/c ∈ [0.85, 1.15]:  "
          f"{'PASS' if eval_result['pass_C_L1_2'] else 'FAIL'}")
    print(f"  C-L1.3 anisotropy ∈ [1.30, 1.55]:    "
          f"{'PASS' if eval_result['pass_C_L1_3'] else 'FAIL'}")
    print(f"  Overall Layer 1 (cardinal+diagonal): "
          f"{'PASS' if eval_result['all_pass'] else 'PARTIAL'}")

    out_png = assets_dir / "lattice_layer1_diagonal_panels.png"
    render_panels(result, eval_result, str(out_png))

    out_json = results_dir / "lattice_layer1_diagonal.json"
    result_serial = {
        k: (v.tolist() if isinstance(v, np.ndarray) else v)
        for k, v in result.items()
    }
    with open(out_json, "w") as f:
        json.dump({"prereg": PREREG, "eval": eval_result, "result": result_serial},
                  f, indent=2, default=str)

    print(f"\n  Outputs:")
    print(f"    {out_png}")
    print(f"    {out_json}")


if __name__ == "__main__":
    main()

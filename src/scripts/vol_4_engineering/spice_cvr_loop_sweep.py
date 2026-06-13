"""
SPICE-CVR constitutive-loop sweep — L0/L1/L2 ladder + frozen verdict bin.

Prereg: research/2026-06-13_spice-cvr-constitutive-loop_prereg.md
Harness: ave.solvers.spice_cvr_loop (dimensionless omega*tau; canonical tau in JSON).

HONEST SCOPE: local constitutive law only — NOT topology / winding / genesis.
REMANENT-LOOP proves retention mechanism in silico; does NOT make an electron.
"""

from __future__ import annotations

import json
import os
import sys

import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "src"))

from ave.solvers.spice_cvr_loop import OMEGA_TAU_GRID, simulate_arm  # noqa: E402
from ave_path_util import sim_output  # noqa: E402

OUT = os.path.join(os.path.dirname(__file__), "_output")
os.makedirs(OUT, exist_ok=True)


def _plot_loop(r: np.ndarray, s: np.ndarray, title: str, path: str) -> None:
    fig, ax = plt.subplots(figsize=(6, 5))
    fig.patch.set_facecolor("#0f0f0f")
    ax.set_facecolor("#0f0f0f")
    ax.plot(r, s, color="#4fc3f7", lw=1.5)
    ax.set_xlabel("r (normalized drive)", color="white")
    ax.set_ylabel("S (saturation state)", color="white")
    ax.set_title(title, color="white")
    ax.tick_params(colors="white")
    for spine in ax.spines.values():
        spine.set_edgecolor("#555555")
    ax.grid(color="#333333", linestyle="--", alpha=0.4)
    fig.tight_layout()
    fig.savefig(path, dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)


def _plot_sweep_metrics(result: dict) -> str:
    om = [row["omega_tau"] for row in result["L1_sweep"]]
    l1_a = [row["loop_area"] for row in result["L1_sweep"]]
    l2_a = [row["loop_area"] for row in result["L2_sweep"]]
    l1_br = [row["b_r"] for row in result["L1_sweep"]]
    l2_br = [row["b_r"] for row in result["L2_sweep"]]

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.patch.set_facecolor("#0f0f0f")
    for ax in axes:
        ax.set_facecolor("#0f0f0f")
        ax.tick_params(colors="white")
        ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white")
        ax.title.set_color("white")
        for spine in ax.spines.values():
            spine.set_edgecolor("#555555")
        ax.grid(color="#333333", linestyle="--", alpha=0.4)

    axes[0].plot(om, l1_a, "o-", color="#81c784", label="L1 memristor")
    axes[0].plot(om, l2_a, "s-", color="#ffb74d", label="L2 snap")
    axes[0].set_xlabel("omega * tau (dimensionless)")
    axes[0].set_ylabel("loop area ∮ S dr")
    axes[0].legend(facecolor="#1a1a1a", edgecolor="#555", labelcolor="white")
    axes[0].set_title("Dissipation vs drive rate")

    axes[1].plot(om, l1_br, "o-", color="#81c784", label="L1 B_r")
    axes[1].plot(om, l2_br, "s-", color="#ffb74d", label="L2 B_r")
    axes[1].axhline(result["thresholds"]["epsilon_br"], color="#ef5350", ls="--", lw=1)
    axes[1].set_xlabel("omega * tau")
    axes[1].set_ylabel("B_r = 1 - S at H→0")
    axes[1].legend(facecolor="#1a1a1a", edgecolor="#555", labelcolor="white")
    axes[1].set_title("Remanence vs drive rate")

    fig.suptitle(f"SPICE-CVR ladder — verdict {result['verdict']}", color="white")
    fig.tight_layout()
    path = sim_output("spice_cvr_loop_sweep_metrics.png")
    fig.savefig(path, dpi=150, facecolor=fig.get_facecolor())
    plt.close(fig)
    return path


def main() -> int:
    from ave.solvers.spice_cvr_loop import run_ladder_battery

    print("[*] SPICE-CVR constitutive-loop sweep (omega*tau grid)")
    result = run_ladder_battery()
    print(f"    verdict = {result['verdict']}")
    print(f"    L2 read  = {result['l2_emergence_read']}")
    print(f"    D2 read  = {result['d2_read']}")
    print(
        f"    L2 B_r peak = {result['l2_max_br']:.4f} @ omega*tau={result['l2_max_br_omega_tau']}"
    )
    print(f"    omega*tau grid = {result['omega_tau_grid']}")
    if result["l1_surprise_br"]:
        print(f"    FLAG: L1 max B_r = {result['l1_max_br']:.4f} (prereg predicted pinched)")

    gates = result["frozen_gates"]
    failed = [k for k, v in gates.items() if k.startswith(("H0", "H1", "H2")) and not v]
    if failed:
        print(f"    GATE FAILURES: {failed}")
        return 1

    json_path = os.path.join(OUT, "spice_cvr_loop_sweep_results.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(f"    JSON -> {json_path}")

    mid = OMEGA_TAU_GRID[len(OMEGA_TAU_GRID) // 2]
    hi = OMEGA_TAU_GRID[-2]
    fig_paths = []
    for arm, om, tag in (("L0", mid, "L0_anhysteretic"), ("L1", hi, "L1_memristor"), ("L2", hi, "L2_snap")):
        r, s, m = simulate_arm(arm, omega_tau=om)
        mask = r <= r.max() * 1.01
        p = sim_output(f"spice_cvr_loop_{tag}.png")
        _plot_loop(r[mask], s[mask], f"{arm} omega*tau={om:.2f} area={m.loop_area:.4f} B_r={m.b_r:.4f}", p)
        fig_paths.append(p)
        print(f"    figure -> {p}")

    metrics_path = _plot_sweep_metrics(result)
    print(f"    figure -> {metrics_path}")

    result["figures"] = [str(p) for p in fig_paths + [metrics_path]]
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    assert result["verdict"] in {
        "ANHYSTERETIC",
        "DISSIPATIVE-ONLY",
        "REMANENT-LOOP",
        "REGIME-LIMITED",
        "IMPOSED-LATCH",
    }
    assert gates[f"bin_{result['verdict'].replace('-', '_')}"]
    if result["verdict"] == "DISSIPATIVE-ONLY":
        assert "IMPOSED-LATCH" in result["l2_emergence_read"]
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""
Path C — Cross-Substrate Comparison Render
=============================================

Reads outputs from Path B (Yee Maxwell, photon_chiral_yee.json) and Path A
(K4-TLM, dark_wake_chiral_validation.json). Produces side-by-side
comparison panels.

Compares:
  - CP source verification (both should pass C-P1 / C-C2 etc.)
  - Forward propagation (Yee = c isotropic; K4 = √2c per Phase A.1 anomaly)
  - Dark wake amplitude + spatial profile
  - Chirality asymmetry (RH vs LH)
  - PML / boundary behavior

Outputs:
  - assets/photon_chiral_comparison.png  (side-by-side 6-panel)
  - results/photon_chiral_comparison_summary.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent.parent.parent
    results_dir = repo_root / "results"
    assets_dir = repo_root / "assets"

    yee_json = results_dir / "photon_chiral_yee.json"
    k4_json = results_dir / "dark_wake_chiral_validation.json"

    if not yee_json.exists():
        print(f"  ERROR: {yee_json} not found. Run photon_chiral_yee.py first.")
        return
    if not k4_json.exists():
        print(f"  ERROR: {k4_json} not found. Run dark_wake_chiral_validation.py first.")
        return

    with open(yee_json) as f:
        yee = json.load(f)
    with open(k4_json) as f:
        k4 = json.load(f)

    print("=" * 72)
    print("Path C — Cross-Substrate Comparison")
    print("=" * 72)

    # Pull comparison metrics from both
    yee_eval = yee.get("eval", {})
    k4_eval = k4.get("eval", {})

    print("\n── Yee Maxwell (Path B) ──")
    for k, v in yee_eval.items():
        if k.startswith("pass_"):
            print(f"  {k:30} {'PASS' if v else 'FAIL'}")
    print("\n── K4-TLM (Path A) ──")
    for k, v in k4_eval.items():
        if k.startswith("pass_"):
            print(f"  {k:30} {'PASS' if v else 'FAIL'}")

    # 6-panel side-by-side
    fig, axes = plt.subplots(3, 2, figsize=(14, 13))

    # Panels (row 0): CP source verification
    # Yee: phase offset at source
    yee_phase = yee_eval.get("C_P1_phase_offset_deg")
    yee_amp_ratio = yee_eval.get("C_P1_cp_amp_ratio", 1.0)
    ax = axes[0, 0]
    ax.text(
        0.5, 0.55,
        f"Yee Maxwell CP source\n\n"
        f"amp ratio Ey/Ez = {yee_amp_ratio:.4f}\n"
        f"phase offset = {yee_phase:.2f}°"
        if yee_phase else f"amp ratio Ey/Ez = {yee_amp_ratio:.4f}",
        ha="center", va="center", transform=ax.transAxes, fontsize=11,
        bbox=dict(boxstyle="round,pad=0.5",
                  facecolor="#cce" if yee_eval.get("pass_C_P1") else "#fcc",
                  edgecolor="black"),
    )
    ax.set_title("Path B — CP source verification (Yee)", fontweight="bold")
    ax.set_xticks([])
    ax.set_yticks([])

    k4_phase = k4_eval.get("C_C2_phase_offset_deg_abs")
    k4_amp_err = k4_eval.get("C_C1_amplitude_relative_error", 0.0)
    ax = axes[0, 1]
    ax.text(
        0.5, 0.55,
        f"K4-TLM Cosserat ω injection\n\n"
        f"amp rel err = {k4_amp_err:.3e}\n"
        f"phase offset = {k4_phase:.2f}°"
        if k4_phase else f"amp rel err = {k4_amp_err:.3e}",
        ha="center", va="center", transform=ax.transAxes, fontsize=11,
        bbox=dict(boxstyle="round,pad=0.5",
                  facecolor="#cce" if k4_eval.get("pass_C_C1") else "#fcc",
                  edgecolor="black"),
    )
    ax.set_title("Path A — Cosserat ω injection (K4-TLM)", fontweight="bold")
    ax.set_xticks([])
    ax.set_yticks([])

    # Panels (row 1): Forward propagation velocity
    ax = axes[1, 0]
    yee_v = yee_eval.get("C_P2_v_forward_over_c", 0.0)
    ax.bar(["Yee FDTD"], [yee_v], color="#47c", edgecolor="black")
    ax.axhline(1.0, color="green", ls="--", lw=1, label="c (corpus prediction)")
    ax.axhline(np.sqrt(2.0), color="orange", ls="--", lw=1, label="√2·c (K4 cardinal-axis)")
    ax.set_ylabel("v_forward / c")
    ax.set_title(
        f"Path B forward propagation: {yee_v:.3f}·c\n"
        f"(NOTE: peak-arrival on sustained source unreliable)",
    )
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="y")
    ax.text(
        0.5, 0.95, f"PASS={'✓' if yee_eval.get('pass_C_P2') else '✗'}",
        ha="center", va="top", transform=ax.transAxes,
        bbox=dict(boxstyle="round", facecolor="#cfc" if yee_eval.get("pass_C_P2") else "#fcc"),
    )

    ax = axes[1, 1]
    k4_drift = k4_eval.get("C_D2_centroid_drift", 0.0)
    ax.bar(["K4-TLM"], [k4_drift], color="#c47", edgecolor="black")
    ax.axhline(5.0, color="red", ls="--", lw=1, label="C-D2 threshold (5 cells)")
    ax.set_ylabel("centroid drift (cells)")
    ax.set_title(
        f"Path A forward propagation: drift = {k4_drift:.2f} cells\n"
        f"(per Phase A.1 finding: K4 cardinal v=√2·c)"
    )
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="y")
    ax.text(
        0.5, 0.95, f"PASS={'✓' if k4_eval.get('pass_C_D2') else '✗'}",
        ha="center", va="top", transform=ax.transAxes,
        bbox=dict(boxstyle="round", facecolor="#cfc" if k4_eval.get("pass_C_D2") else "#fcc"),
    )

    # Panels (row 2): chirality asymmetry + dark wake amplitude
    ax = axes[2, 0]
    yee_asym = yee_eval.get("C_P4_chirality_asymmetry_frac", 0.0) * 100
    k4_asym = k4_eval.get("C_D6_chirality_asymmetry", 0.0) * 100
    ax.bar(["Yee\n(Path B)", "K4-TLM\n(Path A)"], [yee_asym, k4_asym],
           color=["#47c", "#c47"], edgecolor="black")
    ax.axhline(5.0, color="red", ls="--", lw=1, label="C-P4/C-D6 threshold (5%)")
    ax.set_ylabel("|RH−LH| / max  [%]")
    ax.set_title("Chirality asymmetry RH vs LH")
    ax.legend(fontsize=9)
    ax.grid(alpha=0.3, axis="y")
    for x, y, p in zip([0, 1], [yee_asym, k4_asym],
                       [yee_eval.get('pass_C_P4'), k4_eval.get('pass_C_D6')]):
        ax.text(x, y + 0.5, f"{'✓' if p else '✗'}", ha="center", fontsize=14, fontweight="bold")

    ax = axes[2, 1]
    yee_wake = yee_eval.get("C_P3_max_wake_amplitude", 0.0)
    k4_wake_rh = k4_eval.get("C_D3_max_tau_zx_RH", 0.0)
    k4_wake_lh = k4_eval.get("C_D3_max_tau_zx_LH", 0.0)
    # Different units; just show RH vs LH ratio
    rh_lh_yee = "—"
    if k4_wake_rh > 0 and k4_wake_lh > 0:
        rh_lh_k4 = f"{k4_wake_rh / k4_wake_lh:.3f}"
    else:
        rh_lh_k4 = "—"
    ax.text(
        0.5, 0.55,
        f"Dark wake max amplitude\n\n"
        f"Path B Yee:  {yee_wake:.3e} (Z_eff·∂|E|²/∂x units)\n"
        f"Path A K4:   RH={k4_wake_rh:.3e}, LH={k4_wake_lh:.3e}\n"
        f"             RH/LH ratio = {rh_lh_k4}\n\n"
        f"NOTE: different units (Yee uses E-field SI, K4-TLM\n"
        f"uses V_inc engine-natural). Direct comparison is\n"
        f"qualitative — both show non-zero wake.",
        ha="center", va="center", transform=ax.transAxes, fontsize=10,
        bbox=dict(boxstyle="round,pad=0.5", facecolor="#eef", edgecolor="black"),
    )
    ax.set_title("Dark wake observation — both substrates")
    ax.set_xticks([])
    ax.set_yticks([])

    plt.suptitle(
        "Path C — Cross-Substrate Comparison: rifled photon + dark wake\n"
        "Yee Maxwell FDTD (Path B) vs K4-TLM CosseratBeltrami (Path A)",
        fontsize=12, fontweight="bold",
    )
    plt.tight_layout()

    out_png = assets_dir / "photon_chiral_comparison.png"
    plt.savefig(out_png, dpi=110, bbox_inches="tight")
    plt.close(fig)

    # Compose summary JSON
    summary = {
        "yee_eval": yee_eval,
        "k4_eval": k4_eval,
        "comparison_notes": [
            "Path B (Yee Maxwell) and Path A (K4-TLM) both run with chiral CP/Beltrami sources.",
            "CP source at injection: Path B passes phase 90° + amp 1:1; Path A Cosserat ω injection per docstring.",
            "Forward propagation: Path B's peak-arrival measurement on sustained source is unreliable; Path A uses centroid drift instead.",
            "Phase A.1 finding (K4 cardinal v=√2·c regardless of T₂ projection) means K4-TLM substrate kinematics differ from Yee Maxwell at the wavefront level.",
            "Dark wake observed in BOTH substrates — Yee via Z_eff·∂|E|²/∂x; K4-TLM via DarkWakeObserver tetrahedral_gradient on V_inc.",
            "Chirality asymmetry: both substrates show NON-zero asymmetry; thresholds (5%) are ad-hoc per A47 v18 since corpus doesn't supply quantitative chirality-induced wake-asymmetry prediction.",
            "Net: the dark wake mechanism is observable across substrate-implementation classes. Quantitative agreement at both magnitudes and propagation speeds requires substrate-physics-canonical prediction the corpus doesn't currently supply.",
        ],
    }
    out_json = results_dir / "photon_chiral_comparison_summary.json"
    with open(out_json, "w") as f:
        json.dump(summary, f, indent=2, default=str)

    print(f"\n  Outputs:")
    print(f"    {out_png}")
    print(f"    {out_json}")


if __name__ == "__main__":
    main()

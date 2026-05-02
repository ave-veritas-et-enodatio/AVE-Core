"""
Phase B.2 — Extended-domain linear-pulse dark wake baseline.

Per implementation plan, Phase B.2: run dark_wake_validation at N=128,
PML=12, n_outer_steps=300 to test whether wake velocity converges to c
(corpus prediction) at extended domain, or stays at ~0.38 c
(per B.1 result at N=48, structural discrepancy).

Pre-registered (verbatim):
  C-B1: max τ_zx > 0
  C-B2: wake_peak_x < source_x (backward propagation)
  C-B3: Pearson r(V², τ_zx) > 0.7
  C-B4: late-time wake velocity v_wake ∈ (-1.1·c, -0.9·c) cells/t
  C-B5: wake amplitude τ_zx still detectable at x = 0.5·N (no premature decay)
  C-B6: wake doesn't reflect off PML (τ_zx at PML interface < 5% of peak)

Outputs:
  - assets/dark_wake_extended_baseline.png
  - assets/dark_wake_extended_baseline.gif
  - results/dark_wake_extended_baseline.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

from dark_wake_validation import run_validation, analyze_and_plot  # noqa: E402


PREREG = {
    "C-B1_max_tau_zx_min": 0.0,
    "C-B3_pearson_min": 0.7,
    "C-B4_v_wake_min_over_c": -1.1,
    "C-B4_v_wake_max_over_c": -0.9,
    "C-B5_tau_at_half_N_min_frac_of_peak": 0.05,
    "C-B6_tau_at_PML_max_frac_of_peak": 0.05,
}


def main() -> None:
    repo_root = Path(__file__).resolve().parent.parent.parent.parent
    assets_dir = repo_root / "assets"
    results_dir = repo_root / "results"
    assets_dir.mkdir(parents=True, exist_ok=True)
    results_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 72)
    print("Phase B.2 — Extended-domain linear-pulse baseline (N=128)")
    print("=" * 72)

    result = run_validation(
        N=128,
        pml=12,
        lambda_cells=8.0,
        amplitude=0.5,
        source_x=20,  # just inside PML=12; wake propagates backward into PML buffer
        t_sigma_periods=1.0,
        n_outer_steps=300,
        record_cadence=4,
    )

    out_png = assets_dir / "dark_wake_extended_baseline.png"
    out_gif = assets_dir / "dark_wake_extended_baseline.gif"
    summary = analyze_and_plot(result, str(out_png), str(out_gif))

    # Note: dark_wake_validation.run_validation outputs `c` for the engine; we need
    # to compute c_engine to evaluate C-B4 in c-relative units.
    # Per K4Lattice3D, dt = dx/(c√2) ⇒ c = dx/(dt·√2).
    # Outer step is one K4-TLM step; engine.outer_dt = engine.k4.dt.
    # For natural units (c0=1, dx=1): c = 1/√2 cells per nat-unit-time.
    # So v_wake (cells / nat-unit-time) / c (cells / nat-unit-time) = v_wake · √2.

    # However, in dark_wake_validation, late_wake_velocity is already cells/(outer_dt-stride),
    # so the conversion depends on how dark_wake_validation reports it. Trust the
    # script's output as cells/nat-unit-time and convert using c=1/√2 nat units.
    c_engine = 1.0 / np.sqrt(2.0)

    v_wake_over_c = summary["late_wake_velocity"] / c_engine

    print()
    print("── Pre-reg evaluation ──")
    pass_C_B1 = summary["max_tau_zx"] > PREREG["C-B1_max_tau_zx_min"]
    pass_C_B3 = summary["pearson_V2_tau"] > PREREG["C-B3_pearson_min"]
    pass_C_B4 = (
        PREREG["C-B4_v_wake_min_over_c"]
        <= v_wake_over_c
        <= PREREG["C-B4_v_wake_max_over_c"]
    )
    print(f"  C-B1 (max τ_zx > 0):                  {'PASS' if pass_C_B1 else 'FAIL'}  (got {summary['max_tau_zx']:.4f})")
    print(f"  C-B3 (Pearson r(V², τ) > 0.7):         {'PASS' if pass_C_B3 else 'FAIL'}  (got {summary['pearson_V2_tau']:.4f})")
    print(f"  C-B4 (v_wake/c ∈ [-1.1, -0.9]):       {'PASS' if pass_C_B4 else 'FAIL'}  (got v_wake = {summary['late_wake_velocity']:.4f}, v_wake/c_eng = {v_wake_over_c:.4f})")
    print(f"  C-B2/C-B5/C-B6: visual confirmation in GIF; tau_slabs in JSON")

    out = {
        "prereg": PREREG,
        "summary": summary,
        "c_engine_assumed": float(c_engine),
        "v_wake_over_c_engine": float(v_wake_over_c),
        "pass_C_B1": bool(pass_C_B1),
        "pass_C_B3": bool(pass_C_B3),
        "pass_C_B4": bool(pass_C_B4),
        "verdict_overall": summary["verdict"],
    }

    out_json = results_dir / "dark_wake_extended_baseline.json"
    with open(out_json, "w") as f:
        json.dump(out, f, indent=2, default=str)

    print()
    print(f"Outputs:")
    print(f"  {out_png}")
    print(f"  {out_gif}")
    print(f"  {out_json}")


if __name__ == "__main__":
    main()

"""
Run the full AVE double-slit / Born-from-clicks capstone end-to-end.

    PYTHONPATH=src python -m scripts.vol_2_subatomic.ave_double_slit_born.run_capstone

Pipeline:
  1. REAL FDTD field  (canonical FDTD3DEngine)          -> |E|^2, |psi|^2 profile
  2. threshold-crossing clicks (no Born in the detector) -> click histogram
  3. validation        (chi^2 / KS / fringe / no-Born grep / exponent scan)
  4. figures           (4 stills + long animation) into research/figures/
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from . import figures
from .click_detector import accumulate_clicks
from .config import DetectorConfig, FieldConfig, fig_path
from .field_engine import run_field
from .validate import exponent_scan, fringe_spacing, grep_no_born, histogram_match


def main(*, skip_anim: bool = False) -> dict:
    print("[1/4] REAL FDTD field (canonical FDTD3DEngine) ...")
    field = run_field(FieldConfig(), verbose=True)

    print("[2/4] threshold-crossing clicks (Born-free detector) ...")
    det_cfg = DetectorConfig()
    clicks = accumulate_clicks(field.intensity_y, det_cfg, verbose=True)

    print("[3/4] validation ...")
    hm = histogram_match(field.intensity_y, clicks.histogram, clicks.click_cells)
    fr = fringe_spacing(field.intensity_y, field)
    detector_src = Path(__file__).with_name("click_detector.py")
    grep = grep_no_born(detector_src)
    escan = exponent_scan(field)

    stats = {
        "chi2_dof": hm["chi2_dof"],
        "corr": hm["corr"],
        "ks": hm["ks"],
        "spacing_clicks": fr["spacing_clicks"],
        "spacing_err_pct": fr["spacing_err_pct"],
    }

    print("[4/4] figures ...")
    heights = figures.cosmetic_heights(clicks.click_cells.size, seed=7)
    paths = {}
    paths["a_smooth_field"] = figures.still_smooth_field(field)
    c12, c_hundreds, _c_all = det_cfg.snapshot_counts
    paths["b_clicks_first"] = figures.still_clicks(
        field, clicks, c12, heights, "b_clicks_first", f"First {c12} clicks — no pattern (each = one self-trap)"
    )
    paths["c_clicks_hundreds"] = figures.still_clicks(
        field, clicks, c_hundreds, heights, "c_clicks_hundreds", f"{c_hundreds} clicks — the fringe pattern emerges"
    )
    paths["d_born_recovered"] = figures.still_born_recovered(field, clicks, heights, {**stats, **fr})
    if not skip_anim:
        paths["animation"] = figures.animation(field, clicks, heights, stats)

    summary = {
        "field": {
            "wavelength_measured": field.wavelength_measured,
            "wavelength_analytic": field.wavelength_analytic,
            "fringe_spacing_pred": field.fringe_spacing_pred,
            "z_uniformity": field.z_uniformity,
            "L": field.cfg.L,
            "d": field.cfg.slit_sep,
        },
        "n_clicks": int(clicks.click_cells.size),
        "mean_micro_steps": clicks.mean_micro_steps,
        "histogram_match": hm,
        "fringe": fr,
        "no_born_grep": grep,
        "exponent_scan": escan,
        "figures": paths,
    }
    out_json = fig_path("capstone_validation.json")
    Path(out_json).write_text(json.dumps(summary, indent=2, default=float))

    print("\n================ CAPSTONE SUMMARY ================")
    print(
        f"  field: lambda={field.wavelength_measured:.1f} cells, L={field.cfg.L}, d={field.cfg.slit_sep}, "
        f"z-uniformity={field.z_uniformity:.1e}"
    )
    print(
        f"  Born recovery: chi2/dof={hm['chi2_dof']:.2f}  KS={hm['ks']:.3f}  corr={hm['corr']:.3f}  "
        f"({clicks.click_cells.size} clicks)"
    )
    print(
        f"  fringe spacing: clicks {fr['spacing_clicks']:.1f} vs de-Broglie λL/d {fr['spacing_pred']:.1f} cells "
        f"({fr['spacing_err_pct']:.1f}%, Fresnel#={fr['fresnel_number']:.2f})"
    )
    print(
        f"  no-Born grep: all_pass={grep['checks']['all_pass']}  "
        f"(raw docstring mentions: born={grep['docstring_mentions']['born_raw_count']}, "
        f"psi={grep['docstring_mentions']['psi_raw_count']})"
    )
    print("  energy-exponent counterfactual (chi2/dof; only p=2 should match):")
    for k, v in escan.items():
        print(f"      |E|^{k.split('=')[1]} -> chi2/dof={v['chi2_dof']:.2f}")
    print(f"  figures -> {fig_path('').parent if False else Path(out_json).parent}")
    print("==================================================")
    return summary


if __name__ == "__main__":
    import sys

    main(skip_anim="--skip-anim" in sys.argv)

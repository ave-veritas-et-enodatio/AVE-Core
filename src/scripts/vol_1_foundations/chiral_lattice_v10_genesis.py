#!/usr/bin/env python3
"""Genesis v10 — CVR convergence driver (snap + tri-channel χ + Ω_freeze IC)."""

from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

from ave.core.chiral_lattice_v10 import V10P6Result, v10_gates

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def _p6_row(c: V10P6Result) -> str:
    return (
        f"  {c.label} (amp={c.amp_frac}, χ={c.chi_shock}): bin={c.bin_label} "
        f"plateau%={c.r_rms_plateau_pct:.2f} e_driveoff={c.e_loc_ratio_driveoff:.3f} "
        f"snap_ev={c.snap_events} E_diss={c.E_diss_snap:.4f} Ω_ic={c.omega_freeze_ic}"
    )


def main() -> None:
    smoke = "--smoke" in sys.argv
    L = 8 if smoke else 10
    g = v10_gates(L=L, smoke=smoke, chi_shock=0.5)
    tag = "(SMOKE)" if smoke else "(PRODUCTION)"
    print("=" * 72)
    print("GENESIS v10 — CVR CONVERGENCE", tag)
    print("Engine:", g["engine_class"])
    print(f"L_p6={g['L_p6']} | A_yield²={g['A_yield_sq']:.6f} | τ_relax={g['tau_relax_s']:.3e}s")
    print("=" * 72)
    print("P6 srs cells:")
    for c in g["P6_cells"]:
        print(_p6_row(c))
    if g.get("P6_diamond_cells"):
        print("P6 diamond:")
        for c in g["P6_diamond_cells"]:
            print(_p6_row(c))
    print(_p6_row(g["P6_snap_ablation"]).replace("  ", "  Ablation ", 1))
    print(_p6_row(g["P6_omega_free_ablation"]).replace("  ", "  Ablation ", 1))
    print(_p6_row(g["P6_op3_ablation"]).replace("  ", "  Ablation ", 1))
    if g.get("P6_op14_ablation"):
        print(_p6_row(g["P6_op14_ablation"]).replace("  ", "  Ablation ", 1))
    if g.get("P6_matched_baseline"):
        mb = g["P6_matched_baseline"]
        print("Matched baseline:")
        print(
            f"  srs={mb['srs_R_z_e_retention']:.3f} snap_off={mb['snap_off_e_retention']:.3f} "
            f"Ω_free={mb['omega_free_e_retention']:.3f} structure_2x={mb['structure_driven_2x']}"
        )
    if g.get("P6_chi_sweep"):
        print("χ sweep (srs-R:+z, amp=0.25):")
        for c in g["P6_chi_sweep"]:
            print(f"    χ={c.chi_shock}: E_diss={c.E_diss_snap:.4f} e_ret={c.e_loc_ratio_driveoff:.3f}")
        print(f"  P6-χ-MONO={g['P6_chi_mono']} P6-χ-RET vs v9={g['P6_chi_ret_vs_v9']}")
    print("=" * 72)
    print("P6 any CVR-SET:", g["P6_pass"])
    print("(Honest closure — do not promote without matched-baseline 2×.)")
    print("=" * 72)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "genesis_v10_cvr_convergence.json"

    def _ser(c: V10P6Result) -> dict:
        return asdict(c)

    payload = {
        "smoke": smoke,
        "L_p6": g["L_p6"],
        "P6_pass": g["P6_pass"],
        "P6_bins": g["P6_bins"],
        "P6_cells": [_ser(c) for c in g["P6_cells"]],
        "P6_diamond_cells": [_ser(c) for c in g.get("P6_diamond_cells", [])],
        "P6_matched_baseline": g.get("P6_matched_baseline"),
        "P6_chi_sweep": [_ser(c) for c in g.get("P6_chi_sweep", [])],
    }
    path.write_text(json.dumps(payload, indent=2))
    print("Wrote", path)


if __name__ == "__main__":
    main()

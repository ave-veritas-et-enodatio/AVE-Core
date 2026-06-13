#!/usr/bin/env python3
"""Genesis v11 — LOOP GAP closure driver (memristive τ + P11 quiescence)."""

from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

from ave.core.chiral_lattice_v11 import V11P6Result, v11_gates

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def _p6_row(c: V11P6Result) -> str:
    return (
        f"  {c.label} (amp={c.amp_frac}, χ={c.chi_shock}, mem={c.memristive_on}): "
        f"bin={c.bin_label} plateau%={c.r_rms_plateau_pct:.2f} "
        f"e_driveoff={c.e_loc_ratio_driveoff:.3f} P11={c.p11_pass} "
        f"E_p={c.E_persist_ratio:.3f} A_p={c.A_persist_ratio:.3f} "
        f"θ_p={c.theta_persist:.3f} loop={c.loop_proxy:.2f}"
    )


def main() -> None:
    smoke = "--smoke" in sys.argv
    L = 8 if smoke else 10
    g = v11_gates(L=L, smoke=smoke, chi_shock=0.5)
    tag = "(SMOKE)" if smoke else "(PRODUCTION)"
    print("=" * 72)
    print("GENESIS v11 — LOOP GAP CLOSURE", tag)
    print("Engine:", g["engine_class"])
    print(
        f"L_p6={g['L_p6']} | τ_steps={g['tau_steps']} | n_quiet={g['n_quiet']} | "
        f"τ_relax={g['tau_relax_s']:.3e}s"
    )
    print("=" * 72)
    print("P6 srs cells (memristive ON):")
    for c in g["P6_cells"]:
        print(_p6_row(c))
    if g.get("P6_diamond_cells"):
        print("P6 diamond:")
        for c in g["P6_diamond_cells"]:
            print(_p6_row(c))
    print(_p6_row(g["P11_memristive_ablation"]).replace("  ", "  Ablation ", 1))
    print(_p6_row(g["P6_snap_ablation"]).replace("  ", "  Ablation ", 1))
    print(_p6_row(g["P6_omega_free_ablation"]).replace("  ", "  Ablation ", 1))
    print(_p6_row(g["P6_op3_ablation"]).replace("  ", "  Ablation ", 1))
    if g.get("P6_op14_ablation"):
        print(_p6_row(g["P6_op14_ablation"]).replace("  ", "  Ablation ", 1))
    print(
        f"v10 replay: bin={g['v10_replay'].bin_label} "
        f"match_mem_off={g['v10_replay_bin_match']}"
    )
    if g.get("P6_matched_baseline"):
        mb = g["P6_matched_baseline"]
        print("Matched baseline:")
        print(
            f"  srs={mb['srs_R_z_e_retention']:.3f} mem_off={mb['memristive_off_e_retention']:.3f} "
            f"snap_off={mb['snap_off_e_retention']:.3f} structure_2x={mb['structure_driven_2x']}"
        )
    if g.get("D6_ringup_sweep"):
        print("D6 ring-up (srs-R:+z, amp=0.5):")
        for c in g["D6_ringup_sweep"]:
            print(
                f"    {c.label}: n_drive implicit P11={c.p11_pass} "
                f"E_p={c.E_persist_ratio:.3f} loop={c.loop_proxy:.2f}"
            )
    if g.get("P6_chi_sweep"):
        print("χ sweep (srs-R:+z, amp=0.25):")
        for c in g["P6_chi_sweep"]:
            print(f"    χ={c.chi_shock}: E_diss={c.E_diss_snap:.4f} e_ret={c.e_loc_ratio_driveoff:.3f}")
    print("=" * 72)
    print("P6 any CVR-SET:", g["P6_pass"])
    print("P11 any PASS:", g["P11_any_pass"])
    print("P11 primary + mem ablation FAIL:", g["P11_primary_ablation_ok"])
    print("VERDICT:", g["verdict"])
    print("(Honest closure — LANDED requires P11 + 2× + +z srs.)")
    print("=" * 72)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "genesis_v11_loop_closure.json"

    def _ser(c: V11P6Result) -> dict:
        return asdict(c)

    payload = {
        "smoke": smoke,
        "verdict": g["verdict"],
        "L_p6": g["L_p6"],
        "tau_steps": g["tau_steps"],
        "P6_pass": g["P6_pass"],
        "P11_any_pass": g["P11_any_pass"],
        "P11_primary_ablation_ok": g["P11_primary_ablation_ok"],
        "P6_bins": g["P6_bins"],
        "P11_metrics": g["P11_metrics"],
        "P6_cells": [_ser(c) for c in g["P6_cells"]],
        "P6_diamond_cells": [_ser(c) for c in g.get("P6_diamond_cells", [])],
        "P11_memristive_ablation": _ser(g["P11_memristive_ablation"]),
        "P6_matched_baseline": g.get("P6_matched_baseline"),
        "D6_ringup_sweep": [_ser(c) for c in g.get("D6_ringup_sweep", [])],
        "v10_replay_bin_match": g["v10_replay_bin_match"],
    }
    path.write_text(json.dumps(payload, indent=2))
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()

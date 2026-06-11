#!/usr/bin/env python3
"""Genesis v9 Phase-2 — P5 hosting + P6 genesis driver (honest bins)."""

from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from ave.core.chiral_lattice_vector_sat import P6RunResult, phase2_gates

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def _p6_row(c: P6RunResult) -> str:
    return (
        f"  {c.label} (amp={c.amp_frac}): bin={c.bin_label} plateau%={c.r_rms_plateau_pct:.2f} "
        f"e_driveoff={c.e_loc_ratio_driveoff:.3f} theta_ok={c.theta_sign_ok} dθ={c.dtheta:.4f}"
    )


def _p6_dict(c: P6RunResult) -> dict:
    return asdict(c)


def main() -> None:
    smoke = "--smoke" in __import__("sys").argv
    L = 8 if smoke else 10
    g = phase2_gates(L=L, smoke=smoke)
    print("=" * 72)
    print("GENESIS v9 PHASE-2 — P5/P6 GATES", "(SMOKE)" if smoke else "(PRODUCTION)")
    print("Engine:", g["engine_class"], "| κ_chiral =", g["kappa_chiral"])
    print(f"Grid: P5 L={g['L_p5']} | P6 L={g['L_p6']} | nodes srs-R =", g["P6_cells"][0].n_nodes)
    print("=" * 72)
    p5 = g["P5"]
    print(
        f"P5 hosting: E_ratio={p5.energy_ratio_end:.4f} Q_drift={p5.charge_drift_rel:.4f} "
        f"PASS_E={p5.pass_E} PASS_Q={p5.pass_Q} PASS={p5.pass_T}"
    )
    print("P6 srs cells (best per amp sweep):")
    for c in g["P6_cells"]:
        print(_p6_row(c))
    if g.get("P6_diamond_cells"):
        print("P6 diamond controls:")
        for c in g["P6_diamond_cells"]:
            print(_p6_row(c))
    ab = g["P6_op3_ablation"]
    print(_p6_row(ab).replace("  ", "  Op3 ablation ", 1))
    if g.get("P6_op14_ablation"):
        print(_p6_row(g["P6_op14_ablation"]).replace("  ", "  Op14 ablation ", 1))
    if g.get("P6_matched_baseline"):
        mb = g["P6_matched_baseline"]
        print("Matched baseline (srs-R:+z vs controls):")
        print(f"  e_retention srs={mb['srs_R_z_e_retention']:.3f} op3_off={mb['op3_off_e_retention']:.3f} "
              f"op14_off={mb['op14_off_e_retention']:.3f} diamond={mb['diamond_e_retention']:.3f}")
        print(f"  structure_driven_2x={mb['structure_driven_2x']} "
              f"diamond_theta/srs={mb['diamond_theta_frac_of_srs']:.4f}")
    print("=" * 72)
    print("P5 PASS:", g["P5_pass"], " P6 any CVR-SET:", g["P6_pass"])
    print("(Honest closure — BIN-D is an informative outcome per A-027.)")
    print("=" * 72)
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "genesis_v9_phase2_genesis.json"
    payload = {
        "smoke": smoke,
        "L_p5": g["L_p5"],
        "L_p6": g["L_p6"],
        "kappa_chiral": g["kappa_chiral"],
        "P5_pass": g["P5_pass"],
        "P6_pass": g["P6_pass"],
        "P5": asdict(p5),
        "P6_bins": g["P6_bins"],
        "P6_cells": [_p6_dict(c) for c in g["P6_cells"]],
        "P6_diamond_cells": [_p6_dict(c) for c in g.get("P6_diamond_cells", [])],
        "P6_op3_ablation": _p6_dict(ab),
        "P6_op14_ablation": _p6_dict(g["P6_op14_ablation"]) if g.get("P6_op14_ablation") else None,
        "P6_matched_baseline": g.get("P6_matched_baseline"),
    }
    path.write_text(json.dumps(payload, indent=2))
    print(f"[artifact] {path}")


if __name__ == "__main__":
    main()

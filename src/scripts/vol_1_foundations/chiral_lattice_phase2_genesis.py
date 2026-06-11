#!/usr/bin/env python3
"""Genesis v9 Phase-2 — P5 hosting + P6 genesis driver (honest bins)."""

from __future__ import annotations

import json
from pathlib import Path

from ave.core.chiral_lattice_vector_sat import phase2_gates

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def main() -> None:
    smoke = "--smoke" in __import__("sys").argv
    g = phase2_gates(L=8, smoke=smoke)
    print("=" * 72)
    print("GENESIS v9 PHASE-2 — P5/P6 GATES", "(SMOKE)" if smoke else "(FULL)")
    print("Engine:", g["engine_class"])
    print("=" * 72)
    p5 = g["P5"]
    print(f"P5 hosting: E_ratio={p5.energy_ratio_end:.4f} Q_drift={p5.charge_drift_rel:.4f} PASS={p5.pass_T}")
    print("P6 cells:")
    for c in g["P6_cells"]:
        print(
            f"  {c.label}: bin={c.bin_label} plateau%={c.r_rms_plateau_pct:.2f} "
            f"e_driveoff={c.e_loc_ratio_driveoff:.3f} theta_ok={c.theta_sign_ok}"
        )
    ab = g["P6_op3_ablation"]
    print(f"  Op3 ablation {ab.label}: bin={ab.bin_label} plateau%={ab.r_rms_plateau_pct:.2f}")
    print("=" * 72)
    print("P5 PASS:", g["P5_pass"], " P6 any CVR-SET:", g["P6_pass"])
    print("(Honest closure — BIN-D is an informative outcome per A-027.)")
    print("=" * 72)
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "genesis_v9_phase2_genesis.json"
    payload = {
        "smoke": smoke,
        "P5_pass": g["P5_pass"],
        "P6_pass": g["P6_pass"],
        "P5": {
            "energy_ratio_end": p5.energy_ratio_end,
            "charge_drift_rel": p5.charge_drift_rel,
            "pass_T": p5.pass_T,
        },
        "P6_bins": g["P6_bins"],
        "P6_op3_ablation_bin": ab.bin_label,
    }
    path.write_text(json.dumps(payload, indent=2))
    print(f"[artifact] {path}")


if __name__ == "__main__":
    main()

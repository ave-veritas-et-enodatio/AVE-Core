#!/usr/bin/env python3
"""Genesis v13 — OP-2 eigen-cavity / bulk-wall confinement driver."""

from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

from ave.core.chiral_lattice_v13 import V13P13Result, v13_gates

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def _p13_row(c: V13P13Result) -> str:
    return (
        f"  {c.label}: wall={c.bulk_wall_on} "
        f"E_frac={c.E_frac_interior:.3f} width×={c.width_ratio:.2f} "
        f"peak={c.peak_retention:.3f} P13={c.p13_pass}"
    )


def main() -> None:
    smoke = "--smoke" in sys.argv
    L = 8 if smoke else 10
    g = v13_gates(L=L, smoke=smoke)
    tag = "(SMOKE)" if smoke else "(PRODUCTION)"
    print("=" * 72)
    print("GENESIS v13 — OP-2 EIGEN-CAVITY / BULK-WALL CONFINEMENT", tag)
    print("Engine:", g["engine_class"])
    print(f"L={g['L_p13']} | n_steps={g['n_steps']} | z_wall={g['z_wall']}")
    print("=" * 72)
    print(_p13_row(g["P13_wall_on"]))
    print(_p13_row(g["P13_wall_off_ablation"]).replace("  ", "  Ablation ", 1))
    print(_p13_row(g["P13_memristive_ablation"]).replace("  ", "  Ablation ", 1))
    print(_p13_row(g["P13_linear_control"]).replace("  ", "  Control ", 1))
    print(
        f"Wall discrimination: width× ratio={g['wall_width_discrimination']:.2f} "
        f"ΔE_frac={g['wall_E_frac_gain']:.3f}"
    )
    print(
        f"v11 regression: bin={g['v11_regression'].bin_label} "
        f"P11={g['v11_regression'].p11_pass}"
    )
    print("=" * 72)
    print("P13 any PASS:", g["P13_any_pass"])
    print("P13 ablation FAIL:", g["P13_ablation_fails"])
    print("P13 wall discriminates:", g["P13_wall_discriminates"])
    print("VERDICT:", g["verdict"])
    print("=" * 72)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "genesis_v13_eigen_cavity.json"
    payload = {
        "smoke": smoke,
        "verdict": g["verdict"],
        "P13_any_pass": g["P13_any_pass"],
        "P13_wall_on": asdict(g["P13_wall_on"]),
        "P13_wall_off_ablation": asdict(g["P13_wall_off_ablation"]),
        "P13_linear_control": asdict(g["P13_linear_control"]),
        "P13_memristive_ablation": asdict(g["P13_memristive_ablation"]),
        "wall_width_discrimination": g["wall_width_discrimination"],
        "wall_E_frac_gain": g["wall_E_frac_gain"],
        "v11_regression_p11": g["v11_regression"].p11_pass,
    }
    path.write_text(json.dumps(payload, indent=2))
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()

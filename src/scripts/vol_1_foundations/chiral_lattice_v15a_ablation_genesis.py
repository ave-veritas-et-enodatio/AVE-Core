#!/usr/bin/env python3
"""Genesis v15a-ablation — latent-window dissipation OFF driver."""

from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

from ave.core.chiral_lattice_v15 import V15P15Result, v15a_ablation_gates

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def _row(c: V15P15Result) -> str:
    return (
        f"  {c.label}: r_yield*={c.r_yield_seed_peak:.3f} "
        f"A2_vsnap*={c.A2_seed_peak:.5f} E_frac={c.E_frac_interior:.3f} "
        f"P15-N={c.p15n_pass}"
    )


def main() -> None:
    smoke = "--smoke" in sys.argv
    L = 8 if smoke else 10
    g = v15a_ablation_gates(L=L, smoke=smoke)
    tag = "(SMOKE)" if smoke else "(PRODUCTION)"
    print("=" * 72)
    print("GENESIS v15a-ABLATION — LATENT DISSIPATION OFF", tag)
    print("Engine:", g["engine_class"])
    sw = g["ablation_switches"]
    print(
        f"L={g['L_p15']} | latent: χ={sw['latent_chi_shock']} snap={sw['latent_snap']} "
        f"mem={sw['latent_memristive']} | baseline χ={sw['baseline_chi_shock']}"
    )
    print("=" * 72)
    print(_row(g["P15_A_baseline"]))
    print(_row(g["P15_A_ablated"]))
    print(_row(g["P15_B_heal"]))
    print(f"Gain r_yield (ablated/baseline): {g['gain_r_yield']:.3f}")
    print(f"Gain A2_vsnap (ablated/baseline): {g['gain_A2_vsnap']:.3f}")
    print(f"P15-H heal pass: {g['P15_H_heal_pass']}")
    print("=" * 72)
    print("VERDICT:", g["verdict"])
    print("=" * 72)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "genesis_v15a_ablation_latent.json"
    payload = {
        "smoke": smoke,
        "verdict": g["verdict"],
        "provenance": g["provenance"],
        "ablation_switches": g["ablation_switches"],
        "gain_r_yield": g["gain_r_yield"],
        "gain_A2_vsnap": g["gain_A2_vsnap"],
        "P15_H_heal_pass": g["P15_H_heal_pass"],
        "P15_A_baseline": asdict(g["P15_A_baseline"]),
        "P15_A_ablated": asdict(g["P15_A_ablated"]),
        "P15_B_heal": asdict(g["P15_B_heal"]),
    }
    path.write_text(json.dumps(payload, indent=2))
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()

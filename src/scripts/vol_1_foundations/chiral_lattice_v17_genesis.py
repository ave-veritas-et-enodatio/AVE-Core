#!/usr/bin/env python3
"""Genesis v17 — moving resonator (cavity + Compton + comoving + P11) driver."""

from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

from ave.core.chiral_lattice_v17 import V17P17Result, v17_gates

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def _row(c: V17P17Result) -> str:
    return (
        f"  {c.label}: drive={c.n_drive} quiet={c.n_quiet} "
        f"disp={c.centroid_disp:.3f} E_frac={c.E_frac_interior:.3f} "
        f"peak_p={c.peak_pocket_retention:.3f} E_persist={c.E_persist_ratio:.3f} "
        f"P11={c.p11_pass} P13={c.p13_pass} P12={c.p12_pass} P17={c.p17_pass} "
        f"bin={c.bin_label}"
    )


def main() -> None:
    smoke = "--smoke" in sys.argv
    L = 8 if smoke else 10
    g = v17_gates(L=L, smoke=smoke)
    tag = "(SMOKE)" if smoke else "(PRODUCTION)"
    print("=" * 72)
    print("GENESIS v17 — MOVING RESONATOR STACK", tag)
    print("Engine:", g["engine_class"])
    print(f"L={g['L_p17']} | Nτ={g['tau_steps']}")
    print(
        f"Transport gain (full−pinned): {g['P17_transport_gain']:.3f} "
        f"(threshold {g['P12_gain_threshold']:.3f})"
    )
    print("=" * 72)
    for r in g["P17_ringup_sweep"]:
        print(_row(r))
    print(_row(g["P17_pinned_cavity"]).replace("  ", "  Ref ", 1))
    print(_row(g["P17_wall_ablation"]).replace("  ", "  Abl wall-OFF ", 1))
    print(_row(g["P17_memristive_ablation"]).replace("  ", "  Abl mem-OFF ", 1))
    print(f"P17 any P11: {g['P17_any_p11']} | any P17: {g['P17_any_p17']}")
    print("=" * 72)
    print("VERDICT:", g["verdict"])
    print("=" * 72)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "genesis_v17_moving_resonator.json"
    payload = {
        "smoke": smoke,
        "verdict": g["verdict"],
        "P17_transport_gain": g["P17_transport_gain"],
        "P12_gain_threshold": g["P12_gain_threshold"],
        "P17_any_p11": g["P17_any_p11"],
        "P17_any_p17": g["P17_any_p17"],
        "P17_best": asdict(g["P17_best"]),
        "P17_ringup_sweep": [asdict(r) for r in g["P17_ringup_sweep"]],
        "P17_pinned_cavity": asdict(g["P17_pinned_cavity"]),
        "P17_wall_ablation": asdict(g["P17_wall_ablation"]),
        "P17_memristive_ablation": asdict(g["P17_memristive_ablation"]),
    }
    path.write_text(json.dumps(payload, indent=2))
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()

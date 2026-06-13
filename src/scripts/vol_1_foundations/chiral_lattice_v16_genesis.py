#!/usr/bin/env python3
"""Genesis v16 — cavity + Compton ring-up + P11 remanence driver."""

from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

from ave.core.chiral_lattice_v16 import V16P16Result, v16_gates

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def _row(c: V16P16Result) -> str:
    return (
        f"  {c.label}: n_drive={c.n_drive} ({c.n_drive_mult}×Nτ) "
        f"E_frac={c.E_frac_interior:.3f} width×={c.width_ratio:.2f} "
        f"E_persist={c.E_persist_ratio:.3f} A_persist={c.A_persist_ratio:.3f} "
        f"P11={c.p11_pass} P13={c.p13_pass} bin={c.bin_label}"
    )


def main() -> None:
    smoke = "--smoke" in sys.argv
    L = 8 if smoke else 10
    g = v16_gates(L=L, smoke=smoke)
    tag = "(SMOKE)" if smoke else "(PRODUCTION)"
    print("=" * 72)
    print("GENESIS v16 — CAVITY + COMPTON RING-UP + P11", tag)
    print("Engine:", g["engine_class"])
    print(f"L={g['L_p16']} | Nτ={g['tau_steps']}")
    print("=" * 72)
    for r in g["P16_ringup_sweep"]:
        print(_row(r))
    print(_row(g["P16_wall_ablation"]).replace("  ", "  Ablation wall-OFF ", 1))
    print(_row(g["P16_memristive_ablation"]).replace("  ", "  Ablation mem-OFF ", 1))
    print(f"P16 any P11: {g['P16_any_p11']} | mem ablation isolates: {g['P16_mem_ablation_ok']}")
    print("=" * 72)
    print("VERDICT:", g["verdict"])
    print("=" * 72)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "genesis_v16_cavity_ringup.json"
    payload = {
        "smoke": smoke,
        "verdict": g["verdict"],
        "P16_any_p11": g["P16_any_p11"],
        "P16_mem_ablation_ok": g["P16_mem_ablation_ok"],
        "P16_best": asdict(g["P16_best"]),
        "P16_ringup_sweep": [asdict(r) for r in g["P16_ringup_sweep"]],
        "P16_wall_ablation": asdict(g["P16_wall_ablation"]),
        "P16_memristive_ablation": asdict(g["P16_memristive_ablation"]),
    }
    path.write_text(json.dumps(payload, indent=2))
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Genesis v14b — pocket-frame peak metric driver."""

from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

from ave.core.chiral_lattice_v14 import V14StackResult, v14b_gates

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def _row(c: V14StackResult) -> str:
    return (
        f"  {c.label}: disp={c.centroid_disp:.3f} E_frac={c.E_frac_interior:.3f} "
        f"width×={c.width_ratio:.2f} peak_g={c.peak_retention:.3f} "
        f"peak_p={c.peak_pocket_retention:.3f} metric={c.peak_metric} "
        f"P13={c.p13_pass} P12={c.p12_pass} P14={c.p14_pass}"
    )


def main() -> None:
    smoke = "--smoke" in sys.argv
    L = 8 if smoke else 10
    g = v14b_gates(L=L, smoke=smoke)
    tag = "(SMOKE)" if smoke else "(PRODUCTION)"
    print("=" * 72)
    print("GENESIS v14b — POCKET-FRAME PEAK GATE", tag)
    print("Engine:", g["engine_class"])
    print(f"L={g['L_p14']} | n_steps={g['n_steps']}")
    print(
        f"Full stack: peak_global={g['P14b_peak_global']:.4f} "
        f"peak_pocket={g['P14b_peak_pocket']:.4f} metric={g['P14b_peak_metric']}"
    )
    print("=" * 72)
    print(_row(g["P14_full_stack"]))
    print(_row(g["P14_pinned_cavity"]))
    print(
        f"Transport gain: {g['P14_transport_gain']:.3f} "
        f"(threshold {g['P14_gain_threshold']:.3f})"
    )
    print(f"P13 on comoving: {g['P13_on_comoving']} | P12: {g['P12_on_comoving']}")
    print("=" * 72)
    print("VERDICT:", g["verdict"])
    print("=" * 72)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "genesis_v14b_cavity_transport.json"
    payload = {
        "smoke": smoke,
        "verdict": g["verdict"],
        "P14b_peak_global": g["P14b_peak_global"],
        "P14b_peak_pocket": g["P14b_peak_pocket"],
        "P14b_peak_metric": g["P14b_peak_metric"],
        "P14_transport_gain": g["P14_transport_gain"],
        "P14_gain_threshold": g["P14_gain_threshold"],
        "P14_full_stack": asdict(g["P14_full_stack"]),
        "P14_pinned_cavity": asdict(g["P14_pinned_cavity"]),
    }
    path.write_text(json.dumps(payload, indent=2))
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()

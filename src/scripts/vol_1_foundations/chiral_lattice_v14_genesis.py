#!/usr/bin/env python3
"""Genesis v14 — cavity + comoving transport stack driver."""

from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

from ave.core.chiral_lattice_v14 import V14StackResult, v14_gates

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def _row(c: V14StackResult) -> str:
    return (
        f"  {c.label}: wall={c.bulk_wall_on} comoving={c.comoving_on} "
        f"disp={c.centroid_disp:.3f} E_frac={c.E_frac_interior:.3f} "
        f"width×={c.width_ratio:.2f} peak={c.peak_retention:.3f} "
        f"peak_p={c.peak_pocket_retention:.3f} ({c.peak_metric}) "
        f"P13={c.p13_pass} P12={c.p12_pass} P14={c.p14_pass}"
    )


def main() -> None:
    smoke = "--smoke" in sys.argv
    L = 8 if smoke else 10
    g = v14_gates(L=L, smoke=smoke)
    tag = "(SMOKE)" if smoke else "(PRODUCTION)"
    print("=" * 72)
    print("GENESIS v14 — CAVITY + COMOVING TRANSPORT STACK", tag)
    print("Engine:", g["engine_class"])
    print(f"L={g['L_p14']} | n_steps={g['n_steps']} | v_boost={g['v_boost']}")
    print("=" * 72)
    print(_row(g["P14_full_stack"]))
    print(_row(g["P14_pinned_cavity"]).replace("  ", "  Regression ", 1))
    print(_row(g["P14_open_comoving"]).replace("  ", "  Ablation ", 1))
    print(_row(g["P14_open_pinned"]).replace("  ", "  Ablation ", 1))
    print(_row(g["P14_op3_only_wall"]).replace("  ", "  Sensitivity ", 1))
    print(_row(g["P14_linear_control"]).replace("  ", "  Control ", 1))
    print(
        f"Transport gain (full−pinned): {g['P14_transport_gain']:.3f} "
        f"(threshold {g['P14_gain_threshold']:.3f})"
    )
    print(f"Open-srs gain (C−D): {g['P14_open_transport_gain']:.3f}")
    print(f"Op3-only gain (E−B): {g['P14_op3_transport_gain']:.3f}")
    if smoke and "P14_boost_sweep_gain" in g:
        print("Boost sweep gain:", g["P14_boost_sweep_gain"])
    print(
        f"v11 regression: bin={g['v11_regression'].bin_label} "
        f"P11={g['v11_regression'].p11_pass}"
    )
    print("=" * 72)
    print("P13 on comoving:", g["P13_on_comoving"])
    print("P12 on comoving:", g["P12_on_comoving"])
    print("P14 any PASS:", g["P14_any_pass"])
    print("VERDICT:", g["verdict"])
    print("=" * 72)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "genesis_v14_cavity_transport.json"
    payload = {
        "smoke": smoke,
        "verdict": g["verdict"],
        "P14_any_pass": g["P14_any_pass"],
        "P13_on_comoving": g["P13_on_comoving"],
        "P12_on_comoving": g["P12_on_comoving"],
        "P14_transport_gain": g["P14_transport_gain"],
        "P14_gain_threshold": g["P14_gain_threshold"],
        "P14_full_stack": asdict(g["P14_full_stack"]),
        "P14_pinned_cavity": asdict(g["P14_pinned_cavity"]),
        "P14_open_comoving": asdict(g["P14_open_comoving"]),
        "P14_op3_only_wall": asdict(g["P14_op3_only_wall"]),
        "P14_linear_control": asdict(g["P14_linear_control"]),
        "v11_regression_p11": g["v11_regression"].p11_pass,
    }
    if smoke and "P14_boost_sweep_gain" in g:
        payload["P14_boost_sweep_gain"] = g["P14_boost_sweep_gain"]
    path.write_text(json.dumps(payload, indent=2))
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()

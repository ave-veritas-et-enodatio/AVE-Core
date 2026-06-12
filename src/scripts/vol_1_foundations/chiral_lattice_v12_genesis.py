#!/usr/bin/env python3
"""Genesis v12 — boost-covariant transport driver (discrete srs comoving advection)."""

from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

from ave.core.chiral_lattice_v12 import V12P12Result, v12_gates

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def _p12_row(c: V12P12Result) -> str:
    return (
        f"  {c.label}: v={c.v_boost:.3f} comoving={c.comoving_on} "
        f"disp={c.centroid_disp:.3f} width×={c.width_ratio:.2f} "
        f"peak={c.peak_retention:.3f} P12={c.p12_pass}"
    )


def main() -> None:
    smoke = "--smoke" in sys.argv
    L = 8 if smoke else 10
    g = v12_gates(L=L, smoke=smoke)
    tag = "(SMOKE)" if smoke else "(PRODUCTION)"
    print("=" * 72)
    print("GENESIS v12 — BOOST-COVARIANT TRANSPORT", tag)
    print("Engine:", g["engine_class"])
    print(f"L={g['L_p12']} | v_boost={g['v_boost']} | n_steps={g['n_steps']}")
    print("=" * 72)
    print(_p12_row(g["P12_comoving"]))
    print(_p12_row(g["P12_pinned_ablation"]).replace("  ", "  Ablation ", 1))
    print(_p12_row(g["P12_memristive_ablation"]).replace("  ", "  Ablation ", 1))
    print(_p12_row(g["P12_linear_control"]).replace("  ", "  Control ", 1))
    print(
        f"v11 regression: bin={g['v11_regression'].bin_label} "
        f"P11={g['v11_regression'].p11_pass}"
    )
    print("=" * 72)
    print("P12 any PASS:", g["P12_any_pass"])
    print("P12 ablation FAIL:", g["P12_ablation_fails"])
    print("Linear apparatus (C4):", g["P12_linear_advances"])
    print("VERDICT:", g["verdict"])
    print("=" * 72)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "genesis_v12_boost_transport.json"
    payload = {
        "smoke": smoke,
        "verdict": g["verdict"],
        "P12_any_pass": g["P12_any_pass"],
        "P12_comoving": asdict(g["P12_comoving"]),
        "P12_pinned_ablation": asdict(g["P12_pinned_ablation"]),
        "P12_linear_control": asdict(g["P12_linear_control"]),
        "P12_memristive_ablation": asdict(g["P12_memristive_ablation"]),
        "v11_regression_p11": g["v11_regression"].p11_pass,
    }
    path.write_text(json.dumps(payload, indent=2))
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()

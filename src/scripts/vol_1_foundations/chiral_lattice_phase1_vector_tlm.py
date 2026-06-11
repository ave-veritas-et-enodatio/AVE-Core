#!/usr/bin/env python3
"""Genesis v9 Phase-1 — vector-TLM gate driver (P1–P4). No genesis / Op14 yet."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from ave.core.chiral_lattice_vector import phase1_gates

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def main() -> None:
    g = phase1_gates(L=8)
    print("=" * 72)
    print("GENESIS v9 PHASE-1 — VECTOR-TLM GATES (P1–P4)")
    print("=" * 72)
    print("P1 drift:", g["P1_drift"], " PASS:", g["P1_pass"])
    print("P1 isotropy rel err:", g["P1_isotropy"], " PASS:", g["P1_isotropy_pass"])
    for k, r in g["rotation"].items():
        print(
            f"  {k}: dθ/step={np.degrees(r.dtheta_per_step):+.4f} deg  "
            f"writhe={r.writhe:+.4e}  total={np.degrees(r.dtheta_total):+.2f} deg"
        )
    print("P2 PASS:", g["P2_pass"])
    print("P3 PASS:", g["P3_pass"])
    print("P4 PASS:", g["P4_pass"])
    all_pass = g["P1_pass"] and g["P1_isotropy_pass"] and g["P2_pass"] and g["P3_pass"] and g["P4_pass"]
    print("=" * 72)
    print("PHASE-1 VECTOR-TLM (P1–P4):", "ALL PASS" if all_pass else "FAIL — see gates")
    print("P5/P6 (genesis) deferred to Phase-2 per freeze scope.")
    print("=" * 72)
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "genesis_v9_phase1_vector_tlm.json"
    payload = {
        "P1_drift": {k: float(v) for k, v in g["P1_drift"].items()},
        "P1_pass": bool(g["P1_pass"]),
        "P2_pass": bool(g["P2_pass"]),
        "P3_pass": bool(g["P3_pass"]),
        "P4_pass": bool(g["P4_pass"]),
        "rotation_deg_per_step": {
            k: float(np.degrees(v.dtheta_per_step)) for k, v in g["rotation"].items()
        },
    }
    path.write_text(json.dumps(payload, indent=2))
    print(f"[artifact] {path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Genesis v18 — DEPRECATED driver; use loop_gap_harness_genesis.py instead.

Canonical post-pivot entry:
  src/scripts/vol_1_foundations/loop_gap_harness_genesis.py

This driver delegates to the unified harness for backward compatibility.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from ave.core.loop_gap_harness import loop_gap_battery

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def main() -> None:
    smoke = "--smoke" in sys.argv
    L = 10 if smoke else 14
    result = loop_gap_battery(N=L, smoke=smoke)
    result["smoke"] = smoke
    result["N"] = L
    result["deprecated_driver"] = "genesis_v18_coupled.py → loop_gap_harness"

    tag = "(SMOKE)" if smoke else "(PRODUCTION)"
    print("=" * 72)
    print("GENESIS v18 — DELEGATES TO LOOP GAP HARNESS", tag)
    print("=" * 72)
    print("VERDICT:", result["verdict"])
    print("=" * 72)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "genesis_v18_operator_native.json"
    path.write_text(json.dumps(result, indent=2))
    print(f"Wrote {path} (canonical: loop_gap_harness_battery.json)")


if __name__ == "__main__":
    main()

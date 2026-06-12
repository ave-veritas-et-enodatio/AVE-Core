#!/usr/bin/env python3
"""LOOP GAP unified harness driver — canonical K4 genesis probe post-pivot.

Replaces per-version drivers (v18+) for rank-1–4 closure work.
srs chiral_lattice_v{9..17} is FROZEN.

DAG: _orchestration/2026-06-12_loop-gap-engine-dag.md
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from ave.core.loop_gap_harness import loop_gap_battery
from ave.core.loop_gap_seeds import SeedMode

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def main() -> None:
    smoke = "--smoke" in sys.argv
    bulk = "--bulk" in sys.argv
    seed: SeedMode = "photon_lock"
    for arg in sys.argv[1:]:
        if arg.startswith("--seed="):
            seed = arg.split("=", 1)[1]
    N = 10 if smoke else 14
    result = loop_gap_battery(
        N=N,
        smoke=smoke,
        primary_seed=seed,  # type: ignore[arg-type]
        bulk_density_on=bulk,
    )
    # seed validated by loop_gap_battery; CLI passes pair|photon_lock|graded_a0
    result["smoke"] = smoke
    result["N"] = N

    tag = "(SMOKE)" if smoke else "(PRODUCTION)"
    print("=" * 72)
    print("LOOP GAP UNIFIED HARNESS", tag)
    print(
        f"N={N} platform=VacuumEngine3D rank_profile=4 "
        f"seed={result.get('primary_seed', seed)} "
        f"phase={result.get('harness_phase', 2)} bulk={result.get('bulk_density_on', False)} "
        f"srs=FROZEN@v17"
    )
    print("=" * 72)
    for row in result["rank_sweep"]:
        print(
            f"  {row['label']}: V_inc={row['v_inc_peak']:.3e} "
            f"Γ_min={row['gamma_min_drive']:.3f} "
            f"E_persist={row['E_persist_ratio']:.3f} "
            f"R1={row['rank1_pass']} R1b={row.get('rank1b_pass', False)} "
            f"R3={row['rank3_pass']} R4={row['rank4_pass']} "
            f"ch={row.get('channel_primary', 'EM+shear')}"
        )
    if result.get("bulk_ablation"):
        bo = result["bulk_ablation"]["bulk_ON"]
        bf = result["bulk_ablation"]["bulk_OFF"]
        bc = result["bulk_ablation"].get("bulk_circulation", {})
        print(
            f"  bulk_F1: ON rho_min={bo['rho_bar_min_end']:.4f} "
            f"OFF rho_min={bf['rho_bar_min_end']:.4f} pass={result.get('bulk_f1_pass')}"
        )
        if bc:
            print(
                f"  bulk_motor: rho_min_drive={bc.get('rho_bar_min_drive', 0):.4f} "
                f"R1b={bc.get('rank1b_pass', False)} ch={bc.get('channel_primary', '')}"
            )
        print(f"  bulk_F2 channel-tagged: {result.get('bulk_f2_channel_tagged')}")
    print("=" * 72)
    print("VERDICT:", result["verdict"])
    print("Best:", result["best_arm"])
    print("=" * 72)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "loop_gap_harness_battery.json"
    path.write_text(json.dumps(result, indent=2))
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()

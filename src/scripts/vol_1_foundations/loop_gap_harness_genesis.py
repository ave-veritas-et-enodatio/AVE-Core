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

from ave.core.loop_gap_harness import (
    loop_gap_battery,
    loop_gap_dlite_battery,
    loop_gap_scalar_battery,
)
from ave.core.loop_gap_seeds import A_YIELD, SeedMode

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def main() -> None:
    scalar = "--smoke-scalar" in sys.argv or "--scalar" in sys.argv
    dlite = "--dlite" in sys.argv
    smoke = "--smoke" in sys.argv or dlite or scalar
    bulk = "--bulk" in sys.argv or dlite or scalar
    seed: SeedMode = "photon_lock"
    for arg in sys.argv[1:]:
        if arg.startswith("--seed="):
            seed = arg.split("=", 1)[1]
    N = 10 if smoke else 14
    if scalar:
        result = loop_gap_scalar_battery(N=N)
        result["smoke"] = True
        result["scalar"] = True
        print("=" * 72)
        print("LOOP GAP UNIFIED HARNESS (C′ SMOKE-SCALAR)")
        print(
            f"N={N} platform=VacuumEngine3D phase=C-prime "
            f"frac={result.get('scalar_seed_frac', 0.85)} bulk=True srs=FROZEN@v17"
        )
        for row in result["arms"]:
            print(
                f"  {row['label']}: V_inc={row['v_inc_peak']:.3e} "
                f"Γ_bulk={row['gamma_bulk_min_drive']:.3f} "
                f"|ω|={row['max_omega_end']:.3e} "
                f"A²_V={row['a2_v_peak']:.4f} "
                f"H_drift={row['h_drift_rel']:.3e} "
                f"OP2={row['op2_bin']} SCALAR={row.get('scalar_bin', '')}"
            )
        fals = result.get("falsifiers", {})
        print(
            f"  F1={fals.get('F1_scalar_seed')} "
            f"F2={fals.get('F2_v_to_omega_source')} "
            f"F3={fals.get('F3_op2_composite')}"
        )
        print("=" * 72)
        print("VERDICT:", result["verdict"], "| OP2:", result["op2_bin"])
        print("Primary:", result["primary_arm"])
        if not result.get("gap_c_coupling_wired"):
            print("NOTE: GAP-C (S4) not wired — C′5 pending")
        print("=" * 72)
        OUT.mkdir(parents=True, exist_ok=True)
        path = OUT / "loop_gap_harness_scalar_battery.json"
        path.write_text(json.dumps(result, indent=2))
        print(f"Wrote {path}")
        return
    if dlite:
        result = loop_gap_dlite_battery(N=N)
        result["smoke"] = True
        result["dlite"] = True
    else:
        result = loop_gap_battery(
            N=N,
            smoke=smoke,
            primary_seed=seed,  # type: ignore[arg-type]
            bulk_density_on=bulk,
        )
        result["smoke"] = smoke
        result["N"] = N

    tag = "(D-LITE)" if dlite else ("(SMOKE)" if smoke else "(PRODUCTION)")
    print("=" * 72)
    print("LOOP GAP UNIFIED HARNESS", tag)
    if dlite:
        print(
            f"N={N} platform=VacuumEngine3D phase=D-lite "
            f"target_A_front={A_YIELD:.6f} bulk=True srs=FROZEN@v17"
        )
        for row in result["arms"]:
            print(
                f"  {row['label']}: V_inc={row['v_inc_peak']:.3e} "
                f"Γ_bulk_min={row['gamma_bulk_min_drive']:.3f} "
                f"proxy_Γ={row['proxy_gamma_min']:.3f} "
                f"A_seed={row['achieved_a_front_seed']:.4f} "
                f"OP2={row['op2_bin']} ch={row.get('channel_primary', '')}"
            )
        print("=" * 72)
        print("VERDICT:", result["verdict"], "| OP2:", result["op2_bin"])
        print("Primary:", result["primary_arm"])
        print("=" * 72)
        OUT.mkdir(parents=True, exist_ok=True)
        path = OUT / "loop_gap_harness_dlite_battery.json"
        path.write_text(json.dumps(result, indent=2))
        print(f"Wrote {path}")
        return

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

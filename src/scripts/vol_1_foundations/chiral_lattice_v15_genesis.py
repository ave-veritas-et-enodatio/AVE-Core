#!/usr/bin/env python3
"""Genesis v15 — nucleation from latent heat (Lane A) driver."""

from __future__ import annotations

import json
import sys
from dataclasses import asdict
from pathlib import Path

from ave.core.chiral_lattice_v15 import V15P15Result, v15_gates

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"


def _row(c: V15P15Result) -> str:
    return (
        f"  {c.label}: latent={c.latent_on} seed={c.seed_mode} "
        f"wall={c.bulk_wall_on} r_yield*={c.r_yield_seed_peak:.3f} "
        f"A2_vsnap*={c.A2_seed_peak:.5f} E_frac={c.E_frac_interior:.3f} "
        f"width×={c.width_ratio:.2f} P15-N={c.p15n_pass}"
    )


def main() -> None:
    smoke = "--smoke" in sys.argv
    L = 8 if smoke else 10
    g = v15_gates(L=L, smoke=smoke)
    tag = "(SMOKE)" if smoke else "(PRODUCTION)"
    print("=" * 72)
    print("GENESIS v15 — NUCLEATION FROM LATENT HEAT (LANE A)", tag)
    print("Engine:", g["engine_class"])
    prov = g["provenance"]
    print(
        f"L={g['L_p15']} | steps={prov['timing']['n_steps_total']} "
        f"| latent_steps={prov['timing']['n_latent_steps']} "
        f"| path={prov['injection_path']}"
    )
    loc = prov["local"]
    cos = prov["cosmic"]
    print(f"  units: {prov['unit_system']}")
    print(
        f"  seed r_yield={loc['seed_r_yield']:.3f} → target r_yield={loc['target_r_yield']:.4f} "
        f"(knee √2 native)"
    )
    print(
        f"  ΔE_native/step/pair={loc['delta_e_native_per_step_pair']:.4f} "
        f"(E_unit=m_e c²); deficit={loc['e_deficit_native']:.2f} native"
    )
    print(
        f"  P15 floor: r_yield≥{loc['r_yield_threshold']:.4f} "
        f"(A²_vsnap≥{loc['a2_vsnap_threshold']:.6f})"
    )
    print(
        f"  cosmic/cell/τ native={cos['e_per_cell_per_tau_native']:.3e} "
        f"/ yield={cos['e_yield_kinetic_native']:.4f} "
        f"ratio={cos['ratio_to_yield']:.3e} (logged only)"
    )
    print("=" * 72)
    for key in ("P15_A_cosmic", "P15_B_heal", "P15_C_photon", "P15_D_no_wall", "P15_E_single"):
        print(_row(g[key]))
    print(f"P15-H heal pass: {g['P15_H_heal_pass']}")
    print(f"Photon ablation (C fails P15-N): {g['P15_photon_ablation']}")
    print(f"Wall ΔE_frac (A−D): {g['wall_E_frac_gain']:.3f}")
    print("=" * 72)
    print("VERDICT:", g["verdict"])
    print("=" * 72)

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / "genesis_v15_nucleation_latent.json"
    payload = {
        "smoke": smoke,
        "verdict": g["verdict"],
        "provenance": g["provenance"],
        "P15_H_heal_pass": g["P15_H_heal_pass"],
        "P15_photon_ablation": g["P15_photon_ablation"],
        "wall_E_frac_gain": g["wall_E_frac_gain"],
        "P15_A_cosmic": asdict(g["P15_A_cosmic"]),
        "P15_B_heal": asdict(g["P15_B_heal"]),
        "P15_C_photon": asdict(g["P15_C_photon"]),
        "P15_D_no_wall": asdict(g["P15_D_no_wall"]),
        "P15_E_single": asdict(g["P15_E_single"]),
    }
    path.write_text(json.dumps(payload, indent=2))
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()

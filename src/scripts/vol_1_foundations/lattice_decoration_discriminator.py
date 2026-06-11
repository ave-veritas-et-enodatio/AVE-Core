#!/usr/bin/env python3
"""
R3 — Lattice decoration discriminator driver.

Runs the three-arm battery (bare srs, bare diamond, decorated diamond) and
prints D1 partial bin assignment. SCOPE: Phase-0 extension only — no genesis.

Usage:
    PYTHONPATH=src python src/scripts/vol_1_foundations/lattice_decoration_discriminator.py
"""

from __future__ import annotations

import json
from pathlib import Path

from ave.core.lattice_decoration_discriminator import run_r3_battery

PROJECT_ROOT = next(p for p in Path(__file__).parents if (p / ".git").exists())
OUT = PROJECT_ROOT / "assets" / "sim_outputs"
OUT.mkdir(parents=True, exist_ok=True)


def main() -> None:
    res = run_r3_battery(L=6)
    print("=" * 72)
    print("R3 — LATTICE DECORATION DISCRIMINATOR")
    print("=" * 72)
    for arm in res.writhe_arms:
        print(f"  O1 writhe {arm.label:14s}: {arm.writhe:+.5e}  (n={arm.n_rings})")
    print(f"  O2 Bishop srs-R     : Δθ/L = {res.bishop_srs_right.rate_per_len_deg:+.3f} deg/unit")
    print(f"  O2 Bishop mirror    : Δθ/L = {res.bishop_srs_mirror.rate_per_len_deg:+.3f} deg/unit")
    print(f"  O2 Bishop diamond   : Δθ/L = {res.bishop_diamond.rate_per_len_deg:+.3f} deg/unit")
    for arm in res.decoration_arms:
        print(
            f"  O3 decoration κ={arm.kappa:+.4e}: signed_proxy={arm.signed_proxy:+.6e}  "
            f"mean_h={arm.mean_h:.3f}"
        )
    print(f"  ρ(decoration/srs Bishop) = {res.rho_decoration_vs_srs}")
    print("  Gates:")
    for k, v in res.gates.items():
        print(f"    {k}: {v}")
    print(f"  --> D1 PARTIAL BIN: {res.d1_bin}")
    print("  (Full D1 requires Phase-1 P4/P6 — see lattice-d1-test-gated epic)")
    print("=" * 72)

    payload = {
        "L": res.L,
        "writhe": {a.label: a.writhe for a in res.writhe_arms},
        "bishop_deg_per_unit": {
            "srs-R": res.bishop_srs_right.rate_per_len_deg,
            "srs-mirror": res.bishop_srs_mirror.rate_per_len_deg,
            "diamond": res.bishop_diamond.rate_per_len_deg,
        },
        "decoration": [
            {"kappa": a.kappa, "signed_proxy": a.signed_proxy} for a in res.decoration_arms
        ],
        "rho": res.rho_decoration_vs_srs,
        "gates": res.gates,
        "d1_bin": res.d1_bin,
    }
    out_path = OUT / "r3_lattice_decoration_discriminator.json"
    out_path.write_text(json.dumps(payload, indent=2))
    print(f"  [artifact] {out_path}")


if __name__ == "__main__":
    main()

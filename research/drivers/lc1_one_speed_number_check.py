#!/usr/bin/env python3
"""Gating number-check (G-DOC): LC-1 one-speed result-doc numerals vs the shipped JSON.

Lane: research/lc1-one-speed (Lorentz-compliance arc, LC-1)
Doc : research/2026-08-06_lc1-one-speed_result.md
JSON: research/drivers/lc1_one_speed_results.json

Every LOAD-BEARING numeral in the result doc is re-derived here from the shipped JSON
and compared against the literal string in the doc. A drift in either direction FAILS.

Each check names the EXACT scalar path it reads, and the mutation receipt perturbs
THAT SAME PATH -- so a check can never be "receipted" by a perturbation that misses it.

MUTATION RECEIPT (`--mutation-receipt`): perturb each checked JSON scalar and assert
the checker's expected literal changes. A checker that cannot fail is not a gate.

Regex engine used for the doc scans: Python `re` (named per the two-method discipline;
this checker uses literal containment, which is `str.__contains__`, not a regex).
"""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "research/2026-08-06_lc1-one-speed_result.md"
JSON_PATH = ROOT / "research/drivers/lc1_one_speed_results.json"

# (label, exact scalar path into the JSON, formatter)
SPEC = [
    # --- LEG A: the spectrum, and what forces the superluminality ----------
    ("vL/vT at K=2G",
     ["legA_christoffel", "vL_over_vT_at_K2G"], repr),
    ("vL/vT floor at K=0",
     ["legA_christoffel", "vL_over_vT_floor_at_K_zero"], repr),
    ("K=0 negative control",
     ["legA_christoffel", "vL_over_vT_at_K0_negative_control"], repr),
    ("longitudinal eigenvalue [100]",
     ["legA_christoffel", "spectrum_over_G_at_K2G", "[100]", 1], repr),
    ("n distinct eigenvalues [100]",
     ["legA_christoffel", "n_distinct_eigenvalues_at_K2G", "[100]"], str),
    ("G-SPEC fireability distinct count",
     ["legA_christoffel", "gspec_fireability_selftest_distinct_count"], str),
    # --- LEG B --------------------------------------------------------------
    ("Poisson absdiff vs NU_VAC",
     ["legB_poisson", "abs_diff"], repr),
    # --- LEG D --------------------------------------------------------------
    ("combine-member vT absdiff",
     ["legD_combine_member", "vT_member_absdiff"], repr),
    # --- LEG E: the arrival kinematics --------------------------------------
    ("chirp mass (equal-mass)",
     ["legE_arrival_kinematics", "chirp_mass_msun_equal_mass"], repr),
    ("light-travel time Myr",
     ["legE_arrival_kinematics", "nominal", "light_travel_time_myr"], repr),
    ("1 - c/v",
     ["legE_arrival_kinematics", "nominal", "one_minus_c_over_v"], repr),
    ("retarded offset Myr",
     ["legE_arrival_kinematics", "nominal", "retarded_offset_myr"], repr),
    ("f_GW at arrival Hz",
     ["legE_arrival_kinematics", "nominal", "f_gw_at_arrival_hz"], repr),
    ("band shortfall factor",
     ["legE_arrival_kinematics", "band_shortfall_factor_at_20hz"], repr),
    ("decades below 20 Hz",
     ["legE_arrival_kinematics", "decades_below_20hz"], repr),
    ("decades below 10 Hz",
     ["legE_arrival_kinematics", "band_bracket", "f_low=10.0", "decades_below_band"], repr),
    ("decades below 30 Hz",
     ["legE_arrival_kinematics", "band_bracket", "f_low=30.0", "decades_below_band"], repr),
    ("f at q=0.5",
     ["legE_arrival_kinematics", "chirp_bracket", "q=0.5", "f_gw_at_arrival_hz"], repr),
    ("f at D=26 Mpc",
     ["legE_arrival_kinematics", "distance_bracket", "D=26.0Mpc", "f_gw_at_arrival_hz"], repr),
    # --- LEG F --------------------------------------------------------------
    ("gap MeV",
     ["legF_cosserat_margins", "gap_energy_MeV"], repr),
    ("drive/gap",
     ["legF_cosserat_margins", "drive_over_gap"], repr),
    ("log10 drive/gap",
     ["legF_cosserat_margins", "log10_drive_over_gap"], repr),
    ("path in Yukawa reaches",
     ["legF_cosserat_margins", "path_in_yukawa_reaches"], repr),
    # --- FLAG-A + digest ----------------------------------------------------
    ("V_LONG/C_0",
     ["flagA_check", "V_LONG_over_C0"], repr),
    ("deterministic digest",
     ["digest"], str),
]


def get(d, path):
    node = d
    for k in path:
        node = node[k]
    return node


def put(d, path, value):
    node = d
    for k in path[:-1]:
        node = node[k]
    node[path[-1]] = value


def literals(d):
    return [(label, path, fmt(get(d, path))) for label, path, fmt in SPEC]


def main():
    d = json.loads(JSON_PATH.read_text())
    doc_text = DOC.read_text()
    print(f"[G-DOC] {DOC.relative_to(ROOT)} vs {JSON_PATH.relative_to(ROOT)}")

    fails = []
    for label, path, lit in literals(d):
        ok = lit in doc_text
        if not ok:
            fails.append((label, ".".join(str(p) for p in path), lit))
        print(f"  [{'OK ' if ok else 'FAIL'}] {label:<34} {lit}")

    rc = 0
    if "--mutation-receipt" in sys.argv:
        print("\n[mutation receipt] perturbing each checked JSON scalar at its own path")
        base = {lbl: lit for lbl, _p, lit in literals(d)}
        survivors = []
        for label, path, _lit in literals(d):
            m = copy.deepcopy(d)
            v = get(m, path)
            if isinstance(v, str):
                put(m, path, "0" * len(v))
            elif isinstance(v, bool):
                put(m, path, not v)
            else:
                put(m, path, v * 1.000001 + 1e-9)
            if {lbl: lit for lbl, _p2, lit in literals(m)}[label] == base[label]:
                survivors.append(label)
        if survivors:
            print(f"  [FAIL] mutation did not change: {survivors}")
            rc = 1
        else:
            print(f"  [OK ] all {len(base)} checks change under mutation — the gate can fail")

    if fails:
        print(f"\n[G-DOC] FAIL — {len(fails)} numeral(s) not found in the doc:")
        for label, path, lit in fails:
            print(f"    {label}  ({path})  expected literal: {lit}")
        return 1
    if rc:
        return rc
    print(f"\n[G-DOC] PASS — {len(SPEC)} load-bearing numerals reconciled.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

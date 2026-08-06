#!/usr/bin/env python3
"""Gating number-check: srs compression->twist result-doc numerals vs the shipped JSON.

Lane: research/srs-twist-coefficient (SVA pilot case 6, Grant ruling 2026-08-05).
Doc : research/2026-08-05_srs-twist-coefficient_result.md
JSON: research/drivers/srs_twist_coefficient_results.json

Every LOAD-BEARING numeral in the result doc is re-derived here from the shipped
JSON and compared against the literal string in the doc. A drift in either
direction FAILS.

MUTATION RECEIPT (`--mutation-receipt`): perturb each checked JSON source value
and assert the checker FAILS. A checker that cannot fail is not a gate.

Regex engine used for the doc scans: Python `re` (named per the lane's
two-method discipline; the companion POSIX-ERE scans live in the result doc S9).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "research/2026-08-05_srs-twist-coefficient_result.md"
JSON = ROOT / "research/drivers/srs_twist_coefficient_results.json"

RHO1 = "rho_bond=1 (Ax-3 match point)"
RHOK = "rho*=9.7734 (K=2G, GR-imported)"


def _gate(d, name):
    for g in d["gates"]:
        if g["gate"] == name:
            return g
    raise KeyError(name)


def checks(d):
    """(label, literal-string-that-must-appear-in-the-doc) derived from the JSON."""
    out = []
    b1 = d["load_path_B"][RHO1]["[001]"]
    bK = d["load_path_B"][RHOK]["[001]"]

    # --- the coefficient (headline) -------------------------------------
    out.append(("c2 [001] rho=1", f"+{b1['c2_signed_right']:.6e}".replace("e-03", "×10⁻³")))
    out.append(("c2 [001] rho=1 (verdict box mantissa)",
                f"{b1['c2_signed_right'] * 1e3:.4f}"))
    out.append(("c2 [001] rho* (6dp mantissa)", f"{bK['c2_signed_right']:.6e}".split("e")[0]))
    out.append(("fitted power [001] rho=1", f"{b1['power_of_q_in_kappa_over_eps']:.4f}"))
    out.append(("fitted power [110] rho=1", f"{d['load_path_B'][RHO1]['[110]']['power_of_q_in_kappa_over_eps']:.4f}"))
    out.append(("fitted power [111] rho=1", f"{d['load_path_B'][RHO1]['[111]']['power_of_q_in_kappa_over_eps']:.4f}"))

    # --- constitutive ----------------------------------------------------
    c = d["constitutive"]
    out.append(("alpha relrot modulus", f"{c[RHO1]['alpha_relrot_modulus']:.16g}"))
    out.append(("B chiral coupling rho=1", f"{c[RHO1]['B_chiral_coupling']:.4e}".split("e")[0]))
    out.append(("B chiral coupling rho*", f"{c[RHOK]['B_chiral_coupling']:.4e}".split("e")[0]))

    # --- lockstep + S_kappa(wall) ----------------------------------------
    rows = {(r["gradient_scale"], r["operating_point"]): r for r in d["lockstep"]["rows"]}
    ceil1 = rows[("q*ell_node = 1 (single-node gradient; the ABSOLUTE ceiling)", RHO1)]
    ceilK = rows[("q*ell_node = 1 (single-node gradient; the ABSOLUTE ceiling)", RHOK)]
    out.append(("S_kappa(wall) ceiling rho=1", f"{ceil1['S_kappa_at_wall']:.15f}"))
    out.append(("S_kappa(wall) ceiling rho*", f"{ceilK['S_kappa_at_wall']:.15f}"))
    out.append(("lockstep ratio ceiling rho=1", f"{ceil1['lockstep_ratio_dLL_over_dCC']:.2e}".split("e")[0]))
    rsat = rows[("solar r_sat = 7GM/c^2 = 1.03e4 m", RHO1)]
    out.append(("A_mu/A_eps at solar r_sat", f"{rsat['A_mu_over_A_eps']:.2e}".split("e")[0]))

    # --- gates ------------------------------------------------------------
    g2 = _gate(d, "G2")
    out.append(("G2 symmetric C11", f"{g2['C11']:.7f}"))
    out.append(("G2 symmetric C44", f"{g2['C44']:.7f}"))
    out.append(("G2 acoustic longitudinal", f"{g2['KEEPBOTH_acoustic_reading']['Gamma_100_zz_longitudinal']:.7f}"))
    out.append(("G2 acoustic transverse", f"{g2['KEEPBOTH_acoustic_reading']['Gamma_100_transverse_eigs'][0]:.7f}"))
    g6 = _gate(d, "G6")
    out.append(("G6 ks0 kappa/eps", f"{g6['KEEPBOTH_matched_q']['ks0_kappa_over_eps']:.4e}".split("e")[0]))
    out.append(("G6 ks1 kappa/eps", f"{g6['KEEPBOTH_matched_q']['ks1_kappa_over_eps']:.4e}".split("e")[0]))
    out.append(("G6 suppression OOM", f"{g6['KEEPBOTH_matched_q']['suppression_OOM']:.2f}"))
    g7 = _gate(d, "G7")
    out.append(("G7 central spectrum mid", f"{g7['central_site_spectrum'][1]:.16f}"))
    out.append(("G7 global nullity", f"nullity **exactly {g7['global_nullity_lever1']}**"))
    g4 = _gate(d, "G4")
    out.append(("G4 verdict", g4["verdict"]))

    # --- roll-off ---------------------------------------------------------
    roll = {r["A_wall"]: r for r in d["roll_off"]}
    out.append(("roll-off c2 at A=0.999", f"{roll[0.999]['abs_c2_001']:.2e}".split("e")[0]))
    out.append(("roll-off c2 at A=0.3 (non-monotone note)", f"{roll[0.3]['abs_c2_001']:.2e}".split("e")[0]))
    return out


def run(mutate=None):
    d = json.loads(JSON.read_text())
    if mutate is not None:
        d = mutate(d)
    doc = DOC.read_text()
    bad = []
    for label, literal in checks(d):
        if not re.search(re.escape(literal), doc):
            bad.append((label, literal))
    return bad


def main(argv):
    if "--mutation-receipt" in argv:
        muts = [
            ("c2 [001] rho=1",
             lambda d: _set(d, ["load_path_B", RHO1, "[001]", "c2_signed_right"], 9.9e-3)),
            ("alpha", lambda d: _set(d, ["constitutive", RHO1, "alpha_relrot_modulus"], 0.4242424242424242)),
            ("S_kappa ceiling", lambda d: _mut_lockstep(d)),
            ("G2 acoustic longitudinal",
             lambda d: _set_gate(d, "G2", ["KEEPBOTH_acoustic_reading",
                                           "Gamma_100_zz_longitudinal"], 0.4242424)),
            ("G6 suppression OOM",
             lambda d: _set_gate(d, "G6", ["KEEPBOTH_matched_q", "suppression_OOM"], 3.0)),
            ("G4 verdict", lambda d: _set_gate(d, "G4", ["verdict"], "GAPLESS")),
        ]
        ok = True
        for name, m in muts:
            bad = run(m)
            fired = len(bad) > 0
            print(f"[mutation] {name:32s} -> checker {'FAILS (good)' if fired else 'PASSES (BAD)'}")
            ok = ok and fired
        if not ok:
            print("MUTATION RECEIPT FAILED: a perturbed source did not trip the checker.")
            return 1
        print("MUTATION RECEIPT OK: every perturbed source trips the checker.")
        return 0

    bad = run()
    if bad:
        print("NUMBER-CHECK FAILED — doc numerals absent from the doc for:")
        for label, lit in bad:
            print(f"  - {label}: expected literal {lit!r}")
        return 1
    print(f"NUMBER-CHECK OK — {len(checks(json.loads(JSON.read_text())))} "
          "load-bearing numerals re-derived from the shipped JSON and found in the doc.")
    return 0


def _set(d, path, val):
    o = d
    for k in path[:-1]:
        o = o[k]
    o[path[-1]] = val
    return d


def _set_gate(d, gate, path, val):
    for g in d["gates"]:
        if g["gate"] == gate:
            o = g
            for k in path[:-1]:
                o = o[k]
            o[path[-1]] = val
    return d


def _mut_lockstep(d):
    for r in d["lockstep"]["rows"]:
        r["S_kappa_at_wall"] = 0.5
    return d


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

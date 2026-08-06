#!/usr/bin/env python3
"""Gating number check for the last-bond kernel-collapse lane.

Every back-ticked numeric in `research/2026-08-05_last-bond-kernel-collapse_result.md`
must be present in `last_bond_kernel_collapse_results.json`, or be DERIVED here from
registered JSON inputs by a stated formula. Wired into `make verify`.

Runtimes are deliberately NOT registered (`_runtime_sec` is machine-dependent; the #801 R3
lesson), and no back-ticks are used around them in the result doc.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from mpmath import mp, mpf, nstr, sqrt

mp.dps = 60

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
RESULTS = HERE / "last_bond_kernel_collapse_results.json"
DOC = REPO / "research" / "2026-08-05_last-bond-kernel-collapse_result.md"

FAILURES: list[str] = []


def check(label: str, doc_value: str, ref_value: str) -> None:
    if doc_value != ref_value:
        FAILURES.append(f"{label}: doc has `{doc_value}`, reference is `{ref_value}`")


def main(mutation_receipt: bool = False) -> int:
    d = json.loads(RESULTS.read_text(encoding="utf-8"))
    g = d["gates"]
    st = d["self_tests"]
    t3 = d["task3_continuum"]
    scan = d["task1_scan"]

    # ---- registered directly from the shipped JSON -------------------------
    reg: dict[str, str] = {
        "digest": d["_digest"],
        "n_rows": str(d["task2_row"]["n_rows"]),
        "G-BOND.max_k0": g["G-BOND"]["measured_max_abs_k0"],
        "G-ROW.max_resid": g["G-ROW"]["measured_max_abs_resid"],
        "G-ROW.n_points": str(g["G-ROW"]["n_points"]),
        "G-RHO.max_spread": g["G-RHO"]["measured_max_spread"],
        "G-RHO.n_groups": str(g["G-RHO"]["n_groups"]),
        "G-RHO2.exponent": g["G-RHO2"]["measured_exponent"],
        "G-COLD.max_sep": g["G-COLD"]["measured_max_sep"],
        "G-UNIT.LB": g["G-UNIT"]["measured_worst_LB"],
        "G-UNIT.N0": g["G-UNIT"]["measured_worst_N0"],
        "G-PLANE.max": g["G-PLANE"]["measured_max"],
        "G-PREC.worst": g["G-PREC"]["measured_worst_rel"],
        "G-COND.S2": g["G-COND"]["cancellation_free_S2"],
        "G-COND.naive": g["G-COND"]["naive_float64_1_minus_A2"],
        "G-NC-ARITH.max_k0": g["G-NC-ARITH"]["measured_max_k0"],
        "G-NC-ARITH.max_resid": g["G-NC-ARITH"]["measured_max_resid"],
        "G-SCAN.files_a": str(g["G-SCAN"]["method_a_scanned_files"]),
        "G-SCAN.files_b": str(g["G-SCAN"]["method_b_scanned_files"]),
        "G-SCAN.n_patterns": str(g["G-SCAN"]["n_patterns"]),
        "FT-BOND.k0": st["FT-BOND"]["measured_k0"],
        "FT-ROW.resid": st["FT-ROW"]["measured_abs_resid"],
        "FT-RHO.spread": st["FT-RHO"]["measured_spread"],
        "FT-PLANE.sep": st["FT-PLANE"]["measured_sep_at_om_1e-200"],
        "FT-ARITH.k0": st["FT-ARITH"]["measured_k0_arith"],
        "FT-ARITH.resid": st["FT-ARITH"]["measured_abs_resid"],
        "FT-SCAN.present_a": str(st["FT-SCAN"]["present_n_a"]),
        "FT-SCAN.present_b": str(st["FT-SCAN"]["present_n_b"]),
        "T3.rate_measured": t3["log_rate_measured_per_decade"],
        "T3.rate_predicted": t3["log_rate_predicted_half_ln10"],
        "T3.rate_rel_sep": t3["log_rate_rel_sep"],
        "T3.rhoa_1e-3": t3["rho_a_control_T_at_1e-3"],
        "T3.rhoa_1e-12": t3["rho_a_control_T_at_1e-12"],
        "T3.rhoa_ratio": t3["rho_a_control_growth_ratio"],
        "T3.sigma_plus": t3["traction"]["continuum_exponent_sigma_plus_READ"],
        "T3.sigma_minus": t3["traction"]["continuum_exponent_sigma_minus_READ"],
    }
    for row in t3["ladder"]:
        tag = row["ell_over_rsat"]
        reg[f"T3.ladder[{tag}].S_last"] = row["S_last_from_exact_S2"]
        reg[f"T3.ladder[{tag}].RHO_B"] = row["roundtrip_optical_RHO_B_over_rsat_c0"]
        reg[f"T3.ladder[{tag}].RHO_A"] = row["roundtrip_optical_RHO_A_over_rsat_c0"]

    # ---- DERIVED here from registered JSON inputs, by a stated formula -----
    # The PLANE-N0 short<->open crossover of the discrete row, under RHO-B:
    #   om*m_0 / Z_1 = (om/om_C) / S_last^2       [prereg section 3 units]
    #   S_cross      = sqrt(om/om_C)              [the S at which the two are equal]
    s2 = mpf(g["G-COND"]["cancellation_free_S2"])
    om_over_omc = mpf(d["_frozen_numerics"]["om_over_omC_grid"][1])  # 1e-19, the frozen middle rung
    reg["DERIVED.omm0_over_Z1_at_physical"] = nstr(om_over_omc / s2, 30, strip_zeros=False)
    reg["DERIVED.S_cross"] = nstr(sqrt(om_over_omc), 30, strip_zeros=False)
    reg["DERIVED.S_last_over_S_cross"] = nstr(sqrt(s2) / sqrt(om_over_omc), 30, strip_zeros=False)
    reg["DERIVED.n_patterns_agreeing"] = str(
        g["G-SCAN"]["n_patterns"] - len(g["G-SCAN"]["disagreements"])
    )
    reg["DERIVED.n_disagreements"] = str(len(g["G-SCAN"]["disagreements"]))

    # READ from the predecessor's own shipped result doc, never recomputed: the echo-v2
    # FLAG-CAUSAL three-way spread this lane cites in section 5.1.
    echo_doc = (
        REPO / "research" / "2026-08-05_echo-delay-v2-reach-through_result.md"
    ).read_text(encoding="utf-8")
    spread = "0.9921666107469662"
    if spread not in echo_doc:
        FAILURES.append(
            f"the cited echo-v2 spread `{spread}` is not present in that lane's own result doc"
        )
    reg["READ.echo_v2_flag_causal_spread"] = spread

    if not DOC.exists():
        print(f"[last-bond-check] result doc not found: {DOC}")
        return 1
    doc = DOC.read_text(encoding="utf-8")
    if mutation_receipt:
        # Perturb one registered numeral in a COPY of the doc; the checker must FAIL.
        # This proves the gate can fail on every invocation, not only when something
        # is already broken.
        victim = reg["G-PLANE.max"]
        mutated = victim[:-1] + ("7" if victim[-1] != "7" else "3")
        doc = doc.replace(f"`{victim}`", f"`{mutated}`", 1)

    # every back-ticked token that looks like a number must be a registered value
    ticked = set(re.findall(r"`([^`\n]+)`", doc))
    numeric = {
        t
        for t in ticked
        if re.fullmatch(r"[-+]?[0-9][0-9._eE+\-]*", t) and any(ch.isdigit() for ch in t)
    }
    known = set(reg.values()) | set(d["_frozen_numerics"]["S_last_grid"])
    known |= set(d["_frozen_numerics"]["rho_beyond_grid"])
    known |= set(d["_frozen_numerics"]["Z_beyond_over_Z1_grid"])
    known |= set(d["_frozen_numerics"]["om_over_omC_grid"])
    known |= set(d["_frozen_numerics"]["ell_over_rsat_ladder"])
    known |= set(d["_frozen_numerics"]["p_branches"].values())
    known |= {str(d["_frozen_numerics"]["dps"]), "-1", "+1", "0", "1", "2", "4", "1e-30", "1e-6",
              "1e-50", "1e-12", "1.9", "2.1", "1e-300", "1e-200", "0.5"}
    unknown = sorted(t for t in numeric if t not in known)
    if unknown:
        FAILURES.append(f"unregistered back-ticked numerics in the result doc: {unknown}")

    # and every registered value that the doc claims must actually appear
    must_appear = [
        "digest",
        "G-BOND.max_k0",
        "G-ROW.max_resid",
        "G-RHO.max_spread",
        "G-RHO2.exponent",
        "G-COLD.max_sep",
        "G-PLANE.max",
        "G-PREC.worst",
        "G-COND.S2",
        "T3.rate_measured",
        "T3.rate_predicted",
        "T3.rhoa_ratio",
        "DERIVED.omm0_over_Z1_at_physical",
        "DERIVED.S_cross",
    ]
    for key in must_appear:
        val = reg[key]
        if f"`{val}`" not in doc:
            FAILURES.append(f"{key}: registered value `{val}` does not appear back-ticked in the doc")

    # structural invariants the doc asserts
    if g["G-SCAN"]["pass"]:
        FAILURES.append("G-SCAN is recorded as PASS but the doc reports it as FAIL")
    if g["G-RHO2"]["pass"]:
        FAILURES.append("G-RHO2 is recorded as PASS but the doc reports it as FAIL")
    if st["FT-SCAN"]["fires"]:
        FAILURES.append("FT-SCAN is recorded as FIRING but the doc reports it as not firing")
    expected_disagreements = ["C3_Gc::ADJ_S", "C5_op10::ADJ_S", "C6_hopf::ADJ_S", "C7_refl::ADJ_S"]
    if sorted(g["G-SCAN"]["disagreements"]) != sorted(expected_disagreements):
        FAILURES.append(
            f"G-SCAN disagreement set changed: {sorted(g['G-SCAN']['disagreements'])}"
        )
    for gate in ("G-BOND", "G-ROW", "G-RHO", "G-COLD", "G-UNIT", "G-PLANE", "G-PREC",
                 "G-COND", "G-NC-SIGN", "G-NC-ECHO", "G-NC-ARITH"):
        if not g[gate]["pass"]:
            FAILURES.append(f"{gate} is recorded as FAIL but the doc reports it as PASS")
    for ft in ("FT-BOND", "FT-ROW", "FT-RHO", "FT-PLANE", "FT-ARITH", "FT-COND"):
        if not st[ft]["fires"]:
            FAILURES.append(f"{ft} is recorded as not firing but the doc reports it as firing")
    if scan["method_a_scanned_files"] != scan["method_b_scanned_files"]:
        FAILURES.append("the two scan methods no longer report equal file counts")

    if mutation_receipt:
        if FAILURES:
            print(
                "[last-bond-check] MUTATION RECEIPT OK \u2014 perturbing one registered numeral "
                f"made the checker FAIL on {len(FAILURES)} count(s); the gate can fail."
            )
            return 0
        print("[last-bond-check] MUTATION RECEIPT FAILED \u2014 a perturbed doc still PASSED.")
        return 1

    if FAILURES:
        print("[last-bond-check] FAIL")
        for f in FAILURES:
            print("   ·", f)
        return 1
    print(
        f"[last-bond-check] OK — {len(reg)} registered values "
        f"({sum(1 for k in reg if k.startswith('DERIVED'))} derived), "
        f"{len(numeric)} back-ticked numerics in the doc, all accounted for"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(mutation_receipt="--mutation-receipt" in sys.argv))

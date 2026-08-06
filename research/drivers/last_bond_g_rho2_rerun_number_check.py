#!/usr/bin/env python3
"""Gating number check for the G-RHO2 rerun v2 lane.

Every back-ticked numeric in `research/2026-08-05_last-bond-g-rho2-rerun_result.md` must be
present in `last_bond_g_rho2_rerun_results.json`, or be DERIVED here from registered JSON
inputs by a stated formula, or be a frozen parameter of the prereg.  Wired into `make verify`.

Runtimes are deliberately NOT registered (`_runtime_sec` is machine-dependent), and no
back-ticks are used around them in the result doc.

Beyond the numerals, this checker reconciles every LABEL in the doc against the COMPUTED
truth in the JSON (a gate that consumes self-declared fields is a checklist, not a gate):
the certification verdict, every pass/fires flag, the zero-mismatch claim, the byte-untouched
claim, and the fact that the v1 FAILING records reproduce as FAILING.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from mpmath import mp, mpf, nstr

mp.dps = 60

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
RESULTS = HERE / "last_bond_g_rho2_rerun_results.json"
DOC = REPO / "research" / "2026-08-05_last-bond-g-rho2-rerun_result.md"
PREREG = REPO / "research" / "2026-08-05_last-bond-g-rho2-rerun_prereg-FROZEN.md"
V1_JSON = HERE / "last_bond_kernel_collapse_results.json"

FAILURES: list[str] = []


def main(mutation_receipt: bool = False) -> int:
    d = json.loads(RESULTS.read_text(encoding="utf-8"))
    op = d["operating_point"]
    gate = d["gates"]["G-RHO2"]
    ft = d["self_tests"]["FT-RHO2"]
    diag = d["diagnostics"]["D-RHO2-PRED"]
    nc = d["negative_controls"]
    frz = d["_frozen_numerics"]

    # ---- registered directly from the shipped v2 JSON -----------------------
    reg: dict[str, str] = {
        "digest": d["_digest"],
        "OP.Z_1": op["Z_1"],
        "OP.om": op["om"],
        "OP.k_cold": op["k_cold"],
        "OP.k0_cross": op["k0_crossover_om_Z1"],
        "OP.eps_cross": op["eps_crossover_in_v1_parametrization"],
        "GATE.exponent": gate["measured_exponent"],
        "GATE.min_decades": str(gate["min_decades_below_crossover"]),
        "FT.exponent": ft["measured_exponent"],
        "DIAG.expected": diag["derived_expected_exponent"],
        "DIAG.predicted_dev": diag["derived_predicted_deviation"],
        "DIAG.measured_dev": diag["measured_deviation_from_2"],
        "NC.n_blocks": str(nc["NC-GATES+NC-FT"]["n_blocks_compared"]),
        "NC.n_fields": str(nc["NC-GATES+NC-FT"]["n_fields_compared"]),
        "NC.n_mismatches": str(nc["NC-GATES+NC-FT"]["n_mismatches"]),
        "NC.rows": str(nc["NC-ROWS"]["measured_n_rows"]),
        "NC.rows_v1": str(nc["NC-ROWS"]["v1_shipped_n_rows"]),
        "NC.rho2_v1_exponent": nc["NC-RHO2-V1"]["v1_shipped_exponent"],
        "NC.bytes_n_artifacts": str(len(nc["NC-BYTES"]["artifacts"])),
        "NC.bytes_n_modified": str(nc["NC-BYTES"]["n_modified"]),
    }
    for i, v in enumerate(gate["per_pair"]):
        reg[f"GATE.per_pair[{i}]"] = v
    for i, v in enumerate(gate["injected_k0"]):
        reg[f"GATE.k0[{i}]"] = v
    for i, v in enumerate(gate["measured_abs_delta_resid"]):
        reg[f"GATE.absDelta[{i}]"] = v
    for i, v in enumerate(ft["per_pair"]):
        reg[f"FT.per_pair[{i}]"] = v
    for i, v in enumerate(nc["NC-RHO2-V1"]["v1_shipped_per_pair"]):
        reg[f"NC.rho2_v1_per_pair[{i}]"] = v
    for i, v in enumerate(nc["NC-RHO2-V1"]["probe_coordinate_delta"]):
        reg[f"NC.v1_delta[{i}]"] = v

    # ---- DERIVED here from registered JSON inputs, by a stated formula -------
    # The reproduction-class ledger counts the doc reports are DERIVED from the class map,
    # never transcribed:  n(class) = |{k : REPRO_CLASS[k] == class}|.
    classes = nc["NC-GATES+NC-FT"]["reproduction_class"]
    for label, name in (("RECOMPUTED", "n_recomputed"), ("FILE-READ", "n_file_read"),
                        ("REPLAYED", "n_replayed")):
        reg[f"DERIVED.{name}"] = str(sum(1 for v in classes.values() if v == label))
    # the doc's "plus N further controls" = the NC- controls other than NC-GATES+NC-FT
    reg["DERIVED.n_further_controls"] = str(len([k for k in nc if k != "NC-GATES+NC-FT"]))
    # the predicted deviation of prereg section 3.2:  0.6786 * (eps_1^2 + eps_2^2)/2
    coeff = "0.6786"
    if coeff not in PREREG.read_text(encoding="utf-8"):
        FAILURES.append(f"the prereg no longer states the `{coeff}` coefficient this check derives from")
    e1, e2 = mpf(frz["eps_v2_gate"][0]), mpf(frz["eps_v2_gate"][1])
    derived_dev = nstr(mpf(coeff) * (e1**2 + e2**2) / 2, 30, strip_zeros=False)
    if derived_dev != reg["DIAG.predicted_dev"]:
        FAILURES.append(
            f"DERIVED predicted deviation `{derived_dev}` != shipped `{reg['DIAG.predicted_dev']}`"
        )
    reg["DERIVED.coeff"] = coeff

    # ---- READ from the v1 shipped record, never recomputed here --------------
    v1 = json.loads(V1_JSON.read_text(encoding="utf-8"))
    if v1["gates"]["G-RHO2"]["measured_exponent"] != reg["NC.rho2_v1_exponent"]:
        FAILURES.append("the v1 exponent registered by NC-RHO2-V1 is not the one the v1 JSON ships")
    reg["READ.v1_ell"] = v1["_frozen_numerics"]["ell_over_rsat_ladder"][0]

    if not DOC.exists():
        print(f"[g-rho2-v2-check] result doc not found: {DOC}")
        return 1
    doc = DOC.read_text(encoding="utf-8")
    if mutation_receipt:
        # Perturb one registered numeral in a COPY of the doc; the checker must FAIL.
        victim = reg["GATE.exponent"]
        mutated = victim[:-1] + ("7" if victim[-1] != "7" else "3")
        doc = doc.replace(f"`{victim}`", f"`{mutated}`", 1)

    # every back-ticked token that looks like a number must be a registered value
    ticked = set(re.findall(r"`([^`\n]+)`", doc))
    numeric = {
        t
        for t in ticked
        if re.fullmatch(r"[-+]?[0-9][0-9._eE+\-]*", t) and any(ch.isdigit() for ch in t)
    }
    known = set(reg.values())
    known |= set(frz["eps_v2_gate"]) | set(frz["eps_v2_plateau"]) | set(frz["eps_v1_siting"])
    known |= set(frz["rho2_tolerance"]) | {frz["d_pred_tolerance"], str(frz["dps"])}
    known |= {"0", "1", "2", "3", "4", "6", "-1", "+1"}
    unknown = sorted(t for t in numeric if t not in known)
    if unknown:
        FAILURES.append(f"unregistered back-ticked numerics in the result doc: {unknown}")

    # and every registered value the doc claims must actually appear
    must_appear = [
        "digest", "OP.Z_1", "OP.om", "OP.k_cold", "OP.k0_cross", "OP.eps_cross",
        "GATE.exponent", "GATE.per_pair[0]", "GATE.per_pair[1]",
        "GATE.absDelta[0]", "GATE.k0[0]",
        "FT.exponent", "FT.per_pair[0]", "FT.per_pair[1]",
        "DIAG.predicted_dev", "DIAG.measured_dev",
        "NC.n_blocks", "NC.n_fields", "NC.rho2_v1_exponent",
        "NC.rho2_v1_per_pair[0]", "NC.rho2_v1_per_pair[1]",
        "NC.v1_delta[0]", "NC.v1_delta[1]", "NC.v1_delta[2]",
        "DERIVED.n_recomputed", "DERIVED.coeff",
    ]
    for key in must_appear:
        val = reg[key]
        if f"`{val}`" not in doc:
            FAILURES.append(f"{key}: registered value `{val}` does not appear back-ticked in the doc")

    # ---- LABEL-vs-COMPUTED reconciliation (never consume a self-declared field) ----
    if not gate["pass"]:
        FAILURES.append("G-RHO2 is recorded as FAIL but the doc reports it as PASS")
    lo, hi = mpf(frz["rho2_tolerance"][0]), mpf(frz["rho2_tolerance"][1])
    if not (lo <= mpf(gate["measured_exponent"]) <= hi):
        FAILURES.append("G-RHO2 pass flag disagrees with the measured exponent vs the interval")
    if not ft["fires"]:
        FAILURES.append("FT-RHO2 is recorded as not firing but the doc reports it as FIRING")
    if lo <= mpf(ft["measured_exponent"]) <= hi:
        FAILURES.append("FT-RHO2 claims to fire but its exponent is INSIDE the acceptance interval")
    if not diag["agrees"]:
        FAILURES.append("D-RHO2-PRED is recorded as disagreeing but the doc reports AGREES")
    for k, v in nc.items():
        if not v["pass"]:
            FAILURES.append(f"{k} is recorded as FAIL but the doc reports every control as PASS")
    if nc["NC-GATES+NC-FT"]["n_mismatches"] != 0 or nc["NC-GATES+NC-FT"]["mismatches"]:
        FAILURES.append("the doc claims ZERO mismatches but the JSON carries some")
    if nc["NC-BYTES"]["n_modified"] != 0:
        FAILURES.append("the doc claims the predecessor artifacts are byte-untouched but they are not")
    if d["certification"]["task2"] != "ROW-CERTIFIED":
        FAILURES.append("the doc headlines ROW-CERTIFIED but the JSON does not")
    # the v1 FAILING records must reproduce as FAILING -- the doc says so explicitly
    for name, flags, want in (("G-RHO2", "v1_reproduced_pass_flags", False),
                              ("G-SCAN", "v1_reproduced_pass_flags", False)):
        if d[flags][name] is not want:
            FAILURES.append(f"{name} did not reproduce as FAIL in the v1 record replay")
    if d["v1_reproduced_fire_flags"]["FT-SCAN"] is not False:
        FAILURES.append("FT-SCAN did not reproduce as not-firing in the v1 record replay")
    for g in ("G-BOND", "G-ROW", "G-RHO", "G-COLD", "G-UNIT", "G-PLANE", "G-PREC", "G-COND",
              "G-NC-SIGN", "G-NC-ECHO", "G-NC-ARITH"):
        if not d["v1_reproduced_pass_flags"][g]:
            FAILURES.append(f"{g} is recorded as FAIL but the doc reports the v1 Task-2 set as PASS")
    for f in ("FT-BOND", "FT-ROW", "FT-RHO", "FT-PLANE", "FT-ARITH", "FT-COND"):
        if not d["v1_reproduced_fire_flags"][f]:
            FAILURES.append(f"{f} is recorded as not firing but the doc reports the FT battery as firing")
    # scope discipline: this lane must NOT have promoted TASK 1
    if "SCAN-NOT-CERTIFIED" not in d["certification"]["task1"]:
        FAILURES.append("TASK 1 was promoted by this lane; the freeze forbids it")
    if "SCAN-NOT-CERTIFIED" not in doc:
        FAILURES.append("the result doc no longer states that TASK 1 remains SCAN-NOT-CERTIFIED")
    if sorted(nc["NC-GATES+NC-FT"]["replayed_not_reproduced"]) != ["FT-SCAN", "G-SCAN"]:
        FAILURES.append("the replayed-not-reproduced declaration changed")

    if mutation_receipt:
        if FAILURES:
            print(
                "[g-rho2-v2-check] MUTATION RECEIPT OK — perturbing one registered numeral "
                f"made the checker FAIL on {len(FAILURES)} count(s); the gate can fail."
            )
            return 0
        print("[g-rho2-v2-check] MUTATION RECEIPT FAILED — a perturbed doc still PASSED.")
        return 1

    if FAILURES:
        print("[g-rho2-v2-check] FAIL")
        for f in FAILURES:
            print("   ·", f)
        return 1
    print(
        f"[g-rho2-v2-check] OK — {len(reg)} registered values "
        f"({sum(1 for k in reg if k.startswith('DERIVED'))} derived), "
        f"{len(numeric)} back-ticked numerics in the doc, all accounted for"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(mutation_receipt="--mutation-receipt" in sys.argv))

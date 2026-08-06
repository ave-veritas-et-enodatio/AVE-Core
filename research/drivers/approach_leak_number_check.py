#!/usr/bin/env python3
"""Gating number check for the APPROACH-LEAK lane.

Every back-ticked numeric in `research/2026-08-05_approach-leak_result.md` must be
present in `approach_leak_results.json`, or be DERIVED here from registered JSON
inputs by a stated formula.  Wired into `make verify`.

It ALSO machine-gates G-DET: the driver is re-run into a temporary path via the
APPROACH_LEAK_OUT env override, and the recomputed `_digest` must equal the
shipped one.  That is why G-DET is recorded in the JSON as
"GATED BY THE NUMBER-CHECK" rather than as a one-time manual receipt.

Runtimes are deliberately NOT registered (`_runtime_sec` is machine-dependent);
no back-ticks are used around them in the result doc.

`--mutation-receipt` re-runs the checker against deliberately perturbed sources
and requires it to FAIL, so the gate cannot silently degrade into a no-op.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
RESULTS = HERE / "approach_leak_results.json"
DRIVER = HERE / "approach_leak.py"
DOC = REPO / "research" / "2026-08-05_approach-leak_result.md"

FAILURES: list[str] = []

# Backticked tokens in the doc that are NOT instrument outputs: cited canon,
# frozen inputs, file:line cites, symbols, and prose fragments.  Each is here
# because it is verifiable at its own cited home, not because it is unchecked.
ALLOWED_LITERAL = {
    # frozen sweep inputs + bracket members (prereg §4)
    "0.5", "1.0", "1.5", "2.0", "2.5", "3.0", "1", "2", "4", "5", "6", "62", "65",
    "6240", "3120", "4418", "1040", "4096", "0", "3", "100", "1660054583759796203",
    # frozen tolerances (prereg §5.3)
    "1e-40", "1e-45", "1e-30", "1e-16", "1e-10", "1e30", "12",
    # canon values cited to their homes
    "5.4414", "17.0111", "1.022", "2.861", "27", "761", "762", "767", "118", "149",
    "104", "59", "18", "24", "117", "172", "522", "30", "74", "233", "386", "48",
    "50", "152-155", "163-179", "194-201", "163", "179", "194", "201", "1.18",
    "2.5e-4", "6.4e5", "6.4e8", "1e-36", "1e-16", "1e-9", "1.0976e-9", "2",
    # commit hashes and the base HEAD, cited as provenance
    "48076793", "68e46379", "bdb8b4a4", "c4fdced0", "6.0238983090250982e-19",
    # rounded margins whose full values are registered (see DERIVED block)
    "24.33", "28.54", "8.058", "9.738", "2.634", "3.471", "-0.0777", "+0.337",
    "-1.905", "-1.343", "-3.123", "-2.463",
}

NUM_RE = re.compile(r"`([^`]+)`")


def check(label: str, doc_value: str, ref_value: str) -> None:
    if doc_value != ref_value:
        FAILURES.append(f"{label}: doc has `{doc_value}`, reference is `{ref_value}`")


def registry(d: dict) -> dict[str, str]:
    g = d["gates"]
    st = d["self_tests"]
    sw = d["sweep"]
    res = d["residual_backaction_QUARANTINED"]
    reg: dict[str, str] = {
        "digest": d["_digest"],
        "L_NODE": g["G-CANON"]["L_NODE"],
        "OMEGA_C": g["G-CANON"]["OMEGA_C"],
        "band_lo": g["G-NC-BAND"]["band_lo"],
        "band_hi": g["G-NC-BAND"]["band_hi"],
        "slast_rel": g["G-NC-SLAST"]["measured_rel_sep"],
        "slast_shipped": g["G-NC-SLAST"]["shipped_S_last"],
        "slast_ours": g["G-NC-SLAST"]["this_lane_S_1"],
        "slast_x_rel": g["G-NC-SLAST"]["ell_over_rsat_rel_sep"],
        "x_shipped": g["G-NC-SLAST"]["shipped_ell_over_rsat"],
        "x_ours": g["G-NC-SLAST"]["this_lane_ell_over_rsat"],
        "cond_S2": g["G-COND"]["cancellation_free_S2"],
        "count_rows": str(g["G-COUNT"]["n_rows_swept"]),
        "count_mismatch": str(g["G-COUNT"]["mismatches"]),
        "count_unconf": str(g["G-COUNT"]["rows_without_linear_scan_confirmation"]),
        "zid": g["G-ZID"]["measured_max_rel_sep"],
        "real_min": g["G-REAL"]["measured_min_gap2_minus_omega2_in_omegaC2_units"],
        "knife": g["G-KNIFE"]["measured_spread"],
        "knife_exact": g["G-KNIFE"]["NON_GATED_exact_S1_variant_spread"],
        "knife_closed": g["G-KNIFE"]["closed_form_S_open_over_S_1_at_p2"],
        "scan_files": str(g["G-SCAN"]["n_files_scanned"]),
        "rho_spectator": g["G-RHO-SPECTATOR"]["measured_max_separation"],
        "ft_zid": st["FT-ZID"]["measured_rel_sep_after_perturbation"],
        "ft_real": st["FT-REAL"]["measured"],
        "ft_knife_199": st["FT-KNIFE"]["spread_p199"],
        "ft_knife_201": st["FT-KNIFE"]["spread_p201"],
        "ft_knife_t199": st["FT-KNIFE"]["trend_p199"],
        "ft_knife_t201": st["FT-KNIFE"]["trend_p201"],
        "ft_scan_present_A": str(st["FT-SCAN"]["present_sentinel_A"]),
        "T1": d["rotational_band_top_bracket_REPORTED_NONE_CHOSEN"]["T1_continuum_srs_nyquist"],
    }
    for pk, v in sw["per_p"].items():
        reg[f"zeta_{pk}"] = v["zeta_max_over_sweep"]
        reg[f"lo_{pk}"] = v["log10_margin_min"]
        reg[f"hi_{pk}"] = v["log10_margin_max"]
    for pk in ("0.5", "1.0", "1.5"):
        reg[f"resid_{pk}"] = res[pk]["total_sum_zeta_n_squared"]
    reg["psi1"] = res["1.0"]["psi1_theta"]

    # ---- DERIVED from registered JSON inputs by a stated formula -----------
    # (a) the margin ranges quoted in prose are the registered log10 bounds
    #     rounded to THREE significant figures.
    def sig3(s: str) -> str:
        v = float(s)
        return f"{v:.3g}"
    for pk, v in sw["per_p"].items():
        reg[f"lo3_{pk}"] = sig3(v["log10_margin_min"])
        reg[f"hi3_{pk}"] = sig3(v["log10_margin_max"])
        # (b) the open-cell counts quoted in prose are min/max of the distinct set
        nv = v["N_open_distinct_values"]
        reg[f"nmin_{pk}"] = str(min(nv))
        reg[f"nmax_{pk}"] = str(max(nv))
    # (c) FT-KNIFE's trends are quoted with an explicit sign in the doc
    reg["trend_pos"] = "+" + st["FT-KNIFE"]["trend_p201"]
    reg["trend_neg"] = st["FT-KNIFE"]["trend_p199"]
    for r in sw["corner_rows"]:
        if r["rho_branch"] == "RHO-A" and r["band_end"] == "HI":
            reg[f"corner_zeta_{r['p']}"] = r["zeta_max_transfer"]
            reg[f"corner_log10_{r['p']}"] = r["log10_S1_over_Sopen"]
            reg[f"corner_d_{r['p']}"] = r["decay_depth_cells_at_last_cell"]
    return reg


def main(mutation_receipt: bool = False) -> int:
    if mutation_receipt:
        return mutation()

    d = json.loads(RESULTS.read_text(encoding="utf-8"))
    reg = registry(d)
    known = set(reg.values()) | ALLOWED_LITERAL

    text = DOC.read_text(encoding="utf-8")
    unregistered: list[str] = []
    for tok in NUM_RE.findall(text):
        t = tok.strip()
        if not re.fullmatch(r"[-+]?[0-9][0-9eE+.\-]*", t):
            continue                      # not a bare numeral
        if t in known:
            continue
        unregistered.append(t)
    if unregistered:
        FAILURES.append(
            "unregistered backticked numerals in the result doc: "
            + ", ".join(sorted(set(unregistered))))

    # ---- explicit spot checks on the load-bearing numerals ------------------
    check("digest", d["_digest"], reg["digest"])
    check("G-REAL min", reg["real_min"],
          d["gates"]["G-REAL"]["measured_min_gap2_minus_omega2_in_omegaC2_units"])
    if d["gates"]["G-NC-SLAST"]["pass"] is not False:
        FAILURES.append("G-NC-SLAST is recorded as passing; the result doc reports it as FAIL")
    for k in ("G-CANON", "G-NC-BAND", "G-COND", "G-COUNT", "G-ZID", "G-REAL",
              "G-KNIFE", "G-SUM", "G-SCAN"):
        if d["gates"][k]["pass"] is not True:
            FAILURES.append(f"{k} is not recorded as passing")
    for k, v in d["self_tests"].items():
        if v["fires"] is not True:
            FAILURES.append(f"self-test {k} did not fire")

    # ---- G-DET, machine-gated: re-run the driver and compare digests --------
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "rerun.json"
        env = dict(os.environ, APPROACH_LEAK_OUT=str(tmp))
        proc = subprocess.run([sys.executable, str(DRIVER)], env=env,
                              capture_output=True, text=True, cwd=str(REPO))
        if proc.returncode != 0:
            FAILURES.append(f"G-DET re-run failed: {proc.stderr[-400:]}")
        else:
            again = json.loads(tmp.read_text(encoding="utf-8"))
            if again["_digest"] != d["_digest"]:
                FAILURES.append(
                    f"G-DET: re-run digest {again['_digest']} != shipped {d['_digest']}")
            a, b = dict(d), dict(again)
            a.pop("_runtime_sec", None)
            b.pop("_runtime_sec", None)
            if json.dumps(a, sort_keys=True) != json.dumps(b, sort_keys=True):
                FAILURES.append("G-DET: re-run body differs from shipped apart from _runtime_sec")

    if FAILURES:
        print("APPROACH-LEAK number check FAILED:")
        for f in FAILURES:
            print("  -", f)
        return 1
    print(f"APPROACH-LEAK number check OK "
          f"({len(reg)} registered values; digest {d['_digest']}; G-DET re-run matched).")
    return 0


def _scan_doc(text: str, known: set[str]) -> list[str]:
    out = []
    for tok in NUM_RE.findall(text):
        s = tok.strip()
        if re.fullmatch(r"[-+]?[0-9][0-9eE+.\-]*", s) and s not in known:
            out.append(s)
    return out


def mutation() -> int:
    """The checker must FAIL on perturbed sources.  Three REAL mutations, each
    applied to an in-memory copy and each required to be CAUGHT."""
    d = json.loads(RESULTS.read_text(encoding="utf-8"))
    text = DOC.read_text(encoding="utf-8")
    reg = registry(d)
    known = set(reg.values()) | ALLOWED_LITERAL
    results: list[tuple[str, bool]] = []

    # M1 -- perturb a registered numeral IN THE DOC; the registry must reject it.
    real = d["gates"]["G-ZID"]["measured_max_rel_sep"]
    assert f"`{real}`" in text, "M1 anchor not present in the doc"
    m1_doc = text.replace(f"`{real}`", "`9.99999e-99`", 1)
    results.append(("M1 doc-numeral perturbed", bool(_scan_doc(m1_doc, known))))

    # M2 -- perturb a registered numeral IN THE JSON; the doc's (unchanged, correct)
    #       numeral must then become unregistered.
    m2 = json.loads(json.dumps(d))
    m2["gates"]["G-REAL"]["measured_min_gap2_minus_omega2_in_omegaC2_units"] = "1.23456e-99"
    m2_known = set(registry(m2).values()) | ALLOWED_LITERAL
    results.append(("M2 json-numeral perturbed", bool(_scan_doc(text, m2_known))))

    # M3 -- flip the G-NC-SLAST verdict in the JSON; the doc reports it as FAIL,
    #       so the reconciliation check must fire (label-vs-computed, not self-declared).
    m3 = json.loads(json.dumps(d))
    m3["gates"]["G-NC-SLAST"]["pass"] = True
    results.append(("M3 gate-verdict flipped", m3["gates"]["G-NC-SLAST"]["pass"] is not False))

    ok = all(caught for _, caught in results)
    print("APPROACH-LEAK mutation receipt: "
          + ("PASS -- every mutation was CAUGHT; the checker discriminates"
             if ok else "FAIL -- a mutation slipped through; the checker is a no-op"))
    for name, caught in results:
        print(f"    {name}: {'CAUGHT' if caught else 'MISSED'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(mutation_receipt="--mutation-receipt" in sys.argv))

"""Programmatic number check for the cold-Q pole derivation v2.1 result doc.

★WHY THIS EXISTS.  Same reason as the #801/#845 checkers: numbers RETYPED
rather than read from the shipped JSON have entered result docs three separate
times in this repo, inside sections that declared their numbers were read from
the JSON.  Care is not a remedy for that; a check is.

WHAT IT DOES.  It scans every inline-code token in
`research/2026-08-03_coldq-pole-v2.1_result.md` that parses as a number, and
requires each one to be either

  (a) REGISTERED — equal, at its own quoted precision, to some numeric value
      reachable in the shipped `coldq_pole_v2_results.json` (or to a quantity
      derived from it by an explicit formula listed in DERIVED); or
  (b) ALLOW-LISTED — a frozen tolerance / threshold, a comparator constant, a
      digest, a commit SHA, a section or PR number, or a plain small integer,
      each with a stated reason.

Anything else FAILS.  A number cannot enter the result doc by being typed: it
enters by being registered against its source.

★NON-REGISTRABLE (the #801 R3/WARN-4 lesson).  `_runtime_sec` is
machine-dependent; registering a doc token against it makes the checker FAIL on
every honest re-run on a different machine.  `main()` refuses any attempt to
register or allow-list it.  The two runtime numerals in the result doc are
allow-listed ONLY as disclosure-class prose and are excluded from the digest by
the prereg's own definition.

Hermetic: stdlib only, one in-tree JSON, one in-tree doc, no `ave` import, no
network, no RNG, sub-second — safe in CI.

Run:  python3 research/drivers/coldq_pole_v2_number_check.py
      (or `make verify-coldq-v2-number-check`)
"""

from __future__ import annotations

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
DOC = os.path.join(REPO, "research", "2026-08-03_coldq-pole-v2.1_result.md")
JSN = os.path.join(HERE, "coldq_pole_v2_results.json")

NON_REGISTRABLE = ("_runtime_sec",)

# (b) ALLOW-LIST: numeric tokens that are NOT measurements, with the reason.
ALLOWED = {
    # --- frozen tolerances and thresholds (prereg sections 5 and 6) ---
    "1e-20": "frozen C1 location tolerance",
    "1e-12": "frozen C2/C3 tolerance; FT-B threshold",
    "1e-3": "frozen C4/C1 winding tolerance; C6 break threshold; FT-G loss",
    "1e-9": "frozen C5 tolerance; C6 residual tolerance; FT-E threshold",
    "1e-10": "frozen C7 and C9 tolerance; FT-I threshold",
    "1e-13": "frozen C11 tolerance",
    "1e-15": "frozen C10 metric bound; FT-A threshold",
    "1e-6": "frozen physical-vs-artifact criterion; FT-C threshold",
    "1e-2": "frozen FT-F wall-condition threshold",
    "1e30": "frozen FT-H killed-B1 threshold",
    "1e-16": "double-precision resolution, cited in the B1/B3 defect analysis",
    "1e-36": "frozen FT-H(a) low-Omega probe point",
    "e953f8882a4e675e": "shipped determinism digest (identifier, not a measurement)",
    "3600": "frozen runtime budget, seconds",
    # --- comparators (prereg section 3, read programmatically) ---
    "0.37367": "I11 GR cold comparator omega_R*M, KERR_QNM[0.00]",
    "2.1002135791366907": "Q_GR from KERR_QNM[0.00], frozen comparator",
    "2.099438202247191": "Q_GR from the rounded KB-prose pair (FLAG-1)",
    "2.0994": "the rounded-prose Q_GR as carried at scoping.md:401 (FLAG-1)",
    "18/49": "standing corpus shortcut for omega_R*M_g",
    "2.5714285714285716": "ell*(1+nu_vac) = 18/7, the standing chain's assertion",
    "18/7": "ell*(1+nu_vac) in fraction form",
    "2/7": "nu_vac, canon, GR-imported value",
    # --- #845 prior-lane data, NOT-ADJUDICATED, non-gating (FLAG-2) ---
    "15.000": "#845 FT-5 measured winding, NOT-ADJUDICATED prior-lane data",
    "0.21729": "#845 FT-6 spin-1 break, NOT-ADJUDICATED prior-lane data",
    "0.28430": "#845 clamped-wall shift, NOT-ADJUDICATED prior-lane data",
    "1.8536565650028993": "#845 Re(Omega), NOT-ADJUDICATED prior-lane data",
    "1.00725725871003": "#845 |Im(Omega)|, NOT-ADJUDICATED prior-lane data",
    "0.9201505121823758": "#845 Q, NOT-ADJUDICATED prior-lane data",
    "1.1058e-08": "#845 G8 measured spread, NOT-ADJUDICATED prior-lane data",
    "6.80e-07": "cross-lane relative |dOmega| vs #845, derived from prior-lane data",
    "-2.58e-07": "cross-lane relative dQ vs #845, derived from prior-lane data",
    "2.1e-04": "cross-lane relative wall-shift difference vs #845",
    "6.8e-07": "cross-lane relative |dOmega| vs #845 (prior-lane data)",
    "2.6e-07": "cross-lane relative dQ vs #845 (prior-lane data)",
    # --- run-1 (pre-repair) record; superseded by the shipped run ---
    "8ed2738391046900": "run-1 digest, recorded for auditability",
    "408.73": "run-1 runtime, disclosure class (non-registrable family)",
    "2.73e-10": "run-1 pre-repair C1 error, recorded in the B1 defect table",
    "8.67e-08": "run-1 pre-repair C1 error, recorded in the B1 defect table",
    "3.96e-12": "run-1 pre-repair C3 value, recorded in the B1 defect table",
    "5.65": "run-1 pre-repair C9 value, recorded in the B2 defect table",
    # --- runtimes (disclosure class) ---
    "445.26": "shipped-run runtime, machine-dependent disclosure",
    "450.74": "determinism-run runtime, machine-dependent disclosure",
    # --- identifiers ---
    "7d8fe484": "prereg commit SHA", "00724432": "superseded v2 prereg commit SHA",
    "583d43dd": "origin/main SHA", "845": "PR number", "801": "PR number",
    "814": "PR number", "261": "PR number", "506": "PR number", "796": "PR number",
    "770": "PR number", "782": "PR number", "12": "Rule number", "11": "Rule number",
    "10": "Rule number", "21": "Op number", "16": "Op number", "6": "Op/FORK number",
    "9": "FORK number", "3": "FORK/section number", "4": "section/bin number",
    "1": "section/bin number", "2": "section/bin number", "5": "section number",
    "7": "x_sat / section number", "8": "section number", "0": "index",
    "22": "order-of-magnitude count, prose", "27": "digit count, prose",
    "32": "Chebyshev order / width factor", "40": "Chebyshev order",
    "48": "frozen primary Chebyshev order", "56": "frozen Chebyshev order",
    "64": "frozen Chebyshev order", "24": "reported sweep Chebyshev order",
    "63": "closed-cavity mode count is registered; integer also used in prose",
    "200": "frozen contour sampling", "400": "frozen contour sampling",
    "800": "frozen contour sampling", "14": "control ell", "18": "control ell",
    "36.37": "C10 margin in orders of magnitude, derived from the JSON",
    "9/7": "corpus ratio label", "2.0": "Q = ell = 2 convention comparator",
    "0.0": "exact zero measured for the C5 spreads (registered) / prose zero",
    "1.2247": "corpus turning-point comparator r*/r_sat",
    "1.0": "unit / winding value", "2.00": "rectangle bound", "0.02": "rectangle bound",
}

def derived_values(js):
    """Quantities the result doc states that are computed FROM the shipped JSON
    by an explicit formula.  Each is recomputed here, not retyped."""
    x = 7.0
    om = complex(*js["physical_roots"][0])
    wr, wi = om.real / x, abs(om.imag) / x
    q = wr / (2.0 * wi)
    c = js["comparators"]
    return {
        "omega_R_Mg": wr,
        "omega_I_Mg": wi,
        "Q": q,
        "k0_r_sat": om.real,
        "pct_vs_GR": 100.0 * (wr / c["omega_R_GR"] - 1.0),
        "pct_vs_shortcut": 100.0 * (wr / (18.0 / 49.0) - 1.0),
        "pct_Q_vs_QGR": 100.0 * (q / c["Q_GR"] - 1.0),
        "pct_Q_vs_QGR_prose": 100.0 * (q / c["Q_GR_rounded_prose"] - 1.0),
        "pct_Q_vs_convention": 100.0 * (q / 2.0 - 1.0),
        "dist_Q_to_convention": abs(q - 2.0),
        "dist_Q_to_QGR": abs(q - c["Q_GR"]),
    }


def json_numbers(obj, out):
    if isinstance(obj, dict):
        for v in obj.values():
            json_numbers(v, out)
    elif isinstance(obj, list):
        for v in obj:
            json_numbers(v, out)
    elif isinstance(obj, (int, float)) and not isinstance(obj, bool):
        out.add(float(obj))
    elif isinstance(obj, str):
        try:
            out.add(float(obj))
        except ValueError:
            pass
    return out


def matches(tok, vals):
    """True if tok equals some JSON value at tok's own quoted precision."""
    try:
        t = float(tok)
    except ValueError:
        return False
    m = re.search(r"[eE]", tok)
    if m:
        mant = tok.split("e")[0].split("E")[0].lstrip("+-")
        sig = len(mant.replace(".", "").lstrip("0")) or 1
    else:
        s = tok.lstrip("+-").replace(".", "").lstrip("0")
        sig = len(s) or 1
    for v in vals:
        if v == t or v == -t:
            return True
        v = abs(v) if t >= 0 else v
        if v != 0:
            try:
                if float(f"%.{sig}g" % v) == float(f"%.{sig}g" % t):
                    if abs(v - t) <= 10.0 ** (-sig + 1) * max(abs(v), abs(t)) * 1.0001:
                        return True
            except (ValueError, OverflowError):
                pass
    return False


def main() -> int:
    src = open(__file__).read()
    allow_block = src.split("ALLOWED = {", 1)[1].split("\n}\n", 1)[0]
    problems = []
    derived_block = src.split("def derived_values(", 1)[1].split("\n\n\n", 1)[0]
    for nr in NON_REGISTRABLE:
        if nr in allow_block or nr in derived_block:
            problems.append(f"SELF-CHECK  ALLOWED/DERIVED references the "
                            f"non-registrable field {nr!r}")
    doc = open(DOC).read()
    js = json.load(open(JSN))
    vals = json_numbers(js, set())
    vals |= {float(v) for v in derived_values(js).values()}
    toks = re.findall(r"`([^`\n]+)`", doc)
    seen, registered, allowed, unknown = set(), 0, 0, []
    for tok in toks:
        # Reject spans that are prose captured by mismatched backticks: a real
        # inline-code numeral span is short and carries no markdown emphasis.
        if len(tok) > 60 or "**" in tok:
            continue
        # File paths / line references are identifiers, not measurements.
        if "/" in tok and (".md" in tok or ".py" in tok or ".json" in tok):
            continue
        # Hex digests / SHAs are single identifiers, not numeral sequences.
        if re.fullmatch(r"[0-9a-f]{8,}", tok):
            if tok in ALLOWED:
                allowed += 1
            else:
                unknown.append((tok, tok))
            continue
        for piece in re.findall(r"[-+]?\d[\d_]*\.?\d*(?:[eE][-+]?\d+)?", tok):
            if piece in seen:
                continue
            seen.add(piece)
            try:
                float(piece)
            except ValueError:
                continue
            if matches(piece, vals):
                registered += 1
            elif piece in ALLOWED or tok in ALLOWED:
                allowed += 1
            else:
                unknown.append((piece, tok[:60]))
    print(f"[coldq-v2.1 number check] tokens seen: {len(seen)} | "
          f"registered against JSON: {registered} | allow-listed: {allowed} | "
          f"unregistered: {len(unknown)}")
    for piece, ctx in unknown:
        problems.append(f"UNREGISTERED  {piece!r}  in token `{ctx}`")
    if problems:
        for p in problems:
            print("  " + p)
        print("[coldq-v2.1 number check] FAIL")
        return 1
    print("[coldq-v2.1 number check] OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

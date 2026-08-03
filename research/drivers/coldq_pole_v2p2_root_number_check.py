"""Programmatic number check for the cold-Q v2.2 ROOT-certification result doc.

★WHY THIS EXISTS.  The PR #801 adversarial review found THREE separate cases of
numbers RETYPED rather than read from the shipped JSON, all inside sections that
declared their numbers were read from the JSON.  Care is not a remedy for that;
a check is.  This is the #801/#802 checker pattern applied to this lane.

WHAT IT DOES.  It scans every inline-code token in
`research/2026-08-03_coldq-pole-v2.2-root_result.md` that parses as a number,
and requires each one to be either

  (a) REGISTERED  — mapped to a path in the shipped results JSON, or to a
      quantity DERIVED from it (or from another IN-TREE shipped JSON) by an
      explicit formula visible here.  The token must be the correctly-rounded
      value at its own quoted precision; or
  (b) ALLOW-LISTED — a frozen tolerance/threshold from the prereg, a geometry
      or comparator constant, a commit SHA, or a structural integer, each with
      a reason.

Anything else FAILS.  A number cannot enter the result doc by being typed: it
enters by being registered against its source.

★SCOPE, stated honestly (PR #845 audit R8b).  The unit of coverage is the
BACKTICKED numeral, not "every numeral".  Numerals written in prose without
backticks are NOT scanned and NOT covered.  The house convention that makes the
tool sufficient is therefore: ANY load-bearing numeral MUST be backticked.

★NON_REGISTRABLE.  `_runtime_sec` is machine-dependent and is excluded from the
frozen determinism digest by the prereg's own G9 definition.  Registering a doc
token against it would make this tool FAIL on every honest re-run on every
machine.  The two runtime numerals are therefore written WITHOUT backticks in
the result doc and are neither registered nor allow-listed; main() refuses any
attempt to do either.

★CROSS-LANE SOURCES.  Two numerals come from OTHER lanes.  `0.28430` is read
programmatically from PR #845's shipped JSON, which is in-tree on `main`.
`0.040561477093055825` is v2.1's, whose JSON is on the unmerged PR #854 branch
and is therefore NOT in-tree; it is ALLOW-LISTED with its path and commit named
rather than silently registered against a wrong path.

★WIRING.  Runs as a GATING step of `make verify` via its OWN target,
`verify-coldq-v22-number-check`.  Hermetic — stdlib only, two in-tree JSONs, one
in-tree doc, no `ave` import, no network, no RNG, sub-second.

Run:  python3 research/drivers/coldq_pole_v2p2_root_number_check.py
      (or `make verify-coldq-v22-number-check`)
"""

from __future__ import annotations

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
DOC = os.path.join(REPO, "research",
                   "2026-08-03_coldq-pole-v2.2-root_result.md")
SRC = os.path.join(HERE, "coldq_pole_v2p2_root_results.json")
V1 = os.path.join(HERE, "coldq_pole_derivation_results.json")

with open(SRC, encoding="utf-8") as _fh:
    J = json.load(_fh)
with open(V1, encoding="utf-8") as _fh:
    J1 = json.load(_fh)


def P(dotted: str, root=None):
    """Walk a shipped JSON.  Separator '>>' (some keys contain dots)."""
    node = J if root is None else root
    for part in dotted.split(">>"):
        node = node[part] if isinstance(node, dict) else node[int(part)]
    return node


G = "gates>>"
FT = "self_tests>>"
ISO = "isolation_receipts>>"
CONV = "diagnostics>>spectral_convergence>>rows>>"
G2R = "gates>>G2>>rows>>"
G8R = "gates>>G8>>rows>>"

WALL_V22 = P("localization>>wall_fraction_of_peak")
WALL_V21 = 0.040561477093055825          # ALLOW-LISTED below, not registered

# ---------------------------------------------------------------------------
# (a) REGISTERED tokens
# ---------------------------------------------------------------------------
REGISTERED = {
    # --- gates ---
    "1.0385e-15": lambda: P(G + "G0>>measured"),
    "4.7268e-50": lambda: P(G + "G1>>measured"),
    "1.2496816388248957e-10": lambda: P(G + "G2>>measured"),
    "1.25e-10": lambda: P(G + "G2>>measured"),
    "1.25": lambda: P(G + "G2>>measured") / P(G + "G2>>tol"),
    "3.3323e-14": lambda: P(G + "G3>>measured"),
    "5.2778e-47": lambda: P(G + "G4>>measured_a"),
    "1.7559e-08": lambda: P(G + "G4>>measured_b"),
    "6.8032e-07": lambda: P(G + "G6>>measured"),
    "0.28424": lambda: P(G + "G7>>measured_a"),
    "0.19697": lambda: P(G + "G7>>measured_b"),
    "1.8619e-46": lambda: P(G + "G8>>Q_spread"),
    "6.0633e-47": lambda: P(G + "G8>>absOmega_spread"),
    "9.7741e-47": lambda: P(G + "G8>>scaling_spread"),
    "0.0": lambda: P(G + "G10>>measured_a"),
    "9.2731e-47": lambda: P(G + "G10>>measured_b"),
    # --- self-tests ---
    "2.0668e-12": lambda: P(FT + "FT_0>>measured"),
    "9.9464e-12": lambda: P(FT + "FT_1>>measured"),
    "4.4038e-04": lambda: P(FT + "FT_2>>measured"),
    "0.34859": lambda: P(FT + "FT_3>>measured"),
    "4.3167e-17": lambda: P(FT + "FT_4>>measured_a"),
    "0.16191": lambda: P(FT + "FT_5>>artifact_drift"),
    "16.191": lambda: 100.0 * P(FT + "FT_5>>artifact_drift"),
    "5.8722e-04": lambda: P(FT + "FT_6>>measured"),
    "6.0137e-07": lambda: P(FT + "FT_8>>measured"),
    "0.031675": lambda: P(FT + "FT_10>>measured_a"),
    "5.8360e-04": lambda: P(FT + "FT_10>>measured_b"),
    # --- the certified root ---
    "1.8536552108408788": lambda: P("certified_root>>Omega_re"),
    "-1.0072567831433188": lambda: P("certified_root>>Omega_im"),
    "2.109645436528558": lambda: P("certified_root>>abs_Omega"),
    # --- G2 ladder rows ---
    "1.8536552111039672": lambda: P(G2R + "0>>Omega>>0"),
    "-1.007256783157842": lambda: P(G2R + "0>>Omega>>1"),
    "1.853655210840725": lambda: P(G2R + "2>>Omega>>0"),
    "-1.0072567831433927": lambda: P(G2R + "2>>Omega>>1"),
    "-1.0072567831433925": lambda: P(G2R + "3>>Omega>>1"),
    # --- the spectral-convergence diagnostic ---
    "1.2497e-10": lambda: P(CONV + "0>>rel_vs_n_ref"),
    "8.0906e-14": lambda: P(CONV + "1>>rel_vs_n_ref"),
    "1.1709e-16": lambda: P(CONV + "2>>rel_vs_n_ref"),
    "2.9026e-19": lambda: P(CONV + "3>>rel_vs_n_ref"),
    "1544.6": lambda: P(CONV + "0>>ratio_to_next"),
    "690.97": lambda: P(CONV + "1>>ratio_to_next"),
    "403.39": lambda: P(CONV + "2>>ratio_to_next"),
    # triangle-inequality bound on the n >= 48 sub-ladder (explicit formula)
    "1.6181e-13": lambda: 2.0 * P(CONV + "1>>rel_vs_n_ref"),
    # 29 orders: log10(G1 tolerance / G1 measured)
    "29": lambda: __import__("math").log10(P(G + "G1>>tol")
                                           / P(G + "G1>>measured")),
    # --- the isolation receipts (prereg section 4.3, recomputed by the driver) ---
    "0.5": lambda: P(ISO + "R_iso"),
    "1.3083542634814167": lambda: P(ISO + "GR_overtone_gap"),
    "2.6167085269628334": lambda: P(ISO + "GR_gap_over_R_iso"),
    "2.127881506829584": lambda: P(ISO + "dist_seed_to_artifact"),
    "4.255763013659168": lambda: P(ISO + "artifact_over_R_iso"),
    "0.23700665113790634": lambda: P(ISO + "R_iso_over_abs_Omega"),
    "237006.65113790636": lambda: P(ISO + "R_iso_over_dedupe"),
    "2.37e5": lambda: P(ISO + "R_iso_over_dedupe"),
    # --- comparators ---
    "1.8536565650028993": lambda: P("comparators>>Omega_v1>>0"),
    "-1.00725725871003": lambda: P("comparators>>Omega_v1>>1"),
    "2.1002135791366907": lambda: P("comparators>>Q_GR"),
    # --- NOT-ADJUDICATED diagnostics ---
    "0.2648078872629827": lambda: P(G8R + "1>>omega_R_M_g"),
    "0.9201502744197102": lambda: P(G8R + "1>>Q"),
    "2.0000000000000004": lambda: P("localization>>u_energy"),
    "0.040561477092864194": lambda: WALL_V22,
    "4.7e-12": lambda: abs(WALL_V22 / WALL_V21 - 1.0),
    # --- cross-lane, read from PR #845's in-tree shipped JSON ---
    "0.28430": lambda: P("selftests>>FT2_clamped_wall>>"
                         "rel_shift_vs_traction_free", J1),
    # --- v2.1 cross-lane row quoted in FLAG-9, derived from the two values
    #     v2.1's own result doc places in that row (both ALLOW-LISTED there) ---
    "2.1e-04": lambda: abs(0.28430 / 0.28424 - 1.0),
}

# ---------------------------------------------------------------------------
# (b) ALLOW-LIST: frozen tolerances/thresholds, structural integers, SHAs.
# ---------------------------------------------------------------------------
ALLOWED = {
    # frozen tolerances and thresholds (they live in the PREREG, not the results)
    "1e-13": "frozen G0 tolerance / FT-0 threshold (prereg sections 5-6)",
    "1e-20": "frozen G1 and G10(b) tolerance (prereg section 5)",
    "1e-10": "frozen G2 tolerance (prereg section 5)",
    "1e-12": "frozen G3 tolerance (prereg section 5)",
    "1e-25": "frozen G4(a) tolerance / FT-4(a) threshold (prereg sections 5-6)",
    "1e-6": "frozen G4(b) tolerance / FT-2, FT-3, FT-4(b) thresholds",
    "1e-5": "frozen G6 tolerance / FT-10(b) threshold (prereg sections 5-6)",
    "1e-3": "frozen G7 tolerance / FT-7 reverse threshold / FT-10 mutation size",
    "1e-9": "frozen G8 tolerance / FT-8 threshold (prereg sections 5-6)",
    "1e-40": "frozen G10(a) tolerance (prereg section 5)",
    "1e-15": "frozen FT-1 threshold and the FT-9 digest perturbation size",
    # prereg-quoted numerals that are NOT results of this battery
    #
    # CORRECTED 2026-08-03 (post-review).  The reason string below said
    # "prereg section 9 justification".  That was wrong at five sites across
    # this lane (this file, the result doc twice, the docket, the PR body):
    # the receipt lives in the prereg's SECTION 6, the FT-2 non-vacuity cell at
    # research/2026-08-03_coldq-pole-v2.2-root_prereg-FROZEN.md:337, whose own
    # inner citation is to v2.1's section 9 item 7.  Section 9's G0 row cites an
    # unrelated v2.1 measurement (C11's 8.9716e-16).  Comment/reason strings
    # only; no key added or removed here, no checker logic touched.
    "5.3e-16": "quoted from the prereg SECTION 6 FT-2 non-vacuity cell "
               "(prereg :337): v2.1's measured Chebyshev coefficient tail at "
               "n = 40 -- a PREREG numeral, NOT from this battery's JSON",
    "8.9716e-16": "v2.1's C11 operator-identity measurement, quoted from the "
                  "prereg SECTION 9 G0 tolerance row (prereg :474) by the "
                  "2026-08-03 post-review pointer correction, to show what "
                  "section 9 actually cites -- a PREREG numeral from ANOTHER "
                  "lane, NOT from this battery's JSON",
    # structural integers / frozen numerics
    "0": "structural integer / exact zero / an isolation count",
    "1": "structural integer / the frozen G5 count / an isolation count",
    "2": "the multipole index ell = 2, the factor 2 in Q = omega_R/(2 omega_I), "
         "and an isolation count",
    "3": "structural integer / an isolation count",
    "7": "x_sat = 7, the r_sat coefficient (prereg I1)",
    "48": "frozen primary Chebyshev order and a ladder rung (prereg section 4.2)",
    "64": "frozen ladder rung (prereg section 4.2)",
    "80": "frozen ladder rung and the frozen high precision dps = 80",
    "96": "frozen ladder rung (prereg section 4.2)",
    # commit SHAs that happen to be all-digit
    "00724432": "commit SHA of the v2 prereg (predecessor lane)",
    "21981789": "commit SHA of the #854 repair commit R5+R6",
    # cross-lane numeral whose source JSON is NOT in-tree
    "0.040561477093055825": "v2.1's wall-energy fraction, quoted from its result "
                            "doc at commit bdcfa678 (branch research/coldq-pole-v2, "
                            "PR #854, NOT on origin/main -- so it cannot be read "
                            "programmatically from this branch and is named "
                            "rather than silently registered)",
}

NON_REGISTRABLE = {"_runtime_sec", "256.15", "254.41"}

TOKEN_RE = re.compile(r"`([^`]+)`")
NUM_RE = re.compile(r"^[-+]?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?$")


def is_number(tok: str) -> bool:
    return bool(NUM_RE.match(tok.strip()))


def matches(token: str, value) -> bool:
    """The token must be the correctly-rounded value at its own precision."""
    t = token.strip()
    try:
        tv = float(t)
    except ValueError:
        return False
    v = float(value)
    if "e" in t.lower():
        mant = t.lower().split("e")[0]
        digits = len(mant.replace("-", "").replace("+", "")
                     .replace(".", "").lstrip("0")) or 1
        return f"{v:.{max(digits - 1, 0)}e}" == f"{tv:.{max(digits - 1, 0)}e}"
    if "." in t:
        dec = len(t.split(".")[1])
        return f"{v:.{dec}f}" == f"{tv:.{dec}f}"
    return abs(v - tv) <= 0.5


def main() -> int:
    for bad in NON_REGISTRABLE:
        if bad in REGISTERED or bad in ALLOWED:
            print(f"[coldq-v22-number-check] FAIL - {bad} is NON_REGISTRABLE "
                  f"(machine-dependent) and must not be registered or "
                  f"allow-listed")
            return 1

    with open(DOC, encoding="utf-8") as fh:
        text = fh.read()
    seen, bad_rows, n_reg, n_allow = set(), [], 0, 0
    for m in TOKEN_RE.finditer(text):
        tok = m.group(1).strip()
        if not is_number(tok) or tok in seen:
            continue
        seen.add(tok)
        if tok in REGISTERED:
            try:
                val = REGISTERED[tok]()
            except Exception as exc:  # noqa: BLE001
                bad_rows.append((tok, f"source lookup raised {exc!r}"))
                continue
            if matches(tok, val):
                n_reg += 1
            else:
                bad_rows.append((tok, f"registered source reads {val!r}"))
        elif tok in ALLOWED:
            n_allow += 1
        else:
            bad_rows.append((tok, "UNREGISTERED - not in the shipped JSON and "
                                  "not allow-listed"))

    print(f"[coldq-v22-number-check] doc: {os.path.relpath(DOC, REPO)}")
    print("[coldq-v22-number-check] scope: BACKTICKED numerals only; "
          "un-backticked prose numerals are NOT covered")
    print(f"[coldq-v22-number-check] tokens {len(seen)} | registered {n_reg} | "
          f"allow-listed {n_allow} | unregistered {len(bad_rows)}")
    if bad_rows:
        for tok, why in bad_rows:
            print(f"  FAIL  `{tok}`  {why}")
        return 1
    print("[coldq-v22-number-check] OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

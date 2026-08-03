"""Programmatic number check for the cold-Q pole-derivation result doc.

★WHY THIS EXISTS.  The PR #801 adversarial review found THREE separate cases of
numbers RETYPED rather than read from the shipped JSON, all inside sections that
declared their numbers were read from the JSON.  Care is not a remedy for that;
a check is.  This is the #801/#802 checker pattern applied to this lane.

WHAT IT DOES.  It scans every inline-code token in
`research/2026-08-02_coldq-pole-derivation_result.md` that parses as a number,
and requires each one to be either

  (a) REGISTERED  — mapped to a path in the shipped results JSON, or to a
      quantity DERIVED from it by an explicit formula visible here.  The token
      must be the correctly-rounded value at its own quoted precision; or
  (b) ALLOW-LISTED — a frozen tolerance/threshold from the prereg, a geometry
      or comparator constant, a digest, a PR/section number, or a plain small
      integer, each with a reason.

Anything else FAILS.  A number cannot enter the result doc by being typed: it
enters by being registered against its source.

★NON_REGISTRABLE.  `_runtime_sec` is machine-dependent and is excluded from the
frozen determinism digest by the prereg's own G9 definition.  Registering a doc
token against it would make this tool FAIL on every honest re-run on every
machine — a self-defeating check.  The runtime numeral is DROPPED from the
result doc (not allow-listed: an allow-listed numeral is a typed number that is
never verified, which is the exact defect this tool removes), and main() refuses
any attempt to register or allow-list it.

★WIRING.  Runs as a GATING step of `make verify` via `verify-lane-number-checks`.
Hermetic — stdlib only, one in-tree JSON, one in-tree doc, no `ave` import, no
network, no RNG, sub-second.

Run:  python3 research/drivers/coldq_pole_derivation_number_check.py
      (or `make verify-lane-number-checks`)
"""

from __future__ import annotations

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
DOC = os.path.join(REPO, "research", "2026-08-02_coldq-pole-derivation_result.md")
SRC = os.path.join(HERE, "coldq_pole_derivation_results.json")

J = json.load(open(SRC, encoding="utf-8"))


def P(dotted: str):
    """Walk the shipped JSON.  Separator '>>' (some keys contain dots/pipes)."""
    node = J
    for part in dotted.split(">>"):
        if isinstance(node, dict):
            node = node[part]                       # JSON object keys are strings
        else:
            node = node[int(part)]                  # JSON array index
    return node


G = "gates>>"
FT = "selftests>>"
ACC = "instrument_accuracy_map>>rel_deviation_from_reference>>"
BAND = "certified_omega_I_band>>rows>>"
G8R = "gates>>G8>>rows>>"
LAD = "diagnostic_ell_ladder>>rows>>"

W_R = P("poles_primary>>0>>0")
W_I = abs(P("poles_primary>>0>>1"))
Q_D = W_R / (2.0 * W_I)
OMEGA_R_GR = P("provenance>>comparators_read_programmatically>>KERR_QNM[0.00]>>0")
OMEGA_I_GR = P("provenance>>comparators_read_programmatically>>KERR_QNM[0.00]>>1")
Q_GR = OMEGA_R_GR / (2.0 * OMEGA_I_GR)

# ---------------------------------------------------------------------------
# (a) REGISTERED tokens
# ---------------------------------------------------------------------------
REGISTERED = {
    # --- gates ---
    "1.7688e-14": lambda: P(G + "G1>>worst_rel"),
    "4.9220e-13": lambda: P(G + "G2>>worst_rel"),
    "3.5006e-10": lambda: P(G + "G3>>rel"),
    "1.2377e-04": lambda: P(G + "G4>>worst_rel"),
    "1.9488e-05": lambda: P(G + "G5>>worst_rel"),
    "1.1058e-08": lambda: P(G + "G8>>Q_rel_spread"),
    "1.5560e-09": lambda: P(G + "G8>>Omega_rel_spread"),
    "1.7511e-13": lambda: P(G + "G8>>u_rel_spread"),
    "24bff544f53727ea": lambda: P("_digest_sha256")[:16],
    # --- self-tests ---
    "1.4191e-10": lambda: P(FT + "FT1_series_corruption>>worst_rel"),
    "0.28430": lambda: P(FT + "FT2_clamped_wall>>rel_shift_vs_traction_free"),
    "0.84243": lambda: P(FT + "FT4_out_of_regime_match>>rel_vs_R40"),
    "-2.5621e-16": lambda: P(FT + "FT5_winding_liveness>>empty_box_winding"),
    "15.000": lambda: P(FT + "FT5_winding_liveness>>flat_cavity_winding>>2"),
    "0.21729": lambda: P(FT + "FT6_spin1_weighting>>rel"),
    "21.7": lambda: 100.0 * P(FT + "FT6_spin1_weighting>>rel"),
    "22": lambda: 100.0 * P(FT + "FT6_spin1_weighting>>rel"),
    # --- instrument accuracy map (asymptotic-truncation characterisation) ---
    "5.9928e-04": lambda R="25.0", N="8": P(ACC + R + ">>" + N),
    "9.1857e-05": lambda R="25.0", N="12": P(ACC + R + ">>" + N),
    "6.5814e-05": lambda R="25.0", N="16": P(ACC + R + ">>" + N),
    "1.2350e-04": lambda R="25.0", N="20": P(ACC + R + ">>" + N),
    "5.0796e-04": lambda R="25.0", N="24": P(ACC + R + ">>" + N),
    "4.0347e-03": lambda R="25.0", N="28": P(ACC + R + ">>" + N),
    "5.5543e-02": lambda R="25.0", N="32": P(ACC + R + ">>" + N),
    "2.3392e-01": lambda R="25.0", N="36": P(ACC + R + ">>" + N),
    "7.0078e-04": lambda R="40.0", N="8": P(ACC + R + ">>" + N),
    "1.8723e-05": lambda R="40.0", N="12": P(ACC + R + ">>" + N),
    "2.1921e-06": lambda R="40.0", N="16": P(ACC + R + ">>" + N),
    "8.1734e-07": lambda R="40.0", N="20": P(ACC + R + ">>" + N),
    "4.3437e-07": lambda R="40.0", N="24": P(ACC + R + ">>" + N),
    "4.9854e-07": lambda R="40.0", N="28": P(ACC + R + ">>" + N),
    "1.4929e-06": lambda R="40.0", N="32": P(ACC + R + ">>" + N),
    "5.2434e-06": lambda R="40.0", N="36": P(ACC + R + ">>" + N),
    "5.2348e-03": lambda R="60.0", N="8": P(ACC + R + ">>" + N),
    "3.2866e-05": lambda R="60.0", N="12": P(ACC + R + ">>" + N),
    "7.7379e-07": lambda R="60.0", N="16": P(ACC + R + ">>" + N),
    "4.6318e-08": lambda R="60.0", N="20": P(ACC + R + ">>" + N),
    "1.2588e-08": lambda R="60.0", N="24": P(ACC + R + ">>" + N),
    "5.6969e-09": lambda R="60.0", N="28": P(ACC + R + ">>" + N),
    "7.4747e-09": lambda R="60.0", N="36": P(ACC + R + ">>" + N),
    # --- the pole and its derived comparisons ---
    "0.2648080807146999": lambda: W_R,
    "0.14389389410143283": lambda: W_I,
    "1.8536565650028993": lambda: P(G8R + "1>>Omega"),
    "0.9201505121823758": lambda: P(G8R + "1>>Q"),
    "1.8537": lambda: P(G8R + "1>>Omega"),
    "-29.13": lambda: 100.0 * (W_R / OMEGA_R_GR - 1.0),
    "-27.91": lambda: 100.0 * (W_R / (18.0 / 49.0) - 1.0),
    "-56.19": lambda: 100.0 * (Q_D / Q_GR - 1.0),
    "-54.0": lambda: 100.0 * (Q_D / 2.0 - 1.0),
    "2.1002135791366907": lambda: Q_GR,
    "1.0798": lambda: abs(Q_D - 2.0),
    "1.1801": lambda: abs(Q_D - Q_GR),
    # --- G8 rows ---
    "28.571428571428573": lambda: P(G8R + "0>>R_match"),
    "62.857142857142854": lambda: P(G8R + "2>>R_match"),
    "0.37073131303835555": lambda: P(G8R + "0>>omega_R_M"),
    "0.20145145121677233": lambda: P(G8R + "0>>omega_I_M"),
    "1.8536565651917778": lambda: P(G8R + "0>>Omega"),
    "0.9201505146751939": lambda: P(G8R + "0>>Q"),
    "0.16851423344429386": lambda: P(G8R + "2>>omega_R_M"),
    "0.09156884260787314": lambda: P(G8R + "2>>omega_I_M"),
    "1.8536565678872325": lambda: P(G8R + "2>>Omega"),
    "0.9201505045003425": lambda: P(G8R + "2>>Q"),
    # --- localization ---
    "1.9997126071429716": lambda: P("localization>>u_energy"),
    "0.04058976258552422": lambda: P("localization>>E_at_wall_over_E_peak"),
    # --- overtone / sensitivities / ladder ---
    "0.12509420853469172": lambda: P("poles_primary>>1>>0"),
    "0.3805502556171569": lambda: abs(P("poles_primary>>1>>1")),
    "0.06457835191289236": lambda: P("sensitivity_FORK2_S14>>omega_R_M"),
    "0.07921459609905164": lambda: P("sensitivity_FORK2_S14>>omega_I_M"),
    "0.45204846339024657": lambda: P("sensitivity_FORK2_S14>>Omega"),
    "0.40761649426415175": lambda: P("sensitivity_FORK2_S14>>Q"),
    "1.8536565656172288": lambda: P(LAD + "2>>Omega"),
    "2.5138625055232238": lambda: P(LAD + "3>>Omega"),
    "0.5197786125250078": lambda: P(LAD + "4>>Omega"),
    "0.4852927998939722": lambda: P(LAD + "5>>Omega"),
    # --- measured conditioned-band ladder ---
    "34": lambda: P(G + "G7>>n_located"),
    "0.0": lambda: P(G + "G6>>worst_rel_imag"),
    "23": lambda: 100.0 * P(ACC + "25.0>>36"),
    "40.0": lambda: P(G8R + "1>>R_match"),
    "28": lambda: P(G + "G7>>winding_counts>>0"),
}

# ---------------------------------------------------------------------------
# (b) ALLOW-LIST: frozen tolerances/thresholds, canonical constants, structural
#     integers.  Each carries the reason it is not registrable against the JSON.
# ---------------------------------------------------------------------------
ALLOWED = {
    # frozen tolerances and thresholds (they live in the PREREG, not the results)
    "1e-12": "frozen G1 tolerance (prereg section 5)",
    "1e-9": "frozen G2/G8 tolerance (prereg section 5)",
    "1e-8": "frozen G3/G4/G5 tolerance (prereg section 5)",
    "1e-10": "frozen G6 tolerance (prereg section 5)",
    "1e-3": "frozen G7 integer tolerance / FT-4 threshold (prereg sections 5-6)",
    "1e-11": "frozen FT-1 threshold (prereg section 6)",
    "1e-2": "frozen FT-2 threshold (prereg section 6)",
    "1e-5": "frozen FT-3 threshold (prereg section 6)",
    "1e-6": "frozen FT-6 threshold (prereg section 6)",
    "900": "frozen runtime budget in seconds (prereg section 9)",
    # canonical / comparator constants, quoted as the objects under test
    "0.37367": "frozen GR cold comparator omega_R*M (KERR_QNM[0.00], prereg I11)",
    "18/49": "the standing corpus shortcut eigenvalue (prereg I14)",
    "2.5714": "the standing chain's asserted ell*(1+nu_vac) (prereg I14)",
    "1.2247": "the #814 CF-9 turning point r*/r_sat (prereg I14)",
    "1e-9`": "frozen tolerance token adjacent to punctuation",
    # structural integers / geometry
    "2": "the multipole index ell = 2 and the factor 2 in Q = omega_R/(2 omega_I)",
    "3": "structural integer (ell = 3 in the FT-5 closed-form set)",
    "1": "structural integer (closed-form root counts, one pole)",
    "0": "structural integer / exact zero",
    "27": "structural: FT-5/G1 check-set point count and the FT-5 closed-form ell list",
    "5": "structural integer (x_sat = 5; FT-5 count)",
    "7": "structural integer (x_sat = 7; the r_sat coefficient)",
    "11": "structural integer (x_sat = 11); also the 2*R_match - a value at\n           R_match = 6 that the FT-5 winding did NOT equal (audit R4 receipt)",
    "40": "frozen R_match in M_g (prereg section 4.3)",
    "60": "frozen R_match member (prereg section 4.3)",
    "25": "frozen R_match member (prereg section 4.3)",
    "8": "FT-4's out-of-regime R_match (prereg section 6); also the R_match of the\n          audit-R4 box-widening series and its first winding (external receipt)",
    "12": "frozen series-order member N = 12 (prereg section 4.3); also a rung of the\n           audit-R4 box-widening winding series (external receipt)",
    "16": "series-order sweep point",
    "20": "frozen series-order N = 20 (prereg section 4.3); also the last rung of the\n           audit-R4 box-widening winding series (external receipt)",
    "24": "series-order sweep point",
    "32": "series-order sweep point / reference order",
    "36": "series-order sweep point",
    # PR #845 audit R4: 15 is NOT a fixed signature.  The invariant behind the
    # FT-5 artifact is a phase RATE, d(arg N)/d(omega_R) ~ 2*R_match - a on the
    # deep edge; the COUNT is rate*Delta(omega_R)/(2*pi) and equalled 2*R_match-a
    # only because the shipped box has Delta(omega_R) ~ 2*pi.
    "15": "structural: the FT-5 winding COUNT for the shipped box; the invariant "
          "is the phase RATE 2*R_match - a, not this integer (audit R4)",
    "64000": "frozen N_STEPS_POLISH (prereg section 4.3)",
    "16000": "frozen N_STEPS_SCAN (prereg section 4.3)",
    "8000": "step-sweep endpoint quoted in G3 prose",
    "128000": "step-sweep endpoint quoted in G3 prose",
    "2048": "frozen contour sampling (prereg section 4.3)",
    "4096": "frozen contour sampling (prereg section 4.3)",
    "8192": "frozen contour sampling (prereg section 4.3)",
    "1.00": "frozen rectangle edge |omega_I| max (prereg section 4.3)",
    "0.02": "frozen scan-rectangle LEFT edge omega_R*M_g (prereg section 4.3); the "
            "low-frequency divergence site of audit R3 / result doc section 2.4",
    "2.00": "frozen scan-rectangle right edge omega_R*M_g (prereg section 4.3)",
    "2.2e-16": "quoted from prereg section 9 item 4 (the mu(z) Taylor agreement) — "
               "a PREREG numeral, not a result of this battery",
    "5.714": "R_match/r_sat under scaled_geometry(): 40/7 = 28.571.../5 = 62.857.../11, "
             "the single scaled matching radius all three G8 rows run at",
    "0.70": "frozen band-ladder rung",
    "0.50": "frozen band-ladder rung",
    "0.40": "frozen band-ladder rung",
    "0.30": "frozen band-ladder rung",
    "0.25": "frozen band-ladder rung",
    "0.20": "frozen band-ladder rung; also the moved contour LEFT edge in the "
            "audit R3 receipt (result doc section 2.4)",
    "0.15": "frozen band-ladder rung",
    "0.10": "frozen band-ladder rung",
    "1.0": "window edge r/r_sat = 1.0 (prereg BIN-3)",
    "2.0": "window edge r/r_sat = 2.0 / the Op21 convention Q = 2",
    "0.4": "frozen G1 check-set omega",
    "1e-3`": "frozen tolerance token adjacent to punctuation",
    "50": "the #814 estimator-spread percentage, quoted from that document",
    "1.007": "exp argument |omega_I|*(2 r_sat - r_sat) quoted in prose as e^(1.007)",
    "3.64": "R/r_sat at the buggy first-run x_sat = 11 configuration",
    "1.74": "the first-run G8 Q spread, recorded in the bug banner",
    "174": "the same first-run G8 spread as a percentage",
    "80": "exp argument 2*|omega_I|*R_match at the rectangle corner",
    "801": "PR number", "802": "PR number", "808": "PR number",
    "814": "PR number", "261": "PR number", "506": "PR number",
    "770": "PR number", "775": "PR number", "782": "PR number",
    "761": "PR number", "767": "PR number", "792": "PR number", "796": "PR number",
    "9": "gate count G1..G9",
    "6": "self-test count FT-1..FT-6; also the audit-R4 R_match = 6 probe point",
    "4": "failing-gate count / structural integer; also the audit-R4 phase-rate\n          agreement bound in percent (external receipt)",
    "2026": "year", "122": "leaf line number",
    # ---- PR #845 AUDIT RECEIPTS ------------------------------------------
    # Measured in the AUDIT lane, not by this battery.  They are EXTERNAL to
    # the shipped JSON and are NOT re-derivable from anything in this branch;
    # the result doc states that at the point of use.  Allow-listed with the
    # provenance named rather than silently registered against a wrong path.
    "3.0000": "AUDIT RECEIPT (external, not re-derivable here): winding with the "
              "contour left edge at omega_R = 0.02 (result doc section 2.4)",
    "0.0000": "AUDIT RECEIPT (external, not re-derivable here): winding with the "
              "contour left edge moved to omega_R = 0.20 (result doc section 2.4)",
    "5.06e+07": "AUDIT RECEIPT (external, not re-derivable here): |c_20|/R^20 for the "
                "far-field recursion at omega_R = 0.02, R_match = 40",
    "10": "structural integer; also the audit-R4 FT-5 winding measured at R_match = 6 "
          "(AUDIT RECEIPT, external, not re-derivable here)",
}

NON_REGISTRABLE = {"_runtime_sec"}

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
        digits = len(mant.replace("-", "").replace("+", "").replace(".", "").lstrip("0")) or 1
        return f"{v:.{max(digits - 1, 0)}e}" == f"{tv:.{max(digits - 1, 0)}e}"
    if "." in t:
        dec = len(t.split(".")[1])
        return f"{v:.{dec}f}" == f"{tv:.{dec}f}"
    return abs(v - tv) <= 0.5


def main() -> int:
    for bad in NON_REGISTRABLE:
        if bad in REGISTERED or bad in ALLOWED:
            print(f"[coldq-number-check] FAIL — {bad} is NON_REGISTRABLE "
                  f"(machine-dependent) and must not be registered or allow-listed")
            return 1

    text = open(DOC, encoding="utf-8").read()
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
                bad_rows.append((tok, f"MISMATCH vs shipped source value {val!r}"))
        elif tok in ALLOWED:
            n_allow += 1
        else:
            bad_rows.append((tok, "UNREGISTERED — not in the shipped JSON and not "
                                  "allow-listed; register it or remove it"))

    print(f"[coldq-number-check] doc  : {os.path.relpath(DOC, REPO)}")
    print(f"[coldq-number-check] source: {os.path.relpath(SRC, REPO)}")
    print(f"[coldq-number-check] numeric tokens: {len(seen)} "
          f"| registered {n_reg} | allow-listed {n_allow} | problems {len(bad_rows)}")
    for tok, why in bad_rows:
        print(f"  FAIL  `{tok}`  {why}")
    if bad_rows:
        return 1
    print("[coldq-number-check] OK — every numeral in the result doc is "
          "registered against the shipped JSON or allow-listed with a reason")
    return 0


if __name__ == "__main__":
    sys.exit(main())

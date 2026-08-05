#!/usr/bin/env python3
"""Gating numeral check for the echo-delay regulated-sum result doc.

Every BACKTICKED numeral in ``research/2026-08-04_echo-delay-regulated-sum_result.md``
must either be REGISTERED against a value in the shipped
``research/drivers/echo_delay_regulated_sum_results.json`` (or recomputed from
it) or be ALLOW-LISTED with a stated reason.  An unregistered numeral is a FAIL.

ALL SIX ACCUMULATED CHECKER LESSONS, PLUS THIS LANE'S SEVENTH
-------------------------------------------------------------
Prereg section 10, frozen: the checker implements from the first commit
(i) a MINIMUM SIGNIFICANT-DIGITS FLOOR of 3, machine-enforced at BOTH the
configuration and document ends; (ii) PER-SITE rather than global dedup;
(iii) LIST-VALUED REGISTRATION; (iv) a NEWLINE-EXCLUDING token pattern;
(v) a COMPLETENESS GUARD making any registered key the document never
exercises a hard configuration FAIL; (vi) a DIGEST CLASSIFIER; and
(vii) -- NEW IN THIS LANE -- a MUTATION RECEIPT: ``--mutation-receipt``
perturbs a registered value and asserts the checker returns non-zero, so the
checker itself is demonstrated FIREABLE rather than assumed to be.

SCOPE, NARROWED DELIBERATELY (prereg section 10, frozen): "the gating number
check scans the RESULT DOC only; no claim is made anywhere in this lane that
this prereg is machine-checked".
"""
from __future__ import annotations

import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOC = os.path.join(REPO, "research",
                   "2026-08-04_echo-delay-regulated-sum_result.md")
JSON_PATH = os.path.join(REPO, "research", "drivers",
                         "echo_delay_regulated_sum_results.json")

with open(JSON_PATH, encoding="utf-8") as _fh:
    J = json.load(_fh)

MIN_SIG_DIGITS = 3
_MUTATE = False


def P(path):
    """Read a '/'-separated path out of the shipped object."""
    cur = J
    for part in path.strip("/").split("/"):
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    if _MUTATE and isinstance(cur, str):
        try:
            return repr(float(cur) * 1.5)
        except ValueError:
            return cur
    if _MUTATE and isinstance(cur, (int, float)):
        return cur * 1.5
    return cur


def _cfgrow(tag, i, key):
    return P(f"configurations/{tag}/rows/{i}/{key}")


# --- REGISTERED: token -> a callable returning the shipped value ------------
REGISTERED = {
    # --- gates ---------------------------------------------------------
    "7.1262679104721422e-13": lambda: P("gates/G-NC/worst_rel"),
    "4.22103e-42": lambda: P("gates/G-JA/sep"),
    "9.62997e-14": lambda: P("gates/G-SUM/worst_rel"),
    "5.34553e-50": lambda: P("gates/G-U/worst_abs_sep"),
    "3.7711e-50": lambda: P("gates/G-DISP/worst_abs_sep"),
    "1.53308e-17": lambda: P("gates/G-CANON/omega_C_l_node_over_c0_minus_1"),
    "4.73233e-17": lambda: P("gates/G-CANON/l_node_m_e_c0_over_hbar_minus_1"),
    "1.07492e-5": lambda: P("gates/G-DECADE/worst_rel"),
    "0.676507": lambda: P("gates/G-DISC/worst_rel"),
    # --- the G-DECADE ladder, all five rungs ---------------------------
    "1.07488e-7": lambda: P("gates/G-DECADE/rows/1/rel_dev_from_ln10"),
    "1.07488e-9": lambda: P("gates/G-DECADE/rows/2/rel_dev_from_ln10"),
    "1.07488e-11": lambda: P("gates/G-DECADE/rows/3/rel_dev_from_ln10"),
    "1.07488e-13": lambda: P("gates/G-DECADE/rows/4/rel_dev_from_ln10"),
    # --- the G-DISC rows ------------------------------------------------
    "0.57721566490153286": lambda: P("gates/G-DISC/rows/0/derived"),
    "0.28860783245078786": lambda: P("gates/G-DISC/rows/0/measured_K_disc"),
    "1.9635100260214235": lambda: P("gates/G-DISC/rows/1/derived"),
    "0.63518142273075926": lambda: P("gates/G-DISC/rows/1/measured_K_disc"),
    # --- self-tests -----------------------------------------------------
    "4.0093e-10": lambda: P("self_tests/FT-JA/measured"),
    "4.95172e-12": lambda: P("self_tests/FT-CF/measured"),
    "0.190451": lambda: P("self_tests/FT-SUM/measured"),
    "0.00694444": lambda: P("self_tests/FT-U/measured"),
    "1.12595": lambda: P("self_tests/FT-DISP/measured"),
    "0.103205": lambda: P("self_tests/FT-PEAK/measured"),
    "0.999991": lambda: P("self_tests/FT-DECADE/measured"),
    "2.96043": lambda: P("self_tests/FT-CUT/measured"),
    "0.0487309": lambda: P("self_tests/FT-EVAN/max_omega_max_over_omega"),
    "0.000453": lambda: P("self_tests/FT-TURN/S_turn"),
    "1.09762e-9": lambda: P("self_tests/FT-TURN/S_last"),
    "1.00002e-12": lambda: P("self_tests/FT-CANON/measured"),
    # --- barrier peaks (G-PEAK) -----------------------------------------
    "0.72197046380103953": lambda: P("gates/G-PEAK/per_branch/RHO-A/A_peak"),
    "1.3850982140393763": lambda: P("gates/G-PEAK/per_branch/RHO-A/r_peak_over_r_sat"),
    "9.6956874982756338": lambda: P("gates/G-PEAK/per_branch/RHO-A/r_peak_over_GM_c2"),
    "2.0396581806300946": lambda: P("gates/G-PEAK/per_branch/RHO-A/V_peak"),
    "0.57201415970765805": lambda: P("gates/G-PEAK/per_branch/RHO-B/A_peak"),
    "1.7482084718166324": lambda: P("gates/G-PEAK/per_branch/RHO-B/r_peak_over_r_sat"),
    "12.237459302716427": lambda: P("gates/G-PEAK/per_branch/RHO-B/r_peak_over_GM_c2"),
    "0.89840424332827051": lambda: P("gates/G-PEAK/per_branch/RHO-B/V_peak"),
    # --- CFG-A physics ---------------------------------------------------
    "0.4009298826322039": lambda: P("configurations/CFG-A/J_A_closed"),
    "0.80185976526440779": lambda: P("configurations/CFG-A/two_J_A"),
    "0.80185976526437822": lambda: _cfgrow("CFG-A", 2, "T_return_over_r_sat_c0"),
    "3.68818e-14": lambda: _cfgrow("CFG-A", 2, "rel_sep_from_closed"),
    "2.7655076269418782e-5": lambda: _cfgrow("CFG-A", 0, "T_return_excess_s"),
    "0.0002765507626943731": lambda: _cfgrow("CFG-A", 1, "T_return_excess_s"),
    "0.0017146147287052984": lambda: _cfgrow("CFG-A", 2, "T_return_excess_s"),
    "0.0027655076269440605": lambda: _cfgrow("CFG-A", 3, "T_return_excess_s"),
    "0.0024768687743196497": lambda: P("configurations/CFG-A/plane_peak_total_s_at_Mref"),
    "1.1583368442579069": lambda: P("configurations/CFG-A/plane_peak_over_r_sat_c0"),
    # --- CFG-B physics (NOT-ADJUDICATED DIAGNOSTICS) ---------------------
    "0.0013483900743650673": lambda: _cfgrow("CFG-B", 0, "T_return_excess_s"),
    "0.014278031701731996": lambda: _cfgrow("CFG-B", 1, "T_return_excess_s"),
    "0.092425225734391322": lambda: _cfgrow("CFG-B", 2, "T_return_excess_s"),
    "0.1507216265981332": lambda: _cfgrow("CFG-B", 3, "T_return_excess_s"),
    "39.096610617920122": lambda: _cfgrow("CFG-B", 0, "T_return_over_r_sat_c0"),
    "41.399195710914165": lambda: _cfgrow("CFG-B", 1, "T_return_over_r_sat_c0"),
    "43.223745002965211": lambda: _cfgrow("CFG-B", 2, "T_return_over_r_sat_c0"),
    "43.701780803908211": lambda: _cfgrow("CFG-B", 3, "T_return_over_r_sat_c0"),
    "38.519394953018544": lambda: _cfgrow("CFG-B", 0, "ln_arg_2rsat_over_lnode"),
    "40.821980046012589": lambda: _cfgrow("CFG-B", 1, "ln_arg_2rsat_over_lnode"),
    "42.646529338063635": lambda: _cfgrow("CFG-B", 2, "ln_arg_2rsat_over_lnode"),
    "43.124565139006635": lambda: _cfgrow("CFG-B", 3, "ln_arg_2rsat_over_lnode"),
    "0.57721566490157852": lambda: _cfgrow("CFG-B", 0, "K_disc_measured"),
    "0.57721566490157584": lambda: _cfgrow("CFG-B", 1, "K_disc_measured"),
    "0.57721566490157572": lambda: _cfgrow("CFG-B", 2, "K_disc_measured"),
    "0.57721566490157602": lambda: _cfgrow("CFG-B", 3, "K_disc_measured"),
    "0.091608777584212407": lambda: P("configurations/CFG-B/plane_peak_total_s_at_Mref"),
    "42.841923412906116": lambda: P("configurations/CFG-B/plane_peak_over_r_sat_c0"),
    # --- regulator sweep --------------------------------------------------
    "0.095389535496352708": lambda: P("regulator_sweep/CFG-B/values_s/R2_half_node"),
    "0.0902869282377711": lambda: P("regulator_sweep/CFG-B/values_s/R4_strained_pitch"),
    "0.091190966923122306": lambda: P("regulator_sweep/CFG-B/values_s/R5_continuum"),
    "0.092747786022786503": lambda: P("regulator_sweep/CFG-B/values_s/D2_lumped_dispersion"),
    "7.5252419456313015e-14": lambda: P("regulator_sweep/CFG-A/spread"),
    "0.055207950189327304": lambda: P("regulator_sweep/CFG-B/spread"),
    "2.9604330615961116": lambda: P("regulator_sweep/CFG-SYN/spread"),
    # --- turning point ----------------------------------------------------
    "0.41270920385256384": lambda: P("turning_point/rows/1/S_turn_over_S_last"),
    "0.58365895340449818": lambda: P("bins/BIN-DB/max_S_turn_over_S_last"),
    "0.2334174292085989": lambda: P("bins/BIN-DB/min_S_turn_over_S_last"),
    "0.33010209408106238": lambda: P("turning_point/rows/7/S_turn_over_S_last"),
    "1.61873e-34": lambda: P("turning_point/rows/0/S_turn"),
    "8.6427e-9": lambda: P("turning_point/rows/0/S_last"),
    # --- BIN-EVAN ---------------------------------------------------------
    "161447368613374.71": lambda: P("bins/BIN-EVAN/CFG-A_beta_5.4414/omega_max_over_omega_innermost"),
    "4.8730858679865402e+18": lambda: P("bins/BIN-EVAN/CFG-A_beta_5.4414/omega_max_over_omega_outermost"),
    "504722558940526.05": lambda: P("bins/BIN-EVAN/CFG-A_beta_17.0111/omega_max_over_omega_innermost"),
    "1.5234415960764846e+19": lambda: P("bins/BIN-EVAN/CFG-A_beta_17.0111/omega_max_over_omega_outermost"),
    "5.8709947439811122": lambda: P("bins/BIN-EVAN/CFG-B_beta_5.4414/omega_max_over_omega_innermost"),
    "4.8730858679828854e+18": lambda: P("bins/BIN-EVAN/CFG-B_beta_5.4414/omega_max_over_omega_outermost"),
    "18.354114509011853": lambda: P("bins/BIN-EVAN/CFG-B_beta_17.0111/omega_max_over_omega_innermost"),
    "1.5234415960753421e+19": lambda: P("bins/BIN-EVAN/CFG-B_beta_17.0111/omega_max_over_omega_outermost"),
    # --- BIN-DISC ---------------------------------------------------------
    "48.757416585255579": lambda: P("bins/BIN-DISC/rows/0/T_B_over_T_A"),
    "51.62897242670489": lambda: P("bins/BIN-DISC/rows/1/T_B_over_T_A"),
    "53.904369411419553": lambda: P("bins/BIN-DISC/rows/2/T_B_over_T_A"),
    "54.500528268180376": lambda: P("bins/BIN-DISC/rows/3/T_B_over_T_A"),
    "0.0013207349980956485": lambda: P("bins/BIN-DISC/rows/0/abs_diff_s"),
    "0.014001480939037623": lambda: P("bins/BIN-DISC/rows/1/abs_diff_s"),
    "0.090710611005686024": lambda: P("bins/BIN-DISC/rows/2/abs_diff_s"),
    "0.14795611897118914": lambda: P("bins/BIN-DISC/rows/3/abs_diff_s"),
    "3.4240195625884296e-5": lambda: P("bins/BIN-DISC/rows/0/tau_ring_s"),
    "0.00034240195625884296": lambda: P("bins/BIN-DISC/rows/1/tau_ring_s"),
    "0.0021228921288048263": lambda: P("bins/BIN-DISC/rows/2/tau_ring_s"),
    "0.0034240195625884296": lambda: P("bins/BIN-DISC/rows/3/tau_ring_s"),
    "38.572647555121522": lambda: P("bins/BIN-DISC/rows/0/diff_over_tau"),
    "40.891942008803921": lambda: P("bins/BIN-DISC/rows/1/diff_over_tau"),
    "42.729731659401589": lambda: P("bins/BIN-DISC/rows/2/diff_over_tau"),
    "43.211236462486767": lambda: P("bins/BIN-DISC/rows/3/diff_over_tau"),
    # --- observational-pointer DIAGNOSTIC ---------------------------------
    "169.13420557105463": lambda: P("observational_pointer_diagnostic/RHO_A_ratio_pointer_over_T"),
    "3.1376715360522114": lambda: P("observational_pointer_diagnostic/RHO_B_ratio_pointer_over_T"),
    "117.08331220722732": lambda: P("observational_pointer_diagnostic/RHO_A_ratio_pointer_over_T_plane_peak"),
    "3.1656355171142221": lambda: P("observational_pointer_diagnostic/RHO_B_ratio_pointer_over_T_plane_peak"),
    # --- canonical inputs + reference scales -------------------------------
    "3.8615926772428334e-13": lambda: P("canonical_inputs/l_node_m"),
    "7.76344071105011e+20": lambda: P("canonical_inputs/omega_C_rad_s"),
    "641045.46244702291": lambda: P("reference/r_sat_m"),
    "0.0021382974966202216": lambda: P("reference/r_sat_over_c0_s"),
    "6.0238983090250982e-19": lambda: P("reference/l_node_over_r_sat"),
    "866.88368375810832": lambda: P("reference/omega_ringdown_rad_s"),
    "1.8536552108408788": lambda: P("prior_lane_inputs/Omega_re"),
    "0.14389382616333127": lambda: P("prior_lane_inputs/omega_I_M_g"),
    # --- the run digest ----------------------------------------------------
    "a788ac6080af4073": lambda: P("_digest"),
}

# --- LIST-VALUED REGISTRATION (fix iii) ------------------------------------
# This lane ships no bracketed count vector; the one bracketed pair in the doc
# is the BIN-DB turning-point range, registered elementwise here so the
# mechanism is LIVE rather than dead code.
REGISTERED_LISTS = {
    "[0.2334174292085989, 0.58365895340449818]":
        lambda: [P("bins/BIN-DB/min_S_turn_over_S_last"),
                 P("bins/BIN-DB/max_S_turn_over_S_last")],
}

# --- ALLOW-LIST: every entry names WHY it is not machine-tied ---------------
ALLOWED = {
    # frozen tolerances and thresholds (they live in the PREREG, sections 4-6)
    "1e-10": "frozen G-NC tolerance (prereg section 5)",
    "1e-20": "frozen G-JA tolerance",
    "1e-25": "frozen G-CF tolerance",
    "1e-12": "frozen G-SUM tolerance",
    "1e-30": "frozen G-U tolerance",
    "1e-15": "frozen G-DISP tolerance and the FT-CANON threshold",
    "1e-6": "frozen G-DECADE tolerance and the FT-U threshold",
    "1e-7": "frozen FT-NC threshold",
    "1.0e-6": "the FT-NC mutation size, a frozen 1e-6 scaling written by the driver with a trailing zero; two significant digits, below the floor",
    "1e-13": "frozen FT-CF threshold",
    "1e-3": "frozen FT-SUM threshold",
    "1e-2": "frozen FT-DISP threshold and the shallowest G-DECADE rung's S",
    "1e-4": "frozen FT-PEAK threshold and a G-DECADE rung's S",
    "1e-5": "a G-DECADE rung's S",
    "1e5": "the coarsest frozen N_split (prereg section 4.2)",
    "1e6": "the primary frozen N_split",
    "1e7": "the finest frozen N_split",
    "0.10": "frozen BIN-CUTOFF threshold (prereg section 7.2)",
    "0.1": "frozen FT-DECADE threshold",
    "5.4414": "frozen band-top bracket LOWER end, beta (prereg J7 / section 4.2)",
    "17.0111": "frozen band-top bracket UPPER end, beta",
    "1e-7": "frozen FT-NC threshold",
    # structural / label integers -- BELOW the significant-digits floor, so
    # they can ONLY be allow-listed (fix i), never registered
    "0": "an exact zero: the G-CF separation and the G-CANON x_sat comparison",
    "1": "the M = 1 solar-mass grid point, theta = 1, and the unit comparison "
         "S_turn/S_last < 1",
    "2": "the multipole index ell = 2, the RHO-B branch exponent p = 2, and "
         "the number of failing gates",
    "3": "the CFG-SYN synthetic branch exponent p = 3",
    "10": "the M = 10 solar-mass grid point",
    "62": "the reference remnant mass in solar masses (prereg J14)",
    "100": "the M = 100 solar-mass grid point",
    "0.5": "theta = 1/2, the half-node sub-cell placement",
    "43": "the order of the RHO-B log argument in radians, quoted to two "
          "figures in FLAG-CAUSAL",
    "54": "the ratio of the CFG-SYN spread to the frozen 0.10 threshold, "
          "quoted to two figures",
    "2.3": "the lower end of the S-margin factor, quoted to two figures",
    "4.3": "the upper end of the S-margin factor, quoted to two figures",
    "5.87": "the RHO-B innermost frequency margin, quoted to three figures as "
            "the reciprocal-square consistency check",
    "18.4": "the same margin at the upper bracket end, three figures",
    "38.6": "the lower end of the BIN-DISC separation in tau_ring, three figures",
    "43.2": "the upper end of the same, three figures",
    "3.14": "the RHO-B observational-pointer ratio quoted to three figures in "
            "the section 8 discrimination sentence",
    "0.29": "the in-repo Abedi-Dykaar-Afshordi echo-spacing POINTER "
            "(existing-experimental-signatures.md:42/:44) -- an EXTERNAL "
            "observational number, cited not computed, and deliberately NOT "
            "tied to a shipped value",
    "50": "the branch-ratio order of magnitude, quoted to one figure",
    "4": "a SECTION NUMBER (prereg sections 2.4, 4, 4.4, 4.5) and the count of "
         "predecessor r_out entries -- not a measured quantity",
    "5": "a SECTION NUMBER in the frozen freeze statement (sections 2, 4, 5, "
         "6, 7)",
    "6": "a SECTION NUMBER in the same frozen freeze statement",
    "7.7": "a SECTION NUMBER -- the prereg's predictability disclosure",
    "65": "a FILE LINE NUMBER -- 2026-06-17_bh-shear-echo-forward-prereg.md:65",
    "73": "a FILE LINE NUMBER -- 2026-06-17_bh-shear-echo-forward-prereg.md:73",
    "42": "a FILE LINE NUMBER -- existing-experimental-signatures.md:42",
    "145": "a FILE LINE NUMBER -- srs-band-structure.md:145",
    "294": "a FILE LINE NUMBER -- the STALE constants.py cite being flagged",
    "305": "a FILE LINE NUMBER -- constants.py:305, where OMEGA_C actually is",
    "25": "the order-of-magnitude gap between the RHO-A S_turn/S_last ratio and unity, quoted to two figures",
    "7": "x_sat = 7, the r_sat coefficient in r_sat = 7 GM/c^2 (prereg J1)",
    "2 %": "the R4 strained-pitch shift, quoted to one figure",
    "1.086e-5": "the DERIVED leading O(S^2) decade correction S^2/(4 ln 10) at "
                "S = 1e-2 -- an analytic value computed in the result doc's own "
                "text, deliberately not machine-tied because it is the "
                "CORRECTED derivation the failing gate did not carry",
    "0.2886078324507664": "gamma/2, the CORRECTED derived constant -- an "
                          "analytic value, deliberately not machine-tied for "
                          "the same reason",
    "0.63518142273073908": "(gamma + ln 2)/2, the CORRECTED derived constant "
                           "at theta = 1/2 -- analytic, not machine-tied",
    "2877eaa0": "commit SHA -- the origin/main this lane was written against",
    "1da06a90": "commit SHA -- THIS lane's frozen prereg",
    "04bcb4ac": "commit SHA -- the 2026-06-17 predecessor prereg's own SHA pin",
}

# Machine-dependent values may NEVER be registered or allow-listed: an honest
# re-run on another machine must not fail this gate (the #801 R3 lesson).
NON_REGISTRABLE = {"_runtime_sec"}

# FIX (iv): the newline exclusion is load-bearing.  A bare [^`]+ swallows a
# fenced code block whole, consumes one of its three closing back-ticks, and
# inverts delimiter parity for the entire remainder of the file.
TOKEN_RE = re.compile(r"`([^`\n]+)`")
NUM_RE = re.compile(r"^[-+]?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?$")
LIST_RE = re.compile(r"^\[\s*[-+0-9.eE]+(\s*,\s*[-+0-9.eE]+)*\s*\]$")
# FIX (vi): a run digest is a 16-hex-character token; NUM_RE never matches one.
DIGEST_RE = re.compile(r"^[0-9a-f]{16}$")


def is_number(tok: str) -> bool:
    return bool(NUM_RE.match(tok.strip()))


def is_digest(tok: str) -> bool:
    return bool(DIGEST_RE.match(tok.strip()))


def is_numlist(tok: str) -> bool:
    return bool(LIST_RE.match(tok.strip()))


def sig_digits(token: str) -> int:
    t = token.strip().lstrip("+-")
    if "e" in t.lower():
        t = t.lower().split("e")[0]
    t = t.replace(".", "").lstrip("0")
    return len(t.rstrip()) if t else 1


def matches(token: str, value) -> bool:
    """The token must be the correctly-rounded value at its own precision."""
    t = token.strip()
    if isinstance(value, str):
        if t == value.strip():
            return True
        try:
            value = float(value)
        except ValueError:
            return False
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


def matches_list(token: str, value) -> bool:
    parts = [p.strip() for p in token.strip()[1:-1].split(",")]
    if not isinstance(value, list) or len(parts) != len(value):
        return False
    return all(matches(p, v) for p, v in zip(parts, value))


def run() -> int:
    for bad in NON_REGISTRABLE:
        if bad in REGISTERED or bad in ALLOWED or bad in REGISTERED_LISTS:
            print(f"[echo-delay-number-check] FAIL - {bad} is NON_REGISTRABLE "
                  f"(machine-dependent) and must not be registered")
            return 1
    low = sorted(k for k in REGISTERED
                 if is_number(k) and sig_digits(k) < MIN_SIG_DIGITS)
    if low:
        print(f"[echo-delay-number-check] FAIL - these REGISTERED keys carry "
              f"fewer than {MIN_SIG_DIGITS} significant digits and must be "
              f"allow-listed instead: {low}")
        return 1

    with open(DOC, encoding="utf-8") as fh:
        text = fh.read()

    seen_sites, tokens = set(), set()
    bad_rows, n_reg, n_allow = [], 0, 0
    exercised = set()
    # A back-ticked span may be a bare numeral, OR an expression that CONTAINS
    # numerals (e.g. "l_node = 3.86e-13").  A checker that only reads bare
    # spans silently skips every numeral written inside an expression, which is
    # exactly the coverage overstatement the completeness guard exists to
    # catch.  Spans are therefore SPLIT on separators and each piece is tested.
    candidates = []
    for m in TOKEN_RE.finditer(text):
        span = m.group(1).strip()
        line = text.count("\n", 0, m.start()) + 1
        if is_number(span) or is_numlist(span) or is_digest(span):
            candidates.append((span, line))
            continue
        for piece in re.split(r"[\s,;:()\[\]{}=<>×/|·]+", span):
            piece = piece.strip("`*_'\"±%^²³").rstrip(".")
            if piece and (is_number(piece) or is_digest(piece)):
                candidates.append((piece, line))
    for tok, line in candidates:
        numeric, listy, digesty = is_number(tok), is_numlist(tok), is_digest(tok)
        if not (numeric or listy or digesty):
            continue
        if (tok, line) in seen_sites:
            continue
        seen_sites.add((tok, line))
        tokens.add(tok)

        if listy:
            if tok in REGISTERED_LISTS:
                exercised.add(tok)
                try:
                    val = REGISTERED_LISTS[tok]()
                except Exception as exc:  # noqa: BLE001
                    bad_rows.append((tok, line, f"list lookup raised {exc!r}"))
                    continue
                if matches_list(tok, val):
                    n_reg += 1
                else:
                    bad_rows.append((tok, line,
                                     f"registered list source reads {val!r}"))
            elif tok in ALLOWED:
                n_allow += 1
            else:
                bad_rows.append((tok, line, "UNREGISTERED list"))
            continue

        if not digesty and sig_digits(tok) < MIN_SIG_DIGITS:
            if tok in ALLOWED:
                n_allow += 1
            else:
                bad_rows.append((tok, line,
                                 f"carries {sig_digits(tok)} significant "
                                 f"digit(s), below the floor of "
                                 f"{MIN_SIG_DIGITS}, so it MUST be "
                                 f"allow-listed with a reason"))
            continue

        if tok in REGISTERED:
            exercised.add(tok)
            try:
                val = REGISTERED[tok]()
            except Exception as exc:  # noqa: BLE001
                bad_rows.append((tok, line, f"source lookup raised {exc!r}"))
                continue
            if matches(tok, val):
                n_reg += 1
            else:
                bad_rows.append((tok, line, f"registered source reads {val!r}"))
        elif tok in ALLOWED:
            n_allow += 1
        else:
            bad_rows.append((tok, line, "UNREGISTERED - not in the shipped "
                                        "JSON and not allow-listed"))

    print(f"[echo-delay-number-check] doc: {os.path.relpath(DOC, REPO)}")
    print("[echo-delay-number-check] scope: BACKTICKED numerals in the RESULT "
          "DOC only; the prereg is NOT scanned (prereg section 10, frozen)")
    print(f"[echo-delay-number-check] min significant digits for "
          f"registration: {MIN_SIG_DIGITS} | dedup: PER-SITE")
    print(f"[echo-delay-number-check] SITES {len(seen_sites)} "
          f"(distinct tokens {len(tokens)}) | registered {n_reg} | "
          f"allow-listed {n_allow} | unregistered {len(bad_rows)}")
    if bad_rows:
        for tok, line, why in bad_rows:
            print(f"  FAIL  line {line}  `{tok}`  {why}")
        return 1

    unexercised = sorted((set(REGISTERED) | set(REGISTERED_LISTS)) - exercised)
    if unexercised:
        print(f"[echo-delay-number-check] FAIL - {len(unexercised)} of "
              f"{len(REGISTERED) + len(REGISTERED_LISTS)} registered keys were "
              f"NEVER EXERCISED by the document.  A registration the scan never "
              f"reaches checks nothing and overstates coverage: {unexercised}")
        return 1

    print(f"[echo-delay-number-check] completeness: all "
          f"{len(REGISTERED) + len(REGISTERED_LISTS)} registered keys "
          f"exercised")
    print("[echo-delay-number-check] OK")
    return 0


def main() -> int:
    global _MUTATE
    if "--mutation-receipt" in sys.argv:
        # FIX (vii), THIS LANE'S ADDITION: a checker that cannot FAIL is not a
        # checker.  Perturb every shipped value by 1.5x and assert non-zero.
        _MUTATE = True
        rc = run()
        print(f"[echo-delay-number-check] MUTATION RECEIPT: perturbed sources "
              f"by 1.5x, checker returned {rc}")
        if rc == 0:
            print("[echo-delay-number-check] FAIL - the checker PASSED on "
                  "mutated sources; it is not fireable")
            return 1
        print("[echo-delay-number-check] MUTATION RECEIPT OK - the checker is "
              "demonstrated FIREABLE")
        return 0
    return run()


if __name__ == "__main__":
    sys.exit(main())

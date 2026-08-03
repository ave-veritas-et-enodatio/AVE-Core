#!/usr/bin/env python3
"""Gating numeral check for the cold-Q v2.4 ROOT-certification result doc.

Every BACKTICKED numeral in
``research/2026-08-03_coldq-pole-v2.4-root_result.md`` must either be
REGISTERED against a value in the shipped
``research/drivers/coldq_pole_v2p4_root_results.json`` (or recomputed from it)
or be ALLOW-LISTED with a stated reason.  An unregistered numeral is a FAIL.

THE THREE FIXES ROUTED BY THE PR #854 DOCKET AND FROZEN PRE-MEASUREMENT
----------------------------------------------------------------------
Prereg section 4.5, frozen:

  "this lane's gating number check implements (i) a MINIMUM SIGNIFICANT-DIGITS
   FLOOR of 3, machine-enforced, below which a numeral token may NOT be
   registered against the shipped JSON and MUST be allow-listed with a stated
   reason; (ii) PER-SITE rather than global dedup, so every occurrence of a
   numeral is checked and the reported counts describe SITES rather than
   distinct tokens; and (iii) LIST-VALUED REGISTRATION, so that a bracketed
   count vector such as the G5 isolation counts or the FT-5 artifact counts is
   registered against the shipped JSON list as a whole rather than decomposed
   into single-digit tokens that the significant-digits floor would force onto
   the allow-list"

(i) closes the attribution defect the #854 re-audit found: a one- or two-digit
    token "registering" against an unrelated JSON value is not machine-tied to
    anything, and counting it as registered overstates how much of a document
    is checked.  The floor is enforced at BOTH ends -- a low-digit key in
    REGISTERED is a hard configuration FAIL, and a low-digit token found in the
    doc can only be allow-listed.
(ii) each OCCURRENCE is checked and counted.  The printed counts describe
    SITES, and the distinct-token count is reported separately so the two are
    never confused again.
(iii) list-valued tokens such as `[1, 1, 1, 1, 1]` are matched elementwise
    against a shipped JSON list, so a count vector is machine-tied as a vector
    instead of dissolving into allow-listed single digits.

SCOPE, NARROWED DELIBERATELY (prereg section 4.5, frozen): "the gating number
check scans the RESULT DOC only; the arithmetic of sections 4.3 and 4.4 of this
prereg is reproduced by the driver and reported in the result doc, where it IS
machine-checked, and no claim is made anywhere in this lane that the prereg
itself is machine-checked".

TIGHTEN-TO-SPEC REPAIR, 2026-08-03 (post-ship; the frozen text is unchanged)
--------------------------------------------------------------------------
AS SHIPPED this file did NOT implement the frozen fix (ii).  ``TOKEN_RE`` was
``r"`([^`]+)`"``; a negated character class matches newlines, so the FENCED
CODE BLOCK at result-doc lines 99-103 was consumed as a single "token" that
swallowed one of its own closing back-ticks.  That INVERTED back-tick pairing
for the whole remainder of the document: from line ~97 onward, opening
delimiters were read as closing ones.  Result: 71 sites were reported where
151 exist, and 34 of the 72 keys registered in this file -- EVERY bin numeral,
G2b's fitted ``c``, and the run digest -- were never exercised at all.

The repair is a TIGHTENING, not a loosening.  Rule 11 forbids dropping or
widening a frozen criterion after a result is seen; it does not forbid making
an implementation actually meet the criterion it was frozen to meet.  The
frozen text says "every occurrence of a numeral is checked".  As shipped, it
was not.  Three changes, all in the direction of MORE checking:

  (a) ``TOKEN_RE`` excludes newlines (``r"`([^`\\n]+)`"``), the form used by
      the v1 checker at research/drivers/coldq_pole_derivation_number_check.py.
      Triple-back-tick fences no longer pair with anything, so pairing parity
      is restored and every inline site downstream of a fenced block is read.
  (b) a COMPLETENESS GUARD: any key in REGISTERED or REGISTERED_LISTS that the
      document never exercises is a hard configuration FAIL.  A registration
      that is never reached checks nothing, and its presence in this file
      overstates how much of the document is machine-tied -- which is the
      defect that hid (a) for a whole ship cycle.
  (c) the one token the repair newly exposed as unregistered, ``0.28430``, is
      allow-listed with its provenance (below).

TWO STATEMENTS SHIPPED WITH THIS LANE WERE FALSE WHEN MADE, and are corrected
in the result doc rather than quietly dropped; see result doc section 8.
"""
from __future__ import annotations

import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOC = os.path.join(REPO, "research",
                   "2026-08-03_coldq-pole-v2.4-root_result.md")
JSON_PATH = os.path.join(REPO, "research", "drivers",
                         "coldq_pole_v2p4_root_results.json")

with open(JSON_PATH, encoding="utf-8") as _fh:
    J = json.load(_fh)

MIN_SIG_DIGITS = 3


def P(path):
    """Read a '/'-separated path out of the shipped object."""
    cur = J
    for part in path.strip("/").split("/"):
        if isinstance(cur, list):
            cur = cur[int(part)]
        else:
            cur = cur[part]
    return cur


def _g2_diag_row(n):
    for r in P("gates/G2/diagnostic/rows"):
        if r["n"] == n:
            return r
    raise KeyError(n)


def _g2b_resid(n):
    for r in P("gates/G2b/residuals"):
        if r["n"] == n:
            return r["residual"]
    raise KeyError(n)


def _g2b_err(n, key="gates/G2b/errors"):
    for r in P(key):
        if r["n"] == n:
            return r["e_vs_ref"]
    raise KeyError(n)


def _g2b_ratio(pair):
    for r in P("gates/G2b/ratios"):
        if r["pair"] == pair:
            return r["ratio"]
    raise KeyError(pair)


GATES = "gates/"
FT = "self_tests/"
ADJ = "adjudication/"
CMP = "comparators/"
DIAG = "diagnostics/"

# --- REGISTERED: token -> a callable returning the shipped value ------------
REGISTERED = {
    # the certified root and its projections
    "1.853655210840878848320699157729883961213":
        lambda: P("certified_root/Omega_re_mp"),
    "-1.00725678314331889260211374956072904467":
        lambda: P("certified_root/Omega_im_mp"),
    "1.8536552108408788": lambda: P("certified_root/Omega_re"),
    "-1.0072567831433188": lambda: P("certified_root/Omega_im"),
    "2.109645436528558": lambda: P("certified_root/abs_Omega"),
    "0.2648078872629827": lambda: P(ADJ + "omega_R_M_g"),
    "0.14389382616333127": lambda: P(ADJ + "omega_I_M_g"),
    "0.9201502744197102": lambda: P(ADJ + "Q"),
    # gates
    "1.038488291045556e-15": lambda: P(GATES + "G0/measured"),
    "4.726832751705419e-50": lambda: P(GATES + "G1/measured"),
    "8.090607956292325e-14": lambda: P(GATES + "G2/measured"),
    "3.332294747541498e-14": lambda: P(GATES + "G3/measured"),
    "5.277782707837865e-47": lambda: P(GATES + "G4/measured_a"),
    "1.755941633596894e-08": lambda: P(GATES + "G4/measured_b"),
    "6.803231574438666e-07": lambda: P(GATES + "G6/measured"),
    "0.28423799223517354": lambda: P(GATES + "G7/measured_a"),
    "0.19696614906560894": lambda: P(GATES + "G7/measured_b"),
    "1.8618720608205777e-46": lambda: P(GATES + "G8/measured"),
    "9.273121713408482e-47": lambda: P(GATES + "G10/measured_b"),
    # G2b -- the convergence law
    "6.216374478994577": lambda: P(GATES + "G2b/c"),
    "12.962558101032272": lambda: P(GATES + "G2b/lnC"),
    "0.08484862390265135": lambda: P(GATES + "G2b/max_abs_residual"),
    "8.090599741070316e-14": lambda: _g2b_err(48),
    "1.1708996452296386e-16": lambda: _g2b_err(64),
    "2.9026479440283196e-19": lambda: _g2b_err(80),
    "-0.039741": lambda: _g2b_resid(48),
    "0.084849": lambda: _g2b_resid(64),
    "-0.045108": lambda: _g2b_resid(80),
    "690.9729432434473": lambda: _g2b_ratio("e(48)/e(64)"),
    "403.39016918622724": lambda: _g2b_ratio("e(64)/e(80)"),
    # the n = 32 NON-GATED diagnostic
    "1.853655211103967150148849766702804665292":
        lambda: _g2_diag_row(32)["Omega_re_mp"],
    "-1.00725678315784204770526531401798871333":
        lambda: _g2_diag_row(32)["Omega_im_mp"],
    "1.2496816369074884e-10":
        lambda: _g2_diag_row(32)["e_vs_ref_measured"],
    "2.2779698805088156e-10":
        lambda: _g2_diag_row(32)["e_vs_ref_predicted_out_of_sample"],
    "1.822840164432575":
        lambda: _g2_diag_row(32)["predicted_over_measured"],
    "1.2496816389659964e-10":
        lambda: P(GATES + "G2/diagnostic/full_ladder_max_pairwise"),
    # F3: the SAME 32 <-> 80 separation under the other ordering of the
    # relative-separation denominator.  Shipped, and it is v2.2's published
    # number -- so both forms are machine-tied here rather than one being
    # allow-listed as un-readable cross-lane prose.
    "1.2496816388248957e-10":
        lambda: _g2_diag_row(32)["rel_vs_certification_rungs"]["80"],
    # self-tests
    "2.0668129728690202e-12": lambda: P(FT + "FT_0/measured"),
    "9.946402719819208e-12": lambda: P(FT + "FT_1/measured"),
    "0.000440375300940382": lambda: P(FT + "FT_2/measured"),
    "0.07345138526200583": lambda: P(FT + "FT_2b/c"),
    "0.3485948410197033": lambda: P(FT + "FT_3/measured"),
    "4.316731050519307e-17": lambda: P(FT + "FT_4/measured_a"),
    "0.0004403753009474462": lambda: P(FT + "FT_4/measured_b"),
    "0.0005872196298821127": lambda: P(FT + "FT_6/measured"),
    "1.5015831404915055e-46": lambda: P(FT + "FT_7/measured_a"),
    "4.440892098500626e-16": lambda: P(FT + "FT_7/measured_b"),
    "6.013720615540751e-07": lambda: P(FT + "FT_8/measured"),
    "0.03167549395692262": lambda: P(FT + "FT_10/measured_a"),
    "0.0005836018036712878": lambda: P(FT + "FT_10/measured_b"),
    # bins and comparators
    "-0.2913322255921462": lambda: P(ADJ + "D_omega"),
    "-0.2791340846729915": lambda: P(ADJ + "D_omega_shortcut"),
    "-0.5618777615951112": lambda: P(ADJ + "D_Q"),
    "1.1800633047169806": lambda: P(ADJ + "dist_to_Q_GR"),
    "1.07984972558029": lambda: P(ADJ + "dist_to_Q_convention"),
    "2.0497191011235953": lambda: P(ADJ + "BIN_2_flag1_window/0"),
    "2.0501067895683454": lambda: P(ADJ + "BIN_2_flag1_window/1"),
    "0.37367": lambda: P(CMP + "omega_R_GR"),
    "0.08896": lambda: P(CMP + "omega_I_GR"),
    "2.1002135791366907": lambda: P(CMP + "Q_GR"),
    "0.3673469387755102": lambda: P(CMP + "omega_R_shortcut"),
    # localization
    "2.0000000000000004": lambda: P("localization/u_energy"),
    "0.040561477092864194": lambda: P("localization/wall_fraction_of_peak"),
    # the artifact convergence diagnostic (non-gating, still machine-tied)
    "0.25002341694486013": lambda: P(DIAG + "artifact_convergence/c"),
    "0.17911773057438807":
        lambda: P(DIAG + "artifact_convergence/max_abs_residual"),
    "0.4634575039104712":
        lambda: _g2b_err(48, DIAG + "artifact_convergence/errors"),
    "0.4611632142706101":
        lambda: _g2b_err(64, DIAG + "artifact_convergence/errors"),
    "0.27680695848541004":
        lambda: _g2b_err(80, DIAG + "artifact_convergence/errors"),
    # the full-ladder convergence diagnostic (non-gating)
    "6.043847309998414":
        lambda: P(DIAG + "spectral_convergence_full_ladder/c"),
    "0.18870776957898983":
        lambda: P(DIAG + "spectral_convergence_full_ladder/max_abs_residual"),
    # digests
    "6cec005e0155513a": lambda: P("_digest"),
    "75d7fc892e625892": lambda: P(FT + "FT_9/digest"),
    "95676d738972694d": lambda: P(FT + "FT_9/perturbed_digest"),
}

# --- LIST-VALUED REGISTRATION (fix iii) ------------------------------------
REGISTERED_LISTS = {
    "[1, 1, 1, 1, 1]": lambda: P(GATES + "G5/counts"),
    "[2, 1, 2, 3, 0]": lambda: P(FT + "FT_5/artifact_counts"),
    "[1, 1, 0, 0, 0]": lambda: P(FT + "FT_5/edge_counts"),
    "[48, 64, 80, 96]": lambda: P(GATES + "G2/certification_ladder"),
    "[4.4, 7.6]": lambda: P(GATES + "G2b/c_band"),
}

# --- ALLOW-LIST: every entry names WHY it is not machine-tied ---------------
ALLOWED = {
    # frozen tolerances, thresholds and bands (they live in the PREREG)
    "1e-13": "frozen G0 tolerance / FT-0 threshold (prereg sections 5-6)",
    "1e-20": "frozen G1 and G10(b) tolerances (prereg section 5)",
    "1e-10": "frozen G2 tolerance / FT-1 offset size (prereg sections 4-6)",
    "1e-12": "frozen G3 tolerance / FT-0 mutation size / FT-2b stagnation "
             "offset (prereg sections 4-6)",
    "1e-25": "frozen G4(a) tolerance / FT-4(a) threshold (prereg section 5)",
    "1e-6": "frozen G4(b) tolerance, dedupe radius, and the FT-2 / FT-3 / "
            "FT-4(b) / FT-8 / FT-10(a) thresholds (prereg sections 4-6)",
    "1e-5": "frozen G6 tolerance / FT-10(b) threshold (prereg sections 5-6)",
    "1e-3": "frozen G7 tolerance / FT-7 reverse threshold / FT-6 and FT-10 "
            "mutation sizes (prereg sections 5-6)",
    "1e-9": "frozen G8 tolerance / FT-8 threshold (prereg sections 5-6)",
    "1e-40": "frozen G10(a) tolerance (prereg section 5)",
    "1e-15": "frozen FT-1 threshold and the FT-9 digest perturbation size",
    "+1e-12": "the FT-2b stagnation offset written with an explicit sign in "
              "the self-test table's mutation column (prereg section 6)",
    "1e-16": "an ORDER OF MAGNITUDE in the FT-7 expectation prose, not a "
             "measured value",
    "0.40": "frozen G2b fit-residual floor (prereg section 4.4(c))",
    "0.03": "frozen BIN-1/BIN-2 MATCH boundary and the (1+nu_vac) rider's "
            "trip level (prereg sections 7.2-7.3)",
    "4.4": "frozen G2b c-band lower edge (prereg section 4.4(c))",
    "7.6": "frozen G2b c-band upper edge (prereg section 4.4(c))",
    "0.5": "frozen isolation radius R_iso (prereg section 4.3)",
    "0.10": "frozen BIN-1/BIN-2 NEAR-vs-MISS boundary (prereg section 7.2)",
    "18/49": "the standing corpus shortcut, quoted as a FRACTION not a "
             "decimal; its decimal is registered as omega_R_shortcut",
    # prereg-quoted numerals that are NOT results of this battery
    "2.277976e-10": "the out-of-sample prediction as QUOTED IN THE PREREG at "
                    "6 significant figures (frozen section 4.4(e)); the "
                    "battery's full-precision value is registered separately",
    "1.249682e-10": "the measured e(32) as QUOTED IN THE PREREG at 6 "
                    "significant figures (frozen section 4.4(e)); the "
                    "battery's full-precision value is registered separately",
    "5.3e-16": "the v2.1 coefficient-tail receipt, an I20 PRIOR-LANE numeral "
               "quoted from research/2026-08-03_coldq-pole-v2.1_prereg-"
               "FROZEN.md:489 @ 7d8fe484 -- not a value of this battery",
    "4.7143": "the residual-floor headroom factor, PREREG arithmetic "
              "(section 4.4(c)); this checker scans the result doc only",
    "76.3426": "the G2 tolerance headroom factor, PREREG arithmetic "
               "(section 4.4(d)); this checker scans the result doc only",
    "2.9206": "the c-band ratio-tolerance factor, PREREG arithmetic "
              "(section 4.4(c)); this checker scans the result doc only",
    "5.775382": "a PAIRWISE c estimate from the prereg's section 4.4(b) fit on "
                "the in-repo blob at 982c4c9b; PREREG arithmetic, not a value "
                "of this battery",
    "6.100131": "a PAIRWISE c estimate, same provenance",
    "6.354001": "a PAIRWISE c estimate, same provenance",
    "0.578619": "the total monotonic drift across the pairwise c sequence, "
                "6.354001 - 5.775382, arithmetic on two allow-listed PREREG "
                "numerals; not a value of this battery",
    "[4.775382, 7.354001]": "the COUNTERFACTUAL lane-only G2b c band -- this "
                            "lane's own pairwise span widened by the prereg's "
                            "plus/minus 1.0, computed here to show that no "
                            "gate OUTCOME depends on the relayed I22 range.  "
                            "It is NOT a frozen band and gates nothing",
    "5.4": "the lower edge of the ORCHESTRATOR-RELAYED, UNVERIFIED I22 range "
           "(prereg section 4.4(c)); names no value of this battery",
    "6.6": "the upper edge of the same relayed I22 range",
    # cross-lane numerals quoted at v2.2's published precision (its JSON is on
    # PR #856's branch, NOT on origin/main, so it cannot be read from here)
    "1.0385e-15": "v2.2's published G0, quoted for the expectation-5 "
                  "regression check at the precision v2.2 printed",
    "4.7268e-50": "v2.2's published G1, same",
    "3.3323e-14": "v2.2's published G3, same",
    "5.2778e-47": "v2.2's published G4(a), same",
    "1.7559e-08": "v2.2's published G4(b), same",
    "6.8032e-07": "v2.2's published G6, same",
    "0.28424": "v2.2's published G7(a), same",
    "0.19697": "v2.2's published G7(b), same",
    "1.8619e-46": "v2.2's published G8, same",
    "9.2731e-47": "v2.2's published G10(b), same",
    "1.2497e-10": "v2.2's published G2 failure value, quoted in the "
                  "expectation-4 regression check at v2.2's precision",
    "8.09e-14": "the expectation-2 statement, quoted at the precision the "
                "prereg froze it (section 9)",
    "2.220446049250313e-16": "IEEE-754 binary64 machine epsilon, 2**-52 -- a "
                             "property of the FORMAT, not a value of this "
                             "battery; quoted to size FT-7(b) in ULPs",
    # FLAG-1's corpus-precision numerals, none of them values of this battery
    "2.099438202247191": "the ROUNDED-PROSE Q_GR of FLAG-1, re-computed from "
                         "the 4-s.f. corpus pair; a PREREG numeral (section "
                         "7.3), not a measurement here",
    "2.0994": "the same rounded-prose Q_GR as actually written at "
              "research/2026-07-30_qlaw-derivation_scoping.md:401 -- the "
              "citation-precision note's whole point",
    "0.3737": "the 4-s.f. corpus omega_R M at "
              "research/2026-07-30_qlaw-derivation_scoping.md:399",
    "0.0890": "the 4-s.f. corpus omega_I M at "
              "research/2026-07-30_qlaw-derivation_scoping.md:400",
    # cross-lane numerals from PR #845 (v1), quoted inside a FLAG restatement
    "0.28430": "v1's FT-2 CLAMPED-wall relative shift, an I20-class PRIOR-LANE "
               "numeral quoted verbatim from research/2026-08-02_coldq-pole-"
               "derivation_result.md:58 (shipped by that lane under "
               "selftests/FT2_clamped_wall/rel_shift_vs_traction_free) -- it "
               "is the subject of FLAG-9 and is not a value of this battery",
    # structural / label integers -- BELOW the significant-digits floor, so
    # they can only be allow-listed (fix i), never registered
    "0.0": "an exact zero: G10(a)'s measured operator reality, and the FT-7 "
           "collapse condition that did NOT occur",
    "1": "structural integer / the frozen G5 count / a list element",
    "2": "the multipole index ell = 2, the factor 2 in Q, and BIN-2's "
         "convention comparator",
    "2.0": "the corpus 2-pi-convention comparator Q = ell = 2 (prereg "
           "section 7.3)",
    "3": "structural integer / the minimum-significant-digits floor",
    "4": "the spin-2 energy weight (ell-1)(ell+2) = ell**2+ell-2 at ell = 2, "
         "an exact integer -- the numeral whose two spellings the FT-7(b) "
         "attribution correction shows to be bit-identical",
    "7": "x_sat = 7, the r_sat coefficient (prereg I1)",
    "8": "the FT-2 / FT-4(b) under-resolved Chebyshev order",
    "32": "a ladder rung -- the NON-GATED diagnostic order",
    "36": "the orchestrator-relayed FAIL/PASS boundary's upper order, an "
          "UNVERIFIED I22 numeral naming no value of this battery",
    "40": "the order at which the v2.1 coefficient tail resolves (I20)",
    "48": "the primary Chebyshev order and a certification-ladder rung",
    "50": "the primary extended precision dps",
    "64": "a certification-ladder rung",
    "80": "a certification-ladder rung and the high-precision dps",
    "96": "the certification ladder's reference rung",
    "1.0": "the BIN-3 localization window's inner edge, r/r_sat = 1",
    "17.6": "a ratio of two registered values (the G2b c-band lower edge "
            "divided by the artifact's fitted c), stated in prose",
    "1.82": "the predicted/measured ratio quoted to 3 s.f. in prose; its "
            "full-precision value is registered",
    "1.08": "the BIN-2 distance to the convention comparator quoted to 3 s.f. "
            "in prose; its full-precision value is registered",
    "1.18": "the BIN-2 distance to Q_GR quoted to 3 s.f. in prose; its "
            "full-precision value is registered",
    "0.920": "Q quoted to 3 s.f. in prose; its full-precision value is "
             "registered",
    "2.100": "Q_GR quoted to 4 s.f. in prose; its full-precision value is "
             "registered",
    "6.2": "the expectation-3 statement's approximate c, quoted at the "
           "precision the prereg froze it (section 9)",
    "0.085": "the expectation-3 statement's approximate residual, same",
    # commit SHAs that happen to be all-digit or hex-with-digits
    "052ccbba": "commit SHA -- the PR #845 merge",
    "00724432": "commit SHA -- the v2 prereg",
    "36186006": "commit SHA -- THIS lane's frozen prereg",
    "982c4c9b": "commit SHA -- the v2.2 result commit and the in-repo blob "
                "this lane fitted its convergence law on",
}

NON_REGISTRABLE = {"_runtime_sec", "262.19", "255.27"}

# TIGHTEN-TO-SPEC (a), 2026-08-03.  The newline exclusion is load-bearing: a
# bare [^`]+ swallows a fenced code block whole, consumes one of its three
# closing back-ticks, and inverts delimiter parity for the entire remainder of
# the file.  Same form as the v1 checker.
TOKEN_RE = re.compile(r"`([^`\n]+)`")
NUM_RE = re.compile(r"^[-+]?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?$")
LIST_RE = re.compile(r"^\[\s*[-+0-9.eE]+(\s*,\s*[-+0-9.eE]+)*\s*\]$")
# TIGHTEN-TO-SPEC (b), consequence.  A run digest is a 16-hex-character blake2b
# token; NUM_RE never matched one, so the three digest registrations below were
# unreachable BY CLASSIFICATION even after the regex repair.  They are shipped
# values of this battery and are checked against the JSON like any other; the
# significant-digits floor does not apply to a hash, which is not a numeral.
DIGEST_RE = re.compile(r"^[0-9a-f]{16}$")


def is_number(tok: str) -> bool:
    return bool(NUM_RE.match(tok.strip()))


def is_digest(tok: str) -> bool:
    return bool(DIGEST_RE.match(tok.strip()))


def is_numlist(tok: str) -> bool:
    return bool(LIST_RE.match(tok.strip()))


def sig_digits(token: str) -> int:
    """Significant digits carried by a numeral token as WRITTEN."""
    t = token.strip().lstrip("+-")
    if "e" in t.lower():
        t = t.lower().split("e")[0]
    t = t.replace(".", "")
    t = t.lstrip("0")
    return len(t.rstrip()) if t else 1


def matches(token: str, value) -> bool:
    """The token must be the correctly-rounded value at its own precision."""
    t = token.strip()
    if isinstance(value, str):
        return t == value.strip()
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


def main() -> int:
    # --- configuration guards, checked BEFORE the doc is read --------------
    for bad in NON_REGISTRABLE:
        if bad in REGISTERED or bad in ALLOWED or bad in REGISTERED_LISTS:
            print(f"[coldq-v24-number-check] FAIL - {bad} is NON_REGISTRABLE "
                  f"(machine-dependent) and must not be registered or "
                  f"allow-listed")
            return 1
    # FIX (i), enforced at the CONFIGURATION end: a token below the floor may
    # not even appear as a REGISTERED key.
    low = sorted(k for k in REGISTERED
                 if is_number(k) and sig_digits(k) < MIN_SIG_DIGITS)
    if low:
        print(f"[coldq-v24-number-check] FAIL - these REGISTERED keys carry "
              f"fewer than {MIN_SIG_DIGITS} significant digits and must be "
              f"allow-listed instead: {low}")
        return 1

    with open(DOC, encoding="utf-8") as fh:
        text = fh.read()

    # FIX (ii): PER-SITE dedup.  Every occurrence is checked; the dedup key is
    # (token, line), so a token repeated on one line is one site while the same
    # token on another line is a DIFFERENT site that is checked again.
    seen_sites, tokens = set(), set()
    bad_rows, n_reg, n_allow = [], 0, 0
    # TIGHTEN-TO-SPEC (b): every REGISTERED / REGISTERED_LISTS key must be
    # reached by at least one site in the document.  A registration the scan
    # never touches is dead configuration that inflates the apparent coverage.
    exercised = set()
    for m in TOKEN_RE.finditer(text):
        tok = m.group(1).strip()
        numeric, listy, digesty = is_number(tok), is_numlist(tok), is_digest(tok)
        if not (numeric or listy or digesty):
            continue
        line = text.count("\n", 0, m.start()) + 1
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
                bad_rows.append((tok, line, "UNREGISTERED list - not in the "
                                            "shipped JSON and not allow-listed"))
            continue

        # FIX (i), enforced at the DOCUMENT end.  A digest is exempt: it is a
        # 16-character hash, not a numeral carrying significant figures.
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

    print(f"[coldq-v24-number-check] doc: {os.path.relpath(DOC, REPO)}")
    print("[coldq-v24-number-check] scope: BACKTICKED numerals in the RESULT "
          "DOC only; the prereg is NOT scanned (prereg section 4.5, frozen)")
    print(f"[coldq-v24-number-check] min significant digits for registration: "
          f"{MIN_SIG_DIGITS} | dedup: PER-SITE")
    print(f"[coldq-v24-number-check] SITES {len(seen_sites)} "
          f"(distinct tokens {len(tokens)}) | registered {n_reg} | "
          f"allow-listed {n_allow} | unregistered {len(bad_rows)}")
    if bad_rows:
        for tok, line, why in bad_rows:
            print(f"  FAIL  line {line}  `{tok}`  {why}")
        return 1

    # TIGHTEN-TO-SPEC (b): the completeness guard, run AFTER the scan.
    unexercised = sorted((set(REGISTERED) | set(REGISTERED_LISTS))
                         - exercised)
    if unexercised:
        print(f"[coldq-v24-number-check] FAIL - {len(unexercised)} of "
              f"{len(REGISTERED) + len(REGISTERED_LISTS)} registered keys were "
              f"NEVER EXERCISED by the document.  A registration the scan never "
              f"reaches checks nothing and overstates coverage; either the key "
              f"is dead configuration and must be removed, or the scanner is "
              f"not reaching the site: {unexercised}")
        return 1

    print(f"[coldq-v24-number-check] completeness: all "
          f"{len(REGISTERED) + len(REGISTERED_LISTS)} registered keys "
          f"exercised")
    print("[coldq-v24-number-check] OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

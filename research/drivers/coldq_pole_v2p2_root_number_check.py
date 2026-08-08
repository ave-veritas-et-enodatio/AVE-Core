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

import contextlib
import io
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
    "1e-12": "frozen G3 tolerance (prereg section 5); ALSO, from the 2026-08-03 "
             "post-review section 2.5 table, the numeric reading of a "
             "'12 significant digits' stability premise -- a PREREG/prior-lane "
             "premise, not a measurement of this battery",
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
    # --- 2026-08-03 POST-REVIEW additions (PR #856 findings 2, 3, 5, 9). ---
    # Each of these is a COUNTERFACTUAL or a PREREG numeral introduced by the
    # post-review correction notes.  NONE is a battery output and NONE is in the
    # shipped JSON, so each is ALLOW-LISTED with its formula or its source named
    # rather than registered against a path.  The checker's REGISTERED table and
    # its matching logic are UNCHANGED by this repair -- changing gating logic
    # after the result is the post-result move Rule 11 forbids, and the two
    # known gaps in that logic (a minimum significant-digit floor, and per-site
    # rather than global dedup) are ROUTED to the v2.3 checker, disclosed in the
    # docket fragment, NOT fixed here.
    "1e-8": "section 2.5 COUNTERFACTUAL tolerance: the prereg's own "
            "'two orders looser than the measured evidence supports' rule "
            "(prereg :476) applied to the CORRECTED '~10 digits from n = 32' "
            "premise of cb2012af.  Not a frozen tolerance, not a measurement, "
            "adjudicates nothing",
    "80.02": "section 2.5 COUNTERFACTUAL margin = 1e-8 / 1.2496816388248957e-10 "
             "(the counterfactual tolerance above divided by the SHIPPED G2 "
             "measured value, which IS registered).  Reported to one decimal "
             "beyond the leading digits; adjudicates nothing",
    "1236": "section 2.5 COUNTERFACTUAL margin = 1e-10 / 8.0906e-14 (the FROZEN "
            "G2 tolerance divided by the SHIPPED n = 48 convergence row, which "
            "IS registered) -- the margin a ladder starting at n = 48 would "
            "have had at the frozen tolerance.  Adjudicates nothing",
    "5.8": "section 2.2 root-exponential rate c = -dlnE/dsqrt(n) on the FIRST "
           "interval the shipped convergence table prints (n = 32 -> 48): "
           "(ln 1.2497e-10 - ln 8.0906e-14)/(sqrt(48)-sqrt(32)) = 5.7754, "
           "quoted to two significant figures.  Derived from two REGISTERED "
           "tokens by the formula stated here; a post-review characterization, "
           "not a battery output",
    "6.4": "section 2.2 root-exponential rate on the LAST interval the shipped "
           "convergence table prints (n = 64 -> 80): "
           "(ln 1.1709e-16 - ln 2.9026e-19)/(sqrt(80)-sqrt(64)) = 6.3540, "
           "quoted to two significant figures.  Same formula, same two "
           "REGISTERED-token provenance",
    "5.4": "section 2.2: the same rate on the LOWEST interval of the twelve-rung "
           "post-review extension (n = 24 -> 32) = 5.4718.  The extension is a "
           "POST-RESULT reproduction recorded in the docket fragment; it is NOT "
           "in the shipped JSON and it adjudicates nothing",
    "6.6": "section 2.2: the same rate at n = 88 -> 96 of that extension = "
           "6.6206 -- the top of the band over n = 24 -> 96.  The rate keeps "
           "climbing above n = 96 (6.71, 6.81), which the doc states rather "
           "than truncating.  POST-RESULT, docket-recorded, adjudicates nothing",
    "-2.857143e-07": "section 3.5 post-review correction of the FROZEN PREREG's "
                     "FT-8 non-vacuity arithmetic (prereg :343, which quotes "
                     "+/-1.43e-06).  Exact value of the frozen mutation "
                     "1e-6*(x_sat - 7)/7 at x_sat = 5.  A PREREG-arithmetic "
                     "correction, disclosed not edited; NOT a battery output",
    "5.714286e-07": "same, at x_sat = 11: 1e-6*(11 - 7)/7.  A PREREG-arithmetic "
                    "correction, disclosed not edited; NOT a battery output",
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


def scan_spans(text: str) -> list[str]:
    """Every back-tick span in `text`, paired PER LINE.

    PARITY IMMUNISATION (ruling R27, `_orchestration/docket-entries/
    2026-08-07-rulings-r23-r27.md`; defect found by the #912 sibling audit,
    `_orchestration/docket-entries/2026-08-06-backtick-parity.md` section 6).

    This was a single `TOKEN_RE.finditer(text)` over the WHOLE document.  The
    token class ``[^`]+`` does NOT exclude newlines, so ONE line carrying an ODD
    back-tick count flips the open/close phase for the ENTIRE REST OF THE
    DOCUMENT: every numeral below it lands in a gap the scanner never reads --
    silently, with the gate still green.

    On this checker's document the repair is a MEASURED NO-OP: +0/-0 spans, 0
    odd-parity lines, re-measured at the landing commit.  It ships anyway because
    the defect is a TIME BOMB -- the first odd-parity line anyone adds unscans
    everything below it.  Per-line pairing fails SAFE: a malformed line can only
    ever ADD spans on its own line, never remove coverage from the lines below.

    SCOPE, and it is not a general theorem: a CommonMark code span may straddle a
    newline; such a span is read by global pairing and missed per-line.  This
    document contains none (hence the measured +0/-0, not an argument).  The same
    bounded hole is the repo's standing convention for this scan.  What the
    repair removes is the UNBOUNDED hole.
    """
    return [m for line in text.splitlines() for m in TOKEN_RE.findall(line)]


def _scan_spans_legacy_global(text: str) -> list[str]:
    """The PRE-REPAIR scanner (GLOBAL pairing), retained for exactly ONE purpose:
    it is the parity mutation's FORCED-OFF arm.  A mutation the old scanner
    catches too proves nothing about the repair, so the receipt re-runs `main`
    with this scanner injected and REQUIRES it to MISS.  Not reachable from any
    gate -- `main`'s `_scanner` parameter has no argv spelling."""
    return TOKEN_RE.findall(text)


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


def main(_text_override: str | None = None, _scanner=None) -> int:
    """The gating check.

    The two private parameters are SEAMS FOR THE MUTATION RECEIPT and have no
    argv spelling, so nothing a caller can type reaches them:
      * `_text_override` -- run the shipped classification over an IN-MEMORY
        planted copy of the document, leaving the file on disk untouched;
      * `_scanner` -- substitute the pre-repair global-paired scanner, which is
        how the receipt FORCES THE FIX OFF and demonstrates the same plant is
        MISSED without it.
    Both default to the shipped behaviour.
    """
    scan = _scanner or scan_spans
    for bad in NON_REGISTRABLE:
        if bad in REGISTERED or bad in ALLOWED:
            print(f"[coldq-v22-number-check] FAIL - {bad} is NON_REGISTRABLE "
                  f"(machine-dependent) and must not be registered or "
                  f"allow-listed")
            return 1

    if _text_override is None:
        with open(DOC, encoding="utf-8") as fh:
            text = fh.read()
    else:
        text = _text_override
    seen, bad_rows, n_reg, n_allow = set(), [], 0, 0
    for raw in scan(text):
        tok = raw.strip()
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


# ---------------------------------------------------------------------------
# Mutation receipt for the parity immunisation (ruling R27).
# ---------------------------------------------------------------------------
#
# The repair is a MEASURED NO-OP on today's document(s) (+0/-0 spans, 0
# odd-parity lines).  A no-op repair is exactly the kind that rots into
# decoration, so it ships with a receipt that DEMONSTRATES the failure mode it
# removes, on an in-memory copy, with the fix forced off as the counterfactual.

PARITY_PROBE_LINE = ("Parity probe planted by the mutation receipt: one ` "
                     "unbalanced back-tick.")
PARITY_PLANT_TOKEN = "1.2345678e-77"
PARITY_PLANT_LINE = f"Planted by the mutation receipt: `{PARITY_PLANT_TOKEN}`."

# Every arm below must appear in this set and must be True.  Enumerated rather
# than counted so a DROPPED arm is a FAIL, not a silently smaller receipt.
PARITY_ARMS = ("anti-vacuity", "negative-control", "scanner-level", "CATCH",
               "forced-off MISS")


def mutation_receipt() -> int:
    """Prove the per-line parity repair is load-bearing, end-to-end.

    Five arms, every one EXECUTED against the SHIPPED `main`, none asserted:

      anti-vacuity ..... the planted numeral is absent from the real document(s)
                         and is in none of this checker's registries.  Without
                         this the plant could be a registered value and the whole
                         receipt would be vacuous.
      negative-control . the UNPERTURBED document(s) must PASS, so the catch is
                         attributable to the plant and not to standing red.
      scanner-level .... the repaired scanner READS the planted numeral and the
                         pre-repair one does NOT.  Names the mechanism, so a
                         failure localises instead of pointing at `main`.
      CATCH ............ `main` over the planted text must return 1.
      forced-off MISS .. `main` over the SAME planted text with the PRE-REPAIR
                         global-paired scanner injected must return 0.  This is
                         the arm that makes the receipt a receipt for THE FIX
                         rather than for the checker in general: back the repair
                         out and the mutation goes MISSED.

    The plant is two lines appended IN MEMORY: an odd-back-tick probe line, then
    an unregistered back-ticked numeral below it.  Under global pairing the probe
    line's lone back-tick opens a span that swallows the numeral's opening
    back-tick, so the numeral is never read.  Under per-line pairing the probe
    line yields no span at all and the numeral is read normally.
    """
    text = open(DOC, encoding="utf-8").read()
    planted = text + "\n" + PARITY_PROBE_LINE + "\n" + PARITY_PLANT_LINE + "\n"

    results: dict[str, bool] = {}
    results["anti-vacuity"] = (PARITY_PLANT_TOKEN not in text
                               and PARITY_PLANT_TOKEN not in REGISTERED
                               and PARITY_PLANT_TOKEN not in ALLOWED)
    sink = io.StringIO()
    with contextlib.redirect_stdout(sink):
        rc_clean = main(_text_override=text)
        rc_planted = main(_text_override=planted)
        rc_forced = main(_text_override=planted,
                         _scanner=_scan_spans_legacy_global)
    results["negative-control"] = rc_clean == 0
    results["scanner-level"] = (
        PARITY_PLANT_TOKEN in [s.strip() for s in scan_spans(planted)]
        and PARITY_PLANT_TOKEN not in
        [s.strip() for s in _scan_spans_legacy_global(planted)])
    results["CATCH"] = rc_planted == 1
    results["forced-off MISS"] = rc_forced == 0

    ok = set(results) == set(PARITY_ARMS) and all(results.values())
    for arm in PARITY_ARMS:
        got = results.get(arm)
        print(f"[coldq-v22-number-check]   {arm:<17} "
              f"{'OK' if got else 'FAIL' if got is False else 'MISSING'}")
    if not ok:
        print("[coldq-v22-number-check] --- captured output from the arms ---")
        print(sink.getvalue())
    print(f"[coldq-v22-number-check] parity mutation receipt: "
          f"{'PASS' if ok else 'FAIL'} ({len(PARITY_ARMS)} arms)")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--mutation-receipt" in sys.argv:
        sys.exit(mutation_receipt())
    sys.exit(main())

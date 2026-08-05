#!/usr/bin/env python3
"""Gating numeral check for the cold-Q AXIAL RHO-B result doc.

Every BACKTICKED numeral in ``research/2026-08-04_coldq-axial-rhob_result.md``
must either be REGISTERED against a value in the shipped
``research/drivers/coldq_axial_rhob_results.json`` (or recomputed from it) or be
ALLOW-LISTED with a stated reason.  An unregistered numeral is a FAIL.

ALL SIX ACCUMULATED CHECKER LESSONS ARE IMPLEMENTED FROM THE FIRST COMMIT.
Prereg section 11, frozen:

  "this lane's gating number check implements, from the first commit: (i) a
   MINIMUM SIGNIFICANT-DIGITS FLOOR of 3, machine-enforced at BOTH the
   configuration end and the document end; (ii) PER-SITE rather than global
   dedup, so every occurrence of a numeral is checked and the reported counts
   describe SITES; (iii) LIST-VALUED REGISTRATION, so a bracketed count vector
   is matched elementwise against a shipped JSON list rather than decomposed
   into single-digit tokens; (iv) a NEWLINE-EXCLUDING token pattern, so a
   fenced code block cannot be consumed as one span and invert back-tick
   pairing for the remainder of the document; (v) a COMPLETENESS GUARD making
   any registered key the document never exercises a hard configuration FAIL;
   and (vi) a DIGEST CLASSIFIER, so run digests are checked against the shipped
   JSON as tokens in their own class rather than skipped by a numeral regex
   that never matched them"

SCOPE (frozen, prereg section 11): the gating check scans the RESULT DOC only.
No claim is made anywhere in this lane that the prereg is machine-checked.

ONE ADDITIONAL GUARD THIS LANE ADDS, and it is a defect this lane actually hit
while drafting: an ASCII-MINUS GUARD.  A numeral written with the Unicode
MINUS SIGN U+2212 inside back-ticks is not matched by the numeral regex, so it
would be silently UNCHECKED while looking checked.  The guard fails the
configuration if any back-ticked span contains U+2212.
"""
from __future__ import annotations

import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOC = os.path.join(REPO, "research", "2026-08-04_coldq-axial-rhob_result.md")
JSON_PATH = os.path.join(REPO, "research", "drivers",
                         "coldq_axial_rhob_results.json")

with open(JSON_PATH, encoding="utf-8") as _fh:
    J = json.load(_fh)

MIN_SIG_DIGITS = 3

CTL = "CFG-A-CONTROL"
INF = "CFG-IN-FROB"
BFR = "CFG-BOUND-FROB"


def P(path):
    """Read a '/'-separated path out of the shipped object."""
    cur = J
    for part in path.strip("/").split("/"):
        cur = cur[int(part)] if isinstance(cur, list) else cur[part]
    return cur


def DIAG(key):
    return P(f"adjudication/{INF}/not_adjudicated_diagnostics/{key}")


def TOP(cfg, i, key):
    return P(f"search/{cfg}/top_five/{i}/{key}")


def ROW(cfg, i, key):
    return P(f"gates/{cfg}/G2/rows/{i}/{key}")


# --- REGISTERED: token -> a callable returning the shipped value ------------
REGISTERED = {
    # ---- the negative control and the shared gates
    "2.139211445202149e-40": lambda: P("gates/_global/G-NC/b_root_relsep"),
    "9.960790154561388e-14": lambda: P("gates/_global/G0/measured"),
    "2.0668129844705777e-12": lambda: P("self_tests/_global/FT-0/measured"),
    "0.281050872448155": lambda: P("self_tests/_global/FT-NC/measured"),
    # ---- FT-SHORT, the load-bearing self-test
    "0.2739562093388408": lambda: P("self_tests/_global/FT-SHORT/measured"),
    "1.0763874319332618": lambda: P("self_tests/_global/FT-SHORT/"
                                    "rejected_row_root/0"),
    "-0.02415021827442051": lambda: P("self_tests/_global/FT-SHORT/"
                                      "rejected_row_root/1"),
    # ---- CFG-A-CONTROL gates
    "4.726832751705419e-50": lambda: P(f"gates/{CTL}/G1/measured"),
    "1.2496816388248957e-10": lambda: P(f"gates/{CTL}/G2/measured"),
    "5.918368041595941": lambda: P(f"gates/{CTL}/G2c/parameter"),
    "0.12473145492156945": lambda: P(f"gates/{CTL}/G2c/max_resid"),
    "3.332294747541498e-14": lambda: P(f"gates/{CTL}/G3/measured"),
    "5.277782707837865e-47": lambda: P(f"gates/{CTL}/G4/a_measured"),
    "1.4856751378261543e-09": lambda: P(f"gates/{CTL}/G4/b_measured"),
    "9.132344757601747e-47": lambda: P(f"gates/{CTL}/G8/measured"),
    "9.273121713408482e-47": lambda: P(f"gates/{CTL}/G10/b_measured"),
    # ---- CFG-A-CONTROL self-tests
    "9.946402719819208e-12": lambda: P(f"self_tests/{CTL}/FT-1/measured"),
    "0.00044024054986192525": lambda: P(f"self_tests/{CTL}/FT-2/measured"),
    "2.115446629621273": lambda: P(f"self_tests/{CTL}/FT-2c/parameter"),
    "0.1521820946917692": lambda: P(f"self_tests/{CTL}/FT-3/measured"),
    "4.316731050519307e-17": lambda: P(f"self_tests/{CTL}/FT-4/a_measured"),
    "0.0004403753009474462": lambda: P(f"self_tests/{CTL}/FT-4/b_measured"),
    "3.8343049675985186e-07": lambda: P(f"self_tests/{CTL}/FT-8/measured"),
    "0.0002919046996412571": lambda: P(f"self_tests/{CTL}/FT-10/b_measured"),
    # ---- CFG-IN-FROB gates
    "1.0000000003434282e-10": lambda: P(f"gates/{INF}/G-FROB/ratio"),
    "1.6503104687572565e-50": lambda: P(f"gates/{INF}/G1/measured"),
    "3.6140893550967903e-10": lambda: P(f"gates/{INF}/G2/measured"),
    "7.840463472871456e-16": lambda: ROW(INF, 2, "err_vs_ref"),
    "18.695313410394075": lambda: P(f"gates/{INF}/G2c/parameter"),
    "0.48520667756680425": lambda: P(f"gates/{INF}/G2c/max_resid"),
    "5.057619054190125e-14": lambda: P(f"gates/{INF}/G3/measured"),
    "4.740753178069656e-49": lambda: P(f"gates/{INF}/G4/a_measured"),
    "5.629708455436147e-49": lambda: P(f"gates/{INF}/G8/measured"),
    # ---- the wall gates G-W (the exponents and the reported traction limbs)
    "0.8540436614074668": lambda: P(f"gates/{INF}/G-W/sigma_plus/0"),
    "0.9052029603401721": lambda: P(f"gates/{INF}/G-W/sigma_plus/1"),
    "0.14595633859253326": lambda: P(f"gates/{INF}/G-W/sigma_minus/0"),
    "-0.9052029603401721": lambda: P(f"gates/{INF}/G-W/sigma_minus/1"),
    "1.9439540257849885": lambda: P(f"gates/{INF}/G-W/abs_sigma_gap"),
    "1.8337891396602275": lambda: P(f"gates/{INF}/G-W/resonance_distance"),
    "-0.1459563385925332": lambda: P(f"gates/{INF}/G-W/traction_exponent_plus"),
    "-0.8540436614074667": lambda: P(f"gates/{INF}/G-W/traction_exponent_minus"),
    # ---- CFG-IN-FROB self-tests
    "9.91230144564457e-12": lambda: P(f"self_tests/{INF}/FT-1/measured"),
    "0.00035819373665375967": lambda: P(f"self_tests/{INF}/FT-2/measured"),
    "8.845771752822197": lambda: P(f"self_tests/{INF}/FT-2c/parameter"),
    "0.03667623351896569": lambda: P(f"self_tests/{INF}/FT-3/measured"),
    "1.9013913017026223e-19": lambda: P(f"self_tests/{INF}/FT-4/a_measured"),
    "1.2354164130261005e-05": lambda: P(f"self_tests/{INF}/FT-8/measured"),
    "0.013250813115859395": lambda: P(f"self_tests/{INF}/FT-10/b_measured"),
    # ---- the search
    "3.665073726334936e-13": lambda: P(f"search/{INF}/chosen/nstable_rel"),
    "8.509638653899817e-08": lambda: TOP(INF, 1, "nstable_rel"),
    "0.4197942558740729": lambda: TOP(INF, 1, "Q"),
    "2.976013135309959": lambda: TOP(BFR, 0, "Omega_n48/0"),
    "-0.02673481415359522": lambda: TOP(BFR, 0, "Omega_n48/1"),
    "0.024370271722028894": lambda: TOP(BFR, 0, "Omega_n80/0"),
    "-0.19249955107351446": lambda: TOP(BFR, 0, "Omega_n80/1"),
    "2.956293886300157": lambda: TOP(BFR, 0, "nstable_rel"),
    # ---- the primary seed chain
    "1.8536552108408788": lambda: P("primary_seed_chain/Omega_A_seed/0"),
    "-1.0072567831433188": lambda: P("primary_seed_chain/Omega_A_seed/1"),
    "2.169389621753286": lambda: P("primary_seed_chain/"
                                   "poly_pencil_seed_double/0"),
    "-0.46925128885615547": lambda: P("primary_seed_chain/"
                                      "poly_pencil_seed_double/1"),
    "2.1693896217534925": lambda: P("primary_seed_chain/poly_polished/0"),
    "-0.46925128885126355": lambda: P("primary_seed_chain/poly_polished/1"),
    "-0.20536852387225474": lambda: P(f"primary_seed_chain/{BFR}/Omega/1"),
    "-1.3445557174632785": lambda: P(f"primary_seed_chain/{INF}/Omega/1"),
    # ---- the NOT-ADJUDICATED diagnostics (labelled as such in the doc)
    "1.021058710655384226893259908522031969379": lambda: DIAG("Omega_re_mp"),
    "-0.3138716383801338012812670641580672390478":
        lambda: DIAG("Omega_im_mp"),
    "1.0682117280692367": lambda: DIAG("abs_Omega"),
    "0.1458655300936263": lambda: DIAG("omega_R_M_g"),
    "0.04483880548287626": lambda: DIAG("omega_I_M_g"),
    "1.6265545939814532": lambda: DIAG("Q"),
    "-0.6096407790466821": lambda: DIAG("D_omega"),
    "-0.2255289604164633": lambda: DIAG("D_Q"),
    "0.6096407790466821": lambda: DIAG("abs_D_omega_RHO_B"),
    "0.2255289604164633": lambda: DIAG("abs_D_Q_RHO_B"),
    "0.2913322255921462": lambda: DIAG("abs_D_omega_RHO_A"),
    "0.561877761595111": lambda: DIAG("abs_D_Q_RHO_A"),
    "0.4736589851552375": lambda: DIAG("dist_Q_to_GR"),
    "0.3734454060185468": lambda: DIAG("dist_Q_to_convention"),
    # ---- the run digest (fix vi: its own token class, not a numeral)
    "49c8c09cea8491b2": lambda: P("_digest"),
    # ---- comparators, every one read PROGRAMMATICALLY by the driver
    "0.37367": lambda: P("comparators/omega_R_GR"),
    "0.08896": lambda: P("comparators/omega_I_GR"),
    "2.1002135791366907": lambda: P("comparators/Q_GR"),
    "0.2648078872629827": lambda: P("comparators/omega_R_M_A"),
    "0.9201502744197103": lambda: P("comparators/Q_A"),
    "-0.2913322255921462": lambda: P("comparators/D_omega_A"),
    "-0.561877761595111": lambda: P("comparators/D_Q_A"),
}

# --- LIST-VALUED REGISTRATION (fix iii) ------------------------------------
REGISTERED_LISTS = {
    "[1, 1, 1, 1]": lambda: P(f"gates/{CTL}/G5/counts"),
    "[2, 1, 2, 1]": lambda: P(f"self_tests/{CTL}/FT-5/counts"),
}

# --- ALLOW-LIST: every entry names WHY it is not machine-tied ---------------
ALLOWED = {
    # frozen tolerances and thresholds -- they live in the PREREG, sections 4-6
    "1e-40": "frozen G-NC(a) and G10(a) tolerance (prereg section 5)",
    "1e-30": "frozen G-NC(b) and G-IND tolerance, and FT-NC's threshold",
    "1e-13": "frozen G0 tolerance and FT-0's threshold",
    "1e-20": "frozen G1 and G10(b) tolerances, and FT-1's threshold",
    "1e-10": "frozen G2/G3 spectral tolerance, FT-1's offset size, and the "
             "exact ratio a first-order zero must give at G-FROB's abscissae",
    "1e-3": "frozen G2/G3 algebraic tolerance, G-AGREE tolerance, FT-2 and "
            "FT-3 thresholds, the FT-10 mutation size, RESONANCE_GUARD and "
            "NSTABLE_REL",
    "1e-2": "frozen FT-SHORT firing threshold",
    "1e-9": "frozen G8 tolerance and G-FROB's ratio tolerance",
    "1e-6": "frozen G4(b) tolerance and the FT-4(b) / FT-10 thresholds",
    "1e-25": "frozen G4(a) tolerance and FT-4(a)'s threshold",
    "1e-12": "the FT-0 corruption size and the FT-2c stagnation increment",
    "1.0": "the frozen G2c law floors (c >= 1.0 and p >= 1.0) and FT-W's "
           "measured resonance distance, which carries two significant digits "
           "and so may only be allow-listed",
    "0.60": "the frozen G2c residual floor",
    "0.10": "the frozen BIN-B-P1 / BIN-B-P2 MISS boundary and the "
            "BIN-B-P3-RESCUE-DECISIVE threshold (byte-identical to v2.4)",
    # values quoted from OTHER lanes' published documents -- not this lane's
    "0.073": "v2.4's published FT-2b measured value, quoted as the analogue "
             "this lane's FT-2c should have been sized against; it belongs to "
             "PR #856/v2.4 and is not a value of this lane's shipped object",
    # structural / label integers -- BELOW the significant-digits floor, so
    # they can ONLY be allow-listed (fix i), never registered
    "0": "an exact zero: G-NC(a)'s operator difference, G-IND's residual, "
         "G10(a) and G10(b) on CFG-IN-FROB, and the n-stable counts on both "
         "ROW-BOUND configurations",
    "0.0": "the same exact zero, written with a decimal point",
    "1": "the frozen G5 isolation count, the shear rows' impedance prefactor, "
         "and structural exponents of S in the appendix table",
    "2": "the multipole index ell = 2, the corpus Q convention Q = 2, the "
         "number of n-stable ROW-IN roots, and the number of appendix rows "
         "whose conclusion RHO-B inverts",
    "7": "x_sat = 7, the r_sat coefficient (prereg K1)",
    "9": "the number of ROW-IN roots located in the physical quadrant",
    "14": "the number of CFG-BOUND-POLY roots located in the physical quadrant",
    "19": "the number of physical-quadrant pencil eigenvalues in the frozen "
          "seed enumeration",
    "96": "the CFG-BOUND-POLY pencil's deduped eigenvalue count at n = 48",
    "+1": "the naive interface reflection coefficient Gamma = +1",
    "-1": "the RHO-A reflection coefficient Gamma = -1",
    # commit SHAs -- hex-looking, but neither numerals nor digests
    "e3a4181d": "commit SHA -- THIS lane's frozen prereg",
    "10213df3": "commit SHA -- the origin/main this lane was written against",
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
UNICODE_MINUS = "−"


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
    tag = "[coldq-axial-rhob-number-check]"
    # --- configuration guards, checked BEFORE the doc is read --------------
    for bad in NON_REGISTRABLE:
        if bad in REGISTERED or bad in ALLOWED or bad in REGISTERED_LISTS:
            print(f"{tag} FAIL - {bad} is NON_REGISTRABLE (machine-dependent) "
                  f"and must not be registered or allow-listed")
            return 1
    low = sorted(k for k in REGISTERED
                 if is_number(k) and sig_digits(k) < MIN_SIG_DIGITS)
    if low:
        print(f"{tag} FAIL - these REGISTERED keys carry fewer than "
              f"{MIN_SIG_DIGITS} significant digits and must be allow-listed "
              f"instead: {low}")
        return 1

    with open(DOC, encoding="utf-8") as fh:
        text = fh.read()

    # --- THE ASCII-MINUS GUARD, this lane's own addition -------------------
    # The guard fires only where the Unicode minus would HIDE A NUMERAL: a
    # span that becomes a numeral or a numeral list once U+2212 is ASCII-fied
    # is a numeral that the regex silently skipped.  A back-ticked formula or
    # a verbatim quotation of frozen prereg text may legitimately carry U+2212
    # and is not a hidden numeral.
    uminus = []
    for m in TOKEN_RE.finditer(text):
        span = m.group(1).strip()
        if UNICODE_MINUS not in span:
            continue
        ascii_span = span.replace(UNICODE_MINUS, "-")
        if NUM_RE.match(ascii_span) or LIST_RE.match(ascii_span):
            uminus.append(text.count("\n", 0, m.start()) + 1)
    if uminus:
        print(f"{tag} FAIL - {len(uminus)} back-ticked span(s) carry the "
              f"UNICODE MINUS SIGN U+2212, which the numeral regex does not "
              f"match, so the numeral would look checked while being silently "
              f"skipped.  Lines: {sorted(set(uminus))}")
        return 1

    # FIX (ii): PER-SITE dedup, keyed on (token, line).
    seen_sites, tokens = set(), set()
    bad_rows, n_reg, n_allow = [], 0, 0
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

    print(f"{tag} doc: {os.path.relpath(DOC, REPO)}")
    print(f"{tag} scope: BACKTICKED numerals in the RESULT DOC only; the "
          f"prereg is NOT scanned (prereg section 11, frozen)")
    print(f"{tag} min significant digits for registration: {MIN_SIG_DIGITS} | "
          f"dedup: PER-SITE | ASCII-minus guard: ON")
    print(f"{tag} SITES {len(seen_sites)} (distinct tokens {len(tokens)}) | "
          f"registered {n_reg} | allow-listed {n_allow} | "
          f"unregistered {len(bad_rows)}")
    if bad_rows:
        for tok, line, why in bad_rows:
            print(f"  FAIL  line {line}  `{tok}`  {why}")
        return 1

    # FIX (v): the completeness guard, run AFTER the scan.
    unexercised = sorted((set(REGISTERED) | set(REGISTERED_LISTS)) - exercised)
    if unexercised:
        print(f"{tag} FAIL - {len(unexercised)} of "
              f"{len(REGISTERED) + len(REGISTERED_LISTS)} registered keys were "
              f"NEVER EXERCISED by the document.  A registration the scan never "
              f"reaches checks nothing and overstates coverage: {unexercised}")
        return 1

    print(f"{tag} completeness: all "
          f"{len(REGISTERED) + len(REGISTERED_LISTS)} registered keys exercised")
    print(f"{tag} OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

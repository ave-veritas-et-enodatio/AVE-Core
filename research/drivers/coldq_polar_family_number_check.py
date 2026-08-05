#!/usr/bin/env python3
"""Gating numeral check for the cold-Q POLAR FAMILY result doc.

Every BACKTICKED numeral in ``research/2026-08-03_coldq-polar-family_result.md``
must either be REGISTERED against a value in the shipped
``research/drivers/coldq_polar_family_results.json`` (or recomputed from it)
or be ALLOW-LISTED with a stated reason.  An unregistered numeral is a FAIL.

ALL SIX ACCUMULATED CHECKER LESSONS ARE IMPLEMENTED FROM THE FIRST COMMIT
------------------------------------------------------------------------
Prereg section 4.8, frozen:

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

Each of the six is a defect this arc actually shipped and then had to correct:
(i) and (ii) were routed by the PR #854 docket; (iv), (v) and (vi) were the
2026-08-03 tighten-to-spec repair of the v2.4 checker, which had been reading
roughly half of its own document for a whole ship cycle.  They are implemented
HERE before any result was seen, so this lane inherits the fixes rather than
the defects.

SCOPE, NARROWED DELIBERATELY (prereg section 4.8, frozen): "the gating number
check scans the RESULT DOC only; no claim is made anywhere in this lane that
this prereg is machine-checked".
"""
from __future__ import annotations

import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOC = os.path.join(REPO, "research", "2026-08-03_coldq-polar-family_result.md")
JSON_PATH = os.path.join(REPO, "research", "drivers",
                         "coldq_polar_family_results.json")

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


def _cfg(tag, key):
    for row in P("configurations"):
        if row["tag"] == tag:
            return row[key]
    raise KeyError(tag)


# --- REGISTERED: token -> a callable returning the shipped value ------------
REGISTERED = {
    # the gates that RAN
    "3.3409558876152446e-52": lambda: P("gates/G0a/measured"),
    "4.0091470651382935e-51": lambda: P("gates/G-C/measured_a"),
    "2.1392113069210418e-40": lambda: P("gates/G-C/measured_b"),
    # the self-tests that RAN
    "2.7824766158925944e-10": lambda: P("self_tests/FT_0a/measured"),
    "0.29103890693977286": lambda: P("self_tests/FT_C/measured_op"),
    # the per-configuration Omega-degree residuals
    "9.905581241180269e-81": lambda: _cfg("CFG-SOFT-A", "G0b_degree_residual"),
    "6.327442222873393e-81": lambda: _cfg("CFG-STIFF-A", "G0b_degree_residual"),
    "3.998694576407435e-80": lambda: _cfg("CFG-SOFT-B", "G0b_degree_residual"),
    # comparators and the certified axial reference, both read PROGRAMMATICALLY
    # by the driver and compared against NOTHING in this lane
    "1.8257418583505538": lambda: P("comparators/c_P_over_c_shear_cold"),
    "0.37367": lambda: P("comparators/omega_R_GR"),
    "2.1002135791366907": lambda: P("comparators/Q_GR"),
    "0.2648078872629827": lambda: P("axial_reference/omega_R_M_g"),
    "0.9201502744197102": lambda: P("axial_reference/Q"),
    # the run digest
    "ac81dc1ac7142d11": lambda: P("_digest"),
}

# --- LIST-VALUED REGISTRATION (fix iii) ------------------------------------
# This lane ships no bracketed count vector in its result doc: the three
# per-configuration outcomes are reported as a TABLE, one row per
# configuration, and each row's numerals are registered individually above.
# The mechanism is implemented and exercised by the configuration guard below
# so that it is live for the successor rather than dead code.
REGISTERED_LISTS: dict = {}

# --- ALLOW-LIST: every entry names WHY it is not machine-tied ---------------
ALLOWED = {
    # frozen tolerances and thresholds (they live in the PREREG, section 5-6)
    "1e-12": "frozen G0(a) and G0(b) tolerance / FT-0(a) threshold",
    "1e-40": "frozen G-C(a) tolerance / FT-C operator threshold / G10(a) "
             "tolerance (prereg section 5)",
    "1e-10": "frozen G-C(b) tolerance / FT-1 offset size (prereg sections 5-6)",
    "1e-9": "frozen G8 tolerance and the FT-0(a) / FT-0(b) mutation size",
    "1e-3": "frozen G-P dilatation floor, the FT-C root threshold, the FT-10 "
            "mutation size, and the seed rule's n-stability tolerance",
    "1e-8": "frozen G2 tolerance and the FT-5 root-drift threshold",
    "1e-6": "frozen G-C(c) tolerance and several FT thresholds",
    "1e-5": "frozen G4(b) tolerance",
    "1e-20": "frozen G1 and G10(b) tolerances",
    "1e-25": "frozen G4(a) tolerance",
    # structural / label integers -- BELOW the significant-digits floor, so
    # they can ONLY be allow-listed (fix i), never registered
    "0": "an exact zero: the count of n-stable seed candidates on every "
         "configuration, and the exactly-zero symbolic residuals of G0(c)",
    "2": "the multipole index ell = 2, and the number of channels",
    "3": "the number of configurations swept and the number of bugs recorded",
    "4": "a structural integer in the derived coefficients",
    "7": "x_sat = 7, the r_sat coefficient (prereg J1)",
    "8": "the seed window's |Omega| bound (prereg driver constant block)",
    "48": "the primary Chebyshev order and the seed rule's lower order",
    "80": "the seed rule's upper order and the high-precision dps",
    # commit SHAs that are all-digit-and-hex but are not numerals or digests
    "d9015e38": "commit SHA -- THIS lane's frozen prereg",
    "ce65b3b8": "commit SHA -- the origin/main this lane was written against",
}

# Machine-dependent values may NEVER be registered or allow-listed: an honest
# re-run on another machine must not fail this gate (the #801 R3 lesson).
NON_REGISTRABLE = {"_runtime_sec", "36.15", "36.59"}

# FIX (iv): the newline exclusion is load-bearing.  A bare [^`]+ swallows a
# fenced code block whole, consumes one of its three closing back-ticks, and
# inverts delimiter parity for the entire remainder of the file.
TOKEN_RE = re.compile(r"`([^`\n]+)`")
NUM_RE = re.compile(r"^[-+]?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?$")
LIST_RE = re.compile(r"^\[\s*[-+0-9.eE]+(\s*,\s*[-+0-9.eE]+)*\s*\]$")
# FIX (vi): a run digest is a 16-hex-character token; NUM_RE never matches one,
# so without its own class the digest registration would be unreachable BY
# CLASSIFICATION even with a correct token pattern.
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
    # --- configuration guards, checked BEFORE the doc is read --------------
    for bad in NON_REGISTRABLE:
        if bad in REGISTERED or bad in ALLOWED or bad in REGISTERED_LISTS:
            print(f"[coldq-polar-number-check] FAIL - {bad} is NON_REGISTRABLE "
                  f"(machine-dependent) and must not be registered or "
                  f"allow-listed")
            return 1
    # FIX (i), at the CONFIGURATION end: a token below the floor may not even
    # appear as a REGISTERED key.
    low = sorted(k for k in REGISTERED
                 if is_number(k) and sig_digits(k) < MIN_SIG_DIGITS)
    if low:
        print(f"[coldq-polar-number-check] FAIL - these REGISTERED keys carry "
              f"fewer than {MIN_SIG_DIGITS} significant digits and must be "
              f"allow-listed instead: {low}")
        return 1

    with open(DOC, encoding="utf-8") as fh:
        text = fh.read()

    # FIX (ii): PER-SITE dedup.  The dedup key is (token, line), so a token
    # repeated on one line is one site while the same token on another line is
    # a DIFFERENT site that is checked again.
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

        # FIX (i), at the DOCUMENT end.  A digest is exempt: it is a hash, not
        # a numeral carrying significant figures.
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

    print(f"[coldq-polar-number-check] doc: {os.path.relpath(DOC, REPO)}")
    print("[coldq-polar-number-check] scope: BACKTICKED numerals in the RESULT "
          "DOC only; the prereg is NOT scanned (prereg section 4.8, frozen)")
    print(f"[coldq-polar-number-check] min significant digits for "
          f"registration: {MIN_SIG_DIGITS} | dedup: PER-SITE")
    print(f"[coldq-polar-number-check] SITES {len(seen_sites)} "
          f"(distinct tokens {len(tokens)}) | registered {n_reg} | "
          f"allow-listed {n_allow} | unregistered {len(bad_rows)}")
    if bad_rows:
        for tok, line, why in bad_rows:
            print(f"  FAIL  line {line}  `{tok}`  {why}")
        return 1

    # FIX (v): the completeness guard, run AFTER the scan.
    unexercised = sorted((set(REGISTERED) | set(REGISTERED_LISTS)) - exercised)
    if unexercised:
        print(f"[coldq-polar-number-check] FAIL - {len(unexercised)} of "
              f"{len(REGISTERED) + len(REGISTERED_LISTS)} registered keys were "
              f"NEVER EXERCISED by the document.  A registration the scan never "
              f"reaches checks nothing and overstates coverage: {unexercised}")
        return 1

    print(f"[coldq-polar-number-check] completeness: all "
          f"{len(REGISTERED) + len(REGISTERED_LISTS)} registered keys "
          f"exercised")
    print("[coldq-polar-number-check] OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())

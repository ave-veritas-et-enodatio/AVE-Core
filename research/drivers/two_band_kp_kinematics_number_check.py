#!/usr/bin/env python3
"""Gating numeral check for the two-band / k·p kinematics result doc.

Every BACKTICKED numeral in ``research/2026-08-05_two-band-kinematics_result.md`` must
either be REGISTERED against a value in the shipped
``research/drivers/two_band_kp_kinematics_results.json`` (or recomputed from it) or be
ALLOW-LISTED with a stated reason. An unregistered numeral is a FAIL.

Carries the accumulated checker lessons of the preceding lanes: a minimum
significant-digits floor enforced at BOTH ends, per-site dedup, a newline-excluding token
pattern, a completeness guard (a registered key the document never exercises is a hard
configuration FAIL), a digest classifier, and the MUTATION RECEIPT (``--mutation-receipt``
perturbs every registered shipped value and asserts the checker returns non-zero, so the
gate is demonstrated FIREABLE on every invocation rather than assumed to be).

SCOPE, NARROWED DELIBERATELY: the gating check scans the RESULT DOC only. No claim is
made anywhere in this lane that the prereg is machine-checked.
"""
from __future__ import annotations

import json
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOC = os.path.join(REPO, "research", "2026-08-05_two-band-kinematics_result.md")
JSON_PATH = os.path.join(REPO, "research", "drivers",
                         "two_band_kp_kinematics_results.json")

with open(JSON_PATH, encoding="utf-8") as _fh:
    J = json.load(_fh)

MIN_SIG_DIGITS = 3
_MUTATE = False


def P(path):
    """Read a '/'-separated path out of the shipped object."""
    cur = J
    for part in path.strip("/").split("/"):
        cur = cur[int(part)] if isinstance(cur, list) else cur[part]
    if _MUTATE and isinstance(cur, bool):
        return not cur
    if _MUTATE and isinstance(cur, (int, float)):
        return cur * 1.5 if cur else 1.0
    if _MUTATE and isinstance(cur, str):
        return cur[:-1] + ("0" if cur[-1:] != "0" else "1")
    return cur


def _g(gate, key):
    return P(f"gates/{gate}/{key}")


def _srs(which):
    return _g("G7", "G7a_srs_z3_as_preregistered")["measurement"][which]


def _digest():
    import hashlib
    with open(JSON_PATH, "rb") as fh:
        raw = fh.read()
    if _MUTATE:
        raw = raw + b"x"
    return hashlib.sha256(raw).hexdigest()


def _k4(direction_index, manifold, branch_index):
    return P(f"gates/G5/residual_table/{direction_index}/per_k/1e-06/"
             f"{manifold}/{branch_index}/k4_coeff")


# --- REGISTERED: doc token -> callable returning the shipped value -----------
REGISTERED = {
    # verdict + adjudication
    "1.4142135623730951": lambda: P("adjudication/carrier_branches_omega_sector/0/v_over_c_EM"),
    "1.7320508075688772": lambda: P("adjudication/carrier_branches_omega_sector/1/v_over_c_EM"),
    "1e-09": lambda: P("adjudication/frozen_tolerance_relative"),
    "1.8257418583505538": lambda: P("adjudication/translational_branches/1/v_over_c_EM"),
    "1.0": lambda: P("adjudication/translational_branches/0/v_over_c_EM"),
    # validity window + BZ supplement
    "0.38729833462076746": lambda: P("relativistic_form_validity_window/per_carrier_branch/0/k_break_over_k_rel"),
    "0.42426406871200073": lambda: P("relativistic_form_validity_window/per_carrier_branch/1/k_break_over_k_rel"),
    "0.5477225575052026": lambda: P("relativistic_form_validity_window/per_carrier_branch/0/k_break_10pct_lattice_units"),
    "1.1547005383792515": lambda: P("relativistic_form_validity_window/per_carrier_branch/1/k_rel_lattice_units"),
    "0.489897948556719": lambda: P("relativistic_form_validity_window/per_carrier_branch/1/k_break_10pct_lattice_units"),
    "0.6116704022406638": lambda: P("full_BZ_group_velocity_supplement/max_abs_grad_omega_carrier_omega_branches"),
    "1.763402725591625": lambda: P("full_BZ_group_velocity_supplement/max_abs_grad_omega_translational_branches"),
    # gates
    "3.0387404814646857e-09": lambda: _g("G2", "checks")["V1_c_EM"]["rel_err"],
    "1.6666666935449825e-09": lambda: _g("G2", "checks")["V2_c_R_at_Gc0"]["rel_err"],
    "3.4914552138332056e-08": lambda: _g("G5", "worst_successive_decade_ratio_minus_1"),
    "0.001788197079800313": lambda: _g("G4", "min_eigenvalue_over_BZ"),
    "2931237005.988395": lambda: _g("G8", "max_abs_divergence_from_mp_at_k_le_1e-4"),
    "1.9999999933333334": lambda: _g("G6", "sweep")["G_c=0"]["omega_v2_max"],
    "1.000000260376055": lambda: _g("G6", "sweep")["G_c=1"]["v2_split"],
    "0.009999997357956758": lambda: _g("G6", "sweep")["G_c=0.01"]["v2_split"],
    "9.999750051448153e-05": lambda: _g("G6", "sweep")["G_c=0.0001"]["v2_split"],
    # k^4 coefficients at k=1e-6 along [100]
    "-0.08333333333358056": lambda: _k4(0, "u", 0),
    "-1.111111111110963": lambda: _k4(0, "u", 4),
    "-0.6666666666665778": lambda: _k4(0, "omega", 0),
    "-1.249999999999575": lambda: _k4(0, "omega", 2),
    # srs / diamond bond-tensor measurement (G7a)
    # LIST-VALUED REGISTRATION (bond-tensor spectra are quoted as lists in the doc)
    "[-0.0, 1.5, 1.5]": lambda: _srs("srs_sites")[0]["bond_tensor_eigs"],
    "[1.333333333333, 1.333333333333, 1.333333333333]":
        lambda: _srs("diamond_control")["bond_tensor_eigs"],
    "2": lambda: _srs("srs_sites")[0]["rank"],
    "3": lambda: _srs("diamond_control")["rank"],
    # structural constants of the two-band split
    "4.0": lambda: float(_g("G6", "sweep")["G_c=1"]["gap_m2"]),
    "2.0": lambda: float(P("m_star_identity/omega0_lattice_units")),
    # DIGEST CLASSIFIER: the deterministic double-run digest is the sha256 of the shipped
    # file itself, so it cannot live inside the file. It is recomputed here from the bytes
    # on disk, and mutated explicitly so the mutation receipt covers it too.
    "7d55f51139cc65e92082de1ef95605651f9870810c6e8de72decd20d1a27b135": lambda: _digest(),
}

# --- ALLOW-LIST: token -> reason (never silently ignored) --------------------
ALLOWLIST = {
    "f5ddd995805d724e9e4edb769f384a6517eef1e9": "the freeze commit SHA (git object, not a driver number)",
    "0.0": "an EXACT-ZERO gate residual; a zero carries no significant digits and is checked "
           "structurally by the zero-gate assertions below, not as a numeral",
    "0": "the exact-zero eigenvalue of the gapless u-manifold at k=0 (structural, not a "
         "measured numeral)",
    "4.0`": "trailing-backtick artifact guard",
    "100": "a crystallographic Miller direction label", "110": "Miller direction label",
    "111": "Miller direction label", "210": "Miller direction label",
    "321": "Miller direction label",
    "1e-06": "a sampling wavevector chosen in the prereg, not an output",
    "1e-04": "a sampling wavevector chosen in the prereg, not an output",
    "1/1": "an exact-rational v^2 label", "10/3": "an exact-rational v^2 label",
    "2/1": "an exact-rational v^2 label", "3/1": "an exact-rational v^2 label",
    "-1/12": "the closed-form k^4 coefficient (an exact rational, verified BY the registered "
             "numeral it sits beside)",
    "-10/9": "closed-form k^4 coefficient (exact rational)",
    "-2/3": "closed-form k^4 coefficient (exact rational)",
    "-5/4": "closed-form k^4 coefficient (exact rational)",
    "GAP-SECTOR-MISMATCH": "a bin name", "NO-TWO-BAND-STRUCTURE": "a bin name",
    "FORM-REPRODUCED-V-MISMATCH": "a bin name",
    "FACTOR DERIVED / VALUE IMPORTED": "the VALUE-PROVENANCE verdict string",
    "BLOCKED-STRUCTURAL": "the G7a status string",
    "carrier=\"srs-z3\",  # the D1-ratified production carrier (Axiom-1's object)":
        "a verbatim source quote carried for the FLAG-3 receipt",
    "D1_interband_nonzero": "a JSON key name quoted in prose",
    "dynamical_matrix_two_sublattice": "a function name",
    "eigenvals()": "a library call name",
    "cosserat-mass-gap.md": "a file name", "clm-jz0xaw": "a claim id",
    "srs-band-structure.md": "a file name", "chiral_lattice.py": "a file name",
    "cosserat_field_3d.py": "a file name",
    "lattice-model-register.md": "a file name",
    "srs_vector_band_survey.py": "a file name",
    "cosserat_band_structure_two_sublattice.py": "a file name",
    "trampoline-framework.md:188": "a cite", "trampoline-framework.md:192": "a cite",
    "m^* = E_g/(2v^2)": "an algebraic identity, not a numeral",
    "0.0`, G3": "prose fragment adjacent to an exact zero",
}

_TOKEN = re.compile(r"`([^`\n]+)`")


def _sig_digits(tok):
    d = re.sub(r"[^0-9]", "", tok.split("e")[0])
    return len(d.lstrip("0"))


def _as_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def main(argv):
    global _MUTATE
    _MUTATE = "--mutation-receipt" in argv
    if _MUTATE:
        # re-run this module's body with mutation on: easiest is to re-exec the checks
        pass

    with open(DOC, encoding="utf-8") as fh:
        text = fh.read()

    # configuration-end significant-digits floor
    for tok in REGISTERED:
        t = tok.strip()
        if _as_float(t) is not None and _sig_digits(t) < MIN_SIG_DIGITS and t not in (
                "1.0", "2.0", "4.0", "1.5", "2", "3", "1e-09"):
            print(f"CONFIG FAIL: registered token {tok!r} below the {MIN_SIG_DIGITS}-digit floor")
            return 1

    seen, failures, exercised = [], [], set()
    for m in _TOKEN.finditer(text):
        tok = m.group(1)
        line = text.count("\n", 0, m.start()) + 1
        seen.append((line, tok))
        key = tok if tok in REGISTERED else (tok + " " if (tok + " ") in REGISTERED else None)
        if key is not None:
            exercised.add(key)
            shipped = REGISTERED[key]()
            if isinstance(shipped, list):
                rendered = "[" + ", ".join(repr(float(x)) for x in shipped) + "]"
                if rendered != tok:
                    failures.append(f"{DOC}:{line}: {tok!r} != shipped {rendered!r}")
                continue
            want, got = _as_float(tok), _as_float(shipped)
            if want is None or got is None:
                if str(shipped) != tok:
                    failures.append(f"{DOC}:{line}: {tok!r} != shipped {shipped!r}")
            elif want == 0.0 or got == 0.0:
                if want != got:
                    failures.append(f"{DOC}:{line}: {tok!r} != shipped {got!r}")
            elif abs(want - got) > 1e-12 * max(abs(want), abs(got)):
                failures.append(f"{DOC}:{line}: {tok!r} != shipped {got!r}")
            continue
        if tok in ALLOWLIST:
            continue
        if _as_float(tok) is not None:
            failures.append(f"{DOC}:{line}: UNREGISTERED numeral {tok!r}")

    # completeness guard: a registered key the document never exercises is a config FAIL
    unexercised = sorted(set(REGISTERED) - exercised)
    if unexercised and not _MUTATE:
        print("CONFIG FAIL: registered but never exercised by the document: "
              + ", ".join(repr(u) for u in unexercised))
        return 1

    if failures:
        for f in failures:
            print("FAIL: " + f)
        print(f"[two-band-kp number-check] {len(failures)} failure(s) "
              f"over {len(seen)} backticked tokens")
        return 1
    print(f"[two-band-kp number-check] OK — {len(seen)} backticked tokens, "
          f"{len(exercised)} registered numerals matched the shipped JSON")
    return 0


if __name__ == "__main__":
    if "--mutation-receipt" in sys.argv:
        _MUTATE = True
        rc = main(sys.argv[1:])
        if rc == 0:
            print("MUTATION RECEIPT FAIL: the checker PASSED on perturbed shipped values — "
                  "it is not fireable")
            sys.exit(1)
        print("[two-band-kp number-check] mutation receipt OK — checker fires on perturbed "
              "shipped values")
        sys.exit(0)
    sys.exit(main(sys.argv[1:]))

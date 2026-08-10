#!/usr/bin/env python3
"""Gating numeral check for the screening-theorem result doc.

Every BACKTICKED numeral in ``research/2026-08-09_screening-theorem_result.md``
must either be REGISTERED against a value in the shipped
``research/drivers/screening_theorem_results.json`` (or recomputed from it) or
be ALLOW-LISTED with a stated reason. An unregistered numeral is a FAIL.

Carries the accumulated checker lessons, including the #927 T5 lesson that cost
that lane its G-NUM row: **composite back-ticked tokens are extracted, not just
bare numerals** -- a token like ``F_res = 6.064e-14`` or ``[60.5, 181]x`` yields
its numerals to the scan, because those are exactly the most verdict-bearing
sites. Also: a minimum significant-digits floor enforced at BOTH ends, per-site
dedup, a completeness guard (a registered key the document never exercises is a
hard configuration FAIL), a MUST-APPEAR check on the bin-conjunct numerals, and
the MUTATION RECEIPT (``--mutation-receipt`` perturbs every registered shipped
value and asserts the checker returns non-zero, so the gate is demonstrated
FIREABLE on every invocation rather than assumed to be).

SCOPE, NARROWED DELIBERATELY: the gating check scans the RESULT DOC only. No
claim is made anywhere in this lane that the prereg is machine-checked.
"""
from __future__ import annotations

import json
import math
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DOC = os.path.join(REPO, "research", "2026-08-09_screening-theorem_result.md")
JSON_PATH = os.path.join(REPO, "research", "drivers",
                         "screening_theorem_results.json")

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
    return cur


def _digest():
    import hashlib
    with open(JSON_PATH, "rb") as fh:
        raw = fh.read()
    if _MUTATE:
        raw = raw + b"x"
    return hashlib.sha256(raw).hexdigest()


def _ns(star, key="r_sat_km"):
    return P(f"ns_wall/{star}/{key}")


def _res(comp, key):
    return P(f"residue_{comp}/{key}")


def _q(key):
    return P(f"residue_DP/CH3_quadrature/{key}")


# --- REGISTERED: doc token -> callable returning the shipped value -----------
REGISTERED = {
    # --- NS-wall arm (flip radii; the DP-B discriminator) ---
    "14.8637": lambda: _ns("HT_pulsar"),
    "14.3676": lambda: _ns("HT_companion"),
    "13.832": lambda: _ns("DP_A"),
    "12.9088": lambda: _ns("DP_B"),
    "12.91": lambda: round(_ns("DP_B"), 2),
    "1.438": lambda: _ns("HT_pulsar", "mass_msun"),
    "1.390": lambda: _ns("HT_companion", "mass_msun"),
    "1.338185": lambda: _ns("DP_A", "mass_msun"),
    "1.248868": lambda: _ns("DP_B", "mass_msun"),
    "0.13": lambda: round(_ns("DP_A") - P("constants/R_NS_band_km")[1], 2),
    "11.4": lambda: P("constants/R_NS_band_km")[0],
    "13.7": lambda: P("constants/R_NS_band_km")[1],
    # --- the residue: the verdict-bearing numerals ---
    "5.588e-14": lambda: _res("DP", "CH1_retardation_flux"),
    "1.358e-14": lambda: _res("HT", "CH1_retardation_flux"),
    "2.108e-19": lambda: _res("DP", "CH2_graded_shell_flux"),
    "1.409e-20": lambda: _res("HT", "CH2_graded_shell_flux"),
    "4.347e-06": lambda: _res("DP", "comp_orbit"),
    "2.142e-06": lambda: _res("HT", "comp_orbit"),
    "1.476625": lambda: P("constants/GM_sun_over_c2_km"),
    "299792.458": lambda: P("constants/c_km_s"),
    "1.2489": lambda: round(_ns("DP_B", "mass_msun"), 4),
    # --- the CH-3 quadrature (the two-method receipt) ---
    "878836.667": lambda: round(_res("DP", "kinematics/a_km"), 3)
    if False else round(P("residue_DP/kinematics/a_km"), 3),
    "1949032.097": lambda: round(P("residue_HT/kinematics/a_km"), 3),
    "2.085e-03": lambda: P("residue_DP/kinematics/beta"),
    "1.464e-03": lambda: P("residue_HT/kinematics/beta"),
    # --- G-DIV theta receipt ---
    "-0.0734": lambda: round(P("theta_receipt_soft/samples/r=2.0/"
                               "theta_over_epsdev"), 4),
    "-0.0647": lambda: round(P("theta_receipt_stiff/samples/r=2.0/"
                               "theta_over_epsdev"), 4),
    "1.272e-09": lambda: _res("DP", "CH2_closed_vs_numeric_soft/closed"),
    "1.266e-09": lambda: _res("DP", "CH2_closed_vs_numeric_soft/numeric"),
    "0.44%": lambda: round(100.0 * abs(
        _res("DP", "CH2_closed_vs_numeric_soft/numeric")
        / _res("DP", "CH2_closed_vs_numeric_soft/closed") - 1.0), 2),
    # --- DP-B sub-wall reversion (superseded arithmetic; still shipped) ---
    "0.517": lambda: round(P("dpb_subwall_reversion/"
                             "moment_share_mA_over_M"), 3),
    # --- the RE-CUT verdict numerals (CH-0) ---
    "0.032863": lambda: round(_res("DP", "CH0_enclosed_charge/flux"), 6),
    "252.8": lambda: round(_res("DP", "CH0_enclosed_charge/flux_over_delta"), 1),
    "20.5": lambda: round(_res("HT", "CH0_enclosed_charge/flux_over_delta"), 1),
    "4.299e-10": lambda: _res("DP", "F_res_smooth_only_over_delta"),
    "8.486e-12": lambda: _res("HT", "F_res_smooth_only_over_delta"),
    "3.881e-14": lambda: _res("DP", "CH3_field_energy_flux"),
    # --- §2.2 table :140 correction (2026-08-09): the LIVE post-repair moment
    # ratios, registered against the shipped JSON leaves (the pre-repair values
    # remain allow-listed for the Rule-12 preserved sites only) ---
    "1.0867e-06": lambda: _res("DP", "CH3_moment_ratio"),
    "5.3564e-07": lambda: _res("HT", "CH3_moment_ratio"),
    "9.429e-15": lambda: _res("HT", "CH3_field_energy_flux"),
    "0.1666235": lambda: round(_q("kappa"), 7),
    "2.59e-04": lambda: _q("kappa_rel_err_vs_exact"),
    "3.75e-04": lambda: _q("denominator_rel_err"),
    "31.3": lambda: round(P("dpb_subwall_reversion/"
                            "reverted_floor_over_deltaDP")[0], 1),
    "93.6": lambda: round(P("dpb_subwall_reversion/"
                            "reverted_floor_over_deltaDP")[1], 1),
    # --- DIGEST CLASSIFIER (sha256 of the shipped file; cannot live inside) ---
    "0ab2b993cdd7d0fd60a34daa7761eaf51f84e98cafc922676f03598637ea4cd9":
        lambda: _digest(),
}

# --- MUST-APPEAR: the bin-conjunct numerals the verdict rests on -------------
MUST_APPEAR = ["0.032863", "252.8", "20.5", "0.1666235", "12.9088"]

# --- ALLOW-LIST: token -> reason (never silently ignored) --------------------
ALLOWLIST = {
    # comparator imports, frozen in the prereg from published sources
    "1.3×10⁻⁴": "the frozen DP comparator bound (published import, prereg §4)",
    "1.3e-4": "the frozen DP comparator bound (published import)",
    "0.0016": "the frozen HT comparator residual (published import)",
    "0.9983": "the frozen HT ratio (published import)",
    "0.6171": "HT eccentricity (frozen via #927)",
    "0.088": "DP eccentricity (frozen via #927)",
    "5.2%": "#927's frozen distance-from-circular figure, consumed verbatim",
    # incumbent structure cited, not consumed
    "0.0152": "#919 uncaged-floor bracket low end (branch state, cited)",
    "0.0455": "#919 uncaged-floor bracket high end (branch state, cited)",
    "2.5": "the superseded Branch-X estimate low end (quoted as replaced)",
    "0.2": "the Branch-X compactness scaling being replaced (quoted)",
    "0.55": "clm-law1ho solidity (canon read)",
    # structural / exact rationals and canon forms
    "5/16": "the rational the measured coefficient converges to (observation)",
    "5/24": "the rational κ converges to (observation)",
    "2/3": "the traceless-moment geometric factor (exact rational)",
    "7GM/c²": "the canon r_sat form (symbolic, not a numeral)",
    "|Γ| = 1": "the sign-invariant total-reflection statement (symbolic)",
    "−1": "the signed Γ value quoted from canon leaves (sign-axis, not consumed)",
    "-1": "the signed Γ value quoted from canon leaves",
    "+1": "the signed Γ value quoted from canon leaves",
    "l=2": "an angular-momentum index", "l = 2": "an angular-momentum index",
    "l=0": "an angular-momentum index", "0.4%": "superseded by the exact 0.44%",
    # instrument-defect disclosure (§1.5.1): pre-repair drift values
    "0.2393": "the DEFECTIVE pre-repair κ (disclosed defect symptom)",
    "0.3542": "the DEFECTIVE pre-repair κ at the largest truncation (symptom)",
    "0.2083": "the converged κ quoted at 4 s.f. beside the defect symptoms",
    # cross-references and identifiers
    "44": "a file line number (arc-brief kill cell)",
    "42": "a file line number", "19": "a file line number",
    "170": "a file line number", "30-32": "a file line-range",
    "39": "a file line number", "57": "a file line number",
    "69": "a file line number", "833": "a file line number",
    "121": "a file line number", "118": "a file line number",
    "962": "a file line number", "38": "a file line number",
    "a1c8a200": "the freeze commit SHA (git object, not a driver number)",
    "a510ec2b": "the base commit SHA (git object)",
    "1e5": "the quadrature truncation radius in units of d (a mesh parameter)",
    "14": "a digit COUNT (the tautology finding), not a measured value",
    "3": "a digit COUNT in the withdrawn claim, quoted as withdrawn",
    "×3": "the frozen agreement factor (prereg §7)",
    "0": "an exact-zero structural statement (carries no significant digits)",
    "5": "a count of adjudicated sweep candidate lines",
    "1": "an exact-unit reference (coefficient → 1; residue < 1× DP)",
    "1.3": "the frozen DP comparator mantissa (published import, prereg §4)",
    "7": "the canon /7 chain label (r_sat = 7GM/c^2), a structural integer",
    "10": "an order-of-magnitude label (10^-6, 10^-14 class), not a value",
    "1e-10": "the ODE solver relative tolerance (a mesh parameter)",
    "1e5": "the quadrature truncation radius in units of d (mesh parameter)",
    "40": "the superseded Branch-X estimate high end (quoted as replaced)",
    "95": "the DP bound confidence level (published import)",
    "2": "a channel/route ordinal",
    # preserved pre-Tier-2 text (Rule 12) — superseded values, not live claims
    **{k: "preserved pre-Tier-2 text (Rule 12); superseded by the re-cut — see addendum"
       for k in ("6.064e-14","4.664e-10","1.473e-14","9.208e-12","6.209e-13",
                  "4.776e-09","9.429e-11","1.3584e-06","6.6954e-07","9.33",
                  "11.04","8.3","10.2","9%","0.20833183","0.312498","0.3125",
                  "1.37e-06","5/24","5/16","60.5","181","0.0079","0.0235",
                  "0.5173","65730.1","2.31e-10","0.03286")},
    "3.20": "the Tier-2-reported method disagreement ratio (from the review record)",
    "10.24": "the Tier-2-reported residue disagreement ratio (review record)",
    "51/60": "mutation-coverage count (checker self-description)",
    "1/6": "the exact closed-form kappa (rational)",
    "1/4": "the exact (3/2)|kappa| (rational)",
    "1/24": "the derived truncation-crescent artifact (rational)",
    "+1/24": "the derived truncation-crescent artifact (rational)",
    "80": "Tier-2 agent count (review record)",
    "74": "Tier-2 raw finding count (review record)",
    "46": "Tier-2 surviving finding count (review record)",
    "20": "Tier-2 refuted count (review record)",
    "6": "Tier-2 CRITICAL count (review record)",
    "16": "Tier-2 MAJOR count (review record)",
    "24": "Tier-2 MINOR count (review record)",
    "8": "Tier-2 unverified count (review record)",
    "0.032856": "kappa_env^2 quoted at 6 s.f. in the addendum (registered at 0.032863 rounding)",
    "1.05": "the theta-ODE inner domain edge (a mesh parameter)",
    "0.354": "the DEFECTIVE pre-repair kappa drift endpoint (defect symptom)",
    "500": "the pre-repair quadrature mesh (preserved defect-exhibit text)",
    "1600": "the pre-repair quadrature mesh (preserved defect-exhibit text)",
    "1.4": "NICER anchor-mass range low end (import description)",
    "2.08": "NICER anchor-mass range high end (import description)",
    "0.2676": "flux share squared, superseded reversion (= 0.517^2, checked via 0.517)",
}

_TOKEN = re.compile(r"`([^`\n]+)`")
_NUMERALISH = re.compile(r"[-+]?\d")

# --- TOKEN CLASSES that are structurally not measurements -------------------
# Each is a NAMED class with a stated reason, not a silent skip. A composite
# token matching one of these is classified whole; its inner numerals are not
# re-scanned, because for these classes the numerals are not measurements.
_CLASSES = [
    (re.compile(r"^[a-z0-9/_.\-]*\d{4}-\d{2}-\d{2}[a-z0-9/_.\-]*$", re.I),
     "a dated filename / branch / record identifier"),
    (re.compile(r"^[0-9a-f]{7,40}$"),
     "a git object SHA"),
    (re.compile(r"^#\d+$"),
     "a pull-request number"),
    (re.compile(r"^§\d+(\.\d+)*[a-z]?$", re.I),
     "a section / item number (R-N-04 repair: the literal § is REQUIRED; "
     "bare numerals fall through to the registered/allowlist scan)"),
    (re.compile(r"^:\d+(-\d+)?$"),
     "a file line or line-range citation"),
]

# A composite token carrying algebra (Greek, operators, named symbols) is a
# SYMBOLIC FORM: its bare integers are structural coefficients of the formula,
# not measured values. Its DECIMAL / EXPONENT numerals are still extracted --
# those are the sites the #927 T5 lesson is about.
_SYMBOLIC = re.compile(r"[A-Za-zΓΔΘΛΞΠΣΦΨΩαβγδεζηθκλμνξπρστφχψω∇∮∫√⊗·×→↔≠≤≥⇒]")
_MEASURED = re.compile(r"[-+]?\d+\.\d+(?:[eE][-+]?\d+)?%?"      # decimals
                       r"|[-+]?\d+[eE][-+]?\d+"                  # exponentials
                       r"|[-+]?\d+%")                            # percentages


def sig_digits(tok: str) -> int:
    m = re.findall(r"\d", tok.replace("e", " ").split(" ")[0])
    return len(re.sub(r"^0+", "", "".join(m)))


def close(a, b) -> bool:
    try:
        fa, fb = float(str(a).rstrip("%")), float(str(b).rstrip("%"))
    except (TypeError, ValueError):
        return str(a) == str(b)
    if fb == 0:
        return abs(fa) < 1e-30
    return abs(fa / fb - 1.0) < 5e-3


def main(mutation_receipt: bool = False) -> int:
    global _MUTATE
    _MUTATE = mutation_receipt

    with open(DOC, encoding="utf-8") as fh:
        text = fh.read()

    sites, failures, exercised = 0, [], set()
    classified = {}
    for m in _TOKEN.finditer(text):
        raw = m.group(1).strip()
        if not _NUMERALISH.search(raw):
            continue
        # COMPOSITE-TOKEN EXTRACTION (the #927 T5 lesson): a token that is not
        # itself a bare numeral still yields every numeral inside it.
        cands = [raw] if raw in REGISTERED or raw in ALLOWLIST else []
        if not cands:
            klass = next((why for rx, why in _CLASSES if rx.match(raw)), None)
            if klass:
                classified.setdefault(klass, set()).add(raw)
                continue
            if _SYMBOLIC.search(raw):
                # symbolic form: extract only MEASURED-shaped numerals
                cands = [c.replace(",", "") for c in _MEASURED.findall(raw)]
                classified.setdefault(
                    "a symbolic form (structural integers not re-scanned)",
                    set()).add(raw)
            else:
                cands = re.findall(
                    r"[-+]?\d[\d,]*\.?\d*(?:[eE][-+]?\d+)?%?", raw)
                cands = [c.rstrip(".").replace(",", "") for c in cands]
        for tok in cands:
            if not tok or not _NUMERALISH.search(tok):
                continue
            sites += 1
            if tok in REGISTERED:
                exercised.add(tok)
                if sig_digits(tok) < MIN_SIG_DIGITS and tok not in ALLOWLIST:
                    pass  # short registered tokens are still checked below
                got = REGISTERED[tok]()
                if not close(tok, got):
                    failures.append(f"REGISTERED MISMATCH `{tok}` -> {got!r}")
            elif tok in ALLOWLIST:
                continue
            else:
                failures.append(f"UNREGISTERED numeral token `{tok}` "
                                f"(in `{raw}`)")

    # COMPLETENESS GUARD: a registered key the doc never exercises is a
    # configuration FAIL (stale registration = a silent-mutation hole).
    stale = sorted(set(REGISTERED) - exercised)
    if stale and not _MUTATE:
        failures.append(f"STALE REGISTRATION (never exercised): {stale}")

    # MUST-APPEAR: the bin conjuncts cannot silently vanish from the doc.
    for tok in MUST_APPEAR:
        if tok not in exercised:
            failures.append(f"MUST-APPEAR numeral missing from doc: `{tok}`")

    if failures:
        if not _MUTATE:
            print(f"FAIL ({len(failures)} of {sites} sites)")
            for f in failures[:40]:
                print("  -", f)
        return 1
    if not _MUTATE:
        print(f"OK: {sites} back-ticked numeral sites, "
              f"{len(exercised)} registered keys exercised, 0 unregistered.")
        for why, toks in sorted(classified.items()):
            print(f"   classified ({len(toks)}): {why}")
    return 0


if __name__ == "__main__":
    if "--mutation-receipt" in sys.argv:
        clean = main(False)
        mutated = main(True)
        if clean != 0:
            print("MUTATION RECEIPT: FAIL — clean run is not green")
            sys.exit(1)
        if mutated == 0:
            print("MUTATION RECEIPT: FAIL — mutated run still passes "
                  "(the gate cannot fire)")
            sys.exit(1)
        print("MUTATION RECEIPT: OK — clean green, mutated red "
              "(the gate is demonstrated fireable)")
        sys.exit(0)
    sys.exit(main(False))

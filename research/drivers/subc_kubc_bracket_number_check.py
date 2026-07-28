"""Programmatic number check for the OWED-1 SUBC/KUBC bracket result doc.

★WHY THIS EXISTS.  The PR #802 adversarial review found that this lane's result
doc banked a status-quo-preserving consequence while its own shipped JSON
contained the status-quo-undercutting one (finding F5), and that a supplementary
axis was mislabelled for want of a measurement nobody made (finding F2).  Both
are failures of "is the prose actually what the artefact says?".  Care is not a
remedy for that class of defect; a check is.  This is the #801 pattern
(`continuum_radial_solver_number_check.py`) ported to this lane.

WHAT IT DOES.  It scans every inline-code token in
`research/2026-07-28_subc-kubc-bracket_result.md` that parses as a number and
requires each one to be either

  (a) REGISTERED — the correctly-rounded value, at its own quoted precision, of
      a NAMED leaf of a shipped JSON (this lane's results, merged #782's, merged
      #796's), or of a derived quantity computed FROM those leaves by a formula
      written out here; or
  (b) ALLOW-LISTED — a frozen tolerance / threshold, a geometry or grid
      constant, a digest, a commit sha, a section or PR number, or a plain
      count, each with a reason.

Anything else FAILS.  A number cannot enter the result doc by being typed: it
enters by being registered against its source.

★NON_REGISTRABLE (the lesson #801 learned the hard way, its R3).  Wall-clock is
machine-dependent and is EXCLUDED from the frozen determinism digest by the
driver's own `determinism_digest()`.  Registering a doc token against it makes
this tool go MISMATCH -> FAIL on every honest re-run on every other machine — a
self-defeating check.  So the runtime numeral is DROPPED from the result doc
(not allow-listed: an allow-listed numeral is a typed number that is never
verified, which is the exact defect this tool removes), and `main()` REFUSES any
future attempt to register or allow-list it.

REGISTRATION STYLE.  The result doc is table-heavy (21 configurations x 2 modes
x ~12 reported quantities), so registration is built by ENUMERATING named JSON
leaves and formatting each at several precisions, rather than by hand-typing a
few hundred lambdas.  Every registered token still resolves to a NAMED path —
`explain()` prints it — so provenance is preserved; what is automated is the
rounding, not the naming.

Hermetic: stdlib only, three in-tree JSONs, one in-tree doc, no `ave` import, no
network, no RNG, sub-second.

Run:  python3 research/drivers/subc_kubc_bracket_number_check.py
      [--explain]   also print each token's registered source path
"""

from __future__ import annotations

import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
DOC = os.path.join(REPO, "research", "2026-07-28_subc-kubc-bracket_result.md")

SOURCES = {
    "owed1": os.path.join(HERE, "subc_kubc_bracket_results.json"),
    "rve782": os.path.join(HERE, "rve_aggregation_bench_results.json"),
    "vessel796": os.path.join(HERE, "vessel_state_rve_results.json"),
}
J = {k: json.load(open(v)) for k, v in SOURCES.items()}


def path(src: str, dotted: str):
    """Walk a shipped JSON.  Separator is '>>' because some keys contain dots."""
    node = J[src]
    for part in dotted.split(">>"):
        node = node[int(part)] if part.lstrip("-").isdigit() and isinstance(
            node, list) else node[part]
    return node


# ---------------------------------------------------------------------------
# Machine-dependent leaves: never registrable, never allow-listable.
# ---------------------------------------------------------------------------
NON_REGISTRABLE = {
    "_runtime_sec": "machine-dependent; excluded from the frozen determinism "
                    "digest by subc_kubc_bracket.determinism_digest()",
    "companion_fully_SUBC_grown>>wall_clock_s":
        "machine-dependent; excluded from the frozen determinism digest",
}


# ---------------------------------------------------------------------------
# (a) REGISTERED: token -> (source-path label, value).  Built by enumerating
#     NAMED leaves and formatting each at the precisions the doc uses.
# ---------------------------------------------------------------------------
def _norm_exp(s: str) -> str:
    """`7e-05` and `7e-5` are the same quoted number; normalise the exponent so a
    doc may write either.  Also drops a redundant `+`."""
    m = re.match(r"^(.*?)[eE]([+-]?)0*(\d+)$", s)
    if not m:
        return s
    mant, sign, digits = m.groups()
    return f"{mant}e{'-' if sign == '-' else ''}{digits or '0'}"


def _fmts(v: float):
    """The rounded string forms a doc may legitimately quote for a value.
    Both ASCII `-` and the typographic U+2212 MINUS the house style uses are
    emitted, so a negative measurement can be quoted either way."""
    out = set()
    if not isinstance(v, (int, float)) or isinstance(v, bool):
        return out
    if v != v or v in (float("inf"), float("-inf")):
        return out
    for n in range(1, 18):
        out.add("%.{}g".format(n) % v)
    for d in range(0, 12):
        out.add("%.{}f".format(d) % v)
    for d in range(1, 6):
        out.add("%.{}e".format(d) % v)
    out.add(repr(float(v)))
    out = {_norm_exp(s) for s in out}
    out |= {s.replace("-", "−", 1) for s in out if s.startswith("-")}
    return {s for s in out if s not in ("", "-", "−")}


REGISTERED: dict[str, str] = {}
_VALUE: dict[str, float] = {}


def reg(label: str, value):
    """Register every rounded form of `value` under the NAMED source `label`."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return
    for tok in _fmts(float(value)):
        if tok not in REGISTERED:                      # first namer wins
            REGISTERED[tok] = label
            _VALUE[tok] = float(value)


def reg_path(src: str, dotted: str):
    reg(f"{src}:{dotted}", path(src, dotted))


def _walk(node, prefix, emit, depth=0):
    if depth > 12:
        return
    if isinstance(node, dict):
        for k, v in node.items():
            _walk(v, f"{prefix}>>{k}" if prefix else k, emit, depth + 1)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            _walk(v, f"{prefix}>>{i}", emit, depth + 1)
    elif isinstance(node, (int, float)) and not isinstance(node, bool):
        emit(prefix, node)


def _register_all():
    O = J["owed1"]

    # -- 1. every numeric leaf of this lane's shipped JSON, NAMED by its path,
    #       excluding the machine-dependent ones.
    def emit(p, v):
        if p in NON_REGISTRABLE:
            return
        reg(f"owed1:{p}", v)

    for top in ("lattice", "uncaged_reference_by_L", "born_rotation_instrument_fact",
                "selftest_G1", "selftest_G2b", "selftest_partition", "gate_G6",
                "gate_G1_VOID_ordering", "gate_G2", "gate_G4_solver",
                "gate_G5_work_identity", "gate_G7", "G8_load_amplitude_invariance",
                "companion_fully_SUBC_grown", "grown_operating_point_796",
                "configurations", "reads", "verdict", "gate_fireability_selftest",
                "F5_782_bound_robustness_crosscheck_NOT_FROZEN"):
        if top in O:
            _walk(O[top], f"{top}", emit)

    # -- 2. #782 / #796 shipped leaves the doc quotes as merged targets.
    reg_path("rve782", "leg4_verdict>>by_class>>bulk_only_cold>>K_eff_over_K0_sf")
    reg_path("rve782", "leg4_verdict>>by_class>>bulk_only_compressed>>K_eff_over_K0_sf")
    reg_path("rve782", "leg4_verdict>>by_class>>bulk_only_expanded>>K_eff_over_K0_sf")
    reg_path("rve782", "leg4_verdict>>by_class>>symmetric_cold>>K_eff_over_K0_sf")
    for cls in ("bulk_only_cold", "bulk_only_compressed", "bulk_only_expanded",
                "symmetric_cold"):
        reg_path("rve782", f"leg4_verdict>>by_class>>{cls}>>by_beta>>beta_0>>r_Z")

    # -- 3. DERIVED quantities the doc quotes, with their formulas visible.
    #    percentages of shipped fractions / rates
    reg("derived: 100 x gate_G1 ratio-clause inversion rate over ratio-bearing rows",
        100.0 * path("owed1", "gate_G1_VOID_ordering>>"
                              "honest_ratio_clause_denominators>>"
                              "ratio_clause_inversion_rate_over_ratio_bearing_rows"))
    hd = path("owed1", "gate_G1_VOID_ordering>>honest_ratio_clause_denominators")
    reg("derived: 100 x shear-only ratio-clause inversion rate "
        "(shear violations / ratio-bearing shear rows)",
        100.0 * hd["shear_ratio_clause_violations"] / hd["n_ratio_bearing_shear"])
    reg("derived: 100 x (violations / walked rows) — the INFLATED rate the doc "
        "names in order to correct it",
        100.0 * hd["ratio_clause_violations"]
        / hd["n_rows_walked_including_uncaged_identity_rows"])
    #    anisotropy overstatement percentages
    for L in ("12", "16", "20"):
        a = path("owed1", f"uncaged_reference_by_L>>{L}>>"
                          "SUPPLEMENTARY_anisotropy_NOT_FROZEN")
        reg(f"derived: 100 x uncaged L={L} M_111_overstates_C11_by_KUBC",
            100.0 * a["M_111_overstates_C11_by_KUBC"])
        reg(f"derived: 100 x uncaged L={L} M_111_overstates_C11_by_SUBC",
            100.0 * a["M_111_overstates_C11_by_SUBC"])
    for cfg in [c for c in path("owed1", "configurations")
                if "SUPPLEMENTARY_anisotropy_NOT_FROZEN" in c]:
        a = cfg["SUPPLEMENTARY_anisotropy_NOT_FROZEN"]["M_111_overstates_C11_by_arm"]
        for bc in ("SUBC", "KUBC"):
            reg(f"derived: 100 x {cfg['config']} M_111_overstates_C11_by_arm[{bc}]",
                100.0 * a[bc])
    #    pinned-shell fractions as percentages
    for cfg in path("owed1", "configurations"):
        fr = cfg.get("fractions") or {}
        for key, v in fr.items():
            if "pinned" not in key:
                continue
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                reg(f"derived: 100 x {cfg['config']}.fractions.{key}", 100.0 * v)
            elif isinstance(v, dict):
                for k2, v2 in v.items():
                    if isinstance(v2, (int, float)) and not isinstance(v2, bool):
                        reg(f"derived: 100 x {cfg['config']}.fractions."
                            f"{key}.{k2}", 100.0 * v2)
    #    the companion's self-consistency decay history
    for i, h in enumerate(path("owed1", "companion_fully_SUBC_grown>>outer_history")):
        for k, v in h.items():
            if isinstance(v, (int, float)) and not isinstance(v, bool):
                reg(f"owed1:companion_fully_SUBC_grown>>outer_history>>{i}>>{k}", v)
    #    the shear-channel gap ratio quoted in the §4 mechanism paragraph
    sh = [c for c in path("owed1", "configurations")
          if c["config"] == "bulk_only_cold_phi_sf"][0]["by_mode"]["shear"]
    reg("derived: bulk_only_cold_phi_sf shear K_KUBC_abs / K_SUBC_abs "
        "(the arm's own KUBC/SUBC gap)",
        sh["abs"]["K_KUBC"] / sh["abs"]["K_SUBC"])
    #    #796's banked grown live-operator tangent ratio
    for dotted in ("verdict>>fixed_budget_headline>>K_tan_over_K0",
                   "verdict>>fixed_budget_headline>>K_tan_over_K0_grown",
                   "verdict>>fixed_budget_headline>>K_ratio"):
        if _has("vessel796", dotted):
            reg_path("vessel796", dotted)
    _walk(J["vessel796"].get("verdict", {}), "verdict",
          lambda p, v: reg(f"vessel796:{p}", v))
    #    T4 worst departure as a percentage
    reg("derived: 100 x verdict.T4...worst_departure_from_unity",
        100.0 * path("owed1", "verdict>>T4_lift_bands_per_boundary_condition>>"
                              "worst_departure_from_unity"))
    #    G2b agreement percentages: |g0 - 1/(Sbar/sigma)^2| / g0
    g2b = path("owed1", "selftest_G2b")
    for blob in (g2b,):
        rows = blob.get("rows") or blob.get("by_L") or []
        if isinstance(rows, dict):
            rows = list(rows.values())
        for r in rows:
            if isinstance(r, dict) and "g0_hill" in r and "one_over_sbar_sq" in r:
                reg("derived: 100 x |g0_hill - 1/(Sbar/sigma)^2| / g0_hill",
                    100.0 * abs(r["g0_hill"] - r["one_over_sbar_sq"]) / r["g0_hill"])
    #    companion-vs-grown agreement
    try:
        comp = path("owed1", "companion_fully_SUBC_grown")
        gt = [c for c in path("owed1", "configurations")
              if c["config"] == "grown_frozen_tangent"][0]["by_mode"]["hydro"]
        for k_c, k_g in (("R_SUBC", "R_SUBC"), ("R_KUBC", "R_KUBC")):
            if k_c in comp:
                reg("derived: 100 x |companion - grown_frozen_tangent| / grown "
                    f"on {k_g}",
                    100.0 * abs(comp[k_c] - gt[k_g]) / abs(gt[k_g]))
    except (KeyError, IndexError):
        pass
    #    tolerance / measured margins the doc quotes
    reg("derived: G4 frozen tol 1e-9 / worst SUBC residual",
        1e-9 / path("owed1", "gate_G4_solver>>worst_relative_residual")
        if _has("owed1", "gate_G4_solver>>worst_relative_residual") else float("nan"))


def _has(src, dotted):
    try:
        path(src, dotted)
        return True
    except (KeyError, IndexError, TypeError):
        return False


# ---------------------------------------------------------------------------
# (b) ALLOW-LIST: numeric tokens that are NOT measurements, with the reason.
# ---------------------------------------------------------------------------
ALLOWED = {
    # frozen thresholds / tolerances quoted from the prereg
    "0.5": "frozen T1 r_Z bin edge", "0.50": "frozen T1 r_Z bin edge",
    "0.45": "frozen T2 lower r_Z edge", "0.55": "frozen T2 upper r_Z edge",
    "1.0": "frozen T3 sign threshold / identity value / isotropic Zener A",
    "1.2": "frozen T4 band L1/L2 edge", "1.5": "frozen T4 band L2/L3 edge",
    "1e-6": "frozen G1 relative slack", "1e-9": "frozen G4 residual tolerance",
    "1e-8": "frozen G5 work-identity tolerance",
    "1e-10": "frozen G8 load-amplitude-invariance tolerance",
    "1e-12": "frozen G2a identity tolerance",
    "1e-3": "frozen KUBC probe strain eps", "1e-4": "frozen deep rail S_RAIL",
    "2e-3": "frozen G6 reproduction tolerance",
    "0.10": "frozen #782 Lame deliverable tolerance",
    "0.02": "frozen G7b size-trend absolute slack",
    "60000": "frozen SUBC CG iteration cap",
    "40": "frozen companion outer-iteration cap",
    "20": "frozen companion wall-clock cap in minutes / box size L=20",
    "0.30": "frozen #782 collapse tolerance",
    # grid / geometry constants fixed by frozen sec 3
    "12": "frozen box size L", "16": "frozen box size L (L_BASE)",
    "1.3": "frozen r_cage grid point", "1.6": "frozen r_cage grid point",
    "1.9": "frozen r_cage grid point", "2.2": "frozen r_cage grid point (phi_sf)",
    "3.6": "frozen route-B s grid point", "4.2": "frozen route-B s grid point",
    "5.0": "frozen route-B s grid point", "6.5": "frozen route-B s grid point",
    "4.5": "frozen route-A s / the KUBC hydro prefactor 9/2",
    "1.7": "frozen route-B r_cage", "1.5": "frozen bw shared skin / T4 band edge",
    "1.0": "frozen cage_w / unit sigma / identity",
    "0.08": "frozen pre-stress amplitude", "3.0": "frozen cage-centre margin",
    "9.77337": "imported srs bond model rho* (ave.core.constants-derived)",
    "100": "STOP-gate rigid control stiffness multiplier",
    # plain counts / indices / labels
    "0": "count", "1": "count", "2": "count", "3": "count", "4": "count",
    "5": "count", "6": "count", "7": "count", "8": "count", "11": "count",
    "13": "count", "14": "count", "19": "count", "21": "count", "24": "count",
    "27": "count", "32": "count", "42": "count", "48": "count", "64": "count",
    "437": "line count of the surviving driver skeleton (D-1)",
    "8587": "numeric-leaf count of the leaf-by-leaf WIP audit (D-1)",
    "782": "PR number", "796": "PR number", "802": "PR number",
    "770": "PR number", "801": "PR number", "761": "PR number",
    "767": "PR number", "775": "PR number", "779": "PR number",
    "789": "PR number",
    "3.19": "an externally-reported claim this lane explicitly does NOT rely on "
            "and does not reproduce (D-9) — quoted, never used",
    "2026": "year", "07": "month", "28": "day",
    # exact zeros: identity/by-construction values, not measurements with error
    "0.0": "exact zero (uniform-translation energy; pinned_fraction_SUBC = 0 by "
           "construction; G6 rel = 0 at the two bit-exact reproductions)",
    "0.00e0": "exact zero, exponent-formatted (G6 rel = 0.00e+00)",
    "0.00e+00": "exact zero, exponent-formatted (G6 rel = 0.00e+00)",
    # ★D-14: the WRONG values this doc quotes in order to record that they were
    #   shipped wrong and are corrected. They must NOT resolve to a JSON leaf —
    #   that is the whole point of quoting them.
    "0.69588": "D-14: a RETYPED value, quoted as wrong; JSON says 0.69597",
    "0.21651": "D-14: a RETYPED value, quoted as wrong; JSON says 0.21652",
    "0.60034": "D-14: a RETYPED value, quoted as wrong; JSON says 0.60037",
    "0.53275": "D-14: a RETYPED value, quoted as wrong; JSON says 0.53276",
    "4.284e-3": "D-14: a RETYPED value (digit transposition), quoted as wrong; "
                "JSON says 4.238e-3",
    # this checker's OWN reported counts, quoted in sec 8 / D-13
    "404": "this checker's own token count, quoted in sec 8 — re-run to verify",
    "318": "this checker's own auto-registered count, quoted in sec 8",
    "66": "this checker's own allow-list count, quoted in sec 8",
    "31164": "this checker's own registered-rounded-form count, quoted in D-13",
    # crystallographic direction indices, not measurements
    "111": "Miller index [111] (body diagonal)",
    "100": "Miller index [100] / STOP-gate rigid control stiffness multiplier",
    "110": "Miller index",
    # line-number cites into merged docs (verify-before-cite anchors)
    "124": "line cite research/2026-07-21_rve-aggregation-bench_result.md:124",
    # tensor components of the frozen / supplementary probe modes
    "−1": "component of the tetragonal probe tensor diag(1,−1,0)",
    "−0": "sign-only token",
    # values quoted VERBATIM from the FROZEN prereg in order to report that the
    # shipped construction does NOT reproduce them (D-5). Registering these
    # against this lane's JSON would be a category error: the whole point is
    # that they are NOT this lane's measurements.
    "3.2e-14": "frozen prereg §1.1 design-time pilot moment, quoted verbatim in "
               "D-5 precisely because the shipped load set does NOT reproduce it",
    "3.8e-15": "frozen prereg §1.1 design-time pilot net force, quoted verbatim",
    "1e-14": "frozen prereg §6.2 pilot order-of-magnitude, quoted verbatim",
    "0.296": "merged #782's own QUOTED headline precision (the G6 target string "
             "frozen in prereg §4 G6), not a value this lane computes",
}

# ---------------------------------------------------------------------------
# (c) PINNED: LOW-PRECISION measurement tokens, mapped BY HAND to a named path.
#
# ★WHY A PRECISION FLOOR EXISTS.  Auto-registration enumerates ~31k rounded
# forms of named JSON leaves.  At 5-6 significant digits a collision is
# vanishingly unlikely, so an auto-match IS provenance.  At 1-2 significant
# digits it is not: `0.5` matches *some* leaf in a bench this size by accident,
# which would make the check vacuous exactly where a wrong number is easiest to
# hide.  So tokens with fewer than MIN_SIG significant digits are REFUSED
# auto-registration and must appear here (hand-mapped, still value-verified) or
# in ALLOWED (a constant, with a reason).
# ---------------------------------------------------------------------------
MIN_SIG = 3


def _g2b_agreement_pct(i: int) -> float:
    """|g_0(L) - 1/(Sigma_bar/sigma)^2| / g_0(L), in percent, at grid index i —
    the §3 'the gap and the Hill deficit are the SAME boundary layer' figures."""
    g = path("owed1", "selftest_G2b>>g0_hill_normalized")[i]
    inv = path("owed1", "selftest_G2b>>inverse_sigma_bar_squared")[i]
    return 100.0 * abs(g - inv) / inv


PINNED = {
    "0.0063": ("owed1", "verdict>>T4_lift_bands_per_boundary_condition>>"
                        "worst_departure_from_unity"),
    "0.63": ("derived", lambda: 100.0 * path(
        "owed1", "verdict>>T4_lift_bands_per_boundary_condition>>"
                 "worst_departure_from_unity")),
    "0.54": ("rve782", "leg4_verdict>>by_class>>bulk_only_cold>>by_beta>>"
                       "beta_0>>r_Z"),
    "19": ("derived", lambda: 100.0 * path(
        "owed1", "gate_G1_VOID_ordering>>honest_ratio_clause_denominators>>"
                 "ratio_clause_inversion_rate_over_ratio_bearing_rows")),
    "17": ("derived", lambda: 100.0 * path(
        "owed1", "gate_G1_VOID_ordering>>honest_ratio_clause_denominators>>"
                 "ratio_clause_violations") / path(
        "owed1", "gate_G1_VOID_ordering>>honest_ratio_clause_denominators>>"
                 "n_rows_walked_including_uncaged_identity_rows")),
    "38": ("derived", lambda: 100.0 * path(
        "owed1", "gate_G1_VOID_ordering>>honest_ratio_clause_denominators>>"
                 "shear_ratio_clause_violations") / path(
        "owed1", "gate_G1_VOID_ordering>>honest_ratio_clause_denominators>>"
                 "n_ratio_bearing_shear")),
    "7.9": ("derived", lambda: 100.0 * path(
        "owed1", "uncaged_reference_by_L>>16>>"
                 "SUPPLEMENTARY_anisotropy_NOT_FROZEN>>"
                 "M_111_overstates_C11_by_SUBC")),
    "5.2": ("derived", lambda: 100.0 * path(
        "owed1", "configurations>>3>>SUPPLEMENTARY_anisotropy_NOT_FROZEN>>"
                 "M_111_overstates_C11_by_arm>>SUBC")),
    "2.4": ("derived", lambda: _g2b_agreement_pct(0)),
    "1.7": ("derived", lambda: _g2b_agreement_pct(1)),
    "9.4": ("derived", lambda: 100.0 * path(
        "owed1", "configurations>>0>>fractions>>"
                 "pinned_shell_node_fraction_KUBC>>pinned_fraction")),
    "8.6e-16": ("owed1", "gate_G5_work_identity>>worst_work_identity_rel"),
    "4.5e-12": ("owed1", "uncaged_reference_by_L>>12>>by_mode>>hydro>>"
                         "net_force_norm"),
    "2.6e-6": ("owed1", "uncaged_reference_by_L>>12>>by_mode>>hydro>>"
                        "net_torque_norm_rel"),
    "7e-5": ("derived", lambda: abs(path(
        "owed1", "uncaged_reference_by_L>>16>>"
                 "SUPPLEMENTARY_anisotropy_NOT_FROZEN>>tetra_solver>>"
                 "Sigma_bar_tensor_SUBC>>0>>2"))),
    "1.1": ("derived", lambda: _g2b_agreement_pct(2)),
    "0.0000": ("derived", lambda: [r for r in path("owed1", "reads")
                                   if r["config"] == "uniform_medium_null"
                                   and r["mode"] == "hydro"][0]["width"]),
}

# digests / shas / md5s: matched structurally, not by value
_HEXY = re.compile(r"^[0-9a-f]{7,64}$")


def sig_digits(tok: str) -> int:
    m = tok.lstrip("−-").split("e")[0].split("E")[0]
    d = m.replace(".", "").lstrip("0")
    return max(len(d), 1)


def as_float(tok: str) -> float:
    return float(tok.replace("−", "-"))


def rounds_to(value, tok: str) -> bool:
    n = sig_digits(tok)
    try:
        return float("%.{}g".format(n) % float(value)) == as_float(tok)
    except (TypeError, ValueError):
        return False


NUM = re.compile(r"^[−-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$")
TOKEN = re.compile(r"`([^`]+)`")


def self_check() -> list:
    """Refuse to run if a machine-dependent leaf has been NAMED as a source.

    The test is STRUCTURAL — "does any registration label point at a
    non-registrable path?" — deliberately NOT value-based.  A value-based test
    ("does any token that happens to equal the runtime appear?") is itself
    machine-dependent: on one machine the runtime rounds to `13` and collides
    with an unrelated measurement, on another it does not, so the checker's own
    verdict would vary by machine.  That is the #801 R3 failure mode one level
    up, and this function must not reproduce it."""
    bad = []
    for label in set(REGISTERED.values()):
        for p, why in NON_REGISTRABLE.items():
            if label.endswith(":" + p) or label.endswith(">>" + p.split(">>")[-1]) \
                    and p in label:
                bad.append(f"SELF-CHECK  a registration names NON-REGISTRABLE "
                           f"'{p}' ({why}) via label '{label}'. Machine-dependent "
                           f"values may not be registered; remove the numeral "
                           f"from the doc instead of laundering it.")
    return bad


def main() -> int:
    _register_all()
    text = open(DOC).read()
    seen, checked, allowed_n, hexy_n, unaccounted = set(), 0, 0, 0, 0
    pinned_n = 0
    explain = "--explain" in sys.argv
    bad = list(self_check())
    lines = []
    for raw in TOKEN.findall(text):
        for tok in re.split(r"[\s,;:()\[\]{}=<>×/|]+", raw):
            tok = tok.strip("`*_.'\"±%")
            if not tok or tok in seen:
                continue
            if _HEXY.match(tok) and not NUM.match(tok):
                seen.add(tok)
                hexy_n += 1
                continue
            if not NUM.match(tok):
                continue
            seen.add(tok)
            if _HEXY.match(tok) and len(tok) >= 7 and not tok.startswith("0."):
                # e.g. a 7+ hex-digit sha that happens to be all decimal digits
                hexy_n += 1
                continue
            tok = _norm_exp(tok)   # `1.24e-03` and `1.24e-3` are one number
            lowp = sig_digits(tok) < MIN_SIG
            if lowp and tok in PINNED:
                src, ref = PINNED[tok]
                val = ref() if callable(ref) else path(src, ref)
                pinned_n += 1
                label = (f"PINNED {src}:{ref}" if not callable(ref)
                         else f"PINNED derived (formula in PINNED[{tok!r}])")
                if not rounds_to(val, tok):
                    bad.append(f"MISMATCH  `{tok}`  <-  {label}  value {val!r}")
                elif explain:
                    lines.append(f"  OK  `{tok}`  <-  {label}")
            elif lowp and tok in ALLOWED:
                allowed_n += 1
                if explain:
                    lines.append(f"  ALLOW  `{tok}`  — {ALLOWED[tok]}")
            elif lowp:
                unaccounted += 1
                bad.append(
                    f"LOW-PRECISION UNPINNED  `{tok}`  — only "
                    f"{sig_digits(tok)} significant digit(s), below MIN_SIG="
                    f"{MIN_SIG}, so an auto-match against ~{len(REGISTERED)} "
                    f"rounded forms would be coincidence, not provenance. Add it "
                    f"to PINNED (hand-mapped to a named path) or to ALLOWED "
                    f"(a constant, with a reason).")
            elif tok in REGISTERED:
                checked += 1
                if explain:
                    lines.append(f"  OK  `{tok}`  <-  {REGISTERED[tok]}")
            elif tok in ALLOWED:
                allowed_n += 1
                if explain:
                    lines.append(f"  ALLOW  `{tok}`  — {ALLOWED[tok]}")
            else:
                unaccounted += 1
                bad.append(f"UNREGISTERED  `{tok}`  — not the rounded value of "
                           f"any named JSON leaf and not allow-listed. Register "
                           f"it against its source or justify it.")
    print(f"[number-check] doc: {os.path.relpath(DOC, REPO)}")
    print(f"[number-check] JSON leaves registered (named): {len(REGISTERED)} "
          f"distinct rounded forms")
    print(f"[number-check] distinct numeric tokens in doc: {len(seen)}")
    print(f"[number-check]   auto-registered + verified (>= {MIN_SIG} sig digits, "
          f"matched to a NAMED JSON leaf): {checked}")
    print(f"[number-check]   PINNED + verified (low-precision, hand-mapped to a "
          f"named path): {pinned_n}")
    print(f"[number-check]   allow-listed constants (frozen thresholds, grid "
          f"points, counts, indices): {allowed_n}")
    print(f"[number-check]   sha / digest / md5-shaped: {hexy_n}")
    print(f"[number-check]   UNACCOUNTED: {unaccounted}")
    for ln in lines:
        print(ln)
    for b in bad:
        print("  " + b)
    if bad:
        print(f"[number-check] FAIL — {len(bad)} finding(s)")
        return 1
    print("[number-check] PASS — every quoted number is the correctly-rounded "
          "value of a NAMED shipped-JSON leaf (or an allow-listed constant); no "
          "machine-dependent value is registered or allow-listed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

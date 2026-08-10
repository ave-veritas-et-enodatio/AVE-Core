"""Programmatic number check for the Pasteur-kappa desk-calc lane.

★WHY THIS EXISTS.  The #801 / #802 pattern: a number cannot enter this lane's
documents by being TYPED — it enters by being REGISTERED against its source.  Two
prior lanes shipped prose that disagreed with their own JSON (a fabricated frozen
string, a swapped criterion), each caught only by adversarial review.  Care is not
a remedy for that class of defect; a check is.

WHAT IT DOES.  It scans every inline-code token that parses as a number in EVERY
document this lane ships (see DOCS: the result doc AND the docket fragment) and
requires each to be either

  (a) REGISTERED — the correctly-rounded value, at its own quoted precision, of a
      NAMED leaf of the shipped JSON, or of a derived quantity computed FROM those
      leaves by a formula written out here; or
  (b) ALLOW-LISTED — a frozen tolerance/bin edge, a geometry constant, a count, a
      section/line cite, or a value QUOTED FROM ANOTHER REPO (which by definition
      is not a leaf of this lane's JSON), each with a reason.

Anything else FAILS.

★BARE INTEGERS are never auto-registrable: a count is not a measurement, and an
integer-vs-integer value match is coincidence rather than provenance.

★LOW-PRECISION FLOOR (MIN_SIG).  Auto-registration enumerates thousands of rounded
forms; at >=3 significant digits a collision is negligible and an auto-match IS
provenance.  Below that it is not, so such tokens must be PINNED (hand-mapped to a
named path) or ALLOWED (a constant, with a reason).

★NON_REGISTRABLE.  Nothing machine-dependent is registrable or allow-listable:
this lane's JSON ships no wall-clock, and main() refuses any attempt to add one.

Hermetic: stdlib only, one in-tree JSON, two in-tree docs, no `ave` import, no
network, sub-second.

Run:  python3 research/drivers/pasteur_kappa_desk_calc_number_check.py [--explain]
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

DOCS = [
    os.path.join(REPO, "research", "2026-08-02_pasteur-kappa-desk-calc_result.md"),
    os.path.join(REPO, "_orchestration", "docket-entries",
                 "2026-08-02-pasteur-kappa-calc.md"),
]
SOURCE = os.path.join(HERE, "pasteur_kappa_desk_calc_results.json")
J = json.load(open(SOURCE))

# This lane ships no machine-dependent leaf.  The guard is structural, so that a
# future edit that adds one cannot quietly launder it into a document.
NON_REGISTRABLE = {
    "_runtime_sec": "machine-dependent",
    "wall_clock_s": "machine-dependent",
}

MIN_SIG = 3


def path(dotted: str):
    node = J
    for part in dotted.split(">>"):
        node = (node[int(part)]
                if part.lstrip("-").isdigit() and isinstance(node, list)
                else node[part])
    return node


def _norm_exp(s: str) -> str:
    """`7e-05` and `7e-5` are the same quoted number; normalise the exponent."""
    m = re.match(r"^(.*?)[eE]([+-]?)0*(\d+)$", s)
    if not m:
        return s
    mant, sign, digits = m.groups()
    return f"{mant}e{'-' if sign == '-' else ''}{digits or '0'}"


def _fmts(v: float) -> set[str]:
    """Every rounded string form a doc may legitimately quote for `v`."""
    out: set[str] = set()
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        return out
    if v != v or v in (float("inf"), float("-inf")):
        return out
    for n in range(1, 18):
        out.add(("%." + str(n) + "g") % v)
    for d in range(0, 13):
        out.add(("%." + str(d) + "f") % v)
    for d in range(1, 18):
        out.add(("%." + str(d) + "e") % v)
    out.add(repr(float(v)))
    out = {_norm_exp(s) for s in out}
    out |= {s.replace("-", "−", 1) for s in out if s.startswith("-")}
    return {s for s in out if s not in ("", "-", "−")}


REGISTERED: dict[str, str] = {}


def reg(label: str, value) -> None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return
    for tok in _fmts(float(value)):
        REGISTERED.setdefault(tok, label)   # first namer wins


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


def _register_all() -> None:
    # 1. every numeric leaf of the shipped JSON, NAMED by its path.
    def emit(p, v):
        if p.split(">>")[-1] in NON_REGISTRABLE:
            return
        reg(f"json:{p}", v)

    _walk(J, "", emit)

    # 2. DERIVED quantities the documents quote, with their formulas visible here.
    kR = path("K1_primary>>k23_R")
    k3 = path("K3_density_free")
    qc = path("quadrature_convergence")
    z0 = path("inputs>>Z_0_ohm")
    reg("derived: Z_0 / (3 R_rad) — the impedance-over-loss lever in V_chi",
        z0 / (3.0 * kR["R_rad_ohm"]))
    reg("derived: (lambda/pi) / |ell_e| — the effective-length collapse factor",
        (kR["lambda_m"] / 3.141592653589793) / kR["ell_e_mag_m"])
    reg("derived: N_dilute_ceiling / N_star — how far INSIDE linear-mixing "
        "validity the iso-kappa density sits",
        k3["N_dilute_ceiling_per_m3"] / k3["N_star_per_m3"])
    reg("derived: kappa_cls(N_ref) / 0.1 — how far OUTSIDE linear-mixing validity "
        "the close-packed value sits",
        kR["kappa_cls_isotropic"] / 0.1)
    reg("derived: max |chi| relative mesh drift over the convergence probe",
        max(qc["chi_rel_drift_vs_base"]))
    reg("derived: max R_rad relative mesh drift over the convergence probe",
        max(qc["R_rad_rel_drift_vs_base"]))
    # --- 2026-08-02 audit-repair pass (PR #834 F1/F4) -----------------------
    k2 = path("K2_observable_matched")
    s3 = path("post_audit_supplementary_NOT_FROZEN>>S3_combined_floor_scope")
    reg("derived: the S-8 + measurement COMBINED floor in kHz (F4) — "
        "sqrt(130 kHz^2 + (290 kHz sqrt(2/10))^2), inputs cross-repo",
        s3["combined_floor_Hz"] / 1e3)
    reg("derived: the MEASUREMENT-only floor in kHz (F4) — 290 kHz sqrt(2/10)",
        s3["measurement_floor_Hz"] / 1e3)
    reg("derived: the FR-4 glass-weave systematic OOM in MHz (F1) — taken at "
        "6 percent of the AVE enantiomer split, 0.06 * ave_value_MHz_at_f0",
        0.06 * k2["ave_value_MHz_at_f0"])


# ---------------------------------------------------------------------------
# (b) ALLOW-LIST — numeric tokens that are NOT measurements of this lane.
# ---------------------------------------------------------------------------
ALLOWED = {
    # frozen bin edges / gate tolerances, quoted verbatim from the prereg
    "3": "frozen magnitude-bin edge R>=3 / a plain count / the NPTH drill "
         "file's decimal-place count",
    "10": "frozen STRONG sub-band edge R>=10",
    "0.1": "frozen STRONG sub-band edge R<=0.1 AND the linear-mixing ceiling",
    "1e-9": "frozen G1/G2/G3 tolerance",
    "1e-6": "frozen G4 tolerance",
    "0.25": "frozen G6 subwavelength tolerance",
    "2": "frozen G5 percent tolerance / a plain count",
    "1": "frozen G5 percent tolerance / a plain count",
    "4": "plain count (checklist rows) / mesh-refinement factor",
    "7": "plain count (gates)",
    "8": "plain count (seeded origin shifts)",
    "73.13": "textbook half-wave-dipole radiation resistance — the EXTERNAL "
             "known-positive target G5 must reproduce, not a leaf of this lane",
    # as-fabbed geometry constants (frozen prereg 6.1), low precision
    "2.6": "as-fabbed bbox z-extent in mm (frozen geometry input)",
    "680": "as-fabbed f0 in MHz (frozen input; the Hz leaf is 680000000.0)",
    "130": "round-2 sec 4 inherited S-8 fab floor in kHz (quoted from AVE-HOPF)",
    "231": "as-fabbed polyline length in mm as quoted in the AVE-HOPF design "
           "proposal (this lane computes 230.560 from the CSV)",
    "73": "textbook half-wave dipole R_rad in ohm, quoted to 2 figures in prose",
    "1.0": "frozen sensitivity grid point (gamma and eps_eff)",
    "1.5": "frozen sensitivity grid point (eps_eff)",
    "2.0": "frozen sensitivity grid point (eps_eff)",
    "0.8": "frozen sensitivity grid point (gamma)",
    "1.2": "frozen sensitivity grid point (gamma) / the (2,3) harmonic mean 6/5",
    # values QUOTED FROM ANOTHER REPO — by definition not leaves of this JSON
    "0.000": "AVE-HOPF nec2_prediction.md:80 Delta_classical column, quoted",
    "11.91": "AVE-HOPF nec2_prediction.md:80 Delta_AVE_pred in MHz, quoted "
             "(this lane independently computes 11.9093)",
    "−11.91": "AVE-HOPF nec2_prediction.md:80 Delta_AVE_pred, quoted with "
                   "the typographic minus",
    "1.75": "AVE-HOPF nec2_prediction.md:80 Delta_AVE/f0 in percent, quoted",
    # file:line cites (verify-before-cite anchors, each re-read from the git blob)
    "155": "line cite ~/.claude/skills/ave-discrimination-check/SKILL.md:155",
    "166": "line cite ~/.claude/skills/ave-discrimination-check/SKILL.md:166",
    "180": "line cite AVE-HOPF hardware/hopf_01_TEST_PROCEDURE.md:180",
    "57": "line cite AVE-HOPF docs/design/2026-05-05_hopf02_design_proposal.md:57",
    "80": "line cite AVE-HOPF docs/design/2026-05-05_hopf02_nec2_prediction.md:80",
    "27": "line cite AVE-HOPF docs/ave_crib_sheet.md:27",
    "131": "line cite AVE-HOPF docs/glossary.md:131",
    "84": "line cite — round-2 result sec 2.3 first line",
    "88": "line cite — round-2 result sec 2.3 last line",
    # this lane's own reported counts, quoted in the docs — re-run to verify
    "0": "exact zero (the classical enantiomer split; chi_control; G2/G3 residual)",
    "6": "plain count / the 6 mm SMA-ground aperture diameter in the Gerber "
         "aperture list / the weave-anisotropy OOM as a percent of the split",
    "5": "plain count (idealizations I-1..I-5) / the weave OOM as a multiple of "
         "the 130 kHz S-8 floor, stated to one figure",
    # -------------------------------------------------------------------
    # 2026-08-02 AUDIT-REPAIR PASS (PR #834 F1/F2/F4 + nits).  Every entry
    # below is a value READ FROM ANOTHER REPO's blob or a line cite — by
    # construction not a leaf of this lane's JSON.  Each was re-read from the
    # live git blob at repair time (`verify-before-cite`).
    # -------------------------------------------------------------------
    # AVE-HOPF main:hardware/Gerbers_hopf_02a/ — read-only symmetry check (F1)
    "250": "AVE-HOPF Gerbers hopf_02a-Edge_Cuts.gm1 — panel x-extent in mm",
    "185": "AVE-HOPF Gerbers hopf_02a-Edge_Cuts.gm1 — panel y-extent in mm",
    "50": "AVE-HOPF Gerbers Edge_Cuts v-score / coupon-lane pitch in mm",
    "100": "AVE-HOPF Gerbers Edge_Cuts v-score position in mm",
    "150": "AVE-HOPF Gerbers Edge_Cuts v-score position in mm — the (2,5) "
           "pair's mirror line",
    "200": "AVE-HOPF Gerbers Edge_Cuts v-score position in mm",
    "45": "AVE-HOPF Gerbers — PTH.drl hole count, and the per-layer copper "
          "flash count in F_Cu.gtl / B_Cu.gbl; also the line cite AVE-HOPF "
          "research/2026-06-04_hopf-round2-chiral-counterfactual-result.md:45",
    "63": "line cite AVE-HOPF research/"
          "2026-06-04_hopf-round2-chiral-counterfactual-result.md:63",
    "94": "AVE-HOPF Gerbers hopf_02a-NPTH.drl hole count",
    "0.001": "AVE-HOPF Gerbers NPTH.drl mirror residual in mm — the file's own "
             "3-decimal-place quantization, not a measured asymmetry",
    "7.709": "AVE-HOPF Gerbers F_Cu.gtl — SMA centre-pin flash offset from the "
             "x=50 mm mirror line, in mm (flashes at x=42.291 and x=57.709)",
    "8.436": "AVE-HOPF Gerbers F_Cu.gtl — same, for the (2,5) pair about "
             "x=150 mm (flashes at x=141.564 and x=158.436)",
    # AVE-HOPF cross-repo quotes and line cites added by the repair pass
    "72": "line cite AVE-HOPF docs/design/2026-05-05_hopf02_nec2_prediction.md:72",
    "74": "line cite AVE-HOPF docs/design/2026-05-05_hopf02_nec2_prediction.md:74",
    "81": "line cite AVE-HOPF docs/design/2026-05-05_hopf02_nec2_prediction.md:81",
    "264": "line cite AVE-HOPF docs/analysis/"
           "2026-06-03_hopf_antenna_hardened_prereg.md:264 (the S-8 row)",
    "193": "line cite AVE-HOPF research/"
           "2026-06-04_hopf-round2-chiral-counterfactual-result.md:193",
    "14": "line cite AVE-HOPF .agents/HANDOFF.md:14 (the Phase-0b status line)",
    "42": "line cite AVE-HOPF .agents/HANDOFF.md:42 (the gated fab-order TODO)",
    "19": "line cite AVE-Core research/"
          "2026-06-04_experimental-round2-synthesis.md:19 (Cleave-01 row)",
    "28": "line cite AVE-Core research/"
          "2026-06-04_experimental-round2-synthesis.md:28",
    "116": "line cite AVE-HOPF PR #3 docs/open_questions.md:116",
    "5000": "AVE-HOPF hardened-prereg:264 Monte-Carlo trial count, quoted",
    "380": "AVE-HOPF nec2_prediction.md:81 f_classical for (2,5) in MHz, quoted",
    "1.429": "AVE-HOPF nec2_prediction.md:81 pq/(p+q) for (2,5), quoted",
    "123": "AVE-HOPF .agents/HANDOFF.md:14 and :42 HOPF-02a BOM cost in USD, "
           "quoted — not a measurement of this lane",
    "0.29": "AVE-HOPF PR #3 docs/open_questions.md:116 — the sigma_repeat "
            "CEILING in MHz that S-1's own N>=10 implies, quoted. UNMEASURED.",
    "290": "the same sigma_repeat ceiling in kHz",
}

_HEXY = re.compile(r"^[0-9a-f]{7,64}$")
NUM = re.compile(r"^[−-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$")
TOKEN = re.compile(r"`([^`]+)`")


def scan_spans(text: str) -> list[str]:
    """Every back-tick span in `text`, paired PER LINE.

    PARITY IMMUNISATION (ruling R27, `_orchestration/docket-entries/
    2026-08-07-rulings-r23-r27.md`; defect found by the #912 sibling audit,
    `_orchestration/docket-entries/2026-08-06-backtick-parity.md` section 6).

    This was a single `TOKEN.findall(text)` over the WHOLE JOINED text of
    every declared document.  The token
    class ``[^`]+`` does NOT exclude newlines, so ONE line carrying an ODD
    back-tick count flips the open/close phase for EVERY LINE BELOW IT,
    ACROSS DOCUMENT BOUNDARIES: every numeral below it
    lands in a gap the scanner never reads -- silently, with the gate still green.

    On this checker's document(s) the repair is a MEASURED NO-OP: +0/-0 spans, 0
    odd-parity lines, re-measured at the landing commit.  It ships anyway because
    the defect is a TIME BOMB -- the first odd-parity line anyone adds unscans
    everything below it.  Per-line pairing fails SAFE: a malformed line can only
    ever ADD spans on its own line, never remove coverage from the lines below.

    SCOPE, and it is not a general theorem: a CommonMark code span may straddle a
    newline; such a span is read by global pairing and missed per-line.  These
    documents contain none (hence the measured +0/-0, not an argument).  The same
    bounded hole is the repo's standing convention for this scan.  What the
    repair removes is the UNBOUNDED hole.
    """
    return [m for line in text.splitlines() for m in TOKEN.findall(line)]


def _scan_spans_legacy_global(text: str) -> list[str]:
    """The PRE-REPAIR scanner (GLOBAL pairing), retained for exactly ONE purpose:
    it is the parity mutation's FORCED-OFF arm.  A mutation the old scanner
    catches too proves nothing about the repair, so the receipt re-runs `main`
    with this scanner injected and REQUIRES it to MISS.  Not reachable from any
    gate -- `main`'s `_scanner` parameter has no argv spelling."""
    return TOKEN.findall(text)


BARE_INT = re.compile(r"^[−-]?\d+$")

# low-precision / bare-integer tokens hand-mapped to a NAMED path (still verified)
PINNED: dict[str, tuple[str, object]] = {
    "0.0": ("json", "gates>>G2_mirror_antisymmetry>>rel"),
    "29.09": ("json", "K1_primary>>k23_R>>kappa_cls_isotropic"),
    "0.7385": ("json", "K1_primary>>k23_R>>R_rad_ohm"),
    "0.1403": ("json", "gates>>G5_dipole_validation>>lambda_over_pi_m"),
    "20.35": ("derived", lambda: (path("K1_primary>>k23_R>>lambda_m")
                                  / 3.141592653589793)
              / path("K1_primary>>k23_R>>ell_e_mag_m")),
    # 2026-08-02 audit-repair pass (F1): the glass-weave OOM is quoted to ONE
    # figure on purpose (it is an order of magnitude, not a measurement), so it
    # is below MIN_SIG and must be hand-mapped rather than auto-matched.
    "0.7": ("derived",
            lambda: 0.06 * path("K2_observable_matched>>ave_value_MHz_at_f0")),
    # 2026-08-02 audit-repair pass (nit N1): the sub-elements-per-edge count,
    # quoted in the sec 2 chi-digit-count note.  A bare integer, so hand-mapped
    # to the leaf that actually carries it rather than auto-matched.
    "64": ("json", "inputs>>quadrature>>n_sub_per_edge"),
}


def sig_digits(tok: str) -> int:
    m = tok.lstrip("−-").split("e")[0].split("E")[0]
    d = m.replace(".", "").lstrip("0")
    return max(len(d), 1)


def as_float(tok: str) -> float:
    return float(tok.replace("−", "-"))


def rounds_to(value, tok: str) -> bool:
    n = sig_digits(tok)
    try:
        return float(("%." + str(n) + "g") % float(value)) == as_float(tok)
    except (TypeError, ValueError):
        return False


def self_check() -> list[str]:
    """Refuse to run if a registration NAMES a machine-dependent leaf.

    Structural, deliberately not value-based: a value-based test would itself be
    machine-dependent and the checker's verdict would vary by machine.
    """
    bad = []
    for label in set(REGISTERED.values()):
        for p in NON_REGISTRABLE:
            if label.endswith(">>" + p) or label.endswith(":" + p):
                bad.append(f"SELF-CHECK  registration '{label}' names "
                           f"NON-REGISTRABLE '{p}' ({NON_REGISTRABLE[p]})")
    return bad


def main(_text_override: str | None = None, _scanner=None) -> int:
    """The gating check.

    The two private parameters are SEAMS FOR THE MUTATION RECEIPT and have no
    argv spelling, so nothing a caller can type reaches them:
      * `_text_override` -- run the shipped classification over an IN-MEMORY
        planted copy of the document(s), leaving the files on disk untouched;
      * `_scanner` -- substitute the pre-repair global-paired scanner, which is
        how the receipt FORCES THE FIX OFF and demonstrates the same plant is
        MISSED without it.
    Both default to the shipped behaviour.
    """
    scan = _scanner or scan_spans
    _register_all()
    explain = "--explain" in sys.argv
    text = ("\n".join(open(d).read() for d in DOCS)
            if _text_override is None else _text_override)
    seen: set[str] = set()
    checked = pinned_n = allowed_n = hexy_n = unaccounted = 0
    bad = list(self_check())
    lines: list[str] = []

    for raw in scan(text):
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
            tok = _norm_exp(tok)
            lowp = sig_digits(tok) < MIN_SIG or bool(BARE_INT.match(tok))
            if lowp and tok in PINNED:
                src, ref = PINNED[tok]
                val = ref() if callable(ref) else path(ref)
                pinned_n += 1
                label = (f"PINNED {src}:{ref}" if not callable(ref)
                         else f"PINNED derived (formula in PINNED[{tok!r}])")
                if not rounds_to(val, tok):
                    bad.append(f"MISMATCH  `{tok}`  <-  {label}  value {val!r}")
                elif explain:
                    lines.append(f"  OK     `{tok}`  <-  {label}")
            elif lowp and tok in ALLOWED:
                allowed_n += 1
                if explain:
                    lines.append(f"  ALLOW  `{tok}`  — {ALLOWED[tok]}")
            elif lowp:
                unaccounted += 1
                why = ("a BARE INTEGER (a count/index), never auto-registrable: a "
                       "value match would be coincidence, not provenance"
                       if BARE_INT.match(tok) else
                       f"only {sig_digits(tok)} significant digit(s), below "
                       f"MIN_SIG={MIN_SIG}, so an auto-match against "
                       f"~{len(REGISTERED)} rounded forms would be coincidence")
                bad.append(f"LOW-PRECISION / BARE-INT UNPINNED  `{tok}`  — {why}. "
                           f"Add it to PINNED (hand-mapped to a named path) or to "
                           f"ALLOWED (a constant/count, with a reason).")
            elif tok in REGISTERED:
                checked += 1
                if explain:
                    lines.append(f"  OK     `{tok}`  <-  {REGISTERED[tok]}")
            elif tok in ALLOWED:
                allowed_n += 1
                if explain:
                    lines.append(f"  ALLOW  `{tok}`  — {ALLOWED[tok]}")
            else:
                unaccounted += 1
                bad.append(f"UNREGISTERED  `{tok}`  — not the rounded value of any "
                           f"named JSON leaf and not allow-listed. Register it "
                           f"against its source or justify it.")

    for d in DOCS:
        print(f"[number-check] doc: {os.path.relpath(d, REPO)}")
    print(f"[number-check] JSON leaves registered (named): {len(REGISTERED)} "
          f"distinct rounded forms")
    print(f"[number-check] distinct numeric tokens in docs: {len(seen)}")
    print(f"[number-check]   auto-registered + verified (>= {MIN_SIG} sig digits): "
          f"{checked}")
    print(f"[number-check]   PINNED + verified (low-precision, hand-mapped): "
          f"{pinned_n}")
    print(f"[number-check]   allow-listed (frozen edges, geometry, counts, cites, "
          f"cross-repo quotes): {allowed_n}")
    print(f"[number-check]   sha / digest-shaped: {hexy_n}")
    print(f"[number-check]   UNACCOUNTED: {unaccounted}")
    for ln in lines:
        print(ln)
    for b in bad:
        print("  " + b)
    if bad:
        print(f"[number-check] FAIL — {len(bad)} finding(s)")
        return 1
    print("[number-check] PASS — every quoted number is the correctly-rounded "
          "value of a NAMED shipped-JSON leaf, a named derived formula, or an "
          "allow-listed constant with a reason")
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
    _register_all()   # idempotent (`reg` is first-namer-wins); the registries
    #                 must be populated before the anti-vacuity arm reads them.
    text = "\n".join(open(d).read() for d in DOCS)
    planted = text + "\n" + PARITY_PROBE_LINE + "\n" + PARITY_PLANT_LINE + "\n"

    results: dict[str, bool] = {}
    results["anti-vacuity"] = (PARITY_PLANT_TOKEN not in text
                               and PARITY_PLANT_TOKEN not in REGISTERED
                               and PARITY_PLANT_TOKEN not in ALLOWED
                               and PARITY_PLANT_TOKEN not in PINNED)
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
        print(f"[number-check]   {arm:<17} "
              f"{'OK' if got else 'FAIL' if got is False else 'MISSING'}")
    if not ok:
        print("[number-check] --- captured output from the arms ---")
        print(sink.getvalue())
    print(f"[number-check] parity mutation receipt: "
          f"{'PASS' if ok else 'FAIL'} ({len(PARITY_ARMS)} arms)")
    return 0 if ok else 1


if __name__ == "__main__":
    if "--mutation-receipt" in sys.argv:
        sys.exit(mutation_receipt())
    sys.exit(main())

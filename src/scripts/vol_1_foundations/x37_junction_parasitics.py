#!/usr/bin/env python3
"""X37 — junction-parasitic extraction driver: the srs vertex equivalent circuit
DERIVED from bond geometry (D-I route, after #613/X36 was BLOCKED for installing).

Prereg (FROZEN): research/2026-07-10_x37-junction-parasitics_prereg_FROZEN.md
Derivation:      research/2026-07-10_x37-junction-parasitics_derivation.md
Class: MIXED — the g VALUE is derived-geometric (ave.core.junction_parasitics, which
imports NO scale); the SCALE omega_C = c/ell_node is dimensional-forced/identity and
appears ONLY in this driver's reporting layer (MeV labels).

Runs the four pre-registered gates with planted-violation proofs (G-A anti-install via
AST scan, G-B independent-reference recovery vs the FROZEN #604 top, G-C vertex-extent
honesty + branch assignment, G-D gates-can-fire), sweeps the ceiling g(f), writes JSON
and a WHITE figure.

Run: PYTHONPATH=src python3 src/scripts/vol_1_foundations/x37_junction_parasitics.py
"""

from __future__ import annotations

import ast
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from ave.core import junction_parasitics as jp

# REPORTING + DETECTOR scale imports (this driver is the DETECTOR, not the extraction
# path — G-A scans ave.core.junction_parasitics, never this file). Used for MeV labels,
# the pi*sqrt3 reference, and the forbidden-MAGNITUDE list (review R8). Imported by
# SYMBOL — no hard-coded constant values (the anti-cheat DAG scan forbids magic numbers).
from ave.core.constants import C_CELL, HBAR, L_CELL, M_E, OMEGA_C, e_charge
from ave.viz import style

# ─────────────────────────────────────────────────────────────────────────────
# FROZEN reference (G-B): the merged #604 memoryless scalar band top, hard-coded
# FROM the result doc, NOT recomputed by the loaded solver's own path.
#   research/2026-07-09_srs-band-survey_result.md:18
#     "GLOBAL BAND TOP = pi*sqrt3 omega_C = 5.4414 omega_C = 2.781 MeV, at H"
# ─────────────────────────────────────────────────────────────────────────────
REF_604_BAND_TOP_OVER_OMEGA_C = np.pi * np.sqrt(3.0)  # = 5.441398092702653 (#604)
REF_604_DOC = "research/2026-07-09_srs-band-survey_result.md:18"

MEV_PER_OMEGA_C = HBAR * OMEGA_C / e_charge / 1e6  # ~0.511 MeV/omega_C (m_e c^2 IDENTITY)

# Frozen tolerances / thresholds (prereg §6 — no post-hoc relaxation)
BRANCH_I_TOL = 0.02  # |g(f*) - pi*sqrt3| / pi*sqrt3
BRANCH_I_SWING = 0.05  # |g(0)-g(0.5)| / pi*sqrt3
BRANCH_III_SWING = 0.10  # extent-dominated threshold
F_STAR = jp.F_WIGNER_SEITZ  # reported central (upper-bound probe), 0.5

_HERE = Path(__file__).resolve().parent
_OUT = _HERE / "_output"
_OUT.mkdir(exist_ok=True)

_FORBIDDEN = {"OMEGA_C", "M_E", "L_CELL", "C_CELL"}
_EXTRACTION_MODULE = Path(jp.__file__)

# Forbidden-scale MAGNITUDES, taken by SYMBOL from constants (NO hard-coded values —
# the anti-cheat DAG scan forbids magic numbers, and this keeps the detector exact).
# The symbol scan is blind to a hard-coded numeric LITERAL of, e.g., omega_C's value
# (review R8), so the detector also flags any numeric literal in the extraction path
# matching one of these to 0.1%. NOTE the residual limitation, disclosed in gate_A():
# a value reached by ARITHMETIC on allowed literals is not literal-caught — the
# structural guarantee is the no-scale-import invariant, not literal-hunting.
_FORBIDDEN_MAGNITUDES = {
    "OMEGA_C": OMEGA_C,
    "M_E": M_E,
    "L_CELL": L_CELL,
    "C_CELL": C_CELL,
}


def _json_default(o):
    """Coerce numpy scalars/arrays to native JSON types."""
    if isinstance(o, np.bool_):
        return bool(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.floating):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"not JSON serializable: {type(o).__name__}")


# ═════════════════════════════════════════════════════════════════════════════
# G-A — anti-install gate (AST scan of the extraction path)
# ═════════════════════════════════════════════════════════════════════════════
def scan_forbidden_inputs(source: str) -> dict:
    """AST-scan `source` for forbidden physical-scale inputs in the CODE (not in
    docstrings/comments — AST excludes those). Returns the offenders found.

    Forbidden: any Name/Attribute id in {OMEGA_C, M_E, L_CELL, C_CELL}; any
    `from ave.core.constants import ...` (the extraction path must import no scale);
    and any numeric LITERAL matching a forbidden magnitude to 0.1% (review R8, the
    symbol scan is blind to a hard-coded value). AST excludes docstrings/comments.
    This is the machine-checkable #613 anti-install lesson.
    """
    tree = ast.parse(source)
    name_hits: list[str] = []
    import_hits: list[str] = []
    literal_hits: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and node.id in _FORBIDDEN:
            name_hits.append(node.id)
        elif isinstance(node, ast.Attribute) and node.attr in _FORBIDDEN:
            name_hits.append(node.attr)
        elif isinstance(node, ast.ImportFrom) and node.module == "ave.core.constants":
            import_hits.append("ave.core.constants:" + ",".join(a.name for a in node.names))
        elif (
            isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and not isinstance(node.value, bool)
        ):
            v = abs(float(node.value))
            if v > 0.0:
                for nm, mag in _FORBIDDEN_MAGNITUDES.items():
                    if abs(v - mag) / mag < 1e-3:
                        literal_hits.append(f"{nm}~{node.value}")
    return {
        "name_hits": sorted(set(name_hits)),
        "import_hits": sorted(set(import_hits)),
        "literal_hits": sorted(set(literal_hits)),
    }


def gate_A() -> dict:
    hits = scan_forbidden_inputs(_EXTRACTION_MODULE.read_text())
    clean = not hits["name_hits"] and not hits["import_hits"] and not hits["literal_hits"]
    return {
        "gate": "G-A anti-install",
        "module_scanned": str(_EXTRACTION_MODULE.relative_to(_HERE.parents[3])),
        "forbidden_set": sorted(_FORBIDDEN),
        "name_hits": hits["name_hits"],
        "import_hits": hits["import_hits"],
        "literal_hits": hits["literal_hits"],
        "limitation_disclosed": (
            "symbol + import + numeric-literal scan (review R8). NOT caught: a value "
            "reached by ARITHMETIC on allowed literals. The structural guarantee is "
            "the no-scale-import invariant + the dimensionless-cancellation proof "
            "(derivation §5), not literal-hunting."
        ),
        "pass": clean,
    }


def gate_A_planted() -> dict:
    """Planted-violation proof: (1) an extraction snippet that references OMEGA_C by
    symbol AND (2) one that hard-codes omega_C's numeric VALUE (review R8) must both
    be flagged by the same scanner (proves G-A can fire on symbol AND literal)."""
    bad_symbol = (
        "from ave.core.constants import OMEGA_C\n"
        "def bad_extract(f):\n"
        "    return OMEGA_C  # installed scale — the #613 error\n"
    )
    # build the plant from the imported symbol (no magic number in this file)
    bad_literal = f"def bad_extract(f):\n    return 1.0 / {OMEGA_C!r}  # hard-coded omega_C value\n"
    h1 = scan_forbidden_inputs(bad_symbol)
    h2 = scan_forbidden_inputs(bad_literal)
    fired_symbol = bool(h1["name_hits"]) and bool(h1["import_hits"])
    fired_literal = bool(h2["literal_hits"])
    return {
        "planted": "G-A: OMEGA_C by symbol AND by numeric literal",
        "symbol_hits": h1["name_hits"] + h1["import_hits"],
        "literal_hits": h2["literal_hits"],
        "gate_fired": fired_symbol and fired_literal,
        "pass": fired_symbol and fired_literal,  # both plants MUST fire
    }


# ═════════════════════════════════════════════════════════════════════════════
# G-B — independent-reference recovery (vs FROZEN #604)
# Review R3: the OLD G-B read g_scalar(0.0), which hits the memoryless early-return
# (theta=pi) — the loaded dispersion solver was NEVER exercised, so the gate was
# effectively unfireable (float roundoff of pi*sqrt3 computed two ways). The gate
# now DRIVES the loaded solver at a small NONZERO f (the full coarse+fine crossing
# scan runs) and asserts it CONVERGES to the FROZEN #604 top pi*sqrt3.
# ═════════════════════════════════════════════════════════════════════════════
G_B_PROBE_F = 1e-5  # small but nonzero: exercises the loaded solver, no early return
G_B_CONVERGE_TOL = 1e-4  # loaded solver must converge to pi*sqrt3 within this


def gate_B() -> dict:
    g_probe = jp.g_scalar(G_B_PROBE_F)  # LOADED solver at small f (no early return)
    rel = abs(g_probe - REF_604_BAND_TOP_OVER_OMEGA_C) / REF_604_BAND_TOP_OVER_OMEGA_C
    # separately record the exact memoryless identity (the f=0 closed form)
    g0_identity = jp.g_scalar(0.0)
    return {
        "gate": "G-B independent-reference recovery",
        "reference_source": REF_604_DOC,
        "reference_value_over_omega_C": REF_604_BAND_TOP_OVER_OMEGA_C,
        "loaded_solver_probe_f": G_B_PROBE_F,
        "loaded_solver_probe_over_omega_C": g_probe,
        "memoryless_identity_f0_over_omega_C": g0_identity,
        "rel_error": rel,
        "tol": G_B_CONVERGE_TOL,
        "pass": rel < G_B_CONVERGE_TOL,
    }


def gate_B_planted() -> dict:
    """Planted-violation proof: a perturbed loaded-solver output (offset) must FAIL
    the reference-convergence tolerance (proves G-B can fire)."""
    perturbed = jp.g_scalar(G_B_PROBE_F) * 1.01  # 1% off the loaded value
    rel = abs(perturbed - REF_604_BAND_TOP_OVER_OMEGA_C) / REF_604_BAND_TOP_OVER_OMEGA_C
    return {
        "planted": "G-B: loaded-solver output offset by +1%",
        "perturbed_over_omega_C": perturbed,
        "rel_error": rel,
        "tol": G_B_CONVERGE_TOL,
        "gate_fired": rel >= G_B_CONVERGE_TOL,
        "pass": rel >= G_B_CONVERGE_TOL,  # the gate MUST fail (fire) on the plant
    }


# ═════════════════════════════════════════════════════════════════════════════
# G-C — vertex-extent honesty + frozen branch assignment
# ═════════════════════════════════════════════════════════════════════════════
def _classify_branch(g_f0: float, g_fstar: float, g_f5: float) -> str:
    ref = REF_604_BAND_TOP_OVER_OMEGA_C
    swing = abs(g_f0 - g_f5) / ref
    dev_star = abs(g_fstar - ref) / ref
    if dev_star < BRANCH_I_TOL and swing < BRANCH_I_SWING:
        return "i"  # walk clock == vertex clock (X33 two-clock closes in-engine)
    if swing > BRANCH_III_SWING:
        return "iii"  # extent-dominated: not closable at TL abstraction
    if swing < BRANCH_I_SWING and dev_star >= BRANCH_I_TOL:
        return "ii"  # a new definite derived scale
    return "indeterminate"


def gate_C(s_L: float = 1.0, s_C: float = 1.0) -> dict:
    g0 = jp.g_scalar(0.0, s_L, s_C)
    gstar = jp.g_scalar(F_STAR, s_L, s_C)
    g5 = jp.g_scalar(0.5, s_L, s_C)
    swing = abs(g0 - g5) / REF_604_BAND_TOP_OVER_OMEGA_C
    branch = _classify_branch(g0, gstar, g5)
    return {
        "gate": "G-C vertex-extent honesty",
        "note": "canon fixes NO transverse bond scale; f not canonically pinned",
        "s_L": s_L,
        "s_C": s_C,
        "g_f0_over_omega_C": g0,
        "g_fstar_over_omega_C": gstar,
        "f_star": F_STAR,
        "swing_over_pi_sqrt3": swing,
        "branch_iii_threshold": BRANCH_III_SWING,
        "branch_fired": branch,
        "pass": True,  # G-C reports; the swing is a first-class result, not a pass/fail
    }


def gate_C_planted() -> dict:
    """Planted-violation proof of the extent-dominated DETECTOR: a synthetic
    f-INDEPENDENT ceiling must NOT be flagged extent-dominated; the real
    f-DEPENDENT ceiling MUST be. Proves the detector discriminates (can fire)."""
    ref = REF_604_BAND_TOP_OVER_OMEGA_C
    # control: flat ceiling -> swing 0 -> NOT extent-dominated
    flat_swing = abs(ref - ref) / ref
    flat_flagged = flat_swing > BRANCH_III_SWING
    # real: the true loaded ceiling -> large swing -> extent-dominated
    real_swing = abs(jp.g_scalar(0.0) - jp.g_scalar(0.5)) / ref
    real_flagged = real_swing > BRANCH_III_SWING
    return {
        "planted": "G-C detector: flat (control) must NOT flag; real must flag",
        "flat_swing": flat_swing,
        "flat_flagged_extent_dominated": flat_flagged,
        "real_swing": real_swing,
        "real_flagged_extent_dominated": real_flagged,
        "gate_fired": (not flat_flagged) and real_flagged,
        "pass": (not flat_flagged) and real_flagged,
    }


# ═════════════════════════════════════════════════════════════════════════════
# Sweep + figure
# ═════════════════════════════════════════════════════════════════════════════
def run_sweep(s_L: float = 1.0, s_C: float = 1.0) -> dict:
    fs = jp.vertex_extent_sweep(26)
    g_exact = np.array([jp.g_scalar(f, s_L, s_C) for f in fs])  # combined channel
    g_shunt = np.array([jp.g_scalar(f, 0.0, s_C) for f in fs])  # pure accumulator
    g_series = np.array([jp.g_scalar(f, s_L, 0.0) for f in fs])  # pure throat
    g_lin = np.array([jp.g_scalar_linear(f, s_L, s_C) for f in fs])  # single-channel anchor
    w_vertex = np.array([jp.extract_vertex_circuit(f, s_L, s_C).omega_vertex_over_omega_C for f in fs])
    return {
        "f": fs.tolist(),
        "g_exact_over_omega_C": g_exact.tolist(),
        "g_pure_shunt_over_omega_C": g_shunt.tolist(),
        "g_pure_series_over_omega_C": g_series.tolist(),
        "g_single_channel_anchor_over_omega_C": g_lin.tolist(),
        # f=0 -> point junction -> no resonance (inf); emit null for strict JSON
        "omega_vertex_over_omega_C": [None if not np.isfinite(w) else float(w) for w in w_vertex],
    }


def make_figure(sweep: dict, s_L: float, s_C: float) -> Path:
    style.apply("print")
    fs = np.array(sweep["f"])
    g_exact = np.array(sweep["g_exact_over_omega_C"])
    g_shunt = np.array(sweep["g_pure_shunt_over_omega_C"])
    g_series = np.array(sweep["g_pure_series_over_omega_C"])
    w_vertex = np.array(sweep["omega_vertex_over_omega_C"], dtype=float)
    ref = REF_604_BAND_TOP_OVER_OMEGA_C

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11.0, 4.4))

    # Panel A: the connected-band ceiling vs extent (the deliverable), with the
    # channel decomposition showing both accumulator + throat LOWER the ceiling
    # and the combined case tracks the STRONGER (series) channel (non-additive).
    axL.plot(
        fs,
        g_exact,
        color=style.COLORS["ave"],
        lw=2.4,
        marker="o",
        ms=3,
        label=r"ceiling $g(f)$: combined ($s_L{=}s_C{=}1$)",
    )
    axL.plot(fs, g_series, color=style.COLORS["comparison"], lw=1.5, ls="--", label=r"pure throat $s_L{=}1$")
    axL.plot(fs, g_shunt, color=style.COLORS["accent"], lw=1.5, ls="-.", label=r"pure accumulator $s_C{=}1$")
    axL.axhline(ref, color=style.COLORS["data"], lw=1.2, ls=":", label=r"memoryless #604 top $\pi\sqrt{3}$")
    axL.axhspan(
        ref * (1 - BRANCH_III_SWING),
        ref,
        color=style.COLORS["muted"],
        alpha=0.12,
        label="branch-(i) robust band (<10%)",
    )
    axL.axvline(F_STAR, color=style.COLORS["muted"], lw=1.0, ls="-.", label=r"Wigner–Seitz probe $f{=}0.5$")
    axL.set_xlabel(style.axis_label("Vertex extent", "f = d/\\ell_{node}", ""))
    axL.set_ylabel(style.axis_label("Band ceiling", "g = \\omega_{top}/\\omega_C", ""))
    axL.set_xlim(0, 0.5)
    axL.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), frameon=False, fontsize=8)

    # Panel B: the junction LC self-resonance vs the memoryless top (crossover)
    axR.plot(
        fs[1:],
        w_vertex[1:],
        color=style.COLORS["comparison"],
        lw=2.2,
        label=r"junction $\omega_{vertex}/\omega_C = 1/(\sqrt{s_L s_C}\,f)$",
    )
    axR.axhline(ref, color=style.COLORS["data"], lw=1.2, ls=":", label=r"memoryless top $\pi\sqrt{3}$")
    f_crit = 1.0 / (np.pi * np.sqrt(3.0) * np.sqrt(s_L * s_C))
    axR.axvline(
        f_crit, color=style.COLORS["muted"], lw=1.0, ls="-.", label=rf"crossover $f_{{crit}}\approx{f_crit:.3f}$"
    )
    axR.set_xlabel(style.axis_label("Vertex extent", "f = d/\\ell_{node}", ""))
    axR.set_ylabel(style.axis_label("Junction self-resonance", "\\omega_{vertex}/\\omega_C", ""))
    axR.set_xlim(0, 0.5)
    axR.set_ylim(0, 12)
    axR.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), frameon=False, fontsize=8)

    out = _OUT / "x37_junction_parasitics.png"
    style.save(fig, out, strict=True)
    plt.close(fig)
    return out


# ═════════════════════════════════════════════════════════════════════════════
# First-class disclosures demanded by the adversarial review (R2 / R4 / R5)
# ═════════════════════════════════════════════════════════════════════════════
def shape_factor_bracket(f: float = 0.5, s_grid=(0.3, 0.5, 1.0, 2.0, 3.0)) -> dict:
    """R5: the ceiling at f=0.5 is DOUBLY conditional (f<=0.5 AND s=1). Sweep
    s_L,s_C over [0.3,3]^2 and report the bracket floor/ceiling of g(0.5)."""
    vals = [jp.g_scalar(f, sL, sC) for sL in s_grid for sC in s_grid]
    return {"f": f, "s_grid": list(s_grid), "g_min": float(min(vals)), "g_max": float(max(vals))}


def reciprocity_identity(s_grid=None) -> dict:
    """R4: at s_L=s_C=1 the combined ceiling EQUALS the pure-throat ceiling EXACTLY
    (the shunt accumulator has ZERO effect on every reported g(f)). Report the max
    deviation over the extent sweep to make the identity explicit."""
    fs = jp.vertex_extent_sweep(26)
    dev = max(abs(jp.g_scalar(f, 1.0, 1.0) - jp.g_scalar(f, 1.0, 0.0)) for f in fs)
    return {"max_abs_combined_minus_pure_throat": float(dev), "identity": bool(dev < 1e-9)}


def one_d_cross_check() -> dict:
    """R2: ship the 1D two-node closed-form cross-check the prereg §3.4 promised.
    g_1d in omega_C units (no sqrt(3) network factor); f=0 -> pi."""
    return {
        "note": "1D (z=2) loaded line, closed-form cos(k a) transfer-matrix trace",
        "g_1d_f0": jp.band_top_1d(0.0),
        "g_1d_f0.2_combined": jp.band_top_1d(0.2, 1.0, 1.0),
        "g_1d_f0.2_pure_shunt": jp.band_top_1d(0.2, 0.0, 1.0),
        "g_1d_f0.5_combined": jp.band_top_1d(0.5, 1.0, 1.0),
        "memoryless_pi": float(np.pi),
    }


def lift_detector_selftest() -> dict:
    """R3: prove the topology detector CAN report a lift — a non-passive
    (negative-reactance) loading lifts the ceiling above memoryless and is reported
    as a bypass (the old [0,pi]-clipped detector could only ever say 'transparent')."""
    passive = jp.band_ceiling_diagnosis(0.2, 1.0, 1.0)["status"]
    lift = jp.band_ceiling_diagnosis(0.2, -1.0, -1.0)["status"]
    return {
        "passive_positive_status": passive,
        "planted_negative_status": lift,
        "lift_is_reachable": bool(lift == "lift"),
        "pass": bool(passive == "low-pass" and lift == "lift"),
    }


# ═════════════════════════════════════════════════════════════════════════════
# main
# ═════════════════════════════════════════════════════════════════════════════
def main() -> None:
    s_L, s_C = 1.0, 1.0  # equivalent-length normalization (flagged modeling choice)

    gA, gA_p = gate_A(), gate_A_planted()
    gB, gB_p = gate_B(), gate_B_planted()
    gC, gC_p = gate_C(s_L, s_C), gate_C_planted()
    bracket = shape_factor_bracket()
    reciprocity = reciprocity_identity()
    one_d = one_d_cross_check()
    lift_selftest = lift_detector_selftest()

    sweep = run_sweep(s_L, s_C)
    fig_path = make_figure(sweep, s_L, s_C)

    branch = gC["branch_fired"]
    top_class = jp.topology_class(F_STAR, s_L, s_C)
    vc = jp.extract_vertex_circuit(F_STAR, s_L, s_C)

    result = {
        "task": "X37 junction-parasitic extraction (scalar/compression, Phase 1)",
        "class": "MIXED: g VALUE derived-geometric; SCALE omega_C dimensional-forced/identity",
        "reference_604": {
            "doc": REF_604_DOC,
            "band_top_over_omega_C": REF_604_BAND_TOP_OVER_OMEGA_C,
            "band_top_MeV": REF_604_BAND_TOP_OVER_OMEGA_C * MEV_PER_OMEGA_C,
        },
        "shape_factors": {
            "s_L": s_L,
            "s_C": s_C,
            "note": "equivalent-length normalization; s needs a transverse "
            "bond scale canon does not provide (flagged)",
        },
        "vertex_equivalent_circuit_at_f_star": {
            "f_star": F_STAR,
            "L_j_over_Lprime_ell (=s_L f)": vc.L_j_over_Lprime_ell,
            "C_j_over_Cprime_ell (=s_C f)": vc.C_j_over_Cprime_ell,
            "omega_vertex_over_omega_C": vc.omega_vertex_over_omega_C,
            "topology_class": top_class,
        },
        "g_scalar": {
            "f0": jp.g_scalar(0.0, s_L, s_C),
            "f_star": jp.g_scalar(F_STAR, s_L, s_C),
            "f0_MeV": jp.g_scalar(0.0, s_L, s_C) * MEV_PER_OMEGA_C,
            "f_star_MeV": jp.g_scalar(F_STAR, s_L, s_C) * MEV_PER_OMEGA_C,
            "kappa_s_L+2/3_s_C": s_L + (2.0 / 3.0) * s_C,
        },
        "branch_fired": branch,
        "gates": {"G-A": gA, "G-A_planted": gA_p, "G-B": gB, "G-B_planted": gB_p, "G-C": gC, "G-C_planted": gC_p},
        "disclosures": {
            "R5_shape_factor_bracket": bracket,
            "R4_reciprocity_identity": reciprocity,
            "R2_one_d_cross_check": one_d,
            "R3_lift_detector_selftest": lift_selftest,
        },
        "sweep": sweep,
        "figure": str(fig_path.relative_to(_HERE.parents[3])),
    }

    out_json = _OUT / "x37_junction_parasitics.json"
    out_json.write_text(json.dumps(result, indent=2, default=_json_default))

    # ── ledger to stdout ──
    print("=" * 78)
    print("X37 — junction-parasitic extraction (scalar/compression, Phase 1)")
    print("=" * 78)
    print(
        f"  #604 memoryless top   : {REF_604_BAND_TOP_OVER_OMEGA_C:.6f} omega_C "
        f"({REF_604_BAND_TOP_OVER_OMEGA_C*MEV_PER_OMEGA_C:.4f} MeV)  [{REF_604_DOC}]"
    )
    print(f"  topology class        : {top_class}")
    print(
        f"  vertex circuit @f*={F_STAR}: L_j={vc.L_j_over_Lprime_ell:.3f} mu_0 ell, "
        f"C_j={vc.C_j_over_Cprime_ell:.3f} eps_0 ell, omega_vertex={vc.omega_vertex_over_omega_C:.3f} omega_C"
    )
    print(f"  g_scalar(f=0)         : {jp.g_scalar(0.0,s_L,s_C):.6f} omega_C  (memoryless identity)")
    print(f"  g_scalar(f*=0.5)      : {jp.g_scalar(F_STAR,s_L,s_C):.6f} omega_C  (s=1)")
    print(f"  extent swing [0,0.5]  : {gC['swing_over_pi_sqrt3']*100:.1f}% of pi*sqrt3")
    print(f"  BRANCH FIRED          : ({branch})")
    print("-" * 78)
    print("  DISCLOSURES (adversarial review):")
    print(
        f"   R5 bracket g(0.5), s in [0.3,3]^2 : [{bracket['g_min']:.3f}, {bracket['g_max']:.3f}] omega_C "
        f"(DOUBLY conditional: f<=0.5 AND s=1)"
    )
    print(
        f"   R4 reciprocity: max|combined - pure-throat| = {reciprocity['max_abs_combined_minus_pure_throat']:.2e} "
        f"(shunt has ZERO effect at s=1: {reciprocity['identity']})"
    )
    print(
        f"   R2 1D cross-check g_1d(f=0)={one_d['g_1d_f0']:.4f} (=pi), "
        f"combined f=0.2 -> {one_d['g_1d_f0.2_combined']:.4f}, f=0.5 -> {one_d['g_1d_f0.5_combined']:.4f}"
    )
    print(
        f"   R3 lift-detector self-test: passive={lift_selftest['passive_positive_status']}, "
        f"planted-neg={lift_selftest['planted_negative_status']} (lift reachable: {lift_selftest['lift_is_reachable']})"
    )
    print("-" * 78)
    for g in (gA, gA_p, gB, gB_p, gC, gC_p):
        label = g.get("gate", g.get("planted"))
        print(f"  [{'PASS' if g['pass'] else 'FAIL'}] {label}")
    print("-" * 78)
    print(f"  JSON  : {out_json}")
    print(f"  FIG   : {fig_path}")

    assert all(g["pass"] for g in (gA, gA_p, gB, gB_p, gC, gC_p)), "a gate failed"
    assert lift_selftest["pass"], "lift-detector self-test failed (R3)"


if __name__ == "__main__":
    main()

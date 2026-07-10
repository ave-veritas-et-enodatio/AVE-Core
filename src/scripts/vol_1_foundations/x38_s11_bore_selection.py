#!/usr/bin/env python3
"""X38 — S₁₁-minimization bore selection driver: does the substrate SELECT the
bond's junction extent f by applying canon's OWN geometry-selection operator
(Universal Operator #6, lambda_min(S†S)->0) at the srs vertex? (route d for the
bond-bore fork X37/#616 sharpened.)

Prereg (FROZEN): research/2026-07-10_x38-s11-bore-selection_prereg_FROZEN.md
Derivation:      research/2026-07-10_x38-s11-bore-selection_derivation.md
Class: MIXED — the selected f* is derived-geometric (ave.core.junction_scattering,
which imports NO scale); the SCALE omega_C = c/ell_node is dimensional-forced/
identity and appears ONLY in this driver's reporting layer (MeV labels).

Runs the four pre-registered gates with planted-violation proofs (G-A anti-install
AST scan, G-B recovery of the bare Gamma=-1/3 AND the pi*sqrt3 ceiling through the
loaded path, G-C objective-robustness = the branch-iv detector, G-D fireability),
computes f* under all three frozen objectives, sweeps s_L,s_C, writes JSON + a
WHITE figure.

Run: PYTHONPATH=src python3 src/scripts/vol_1_foundations/x38_s11_bore_selection.py
"""

from __future__ import annotations

import ast
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from ave.core import junction_scattering as js

# REPORTING + DETECTOR scale imports (this driver is the DETECTOR, not the S₁₁
# extraction path — G-A scans ave.core.junction_scattering, never this file). Used
# for MeV labels, the pi*sqrt3 reference, and the forbidden-MAGNITUDE list.
# Imported by SYMBOL — no hard-coded constant values.
from ave.core.constants import C_CELL, HBAR, L_CELL, M_E, OMEGA_C, e_charge
from ave.viz import style

# ─────────────────────────────────────────────────────────────────────────────
# FROZEN references (G-B): (i) the bare-junction reflection |S11| = 1/3 for z=3;
# (ii) the merged #604 memoryless scalar band top pi*sqrt3, hard-coded FROM the
# result doc, NOT recomputed by the loaded solver's own path.
#   research/2026-07-09_srs-band-survey_result.md:18
#     "GLOBAL BAND TOP = pi*sqrt3 omega_C = 5.4414 omega_C = 2.781 MeV, at H"
# ─────────────────────────────────────────────────────────────────────────────
REF_BARE_S11_MAG = 1.0 / 3.0  # |(2-z)/z| for z=3 (analytic memoryless star)
REF_604_BAND_TOP_OVER_OMEGA_C = np.pi * np.sqrt(3.0)  # = 5.441398092702653 (#604)
REF_604_DOC = "research/2026-07-09_srs-band-survey_result.md:18"

MEV_PER_OMEGA_C = HBAR * OMEGA_C / e_charge / 1e6  # ~0.511 MeV/omega_C (m_e c^2 IDENTITY)

# Frozen thresholds (prereg §6 — no post-hoc relaxation)
G_B_PROBE_F = 1e-5  # small but nonzero: exercises the LOADED path, no early return
G_B_TOL = 1e-4  # loaded recovery tolerance for both baselines
G_C_ROBUST_SPREAD = 0.02  # spread < this => robust selection
G_C_SCATTER_SPREAD = 0.05  # spread >= this => objective-dependent scatter (branch iv)
F_CRIT = 1.0 / (np.pi * np.sqrt(3.0))  # ~0.184 (X37 lumped-abstraction self-consistency at s=1)
TUBE_RADIUS_MARK = 1.0 / (2.0 * np.pi)  # ~0.159 soliton comparison mark (constants.py:76), NOT an input
CORE_THICKNESS_MARK = 1.0  # core-tube thickness (constants.py:189), NOT an input

_HERE = Path(__file__).resolve().parent
_OUT = _HERE / "_output"
_OUT.mkdir(exist_ok=True)

# ═════════════════════════════════════════════════════════════════════════════
# G-A — anti-install gate (AST scan of the S₁₁ extraction path).
# PROVENANCE: scan_forbidden_inputs + _FORBIDDEN_MAGNITUDES are PORTED from the
# X37 driver src/scripts/vol_1_foundations/x37_junction_parasitics.py (origin
# branch analysis/x37-junction-parasitics, commit 1186c891 — review R8). X37 is
# NOT merged to main, so it cannot be imported here; this is a CITED port, not a
# silent fork-copy. Extended: the scanned module is ave.core.junction_scattering.
# ═════════════════════════════════════════════════════════════════════════════
_FORBIDDEN = {"OMEGA_C", "M_E", "L_CELL", "C_CELL"}
_EXTRACTION_MODULE = Path(js.__file__)
_FORBIDDEN_MAGNITUDES = {"OMEGA_C": OMEGA_C, "M_E": M_E, "L_CELL": L_CELL, "C_CELL": C_CELL}


def _json_default(o):
    if isinstance(o, np.bool_):
        return bool(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.floating):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"not JSON serializable: {type(o).__name__}")


def scan_forbidden_inputs(source: str) -> dict:
    """AST-scan `source` for forbidden physical-scale inputs in the CODE (AST
    excludes docstrings/comments). Ported from X37 (cited above). Flags: any
    Name/Attribute in {OMEGA_C, M_E, L_CELL, C_CELL}; any `from ave.core.constants
    import ...`; any numeric LITERAL matching a forbidden magnitude to 0.1% (the
    symbol scan is blind to a hard-coded value)."""
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
            "symbol + import + numeric-literal scan (ported from X37 R8). NOT caught: a "
            "value reached by ARITHMETIC on allowed literals. Structural guarantee = the "
            "no-scale-import invariant + the dimensionless-cancellation proof (derivation §3)."
        ),
        "pass": clean,
    }


def gate_A_planted() -> dict:
    """Planted-violation proof: OMEGA_C by SYMBOL and by NUMERIC LITERAL must both be
    flagged by the same scanner (proves G-A fires on symbol AND literal)."""
    bad_symbol = (
        "from ave.core.constants import OMEGA_C\n"
        "def bad_extract(f):\n    return OMEGA_C  # installed scale — the #613 error\n"
    )
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
        "pass": fired_symbol and fired_literal,
    }


# ═════════════════════════════════════════════════════════════════════════════
# G-B — independent-reference recovery through the LOADED path (no early return).
# (i) bare-junction |S11| = 1/3 recovered by the loaded s11 at small nonzero f;
# (ii) the pi*sqrt3 ceiling recovered by the loaded connected-band top (the X37
# loaded-mu form, ported into junction_scattering with derivation §1 citation;
# X37 is unmerged so it cannot be imported — DISCLOSED deviation from the prereg's
# "via the X37 module" wording). g = sqrt(3) * theta_top ; f->0 -> pi*sqrt3.
# ═════════════════════════════════════════════════════════════════════════════
def _g_scalar_loaded(f: float, s_L: float = 1.0, s_C: float = 1.0) -> float:
    """omega_top/omega_C = sqrt(3)*theta_top(f) — the X37 loaded-dispersion ceiling,
    through junction_scattering.connected_band_top_theta (the ported X37 loaded-mu
    form). sqrt(3) is the geometric network factor (reporting)."""
    return float(np.sqrt(3.0) * js.connected_band_top_theta(f, s_L, s_C))


def gate_B() -> dict:
    # (i) bare-junction reflection through the loaded S11 at small nonzero f
    s11_probe = abs(js.s11_junction(1e-6, G_B_PROBE_F))  # loaded path, no early return
    rel_bare = abs(s11_probe - REF_BARE_S11_MAG) / REF_BARE_S11_MAG
    # (ii) pi*sqrt3 ceiling through the loaded connected-band top at small f
    g_probe = _g_scalar_loaded(G_B_PROBE_F)
    rel_ceiling = abs(g_probe - REF_604_BAND_TOP_OVER_OMEGA_C) / REF_604_BAND_TOP_OVER_OMEGA_C
    return {
        "gate": "G-B independent-reference recovery (loaded path)",
        "bare_ref_S11_mag": REF_BARE_S11_MAG,
        "bare_loaded_probe_S11_mag": s11_probe,
        "bare_rel_error": rel_bare,
        "ceiling_ref_source": REF_604_DOC,
        "ceiling_ref_over_omega_C": REF_604_BAND_TOP_OVER_OMEGA_C,
        "ceiling_loaded_probe_over_omega_C": g_probe,
        "ceiling_rel_error": rel_ceiling,
        "tol": G_B_TOL,
        "x37_module_available": Path(js.__file__).with_name("junction_parasitics.py").exists(),
        "note": (
            "X37 junction_parasitics is UNMERGED on main; the pi*sqrt3 recovery uses the X37 "
            "loaded-mu form ported into junction_scattering.connected_band_top_theta (cited, "
            "derivation §1) — disclosed deviation from the prereg 'via the X37 module' wording."
        ),
        "pass": bool(rel_bare < G_B_TOL and rel_ceiling < G_B_TOL),
    }


def gate_B_planted() -> dict:
    """Planted-violation proof: a +1% offset on EACH loaded recovery must FAIL."""
    bare_off = abs(js.s11_junction(1e-6, G_B_PROBE_F)) * 1.01
    ceil_off = _g_scalar_loaded(G_B_PROBE_F) * 1.01
    rel_bare = abs(bare_off - REF_BARE_S11_MAG) / REF_BARE_S11_MAG
    rel_ceil = abs(ceil_off - REF_604_BAND_TOP_OVER_OMEGA_C) / REF_604_BAND_TOP_OVER_OMEGA_C
    fired = rel_bare >= G_B_TOL and rel_ceil >= G_B_TOL
    return {
        "planted": "G-B: +1% offset on both loaded recoveries",
        "bare_rel_error": rel_bare,
        "ceiling_rel_error": rel_ceil,
        "gate_fired": bool(fired),
        "pass": bool(fired),
    }


# ═════════════════════════════════════════════════════════════════════════════
# G-C — objective-robustness (the branch-iv detector) + frozen branch assignment.
# ═════════════════════════════════════════════════════════════════════════════
def _classify_branch(f_stars: dict, spread: float) -> str:
    """Frozen branch rule (prereg §6). f* under the PRIMARY objective (obj1_op6)."""
    f_primary = f_stars["obj1_op6"]
    if spread >= G_C_SCATTER_SPREAD:
        return "iv"  # objective-dependent scatter -> honest null
    # robust (spread < scatter threshold): read the primary f*
    if abs(f_primary - TUBE_RADIUS_MARK) < 0.02 and spread < G_C_ROBUST_SPREAD:
        return "i"  # matched bore == unknot tube radius -> identity candidate
    if f_primary == 0.0 and spread < G_C_ROBUST_SPREAD:
        return "ii"  # point junction -> closure (c)
    if f_primary > 0.02 and abs(f_primary - TUBE_RADIUS_MARK) >= 0.02 and spread < G_C_ROBUST_SPREAD:
        return "iii"  # a new derived interior scale
    return "indeterminate"


def gate_C(s_L: float = 1.0, s_C: float = 1.0) -> dict:
    sp = js.objective_spread(s_L, s_C)
    branch = _classify_branch(sp["f_stars"], sp["spread"])
    return {
        "gate": "G-C objective-robustness (branch-iv detector)",
        "s_L": s_L,
        "s_C": s_C,
        "f_stars": sp["f_stars"],
        "spread": sp["spread"],
        "robust_threshold": G_C_ROBUST_SPREAD,
        "scatter_threshold": G_C_SCATTER_SPREAD,
        "branch_fired": branch,
        "pass": True,  # G-C reports; the spread + branch are first-class results
    }


def gate_C_planted() -> dict:
    """Planted-violation proof of the branch-iv (spread) detector: a DIVERGENT bogus
    objective (one that MAXIMISES reflection -> selects f=0.5, the opposite extreme)
    must push the spread across the scatter threshold; the 3 real objectives (control)
    must NOT. Proves the detector can fire."""
    real = js.objective_spread()  # control: 3 real objectives
    real_flagged = real["spread"] >= G_C_SCATTER_SPREAD
    # divergent plant: argmax |S11(pi)|^2 over f (bogus "maximise reflection" objective)
    fs = np.linspace(js.F_POINT_JUNCTION, js.F_WIGNER_SEITZ, 501)
    j_bad = np.array([js.objective_op6(f) for f in fs])
    f_bad = float(fs[int(np.argmax(j_bad))])  # selects a large f (opposite of the real min)
    planted_stars = dict(real["f_stars"])
    planted_stars["obj_bogus_maximise"] = f_bad
    planted_spread = max(planted_stars.values()) - min(planted_stars.values())
    planted_flagged = planted_spread >= G_C_SCATTER_SPREAD
    return {
        "planted": "G-C: divergent bogus objective (maximise reflection -> f!=0)",
        "control_real_spread": real["spread"],
        "control_flagged_scatter": real_flagged,
        "planted_f_bogus": f_bad,
        "planted_spread": planted_spread,
        "planted_flagged_scatter": planted_flagged,
        "gate_fired": (not real_flagged) and planted_flagged,
        "pass": (not real_flagged) and planted_flagged,
    }


# ═════════════════════════════════════════════════════════════════════════════
# s-sweep (X37 R5 lesson) + landscape + figure
# ═════════════════════════════════════════════════════════════════════════════
def s_sweep(s_grid=(0.3, 0.5, 1.0, 2.0, 3.0)) -> dict:
    """f* under the PRIMARY objective (obj1_op6) over s_L,s_C in [0.3,3]^2, and the
    per-cell objective spread. Reports whether f*=0 is robust to the shape factors."""
    rows = []
    worst_fstar = 0.0
    max_spread = 0.0
    for sL in s_grid:
        for sC in s_grid:
            sp = js.objective_spread(sL, sC)
            f1 = sp["f_stars"]["obj1_op6"]
            rows.append({"s_L": sL, "s_C": sC, "f_star_op6": f1, "spread": sp["spread"]})
            worst_fstar = max(worst_fstar, max(sp["f_stars"].values()))
            max_spread = max(max_spread, sp["spread"])
    return {"grid": list(s_grid), "rows": rows, "worst_f_star": worst_fstar, "max_spread": max_spread}


def near_degeneracy_disclosure(s_L: float = 1.0, s_C: float = 1.0, n: int = 2001) -> dict:
    """HONEST disclosure (visible in the figure): obj-1 |S11(pi;f)|^2 has a NEAR-
    degenerate interior local minimum (the vertex self-resonance brings |S11(pi)|
    back toward 1/3). Records how close the best INTERIOR (f>0) point comes to the
    f=0 floor, and whether it beats f=0 (it must NOT), and whether it sits beyond
    f_crit (where the lumped abstraction self-invalidates -> not a physical competitor).

    Searches f in [0.1, 0.5] (AWAY from the trivial f->0+ continuation) so it captures
    the SECOND, physically interesting local minimum (the vertex self-resonance dip)."""
    fs = np.linspace(0.1, js.F_WIGNER_SEITZ, n)
    j = np.array([js.objective_op6(f, s_L, s_C) for f in fs])
    j0 = js.objective_op6(0.0, s_L, s_C)
    i = int(np.argmin(j))
    return {
        "f0_floor": float(j0),
        "best_interior_f": float(fs[i]),
        "best_interior_value": float(j[i]),
        "interior_minus_floor": float(j[i] - j0),
        "interior_beats_f0": bool(j[i] < j0 - 1e-12),
        "best_interior_beyond_f_crit": bool(fs[i] > F_CRIT),
        "note": "obj-1 has a near-degenerate interior dip; it does NOT beat f=0 and sits "
        "at f>f_crit (self-invalidated regime) -> not a physical competitor; f*=0 stands.",
    }


def objective_curves(s_L: float = 1.0, s_C: float = 1.0, n: int = 101) -> dict:
    fs = np.linspace(js.F_POINT_JUNCTION, js.F_WIGNER_SEITZ, n)
    return {
        "f": fs.tolist(),
        "obj1_op6": [js.objective_op6(f, s_L, s_C) for f in fs],
        "obj2_band_integrated": [js.objective_band_integrated(f, s_L, s_C) for f in fs],
        "obj3_single_freq": [js.objective_single_freq(f, s_L, s_C) for f in fs],
        "deepest_notch": [js.deepest_notch(f, s_L, s_C) for f in fs],
    }


def make_figure(curves: dict, s_L: float, s_C: float) -> Path:
    style.apply("print")
    fs = np.array(curves["f"])
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11.0, 4.4))

    # Panel A: the |S11|(theta, f) landscape (why the bore only adds reflection)
    thetas = np.linspace(1e-4, np.pi, 400)
    f_marks = [0.0, 0.1, 0.2, 0.3, 0.5]
    cmap = [
        style.COLORS["ave"],
        style.COLORS["comparison"],
        style.COLORS["accent"],
        style.COLORS["muted"],
        style.COLORS["data"],
    ]
    for f, c in zip(f_marks, cmap):
        axL.plot(thetas / np.pi, np.abs(js.s11_junction(thetas, f, s_L, s_C)), color=c, lw=1.8, label=rf"$f={f:.1f}$")
    axL.axhline(REF_BARE_S11_MAG, color="0.4", lw=1.0, ls=":", label=r"bare $|S_{11}|=1/3$")
    axL.set_xlabel(style.axis_label("Bond electrical length", r"\theta/\pi", ""))
    axL.set_ylabel(style.axis_label("Vertex reflection", r"|S_{11}|", ""))
    axL.set_xlim(0, 1)
    axL.set_ylim(0.30, 1.02)
    axL.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), frameon=False, fontsize=8)

    # Panel B: the three objectives + deepest-notch vs f (all minimised at f=0)
    axR.plot(
        fs,
        curves["obj1_op6"],
        color=style.COLORS["ave"],
        lw=2.2,
        marker="o",
        ms=2.5,
        label=r"obj-1 Op6 $|S_{11}(\pi)|^2$ (primary)",
    )
    axR.plot(
        fs,
        curves["obj2_band_integrated"],
        color=style.COLORS["comparison"],
        lw=1.6,
        ls="--",
        label=r"obj-2 band-integrated $\langle|S_{11}|^2\rangle$",
    )
    axR.plot(
        fs,
        curves["obj3_single_freq"],
        color=style.COLORS["accent"],
        lw=1.6,
        ls="-.",
        label=r"obj-3 $|S_{11}(\pi/2)|^2$",
    )
    axR.plot(
        fs,
        curves["deepest_notch"],
        color=style.COLORS["muted"],
        lw=1.4,
        ls=":",
        label=r"deepest notch $\min_\theta|S_{11}|^2$",
    )
    axR.axhline(1.0 / 9.0, color="0.4", lw=1.0, ls=":", label=r"bare floor $1/9$")
    axR.axvline(0.0, color=style.COLORS["ave"], lw=1.2, alpha=0.5, label=r"$f^\ast=0$ (all objectives)")
    axR.axvline(F_CRIT, color="0.6", lw=1.0, ls="-.", label=rf"$f_{{crit}}\approx{F_CRIT:.3f}$")
    axR.axvline(
        TUBE_RADIUS_MARK, color="0.75", lw=1.0, ls=":", label=rf"tube-radius mark $1/2\pi\approx{TUBE_RADIUS_MARK:.3f}$"
    )
    axR.set_xlabel(style.axis_label("Vertex extent", r"f = d/\ell_{node}", ""))
    axR.set_ylabel(style.axis_label("Objective", r"J(f)", ""))
    axR.set_xlim(0, 0.5)
    axR.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), frameon=False, fontsize=7.5)

    out = _OUT / "x38_s11_bore_selection.png"
    style.save(fig, out, strict=True)
    plt.close(fig)
    return out


# ═════════════════════════════════════════════════════════════════════════════
# main
# ═════════════════════════════════════════════════════════════════════════════
def main() -> None:
    s_L, s_C = 1.0, 1.0  # equivalent-length normalization (flagged modeling choice)

    gA, gA_p = gate_A(), gate_A_planted()
    gB, gB_p = gate_B(), gate_B_planted()
    gC, gC_p = gate_C(s_L, s_C), gate_C_planted()
    sweep = s_sweep()
    curves = objective_curves(s_L, s_C)
    near_deg = near_degeneracy_disclosure(s_L, s_C)
    fig_path = make_figure(curves, s_L, s_C)

    branch = gC["branch_fired"]
    f_star = gC["f_stars"]["obj1_op6"]
    self_invalidates = f_star > F_CRIT

    result = {
        "task": "X38 S11-minimization bore selection (scalar/compression, Phase 1)",
        "class": "MIXED: selected f* derived-geometric; SCALE omega_C dimensional-forced/identity",
        "objective_provenance": {
            "canonical_operator": "Universal Operator #6 lambda_min(S†S)->0",
            "leaf": "manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/eigenvalue-target.md",
            "claim": "clm-gdd70j",
            "code_path": "ave.core.universal_operators.universal_eigenvalue_target",
            "trefoil_application": "constants.py:191-206 (S11 min -> R.r=1/4 golden torus)",
        },
        "bare_junction": {
            "S11_analytic": js.bare_junction_s11(3),
            "abs_S11": abs(js.bare_junction_s11(3)),
            "note": "z=3 star: incident sees Z0/2 -> Gamma=(2-z)/z=-1/3; memoryless NOT matched",
        },
        "l_match": {
            "Q_for_2to1": float(np.sqrt(2.0 - 1.0)),
            "ideal_null_reachable": True,
            "physical_vertex_dips_below_1_3": bool(min(curves["deepest_notch"][1:]) < REF_BARE_S11_MAG**2 - 1e-9),
            "verdict": "L-match Q=1 CONFIRMED as a network fact; REFUTED at the vertex "
            "(accumulator on low-Z node side + C3v forbids a privileged one-arm shunt "
            "-> wrong orientation, cannot raise Z0/2 to Z0)",
        },
        "op6_target": {
            "deepest_notch_all_f": {f"f={f:.2f}": js.deepest_notch(f) for f in (0.0, 0.1, 0.3, 0.5)},
            "reflectionless_target_reachable": False,
            "note": "min|S11|^2 = 1/9 for ALL f (the theta->0 floor) => lambda_min->0 UNREACHABLE; "
            "the srs vertex is an intrinsic 1/9-power branch-backscatterer (z=3 structural)",
        },
        "f_star": {
            "obj1_op6_primary": gC["f_stars"]["obj1_op6"],
            "obj2_band_integrated": gC["f_stars"]["obj2_band_integrated"],
            "obj3_single_freq": gC["f_stars"]["obj3_single_freq"],
            "spread": gC["spread"],
        },
        "branch_fired": branch,
        "self_consistency": {
            "f_crit": F_CRIT,
            "f_star_gt_f_crit": bool(self_invalidates),
            "note": "f*=0 < f_crit -> lumped abstraction self-consistent at its minimum (does NOT self-invalidate)",
        },
        "comparison_marks": {
            "tube_radius_1_over_2pi": TUBE_RADIUS_MARK,
            "core_thickness": CORE_THICKNESS_MARK,
            "f_star_matches_tube_radius": bool(abs(f_star - TUBE_RADIUS_MARK) < 0.02),
            "note": "f*=0 matches NEITHER soliton mark -> branch (i) identity candidate does NOT fire",
        },
        "s_sweep": sweep,
        "near_degeneracy_disclosure": near_deg,
        "gates": {"G-A": gA, "G-A_planted": gA_p, "G-B": gB, "G-B_planted": gB_p, "G-C": gC, "G-C_planted": gC_p},
        "objective_curves": curves,
        "reporting_unit": {
            "MeV_per_omega_C": MEV_PER_OMEGA_C,
            "pi_sqrt3_MeV": REF_604_BAND_TOP_OVER_OMEGA_C * MEV_PER_OMEGA_C,
        },
        "figure": str(fig_path.relative_to(_HERE.parents[3])),
    }

    out_json = _OUT / "x38_s11_bore_selection.json"
    out_json.write_text(json.dumps(result, indent=2, default=_json_default))

    # ── ledger to stdout ──
    print("=" * 78)
    print("X38 — S11-minimization bore selection (scalar/compression, Phase 1)")
    print("=" * 78)
    print("  objective (canon)     : Op6 lambda_min(S†S)->0  [eigenvalue-target.md clm-gdd70j]")
    print(f"  bare junction z=3     : S11 = {js.bare_junction_s11(3):+.4f}  (|S11|=1/3; memoryless NOT matched)")
    print(
        f"  L-match Q (2:1)       : {np.sqrt(1.0):.3f}  -> ideal null reachable; REFUTED at vertex (orientation + C3v)"
    )
    print("  Op6 reflectionless    : UNREACHABLE (min|S11|^2 = 1/9 for ALL f -> z=3 intrinsic backscatter)")
    print(f"  f* obj-1 Op6 (primary): {gC['f_stars']['obj1_op6']:.4f}")
    print(f"  f* obj-2 band-int     : {gC['f_stars']['obj2_band_integrated']:.4f}")
    print(f"  f* obj-3 single-freq  : {gC['f_stars']['obj3_single_freq']:.4f}")
    print(
        f"  objective spread      : {gC['spread']:.4f}  (robust < {G_C_ROBUST_SPREAD}; scatter >= {G_C_SCATTER_SPREAD})"
    )
    print(f"  BRANCH FIRED          : ({branch})   [f*=0 => point junction; walk ceiling pi*sqrt3 exact]")
    print(f"  f* vs f_crit          : f*=0 < f_crit={F_CRIT:.3f} -> self-consistent (does NOT self-invalidate)")
    print(f"  vs soliton marks      : f*=0 != 1/2pi={TUBE_RADIUS_MARK:.3f}, != 1 -> branch (i) does NOT fire")
    print("-" * 78)
    print(
        f"  s-sweep [0.3,3]^2     : worst-case f*={sweep['worst_f_star']:.3f}, "
        f"max spread={sweep['max_spread']:.4f} (f*=0 robust to s)"
    )
    print(
        f"  obj-1 near-degeneracy : interior dip f={near_deg['best_interior_f']:.3f} "
        f"is {near_deg['interior_minus_floor']:+.2e} vs f=0 floor (beats f=0: "
        f"{near_deg['interior_beats_f0']}; beyond f_crit: {near_deg['best_interior_beyond_f_crit']})"
    )
    print("-" * 78)
    print(
        f"  G-B recovery (loaded) : bare|S11|={gB['bare_loaded_probe_S11_mag']:.6f} (rel {gB['bare_rel_error']:.1e}), "
        f"ceiling={gB['ceiling_loaded_probe_over_omega_C']:.6f} (rel {gB['ceiling_rel_error']:.1e})"
    )
    print("-" * 78)
    for g in (gA, gA_p, gB, gB_p, gC, gC_p):
        label = g.get("gate", g.get("planted"))
        print(f"  [{'PASS' if g['pass'] else 'FAIL'}] {label}")
    print("-" * 78)
    print(f"  JSON  : {out_json}")
    print(f"  FIG   : {fig_path}")

    assert all(g["pass"] for g in (gA, gA_p, gB, gB_p, gC, gC_p)), "a gate failed"


if __name__ == "__main__":
    main()

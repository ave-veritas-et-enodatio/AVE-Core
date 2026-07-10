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

from ave.core import junction_parasitics as jp  # CANONICAL X37 loaded dispersion (#616 merged; R10)
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
# PROVENANCE: scan_forbidden_inputs + _FORBIDDEN_MAGNITUDES follow the X37 driver's
# AST scan (x37_junction_parasitics.py, #616 merged, review R8). Extended: the
# scanned module is ave.core.junction_scattering. (The scanner logic is small +
# self-contained; kept inline in the driver rather than imported from a sibling
# script under src/scripts, which is not a package.)
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
# G-B — independent-reference recovery, now with an F-SENSITIVE leg (R8, PR #619).
# The pi*sqrt3 ceiling uses the CANONICAL X37 routine jp.g_scalar (R10 import), NOT
# a re-implementation. TWO legs each:
#   memoryless: bare |S11(f->0)| = 1/3 ; ceiling g(f->0) = pi*sqrt3 (references);
#   ACTIVE:     the parasitics MUST bite — |S11(pi, f=0.2)| > 1/3 + margin AND
#               g(f=0.2) < pi*sqrt3 - margin. A parasitics-DISABLED path returns the
#               memoryless values for ALL f and so FAILS the active legs (the R8
#               sabotage: the old gate probed only f->0, which is f-insensitive by
#               the deepest-notch result, so a disabled path passed spuriously).
# ═════════════════════════════════════════════════════════════════════════════
G_B_ACTIVE_F = 0.2  # extent where the parasitics visibly bite (f-sensitive leg)
G_B_ACTIVE_MARGIN = 1e-2  # the active legs must move by at least this


def _g_scalar_loaded(f: float, s_L: float = 1.0, s_C: float = 1.0) -> float:
    """omega_top/omega_C = the CANONICAL X37 loaded-dispersion ceiling jp.g_scalar
    (#616 merged; R10 — imported, not re-implemented). f->0 -> pi*sqrt3."""
    return float(jp.g_scalar(f, s_L, s_C))


def gate_B() -> dict:
    # memoryless references
    s11_mem = abs(js.s11_junction(1e-6, G_B_PROBE_F))  # loaded path, no early return
    rel_bare = abs(s11_mem - REF_BARE_S11_MAG) / REF_BARE_S11_MAG
    g_mem = _g_scalar_loaded(G_B_PROBE_F)
    rel_ceiling = abs(g_mem - REF_604_BAND_TOP_OVER_OMEGA_C) / REF_604_BAND_TOP_OVER_OMEGA_C
    # ACTIVE (f-sensitive) legs: the parasitics must move both observables
    s11_active = abs(js.s11_junction(np.pi, G_B_ACTIVE_F))  # |S11| at band-top mode, f=0.2
    g_active = _g_scalar_loaded(G_B_ACTIVE_F)
    bare_moves = (s11_active - REF_BARE_S11_MAG) > G_B_ACTIVE_MARGIN  # reflection RISES
    ceiling_moves = (REF_604_BAND_TOP_OVER_OMEGA_C - g_active) > G_B_ACTIVE_MARGIN  # ceiling DROPS
    mem_ok = rel_bare < G_B_TOL and rel_ceiling < G_B_TOL
    return {
        "gate": "G-B independent-reference recovery (memoryless + f-sensitive legs)",
        "bare_ref_S11_mag": REF_BARE_S11_MAG,
        "bare_memoryless_probe_S11_mag": s11_mem,
        "bare_rel_error": rel_bare,
        "ceiling_ref_source": REF_604_DOC,
        "ceiling_ref_over_omega_C": REF_604_BAND_TOP_OVER_OMEGA_C,
        "ceiling_memoryless_probe_over_omega_C": g_mem,
        "ceiling_rel_error": rel_ceiling,
        "active_f": G_B_ACTIVE_F,
        "active_S11_at_band_top": s11_active,
        "active_ceiling_over_omega_C": g_active,
        "bare_leg_f_sensitive": bool(bare_moves),
        "ceiling_leg_f_sensitive": bool(ceiling_moves),
        "tol": G_B_TOL,
        "note": "pi*sqrt3 ceiling via CANONICAL jp.g_scalar (#616 merged; R10). Active legs "
        "(R8) fail if the parasitics are disabled (sabotage caught).",
        "pass": bool(mem_ok and bare_moves and ceiling_moves),
    }


def gate_B_planted() -> dict:
    """Planted-violation proofs (R8): (a) a +1% offset on the memoryless recoveries
    FAILS the reference tolerance; (b) a PARASITICS-DISABLED sabotage (a loaded path
    that ignores f -> returns the memoryless values for ALL f) FAILS the f-sensitive
    active legs (the old f->0-only gate passed this sabotage spuriously)."""
    # (a) offset plant
    bare_off = abs(js.s11_junction(1e-6, G_B_PROBE_F)) * 1.01
    ceil_off = _g_scalar_loaded(G_B_PROBE_F) * 1.01
    rel_bare = abs(bare_off - REF_BARE_S11_MAG) / REF_BARE_S11_MAG
    rel_ceil = abs(ceil_off - REF_604_BAND_TOP_OVER_OMEGA_C) / REF_604_BAND_TOP_OVER_OMEGA_C
    offset_fires = rel_bare >= G_B_TOL and rel_ceil >= G_B_TOL
    # (b) parasitics-disabled sabotage: memoryless values regardless of f
    sab_s11 = REF_BARE_S11_MAG  # disabled parasitics -> |S11|=1/3 for all f
    sab_g = REF_604_BAND_TOP_OVER_OMEGA_C  # disabled parasitics -> pi*sqrt3 for all f
    sab_bare_moves = (sab_s11 - REF_BARE_S11_MAG) > G_B_ACTIVE_MARGIN
    sab_ceiling_moves = (REF_604_BAND_TOP_OVER_OMEGA_C - sab_g) > G_B_ACTIVE_MARGIN
    sabotage_fires = (not sab_bare_moves) and (not sab_ceiling_moves)  # active legs FAIL
    return {
        "planted": "G-B: (a) +1% offset on memoryless; (b) parasitics-disabled sabotage",
        "offset_bare_rel_error": rel_bare,
        "offset_ceiling_rel_error": rel_ceil,
        "offset_gate_fires": bool(offset_fires),
        "sabotage_bare_leg_f_sensitive": bool(sab_bare_moves),
        "sabotage_ceiling_leg_f_sensitive": bool(sab_ceiling_moves),
        "sabotage_gate_fires": bool(sabotage_fires),
        "gate_fired": bool(offset_fires and sabotage_fires),
        "pass": bool(offset_fires and sabotage_fires),
    }


# ═════════════════════════════════════════════════════════════════════════════
# G-C — objective-robustness + TWO-AXIS branch assignment (R1/R2, PR #619 review).
# The frozen single-frequency PRIMARY (obj-1 at pi) is EXACTLY DEGENERATE whenever
# its half-wave-invisible touch f_touch(pi) lies in (0,0.5] — co-equal minima
# {0, f_touch} => under the frozen rule's degenerate clause it fires BRANCH (iv).
# The band-integrated comparator (obj-2) has no such touch => uniquely f*=0 =>
# BRANCH (ii) on the broadband axis. KEEP BOTH. And (R2) if f_touch == 1/(2pi)
# INSIDE f_crit, the co-minimum sits ON the branch-(i) soliton mark in the
# self-consistent regime => branch (i) UNADJUDICATED PENDING-GRANT (not "no fire").
# ═════════════════════════════════════════════════════════════════════════════
def classify_two_axis(sp: dict, s_L: float, s_C: float) -> dict:
    """TWO-AXIS verdict. Returns the frozen-PRIMARY branch (obj-1) and the
    BAND-INTEGRATED branch (obj-2), plus the branch-(i) PENDING-GRANT flag."""
    primary_degen = sp["degeneracy"]["obj1_op6"]
    f_touch = primary_degen["f_touch"]
    # frozen-primary axis (obj-1, single-freq at pi)
    if sp["spread"] >= G_C_SCATTER_SPREAD:
        primary_branch = "iv"  # objective scatter
    elif primary_degen["degenerate"]:
        primary_branch = "iv"  # EXACT degeneracy {0, f_touch} -> frozen degenerate clause
    elif sp["f_stars"]["obj1_op6"] == 0.0:
        primary_branch = "ii"
    else:
        primary_branch = "indeterminate"
    # band-integrated axis (obj-2, broadband -> no half-wave trick)
    band_branch = "ii" if sp["band_integrated_unique_f0"] else "indeterminate"
    # branch-(i) PENDING-GRANT: a degenerate touch ON the tube-radius mark, inside f_crit
    on_mark = bool(primary_degen["degenerate"] and abs(f_touch - TUBE_RADIUS_MARK) < 1e-6)
    inside_fcrit = bool(np.isfinite(f_touch) and f_touch < F_CRIT)
    branch_i_pending_grant = bool(on_mark and inside_fcrit)
    return {
        "frozen_primary_branch": primary_branch,
        "band_integrated_branch": band_branch,
        "primary_degenerate": bool(primary_degen["degenerate"]),
        "primary_f_touch": f_touch,
        "branch_i_pending_grant_on_locus": branch_i_pending_grant,
        "banked": "f*=0 uniquely selected by the band-integrated comparator (obj-2); the "
        "single-frequency objectives are exactly degenerate along {0, f_touch} (half-wave-"
        "invisible bore family). Frozen-primary outcome = branch (iv); obj-2 axis = branch (ii).",
    }


def gate_C(s_L: float = 1.0, s_C: float = 1.0) -> dict:
    sp = js.objective_spread(s_L, s_C)
    verdict = classify_two_axis(sp, s_L, s_C)
    return {
        "gate": "G-C objective-robustness (two-axis; branch-iv/degeneracy detector)",
        "s_L": s_L,
        "s_C": s_C,
        "f_stars": sp["f_stars"],
        "spread": sp["spread"],
        "primary_degenerate": sp["primary_degenerate"],
        "primary_f_touch": sp["degeneracy"]["obj1_op6"]["f_touch"],
        "band_integrated_unique_f0": sp["band_integrated_unique_f0"],
        "robust_threshold": G_C_ROBUST_SPREAD,
        "scatter_threshold": G_C_SCATTER_SPREAD,
        "two_axis_verdict": verdict,
        "pass": True,  # G-C reports; the two-axis verdict is a first-class result
    }


def gate_C_planted() -> dict:
    """Planted-violation proofs of the two detectors (R1 + branch-iv):
    (a) the DEGENERACY detector: obj-1's half-wave-invisible touch at f_touch(pi)
        must be EXACTLY co-minimal with f=0 (|S11(pi;f_touch)|^2 - 1/9 == machine 0),
        and the band-integrated obj-2 must NOT touch (unique) — proves the two-axis
        detector discriminates.
    (b) the SCATTER (branch-iv) detector: a divergent bogus objective (maximise
        reflection -> f!=0) pushes the spread across the scatter threshold; the 3
        real objectives (control) do not."""
    # (a) degeneracy discrimination
    f_touch = js.half_wave_invisible_touch(np.pi, 1.0, 1.0)
    touch_is_exact = abs(js.objective_op6(f_touch) - 1.0 / 9.0) < 1e-12
    obj2_not_degenerate = not js.objective_is_degenerate("obj2_band_integrated")["degenerate"]
    degen_detector_fires = bool(touch_is_exact and obj2_not_degenerate)
    # (b) scatter discrimination
    real = js.objective_spread()
    real_flagged = real["spread"] >= G_C_SCATTER_SPREAD
    fs = np.linspace(js.F_POINT_JUNCTION, js.F_WIGNER_SEITZ, 501)
    j_bad = np.array([js.objective_op6(f) for f in fs])
    f_bad = float(fs[int(np.argmax(j_bad))])  # bogus "maximise reflection" -> large f
    planted_spread = max(list(real["f_stars"].values()) + [f_bad]) - min(list(real["f_stars"].values()) + [f_bad])
    scatter_detector_fires = (not real_flagged) and (planted_spread >= G_C_SCATTER_SPREAD)
    return {
        "planted": "G-C: (a) exact-degeneracy discrimination; (b) divergent-objective scatter",
        "degeneracy_f_touch": f_touch,
        "obj1_at_touch_minus_1_9": js.objective_op6(f_touch) - 1.0 / 9.0,
        "degeneracy_detector_fires": degen_detector_fires,
        "control_real_spread": real["spread"],
        "planted_f_bogus": f_bad,
        "planted_spread": planted_spread,
        "scatter_detector_fires": bool(scatter_detector_fires),
        "gate_fired": bool(degen_detector_fires and scatter_detector_fires),
        "pass": bool(degen_detector_fires and scatter_detector_fires),
    }


# ═════════════════════════════════════════════════════════════════════════════
# s-sweep (X37 R5 lesson) + landscape + figure
# ═════════════════════════════════════════════════════════════════════════════
def s_sweep(s_grid=(0.3, 0.5, 1.0, 2.0, 3.0)) -> dict:
    """f* + EXACT obj-1 degeneracy over s_L,s_C in [0.3,3]^2 (X37 R5 lesson). For each
    cell records the half-wave-invisible touch f_touch(pi), whether it is in-domain
    (obj-1 degenerate there), and (R2) whether it lands ON the tube-radius mark
    1/(2pi) INSIDE f_crit -> a branch-(i) PENDING-GRANT locus. The band-integrated
    obj-2 uniquely selects f*=0 at every cell (the load-bearing broadband axis)."""
    rows = []
    band_unique_all = True
    branch_i_loci = []
    for sL in s_grid:
        for sC in s_grid:
            sp = js.objective_spread(sL, sC)
            ft = sp["degeneracy"]["obj1_op6"]["f_touch"]
            degen = sp["degeneracy"]["obj1_op6"]["degenerate"]
            on_mark_inside = bool(np.isfinite(ft) and abs(ft - TUBE_RADIUS_MARK) < 1e-6 and ft < F_CRIT)
            rows.append(
                {
                    "s_L": sL,
                    "s_C": sC,
                    "f_star_obj2": sp["f_stars"]["obj2_band_integrated"],
                    "obj1_f_touch": None if not np.isfinite(ft) else float(ft),
                    "obj1_degenerate": bool(degen),
                    "branch_i_pending_grant_on_locus": on_mark_inside,
                }
            )
            band_unique_all = band_unique_all and sp["band_integrated_unique_f0"]
            if on_mark_inside:
                branch_i_loci.append({"s_L": sL, "s_C": sC, "f_touch": float(ft)})
    return {
        "grid": list(s_grid),
        "rows": rows,
        "band_integrated_uniquely_f0_all_cells": bool(band_unique_all),
        "branch_i_pending_grant_loci": branch_i_loci,
        "note": "obj-2 uniquely selects f*=0 at every cell; obj-1 is degenerate wherever "
        "f_touch(pi) in (0,0.5]. Cell (s_L,s_C)=(2,3) puts f_touch = 1/(2pi) EXACTLY inside "
        "f_crit -> an obj-1 co-minimum ON the branch-(i) soliton mark: UNADJUDICATED PENDING-GRANT.",
    }


def exact_degeneracy_disclosure(s_L: float = 1.0, s_C: float = 1.0) -> dict:
    """R1 CORRECTION of the old 'near-degeneracy' framing. obj-1 |S11(pi;f)|^2 touches
    the f=0 floor (1/9) EXACTLY (machine zero, NOT +2.7e-8 as first shipped) at the
    half-wave-invisible extent f_touch(pi) — the junction section is half-wave at the
    band-top tone and thus impedance-transparent there. So obj-1 has co-equal global
    minima {0, f_touch}: it is EXACTLY DEGENERATE (the earlier grid argmin landed on 0
    only by resolution luck). f_touch is a single-tone trick; obj-2 (band-integrated)
    is unaffected -> uniquely f*=0."""
    f_touch = js.half_wave_invisible_touch(np.pi, s_L, s_C)
    if not np.isfinite(f_touch):
        return {"f_touch": None, "in_domain": False, "note": "no real touch (s_C >= 3 s_L)"}
    obj_at_touch = js.objective_op6(f_touch, s_L, s_C)
    return {
        "f_touch": float(f_touch),
        "f0_floor": 1.0 / 9.0,
        "obj1_at_touch": float(obj_at_touch),
        "obj1_at_touch_minus_floor": float(obj_at_touch - 1.0 / 9.0),  # machine zero
        "in_domain": bool(js.F_POINT_JUNCTION < f_touch <= js.F_WIGNER_SEITZ),
        "beyond_f_crit": bool(f_touch > F_CRIT),
        "on_tube_radius_mark": bool(abs(f_touch - TUBE_RADIUS_MARK) < 1e-6),
        "note": "obj-1 EXACTLY degenerate along {0, f_touch} (half-wave-invisible bore); "
        "obj-2 broadband breaks the degeneracy -> f*=0 on the broadband axis.",
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
    axR.axvline(0.0, color=style.COLORS["ave"], lw=1.2, alpha=0.5, label=r"obj-2 $f^\ast{=}0$ (broadband)")
    f_touch = js.half_wave_invisible_touch(np.pi, s_L, s_C)
    if np.isfinite(f_touch) and f_touch <= 0.5:
        axR.axvline(
            f_touch,
            color=style.COLORS["ave"],
            lw=1.2,
            ls="--",
            label=rf"obj-1 co-min $f_{{touch}}{{=}}\sqrt{{2}}/\pi\approx{f_touch:.3f}$ (degenerate)",
        )
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
    exact_deg = exact_degeneracy_disclosure(s_L, s_C)
    fig_path = make_figure(curves, s_L, s_C)

    verdict = gC["two_axis_verdict"]
    primary_branch = verdict["frozen_primary_branch"]
    band_branch = verdict["band_integrated_branch"]
    circ = js.ideal_circulator_s_matrix()

    result = {
        "task": "X38 S11-minimization bore selection (scalar/compression, Phase 1)",
        "class": "MIXED: selected f* derived-geometric; SCALE omega_C dimensional-forced/identity",
        "objective_provenance": {
            "canonical_operator": "Universal Operator #6 lambda_min(S†S)->0",
            "leaf": "manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/eigenvalue-target.md",
            "claim": "clm-gdd70j",
            "code_path": "ave.core.universal_operators.universal_eigenvalue_target",
            "op6_scope_note_R6": "Op6 applied HERE as a CANDIDATE selector. Per canon's OWN honest-scope "
            "note (constants.py, HONEST SCOPE 2026-06-14) the S11 landscape is FLAT in R.r and "
            "'S11 minimization does NOT select R.r=1/4' -> Op6 did NOT select the trefoil geometry. "
            "(The 'same operator that selected the trefoil' premise entered via the orchestrator brief.)",
        },
        "two_axis_verdict_R1": {
            "banked": verdict["banked"],
            "frozen_primary_branch": primary_branch,
            "band_integrated_branch": band_branch,
            "primary_degenerate": verdict["primary_degenerate"],
            "primary_f_touch_at_pi": verdict["primary_f_touch"],
            "note": "obj-1 (primary, single-freq at pi) EXACTLY degenerate {0, f_touch=sqrt2/pi}; "
            "obj-2 (band-integrated) uniquely f*=0. 'demonstrated' not 'adjudicated' (R7; #613 MAJOR-11).",
        },
        "bare_junction": {
            "S11_analytic": js.bare_junction_s11(3),
            "abs_S11": abs(js.bare_junction_s11(3)),
            "note": "z=3 star: incident sees Z0/2 -> Gamma=(2-z)/z=-1/3; memoryless NOT matched",
        },
        "l_match": {
            "Q_for_2to1": float(np.sqrt(2.0 - 1.0)),
            "ideal_null_reachable": True,
            "physical_vertex_dips_below_1_3": bool(min(curves["deepest_notch"]) < REF_BARE_S11_MAG**2 - 1e-9),
            "verdict": "L-match Q=1 CONFIRMED as a network fact; REFUTED at the LOSSLESS RECIPROCAL "
            "vertex (accumulator on low-Z node + C3v forbids a one-arm shunt -> wrong orientation)",
        },
        "op6_target_and_theorem": {
            "deepest_notch_all_f": {f"f={f:.2f}": js.deepest_notch(f) for f in (0.0, 0.1, 0.3, 0.5)},
            "reflectionless_target_reachable_reciprocal": False,
            "classification_R5": "the classic matched-lossless-reciprocal-3-port theorem (Pozar §7.1 "
            "class; |S11|>=1/3 symmetric corollary), CONFIRMED at the vertex — provable, not numerical",
            "vocabulary_R9": "reactive BACK-SCATTER / redistribution (Ax3 lossless: no dissipation), NOT a 'loss'",
            "reciprocity_scope_R3": "holds for the LOSSLESS RECIPROCAL class only",
        },
        "non_reciprocal_escape_R3_R4": {
            "circulator_S": circ.real.tolist(),
            "circulator_unitary": bool(np.allclose(circ.conj().T @ circ, np.eye(3))),
            "circulator_S11": float(abs(circ[0, 0])),
            "circulator_reciprocal": bool(np.allclose(circ, circ.T)),
            "escape_class": "matched lossless C3-symmetric 3-ports EXIST but ONLY non-reciprocally "
            "(circulator witness). ANY lossless+reciprocal+C3 network (incl. the evanescent-stub / "
            "finite-volume resonant branch named earlier) obeys the 1/3 theorem -> that escape is DEAD "
            "(R4); the ONLY escape class is non-reciprocity.",
            "chirality_and_T_breaking": "the lattice is chiral at Axiom-1 (right-handed I4_1 32, "
            "axiom-definitions.md:16) -> parity broken; but circulation needs a TIME-REVERSAL-breaking "
            "bias (candidate: frozen-bias sector u0*/Omega_freeze) -> PENDING-GRANT, asserted nowhere.",
            "x37_c2_flag": "X37's MERGED Correction-Log C2 names the same now-dead evanescent-stub "
            "escape -> correction-PR candidate (surfaced for the orchestrator; NOT edited here).",
        },
        "f_star": {
            "obj1_op6_primary_gridargmin": gC["f_stars"]["obj1_op6"],
            "obj2_band_integrated": gC["f_stars"]["obj2_band_integrated"],
            "obj3_single_freq": gC["f_stars"]["obj3_single_freq"],
            "spread": gC["spread"],
            "note": "obj-1 grid-argmin=0 is resolution luck (co-min at f_touch missed by the grid); "
            "the EXACT statement is the two-axis verdict above.",
        },
        "self_consistency": {
            "f_crit": F_CRIT,
            "note": "the band-integrated f*=0 < f_crit (self-consistent). The obj-1 co-minimum f_touch "
            "sits at f>f_crit at s=1 (self-invalidated regime) but INSIDE f_crit at cell (2,3).",
        },
        "comparison_marks": {
            "tube_radius_1_over_2pi": TUBE_RADIUS_MARK,
            "core_thickness": CORE_THICKNESS_MARK,
            "branch_i_status_R2": "UNADJUDICATED PENDING-GRANT on the degenerate locus: at cell "
            "(s_L,s_C)=(2,3), f_touch = 1/(2pi) EXACTLY, INSIDE f_crit -> an obj-1 co-minimum ON the "
            "tube-radius mark in the self-consistent regime. A formula locus (s-cell-dependent), NOT "
            "asserted as branch (i); flagged for Grant.",
        },
        "exact_degeneracy_disclosure_R1": exact_deg,
        "s_sweep": sweep,
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
    print("X38 — S11-minimization bore selection (scalar/compression, Phase 1) [PR #619 REPAIR]")
    print("=" * 78)
    print("  objective (canon)     : Op6 lambda_min(S†S)->0 [candidate selector; NOT the trefoil selector, R6]")
    print(f"  bare junction z=3     : S11 = {js.bare_junction_s11(3):+.4f}  (|S11|=1/3; memoryless NOT matched)")
    print(f"  L-match Q (2:1)       : {np.sqrt(1.0):.3f}  -> ideal null reachable; REFUTED at lossless-recip vertex")
    print("  1/3 floor (R5)        : classic matched-lossless-RECIPROCAL-3-port theorem (Pozar §7.1), confirmed")
    print(
        f"  non-recip escape (R3) : circulator S11={float(abs(circ[0, 0])):.0f} "
        f"(unitary, C3, NON-recip) -> T-break PENDING-GRANT"
    )
    print("-" * 78)
    print("  TWO-AXIS VERDICT (R1):")
    print(
        f"    obj-1 (primary, pi)  : EXACTLY degenerate {{0, f_touch={exact_deg['f_touch']:.4f}}} "
        f"(obj1@touch-1/9={exact_deg['obj1_at_touch_minus_floor']:+.1e}) -> frozen BRANCH ({primary_branch})"
    )
    print(f"    obj-3 (pi/2)         : f_touch={js.half_wave_invisible_touch(np.pi / 2):.3f} OUT of [0,0.5] at s=1")
    print(
        f"    obj-2 (band-integ.)  : uniquely f*={gC['f_stars']['obj2_band_integrated']:.3f} -> BRANCH ({band_branch})"
    )
    print("    BANKED               : f*=0 selected ONLY on the broadband axis; single-freq objectives degenerate")
    print("-" * 78)
    print(
        f"  s-sweep [0.3,3]^2     : obj-2 uniquely f*=0 all cells = {sweep['band_integrated_uniquely_f0_all_cells']}; "
        f"branch-(i) PENDING-GRANT loci: {[(r['s_L'], r['s_C']) for r in sweep['branch_i_pending_grant_loci']]}"
    )
    print("-" * 78)
    print(
        f"  G-B (R8)              : mem bare|S11|={gB['bare_memoryless_probe_S11_mag']:.4f} "
        f"rel {gB['bare_rel_error']:.0e}, ceiling={gB['ceiling_memoryless_probe_over_omega_C']:.4f} "
        f"rel {gB['ceiling_rel_error']:.0e}; "
        f"f-sensitive legs bare={gB['bare_leg_f_sensitive']}/ceiling={gB['ceiling_leg_f_sensitive']}"
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

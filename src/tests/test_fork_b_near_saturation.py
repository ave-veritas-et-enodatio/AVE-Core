"""Fork-B GATE3 NEAR-SATURATION re-run tests — pin the ECHO-FINAL verdict.

Parent result: research/2026-06-20_fork-b-saturation-tank-confinement_result.md §4
This module: src/ave/solvers/fork_b_near_saturation.py

═══════════════════════════════════════════════════════════════════════════════
THE FROZEN NEAR-SATURATION OUTCOME (BRUTAL HONESTY — Rule 11)
═══════════════════════════════════════════════════════════════════════════════
The merged GATE3 reported the quarter-arc shape-generic, but ONLY at A_bond.max≈0.77
(shallow). This re-run drives FULL saturation (A_bond.max≈0.95–0.99, the steep
regime where √(1−A²)'s dS/dA→−∞) and re-runs the SAME Δ/L metric against five
GENUINELY-DIFFERENT smooth families (plain tanh, exp, Lorentzian, power 1−Aⁿ,
linear) — all norm+depth-matched — plus a top-hat POSITIVE CONTROL.

VERDICT = ECHO-FINAL (the expected, fully-acceptable outcome):
  * At A_bond.max≈0.976 (srs L=6): max smooth Δ/L gap ≈ 0.25% (≪10%), min eigvec
    overlap ≈ 0.99999 — the SAME physical bound mode, even though the shapes are
    genuinely different (max|ΔS| ≈ 0.42).
  * The top-hat POSITIVE CONTROL opens a gap ≈ 165% with overlap ≈ 0.44 — the
    metric STILL DISCRIMINATES at full saturation (the zero is physical, not blind).
  * Deeper (srs L=8, A_max≈0.99, S_min=1e-5): the smooth gap shrinks toward 0
    (≈0.007%), overlap → 1.0, while the top-hat gap GROWS (≈302%).

=> the quarter-arc is NOT shape-special even in its steepest regime. A
   step-DISCONTINUOUS stiffness IS discriminable; the metric resolves shape; the
   zero is physical, not baked. These tests assert the ECHO-FINAL outcome. Forcing
   a CHORD by un-matching norm/depth or dropping the positive control would be
   debugging-toward-a-rescue (Rule 11 wrong-reaction).
"""

import numpy as np

from ave.solvers.fork_b_near_saturation import (
    QUARTER_ARC_NORM,
    NearSaturationConfig,
    norm_match_family,
    solve_near_saturation_shape,
    _SMOOTH_FAMILIES,
)

# srs L=6 is the FAST verdict net (A_max≈0.976, ~2s). Used for the CI pins.
_CFG = NearSaturationConfig(net="srs", L=6, frac=0.999, sigma_frac=1.0 / 6.0, S_min=1e-3)


# ─────────────────────────────────────────────────────────────────────────────
# PART-1 BASIS: the cross-family comparators are genuinely-different AND NORM-FEASIBLE
# (the STRONGER basis that "cross-family is norm-infeasible" over-generalized from
# the ONE retired endpoint-tanh parameterization 0.5(1+tanh(k(0.5−A)))).
# ─────────────────────────────────────────────────────────────────────────────


def test_all_cross_family_kernels_reach_quarter_arc_norm():
    """All five GENUINELY-DIFFERENT families reach the quarter-arc norm π/4 (the
    brentq norm-match SUCCEEDS) — they are norm-FEASIBLE, NOT assumed-away. This is
    the corrected, STRONGER basis for the ECHO (the retired tanh was the only
    norm-infeasible one)."""
    for name, (builder, bracket) in _SMOOTH_FAMILIES.items():
        nm = norm_match_family(builder, bracket)
        assert nm["ok"], f"{name} unexpectedly norm-INFEASIBLE to π/4: {nm.get('reason')}"
        assert abs(nm["norm"] - QUARTER_ARC_NORM) < 1e-6, f"{name} norm {nm['norm']} != π/4"


# ─────────────────────────────────────────────────────────────────────────────
# PART-2: the near-saturation re-run is IN the steep regime, and the metric
# STILL DISCRIMINATES there (positive control). Without these, a zero gap is void.
# ─────────────────────────────────────────────────────────────────────────────


def test_near_saturation_reaches_steep_regime():
    """The re-run actually drives A_bond into the steep regime (A_max≥0.95) — the
    regime the merged GATE3 (A_max≈0.77) never reached. Confirms the kernel clip
    does NOT no-op the full-saturation drive."""
    out = solve_near_saturation_shape(_CFG)
    assert out["ok"]
    assert out["achieved_A_max"] >= 0.95, f"did not reach steep regime: A_max={out['achieved_A_max']}"
    assert out["in_steep_regime"]
    assert out["n_bonds_A_gt_0p9"] >= 1  # the steep tail IS exercised by some bonds


def test_positive_control_top_hat_discriminates_at_full_sat():
    """ANTI-TAUTOLOGY (load-bearing): the top-hat (step-discontinuous) stiffness
    MUST open a large Δ/L gap (>10%) AND drop the eigenvector overlap (<0.95) at
    full saturation — else the metric is blind here and the test is VOID. A zero
    smooth gap is only informative because the metric CAN open one."""
    out = solve_near_saturation_shape(_CFG)
    pc = out["positive_control_top_hat"]
    assert pc["shape_gap"] > 0.10, f"positive control did not open a gap: {pc['shape_gap']}"
    assert pc["eigvec_overlap"] < 0.95, f"positive control overlap not dropped: {pc['eigvec_overlap']}"
    assert out["metric_discriminates_at_full_sat"], "metric does NOT discriminate => test void"


def test_cross_family_shapes_are_genuinely_different():
    """The zero gap is PHYSICAL, not because the shapes are secretly identical:
    the depth-matched cross-family comparators differ from the quarter-arc by a
    substantial max|ΔS| (≈0.4 for exp) yet give the same Δ/L + overlap=1."""
    out = solve_near_saturation_shape(_CFG)
    assert out["max_abs_dS_smooth_vs_canon"] > 0.05, (
        "shapes too similar — the zero gap could be a same-shape artifact"
    )


# ─────────────────────────────────────────────────────────────────────────────
# THE PINNED VERDICT: ECHO-FINAL (smooth gap ~0 AND overlap ~1 at full saturation).
# ─────────────────────────────────────────────────────────────────────────────


def test_near_saturation_verdict_is_echo_final():
    """The frozen-binned near-saturation verdict is ECHO-FINAL: every SMOOTH
    cross-family comparator gives Δ/L gap ≪10% AND eigvec overlap ≥0.95 at full
    saturation (with the positive control confirming discrimination). The
    quarter-arc is NOT shape-special even in its steep regime."""
    out = solve_near_saturation_shape(_CFG)
    assert out["verdict"] == "ECHO-FINAL", f"verdict moved: {out['verdict']} — {out['reason']}"
    # the load-bearing bins (the SAME thresholds as the frozen binning):
    assert out["max_smooth_shape_gap"] < 0.10, (
        f"a smooth cross-family gap reached {out['max_smooth_shape_gap']:.4f} ≥10% "
        "at full saturation — this would be a PARTIAL CHORD, re-run adjudication"
    )
    assert out["min_smooth_eigvec_overlap"] >= 0.95, (
        f"a smooth bound-mode overlap dropped to {out['min_smooth_eigvec_overlap']:.4f} "
        "<0.95 at full saturation — this would be a PARTIAL CHORD, re-run adjudication"
    )
    assert out["all_smooth_norm_feasible"]


def test_near_saturation_alpha_free_structural():
    """α-FREE STRUCTURAL: the near-saturation module never imports an α-carrier
    (the kernels read the dimensionless A=|V|/V_yield). Import-guard on the module
    globals (HR2 anti-circularity)."""
    import ave.solvers.fork_b_near_saturation as F

    for tok in ("ALPHA", "Q_TANK", "ELECTRON", "RHO_BULK"):
        assert tok not in vars(F), f"alpha-leak: {tok} reachable in near-saturation module"

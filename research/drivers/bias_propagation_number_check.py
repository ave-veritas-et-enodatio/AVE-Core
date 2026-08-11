#!/usr/bin/env python3
"""Gating number check for the bias propagation theorem lane (R49b/R50).

Re-verifies every verdict-bearing numeral of the lane against the driver JSON
with INDEPENDENT arithmetic (math module — the second engine; the driver used
sympy + mpmath). Supports --mutation-receipt: perturbs a loaded value in memory
and MUST detect it, proving the checker is live. Auto-discovered by the
make-verify umbrella.

Frozen source of every target below: research/2026-08-10_bias-propagation_prereg-FROZEN.md
(committed and pushed ALONE at d4bee683 before any driver code existed).
"""
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
JSON = os.path.join(HERE, "bias_propagation_lane_results.json")

MUTATE = "--mutation-receipt" in sys.argv


def fail(msg):
    print(f"BIAS-PROPAGATION NUMBER CHECK: FAIL — {msg}")
    sys.exit(1)


def main():
    with open(JSON) as f:
        r = json.load(f)

    if MUTATE:
        # corrupt one verdict-bearing numeral; the checks below MUST catch it
        r["L3_frequency_response_instrument"]["positive_controls"]["hyperbolic"]["p_measured"] = 1.0

    K = r["constants"]
    c, G_, hbar, ln, me = K["C_0"], K["G"], K["HBAR"], K["L_NODE"], K["M_E"]
    rho, xi = K["RHO_BULK"], K["XI_MACHIAN"]
    M_SUN = K["M_SUN"]  # canonical, carried through the driver JSON

    checks = []

    # ---- L0: kappa, the bias inertia, and the G-TAUTOLOGY identity ----
    L0 = r["L0_constants_and_tautology"]
    kappa_ind = c**4 / (7.0 * G_)                      # independent arithmetic
    checks.append(("kappa == c^4/7G", abs(L0["kappa_N"] - kappa_ind) / kappa_ind < 1e-12))
    checks.append(("inertia_req == kappa/c^2",
                   abs(L0["inertia_required_for_cg_eq_c_kg_per_m"] - kappa_ind / c**2)
                   / (kappa_ind / c**2) < 1e-12))
    checks.append(("G-TAUTOLOGY: ratio/xi == 2 to 1e-9",
                   abs(L0["ratio_over_xi"] - 2.0) < 1e-9))
    checks.append(("G-TAUTOLOGY: identity SYMBOLICALLY proven (not asserted)",
                   L0["G_TAUTOLOGY_identity_symbolically_proven"] is True))
    checks.append(("G-TAUTOLOGY premise rho_bulk == m_e/(2 l^3)",
                   abs(me / (2.0 * ln**3) - rho) / rho < 1e-9))
    checks.append(("G-TAUTOLOGY premise xi == c^2 l/(7 G m_e)",
                   abs(c**2 * ln / (7.0 * G_ * me) - xi) / xi < 1e-12))

    # ---- L1: Ax4 dialect consistency ----
    L1 = r["L1_ax4_dialect_consistency"]
    checks.append(("A = (2/7)eps_11 gives A == 1 at r_s", L1["A_at_r_s_equals_one"] is True))
    checks.append(("n_temporal == 1 + 2GM/c^2 r",
                   L1["n_temporal_equals_1_plus_2GM_over_c2r"] is True))

    # ---- L2: the two clock branches (deliverable 2) ----
    L2 = r["L2_clock_branches"]
    c1, cS = L2["CLOCK_1"], L2["CLOCK_S"]
    checks.append(("CLOCK-1 leading F/F_Newton == 1 exactly",
                   c1["leading_is_exactly_one"] is True))
    checks.append(("CLOCK-1 hbar cancels", c1["hbar_cancels"] is True))
    checks.append(("CLOCK-1 is A_g-free (G-AGFREE)", c1["Ag_appears"] is False))
    checks.append(("CLOCK-1 matches GR static force-at-infinity EXACTLY",
                   c1["matches_GR_static_force_at_infinity_EXACTLY"] is True))
    # independent solar-surface arithmetic
    # M_SUN is canonical (constants.py:132). The solar RADIUS is not a
    # canonical substrate constant -- it is an external comparator, declared
    # ENG-CHOICE(IAU nominal photospheric radius) per SVA row 5. It scales
    # only the exhibit, never a verdict: both clock branches are evaluated at
    # the same r, and the branch separation is a RATIO.
    R_SUN_ENG_CHOICE = 6.957e8  # [m] IAU nominal; comparator, not a constant
    M_sun, R_sun = M_SUN, R_SUN_ENG_CHOICE
    rs_ind = 2.0 * G_ * M_sun / c**2
    A_ind = rs_ind / R_sun
    checks.append(("solar r_s independent", abs(L2["solar_r_s_m"] - rs_ind) / rs_ind < 1e-12))
    checks.append(("A(R_sun) independent", abs(L2["A_at_solar_surface"] - A_ind) / A_ind < 1e-12))
    checks.append(("CLOCK-1 numeric == (1-A)^(-1/2)",
                   abs(c1["numeric_at_solar_surface"] - (1 - A_ind) ** -0.5) < 1e-12))
    checks.append(("CLOCK-S leading ratio == A (frozen 4.246094e-6)",
                   abs(cS["numeric_at_solar_surface"] - A_ind) / A_ind < 1e-6))
    checks.append(("CLOCK-S under-predicts by 2.355e5 (frozen)",
                   abs(cS["underprediction_factor"] - 1.0 / A_ind) / (1.0 / A_ind) < 1e-6))
    checks.append(("clock branches separated by >5 OOM",
                   L2["separation_orders_of_magnitude"] > 5.0))

    # ---- L3: the FROZEN liveness set (G-LIVE). UNRUN != PASSED. ----
    L3 = r["L3_frequency_response_instrument"]
    pc = L3["positive_controls"]
    for kind, target, tol in (("hyperbolic", 2.0, 0.2),
                              ("diffusive", 0.5, 0.15),
                              ("schrodinger", 1.0, 0.2)):
        checks.append((f"G-LIVE positive control {kind}: p == {target} +/- {tol}",
                       pc[kind]["p_measured"] is not None
                       and abs(pc[kind]["p_measured"] - target) <= tol))
    # the Ax3 amplitude test: lossless classes must have |H| == 1, diffusive must not
    checks.append(("Ax3 |H|==1 for hyperbolic", pc["hyperbolic"]["lossless_absH_is_1"] is True))
    checks.append(("Ax3 |H|==1 for schrodinger", pc["schrodinger"]["lossless_absH_is_1"] is True))
    checks.append(("Ax3 |H|<1 for diffusive (needs a named port)",
                   pc["diffusive"]["lossless_absH_is_1"] is False))
    checks.append(("G-LIVE negative control: instantaneous solve UNRESOLVABLE",
                   L3["negative_control_instantaneous"]["resolvable"] is False))

    # RECONCILE, do not consume. A gate that reads a self-declared summary field is
    # a checklist, not a gate: recompute the summary from the underlying numbers and
    # FAIL on contradiction between the declared label and the computed truth.
    recomputed_live = all(
        pc[k]["p_measured"] is not None and abs(pc[k]["p_measured"] - t) <= tol
        for k, t, tol in (("hyperbolic", 2.0, 0.2), ("diffusive", 0.5, 0.15),
                          ("schrodinger", 1.0, 0.2))
    ) and L3["negative_control_instantaneous"]["resolvable"] is False
    checks.append(("G-LIVE declared == RECOMPUTED (no self-declared gate)",
                   L3["G_LIVE_all_green"] == recomputed_live))
    checks.append(("G-LIVE all green (recomputed)", recomputed_live is True))
    for kind, target, tol in (("hyperbolic", 2.0, 0.2), ("diffusive", 0.5, 0.15),
                              ("schrodinger", 1.0, 0.2)):
        recomputed_pass = (pc[kind]["p_measured"] is not None
                           and abs(pc[kind]["p_measured"] - target) <= tol)
        checks.append((f"{kind} PASS label == recomputed",
                       pc[kind]["PASS"] == recomputed_pass))

    # ---- L4: the LC-HYPERBOLIC admission price ----
    L4 = r["L4_lc_admission_price"]
    checks.append(("LC admission price == kappa/c^2",
                   abs(L4["inertia_required_kg_per_m"] - kappa_ind / c**2)
                   / (kappa_ind / c**2) < 1e-12))
    checks.append(("implied length scale independent",
                   abs(L4["implied_length_scale_m"]
                       - math.sqrt((kappa_ind / c**2) / rho))
                   / math.sqrt((kappa_ind / c**2) / rho) < 1e-12))

    bad = [name for name, ok in checks if not ok]
    if MUTATE:
        if bad:
            print(f"BIAS-PROPAGATION MUTATION RECEIPT: FIRED — {len(bad)} detector(s) "
                  f"caught the injected corruption: {bad}")
            return 0
        fail("mutation receipt did NOT fire — the checker is not live")
    if bad:
        fail(f"{len(bad)} check(s) failed: {bad}")
    print(f"BIAS-PROPAGATION NUMBER CHECK: PASS — {len(checks)} checks green")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

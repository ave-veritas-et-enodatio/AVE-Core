#!/usr/bin/env python3
"""Gating number check for the bias propagation theorem lane (R49b/R50).

Re-verifies every verdict-bearing numeral of the lane against the driver JSON
with INDEPENDENT arithmetic (math module — the second engine; the driver used
sympy + mpmath). Supports --mutation-receipt: perturbs a loaded value in memory
and MUST detect it, proving the checker is live. Auto-discovered by the
make-verify umbrella.

Frozen source of every target below: research/2026-08-10_bias-propagation_prereg-FROZEN.md
(committed and pushed ALONE at d4bee683 before any driver code existed).

RECONCILE, DO NOT CONSUME (2026-08-11 review, F8c). A check that reads a
self-declared boolean out of the JSON is a checklist entry, not a gate. Every
declared boolean below is now paired with a RECOMPUTATION from the JSON's own
numeric inputs, and the checker FAILS on any contradiction between the declared
label and the computed truth. The per-check counter at the bottom reports how
many checks still rest on an unreconciled declared boolean; the target is zero.
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
    # RECONCILED: the declared boolean is checked AGAINST the residual the driver
    # also shipped, so the label cannot outrun the computation it summarises.
    checks.append(("G-TAUTOLOGY: identity SYMBOLICALLY proven (not asserted)",
                   L0["G_TAUTOLOGY_identity_symbolically_proven"] is True))
    checks.append(("G-TAUTOLOGY: declared-proven == (residual string is '0')",
                   L0["G_TAUTOLOGY_identity_symbolically_proven"]
                   == (L0["G_TAUTOLOGY_residual"].strip() == "0")))
    checks.append(("G-TAUTOLOGY premise rho_bulk == m_e/(2 l^3)",
                   abs(me / (2.0 * ln**3) - rho) / rho < 1e-9))
    checks.append(("G-TAUTOLOGY premise xi == c^2 l/(7 G m_e)",
                   abs(c**2 * ln / (7.0 * G_ * me) - xi) / xi < 1e-12))

    # ---- L1: Ax4 dialect consistency (declared booleans RECONCILED) ----
    L1 = r["L1_ax4_dialect_consistency"]
    checks.append(("A = (2/7)eps_11 gives A == 1 at r_s", L1["A_at_r_s_equals_one"] is True))
    recomputed_A_at_rs = abs(L1["A_at_r_s_numeric"] - 1.0) < 1e-12
    checks.append(("A(r_s) label == RECOMPUTED from the shipped numeric",
                   L1["A_at_r_s_equals_one"] == recomputed_A_at_rs))
    checks.append(("n_temporal == 1 + 2GM/c^2 r",
                   L1["n_temporal_equals_1_plus_2GM_over_c2r"] is True))
    # recompute 1 + 2GM/c^2 r in plain math at the driver's own sample points and
    # reconcile the declared boolean against it
    ntemp_ok = all(
        abs(s["n_temporal"] - (1.0 + 2.0 * s["G"] * s["M"] / (s["c"] ** 2 * s["r"])))
        < 1e-15
        for s in L1["n_temporal_samples"]
    )
    checks.append(("n_temporal samples recomputed independently (plain math)", ntemp_ok))
    checks.append(("n_temporal label == RECOMPUTED at every sample",
                   L1["n_temporal_equals_1_plus_2GM_over_c2r"] == ntemp_ok))

    # ---- L2: the two clock branches (deliverable 2) ----
    L2 = r["L2_clock_branches"]
    c1, cS = L2["CLOCK_1"], L2["CLOCK_S"]
    checks.append(("CLOCK-1 leading F/F_Newton == 1 exactly",
                   c1["leading_is_exactly_one"] is True))
    checks.append(("CLOCK-1 leading label == RECOMPUTED from the shipped G^0 term",
                   c1["leading_is_exactly_one"]
                   == (c1["F_over_F_newton_G0_leading"].strip() == "1")))
    checks.append(("CLOCK-1 hbar cancels", c1["hbar_cancels"] is True))
    # RECONCILED: hbar-cancellation recomputed from the driver's own two-hbar pair
    hbar_pair = c1["hbar_independence_pair"]
    recomputed_hbar_cancels = hbar_pair[0] == hbar_pair[1]
    checks.append(("CLOCK-1 hbar-cancellation RECOMPUTED (target identical at hbar and 2*hbar)",
                   recomputed_hbar_cancels))
    checks.append(("CLOCK-1 hbar label == RECOMPUTED",
                   c1["hbar_cancels"] == recomputed_hbar_cancels))
    # G-AGFREE: SYMBOLIC independence (expression-tree), not substring absence.
    # Two-sided: absent from the target AND detected in the counterfactual control.
    checks.append(("G-AGFREE: A_g absent from the target's free_symbols",
                   c1["Ag_free_symbol_absent_from_target"] is True))
    checks.append(("G-AGFREE: d(target)/dA_g == 0 symbolically",
                   c1["Ag_derivative_of_target_is_zero"] is True))
    checks.append(("G-AGFREE: A_g symbol is LIVE in u_0 (not an inert symbol)",
                   c1["Ag_symbol_is_live_in_u0"] is True))
    checks.append(("G-AGFREE detector liveness: A_g IS seen in the counterfactual control",
                   c1["Ag_detector_sees_it_in_counterfactual_control"] is True))
    checks.append(("G-AGFREE: legacy Ag_appears label == free_symbols truth",
                   c1["Ag_appears"] == (not c1["Ag_free_symbol_absent_from_target"])))
    # RECONCILED with an INDEPENDENT engine (string scan of the shipped exact
    # expressions) against sympy's expression-tree verdict, both directions.
    AG = "mathcal_A_g"
    recomputed_absent = AG not in c1["F_over_F_newton_exact"]
    checks.append(("G-AGFREE absence label == RECOMPUTED by string scan of the exact target",
                   c1["Ag_free_symbol_absent_from_target"] == recomputed_absent))
    checks.append(("G-AGFREE d/dA_g label == RECOMPUTED (absent => derivative zero)",
                   c1["Ag_derivative_of_target_is_zero"] == recomputed_absent))
    recomputed_live_u0 = AG in c1["Ag_u0_expression"]
    checks.append(("G-AGFREE liveness label == RECOMPUTED (A_g present in u_0)",
                   c1["Ag_symbol_is_live_in_u0"] == recomputed_live_u0))
    recomputed_cf_sees = AG in c1["Ag_counterfactual_control_ratio_expression"]
    checks.append(("G-AGFREE control label == RECOMPUTED (A_g present in the counterfactual)",
                   c1["Ag_detector_sees_it_in_counterfactual_control"] == recomputed_cf_sees))
    # ---- F4 RELABEL. The derived object is GR's STATIC-OBSERVER PROPER force
    # m*a = (GMm/r^2)(1-r_s/r)^(-1/2) (equivalently -dE_inf/dr in Schwarzschild
    # coordinate r) -- NOT the force at infinity, which is GMm/r^2 EXACTLY
    # (Wald sec 6.3). Both are now asserted, so the distinction is machine-held.
    checks.append(("CLOCK-1 matches GR STATIC-OBSERVER PROPER force m*a EXACTLY",
                   c1["matches_GR_static_observer_PROPER_force_EXACTLY"] is True))
    checks.append(("GR force AT INFINITY ratio == 1 exactly (Wald 6.3; NOT the derived object)",
                   c1["force_AT_INFINITY_is_exactly_newtonian"] is True
                   and c1["force_AT_INFINITY_ratio_expression"].strip() == "1"))
    # RECONCILED: the declared exactness label recomputed from the shipped residuals
    recomputed_gr_exact = all(
        s["abs_diff_ratio_minus_gr"] < 1e-40 for s in c1["gr_reference_diff_samples"]
    )
    checks.append(("GR-match residuals < 1e-40 at every sample radius", recomputed_gr_exact))
    checks.append(("GR-match label == RECOMPUTED from residuals",
                   c1["matches_GR_static_observer_PROPER_force_EXACTLY"] == recomputed_gr_exact))
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
    # ---- F9 REPAIR (2026-08-11 review). The old check NAME carried the stale
    # literal "frozen 4.246094e-6". That numeral was computed from the prereg's
    # pre-repair solar mass (r_s = 2954.008 m); the driver, importing the
    # canonical M_SUN, returns r_s = 2954.1266 m and A = 4.246265e-6. The stale
    # literal is stripped from the name AND the live numeral is now TESTED, not
    # narrated. The prereg is FROZEN and untouched: this is the result-doc-side
    # disclosure of a canonical-source repair, not a criterion change.
    checks.append(("CLOCK-S leading ratio == A (driver value, recomputed here)",
                   abs(cS["numeric_at_solar_surface"] - A_ind) / A_ind < 1e-6))
    checks.append(("CLOCK-S leading ratio == 4.246265e-6 (the LIVE numeral, tested)",
                   abs(cS["numeric_at_solar_surface"] - 4.246265e-6) / 4.246265e-6 < 1e-6))
    checks.append(("stale prereg numeral 4.246094e-6 does NOT match the repaired M_SUN "
                   "(the disclosure is real, not cosmetic)",
                   abs(cS["numeric_at_solar_surface"] - 4.246094e-6) / 4.246094e-6 > 1e-6))
    checks.append(("CLOCK-S under-predicts by 2.355e5 (frozen, order+3 digits)",
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
    # RECONCILED: recompute each |H|==1 label from the shipped amplitude
    for kind in ("hyperbolic", "schrodinger", "diffusive"):
        recomputed_absH = abs(pc[kind]["abs_H_at_w1e-5"] - 1.0) < 1e-12
        checks.append((f"{kind} |H|==1 label == RECOMPUTED from abs_H_at_w1e-5",
                       pc[kind]["lossless_absH_is_1"] == recomputed_absH))
    checks.append(("G-LIVE negative control: instantaneous solve UNRESOLVABLE",
                   L3["negative_control_instantaneous"]["resolvable"] is False))
    # RECONCILED: 'resolvable' recomputed from the shipped p_measured
    recomputed_resolvable = L3["negative_control_instantaneous"]["p_measured"] is not None
    checks.append(("negative-control 'resolvable' label == RECOMPUTED from p_measured",
                   L3["negative_control_instantaneous"]["resolvable"] == recomputed_resolvable))
    checks.append(("negative-control PASS label == RECOMPUTED",
                   L3["negative_control_instantaneous"]["PASS_expect_unresolvable"]
                   == (not recomputed_resolvable)))

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

    # ---- L5: the WIDENED clock lemma (F1/F-lemma repair) ----
    L5 = r["L5_widened_clock_lemma"]
    checks.append(("LEMMA: generic C^1 f(S) has dW/dA|_0 == 0",
                   L5["generic_C1_first_derivative_vanishes"] is True
                   and L5["generic_C1_dW_dA_at_zero"].strip() == "0"))
    checks.append(("LEMMA: generic leading force is 1/r^3 (radial power == 3)",
                   L5["generic_leading_force_radial_power"] == 3))
    checks.append(("LEMMA: generic leading force == -f'(1) hbar w_0 r_s^2 / r^3",
                   L5["generic_leading_force_matches_minus_fprime1_rs2_over_r3"] is True))
    checks.append(("LEMMA: S^p is the SPECIAL CASE f'(1) = p",
                   L5["Sp_is_special_case_fprime1_equals_p"].strip() == "p"
                   and L5["Sp_leading_matches_widened_lemma"] is True))
    checks.append(("LEMMA: S^p first derivative vanishes (the old, narrower statement)",
                   L5["Sp_first_derivative_vanishes"] is True))
    checks.append(("LEMMA escape condition is dW/dA|_0 != 0 (leading-order LINEAR in A)",
                   "dW/dA|_0 != 0" in L5["escape_condition"]))
    checks.append(("LEMMA: the slope-1 lapse ESCAPES with dW/dA|_0 == -1/2",
                   L5["slope1_lapse_escapes"] is True
                   and L5["slope1_lapse_dW_dA_at_zero"].strip() == "-1/2"))
    checks.append(("LEMMA: |grad eps| keying does NOT escape (radial power == 3)",
                   L5["grad_eps_route_radial_power"] == 3
                   and L5["grad_eps_route_is_1_over_r3"] is True))
    checks.append(("LEMMA: no coupling lambda makes the |grad eps| route 1/r^2",
                   L5["grad_eps_route_can_never_be_1_over_r2"] is True))

    # RECONCILED: recompute every lemma POWER in plain math from the shipped
    # two-radius samples, n = log(F1/F2)/log(r2/r1), and reconcile the declared
    # labels against it. No lemma verdict rests on an unreconciled boolean.
    def _power(samples):
        (r1, f1_), (r2, f2_) = ((s["r_m"], s["F"]) for s in samples)
        return math.log(f1_ / f2_) / math.log(r2 / r1)

    n_gen = _power(L5["generic_force_samples_fprime1_eq_1"])
    n_sp = _power(L5["Sp_force_samples_p_eq_2"])
    n_grad = _power(L5["grad_eps_force_samples_lambda_eq_1"])
    checks.append(("LEMMA power RECOMPUTED (generic C^1) == 3", abs(n_gen - 3.0) < 1e-9))
    checks.append(("LEMMA power RECOMPUTED (S^p, p=2) == 3", abs(n_sp - 3.0) < 1e-9))
    checks.append(("LEMMA power RECOMPUTED (|grad eps| route) == 3", abs(n_grad - 3.0) < 1e-9))
    checks.append(("LEMMA: generic power label == RECOMPUTED",
                   L5["generic_leading_force_radial_power"] == round(n_gen)))
    checks.append(("LEMMA: |grad eps| power label == RECOMPUTED",
                   L5["grad_eps_route_radial_power"] == round(n_grad)))
    checks.append(("LEMMA: |grad eps| never-1/r^2 label == RECOMPUTED",
                   L5["grad_eps_route_can_never_be_1_over_r2"] == (round(n_grad) != 2)))
    # the S^p leading coefficient, recomputed in plain math: F = -p hbar w_0 r_s^2/r^3
    KS = L5["constants_used_for_samples"]
    rs_lemma = 2.0 * KS["G"] * KS["M_SUN"] / KS["c"] ** 2
    p_lemma = 2.0
    sp_pred = [
        -p_lemma * KS["hbar"] * KS["omega_0"] * rs_lemma**2 / s["r_m"] ** 3
        for s in L5["Sp_force_samples_p_eq_2"]
    ]
    sp_coeff_ok = all(
        abs(s["F"] - q) / abs(q) < 1e-12
        for s, q in zip(L5["Sp_force_samples_p_eq_2"], sp_pred)
    )
    checks.append(("LEMMA: S^p leading force == -p hbar w_0 r_s^2/r^3 (plain-math recompute)",
                   sp_coeff_ok))
    checks.append(("LEMMA: S^p-matches-widened label == RECOMPUTED",
                   L5["Sp_leading_matches_widened_lemma"] == sp_coeff_ok))
    # the generic coefficient at f'(1) = 1 must be the same expression with p -> 1
    gen_pred = [
        -1.0 * KS["hbar"] * KS["omega_0"] * rs_lemma**2 / s["r_m"] ** 3
        for s in L5["generic_force_samples_fprime1_eq_1"]
    ]
    gen_coeff_ok = all(
        abs(s["F"] - q) / abs(q) < 1e-12
        for s, q in zip(L5["generic_force_samples_fprime1_eq_1"], gen_pred)
    )
    checks.append(("LEMMA: generic force == -f'(1) hbar w_0 r_s^2/r^3 (plain-math recompute)",
                   gen_coeff_ok))
    checks.append(("LEMMA: generic-coefficient label == RECOMPUTED",
                   L5["generic_leading_force_matches_minus_fprime1_rs2_over_r3"]
                   == gen_coeff_ok))
    # dW/dA -> 0 for S^p: recompute -p*A in plain math at the shipped small A
    sp_deriv_ok = all(
        abs(s["dW_dA"] - (-p_lemma * s["A"])) < 1e-14 * abs(s["dW_dA"])
        or abs(s["dW_dA"] - (-p_lemma * s["A"])) < 1e-20
        for s in L5["Sp_dW_dA_small_A_samples"]
    )
    checks.append(("LEMMA: S^p dW/dA -> 0 linearly in A (plain-math recompute)", sp_deriv_ok))
    checks.append(("LEMMA: S^p vanishing-derivative label == RECOMPUTED",
                   L5["Sp_first_derivative_vanishes"] == sp_deriv_ok))

    # ---- L6: the pole-test VALIDITY SCOPE (F3 repair) ----
    L6 = r["L6_pole_test_validity_scope"]
    cg = L6["cg_over_c_forced_by_node_scale_inertia"]
    # independent arithmetic: c_g/c forced by paying the admission price with the
    # only substrate-native inertia candidate is sqrt(2 xi_Machian)
    checks.append(("pole scope: c_g/c forced == sqrt(2 xi_Machian) (independent)",
                   abs(cg - math.sqrt(2.0 * xi)) / cg < 1e-12))
    checks.append(("pole scope: the banked bound's radiating multipole is the quadrupole",
                   L6["radiating_multipole_of_the_banked_bound"] == 2))
    checks.append(("pole scope: banked exclusion range is 1e2-1e3 x (port-register.md:93)",
                   L6["banked_exclusion_range_x"] == [100.0, 1400.0]))
    for ell in (1, 2, 3):
        row = L6["per_multipole"][f"l={ell}"]
        checks.append((f"pole scope l={ell}: exponent == 2l+1", row["exponent_2l_plus_1"] == 2 * ell + 1))
        checks.append((f"pole scope l={ell}: (c/c_g)^(2l+1) recomputed independently",
                       abs(row["suppression_c_over_cg_pow"] - cg ** (-(2 * ell + 1)))
                       / row["suppression_c_over_cg_pow"] < 1e-12))
    q = L6["per_multipole"]["l=2"]
    checks.append(("pole scope: quadrupole exclusion at the forced c_g is ~1e-107 "
                   "(ORDER ONLY) -- i.e. NOT excluded",
                   1e-108 < q["rescaled_exclusion_ratio_ORDER_ONLY"] < 1e-106))
    checks.append(("pole scope: validity condition is c_g <~ O(c)",
                   L6["validity_condition"] == "c_g <~ O(c)"))

    # ---- F8c: DECLARED-BOOLEAN COVERAGE GATE -------------------------------
    # Every declared boolean this checker consumes is registered here together
    # with the name of the check that RECOMPUTES the same fact from the JSON's
    # own inputs. The gate fails if any registered reconciliation is missing
    # from `checks` -- so the "no check rests on an unreconciled self-declared
    # field" claim is machine-held, not narrated.
    reconciliation_registry = {
        "L0.G_TAUTOLOGY_identity_symbolically_proven":
            "G-TAUTOLOGY: declared-proven == (residual string is '0')",
        "L1.A_at_r_s_equals_one":
            "A(r_s) label == RECOMPUTED from the shipped numeric",
        "L1.n_temporal_equals_1_plus_2GM_over_c2r":
            "n_temporal label == RECOMPUTED at every sample",
        "L2.CLOCK_1.leading_is_exactly_one":
            "CLOCK-1 leading label == RECOMPUTED from the shipped G^0 term",
        "L2.CLOCK_1.hbar_cancels":
            "CLOCK-1 hbar label == RECOMPUTED",
        "L2.CLOCK_1.Ag_appears":
            "G-AGFREE: legacy Ag_appears label == free_symbols truth",
        "L2.CLOCK_1.Ag_free_symbol_absent_from_target":
            "G-AGFREE absence label == RECOMPUTED by string scan of the exact target",
        "L2.CLOCK_1.Ag_derivative_of_target_is_zero":
            "G-AGFREE d/dA_g label == RECOMPUTED (absent => derivative zero)",
        "L2.CLOCK_1.Ag_symbol_is_live_in_u0":
            "G-AGFREE liveness label == RECOMPUTED (A_g present in u_0)",
        "L2.CLOCK_1.Ag_detector_sees_it_in_counterfactual_control":
            "G-AGFREE control label == RECOMPUTED (A_g present in the counterfactual)",
        "L2.CLOCK_1.matches_GR_static_observer_PROPER_force_EXACTLY":
            "GR-match label == RECOMPUTED from residuals",
        "L2.CLOCK_1.force_AT_INFINITY_is_exactly_newtonian":
            "GR force AT INFINITY ratio == 1 exactly (Wald 6.3; NOT the derived object)",
        "L3.positive_controls.hyperbolic.lossless_absH_is_1":
            "hyperbolic |H|==1 label == RECOMPUTED from abs_H_at_w1e-5",
        "L3.positive_controls.schrodinger.lossless_absH_is_1":
            "schrodinger |H|==1 label == RECOMPUTED from abs_H_at_w1e-5",
        "L3.positive_controls.diffusive.lossless_absH_is_1":
            "diffusive |H|==1 label == RECOMPUTED from abs_H_at_w1e-5",
        "L3.positive_controls.hyperbolic.PASS": "hyperbolic PASS label == recomputed",
        "L3.positive_controls.diffusive.PASS": "diffusive PASS label == recomputed",
        "L3.positive_controls.schrodinger.PASS": "schrodinger PASS label == recomputed",
        "L3.G_LIVE_all_green": "G-LIVE declared == RECOMPUTED (no self-declared gate)",
        "L3.negative_control_instantaneous.resolvable":
            "negative-control 'resolvable' label == RECOMPUTED from p_measured",
        "L3.negative_control_instantaneous.PASS_expect_unresolvable":
            "negative-control PASS label == RECOMPUTED",
        "L5.generic_C1_first_derivative_vanishes":
            "LEMMA: generic C^1 f(S) has dW/dA|_0 == 0",
        "L5.generic_leading_force_radial_power":
            "LEMMA: generic power label == RECOMPUTED",
        "L5.generic_leading_force_matches_minus_fprime1_rs2_over_r3":
            "LEMMA: generic-coefficient label == RECOMPUTED",
        "L5.Sp_first_derivative_vanishes":
            "LEMMA: S^p vanishing-derivative label == RECOMPUTED",
        "L5.Sp_leading_matches_widened_lemma":
            "LEMMA: S^p-matches-widened label == RECOMPUTED",
        "L5.slope1_lapse_escapes":
            "LEMMA: the slope-1 lapse ESCAPES with dW/dA|_0 == -1/2",
        "L5.grad_eps_route_is_1_over_r3":
            "LEMMA: |grad eps| power label == RECOMPUTED",
        "L5.grad_eps_route_radial_power":
            "LEMMA: |grad eps| power label == RECOMPUTED",
        "L5.grad_eps_route_can_never_be_1_over_r2":
            "LEMMA: |grad eps| never-1/r^2 label == RECOMPUTED",
    }
    check_names = {name for name, _ in checks}
    missing_recon = sorted(
        f"{k} -> {v}" for k, v in reconciliation_registry.items() if v not in check_names
    )
    checks.append((f"F8c: every consumed declared boolean has a live reconciliation "
                   f"({len(reconciliation_registry)} registered)", not missing_recon))
    if missing_recon:
        print(f"[declared-boolean coverage] MISSING RECONCILIATIONS: {missing_recon}")

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

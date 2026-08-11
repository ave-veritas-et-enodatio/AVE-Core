#!/usr/bin/env python3
"""Driver for the bias propagation theorem lane (R49b/R50).

Governed by research/2026-08-10_bias-propagation_prereg-FROZEN.md, committed and
pushed ALONE at d4bee683 before this file existed (freeze-by-push).

This driver produces receipts for the frozen criteria ONLY. It adjudicates
nothing on its own; every bin is awarded in the result doc against the frozen
grammar.

Legs
----
L0  canonical-constant provenance + the G-TAUTOLOGY identity, symbolically.
L1  the Ax4 dialect-consistency check: A = (2/7) eps_11 => A = 1 at r = r_s.
L2  the two clock branches (deliverable 2), sympy-exact, both engines.
L3  the near-zone frequency-response instrument (deliverable 1) with its FROZEN
    liveness set: three analytic positive controls + one negative control.
L4  the bias-inertia magnitude the LC-HYPERBOLIC bin must pay for.
L5  the WIDENED clock lemma: any C^1 W = f(S) with f'(1) finite dies (S^p is a
    proper subset); the escape condition dW/dA|_0 != 0; the |grad eps| non-escape.
L6  the pole-test VALIDITY SCOPE: the (c/c_g)^(2l+1) suppression that bounds where
    the banked pulsar exclusion can be read at all.

Two engines wherever a number carries a verdict: sympy exact symbolics and an
independent mpmath 50-digit numeric arm. Engine `src/ave` is never imported for
dynamics -- only `ave.core.constants` is read, per ave-canonical-source.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
import tempfile
from pathlib import Path

import mpmath as mp
import sympy as sp

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "src"))

from ave.core.constants import (  # noqa: E402  canonical source, never hard-coded
    C_0,
    G,
    HBAR,
    L_NODE,
    M_E,
    M_SUN,
    RHO_BULK,
    XI_MACHIAN,
)

mp.mp.dps = 50

OUT = Path(__file__).with_name("bias_propagation_lane_results.json")


# --------------------------------------------------------------------------
# L0 -- constants, kappa, and the G-TAUTOLOGY identity
# --------------------------------------------------------------------------
def leg0(mutate: bool = False) -> dict:
    kappa = C_0**4 / (7.0 * G)
    inertia_req = kappa / C_0**2  # kg/m, the bias inertia for c_g = c
    ratio = inertia_req / (RHO_BULK * L_NODE**2)

    if mutate:  # --mutation-receipt: perturb a load-bearing number
        kappa *= 1.000001

    # --- the identity, proven symbolically (NOT asserted) ---
    c, Gs, me, ln, pi_ = sp.symbols("c G m_e ell_node pi", positive=True)
    # canon definitions (see src/ave/core/constants.py:757-758 and the
    # T_max,g = xi * T_EM = c^4/7G chain with T_EM = m_e c^2 / ell_node)
    rho_sym = me / (2 * ln**3)          # RHO_BULK reduces to this (checked below)
    xi_sym = c**2 * ln / (7 * Gs * me)  # XI_MACHIAN from T_max,g = xi T_EM
    inertia_sym = c**2 / (7 * Gs)       # = kappa/c^2
    identity_residual = sp.simplify(inertia_sym - 2 * xi_sym * rho_sym * ln**2)
    identity_holds = identity_residual == 0

    # the two numeric premises of that reduction, checked against constants.py
    rho_from_me = M_E / (2.0 * L_NODE**3)
    xi_from_chain = C_0**2 * L_NODE / (7.0 * G * M_E)

    return {
        "kappa_N": kappa,
        "inertia_required_for_cg_eq_c_kg_per_m": inertia_req,
        "inertia_over_rho_lnode2": ratio,
        "xi_machian": XI_MACHIAN,
        "ratio_over_xi": ratio / XI_MACHIAN,
        "G_TAUTOLOGY_identity_symbolically_proven": bool(identity_holds),
        "G_TAUTOLOGY_residual": str(identity_residual),
        "premise_rho_bulk_eq_me_over_2lnode3_relerr": abs(rho_from_me - RHO_BULK) / RHO_BULK,
        "premise_xi_eq_c2_lnode_over_7Gme_relerr": abs(xi_from_chain - XI_MACHIAN) / XI_MACHIAN,
        "verdict": (
            "DEFINITIONAL IDENTITY: inertia_required = 2 * xi_Machian * rho_bulk * "
            "ell_node^2 reduces to c^2/7G symbolically. NOT a structural coincidence."
        ),
    }


# --------------------------------------------------------------------------
# L1 -- Ax4 dialect consistency: A = (2/7) eps_11 must hit A = 1 at r_s
# --------------------------------------------------------------------------
def leg1() -> dict:
    Gs, M, c, r = sp.symbols("G M c r", positive=True)
    eps11 = 7 * Gs * M / (c**2 * r)            # gordon-optical-metric.md:33
    A = sp.Rational(2, 7) * eps11              # nu_vac = 2/7 projection
    r_s = 2 * Gs * M / c**2                    # Schwarzschild radius
    A_at_rs = sp.simplify(A.subs(r, r_s))
    n_temporal = 1 + sp.Rational(2, 7) * eps11  # slope-2 bulk/propagation index
    return {
        "eps11": sp.srepr(eps11) and str(eps11),
        "A_definition": str(A),
        "A_at_r_s": str(A_at_rs),
        "A_at_r_s_equals_one": bool(sp.simplify(A_at_rs - 1) == 0),
        "n_temporal_at_r": str(sp.simplify(n_temporal)),
        "n_temporal_equals_1_plus_2GM_over_c2r": bool(
            sp.simplify(n_temporal - (1 + 2 * Gs * M / (c**2 * r))) == 0
        ),
        # --- RECONCILIATION MATERIAL (no declared boolean is the sole basis of a
        # check; the number check recomputes each of these in plain `math`) ---
        "A_at_r_s_numeric": float(sp.N(A.subs(r, r_s))),
        "n_temporal_samples": [
            # constants CANONICAL (never hard-coded); the sample radii are pure
            # evaluation points for a two-engine reconciliation, not comparators.
            {
                "G": G, "M": M_SUN, "c": C_0, "r": rr,
                "n_temporal": float(
                    sp.N(n_temporal.subs({Gs: G, M: M_SUN, c: C_0, r: rr}), 30)
                ),
            }
            for rr in (6.957e8, 1.0e9, 1.0e11)
        ],
        "note": (
            "Reconciles eq_axiom_4.tex ('BH event horizon eps_11(r)=1 matches "
            "Schwarzschild r_s=2GM/c^2 exactly') with the eps_11 = 7GM/c^2 r profile: "
            "Ax4's A and the profile's eps_11 differ by the factor nu_vac = 2/7."
        ),
    }


# --------------------------------------------------------------------------
# L2 -- deliverable 2: the two clock branches
# --------------------------------------------------------------------------
def leg2() -> dict:
    Gs, M, c, r, hbar, w0 = sp.symbols("G M c r hbar omega_0", positive=True)
    eps11 = 7 * Gs * M / (c**2 * r)
    A = sp.Rational(2, 7) * eps11
    m = hbar * w0 / c**2                        # Planck-Einstein resonator mass
    F_newton = -Gs * M * m / r**2               # radial component, attractive

    # CLOCK-1: canon slope-1 local clock (temporal-spatial-lattice-decomposition W2)
    w_inf_1 = w0 * sp.sqrt(1 - A)
    E1 = hbar * w_inf_1
    F1 = sp.simplify(-sp.diff(E1, r))
    ratio1_exact = sp.simplify(F1 / F_newton)
    ratio1_lead = sp.simplify(sp.limit(ratio1_exact, Gs, 0))          # G^0 term
    ratio1_1pn = sp.simplify(sp.series(ratio1_exact, Gs, 0, 2).removeO())
    # GR cross-check -- NAME THE OBJECT PRECISELY (F4 repair, 2026-08-11 review).
    # The quantity derived here is -d/dr of the energy-at-infinity in SCHWARZSCHILD
    # COORDINATE r. That equals GR's static-observer PROPER force
    #     m*a = (GMm/r^2) * (1 - r_s/r)^(-1/2)
    # (the force the LOCAL static observer must exert). It is NOT the force at
    # infinity: the force applied at infinity through an ideal string is
    #     F_inf = sqrt(1 - r_s/r) * m*a = GMm/r^2  EXACTLY  (Wald sec 6.3),
    # i.e. the Newtonian expression with no correction at any order. The two
    # differ by the redshift factor, which is exactly the coordinate-r vs
    # proper-length conversion dl = dr/sqrt(1 - r_s/r). Both are emitted below.
    gr_ratio = 1 / sp.sqrt(1 - 2 * Gs * M / (c**2 * r))
    gr_match_exact = bool(sp.simplify(ratio1_exact - gr_ratio) == 0)
    # the force-AT-INFINITY ratio: multiply by the redshift factor. Must be 1.
    redshift = sp.sqrt(1 - 2 * Gs * M / (c**2 * r))
    ratio1_at_infinity = sp.simplify(ratio1_exact * redshift)
    force_at_infinity_is_exactly_newtonian = bool(
        sp.simplify(ratio1_at_infinity - 1) == 0
    )

    # --- G-AGFREE, SYMBOLICALLY (F8b repair). Introduce A_g as a live free symbol,
    # carry it through the ONE relation canon gives it (u_0 = -A_g grad eps_11),
    # and prove the deliverable-2 target is INDEPENDENT of it on the sympy
    # EXPRESSION TREE -- free_symbols membership + d/dA_g == 0 -- not by string
    # inspection of the printed form. Stated honestly: this is an INDEPENDENCE
    # proof, not the cancellation of a term that was ever present; A_g never
    # enters the energy chain E = hbar*omega_inf(A) at all.
    Ag = sp.Symbol("mathcal_A_g", positive=True)
    u0 = -Ag * sp.diff(eps11, r)                 # the ONE place A_g appears (Ax5 clause G)
    # (i) the symbol is LIVE in the construction, not inert:
    ag_live_in_u0 = bool(Ag in u0.free_symbols) and bool(sp.diff(u0, Ag) != 0)
    # (ii) the deliverable-2 target does not see it, on the expression tree:
    ag_in_target_free_symbols = bool(Ag in ratio1_exact.free_symbols)
    ag_derivative_is_zero = bool(sp.simplify(sp.diff(ratio1_exact, Ag)) == 0)
    # (iii) DETECTOR LIVENESS (the "absence where it doesn't exist" half): a
    # COUNTERFACTUAL energy chain in which the resonator energy is allowed to
    # depend on the bound response, E' = hbar*omega_inf*(1 + lam*u_0). This is
    # NOT a canon claim -- it exists only to prove the detector can SEE A_g when
    # A_g is there. If this control came out A_g-free, the gate above would be
    # vacuous.
    lam = sp.Symbol("lambda_cf", positive=True)
    E1_cf = hbar * w_inf_1 * (1 + lam * u0)
    ratio_cf = sp.simplify(sp.simplify(-sp.diff(E1_cf, r)) / F_newton)
    ag_detector_sees_it_in_control = bool(
        Ag in ratio_cf.free_symbols and sp.simplify(sp.diff(ratio_cf, Ag)) != 0
    )

    # CLOCK-S: Ax4 kernel route, c_eff = c_0 sqrt(S) = c_0 (1-A^2)^(1/4)
    w_inf_S = w0 * (1 - A**2) ** sp.Rational(1, 4)
    ES = hbar * w_inf_S
    FS = sp.simplify(-sp.diff(ES, r))
    ratioS_exact = sp.simplify(FS / F_newton)
    ratioS_lead = sp.simplify(sp.series(ratioS_exact, Gs, 0, 2).removeO())

    # numeric evaluation at the solar surface (frozen comparator of the prereg)
    # M_SUN is canonical (constants.py:132). The solar RADIUS is not a
    # canonical substrate constant -- it is an external comparator, declared
    # ENG-CHOICE(IAU nominal photospheric radius) per SVA row 5. It scales
    # only the exhibit, never a verdict: both clock branches are evaluated at
    # the same r, and the branch separation is a RATIO.
    R_SUN_ENG_CHOICE = 6.957e8  # [m] IAU nominal; comparator, not a constant
    M_sun, R_sun = M_SUN, R_SUN_ENG_CHOICE
    subs = {Gs: mp.mpf(G), M: mp.mpf(M_sun), c: mp.mpf(C_0), r: mp.mpf(R_sun),
            hbar: mp.mpf(HBAR), w0: mp.mpf(1.0)}
    f1 = mp.mpf(sp.N(ratio1_exact.subs(subs), 50))
    fS = mp.mpf(sp.N(ratioS_exact.subs(subs), 50))
    r_s_sun = 2 * G * M_sun / C_0**2
    A_sun = r_s_sun / R_sun

    # reconciliation material for the hbar-cancellation claim: evaluate the target
    # at two different hbar values. If hbar truly cancels the two are identical.
    subs_2hbar = {**subs, hbar: mp.mpf(HBAR) * 2}
    f1_2hbar = mp.mpf(sp.N(ratio1_exact.subs(subs_2hbar), 50))

    return {
        "CLOCK_1": {
            "omega_inf": str(w_inf_1),
            "F_over_F_newton_exact": str(ratio1_exact),
            "F_over_F_newton_G0_leading": str(ratio1_lead),
            "leading_is_exactly_one": bool(sp.simplify(ratio1_lead - 1) == 0),
            "F_over_F_newton_through_1PN": str(ratio1_1pn),
            # --- F4 RELABEL (2026-08-11 review). The derived object is GR's
            # static-observer PROPER force m*a, equivalently -d(E_inf)/dr in
            # Schwarzschild coordinate r -- NOT the force at infinity.
            "matches_GR_static_observer_PROPER_force_EXACTLY": gr_match_exact,
            "gr_static_observer_proper_force_ratio_expression": str(gr_ratio),
            "force_AT_INFINITY_ratio_expression": str(ratio1_at_infinity),
            "force_AT_INFINITY_is_exactly_newtonian": force_at_infinity_is_exactly_newtonian,
            "gr_object_note": (
                "m*a = (GMm/r^2)(1-r_s/r)^(-1/2) is the STATIC-OBSERVER PROPER force "
                "(= -dE_inf/dr in Schwarzschild coordinate r). The force AT INFINITY "
                "is sqrt(1-r_s/r) times it = GMm/r^2 EXACTLY, with no correction at "
                "any order (Wald sec 6.3). The redshift factor between them IS the "
                "coordinate-vs-proper-length conversion dl = dr/sqrt(1-r_s/r)."
            ),
            "pn_scope_note": (
                "What is reproduced exactly is the g_00 function in SCHWARZSCHILD "
                "COORDINATES. The spatial-metric sector (PPN gamma) is untouched by "
                "this construction and is neither imported nor tested here."
            ),
            "hbar_cancels": "hbar" not in str(sp.simplify(ratio1_exact)),
            "hbar_independence_pair": [float(f1), float(f1_2hbar)],
            # --- G-AGFREE, symbolic (F8b repair) ---
            "Ag_appears": bool(ag_in_target_free_symbols),
            "Ag_free_symbol_absent_from_target": bool(not ag_in_target_free_symbols),
            "Ag_derivative_of_target_is_zero": ag_derivative_is_zero,
            "Ag_symbol_is_live_in_u0": ag_live_in_u0,
            "Ag_u0_expression": str(u0),
            "Ag_detector_sees_it_in_counterfactual_control": ag_detector_sees_it_in_control,
            "Ag_counterfactual_control_ratio_expression": str(ratio_cf),
            "Ag_basis_note": (
                "INDEPENDENCE proof on the sympy expression tree (free_symbols "
                "membership + d/dA_g == 0), NOT a cancellation of a term that was "
                "ever present: A_g never enters E = hbar*omega_inf(A). Detector "
                "liveness shown on a declared COUNTERFACTUAL control in which the "
                "energy is allowed to depend on u_0 -- there A_g IS seen."
            ),
            "numeric_at_solar_surface": float(f1),
            "gr_reference_diff_samples": [
                {
                    "r_m": rr,
                    "abs_diff_ratio_minus_gr": float(
                        abs(sp.N((ratio1_exact - gr_ratio).subs({**subs, r: mp.mpf(rr)}), 50))
                    ),
                }
                for rr in (6.957e8, 1.0e9, 1.0e11)
            ],
        },
        "CLOCK_S": {
            "omega_inf": str(w_inf_S),
            "F_over_F_newton_exact": str(ratioS_exact),
            "F_over_F_newton_leading": str(ratioS_lead),
            "leading_equals_A": bool(
                sp.simplify(ratioS_lead - sp.Rational(2, 7) * eps11) == 0
            ),
            "numeric_at_solar_surface": float(fS),
            "underprediction_factor": float(1 / fS) if fS != 0 else None,
        },
        "solar_r_s_m": r_s_sun,
        "A_at_solar_surface": A_sun,
        "separation_orders_of_magnitude": math.log10(float(f1 / fS)) if fS != 0 else None,
    }


# --------------------------------------------------------------------------
# L3 -- deliverable 1 instrument: near-zone frequency response
#
# Observable (frozen, prereg SVA row 4): H(w) = phi(r,w) / phi_instantaneous(r,w),
# the near-zone response against the clock-free elliptic solve at the SAME plane.
#   p          = d log|Re H - 1| / d log w      (the frozen class exponent)
#   |H|        = amplitude ratio                (the Ax3 lossless test: must be 1)
#   phase slope= d log|arg H| / d log w         (independent corroborator)
# --------------------------------------------------------------------------
def _transfer(kind: str, w, r_, c_=1.0, D_=1.0, m_=1.0):
    w = mp.mpf(w)
    if kind == "hyperbolic":
        return mp.e ** (1j * w * r_ / c_)
    if kind == "diffusive":
        k = mp.sqrt(w / (2 * D_))
        return mp.e ** (-(1 + 1j) * r_ * k)
    if kind == "schrodinger":
        return mp.e ** (1j * mp.sqrt(2 * m_ * w) * r_)
    if kind == "instantaneous":
        return mp.mpf(1)  # clock-free elliptic solve: H == 1 identically
    raise ValueError(kind)


def _fit_p(kind: str, r_=1.0, w_lo=1e-6, w_hi=1e-4, n=25):
    """Log-log slope of |Re H - 1| vs w. Returns (p, floor_ratio, points)."""
    ws = [w_lo * (w_hi / w_lo) ** (i / (n - 1)) for i in range(n)]
    xs, ys = [], []
    for w in ws:
        H = _transfer(kind, w, r_)
        resid = abs(mp.re(H) - 1)
        if resid == 0:
            continue
        xs.append(mp.log(w))
        ys.append(mp.log(resid))
    if len(xs) < 3:
        return None, None, len(xs)
    n_ = len(xs)
    mx, my = sum(xs) / n_, sum(ys) / n_
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = sum((x - mx) ** 2 for x in xs)
    p = num / den
    # instrument floor: the smallest residual resolved, vs 50-digit precision
    floor = mp.mpf(10) ** (-mp.mp.dps + 2)
    smallest = mp.e ** min(ys)
    return float(p), float(smallest / floor), n_


def leg3() -> dict:
    # FROZEN liveness set (prereg section 5). All must read correctly before any
    # lane p is bookable. UNRUN != PASSED.
    frozen_bands = {
        "hyperbolic": (2.0, 0.2),
        "diffusive": (0.5, 0.15),
        "schrodinger": (1.0, 0.2),
    }
    controls = {}
    all_green = True
    for kind, (target, tol) in frozen_bands.items():
        p, floor_ratio, npts = _fit_p(kind)
        ok = p is not None and abs(p - target) <= tol
        all_green &= ok
        H1 = _transfer(kind, 1e-5, 1.0)
        controls[kind] = {
            "p_measured": p,
            "p_frozen_target": target,
            "p_frozen_tol": tol,
            "PASS": bool(ok),
            "abs_H_at_w1e-5": float(abs(H1)),
            "lossless_absH_is_1": bool(abs(abs(H1) - 1) < 1e-12),
            "points": npts,
            "resid_over_floor": floor_ratio,
        }

    # NEGATIVE control: the clock-free elliptic solve must show NO resolvable p.
    p_neg, floor_neg, npts_neg = _fit_p("instantaneous")
    negative_ok = p_neg is None
    all_green &= negative_ok

    return {
        "positive_controls": controls,
        "negative_control_instantaneous": {
            "p_measured": p_neg,
            "resolvable": p_neg is not None,
            "PASS_expect_unresolvable": bool(negative_ok),
            "points_above_floor": npts_neg,
        },
        "G_LIVE_all_green": bool(all_green),
        "amplitude_test_note": (
            "|H| = 1 for hyperbolic and schrodinger (lossless); |H| < 1 for "
            "diffusive. This is the Ax3 port test: a diffusive bias line loses "
            "amplitude, which requires a named boundary-crossing port."
        ),
    }


# --------------------------------------------------------------------------
# L4 -- the LC-HYPERBOLIC admission price
# --------------------------------------------------------------------------
def leg4() -> dict:
    kappa = C_0**4 / (7.0 * G)
    inertia_req = kappa / C_0**2
    return {
        "inertia_required_kg_per_m": inertia_req,
        "substrate_rho_bulk_kg_per_m3": RHO_BULK,
        "inertia_over_rho_bulk_m2": inertia_req / RHO_BULK,
        "implied_length_scale_m": math.sqrt(inertia_req / RHO_BULK),
        "l_node_squared_m2": L_NODE**2,
        "implied_over_lnode2": (inertia_req / RHO_BULK) / L_NODE**2,
        "note": (
            "The LC-HYPERBOLIC bin's admission price: a fast-layer object with "
            "inertia density 1.92e26 kg/m. The substrate's own bulk inertia is "
            "RHO_BULK = 7.91e6 kg/m^3; the required inertia corresponds to an "
            "area 2.43e19 m^2 (length 4.93e9 m), which is 1.63e44 x ell_node^2. "
            "Whether the fast layer supplies this is the derivation, not this number."
        ),
    }


# --------------------------------------------------------------------------
# L5 -- the WIDENED clock lemma (F1/F-lemma repair, 2026-08-11 review)
#
# The result doc's original lemma was stated for the one-parameter family
# W = S^p. That family is a PROPER SUBSET of what actually dies. The widened
# statement, proven here:
#
#   For ANY C^1 function f with f'(1) finite, the clock law W = f(S(A)) on
#   Axiom 4's kernel S(A) = sqrt(1-A^2) has dW/dA|_0 = 0 identically, because
#   dS/dA|_0 = 0. Hence the leading force is
#       F = -hbar*omega_0 * f'(1) * r_s^2 / r^3      (1/r^3, NOT 1/r^2)
#   and no such clock can produce Newtonian gravity at all.
#   S^p is the special case f'(1) = p, reproducing F = -p*hbar*omega_0*r_s^2/r^3.
#
#   ESCAPE CONDITION: dW/dA|_0 != 0, i.e. the clock must be LEADING-ORDER LINEAR
#   in A. Since S = 1 - A^2/2 + O(A^4) is quadratic in A, no C^1 f(S) achieves
#   it; the escape requires f'(1) -> infinity (non-C^1 at S=1). The surviving
#   realization is the slope-1 lapse W = sqrt(1-A), dW/dA|_0 = -1/2.
#
#   NAMED NON-ESCAPE: keying the clock on the observable GRADIENT |grad eps_11|
#   instead (canon's "only spatial gradients of A are observable" rescue) also
#   fails: |grad eps_11| = 7GM/c^2 r^2, so a clock linear in it gives F ~ 1/r^3
#   again. Verified symbolically below.
# --------------------------------------------------------------------------
def _radial_power(expr, r, lo: int = 0, hi: int = 8) -> int:
    """Smallest n in [lo, hi] with expr * r**n free of r, i.e. expr ~ 1/r**n."""
    for n in range(lo, hi + 1):
        if r not in sp.simplify(expr * r**n).free_symbols:
            return n
    raise ValueError(f"no pure 1/r**n form found for {expr}")


def leg5() -> dict:
    Aa = sp.Symbol("A", positive=True)
    Gs, M, c, r, hbar, w0 = sp.symbols("G M c r hbar omega_0", positive=True)
    S = sp.sqrt(1 - Aa**2)

    # (a) generic C^1 f: dW/dA at A=0
    f = sp.Function("f")
    W_gen = f(S)
    dW_gen = sp.diff(W_gen, Aa)
    dW_gen_at_0 = sp.simplify(dW_gen.subs(Aa, 0))
    generic_first_derivative_vanishes = bool(dW_gen_at_0 == 0)

    # (b) the surviving second-order coefficient: W ~ f(1) - (1/2) f'(1) A^2
    fp = sp.Symbol("fprime1", real=True)   # stands for f'(1)
    W_quad = sp.Symbol("f1", real=True) - sp.Rational(1, 2) * fp * Aa**2
    A_of_r = 2 * Gs * M / (c**2 * r)       # A = r_s/r
    r_s_sym = 2 * Gs * M / c**2
    E_quad = hbar * w0 * W_quad.subs(Aa, A_of_r)
    F_quad = sp.simplify(-sp.diff(E_quad, r))
    F_quad_target = sp.simplify(-hbar * w0 * fp * r_s_sym**2 / r**3)
    generic_force_matches_1_over_r3 = bool(sp.simplify(F_quad - F_quad_target) == 0)
    generic_force_power = _radial_power(F_quad, r)

    # (c) S^p as the SPECIAL CASE f'(1) = p
    p = sp.Symbol("p", positive=True)
    W_p = S**p
    dWp_at_0 = sp.simplify(sp.diff(W_p, Aa).subs(Aa, 0))
    Sp_first_derivative_vanishes = bool(dWp_at_0 == 0)
    E_p = hbar * w0 * (W_p.subs(Aa, A_of_r))
    F_p = sp.simplify(-sp.diff(E_p, r))
    F_p_leading = sp.simplify(sp.series(F_p, Gs, 0, 3).removeO())
    Sp_leading_matches_generic = bool(
        sp.simplify(F_p_leading - (-p * hbar * w0 * r_s_sym**2 / r**3)) == 0
    )
    # f'(1) for f(S) = S^p is p -- the widened lemma's coefficient specialises
    fprime1_of_Sp = sp.simplify(sp.diff(sp.Symbol("s")**p, sp.Symbol("s")).subs(sp.Symbol("s"), 1))

    # (d) the ESCAPE: the slope-1 lapse is leading-order LINEAR in A
    W_lapse = sp.sqrt(1 - Aa)
    dW_lapse_at_0 = sp.simplify(sp.diff(W_lapse, Aa).subs(Aa, 0))
    lapse_escapes = bool(dW_lapse_at_0 != 0)

    # (e) the NAMED NON-ESCAPE: a clock keyed on |grad eps_11|
    lam = sp.Symbol("lambda_g", positive=True)
    eps11 = 7 * Gs * M / (c**2 * r)
    grad_eps_mag = sp.simplify(-sp.diff(eps11, r))          # = 7GM/c^2 r^2 > 0
    W_grad = 1 - lam * grad_eps_mag
    F_grad = sp.simplify(-sp.diff(hbar * w0 * W_grad, r))
    grad_force_power = _radial_power(F_grad, r)
    grad_route_is_1_over_r3 = bool(
        sp.simplify(F_grad - (-2 * lam * hbar * w0 * 7 * Gs * M / (c**2 * r**3))) == 0
    )
    # the power is independent of lambda: F_grad * r^3 is free of BOTH r and lam's
    # ability to move it, so no choice of the coupling recovers a 1/r^2 law.
    grad_route_can_never_be_newtonian = bool(
        r not in sp.simplify(F_grad * r**3).free_symbols and grad_force_power != 2
    )

    # --- RECONCILIATION MATERIAL: numeric samples so the number check can
    # recompute the radial POWERS and the lemma coefficients in plain `math`,
    # instead of consuming a declared boolean. Constants canonical; f'(1) = 1,
    # p = 2 and lambda_g = 1 are pure evaluation choices, not comparators.
    ev = {Gs: G, M: M_SUN, c: C_0, hbar: HBAR, w0: 1.0}
    radii = (1.0e9, 2.0e9)
    generic_samples = [
        {"r_m": rr, "F": float(sp.N(F_quad.subs({**ev, fp: 1.0, r: rr}), 30))}
        for rr in radii
    ]
    Sp_samples = [
        {"r_m": rr, "F": float(sp.N(F_p_leading.subs({**ev, p: 2.0, r: rr}), 30))}
        for rr in radii
    ]
    grad_samples = [
        {"r_m": rr, "F": float(sp.N(F_grad.subs({**ev, lam: 1.0, r: rr}), 30))}
        for rr in radii
    ]
    # dW/dA at small A for W = S^p (p = 2): must vanish linearly in A
    Sp_dWdA_small_A = [
        {"A": aa, "dW_dA": float(sp.N(sp.diff(W_p, Aa).subs({p: 2.0, Aa: aa}), 30))}
        for aa in (1e-6, 1e-8)
    ]

    return {
        "kernel": str(S),
        "constants_used_for_samples": {"G": G, "M_SUN": M_SUN, "c": C_0, "hbar": HBAR,
                                       "omega_0": 1.0},
        "generic_force_samples_fprime1_eq_1": generic_samples,
        "Sp_force_samples_p_eq_2": Sp_samples,
        "grad_eps_force_samples_lambda_eq_1": grad_samples,
        "Sp_dW_dA_small_A_samples": Sp_dWdA_small_A,
        "generic_C1_dW_dA_at_zero": str(dW_gen_at_0),
        "generic_C1_first_derivative_vanishes": generic_first_derivative_vanishes,
        "generic_leading_force": str(F_quad),
        "generic_leading_force_matches_minus_fprime1_rs2_over_r3":
            generic_force_matches_1_over_r3,
        "generic_leading_force_radial_power": generic_force_power,
        "Sp_is_special_case_fprime1_equals_p": str(fprime1_of_Sp),
        "Sp_first_derivative_vanishes": Sp_first_derivative_vanishes,
        "Sp_leading_force": str(F_p_leading),
        "Sp_leading_matches_widened_lemma": Sp_leading_matches_generic,
        "escape_condition": "dW/dA|_0 != 0  (the clock must be LEADING-ORDER LINEAR in A)",
        "slope1_lapse_dW_dA_at_zero": str(dW_lapse_at_0),
        "slope1_lapse_escapes": lapse_escapes,
        "grad_eps_route_force": str(F_grad),
        "grad_eps_route_radial_power": grad_force_power,
        "grad_eps_route_is_1_over_r3": grad_route_is_1_over_r3,
        "grad_eps_route_can_never_be_1_over_r2": grad_route_can_never_be_newtonian,
        "verdict": (
            "WIDENED: every C^1 clock law W = f(S) with f'(1) finite gives a 1/r^3 "
            "leading force and cannot produce Newtonian gravity. S^p is the special "
            "case f'(1) = p. The escape is dW/dA|_0 != 0, which no C^1 f(S) supplies "
            "(S is quadratic in A at the origin); the surviving realization in canon "
            "is the slope-1 lapse sqrt(1-A). Keying on |grad eps_11| does NOT escape: "
            "it returns 1/r^3 as well."
        ),
    }


# --------------------------------------------------------------------------
# L6 -- the pole-test VALIDITY SCOPE (F3 repair, 2026-08-11 review)
#
# The banked pulsar exclusion (port-register.md:93 -- "9-110 sigma Hulse-Taylor /
# 100-1400x the double-pulsar bound") was computed for a Reading-A QUADRUPOLE
# (l = 2) radiating at O(c). Multipole-l radiated power carries (v/c_g)^(2l+1),
# so the exclusion of a pole-bearing completion is suppressed by (c/c_g)^(2l+1).
# The test therefore BOUNDS ONLY completions with c_g <~ O(c). At this lane's own
# forced value c_g = sqrt(2 xi_Machian) c the suppression is ~10^-111 and the
# exclusion evaporates: a SUPERLUMINAL pole-bearing completion is NOT excluded by
# pulsar timing.
# --------------------------------------------------------------------------
def leg6() -> dict:
    cg_over_c_forced = math.sqrt(2.0 * XI_MACHIAN)
    # the lane's own c_g = c central exclusion factor. ORDER-ONLY (a confirmed
    # Tier-2 MAJOR stands against its digits); carried as a declared INPUT here,
    # never re-derived, and used only to show where the ORDER lands.
    central_at_cg_eq_c_ORDER_ONLY = 8974.0
    banked_exclusion_range = [100.0, 1400.0]   # port-register.md:93, double pulsar
    supp = {}
    for ell in (1, 2, 3):
        s = cg_over_c_forced ** (-(2 * ell + 1))
        supp[f"l={ell}"] = {
            "exponent_2l_plus_1": 2 * ell + 1,
            "suppression_c_over_cg_pow": s,
            "rescaled_exclusion_ratio_ORDER_ONLY": central_at_cg_eq_c_ORDER_ONLY * s,
        }
    return {
        "validity_condition": "c_g <~ O(c)",
        "suppression_law": "(c/c_g)^(2l+1)",
        "radiating_multipole_of_the_banked_bound": 2,
        "banked_exclusion_range_x": banked_exclusion_range,
        "banked_exclusion_source": "manuscript/ave-kb/common/port-register.md:93",
        "cg_over_c_forced_by_node_scale_inertia": cg_over_c_forced,
        "cg_over_c_forced_provenance": "sqrt(2 * XI_MACHIAN) -- L0/L4 admission price",
        "per_multipole": supp,
        "central_at_cg_eq_c_ORDER_ONLY_INPUT": central_at_cg_eq_c_ORDER_ONLY,
        "verdict": (
            "The pole test bounds only c_g <~ O(c). At the lane's own forced "
            "c_g = 1.277e22 c the quadrupole (l=2) exclusion ratio falls to ~1e-107 "
            "-- i.e. ~107 orders BELOW the comparator instead of ~4 above. A "
            "SUPERLUMINAL pole-bearing completion is NOT excluded by pulsar timing. "
            "ORDER-ONLY at every step; no digit here is banked."
        ),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mutation-receipt", action="store_true",
                    help="perturb a load-bearing number; the number check must FAIL")
    args = ap.parse_args()

    results = {
        "lane": "bias-propagation-theorem",
        "prereg": "research/2026-08-10_bias-propagation_prereg-FROZEN.md",
        "prereg_freeze_commit": "d4bee683",
        "mutation_receipt_mode": args.mutation_receipt,
        "constants": {
            "C_0": C_0, "G": G, "HBAR": HBAR, "L_NODE": L_NODE,
            "M_E": M_E, "RHO_BULK": RHO_BULK, "XI_MACHIAN": XI_MACHIAN,
            "M_SUN": M_SUN,
        },
        "L0_constants_and_tautology": leg0(mutate=args.mutation_receipt),
        "L1_ax4_dialect_consistency": leg1(),
        "L2_clock_branches": leg2(),
        "L3_frequency_response_instrument": leg3(),
        "L4_lc_admission_price": leg4(),
        "L5_widened_clock_lemma": leg5(),
        "L6_pole_test_validity_scope": leg6(),
    }
    # TREE-DIRTYING HAZARD (2026-08-11 review): --mutation-receipt used to write
    # the CORRUPTED payload over the tracked JSON, leaving a dirty tree that a
    # later commit could capture. Mutated runs now go to a temp path and the
    # tracked artifact is never touched.
    out = OUT
    if args.mutation_receipt:
        out = Path(tempfile.gettempdir()) / f"{OUT.stem}_MUTATED.json"
    payload = json.dumps(results, indent=2, sort_keys=True)
    out.write_text(payload)
    results["self_sha256"] = hashlib.sha256(payload.encode()).hexdigest()
    out.write_text(json.dumps(results, indent=2, sort_keys=True))
    tag = "  [MUTATED -- temp path, tracked JSON untouched]" if args.mutation_receipt else ""
    print(f"wrote {out}  sha256={results['self_sha256'][:16]}...{tag}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

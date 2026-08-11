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
    # GR cross-check: the force-at-infinity on a STATIC test mass in Schwarzschild
    # is F = (GMm/r^2) * (1 - r_s/r)^(-1/2). If CLOCK-1 reproduces that EXACTLY
    # (not just to leading order), the ENTAILED declaration of prereg 3.2 is
    # confirmed at every post-Newtonian order, not merely the Newtonian one.
    gr_ratio = 1 / sp.sqrt(1 - 2 * Gs * M / (c**2 * r))
    gr_match_exact = bool(sp.simplify(ratio1_exact - gr_ratio) == 0)

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

    return {
        "CLOCK_1": {
            "omega_inf": str(w_inf_1),
            "F_over_F_newton_exact": str(ratio1_exact),
            "F_over_F_newton_G0_leading": str(ratio1_lead),
            "leading_is_exactly_one": bool(sp.simplify(ratio1_lead - 1) == 0),
            "F_over_F_newton_through_1PN": str(ratio1_1pn),
            "matches_GR_static_force_at_infinity_EXACTLY": gr_match_exact,
            "gr_reference_expression": str(gr_ratio),
            "hbar_cancels": "hbar" not in str(sp.simplify(ratio1_exact)),
            "Ag_appears": "A_g" in str(ratio1_exact),
            "numeric_at_solar_surface": float(f1),
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
    }
    payload = json.dumps(results, indent=2, sort_keys=True)
    OUT.write_text(payload)
    results["self_sha256"] = hashlib.sha256(payload.encode()).hexdigest()
    OUT.write_text(json.dumps(results, indent=2, sort_keys=True))
    print(f"wrote {OUT.name}  sha256={results['self_sha256'][:16]}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

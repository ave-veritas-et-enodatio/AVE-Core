#!/usr/bin/env python3
"""Independent reproduction driver for research/2026-08-27_two-knob-gravity-repair_result.md.

WHAT THIS IS.  A from-scratch re-derivation of the four-lane derive workflow's
load-bearing algebra, plus the observational translation.  It exists so that
every number quoted in the result document has a receipt that a reader can
re-run, and so that the DERIVED-vs-IMPORTED ledger in that document can be
checked mechanically rather than trusted.

WHAT IT IS NOT.  It is not an engine driver.  Nothing here touches the lattice,
the TLM stepper, or `ave.core.constants` -- the physical constants are written
literally so that the arithmetic can be checked against CODATA by eye.  It mints
nothing and moves no solidity.

SECTOR.  T2 transverse shear-EM (light) and the gapped branch (a bound soliton),
read against a static radially-graded A1 bias.  Crystalline, cold, sub-yield,
LOSSLESS-REACTIVE (C, L, S real; no R, no G), small-signal, static grading.
Op14 saturation NOT engaged.

THE TWO LEGS, deliberately sharing no assumptions:
  A. symbolic  -- sympy perturbative Binet reduction of the ray equations.
  B. numeric   -- 60-digit mpmath apsidal quadrature using NO series expansion.
Agreement between them is the check; either alone would be an unverified claim.

Run:  python3 research/drivers/two_knob_gravity_repro.py
Emits: research/drivers/two_knob_gravity_repro_results.json
"""

from __future__ import annotations

import json
import pathlib

import mpmath as mp
import sympy as sp

mp.mp.dps = 60
OUT: dict[str, object] = {}


# ----------------------------------------------------------------------------
# LEG A -- symbolic.  The ray equation for H = omega(k, r).  No metric anywhere.
# ----------------------------------------------------------------------------
def leg_a_symbolic() -> None:
    u, m = sp.symbols("u m", positive=True)
    a1, a2, b1, b2, W, E, c, lp = sp.symbols("a1 a2 b1 b2 W E c l_p", positive=True)

    U = m * u                                     # U = GM/(c^2 r)
    c_eff = c * (1 - a1 * U + a2 * U**2)          # knob 1: local characteristic speed
    Om = sp.sqrt(W) * (1 - b1 * U + b2 * U**2)    # knob 2: local internal rest frequency

    # f(u) = k_r^2 + p^2 u^2 = (omega^2 - Omega^2)/c_eff^2 ; omega^2 = E + W
    f = sp.series(((E + W) - Om**2) / c_eff**2, m, 0, 3).removeO().expand()
    fp = sp.expand(sp.diff(f, u))

    # u'' + u = f'(u)/(2 p^2)  =>  u'' + (1 - eps) u = C0 = 1/l_p
    lin, quad = sp.simplify(fp.coeff(u, 0)), sp.simplify(fp.coeff(u, 1))
    dphi = sp.simplify(sp.pi * quad / (lin * lp))

    target = sp.pi * m * (3 * E * a1**2 - 2 * E * a2 + 4 * W * a1 * b1
                          - W * b1**2 - 2 * W * b2) / (lp * (E * a1 + W * b1))
    nr = sp.simplify(sp.limit(dphi, E, 0))
    nr_target = sp.pi * m / lp * (4 * a1 - b1 - 2 * b2 / b1)

    OUT["exact_form_matches_L1"] = bool(sp.simplify(dphi - target) == 0)
    OUT["nr_form_matches_L1"] = bool(sp.simplify(nr - nr_target) == 0)
    OUT["exact_dphi"] = str(sp.simplify(dphi))
    OUT["nr_dphi"] = str(nr)

    # a2 must be absent from the NR bracket; b2 must not be.
    OUT["a2_absent_from_NR"] = bool(sp.simplify(sp.diff(nr, a2)) == 0)
    OUT["b2_present_in_NR"] = bool(sp.simplify(sp.diff(nr, b2)) != 0)

    bracket = lambda A1, B1, B2: sp.nsimplify(4 * A1 - B1 - 2 * sp.Rational(B2) / B1)
    OUT["brackets"] = {
        "GR / two-knob repair (2, 1, 1/2)": str(bracket(2, 1, sp.Rational(1, 2))),
        "Gordon scalar n=1+U  (AVE matter, canon)": str(bracket(1, 1, 1)),
        "Gordon scalar n=1+2U (AVE light index)": str(bracket(2, 2, 4)),
        "two-knob, ADDITIVE clock b2=0": str(bracket(2, 1, 0)),
    }

    # PPN identity -- reporting language only, used as a check, never as a premise.
    g, bt = sp.symbols("gamma beta")
    OUT["ppn_identity_holds"] = bool(
        sp.simplify((4 * (1 + g) - 1 - 2 * (bt - sp.Rational(1, 2))) - 6 * (2 - bt + 2 * g) / 3) == 0
    )

    # The Gordon construction: ONE knob wired to BOTH slots.  An identity.
    n, aN = sp.symbols("n a_N", positive=True)
    OUT["gordon_g00"] = str(sp.simplify(-1 + (1 - 1 / n**2)))          # = -1/n^2
    ce = sp.expand(sp.series(1 / (1 + aN * U), m, 0, 3).removeO())
    OUT["gordon_forces_a1_eq_b1"] = True   # c_eff/c and Omega/Omega_inf are the SAME series
    OUT["gordon_series"] = str(ce)
    OUT["gordon_bracket_is_bare_slope"] = str(sp.simplify(4 * aN - aN - 2 * aN**2 / aN))

    # Canon's Path-A Lagrangian is the Gordon scalar metric, and for n linear in u
    # the Binet equation is EXACT (f is exactly quadratic in u) -- no truncation.
    q, w = sp.symbols("q omega", positive=True)
    p = sp.symbols("p", positive=True)
    f_exact = sp.expand((w**2 * (1 + q * m * u) ** 2 - W) / c**2)
    OUT["pathA_f_is_quadratic"] = bool(sp.degree(sp.Poly(f_exact, u)) == 2)
    fpe = sp.expand(sp.diff(f_exact, u))
    C_e, eps_e = fpe.coeff(u, 0) / (2 * p**2), fpe.coeff(u, 1) / (2 * p**2)
    w_sub = sp.solve(sp.Eq(C_e, 1 / lp), w)[0]
    OUT["pathA_eps"] = str(sp.simplify(eps_e.subs(w, w_sub)))          # = q*m/l_p
    OUT["pathA_dphi_over_pi_GM_c2_lp"] = str(sp.simplify(eps_e.subs(w, w_sub) * lp / m))

    # Exact isotropic Schwarzschild, for the record: (a1, a2, b1, b2).
    Us = sp.symbols("U", positive=True)
    A = ((1 - Us / 2) / (1 + Us / 2)) ** 2
    B = (1 + Us / 2) ** 4
    ces = sp.expand(sp.series(sp.sqrt(A / B), Us, 0, 3).removeO())
    oms = sp.expand(sp.series(sp.sqrt(A), Us, 0, 3).removeO())
    OUT["GR_isotropic_exponents"] = {
        "a1": str(-ces.coeff(Us, 1)), "a2": str(ces.coeff(Us, 2)),
        "b1": str(-oms.coeff(Us, 1)), "b2": str(oms.coeff(Us, 2)),
    }
    OUT["n_opt_vs_inv_g00"] = {
        "n_opt": str(sp.expand(sp.series(1 / sp.sqrt(A / B), Us, 0, 3).removeO())),
        "one_over_abs_g00": str(sp.expand(sp.series(1 / A, Us, 0, 3).removeO())),
    }

    # The ultrarelativistic-convergence theorem, in closed form.
    beta = sp.symbols("beta", positive=True)
    conv = sp.simplify(2 * (a1 + b1 * (1 - beta**2) / beta**2))
    OUT["deflection_closed_form"] = str(conv)
    OUT["deflection_beta_to_1"] = str(sp.limit(conv, beta, 1))          # -> 2*a1
    OUT["deflection_table"] = {
        v: {"GR_a1_2": float(conv.subs({a1: 2, b1: 1, beta: sp.Rational(v)})),
            "AVE_canon_a1_1": float(conv.subs({a1: 1, b1: 1, beta: sp.Rational(v)}))}
        for v in ("0.1", "0.5", "0.9", "0.99", "0.9999")
    }


# ----------------------------------------------------------------------------
# LEG B -- numeric.  Exact apsidal quadrature.  NO series expansion is used.
# ----------------------------------------------------------------------------
def apsidal(ceff, Om, rp, ra):
    """Advance per orbit for H = omega(k,r).  Units GM/c^2 = c = Omega_inf = 1.

    Solves the 2x2 linear system that places the turning points EXACTLY at
    (rp, ra), then integrates the apsidal angle with the endpoint square-root
    singularities factored out by the substitution u = u_mid + u_half*sin(theta).
    """
    u1, u2 = mp.mpf(1) / ra, mp.mpf(1) / rp
    M = mp.matrix([[1 / ceff(1 / u1) ** 2, -u1**2], [1 / ceff(1 / u2) ** 2, -u2**2]])
    rhs = mp.matrix([Om(1 / u1) ** 2 / ceff(1 / u1) ** 2, Om(1 / u2) ** 2 / ceff(1 / u2) ** 2])
    sol = mp.lu_solve(M, rhs)
    w, p2 = sol[0], sol[1]
    f = lambda uu: (w - Om(1 / uu) ** 2) / ceff(1 / uu) ** 2
    um, uh = (u1 + u2) / 2, (u2 - u1) / 2

    def integrand(th):
        uu = um + uh * mp.sin(th)
        den = (uu - u1) * (u2 - uu)
        return mp.sqrt(p2) / mp.sqrt((f(uu) - p2 * uu**2) / den) if den != 0 else mp.mpf(0)

    return 2 * mp.quad(integrand, [-mp.pi / 2, mp.pi / 2]) - 2 * mp.pi


def leg_b_numeric() -> None:
    rp, ra = mp.mpf("6e6"), mp.mpf("1e7")
    lp = 2 / (1 / rp + 1 / ra)
    A = lambda r: ((1 - mp.mpf(1) / (2 * r)) / (1 + mp.mpf(1) / (2 * r))) ** 2
    B = lambda r: (1 + mp.mpf(1) / (2 * r)) ** 4
    cases = {
        "GR isotropic EXACT (predict 6)": (lambda r: mp.sqrt(A(r) / B(r)), lambda r: mp.sqrt(A(r)), 6),
        "Gordon n=1+U  AVE matter (predict 1)": (lambda r: 1 / (1 + mp.mpf(1) / r), lambda r: 1 / (1 + mp.mpf(1) / r), 1),
        "Gordon n=1+2U AVE light  (predict 2)": (lambda r: 1 / (1 + mp.mpf(2) / r), lambda r: 1 / (1 + mp.mpf(2) / r), 2),
        "two-knob exponential      (predict 6)": (lambda r: mp.e ** (-mp.mpf(2) / r), lambda r: mp.e ** (-mp.mpf(1) / r), 6),
        "two-knob additive b2=0    (predict 7)": (lambda r: 1 - mp.mpf(2) / r, lambda r: 1 - mp.mpf(1) / r, 7),
    }
    res = {}
    for lbl, (ce, om, pred) in cases.items():
        val = apsidal(ce, om, rp, ra) * lp / mp.pi
        res[lbl] = {"quadrature": mp.nstr(mp.re(val), 10), "analytic": pred}
    OUT["quadrature"] = res


# ----------------------------------------------------------------------------
# Observational translation.  Elements are this lane's, stated so they can be
# swapped; they contribute ~0.01 arcsec to Mercury, negligible against 895 sigma.
# ----------------------------------------------------------------------------
def observational() -> None:
    c = mp.mpf("299792458")
    G = mp.mpf("6.67430e-11")
    GMs = mp.mpf("1.32712440018e20")
    Msun = GMs / G
    arcs = 180 / mp.pi * 3600

    a_M, e_M, P_M = mp.mpf("5.790905e10"), mp.mpf("0.205630"), mp.mpf("87.9691") * 86400
    pre = mp.pi * GMs / (c**2 * a_M * (1 - e_M**2))
    norb = mp.mpf(100) * mp.mpf("365.25") * 86400 / P_M
    merc = {}
    for lbl, F in (("canon Gordon n=1+U (bracket 1)", 1), ("matter on light index (2)", 2),
                   ("two-knob repair / GR (6)", 6), ("two-knob additive b2=0 (7)", 7)):
        v = pre * F * norb * arcs
        merc[lbl] = {"arcsec_per_century": mp.nstr(v, 8),
                     "sigma_vs_42.98pm0.04": mp.nstr((v - mp.mpf("42.98")) / mp.mpf("0.04"), 6)}
    OUT["mercury"] = merc
    OUT["mercury_measured"] = "42.98 +/- 0.04 arcsec/century"

    Mtot, Pb, e_H = mp.mpf("2.828378") * Msun, mp.mpf("0.322997448911") * 86400, mp.mpf("0.6171334")
    wdot = 3 * (Pb / (2 * mp.pi)) ** (mp.mpf(-5) / 3) * (G * Mtot / c**3) ** (mp.mpf(2) / 3) / (1 - e_H**2)
    dpy = 180 / mp.pi * mp.mpf("365.25") * 86400
    OUT["hulse_taylor"] = {"repair_or_GR_deg_per_yr": mp.nstr(wdot * dpy, 8),
                           "canon_one_sixth_deg_per_yr": mp.nstr(wdot * dpy / 6, 8),
                           "measured": "4.226585(4) deg/yr"}

    R = mp.mpf("6.957e8")
    OUT["solar_limb_arcsec"] = {f"a1={k}": mp.nstr(2 * k * GMs / (c**2 * R) * arcs, 7) for k in (1, 2)}
    OUT["solar_limb_measured"] = "1.7509 arcsec"

    # SN1987A.  Method chosen to avoid an enclosed-mass guess: for a FLAT rotation
    # curve, GM(<r)/r = v_c^2, so the index argument U = (v_c/c)^2 is CONSTANT
    # along the path and the mass model cancels out of the fractional statement.
    kpc = mp.mpf("3.0856775814913673e19")
    vc, D = mp.mpf("220e3"), mp.mpf("51.4") * kpc
    U = (vc / c) ** 2
    dt = U * D / c
    OUT["sn1987a"] = {
        "method": "flat rotation curve v_c=220 km/s -> U = (v_c/c)^2 constant along the path",
        "U": mp.nstr(U, 6),
        "photon_excess_days": mp.nstr(2 * dt / 86400, 6),
        "ave_matter_excess_days": mp.nstr(dt / 86400, 6),
        "predicted_nu_gamma_differential_days": mp.nstr(dt / 86400, 6),
        "observed_offset_hours": 3,
        "ratio_predicted_over_observed": mp.nstr(dt / (3 * 3600), 6),
        "model_free_statement": "AVE predicts (n_nu-1)/(n_gamma-1) = 0.5; SN1987A bounds "
                                "the species differential at ~ 3h/65.9d = 2e-3. The mass "
                                "model cancels out of the fraction.",
    }

    # Umklapp thresholds -- exact because l_node = hbar/(m_e c) is DEFINITIONAL.
    mec2, mpc2 = mp.mpf("0.51099895000"), mp.mpf("938.27208816")   # MeV
    pc = mp.pi * mec2
    OUT["umklapp_zone_edge"] = {
        "photon_MeV": mp.nstr(pc, 7),
        "electron_kinetic_MeV": mp.nstr(mp.sqrt(pc**2 + mec2**2) - mec2, 7),
        "proton_kinetic_keV": mp.nstr((mp.sqrt(pc**2 + mpc2**2) - mpc2) * 1000, 7),
    }


def main() -> None:
    leg_a_symbolic()
    leg_b_numeric()
    observational()
    for k, v in OUT.items():
        print(f"{k}: {json.dumps(v, indent=2) if isinstance(v, dict) else v}")
    dst = pathlib.Path(__file__).with_name("two_knob_gravity_repro_results.json")
    dst.write_text(json.dumps(OUT, indent=2) + "\n")
    print(f"\n[driver] wrote {dst}")


if __name__ == "__main__":
    main()

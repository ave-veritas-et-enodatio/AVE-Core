#!/usr/bin/env python3
"""LC-1 ONE-SPEED (multi-messenger) — derivation driver.

Lane   : research/lc1-one-speed (Lorentz-compliance arc, LC-1 leading kill test)
Prereg : research/2026-08-06_lc1-one-speed_prereg-FROZEN.md, frozen ALONE at 992bb5a6
Result : research/2026-08-06_lc1-one-speed_result.md

DERIVATION-ONLY. No engine run, no eigensolve on a lattice, no simulation campaign.
Every substrate constant is imported from `ave.core.constants` (G-CONST); nothing is
hard-coded. The three non-substrate inputs (solar mass parameter, parsec, Julian year)
are UNIT DEFINITIONS, declared explicitly and emitted into the JSON.

Legs, in the frozen order of prereg §3:
  A  Christoffel eigen-spectrum of the isotropic medium              (G-SPEC, G-NEG)
  B  Poisson-ratio cross-check against the corpus NU_VAC symbol      (G-NU)
  C  micropolar 2x2 k.p transverse cancellation, re-derived here     (G-KP)
  D  combine-member insensitivity at S = 1                           (G-MEMBER)
  E  arrival kinematics of a superluminal channel from a chirp       (G-BAND/CHIRP/DIST)
  F  Cosserat gap + Yukawa-reach margins                             (G-GAPMARGIN)

Regex engine for any doc scan performed by the companion checker: Python `re`.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from ave.core import constants as K  # noqa: E402  (path set above)

OUT = Path(__file__).with_name("lc1_one_speed_results.json")

# --- UNIT DEFINITIONS (declared; not substrate values) -----------------------
GM_SUN = 1.32712440018e20  # IAU nominal solar mass parameter, m^3 s^-2
PARSEC = 3.0856775814913673e16  # m, exact from the au + arcsec definitions
MPC = 1.0e6 * PARSEC
JULIAN_YEAR = 365.25 * 86400.0  # s

# --- COMPARATOR INPUTS (external observation import; see prereg §2) ----------
COMPARATOR = {
    "paper_timing": "LIGO/Virgo/Fermi-GBM/INTEGRAL, ApJL 848:L13 (2017), arXiv:1710.05834",
    "paper_source": "LIGO/Virgo, Phys. Rev. Lett. 119 161101 (2017), arXiv:1710.05832",
    "delta_v_over_c_lower": -3.0e-15,
    "delta_v_over_c_upper": +7.0e-16,
    "observed_delay_s": 1.74,
    "total_mass_msun": 2.74,
    "luminosity_distance_mpc": 40.0,
    "luminosity_distance_mpc_lo": 40.0 - 14.0,
    "luminosity_distance_mpc_hi": 40.0 + 8.0,
    "f_low_hz_nominal": 20.0,
    "f_low_hz_bracket": [10.0, 30.0],
}


# =============================================================================
# LEG A — the Christoffel eigen-spectrum of the isotropic medium
# =============================================================================
def christoffel_symbolic():
    """Exact eigen-spectrum of Gamma_ik = C_ijkl n_j n_l for an isotropic medium.

    C_ijkl = lambda d_ij d_kl + G (d_ik d_jl + d_il d_jk),  lambda = K_bulk - 2G/3.
    Returns the symbolic eigenvalues with multiplicities for a general unit n.
    """
    Kb, G = sp.symbols("K_bulk G", positive=True)
    n1, n2, n3 = sp.symbols("n1 n2 n3", real=True)
    lam = Kb - sp.Rational(2, 3) * G
    n = sp.Matrix([n1, n2, n3])

    Gam = sp.zeros(3, 3)
    for i in range(3):
        for k in range(3):
            s = 0
            for j in range(3):
                for ll in range(3):
                    c = (
                        lam * (1 if i == j else 0) * (1 if k == ll else 0)
                        + G * (1 if i == k else 0) * (1 if j == ll else 0)
                        + G * (1 if i == ll else 0) * (1 if j == k else 0)
                    )
                    s += c * n[j] * n[ll]
            Gam[i, k] = sp.simplify(s)

    # constrain to a unit vector
    Gam_u = sp.simplify(Gam.subs(n3**2, 1 - n1**2 - n2**2))
    ev = Gam_u.eigenvals()
    return Kb, G, {sp.simplify(sp.expand(k)): v for k, v in ev.items()}



def christoffel_cubic(C, direction):
    """Eigenvalues of Gamma_ik = C_ijkl n_j n_l for a CUBIC medium, given (C11,C12,C44).

    Cubic (m-3m) Voigt tensor.  Used by (a) the G-SPEC fireability self-test and (b) the
    REVIEW-FOLLOW-ON direction-resolved sweep on the ratified srs carrier's Cauchy tensor.
    Returns eigenvalues sorted ascending (= rho * v^2).
    """
    C11, C12, C44 = C
    n = np.asarray(direction, dtype=float)
    n = n / np.linalg.norm(n)
    G = np.empty((3, 3))
    for i in range(3):
        for k in range(3):
            if i == k:
                j, l = [x for x in range(3) if x != i]
                G[i, k] = C11 * n[i] ** 2 + C44 * (n[j] ** 2 + n[l] ** 2)
            else:
                G[i, k] = (C12 + C44) * n[i] * n[k]
    return np.sort(np.linalg.eigvalsh(G))

def christoffel_numeric(K_over_G, directions):
    """Numeric eigenvalues of Gamma/G for a list of directions, at a given K/G."""
    lam = K_over_G - 2.0 / 3.0
    out = {}
    for name, d in directions.items():
        nv = np.asarray(d, dtype=float)
        nv = nv / np.linalg.norm(nv)
        Gam = np.zeros((3, 3))
        for i in range(3):
            for k in range(3):
                s = 0.0
                for j in range(3):
                    for ll in range(3):
                        c = (
                            lam * (i == j) * (k == ll)
                            + 1.0 * (i == k) * (j == ll)
                            + 1.0 * (i == ll) * (j == k)
                        )
                        s += c * nv[j] * nv[ll]
                Gam[i, k] = s
        w = np.sort(np.linalg.eigvalsh(Gam))
        out[name] = [float(x) for x in w]
    return out


def leg_A():
    directions = {
        "[100]": (1, 0, 0),
        "[110]": (1, 1, 0),
        "[111]": (1, 1, 1),
        "[210]": (2, 1, 0),
        "[321]": (3, 2, 1),
    }
    Kb, G, ev = christoffel_symbolic()
    sym = {sp.srepr(k): int(v) for k, v in ev.items()}
    sym_pretty = {str(sp.simplify(k)): int(v) for k, v in ev.items()}

    num = christoffel_numeric(2.0, directions)
    # distinct-eigenvalue count per direction, at K = 2G
    distinct = {
        k: sorted({round(x, 12) for x in v}) for k, v in num.items()
    }
    n_distinct = {k: len(v) for k, v in distinct.items()}

    vL2_over_vT2 = float(sp.nsimplify(sp.Rational(10, 3)))
    ratio = float(np.sqrt(10.0 / 3.0))

    # G-NEG negative control: K -> 0 must give vL/vT = sqrt(4/3), NOT sqrt(2)
    num_K0 = christoffel_numeric(0.0, {"[100]": (1, 0, 0)})["[100]"]
    ratio_K0 = float(np.sqrt(max(num_K0) / min(num_K0)))

    # is sqrt(2)c an eigenvalue at K=2G?  (i.e. is K/rho in the spectrum)
    spec_100 = distinct["[100]"]
    sqrt2_present = any(abs(x - 2.0) < 1e-12 for x in spec_100)

    # the K-condition for vL > vT
    Kb_s, G_s = sp.symbols("K_bulk G", positive=True)
    cond = sp.simplify((Kb_s + sp.Rational(4, 3) * G_s) - G_s)  # > 0  <=>  vL > vT
    ratio_general = sp.simplify((Kb_s + sp.Rational(4, 3) * G_s) / G_s)
    floor_at_K0 = float(np.sqrt(4.0 / 3.0))
    # K required to bring the longitudinal branch DOWN to c
    K_for_vL_eq_c = sp.solve(sp.Eq(Kb_s + sp.Rational(4, 3) * G_s, G_s), Kb_s, dict=False)
    K_for_vL_eq_c = [sp.simplify(x) for x in sp.solve(
        sp.Eq(sp.Symbol("Kb") + sp.Rational(4, 3) * G_s, G_s), sp.Symbol("Kb")
    )]

    # G-SPEC fireability self-test (REVIEW-REPAIRED R3a).  The previous version fed a
    # diagonal matrix straight to eigvalsh -- it exercised numpy, not the gate.  This
    # builds a genuinely anisotropic CUBIC stiffness tensor (Zener A != 1) and pushes
    # it THROUGH the same christoffel_cubic path the real spectrum uses, probing [110]
    # where cubic anisotropy splits the degenerate transverse pair.
    aniso_C = (1.0, 0.3, 0.5)  # (C11, C12, C44); Zener A = 2*C44/(C11-C12) = 1.428...
    aniso_eigs = christoffel_cubic(aniso_C, (1, 1, 0))
    aniso_distinct = len({round(float(x), 12) for x in aniso_eigs})
    aniso_zener = 2.0 * aniso_C[2] / (aniso_C[0] - aniso_C[1])
    # control: the SAME path on an ISOTROPIC cubic tensor (A = 1) must give exactly 2
    iso_C = (1.0, 0.3, 0.35)  # C44 = (C11-C12)/2 -> A = 1 exactly
    iso_distinct = len({round(float(x), 12) for x in christoffel_cubic(iso_C, (1, 1, 0))})

    return {
        "symbolic_eigenvalues_pretty": sym_pretty,
        "symbolic_eigenvalues_srepr": sym,
        "n_distinct_eigenvalues_at_K2G": n_distinct,
        "spectrum_over_G_at_K2G": distinct,
        "vL2_over_vT2_at_K2G": vL2_over_vT2,
        "vL_over_vT_at_K2G": ratio,
        "vL_over_c": ratio,
        "sqrt2_is_an_eigenvalue_at_K2G": bool(sqrt2_present),
        "vL_over_vT_at_K0_negative_control": ratio_K0,
        "vL_gt_vT_condition_expr": str(cond),
        "vL2_over_vT2_general_expr": str(ratio_general),
        "vL_over_vT_floor_at_K_zero": floor_at_K0,
        "K_required_for_vL_equals_c": [str(x) for x in K_for_vL_eq_c],
        "superluminal_forced_by_G_alone": bool(floor_at_K0 > 1.0),
        "gspec_fireability_selftest_distinct_count": aniso_distinct,
        "gspec_fireability_selftest_zener": aniso_zener,
        "gspec_fireability_isotropic_control_distinct_count": iso_distinct,
        "gspec_fireability_is_through_christoffel_path": True,
    }


# =============================================================================
# LEG B — Poisson-ratio cross-check
# =============================================================================
def leg_B():
    Kb, G = sp.symbols("K_bulk G", positive=True)
    nu = (3 * Kb - 2 * G) / (2 * (3 * Kb + G))
    nu_at_2G = sp.simplify(nu.subs(Kb, 2 * G))
    nu_val = float(nu_at_2G)
    return {
        "nu_symbolic_at_K2G": str(nu_at_2G),
        "nu_value": nu_val,
        "NU_VAC_from_constants": float(K.NU_VAC),
        "abs_diff": abs(nu_val - float(K.NU_VAC)),
    }


# =============================================================================
# LEG C — the micropolar transverse cancellation, re-derived from a functional
# =============================================================================
def leg_C():
    """Independent re-derivation of clm-2bkp7v's photon-branch cancellation.

    Energy density for a transverse plane wave  u = U cos(kz) x_hat,
    omega = W sin(kz) y_hat, on the isotropic micropolar functional

        W_tot = W_cauchy + 2 G_c (Omega - omega)^2 ,   Omega = (1/2) curl u .

    The 2 G_c normalization is NOT chosen for convenience: it is FIXED by requiring
    the k=0 optical branch to reproduce the corpus mass gap m^2 = 4 G_c / I_omega
    (cosserat-mass-gap.md, clm-jz0xaw).  The cancellation is then a prediction of
    that same normalization, not an input.
    """
    G, Gc, rho, Iw, k, w2 = sp.symbols("G G_c rho I_omega k omega2", positive=True)
    U, W = sp.symbols("U W", real=True)

    # z-averaged potential energy density (see result doc S3 for the algebra)
    V = G * k**2 * U**2 / 4 + Gc * (k * U / 2 + W) ** 2
    # z-averaged kinetic coefficient matrix (T = 1/2 q_dot^T M q_dot)
    M = sp.diag(rho / 2, Iw / 2)
    Kmat = sp.hessian(V, (U, W))

    # generalized eigenproblem  K q = omega^2 M q
    char = sp.simplify(sp.det(Kmat - w2 * M))
    roots = sp.solve(sp.Eq(char, 0), w2)

    # gap: k -> 0
    gap_roots = sorted({sp.simplify(r.subs(k, 0)) for r in roots}, key=str)
    # acoustic branch: the root that vanishes as k -> 0
    acoustic = [r for r in roots if sp.simplify(r.subs(k, 0)) == 0]
    optical = [r for r in roots if sp.simplify(r.subs(k, 0)) != 0]
    assert len(acoustic) == 1 and len(optical) == 1

    ac_series = sp.simplify(sp.series(acoustic[0], k, 0, 4).removeO())
    v2_coeff = sp.simplify(sp.expand(ac_series).coeff(k, 2))
    residual = sp.simplify(v2_coeff - G / rho)

    gap_expr = sp.simplify(optical[0].subs(k, 0))
    gap_residual = sp.simplify(gap_expr - 4 * Gc / Iw)

    # --- longitudinal contrast: pure longitudinal has curl u = 0, so Omega = 0 -----
    # u = U cos(kz) z_hat  =>  eps_zz = -kU sin(kz), curl u = 0.
    lam = sp.Symbol("lambda_lame", real=True)
    V_long = (lam / 2 + G) * k**2 * U**2 / 2 + Gc * W**2  # z-averaged
    K_long = sp.hessian(V_long, (U, W))
    long_offdiag = sp.simplify(K_long[0, 1])
    long_v2 = sp.simplify(K_long[0, 0] / (rho / 2) / k**2)

    # --- REVIEW-REPAIRED R3b: the G_c -> 0 leg of G-NEG, actually computed ---------
    # Extend the same functional with the curvature term W_kappa = gamma |grad omega|^2
    # (no-1/2 convention, clm-kmliqx).  Two carrier branches:
    #   omega PARALLEL k : decoupled from u (Omega_z = 0) -> its own 1-DOF problem
    #   omega PERP     k : the optical root of the SAME 2x2 as above, plus curvature
    gamma = sp.Symbol("gamma", positive=True)

    # omega || k  (twist branch): V = gamma k^2 W^2 / 2 + G_c W^2 ; M = I_omega/2
    V_par = gamma * k**2 * W**2 / 2 + Gc * W**2
    v2_par = sp.simplify(sp.hessian(V_par, (W,))[0, 0] / (Iw / 2) / k**2 - 4 * Gc / (Iw * k**2))
    v2_par = sp.simplify(sp.expand(
        sp.hessian(V_par, (W,))[0, 0] / (Iw / 2)).coeff(k, 2))

    # omega perp k : same 2x2 with the curvature term added to K_WW
    # Hessian of the curvature term gamma*k^2*W^2/2 is gamma*k^2 -- the SAME
    # normalization used for the omega||k branch above.  (An earlier draft wrote
    # 2*gamma*k^2 here and the G_c->0 control caught it: the splitting came out
    # G_c/rho + 2*gamma/I_omega instead of G_c/rho, i.e. it did not vanish at
    # G_c = 0.  Recorded because it is exactly what a negative control is for.)
    K_perp = Kmat + sp.Matrix([[0, 0], [0, gamma * k**2]])
    char_perp = sp.simplify(sp.det(K_perp - w2 * M))
    roots_perp = sp.solve(sp.Eq(char_perp, 0), w2)
    ac_p = [r for r in roots_perp if sp.simplify(r.subs(k, 0)) == 0]
    op_p = [r for r in roots_perp if sp.simplify(r.subs(k, 0)) != 0]
    v2_perp = sp.simplify(sp.expand(
        sp.series(op_p[0], k, 0, 4).removeO()).coeff(k, 2)) if op_p else None
    v2_ac_p = sp.simplify(sp.expand(
        sp.series(ac_p[0], k, 0, 4).removeO()).coeff(k, 2)) if ac_p else None

    splitting = sp.simplify(v2_perp - v2_par)
    splitting_residual = sp.simplify(splitting - Gc / rho)
    splitting_at_Gc0 = sp.simplify(splitting.subs(Gc, 0))
    gap_at_Gc0 = sp.simplify(gap_expr.subs(Gc, 0))
    acoustic_at_Gc0 = sp.simplify(v2_coeff.subs(Gc, 0))

    return {
        "acoustic_branch_v2_coefficient": str(v2_coeff),
        "acoustic_branch_v2_minus_G_over_rho": str(residual),
        "cancellation_exact": bool(residual == 0),
        "optical_branch_gap_expr": str(gap_expr),
        "gap_minus_4Gc_over_Iomega": str(gap_residual),
        "gap_matches_corpus_m2": bool(gap_residual == 0),
        "gap_roots_at_k0": [str(g) for g in gap_roots],
        "longitudinal_offdiagonal_coupling": str(long_offdiag),
        "longitudinal_is_micropolar_decoupled": bool(long_offdiag == 0),
        "longitudinal_v2_expr": str(long_v2),
        # --- G-NEG, G_c -> 0 leg (REVIEW-REPAIRED R3b) -------------------------
        "carrier_v2_parallel": str(v2_par),
        "carrier_v2_perp": str(v2_perp),
        "carrier_splitting": str(splitting),
        "carrier_splitting_minus_Gc_over_rho": str(splitting_residual),
        "splitting_reproduces_clm2bkp7v": bool(splitting_residual == 0),
        "carrier_splitting_at_Gc_zero": str(splitting_at_Gc0),
        "splitting_vanishes_at_Gc_zero": bool(splitting_at_Gc0 == 0),
        "gap_at_Gc_zero": str(gap_at_Gc0),
        "gap_vanishes_at_Gc_zero": bool(gap_at_Gc0 == 0),
        "acoustic_v2_at_Gc_zero": str(acoustic_at_Gc0),
        "acoustic_unchanged_at_Gc_zero": bool(sp.simplify(acoustic_at_Gc0 - G / rho) == 0),
        "acoustic_v2_from_perp_operator": str(v2_ac_p),
    }


# =============================================================================
# LEG D — combine-member insensitivity at S = 1  (#905/#907 fence)
# =============================================================================
def leg_D():
    """At cold amplitude every saturation kernel is unity; both combine members
    multiply the same moduli by 1.  Evaluated rather than asserted."""
    S = 1.0
    per_grade = {"S_eps": S, "S_kappa": S}  # L-infinity across grades
    l2 = float(np.sqrt((S**2 + S**2) / 2.0))  # normalized L2 across grades
    G_eff_pg = float(K.G_VAC) * per_grade["S_eps"]
    G_eff_l2 = float(K.G_VAC) * l2
    vT_pg = float(np.sqrt(G_eff_pg / K.RHO_BULK))
    vT_l2 = float(np.sqrt(G_eff_l2 / K.RHO_BULK))
    vL_pg = float(np.sqrt(10.0 / 3.0 * G_eff_pg / K.RHO_BULK))
    vL_l2 = float(np.sqrt(10.0 / 3.0 * G_eff_l2 / K.RHO_BULK))
    return {
        "S_at_cold": S,
        "normalized_L2_kernel_at_S1": l2,
        "vT_per_grade_member": vT_pg,
        "vT_normalizedL2_member": vT_l2,
        "vT_member_absdiff": abs(vT_pg - vT_l2),
        "vL_per_grade_member": vL_pg,
        "vL_normalizedL2_member": vL_l2,
        "vL_member_absdiff": abs(vL_pg - vL_l2),
        "member_insensitive": bool(
            abs(vT_pg - vT_l2) == 0.0 and abs(vL_pg - vL_l2) == 0.0
        ),
    }


# =============================================================================
# LEG E — arrival kinematics of a superluminal channel from a chirping source
# =============================================================================
def chirp_mass_msun(total_msun, q=1.0):
    """Chirp mass from total mass and mass ratio q = m2/m1 (q=1 -> equal mass)."""
    m1 = total_msun / (1.0 + q)
    m2 = total_msun - m1
    return (m1 * m2) ** 0.6 / total_msun**0.2


def f_gw_at_tc(tc_s, mchirp_msun):
    """Leading-order inspiral: f_GW at time tc before coalescence."""
    tau = GM_SUN * mchirp_msun / float(K.C_0) ** 3  # geometric chirp time, s
    return (1.0 / np.pi) * (5.0 / (256.0 * tc_s)) ** 0.375 * tau ** (-0.625)


def arrival_row(v_over_c, D_mpc, mchirp_msun):
    D = D_mpc * MPC
    t_light = D / float(K.C_0)
    dt = t_light * (1.0 - 1.0 / v_over_c)
    f = f_gw_at_tc(dt, mchirp_msun) if dt > 0 else float("inf")
    return {
        "v_over_c": v_over_c,
        "D_mpc": D_mpc,
        "light_travel_time_s": t_light,
        "light_travel_time_myr": t_light / JULIAN_YEAR / 1e6,
        "one_minus_c_over_v": 1.0 - 1.0 / v_over_c,
        "retarded_offset_s": dt,
        "retarded_offset_myr": dt / JULIAN_YEAR / 1e6,
        "f_gw_at_arrival_hz": f,
    }


def leg_E():
    mc = chirp_mass_msun(COMPARATOR["total_mass_msun"])
    vL = float(np.sqrt(10.0 / 3.0))
    nominal = arrival_row(vL, COMPARATOR["luminosity_distance_mpc"], mc)

    f_nom = nominal["f_gw_at_arrival_hz"]
    f_low = COMPARATOR["f_low_hz_nominal"]

    # G-BAND: f_low bracket
    band = {
        f"f_low={fl}": {
            "f_low_hz": fl,
            "in_band": bool(f_nom >= fl),
            "decades_below_band": float(np.log10(fl / f_nom)),
        }
        for fl in COMPARATOR["f_low_hz_bracket"] + [f_low]
    }
    # G-CHIRP: mass-ratio bracket (component masses 1.17-1.60 Msun per the paper)
    chirp = {}
    for q in (1.0, 0.75, 0.6, 0.5):
        m = chirp_mass_msun(COMPARATOR["total_mass_msun"], q)
        r = arrival_row(vL, COMPARATOR["luminosity_distance_mpc"], m)
        chirp[f"q={q}"] = {
            "mchirp_msun": m,
            "f_gw_at_arrival_hz": r["f_gw_at_arrival_hz"],
            "in_band_at_20hz": bool(r["f_gw_at_arrival_hz"] >= f_low),
        }
    # G-DIST: distance bracket
    dist = {}
    for D in (
        COMPARATOR["luminosity_distance_mpc_lo"],
        COMPARATOR["luminosity_distance_mpc"],
        COMPARATOR["luminosity_distance_mpc_hi"],
    ):
        r = arrival_row(vL, D, mc)
        dist[f"D={D}Mpc"] = {
            "retarded_offset_myr": r["retarded_offset_myr"],
            "f_gw_at_arrival_hz": r["f_gw_at_arrival_hz"],
            "in_band_at_20hz": bool(r["f_gw_at_arrival_hz"] >= f_low),
        }
    # the other FLAG-A column, for completeness (even though leg A says it is not a wave)
    sqrt2_row = arrival_row(float(np.sqrt(2.0)), COMPARATOR["luminosity_distance_mpc"], mc)

    # fireability self-test: a fictitious ultra-low-f detector must flip the verdict
    fire = {"f_low_hz": 1.0e-6, "in_band": bool(f_nom >= 1.0e-6)}

    return {
        "chirp_mass_msun_equal_mass": mc,
        "nominal": nominal,
        "band_bracket": band,
        "band_shortfall_factor_at_20hz": float(f_low / f_nom),
        "decades_below_20hz": float(np.log10(f_low / f_nom)),
        "chirp_bracket": chirp,
        "distance_bracket": dist,
        "sqrt2_column_row": sqrt2_row,
        "gband_fireability_selftest": fire,
    }


# =============================================================================
# LEG F — Cosserat gap and Yukawa-reach margins
# =============================================================================
def leg_F():
    E_gap_J = 2.0 * float(K.M_E) * float(K.C_0) ** 2
    # e_charge imported from ave.core.constants (G-CONST: no hard-coded values)
    joule_per_MeV = 1.0e6 * float(K.e_charge)
    E_gap_MeV = E_gap_J / joule_per_MeV
    f_drive = 100.0  # Hz, mid-band for a BNS inspiral
    E_drive_J = float(K.HBAR) * 2.0 * np.pi * f_drive
    E_drive_eV = E_drive_J / float(K.e_charge)
    ratio = E_drive_J / E_gap_J

    D = COMPARATOR["luminosity_distance_mpc"] * MPC
    reaches = D / float(K.L_NODE)

    margins = {}
    for scale in (0.25, 0.5, 1.0, 2.0, 4.0):
        margins[f"gap x{scale}"] = {
            "gap_J": E_gap_J * scale,
            "drive_over_gap": ratio / scale,
            "still_dead": bool(ratio / scale < 1.0),
        }
    return {
        "gap_energy_J": E_gap_J,
        "gap_energy_MeV": E_gap_MeV,
        "drive_frequency_hz": f_drive,
        "drive_quantum_J": E_drive_J,
        "drive_quantum_eV": E_drive_eV,
        "drive_over_gap": ratio,
        "log10_drive_over_gap": float(np.log10(ratio)),
        "yukawa_reach_m": float(K.L_NODE),
        "path_length_m": D,
        "path_in_yukawa_reaches": reaches,
        "log10_path_in_reaches": float(np.log10(reaches)),
        "gap_margin_sweep": margins,
        "over_determined": bool(ratio < 1e-12 and reaches > 1e12),
    }



# =============================================================================
# LEG G — REVIEW-FOLLOW-ON CHARACTERIZATION (R4 iii), QUARANTINED from the frozen bins
# =============================================================================
# The frozen legs run on an ISOTROPIC constitutive ansatz.  Canon's ratified srs-z3
# carrier is materially ANISOTROPIC at exactly this order (constants.py:623-626: 2/7 is
# the isotropic Voigt-Reuss-Hill AVERAGE over an anisotropic tensor, Zener A ~ 1.23).
# This leg asks the direction-resolved question the isotropic ansatz cannot: does ANY
# propagation direction on the real cubic Cauchy tensor bring the fastest branch down to
# the transverse branches?
#
# POST-FREEZE.  Adjudicates NO frozen bin.  Reported as characterization only.
#
# The tensor is READ from the shipped, gated artifact of the merged #890 lane
# (srs_twist_coefficient_results.json, gate G2) -- not hard-coded.  That member carries
# Zener A ~ 1.41, MORE anisotropic than the srs-elastic-tensor table's A ~ 1.23 row at
# the same rho*, so it is the CONSERVATIVE member for this question (more anisotropy =
# more direction-dependence = more chance of a dip).  The two members are the #890
# lane's own KEEP-BOTH fork and both are named in the result doc.
SRS_JSON = Path(__file__).with_name("srs_twist_coefficient_results.json")


def _fibonacci_directions(n):
    i = np.arange(n) + 0.5
    phi = np.arccos(1.0 - 2.0 * i / n)
    theta = np.pi * (1.0 + 5.0**0.5) * i
    return np.stack(
        [np.sin(phi) * np.cos(theta), np.sin(phi) * np.sin(theta), np.cos(phi)], axis=1
    )


def leg_G():
    if not SRS_JSON.exists():
        return {"status": "SKIPPED — shipped srs tensor artifact not present"}
    srs = json.loads(SRS_JSON.read_text())
    g2 = next(g for g in srs["gates"] if g.get("gate") == "G2")
    C = (float(g2["C11"]), float(g2["C12"]), float(g2["C44"]))
    zener = 2.0 * C[2] / (C[0] - C[1])

    dirs = list(_fibonacci_directions(20000))
    for d in [(1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0), (3, 2, 1), (1, 1, 2)]:
        dirs.append(np.asarray(d, dtype=float))

    ratios_fast_slow, ratios_fast_mid, worst = [], [], None
    for nvec in dirs:
        e = christoffel_cubic(C, nvec)  # ascending: T_slow, T_fast, L
        r_slow = float(np.sqrt(e[2] / e[0]))
        r_mid = float(np.sqrt(e[2] / e[1]))
        ratios_fast_slow.append(r_slow)
        ratios_fast_mid.append(r_mid)
        if worst is None or r_mid < worst[0]:
            worst = (r_mid, nvec / np.linalg.norm(nvec), e)

    hs = {
        name: [float(x) for x in christoffel_cubic(C, d)]
        for name, d in [("[100]", (1, 0, 0)), ("[110]", (1, 1, 0)), ("[111]", (1, 1, 1))]
    }
    return {
        "status": "REVIEW-FOLLOW-ON CHARACTERIZATION — adjudicates no frozen bin",
        "source": "research/drivers/srs_twist_coefficient_results.json gate G2 (merged #890)",
        "C11_C12_C44": list(C),
        "zener_A_of_this_member": zener,
        "n_directions": len(dirs),
        "min_over_directions_vfast_over_vslow": float(min(ratios_fast_slow)),
        "min_over_directions_vfast_over_vmid": float(min(ratios_fast_mid)),
        "max_over_directions_vfast_over_vmid": float(max(ratios_fast_mid)),
        "worst_direction": [float(x) for x in worst[1]],
        "worst_direction_eigs": [float(x) for x in worst[2]],
        "fastest_branch_exceeds_both_transverse_everywhere": bool(
            min(ratios_fast_mid) > 1.0
        ),
        "high_symmetry_eigs": hs,
        "isotropic_ansatz_comparison_vL_over_vT": float(np.sqrt(10.0 / 3.0)),
    }

# =============================================================================
def main():
    res = {
        "lane": "LC-1 one-speed (multi-messenger)",
        "prereg": "research/2026-08-06_lc1-one-speed_prereg-FROZEN.md",
        "prereg_freeze_commit": "992bb5a60230e66f8dd9181d9b3942cdc2b89593",
        "unit_definitions": {
            "GM_SUN_m3_s2": GM_SUN,
            "PARSEC_m": PARSEC,
            "JULIAN_YEAR_s": JULIAN_YEAR,
        },
        "constants_from_ave_core": {
            "C_0": float(K.C_0),
            "HBAR": float(K.HBAR),
            "M_E": float(K.M_E),
            "L_NODE": float(K.L_NODE),
            "RHO_BULK": float(K.RHO_BULK),
            "G_VAC": float(K.G_VAC),
            "V_LONG": float(K.V_LONG),
            "NU_VAC": float(K.NU_VAC),
        },
        "comparator": COMPARATOR,
        "legA_christoffel": leg_A(),
        "legB_poisson": leg_B(),
        "legC_micropolar_kp": leg_C(),
        "legD_combine_member": leg_D(),
        "legE_arrival_kinematics": leg_E(),
        "legF_cosserat_margins": leg_F(),
        "legG_srs_anisotropy_characterization_POST_FREEZE": leg_G(),
    }
    # derived consistency: V_LONG / C_0 must be sqrt(2), and must NOT equal vL/c
    res["flagA_check"] = {
        "V_LONG_over_C0": float(K.V_LONG) / float(K.C_0),
        "christoffel_vL_over_c": res["legA_christoffel"]["vL_over_c"],
        "they_differ": bool(
            abs(float(K.V_LONG) / float(K.C_0) - res["legA_christoffel"]["vL_over_c"]) > 1e-9
        ),
    }
    blob = json.dumps(res, sort_keys=True, indent=2)
    res["digest"] = hashlib.sha256(blob.encode()).hexdigest()
    OUT.write_text(json.dumps(res, sort_keys=True, indent=2) + "\n")
    print(f"[lc1] wrote {OUT}")
    print(f"[lc1] digest {res['digest']}")
    return res


if __name__ == "__main__":
    main()

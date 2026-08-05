#!/usr/bin/env python3
"""The LATTICE-REGULATED optical return delay to the r_sat wall, both branches.

Resolves the frozen gates and bins of
``research/2026-08-04_echo-delay-regulated-sum_prereg-FROZEN.md`` (commit
``1da06a90``, COMMIT 1 of this lane, pushed ALONE before this file existed).

WHAT THIS COMPUTES
------------------
The round-trip optical delay from a declared exterior reference plane inward to
the innermost node the wave reaches, under both FORK-3(b) profile branches:

    v(r) = c_0 * S(A)^p ,   A(r) = r_sat/r ,  S = sqrt(1-A^2)
    p = 1/2  RHO-A  (rho = rho_bulk)          -> c_0 sqrt(S)
    p = 2    RHO-B  (rho_eff = rho_bulk/S^3)  -> c_0 S^2
    p = 3    SYNTHETIC, self-test only (prereg section 4.3, CFG-SYN)

PRIMARY PLANE (prereg section 2.2): PLANE-inf, the EXCESS over cold-lattice
flight, r_out -> infinity.  Plane-INVARIANT because the graded deviation is
O(1/r^2) with no 1/r term.

NUMERICAL DISCIPLINE
--------------------
Near the wall A -> 1 to within l_node/r_sat ~ 1e-17, so ANY float64 evaluation
of 1 - A^2 by direct subtraction returns exactly zero.  Every near-wall
quantity here is therefore computed from the cancellation-free form

    S^2 = x (2 r_sat + x) / (r_sat + x)^2 ,      x = r - r_sat

and every  S^{-p} - 1  from expm1(-p/2 * log(S^2))  so the far field does not
cancel either.  The closed forms run in mpmath at dps = 50.

substrate-first: every constant is imported read-only from ave.core.constants;
the band model is the ADJUDICATED arccos transmission-line map of
srs-band-structure.md section 2, NOT the graph-Laplacian map.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import time

import mpmath as mp
import numpy as np

from ave.core import constants as K

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT_JSON = os.path.join(REPO, "research", "drivers",
                        "echo_delay_regulated_sum_results.json")
V24_JSON = os.path.join(REPO, "research", "drivers",
                        "coldq_pole_v2p4_root_results.json")
PRED_DRIVER = os.path.join(REPO, "src", "scripts", "vol_3_macroscopic",
                           "bh_shear_echo_delay.py")

mp.mp.dps = 50

# ---------------------------------------------------------------------------
# FROZEN NUMERICS (prereg section 4.2) -- no value below is tuned after a result
# ---------------------------------------------------------------------------
P_A, P_B, P_SYN = mp.mpf(1) / 2, mp.mpf(2), mp.mpf(3)
THETAS = (mp.mpf(1), mp.mpf(1) / 2)
BETAS = (mp.mpf("5.4414"), mp.mpf("17.0111"))   # vector band-top bracket (J7)
N_SPLITS = (10**5, 10**6, 10**7)
N_SPLIT_PRIMARY = 10**6
MASS_GRID_MSUN = (1.0, 10.0, 62.0, 100.0)
M_REF_MSUN = 62.0
ELL = 2
A_PEAK_BRACKET = (mp.mpf("0.05"), mp.mpf("0.999"))
QUAD_TOL_DPS = 30

# frozen gate tolerances (prereg section 4.5 / section 5)
TOL_NC = mp.mpf("1e-10")
TOL_JA = mp.mpf("1e-20")
TOL_CF = mp.mpf("1e-25")
TOL_SUM = mp.mpf("1e-12")
TOL_U = mp.mpf("1e-30")
TOL_DISP = mp.mpf("1e-15")
TOL_DECADE = mp.mpf("1e-6")
TOL_DISC = mp.mpf("0.01")
BIN_CUTOFF_THRESHOLD = mp.mpf("0.10")

# canonical constants, imported read-only (ave-canonical-source)
C0 = mp.mpf(repr(K.C_0))
G_NEWTON = mp.mpf(repr(K.G))
M_SUN = mp.mpf(repr(K.M_SUN))
L_NODE = mp.mpf(repr(K.L_NODE))
OMEGA_C = mp.mpf(repr(K.OMEGA_C))
HBAR = mp.mpf(repr(K.HBAR))
M_E = mp.mpf(repr(K.M_E))
X_SAT = mp.mpf(7)          # r_sat = 7 GM/c^2  (J1)


# ---------------------------------------------------------------------------
# geometry
# ---------------------------------------------------------------------------
def r_sat_of(M_msun) -> mp.mpf:
    """r_sat = 7 G M / c^2 (J1, J2)."""
    return X_SAT * G_NEWTON * (mp.mpf(repr(M_msun)) * M_SUN) / C0**2


def m_g_time(M_msun) -> mp.mpf:
    """The geometric mass in TIME units, G M / c^3."""
    return G_NEWTON * (mp.mpf(repr(M_msun)) * M_SUN) / C0**3


def s2_from_x(x, rsat):
    """S^2 at radius r = r_sat + x -- CANCELLATION-FREE.

    S^2 = 1 - A^2 = (r^2 - r_sat^2)/r^2 = x(2 r_sat + x)/(r_sat + x)^2.
    """
    return x * (2 * rsat + x) / (rsat + x) ** 2


def x_from_s2(s2, rsat):
    """Inverse of s2_from_x: x = r_sat (1/A - 1) with A = sqrt(1 - S^2)."""
    A = mp.sqrt(1 - s2)
    return rsat * (1 / A - 1)


# ---------------------------------------------------------------------------
# section 2.3 -- the closed form containing BOTH branches
# ---------------------------------------------------------------------------
def J_closed(p):
    """J(p) = 1 - sqrt(pi) Gamma(1 - p/2) / Gamma((1 - p)/2).

    Finite at p = 1/2 (RHO-A); a Gamma pole at p = 2 (RHO-B).
    """
    return 1 - mp.sqrt(mp.pi) * mp.gamma(1 - p / 2) / mp.gamma((1 - p) / 2)


def J_quad(p, a_lo=0, a_hi=1):
    """Numerical quadrature of the same integrand: INT [(1-A^2)^{-p/2} - 1] dA/A^2."""
    def integrand(A):
        if A == 0:
            return p / 2
        return (mp.expm1(-(p / 2) * mp.log1p(-A**2))) / A**2
    return mp.quad(integrand, [a_lo, a_hi])


def excess_tail_integral(p, a_hi):
    """(c_0/r_sat) * INT_{r(a_hi)}^{infinity} (1/v - 1/c_0) dr, dimensionless.

    Equals INT_0^{a_hi} [(1-A^2)^{-p/2} - 1] dA/A^2.  Exact for p = 2:
    artanh(a_hi).
    """
    if p == 2:
        return mp.atanh(a_hi)
    return J_quad(p, 0, a_hi)


# ---------------------------------------------------------------------------
# section 2.2 -- the regulated node sum
# ---------------------------------------------------------------------------
def _f_excess_block(x_arr, rsat_f, p_f, c0_f, lumped_omega=None, ell_f=None):
    """(1/v - 1/c_0) on a float64 block of x = r - r_sat, cancellation-free.

    lumped_omega, when given, applies the REJECTED lumped-dispersion group
    velocity v_g = v sqrt(1 - (omega l /(2 v))^2)  (robustness variant D2);
    entries past cutoff are returned as NaN so the caller can truncate.
    """
    s2 = x_arr * (2.0 * rsat_f + x_arr) / (rsat_f + x_arr) ** 2
    logS2 = np.log(s2)
    # v/c_0 = S^p ; 1/v - 1/c_0 = (S^{-p} - 1)/c_0 = expm1(-p/2 log S^2)/c_0
    inv = np.expm1(-(p_f / 2.0) * logS2) / c0_f
    if lumped_omega is None:
        return inv
    v = c0_f * np.exp((p_f / 2.0) * logS2)
    arg = lumped_omega * ell_f / (2.0 * v)
    rad = 1.0 - arg**2
    vg = np.where(rad > 0.0, v * np.sqrt(np.abs(rad)), np.nan)
    return 1.0 / vg - 1.0 / c0_f


def node_sum_excess(p, rsat, theta, n_split, x_inner=None,
                    lumped_omega=None):
    """One-way EXCESS delay by the regulated node sum + exact integral tail.

    T = SUM_{n=1..n_split} l_node * f(x_n)  +  INT_{x_split + l/2}^{inf} f dx
    with x_n = x_inner + (n-1) l_node, x_inner = theta*l_node by default.
    """
    rsat_f = float(rsat)
    p_f = float(p)
    c0_f = float(C0)
    l_f = float(L_NODE)
    x0 = float(theta * L_NODE) if x_inner is None else float(x_inner)

    total = 0.0
    n_cut = 0
    block = 10**6
    done = 0
    while done < n_split:
        m = min(block, n_split - done)
        idx = np.arange(done, done + m, dtype=np.float64)
        x = x0 + idx * l_f
        vals = _f_excess_block(x, rsat_f, p_f, c0_f, lumped_omega, l_f)
        if lumped_omega is not None:
            # cells past the lumped-dispersion band edge are EVANESCENT and
            # contribute no propagating delay; they are the INNERMOST cells,
            # so they are masked, NOT truncated-and-returned.
            bad = np.isnan(vals)
            n_cut += int(bad.sum())
            vals = np.where(bad, 0.0, vals)
        total += float(np.sum(vals))
        done += m

    x_match = mp.mpf(repr(x0)) + (mp.mpf(n_split) - 1) * L_NODE + L_NODE / 2
    a_match = rsat / (rsat + x_match)
    tail = (rsat / C0) * excess_tail_integral(p, a_match)
    return mp.mpf(repr(total)) * L_NODE + tail, n_cut


def continuum_excess(p, rsat, x_inner):
    """One-way EXCESS delay by the CONTINUUM integral cut at x_inner (variant R5)."""
    a_in = rsat / (rsat + x_inner)
    return (rsat / C0) * excess_tail_integral(p, a_in)


# ---------------------------------------------------------------------------
# section 2.5 -- the substrate-native dispersion, and the local band edge
# ---------------------------------------------------------------------------
def omega_max_local(beta, p, s2):
    """omega_max(r) = beta * omega_C * S(r)^p  (Op14 local-clock modulation)."""
    return beta * OMEGA_C * mp.e ** ((p / 2) * mp.log(s2))


def s_turn(omega, beta, p):
    """Band-edge turning point: S^p = eps == omega/(beta omega_C)."""
    eps = omega / (beta * OMEGA_C)
    return eps ** (1 / p)


def s_last(theta, rsat):
    """Last-node cutoff: S at x = theta * l_node (cancellation-free)."""
    return mp.sqrt(s2_from_x(theta * L_NODE, rsat))


# ---------------------------------------------------------------------------
# section 2.6 -- the effective barrier and PLANE-PEAK
# ---------------------------------------------------------------------------
def U_collected(A, ell=ELL):
    """U * r_sat^2 = l(l+1) A^2 + A^4/(2 S^2) - (3/4) A^6 / S^4."""
    s2 = 1 - A**2
    return ell * (ell + 1) * A**2 + A**4 / (2 * s2) - mp.mpf(3) / 4 * A**6 / s2**2


def U_uncollected(A, ell=ELL):
    """U r_sat^2 from the raw transformation: l(l+1)/r^2 + 2g/r + g^2/4 + g'/2.

    Written in r with r_sat = 1 so the result is already U * r_sat^2.
    """
    def mu(r):
        return mp.sqrt(1 - (1 / r) ** 2)          # G_vac = 1, A = 1/r

    def g(r):
        return mp.diff(mu, r) / mu(r)

    r = 1 / A
    return (ell * (ell + 1) / r**2 + 2 * g(r) / r + g(r) ** 2 / 4
            + mp.diff(g, r) / 2)


def V_barrier(A, p, ell=ELL):
    """V(A) = v^2 U (r_sat^2/c_0^2) = S^{2p} * (U r_sat^2)."""
    s2 = 1 - A**2
    return s2**p * U_collected(A, ell)


def find_peak(p, ell=ELL):
    """Bracketed maximum of V(A) on A_PEAK_BRACKET."""
    def dV(A):
        return mp.diff(lambda a: V_barrier(a, p, ell), A)
    lo, hi = A_PEAK_BRACKET
    n = 400
    grid = [lo + (hi - lo) * mp.mpf(i) / n for i in range(n + 1)]
    vals = [dV(a) for a in grid]
    brack = None
    for i in range(n):
        if vals[i] > 0 > vals[i + 1]:
            brack = (grid[i], grid[i + 1])
            break
    if brack is None:
        return None
    root = mp.findroot(dV, (brack[0], brack[1]), solver="bisect", tol=mp.mpf("1e-30"))
    d2 = mp.diff(lambda a: V_barrier(a, p, ell), root, 2)
    return {"A_peak": root, "bracket": brack, "d2": d2,
            "V_peak": V_barrier(root, p, ell)}


# ---------------------------------------------------------------------------
# read-only prior-lane inputs (J10-J13)
# ---------------------------------------------------------------------------
def load_v24():
    with open(V24_JSON, encoding="utf-8") as fh:
        J = json.load(fh)
    return {
        "Omega_re": mp.mpf(J["certified_root"]["Omega_re_mp"]),
        "omega_R_M_g": mp.mpf(repr(J["adjudication"]["omega_R_M_g"])),
        "omega_I_M_g": mp.mpf(repr(J["adjudication"]["omega_I_M_g"])),
        "Q_GR": mp.mpf(repr(J["comparators"]["Q_GR"])),
        "x_sat_shipped": mp.mpf(repr(J["_frozen_numerics"]["x_sat"])),
    }


def load_predecessor():
    spec = importlib.util.spec_from_file_location("_pred", PRED_DRIVER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def total_delay_mine(p, rsat, fac):
    """2 * INT_{r_sat}^{fac r_sat} dr/v  -- the NON-excess delay, for G-NC."""
    a_out = 1 / mp.mpf(repr(fac))

    def integrand(A):
        return mp.e ** (-(p / 2) * mp.log1p(-A**2)) / A**2

    return 2 * (rsat / C0) * mp.quad(integrand, [a_out, 1])


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main() -> int:
    t_start = time.time()
    v24 = load_v24()
    pred = load_predecessor()

    out: dict = {
        "_prereg": "research/2026-08-04_echo-delay-regulated-sum_prereg-FROZEN.md",
        "_prereg_commit": "1da06a90",
        "_method": ("regulated node sum + exact integral tail; closed forms in "
                    "mpmath dps=50; PLANE-inf excess delay (plane-invariant); "
                    "substrate-native ARCCOS transmission-line band model"),
        "_non_claim": ("computes a DELAY only: no reflectivity, no echo "
                       "amplitude, no echo train, no detectability, no "
                       "adjudication of FORK-3(b)"),
        "_frozen_numerics": {
            "p_A": float(P_A), "p_B": float(P_B), "p_SYN": float(P_SYN),
            "thetas": [float(t) for t in THETAS],
            "betas": [float(b) for b in BETAS],
            "n_splits": list(N_SPLITS), "n_split_primary": N_SPLIT_PRIMARY,
            "mass_grid_msun": list(MASS_GRID_MSUN), "m_ref_msun": M_REF_MSUN,
            "ell": ELL, "dps": mp.mp.dps, "x_sat": float(X_SAT),
            "bin_cutoff_threshold": float(BIN_CUTOFF_THRESHOLD),
        },
        "canonical_inputs": {
            "l_node_m": mp.nstr(L_NODE, 17),
            "omega_C_rad_s": mp.nstr(OMEGA_C, 17),
            "c_0_m_s": float(C0),
        },
        "prior_lane_inputs": {k: mp.nstr(v, 17) for k, v in v24.items()},
        "gates": {}, "self_tests": {}, "configurations": {},
        "regulator_sweep": {}, "bins": {},
    }

    rsat_ref = r_sat_of(M_REF_MSUN)
    out["reference"] = {
        "M_ref_Msun": M_REF_MSUN,
        "r_sat_m": mp.nstr(rsat_ref, 17),
        "r_sat_over_c0_s": mp.nstr(rsat_ref / C0, 17),
        "l_node_over_r_sat": mp.nstr(L_NODE / rsat_ref, 17),
    }

    # --- the substrate-native ringdown scales (J10, J11) --------------------
    omega_v24 = v24["Omega_re"] * C0 / rsat_ref
    tau_ring_ref = m_g_time(M_REF_MSUN) / v24["omega_I_M_g"]
    out["reference"]["omega_ringdown_rad_s"] = mp.nstr(omega_v24, 17)
    out["reference"]["tau_ring_s"] = mp.nstr(tau_ring_ref, 17)

    # =======================================================================
    # G-CANON
    # =======================================================================
    canon_a = abs(OMEGA_C * L_NODE / C0 - 1)
    canon_b = abs(L_NODE * M_E * C0 / HBAR - 1)
    canon_c = abs(X_SAT - v24["x_sat_shipped"])
    out["gates"]["G-CANON"] = {
        "omega_C_l_node_over_c0_minus_1": mp.nstr(canon_a, 6),
        "l_node_m_e_c0_over_hbar_minus_1": mp.nstr(canon_b, 6),
        "x_sat_vs_v24_shipped": mp.nstr(canon_c, 6),
        "pass": bool(canon_a < mp.mpf("1e-15") and canon_b < mp.mpf("1e-15")
                     and canon_c == 0),
    }

    # =======================================================================
    # G-NC -- the NEGATIVE CONTROL against the 2026-06-17 predecessor driver
    # =======================================================================
    M_pred = mp.mpf(repr(pred.M_GW150914 / pred.MSUN))
    nc_rows = []
    worst = mp.mpf(0)
    rsat_pred = r_sat_of(float(M_pred))
    for fac in (1.1, 1.5, 2.0, 3.0):
        theirs = mp.mpf(repr(pred.echo_delay(pred.M_GW150914, fac)))
        mine = total_delay_mine(P_A, rsat_pred, fac)
        rel = abs(mine / theirs - 1)
        worst = max(worst, rel)
        nc_rows.append({"r_out_over_r_sat": fac,
                        "predecessor_s": mp.nstr(theirs, 17),
                        "this_lane_s": mp.nstr(mine, 17),
                        "rel_sep": mp.nstr(rel, 6)})
    out["gates"]["G-NC"] = {"rows": nc_rows, "worst_rel": mp.nstr(worst, 17),
                            "tol": mp.nstr(TOL_NC, 3),
                            "pass": bool(worst < TOL_NC)}
    out["reference"]["predecessor_mass_Msun"] = float(M_pred)

    # =======================================================================
    # G-JA / G-CF -- the closed forms against their own quadrature
    # =======================================================================
    J_A_closed, J_A_quad = J_closed(P_A), J_quad(P_A)
    ja_sep = abs(J_A_closed - J_A_quad)
    out["gates"]["G-JA"] = {"J_A_closed": mp.nstr(J_A_closed, 25),
                            "J_A_quad": mp.nstr(J_A_quad, 25),
                            "sep": mp.nstr(ja_sep, 6),
                            "tol": mp.nstr(TOL_JA, 3),
                            "pass": bool(ja_sep < TOL_JA)}
    a_test = mp.mpf("0.9999")
    cf_sep = abs(mp.atanh(a_test) - J_quad(P_B, 0, a_test))
    out["gates"]["G-CF"] = {"artanh": mp.nstr(mp.atanh(a_test), 25),
                            "quad": mp.nstr(J_quad(P_B, 0, a_test), 25),
                            "sep": mp.nstr(cf_sep, 6),
                            "tol": mp.nstr(TOL_CF, 3),
                            "pass": bool(cf_sep < TOL_CF)}
    # the Gamma pole at p = 2 -- the two-method receipt that RHO-B diverges
    try:
        _g = mp.gamma(1 - P_B / 2)
        pole_note = f"Gamma(0) evaluated finite: {mp.nstr(_g, 6)} -- UNEXPECTED"
    except ValueError as exc:
        pole_note = f"Gamma(1 - p/2) at p = 2 raises: {exc} -- RHO-B DIVERGES"
    out["gates"]["G-JA"]["gamma_pole_at_p2"] = pole_note

    # =======================================================================
    # G-SUM -- split-independence of the regulated node sum
    # =======================================================================
    sum_rows = {}
    for p, tag in ((P_A, "RHO-A"), (P_B, "RHO-B")):
        vals = []
        for ns in N_SPLITS:
            t, _ = node_sum_excess(p, rsat_ref, THETAS[0], ns)
            vals.append(t)
        seps = [abs(vals[i] / vals[0] - 1) for i in (1, 2)]
        sum_rows[tag] = {"values_s": [mp.nstr(v, 17) for v in vals],
                         "max_rel_sep": mp.nstr(max(seps), 6)}
    worst_sum = max(mp.mpf(sum_rows[t]["max_rel_sep"]) for t in sum_rows)
    out["gates"]["G-SUM"] = {"per_branch": sum_rows,
                             "worst_rel": mp.nstr(worst_sum, 6),
                             "tol": mp.nstr(TOL_SUM, 3),
                             "pass": bool(worst_sum < TOL_SUM)}

    # =======================================================================
    # G-U -- the collected effective potential against the raw transformation
    # =======================================================================
    u_worst = mp.mpf(0)
    for i in range(12):
        A = mp.mpf("0.07") + mp.mpf("0.07") * i
        u_worst = max(u_worst, abs(U_collected(A) - U_uncollected(A)))
    out["gates"]["G-U"] = {"worst_abs_sep": mp.nstr(u_worst, 6),
                           "tol": mp.nstr(TOL_U, 3),
                           "pass": bool(u_worst < TOL_U)}

    # =======================================================================
    # G-DISP -- the arccos map on the z = 2 radial cascade is EXACTLY LINEAR
    # =======================================================================
    disp_worst = mp.mpf(0)
    for i in range(1, 200):
        kl = mp.pi * mp.mpf(i) / 200
        disp_worst = max(disp_worst, abs(mp.acos(mp.cos(kl)) - kl))
    out["gates"]["G-DISP"] = {"worst_abs_sep": mp.nstr(disp_worst, 6),
                              "tol": mp.nstr(TOL_DISP, 3),
                              "pass": bool(disp_worst < TOL_DISP),
                              "note": ("z = 2 adjacency mu(k) = 2 cos(k l); "
                                       "omega = omega_link arccos(mu/2) = "
                                       "omega_link k l -> v_group == v_phase")}

    # =======================================================================
    # G-PEAK -- the derived barrier maximum, per branch
    # =======================================================================
    peaks = {}
    peak_ok = True
    for p, tag in ((P_A, "RHO-A"), (P_B, "RHO-B")):
        pk = find_peak(p)
        if pk is None:
            peak_ok = False
            peaks[tag] = {"found": False}
            continue
        ok = bool(pk["d2"] < 0 and 0 < pk["A_peak"] < 1)
        peak_ok = peak_ok and ok
        peaks[tag] = {
            "found": True,
            "A_peak": mp.nstr(pk["A_peak"], 17),
            "r_peak_over_r_sat": mp.nstr(1 / pk["A_peak"], 17),
            "r_peak_over_GM_c2": mp.nstr(X_SAT / pk["A_peak"], 17),
            "V_peak": mp.nstr(pk["V_peak"], 17),
            "d2_negative": bool(pk["d2"] < 0),
        }
    out["gates"]["G-PEAK"] = {"per_branch": peaks, "pass": peak_ok}

    # =======================================================================
    # G-DECADE -- each decade of S contributes ln 10 * (r_sat/c_0) under RHO-B
    # =======================================================================
    dec_rows, dec_worst = [], mp.mpf(0)
    for k in (2, 3, 4, 5, 6):
        s_hi, s_lo = mp.mpf(10) ** (-k), mp.mpf(10) ** (-(k + 1))
        a_hi = mp.sqrt(1 - s_lo**2)
        a_lo = mp.sqrt(1 - s_hi**2)
        contrib = mp.atanh(a_hi) - mp.atanh(a_lo)
        rel = abs(contrib / mp.log(10) - 1)
        dec_worst = max(dec_worst, rel)
        dec_rows.append({"decade": f"1e-{k} -> 1e-{k+1}",
                         "contribution_over_r_sat_c0": mp.nstr(contrib, 17),
                         "rel_dev_from_ln10": mp.nstr(rel, 6)})
    out["gates"]["G-DECADE"] = {"rows": dec_rows,
                                "worst_rel": mp.nstr(dec_worst, 6),
                                "tol": mp.nstr(TOL_DECADE, 3),
                                "pass": bool(dec_worst < TOL_DECADE)}

    # =======================================================================
    # G-DISC -- the derived discrete-minus-continuum offset (gamma)
    # =======================================================================
    disc_rows, disc_worst = [], mp.mpf(0)
    for theta in THETAS:
        node, _ = node_sum_excess(P_B, rsat_ref, theta, N_SPLIT_PRIMARY)
        cont = continuum_excess(P_B, rsat_ref, theta * L_NODE)
        measured = (node - cont) / (rsat_ref / C0)
        derived = mp.euler if theta == 1 else mp.euler + 2 * mp.log(2)
        rel = abs(measured / derived - 1)
        disc_worst = max(disc_worst, rel)
        disc_rows.append({"theta": float(theta),
                          "measured_K_disc": mp.nstr(measured, 17),
                          "derived": mp.nstr(derived, 17),
                          "rel_sep": mp.nstr(rel, 6)})
    out["gates"]["G-DISC"] = {"rows": disc_rows,
                              "worst_rel": mp.nstr(disc_worst, 6),
                              "tol": mp.nstr(TOL_DISC, 3),
                              "pass": bool(disc_worst < TOL_DISC)}

    # =======================================================================
    # THE PHYSICS: the two branches on the mass grid, PLANE-inf excess delay
    # =======================================================================
    J_A = J_A_closed
    for tag, p in (("CFG-A", P_A), ("CFG-B", P_B)):
        rows = []
        for M in MASS_GRID_MSUN:
            rs = r_sat_of(M)
            one_way, _ = node_sum_excess(p, rs, THETAS[0], N_SPLIT_PRIMARY)
            T = 2 * one_way
            row = {
                "M_Msun": M,
                "r_sat_over_c0_s": mp.nstr(rs / C0, 17),
                "T_return_excess_s": mp.nstr(T, 17),
                "T_return_over_r_sat_c0": mp.nstr(T / (rs / C0), 17),
                "tau_ring_s": mp.nstr(m_g_time(M) / v24["omega_I_M_g"], 17),
            }
            if p == P_A:
                closed = 2 * (rs / C0) * J_A
                row["closed_form_s"] = mp.nstr(closed, 17)
                row["rel_sep_from_closed"] = mp.nstr(abs(T / closed - 1), 6)
            else:
                closed = (rs / C0) * mp.log(2 * rs / (THETAS[0] * L_NODE))
                row["log_law_s"] = mp.nstr(closed, 17)
                row["K_disc_measured"] = mp.nstr((T - closed) / (rs / C0), 17)
                row["ln_arg_2rsat_over_lnode"] = mp.nstr(
                    mp.log(2 * rs / L_NODE), 17)
            rows.append(row)
        out["configurations"][tag] = {"p": float(p), "rows": rows}

    out["configurations"]["CFG-A"]["J_A_closed"] = mp.nstr(J_A, 17)
    out["configurations"]["CFG-A"]["two_J_A"] = mp.nstr(2 * J_A, 17)

    # PLANE-PEAK secondary totals
    for tag, p in (("CFG-A", P_A), ("CFG-B", P_B)):
        pk = peaks["RHO-A" if p == P_A else "RHO-B"]
        if not pk["found"]:
            continue
        a_peak = mp.mpf(pk["A_peak"])
        a_in = rsat_ref / (rsat_ref + THETAS[0] * L_NODE)

        def integ(A, _p=p):
            return mp.e ** (-(_p / 2) * mp.log1p(-A**2)) / A**2

        tot = 2 * (rsat_ref / C0) * mp.quad(integ, [a_peak, a_in])
        out["configurations"][tag]["plane_peak_total_s_at_Mref"] = mp.nstr(tot, 17)
        out["configurations"][tag]["plane_peak_over_r_sat_c0"] = mp.nstr(
            tot / (rsat_ref / C0), 17)

    # =======================================================================
    # THE TURNING POINT (section 2.7) -- the full sweep
    # =======================================================================
    turn_rows = []
    node_governed_all, band_governed_all = True, True
    for M in MASS_GRID_MSUN:
        rs = r_sat_of(M)
        om = v24["Omega_re"] * C0 / rs
        for beta in BETAS:
            for theta in THETAS:
                for p, tag in ((P_A, "RHO-A"), (P_B, "RHO-B")):
                    st = s_turn(om, beta, p)
                    sl = s_last(theta, rs)
                    ratio = st / sl
                    if p == P_B:
                        node_governed_all &= bool(st < sl)
                        band_governed_all &= bool(st > sl)
                    turn_rows.append({
                        "M_Msun": M, "beta": float(beta),
                        "theta": float(theta), "branch": tag,
                        "S_turn": mp.nstr(st, 6), "S_last": mp.nstr(sl, 6),
                        "S_turn_over_S_last": mp.nstr(ratio, 17),
                        "governed_by": "NODE" if st < sl else "BAND-EDGE",
                    })
    out["turning_point"] = {
        "rows": turn_rows,
        "closed_form": "S_turn/S_last = sqrt(Omega/(2 theta beta))  -- MASS-FREE",
        "all_node_governed_RHO_B": node_governed_all,
        "all_band_governed_RHO_B": band_governed_all,
    }

    # =======================================================================
    # THE REGULATOR SWEEP (section 4.4) -- BIN-CUTOFF is decided on this
    # =======================================================================
    def sweep(p):
        om = v24["Omega_re"] * C0 / rsat_ref
        vals = {}
        v_r1, _ = node_sum_excess(p, rsat_ref, mp.mpf(1), N_SPLIT_PRIMARY)
        vals["R1_full_node"] = 2 * v_r1
        v_r2, _ = node_sum_excess(p, rsat_ref, mp.mpf(1) / 2, N_SPLIT_PRIMARY)
        vals["R2_half_node"] = 2 * v_r2
        for beta in BETAS:
            st = s_turn(om, beta, p)
            x_t = x_from_s2(st**2, rsat_ref)
            x_in = max(x_t, L_NODE)
            v_r3, _ = node_sum_excess(p, rsat_ref, mp.mpf(1),
                                      N_SPLIT_PRIMARY, x_inner=x_in)
            vals[f"R3_turning_beta_{mp.nstr(beta, 6)}"] = 2 * v_r3
        v_r4, _ = node_sum_excess(p, rsat_ref, mp.mpf(1), N_SPLIT_PRIMARY,
                                  x_inner=2 * L_NODE)
        vals["R4_strained_pitch"] = 2 * v_r4
        vals["R5_continuum"] = 2 * continuum_excess(p, rsat_ref, L_NODE)
        v_d2, n_cut = node_sum_excess(p, rsat_ref, mp.mpf(1), N_SPLIT_PRIMARY,
                                      lumped_omega=float(om))
        vals["D2_lumped_dispersion"] = 2 * v_d2
        arr = sorted(vals.values())
        med = arr[len(arr) // 2]
        spread = (arr[-1] - arr[0]) / med
        return vals, spread, n_cut

    for tag, p in (("CFG-A", P_A), ("CFG-B", P_B), ("CFG-SYN", P_SYN)):
        vals, spread, n_cut = sweep(p)
        out["regulator_sweep"][tag] = {
            "values_s": {k: mp.nstr(v, 17) for k, v in vals.items()},
            "spread": mp.nstr(spread, 17),
            "D2_evanescent_cells_masked": n_cut,
        }

    # =======================================================================
    # THE SELF-TESTS (section 6) -- each MUST fire
    # =======================================================================
    st_out = {}

    # FT-NC
    ft = abs((mp.mpf(nc_rows[0]["this_lane_s"]) * (1 + mp.mpf("1e-6")))
             / mp.mpf(nc_rows[0]["predecessor_s"]) - 1)
    st_out["FT-NC"] = {"measured": mp.nstr(ft, 6), "threshold": "1e-7",
                       "fires": bool(ft >= mp.mpf("1e-7"))}
    # FT-JA
    ft = abs(J_A * (1 + mp.mpf("1e-9")) - J_A_quad)
    st_out["FT-JA"] = {"measured": mp.nstr(ft, 6), "threshold": "1e-10",
                       "fires": bool(ft >= mp.mpf("1e-10"))}
    # FT-CF
    ft = abs(mp.atanh(a_test) * (1 + mp.mpf("1e-12")) - J_quad(P_B, 0, a_test))
    st_out["FT-CF"] = {"measured": mp.nstr(ft, 6), "threshold": "1e-13",
                       "fires": bool(ft >= mp.mpf("1e-13"))}
    # FT-SUM -- drop the integral tail entirely
    def _sum_no_tail(p, ns):
        rsat_f, p_f, c0_f = float(rsat_ref), float(p), float(C0)
        l_f, x0 = float(L_NODE), float(L_NODE)
        tot, done = 0.0, 0
        while done < ns:
            m = min(10**6, ns - done)
            x = x0 + np.arange(done, done + m, dtype=np.float64) * l_f
            tot += float(np.sum(_f_excess_block(x, rsat_f, p_f, c0_f)))
            done += m
        return mp.mpf(repr(tot)) * L_NODE
    a1, a2 = _sum_no_tail(P_B, 10**5), _sum_no_tail(P_B, 10**6)
    ft = abs(a2 / a1 - 1)
    st_out["FT-SUM"] = {"measured": mp.nstr(ft, 6), "threshold": "1e-3",
                        "fires": bool(ft >= mp.mpf("1e-3"))}
    # FT-U -- drop the g^2/4 term
    def _U_broken(A, ell=ELL):
        def mu(r):
            return mp.sqrt(1 - (1 / r) ** 2)

        def g(r):
            return mp.diff(mu, r) / mu(r)
        r = 1 / A
        return (ell * (ell + 1) / r**2 + 2 * g(r) / r + mp.diff(g, r) / 2)
    ft = abs(U_collected(mp.mpf("0.5")) - _U_broken(mp.mpf("0.5")))
    st_out["FT-U"] = {"measured": mp.nstr(ft, 6), "threshold": "1e-6",
                      "fires": bool(ft >= mp.mpf("1e-6"))}
    # FT-DISP -- the REJECTED lumped map
    d = mp.mpf(0)
    for i in range(1, 200):
        kl = mp.pi * mp.mpf(i) / 200
        d = max(d, abs(2 * mp.sin(kl / 2) - kl))
    st_out["FT-DISP"] = {"measured": mp.nstr(d, 6), "threshold": "1e-2",
                         "fires": bool(d >= mp.mpf("1e-2"))}
    # FT-PEAK
    a_p = mp.mpf(peaks["RHO-B"]["A_peak"])
    ft = abs(mp.diff(lambda a: V_barrier(a, P_B), a_p * mp.mpf("1.01")))
    st_out["FT-PEAK"] = {"measured": mp.nstr(ft, 6), "threshold": "1e-4",
                         "fires": bool(ft >= mp.mpf("1e-4"))}
    # FT-DECADE -- the RHO-A profile, where no log law holds
    s_hi, s_lo = mp.mpf("1e-3"), mp.mpf("1e-4")
    a_hi, a_lo = mp.sqrt(1 - s_lo**2), mp.sqrt(1 - s_hi**2)
    contrib = J_quad(P_A, a_lo, a_hi)
    ft = abs(contrib / mp.log(10) - 1)
    st_out["FT-DECADE"] = {"measured": mp.nstr(ft, 6), "threshold": "0.1",
                           "fires": bool(ft >= mp.mpf("0.1"))}
    # FT-CUT -- the synthetic power-law-divergent profile
    syn_spread = mp.mpf(out["regulator_sweep"]["CFG-SYN"]["spread"])
    st_out["FT-CUT"] = {"measured": mp.nstr(syn_spread, 6),
                        "threshold": mp.nstr(BIN_CUTOFF_THRESHOLD, 3),
                        "fires": bool(syn_spread > BIN_CUTOFF_THRESHOLD)}
    # FT-EVAN
    om_ref = v24["Omega_re"] * C0 / rsat_ref
    om_evan = om_ref * mp.mpf("1e20")
    s2_out = s2_from_x(mp.mpf(10) ** 6 * rsat_ref, rsat_ref)
    max_ratio = omega_max_local(BETAS[0], P_B, s2_out) / om_evan
    st_out["FT-EVAN"] = {"max_omega_max_over_omega": mp.nstr(max_ratio, 6),
                         "fires": bool(max_ratio < 1)}
    # FT-TURN
    om_turn = om_ref * mp.mpf("1e12")
    st_ = s_turn(om_turn, BETAS[0], P_B)
    sl_ = s_last(mp.mpf(1), rsat_ref)
    st_out["FT-TURN"] = {"S_turn": mp.nstr(st_, 6), "S_last": mp.nstr(sl_, 6),
                         "fires": bool(st_ > sl_)}
    # FT-CANON
    ft = abs(OMEGA_C * (L_NODE * (1 + mp.mpf("1e-12"))) / C0 - 1)
    st_out["FT-CANON"] = {"measured": mp.nstr(ft, 6), "threshold": "1e-15",
                          "fires": bool(ft >= mp.mpf("1e-15"))}
    out["self_tests"] = st_out

    # =======================================================================
    # THE BINS (section 7), in the frozen precedence order
    # =======================================================================
    gates_pass = all(g.get("pass", False) for g in out["gates"].values())
    tests_fire = all(t.get("fires", False) for t in st_out.values())
    certified = bool(gates_pass and tests_fire)
    out["certification"] = ("DELAY-CERTIFIED" if certified
                            else "DELAY-NOT-CERTIFIED")

    # PER-CONFIGURATION certification, which the prereg section 7.0 requires
    # ("Certification ... is stated PER CONFIGURATION").  The gate-to-
    # configuration map is declared here, not inferred: it is fixed by which
    # branch each gate's arithmetic runs on.
    GATE_SCOPE = {
        "G-CANON": ("CFG-A", "CFG-B"), "G-U": ("CFG-A", "CFG-B"),
        "G-DISP": ("CFG-A", "CFG-B"), "G-SUM": ("CFG-A", "CFG-B"),
        "G-PEAK": ("CFG-A", "CFG-B"),
        "G-NC": ("CFG-A",), "G-JA": ("CFG-A",),
        "G-CF": ("CFG-B",), "G-DECADE": ("CFG-B",), "G-DISC": ("CFG-B",),
    }
    TEST_SCOPE = {
        "FT-NC": ("CFG-A",), "FT-JA": ("CFG-A",),
        "FT-CF": ("CFG-B",), "FT-SUM": ("CFG-B",), "FT-DECADE": ("CFG-B",),
        "FT-PEAK": ("CFG-B",),
        "FT-U": ("CFG-A", "CFG-B"), "FT-DISP": ("CFG-A", "CFG-B"),
        "FT-CANON": ("CFG-A", "CFG-B"), "FT-EVAN": ("CFG-A", "CFG-B"),
        "FT-TURN": ("CFG-A", "CFG-B"), "FT-CUT": ("CFG-A", "CFG-B"),
    }
    per_cfg = {}
    for cfg in ("CFG-A", "CFG-B"):
        failed = [g for g, sc in GATE_SCOPE.items()
                  if cfg in sc and not out["gates"][g].get("pass", False)]
        unfired = [t for t, sc in TEST_SCOPE.items()
                   if cfg in sc and not st_out[t].get("fires", False)]
        per_cfg[cfg] = {
            "gates_in_scope": sorted(g for g, sc in GATE_SCOPE.items()
                                     if cfg in sc),
            "gates_failed": sorted(failed),
            "self_tests_unfired": sorted(unfired),
            "certification": ("DELAY-CERTIFIED" if not failed and not unfired
                              else "DELAY-NOT-CERTIFIED"),
        }
    out["certification_per_configuration"] = per_cfg

    evan = {}
    for tag, p in (("CFG-A", P_A), ("CFG-B", P_B)):
        for beta in BETAS:
            s2_in = s2_from_x(L_NODE, rsat_ref)
            lo = omega_max_local(beta, p, s2_in) / om_ref
            hi = omega_max_local(beta, p, s2_out) / om_ref
            evan[f"{tag}_beta_{mp.nstr(beta, 6)}"] = {
                "omega_max_over_omega_innermost": mp.nstr(lo, 17),
                "omega_max_over_omega_outermost": mp.nstr(hi, 17),
                "bin": "BIN-EVAN-FIRES" if hi < 1 else "BIN-EVAN-CLEAR",
            }
    out["bins"]["BIN-EVAN"] = evan

    cut = {}
    for tag in ("CFG-A", "CFG-B"):
        sp = mp.mpf(out["regulator_sweep"][tag]["spread"])
        cut[tag] = {"spread": mp.nstr(sp, 17),
                    "bin": ("BIN-CUTOFF-ARTIFACT" if sp > BIN_CUTOFF_THRESHOLD
                            else "BIN-CUTOFF-ROBUST")}
    out["bins"]["BIN-CUTOFF"] = cut

    da_ok = all(mp.mpf(r["rel_sep_from_closed"]) < mp.mpf("1e-6")
                for r in out["configurations"]["CFG-A"]["rows"])
    da_ok = da_ok and mp.mpf(out["regulator_sweep"]["CFG-A"]["spread"]) < mp.mpf("1e-6")
    out["bins"]["BIN-DA"] = {"bin": "BIN-DA-CLOSED" if da_ok else "BIN-DA-OPEN"}

    if node_governed_all:
        db = "BIN-DB-NODE"
    elif band_governed_all:
        db = "BIN-DB-BAND"
    else:
        db = "BIN-DB-SPLIT"
    ratios = [mp.mpf(r["S_turn_over_S_last"]) for r in turn_rows
              if r["branch"] == "RHO-B"]
    out["bins"]["BIN-DB"] = {"bin": db,
                             "min_S_turn_over_S_last": mp.nstr(min(ratios), 17),
                             "max_S_turn_over_S_last": mp.nstr(max(ratios), 17)}

    disc_rows2, all_gt, all_le = [], True, True
    for i, M in enumerate(MASS_GRID_MSUN):
        TA = mp.mpf(out["configurations"]["CFG-A"]["rows"][i]["T_return_excess_s"])
        TB = mp.mpf(out["configurations"]["CFG-B"]["rows"][i]["T_return_excess_s"])
        tau = m_g_time(M) / v24["omega_I_M_g"]
        d = abs(TB - TA)
        all_gt &= bool(d > tau)
        all_le &= bool(d <= tau)
        disc_rows2.append({"M_Msun": M, "abs_diff_s": mp.nstr(d, 17),
                           "tau_ring_s": mp.nstr(tau, 17),
                           "diff_over_tau": mp.nstr(d / tau, 17),
                           "T_B_over_T_A": mp.nstr(TB / TA, 17)})
    out["bins"]["BIN-DISC"] = {
        "rows": disc_rows2,
        "bin": ("BIN-DISC" if all_gt else
                "BIN-DEGEN" if all_le else "BIN-DISC-SPLIT")}

    # section 7.5b -- the observational-pointer DIAGNOSTIC (NOT a bin)
    dt_obs = mp.mpf(repr(pred.DT_OBSERVED))
    i_ref = MASS_GRID_MSUN.index(M_REF_MSUN)
    out["observational_pointer_diagnostic"] = {
        "_class": "DIAGNOSTIC, NOT a bin, NOT a verdict, NOT a detection",
        "pointer_s": float(dt_obs),
        "pointer_source": ("existing-experimental-signatures.md:42/:44 via "
                           "bh_shear_echo_delay.py DT_OBSERVED"),
        "RHO_A_ratio_pointer_over_T": mp.nstr(
            dt_obs / mp.mpf(out["configurations"]["CFG-A"]["rows"][i_ref]
                            ["T_return_excess_s"]), 17),
        "RHO_B_ratio_pointer_over_T": mp.nstr(
            dt_obs / mp.mpf(out["configurations"]["CFG-B"]["rows"][i_ref]
                            ["T_return_excess_s"]), 17),
        "RHO_A_ratio_pointer_over_T_plane_peak": mp.nstr(
            dt_obs / mp.mpf(out["configurations"]["CFG-A"]
                            ["plane_peak_total_s_at_Mref"]), 17),
        "RHO_B_ratio_pointer_over_T_plane_peak": mp.nstr(
            dt_obs / mp.mpf(out["configurations"]["CFG-B"]
                            ["plane_peak_total_s_at_Mref"]), 17),
    }

    # BIN GATING BY CERTIFICATION (prereg section 7.0): a DELAY-NOT-CERTIFIED
    # configuration adjudicates NO bin.  Applied here so the shipped object
    # cannot be quoted as an adjudication it is not entitled to.
    for bname, scope in (("BIN-DA", ("CFG-A",)), ("BIN-DB", ("CFG-B",)),
                         ("BIN-DISC", ("CFG-A", "CFG-B"))):
        blocked = [c for c in scope
                   if per_cfg[c]["certification"] == "DELAY-NOT-CERTIFIED"]
        if blocked:
            out["bins"][bname]["adjudicated"] = False
            out["bins"][bname]["not_adjudicated_because"] = (
                f"{sorted(blocked)} is DELAY-NOT-CERTIFIED; the token above is "
                f"a NOT-ADJUDICATED DIAGNOSTIC")
        else:
            out["bins"][bname]["adjudicated"] = True
    for cfg in ("CFG-A", "CFG-B"):
        adj = per_cfg[cfg]["certification"] == "DELAY-CERTIFIED"
        out["bins"]["BIN-CUTOFF"][cfg]["adjudicated"] = adj
        for k in out["bins"]["BIN-EVAN"]:
            if k.startswith(cfg):
                out["bins"]["BIN-EVAN"][k]["adjudicated"] = adj

    # =======================================================================
    # ship
    # =======================================================================
    out["_runtime_sec"] = round(time.time() - t_start, 2)
    body = {k: v for k, v in out.items() if k != "_runtime_sec"}
    out["_digest"] = hashlib.sha256(
        json.dumps(body, sort_keys=True).encode()).hexdigest()[:16]
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, sort_keys=True)
    print(f"[echo-delay] certification: {out['certification']}")
    print(f"[echo-delay] digest: {out['_digest']}")
    print(f"[echo-delay] wrote {os.path.relpath(OUT_JSON, REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

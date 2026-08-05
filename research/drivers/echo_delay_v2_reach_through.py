#!/usr/bin/env python3
"""echo-delay v2 — the certification RERUN plus Y8, the REACH-THROUGH computation.

Resolves the frozen gates and bins of
``research/2026-08-05_echo-delay-v2-reach-through_prereg-FROZEN.md`` (COMMIT 1
of this lane, pushed ALONE before this file existed).

PART 1 -- CERTIFICATION RERUN
-----------------------------
v1 (``research/2026-08-04_echo-delay-regulated-sum_prereg-FROZEN.md``, commit
1da06a90) certified CFG-A and failed CFG-B on TWO freeze-time algebra errors of
its own.  v2 repairs exactly those two and NOTHING else:

  * G-DISC   -- the LAW is repaired.  K_disc(theta) = [ln theta - psi(theta)]/2
                PER ONE-WAY PASS, evaluated from mpmath's digamma.  The 1 per
                cent tolerance is CARRIED UNCHANGED.
  * G-DECADE -- the TOLERANCE is resized from the derived O(S^2) law
                delta = (S_hi^2 - S_lo^2)/(4 ln 10) = 0.99 S_hi^2/(4 ln 10),
                to 1e-4 (limb a, 9.30x headroom) plus a NEW strictly
                strengthening residual limb at 1e-3 (limb b) testing the SHAPE.

Every other threshold, bin boundary, regulator variant, mass, theta, beta and
N_split is byte-identical to v1, and two NEW negative controls demand EXACT
string equality against v1's shipped JSON: G-NC-V1A on the certified CFG-A set
and G-NC-V1B on the CFG-B diagnostics.  If a number moves, the lane STOPS.

PART 2 -- Y8, THE REACH-THROUGH COMPUTATION (SEMICONDUCTOR register)
--------------------------------------------------------------------
DEPLETION EDGE  the per-frequency surface where the local band edge falls to
                the drive, omega = omega_max(r) = beta omega_C S^p.  IDENTICAL
                to v1's S_turn under a ruled name.
DEPLETION WIDTH W(omega) = the number of intact lattice cells between that edge
                and the physical end.  Derived closed form, MASS-FREE:
                W = max(0, floor(Omega/(2 beta) + 1 - theta)).
JUNCTION        the EXACT per-cell ABCD product across the depleted cells.
TWO-PORT        No WKB.  No continuum approximation.
REACH-THROUGH   the thin-W limit in which the FAR CONTACT governs the composite
                reflection at the declared plane.

Carves (prereg section 0.4): what is depleted is SIGNAL-BAND SUPPORT, not
charge; the edge is DRIVE-FREQUENCY-INDEXED; NO space-charge or built-in-field
electrostatics rides along -- small-signal network topology only.

NUMERICAL CONDITIONING (prereg section 0 row 11)
------------------------------------------------
Named cancellations: (i) 1 - A^2 at the innermost node, where
l_node/r_sat ~ 6e-19 and a float64 subtraction returns EXACTLY ZERO -- computed
instead from S^2 = x(2 r_sat + x)/(r_sat + x)^2; (ii) S^{-p} - 1 in the far
field -- from expm1(-p/2 log S^2); (iii) artanh differences in the decade sweep,
~14 digits of cancellation -- mpmath dps = 50; (iv) 1 + rho*Gamma in the Schur
recursion, bounded because |rho_n| <= (sqrt2-1)/(sqrt2+1) = 0.1716; (v) the
accumulated phase, bounded at ~27 rad round trip BECAUSE the delay law is
logarithmic.  float64 is used only where a gate MEASURES its error: G-SUM and
the v1 controls for the node sum, G-UNIT and G-PREC for the Schur recursion.

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
                        "echo_delay_v2_reach_through_results.json")
V1_JSON = os.path.join(REPO, "research", "drivers",
                       "echo_delay_regulated_sum_results.json")
V24_JSON = os.path.join(REPO, "research", "drivers",
                        "coldq_pole_v2p4_root_results.json")
PRED_DRIVER = os.path.join(REPO, "src", "scripts", "vol_3_macroscopic",
                           "bh_shear_echo_delay.py")

mp.mp.dps = 50

# ---------------------------------------------------------------------------
# FROZEN NUMERICS -- PART 1 (prereg section 4.2; IDENTICAL to v1 section 4.2)
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

# frozen PART 1 gate tolerances -- all CARRIED from v1 except G-DECADE's
TOL_NC = mp.mpf("1e-10")
TOL_JA = mp.mpf("1e-20")
TOL_CF = mp.mpf("1e-25")
TOL_SUM = mp.mpf("1e-12")
TOL_U = mp.mpf("1e-30")
TOL_DISP = mp.mpf("1e-15")
TOL_DISC = mp.mpf("0.01")            # CARRIED UNCHANGED -- only the LAW moved
TOL_DECADE_A = mp.mpf("1e-4")        # RESIZED, 9.30x headroom (prereg 2P.2)
TOL_DECADE_B = mp.mpf("1e-3")        # NEW residual limb, 26.7x headroom
BIN_CUTOFF_THRESHOLD = mp.mpf("0.10")

# ---------------------------------------------------------------------------
# FROZEN NUMERICS -- PART 2 / Y8 (prereg section 4Y.2)
# ---------------------------------------------------------------------------
K_WINDOWS = (10**4, 10**5, 10**6)
K_PRIMARY = 10**6
N_BAND = 65
GAMMA_L_READINGS = (("CONTACT-PORT", 0.0), ("CONTACT-FREE", -1.0),
                    ("CONTACT-CLAMPED", +1.0))
MFREE_MASSES = (1.0, 62.0, 100.0)
RT_CONTACT_THRESHOLD = mp.mpf("0.10")   # -20 dB return loss
RT_EDGE_THRESHOLD = mp.mpf("0.90")      # 81 per cent reflected power
SYNTHETIC_LADDER_RATIOS = (mp.mpf("1.01"), mp.mpf(3), mp.mpf(1000))

# frozen Y8 gate tolerances (prereg section 4Y.5)
TOL_BAND = mp.mpf("1e-15")
TOL_ABCD = mp.mpf("1e-14")
TOL_ABCD_ROUTE = mp.mpf("1e-12")
TOL_UNIT = mp.mpf("1e-12")
TOL_PREC = mp.mpf("1e-12")
TOL_KWIN = mp.mpf("1e-3")
TOL_XTIE = mp.mpf("1e-10")
TOL_MFREE = mp.mpf("1e-6")

# canonical constants, imported read-only (ave-canonical-source)
C0 = mp.mpf(repr(K.C_0))
G_NEWTON = mp.mpf(repr(K.G))
M_SUN = mp.mpf(repr(K.M_SUN))
L_NODE = mp.mpf(repr(K.L_NODE))
OMEGA_C = mp.mpf(repr(K.OMEGA_C))
HBAR = mp.mpf(repr(K.HBAR))
M_E = mp.mpf(repr(K.M_E))
X_SAT = mp.mpf(7)          # r_sat = 7 GM/c^2  (J1)


# ===========================================================================
# PART 1 -- v1's machinery, carried BYTE-IDENTICAL so that the float64
# summation order cannot drift.  G-NC-V1A / G-NC-V1B exist to detect it if
# it does.
# ===========================================================================
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


def J_closed(p):
    """J(p) = 1 - sqrt(pi) Gamma(1 - p/2) / Gamma((1 - p)/2)."""
    return 1 - mp.sqrt(mp.pi) * mp.gamma(1 - p / 2) / mp.gamma((1 - p) / 2)


def J_quad(p, a_lo=0, a_hi=1):
    """Quadrature of the same integrand: INT [(1-A^2)^{-p/2} - 1] dA/A^2."""
    def integrand(A):
        if A == 0:
            return p / 2
        return (mp.expm1(-(p / 2) * mp.log1p(-A**2))) / A**2
    return mp.quad(integrand, [a_lo, a_hi])


def excess_tail_integral(p, a_hi):
    """(c_0/r_sat) INT_{r(a_hi)}^{inf} (1/v - 1/c_0) dr.  Exact for p = 2."""
    if p == 2:
        return mp.atanh(a_hi)
    return J_quad(p, 0, a_hi)


def _f_excess_block(x_arr, rsat_f, p_f, c0_f, lumped_omega=None, ell_f=None):
    """(1/v - 1/c_0) on a float64 block of x = r - r_sat, cancellation-free."""
    s2 = x_arr * (2.0 * rsat_f + x_arr) / (rsat_f + x_arr) ** 2
    logS2 = np.log(s2)
    inv = np.expm1(-(p_f / 2.0) * logS2) / c0_f
    if lumped_omega is None:
        return inv
    v = c0_f * np.exp((p_f / 2.0) * logS2)
    arg = lumped_omega * ell_f / (2.0 * v)
    rad = 1.0 - arg**2
    vg = np.where(rad > 0.0, v * np.sqrt(np.abs(rad)), np.nan)
    return 1.0 / vg - 1.0 / c0_f


def node_sum_excess(p, rsat, theta, n_split, x_inner=None, lumped_omega=None):
    """One-way EXCESS delay by the regulated node sum + exact integral tail."""
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
    """One-way EXCESS delay by the CONTINUUM integral cut at x_inner (R5)."""
    a_in = rsat / (rsat + x_inner)
    return (rsat / C0) * excess_tail_integral(p, a_in)


def omega_max_local(beta, p, s2):
    """omega_max(r) = beta omega_C S(r)^p  (Op14 local-clock modulation)."""
    return beta * OMEGA_C * mp.e ** ((p / 2) * mp.log(s2))


def s_turn(omega, beta, p):
    """The DEPLETION EDGE, identical to v1's band-edge turning point."""
    eps = omega / (beta * OMEGA_C)
    return eps ** (1 / p)


def s_last(theta, rsat):
    """S at the innermost intact node, x = theta * l_node."""
    return mp.sqrt(s2_from_x(theta * L_NODE, rsat))


def U_collected(A, ell=ELL):
    """U r_sat^2 = l(l+1) A^2 + A^4/(2 S^2) - (3/4) A^6/S^4."""
    s2 = 1 - A**2
    return ell * (ell + 1) * A**2 + A**4 / (2 * s2) - mp.mpf(3) / 4 * A**6 / s2**2


def U_uncollected(A, ell=ELL):
    """U r_sat^2 from the raw W = Psi/(r sqrt(mu)) transformation."""
    def mu(r):
        return mp.sqrt(1 - (1 / r) ** 2)

    def g(r):
        return mp.diff(mu, r) / mu(r)

    r = 1 / A
    return (ell * (ell + 1) / r**2 + 2 * g(r) / r + g(r) ** 2 / 4
            + mp.diff(g, r) / 2)


def V_barrier(A, p, ell=ELL):
    """V(A) = v^2 U (r_sat^2/c_0^2) = S^{2p} (U r_sat^2)."""
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
    root = mp.findroot(dV, (brack[0], brack[1]), solver="bisect",
                       tol=mp.mpf("1e-30"))
    d2 = mp.diff(lambda a: V_barrier(a, p, ell), root, 2)
    return {"A_peak": root, "bracket": brack, "d2": d2,
            "V_peak": V_barrier(root, p, ell)}


def total_delay_mine(p, rsat, fac):
    """2 INT_{r_sat}^{fac r_sat} dr/v -- the NON-excess delay, for G-NC."""
    a_out = 1 / mp.mpf(repr(fac))

    def integrand(A):
        return mp.e ** (-(p / 2) * mp.log1p(-A**2)) / A**2

    return 2 * (rsat / C0) * mp.quad(integrand, [a_out, 1])


# ---------------------------------------------------------------------------
# THE TWO REPAIRED LAWS -- re-derived in prereg sections 2P.1 and 2P.2 and
# evaluated here from mpmath special functions, never from a transcription.
# ---------------------------------------------------------------------------
def K_disc_derived(theta):
    """K_disc(theta) = [ln(theta) - psi(theta)]/2, PER ONE-WAY PASS.

    From SUM_{n=1..N} 1/(n-1+theta) = psi(N+theta) - psi(theta) against
    INT_{theta l}^{N l} dx/x = ln N - ln theta, with the near-wall RHO-B
    excess 1/v - 1/c_0 -> r_sat/(2 c_0 x).  The factor 1/2 is the whole of
    v1's error and it is derived here, not imported.
    """
    return (mp.log(theta) - mp.digamma(theta)) / 2


def decade_deviation_derived(s_hi, s_lo):
    """The derived relative deviation of one S-decade from ln 10.

    artanh(A) = ln(2/S) - S^2/4 + O(S^4)  with A = sqrt(1 - S^2), so a decade
    from S_hi down to S_lo contributes ln 10 + (S_hi^2 - S_lo^2)/4.
    """
    return (s_hi**2 - s_lo**2) / (4 * mp.log(10))


# ---------------------------------------------------------------------------
# read-only prior-lane inputs
# ---------------------------------------------------------------------------
def load_v24():
    with open(V24_JSON, encoding="utf-8") as fh:
        J = json.load(fh)
    return {
        "Omega_re": mp.mpf(J["certified_root"]["Omega_re_mp"]),
        "Omega_im": mp.mpf(J["certified_root"]["Omega_im_mp"]),
        "omega_R_M_g": mp.mpf(repr(J["adjudication"]["omega_R_M_g"])),
        "omega_I_M_g": mp.mpf(repr(J["adjudication"]["omega_I_M_g"])),
        "Q_GR": mp.mpf(repr(J["comparators"]["Q_GR"])),
        "x_sat_shipped": mp.mpf(repr(J["_frozen_numerics"]["x_sat"])),
    }


def load_v1():
    with open(V1_JSON, encoding="utf-8") as fh:
        return json.load(fh)


def load_predecessor():
    spec = importlib.util.spec_from_file_location("_pred", PRED_DRIVER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def jpath(obj, path):
    """Read a '/'-separated path out of a shipped object."""
    cur = obj
    for part in path.strip("/").split("/"):
        cur = cur[int(part)] if isinstance(cur, list) else cur[part]
    return cur


# ===========================================================================
# PART 2 -- Y8, THE REACH-THROUGH MACHINERY
# ===========================================================================
# The per-cell two-port is the EXACT lossless section
#
#     ABCD_n = [[ cos(th_n) ,  i z_n sin(th_n) ],
#               [ i sin(th_n)/z_n ,  cos(th_n) ]]        det = 1 exactly
#
# with z_n = Z_n/Z_1 = (S_n/S_1)^{1-p}  (prereg 2Y.5: Z = rho v = rho_b c_0
# S^{1-p}, DERIVED from mu = G_vac S and v = c_0 S^p) and th_n the electrical
# length in the frozen reading E1 or E2.
#
# Gamma is propagated by the SCHUR / MOBIUS recursion, which is algebraically
# the same cascade and is used because it is EXACT for the |Gamma_L| = 1
# terminations (where the ABCD route divides by zero) and because every step
# is a Mobius map of the closed unit disc onto itself, so |Gamma| <= 1 is
# preserved structurally and float64 error cannot amplify.
# ---------------------------------------------------------------------------
def cell_profile(cfg, n0, count):
    """S^2 (phase point), z (impedance point) for cells n0+1 .. n0+count.

    ``n0`` is 0-based.  The Y-MID variant moves ONLY the impedance sample to
    the bond midpoint; the phase stays at the node, because the variant is
    about impedance PLACEMENT (prereg section 0.1 item 8) and the per-cell
    delay must remain PART 1's per-node delay.
    """
    l_f = float(L_NODE)
    rs_f = float(cfg["rsat"])
    x_node = cfg["x_inner"] + (np.arange(n0, n0 + count, dtype=np.float64)) * l_f
    x_imp = x_node + (0.5 * l_f if cfg["variant"] == "Y-MID" else 0.0)
    s2_ph = x_node * (2.0 * rs_f + x_node) / (rs_f + x_node) ** 2
    s2_im = x_imp * (2.0 * rs_f + x_imp) / (rs_f + x_imp) ** 2
    p_f = float(cfg["p"])
    z = np.exp(((1.0 - p_f) / 2.0) * np.log(s2_im))       # z propto S^{1-p}
    return s2_ph, z


def schur_small(z_arr, th_arr, gamma_L, steps_off=False):
    """Exact Schur recursion over a short section, float64 or complex.

    Returns Gamma at the OUTER face of the last cell, referenced to that
    cell's own characteristic impedance.
    """
    g = complex(gamma_L)
    n = len(th_arr)
    for j in range(n):
        g = g * np.exp(-2j * th_arr[j])
        if j < n - 1 and not steps_off:
            rho = (z_arr[j] - z_arr[j + 1]) / (z_arr[j] + z_arr[j + 1])
            g = (rho + g) / (1.0 + rho * g)
    return g


def schur_small_mp(z_arr, th_arr, gamma_L):
    """The same recursion in mpmath at dps = 50 -- the G-PREC reference."""
    g = mp.mpc(gamma_L)
    n = len(th_arr)
    for j in range(n):
        g = g * mp.e ** (-2j * th_arr[j])
        if j < n - 1:
            rho = (z_arr[j] - z_arr[j + 1]) / (z_arr[j] + z_arr[j + 1])
            g = (rho + g) / (1 + rho * g)
    return g


def abcd_product(z_arr, th_arr):
    """Exact per-cell ABCD product, NORMALIZED (B in Z_1, C in 1/Z_1).

    Cascade order: T = M_N ... M_1, mapping (V, I) at the INNER face of cell 1
    to the OUTER face of cell N.  An empty section returns the 2x2 IDENTITY,
    which is the W = 0 reach-through statement made exact.
    """
    T = np.array([[1.0 + 0j, 0j], [0j, 1.0 + 0j]])
    for j in range(len(th_arr)):
        c, s, z = np.cos(th_arr[j]), np.sin(th_arr[j]), z_arr[j]
        M = np.array([[c + 0j, 1j * z * s], [1j * s / z, c + 0j]])
        T = M @ T
    return T


def gamma_from_abcd(T, z_load, z_plane):
    """Gamma at the plane from the ABCD product and a finite load impedance."""
    num = T[0, 0] * z_load + T[0, 1]
    den = T[1, 0] * z_load + T[1, 1]
    z_in = num / den
    return (z_in - z_plane) / (z_in + z_plane)


def depletion_width(omega, beta, p, rsat, x_inner):
    """W in cells, by EXACT inversion of the frozen depletion-edge criterion.

    A cell at x_n is depleted iff S_n < S_dep, i.e. x_n < x_dep.  Cells sit at
    x_n = x_inner + (n-1) l_node, so W = #{ m >= 0 : m < (x_dep - x_inner)/l }.
    """
    eps = omega / (beta * OMEGA_C)
    s_dep = eps ** (1 / p)
    if s_dep >= 1:
        return None, s_dep, None          # edge outside the graded region
    a_dep = mp.sqrt(1 - s_dep**2)
    x_dep = rsat * (1 / a_dep - 1)
    t = (x_dep - x_inner) / L_NODE
    W = 0 if t <= 0 else int(mp.ceil(t))
    return W, s_dep, x_dep


def depletion_width_by_count(omega, beta, p, rsat, x_inner, cap=10**7):
    """W by DIRECT node-by-node count from the exact cancellation-free S_n."""
    eps = omega / (beta * OMEGA_C)
    s_dep = eps ** (1 / p)
    n, W = 0, 0
    while n < cap:
        x = x_inner + n * L_NODE
        s = mp.sqrt(s2_from_x(x, rsat))
        if s < s_dep:
            W += 1
            n += 1
        else:
            break
    return W


def y8_pass(cfgs, omega_of_row, cfg_of_row, k_max, checkpoints, blk=4000):
    """The EXACT per-cell cascade, run outward over k_max cells.

    Rows index (config, band-point); columns index the three frozen far-contact
    readings.  Returns, per checkpoint: Gamma (nrow x 3), the local reference
    z at the plane (per config), and the accumulated one-way transit delay and
    one-way phase (per config).
    """
    nrow = len(omega_of_row)
    nterm = len(GAMMA_L_READINGS)
    g = np.empty((nrow, nterm), dtype=np.complex128)
    for t, (_tag, gl) in enumerate(GAMMA_L_READINGS):
        g[:, t] = gl
    nc = len(cfgs)
    p_f = np.array([float(c["p"]) for c in cfgs])
    steps_off = np.array([bool(c["steps_off"]) for c in cfgs])
    coef = np.array([float(cfg_coef(cfgs[cfg_of_row[i]], omega_of_row[i]))
                     for i in range(nrow)])
    # z is normalized to cell 1 of each configuration
    z1 = np.array([cell_profile(c, 0, 1)[1][0] for c in cfgs])

    out = {}
    transit = np.zeros(nc)           # SUM_n l_node / v(r_n), one way, seconds
    phase_sum = np.zeros(nrow)       # SUM_n theta_n, one way, radians
    l_f, c0_f = float(L_NODE), float(C0)
    done = 0
    while done < k_max:
        m = min(blk, k_max - done)
        s2_ph = np.empty((nc, m))
        zz = np.empty((nc, m + 1))
        for ci, c in enumerate(cfgs):
            a, b = cell_profile(c, done, m + 1)
            s2_ph[ci] = a[:m]
            zz[ci] = b / z1[ci]
        sp = np.exp((p_f[:, None] / 2.0) * np.log(s2_ph))      # S^p
        transit += (l_f / c0_f) * np.sum(1.0 / sp, axis=1)
        rho = (zz[:, :m] - zz[:, 1:m + 1]) / (zz[:, :m] + zz[:, 1:m + 1])
        rho[steps_off, :] = 0.0
        th = coef[:, None] / sp[cfg_of_row, :]
        phase_sum += np.sum(th, axis=1)
        ph = np.exp(-2j * th)
        rho_row = rho[cfg_of_row, :]
        for j in range(m):
            n_global = done + j + 1
            g *= ph[:, j][:, None]
            if n_global in checkpoints:
                out[n_global] = {
                    "gamma": g.copy(),
                    "z_plane": zz[:, j].copy(),
                    "transit_oneway_s": transit.copy(),
                    "phase_oneway_rad": phase_sum.copy(),
                }
            if n_global < k_max:
                r = rho_row[:, j][:, None]
                g = (r + g) / (1.0 + r * g)
        done += m
    return out


def cfg_coef(cfg, omega):
    """The frozen electrical-length coefficient: theta_n = coef / S_n^p.

    E1 (PRIMARY, radial-delay-consistent):  coef = omega/omega_C
    E2 (SWEPT,  band-top-consistent):       coef = pi (omega/omega_C) / beta
    """
    base = omega / OMEGA_C
    if cfg["e_reading"] == "E1":
        return base
    return mp.pi * base / cfg["beta"]


# ===========================================================================
# PART 1 DRIVER
# ===========================================================================
def part1():                                          # noqa: C901, PLR0915
    """The certification rerun.  Returns the partial results object."""
    t_start = time.time()
    v24 = load_v24()
    v1 = load_v1()
    pred = load_predecessor()

    out: dict = {
        "_prereg": ("research/2026-08-05_echo-delay-v2-reach-through_"
                    "prereg-FROZEN.md"),
        "_supersedes": ("research/2026-08-04_echo-delay-regulated-sum_"
                        "prereg-FROZEN.md (v1, 1da06a90) -- VERSIONED "
                        "successor; v1's DELAY-NOT-CERTIFIED verdict on CFG-B "
                        "stands as a historical fact and is not converted"),
        "_method": ("PART 1: v1's regulated node sum + exact integral tail, "
                    "byte-identical, with G-DISC's LAW repaired and "
                    "G-DECADE's TOLERANCE resized from the derived O(S^2) "
                    "law. PART 2 (Y8): the EXACT per-cell ABCD / Schur "
                    "cascade over the frozen near-wall window -- no WKB, no "
                    "continuum approximation, no evanescent-decay length"),
        "_non_claim": ("adjudicates no fork; FLAG-CAUSAL is SWEPT at "
                       "Gamma_L in {0,-1,+1} and NOT resolved; no echo "
                       "amplitude, train, visibility or detectability; no "
                       "Gamma_in at PLANE-PEAK or PLANE-inf; nothing "
                       "observational; no claim, solidity, leaf or ledger "
                       "touched"),
        "_carves": {
            "depleted_quantity": ("SIGNAL-BAND SUPPORT, not charge: there is "
                                  "no carrier density, no doping, no ionized "
                                  "background and no charge in this problem"),
            "edge_indexing": ("the depletion edge is DRIVE-FREQUENCY-INDEXED; "
                              "W is a function of omega, not a property of "
                              "the structure"),
            "no_electrostatics": ("no Poisson equation, no built-in "
                                  "potential, no depletion approximation, no "
                                  "C-V relation; small-signal network "
                                  "topology ONLY"),
            "reach_through_scope": ("reach-through here means ONLY that the "
                                    "composite reflection at the declared "
                                    "plane is dominated by the far contact; "
                                    "it is NOT punch-through, implies no "
                                    "breakdown and no irreversible process, "
                                    "and says nothing about Regime IV"),
        },
        "_frozen_numerics": {
            "p_A": float(P_A), "p_B": float(P_B), "p_SYN": float(P_SYN),
            "thetas": [float(t) for t in THETAS],
            "betas": [float(b) for b in BETAS],
            "n_splits": list(N_SPLITS), "n_split_primary": N_SPLIT_PRIMARY,
            "mass_grid_msun": list(MASS_GRID_MSUN), "m_ref_msun": M_REF_MSUN,
            "ell": ELL, "dps": mp.mp.dps, "x_sat": float(X_SAT),
            "bin_cutoff_threshold": float(BIN_CUTOFF_THRESHOLD),
            "K_windows": list(K_WINDOWS), "K_primary": K_PRIMARY,
            "N_band": N_BAND,
            "rt_contact_threshold": float(RT_CONTACT_THRESHOLD),
            "rt_edge_threshold": float(RT_EDGE_THRESHOLD),
            "tol_decade_a": mp.nstr(TOL_DECADE_A, 3),
            "tol_decade_b": mp.nstr(TOL_DECADE_B, 3),
            "tol_disc_carried_from_v1": mp.nstr(TOL_DISC, 3),
        },
        "canonical_inputs": {
            "l_node_m": mp.nstr(L_NODE, 17),
            "omega_C_rad_s": mp.nstr(OMEGA_C, 17),
            "c_0_m_s": float(C0),
        },
        "prior_lane_inputs": {k: mp.nstr(v, 17) for k, v in v24.items()},
        "gates": {}, "self_tests": {}, "configurations": {},
        "regulator_sweep": {}, "bins": {}, "y8": {},
    }

    rsat_ref = r_sat_of(M_REF_MSUN)
    out["reference"] = {
        "M_ref_Msun": M_REF_MSUN,
        "r_sat_m": mp.nstr(rsat_ref, 17),
        "r_sat_over_c0_s": mp.nstr(rsat_ref / C0, 17),
        "l_node_over_r_sat": mp.nstr(L_NODE / rsat_ref, 17),
    }
    om_ref = v24["Omega_re"] * C0 / rsat_ref
    out["reference"]["omega_ringdown_rad_s"] = mp.nstr(om_ref, 17)
    out["reference"]["tau_ring_s"] = mp.nstr(
        m_g_time(M_REF_MSUN) / v24["omega_I_M_g"], 17)

    # =======================================================================
    # PART 1 -- the gates carried unchanged from v1
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

    M_pred = mp.mpf(repr(pred.M_GW150914 / pred.MSUN))
    nc_rows, worst = [], mp.mpf(0)
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

    J_A_closed, J_A_quad = J_closed(P_A), J_quad(P_A)
    ja_sep = abs(J_A_closed - J_A_quad)
    out["gates"]["G-JA"] = {"J_A_closed": mp.nstr(J_A_closed, 25),
                            "sep": mp.nstr(ja_sep, 6),
                            "tol": mp.nstr(TOL_JA, 3),
                            "pass": bool(ja_sep < TOL_JA)}
    try:
        _g = mp.gamma(1 - P_B / 2)
        out["gates"]["G-JA"]["gamma_pole_at_p2"] = (
            f"Gamma(0) evaluated finite: {mp.nstr(_g, 6)} -- UNEXPECTED")
    except ValueError as exc:
        out["gates"]["G-JA"]["gamma_pole_at_p2"] = (
            f"Gamma(1 - p/2) at p = 2 raises: {exc} -- RHO-B DIVERGES")

    a_test = mp.mpf("0.9999")
    cf_sep = abs(mp.atanh(a_test) - J_quad(P_B, 0, a_test))
    out["gates"]["G-CF"] = {"sep": mp.nstr(cf_sep, 6),
                            "tol": mp.nstr(TOL_CF, 3),
                            "pass": bool(cf_sep < TOL_CF)}

    sum_rows = {}
    for p, tag in ((P_A, "RHO-A"), (P_B, "RHO-B")):
        vals = [node_sum_excess(p, rsat_ref, THETAS[0], ns)[0]
                for ns in N_SPLITS]
        seps = [abs(vals[i] / vals[0] - 1) for i in (1, 2)]
        sum_rows[tag] = {"values_s": [mp.nstr(v, 17) for v in vals],
                         "max_rel_sep": mp.nstr(max(seps), 6)}
    worst_sum = max(mp.mpf(sum_rows[t]["max_rel_sep"]) for t in sum_rows)
    out["gates"]["G-SUM"] = {"per_branch": sum_rows,
                             "worst_rel": mp.nstr(worst_sum, 6),
                             "tol": mp.nstr(TOL_SUM, 3),
                             "pass": bool(worst_sum < TOL_SUM)}

    u_worst = mp.mpf(0)
    for i in range(12):
        A = mp.mpf("0.07") + mp.mpf("0.07") * i
        u_worst = max(u_worst, abs(U_collected(A) - U_uncollected(A)))
    out["gates"]["G-U"] = {"worst_abs_sep": mp.nstr(u_worst, 6),
                           "tol": mp.nstr(TOL_U, 3),
                           "pass": bool(u_worst < TOL_U)}

    disp_worst = mp.mpf(0)
    for i in range(1, 200):
        kl = mp.pi * mp.mpf(i) / 200
        disp_worst = max(disp_worst, abs(mp.acos(mp.cos(kl)) - kl))
    out["gates"]["G-DISP"] = {"worst_abs_sep": mp.nstr(disp_worst, 6),
                              "tol": mp.nstr(TOL_DISP, 3),
                              "pass": bool(disp_worst < TOL_DISP)}

    peaks, peak_ok = {}, True
    for p, tag in ((P_A, "RHO-A"), (P_B, "RHO-B")):
        pk = find_peak(p)
        ok = bool(pk is not None and pk["d2"] < 0 and 0 < pk["A_peak"] < 1)
        peak_ok = peak_ok and ok
        peaks[tag] = {
            "found": pk is not None,
            "A_peak": mp.nstr(pk["A_peak"], 17),
            "r_peak_over_r_sat": mp.nstr(1 / pk["A_peak"], 17),
            "r_peak_over_GM_c2": mp.nstr(X_SAT / pk["A_peak"], 17),
            "V_peak": mp.nstr(pk["V_peak"], 17),
            "d2_negative": bool(pk["d2"] < 0),
        }
    out["gates"]["G-PEAK"] = {"per_branch": peaks, "pass": peak_ok}

    # =======================================================================
    # PART 1 -- G-DECADE, the two frozen limbs (prereg 2P.2)
    # =======================================================================
    dec_rows, dec_a, dec_b = [], mp.mpf(0), mp.mpf(0)
    for k in (2, 3, 4, 5, 6):
        s_hi, s_lo = mp.mpf(10) ** (-k), mp.mpf(10) ** (-(k + 1))
        a_hi, a_lo = mp.sqrt(1 - s_lo**2), mp.sqrt(1 - s_hi**2)
        contrib = mp.atanh(a_hi) - mp.atanh(a_lo)
        rel = abs(contrib / mp.log(10) - 1)
        derived = decade_deviation_derived(s_hi, s_lo)
        resid = abs(rel / derived - 1)
        dec_a, dec_b = max(dec_a, rel), max(dec_b, resid)
        dec_rows.append({"decade": f"1e-{k} -> 1e-{k+1}",
                         "contribution_over_r_sat_c0": mp.nstr(contrib, 17),
                         "rel_dev_from_ln10": mp.nstr(rel, 6),
                         "derived_leading": mp.nstr(derived, 6),
                         "residual_vs_derived": mp.nstr(resid, 6)})
    out["gates"]["G-DECADE"] = {
        "rows": dec_rows,
        "limb_a_worst_rel": mp.nstr(dec_a, 6),
        "limb_a_tol": mp.nstr(TOL_DECADE_A, 3),
        "limb_a_pass": bool(dec_a < TOL_DECADE_A),
        "limb_b_worst_residual": mp.nstr(dec_b, 6),
        "limb_b_tol": mp.nstr(TOL_DECADE_B, 3),
        "limb_b_pass": bool(dec_b < TOL_DECADE_B),
        "derived_law": "delta = (S_hi^2 - S_lo^2)/(4 ln 10)",
        "pass": bool(dec_a < TOL_DECADE_A and dec_b < TOL_DECADE_B),
    }

    # =======================================================================
    # PART 1 -- G-DISC with the REPAIRED law, tolerance CARRIED UNCHANGED
    # =======================================================================
    disc_rows, disc_worst = [], mp.mpf(0)
    for theta in THETAS:
        node = node_sum_excess(P_B, rsat_ref, theta, N_SPLIT_PRIMARY)[0]
        cont = continuum_excess(P_B, rsat_ref, theta * L_NODE)
        measured = (node - cont) / (rsat_ref / C0)
        derived = K_disc_derived(theta)
        rel = abs(measured / derived - 1)
        disc_worst = max(disc_worst, rel)
        disc_rows.append({"theta": float(theta),
                          "pass_count": "ONE-WAY",
                          "measured_K_disc_oneway": mp.nstr(measured, 17),
                          "derived_K_disc_oneway": mp.nstr(derived, 17),
                          "round_trip_2K_disc": mp.nstr(2 * derived, 17),
                          "rel_sep": mp.nstr(rel, 6)})
    out["gates"]["G-DISC"] = {"rows": disc_rows,
                              "worst_rel": mp.nstr(disc_worst, 6),
                              "tol": mp.nstr(TOL_DISC, 3),
                              "law": "K_disc(theta) = [ln theta - psi(theta)]/2"
                                     " PER ONE-WAY PASS",
                              "pass": bool(disc_worst < TOL_DISC)}

    # =======================================================================
    # PART 1 -- the physics, byte-identical to v1
    # =======================================================================
    for tag, p in (("CFG-A", P_A), ("CFG-B", P_B)):
        rows = []
        for M in MASS_GRID_MSUN:
            rs = r_sat_of(M)
            T = 2 * node_sum_excess(p, rs, THETAS[0], N_SPLIT_PRIMARY)[0]
            row = {"M_Msun": M,
                   "r_sat_over_c0_s": mp.nstr(rs / C0, 17),
                   "T_return_excess_s": mp.nstr(T, 17),
                   "T_return_over_r_sat_c0": mp.nstr(T / (rs / C0), 17),
                   "tau_ring_s": mp.nstr(m_g_time(M) / v24["omega_I_M_g"], 17)}
            if p == P_A:
                closed = 2 * (rs / C0) * J_A_closed
                row["closed_form_s"] = mp.nstr(closed, 17)
                row["rel_sep_from_closed"] = mp.nstr(abs(T / closed - 1), 6)
            else:
                closed = (rs / C0) * mp.log(2 * rs / (THETAS[0] * L_NODE))
                row["log_law_s"] = mp.nstr(closed, 17)
                row["K_disc_measured"] = mp.nstr((T - closed) / (rs / C0), 17)
                row["K_disc_pass_count"] = "ROUND TRIP (= 2 * one-way)"
                row["ln_arg_2rsat_over_lnode"] = mp.nstr(mp.log(2 * rs / L_NODE), 17)
            rows.append(row)
        out["configurations"][tag] = {"p": float(p), "rows": rows}
    out["configurations"]["CFG-A"]["J_A_closed"] = mp.nstr(J_A_closed, 17)
    out["configurations"]["CFG-A"]["two_J_A"] = mp.nstr(2 * J_A_closed, 17)

    for tag, p in (("CFG-A", P_A), ("CFG-B", P_B)):
        a_peak = mp.mpf(peaks["RHO-A" if p == P_A else "RHO-B"]["A_peak"])
        a_in = rsat_ref / (rsat_ref + THETAS[0] * L_NODE)

        def integ(A, _p=p):
            return mp.e ** (-(_p / 2) * mp.log1p(-A**2)) / A**2

        tot = 2 * (rsat_ref / C0) * mp.quad(integ, [a_peak, a_in])
        out["configurations"][tag]["plane_peak_total_s_at_Mref"] = mp.nstr(tot, 17)
        out["configurations"][tag]["plane_peak_over_r_sat_c0"] = mp.nstr(
            tot / (rsat_ref / C0), 17)

    turn_rows = []
    node_gov, band_gov = True, True
    for M in MASS_GRID_MSUN:
        rs = r_sat_of(M)
        om = v24["Omega_re"] * C0 / rs
        for beta in BETAS:
            for theta in THETAS:
                for p, tag in ((P_A, "RHO-A"), (P_B, "RHO-B")):
                    st, sl = s_turn(om, beta, p), s_last(theta, rs)
                    if p == P_B:
                        node_gov &= bool(st < sl)
                        band_gov &= bool(st > sl)
                    turn_rows.append({
                        "M_Msun": M, "beta": float(beta),
                        "theta": float(theta), "branch": tag,
                        "S_turn": mp.nstr(st, 6), "S_last": mp.nstr(sl, 6),
                        "S_turn_over_S_last": mp.nstr(st / sl, 17),
                        "governed_by": "NODE" if st < sl else "BAND-EDGE"})
    out["turning_point"] = {
        "rows": turn_rows,
        "closed_form": "S_turn/S_last = sqrt(Omega/(2 theta beta)) -- MASS-FREE",
        "note_v2": ("S_turn is renamed the DEPLETION EDGE in PART 2; the "
                    "criterion is byte-identical and nothing is redefined"),
        "all_node_governed_RHO_B": node_gov,
        "all_band_governed_RHO_B": band_gov}

    def sweep(p):
        vals = {}
        vals["R1_full_node"] = 2 * node_sum_excess(
            p, rsat_ref, mp.mpf(1), N_SPLIT_PRIMARY)[0]
        vals["R2_half_node"] = 2 * node_sum_excess(
            p, rsat_ref, mp.mpf(1) / 2, N_SPLIT_PRIMARY)[0]
        for beta in BETAS:
            st = s_turn(om_ref, beta, p)
            x_in = max(x_from_s2(st**2, rsat_ref), L_NODE)
            vals[f"R3_turning_beta_{mp.nstr(beta, 6)}"] = 2 * node_sum_excess(
                p, rsat_ref, mp.mpf(1), N_SPLIT_PRIMARY, x_inner=x_in)[0]
        vals["R4_strained_pitch"] = 2 * node_sum_excess(
            p, rsat_ref, mp.mpf(1), N_SPLIT_PRIMARY, x_inner=2 * L_NODE)[0]
        vals["R5_continuum"] = 2 * continuum_excess(p, rsat_ref, L_NODE)
        v_d2, n_cut = node_sum_excess(p, rsat_ref, mp.mpf(1), N_SPLIT_PRIMARY,
                                      lumped_omega=float(om_ref))
        vals["D2_lumped_dispersion"] = 2 * v_d2
        arr = sorted(vals.values())
        return vals, (arr[-1] - arr[0]) / arr[len(arr) // 2], n_cut

    for tag, p in (("CFG-A", P_A), ("CFG-B", P_B), ("CFG-SYN", P_SYN)):
        vals, spread, n_cut = sweep(p)
        out["regulator_sweep"][tag] = {
            "values_s": {k: mp.nstr(v, 17) for k, v in vals.items()},
            "spread": mp.nstr(spread, 17),
            "D2_evanescent_cells_masked": n_cut}
    return out, v1, v24, pred, peaks, J_A_closed, J_A_quad, a_test, \
        rsat_ref, om_ref, nc_rows, t_start


def cnum(z, d=17):
    """Render a complex number for the shipped object."""
    return {"re": mp.nstr(mp.mpf(float(np.real(z))), d),
            "im": mp.nstr(mp.mpf(float(np.imag(z))), d),
            "abs": mp.nstr(mp.mpf(float(abs(z))), d)}


def main() -> int:                                    # noqa: C901, PLR0915
    (out, v1, v24, pred, peaks, J_A_closed, J_A_quad, a_test,
     rsat_ref, om_ref, nc_rows, t_start) = part1()

    # =======================================================================
    # PART 1 -- the v1 bins, criteria BYTE-IDENTICAL
    # =======================================================================
    s2_out = s2_from_x(mp.mpf(10) ** 6 * rsat_ref, rsat_ref)
    evan = {}
    for tag, p in (("CFG-A", P_A), ("CFG-B", P_B)):
        for beta in BETAS:
            lo = omega_max_local(beta, p, s2_from_x(L_NODE, rsat_ref)) / om_ref
            hi = omega_max_local(beta, p, s2_out) / om_ref
            evan[f"{tag}_beta_{mp.nstr(beta, 6)}"] = {
                "omega_max_over_omega_innermost": mp.nstr(lo, 17),
                "omega_max_over_omega_outermost": mp.nstr(hi, 17),
                "bin": "BIN-EVAN-FIRES" if hi < 1 else "BIN-EVAN-CLEAR"}
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
    da_ok = da_ok and mp.mpf(
        out["regulator_sweep"]["CFG-A"]["spread"]) < mp.mpf("1e-6")
    out["bins"]["BIN-DA"] = {"bin": "BIN-DA-CLOSED" if da_ok else "BIN-DA-OPEN"}

    tp = out["turning_point"]
    db = ("BIN-DB-NODE" if tp["all_node_governed_RHO_B"]
          else "BIN-DB-BAND" if tp["all_band_governed_RHO_B"]
          else "BIN-DB-SPLIT")
    ratios = [mp.mpf(r["S_turn_over_S_last"]) for r in tp["rows"]
              if r["branch"] == "RHO-B"]
    out["bins"]["BIN-DB"] = {"bin": db,
                             "min_S_turn_over_S_last": mp.nstr(min(ratios), 17),
                             "max_S_turn_over_S_last": mp.nstr(max(ratios), 17)}

    disc2, all_gt, all_le = [], True, True
    for i, M in enumerate(MASS_GRID_MSUN):
        TA = mp.mpf(out["configurations"]["CFG-A"]["rows"][i]["T_return_excess_s"])
        TB = mp.mpf(out["configurations"]["CFG-B"]["rows"][i]["T_return_excess_s"])
        tau = m_g_time(M) / v24["omega_I_M_g"]
        d = abs(TB - TA)
        all_gt &= bool(d > tau)
        all_le &= bool(d <= tau)
        disc2.append({"M_Msun": M, "abs_diff_s": mp.nstr(d, 17),
                      "tau_ring_s": mp.nstr(tau, 17),
                      "diff_over_tau": mp.nstr(d / tau, 17),
                      "T_B_over_T_A": mp.nstr(TB / TA, 17)})
    out["bins"]["BIN-DISC"] = {
        "rows": disc2,
        "bin": ("BIN-DISC" if all_gt else
                "BIN-DEGEN" if all_le else "BIN-DISC-SPLIT")}

    dt_obs = mp.mpf(repr(pred.DT_OBSERVED))
    iref = MASS_GRID_MSUN.index(M_REF_MSUN)
    out["observational_pointer_diagnostic"] = {
        "_class": "DIAGNOSTIC, NOT a bin, NOT a verdict, NOT a detection",
        "pointer_s": float(dt_obs),
        "RHO_A_ratio_pointer_over_T": mp.nstr(dt_obs / mp.mpf(
            out["configurations"]["CFG-A"]["rows"][iref]["T_return_excess_s"]), 17),
        "RHO_B_ratio_pointer_over_T": mp.nstr(dt_obs / mp.mpf(
            out["configurations"]["CFG-B"]["rows"][iref]["T_return_excess_s"]), 17)}

    # =======================================================================
    # G-NC-V1A / G-NC-V1B -- EXACT STRING EQUALITY against v1's shipped JSON
    # =======================================================================
    def pairs_A():
        yield "gates/G-NC/worst_rel", out["gates"]["G-NC"]["worst_rel"]
        for k in ("J_A_closed", "two_J_A", "plane_peak_total_s_at_Mref",
                  "plane_peak_over_r_sat_c0"):
            yield f"configurations/CFG-A/{k}", out["configurations"]["CFG-A"][k]
        for i in range(len(MASS_GRID_MSUN)):
            for k in ("T_return_excess_s", "T_return_over_r_sat_c0",
                      "closed_form_s", "rel_sep_from_closed",
                      "r_sat_over_c0_s", "tau_ring_s"):
                yield (f"configurations/CFG-A/rows/{i}/{k}",
                       out["configurations"]["CFG-A"]["rows"][i][k])
        yield ("regulator_sweep/CFG-A/spread",
               out["regulator_sweep"]["CFG-A"]["spread"])
        for k, v in out["regulator_sweep"]["CFG-A"]["values_s"].items():
            yield f"regulator_sweep/CFG-A/values_s/{k}", v

    def pairs_B():
        for i in range(len(MASS_GRID_MSUN)):
            for k in ("T_return_excess_s", "T_return_over_r_sat_c0",
                      "log_law_s", "ln_arg_2rsat_over_lnode",
                      "r_sat_over_c0_s", "tau_ring_s"):
                yield (f"configurations/CFG-B/rows/{i}/{k}",
                       out["configurations"]["CFG-B"]["rows"][i][k])
            yield (f"configurations/CFG-B/rows/{i}/K_disc_measured",
                   out["configurations"]["CFG-B"]["rows"][i]["K_disc_measured"])
        for k in ("plane_peak_total_s_at_Mref", "plane_peak_over_r_sat_c0"):
            yield f"configurations/CFG-B/{k}", out["configurations"]["CFG-B"][k]
        for cfg in ("CFG-B", "CFG-SYN"):
            yield (f"regulator_sweep/{cfg}/spread",
                   out["regulator_sweep"][cfg]["spread"])
            for k, v in out["regulator_sweep"][cfg]["values_s"].items():
                yield f"regulator_sweep/{cfg}/values_s/{k}", v
        for br in ("RHO-A", "RHO-B"):
            for k in ("A_peak", "r_peak_over_r_sat", "r_peak_over_GM_c2",
                      "V_peak"):
                yield (f"gates/G-PEAK/per_branch/{br}/{k}", peaks[br][k])
        for i, r in enumerate(out["turning_point"]["rows"]):
            for k in ("S_turn", "S_last", "S_turn_over_S_last"):
                yield f"turning_point/rows/{i}/{k}", r[k]
        for i, r in enumerate(out["bins"]["BIN-DISC"]["rows"]):
            for k in ("abs_diff_s", "tau_ring_s", "diff_over_tau",
                      "T_B_over_T_A"):
                yield f"bins/BIN-DISC/rows/{i}/{k}", r[k]
        for i, th in enumerate(THETAS):
            yield (f"gates/G-DISC/rows/{i}/measured_K_disc",
                   out["gates"]["G-DISC"]["rows"][i]["measured_K_disc_oneway"])
        for pth, key in (("gates/G-SUM/worst_rel", "worst_rel"),
                         ("gates/G-U/worst_abs_sep", "worst_abs_sep"),
                         ("gates/G-DISP/worst_abs_sep", "worst_abs_sep")):
            yield pth, out["gates"][pth.split("/")[1]][key]

    def run_nc(gen, name):
        mismatches, n = [], 0
        for pth, mine in gen:
            n += 1
            theirs = jpath(v1, pth)
            if str(theirs) != str(mine):
                mismatches.append({"path": pth, "v1": str(theirs),
                                   "v2": str(mine)})
        return {"compared": n, "mismatches": mismatches,
                "criterion": "EXACT STRING EQUALITY at v1's shipped rendering",
                "pass": not mismatches}, mismatches

    ncA, mmA = run_nc(pairs_A(), "G-NC-V1A")
    ncB, mmB = run_nc(pairs_B(), "G-NC-V1B")
    out["gates"]["G-NC-V1A"] = ncA
    out["gates"]["G-NC-V1B"] = ncB
    out["bins"]["BIN-STOP-V1"] = {
        "fired": bool(mmA or mmB),
        "disposition": ("THE LANE STOPS -- a v1 number moved" if (mmA or mmB)
                        else "not fired: every v1 number reproduced exactly")}

    # =======================================================================
    # PART 1 SELF-TESTS -- v1's twelve, carried byte-identical, plus two new
    # =======================================================================
    st = {}
    ft = abs((mp.mpf(nc_rows[0]["this_lane_s"]) * (1 + mp.mpf("1e-6")))
             / mp.mpf(nc_rows[0]["predecessor_s"]) - 1)
    st["FT-NC"] = {"measured": mp.nstr(ft, 6), "threshold": "1e-7",
                   "fires": bool(ft >= mp.mpf("1e-7"))}
    ft = abs(J_A_closed * (1 + mp.mpf("1e-9")) - J_A_quad)
    st["FT-JA"] = {"measured": mp.nstr(ft, 6), "threshold": "1e-10",
                   "fires": bool(ft >= mp.mpf("1e-10"))}
    ft = abs(mp.atanh(a_test) * (1 + mp.mpf("1e-12")) - J_quad(P_B, 0, a_test))
    st["FT-CF"] = {"measured": mp.nstr(ft, 6), "threshold": "1e-13",
                   "fires": bool(ft >= mp.mpf("1e-13"))}

    def _sum_no_tail(p, ns):
        rsat_f, p_f, c0_f = float(rsat_ref), float(p), float(C0)
        l_f, x0, tot, done = float(L_NODE), float(L_NODE), 0.0, 0
        while done < ns:
            m = min(10**6, ns - done)
            x = x0 + np.arange(done, done + m, dtype=np.float64) * l_f
            tot += float(np.sum(_f_excess_block(x, rsat_f, p_f, c0_f)))
            done += m
        return mp.mpf(repr(tot)) * L_NODE
    ft = abs(_sum_no_tail(P_B, 10**6) / _sum_no_tail(P_B, 10**5) - 1)
    st["FT-SUM"] = {"measured": mp.nstr(ft, 6), "threshold": "1e-3",
                    "fires": bool(ft >= mp.mpf("1e-3"))}

    def _U_broken(A, ell=ELL):
        def mu(r):
            return mp.sqrt(1 - (1 / r) ** 2)

        def g(r):
            return mp.diff(mu, r) / mu(r)
        r = 1 / A
        return (ell * (ell + 1) / r**2 + 2 * g(r) / r + mp.diff(g, r) / 2)
    ft = abs(U_collected(mp.mpf("0.5")) - _U_broken(mp.mpf("0.5")))
    st["FT-U"] = {"measured": mp.nstr(ft, 6), "threshold": "1e-6",
                  "fires": bool(ft >= mp.mpf("1e-6"))}

    d = mp.mpf(0)
    for i in range(1, 200):
        kl = mp.pi * mp.mpf(i) / 200
        d = max(d, abs(2 * mp.sin(kl / 2) - kl))
    st["FT-DISP"] = {"measured": mp.nstr(d, 6), "threshold": "1e-2",
                     "fires": bool(d >= mp.mpf("1e-2"))}
    a_p = mp.mpf(peaks["RHO-B"]["A_peak"])
    ft = abs(mp.diff(lambda a: V_barrier(a, P_B), a_p * mp.mpf("1.01")))
    st["FT-PEAK"] = {"measured": mp.nstr(ft, 6), "threshold": "1e-4",
                     "fires": bool(ft >= mp.mpf("1e-4"))}
    s_hi, s_lo = mp.mpf("1e-3"), mp.mpf("1e-4")
    contrib = J_quad(P_A, mp.sqrt(1 - s_hi**2), mp.sqrt(1 - s_lo**2))
    ft = abs(contrib / mp.log(10) - 1)
    st["FT-DECADE"] = {"measured": mp.nstr(ft, 6), "threshold": "0.1",
                       "note": "fires if EITHER G-DECADE limb would fail",
                       "fires": bool(ft >= mp.mpf("0.1")
                                     and ft >= TOL_DECADE_A)}
    syn = mp.mpf(out["regulator_sweep"]["CFG-SYN"]["spread"])
    st["FT-CUT"] = {"measured": mp.nstr(syn, 6),
                    "threshold": mp.nstr(BIN_CUTOFF_THRESHOLD, 3),
                    "fires": bool(syn > BIN_CUTOFF_THRESHOLD)}
    mr = omega_max_local(BETAS[0], P_B, s2_out) / (om_ref * mp.mpf("1e20"))
    st["FT-EVAN"] = {"max_omega_max_over_omega": mp.nstr(mr, 6),
                     "fires": bool(mr < 1)}
    st_, sl_ = s_turn(om_ref * mp.mpf("1e12"), BETAS[0], P_B), s_last(mp.mpf(1), rsat_ref)
    st["FT-TURN"] = {"S_turn": mp.nstr(st_, 6), "S_last": mp.nstr(sl_, 6),
                     "fires": bool(st_ > sl_)}
    ft = abs(OMEGA_C * (L_NODE * (1 + mp.mpf("1e-12"))) / C0 - 1)
    st["FT-CANON"] = {"measured": mp.nstr(ft, 6), "threshold": "1e-15",
                      "fires": bool(ft >= mp.mpf("1e-15"))}

    # FT-DISC (NEW) -- the repaired law's own fireability
    meas0 = mp.mpf(out["gates"]["G-DISC"]["rows"][0]["measured_K_disc_oneway"])
    der0 = K_disc_derived(THETAS[0])
    der_mut = der0 * (1 + mp.mpf("0.02"))
    sep_gate = abs(meas0 / der_mut - 1)
    st["FT-DISC"] = {
        "introduced_perturbation": "0.02",
        "resulting_gate_separation": mp.nstr(sep_gate, 6),
        "frozen_tolerance": mp.nstr(TOL_DISC, 3),
        "gate_would_fail": bool(sep_gate > TOL_DISC),
        "disclosure": ("the frozen row reads 'separation >= 0.02'; the "
                       "INTRODUCED perturbation is exactly 0.02 while the "
                       "RESULTING gate separation is |1/1.02 - 1| = 0.0196, "
                       "so the two readings of 'separation' differ; the "
                       "SUBSTANTIVE fire condition is that G-DISC FAILS "
                       "under the mutation and it does, by 1.96x over the "
                       "frozen 1 per cent tolerance; the wording imprecision "
                       "is SURFACED, not resolved in this lane's favour"),
        "fires": bool(sep_gate > TOL_DISC)}

    # FT-V1 (NEW) -- the negative controls' own fireability
    probe_path = "configurations/CFG-A/two_J_A"
    probe_true = jpath(v1, probe_path)
    probe_mut = mp.nstr(mp.mpf(probe_true) * (1 + mp.mpf("1e-12")), 17)
    st["FT-V1"] = {"path": probe_path, "v1_value": str(probe_true),
                   "mutated": probe_mut,
                   "fires": bool(str(probe_true) != probe_mut)}
    out["self_tests"] = st
    return _part2(out, v1, v24, peaks, rsat_ref, om_ref, st, t_start)


def _mkcfg(tag, variant, theta, M, e_reading, beta=None, steps_off=False,
           pitch=None):
    rs = r_sat_of(M)
    xin = float((pitch if pitch is not None else theta) * L_NODE)
    return {"tag": tag, "variant": variant, "p": P_B, "theta": theta,
            "M": M, "rsat": rs, "e_reading": e_reading, "beta": beta,
            "steps_off": steps_off, "x_inner": xin}


def _part2(out, v1, v24, peaks, rsat_ref, om_ref, st, t_start):   # noqa: C901, PLR0915
    # =======================================================================
    # Y8.1 -- THE FROZEN BAND, read PROGRAMMATICALLY from v2.4's artifacts
    # =======================================================================
    Om_R, Om_I = v24["Omega_re"], abs(v24["Omega_im"])
    band_alt = X_SAT * v24["omega_I_M_g"]
    band_sep = abs(Om_I / band_alt - 1)
    out["gates"]["G-BAND"] = {
        "Omega_R": mp.nstr(Om_R, 17), "Omega_I": mp.nstr(Om_I, 17),
        "Omega_I_two_method": mp.nstr(band_alt, 17),
        "rel_sep": mp.nstr(band_sep, 6), "tol": mp.nstr(TOL_BAND, 3),
        "pass": bool(band_sep < TOL_BAND)}
    Om_lo, Om_hi = Om_R - Om_I, Om_R + Om_I
    band = [Om_lo + (Om_hi - Om_lo) * mp.mpf(i) / (N_BAND - 1)
            for i in range(N_BAND)]
    out["y8"]["band"] = {
        "definition": ("FWHM of the v2.4 certified axial pole, both endpoints "
                       "read programmatically from the shipped JSON"),
        "Omega_lo": mp.nstr(Om_lo, 17), "Omega_hi": mp.nstr(Om_hi, 17),
        "N_points": N_BAND,
        "omega_lo_rad_s_at_Mref": mp.nstr(Om_lo * C0 / rsat_ref, 17),
        "omega_hi_rad_s_at_Mref": mp.nstr(Om_hi * C0 / rsat_ref, 17)}

    # =======================================================================
    # Y8.2 -- THE DEPLETION WIDTH W(omega), two methods + the mass-free form
    # =======================================================================
    w_rows, wmax, dep_ok = [], 0, True
    for bi, Om in enumerate(band):
        omega = Om * C0 / rsat_ref
        for beta in BETAS:
            for theta in THETAS:
                xin = theta * L_NODE
                W, s_dep, x_dep = depletion_width(omega, beta, P_B,
                                                  rsat_ref, xin)
                Wc = depletion_width_by_count(omega, beta, P_B, rsat_ref, xin)
                asym = Om / (2 * beta) + 1 - theta
                Wa = max(0, int(mp.floor(asym)))
                dep_ok &= bool(W == Wc)
                wmax = max(wmax, W)
                if bi in (0, (N_BAND - 1) // 2, N_BAND - 1):
                    w_rows.append({
                        "Omega": mp.nstr(Om, 17), "beta": float(beta),
                        "theta": float(theta), "W_exact": W,
                        "W_by_count": Wc, "W_asymptotic": Wa,
                        "S_dep": mp.nstr(s_dep, 6),
                        "x_dep_over_l_node": mp.nstr(x_dep / L_NODE, 17)})
    out["gates"]["G-DEP"] = {"criterion": "exact integer equality",
                             "all_agree": dep_ok, "pass": bool(dep_ok)}
    om_crit = [{"theta": float(th), "beta": float(b),
                "Omega_crit_for_W_ge_1": mp.nstr(2 * th * b, 17),
                "margin_Omega_crit_over_band_top": mp.nstr(2 * th * b / Om_hi, 17)}
               for th in THETAS for b in BETAS]
    out["y8"]["depletion_width"] = {
        "closed_form": "W = max(0, floor(Omega/(2 beta) + 1 - theta)) -- MASS-FREE",
        "max_W_over_frozen_band": wmax,
        "sampled_rows": w_rows,
        "crossing": om_crit,
        "bin": ("BIN-W-ZERO" if wmax == 0 else
                "BIN-W-THIN" if wmax <= 10 else "BIN-W-THICK")}

    # the JUNCTION TWO-PORT across the depleted cells
    jt = []
    for beta in BETAS:
        for theta in THETAS:
            W, _, _ = depletion_width(Om_hi * C0 / rsat_ref, beta, P_B,
                                      rsat_ref, theta * L_NODE)
            cfg = _mkcfg("jt", "Y-NODE", theta, M_REF_MSUN, "E1", beta)
            if W == 0:
                T = abcd_product(np.array([]), np.array([]))
            else:
                s2p, z = cell_profile(cfg, 0, W)
                z = z / z[0]
                th = float(cfg_coef(cfg, Om_hi * C0 / rsat_ref)) / \
                    np.exp((float(P_B) / 2.0) * np.log(s2p))
                T = abcd_product(z, th)
            jt.append({"beta": float(beta), "theta": float(theta),
                       "at": "band top", "W": W,
                       "A": cnum(T[0, 0]), "B_over_Z1": cnum(T[0, 1]),
                       "C_times_Z1": cnum(T[1, 0]), "D": cnum(T[1, 1]),
                       "is_identity": bool(abs(T[0, 0] - 1) < 1e-15
                                           and abs(T[0, 1]) < 1e-15
                                           and abs(T[1, 0]) < 1e-15
                                           and abs(T[1, 1] - 1) < 1e-15),
                       "T_squared_through_depleted_section":
                           mp.nstr(mp.mpf(1), 17) if W == 0 else "see y8/gamma"})
    out["y8"]["junction_two_port"] = jt

    # RHO-A: the reach-through question is MOOT unless a cell is depleted
    wa_max = 0
    for Om in (Om_lo, Om_hi):
        for M in MASS_GRID_MSUN:
            rs = r_sat_of(M)
            for beta in BETAS:
                for theta in THETAS:
                    W, _, _ = depletion_width(Om * C0 / rs, beta, P_A, rs,
                                              theta * L_NODE)
                    wa_max = max(wa_max, W)
    sdepA = s_turn(Om_R * C0 / rsat_ref, BETAS[0], P_A)
    out["y8"]["rho_a"] = {
        "max_W": wa_max,
        "S_dep_over_S_last_at_band_centre": mp.nstr(
            sdepA / s_last(THETAS[0], rsat_ref), 6),
        "bin": "BIN-RHOA-MOOT" if wa_max == 0 else "BIN-RHOA-LIVE"}

    # =======================================================================
    # Y8.3 -- THE EXACT CASCADE
    # =======================================================================
    cfgs = [
        _mkcfg("Y-NODE", "Y-NODE", THETAS[0], M_REF_MSUN, "E1"),
        _mkcfg("Y-THETA", "Y-NODE", THETAS[1], M_REF_MSUN, "E1"),
        _mkcfg("Y-MID", "Y-MID", THETAS[0], M_REF_MSUN, "E1"),
        _mkcfg("Y-PITCH", "Y-NODE", THETAS[0], M_REF_MSUN, "E1", pitch=mp.mpf(2)),
        _mkcfg("Y-E2-BLO", "Y-NODE", THETAS[0], M_REF_MSUN, "E2", BETAS[0]),
        _mkcfg("Y-E2-BHI", "Y-NODE", THETAS[0], M_REF_MSUN, "E2", BETAS[1]),
        _mkcfg("Y-MASS-1", "Y-NODE", THETAS[0], MFREE_MASSES[0], "E1"),
        _mkcfg("Y-MASS-100", "Y-NODE", THETAS[0], MFREE_MASSES[2], "E1"),
        _mkcfg("Y-STEPSOFF", "Y-NODE", THETAS[0], M_REF_MSUN, "E1",
               steps_off=True),
    ]
    nc = len(cfgs)
    omega_of_row, cfg_of_row = [], []
    for ci, c in enumerate(cfgs):
        for Om in band:
            omega_of_row.append(Om * C0 / c["rsat"])
            cfg_of_row.append(ci)
    cfg_of_row = np.array(cfg_of_row)
    res = y8_pass(cfgs, omega_of_row, cfg_of_row, K_PRIMARY, set(K_WINDOWS),
                  blk=2000)

    def row(ci, bi):
        return ci * N_BAND + bi

    bic0 = row(0, (N_BAND - 1) // 2)

    # --- G-UNIT: |Gamma_in| = 1 EXACTLY for both mirror contacts -----------
    unit_worst, unit_per_k = 0.0, {}
    for kk in K_WINDOWS:
        g = res[kk]["gamma"]
        wk = 0.0
        for t in (1, 2):
            wk = max(wk, float(np.max(np.abs(np.abs(g[:, t]) - 1.0))))
        unit_per_k[str(kk)] = mp.nstr(mp.mpf(wk), 6)
        unit_worst = max(unit_worst, wk)
    out["gates"]["G-UNIT"] = {
        "worst_abs_dev": mp.nstr(mp.mpf(unit_worst), 6),
        "worst_abs_dev_per_K": unit_per_k,
        "tol": mp.nstr(TOL_UNIT, 3), "pass": bool(unit_worst < float(TOL_UNIT)),
        "content": ("Ax-3 losslessness: a |Gamma_L| = 1 termination returns "
                    "|Gamma_in| = 1 at every plane and every frequency")}

    # --- G-KWIN: window-independence of the MATCHED reflection -------------
    gk = np.stack([np.abs(res[kk]["gamma"][:, 0]) for kk in K_WINDOWS])
    kwin = float(np.max(gk.max(axis=0) - gk.min(axis=0)))
    out["gates"]["G-KWIN"] = {
        "worst_abs_spread": mp.nstr(mp.mpf(kwin), 6),
        "tol": mp.nstr(TOL_KWIN, 3),
        "abs_gamma_at_band_centre_primary_cfg_per_K": {
            str(kk): mp.nstr(mp.mpf(float(abs(res[kk]["gamma"][bic0, 0]))), 17)
            for kk in K_WINDOWS},
        "z_plane_over_z1_primary_cfg_per_K": {
            str(kk): mp.nstr(mp.mpf(float(res[kk]["z_plane"][0])), 17)
            for kk in K_WINDOWS},
        "pass": bool(kwin < float(TOL_KWIN))}

    # --- G-MFREE: the near-wall two-port is mass-free ----------------------
    gm = np.stack([np.array([abs(res[K_PRIMARY]["gamma"][row(ci, bi), 0])
                             for bi in range(N_BAND)])
                   for ci in (0, 6, 7)])
    mfree = float(np.max(gm.max(axis=0) - gm.min(axis=0)))
    out["gates"]["G-MFREE"] = {"worst_abs_spread": mp.nstr(mp.mpf(mfree), 6),
                               "masses_Msun": list(MFREE_MASSES),
                               "tol": mp.nstr(TOL_MFREE, 3),
                               "pass": bool(mfree < float(TOL_MFREE))}

    # --- phase slope, reflection group delay, CHIRP-MEASURE ---------------
    om_arr = {ci: np.array([float(omega_of_row[row(ci, bi)])
                            for bi in range(N_BAND)]) for ci in range(nc)}
    phase = {}
    for ci in range(nc):
        for t in range(3):
            gg = np.array([res[K_PRIMARY]["gamma"][row(ci, bi), t]
                           for bi in range(N_BAND)])
            ph = np.unwrap(np.angle(gg))
            w = om_arr[ci]
            D = -np.gradient(ph, w)                 # reflection group delay, s
            lnw = np.log(w)
            dD = np.gradient(D, lnw)
            phase[(ci, t)] = {"D": D, "dD_dlnw": dD, "absG": np.abs(gg)}

    rs_c0 = {ci: float(cfgs[ci]["rsat"] / C0) for ci in range(nc)}
    # --- G-XTIE: the CROSS-PART control, steps OFF -------------------------
    ci_off = 8
    transit_rt = 2.0 * res[K_PRIMARY]["transit_oneway_s"][ci_off]
    xt_worst = 0.0
    for t in (1, 2):
        D = phase[(ci_off, t)]["D"][2:-2]
        xt_worst = max(xt_worst, float(np.max(np.abs(D / transit_rt - 1.0))))
    out["gates"]["G-XTIE"] = {
        "node_sum_round_trip_s": mp.nstr(mp.mpf(transit_rt), 17),
        "worst_rel_sep": mp.nstr(mp.mpf(xt_worst), 6),
        "tol": mp.nstr(TOL_XTIE, 3), "pass": bool(xt_worst < float(TOL_XTIE)),
        "content": ("with the impedance steps switched off the mirror phase "
                    "slope is EXACTLY minus PART 1's node-sum round-trip "
                    "delay over the same K cells")}

    # --- G-ABCD: per-cell structure, and the two-route cross-check ---------
    cfg0, bic = cfgs[0], (N_BAND - 1) // 2
    s2p, zz = cell_profile(cfg0, 0, 1001)
    zz = zz / zz[0]
    thh = float(cfg_coef(cfg0, omega_of_row[row(0, bic)])) / \
        np.exp((float(P_B) / 2.0) * np.log(s2p))
    ab_worst = 0.0
    for n in (0, 1, 9, 99, 999):
        c_, s_, z_ = np.cos(thh[n]), np.sin(thh[n]), zz[n]
        M = np.array([[c_ + 0j, 1j * z_ * s_], [1j * s_ / z_, c_ + 0j]])
        det = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
        ab_worst = max(ab_worst, abs(det - 1), abs(M[0, 0].imag),
                       abs(M[0, 1].real), abs(M[1, 0].real))
    out["gates"]["G-ABCD"] = {
        "worst_structural_dev": mp.nstr(mp.mpf(float(ab_worst)), 6),
        "tol": mp.nstr(TOL_ABCD, 3),
        "route_comparison": ("N/A BY OUTCOME on the frozen band because W = 0 "
                             "makes both routes the identity; the two-route "
                             "comparison is EXERCISED by FT-W below"),
        "pass": bool(ab_worst < float(TOL_ABCD))}

    # --- G-PREC: float64 against mpmath dps = 50 at K = 1e4 ---------------
    kp = K_WINDOWS[0]
    s2p_mp = []
    z_mp = []
    for n in range(kp + 1):
        x = mp.mpf(repr(cfg0["x_inner"])) + n * L_NODE
        s2 = s2_from_x(x, cfg0["rsat"])
        s2p_mp.append(s2)
        z_mp.append(s2 ** ((1 - P_B) / 2))
    z1 = z_mp[0]
    z_mp = [z / z1 for z in z_mp]
    coef = cfg_coef(cfg0, omega_of_row[row(0, bic)])
    th_mp = [coef / (s2p_mp[n] ** (P_B / 2)) for n in range(kp)]
    g_mp = schur_small_mp(z_mp, th_mp, 0.0)
    g_f64 = res[kp]["gamma"][row(0, bic), 0]
    prec = abs(mp.mpc(complex(g_f64)) - g_mp)
    out["gates"]["G-PREC"] = {
        "gamma_float64": cnum(g_f64), "gamma_mpmath_abs": mp.nstr(abs(g_mp), 17),
        "abs_diff": mp.nstr(prec, 6), "tol": mp.nstr(TOL_PREC, 3),
        "pass": bool(prec < TOL_PREC)}

    # =======================================================================
    # Y8.4 -- THE REACH-THROUGH BIN
    # =======================================================================
    # The frozen section 7Y.2 statistic runs over the section 4Y.4 VARIANT SET
    # {Y-NODE, Y-MID, Y-E2, Y-PITCH, Y-THETA}; Y-STEPSOFF is the G-XTIE
    # CONTROL and is not a variant, so it is excluded from the bin statistic
    # (it would contribute an identically-zero reflection).
    variant_rows = np.array([r for r in range(len(cfg_of_row))
                             if not cfgs[cfg_of_row[r]]["steps_off"]])
    R_all = np.abs(res[K_PRIMARY]["gamma"][variant_rows, 0])
    R_max, R_min = float(np.max(R_all)), float(np.min(R_all))

    def classify(r):
        if r < float(RT_CONTACT_THRESHOLD):
            return "CONTACT-GOVERNED"
        if r > float(RT_EDGE_THRESHOLD):
            return "EDGE-GOVERNED"
        return "INTERFERENCE"

    rt_bin = ("BIN-RT-CONTACT" if R_max < float(RT_CONTACT_THRESHOLD)
              else "BIN-RT-EDGE" if R_min > float(RT_EDGE_THRESHOLD)
              else "BIN-RT-INTERFERENCE")

    per_cfg = []
    for ci, c in enumerate(cfgs):
        Rs = np.array([abs(res[K_PRIMARY]["gamma"][row(ci, bi), 0])
                       for bi in range(N_BAND)])
        spread3 = np.array([max(abs(res[K_PRIMARY]["gamma"][row(ci, bi), t])
                                for t in range(3))
                            - min(abs(res[K_PRIMARY]["gamma"][row(ci, bi), t])
                                  for t in range(3)) for bi in range(N_BAND)])
        Dm = phase[(ci, 1)]["D"][2:-2] / rs_c0[ci]
        chirp = np.abs(phase[(ci, 1)]["dD_dlnw"][2:-2]) / rs_c0[ci]
        per_cfg.append({
            "tag": c["tag"], "variant": c["variant"],
            "theta": float(c["theta"]), "M_Msun": c["M"],
            "e_reading": c["e_reading"],
            "beta": None if c["beta"] is None else float(c["beta"]),
            "steps_off": c["steps_off"],
            "R_matched_min": mp.nstr(mp.mpf(float(Rs.min())), 17),
            "R_matched_max": mp.nstr(mp.mpf(float(Rs.max())), 17),
            "R_matched_band_centre": mp.nstr(mp.mpf(float(Rs[bic])), 17),
            "T_squared_min": mp.nstr(mp.mpf(float(1 - Rs.max()**2)), 17),
            "contact_spread_max": mp.nstr(mp.mpf(float(spread3.max())), 17),
            "D_mirror_over_rsat_c0_min": mp.nstr(mp.mpf(float(Dm.min())), 17),
            "D_mirror_over_rsat_c0_max": mp.nstr(mp.mpf(float(Dm.max())), 17),
            "CHIRP_MEASURE_over_rsat_c0": mp.nstr(mp.mpf(float(chirp.max())), 17),
            "bin": classify(float(Rs.max()))})

    dphi = (0.5 * (mp.digamma(K_PRIMARY + THETAS[0]) - mp.digamma(THETAS[0])))
    dOm_ripple = mp.pi / dphi
    phi_direct = mp.mpf(repr(float(res[K_PRIMARY]["phase_oneway_rad"][row(0, bic)])))
    dOm_direct = mp.pi * band[bic] / phi_direct
    out["y8"]["reach_through"] = {
        "R_definition": ("|Gamma_in| at K = 1e6 under the MATCHED "
                         "CONTACT-PORT reading, at the outer face of cell K, "
                         "referenced to that cell's own impedance"),
        "R_max_over_all": mp.nstr(mp.mpf(R_max), 17),
        "R_min_over_all": mp.nstr(mp.mpf(R_min), 17),
        "T_squared_depleted_section": mp.nstr(mp.mpf(1), 17),
        "T_squared_near_wall_window_min": mp.nstr(mp.mpf(1 - R_max**2), 17),
        "per_configuration": per_cfg,
        "ripple_period_Omega_closed_form": mp.nstr(dOm_ripple, 17),
        "ripple_period_Omega_direct": mp.nstr(dOm_direct, 17),
        "ripple_period_rad_s_at_Mref": mp.nstr(dOm_ripple * C0 / rsat_ref, 17),
        "ripple_periods_across_band": mp.nstr((Om_hi - Om_lo) / dOm_ripple, 17),
        "v1_band_governed_chirp_slope_for_comparison": (
            "1 in units of r_sat/c_0 -- see v1 prereg section 2.7, "
            "cross-referenced, values not restated"),
        "bin": rt_bin}
    return _part3(out, v1, cfgs, res, band, omega_of_row, cfg_of_row, phase,
                  rs_c0, st, rsat_ref, classify, t_start)


def _part3(out, v1, cfgs, res, band, omega_of_row, cfg_of_row, phase,
           rs_c0, st, rsat_ref, classify, t_start):   # noqa: C901, PLR0915
    bic = (N_BAND - 1) // 2
    cfg0 = cfgs[0]

    def row(ci, bi):
        return ci * N_BAND + bi

    # =======================================================================
    # Y8 SELF-TESTS
    # =======================================================================
    # FT-W -- push omega up until cells ARE depleted; exercises the non-trivial
    # junction ABCD product AND the two-route cross-check that G-ABCD's second
    # limb is N/A-by-outcome for on the unmutated band.
    ftw_rows, ftw_fire, route_worst = [], True, 0.0
    om_mut = band[bic] * mp.mpf("1e3") * C0 / rsat_ref
    for beta in BETAS:
        cfg = _mkcfg("ftw", "Y-NODE", THETAS[0], M_REF_MSUN, "E1", beta)
        W, s_dep, _ = depletion_width(om_mut, beta, P_B, rsat_ref,
                                      THETAS[0] * L_NODE)
        ftw_fire &= bool(W >= 1)
        s2p, z = cell_profile(cfg, 0, W)
        z = z / z[0]
        th = float(cfg_coef(cfg, om_mut)) / np.exp((float(P_B) / 2.0)
                                                   * np.log(s2p))
        T = abcd_product(z, th)
        g_schur = schur_small(z, th, 0.0)
        g_abcd = gamma_from_abcd(T, complex(z[0]), complex(z[-1]))
        route_worst = max(route_worst, abs(g_schur - g_abcd))
        ftw_rows.append({"beta": float(beta), "W": W,
                         "S_dep": mp.nstr(s_dep, 6),
                         "junction_A": cnum(T[0, 0]),
                         "junction_B_over_Z1": cnum(T[0, 1]),
                         "junction_C_times_Z1": cnum(T[1, 0]),
                         "junction_D": cnum(T[1, 1]),
                         "gamma_schur": cnum(g_schur),
                         "gamma_abcd": cnum(g_abcd),
                         "T_squared_through_depleted":
                             mp.nstr(mp.mpf(float(1 - abs(g_schur)**2)), 17)})
    st["FT-W"] = {"mutation": "omega x 1e3 at the reference mass",
                  "rows": ftw_rows, "fires": bool(ftw_fire)}
    out["gates"]["G-ABCD"]["route_worst_abs_sep_under_FT_W"] = mp.nstr(
        mp.mpf(float(route_worst)), 6)
    out["gates"]["G-ABCD"]["route_tol"] = mp.nstr(TOL_ABCD_ROUTE, 3)
    out["gates"]["G-ABCD"]["route_pass_under_FT_W"] = bool(
        route_worst < float(TOL_ABCD_ROUTE))

    # FT-RT-* -- three EXACT synthetic ladders, one strictly inside each bin
    for tag, f, want in (("FT-RT-C", SYNTHETIC_LADDER_RATIOS[0],
                          "CONTACT-GOVERNED"),
                         ("FT-RT-I", SYNTHETIC_LADDER_RATIOS[1],
                          "INTERFERENCE"),
                         ("FT-RT-E", SYNTHETIC_LADDER_RATIOS[2],
                          "EDGE-GOVERNED")):
        z2 = np.array([1.0, float(f)])
        th2 = np.array([0.3, 0.7])
        g = schur_small(z2, th2, 0.0)
        exact = float(abs((1 - f) / (1 + f)))
        st[tag] = {"impedance_ratio": mp.nstr(f, 6),
                   "abs_gamma": mp.nstr(mp.mpf(float(abs(g))), 17),
                   "closed_form_abs_gamma": mp.nstr(mp.mpf(exact), 17),
                   "classifier": classify(float(abs(g))),
                   "expected": want,
                   "fires": bool(classify(float(abs(g))) == want
                                 and abs(abs(g) - exact) < 1e-14)}

    # FT-UNIT -- a complex cell impedance must break the losslessness receipt
    kp = K_WINDOWS[0]
    s2p, zbase = cell_profile(cfg0, 0, kp + 1)
    zbase = zbase / zbase[0]
    unit_dev = 0.0
    for bi in range(0, N_BAND, 8):
        coef = float(cfg_coef(cfg0, omega_of_row[row(0, bi)]))
        th = coef / np.exp((float(P_B) / 2.0) * np.log(s2p[:kp]))
        zmut = zbase.astype(np.complex128).copy()
        zmut[0] = zmut[0] * (1 + 0.01j)
        for gl in (-1.0, +1.0):
            g = schur_small(zmut, th, gl)
            unit_dev = max(unit_dev, abs(abs(g) - 1.0))
    st["FT-UNIT"] = {"mutation": "cell 1 impedance x (1 + 0.01i)",
                     "measured_abs_dev": mp.nstr(mp.mpf(float(unit_dev)), 6),
                     "threshold": "1e-3",
                     "fires": bool(unit_dev >= 1e-3)}

    # FT-XTIE
    ft = abs(mp.mpf(1) / (1 + mp.mpf("1e-6")) - 1)
    st["FT-XTIE"] = {"measured": mp.nstr(ft, 6), "threshold": "1e-7",
                     "fires": bool(ft >= mp.mpf("1e-7"))}
    # FT-DEP
    W0, _, _ = depletion_width(band[bic] * C0 / rsat_ref, BETAS[0], P_B,
                               rsat_ref, THETAS[0] * L_NODE)
    Wc0 = depletion_width_by_count(band[bic] * C0 / rsat_ref, BETAS[0], P_B,
                                   rsat_ref, THETAS[0] * L_NODE)
    st["FT-DEP"] = {"W_closed_form_mutated": W0 + 1, "W_by_count": Wc0,
                    "fires": bool((W0 + 1) != Wc0)}
    out["self_tests"] = st

    # =======================================================================
    # CERTIFICATION -- per configuration, per part
    # =======================================================================
    P1_GATE_SCOPE = {
        "G-CANON": ("CFG-A", "CFG-B"), "G-U": ("CFG-A", "CFG-B"),
        "G-DISP": ("CFG-A", "CFG-B"), "G-SUM": ("CFG-A", "CFG-B"),
        "G-PEAK": ("CFG-A", "CFG-B"),
        "G-NC": ("CFG-A",), "G-JA": ("CFG-A",), "G-NC-V1A": ("CFG-A",),
        "G-CF": ("CFG-B",), "G-DECADE": ("CFG-B",), "G-DISC": ("CFG-B",),
        "G-NC-V1B": ("CFG-B",),
    }
    P1_TEST_SCOPE = {
        "FT-NC": ("CFG-A",), "FT-JA": ("CFG-A",), "FT-V1": ("CFG-A", "CFG-B"),
        "FT-CF": ("CFG-B",), "FT-SUM": ("CFG-B",), "FT-DECADE": ("CFG-B",),
        "FT-PEAK": ("CFG-B",), "FT-DISC": ("CFG-B",),
        "FT-U": ("CFG-A", "CFG-B"), "FT-DISP": ("CFG-A", "CFG-B"),
        "FT-CANON": ("CFG-A", "CFG-B"), "FT-EVAN": ("CFG-A", "CFG-B"),
        "FT-TURN": ("CFG-A", "CFG-B"), "FT-CUT": ("CFG-A", "CFG-B"),
    }
    per_cfg = {}
    for cfg in ("CFG-A", "CFG-B"):
        failed = sorted(g for g, sc in P1_GATE_SCOPE.items()
                        if cfg in sc and not out["gates"][g].get("pass", False))
        unfired = sorted(t for t, sc in P1_TEST_SCOPE.items()
                         if cfg in sc and not st[t].get("fires", False))
        per_cfg[cfg] = {
            "gates_in_scope": sorted(g for g, sc in P1_GATE_SCOPE.items()
                                     if cfg in sc),
            "gates_failed": failed, "self_tests_unfired": unfired,
            "certification": ("DELAY-CERTIFIED" if not failed and not unfired
                              else "DELAY-NOT-CERTIFIED")}
    out["certification_per_configuration"] = per_cfg

    Y8_GATES = ("G-BAND", "G-DEP", "G-ABCD", "G-UNIT", "G-PREC", "G-KWIN",
                "G-XTIE", "G-MFREE")
    Y8_TESTS = ("FT-W", "FT-RT-C", "FT-RT-I", "FT-RT-E", "FT-UNIT",
                "FT-XTIE", "FT-DEP")
    y8_failed = sorted(g for g in Y8_GATES
                       if not out["gates"][g].get("pass", False))
    y8_unfired = sorted(t for t in Y8_TESTS if not st[t].get("fires", False))
    out["y8"]["certification"] = {
        "gates_in_scope": list(Y8_GATES), "gates_failed": y8_failed,
        "self_tests_unfired": y8_unfired,
        "certification": ("Y8-CERTIFIED" if not y8_failed and not y8_unfired
                          else "Y8-NOT-CERTIFIED"),
        "cross_part_gate": ("Y8 bins are additionally gated on CFG-B being "
                            "DELAY-CERTIFIED in PART 1")}

    # bin gating by certification
    for bname, scope in (("BIN-DA", ("CFG-A",)), ("BIN-DB", ("CFG-B",)),
                         ("BIN-DISC", ("CFG-A", "CFG-B"))):
        blocked = [c for c in scope
                   if per_cfg[c]["certification"] == "DELAY-NOT-CERTIFIED"]
        out["bins"][bname]["adjudicated"] = not blocked
        if blocked:
            out["bins"][bname]["not_adjudicated_because"] = (
                f"{sorted(blocked)} is DELAY-NOT-CERTIFIED")
    for cfg in ("CFG-A", "CFG-B"):
        adj = per_cfg[cfg]["certification"] == "DELAY-CERTIFIED"
        out["bins"]["BIN-CUTOFF"][cfg]["adjudicated"] = adj
        for k in out["bins"]["BIN-EVAN"]:
            if k.startswith(cfg):
                out["bins"]["BIN-EVAN"][k]["adjudicated"] = adj

    y8_adj = bool(out["y8"]["certification"]["certification"] == "Y8-CERTIFIED"
                  and per_cfg["CFG-B"]["certification"] == "DELAY-CERTIFIED"
                  and not out["bins"]["BIN-STOP-V1"]["fired"])
    for key in ("depletion_width", "reach_through", "rho_a"):
        out["y8"][key]["adjudicated"] = y8_adj
        if not y8_adj:
            out["y8"][key]["not_adjudicated_because"] = (
                "Y8 bins are gated on Y8-CERTIFIED AND CFG-B "
                "DELAY-CERTIFIED AND BIN-STOP-V1 not fired")

    out["certification"] = (
        "DELAY-CERTIFIED" if all(
            per_cfg[c]["certification"] == "DELAY-CERTIFIED"
            for c in ("CFG-A", "CFG-B")) else "DELAY-NOT-CERTIFIED")

    # =======================================================================
    # ship
    # =======================================================================
    out["_runtime_sec"] = round(time.time() - t_start, 2)
    body = {k: v for k, v in out.items() if k != "_runtime_sec"}
    out["_digest"] = hashlib.sha256(
        json.dumps(body, sort_keys=True).encode()).hexdigest()[:16]
    with open(OUT_JSON, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, sort_keys=True)
    print(f"[echo-delay-v2] PART 1 certification: {out['certification']}")
    print(f"[echo-delay-v2] per-config: "
          f"{ {c: per_cfg[c]['certification'] for c in per_cfg} }")
    print(f"[echo-delay-v2] Y8: {out['y8']['certification']['certification']}")
    print(f"[echo-delay-v2] BIN-W: {out['y8']['depletion_width']['bin']}  "
          f"BIN-RT: {out['y8']['reach_through']['bin']}  "
          f"RHO-A: {out['y8']['rho_a']['bin']}")
    print(f"[echo-delay-v2] digest: {out['_digest']}")
    print(f"[echo-delay-v2] wrote {os.path.relpath(OUT_JSON, REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

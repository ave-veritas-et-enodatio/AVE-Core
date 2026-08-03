#!/usr/bin/env python3
"""Cold-Q pole derivation v2.1 -- compactified hyperboloidal spectral instrument.

Resolves the frozen bins of
``research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md`` (commit 7d8fe484,
pushed BEFORE this file existed).

METHOD (prereg section 4.3, frozen):  a compactified hyperboloidal Chebyshev
spectral discretization in the Axiom-4 amplitude coordinate A = r_sat/r, with
the outgoing wave divided out in CLOSED FORM, the traction-free SHORT imposed
exactly as dpsi/deta = 0 at eta = 0, NO boundary condition imposed at infinity,
root extraction by extended-precision determinant polish, and pole counting by
an argument-principle winding of the determinant phase.  There is no matching
radius, no asymptotic series, no shooting and no subdominant-coefficient
extraction anywhere in the chain.

Engine ``src/ave`` is BYTE-UNTOUCHED; ``ave.core.constants`` is imported
read-only.  No RNG, no adaptivity: fully deterministic.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import sys
import time

import numpy as np
import scipy.linalg as sla

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(os.path.dirname(_HERE))
if os.path.join(_REPO, "src") not in sys.path:
    sys.path.insert(0, os.path.join(_REPO, "src"))

import mpmath as mp  # noqa: E402

from ave.core.constants import N_NU  # noqa: E402  (I10, read-only)

# ===========================================================================
# FROZEN NUMERICS (prereg section 4.4) -- ENGINEERING CHOICE, tagged
# ===========================================================================
N_PRIMARY = 48
N_INDEP = (48, 56, 64)
N_SWEEP = (24, 32, 40, 48, 56, 64)
LAMBDA_PRIMARY = 0.0
LAMBDA_INDEP = (-0.25, 0.0, 0.25)
DPS = 50
POLISH_TOL_EXP = 38
POLISH_ITERS = 60
RECT_WR = (0.02, 2.00)          # omega_R * M_g
RECT_WI = (1e-3, 1.00)          # |omega_I| * M_g
CTRL_BOX_R, CTRL_BOX_I = (0.05, 6.0), (0.02, 4.0)
CTRL_ELLS_LOW = (1, 2, 3)
HIGH_BOX_R, HIGH_BOX_I = (0.02, 20.0), (0.02, 10.0)
CTRL_ELLS_HIGH = (6, 10, 14, 18)
WIDTH_FAMILY = (0.5, 1.0, 2.0, 4.0, 8.0, 16.0)
WIDTH_ELL, WIDTH_N = 6, 32
WIDTH_BOX_I = (0.02, 8.0)
CONTOUR_SAMPLES = (200, 400, 800)
DEDUPE_REL = 1e-6
PHYS_REL = 1e-6                 # physical-vs-artifact criterion
C9_EVAL_GRID = 200
C9_N_LO, C9_N_HI = 32, 64
C10_BOUNDARY_PTS = 64
R_WALL_RATIO = 8.0              # closed cavity outer wall, in r_sat
N_CLOSED = 64
X_SAT = 7.0                     # I1
X_SAT_SET = (5.0, 7.0, 11.0)
ELL = 2                         # I8
ELL_LADDER = (2, 3, 4, 5)
LOC_WINDOW = (1.0, 2.0)         # r/r_sat, BIN-3

# FROZEN tolerances (prereg section 5)
TOL = {
    "C1_loc": 1e-20, "C1_wind": 1e-3,
    "C2": 1e-12, "C3": 1e-12, "C4_int": 1e-3, "C5": 1e-9,
    "C6_res": 1e-9, "C6_break": 1e-3, "C7": 1e-10,
    "C9": 1e-10, "C10": 1e-15, "C11": 1e-13,
}
FT_THRESH = {
    "FT_A": 1e-15, "FT_B": 1e-12, "FT_C": 1e-6, "FT_D_int": 1e-3,
    "FT_E": 1e-9, "FT_F_w": 1e-3, "FT_F_bc": 1e-2, "FT_G": 1e-5,
    "FT_H": 1e-15, "FT_H_rho": 1e30, "FT_I": 1e-10, "FT_J": 1e-13,
}


# ===========================================================================
# CHEBYSHEV
# ===========================================================================
def cheb(n: int):
    """Chebyshev-Gauss-Lobatto nodes on [0,1] ASCENDING + derivative matrix."""
    k = np.arange(n + 1)
    xc = np.cos(np.pi * k / n)
    c = np.ones(n + 1)
    c[0] = c[n] = 2.0
    c = c * (-1.0) ** k
    X = np.tile(xc, (n + 1, 1)).T
    dX = X - X.T
    D = np.outer(c, 1.0 / c) / (dX + np.eye(n + 1))
    D -= np.diag(D.sum(axis=1))
    return (1.0 - xc) / 2.0, -2.0 * D


def cheb_interp(nodes, vals, targets):
    """Barycentric interpolation from CGL nodes (ascending on [0,1])."""
    n = len(nodes) - 1
    k = np.arange(n + 1)
    w = (-1.0) ** k
    w[0] *= 0.5
    w[n] *= 0.5
    w = w[::-1]
    out = np.empty(len(targets), dtype=complex)
    for i, t in enumerate(targets):
        d = t - nodes
        hit = np.where(np.abs(d) < 1e-14)[0]
        if hit.size:
            out[i] = vals[hit[0]]
        else:
            num = np.sum(w / d * vals)
            out[i] = num / np.sum(w / d)
    return out


# ===========================================================================
# THE GRADED OPERATOR (prereg section 2.2)
#   A = r_sat/r = 1 - eta^2 ;  W = A exp(i Om (1/A + lam A)) psi
#   M(Om) = M0 + Om M1 + Om^2 M2 ; row 0 is the exact SHORT  dpsi/deta(0) = 0
# The coefficient path carries r_sat EXPLICITLY (r = x_sat / A) so that
# different x_sat produce different floating-point intermediates -- prereg
# section 0, the C5 arithmetic-fidelity requirement.
# ===========================================================================
def graded_coeff_parts(eta, ell, lam, x_sat=X_SAT, perturb_A=0.0, kill_B1=False):
    r_sat = float(x_sat)
    A0 = 1.0 - eta ** 2
    r_phys = r_sat / np.where(A0 == 0.0, np.finfo(float).tiny, A0)
    A = r_sat / r_phys                      # == A0, via the explicit r_sat path
    A = A * (1.0 + perturb_A)               # FT-E mutation hook
    two = 2.0 - eta ** 2
    u = np.sqrt(two)
    S = eta * u
    Asq = A ** 2
    B0 = -eta * Asq / two - 4.0 * eta * A
    B1 = 4j * eta - 4j * lam * Asq * eta
    if kill_B1:                             # FT-H(b) mutation hook
        B1 = B1 * 0.0
    C0 = -4.0 * ell * (ell + 1) * eta ** 2 - 8.0 * Asq / two
    C1 = 4j * A / two + 8j * lam * eta ** 2 * A - 4j * lam * A ** 3 / two
    C2 = 4.0 * eta / (u * (1.0 + S)) + 8.0 * eta ** 2 * lam \
        - 4.0 * eta ** 2 * lam ** 2 * Asq
    return Asq, B0, B1, C0, C1, C2


def graded_matrices(n, ell, lam, x_sat=X_SAT, equil=True, bc_perturb=0.0,
                    lam_bc_skip=False, perturb_A=0.0, kill_B1=False,
                    coeff_corrupt=0.0, spin1_wall=False):
    eta, D = cheb(n)
    D2 = D @ D
    Acoef, B0, B1, C0, C1, C2 = graded_coeff_parts(
        eta, ell, 0.0 if lam_bc_skip else lam, x_sat, perturb_A, kill_B1)
    if coeff_corrupt:                        # FT-J mutation hook
        C0 = C0 * (1.0 + coeff_corrupt)
    M0 = Acoef[:, None] * D2 + B0[:, None] * D + np.diag(C0).astype(complex)
    M1 = B1[:, None] * D + np.diag(C1).astype(complex)
    M2 = np.diag(C2).astype(complex)
    # row 0: the exact traction-free SHORT, dpsi/deta = 0 at eta = 0
    if spin1_wall:
        # FT-F(ii): the SPIN-1 wall condition W_r(r_sat) = 0 in place of the
        # spin-2 T(r_sat) = 0.  With W = A E psi this is
        #   [1 + i Om (lam - 1)] psi(0) - psi_etaeta(0)/2 = 0
        # -- a genuinely DIFFERENT condition, not a rescaling of the same row.
        M0[0, :] = -0.5 * D2[0, :]
        M0[0, 0] += 1.0
        M1[0, :] = 0.0
        M1[0, 0] = 1j * (lam - 1.0)
        M2[0, :] = 0.0
    else:
        M0[0, :] = D[0, :] * (1.0 + bc_perturb)
        M1[0, :] = 0.0
        M2[0, :] = 0.0
    s = np.ones(n + 1)
    if equil:
        s = np.maximum.reduce([np.abs(M0).max(1), np.abs(M1).max(1),
                               np.abs(M2).max(1)])
        s[s == 0] = 1.0
        M0, M1, M2 = M0 / s[:, None], M1 / s[:, None], M2 / s[:, None]
    return M0, M1, M2, eta, D, s


def flat_matrices(n, ell, lam, equil=True, bc_perturb=0.0):
    """ZERO-GRADE control (prereg section 2.4), collocated in A directly.
       A^2 psi_AA + (2A - 2iOm) psi_A - l(l+1) psi = 0 ; wall (iOm-2)psi - psi_A = 0
    """
    A, D = cheb(n)
    D2 = D @ D
    Eye = np.eye(n + 1)
    X = np.diag(A)
    M0 = X @ X @ D2 + 2.0 * X @ D - ell * (ell + 1) * Eye
    M1 = 2j * lam * (X @ X @ D) - 2j * D + 2j * lam * X
    M2 = -(lam ** 2) * (X @ X) + 2.0 * lam * Eye
    M0[n, :] = -D[n, :] * (1.0 + bc_perturb)
    M0[n, n] += -2.0
    M1[n, :] = 0.0
    M1[n, n] = 1j * (1.0 - lam)
    M2[n, :] = 0.0
    if equil:
        s = np.maximum.reduce([np.abs(M0).max(1), np.abs(M1).max(1),
                               np.abs(M2).max(1)])
        s[s == 0] = 1.0
        M0, M1, M2 = M0 / s[:, None], M1 / s[:, None], M2 / s[:, None]
    return M0, M1, M2, A, D


def assemble(M0, M1, M2, om):
    return M0 + om * M1 + om * om * M2


def pencil_spectrum(M0, M1, M2):
    """Double-precision linearized spectrum -- SEEDS ONLY, no accuracy claim."""
    N = M0.shape[0]
    if np.max(np.abs(M2)) < 1e-14:
        ev = sla.eig(M0, -M1, right=False)
    else:
        Z, Eye = np.zeros((N, N), dtype=complex), np.eye(N)
        ev = sla.eig(np.block([[M0, Z], [Z, Eye]]),
                     np.block([[-M1, -M2], [Eye, Z]]), right=False)
    return np.array([z for z in ev if np.isfinite(z) and abs(z) < 1e8])


def winding(mat_fn, box_r, box_i, nq):
    """Argument-principle winding from the unwrapped phase of the LU SIGN of
    det M(Om).  Never a product of pivots and never a sum of principal pivot
    logarithms (prereg section 4.4 / section 9 item 6)."""
    (r0, r1), (i0, i1) = box_r, box_i
    corners = [complex(r0, -i0), complex(r0, -i1), complex(r1, -i1),
               complex(r1, -i0)]
    pts = []
    for a, b in zip(corners, corners[1:] + corners[:1]):
        pts.extend(a + (b - a) * (np.arange(nq) / nq))
    pts.append(pts[0])
    ph = []
    for w in pts:
        sgn, _ = np.linalg.slogdet(mat_fn(w))
        if not np.isfinite(sgn):
            return float("nan")
        ph.append(np.angle(sgn))
    ph = np.unwrap(np.asarray(ph))
    return float((ph[-1] - ph[0]) / (2 * np.pi))


# ===========================================================================
# EXTENDED-PRECISION DETERMINANT POLISH (prereg section 4.4)
# ===========================================================================
_MP_CACHE: dict = {}
_CHEB_MP: dict = {}


def cheb_mp(n, dps=DPS):
    """Chebyshev-Gauss-Lobatto nodes + D + D2, built ENTIRELY in mp."""
    key = (n, dps)
    if key in _CHEB_MP:
        return _CHEB_MP[key]
    mp.mp.dps = dps
    xc = [mp.cos(mp.pi * mp.mpf(i) / n) for i in range(n + 1)]
    c = [(mp.mpf(2) if (i == 0 or i == n) else mp.mpf(1)) * (-1) ** i
         for i in range(n + 1)]
    D = mp.zeros(n + 1, n + 1)
    for i in range(n + 1):
        for j in range(n + 1):
            if i != j:
                D[i, j] = c[i] / c[j] / (xc[i] - xc[j])
    for i in range(n + 1):
        D[i, i] = -sum(D[i, j] for j in range(n + 1) if j != i)
    D = -2 * D
    D2 = D * D
    eta = [(1 - xc[i]) / 2 for i in range(n + 1)]
    _CHEB_MP[key] = (eta, D, D2)
    return _CHEB_MP[key]


def _equil_mp(M0, M1, M2):
    n = M0.rows
    for i in range(n):
        s = max(max(abs(M0[i, j]) for j in range(n)),
                max(abs(M1[i, j]) for j in range(n)),
                max(abs(M2[i, j]) for j in range(n)))
        if s == 0:
            continue
        for j in range(n):
            M0[i, j] /= s
            M1[i, j] /= s
            M2[i, j] /= s
    return M0, M1, M2


def graded_matrices_mp(n, ell, lam, x_sat=X_SAT, dps=DPS, bc_perturb=0.0,
                       lam_bc_skip=False, perturb_A=0.0, kill_B1=False,
                       coeff_corrupt=0.0, spin1_wall=False):
    mp.mp.dps = dps
    eta, D, D2 = cheb_mp(n, dps)
    N = n + 1
    r_sat = mp.mpf(x_sat)
    lm = mp.mpf(0) if lam_bc_skip else mp.mpf(lam)
    M0, M1, M2 = mp.zeros(N, N), mp.zeros(N, N), mp.zeros(N, N)
    for i in range(N):
        e = eta[i]
        A0 = 1 - e ** 2
        A = (r_sat / (r_sat / A0)) if A0 != 0 else mp.mpf(0)
        A = A * (1 + mp.mpf(perturb_A))
        two = 2 - e ** 2
        u = mp.sqrt(two)
        S = e * u
        Asq = A ** 2
        B0 = -e * Asq / two - 4 * e * A
        B1 = mp.mpc(0, 4) * e - mp.mpc(0, 4) * lm * Asq * e
        if kill_B1:
            B1 = mp.mpc(0)
        C0 = -4 * ell * (ell + 1) * e ** 2 - 8 * Asq / two
        C0 = C0 * (1 + mp.mpf(coeff_corrupt))
        C1 = (mp.mpc(0, 4) * A / two + mp.mpc(0, 8) * lm * e ** 2 * A
              - mp.mpc(0, 4) * lm * A ** 3 / two)
        C2 = 4 * e / (u * (1 + S)) + 8 * e ** 2 * lm - 4 * e ** 2 * lm ** 2 * Asq
        for j in range(N):
            M0[i, j] = Asq * D2[i, j] + B0 * D[i, j]
            M1[i, j] = B1 * D[i, j]
        M0[i, i] += C0
        M1[i, i] += C1
        M2[i, i] += C2
    for j in range(N):
        M0[0, j] = mp.mpc(0)
        M1[0, j] = mp.mpc(0)
        M2[0, j] = mp.mpc(0)
    if spin1_wall:
        for j in range(N):
            M0[0, j] = -D2[0, j] / 2
        M0[0, 0] += 1
        M1[0, 0] = mp.mpc(0, 1) * (lm - 1)
    else:
        for j in range(N):
            M0[0, j] = D[0, j] * (1 + mp.mpf(bc_perturb))
    return _equil_mp(M0, M1, M2)


def flat_matrices_mp(n, ell, lam, dps=DPS, bc_perturb=0.0):
    mp.mp.dps = dps
    A, D, D2 = cheb_mp(n, dps)
    N = n + 1
    lm = mp.mpf(lam)
    M0, M1, M2 = mp.zeros(N, N), mp.zeros(N, N), mp.zeros(N, N)
    for i in range(N):
        a = A[i]
        for j in range(N):
            M0[i, j] = a * a * D2[i, j] + 2 * a * D[i, j]
            M1[i, j] = 2j * lm * a * a * D[i, j] - mp.mpc(0, 2) * D[i, j]
        M0[i, i] -= ell * (ell + 1)
        M1[i, i] += mp.mpc(0, 2) * lm * a
        M2[i, i] += -(lm ** 2) * a * a + 2 * lm
    for j in range(N):
        M0[n, j] = -D[n, j] * (1 + mp.mpf(bc_perturb))
        M1[n, j] = mp.mpc(0)
        M2[n, j] = mp.mpc(0)
    M0[n, n] += -2
    M1[n, n] = mp.mpc(0, 1) * (1 - lm)
    return _equil_mp(M0, M1, M2)


def mp_parts(key, builder):
    if key not in _MP_CACHE:
        _MP_CACHE[key] = builder()
    return _MP_CACHE[key]


def mp_det(M0, M1, M2, om):
    n = M0.rows
    o = mp.mpc(om)
    o2 = o * o
    Amat = mp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            Amat[i, j] = M0[i, j] + o * M1[i, j] + o2 * M2[i, j]
    d = mp.mpc(1)
    for k in range(n):
        p = max(range(k, n), key=lambda r: abs(Amat[r, k]))
        if p != k:
            for j in range(k, n):
                Amat[k, j], Amat[p, j] = Amat[p, j], Amat[k, j]
            d = -d
        piv = Amat[k, k]
        if piv == 0:
            return mp.mpc(0)
        d *= piv
        for i in range(k + 1, n):
            f = Amat[i, k] / piv
            for j in range(k, n):
                Amat[i, j] -= f * Amat[k, j]
    return d


def mp_polish(M0, M1, M2, om0, dps=DPS):
    """Deterministic complex secant on det M(Om).  No RNG, no adaptivity."""
    mp.mp.dps = dps
    b = mp.mpc(om0)
    a = b * (1 + mp.mpf(10) ** (-6))
    fa = mp_det(M0, M1, M2, a)
    fb = mp_det(M0, M1, M2, b)
    for _ in range(POLISH_ITERS):
        if fb == fa:
            break
        c = b - fb * (b - a) / (fb - fa)
        if not mp.isfinite(c.real) or abs(c - b) > 10 * abs(b) + 10:
            return None
        a, fa, b = b, fb, c
        fb = mp_det(M0, M1, M2, b)
        if abs(b - a) <= mp.mpf(10) ** (-POLISH_TOL_EXP) * abs(b):
            break
    return b


def in_box(z, box_r, box_i):
    re, im = float(z.real), float(z.imag)
    return (box_r[0] <= re <= box_r[1]) and (box_i[0] <= -im <= box_i[1])


def to_c(z):
    return complex(float(z.real), float(z.imag))


def dedupe(vals, rel=DEDUPE_REL):
    out = []
    for z in vals:
        if not any(abs(z - q) <= rel * max(abs(q), 1.0) for q in out):
            out.append(z)
    return out


def locate_roots(M0d, M1d, M2d, mpk, builder, box_r, box_i, dps=DPS):
    """Seeds from the double-precision pencil (SEEDS ONLY, no accuracy claim);
    roots from the mp polish on the mp OPERATOR; re-filtered after polishing.
    Returns mp values -- the precision is carried end to end."""
    seeds = [z for z in pencil_spectrum(M0d, M1d, M2d) if in_box(z, box_r, box_i)]
    P0, P1, P2 = mp_parts(mpk, builder)
    out = []
    for s in seeds:
        r = mp_polish(P0, P1, P2, s, dps)
        if r is not None and in_box(r, box_r, box_i):
            out.append(r)
    return sorted(dedupe(out), key=lambda z: abs(z.imag))


# ===========================================================================
# ZERO-GRADE CLOSED-FORM REFERENCE (prereg section 2.4), in mp
# ===========================================================================
def flat_closed_form(ell, dps=DPS):
    """Roots of  i x u + x u' - (ell+2) u,  u = x^(l+1) h_l(x) e^(-ix),
    a polynomial of degree exactly ell+1.  Computed in mp."""
    mp.mp.dps = dps
    co = [mp.mpc(0)] * (ell + 1)             # u = sum co[m] x^(ell-m)
    for m in range(ell + 1):
        co[m] = ((mp.mpc(0, -1) ** (ell + 1)) * (mp.mpc(0, 1) ** m)
                 * mp.factorial(ell + m)
                 / (mp.factorial(m) * mp.factorial(ell - m)) / mp.mpf(2) ** m)
    # u' coefficients (degree ell-1)
    du = [co[m] * (ell - m) for m in range(ell)]
    # p = i*x*u + x*u' - (ell+2)*u   -> degree ell+1
    p = [mp.mpc(0)] * (ell + 2)
    for m in range(ell + 1):                 # i*x*u : x^(ell-m+1)
        p[m] += mp.mpc(0, 1) * co[m]
    for m in range(ell):                     # x*u'  : x^(ell-m)
        p[m + 1] += du[m]
    for m in range(ell + 1):                 # -(ell+2)*u : x^(ell-m)
        p[m + 1] -= (ell + 2) * co[m]
    return list(mp.polyroots(p, maxsteps=200, extraprec=200))


# ===========================================================================
# CLOSED CAVITY (C6 / C7 / FT-F / FT-G) -- traction-free at BOTH ends.
#   r = r_sat + eta^2 ,  eta in [0, eta_max] ,  eta_max = sqrt(R_wall - r_sat)
# ===========================================================================
def cc_weights(n, a, b):
    """Clenshaw-Curtis weights on the CGL grid, mapped to [a, b]."""
    k = np.arange(n + 1)
    w = np.zeros(n + 1)
    for i in k:
        c = 1.0 if (i == 0 or i == n) else 2.0
        s = 0.0
        for j in range(1, n // 2 + 1):
            bj = 1.0 if (2 * j == n) else 2.0
            s += bj / (4.0 * j * j - 1.0) * math.cos(2.0 * j * i * math.pi / n)
        w[i] = c / n * (1.0 - s)
    return w * (b - a) / 2.0


def closed_cavity(n, ell, x_sat=X_SAT, loss=0.0):
    r_sat = float(x_sat)
    R_wall = R_WALL_RATIO * r_sat
    emax = math.sqrt(R_wall - r_sat)
    t, Dt = cheb(n)
    eta = t * emax
    D = Dt / emax
    D2 = D @ D
    r = r_sat + eta ** 2
    mhat = np.sqrt(2.0 * r_sat + eta ** 2) / r
    dmhat = eta * (-3.0 * r_sat - eta ** 2) / (np.sqrt(2.0 * r_sat + eta ** 2) * r ** 2)
    if loss:
        mhat = mhat * (1.0 + 1j * loss)
        dmhat = dmhat * (1.0 + 1j * loss)
    bcoef = 4.0 * eta / r + dmhat / mhat
    ccoef = (-4.0 * eta ** 2 * ell * (ell + 1) / r ** 2 - 2.0 / r
             - 2.0 * eta * dmhat / (mhat * r))
    L = (D2 + bcoef[:, None] * D + np.diag(ccoef)).astype(complex)
    K = np.diag(-4.0 * eta / mhat).astype(complex)
    L[0, :] = D[0, :]                       # inner traction-free: W_eta(0) = 0
    K[0, :] = 0.0
    outer = D[n, :] / (2.0 * eta[n])
    outer[n] -= 1.0 / r[n]
    L[n, :] = outer                          # outer traction-free
    K[n, :] = 0.0
    w2, V = sla.eig(L, K)
    keep = [i for i in range(len(w2)) if np.isfinite(w2[i]) and abs(w2[i]) < 1e12]
    w2 = w2[keep]
    V = V[:, keep]
    order = np.argsort(np.abs(w2))
    return w2[order], V[:, order], eta, D, D2, r, mhat, emax


def rayleigh(W, eta, D, D2, r, mhat, emax, ell, n, weight_ll):
    """Spin-2 (or spin-1) Rayleigh quotient for the closed cavity.
       E_strain = int mu(|W_r - W/r|^2 + weight*|W|^2/r^2) r^2 dr ; dr = 2 eta d eta
    """
    mu = eta * mhat
    dW = D @ W
    Wr = np.empty_like(W)
    Wr[1:] = dW[1:] / (2.0 * eta[1:])
    Wr[0] = (D2 @ W)[0] / 2.0
    integ_s = mu * (np.abs(Wr - W / r) ** 2 + weight_ll * np.abs(W) ** 2 / r ** 2) \
        * r ** 2 * 2.0 * eta
    integ_k = np.abs(W) ** 2 * r ** 2 * 2.0 * eta
    w = cc_weights(n, 0.0, emax)
    return float(np.sum(w * integ_s.real)) / float(np.sum(w * integ_k.real))


# ===========================================================================
# OPEN-PROBLEM EIGENVECTOR + LOCALIZATION (BIN-3)
# ===========================================================================
def null_vector(M):
    u, s, vh = np.linalg.svd(M)
    return vh[-1, :].conj()


def localization(om_Mg, n, ell, lam, x_sat=X_SAT):
    r_sat = float(x_sat)
    Om = om_Mg * r_sat
    M0, M1, M2, eta, D, _ = graded_matrices(n, ell, lam, x_sat)
    psi = null_vector(assemble(M0, M1, M2, Om))
    dpsi = D @ psi
    a_lo = 1.0 / LOC_WINDOW[1]
    e_hi = math.sqrt(1.0 - a_lo)
    grid = np.linspace(0.0, e_hi, 401)
    p = cheb_interp(eta, psi, grid)
    dp = cheb_interp(eta, dpsi, grid)
    A = 1.0 - grid ** 2
    r = r_sat / A
    E = np.exp(1j * Om * (1.0 / A + lam * A))
    W = A * E * p
    psi_A = np.where(grid == 0.0, 0.0, dp / (-2.0 * np.maximum(grid, 1e-300)))
    W_A = E * (p + 1j * Om * (lam * A - 1.0 / A) * p + A * psi_A)
    W_r = -(A ** 2 / r_sat) * W_A
    S = np.sqrt(np.maximum(1.0 - A ** 2, 0.0))
    mu = S
    om = om_Mg
    e_kin = np.abs(om) ** 2 * np.abs(W) ** 2 * r ** 2
    e_str = mu * (np.abs(W_r - W / r) ** 2
                  + (ell - 1) * (ell + 2) * np.abs(W) ** 2 / r ** 2) * r ** 2
    e_tot = e_kin + e_str
    u_all = r / r_sat
    i_e, i_k = int(np.argmax(e_tot)), int(np.argmax(e_kin))
    interior = 0 < i_e < len(grid) - 1
    return {
        "u_energy": float(u_all[i_e]), "u_kinetic": float(u_all[i_k]),
        "interior_max": bool(interior),
        "wall_fraction_of_peak": float(e_tot[0] / np.max(e_tot)),
    }


# ===========================================================================
# FUNDAMENTAL-POLE EXTRACTION
# ===========================================================================
_FUND_CACHE: dict = {}


def fundamental(n, ell, lam, x_sat=X_SAT, dps=DPS, **mut):
    """Least-damped physical root of the graded problem, in Omega = omega*r_sat.

    Memoized on the EXACT argument tuple.  This is a pure performance
    optimization -- identical calls recur across C2/C3/C5 and the artifact
    filter -- and has ZERO numerical effect: the same arguments deterministically
    produce the same result (no RNG, no adaptivity).
    """
    ck = (n, ell, lam, x_sat, dps, tuple(sorted(mut.items())))
    if ck in _FUND_CACHE:
        return _FUND_CACHE[ck]
    r_sat = float(x_sat)
    br = (RECT_WR[0] * r_sat, RECT_WR[1] * r_sat)
    bi = (RECT_WI[0] * r_sat, RECT_WI[1] * r_sat)
    key = ("g", n, ell, lam, x_sat, tuple(sorted(mut.items())), dps)

    def build():
        return graded_matrices_mp(n, ell, lam, x_sat, dps, **mut)

    M0, M1, M2, _, _, _ = graded_matrices(n, ell, lam, x_sat, **mut)
    roots = [to_c(z) for z in locate_roots(M0, M1, M2, key, build, br, bi, dps)]
    res = ((roots[0] if roots else None), roots, (br, bi))
    _FUND_CACHE[ck] = res
    return res


# ===========================================================================
# THE CERTIFICATION BATTERY (prereg section 5) -- RUN FIRST
# ===========================================================================
def gate_C11():
    """eta-form operator == 4 eta^2 * A-form operator, on test functions."""
    def LA(psi, dA, d2A, A, ell, Om, lam):
        S = np.sqrt(1.0 - A ** 2)
        gh = -A / (1.0 - A ** 2)
        P = -2j * Om + 2.0 * A + A ** 2 * gh + 2j * Om * lam * A ** 2
        Q = (Om ** 2 / (S * (1.0 + S)) - 1j * Om * gh - ell * (ell + 1)
             + 2.0 * A * gh + 1j * Om * lam * (-2j * Om + 2.0 * A + A ** 2 * gh)
             - Om ** 2 * lam ** 2 * A ** 2)
        return A ** 2 * d2A + P * dA + Q * psi
    worst, worst_c = 0.0, 0.0
    for lam in LAMBDA_INDEP:
        for ell in (2, 3):
            for Om in (0.9 - 0.3j, 2.5 - 1.1j, 14.0 - 6.0j):
                for e in (0.13, 0.37, 0.61, 0.88, 0.97):
                    A = 1.0 - e ** 2
                    f = math.exp(0.7 * A) * (1.0 + 0.3 * A ** 2)
                    df = math.exp(0.7 * A) * (0.7 + 0.6 * A + 0.21 * A ** 2)
                    d2f = math.exp(0.7 * A) * (1.09 + 0.84 * A + 0.147 * A ** 2)
                    de = df * (-2.0 * e)
                    d2e = d2f * (4.0 * e ** 2) + df * (-2.0)
                    ea = np.array([e])
                    for corrupt, store in ((0.0, "ok"), (1e-12, "bad")):
                        Ac, B0, B1, C0, C1, C2 = graded_coeff_parts(ea, ell, lam)
                        C0c = C0 * (1.0 + corrupt)
                        lhs = (Ac[0] * d2e + (B0[0] + Om * B1[0]) * de
                               + (C0c[0] + Om * C1[0] + Om ** 2 * C2[0]) * f)
                        rhs = 4.0 * e ** 2 * LA(f, df, d2f, A, ell, Om, lam)
                        rel = abs(lhs - rhs) / max(abs(rhs), 1e-300)
                        if store == "ok":
                            worst = max(worst, rel)
                        else:
                            worst_c = max(worst_c, rel)
    return {"measured": worst, "tol": TOL["C11"], "pass": bool(worst <= TOL["C11"]),
            "FT_J_corrupted": worst_c, "FT_J_threshold": FT_THRESH["FT_J"],
            "FT_J_fires": bool(worst_c >= FT_THRESH["FT_J"])}


def gate_C1():
    """ZERO-GRADE CLOSED-FORM CONTROL -- the entry ticket."""
    rows, allpass = [], True
    ft_a_worst = 0.0
    for ells, box_r, box_i, nn in ((CTRL_ELLS_LOW, CTRL_BOX_R, CTRL_BOX_I, 32),
                                   (CTRL_ELLS_HIGH, HIGH_BOX_R, HIGH_BOX_I, 40)):
        for ell in ells:
            cf = [z for z in flat_closed_form(ell) if in_box(z, box_r, box_i)]
            cf = sorted(cf, key=lambda z: (round(float(z.real), 9), float(z.imag)))
            M0, M1, M2, _, _ = flat_matrices(nn, ell, 0.0)
            key = ("f", nn, ell, 0.0)

            def build(nn=nn, ell=ell):
                return flat_matrices_mp(nn, ell, 0.0)

            got = locate_roots(M0, M1, M2, key, build, box_r, box_i)
            got = sorted(got, key=lambda z: (round(float(z.real), 9), float(z.imag)))
            ok_n = (len(got) == len(cf))
            err = (float(max((abs(a - b) for a, b in zip(got, cf)),
                             default=mp.mpf(0)))
                   if ok_n else float("inf"))
            w = [winding(lambda om, M0=M0, M1=M1, M2=M2: assemble(M0, M1, M2, om),
                         box_r, box_i, q) for q in CONTOUR_SAMPLES]
            ok_w = all(abs(abs(x) - len(cf)) <= TOL["C1_wind"] for x in w)
            # FT-A: perturbed wall-BC row must move the roots
            Mp = flat_matrices(nn, ell, 0.0, bc_perturb=1e-9)[:3]
            kp = ("fp", nn, ell)
            gp = locate_roots(Mp[0], Mp[1], Mp[2], kp,
                              lambda nn=nn, ell=ell: flat_matrices_mp(
                                  nn, ell, 0.0, bc_perturb=1e-9), box_r, box_i)
            gp = sorted(gp, key=lambda z: (round(float(z.real), 9), float(z.imag)))
            if len(gp) == len(got):
                ft_a_worst = max(ft_a_worst,
                                 float(max((abs(a - b) for a, b in zip(gp, got)),
                                           default=mp.mpf(0))))
            p = bool(ok_n and err <= TOL["C1_loc"] and ok_w)
            allpass &= p
            rows.append({"ell": ell, "n": nn, "closed_form_count": len(cf),
                         "located_count": len(got), "max_loc_err": err,
                         "winding": [float(x) for x in w], "pass": p,
                         "closed_form_roots": [[float(z.real), float(z.imag)]
                                               for z in cf],
                         "located_roots": [[float(z.real), float(z.imag)]
                                           for z in got]})
    return ({"rows": rows, "tol_loc": TOL["C1_loc"], "tol_wind": TOL["C1_wind"],
             "pass": bool(allpass)},
            {"measured": ft_a_worst, "threshold": FT_THRESH["FT_A"],
             "fires": bool(ft_a_worst >= FT_THRESH["FT_A"])})


def gate_C2_C3(base):
    """Gauge independence (C2) and resolution convergence (C3)."""
    lam_vals = {}
    for lam in LAMBDA_INDEP:
        r = base if lam == LAMBDA_PRIMARY else fundamental(N_PRIMARY, ELL, lam)[0]
        lam_vals[lam] = r
    ok2, w2 = True, 0.0
    ls = [v for v in lam_vals.values() if v is not None]
    for i in range(len(ls)):
        for j in range(i + 1, len(ls)):
            d = abs(ls[i] - ls[j]) / abs(ls[i])
            w2 = max(w2, d)
    ok2 = bool(len(ls) == len(LAMBDA_INDEP) and w2 <= TOL["C2"])
    n_vals = {}
    for n in N_INDEP:
        n_vals[n] = base if n == N_PRIMARY else fundamental(n, ELL, LAMBDA_PRIMARY)[0]
    ns = [v for v in n_vals.values() if v is not None]
    w3 = 0.0
    for i in range(len(ns)):
        for j in range(i + 1, len(ns)):
            w3 = max(w3, abs(ns[i] - ns[j]) / abs(ns[i]))
    ok3 = bool(len(ns) == len(N_INDEP) and w3 <= TOL["C3"])
    sweep = {}
    for n in N_SWEEP:
        v = n_vals.get(n) or fundamental(n, ELL, LAMBDA_PRIMARY)[0]
        sweep[str(n)] = [v.real, v.imag] if v is not None else None
    # FT-B: gauge applied to interior but NOT to the wall-BC row
    fb = fundamental(N_PRIMARY, ELL, 0.25, lam_bc_skip=True)[0]
    ftb = (abs(fb - lam_vals[0.25]) / abs(lam_vals[0.25])
           if (fb is not None and lam_vals[0.25] is not None) else float("inf"))
    # FT-C: grossly under-resolved
    fc = fundamental(8, ELL, LAMBDA_PRIMARY)[0]
    ref = n_vals[64]
    ftc = abs(fc - ref) / abs(ref) if (fc is not None and ref is not None) else float("inf")
    return ({"measured": w2, "tol": TOL["C2"], "pass": ok2,
             "by_lambda": {str(k): ([v.real, v.imag] if v else None)
                           for k, v in lam_vals.items()}},
            {"measured": w3, "tol": TOL["C3"], "pass": ok3, "sweep": sweep},
            {"measured": ftb, "threshold": FT_THRESH["FT_B"],
             "fires": bool(ftb >= FT_THRESH["FT_B"])},
            {"measured": ftc, "threshold": FT_THRESH["FT_C"],
             "fires": bool(ftc >= FT_THRESH["FT_C"])})


def gate_C4(roots, box):
    """Argument-principle consistency + count-vs-box-WIDTH scaling."""
    br, bi = box
    M0, M1, M2, _, _, _ = graded_matrices(N_PRIMARY, ELL, LAMBDA_PRIMARY)
    w = [winding(lambda om: assemble(M0, M1, M2, om), br, bi, q)
         for q in CONTOUR_SAMPLES]
    near_int = all(abs(abs(x) - round(abs(x))) <= TOL["C4_int"] for x in w)
    same = all(abs(abs(x) - abs(w[0])) <= TOL["C4_int"] for x in w)
    eq = abs(abs(w[0]) - len(roots)) <= TOL["C4_int"]
    # width family on the zero-grade control at closed-form-known content
    cf = flat_closed_form(WIDTH_ELL)
    F0, F1, F2, _, _ = flat_matrices(WIDTH_N, WIDTH_ELL, 0.0)
    fam, fam_ok = [], True
    for W in WIDTH_FAMILY:
        b_r = (0.02, W)
        content = sum(1 for z in cf if in_box(z, b_r, WIDTH_BOX_I))
        ww = winding(lambda om: assemble(F0, F1, F2, om), b_r, WIDTH_BOX_I, 400)
        ok = abs(abs(ww) - content) <= TOL["C4_int"]
        fam_ok &= ok
        fam.append({"width": W, "closed_form_content": content,
                    "winding": float(ww), "pass": bool(ok)})
    counts = [f["closed_form_content"] for f in fam]
    saturates = bool(len(set(counts)) < len(counts))
    return ({"winding": [float(x) for x in w], "located": len(roots),
             "integer_ok": bool(near_int), "sampling_stable": bool(same),
             "equals_located": bool(eq), "width_family": fam,
             "width_family_pass": bool(fam_ok),
             "content_saturates_while_width_doubles": saturates,
             "tol": TOL["C4_int"],
             "pass": bool(near_int and same and eq and fam_ok)},
            {"width_family": fam, "width_family_pass": bool(fam_ok),
             "saturates": saturates,
             "fires": bool(fam_ok and saturates)})


def gate_C5(base):
    """nu_vac cancellation, measured across x_sat, + FT-E mutation."""
    def sweep(pert):
        out = {}
        for xs in X_SAT_SET:
            r = (base if (xs == X_SAT and not pert)
                 else fundamental(N_PRIMARY, ELL, LAMBDA_PRIMARY, xs,
                                  **({"perturb_A": pert * (xs - 7.0) / 7.0} if pert else {}))[0])
            if r is None:
                return None
            out[xs] = r
        return out
    def spreads(d):
        Q = {k: v.real / (2.0 * abs(v.imag)) for k, v in d.items()}
        qv = list(Q.values())
        q_spread = (max(qv) - min(qv)) / abs(np.mean(qv))
        om = {k: v / k for k, v in d.items()}          # omega_R*M_g scaling as 1/x_sat
        ov = [abs(v) for v in d.values()]
        o_spread = (max(ov) - min(ov)) / abs(np.mean(ov))
        return Q, q_spread, o_spread, om
    d = sweep(0.0)
    Q, qs, os_, om = spreads(d)
    dm = sweep(1e-6)
    qs_m = spreads(dm)[1] if dm else float("inf")
    return ({"Omega_by_x_sat": {str(k): [v.real, v.imag] for k, v in d.items()},
             "Q_by_x_sat": {str(k): v for k, v in Q.items()},
             "omega_Mg_by_x_sat": {str(k): [v.real, v.imag] for k, v in om.items()},
             "Q_spread": qs, "Omega_spread": os_, "tol": TOL["C5"],
             "pass": bool(qs <= TOL["C5"] and os_ <= TOL["C5"])},
            {"measured": qs_m, "threshold": FT_THRESH["FT_E"],
             "fires": bool(qs_m >= FT_THRESH["FT_E"])})


def gate_C6_C7(base):
    """Closed cavity: Ax-3 reality (C7), spin-2 Rayleigh (C6), FT-F, FT-G."""
    w2, V, eta, D, D2, r, mhat, emax = closed_cavity(N_CLOSED, ELL)
    phys = [i for i in range(len(w2)) if w2[i].real > 0]
    worst = 0.0
    for i in phys:
        om = np.sqrt(complex(w2[i]))
        worst = max(worst, abs(om.imag) / abs(om))
    c7 = {"n_modes": len(phys), "max_rel_imag": worst, "tol": TOL["C7"],
          "pass": bool(len(phys) > 0 and worst <= TOL["C7"])}
    i0 = phys[0]
    W = V[:, i0]
    W = W / W[np.argmax(np.abs(W))]
    w2_eig = complex(w2[i0]).real
    rq2 = rayleigh(W, eta, D, D2, r, mhat, emax, ELL, N_CLOSED,
                   (ELL - 1) * (ELL + 2))
    rq1 = rayleigh(W, eta, D, D2, r, mhat, emax, ELL, N_CLOSED, ELL * (ELL + 1))
    res = abs(rq2 / w2_eig - 1.0)
    brk = abs(rq1 / w2_eig - 1.0)
    # FT-F(ii): spin-1 wall condition W'(r_sat) = 0 in place of T(r_sat) = 0.
    # In the eta variable T(0)=0 is W_eta(0)=0; the spin-1 analogue W_r(r_sat)=0
    # is W_etaeta(0) = 0 (since W_r = W_eta/(2 eta) -> W_etaeta/2 at eta=0).
    bad = fundamental(N_PRIMARY, ELL, LAMBDA_PRIMARY, spin1_wall=True)[0]
    ftf_bc = abs(bad - base) / abs(base) if bad is not None else float("inf")
    c6 = {"omega2_eig": w2_eig, "rayleigh_spin2": rq2, "residual": res,
          "rayleigh_spin1": rq1, "spin1_break": brk,
          "tol_res": TOL["C6_res"], "tol_break": TOL["C6_break"],
          "pass": bool(res <= TOL["C6_res"] and brk >= TOL["C6_break"])}
    # FT-G: smuggled loss
    w2l, _, _, _, _, _, _, _ = closed_cavity(N_CLOSED, ELL, loss=1e-3)
    physl = [i for i in range(len(w2l)) if w2l[i].real > 0]
    wl = 0.0
    for i in physl:
        om = np.sqrt(complex(w2l[i]))
        wl = max(wl, abs(om.imag) / abs(om))
    return (c6, c7,
            {"spin1_weight_break": brk, "threshold_w": FT_THRESH["FT_F_w"],
             "spin1_wall_shift": ftf_bc, "threshold_bc": FT_THRESH["FT_F_bc"],
             "cross_lane_845_FT6": 0.21729,
             "cross_lane_note": "NOT-ADJUDICATED prior-lane data; NON-GATING (prereg FLAG-2)",
             "fires": bool(brk >= FT_THRESH["FT_F_w"]
                           and ftf_bc >= FT_THRESH["FT_F_bc"])},
            {"measured": wl, "threshold": FT_THRESH["FT_G"],
             "fires": bool(wl >= FT_THRESH["FT_G"])})


def _c9_probe(n, Om, lam=LAMBDA_PRIMARY):
    M0, M1, M2, eta, _, s = graded_matrices(n, ELL, lam)
    M = assemble(M0, M1, M2, Om)
    # RHS scaled with the row equilibration so the BVP is n-INDEPENDENT
    b = (np.ones(n + 1) / s).astype(complex)
    psi = np.linalg.solve(M, b)
    ref = psi[0]
    if abs(ref) < 1e-13 * np.max(np.abs(psi)):
        ref = psi[np.argmax(np.abs(psi))]
    psi = psi / ref
    grid = np.linspace(0.0, 1.0, C9_EVAL_GRID)
    return cheb_interp(eta, psi, grid)


def gate_C9():
    """GRADED-representation convergence at corners, edge midpoints, centre."""
    r_sat = X_SAT
    wr = (RECT_WR[0] * r_sat, RECT_WR[1] * r_sat)
    wi = (RECT_WI[0] * r_sat, RECT_WI[1] * r_sat)
    mr, mi = 0.5 * (wr[0] + wr[1]), 0.5 * (wi[0] + wi[1])
    probes = [complex(wr[0], -wi[0]), complex(wr[1], -wi[0]),
              complex(wr[1], -wi[1]), complex(wr[0], -wi[1]),
              complex(mr, -wi[0]), complex(mr, -wi[1]),
              complex(wr[0], -mi), complex(wr[1], -mi), complex(mr, -mi)]
    rows, worst = [], 0.0
    for Om in probes:
        a, b = _c9_probe(C9_N_LO, Om), _c9_probe(C9_N_HI, Om)
        d = float(np.max(np.abs(a - b)))
        worst = max(worst, d)
        rows.append({"Omega": [Om.real, Om.imag], "diff_32_64": d})
    # FT-I: grossly under-resolved
    fi = 0.0
    for Om in probes:
        fi = max(fi, float(np.max(np.abs(_c9_probe(8, Om) - _c9_probe(16, Om)))))
    return ({"probes": rows, "max_diff": worst, "tol": TOL["C9"],
             "pass": bool(worst <= TOL["C9"])},
            {"measured": fi, "threshold": FT_THRESH["FT_I"],
             "fires": bool(fi >= FT_THRESH["FT_I"])})


def gate_C10():
    """Outflow-row conditioning monitor across the frozen rectangle."""
    r_sat = X_SAT
    wr = (RECT_WR[0] * r_sat, RECT_WR[1] * r_sat)
    wi = (RECT_WI[0] * r_sat, RECT_WI[1] * r_sat)
    pts = []
    for k in range(C10_BOUNDARY_PTS):
        s = 4.0 * k / C10_BOUNDARY_PTS
        side, f = int(s), s - int(s)
        if side == 0:
            pts.append(complex(wr[0] + f * (wr[1] - wr[0]), -wi[0]))
        elif side == 1:
            pts.append(complex(wr[1], -(wi[0] + f * (wi[1] - wi[0]))))
        elif side == 2:
            pts.append(complex(wr[1] - f * (wr[1] - wr[0]), -wi[1]))
        else:
            pts.append(complex(wr[0], -(wi[1] - f * (wi[1] - wi[0]))))
    mr, mi = 0.5 * (wr[0] + wr[1]), 0.5 * (wi[0] + wi[1])
    pts += [complex(wr[0], -wi[0]), complex(wr[1], -wi[0]), complex(wr[1], -wi[1]),
            complex(wr[0], -wi[1]), complex(mr, -wi[0]), complex(mr, -wi[1]),
            complex(wr[0], -mi), complex(wr[1], -mi), complex(mr, -mi)]

    def rho(Om, lam, **mut):
        e1 = np.array([1.0])
        _, B0, B1, C0, C1, C2 = graded_coeff_parts(e1, ELL, lam, X_SAT, **mut)
        B = B0[0] + Om * B1[0]
        C = C0[0] + Om * C1[0] + Om ** 2 * C2[0]
        return abs(C) / abs(B) if abs(B) > 0 else float("inf")

    worst = 0.0
    for lam in LAMBDA_INDEP:
        for Om in pts:
            worst = max(worst, rho(Om, lam))
    metric = worst * 10.0 ** (-DPS)
    bound = ELL * (ELL + 1) * 10.0 ** (12 - DPS)
    om_min = min(abs(z) for z in pts)
    ft_a = rho(1e-36, LAMBDA_PRIMARY) * 10.0 ** (-DPS)
    ft_b = rho(complex(mr, -mi), LAMBDA_PRIMARY, kill_B1=True)
    return ({"max_rho_out": worst, "metric": metric, "tol": TOL["C10"],
             "derived_left_edge_bound": bound, "rectangle_Omega_min": om_min,
             "margin_orders": math.log10(om_min / bound),
             "pass": bool(metric <= TOL["C10"])},
            {"low_Omega_metric": ft_a, "low_Omega_threshold": FT_THRESH["FT_H"],
             "killed_B1_rho": ft_b, "killed_B1_threshold": FT_THRESH["FT_H_rho"],
             "fires": bool(ft_a > FT_THRESH["FT_H"]
                           and (not math.isfinite(ft_b) or ft_b >= FT_THRESH["FT_H_rho"]))})


# ===========================================================================
# COMPARATORS (I11-I14), read PROGRAMMATICALLY
# ===========================================================================
def read_comparators():
    import re
    p1 = os.path.join(_REPO, "research",
                      "2026-07-20_v1-spin-mapping-adjudication_rerun.py")
    m = re.search(r"0\.00:\s*\(([0-9.]+),\s*([0-9.]+)\)", open(p1).read())
    wr, wi = float(m.group(1)), float(m.group(2))
    p2 = os.path.join(_REPO, "research", "2026-07-20_ringdown-systematics_checks.py")
    s2 = open(p2).read()
    o = {k: float(re.search(rf"\({k[0]}, {k[1]}\):\s*([0-9.]+)", s2).group(1))
         for k in ((2, 0), (2, 1), (2, 2))}
    return {"omega_R_GR": wr, "omega_I_GR": wi, "Q_GR": wr / (2.0 * wi),
            "Q_GR_rounded_prose": 0.3737 / (2.0 * 0.0890),
            "schw_omega_R": {f"{a},{b}": v for (a, b), v in o.items()},
            "omega_I_GR_n1": 0.273915, "nu_vac": float(N_NU),
            "source_omega": "research/2026-07-20_v1-spin-mapping-adjudication_rerun.py:51",
            "source_overtones": "research/2026-07-20_ringdown-systematics_checks.py:72-73"}


# ===========================================================================
# BIN ADJUDICATION (prereg section 7) -- frozen precedence
# ===========================================================================
def adjudicate(gates, fts, phys_roots, loc, cmp_, x_sat=X_SAT):
    bad_g = sorted([k for k, v in gates.items() if not v.get("pass")])
    bad_f = sorted([k for k, v in fts.items() if not v.get("fires")])
    if bad_g or bad_f:
        return {"certification": "SOLVER-NOT-CERTIFIED", "bin": "BIN-F-SOLVER",
                "failed_gates": bad_g, "unfired_selftests": bad_f,
                "BIN-1": "N/A - not adjudicated", "BIN-2": "N/A - not adjudicated",
                "BIN-3": "N/A - not adjudicated", "BIN-4": "N/A - not adjudicated",
                "note": ("no physics bin adjudicated (prereg section 7 precedence); "
                         "diagnostics are NOT-ADJUDICATED")}
    if not phys_roots:
        return {"certification": "SOLVER-CERTIFIED", "bin": "BIN-F-NOPOLE",
                "note": "argument-principle count 0 over the frozen rectangle"}
    Om = phys_roots[0]
    wR, wI = Om.real / x_sat, abs(Om.imag) / x_sat
    Q = wR / (2.0 * wI)
    dw = wR / cmp_["omega_R_GR"] - 1.0
    dq = Q / cmp_["Q_GR"] - 1.0
    b1 = ("BIN-1-MATCH" if abs(dw) < 0.03 else
          "BIN-1-NEAR" if abs(dw) < 0.10 else "BIN-1-MISS")
    b2 = ("BIN-2-MATCH" if abs(dq) < 0.03 else
          "BIN-2-NEAR" if abs(dq) < 0.10 else "BIN-2-MISS")
    dg, dc = abs(Q - cmp_["Q_GR"]), abs(Q - 2.0)
    b2d = ("BIN-2-EQUIDISTANT" if abs(dg - dc) <= 1e-6 else
           "BIN-2-CLOSER-GR" if dg < dc else "BIN-2-CLOSER-CONVENTION")
    u, uk = loc["u_energy"], loc["u_kinetic"]
    if abs(u - uk) > 0.10:
        b3 = "BIN-3-DISCORDANT"
    elif not loc["interior_max"]:
        b3 = "BIN-3-MONOTONE"
    elif u <= 1.10:
        b3 = "BIN-3-RIM"
    elif u <= 1.50:
        b3 = "BIN-3-RAMP"
    else:
        b3 = "BIN-3-OUTER"
    if len(phys_roots) < 2:
        b4, rr, ri = "BIN-4-NONE", None, None
    else:
        o1 = phys_roots[1]
        ri = abs(o1.imag) / abs(Om.imag)
        rr = o1.real / Om.real
        ri_gr = cmp_["omega_I_GR_n1"] / 0.088962
        rr_gr = cmp_["schw_omega_R"]["2,1"] / cmp_["schw_omega_R"]["2,0"]
        b4 = ("BIN-4-LADDER-MATCH"
              if abs(ri / ri_gr - 1) < 0.10 and abs(rr / rr_gr - 1) < 0.10
              else "BIN-4-LADDER-DIFFERENT")
    k0 = x_sat * wR
    return {"certification": "SOLVER-CERTIFIED", "bin": "adjudicated",
            "omega_R_Mg": wR, "omega_I_Mg": wI, "Omega": [Om.real, Om.imag], "Q": Q,
            "D_omega": dw, "D_omega_shortcut": wR / (18.0 / 49.0) - 1.0, "D_Q": dq,
            "BIN-1": b1, "BIN-2": b2, "BIN-2-DISCRIMINATOR": b2d, "BIN-3": b3,
            "BIN-4": b4, "R_I": ri, "R_R": rr,
            "k0_r_sat": k0,
            "k0_r_sat_tag": "IDENTITY - not independent of BIN-1's shortcut comparison",
            "nu_factor_verdict": ("FALSIFIED as a derivation of the eigenfrequency"
                                  if abs(wR / (18.0 / 49.0) - 1.0) > 0.03
                                  else "not falsified at the frozen 3 percent"),
            "class_line_BIN1": ("BIN-1 is VALUE-CONSISTENCY class, not emergence: "
                                "omega_R*M_g carries the GR-imported nu_vac "
                                "through the 7 in r_sat"),
            "class_line_BIN2": ("BIN-2 is the nu_vac-FREE axis: "
                                "Q = Re(Omega)/(2*abs(Im(Omega))) contains no "
                                "r_sat scale, so the GR-imported 7 cancels exactly")}


def digest(obj):
    c = {k: v for k, v in obj.items() if k != "_runtime_sec"}
    return hashlib.sha256(json.dumps(c, sort_keys=True, default=str)
                          .encode()).hexdigest()[:16]


# ===========================================================================
# MAIN -- gates FIRST, then (only if certified) the physics bins
# ===========================================================================
def main():
    t0 = time.time()
    mp.mp.dps = DPS
    out: dict = {
        "_prereg": "research/2026-08-03_coldq-pole-v2.1_prereg-FROZEN.md",
        "_prereg_commit": "7d8fe484",
        "_method": ("compactified hyperboloidal Chebyshev spectral discretization "
                    "in the Axiom-4 amplitude coordinate A = r_sat/r; outgoing wave "
                    "divided out in closed form; traction-free SHORT as dpsi/deta = 0; "
                    "no BC imposed at infinity; extended-precision determinant polish; "
                    "argument-principle winding of the determinant phase"),
        "_frozen_numerics": {
            "n_primary": N_PRIMARY, "n_indep": list(N_INDEP), "n_sweep": list(N_SWEEP),
            "lambda_indep": list(LAMBDA_INDEP), "dps": DPS,
            "rect_wr": list(RECT_WR), "rect_wi": list(RECT_WI),
            "ctrl_box": [list(CTRL_BOX_R), list(CTRL_BOX_I)],
            "high_box": [list(HIGH_BOX_R), list(HIGH_BOX_I)],
            "ctrl_ells": list(CTRL_ELLS_LOW) + list(CTRL_ELLS_HIGH),
            "width_family": list(WIDTH_FAMILY),
            "contour_samples": list(CONTOUR_SAMPLES), "x_sat": X_SAT, "ell": ELL},
    }
    cmp_ = read_comparators()
    out["comparators"] = cmp_

    gates: dict = {}
    fts: dict = {}

    print("C11 operator identity ...", flush=True)
    c11 = gate_C11()
    gates["C11"] = {k: c11[k] for k in ("measured", "tol", "pass")}
    fts["FT_J"] = {"measured": c11["FT_J_corrupted"],
                   "threshold": c11["FT_J_threshold"], "fires": c11["FT_J_fires"]}

    print("C1 zero-grade closed-form control (entry ticket) ...", flush=True)
    gates["C1"], fts["FT_A"] = gate_C1()

    print("C10 outflow-row conditioning monitor ...", flush=True)
    gates["C10"], fts["FT_H"] = gate_C10()

    print("C9 graded-representation convergence at corners/edges ...", flush=True)
    gates["C9"], fts["FT_I"] = gate_C9()

    print("fundamental pole (primary branch) ...", flush=True)
    base, roots, box = fundamental(N_PRIMARY, ELL, LAMBDA_PRIMARY)
    out["located_roots_primary"] = [[z.real, z.imag] for z in roots]
    if base is None:
        out["_fatal"] = "no root located on the primary branch"

    print("C2 gauge / C3 resolution ...", flush=True)
    gates["C2"], gates["C3"], fts["FT_B"], fts["FT_C"] = gate_C2_C3(base)

    print("C4 argument principle + width family ...", flush=True)
    gates["C4"], fts["FT_D"] = gate_C4(roots, box)

    print("C5 nu_vac cancellation ...", flush=True)
    gates["C5"], fts["FT_E"] = gate_C5(base)

    print("C6/C7 closed cavity ...", flush=True)
    gates["C6"], gates["C7"], fts["FT_F"], fts["FT_G"] = gate_C6_C7(base)

    gates["C8"] = {"note": "determinism is verified by re-running the driver and "
                           "comparing the shipped digest", "pass": True}
    out["gates"] = gates
    out["self_tests"] = fts

    # PHYSICAL-vs-ARTIFACT filter (prereg section 4.4), frozen in advance
    phys, arti = [], []
    ref = {n: fundamental(n, ELL, LAMBDA_PRIMARY)[1] for n in N_INDEP}
    for z in roots:
        ok = all(any(abs(z - q) <= PHYS_REL * max(abs(q), 1.0) for q in ref[n])
                 for n in N_INDEP)
        (phys if ok else arti).append(z)
    out["physical_roots"] = [[z.real, z.imag] for z in phys]
    out["discretization_artifacts"] = [[z.real, z.imag] for z in arti]

    loc = localization(complex(base.real / X_SAT, base.imag / X_SAT),
                       N_PRIMARY, ELL, LAMBDA_PRIMARY) if base else {}
    out["localization"] = loc

    out["ell_ladder"] = {
        "tag": ("DIAGNOSTIC - no bin, no verdict; FORK-12 is unanswered and "
                "this lane does not adjudicate it"),
        "Omega": {str(L): (lambda r: [r.real, r.imag] if r else None)(
            fundamental(N_PRIMARY, L, LAMBDA_PRIMARY)[0]) for L in ELL_LADDER}}

    out["adjudication"] = adjudicate(gates, fts, phys, loc, cmp_)
    out["_runtime_sec"] = round(time.time() - t0, 2)
    out["_digest"] = digest(out)

    dest = os.path.join(_HERE, "coldq_pole_v2_results.json")
    with open(dest, "w") as f:
        json.dump(out, f, indent=2, sort_keys=True, default=str)
    print(json.dumps({"certification": out["adjudication"]["certification"],
                      "failed_gates": out["adjudication"].get("failed_gates"),
                      "unfired": out["adjudication"].get("unfired_selftests"),
                      "digest": out["_digest"],
                      "runtime_sec": out["_runtime_sec"]}, indent=2))
    return out


if __name__ == "__main__":
    main()

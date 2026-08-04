#!/usr/bin/env python3
"""Cold-Q pole v2.2 -- ROOT CERTIFICATION of a single located pole.

Resolves the frozen gates and bins of
``research/2026-08-03_coldq-pole-v2.2-root_prereg-FROZEN.md`` (commit
f15a6e4d, pushed ALONE BEFORE this file existed and before any number
produced by this instrument existed).

TARGET (prereg section 1).  Certification of the SINGLE located root of the
graded spin-2 hyperboloidal problem near

    Omega_0 = 1.8536552108408788 - 1.0072567831433188j

NON-CLAIM (prereg section 1.2, frozen).  "this lane asserts the existence and
location of THIS root; it asserts NOTHING about the absence or presence of
other modes".  NO argument-principle winding, NO contour integral and NO
region count is computed anywhere in this file.  BIN-4 is N/A BY CONSTRUCTION.

METHOD (prereg section 4.1, frozen).  Compactified hyperboloidal Chebyshev
spectral discretization in the Axiom-4 amplitude coordinate A = r_sat/r with
the outgoing wave divided out in closed form, the traction-free SHORT imposed
exactly as dpsi/deta = 0 at eta = 0, no boundary condition imposed at
infinity, root extraction by extended-precision determinant polish seeded from
the double-precision linearized pencil, and eigenfunction extraction by
extended-precision inverse iteration.

REIMPLEMENTATION DISCLOSURE (prereg section 2.3, frozen).  This file is an
INDEPENDENT REIMPLEMENTATION.  ``research/drivers/coldq_pole_v2.py`` (the
concurrent PR #854 repair lane's driver) is neither imported nor edited nor
executed here.  Algebraic forms and routine shapes transcribed from it carry
an ATTRIBUTION comment at the transcription site, marked ``[xcribe v2.1 ...]``.

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
# FROZEN NUMERICS (prereg section 4.2) -- ENGINEERING CHOICE, tagged (I19)
# ===========================================================================
N_PRIMARY = 48
N_LADDER = (32, 48, 64, 80, 96)
LAMBDA_PRIMARY = 0.0
LAMBDA_SET = (-0.25, 0.0, 0.25)
DPS = 50
DPS_HIGH = 80
DPS_FT4 = 20                     # FT-4(a) mutation
POLISH_TOL_EXP = 38
POLISH_ITERS = 60
INVIT_ROUNDS = 4                 # mp inverse-iteration rounds
DEDUPE_REL = 1e-6
R_ISO = 0.5                      # prereg section 4.3, DERIVED then frozen
X_SAT = 7.0                      # I1
X_SAT_SET = (5.0, 7.0, 11.0)
ELL = 2                          # I8
LOC_WINDOW = (1.0, 2.0)          # r/r_sat, BIN-3
LOC_POINTS = 401
N_UNDER = 8                      # FT-2 / FT-4(b) under-resolved order
RUNTIME_BUDGET_S = 3600.0

# I15 -- PRIOR-LANE SEED.  Transcribed from
#   research/drivers/coldq_pole_v2_results.json @ commit bdcfa678
#   (branch research/coldq-pole-v2, PR #854, OPEN/DO-NOT-MERGE; the file is
#    NOT on origin/main, which is why it is transcribed rather than read).
# SEED ONLY: it selects WHICH pencil eigenvalue is polished and enters no
# gate, tolerance, comparator or bin as a value (prereg section 1.1, frozen).
OMEGA_SEED = 1.8536552108408788 - 1.0072567831433188j

# I17 -- PRIOR-LANE DISCRETIZATION ARTIFACT, banked by v2.1's own frozen
# physical-vs-artifact criterion.  FT-5(a) fireability target ONLY.
OMEGA_ARTIFACT = 0.30587571217415294 - 2.4674822214282157j

# I18 -- PRIOR-LANE contaminated-left-edge probe (a v2.1 C9 probe point).
# FT-5(b) fireability target ONLY.
OMEGA_EDGE = 0.1400 - 3.5035j

# I16 -- v1 comparator source (PR #845, MERGED at 052ccbba).  Read
# PROGRAMMATICALLY at run time; nothing about it is typed here.
V1_JSON = os.path.join(_HERE, "coldq_pole_derivation_results.json")

# I11 / I12 / I13 -- GR comparators, read PROGRAMMATICALLY at run time.
RERUN_PY = os.path.join(_REPO, "research",
                        "2026-07-20_v1-spin-mapping-adjudication_rerun.py")
RINGDOWN_PY = os.path.join(_REPO, "research",
                           "2026-07-20_ringdown-systematics_checks.py")

# FROZEN tolerances (prereg section 5)
TOL = {
    "G0": 1e-13,
    "G1": 1e-20,
    "G2": 1e-10,
    "G3": 1e-12,
    "G4a": 1e-25,
    "G4b": 1e-6,
    "G6": 1e-5,
    "G7": 1e-3,
    "G8": 1e-9,
    "G10a": 1e-40,
    "G10b": 1e-20,
}
FT_THRESH = {
    "FT_0": 1e-13,
    "FT_1": 1e-15,
    "FT_2": 1e-6,
    "FT_3": 1e-6,
    "FT_4a": 1e-25,
    "FT_4b": 1e-6,
    "FT_6": 1e-5,
    "FT_7": 1e-3,       # REVERSE: both null differences MUST be BELOW this
    "FT_8": 1e-9,
    "FT_10a": 1e-6,
    "FT_10b": 1e-5,
}
FT_MUT = {
    "FT_0_corrupt": 1e-12,
    "FT_1_offset": 1e-10,
    "FT_3_lambda": 0.25,
    "FT_6_corrupt": 1e-3,
    "FT_8_perturb": 1e-6,
    "FT_9_perturb": 1e-15,
    "FT_10_loss": 1e-3,
}


# ===========================================================================
# CHEBYSHEV -- double precision
# [xcribe v2.1 coldq_pole_v2.py::cheb -- standard CGL differentiation matrix,
#  ASCENDING on [0,1]; transcribed for behavioural parity of the seeding path]
# ===========================================================================
def cheb(n: int):
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
            out[i] = np.sum(w / d * vals) / np.sum(w / d)
    return out


_CHEB_MP: dict = {}


def cheb_mp(n: int, dps: int = DPS):
    """CGL nodes + D + D2 built ENTIRELY in mp (the B1 lesson of v2.1: mp
    arithmetic on a double-precision operator polishes the DOUBLE operator's
    root, not the continuous problem's)."""
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


# ===========================================================================
# THE GRADED OPERATOR (prereg section 2.2)
#   A = r_sat/r = 1 - eta^2 ;  W = A exp(i Om (1/A + lam A)) psi
#   M(Om) = M0 + Om M1 + Om^2 M2 ; row 0 is the exact SHORT dpsi/deta(0) = 0
#
# [xcribe v2.1 coldq_pole_v2.py::graded_coeff_parts -- the eta-form
#  coefficient algebra.  It is re-verified here as an operator identity by
#  gate G0 rather than trusted.]
#
# MUTATION HOOKS, each tied to exactly one frozen self-test:
#   spin1_wall    -> G7(a)   corrupt_C0 -> FT-0 / FT-6
#   omit_lam_C2   -> FT-3    perturb_A  -> FT-8      loss -> FT-10
# The coefficient path carries r_sat EXPLICITLY (r = x_sat / A) so different
# x_sat produce different floating-point intermediates -- the G8
# arithmetic-fidelity requirement.
# ===========================================================================
def graded_coeff_parts(eta, ell, lam, x_sat=X_SAT, perturb_A=0.0,
                       corrupt_C0=0.0, omit_lam_C2=False, loss=0.0):
    r_sat = float(x_sat)
    A0 = 1.0 - eta ** 2
    with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
        # The eta = 1 node IS the compactified infinity (A = 0); the explicit
        # r_sat round trip sends it through r -> inf and back to A = 0 exactly.
        r_phys = r_sat / np.where(A0 == 0.0, np.finfo(float).tiny, A0)
        A = r_sat / r_phys                  # == A0, via the explicit r_sat path
    A = A * (1.0 + perturb_A)
    two = 2.0 - eta ** 2
    u = np.sqrt(two)
    S = eta * u
    Asq = A ** 2
    B0 = -eta * Asq / two - 4.0 * eta * A
    B1 = 4j * eta - 4j * lam * Asq * eta
    C0 = (-4.0 * ell * (ell + 1) * eta ** 2 - 8.0 * Asq / two) \
        * (1.0 + corrupt_C0)
    C1 = 4j * A / two + 8j * lam * eta ** 2 * A - 4j * lam * A ** 3 / two
    # C2's FIRST term is the Om^2 rho/mu term: a constant complex factor on mu
    # enters HERE and nowhere else (prereg FT-10 non-vacuity argument).
    C2_mu = 4.0 * eta / (u * (1.0 + S))
    if loss:
        C2_mu = C2_mu / (1.0 + 1j * loss)
    C2_lam = 0.0 if omit_lam_C2 else (8.0 * eta ** 2 * lam
                                      - 4.0 * eta ** 2 * lam ** 2 * Asq)
    return Asq, B0, B1, C0, C1, C2_mu + C2_lam


def graded_matrices(n, ell, lam, x_sat=X_SAT, spin1_wall=False, **mut):
    """Double-precision operator parts.  SEEDING + G4(b) + G5 path."""
    eta, D = cheb(n)
    D2 = D @ D
    Acoef, B0, B1, C0, C1, C2 = graded_coeff_parts(eta, ell, lam, x_sat, **mut)
    M0 = Acoef[:, None] * D2 + B0[:, None] * D + np.diag(C0).astype(complex)
    M1 = B1[:, None] * D + np.diag(C1).astype(complex)
    M2 = np.diag(C2).astype(complex)
    if spin1_wall:
        # G7(a): the SPIN-1 wall condition W_r(r_sat) = 0 in place of the
        # spin-2 T(r_sat) = 0.  With W = A E psi this is
        #   [1 + i Om (lam - 1)] psi(0) - psi_etaeta(0)/2 = 0
        # -- a genuinely DIFFERENT condition, not a rescaling of the same row.
        # [xcribe v2.1 coldq_pole_v2.py::graded_matrices spin1_wall branch]
        M0[0, :] = -0.5 * D2[0, :]
        M0[0, 0] += 1.0
        M1[0, :] = 0.0
        M1[0, 0] = 1j * (lam - 1.0)
        M2[0, :] = 0.0
    else:
        M0[0, :] = D[0, :]
        M1[0, :] = 0.0
        M2[0, :] = 0.0
    s = np.maximum.reduce([np.abs(M0).max(1), np.abs(M1).max(1),
                           np.abs(M2).max(1)])
    s[s == 0] = 1.0
    return M0 / s[:, None], M1 / s[:, None], M2 / s[:, None], eta, D


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


def graded_matrices_mp(n, ell, lam, x_sat=X_SAT, dps=DPS, spin1_wall=False,
                       perturb_A=0.0, corrupt_C0=0.0, omit_lam_C2=False,
                       loss=0.0):
    """The mp operator.  EVERY gate value is read from THIS object."""
    mp.mp.dps = dps
    eta, D, D2 = cheb_mp(n, dps)
    N = n + 1
    r_sat = mp.mpf(x_sat)
    lm = mp.mpf(lam)
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
        C0 = (-4 * ell * (ell + 1) * e ** 2 - 8 * Asq / two) \
            * (1 + mp.mpf(corrupt_C0))
        C1 = (mp.mpc(0, 4) * A / two + mp.mpc(0, 8) * lm * e ** 2 * A
              - mp.mpc(0, 4) * lm * A ** 3 / two)
        C2 = 4 * e / (u * (1 + S))
        if loss:
            C2 = C2 / (1 + mp.mpc(0, 1) * mp.mpf(loss))
        if not omit_lam_C2:
            C2 = C2 + 8 * e ** 2 * lm - 4 * e ** 2 * lm ** 2 * Asq
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
            M0[0, j] = D[0, j]
    return _equil_mp(M0, M1, M2)


# ===========================================================================
# DOUBLE-PRECISION LINEARIZED PENCIL -- the SEEDING path and the G5 object
# [xcribe v2.1 coldq_pole_v2.py::pencil_spectrum -- the companion
#  linearization of the quadratic pencil M0 + Om M1 + Om^2 M2]
# ===========================================================================
def pencil_spectrum(M0, M1, M2):
    N = M0.shape[0]
    Z, Eye = np.zeros((N, N), dtype=complex), np.eye(N)
    ev = sla.eig(np.block([[M0, Z], [Z, Eye]]),
                 np.block([[-M1, -M2], [Eye, Z]]), right=False)
    return np.array([z for z in ev if np.isfinite(z) and abs(z) < 1e8])


def dedupe(vals, rel=DEDUPE_REL):
    out = []
    for z in vals:
        if not any(abs(z - q) <= rel * max(abs(q), 1.0) for q in out):
            out.append(z)
    return out


# ===========================================================================
# EXTENDED-PRECISION DETERMINANT, LU AND POLISH
# ===========================================================================
def mp_assemble(M0, M1, M2, om):
    n = M0.rows
    o = mp.mpc(om)
    o2 = o * o
    A = mp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            A[i, j] = M0[i, j] + o * M1[i, j] + o2 * M2[i, j]
    return A


def mp_det(M0, M1, M2, om):
    """LU with partial pivoting; never a product of unpivoted pivots."""
    A = mp_assemble(M0, M1, M2, om)
    n = A.rows
    d = mp.mpc(1)
    for k in range(n):
        p = max(range(k, n), key=lambda r: abs(A[r, k]))
        if p != k:
            for j in range(k, n):
                A[k, j], A[p, j] = A[p, j], A[k, j]
            d = -d
        piv = A[k, k]
        if piv == 0:
            return mp.mpc(0)
        d *= piv
        for i in range(k + 1, n):
            f = A[i, k] / piv
            for j in range(k, n):
                A[i, j] -= f * A[k, j]
    return d


def mp_lu(A):
    """In-place LU with partial pivoting; returns (LU, perm)."""
    n = A.rows
    perm = list(range(n))
    for k in range(n):
        p = max(range(k, n), key=lambda r: abs(A[r, k]))
        if p != k:
            for j in range(n):
                A[k, j], A[p, j] = A[p, j], A[k, j]
            perm[k], perm[p] = perm[p], perm[k]
        piv = A[k, k]
        if piv == 0:
            piv = mp.mpf(10) ** (-2 * mp.mp.dps)
            A[k, k] = piv
        for i in range(k + 1, n):
            f = A[i, k] / piv
            A[i, k] = f
            for j in range(k + 1, n):
                A[i, j] -= f * A[k, j]
    return A, perm


def mp_lu_solve(LU, perm, b):
    n = LU.rows
    y = [b[perm[i]] for i in range(n)]
    for i in range(n):
        for j in range(i):
            y[i] -= LU[i, j] * y[j]
    x = [mp.mpc(0)] * n
    for i in range(n - 1, -1, -1):
        s = y[i]
        for j in range(i + 1, n):
            s -= LU[i, j] * x[j]
        x[i] = s / LU[i, i]
    return x


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


# ===========================================================================
# THE ROOT -- seeded from the double pencil eigenvalue NEAREST the frozen seed
# (prereg section 1.1, frozen).  Memoized on the EXACT argument tuple: a pure
# performance optimization with ZERO numerical effect (no RNG, no adaptivity).
# ===========================================================================
_ROOT_CACHE: dict = {}


def _mut_key(mut):
    return tuple(sorted(mut.items()))


def pencil_at(n, ell=ELL, lam=LAMBDA_PRIMARY, x_sat=X_SAT, **mut):
    M0, M1, M2, _, _ = graded_matrices(n, ell, lam, x_sat, **mut)
    return dedupe(list(pencil_spectrum(M0, M1, M2)))


def nearest(vals, target):
    if not len(vals):
        return None
    return min(vals, key=lambda z: abs(z - target))


def root(n, lam=LAMBDA_PRIMARY, x_sat=X_SAT, dps=DPS, ell=ELL,
         seed=OMEGA_SEED, n_double=None, **mut):
    """Polished root: seed -> nearest double pencil eigenvalue -> mp secant."""
    ck = (n, lam, x_sat, dps, ell, seed, n_double, _mut_key(mut))
    if ck in _ROOT_CACHE:
        return _ROOT_CACHE[ck]
    nd = n if n_double is None else n_double
    spec = pencil_at(nd, ell, lam, x_sat, **mut)
    s = nearest(spec, seed)
    if s is None:
        _ROOT_CACHE[ck] = (None, None, spec)
        return _ROOT_CACHE[ck]
    P0, P1, P2 = graded_matrices_mp(n, ell, lam, x_sat, dps, **mut)
    r = mp_polish(P0, P1, P2, s, dps)
    _ROOT_CACHE[ck] = (r, complex(s), spec)
    return _ROOT_CACHE[ck]


def relsep(a, b):
    """Relative separation of two mp complex numbers, computed IN MP and cast
    to float ONLY at the end (the v2.1 R6 lesson: casting the ROOT to a
    double-precision complex before differencing reports anything below
    ~1e-16 as exactly 0.0)."""
    return float(abs(a - b) / abs(a))


# ===========================================================================
# THE CERTIFIED EIGENFUNCTION -- mp inverse iteration from the ALL-ONES vector
# ===========================================================================
def eigenfunction(n, om, lam=LAMBDA_PRIMARY, x_sat=X_SAT, dps=DPS, ell=ELL,
                  rounds=INVIT_ROUNDS, **mut):
    """Returns (psi as an mp list, residual max|M psi|/max|psi|)."""
    mp.mp.dps = dps
    P0, P1, P2 = graded_matrices_mp(n, ell, lam, x_sat, dps, **mut)
    A = mp_assemble(P0, P1, P2, om)
    LU, perm = mp_lu(mp.matrix(A))
    v = [mp.mpc(1)] * (n + 1)
    for _ in range(rounds):
        v = mp_lu_solve(LU, perm, v)
        m = max(abs(z) for z in v)
        v = [z / m for z in v]
    r = [sum(A[i, j] * v[j] for j in range(n + 1)) for i in range(n + 1)]
    resid = max(abs(z) for z in r) / max(abs(z) for z in v)
    return v, resid


def residual_at(n, om, psi, lam=LAMBDA_PRIMARY, x_sat=X_SAT, dps=DPS,
                ell=ELL, **mut):
    """Residual of a GIVEN psi on M(om) -- FT-1 uses this off-root."""
    mp.mp.dps = dps
    P0, P1, P2 = graded_matrices_mp(n, ell, lam, x_sat, dps, **mut)
    A = mp_assemble(P0, P1, P2, om)
    r = [sum(A[i, j] * psi[j] for j in range(n + 1)) for i in range(n + 1)]
    return float(max(abs(z) for z in r) / max(abs(z) for z in psi))


# ===========================================================================
# MODE PROFILE + ENERGY FUNCTIONAL (BIN-3 and G7(b))
#
# DISCLOSED CAST.  The certified eigenfunction is computed in mp (above); for
# the localization argmax and the energy RATIO it is cast to double precision
# here.  Both observables are argmax / ratio reads adjudicated at the 1e-3 and
# 1e-1 class, so the cast is immaterial to them -- and it is confined to THIS
# function.  It does NOT touch G1, G2, G3, G4, G8 or G10, each of which stays
# mp end-to-end.  (The v2.1 R6 defect was exactly a cast on the G8 path.)
# ===========================================================================
def mode_profile(n, Om, psi, lam=LAMBDA_PRIMARY, x_sat=X_SAT, ell=ELL):
    eta, D = cheb(n)
    p_nodes = np.array([complex(z) for z in psi])
    dpsi = D @ p_nodes
    a_lo = 1.0 / LOC_WINDOW[1]
    e_hi = math.sqrt(1.0 - a_lo)
    grid = np.linspace(0.0, e_hi, LOC_POINTS)
    p = cheb_interp(eta, p_nodes, grid)
    dp = cheb_interp(eta, dpsi, grid)
    A = 1.0 - grid ** 2
    r = x_sat / A
    E = np.exp(1j * Om * (1.0 / A + lam * A))
    W = A * E * p
    # psi_A = psi_eta / (dA/deta) = psi_eta / (-2 eta).  At eta = 0 the exact
    # SHORT gives psi_eta(0) = 0, and mu(0) = 0 kills the strain term there, so
    # the endpoint value is set to 0 and cannot influence any reported number.
    psi_A = np.where(grid == 0.0, 0.0, dp / (-2.0 * np.maximum(grid, 1e-300)))
    W_A = E * (p + 1j * Om * (lam * A - 1.0 / A) * p + A * psi_A)
    W_r = -(A ** 2 / x_sat) * W_A
    mu = np.sqrt(np.maximum(1.0 - A ** 2, 0.0))
    om = Om / x_sat
    e_kin = np.abs(om) ** 2 * np.abs(W) ** 2 * r ** 2
    return grid, r, W, W_r, mu, e_kin


def strain_density(W, W_r, mu, r, weight):
    return mu * (np.abs(W_r - W / r) ** 2
                 + weight * np.abs(W) ** 2 / r ** 2) * r ** 2


def localization(n, Om, psi, lam=LAMBDA_PRIMARY, x_sat=X_SAT, ell=ELL):
    grid, r, W, W_r, mu, e_kin = mode_profile(n, Om, psi, lam, x_sat, ell)
    e_str = strain_density(W, W_r, mu, r, (ell - 1) * (ell + 2))
    e_tot = e_kin + e_str
    u_all = r / x_sat
    i_e, i_k = int(np.argmax(e_tot)), int(np.argmax(e_kin))
    return {
        "u_energy": float(u_all[i_e]),
        "u_kinetic": float(u_all[i_k]),
        "interior_max": bool(0 < i_e < len(grid) - 1),
        "wall_fraction_of_peak": float(e_tot[0] / np.max(e_tot)),
        "window": list(LOC_WINDOW),
    }


def strain_to_kinetic(n, Om, psi, weight, lam=LAMBDA_PRIMARY, x_sat=X_SAT,
                      ell=ELL):
    grid, r, W, W_r, mu, e_kin = mode_profile(n, Om, psi, lam, x_sat, ell)
    e_str = strain_density(W, W_r, mu, r, weight)
    return float(np.trapezoid(e_str, r) / np.trapezoid(e_kin, r))


# ===========================================================================
# COMPARATORS -- read PROGRAMMATICALLY (nothing below is typed)
# ===========================================================================
def _grab(path, pattern, group=1):
    import re
    with open(path, encoding="utf-8") as fh:
        m = re.search(pattern, fh.read())
    if not m:
        raise RuntimeError(f"comparator pattern not found in {path}: {pattern}")
    return float(m.group(group))


def comparators():
    """I11 / I12 / I13 / I16, each read from its in-repo carrier."""
    wr_gr = _grab(RERUN_PY, r"0\.00:\s*\(([0-9.]+),\s*[0-9.]+\)")     # I11
    wi_gr = _grab(RERUN_PY, r"0\.00:\s*\([0-9.]+,\s*([0-9.]+)\)")     # I11
    wr20 = _grab(RINGDOWN_PY, r"\(2,\s*0\):\s*([0-9.]+),")            # I12
    wr21 = _grab(RINGDOWN_PY, r"\(2,\s*1\):\s*([0-9.]+),")            # I12
    wi20 = _grab(RINGDOWN_PY, r"SCHW_OMEGA_I\s*=\s*\{\(2,\s*0\):\s*([0-9.]+)")
    wi21 = _grab(os.path.join(_HERE, "coldq_pole_derivation.py"),
                 r"OMEGA_I_GR_N1\s*=\s*([0-9.]+)")                    # I13
    with open(V1_JSON, encoding="utf-8") as fh:
        v1 = json.load(fh)
    rows = [r for r in v1["gates"]["G8"]["rows"] if r["x_sat"] == X_SAT]
    if len(rows) != 1:
        raise RuntimeError("v1 comparator row x_sat = 7.0 not uniquely found")
    om_v1 = X_SAT * (rows[0]["omega_R_M"] - 1j * rows[0]["omega_I_M"])
    return {
        "omega_R_GR": wr_gr, "omega_I_GR": wi_gr,
        "Q_GR": wr_gr / (2.0 * wi_gr),
        "Q_GR_rounded_prose": 0.3737 / (2.0 * 0.0890),
        "Q_convention": 2.0,
        "omega_R_shortcut": 18.0 / 49.0,
        "nu_vac": float(N_NU),
        "Omega_GR_n0": [X_SAT * wr20, -X_SAT * wi20],
        "Omega_GR_n1": [X_SAT * wr21, -X_SAT * wi21],
        "Omega_v1": [om_v1.real, om_v1.imag],
    }


def iso_receipts(cmp_):
    """prereg section 4.3 -- the four R_iso receipts, recomputed here."""
    g0 = complex(*cmp_["Omega_GR_n0"])
    g1 = complex(*cmp_["Omega_GR_n1"])
    gap = abs(g0 - g1)
    dart = abs(OMEGA_SEED - OMEGA_ARTIFACT)
    return {
        "R_iso": R_ISO,
        "GR_overtone_gap": gap,
        "GR_gap_over_R_iso": gap / R_ISO,
        "dist_seed_to_artifact": dart,
        "artifact_over_R_iso": dart / R_ISO,
        "abs_Omega_seed": abs(OMEGA_SEED),
        "R_iso_over_abs_Omega": R_ISO / abs(OMEGA_SEED),
        "R_iso_over_dedupe": R_ISO / (DEDUPE_REL * abs(OMEGA_SEED)),
    }


# ===========================================================================
# ISOLATION MEASUREMENT (G5 and FT-5) -- the SAME routine for both
# ===========================================================================
def isolation_row(n, seed, lam=LAMBDA_PRIMARY, x_sat=X_SAT, dps=DPS, **mut):
    r, s, spec = root(n, lam, x_sat, dps, seed=seed, **mut)
    if r is not None and abs(complex(r) - seed) <= R_ISO:
        centre = complex(r)
        polished = [float(r.real), float(r.imag)]
    else:
        centre = seed
        polished = None
    inside = [z for z in spec if abs(z - centre) <= R_ISO]
    return {
        "n": n,
        "polished": polished,
        "centre": [centre.real, centre.imag],
        "count_within_R_iso": len(inside),
        "inside": sorted([[z.real, z.imag] for z in inside],
                         key=lambda p: (p[0], p[1])),
        "pencil_total": len(spec),
    }


# ===========================================================================
# THE ROOT-LOCAL CERTIFICATION GATES (prereg section 5)
# Each gate's SELF-TEST is executed and recorded in the same block, BEFORE the
# gate's own measurement is read (prereg section 6 ordering rule).
# ===========================================================================
def gate_G0():
    """Operator-transcription identity: L_eta[psi] == 4 eta^2 L_A[psi]."""
    def LA(f, df, d2f, A, ell, Om, lam):
        S = math.sqrt(1.0 - A ** 2)
        gh = -A / (1.0 - A ** 2)
        P = -2j * Om + 2.0 * A + A ** 2 * gh + 2j * Om * lam * A ** 2
        Q = (Om ** 2 / (S * (1.0 + S)) - 1j * Om * gh - ell * (ell + 1)
             + 2.0 * A * gh
             + 1j * Om * lam * (-2j * Om + 2.0 * A + A ** 2 * gh)
             - Om ** 2 * lam ** 2 * A ** 2)
        return A ** 2 * d2f + P * df + Q * f

    worst, worst_c = 0.0, 0.0
    for lam in LAMBDA_SET:
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
                    for corrupt, slot in ((0.0, "ok"),
                                          (FT_MUT["FT_0_corrupt"], "bad")):
                        Ac, B0, B1, C0, C1, C2 = graded_coeff_parts(
                            ea, ell, lam, corrupt_C0=corrupt)
                        lhs = (Ac[0] * d2e + (B0[0] + Om * B1[0]) * de
                               + (C0[0] + Om * C1[0] + Om ** 2 * C2[0]) * f)
                        rhs = 4.0 * e ** 2 * LA(f, df, d2f, A, ell, Om, lam)
                        rel = abs(lhs - rhs) / max(abs(rhs), 1e-300)
                        if slot == "ok":
                            worst = max(worst, rel)
                        else:
                            worst_c = max(worst_c, rel)
    return ({"measured": worst, "tol": TOL["G0"], "pass": bool(worst <= TOL["G0"])},
            {"measured": worst_c, "threshold": FT_THRESH["FT_0"],
             "fires": bool(worst_c >= FT_THRESH["FT_0"]),
             "mutation": "C0 corrupted by 1e-12 relative"})


def gate_G1(om_star, psi):
    """Residual of the CERTIFIED EIGENFUNCTION at the certified root."""
    _, resid = eigenfunction(N_PRIMARY, om_star)
    off = om_star * (1 + mp.mpf(FT_MUT["FT_1_offset"]))
    ft = residual_at(N_PRIMARY, off, psi)
    return ({"measured": float(resid), "tol": TOL["G1"],
             "pass": bool(float(resid) <= TOL["G1"]),
             "dps": DPS, "n": N_PRIMARY, "invit_rounds": INVIT_ROUNDS},
            {"measured": ft, "threshold": FT_THRESH["FT_1"],
             "fires": bool(ft >= FT_THRESH["FT_1"]),
             "mutation": "residual evaluated at Omega_star*(1 + 1e-10)"})


def gate_G2(om_star):
    """n-INDEPENDENCE across the frozen ladder."""
    rows, vals = [], []
    for n in N_LADDER:
        r = root(n)[0]
        rows.append({"n": n, "Omega": [float(r.real), float(r.imag)]
                     if r is not None else None})
        if r is not None:
            vals.append(r)
    worst = 0.0
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            worst = max(worst, relsep(vals[i], vals[j]))
    ru = root(N_UNDER)[0]
    ft = relsep(om_star, ru) if ru is not None else float("inf")
    return ({"measured": worst, "tol": TOL["G2"], "ladder": list(N_LADDER),
             "rows": rows, "pass": bool(len(vals) == len(N_LADDER)
                                        and worst <= TOL["G2"])},
            {"measured": ft, "threshold": FT_THRESH["FT_2"],
             "fires": bool(ft >= FT_THRESH["FT_2"]),
             "mutation": f"under-resolved order n = {N_UNDER}"})


def gate_G3():
    """Hyperboloidal-gauge independence."""
    vals, rows = [], []
    for lam in LAMBDA_SET:
        r = root(N_PRIMARY, lam=lam)[0]
        rows.append({"lambda": lam, "Omega": [float(r.real), float(r.imag)]
                     if r is not None else None})
        if r is not None:
            vals.append(r)
    worst = 0.0
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            worst = max(worst, relsep(vals[i], vals[j]))
    # FT-3: the CORRECTLY-SPECIFIED half-applied gauge -- lambda carried into
    # B1 and C1 but OMITTED from C2.  Non-vacuous: the omitted terms are
    # 8 eta^2 lam - 4 eta^2 lam^2 A^2, which is O(1) at eta -> 1 for lam = 1/4.
    mvals = []
    for lam in LAMBDA_SET:
        r = root(N_PRIMARY, lam=lam, omit_lam_C2=True)[0]
        if r is not None:
            mvals.append(r)
    ftw = 0.0
    for i in range(len(mvals)):
        for j in range(i + 1, len(mvals)):
            ftw = max(ftw, relsep(mvals[i], mvals[j]))
    return ({"measured": worst, "tol": TOL["G3"], "rows": rows,
             "pass": bool(len(vals) == len(LAMBDA_SET) and worst <= TOL["G3"])},
            {"measured": ftw, "threshold": FT_THRESH["FT_3"],
             "fires": bool(ftw >= FT_THRESH["FT_3"]),
             "mutation": "lambda carried into B1 and C1 but omitted from C2"})


def gate_G4(om_star):
    """Precision (a) and arithmetic-path (b) independence."""
    hi = root(N_PRIMARY, dps=DPS_HIGH)[0]
    a = relsep(om_star, hi) if hi is not None else float("inf")
    rows, worst_b = [], 0.0
    for n in N_LADDER:
        r, s, _ = root(n)
        d = abs(complex(r) - s) / abs(complex(r)) if r is not None else float("inf")
        rows.append({"n": n, "pencil_double": [s.real, s.imag] if s else None,
                     "rel_double_vs_mp": d})
        worst_b = max(worst_b, d)
    lo = root(N_PRIMARY, dps=DPS_FT4)[0]
    ft_a = relsep(om_star, lo) if lo is not None else float("inf")
    rm, sm, _ = root(N_PRIMARY, n_double=N_UNDER)
    ft_b = abs(complex(rm) - sm) / abs(complex(rm)) if rm is not None else 0.0
    return ({"measured_a": a, "tol_a": TOL["G4a"],
             "measured_b": worst_b, "tol_b": TOL["G4b"], "rows": rows,
             "dps_pair": [DPS, DPS_HIGH],
             "pass": bool(a <= TOL["G4a"] and worst_b <= TOL["G4b"])},
            {"measured_a": ft_a, "threshold_a": FT_THRESH["FT_4a"],
             "measured_b": ft_b, "threshold_b": FT_THRESH["FT_4b"],
             "fires": bool(ft_a >= FT_THRESH["FT_4a"]
                           and ft_b >= FT_THRESH["FT_4b"]),
             "mutation": f"(a) dps = {DPS_FT4}; (b) double pencil at "
                         f"n = {N_UNDER} against the mp root at n = {N_PRIMARY}"})


def gate_G5():
    """ISOLATION -- exactly one pencil eigenvalue within R_iso at every order."""
    rows = [isolation_row(n, OMEGA_SEED) for n in N_LADDER]
    counts = [r["count_within_R_iso"] for r in rows]
    ok = all(c == 1 for c in counts)
    # FT-5(a): the v2.1-banked discretization artifact.
    art = [isolation_row(n, OMEGA_ARTIFACT) for n in N_LADDER]
    art_counts = [r["count_within_R_iso"] for r in art]
    art_roots = [complex(*r["polished"]) for r in art if r["polished"]]
    art_drift = 0.0
    for i in range(len(art_roots)):
        for j in range(i + 1, len(art_roots)):
            art_drift = max(art_drift,
                            abs(art_roots[i] - art_roots[j]) / abs(art_roots[i]))
    fires_a = bool(any(c != 1 for c in art_counts) or art_drift > TOL["G2"])
    # FT-5(b): the v2.1 C9 probe point inside the contaminated left edge.
    edge = [isolation_row(n, OMEGA_EDGE) for n in N_LADDER]
    edge_counts = [r["count_within_R_iso"] for r in edge]
    fires_b = bool(any(c != 1 for c in edge_counts))
    return ({"R_iso": R_ISO, "counts": counts, "rows": rows, "pass": bool(ok)},
            {"artifact_counts": art_counts, "artifact_drift": art_drift,
             "artifact_rows": art, "fires_a": fires_a,
             "edge_counts": edge_counts, "edge_rows": edge, "fires_b": fires_b,
             "fires": bool(fires_a and fires_b),
             "mutation": "(a) centred on the v2.1 artifact; "
                         "(b) centred on the v2.1 contaminated-edge C9 probe"})


def gate_G6(om_star, cmp_):
    """Two-instrument agreement against v1's different-in-kind instrument."""
    om_v1 = complex(*cmp_["Omega_v1"])
    d = abs(complex(om_star) - om_v1) / abs(om_v1)
    rc = root(N_PRIMARY, corrupt_C0=FT_MUT["FT_6_corrupt"])[0]
    ft = abs(complex(rc) - om_v1) / abs(om_v1) if rc is not None else float("inf")
    return ({"measured": d, "tol": TOL["G6"],
             "Omega_v1": cmp_["Omega_v1"], "pass": bool(d <= TOL["G6"])},
            {"measured": ft, "threshold": FT_THRESH["FT_6"],
             "fires": bool(ft >= FT_THRESH["FT_6"]),
             "mutation": "C0 corrupted by 1e-3 relative"})


def gate_G7(om_star, psi):
    """Spin-2-vs-spin-1 discrimination AT THE ROOT: eigenvalue AND eigenfunction."""
    r1 = root(N_PRIMARY, spin1_wall=True)[0]
    a = relsep(om_star, r1) if r1 is not None else float("inf")
    om_c = complex(om_star)
    w2, w1 = (ELL - 1) * (ELL + 2), ELL * (ELL + 1)
    R2 = strain_to_kinetic(N_PRIMARY, om_c, psi, w2)
    R1 = strain_to_kinetic(N_PRIMARY, om_c, psi, w1)
    b = abs(R1 / R2 - 1.0)
    # FT-7: REVERSE fireability -- the null mutations MUST return BELOW 1e-3.
    ft_a = relsep(om_star, root(N_PRIMARY, spin1_wall=False)[0])
    ft_b = abs(strain_to_kinetic(N_PRIMARY, om_c, psi, w2) / R2 - 1.0)
    return ({"measured_a": a, "measured_b": b, "tol": TOL["G7"],
             "weight_spin2": w2, "weight_spin1": w1,
             "strain_to_kinetic_spin2": R2, "strain_to_kinetic_spin1": R1,
             "pass": bool(a >= TOL["G7"] and b >= TOL["G7"])},
            {"measured_a": ft_a, "measured_b": ft_b,
             "threshold": FT_THRESH["FT_7"],
             "fires": bool(ft_a < FT_THRESH["FT_7"] and ft_b < FT_THRESH["FT_7"]),
             "mutation": "REVERSE: identical specifications on both axes"})


def _spread_mp(vals):
    lo, hi = min(vals), max(vals)
    mid = sum(vals) / len(vals)
    return float(abs(hi - lo) / abs(mid))


def gate_G8():
    """nu_vac cancellation AT THE ROOT, measured in mp END-TO-END."""
    def measure(**mut):
        Qs, As, Rs, rows = [], [], [], []
        for xs in X_SAT_SET:
            p = mut.get("perturb_A_scale", 0.0)
            kw = {}
            if p:
                kw["perturb_A"] = p * (xs - X_SAT) / X_SAT
            r = root(N_PRIMARY, x_sat=xs, **kw)[0]
            if r is None:
                return None, None, None, rows
            mp.mp.dps = DPS
            Qs.append(r.real / (2 * abs(r.imag)))
            As.append(abs(r))
            Rs.append(r.real)          # = omega_R*M_g * x_sat
            rows.append({"x_sat": xs, "Omega": [float(r.real), float(r.imag)],
                         "Q": float(r.real / (2 * abs(r.imag))),
                         "omega_R_M_g": float(r.real / mp.mpf(xs))})
        return _spread_mp(Qs), _spread_mp(As), _spread_mp(Rs), rows

    q, a, s, rows = measure()
    fq, fa, fs, frows = measure(perturb_A_scale=FT_MUT["FT_8_perturb"])
    worst = max(q, a, s)
    ftw = max(fq, fa, fs) if fq is not None else float("inf")
    return ({"Q_spread": q, "absOmega_spread": a, "scaling_spread": s,
             "measured": worst, "tol": TOL["G8"], "rows": rows,
             "mp_end_to_end": True, "pass": bool(worst <= TOL["G8"])},
            {"measured": ftw, "threshold": FT_THRESH["FT_8"],
             "fires": bool(ftw >= FT_THRESH["FT_8"]), "rows": frows,
             "mutation": "A -> A*(1 + 1e-6*(x_sat - 7)/7)"})


def gate_G10(om_star):
    """Ax-3 reality (a) and conjugate-mirror symmetry (b)."""
    def structure(**mut):
        w = 0.0
        for lam in LAMBDA_SET:
            M0, M1, M2 = graded_matrices_mp(N_PRIMARY, ELL, lam, X_SAT, DPS,
                                            **mut)
            for M, part in ((M0, "im"), (M1, "re"), (M2, "im")):
                num = mag = mp.mpf(0)
                for i in range(M.rows):
                    for j in range(M.cols):
                        z = M[i, j]
                        num = max(num, abs(z.imag if part == "im" else z.real))
                        mag = max(mag, abs(z))
                if mag > 0:
                    w = max(w, float(num / mag))
        return w

    a = structure()
    mirror = root(N_PRIMARY,
                  seed=complex(float(-om_star.real), float(om_star.imag)))[0]
    b = (float(abs(mirror + mp.conj(om_star)) / abs(om_star))
         if mirror is not None else float("inf"))
    ft_a = structure(loss=FT_MUT["FT_10_loss"])
    lo_star = root(N_PRIMARY, loss=FT_MUT["FT_10_loss"])[0]
    lo_mir = root(N_PRIMARY, loss=FT_MUT["FT_10_loss"],
                  seed=complex(float(-lo_star.real), float(lo_star.imag)))[0]
    ft_b = (float(abs(lo_mir + mp.conj(lo_star)) / abs(lo_star))
            if lo_mir is not None else float("inf"))
    return ({"measured_a": a, "tol_a": TOL["G10a"],
             "measured_b": b, "tol_b": TOL["G10b"],
             "Omega_mirror": [float(mirror.real), float(mirror.imag)]
             if mirror is not None else None,
             "pass": bool(a <= TOL["G10a"] and b <= TOL["G10b"])},
            {"measured_a": ft_a, "threshold_a": FT_THRESH["FT_10a"],
             "measured_b": ft_b, "threshold_b": FT_THRESH["FT_10b"],
             "fires": bool(ft_a >= FT_THRESH["FT_10a"]
                           and ft_b >= FT_THRESH["FT_10b"]),
             "mutation": "Im(mu)/Re(mu) = 1e-3 smuggled into the modulus"})


# ===========================================================================
# THE FROZEN BINS (prereg section 7) -- adjudicated IFF ALL GATES PASS
# ===========================================================================
def adjudicate(om_star, loc, cmp_):
    wr = float(om_star.real) / X_SAT
    wi = float(abs(om_star.imag)) / X_SAT
    Q = float(om_star.real / (2 * abs(om_star.imag)))
    d_om = wr / cmp_["omega_R_GR"] - 1.0
    d_short = wr / cmp_["omega_R_shortcut"] - 1.0
    Q_GR = cmp_["Q_GR"]
    d_Q = Q / Q_GR - 1.0
    b1 = ("BIN-1-MATCH" if abs(d_om) < 0.03 else
          "BIN-1-NEAR" if abs(d_om) < 0.10 else "BIN-1-MISS")
    b2 = ("BIN-2-MATCH" if abs(d_Q) < 0.03 else
          "BIN-2-NEAR" if abs(d_Q) < 0.10 else "BIN-2-MISS")
    dg, dc = abs(Q - Q_GR), abs(Q - cmp_["Q_convention"])
    if abs(dg - dc) <= 1e-6:
        b2d = "BIN-2-EQUIDISTANT"
    elif dg < dc:
        b2d = "BIN-2-CLOSER-GR"
    else:
        b2d = "BIN-2-CLOSER-CONVENTION"
    # FLAG-1 robustness, frozen as a CRITERION (prereg section 7.3)
    lo = (cmp_["Q_GR_rounded_prose"] + cmp_["Q_convention"]) / 2.0
    hi = (Q_GR + cmp_["Q_convention"]) / 2.0
    lo, hi = min(lo, hi), max(lo, hi)
    ambiguous = bool(lo <= Q <= hi)
    if ambiguous:
        b2d = "BIN-2-AMBIGUOUS-UNDER-FLAG-1"
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
    b3sub = (["BIN-3-RAMP-TURNING-POINT"]
             if b3 == "BIN-3-RAMP" and abs(u - 1.2247) <= 0.05 else [])
    return {
        "omega_R_M_g": wr, "omega_I_M_g": wi, "Q": Q,
        "D_omega": d_om, "D_omega_shortcut": d_short, "D_Q": d_Q,
        "k0_r_sat": float(om_star.real),
        "k0_r_sat_identity_tag": "IDENTITY -- not independent of BIN-1's "
                                 "shortcut comparison",
        "BIN_1": b1, "BIN_2": b2, "BIN_2_discriminator": b2d,
        "BIN_2_flag1_window": [lo, hi],
        "BIN_2_flag1_ambiguous": ambiguous,
        "dist_to_Q_GR": dg, "dist_to_Q_convention": dc,
        "BIN_3": b3, "BIN_3_subflags": b3sub,
        "BIN_4": "N/A BY CONSTRUCTION",
        "nu_vac_rider_falsified": bool(abs(d_short) > 0.03),
    }


def spectral_convergence(ref_n=96):
    """NOT-ADJUDICATED DIAGNOSTIC -- added AFTER G2's outcome was seen, to TEST
    the attribution of that outcome rather than assert it.  It is not a gate,
    it changes no frozen criterion, it changes no verdict, and it enters no
    bin.  If the ladder's spread is spectral under-resolution then the error
    against the highest order must fall geometrically in n; if it is a
    migrating pseudo-pole (the PR #854 audit's mechanism) it must not."""
    ref = root(ref_n)[0]
    rows = []
    for n in N_LADDER:
        r = root(n)[0]
        rows.append({"n": n,
                     "rel_vs_n_ref": relsep(ref, r) if r is not None else None})
    for i in range(len(rows) - 1):
        lo, hi = rows[i]["rel_vs_n_ref"], rows[i + 1]["rel_vs_n_ref"]
        rows[i]["ratio_to_next"] = (lo / hi) if (lo and hi) else None
    return {"reference_n": ref_n, "rows": rows,
            "tag": "NOT-ADJUDICATED DIAGNOSTIC -- no gate, no bin, no verdict"}


def digest_of(obj):
    clean = {k: v for k, v in obj.items() if k not in ("_digest", "_runtime_sec")}
    blob = json.dumps(clean, sort_keys=True, separators=(",", ":"),
                      default=str).encode()
    return hashlib.sha256(blob).hexdigest()[:16]


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    t0 = time.time()
    cmp_ = comparators()

    G0, FT0 = gate_G0()

    om_star, seed_double, _ = root(N_PRIMARY)
    if om_star is None:
        out = {"certification": "BIN-F-NOROOT", "note":
               "no pencil eigenvalue within R_iso of the frozen seed at "
               "n = 48, or the mp polish failed to converge"}
        print(json.dumps(out, indent=1))
        return 0
    psi, _ = eigenfunction(N_PRIMARY, om_star)

    G1, FT1 = gate_G1(om_star, psi)
    G2, FT2 = gate_G2(om_star)
    G3, FT3 = gate_G3()
    G4, FT4 = gate_G4(om_star)
    G5, FT5 = gate_G5()
    G6, FT6 = gate_G6(om_star, cmp_)
    G7, FT7 = gate_G7(om_star, psi)
    G8, FT8 = gate_G8()
    G10, FT10 = gate_G10(om_star)

    loc = localization(N_PRIMARY, complex(om_star), psi)

    gates = {"G0": G0, "G1": G1, "G2": G2, "G3": G3, "G4": G4, "G5": G5,
             "G6": G6, "G7": G7, "G8": G8,
             "G9": {"note": "determinism is adjudicated EXTERNALLY by running "
                            "the driver twice and diffing the shipped objects; "
                            "this flag is a placeholder and is NOT a "
                            "self-measurement",
                    "pass": True},
             "G10": G10}
    self_tests = {"FT_0": FT0, "FT_1": FT1, "FT_2": FT2, "FT_3": FT3,
                  "FT_4": FT4, "FT_5": FT5, "FT_6": FT6, "FT_7": FT7,
                  "FT_8": FT8, "FT_10": FT10}

    failed = sorted(k for k, v in gates.items() if not v.get("pass"))
    unfired = sorted(k for k, v in self_tests.items() if not v.get("fires"))

    out = {
        "_prereg": "research/2026-08-03_coldq-pole-v2.2-root_prereg-FROZEN.md",
        "_prereg_commit": "f15a6e4d",
        "_method": "compactified hyperboloidal Chebyshev spectral; ROOT-LOCAL "
                   "certification only; NO winding, NO contour, NO region count",
        "_non_claim": "this lane asserts the existence and location of THIS "
                      "root; it asserts NOTHING about the absence or presence "
                      "of other modes",
        "_frozen_numerics": {
            "n_primary": N_PRIMARY, "n_ladder": list(N_LADDER),
            "lambda_set": list(LAMBDA_SET), "dps": DPS, "dps_high": DPS_HIGH,
            "polish_tol_exp": POLISH_TOL_EXP, "polish_iters": POLISH_ITERS,
            "invit_rounds": INVIT_ROUNDS, "dedupe_rel": DEDUPE_REL,
            "R_iso": R_ISO, "x_sat": X_SAT, "x_sat_set": list(X_SAT_SET),
            "ell": ELL, "loc_window": list(LOC_WINDOW),
            "loc_points": LOC_POINTS, "runtime_budget_s": RUNTIME_BUDGET_S,
        },
        "seed": {"Omega_seed": [OMEGA_SEED.real, OMEGA_SEED.imag],
                 "source": "research/drivers/coldq_pole_v2_results.json "
                           "@ bdcfa678 (PR #854, not on origin/main)",
                 "role": "SEED ONLY -- selects which pencil eigenvalue is "
                         "polished; enters no gate, tolerance, comparator "
                         "or bin"},
        "certified_root": {
            "Omega_re": float(om_star.real), "Omega_im": float(om_star.imag),
            "Omega_re_mp": mp.nstr(om_star.real, 40),
            "Omega_im_mp": mp.nstr(om_star.imag, 40),
            "abs_Omega": float(abs(om_star)),
            "pencil_seed_double": [seed_double.real, seed_double.imag],
        },
        "comparators": cmp_,
        "isolation_receipts": iso_receipts(cmp_),
        "localization": loc,
        "diagnostics": {"spectral_convergence": spectral_convergence()},
        "gates": gates,
        "self_tests": self_tests,
        "failed_gates": failed,
        "unfired_self_tests": unfired,
    }

    certified = (not failed) and (not unfired)
    out["certification"] = "ROOT-CERTIFIED" if certified else "ROOT-NOT-CERTIFIED"
    if certified:
        out["adjudication"] = adjudicate(om_star, loc, cmp_)
    else:
        out["adjudication"] = {
            "BIN_1": "N/A -- not adjudicated", "BIN_2": "N/A -- not adjudicated",
            "BIN_2_discriminator": "N/A -- not adjudicated",
            "BIN_3": "N/A -- not adjudicated",
            "BIN_4": "N/A BY CONSTRUCTION",
            "precedence_fired": "BIN-F-ROOT",
        }

    # FT-9: the digest must actually cover the gate payload.
    d0 = digest_of(out)
    probe = json.loads(json.dumps(out, default=str))
    probe["gates"]["G1"]["measured"] = (out["gates"]["G1"]["measured"]
                                        * (1 + FT_MUT["FT_9_perturb"]))
    d1 = digest_of(probe)
    out["self_tests"]["FT_9"] = {
        "digest": d0, "perturbed_digest": d1, "fires": bool(d0 != d1),
        "mutation": "gates.G1.measured perturbed by 1e-15 relative in a copy"}
    if not out["self_tests"]["FT_9"]["fires"]:
        out["unfired_self_tests"] = sorted(set(out["unfired_self_tests"])
                                           | {"FT_9"})
        out["certification"] = "ROOT-NOT-CERTIFIED"
        out["adjudication"] = {
            "BIN_1": "N/A -- not adjudicated", "BIN_2": "N/A -- not adjudicated",
            "BIN_2_discriminator": "N/A -- not adjudicated",
            "BIN_3": "N/A -- not adjudicated",
            "BIN_4": "N/A BY CONSTRUCTION",
            "precedence_fired": "BIN-F-ROOT"}

    out["_digest"] = digest_of(out)
    out["_runtime_sec"] = round(time.time() - t0, 2)

    dest = os.path.join(_HERE, "coldq_pole_v2p2_root_results.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, sort_keys=True, default=str)
        fh.write("\n")

    print(f"certification      : {out['certification']}")
    print(f"failed gates       : {failed or 'none'}")
    print(f"unfired self-tests : {out['unfired_self_tests'] or 'none'}")
    print(f"Omega              : {float(om_star.real):.16f} "
          f"{float(om_star.imag):+.16f}i")
    print(f"digest             : {out['_digest']}")
    print(f"runtime            : {out['_runtime_sec']} s "
          f"(budget {RUNTIME_BUDGET_S} s)")
    print(f"wrote              : {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

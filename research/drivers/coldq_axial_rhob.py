#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The cold-Q AXIAL family under RHO-B -- FORK-3(b) in the certified axial class.

PREREG (FROZEN, committed ALONE at e3a4181d before this file existed):
    research/2026-08-04_coldq-axial-rhob_prereg-FROZEN.md

WHAT THIS IS.  v2.4 certified the l = 2 toroidal shear pole of the graded
saturation cavity under RHO-A (rho = rho_bulk).  Its section 7 FLAG-4 records
that a second canonical inertia reading exists -- RHO-B, rho_eff = rho_bulk/S^3
-- that X6 fenced off and never ran, and that "would move the eigenvalue".
This driver runs it.

THE ONE-COEFFICIENT CHANGE (prereg 2.3, DERIVED there, re-verified by G0 here):
    rho/mu enters the toroidal radial system at exactly one place.
    RHO-A :  Om^2 / ( S (1 + S) )        [ = (1/S   - 1) / A^2 ]
    RHO-B :  Om^2 ( 1 + S^2 ) / S^4      [ = (1/S^4 - 1) / A^2 ]

THE WALL (prereg 2.4/2.5, DERIVED, NOT imported from RHO-A):
    Z_shear = sqrt(mu rho) = rho c_shear = 1/S -> INFINITY  (RHO-A: sqrt(S) -> 0)
    int dr/c_shear diverges logarithmically -> the wall is at INFINITE optical
        distance and there is no reflection event
    eta = 0 is a REGULAR SINGULAR point (RHO-A: an ORDINARY point), indicial
        equation  sigma(sigma - 1) + Om^2 = 0,  sigma_pm = (1 +- sqrt(1-4Om^2))/2
    the RHO-A traction-free row dpsi/deta = 0 is REJECTED BY DERIVATION and is
        exercised only as the self-test FT-SHORT
    the RHO-B row is dphi/deta = 0 on phi = eta^(-sigma) psi -- the a_1 = 0
        Frobenius analyticity constraint, identical in form for both branches

CARRY-OVER DISCLOSURE (prereg section 8).  The Chebyshev construction, the mp
LU/determinant/polish/inverse-iteration machinery, the companion linearization
and the comparator readers are CARRIED OVER from v2.4 by READ-ONLY IMPORT of
research/drivers/coldq_pole_v2p4_root.py, so that the OPERATOR and the WALL ROW
are the only variables.  That file is imported, never edited, and never run as
a battery.  This lane claims NO reimplementation independence from v2.4.

Engine src/ave BYTE-UNTOUCHED.  ave.core.* imported read-only (through v2.4).
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import os
import sys
import time

import mpmath as mp
import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(os.path.dirname(_HERE))

# ===========================================================================
# READ-ONLY IMPORT OF THE CERTIFIED AXIAL INSTRUMENT
# The predecessor file is loaded as a module and used as (i) the source of the
# shared numerical machinery and (ii) the comparison object of the negative
# control G-NC.  It is NOT edited and its main() is NOT executed.
# ===========================================================================
V24_PY = os.path.join(_HERE, "coldq_pole_v2p4_root.py")
V24_JSON = os.path.join(_HERE, "coldq_pole_v2p4_root_results.json")

_spec = importlib.util.spec_from_file_location("_v24_readonly", V24_PY)
V24 = importlib.util.module_from_spec(_spec)
sys.modules["_v24_readonly"] = V24
_spec.loader.exec_module(V24)

cheb = V24.cheb                       # CGL nodes + D, ASCENDING on [0, 1]
cheb_mp = V24.cheb_mp                 # the same, built ENTIRELY in mp
pencil_spectrum = V24.pencil_spectrum  # companion linearization
dedupe = V24.dedupe
mp_lu = V24.mp_lu
mp_lu_solve = V24.mp_lu_solve
relsep = V24.relsep                   # relative separation computed IN MP

# ===========================================================================
# FROZEN NUMERICS -- prereg section 4.2.  Nothing below is tunable.
# ===========================================================================
N_PRIMARY = 48
N_LADDER = (32, 48, 64, 80)
N_LADDER_CERT = (32, 48, 64)
N_REF = 80
LAMBDA_PRIMARY = 0.0
LAMBDA_SET = (-0.25, 0.0, 0.25)
DPS = 50
DPS_HIGH = 80
DPS_FT4 = 20
POLISH_TOL_EXP = 38
POLISH_ITERS = 60
INVIT_ROUNDS = 4
DEDUPE_REL = 1e-6
R_ISO = 0.5
X_SAT = 7.0
X_SAT_SET = (5.0, 7.0, 11.0)
ELL = 2
N_UNDER = 8
OMEGA_FTW = 0.5
NSTABLE_REL = 1e-3
RESONANCE_GUARD = 1e-3
RUNTIME_BUDGET_S = 7200.0

# prereg section 4.5 -- every tolerance, with its derivation in that table
TOL = {
    "G_NC_a": 1e-40,
    "G_NC_b": 1e-30,
    "G0": 1e-13,
    "G_IND": 1e-30,
    "G_FROB": 1e-9,
    "G1": 1e-20,
    "G2_spectral": 1e-10,
    "G2_algebraic": 1e-3,
    "G2c_p_floor": 1.0,
    "G2c_c_floor": 1.0,
    "G2c_resid": 0.60,
    "G3_spectral": 1e-10,
    "G3_algebraic": 1e-3,
    "G4a": 1e-25,
    "G4b": 1e-6,
    "G8": 1e-9,
    "G10a": 1e-40,
    "G10b": 1e-20,
    "G_AGREE": 1e-3,
}

FT_THRESH = {
    "FT_NC": 1e-30,
    "FT_0": 1e-13,
    "FT_1": 1e-20,
    "FT_2": 1e-3,
    "FT_3": 1e-3,
    "FT_4a": 1e-25,
    "FT_4b": 1e-6,
    "FT_8": 1e-9,
    "FT_10": 1e-6,
    "FT_SHORT": 1e-2,
}

FT_MUT = {
    "FT_0_corrupt": 1e-12,
    "FT_1_offset": 1e-10,
    "FT_2c_stagnate": 1e-12,
    "FT_8_perturb": 1e-6,
    "FT_10_loss": 1e-3,
}

# The configuration matrix -- prereg section 4.3
CFG_A_CONTROL = "CFG-A-CONTROL"
CFG_BOUND_FROB = "CFG-BOUND-FROB"
CFG_IN_FROB = "CFG-IN-FROB"
CFG_BOUND_POLY = "CFG-BOUND-POLY"

# Which convergence law each configuration's endpoint regularity class implies
# (prereg 5, G2c: "law-matched to the derived endpoint class").
LAW = {
    CFG_A_CONTROL: "rootexp",
    CFG_BOUND_FROB: "rootexp",
    CFG_IN_FROB: "power",
    CFG_BOUND_POLY: "power",
}
G2_TOL = {
    CFG_A_CONTROL: TOL["G2_spectral"],
    CFG_BOUND_FROB: TOL["G2_spectral"],
    CFG_IN_FROB: TOL["G2_algebraic"],
    CFG_BOUND_POLY: TOL["G2_algebraic"],
}
G3_TOL = {
    CFG_A_CONTROL: TOL["G3_spectral"],
    CFG_BOUND_FROB: TOL["G3_spectral"],
    CFG_IN_FROB: TOL["G3_algebraic"],
    CFG_BOUND_POLY: TOL["G3_algebraic"],
}


# ===========================================================================
# THE INDICIAL EXPONENTS -- prereg section 2.4(c), DERIVED there
#   sigma (sigma - 1) + Om^2 = 0   =>   sigma_pm = (1 +- sqrt(1 - 4 Om^2))/2
# on the PRINCIPAL branch of the square root, so Re sqrt >= 0 and
# Re sigma_+ >= Re sigma_-.
# ===========================================================================
def sigma_pair(om):
    """(sigma_plus, sigma_minus) in mp, principal branch."""
    o = mp.mpc(om)
    rt = mp.sqrt(1 - 4 * o ** 2)
    return (1 + rt) / 2, (1 - rt) / 2


def sigma_for(cfg, om):
    sp, sm = sigma_pair(om)
    if cfg == CFG_BOUND_FROB:
        return sp
    if cfg == CFG_IN_FROB:
        return sm
    return None


# ===========================================================================
# THE COEFFICIENT PARTS -- one function, one inertia switch.
#
# prereg 2.1 frozen: "the inertia enters the toroidal radial system at exactly
# one place, the combination rho/mu in the omega^2 coefficient, so FORK-3(b) is
# a ONE-COEFFICIENT change to the certified axial operator and every other
# coefficient ... is byte-identical between RHO-A and RHO-B".
#
# EVERY line below except C2_rho is carried over verbatim from
# V24.graded_coeff_parts / V24.graded_matrices_mp -- see the module docstring's
# carry-over disclosure.  The RHO-A branch is therefore a re-execution of the
# certified coefficient algebra and is what G-NC(a) gates.
# ===========================================================================
def coeff_parts(eta, ell, lam, rho_mode, x_sat=X_SAT, perturb_A=0.0,
                corrupt_C0=0.0, omit_lam_C2=False, loss=0.0):
    """Double-precision eta-form coefficient parts (Acoef, B0, B1, C0, C1, C2)."""
    r_sat = float(x_sat)
    A0 = 1.0 - eta ** 2
    with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
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
    # ---- THE FORK.  This is the only line that differs between RHO-A/RHO-B.
    if rho_mode == "A":
        C2_rho = 4.0 * eta / (u * (1.0 + S))
    elif rho_mode == "B":
        # 4 eta^2 (1 + S^2)/S^4 with S = eta u.  Guarded at eta = 0, where the
        # coefficient has its DERIVED double pole and where row 0 is replaced
        # by the wall row in every configuration.
        with np.errstate(divide="ignore", invalid="ignore"):
            e2 = np.where(eta == 0.0, 1.0, eta) ** 2
            C2_rho = np.where(eta == 0.0, 0.0,
                              4.0 * (1.0 + S ** 2) / (e2 * u ** 4))
    else:
        raise ValueError(f"rho_mode must be 'A' or 'B', got {rho_mode!r}")
    if loss:
        C2_rho = C2_rho / (1.0 + 1j * loss)
    C2_lam = 0.0 if omit_lam_C2 else (8.0 * eta ** 2 * lam
                                      - 4.0 * eta ** 2 * lam ** 2 * Asq)
    return Asq, B0, B1, C0, C1, C2_rho + C2_lam


def coeff_parts_mp(e, ell, lam, rho_mode, x_sat=X_SAT, perturb_A=0.0,
                   corrupt_C0=0.0, omit_lam_C2=False, loss=0.0):
    """The same algebra in mp, one node at a time."""
    r_sat = mp.mpf(x_sat)
    lm = mp.mpf(lam)
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
    if rho_mode == "A":
        C2 = 4 * e / (u * (1 + S))
    elif rho_mode == "B":
        C2 = mp.mpf(0) if e == 0 else 4 * (1 + S ** 2) / (e ** 2 * u ** 4)
    else:
        raise ValueError(f"rho_mode must be 'A' or 'B', got {rho_mode!r}")
    if loss:
        C2 = C2 / (1 + mp.mpc(0, 1) * mp.mpf(loss))
    if not omit_lam_C2:
        C2 = C2 + 8 * e ** 2 * lm - 4 * e ** 2 * lm ** 2 * Asq
    return Asq, B0, B1, C0, C1, C2


# ===========================================================================
# THE WALL ROWS -- prereg section 2.5.  Three named rows, one rejected.
#   "neumann"    dpsi/deta(0) = 0   RHO-A's traction-free SHORT.  Legitimate at
#                                   an ORDINARY point.  Under RHO-B it is the
#                                   REJECTED row and is used only by FT-SHORT.
#   "dirichlet"  psi(0) = 0         the eta = 0 limit of the eta^2-multiplied
#                                   equation given Om != 0; the discrete
#                                   surrogate for retaining the sigma_+ branch.
#   "frob"       dphi/deta(0) = 0   the DERIVED a_1 = 0 analyticity constraint
#                                   on phi = eta^(-sigma) psi.
# ===========================================================================
WALL_NEUMANN = "neumann"
WALL_DIRICHLET = "dirichlet"
WALL_FROB = "frob"

CFG_SPEC = {
    CFG_A_CONTROL: ("A", WALL_NEUMANN),
    CFG_BOUND_POLY: ("B", WALL_DIRICHLET),
    CFG_BOUND_FROB: ("B", WALL_FROB),
    CFG_IN_FROB: ("B", WALL_FROB),
}


# ===========================================================================
# THE QUADRATIC PENCIL (the "neumann" and "dirichlet" wall rows only)
#   M(Om) = M0 + Om M1 + Om^2 M2 on CGL nodes, row 0 replaced by the wall row.
# This is the object the companion linearization needs; the Frobenius
# configurations are NOT of this form (prereg 4.1, disclosed).
# ===========================================================================
def pencil_double(n, ell, lam, rho_mode, wall, x_sat=X_SAT, **mut):
    eta, D = cheb(n)
    D2 = D @ D
    Ac, B0, B1, C0, C1, C2 = coeff_parts(eta, ell, lam, rho_mode, x_sat, **mut)
    M0 = Ac[:, None] * D2 + B0[:, None] * D + np.diag(C0).astype(complex)
    M1 = B1[:, None] * D + np.diag(C1).astype(complex)
    M2 = np.diag(C2).astype(complex)
    M0[0, :] = 0.0
    M1[0, :] = 0.0
    M2[0, :] = 0.0
    if wall == WALL_NEUMANN:
        M0[0, :] = D[0, :]
    elif wall == WALL_DIRICHLET:
        M0[0, 0] = 1.0
    else:
        raise ValueError(f"pencil_double does not carry wall={wall!r}")
    s = np.maximum.reduce([np.abs(M0).max(1), np.abs(M1).max(1),
                           np.abs(M2).max(1)])
    s[s == 0] = 1.0
    return M0 / s[:, None], M1 / s[:, None], M2 / s[:, None], eta, D


def pencil_mp(n, ell, lam, rho_mode, wall, x_sat=X_SAT, dps=DPS, **mut):
    mp.mp.dps = dps
    eta, D, D2 = cheb_mp(n, dps)
    N = n + 1
    M0, M1, M2 = mp.zeros(N, N), mp.zeros(N, N), mp.zeros(N, N)
    for i in range(N):
        Asq, B0, B1, C0, C1, C2 = coeff_parts_mp(eta[i], ell, lam, rho_mode,
                                                 x_sat, **mut)
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
    if wall == WALL_NEUMANN:
        for j in range(N):
            M0[0, j] = D[0, j]
    elif wall == WALL_DIRICHLET:
        M0[0, 0] = mp.mpc(1)
    else:
        raise ValueError(f"pencil_mp does not carry wall={wall!r}")
    return V24._equil_mp(M0, M1, M2)


# ===========================================================================
# THE FROBENIUS OPERATOR -- transcendental in Om (prereg 4.1, disclosed).
#
#   psi = eta^sigma phi  =>  multiply the eta-form by eta^2 and substitute:
#     A_F = eta^2 A ,  B_F = 2 sigma eta A + eta^2 B ,
#     C_F = A sigma(sigma-1) + sigma eta B + eta^2 C
#   Row 0 of that operator is IDENTICALLY ZERO, because
#     C_F(0) = sigma(sigma-1) + Om^2 = 0  by the indicial equation,
#   which is why the derived row dphi/deta(0) = 0 is not a choice: the
#   collocation row at eta = 0 is degenerate and the analyticity constraint is
#   what replaces it.
#
# EQUILIBRATION.  Row scales are computed ONCE at a fixed reference Om and then
# held, so the scaling is Om-INDEPENDENT and provably cannot move a root of
# det M(Om).  (An Om-dependent row scaling multiplies the determinant by a
# function of Om and is not safe.)
# ===========================================================================
def frob_matrix_mp(n, om, sigma, ell, lam, x_sat=X_SAT, dps=DPS,
                   scales=None, wall=WALL_FROB, rho_mode="B", **mut):
    mp.mp.dps = dps
    eta, D, D2 = cheb_mp(n, dps)
    N = n + 1
    o = mp.mpc(om)
    sg = mp.mpc(sigma)
    M = mp.zeros(N, N)
    for i in range(N):
        e = eta[i]
        Asq, B0, B1, C0, C1, C2 = coeff_parts_mp(e, ell, lam, rho_mode, x_sat,
                                                 **mut)
        Bc = B0 + o * B1
        Cc = C0 + o * C1 + o ** 2 * C2
        AF = e ** 2 * Asq
        BF = 2 * sg * e * Asq + e ** 2 * Bc
        CF = Asq * sg * (sg - 1) + sg * e * Bc + e ** 2 * Cc
        for j in range(N):
            M[i, j] = AF * D2[i, j] + BF * D[i, j]
        M[i, i] += CF
    for j in range(N):
        M[0, j] = mp.mpc(0)
    if wall in (WALL_FROB, WALL_NEUMANN):
        for j in range(N):
            M[0, j] = D[0, j]          # the DERIVED row: dphi/deta(0) = 0
    elif wall == WALL_DIRICHLET:
        M[0, 0] = mp.mpc(1)
    else:
        raise ValueError(f"frob_matrix_mp does not carry wall={wall!r}")
    if scales is None:
        scales = [max(abs(M[i, j]) for j in range(N)) or mp.mpf(1)
                  for i in range(N)]
    for i in range(N):
        for j in range(N):
            M[i, j] /= scales[i]
    return M, scales


def mp_det_single(A):
    """LU with partial pivoting; never a product of unpivoted pivots."""
    n = A.rows
    B = mp.matrix(A)
    d = mp.mpc(1)
    for k in range(n):
        p = max(range(k, n), key=lambda r: abs(B[r, k]))
        if p != k:
            for j in range(k, n):
                B[k, j], B[p, j] = B[p, j], B[k, j]
            d = -d
        piv = B[k, k]
        if piv == 0:
            return mp.mpc(0)
        d *= piv
        for i in range(k + 1, n):
            f = B[i, k] / piv
            for j in range(k, n):
                B[i, j] -= f * B[k, j]
    return d


def mp_polish_fn(fn, om0, dps=DPS):
    """Deterministic complex secant on a callable.  No RNG, no adaptivity."""
    mp.mp.dps = dps
    b = mp.mpc(om0)
    a = b * (1 + mp.mpf(10) ** (-6))
    fa, fb = fn(a), fn(b)
    for _ in range(POLISH_ITERS):
        if fb == fa:
            break
        c = b - fb * (b - a) / (fb - fa)
        if not mp.isfinite(c.real) or abs(c - b) > 10 * abs(b) + 10:
            return None
        a, fa, b = b, fb, c
        fb = fn(b)
        if abs(b - a) <= mp.mpf(10) ** (-POLISH_TOL_EXP) * abs(b):
            break
    return b


# ===========================================================================
# ROOTS -- one entry point per configuration class, memoized on the exact
# argument tuple (a pure performance optimization; no RNG, no adaptivity).
# ===========================================================================
_CACHE: dict = {}


def _mk(mut):
    return tuple(sorted(mut.items()))


def poly_root(cfg, n, lam=LAMBDA_PRIMARY, x_sat=X_SAT, dps=DPS, ell=ELL,
              seed=None, n_double=None, **mut):
    """Seed -> nearest double pencil eigenvalue -> mp secant.  v2.4's path."""
    rho_mode, wall = CFG_SPEC[cfg]
    key = ("poly", cfg, n, lam, x_sat, dps, ell, seed, n_double, _mk(mut))
    if key in _CACHE:
        return _CACHE[key]
    nd = n if n_double is None else n_double
    M0, M1, M2, _, _ = pencil_double(nd, ell, lam, rho_mode, wall, x_sat, **mut)
    spec = dedupe(list(pencil_spectrum(M0, M1, M2)), DEDUPE_REL)
    s = min(spec, key=lambda z: abs(z - seed)) if spec else None
    if s is None:
        _CACHE[key] = (None, None, spec)
        return _CACHE[key]
    P0, P1, P2 = pencil_mp(n, ell, lam, rho_mode, wall, x_sat, dps, **mut)
    r = V24.mp_polish(P0, P1, P2, s, dps)
    _CACHE[key] = (r, complex(s), spec)
    return _CACHE[key]


def frob_root(cfg, n, seed, lam=LAMBDA_PRIMARY, x_sat=X_SAT, dps=DPS, ell=ELL,
              **mut):
    """mp secant on det M(Om) with sigma(Om) recomputed at every evaluation."""
    key = ("frob", cfg, n, lam, x_sat, dps, ell, complex(seed), _mk(mut))
    if key in _CACHE:
        return _CACHE[key]
    _, scales = frob_matrix_mp(n, seed, sigma_for(cfg, seed), ell, lam,
                               x_sat, dps, **mut)

    def det_of(om):
        sg = sigma_for(cfg, om)
        M, _ = frob_matrix_mp(n, om, sg, ell, lam, x_sat, dps,
                              scales=scales, **mut)
        return mp_det_single(M)

    r = mp_polish_fn(det_of, seed, dps)
    _CACHE[key] = (r, scales)
    return _CACHE[key]


def root_of(cfg, n, seed, lam=LAMBDA_PRIMARY, x_sat=X_SAT, dps=DPS, ell=ELL,
            **mut):
    """Uniform root entry point.  Returns the mp root or None."""
    if CFG_SPEC[cfg][1] == WALL_FROB:
        return frob_root(cfg, n, seed, lam, x_sat, dps, ell, **mut)[0]
    return poly_root(cfg, n, lam, x_sat, dps, ell, seed=seed, **mut)[0]


def matrix_at(cfg, n, om, lam=LAMBDA_PRIMARY, x_sat=X_SAT, dps=DPS, ell=ELL,
              **mut):
    """The assembled mp matrix M(Om) for either configuration class."""
    rho_mode, wall = CFG_SPEC[cfg]
    if wall == WALL_FROB:
        M, _ = frob_matrix_mp(n, om, sigma_for(cfg, om), ell, lam, x_sat, dps,
                              **mut)
        return M
    P0, P1, P2 = pencil_mp(n, ell, lam, rho_mode, wall, x_sat, dps, **mut)
    return V24.mp_assemble(P0, P1, P2, om)


def eigenfunction(cfg, n, om, lam=LAMBDA_PRIMARY, x_sat=X_SAT, dps=DPS,
                  ell=ELL, rounds=INVIT_ROUNDS, **mut):
    """mp inverse iteration from the deterministic all-ones vector."""
    mp.mp.dps = dps
    A = matrix_at(cfg, n, om, lam, x_sat, dps, ell, **mut)
    LU, perm = mp_lu(mp.matrix(A))
    v = [mp.mpc(1)] * (n + 1)
    for _ in range(rounds):
        v = mp_lu_solve(LU, perm, v)
        m = max(abs(z) for z in v)
        v = [z / m for z in v]
    r = [sum(A[i, j] * v[j] for j in range(n + 1)) for i in range(n + 1)]
    return v, max(abs(z) for z in r) / max(abs(z) for z in v)


def residual_at(cfg, n, om, vec, lam=LAMBDA_PRIMARY, x_sat=X_SAT, dps=DPS,
                ell=ELL, **mut):
    mp.mp.dps = dps
    A = matrix_at(cfg, n, om, lam, x_sat, dps, ell, **mut)
    r = [sum(A[i, j] * vec[j] for j in range(n + 1)) for i in range(n + 1)]
    return float(max(abs(z) for z in r) / max(abs(z) for z in vec))


def _mp_pair(r):
    if r is None:
        return {"Omega_re_mp": None, "Omega_im_mp": None}
    return {"Omega_re_mp": mp.nstr(r.real, 40), "Omega_im_mp": mp.nstr(r.imag, 40)}


def _row(n, r, **extra):
    d = {"n": n, "Omega": [float(r.real), float(r.imag)] if r is not None else None}
    d.update(_mp_pair(r))
    d.update(extra)
    return d


# ===========================================================================
# COMPARATORS + THE CERTIFIED RHO-A ROOT -- read PROGRAMMATICALLY (K12, K13).
# Nothing below is typed.
# ===========================================================================
def certified_rho_a(dps=DPS):
    mp.mp.dps = dps
    with open(V24_JSON, encoding="utf-8") as fh:
        j = json.load(fh)
    cr = j["certified_root"]
    return mp.mpc(mp.mpf(cr["Omega_re_mp"]), mp.mpf(cr["Omega_im_mp"])), j


def comparators():
    c = V24.comparators()          # K12, read from its in-repo carrier
    om_a, j = certified_rho_a()
    adj = j["adjudication"]
    c["Omega_A"] = [float(om_a.real), float(om_a.imag)]
    c["omega_R_M_A"] = float(om_a.real) / X_SAT
    c["Q_A"] = float(om_a.real) / (2.0 * abs(float(om_a.imag)))
    c["D_omega_A"] = c["omega_R_M_A"] / c["omega_R_GR"] - 1.0
    c["D_Q_A"] = c["Q_A"] / c["Q_GR"] - 1.0
    c["v24_adjudication"] = {k: adj[k] for k in sorted(adj) if isinstance(adj[k], str)}
    return c


# ===========================================================================
# THE SEARCH -- prereg section 4.4, frozen BEFORE any code existed.
#   primary chain : Omega_A -> nearest CFG-BOUND-POLY pencil eigenvalue ->
#                   polished -> used as the Frobenius seed
#   enumeration   : ALL CFG-BOUND-POLY pencil eigenvalues in the physical
#                   quadrant with |Om| <= 8, deduped at DEDUPE_REL
#   filter        : located roots kept only if n-STABLE between n = 48 and
#                   n = 80 at NSTABLE_REL   (prereg 7.1's BIN-B-N wording:
#                   "no LOCATED root is n-stable", so the filter is applied to
#                   located roots, not to raw pencil eigenvalues)
#   order         : decreasing Re/(2|Im|); top five reported
# ===========================================================================
def _phys(z):
    return z.real > 1e-6 and z.imag < -1e-6 and abs(z) <= 8.0


def enumerate_seeds(seed_A):
    _, _, spec = poly_root(CFG_BOUND_POLY, N_PRIMARY, seed=seed_A)
    return [z for z in spec if _phys(z)], spec


def search(cfg, seeds, seed_A):
    """Returns (record, chosen_root_mp or None)."""
    located, seen = [], []
    for z in seeds:
        r = root_of(cfg, N_PRIMARY, z)
        if r is None:
            continue
        w = complex(r)
        if not _phys(w):
            continue
        if any(abs(w - q) <= DEDUPE_REL * max(abs(q), 1.0) for q in seen):
            continue
        seen.append(w)
        located.append((w, r))
    stable = []
    for w, r in located:
        r80 = root_of(cfg, N_REF, w)
        if r80 is None:
            continue
        w80 = complex(r80)
        rel = abs(w - w80) / max(abs(w80), 1.0)
        stable.append({"Omega_n48": [w.real, w.imag],
                       "Omega_n80": [w80.real, w80.imag],
                       "nstable_rel": rel,
                       "n_stable": bool(rel <= NSTABLE_REL and _phys(w80)),
                       "Q": w80.real / (2.0 * abs(w80.imag)),
                       **_mp_pair(r80)})
    stable.sort(key=lambda d: -d["Q"])
    keep = [d for d in stable if d["n_stable"]]
    rec = {"n_seeds": len(seeds),
           "n_located_physical_quadrant": len(located),
           "n_stable_located": len(keep),
           "top_five": stable[:5],
           "chosen": keep[0] if keep else None}
    if not keep:
        return rec, None
    # DEFECT D1, repaired 2026-08-04 after run 1 -- a TIGHTENING, no frozen
    # criterion changed.  The CERTIFIED root of a configuration is its
    # N_PRIMARY root, exactly as v2.4's is (its om_star = root(N_PRIMARY) and
    # its ladder measures against a coarser-than-primary reference).  Run 1
    # returned the N_REF root here, so gate G1 evaluated the n = 48 operator at
    # the n = 80 root and gate G10(b) mirrored across two different orders --
    # both then measured the LADDER separation instead of what they were frozen
    # to measure.  The tolerances are untouched.
    return rec, root_of(cfg, N_PRIMARY, complex(*keep[0]["Omega_n48"]))


def primary_chain(seed_A):
    """The frozen primary seed chain, reported whether or not it agrees."""
    rp, sd, _ = poly_root(CFG_BOUND_POLY, N_PRIMARY, seed=seed_A)
    out = {"Omega_A_seed": [seed_A.real, seed_A.imag],
           "poly_pencil_seed_double": [sd.real, sd.imag] if sd else None,
           "poly_polished": [float(rp.real), float(rp.imag)] if rp else None}
    for cfg in (CFG_BOUND_FROB, CFG_IN_FROB):
        r = root_of(cfg, N_PRIMARY, complex(rp)) if rp is not None else None
        out[cfg] = {"Omega": [float(r.real), float(r.imag)] if r else None,
                    "in_physical_quadrant":
                        bool(r is not None and _phys(complex(r)))}
    return out


# ===========================================================================
# GATES -- prereg section 5.  Every gate's self-test is executed and recorded
# in the same block, BEFORE the gate's own measurement is read.
# ===========================================================================
def gate_G_NC():
    """NEGATIVE CONTROL.  (a) operator level, (b) root level, vs v24."""
    om_a, _ = certified_rho_a()
    P = pencil_mp(N_PRIMARY, ELL, LAMBDA_PRIMARY, "A", WALL_NEUMANN, X_SAT, DPS)
    Q = V24.graded_matrices_mp(N_PRIMARY, ELL, LAMBDA_PRIMARY, X_SAT, DPS)
    N = N_PRIMARY + 1
    worst = mp.mpf(0)
    for k in range(3):
        for i in range(N):
            for j in range(N):
                d = abs(P[k][i, j] - Q[k][i, j])
                if d > worst:
                    worst = d
    r = root_of(CFG_A_CONTROL, N_PRIMARY, complex(om_a))
    sep = relsep(r, om_a) if r is not None else float("inf")
    # FT-NC: the same control with the inertia switch flipped to RHO-B.
    ft = root_of(CFG_BOUND_POLY, N_PRIMARY, complex(om_a))
    ft_sep = relsep(ft, om_a) if ft is not None else float("inf")
    return ({"a_operator_max_abs_diff": float(worst), "a_tol": TOL["G_NC_a"],
             "a_pass": bool(float(worst) <= TOL["G_NC_a"]),
             "b_root_relsep": sep, "b_tol": TOL["G_NC_b"],
             "b_pass": bool(sep <= TOL["G_NC_b"]),
             "pass": bool(float(worst) <= TOL["G_NC_a"] and sep <= TOL["G_NC_b"]),
             **_mp_pair(r)},
            {"measured": ft_sep, "threshold": FT_THRESH["FT_NC"],
             "fires": bool(ft_sep >= FT_THRESH["FT_NC"]),
             "mutation": "the inertia switch flipped to RHO-B inside the "
                         "negative control"})


def gate_G0():
    """L_eta == 4 eta^2 L_A, for BOTH inertia readings, on a frozen probe.

    The RHO-A limb re-derives v2.4's shipped coefficient Om^2/(S(1+S)); the
    RHO-B limb is the DERIVED Om^2 (1 + S^2)/S^4 of prereg 2.3.  A single
    closed-form LA carries both through the rho/mu switch, so the identity
    tests the transformation and not a transcription of one special case."""
    def LA(f, df, d2f, A, ell, Om, lam, rho_mode):
        S = math.sqrt(1.0 - A ** 2)
        gh = -A / (1.0 - A ** 2)
        rom = (1.0 / S) if rho_mode == "A" else (1.0 / S ** 4)
        P = -2j * Om + 2.0 * A + A ** 2 * gh + 2j * Om * lam * A ** 2
        Q = (Om ** 2 * (rom - 1.0) / A ** 2 - 1j * Om * gh - ell * (ell + 1)
             + 2.0 * A * gh
             + 1j * Om * lam * (-2j * Om + 2.0 * A + A ** 2 * gh)
             - Om ** 2 * lam ** 2 * A ** 2)
        return A ** 2 * d2f + P * df + Q * f

    worst, worst_c = 0.0, 0.0
    for rho_mode in ("A", "B"):
        for lam in LAMBDA_SET:
            for ell in (2, 3):
                for Om in (0.9 - 0.3j, 2.5 - 1.1j, 14.0 - 6.0j):
                    for e in (0.13, 0.37, 0.61, 0.88, 0.97):
                        A = 1.0 - e ** 2
                        f = math.exp(0.7 * A) * (1.0 + 0.3 * A ** 2)
                        df = math.exp(0.7 * A) * (0.7 + 0.6 * A + 0.21 * A ** 2)
                        d2f = math.exp(0.7 * A) * (1.09 + 0.84 * A
                                                   + 0.147 * A ** 2)
                        de = df * (-2.0 * e)
                        d2e = d2f * (4.0 * e ** 2) + df * (-2.0)
                        ea = np.array([e])
                        for corrupt, slot in ((0.0, "ok"),
                                              (FT_MUT["FT_0_corrupt"], "bad")):
                            Ac, B0, B1, C0, C1, C2 = coeff_parts(
                                ea, ell, lam, rho_mode, corrupt_C0=corrupt)
                            lhs = (Ac[0] * d2e + (B0[0] + Om * B1[0]) * de
                                   + (C0[0] + Om * C1[0] + Om ** 2 * C2[0]) * f)
                            rhs = 4.0 * e ** 2 * LA(f, df, d2f, A, ell, Om,
                                                    lam, rho_mode)
                            rel = abs(lhs - rhs) / max(abs(rhs), 1e-300)
                            if slot == "ok":
                                worst = max(worst, rel)
                            else:
                                worst_c = max(worst_c, rel)
    return ({"measured": worst, "tol": TOL["G0"],
             "pass": bool(worst <= TOL["G0"]),
             "note": "both inertia readings exercised through one closed form"},
            {"measured": worst_c, "threshold": FT_THRESH["FT_0"],
             "fires": bool(worst_c >= FT_THRESH["FT_0"]),
             "mutation": "C0 corrupted by 1e-12 relative"})


def gate_G_IND(om_star):
    """The derived indicial identity sigma(sigma-1) + Om^2 = 0, in mp."""
    mp.mp.dps = DPS
    sp, sm = sigma_pair(om_star)
    o2 = mp.mpc(om_star) ** 2
    rp = abs(sp * (sp - 1) + o2)
    rm = abs(sm * (sm - 1) + o2)
    w = float(max(rp, rm))
    return {"measured": w, "tol": TOL["G_IND"], "pass": bool(w <= TOL["G_IND"]),
            "sigma_plus": [float(sp.real), float(sp.imag)],
            "sigma_minus": [float(sm.real), float(sm.imag)]}


def gate_G_FROB(om_star, sigma):
    """The derived Frobenius row: the prereg 2.5 bracket vanishes LINEARLY.

        bracket(eta) = ( A sigma(sigma-1) + eta^2 C )/eta + sigma B
    is evaluated in mp at eta = 1e-5 and eta = 1e-15; a first-order zero gives
    a ratio of exactly 1e-10, so the frozen gate is ratio <= 1e-9."""
    mp.mp.dps = DPS
    sg = mp.mpc(sigma)
    o = mp.mpc(om_star)
    vals = {}
    for k in (5, 15):
        e = mp.mpf(10) ** (-k)
        Asq, B0, B1, C0, C1, C2 = coeff_parts_mp(e, ELL, LAMBDA_PRIMARY, "B")
        Bc = B0 + o * B1
        Cc = C0 + o * C1 + o ** 2 * C2
        vals[k] = abs((Asq * sg * (sg - 1) + e ** 2 * Cc) / e + sg * Bc)
    ratio = float(vals[15] / vals[5]) if vals[5] != 0 else 0.0
    return {"bracket_1e5": float(vals[5]), "bracket_1e15": float(vals[15]),
            "ratio": ratio, "tol": TOL["G_FROB"],
            "pass": bool(ratio <= TOL["G_FROB"])}


def _wall_limbs(om):
    """G-W's four limbs plus the REPORTED (non-gated) traction exponents."""
    sp, sm = sigma_pair(om)
    delta = sp - sm
    # DEFECT D2, repaired 2026-08-04 after run 1 -- a TIGHTENING, no frozen
    # criterion changed.  The frozen limb (iv) reads
    #     min_k |(sigma_+ - sigma_-) - k| > RESONANCE_GUARD, 1 <= k <= 20
    # i.e. the COMPLEX distance from Delta to an integer.  Run 1 computed
    # | |Delta| - k |, the distance from Delta's MODULUS, which is a different
    # and weaker quantity.
    dist = min(abs(delta - k) for k in range(1, 21))
    return {
        "sigma_plus": [float(sp.real), float(sp.imag)],
        "sigma_minus": [float(sm.real), float(sm.imag)],
        "abs_sigma_gap": float(abs(delta)),
        "i_finite_energy_sigma_plus": bool(float(sp.real) > 0.5),
        "ii_limit_point_sigma_minus": bool(float(sm.real) <= 0.5),
        "iii_ordering": bool(float((sp - sm).real) > 0.0),
        "iv_nonresonant": bool(dist > RESONANCE_GUARD),
        "resonance_distance": float(dist),
        "_resonance_metric": "min over integers 1 <= k <= 20 of the COMPLEX distance |(sigma_+ - sigma_-) - k| (prereg 5, G-W limb iv)",
        "traction_exponent_plus": float(sp.real) - 1.0,
        "traction_exponent_minus": float(sm.real) - 1.0,
    }


def gate_G_W(om_star):
    lim = _wall_limbs(om_star)
    ok = all(lim[k] for k in ("i_finite_energy_sigma_plus",
                              "ii_limit_point_sigma_minus",
                              "iii_ordering", "iv_nonresonant"))
    ft = _wall_limbs(mp.mpc(OMEGA_FTW))
    fires = (not ft["iii_ordering"]) and (not ft["iv_nonresonant"])
    return ({**lim, "pass": bool(ok)},
            {**ft, "fires": bool(fires),
             "mutation": f"wall classifier evaluated at the degenerate trial "
                         f"point Omega = {OMEGA_FTW}, where sqrt(1-4 Om^2) = 0"})


def gate_G1(cfg, om_star):
    vec, resid = eigenfunction(cfg, N_PRIMARY, om_star)
    off = om_star * (1 + mp.mpf(FT_MUT["FT_1_offset"]))
    ft = residual_at(cfg, N_PRIMARY, off, vec)
    return ({"measured": float(resid), "tol": TOL["G1"],
             "pass": bool(float(resid) <= TOL["G1"]),
             "dps": DPS, "n": N_PRIMARY, "invit_rounds": INVIT_ROUNDS},
            {"measured": ft, "threshold": FT_THRESH["FT_1"],
             "fires": bool(ft >= FT_THRESH["FT_1"]),
             "mutation": "residual evaluated at Omega_star*(1 + 1e-10)"}, vec)


def _fit_power(ns, errs):
    """ln e = lnC - p ln n  by OLS.  Returns (p, lnC, max|resid|)."""
    xs = [math.log(n) for n in ns]
    ys = [math.log(e) for e in errs]
    k = len(xs)
    mx, my = sum(xs) / k, sum(ys) / k
    den = sum((x - mx) ** 2 for x in xs)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / den
    a = my - b * mx
    res = max(abs(y - (a + b * x)) for x, y in zip(xs, ys))
    return -b, a, res


def _fit_rootexp(ns, errs):
    """ln e = lnC - c sqrt(n)  by OLS.  Returns (c, lnC, max|resid|)."""
    xs = [math.sqrt(n) for n in ns]
    ys = [math.log(e) for e in errs]
    k = len(xs)
    mx, my = sum(xs) / k, sum(ys) / k
    den = sum((x - mx) ** 2 for x in xs)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / den
    a = my - b * mx
    res = max(abs(y - (a + b * x)) for x, y in zip(xs, ys))
    return -b, a, res


def gate_G2(cfg, om_star):
    """n-independence over N_LADDER_CERT against N_REF, plus G2c's law."""
    ref = root_of(cfg, N_REF, complex(om_star))
    rows, errs = [], []
    for n in N_LADDER_CERT:
        r = root_of(cfg, n, complex(om_star))
        e = relsep(r, ref) if r is not None else float("inf")
        rows.append(_row(n, r, err_vs_ref=e))
        errs.append(e)
    worst = max(errs)
    tol = G2_TOL[cfg]
    law = LAW[cfg]
    fit = (_fit_rootexp if law == "rootexp" else _fit_power)(
        list(N_LADDER_CERT), errs)
    floor = TOL["G2c_c_floor"] if law == "rootexp" else TOL["G2c_p_floor"]
    g2c = {"law": law, "parameter": fit[0], "floor": floor,
           "lnC": fit[1], "max_resid": fit[2],
           "resid_floor": TOL["G2c_resid"],
           "pass": bool(fit[0] >= floor and fit[2] <= TOL["G2c_resid"])}
    # FT-2: under-resolved order.  FT-2c: stagnation of every non-reference rung.
    ru = root_of(cfg, N_UNDER, complex(om_star))
    ft2 = relsep(ru, ref) if ru is not None else float("inf")
    stag = [e + FT_MUT["FT_2c_stagnate"] for e in errs]
    sfit = (_fit_rootexp if law == "rootexp" else _fit_power)(
        list(N_LADDER_CERT), stag)
    return ({"rows": rows, "measured": worst, "tol": tol,
             "pass": bool(worst <= tol), "reference_n": N_REF,
             **_mp_pair(ref)},
            g2c,
            {"measured": ft2, "threshold": FT_THRESH["FT_2"],
             "fires": bool(ft2 >= FT_THRESH["FT_2"]),
             "mutation": f"under-resolved n = {N_UNDER}"},
            {"parameter": sfit[0], "floor": floor,
             "fires": bool(sfit[0] < floor),
             "mutation": "stagnation: 1e-12 added to every non-reference rung"})


def gate_G3(cfg, om_star):
    vals = []
    for lam in LAMBDA_SET:
        r = root_of(cfg, N_PRIMARY, complex(om_star), lam=lam)
        vals.append(r)
    worst = 0.0
    for i in range(len(vals)):
        for j in range(i + 1, len(vals)):
            if vals[i] is None or vals[j] is None:
                worst = float("inf")
            else:
                worst = max(worst, relsep(vals[i], vals[j]))
    ft = root_of(cfg, N_PRIMARY, complex(om_star), lam=LAMBDA_SET[0],
                 omit_lam_C2=True)
    ftv = relsep(ft, vals[0]) if (ft is not None and vals[0] is not None) \
        else float("inf")
    tol = G3_TOL[cfg]
    return ({"lambda_set": list(LAMBDA_SET), "measured": worst, "tol": tol,
             "pass": bool(worst <= tol)},
            {"measured": ftv, "threshold": FT_THRESH["FT_3"],
             "fires": bool(ftv >= FT_THRESH["FT_3"]),
             "mutation": "half-applied gauge: lambda in the factoring but "
                         "omitted from the Om^2 coefficient"})


def gate_G4(cfg, om_star):
    hi = root_of(cfg, N_PRIMARY, complex(om_star), dps=DPS_HIGH)
    lo = root_of(cfg, N_PRIMARY, complex(om_star), dps=DPS)
    a = relsep(hi, lo) if (hi is not None and lo is not None) else float("inf")
    ft_lo = root_of(cfg, N_PRIMARY, complex(om_star), dps=DPS_FT4)
    fta = relsep(ft_lo, lo) if (ft_lo is not None) else float("inf")
    out = {"a_measured": a, "a_tol": TOL["G4a"], "a_pass": bool(a <= TOL["G4a"])}
    ftb = None
    if CFG_SPEC[cfg][1] != WALL_FROB:
        worst = 0.0
        for n in N_LADDER:
            r = root_of(cfg, n, complex(om_star))
            _, sd, _ = poly_root(cfg, n, seed=complex(om_star))
            if r is None or sd is None:
                worst = float("inf")
            else:
                worst = max(worst, abs(complex(r) - sd) / abs(complex(r)))
        out.update({"b_measured": worst, "b_tol": TOL["G4b"],
                    "b_pass": bool(worst <= TOL["G4b"])})
        _, sd8, _ = poly_root(cfg, N_UNDER, seed=complex(om_star))
        r48 = root_of(cfg, N_PRIMARY, complex(om_star))
        ftb = abs(sd8 - complex(r48)) / abs(complex(r48)) if sd8 else float("inf")
        out["pass"] = bool(out["a_pass"] and out["b_pass"])
    else:
        out.update({"b_measured": None, "b_tol": TOL["G4b"], "b_pass": None,
                    "b_note": "N/A -- the Frobenius operator admits no "
                              "companion linearization (prereg 4.1)"})
        out["pass"] = bool(out["a_pass"])
    return (out,
            {"a_measured": fta, "a_threshold": FT_THRESH["FT_4a"],
             "b_measured": ftb, "b_threshold": FT_THRESH["FT_4b"],
             "fires": bool(fta >= FT_THRESH["FT_4a"]
                           and (ftb is None or ftb >= FT_THRESH["FT_4b"])),
             "mutation": f"(a) dps = {DPS_FT4}; (b) double pencil at "
                         f"n = {N_UNDER} vs mp at n = {N_PRIMARY}"})


def isolation_row(cfg, n, centre, **mut):
    _, _, spec = poly_root(cfg, n, seed=centre, **mut)
    inside = [z for z in spec if abs(z - centre) <= R_ISO]
    return {"n": n, "centre": [centre.real, centre.imag],
            "count_within_R_iso": len(inside), "pencil_total": len(spec)}


def gate_G5(cfg, om_star):
    centre = complex(om_star)
    rows = [isolation_row(cfg, n, centre) for n in N_LADDER]
    counts = [r["count_within_R_iso"] for r in rows]
    ftc = [isolation_row(cfg, n, V24.OMEGA_ARTIFACT)["count_within_R_iso"]
           for n in N_LADDER]
    return ({"R_iso": R_ISO, "rows": rows, "counts": counts,
             "pass": bool(all(c == 1 for c in counts))},
            {"counts": ftc, "fires": bool(any(c != 1 for c in ftc)),
             "mutation": "isolation pointed at the v2.1-banked artifact "
                         "Omega_art (K14, read from the read-only import)"})


def gate_G8(cfg, om_star):
    vals = {}
    for xs in X_SAT_SET:
        r = root_of(cfg, N_PRIMARY, complex(om_star), x_sat=xs)
        vals[xs] = r
    ks = list(X_SAT_SET)
    worst = 0.0
    for i in range(len(ks)):
        for j in range(i + 1, len(ks)):
            a, b = vals[ks[i]], vals[ks[j]]
            worst = float("inf") if (a is None or b is None) \
                else max(worst, relsep(a, b))
    ft = root_of(cfg, N_PRIMARY, complex(om_star), x_sat=X_SAT_SET[0],
                 perturb_A=FT_MUT["FT_8_perturb"] * (X_SAT_SET[0] - 7.0) / 7.0)
    base = vals[X_SAT_SET[0]]
    ftv = relsep(ft, base) if (ft is not None and base is not None) else 0.0
    ft2 = root_of(cfg, N_PRIMARY, complex(om_star), x_sat=X_SAT_SET[2],
                  perturb_A=FT_MUT["FT_8_perturb"] * (X_SAT_SET[2] - 7.0) / 7.0)
    b2 = vals[X_SAT_SET[2]]
    ftv = max(ftv, relsep(ft2, b2) if (ft2 is not None and b2 is not None) else 0.0)
    return ({"x_sat_set": list(X_SAT_SET), "measured": worst, "tol": TOL["G8"],
             "pass": bool(worst <= TOL["G8"])},
            {"measured": ftv, "threshold": FT_THRESH["FT_8"],
             "fires": bool(ftv >= FT_THRESH["FT_8"]),
             "mutation": "x_sat-dependent profile perturbation "
                         "1e-6*(x_sat-7)/7"})


def gate_G10(cfg, om_star):
    """Ax-3.  (a) the operator's reality structure; (b) conjugate mirror."""
    mp.mp.dps = DPS
    rho_mode = CFG_SPEC[cfg][0]
    worst = mp.mpf(0)
    eta, _, _ = cheb_mp(N_PRIMARY, DPS)
    for e in eta:
        Asq, B0, B1, C0, C1, C2 = coeff_parts_mp(e, ELL, 0.0, rho_mode)
        for z in (Asq, B0, C0, C2):
            worst = max(worst, abs(mp.im(mp.mpc(z))))
        for z in (B1, C1):
            worst = max(worst, abs(mp.re(mp.mpc(z))))
    mirror = root_of(cfg, N_PRIMARY, complex(-om_star.real, om_star.imag))
    b = relsep(mirror, -mp.conj(om_star)) if mirror is not None else float("inf")
    ftl = root_of(cfg, N_PRIMARY, complex(om_star), loss=FT_MUT["FT_10_loss"])
    ftv = relsep(ftl, om_star) if ftl is not None else float("inf")
    wl = mp.mpf(0)
    for e in eta:
        parts = coeff_parts_mp(e, ELL, 0.0, rho_mode, loss=FT_MUT["FT_10_loss"])
        wl = max(wl, abs(mp.im(mp.mpc(parts[5]))))
    return ({"a_measured": float(worst), "a_tol": TOL["G10a"],
             "a_pass": bool(float(worst) <= TOL["G10a"]),
             "b_measured": b, "b_tol": TOL["G10b"],
             "b_pass": bool(b <= TOL["G10b"]),
             "pass": bool(float(worst) <= TOL["G10a"] and b <= TOL["G10b"])},
            {"a_measured": float(wl), "b_measured": ftv,
             "a_threshold": FT_THRESH["FT_10"], "b_threshold": FT_THRESH["FT_10"],
             "fires": bool(float(wl) >= FT_THRESH["FT_10"]
                           or ftv >= FT_THRESH["FT_10"]),
             "mutation": "smuggled Im(mu)/Re(mu) = 1e-3"})


def ft_short(om_star):
    """FT-SHORT -- THE load-bearing self-test.  Impose the REJECTED RHO-A
    traction-free row dpsi/deta(0) = 0 on the RHO-B operator and measure how
    far the located root moves.  A small move would mean the wall-row
    derivation of prereg 2.5 is doing no work."""
    r = poly_root(CFG_BOUND_POLY, N_PRIMARY, seed=complex(om_star))[0]
    M0, M1, M2 = pencil_mp(N_PRIMARY, ELL, LAMBDA_PRIMARY, "B", WALL_NEUMANN,
                           X_SAT, DPS)
    _, sd, _ = poly_root(CFG_BOUND_POLY, N_PRIMARY, seed=complex(om_star))
    Md0, Md1, Md2, _, _ = pencil_double(N_PRIMARY, ELL, LAMBDA_PRIMARY, "B",
                                        WALL_NEUMANN)
    spec = dedupe(list(pencil_spectrum(Md0, Md1, Md2)), DEDUPE_REL)
    s = min(spec, key=lambda z: abs(z - complex(om_star))) if spec else None
    rs = V24.mp_polish(M0, M1, M2, s, DPS) if s is not None else None
    sep = relsep(rs, om_star) if rs is not None else float("inf")
    return {"measured": sep, "threshold": FT_THRESH["FT_SHORT"],
            "fires": bool(sep >= FT_THRESH["FT_SHORT"]),
            "rejected_row_root": [float(rs.real), float(rs.imag)]
            if rs is not None else None,
            "mutation": "the REJECTED RHO-A traction-free row dpsi/deta(0) = 0 "
                        "imposed on the RHO-B operator"}


# ===========================================================================
# THE DERIVED-CONSEQUENCE APPENDIX -- prereg section 9.  FLAG OUTPUT ONLY.
# It repairs nothing, edits no leaf, prefers no FLAG-W branch and adjudicates
# nothing.  Every row is a two-line algebraic substitution on canon's own
# formulas: exact powers of S, plus a numeric evaluation at a frozen S grid.
# ===========================================================================
S_GRID = (1e-1, 1e-2, 1e-3)

# (tag, K exponent of S, K prefactor) and (tag, rho exponent, rho prefactor)
K_BRANCH = {"BULK-STIFF": (-1.0, 2.0), "BULK-SOFT": (1.0, 2.0),
            "SHEAR": (1.0, 1.0)}
RHO_READ = {"RHO-A": (0.0, 1.0), "RHO-B": (-3.0, 1.0)}


def appendix_flag_w():
    rows = []
    for ch, (ke, kp) in K_BRANCH.items():
        for rd, (re_, rp) in RHO_READ.items():
            c_exp = (ke - re_) / 2.0
            z_exp = (ke + re_) / 2.0
            pref = math.sqrt(kp * rp)
            verdict = ("VENTS (Z -> 0)" if z_exp > 0 else
                       "JAMS (Z -> infinity)" if z_exp < 0 else
                       "INDETERMINATE (Z -> a finite constant)")
            rows.append({
                "channel": ch, "inertia": rd,
                "K_exponent_of_S": ke, "rho_exponent_of_S": re_,
                "c_exponent_of_S": c_exp, "Z_exponent_of_S": z_exp,
                "Z_prefactor": pref,
                "Z_at_S_grid": [pref * s ** z_exp for s in S_GRID],
                "c_at_S_grid": [pref / math.sqrt(kp * rp) * math.sqrt(kp / rp)
                                * s ** c_exp for s in S_GRID],
                "wall_verdict": verdict})
    inverted = [r for r in rows
                if r["inertia"] == "RHO-B" and r["Z_exponent_of_S"] < 0
                and any(q["channel"] == r["channel"] and q["inertia"] == "RHO-A"
                        and q["Z_exponent_of_S"] > 0 for q in rows)]
    return {
        "S_grid": list(S_GRID),
        "rows": rows,
        "n_conclusions_inverted_by_RHO_B": len(inverted),
        "inverted_channels": sorted({r["channel"] for r in inverted}),
        "flag_w_sign_split_under_RHO_A": bool(
            any(r["channel"] == "BULK-SOFT" and r["inertia"] == "RHO-A"
                and r["Z_exponent_of_S"] > 0 for r in rows)
            and any(r["channel"] == "BULK-STIFF" and r["inertia"] == "RHO-A"
                    and r["Z_exponent_of_S"] < 0 for r in rows)),
        "flag_w_sign_split_under_RHO_B": bool(
            len({r["wall_verdict"] for r in rows
                 if r["inertia"] == "RHO-B" and r["channel"].startswith("BULK")})
            > 1),
        "_fence": "FLAG OUTPUT ONLY: repairs nothing, edits no KB leaf, mints "
                  "no claim, prefers no FLAG-W branch, adjudicates nothing; "
                  "this lane is SHEAR-CHANNEL ONLY and computes no bulk "
                  "eigenvalue, no polar mode and no coupled system",
    }


# ===========================================================================
# ADJUDICATION -- prereg section 7.  Precedence, per configuration:
#   BIN-B-N > BIN-B-W > BIN-B-S > BIN-B-P1 / BIN-B-P2 / BIN-B-P3
# ===========================================================================
_DIAG_FENCE = ("NOT ADJUDICATED.  A failure bin fired for this configuration "
               "under the frozen precedence, so these numbers are shipped as "
               "DIAGNOSTICS and NO bin verdict is banked from them.  They are "
               "reported so a successor inherits a measurement rather than a "
               "silence, exactly as v2.2 shipped the NOT-ADJUDICATED "
               "diagnostics v2.4 later certified.")


def _physics_numbers(om_star, cmp_):
    """The bin arithmetic.  Shipped EITHER as an adjudicated verdict OR, when a
    failure bin fires, as a clearly-labelled NOT-ADJUDICATED diagnostic -- the
    shape v2.2 used and v2.4 later certified.  A diagnostic is not a verdict
    and this driver never presents one as such."""
    om = complex(om_star)
    wr = om.real / X_SAT
    Q = om.real / (2.0 * abs(om.imag))
    d_om = wr / cmp_["omega_R_GR"] - 1.0
    d_q = Q / cmp_["Q_GR"] - 1.0
    p1 = ("BIN-B-P1-MATCH" if abs(d_om) < 0.03
          else "BIN-B-P1-NEAR" if abs(d_om) < 0.10 else "BIN-B-P1-MISS")
    p2 = ("BIN-B-P2-MATCH" if abs(d_q) < 0.03
          else "BIN-B-P2-NEAR" if abs(d_q) < 0.10 else "BIN-B-P2-MISS")
    dgr, dcv = abs(Q - cmp_["Q_GR"]), abs(Q - cmp_["Q_convention"])
    disc = ("BIN-B-P2-EQUIDISTANT" if abs(dgr - dcv) <= 1e-6
            else "BIN-B-P2-CLOSER-GR" if dgr < dcv
            else "BIN-B-P2-CLOSER-CONVENTION")
    da_om, da_q = abs(cmp_["D_omega_A"]), abs(cmp_["D_Q_A"])
    better_om, better_q = abs(d_om) < da_om, abs(d_q) < da_q
    if abs(abs(d_om) - da_om) <= 1e-6 and abs(abs(d_q) - da_q) <= 1e-6:
        p3 = "BIN-B-P3-NEUTRAL"
    elif better_om and better_q:
        p3 = "BIN-B-P3-RESCUE-BOTH"
    elif abs(d_om) > da_om and abs(d_q) > da_q:
        p3 = "BIN-B-P3-WORSE-BOTH"
    elif better_om != better_q:
        p3 = "BIN-B-P3-RESCUE-PARTIAL"
    else:
        p3 = "BIN-B-P3-NEUTRAL"
    return {
        "Omega": [om.real, om.imag], **_mp_pair(om_star), "abs_Omega": abs(om),
        "omega_R_M_g": wr, "omega_I_M_g": abs(om.imag) / X_SAT, "Q": Q,
        "D_omega": d_om, "D_Q": d_q,
        "BIN-B-P1": p1, "BIN-B-P2": p2, "BIN-B-P2-discriminator": disc,
        "dist_Q_to_GR": dgr, "dist_Q_to_convention": dcv,
        "BIN-B-P3": p3,
        "BIN-B-P3-RESCUE-DECISIVE": bool(p3 == "BIN-B-P3-RESCUE-BOTH"
                                         and abs(d_om) < 0.10
                                         and abs(d_q) < 0.10),
        "abs_D_omega_RHO_A": da_om, "abs_D_Q_RHO_A": da_q,
        "abs_D_omega_RHO_B": abs(d_om), "abs_D_Q_RHO_B": abs(d_q),
        "_class_P1": "BIN-B-P1 is VALUE-CONSISTENCY class, not emergence: "
                     "omega_R*M_g carries the GR-imported nu_vac through the "
                     "7 in r_sat",
        "_class_P2": "BIN-B-P2 is the nu_vac-FREE axis: Q = Re(Omega)/"
                     "(2*abs(Im(Omega))) contains no r_sat scale, so the "
                     "GR-imported 7 cancels exactly",
    }


def adjudicate(cfg, om_star, gates, fts, cmp_):
    out = {"configuration": cfg}
    if om_star is None:
        out.update({"bin": "BIN-B-N", "certification": "N/A -- no located root",
                    "BIN-B-P1": "N/A -- not adjudicated",
                    "BIN-B-P2": "N/A -- not adjudicated",
                    "BIN-B-P3": "N/A -- not adjudicated",
                    "BIN-B-4": "N/A BY CONSTRUCTION"})
        return out
    diag = _physics_numbers(om_star, cmp_)
    wall_ok = gates.get("G-W", {}).get("pass", False) if "G-W" in gates else True
    if not wall_ok:
        out.update({"bin": "BIN-B-W",
                    "certification": "N/A -- wall classification failed",
                    "BIN-B-P1": "N/A -- not adjudicated",
                    "BIN-B-P2": "N/A -- not adjudicated",
                    "BIN-B-P3": "N/A -- not adjudicated",
                    "BIN-B-4": "N/A BY CONSTRUCTION",
                    "not_adjudicated_diagnostics": diag,
                    "_diagnostic_fence": _DIAG_FENCE})
        return out
    failed = sorted(k for k, v in gates.items()
                    if isinstance(v, dict) and v.get("pass") is False)
    unfired = sorted(k for k, v in fts.items()
                     if isinstance(v, dict) and v.get("fires") is False)
    out["failed_gates"] = failed
    out["unfired_self_tests"] = unfired
    if failed or unfired:
        out.update({"bin": "BIN-B-S", "certification": "ROOT-NOT-CERTIFIED",
                    "BIN-B-P1": "N/A -- not adjudicated",
                    "BIN-B-P2": "N/A -- not adjudicated",
                    "BIN-B-P3": "N/A -- not adjudicated",
                    "BIN-B-4": "N/A BY CONSTRUCTION",
                    "not_adjudicated_diagnostics": diag,
                    "_diagnostic_fence": _DIAG_FENCE})
        return out
    out.update({"bin": "adjudicated", "certification": "ROOT-CERTIFIED",
                **diag, "BIN-B-4": "N/A BY CONSTRUCTION"})
    return out


def digest_of(obj):
    blob = json.dumps(obj, sort_keys=True, default=str).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:16]


# ===========================================================================
# MAIN
# ===========================================================================
def run_config(cfg, om_star, cmp_):
    """Every gate that APPLIES to this configuration, with its self-test."""
    gates, fts, na = {}, {}, {}
    if om_star is None:
        na["all-root-local"] = ("N/A -- BIN-B-N fired for this configuration; "
                                "a root-local gate has no root to be local to")
        return gates, fts, na, None
    if CFG_SPEC[cfg][0] == "B":
        gates["G-IND"] = gate_G_IND(om_star)
        if CFG_SPEC[cfg][1] == WALL_FROB:
            gates["G-FROB"] = gate_G_FROB(om_star, sigma_for(cfg, om_star))
        else:
            na["G-FROB"] = ("N/A -- this configuration carries no Frobenius "
                            "factoring (prereg 2.6)")
        gates["G-W"], fts["FT-W"] = gate_G_W(om_star)
    g1, ft1, vec = gate_G1(cfg, om_star)
    gates["G1"], fts["FT-1"] = g1, ft1
    g2, g2c, ft2, ft2c = gate_G2(cfg, om_star)
    gates["G2"], gates["G2c"] = g2, g2c
    fts["FT-2"], fts["FT-2c"] = ft2, ft2c
    gates["G3"], fts["FT-3"] = gate_G3(cfg, om_star)
    gates["G4"], fts["FT-4"] = gate_G4(cfg, om_star)
    if CFG_SPEC[cfg][1] != WALL_FROB:
        gates["G5"], fts["FT-5"] = gate_G5(cfg, om_star)
    else:
        na["G5"] = ("N/A BY CONSTRUCTION, disclosed in prereg 4.1 -- the "
                    "Frobenius operator admits no companion linearization, so "
                    "G5 certifies isolation for the POLY instrument only and "
                    "NO isolation claim of any kind is made here")
        na["G4(b)"] = "N/A BY CONSTRUCTION, same reason"
    gates["G8"], fts["FT-8"] = gate_G8(cfg, om_star)
    gates["G10"], fts["FT-10"] = gate_G10(cfg, om_star)
    return gates, fts, na, vec


def main():
    t0 = time.time()
    mp.mp.dps = DPS
    om_a, _ = certified_rho_a()
    seed_A = complex(om_a)
    cmp_ = comparators()

    # ---- THE STOP RULE (prereg 4.3).  Nothing RHO-B runs until this passes.
    g_nc, ft_nc = gate_G_NC()
    if not g_nc["pass"]:
        out = {"_prereg": "research/2026-08-04_coldq-axial-rhob_prereg-FROZEN.md",
               "_prereg_commit": "e3a4181d",
               "certification": "BIN-B-STOP",
               "negative_control": g_nc, "self_tests": {"FT-NC": ft_nc},
               "_stop": "the negative control failed; NO RHO-B number of any "
                        "kind was produced (prereg 4.3 stop rule)"}
        out["_digest"] = digest_of(out)
        out["_runtime_sec"] = round(time.time() - t0, 2)
        with open(os.path.join(_HERE, "coldq_axial_rhob_results.json"), "w",
                  encoding="utf-8") as fh:
            json.dump(out, fh, indent=1, sort_keys=True, default=str)
        print("BIN-B-STOP -- negative control failed")
        return out

    g0, ft0 = gate_G0()
    seeds, spec48 = enumerate_seeds(seed_A)
    chain = primary_chain(seed_A)

    searches, roots, gates_all, fts_all, na_all, adj = {}, {}, {}, {}, {}, {}
    for cfg in (CFG_A_CONTROL, CFG_BOUND_POLY, CFG_BOUND_FROB, CFG_IN_FROB):
        if cfg == CFG_A_CONTROL:
            # D1: the control's certified root is its N_PRIMARY root too.
            roots[cfg] = root_of(cfg, N_PRIMARY, seed_A)
            searches[cfg] = {"_note": "the negative control is seeded from the "
                                      "certified RHO-A root and is not searched"}
        else:
            searches[cfg], roots[cfg] = search(cfg, seeds, seed_A)
        g, f, n, _ = run_config(cfg, roots[cfg], cmp_)
        gates_all[cfg], fts_all[cfg], na_all[cfg] = g, f, n

    # ---- FT-SHORT: the load-bearing self-test.  It needs a RHO-B reference
    # root; the CFG-IN-FROB root is used if one exists, else the RHO-A root.
    ref_for_short = roots[CFG_IN_FROB] or roots[CFG_BOUND_FROB] or om_a
    fts_all["_global"] = {"FT-NC": ft_nc, "FT-0": ft0,
                          "FT-SHORT": ft_short(ref_for_short)}
    gates_all["_global"] = {"G-NC": g_nc, "G0": g0}

    # ---- G-AGREE: two-instrument agreement on the ROW-BOUND pair.
    rp, rf = roots[CFG_BOUND_POLY], roots[CFG_BOUND_FROB]
    if rp is not None and rf is not None:
        sep = relsep(rp, rf)
        agree = {"measured": sep, "tol": TOL["G_AGREE"],
                 "pass": bool(sep <= TOL["G_AGREE"])}
    else:
        agree = {"measured": None, "tol": TOL["G_AGREE"], "pass": None,
                 "note": "N/A BY OUTCOME -- BIN-B-N fired on at least one "
                         "member of the ROW-BOUND pair, so no two-instrument "
                         "agreement exists; prereg 5 froze that ROW-IN has NO "
                         "agreement gate at all"}
    gates_all["_global"]["G-AGREE"] = agree

    for cfg in (CFG_A_CONTROL, CFG_BOUND_POLY, CFG_BOUND_FROB, CFG_IN_FROB):
        merged = dict(gates_all[cfg])
        merged.update({"G0": g0})
        if cfg != CFG_A_CONTROL:
            adj[cfg] = adjudicate(cfg, roots[cfg], merged, fts_all[cfg], cmp_)
        else:
            failed = sorted(k for k, v in merged.items()
                            if isinstance(v, dict) and v.get("pass") is False)
            unf = sorted(k for k, v in fts_all[cfg].items()
                         if isinstance(v, dict) and v.get("fires") is False)
            adj[cfg] = {"configuration": cfg,
                        "certification": "ROOT-CERTIFIED" if not (failed or unf)
                                         else "ROOT-NOT-CERTIFIED",
                        "failed_gates": failed, "unfired_self_tests": unf,
                        "_role": "NEGATIVE CONTROL ONLY -- no physics bin"}

    scope = {}
    for cfg in gates_all:
        scope[cfg] = {"RUN": sorted(gates_all[cfg]),
                      "N/A-BY-CONSTRUCTION-OR-OUTCOME": na_all.get(cfg, {}),
                      "UNRUN-BY-OMISSION": []}

    out = {
        "_prereg": "research/2026-08-04_coldq-axial-rhob_prereg-FROZEN.md",
        "_prereg_commit": "e3a4181d",
        "_method": "compactified hyperboloidal Chebyshev spectral in A = "
                   "r_sat/r under A = 1 - eta^2, with the RHO-B wall handled "
                   "by an EXACT Frobenius factoring psi = eta^sigma phi; NO "
                   "winding, NO contour, NO argument principle, NO matching "
                   "radius, NO regularized modulus floor",
        "_one_change": "rho/mu: RHO-A Om^2/(S(1+S)) -> RHO-B Om^2(1+S^2)/S^4",
        "_wall_row": "DERIVED: dphi/deta(0) = 0 on phi = eta^(-sigma) psi, the "
                     "a_1 = 0 Frobenius analyticity constraint at a REGULAR "
                     "SINGULAR point; the RHO-A traction-free row is REJECTED "
                     "BY DERIVATION and exercised only by FT-SHORT",
        "_carry_over": "the numerical machinery is CARRIED OVER from v2.4 by "
                       "READ-ONLY IMPORT so the operator and the wall row are "
                       "the only variables; NO reimplementation independence "
                       "is claimed",
        "_non_claim": "this lane runs FORK-3(b); it does not adjudicate "
                      "FORK-3, does not prefer RHO-B over RHO-A, computes no "
                      "bulk quantity and CANNOT adjudicate FLAG-W",
        "_frozen_numerics": {
            "N_PRIMARY": N_PRIMARY, "N_LADDER": list(N_LADDER),
            "N_LADDER_CERT": list(N_LADDER_CERT), "N_REF": N_REF,
            "LAMBDA_SET": list(LAMBDA_SET), "DPS": DPS, "DPS_HIGH": DPS_HIGH,
            "X_SAT": X_SAT, "X_SAT_SET": list(X_SAT_SET), "ELL": ELL,
            "R_ISO": R_ISO, "NSTABLE_REL": NSTABLE_REL,
            "RESONANCE_GUARD": RESONANCE_GUARD, "OMEGA_FTW": OMEGA_FTW,
            "TOL": TOL, "FT_THRESH": FT_THRESH, "FT_MUT": FT_MUT},
        "_certification_scope": scope,
        "comparators": cmp_,
        "primary_seed_chain": chain,
        "seed_enumeration": {
            "n_pencil_total": len(spec48),
            "n_physical_quadrant": len(seeds),
            "rule": "ALL CFG-BOUND-POLY pencil eigenvalues in the physical "
                    "quadrant with |Om| <= 8, deduped at DEDUPE_REL; located "
                    "roots are then filtered to those n-stable between n = 48 "
                    "and n = 80 at NSTABLE_REL (prereg 7.1's BIN-B-N wording)"},
        "search": searches,
        "gates": gates_all,
        "self_tests": fts_all,
        "adjudication": adj,
        "appendix_flag_w": appendix_flag_w(),
        "_g9": "this driver emits NO pass field for G9; the determinism verdict "
               "is obtained solely by the external two-run diff recorded in the "
               "result doc",
    }
    out["_digest"] = digest_of(out)
    out["_runtime_sec"] = round(time.time() - t0, 2)
    with open(os.path.join(_HERE, "coldq_axial_rhob_results.json"), "w",
              encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, sort_keys=True, default=str)
    for cfg in (CFG_A_CONTROL, CFG_BOUND_POLY, CFG_BOUND_FROB, CFG_IN_FROB):
        a = adj[cfg]
        print(f"{cfg:18s} {a.get('certification'):22s} "
              f"{a.get('bin', '-'):14s} "
              f"P1={a.get('BIN-B-P1', '-')} P2={a.get('BIN-B-P2', '-')} "
              f"P3={a.get('BIN-B-P3', '-')}")
    print("digest", out["_digest"], " runtime", out["_runtime_sec"], "s")
    return out


if __name__ == "__main__":
    main()

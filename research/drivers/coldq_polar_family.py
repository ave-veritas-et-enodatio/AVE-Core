#!/usr/bin/env python3
"""Cold-Q POLAR FAMILY -- the coupled shear-bulk channel network.

Resolves the frozen gates and bins of
``research/2026-08-03_coldq-polar-family_prereg-FROZEN.md`` (commit d9015e38,
pushed ALONE BEFORE this file existed and before any number produced by this
instrument existed).

WHAT THIS IS.  The AXIAL (toroidal, pure shear-channel) l = 2 pole of the
graded saturation cavity was certified by the v2.4 lane.  That family is
exactly divergence-free, so the bulk modulus drops out identically.  THIS lane
builds the POLAR family -- the coupled shear + bulk two-line network, whose
displacement field carries BOTH a dilatation and a shear -- for the SAME
canonical profile.

WHY IT MATTERS (prereg section P.3, frozen).  Schwarzschild axial/polar
isospectrality is a THEOREM OF GR.  A medium carrying separate Z_shear and
Z_bulk generically SPLITS the two families.  A SPLIT is a forward divergent
prediction; a DEGENERACY is a nontrivial consistency.  Both readings were
committed in advance.

===========================================================================
CARRY-OVER DISCLOSURE (prereg section P.5, FROZEN) -- READ THIS FIRST
===========================================================================
This file is NOT an independent reimplementation of the v2.4 machinery.  It
CARRIES OVER, by COPY-WITH-ATTRIBUTION from
``research/drivers/coldq_pole_v2p4_root.py`` (blob
6758725b10ccec684021e13767fdf29349226973, on origin/main), the Chebyshev
differentiation matrices in double and in mp, the quadratic-pencil
linearization and its seeding path, the mp LU determinant and secant polish,
the mp inverse iteration, the relative-separation-in-mp helper and the root
cache.  Transcription sites carry ``[xcribe v2.4 ...]`` markers.  That file is
IMPORTED READ-ONLY by gate G-C(a) as a comparison object and is BYTE-UNTOUCHED.

NEW here, and therefore where any defect will live: the two-field coupled
operator, its symbolic derivation, the moduli grading, the branch fork, the
wall rows, the dilatation diagnostic, and gates G0(a), G0(c), G-C and G-P.

===========================================================================
THE FLAG-W FORK (prereg section 2.2(c), FROZEN) -- canon speaks with two voices
===========================================================================
  BRANCH-SOFT   K = 2*G_vac*S    (bulk-impedance-at-saturation-boundary.md:31)
  BRANCH-STIFF  K = 2*G_vac/S    (saturating-modulus-and-backreaction.md:57)
Both are CO-PRIMARY.  Neither is preferred.  Neither leaf is repaired here.

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
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.dirname(os.path.dirname(_HERE))
if os.path.join(_REPO, "src") not in sys.path:
    sys.path.insert(0, os.path.join(_REPO, "src"))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import mpmath as mp  # noqa: E402

from ave.core.constants import N_NU  # noqa: E402  (J13, read-only)

# ===========================================================================
# FROZEN NUMERICS (prereg section 4.2) -- ENGINEERING CHOICE, tagged (J17)
# ===========================================================================
N_PRIMARY = 48
N_LADDER = (32, 48, 64, 80)
N_LADDER_G2 = (48, 64, 80)
N_DIAG_G2 = tuple(n for n in N_LADDER if n not in N_LADDER_G2)

HGAUGE_PRIMARY = 0.0
HGAUGE_SET = (-0.25, 0.0, 0.25)
DPS = 50
DPS_HIGH = 80
DPS_FT4 = 20
DPS_COEFF_EXTRA = 30             # coefficient evaluation headroom (see below)
POLISH_TOL_EXP = 38
POLISH_ITERS = 60
INVIT_ROUNDS = 4
DEDUPE_REL = 1e-6
R_ISO = 0.5
X_SAT = 7.0
X_SAT_SET = (5.0, 7.0, 11.0)
ELL = 2
N_UNDER = 8
DILATATION_FLOOR = 1e-3          # G-P, prereg section 4.7
LOC_WINDOW = (1.0, 2.0)          # byte-identical to the axial lane's window
LOC_POINTS = 401
G2B_RESID_FLOOR = 0.40
G2B_C_FLOOR = 1.0                # prereg section 4.5 -- floor only, NO upper edge
FT2B_STAGNATION = 1e-12
RUNTIME_BUDGET_S = 7200.0

# SEED WINDOW + SEED RULE.  The prereg froze the METHOD ("polish seeded from
# the double-precision linearized pencil") but not the seed-selection rule.
# The rule below was CHOSEN BEFORE ANY RUN and is disclosed in the result doc:
#   keep double-pencil eigenvalues with Re > 0, Im < 0 and |Omega| <= 8;
#   require n-stability between n = 48 and n = 80 at 1e-3 relative;
#   take the LEAST DAMPED survivor (largest Re/(2|Im|)).
# It makes NO completeness claim and no mode count.  A second, independent
# seed -- the certified AXIAL root -- is ALSO polished and both are reported.
SEED_ABS_MAX = 8.0
SEED_STABILITY_REL = 1e-3

# FROZEN tolerances (prereg section 5)
TOL = {
    "G0a": 1e-12, "G0b": 1e-12,
    "G1": 1e-20, "G2": 1e-8, "G3": 1e-10,
    "G4a": 1e-25, "G4b": 1e-5,
    "GCa": 1e-40, "GCb": 1e-10, "GCc": 1e-6,
    "GP": DILATATION_FLOOR,
    "G8": 1e-9, "G10a": 1e-40, "G10b": 1e-20,
}
FT_THRESH = {
    "FT_0a": 1e-12, "FT_0b": 1e-12,
    "FT_1": 1e-15, "FT_2": 1e-6, "FT_3": 1e-6,
    "FT_4a": 1e-25, "FT_4b": 1e-6,
    "FT_5": 1e-8,
    "FT_C_op": 1e-40, "FT_C_root": 1e-3,
    "FT_P": DILATATION_FLOOR,
    "FT_8": 1e-9, "FT_10a": 1e-6, "FT_10b": 1e-5,
}
FT_MUT = {
    "FT_0a_coupling": 1e-9,
    "FT_0b_chain": 1e-9,
    "FT_1_offset": 1e-10,
    "FT_3_hgauge": 0.25,
    "FT_8_perturb": 1e-6,
    "FT_9_perturb": 1e-15,
    "FT_10_loss": 1e-3,
}

# J14 / GR comparators, read PROGRAMMATICALLY at run time.
RERUN_PY = os.path.join(_REPO, "research",
                        "2026-07-20_v1-spin-mapping-adjudication_rerun.py")
RINGDOWN_PY = os.path.join(_REPO, "research",
                           "2026-07-20_ringdown-systematics_checks.py")
# J15 / J16 -- the merged, CERTIFIED axial lane's shipped object.  Read
# PROGRAMMATICALLY; nothing about it is typed here.
AXIAL_JSON = os.path.join(_HERE, "coldq_pole_v2p4_root_results.json")


# ===========================================================================
# CHEBYSHEV -- double precision
# [xcribe v2.4 coldq_pole_v2p4_root.py::cheb -- standard CGL differentiation
#  matrix, ASCENDING on [0,1]]
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
    """Barycentric interpolation from CGL nodes (ascending on [0,1]).
    [xcribe v2.4 coldq_pole_v2p4_root.py::cheb_interp]"""
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
    """CGL nodes + D + D2 built ENTIRELY in mp.
    [xcribe v2.4 coldq_pole_v2p4_root.py::cheb_mp -- the B1 lesson of v2.1]"""
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
# G0(c) -- THE SYMBOLIC DERIVATION OF THE COUPLED POLAR RADIAL SYSTEM
#
# Re-executed here rather than trusted (prereg section 2.1, frozen).  The
# graded-moduli Navier operator
#     div T = lam_L' Delta rhat + (lam_L + mu) grad Delta + mu lap u
#             + 2 mu' (e . rhat)
# is applied to the polar ansatz  u = U(r) Y rhat + V(r) grad_1 Y  with
# Y = P_ell(cos th) (m = 0, which loses no generality: the radial system is
# m-independent), projected onto Y and onto dY/dth, checked theta-separable,
# and checked EXACTLY AFFINE in L = ell(ell+1) by three-point interpolation.
# ===========================================================================
def derive_radial_system(ell, perturb_L_coeff=0.0):
    """Return (radial_eq, tangential_eq) as sympy expressions == 0."""
    r, th = sp.symbols('r theta', positive=True)
    w2 = sp.symbols('omega2')
    U = sp.Function('U')(r)
    V = sp.Function('V')(r)
    lamL = sp.Function('lamL')(r)
    mu = sp.Function('mu')(r)
    rho = sp.Function('rho')(r)

    Y = sp.legendre(ell, sp.cos(th))
    dY = sp.diff(Y, th)
    ur, ut = U * Y, V * dY

    Delta = sp.simplify(sp.diff(r ** 2 * ur, r) / r ** 2
                        + sp.diff(sp.sin(th) * ut, th) / (r * sp.sin(th)))
    e_rr = sp.diff(ur, r)
    e_rth = sp.Rational(1, 2) * (sp.diff(ut, r) - ut / r + sp.diff(ur, th) / r)

    def slap(f):
        return (sp.diff(r ** 2 * sp.diff(f, r), r) / r ** 2
                + sp.diff(sp.sin(th) * sp.diff(f, th), th)
                / (r ** 2 * sp.sin(th)))

    lap_r = (slap(ur) - 2 * ur / r ** 2
             - 2 * (sp.diff(ut, th) + sp.cos(th) / sp.sin(th) * ut) / r ** 2)
    lap_t = (slap(ut) - ut / (r ** 2 * sp.sin(th) ** 2)
             + 2 * sp.diff(ur, th) / r ** 2)

    coup = (lamL + mu) * (1 + _ex(perturb_L_coeff))  # FT-0(a) hook
    divT_r = (sp.diff(lamL, r) * Delta + coup * sp.diff(Delta, r)
              + mu * lap_r + 2 * sp.diff(mu, r) * e_rr)
    divT_t = (coup * sp.diff(Delta, th) / r
              + mu * lap_t + 2 * sp.diff(mu, r) * e_rth)

    eq_r = sp.simplify(sp.expand(divT_r + rho * w2 * ur) / Y)
    eq_t = sp.simplify(sp.expand(divT_t + rho * w2 * ut) / dY)
    return eq_r, eq_t


def gate_G0c():
    """The derivation is re-run for ell in {2, 3, 4}; theta-separability and
    the affine-in-L three-point residual must both be EXACTLY zero."""
    th = sp.symbols('theta', positive=True)
    Ls, out = sp.symbols('L'), {}

    def run(perturb):
        rows, seps = {}, []
        for ell in (2, 3, 4):
            er, et = derive_radial_system(ell, perturb)
            seps.append(sp.simplify(sp.diff(er, th)))
            seps.append(sp.simplify(sp.diff(et, th)))
            rows[ell * (ell + 1)] = (sp.simplify(er), sp.simplify(et))
        sep_ok = all(s == 0 for s in seps)
        keys = sorted(rows)
        res = []
        for idx in (0, 1):
            a, b = rows[keys[0]][idx], rows[keys[1]][idx]
            La, Lb = keys[0], keys[1]
            guess = a + (Ls - La) * (b - a) / (Lb - La)
            res.append(sp.simplify(sp.expand(
                guess.subs(Ls, keys[2]) - rows[keys[2]][idx])))
        return sep_ok, res

    sep_ok, res = run(0.0)
    affine_ok = all(x == 0 for x in res)
    _, mres = run(FT_MUT["FT_0a_coupling"])
    mut_nonzero = any(x != 0 for x in mres)
    out["separability_residual_exactly_zero"] = bool(sep_ok)
    out["affine_in_L_residual_exactly_zero"] = bool(affine_ok)
    out["ells_derived"] = [2, 3, 4]
    out["pass"] = bool(sep_ok and affine_ok)
    ft = {"mutation": "the (lam_L + mu) coupling coefficient scaled by "
                      f"(1 + {FT_MUT['FT_0a_coupling']}) in the SYMBOLIC "
                      "derivation",
          "affine_residual_becomes_nonzero": bool(mut_nonzero),
          "fires": bool(mut_nonzero)}
    return out, ft


# ===========================================================================
# THE MEDIUM (prereg sections 2.2, 2.3) -- symbolic, per branch
#
#   A = 1 - eta^2 ;  S = sqrt(1 - A^2) = eta*sqrt(2 - eta^2) ;  r = r_sat/A
#   mu   = G_vac*S                                        (Op16, both branches)
#   K    = 2*G_vac*S      BRANCH-SOFT   (Gamma_bulk = -1, the wall VENTS)
#   K    = 2*G_vac/S      BRANCH-STIFF  (Gamma_bulk = +1, the wall JAMS)
#   lamL = K - 2*mu/3 ;  beta = lamL + 2*mu = K + 4*mu/3
#   rho  = 1              RHO-A         |  rho = 1/S^3   RHO-B  (FORK-3(b))
# Units: c_0 = rho_bulk = G_vac = 1.
# ===========================================================================
_ETA, _OM, _RS = sp.symbols('eta Om rs')
# uu stands for sqrt(2 - eta^2), so that S = eta*uu EXACTLY and the whole
# medium is RATIONAL in (eta, uu).  This is what lets the 1/A^2 poles of the
# factoring cancel ALGEBRAICALLY (they must: the axial lane's published
# residual Om^2/(S(1+S)) is exactly that cancellation) instead of being
# evaluated as inf*0 at the compactified infinity eta = 1.
_U = sp.Symbol('uu')


def _redpoly(e):
    """Reduce uu**k (k >= 2) using uu**2 = 2 - eta**2."""
    e = sp.expand(e)
    while True:
        new = sp.expand(e.replace(
            lambda x: x.is_Pow and x.base == _U
            and x.exp.is_Integer and x.exp >= 2,
            lambda x: (2 - _ETA ** 2) ** (x.exp // 2) * _U ** (x.exp % 2)))
        if new == e:
            return e
        e = new


def _reduce_u(expr, tries=4):
    """Clear the compactified-infinity pole ALGEBRAICALLY.

    The factoring's 1/A^2 poles cancel against the medium's 1 - S = 1 - eta*uu
    -- but only MODULO uu^2 = 2 - eta^2, since A^2 = (1 - eta*uu)(1 + eta*uu)
    holds only under that relation.  sympy's cancel works in QQ[eta, uu]
    WITHOUT the relation and therefore cannot see the common factor.  The fix
    is to rationalize: multiply numerator and denominator by (1 + eta*uu)
    (an identity operation) and re-reduce, until the denominator no longer
    vanishes at the compactified infinity eta = 1, uu = 1.
    """
    num, den = sp.fraction(sp.together(expr))
    num, den = _redpoly(num), _redpoly(den)
    for _ in range(tries):
        r = sp.cancel(num / den)
        num, den = sp.fraction(sp.together(r))
        if sp.simplify(den.subs({_ETA: 1, _U: 1})) != 0:
            return r
        num = _redpoly(sp.expand(num * (1 + _ETA * _U)))
        den = _redpoly(sp.expand(den * (1 + _ETA * _U)))
    return sp.cancel(num / den)


def _to_eval(expr):
    """Cancel the poles algebraically, THEN put the radical back."""
    return _reduce_u(expr).subs(_U, sp.sqrt(2 - _ETA ** 2))


def _d(X):
    """d/deta, with uu KNOWN to be sqrt(2 - eta^2) rather than an opaque
    symbol: d(uu)/d(eta) = -eta/uu.

    ★ This helper exists because omitting it is a silent, plausible-looking
    bug: a bare sp.diff(S, eta) with S = eta*uu returns uu instead of the
    correct 2A/uu, which corrupts EVERY modulus gradient in the operator --
    i.e. exactly the coupling the polar family is built to measure.  It was
    caught by the reduction gate G-C against the certified axial operator
    BEFORE any physics number was produced, and the helper is named and
    commented so it cannot be quietly dropped.
    """
    return sp.diff(X, _ETA) + sp.diff(X, _U) * (-_ETA / _U)


def _ex(x):
    """Exact sympy rational from a Python float -- keeps the whole symbolic
    chain free of binary-float contamination, so that G-C(a)'s operator
    identity is an ALGEBRAIC identity rather than a float coincidence."""
    if isinstance(x, sp.Expr):
        return x
    return sp.nsimplify(sp.Float(repr(float(x)), 25), rational=True)


def medium(branch, rho_mode, perturb_A=0.0, loss=0.0):
    # S = eta*uu is the UNPERTURBED kernel; perturb_A scales the EXPLICIT A
    # appearances only.  [xcribe v2.4 coldq_pole_v2p4_root.py::
    # graded_coeff_parts -- that lane perturbs A and leaves S = eta*u alone,
    # and FT-8 is transcribed faithfully rather than reinterpreted.]
    A = (1 - _ETA ** 2) * (1 + _ex(perturb_A))
    S = _ETA * _U
    mu = S * (1 + sp.I * _ex(loss))            # FT-10 hook: Im(mu)/Re(mu)
    K = 2 * S if branch == "SOFT" else 2 / S
    lamL = K - 2 * mu / 3
    rho = sp.Integer(1) if rho_mode == "A" else 1 / S ** 3
    return A, S, mu, lamL, lamL + 2 * mu, rho


def _rform(branch, rho_mode, ell, chain_pert=0.0, decouple=False,
           perturb_A=0.0, loss=0.0):
    """The r-form coefficients of the DERIVED system, divided by the leading
    modulus of each equation (the axial lane's normalization), as sympy
    expressions in eta and Om.

    Returns (bU, cU, bUV, cUV, bV, cV, bVU, cVU) where equation 1 is
        U'' + bU U' + cU U + bUV V' + cUV V = 0
    and equation 2 is
        V'' + bV V' + cV V + bVU U' + cVU U = 0 .
    """
    A, S, mu, lamL, beta, rho = medium(branch, rho_mode, perturb_A, loss)
    r = _RS / A
    L = ell * (ell + 1)
    q = A ** 2 / (2 * _ETA * _RS) * (1 + _ex(chain_pert))   # FT-0(b) hook

    def ddr(f):
        return q * _d(f)

    om2 = _OM ** 2 / _RS ** 2
    dlam, dmu = ddr(lamL), ddr(mu)
    a11, a22 = beta, mu
    bU = (dlam + 2 * dmu) / a11 + 2 / r
    cU = (rho * om2 - (2 * beta + L * mu) / r ** 2 + 2 * dlam / r) / a11
    bV = dmu / a22 + 2 / r
    cV = (rho * om2 - dmu / r - L * beta / r ** 2) / a22
    if decouple:                                       # G-C(c) hook
        z = sp.Integer(0)
        return bU, cU, z, z, bV, cV, z, z
    bUV = -L * (lamL + mu) / (r * a11)
    cUV = (-L * dlam / r + L * (lamL + 3 * mu) / r ** 2) / a11
    bVU = (lamL + mu) / (r * a22)
    cVU = (dmu / r + 2 * beta / r ** 2) / a22
    return bU, cU, bUV, cUV, bV, cV, bVU, cVU


def _rform_toroidal(rho_mode, ell, chain_pert=0.0, perturb_A=0.0, loss=0.0):
    """The AXIAL (toroidal) single-field r-form, already divided by mu:
        W'' + (2/r + mu'/mu) W' + [rho w^2/mu - L/r^2 - (mu'/mu)/r] W = 0
    This is the object gate G-C compares against v2.4's certified operator."""
    A, S, mu, lamL, beta, rho = medium("SOFT", rho_mode, perturb_A, loss)
    r = _RS / A
    L = ell * (ell + 1)
    q = A ** 2 / (2 * _ETA * _RS) * (1 + _ex(chain_pert))
    g_mu = q * _d(mu) / mu
    bW = 2 / r + g_mu
    cW = rho * (_OM ** 2 / _RS ** 2) / mu - L / r ** 2 - g_mu / r
    return bW, cW


# ===========================================================================
# THE FACTORING AND THE eta-FORM (prereg section 2.6)
#
#   (U, V) = E(eta) * (u, v) ,   E = A * exp( i Om (1/A + kappa A) )
#
# ★ CONSTRUCTED DIRECTLY BY SYMBOLIC CHAIN RULE, NOT BY A HAND-EXPANDED
#   FORMULA.  A first implementation of this function used a hand-expanded
#   expression for the second derivative of a product; it disagreed with the
#   certified axial operator in the C coefficient by 2*eta^2*(i*Om - 2*A)/u^2,
#   and the manufactured-solution check of gate G0 caught it BEFORE any
#   physics number was produced.  The hand expansion is GONE: sympy now
#   differentiates E*f directly, so the only thing that can be wrong is the
#   r-form input, which G0(a) checks against the exact Bessel solution.
#
# Normalization Wn = 4 eta^2 rs^2 / A^2, which reproduces the axial lane's
# leading coefficient A^2 exactly (re-verified by gate G-C(a)).
# ===========================================================================
def _eta_form(b, c, b_x, c_x, hgauge, chain_pert=0.0,
              p_self=1, p_other=1, wn_pow=2):
    """Apply the factoring + normalization; return (Acoef, B, C, Dx, Ex).

    p_self / p_other are the ALGEBRAIC prefactor powers of this block's own
    field and of its partner:  F = A**p_self * exp(i Om (1/A + kappa A)) * f.
    wn_pow is the power of A in the row normalization Wn = 4 eta^2 rs^2/A^wn_pow.

    ★ WHY THESE ARE NOT ALL 1 AND 2 (the toroidal values).  Derived, and it is
    the structural finding of the build phase.  The two channels radiate at
    DIFFERENT speeds, c_S = c_0 sqrt(S) and c_P = sqrt(10/3) c_0 sqrt(S).
    Dividing BOTH fields by the SHEAR outgoing factor leaves the radial
    equation with an unbalanced (k_P^2 - k_S^2) term, so the A -> 0 endpoint is
    an IRREGULAR singular point of that equation and its Wn = 4 eta^2 rs^2/A^2
    coefficient DIVERGES like 1/A^2.  The medium's own answer is that the
    residual bulk-outgoing amplitude vanishes at A = 0 faster than any power
    (the exp(-(1 - sqrt(3/10)) |Im Om| / A) suppression disclosed in prereg
    section 2.6), so the radial field carries one MORE algebraic power of A
    than the tangential one and its row needs no 1/A^2 normalization:
        radial block      p_self = 2, p_other = 1, wn_pow = 0
        tangential block  p_self = 1, p_other = 2, wn_pow = 2
    Both choices are pure row/column scalings of the SAME eigenvalue problem --
    they cannot move a root -- and they are what makes every coefficient finite
    at the compactified infinity instead of infinite there.
    """
    A = 1 - _ETA ** 2
    q = A ** 2 / (2 * _ETA * _RS) * (1 + _ex(chain_pert))
    kap = _ex(hgauge)
    PHI = sp.exp(sp.I * _OM * (1 / A + kap * A))
    E_self, E_other = A ** p_self * PHI, A ** p_other * PHI
    f, h = sp.Function('f')(_ETA), sp.Function('h')(_ETA)

    def ddr(X):
        return q * _d(X)

    F, H = E_self * f, E_other * h
    Wn = 4 * _ETA ** 2 * _RS ** 2 / A ** wn_pow
    expr = sp.expand(Wn * (ddr(ddr(F)) + b * ddr(F) + c * F
                           + b_x * ddr(H) + c_x * H) / E_self)
    slots = (sp.Derivative(f, (_ETA, 2)), sp.Derivative(f, _ETA), f,
             sp.Derivative(h, _ETA), h)
    out = []
    rest = expr
    for s in slots:
        co = rest.coeff(s)
        out.append(sp.expand(co))
        rest = sp.expand(rest - co * s)
    if sp.simplify(rest) != 0:
        raise RuntimeError("eta-form extraction left a residue: the operator "
                           "is not first/second order in the two fields")
    return tuple(out)


# ===========================================================================
# Omega-SPLITTING BY EVALUATION, and the DEGREE CHECK that licenses it
#
# Every eta-form coefficient is a polynomial in Omega of degree <= 2: rho*w^2
# is the only intrinsically-Omega^2 term and the factoring contributes at most
# Omega^2 through (E'/E)^2.  A quadratic is recovered exactly from three
# evaluations,
#     c0 = f(0),  c1 = (f(1) - f(-1))/2,  c2 = (f(1) + f(-1))/2 - f(0),
# which avoids all symbolic manipulation in Omega.  THE ASSUMPTION IS NOT
# TRUSTED: a FOURTH evaluation at Omega = 2 is compared against the recovered
# quadratic, and that residual is gate G0(b)'s degree limb.
# ===========================================================================
_LAMB_CACHE: dict = {}


def _lam(expr):
    key = sp.srepr(expr)
    fn = _LAMB_CACHE.get(key)
    if fn is None:
        fn = sp.lambdify((_ETA, _OM, _RS), expr, modules=["mpmath"])
        _LAMB_CACHE[key] = fn
    return fn


def _om_parts(fn, eta, rs, degree_probe=False):
    """(c0, c1, c2[, degree residual]) at one node, evaluated in mp."""
    f0 = mp.mpc(fn(eta, mp.mpf(0), rs))
    fp = mp.mpc(fn(eta, mp.mpf(1), rs))
    fm = mp.mpc(fn(eta, mp.mpf(-1), rs))
    c0 = f0
    c1 = (fp - fm) / 2
    c2 = (fp + fm) / 2 - f0
    if not degree_probe:
        return c0, c1, c2
    f2 = mp.mpc(fn(eta, mp.mpf(2), rs))
    pred = c0 + 2 * c1 + 4 * c2
    scale = max(abs(f2), abs(pred), mp.mpf(1))
    return c0, c1, c2, abs(f2 - pred) / scale


# ===========================================================================
# THE OPERATOR (prereg section 4.1) -- assembled in mp from the symbolic
# coefficients, evaluated with DPS_COEFF_EXTRA digits of headroom because the
# factoring's Omega^2 cancellation is exact but not manifest (the raw terms
# carry 1/A^2 poles that cancel identically -- verified at freeze against the
# axial lane's published Om^2/(S(1+S)) residual).
# ===========================================================================
_EXPR_CACHE: dict = {}


def _coeff_exprs(kind, branch, rho_mode, ell, hgauge, chain_pert=0.0,
                 decouple=False, perturb_A=0.0, loss=0.0):
    ck = (kind, branch, rho_mode, ell, hgauge, chain_pert, decouple,
          perturb_A, loss)
    if ck in _EXPR_CACHE:
        return _EXPR_CACHE[ck]
    _EXPR_CACHE[ck] = _build_coeff_exprs(
        kind, branch, rho_mode, ell, hgauge, chain_pert, decouple, perturb_A,
        loss)
    return _EXPR_CACHE[ck]


def _build_coeff_exprs(kind, branch, rho_mode, ell, hgauge, chain_pert=0.0,
                       decouple=False, perturb_A=0.0, loss=0.0):
    """Return the eta-form coefficient expressions.

    kind == 'polar'    -> ((A1,B1,C1,D1,E1), (A2,B2,C2,D2,E2))
    kind == 'toroidal' -> ((A,B,C,0,0),)
    """
    if kind == "toroidal":
        bW, cW = _rform_toroidal(rho_mode, ell, chain_pert, perturb_A, loss)
        blocks = (_eta_form(bW, cW, sp.Integer(0), sp.Integer(0), hgauge,
                            chain_pert),)
    else:
        bU, cU, bUV, cUV, bV, cV, bVU, cVU = _rform(
            branch, rho_mode, ell, chain_pert, decouple, perturb_A, loss)
        blocks = (_eta_form(bU, cU, bUV, cUV, hgauge, chain_pert,
                            p_self=2, p_other=1, wn_pow=0),
                  _eta_form(bV, cV, bVU, cVU, hgauge, chain_pert,
                            p_self=1, p_other=2, wn_pow=2))
    return tuple(tuple(_to_eval(e) for e in blk) for blk in blocks)


def _nodes_mp(n, dps):
    eta, D, D2 = cheb_mp(n, dps)
    return eta, D, D2


def _wall_rows(kind, branch, N, nb, D, ell, om_free=True):
    """The frozen wall rows (prereg section 2.5), as (M0row, M1row) pairs.

    Row index 0 of each block is replaced.  Returned rows are dense lists of
    length N == nb*(n+1).

    toroidal / BRANCH-SOFT : dW/deta = 0 (per field) -- an Omega-FREE row.
    BRANCH-STIFF           : block 1 carries the incompressibility
                             (1 + i Omega) u(0) - L v(0) = 0, which IS the
                             Delta(r_sat) = 0 condition and IS the
                             finite-traction condition (prereg 2.5);
                             block 2 keeps dv/deta = 0.
    """
    n1 = N // nb
    L = ell * (ell + 1)
    rows = []
    for blk in range(nb):
        r0 = [mp.mpc(0)] * N
        r1 = [mp.mpc(0)] * N
        if kind == "polar" and branch == "STIFF" and blk == 0:
            r0[0] = mp.mpc(1)                 # (1)*u(0)
            r1[0] = mp.mpc(0, 1)              # (i Omega)*u(0)
            r0[n1] = mp.mpc(-L)               # -L*v(0)
        else:
            for j in range(n1):
                r0[blk * n1 + j] = D[0, j]
        rows.append((r0, r1))
    return rows


def _equil_mp(M0, M1, M2):
    """[xcribe v2.4 coldq_pole_v2p4_root.py::_equil_mp]"""
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


_OPCACHE: dict = {}


def operator_mp(n, kind="polar", branch="SOFT", rho_mode="A", ell=ELL,
                hgauge=HGAUGE_PRIMARY, x_sat=X_SAT, dps=DPS, degree_probe=False,
                omit_hgauge_om2=False, **mut):
    """Assemble the equilibrated quadratic pencil M0 + Om M1 + Om^2 M2 in mp.

    omit_hgauge_om2 is the FT-3 mutation: the hyperboloidal gauge is carried
    into the Omega^0 and Omega^1 parts but OMITTED from the Omega^2 part -- a
    CORRECTLY-SPECIFIED half-applied gauge, which a genuine gauge-independence
    gate must detect."""
    key = (n, kind, branch, rho_mode, ell, hgauge, x_sat, dps, degree_probe,
           omit_hgauge_om2, tuple(sorted(mut.items())))
    if key in _OPCACHE:
        return _OPCACHE[key]
    hi = dps + DPS_COEFF_EXTRA
    blocks = _coeff_exprs(kind, branch, rho_mode, ell, hgauge, **mut)
    blocks0 = (_coeff_exprs(kind, branch, rho_mode, ell, 0.0, **mut)
               if omit_hgauge_om2 else None)
    nb = len(blocks)
    n1 = n + 1
    N = nb * n1
    mp.mp.dps = dps
    eta, D, D2 = _nodes_mp(n, dps)
    M0, M1, M2 = mp.zeros(N, N), mp.zeros(N, N), mp.zeros(N, N)
    worst_deg = mp.mpf(0)
    fns = [[_lam(e) for e in blk] for blk in blocks]
    fns0 = ([[_lam(e) for e in blk] for blk in blocks0]
            if blocks0 is not None else None)
    mp.mp.dps = hi
    rs = mp.mpf(x_sat)
    cache = []
    for bi in range(nb):
        rowvals = [None]        # index 0 is the WALL row: never evaluated,
        for i in range(1, n1):  # and eta = 0 is a pole of the chain factor q
            e = mp.mpf(eta[i])
            vals = []
            for si, fn in enumerate(fns[bi]):
                if degree_probe:
                    c0, c1, c2, dres = _om_parts(fn, e, rs, True)
                    worst_deg = max(worst_deg, dres)
                else:
                    c0, c1, c2 = _om_parts(fn, e, rs)
                if fns0 is not None:
                    c2 = _om_parts(fns0[bi][si], e, rs)[2]
                vals.append((c0, c1, c2))
            rowvals.append(vals)
        cache.append(rowvals)
    mp.mp.dps = dps
    for bi in range(nb):
        other = (bi + 1) % nb if nb > 1 else bi
        for i in range(1, n1):
            (a0, a1, a2), (b0, b1, b2), (c0, c1, c2), \
                (d0, d1, d2), (e0, e1, e2) = cache[bi][i]
            gi = bi * n1 + i
            for j in range(n1):
                M0[gi, bi * n1 + j] = a0 * D2[i, j] + b0 * D[i, j]
                M1[gi, bi * n1 + j] = a1 * D2[i, j] + b1 * D[i, j]
                M2[gi, bi * n1 + j] = a2 * D2[i, j] + b2 * D[i, j]
            M0[gi, gi] += c0
            M1[gi, gi] += c1
            M2[gi, gi] += c2
            if nb > 1:
                for j in range(n1):
                    M0[gi, other * n1 + j] += d0 * D[i, j]
                    M1[gi, other * n1 + j] += d1 * D[i, j]
                    M2[gi, other * n1 + j] += d2 * D[i, j]
                M0[gi, other * n1 + i] += e0
                M1[gi, other * n1 + i] += e1
                M2[gi, other * n1 + i] += e2
    for bi, (r0, r1) in enumerate(_wall_rows(kind, branch, N, nb, D, ell)):
        gi = bi * n1
        for j in range(N):
            M0[gi, j] = r0[j]
            M1[gi, j] = r1[j]
            M2[gi, j] = mp.mpc(0)
    out = _equil_mp(M0, M1, M2)
    _OPCACHE[key] = (out, float(worst_deg))
    return _OPCACHE[key]


def operator_double(n, **kw):
    """Double-precision copy of the SAME operator -- the seeding path only."""
    (M0, M1, M2), _ = operator_mp(n, **kw)
    N = M0.rows
    cast = lambda M: np.array(  # noqa: E731
        [[complex(M[i, j]) for j in range(N)] for i in range(N)], dtype=complex)
    return cast(M0), cast(M1), cast(M2)


# ===========================================================================
# DOUBLE-PRECISION LINEARIZED PENCIL -- the SEEDING path and the G5 object
# [xcribe v2.4 coldq_pole_v2p4_root.py::pencil_spectrum / dedupe]
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


_PENCIL: dict = {}


def pencil_at(n, **kw):
    key = (n, tuple(sorted((k, str(v)) for k, v in kw.items())))
    if key not in _PENCIL:
        _PENCIL[key] = dedupe(list(pencil_spectrum(*operator_double(n, **kw))))
    return _PENCIL[key]


def nearest(vals, target):
    if not len(vals):
        return None
    return min(vals, key=lambda z: abs(z - target))


# ===========================================================================
# EXTENDED-PRECISION DETERMINANT, LU AND POLISH
# [xcribe v2.4 coldq_pole_v2p4_root.py::mp_assemble / mp_det / mp_lu /
#  mp_lu_solve / mp_polish -- transcribed unchanged]
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


def relsep(a, b):
    """Relative separation computed IN MP, cast to float only at the end.
    [xcribe v2.4 coldq_pole_v2p4_root.py::relsep -- the v2.1 R6 lesson]"""
    return float(abs(a - b) / abs(a))


# ===========================================================================
# THE SEED RULE (disclosed; chosen BEFORE any run -- see the header constant
# block).  Makes NO completeness claim and no mode count.
# ===========================================================================
def seed_candidates(kw48, kw80):
    """n-stable, physical-quadrant, in-window double-pencil eigenvalues."""
    def keep(spec):
        return [z for z in spec
                if z.real > 0 and z.imag < 0 and abs(z) <= SEED_ABS_MAX]
    s48, s80 = keep(pencil_at(48, **kw48)), keep(pencil_at(80, **kw80))
    stable = []
    for z in s48:
        w = nearest(s80, z)
        if w is not None and abs(z - w) <= SEED_STABILITY_REL * abs(z):
            stable.append(w)
    stable = dedupe(stable)
    stable.sort(key=lambda z: -(z.real / (2 * abs(z.imag))))
    return stable


_ROOT_CACHE: dict = {}


def root(n, seed, dps=DPS, n_double=None, **kw):
    """Polished root: seed -> nearest double pencil eigenvalue -> mp secant."""
    ck = (n, complex(seed), dps, n_double,
          tuple(sorted((k, str(v)) for k, v in kw.items())))
    if ck in _ROOT_CACHE:
        return _ROOT_CACHE[ck]
    nd = n if n_double is None else n_double
    spec = pencil_at(nd, **kw)
    s = nearest(spec, seed)
    if s is None:
        _ROOT_CACHE[ck] = (None, None, spec)
        return _ROOT_CACHE[ck]
    (P0, P1, P2), _ = operator_mp(n, dps=dps, **kw)
    r = mp_polish(P0, P1, P2, s, dps)
    _ROOT_CACHE[ck] = (r, complex(s), spec)
    return _ROOT_CACHE[ck]


def eigenvector(n, om, dps=DPS, rounds=INVIT_ROUNDS, **kw):
    """mp inverse iteration from the ALL-ONES vector; returns (psi, residual).
    [xcribe v2.4 coldq_pole_v2p4_root.py::eigenfunction]"""
    mp.mp.dps = dps
    (P0, P1, P2), _ = operator_mp(n, dps=dps, **kw)
    A = mp_assemble(P0, P1, P2, om)
    LU, perm = mp_lu(mp.matrix(A))
    N = P0.rows
    v = [mp.mpc(1)] * N
    for _ in range(rounds):
        v = mp_lu_solve(LU, perm, v)
        m = max(abs(z) for z in v)
        v = [z / m for z in v]
    r = [sum(A[i, j] * v[j] for j in range(N)) for i in range(N)]
    resid = max(abs(z) for z in r) / max(abs(z) for z in v)
    return v, resid


def residual_at(n, om, psi, dps=DPS, **kw):
    mp.mp.dps = dps
    (P0, P1, P2), _ = operator_mp(n, dps=dps, **kw)
    A = mp_assemble(P0, P1, P2, om)
    N = P0.rows
    r = [sum(A[i, j] * psi[j] for j in range(N)) for i in range(N)]
    return float(max(abs(z) for z in r) / max(abs(z) for z in psi))


# ===========================================================================
# G0(a) -- THE HOMOGENEOUS-LIMIT BESSEL IDENTITY
#
# In a HOMOGENEOUS medium the exact polar solution is the two-potential pair
#     phi = a*j_l(k_P r) ,  psi = b*j_l(k_S r)
#     U = a k_P j_l'(k_P r) + b L j_l(k_S r)/r
#     V = a j_l(k_P r)/r    + b [ j_l(k_S r)/r + k_S j_l'(k_S r) ]
# with k_P = w/c_P, k_S = w/c_S.  Substituted into the DERIVED r-form system
# of prereg section 2.1 with constant moduli, the residual must vanish.
#
# This is the strongest check in the battery: it is a MANUFACTURED SOLUTION
# for a freshly-derived coupled operator, and any factor error anywhere in
# that derivation fails it.
# ===========================================================================
def gate_G0a(ell=ELL, dps=DPS):
    mp.mp.dps = dps
    L = ell * (ell + 1)

    def residual(lamL, mu, rho, coupling_scale=1):
        cS2, cP2 = mu / rho, (lamL + 2 * mu) / rho
        w = mp.mpf(1) / 3
        kS, kP = w / mp.sqrt(cS2), w / mp.sqrt(cP2)

        def jl(x):
            return mp.sqrt(mp.pi / (2 * x)) * mp.besselj(ell + mp.mpf(1) / 2, x)

        def U(r):
            return (mp.diff(lambda t: jl(kP * t), r)
                    + 2 * L * jl(kS * r) / r)

        def V(r):
            return (jl(kP * r) / r
                    + 2 * (jl(kS * r) / r + mp.diff(lambda t: jl(kS * t), r)))

        cpl = (lamL + mu) * coupling_scale
        worst = mp.mpf(0)
        for r in (mp.mpf(2), mp.mpf('3.7'), mp.mpf(9)):
            Up, Upp = mp.diff(U, r), mp.diff(U, r, 2)
            Vp, Vpp = mp.diff(V, r), mp.diff(V, r, 2)
            u, v = U(r), V(r)
            beta = lamL + 2 * mu
            e1 = (beta * Upp + (2 * beta / r) * Up
                  + (rho * w ** 2 - (2 * beta + L * mu) / r ** 2) * u
                  - (L * cpl / r) * Vp + (L * (lamL + 3 * mu) / r ** 2) * v)
            e2 = (mu * Vpp + (2 * mu / r) * Vp
                  + (rho * w ** 2 - L * beta / r ** 2) * v
                  + (cpl / r) * Up + (2 * beta / r ** 2) * u)
            scale = max(abs(beta * Upp), abs(mu * Vpp), mp.mpf(1))
            worst = max(worst, abs(e1) / scale, abs(e2) / scale)
        return float(worst)

    # the AVE cold operating point: mu = 1, K = 2, lam_L = K - 2mu/3 = 4/3
    lamL, mu, rho = mp.mpf(4) / 3, mp.mpf(1), mp.mpf(1)
    ok = residual(lamL, mu, rho)
    ft = residual(lamL, mu, rho, 1 + mp.mpf(FT_MUT["FT_0a_coupling"]))
    return ({"measured": ok, "tol": TOL["G0a"], "ell": ell,
             "moduli": {"lambda_L": float(lamL), "mu": float(mu),
                        "rho": float(rho),
                        "c_P_over_c_S": float(mp.sqrt((lamL + 2 * mu) / mu))},
             "pass": bool(ok <= TOL["G0a"])},
            {"measured": ft, "threshold": FT_THRESH["FT_0a"],
             "fires": bool(ft >= FT_THRESH["FT_0a"]),
             "mutation": "the (lam_L + mu) coupling coefficient scaled by "
                         f"(1 + {FT_MUT['FT_0a_coupling']})"})


# ===========================================================================
# G-C -- THE REDUCTION GATE (prereg section 5)
#   (a) OPERATOR IDENTITY against v2.4's certified axial operator
#   (b) ROOT reproduction of the certified axial root
#   (c) COUPLING NON-VACUITY
# v2.4's driver is IMPORTED READ-ONLY; it is BYTE-UNTOUCHED.
# ===========================================================================
def _v24():
    import coldq_pole_v2p4_root as v24  # noqa: E402  READ-ONLY comparison
    return v24


def gate_GCa(n=N_PRIMARY, dps=DPS, spin1=False):
    v24 = _v24()
    (A0, A1, A2), _ = operator_mp(n, kind="toroidal", dps=dps)
    B0, B1, B2 = v24.graded_matrices_mp(n, ELL, HGAUGE_PRIMARY, X_SAT, dps,
                                        spin1_wall=spin1)
    mp.mp.dps = dps
    worst = mp.mpf(0)
    for i in range(n + 1):
        for j in range(n + 1):
            for X, Y in ((A0, B0), (A1, B1), (A2, B2)):
                worst = max(worst, abs(X[i, j] - Y[i, j]))
    return float(worst)


def axial_reference():
    """J15 -- read PROGRAMMATICALLY from the merged, certified axial JSON."""
    with open(AXIAL_JSON, encoding="utf-8") as fh:
        j = json.load(fh)
    mp.mp.dps = DPS
    om = mp.mpc(mp.mpf(j["certified_root"]["Omega_re_mp"]),
                mp.mpf(j["certified_root"]["Omega_im_mp"]))
    return {
        "Omega": om,
        "omega_R_M_g": j["adjudication"]["omega_R_M_g"],
        "Q": j["adjudication"]["Q"],
        "source": "research/drivers/coldq_pole_v2p4_root_results.json "
                  "(MERGED on origin/main), keys certified_root.Omega_*_mp "
                  "and adjudication.{omega_R_M_g,Q}",
        "g2b_c": j["gates"]["G2b"]["c"],
        "artifact_c": j["diagnostics"]["artifact_convergence"]["c"],
        "ft2b_c": j["self_tests"]["FT_2b"]["c"],
    }


def gate_GC(ax):
    a = gate_GCa()
    a_mut = gate_GCa(spin1=True)
    om_ax = ax["Omega"]
    r_tor = root(N_PRIMARY, complex(om_ax), kind="toroidal")[0]
    b = relsep(om_ax, r_tor) if r_tor is not None else float("inf")
    gate = {
        "measured_a": a, "tol_a": TOL["GCa"],
        "measured_b": b, "tol_b": TOL["GCb"],
        "n": N_PRIMARY, "dps": DPS,
        "Omega_toroidal_re_mp": mp.nstr(r_tor.real, 40) if r_tor else None,
        "Omega_toroidal_im_mp": mp.nstr(r_tor.imag, 40) if r_tor else None,
        "note": "G-C(a) is an OPERATOR IDENTITY against the certified axial "
                "operator, entry by entry; G-C(b) is the root that operator "
                "returns.  Both gate the SHARED machinery and neither is a "
                "two-instrument agreement on any polar quantity.",
        "pass_a": bool(a <= TOL["GCa"]),
        "pass_b": bool(b <= TOL["GCb"]),
    }
    ft = {"measured_op": a_mut, "threshold_op": FT_THRESH["FT_C_op"],
          "fires": bool(a_mut >= FT_THRESH["FT_C_op"]),
          "mutation": "the toroidal instantiation compared against v2.4's "
                      "SPIN-1 wall row instead of its spin-2 one",
          "frozen_text_defect": "the frozen FT-C text names the spin-1 "
                                "STORED-ENERGY WEIGHTING, which does not "
                                "enter the operator and could not move it; "
                                "the implemented mutation is v2.4's own "
                                "spin-1 WALL row, which does.  DISCLOSED "
                                "PRE-MEASUREMENT as a defect in the frozen "
                                "text, not a post-hoc adjustment, and it is "
                                "a STRENGTHENING: the frozen mutation would "
                                "have been vacuous."}
    gate["pass"] = bool(gate["pass_a"] and gate["pass_b"])
    return gate, ft


# ===========================================================================
# COMPARATORS -- read PROGRAMMATICALLY (nothing below is typed)
# [xcribe v2.4 coldq_pole_v2p4_root.py::_grab / comparators]
# ===========================================================================
def _grab(path, pattern, group=1):
    import re
    with open(path, encoding="utf-8") as fh:
        m = re.search(pattern, fh.read())
    if not m:
        raise RuntimeError(f"comparator pattern not found in {path}: {pattern}")
    return float(m.group(group))


def comparators():
    wr_gr = _grab(RERUN_PY, r"0\.00:\s*\(([0-9.]+),\s*[0-9.]+\)")       # J14
    wi_gr = _grab(RERUN_PY, r"0\.00:\s*\([0-9.]+,\s*([0-9.]+)\)")       # J14
    wr20 = _grab(RINGDOWN_PY, r"\(2,\s*0\):\s*([0-9.]+),")
    wr21 = _grab(RINGDOWN_PY, r"\(2,\s*1\):\s*([0-9.]+),")
    wi20 = _grab(RINGDOWN_PY, r"SCHW_OMEGA_I\s*=\s*\{\(2,\s*0\):\s*([0-9.]+)")
    return {
        "omega_R_GR": wr_gr, "omega_I_GR": wi_gr,
        "Q_GR": wr_gr / (2.0 * wi_gr),
        "nu_vac": float(N_NU),
        "c_P_over_c_shear_cold": math.sqrt(10.0 / 3.0),
        "Omega_GR_n0": [X_SAT * wr20, -X_SAT * wi20],
        "GR_overtone_real_gap": X_SAT * abs(wr20 - wr21),
    }


# ===========================================================================
# THE CONFIGURATION SWEEP (prereg section 4.3)
# ===========================================================================
CONFIGS = (
    ("CFG-SOFT-A", "SOFT", "A", "CO-PRIMARY"),
    ("CFG-STIFF-A", "STIFF", "A", "CO-PRIMARY"),
    ("CFG-SOFT-B", "SOFT", "B", "SENSITIVITY (FORK-3(b), first run)"),
)


def sweep_config(tag, branch, rho_mode, role, ax):
    kw = dict(kind="polar", branch=branch, rho_mode=rho_mode)
    out = {"tag": tag, "branch": branch, "rho_mode": rho_mode, "role": role}
    (M0, M1, M2), deg = operator_mp(N_PRIMARY, degree_probe=True, **kw)
    out["G0b_degree_residual"] = deg
    try:
        cands = seed_candidates(kw, kw)
    except Exception as exc:                                  # noqa: BLE001
        out["seed_error"] = repr(exc)
        cands = []
    out["n_stable_seed_candidates"] = len(cands)
    out["seed_candidates"] = [[z.real, z.imag] for z in cands[:8]]
    out["seed_rule"] = ("double-pencil eigenvalues with Re > 0, Im < 0, "
                        f"|Omega| <= {SEED_ABS_MAX}, n-stable between n = 48 "
                        f"and n = 80 at {SEED_STABILITY_REL} relative, ordered "
                        "by decreasing Re/(2|Im|).  SEED RULE ONLY: it makes "
                        "NO completeness claim and NO mode count.")
    roots = {}
    for name, seed in (("least_damped_n_stable",
                        cands[0] if cands else None),
                       ("axial_seeded", complex(ax["Omega"]))):
        if seed is None:
            roots[name] = None
            continue
        r, s, spec = root(N_PRIMARY, seed, **kw)
        if r is None:
            roots[name] = None
            continue
        inside = [z for z in spec if abs(z - complex(r)) <= R_ISO]
        roots[name] = {
            "seed": [seed.real, seed.imag],
            "Omega": [float(r.real), float(r.imag)],
            "Omega_re_mp": mp.nstr(r.real, 40),
            "Omega_im_mp": mp.nstr(r.imag, 40),
            "within_R_iso_of_seed": bool(abs(complex(r) - seed) <= R_ISO),
            "pencil_count_within_R_iso": len(inside),
            "rel_to_axial": relsep(ax["Omega"], r),
        }
    out["roots"] = roots
    out["BIN_PF_NOROOT"] = bool(not cands)
    return out


def digest_of(obj):
    clean = {k: v for k, v in obj.items()
             if k not in ("_digest", "_runtime_sec")}
    blob = json.dumps(clean, sort_keys=True, separators=(",", ":"),
                      default=str).encode()
    return hashlib.sha256(blob).hexdigest()[:16]


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    t0 = time.time()
    cmp_ = comparators()
    ax = axial_reference()

    G0a, FT0a = gate_G0a()
    G0c, FT0c = gate_G0c()
    GC, FTC = gate_GC(ax)

    configs = [sweep_config(*c, ax) for c in CONFIGS]

    gates = {
        "G0a": G0a,
        "G0c": G0c,
        "G-C": GC,
        "G9": {"note": "determinism is adjudicated EXTERNALLY by running the "
                       "driver twice and diffing the shipped objects; this "
                       "driver deliberately emits NO pass field for G9 "
                       "(prereg section 4.9, executing the successor "
                       "instruction routed by the v2.4 result doc)"},
    }
    self_tests = {"FT_0a": FT0a, "FT_0c": FT0c, "FT_C": FTC}

    # ---- THE FROZEN PRECEDENCE, APPLIED HONESTLY ------------------------
    # prereg section 5: SOLVER-CERTIFIED requires ALL gates of section 5 to
    # PASS and ALL self-tests of section 6 to FIRE.  This driver IMPLEMENTS
    # ONLY the build-phase subset below.  The remaining gates are UNRUN, which
    # is NOT the same as passed, so the certification is SOLVER-NOT-CERTIFIED
    # and NO physics bin is adjudicated at any precedence level.
    implemented = ["G0(a)", "G0(b) degree limb", "G0(c)", "G-C(a)", "G-C(b)"]
    unrun = ["G1", "G2", "G2b", "G3", "G4", "G5", "G-C(c)", "G-P", "G8", "G10",
             "FT-0(b)", "FT-1", "FT-2", "FT-2b", "FT-3", "FT-4", "FT-5",
             "FT-P", "FT-8", "FT-9", "FT-10"]

    out = {
        "_prereg": "research/2026-08-03_coldq-polar-family_prereg-FROZEN.md",
        "_prereg_commit": "d9015e38",
        "_phase": "BUILD PHASE ONLY",
        "_method": "compactified hyperboloidal Chebyshev spectral, TWO-FIELD "
                   "coupled shear-bulk operator; NO winding, NO contour, NO "
                   "region count anywhere",
        "_certification_scope": {
            "implemented_and_measured": implemented,
            "UNRUN_therefore_NOT_PASSED": unrun,
            "consequence": "the frozen precedence of prereg section 7 places "
                           "solver certification FIRST; an UNRUN gate is not "
                           "a passed gate, so this run is SOLVER-NOT-CERTIFIED "
                           "and NO physics bin (BIN-P1, BIN-P2, BIN-P3) is "
                           "adjudicated at any precedence level, including for "
                           "any configuration that located a root",
        },
        "_carry_over": "CARRY-OVER of the v2.4 numerical machinery by "
                       "copy-with-attribution (prereg section P.5); NOT an "
                       "independent reimplementation; no agreement with v2.4 "
                       "on any shared quantity is independent corroboration",
        "_non_claim": "this lane asserts the existence and location of the "
                      "polar roots it CERTIFIES, on the branches it certifies "
                      "them on; it certifies none here, and it asserts NOTHING "
                      "about the absence or presence of other modes in either "
                      "family and NOTHING about which FLAG-W branch the "
                      "substrate is",
        "_flag_W": {
            "SOFT": "K = 2*G_vac*S  -- bulk-impedance-at-saturation-"
                    "boundary.md:31 (c_bulk -> 0, Z_bulk -> 0, Gamma = -1)",
            "STIFF": "K = 2*G_vac/S -- saturating-modulus-and-"
                     "backreaction.md:57 (D = 1/S -> inf, the modulus goes "
                     "rigid, Gamma = +1)",
            "third_voice": "engine-capability-map.md:69 flags conflating the "
                           "stiffening and softening branches as a firewall "
                           "violation",
            "status": "SURFACED, NOT ADJUDICATED.  Both branches run; neither "
                      "leaf repaired by this lane.",
        },
        "_frozen_numerics": {
            "n_primary": N_PRIMARY, "n_ladder": list(N_LADDER),
            "n_ladder_g2": list(N_LADDER_G2), "hgauge_set": list(HGAUGE_SET),
            "dps": DPS, "dps_high": DPS_HIGH,
            "dps_coeff_extra": DPS_COEFF_EXTRA,
            "R_iso": R_ISO, "x_sat": X_SAT, "ell": ELL,
            "dilatation_floor": DILATATION_FLOOR,
            "g2b_resid_floor": G2B_RESID_FLOOR, "g2b_c_floor": G2B_C_FLOOR,
            "seed_abs_max": SEED_ABS_MAX,
            "seed_stability_rel": SEED_STABILITY_REL,
            "runtime_budget_s": RUNTIME_BUDGET_S,
        },
        "axial_reference": {k: (mp.nstr(v.real, 40) + " " + mp.nstr(v.imag, 40)
                                if k == "Omega" else v)
                            for k, v in ax.items()},
        "comparators": cmp_,
        "gates": gates,
        "self_tests": self_tests,
        "configurations": configs,
        "adjudication": {
            "BIN_P1": "N/A -- NOT ADJUDICATED (solver not certified)",
            "BIN_P2": "N/A -- NOT ADJUDICATED (solver not certified)",
            "BIN_P3": "N/A -- NOT ADJUDICATED (solver not certified)",
            "BIN_P4": "N/A BY CONSTRUCTION",
            "precedence_fired": "BIN-PF-SOLVER",
        },
        "certification": "SOLVER-NOT-CERTIFIED",
    }
    out["_digest"] = digest_of(out)
    out["_runtime_sec"] = round(time.time() - t0, 2)

    dest = os.path.join(_HERE, "coldq_polar_family_results.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, sort_keys=True, default=str)
        fh.write("\n")

    print(f"certification   : {out['certification']} (BUILD PHASE ONLY)")
    print(f"G0(a) Bessel    : {G0a['measured']:.6e} vs {TOL['G0a']:.0e} "
          f"-> {'PASS' if G0a['pass'] else 'FAIL'}")
    print(f"G0(c) symbolic  : sep={G0c['separability_residual_exactly_zero']} "
          f"affine={G0c['affine_in_L_residual_exactly_zero']}")
    print(f"G-C(a) operator : {GC['measured_a']:.6e} vs {TOL['GCa']:.0e} "
          f"-> {'PASS' if GC['pass_a'] else 'FAIL'}")
    print(f"G-C(b) root     : {GC['measured_b']:.6e} vs {TOL['GCb']:.0e} "
          f"-> {'PASS' if GC['pass_b'] else 'FAIL'}")
    for c in configs:
        print(f"{c['tag']:14s}: n-stable seeds = "
              f"{c['n_stable_seed_candidates']}  "
              f"BIN-PF-NOROOT = {c['BIN_PF_NOROOT']}")
    print(f"digest          : {out['_digest']}")
    print(f"runtime         : {out['_runtime_sec']} s")
    print(f"wrote           : {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

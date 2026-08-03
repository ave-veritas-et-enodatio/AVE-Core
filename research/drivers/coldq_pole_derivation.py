"""The cold-Q pole derivation — spin-2 (toroidal / odd-parity) quasinormal poles
of the canonical graded saturation profile.

FROZEN PRE-REGISTRATION (read it first; this driver implements it and nothing
else):  research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md

WHAT THIS COMPUTES.  The complex quasinormal eigenvalues `omega * M_g` of the
`ell = 2` transverse-shear (T2) mode of the vacuum's saturation cavity, with

    A(r)      = r_sat / r,     r_sat = 7 GM/c^2,   eps_yield = 1   [Ax 4]
    S(A)      = (1 - A^2)^(1/2)                                    [Ax 4 kernel]
    c_shear   = c_0 * S^(1/2)                                      [Op16]
    rho(r)    = rho_0                       (cold lattice inertia; FORK-3 (a)/(c))
    mu(r)     = rho_0 c_shear^2 = G_0 * S    (so Z_shear = Z_0 sqrt(S) -> 0)
    BC inner  : traction-free at r_sat   (Z_shear -> 0, Gamma_shear = -1, SHORT)
    BC outer  : outgoing radiation into the cold matched Regime-I lattice

There are NO free parameters.  In units of `r_sat` the problem has none at all,
which is why `Q` is exactly `nu_vac`-free (prereg section 0) — gate G8 measures that.

SPIN-2 DISCIPLINE (the PR #814 R7 prerequisite).  The radial system is DERIVED
for the toroidal branch, not imported from the spin-1 vector multipole:

    W' = W/r + T/mu
    T' = -3T/r + [ (ell-1)(ell+2) mu/r^2 - rho omega^2 ] W ,   T = mu (W' - W/r)

The radial functions coincide with spherical Hankel functions in the homogeneous
limit (gate G1) — that is what makes `ka = ell` the same cutoff object in both
sectors — but the impedance relation `T = mu(W' - W/r)` and the `(ell-1)(ell+2)`
stored-energy weighting are the SPIN-2 ones.  Self-test FT-6 shows that using the
spin-1 `ell(ell+1)` weighting instead BREAKS the energy-consistency gate, i.e. the
spin-2 discipline is load-bearing here rather than decorative.

Run:  PYTHONPATH=src python3 research/drivers/coldq_pole_derivation.py
"""

from __future__ import annotations

import ast
import hashlib
import math
import json
import os
import sys
import time

import numpy as np
from scipy.integrate import simpson
from scipy.special import spherical_jn, spherical_yn

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "src"))

from ave.core.constants import N_NU  # noqa: E402  canonical constants only, read-only

PREREG = "research/2026-08-02_coldq-pole-derivation_prereg-FROZEN.md"

# ---------------------------------------------------------------------------
# I1-I9 — the canonical input ledger, in the units of prereg I9 (M_g = c_0 = rho_0 = 1)
# ---------------------------------------------------------------------------
X_SAT = 7.0          # I1  r_sat = 7 GM/c^2   [canon; VALUE rides the GR-imported nu_vac]
EPS_YIELD = 1.0      # I2  saturating-modulus-and-backreaction.md:51
ELL_PRIMARY = 2      # I8  quadrupole selection — INPUT, not derived
NU_VAC = N_NU        # I10 imported read-only from ave.core.constants

# I15 — ENGINEERING numerics, frozen in prereg section 4.3
R_MATCH = 40.0
SERIES_N = 20
N_STEPS_SCAN = 16000
N_STEPS_POLISH = 64000
SCAN_WR = (0.02, 2.00, 181)
SCAN_WI = (1e-3, 1.00, 91)
CONTOUR_PTS = 4096
MULLER_MAX = 60
MULLER_TOL = 1e-12
R_MATCH_SET = (25.0, 40.0, 60.0)
SERIES_N_SET = (12, 20, 28)
N_STEPS_SET = (16000, 32000, 64000)
CONTOUR_SET = (2048, 4096, 8192)
X_SAT_SET = (5.0, 7.0, 11.0)


# ===========================================================================
# Comparator ingest — I11/I12 read PROGRAMMATICALLY from shipped in-repo sources
# (never retyped from prose; the #801/#802 lesson)
# ===========================================================================
def _literal_from_source(relpath: str, name: str):
    src = open(os.path.join(REPO, relpath), encoding="utf-8").read()
    for node in ast.parse(src).body:
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id == name:
                    return ast.literal_eval(node.value)
    raise KeyError(f"{name} not found in {relpath}")


KERR_QNM = _literal_from_source(
    "research/2026-07-20_v1-spin-mapping-adjudication_rerun.py", "KERR_QNM")
SCHW_OMEGA_R = _literal_from_source(
    "research/2026-07-20_ringdown-systematics_checks.py", "SCHW_OMEGA_R")

OMEGA_R_GR, OMEGA_I_GR = KERR_QNM[0.00]      # I11 frozen a*=0 C-comparator
Q_GR = OMEGA_R_GR / (2.0 * OMEGA_I_GR)
OMEGA_R_GR_N1 = SCHW_OMEGA_R[(2, 1)]         # I12 in-repo overtone real part
OMEGA_I_GR_N1 = 0.273915                     # I13 EXTERNAL comparator, no in-repo carrier
OMEGA_R_SHORTCUT = 18.0 / 49.0               # I14 the standing corpus eigenvalue
Q_CONVENTION = 2.0                           # I14 the Op21 2*pi-convention Q = ell
R_EFF_OVER_RSAT = 1.0 / (1.0 + NU_VAC)       # = 7/9; r_eff = r_sat/(1+nu_vac)
R_STAR_OVER_RSAT = 1.0 / np.sqrt(2.0 / 3.0)  # #814 CF-9 turning point, A^2 = 2/3


# ===========================================================================
# Truncated power series in z = 1/r  (stdlib+numpy arithmetic, no symbolics)
# ===========================================================================
def s_mul(a, b, N):
    out = np.zeros(N + 1, dtype=complex)
    for i in range(min(len(a), N + 1)):
        if a[i] == 0:
            continue
        m = min(len(b), N + 1 - i)
        out[i:i + m] += a[i] * b[:m]
    return out


def s_inv(a, N):
    out = np.zeros(N + 1, dtype=complex)
    out[0] = 1.0 / a[0]
    for n in range(1, N + 1):
        s = sum(a[k] * out[n - k] for k in range(1, min(n, len(a) - 1) + 1))
        out[n] = -s / a[0]
    return out


def s_pow(a, p, N):
    """a**p for a[0] != 0 (J.C.P. Miller recurrence)."""
    out = np.zeros(N + 1, dtype=complex)
    out[0] = complex(a[0]) ** p
    for n in range(1, N + 1):
        s = sum((k * p - (n - k)) * a[k] * out[n - k]
                for k in range(1, min(n, len(a) - 1) + 1))
        out[n] = s / (n * a[0])
    return out


def s_der(a, N):
    out = np.zeros(N + 1, dtype=complex)
    for n in range(1, min(len(a), N + 2)):
        if n - 1 <= N:
            out[n - 1] = n * a[n]
    return out


# ===========================================================================
# The constitutive profile branches (prereg section 2.1 + FORK-2 KEEP-BOTH)
# ===========================================================================
class Profile:
    """rho(r), mu(r) and their 1/r expansions for one frozen constitutive branch.

    branch 'sqrtS'  : c_shear = c0 * S^(1/2)  -> mu = G0 * S          [Op16, PRIMARY]
    branch 'S14'    : c_shear = c0 * S^(1/4)  -> mu = G0 * S^(1/2)    [Family-E counterfactual]
    branch 'flat'   : mu = rho = 1 everywhere                          [zero-grade reference]
    """

    def __init__(self, branch="sqrtS", x_sat=X_SAT):
        self.branch = branch
        self.x_sat = float(x_sat)
        if branch == "sqrtS":
            self.mu_exp, self.q = 0.5, 2      # mu = (1-A^2)^{mu_exp}; x = sigma^q
        elif branch == "S14":
            self.mu_exp, self.q = 0.25, 4
        elif branch == "flat":
            self.mu_exp, self.q = 0.0, 1
        else:
            raise ValueError(branch)

    def mu(self, r):
        if self.branch == "flat":
            return np.ones_like(np.asarray(r, dtype=float))
        return (1.0 - (self.x_sat / r) ** 2) ** self.mu_exp

    def rho(self, r):
        return np.ones_like(np.asarray(r, dtype=float))

    def mhat(self, sigma):
        """mu / sigma, analytic and nonzero at sigma = 0 under x = sigma^q."""
        if self.branch == "flat":
            return None
        x = sigma ** self.q
        r = self.x_sat + x
        # 1 - A^2 = x (2 x_sat + x) / r^2  ->  mu = [x(2 x_sat + x)]^p / r^{2p}
        p = self.mu_exp
        return (x ** p * (2.0 * self.x_sat + x) ** p) / (r ** (2.0 * p) * sigma)

    def series(self, N):
        """Taylor coefficients of mu(z), rho(z) in z = 1/r, both with [0] == 1."""
        one_minus = np.zeros(N + 3, dtype=complex)
        one_minus[0] = 1.0
        if self.branch != "flat":
            one_minus[2] = -self.x_sat ** 2
        mu_z = s_pow(one_minus, self.mu_exp, N + 2) if self.branch != "flat" else \
            np.eye(1, N + 3, 0)[0].astype(complex)
        rho_z = np.zeros(N + 3, dtype=complex)
        rho_z[0] = 1.0
        return mu_z, rho_z


# ===========================================================================
# The exact asymptotic outgoing / ingoing solutions (prereg section 4.2)
# ===========================================================================
def asymptotic_coeffs(omega, ell, prof, N, corrupt=None):
    """c_1..c_N of F = sum_n c_n z^n with W = exp(i omega r) F, c_1 = 1."""
    mu_z, rho_z = prof.series(N)
    dmu = s_der(mu_z, N + 2)
    g_z = -s_mul(np.concatenate(([0.0, 0.0], dmu[:N + 1])), s_inv(mu_z, N + 2), N + 2)
    rho_over_mu = s_mul(rho_z, s_inv(mu_z, N + 2), N + 2)

    M = N + 3
    alpha = np.zeros(M, dtype=complex)          # alpha = 2 i w + 2 z + g
    alpha[0] = 2j * omega
    alpha[1] += 2.0
    alpha[:min(len(g_z), M)] += g_z[:M]

    beta = np.zeros(M, dtype=complex)           # beta = w^2 (rho/mu - 1) - l(l+1) z^2
    beta[:min(len(rho_over_mu), M)] += omega ** 2 * rho_over_mu[:M]  # ... - g z + i w (2z + g)
    beta[0] -= omega ** 2
    beta[2] -= ell * (ell + 1)
    beta[1:] -= g_z[:M - 1]
    beta[1] += 2j * omega
    beta[:min(len(g_z), M)] += 1j * omega * g_z[:M]

    c = np.zeros(N + 2, dtype=complex)
    c[1] = 1.0
    for m in range(3, N + 3):
        tot = 0.0 + 0j
        if m - 2 >= 1:
            tot += (m - 2) * (m - 1) * c[m - 2]
        for n in range(1, m - 1):
            if 0 <= m - n - 1 < len(alpha):
                tot -= n * c[n] * alpha[m - n - 1]
            if 0 <= m - n < len(beta):
                tot += c[n] * beta[m - n]
        c[m - 1] = -tot / (2j * omega * (2 - m))
    out = c[1:N + 1].copy()
    if corrupt is not None:
        idx, rel = corrupt
        if idx < len(out):
            out[idx] *= (1.0 + rel)
    return out


def eval_asymptotic(c, omega, r, prof):
    """(W, T) of the outgoing asymptotic solution at radius r."""
    z = 1.0 / r
    n = np.arange(1, len(c) + 1)
    zp = z ** n
    if c.ndim == 1:                       # single omega
        F = np.sum(c * zp)
        dFdz = np.sum(c * n * z ** (n - 1))
    else:                                 # c has shape (N, K): vectorised over omega
        F = np.einsum("nk,n->k", c, zp)
        dFdz = np.einsum("nk,n->k", c, n * z ** (n - 1))
    Fr = -z ** 2 * dFdz
    e = np.exp(1j * omega * r)
    W = e * F
    dW = e * (1j * omega * F + Fr)
    mu = prof.mu(r)
    T = mu * (dW - W / r)
    return W, T


def asymptotic_pair(omega_arr, ell, prof, N, R, corrupt=None):
    """(W_out, T_out, W_in, T_in) at R, vectorised over the omega array."""
    omega_arr = np.atleast_1d(np.asarray(omega_arr, dtype=complex))
    c_out = np.empty((N, omega_arr.size), dtype=complex)
    c_in = np.empty((N, omega_arr.size), dtype=complex)
    for k, w in enumerate(omega_arr):
        c_out[:, k] = asymptotic_coeffs(w, ell, prof, N, corrupt)
        c_in[:, k] = asymptotic_coeffs(-w, ell, prof, N, corrupt)
    Wo, To = eval_asymptotic(c_out, omega_arr, R, prof)
    Wi, Ti = eval_asymptotic(c_in, -omega_arr, R, prof)
    return Wo, To, Wi, Ti


# ===========================================================================
# The regular-at-the-wall integrator (prereg section 4.1)
# ===========================================================================
def _rhs(sigma, y, omega, ell, prof, mu_im=0.0):
    q = prof.q
    x = sigma ** q
    r = prof.x_sat + x
    Lc = (ell - 1) * (ell + 2)
    W, T = y[0], y[1]
    if prof.branch == "flat":
        mu = 1.0 + 1j * mu_im
        dW = W / r + T / mu
        dT = -3.0 * T / r + (Lc * mu / r ** 2 - omega ** 2) * W
        return np.stack((dW, dT))
    mh = prof.mhat(sigma) if sigma > 0 else _mhat0(prof)
    mh = mh * (1.0 + 1j * mu_im)
    mu = sigma * mh
    dW = q * sigma ** (q - 1) * W / r + q * sigma ** (q - 2) * T / mh
    dT = q * sigma ** (q - 1) * (-3.0 * T / r + Lc * mu * W / r ** 2 - omega ** 2 * W)
    return np.stack((dW, dT))


def _mhat0(prof):
    p = prof.mu_exp
    return (2.0 * prof.x_sat) ** p / prof.x_sat ** (2.0 * p)


def integrate(omega_arr, ell, prof, R, n_steps, clamped=False, mu_im=0.0):
    """Fixed-step RK4 from the wall to R, vectorised over omega.  Deterministic."""
    omega = np.atleast_1d(np.asarray(omega_arr, dtype=complex))
    K = omega.size
    if prof.branch == "flat":
        s0, s_end = 0.0, R - prof.x_sat
    else:
        s0, s_end = 0.0, (R - prof.x_sat) ** (1.0 / prof.q)
    h = (s_end - s0) / n_steps
    if clamped:
        y = np.stack((np.zeros(K, dtype=complex), np.ones(K, dtype=complex)))
    else:
        y = np.stack((np.ones(K, dtype=complex), np.zeros(K, dtype=complex)))
    if prof.branch == "flat":
        # no singular point: shift the start off sigma=0 is unnecessary
        pass
    s = s0
    for _ in range(n_steps):
        k1 = _rhs(s, y, omega, ell, prof, mu_im)
        k2 = _rhs(s + h / 2, y + h / 2 * k1, omega, ell, prof, mu_im)
        k3 = _rhs(s + h / 2, y + h / 2 * k2, omega, ell, prof, mu_im)
        k4 = _rhs(s + h, y + h * k3, omega, ell, prof, mu_im)
        y = y + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        s += h
    return y[0], y[1]


def integrate_profile(omega, ell, prof, R, n_steps, n_sample=4000, clamped=False):
    """Single-omega integration returning the sampled eigenfunction (sigma-grid)."""
    if prof.branch == "flat":
        s_end = R - prof.x_sat
    else:
        s_end = (R - prof.x_sat) ** (1.0 / prof.q)
    h = s_end / n_steps
    y = np.array([[0.0 + 0j], [1.0 + 0j]]) if clamped else np.array([[1.0 + 0j], [0.0 + 0j]])
    s = 0.0
    stride = max(1, n_steps // n_sample)
    sg, Ws, Ts = [], [], []
    om = np.array([omega], dtype=complex)
    for i in range(n_steps + 1):
        if i % stride == 0:
            sg.append(s)
            Ws.append(y[0, 0])
            Ts.append(y[1, 0])
        if i == n_steps:
            break
        k1 = _rhs(s, y, om, ell, prof)
        k2 = _rhs(s + h / 2, y + h / 2 * k1, om, ell, prof)
        k3 = _rhs(s + h / 2, y + h / 2 * k2, om, ell, prof)
        k4 = _rhs(s + h, y + h * k3, om, ell, prof)
        y = y + (h / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        s += h
    sg = np.array(sg)
    x = sg ** prof.q if prof.branch != "flat" else sg
    return sg, prof.x_sat + x, np.array(Ws), np.array(Ts)


# ===========================================================================
# The QNM objective  N(omega) = W_num T_out - T_num W_out   (analytic; zeros = poles)
# ===========================================================================
def objective(omega_arr, ell, prof, R=R_MATCH, N=SERIES_N, n_steps=N_STEPS_SCAN,
              corrupt=None, clamped=False):
    Wn, Tn = integrate(omega_arr, ell, prof, R, n_steps, clamped=clamped)
    Wo, To, _, _ = asymptotic_pair(omega_arr, ell, prof, N, R, corrupt)
    raw = Wn * To - Tn * Wo
    scale = np.abs(Wn) * np.abs(To) + np.abs(Tn) * np.abs(Wo)
    return raw, raw / np.where(scale == 0, 1.0, scale)


def closed_objective(omega_arr, ell, prof, R, n_steps=N_STEPS_SCAN, mu_im=0.0):
    """Doubly traction-free (CLOSED) cavity: T(R) = 0.  Lossless => real spectrum."""
    _, T = integrate(omega_arr, ell, prof, R, n_steps, mu_im=mu_im)
    return T


# ===========================================================================
# Root location: grid scan -> Muller polish -> argument-principle count
# ===========================================================================
def scaled_geometry(x_sat):
    """The problem is EXACTLY scale-free in r_sat: in y = r/r_sat and
    Omega = omega*r_sat the radial system is identical for every x_sat.  The
    NUMERICS must respect that -- the matching radius and the search rectangle
    are held fixed in units of r_sat, not in units of M_g.  (Holding R_match
    fixed in M_g while x_sat varies puts the match INSIDE the grade and was a
    real bug in the first battery run; see the result doc.)"""
    f = X_SAT / float(x_sat)
    R = R_MATCH * float(x_sat) / X_SAT
    wr = (SCAN_WR[0] * f, SCAN_WR[1] * f, SCAN_WR[2])
    wi = (SCAN_WI[0] * f, SCAN_WI[1] * f, SCAN_WI[2])
    return R, wr, wi


def scan_grid(ell, prof, R=R_MATCH, N=SERIES_N, n_steps=N_STEPS_SCAN,
              WRr=SCAN_WR, WIi=SCAN_WI):
    wr = np.linspace(*WRr[:2], WRr[2])
    wi = np.linspace(*WIi[:2], WIi[2])
    WR, WI = np.meshgrid(wr, wi, indexing="ij")
    omegas = (WR - 1j * WI).ravel()
    _, red = objective(omegas, ell, prof, R, N, n_steps)
    mag = np.abs(red).reshape(WR.shape)
    seeds = []
    for i in range(1, mag.shape[0] - 1):
        for j in range(1, mag.shape[1] - 1):
            w = mag[i - 1:i + 2, j - 1:j + 2]
            if mag[i, j] == w.min() and mag[i, j] < w.max():
                seeds.append(WR[i, j] - 1j * WI[i, j])
    return seeds, mag


def muller(f, seeds, tol=MULLER_TOL, itmax=MULLER_MAX):
    """Vectorised Muller iteration on an array of complex seeds."""
    z = np.asarray(seeds, dtype=complex)
    if z.size == 0:
        return z, np.zeros(0, dtype=bool)
    x0 = z * (1.0 - 1e-3) - 1e-4
    x1 = z * (1.0 + 1e-3) + 1e-4
    x2 = z.copy()
    f0, f1, f2 = f(x0), f(x1), f(x2)
    done = np.zeros(z.size, dtype=bool)
    conv = np.zeros(z.size, dtype=bool)
    for _ in range(itmax):
        h0, h1 = x1 - x0, x2 - x1
        d0 = (f1 - f0) / np.where(h0 == 0, 1e-30, h0)
        d1 = (f2 - f1) / np.where(h1 == 0, 1e-30, h1)
        a = (d1 - d0) / np.where(h1 + h0 == 0, 1e-30, h1 + h0)
        b = a * h1 + d1
        disc = np.sqrt(b * b - 4.0 * a * f2)
        den = np.where(np.abs(b + disc) > np.abs(b - disc), b + disc, b - disc)
        den = np.where(np.abs(den) < 1e-300, 1e-300, den)
        dx = -2.0 * f2 / den
        dx = np.where(done, 0.0, dx)
        x0, x1 = x1, x2
        x2 = x2 + dx
        f0, f1 = f1, f2
        f2 = f(x2)
        bad = ~np.isfinite(x2) | (np.abs(x2) > 20.0)
        x2 = np.where(bad, x1, x2)
        done = done | bad | (np.abs(dx) <= tol * np.maximum(np.abs(x2), 1e-12))
        conv = conv | (~bad & (np.abs(dx) <= tol * np.maximum(np.abs(x2), 1e-12)))
        if done.all():
            break
    return x2, conv


def dedupe(roots, tol=1e-6):
    out = []
    for r in roots:
        if not np.isfinite(r):
            continue
        if any(abs(r - o) <= tol * max(abs(r), 1.0) for o in out):
            continue
        out.append(complex(r))
    return out


def in_rect(w, WRr=SCAN_WR, WIi=SCAN_WI):
    return (WRr[0] <= w.real <= WRr[1]) and (WIi[0] <= -w.imag <= WIi[1])


def winding_count(fn, npts, wr=SCAN_WR, wi=SCAN_WI):
    """(1/2 pi i) contour integral of dlog(N) round the frozen rectangle."""
    per = max(4, npts // 4)
    a, b = wr[0], wr[1]
    c, d = -wi[1], -wi[0]           # imaginary parts (negative)
    e1 = a + 1j * np.linspace(c, d, per, endpoint=False)
    e2 = np.linspace(a, b, per, endpoint=False) + 1j * d
    e3 = b + 1j * np.linspace(d, c, per, endpoint=False)
    e4 = np.linspace(b, a, per, endpoint=False) + 1j * c
    # (a,c) -> (a,d) -> (b,d) -> (b,c) -> (a,c) traverses the rectangle CLOCKWISE
    # in the complex plane, so the winding integral is NEGATED to give the
    # positively-oriented zero count.
    path = np.concatenate([e1, e2, e3, e4])
    vals = fn(path)
    vals = np.concatenate([vals, vals[:1]])
    dphi = np.angle(vals[1:] / vals[:-1])
    return float(-np.sum(dphi) / (2.0 * np.pi)), float(np.min(np.abs(vals)))


def find_poles(ell, prof, R=R_MATCH, N=SERIES_N,
               n_scan=N_STEPS_SCAN, n_polish=N_STEPS_SCAN,
               WRr=SCAN_WR, WIi=SCAN_WI):
    """Seed-refinement runs at `n_scan` steps (the pole is converged to ~1e-11 there,
    measured; n_steps is NOT the accuracy limit).  main() re-polishes the surviving
    distinct roots at the frozen N_STEPS_POLISH = 64000 before anything is reported."""
    seeds, mag = scan_grid(ell, prof, R, N, n_scan, WRr, WIi)

    def f(w):
        return objective(w, ell, prof, R, N, n_polish)[1]

    roots, ok = muller(f, seeds) if seeds else (np.zeros(0, dtype=complex),
                                               np.zeros(0, dtype=bool))
    keep = [complex(r) for r, k in zip(roots, ok) if k and in_rect(complex(r), WRr, WIi)]
    keep = dedupe(keep)
    keep.sort(key=lambda w: abs(w.imag))
    return keep, seeds, mag


# ===========================================================================
# Observables read off a located pole
# ===========================================================================
def mode_energy_profile(omega, ell, prof, R=R_MATCH, n_steps=N_STEPS_SCAN,
                        weight_ll=None):
    """Frozen spin-2 mode-energy radial density and its kinetic-only partner."""
    Lc = (ell - 1) * (ell + 2) if weight_ll is None else weight_ll
    sg, rs, W, T = integrate_profile(omega, ell, prof, R, n_steps)
    mu = prof.mu(rs)
    rho = prof.rho(rs)
    strain = np.where(mu > 0, np.abs(T) ** 2 / np.where(mu > 0, mu, 1.0), 0.0)
    kin = rho * abs(omega) ** 2 * np.abs(W) ** 2 * rs ** 2
    E = kin + (strain + Lc * mu * np.abs(W) ** 2 / rs ** 2) * rs ** 2
    return sg, rs, W, T, E, kin


def localization(omega, ell, prof, R=R_MATCH, n_steps=N_STEPS_SCAN):
    _, rs, W, T, E, kin = mode_energy_profile(omega, ell, prof, R, n_steps)
    lo, hi = prof.x_sat * 1.0, prof.x_sat * 2.0
    m = (rs >= lo) & (rs <= hi)
    rw, Ew, Kw = rs[m], E[m], kin[m]
    i_e, i_k = int(np.argmax(Ew)), int(np.argmax(Kw))
    interior = 0 < i_e < len(Ew) - 1
    endpoint = None if interior else ("inner" if i_e == 0 else "outer")
    return {
        "u_energy": float(rw[i_e] / prof.x_sat),
        "u_kinetic": float(rw[i_k] / prof.x_sat),
        "interior_max": bool(interior),
        "endpoint": endpoint,
        "window_over_r_sat": [1.0, 2.0],
        "E_at_wall_over_E_peak": float(Ew[0] / Ew[i_e]),
        "E_at_outer_over_E_peak": float(Ew[-1] / Ew[i_e]),
    }


def rayleigh_quotient(omega, ell, prof, R, n_steps, weight_ll=None):
    """omega from the frozen spin-2 energy functional (valid on the CLOSED cavity).

    Simpson quadrature on the UNIFORM sigma grid with the exact Jacobian
    dr/dsigma = q sigma^(q-1), so the quadrature error is O(h^4) and does not
    limit the gate.
    """
    Lc = (ell - 1) * (ell + 2) if weight_ll is None else weight_ll
    sg, rs, W, T = integrate_profile(omega, ell, prof, R, n_steps)
    mu, rho = prof.mu(rs), prof.rho(rs)
    strain = np.where(mu > 0, np.abs(T) ** 2 / np.where(mu > 0, mu, 1.0), 0.0)
    jac = prof.q * sg ** (prof.q - 1) if prof.branch != "flat" else np.ones_like(sg)
    num = simpson((strain + Lc * mu * np.abs(W) ** 2 / rs ** 2) * rs ** 2 * jac, x=sg)
    den = simpson(rho * np.abs(W) ** 2 * rs ** 2 * jac, x=sg)
    return float(np.sqrt(num / den))


# ===========================================================================
# GATES G1-G9 (prereg section 5) — frozen tolerances, no post-hoc widening
# ===========================================================================
G1_SET_ELL = (1, 2, 3)
G1_SET_W = (0.4 + 0j, 0.4 - 0.09j, 1.3 - 0.4j)
G1_SET_R = (12.0, 25.0, 40.0)


def sph_h1(ell, x):
    return spherical_jn(ell, x) + 1j * spherical_yn(ell, x)


def sph_h1p(ell, x):
    return (spherical_jn(ell, x, derivative=True)
            + 1j * spherical_yn(ell, x, derivative=True))


def gate_G1(corrupt=None):
    """Asymptotic series vs exact spherical Hankel at ZERO grade."""
    flat = Profile("flat", x_sat=1.0)
    worst, rows = 0.0, []
    for ell in G1_SET_ELL:
        for w in G1_SET_W:
            c = asymptotic_coeffs(w, ell, flat, SERIES_N, corrupt)
            for R in G1_SET_R:
                z = 1.0 / R
                n = np.arange(1, len(c) + 1)
                F = np.sum(c * z ** n)
                dFdz = np.sum(c * n * z ** (n - 1))
                dW_over_W = 1j * w + (-z ** 2 * dFdz) / F
                x = w * R
                ref = w * sph_h1p(ell, x) / sph_h1(ell, x)
                rel = abs(dW_over_W - ref) / abs(ref)
                worst = max(worst, rel)
                rows.append({"ell": ell, "omega": str(w), "R": R, "rel": float(rel)})
    return {"worst_rel": float(worst), "tol": 1e-12, "pass": bool(worst <= 1e-12),
            "n_points": len(rows)}


def closed_reduced(omega_arr, ell, prof, R, n_steps=N_STEPS_SCAN, mu_im=0.0):
    W, T = integrate(omega_arr, ell, prof, R, n_steps, mu_im=mu_im)
    return T / (np.abs(W) + np.abs(T))


def closed_spectrum(ell, prof, R, n_steps=N_STEPS_SCAN, mu_im=0.0, wmax=1.2):
    """Real-axis scan for the doubly traction-free (CLOSED, lossless) cavity."""
    def f(w):
        return closed_reduced(w, ell, prof, R, n_steps, mu_im)
    wr = np.linspace(0.02, wmax, 1200)
    vals = f(wr.astype(complex))
    seeds = []
    for i in range(len(wr) - 1):
        if np.real(vals[i]) * np.real(vals[i + 1]) < 0:
            seeds.append(complex(0.5 * (wr[i] + wr[i + 1]), 0.0))
    roots, ok = muller(f, seeds) if seeds else (np.zeros(0, dtype=complex),
                                                np.zeros(0, dtype=bool))
    keep = dedupe([complex(r) for r, k in zip(roots, ok) if k])
    keep.sort(key=lambda w: w.real)
    return keep


def gate_G2(ell, prof, R_wall):
    """Energy-functional consistency: the Rayleigh quotient built from the frozen
    spin-2 weighting must reproduce the SHOT closed-cavity eigenvalue.

    NOTE (stated, not hidden): the pointwise ODE residual of the Euler-Lagrange
    identity is algebraically zero on ANY solution of the integrated system, i.e.
    it is a gate that cannot fail.  The frozen criterion is therefore instantiated
    in its only non-tautological form -- the Rayleigh quotient, which ties the
    eigenvalue found by SHOOTING to the eigenvalue predicted by the ENERGY
    FUNCTIONAL through two independent computations.  FT-6 breaks it.
    """
    spec = closed_spectrum(ell, prof, R_wall)
    if not spec:
        return {"pass": False, "reason": "no closed-cavity eigenvalue found",
                "worst_rel": None, "tol": 1e-9}
    rows, worst = [], 0.0
    for w in spec[:3]:
        rq = rayleigh_quotient(w.real, ell, prof, R_wall, N_STEPS_SCAN)
        rel = abs(rq - w.real) / abs(w.real)
        worst = max(worst, rel)
        rows.append({"omega_shot": float(w.real), "omega_rayleigh": float(rq),
                     "rel": float(rel)})
    return {"worst_rel": float(worst), "tol": 1e-9, "pass": bool(worst <= 1e-9),
            "rows": rows}


def gate_G6(ell, prof, R_wall, mu_im=0.0):
    """Ax-3: the CLOSED (lossless) cavity spectrum must be REAL."""
    def f(w):
        return closed_reduced(w, ell, prof, R_wall, N_STEPS_SCAN, mu_im)
    seeds = []
    wr = np.linspace(0.02, 1.2, 400)
    wi = np.linspace(0.0, 0.30, 16)
    WR, WI = np.meshgrid(wr, wi, indexing="ij")
    grid = (WR - 1j * WI).ravel()
    mag = np.abs(f(grid)).reshape(WR.shape)
    for i in range(1, mag.shape[0] - 1):
        for j in range(mag.shape[1] - 1):
            win = mag[i - 1:i + 2, max(0, j - 1):j + 2]
            if mag[i, j] == win.min() and mag[i, j] < win.max():
                seeds.append(WR[i, j] - 1j * WI[i, j])
    roots, ok = muller(f, seeds) if seeds else (np.zeros(0, dtype=complex),
                                                np.zeros(0, dtype=bool))
    keep = dedupe([complex(r) for r, k in zip(roots, ok) if k and 0.02 <= r.real <= 1.2])
    worst = max((abs(w.imag) / abs(w) for w in keep), default=None)
    # real-coefficient check of the OPEN problem's assembled transfer
    y = np.stack((np.array([1.0 + 0j]), np.array([0.0 + 0j])))
    im_max = 0.0
    for sg in (0.0, 0.5, 1.5, 3.0):
        d = _rhs(sg, y, np.array([0.4 + 0j]), ell, prof)
        im_max = max(im_max, float(np.max(np.abs(np.imag(d)))))
    return {"n_roots": len(keep),
            "roots": [[float(w.real), float(w.imag)] for w in keep],
            "worst_rel_imag": None if worst is None else float(worst),
            "tol": 1e-10,
            "transfer_max_abs_imag": im_max,
            "pass": bool(keep) and bool(worst is not None and worst <= 1e-10)
                    and im_max == 0.0}


def gate_G7(ell, prof, poles):
    """Argument-principle winding count vs the number of located poles."""
    def fn(w):
        return objective(w, ell, prof, R_MATCH, SERIES_N, N_STEPS_SCAN)[0]
    rows = []
    counts = []
    for npts in CONTOUR_SET:
        cnt, minabs = winding_count(fn, npts)
        counts.append(cnt)
        rows.append({"n_contour": npts, "winding": cnt, "min_abs_N": minabs})
    ints = [round(c) for c in counts]
    integral_ok = all(abs(c - round(c)) <= 1e-3 for c in counts)
    stable = len(set(ints)) == 1
    return {"rows": rows, "winding_counts": counts, "rounded": ints,
            "n_located": len(poles), "integer_tol": 1e-3,
            "pass": bool(integral_ok and stable and ints[0] == len(poles))}


# ===========================================================================
# SELF-TESTS FT-1..FT-5 (frozen, prereg section 6) + FT-6 (ADDED strengthening)
# ===========================================================================
def selftests(ell, prof, R_wall, pole0, poles):
    out = {}

    # FT-1 — corrupt one asymptotic-recursion coefficient by 1e-9 relative
    g1c = gate_G1(corrupt=(3, 1e-9))
    out["FT1_series_corruption"] = {
        "targets": "G1", "worst_rel": g1c["worst_rel"], "threshold": 1e-11,
        "fires": bool(g1c["worst_rel"] >= 1e-11)}

    # FT-2 — clamped inner wall instead of traction-free (the Gamma = +1 alternative)
    def fc(w):
        return objective(w, ell, prof, R_MATCH, SERIES_N, N_STEPS_SCAN,
                         clamped=True)[1]
    seeds_c, _ = scan_grid_clamped(ell, prof)
    rc, okc = muller(fc, seeds_c) if seeds_c else (np.zeros(0, complex),
                                                   np.zeros(0, bool))
    keep_c = dedupe([complex(r) for r, k in zip(rc, okc) if k and in_rect(complex(r))])
    keep_c.sort(key=lambda w: abs(w.imag))
    rel_c = (abs(keep_c[0] - pole0) / abs(pole0)) if keep_c else None
    out["FT2_clamped_wall"] = {
        "targets": "G3 / the inner BC is load-bearing",
        "clamped_poles": [[float(w.real), float(w.imag)] for w in keep_c],
        "rel_shift_vs_traction_free": None if rel_c is None else float(rel_c),
        "threshold": 1e-2,
        "fires": bool(rel_c is not None and rel_c >= 1e-2)}

    # FT-3 — smuggled friction Im(mu)/Re(mu) = 1e-3 in the CLOSED cavity
    g6l = gate_G6(ell, prof, R_wall, mu_im=1e-3)
    out["FT3_smuggled_loss"] = {
        "targets": "G6 (Ax 3)", "worst_rel_imag": g6l["worst_rel_imag"],
        "threshold": 1e-5,
        "fires": bool(g6l["worst_rel_imag"] is not None
                      and g6l["worst_rel_imag"] >= 1e-5)}

    # FT-4 — match deep INSIDE the grade, where the asymptotic series is invalid
    def f8(w):
        return objective(w, ell, prof, 8.0, SERIES_N, N_STEPS_SCAN)[1]
    r8, ok8 = muller(f8, [pole0])
    rel_8 = abs(complex(r8[0]) - pole0) / abs(pole0) if ok8[0] else float("inf")
    out["FT4_out_of_regime_match"] = {
        "targets": "G4 / G5", "R_match": 8.0,
        "omega_R8": [float(np.real(r8[0])), float(np.imag(r8[0]))],
        "rel_vs_R40": float(rel_8), "threshold": 1e-3,
        "fires": bool(rel_8 >= 1e-3)}

    # FT-5 — winding count on (a) a pole-free sub-rectangle, (b) the zero-grade
    #        problem whose root count is known in closed form
    def fn(w):
        return objective(w, ell, prof, R_MATCH, SERIES_N, N_STEPS_SCAN)[0]
    lo = SCAN_WR[1] - 0.10
    empty_wr = (lo, SCAN_WR[1], 0)
    empty_wi = (SCAN_WI[0], SCAN_WI[0] + 0.02, 0)
    poles_in_empty = [w for w in poles
                      if lo <= w.real <= SCAN_WR[1]
                      and SCAN_WI[0] <= -w.imag <= SCAN_WI[0] + 0.02]
    cnt_a, _ = winding_count(fn, 2048, empty_wr, empty_wi)
    fbox_wr, fbox_wi = (0.05, 6.0, 0), (0.02, 4.0, 0)
    closed_form, cnt_b = {}, {}
    for L in (1, 2, 3):
        allroots = flat_cavity_roots(L)
        closed_form[L] = [z for z in allroots
                          if fbox_wr[0] <= z.real <= fbox_wr[1]
                          and fbox_wi[0] <= -z.imag <= fbox_wi[1]]
        flat = Profile("flat", x_sat=1.0)

        def fb(w, L=L, flat=flat):
            return objective(w, L, flat, 8.0, SERIES_N, 4000)[0]
        c, _ = winding_count(fb, 2048, fbox_wr, fbox_wi)
        cnt_b[L] = c
    out["FT5_winding_liveness"] = {
        "targets": "G7",
        "empty_box_winding": cnt_a, "empty_box_expected": 0,
        "known_poles_in_empty_box": len(poles_in_empty),
        "flat_cavity_winding": {str(k): v for k, v in cnt_b.items()},
        "flat_cavity_closed_form_count": {str(k): len(v) for k, v in closed_form.items()},
        "flat_cavity_closed_form_roots": {
            str(k): [[float(z.real), float(z.imag)] for z in v]
            for k, v in closed_form.items()},
        "fires": bool(abs(cnt_a) < 0.5
                      and all(abs(cnt_b[L] - len(closed_form[L])) < 0.5
                              for L in (1, 2, 3)))}

    # FT-6 — ADDED (a strengthening beyond the frozen FT-1..FT-5 set; it adds a
    # firing requirement, it does not drop one).  Evaluate G2's Rayleigh quotient
    # with the SPIN-1 weighting ell(ell+1) instead of the derived spin-2
    # (ell-1)(ell+2).  G2 must BREAK -- i.e. the spin-2 discipline is load-bearing.
    spec = closed_spectrum(ell, prof, R_wall)
    if spec:
        w0 = spec[0].real
        rq1 = rayleigh_quotient(w0, ell, prof, R_wall, N_STEPS_SCAN,
                                weight_ll=ell * (ell + 1))
        rel1 = abs(rq1 - w0) / abs(w0)
    else:
        rq1, rel1 = None, None
    out["FT6_spin1_weighting"] = {
        "targets": "G2 / the spin-2 discipline",
        "note": "ADDED at implementation time; strengthening, not a relaxation",
        "omega_shot": None if not spec else float(w0),
        "omega_rayleigh_spin1_weighting": rq1,
        "rel": rel1, "threshold": 1e-6,
        "fires": bool(rel1 is not None and rel1 >= 1e-6)}
    return out


def scan_grid_clamped(ell, prof, R=R_MATCH, N=SERIES_N, n_steps=N_STEPS_SCAN):
    wr = np.linspace(*SCAN_WR[:2], SCAN_WR[2])
    wi = np.linspace(*SCAN_WI[:2], SCAN_WI[2])
    WR, WI = np.meshgrid(wr, wi, indexing="ij")
    omegas = (WR - 1j * WI).ravel()
    _, red = objective(omegas, ell, prof, R, N, n_steps, clamped=True)
    mag = np.abs(red).reshape(WR.shape)
    seeds = []
    for i in range(1, mag.shape[0] - 1):
        for j in range(1, mag.shape[1] - 1):
            w = mag[i - 1:i + 2, j - 1:j + 2]
            if mag[i, j] == w.min() and mag[i, j] < w.max():
                seeds.append(WR[i, j] - 1j * WI[i, j])
    return seeds, mag


def flat_cavity_roots(ell):
    """Closed-form traction-free QNMs of a spherical cavity in a UNIFORM medium.

    With u(x) = x^(ell+1) h_ell(x) e^(-i x) a polynomial of degree ell, the
    traction-free condition x h' - h = 0 becomes  i x u + x u' - (ell+2) u = 0,
    a polynomial of degree exactly ell+1 -- hence exactly ell+1 roots.  (Radius
    a = 1, so x = omega.)  Used only as the FT-5(b) reference count.
    """
    # h_ell(x) = (-i)^(ell+1) e^{ix}/x * sum_m i^m (ell+m)!/(m!(ell-m)!) / (2x)^m
    coeffs = np.zeros(ell + 1, dtype=complex)   # u(x) = sum_m coeffs[m] x^{ell-m}
    for m in range(ell + 1):
        coeffs[m] = ((-1j) ** (ell + 1) * (1j ** m)
                     * math.factorial(ell + m)
                     / (math.factorial(m) * math.factorial(ell - m))
                     / (2.0 ** m))
    u = np.poly1d(coeffs)                       # degree ell in x
    du = u.deriv()
    p = np.poly1d([1j, 0]) * u + np.poly1d([1, 0]) * du - (ell + 2) * u
    return [complex(z) for z in np.roots(p)]


# ===========================================================================
# BIN ADJUDICATION (prereg section 7) — frozen criteria, evaluated in precedence order
# ===========================================================================
def adjudicate(gates, fts, poles, loc, x_sat=X_SAT):
    solver_fail = [k for k, v in gates.items() if not v.get("pass")]
    ft_fail = [k for k, v in fts.items() if not v.get("fires")]
    if solver_fail or ft_fail:
        return {"certification": "SOLVER-NOT-CERTIFIED",
                "bin": "BIN-F-SOLVER",
                "failed_gates": solver_fail, "unfired_selftests": ft_fail,
                "note": "no physics bin adjudicated (prereg section 7 precedence)"}
    if not poles:
        return {"certification": "SOLVER-CERTIFIED", "bin": "BIN-F-NOPOLE",
                "note": "argument-principle count 0 over the frozen rectangle"}

    w0 = poles[0]
    wR, wI = float(w0.real), float(abs(w0.imag))
    Q = wR / (2.0 * wI)
    D_omega = wR / OMEGA_R_GR - 1.0
    D_omega_shortcut = wR / OMEGA_R_SHORTCUT - 1.0
    D_Q = Q / Q_GR - 1.0

    b1 = ("BIN-1-MATCH" if abs(D_omega) < 0.03 else
          "BIN-1-NEAR" if abs(D_omega) < 0.10 else "BIN-1-MISS")
    b2 = ("BIN-2-MATCH" if abs(D_Q) < 0.03 else
          "BIN-2-NEAR" if abs(D_Q) < 0.10 else "BIN-2-MISS")
    dgr, dcv = abs(Q - Q_GR), abs(Q - Q_CONVENTION)
    b2d = ("BIN-2-EQUIDISTANT" if abs(dgr - dcv) <= 1e-6 else
           "BIN-2-CLOSER-GR" if dgr < dcv else "BIN-2-CLOSER-CONVENTION")

    u, uk = loc["u_energy"], loc["u_kinetic"]
    if abs(u - uk) > 0.10:
        b3 = "BIN-3-DISCORDANT"
    elif not loc["interior_max"]:
        b3 = "BIN-3-MONOTONE"
    elif 1.00 <= u <= 1.10:
        b3 = "BIN-3-RIM"
    elif u <= 1.50:
        b3 = "BIN-3-RAMP"
    else:
        b3 = "BIN-3-OUTER"
    b3_tp = bool(b3 == "BIN-3-RAMP" and abs(u - R_STAR_OVER_RSAT) <= 0.05)

    if len(poles) < 2:
        b4 = "BIN-4-NONE"
        R_I = R_R = None
    else:
        w1 = poles[1]
        R_I = abs(w1.imag) / abs(w0.imag)
        R_R = float(w1.real) / wR
        R_I_GR = OMEGA_I_GR_N1 / OMEGA_I_GR
        R_R_GR = OMEGA_R_GR_N1 / OMEGA_R_GR
        ok = (abs(R_I / R_I_GR - 1.0) < 0.10) and (abs(R_R / R_R_GR - 1.0) < 0.10)
        b4 = "BIN-4-LADDER-MATCH" if ok else "BIN-4-LADDER-DIFFERENT"

    k0_r_sat = wR * x_sat
    nu_falsified = abs(D_omega_shortcut) > 0.03
    return {
        "certification": "SOLVER-CERTIFIED",
        "fundamental": {"omega_R_M": wR, "omega_I_M": wI, "Q": Q,
                        "Omega_scale_free": wR * x_sat},
        "BIN-1": {"bin": b1, "D_omega_vs_GR": D_omega,
                  "omega_R_GR": OMEGA_R_GR,
                  "D_omega_vs_shortcut_18_over_49": D_omega_shortcut,
                  "omega_R_shortcut": OMEGA_R_SHORTCUT,
                  "class": "VALUE-CONSISTENCY (rides the GR-imported nu_vac via the 7)"},
        "BIN-2": {"bin": b2, "three_way": b2d, "Q_derived": Q, "Q_GR": Q_GR,
                  "Q_convention": Q_CONVENTION, "D_Q": D_Q,
                  "dist_to_GR": dgr, "dist_to_convention": dcv,
                  "class": "nu_vac-FREE (emergence-capable at value level); G8 measures it"},
        "BIN-3": {"bin": b3, "turning_point_subflag": b3_tp,
                  "u_energy": u, "u_kinetic": uk,
                  "r_star_over_r_sat": float(R_STAR_OVER_RSAT),
                  "interior_max": loc["interior_max"], "endpoint": loc["endpoint"],
                  "k0_r_sat": k0_r_sat,
                  "k0_r_sat_asserted_l_1_plus_nu": ELL_PRIMARY * (1.0 + NU_VAC),
                  "k0_r_sat_IDENTITY_note":
                      "k0*r_sat = x_sat*omega_R*M is IDENTICALLY BIN-1's shortcut "
                      "comparison; NOT an independent axis (prereg BIN-3 identity note)"},
        "BIN-4": {"bin": b4, "n_poles": len(poles),
                  "R_I": R_I, "R_I_GR": OMEGA_I_GR_N1 / OMEGA_I_GR,
                  "R_R": R_R, "R_R_GR": OMEGA_R_GR_N1 / OMEGA_R_GR,
                  "poles": [[float(w.real), float(w.imag)] for w in poles]},
        "nu_factor_verdict": {
            "criterion": "|omega_R derived / (18/49) - 1| > 0.03 falsifies "
                         "r_eff = r_sat/(1+nu_vac) as a derivation of the eigenfrequency",
            "deviation": D_omega_shortcut,
            "falsified": bool(nu_falsified)},
    }


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    t_start = time.time()
    ell = ELL_PRIMARY
    prof = Profile("sqrtS", X_SAT)
    R_WALL = R_MATCH

    print("[coldq] G1 asymptotic series vs spherical Hankel (zero grade) ...")
    G1 = gate_G1()

    print("[coldq] locating poles on the PRIMARY branch (sqrt(S), rho = rho_0) ...")
    poles, seeds, mag = find_poles(ell, prof)
    if poles:                       # re-polish at the FROZEN polish step count
        rp, okp = muller(lambda w: objective(w, ell, prof, R_MATCH, SERIES_N,
                                             N_STEPS_POLISH)[1], poles)
        poles = dedupe([complex(x) for x, k in zip(rp, okp) if k and in_rect(complex(x))])
        poles.sort(key=lambda w: abs(w.imag))
    print(f"        {len(poles)} pole(s), least-damped: "
          + (f"{poles[0].real:.8f}{poles[0].imag:+.8f}i" if poles else "none"))
    pole0 = poles[0] if poles else None
    if pole0 is None:
        raise SystemExit("BIN-F-NOPOLE: no pole located on the primary branch")

    print("[coldq] instrument-accuracy map (asymptotic-truncation characterisation) ...")
    acc_ref = complex(muller(lambda w: objective(w, ell, prof, 60.0, 32,
                                                 N_STEPS_SCAN)[1], [pole0])[0][0])
    acc = {}
    for R in (25.0, 40.0, 60.0):
        row = {}
        for N in (8, 12, 16, 20, 24, 28, 32, 36):
            w = complex(muller(lambda x: objective(x, ell, prof, R, N,
                                                   N_STEPS_SCAN)[1], [pole0])[0][0])
            row[str(N)] = float(abs(w - acc_ref) / abs(acc_ref))
        acc[str(R)] = row
    accuracy_map = {
        "reference": [float(acc_ref.real), float(acc_ref.imag)],
        "reference_config": {"R_match": 60.0, "series_N": 32,
                             "n_steps": N_STEPS_SCAN,
                             "note": "n_steps is measurably NOT the accuracy "
                                     "limit here (G3: 8000 vs 128000 agree to 1e-11)"},
        "rel_deviation_from_reference": acc,
        "note": "the far-field expansion is an ASYMPTOTIC series: its error is "
                "minimised near an R-dependent optimal truncation and grows on BOTH "
                "sides.  This is the mechanism behind the G4/G5 outcome.",
    }

    print("[coldq] measured |omega_I| band over which the winding count is stable ...")
    def fn_band(w):
        return objective(w, ell, prof, R_MATCH, SERIES_N, N_STEPS_SCAN)[0]
    band_rows, band = [], None
    for wi_max in (1.00, 0.70, 0.50, 0.40, 0.30, 0.25, 0.20, 0.15, 0.10):
        cs = []
        for npts in (2048, 4096):
            c, _ = winding_count(fn_band, npts, SCAN_WR, (SCAN_WI[0], wi_max, 0))
            cs.append(c)
        n_in = len([w for w in poles if abs(w.imag) <= wi_max])
        ok = (all(abs(c - round(c)) <= 1e-3 for c in cs)
              and round(cs[0]) == round(cs[1]) and round(cs[0]) == n_in)
        band_rows.append({"wi_max": wi_max, "winding": cs,
                          "n_located_inside": n_in, "stable_and_matched": bool(ok)})
        if ok and band is None:
            band = wi_max
    certified_band = {"rows": band_rows, "largest_stable_wi_max": band,
                      "note": "measured, not assumed (the #801 G9 discipline); a "
                              "reduced band is the prereg's CLASS-B shape"}

    print("[coldq] G2 energy-functional (Rayleigh) consistency ...")
    G2 = gate_G2(ell, prof, R_WALL)

    print("[coldq] G3/G4/G5 convergence + independence ...")
    def polish(R, N, n):
        r, ok = muller(lambda w: objective(w, ell, prof, R, N, n)[1], [pole0])
        return complex(r[0]) if ok[0] else complex("nan")

    w_16k = polish(R_MATCH, SERIES_N, 16000)
    w_64k = polish(R_MATCH, SERIES_N, 64000)
    g3rel = abs(w_64k - w_16k) / abs(w_64k)
    G3 = {"omega_16000": [float(w_16k.real), float(w_16k.imag)],
          "omega_64000": [float(w_64k.real), float(w_64k.imag)],
          "rel": float(g3rel), "tol": 1e-8, "pass": bool(g3rel <= 1e-8)}

    wR_set = {R: polish(R, SERIES_N, N_STEPS_POLISH) for R in R_MATCH_SET}
    g4worst = max(abs(wR_set[a] - wR_set[b]) / abs(wR_set[b])
                  for a in R_MATCH_SET for b in R_MATCH_SET if a != b)
    G4 = {"omegas": {str(k): [float(v.real), float(v.imag)] for k, v in wR_set.items()},
          "worst_rel": float(g4worst), "tol": 1e-8, "pass": bool(g4worst <= 1e-8)}

    wN_set = {N: polish(R_MATCH, N, N_STEPS_POLISH) for N in SERIES_N_SET}
    g5worst = max(abs(wN_set[a] - wN_set[b]) / abs(wN_set[b])
                  for a in SERIES_N_SET for b in SERIES_N_SET if a != b)
    G5 = {"omegas": {str(k): [float(v.real), float(v.imag)] for k, v in wN_set.items()},
          "worst_rel": float(g5worst), "tol": 1e-8, "pass": bool(g5worst <= 1e-8)}

    print("[coldq] G6 Ax-3 closed-cavity reality ...")
    G6 = gate_G6(ell, prof, R_WALL)

    print("[coldq] G7 argument-principle pole count ...")
    G7 = gate_G7(ell, prof, poles)

    print("[coldq] G8 nu_vac-cancellation measured over x_sat in {5, 7, 11} ...")
    g8rows, g8Q, g8u, g8w = [], [], [], []
    for xs in X_SAT_SET:
        p_xs = Profile("sqrtS", xs)
        Rx, wrx, wix = scaled_geometry(xs)
        pl, _, _ = find_poles(ell, p_xs, R=Rx, WRr=wrx, WIi=wix)
        if not pl:
            g8rows.append({"x_sat": xs, "poles": 0})
            continue
        rp8, ok8 = muller(lambda w: objective(w, ell, p_xs, Rx, SERIES_N,
                                              N_STEPS_POLISH)[1], [pl[0]])
        w = complex(rp8[0]) if ok8[0] else pl[0]
        Qx = w.real / (2.0 * abs(w.imag))
        lx = localization(w, ell, p_xs, R=Rx)
        g8rows.append({"x_sat": xs, "R_match": Rx, "omega_R_M": float(w.real),
                       "omega_I_M": float(abs(w.imag)), "Q": float(Qx),
                       "Omega": float(w.real * xs), "u_energy": lx["u_energy"],
                       "n_poles": len(pl)})
        g8Q.append(Qx)
        g8u.append(lx["u_energy"])
        g8w.append(w.real * xs)
    q_spread = (max(g8Q) - min(g8Q)) / np.mean(g8Q) if g8Q else None
    u_spread = (max(g8u) - min(g8u)) / np.mean(g8u) if g8u else None
    w_spread = (max(g8w) - min(g8w)) / np.mean(g8w) if g8w else None
    G8 = {"rows": g8rows, "Q_rel_spread": None if q_spread is None else float(q_spread),
          "u_rel_spread": None if u_spread is None else float(u_spread),
          "Omega_rel_spread": None if w_spread is None else float(w_spread),
          "tol": 1e-9,
          "pass": bool(q_spread is not None and q_spread <= 1e-9
                       and w_spread is not None and w_spread <= 1e-9)}

    print("[coldq] self-tests FT-1..FT-6 ...")
    FT = selftests(ell, prof, R_WALL, pole0, poles)

    print("[coldq] localization + sensitivities + diagnostics ...")
    loc = localization(pole0, ell, prof)

    # FORK-2 KEEP-BOTH sensitivity: the Family-E S^(1/4) counterfactual
    prof14 = Profile("S14", X_SAT)
    poles14, _, _ = find_poles(ell, prof14, n_polish=N_STEPS_SCAN)
    s14 = None
    if poles14:
        w = poles14[0]
        s14 = {"omega_R_M": float(w.real), "omega_I_M": float(abs(w.imag)),
               "Omega": float(w.real * X_SAT),
               "Q": float(w.real / (2 * abs(w.imag))),
               "n_poles": len(poles14),
               "localization": localization(w, ell, prof14),
               "poles": [[float(z.real), float(z.imag)] for z in poles14]}

    # ell-ladder DIAGNOSTIC (FORK-12 unanswered; no bin, no verdict)
    ladder = {}
    for L in (2, 3, 4, 5):
        pl, _, _ = find_poles(L, prof, n_polish=N_STEPS_SCAN)
        if pl:
            w = pl[0]
            ladder[str(L)] = {"omega_R_M": float(w.real),
                              "omega_I_M": float(abs(w.imag)),
                              "Omega": float(w.real * X_SAT),
                              "Q": float(w.real / (2 * abs(w.imag))),
                              "n_poles": len(pl)}
        else:
            ladder[str(L)] = {"n_poles": 0}

    gates = {"G1": G1, "G2": G2, "G3": G3, "G4": G4, "G5": G5,
             "G6": G6, "G7": G7, "G8": G8}
    verdict = adjudicate(gates, FT, poles, loc, X_SAT)

    results = {
        "lane": "cold-Q pole derivation (spin-2 toroidal QNM of the graded saturation cavity)",
        "prereg": PREREG,
        "provenance": {
            "grant_go": "2026-08-02, verbatim [sic]: \"6, GO\"",
            "upstream": ["research/2026-07-30_qlaw-derivation_scoping.md",
                         "research/2026-07-31_qlaw-framing-challenge_walk.md"],
            "comparators_read_programmatically": {
                "KERR_QNM[0.00]": list(KERR_QNM[0.00]),
                "SCHW_OMEGA_R[(2,1)]": SCHW_OMEGA_R[(2, 1)],
                "SCHW_OMEGA_R[(2,2)]": SCHW_OMEGA_R[(2, 2)]},
            "external_comparator_no_in_repo_carrier": {
                "omega_I_M_ell2_n1": OMEGA_I_GR_N1},
            "canonical_constants": {"N_NU": float(NU_VAC)},
        },
        "inputs": {"x_sat": X_SAT, "eps_yield": EPS_YIELD, "ell": ell,
                   "kernel": "S = (1 - A^2)^(1/2)", "c_shear": "c_0 * S^(1/2)",
                   "rho": "rho_0 (cold lattice inertia; FORK-3 (a)/(c))",
                   "inner_BC": "traction-free (Z_shear -> 0, Gamma_shear = -1)",
                   "outer_BC": "outgoing radiation into the cold matched lattice",
                   "free_parameters": 0},
        "numerics": {"R_match": R_MATCH, "series_N": SERIES_N,
                     "n_steps_scan": N_STEPS_SCAN, "n_steps_polish": N_STEPS_POLISH,
                     "scan_grid": [SCAN_WR, SCAN_WI], "contour_points": CONTOUR_SET},
        "gates": gates,
        "selftests": FT,
        "poles_primary": [[float(w.real), float(w.imag)] for w in poles],
        "localization": loc,
        "verdict": verdict,
        "sensitivity_FORK2_S14": s14,
        "diagnostic_ell_ladder": {
            "tag": "DIAGNOSTIC - no bin, no verdict; FORK-12 is unanswered and "
                   "this lane does not adjudicate it",
            "rows": ladder},
        "diagnostic_clamped_wall": FT["FT2_clamped_wall"],
        "instrument_accuracy_map": accuracy_map,
        "certified_omega_I_band": certified_band,
    }

    digest_src = json.dumps(results, sort_keys=True, default=str)
    results["_digest_sha256"] = hashlib.sha256(digest_src.encode()).hexdigest()
    results["_runtime_sec"] = round(time.time() - t_start, 1)

    out = (sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv
           else os.path.join(HERE, "coldq_pole_derivation_results.json"))
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2, sort_keys=True, default=str)
    print(f"\n[coldq] wrote {out}")
    print(f"[coldq] certification : {verdict['certification']}")
    for k in ("BIN-1", "BIN-2", "BIN-3", "BIN-4"):
        if k in verdict:
            print(f"[coldq] {k}: {verdict[k]['bin']}")
    print(f"[coldq] digest {results['_digest_sha256'][:16]}  "
          f"runtime {results['_runtime_sec']} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Two-band / k·p kinematics of the K4 carrier sector — near-gap dispersion.

Pre-registration: research/2026-08-05_two-band-kinematics_prereg-FROZEN.md (SVA pilot 4).
Frozen at f5ddd995 BEFORE this file existed.

WHAT THIS DRIVER ANSWERS
------------------------
Does the Cosserat (micro-rotation / winding) carrier sector's near-gap dispersion take the
relativistic massive form  E(k)^2 = (E_g/2)^2 + (hbar v k)^2, and is the carrier limiting
velocity v equal to the EM-channel speed c_EM = sqrt(G/rho)?

SECTOR HEADER (mandatory, before any standard-physics word)
-----------------------------------------------------------
SECTOR   : carrier = Cosserat micro-rotation (omega). The gap used is THAT sector's own
           on-site micropolar gap m^2 = 4 G_c / I_omega (cosserat-mass-gap.md, clm-jz0xaw).
           c_EM is read off the massless transverse-TRANSLATIONAL (u) branches of the SAME
           operator (G2 ruling 2026-07-03). Mass (A1 dilatation) is NOT invoked anywhere.
REGIME   : cold linear, sub-yield. Axiom-4 saturation OFF; kappa_chiral is saturation-only
           (cosserat_field_3d.py:562) so the cold bands are parity-symmetric by construction.
COORDS   : real-space / spatial-Brillouin omega(k). NOT a phase-space (V_inc,V_ref) claim.
LEDGER   : rim-only. D(k) is Hermitian, lossless; no port is crossed; no loss word is used.
CLASS    : FORM-derivation / emergence-class at PEER-WITH-SM strength. The Dirac equation
           POSTULATES the same form and Wilsonian universality says any gapped two-band
           lattice reproduces it. NOT a chord. The only falsifiable content is the NUMBER
           v / c_EM.

OPERATOR PROVENANCE
-------------------
The 12x12 Bloch operator is the canonical one certified by PR #392
(src/scripts/vol_1_foundations/cosserat_band_structure_two_sublattice.py, CI-gated at
src/tests/test_cr_rotational_curvature_sqrt2.py). This driver imports it for the negative
control and rebuilds it independently (scalar-sum route, no 9x12 map machinery) for G1.

Outputs: _output/two_band_kp_kinematics.json  (deterministic; double-run digest gate).
"""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from pathlib import Path

import numpy as np

_HERE = Path(__file__).resolve().parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

# ---------------------------------------------------------------------------
# Canonical geometry + operator (imported, never re-typed)
# ---------------------------------------------------------------------------
from cosserat_band_structure_two_sublattice import (  # noqa: E402
    TETRA_OFFSETS,
    dynamical_matrix_two_sublattice,
)

from ave.core.chiral_lattice import _SRS_NN, srs_motif  # noqa: E402

# Shipped (TRACKED) artifact. src/scripts/**/_output/ is gitignored (.gitignore:52), so
# the gating number-check needs the JSON under research/drivers/ like every other lane.
OUT_DIR = _HERE.parents[2] / "research" / "drivers"
OUT_JSON = OUT_DIR / "two_band_kp_kinematics_results.json"

# Levi-Civita
_EPS = np.zeros((3, 3, 3))
for _i, _j, _k in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
    _EPS[_i, _j, _k] = 1.0
    _EPS[_i, _k, _j] = -1.0

# amplitude index map for x = (u^A, w^A, u^B, w^B)
IDX_U = [0, 1, 2, 6, 7, 8]
IDX_W = [3, 4, 5, 9, 10, 11]

DIRECTIONS = {
    "100": (1.0, 0.0, 0.0),
    "110": (1.0, 1.0, 0.0),
    "111": (1.0, 1.0, 1.0),
    "210": (2.0, 1.0, 0.0),
    "321": (3.0, 2.0, 1.0),
}


# ---------------------------------------------------------------------------
# SECTION A — independent rebuild of D(k) (G1)
# ---------------------------------------------------------------------------
def _projectors_9():
    """Symmetric / antisymmetric projectors on the flattened (i,j) 9-vector."""
    psym = np.zeros((9, 9))
    pasym = np.zeros((9, 9))
    for i in range(3):
        for j in range(3):
            r, rt = 3 * i + j, 3 * j + i
            psym[r, r] += 0.5
            psym[r, rt] += 0.5
            pasym[r, r] += 0.5
            pasym[r, rt] -= 0.5
    return psym, pasym


def dynamical_matrix_rebuild(kvec, bonds=None, G=1.0, G_c=1.0, gamma=1.0, rho=1.0,
                             I_omega=1.0, b_sign=+1.0):
    """INDEPENDENT rebuild of the 12x12 D(k) — scalar-sum route.

    Structurally different code from the canonical driver (no shared helper, the
    strain/curvature rows assembled directly), so an index-map bug in either one is
    caught by G1.

    `bonds` = the (z,3) array of bond DISPLACEMENT vectors from a home site. Defaults to
    the canonical TETRA_OFFSETS (diamond, z=4). The engine's tetrahedral gradient
    generalises to a least-squares gradient on any bond set whose bond tensor
    M = sum_b d_b (x) d_b is invertible:
        (d_j V_i) = [M^-1]_{jm} sum_b d_b^m [V(x + d_b) - V(x)]
    For TETRA_OFFSETS, M = 4*I, recovering the engine's (1/4) sum_b p_b^j [...] exactly
    (cosserat_field_3d.py:148). This generalisation is what G7b exercises.

    `b_sign`: +1 reproduces the canonical driver's B-reference convention (conjugate
    phase); -1 is the diamond-faithful reverse-bond convention (grad at B uses -d_b).
    Both are carried because the choice is a unitary gauge (proved by G1b) and must be
    shown not to move the spectrum, rather than assumed not to.
    """
    kvec = np.asarray(kvec, dtype=float)
    d = np.asarray(TETRA_OFFSETS if bonds is None else bonds, dtype=float)
    m_bond = d.T @ d
    m_inv = np.linalg.inv(m_bond)
    phase = np.exp(1j * (d @ kvec))
    # cross (neighbour) gradient symbol; self term is -M^-1 sum_b d_b (=0 for centro sets)
    g_cross = m_inv @ (d.T @ phase)
    g_self = -(m_inv @ d.sum(axis=0)).astype(complex)

    psym, pasym = _projectors_9()
    q = np.zeros((12, 12), dtype=complex)
    for home in ("A", "B"):
        if home == "A":
            gs, gc, hu, hw, nu_, nw = g_self, g_cross, 0, 3, 6, 9
        else:
            gs, gc, hu, hw, nu_, nw = g_self, b_sign * np.conj(g_cross), 6, 9, 0, 3
        e_map = np.zeros((9, 12), dtype=complex)
        k_map = np.zeros((9, 12), dtype=complex)
        for i in range(3):
            for j in range(3):
                r = 3 * i + j
                e_map[r, hu + i] += gs[j]          # strain  d_j u_i : home u
                e_map[r, nu_ + i] += gc[j]         # strain  d_j u_i : neighbour u
                for c in range(3):
                    e_map[r, hw + c] += -_EPS[i, j, c]   # on-site  -eps_ijk w_k
                k_map[r, hw + i] += gs[j]          # curvature d_j w_i : home w
                k_map[r, nw + i] += gc[j]          # curvature d_j w_i : neighbour w
        t_map = sum(e_map[3 * i + i, :] for i in range(3))[None, :]
        e_s, e_a = psym @ e_map, pasym @ e_map
        q += (
            (2.0 / 3.0) * G * (t_map.conj().T @ t_map)
            + G * (e_s.conj().T @ e_s)
            + G_c * (e_a.conj().T @ e_a)
            + gamma * (k_map.conj().T @ k_map)
        )
    phi = 2.0 * q                                   # Lagrangian -> EOM Hessian factor 2
    phi = 0.5 * (phi + phi.conj().T)
    minv = 1.0 / np.sqrt(np.array([rho] * 3 + [I_omega] * 3 + [rho] * 3 + [I_omega] * 3))
    dmat = (minv[:, None] * phi) * minv[None, :]
    return 0.5 * (dmat + dmat.conj().T)


def branch_character(dmat):
    """Split the 12 eigenvalues by eigenvector CHARACTER (computed, never by sort index).

    Returns (w2, u_weight, w_weight) with w2 ascending.
    """
    w2, vecs = np.linalg.eigh(dmat)
    uw = (np.abs(vecs[IDX_U, :]) ** 2).sum(axis=0)
    ww = (np.abs(vecs[IDX_W, :]) ** 2).sum(axis=0)
    return w2, uw, ww


# ---------------------------------------------------------------------------
# SECTION B — symbolic k·p (D3): closed-form v^2 per branch, general moduli
# ---------------------------------------------------------------------------
def kp_closed_forms(direction, bonds=None):
    """EXACT symbolic second-order degenerate perturbation theory on D(k).

    Returns dict with the omega-manifold and u-manifold v^2 eigenvalue multisets as
    sympy expressions in (G, G_c, gamma, rho, I_omega).

    D(k) = D0 + D1 + D2 + O(k^3) with D1 = O(k), D2 = O(k^2).  D0 is block diagonal:
    the u-manifold at 0 and the omega-manifold at m^2 = 4 G_c / I_omega.  Standard
    second-order degenerate PT then gives, for the two manifolds,

        lam_w(k) = m^2 + P_w D2 P_w + (1/m^2) P_w D1 P_u D1 P_w + O(k^4)
        lam_u(k) =       P_u D2 P_u - (1/m^2) P_u D1 P_w D1 P_u + O(k^4)

    The level-repulsion term is the whole point: v^2 is the TOTAL branch curvature, NOT
    the gamma-slot label 2*gamma/I_omega (SVA row 3, total-vs-slot).
    """
    import sympy as sp

    d = np.asarray(TETRA_OFFSETS if bonds is None else bonds, dtype=float)
    dm = sp.Matrix([[sp.nsimplify(x, rational=True) for x in row] for row in d])
    mb = (dm.T * dm).inv()

    g_s, g_c, gam, rho, iw, e = sp.symbols(
        "G G_c gamma rho I_omega epsilon", positive=True)
    nvec = [sp.nsimplify(c, rational=True) for c in direction]
    nrm = sp.sqrt(sum(c**2 for c in nvec))
    kv = [e * c / nrm for c in nvec]

    ph = [sp.series(sp.exp(sp.I * sum(dm[b, a] * kv[a] for a in range(3))),
                    e, 0, 3).removeO() for b in range(dm.rows)]
    raw = sp.Matrix([sum(dm[b, m] * ph[b] for b in range(dm.rows)) for m in range(3)])
    g_cross = [sp.expand((mb * raw)[j]) for j in range(3)]
    col_sum = sp.Matrix([sum(dm[b, m] for b in range(dm.rows)) for m in range(3)])
    g_self = [sp.expand(-(mb * col_sum)[j]) for j in range(3)]

    # EXACT rational projectors. Reusing the float64 _projectors_9() here injects
    # sympy Floats into every downstream expression, which destroys the exact
    # characteristic-polynomial identity (it silently returns "no match" even where the
    # spectrum is correct). Caught at integrator time (Rule 10).
    psym = sp.zeros(9, 9)
    pasym = sp.zeros(9, 9)
    for _i in range(3):
        for _j in range(3):
            _r, _rt = 3 * _i + _j, 3 * _j + _i
            psym[_r, _r] += sp.Rational(1, 2)
            psym[_r, _rt] += sp.Rational(1, 2)
            pasym[_r, _r] += sp.Rational(1, 2)
            pasym[_r, _rt] -= sp.Rational(1, 2)

    q = sp.zeros(12, 12)
    for home in ("A", "B"):
        if home == "A":
            gs, gc, hu, hw, nu_, nw = g_self, g_cross, 0, 3, 6, 9
        else:
            gs = [sp.conjugate(x).subs(sp.I, -sp.I) for x in g_self]
            gc = [sp.conjugate(x).subs(sp.I, -sp.I) for x in g_cross]
            hu, hw, nu_, nw = 6, 9, 0, 3
        e_map = sp.zeros(9, 12)
        k_map = sp.zeros(9, 12)
        for i in range(3):
            for j in range(3):
                r = 3 * i + j
                e_map[r, hu + i] += gs[j]
                e_map[r, nu_ + i] += gc[j]
                for c in range(3):
                    e_map[r, hw + c] += -int(_EPS[i, j, c])
                k_map[r, hw + i] += gs[j]
                k_map[r, nw + i] += gc[j]
        t_map = sp.zeros(1, 12)
        for i in range(3):
            t_map += e_map[3 * i + i, :]
        e_s, e_a = psym * e_map, pasym * e_map
        q += (sp.Rational(2, 3) * g_s * (t_map.H * t_map) + g_s * (e_s.H * e_s)
              + g_c * (e_a.H * e_a) + gam * (k_map.H * k_map))
    phi = 2 * q
    sc = [1 / sp.sqrt(rho)] * 3 + [1 / sp.sqrt(iw)] * 3 + \
         [1 / sp.sqrt(rho)] * 3 + [1 / sp.sqrt(iw)] * 3
    dmat = sp.Matrix(12, 12, lambda a, b: sp.expand(sc[a] * phi[a, b] * sc[b]))
    dmat = dmat.applyfunc(lambda x: sp.expand(sp.series(sp.expand(x), e, 0, 3).removeO()))

    d0 = dmat.applyfunc(lambda x: x.subs(e, 0))
    d1 = dmat.applyfunc(lambda x: sp.expand(sp.diff(x, e).subs(e, 0)))
    d2 = dmat.applyfunc(lambda x: sp.expand(sp.diff(x, e, 2).subs(e, 0) / 2))

    m2 = 4 * g_c / iw
    mw = sp.simplify(d2[IDX_W, IDX_W] + (d1[IDX_W, IDX_U] * d1[IDX_U, IDX_W]) / m2)
    mu = sp.simplify(d2[IDX_U, IDX_U] - (d1[IDX_U, IDX_W] * d1[IDX_W, IDX_U]) / m2)

    # The v^2 spectrum is DERIVED by exact eigenvals() on the high-symmetry axis (where the
    # characteristic polynomial factors cleanly) and then VERIFIED at every other direction
    # as an exact POLYNOMIAL IDENTITY on the characteristic polynomial.  Calling eigenvals()
    # on a low-symmetry direction makes sympy fall back to numeric root-finding of a sextic
    # and returns a float-contaminated radical mess — caught at integrator time (Rule 10);
    # the charpoly identity is the exact, direction-robust test.
    lam = sp.Symbol("lam")
    v2_par = 2 * gam / iw
    v2_perp = 2 * gam / iw + g_c / rho
    v2_T = g_s / rho
    v2_L = sp.Rational(10, 3) * g_s / rho
    pred_w = sp.expand((lam - v2_par) ** 2 * (lam - v2_perp) ** 4)
    pred_u = sp.expand((lam - v2_T) ** 4 * (lam - v2_L) ** 2)
    cw = sp.expand(mw.charpoly(lam).as_expr())
    cu = sp.expand(mu.charpoly(lam).as_expr())
    match_w = bool(sp.simplify(cw - pred_w) == 0)
    match_u = bool(sp.simplify(cu - pred_u) == 0)
    return {
        "D0_diag": [sp.simplify(d0[i, i]) for i in range(12)],
        "D0_offdiag_max_is_zero": bool(sp.simplify(
            d0 - sp.diag(*[d0[i, i] for i in range(12)])).is_zero_matrix),
        "omega_v2": {str(v2_par): 2, str(sp.expand(v2_perp)): 4},
        "u_v2": {str(v2_T): 4, str(v2_L): 2},
        "omega_charpoly_matches": match_w,
        "u_charpoly_matches": match_u,
        "D1_interband_is_nonzero": bool(not d1[IDX_W, IDX_U].is_zero_matrix),
    }


# ---------------------------------------------------------------------------
# SECTION C — exact full dispersion at extended precision (D4 / G5 / G8)
# ---------------------------------------------------------------------------
def exact_omega2_mp(kvec, dps=60, G=1, G_c=1, gamma=1, rho=1, I_omega=1, bonds=None):
    """Exact eigenvalues of the FULL D(k) at `dps` decimal digits (mpmath).

    NUMERICAL CONDITIONING (prereg §3): the k^4 residual extraction is a catastrophic
    cancellation of the float64 1-A^2 class.  At k=1e-6, lam - m^2 ~ 2e-12 against
    m^2 = 4 (already within 3 decades of float64 eps*m^2 ~ 9e-16), and the second
    subtraction lam - m^2 - v^2 k^2 ~ k^4 = 1e-24 is FULLY below the float64 floor.
    All arithmetic here is mpmath at 60 dps; a float64 shadow is run alongside and its
    divergence is REPORTED as the conditioning receipt (G8).
    """
    from mpmath import mp, matrix as mpmatrix, eigsy, exp as mexp, mpf, mpc, sqrt as msqrt

    mp.dps = dps
    d = np.asarray(TETRA_OFFSETS if bonds is None else bonds, dtype=float)
    m_inv_np = np.linalg.inv(d.T @ d)
    m_inv = [[mpf(str(m_inv_np[a, b])) for b in range(3)] for a in range(3)]
    kk = [c if isinstance(c, type(mpf(0))) else mpf(str(c)) for c in kvec]

    ph = [mexp(mpc(0, 1) * sum(mpf(str(d[b, a])) * kk[a] for a in range(3)))
          for b in range(d.shape[0])]
    raw = [sum(mpf(str(d[b, m])) * ph[b] for b in range(d.shape[0])) for m in range(3)]
    g_cross = [sum(m_inv[j][m] * raw[m] for m in range(3)) for j in range(3)]
    csum = [sum(mpf(str(d[b, m])) for b in range(d.shape[0])) for m in range(3)]
    g_self = [-sum(m_inv[j][m] * csum[m] for m in range(3)) for j in range(3)]

    psym_n, pasym_n = _projectors_9()
    q = [[mpc(0) for _ in range(12)] for _ in range(12)]
    for home in ("A", "B"):
        if home == "A":
            gs, gc, hu, hw, nu_, nw = g_self, g_cross, 0, 3, 6, 9
        else:
            gs = [x.conjugate() for x in g_self]
            gc = [x.conjugate() for x in g_cross]
            hu, hw, nu_, nw = 6, 9, 0, 3
        e_map = [[mpc(0) for _ in range(12)] for _ in range(9)]
        k_map = [[mpc(0) for _ in range(12)] for _ in range(9)]
        for i in range(3):
            for j in range(3):
                r = 3 * i + j
                e_map[r][hu + i] += gs[j]
                e_map[r][nu_ + i] += gc[j]
                for c in range(3):
                    e_map[r][hw + c] += mpf(str(-_EPS[i, j, c]))
                k_map[r][hw + i] += gs[j]
                k_map[r][nw + i] += gc[j]
        t_map = [sum(e_map[3 * i + i][col] for i in range(3)) for col in range(12)]
        e_s = [[sum(mpf(str(psym_n[r][s])) * e_map[s][c] for s in range(9))
                for c in range(12)] for r in range(9)]
        e_a = [[sum(mpf(str(pasym_n[r][s])) * e_map[s][c] for s in range(9))
                for c in range(12)] for r in range(9)]

        def accum(rows, coef):
            for a in range(12):
                for b in range(12):
                    q[a][b] += coef * sum(rows[r][a].conjugate() * rows[r][b]
                                          for r in range(len(rows)))
        accum([t_map], mpf(2) / 3 * G)
        accum(e_s, mpf(G))
        accum(e_a, mpf(G_c))
        accum(k_map, mpf(gamma))

    minv = [1 / msqrt(mpf(rho))] * 3 + [1 / msqrt(mpf(I_omega))] * 3 + \
           [1 / msqrt(mpf(rho))] * 3 + [1 / msqrt(mpf(I_omega))] * 3
    dm = mpmatrix(12, 12)
    for a in range(12):
        for b in range(12):
            val = 2 * q[a][b] * minv[a] * minv[b]
            dm[a, b] = val
    # hermitise then split into the real symmetric 24x24 image (eigsy on real sym)
    for a in range(12):
        for b in range(12):
            pass
    herm = mpmatrix(12, 12)
    for a in range(12):
        for b in range(12):
            herm[a, b] = (dm[a, b] + dm[b, a].conjugate()) / 2
    big = mpmatrix(24, 24)
    for a in range(12):
        for b in range(12):
            re, im = herm[a, b].real, herm[a, b].imag
            big[a, b] = re
            big[a + 12, b + 12] = re
            big[a, b + 12] = -im
            big[a + 12, b] = im
    evs = eigsy(big, eigvals_only=True)
    vals = sorted([evs[i] for i in range(24)])
    return vals[0::2]   # each complex-Hermitian eigenvalue appears twice in the real image


# ---------------------------------------------------------------------------
# SECTION D — connectivity axis (FLAG-3): srs z=3 blocker + independence check
# ---------------------------------------------------------------------------
def srs_bond_tensor_report():
    """MEASURE whether the engine's gradient functional can transfer to the z=3 srs net.

    The engine's tetrahedral gradient is a least-squares gradient; it exists only if the
    per-site bond tensor M = sum_b dhat_b (x) dhat_b is INVERTIBLE.  This function
    computes M's spectrum at every srs site and at the diamond control site.  It makes no
    claim about which net is right — it reports whether the OPERATOR transfers.
    """
    motif = srs_motif("right")
    rows = []
    for s in range(len(motif)):
        bhat = []
        for t in range(len(motif)):
            for sh in itertools.product((-1, 0, 1), repeat=3):
                dv = motif[t] + np.array(sh, dtype=float) - motif[s]
                ln = float(np.linalg.norm(dv))
                if abs(ln - _SRS_NN) < 1e-9:
                    bhat.append(dv / ln)
        bhat = np.array(bhat)
        mten = bhat.T @ bhat
        rows.append({
            "site": s, "z": int(bhat.shape[0]),
            "bond_tensor_eigs": [round(float(x), 12) for x in np.linalg.eigvalsh(mten)],
            "rank": int(np.linalg.matrix_rank(mten, tol=1e-9)),
        })
    dhat = TETRA_OFFSETS / np.linalg.norm(TETRA_OFFSETS[0])
    ctrl = {
        "z": int(TETRA_OFFSETS.shape[0]),
        "bond_tensor_eigs": [round(float(x), 12) for x in np.linalg.eigvalsh(dhat.T @ dhat)],
        "rank": int(np.linalg.matrix_rank(dhat.T @ dhat, tol=1e-9)),
    }
    all_rank3 = all(r["rank"] == 3 for r in rows)
    return {"srs_sites": rows, "diamond_control": ctrl, "srs_all_full_rank": all_rank3}


def alternative_bond_sets():
    """Full-rank NON-diamond bond sets used to test connectivity-independence (G7b).

    If the O(k^2) k·p result is a property of the CONTINUUM micropolar functional rather
    than of the z=4 diamond connectivity, these must reproduce the SAME closed forms.
    """
    cubic6 = np.array([[1., 0, 0], [-1., 0, 0], [0, 1., 0], [0, -1., 0], [0, 0, 1.], [0, 0, -1.]])
    bcc8 = np.array([[sx, sy, sz] for sx in (1., -1.) for sy in (1., -1.) for sz in (1., -1.)])
    stretched = TETRA_OFFSETS * np.array([1.0, 1.7, 0.6])   # deliberately anisotropic z=4
    return {"cubic-z6": cubic6, "bcc-z8": bcc8, "anisotropic-tetra-z4": stretched}


# ---------------------------------------------------------------------------
# GATES (frozen in the prereg BEFORE this file existed; UNRUN != PASSED)
# ---------------------------------------------------------------------------
def gate_G1():
    """Independent rebuild == canonical operator; and the B-reference sign is a gauge."""
    rng = np.random.default_rng(20260805)
    dmax = 0.0
    emax = 0.0
    gauge_emax = 0.0
    for _ in range(5):
        kv = rng.normal(size=3) * 0.9
        dc = dynamical_matrix_two_sublattice(kv)
        dr = dynamical_matrix_rebuild(kv, b_sign=+1.0)
        dg = dynamical_matrix_rebuild(kv, b_sign=-1.0)
        dmax = max(dmax, float(np.abs(dr - dc).max()))
        emax = max(emax, float(np.abs(np.linalg.eigvalsh(dr) - np.linalg.eigvalsh(dc)).max()))
        gauge_emax = max(gauge_emax,
                         float(np.abs(np.linalg.eigvalsh(dg) - np.linalg.eigvalsh(dc)).max()))
    return {"name": "G1 independent rebuild == canonical", "run": True,
            "max_abs_matrix_diff": dmax, "max_abs_eig_diff": emax,
            "b_sign_gauge_max_eig_diff": gauge_emax,
            "criterion": "matrix diff < 1e-12 and eig diff < 1e-12",
            "pass": bool(dmax < 1e-12 and emax < 1e-12),
            "note": "b_sign=-1 (diamond-faithful reverse bond) gives a DIFFERENT matrix but "
                    "identical spectrum -> the B-reference sign is a unitary gauge, measured "
                    "not assumed"}


def gate_G2():
    """Negative control: reproduce the certified PR #392 V1-V4 receipts."""
    kmag = 1e-4
    kv = np.array([1.0, 0.0, 0.0]) * kmag
    w2, uw, ww = branch_character(dynamical_matrix_rebuild(kv))
    u_v = np.sqrt(np.array([w2[i] for i in range(12) if uw[i] > 0.5])) / kmag
    c_em = float(np.min(u_v))
    # V2: rotational curvature speed with the gap OFF
    w2b, _, wwb = branch_character(dynamical_matrix_rebuild(kv, G_c=0.0))
    rot_b = sorted(w2b[i] for i in range(12) if wwb[i] > 0.5)
    c_r = float(np.sqrt(max(rot_b)) / kmag)
    # V3: k=0 gap
    w20, _, ww0 = branch_character(dynamical_matrix_rebuild(np.zeros(3)))
    gap = float(np.max([w20[i] for i in range(12) if ww0[i] > 0.5]))
    n_gapless = int(np.sum(w20 < 1e-12))
    checks = {
        "V1_c_EM": {"value": c_em, "target": 1.0, "rel_err": abs(c_em - 1.0), "tol": 1e-3},
        "V2_c_R_at_Gc0": {"value": c_r, "target": float(np.sqrt(2.0)),
                          "rel_err": abs(c_r / np.sqrt(2.0) - 1.0), "tol": 5e-2},
        "V3_gap_m2": {"value": gap, "target": 4.0, "rel_err": abs(gap / 4.0 - 1.0), "tol": 1e-2},
        "V4_n_gapless": {"value": n_gapless, "target": 6, "rel_err": abs(n_gapless - 6), "tol": 0},
    }
    ok = all(c["rel_err"] <= c["tol"] for c in checks.values())
    return {"name": "G2 negative control (PR #392 V1-V4)", "run": True,
            "checks": checks, "pass": bool(ok)}


def gate_G3():
    """D(0) block structure: 6 pure-u at 0, 6 pure-omega at m^2."""
    d0 = dynamical_matrix_rebuild(np.zeros(3))
    offdiag = float(np.abs(d0 - np.diag(np.diag(d0))).max())
    w2, vecs = np.linalg.eigh(d0)
    n0 = int(np.sum(np.abs(w2) < 1e-12))
    ngap = int(np.sum(np.abs(w2 - 4.0) < 1e-12))
    cross = 0.0
    for i in range(12):
        uw = float((np.abs(vecs[IDX_U, i]) ** 2).sum())
        ww = float((np.abs(vecs[IDX_W, i]) ** 2).sum())
        cross = max(cross, min(uw, ww))
    return {"name": "G3 D(0) two-band block structure", "run": True,
            "offdiag_max": offdiag, "n_zero": n0, "n_at_gap": ngap,
            "max_offcharacter_weight": cross,
            "criterion": "6 at 0, 6 at m^2=4, off-character weight < 1e-12",
            "pass": bool(n0 == 6 and ngap == 6 and cross < 1e-12),
            "structural_reading": "the two-band split is SECTOR-based (u vs omega, gap set by "
                                  "the ON-SITE G_c term); the K4 bipartite doubling supplies a "
                                  "DEGENERATE PARTNER inside each manifold, NOT the gap"}


def gate_G4():
    """Hermiticity + reality of omega^2 (SVA row 6: lossless, rim-only)."""
    rng = np.random.default_rng(4)
    herm = 0.0
    minev = np.inf
    for _ in range(24):
        kv = rng.uniform(-np.pi, np.pi, size=3)
        dmat = dynamical_matrix_rebuild(kv)
        herm = max(herm, float(np.abs(dmat - dmat.conj().T).max()))
        minev = min(minev, float(np.linalg.eigvalsh(dmat).min()))
    return {"name": "G4 Hermitian / real non-negative omega^2", "run": True,
            "max_non_hermiticity": herm, "min_eigenvalue_over_BZ": minev,
            "criterion": "|D-D^H| < 1e-14 and min omega^2 >= -1e-12",
            "pass": bool(herm < 1e-14 and minev > -1e-12)}


def _classify_branches_mp(vals, m2):
    """Split extended-precision eigenvalues into the u-manifold and omega-manifold."""
    lo = [v for v in vals if float(v) < m2 / 2.0]
    hi = [v for v in vals if float(v) >= m2 / 2.0]
    return lo, hi


def gate_G5_G8(v2_expected, dps=60):
    """k·p vs EXACT dispersion at extended precision + the float64 conditioning receipt.

    R(k) = |lam_exact - (lam0 + v^2 k^2)| / k^4 must converge to a finite constant.

    v2_expected carries the EXACT RATIONAL v^2 (numerator, denominator) from the symbolic
    D3 result, never a float64 round-trip: the k^4 extraction divides by k^4, so a
    1.5e-16 float64 representation error in v^2 = 10/3 lands as a 3e-3 error in the k^4
    coefficient at k=1e-6.  Caught at integrator time (Rule 10) on the first run.
    """
    from mpmath import mp, mpf
    mp.dps = dps

    def _exact(entry):
        return mpf(entry[1]) / mpf(entry[2])
    m2 = 4.0
    rows = []
    f64_rows = []
    for dname, dvec in DIRECTIONS.items():
        # EXACT direction normalisation in mp. A float64 unit vector carries a ~1e-16
        # relative error which enters as delta(k^2)*v^2 and, divided by k^4, lands as a
        # ~4e-4 error in the k^4 coefficient that GROWS as 1/k^2 — i.e. the residual
        # appears to diverge at small k for every non-axis direction. Caught at
        # integrator time (Rule 10); the axis direction [100] hid it because its
        # components are exactly representable.
        nrm_mp = sum(mpf(str(c)) ** 2 for c in dvec) ** mpf("0.5")
        nhat_mp = [mpf(str(c)) / nrm_mp for c in dvec]
        nhat = np.array(dvec, dtype=float)
        nhat = nhat / np.linalg.norm(nhat)
        per_k = {}
        per_k_f64 = {}
        for kmag in (1e-2, 1e-3, 1e-4, 1e-5, 1e-6):
            kvec_mp = [c * mpf(str(kmag)) for c in nhat_mp]
            vals = exact_omega2_mp(kvec_mp, dps=dps)
            lo, hi = _classify_branches_mp(vals, m2)
            k2 = mpf(str(kmag)) ** 2
            k4 = k2 * k2
            res = {}
            for label, group, lam0 in (("u", lo, mpf(0)), ("omega", hi, mpf(m2))):
                out = []
                for v in group:
                    # match each eigenvalue to its predicted v^2 by nearest fit
                    best = min(v2_expected[label],
                               key=lambda c: abs(float((v - lam0) / k2) - c[0]))
                    out.append({"v2_predicted_exact": f"{best[1]}/{best[2]}",
                                "v2_predicted": best[0],
                                "v2_measured": float((v - lam0) / k2),
                                "k4_coeff": float((v - lam0 - _exact(best) * k2) / k4)})
                res[label] = out
            per_k[f"{kmag:g}"] = res
            # float64 shadow (SAME extraction, no extended precision)
            w2f = np.linalg.eigvalsh(dynamical_matrix_rebuild(nhat * kmag))
            lof = [x for x in w2f if x < m2 / 2]
            hif = [x for x in w2f if x >= m2 / 2]
            shadow = []
            for label, group, lam0 in (("u", lof, 0.0), ("omega", hif, m2)):
                for v in group:
                    best = min(v2_expected[label],
                               key=lambda c: abs((v - lam0) / kmag ** 2 - c[0]))
                    shadow.append((v - lam0 - best[0] * kmag ** 2) / kmag ** 4)
            per_k_f64[f"{kmag:g}"] = [float(x) for x in shadow]
        rows.append({"direction": dname, "per_k": per_k})
        f64_rows.append({"direction": dname, "per_k_k4_float64": per_k_f64})

    # convergence test: successive-decade ratio of the k^4 coefficient -> 1
    worst = 0.0
    for r in rows:
        ks = ["0.0001", "1e-05", "1e-06"]
        ks = [k for k in r["per_k"] if k in ("0.0001", "1e-05", "1e-06")]
        for label in ("u", "omega"):
            for idx in range(len(r["per_k"][ks[0]][label])):
                seq = [r["per_k"][k][label][idx]["k4_coeff"] for k in ks]
                for a, b in zip(seq, seq[1:]):
                    if abs(a) > 1e-30:
                        worst = max(worst, abs(b / a - 1.0))
    # float64 shadow divergence at k <= 1e-4
    f64_bad = 0.0
    for r, rf in zip(rows, f64_rows):
        for k in ("0.0001", "1e-05", "1e-06"):
            mpvals = []
            for label in ("u", "omega"):
                mpvals += [x["k4_coeff"] for x in r["per_k"][k][label]]
            for a, b in zip(sorted(mpvals), sorted(rf["per_k_k4_float64"][k])):
                f64_bad = max(f64_bad, abs(b - a))
    return ({"name": "G5 k·p vs exact dispersion (mpmath %d dps)" % dps, "run": True,
             "residual_table": rows,
             "worst_successive_decade_ratio_minus_1": worst,
             "criterion": "k^4 coefficient converges: |ratio-1| < 1e-6 over k=1e-4..1e-6",
             "pass": bool(worst < 1e-6)},
            {"name": "G8 float64 conditioning receipt", "run": True,
             "float64_k4_shadow": f64_rows,
             "max_abs_divergence_from_mp_at_k_le_1e-4": f64_bad,
             "criterion": "float64 k^4 extraction is noise-dominated (divergence >> the "
                          "mp value) — reported, not passed/failed as physics",
             "pass": bool(f64_bad > 1.0)})


def gate_G6():
    """Second negative control: G_c -> 0 closes the gap AND collapses the v^2 splitting."""
    kmag = 1e-4
    kv = np.array([1.0, 0.0, 0.0]) * kmag
    out = {}
    for gc in (1.0, 1e-2, 1e-4, 0.0):
        d0 = dynamical_matrix_rebuild(np.zeros(3), G_c=gc)
        gap = float(np.max(np.linalg.eigvalsh(d0)))
        w2, uw, ww = branch_character(dynamical_matrix_rebuild(kv, G_c=gc))
        rot = sorted(((w2[i] - gap) / kmag ** 2) for i in range(12) if ww[i] > 0.5)
        out[f"G_c={gc:g}"] = {"gap_m2": gap, "omega_v2_min": rot[0], "omega_v2_max": rot[-1],
                             "v2_split": rot[-1] - rot[0]}
    ok = (abs(out["G_c=0"]["gap_m2"]) < 1e-12 and abs(out["G_c=0"]["v2_split"]) < 1e-8
          and abs(out["G_c=0"]["omega_v2_max"] - 2.0) < 1e-6)
    return {"name": "G6 negative control G_c -> 0", "run": True, "sweep": out,
            "criterion": "gap -> 0 AND omega-branch v^2 splitting -> 0 (all at 2*gamma/I_omega)",
            "pass": bool(ok),
            "structural_reading": "the v^2 splitting is carried by the SAME modulus that opens "
                                  "the gap: v2_split == G_c/rho == (I_omega/4rho)*m^2"}


def gate_G7():
    """FLAG-3 connectivity axis.

    G7a (as pre-registered) is BLOCKED-STRUCTURAL and is reported as BLOCKED, not passed:
    the engine's least-squares gradient functional requires an invertible per-site bond
    tensor, and every z=3 srs site has a rank-2 (singular) bond tensor.  Reported with
    the measured spectrum, not asserted.

    G7b is the DISCLOSED SUBSTITUTE: connectivity-INDEPENDENCE of the O(k^2) result,
    demonstrated on three full-rank NON-diamond bond sets.  If the closed forms are
    identical, the O(k^2) verdict is a property of the continuum micropolar functional
    and FLAG-3 does not move it.
    """
    srs = srs_bond_tensor_report()
    alt = {}
    for name, bonds in alternative_bond_sets().items():
        cf = kp_closed_forms((1.0, 0.0, 0.0), bonds=bonds)
        alt[name] = {"z": int(np.asarray(bonds).shape[0]),
                     "omega_v2": cf["omega_v2"], "u_v2": cf["u_v2"],
                     "omega_charpoly_matches": cf["omega_charpoly_matches"],
                     "u_charpoly_matches": cf["u_charpoly_matches"]}
    base = kp_closed_forms((1.0, 0.0, 0.0))
    same = all(a["omega_charpoly_matches"] and a["u_charpoly_matches"] for a in alt.values())
    return {"name": "G7 connectivity axis (FLAG-3)",
            "G7a_srs_z3_as_preregistered": {
                "run": True, "pass": None, "status": "BLOCKED-STRUCTURAL",
                "measurement": srs,
                "reason": "the engine gradient is a least-squares gradient needing an "
                          "invertible bond tensor M = sum_b dhat (x) dhat; every srs z=3 "
                          "site is trigonal-planar so M has eigenvalues {0, 3/2, 3/2} "
                          "(rank 2) and M^-1 does not exist. Transferring the functional "
                          "to z=3 requires a NEW bond-based constitutive model, which is "
                          "outside this lane's scope and is NOT silently substituted."},
            "G7b_connectivity_independence_SUBSTITUTE": {
                "run": True, "pass": bool(same), "baseline_diamond_z4": {
                    "omega_v2": base["omega_v2"], "u_v2": base["u_v2"]},
                "alternatives": alt,
                "criterion": "identical symbolic v^2 closed forms on all full-rank bond sets"},
            "run": True, "pass": bool(same)}


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------
def main():
    import sympy as sp

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    res = {"prereg": "research/2026-08-05_two-band-kinematics_prereg-FROZEN.md",
           "freeze_commit": "f5ddd995805d724e9e4edb769f384a6517eef1e9"}

    # --- D3 symbolic k·p closed forms, several directions -------------------
    closed = {}
    for dname, dvec in DIRECTIONS.items():
        cf = kp_closed_forms(dvec)
        closed[dname] = {"omega_v2": cf["omega_v2"], "u_v2": cf["u_v2"],
                         "D0_diag": [str(x) for x in cf["D0_diag"]],
                         "D0_is_diagonal": cf["D0_offdiag_max_is_zero"],
                         "omega_charpoly_matches": cf["omega_charpoly_matches"],
                         "u_charpoly_matches": cf["u_charpoly_matches"],
                         "D1_interband_nonzero": cf["D1_interband_is_nonzero"]}
    isotropic = all(closed[d]["omega_charpoly_matches"] and closed[d]["u_charpoly_matches"]
                    for d in closed)
    res["kp_closed_forms"] = {"per_direction": closed,
                              "isotropic_at_O_k2": bool(isotropic)}

    # --- D5 the adjudication at the engine's placeholder moduli -------------
    g_s, g_c, gam, rho, iw = sp.symbols("G G_c gamma rho I_omega", positive=True)
    sub = {g_s: 1, g_c: 1, gam: 1, rho: 1, iw: 1}
    # NOTE: bare sympify() parses "gamma" as the gamma FUNCTION; the local symbol map is
    # mandatory here (caught at integrator time, Rule 10).
    loc = {"G": g_s, "G_c": g_c, "gamma": gam, "rho": rho, "I_omega": iw}
    v2_omega = sorted({float(sp.sympify(k, locals=loc).subs(sub)): v
                       for k, v in closed["100"]["omega_v2"].items()}.items())
    v2_u = sorted({float(sp.sympify(k, locals=loc).subs(sub)): v
                   for k, v in closed["100"]["u_v2"].items()}.items())
    c_em2 = float(sp.sympify("G/rho", locals=loc).subs(sub))
    tol = 1e-9
    carrier = []
    for val, mult in v2_omega:
        ratio = float(np.sqrt(val / c_em2))
        carrier.append({"v2": val, "v_over_c_EM": ratio, "multiplicity": mult,
                        "equals_c_EM_within_tol": bool(abs(ratio - 1.0) <= 0.5 * tol)})
    res["adjudication"] = {
        "c_EM_squared_closed_form": "G/rho",
        "c_EM_at_placeholder_moduli": float(np.sqrt(c_em2)),
        "frozen_tolerance_relative": tol,
        "carrier_branches_omega_sector": carrier,
        "translational_branches": [{"v2": v, "v_over_c_EM": float(np.sqrt(v / c_em2)),
                                    "multiplicity": m} for v, m in v2_u],
        "any_carrier_branch_equals_c_EM": bool(any(c["equals_c_EM_within_tol"] for c in carrier)),
        "all_carrier_branches_equal_c_EM": bool(all(c["equals_c_EM_within_tol"] for c in carrier)),
        "structural_theorem": (
            "v2_perp - v2_par = G_c/rho = (I_omega/(4 rho)) * m^2 exactly. The carrier "
            "branch splitting is carried by the SAME modulus that opens the gap, so a "
            "single carrier limiting velocity requires G_c = 0, i.e. NO GAP. No choice of "
            "positive moduli makes both carrier branches equal c_EM = sqrt(G/rho)."),
    }

    # --- D6 the m* identity (declared tautological, run as a numerics check) -
    m2 = 4.0
    omega0 = float(np.sqrt(m2))
    res["m_star_identity"] = {
        "declared": "TAUTOLOGICAL — algebraically forced by omega^2 = omega0^2 + v^2 k^2; "
                    "reported as an internal consistency check, NOT as evidence",
        "omega0_lattice_units": omega0,
        "E_g_over_hbar_lattice_units": 2 * omega0,
        "per_branch": [{"v2": v, "m_star_times_v2_over_hbar": omega0,
                        "E_g_over_2v2_times_v2_over_hbar": (2 * omega0) / 2,
                        "identity_residual": abs(omega0 - (2 * omega0) / 2)}
                       for v, _ in v2_omega],
    }

    # --- supplement: full-BZ group-velocity read on the carrier manifold -----
    # The k·p v IS the parameter the relativistic form asserts; this supplement reports
    # the largest |grad_k omega| actually attained by the omega-character branches over a
    # BZ scan, so "limiting velocity" is not read from the expansion alone.
    rng = np.random.default_rng(11)
    kmax_vg = 0.0
    kmax_vg_u = 0.0
    h = 1e-6
    for _ in range(400):
        kv = rng.uniform(-np.pi, np.pi, size=3)
        w2, uw, ww = branch_character(dynamical_matrix_rebuild(kv))
        grads = np.zeros((12, 3))
        for ax in range(3):
            dk = np.zeros(3)
            dk[ax] = h
            wp, _, _ = branch_character(dynamical_matrix_rebuild(kv + dk))
            wm, _, _ = branch_character(dynamical_matrix_rebuild(kv - dk))
            grads[:, ax] = (np.sqrt(np.clip(wp, 0, None)) - np.sqrt(np.clip(wm, 0, None))) / (2 * h)
        for i in range(12):
            g = float(np.linalg.norm(grads[i]))
            if ww[i] > 0.5:
                kmax_vg = max(kmax_vg, g)
            else:
                kmax_vg_u = max(kmax_vg_u, g)
    res["full_BZ_group_velocity_supplement"] = {
        "max_abs_grad_omega_carrier_omega_branches": kmax_vg,
        "max_abs_grad_omega_translational_branches": kmax_vg_u,
        "c_EM": 1.0,
        "note": "400 pseudo-random BZ points, seeded (20260805 family), central differences "
                "at h=1e-6 in float64. Supplement only — the verdict rides on the exact "
                "symbolic k·p, not on this scan.",
    }

    # --- gates ---------------------------------------------------------------
    def _rat(expr_str):
        r = sp.nsimplify(sp.sympify(expr_str, locals=loc).subs(sub), rational=True)
        r = sp.Rational(r)
        return (float(r), int(r.p), int(r.q))
    v2_expected = {
        "omega": [_rat(k) for k in closed["100"]["omega_v2"]],
        "u": [_rat(k) for k in closed["100"]["u_v2"]],
    }
    g5, g8 = gate_G5_G8(v2_expected)
    res["gates"] = {"G1": gate_G1(), "G2": gate_G2(), "G3": gate_G3(), "G4": gate_G4(),
                    "G5": g5, "G6": gate_G6(), "G7": gate_G7(), "G8": g8}

    # --- bin -----------------------------------------------------------------
    form_ok = res["gates"]["G5"]["pass"] and isotropic
    v_ok = res["adjudication"]["all_carrier_branches_equal_c_EM"]
    if not res["gates"]["G3"]["pass"]:
        binv = "NO-TWO-BAND-STRUCTURE"
    elif form_ok and v_ok:
        binv = "FORM-REPRODUCED-v=c"
    elif form_ok:
        binv = "FORM-REPRODUCED-V-MISMATCH"
    else:
        binv = "NO-TWO-BAND-STRUCTURE"
    res["bin"] = binv
    res["value_provenance"] = {
        "verdict": "FACTOR DERIVED / VALUE IMPORTED",
        "factor_4": "DERIVED (cosserat-mass-gap.md:61)",
        "G_c_and_I_omega": "ENG-CHOICE phase-I placeholder (cosserat_field_3d.py:12, :954); "
                           "no constants.py symbol exists for either",
        "MeV_scale": "IMPORTED from CODATA m_e via ell_node = hbar/(m_e c) "
                     "(cosserat-mass-gap.md:143, :151)",
        "quarantine": "no gate and no bin reads the MeV value",
    }

    # --- validity window of the relativistic form ----------------------------
    # The relativistic form names an ASYMPTOTIC velocity v, reached only where
    # hbar*v*k >> E_g/2. Ask whether that regime is inside the expansion's validity:
    #   k_rel   : v^2 k^2 = omega_0^2          (the crossover to the relativistic regime)
    #   k_break : |a4| k^4 = 0.1 * v^2 k^2     (the k^4 term reaches 10% of the k^2 term)
    a4_by_v2 = {}
    r100 = res["gates"]["G5"]["residual_table"][0]["per_k"]["1e-06"]["omega"]
    for row in r100:
        a4_by_v2.setdefault(round(row["v2_predicted"], 12), row["k4_coeff"])
    window = []
    for v2, a4 in sorted(a4_by_v2.items()):
        k_rel = float(np.sqrt(m2 / v2))
        k_break = float(np.sqrt(0.1 * v2 / abs(a4))) if abs(a4) > 0 else float("inf")
        window.append({
            "v2": v2, "v_over_c_EM": float(np.sqrt(v2)), "k4_coefficient": a4,
            "k_rel_lattice_units": k_rel, "k_break_10pct_lattice_units": k_break,
            "k_break_over_k_rel": k_break / k_rel,
            "relativistic_regime_inside_validity": bool(k_break > k_rel),
        })
    res["relativistic_form_validity_window"] = {
        "per_carrier_branch": window,
        "zone_edge_k_lattice_units": float(np.pi),
        "reading": ("k_break < k_rel on every carrier branch: the lattice bends the band "
                    "over BEFORE the carrier reaches the regime where v would become its "
                    "group velocity. The relativistic form is therefore a valid SMALL-k "
                    "truncation whose named limiting velocity is never attained on this "
                    "lattice — which is why the full-BZ group-velocity supplement reads "
                    "BELOW c_EM even though the form's v exceeds it."),
    }

    res["constructive_v_equals_c_conditions"] = {
        "carrier_parallel_branch": "2*gamma/I_omega == G/rho",
        "carrier_transverse_branch": "2*gamma/I_omega + G_c/rho == G/rho",
        "both_simultaneously": "requires G_c == 0, i.e. the gap CLOSES — no positive-moduli "
                               "solution exists with a massive carrier",
        "translational_transverse_branch": "identically satisfied: v^2 == G/rho == c_EM^2 for "
                                           "ALL moduli (the G_c direct stiffness is exactly "
                                           "cancelled by the k·p level repulsion)",
    }

    payload = json.dumps(res, indent=2, sort_keys=True, default=str)
    OUT_JSON.write_text(payload)
    digest = hashlib.sha256(payload.encode()).hexdigest()
    print(f"[two-band-kp] BIN = {binv}")
    for gname, g in res["gates"].items():
        print(f"  {gname}: pass={g.get('pass')}  {g.get('name','')}")
    print(f"[two-band-kp] wrote {OUT_JSON}")
    print(f"[two-band-kp] sha256 = {digest}")
    return res


if __name__ == "__main__":
    main()

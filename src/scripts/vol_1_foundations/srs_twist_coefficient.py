#!/usr/bin/env python3
"""The srs COMPRESSION->TWIST coefficient + the L-C lockstep adjudication.

Grant ruling 2026-08-05 ("1 and 2, go"). Prereg (FROZEN):
research/2026-08-05_srs-twist-coefficient_prereg-FROZEN.md.
Ruling record: _orchestration/docket-entries/2026-08-05-ruling-squeeze-twist.md.

===============================================================================
SUBSTRATE-FIRST SECTOR HEADER (stated before any standard-physics word)
===============================================================================
  SECTOR : A1 translational (dilatation) = the CAPACITIVE C-side load;
           Cosserat micro-rotational phi / wryness kappa = the INDUCTIVE L-side
           response. Ownership per translation-circuit.md:35. NOT the Cosserat
           (2,3) winding charge; NOT the Axiom-4 "T2 bow" coordinate
           (axiom-register.md:193 homonym guard).
  REGIME : STATIC. Cold linear, sub-yield, saturation OFF (S(A)=1). Small-signal
           about the cold bias point. Near-yield entered ONLY via the canon-forced
           swapped-spring rho_eff = rho_cold*(S_axial/S_shear), MODEL SCOPE
           inherited (pre-stress + bias geometry change OMITTED).
  COORDS : real-space / spatial-Brillouin (A46). The claim under test is a
           real-space mechanical statement; readouts phi_bar/eps and kappa/eps are
           real-space. Coordinates match.
  CLASS  : CONSISTENCY / DC-internal. alpha-CLEAN: every headline is a
           dimensionless ratio in units of k_s and a_cell. No CODATA, no SI
           substitution, no Q_TANK on any verdict path.
  LEDGER : entirely RIM (lossless static elastic-energy minimisation on a closed
           periodic cell). No port, no radiation, no detector. No loss word.

METHOD. Direct stiffness assembly under PBC on the D1-ratified chiral srs-z3
carrier (chiral_lattice.build_srs_net, carrier="srs-z3"). Per node 6 DOF (u,phi)
per Axiom 1. The per-bond 6x6 blocks are IMPORTED from the certified
ave.core.micropolar_bloch.bond_6dof_block (Rule-14 anti-rebuild) -- what this
driver adds is the STATIC load path that module does not have:

  LOAD PATH A (k=0 affine squeeze): u_n = H.r_n + utilde_n, phi_n = phitilde_n;
    minimise the cell energy over the cell-periodic internals. Readouts: the net
    micro-rotation phi_bar (the macroscopic twist) and the internal-only rms
    (an internal-strain pattern, reported SEPARATELY and never summed).

  LOAD PATH B (finite-q gradient squeeze): Bloch-phased K(q); the full uniform-
    translation TRIPLET is clamped (the prescribed macroscopic displacement) and
    every optical + rotational DOF relaxes. Readout: kappa/eps = Phi/A and the
    dimensionless c_twist = (kappa/eps)/q.

Run: PYTHONPATH=src python3 src/scripts/vol_1_foundations/srs_twist_coefficient.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core.constants import ELL_C, L_NODE
from ave.core.micropolar_bloch import bond_6dof_block, micropolar_phi

# ---------------------------------------------------------------------------
# CANON-PINNED INPUTS (provenance table = prereg SVA row 5)
# ---------------------------------------------------------------------------
LEVER_GEOM = 1.0          # bond-midpoint attachment, geometry-fixed (micropolar_bloch.py:77-87)
GAMMA_OVER_KS = 6.0       # ell_c^2 = gamma/G = 6  (constants.py:338, ELL_C = sqrt(6)*L_NODE)
RHO_MATCH = 1.0           # Ax-3 zero-reflection match point (clm-mfb2ax); K<0 here -- see G8
RHO_K2G = 9.7734          # GR-imported K=2G point (PR #506/#261)

# Stage-1 certified regression targets (2026-07-04_srs-elastic-tensor_result.md
# section 1 + the #506 table with the docket 2026-08-02 arithmetic correction).
STAGE1_C11 = 0.72786
STAGE1_C44 = 0.24876
STAGE1_K = 0.458052       # (C11+2*C12)/3 at rho* -- docket-corrected value
STAGE1_ZENER = 1.2293


# ---------------------------------------------------------------------------
# section 1 -- nets and bond lists
# ---------------------------------------------------------------------------
def srs_cell(enantiomorph: str = "right"):
    """One srs unit cell (8 Wyckoff-8a nodes) + bidirectional bond list.

    Returns (pos, bonds, a_cell). `bonds` = list of directed (i, j, d) with d the
    minimum-image displacement -- the SAME tuple convention Stage-1/Stage-2 use.
    """
    net = cl.build_srs_net(1, enantiomorph)
    assert net.carrier == "srs-z3", f"carrier drift: {net.carrier}"
    a = float(net.box)
    pos = net.pos.copy()
    bonds = []
    for i in range(net.n_nodes):
        for j in net.neighbors[i]:
            d = pos[j] - pos[i]
            d -= a * np.round(d / a)
            bonds.append((i, j, d))
    return pos, bonds, a


def diamond_cell():
    """The achiral z=4 diamond CONTROL instrument (D1: non-canonical instrument)."""
    net = cl.build_diamond_net(4)
    a = float(net.box)
    pos = net.pos.copy()
    bonds = []
    for i in range(net.n_nodes):
        for j in net.neighbors[i]:
            d = pos[j] - pos[i]
            d -= a * np.round(d / a)
            bonds.append((i, j, d))
    return pos, bonds, a


# ---------------------------------------------------------------------------
# section 2 -- static assembly: stiffness, affine force, relaxation
# ---------------------------------------------------------------------------
def stiffness_k0(pos, bonds, *, k_a, k_s, gamma, lever):
    """The k=0 6N x 6N Hessian of the total cell energy (real, symmetric).

    micropolar_phi with the bidirectional bond list stamps exactly the total-energy
    Hessian once: listing (i,j,d) supplies the (i,i) and (i,j) blocks, listing
    (j,i,-d) supplies (j,j) and (j,i). Verified by G0 (finite-difference).
    """
    K = micropolar_phi(np.zeros(3), pos, bonds, k_axial=k_a, k_shear=k_s,
                       gamma=gamma, kappa_rot=0.0, lever=lever, reading="a")
    K = np.real(K)
    return 0.5 * (K + K.T)


def affine_force(pos, bonds, H, *, k_a, k_s, gamma, lever):
    """f = dE/dx at x=0 for the affine macroscopic load H (6N vector).

    For each DIRECTED listing (i,j,d) the i-endpoint term is  -J_i^T Phi_b (H.d);
    the reverse listing supplies the j-endpoint term, so iterating all directed
    listings and adding only the i-endpoint contribution is exact and PBC-safe
    (it never needs an i<j ordering, which self-bonds through PBC would break).
    """
    n = len(pos)
    f = np.zeros(6 * n)
    for (i, j, d) in bonds:
        d = np.asarray(d, float)
        dn = d / np.linalg.norm(d)
        P = np.outer(dn, dn)
        Phi_b = k_a * P + k_s * (np.eye(3) - P)
        b_i = +0.5 * lever * d
        Bi = np.array([[0.0, -b_i[2], b_i[1]],
                       [b_i[2], 0.0, -b_i[0]],
                       [-b_i[1], b_i[0], 0.0]])
        Ji = np.hstack([np.eye(3), -Bi])          # 3x6
        f[6 * i:6 * i + 6] += -Ji.T @ (Phi_b @ (H @ d))
    return f


def affine_energy0(pos, bonds, H, *, k_a, k_s, lever):
    """E at zero internal relaxation (the affine-only energy), for the C_ij path."""
    E = 0.0
    for (i, j, d) in bonds:
        d = np.asarray(d, float)
        dn = d / np.linalg.norm(d)
        P = np.outer(dn, dn)
        Phi_b = k_a * P + k_s * (np.eye(3) - P)
        Dl = H @ d
        E += 0.5 * (Dl @ (Phi_b @ Dl))
    return 0.5 * E   # each undirected bond is listed twice


def _complement_basis(clamp, N, dtype=float):
    """Orthonormal basis (N x (N-m)) of the orthogonal complement of `clamp` rows."""
    if clamp is None or len(clamp) == 0:
        return np.eye(N, dtype=dtype)
    C = np.atleast_2d(np.asarray(clamp, dtype)).T          # (N, m)
    Qf, _ = np.linalg.qr(C, mode="complete")               # (N, N)
    m = int(np.linalg.matrix_rank(C))
    return Qf[:, m:]


def relax(K, f, *, null_tol=1e-9, clamp=None):
    """Minimise 1/2 x'Kx + Re(x'f) on the complement of `clamp` and of K's nullspace.

    Returns (x, info). `clamp` = optional (m, N) array of directions held at zero
    (load path B holds the macroscopic uniform-translation triplet). Never inverts
    a rank-deficient matrix: the solve happens on an explicit orthonormal basis of
    the admissible subspace (prereg SVA row 11a).
    """
    N = K.shape[0]
    cx = np.iscomplexobj(K) or np.iscomplexobj(f)
    B = _complement_basis(clamp, N, dtype=complex if cx else float)
    Kb = B.conj().T @ K @ B
    Kb = 0.5 * (Kb + Kb.conj().T)
    w, U = np.linalg.eigh(Kb)
    scale = max(1.0, float(np.max(np.abs(w))))
    keep = np.abs(w) > null_tol * scale
    nullity = int(np.sum(~keep))
    Q = B @ U[:, keep]
    Kr = Q.conj().T @ K @ Q
    Kr = 0.5 * (Kr + Kr.conj().T)
    fr = Q.conj().T @ f
    x = Q @ np.linalg.solve(Kr, -fr)
    ev = np.linalg.eigvalsh(Kr)
    info = {
        "nullity_after_clamp": nullity,
        "cond": float(np.max(np.abs(ev)) / max(float(np.min(np.abs(ev))), 1e-300)),
        "min_eig_reduced": float(np.min(ev)),
        "max_eig_reduced": float(np.max(ev)),
        "indefinite": bool(np.min(ev) < 0.0),
        "residual": float(np.linalg.norm(Q.conj().T @ (K @ x + f))),
    }
    return x, info


def load_path_A(pos, bonds, H, *, k_a, k_s, gamma, lever):
    """k=0 affine squeeze. Returns the relaxed internals + the twist readouts."""
    n = len(pos)
    K = stiffness_k0(pos, bonds, k_a=k_a, k_s=k_s, gamma=gamma, lever=lever)
    f = affine_force(pos, bonds, H, k_a=k_a, k_s=k_s, gamma=gamma, lever=lever)
    x, info = relax(K, f)
    u = x.reshape(n, 6)[:, :3]
    phi = x.reshape(n, 6)[:, 3:]
    return {
        "phi_bar": phi.mean(axis=0),
        "phi_rms": float(np.sqrt(np.mean(np.sum(phi * phi, axis=1)))),
        "u_rms": float(np.sqrt(np.mean(np.sum(u * u, axis=1)))),
        "E_relaxed": float(0.5 * x @ (K @ x) + x @ f),
        **info,
    }


def total_energy(pos, bonds, H, x, *, k_a, k_s, gamma, lever):
    """Exact total cell energy for macroscopic H plus internal DOF vector x (6N)."""
    n = len(pos)
    q = np.asarray(x, float).reshape(n, 6)
    u, ph = q[:, :3], q[:, 3:]
    E = 0.0
    for (i, j, d) in bonds:
        d = np.asarray(d, float)
        dn = d / np.linalg.norm(d)
        P = np.outer(dn, dn)
        Phi_b = k_a * P + k_s * (np.eye(3) - P)
        b_i, b_j = +0.5 * lever * d, -0.5 * lever * d
        Delta = (H @ d) + (u[j] - u[i]) + np.cross(ph[j], b_j) - np.cross(ph[i], b_i)
        dphi = ph[j] - ph[i]
        E += 0.5 * (Delta @ (Phi_b @ Delta)) + 0.5 * gamma * (dphi @ dphi)
    return 0.5 * E   # each undirected bond appears twice in the directed listing


# ---------------------------------------------------------------------------
# section 3 -- load path B: the finite-q gradient squeeze
# ---------------------------------------------------------------------------
def _uniform_vec(n, slot):
    """6n-vector that is 1 in DOF `slot` (0..5) at every node."""
    v = np.zeros(6 * n)
    v[slot::6] = 1.0
    return v


def _sumzero_basis(n):
    """EXACT integer basis of {clamp-free} = (u with zero net translation) + (all phi).

    Columns: for each Cartesian a, the n-1 differences e_{6k+a} - e_{6(k+1)+a};
    plus every phi DOF. Dimension 3(n-1) + 3n = 6n-3. Integer entries -> mp-safe.
    """
    cols = []
    for a in range(3):
        for k in range(n - 1):
            v = np.zeros(6 * n)
            v[6 * k + a] = 1.0
            v[6 * (k + 1) + a] = -1.0
            cols.append(v)
    for k in range(n):
        for a in range(3):
            v = np.zeros(6 * n)
            v[6 * k + 3 + a] = 1.0
            cols.append(v)
    return np.array(cols).T                     # (6n, 6n-3)


def load_path_B(pos, bonds, qvec, ehat, *, k_a, k_s, gamma, lever, mp_dps=0):
    """Bloch static response to a clamped macroscopic longitudinal displacement wave.

    Drive: psi = A*T_ehat (A=1) -- the uniform-translation triplet is CLAMPED.
    Free : every optical translation + every micro-rotation, relaxed.
    Read : Phi = mean micro-rotation about ehat;  kappa/eps = Phi/A;
           c_twist = (kappa/eps)/q  (dimensionless).
    """
    n = len(pos)
    ehat = np.asarray(ehat, float)
    ehat = ehat / np.linalg.norm(ehat)
    qvec = np.asarray(qvec, float)
    qmag = float(np.linalg.norm(qvec))

    K = micropolar_phi(qvec, pos, bonds, k_axial=k_a, k_shear=k_s, gamma=gamma,
                       kappa_rot=0.0, lever=lever, reading="a")
    K = 0.5 * (K + K.conj().T)

    T = sum(ehat[a] * _uniform_vec(n, a) for a in range(3))      # drive direction
    B = _sumzero_basis(n).astype(complex)
    Kb = B.conj().T @ K @ B
    fb = B.conj().T @ (K @ T)                                    # A = 1
    # MIN-NORM LEAST SQUARES, not a direct inverse. Identical (bit-level, verified by
    # the G6b receipt) on every non-singular configuration; the ONLY configurations it
    # changes are the ones where the phi sector DECOUPLES exactly (k_s=0, the G6
    # mechanism null), where a direct solve returns amplified round-off instead of the
    # exact zero-force answer. Disclosed method change, made on a NEGATIVE CONTROL.
    y, _res, rank, sv_ls = np.linalg.lstsq(Kb, -fb, rcond=None)
    psi_f = B @ y

    R = sum(ehat[a] * _uniform_vec(n, 3 + a) for a in range(3))  # uniform-rotation reader
    Phi = complex(R @ psi_f) / n
    kappa_over_eps = Phi                                          # A = 1
    c_twist = Phi / qmag

    sv = np.linalg.svd(Kb, compute_uv=False)
    # SIGNED second-order coefficient: kappa/eps = c2 * q^2  (c2 has units of length).
    # The response to a longitudinal drive is REAL (Phi = q^2 B/alpha), so Phi.real
    # carries the chirality sign and Phi.imag is the numerical-zero control.
    c2 = Phi.real / (qmag ** 2)
    out = {
        "q": qmag,
        "Phi_re": float(Phi.real), "Phi_im": float(Phi.imag),
        "abs_kappa_over_eps": float(abs(kappa_over_eps)),
        "c2_signed": float(c2),
        "c2_imag_control": float(Phi.imag / (qmag ** 2)),
        "c_twist_re": float(c_twist.real), "c_twist_im": float(c_twist.imag),
        "abs_c_twist": float(abs(c_twist)),
        "cond_Kb": float(sv.max() / max(sv.min(), 1e-300)),
        "smallest_sv": float(sv.min()), "lstsq_rank": int(rank), "dim_Kb": int(Kb.shape[0]),
        "residual": float(np.linalg.norm(Kb @ y + fb)),
    }
    if mp_dps:
        from mpmath import mp, mpc, matrix, lu_solve
        mp.dps = mp_dps
        m = Kb.shape[0]
        Km = matrix(m, m)
        fm = matrix(m, 1)
        for r in range(m):
            fm[r] = mpc(fb[r].real, fb[r].imag)
            for c in range(m):
                Km[r, c] = mpc(Kb[r, c].real, Kb[r, c].imag)
        ym = lu_solve(Km, -fm)
        psi_mp = B @ np.array([complex(ym[r]) for r in range(m)])
        Phi_mp = complex(R @ psi_mp) / n
        out["mp_dps"] = mp_dps
        out["abs_c_twist_mp"] = float(abs(Phi_mp / qmag))
        out["c2_signed_mp"] = float(Phi_mp.real / (qmag ** 2))
        out["mp_vs_f64_rel"] = float(abs(abs(Phi_mp) - abs(Phi)) / max(abs(Phi), 1e-300))
    return out


# ---------------------------------------------------------------------------
# section 4 -- the relaxed Cauchy tensor (G2 regression on a certified predecessor)
# ---------------------------------------------------------------------------
def cauchy_Cij(pos, bonds, a_cell, *, k_a, k_s, eps=1e-3):
    """Relaxed C11/C12/C44 from the STATIC affine machinery (phi clamped, lever=0)."""
    n = len(pos)
    V = a_cell ** 3
    K = stiffness_k0(pos, bonds, k_a=k_a, k_s=k_s, gamma=0.0, lever=0.0)
    # clamp every phi DOF (Cauchy-grade: rotations frozen out)
    clamp = [np.eye(6 * n)[6 * k + 3 + a] for k in range(n) for a in range(3)]

    def W(H):
        f = affine_force(pos, bonds, H, k_a=k_a, k_s=k_s, gamma=0.0, lever=0.0)
        x, _ = relax(K, f, clamp=clamp)
        E = affine_energy0(pos, bonds, H, k_a=k_a, k_s=k_s, lever=0.0)
        return (E + 0.5 * x @ (K @ x) + x @ f) / V

    H1 = np.diag([eps, 0.0, 0.0])
    H2 = np.diag([eps, eps, 0.0])
    H4 = np.zeros((3, 3)); H4[1, 2] = H4[2, 1] = eps
    C11 = 2.0 * W(H1) / eps ** 2
    C12 = W(H2) / eps ** 2 - C11
    C44 = W(H4) / (2.0 * eps ** 2)
    zener = 2.0 * C44 / (C11 - C12)
    return {"C11": float(C11), "C12": float(C12), "C44": float(C44),
            "K_bulk": float((C11 + 2 * C12) / 3.0), "Zener_A": float(zener),
            "C44_over_C11": float(C44 / C11), "C12_over_C11": float(C12 / C11)}


# ---------------------------------------------------------------------------
# section 5 -- GATES (frozen in the prereg; UNRUN != PASSED)
# ---------------------------------------------------------------------------
def gate_G1(pos, bonds, a_cell):
    """Carrier + bond-list rebuild; plus a Hessian-vs-energy finite-difference
    sub-check (ADDED rigor -- no frozen criterion dropped)."""
    n = len(pos)
    deg = np.zeros(n, int)
    for (i, j, d) in bonds:
        deg[i] += 1
    nn = np.array([np.linalg.norm(d) for (_, _, d) in bonds])
    net4 = cl.build_srs_net(4, "right")
    _, _, _, (lmin, lmax) = cl.net_ring_writhe(net4, n_sample=24)
    # FD check of the k=0 Hessian against the exact energy
    rng = np.random.default_rng(20260805)
    x = rng.normal(size=6 * n) * 1e-4
    K = stiffness_k0(pos, bonds, k_a=1.3, k_s=1.0, gamma=6.0, lever=1.0)
    E_quad = 0.5 * x @ (K @ x)
    E_exact = total_energy(pos, bonds, np.zeros((3, 3)), x,
                           k_a=1.3, k_s=1.0, gamma=6.0, lever=1.0)
    rel = abs(E_quad - E_exact) / max(abs(E_exact), 1e-300)
    ok = (n == 8 and deg.min() == 3 and deg.max() == 3
          and abs(nn.max() - nn.min()) < 1e-12
          and abs(nn.mean() - a_cell * np.sqrt(2) / 4) < 1e-12
          and lmin == 10 and rel < 1e-12)
    return {"gate": "G1", "pass": bool(ok), "n_nodes": int(n),
            "degree_min": int(deg.min()), "degree_max": int(deg.max()),
            "nn_bond": float(nn.mean()), "nn_expected": float(a_cell * np.sqrt(2) / 4),
            "girth_L4": int(lmin), "ring_len_max_L4": int(lmax),
            "hessian_vs_energy_rel": float(rel)}


def acoustic_gamma(pos, bonds, a_cell, qhat, *, k_a, k_s, eps=1e-3):
    """Gamma_ik(qhat) from the FULL (unsymmetrised) displacement-gradient Hessian.

    This is the acoustic-slope reading Stage-1 used. It differs from the
    symmetric-strain elastic tensor whenever the bond model carries absolute-frame
    rotational stiffness -- exactly the standing FLAG-4 axis
    (_orchestration/docket-entries/2026-08-02-biased-tensor-scoping.md:8). Reported
    as a KEEP-BOTH companion; the frozen G2 comparison is NOT rewritten.
    """
    n = len(pos)
    V = a_cell ** 3
    K = stiffness_k0(pos, bonds, k_a=k_a, k_s=k_s, gamma=0.0, lever=0.0)
    clamp = [np.eye(6 * n)[6 * k + 3 + a] for k in range(n) for a in range(3)]

    def W(H):
        f = affine_force(pos, bonds, H, k_a=k_a, k_s=k_s, gamma=0.0, lever=0.0)
        x, _ = relax(K, f, clamp=clamp)
        E = affine_energy0(pos, bonds, H, k_a=k_a, k_s=k_s, lever=0.0)
        return (E + 0.5 * x @ (K @ x) + x @ f) / V

    qhat = np.asarray(qhat, float); qhat = qhat / np.linalg.norm(qhat)
    G = np.zeros((3, 3))
    for i in range(3):
        for k in range(3):
            Hi = eps * np.outer(np.eye(3)[i], qhat)
            Hk = eps * np.outer(np.eye(3)[k], qhat)
            G[i, k] = (W(Hi + Hk) - W(Hi) - W(Hk)) / eps ** 2
            if i == k:
                G[i, k] = 2.0 * W(Hi) / eps ** 2
    return 0.5 * (G + G.T)


def gate_G2(pos, bonds, a_cell):
    """Stage-1 regression: relaxed Cauchy C_ij at rho* = 9.7734 (phi clamped)."""
    C = cauchy_Cij(pos, bonds, a_cell, k_a=RHO_K2G, k_s=1.0)
    tgt_c44_c11 = STAGE1_C44 / STAGE1_C11
    tgt_c12_c11 = ((3.0 * STAGE1_K - STAGE1_C11) / 2.0) / STAGE1_C11
    d1 = abs(C["C44_over_C11"] - tgt_c44_c11) / tgt_c44_c11
    d2 = abs(C["C12_over_C11"] - tgt_c12_c11) / tgt_c12_c11
    d3 = abs(C["Zener_A"] - STAGE1_ZENER) / STAGE1_ZENER
    scale = C["C11"] / STAGE1_C11
    Gm = acoustic_gamma(pos, bonds, a_cell, [0.0, 0.0, 1.0], k_a=RHO_K2G, k_s=1.0)
    ev = np.sort(np.linalg.eigvalsh(Gm))
    acoustic = {"Gamma_100_zz_longitudinal": float(Gm[2, 2]),
                "Gamma_100_transverse_eigs": [float(ev[0]), float(ev[1])],
                "stage1_C11": STAGE1_C11, "stage1_C44": STAGE1_C44,
                "rel_dev_longitudinal": float(abs(Gm[2, 2] - STAGE1_C11) / STAGE1_C11),
                "rel_dev_transverse": float(abs(ev[0] - STAGE1_C44) / STAGE1_C44)}
    return {"gate": "G2", "pass": bool(max(d1, d2, d3) < 1e-4), **C,
            "KEEPBOTH_acoustic_reading": acoustic,
            "target_C44_over_C11": float(tgt_c44_c11),
            "target_C12_over_C11": float(tgt_c12_c11),
            "rel_dev_C44_over_C11": float(d1), "rel_dev_C12_over_C11": float(d2),
            "rel_dev_Zener": float(d3),
            "abs_normalisation_ratio_C11": float(scale)}


def gate_G3(pos, bonds):
    """Objectivity: the global rigid rotation is a zero mode iff lever == 1."""
    n = len(pos)
    theta = np.array([0.3, -0.7, 0.45]) * 1e-3
    Hrot = np.array([[0.0, -theta[2], theta[1]],
                     [theta[2], 0.0, -theta[0]],
                     [-theta[1], theta[0], 0.0]])
    x = np.zeros(6 * n)
    for k in range(n):
        x[6 * k + 3:6 * k + 6] = theta
    out = {}
    for lev in (1.0, 0.5, 2.0, 0.0):
        out[f"E_rigid_lever_{lev}"] = float(
            total_energy(pos, bonds, Hrot, x, k_a=1.0, k_s=1.0, gamma=6.0, lever=lev))
    ok = abs(out["E_rigid_lever_1.0"]) < 1e-20 and out["E_rigid_lever_0.0"] > 0.0
    return {"gate": "G3", "pass": bool(ok), **out,
            "objective_at_lever1": bool(abs(out["E_rigid_lever_1.0"]) < 1e-20)}


def gate_G4(pos, bonds):
    """Rotational gap: is a uniform phi (u=0, H=0) a zero mode of the k=0 stiffness?"""
    n = len(pos)
    res = {}
    for lev in (1.0, 0.0):
        K = stiffness_k0(pos, bonds, k_a=1.0, k_s=1.0, gamma=6.0, lever=lev)
        e = 0.0
        for a in range(3):
            v = _uniform_vec(n, 3 + a)
            e = max(e, float(v @ (K @ v)) / float(v @ v))
        res[f"rayleigh_uniform_phi_lever_{lev}"] = e
    gapped = res["rayleigh_uniform_phi_lever_1.0"] > 1e-12
    return {"gate": "G4", "pass": True, **res,
            "verdict": "GAPPED" if gapped else "GAPLESS",
            "contradicts_micropolar_bloch_docstring": bool(gapped)}


def gate_G7(pos, bonds, a_cell):
    """(a) srs site central tensor spectrum {0, 1.5, 1.5}; (b) reduced nullity == 3."""
    n = len(pos)
    site = np.zeros((3, 3))
    cnt = 0
    for (i, j, d) in bonds:
        if i == 0:
            dn = np.asarray(d, float) / np.linalg.norm(d)
            site += np.outer(dn, dn)
            cnt += 1
    spec_central = np.sort(np.linalg.eigvalsh(site))
    site_born = np.zeros((3, 3))
    for (i, j, d) in bonds:
        if i == 0:
            dn = np.asarray(d, float) / np.linalg.norm(d)
            P = np.outer(dn, dn)
            site_born += 1.0 * P + 1.0 * (np.eye(3) - P)
    spec_born = np.sort(np.linalg.eigvalsh(site_born))
    K = stiffness_k0(pos, bonds, k_a=1.0, k_s=1.0, gamma=6.0, lever=1.0)
    w = np.linalg.eigvalsh(K)
    nullity = int(np.sum(np.abs(w) <= 1e-9 * max(1.0, np.abs(w).max())))
    a_ok = (abs(spec_central[0]) < 1e-12 and abs(spec_central[1] - 1.5) < 1e-12
            and abs(spec_central[2] - 1.5) < 1e-12)
    b_ok = (nullity == 3)
    return {"gate": "G7", "pass": bool(a_ok and b_ok), "bonds_at_site0": cnt,
            "central_site_spectrum": [float(v) for v in spec_central],
            "born_site_spectrum_rank3": [float(v) for v in spec_born],
            "central_rank": int(np.sum(spec_central > 1e-12)),
            "born_rank": int(np.sum(spec_born > 1e-12)),
            "global_nullity_lever1": nullity,
            "a_pass": bool(a_ok), "b_pass_STOP_GATE": bool(b_ok)}


# ---------------------------------------------------------------------------
# section 6 -- measurements
# ---------------------------------------------------------------------------
LOADS = {
    "A-ISO   (hydrostatic squeeze)": -np.eye(3),
    "A-UNI001 (uniaxial [001])": -np.diag([0.0, 0.0, 1.0]),
    "A-UNI111 (uniaxial [111])": -np.outer([1, 1, 1], [1, 1, 1]) / 3.0,
}


def measure_A(pos, bonds, *, k_a, k_s, gamma, lever, eps=1e-3):
    rows = []
    for name, Hdir in LOADS.items():
        r = load_path_A(pos, bonds, eps * Hdir, k_a=k_a, k_s=k_s, gamma=gamma, lever=lever)
        pb = r["phi_bar"]
        rows.append({
            "load": name,
            "tau_net_twist_per_strain": float(np.linalg.norm(pb) / eps),
            "phi_bar": [float(v) for v in pb],
            "tau_rms_internal_per_strain": float(r["phi_rms"] / eps),
            "u_rms_per_strain": float(r["u_rms"] / eps),
            "nullity_after_clamp": r["nullity_after_clamp"],
            "cond": r["cond"], "indefinite": r["indefinite"],
            "min_eig_reduced": r["min_eig_reduced"], "residual": r["residual"],
        })
    return rows


def measure_B(pos, bonds, a_cell, *, k_a, k_s, gamma, lever, dirs=None, mp_at=None):
    dirs = dirs or {"[001]": np.array([0.0, 0.0, 1.0]),
                    "[111]": np.array([1.0, 1.0, 1.0]),
                    "[110]": np.array([1.0, 1.0, 0.0])}
    rows = []
    for dname, e in dirs.items():
        e = e / np.linalg.norm(e)
        for expo in range(1, 8):
            qm = 10.0 ** (-expo) * (2.0 * np.pi / a_cell)
            dps = 60 if (mp_at and dname == mp_at and expo in (1, 4, 7)) else 0
            r = load_path_B(pos, bonds, qm * e, e, k_a=k_a, k_s=k_s,
                            gamma=gamma, lever=lever, mp_dps=dps)
            r["direction"] = dname
            r["q_over_2pi_a"] = float(qm * a_cell / (2 * np.pi))
            rows.append(r)
    return rows


def fit_power(rows, key="abs_kappa_over_eps"):
    """Leading power of q in `key` (fitted, not assumed), from the smallest-q decade pair."""
    r = sorted(rows, key=lambda z: z["q"])
    a, b = r[0], r[1]
    if a[key] <= 0 or b[key] <= 0:
        return None
    return float(np.log(b[key] / a[key]) / np.log(b["q"] / a["q"]))


def main():
    out = {"meta": {
        "driver": "src/scripts/vol_1_foundations/srs_twist_coefficient.py",
        "prereg": "research/2026-08-05_srs-twist-coefficient_prereg-FROZEN.md",
        "carrier": "srs-z3 (D1-ratified)", "lever": LEVER_GEOM,
        "gamma_over_ks": GAMMA_OVER_KS,
        "ELL_C_over_L_NODE": float(ELL_C / L_NODE),
        "regime": "STATIC, cold linear, sub-yield, saturation OFF",
    }}

    posR, bondsR, a = srs_cell("right")
    posL, bondsL, _ = srs_cell("left")
    g = GAMMA_OVER_KS

    # ---- gates, negative controls FIRST (frozen ordering) -------------------
    posD, bondsD, aD = diamond_cell()
    g5 = {"gate": "G5", "diamond_A": measure_A(posD, bondsD, k_a=1.0, k_s=1.0,
                                               gamma=g, lever=LEVER_GEOM),
          "diamond_B": measure_B(posD, bondsD, aD, k_a=1.0, k_s=1.0, gamma=g,
                                 lever=LEVER_GEOM,
                                 dirs={"[001]": np.array([0.0, 0.0, 1.0])})}
    g5["max_abs_c_twist"] = max(r["abs_c_twist"] for r in g5["diamond_B"])
    g5["KEEPBOTH_max_abs_kappa_over_eps"] = max(r["abs_kappa_over_eps"] for r in g5["diamond_B"])
    g5["KEEPBOTH_max_abs_c2"] = max(abs(r["c2_signed"]) for r in g5["diamond_B"])
    g5["max_tau"] = max(r["tau_net_twist_per_strain"] for r in g5["diamond_A"])
    g5["pass"] = bool(g5["max_abs_c_twist"] < 1e-12 and g5["max_tau"] < 1e-12)

    g6 = {"gate": "G6", "srs_ks0_B": measure_B(posR, bondsR, a, k_a=1.0, k_s=0.0,
                                               gamma=g, lever=LEVER_GEOM,
                                               dirs={"[001]": np.array([0.0, 0.0, 1.0])})}
    g6["max_abs_c_twist"] = max(r["abs_c_twist"] for r in g6["srs_ks0_B"])
    g6["KEEPBOTH_max_abs_kappa_over_eps"] = max(r["abs_kappa_over_eps"] for r in g6["srs_ks0_B"])
    g6["KEEPBOTH_max_abs_c2"] = max(abs(r["c2_signed"]) for r in g6["srs_ks0_B"])
    g6["KEEPBOTH_note"] = ("the frozen threshold is on c_twist=|kappa/eps|/q, which "
                           "DIVIDES a round-off floor by q and therefore diverges on a "
                           "true null; the mechanism observable is kappa/eps (and c2)")
    # matched-q comparison at the BEST-CONDITIONED q (largest), k_s=0 vs k_s=1
    q0 = max(r["q"] for r in g6["srs_ks0_B"])
    n0 = [r for r in g6["srs_ks0_B"] if r["q"] == q0][0]["abs_kappa_over_eps"]
    ref = load_path_B(posR, bondsR, q0 * np.array([0.0, 0.0, 1.0]),
                      np.array([0.0, 0.0, 1.0]), k_a=1.0, k_s=1.0, gamma=g,
                      lever=LEVER_GEOM)["abs_kappa_over_eps"]
    g6["KEEPBOTH_matched_q"] = {"q": float(q0), "ks0_kappa_over_eps": float(n0),
                                "ks1_kappa_over_eps": float(ref),
                                "suppression_OOM": float(np.log10(max(ref, 1e-300) / max(n0, 1e-300)))}
    g6["pass"] = bool(g6["max_abs_c_twist"] < 1e-12)

    out["gates"] = [gate_G1(posR, bondsR, a), gate_G2(posR, bondsR, a),
                    gate_G3(posR, bondsR), gate_G4(posR, bondsR),
                    g5, g6, gate_G7(posR, bondsR, a)]

    # ---- measurements -------------------------------------------------------
    out["load_path_A"] = {}
    for rho, tag in ((RHO_MATCH, "rho_bond=1 (Ax-3 match point)"),
                     (RHO_K2G, "rho*=9.7734 (K=2G, GR-imported)")):
        out["load_path_A"][tag] = {
            "right": measure_A(posR, bondsR, k_a=rho, k_s=1.0, gamma=g, lever=LEVER_GEOM),
            "left": measure_A(posL, bondsL, k_a=rho, k_s=1.0, gamma=g, lever=LEVER_GEOM),
        }

    out["load_path_B"] = {}
    for rho, tag in ((RHO_MATCH, "rho_bond=1 (Ax-3 match point)"),
                     (RHO_K2G, "rho*=9.7734 (K=2G, GR-imported)")):
        R = measure_B(posR, bondsR, a, k_a=rho, k_s=1.0, gamma=g,
                      lever=LEVER_GEOM, mp_at="[001]")
        L = measure_B(posL, bondsL, a, k_a=rho, k_s=1.0, gamma=g, lever=LEVER_GEOM)
        by_dir = {}
        for dname in {r["direction"] for r in R}:
            rr = [r for r in R if r["direction"] == dname]
            ll = [r for r in L if r["direction"] == dname]
            # THE COEFFICIENT: kappa/eps = c2 * q^2, c2 signed and in ell_node units
            # (ell_node == 1 in the driver's length unit: NN bond == 1, G1 receipt).
            cR = np.mean([r["c2_signed"] for r in rr[-4:]])
            cL = np.mean([r["c2_signed"] for r in ll[-4:]])
            iR = np.mean([abs(r["c2_imag_control"]) for r in rr[-4:]])
            spread = float(np.std([r["c2_signed"] for r in rr[-4:]])
                           / max(abs(cR), 1e-300))
            by_dir[dname] = {
                "c2_signed_right": float(cR), "c2_signed_left": float(cL),
                "c2_imag_control_right": float(iR),
                "parity_sum": float(cR + cL),
                "parity_odd": bool(abs(cR + cL) < 1e-6 * max(abs(cR), 1e-300)),
                "c2_plateau_relspread": spread,
                "power_of_q_in_kappa_over_eps": fit_power(rr),
                "rows_right": rr,
            }
        out["load_path_B"][tag] = by_dir

    # ---- roll-off toward yield (canon-forced swapped-spring rho_eff) --------
    roll = []
    for A in (0.0, 0.3, 0.6, 0.8, 0.9, 0.95, 0.99, 0.999):
        S = np.sqrt(max(1.0 - A * A, 0.0))
        # rho_eff = rho_cold*(S_axial/S_shear); the canon composition with the
        # AXIAL channel loaded by the squeeze and the shear channel cold.
        rho_eff = RHO_MATCH * (S / 1.0) if S > 0 else 0.0   # AXIAL channel loaded
        if rho_eff <= 1e-9:
            roll.append({"A_wall": A, "S": float(S), "rho_eff": float(rho_eff),
                         "tau": None, "c_twist_001": None, "note": "rho_eff -> 0"})
            continue
        rA = measure_A(posR, bondsR, k_a=rho_eff, k_s=1.0, gamma=g, lever=LEVER_GEOM)
        rB = load_path_B(posR, bondsR,
                         (1e-4 * 2 * np.pi / a) * np.array([0.0, 0.0, 1.0]),
                         np.array([0.0, 0.0, 1.0]),
                         k_a=rho_eff, k_s=1.0, gamma=g, lever=LEVER_GEOM)
        roll.append({"A_wall": A, "S": float(S), "rho_eff": float(rho_eff),
                     "tau_iso": rA[0]["tau_net_twist_per_strain"],
                     "tau_uni001": rA[1]["tau_net_twist_per_strain"],
                     "c_twist_001": rB["abs_c_twist"]})
    out["roll_off"] = roll

    # ---- the leak ratio -----------------------------------------------------
    c001 = abs(out["load_path_B"]["rho_bond=1 (Ax-3 match point)"]["[001]"]["c2_signed_right"])
    leak = []
    for R_m, label in ((1e-3, "1 mm"), (1.0, "1 m"), (6.371e6, "Earth radius"),
                       (6.957e8, "solar radius"), (1.48e3, "solar r_sat = 7GM/c^2")):
        qell = float(L_NODE / R_m)
        leak.append({"gradient_scale": label, "R_m": R_m,
                     "q_ell_node": qell,
                     "A_mu_over_A_eps__x__(omega_yield*ell/eps_yield)": float(c001 * qell * qell)})
    out["leak"] = {
        "c2_dimensionless_ell_node_units": float(c001),
        "form": "kappa/eps = c2*q^2  =>  A_mu/A_eps = c2 * (q*ell_node)^2 * (eps_yield/(omega_yield*ell_node^2))",
        "omega_yield_status": "CANON-ABSENT (no constants.py symbol, no KB home)",
        "rows": leak,
    }

    # ---- the relative-rotation modulus alpha and the constitutive coupling B ----
    # W = 1/2*C*eps^2 + 1/2*alpha*phi^2 + 1/2*D*kappa^2 + B*eps*kappa
    # A longitudinal wave has omega_macro = 0, so the phi restoring term is 1/2*alpha*phi^2
    # and minimising gives  kappa/eps = (B/alpha) q^2  ==  c2 q^2.  Hence B = c2 * alpha.
    V = a ** 3
    consts = {}
    for rho, tag in ((RHO_MATCH, "rho_bond=1 (Ax-3 match point)"),
                     (RHO_K2G, "rho*=9.7734 (K=2G, GR-imported)")):
        K = stiffness_k0(posR, bondsR, k_a=rho, k_s=1.0, gamma=g, lever=LEVER_GEOM)
        v = _uniform_vec(len(posR), 5)                       # uniform phi_z
        alpha = 2.0 * (0.5 * float(v @ (K @ v))) / V          # W = 1/2 alpha phi^2
        c2 = out["load_path_B"][tag]["[001]"]["c2_signed_right"]
        consts[tag] = {"alpha_relrot_modulus": float(alpha),
                       "c2_signed_[001]": float(c2),
                       "B_chiral_coupling": float(c2 * alpha),
                       "note": "alpha in k_s/a_cell^0 units; B = c2*alpha (stress x length)"}
    out["constitutive"] = consts

    # ---- the lockstep adjudication + S_kappa(wall) --------------------------
    # Cold expansion S = sqrt(1-A^2) ~ 1 - A^2/2  =>  dL/L = dS_mu/S_mu ~ -A_mu^2/2,
    # dC/C = dS_eps/S_eps ~ -A_eps^2/2. Lockstep ratio = (A_mu/A_eps)^2.
    # A_mu/A_eps = c2hat * (q*ell_node)^2  under the dimensionally-forced normalisation
    # omega_yield == eps_yield / ell_node (DECLARED: omega_yield is CANON-ABSENT).
    lock = []
    for label, qell in (("q*ell_node = 1 (single-node gradient; the ABSOLUTE ceiling)", 1.0),
                        ("1 mm gradient scale", L_NODE / 1e-3),
                        ("1 m gradient scale", L_NODE / 1.0),
                        ("solar r_sat = 7GM/c^2 = 1.03e4 m", L_NODE / 1.034e4),
                        ("Earth radius", L_NODE / 6.371e6)):
        for tag in consts:
            c2h = abs(consts[tag]["c2_signed_[001]"])
            amu_over_aeps = c2h * qell ** 2
            lock.append({
                "gradient_scale": label, "operating_point": tag,
                "q_ell_node": float(qell),
                "A_mu_over_A_eps": float(amu_over_aeps),
                "lockstep_ratio_dLL_over_dCC": float(amu_over_aeps ** 2),
                "S_kappa_at_wall": float(np.sqrt(max(0.0, 1.0 - amu_over_aeps ** 2))),
                "one_minus_S_kappa_at_wall": float(1.0 - np.sqrt(max(0.0, 1.0 - amu_over_aeps ** 2))),
            })
    out["lockstep"] = {
        "operational_definition": "(dL/L)/(dC/C) == 1  <=>  S_mu == S_eps  (Gamma_EM = 0)",
        "normalisation_declared": "omega_yield == eps_yield/ell_node (CANON-ABSENT; dimensionally forced)",
        "rows": lock,
    }

    dest = Path("research/drivers/srs_twist_coefficient_results.json")
    dest.parent.mkdir(parents=True, exist_ok=True)
    txt = json.dumps(out, indent=2, sort_keys=True, default=float)
    dest.write_text(txt)
    digest = hashlib.sha256(txt.encode()).hexdigest()
    out["meta"]["digest"] = digest
    print(json.dumps({"gates": [{k: v for k, v in gg.items()
                                 if k in ("gate", "pass", "verdict")}
                                for gg in out["gates"]]}, indent=2))
    print(f"[digest] sha256 = {digest}")
    return out


if __name__ == "__main__":
    sys.exit(0 if main() else 0)

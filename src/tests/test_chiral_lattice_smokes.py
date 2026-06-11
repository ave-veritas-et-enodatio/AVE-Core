"""
Genesis v9 Phase-0 — chiral trivalent lattice: geometry keepers + two smokes.

Every keeper is a REAL test: it FINDS the property (degree, girth, chirality,
unitarity, energy drift, ring writhe) and asserts it — nothing is asserted by
fiat. See research/2026-06-11_genesis-v9-chiral-lattice_design.md.

External-mathematics properties of the srs (Laves / (10,3)-a / Sunada-K4) net
(trivalent, 120 deg balanced bonds, girth-10, I4_1 32 / I4_3 32 enantiomorph
pair) are asserted ONLY here, against the constructed net — source class:
Sunada (Notices AMS 2008), RCSR `srs`, Wells (10,3)-a.

PHASE-0 scaffold. NO genesis run. Phase-1 is prereg-gated (Grant freezes), and
gated additionally on the §0 adjudication (v9 re-opens the 2026-06-07
lattice-net resolution-of-record).
"""

from itertools import permutations, product

import numpy as np
import pytest

from ave.core import chiral_lattice as cl


# ─── helpers (test-only) ─────────────────────────────────────────────────────
def _cubic_group():
    """48 signed permutation matrices (full O_h); det +1 = proper, -1 = improper."""
    mats = []
    for perm in permutations(range(3)):
        P = np.zeros((3, 3))
        for i, p in enumerate(perm):
            P[i, p] = 1.0
        for signs in product([1, -1], repeat=3):
            mats.append(np.diag(signs).astype(float) @ P)
    return mats


def _match_mod1(A, B, tol=1e-6):
    used = [False] * len(B)
    for a in A:
        ok = False
        for j, b in enumerate(B):
            if not used[j] and np.all(np.abs(((a - b + 0.5) % 1.0) - 0.5) < tol):
                used[j] = True
                ok = True
                break
        if not ok:
            return False
    return all(used)


def _maps_to(src, dst, M):
    Rs = (M @ src.T).T
    for j in range(len(dst)):
        if _match_mod1(np.mod(Rs + dst[j] - Rs[0], 1.0), np.mod(dst, 1.0)):
            return True
    return False


# ─── geometry keepers ────────────────────────────────────────────────────────
def test_srs_is_trivalent():
    net = cl.build_srs_net(4, "right")
    deg = np.array([len(a) for a in net.neighbors])
    assert (deg == 3).all(), f"srs must be degree-3; got degrees {np.unique(deg)}"


def test_srs_bonds_120_balanced():
    """Harmonic (balanced) realization: 3 edge unit-vectors sum to 0, pairwise 120 deg."""
    net = cl.build_srs_net(4, "right")
    for v in np.where(net.interior_mask)[0][:24]:
        vecs = net.bond_unit[v]
        assert np.linalg.norm(np.sum(vecs, axis=0)) < 1e-9
        for a in range(3):
            for b in range(a + 1, 3):
                ang = np.degrees(np.arccos(np.clip(np.dot(vecs[a], vecs[b]), -1, 1)))
                assert abs(ang - 120.0) < 1e-3, f"bond angle {ang} != 120"


def test_srs_girth_is_ten():
    """FIND the shortest rings and assert their size is 10 (not assumed)."""
    _, _, n, (lo, hi) = cl.net_ring_writhe(cl.build_srs_net(6, "right"))
    assert n > 0
    assert lo == 10 and hi == 10, f"srs girth must be 10; found ring lengths [{lo},{hi}]"


def test_srs_chiral_point_group_432():
    """Self-symmetry = 24 proper, 0 improper => chiral point group 432."""
    motif = cl.srs_motif("right")
    G = _cubic_group()
    proper = sum(1 for M in G if np.linalg.det(M) > 0 and _maps_to(motif, motif, M))
    improper = sum(1 for M in G if np.linalg.det(M) < 0 and _maps_to(motif, motif, M))
    assert proper == 24, f"expected 24 proper self-symmetries; got {proper}"
    assert improper == 0, f"chiral net must have 0 improper self-symmetries; got {improper}"


def test_enantiomorph_pair_is_improper():
    """native -> mirror requires an improper operation (no proper rotation maps them)."""
    right, left = cl.srs_motif("right"), cl.srs_motif("left")
    G = _cubic_group()
    proper = sum(1 for M in G if np.linalg.det(M) > 0 and _maps_to(right, left, M))
    improper = sum(1 for M in G if np.linalg.det(M) < 0 and _maps_to(right, left, M))
    assert proper == 0, f"enantiomorphs must NOT be related by a proper rotation; got {proper}"
    assert improper > 0, "enantiomorphs must be related by an improper operation"


def test_diamond_control_is_degree4_achiral():
    net = cl.build_diamond_net(4)
    deg = np.array([len(a) for a in net.neighbors])
    assert (deg == 4).all(), "diamond control must be degree-4"
    mean, _, n, _ = cl.net_ring_writhe(net)
    assert n > 0
    assert abs(mean) < 1e-9, f"achiral control rings must have ~0 writhe; got {mean}"


# ─── Op5 trivalent scatter (derived, new instantiation) ──────────────────────
def test_trivalent_scatter_unitary_and_reduces_to_canon():
    S3 = cl.scatter_matrix(3)
    assert np.abs(S3.T @ S3 - np.eye(3)).max() < 1e-12, "trivalent scatter must be unitary"
    assert np.allclose(np.abs(np.linalg.eigvals(S3)), 1.0, atol=1e-12)
    # cross-anchor: n=4 must reduce to canonical diamond S_ij = 1/2 - delta_ij
    S4 = cl.scatter_matrix(4)
    assert np.allclose(S4, 0.5 * np.ones((4, 4)) - np.eye(4)), "n=4 must recover canon 1/2 - delta"


# ─── Smoke A — consistency gate (didn't break the physics that worked) ───────
def test_smoke_a_energy_conservation():
    net = cl.build_srs_net(6, "right")
    conn = net.connect_index()
    S = cl.scatter_matrix(3)
    V = np.zeros((net.n_nodes, 3))
    V[int(np.where(net.interior_mask)[0][0])] = 1.0
    E0 = cl.lattice_energy(V)
    drift = 0.0
    for _ in range(200):
        V = cl.scalar_tlm_step(net, V, S, conn)
        drift = max(drift, abs(cl.lattice_energy(V) - E0) / E0)
    assert drift < 1e-10, f"closed-system energy must conserve; drift={drift:.2e}"


def test_smoke_a_dispersion_isotropic():
    """Point-source pulse spreads isotropically on the chiral net (achiral physics intact)."""
    net = cl.build_srs_net(6, "right")
    conn = net.connect_index()
    S = cl.scatter_matrix(3)
    i0 = int(np.where(net.interior_mask)[0][0])
    V = np.zeros((net.n_nodes, 3))
    V[i0] = 1.0
    for _ in range(120):
        V = cl.scalar_tlm_step(net, V, S, conn)
    E = np.sum(V * V, axis=1)
    d = net.pos - net.pos[i0]
    d -= net.box * np.round(d / net.box)
    rms = np.sqrt(np.sum(E[:, None] * d**2, axis=0) / E.sum())
    iso = rms.min() / rms.max()
    assert iso > 0.9, f"scalar dispersion must be axis-isotropic; ratio={iso:.3f}"


# ─── Smoke B — optical-activity source (writhe of shortest circuits) ─────────
def test_smoke_b_optical_activity_signed_and_control_zero():
    """The discriminating heart: signed, enantiomorph-flipped, zero on control."""
    wr_r, _, nr, _ = cl.net_ring_writhe(cl.build_srs_net(6, "right"))
    wr_l, _, nl, _ = cl.net_ring_writhe(cl.build_srs_net(6, "left"))
    wr_d, _, nd, _ = cl.net_ring_writhe(cl.build_diamond_net(6))
    assert nr > 0 and nl > 0 and nd > 0
    # (1) chiral net carries nonzero helicity
    assert abs(wr_r) > 1e-3, f"srs must carry nonzero ring helicity; got {wr_r:.2e}"
    # (2) enantiomorphs: opposite sign, equal magnitude
    assert wr_r * wr_l < 0, "enantiomorphs must have opposite-sign writhe"
    assert abs(wr_r + wr_l) < 1e-2 * abs(wr_r), "enantiomorph magnitudes must match"
    # (3) achiral control: zero (a pseudoscalar from a centrosymmetric net vanishes)
    assert abs(wr_d) < 0.05 * abs(wr_r), f"control writhe must be ~0; got {wr_d:.2e}"


def test_smoke_b_writhe_is_box_independent():
    """Robustness: the ring helicity is intensive (box-size invariant)."""
    vals = [cl.net_ring_writhe(cl.build_srs_net(L, "right"))[0] for L in (4, 6, 8)]
    assert max(vals) - min(vals) < 1e-6, f"writhe must be box-independent; got {vals}"

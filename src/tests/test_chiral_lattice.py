"""
Genesis v9 Phase-0 — chiral trivalent lattice: GRAPH-LIBRARY geometry keepers.

The dedicated graph-geometry validation suite for the v9 lattice library
(src/ave/core/chiral_lattice.py). Companion to test_chiral_lattice_smokes.py,
which carries the two PHYSICS smokes (consistency gate + optical-activity
source); THIS file validates the GRAPH itself — coordination, bond angles,
shortest-ring girth, the 4_1 screw axis, the enantiomorph mirror relation, and
the cubic-system achiral control.

Every keeper is a REAL test: it FINDS the property from the constructed graph
(coordination from the adjacency lists, bond angles from the edge unit-vectors,
girth by BFS ring enumeration, the 4_1 screw by searching for an edge-preserving
graph automorphism, the handedness from the shortest-circuit writhe) and asserts
the MEASURED value. Nothing is asserted by fiat — the girth keeper asserts what
BFS returns, not a hard-coded 10.

External-mathematics properties of the srs (Laves / (10,3)-a / Sunada-K4) net
(trivalent, 120 deg balanced bonds, girth-10, I4_1 32 / I4_3 32 enantiomorph
pair, 4_1 screw axes) are asserted ONLY here against the constructed net.
Source class: Sunada, "Crystals that nature might miss creating," Notices AMS
2008; RCSR `srs`; Wells (10,3)-a. They are NOT taken from canon — canon's
computed object is the degree-4 achiral diamond (design doc §0 adjudication
flag); these are the flagged outlier leaves, validated in-scaffold.

PHASE-0 scaffold. NO genesis run. See
research/2026-06-11_genesis-v9-chiral-lattice_design.md.
"""

from itertools import permutations, product

import numpy as np
from scipy.spatial import cKDTree

from ave.core import chiral_lattice as cl


# ─── shared measurement helper ───────────────────────────────────────────────
def _bfs_girth(net, n_start=64):
    """FIND the shortest rings by BFS over interior nodes.

    Returns (min_len, max_len, n_distinct) — the girth is min_len, MEASURED, not
    assumed. Distinct rings are de-duplicated by node-set so the count is the
    number of independent shortest circuits sampled.
    """
    starts = np.where(net.interior_mask)[0][:n_start]
    seen, lengths = set(), []
    for s in starts:
        ring = cl.shortest_ring(net, int(s))
        if ring is None:
            continue
        key = frozenset(ring)
        if key in seen:
            continue
        seen.add(key)
        lengths.append(len(ring))
    if not lengths:
        return 0, 0, 0
    return min(lengths), max(lengths), len(lengths)


# ─── keeper 1 — coordination number, asserted FROM the graph ─────────────────
def test_coordination_number_from_graph():
    """Coordination is read off the adjacency lists, not declared. srs -> 3 on
    every interior node, on BOTH enantiomorphs; the cubic control -> 4."""
    for hand in ("right", "left"):
        net = cl.build_srs_net(4, hand)
        deg = np.array([len(a) for a in net.neighbors])
        vals, counts = np.unique(deg, return_counts=True)
        hist = dict(zip(vals.tolist(), counts.tolist()))
        assert (deg == 3).all(), f"srs[{hand}] must be uniformly trivalent; degree histogram {hist}"
    dn = cl.build_diamond_net(6)
    degd = np.array([len(a) for a in dn.neighbors])
    assert (degd == 4).all(), f"cubic control (diamond) must be degree-4; got {np.unique(degd)}"


# ─── keeper 2 — bond angles, MEASURED from the edge vectors ───────────────────
def test_bond_angles_measured():
    """Measure the angles between the three edge unit-vectors at each node and
    assert the balanced 120 deg / 120 deg / 120 deg trivalent vertex (sum of the
    three edge unit-vectors = 0). Both enantiomorphs."""
    for hand in ("right", "left"):
        net = cl.build_srs_net(4, hand)
        for v in np.where(net.interior_mask)[0][:24]:
            vecs = net.bond_unit[v]
            assert len(vecs) == 3, f"srs[{hand}] node {v} must have 3 edges"
            assert np.linalg.norm(np.sum(vecs, axis=0)) < 1e-9, (
                f"srs[{hand}] node {v}: edge unit-vectors not balanced (Σ != 0)"
            )
            for a in range(3):
                for b in range(a + 1, 3):
                    ang = np.degrees(np.arccos(np.clip(np.dot(vecs[a], vecs[b]), -1.0, 1.0)))
                    assert abs(ang - 120.0) < 1e-3, f"srs[{hand}] bond angle {ang:.4f} != 120"


# ─── keeper 3 — shortest-ring girth by BFS (assert the MEASURED size) ─────────
def test_shortest_ring_girth_bfs():
    """Enumerate shortest rings by BFS and assert the MEASURED girth. The size is
    whatever BFS finds; the srs external-mathematics value is 10 and the keeper
    fails loudly with the measured size if it is not."""
    for hand in ("right", "left"):
        lo, hi, n = _bfs_girth(cl.build_srs_net(6, hand))
        assert n > 0, f"srs[{hand}]: BFS found no rings"
        assert lo == hi == 10, (
            f"srs[{hand}] measured girth = [{lo},{hi}] over {n} distinct shortest rings "
            f"(srs external-math value is 10)"
        )


# ─── keeper 6 — cubic-system achiral reference (the control) ──────────────────
def test_cubic_reference_degree4_achiral_distinct():
    """The cubic-system achiral control: the canonical diamond net (design §2.2 —
    the engine's own degree-4 substrate, space group Fd-3m, centrosymmetric).
    Asserts degree-4, MEASURED girth-6 (a genuinely DIFFERENT graph from the
    trivalent girth-10 srs), and zero handedness measure (a pseudoscalar of a
    centrosymmetric net vanishes). L>=6: at L=4 the girth is a PBC wrap artifact
    (=4); it converges to the true diamond girth 6 at L>=6.
    """
    dn = cl.build_diamond_net(6)
    deg = np.array([len(a) for a in dn.neighbors])
    assert (deg == 4).all(), "cubic reference (diamond) must be degree-4"
    lo, hi, n = _bfs_girth(dn)
    assert lo == hi == 6, f"diamond girth measured [{lo},{hi}] over {n} rings (expected 6)"
    mean, _, nr, _ = cl.net_ring_writhe(dn)
    assert nr > 0 and abs(mean) < 1e-9, f"cubic-reference handedness must be 0; got {mean:.2e}"
    # explicitly a different graph from the chiral net (degree + girth both differ)
    assert dn.degree == 4 and cl.build_srs_net(4, "right").degree == 3


# ─── 4_1 screw-axis helpers (test-local — chiral_lattice.py stays the graph library) ──
def _proper_4fold_rotations():
    """Proper signed-permutation matrices that are 4-fold (90deg about a cubic axis)."""
    out = []
    for perm in permutations(range(3)):
        P = np.zeros((3, 3))
        for i, p in enumerate(perm):
            P[i, p] = 1.0
        for signs in product((1, -1), repeat=3):
            M = np.diag(signs).astype(float) @ P
            if np.linalg.det(M) <= 0:
                continue
            M2 = M @ M
            if (not np.allclose(M, np.eye(3)) and not np.allclose(M2, np.eye(3))
                    and np.allclose(M2 @ M2, np.eye(3))):
                out.append(M)
    return out


def _rotation_axis(R):
    """Unit eigenvector of R with eigenvalue +1 (the 4-fold rotation axis)."""
    w, v = np.linalg.eig(R)
    for i in range(3):
        if np.isclose(w[i].real, 1.0) and abs(w[i].imag) < 1e-9:
            a = np.real(v[:, i])
            return a / np.linalg.norm(a)
    return None


def _motif_translation(R, motif, tol=1e-6):
    """The in-cell translation t with R·motif + t ≡ motif (mod 1) as a set, or None."""
    Rm = (R @ motif.T).T
    for j in range(len(motif)):
        t = np.mod(motif[j] - Rm[0], 1.0)
        cand = np.mod(Rm + t, 1.0)
        used = [False] * len(motif)
        ok = True
        for c in cand:
            hit = False
            for k, m in enumerate(motif):
                if not used[k] and np.all(np.abs(((c - m + 0.5) % 1.0) - 0.5) < tol):
                    used[k] = True
                    hit = True
                    break
            if not hit:
                ok = False
                break
        if ok and all(used):
            return t
    return None


def _graph_automorphism(net, R, t):
    """Apply (R, t) in cell units to the FULL net; return
    (dmax, is_bijection, edge_preserving). A genuine automorphism has dmax≈0,
    is a bijection on the node set, and preserves every edge."""
    pts = net.pos / net.a_cell
    Lb = net.box / net.a_cell
    img = np.mod((R @ pts.T).T + t, Lb)
    tree = cKDTree(np.mod(pts, Lb), boxsize=Lb)
    d, sigma = tree.query(img, k=1)
    dmax = float(d.max())
    is_bij = len(set(sigma.tolist())) == net.n_nodes
    edge_ok = is_bij
    if is_bij:
        for u in range(net.n_nodes):
            mapped = {int(sigma[v]) for v in net.neighbors[u]}
            target = {int(x) for x in net.neighbors[int(sigma[u])]}
            if mapped != target:
                edge_ok = False
                break
    return dmax, is_bij, edge_ok


def _find_graph_screw_ops(net, motif):
    """All 4-fold proper ops (R, t) mapping this net's motif to itself, each
    validated as a full-graph automorphism. Returns
    [(axis, along_axis_frac, dmax, is_bijection, edge_preserving), ...]."""
    ops = []
    for R in _proper_4fold_rotations():
        t = _motif_translation(R, motif)
        if t is None:
            continue
        axis = _rotation_axis(R)
        along = float(np.dot(t, np.abs(axis))) % 1.0
        dmax, is_bij, edge_ok = _graph_automorphism(net, R, t)
        ops.append((axis, along, dmax, is_bij, edge_ok))
    return ops


# ─── keeper 4 — the 4_1 screw axis maps the GRAPH to itself ───────────────────
def test_screw_axis_4_1_maps_graph_to_itself():
    """The 4_1 screw symmetry of I4_1 32 / I4_3 32: a 4-fold proper rotation plus a
    quarter-pitch translation along the axis, mapping the GRAPH (positions AND
    adjacency) to itself. Each candidate is FOUND by search, then verified as a
    genuine edge-preserving graph automorphism. The 1/4 (or 3/4 = -1/4) along-axis
    translation is the SCREW signature — a pure 4-fold rotation would give 0."""
    for hand in ("right", "left"):
        net = cl.build_srs_net(4, hand)
        motif = cl.srs_motif(hand)
        ops = _find_graph_screw_ops(net, motif)
        assert len(ops) >= 3, (
            f"srs[{hand}]: expected >=3 four-fold screw axes (the 3 cubic <100>); found {len(ops)}"
        )
        for (axis, along, dmax, is_bij, edge_ok) in ops:
            assert is_bij and edge_ok, (
                f"srs[{hand}] 4-fold op (axis {np.round(axis, 3)}) is not a graph automorphism"
            )
            assert dmax < 1e-9, f"srs[{hand}] screw op not exact: position dmax={dmax:.2e}"
            quarter = min(abs(along - 0.25), abs(along - 0.75))
            assert quarter < 1e-6, (
                f"srs[{hand}] 4-fold op is not a 1/4-screw (4_1); along-axis frac={along:.4f}"
            )


# ─── keeper 5 — enantiomorph mirror: same invariants, opposite handedness ─────
def test_enantiomorph_mirror_same_invariants_opposite_handedness():
    """The two enantiomorphs (I4_1 32 / I4_3 32) are mirror images: IDENTICAL graph
    invariants (degree sequence, girth, distinct-ring count, bond-angle multiset)
    but OPPOSITE handedness measure (shortest-circuit writhe — sign flips, magnitude
    matches)."""
    right = cl.build_srs_net(6, "right")
    left = cl.build_srs_net(6, "left")

    # identical graph invariants
    assert sorted(len(a) for a in right.neighbors) == sorted(len(a) for a in left.neighbors), \
        "enantiomorphs must share the degree sequence"
    # girth (min,max) is the cross-enantiomorph invariant; the distinct-ring COUNT
    # from a truncated BFS sample is node-labeling dependent (the mirror relabels
    # the node indices, so a 64-start sample discovers a different ring subset), so
    # only the girth is compared here, not the sampled ring count.
    gr, gl = _bfs_girth(right), _bfs_girth(left)
    assert gr[:2] == gl[:2], f"enantiomorph girth must match: {gr[:2]} vs {gl[:2]}"

    def _angle_multiset(net):
        out = []
        for v in np.where(net.interior_mask)[0][:24]:
            vv = net.bond_unit[v]
            for a in range(3):
                for b in range(a + 1, 3):
                    out.append(round(np.degrees(np.arccos(np.clip(np.dot(vv[a], vv[b]), -1, 1))), 3))
        return sorted(out)

    assert _angle_multiset(right) == _angle_multiset(left), \
        "enantiomorph bond-angle multiset must match"

    # OPPOSITE handedness measure: writhe sign-flip, equal magnitude (the mirror)
    wr = cl.net_ring_writhe(right)[0]
    wl = cl.net_ring_writhe(left)[0]
    assert wr * wl < 0, f"enantiomorph handedness must be opposite-sign; got {wr:.4e}, {wl:.4e}"
    assert abs(wr + wl) < 1e-2 * abs(wr), \
        f"enantiomorph |handedness| must match (mirror); sum={wr + wl:.2e}"

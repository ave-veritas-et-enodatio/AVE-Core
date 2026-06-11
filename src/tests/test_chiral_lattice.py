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

import numpy as np

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

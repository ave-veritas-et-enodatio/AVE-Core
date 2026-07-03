"""LANE-Z STEP-0 keepers — the punctured srs-complex fluxoid-doorway topology.

Certifies the step-0 finding (research/2026-07-03_lanez-fluxoid-step0_note.md):
  - BALL puncture: Δb1 = 0 at all radii, all box sizes (L=3,4,5) — the ball
    opens NO source-free harmonic 1-cochain DOF on the 2-complex. NO-DOORWAY for
    the ball shape (its would-be H2 enclosing-sphere is not carried by a complex
    with no 3-cells).
  - TORUS puncture (the (2,3) tube): Δb1 = +1, STABLE across L, at the
    geometrically-matched cut — a NEW harmonic 1-cochain = the meridian linking
    cycle. DOORWAY exists for the torus shape.
  - DISC-FILL certification (L=3): re-adding one meridian disc drops b1 by 1,
    proving the new generator is the CORE-LINKING meridian (not boundary roughness).
  - Two-method b1 (rank-nullity vs 1-Laplacian nullity) agree — no rank artifact.

Deterministic; α-clean (integer topology only). Fast (a few seconds at L≤4).
"""
import numpy as np
import pytest
from scipy import sparse

from ave.core.chiral_lattice import build_srs_net
from ave.topological.srs_dec_punctured import (
    ball_keep_mask,
    betti_punctured,
    build_punctured,
    cube_frame_coords,
    doorway_delta,
    torus_keep_mask,
)

_FRAME_N = 20  # cube-frame the (2,3) winding torus (R=7,r=2.3) is specified in


# ─────────────────────────────────────────────────────────────────────────────
# 1. Closed box reproduces the merged srs_dec result (b1=3, the T³ handles).
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.parametrize("L,expect_V", [(3, 216), (4, 512)])
def test_closed_box_b1_is_three(L, expect_V):
    net = build_srs_net(L=L, enantiomorph="right")
    b = betti_punctured(build_punctured(net, np.ones(net.n_nodes, bool)))
    assert b["V"] == expect_V
    assert b["b0"] == 1               # connected
    assert b["b1"] == 3               # the three periodic-T³ wraps (merged result)
    assert b["b1_two_method_agree"]   # rank-nullity == 1-Laplacian nullity


# ─────────────────────────────────────────────────────────────────────────────
# 2. BALL puncture opens NO harmonic DOF: Δb1 = 0 (NO-DOORWAY for the ball).
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.parametrize("L", [3, 4, 5])
@pytest.mark.parametrize("r_ball", [2.5, 3.0, 3.5, 4.0])
def test_ball_puncture_no_new_harmonic_dof(L, r_ball):
    net = build_srs_net(L=L, enantiomorph="right")
    keep = ball_keep_mask(net, _FRAME_N, r_ball)
    if (~keep).sum() == 0:
        pytest.skip("no nodes removed at this radius/box")
    d = doorway_delta(net, keep)
    assert d["delta_b1"] == 0, f"ball opened a harmonic DOF: {d}"
    assert d["b1_two_method_agree"]


# ─────────────────────────────────────────────────────────────────────────────
# 3. TORUS puncture opens EXACTLY ONE harmonic DOF at the matched cut: Δb1 = +1.
#    (The (2,3) tube radius is r=2.3; the matched cut window is rc ∈ [2.3, 2.8].)
# ─────────────────────────────────────────────────────────────────────────────
@pytest.mark.parametrize("L", [3, 4, 5])
def test_torus_puncture_opens_one_meridian_dof(L):
    net = build_srs_net(L=L, enantiomorph="right")
    # rc = 2.8 is inside the matched window and clears the ragged-cut outliers
    keep = torus_keep_mask(net, _FRAME_N, r_cut=2.8)
    d = doorway_delta(net, keep)
    assert d["delta_b1"] == 1, f"torus Δb1 != +1 at matched cut: {d}"
    assert d["b1_two_method_agree"]


# ─────────────────────────────────────────────────────────────────────────────
# 4. DISC-FILL: the new torus generator IS the core-linking meridian (L=3).
#    Re-add ONE synthetic 2-cell spanning a meridian edge-loop; b1 drops by 1.
# ─────────────────────────────────────────────────────────────────────────────
def _shortest_meridian_loop(net, pc, frame_N, R=7.0):
    """A surviving edge-cycle whose poloidal angle psi winds ~2π (links the tube)."""
    import heapq

    gc = cube_frame_coords(net, frame_N)
    rho = np.hypot(gc[:, 0], gc[:, 1])
    psi = np.arctan2(gc[:, 2], rho - R)
    rtube = np.hypot(rho - R, gc[:, 2])
    knset = set(np.flatnonzero(pc.keep).tolist())
    adj = {n: [] for n in knset}
    for (u, v) in pc.edges:
        adj[u].append(v)
        adj[v].append(u)
    seeds = sorted((n for n in knset if rtube[n] < 4.0), key=lambda n: rtube[n])[:40]
    for start in seeds:
        pq = [(0, start, 0.0, (start,))]
        seen = {}
        while pq:
            d, node, wind, path = heapq.heappop(pq)
            if len(path) > 16:
                continue
            for nb in adj[node]:
                dpsi = (psi[nb] - psi[node] + np.pi) % (2 * np.pi) - np.pi
                nwind = wind + dpsi
                if nb == start and len(path) >= 5 and 1.5 * np.pi < abs(nwind) < 2.5 * np.pi:
                    return path + (start,)
                if nb in path:
                    continue
                key = (nb, round(nwind, 1))
                if key in seen and seen[key] <= d + 1:
                    continue
                seen[key] = d + 1
                heapq.heappush(pq, (d + 1, nb, nwind, path + (nb,)))
    return None


def test_disc_fill_certifies_core_linking_meridian_L3():
    net = build_srs_net(L=3, enantiomorph="right")
    pc = build_punctured(net, torus_keep_mask(net, _FRAME_N, r_cut=2.8))
    b_before = betti_punctured(pc)["b1"]
    assert b_before == 4  # 3 wraps + 1 meridian

    loop = _shortest_meridian_loop(net, pc, _FRAME_N)
    assert loop is not None, "meridian edge-loop search miss (deterministic at L=3)"
    eidx = {e: i for i, e in enumerate(pc.edges)}
    col = np.zeros(pc.E)
    for i in range(len(loop) - 1):
        a, b = loop[i], loop[i + 1]
        col[eidx[(min(a, b), max(a, b))]] += 1.0 if a < b else -1.0

    D2aug = sparse.hstack([pc.D2, sparse.csr_matrix(col.reshape(-1, 1))]).tocsr()
    r1 = int(np.linalg.matrix_rank(pc.D1.toarray()))
    r2 = int(np.linalg.matrix_rank(D2aug.toarray()))
    b1_filled = pc.E - r1 - r2
    # adding the meridian disc kills exactly the new generator: 4 -> 3
    assert b_before - b1_filled == 1, (
        f"disc-fill drop = {b_before - b1_filled} (expected 1: the new generator "
        f"is the disc-bounded core-linking meridian)")

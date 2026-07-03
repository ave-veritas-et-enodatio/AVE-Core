"""Punctured srs DEC complex — the lane-Z fluxoid doorway topology (STEP-0).

LANE Z STEP-0 (Grant-fired 2026-07-03). This module extends the merged srs DEC
machinery (`ave.topological.srs_dec`) to a PUNCTURED complex: remove a core region
(a ball of nodes, or the (2,3) winding's solid-torus tube) from the periodic srs
box, and compute the cohomology of the EXTERIOR subcomplex.

═══════════════════════════════════════════════════════════════════════════════
WHY THIS EXISTS (the convergence — verify each leg at HEAD)
═══════════════════════════════════════════════════════════════════════════════
(1) The [NO-FLUX-STRUCTURAL] maximum-principle theorem
    (research/2026-07-03_em-readout-stage2-redesign_prereg.md §R1) closes STATIC
    exterior-E sourcing for ANY strictly-positive edge weight S(A)>0. Its ONE
    stated escape (§R1 last para) is S=0 EXACTLY — the DEGENERATE operator where a
    bond weight vanishes (the over-yield rupture point).
(2) Canon puts the electron's T2 wall AT V_yield — SATURATED, S->0 is the wall's
    regime (resonant-lc-solitons.md:127,134: Z_shear->0, Gamma=-1). So the escape
    hatch is exactly where the electron's wall lives.
(3) The DEC harmonic sector (srs_dec.betti_numbers, b1=3 on the CLOSED box) is the
    unique survivor of the div-of-curl cascade (the theorem does NOT annihilate
    harmonic 1-cochains). It is where non-contractible-cycle flux lives.

CONCLUSION TESTED HERE: the saturated core (S=0) PUNCTURES the domain. A punctured
domain has NEW topological field content — flux through a surface enclosing the
core becomes a harmonic DOF of the exterior, determined by no source. That is the
fluxoid pattern. This module CONFIRMS or REFUTES the doorway by computing whether
the exterior gains a harmonic generator.

═══════════════════════════════════════════════════════════════════════════════
THE SUBSTRATE-NATIVE DISTINCTION (why the naive "ball -> +1 H2" was wrong)
═══════════════════════════════════════════════════════════════════════════════
The naive charter expectation ("ball: expect +1 = the enclosed-flux DOF") is the
answer for a complex WITH 3-cells, where H2 counts enclosing surfaces. The srs DEC
complex is a 2-COMPLEX (0-,1-,2-cells; NO 3-cells). On a 2-complex:
  - A BALL puncture's enclosing sphere would be an H2 generator, but with no
    3-cells there is nothing for it to fail-to-bound against in a source-free way,
    and b2 is over-complete on the full 10-ring face set anyway (srs_dec result
    doc §4). => the BALL puncture opens NO source-free harmonic DOF on this
    substrate. This is a substrate-native REFUTATION of the ball doorway, not a
    bug.
  - A SOLID-TORUS puncture's linking loop IS an H1 generator (a meridian 1-cycle
    that encircles the removed tube). H1 IS carried by the 2-complex (b1=3 closed).
    => the (2,3) TORUS puncture opens a NEW harmonic 1-cochain DOF (db1=+1), the
    meridian linking cycle — the fluxoid-carrying doorway.

So the physical fluxoid DOF is a HARMONIC 1-COCHAIN (an edge field E whose
circulation around a loop LINKING the core is fixed by no source), NOT an H2
enclosing-surface. This matches the fluxoid (superconductor: flux through the
RING's hole, threaded by a loop linking the hole).

α-CLEAN: no ALPHA / Q_TANK / V_SNAP on any path. Pure combinatorial topology of
the punctured connect-map (integer incidence matrices + rank–nullity).
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.core.chiral_lattice import LatticeNet, build_srs_net
from ave.topological.srs_dec import enumerate_girth_faces, oriented_edges

assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK must NOT be imported"
assert "V_SNAP" not in globals(), "α-leak: V_SNAP must NOT be on this path"

# The (2,3) winding torus geometry (cube-frame), verbatim from the winding seed
# (src/ave/solvers/srs_cage_winding.py:301-302). GEOMETRY-INPUT, not a posit here.
WINDING_R: float = 7.0   # (2,3) torus MAJOR radius (cube-frame)
WINDING_r: float = 2.3   # (2,3) torus MINOR (tube) radius (cube-frame)


def cube_frame_coords(net: LatticeNet, frame_N: int) -> np.ndarray:
    """srs node positions in the CENTERED cube-frame the winding seed uses.

    Verbatim mapping from srs_cage_winding.seed_pq_winding_on_srs:174-176:
        g = net.pos / net.box * frame_N ;  c = (frame_N-1)/2 ; centered = g - c.
    """
    g = net.pos / net.box * frame_N
    return g - (frame_N - 1) / 2.0


def ball_keep_mask(net: LatticeNet, frame_N: int, r_ball: float) -> np.ndarray:
    """Keep nodes OUTSIDE a cube-frame ball of radius r_ball centred at origin."""
    gc = cube_frame_coords(net, frame_N)
    return np.linalg.norm(gc, axis=1) >= r_ball


def torus_keep_mask(net: LatticeNet, frame_N: int, r_cut: float,
                    R: float = WINDING_R) -> np.ndarray:
    """Keep nodes OUTSIDE the (2,3) solid-torus tube (rtube = sqrt((rho-R)^2+z^2))."""
    gc = cube_frame_coords(net, frame_N)
    rho = np.hypot(gc[:, 0], gc[:, 1])
    rtube = np.hypot(rho - R, gc[:, 2])
    return rtube >= r_cut


@dataclass(frozen=True)
class PuncturedComplex:
    """The exterior subcomplex (full subcomplex on the surviving nodes).

    An edge survives iff BOTH endpoints survive; a girth-10 face survives iff ALL
    its ring nodes survive (the open-star removal → a genuine subcomplex, so the
    ∂∂=0 identity is inherited exactly)."""

    net: LatticeNet
    keep: np.ndarray            # bool node mask (True = kept in the exterior)
    edges: list                 # surviving oriented edges (remapped-node indices)
    faces: list                 # surviving girth-10 rings (original node indices)
    D1: object                  # ∂₁ on the subcomplex (n_kept × n_edges)
    D2: object                  # ∂₂ on the subcomplex (n_edges × n_faces)

    @property
    def V(self) -> int:
        return int(self.keep.sum())

    @property
    def E(self) -> int:
        return self.D1.shape[1]

    @property
    def F(self) -> int:
        return self.D2.shape[1]


def build_punctured(net: LatticeNet, keep: np.ndarray) -> PuncturedComplex:
    """Assemble ∂₁, ∂₂ on the full subcomplex of the kept nodes."""
    from scipy import sparse

    remap = -np.ones(net.n_nodes, dtype=np.int64)
    kept = np.flatnonzero(keep)
    remap[kept] = np.arange(len(kept))

    edges = [(u, v) for (u, v) in oriented_edges(net) if keep[u] and keep[v]]
    faces = [rg for rg in enumerate_girth_faces(net) if all(keep[n] for n in rg)]
    eidx = {e: i for i, e in enumerate(edges)}
    nv, ne, nf = len(kept), len(edges), len(faces)

    rows, cols, vals = [], [], []
    for e, (u, v) in enumerate(edges):
        rows += [remap[v], remap[u]]
        cols += [e, e]
        vals += [1.0, -1.0]
    D1 = sparse.csr_matrix((vals, (rows, cols)), shape=(nv, ne)) if ne \
        else sparse.csr_matrix((nv, 0))

    rows, cols, vals = [], [], []
    for fj, rg in enumerate(faces):
        n = len(rg)
        for i in range(n):
            a, b = rg[i], rg[(i + 1) % n]
            rows.append(eidx[(min(a, b), max(a, b))])
            cols.append(fj)
            vals.append(1.0 if a < b else -1.0)
    D2 = sparse.csr_matrix((vals, (rows, cols)), shape=(ne, nf)) if nf \
        else sparse.csr_matrix((ne, 0))

    return PuncturedComplex(net=net, keep=keep, edges=edges, faces=faces,
                            D1=D1, D2=D2)


def betti_punctured(pc: PuncturedComplex) -> dict:
    """(b0, b1, b2) of the punctured exterior via rank–nullity, PLUS a two-method
    cross-check on b1 (the load-bearing harmonic-DOF count):

        b1(rank-nullity) = E − rank(∂₁) − rank(∂₂)
        b1(1-Laplacian)  = E − rank(L1),   L1 = ∂₁ᵀ∂₁ + ∂₂∂₂ᵀ  (Hodge nullity)

    The two agree on a valid complex (grep-completeness / two-method discipline).
    b1 is the HARMONIC 1-cochain dimension = the number of independent non-
    contractible 1-cycles. b2 is OVER-COMPLETE on the full 10-ring face set
    (inherited from the closed box — srs_dec result doc §4) and reported for
    bookkeeping only, NOT as a clean invariant."""
    D1d = pc.D1.toarray()
    D2d = pc.D2.toarray()
    r1 = int(np.linalg.matrix_rank(D1d)) if pc.E else 0
    r2 = int(np.linalg.matrix_rank(D2d)) if pc.F else 0
    b1_rn = pc.E - r1 - r2
    if pc.E:
        L1 = D1d.T @ D1d + D2d @ D2d.T
        b1_lap = int(pc.E - np.linalg.matrix_rank(L1))
    else:
        b1_lap = 0
    return {
        "V": pc.V, "E": pc.E, "F": pc.F, "rank_D1": r1, "rank_D2": r2,
        "b0": pc.V - r1, "b1": b1_rn, "b1_laplacian": b1_lap, "b2": pc.F - r2,
        "b1_two_method_agree": b1_rn == b1_lap,
    }


def doorway_delta(net: LatticeNet, keep: np.ndarray) -> dict:
    """The lane-Z doorway signature: Δb1 of the punctured exterior vs the CLOSED
    box (same net). Δb1 = +k means k NEW source-free harmonic 1-cochain DOFs
    opened by the puncture (the fluxoid doorway if the generator LINKS the core)."""
    closed = betti_punctured(build_punctured(net, np.ones(net.n_nodes, bool)))
    punct = betti_punctured(build_punctured(net, keep))
    return {
        "closed_b1": closed["b1"], "punctured_b1": punct["b1"],
        "delta_b1": punct["b1"] - closed["b1"],
        "closed_b2": closed["b2"], "punctured_b2": punct["b2"],
        "delta_b2": punct["b2"] - closed["b2"],
        "removed_nodes": int((~keep).sum()),
        "b1_two_method_agree": punct["b1_two_method_agree"],
    }


def _emit(frame_N: int = 20) -> dict:
    """Reproduce the committed evidence rows (research/data/..._topology.json).

    Run: `python -m ave.topological.srs_dec_punctured`  (from src/ on PYTHONPATH).
    The numbers here MUST match the JSON evidence file (regression by eye + the
    keeper suite test_srs_dec_punctured.py)."""
    out = {}
    for L in (3, 4, 5):
        net = build_srs_net(L=L, enantiomorph="right")
        ball = {f"r{rb}": doorway_delta(net, ball_keep_mask(net, frame_N, rb))["delta_b1"]
                for rb in (2.5, 3.0, 3.5, 4.0)}
        tor = {f"rc{rc}": doorway_delta(net, torus_keep_mask(net, frame_N, rc))["delta_b1"]
               for rc in (1.8, 2.3, 2.8, 3.3)}
        out[f"L{L}"] = {"ball_delta_b1": ball, "torus_delta_b1": tor}
    return out


if __name__ == "__main__":
    import json

    print(json.dumps(_emit(), indent=2))

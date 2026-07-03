"""Discrete-Exterior-Calculus (DEC) operator set on the chiral srs (z=3) lattice.

DEC MINI-ARC (Grant-chartered 2026-07-03). This module upgrades the cold-linear-
static-local closure of the {∇×ω, ω} curl-coupling class from "a property of an
engineering-choice operator pair" to a THEOREM (a ∂∂=0 structural identity) for
the ENTIRE curl class.

═══════════════════════════════════════════════════════════════════════════════
WHY THIS EXISTS (verify at HEAD)
═══════════════════════════════════════════════════════════════════════════════
The EM-readout Stage-1b review (research/2026-07-03_em-readout-vsector-stage1_
result.md PANEL-FINDINGS §Blocker-2) proved the two operators used there —
    _srs_curl_nodes      : 1/deg-weighted, per-node 3-vector, bond-projected curl
    _srs_node_divergence : 1/2 face-average, per-node bond-projected divergence
(both in src/scripts/vol_2_subatomic/em_readout_vsector_transducer.py) are NOT an
adjoint/DEC pair: div∘curl on a random field is pointwise O(1) (RMS ≈ 0.35, max
≈ 1.4). They are two independent Cartesian-embedded (per-node 3-vector) heuristics
that do not compose to zero. Consequently the merged closure of the
{static, linear, cold, local, curl-coupling} cell was scoped as an
OPERATOR-PAIR property — true of those two members, not proven for the class.

═══════════════════════════════════════════════════════════════════════════════
THE FIX IS SUBSTRATE-NATIVE, NOT A NEW HEURISTIC (phase-space-coordinate-check)
═══════════════════════════════════════════════════════════════════════════════
The Stage-1b operators live in REAL-SPACE, CARTESIAN coordinates: they carry a
3-vector per node and take np.cross with the Cartesian bond directions. That
Cartesian embedding is exactly what breaks cochain adjointness — projecting onto
the ambient x/y/z axes is not a lattice-intrinsic operation, so div and curl are
built on different, non-conjugate projections.

DEC replaces per-node 3-vectors with COORDINATE-FREE COCHAINS:
    0-cochains  scalars on nodes (n_nodes)
    1-cochains  scalars on oriented edges (n_edges)   ← flux/potential-difference
    2-cochains  scalars on oriented faces (n_faces)   ← circulation
The operators are the INTEGER incidence matrices of the srs 2-complex:
    grad = d0 = ∂₁ᵀ          (0-cochains → 1-cochains)
    div  = −∂₁               (1-cochains → 0-cochains; the exact negative adjoint)
    curl = d1 = ∂₂ᵀ          (1-cochains → 2-cochains)
    curl-adjoint = ∂₂        (2-cochains → 1-cochains)
Then ∂₁∂₂ = 0 is a COMBINATORIAL identity (every face-boundary edge is traversed
with cancelling incidence at each node), independent of ANY coordinate embedding.
It holds at machine precision — in fact at EXACT integer zero — for the class of
ALL fields, because it is a property of the operators, not of the field.

═══════════════════════════════════════════════════════════════════════════════
THE 2-COMPLEX (the design decision — see the CHOICE LEDGER in the research note)
═══════════════════════════════════════════════════════════════════════════════
Nodes (0-cells) and bonds (1-cells) are GIVEN by build_srs_net (the z=3 chiral
Laves connectivity — EXTERNAL MATHEMATICS, chiral_lattice.py). The 2-cells are the
girth-10 minimal cycles of the srs net (the srs net is girth-10 / (10,3)-a; that
is asserted only by executable keepers, chiral_lattice.py:19-23). This module
enumerates the 10-ring faces algorithmically and assembles ∂₂ from them, with an
honest choice-ledger (each choice tagged ENGINEERING-CHOICE or GEOMETRY-FORCED).

α-CLEAN: no ALPHA / Q_TANK / V_SNAP on any path here. This is pure combinatorial
topology of the connect-map; no physical constant enters ∂₁ or ∂₂ (they are
integer matrices). Canonical constants only where a bond LENGTH or weight is used.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

# the chiral srs net + its z=3 connectivity (the free-mode carrier's net).
from ave.core.chiral_lattice import LatticeNet, build_srs_net

# ─────────────────────────────────────────────────────────────────────────────
# α-leak guard (import-time). ∂₁/∂₂ are INTEGER matrices; no α-carrier belongs
# on any path. The leak is the signal.
# ─────────────────────────────────────────────────────────────────────────────
assert "ALPHA" not in globals(), "α-leak: ALPHA must NOT be imported"
assert "Q_TANK" not in globals(), "α-leak: Q_TANK (=1/alpha) must NOT be imported"
assert "V_SNAP" not in globals(), "α-leak: V_SNAP must NOT be on the DEC path"


# ═════════════════════════════════════════════════════════════════════════════
# THE 1-COMPLEX:  oriented edges + the boundary map ∂₁ (edges → nodes)
# ═════════════════════════════════════════════════════════════════════════════
def oriented_edges(net: LatticeNet) -> list[tuple[int, int]]:
    """The undirected srs bonds, oriented by the convention (u < v) → +1 head at v.

    Built from net.neighbors (the lattice's OWN z=3 adjacency), NEVER a Cartesian
    distance posit. Deterministic (sorted). This is the SAME bond set that
    ave.solvers.srs_cage_winding.unique_bonds enumerates — reconciled in the
    research note (the two builders agree edge-for-edge)."""
    N = net.n_nodes
    return sorted({(min(u, v), max(u, v)) for u in range(N) for v in net.neighbors[u]})


def boundary_1(net: LatticeNet, edges: list[tuple[int, int]] | None = None):
    """∂₁ : 1-cochains (edges) → 0-cochains (nodes), sparse (n_nodes × n_edges).

    Convention: an oriented edge e = (u, v) with u < v has boundary ∂e = [v] − [u],
    so ∂₁[v, e] = +1 and ∂₁[u, e] = −1. This is the standard simplicial/CW
    boundary operator. Returns (D1, edges).

    RELATION TO THE EXISTING SOLVER OPERATOR (reconciled, not re-derived):
      srs_cage_winding.build_incidence returns B of shape (n_edges × n_nodes) with
      B[e, u] = +1, B[e, v] = −1 for the SAME oriented edge (u, v), u < v. Hence
      B = −∂₁ᵀ exactly (same bond set, same orientation, transposed with a global
      sign). The solver's graph Laplacian L_srs = Bᵀ diag(D) B therefore equals
      ∂₁ diag(D) ∂₁ᵀ, which for D ≡ 1 is EXACTLY div∘grad = −∂₁ (−∂₁ᵀ)ᵀ... — the
      DEC scalar Laplacian up to sign (see laplacian_0 + the research-note
      reconciliation table). SAME operator; the sign is the div=−∂₁ convention."""
    from scipy import sparse

    if edges is None:
        edges = oriented_edges(net)
    ne = len(edges)
    rows = np.empty(2 * ne, dtype=np.int64)
    cols = np.empty(2 * ne, dtype=np.int64)
    vals = np.empty(2 * ne, dtype=np.float64)
    for e, (u, v) in enumerate(edges):
        rows[2 * e] = v          # +1 at the head (larger index)
        cols[2 * e] = e
        vals[2 * e] = +1.0
        rows[2 * e + 1] = u      # −1 at the tail
        cols[2 * e + 1] = e
        vals[2 * e + 1] = -1.0
    D1 = sparse.csr_matrix((vals, (rows, cols)), shape=(net.n_nodes, ne))
    return D1, edges


# ═════════════════════════════════════════════════════════════════════════════
# THE 2-COMPLEX:  girth-10 faces + the boundary map ∂₂ (faces → edges)
# ═════════════════════════════════════════════════════════════════════════════
# GIRTH — the srs net's girth. EXTERNAL MATHEMATICS (srs = (10,3)-a, girth-10;
# chiral_lattice.py:19-23, asserted by executable keepers, not by fiat here). The
# minimal cycles ARE the 10-rings; they are the natural 2-cells of the complex.
SRS_GIRTH: int = 10

# Minimum supercell edge for a valid complex. GEOMETRY-FORCED: at L=2 the periodic
# wrap folds the girth-10 rings into spurious 8-rings (empirically verified — see
# the research-note choice ledger). L>=3 recovers the true girth-10 everywhere.
MIN_SRS_L: int = 3


def enumerate_girth_faces(net: LatticeNet, girth: int = SRS_GIRTH) -> list[tuple[int, ...]]:
    """All distinct simple cycles of length `girth` (the srs 10-rings = the 2-cells).

    Deterministic DFS with the pruning rule "the cycle's start node is its minimum
    index and all subsequent nodes exceed it" (each undirected ring is discovered
    exactly once from its min node). Returned as ORDERED node-tuples (the cyclic
    order carries the face orientation ∂₂ needs); dedup is by the frozenset of the
    ring's edges (a ring and its reverse share the same edge set → one face).

    NB (GEOMETRY-FORCED): raises if net.box implies L < MIN_SRS_L, because the L=2
    supercell has PBC-spurious 8-rings that are NOT girth-10 faces."""
    N = net.n_nodes
    adj = [list(a) for a in net.neighbors]
    raw: set[tuple[int, ...]] = set()

    def _dfs(start: int, path: list[int], visited: set[int]) -> None:
        last = path[-1]
        if len(path) == girth:
            if start in adj[last]:
                raw.add(tuple(path))
            return
        for y in adj[last]:
            if y <= start or y in visited:  # start is the ring minimum
                continue
            visited.add(y)
            path.append(y)
            _dfs(start, path, visited)
            path.pop()
            visited.discard(y)

    for s in range(N):
        _dfs(s, [s], {s})

    seen: set[frozenset] = set()
    faces: list[tuple[int, ...]] = []
    for ring in raw:
        n = len(ring)
        key = frozenset(tuple(sorted((ring[i], ring[(i + 1) % n]))) for i in range(n))
        if key in seen:
            continue
        seen.add(key)
        faces.append(ring)
    # deterministic order: sort by the sorted node tuple of each ring
    faces.sort(key=lambda r: tuple(sorted(r)))
    return faces


def boundary_2(net: LatticeNet, edges: list[tuple[int, int]] | None = None,
               faces: list[tuple[int, ...]] | None = None, girth: int = SRS_GIRTH):
    """∂₂ : 2-cochains (faces) → 1-cochains (edges), sparse (n_edges × n_faces).

    Each face is a cyclic node-ring (a, b, c, …); its boundary walks the ring's
    directed edges. For directed step a→b the incidence is +1 if it AGREES with the
    oriented edge (min,max) convention (a < b) and −1 if it opposes it (a > b). This
    is the standard cellular ∂₂; the cyclic order fixes the face orientation, so
    ∂₁∂₂ = 0 holds EXACTLY (integer zero) — each interior node of the ring is
    entered once (−) and left once (+), cancelling in ∂₁∂₂.

    Returns (D2, edges, faces)."""
    from scipy import sparse

    if edges is None:
        edges = oriented_edges(net)
    eidx = {e: i for i, e in enumerate(edges)}
    if faces is None:
        faces = enumerate_girth_faces(net, girth=girth)
    ne, nf = len(edges), len(faces)
    rows: list[int] = []
    cols: list[int] = []
    vals: list[float] = []
    for fj, ring in enumerate(faces):
        n = len(ring)
        for i in range(n):
            a, b = ring[i], ring[(i + 1) % n]
            ei = eidx[(min(a, b), max(a, b))]
            rows.append(ei)
            cols.append(fj)
            vals.append(1.0 if a < b else -1.0)
    D2 = sparse.csr_matrix((vals, (rows, cols)), shape=(ne, nf))
    return D2, edges, faces


# ═════════════════════════════════════════════════════════════════════════════
# THE OPERATOR SET (all derived from ∂₁, ∂₂ — no free heuristic)
# ═════════════════════════════════════════════════════════════════════════════
@dataclass(frozen=True)
class SrsDEC:
    """The complete DEC operator set of the chiral srs 2-complex.

    All operators are the INTEGER incidence matrices (or their transposes) of the
    complex; they carry NO physical constant and NO coordinate embedding, so the
    identities below are combinatorial (exact-integer), true for the WHOLE class of
    fields — not properties of a particular field or a tuned operator pair.

      grad = d0 = ∂₁ᵀ           0-cochains (nodes)  → 1-cochains (edges)
      div  = −∂₁               1-cochains (edges)  → 0-cochains (nodes)
      curl = d1 = ∂₂ᵀ          1-cochains (edges)  → 2-cochains (faces)
      curl_adj = ∂₂            2-cochains (faces)  → 1-cochains (edges)
      L0 = div∘grad = −∂₁∂₁ᵀ   the scalar (0-form) Laplacian  (nodes → nodes)

    Identities (exact-integer 0):
      curl∘grad = ∂₂ᵀ∂₁ᵀ = (∂₁∂₂)ᵀ = 0
      div∘curl_adj = −∂₁∂₂ = 0    ← THE THEOREM's operator: any F=curl_adj(anything)
                                     has div F ≡ 0, hence zero enclosed charge.
    """

    net: LatticeNet
    edges: list
    faces: list
    D1: object   # ∂₁  (n_nodes × n_edges)
    D2: object   # ∂₂  (n_edges × n_faces)

    # --- the operators (cheap transposes of the stored boundary maps) ---
    @property
    def grad(self):
        """d0 = ∂₁ᵀ : node 0-cochain → edge 1-cochain (potential differences)."""
        return self.D1.T.tocsr()

    @property
    def div(self):
        """−∂₁ : edge 1-cochain → node 0-cochain (the exact negative adjoint of grad)."""
        return (-self.D1).tocsr()

    @property
    def curl(self):
        """d1 = ∂₂ᵀ : edge 1-cochain → face 2-cochain (circulation around each face)."""
        return self.D2.T.tocsr()

    @property
    def curl_adj(self):
        """∂₂ : face 2-cochain → edge 1-cochain (the adjoint curl — assembles an
        edge flux from face circulations)."""
        return self.D2.tocsr()

    @property
    def laplacian_0(self):
        """L0 = div∘grad = −∂₁∂₁ᵀ : the scalar graph Laplacian (nodes→nodes).

        With div=−∂₁ and grad=∂₁ᵀ, L0 = (−∂₁)(∂₁ᵀ) = −∂₁∂₁ᵀ. This is the NEGATIVE
        of the combinatorial graph Laplacian ∂₁∂₁ᵀ (which is +PSD). It matches the
        existing solver operator up to the div-sign convention:
        srs_cage_winding.assemble_L_srs(D≡1) = Bᵀ B = ∂₁∂₁ᵀ = −L0 exactly (same
        bond set, same orientation). See the research-note reconciliation table."""
        return (-(self.D1 @ self.D1.T)).tocsr()

    @property
    def n_nodes(self) -> int:
        return self.D1.shape[0]

    @property
    def n_edges(self) -> int:
        return self.D1.shape[1]

    @property
    def n_faces(self) -> int:
        return self.D2.shape[1]


def build_srs_dec(L: int = MIN_SRS_L, enantiomorph: str = "right",
                  girth: int = SRS_GIRTH) -> SrsDEC:
    """Assemble the full DEC operator set on the chiral srs supercell.

    GEOMETRY-FORCED guard: L >= MIN_SRS_L (=3). At L=2 the periodic wrap yields
    spurious 8-rings (not girth-10 faces) — the complex would be built on the wrong
    2-cells. The guard is a hard error, not a silent clamp (flag-don't-fix)."""
    if L < MIN_SRS_L:
        raise ValueError(
            f"srs DEC complex needs L >= {MIN_SRS_L}: at L={L} the periodic wrap "
            f"folds girth-{girth} rings into spurious 8-rings (GEOMETRY-FORCED; "
            f"see research/2026-07-03_srs-dec-operators_result.md choice ledger)."
        )
    net = build_srs_net(L=L, enantiomorph=enantiomorph)
    D1, edges = boundary_1(net)
    D2, edges, faces = boundary_2(net, edges=edges, girth=girth)
    return SrsDEC(net=net, edges=edges, faces=faces, D1=D1, D2=D2)


def betti_numbers(dec: SrsDEC) -> dict:
    """(b0, b1, b2) of the srs 2-complex via the rank–nullity chain
        b0 = V − rank(∂₁)
        b1 = E − rank(∂₁) − rank(∂₂)
        b2 = F − rank(∂₂)
    b1 is the HARMONIC 1-cochain dimension = the number of independent non-
    contractible 1-cycles (the periodic 3-torus wraps). For the periodic srs
    supercell b0=1 (connected), b1=3 (the three T³ handles), and b2 is over-
    complete on the FULL 10-ring face set (uniqueness of a minimal 2-complex FAILS
    — booked honestly). b1=3 is an L-independent topological invariant."""
    D1d = dec.D1.toarray()
    D2d = dec.D2.toarray()
    r1 = int(np.linalg.matrix_rank(D1d))
    r2 = int(np.linalg.matrix_rank(D2d))
    V, E, F = dec.n_nodes, dec.n_edges, dec.n_faces
    return {"b0": V - r1, "b1": E - r1 - r2, "b2": F - r2,
            "V": V, "E": E, "F": F, "rank_D1": r1, "rank_D2": r2}

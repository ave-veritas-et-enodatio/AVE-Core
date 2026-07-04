"""
Genesis v9 — Chiral trivalent (srs / Laves / Sunada-K4) lattice scaffold.

PHASE-0 scaffold. NO genesis run. See
research/2026-06-11_genesis-v9-chiral-lattice_design.md for the substrate-native
walk, the §0 adjudication flag (v9 re-opens the 2026-06-07 lattice-net
resolution-of-record), and the citation ledger.

This module is the FUNDAMENTAL-GROUND-UP build (no cubic stencil reused):

  * the srs (degree-3 chiral Laves / (10,3)-a / Sunada-K4) net, BOTH
    enantiomorphs, built from the I4_1 32 Wyckoff-8a motif and tiled under PBC;
  * the canonical diamond (engine-"K4", degree-4, achiral) net as the control;
  * the trivalent scatter matrix DERIVED from Op5's shunt-junction reduction
    S_ij = 2/n - delta_ij  (canon instantiates only n=4: S_ij = 1/2 - delta_ij);
  * the universal CONNECT map (reverse-port index per directed edge), which
    generalises the canonical bipartite connect to a non-bipartite valence-3 net.

Geometric properties of the srs net (trivalent, 120 deg balanced bonds,
girth-10, I4_1 32 / I4_3 32 enantiomorph pair) are EXTERNAL MATHEMATICS
(source class: Sunada, "Crystals that nature might miss creating," Notices AMS
2008; RCSR `srs`; Wells (10,3)-a). They are asserted ONLY by the executable
keepers in tests/test_chiral_lattice_smokes.py, never by fiat.

Canon anchors (origin/main @ f6ffd98d, verified):
  Op5            manuscript/ave-kb/common/operators.md:45
  4-port scatter src/ave/core/k4_tlm.py:64-93 ; k4-tlm-simulator.md:24-32
  CONNECT        src/ave/core/k4_tlm.py:117-118
  diamond ports  src/ave/core/k4_tlm.py:101-119
  c0 = dx/(dt√2) k4-tlm-simulator.md:42
  constants      src/ave/core/constants.py:96-98,239 (Z_0, MU_0, EPSILON_0, L_NODE)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from itertools import product

import numpy as np

from ave.core.constants import C_0, EPSILON_0, L_NODE, MU_0, Z_0

# ─────────────────────────────────────────────────────────────────────────────
# srs (Laves / Sunada-K4 / (10,3)-a) motif — EXTERNAL MATHEMATICS
# I4_1 32 (#214), Wyckoff 8a. Native = right-handed enantiomorph.
# ─────────────────────────────────────────────────────────────────────────────
_SRS_8A = np.array(
    [
        (1 / 8, 1 / 8, 1 / 8),
        (3 / 8, 5 / 8, 7 / 8),
        (7 / 8, 3 / 8, 5 / 8),
        (5 / 8, 7 / 8, 3 / 8),
        (5 / 8, 5 / 8, 5 / 8),
        (7 / 8, 1 / 8, 3 / 8),
        (3 / 8, 7 / 8, 1 / 8),
        (1 / 8, 3 / 8, 7 / 8),
    ],
    dtype=float,
)
_SRS_NN = np.sqrt(2.0) / 4.0  # nearest-neighbour bond length in cell units


def srs_motif(enantiomorph: str = "right") -> np.ndarray:
    """8 fractional coords of the srs unit cell.

    enantiomorph='right' -> I4_1 32 (native); 'left' -> I4_3 32 mirror (x -> -x).
    """
    m = _SRS_8A.copy()
    if enantiomorph == "left":
        m = m.copy()
        m[:, 0] = -m[:, 0]
        m = np.mod(m, 1.0)
    elif enantiomorph != "right":
        raise ValueError("enantiomorph must be 'right' or 'left'")
    return m


# ─────────────────────────────────────────────────────────────────────────────
# Op5 trivalent scatter — DERIVED, new instantiation (canon: n=4 only)
# ─────────────────────────────────────────────────────────────────────────────
def scatter_matrix(n: int, z_local: float = 1.0) -> np.ndarray:
    """Equal-admittance shunt-junction scatter for an n-port node.

    Derived from Op5 [S] = (I + Y/Y0)^-1 (I - Y/Y0) via the shunt-node KCL
    reduction (see design doc §2.4):

        V_i = V_i^inc + V_i^ref = V (common node voltage, shunt)
        sum_i Y0 (V_i^inc - V_i^ref) = 0  (KCL)
        => V = (2/n) sum_j V_j^inc
        => S_ij = 2/n - delta_ij

    n=4 reduces to the canonical diamond S_ij = 1/2 - delta_ij (k4_tlm.py:64-93).
    n=3 gives S_ij = 2/3 - delta_ij = (2/3)J - I, which is orthogonal (S^2 = I).

    z_local is reserved for the strained-vacuum (Op14) case; Phase-0 is
    unstrained (z_local == 1.0). Uniform per-port admittance cancels, so the
    unstrained form holds for any uniform z_local.
    """
    if n < 2:
        raise ValueError("n must be >= 2")
    S = (2.0 / n) * np.ones((n, n), dtype=float) - np.eye(n, dtype=float)
    return S


# ─────────────────────────────────────────────────────────────────────────────
# Generic periodic net (positions + directed-edge CONNECT map)
# ─────────────────────────────────────────────────────────────────────────────
@dataclass
class LatticeNet:
    """A periodic lattice net: positions + adjacency + the TLM CONNECT map.

    neighbors[u]      : list of neighbour node indices (length = degree).
    reverse_port[u][p]: port index q on neighbours[u][p] of the reverse edge.
    bond_unit[u][p]   : minimum-image unit vector u -> neighbours[u][p].
    pos               : (N,3) Cartesian positions (cell units * a_cell).
    """

    name: str
    handedness: str
    degree: int
    pos: np.ndarray
    neighbors: list
    reverse_port: list
    bond_unit: list
    box: float
    a_cell: float = 1.0
    interior_mask: np.ndarray = field(default=None)
    # ENGINE-HARDENING item 5: the D1-ratified carrier this net speaks. Additive +
    # defaulted (backward-compatible: a net built without a carrier declaration reports
    # "unknown"). The builders set it (build_srs_net → "srs-z3"; build_diamond_net →
    # "diamond-z4-instrument"). See ave.core.carrier.Carrier for the vocabulary.
    carrier: str = "unknown"

    @property
    def n_nodes(self) -> int:
        return len(self.pos)

    def connect_index(self):
        """Flat (src -> dst) index arrays for vectorised CONNECT.

        Returns (src_flat, dst_flat) with src_flat[k] = u*d + p and
        dst_flat[k] = v*d + q, so V_new.flat[dst_flat] = V_ref.flat[src_flat].
        """
        d = self.degree
        src, dst = [], []
        for u in range(self.n_nodes):
            for p in range(len(self.neighbors[u])):
                v = self.neighbors[u][p]
                q = self.reverse_port[u][p]
                src.append(u * d + p)
                dst.append(v * d + q)
        return np.array(src, dtype=np.int64), np.array(dst, dtype=np.int64)


def _build_net_from_points(
    frac_pts: np.ndarray,
    box: float,
    nn_dist: float,
    expected_degree: int,
    name: str,
    handedness: str,
    a_cell: float = 1.0,
    nn_tol: float = 0.05,
    carrier: str = "unknown",
) -> LatticeNet:
    """Build a LatticeNet from fractional points under PBC (minimum image)."""
    from scipy.spatial import cKDTree

    pts = np.mod(frac_pts, box)
    tree = cKDTree(pts, boxsize=box)
    pairs = tree.query_pairs(nn_dist * (1.0 + nn_tol))
    n = len(pts)
    neighbors = [[] for _ in range(n)]
    bond_unit = [[] for _ in range(n)]
    for i, j in pairs:
        dij = pts[j] - pts[i]
        dij -= box * np.round(dij / box)  # minimum image
        u = dij / np.linalg.norm(dij)
        neighbors[i].append(j)
        bond_unit[i].append(u)
        neighbors[j].append(i)
        bond_unit[j].append(-u)
    # reverse-port resolution
    reverse_port = [[] for _ in range(n)]
    for u in range(n):
        for v in neighbors[u]:
            q = neighbors[v].index(u)
            reverse_port[u].append(q)
    deg = np.array([len(a) for a in neighbors])
    interior = deg == expected_degree
    return LatticeNet(
        name=name,
        handedness=handedness,
        degree=expected_degree,
        pos=pts * a_cell,
        neighbors=neighbors,
        reverse_port=reverse_port,
        bond_unit=bond_unit,
        box=box * a_cell,
        a_cell=a_cell,
        interior_mask=interior,
        carrier=carrier,
    )


def build_srs_net(L: int = 4, enantiomorph: str = "right", a_cell: float | None = None) -> LatticeNet:
    """Periodic srs net, L cubic cells per side. Degree-3, girth-10, chiral.

    a_cell defaults to 2*sqrt(2)*L_NODE so one NN bond == one node pitch L_NODE
    (design doc §2.5; engineering choice of supercell scale, tagged as such).
    """
    if a_cell is None:
        # dimensionless cell unit; smoke invariants are scale-free (design doc §2.5).
        # Physical scale: NN bond == L_NODE => a_cell_physical = 2*sqrt(2)*L_NODE.
        a_cell = 2.0 * np.sqrt(2.0)
    motif = srs_motif(enantiomorph)
    pts = []
    for cx, cy, cz in product(range(L), repeat=3):
        for m in motif:
            pts.append(m + np.array([cx, cy, cz], dtype=float))
    pts = np.array(pts)
    hand = "right (I4_1 32)" if enantiomorph == "right" else "left (I4_3 32)"
    return _build_net_from_points(
        pts,
        float(L),
        _SRS_NN,
        3,
        f"srs[{enantiomorph}]",
        hand,
        a_cell=a_cell,
        carrier="srs-z3",  # the D1-ratified production carrier (Axiom-1's object)
    )


# Canonical diamond ports (k4_tlm.py:101-114). A joins B via these; B via negatives.
_DIAMOND_PORTS = np.array([(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)], dtype=float)


def build_diamond_net(L: int = 4, a_cell: float | None = None) -> LatticeNet:
    """Canonical diamond (engine-'K4', degree-4, achiral) control net.

    A = all-even coords, B = all-odd. Adjacency is built from the EXPLICIT
    tetrahedral ports (k4_tlm.py:101-119), NOT a distance heuristic: a
    distance-sqrt(3) NN search wrongly grabs all 8 sign patterns (BCC-like
    degree-8), whereas the diamond bonds are exactly the 4 tetrahedral patterns.
    L must be even for clean PBC; L >= 4.
    """
    if L % 2 != 0 or L < 4:
        raise ValueError("diamond control needs even L >= 4 for clean PBC")
    if a_cell is None:
        a_cell = 1.0
    nodes, index = [], {}
    for i, j, k in product(range(L), repeat=3):
        all_even = i % 2 == 0 and j % 2 == 0 and k % 2 == 0
        all_odd = i % 2 == 1 and j % 2 == 1 and k % 2 == 1
        if all_even or all_odd:
            index[(i, j, k)] = len(nodes)
            nodes.append((i, j, k))
    pts = np.array(nodes, dtype=float)
    n = len(pts)
    neighbors = [[] for _ in range(n)]
    bond_unit = [[] for _ in range(n)]
    inv_sqrt3 = 1.0 / np.sqrt(3.0)
    for idx, (i, j, k) in enumerate(nodes):
        is_a = i % 2 == 0
        ports = _DIAMOND_PORTS if is_a else -_DIAMOND_PORTS
        for p in ports:
            nb = ((i + int(p[0])) % L, (j + int(p[1])) % L, (k + int(p[2])) % L)
            neighbors[idx].append(index[nb])
            bond_unit[idx].append(p * inv_sqrt3)
    reverse_port = [[] for _ in range(n)]
    for u in range(n):
        for v in neighbors[u]:
            reverse_port[u].append(neighbors[v].index(u))
    deg = np.array([len(a) for a in neighbors])
    return LatticeNet(
        name="diamond",
        handedness="achiral (Fd-3m)",
        degree=4,
        pos=pts * a_cell,
        neighbors=neighbors,
        reverse_port=reverse_port,
        bond_unit=bond_unit,
        box=float(L) * a_cell,
        a_cell=a_cell,
        interior_mask=(deg == 4),
        carrier="diamond-z4-instrument",  # NON-CANONICAL instrument (D1); consumers ack
    )


# ─────────────────────────────────────────────────────────────────────────────
# Scalar TLM (Smoke A) — scatter + connect, closed system
# ─────────────────────────────────────────────────────────────────────────────
def scalar_tlm_step(net: LatticeNet, V_inc: np.ndarray, S: np.ndarray, conn) -> np.ndarray:
    """One scatter+connect step. V_inc shape (N, degree). conn = net.connect_index()."""
    src_flat, dst_flat = conn
    V_ref = V_inc @ S.T  # per node: V_ref[u] = S @ V_inc[u]
    V_new = np.zeros_like(V_inc)
    V_new.flat[dst_flat] = V_ref.flat[src_flat]
    return V_new


def lattice_energy(V_inc: np.ndarray) -> float:
    """Closed-system TLM energy proxy: sum of squared incident amplitudes."""
    return float(np.sum(V_inc * V_inc))


# ─────────────────────────────────────────────────────────────────────────────
# Smoke B — optical-activity source term: writhe (helicity) of shortest circuits
#
# The reflection-ODD, frame-free, box-independent pseudoscalar. Optical activity
# (gyrotropy) is sourced by the net helicity of a medium's closed circuits — the
# chiral-antenna / wire-loop mechanism (k4-tlm-simulator wire loops; the canonical
# (2,3)-knot helicity picture). Phase-0 measures this SOURCE term robustly; the
# dynamical polarization-rotation of a propagating packet is the Phase-1 full
# vector-TLM deliverable (a wandering scalar-walk does not give a converged
# per-length rotation at Phase-0 — verified empirically, see design doc §3).
#
# Writhe is INDEPENDENT of traversal direction (reversing a closed curve leaves
# the Gauss double integral unchanged) and ODD under mirror (x -> -x flips sign),
# so ring writhes sum coherently without an orientation convention, and the sum
# vanishes identically for an achiral (centrosymmetric) net.
# ─────────────────────────────────────────────────────────────────────────────
def shortest_ring(net: LatticeNet, start: int):
    """Return one shortest cycle (node list) through `start`, found by BFS."""
    par = {start: -1}
    dist = {start: 0}
    q = [start]
    meet = None
    head = 0
    while head < len(q) and meet is None:
        u = q[head]
        head += 1
        for w in net.neighbors[u]:
            if w not in dist:
                dist[w] = dist[u] + 1
                par[w] = u
                q.append(w)
            elif w != par[u]:
                meet = (u, w)
                break
    if meet is None:
        return None

    def up(x):
        p = []
        while x != -1:
            p.append(x)
            x = par[x]
        return p

    a, b = up(meet[0]), up(meet[1])
    sa = set(a)
    lca = next(x for x in b if x in sa)
    return a[: a.index(lca) + 1] + b[: b.index(lca)][::-1]


def ring_coords(net: LatticeNet, ring) -> np.ndarray:
    """Minimum-image-unwrapped Cartesian coords of a ring (PBC-safe)."""
    P = [net.pos[ring[0]].copy()]
    for k in range(1, len(ring)):
        d = net.pos[ring[k]] - P[-1]
        d -= net.box * np.round(d / net.box)
        P.append(P[-1] + d)
    return np.array(P)


def _segment_writhe(p1, p2, p3, p4) -> float:
    """Banchoff signed solid-angle writhe contribution of two segments [p1,p2],[p3,p4]."""
    r13, r14, r23, r24 = p3 - p1, p4 - p1, p3 - p2, p4 - p2
    r12, r34 = p2 - p1, p4 - p3

    def _u(a, b):
        c = np.cross(a, b)
        n = np.linalg.norm(c)
        return c / n if n > 1e-12 else np.zeros(3)

    n1, n2, n3, n4 = _u(r13, r14), _u(r14, r24), _u(r24, r23), _u(r23, r13)

    def _asin(a, b):
        return np.arcsin(np.clip(np.dot(a, b), -1.0, 1.0))

    omega = _asin(n1, n2) + _asin(n2, n3) + _asin(n3, n4) + _asin(n4, n1)
    sgn = np.sign(np.dot(np.cross(r34, r12), r13))
    return float(omega * sgn / (4.0 * np.pi))


def ring_writhe(P: np.ndarray) -> float:
    """Discrete writhe (Klenin-Langowski / Banchoff) of a closed polygon P."""
    n = len(P)
    w = 0.0
    for i in range(n):
        for j in range(i + 2, n):
            if i == 0 and j == n - 1:
                continue  # skip closing-adjacent pair
            w += _segment_writhe(P[i], P[(i + 1) % n], P[j], P[(j + 1) % n])
    return 2.0 * w


def net_ring_writhe(net: LatticeNet, n_sample: int = 48):
    """Mean writhe over distinct shortest rings.

    Returns (mean, std, n_rings, (min_len, max_len)). The Smoke-B discriminator:
    nonzero + sign-flipped between enantiomorphs; identically zero on the achiral
    control. min_len/max_len double as the girth re-confirmation.
    """
    seen = set()
    writhes = []
    lengths = []
    starts = np.where(net.interior_mask)[0][:n_sample]
    for s in starts:
        ring = shortest_ring(net, int(s))
        if ring is None:
            continue
        key = frozenset(ring)
        if key in seen:
            continue
        seen.add(key)
        P = ring_coords(net, ring)
        writhes.append(ring_writhe(P))
        lengths.append(len(ring))
    writhes = np.array(writhes)
    if len(writhes) == 0:
        return 0.0, 0.0, 0, (0, 0)
    return float(writhes.mean()), float(writhes.std()), len(writhes), (min(lengths), max(lengths))


# ─────────────────────────────────────────────────────────────────────────────
# Parameter mapping from constants.py (ave-canonical-source)
# ─────────────────────────────────────────────────────────────────────────────
def bond_lc():
    """Per-bond L, C from canonical constants (Z_0 = sqrt(L/C), c0 = 1/sqrt(LC))."""
    # c0 per node pitch: a node pitch L_NODE traversed in tau = L_NODE / C_0
    # Z_0 = sqrt(L/C), c0 = 1/sqrt(LC) -> L = Z_0/c0, C = 1/(Z_0 c0) per unit length.
    c0 = C_0
    L_per = Z_0 / c0
    C_per = 1.0 / (Z_0 * c0)
    return {"Z_0": Z_0, "c0": c0, "L_per": L_per, "C_per": C_per, "ell_node": L_NODE, "mu_0": MU_0, "eps_0": EPSILON_0}

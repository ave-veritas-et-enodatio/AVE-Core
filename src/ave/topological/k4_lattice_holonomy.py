"""K4 lattice-holonomy operator — the double-cover from LATTICE CONNECTIVITY.

Carrier-sector PREREQUISITE (charter `_orchestration/2026-06-20_carrier-sector-charter.md`).

This is the substrate-native UPGRADE of the #299 spin double-cover probe
(`cosserat_field_3d.py::probe_spin_doublecover_holonomy`). The #299 probe's −I at
2π is produced by OP_B — the analytic axis-angle SU(2) rotor
`q_body = [cos(φ/2), axis·sin(φ/2)]` — so the −I is BAKED by the half-angle
convention; the lattice never enters. That makes #299 a *representability* result
("the substrate CAN host the double-cover"), not a *substrate-forced* one.

Here the double-cover EMERGES FROM CONNECTIVITY: frame-transport is composed
LINK-BY-LINK from the A4 port-permutation action on the REAL K4 connect-map
(`chiral_lattice.py::LatticeNet`, the diamond/"K4" net). Each link's rotation is
the A4 tetrahedral rotation read from the (port-out, port-in) bond labels — NOT
an angle plugged into an analytic rotor. The holonomy of a path is the ordered
product of the per-link SO(3)→SU(2) lifts. A closed link-path whose composed A4
rotation nets a 2π SO(3) loop lifts to −I; a contractible loop lifts to +I.

THE GROUP-THEORY ANCHOR (verify-before-cite 2026-06-20):
  K4 → A4 → 2T ⊂ SU(2): the K4 tetrahedral rotation group is T = A4 (order 12);
  its double cover is the binary tetrahedral group 2T ⊂ SU(2) (order 24); a 2π
  rotation lifts to −I, only 4π to +I.
    `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md:125-136` (§6)
  The 12 A4 elements are the even permutations of the 4 tetrahedral ports
  {p0,p1,p2,p3}; the 8 C3 vertex rotations (±120°) + 3 C2 edge rotations (180°)
  + identity.
    `k4-rotation-group.md:61-114` (§3-§4); ports `k4_tlm.py:80-86`.

ANTI-TAUTOLOGY (load-bearing — see `holonomy_of_path` / `connectivity_scramble`
and the `uses_analytic_qbody` report flag): the −I MUST come from the product of
lattice-link rotations, NOT from `q_body(2π)`. This module NEVER imports or calls
the OP_B analytic axis-angle rotor in `cosserat_field_3d.py`. Scrambling the
connectivity (the per-link A4 assignment) CHANGES the holonomy, proving it reads
the lattice, not a convention.

GUARDS (def-kn0t01 / master-equation.md:20):
  - Cosserat ω micro-rotation grade ONLY (T2); A1 ⊥ T2; NEVER wired into the A1
    (V_inc, V_ref) mass phasor.
  - SIGN-only readout. α-free: no −e / α / Q_TANK ever read.
  - Substrate-native (Ckpt-2): A4 port-permutations on the connect-map, NOT a
    Cartesian-FD rotation on a parity-mask.

HONEST SCOPE: Class-C. This is the lattice-holonomy machinery + the
double-cover-from-connectivity. It does NOT test exchange / spin-statistics (the
next gate) and does NOT establish dynamical selection. Claim: "the double-cover
emerges from connectivity," NOT "spin-statistics derived."
"""

from __future__ import annotations

import itertools

import numpy as np

# ─────────────────────────────────────────────────────────────────────────────
# The K4 tetrahedral port basis (k4-rotation-group.md:17 ; k4_tlm.py:80-86).
# These are the A→B sublattice bond directions; ‖p_j‖ = √3, p_i·p_j = −1 (i≠j).
# ─────────────────────────────────────────────────────────────────────────────
PORTS = np.array(
    [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)],
    dtype=np.float64,
)


# ─────────────────────────────────────────────────────────────────────────────
# A4 rotation from a port-permutation — read from the LATTICE GEOMETRY, never
# from an analytic axis-angle rotor.
# ─────────────────────────────────────────────────────────────────────────────
def _permutation_parity_even(perm: tuple[int, ...]) -> bool:
    """True iff `perm` is an even permutation (an A4 element)."""
    n = len(perm)
    inversions = 0
    for i in range(n):
        for j in range(i + 1, n):
            if perm[i] > perm[j]:
                inversions += 1
    return inversions % 2 == 0


def rotation_from_port_permutation(perm: tuple[int, ...]) -> np.ndarray:
    """The SO(3) rotation matrix R that sends port p_i → p_{perm[i]}.

    The 4 tetrahedral ports span R^3 (rank 3, centered at origin), so the
    orthogonal map realizing a tetrahedral SYMMETRY permutation is uniquely
    determined by R · PORTS.T = PORTS[perm].T. We solve it as R = B · A^+ where
    A = PORTS.T, B = PORTS[perm].T. For an even permutation (an A4 element) this
    is EXACTLY a proper rotation (orthogonal, det = +1); the routine asserts it.

    This is the substrate's own geometry: R is fixed by WHICH PORTS map to WHICH
    (the connect-map's combinatorics), NOT by any continuous angle parameter. No
    half-angle, no `cos(φ/2)` — the entire point of the anti-tautology guard.
    """
    if len(perm) != 4 or sorted(perm) != [0, 1, 2, 3]:
        raise ValueError(f"perm must be a permutation of (0,1,2,3); got {perm}")
    A = PORTS.T  # (3,4) source frame
    B = PORTS[list(perm)].T  # (3,4) target frame
    R = B @ np.linalg.pinv(A)
    # A4 elements (even perms) are proper rotations; odd perms are improper
    # (reflections, T_d \ T) — those are NOT lattice rotations and must not enter
    # a rotation-only (A4) holonomy. Reject them loudly (chord-discriminator).
    if not _permutation_parity_even(perm):
        raise ValueError(
            f"perm {perm} is ODD (a reflection in T_d \\ T); the chiral K4 "
            "rotation group is A4 (even perms only). A reflection is an ECHO, "
            "not a substrate rotation — refused."
        )
    if not np.allclose(R @ R.T, np.eye(3), atol=1e-9):
        raise AssertionError(f"perm {perm} did not yield an orthogonal R")
    if not np.isclose(np.linalg.det(R), 1.0, atol=1e-9):
        raise AssertionError(f"perm {perm} det={np.linalg.det(R)} (not +1)")
    return R


def a4_rotation_group() -> dict[tuple[int, ...], np.ndarray]:
    """The 12 A4 rotation matrices keyed by their port-permutation.

    1 identity + 8 C3 vertex rotations (±120°) + 3 C2 edge rotations (180°);
    all even permutations of {0,1,2,3} (k4-rotation-group.md §3-§4).
    """
    group = {}
    for perm in itertools.permutations(range(4)):
        if _permutation_parity_even(perm):
            group[perm] = rotation_from_port_permutation(perm)
    return group


# ─────────────────────────────────────────────────────────────────────────────
# SO(3) → SU(2) lift: matrix-to-quaternion of a FINITE rotation.
#
# This is NOT the OP_B analytic rotor. It does not take an angle φ; it takes a
# rotation MATRIX (already fixed by the port-permutation combinatorics) and reads
# off its unit-quaternion representative via the standard Shepperd construction.
# The double-cover sign then arises because the PRODUCT of these finite lifts can
# be −I even when the product of the matrices is the identity (the 2T cocycle),
# resolved by continuity along the path — never by a `cos(φ/2)` at φ = 2π.
# ─────────────────────────────────────────────────────────────────────────────
def rotation_matrix_to_quaternion(R: np.ndarray) -> np.ndarray:
    """Unit quaternion (w, x, y, z) of a proper rotation matrix R (Shepperd).

    Sign convention: returns the representative with w ≥ 0. The double-cover
    ambiguity (q vs −q) is resolved at COMPOSITION time by continuity along the
    path, NOT here — so the lift of a single finite lattice rotation is a pure
    function of its matrix.
    """
    R = np.asarray(R, dtype=np.float64)
    t = np.trace(R)
    if t > 0.0:
        s = np.sqrt(t + 1.0) * 2.0
        w = 0.25 * s
        x = (R[2, 1] - R[1, 2]) / s
        y = (R[0, 2] - R[2, 0]) / s
        z = (R[1, 0] - R[0, 1]) / s
    elif R[0, 0] > R[1, 1] and R[0, 0] > R[2, 2]:
        s = np.sqrt(1.0 + R[0, 0] - R[1, 1] - R[2, 2]) * 2.0
        w = (R[2, 1] - R[1, 2]) / s
        x = 0.25 * s
        y = (R[0, 1] + R[1, 0]) / s
        z = (R[0, 2] + R[2, 0]) / s
    elif R[1, 1] > R[2, 2]:
        s = np.sqrt(1.0 + R[1, 1] - R[0, 0] - R[2, 2]) * 2.0
        w = (R[0, 2] - R[2, 0]) / s
        x = (R[0, 1] + R[1, 0]) / s
        y = 0.25 * s
        z = (R[1, 2] + R[2, 1]) / s
    else:
        s = np.sqrt(1.0 + R[2, 2] - R[0, 0] - R[1, 1]) * 2.0
        w = (R[1, 0] - R[0, 1]) / s
        x = (R[0, 2] + R[2, 0]) / s
        y = (R[1, 2] + R[2, 1]) / s
        z = 0.25 * s
    q = np.array([w, x, y, z], dtype=np.float64)
    q = q / np.linalg.norm(q)
    if q[0] < 0.0:
        q = -q
    return q


def quat_mul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Hamilton product a ⊗ b of two unit quaternions (w, x, y, z)."""
    aw, ax, ay, az = a
    bw, bx, by, bz = b
    return np.array(
        [
            aw * bw - ax * bx - ay * by - az * bz,
            aw * bx + ax * bw + ay * bz - az * by,
            aw * by - ax * bz + ay * bw + az * bx,
            aw * bz + ax * by - ay * bx + az * bw,
        ],
        dtype=np.float64,
    )


_IDENTITY_QUAT = np.array([1.0, 0.0, 0.0, 0.0], dtype=np.float64)


# ─────────────────────────────────────────────────────────────────────────────
# The connection: a FLAT background + a seeded DISCLINATION defect.
#
# A genuine substrate-native double-cover must satisfy BOTH validate-on-known
# gates: (i) a contractible face → +I (zero curvature on faces), and (ii) a
# topologically nontrivial loop → −I. A *pure* flat connection gives +I on every
# loop → fails (ii); a per-link "always rotate" assignment gives curvature on
# every face → fails (i) (verified empirically: a real 6-ring came back −I — a
# clean Rule-10 integrator-time finding that killed the naive design).
#
# The honest object is the Finkelstein–Misner disclination: the connection is
# FLAT everywhere except across a "branch-cut" surface emanating from a seeded
# disclination DEFECT LINE. A link that CROSSES the cut carries the C3 vertex
# rotation (the disclination's Frank rotation, a 120° A4 element); all other
# links carry identity. A contractible loop crossing the cut an even-canceling
# number of times → +I. A loop ENCIRCLING the defect picks up the C3 rotation;
# encircling it three times nets a 2π SO(3) loop (R³ = I) whose SU(2) lift is −I.
#
# Every ingredient is read from the connect-map: which links cross the cut is a
# geometric/topological property of the lattice + the seeded defect, and the C3
# rotation is the port-permutation A4 element (NOT an analytic angle). The
# connectivity-SCRAMBLE test changes the cut-crossing set (or the Frank rotation)
# and the holonomy changes — proving it reads the lattice, not a convention.
# ─────────────────────────────────────────────────────────────────────────────

# The four C3 vertex 3-cycles (fixing port j, cycling the other three forward).
# These are the +120° vertex rotations of k4-rotation-group.md §3, indexed by the
# FIXED port j. Each is an even permutation (A4); R_j fixes the port-axis p_j;
# q_j has order 6 in SU(2) (q_j³ = −I) — the double-cover seed.
_VERTEX_3CYCLE = {
    0: (0, 2, 3, 1),  # fix 0, cycle 1→2→3→1
    1: (3, 1, 0, 2),  # fix 1, cycle 0→3→2→0  (even perm)
    2: (1, 3, 2, 0),  # fix 2, cycle 0→1→3→0  (even perm)
    3: (2, 0, 1, 3),  # fix 3, cycle 0→2→1→0  (even perm)
}

# Identity permutation (a flat link carries no rotation).
_IDENTITY_PERM = (0, 1, 2, 3)


def disclination_frank_permutation(frank_port: int = 0) -> tuple[int, ...]:
    """The Frank rotation of a wedge disclination = the C3 vertex 3-cycle.

    `frank_port` selects which tetrahedral vertex-axis the disclination's Frank
    vector lies along (k4-rotation-group.md §3 vertex class). The default port 0
    gives the (0,2,3,1) 120° rotation, lift q = ½(1,1,1,1), order 6 in SU(2).
    """
    return _VERTEX_3CYCLE[int(frank_port)]


def link_rotation_permutation(
    crosses_cut: bool,
    frank_port: int = 0,
    frank_override: tuple[int, ...] | None = None,
) -> tuple[int, ...]:
    """A4 port-permutation carried by a link: Frank rotation if it crosses the
    disclination's branch-cut, else identity.

    `frank_override` lets the connectivity-SCRAMBLE test substitute a DIFFERENT A4
    element (or even a reflection, which is then refused upstream) to prove the
    holonomy depends on the actual assignment.
    """
    if not crosses_cut:
        return _IDENTITY_PERM
    if frank_override is not None:
        return frank_override
    return disclination_frank_permutation(frank_port)


# ─────────────────────────────────────────────────────────────────────────────
# Branch-cut membership — a connect-map / geometry lookup.
#
# The disclination defect is a LINE along `defect_axis` through `defect_origin`.
# Its branch cut is a half-plane: the set of points on one side of the defect
# line in a chosen reference direction. A directed link (u → v) "crosses the cut"
# iff the bond passes through that half-plane — determined entirely by the two
# node POSITIONS (`net.pos`, the lattice geometry) relative to the seeded defect.
# ─────────────────────────────────────────────────────────────────────────────
def link_crosses_cut(
    pos_u: np.ndarray,
    pos_v: np.ndarray,
    defect_origin: np.ndarray,
    defect_axis: np.ndarray,
    cut_dir: np.ndarray,
) -> bool:
    """True iff the directed bond from `pos_u` to `pos_v` crosses the cut half-plane.

    PURE GEOMETRY (no PBC bookkeeping here): callers must pass endpoint positions
    already unwrapped into a single consistent frame (the walker tracks this).
    The cut is the half-plane through the defect line (origin `defect_origin`,
    direction `defect_axis`) on the `cut_dir` side. The bond crosses iff, in the
    plane ⟂ axis, the endpoints straddle the cut-line (perp-coord sign flips) and
    the perp=0 crossing point lies on the half-line (cdir-coord ≥ 0).
    """
    axis = np.asarray(defect_axis, dtype=np.float64)
    axis = axis / np.linalg.norm(axis)
    cdir = np.asarray(cut_dir, dtype=np.float64)
    cdir = cdir - np.dot(cdir, axis) * axis  # in-plane reference ray
    cdir = cdir / np.linalg.norm(cdir)
    perp = np.cross(axis, cdir)  # second in-plane basis (right-handed about axis)

    r_u = np.asarray(pos_u, dtype=np.float64) - defect_origin
    r_v = np.asarray(pos_v, dtype=np.float64) - defect_origin
    r_u = r_u - np.dot(r_u, axis) * axis
    r_v = r_v - np.dot(r_v, axis) * axis

    su, pu_ = np.dot(r_u, cdir), np.dot(r_u, perp)
    sv, pv_ = np.dot(r_v, cdir), np.dot(r_v, perp)

    if pu_ == pv_:
        return False
    if (pu_ > 0.0) == (pv_ > 0.0):
        return False  # same side of the cut line → no crossing
    t = pu_ / (pu_ - pv_)  # parameter where perp-coord = 0
    s_cross = su + t * (sv - su)
    return bool(s_cross >= 0.0)


# ─────────────────────────────────────────────────────────────────────────────
# Path holonomy — the ordered PRODUCT of per-link SU(2) lifts.
#
# `path` is a list of directed links; each link is (u, p_out): leave node u via
# port p_out. Arrival node v = net.neighbors[u][p_out] (a connect-map lookup).
# Each link's SU(2) lift is the matrix-to-quaternion of its A4 rotation (Frank
# rotation if it crosses the seeded disclination's cut, else identity), composed
# left-to-right with continuity-resolution of the q-vs-−q cover ambiguity — which
# is what lets a defect-encircling loop accumulate the −I of the 2T cover.
# ─────────────────────────────────────────────────────────────────────────────
def holonomy_of_path(
    net,
    path: list[tuple[int, int]],
    defect: dict | None = None,
    require_closed: bool = True,
    frank_override: tuple[int, ...] | None = None,
) -> dict:
    """Compose the SU(2) holonomy of a directed lattice path, link by link.

    `defect` (or None for the trivial flat connection) is a dict with keys
    `origin` (3,), `axis` (3,), `cut_dir` (3,), `frank_port` (int). A link is
    assigned the Frank C3 rotation iff it crosses the cut, else identity.

    ANTI-TAUTOLOGY (load-bearing): this builds each link matrix from the
    connect-map + node positions via `rotation_from_port_permutation`. It does
    NOT import or call the OP_B analytic axis-angle rotor `q_body` in
    `cosserat_field_3d.py`. No `cos(φ/2)`, no traversal-angle anywhere.

    Returns a dict: running SU(2) `q`, SO(3) `R`, `so3_is_identity`,
    `holonomy_sign` (+1 ⇒ +I, −1 ⇒ −I), `closed`, `n_cut_crossings`, and the
    per-link permutation trace.
    """
    if not path:
        raise ValueError("empty path")

    if defect is not None:
        origin = np.asarray(defect["origin"], dtype=np.float64)
        axis = np.asarray(defect["axis"], dtype=np.float64)
        cut_dir = np.asarray(defect["cut_dir"], dtype=np.float64)
        frank_port = int(defect.get("frank_port", 0))

    q_running = _IDENTITY_QUAT.copy()
    R_running = np.eye(3)
    node = path[0][0]
    start_node = node
    # Track the walker's UNWRAPPED position (PBC min-image accumulated along the
    # path) so the cut-crossing test sees a single consistent frame, not the
    # box-wrapped raw coordinates.
    pos = net.pos[node].copy()
    link_perms = []
    n_cut_crossings = 0

    for (u, p_out) in path:
        if u != node:
            raise ValueError(
                f"path discontinuity: link starts at {u} but walker is at {node}"
            )
        v = net.neighbors[u][p_out]
        # Unwrapped position of v (min-image step from the current unwrapped pos).
        step = net.pos[v] - net.pos[u]
        step -= net.box * np.round(step / net.box)
        pos_v = pos + step

        if defect is None:
            crosses = False
        else:
            crosses = link_crosses_cut(pos, pos_v, origin, axis, cut_dir)
        if crosses:
            n_cut_crossings += 1

        perm = link_rotation_permutation(
            crosses,
            frank_port=(frank_port if defect is not None else 0),
            frank_override=frank_override if crosses else None,
        )
        link_perms.append(perm)
        R_link = rotation_from_port_permutation(perm)
        q_link = rotation_matrix_to_quaternion(R_link)

        q_next = quat_mul(q_link, q_running)
        # Continuity-resolve q vs −q against the running product (track the cover).
        if np.dot(q_next, q_running) < 0.0:
            q_next = -q_next
        q_running = q_next
        R_running = R_link @ R_running
        node = v
        pos = pos_v

    closed = node == start_node
    if require_closed and not closed:
        raise ValueError(
            f"path not closed: started at {start_node}, ended at {node}"
        )

    so3_is_identity = bool(np.allclose(R_running, np.eye(3), atol=1e-9))
    sign = float(np.sign(q_running[0])) if abs(q_running[0]) > 1e-9 else 0.0

    return {
        "q": q_running,
        "R": R_running,
        "so3_is_identity": so3_is_identity,
        "holonomy_sign": sign,
        "closed": closed,
        "n_links": len(path),
        "n_cut_crossings": n_cut_crossings,
        "link_perms": link_perms,
        # Anti-tautology self-report: this code path never touches q_body.
        "uses_analytic_qbody": False,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Lattice-path generators — closed directed-link loops built from the connect-map.
# ─────────────────────────────────────────────────────────────────────────────
def shortest_closed_loop(net, start: int) -> list[tuple[int, int]]:
    """A shortest closed directed-link loop through `start` (a single lattice face).

    BFS tree + the first non-tree edge → the fundamental cycle. Returns the loop
    as a list of directed links (node, port_out). For the diamond net (girth 6)
    this is a 6-ring chair hexagon. Every step is a connect-map lookup.

    NOTE on lattice size: at L < 8 the diamond is small enough that the shortest
    fundamental cycle WRAPS the periodic torus (unwrapped diameter > box) rather
    than bounding a clean LOCAL face — use `loop_wraps_torus` to check, and
    L ≥ 8 for a contractible-face gate. The encircle-n holonomy is robust either
    way (it depends on the defect-cut crossings, not on locality).
    """
    from collections import deque

    parent = {start: None}
    parent_port = {start: None}
    dist = {start: 0}
    q = deque([start])
    nontree = None
    while q and nontree is None:
        u = q.popleft()
        for p, w in enumerate(net.neighbors[u]):
            if w not in dist:
                dist[w] = dist[u] + 1
                parent[w] = u
                parent_port[w] = p
                q.append(w)
            elif parent.get(u) != w:
                nontree = (u, p, w)
                break
    if nontree is None:
        raise ValueError(f"no cycle reachable from node {start}")
    u, p_uw, w = nontree

    def path_from_root(x):
        seq = []
        while parent[x] is not None:
            seq.append((parent[x], parent_port[x]))  # directed link parent→x
            x = parent[x]
        return seq[::-1]

    def reverse_link(a, p):
        return (net.neighbors[a][p], net.reverse_port[a][p])

    pu = path_from_root(u)  # start → … → u
    pw = path_from_root(w)  # start → … → w
    return pu + [(u, p_uw)] + [reverse_link(a, p) for (a, p) in reversed(pw)]


def loop_wraps_torus(net, loop: list[tuple[int, int]]) -> bool:
    """True iff the loop's unwrapped extent exceeds the box (a PBC-wrapping cycle).

    A wrapping loop is not a clean local face; the contractible-face gate needs a
    non-wrapping loop (L ≥ 8 for the diamond). See `shortest_closed_loop` note.
    """
    nodes = [u for (u, _p) in loop]
    pts = [net.pos[nodes[0]].copy()]
    for nd in nodes[1:]:
        d = net.pos[nd] - pts[-1]
        d -= net.box * np.round(d / net.box)
        pts.append(pts[-1] + d)
    pts = np.array(pts)
    diam = float(np.max([np.linalg.norm(a - b) for a in pts for b in pts]))
    return diam > net.box - 1e-6


def repeat_loop(loop: list[tuple[int, int]], n: int) -> list[tuple[int, int]]:
    """Traverse a closed loop `n` times (the encircle-n-times path).

    Encircling a disclination once accumulates the Frank C3 rotation (120°); three
    times nets a 2π SO(3) loop (R³ = I) whose SU(2) lift is −I — the
    double-cover from connectivity.
    """
    return loop * int(n)


def loop_centroid(net, loop: list[tuple[int, int]]) -> np.ndarray:
    """Min-image-unwrapped centroid of a loop's node positions (defect seed point)."""
    nodes = [u for (u, _p) in loop]
    base = net.pos[nodes[0]].copy()
    acc = base.copy()
    prev = base.copy()
    for nd in nodes[1:]:
        d = net.pos[nd] - prev
        d -= net.box * np.round(d / net.box)
        prev = prev + d
        acc = acc + prev
    return acc / len(nodes)


def loop_plane(net, loop: list[tuple[int, int]]) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Best-fit plane of a loop: returns (centroid, normal, in_plane_dir).

    The disclination defect line is seeded along `normal` through `centroid`; the
    branch cut is the half-plane on the `in_plane_dir` side. All from the loop's
    own node geometry (`net.pos`), a connect-map-derived quantity.
    """
    nodes = [u for (u, _p) in loop]
    pts = [net.pos[nodes[0]].copy()]
    for nd in nodes[1:]:
        d = net.pos[nd] - pts[-1]
        d -= net.box * np.round(d / net.box)
        pts.append(pts[-1] + d)
    pts = np.array(pts)
    centroid = pts.mean(axis=0)
    _, _, vt = np.linalg.svd(pts - centroid)
    return centroid, vt[-1], vt[0]


# ─────────────────────────────────────────────────────────────────────────────
# Anti-tautology checker — AST proof that NO analytic axis-angle rotor is used.
#
# The #299 substrate-blindness lives in OP_B's continuous axis-angle rotor
# (the half-angle quaternion of a traversal parameter) and its helpers
# (_axis_angle_to_rotation, _omega_to_quaternion) in the cosserat field module.
# This checker parses THIS module's AST and asserts: (1) it does not import the
# cosserat field module; (2) it never calls those rotor helpers; (3) the rotor's
# parameter-name token does not appear as a code-level NAME (only in docstrings).
# A docstring grep would false-positive on our own anti-tautology prose, so we use
# the AST — comments and docstrings are not in the AST's Name/Call/Import nodes.
# ─────────────────────────────────────────────────────────────────────────────
def uses_analytic_qbody() -> bool:
    """True iff this module's executable code imports/calls the analytic rotor.

    Returns False for the substrate-native build (the −I comes from lattice-link
    A4 rotations, not an analytic half-angle rotor). If this ever returns True,
    the holonomy is convention-baked → the result must HALT (report the tautology).
    """
    import ast
    import inspect

    this_module = inspect.getmodule(uses_analytic_qbody)
    src = inspect.getsource(this_module)
    tree = ast.parse(src)

    forbidden_calls = {"_axis_angle_to_rotation", "_omega_to_quaternion"}
    # The analytic rotor's traversal-parameter quaternion variable name, assembled
    # so this very source line is not itself a literal tripwire for a naive grep.
    forbidden_name = "q" + "_body"

    imported_cosserat = False
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module and "cosserat_field_3d" in node.module:
            imported_cosserat = True
        if isinstance(node, ast.Import):
            for alias in node.names:
                if "cosserat_field_3d" in alias.name:
                    imported_cosserat = True
        if isinstance(node, ast.Call):
            f = node.func
            attr = f.id if isinstance(f, ast.Name) else (f.attr if isinstance(f, ast.Attribute) else "")
            if attr in forbidden_calls:
                return True
        if isinstance(node, ast.Name) and node.id == forbidden_name:
            return True
    return imported_cosserat


# ─────────────────────────────────────────────────────────────────────────────
# Top-level probe — bundles validate-on-known + the two anti-tautology proofs.
# ─────────────────────────────────────────────────────────────────────────────
def probe_lattice_doublecover(L: int = 8) -> dict:
    """Run the full carrier-sector prerequisite gate on the diamond ('K4') net.

    Validate-on-known:
      (i)  CONTRACTIBLE loop (defect outside) → holonomy = +I.
      (ii) 2π-effecting closed path (encircle the seeded disclination 3×, netting
           a 2π SO(3) loop) → holonomy = −I; the double-cover FROM CONNECTIVITY.

    Anti-tautology:
      (a) `uses_analytic_qbody` is False (AST proof — no analytic rotor).
      (b) scrambling the per-link Frank assignment (→ identity) CHANGES the −I to
          +I, proving the holonomy reads the lattice not a convention.

    Returns a verdict dict. VERDICT = PASS only if (i) +I, (ii) −I (with R = I at
    3× and the single-encirclement giving the C3 120° rotation), (a) no rotor,
    (b) scramble changes the sign. HALT if `uses_analytic_qbody` is True.
    """
    from ave.core.chiral_lattice import build_diamond_net

    net = build_diamond_net(L=L)
    loop = shortest_closed_loop(net, 0)
    centroid, normal, in_plane = loop_plane(net, loop)
    defect = {"origin": centroid, "axis": normal, "cut_dir": in_plane, "frank_port": 0}

    # (i) contractible — defect shifted out of the loop along the in-plane dir.
    defect_out = {
        "origin": centroid + in_plane * net.box * 0.5,
        "axis": normal,
        "cut_dir": in_plane,
        "frank_port": 0,
    }
    contractible = holonomy_of_path(net, loop, defect=defect_out)

    # (ii) encircle 1× (C3) and 3× (2π → −I).
    enc1 = holonomy_of_path(net, repeat_loop(loop, 1), defect=defect)
    enc3 = holonomy_of_path(net, repeat_loop(loop, 3), defect=defect)
    enc6 = holonomy_of_path(net, repeat_loop(loop, 6), defect=defect)

    # (b) scramble: Frank rotation → identity ⇒ −I must vanish.
    scrambled = holonomy_of_path(
        net, repeat_loop(loop, 3), defect=defect, frank_override=(0, 1, 2, 3)
    )

    rotor = uses_analytic_qbody()

    if rotor:
        verdict = "HALT"  # convention-baked — the tautology the design must avoid
    elif (
        contractible["holonomy_sign"] > 0.0
        and contractible["n_cut_crossings"] == 0
        and enc3["holonomy_sign"] < 0.0
        and enc3["so3_is_identity"]
        and not enc1["so3_is_identity"]  # single encircle is the genuine C3, not I
        and enc6["holonomy_sign"] > 0.0  # 4π-equivalent return
        and scrambled["holonomy_sign"] > 0.0  # scramble killed the −I
    ):
        verdict = "PASS"
    else:
        verdict = "FAIL"

    return {
        "verdict": verdict,
        "L": L,
        "loop_n_links": len(loop),
        "contractible_sign": contractible["holonomy_sign"],
        "contractible_cuts": contractible["n_cut_crossings"],
        "encircle1_sign": enc1["holonomy_sign"],
        "encircle1_so3_is_identity": enc1["so3_is_identity"],
        "encircle1_q": enc1["q"],
        "encircle3_sign": enc3["holonomy_sign"],
        "encircle3_so3_is_identity": enc3["so3_is_identity"],
        "encircle3_q": enc3["q"],
        "encircle6_sign": enc6["holonomy_sign"],
        "scrambled_sign": scrambled["holonomy_sign"],
        "scramble_changes_holonomy": (
            enc3["holonomy_sign"] != scrambled["holonomy_sign"]
        ),
        "uses_analytic_qbody": rotor,
    }

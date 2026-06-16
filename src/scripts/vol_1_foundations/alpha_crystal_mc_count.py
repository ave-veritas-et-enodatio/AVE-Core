"""
Exact Maxwell-Calladine constraint count of the achiral diamond (z=4) K4 crystal.

Settles: does an EXACT Maxwell-Calladine constraint count (floppy modes
f = DOF - rank(R); states of self-stress s = #constraints - rank(R)) on the
alpha-FREE over-braced achiral diamond K4 crystal yield an effective
independent-constraint coordination z_eff that maps to the electron's
alpha^-1 = 137.036 via an alpha-FREE map -- or does it land the *additive*
~16 (-> 1/alpha ~ 49 only via the circular FTG-EMT), confirming that
z0 = 52 -> 137 was a PATH-COUNT CONVENTION dressed with the 8*pi*alpha
identity, never a constraint count?

PREREG: research/2026-06-15_alpha-crystal-mc-count_prereg_FROZEN.md (Rule-11).
RESULT: research/2026-06-15_alpha-crystal-mc-count_result.md.

------------------------------------------------------------------------------
ALPHA-FREE DISCIPLINE (load-bearing -- prereg Q1, Q6):
------------------------------------------------------------------------------
This module computes a RAW geometric constraint count. It takes NO alpha-bearing
input. To enforce that mechanically it runs an IMPORT-GRAPH GUARD at import time:

    assert 'ave.core' not in sys.modules

This is STRONGER than verify_universe.py's literal-float scan: it forbids the
alpha-bearing constants module (`ave.core.constants` defines P_C = 8*pi*alpha,
Z_COORDINATION ~ 51.25 via the circular FTG-EMT quadratic, RR_GOLDEN_TORUS = 1/4,
ALPHA_COLD_INV = 4*pi^3 + pi^2 + pi) from EVER being on the import graph of the
count. Consequence: the diamond net is REBUILT standalone here (integer lattice +
the 4 tetrahedral ports + 1/sqrt(3) bond units), NOT imported from
`ave.core.chiral_lattice.build_diamond_net` (which imports `ave.core.constants`).
The diamond topology is byte-for-byte the same construction (A=all-even,
B=all-odd, the same _DIAMOND_PORTS, PBC); it is verified identical against
build_diamond_net's adjacency in __main__ (which is allowed to import ave.core,
since __main__ runs AFTER the count module is built and is exempt from
verify_universe's float scan).

USABLE alpha-free constants only:
    |T| = 12   (diamond 2nd-neighbour shell size; 4 B-neighbours x 3 other-A
                sublattices = the 12 graph-2-hop A-nodes)
    N_K4 = 4   (diamond coordination)
    bare pi / 8*pi  (tainted the moment routed through P_C)

FORBIDDEN inputs (none appear, by construction + the import guard):
    alpha, P_C = 8*pi*alpha, Z_COORDINATION = 51.25, 1.187 / C_ratio,
    RR_GOLDEN_TORUS = 1/4, ALPHA_COLD_INV = 4*pi^3 + pi^2 + pi.

CODATA alpha^-1 appears ONLY in __main__ (exempt from the float scan) and the
result doc, as a ONE-WAY comparison target -- never fed into the count.

The deprecated stochastic-disorder route (amorphous random points + dilution
percolation p_c + "1/alpha = 8*pi/p_c", as in derive_alpha_m4_pro.py and
boinc_alpha_derivation.cpp) is NOT used: it is exactly the smuggle the prereg
forbids (8*pi/p_c being type-correct for 1/alpha ONLY in the dilution form IS
the tell). This module reuses ONLY the directional-cosine ROW-ASSEMBLY pattern
of build_sparse_rigidity_matrix, fed EXPLICIT crystal bonds, never a KD-tree
radius query over random points.

------------------------------------------------------------------------------
SUBSTRATE-NATIVE WALK (done before this code; substrate-native-check):
------------------------------------------------------------------------------
  CP1 dynamics: NOT a time-domain wave propagation, NOT energy minimization.
                A STATIC linear-algebra rank computation on the compatibility/
                rigidity matrix R. The Maxwell-Calladine count IS the
                AVE-native object (floppy modes + self-stress states of the
                bond network). No Lagrangian / gradient-descent / Hessian-of-W.
  CP2 sector:   K4 connectivity sector (bond topology). The 6N micropolar
                variant adds the Cosserat micro-rotation DOF as a sensitivity
                check.
  CP3 objective: constraint count / rank(R), NOT energy minimization.
  CP4 coords:   REAL-SPACE BULK count. The electron's alpha is a PHASE-SPACE /
                BOUNDARY Q. A bulk-z_eff -> boundary-alpha link is itself an
                OPEN PROJECTION QUESTION -- flagged in the result doc.
  CP10 boundary: PBC handles the boundary; no saturation/confinement bulk term.

ave-driver-script-honesty: this driver FORWARD-COMPUTES rank(R) exactly (no
minimize / curve_fit / target-fit anywhere). The honest deliverable is whatever
z_eff comes out -- including the expected ECHO. No manufactured map to 137.
"""

from __future__ import annotations

import sys

# -- IMPORT-GRAPH GUARD (alpha-free, prereg Q6) -------------------------------
# Stronger than verify_universe.py's literal scan: forbid the alpha-bearing
# constants module from being on this module's import graph at all.
assert "ave.core" not in sys.modules, (
    "alpha-free guard tripped: ave.core is already imported when "
    "alpha_crystal_mc_count was imported. This module must compute a RAW "
    "geometric constraint count with NO alpha-bearing input on its import "
    "graph (ave.core.constants defines P_C = 8*pi*alpha, Z_COORDINATION ~ "
    "51.25, RR_GOLDEN_TORUS = 1/4, ALPHA_COLD_INV = 4*pi^3+pi^2+pi)."
)

from dataclasses import dataclass
from itertools import product

import numpy as np

# alpha-free structural constants (prereg Q6)
ABS_T = 12  # |T| -- diamond 2nd-neighbour shell size
N_K4 = 4    # diamond coordination


# =============================================================================
# Diamond net -- STANDALONE rebuild (NO ave.core import; topology identical to
# ave.core.chiral_lattice.build_diamond_net). The 4 tetrahedral ports are pure
# sign patterns; the bond unit vectors are p / sqrt(3); A=all-even, B=all-odd.
# =============================================================================

# Canonical diamond ports (k4_tlm.py:101-114; chiral_lattice.py:222-224).
# A joins B via these; B joins A via their negatives.
_DIAMOND_PORTS = np.array(
    [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)], dtype=float
)


@dataclass
class DiamondNet:
    """Periodic diamond (z=4 K4) net: positions + 1st-neighbour adjacency.

    pos        : (N,3) integer-lattice coords (cell units).
    neighbors  : neighbors[u] = list of 1st-neighbour node indices (len 4).
    index      : {(i,j,k): node_idx}.
    nodes      : list of (i,j,k) integer coords.
    L          : supercell size (cells per side).
    """

    L: int
    pos: np.ndarray
    neighbors: list
    index: dict
    nodes: list

    @property
    def n_nodes(self) -> int:
        return len(self.nodes)


def build_diamond_net_standalone(L: int) -> DiamondNet:
    """Diamond (z=4) net, L cells/side, PBC. NO ave.core import.

    Mirrors ave.core.chiral_lattice.build_diamond_net EXACTLY: nodes are the
    all-even (A) and all-odd (B) integer sites; bonds are the 4 explicit
    tetrahedral ports (NOT a distance heuristic -- a sqrt(3) NN search wrongly
    grabs all 8 sign patterns). L must be even >= 4 for clean PBC.
    """
    if L % 2 != 0 or L < 4:
        raise ValueError("diamond net needs even L >= 4 for clean PBC")
    nodes: list = []
    index: dict = {}
    for (i, j, k) in product(range(L), repeat=3):
        all_even = i % 2 == 0 and j % 2 == 0 and k % 2 == 0
        all_odd = i % 2 == 1 and j % 2 == 1 and k % 2 == 1
        if all_even or all_odd:
            index[(i, j, k)] = len(nodes)
            nodes.append((i, j, k))
    n = len(nodes)
    neighbors = [[] for _ in range(n)]
    for idx, (i, j, k) in enumerate(nodes):
        is_a = i % 2 == 0
        ports = _DIAMOND_PORTS if is_a else -_DIAMOND_PORTS
        for p in ports:
            nb = ((i + int(p[0])) % L, (j + int(p[1])) % L, (k + int(p[2])) % L)
            neighbors[idx].append(index[nb])
    pos = np.array(nodes, dtype=float)
    return DiamondNet(L=L, pos=pos, neighbors=neighbors, index=index, nodes=nodes)


def _min_image_disp(net: DiamondNet, u: int, v: int) -> np.ndarray:
    """Minimum-image displacement u -> v in integer cell units (PBC, box=L)."""
    d = net.pos[v] - net.pos[u]
    d -= net.L * np.round(d / net.L)
    return d


# A "bond" carries both endpoints AND its minimum-image integer displacement, so
# that two DISTINCT geometric edges between the same node pair (possible under a
# small PBC supercell, where 2-hop paths wrap differently) are NOT collapsed.
# Bond = (i, j, dx, dy, dz) with i < j and (dx,dy,dz) the min-image disp i->j
# canonicalised to the i<j orientation. Tuple-keyed for exact set dedup.

def _bond_key(net: DiamondNet, u: int, v: int):
    if u <= v:
        d = _min_image_disp(net, u, v)
        return (u, v, int(round(d[0])), int(round(d[1])), int(round(d[2])))
    d = _min_image_disp(net, v, u)
    return (v, u, int(round(d[0])), int(round(d[1])), int(round(d[2])))


def first_neighbour_bonds(net: DiamondNet) -> list:
    """1st-neighbour bonds as (i, j, dx, dy, dz) keys, i <= j, deduped.

    The z=4 primary (central-force) network. Each A-B tetrahedral edge once,
    geometrically distinct by min-image displacement.
    """
    bonds = set()
    for u in range(net.n_nodes):
        for v in net.neighbors[u]:
            bonds.add(_bond_key(net, u, v))
    return sorted(bonds)


def second_neighbour_bonds(net: DiamondNet) -> list:
    """2nd-neighbour bonds as (i, j, dx, dy, dz) keys, i <= j, deduped.

    The crystallographic 2nd-neighbour shell: each node's |T| = 12 graph-2-hop
    same-sublattice neighbours (4 first-neighbours x 3 OTHER first-neighbours of
    each = the 12 atoms at sqrt(8/3)*ell_node). This is the alpha-FREE
    over-bracing secondary network (prereg Q3 / Method 3): specified
    TOPOLOGICALLY (which shell), NEVER by an alpha-bearing length ratio.
    NO 1.187, NO C_ratio, NO p_c.

    Deduped by (node-pair, min-image displacement): two 2-hop paths that land on
    the same node pair via the SAME geometric displacement are one bond; paths
    that wrap to DIFFERENT displacements (small-PBC artifact) are distinct bonds.
    """
    bonds = set()
    for u in range(net.n_nodes):
        nbrs = net.neighbors[u]
        for mid in nbrs:
            for w in net.neighbors[mid]:
                if w == u:
                    continue
                bonds.add(_bond_key(net, u, w))
    return sorted(bonds)


# =============================================================================
# Rigidity / compatibility matrix assembly.
# Reuses ONLY the directional-cosine row pattern of
# derive_alpha_m4_pro.py::build_sparse_rigidity_matrix (the +-n_hat rows), fed
# EXPLICIT crystal bonds (NOT a KD-tree radius query over random points). The
# amorphous/dilution machinery of that file is NOT used.
# =============================================================================

def build_central_force_rigidity(net: DiamondNet, bonds: list) -> np.ndarray:
    """Central-force rigidity matrix R: rows = bonds, cols = 3N translational DOF.

    Row b for bond (i, j) with min-image unit vector n = (pos_j - pos_i)/|...|:
        R[b, 3i:3i+3] = -n ;  R[b, 3j:3j+3] = +n
    (the derive_alpha_m4_pro.py directional-cosine pattern). A central-force bond
    constrains ONE scalar (the bond-length change), hence ONE row.
    """
    n_nodes = net.n_nodes
    n_bonds = len(bonds)
    R = np.zeros((n_bonds, 3 * n_nodes), dtype=float)
    for b, (i, j, dx, dy, dz) in enumerate(bonds):
        d = np.array([dx, dy, dz], dtype=float)  # min-image disp i->j
        nrm = np.linalg.norm(d)
        if nrm == 0.0:
            continue
        nhat = d / nrm
        R[b, 3 * i : 3 * i + 3] = -nhat
        R[b, 3 * j : 3 * j + 3] = +nhat
    return R


def build_micropolar_rigidity(net: DiamondNet, bonds: list) -> np.ndarray:
    """6N micropolar (Cosserat) rigidity matrix -- SENSITIVITY VARIANT.

    DOF per node: 3 translation (u) + 3 micro-rotation (phi). A Cosserat bond
    couples the relative translation to the average micro-rotation across the
    bond, constraining the transverse (shear) relative motion as well as the
    axial. We model each bond as constraining all 3 components of the relative
    GENERALISED displacement at the bond midpoint:

        g = (u_j - u_i) - (1/2)(phi_i + phi_j) x r_ij

    where r_ij = (pos_j - pos_i) min-image. This yields 3 rows per bond (the
    full vector compatibility), the standard Cosserat-rod / micropolar-lattice
    constraint. (Central-force keeps only the n.g axial projection -> 1 row.)

    DOF ordering per node n: [u_x,u_y,u_z, phi_x,phi_y,phi_z] at cols 6n..6n+5.
    """
    n_nodes = net.n_nodes
    n_bonds = len(bonds)
    R = np.zeros((3 * n_bonds, 6 * n_nodes), dtype=float)
    for b, (i, j, dx, dy, dz) in enumerate(bonds):
        r = np.array([dx, dy, dz], dtype=float)  # r_ij = pos_j - pos_i (min img)
        # relative translation: +I on u_j, -I on u_i
        for c in range(3):
            R[3 * b + c, 6 * i + c] += -1.0
            R[3 * b + c, 6 * j + c] += +1.0
        # -(1/2)(phi_i + phi_j) x r  ->  rotation couples via the cross-product
        # [a x r]_c = sum_d eps[c,d,e] a_d r_e ; d(g_c)/d(phi_*) = -1/2 * [e x r]
        # cross-product matrix Cx such that (a x r) = Cx @ a:
        Cx = np.array(
            [
                [0.0, r[2], -r[1]],
                [-r[2], 0.0, r[0]],
                [r[1], -r[0], 0.0],
            ]
        )
        # g_c -= 1/2 (phi_i + phi_j) x r  => d g / d phi_i = -1/2 Cx, same for j
        R[3 * b : 3 * b + 3, 6 * i + 3 : 6 * i + 6] += -0.5 * Cx
        R[3 * b : 3 * b + 3, 6 * j + 3 : 6 * j + 6] += -0.5 * Cx
    return R


# =============================================================================
# Exact Maxwell-Calladine count.
# =============================================================================

def exact_rank(R: np.ndarray) -> int:
    """Exact numerical rank via SVD (tractable for these supercells: largest is
    768 x 768 at L=8 micropolar). rcond chosen against the largest singular
    value -- a hard floppy/rigid gap is expected for an exact crystal, so the
    rank is robust to the cutoff (verified by reporting the singular-value gap).
    """
    if R.size == 0:
        return 0
    s = np.linalg.svd(R, compute_uv=False)
    if s.size == 0:
        return 0
    tol = s.max() * max(R.shape) * np.finfo(float).eps
    return int(np.sum(s > tol))


def singular_value_gap(R: np.ndarray) -> tuple:
    """(smallest nonzero singular value, largest zero-cluster value, ratio) for
    audit of the rank cutoff robustness. Returns (s_min_nonzero, s_max_zero,
    gap_ratio) where gap_ratio = s_min_nonzero / s_max_zero (inf if no zeros)."""
    if R.size == 0:
        return (0.0, 0.0, float("inf"))
    s = np.linalg.svd(R, compute_uv=False)
    tol = s.max() * max(R.shape) * np.finfo(float).eps
    nonzero = s[s > tol]
    zero = s[s <= tol]
    s_min_nz = float(nonzero.min()) if nonzero.size else 0.0
    s_max_z = float(zero.max()) if zero.size else 0.0
    gap = (s_min_nz / s_max_z) if s_max_z > 0 else float("inf")
    return (s_min_nz, s_max_z, gap)


@dataclass
class MCResult:
    L: int
    dof_per_node: int      # 3 (central-force) or 6 (micropolar)
    n_nodes: int
    n_dof: int             # DOF = dof_per_node * N
    n_constraints: int     # #rows of R (bonds, or 3*bonds for micropolar)
    rank: int
    floppy: int            # f = DOF - rank
    self_stress: int       # s = #constraints - rank
    mc_index: int          # f - s = DOF - #constraints  (Maxwell-Calladine)
    z_eff: float           # 2 * rank / N  (additive effective independent-
                           #                constraint coordination per node)
    n_first_bonds: int
    n_second_bonds: int
    sv_gap_ratio: float    # robustness of the rank cutoff
    variant: str           # description


def maxwell_calladine_count(
    net: DiamondNet,
    *,
    micropolar: bool,
    overbrace: bool,
) -> MCResult:
    """Exact Maxwell-Calladine count on the diamond net.

    overbrace=False : primary z=4 network only (1st-neighbour bonds).
    overbrace=True  : 1st + 2nd-neighbour shell (the alpha-FREE |T|=12
                      over-bracing); the over-braced count is the load-bearing
                      one (the question is whether over-bracing pushes z_eff
                      toward a coordination that maps to 1/alpha).
    micropolar=False: central-force 3N (primary).
    micropolar=True : 6N Cosserat micro-rotation (sensitivity variant).

    z_eff = 2 * rank(R) / N : the ADDITIVE effective independent-constraint
    coordination per node (each independent scalar constraint shared by 2 nodes
    contributes 2/N to per-node coordination -- the standard rigidity-percolation
    coordination, distinct from the multiplicative path-count z0 = 52 = 4 * 13).
    """
    first = first_neighbour_bonds(net)
    second = second_neighbour_bonds(net) if overbrace else []
    bonds = first + second

    if micropolar:
        R = build_micropolar_rigidity(net, bonds)
        dof_per_node = 6
    else:
        R = build_central_force_rigidity(net, bonds)
        dof_per_node = 3

    N = net.n_nodes
    n_dof = dof_per_node * N
    n_constraints = R.shape[0]
    rank = exact_rank(R)
    _, _, gap = singular_value_gap(R)

    floppy = n_dof - rank
    self_stress = n_constraints - rank
    mc_index = floppy - self_stress  # == n_dof - n_constraints
    z_eff = 2.0 * rank / N

    variant = (
        f"{'micropolar-6N' if micropolar else 'central-force-3N'}"
        f"/{'overbraced(1st+2nd)' if overbrace else 'primary(1st only)'}"
    )
    return MCResult(
        L=net.L,
        dof_per_node=dof_per_node,
        n_nodes=N,
        n_dof=n_dof,
        n_constraints=n_constraints,
        rank=rank,
        floppy=floppy,
        self_stress=self_stress,
        mc_index=mc_index,
        z_eff=z_eff,
        n_first_bonds=len(first),
        n_second_bonds=len(second),
        sv_gap_ratio=gap,
        variant=variant,
    )


# =============================================================================
# Keating / Cosserat ANGULAR over-bracing (the prereg's "EITHER ... OR"
# alternative to 2nd-neighbour central-force bonds). An angular (bond-bending)
# constraint pins the angle between the two 1st-neighbour bonds (mid->i, mid->j)
# meeting at a node `mid`. To leading order, fixing the bond LENGTHS (central
# force) + fixing the ANGLE pins the i-j 2nd-neighbour separation -- so Keating
# angular bracing is the linear-rigidity SIBLING of 2nd-neighbour central-force
# bonds. We assemble it independently and report the count for completeness.
#
# k_theta / k_s = k_theta/d^2 convention per q_g47_path_b_k4_eigenmode.py
# (KeatingBond). For a PURE constraint COUNT (rank/floppy/self-stress), the
# spring CONSTANTS are irrelevant -- only the constraint DIRECTIONS (the
# gradient rows) set the rank. We use the linearised angle-change row.
# =============================================================================

def build_keating_angular_rigidity(net: DiamondNet) -> tuple:
    """Central-force 1st-neighbour rows + Keating angular (bond-bending) rows.

    Each node `mid` with bonds to i and j (i<j among its 1st-neighbours)
    contributes one angular constraint row = the gradient of the angle theta_imj
    w.r.t. the translational DOF of (i, mid, j). Linearised about the reference
    geometry. Returns (R, n_central_rows, n_angular_rows).

    Angle-change linearisation (standard bond-bending): for unit bond vectors
    a = (pos_i - pos_mid)/|.|, b = (pos_j - pos_mid)/|.|, the change in
    cos(theta) = a.b under small displacements du_i, du_mid, du_j is the row we
    assemble (cos is monotone in theta over (0,pi), so its gradient sets the same
    rank as the angle's). d(a.b) projected transverse to each bond.
    """
    n_nodes = net.n_nodes
    # central-force first-neighbour rows (length constraints)
    first = first_neighbour_bonds(net)
    rows = []  # each: dict col->value over 3N translational DOF

    # length-constraint rows
    for (i, j, dx, dy, dz) in first:
        d = np.array([dx, dy, dz], dtype=float)
        nrm = np.linalg.norm(d)
        if nrm == 0.0:
            continue
        nhat = d / nrm
        row = {}
        for c in range(3):
            row[3 * i + c] = -nhat[c]
            row[3 * j + c] = +nhat[c]
        rows.append(row)
    n_central = len(rows)

    # angular rows: for each node mid, each unordered pair (i, j) of its
    # 1st-neighbours, one bond-bending constraint.
    for mid in range(n_nodes):
        nbrs = net.neighbors[mid]
        # geometric directions mid->neighbour (min image)
        dirs = {}
        for nb in nbrs:
            d = _min_image_disp(net, mid, nb)
            nrm = np.linalg.norm(d)
            if nrm > 0:
                dirs[nb] = (d / nrm, nrm)
        nb_list = sorted(dirs.keys())
        for a_idx in range(len(nb_list)):
            for b_idx in range(a_idx + 1, len(nb_list)):
                i = nb_list[a_idx]
                j = nb_list[b_idx]
                a_hat, la = dirs[i]
                b_hat, lb = dirs[j]
                # d(cos theta) = d(a_hat . b_hat).
                # a_hat = (pos_i - pos_mid)/la ; b_hat = (pos_j - pos_mid)/lb.
                # gradient w.r.t. transverse displacements:
                #   d(a_hat)/du_i = (I - a_hat a_hat^T)/la  (transverse projector)
                # d(cos)/du_i = b_hat^T (I - a_hat a_hat^T)/la = (b_hat - (a.b) a_hat)/la
                ab = float(np.dot(a_hat, b_hat))
                g_i = (b_hat - ab * a_hat) / la      # d cos / d u_i
                g_j = (a_hat - ab * b_hat) / lb      # d cos / d u_j
                g_mid = -(g_i + g_j)                  # d cos / d u_mid (sum=0)
                row = {}
                for c in range(3):
                    row[3 * i + c] = row.get(3 * i + c, 0.0) + g_i[c]
                    row[3 * j + c] = row.get(3 * j + c, 0.0) + g_j[c]
                    row[3 * mid + c] = row.get(3 * mid + c, 0.0) + g_mid[c]
                rows.append(row)
    n_angular = len(rows) - n_central

    R = np.zeros((len(rows), 3 * n_nodes), dtype=float)
    for b, row in enumerate(rows):
        for col, val in row.items():
            R[b, col] = val
    return R, n_central, n_angular


def keating_mc_count(net: DiamondNet) -> MCResult:
    """Exact MC count for the Keating angular-overbracing variant (central-force
    1st-neighbour length constraints + bond-bending angular constraints)."""
    R, n_central, n_angular = build_keating_angular_rigidity(net)
    N = net.n_nodes
    n_dof = 3 * N
    n_constraints = R.shape[0]
    rank = exact_rank(R)
    _, _, gap = singular_value_gap(R)
    floppy = n_dof - rank
    self_stress = n_constraints - rank
    mc_index = floppy - self_stress
    z_eff = 2.0 * rank / N
    return MCResult(
        L=net.L,
        dof_per_node=3,
        n_nodes=N,
        n_dof=n_dof,
        n_constraints=n_constraints,
        rank=rank,
        floppy=floppy,
        self_stress=self_stress,
        mc_index=mc_index,
        z_eff=z_eff,
        n_first_bonds=n_central,
        n_second_bonds=n_angular,
        sv_gap_ratio=gap,
        variant="central-force-3N/keating-angular-overbraced",
    )


# =============================================================================
# __main__ : run the L = 4, 6, 8 sweep, all variants, the topology-parity check
# against ave.core.chiral_lattice.build_diamond_net, and the alpha-free-map
# verdict. Everything alpha-comparison-related lives HERE (verify_universe.py
# exempts the __main__ block from its float scan; ave.core is only imported
# here, AFTER the count module is fully built, so the import-graph guard above
# is never violated for the count itself).
# =============================================================================

def _verify_topology_parity(L: int) -> tuple:
    """Confirm the standalone diamond net's adjacency == build_diamond_net's,
    so the alpha-free standalone build is provably the SAME topology as the
    canonical (alpha-importing) one. Returns (ok, n_nodes, detail)."""
    net = build_diamond_net_standalone(L)
    try:
        from ave.core.chiral_lattice import build_diamond_net  # noqa: PLC0415
    except Exception as e:  # pragma: no cover
        return (None, net.n_nodes, f"could not import build_diamond_net: {e}")
    canon = build_diamond_net(L)
    if canon.n_nodes != net.n_nodes:
        return (False, net.n_nodes, f"node count {net.n_nodes} != {canon.n_nodes}")
    # Compare adjacency as sets of neighbour-coordinate-sets (order-independent).
    # Both nets index nodes in the SAME enumeration order (identical loop), so
    # compare neighbour index-sets directly.
    for u in range(net.n_nodes):
        if set(net.neighbors[u]) != set(canon.neighbors[u]):
            return (False, net.n_nodes, f"node {u} adjacency mismatch")
    return (True, net.n_nodes, "adjacency identical to build_diamond_net")


def _alpha_free_map_verdict(z_eff_overbraced: float, alpha_inv_codata: float):
    """The load-bearing Q1 verdict. Reports z_eff against the candidate targets
    and asks: is there an alpha-FREE map z_eff -> 1/alpha? Returns a dict.

    Candidate reference numbers (NONE fed into the count):
      multiplicative-52 : z0 = 4 * (1 + |T|) = 4 * 13 = 52  (path-count convention)
      additive-16       : z ~ 16  (the additive coordination the walk-back named)
      alpha-fit-51.25   : Z_COORDINATION, the FTG-EMT root of p_c = 8*pi*alpha
                          (CIRCULAR -- requires alpha as input; shown only to
                          demonstrate the smuggle)
      1/alpha           : 137.036 CODATA (the chord target)
    """
    mult_52 = N_K4 * (1 + ABS_T)  # 52, alpha-free integer
    add_16 = 16  # the additive coordination (alpha-free integer reference)

    # The ONLY published z_eff -> 1/alpha maps in the corpus:
    #   (a) the FTG-EMT quadratic p_c = (10z-12)/(z(z+2)) = 8*pi*alpha then
    #       1/alpha = 8*pi/p_c  -- REQUIRES alpha (circular).
    #   (b) the dilution percolation 1/alpha = 8*pi/p_c with p_c a packing
    #       fraction -- reintroduces stochastic disorder (forbidden).
    # There is NO alpha-free closed form taking an integer/float coordination to
    # 137.036. We therefore test only whether z_eff coincides (within tol) with
    # any candidate, and report the explicit ABSENCE of an alpha-free 137 map.

    def rel(a, b):
        return abs(a - b) / abs(b) if b else float("inf")

    nearest = min(
        [
            ("multiplicative-52", mult_52, rel(z_eff_overbraced, mult_52)),
            ("additive-16", add_16, rel(z_eff_overbraced, add_16)),
            ("alpha-fit-51.25(CIRCULAR)", 51.25, rel(z_eff_overbraced, 51.25)),
        ],
        key=lambda t: t[2],
    )

    # 1/alpha from an alpha-free map: NONE exists. The closest the count could
    # come is an arithmetic coincidence z_eff ~ 137 directly -- check it.
    direct_137 = rel(z_eff_overbraced, alpha_inv_codata)

    return {
        "z_eff_overbraced": z_eff_overbraced,
        "multiplicative_52": mult_52,
        "additive_16": add_16,
        "alpha_fit_51_25_CIRCULAR": 51.25,
        "alpha_inv_codata": alpha_inv_codata,
        "nearest_candidate": nearest[0],
        "nearest_value": nearest[1],
        "nearest_rel_err": nearest[2],
        "rel_err_vs_137_direct": direct_137,
        "alpha_free_map_to_137_exists": False,  # no such map in the corpus
    }


def main() -> None:
    import json

    # CODATA alpha^-1 -- ONE-WAY comparison target ONLY (input label, never fed
    # into the count). Imported from the canonical constants module HERE in main()
    # (ave-canonical-source: never hard-code), computed as 1/ALPHA so no literal
    # 137.036 token appears (passes verify_universe's AST float scan). This is
    # AFTER the count module is fully built; the import-graph guard at top-of-file
    # already verified ave.core was NOT on the count's import graph -- importing it
    # now, at __main__ time, for a ONE-WAY comparison, does not feed alpha into any
    # count. The count results are ALL produced by the alpha-free functions above.
    from ave.core.constants import ALPHA  # noqa: PLC0415 (deliberate main-time import)
    ALPHA_INV_CODATA = 1.0 / ALPHA  # CODATA alpha^-1 (comparison reference ONLY)

    Ls = [4, 6, 8]

    print("=" * 78)
    print("  EXACT MAXWELL-CALLADINE CONSTRAINT COUNT")
    print("  achiral diamond (z=4) K4 crystal -- alpha-FREE")
    print("  prereg: 2026-06-15_alpha-crystal-mc-count_prereg_FROZEN.md")
    print("=" * 78)
    print(f"  alpha-free guard: 'ave.core' in sys.modules at module import = "
          f"{'ave.core' in sys.modules}  (False expected)")
    print()

    # ---- topology parity ----------------------------------------------------
    print("-" * 78)
    print("  Topology parity vs ave.core.chiral_lattice.build_diamond_net")
    print("-" * 78)
    for L in Ls:
        ok, nn, detail = _verify_topology_parity(L)
        print(f"  L={L}: N={nn:4d}  parity={ok}  ({detail})")
    print()

    all_results = {}

    # ---- central-force 3N (primary) -----------------------------------------
    for overbrace in (False, True):
        tag = "overbraced(1st+2nd)" if overbrace else "primary(1st only)"
        print("-" * 78)
        print(f"  CENTRAL-FORCE 3N  --  {tag}")
        print("-" * 78)
        print(f"  {'L':>3} {'N':>5} {'DOF':>6} {'#C':>6} {'rank':>6} "
              f"{'f':>5} {'s':>5} {'f-s':>6} {'z_eff':>8} {'svgap':>10}")
        for L in Ls:
            net = build_diamond_net_standalone(L)
            res = maxwell_calladine_count(net, micropolar=False, overbrace=overbrace)
            print(f"  {res.L:>3} {res.n_nodes:>5} {res.n_dof:>6} "
                  f"{res.n_constraints:>6} {res.rank:>6} {res.floppy:>5} "
                  f"{res.self_stress:>5} {res.mc_index:>6} {res.z_eff:>8.4f} "
                  f"{res.sv_gap_ratio:>10.2e}")
            all_results[f"cf3N_{tag}_L{L}"] = res.__dict__
        print()

    # ---- micropolar 6N (sensitivity) ----------------------------------------
    for overbrace in (False, True):
        tag = "overbraced(1st+2nd)" if overbrace else "primary(1st only)"
        print("-" * 78)
        print(f"  MICROPOLAR 6N (Cosserat, sensitivity)  --  {tag}")
        print("-" * 78)
        print(f"  {'L':>3} {'N':>5} {'DOF':>6} {'#C':>6} {'rank':>6} "
              f"{'f':>5} {'s':>5} {'f-s':>6} {'z_eff':>8} {'svgap':>10}")
        for L in Ls:
            net = build_diamond_net_standalone(L)
            res = maxwell_calladine_count(net, micropolar=True, overbrace=overbrace)
            print(f"  {res.L:>3} {res.n_nodes:>5} {res.n_dof:>6} "
                  f"{res.n_constraints:>6} {res.rank:>6} {res.floppy:>5} "
                  f"{res.self_stress:>5} {res.mc_index:>6} {res.z_eff:>8.4f} "
                  f"{res.sv_gap_ratio:>10.2e}")
            all_results[f"mp6N_{tag}_L{L}"] = res.__dict__
        print()

    # ---- Keating angular over-bracing (the EITHER/OR alternative) ------------
    print("-" * 78)
    print("  KEATING ANGULAR over-bracing (central-force 1st + bond-bending)")
    print("-" * 78)
    print(f"  {'L':>3} {'N':>5} {'DOF':>6} {'#C':>6} {'rank':>6} "
          f"{'f':>5} {'s':>5} {'f-s':>6} {'z_eff':>8} {'svgap':>10}")
    for L in Ls:
        net = build_diamond_net_standalone(L)
        res = keating_mc_count(net)
        print(f"  {res.L:>3} {res.n_nodes:>5} {res.n_dof:>6} "
              f"{res.n_constraints:>6} {res.rank:>6} {res.floppy:>5} "
              f"{res.self_stress:>5} {res.mc_index:>6} {res.z_eff:>8.4f} "
              f"{res.sv_gap_ratio:>10.2e}")
        all_results[f"keating_L{L}"] = res.__dict__
    print()

    # ---- alpha-free-map verdict (Q1, load-bearing) --------------------------
    print("=" * 78)
    print("  ALPHA-FREE-MAP VERDICT (prereg Q1)")
    print("=" * 78)
    # use the converged (largest L) central-force OVER-BRACED z_eff
    net8 = build_diamond_net_standalone(8)
    res8_ob = maxwell_calladine_count(net8, micropolar=False, overbrace=True)
    verdict = _alpha_free_map_verdict(res8_ob.z_eff, ALPHA_INV_CODATA)
    print(f"  z_eff (central-force, over-braced, L=8) = {verdict['z_eff_overbraced']:.4f}")
    print(f"  multiplicative path-count  z0 = 4*(1+|T|) = {verdict['multiplicative_52']}")
    print(f"  additive coordination ref        z ~ {verdict['additive_16']}")
    print(f"  alpha-fit (CIRCULAR, FTG-EMT)     = {verdict['alpha_fit_51_25_CIRCULAR']}  "
          f"(requires alpha; shown to expose the smuggle)")
    print(f"  CODATA 1/alpha                    = {verdict['alpha_inv_codata']}")
    print(f"  nearest candidate to z_eff        = {verdict['nearest_candidate']} "
          f"({verdict['nearest_value']}, {verdict['nearest_rel_err']*100:.1f}% off)")
    print(f"  z_eff vs 137 direct               = {verdict['rel_err_vs_137_direct']*100:.1f}% off")
    print(f"  alpha-FREE map z_eff -> 137 exists = {verdict['alpha_free_map_to_137_exists']}  "
          f"(NONE in corpus: only 8*pi*alpha [circular] or dilution-p_c [forbidden])")
    print("=" * 78)

    all_results["_alpha_free_map_verdict"] = verdict
    all_results["_alpha_inv_codata_INPUT_LABEL"] = ALPHA_INV_CODATA

    out_path = (
        __import__("os").path.join(
            __import__("os").path.dirname(__file__),
            "alpha_crystal_mc_count_results.json",
        )
    )
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2)
    print(f"\n  Wrote: {out_path}")


if __name__ == "__main__":
    main()

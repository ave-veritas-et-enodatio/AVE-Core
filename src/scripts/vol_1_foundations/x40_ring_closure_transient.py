"""x40 — the 10-ring closure transient: the derivable stick/slip split.

SECTOR HEADER (binding).
  MODE     formation-epoch transient — a single nucleation at the growth front,
           the moment one new bond closes onto the settled lattice.
  REGIME   lossless. Linear TL abstraction at a fixed operating point; the
           Axiom-4 kernel is NOT engaged (any constant saturation is absorbed
           into Z0). Kernel-independence at this abstraction is a stated model
           scope, not a claim about the saturated front.
  SECTOR   winding-vs-wave. The trapped DC mesh circulation is GRAPH-register
           content (winding/counting bin); the AC transient is on-line wave
           content radiated to the bath. The mesh quantity is the loop flux
           linkage Lambda = sum over ring bonds — a 2-cochain, NOT a per-node
           Cartesian proxy.
  VOCAB    reactive / trapped / radiated — never "loss." Each ring node's stub
           is the matched bath port (energy carried away down a semi-infinite
           lossless line), not a resistor.

WHAT THIS COMPUTES.
  Each nucleation = a switch closure connecting a new bond carrying inherited
  circulation i(0) = I_parent to the settled lattice. The lossless split:
    (1) a DC loop current TRAPPED in the smallest closed mesh (frozen winding),
    (2) an AC transient RADIATED into the semi-infinite Z0 stub lines.
  Headline (substrate-native TLM): trapped energy fraction f_E = L_bond/L_loop
  = 1/N = 1/10 EXACTLY (radiated 9/10); flux banks WHOLE (Lambda conserved
  100%). Second axis (KEEP-BOTH, geometric): f_E^(geom) = 1/(N + sum m_jk) with
  the Neumann mutual terms of the actual skew ring — see x40_neumann_second_axis.

ANTI-INSTALL (gate G-E).
  This module works in DIMENSIONLESS units end-to-end: Z0 = 1, per-bond delay
  tau = 1, length l = 1 => L_bond = Z0*tau = 1, C_bond = tau/Z0 = 1. It imports
  NO dimensional constant from ave.core.constants (no OMEGA_C, M_E, HBAR, ALPHA,
  L_NODE, ...). The load-bearing identity L_bond = mu0*l = Z0*tau makes the
  split fraction scale-free by construction; only ring topology (and, on the
  second axis, ring geometry) survives. `scan_for_dimensional_constants` is the
  machine check of this claim (applied to this file by the test suite).

Frozen prereg: research/2026-07-10_x40-ring-closure-transient_prereg_FROZEN.md
Brief:         _orchestration/2026-07-10_x40-ring-closure-brief.md
"""

from __future__ import annotations

import ast
from dataclasses import dataclass

import numpy as np

from ave.core.chiral_lattice import build_srs_net, ring_coords
from ave.topological.srs_dec import MIN_SRS_L, enumerate_girth_faces

# ─────────────────────────────────────────────────────────────────────────────
# Ring topology — N is DERIVED from the srs net, never hardcoded (gate G-D).
# ─────────────────────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class Ring:
    """One smallest mesh of the srs net: the closed 10-cycle the new bond completes."""

    nodes: tuple[int, ...]  # cyclic node order (carries face orientation)
    coords: np.ndarray  # (N, 3) PBC-unwrapped Cartesian coords, ring order
    N: int  # ring length == girth; asserted == 10


def derive_ring(L: int = MIN_SRS_L, enantiomorph: str = "right") -> Ring:
    """Build an L>=3 srs net, enumerate its girth cycles, return one ring.

    N is TAKEN from the enumerated minimal-cycle length — asserted == 10 (G-D).
    An L=2 supercell folds girth-10 rings into spurious 8-rings; MIN_SRS_L=3.
    """
    if L < MIN_SRS_L:
        raise ValueError(f"L={L} < MIN_SRS_L={MIN_SRS_L}: PBC folds girth-10 into spurious 8-rings")
    net = build_srs_net(L=L, enantiomorph=enantiomorph)
    faces = enumerate_girth_faces(net)
    if not faces:
        raise RuntimeError("enumerate_girth_faces returned no cycles — cannot derive N")
    lengths = sorted({len(f) for f in faces})
    N = lengths[0]  # minimal cycle length = girth
    if lengths != [N]:
        raise RuntimeError(f"non-uniform cycle lengths {lengths}; expected all == girth")
    if N != 10:
        raise RuntimeError(f"derived girth N={N} != 10 — contradicts srs (10,3)-a canon (G-D FAIL)")
    ring_nodes = faces[0]
    coords = ring_coords(net, ring_nodes)
    return Ring(nodes=tuple(ring_nodes), coords=coords, N=N)


# ─────────────────────────────────────────────────────────────────────────────
# The exact synchronous TLM bounce model (dimensionless: Z0 = tau = l = 1).
#
# Nodes 0..N-1 cyclic; bond k connects node k -> node k+1. Two directed wave
# samples per bond: p[k] travels k->k+1, m[k] travels k+1->k. Each node is the
# equal-Z0 3-port shunt (2 ring ports + 1 matched stub), S_pq = 2/n - delta_pq
# (n=3): S_jj = -1/3, S_jk = 2/3. The stub reflected wave = node voltage v_k;
# it leaves down the semi-infinite line and never returns (radiated ledger).
# ─────────────────────────────────────────────────────────────────────────────


def initial_condition(N: int, I_parent: float = 1.0, closing_bond: int = 0) -> tuple[np.ndarray, np.ndarray]:
    """IC: uniform current I_parent on the closing bond, v = 0, all else quiescent.

    v = 0 => p + m = 0; i = (p - m)/Z0 = I_parent => p = +I_parent/2, m = -I_parent/2
    (the equal counter-propagating wave decomposition).
    """
    p = np.zeros(N)
    m = np.zeros(N)
    p[closing_bond] = I_parent / 2.0
    m[closing_bond] = -I_parent / 2.0
    return p, m


def step(
    p: np.ndarray,
    m: np.ndarray,
    *,
    bond_loss: float = 0.0,
    loss_bond: int = 0,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """One synchronous scatter+connect tick. Returns (p_new, m_new, v).

    v_k       = (2/3)(p[k-1] + m[k])   node voltage = stub reflected (radiated) wave
    p_new[k]  = v_k - m[k]             reflected onto +ring port at node k
    m_new[k]  = v[k+1] - p[k]          reflected onto -ring port (from node k+1)

    `bond_loss` in (0,1] plants a series resistance on one ring bond (SABOTAGE
    S1): the crossing waves are attenuated by sqrt(1 - bond_loss). Lossless
    physics uses bond_loss = 0.0.
    """
    p_left_in = np.roll(p, 1)  # p_left_in[k] = p[k-1]
    v = (2.0 / 3.0) * (p_left_in + m)  # node voltage (= stub reflected wave)
    p_new = v - m
    m_new = np.roll(v, -1) - p  # m_new[k] = v[k+1] - p[k]
    if bond_loss > 0.0:
        gamma = np.sqrt(max(0.0, 1.0 - bond_loss))
        p_new[loss_bond] *= gamma
        m_new[loss_bond] *= gamma
    return p_new, m_new, v


def flux_linkage(p: np.ndarray, m: np.ndarray) -> float:
    """Loop flux linkage Lambda = sum_k L_bond * i_k = sum_k (p_k - m_k) (L_bond=1)."""
    return float(np.sum(p - m))


def bond_currents(p: np.ndarray, m: np.ndarray) -> np.ndarray:
    """Per-bond current i_k = (p_k - m_k)/Z0 = p_k - m_k (Z0 = 1)."""
    return p - m


def ring_energy(p: np.ndarray, m: np.ndarray) -> float:
    """In-flight ring energy E_ring = sum_k (p_k^2 + m_k^2) (L_bond = C_bond = 1)."""
    return float(np.sum(p * p + m * m))


@dataclass
class Transient:
    """Recorded closure transient over the window [0, n_ticks] (all in units of tau)."""

    t: np.ndarray  # (T+1,) tick index, units of tau
    Lambda: np.ndarray  # (T+1,) loop flux linkage Lambda(t)
    E_ring: np.ndarray  # (T+1,) in-flight ring energy
    E_rad: np.ndarray  # (T+1,) cumulative radiated (to bath) energy
    i_min: np.ndarray  # (T+1,) min per-bond current
    i_max: np.ndarray  # (T+1,) max per-bond current
    i_mean: np.ndarray  # (T+1,) mean per-bond current (= Lambda/N exactly)
    E0: float  # initial energy
    Lambda0: float  # initial flux linkage
    N: int
    currents_final: np.ndarray  # (N,) final per-bond DC current profile


def simulate(
    N: int,
    n_ticks: int = 300,
    I_parent: float = 1.0,
    closing_bond: int = 0,
    *,
    bond_loss: float = 0.0,
    loss_bond: int = 0,
    drop_stub: int | None = None,
) -> Transient:
    """Evolve the closure transient for `n_ticks` synchronous TLM ticks.

    `bond_loss`   > 0 plants series resistance on `loss_bond` (SABOTAGE S1).
    `drop_stub`   != None omits that node's stub outflow from the radiated
                  ledger only — the dynamics are UNCHANGED; the accounting loses
                  energy (SABOTAGE S3, targets G-C alone).
    """
    p, m = initial_condition(N, I_parent=I_parent, closing_bond=closing_bond)
    E0 = ring_energy(p, m)
    Lambda0 = flux_linkage(p, m)

    T = n_ticks
    t = np.arange(T + 1)
    Lam = np.empty(T + 1)
    Er = np.empty(T + 1)
    Erad = np.empty(T + 1)
    imin = np.empty(T + 1)
    imax = np.empty(T + 1)
    imean = np.empty(T + 1)

    E_rad = 0.0
    ic = bond_currents(p, m)
    Lam[0], Er[0], Erad[0] = Lambda0, E0, 0.0
    imin[0], imax[0], imean[0] = ic.min(), ic.max(), ic.mean()

    for k in range(1, T + 1):
        p, m, v = step(p, m, bond_loss=bond_loss, loss_bond=loss_bond)
        rad_node = v * v
        if drop_stub is None:
            E_rad += float(np.sum(rad_node))
        else:  # S3: silently drop one stub from the ledger (dynamics unchanged)
            E_rad += float(np.sum(rad_node) - rad_node[drop_stub])
        ic = bond_currents(p, m)
        Lam[k] = flux_linkage(p, m)
        Er[k] = ring_energy(p, m)
        Erad[k] = E_rad
        imin[k], imax[k], imean[k] = ic.min(), ic.max(), ic.mean()

    return Transient(
        t=t, Lambda=Lam, E_ring=Er, E_rad=Erad, i_min=imin, i_max=imax, i_mean=imean,
        E0=E0, Lambda0=Lambda0, N=N, currents_final=bond_currents(p, m),
    )


# ─────────────────────────────────────────────────────────────────────────────
# Gate G-E — the ANTI-INSTALL scanner (machine-checked, AST-based).
#
# Any import from `ave.core.constants`, or any use of a forbidden dimensional
# constant name, is an automatic FAIL. AST-based (Name / Import / Attribute
# nodes only) so a mention inside a docstring or comment does NOT trip it — only
# a live code reference does.
# ─────────────────────────────────────────────────────────────────────────────

FORBIDDEN_CONSTANTS: frozenset[str] = frozenset({
    "OMEGA_C", "M_E", "HBAR", "ALPHA", "L_NODE", "L_CELL", "C_CELL",
    "Z_0", "C_0", "V_SNAP", "Q_TANK", "EPS_0", "MU_0", "ELL_NODE",
})
_CONSTANTS_MODULE = "ave.core.constants"


def scan_for_dimensional_constants(source_path: str) -> list[str]:
    """Return a list of anti-install violations found in `source_path` (empty = clean).

    Flags: (1) any `import ave.core.constants` / `from ave.core.constants import`;
    (2) any Name node whose id is a forbidden dimensional constant; (3) any
    attribute access `<constants>.<FORBIDDEN>`. Docstrings/comments are Constant
    (str) nodes and are NOT scanned.
    """
    with open(source_path, encoding="utf-8") as fh:
        tree = ast.parse(fh.read(), filename=source_path)
    violations: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and (node.module or "").startswith(_CONSTANTS_MODULE):
            names = ", ".join(a.name for a in node.names)
            violations.append(f"line {node.lineno}: from {node.module} import {names}")
        elif isinstance(node, ast.Import):
            for a in node.names:
                if a.name.startswith(_CONSTANTS_MODULE):
                    violations.append(f"line {node.lineno}: import {a.name}")
        elif isinstance(node, ast.Name) and node.id in FORBIDDEN_CONSTANTS:
            violations.append(f"line {node.lineno}: use of dimensional constant '{node.id}'")
        elif isinstance(node, ast.Attribute) and node.attr in FORBIDDEN_CONSTANTS:
            violations.append(f"line {node.lineno}: attribute access '.{node.attr}'")
    return violations


# ─────────────────────────────────────────────────────────────────────────────
# E4 — the Neumann-mutual SECOND AXIS (KEEP-BOTH; the genuinely open number).
#
# L_loop^(geom) = N*L_self + sum_{j!=k} M_jk, with the SELF footing fixed at the
# canonical TLM per-bond mu0*l (substrate-native) — NOT the divergent filament
# self-inductance. M_jk = (mu0/4pi) oint_j oint_k (dl_j . dl_k)/|r_j - r_k| over
# the ACTUAL skew ring, consistent signed orientation. Reported as a SEPARATE
# characterization axis (mixed footing declared); the headline stays the TLM 1/10.
#
# Method: reduce the double Neumann integral to a 1-D outer integral of the exact
# inner segment potential. Adjacent bonds share a vertex => integrable log
# endpoint singularity, flagged to the quadrature.
# ─────────────────────────────────────────────────────────────────────────────


def _segment_potential(r: np.ndarray, c: np.ndarray, bhat: np.ndarray, length: float) -> float:
    """G_k(r) = integral_0^length dt / |r - (c + t*bhat)|  (exact closed form).

    = asinh((L - t0)/h) - asinh(-t0/h), t0 = (r-c).bhat, h = perp distance.
    Uses the equivalent log-ratio form; +inf only at a point ON the segment
    (the shared vertex) where the outer integral's log singularity is integrable.
    """
    w = r - c
    t0 = float(w @ bhat)
    perp2 = float(w @ w) - t0 * t0
    h2 = max(perp2, 0.0)
    a = length - t0
    b = -t0
    num = a + np.sqrt(a * a + h2)
    den = b + np.sqrt(b * b + h2)
    if den <= 0.0 or num <= 0.0:  # exactly on the segment line at/through the vertex
        den = max(den, 1e-300)
        num = max(num, 1e-300)
    return float(np.log(num) - np.log(den))


def mutual_inductance(seg_j: np.ndarray, seg_k: np.ndarray) -> float:
    """Neumann mutual inductance M_jk (mu0 = 1) between two oriented straight bonds.

    seg = (2,3) endpoints [P_start, P_end]; the current direction is P_start->P_end
    (the signed ring orientation). Adjacent bonds sharing a vertex are handled by
    flagging the singular abscissa to the adaptive quadrature.
    """
    from scipy.integrate import quad

    a0, a1 = seg_j[0], seg_j[1]
    c0, c1 = seg_k[0], seg_k[1]
    da = a1 - a0
    dc = c1 - c0
    L1 = float(np.linalg.norm(da))
    L2 = float(np.linalg.norm(dc))
    ahat = da / L1
    chat = dc / L2
    dot = float(ahat @ chat)  # sign of the mutual rides on the orientation dot

    # singular abscissae: s where r1(s) coincides with a shared vertex of seg_k
    sing = []
    for vtx in (c0, c1):
        s = float((vtx - a0) @ ahat)
        if -1e-9 <= s <= L1 + 1e-9 and np.linalg.norm(a0 + s * ahat - vtx) < 1e-9:
            sing.append(min(max(s, 0.0), L1))

    def integrand(s: float) -> float:
        return _segment_potential(a0 + s * ahat, c0, chat, L2)

    val, _ = quad(integrand, 0.0, L1, points=sing or None, limit=200)
    return (1.0 / (4.0 * np.pi)) * dot * val


def neumann_second_axis(ring: Ring) -> dict[str, float]:
    """Compute the geometric second axis over the actual skew ring.

    Returns Sigma m_jk (ordered-pair sum), f_E^(geom), and the split of Sigma
    into adjacent (shared-vertex) vs non-adjacent contributions. Footing: self =
    mu0*l (TLM), mutuals = Neumann. m_jk = M_jk/(mu0*l); l = mean bond length.
    """
    P = ring.coords
    N = ring.N
    segs = [np.array([P[k], P[(k + 1) % N]]) for k in range(N)]
    ell = float(np.mean([np.linalg.norm(s[1] - s[0]) for s in segs]))

    sum_m = 0.0
    sum_adj = 0.0
    sum_nonadj = 0.0
    for j in range(N):
        for k in range(N):
            if j == k:
                continue
            M = mutual_inductance(segs[j], segs[k])
            m = M / ell  # normalize by mu0*l (mu0 = 1)
            sum_m += m
            if k in ((j + 1) % N, (j - 1) % N):
                sum_adj += m
            else:
                sum_nonadj += m
    f_E_geom = 1.0 / (N + sum_m)
    return {
        "sum_m_jk": sum_m,
        "sum_m_adjacent": sum_adj,
        "sum_m_nonadjacent": sum_nonadj,
        "f_E_geom": f_E_geom,
        "L_loop_geom_over_mu0l": N + sum_m,
        "ell": ell,
        "N": float(N),
    }


# ─────────────────────────────────────────────────────────────────────────────
# E5 — the cut/cycle (T-even / T-odd) Hodge split of the injected current
# (post-freeze amendment). The srs edge space E = cut-space (im d1^T, gradient,
# T-even bond strain) (+) cycle-space (ker d1, divergence-free circulation, T-odd
# loop current). Project i(0) = delta(closing edge); |P_cut d_e|^2 = R_eff(e).
# For an otherwise-tree-local 10-ring, R_eff = 9/10 => cut:cycle = 9:1, and the
# T-odd cycle fraction = 1/10 EQUALS the E2 energy split (the divergence-free part
# is exactly what the matched stubs cannot drain). Gate G-F checks the split is a
# genuine orthogonal decomposition; `perturb` plants the S4 non-orthogonal basis.
# ─────────────────────────────────────────────────────────────────────────────


def _ring_incidence(N: int) -> np.ndarray:
    """Node x edge incidence d1 of the oriented N-cycle (edge k: node k -> k+1).

    The ring-restriction of the srs boundary_1 (reused machinery); a clean cyclic
    incidence is the tree-local nucleation-front subgraph the injected bond closes.
    """
    B = np.zeros((N, N))
    for k in range(N):
        B[k, k] = -1.0  # tail
        B[(k + 1) % N, k] = +1.0  # head
    return B


def hodge_split_injected_current(ring: Ring, closing_edge: int = 0, perturb: float = 0.0) -> dict[str, float]:
    """Cut/cycle projection of i(0) on the tree-local nucleation ring (PRIMARY, E5).

    `perturb` > 0 skews the cycle projector by +perturb*P_cut (SABOTAGE S4): the
    two subspaces then overlap and G-F FIRES. Lossless/clean physics: perturb=0.
    """
    N = ring.N
    B = _ring_incidence(N)
    lap = B @ B.T
    P_cut = B.T @ np.linalg.pinv(lap) @ B
    P_cyc = np.eye(N) - P_cut
    if perturb > 0.0:
        P_cyc = P_cyc + perturb * P_cut  # oblique / non-orthogonal (planted S4 fault)

    i0 = np.zeros(N)
    i0[closing_edge] = 1.0
    norm2 = float(i0 @ i0)
    cut = float((P_cut @ i0) @ i0)
    cyc = float((P_cyc @ i0) @ i0)
    gf_ortho = float((P_cut @ i0) @ (P_cyc @ i0)) / norm2
    gf_complete = abs(cut + cyc - norm2) / norm2
    gf_projsum = float(np.max(np.abs((P_cut + P_cyc) - np.eye(N))))
    return {
        "cut_fraction_T_even": cut / norm2,
        "cycle_fraction_T_odd": cyc / norm2,
        "b1_cycle_dim": float(round(float(np.trace(P_cyc)))),
        "G_F_ortho": gf_ortho,
        "G_F_completeness": gf_complete,
        "G_F_projsum_max": gf_projsum,
    }


def hodge_split_fullnet(L: int = MIN_SRS_L, enantiomorph: str = "right") -> dict[str, float]:
    """Cut/cycle of the SAME single edge on the FULL srs net (SECONDARY, KEEP-BOTH).

    Reuses srs_dec.boundary_1. Extra parallel paths lower R_eff below 9/10, so the
    cycle fraction is LARGER than the tree-local 1/10 — the qualifier is load-bearing.
    """
    from ave.topological.srs_dec import boundary_1

    net = build_srs_net(L=L, enantiomorph=enantiomorph)
    faces = enumerate_girth_faces(net)
    ring = faces[0]
    D1, edges = boundary_1(net)
    D1 = D1.toarray()
    edge_index = {tuple(sorted(e)): idx for idx, e in enumerate(edges)}
    ei = edge_index[tuple(sorted((ring[0], ring[1])))]
    ne = D1.shape[1]
    lap = D1 @ D1.T
    b = D1[:, ei]
    cut = float(b @ np.linalg.pinv(lap) @ b)
    return {
        "cut_fraction_T_even_fullnet": cut,
        "cycle_fraction_T_odd_fullnet": 1.0 - cut,
        "b1_fullnet": float(ne - net.n_nodes + 1),
        "n_edges_fullnet": float(ne),
    }


def _newell_normal(P: np.ndarray) -> np.ndarray:
    """Newell area-weighted unit normal of a (possibly non-planar) polygon ring."""
    n = np.zeros(3)
    m = len(P)
    for k in range(m):
        a, b = P[k], P[(k + 1) % m]
        n[0] += (a[1] - b[1]) * (a[2] + b[2])
        n[1] += (a[2] - b[2]) * (a[0] + b[0])
        n[2] += (a[0] - b[0]) * (a[1] + b[1])
    return n / np.linalg.norm(n)


def ring_orientation_ensemble(L: int = MIN_SRS_L, enantiomorph: str = "right") -> dict:
    """Sign-vs-orientation deliverable: ring-normal ensemble bias vs balance (E5, sign leg).

    Omega_parent enters ONLY as unit reference axes (NOT a scale) — anti-install safe.
    Returns the sign-free orientation tensor Q = <n n^T> eigenvalues, the signed mean
    |sum n|/N (0 => balanced), and mean/signed |n . Omega| for reference axes.
    """
    net = build_srs_net(L=L, enantiomorph=enantiomorph)
    faces = enumerate_girth_faces(net)
    normals = np.array([_newell_normal(ring_coords(net, f)) for f in faces])
    Q = (normals[:, :, None] * normals[:, None, :]).mean(axis=0)
    eig = np.linalg.eigvalsh(Q)
    signed_mean_norm = float(np.linalg.norm(normals.mean(axis=0)))
    axes = {
        "[001]": np.array([0.0, 0.0, 1.0]),
        "[111]": np.array([1.0, 1.0, 1.0]) / np.sqrt(3.0),
        "[110]": np.array([1.0, 1.0, 0.0]) / np.sqrt(2.0),
    }
    projections = {
        name: {"mean_abs": float(np.mean(np.abs(normals @ ax))),
               "signed_mean": float(np.mean(normals @ ax))}
        for name, ax in axes.items()
    }
    return {
        "n_rings": int(len(faces)),
        "Q_eigenvalues": [float(x) for x in eig],
        "signed_mean_normal_magnitude": signed_mean_norm,
        "omega_projections": projections,
    }


# ─────────────────────────────────────────────────────────────────────────────
# Reporting — gate metrics, the figure, and the JSON results dump.
# ─────────────────────────────────────────────────────────────────────────────


def gate_metrics(tr: Transient) -> dict[str, float]:
    """Compute the G-A / G-B / G-C headline metrics from a transient."""
    lam_dev = float(np.max(np.abs(tr.Lambda - tr.Lambda0) / abs(tr.Lambda0)))
    ledger_dev = float(np.max(np.abs(tr.E_ring + tr.E_rad - tr.E0) / tr.E0))
    i_final = tr.currents_final
    return {
        "G_A_lambda_max_rel_dev": lam_dev,
        "G_B_plateau_max_abs_dev": float(np.max(np.abs(i_final - 1.0 / tr.N))),
        "G_B_i_dc_mean": float(i_final.mean()),
        "G_C_ledger_max_rel_dev": ledger_dev,
        "f_E_trapped": float(tr.E_ring[-1] / tr.E0),
        "f_rad": float(tr.E_rad[-1] / tr.E0),
        "target_f_E": 1.0 / tr.N,
    }


def make_figure(tr: Transient, out_path) -> None:
    """WHITE house-style figure: the closure transient + energy ledger.

    Top    Lambda(t)/Lambda0 (conserved flat) and the per-bond current spread
           [min,max] with the frozen 1/N plateau line.
    Bottom the lossless energy ledger E_ring, E_rad, and their sum (units of E0).
    """
    import matplotlib.pyplot as plt

    from ave.viz.style import COLORS, apply, axis_label

    apply("print")
    fig, (ax0, ax1) = plt.subplots(2, 1, figsize=(7.0, 6.4), sharex=True)

    inv_n = 1.0 / tr.N
    ax0.fill_between(tr.t, tr.i_min, tr.i_max, color=COLORS["accent"], alpha=0.30,
                     label="per-bond current spread [min, max]")
    ax0.plot(tr.t, tr.Lambda / tr.Lambda0, color=COLORS["ave"], lw=1.8, ls="-",
             label=r"$\Lambda(t)/\Lambda_0$ (trapped flux, conserved)")
    ax0.axhline(inv_n, color=COLORS["muted"], lw=1.2, ls="--",
                label=rf"frozen plateau $1/N = {inv_n:.2f}$")
    ax0.axhline(1.0, color=COLORS["muted"], lw=0.8, ls=":", alpha=0.7)
    ax0.set_ylabel(axis_label("Normalized", r"\Lambda/\Lambda_0,\ i", ""))
    ax0.set_ylim(-0.15, 1.15)
    ax0.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), frameon=False, fontsize=8)

    ax1.plot(tr.t, tr.E_ring / tr.E0, color=COLORS["ave"], lw=1.8, ls="-",
             label=r"$E_\mathrm{ring}$ (reactive, trapped)")
    ax1.plot(tr.t, tr.E_rad / tr.E0, color=COLORS["comparison"], lw=1.8, ls="--",
             label=r"$E_\mathrm{rad}$ (radiated to bath)")
    ax1.plot(tr.t, (tr.E_ring + tr.E_rad) / tr.E0, color=COLORS["data"], lw=1.0, ls=":",
             label=r"$E_\mathrm{ring}+E_\mathrm{rad}$ (lossless ledger)")
    ax1.axhline(inv_n, color=COLORS["muted"], lw=1.0, ls="--", alpha=0.7)
    ax1.axhline(1.0 - inv_n, color=COLORS["muted"], lw=1.0, ls="--", alpha=0.7)
    ax1.set_ylabel(axis_label("Energy", "E/E_0", ""))
    ax1.set_xlabel(axis_label("Time", "t", r"$\tau$"))
    ax1.set_ylim(-0.05, 1.05)
    ax1.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), frameon=False, fontsize=8)

    fig.savefig(out_path, facecolor=fig.get_facecolor(), bbox_inches="tight", dpi=150)
    plt.close(fig)


def main() -> dict:
    """Run the full x40 lane: transient + gates + E4 + figure + JSON dump."""
    import json
    from pathlib import Path

    here = Path(__file__).resolve().parent
    out_dir = here / "_output"
    out_dir.mkdir(exist_ok=True)
    fig_path = here / "x40_ring_closure_transient.png"  # tracked (cited render)

    ring = derive_ring()
    tr = simulate(ring.N, n_ticks=300)
    gm = gate_metrics(tr)
    e4 = neumann_second_axis(ring)
    e5 = hodge_split_injected_current(ring)
    e5_full = hodge_split_fullnet()
    orient = ring_orientation_ensemble()
    ge = scan_for_dimensional_constants(str(Path(__file__).resolve()))

    results = {
        "N_derived": ring.N,
        "ring_nodes": list(ring.nodes),
        "gates": gm,
        "G_D_N": ring.N,
        "G_E_self_scan_violations": ge,
        "E4_second_axis": e4,
        "E5_cut_cycle_split": e5,
        "E5_cut_cycle_fullnet": e5_full,
        "E5_orientation_ensemble": orient,
        "headline_f_E_TLM": gm["target_f_E"],
        "dynamical_residue_equals_cycle_projection": abs(gm["f_E_trapped"] - e5["cycle_fraction_T_odd"]),
    }
    make_figure(tr, fig_path)
    with open(out_dir / "x40_ring_closure_transient_results.json", "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=2)
    return results


if __name__ == "__main__":
    import json as _json

    print(_json.dumps(main(), indent=2))

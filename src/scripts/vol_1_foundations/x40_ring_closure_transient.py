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

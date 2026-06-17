"""Shared srs-medium helpers for the L0-L1 acceptance suite.

Thin wrappers over `ave.core.chiral_lattice{,_vector,_dynamics}` — the FROZEN v9
chiral-srs medium. No new physics: these only seed fields and read DYNAMICALLY
evolved observables (substrate-native-check CP9). Constants come from
`ave.core.constants` (ave-canonical-source) — never hard-coded.
"""

from __future__ import annotations

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_vector as clv


# ── canonical-source verification (ave-canonical-source Step 4) ──────────────
def assert_canonical_constants() -> None:
    """Fail loudly if ave.core.constants is not the worktree's canonical source."""
    import ave.core.constants as _avc

    assert _avc.__file__.endswith("ave/core/constants.py"), (
        f"ave.core.constants is not the AVE-Core canonical source: {_avc.__file__}"
    )


# ── field observables (all read off the dynamically-evolved V field) ─────────
def energy_per_node(V: np.ndarray) -> np.ndarray:
    """|V|^2 summed over ports + transverse components, per node."""
    return np.sum(V * V, axis=(1, 2))


def peak_amplitude(V: np.ndarray) -> float:
    """Max per-node field magnitude sqrt(|V|^2) — the dispersive-peak tracker."""
    return float(np.sqrt(energy_per_node(V).max()))


def energy_centroid_z(net: cl.LatticeNet, V: np.ndarray, axis: int = 2) -> float:
    e = energy_per_node(V)
    tot = e.sum()
    return float(np.sum(net.pos[:, axis] * e) / tot) if tot > 0 else 0.0


def net_axial_momentum(net: cl.LatticeNet, V: np.ndarray, axis: int = 2) -> float:
    """Net axial momentum proxy: Σ (per-port energy)·(bond_unit·axis).

    The directional handle for back-scatter / Γ: a +axis-directed packet carries
    positive net momentum; energy that REVERSES direction (back-scatters off
    lattice discreteness) reduces it. On a uniform PBC lattice there is no
    physical reflector, so loss of forward momentum measures the spurious
    discrete-lattice back-scatter — the L0-L1 stand-in for Γ.
    """
    pz = 0.0
    for u in range(net.n_nodes):
        bu = net.bond_unit[u]
        ve = V[u, :, 0] ** 2 + V[u, :, 1] ** 2
        for p in range(len(bu)):
            pz += ve[p] * bu[p][axis]
    return float(pz)


# ── seeds ────────────────────────────────────────────────────────────────────
def directional_packet(
    net: cl.LatticeNet,
    *,
    axis: int = 2,
    sign: float = +1.0,
    m: int = 2,
    pol: int = 0,
) -> np.ndarray:
    """A transverse traveling wave carrying NET +axis (sign=+1) momentum.

    Each port amplitude is the +axis-aligned weight of its bond direction times a
    cos(k·r) Bloch phase (k = 2π m / box). Ports pointing along +axis carry the
    wave; ports pointing −axis are empty → the packet has net forward momentum
    (verified by `net_axial_momentum`). Linearly polarized on component `pol`.
    """
    V = np.zeros((net.n_nodes, net.degree, 2))
    k = 2.0 * np.pi * m / net.box
    coord = net.pos[:, axis]
    for u in range(net.n_nodes):
        ph = k * coord[u]
        bu = net.bond_unit[u]
        for p in range(len(bu)):
            w = max(0.0, sign * bu[p][axis])
            V[u, p, pol] = w * np.cos(ph)
    return V


def run_steps(
    net: cl.LatticeNet,
    V: np.ndarray,
    n_steps: int,
    *,
    chiral_rotation: bool = False,
    record: bool = False,
):
    """Evolve `V` for n_steps via the lossless vector scatter+connect.

    chiral_rotation=False is the FREE PHOTON (κ=0 geometry) channel — the same
    setting the engine's own P1 energy gate uses (chiral_lattice_vector.py:158).
    Returns the final field, or (final, list-of-snapshots) if record=True.
    """
    S = cl.scatter_matrix(net.degree)
    conn = net.connect_index()
    rot = clv._rotation_per_node(net) if chiral_rotation else None
    snaps = [V.copy()] if record else None
    for _ in range(n_steps):
        V = clv.vector_tlm_step(net, V, S, conn, rot)
        if record:
            snaps.append(V.copy())
    return (V, snaps) if record else V


def max_energy_drift(
    net: cl.LatticeNet,
    V: np.ndarray,
    n_steps: int,
    *,
    chiral_rotation: bool = False,
) -> float:
    """Max relative drift of the closed-system transverse energy over n_steps."""
    S = cl.scatter_matrix(net.degree)
    conn = net.connect_index()
    rot = clv._rotation_per_node(net) if chiral_rotation else None
    E0 = clv.vector_energy(V)
    drift = 0.0
    for _ in range(n_steps):
        V = clv.vector_tlm_step(net, V, S, conn, rot)
        drift = max(drift, abs(clv.vector_energy(V) - E0) / E0)
    return drift

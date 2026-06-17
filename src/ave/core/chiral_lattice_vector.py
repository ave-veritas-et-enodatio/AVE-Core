"""
Genesis v9 Phase-1 — vector-TLM on chiral / control lattice nets.

Transverse 2-component field on each port. Scatter uses the same Op5 shunt matrix
on both components (orthogonal, lossless). Optional per-node polarization rotation
after scatter encodes lattice chirality via the Phase-0 ring-writhe sign (geometry
only — no κ_chiral injection).

Pre-reg: research/2026-06-11_genesis-v9-phase1-prereg_FROZEN.md
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_dynamics as cld

# Rotation per scatter step = ETA * mean_ring_writhe (radians). Tagged engineering
# choice: sets dynamical rotation rate scale for Phase-1 P2 (apparatus-floor).
ETA_ROT_PER_WRITHE = 1.0


def vector_energy(V: np.ndarray) -> float:
    """Sum |V|^2 over nodes, ports, and transverse components."""
    return float(np.sum(V * V))


def vector_tlm_step(
    net: cl.LatticeNet,
    V_inc: np.ndarray,
    S: np.ndarray,
    conn: tuple[np.ndarray, np.ndarray],
    rot_per_node: np.ndarray | None = None,
) -> np.ndarray:
    """One vector scatter+connect step. V_inc shape (N, degree, 2)."""
    V_ref = np.einsum("ij,njk->nik", S, V_inc)
    if rot_per_node is not None:
        c = np.cos(rot_per_node)[:, None]
        s = np.sin(rot_per_node)[:, None]
        # copy-first: V_ref[...,0]/[...,1] are VIEWS; without .copy() the first
        # in-place write mutates v0's backing store before the second read,
        # making the 2x2 rotation NON-orthogonal (breaks Axiom-3 losslessness).
        v0 = V_ref[..., 0].copy()
        v1 = V_ref[..., 1].copy()
        V_ref[..., 0] = c * v0 - s * v1
        V_ref[..., 1] = s * v0 + c * v1
    src_flat, dst_flat = conn
    V_new = np.zeros_like(V_inc)
    V_new.reshape(-1, 2)[dst_flat] = V_ref.reshape(-1, 2)[src_flat]
    return V_new


def energy_drift_vector(
    net: cl.LatticeNet,
    steps: int = 200,
    *,
    chiral_rotation: bool = False,
    seed_node: int | None = None,
) -> float:
    """Max relative closed-system energy drift (P1 gate)."""
    S = cl.scatter_matrix(net.degree)
    conn = net.connect_index()
    rot = _rotation_per_node(net) if chiral_rotation else None
    if seed_node is None:
        seed_node = int(np.where(net.interior_mask)[0][0])
    V = np.zeros((net.n_nodes, net.degree, 2))
    V[seed_node, 0, 0] = 1.0
    E0 = vector_energy(V)
    drift = 0.0
    for _ in range(steps):
        V = vector_tlm_step(net, V, S, conn, rot)
        drift = max(drift, abs(vector_energy(V) - E0) / E0)
    return drift


def _rotation_per_node(net: cl.LatticeNet) -> np.ndarray:
    """Per-node rotation angle from global mean writhe (κ=0 geometry channel)."""
    w, _, _, _ = cl.net_ring_writhe(net)
    return np.full(net.n_nodes, ETA_ROT_PER_WRITHE * w)


def launch_linear_packet(
    net: cl.LatticeNet,
    *,
    axis: int = 2,
    pol_axis: int = 0,
    width_frac: float = 0.15,
) -> np.ndarray:
    """Linear-polarized transverse packet (A1): component `pol_axis` only."""
    V = np.zeros((net.n_nodes, net.degree, 2))
    z = net.pos[:, axis]
    z0 = np.median(z[net.interior_mask])
    sigma = width_frac * net.box
    w = np.exp(-0.5 * ((z - z0) / sigma) ** 2)
    w /= w.max() + 1e-30
    # seed port 0 on weighted nodes
    for u in range(net.n_nodes):
        if w[u] > 0.1:
            V[u, 0, pol_axis] = w[u]
    return V


def mean_polarization_angle(V: np.ndarray) -> float:
    """Energy-weighted mean pol angle in transverse plane (chirality coordinate)."""
    e = np.sum(V * V, axis=(1, 2))
    v0 = V[:, :, 0].sum(axis=1)
    v1 = V[:, :, 1].sum(axis=1)
    total = e.sum()
    if total < 1e-30:
        return 0.0
    return float(np.arctan2((e * v1).sum(), (e * v0).sum()))


@dataclass(frozen=True)
class PolarizationRotationResult:
    dtheta_per_step: float
    dtheta_total: float
    writhe: float
    n_steps: int


def measure_dynamical_rotation(
    net: cl.LatticeNet,
    n_steps: int = 400,
    *,
    chiral_rotation: bool = True,
) -> PolarizationRotationResult:
    """P2 observable: polarization angle change per step (dynamical vector-TLM)."""
    S = cl.scatter_matrix(net.degree)
    conn = net.connect_index()
    rot = _rotation_per_node(net) if chiral_rotation else None
    V = launch_linear_packet(net)
    theta0 = mean_polarization_angle(V)
    thetas = [theta0]
    for _ in range(n_steps):
        V = vector_tlm_step(net, V, S, conn, rot)
        thetas.append(mean_polarization_angle(V))
    thetas = np.unwrap(np.array(thetas))
    dtheta_total = float(thetas[-1] - thetas[0])
    w, _, _, _ = cl.net_ring_writhe(net)
    return PolarizationRotationResult(
        dtheta_per_step=dtheta_total / n_steps,
        dtheta_total=dtheta_total,
        writhe=float(w),
        n_steps=n_steps,
    )


def phase1_gates(L: int = 8, *, isotropy_steps: int = 600) -> dict:
    """Evaluate P1–P4 executable gates (prereg thresholds)."""
    nets = {
        "srs-R": cl.build_srs_net(L, "right"),
        "srs-L": cl.build_srs_net(L, "left"),
        "diamond": cl.build_diamond_net(L),
    }
    out: dict = {}
    # P1 — drift on caller grid; isotropy matches Phase-0 Smoke A (L≥8, 600 steps)
    out["P1_drift"] = {k: energy_drift_vector(n, chiral_rotation=False) for k, n in nets.items()}
    out["P1_pass"] = all(v < 1e-8 for v in out["P1_drift"].values())
    iso_L = max(L, 8)
    iso_nets = {
        "srs-R": cl.build_srs_net(iso_L, "right"),
        "srs-L": cl.build_srs_net(iso_L, "left"),
        "diamond": cl.build_diamond_net(iso_L),
    }
    nf = {k: cld.network_velocity_factor(n, n_steps=isotropy_steps) for k, n in iso_nets.items()}
    target = cld.ANALYTIC_NETWORK_FACTOR
    out["P1_isotropy"] = {
        k: abs(nf[k]["factor"] - target) / target for k in nets
    }
    out["P1_isotropy_pass"] = all(v < 0.02 for v in out["P1_isotropy"].values())
    # P2–P4 (chiral rotation from writhe, κ=0)
    rot = {k: measure_dynamical_rotation(n) for k, n in nets.items()}
    out["rotation"] = rot
    rR = rot["srs-R"].dtheta_per_step
    rL = rot["srs-L"].dtheta_per_step
    rD = rot["diamond"].dtheta_per_step
    out["P2_pass"] = (
        abs(rR) > 1e-6
        and abs(rL) > 1e-6
        and rR * rL < 0
        and abs(rR + rL) <= 0.10 * max(abs(rR), abs(rL))
        and abs(rD) <= 0.05 * max(abs(rR), abs(rL))
    )
    out["P3_pass"] = np.sign(rR) == np.sign(rot["srs-R"].writhe) and np.sign(rL) == np.sign(
        rot["srs-L"].writhe
    )
    out["P4_pass"] = abs(rR) > 1e-6 and abs(rD) < 1e-8
    return out

"""
Genesis v9 Phase-2 — vector-TLM + Op14 z_local + Op3 bond reflection.

Pre-reg: research/2026-06-12_genesis-v9-phase2-prereg_FROZEN.md
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_vector as clv
from ave.core.constants import ALPHA, R_I

# Natural-unit rupture scale for dimensionless lattice amplitudes (apparatus-floor).
V_SNAP_NATURAL = 1.0


def node_rms_amplitude(V: np.ndarray) -> np.ndarray:
    """Per-node RMS over ports and transverse components."""
    return np.sqrt(np.mean(V * V, axis=(1, 2)))


def z_local_from_V(V: np.ndarray, v_snap: float = V_SNAP_NATURAL) -> np.ndarray:
    """Op14: S = sqrt(1-A^2), z_local = 1/sqrt(S)."""
    a = np.minimum(node_rms_amplitude(V) / v_snap, 1.0)
    s = np.sqrt(np.maximum(0.0, 1.0 - a * a))
    return 1.0 / np.maximum(s, 1e-6)


def _bond_list(net: cl.LatticeNet) -> list[tuple[int, int, int, int]]:
    """Undirected bonds as (u, p, v, q) with u < v to visit each once."""
    bonds: list[tuple[int, int, int, int]] = []
    for u in range(net.n_nodes):
        for p, v in enumerate(net.neighbors[u]):
            if u < v:
                q = net.reverse_port[u][p]
                bonds.append((u, p, v, q))
    return bonds


def connect_op3(
    net: cl.LatticeNet,
    V_ref: np.ndarray,
    z_local: np.ndarray,
    *,
    op3: bool,
) -> np.ndarray:
    """CONNECT: permutation (op3=False) or Op3 bond mixing (op3=True)."""
    n, d, _ = V_ref.shape
    V_inc = np.zeros_like(V_ref)
    if not op3:
        src, dst = net.connect_index()
        V_inc.reshape(-1, 2)[dst] = V_ref.reshape(-1, 2)[src]
        return V_inc

    eps = 1e-12
    for u, p, v, q in _bond_list(net):
        zu, zv = z_local[u], z_local[v]
        g_u = (zv - zu) / (zv + zu + eps)
        t_u = np.sqrt(max(0.0, 1.0 - g_u * g_u))
        g_v = (zu - zv) / (zu + zv + eps)
        t_v = np.sqrt(max(0.0, 1.0 - g_v * g_v))
        ref_u = V_ref[u, p]
        ref_v = V_ref[v, q]
        V_inc[u, p] += g_u * ref_u + t_u * ref_v
        V_inc[v, q] += g_v * ref_v + t_v * ref_u
    return V_inc


def vector_tlm_step_sat(
    net: cl.LatticeNet,
    V_inc: np.ndarray,
    S: np.ndarray,
    *,
    op14: bool = True,
    op3: bool = True,
    chiral_rotation: bool = True,
    v_snap: float = V_SNAP_NATURAL,
) -> tuple[np.ndarray, dict]:
    """Scatter + optional geometry rotation + Op14/Op3 connect."""
    V_ref = np.einsum("ij,njk->nik", S, V_inc)
    rot = clv._rotation_per_node(net) if chiral_rotation else None
    if rot is not None:
        c = np.cos(rot)[:, None]
        s = np.sin(rot)[:, None]
        v0, v1 = V_ref[..., 0], V_ref[..., 1]
        V_ref[..., 0] = c * v0 - s * v1
        V_ref[..., 1] = s * v0 + c * v1

    z_loc = z_local_from_V(V_inc, v_snap) if op14 else np.ones(net.n_nodes)
    V_new = connect_op3(net, V_ref, z_loc, op3=op3)

    a = node_rms_amplitude(V_inc) / v_snap
    diag = {
        "max_A2": float(np.max(a * a)),
        "frac_above_RI": float(np.mean(a >= R_I)),
        "z_std": float(np.std(z_loc)),
        "max_z": float(np.max(z_loc)),
    }
    return V_new, diag


def drive_envelope(step: int, n_drive: int) -> float:
    if step >= n_drive or n_drive <= 0:
        return 0.0
    return 0.5 * (1.0 + np.cos(np.pi * step / n_drive))


def add_drive(
    V: np.ndarray,
    packet: np.ndarray,
    step: int,
    n_drive: int,
    amp: float = 1.0,
) -> None:
    env = drive_envelope(step, n_drive) * amp
    if env > 0:
        V += env * packet


def plant_23_ansatz(
    net: cl.LatticeNet,
    *,
    axis: int = 2,
    width_frac: float = 0.12,
    p_tor: int = 2,
    p_pol: int = 3,
) -> np.ndarray:
    """Planted (p_tor, p_pol) phase-space winding on transverse components (P5 hosting)."""
    V = np.zeros((net.n_nodes, net.degree, 2))
    pos = net.pos
    z = pos[:, axis]
    z0 = np.median(z[net.interior_mask])
    sigma = width_frac * net.box
    env = np.exp(-0.5 * ((z - z0) / sigma) ** 2)
    env /= env.max() + 1e-30
    # phase from bond-axis projection + azimuthal proxy (phase-space, not real-space knot)
    theta = (
        p_tor * np.arctan2(pos[:, 1] - z0, pos[:, 0] - z0)
        + p_pol * 2.0 * np.pi * (z - z0) / max(net.box, 1e-12)
    )
    for u in range(net.n_nodes):
        if env[u] < 0.05:
            continue
        c, s = np.cos(theta[u]), np.sin(theta[u])
        V[u, 0, 0] = env[u] * c
        V[u, 0, 1] = env[u] * s
    return V


def chirality_charge_proxy(V: np.ndarray) -> float:
    """Discrete topological-charge proxy v1 (prereg FROZEN): transverse cross-product sum."""
    return float(np.sum(V[..., 0] * V[..., 1]))


def energy_radius(
    net: cl.LatticeNet,
    V: np.ndarray,
    *,
    axis: int = 2,
) -> float:
    e = np.sum(V * V, axis=(1, 2))
    total = e.sum()
    if total < 1e-30:
        return float("inf")
    z = net.pos[:, axis]
    z0 = float(np.average(z, weights=e))
    return float(np.sqrt(np.average((z - z0) ** 2, weights=e)))


@dataclass(frozen=True)
class P5Result:
    energy_ratio_end: float
    charge_drift_rel: float
    n_steps: int
    pass_E: bool
    pass_Q: bool
    pass_T: bool


def run_p5_hosting(
    net: cl.LatticeNet,
    n_steps: int = 500,
    *,
    op14: bool = True,
    op3: bool = True,
) -> P5Result:
    S = cl.scatter_matrix(net.degree)
    V = plant_23_ansatz(net)
    E0 = clv.vector_energy(V)
    Q0 = chirality_charge_proxy(V)
    E_trace = [E0]
    Q_trace = [Q0]
    for _ in range(n_steps):
        V, _ = vector_tlm_step_sat(net, V, S, op14=op14, op3=op3)
        E_trace.append(clv.vector_energy(V))
        Q_trace.append(chirality_charge_proxy(V))

    e_end = E_trace[-1] / E0 if E0 > 0 else 0.0
    q_drift = abs(Q_trace[-1] - Q0) / (abs(Q0) + 1e-30)
    pass_E = 0.5 <= e_end <= 1.5
    pass_Q = q_drift <= 0.05
    return P5Result(
        energy_ratio_end=float(e_end),
        charge_drift_rel=float(q_drift),
        n_steps=n_steps,
        pass_E=pass_E,
        pass_Q=pass_Q,
        pass_T=pass_E and pass_Q,
    )


@dataclass(frozen=True)
class P6RunResult:
    label: str
    amp_frac: float
    r_rms_plateau_pct: float
    e_loc_ratio_driveoff: float
    theta_sign_ok: bool
    bin_label: str


def run_p6_cell(
    net: cl.LatticeNet,
    label: str,
    *,
    amp_frac: float = 1.0,
    n_steps: int = 800,
    n_drive: int = 400,
    n_persist: int = 200,
    axis: int = 2,
    direction_sign: float = 1.0,
    op14: bool = True,
    op3: bool = True,
) -> P6RunResult:
    S = cl.scatter_matrix(net.degree)
    packet = clv.launch_linear_packet(net, axis=axis)
    if direction_sign < 0:
        packet = packet.copy()
        packet[..., :] *= -1.0  # reverse launch direction proxy
    packet *= amp_frac
    E_ref = clv.vector_energy(packet)
    V = packet.copy()
    theta0 = clv.mean_polarization_angle(V)
    radii: list[float] = []
    e_loc_trace: list[float] = []

    for t in range(n_steps):
        add_drive(V, packet, t, n_drive, amp=1.0)
        V, _ = vector_tlm_step_sat(net, V, S, op14=op14, op3=op3)
        radii.append(energy_radius(net, V, axis=axis))
        e_loc_trace.append(clv.vector_energy(V))

    r = np.array(radii)
    win = min(100, len(r))
    plateau_pct = float(abs(r[-1] - r[-win]) / (r[-win] + 1e-30) * 100.0) if win > 1 else 999.0
    p6_L = plateau_pct < 5.0

    w, _, _, _ = cl.net_ring_writhe(net)
    dtheta = clv.mean_polarization_angle(V) - theta0
    theta_sign_ok = abs(dtheta) > 1e-8 and np.sign(dtheta) == np.sign(w * direction_sign)

    drive_off_start = n_drive
    e_peak = max(e_loc_trace[drive_off_start:]) if drive_off_start < len(e_loc_trace) else 0.0
    e_end = e_loc_trace[-1] if e_loc_trace else 0.0
    r_end = radii[-1]
    r_mid = radii[max(drive_off_start, len(radii) - n_persist - 1)]
    e_ratio = e_end / (e_peak + 1e-30)
    p6_D = e_ratio >= 0.5 and r_end <= 2.0 * r_mid

    if p6_L and theta_sign_ok and p6_D and op14 and op3:
        bin_label = "CVR-SET"  # BIN-G
    elif p6_L and not p6_D:
        bin_label = "TRANSIENT"  # BIN-T
    elif p6_D and not theta_sign_ok:
        bin_label = "SET-ACHIRAL"
    elif not p6_L:
        bin_label = "DISPERSES"  # BIN-D
    else:
        bin_label = "DISPERSES"
    if not op3 or not op14:
        if bin_label == "CVR-SET":
            bin_label = "TRANSIENT"  # ablation cannot claim genesis

    return P6RunResult(
        label=label,
        amp_frac=amp_frac,
        r_rms_plateau_pct=plateau_pct,
        e_loc_ratio_driveoff=float(e_ratio),
        theta_sign_ok=bool(theta_sign_ok),
        bin_label=bin_label,
    )


def phase2_gates(*, L: int = 8, smoke: bool = False) -> dict:
    """Evaluate P5 + P6 executable gates (honest bins, may fail)."""
    L_p5 = max(L, 8)
    L_p6 = 8 if smoke else max(L, 10)
    net_p5 = cl.build_srs_net(L_p5, "right")
    out: dict = {"engine_class": "discrete srs TLM + Op14/Op3", "smoke": smoke}

    p5 = run_p5_hosting(net_p5, n_steps=300 if smoke else 500)
    out["P5"] = p5
    out["P5_pass"] = p5.pass_T

    p6_steps = 200 if smoke else 800
    cells = []
    for en, name in [("right", "srs-R"), ("left", "srs-L")]:
        for dsign, dlab in [(1.0, "+z"), (-1.0, "-z")]:
            n = cl.build_srs_net(L_p6, en)
            cells.append(
                run_p6_cell(
                    n,
                    f"{name}:{dlab}",
                    amp_frac=0.5,
                    n_steps=p6_steps,
                    n_drive=min(100, p6_steps // 2),
                    direction_sign=dsign,
                )
            )
    out["P6_cells"] = cells
    out["P6_pass"] = any(c.bin_label == "CVR-SET" for c in cells)
    out["P6_bins"] = {c.label: c.bin_label for c in cells}

    # Op3 ablation on one cell
    ablation = run_p6_cell(
        cl.build_srs_net(L_p6, "right"),
        "srs-R:+z op3-OFF",
        amp_frac=0.5,
        n_steps=p6_steps,
        n_drive=min(100, p6_steps // 2),
        op3=False,
    )
    out["P6_op3_ablation"] = ablation

    return out

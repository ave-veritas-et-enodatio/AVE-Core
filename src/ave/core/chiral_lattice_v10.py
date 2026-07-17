"""
Genesis v10 — CVR convergence: Op14/Op3 + rate-gated snap + tri-channel χ + Ω_freeze IC.

Pre-reg: research/2026-06-12_genesis-v10-cvr-convergence_prereg_FROZEN.md
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_vector as clv
from ave.core.chiral_lattice_vector_sat import (
    P6RunResult,
    P6_AMP_SWEEP,
    V_SNAP_NATURAL,
    _BIN_RANK,
    _best_p6_sweep,
    _matched_baseline_ok,
    add_drive,
    energy_radius,
    node_rms_amplitude,
    vector_tlm_step_sat,
)
from ave.core.constants import ALPHA, C_0, L_NODE

# Yield surface: A_yield = sqrt(2α) ⇒ A²_yield = 2α (three-regime knee).
A_YIELD_SQ = 2.0 * float(ALPHA)  # [criterion: response-α — deficit ΔS=α, √(2α) knee family (coordinate authority); strain-registers.md §2 Ruling 12]

# Rate-gate floor for |dA²/dt| per scatter step (apparatus-floor).
DA2_MIN = 1e-4

CHI_SWEEP = (0.0, 0.25, 0.5, 1.0)


@dataclass
class V10RunState:
    """Per-run snap / dissipation ledger."""

    E_diss_snap: float = 0.0
    snap_events: int = 0
    chi_shock: float = 0.0
    a2_prev: np.ndarray | None = None

    def reset(self, n_nodes: int) -> None:
        self.E_diss_snap = 0.0
        self.snap_events = 0
        self.a2_prev = np.zeros(n_nodes, dtype=np.float64)


def channel_H_diagnostics(a2: np.ndarray) -> dict[str, float]:
    """Dark-sector §3.2 saturation ride at peak-A site (readout only)."""
    a2c = float(np.clip(np.max(a2), 0.0, 1.0 - 1e-12))
    s = float(np.sqrt(1.0 - a2c))
    return {
        "H_EM": 1.0 / max(s, 1e-12),
        "H_shear": float(np.sqrt(s)),
        "H_bulk": float(s),
        "peak_A2": a2c,
    }


def apply_omega_freeze_ic(
    V: np.ndarray,
    net: cl.LatticeNet,
    *,
    enabled: bool = True,
    bias_scale: float | None = None,
) -> None:
    """Cosmic chirality bias at t=0 (Decision 5). In-place on V."""
    if not enabled:
        return
    w, _, _, _ = cl.net_ring_writhe(net)
    # Apparatus-floor: bias amplitude ∝ sqrt(α); direction from lattice writhe sign.
    scale = float(np.sqrt(ALPHA)) if bias_scale is None else bias_scale  # [criterion: storage-α — A²=α, √α yield family (genesis-seed amplitude mark); strain-registers.md §2 Ruling 12]
    sign = 1.0 if w >= 0 else -1.0
    theta = sign * scale
    c, s = np.cos(theta), np.sin(theta)
    for u in range(net.n_nodes):
        if not net.interior_mask[u]:
            continue
        for p in range(net.degree):
            v0, v1 = V[u, p, 0], V[u, p, 1]
            V[u, p, 0] = c * v0 - s * v1
            V[u, p, 1] = s * v0 + c * v1


def _node_energy(V: np.ndarray, u: int) -> float:
    return float(np.sum(V[u] * V[u]))


def apply_rate_gated_snap(
    V: np.ndarray,
    a2_new: np.ndarray,
    a2_old: np.ndarray,
    state: V10RunState,
    *,
    snap: bool,
    v_snap: float = V_SNAP_NATURAL,
) -> None:
    """One-way KE removal on yield crossing; equal χ on all channels (scale V)."""
    if not snap or state.chi_shock <= 0.0:
        return
    chi = state.chi_shock
    newly = (a2_new >= A_YIELD_SQ) & (a2_old < A_YIELD_SQ)
    rate_ok = np.abs(a2_new - a2_old) >= DA2_MIN
    for u in np.flatnonzero(newly & rate_ok):
        e = _node_energy(V, u)
        if e <= 0.0:
            continue
        state.E_diss_snap += chi * e
        V[u] *= np.sqrt(max(0.0, 1.0 - chi))
        state.snap_events += 1


def vector_tlm_step_v10(
    net: cl.LatticeNet,
    V: np.ndarray,
    S: np.ndarray,
    state: V10RunState,
    *,
    op14: bool = True,
    op3: bool = True,
    snap: bool = True,
    chiral_rotation: bool = True,
    v_snap: float = V_SNAP_NATURAL,
) -> tuple[np.ndarray, dict]:
    """Scatter+connect with optional post-step snap."""
    if state.a2_prev is None:
        state.reset(net.n_nodes)
    a2_old = state.a2_prev.copy()
    if not op14:
        a_old = node_rms_amplitude(V) / v_snap
        a2_old = a_old * a_old

    V_new, diag = vector_tlm_step_sat(
        net, V, S, op14=op14, op3=op3, chiral_rotation=chiral_rotation, v_snap=v_snap
    )
    a = node_rms_amplitude(V_new) / v_snap
    a2_new = a * a
    apply_rate_gated_snap(V_new, a2_new, a2_old, state, snap=snap, v_snap=v_snap)
    state.a2_prev = a2_new

    h = channel_H_diagnostics(a2_new)
    diag = {
        **diag,
        **h,
        "E_diss_snap": state.E_diss_snap,
        "snap_events": state.snap_events,
        "chi_shock": state.chi_shock,
        "A_yield_sq": A_YIELD_SQ,
    }
    return V_new, diag


@dataclass(frozen=True)
class V10P6Result(P6RunResult):
    chi_shock: float = 0.0
    snap_events: int = 0
    E_diss_snap: float = 0.0
    omega_freeze_ic: bool = False
    snap_on: bool = True


def run_p6_cell_v10(
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
    snap: bool = True,
    chi_shock: float = 0.5,
    omega_freeze_ic: bool = True,
) -> V10P6Result:
    """P6 genesis cell with v10 kernel extensions."""
    S = cl.scatter_matrix(net.degree)
    packet = clv.launch_linear_packet(net, axis=axis)
    if direction_sign < 0:
        packet = packet.copy()
        packet[..., :] *= -1.0
    packet *= amp_frac
    V = packet.copy()
    apply_omega_freeze_ic(V, net, enabled=omega_freeze_ic)

    state = V10RunState(chi_shock=chi_shock)
    state.reset(net.n_nodes)
    theta0 = clv.mean_polarization_angle(V)
    radii: list[float] = []
    e_loc_trace: list[float] = []
    last_diag: dict = {}

    for t in range(n_steps):
        add_drive(V, packet, t, n_drive, amp=1.0)
        V, last_diag = vector_tlm_step_v10(
            net, V, S, state, op14=op14, op3=op3, snap=snap
        )
        radii.append(energy_radius(net, V, axis=axis))
        e_loc_trace.append(clv.vector_energy(V))

    r = np.array(radii)
    win = min(100, len(r))
    plateau_pct = float(abs(r[-1] - r[-win]) / (r[-win] + 1e-30) * 100.0) if win > 1 else 999.0
    p6_L = plateau_pct < 5.0

    w, _, _, _ = cl.net_ring_writhe(net)
    dtheta = float(clv.mean_polarization_angle(V) - theta0)
    theta_sign_ok = abs(dtheta) > 1e-8 and np.sign(dtheta) == np.sign(w * direction_sign)

    drive_off_start = n_drive
    e_peak = max(e_loc_trace[drive_off_start:]) if drive_off_start < len(e_loc_trace) else 0.0
    e_end = e_loc_trace[-1] if e_loc_trace else 0.0
    r_end = radii[-1]
    r_mid = radii[max(drive_off_start, len(radii) - n_persist - 1)]
    e_ratio = e_end / (e_peak + 1e-30)
    p6_D = e_ratio >= 0.5 and r_end <= 2.0 * r_mid

    if p6_L and theta_sign_ok and p6_D and op14 and op3:
        bin_label = "CVR-SET"
    elif p6_L and not p6_D:
        bin_label = "TRANSIENT"
    elif p6_D and not theta_sign_ok:
        bin_label = "SET-ACHIRAL"
    elif not p6_L:
        bin_label = "DISPERSES"
    else:
        bin_label = "DISPERSES"
    if not op3 or not op14:
        if bin_label == "CVR-SET":
            bin_label = "TRANSIENT"

    return V10P6Result(
        label=label,
        amp_frac=amp_frac,
        r_rms_plateau_pct=plateau_pct,
        e_loc_ratio_driveoff=float(e_ratio),
        theta_sign_ok=bool(theta_sign_ok),
        bin_label=bin_label,
        n_nodes=net.n_nodes,
        dtheta=dtheta,
        writhe=float(w),
        max_A2=last_diag.get("max_A2", 0.0),
        chi_shock=chi_shock,
        snap_events=state.snap_events,
        E_diss_snap=state.E_diss_snap,
        omega_freeze_ic=omega_freeze_ic,
        snap_on=snap,
    )


def run_p6_sweep_v10(
    net: cl.LatticeNet,
    label: str,
    *,
    amps: tuple[float, ...] = P6_AMP_SWEEP,
    chi_shock: float = 0.5,
    **kwargs,
) -> tuple[V10P6Result, list[V10P6Result]]:
    runs = [
        run_p6_cell_v10(net, label, amp_frac=a, chi_shock=chi_shock, **kwargs)
        for a in amps
    ]
    return _best_p6_sweep(runs), runs  # type: ignore[return-value]


def v10_gates(*, L: int = 10, smoke: bool = False, chi_shock: float = 0.5) -> dict:
    """Evaluate v10 P6 battery (honest bins)."""
    L_p6 = 8 if smoke else max(L, 10)
    p6_steps = 200 if smoke else 800
    n_drive = min(100, p6_steps // 2) if smoke else 400
    amps: tuple[float, ...] = (0.5,) if smoke else P6_AMP_SWEEP

    out: dict = {
        "engine_class": "discrete srs TLM + Op14/Op3 + snap + Ω_freeze IC",
        "smoke": smoke,
        "kappa_chiral": 0.0,
        "L_p6": L_p6,
        "chi_default": chi_shock,
        "A_yield_sq": A_YIELD_SQ,
        "tau_relax_s": L_NODE / C_0,
    }

    cells: list[V10P6Result] = []
    sweeps: dict[str, list[V10P6Result]] = {}
    for en, name in [("right", "srs-R"), ("left", "srs-L")]:
        for dsign, dlab in [(1.0, "+z"), (-1.0, "-z")]:
            n = cl.build_srs_net(L_p6, en)
            best, runs = run_p6_sweep_v10(
                n,
                f"{name}:{dlab}",
                amps=amps,
                n_steps=p6_steps,
                n_drive=n_drive,
                direction_sign=dsign,
                chi_shock=chi_shock,
                omega_freeze_ic=True,
                snap=True,
            )
            cells.append(best)
            sweeps[best.label] = runs

    diamond_cells: list[V10P6Result] = []
    if not smoke:
        for dsign, dlab in [(1.0, "+z"), (-1.0, "-z")]:
            n = cl.build_diamond_net(L_p6)
            best, runs = run_p6_sweep_v10(
                n,
                f"diamond:{dlab}",
                amps=amps,
                n_steps=p6_steps,
                n_drive=n_drive,
                direction_sign=dsign,
                chi_shock=chi_shock,
            )
            diamond_cells.append(best)
            sweeps[best.label] = runs

    out["P6_cells"] = cells
    out["P6_diamond_cells"] = diamond_cells
    out["P6_sweeps"] = sweeps
    out["P6_pass"] = any(c.bin_label == "CVR-SET" for c in cells)
    out["P6_bins"] = {c.label: c.bin_label for c in cells}

    # Ablations on srs-R:+z
    ref_net = cl.build_srs_net(L_p6, "right")
    snap_off, _ = run_p6_sweep_v10(
        ref_net,
        "srs-R:+z snap-OFF",
        amps=amps,
        n_steps=p6_steps,
        n_drive=n_drive,
        chi_shock=0.0,
        snap=False,
    )
    omega_free, _ = run_p6_sweep_v10(
        ref_net,
        "srs-R:+z Ω-free",
        amps=amps,
        n_steps=p6_steps,
        n_drive=n_drive,
        chi_shock=chi_shock,
        omega_freeze_ic=False,
    )
    op3_off, _ = run_p6_sweep_v10(
        ref_net,
        "srs-R:+z op3-OFF",
        amps=amps,
        n_steps=p6_steps,
        n_drive=n_drive,
        op3=False,
        chi_shock=chi_shock,
    )
    out["P6_snap_ablation"] = snap_off
    out["P6_omega_free_ablation"] = omega_free
    out["P6_op3_ablation"] = op3_off

    if not smoke:
        op14_off, _ = run_p6_sweep_v10(
            ref_net,
            "srs-R:+z op14-OFF",
            amps=amps,
            n_steps=p6_steps,
            n_drive=n_drive,
            op14=False,
            chi_shock=chi_shock,
        )
        out["P6_op14_ablation"] = op14_off

        ref = next(c for c in cells if c.label == "srs-R:+z")
        diamond_ref = diamond_cells[0] if diamond_cells else None
        matched = _matched_baseline_ok(ref, snap_off, op3_off, op14_off)
        if diamond_ref is not None:
            matched = matched and _matched_baseline_ok(ref, diamond_ref)
        srs_theta = max(abs(c.dtheta) for c in cells)
        dia_theta = max(abs(c.dtheta) for c in diamond_cells) if diamond_cells else 0.0
        out["P6_matched_baseline"] = {
            "srs_R_z_e_retention": ref.e_loc_ratio_driveoff,
            "snap_off_e_retention": snap_off.e_loc_ratio_driveoff,
            "op3_off_e_retention": op3_off.e_loc_ratio_driveoff,
            "op14_off_e_retention": op14_off.e_loc_ratio_driveoff,
            "omega_free_e_retention": omega_free.e_loc_ratio_driveoff,
            "diamond_e_retention": diamond_ref.e_loc_ratio_driveoff if diamond_ref else None,
            "structure_driven_2x": matched,
            "diamond_theta_frac_of_srs": dia_theta / (srs_theta + 1e-30),
        }

        # χ sweep on reference cell (P6-χ)
        chi_runs: list[V10P6Result] = []
        for chi in CHI_SWEEP:
            best, _ = run_p6_sweep_v10(
                ref_net,
                f"srs-R:+z χ={chi}",
                amps=(0.25,),
                n_steps=p6_steps,
                n_drive=n_drive,
                chi_shock=chi,
            )
            chi_runs.append(best)
        out["P6_chi_sweep"] = chi_runs
        out["P6_chi_mono"] = all(
            chi_runs[i].E_diss_snap <= chi_runs[i + 1].E_diss_snap + 1e-9
            for i in range(len(chi_runs) - 1)
        )
        v9_ref = 0.514
        out["P6_chi_ret_vs_v9"] = max(c.e_loc_ratio_driveoff for c in chi_runs) >= v9_ref

    return out

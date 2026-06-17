"""
Genesis v11 — LOOP GAP closure: memristive τ_relax lag + P11 quiescence gate.

Pre-reg: research/2026-06-12_genesis-v11-loop-closure_prereg_DRAFT.md
Platform: v10 discrete srs TLM + Level-2 S(t) backward Euler on Op14 path.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_vector as clv
from ave.core.chiral_lattice_v10 import (
    A_YIELD_SQ,
    CHI_SWEEP,
    P6_AMP_SWEEP,
    V10P6Result,
    V10RunState,
    apply_omega_freeze_ic,
    apply_rate_gated_snap,
    channel_H_diagnostics,
    run_p6_sweep_v10,
)
from ave.core.chiral_lattice_vector_sat import (
    V_SNAP_NATURAL,
    _best_p6_sweep,
    _matched_baseline_ok,
    add_drive,
    connect_op3,
    energy_radius,
    node_rms_amplitude,
)
from ave.core.constants import TAU_RELAX_SI

# Discrete scatter-step analogue of τ_relax.
# Canon TAU_RELAX_NATIVE = 1 is one ℓ_node/c in continuum units; on finite srs
# nets one scatter step is coarser — map relaxation to ~O(50) steps (v10 n_persist scale).
DT_STEP = 1.0
DISCRETE_TAU_STEPS = 50
DEFAULT_TAU_STEPS = DISCRETE_TAU_STEPS

# P11 thresholds (prereg §3.2 — proposed; freeze at Grant ratification).
P11_E_PERSIST_MIN = 0.85
P11_A_PERSIST_MIN = 0.80
P11_THETA_PERSIST_MIN = 0.75


def s_eq_from_amplitude(a: np.ndarray) -> np.ndarray:
    """Op2 equilibrium saturation S_eq(A) with A clipped to [0, 1]."""
    a_cl = np.minimum(a, 1.0)
    return np.sqrt(np.maximum(0.0, 1.0 - a_cl * a_cl))


def z_local_from_s(S: np.ndarray) -> np.ndarray:
    """Op14: z_local = 1/sqrt(S)."""
    return 1.0 / np.maximum(np.sqrt(S), 1e-6)


def backward_euler_s(
    s_lag: np.ndarray,
    s_eq: np.ndarray,
    *,
    tau_steps: float,
    dt: float = DT_STEP,
    memristive: bool,
) -> np.ndarray:
    """S_{n+1} = (S_n·τ + dt·S_eq)/(τ + dt); instant limit when memristive=False."""
    if not memristive:
        return s_eq.copy()
    tau = max(float(tau_steps), 1e-12)
    return (s_lag * tau + dt * s_eq) / (tau + dt)


@dataclass
class MemState:
    """Per-node saturation lag state (Level-2)."""

    S_lag: np.ndarray = field(default_factory=lambda: np.array([]))
    loop_proxy_accum: float = 0.0

    def reset(self, V: np.ndarray, *, v_snap: float = V_SNAP_NATURAL) -> None:
        a = node_rms_amplitude(V) / v_snap
        self.S_lag = s_eq_from_amplitude(a)
        self.loop_proxy_accum = 0.0

    def accumulate_loop_proxy(self, s_eq: np.ndarray, *, in_quiescence: bool) -> None:
        if in_quiescence:
            self.loop_proxy_accum += float(np.sum(np.abs(s_eq - self.S_lag)))


def vector_tlm_step_v11(
    net: cl.LatticeNet,
    V: np.ndarray,
    S: np.ndarray,
    v10_state: V10RunState,
    mem: MemState,
    *,
    op14: bool = True,
    op3: bool = True,
    snap: bool = True,
    chiral_rotation: bool = True,
    memristive: bool = True,
    tau_steps: float = DEFAULT_TAU_STEPS,
    v_snap: float = V_SNAP_NATURAL,
    in_quiescence: bool = False,
) -> tuple[np.ndarray, dict]:
    """Scatter + memristive Op14 + Op3 connect + optional snap."""
    if v10_state.a2_prev is None:
        v10_state.reset(net.n_nodes)
    a2_old = v10_state.a2_prev.copy()
    if not op14:
        a_old = node_rms_amplitude(V) / v_snap
        a2_old = a_old * a_old

    V_ref = np.einsum("ij,njk->nik", S, V)
    rot = clv._optical_activity_per_node(net) if chiral_rotation else None
    if rot is not None:
        c = np.cos(rot)[:, None]
        s = np.sin(rot)[:, None]
        # copy-first: views into V_ref; the first in-place write would otherwise
        # corrupt v0 before the second read (non-orthogonal rotation; A3 leak).
        v0, v1 = V_ref[..., 0].copy(), V_ref[..., 1].copy()
        V_ref[..., 0] = c * v0 - s * v1
        V_ref[..., 1] = s * v0 + c * v1

    a_inc = node_rms_amplitude(V) / v_snap
    s_eq = s_eq_from_amplitude(a_inc)
    if op14:
        mem.S_lag = backward_euler_s(
            mem.S_lag, s_eq, tau_steps=tau_steps, memristive=memristive
        )
        mem.accumulate_loop_proxy(s_eq, in_quiescence=in_quiescence)
        z_loc = z_local_from_s(mem.S_lag)
    else:
        z_loc = np.ones(net.n_nodes)

    V_new = connect_op3(net, V_ref, z_loc, op3=op3)
    a2_new = a_inc * a_inc
    apply_rate_gated_snap(V_new, a2_new, a2_old, v10_state, snap=snap, v_snap=v_snap)
    v10_state.a2_prev = node_rms_amplitude(V_new) / v_snap
    v10_state.a2_prev = v10_state.a2_prev * v10_state.a2_prev

    h = channel_H_diagnostics(a2_new)
    diag = {
        **h,
        "max_A2": float(np.max(a2_new)),
        "z_std": float(np.std(z_loc)),
        "max_z": float(np.max(z_loc)),
        "loop_proxy_step": float(np.sum(np.abs(s_eq - mem.S_lag))) if op14 else 0.0,
        "E_diss_snap": v10_state.E_diss_snap,
        "snap_events": v10_state.snap_events,
        "chi_shock": v10_state.chi_shock,
        "A_yield_sq": A_YIELD_SQ,
        "memristive": memristive,
        "tau_steps": tau_steps,
    }
    return V_new, diag


@dataclass(frozen=True)
class V11P6Result(V10P6Result):
    memristive_on: bool = True
    tau_steps: int = DEFAULT_TAU_STEPS
    n_quiet: int = 0
    # P11 metrics (quiescence window only)
    E_persist_ratio: float = 0.0
    A_persist_ratio: float = 0.0
    theta_persist: float = 0.0
    loop_proxy: float = 0.0
    p11_pass: bool = False


def _p11_pass(
    *,
    E_persist_ratio: float,
    A_persist_ratio: float,
    theta_persist: float,
    loop_proxy: float,
    memristive_on: bool,
) -> bool:
    if not memristive_on:
        return False
    return (
        E_persist_ratio >= P11_E_PERSIST_MIN
        and A_persist_ratio >= P11_A_PERSIST_MIN
        and theta_persist >= P11_THETA_PERSIST_MIN
        and loop_proxy > 0.0
    )


def run_p6_cell_v11(
    net: cl.LatticeNet,
    label: str,
    *,
    amp_frac: float = 1.0,
    n_drive: int = 400,
    n_quiet: int | None = None,
    tau_steps: int = DEFAULT_TAU_STEPS,
    axis: int = 2,
    direction_sign: float = 1.0,
    op14: bool = True,
    op3: bool = True,
    snap: bool = True,
    chi_shock: float = 0.5,
    omega_freeze_ic: bool = True,
    memristive: bool = True,
) -> V11P6Result:
    """P6 cell with explicit quiescence segment and P11 readout."""
    if n_quiet is None:
        n_quiet = 4 * tau_steps
    n_steps = n_drive + n_quiet

    S = cl.scatter_matrix(net.degree)
    packet = clv.launch_linear_packet(net, axis=axis)
    if direction_sign < 0:
        packet = packet.copy()
        packet[..., :] *= -1.0
    packet *= amp_frac
    V = packet.copy()
    apply_omega_freeze_ic(V, net, enabled=omega_freeze_ic)

    v10_state = V10RunState(chi_shock=chi_shock)
    v10_state.reset(net.n_nodes)
    mem = MemState()
    mem.reset(V)

    theta0 = clv.mean_polarization_angle(V)
    radii: list[float] = []
    e_loc_trace: list[float] = []
    a2_trace: list[float] = []
    theta_trace: list[float] = []
    last_diag: dict = {}

    for t in range(n_steps):
        in_quiescence = t >= n_drive
        if not in_quiescence:
            add_drive(V, packet, t, n_drive, amp=1.0)
        V, last_diag = vector_tlm_step_v11(
            net,
            V,
            S,
            v10_state,
            mem,
            op14=op14,
            op3=op3,
            snap=snap,
            memristive=memristive,
            tau_steps=tau_steps,
            in_quiescence=in_quiescence,
        )
        radii.append(energy_radius(net, V, axis=axis))
        e_loc_trace.append(clv.vector_energy(V))
        a2_trace.append(float(np.max((node_rms_amplitude(V) / V_SNAP_NATURAL) ** 2)))
        theta_trace.append(clv.mean_polarization_angle(V))

    r = np.array(radii)
    win = min(100, len(r))
    plateau_pct = float(abs(r[-1] - r[-win]) / (r[-win] + 1e-30) * 100.0) if win > 1 else 999.0
    p6_L = plateau_pct < 5.0

    w, _, _, _ = cl.net_ring_writhe(net)
    dtheta = float(theta_trace[-1] - theta0)
    theta_sign_ok = abs(dtheta) > 1e-8 and np.sign(dtheta) == np.sign(w * direction_sign)

    drive_off_idx = n_drive
    e_at_driveoff = e_loc_trace[drive_off_idx] if drive_off_idx < len(e_loc_trace) else 0.0
    e_end = e_loc_trace[-1] if e_loc_trace else 0.0
    e_peak_drive = max(e_loc_trace[: drive_off_idx + 1]) if e_loc_trace else 0.0
    e_ratio = e_end / (e_peak_drive + 1e-30)

    r_end = radii[-1]
    r_mid = radii[max(drive_off_idx, len(radii) - n_quiet - 1)]
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

    # P11 — quiescence window
    a2_drive = max(a2_trace[: drive_off_idx + 1]) if a2_trace else 0.0
    a2_quiet = max(a2_trace[drive_off_idx:]) if drive_off_idx < len(a2_trace) else 0.0
    theta_drive = abs(theta_trace[drive_off_idx] - theta0) if drive_off_idx < len(theta_trace) else 0.0
    theta_quiet = abs(theta_trace[-1] - theta_trace[drive_off_idx]) if drive_off_idx < len(theta_trace) else 0.0

    E_persist_ratio = e_end / (e_at_driveoff + 1e-30)
    A_persist_ratio = a2_quiet / (a2_drive + 1e-30)
    theta_persist = theta_quiet / (theta_drive + 1e-30)
    loop_proxy = mem.loop_proxy_accum

    p11 = _p11_pass(
        E_persist_ratio=E_persist_ratio,
        A_persist_ratio=A_persist_ratio,
        theta_persist=theta_persist,
        loop_proxy=loop_proxy,
        memristive_on=memristive,
    )

    return V11P6Result(
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
        snap_events=v10_state.snap_events,
        E_diss_snap=v10_state.E_diss_snap,
        omega_freeze_ic=omega_freeze_ic,
        snap_on=snap,
        memristive_on=memristive,
        tau_steps=tau_steps,
        n_quiet=n_quiet,
        E_persist_ratio=float(E_persist_ratio),
        A_persist_ratio=float(A_persist_ratio),
        theta_persist=float(theta_persist),
        loop_proxy=float(loop_proxy),
        p11_pass=p11,
    )


def run_p6_sweep_v11(
    net: cl.LatticeNet,
    label: str,
    *,
    amps: tuple[float, ...] = P6_AMP_SWEEP,
    chi_shock: float = 0.5,
    **kwargs,
) -> tuple[V11P6Result, list[V11P6Result]]:
    runs = [
        run_p6_cell_v11(net, label, amp_frac=a, chi_shock=chi_shock, **kwargs)
        for a in amps
    ]
    return _best_p6_sweep(runs), runs  # type: ignore[return-value]


def v11_gates(*, L: int = 10, smoke: bool = False, chi_shock: float = 0.5) -> dict:
    """Evaluate v11 P11 + inherited P6 battery."""
    L_p6 = 8 if smoke else max(L, 10)
    tau_steps = 10 if smoke else DEFAULT_TAU_STEPS
    n_quiet = 4 * tau_steps
    n_drive = 100 if smoke else 400
    amps: tuple[float, ...] = (0.5,) if smoke else P6_AMP_SWEEP

    out: dict = {
        "engine_class": "discrete srs TLM + memristive Op14 + snap + P11 quiescence",
        "smoke": smoke,
        "L_p6": L_p6,
        "chi_default": chi_shock,
        "A_yield_sq": A_YIELD_SQ,
        "tau_relax_s": TAU_RELAX_SI,
        "tau_steps": tau_steps,
        "n_quiet": n_quiet,
        "n_drive_default": n_drive,
        "P11_thresholds": {
            "E_persist_min": P11_E_PERSIST_MIN,
            "A_persist_min": P11_A_PERSIST_MIN,
            "theta_persist_min": P11_THETA_PERSIST_MIN,
        },
    }

    cells: list[V11P6Result] = []
    sweeps: dict[str, list[V11P6Result]] = {}
    for en, name in [("right", "srs-R"), ("left", "srs-L")]:
        for dsign, dlab in [(1.0, "+z"), (-1.0, "-z")]:
            n = cl.build_srs_net(L_p6, en)
            best, runs = run_p6_sweep_v11(
                n,
                f"{name}:{dlab}",
                amps=amps,
                n_drive=n_drive,
                n_quiet=n_quiet,
                tau_steps=tau_steps,
                direction_sign=dsign,
                chi_shock=chi_shock,
                omega_freeze_ic=True,
                snap=True,
                memristive=True,
            )
            cells.append(best)
            sweeps[best.label] = runs

    diamond_cells: list[V11P6Result] = []
    if not smoke:
        for dsign, dlab in [(1.0, "+z"), (-1.0, "-z")]:
            n = cl.build_diamond_net(L_p6)
            best, runs = run_p6_sweep_v11(
                n,
                f"diamond:{dlab}",
                amps=amps,
                n_drive=n_drive,
                n_quiet=n_quiet,
                tau_steps=tau_steps,
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
    out["P11_cells"] = {c.label: c.p11_pass for c in cells}
    out["P11_any_pass"] = any(c.p11_pass for c in cells)
    out["P11_metrics"] = {
        c.label: {
            "E_persist": c.E_persist_ratio,
            "A_persist": c.A_persist_ratio,
            "theta_persist": c.theta_persist,
            "loop_proxy": c.loop_proxy,
            "p11_pass": c.p11_pass,
        }
        for c in cells
    }

    ref_net = cl.build_srs_net(L_p6, "right")
    mem_off, _ = run_p6_sweep_v11(
        ref_net,
        "srs-R:+z memristive-OFF",
        amps=amps,
        n_drive=n_drive,
        n_quiet=n_quiet,
        tau_steps=tau_steps,
        chi_shock=chi_shock,
        memristive=False,
    )
    snap_off, _ = run_p6_sweep_v11(
        ref_net,
        "srs-R:+z snap-OFF",
        amps=amps,
        n_drive=n_drive,
        n_quiet=n_quiet,
        tau_steps=tau_steps,
        chi_shock=0.0,
        snap=False,
    )
    omega_free, _ = run_p6_sweep_v11(
        ref_net,
        "srs-R:+z Ω-free",
        amps=amps,
        n_drive=n_drive,
        n_quiet=n_quiet,
        tau_steps=tau_steps,
        chi_shock=chi_shock,
        omega_freeze_ic=False,
    )
    op3_off, _ = run_p6_sweep_v11(
        ref_net,
        "srs-R:+z op3-OFF",
        amps=amps,
        n_drive=n_drive,
        n_quiet=n_quiet,
        tau_steps=tau_steps,
        op3=False,
        chi_shock=chi_shock,
    )
    out["P11_memristive_ablation"] = mem_off
    out["P6_snap_ablation"] = snap_off
    out["P6_omega_free_ablation"] = omega_free
    out["P6_op3_ablation"] = op3_off

    # v10 replay (memristive OFF ≡ instantaneous Op14)
    v10_ref, _ = run_p6_sweep_v10(
        ref_net,
        "srs-R:+z v10-replay",
        amps=amps,
        n_steps=n_drive + n_quiet,
        n_drive=n_drive,
        chi_shock=chi_shock,
    )
    out["v10_replay"] = v10_ref
    out["v10_replay_bin_match"] = v10_ref.bin_label == mem_off.bin_label

    if not smoke:
        op14_off, _ = run_p6_sweep_v11(
            ref_net,
            "srs-R:+z op14-OFF",
            amps=amps,
            n_drive=n_drive,
            n_quiet=n_quiet,
            tau_steps=tau_steps,
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
            "memristive_off_e_retention": mem_off.e_loc_ratio_driveoff,
            "diamond_e_retention": diamond_ref.e_loc_ratio_driveoff if diamond_ref else None,
            "structure_driven_2x": matched,
            "diamond_theta_frac_of_srs": dia_theta / (srs_theta + 1e-30),
        }

        # D6 Compton ring-up sweep
        ring_runs: list[V11P6Result] = []
        for mult in (0.25, 0.5, 1.0, 2.0):
            nd = max(10, int(round(mult * tau_steps)))
            best, _ = run_p6_sweep_v11(
                ref_net,
                f"srs-R:+z n_drive={mult}×Nτ",
                amps=(0.5,),
                n_drive=nd,
                n_quiet=n_quiet,
                tau_steps=tau_steps,
                chi_shock=chi_shock,
            )
            ring_runs.append(best)
        out["D6_ringup_sweep"] = ring_runs
        out["D6_best_p11"] = max((r.p11_pass, r.E_persist_ratio, r.label) for r in ring_runs)

        chi_runs: list[V11P6Result] = []
        for chi in CHI_SWEEP:
            best, _ = run_p6_sweep_v11(
                ref_net,
                f"srs-R:+z χ={chi}",
                amps=(0.25,),
                n_drive=n_drive,
                n_quiet=n_quiet,
                tau_steps=tau_steps,
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

    # Verdict ladder (prereg §5)
    ref_cell = next((c for c in cells if c.label == "srs-R:+z"), None)
    p11_primary = ref_cell is not None and ref_cell.p11_pass and not mem_off.p11_pass
    structure_2x = out.get("P6_matched_baseline", {}).get("structure_driven_2x", False)
    if p11_primary and structure_2x:
        verdict = "LANDED"
    elif out["P11_any_pass"]:
        verdict = "PARTIAL"
    else:
        verdict = "LOOP GAP OPEN"
    out["verdict"] = verdict
    out["P11_primary_ablation_ok"] = p11_primary

    return out

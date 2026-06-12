"""
Genesis v17 — moving resonator stack: v16 (cavity + Compton + P11) + v14b comoving.

Stacks rank-1 container, rank-2 Compton ring-up, v14 transport rail, and rank-4
P11 quiescence on the same localized payload.

Pre-reg: extends v16 + v14b charters.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_vector as clv
from ave.core.chiral_lattice_v10 import V10RunState, apply_omega_freeze_ic
from ave.core.chiral_lattice_v11 import (
    DEFAULT_TAU_STEPS,
    P11_A_PERSIST_MIN,
    P11_E_PERSIST_MIN,
    P11_THETA_PERSIST_MIN,
    MemState,
)
from ave.core.chiral_lattice_v12 import (
    P12_MIN_GAIN_PER_100,
    P12_PEAK_RETENTION_MIN,
    P12_WIDTH_GROWTH_MAX,
    energy_centroid,
    energy_weighted_width,
    localized_plant_seed,
    peak_amplitude,
    translate_field_along_axis,
    transport_gain_threshold,
)
from ave.core.chiral_lattice_v13 import (
    Z_BULK_WALL,
    _p13_pass,
    compton_pocket_mask,
    energy_fraction_in_pocket,
    vector_tlm_step_v13,
)
from ave.core.chiral_lattice_v14 import _pbc_centroid_disp, peak_amplitude_in_pocket
from ave.core.chiral_lattice_v16 import COMPTON_DRIVE_MULTS, _p11_pass
from ave.core.chiral_lattice_vector_sat import V_SNAP_NATURAL, add_drive, node_rms_amplitude


@dataclass(frozen=True)
class V17P17Result:
    label: str
    n_drive_mult: float
    n_drive: int
    n_quiet: int
    comoving_on: bool
    v_boost: float
    bulk_wall_on: bool
    memristive_on: bool
    centroid_disp: float
    E_frac_interior: float
    width_ratio: float
    peak_retention: float
    peak_pocket_retention: float
    peak_metric: str
    p13_pass: bool
    E_persist_ratio: float
    A_persist_ratio: float
    theta_persist: float
    loop_proxy: float
    p11_pass: bool
    p12_pass: bool
    p17_pass: bool
    bin_label: str


def run_p17_moving_resonator_cell(
    net: cl.LatticeNet,
    label: str,
    *,
    n_drive_mult: float = 1.0,
    comoving: bool = True,
    v_boost: float = 1.0,
    bulk_wall: bool = True,
    memristive: bool = True,
    tau_steps: int = DEFAULT_TAU_STEPS,
    n_quiet_mult: float = 4.0,
    chi_shock: float = 0.5,
    amp: float = 0.5,
    axis: int = 2,
    use_23: bool = True,
    z_wall: float = Z_BULK_WALL,
    z_half_frac: float = 0.14,
    r_max_frac: float = 0.18,
) -> V17P17Result:
    """P17 — Compton ring-up in cavity + comoving hop + quiescence + P11."""
    pocket = compton_pocket_mask(
        net, axis=axis, z_half_frac=z_half_frac, r_max_frac=r_max_frac
    )
    S = cl.scatter_matrix(net.degree)
    packet = localized_plant_seed(net, amp=amp, use_23=use_23, axis=axis)
    V = packet.copy()
    apply_omega_freeze_ic(V, net, enabled=True)

    v10_state = V10RunState(chi_shock=chi_shock)
    v10_state.reset(net.n_nodes)
    mem = MemState()
    mem.reset(V)

    n_drive = max(10, int(round(n_drive_mult * tau_steps)))
    n_quiet = max(20, int(round(n_quiet_mult * tau_steps)))
    n_steps = n_drive + n_quiet
    k_boost = int(round(v_boost)) if comoving else 0

    z0 = energy_centroid(net, V, axis=axis)
    w0 = energy_weighted_width(net, V, axis=axis)
    p0 = peak_amplitude(V)
    p0_pocket = peak_amplitude_in_pocket(V, pocket) if bulk_wall else p0
    theta0 = clv.mean_polarization_angle(V)

    e_trace: list[float] = []
    a2_trace: list[float] = []
    theta_trace: list[float] = []
    pocket_peak_track: list[float] = []

    for t in range(n_steps):
        in_quiescence = t >= n_drive
        if not in_quiescence:
            add_drive(V, packet, t, n_drive, amp=1.0)
        V, _ = vector_tlm_step_v13(
            net,
            V,
            S,
            v10_state,
            mem,
            pocket_mask=pocket if bulk_wall else None,
            bulk_wall=bulk_wall,
            z_wall=z_wall,
            memristive=memristive,
            tau_steps=tau_steps,
            snap=True,
            in_quiescence=in_quiescence,
        )
        if comoving and k_boost > 0:
            V = translate_field_along_axis(
                net, V, delta=0.0, axis=axis, n_nodes_shift=k_boost
            )
        if bulk_wall:
            pocket_peak_track.append(peak_amplitude_in_pocket(V, pocket))
        e_trace.append(float(clv.vector_energy(V)))
        a2_trace.append(
            float(np.max((node_rms_amplitude(V) / V_SNAP_NATURAL) ** 2))
        )
        theta_trace.append(clv.mean_polarization_angle(V))

    z1 = energy_centroid(net, V, axis=axis)
    drive_off = n_drive
    e_at_driveoff = e_trace[drive_off] if drive_off < len(e_trace) else 0.0
    e_end = e_trace[-1] if e_trace else 0.0
    a2_drive = max(a2_trace[: drive_off + 1]) if a2_trace else 0.0
    a2_quiet = max(a2_trace[drive_off:]) if drive_off < len(a2_trace) else 0.0
    theta_drive = (
        abs(theta_trace[drive_off] - theta0) if drive_off < len(theta_trace) else 0.0
    )
    theta_quiet = (
        abs(theta_trace[-1] - theta_trace[drive_off])
        if drive_off < len(theta_trace)
        else 0.0
    )

    E_persist = e_end / (e_at_driveoff + 1e-30)
    A_persist = a2_quiet / (a2_drive + 1e-30)
    theta_persist = theta_quiet / (theta_drive + 1e-30)

    w1 = energy_weighted_width(net, V, axis=axis)
    p1 = peak_amplitude(V)
    p1_pocket = peak_amplitude_in_pocket(V, pocket) if bulk_wall else p1
    if comoving and bulk_wall and pocket_peak_track:
        p1_pocket = max(p1_pocket, max(pocket_peak_track))
    e_frac = energy_fraction_in_pocket(V, pocket) if bulk_wall else 1.0

    width_ratio = w1 / (w0 + 1e-30)
    peak_retention = p1 / (p0 + 1e-30)
    peak_pocket_retention = p1_pocket / (p0_pocket + 1e-30)
    peak_metric = "pocket" if comoving and bulk_wall else "global"
    peak_gate = peak_pocket_retention if peak_metric == "pocket" else peak_retention

    p13 = _p13_pass(
        E_frac_interior=e_frac,
        width_ratio=width_ratio,
        peak_retention=peak_gate,
        bulk_wall_on=bulk_wall,
    )
    p11 = _p11_pass(
        E_persist_ratio=E_persist,
        A_persist_ratio=A_persist,
        theta_persist=theta_persist,
    )

    if p11 and p13:
        bin_label = "REMANENCE-CANDIDATE"
    elif p13 and E_persist >= 0.5:
        bin_label = "CAVITY-SET"
    elif p13:
        bin_label = "CONFINED-NO-REMANENCE"
    else:
        bin_label = "DISPERSED"

    return V17P17Result(
        label=label,
        n_drive_mult=n_drive_mult,
        n_drive=n_drive,
        n_quiet=n_quiet,
        comoving_on=comoving,
        v_boost=v_boost,
        bulk_wall_on=bulk_wall,
        memristive_on=memristive,
        centroid_disp=_pbc_centroid_disp(net, z0, z1),
        E_frac_interior=float(e_frac),
        width_ratio=float(width_ratio),
        peak_retention=float(peak_retention),
        peak_pocket_retention=float(peak_pocket_retention),
        peak_metric=peak_metric,
        p13_pass=p13,
        E_persist_ratio=float(E_persist),
        A_persist_ratio=float(A_persist),
        theta_persist=float(theta_persist),
        loop_proxy=float(mem.loop_proxy_accum),
        p11_pass=p11,
        p12_pass=False,
        p17_pass=False,
        bin_label=bin_label,
    )


def _apply_p12_p17(
    cell: V17P17Result,
    *,
    transport_gain: float,
    gain_threshold: float,
) -> V17P17Result:
    peak_gate = (
        cell.peak_pocket_retention
        if cell.peak_metric == "pocket"
        else cell.peak_retention
    )
    p12 = (
        cell.comoving_on
        and cell.bulk_wall_on
        and transport_gain >= gain_threshold
        and cell.width_ratio <= P12_WIDTH_GROWTH_MAX
        and peak_gate >= P12_PEAK_RETENTION_MIN
    )
    p17 = cell.p11_pass and cell.p13_pass and p12
    return V17P17Result(
        label=cell.label,
        n_drive_mult=cell.n_drive_mult,
        n_drive=cell.n_drive,
        n_quiet=cell.n_quiet,
        comoving_on=cell.comoving_on,
        v_boost=cell.v_boost,
        bulk_wall_on=cell.bulk_wall_on,
        memristive_on=cell.memristive_on,
        centroid_disp=cell.centroid_disp,
        E_frac_interior=cell.E_frac_interior,
        width_ratio=cell.width_ratio,
        peak_retention=cell.peak_retention,
        peak_pocket_retention=cell.peak_pocket_retention,
        peak_metric=cell.peak_metric,
        p13_pass=cell.p13_pass,
        E_persist_ratio=cell.E_persist_ratio,
        A_persist_ratio=cell.A_persist_ratio,
        theta_persist=cell.theta_persist,
        loop_proxy=cell.loop_proxy,
        p11_pass=cell.p11_pass,
        p12_pass=p12,
        p17_pass=p17,
        bin_label=cell.bin_label,
    )


def v17_gates(*, L: int = 10, smoke: bool = False) -> dict:
    """P17 battery — moving resonator: Compton sweep + pinned/wall/mem ablations."""
    L_p17 = 8 if smoke else max(L, 10)
    tau_steps = 10 if smoke else DEFAULT_TAU_STEPS
    mults = (1.0,) if smoke else COMPTON_DRIVE_MULTS
    n_quiet_mult = 2.0 if smoke else 4.0

    net = cl.build_srs_net(L_p17, "right")
    n_steps_ref = max(10, int(round(1.0 * tau_steps))) + max(
        20, int(round(n_quiet_mult * tau_steps))
    )
    gain_thr = transport_gain_threshold(n_steps_ref, float(net.box))

    out: dict = {
        "engine_class": (
            "v17: v16 cavity+Compton+P11 + v14b comoving transport rail"
        ),
        "smoke": smoke,
        "L_p17": L_p17,
        "tau_steps": tau_steps,
        "compton_mults": mults,
        "P12_gain_threshold": gain_thr,
        "P11_thresholds": {
            "E_persist_min": P11_E_PERSIST_MIN,
            "A_persist_min": P11_A_PERSIST_MIN,
            "theta_persist_min": P11_THETA_PERSIST_MIN,
        },
        "P12_thresholds": {
            "width_max": P12_WIDTH_GROWTH_MAX,
            "peak_min": P12_PEAK_RETENTION_MIN,
            "min_gain_per_100": P12_MIN_GAIN_PER_100,
        },
    }

    common = dict(tau_steps=tau_steps, n_quiet_mult=n_quiet_mult)

    pinned = run_p17_moving_resonator_cell(
        net,
        "B pinned cavity",
        n_drive_mult=1.0,
        comoving=False,
        bulk_wall=True,
        **common,
    )

    ring_runs: list[V17P17Result] = []
    for mult in mults:
        raw = run_p17_moving_resonator_cell(
            net,
            f"A full stack {mult}×Nτ",
            n_drive_mult=mult,
            comoving=True,
            bulk_wall=True,
            **common,
        )
        gain = raw.centroid_disp - pinned.centroid_disp
        ring_runs.append(_apply_p12_p17(raw, transport_gain=gain, gain_threshold=gain_thr))

    full = ring_runs[0] if ring_runs else _apply_p12_p17(
        run_p17_moving_resonator_cell(
            net, "A full stack", comoving=True, bulk_wall=True, **common
        ),
        transport_gain=0.0,
        gain_threshold=gain_thr,
    )

    wall_off = run_p17_moving_resonator_cell(
        net,
        "wall-OFF",
        n_drive_mult=1.0,
        comoving=True,
        bulk_wall=False,
        **common,
    )
    mem_off = run_p17_moving_resonator_cell(
        net,
        "memristive-OFF",
        n_drive_mult=1.0,
        comoving=True,
        bulk_wall=True,
        memristive=False,
        **common,
    )
    transport_gain = full.centroid_disp - pinned.centroid_disp

    out["P17_ringup_sweep"] = ring_runs
    out["P17_full_stack"] = full
    out["P17_pinned_cavity"] = pinned
    out["P17_wall_ablation"] = wall_off
    out["P17_memristive_ablation"] = mem_off
    out["P17_transport_gain"] = float(transport_gain)
    out["P17_any_p11"] = any(r.p11_pass for r in ring_runs)
    out["P17_any_p17"] = any(r.p17_pass for r in ring_runs)
    out["P17_mem_ablation_ok"] = (
        full.p11_pass and not mem_off.p11_pass if full.p11_pass else False
    )

    best = max(
        ring_runs,
        key=lambda r: (r.p17_pass, r.p11_pass, r.E_persist_ratio, r.p13_pass),
    )
    out["P17_best"] = best

    if best.p17_pass and out["P17_mem_ablation_ok"]:
        verdict = "REMANENCE-LANDED"
    elif best.p11_pass and best.p13_pass:
        verdict = "PARTIAL-REMANENCE"
    elif best.p13_pass and transport_gain > 0.0:
        verdict = "MOVING-CAVITY-SET"
    elif best.p13_pass:
        verdict = "CAVITY-SET-ONLY"
    else:
        verdict = "LOOP-GAP-OPEN"

    out["verdict"] = verdict
    return out

"""
Genesis v14 — cavity + comoving transport stack (v13 bulk-wall + v12 Galilean hop).

Pre-reg: research/2026-06-12_genesis-v14-cavity-transport_prereg_DRAFT.md
"""

from __future__ import annotations

from dataclasses import dataclass, replace

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_vector as clv
from ave.core.chiral_lattice_v10 import V10RunState, apply_omega_freeze_ic
from ave.core.chiral_lattice_v11 import DEFAULT_TAU_STEPS, MemState, run_p6_cell_v11
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
    EXTERIOR_LEAK,
    Z_BULK_WALL,
    _p13_pass,
    compton_pocket_mask,
    energy_fraction_in_pocket,
    vector_tlm_step_v13,
)

OP3_ONLY_LEAK = 1.0


@dataclass
class V14Trajectory:
    """Time-series + spatial snapshots for figure drivers."""

    label: str
    bulk_wall_on: bool
    comoving_on: bool
    axis: int
    n_steps: int
    record_every: int
    steps: np.ndarray
    centroid: np.ndarray
    width: np.ndarray
    E_frac: np.ndarray
    peak_global: np.ndarray
    peak_pocket: np.ndarray
    total_energy: np.ndarray
    z_centers: np.ndarray
    z_profiles: np.ndarray  # (n_records, n_bins)
    pocket_z0: float
    pocket_z_half: float
    snapshot_steps: np.ndarray
    snapshot_node_energy: np.ndarray  # (n_snapshots, n_nodes)
    net_pos: np.ndarray
    pocket_mask: np.ndarray


def node_energy(V: np.ndarray) -> np.ndarray:
    return np.sum(V * V, axis=(1, 2))


def peak_amplitude_in_pocket(
    V: np.ndarray,
    pocket_mask: np.ndarray,
    *,
    v_snap: float = 1.0,
) -> float:
    from ave.core.chiral_lattice_vector_sat import V_SNAP_NATURAL, node_rms_amplitude

    a = node_rms_amplitude(V) / v_snap
    if not np.any(pocket_mask):
        return 0.0
    return float(np.max(a[pocket_mask]))


def energy_profile_along_axis(
    net: cl.LatticeNet,
    V: np.ndarray,
    *,
    axis: int = 2,
    n_bins: int = 48,
) -> tuple[np.ndarray, np.ndarray]:
    """Binned energy density profile along axis."""
    e = node_energy(V)
    z = net.pos[:, axis]
    edges = np.linspace(float(z.min()), float(z.max()), n_bins + 1)
    centers = 0.5 * (edges[:-1] + edges[1:])
    hist = np.zeros(n_bins)
    for i in range(n_bins):
        mask = (z >= edges[i]) & (z < edges[i + 1])
        if i == n_bins - 1:
            mask = (z >= edges[i]) & (z <= edges[i + 1])
        hist[i] = float(e[mask].sum())
    return centers, hist


def run_p14_trajectory(
    net: cl.LatticeNet,
    label: str,
    *,
    bulk_wall: bool = True,
    comoving: bool = True,
    v_boost: float = 1.0,
    n_steps: int = 220,
    record_every: int = 5,
    snapshot_fracs: tuple[float, ...] = (0.0, 0.25, 0.5, 0.75, 1.0),
    memristive: bool = True,
    tau_steps: int = DEFAULT_TAU_STEPS,
    chi_shock: float = 0.5,
    amp: float = 0.5,
    axis: int = 2,
    use_23: bool = True,
    z_wall: float = Z_BULK_WALL,
    exterior_leak: float = EXTERIOR_LEAK,
    z_half_frac: float = 0.14,
    r_max_frac: float = 0.18,
    n_profile_bins: int = 48,
) -> V14Trajectory:
    """Record scalar metrics and spatial snapshots for visualization."""
    pocket = compton_pocket_mask(
        net, axis=axis, z_half_frac=z_half_frac, r_max_frac=r_max_frac
    )
    z_med = float(np.median(net.pos[pocket, axis]))
    pocket_z_half = z_half_frac * float(net.box)

    S = cl.scatter_matrix(net.degree)
    V = localized_plant_seed(net, amp=amp, use_23=use_23, axis=axis)
    apply_omega_freeze_ic(V, net, enabled=True)

    v10_state = V10RunState(chi_shock=chi_shock)
    v10_state.reset(net.n_nodes)
    mem = MemState()
    mem.reset(V)

    k_boost = int(round(v_boost)) if comoving else 0
    snap_targets = {int(round(f * n_steps)) for f in snapshot_fracs}
    snap_targets.add(0)
    snap_targets.add(n_steps)

    steps_list: list[int] = []
    centroid_list: list[float] = []
    width_list: list[float] = []
    efrac_list: list[float] = []
    peak_g_list: list[float] = []
    peak_p_list: list[float] = []
    energy_list: list[float] = []
    profiles: list[np.ndarray] = []
    z_centers_ref: np.ndarray | None = None

    snap_steps: list[int] = []
    snap_energy: list[np.ndarray] = []

    def _record(step: int, field: np.ndarray) -> None:
        nonlocal z_centers_ref
        steps_list.append(step)
        centroid_list.append(energy_centroid(net, field, axis=axis))
        width_list.append(energy_weighted_width(net, field, axis=axis))
        if bulk_wall:
            efrac_list.append(energy_fraction_in_pocket(field, pocket))
            peak_p_list.append(
                peak_amplitude_in_pocket(field, pocket)
            )
        else:
            efrac_list.append(0.0)
            peak_p_list.append(0.0)
        peak_g_list.append(peak_amplitude(field))
        energy_list.append(float(clv.vector_energy(field)))
        zc, prof = energy_profile_along_axis(
            net, field, axis=axis, n_bins=n_profile_bins
        )
        if z_centers_ref is None:
            z_centers_ref = zc
        profiles.append(prof)
        if step in snap_targets:
            snap_steps.append(step)
            snap_energy.append(node_energy(field))

    _record(0, V)

    for step in range(1, n_steps + 1):
        V, _ = vector_tlm_step_v13(
            net,
            V,
            S,
            v10_state,
            mem,
            pocket_mask=pocket,
            bulk_wall=bulk_wall,
            z_wall=z_wall,
            exterior_leak=exterior_leak if bulk_wall else 1.0,
            memristive=memristive,
            tau_steps=tau_steps,
            snap=True,
        )
        if comoving and k_boost > 0:
            V = translate_field_along_axis(
                net, V, delta=0.0, axis=axis, n_nodes_shift=k_boost
            )
        if step % record_every == 0 or step == n_steps:
            _record(step, V)

    assert z_centers_ref is not None
    return V14Trajectory(
        label=label,
        bulk_wall_on=bulk_wall,
        comoving_on=comoving,
        axis=axis,
        n_steps=n_steps,
        record_every=record_every,
        steps=np.array(steps_list, dtype=int),
        centroid=np.array(centroid_list),
        width=np.array(width_list),
        E_frac=np.array(efrac_list),
        peak_global=np.array(peak_g_list),
        peak_pocket=np.array(peak_p_list),
        total_energy=np.array(energy_list),
        z_centers=z_centers_ref,
        z_profiles=np.stack(profiles, axis=0),
        pocket_z0=z_med,
        pocket_z_half=pocket_z_half,
        snapshot_steps=np.array(snap_steps, dtype=int),
        snapshot_node_energy=np.stack(snap_energy, axis=0),
        net_pos=net.pos.copy(),
        pocket_mask=pocket.copy(),
    )


@dataclass(frozen=True)
class V14StackResult:
    label: str
    bulk_wall_on: bool
    comoving_on: bool
    v_boost: float
    n_steps: int
    centroid_disp: float
    E_frac_interior: float
    width_ratio: float
    peak_retention: float
    peak_pocket_retention: float
    peak_metric: str
    total_energy_ratio: float
    p13_pass: bool
    p12_pass: bool = False
    p14_pass: bool = False
    exterior_leak: float = EXTERIOR_LEAK
    memristive_on: bool = True
    use_23: bool = True


def _pbc_centroid_disp(
    net: cl.LatticeNet,
    z0: float,
    z1: float,
) -> float:
    box = float(net.box)
    raw = z1 - z0
    if raw > 0.5 * box:
        raw -= box
    elif raw < -0.5 * box:
        raw += box
    return abs(raw)


def _p12_pass(
    *,
    transport_gain: float,
    width_ratio: float,
    peak_retention: float,
    gain_threshold: float,
    comoving_on: bool,
    bulk_wall_on: bool,
) -> bool:
    if not comoving_on or not bulk_wall_on:
        return False
    return (
        transport_gain >= gain_threshold
        and width_ratio <= P12_WIDTH_GROWTH_MAX
        and peak_retention >= P12_PEAK_RETENTION_MIN
    )


def run_p14_stack_cell(
    net: cl.LatticeNet,
    label: str,
    *,
    bulk_wall: bool = True,
    comoving: bool = True,
    v_boost: float = 1.0,
    n_steps: int = 220,
    memristive: bool = True,
    tau_steps: int = DEFAULT_TAU_STEPS,
    chi_shock: float = 0.5,
    amp: float = 0.5,
    axis: int = 2,
    use_23: bool = True,
    z_wall: float = Z_BULK_WALL,
    exterior_leak: float = EXTERIOR_LEAK,
    z_half_frac: float = 0.14,
    r_max_frac: float = 0.18,
) -> V14StackResult:
    """P14 cell — v13 bulk-wall step + optional v12 comoving hop."""
    pocket = compton_pocket_mask(
        net, axis=axis, z_half_frac=z_half_frac, r_max_frac=r_max_frac
    )
    S = cl.scatter_matrix(net.degree)
    V = localized_plant_seed(net, amp=amp, use_23=use_23, axis=axis)
    apply_omega_freeze_ic(V, net, enabled=True)

    v10_state = V10RunState(chi_shock=chi_shock)
    v10_state.reset(net.n_nodes)
    mem = MemState()
    mem.reset(V)

    z0 = energy_centroid(net, V, axis=axis)
    w0 = energy_weighted_width(net, V, axis=axis)
    p0 = peak_amplitude(V)
    p0_pocket = peak_amplitude_in_pocket(V, pocket) if bulk_wall else p0
    e0 = float(clv.vector_energy(V))

    k_boost = int(round(v_boost)) if comoving else 0
    pocket_peak_track: list[float] = []

    for _ in range(n_steps):
        V, _ = vector_tlm_step_v13(
            net,
            V,
            S,
            v10_state,
            mem,
            pocket_mask=pocket,
            bulk_wall=bulk_wall,
            z_wall=z_wall,
            exterior_leak=exterior_leak if bulk_wall else 1.0,
            memristive=memristive,
            tau_steps=tau_steps,
            snap=True,
        )
        if comoving and k_boost > 0:
            V = translate_field_along_axis(
                net, V, delta=0.0, axis=axis, n_nodes_shift=k_boost
            )
        if bulk_wall:
            pocket_peak_track.append(peak_amplitude_in_pocket(V, pocket))

    z1 = energy_centroid(net, V, axis=axis)
    w1 = energy_weighted_width(net, V, axis=axis)
    p1 = peak_amplitude(V)
    p1_pocket = peak_amplitude_in_pocket(V, pocket) if bulk_wall else p1
    if comoving and bulk_wall and pocket_peak_track:
        p1_pocket = max(p1_pocket, max(pocket_peak_track))
    e1 = float(clv.vector_energy(V))
    e_frac = energy_fraction_in_pocket(V, pocket) if bulk_wall else 0.0

    width_ratio = w1 / (w0 + 1e-30)
    peak_retention = p1 / (p0 + 1e-30)
    peak_pocket_retention = p1_pocket / (p0_pocket + 1e-30)
    peak_metric = "pocket" if comoving and bulk_wall else "global"
    peak_gate = peak_pocket_retention if peak_metric == "pocket" else peak_retention

    return V14StackResult(
        label=label,
        bulk_wall_on=bulk_wall,
        comoving_on=comoving,
        v_boost=v_boost,
        n_steps=n_steps,
        centroid_disp=_pbc_centroid_disp(net, z0, z1),
        E_frac_interior=float(e_frac),
        width_ratio=float(width_ratio),
        peak_retention=float(peak_retention),
        peak_pocket_retention=float(peak_pocket_retention),
        peak_metric=peak_metric,
        total_energy_ratio=float(e1 / (e0 + 1e-30)),
        p13_pass=_p13_pass(
            E_frac_interior=e_frac,
            width_ratio=width_ratio,
            peak_retention=peak_gate,
            bulk_wall_on=bulk_wall,
        ),
        exterior_leak=exterior_leak if bulk_wall else 1.0,
        memristive_on=memristive,
        use_23=use_23,
    )


def _apply_p12_p14(
    cell: V14StackResult,
    *,
    transport_gain: float,
    gain_threshold: float,
) -> V14StackResult:
    peak_gate = (
        cell.peak_pocket_retention
        if cell.peak_metric == "pocket"
        else cell.peak_retention
    )
    p12 = _p12_pass(
        transport_gain=transport_gain,
        width_ratio=cell.width_ratio,
        peak_retention=peak_gate,
        gain_threshold=gain_threshold,
        comoving_on=cell.comoving_on,
        bulk_wall_on=cell.bulk_wall_on,
    )
    p14 = cell.p13_pass and p12
    return replace(cell, p12_pass=p12, p14_pass=p14)


def v14_gates(*, L: int = 10, smoke: bool = False) -> dict:
    """P14 dual-gate battery: P13 confinement + P12 transport in cavity."""
    L_p14 = 8 if smoke else max(L, 10)
    n_steps = 60 if smoke else 220
    tau_steps = 10 if smoke else DEFAULT_TAU_STEPS
    v_boost = 1.0

    out: dict = {
        "engine_class": "discrete srs TLM + v13 bulk-wall + v12 comoving hop",
        "smoke": smoke,
        "L_p14": L_p14,
        "n_steps": n_steps,
        "v_boost": v_boost,
        "P12_gain_threshold_ref": P12_MIN_GAIN_PER_100,
        "P13_thresholds": {
            "E_frac_interior_min": 0.55,
            "width_growth_max": 2.0,
            "peak_retention_min": 0.40,
            "peak_metric_comoving": "pocket",
        },
    }

    net = cl.build_srs_net(L_p14, "right")
    gain_thr = transport_gain_threshold(n_steps, float(net.box))

    full = run_p14_stack_cell(
        net,
        "A full stack wall+comoving",
        bulk_wall=True,
        comoving=True,
        v_boost=v_boost,
        n_steps=n_steps,
        tau_steps=tau_steps,
    )
    pinned = run_p14_stack_cell(
        net,
        "B pinned cavity",
        bulk_wall=True,
        comoving=False,
        n_steps=n_steps,
        tau_steps=tau_steps,
    )
    open_comoving = run_p14_stack_cell(
        net,
        "C open transport",
        bulk_wall=False,
        comoving=True,
        v_boost=v_boost,
        n_steps=n_steps,
        tau_steps=tau_steps,
    )
    open_pinned = run_p14_stack_cell(
        net,
        "D open pinned",
        bulk_wall=False,
        comoving=False,
        n_steps=n_steps,
        tau_steps=tau_steps,
    )
    op3_only = run_p14_stack_cell(
        net,
        "E Op3-only wall+comoving",
        bulk_wall=True,
        comoving=True,
        v_boost=v_boost,
        n_steps=n_steps,
        exterior_leak=OP3_ONLY_LEAK,
        tau_steps=tau_steps,
    )
    linear = run_p14_stack_cell(
        net,
        "F linear+cavity+comoving",
        bulk_wall=True,
        comoving=True,
        v_boost=v_boost,
        n_steps=n_steps,
        use_23=False,
        amp=0.25,
        chi_shock=0.0,
        memristive=False,
        tau_steps=tau_steps,
    )

    transport_gain = full.centroid_disp - pinned.centroid_disp
    open_gain = open_comoving.centroid_disp - open_pinned.centroid_disp
    linear_gain = linear.centroid_disp - pinned.centroid_disp
    op3_gain = op3_only.centroid_disp - pinned.centroid_disp

    full = _apply_p12_p14(full, transport_gain=transport_gain, gain_threshold=gain_thr)
    op3_only = _apply_p12_p14(op3_only, transport_gain=op3_gain, gain_threshold=gain_thr)
    linear = _apply_p12_p14(linear, transport_gain=linear_gain, gain_threshold=gain_thr)

    out["P14_full_stack"] = full
    out["P14_pinned_cavity"] = pinned
    out["P14_open_comoving"] = open_comoving
    out["P14_open_pinned"] = open_pinned
    out["P14_op3_only_wall"] = op3_only
    out["P14_linear_control"] = linear
    out["P14_transport_gain"] = float(transport_gain)
    out["P14_gain_threshold"] = float(gain_thr)
    out["P14_open_transport_gain"] = float(open_gain)
    out["P14_op3_transport_gain"] = float(op3_gain)
    out["P14_any_pass"] = full.p14_pass
    out["P13_on_comoving"] = full.p13_pass
    out["P12_on_comoving"] = full.p12_pass

    if smoke:
        boost_sweep: dict[str, float] = {}
        for vb in (0.5, 1.0, 2.0):
            c = run_p14_stack_cell(
                net,
                f"boost-sweep v={vb}",
                bulk_wall=True,
                comoving=True,
                v_boost=vb,
                n_steps=n_steps,
                tau_steps=tau_steps,
            )
            boost_sweep[str(vb)] = c.centroid_disp - pinned.centroid_disp
        out["P14_boost_sweep_gain"] = boost_sweep

    v11_reg = run_p6_cell_v11(
        net,
        "srs-R:+z v11 regression",
        n_drive=80 if smoke else 400,
        n_quiet=40 if smoke else 200,
        tau_steps=tau_steps,
    )
    out["v11_regression"] = v11_reg

    if full.p14_pass:
        verdict = "TRANSPORT-IN-CAVITY-LANDED"
    elif full.p13_pass and transport_gain > 0.0:
        verdict = "PARTIAL"
    elif not full.p13_pass and full.comoving_on:
        verdict = "CAVITY-BREAK"
    else:
        verdict = "ENGINE-GAP"

    out["verdict"] = verdict
    return out


def v14b_gates(*, L: int = 10, smoke: bool = False) -> dict:
    """v14b — same battery as v14 with pocket-frame peak on comoving arms."""
    out = v14_gates(L=L, smoke=smoke)
    out["engine_class"] = (
        "v14b: discrete srs + bulk-wall + comoving; pocket-frame peak gate"
    )
    full = out["P14_full_stack"]
    out["P14b_peak_global"] = full.peak_retention
    out["P14b_peak_pocket"] = full.peak_pocket_retention
    out["P14b_peak_metric"] = full.peak_metric

    if full.p14_pass:
        out["verdict"] = "TRANSPORT-IN-CAVITY-LANDED"
    elif full.p13_pass and out["P14_transport_gain"] > 0.0:
        out["verdict"] = "PARTIAL"
    elif not full.p13_pass and full.comoving_on:
        out["verdict"] = "CAVITY-BREAK"
    else:
        out["verdict"] = "ENGINE-GAP"
    return out

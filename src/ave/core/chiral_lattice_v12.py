"""
Genesis v12 — boost-covariant transport on discrete srs (semi-Lagrangian advection).

Pre-reg: research/2026-06-12_genesis-v12-boost-transport_prereg_DRAFT.md
Platform: v11 memristive kernel + comoving Galilean field transport per scatter step.
"""

from __future__ import annotations

from dataclasses import dataclass, replace

import numpy as np
from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_vector as clv
from ave.core.chiral_lattice_v11 import (
    DEFAULT_TAU_STEPS,
    MemState,
    run_p6_cell_v11,
    vector_tlm_step_v11,
)
from ave.core.chiral_lattice_v10 import V10RunState, apply_omega_freeze_ic
from ave.core.chiral_lattice_vector_sat import V_SNAP_NATURAL, plant_23_ansatz

# P12 gates (moving_defect_transport_gate.py floors, discrete analogue).
P12_WIDTH_GROWTH_MAX = 2.0
P12_PEAK_RETENTION_MIN = 0.50
# Minimum comoving−pinned centroid gain (fraction of box per 100 steps).
P12_MIN_GAIN_PER_100 = 0.08


def energy_centroid(
    net: cl.LatticeNet,
    V: np.ndarray,
    *,
    axis: int = 2,
) -> float:
    """Energy-weighted centroid along axis."""
    e = np.sum(V * V, axis=(1, 2))
    total = float(e.sum())
    if total < 1e-30:
        return float("nan")
    coord = net.pos[:, axis]
    return float(np.average(coord, weights=e))


def energy_weighted_width(
    net: cl.LatticeNet,
    V: np.ndarray,
    *,
    axis: int = 2,
) -> float:
    """RMS width along axis (energy-weighted)."""
    e = np.sum(V * V, axis=(1, 2))
    total = float(e.sum())
    if total < 1e-30:
        return float("inf")
    z = net.pos[:, axis]
    z0 = float(np.average(z, weights=e))
    return float(np.sqrt(np.average((z - z0) ** 2, weights=e)))


def peak_amplitude(V: np.ndarray, *, v_snap: float = V_SNAP_NATURAL) -> float:
    a = np.sqrt(np.mean(V * V, axis=(1, 2))) / v_snap
    return float(np.max(a))


def translate_field_along_axis(
    net: cl.LatticeNet,
    V: np.ndarray,
    *,
    delta: float,
    axis: int = 2,
    n_nodes_shift: int | None = None,
) -> np.ndarray:
    """Galilean transport: roll node fields along sorted axis order (PBC).

    Integer node shift per scatter step (discrete ℓ_node hop). `delta` is
    converted to a node count when `n_nodes_shift` is None via median spacing.
    """
    if n_nodes_shift is None:
        order = np.argsort(net.pos[:, axis])
        z_sorted = net.pos[order, axis]
        dz = np.diff(np.sort(z_sorted))
        dz_med = float(np.median(dz[dz > 1e-9])) if np.any(dz > 1e-9) else 1.0
        n_nodes_shift = int(round(delta / max(dz_med, 1e-9)))
    k = int(n_nodes_shift)
    if k == 0:
        return V
    order = np.argsort(net.pos[:, axis])
    V_sorted = V[order]
    V_shifted = np.roll(V_sorted, k, axis=0)
    V_out = np.zeros_like(V)
    V_out[order] = V_shifted
    return V_out


def localized_plant_seed(
    net: cl.LatticeNet,
    *,
    amp: float = 0.5,
    width_frac: float = 0.10,
    use_23: bool = True,
    axis: int = 2,
) -> np.ndarray:
    """Localized saturation seed for transport tests."""
    if use_23:
        V = plant_23_ansatz(net, axis=axis, width_frac=width_frac) * amp
    else:
        V = clv.launch_linear_packet(net, axis=axis) * amp
        z = net.pos[:, axis]
        z0 = float(np.median(z[net.interior_mask]))
        sigma = max(width_frac * net.box, 1e-6)
        env = np.exp(-0.5 * ((z - z0) / sigma) ** 2)
        V *= env[:, None, None]
    return V


@dataclass(frozen=True)
class V12P12Result:
    label: str
    v_boost: float  # nodes per scatter step (integer)
    comoving_on: bool
    n_steps: int
    centroid_disp: float
    width_ratio: float
    peak_retention: float
    total_energy_ratio: float
    p12_pass: bool
    memristive_on: bool = True


def _median_axis_spacing(net: cl.LatticeNet, axis: int = 2) -> float:
    order = np.argsort(net.pos[:, axis])
    z = net.pos[order, axis]
    dz = np.diff(z)
    return float(np.median(dz[dz > 1e-9])) if np.any(dz > 1e-9) else 1.0


def transport_gain_threshold(n_steps: int, box: float) -> float:
    return P12_MIN_GAIN_PER_100 * (n_steps / 100.0) * box


def _p12_pass(
    *,
    transport_gain: float,
    width_ratio: float,
    peak_retention: float,
    gain_threshold: float,
    comoving_on: bool,
) -> bool:
    if not comoving_on:
        return False
    return (
        transport_gain >= gain_threshold
        and width_ratio <= P12_WIDTH_GROWTH_MAX
        and peak_retention >= P12_PEAK_RETENTION_MIN
    )


def run_p12_transport_cell(
    net: cl.LatticeNet,
    label: str,
    *,
    v_boost: float = 1.0,
    n_steps: int = 200,
    comoving: bool = True,
    memristive: bool = True,
    tau_steps: int = DEFAULT_TAU_STEPS,
    chi_shock: float = 0.5,
    amp: float = 0.5,
    axis: int = 2,
    use_23: bool = True,
) -> V12P12Result:
    """P12 — comoving transport of localized defect on v11 kernel."""
    S = cl.scatter_matrix(net.degree)
    V = localized_plant_seed(net, amp=amp, use_23=use_23, axis=axis)
    apply_omega_freeze_ic(V, net, enabled=True)

    v10_state = V10RunState(chi_shock=chi_shock)
    v10_state.reset(net.n_nodes)
    mem = MemState()
    mem.reset(V)

    e0 = float(clv.vector_energy(V))
    z0 = energy_centroid(net, V, axis=axis)
    w0 = energy_weighted_width(net, V, axis=axis)
    p0 = peak_amplitude(V)

    for _ in range(n_steps):
        V, _ = vector_tlm_step_v11(
            net,
            V,
            S,
            v10_state,
            mem,
            memristive=memristive,
            tau_steps=tau_steps,
            snap=True,
        )
        if comoving and v_boost > 0.0:
            V = translate_field_along_axis(
                net, V, delta=0.0, axis=axis, n_nodes_shift=int(round(v_boost))
            )

    z1 = energy_centroid(net, V, axis=axis)
    w1 = energy_weighted_width(net, V, axis=axis)
    p1 = peak_amplitude(V)
    e1 = float(clv.vector_energy(V))

    # PBC-aware displacement along axis.
    box = float(net.box)
    raw_disp = z1 - z0
    if raw_disp > 0.5 * box:
        raw_disp -= box
    elif raw_disp < -0.5 * box:
        raw_disp += box
    centroid_disp = abs(raw_disp)

    width_ratio = w1 / (w0 + 1e-30)
    peak_retention = p1 / (p0 + 1e-30)
    energy_ratio = e1 / (e0 + 1e-30)

    return V12P12Result(
        label=label,
        v_boost=v_boost,
        comoving_on=comoving,
        n_steps=n_steps,
        centroid_disp=float(centroid_disp),
        width_ratio=float(width_ratio),
        peak_retention=float(peak_retention),
        total_energy_ratio=float(energy_ratio),
        p12_pass=False,  # set in v12_gates via transport_gain vs pinned
        memristive_on=memristive,
    )


def v12_gates(*, L: int = 10, smoke: bool = False) -> dict:
    """P12 transport battery + v11 regression cell."""
    L_p12 = 8 if smoke else max(L, 10)
    n_steps = 80 if smoke else 250
    v_boost = 1.0
    tau_steps = 10 if smoke else DEFAULT_TAU_STEPS

    out: dict = {
        "engine_class": "discrete srs TLM + v11 memristive + comoving Galilean transport",
        "smoke": smoke,
        "L_p12": L_p12,
        "v_boost": v_boost,
        "n_steps": n_steps,
        "P12_thresholds": {
            "width_growth_max": P12_WIDTH_GROWTH_MAX,
            "peak_retention_min": P12_PEAK_RETENTION_MIN,
            "min_gain_per_100_steps_frac_box": P12_MIN_GAIN_PER_100,
        },
    }

    net = cl.build_srs_net(L_p12, "right")

    comoving = run_p12_transport_cell(
        net,
        "srs-R:+z comoving",
        v_boost=v_boost,
        n_steps=n_steps,
        comoving=True,
        tau_steps=tau_steps,
    )
    pinned = run_p12_transport_cell(
        net,
        "srs-R:+z comoving-OFF",
        v_boost=v_boost,
        n_steps=n_steps,
        comoving=False,
        tau_steps=tau_steps,
    )
    linear_ctrl = run_p12_transport_cell(
        net,
        "srs-R:+z linear+comoving",
        v_boost=v_boost,
        n_steps=n_steps,
        comoving=True,
        use_23=False,
        amp=0.25,
        chi_shock=0.0,
        memristive=False,
        tau_steps=tau_steps,
    )
    linear_pinned = run_p12_transport_cell(
        net,
        "srs-R:+z linear pinned",
        v_boost=v_boost,
        n_steps=n_steps,
        comoving=False,
        use_23=False,
        amp=0.25,
        chi_shock=0.0,
        memristive=False,
        tau_steps=tau_steps,
    )
    mem_off = run_p12_transport_cell(
        net,
        "srs-R:+z comoving mem-OFF",
        v_boost=v_boost,
        n_steps=n_steps,
        comoving=True,
        memristive=False,
        tau_steps=tau_steps,
    )

    gain_thr = transport_gain_threshold(n_steps, float(net.box))
    plant_gain = comoving.centroid_disp - pinned.centroid_disp
    linear_gain = linear_ctrl.centroid_disp - linear_pinned.centroid_disp

    comoving = replace(
        comoving,
        p12_pass=_p12_pass(
            transport_gain=plant_gain,
            width_ratio=comoving.width_ratio,
            peak_retention=comoving.peak_retention,
            gain_threshold=gain_thr,
            comoving_on=True,
        ),
    )

    out["P12_comoving"] = comoving
    out["P12_pinned_ablation"] = pinned
    out["P12_linear_control"] = linear_ctrl
    out["P12_linear_pinned"] = linear_pinned
    out["P12_memristive_ablation"] = mem_off
    out["P12_transport_gain"] = plant_gain
    out["P12_gain_threshold"] = gain_thr
    out["P12_any_pass"] = comoving.p12_pass
    out["P12_ablation_fails"] = plant_gain > 0.0 and pinned.centroid_disp < comoving.centroid_disp

    # C4 apparatus: comoving must beat pinned on linear packet.
    out["P12_linear_advances"] = linear_gain > 0.0 and linear_ctrl.centroid_disp >= linear_pinned.centroid_disp
    out["dz_med"] = _median_axis_spacing(net, axis=2)

    # v11 regression (single cell, shortened).
    n_quiet = 4 * tau_steps
    n_drive = min(100, n_steps) if smoke else 200
    v11_ref = run_p6_cell_v11(
        net,
        "srs-R:+z v11-regression",
        amp_frac=0.5,
        n_drive=n_drive,
        n_quiet=n_quiet,
        tau_steps=tau_steps,
        memristive=True,
    )
    out["v11_regression"] = v11_ref

    if comoving.p12_pass and out["P12_ablation_fails"] and out["P12_linear_advances"]:
        verdict = "TRANSPORT-LANDED"
    elif comoving.centroid_disp > pinned.centroid_disp:
        verdict = "PARTIAL"
    else:
        verdict = "ENGINE-GAP"
    out["verdict"] = verdict

    return out

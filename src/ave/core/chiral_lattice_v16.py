"""
Genesis v16 — cavity + Compton ring-up + P11 remanence stack.

Closes LOOP GAP ranks 2 (Compton-resonant drive) and 4 (P11 quiescence probe)
inside v13 bulk-wall container (rank 1 already LANDED).

Pre-reg: extends genesis-v11-loop-closure + genesis-v13-eigen-cavity charters.
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
    energy_weighted_width,
    localized_plant_seed,
    peak_amplitude,
)
from ave.core.chiral_lattice_v13 import (
    Z_BULK_WALL,
    _p13_pass,
    compton_pocket_mask,
    energy_fraction_in_pocket,
    vector_tlm_step_v13,
)
from ave.core.chiral_lattice_vector_sat import V_SNAP_NATURAL, add_drive, node_rms_amplitude

# Compton ring-up multiples of N_τ (v11 D6 sweep analogue).
COMPTON_DRIVE_MULTS = (0.5, 1.0, 2.0, 4.0)


@dataclass(frozen=True)
class V16P16Result:
    label: str
    n_drive_mult: float
    n_drive: int
    n_quiet: int
    bulk_wall_on: bool
    memristive_on: bool
    E_frac_interior: float
    width_ratio: float
    peak_retention: float
    p13_pass: bool
    E_persist_ratio: float
    A_persist_ratio: float
    theta_persist: float
    loop_proxy: float
    p11_pass: bool
    bin_label: str


def _p11_pass(
    *,
    E_persist_ratio: float,
    A_persist_ratio: float,
    theta_persist: float,
) -> bool:
    return (
        E_persist_ratio >= P11_E_PERSIST_MIN
        and A_persist_ratio >= P11_A_PERSIST_MIN
        and theta_persist >= P11_THETA_PERSIST_MIN
    )


def run_p16_cavity_ringup_cell(
    net: cl.LatticeNet,
    label: str,
    *,
    n_drive_mult: float = 1.0,
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
) -> V16P16Result:
    """P16 — plant_23 Compton ring-up in cavity + extended quiescence + P11."""
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

    w0 = energy_weighted_width(net, V, axis=axis)
    p0 = peak_amplitude(V)
    theta0 = clv.mean_polarization_angle(V)

    e_trace: list[float] = []
    a2_trace: list[float] = []
    theta_trace: list[float] = []

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
        e_trace.append(float(clv.vector_energy(V)))
        a2_trace.append(
            float(np.max((node_rms_amplitude(V) / V_SNAP_NATURAL) ** 2))
        )
        theta_trace.append(clv.mean_polarization_angle(V))

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
    e_frac = energy_fraction_in_pocket(V, pocket) if bulk_wall else 1.0
    width_ratio = w1 / (w0 + 1e-30)
    peak_retention = p1 / (p0 + 1e-30)
    p13 = _p13_pass(
        E_frac_interior=e_frac,
        width_ratio=width_ratio,
        peak_retention=peak_retention,
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

    return V16P16Result(
        label=label,
        n_drive_mult=n_drive_mult,
        n_drive=n_drive,
        n_quiet=n_quiet,
        bulk_wall_on=bulk_wall,
        memristive_on=memristive,
        E_frac_interior=float(e_frac),
        width_ratio=float(width_ratio),
        peak_retention=float(peak_retention),
        p13_pass=p13,
        E_persist_ratio=float(E_persist),
        A_persist_ratio=float(A_persist),
        theta_persist=float(theta_persist),
        loop_proxy=float(mem.loop_proxy_accum),
        p11_pass=p11,
        bin_label=bin_label,
    )


def v16_gates(*, L: int = 10, smoke: bool = False) -> dict:
    """P16 battery — Compton ring-up sweep in cavity + ablations."""
    L_p16 = 8 if smoke else max(L, 10)
    tau_steps = 10 if smoke else DEFAULT_TAU_STEPS
    mults = (1.0,) if smoke else COMPTON_DRIVE_MULTS

    net = cl.build_srs_net(L_p16, "right")
    out: dict = {
        "engine_class": "v16: v13 cavity + Compton ring-up + P11 quiescence",
        "smoke": smoke,
        "L_p16": L_p16,
        "tau_steps": tau_steps,
        "compton_mults": mults,
        "P11_thresholds": {
            "E_persist_min": P11_E_PERSIST_MIN,
            "A_persist_min": P11_A_PERSIST_MIN,
            "theta_persist_min": P11_THETA_PERSIST_MIN,
        },
    }

    ring_runs: list[V16P16Result] = []
    for mult in mults:
        ring_runs.append(
            run_p16_cavity_ringup_cell(
                net,
                f"ringup {mult}×Nτ",
                n_drive_mult=mult,
                bulk_wall=True,
                memristive=True,
                tau_steps=tau_steps,
            )
        )
    out["P16_ringup_sweep"] = ring_runs

    wall_off = run_p16_cavity_ringup_cell(
        net,
        "wall-OFF ablation",
        n_drive_mult=1.0,
        bulk_wall=False,
        tau_steps=tau_steps,
    )
    mem_off = run_p16_cavity_ringup_cell(
        net,
        "memristive-OFF ablation",
        n_drive_mult=1.0,
        bulk_wall=True,
        memristive=False,
        tau_steps=tau_steps,
    )
    out["P16_wall_ablation"] = wall_off
    out["P16_memristive_ablation"] = mem_off

    best = max(ring_runs, key=lambda r: (r.p11_pass, r.E_persist_ratio, r.p13_pass))
    out["P16_best"] = best
    out["P16_any_p11"] = any(r.p11_pass for r in ring_runs)
    out["P16_mem_ablation_ok"] = best.p11_pass and not mem_off.p11_pass

    if best.p11_pass and best.p13_pass and out["P16_mem_ablation_ok"]:
        verdict = "REMANENCE-LANDED"
    elif best.p11_pass:
        verdict = "PARTIAL"
    elif best.p13_pass and best.E_persist_ratio >= 0.5:
        verdict = "CAVITY-SET-ONLY"
    else:
        verdict = "LOOP-GAP-OPEN"

    out["verdict"] = verdict
    return out

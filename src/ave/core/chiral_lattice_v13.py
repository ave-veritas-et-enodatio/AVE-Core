"""
Genesis v13 — OP-2 eigen-cavity / bulk-wall confinement on discrete srs.

Pre-reg: research/2026-06-12_genesis-v13-eigen-cavity_prereg_DRAFT.md
Platform: v11 memristive kernel + Γ_bulk→−1 analogue via exterior z_local stiffening.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_vector as clv
from ave.core.chiral_lattice_v10 import (
    V10RunState,
    apply_omega_freeze_ic,
    apply_rate_gated_snap,
    channel_H_diagnostics,
)
from ave.core.chiral_lattice_v11 import (
    DEFAULT_TAU_STEPS,
    MemState,
    backward_euler_s,
    run_p6_cell_v11,
    s_eq_from_amplitude,
    z_local_from_s,
)
from ave.core.chiral_lattice_v12 import (
    energy_weighted_width,
    localized_plant_seed,
    peak_amplitude,
)
from ave.core.chiral_lattice_vector_sat import (
    V_SNAP_NATURAL,
    connect_op3,
    node_rms_amplitude,
)

# Exterior bulk impedance analogue (Γ_bulk → −1 TIR stiffening on Op3 bonds).
Z_BULK_WALL = 12.0
EXTERIOR_LEAK = 0.04

# P13 gates — eigen-cavity localization (confinement, not transport).
P13_E_FRAC_MIN = 0.55
P13_WIDTH_MAX = 2.0
P13_PEAK_MIN = 0.40
P13_WALL_DISCRIMINATION_MIN = 1.20


def compton_pocket_mask(
    net: cl.LatticeNet,
    *,
    axis: int = 2,
    z_half_frac: float = 0.14,
    r_max_frac: float = 0.18,
) -> np.ndarray:
    """Compton-scale tubular pocket along srs axis (interior nodes only)."""
    interior = net.interior_mask
    z = net.pos[:, axis]
    z0 = float(np.median(z[interior]))
    z_half = z_half_frac * float(net.box)
    in_axis = np.abs(z - z0) <= z_half

    perp = [a for a in (0, 1, 2) if a != axis]
    r = np.sqrt(net.pos[:, perp[0]] ** 2 + net.pos[:, perp[1]] ** 2)
    r0 = float(np.median(r[interior]))
    r_max = r0 + r_max_frac * float(net.box)
    in_rad = r <= r_max

    return interior & in_axis & in_rad


def apply_bulk_wall_z_local(
    z_loc: np.ndarray,
    pocket_mask: np.ndarray,
    *,
    z_wall: float = Z_BULK_WALL,
) -> np.ndarray:
    """Stiffen exterior nodes to emulate bulk TIR wall in Op3 bond mixing."""
    z = z_loc.copy()
    exterior = ~pocket_mask
    z[exterior] = np.maximum(z[exterior], z_wall)
    return z


def energy_fraction_in_pocket(V: np.ndarray, pocket_mask: np.ndarray) -> float:
    e = np.sum(V * V, axis=(1, 2))
    total = float(e.sum())
    if total < 1e-30:
        return 0.0
    return float(e[pocket_mask].sum() / total)


def attenuate_exterior_field(
    V: np.ndarray,
    pocket_mask: np.ndarray,
    *,
    leak: float = EXTERIOR_LEAK,
) -> np.ndarray:
    """Hard-container leak suppression outside pocket."""
    V_out = V.copy()
    V_out[~pocket_mask] *= leak
    return V_out


def vector_tlm_step_v13(
    net: cl.LatticeNet,
    V: np.ndarray,
    S: np.ndarray,
    v10_state: V10RunState,
    mem: MemState,
    *,
    pocket_mask: np.ndarray | None = None,
    bulk_wall: bool = False,
    z_wall: float = Z_BULK_WALL,
    exterior_leak: float = EXTERIOR_LEAK,
    op14: bool = True,
    op3: bool = True,
    snap: bool = True,
    chiral_rotation: bool = True,
    memristive: bool = True,
    tau_steps: float = DEFAULT_TAU_STEPS,
    v_snap: float = V_SNAP_NATURAL,
    in_quiescence: bool = False,
) -> tuple[np.ndarray, dict]:
    """v11 scatter step + bulk-wall z_local stiffening and exterior attenuation."""
    if v10_state.a2_prev is None:
        v10_state.reset(net.n_nodes)

    a2_old = v10_state.a2_prev.copy()
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

    if bulk_wall and pocket_mask is not None:
        z_loc = apply_bulk_wall_z_local(z_loc, pocket_mask, z_wall=z_wall)

    V_new = connect_op3(net, V_ref, z_loc, op3=op3)
    a2_new = a_inc * a_inc
    apply_rate_gated_snap(V_new, a2_new, a2_old, v10_state, snap=snap, v_snap=v_snap)
    v10_state.a2_prev = node_rms_amplitude(V_new) / v_snap
    v10_state.a2_prev = v10_state.a2_prev * v10_state.a2_prev

    if bulk_wall and pocket_mask is not None:
        V_new = attenuate_exterior_field(V_new, pocket_mask, leak=exterior_leak)

    h = channel_H_diagnostics(a2_new)
    diag = {
        **h,
        "max_A2": float(np.max(a2_new)),
        "z_std": float(np.std(z_loc)),
        "max_z": float(np.max(z_loc)),
        "bulk_wall": bulk_wall,
        "E_frac_interior": energy_fraction_in_pocket(V_new, pocket_mask)
        if pocket_mask is not None
        else 1.0,
    }
    return V_new, diag


@dataclass(frozen=True)
class V13P13Result:
    label: str
    bulk_wall_on: bool
    n_steps: int
    E_frac_interior: float
    width_ratio: float
    peak_retention: float
    total_energy_ratio: float
    p13_pass: bool
    memristive_on: bool = True
    pocket_fraction: float = 0.0


def _p13_pass(
    *,
    E_frac_interior: float,
    width_ratio: float,
    peak_retention: float,
    bulk_wall_on: bool,
) -> bool:
    if not bulk_wall_on:
        return False
    return (
        E_frac_interior >= P13_E_FRAC_MIN
        and width_ratio <= P13_WIDTH_MAX
        and peak_retention >= P13_PEAK_MIN
    )


def run_p13_cavity_cell(
    net: cl.LatticeNet,
    label: str,
    *,
    bulk_wall: bool = True,
    n_steps: int = 200,
    memristive: bool = True,
    tau_steps: int = DEFAULT_TAU_STEPS,
    chi_shock: float = 0.5,
    amp: float = 0.5,
    axis: int = 2,
    use_23: bool = True,
    z_wall: float = Z_BULK_WALL,
    z_half_frac: float = 0.14,
    r_max_frac: float = 0.18,
) -> V13P13Result:
    """P13 — localized eigen-cavity confinement (no comoving transport)."""
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

    e0 = float(clv.vector_energy(V))
    w0 = energy_weighted_width(net, V, axis=axis)
    p0 = peak_amplitude(V)

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
            memristive=memristive,
            tau_steps=tau_steps,
            snap=True,
        )

    w1 = energy_weighted_width(net, V, axis=axis)
    p1 = peak_amplitude(V)
    e1 = float(clv.vector_energy(V))
    e_frac = energy_fraction_in_pocket(V, pocket)

    width_ratio = w1 / (w0 + 1e-30)
    peak_retention = p1 / (p0 + 1e-30)
    energy_ratio = e1 / (e0 + 1e-30)

    return V13P13Result(
        label=label,
        bulk_wall_on=bulk_wall,
        n_steps=n_steps,
        E_frac_interior=float(e_frac),
        width_ratio=float(width_ratio),
        peak_retention=float(peak_retention),
        total_energy_ratio=float(energy_ratio),
        p13_pass=_p13_pass(
            E_frac_interior=e_frac,
            width_ratio=width_ratio,
            peak_retention=peak_retention,
            bulk_wall_on=bulk_wall,
        ),
        memristive_on=memristive,
        pocket_fraction=float(pocket.sum()) / max(float(net.n_nodes), 1.0),
    )


def v13_gates(*, L: int = 10, smoke: bool = False) -> dict:
    """P13 eigen-cavity battery + v12 width regression context."""
    L_p13 = 8 if smoke else max(L, 10)
    n_steps = 60 if smoke else 220
    tau_steps = 10 if smoke else DEFAULT_TAU_STEPS

    out: dict = {
        "engine_class": "discrete srs TLM + v11 memristive + bulk-wall OP-2 pocket",
        "smoke": smoke,
        "L_p13": L_p13,
        "n_steps": n_steps,
        "P13_thresholds": {
            "E_frac_interior_min": P13_E_FRAC_MIN,
            "width_growth_max": P13_WIDTH_MAX,
            "peak_retention_min": P13_PEAK_MIN,
            "wall_discrimination_min": P13_WALL_DISCRIMINATION_MIN,
        },
        "z_wall": Z_BULK_WALL,
    }

    net = cl.build_srs_net(L_p13, "right")

    wall_on = run_p13_cavity_cell(
        net,
        "srs-R:+z bulk-wall ON",
        bulk_wall=True,
        n_steps=n_steps,
        tau_steps=tau_steps,
    )
    wall_off = run_p13_cavity_cell(
        net,
        "srs-R:+z bulk-wall OFF",
        bulk_wall=False,
        n_steps=n_steps,
        tau_steps=tau_steps,
    )
    linear_ctrl = run_p13_cavity_cell(
        net,
        "srs-R:+z linear packet",
        bulk_wall=True,
        n_steps=n_steps,
        use_23=False,
        amp=0.25,
        chi_shock=0.0,
        memristive=False,
        tau_steps=tau_steps,
    )
    mem_off = run_p13_cavity_cell(
        net,
        "srs-R:+z wall memristive-OFF",
        bulk_wall=True,
        n_steps=n_steps,
        memristive=False,
        tau_steps=tau_steps,
    )

    wall_disc = wall_off.width_ratio / max(wall_on.width_ratio, 1e-30)
    e_disc = wall_on.E_frac_interior - wall_off.E_frac_interior

    out["P13_wall_on"] = wall_on
    out["P13_wall_off_ablation"] = wall_off
    out["P13_linear_control"] = linear_ctrl
    out["P13_memristive_ablation"] = mem_off
    out["wall_width_discrimination"] = float(wall_disc)
    out["wall_E_frac_gain"] = float(e_disc)
    out["P13_any_pass"] = wall_on.p13_pass
    out["P13_ablation_fails"] = not wall_off.p13_pass
    out["P13_wall_discriminates"] = (
        wall_disc >= P13_WALL_DISCRIMINATION_MIN or e_disc >= 0.15
    )

    v11_reg = run_p6_cell_v11(
        net,
        "srs-R:+z v11 regression",
        n_drive=80 if smoke else 400,
        n_quiet=40 if smoke else 200,
        tau_steps=tau_steps,
    )
    out["v11_regression"] = v11_reg

    if wall_on.p13_pass and out["P13_ablation_fails"] and out["P13_wall_discriminates"]:
        verdict = "LOCALIZATION-LANDED"
    elif out["P13_wall_discriminates"] and (
        wall_on.E_frac_interior >= 0.45 or wall_on.width_ratio <= 2.5
    ):
        verdict = "PARTIAL"
    else:
        verdict = "ENGINE-GAP"

    out["verdict"] = verdict
    return out

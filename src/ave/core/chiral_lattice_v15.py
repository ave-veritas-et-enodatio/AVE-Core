"""
Genesis v15 — nucleation from latent heat (Lane A) on discrete srs.

Pre-reg: research/2026-06-12_genesis-v15-nucleation-from-latent_prereg_DRAFT.md
Provenance: genesis_lane_a_provenance.py + research/2026-06-12_genesis-parameter-provenance-audit.md
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np

from ave.core import chiral_lattice as cl
from ave.core import chiral_lattice_vector as clv
from ave.core.chiral_lattice_v10 import A_YIELD_SQ, V10RunState, apply_omega_freeze_ic
from ave.core.chiral_lattice_v11 import DEFAULT_TAU_STEPS, MemState
from ave.core.chiral_lattice_v12 import (
    energy_centroid,
    energy_weighted_width,
    localized_plant_seed,
    peak_amplitude,
)
from ave.core.chiral_lattice_v14 import (
    energy_profile_along_axis,
    node_energy,
)
from ave.core.chiral_lattice_v13 import (
    Z_BULK_WALL,
    compton_pocket_mask,
    energy_fraction_in_pocket,
    vector_tlm_step_v13,
)
from ave.core.chiral_lattice_vector_sat import V_SNAP_NATURAL, node_rms_amplitude
from ave.core.constants import ALPHA
from ave.core.genesis_lane_a_provenance import (
    P15_E_FRAC_MIN,
    P15_WIDTH_MAX,
    LaneAProvenance,
    a2_vsnap_to_r_yield,
    build_lane_a_provenance,
    field_energy_native,
    provenance_dict,
    seed_amp_vsnap,
)

SeedMode = Literal["none", "pair", "single", "photon"]


def node_a2(V: np.ndarray, *, v_snap: float = V_SNAP_NATURAL) -> np.ndarray:
    a = node_rms_amplitude(V) / v_snap
    return a * a


def latent_heat_inject_energy(
    V: np.ndarray,
    pocket_mask: np.ndarray,
    *,
    delta_e_native: float,
) -> None:
    """Add ΔE_native (m_e c² units) to masked field; engine stores V in V_SNAP units."""
    if delta_e_native <= 0.0 or not np.any(pocket_mask):
        return
    e_eng = float(np.sum(V[pocket_mask] * V[pocket_mask]))
    e_nat = e_eng / ALPHA
    if e_nat < 1e-30:
        n_active = int(np.sum(np.any(V[pocket_mask] != 0, axis=(1, 2))))
        if n_active == 0:
            return
        d_amp = float(
            np.sqrt(delta_e_native * ALPHA / max(n_active * V.shape[1], 1))
        )
        V[pocket_mask] += d_amp
        return
    boost = float(np.sqrt((e_nat + delta_e_native) / e_nat))
    V[pocket_mask] *= boost


def _interior_node_indices(net: cl.LatticeNet) -> np.ndarray:
    return np.flatnonzero(net.interior_mask)


def seed_saturated_node_pair(
    net: cl.LatticeNet,
    *,
    pocket_mask: np.ndarray,
    amp: float,
    axis: int = 2,
) -> tuple[np.ndarray, np.ndarray]:
    """Minimal node-pair bias — NOT plant_23 / NOT propagating packet."""
    V = np.zeros((net.n_nodes, net.degree, 2))
    interior = _interior_node_indices(net)
    in_pocket = interior[pocket_mask[interior]]
    if in_pocket.size < 2:
        in_pocket = interior
    z = net.pos[in_pocket, axis]
    order = np.argsort(z)
    nodes = in_pocket[order]
    i0 = nodes[len(nodes) // 2]
    z_i0 = net.pos[i0, axis]
    d = np.abs(net.pos[nodes, axis] - z_i0)
    d[d < 1e-12] = np.inf
    i1 = nodes[int(np.argmin(d))]
    pair = np.array([i0, i1], dtype=int)
    pair_mask = np.zeros(net.n_nodes, dtype=bool)
    pair_mask[pair] = True

    for u in pair:
        V[u, 0, 0] = amp
        V[u, 0, 1] = 0.5 * amp
    return V, pair_mask


def seed_single_node(
    net: cl.LatticeNet,
    *,
    pocket_mask: np.ndarray,
    amp: float,
    axis: int = 2,
) -> np.ndarray:
    V = np.zeros((net.n_nodes, net.degree, 2))
    interior = _interior_node_indices(net)
    in_pocket = interior[pocket_mask[interior]]
    if in_pocket.size < 1:
        in_pocket = interior
    z = net.pos[in_pocket, 2 if axis == 2 else axis]
    u = in_pocket[int(np.argsort(z)[len(in_pocket) // 2])]
    V[u, 0, 0] = amp
    return V


def _initial_field(
    net: cl.LatticeNet,
    *,
    seed_mode: SeedMode,
    pocket_mask: np.ndarray,
    seed_amp: float,
    axis: int = 2,
) -> tuple[np.ndarray, np.ndarray]:
    pair_mask = np.zeros(net.n_nodes, dtype=bool)
    if seed_mode == "none":
        return np.zeros((net.n_nodes, net.degree, 2)), pair_mask
    if seed_mode == "photon":
        return localized_plant_seed(net, amp=0.5, use_23=True, axis=axis), pair_mask
    if seed_mode == "pair":
        return seed_saturated_node_pair(
            net, pocket_mask=pocket_mask, amp=seed_amp, axis=axis
        )
    V = seed_single_node(net, pocket_mask=pocket_mask, amp=seed_amp, axis=axis)
    pair_mask[np.argmax(np.sum(V * V, axis=(1, 2)))] = True
    return V, pair_mask


@dataclass(frozen=True)
class V15P15Result:
    label: str
    latent_on: bool
    seed_mode: str
    bulk_wall_on: bool
    n_steps: int
    A2_seed_peak: float
    r_yield_seed_peak: float
    A2_pair_peak: float
    E_frac_interior: float
    width_ratio: float
    peak_retention: float
    total_energy_ratio: float
    p15n_pass: bool


def _p15n_pass(
    *,
    A2_seed_peak: float,
    E_frac_interior: float,
    width_ratio: float,
    latent_on: bool,
    seed_mode: str,
    a2_threshold: float,
) -> bool:
    if seed_mode == "photon" or not latent_on:
        return False
    return (
        A2_seed_peak >= a2_threshold
        and E_frac_interior >= P15_E_FRAC_MIN
        and width_ratio <= P15_WIDTH_MAX
    )


def run_p15_nucleation_cell(
    net: cl.LatticeNet,
    label: str,
    prov: LaneAProvenance,
    *,
    latent_on: bool = True,
    seed_mode: SeedMode = "pair",
    bulk_wall: bool = True,
    axis: int = 2,
    z_wall: float = Z_BULK_WALL,
    z_half_frac: float = 0.14,
    r_max_frac: float = 0.18,
    memristive: bool = True,
    tau_steps: int = DEFAULT_TAU_STEPS,
    latent_dissipation_ablation: bool = False,
) -> V15P15Result:
    """P15 — Lane A nucleation IC; all rates from prov (no free q_latent).

    When ``latent_dissipation_ablation`` is True, during the latent window only:
    χ-shock=0, snap=OFF, memristive=OFF (derived switches — not tuning knobs).
    """
    pocket = compton_pocket_mask(
        net, axis=axis, z_half_frac=z_half_frac, r_max_frac=r_max_frac
    )
    S = cl.scatter_matrix(net.degree)

    V, pair_mask = _initial_field(
        net,
        seed_mode=seed_mode,
        pocket_mask=pocket,
        seed_amp=seed_amp_vsnap(),
        axis=axis,
    )
    apply_omega_freeze_ic(V, net, enabled=True)

    v10_state = V10RunState(chi_shock=prov.timing.chi_shock)
    v10_state.reset(net.n_nodes)
    mem = MemState()
    mem.reset(V)

    n_steps = prov.timing.n_steps_total
    n_latent = prov.timing.n_latent_steps
    delta_e_step = prov.local.delta_e_native_per_step_pair

    e0 = float(clv.vector_energy(V))
    w0 = energy_weighted_width(net, V, axis=axis)
    p0 = peak_amplitude(V)
    a2_pair_track: list[float] = []

    chi_base = prov.timing.chi_shock
    for step in range(n_steps):
        in_latent = latent_on and step < n_latent
        if in_latent:
            inject_mask = pair_mask if np.any(pair_mask) else pocket
            latent_heat_inject_energy(V, inject_mask, delta_e_native=delta_e_step)
        if latent_dissipation_ablation and in_latent:
            v10_state.chi_shock = 0.0
            step_snap = False
            step_mem = False
        else:
            v10_state.chi_shock = chi_base
            step_snap = True
            step_mem = memristive
        V, _ = vector_tlm_step_v13(
            net,
            V,
            S,
            v10_state,
            mem,
            pocket_mask=pocket if bulk_wall else None,
            bulk_wall=bulk_wall,
            z_wall=z_wall,
            memristive=step_mem,
            tau_steps=tau_steps,
            snap=step_snap,
        )
        a2 = node_a2(V)
        if np.any(pair_mask):
            a2_pair_track.append(float(np.max(a2[pair_mask])))
        elif seed_mode == "photon":
            a2_pair_track.append(float(np.max(a2[pocket])))

    w1 = energy_weighted_width(net, V, axis=axis)
    p1 = peak_amplitude(V)
    e_frac = energy_fraction_in_pocket(V, pocket) if bulk_wall else 1.0

    a2_final = node_a2(V)
    if np.any(pair_mask):
        a2_pair_peak = float(np.max(a2_final[pair_mask]))
    else:
        a2_pair_peak = (
            float(np.max(a2_final[pocket])) if np.any(pocket) else 0.0
        )
    a2_seed_peak = float(max(a2_pair_track) if a2_pair_track else a2_pair_peak)
    r_yield_peak = a2_vsnap_to_r_yield(a2_seed_peak)

    width_ratio = w1 / (w0 + 1e-30)
    peak_retention = p1 / (p0 + 1e-30)

    return V15P15Result(
        label=label,
        latent_on=latent_on,
        seed_mode=seed_mode,
        bulk_wall_on=bulk_wall,
        n_steps=n_steps,
        A2_seed_peak=a2_seed_peak,
        r_yield_seed_peak=float(r_yield_peak),
        A2_pair_peak=a2_pair_peak,
        E_frac_interior=float(e_frac),
        width_ratio=float(width_ratio),
        peak_retention=float(peak_retention),
        total_energy_ratio=float(clv.vector_energy(V)) / (e0 + 1e-30),
        p15n_pass=_p15n_pass(
            A2_seed_peak=a2_seed_peak,
            E_frac_interior=e_frac,
            width_ratio=width_ratio,
            latent_on=latent_on,
            seed_mode=seed_mode,
            a2_threshold=prov.local.a2_vsnap_threshold,
        ),
    )


def v15_gates(*, L: int = 10, smoke: bool = False) -> dict:
    """P15 ablation battery A–E; parameters from build_lane_a_provenance."""
    L_p15 = 8 if smoke else max(L, 10)
    tau_steps = 10 if smoke else DEFAULT_TAU_STEPS

    net = cl.build_srs_net(L_p15, "right")
    pocket = compton_pocket_mask(net)
    prov = build_lane_a_provenance(net, pocket, smoke=smoke)

    out: dict = {
        "engine_class": "discrete srs TLM + v13 pocket + derived latent budget (Lane A)",
        "smoke": smoke,
        "L_p15": L_p15,
        "provenance": provenance_dict(prov),
        "P15_thresholds": {
            "A2_vsnap_min": prov.local.a2_vsnap_threshold,
            "r_yield_min": prov.local.r_yield_threshold,
            "E_frac_min": P15_E_FRAC_MIN,
            "width_max": P15_WIDTH_MAX,
        },
    }

    common = dict(prov=prov, tau_steps=tau_steps)

    cell_a = run_p15_nucleation_cell(
        net, "A cosmic IC", latent_on=True, seed_mode="pair", bulk_wall=True, **common
    )
    cell_b = run_p15_nucleation_cell(
        net, "B heal", latent_on=False, seed_mode="none", bulk_wall=False, **common
    )
    cell_c = run_p15_nucleation_cell(
        net, "C photon compare", latent_on=False, seed_mode="photon", bulk_wall=True, **common
    )
    cell_d = run_p15_nucleation_cell(
        net, "D latent no wall", latent_on=True, seed_mode="pair", bulk_wall=False, **common
    )
    cell_e = run_p15_nucleation_cell(
        net, "E single-node", latent_on=True, seed_mode="single", bulk_wall=True, **common
    )

    out["P15_A_cosmic"] = cell_a
    out["P15_B_heal"] = cell_b
    out["P15_C_photon"] = cell_c
    out["P15_D_no_wall"] = cell_d
    out["P15_E_single"] = cell_e

    heal_ok = (
        cell_b.A2_seed_peak < 0.1 * A_YIELD_SQ
        and cell_b.total_energy_ratio < 1.01
    )
    photon_ablation = not cell_c.p15n_pass
    wall_disc = cell_a.E_frac_interior - cell_d.E_frac_interior

    out["P15_H_heal_pass"] = heal_ok
    out["P15_photon_ablation"] = photon_ablation
    out["wall_E_frac_gain"] = float(wall_disc)

    if cell_a.p15n_pass and heal_ok and photon_ablation:
        verdict = "NUCLEATION-LANDED"
    elif (
        cell_a.r_yield_seed_peak >= 0.5 * prov.local.r_yield_threshold
        and cell_a.E_frac_interior >= 0.40
    ):
        verdict = "PARTIAL"
    elif heal_ok and not cell_a.p15n_pass:
        verdict = "HEAL-CONFIRMED"
    else:
        verdict = "ENGINE-GAP"

    out["verdict"] = verdict
    return out


@dataclass(frozen=True)
class V15Trajectory:
    """Time-series + spatial snapshots for Lane A figure drivers."""

    label: str
    latent_on: bool
    seed_mode: str
    bulk_wall_on: bool
    latent_dissipation_ablation: bool
    axis: int
    n_steps: int
    n_latent_steps: int
    record_every: int
    r_yield_threshold: float
    r_yield_knee: float
    steps: np.ndarray
    r_yield_pair: np.ndarray
    A2_pair: np.ndarray
    centroid: np.ndarray
    width: np.ndarray
    E_frac: np.ndarray
    total_energy_native: np.ndarray
    z_centers: np.ndarray
    z_profiles: np.ndarray
    pocket_z0: float
    pocket_z_half: float
    snapshot_steps: np.ndarray
    snapshot_node_energy: np.ndarray
    net_pos: np.ndarray
    pocket_mask: np.ndarray
    pair_mask: np.ndarray
    pair_node_indices: np.ndarray


def run_p15_trajectory(
    net: cl.LatticeNet,
    label: str,
    prov: LaneAProvenance,
    *,
    latent_on: bool = True,
    seed_mode: SeedMode = "pair",
    bulk_wall: bool = True,
    latent_dissipation_ablation: bool = False,
    record_every: int = 5,
    snapshot_fracs: tuple[float, ...] = (0.0, 0.2, 0.4, 0.6, 0.8, 1.0),
    axis: int = 2,
    z_wall: float = Z_BULK_WALL,
    z_half_frac: float = 0.14,
    r_max_frac: float = 0.18,
    memristive: bool = True,
    tau_steps: int = DEFAULT_TAU_STEPS,
    n_profile_bins: int = 48,
) -> V15Trajectory:
    """Record scalar metrics and spatial snapshots for v15 visualization."""
    pocket = compton_pocket_mask(
        net, axis=axis, z_half_frac=z_half_frac, r_max_frac=r_max_frac
    )
    z_med = float(np.median(net.pos[pocket, axis]))
    pocket_z_half = z_half_frac * float(net.box)

    S = cl.scatter_matrix(net.degree)
    V, pair_mask = _initial_field(
        net,
        seed_mode=seed_mode,
        pocket_mask=pocket,
        seed_amp=seed_amp_vsnap(),
        axis=axis,
    )
    pair_nodes = np.flatnonzero(pair_mask)
    apply_omega_freeze_ic(V, net, enabled=True)

    v10_state = V10RunState(chi_shock=prov.timing.chi_shock)
    v10_state.reset(net.n_nodes)
    mem = MemState()
    mem.reset(V)

    n_steps = prov.timing.n_steps_total
    n_latent = prov.timing.n_latent_steps
    delta_e_step = prov.local.delta_e_native_per_step_pair
    chi_base = prov.timing.chi_shock

    snap_targets = {int(round(f * n_steps)) for f in snapshot_fracs}
    snap_targets.update({0, n_steps})

    steps_list: list[int] = []
    r_yield_list: list[float] = []
    a2_list: list[float] = []
    centroid_list: list[float] = []
    width_list: list[float] = []
    efrac_list: list[float] = []
    energy_list: list[float] = []
    profiles: list[np.ndarray] = []
    z_centers_ref: np.ndarray | None = None
    snap_steps: list[int] = []
    snap_energy: list[np.ndarray] = []

    def _pair_r_yield(field: np.ndarray) -> float:
        a2 = node_a2(field)
        if np.any(pair_mask):
            return float(a2_vsnap_to_r_yield(float(np.max(a2[pair_mask]))))
        if seed_mode == "photon" and np.any(pocket):
            return float(a2_vsnap_to_r_yield(float(np.max(a2[pocket]))))
        return 0.0

    def _pair_a2(field: np.ndarray) -> float:
        a2 = node_a2(field)
        if np.any(pair_mask):
            return float(np.max(a2[pair_mask]))
        if seed_mode == "photon" and np.any(pocket):
            return float(np.max(a2[pocket]))
        return 0.0

    def _record(step: int, field: np.ndarray) -> None:
        nonlocal z_centers_ref
        steps_list.append(step)
        r_yield_list.append(_pair_r_yield(field))
        a2_list.append(_pair_a2(field))
        centroid_list.append(energy_centroid(net, field, axis=axis))
        width_list.append(energy_weighted_width(net, field, axis=axis))
        if bulk_wall:
            efrac_list.append(energy_fraction_in_pocket(field, pocket))
        else:
            efrac_list.append(0.0)
        energy_list.append(field_energy_native(field))
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
        in_latent = latent_on and step < n_latent
        if in_latent:
            inject_mask = pair_mask if np.any(pair_mask) else pocket
            latent_heat_inject_energy(V, inject_mask, delta_e_native=delta_e_step)
        if latent_dissipation_ablation and in_latent:
            v10_state.chi_shock = 0.0
            step_snap = False
            step_mem = False
        else:
            v10_state.chi_shock = chi_base
            step_snap = True
            step_mem = memristive
        V, _ = vector_tlm_step_v13(
            net,
            V,
            S,
            v10_state,
            mem,
            pocket_mask=pocket if bulk_wall else None,
            bulk_wall=bulk_wall,
            z_wall=z_wall,
            memristive=step_mem,
            tau_steps=tau_steps,
            snap=step_snap,
        )
        if step % record_every == 0 or step == n_steps:
            _record(step, V)

    assert z_centers_ref is not None
    return V15Trajectory(
        label=label,
        latent_on=latent_on,
        seed_mode=seed_mode,
        bulk_wall_on=bulk_wall,
        latent_dissipation_ablation=latent_dissipation_ablation,
        axis=axis,
        n_steps=n_steps,
        n_latent_steps=n_latent,
        record_every=record_every,
        r_yield_threshold=prov.local.r_yield_threshold,
        r_yield_knee=prov.local.target_r_yield,
        steps=np.array(steps_list, dtype=int),
        r_yield_pair=np.array(r_yield_list),
        A2_pair=np.array(a2_list),
        centroid=np.array(centroid_list),
        width=np.array(width_list),
        E_frac=np.array(efrac_list),
        total_energy_native=np.array(energy_list),
        z_centers=z_centers_ref,
        z_profiles=np.stack(profiles, axis=0),
        pocket_z0=z_med,
        pocket_z_half=pocket_z_half,
        snapshot_steps=np.array(snap_steps, dtype=int),
        snapshot_node_energy=np.stack(snap_energy, axis=0),
        net_pos=net.pos.copy(),
        pocket_mask=pocket.copy(),
        pair_mask=pair_mask.copy(),
        pair_node_indices=pair_nodes.copy(),
    )


def v15a_ablation_gates(*, L: int = 10, smoke: bool = False) -> dict:
    """v15a-ablation — latent-window dissipation OFF vs baseline cell A."""
    L_p15 = 8 if smoke else max(L, 10)
    tau_steps = 10 if smoke else DEFAULT_TAU_STEPS

    net = cl.build_srs_net(L_p15, "right")
    pocket = compton_pocket_mask(net)
    prov = build_lane_a_provenance(net, pocket, smoke=smoke)
    common = dict(prov=prov, tau_steps=tau_steps)

    baseline = run_p15_nucleation_cell(
        net,
        "A cosmic IC baseline",
        latent_on=True,
        seed_mode="pair",
        bulk_wall=True,
        latent_dissipation_ablation=False,
        **common,
    )
    ablated = run_p15_nucleation_cell(
        net,
        "A cosmic IC latent ablation",
        latent_on=True,
        seed_mode="pair",
        bulk_wall=True,
        latent_dissipation_ablation=True,
        **common,
    )
    heal = run_p15_nucleation_cell(
        net,
        "B heal",
        latent_on=False,
        seed_mode="none",
        bulk_wall=False,
        **common,
    )

    heal_ok = (
        heal.A2_seed_peak < 0.1 * A_YIELD_SQ
        and heal.total_energy_ratio < 1.01
    )
    gain_r = ablated.r_yield_seed_peak / (baseline.r_yield_seed_peak + 1e-30)
    gain_a2 = ablated.A2_seed_peak / (baseline.A2_seed_peak + 1e-30)

    if ablated.p15n_pass and heal_ok:
        verdict = "NUCLEATION-LANDED"
    elif (
        ablated.r_yield_seed_peak >= 0.5 * prov.local.r_yield_threshold
        and ablated.E_frac_interior >= 0.40
    ):
        verdict = "PARTIAL"
    elif gain_r > 1.5 or gain_a2 > 1.5:
        verdict = "DISSIPATION-CONFIRMED"
    elif heal_ok:
        verdict = "HEAL-CONFIRMED"
    else:
        verdict = "ENGINE-GAP"

    return {
        "engine_class": (
            "v15a-ablation: latent phase χ=0, snap-OFF, memristive-OFF"
        ),
        "smoke": smoke,
        "L_p15": L_p15,
        "provenance": provenance_dict(prov),
        "ablation_switches": {
            "latent_chi_shock": 0.0,
            "latent_snap": False,
            "latent_memristive": False,
            "baseline_chi_shock": prov.timing.chi_shock,
        },
        "P15_A_baseline": baseline,
        "P15_A_ablated": ablated,
        "P15_B_heal": heal,
        "gain_r_yield": float(gain_r),
        "gain_A2_vsnap": float(gain_a2),
        "P15_H_heal_pass": heal_ok,
        "verdict": verdict,
    }

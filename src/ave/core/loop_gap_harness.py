"""
LOOP GAP unified harness — one K4⊗Cosserat probe for ranks 1–4.

Replaces per-version genesis engines (v18+) with rank-parameterized profiles on
VacuumEngine3D. srs chiral_lattice_v{9..17} is FROZEN (falsifiers only).

DAG: _orchestration/2026-06-12_loop-gap-engine-dag.md
Epic: _orchestration/2026-06-12_loop-gap-unified-harness.md
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Literal

import numpy as np

from ave.core.constants import ALPHA, R_III
from ave.core.bulk_rarefaction_sector import ENGINE_C0
from ave.core.genesis_v18_coupled import (
    P11_A_PERSIST_MIN,
    P11_E_PERSIST_MIN,
    COMPTON_DRIVE_MULTS,
    DEFAULT_QUIET_MULT,
    IMPEDANCE_CFL_SAFE,
    IMPEDANCE_CLAMP_K,
    P18_GAMMA_MAX,
    P18_PHI_GROW_MIN,
    P18_RHO_MIN,
    P18_VINC_FLOOR,
    snapshot_op14,
    tau_steps_k4,
)
from ave.core.loop_gap_seeds import A_LOCK_DEFAULT, A_YIELD, SeedMode, apply_seed
from ave.core.scalar_grade_seed import ScalarSeedMode, apply_scalar_seed_if_enabled, scalar_seed_certificate
from ave.topological.k4_cosserat_coupling import _cosserat_A_squared
from ave.topological.vacuum_engine import EngineConfig, VacuumEngine3D

# Rank labels align with doctrine §2 plumber order.
RANK_NAMES = {
    1: "container",
    2: "compton_drive",
    3: "energize_lock",
    4: "remanence",
}

IMPEDANCE_DEFAULTS = dict(
    impedance_clamp_strength=IMPEDANCE_CLAMP_K,
    impedance_cfl_safety=IMPEDANCE_CFL_SAFE,
    impedance_implicit=True,
)

PHI_BASELINE_FLOOR = 1e-18
BulkSeedMode = Literal["probe", "circulation", "none"]
C_BULK2_LIVE_FRAC = 0.99
OP2_VINC_FLOOR = 1e-2
OP2_GAMMA_BULK_MAX = P18_GAMMA_MAX
DLITE_PREREG = "research/2026-06-12_loop-gap-harness-rank1-regime_prereg_FROZEN.md"
CPRIME_PREREG = "research/2026-06-13_loop-gap-scalar-grade-restoration_prereg_FROZEN.md"
H_DRIFT_MAX_REL = 1e-6  # F2 conservative-window ceiling (prereg §4 F2)


@dataclass(frozen=True)
class LoopGapResult:
    label: str
    rank_target: int
    seed_mode: str
    a_lock: float
    n_drive_mult: float
    n_drive: int
    n_quiet: int
    v_inc_peak: float
    gamma_min_drive: float
    phi_link_sq_baseline: float
    phi_growth: float
    rho_cross_end: float
    E_persist_ratio: float
    phi_persist_ratio: float
    S_persist_delta: float
    rank1_pass: bool
    rank3_pass: bool
    rank4_pass: bool
    bin_label: str
    bulk_density_on: bool = False
    bulk_seed: str = "none"
    rho_bar_min_end: float = 0.0
    rho_bar_min_drive: float = 0.0
    c_bulk2_min_end: float = 0.0
    c_bulk2_min_drive: float = 0.0
    max_omega_end: float = 0.0
    omega_peak: float = 0.0
    omega_peak_evolved: float = 0.0
    max_a_sq_k4_end: float = 0.0
    channel_primary: str = "EM+shear"
    channel_tags: dict[str, dict[str, float]] = field(default_factory=dict)
    rank1b_pass: bool = False
    gamma_bulk_min_drive: float = 0.0
    gamma_bulk_min_end: float = 0.0
    target_a_front: float = 0.0
    achieved_a_front_seed: float = 0.0
    regime_valid: bool = True
    op2_bin: str = "ENGINE-GAP"
    scalar_seed_on: bool = False
    scalar_seed_frac: float = 0.0
    v_to_omega_source_on: bool = False
    gap_c_coupling_on: bool = False
    bulk_force_v_to_omega: bool = False
    a2_v_peak: float = 0.0
    h_drift_rel: float = 0.0
    cp8_topology_null: bool = False
    scalar_bin: str = ""


def engine_config_for_rank(rank: int, **overrides: Any) -> EngineConfig:
    """Cumulative capability profile per engine DAG."""
    rank = int(rank)
    if rank < 1 or rank > 4:
        raise ValueError(f"rank must be 1..4, got {rank}")

    base = dict(
        N=14,
        pml=3,
        temperature=0.0,
        use_asymmetric_saturation=True,
        disable_cosserat_lc_force=True,
        couple_v_sector=True,
        use_trilinear_converter=True,
        converter_mode="trilinear",
        use_impedance_boundary=True,
        use_memristive_saturation=(rank >= 4),
        **IMPEDANCE_DEFAULTS,
    )
    base.update(overrides)
    return EngineConfig(**base)


def make_engine(rank: int, **overrides: Any) -> VacuumEngine3D:
    return VacuumEngine3D(engine_config_for_rank(rank, **overrides))


def _rank_gates(
    *,
    v_peak: float,
    gamma_min: float,
    phi_growth: float,
    rho: float,
    xl_xc: float,
    E_persist: float,
    phi_persist: float,
    S_delta: float,
    impedance_on: bool,
    converter_on: bool,
    memristive_on: bool,
) -> tuple[bool, bool, bool]:
    rank1 = v_peak > P18_VINC_FLOOR and (
        not impedance_on or gamma_min <= P18_GAMMA_MAX
    )
    rank3 = converter_on and (
        phi_growth >= P18_PHI_GROW_MIN or rho >= P18_RHO_MIN or xl_xc > 0.5
    )
    rank4 = (
        E_persist >= P11_E_PERSIST_MIN
        and phi_persist >= P11_A_PERSIST_MIN
        and (not memristive_on or S_delta > 0.0)
    )
    return rank1, rank3, rank4


def _op2_bin(
    *,
    gamma_bulk_min: float,
    v_inc_peak: float,
    regime_valid: bool,
    bulk_on: bool,
) -> str:
    f1 = bulk_on and gamma_bulk_min <= OP2_GAMMA_BULK_MAX
    f2 = v_inc_peak > OP2_VINC_FLOOR
    if not regime_valid:
        return "ENGINE-GAP_POST_RUPTURE"
    if f1 and f2:
        return "OP-2-LANDED"
    if f1 or f2:
        return "OP-2-PARTIAL"
    return "ENGINE-GAP"


def _seed_a_front(engine: VacuumEngine3D) -> float:
    coupled = engine._coupled
    A_cos_sq = _cosserat_A_squared(
        coupled.cos.u,
        coupled.cos.omega,
        coupled.cos.dx,
        coupled.cos.omega_yield,
        coupled.cos.epsilon_yield,
    )
    return float(np.sqrt(np.max(A_cos_sq)))


def _bulk_channel_tag(
    *,
    bulk_on: bool,
    rho_min: float,
    v_peak: float,
    gamma_min: float,
) -> str:
    if not bulk_on:
        return "EM+shear"
    if rho_min < -1e-6:
        return "bulk+EM+shear"
    if v_peak > P18_VINC_FLOOR:
        return "EM+shear"
    if gamma_min <= P18_GAMMA_MAX:
        return "proxy+EM+shear"
    return "EM+shear"


def run_loop_gap_probe(
    label: str,
    *,
    rank_target: int = 4,
    seed_mode: SeedMode = "photon_lock",
    N: int = 14,
    amp: float | None = None,
    a_lock: float = A_LOCK_DEFAULT,
    n_drive_mult: float = 1.0,
    n_quiet_mult: float = DEFAULT_QUIET_MULT,
    impedance_on: bool = True,
    converter_on: bool = True,
    memristive_on: bool | None = None,
    bulk_density_on: bool = False,
    bulk_seed: BulkSeedMode = "probe",
    bulk_probe_amp: float = 0.08,
    bulk_m_edge: float = 0.75,
    bulk_r_core_frac: float = 0.22,
    front_target: float | None = None,
    scalar_seed_on: bool = False,
    scalar_seed_frac: float = 0.85,
    scalar_seed_mode: ScalarSeedMode = "lane1_standing",
    v_to_omega_source_on: bool = False,
    bulk_force_v_to_omega: bool = False,
    gap_c_coupling_on: bool = False,
    fast: bool = False,
) -> LoopGapResult:
    """Conservative ring-up + quiescence on VacuumEngine3D (no external sources)."""
    if memristive_on is None:
        memristive_on = rank_target >= 4

    cfg_kw = dict(N=N, bulk_density_on=bulk_density_on)
    if v_to_omega_source_on:
        cfg_kw["v_to_omega_source_on"] = True
        cfg_kw["use_impedance_boundary"] = True
    if bulk_force_v_to_omega:
        cfg_kw["bulk_force_v_to_omega"] = True
    if not impedance_on and not v_to_omega_source_on:
        cfg_kw["use_impedance_boundary"] = False
    if not converter_on:
        cfg_kw["use_trilinear_converter"] = False
    cfg_kw["use_memristive_saturation"] = memristive_on

    engine = make_engine(rank_target, **cfg_kw)
    coupled = engine._coupled
    target_a = float(front_target) if front_target is not None else 0.0
    apply_seed(
        engine,
        seed_mode,
        amp=amp,
        a_lock=a_lock,
        front_target=front_target,
    )
    apply_scalar_seed_if_enabled(
        engine,
        scalar_seed_on=scalar_seed_on,
        scalar_seed_frac=scalar_seed_frac,
        scalar_seed_mode=scalar_seed_mode,
    )
    achieved_a_seed = _seed_a_front(engine)
    if bulk_density_on:
        if bulk_seed == "probe":
            engine.apply_bulk_probe_ic(amp=bulk_probe_amp)
        elif bulk_seed == "circulation":
            engine.apply_bulk_circulation_ic(
                m_edge=bulk_m_edge,
                r_core_frac=bulk_r_core_frac,
            )
    engine.freeze_converter_wall()

    cp8_topology_null = False
    a2_v_peak = 0.0
    if scalar_seed_on:
        cert = scalar_seed_certificate(engine, frac=scalar_seed_frac)
        cp8_topology_null = bool(cert["topology_null"])
        a2_v_peak = float(cert["A2_peak"])

    tau = tau_steps_k4(coupled, fast=fast)
    n_drive = max(6 if fast else 10, int(round(n_drive_mult * tau)))
    n_quiet = max(10 if fast else 20, int(round(n_quiet_mult * tau)))
    n_total = n_drive + n_quiet

    obs0 = snapshot_op14(coupled)
    v_peak = obs0["v_inc_max"]
    omega_peak = float(np.max(np.linalg.norm(coupled.cos.omega, axis=-1)))
    omega_peak_evolved = 0.0
    gamma_min_drive = obs0["gamma_min"] if impedance_on else 0.0
    phi_baseline = max(obs0["phi_link_sq"], PHI_BASELINE_FLOOR)
    obs_driveoff = obs0
    bulk0 = engine.bulk_snapshot()
    rho_bar_min_drive = bulk0["rho_bar_min"]
    c_bulk2_min_drive = bulk0["c_bulk2_min"]
    gamma_bulk_min_drive = bulk0.get("gamma_bulk_min", 0.0)
    c0_sq = float(ENGINE_C0**2)

    for t in range(1, n_total + 1):
        engine.step()
        obs_t = snapshot_op14(coupled)
        v_peak = max(v_peak, obs_t["v_inc_max"])
        omega_peak = max(
            omega_peak, float(np.max(np.linalg.norm(coupled.cos.omega, axis=-1)))
        )
        if t >= 1:
            omega_peak_evolved = max(
                omega_peak_evolved,
                float(np.max(np.linalg.norm(coupled.cos.omega, axis=-1))),
            )
        if t == 1:
            phi_baseline = max(obs_t["phi_link_sq"], PHI_BASELINE_FLOOR)
        bulk_t = engine.bulk_snapshot()
        rho_bar_min_drive = min(rho_bar_min_drive, bulk_t["rho_bar_min"])
        c_bulk2_min_drive = min(c_bulk2_min_drive, bulk_t["c_bulk2_min"])
        if bulk_density_on:
            gamma_bulk_min_drive = min(
                gamma_bulk_min_drive, bulk_t.get("gamma_bulk_min", 0.0)
            )
        if t <= n_drive:
            if impedance_on:
                gamma_min_drive = min(gamma_min_drive, obs_t["gamma_min"])
            obs_driveoff = obs_t
    obs_end = obs_t
    bulk_end = engine.bulk_snapshot()
    max_omega_end = float(np.max(np.linalg.norm(coupled.cos.omega, axis=-1)))
    max_a_sq_k4_end = float(obs_end["max_A_sq"])
    regime_valid = max_a_sq_k4_end <= float(R_III) ** 2 + 1e-12
    gamma_bulk_min_end = bulk_end.get("gamma_bulk_min", 0.0)
    op2_bin = _op2_bin(
        gamma_bulk_min=gamma_bulk_min_drive if bulk_density_on else 0.0,
        v_inc_peak=v_peak,
        regime_valid=regime_valid,
        bulk_on=bulk_density_on,
    )

    phi_drive = max(obs_driveoff["phi_link_sq"], phi_baseline)
    phi_end = obs_end["phi_link_sq"]
    H_drive = max(obs_driveoff["H"], 1e-30)
    H_end = obs_end["H"]
    S_drive = obs_driveoff["S_mean"]
    S_end = obs_end["S_mean"]
    h_drift_rel = abs(H_end - H_drive) / H_drive

    phi_growth = phi_drive / phi_baseline
    E_persist = H_end / H_drive
    phi_persist = phi_end / phi_drive if phi_drive > 0 else 0.0
    S_delta = abs(S_end - S_drive)

    rank1, rank3, rank4 = _rank_gates(
        v_peak=v_peak,
        gamma_min=gamma_min_drive,
        phi_growth=phi_growth,
        rho=obs_end["rho_cross"],
        xl_xc=obs_end["xl_over_xc"],
        E_persist=E_persist,
        phi_persist=phi_persist,
        S_delta=S_delta,
        impedance_on=impedance_on,
        converter_on=converter_on,
        memristive_on=memristive_on,
    )

    if rank4 and rank1:
        bin_label = "REMANENCE-LANDED"
    elif rank1 and rank3:
        bin_label = "OPERATOR-SET"
    elif rank1:
        bin_label = "VINC-ONLY"
    else:
        bin_label = "ENGINE-GAP"

    channel_tags = {
        "EM": {"v_inc_peak": v_peak, "max_a_sq_k4": max_a_sq_k4_end},
        "shear": {"max_omega": max_omega_end, "rho_cross": obs_end["rho_cross"]},
        "bulk": {
            "rho_bar_min": bulk_end["rho_bar_min"],
            "c_bulk2_min": bulk_end["c_bulk2_min"],
            "rho_bar_min_drive": rho_bar_min_drive,
            "c_bulk2_min_drive": c_bulk2_min_drive,
            "max_abs_u_adv": bulk_end["max_abs_u_adv"],
            "gamma_bulk_min": gamma_bulk_min_drive,
            "gamma_bulk_min_end": gamma_bulk_min_end,
        },
        "proxy": {"gamma_min": gamma_min_drive},
    }
    rank1b = bulk_density_on and (
        rho_bar_min_drive < -1e-6
        or c_bulk2_min_drive < C_BULK2_LIVE_FRAC * c0_sq
    ) and np.isfinite(H_end)

    return LoopGapResult(
        label=label,
        rank_target=rank_target,
        seed_mode=seed_mode,
        a_lock=a_lock,
        n_drive_mult=n_drive_mult,
        n_drive=n_drive,
        n_quiet=n_quiet,
        v_inc_peak=v_peak,
        gamma_min_drive=gamma_min_drive,
        phi_link_sq_baseline=phi_baseline,
        phi_growth=phi_growth,
        rho_cross_end=obs_end["rho_cross"],
        E_persist_ratio=E_persist,
        phi_persist_ratio=phi_persist,
        S_persist_delta=S_delta,
        rank1_pass=rank1,
        rank3_pass=rank3,
        rank4_pass=rank4,
        bin_label=bin_label,
        bulk_density_on=bulk_density_on,
        bulk_seed=bulk_seed if bulk_density_on else "none",
        rho_bar_min_end=bulk_end["rho_bar_min"],
        rho_bar_min_drive=rho_bar_min_drive,
        c_bulk2_min_end=bulk_end["c_bulk2_min"],
        c_bulk2_min_drive=c_bulk2_min_drive,
        max_omega_end=max_omega_end,
        omega_peak=omega_peak,
        omega_peak_evolved=omega_peak_evolved,
        max_a_sq_k4_end=max_a_sq_k4_end,
        channel_primary=_bulk_channel_tag(
            bulk_on=bulk_density_on,
            rho_min=bulk_end["rho_bar_min"],
            v_peak=v_peak,
            gamma_min=gamma_min_drive,
        ),
        channel_tags=channel_tags,
        rank1b_pass=bool(rank1b),
        gamma_bulk_min_drive=gamma_bulk_min_drive,
        gamma_bulk_min_end=gamma_bulk_min_end,
        target_a_front=target_a,
        achieved_a_front_seed=achieved_a_seed,
        regime_valid=regime_valid,
        op2_bin=op2_bin,
        scalar_seed_on=scalar_seed_on,
        scalar_seed_frac=scalar_seed_frac if scalar_seed_on else 0.0,
        v_to_omega_source_on=v_to_omega_source_on,
        gap_c_coupling_on=gap_c_coupling_on,
        bulk_force_v_to_omega=bulk_force_v_to_omega,
        a2_v_peak=a2_v_peak,
        h_drift_rel=h_drift_rel,
        cp8_topology_null=cp8_topology_null,
    )


def loop_gap_battery(
    *,
    N: int = 14,
    smoke: bool = False,
    primary_seed: SeedMode = "photon_lock",
    bulk_density_on: bool = False,
) -> dict:
    """Standard ablation battery per engine DAG § mandatory arms."""
    mults = (1.0,) if smoke else COMPTON_DRIVE_MULTS
    fast = smoke
    quiet_mult = 1.5 if smoke else DEFAULT_QUIET_MULT
    sweep: list[dict] = []
    for m in mults:
        r = run_loop_gap_probe(
            f"rank4_{primary_seed}_{m}x",
            rank_target=4,
            seed_mode=primary_seed,
            N=N,
            n_drive_mult=m,
            n_quiet_mult=quiet_mult,
            bulk_density_on=bulk_density_on,
            fast=fast,
        )
        sweep.append(_to_dict(r))

    ablation_kw = dict(
        N=N,
        rank_target=4,
        n_drive_mult=1.0,
        n_quiet_mult=quiet_mult,
        bulk_density_on=bulk_density_on,
        fast=fast,
    )
    seed_modes: list[SeedMode] = ["pair", "photon_lock", "graded_a0"] if not smoke else [primary_seed]
    seed_arms: list[dict] = []
    for mode in seed_modes:
        r = run_loop_gap_probe(
            f"seed_{mode}",
            seed_mode=mode,
            **ablation_kw,
        )
        seed_arms.append(_to_dict(r))

    mem_off = run_loop_gap_probe(
        "memristive_OFF",
        seed_mode=primary_seed,
        memristive_on=False,
        **ablation_kw,
    )
    wall_off = run_loop_gap_probe(
        "impedance_OFF",
        seed_mode=primary_seed,
        impedance_on=False,
        **ablation_kw,
    )
    conv_off = run_loop_gap_probe(
        "converter_OFF",
        seed_mode=primary_seed,
        converter_on=False,
        **ablation_kw,
    )
    heal = run_loop_gap_probe(
        "heal_zero_seed",
        seed_mode="pair",
        amp=0.0,
        **ablation_kw,
    )
    bulk_kw = {k: v for k, v in ablation_kw.items() if k != "bulk_density_on"}
    bulk_off = run_loop_gap_probe(
        "bulk_OFF",
        seed_mode=primary_seed,
        bulk_density_on=False,
        **bulk_kw,
    )
    bulk_on = run_loop_gap_probe(
        "bulk_ON",
        seed_mode=primary_seed,
        bulk_density_on=True,
        bulk_seed="probe",
        **bulk_kw,
    )
    bulk_circ = run_loop_gap_probe(
        "bulk_circulation",
        seed_mode=primary_seed,
        bulk_density_on=True,
        bulk_seed="circulation",
        **bulk_kw,
    )

    a_lock_sweep: list[dict] = []
    if not smoke and primary_seed == "photon_lock":
        for a in (1.5, 3.0, 6.0):
            r = run_loop_gap_probe(
                f"a_lock_{a}",
                seed_mode="photon_lock",
                a_lock=a,
                **ablation_kw,
            )
            a_lock_sweep.append(_to_dict(r))

    best = max(
        sweep,
        key=lambda d: (d["rank1_pass"], -d["gamma_min_drive"], d["E_persist_ratio"]),
    )
    any_r4 = any(d["rank4_pass"] for d in sweep)

    if any_r4:
        verdict = "REMANENCE-LANDED"
    elif best["rank1_pass"] and best["rank3_pass"]:
        verdict = "OPERATOR-SET-ONLY"
    elif best["rank1_pass"]:
        verdict = "PARTIAL"
    else:
        verdict = "ENGINE-GAP"

    bulk_f1 = (
        bulk_on.rho_bar_min_end != bulk_off.rho_bar_min_end
        or bulk_on.c_bulk2_min_end != bulk_off.c_bulk2_min_end
    )
    bulk_f2 = bulk_on.rank1b_pass and bulk_on.channel_primary != "EM+shear"

    return {
        "harness": "loop_gap_harness",
        "harness_phase": 2 if not bulk_density_on else "2b",
        "platform": "VacuumEngine3D",
        "srs_genesis": "FROZEN_v17",
        "primary_seed": primary_seed,
        "bulk_density_on": bulk_density_on,
        "verdict": verdict,
        "rank_sweep": sweep,
        "seed_ablation": seed_arms,
        "a_lock_sweep": a_lock_sweep,
        "mem_ablation": _to_dict(mem_off),
        "wall_ablation": _to_dict(wall_off),
        "converter_ablation": _to_dict(conv_off),
        "bulk_ablation": {
            "bulk_OFF": _to_dict(bulk_off),
            "bulk_ON": _to_dict(bulk_on),
            "bulk_circulation": _to_dict(bulk_circ),
        },
        "bulk_f1_pass": bulk_f1,
        "bulk_f2_channel_tagged": bulk_f2,
        "heal": _to_dict(heal),
        "best_arm": best["label"],
        "dag": "_orchestration/2026-06-12_loop-gap-engine-dag.md",
        "prereg": "research/2026-06-12_loop-gap-harness-bulk-channel_prereg_DRAFT.md",
        "classification": {
            "rank_sweep": "emergence-test",
            "seed_ablation": "consistency-check",
            "bulk_ablation": "consistency-check",
            "note": "probe IC = sector-live; circulation IC = OP-3 motor seed (no GAP-C)",
        },
    }


def _scalar_f1_pass(row: dict) -> bool:
    """F1 — scalar seed live (CP8 + A²_V floor)."""
    if not row.get("scalar_seed_on"):
        return False
    floor = 0.25 * float(A_YIELD**2)
    return bool(row.get("cp8_topology_null")) and float(row.get("a2_v_peak", 0.0)) > floor


def _scalar_f2_pass(s2: dict, s3: dict) -> bool:
    """F2 — V→ω source fires vs S2; H drift bounded; not bulk-force detonation."""
    if s3.get("bulk_force_v_to_omega"):
        return False
    omega_ok = float(s3.get("max_omega_end", 0.0)) > float(s2.get("max_omega_end", 0.0))
    h_ok = float(s3.get("h_drift_rel", 1.0)) <= H_DRIFT_MAX_REL
    # v_inc nucleation is F2 PARTIAL metric — full F2 PASS needs omega lift only at smoke
    return omega_ok and h_ok


def _scalar_f3_pass(row: dict) -> bool:
    """F3 — OP-2 composite on restored engine."""
    if not row.get("regime_valid", True):
        return False
    f1_bulk = float(row.get("gamma_bulk_min_drive", 0.0)) <= OP2_GAMMA_BULK_MAX
    f2_v = float(row.get("v_inc_peak", 0.0)) > OP2_VINC_FLOOR
    return f1_bulk and f2_v


def _scalar_arm_bin(
    *,
    arm: dict,
    s1: dict | None = None,
    s2: dict | None = None,
) -> str:
    """Per-arm SCALAR sub-bin (primary arms S1–S3)."""
    label = arm.get("label", "")
    if label == "S0":
        return "BASELINE"
    if label == "S1":
        return "SCALAR-IC-LANDED" if _scalar_f1_pass(arm) else "REPRESENTATION-GAP"
    if label in ("S2", "S3", "S4") and s2 is not None:
        f1 = _scalar_f1_pass(arm)
        if not f1:
            return "REPRESENTATION-GAP"
        if label == "S2":
            return "ABSORB-ARM"
        f2 = _scalar_f2_pass(s2, arm)
        f3 = _scalar_f3_pass(arm)
        if f2 and f3:
            return "SCALAR-LANDED"
        if f2 or f3 or arm.get("op2_bin") == "OP-2-PARTIAL":
            return "SCALAR-PARTIAL"
        return "REPRESENTATION-GAP"
    return ""


def _scalar_battery_verdict(
    *,
    s0: dict,
    s1: dict,
    s2: dict,
    s3: dict,
) -> str:
    """Program-level SCALAR bin from prereg §4 F1–F3 on S3 primary arm."""
    if not s3.get("regime_valid", True):
        return "ENGINE-GAP_POST_RUPTURE"
    f1_s1 = _scalar_f1_pass(s1)
    f1_s3 = _scalar_f1_pass(s3)
    if not (f1_s1 and f1_s3):
        return "REPRESENTATION-GAP"
    f2 = _scalar_f2_pass(s2, s3)
    f3 = _scalar_f3_pass(s3)
    if f2 and f3:
        return "SCALAR-LANDED"
    if f2 or f3 or s3.get("op2_bin") in ("OP-2-PARTIAL", "OP-2-LANDED"):
        return "SCALAR-PARTIAL"
    if f2:
        return "SCALAR-PARTIAL"
    return "REPRESENTATION-GAP"


def loop_gap_scalar_battery(
    *,
    N: int = 10,
    frac: float = 0.85,
    include_frac_sweep: bool = False,
) -> dict:
    """C′ smoke battery S0–S4 + ablations per scalar-grade prereg §3."""
    fast = True
    quiet_mult = 1.0
    drive_mult = 0.75
    base = dict(
        N=N,
        rank_target=1,
        bulk_density_on=True,
        bulk_seed="probe",
        front_target=A_YIELD,
        n_drive_mult=drive_mult,
        n_quiet_mult=quiet_mult,
        fast=fast,
        scalar_seed_frac=frac,
    )

    s0 = run_loop_gap_probe(
        "S0",
        seed_mode="photon_lock",
        scalar_seed_on=False,
        v_to_omega_source_on=False,
        **base,
    )
    s1 = run_loop_gap_probe(
        "S1",
        seed_mode="pair",
        amp=0.0,
        scalar_seed_on=True,
        v_to_omega_source_on=False,
        **base,
    )
    s2 = run_loop_gap_probe(
        "S2",
        seed_mode="photon_lock",
        scalar_seed_on=True,
        v_to_omega_source_on=False,
        **base,
    )
    s3 = run_loop_gap_probe(
        "S3",
        seed_mode="photon_lock",
        scalar_seed_on=True,
        v_to_omega_source_on=True,
        **base,
    )
    s4 = run_loop_gap_probe(
        "S4",
        seed_mode="photon_lock",
        scalar_seed_on=True,
        v_to_omega_source_on=True,
        gap_c_coupling_on=True,
        **base,
    )

    ablation_kw = dict(
        N=N,
        rank_target=1,
        bulk_density_on=True,
        bulk_seed="probe",
        front_target=A_YIELD,
        n_drive_mult=drive_mult,
        n_quiet_mult=quiet_mult,
        fast=fast,
        scalar_seed_frac=frac,
        seed_mode="photon_lock",
    )
    ablations = {
        "scalar_OFF": run_loop_gap_probe(
            "scalar_OFF",
            scalar_seed_on=False,
            v_to_omega_source_on=True,
            **ablation_kw,
        ),
        "source_OFF": run_loop_gap_probe(
            "source_OFF",
            scalar_seed_on=True,
            v_to_omega_source_on=False,
            **ablation_kw,
        ),
        "gap_c_OFF": run_loop_gap_probe(
            "gap_c_OFF",
            scalar_seed_on=True,
            v_to_omega_source_on=True,
            gap_c_coupling_on=False,
            **ablation_kw,
        ),
        "bulk_OFF": run_loop_gap_probe(
            "bulk_OFF",
            bulk_density_on=False,
            scalar_seed_on=True,
            v_to_omega_source_on=True,
            **{k: v for k, v in ablation_kw.items() if k != "bulk_density_on"},
        ),
        "converter_OFF": run_loop_gap_probe(
            "converter_OFF",
            scalar_seed_on=True,
            converter_on=False,
            v_to_omega_source_on=True,
            **ablation_kw,
        ),
        "impedance_OFF": run_loop_gap_probe(
            "impedance_OFF",
            scalar_seed_on=True,
            impedance_on=False,
            v_to_omega_source_on=False,
            **ablation_kw,
        ),
        "bulk_force_ON": run_loop_gap_probe(
            "bulk_force_ON",
            scalar_seed_on=True,
            v_to_omega_source_on=False,
            bulk_force_v_to_omega=True,
            **ablation_kw,
        ),
    }

    frac_sweep: list[dict] = []
    if include_frac_sweep:
        for f in (0.5, 1.0, 1.5):
            r = run_loop_gap_probe(
                f"S3_frac_{f}",
                seed_mode="photon_lock",
                scalar_seed_on=True,
                v_to_omega_source_on=True,
                scalar_seed_frac=f,
                **{k: v for k, v in base.items() if k != "scalar_seed_frac"},
            )
            frac_sweep.append(_to_dict(r))

    primary = [_to_dict(s0), _to_dict(s1), _to_dict(s2), _to_dict(s3), _to_dict(s4)]
    s2d = _to_dict(s2)
    s3d = _to_dict(s3)
    for row in primary:
        row["scalar_bin"] = _scalar_arm_bin(
            arm=row,
            s1=_to_dict(s1),
            s2=s2d,
        )

    verdict = _scalar_battery_verdict(
        s0=_to_dict(s0),
        s1=_to_dict(s1),
        s2=s2d,
        s3=s3d,
    )

    f1_pass = _scalar_f1_pass(_to_dict(s1))
    f2_pass = _scalar_f2_pass(s2d, s3d)
    f3_pass = _scalar_f3_pass(s3d)
    gap_c_wired = False  # C′5 — harness stub; S4 ≡ S3 until vent ledger ported

    return {
        "harness": "loop_gap_harness",
        "harness_phase": "C-prime",
        "platform": "VacuumEngine3D",
        "prereg": CPRIME_PREREG,
        "N": N,
        "scalar_seed_frac": frac,
        "target_a_front": A_YIELD,
        "verdict": verdict,
        "scalar_bin": verdict,
        "op2_bin": s3d["op2_bin"],
        "primary_arm": "S3",
        "falsifiers": {
            "F1_scalar_seed": f1_pass,
            "F2_v_to_omega_source": f2_pass,
            "F3_op2_composite": f3_pass,
        },
        "arms": primary,
        "frac_sweep": frac_sweep,
        "ablations": {k: _to_dict(v) for k, v in ablations.items()},
        "gap_c_coupling_wired": gap_c_wired,
        "classification": {
            "H1": "consistency-check — S0 transverse-only baseline",
            "H2": "consistency-check — S1 scalar IC without source",
            "H3": "emergence-test — S3 scalar + V→ω vs S0",
            "H4": "consistency-check — GAP-C channel separation (pending C′5)",
            "H5": "consistency-check — bulk_force detonation control",
        },
    }


def loop_gap_dlite_battery(*, N: int = 10) -> dict:
    """D-lite smoke baseline per rank-1 FROZEN charter (§3)."""
    fast = True
    quiet_mult = 1.5
    heal_kw = dict(
        N=N,
        rank_target=1,
        n_drive_mult=1.0,
        n_quiet_mult=quiet_mult,
        fast=fast,
    )
    yield_kw = dict(**heal_kw, front_target=A_YIELD)

    b0_off = run_loop_gap_probe(
        "B0_heal_bulk_OFF", seed_mode="pair", amp=0.0, bulk_density_on=False, **heal_kw
    )
    b0_on = run_loop_gap_probe(
        "B0_heal_bulk_ON",
        seed_mode="pair",
        amp=0.0,
        bulk_density_on=True,
        bulk_seed="probe",
        **heal_kw,
    )
    b1 = run_loop_gap_probe(
        "B1_photon_yield",
        seed_mode="photon_lock",
        bulk_density_on=True,
        bulk_seed="probe",
        **yield_kw,
    )
    b2 = run_loop_gap_probe(
        "B2_pair_sqrt_alpha",
        seed_mode="pair",
        amp=float(np.sqrt(ALPHA)),
        bulk_density_on=True,
        bulk_seed="probe",
        **heal_kw,
    )

    ablation_base = dict(
        N=N,
        rank_target=1,
        seed_mode="photon_lock",
        n_drive_mult=1.0,
        n_quiet_mult=quiet_mult,
        fast=fast,
        front_target=A_YIELD,
    )
    bulk_off = run_loop_gap_probe(
        "bulk_OFF", bulk_density_on=False, bulk_seed="probe", **ablation_base
    )
    wall_off = run_loop_gap_probe(
        "impedance_OFF",
        bulk_density_on=True,
        bulk_seed="probe",
        impedance_on=False,
        **ablation_base,
    )
    conv_off = run_loop_gap_probe(
        "converter_OFF",
        bulk_density_on=True,
        bulk_seed="probe",
        converter_on=False,
        **ablation_base,
    )

    primary = _to_dict(b1)
    arms = [_to_dict(b0_off), _to_dict(b0_on), _to_dict(b1), _to_dict(b2)]
    if primary["op2_bin"] == "OP-2-LANDED":
        verdict = "OP-2-LANDED"
    elif primary["op2_bin"] == "OP-2-PARTIAL":
        verdict = "OP-2-PARTIAL"
    elif primary["op2_bin"] == "ENGINE-GAP_POST_RUPTURE":
        verdict = "ENGINE-GAP_POST_RUPTURE"
    else:
        verdict = "ENGINE-GAP"

    return {
        "harness": "loop_gap_harness",
        "harness_phase": "D-lite",
        "platform": "VacuumEngine3D",
        "prereg": DLITE_PREREG,
        "N": N,
        "target_a_front": A_YIELD,
        "verdict": verdict,
        "primary_arm": primary["label"],
        "op2_bin": primary["op2_bin"],
        "arms": arms,
        "ablations": {
            "bulk_OFF": _to_dict(bulk_off),
            "impedance_OFF": _to_dict(wall_off),
            "converter_OFF": _to_dict(conv_off),
        },
        "classification": {
            "H1": "consistency-check — transverse-only ENGINE-GAP on V_inc expected",
            "H3": "consistency-check — motivates Phase C′ scalar restoration",
        },
    }


def _to_dict(r: LoopGapResult) -> dict:
    return {
        "label": r.label,
        "rank_target": r.rank_target,
        "seed_mode": r.seed_mode,
        "a_lock": r.a_lock,
        "n_drive_mult": r.n_drive_mult,
        "n_drive": r.n_drive,
        "n_quiet": r.n_quiet,
        "v_inc_peak": r.v_inc_peak,
        "gamma_min_drive": r.gamma_min_drive,
        "phi_link_sq_baseline": r.phi_link_sq_baseline,
        "phi_growth": r.phi_growth,
        "rho_cross_end": r.rho_cross_end,
        "E_persist_ratio": r.E_persist_ratio,
        "phi_persist_ratio": r.phi_persist_ratio,
        "S_persist_delta": r.S_persist_delta,
        "rank1_pass": r.rank1_pass,
        "rank3_pass": r.rank3_pass,
        "rank4_pass": r.rank4_pass,
        "bin_label": r.bin_label,
        "bulk_density_on": r.bulk_density_on,
        "bulk_seed": r.bulk_seed,
        "rho_bar_min_end": r.rho_bar_min_end,
        "rho_bar_min_drive": r.rho_bar_min_drive,
        "c_bulk2_min_end": r.c_bulk2_min_end,
        "c_bulk2_min_drive": r.c_bulk2_min_drive,
        "max_omega_end": r.max_omega_end,
        "max_a_sq_k4_end": r.max_a_sq_k4_end,
        "channel_primary": r.channel_primary,
        "channel_tags": r.channel_tags,
        "rank1b_pass": r.rank1b_pass,
        "gamma_bulk_min_drive": r.gamma_bulk_min_drive,
        "gamma_bulk_min_end": r.gamma_bulk_min_end,
        "proxy_gamma_min": r.gamma_min_drive,
        "target_a_front": r.target_a_front,
        "achieved_a_front_seed": r.achieved_a_front_seed,
        "regime_valid": r.regime_valid,
        "op2_bin": r.op2_bin,
        "scalar_seed_on": r.scalar_seed_on,
        "scalar_seed_frac": r.scalar_seed_frac,
        "v_to_omega_source_on": r.v_to_omega_source_on,
        "gap_c_coupling_on": r.gap_c_coupling_on,
        "bulk_force_v_to_omega": r.bulk_force_v_to_omega,
        "a2_v_peak": r.a2_v_peak,
        "h_drift_rel": r.h_drift_rel,
        "cp8_topology_null": r.cp8_topology_null,
        "omega_peak": r.omega_peak,
        "omega_peak_evolved": r.omega_peak_evolved,
        "scalar_bin": r.scalar_bin,
    }

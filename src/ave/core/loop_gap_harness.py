"""
LOOP GAP unified harness — one K4⊗Cosserat probe for ranks 1–4.

Replaces per-version genesis engines (v18+) with rank-parameterized profiles on
VacuumEngine3D. srs chiral_lattice_v{9..17} is FROZEN (falsifiers only).

DAG: _orchestration/2026-06-12_loop-gap-engine-dag.md
Epic: _orchestration/2026-06-12_loop-gap-unified-harness.md
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from ave.core.chiral_lattice_v11 import (
    P11_A_PERSIST_MIN,
    P11_E_PERSIST_MIN,
)
from ave.core.constants import ALPHA
from ave.core.genesis_v18_coupled import (
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
from ave.core.loop_gap_seeds import A_LOCK_DEFAULT, SeedMode, apply_seed
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
    fast: bool = False,
) -> LoopGapResult:
    """Conservative ring-up + quiescence on VacuumEngine3D (no external sources)."""
    if memristive_on is None:
        memristive_on = rank_target >= 4

    cfg_kw = dict(N=N)
    if not impedance_on:
        cfg_kw["use_impedance_boundary"] = False
    if not converter_on:
        cfg_kw["use_trilinear_converter"] = False
    cfg_kw["use_memristive_saturation"] = memristive_on

    engine = make_engine(rank_target, **cfg_kw)
    coupled = engine._coupled
    apply_seed(engine, seed_mode, amp=amp, a_lock=a_lock)
    engine.freeze_converter_wall()

    tau = tau_steps_k4(coupled, fast=fast)
    n_drive = max(6 if fast else 10, int(round(n_drive_mult * tau)))
    n_quiet = max(10 if fast else 20, int(round(n_quiet_mult * tau)))
    n_total = n_drive + n_quiet

    obs0 = snapshot_op14(coupled)
    v_peak = obs0["v_inc_max"]
    gamma_min_drive = obs0["gamma_min"] if impedance_on else 0.0
    phi_baseline = max(obs0["phi_link_sq"], PHI_BASELINE_FLOOR)
    obs_driveoff = obs0

    for t in range(1, n_total + 1):
        engine.step()
        obs_t = snapshot_op14(coupled)
        v_peak = max(v_peak, obs_t["v_inc_max"])
        if t == 1:
            phi_baseline = max(obs_t["phi_link_sq"], PHI_BASELINE_FLOOR)
        if t <= n_drive:
            if impedance_on:
                gamma_min_drive = min(gamma_min_drive, obs_t["gamma_min"])
            obs_driveoff = obs_t
    obs_end = obs_t

    phi_drive = max(obs_driveoff["phi_link_sq"], phi_baseline)
    phi_end = obs_end["phi_link_sq"]
    H_drive = max(obs_driveoff["H"], 1e-30)
    H_end = obs_end["H"]
    S_drive = obs_driveoff["S_mean"]
    S_end = obs_end["S_mean"]

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
    )


def loop_gap_battery(
    *,
    N: int = 14,
    smoke: bool = False,
    primary_seed: SeedMode = "photon_lock",
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
            fast=fast,
        )
        sweep.append(_to_dict(r))

    ablation_kw = dict(
        N=N,
        rank_target=4,
        n_drive_mult=1.0,
        n_quiet_mult=quiet_mult,
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

    return {
        "harness": "loop_gap_harness",
        "harness_phase": 2,
        "platform": "VacuumEngine3D",
        "srs_genesis": "FROZEN_v17",
        "primary_seed": primary_seed,
        "verdict": verdict,
        "rank_sweep": sweep,
        "seed_ablation": seed_arms,
        "a_lock_sweep": a_lock_sweep,
        "mem_ablation": _to_dict(mem_off),
        "wall_ablation": _to_dict(wall_off),
        "converter_ablation": _to_dict(conv_off),
        "heal": _to_dict(heal),
        "best_arm": best["label"],
        "dag": "_orchestration/2026-06-12_loop-gap-engine-dag.md",
        "classification": {
            "rank_sweep": "emergence-test",
            "seed_ablation": "consistency-check",
            "note": "∇A₀ stratification lens; not buoyancy import",
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
    }

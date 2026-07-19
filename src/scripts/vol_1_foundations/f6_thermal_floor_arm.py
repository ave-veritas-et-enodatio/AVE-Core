#!/usr/bin/env python3
"""F6 thermal-floor arm — revival-vs-floor (STAGE 3; fires the frozen §3 grid).

Prereg (FROZEN): research/2026-07-19_f6-thermal-floor-arm_prereg_FROZEN.md
  frozen-by-push 2026-07-19T22:31:10Z (API committedDate) BEFORE this driver existed.
Charter:  research/2026-07-16_f6-bath-meter_CHARTER.md §D + §D-post (FROZEN).
Certificate consumed: FLOOR-METER-VALID-BAND[0,5] (STAGE-1 floor-battery).
Instrument: src/ave/thermal/f6_bath_meter.py (LatticeBathCoupler — BYTE-UNTOUCHED).
Reused BYTE-UNTOUCHED: f6_counting_arrow_arm.py (#722 _build/_m_for), f6_floor_battery.py
  (STAGE-1 seed_floor/_signal_per_mode), f6_bath_meter_validate.py (#724 _place_detuned_band).

SECTOR / REGIME (mandatory header):
  Sector    : R7 thermal / entropy-sink (F6 ε->T2 candidate). NOT A1 mass, NOT Cosserat.
  Mode      : reactive K4 TLM lattice + modal bath PRE-OCCUPIED (static noise floor).
  Regime    : Regime I sub-yield, A_max~=0.10 MILD, kappa=0.030; driven-then-source-off.
  Coord.    : revival read in the EXCESS ledger ΔE_bath = E_bath − E_floor_expected (A46).

THE HYPOTHESIS UNDER TEST (Grant's ruling): the T2 sink couples as a STATIC pre-occupied
NOISE FLOOR whose phase-randomness sets the LOCAL arrow — coherent revivals dephase into
the occupied random background, so revivals DIE as the floor rises past the signal. The
no-valve rail: the floor is lossless pre-occupied REACTANCE; any arrow is EMERGENT from
phase-statistics (no Re(Z)). Classes (frozen §4): FLOOR-ARROW / NO-SUPPRESSION /
SUPPRESSION-NOT-TRACKING-ρ / NUMERICAL.

Run: PYTHONPATH=src python src/scripts/vol_1_foundations/f6_thermal_floor_arm.py [--json]
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, field

import numpy as np

from scripts.vol_1_foundations.f6_bath_meter_validate import (
    DELTA_OMEGA as DETUNE_DW,
)
from scripts.vol_1_foundations.f6_bath_meter_validate import (
    DETUNE_M,
    _place_detuned_band,
    _q_spectrum,
)

# ── reused BYTE-UNTOUCHED machinery ──────────────────────────────────────────
from scripts.vol_1_foundations.f6_counting_arrow_arm import OMEGA_MIN, _build, _m_for
from scripts.vol_1_foundations.f6_floor_battery import _signal_per_mode, seed_floor

# ── FROZEN §3 grid (prereg) ──────────────────────────────────────────────────
KAPPA = 0.030
SCALE_MILD = 0.6
PRIMARY_DW = 0.050        # densest-viable comb (M=15)
SPARSE_DW = 0.080         # sparse control (M=10)
RHO_LADDER = (0.0, 0.3, 1.0, 2.0, 3.0, 5.0)
SEEDS = (20260719, 20260720, 20260721, 20260722, 20260723, 20260724)
HORIZON_RECURRENCES = 11
X_TABLE = (0.1, 0.3, 0.5, 1.0, 1.5, 2.0, 3.0, 5.0, 8.0, 11.0)

# ── FROZEN §4 thresholds (DERIVED; no retune) ────────────────────────────────
RIDE_ON_TOP = 0.80        # S(5)/S(0) >= this ⇒ NO-SUPPRESSION
SIG_DROP_ABS = 0.15       # absolute floor on a real decay (above the ~0.09 per-cell SEM)
HALVED = 0.50             # strong-form FLOOR-ARROW marker
STAYS_TOL = 0.20          # late-window re-revival tolerance (excess stays)
DETUNED_VALID_FRAC = 0.50 # detuned R_rev(0) must be < this * primary R_rev(0)
E_BATH_MIN = 1e-2         # detuned transfer-gate (resonance-gating; #724)
LEDGER_ID_TOL = 1e-6      # per-cell conservation identity
EPS_CLAMP = 1e-12
INV_E = 1.0 - 1.0 / np.e
_SIGCACHE: dict[float, float] = {}


def _sig(dw: float) -> float:
    if dw not in _SIGCACHE:
        _SIGCACHE[dw] = _signal_per_mode(dw)
    return _SIGCACHE[dw]


@dataclass
class Cell:
    comb: str
    dw: float
    m: int
    rho: float
    seed: int
    e0: float
    e_floor_expected: float
    n_steps: int
    clamped: bool
    max_cons_drift: float
    excess_plateau_frac: float     # ΔE_bath first-plateau / E0 (transfer health)
    t_fp: int
    r_rev: float                   # R_cum at window end (per-seed revival; frozen §4)
    r_cum_table: dict = field(default_factory=dict)
    stays_resid: float = 0.0       # R_cum(end) − R_cum(0.8·win) (re-revival check)
    # ensemble-average-first cross-check ingredients (banked per seed for later avg)
    excess_traj: list = field(default_factory=list)  # ΔE_bath(t)/E0 (for ens-avg-first)
    # Rule-10 reactance pair (sampled at ρ∈{0,1,5} on primary)
    reactance_c: dict = field(default_factory=dict)
    reactance_l: dict = field(default_factory=dict)


def _build_comb(dw: float, m: int, omega_min: float):
    return _build(dw, m, omega_min=omega_min, kappa=KAPPA, scale=SCALE_MILD)


def run_cell(comb: str, dw: float, rho: float, seed: int, omega_min: float = OMEGA_MIN,
             m: int | None = None, want_reactance: bool = False,
             want_traj: bool = False) -> Cell:
    if m is None:
        m = _m_for(dw)
    t_rec = 2 * np.pi / dw
    n_steps = int(round(HORIZON_RECURRENCES * t_rec))
    e_floor_per_mode = rho * _sig(dw)
    cpl = _build_comb(dw, m, omega_min)
    e0 = cpl.e_lat()
    seed_floor(cpl.bath, e_floor_per_mode, seed)
    e_floor_expected = m * e_floor_per_mode
    etot0 = e0 + cpl.e_bath()

    e_lat = np.empty(n_steps)
    e_bath = np.empty(n_steps)
    ebc = np.empty(n_steps) if want_reactance else None
    ebl = np.empty(n_steps) if want_reactance else None
    max_drift = 0.0
    for k in range(n_steps):
        cpl.step(k + 1)
        e_lat[k] = cpl.e_lat()
        e_bath[k] = cpl.e_bath()
        if want_reactance:
            ebc[k] = float(0.5 * (cpl.bath.omega**2 * cpl.bath.x**2).sum())
            ebl[k] = float(0.5 * (cpl.bath.p**2).sum())
        max_drift = max(max_drift, abs((e_lat[k] + e_bath[k]) - etot0) / e0)

    x = np.arange(1, n_steps + 1) * dw / (2 * np.pi)
    clamp = np.nonzero(e_lat <= EPS_CLAMP)[0]
    clamped = bool(clamp.size)
    alive = int(clamp[0]) if clamped else n_steps
    excess = e_bath - e_floor_expected                # §D.D2 ΔE_bath

    # first-plateau of the excess (transfer settled)
    exc_alive = excess[:alive]
    peak = float(exc_alive.max()) if alive > 0 else 0.0
    if peak > 0:
        hit = np.nonzero(exc_alive >= INV_E * peak)[0]
        t_fp = int(hit[0]) if hit.size else 0
    else:
        t_fp = 0
    ref = excess[t_fp] if abs(excess[t_fp]) > 1e-30 else (peak if peak > 1e-30 else 1e-30)
    r_ret = np.where(np.arange(n_steps) >= t_fp, np.clip(1.0 - excess / ref, 0.0, None), 0.0)
    r_cum = np.maximum.accumulate(r_ret)
    r_rev = float(r_cum[alive - 1]) if alive > 0 else 0.0
    # excess-stays: late-window re-revival (R_cum should not grow in the last 20%)
    lo80 = int(0.8 * alive)
    stays_resid = float(r_cum[alive - 1] - r_cum[max(lo80, 0)]) if alive > 1 else 0.0

    def _at(xt, arr):
        return float(arr[int(np.argmin(np.abs(x - xt)))])

    cell = Cell(
        comb=comb, dw=dw, m=m, rho=rho, seed=seed, e0=e0,
        e_floor_expected=e_floor_expected, n_steps=n_steps, clamped=clamped,
        max_cons_drift=max_drift, excess_plateau_frac=peak / e0, t_fp=t_fp, r_rev=r_rev,
        r_cum_table={xt: _at(xt, r_cum) for xt in X_TABLE}, stays_resid=stays_resid,
    )
    if want_traj:
        cell.excess_traj = (excess / e0).tolist()
    if want_reactance:
        cell.reactance_c = {xt: _at(xt, ebc) / e0 for xt in X_TABLE}
        cell.reactance_l = {xt: _at(xt, ebl) / e0 for xt in X_TABLE}
    return cell


def _place_detuned_once() -> tuple[float, float]:
    """FROZEN placement: measure the resonant primary-comb q-spectrum (cold), place the
    32-mode Δω=0.030 detuned band off the measured q-power (#724 _place_detuned_band)."""
    m = _m_for(PRIMARY_DW)
    res = _build_comb(PRIMARY_DW, m, OMEGA_MIN)
    qs = np.empty(3000)
    for k in range(3000):
        qs[k] = res.read_q()
        res.step(k + 1)
    freqs, psd, _dom, cum = _q_spectrum(qs)
    om_min_det, _om_max, band_frac, _o99 = _place_detuned_band(freqs, psd, cum)
    return float(om_min_det), float(band_frac)


def _ensemble(cells: list[Cell]) -> dict:
    r = np.array([c.r_rev for c in cells])
    return {"r_rev_mean": float(r.mean()), "r_rev_sem": float(r.std() / np.sqrt(len(r))),
            "r_rev_by_seed": r.tolist(),
            "excess_plateau_mean": float(np.mean([c.excess_plateau_frac for c in cells])),
            "max_drift": max(c.max_cons_drift for c in cells),
            "any_clamped": any(c.clamped for c in cells),
            "stays_resid_mean": float(np.mean([c.stays_resid for c in cells]))}


def _ens_avg_first(cells: list[Cell]) -> float:
    """Non-gating cross-check: ensemble-AVERAGE ΔE_bath(t) FIRST (jitter cancels √N),
    then take the revival dip. Under-estimates if the revival TIMING jitters (smear);
    the frozen §4 per-seed-then-mean is the conservative gating observable."""
    trajs = [np.array(c.excess_traj) for c in cells if c.excess_traj]
    if not trajs:
        return float("nan")
    n = min(len(t) for t in trajs)
    mean_traj = np.mean([t[:n] for t in trajs], axis=0)
    peak = mean_traj.max()
    if peak <= 1e-30:
        return 0.0
    hit = np.nonzero(mean_traj >= INV_E * peak)[0]
    t_fp = int(hit[0]) if hit.size else 0
    ref = mean_traj[t_fp] if mean_traj[t_fp] > 1e-30 else peak
    r_ret = np.where(np.arange(n) >= t_fp, np.clip(1.0 - mean_traj / ref, 0.0, None), 0.0)
    return float(np.maximum.accumulate(r_ret)[-1])


def run_arm() -> dict:
    om_det, det_band_frac = _place_detuned_once()

    # ── the grid: primary + sparse + detuned-floor, over ρ × seeds ──
    primary = {rho: [run_cell("primary", PRIMARY_DW, rho, s,
                              want_reactance=(rho in (0.0, 1.0, 5.0) and s == SEEDS[0]),
                              want_traj=True)
                     for s in SEEDS] for rho in RHO_LADDER}
    sparse = {rho: [run_cell("sparse", SPARSE_DW, rho, s, want_traj=True) for s in SEEDS]
              for rho in RHO_LADDER}
    detuned = {rho: [run_cell("detuned", DETUNE_DW, rho, s, omega_min=om_det, m=DETUNE_M)
                     for s in SEEDS] for rho in RHO_LADDER}

    ens_p = {rho: _ensemble(primary[rho]) for rho in RHO_LADDER}
    ens_s = {rho: _ensemble(sparse[rho]) for rho in RHO_LADDER}
    ens_d = {rho: _ensemble(detuned[rho]) for rho in RHO_LADDER}
    eaf_p = {rho: _ens_avg_first(primary[rho]) for rho in RHO_LADDER}

    # ── the FLOOR-ARROW observable S(ρ) = max(R̄_rev(primary) − R̄_rev(detuned), 0) ──
    def _S(ens_pri, ens_det):
        return {rho: max(ens_pri[rho]["r_rev_mean"] - ens_det[rho]["r_rev_mean"], 0.0)
                for rho in RHO_LADDER}
    S_primary = _S(ens_p, ens_d)
    S_sparse = _S(ens_s, ens_d)

    # ── FB5 cold-control bit-for-bit (ρ=0 seed no-op vs un-seeded) ──
    cold_unseeded = run_cell("primary", PRIMARY_DW, 0.0, SEEDS[0])
    cold_diff = abs(primary[0.0][0].r_rev - cold_unseeded.r_rev)

    verdict, crit = classify(S_primary, S_sparse, ens_p, ens_d, primary, sparse, cold_diff)

    # ── FD leg (SECONDARY / non-gating; §7) ──
    fd = run_fd_leg(primary, ens_p)

    # trim the transient full-trajectory arrays before banking (eaf already reduced them)
    for rho in RHO_LADDER:
        for c in primary[rho]:
            c.excess_traj = []

    return {
        "meta": {
            "lane": "F6 thermal-floor arm — revival-vs-floor (STAGE 3)",
            "prereg": "research/2026-07-19_f6-thermal-floor-arm_prereg_FROZEN.md",
            "certificate": "FLOOR-METER-VALID-BAND[0,5] (STAGE-1 floor-battery)",
            "instrument": "src/ave/thermal/f6_bath_meter.py (BYTE-UNTOUCHED; floor = config-only)",
            "kappa": KAPPA, "operating_point": "MILD (scale=0.6)",
            "primary_comb": {"dw": PRIMARY_DW, "M": _m_for(PRIMARY_DW)},
            "sparse_comb": {"dw": SPARSE_DW, "M": _m_for(SPARSE_DW)},
            "detuned_band_omega_min": om_det, "detuned_band_power_frac": det_band_frac,
            "rho_ladder": list(RHO_LADDER), "seeds": list(SEEDS),
        },
        "verdict": verdict, "criteria": crit,
        "S_primary": S_primary, "S_sparse": S_sparse,
        "ensemble_primary": ens_p, "ensemble_sparse": ens_s, "ensemble_detuned": ens_d,
        "ens_avg_first_primary": eaf_p,
        "reactance_pair": {str(rho): {"c": primary[rho][0].reactance_c,
                                      "l": primary[rho][0].reactance_l}
                           for rho in (0.0, 1.0, 5.0)},
        "cold_control_bitforbit_diff": cold_diff,
        "fd_leg": fd,
        "cells_primary": {str(rho): [asdict(c) for c in primary[rho]] for rho in RHO_LADDER},
    }


def classify(S_primary, S_sparse, ens_p, ens_d, primary, sparse, cold_diff) -> tuple[str, dict]:
    all_cells = [c for rho in RHO_LADDER for c in primary[rho] + sparse[rho]]
    # validity gates FIRST
    conservation_ok = all(c.max_cons_drift < LEDGER_ID_TOL for c in all_cells)
    clamp_never = not any(c.clamped for c in all_cells)
    cold_reproduces = bool(cold_diff == 0.0)
    detuned_valid = bool(ens_d[0.0]["excess_plateau_mean"] < E_BATH_MIN
                         and ens_d[0.0]["r_rev_mean"] < DETUNED_VALID_FRAC * ens_p[0.0]["r_rev_mean"])
    nan_seen = any(not np.isfinite(c.r_rev) for c in all_cells)

    S0, S5 = S_primary[0.0], S_primary[5.0]
    sem_pooled = float(np.sqrt(ens_p[0.0]["r_rev_sem"] ** 2 + ens_p[5.0]["r_rev_sem"] ** 2))
    sig_drop = max(2.0 * sem_pooled, SIG_DROP_ABS)
    drop = S0 - S5
    ratio5 = (S5 / S0) if S0 > 1e-9 else float("nan")
    # monotone-tracking-ρ within seed noise (each step <= prev + SEM(prev))
    mono = True
    prev = S_primary[RHO_LADDER[0]]
    for rho in RHO_LADDER[1:]:
        if S_primary[rho] > prev + ens_p[rho]["r_rev_sem"] + 1e-12:
            mono = False
        prev = S_primary[rho]
    # sparse control also decays with ρ (whole-grid)
    sparse_decays = bool(S_sparse[5.0] < RIDE_ON_TOP * S_sparse[0.0]) if S_sparse[0.0] > 1e-9 else False
    stays = bool(abs(ens_p[5.0]["stays_resid_mean"]) <= STAYS_TOL * max(ens_p[5.0]["r_rev_mean"], 1e-9))

    significant = bool(drop > sig_drop)
    real_suppression = bool(np.isfinite(ratio5) and ratio5 < RIDE_ON_TOP)

    crit = {
        "conservation_ok": conservation_ok, "clamp_never": clamp_never,
        "cold_reproduces": cold_reproduces, "detuned_valid": detuned_valid, "nan_seen": nan_seen,
        "S0": S0, "S5": S5, "ratio5": ratio5, "drop": drop, "sig_drop": sig_drop,
        "sem_pooled": sem_pooled, "monotone": mono, "significant": significant,
        "real_suppression": real_suppression, "halved": bool(np.isfinite(ratio5) and ratio5 <= HALVED),
        "sparse_decays": sparse_decays, "excess_stays": stays,
        "S_primary_curve": dict(S_primary), "S_sparse_curve": dict(S_sparse),
    }

    if nan_seen or not conservation_ok or not clamp_never:
        return "NUMERICAL", crit
    if not real_suppression:
        return "NO-SUPPRESSION", crit
    if (mono and significant and real_suppression and stays and detuned_valid and sparse_decays):
        return "FLOOR-ARROW", crit
    return "SUPPRESSION-NOT-TRACKING-ρ", crit


def run_fd_leg(primary, ens_p) -> dict:
    """SECONDARY / non-gating (§7). Bank the floor-injected fluctuation (jitter σ(E_lat))
    vs the relaxation rate (1/e transfer time) → FD ratio, routed to the ℏ-as-FD open.
    NO claim minted; cannot affect the verdict."""
    rows = []
    for rho in RHO_LADDER:
        c0 = primary[rho][0]
        # relaxation time: t_fp (excess reaching 1−1/e of plateau), in T_rec units
        relax = c0.t_fp / (2 * np.pi / PRIMARY_DW)
        # fluctuation proxy: the ensemble jitter of R_rev (seed spread) as a fluctuation amplitude
        fluct = ens_p[rho]["r_rev_sem"]
        rows.append({"rho": rho, "relax_over_trec": relax, "fluct_proxy_sem": fluct,
                     "fd_ratio": (fluct / relax) if relax > 1e-9 else float("nan")})
    return {"note": "SECONDARY / non-gating (§7). FD ratio = fluctuation/relaxation, routed "
                    "to the ℏ-as-FD open. NO claim minted; excluded from the §4 verdict.",
            "rows": rows}


def self_check(out: dict) -> dict:
    c = out["criteria"]
    if c["nan_seen"] or not c["conservation_ok"] or not c["clamp_never"]:
        v = "NUMERICAL"
    elif not c["real_suppression"]:
        v = "NO-SUPPRESSION"
    elif (c["monotone"] and c["significant"] and c["real_suppression"] and c["excess_stays"]
          and c["detuned_valid"] and c["sparse_decays"]):
        v = "FLOOR-ARROW"
    else:
        v = "SUPPRESSION-NOT-TRACKING-ρ"
    return {"recomputed": v, "banked": out["verdict"], "match": bool(v == out["verdict"])}


def main() -> None:
    ap = argparse.ArgumentParser(description="F6 thermal-floor arm (revival-vs-floor; STAGE 3)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    out = run_arm()
    out["self_check"] = self_check(out)
    if args.json:
        print(json.dumps(out, indent=2, default=lambda o: None))
        return

    m = out["meta"]
    c = out["criteria"]
    print("=" * 100)
    print("F6 THERMAL-FLOOR ARM — revival-vs-floor (STAGE 3; κ=0.030 MILD; FLOOR-METER-VALID-BAND[0,5])")
    print("=" * 100)
    print(f"  primary Δω={m['primary_comb']['dw']} M={m['primary_comb']['M']}; "
          f"sparse Δω={m['sparse_comb']['dw']} M={m['sparse_comb']['M']}; "
          f"detuned band ω_min={m['detuned_band_omega_min']:.2f} q-frac={m['detuned_band_power_frac']:.1e}")
    print(f"  {'ρ':>5} {'R̄_rev(pri)':>11} {'±SEM':>7} {'R̄_rev(det)':>11} {'S(ρ)':>7} "
          f"{'S_sparse':>9} {'plat(pri)':>9} {'drift':>9} {'eaf':>6}")
    for rho in RHO_LADDER:
        ep, ed = out["ensemble_primary"][rho], out["ensemble_detuned"][rho]
        print(f"  {rho:>5.1f} {ep['r_rev_mean']:>11.3f} {ep['r_rev_sem']:>7.3f} {ed['r_rev_mean']:>11.3f} "
              f"{out['S_primary'][rho]:>7.3f} {out['S_sparse'][rho]:>9.3f} {ep['excess_plateau_mean']:>9.3f} "
              f"{ep['max_drift']:>9.1e} {out['ens_avg_first_primary'][rho]:>6.3f}")
    print("-" * 100)
    print(f"  validity: conservation={c['conservation_ok']} clamp_never={c['clamp_never']} "
          f"cold_reproduces={c['cold_reproduces']} detuned_valid={c['detuned_valid']}")
    print(f"  S(0)={c['S0']:.3f} S(5)={c['S5']:.3f} ratio5={c['ratio5']:.3f} drop={c['drop']:.3f}"
          f"(>{c['sig_drop']:.3f}={c['significant']}) monotone={c['monotone']} halved={c['halved']} "
          f"sparse_decays={c['sparse_decays']} excess_stays={c['excess_stays']}")
    print("  FD leg (SECONDARY/non-gating): "
          + " ".join(f"ρ{r['rho']:g}:{r['fd_ratio']:.3f}" for r in out["fd_leg"]["rows"]))
    print(f"VERDICT: {out['verdict']}   [self-check {out['self_check']['recomputed']} "
          f"match={out['self_check']['match']}]")
    print("=" * 100)


if __name__ == "__main__":
    main()

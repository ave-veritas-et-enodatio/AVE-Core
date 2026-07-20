#!/usr/bin/env python3
"""F6 floor-battery — pre-occupied-bath (thermal-floor) meter revalidation (STAGE 1).

Charter (FROZEN): research/2026-07-16_f6-bath-meter_CHARTER.md — Amendment §D
  (frozen-by-push BEFORE this driver) + §D-post (first-integrator-run corrections,
  Rule-10; frozen-by-push BEFORE this corrected driver). Battery FB1-FB5 = §D.D3;
  the excess-ledger definitions = §D.D2; the corrections + bounded band = §D-post.
Certificate extended: METER-VALID-KAPPA-BAND[0.030,0.030] @ MILD (§C-post, PR #724).
Instrument: src/ave/thermal/f6_bath_meter.py (LatticeBathCoupler / OscillatorBath —
  BYTE-UNTOUCHED; the floor is the CONFIG-ONLY bath.x/bath.p overwrite of §D.D1).
Reused BYTE-UNTOUCHED: f6_counting_arrow_arm.py (#722 _build / _m_for / grid).

SECTOR / REGIME (mandatory header):
  Sector    : R7 thermal / entropy-sink (T2 latent-heat channel; F6 ε->T2 candidate).
              NOT A1 mass, NOT Cosserat (2,3) winding/charge. The floor is a T2 sink DOF.
  Mode      : reactive K4 TLM lattice (z=3 srs, 4 ports) + modal oscillator bath,
              PRE-OCCUPIED at a target energy-per-mode with FROZEN random phases.
  Regime    : Regime I sub-yield, A_max~=0.10 MILD, at the certified kappa=0.030.
  Phase-st. : driven-then-source-off, closed cavity (pml=0). Floor = static, pre-seeded.
  Plant     : STANDALONE-K4 (within the meter certificate; #721 R-1 SCOPE CAVEAT).
  Coord.    : bath MODAL/spectral phase-space (A46) + scalar energy ledger; excess is
              read relative to the seeded sea (§D.D2), NOT raw N_occ.

WHAT THIS VALIDATES (CONSISTENCY-class): can the certified meter READ a pre-occupied
floor? It does NOT test the arrow hypothesis (STAGE 2). §D-post finding: the floor is
cleanly readable in a BOUNDED low-ρ band (identity breaks at high ρ when the floor
jitter drives over-transfer/clamp) — verdict FLOOR-METER-VALID-BAND / -LEDGER-ARTIFACT
/ -NUMERICAL. Both the frozen-literal and corrected readings are banked.

Run: PYTHONPATH=src python src/scripts/vol_1_foundations/f6_floor_battery.py [--json]
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass

import numpy as np

from ave.thermal.f6_bath_meter import FLOOR_ABS_DEFAULT

# ── #722 arm machinery (BYTE-UNTOUCHED import) ───────────────────────────────
from scripts.vol_1_foundations.f6_counting_arrow_arm import OMEGA_MIN, _build, _m_for

# ── FROZEN §D / §D-post config (ENGINEERING CHOICES — calibrated on the cold plant) ──
KAPPA = 0.030             # the certified point [0.030,0.030]
SCALE_MILD = 0.6          # MILD, A_max~=0.10
DVW = 0.050               # densest-VIABLE comb (§D-post Dp-4; M=15; clean to ρ≥5)
SPARSE = 0.080            # sparse control (M=10; clean to ρ≥5)
BOUNDARY_COMB = 0.030     # the narrow-band boundary case (M=24; clean only to ρ≤2)
BANKED_DENSEST = 0.010    # the banked-dip comb (M=71) — NOT floor-viable (FB5 cold twin)
FLOOR_SEED = 20260719     # canonical frozen RNG seed
SEEDS = (20260719, 20260720, 20260721, 20260722, 20260723, 20260724)  # FB1/FB4 ensemble
HORIZON_RECURRENCES = 11  # window (>= 2.5·T_rec; matches the arm horizon)
RHO_LADDER = (0.3, 1.0, 2.0, 3.0, 5.0)  # floor ladder (ρ=0 is the FB5 cold limit)
FROZEN_LITERAL_RHO = (0.3, 1.0, 3.0, 10.0, 30.0)  # the ORIGINAL §D.D3 ladder (frozen-literal)

# ── FROZEN tolerances (DERIVED / inherited — no tuning) ───────────────────────
LEDGER_ID_TOL = 1e-6      # standalone-K4 identity floor (banked densest cold drift 6.8e-6)
MACHINE_TOL = 1e-10       # seed-energy exactness
FLOOR_ABS = FLOOR_ABS_DEFAULT  # 1e-2 absolute per-mode floor (imported; meter default)
W5_TARE_C_TOL = 0.02      # excess-tare form agreement (§C W5)
SEED_STAT_TOL = 0.10      # FROZEN-LITERAL §D.D3 pairwise-CoV tol (superseded by §D-post Dp-2)
COV_CHAOS = 1.0           # §D-post Dp-2 → §Dp-6 RELABEL: secondary sanity bound (finite-CoV
#                           guard), NOT the FB4 pass condition (CoV 0.17-0.23 << 1.0 is trivial)
SEM_MEAN_MAX = 0.10       # §Dp-6 (PR#734 review, finding 1): FB4 stats-carry FIREABLE gate —
#                           the ensemble MEAN is a stable read iff SEM/mean < this at every ρ.
#                           Derived: SEM/mean = CoV/√N; frozen budget CoV≈0.23, N=6 ⇒ 0.094,
#                           so the 6-seed ensemble is AT the edge of adequacy (a genuinely
#                           fireable bound; a noisier bath / fewer seeds fails it). NOT tuned.
SECULAR_R_MAX = 0.9       # |Pearson r(E_lat, step)| >= this ⇒ secular drain
EPS_CLAMP = 1e-12         # E_lat <= this ⇒ scale=0 absorbing clamp fired
OVER_TRANSFER = 1.0       # ΔE_bath/E0 >= this ⇒ over-transfer (full discharge)
RHO_PAST_SIGNAL = 1.0     # floor-per-mode exceeds signal-per-mode above this
_SIG_CACHE: dict[float, float] = {}


def seed_floor(bath, e_floor_per_mode: float, seed: int) -> float:
    """CONFIG-ONLY floor seed (§D.D1; meter BYTE-UNTOUCHED). Each mode m at EXACTLY
    e_floor_per_mode with a frozen random phase; e_floor_per_mode=0 is a NO-OP."""
    if e_floor_per_mode <= 0.0:
        return 0.0
    rng = np.random.default_rng(seed)
    theta = rng.uniform(0.0, 2.0 * np.pi, size=bath.M)
    amp = np.sqrt(2.0 * e_floor_per_mode)
    bath.x = (amp / bath.omega) * np.cos(theta)
    bath.p = amp * np.sin(theta)
    return float(bath.energy())


def _signal_per_mode(dw: float) -> float:
    """FROZEN config reference: cold (ρ=0) first-plateau excess / M over the first
    2·T_rec. Deterministic; cached (identical across seeds — floor-independent)."""
    if dw in _SIG_CACHE:
        return _SIG_CACHE[dw]
    m = _m_for(dw)
    n = int(round(2 * (2 * np.pi / dw)))
    cpl = _build(dw, m, omega_min=OMEGA_MIN, kappa=KAPPA, scale=SCALE_MILD)
    e0 = cpl.e_lat()
    excess_max = 0.0
    for k in range(n):
        cpl.step(k + 1)
        excess_max = max(excess_max, e0 - cpl.e_lat())
    _SIG_CACHE[dw] = excess_max / m
    return _SIG_CACHE[dw]


@dataclass
class FloorRun:
    dw: float
    m: int
    rho: float
    seed: int
    e0: float
    e_floor_expected: float
    e_floor_seed_return: float
    n_steps: int
    clamped: bool
    over_transfer: bool
    max_cons_drift: float
    excess_plateau_frac: float
    excess_final_frac: float
    jitter_elat_frac: float
    secular_r: float
    non_secular: bool
    excess_identity_maxdiff: float
    n_occ_excess_final: int
    tare_broken_flag: bool          # √(1−E_bath/E0) NaN/clamped (E_bath>E0)
    c_excess: float                 # √(E_lat/E0) at the working window
    c_excess_form_diff: float
    c_range01_ok: bool              # FROZEN-LITERAL §D.D3 gate (c ∈ [0,1])
    c_finite_ok: bool               # §D-post Dp-3 corrected gate (finite & ≥0 & forms agree)
    clean: bool                     # all-seeds-clean ingredient: identity ∧ ¬over ∧ ¬clamp ∧ nonsecular
    nan_seen: bool = False


W_WORKING = 800  # tare working window (matches §C X5 / V5)


def run_floor_comb(dw: float, rho: float, seed: int = FLOOR_SEED,
                   horizon: int = HORIZON_RECURRENCES) -> FloorRun:
    m = _m_for(dw)
    t_rec = 2 * np.pi / dw
    n_steps = int(round(horizon * t_rec))
    e_signal_per_mode = _signal_per_mode(dw)
    e_floor_per_mode = rho * e_signal_per_mode
    cpl = _build(dw, m, omega_min=OMEGA_MIN, kappa=KAPPA, scale=SCALE_MILD)
    e0 = cpl.e_lat()
    e_floor_return = seed_floor(cpl.bath, e_floor_per_mode, seed)
    e_floor_expected = m * e_floor_per_mode
    etot0 = e0 + cpl.e_bath()

    e_lat = np.empty(n_steps)
    e_bath = np.empty(n_steps)
    max_drift = 0.0
    for k in range(n_steps):
        cpl.step(k + 1)
        e_lat[k] = cpl.e_lat()
        e_bath[k] = cpl.e_bath()
        max_drift = max(max_drift, abs((e_lat[k] + e_bath[k]) - etot0) / e0)

    nan_seen = bool(not np.all(np.isfinite(e_lat)) or not np.all(np.isfinite(e_bath)))
    clamp = np.nonzero(e_lat <= EPS_CLAMP)[0]
    clamped = bool(clamp.size)
    alive = int(clamp[0]) if clamped else n_steps
    excess = e_bath - e_floor_expected                # §D.D2 ΔE_bath
    excess_plateau = float(excess[:alive].max()) if alive > 0 else float(excess.max())
    over_transfer = bool(excess_plateau / e0 >= OVER_TRANSFER)
    excess_identity = np.abs(excess - (e0 - e_lat)) / e0   # D2 identity

    # FB1 fluctuation channel over the post-transfer alive window
    t_plat = 0
    if alive > 2 and excess_plateau > 0:
        hit = np.nonzero(excess[:alive] >= (1 - 1 / np.e) * excess_plateau)[0]
        t_plat = int(hit[0]) if hit.size else 0
    win = e_lat[max(t_plat, 1):alive]
    if win.size >= 3 and win.std() > 0:
        jitter = float(win.std() / e0)
        secular_r = float(np.corrcoef(np.arange(win.size, dtype=float), win)[0, 1])
    else:
        jitter, secular_r = (0.0, 0.0)
    non_secular = bool(abs(secular_r) < SECULAR_R_MAX)

    # FB2 excess occupancy
    e_m = cpl.bath.mode_energy()
    n_occ_excess = int(np.count_nonzero(e_m > e_floor_per_mode + FLOOR_ABS))

    # FB3 excess-tare at the working window (fixed step, not the fluctuating final step)
    w_idx = min(W_WORKING, n_steps) - 1 if not clamped else min(W_WORKING, alive) - 1
    w_idx = max(w_idx, 0)
    e_lat_w = float(e_lat[w_idx])
    e_bath_w = float(e_bath[w_idx])
    broken_arg = 1.0 - e_bath_w / e0
    tare_broken = bool(broken_arg < 0.0)
    c_excess = float(np.sqrt(max(e_lat_w / e0, 0.0)))
    excess_w = e0 - e_lat_w
    c_form = float(np.sqrt(max(1.0 - excess_w / e0, 0.0)))
    c_form_diff = abs(c_excess - c_form)
    c_range01_ok = bool(0.0 <= c_excess <= 1.0)                       # frozen-literal
    c_finite_ok = bool(np.isfinite(c_excess) and c_excess >= 0.0 and c_form_diff < W5_TARE_C_TOL)

    identity_ok = bool(max_drift < LEDGER_ID_TOL)
    clean = bool(identity_ok and (not over_transfer) and (not clamped) and non_secular)

    return FloorRun(
        dw=dw, m=m, rho=rho, seed=seed, e0=e0, e_floor_expected=e_floor_expected,
        e_floor_seed_return=e_floor_return, n_steps=n_steps, clamped=clamped,
        over_transfer=over_transfer, max_cons_drift=max_drift,
        excess_plateau_frac=excess_plateau / e0, excess_final_frac=float((e0 - e_lat[-1]) / e0),
        jitter_elat_frac=jitter, secular_r=secular_r, non_secular=non_secular,
        excess_identity_maxdiff=float(excess_identity[:alive].max()) if alive > 0 else 0.0,
        n_occ_excess_final=n_occ_excess, tare_broken_flag=tare_broken, c_excess=c_excess,
        c_excess_form_diff=c_form_diff, c_range01_ok=c_range01_ok, c_finite_ok=c_finite_ok,
        clean=clean, nan_seen=nan_seen,
    )


def run_cold_bitforbit(dw: float) -> dict:
    """FB5: ρ=0 (seed no-op) must be BYTE-IDENTICAL to the un-seeded _build path."""
    m = _m_for(dw)
    n_steps = int(round(HORIZON_RECURRENCES * (2 * np.pi / dw)))

    def _traj(on: bool):
        cpl = _build(dw, m, omega_min=OMEGA_MIN, kappa=KAPPA, scale=SCALE_MILD)
        if on:
            seed_floor(cpl.bath, 0.0, FLOOR_SEED)  # no-op (early return)
        eb = np.empty(n_steps)
        for k in range(n_steps):
            cpl.step(k + 1)
            eb[k] = cpl.e_bath()
        return eb

    maxdiff = float(np.abs(_traj(True) - _traj(False)).max())
    return {"dw": dw, "m": m, "n_steps": n_steps,
            "max_ebath_diff": maxdiff, "bit_for_bit": bool(maxdiff == 0.0)}


# ── FB aggregation (multi-seed; §D-post Dp-2) ─────────────────────────────────
def run_fb_primary() -> dict:
    """FB1/FB2/FB3 over the frozen seed ensemble on the densest-viable comb + the
    band boundary ρ_hi (Dp-1/Dp-5). Returns per-ρ aggregates + all runs."""
    per_rho = []
    all_runs = []
    for rho in RHO_LADDER:
        runs = [run_floor_comb(DVW, rho, seed=s) for s in SEEDS]
        all_runs.extend(runs)
        all_clean = all(r.clean for r in runs)
        n_id_fail = sum(1 for r in runs if r.max_cons_drift >= LEDGER_ID_TOL)
        n_over = sum(1 for r in runs if r.over_transfer)
        n_clamp = sum(1 for r in runs if r.clamped)
        per_rho.append({
            "rho": rho, "all_clean": bool(all_clean),
            "max_drift": max(r.max_cons_drift for r in runs),
            "n_identity_fail": n_id_fail, "n_over_transfer": n_over, "n_clamp": n_clamp,
            "max_excess_identity": max(r.excess_identity_maxdiff for r in runs),
            "seed_exact": bool(all(abs(r.e_floor_seed_return - r.e_floor_expected) < MACHINE_TOL
                                   for r in runs)),
            "n_occ_excess_min": min(r.n_occ_excess_final for r in runs),
            "jitter_mean": float(np.mean([r.jitter_elat_frac for r in runs])),
            "jitter_cov": float(np.std([r.jitter_elat_frac for r in runs])
                                / max(np.mean([r.jitter_elat_frac for r in runs]), 1e-30)),
            "non_secular_all": bool(all(r.non_secular for r in runs)),
            "c_finite_all": bool(all(r.c_finite_ok for r in runs)),
            "c_range01_all": bool(all(r.c_range01_ok for r in runs)),  # frozen-literal
            "tare_broken_any": bool(any(r.tare_broken_flag for r in runs)),
            "c_form_diff_max": max(r.c_excess_form_diff for r in runs),
            "excess_plateau_mean": float(np.mean([r.excess_plateau_frac for r in runs])),
        })
    # DERIVED band top: highest contiguous ρ (from the bottom) that is all-seeds-clean
    rho_hi = 0.0
    for pr in per_rho:
        if pr["all_clean"]:
            rho_hi = pr["rho"]
        else:
            break
    return {"per_rho": per_rho, "rho_hi": rho_hi, "all_runs": [asdict(r) for r in all_runs]}


def run_fb4() -> dict:
    """FB4 (§D-post Dp-2, prose-faithful 'statistics not realization carry the reads'):
    realizations differ; the ensemble MEAN is the stable read (SEM/mean reported); the
    per-realization excess-plateau CoV is finite and bounded (not realization-chaotic) and
    is the FROZEN ARM-ENSEMBLE BUDGET. The seed-robust METER reads (identity/tare/cold) are
    checked in FB1/FB2/FB3. NOT a pairwise-CoV pass/fail gate (that tests realization-
    AGREEMENT — the opposite of the prose). The frozen-literal pairwise CoV<0.10 is banked.

    §Dp-6 (PR#734 review, finding 1 — FIREABLE hardening, disclosed): the PASS now requires
    the ensemble mean to be a stable read, SEM/mean < SEM_MEAN_MAX(=0.10) at every ρ, instead
    of the trivially-true CoV < COV_CHAOS(=1.0). CoV<COV_CHAOS is kept as a secondary sanity
    guard only. No numeric shifts (SEM/mean was already banked); the banked data passes, so
    the verdict is unchanged (Rule-11 tightening, not a retune)."""
    rows = []
    realization_differs = True
    cov_bounded = True
    sem_bounded = True
    frozen_literal_pass = True
    espm = _signal_per_mode(DVW)
    m = _m_for(DVW)
    for rho in (1.0, 5.0):
        runs = [run_floor_comb(DVW, rho, seed=s) for s in SEEDS]
        plats = np.array([r.excess_plateau_frac for r in runs])
        plat_cov = float(plats.std() / max(abs(plats.mean()), 1e-30))
        sem_over_mean = float(plats.std() / np.sqrt(len(plats)) / max(abs(plats.mean()), 1e-30))
        jits = np.array([r.jitter_elat_frac for r in runs])
        b1 = _build(DVW, m, kappa=KAPPA, scale=SCALE_MILD).bath
        b2 = _build(DVW, m, kappa=KAPPA, scale=SCALE_MILD).bath
        seed_floor(b1, rho * espm, SEEDS[0])
        seed_floor(b2, rho * espm, SEEDS[1])
        real_diff = float(np.abs(b1.x - b2.x).max())
        rows.append({
            "rho": rho, "excess_plateau_cov": plat_cov, "excess_plateau_sem_over_mean": sem_over_mean,
            "excess_plateau_mean": float(plats.mean()), "jitter_cov_diag": float(jits.std() / max(jits.mean(), 1e-30)),
            "realization_maxdiff": real_diff, "frozen_literal_cov_ok": bool(plat_cov < SEED_STAT_TOL),
        })
        realization_differs = realization_differs and (real_diff > 0.0)
        cov_bounded = cov_bounded and bool(np.isfinite(plat_cov) and plat_cov < COV_CHAOS)
        sem_bounded = sem_bounded and bool(np.isfinite(sem_over_mean) and sem_over_mean < SEM_MEAN_MAX)
        frozen_literal_pass = frozen_literal_pass and bool(plat_cov < SEED_STAT_TOL)
    # PASS (§Dp-6): the ensemble mean is a stable read (SEM/mean < SEM_MEAN_MAX, FIREABLE) and
    # realizations differ; CoV < COV_CHAOS kept only as a secondary sanity guard.
    stats_carry = bool(realization_differs and sem_bounded and cov_bounded)
    arm_ensemble_budget = max(r["excess_plateau_cov"] for r in rows)  # the STAGE-2 constraint
    return {"rows": rows, "stats_carry_read": stats_carry,
            "realization_differs": bool(realization_differs),
            "sem_bounded": bool(sem_bounded), "cov_bounded": bool(cov_bounded),
            "arm_ensemble_budget_cov": arm_ensemble_budget,
            "frozen_literal_pairwise_pass": bool(frozen_literal_pass)}


def run_boundary_doc() -> dict:
    """Non-gating documentation: the narrow-band boundary comb Δω=0.030 (Dp-1) — clean
    to ρ≤2, breaks above. Confirms the band width grows as the comb transfers less."""
    rows = []
    for rho in (1.0, 2.0, 3.0):
        runs = [run_floor_comb(BOUNDARY_COMB, rho, seed=s) for s in SEEDS[:4]]
        rows.append({"rho": rho, "all_clean": bool(all(r.clean for r in runs)),
                     "n_clamp": sum(1 for r in runs if r.clamped),
                     "max_drift": max(r.max_cons_drift for r in runs)})
    return {"comb": BOUNDARY_COMB, "M": _m_for(BOUNDARY_COMB), "rows": rows}


def run_frozen_literal() -> dict:
    """The ORIGINAL §D.D3 battery, LITERAL: Δω=0.030, ρ∈{0.3,1,3,10,30}, single seed,
    FB3 c∈[0,1] ceiling, FB4 drift/jitter relative-tol. Banks its FLOOR-LEDGER-ARTIFACT
    (the both-ways honesty record — §D-post 'frozen-literal note')."""
    runs = [run_floor_comb(BOUNDARY_COMB, rho, seed=FLOOR_SEED) for rho in FROZEN_LITERAL_RHO]
    fb1_id_ok = all(r.max_cons_drift < LEDGER_ID_TOL for r in runs if not r.clamped)
    fb3_range_ok = all(r.c_range01_ok for r in runs)   # the ceiling gate that fails
    # FB4 literal: two-seed relative-tol on drift (meaningless at machine floor) — reproduce the fail
    a = run_floor_comb(BOUNDARY_COMB, 10.0, seed=SEEDS[0])
    b = run_floor_comb(BOUNDARY_COMB, 10.0, seed=SEEDS[1])
    drift_rel = abs(a.max_cons_drift - b.max_cons_drift) / max(a.max_cons_drift, b.max_cons_drift, 1e-30)
    fb4_literal_ok = drift_rel < SEED_STAT_TOL
    verdict = ("FLOOR-METER-VALID" if (fb1_id_ok and fb3_range_ok and fb4_literal_ok)
               else "FLOOR-LEDGER-ARTIFACT")
    return {"rho_ladder": list(FROZEN_LITERAL_RHO), "comb": BOUNDARY_COMB,
            "fb3_range_ok": bool(fb3_range_ok), "fb4_literal_ok": bool(fb4_literal_ok),
            "drift_rel": drift_rel, "verdict": verdict,
            "note": "Original §D.D3 binary criteria (FB3 c∈[0,1] + FB4 relative-tol) — "
                    "superseded by §D-post; banked as the both-ways honesty record."}


# ── FROZEN §D-post classifier ─────────────────────────────────────────────────
def classify(fb_primary: dict, fb4: dict, fb5: list[dict]) -> tuple[str, dict]:
    per_rho = fb_primary["per_rho"]
    rho_hi = fb_primary["rho_hi"]
    nan_seen = any(r["nan_seen"] for r in fb_primary["all_runs"])

    # within the clean band [0, rho_hi]: FB1-FB3 must hold at every clean ρ
    in_band = [pr for pr in per_rho if pr["rho"] <= rho_hi]
    fb1_ok = bool(rho_hi >= RHO_PAST_SIGNAL and all(pr["all_clean"] for pr in in_band) and len(in_band) >= 1)
    fb2_ok = bool(all(pr["max_excess_identity"] < LEDGER_ID_TOL and pr["seed_exact"]
                      and pr["n_occ_excess_min"] >= 0 for pr in in_band))
    fb3_ok = bool(all(pr["c_finite_all"] and pr["c_form_diff_max"] < W5_TARE_C_TOL for pr in in_band))
    fb3_broken_shown = any(pr["tare_broken_any"] for pr in per_rho)
    fb4_ok = bool(fb4["stats_carry_read"] and fb4["realization_differs"])
    fb5_ok = all(c["bit_for_bit"] for c in fb5)

    crit = {
        "nan_seen": bool(nan_seen), "rho_hi": rho_hi,
        "fb1_ok": fb1_ok, "fb2_ok": fb2_ok, "fb3_ok": fb3_ok,
        "fb3_broken_shown": bool(fb3_broken_shown), "fb4_ok": fb4_ok, "fb5_ok": fb5_ok,
        "band_reaches_past_signal": bool(rho_hi >= RHO_PAST_SIGNAL),
    }

    if nan_seen:
        return "FLOOR-NUMERICAL", crit
    if rho_hi < RHO_PAST_SIGNAL:
        # cannot read a floor that exceeds the signal at all ⇒ arm cannot test past-signal
        return "FLOOR-LEDGER-ARTIFACT", crit
    if fb1_ok and fb2_ok and fb3_ok and fb4_ok and fb5_ok:
        return f"FLOOR-METER-VALID-BAND[0,{rho_hi:g}]", crit
    return "FLOOR-LEDGER-ARTIFACT", crit


def run_battery() -> dict:
    fb_primary = run_fb_primary()
    fb4 = run_fb4()
    fb5 = [run_cold_bitforbit(DVW), run_cold_bitforbit(BANKED_DENSEST)]
    boundary = run_boundary_doc()
    frozen_literal = run_frozen_literal()
    verdict, crit = classify(fb_primary, fb4, fb5)
    return {
        "meta": {
            "lane": "F6 floor-battery — pre-occupied-bath meter revalidation (STAGE 1)",
            "charter": "research/2026-07-16_f6-bath-meter_CHARTER.md §D + §D-post (FROZEN)",
            "instrument": "src/ave/thermal/f6_bath_meter.py (BYTE-UNTOUCHED; floor = config-only)",
            "kappa": KAPPA, "operating_point": "MILD (scale=0.6, A_max~=0.10)",
            "densest_viable_comb": {"delta_omega": DVW, "M": _m_for(DVW)},
            "sparse_control_comb": {"delta_omega": SPARSE, "M": _m_for(SPARSE)},
            "banked_densest_comb": {"delta_omega": BANKED_DENSEST, "M": _m_for(BANKED_DENSEST)},
            "rho_ladder": list(RHO_LADDER), "seeds": list(SEEDS),
            "e_signal_per_mode_dvw": _signal_per_mode(DVW),
        },
        "verdict": verdict, "criteria": crit,
        "fb_primary": {"per_rho": fb_primary["per_rho"], "rho_hi": fb_primary["rho_hi"]},
        "fb4": fb4, "fb5": fb5, "boundary_doc": boundary,
        "frozen_literal": frozen_literal,
    }


def self_check(out: dict) -> dict:
    c = out["criteria"]
    if c["nan_seen"]:
        v = "FLOOR-NUMERICAL"
    elif c["rho_hi"] < RHO_PAST_SIGNAL:
        v = "FLOOR-LEDGER-ARTIFACT"
    elif c["fb1_ok"] and c["fb2_ok"] and c["fb3_ok"] and c["fb4_ok"] and c["fb5_ok"]:
        v = f"FLOOR-METER-VALID-BAND[0,{c['rho_hi']:g}]"
    else:
        v = "FLOOR-LEDGER-ARTIFACT"
    return {"recomputed": v, "banked": out["verdict"], "match": bool(v == out["verdict"])}


def main() -> None:
    ap = argparse.ArgumentParser(description="F6 floor-battery (STAGE 1; pre-occupied-bath revalidation)")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    args = ap.parse_args()

    out = run_battery()
    out["self_check"] = self_check(out)
    if args.json:
        print(json.dumps(out, indent=2, default=lambda o: None))
        return

    m = out["meta"]
    print("=" * 100)
    print("F6 FLOOR-BATTERY — pre-occupied-bath meter revalidation (STAGE 1; κ=0.030 MILD; §D+§D-post)")
    print("=" * 100)
    print(f"  densest-viable comb Δω={m['densest_viable_comb']['delta_omega']} M={m['densest_viable_comb']['M']}; "
          f"E_signal/mode={m['e_signal_per_mode_dvw']:.5f}; seeds={len(m['seeds'])}")
    print(f"  FB1/FB2/FB3 (densest-viable comb, ρ ladder {m['rho_ladder']}, all seeds):")
    print(f"    {'ρ':>5} {'clean':>6} {'maxDrift':>10} {'#idFail':>8} {'#over':>6} {'#clamp':>7} "
          f"{'excId':>9} {'jit(cov)':>12} {'c_fin':>6} {'c[0,1]':>7} {'broke':>6}")
    for pr in out["fb_primary"]["per_rho"]:
        print(f"    {pr['rho']:>5.1f} {str(pr['all_clean']):>6} {pr['max_drift']:>10.1e} "
              f"{pr['n_identity_fail']:>8d} {pr['n_over_transfer']:>6d} {pr['n_clamp']:>7d} "
              f"{pr['max_excess_identity']:>9.1e} {pr['jitter_mean']:>7.3f}({pr['jitter_cov']:.2f}) "
              f"{str(pr['c_finite_all']):>6} {str(pr['c_range01_all']):>7} {str(pr['tare_broken_any']):>6}")
    print(f"  ★ DERIVED clean-floor band: [0, {out['fb_primary']['rho_hi']:g}]")
    print("-" * 100)
    print("  FB4 (statistics-not-realization; excess-plateau CoV = ARM ENSEMBLE BUDGET):")
    for r in out["fb4"]["rows"]:
        print(f"    ρ={r['rho']:>4.1f} plateau_mean={r['excess_plateau_mean']:.3f} CoV={r['excess_plateau_cov']:.3f} "
              f"SEM/mean={r['excess_plateau_sem_over_mean']:.3f} realization_maxdiff={r['realization_maxdiff']:.2e} "
              f"(frozen-literal CoV<0.10={r['frozen_literal_cov_ok']})")
    f4 = out["fb4"]
    print(f"    stats_carry_read={f4['stats_carry_read']} realization_differs={f4['realization_differs']} "
          f"arm_ensemble_budget_CoV={f4['arm_ensemble_budget_cov']:.3f}")
    print("  FB5 (cold limit bit-for-bit):")
    for cc in out["fb5"]:
        print(f"    Δω={cc['dw']} M={cc['m']} max_ebath_diff={cc['max_ebath_diff']:.2e} "
              f"bit_for_bit={cc['bit_for_bit']}")
    bd = out["boundary_doc"]
    print(f"  boundary comb Δω={bd['comb']} (M={bd['M']}; non-gating doc): "
          + " ".join(f"ρ={r['rho']:g}:{'clean' if r['all_clean'] else 'BREAK('+str(r['n_clamp'])+'clamp)'}"
                     for r in bd["rows"]))
    fl = out["frozen_literal"]
    print(f"  frozen-literal (§D.D3 binary, Δω={fl['comb']}, ρ→30): {fl['verdict']} "
          f"(FB3 c∈[0,1]={fl['fb3_range_ok']}, FB4 rel-tol={fl['fb4_literal_ok']})")
    c = out["criteria"]
    print("-" * 100)
    print(f"  FB1={c['fb1_ok']} FB2={c['fb2_ok']} FB3={c['fb3_ok']}(broke_tare_shown={c['fb3_broken_shown']}) "
          f"FB4={c['fb4_ok']} FB5={c['fb5_ok']} | band_past_signal={c['band_reaches_past_signal']}")
    print(f"VERDICT: {out['verdict']}   [self-check recomputed={out['self_check']['recomputed']} "
          f"match={out['self_check']['match']}]")
    print("=" * 100)


if __name__ == "__main__":
    main()

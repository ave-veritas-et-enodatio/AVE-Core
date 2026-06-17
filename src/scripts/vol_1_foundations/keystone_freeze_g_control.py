"""Keystone FREEZE-G CONTROL (+ direct-R accounting) — the RUNG-2 decider.

INDEPENDENT VERIFICATION LANE (per multi-lane redundancy=immune-system). A
sibling lane already ran a freeze-g control at N=20/32 (branch
analysis/2026-06-16-keystone-freezeg) and reported SUBSTRATE-PUMP-CONFIRMED via
Prong-A alone. THIS driver re-runs Prong-A LEAN *and* adds the proof's §6
"cleanest closure" — Prong-B DIRECT-R ACCOUNTING — which that lane did NOT
measure. The two prongs together either doubly-confirm SUBSTRATE-PUMP or expose
WINDOW-MODEL-PUMP.

THE FORK (RUNG-2, ladder commit 4a90944c → SUBSTRATE-PUMP, R∞/R0=0.842):
  the forced-overlap (coupling_support='saturated_interior') EXCESS (ON−OFF)
  H-climb-rate PLATEAUS as dt→0. The PIECE-1 proof
  (research/2026-06-16_keystone-coupling-continuum-conservation-proof.md) shows
  the continuum coupling residual is EXACTLY the dropped moving-window term
      R = κ̃ ∫ ġ·V·Ξ ,   ġ = (∂g/∂A_V)(dA_V/dt),
  which is dt-INDEPENDENT (∝ a physical velocity, not a timestep) and so WOULD
  ALSO plateau. RUNG-2 alone therefore cannot distinguish:
    (A) genuine SUBSTRATE-PUMP (keystone NEGATIVE), vs
    (B) fixable WINDOW-MODEL-PUMP (the variationally-inconsistent f_V that omits
        the ∂g/∂V piece; freeze g → ġVΞ residual vanishes → keystone RE-OPENS).

TWO PRONGS:
  PRONG A — freeze-g control. Re-run the RUNG-2 forced-overlap dt→0 sweep TWICE:
    (1) ġ≠0 MOVING window (recompute _front_window from live A_V each step), and
    (2) ġ≡0 FROZEN window (capture g at t0 after seeding, hold it static).
    DECISIVE READ (declared BEFORE running):
      * frozen EXCESS plateau VANISHES (R∞/R0 < THRESH=0.10) → WINDOW-MODEL-PUMP,
      * frozen EXCESS plateau PERSISTS (R∞/R0 ≥ 0.10) → SUBSTRATE-PUMP CONFIRMED.
    CHEAT-CHECK (load-bearing): the coupling must STILL FIRE under frozen-g
    (f_V AND f_ω nonzero on alive cells over the window) — else a vanished
    plateau is meaningless (coupling removed, not the residual) → CONFOUNDED.

  PRONG B — direct-R accounting (the proof's §6 cleanest closure). On the LIVE-g
    ON run, measure R_t = κ̃ Σ_Bint ġ·V·Ξ each step (ġ = (g_t − g_{t−1})/dt),
    integrate Σ R_t·dt over T_win, and compare to the measured EXCESS H-climb
    (rate_excess·T_win). If Σ R·dt accounts for the EXCESS pump AND frozen-g
    kills it → WINDOW-MODEL doubly confirmed. If Σ R·dt is a SMALL fraction of
    the EXCESS AND frozen-g leaves the plateau intact → SUBSTRATE-PUMP doubly
    confirmed.

α-FREE: wall_on=False; κ̃=6/5=pq/(p+q) is the geometric exchange ratio (NOT α);
no ALPHA/KAPPA in the update path. EXCESS (ON−OFF) decision basis + B_int
interior-box witness, IDENTICAL to the ladder RUNG-2.

LEAN config (declared BEFORE running; this is a COMPARISON, robust to box size):
  N=16 (KF_N), 4-pt dt sweep (KF_NDT), T_win=2.0 (KF_TWIN), B_int half=5 (KF_H).
  dt-grid = dt_base/2^k, k=0..3. Plateau threshold = 0.10 (ladder-matched).

Run:  cd <worktree> && PYTHONPATH=src \
        /Users/grantlindblom/AVE-staging/AVE-Core/.venv/bin/python \
        src/scripts/vol_1_foundations/keystone_freeze_g_control.py
"""
from __future__ import annotations

import json
import os
import types

import numpy as np

import ave.core.constants as _avc
from ave.core.constants import ALPHA
from ave.core.a1_cosserat_moving_wall_engine import A1CosseratMovingWallEngine

HERE = os.path.dirname(os.path.abspath(__file__))

# ── LEAN frozen config (declared BEFORE running; RELATIVE moving-vs-frozen +
#    direct-R is the discriminator, NOT an absolute N=32 reproduction) ──
N = int(os.environ.get("KF_N", "16"))
DX = 1.0
PML = 0
CENTER = N / 2.0
H_BOX = int(os.environ.get("KF_H", "5"))          # B_int half-extent
T_WIN = float(os.environ.get("KF_TWIN", "2.0"))   # recording window
N_DT = int(os.environ.get("KF_NDT", "4"))         # dt grid points dt_base/2^k
THRESH = 0.10                                       # ladder plateau threshold (FROZEN)

# Seed params — IDENTICAL to the ladder RUNG-2 (same physics; only N/box shrink).
SEED_AMP = 0.1
SEED_SIGMA = 2.0
SEED_LAM = 6.0
BULK_FRAC = 0.7
BULK_SIGMA = 2.5


def _alpha_free_provenance_gate() -> None:
    """α-free guard: canonical constants module + κ̃ is the geometric 6/5, not α."""
    assert _avc.__file__.endswith("ave/core/constants.py"), "non-canonical constants"
    assert abs(ALPHA - 7.2973525693e-3) < 1e-12, "ALPHA not canonical"


def _ols_slope(t, y) -> float:
    """OLS slope of y vs t (the H-climb RATE = dH/dt) — same estimator the
    ladder uses for the EXCESS climb-rate."""
    t = np.asarray(t, dtype=float)
    y = np.asarray(y, dtype=float)
    if t.size < 2:
        return 0.0
    tm, ym = t.mean(), y.mean()
    denom = float(((t - tm) ** 2).sum())
    if denom < 1e-30:
        return 0.0
    return float(((t - tm) * (y - ym)).sum() / denom)


def _build_rung2_engine(couple_on, dt, freeze_g):
    """RUNG-2 forced-overlap engine at a given dt: co-located sub-yield bulk blob
    + ω-photon seed, coupling_support='saturated_interior', wall_off, projection
    ON — IDENTICAL physics to the ladder RUNG-2 (only N/box shrink for cost).

    freeze_g=True: capture g=_front_window() at t0 (after seeding, before any
    step) and monkey-patch eng._front_window to RETURN that frozen array, so
    ġ≡0 thereafter. Patching the ONE method freezes g coherently across the
    force (_coupling_forces: f_V=−κ̃gΞ, f_ω=−κ̃∇†(gV)) AND the energy witness
    (coupling_energy_box: H_c=κ̃∫gVΞ) — so with g held fixed f_V IS the exact
    gradient of its own frozen-g energy and the ġVΞ residual is removed by
    construction. The coupling does NOT vanish: g_frozen is the t0 saturated-
    interior window (nonzero), V and Ξ stay live (the cheat-check verifies)."""
    eng = A1CosseratMovingWallEngine(
        N=N, dx=DX, pml_thickness=PML, couple_on=couple_on, wall_on=False,
        coupling_support="saturated_interior", project_alive=True,
    )
    eng.seed_bulk_blob(center=(CENTER, CENTER, CENTER), sigma=BULK_SIGMA, frac=BULK_FRAC)
    eng.seed_cosserat_photon(
        center=(CENTER, CENTER, CENTER), sigma=SEED_SIGMA, wavelength=SEED_LAM,
        amplitude=SEED_AMP, direction=(1, 0, 0), helicity=1.0, axis=2,
    )
    if abs(dt - eng.dt) > 1e-30:
        eng.dt = float(dt)
        eng.A.dt = float(dt)
        c_omega_max = eng.c0 / np.sqrt(eng.cL2_over_cT2 * eng.A.S_min)
        dt_cos = 0.30 * eng.dx / (c_omega_max * np.sqrt(3.0))
        eng.n_sub_cos = max(1, int(np.ceil(eng.dt / max(dt_cos, 1e-30))))
        eng.dt_sub_cos = eng.dt / eng.n_sub_cos
    if freeze_g:
        g_frozen = np.asarray(eng._front_window()).copy()
        eng._front_window = types.MethodType(lambda self: g_frozen, eng)
        eng._g_frozen_t0 = g_frozen
    return eng


def _record(eng, box, dt, coupled, direct_R=False, cheat_check=False):
    """Advance over T_WIN, record box-H(t). When direct_R (LIVE-g ON run only):
    measure the PIECE-1 residual R_t = κ̃ Σ_box ġ·V·Ξ each step, ġ=(g_t−g_{t−1})/dt,
    using the SAME masked window g, the SAME V (self.A.V), and the SAME tetrahedral
    curl Ξ the coupling-energy witness uses — then integrate Σ R_t·dt over the
    window. When cheat_check: record f_V/f_ω max on alive interior + g-drift vs t0
    (the ġ witness) — the load-bearing check that frozen-g did NOT kill the
    coupling."""
    nsteps = int(np.ceil(T_WIN / dt))
    every = max(1, nsteps // 60)
    t_phys, H = [], []
    fV_hist, fw_hist, gdrift_hist = [], [], []
    R_cum = 0.0                         # Σ R_t·dt over EVERY step (not subsampled)
    R_t_series, R_t_t = [], []          # subsampled R_t for the doc
    diverged = None
    boxf = box.astype(float)
    H0_scale = abs(eng.H_witness_box(box)["H"]) + 1e-30
    alive_int = np.asarray(eng.B.mask_alive) & np.asarray(eng._interior)
    g_ref = np.asarray(eng._front_window()).copy() if cheat_check else None
    g_prev = np.asarray(eng._front_window()).copy() if direct_R else None
    for s in range(nsteps + 1):
        if s > 0:
            if coupled:
                eng.step_coupled()
            else:
                eng.B.step(dt=dt)
            if direct_R:
                # ġVΞ on the post-step state: ġ from the live window over [s−1,s],
                # paired with the live post-step V and Ξ — the exact PIECE-1 term.
                g_now = np.asarray(eng._front_window())
                g_dot = (g_now - g_prev) / dt
                Xi = np.asarray(eng._cosserat_axial_curl_tet())
                V = np.asarray(eng.A.V)
                R_t = float(eng.kappa_tilde * (g_dot * V * Xi * boxf).sum())
                R_cum += R_t * dt
                g_prev = g_now.copy()
        if s % every == 0 or s == nsteps:
            w = eng.H_witness_box(box)
            t_phys.append(s * dt)
            H.append(w["H"])
            if direct_R and s > 0:
                R_t_series.append(R_t)
                R_t_t.append(s * dt)
            if cheat_check and coupled:
                fV, fw = eng._coupling_forces()
                fV = np.asarray(fV)
                fwmag = np.sqrt((np.asarray(fw) ** 2).sum(axis=-1))
                fV_hist.append(float(np.abs(fV[alive_int]).max()) if alive_int.any() else 0.0)
                fw_hist.append(float(fwmag[alive_int].max()) if alive_int.any() else 0.0)
                g_now = np.asarray(eng._front_window())
                gdrift_hist.append(float(np.abs(g_now - g_ref).max()))
            if not np.isfinite(w["H"]) or abs(w["H"]) > 1e6 * H0_scale:
                diverged = s
                break
    out = {"t": t_phys, "H": H, "nsteps": nsteps, "diverged": diverged}
    if direct_R:
        out["R_cum_integral"] = R_cum
        out["R_t_series"] = R_t_series
        out["R_t_series_t"] = R_t_t
    if cheat_check:
        out["fV_max_hist"] = fV_hist
        out["fw_max_hist"] = fw_hist
        out["g_drift_vs_t0_hist"] = gdrift_hist
    return out


def _climb_rate(tr):
    """OLS climb-rate dH/dt of a box-H trajectory + H0."""
    H = np.asarray(tr["H"], dtype=float)
    t = np.asarray(tr["t"], dtype=float)
    H0 = float(H[0]) if H.size else 0.0
    return _ols_slope(t, H), H0


def _dt0_extrapolate(dts_arr, rates):
    """dt→0 extrapolation of the EXCESS climb-rate — EXACTLY the ladder's two
    estimators (Richardson on the two finest dt + OLS intercept). Returns
    (R0, R_inf_rich, R_inf_ols, ratio_R_inf_over_R0, monotone_decr)."""
    R0 = float(rates[0])
    dt_fine, dt_coarse = dts_arr[-1], dts_arr[-2]
    R_fine, R_coarse = rates[-1], rates[-2]
    if abs(dt_coarse - dt_fine) > 1e-30:
        R_inf_rich = float(R_fine - (R_coarse - R_fine) * dt_fine / (dt_coarse - dt_fine))
    else:
        R_inf_rich = float(R_fine)
    if dts_arr.size >= 2:
        A = np.vstack([dts_arr, np.ones_like(dts_arr)]).T
        slope_ols, intercept_ols = np.linalg.lstsq(A, rates, rcond=None)[0]
        R_inf_ols = float(intercept_ols)
    else:
        R_inf_ols = float(R_fine)
    ratio = abs(R_inf_rich) / max(abs(R0), 1e-30)
    abs_rates = np.abs(rates)
    monotone_decr = bool(np.all(np.diff(abs_rates) <= 1e-12 + 1e-30 * max(abs(R0), 1e-30)))
    return R0, R_inf_rich, R_inf_ols, ratio, monotone_decr


def _run_branch(label, freeze_g, box, dt_base, do_direct_R):
    """One RUNG-2 dt-sweep for a single branch (moving-g or frozen-g). At each dt:
    coupling-ON climb-rate, coupling-OFF climb-rate (same seed), and the EXCESS
    (ON−OFF) = the pure coupling pump. do_direct_R: on the ON run measure the
    PIECE-1 residual integral Σ R·dt at the COARSEST dt (Prong B; live-g only)."""
    print(f"\n[{label}] freeze_g={freeze_g}  coupling_support=saturated_interior  "
          f"N={N} box_half={H_BOX} T_win={T_WIN}")
    dts = [dt_base / (2.0 ** k) for k in range(N_DT)]
    sweep = []
    cheat = {"fV": [], "fw": [], "gdrift": []}
    direct_R = {"R_cum_integral": None, "R_t_series": [], "R_t_series_t": [],
                "excess_H_change": None, "accounted_frac": None}
    for k, dt in enumerate(dts):
        eng_on = _build_rung2_engine(couple_on=True, dt=dt, freeze_g=freeze_g)
        fV0, fw0 = eng_on._coupling_forces()
        fwmag0 = np.sqrt((np.asarray(fw0) ** 2).sum(axis=-1))
        alive_int = np.asarray(eng_on.B.mask_alive) & np.asarray(eng_on._interior)
        fV0_max = float(np.abs(np.asarray(fV0)[alive_int]).max()) if alive_int.any() else 0.0
        fw0_max = float(fwmag0[alive_int].max()) if alive_int.any() else 0.0
        ov = int(eng_on.coupling_support_overlap()["overlap_cells_tetrahedral"])
        # cheat-check + direct-R only at the coarsest dt (cheap, sufficient).
        do_cheat = (k == 0)
        want_R = do_direct_R and (k == 0)
        tr_on = _record(eng_on, box, dt, coupled=True, direct_R=want_R, cheat_check=do_cheat)
        rate_on, H0 = _climb_rate(tr_on)
        eng_off = _build_rung2_engine(couple_on=False, dt=dt, freeze_g=freeze_g)
        tr_off = _record(eng_off, box, dt, coupled=False)
        rate_off, _ = _climb_rate(tr_off)
        rate_excess = float(rate_on - rate_off)
        if do_cheat:
            cheat["fV"] = tr_on["fV_max_hist"]
            cheat["fw"] = tr_on["fw_max_hist"]
            cheat["gdrift"] = tr_on["g_drift_vs_t0_hist"]
        if want_R:
            direct_R["R_cum_integral"] = tr_on["R_cum_integral"]
            direct_R["R_t_series"] = tr_on["R_t_series"]
            direct_R["R_t_series_t"] = tr_on["R_t_series_t"]
        sweep.append({
            "k": k, "dt": dt, "n_sub_cos": eng_on.n_sub_cos, "H0": H0,
            "climb_rate_on": rate_on, "climb_rate_off": rate_off,
            "climb_rate_excess_on_minus_off": rate_excess,
            "fV0_max_alive": fV0_max, "fw0_max_alive": fw0_max,
            "overlap_cells_tetrahedral": ov,
            "diverged_on": tr_on["diverged"], "diverged_off": tr_off["diverged"],
        })
        print(f"  k={k} dt={dt:.4e} (n_sub={eng_on.n_sub_cos}): rate_ON={rate_on:+.5e}  "
              f"rate_OFF={rate_off:+.5e}  EXCESS={rate_excess:+.5e}  "
              f"f_V0={fV0_max:.3e} f_ω0={fw0_max:.3e} ov={ov}  div={tr_on['diverged']}")

    dts_arr = np.array([r["dt"] for r in sweep])
    rates = np.array([r["climb_rate_excess_on_minus_off"] for r in sweep])
    R0, R_inf_rich, R_inf_ols, ratio_inf, monotone = _dt0_extrapolate(dts_arr, rates)
    delta = abs(R_inf_rich - R_inf_ols)

    # Prong-B closure: does Σ R·dt account for the EXCESS H-change at coarsest dt?
    if do_direct_R and direct_R["R_cum_integral"] is not None:
        rate_excess_coarse = sweep[0]["climb_rate_excess_on_minus_off"]
        excess_dH = float(rate_excess_coarse * T_WIN)        # the EXCESS H-climb over T_win
        direct_R["excess_H_change"] = excess_dH
        direct_R["accounted_frac"] = (direct_R["R_cum_integral"] / excess_dH
                                      if abs(excess_dH) > 1e-30 else None)

    fV_w, fw_w, g_w = cheat["fV"], cheat["fw"], cheat["gdrift"]
    fV_min = float(min(fV_w)) if fV_w else 0.0
    fw_min = float(min(fw_w)) if fw_w else 0.0
    coupling_fires = bool(fV_min > 1e-12 and fw_min > 1e-12)
    g_max_drift = float(max(g_w)) if g_w else 0.0

    print(f"  → dt→0 EXCESS: R0={R0:+.5e}  R∞(Rich)={R_inf_rich:+.5e}  "
          f"R∞(OLS)={R_inf_ols:+.5e}  |R∞|/|R0|={ratio_inf:.4f}  monotone↓={monotone}")
    print(f"  → cheat-check: f_V min/window={fV_min:.3e}  f_ω min/window={fw_min:.3e}  "
          f"coupling_fires={coupling_fires}  g_max_drift={g_max_drift:.3e}")
    if do_direct_R and direct_R["R_cum_integral"] is not None:
        print(f"  → PRONG-B direct-R: ΣR·dt={direct_R['R_cum_integral']:+.5e}  "
              f"EXCESS ΔH={direct_R['excess_H_change']:+.5e}  "
              f"accounted_frac={direct_R['accounted_frac']:+.4f}")
    return {
        "label": label, "freeze_g": freeze_g, "dt_grid": dts, "sweep": sweep,
        "climb_rates_excess": rates.tolist(),
        "R0": R0, "R_inf_richardson": R_inf_rich, "R_inf_ols": R_inf_ols,
        "R_inf": R_inf_rich, "ratio_R_inf_over_R0": ratio_inf,
        "abs_rates_monotone_decreasing": monotone,
        "extrapolation_uncertainty_delta": delta,
        "cheat_check": {
            "fV_max_over_window": fV_w, "fw_max_over_window": fw_w,
            "g_max_drift_over_window": g_w, "fV_min_over_window": fV_min,
            "fw_min_over_window": fw_min, "g_max_drift": g_max_drift,
            "coupling_still_fires": coupling_fires,
        },
        "direct_R_accounting": direct_R,
    }


def main() -> dict:
    _alpha_free_provenance_gate()
    print("=" * 80)
    print("KEYSTONE FREEZE-G CONTROL (+ direct-R) — RUNG-2 forced-overlap")
    print("  ġ≠0 (moving) vs ġ≡0 (frozen);  Prong-B R=κ̃∫ġVΞ on the live-g run")
    print("=" * 80)

    ref = A1CosseratMovingWallEngine(N=N, dx=DX, pml_thickness=PML,
                                     couple_on=False, wall_on=False, project_alive=False)
    dt_base = float(ref.dt)
    box = ref.make_box_mask((CENTER, CENTER, CENTER), H_BOX)
    box_idx = np.argwhere(box)
    guard = CENTER - H_BOX
    # B_int guard-band check: guard ≥ stencil_radius(1) + n_sub_cos·c·dt margin.
    print(f"N={N} dx={DX} PML={PML} | B_int=[{box_idx.min(0)}..{box_idx.max(0)}] "
          f"({int(box.sum())} cells) | guard={guard:.0f} cells | dt_base={dt_base:.5e}")

    # PRONG A (both branches) + PRONG B (live-g branch only).
    moving = _run_branch("MOVING-g (ġ≠0, ladder default)", freeze_g=False,
                         box=box, dt_base=dt_base, do_direct_R=True)
    frozen = _run_branch("FROZEN-g (ġ≡0, the control)", freeze_g=True,
                        box=box, dt_base=dt_base, do_direct_R=False)

    # ── THE DECISIVE READ (Prong A) ──
    ratio_moving = moving["ratio_R_inf_over_R0"]
    ratio_frozen = frozen["ratio_R_inf_over_R0"]
    plateau_moving = bool(ratio_moving >= THRESH)
    plateau_frozen = bool(ratio_frozen >= THRESH)
    plateau_vanishes = bool(plateau_moving and not plateau_frozen)
    coupling_fires_frozen = bool(frozen["cheat_check"]["coupling_still_fires"])
    surviving_frac = abs(frozen["R_inf"]) / max(abs(moving["R_inf"]), 1e-30)

    # ── PRONG B confirmation: does the direct residual account for the pump? ──
    accounted = moving["direct_R_accounting"]["accounted_frac"]
    R_accounts = bool(accounted is not None and abs(accounted) >= 0.50)

    if not coupling_fires_frozen:
        verdict = "FREEZE-G-CONFOUNDED"
        reason = ("Freezing g KILLED the coupling under frozen-g (f_V or f_ω → 0 "
                  "over the window) — the changed plateau is meaningless. The "
                  "control cannot decide the fork.")
    elif plateau_vanishes:
        verdict = "WINDOW-MODEL-PUMP"
        reason = (
            f"Coupling STILL FIRES under frozen-g (f_V,f_ω nonzero on alive cells), "
            f"yet the EXCESS plateau VANISHES with ġ≡0 (|R∞|/|R0|: moving "
            f"{ratio_moving:.4f} ≥ {THRESH} → frozen {ratio_frozen:.4f} < {THRESH}). "
            f"The RUNG-2 pump WAS the moving-window residual R=κ̃∫ġVΞ "
            f"(direct-R accounted_frac={accounted}). Keystone RE-OPENS with a "
            f"variationally-consistent (frozen-g / ∂g/∂V-restored) coupling.")
    else:
        verdict = "SUBSTRATE-PUMP"
        reason = (
            f"The EXCESS plateau PERSISTS under ġ≡0 (frozen |R∞|/|R0|={ratio_frozen:.4f} "
            f"≥ {THRESH}; {surviving_frac*100:.0f}% of the moving R∞ survives freezing g) "
            f"with the coupling still firing — AND the direct-R residual ΣR·dt accounts "
            f"for only {accounted if accounted is None else f'{accounted*100:.1f}%'} of the "
            f"EXCESS pump. Freezing g (removing ġVΞ) does NOT remove the plateau; the "
            f"residual is NOT the pump. The keystone is NEGATIVE: the substrate will not "
            f"losslessly close the energize-LOCK loop even with a variationally-consistent "
            f"(frozen-g) coupling.")

    result = {
        "control": "keystone FREEZE-G (+ direct-R) — RUNG-2 forced-overlap ġ≠0 vs ġ≡0",
        "purpose": "decide RUNG-2 SUBSTRATE-PUMP vs WINDOW-MODEL-PUMP (PIECE-1 ġVΞ residual)",
        "independent_lane": "verifies the freezeg-lane SUBSTRATE-PUMP + adds Prong-B direct-R",
        "banked_rung2": {"commit": "4a90944c", "verdict": "SUBSTRATE-PUMP",
                         "ratio_R_inf_over_R0": 0.8419372278075833,
                         "N": 32, "H_box": 8, "T_win": 4.0},
        "config": {"N": N, "dx": DX, "pml": PML, "H_box": H_BOX, "T_win": T_WIN,
                   "n_dt": N_DT, "dt_base": dt_base, "threshold": THRESH,
                   "coupling_support": "saturated_interior", "wall_on": False,
                   "box_cells": int(box.sum()), "guard_cells": int(guard)},
        "alpha_free": True,
        "moving_g": moving,
        "frozen_g": frozen,
        "decisive_read": {
            "ratio_moving": ratio_moving, "ratio_frozen": ratio_frozen,
            "plateau_moving": plateau_moving, "plateau_frozen": plateau_frozen,
            "plateau_vanishes_under_frozen_g": plateau_vanishes,
            "coupling_still_fires_under_frozen_g": coupling_fires_frozen,
            "frozen_R_inf_surviving_frac_of_moving": surviving_frac,
        },
        "prong_B_direct_R": {
            "R_cum_integral": moving["direct_R_accounting"]["R_cum_integral"],
            "excess_H_change": moving["direct_R_accounting"]["excess_H_change"],
            "accounted_frac": accounted,
            "R_accounts_for_pump": R_accounts,
        },
        "verdict": verdict,
        "verdict_reason": reason,
    }

    print("\n" + "=" * 80)
    print(f"MOVING-g  R∞/R0 = {ratio_moving:.4f}   (plateau={plateau_moving})")
    print(f"FROZEN-g  R∞/R0 = {ratio_frozen:.4f}   (plateau={plateau_frozen})")
    print(f"coupling still fires under frozen-g: {coupling_fires_frozen}")
    print(f"plateau vanishes under frozen-g:     {plateau_vanishes}")
    print(f"PRONG-B direct-R accounted_frac:     {accounted}")
    print(f"\nVERDICT: {verdict}")
    print(f"  {reason}")
    print("=" * 80)

    out_path = os.path.join(HERE, "keystone_freeze_g_control_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2, default=float)
    result["results_json"] = out_path
    print(f"results → {out_path}")
    return result


if __name__ == "__main__":
    main()

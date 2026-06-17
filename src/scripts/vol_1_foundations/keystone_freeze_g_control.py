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


def main() -> dict:
    _alpha_free_provenance_gate()
    raise NotImplementedError("PRONG RUNNER lands in the next commit")


if __name__ == "__main__":
    main()

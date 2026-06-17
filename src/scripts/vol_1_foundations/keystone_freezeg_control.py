"""Keystone FREEZE-G CONTROL — the decisive experiment for the RUNG-2 fork.

THE FORK (banked RUNG-2, commit 4a90944c → SUBSTRATE-PUMP, R∞/R0=0.842):
  the forced-overlap (saturated_interior) EXCESS H-climb-rate PLATEAUS as dt→0.
  BUT a dt-INDEPENDENT plateau is EXACTLY where the PIECE-1 boundary residual
    R = κ̃ ∫ ġ·V·Ξ   (the moving window g, ġ≠0; the dropped ∂g/∂V term)
  lives — and that residual is dt-independent, so it WOULD plateau too. The
  ladder did NOT run the freeze-g control, so it cannot distinguish:
    (A) genuine SUBSTRATE-PUMP (keystone NEGATIVE), vs
    (B) a fixable WINDOW-MODEL-PUMP (the variationally-inconsistent coupling
        force; freeze g and the spurious ġVΞ residual vanishes → keystone RE-OPENS).

THE CONTROL — re-run the RUNG-2 forced-overlap config TWICE at SMALL N:
  (1) ġ≠0  MOVING window g (recompute _front_window() from the live A_V each
       step, the ladder's default) → reproduce the EXCESS plateau (~0.842).
  (2) ġ≡0  FROZEN window (capture g at t0, hold it; do NOT recompute g_front
       each step) → measure the EXCESS plateau.

THE DECISIVE READ + THE CHEAT-CHECK (load-bearing):
  * Plateau VANISHES under ġ≡0  → WINDOW-MODEL-PUMP-FIXABLE (the pump was the
    ġVΞ residual; keystone re-opens with a corrected coupling). BUT FIRST the
    CHEAT-CHECK: confirm the coupling STILL FIRES under frozen-g (f_V AND f_ω
    nonzero on alive cells over the window). If freezing g trivially KILLS the
    coupling (f_V→0), the vanished plateau is meaningless (coupling removed, not
    the residual) → FREEZE-G-CONFOUNDED.
  * Plateau PERSISTS under ġ≡0  → SUBSTRATE-PUMP-CONFIRMED (the pump is NOT the
    moving-window residual; keystone negative).

HOW g IS FROZEN (driver-only, no tracked-engine edit): _front_window() reads
the LIVE A_V=|V|/V_yield, so as Sector A's V evolves, g moves (=ġ≠0). To freeze,
we capture g_frozen = eng._front_window() AT t0 (after seeding, before stepping)
and monkey-patch eng._front_window to RETURN g_frozen. This freezes g coherently
in BOTH the coupling FORCE (_coupling_forces: f_V=−κ̃ g Ξ, f_ω=−κ̃ ∇†(gV)) AND
the H-witness energy (coupling_energy_box: H_c=κ̃∫ g V Ξ) — so with g held fixed
the coupling force IS the exact gradient of its own (frozen-g) energy, and the
ġVΞ residual is removed by construction. The coupling does NOT vanish: f_V and
f_ω stay nonzero because g_frozen is the t0 window (nonzero on the saturated
interior) and V, Ξ remain live.

α-FREE: wall_on=False on both branches; no ALPHA/KAPPA in the update path
(inherited from the ladder driver's RUNG-2 config). The (2,3) readout untouched.

Run:  PYTHONPATH=src ./.venv/bin/python \
        src/scripts/vol_1_foundations/keystone_freezeg_control.py
Env overrides: KF_N (default 20), KF_TWIN (default 2.0), KF_H (default 6 box
  half-extent), KF_NDT (default 4 dt-sweep points).
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

# ── FROZEN geometry (SMALL N — cheap control; the RELATIVE moving-vs-frozen
#    comparison is the discriminator, not an absolute reproduction of N=32) ──
N = int(os.environ.get("KF_N", "20"))
DX = 1.0
PML = 0
CENTER = N / 2.0
H_BOX = int(os.environ.get("KF_H", "6"))         # B_int half-extent (guard to edge)
T_WIN = float(os.environ.get("KF_TWIN", "2.0"))  # recording window (shorter = cheaper)
N_DT = int(os.environ.get("KF_NDT", "4"))        # dt grid points: dt_base/2^k

# Seed params — IDENTICAL to the ladder RUNG-2 (so the physics is the same; only
# N/box/window shrink for cost).
SEED_AMP = 0.1
SEED_SIGMA = 2.0
SEED_LAM = 6.0
BULK_FRAC = 0.7
BULK_SIGMA = 2.5


def _alpha_free_provenance_gate() -> None:
    assert _avc.__file__.endswith("ave/core/constants.py"), "non-canonical constants"
    assert abs(ALPHA - 7.2973525693e-3) < 1e-12, "ALPHA not canonical"


def _ols_slope(t, y):
    """OLS slope of y vs t (the H-climb RATE = dH/dt) — byte-identical to the ladder."""
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
    """Build the RUNG-2 forced-overlap engine at a given dt with the co-located
    sub-yield bulk blob + ω-seed. coupling_support='saturated_interior',
    wall_off, projection ON — IDENTICAL to the ladder RUNG-2 _build_rung_engine.

    freeze_g=True: capture g=_front_window() at t0 (after seeding) and monkey-
    patch eng._front_window to return that frozen array — ġ≡0 thereafter. This
    is the ONLY difference between the two control branches."""
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
        # Capture the t0 window AFTER seeding (the live A_V at the seeded state),
        # then hold it. _front_window is referenced by _coupling_forces (f_V,f_ω),
        # _coupling_energy, and coupling_energy_box (the witness) — patching the
        # one method freezes g coherently across the force AND the energy ledger.
        g_frozen = np.asarray(eng._front_window()).copy()
        eng._front_window = types.MethodType(lambda self: g_frozen, eng)
        eng._g_frozen_t0 = g_frozen           # stash for the cheat-check / audit
    return eng


def _record(eng, box, dt, coupled, cheat_check=False):
    """Advance over T_WIN, record box-H(t). When cheat_check, ALSO record the
    coupling-force magnitudes (f_V max, f_ω max on alive interior) at each
    recorded step — the load-bearing check that frozen-g did NOT kill the
    coupling."""
    nsteps = int(np.ceil(T_WIN / dt))
    every = max(1, nsteps // 50)
    t_phys, H = [], []
    fV_hist, fw_hist, gmove_hist = [], [], []
    diverged = None
    H0_scale = abs(eng.H_witness_box(box)["H"]) + 1e-30
    alive_int = np.asarray(eng.B.mask_alive) & np.asarray(eng._interior)
    g_ref = np.asarray(eng._front_window()).copy() if cheat_check else None
    for s in range(nsteps + 1):
        if s > 0:
            if coupled:
                eng.step_coupled()
            else:
                eng.B.step(dt=dt)
        if s % every == 0 or s == nsteps:
            w = eng.H_witness_box(box)
            t_phys.append(s * dt)
            H.append(w["H"])
            if cheat_check and coupled:
                fV, fw = eng._coupling_forces()
                fV = np.asarray(fV)
                fw = np.asarray(fw)
                fwmag = np.sqrt((fw ** 2).sum(axis=-1))
                fV_hist.append(float(np.abs(fV[alive_int]).max()) if alive_int.any() else 0.0)
                fw_hist.append(float(fwmag[alive_int].max()) if alive_int.any() else 0.0)
                # g-drift vs t0 (0 ⇒ truly frozen; >0 ⇒ moving) — the ġ witness.
                g_now = np.asarray(eng._front_window())
                gmove_hist.append(float(np.abs(g_now - g_ref).max()))
            if not np.isfinite(w["H"]) or abs(w["H"]) > 1e6 * H0_scale:
                diverged = s
                break
    out = {"t": t_phys, "H": H, "nsteps": nsteps, "diverged": diverged}
    if cheat_check:
        out["fV_max_hist"] = fV_hist
        out["fw_max_hist"] = fw_hist
        out["g_drift_vs_t0_hist"] = gmove_hist
    return out


def _climb_rate(tr):
    """OLS climb-rate dH/dt of a box-H trajectory + H0."""
    H = np.asarray(tr["H"], dtype=float)
    t = np.asarray(tr["t"], dtype=float)
    H0 = float(H[0]) if H.size else 0.0
    return _ols_slope(t, H), H0


def _run_branch(label, freeze_g, box, dt_base):
    """Run the RUNG-2 dt-sweep for ONE branch (moving-g or frozen-g). At each dt:
    coupling-ON climb-rate, coupling-OFF climb-rate (same seed), and the EXCESS
    (ON−OFF) = the pure coupling pump. Then dt→0 (Richardson + OLS) on the EXCESS,
    reproducing the ladder's R∞/R0 read EXACTLY (same estimators, same threshold)."""
    print(f"\n[{label}] freeze_g={freeze_g}  coupling_support=saturated_interior  "
          f"N={N} box_half={H_BOX} T_win={T_WIN}")
    dts = [dt_base / (2.0 ** k) for k in range(N_DT)]
    sweep = []
    cheat = {"fV_max_window": [], "fw_max_window": [], "g_max_drift_window": []}
    for k, dt in enumerate(dts):
        eng_on = _build_rung2_engine(couple_on=True, dt=dt, freeze_g=freeze_g)
        # t0 coupling-force probe (the overlap + the cheat-check seed values).
        fV0, fw0 = eng_on._coupling_forces()
        fV0 = np.asarray(fV0); fw0 = np.asarray(fw0)
        fwmag0 = np.sqrt((fw0 ** 2).sum(axis=-1))
        alive_int = np.asarray(eng_on.B.mask_alive) & np.asarray(eng_on._interior)
        fV0_max = float(np.abs(fV0[alive_int]).max()) if alive_int.any() else 0.0
        fw0_max = float(fwmag0[alive_int].max()) if alive_int.any() else 0.0
        ov = int(eng_on.coupling_support_overlap()["overlap_cells_tetrahedral"])
        # cheat-check + g-drift tracking only on the COARSEST dt (cheap, sufficient).
        do_cheat = (k == 0)
        tr_on = _record(eng_on, box, dt, coupled=True, cheat_check=do_cheat)
        rate_on, H0 = _climb_rate(tr_on)
        # COUPLE-OFF control (same bulk+ω seed; freeze_g irrelevant when couple_off,
        # but build identically so the seed/grid are byte-equal).
        eng_off = _build_rung2_engine(couple_on=False, dt=dt, freeze_g=freeze_g)
        tr_off = _record(eng_off, box, dt, coupled=False)
        rate_off, _ = _climb_rate(tr_off)
        rate_excess = float(rate_on - rate_off)
        if do_cheat:
            cheat["fV_max_window"] = tr_on["fV_max_hist"]
            cheat["fw_max_window"] = tr_on["fw_max_hist"]
            cheat["g_max_drift_window"] = tr_on["g_drift_vs_t0_hist"]
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
              f"f_V0={fV0_max:.3e} f_ω0={fw0_max:.3e} overlap={ov}  div={tr_on['diverged']}")

    # ── dt→0 extrapolation on the EXCESS — EXACTLY the ladder's estimators ──
    dts_arr = np.array([r["dt"] for r in sweep])
    rates = np.array([r["climb_rate_excess_on_minus_off"] for r in sweep])
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
    R_inf = R_inf_rich
    ratio_inf = abs(R_inf) / max(abs(R0), 1e-30)
    abs_rates = np.abs(rates)
    monotone_decr = bool(np.all(np.diff(abs_rates) <= 1e-30 * max(abs(R0), 1e-30) + 1e-15) or
                         np.all(np.diff(abs_rates) < 0))
    delta = abs(R_inf_rich - R_inf_ols)

    # cheat-check verdict for THIS branch: did the coupling still fire over the window?
    fV_w = cheat["fV_max_window"]
    fw_w = cheat["fw_max_window"]
    g_w = cheat["g_max_drift_window"]
    fV_min_over_window = float(min(fV_w)) if fV_w else 0.0
    fw_min_over_window = float(min(fw_w)) if fw_w else 0.0
    coupling_fires = bool(fV_min_over_window > 1e-12 and fw_min_over_window > 1e-12)
    g_max_drift = float(max(g_w)) if g_w else 0.0

    print(f"  → dt→0 EXCESS: R0={R0:+.5e}  R∞(Rich)={R_inf_rich:+.5e}  R∞(OLS)={R_inf_ols:+.5e}  "
          f"|R∞|/|R0|={ratio_inf:.4f}  monotone↓={monotone_decr}")
    print(f"  → cheat-check: f_V min-over-window={fV_min_over_window:.3e}  "
          f"f_ω min-over-window={fw_min_over_window:.3e}  coupling_fires={coupling_fires}  "
          f"g_max_drift_vs_t0={g_max_drift:.3e}")
    return {
        "label": label, "freeze_g": freeze_g,
        "dt_grid": dts,
        "sweep": sweep,
        "climb_rates_excess": rates.tolist(),
        "R0": R0,
        "R_inf_richardson": R_inf_rich, "R_inf_ols": R_inf_ols, "R_inf": R_inf,
        "ratio_R_inf_over_R0": ratio_inf,
        "abs_rates_monotone_decreasing": monotone_decr,
        "extrapolation_uncertainty_delta": delta,
        "cheat_check": {
            "fV_max_over_window": fV_w, "fw_max_over_window": fw_w,
            "g_max_drift_over_window": g_w,
            "fV_min_over_window": fV_min_over_window,
            "fw_min_over_window": fw_min_over_window,
            "g_max_drift": g_max_drift,
            "coupling_still_fires": coupling_fires,
        },
    }


def main() -> dict:
    _alpha_free_provenance_gate()
    print("=" * 80)
    print("KEYSTONE FREEZE-G CONTROL — RUNG-2 forced-overlap: ġ≠0 (moving) vs ġ≡0 (frozen)")
    print("=" * 80)

    ref = A1CosseratMovingWallEngine(N=N, dx=DX, pml_thickness=PML,
                                     couple_on=False, wall_on=False, project_alive=False)
    dt_base = float(ref.dt)
    box = ref.make_box_mask((CENTER, CENTER, CENTER), H_BOX)
    box_idx = np.argwhere(box)
    guard = CENTER - H_BOX
    print(f"N={N} dx={DX} PML={PML} | B_int=[{box_idx.min(0)}..{box_idx.max(0)}] "
          f"({int(box.sum())} cells) | guard={guard:.0f} | dt_base={dt_base:.5e}")

    moving = _run_branch("MOVING-g (ġ≠0, ladder default)", freeze_g=False, box=box, dt_base=dt_base)
    frozen = _run_branch("FROZEN-g (ġ≡0, the control)", freeze_g=True, box=box, dt_base=dt_base)

    # ── THE DECISIVE READ ──
    ratio_moving = moving["ratio_R_inf_over_R0"]
    ratio_frozen = frozen["ratio_R_inf_over_R0"]
    THRESH = 0.10                                  # the ladder's plateau threshold
    plateau_moving = bool(ratio_moving >= THRESH)
    plateau_frozen = bool(ratio_frozen >= THRESH)
    plateau_vanishes = bool(plateau_moving and not plateau_frozen)
    coupling_fires_frozen = bool(frozen["cheat_check"]["coupling_still_fires"])
    # relative collapse of the frozen plateau vs the moving plateau (the magnitude
    # of the residual-removal): how much of the moving R∞ survives freezing g?
    surviving_frac = (abs(frozen["R_inf"]) / max(abs(moving["R_inf"]), 1e-30))

    if not coupling_fires_frozen:
        verdict = "FREEZE-G-CONFOUNDED"
        reason = (
            "Freezing g KILLED the coupling under frozen-g (f_V or f_ω → 0 over the "
            "window) — the vanished/changed plateau is meaningless (the coupling was "
            "removed, not the ġVΞ residual). The control cannot decide the fork; "
            "needs a coupling-preserving freeze.")
    elif plateau_vanishes:
        verdict = "WINDOW-MODEL-PUMP-FIXABLE"
        reason = (
            f"With the coupling STILL FIRING under frozen-g (f_V,f_ω nonzero on alive "
            f"cells over the window), the EXCESS plateau VANISHES when ġ≡0 "
            f"(|R∞|/|R0|: moving {ratio_moving:.4f} ≥ {THRESH} → frozen {ratio_frozen:.4f} "
            f"< {THRESH}). The RUNG-2 pump WAS the moving-window residual R=κ̃∫ġ·V·Ξ "
            f"(the dropped ∂g/∂V term), NOT a substrate pump. The keystone RE-OPENS: "
            f"a variationally-consistent coupling (g a fixed external weight, or the "
            f"∂g/∂V term restored) closes the loop. Banked SUBSTRATE-PUMP is the "
            f"window-model artifact, not the substrate.")
    else:
        verdict = "SUBSTRATE-PUMP-CONFIRMED"
        reason = (
            f"The EXCESS plateau PERSISTS under ġ≡0 (frozen |R∞|/|R0|={ratio_frozen:.4f} "
            f"≥ {THRESH}; {surviving_frac*100:.0f}% of the moving R∞ survives freezing g) "
            f"with the coupling still firing. The RUNG-2 pump is NOT the moving-window "
            f"residual — freezing g (removing ġVΞ) does NOT remove the plateau. The "
            f"keystone is NEGATIVE: the substrate will not losslessly close the "
            f"energize-LOCK loop even with a variationally-consistent (frozen-g) coupling.")

    result = {
        "control": "keystone FREEZE-G — RUNG-2 forced-overlap ġ≠0 vs ġ≡0",
        "purpose": "decide RUNG-2 SUBSTRATE-PUMP vs WINDOW-MODEL-PUMP (PIECE-1 ġVΞ residual)",
        "banked_rung2": {"commit": "4a90944c", "verdict": "SUBSTRATE-PUMP",
                         "ratio_R_inf_over_R0": 0.8419372278075833,
                         "N": 32, "H_box": 8, "T_win": 4.0},
        "config": {"N": N, "dx": DX, "pml": PML, "H_box": H_BOX, "T_win": T_WIN,
                   "n_dt": N_DT, "dt_base": dt_base,
                   "coupling_support": "saturated_interior", "wall_on": False,
                   "box_cells": int(box.sum())},
        "alpha_free": True,
        "threshold": THRESH,
        "moving_g": moving,
        "frozen_g": frozen,
        "decisive_read": {
            "ratio_moving": ratio_moving, "ratio_frozen": ratio_frozen,
            "plateau_moving": plateau_moving, "plateau_frozen": plateau_frozen,
            "plateau_vanishes_under_frozen_g": plateau_vanishes,
            "coupling_still_fires_under_frozen_g": coupling_fires_frozen,
            "frozen_R_inf_surviving_frac_of_moving": surviving_frac,
        },
        "verdict": verdict,
        "verdict_reason": reason,
    }

    print("\n" + "=" * 80)
    print(f"MOVING-g  R∞/R0 = {ratio_moving:.4f}   (plateau={plateau_moving})")
    print(f"FROZEN-g  R∞/R0 = {ratio_frozen:.4f}   (plateau={plateau_frozen})")
    print(f"coupling still fires under frozen-g: {coupling_fires_frozen}")
    print(f"plateau vanishes under frozen-g:     {plateau_vanishes}")
    print(f"\nVERDICT: {verdict}")
    print(f"  {reason}")
    print("=" * 80)

    out_path = os.path.join(HERE, "keystone_freezeg_control_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2, default=float)
    result["results_json"] = out_path
    print(f"results → {out_path}")
    return result


if __name__ == "__main__":
    main()

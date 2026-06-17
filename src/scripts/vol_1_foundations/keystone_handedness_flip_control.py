"""Keystone HANDEDNESS FLIP-TEST — is the RUNG-2 pump chirality-selective?

PHYSICAL QUESTION (Grant's): the K4 lattice is chiral, and the energize-LOCK
coupling H_c = κ̃∫ g·V·Ξ, Ξ = (∇×ω)·ẑ is built on a CURL — which carries a
handedness. Does the observed RUNG-2 EXCESS energy pump PERSIST symmetrically
under flipping the ω-seed's handedness relative to the fixed lattice?

  * SYMMETRIC  (both signs pump positive, similar magnitude / plateau ratio)
      → the pump is REFERENCE-INDEPENDENT → keystone-negative is handedness-
        robust; candidate-(c) (the pump is a chirality-reference artifact, the
        keystone-negative was run on the wrong hand) does NOT rescue it.
  * ASYMMETRIC (one handedness pumps positive, the opposite closes / damps /
      flips sign)
      → HANDEDNESS-SELECTIVE → the "pump" is a chirality-reference artifact →
        candidate-(c) CONFIRMED, the keystone RE-OPENS on the closing hand.

THE HANDEDNESS KNOB (identified, single + clean):
  keystone_freezeg_control.py:112 seeds
    eng.seed_cosserat_photon(..., helicity=1.0, axis=2)
  → cosserat_field_3d.py:2088 (initialize_gaussian_wavepacket_omega): when
    helicity != 0 a quadrature ω component is added along ê_perp = d̂ × ê_axis,
    90° out of phase, giving a corkscrew with nonzero Beltrami helicity h. The
    SIGN of helicity sets the winding handedness (e⁻ vs e⁺; docstring :2050-56).
  This winding feeds Ξ = (∇×ω)·ẑ (_cosserat_axial_curl_tet), which enters BOTH
  the coupling force f_V = −κ̃ g Ξ AND the witness energy H_c = κ̃∫ g V Ξ.
  FLIP: helicity = +1.0 (AS-IS, the banked hand) ↔ −1.0 (FLIPPED hand). One
  knob, substrate-native (the Cosserat micro-rotation winding sign = charge-"3").

THE CONTROL QUANTITY (NOT a keystone adjudication — a control read):
  the moving-g (ġ≠0, the LADDER DEFAULT) RUNG-2 forced-overlap dt→0 EXCESS
  (ON−OFF) H-climb-rate plateau, for helicity=+1 and helicity=−1. We DO NOT run
  the freeze-g branch here — the freeze-g control already banked SUBSTRATE-PUMP;
  this asks the orthogonal chirality question on the SAME moving-g pump the
  ladder measured. The estimators (OLS climb-rate, Richardson dt→0, R∞/R0) are
  byte-identical to keystone_freezeg_control.py so the +/− reads are directly
  comparable to the banked moving-g plateau.

α-FREE: wall_on=False; no ALPHA/KAPPA in the update path (inherited config).

Run:  PYTHONPATH=src ./.venv/bin/python \
        src/scripts/vol_1_foundations/keystone_handedness_flip_control.py
Env overrides: KF_N (default 20), KF_TWIN (default 2.0), KF_H (default 6),
  KF_NDT (default 4). To escalate to N=32: KF_N=32 KF_H=8 KF_TWIN=4.0.
"""
from __future__ import annotations

import json
import os

import numpy as np

import ave.core.constants as _avc
from ave.core.constants import ALPHA
from ave.core.a1_cosserat_moving_wall_engine import A1CosseratMovingWallEngine

HERE = os.path.dirname(os.path.abspath(__file__))

# ── geometry / sweep config — IDENTICAL knobs to keystone_freezeg_control.py ──
N = int(os.environ.get("KF_N", "20"))
DX = 1.0
PML = 0
CENTER = N / 2.0
H_BOX = int(os.environ.get("KF_H", "6"))
T_WIN = float(os.environ.get("KF_TWIN", "2.0"))
N_DT = int(os.environ.get("KF_NDT", "4"))

# Seed params — IDENTICAL to the ladder / freeze-g RUNG-2 (only helicity flips).
SEED_AMP = 0.1
SEED_SIGMA = 2.0
SEED_LAM = 6.0
BULK_FRAC = 0.7
BULK_SIGMA = 2.5


def _alpha_free_provenance_gate() -> None:
    assert _avc.__file__.endswith("ave/core/constants.py"), "non-canonical constants"
    assert abs(ALPHA - 7.2973525693e-3) < 1e-12, "ALPHA not canonical"


def _ols_slope(t, y):
    """OLS slope of y vs t (the H-climb RATE) — byte-identical to the ladder."""
    t = np.asarray(t, dtype=float)
    y = np.asarray(y, dtype=float)
    if t.size < 2:
        return 0.0
    tm, ym = t.mean(), y.mean()
    denom = float(((t - tm) ** 2).sum())
    if denom < 1e-30:
        return 0.0
    return float(((t - tm) * (y - ym)).sum() / denom)


def _build_rung2_engine(couple_on, dt, helicity):
    """RUNG-2 forced-overlap engine (saturated_interior, wall_off, projection ON)
    with the co-located sub-yield bulk blob + ω-seed — IDENTICAL to the ladder /
    freeze-g RUNG-2 builder EXCEPT the seed's `helicity` sign (the handedness
    knob under test). MOVING-g (ġ≠0, the ladder default): _front_window is NOT
    frozen here, so this is the same pump the banked moving-g plateau measured."""
    eng = A1CosseratMovingWallEngine(
        N=N, dx=DX, pml_thickness=PML, couple_on=couple_on, wall_on=False,
        coupling_support="saturated_interior", project_alive=True,
    )
    eng.seed_bulk_blob(center=(CENTER, CENTER, CENTER), sigma=BULK_SIGMA, frac=BULK_FRAC)
    eng.seed_cosserat_photon(
        center=(CENTER, CENTER, CENTER), sigma=SEED_SIGMA, wavelength=SEED_LAM,
        amplitude=SEED_AMP, direction=(1, 0, 0), helicity=float(helicity), axis=2,
    )
    if abs(dt - eng.dt) > 1e-30:
        eng.dt = float(dt)
        eng.A.dt = float(dt)
        c_omega_max = eng.c0 / np.sqrt(eng.cL2_over_cT2 * eng.A.S_min)
        dt_cos = 0.30 * eng.dx / (c_omega_max * np.sqrt(3.0))
        eng.n_sub_cos = max(1, int(np.ceil(eng.dt / max(dt_cos, 1e-30))))
        eng.dt_sub_cos = eng.dt / eng.n_sub_cos
    return eng


def _record(eng, box, dt, coupled, fire_check=False):
    """Advance over T_WIN, record box-H(t). When fire_check, ALSO record the
    coupling-force magnitudes (f_V, f_ω max on alive interior) at each step — the
    load-bearing 'coupling fires on this hand' check (f_V, f_ω nonzero)."""
    nsteps = int(np.ceil(T_WIN / dt))
    every = max(1, nsteps // 50)
    t_phys, H = [], []
    fV_hist, fw_hist = [], []
    diverged = None
    H0_scale = abs(eng.H_witness_box(box)["H"]) + 1e-30
    alive_int = np.asarray(eng.B.mask_alive) & np.asarray(eng._interior)
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
            if fire_check and coupled:
                fV, fw = eng._coupling_forces()
                fV = np.asarray(fV)
                fw = np.asarray(fw)
                fwmag = np.sqrt((fw ** 2).sum(axis=-1))
                fV_hist.append(float(np.abs(fV[alive_int]).max()) if alive_int.any() else 0.0)
                fw_hist.append(float(fwmag[alive_int].max()) if alive_int.any() else 0.0)
            if not np.isfinite(w["H"]) or abs(w["H"]) > 1e6 * H0_scale:
                diverged = s
                break
    out = {"t": t_phys, "H": H, "nsteps": nsteps, "diverged": diverged}
    if fire_check:
        out["fV_max_hist"] = fV_hist
        out["fw_max_hist"] = fw_hist
    return out


def _climb_rate(tr):
    H = np.asarray(tr["H"], dtype=float)
    t = np.asarray(tr["t"], dtype=float)
    H0 = float(H[0]) if H.size else 0.0
    return _ols_slope(t, H), H0


def _run_branch(label, helicity, box, dt_base):
    """Run the RUNG-2 moving-g dt-sweep for ONE handedness. At each dt: ON
    climb-rate, OFF climb-rate (same seed/hand), EXCESS (ON−OFF) = pure coupling
    pump. Then dt→0 (Richardson + OLS) on the EXCESS — EXACTLY the ladder /
    freeze-g estimators, so the +/− reads compare to the banked moving-g plateau."""
    sign = "+" if helicity >= 0 else "−"
    print(f"\n[{label}] helicity={helicity:+.1f} ({sign})  coupling_support=saturated_interior  "
          f"N={N} box_half={H_BOX} T_win={T_WIN}")
    dts = [dt_base / (2.0 ** k) for k in range(N_DT)]
    sweep = []
    fire = {"fV_max_window": [], "fw_max_window": []}
    for k, dt in enumerate(dts):
        eng_on = _build_rung2_engine(couple_on=True, dt=dt, helicity=helicity)
        fV0, fw0 = eng_on._coupling_forces()
        fV0 = np.asarray(fV0); fw0 = np.asarray(fw0)
        fwmag0 = np.sqrt((fw0 ** 2).sum(axis=-1))
        alive_int = np.asarray(eng_on.B.mask_alive) & np.asarray(eng_on._interior)
        fV0_max = float(np.abs(fV0[alive_int]).max()) if alive_int.any() else 0.0
        fw0_max = float(fwmag0[alive_int].max()) if alive_int.any() else 0.0
        ov = int(eng_on.coupling_support_overlap()["overlap_cells_tetrahedral"])
        do_fire = (k == 0)
        tr_on = _record(eng_on, box, dt, coupled=True, fire_check=do_fire)
        rate_on, H0 = _climb_rate(tr_on)
        eng_off = _build_rung2_engine(couple_on=False, dt=dt, helicity=helicity)
        tr_off = _record(eng_off, box, dt, coupled=False)
        rate_off, _ = _climb_rate(tr_off)
        rate_excess = float(rate_on - rate_off)
        if do_fire:
            fire["fV_max_window"] = tr_on["fV_max_hist"]
            fire["fw_max_window"] = tr_on["fw_max_hist"]
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

    # SIGN of the EXCESS pump (is energy INJECTED — positive climb — on this hand?)
    excess_sign = "POSITIVE(inject)" if R_inf > 0 else ("NEGATIVE(damp)" if R_inf < 0 else "ZERO")
    R0_sign = "POSITIVE(inject)" if R0 > 0 else ("NEGATIVE(damp)" if R0 < 0 else "ZERO")

    fV_w = fire["fV_max_window"]
    fw_w = fire["fw_max_window"]
    fV_min = float(min(fV_w)) if fV_w else 0.0
    fw_min = float(min(fw_w)) if fw_w else 0.0
    coupling_fires = bool(fV_min > 1e-12 and fw_min > 1e-12)
    overlap_cells = int(sweep[0]["overlap_cells_tetrahedral"]) if sweep else 0

    print(f"  → dt→0 EXCESS: R0={R0:+.5e} ({R0_sign})  R∞(Rich)={R_inf_rich:+.5e} ({excess_sign})  "
          f"R∞(OLS)={R_inf_ols:+.5e}  |R∞|/|R0|={ratio_inf:.4f}  monotone↓={monotone_decr}")
    print(f"  → fire-check: f_V min-over-window={fV_min:.3e}  f_ω min-over-window={fw_min:.3e}  "
          f"coupling_fires={coupling_fires}  overlap_cells={overlap_cells}")
    return {
        "label": label, "helicity": float(helicity), "sign": sign,
        "dt_grid": dts,
        "sweep": sweep,
        "climb_rates_excess": rates.tolist(),
        "R0": R0, "R0_sign": R0_sign,
        "R_inf_richardson": R_inf_rich, "R_inf_ols": R_inf_ols, "R_inf": R_inf,
        "excess_sign": excess_sign,
        "ratio_R_inf_over_R0": ratio_inf,
        "abs_rates_monotone_decreasing": monotone_decr,
        "extrapolation_uncertainty_delta": delta,
        "fire_check": {
            "fV_max_over_window": fV_w, "fw_max_over_window": fw_w,
            "fV_min_over_window": fV_min, "fw_min_over_window": fw_min,
            "coupling_fires": coupling_fires,
        },
        "overlap_cells": overlap_cells,
    }


def main() -> dict:
    _alpha_free_provenance_gate()
    print("=" * 80)
    print("KEYSTONE HANDEDNESS FLIP-TEST — RUNG-2 moving-g EXCESS: helicity +1 vs −1")
    print("=" * 80)

    ref = A1CosseratMovingWallEngine(N=N, dx=DX, pml_thickness=PML,
                                     couple_on=False, wall_on=False, project_alive=False)
    dt_base = float(ref.dt)
    box = ref.make_box_mask((CENTER, CENTER, CENTER), H_BOX)
    box_idx = np.argwhere(box)
    guard = CENTER - H_BOX
    print(f"N={N} dx={DX} PML={PML} | B_int=[{box_idx.min(0)}..{box_idx.max(0)}] "
          f"({int(box.sum())} cells) | guard={guard:.0f} | dt_base={dt_base:.5e}")

    plus = _run_branch("PLUS-hand (helicity=+1, AS-IS banked)", helicity=+1.0, box=box, dt_base=dt_base)
    minus = _run_branch("MINUS-hand (helicity=−1, FLIPPED)", helicity=-1.0, box=box, dt_base=dt_base)

    # ── THE DECISIVE READ (default-NEGATIVE = real leak = SYMMETRIC) ──
    THRESH = 0.10                                  # the ladder's plateau threshold
    rp, rm = plus["ratio_R_inf_over_R0"], minus["ratio_R_inf_over_R0"]
    Rp, Rm = plus["R_inf"], minus["R_inf"]
    plateau_plus = bool(rp >= THRESH)
    plateau_minus = bool(rm >= THRESH)
    same_sign = bool((Rp > 0) == (Rm > 0)) and Rp != 0 and Rm != 0
    fires_plus = bool(plus["fire_check"]["coupling_fires"])
    fires_minus = bool(minus["fire_check"]["coupling_fires"])
    # magnitude similarity of the two R∞ (1.0 = identical; near 0 = one collapsed)
    mag_ratio = min(abs(Rp), abs(Rm)) / max(abs(Rp), abs(Rm), 1e-30)

    # SYMMETRIC = both pump (plateau both), same sign, similar magnitude.
    symmetric = bool(plateau_plus and plateau_minus and same_sign and mag_ratio >= 0.5)

    if symmetric:
        verdict = "SYMMETRIC — REFERENCE-INDEPENDENT"
        reason = (
            f"Both handednesses PUMP with the SAME sign ({plus['excess_sign']}) and similar "
            f"magnitude (|R∞|: +{Rp:+.4e} / −{Rm:+.4e}, min/max={mag_ratio:.3f}) and similar "
            f"plateau ratio (+{rp:.4f} / −{rm:.4f}, thresh={THRESH}). The RUNG-2 EXCESS pump "
            f"PERSISTS under flipping the ω-seed handedness relative to the fixed K4 lattice — "
            f"it is REFERENCE-INDEPENDENT. The keystone-negative is HANDEDNESS-ROBUST: "
            f"candidate-(c) (the pump is a chirality-reference artifact / wrong hand) does NOT "
            f"rescue it.")
    elif same_sign and plateau_plus and plateau_minus and mag_ratio < 0.5:
        verdict = "PARTIALLY-ASYMMETRIC — same sign, magnitude split"
        reason = (
            f"Both hands plateau with the SAME sign ({plus['excess_sign']}) BUT the magnitudes "
            f"split (|R∞|: +{Rp:+.4e} / −{Rm:+.4e}, min/max={mag_ratio:.3f} < 0.5). The pump "
            f"does not vanish on either hand (no sign flip / no plateau collapse), so candidate-"
            f"(c) is NOT cleanly confirmed — but the chirality DOES modulate the pump strength. "
            f"Escalate to N=32 to see whether the split widens to a sign flip / plateau collapse "
            f"(true ASYMMETRIC) or narrows toward SYMMETRIC at the banked resolution.")
    else:
        verdict = "ASYMMETRIC — HANDEDNESS-SELECTIVE"
        # name which hand pumps and which closes/damps
        pumps_plus = bool(plateau_plus and Rp > 0)
        pumps_minus = bool(plateau_minus and Rm > 0)
        closing_hand = ("−" if (pumps_plus and not pumps_minus) else
                        ("+" if (pumps_minus and not pumps_plus) else "ambiguous"))
        reason = (
            f"The two handednesses are NOT symmetric: PLUS R∞={Rp:+.4e} ({plus['excess_sign']}, "
            f"plateau={rp:.4f}) vs MINUS R∞={Rm:+.4e} ({minus['excess_sign']}, plateau={rm:.4f}); "
            f"same_sign={same_sign}, min/max-magnitude={mag_ratio:.3f}. One handedness pumps "
            f"positive while the opposite closes / damps / flips sign → the 'pump' is a CHIRALITY-"
            f"REFERENCE ARTIFACT. Candidate-(c) CONFIRMED: the keystone RE-OPENS on the closing "
            f"hand ({closing_hand}). ESCALATE to N=32 (KF_N=32 KF_H=8 KF_TWIN=4.0) to confirm "
            f"at the banked resolution.")

    result = {
        "control": "keystone HANDEDNESS FLIP-TEST — RUNG-2 moving-g EXCESS, helicity +1 vs −1",
        "physical_question": ("does the RUNG-2 EXCESS pump persist symmetrically under flipping "
                              "the ω-seed handedness vs the fixed chiral K4 lattice (ref-indep, "
                              "real leak) or is it handedness-selective (chirality-ref artifact)?"),
        "handedness_knob": ("seed_cosserat_photon(helicity=±1) → "
                            "cosserat_field_3d.py:2088 quadrature ω along d̂×ê_axis; sign sets "
                            "winding handedness (e⁻ vs e⁺); feeds Ξ=(∇×ω)·ẑ in f_V & H_c"),
        "banked_rung2_moving_g": {"commit": "4a90944c", "verdict": "SUBSTRATE-PUMP",
                                  "ratio_R_inf_over_R0": 0.8419372278075833,
                                  "N": 32, "H_box": 8, "T_win": 4.0, "helicity": 1.0},
        "config": {"N": N, "dx": DX, "pml": PML, "H_box": H_BOX, "T_win": T_WIN,
                   "n_dt": N_DT, "dt_base": dt_base,
                   "coupling_support": "saturated_interior", "wall_on": False,
                   "moving_g": True, "box_cells": int(box.sum())},
        "alpha_free": True,
        "threshold": THRESH,
        "plus_hand": plus,
        "minus_hand": minus,
        "decisive_read": {
            "ratio_plus": rp, "ratio_minus": rm,
            "R_inf_plus": Rp, "R_inf_minus": Rm,
            "excess_sign_plus": plus["excess_sign"], "excess_sign_minus": minus["excess_sign"],
            "plateau_plus": plateau_plus, "plateau_minus": plateau_minus,
            "same_sign": same_sign, "magnitude_min_over_max": mag_ratio,
            "coupling_fires_plus": fires_plus, "coupling_fires_minus": fires_minus,
            "overlap_cells_plus": plus["overlap_cells"], "overlap_cells_minus": minus["overlap_cells"],
            "symmetric": symmetric,
        },
        "verdict": verdict,
        "verdict_reason": reason,
    }

    print("\n" + "=" * 80)
    print(f"PLUS-hand  (+1)  R∞/R0 = {rp:.4f}  R∞={Rp:+.5e}  ({plus['excess_sign']})  "
          f"fires={fires_plus}  overlap={plus['overlap_cells']}")
    print(f"MINUS-hand (−1)  R∞/R0 = {rm:.4f}  R∞={Rm:+.5e}  ({minus['excess_sign']})  "
          f"fires={fires_minus}  overlap={minus['overlap_cells']}")
    print(f"same_sign={same_sign}  magnitude min/max={mag_ratio:.3f}  symmetric={symmetric}")
    print(f"\nVERDICT: {verdict}")
    print(f"  {reason}")
    print("=" * 80)

    out_path = os.path.join(HERE, "keystone_handedness_flip_results.json")
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2, default=float)
    result["results_json"] = out_path
    print(f"results → {out_path}")
    return result


if __name__ == "__main__":
    main()

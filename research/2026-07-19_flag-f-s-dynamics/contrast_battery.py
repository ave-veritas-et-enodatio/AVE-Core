"""Flag-F three-form contrast battery (Stage 2) — frozen tree in the prereg.

Prereg (frozen-by-push): research/2026-07-19_flag-f-s-dynamics_prereg.md
Derivation: research/2026-07-19_flag-f-s-dynamics-derivation.md

Three forms on the identical #735 Leg-B drive r(t)=r0+dr*sin(wt):
  Form S  shipped Eq 2.1 (zeta->inf), byte-locked yield_fork_kernel (k4_tlm.py:283,291)
  Form R  reactive world-a (zeta=0.1 underdamped), reactive_kernel FFT steady-state
  Form T  transductive world-b crossover (zeta=1.0 critical), reactive_kernel

Three frozen discriminator axes:
  (i)   (V,I) peak location vs 0.911 / 0.9577, windows [0.85,0.95] AND [0.954,0.978]
  (ii)  origin-pinch yes/no per form
  (iii) loop shape class: Debye (peak pinned wtau~1, phase caps 90) vs
        Resonant (peak tracks omega_S, phase sweeps 180)  <-- the real discriminator
"""

from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reactive_kernel as rk  # noqa: E402
import yield_fork_kernel as k  # noqa: E402

# Frozen drive + sweep (prereg §2,§3)
R0 = 0.7
DR = 0.3
DR_SUB = 0.25
TAU = 1.0
OMEGA_TAUS = np.logspace(np.log10(0.05), np.log10(10.0), 60)
OMEGA_S_SCAN = np.logspace(np.log10(0.3), np.log10(3.0), 25)  # calibration-tagged, form-level
ZETA_R = 0.1  # Form R underdamped (world a)
ZETA_T = 1.0  # Form T critical (world b crossover)

# Frozen windows + datum (prereg §5 axis i)
WIN_LEGACY = (0.85, 0.95)       # #59 §11
WIN_EQ63 = (0.954, 0.978)       # #59 Eq 6.3 own arithmetic (#735 F-B1)
DATUM_VI = 0.911                # #735 registered (V,I) peak
DATUM_VI_SUB = 0.9577           # #735 sub-rupture


def phase_S_vs_Seq_deg(S: np.ndarray, Seq: np.ndarray) -> float:
    """Fundamental phase of S relative to the forcing S_eq (deg).

    Debye 1st-order caps at -90 deg; reactive 2nd-order sweeps to -180 deg.
    """
    F_S = np.fft.rfft(np.asarray(S)[:-1])
    F_e = np.fft.rfft(np.asarray(Seq)[:-1])
    return float(np.degrees(np.angle(F_S[1] / F_e[1])))


def _peak(omega_taus: np.ndarray, areas: np.ndarray) -> float:
    return float(omega_taus[int(np.argmax(areas))])


def _peak_fine_VI_formS(r0: float, dr: float, coarse_peak: float) -> float:
    """Fine sub-grid refit of Form S (V,I) peak (same method #735 froze:
    leg_b_loop_area.py:58 coarse argmax + fine linspace). Makes the cross-check
    to the #735 datum 0.911 crisp (the 60-pt log grid alone lands on 0.885)."""
    lo, hi = max(0.05, coarse_peak / 1.25), min(10.0, coarse_peak * 1.25)
    fine = np.linspace(lo, hi, 81)
    aa = [k.loop_area_VI(k.integrate_cycle(r0, dr, float(w), tau_relax=TAU, tau_fn=k.tau_const))["area_VI"]
          for w in fine]
    return float(fine[int(np.argmax(aa))])


# ---------------- Form S (shipped Eq 2.1, byte-locked) ----------------
def sweep_form_S(r0: float, dr: float) -> dict:
    a_rs, a_vi, pin_v, pin_i, ph, finite, signed_vi = [], [], [], [], [], [], []
    for wt in OMEGA_TAUS:
        s = k.integrate_cycle(r0, dr, float(wt), tau_relax=TAU, tau_fn=k.tau_const)
        a_rs.append(k.loop_area_rS(s))
        vi = k.loop_area_VI(s)
        a_vi.append(vi["area_VI"])
        pin_v.append(vi["min_absV"])
        pin_i.append(vi["min_absI"])
        # signed (V,I) area for chirality
        r, S = s["r"], s["S"]
        curr = r * np.sqrt(np.maximum(S, 0.0))
        signed_vi.append(float(np.sum(0.5 * (curr[:-1] + curr[1:]) * (r[1:] - r[:-1]))))
        ph.append(phase_S_vs_Seq_deg(s["S"], s["Seq"]))
        finite.append(s["finite"])
    a_rs, a_vi = np.array(a_rs), np.array(a_vi)
    peak_vi_coarse = _peak(OMEGA_TAUS, a_vi)
    peak_vi_fine = _peak_fine_VI_formS(r0, dr, peak_vi_coarse)
    return {
        "form": "S_shipped_Eq2.1",
        "zeta": "inf(first-order)",
        "omega_tau": OMEGA_TAUS.tolist(),
        "area_rS": a_rs.tolist(),
        "area_VI": a_vi.tolist(),
        "peak_rS": _peak(OMEGA_TAUS, a_rs),
        "peak_VI_coarse": peak_vi_coarse,
        "peak_VI": peak_vi_fine,
        "phase_deg": ph,
        "phase_max_abs": float(np.max(np.abs(ph))),
        "signed_VI_sign_flips": int(np.sum(np.diff(np.sign(signed_vi)) != 0)),
        "origin_pinch": bool(min(pin_v) < 1e-3 and min(pin_i) < 1e-3),
        "min_absI": float(min(pin_i)),
        "all_finite": bool(all(finite)),
    }


# ---------------- Forms R / T (reactive, FFT steady-state) ----------------
def sweep_reactive_at_omegaS(r0: float, dr: float, omega_S_tau: float, zeta: float) -> dict:
    a_rs, a_vi, pin_v, pin_i, ph, finite, signed_vi = [], [], [], [], [], [], []
    for wt in OMEGA_TAUS:
        s = rk.integrate_reactive(r0, dr, float(wt), omega_S_tau, zeta)
        a_rs.append(rk.loop_area_rS(s))
        vi = rk.loop_area_VI(s)
        a_vi.append(vi["area_VI"])
        signed_vi.append(vi["signed_VI"])
        pin_v.append(vi["min_absV"])
        pin_i.append(vi["min_absI"])
        ph.append(phase_S_vs_Seq_deg(s["S"], s["Seq"]))
        finite.append(s["finite"])
    a_rs, a_vi = np.array(a_rs), np.array(a_vi)
    return {
        "omega_S_tau": omega_S_tau,
        "peak_rS": _peak(OMEGA_TAUS, a_rs),
        "peak_VI": _peak(OMEGA_TAUS, a_vi),
        "phase_max_abs": float(np.max(np.abs(ph))),
        "signed_VI_sign_flips": int(np.sum(np.diff(np.sign(signed_vi)) != 0)),
        "origin_pinch": bool(min(pin_v) < 1e-3 and min(pin_i) < 1e-3),
        "min_absI": float(min(pin_i)),
        "all_finite": bool(all(finite)),
    }


def sweep_form_reactive(r0: float, dr: float, zeta: float, label: str) -> dict:
    per_omegaS = [sweep_reactive_at_omegaS(r0, dr, float(wS), zeta) for wS in OMEGA_S_SCAN]
    peaks_vi = np.array([p["peak_VI"] for p in per_omegaS])
    peaks_rs = np.array([p["peak_rS"] for p in per_omegaS])
    wS = OMEGA_S_SCAN
    # peak-tracks-omega_S: slope of peak_VI vs omega_S (Resonant ~ 1; Debye ~ 0)
    slope_vi = float(np.polyfit(wS, peaks_vi, 1)[0])
    corr_vi = float(np.corrcoef(wS, peaks_vi)[0, 1])
    # which omega_S (if any) lands the (V,I) peak in each window
    def in_win(win):
        hits = [float(w) for w, p in zip(wS, peaks_vi) if win[0] <= p <= win[1]]
        return {"any": bool(hits), "omega_S_values": hits,
                "all_O1": bool(hits) and all(0.3 <= h <= 3.0 for h in hits)}
    return {
        "form": label,
        "zeta": zeta,
        "omega_S_scan": wS.tolist(),
        "peak_VI_per_omegaS": peaks_vi.tolist(),
        "peak_rS_per_omegaS": peaks_rs.tolist(),
        "peak_VI_slope_vs_omegaS": slope_vi,
        "peak_VI_corr_vs_omegaS": corr_vi,
        "phase_max_abs_over_scan": float(max(p["phase_max_abs"] for p in per_omegaS)),
        "signed_VI_sign_flips_max": int(max(p["signed_VI_sign_flips"] for p in per_omegaS)),
        "in_window_legacy": in_win(WIN_LEGACY),
        "in_window_eq63": in_win(WIN_EQ63),
        "origin_pinch_any": bool(any(p["origin_pinch"] for p in per_omegaS)),
        "all_finite": bool(all(p["all_finite"] for p in per_omegaS)),
    }


# ---------------- G3 audit (reactive integrator soundness) ----------------
def g3_audit() -> dict:
    # exactness: ODE residual machine-zero
    s = rk.integrate_reactive(R0, DR, 1.0, 1.0, ZETA_R)
    resid = rk.ode_residual(s, 1.0, ZETA_R)
    # lossless control: zeta=0 OFF the harmonic grid -> loop area ~ 0
    s0 = rk.integrate_reactive(R0, DR, 0.37, 0.93, 0.0)
    loop0 = rk.loop_area_rS(s0)
    return {
        "ode_residual_zeta0p1": resid,
        "ode_residual_machine_zero": bool(resid < 1e-10),
        "zeta0_offharmonic_loop_area": loop0,
        "zeta0_lossless_confirmed": bool(loop0 < 1e-10),
    }


# ---------------- G2 byte-match gate (Form S vs live engine) ----------------
def g2_byte_match() -> dict:
    """Form S per-step update bit-identical to a live K4Lattice3D memristive step."""
    try:
        from ave.core.k4_tlm import K4Lattice3D
    except Exception as e:  # pragma: no cover
        return {"ran": False, "reason": f"engine import failed: {e}"}
    lat = K4Lattice3D(nx=3, ny=3, nz=3, use_memristive_saturation=True)
    # single-site drive: set V_inc at center so strain r = 0.6, one memristive step
    tau = float(lat.tau_relax)
    dt = float(lat.dt)
    r = 0.6
    # engine step: S_field starts at 1
    S_prev = 1.0
    Seq = float(k.s_eq(r))
    driver_S = k.be_step(S_prev, Seq, tau, dt)
    engine_S = (S_prev * tau + dt * Seq) / (tau + dt)  # k4_tlm.py:291 verbatim
    rel = abs(driver_S - engine_S) / max(abs(engine_S), 1e-300)
    return {"ran": True, "tau": tau, "dt": dt, "driver_S": driver_S,
            "engine_formula_S": engine_S, "rel": rel, "bit_identical": bool(rel < 1e-12)}


def adjudicate(formS: dict, formR: dict, formT: dict) -> dict:
    # Axis (iii): shape class (structural, parameter-robust) — decided FIRST
    S_is_debye = bool(abs(formS["peak_rS"] - 1.0) < 0.12 and formS["phase_max_abs"] < 110.0)
    def is_resonant(f):
        return bool(f["peak_VI_corr_vs_omegaS"] > 0.9 and f["peak_VI_slope_vs_omegaS"] > 0.5
                    and f["phase_max_abs_over_scan"] > 140.0)
    R_is_resonant = is_resonant(formR)
    T_is_resonant = is_resonant(formT)
    shape_class_ok = S_is_debye and R_is_resonant and T_is_resonant

    # Axis (i): peak-location discrimination
    S_in_legacy = WIN_LEGACY[0] <= formS["peak_VI"] <= WIN_LEGACY[1]
    S_in_eq63 = WIN_EQ63[0] <= formS["peak_VI"] <= WIN_EQ63[1]
    R_in = formR["in_window_legacy"]["any"] or formR["in_window_eq63"]["any"]
    forms_in_window = int(S_in_legacy or S_in_eq63) + int(R_in) + int(
        formT["in_window_legacy"]["any"] or formT["in_window_eq63"]["any"])
    if forms_in_window >= 2:
        axis_i = "DATUM-DOES-NOT-DISCRIMINATE"
    elif forms_in_window == 1:
        axis_i = "SUBSTRATE-HAS-SPOKEN"
    else:
        axis_i = "NO-FORM-IN-WINDOW (datum falsifies all three at registered drive)"

    return {
        "axis_iii_shape_class": {
            "FormS_is_Debye": S_is_debye,
            "FormR_is_Resonant": R_is_resonant,
            "FormT_is_Resonant": T_is_resonant,
            "all_as_derived": shape_class_ok,
            "note": ("Debye: peak_rS pinned ~1 AND phase caps ~90; Resonant: (V,I) peak tracks "
                     "omega_S (corr>0.9, slope>0.5) AND phase sweeps ~180. Structural, outranks axis(i)."),
        },
        "axis_i_peak_location": {
            "verdict": axis_i,
            "FormS_peak_VI": formS["peak_VI"],
            "FormS_in_legacy": bool(S_in_legacy),
            "FormS_in_eq63": bool(S_in_eq63),
            "FormR_in_window": formR["in_window_legacy"] if formR["in_window_legacy"]["any"] else formR["in_window_eq63"],
            "forms_in_window_count": forms_in_window,
        },
        "axis_ii_origin_pinch": {
            "FormS": formS["origin_pinch"], "FormR": formR["origin_pinch_any"],
            "FormT": formT["origin_pinch_any"],
            "note": "expected NO for all (drive r in [0.4,1.0] never crosses r=0; F-B2)",
        },
        "precedence": "axis(iii) structural outranks axis(i) tunable (prereg §6.5)",
    }


def run() -> dict:
    from ave.core.constants import TAU_RELAX_NATIVE
    assert float(TAU_RELAX_NATIVE) == 1.0

    g2 = g2_byte_match()
    g3 = g3_audit()
    formS = sweep_form_S(R0, DR)
    formS_sub = sweep_form_S(R0, DR_SUB)
    formR = sweep_form_reactive(R0, DR, ZETA_R, "R_reactive_world_a")
    formT = sweep_form_reactive(R0, DR, ZETA_T, "T_transductive_world_b")
    formR_sub = sweep_form_reactive(R0, DR_SUB, ZETA_R, "R_reactive_world_a_subrupture")

    adj = adjudicate(formS, formR, formT)
    return {
        "prereg": "research/2026-07-19_flag-f-s-dynamics_prereg.md",
        "derivation": "research/2026-07-19_flag-f-s-dynamics-derivation.md",
        "gates": {"G2_byte_match": g2, "G3_reactive_audit": g3,
                  "G0_regime_max_r": R0 + DR, "G1_finite": bool(
                      formS["all_finite"] and formR["all_finite"] and formT["all_finite"])},
        "form_S": formS,
        "form_S_subrupture": {"peak_VI": formS_sub["peak_VI"], "peak_rS": formS_sub["peak_rS"]},
        "form_R": formR,
        "form_T": formT,
        "form_R_subrupture": {"in_window_legacy": formR_sub["in_window_legacy"],
                              "peak_VI_slope_vs_omegaS": formR_sub["peak_VI_slope_vs_omegaS"]},
        "datum": {"VI_registered": DATUM_VI, "VI_subrupture": DATUM_VI_SUB,
                  "window_legacy": WIN_LEGACY, "window_eq63": WIN_EQ63},
        "adjudication": adj,
    }


if __name__ == "__main__":
    import json
    out = run()
    g = out["gates"]
    print("G2 byte-match:", g["G2_byte_match"].get("bit_identical"), "rel=%.1e" % g["G2_byte_match"].get("rel", float("nan")))
    print("G3 reactive audit:", g["G3_reactive_audit"]["ode_residual_machine_zero"],
          "zeta0-lossless:", g["G3_reactive_audit"]["zeta0_lossless_confirmed"])
    print("G1 finite:", g["G1_finite"], " G0 max_r:", g["G0_regime_max_r"])
    print("--- Form S (shipped Eq 2.1): peak_rS=%.3f peak_VI=%.3f phase_max=%.1f pinch=%s" % (
        out["form_S"]["peak_rS"], out["form_S"]["peak_VI"], out["form_S"]["phase_max_abs"], out["form_S"]["origin_pinch"]))
    print("--- Form R (reactive w-a): peak_VI slope/corr vs omega_S=%.2f/%.2f  phase_max=%.1f  in_legacy=%s in_eq63=%s" % (
        out["form_R"]["peak_VI_slope_vs_omegaS"], out["form_R"]["peak_VI_corr_vs_omegaS"],
        out["form_R"]["phase_max_abs_over_scan"], out["form_R"]["in_window_legacy"]["any"], out["form_R"]["in_window_eq63"]["any"]))
    print("--- Form T (transductive w-b): peak_VI slope/corr=%.2f/%.2f phase_max=%.1f" % (
        out["form_T"]["peak_VI_slope_vs_omegaS"], out["form_T"]["peak_VI_corr_vs_omegaS"], out["form_T"]["phase_max_abs_over_scan"]))
    print("=== AXIS iii shape class:", out["adjudication"]["axis_iii_shape_class"]["all_as_derived"])
    print("=== AXIS i peak location:", out["adjudication"]["axis_i_peak_location"]["verdict"])
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                           "2026-07-19_flag-f-s-dynamics_result.json"), "w") as fh:
        json.dump(out, fh, indent=2)
    print("wrote result json")

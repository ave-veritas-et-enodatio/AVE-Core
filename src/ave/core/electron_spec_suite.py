"""
D7 — the ELECTRON SPEC-SHEET harness (genesis-v5 component 6)
============================================================

T1–T6 as runnable MEASUREMENT + FLOOR functions. This is the success-GATE harness,
NOT a verdict: the electron-class verdict is produced by RUNNING these on an
assembled object (a run-time activity, expensive, the parallel runner). Per Rule 11
(honest closure) NO positive is manufactured here — each function returns a bin
(PASS / NEGATIVE / UNRESOLVED-below-floor) from the data, with the floor gating
FIRST (ave-apparatus-floor-attribution; the coax bin-65/67 ordering).

Each Ti carries its consistency-vs-emergence class-tag (prereg §2 D7) and reads its
observable in its OWN coordinate (phase-space-coordinate-check): T2 in the
(V_inc,V_ref) phase-space via the Park-along-contours extractor (r≥3 floor); the
rest in real-space / energy-ledger coordinates.
"""

from __future__ import annotations

import numpy as np

from ave.utils.fast_winding_extractor import extract_2_3_omega_fast


# ----------------------------------------------------------------- T1 MASS
def spec_T1_mass_converges(energy_series, drift_floor: float) -> dict:
    """T1 (primary, emergence-vs-manifestation): H_total → constant. FLOOR FIRST
    (F0e): the convergence is gauged against `drift_floor` (the quiet-phase drift
    level). The FALSIFIER (frozen) is 'still rising at run-end' (the graft-v4 t^2.2
    stop-time-dependent lesson). Bins: CONVERGED / STILL-RISING / UNRESOLVED."""
    s = np.asarray(energy_series, dtype=float)
    if s.size < 4:
        return {"bin": "UNRESOLVED", "reason": "series too short"}
    half = s[s.size // 2:]
    # normalized late-window slope per step
    t = np.arange(half.size)
    slope = float(np.polyfit(t, half, 1)[0])
    scale = float(np.mean(np.abs(half))) + 1e-30
    drift = abs(slope) * half.size / scale  # fractional change over the late window
    if drift < drift_floor:
        bin_ = "CONVERGED"
    elif slope > 0:
        bin_ = "STILL-RISING"          # the falsifier (secular pump / t^2.2)
    else:
        bin_ = "UNRESOLVED"
    return {"bin": bin_, "late_drift_frac": drift, "drift_floor": drift_floor,
            "late_slope": slope, "class": "emergence|manifestation"}


# ----------------------------------------------------------------- T2 CHARGE
def spec_T2_charge_winding(engine, R: float, r: float, r_meas_floor: float = 3.0) -> dict:
    """T2 (emergence-de-novo vs manifestation-planted-survives): the (2,3) winding
    integer, sign=handedness. PHASE-SPACE read (Park-along-contours extractor).
    FLOOR FIRST (F0b): r_meas ≥ 3 cells or the read is VOID."""
    if r < r_meas_floor:
        return {"bin": "VOID", "reason": f"r={r:.2f} < r_meas_floor={r_meas_floor}"}
    pi_omega = (engine.omega - engine.omega_prev) / engine.dt
    res = extract_2_3_omega_fast(engine.omega, pi_omega, R, r, engine.N)
    w_tor, w_pol = res.get("w_tor", 0), res.get("w_pol", 0)
    is_23 = (abs(abs(w_tor) - 2) < 0.5) and (abs(abs(w_pol) - 3) < 0.5)
    bin_ = "QUANTIZED-2-3" if is_23 else "NOT-2-3"
    return {"bin": bin_, "w_tor": w_tor, "w_pol": w_pol,
            "sign": int(np.sign(w_pol)) if w_pol else 0,
            "class": "emergence|manifestation"}


# ----------------------------------------------------------------- T3 SPIN
def spec_T3_spin(engine, R_ring: float, axis: int | None = None) -> dict:
    """T3 (emergence vs consistency): locked angular momentum. DERIVE the engine-
    unit mapping (representation-capability — do NOT assume ℏ/2). Reports L_bulk
    and the DERIVED half-pole-pair target FORM L_target=½·ρ·R²·Ω (the prereg §6(4)
    form, NOT a pre-committed number); the verdict (ratio→½ without dialing
    lock_eta) is a RUN-TIME read."""
    L = engine.angular_momentum_bulk(axis)
    Omega = engine.bulk_circulation_z() / (np.pi * R_ring ** 2 + 1e-30)  # mean ω proxy
    rho0 = 1.0  # natural units
    L_target_form = 0.5 * rho0 * R_ring ** 2 * Omega
    ratio = L / (L_target_form + 1e-30)
    return {"L_bulk": L, "L_target_half_pole_pair_form": L_target_form,
            "ratio_to_half_form": ratio, "class": "emergence|consistency",
            "note": "verdict = ratio->1 (i.e. L->½ρR²Ω) WITHOUT dialing lock_eta; run-time"}


# ----------------------------------------------------------------- T4 KICK
def spec_T4_stability_kick(reverify_callable, *args, **kwargs) -> dict:
    """T4 (manifestation): perturb, then T1–T3 RE-VERIFY. Caller supplies a
    callable that re-runs the relevant measurements post-kick; this records the
    pass/fail of the re-verification."""
    result = reverify_callable(*args, **kwargs)
    return {"bin": "RE-VERIFIED" if result else "FAILED-POST-KICK",
            "reverify": bool(result), "class": "manifestation"}


# ----------------------------------------------------------------- T5 PAIRS
def spec_T5_born_in_pairs(engine, tol: float = 0.1, axis: int | None = None) -> dict:
    """T5 (emergence; absence ≠ failure-of-discipline): the global handedness
    ledger sums to zero (Kelvin/pair-canon). Reuses the D4 ledger."""
    lc = engine.handedness_ledger(axis=axis, tol=tol)
    return {"bin": "BALANCED" if lc["balanced"] else "UNBALANCED",
            "global_handedness": lc["global_handedness"],
            "abs_net_frac": lc["abs_net_frac"], "core_sense": lc["core_sense"],
            "class": "emergence"}


# ----------------------------------------------------------------- T6 DE BROGLIE
def spec_T6_de_broglie(momenta, wavelengths, fit_floor: float = 0.15) -> dict:
    """T6 (consistency): λ ∝ 1/p. Only the EXPONENT (−1) is frozen by power-
    counting (the magnitude is set by the assembled T1 mass). Fits log λ vs log p;
    PASS if the slope ≈ −1 within fit_floor."""
    p = np.asarray(momenta, float)
    lam = np.asarray(wavelengths, float)
    if p.size < 2 or np.any(p <= 0) or np.any(lam <= 0):
        return {"bin": "UNRESOLVED", "reason": "need ≥2 positive (p, λ)"}
    slope = float(np.polyfit(np.log(p), np.log(lam), 1)[0])
    ok = abs(slope - (-1.0)) < fit_floor
    return {"bin": "INVERSE-P" if ok else "NOT-INVERSE-P",
            "log_slope": slope, "fit_floor": fit_floor, "class": "consistency"}

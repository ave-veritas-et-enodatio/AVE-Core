#!/usr/bin/env python3
"""F6 ℏ-as-FD — derived FD-ratio(ρ) vs the banked floor-arm FD leg.

Derivation:  research/2026-07-20_hbar-as-fd_DERIVATION_FROZEN.md (form + bins FROZEN)
Result:      research/2026-07-20_hbar-as-fd_result.md
Data (out):  research/2026-07-20_hbar-as-fd_result.json
Consumes (banked, byte-untouched): research/2026-07-19_f6-thermal-floor-arm_result.json
  (the FENCED FD leg, §5), + seed_floor / OscillatorBath (config-reuse; meter untouched).

SECTOR / REGIME (mandatory header):
  Sector : R7 thermal / entropy-sink (F6 ε→T2). Floor (fluctuation) = T2 bath DOF;
           response (dissipation) = certified scalar-port transduction. NOT A1, NOT Cosserat.
  Regime : Regime I sub-yield, MILD A≈0.10, κ=0.030 certified; cold plant (linear lattice);
           the floor is a CLASSICALLY-seeded ensemble.
  Scope  : instrument-class-scoped to the certified scalar-port junction (phased-array ruling).

WHAT THIS DRIVER DOES (research-only; engine + meter BYTE-UNTOUCHED):
  1. FIRST-PRINCIPLES validation of the FLUCTUATION side: Monte-Carlo the ACTUAL
     seed_floor statistics on real OscillatorBath objects (no lattice, no step) —
     confirm the √ρ amplitude law and the ½:½ quadrature split (§1 of the derivation).
  2. Read the banked FD leg (relax = engine-read certified response; std(R_rev)).
  3. Predict the forced FD-ratio(ρ) = k·√ρ/relax(ρ), k = single calibration anchor (ρ=1).
  4. Overlay vs banked; residuals + per-point N=6 σ margins; apply the FROZEN bins.
  5. Derive the zero-point (ℏ) discriminator numbers (D1 intercept, D2 ω-slope).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from ave.thermal.f6_bath_meter import OscillatorBath
from scripts.vol_1_foundations.f6_counting_arrow_arm import OMEGA_MIN, _m_for
from scripts.vol_1_foundations.f6_floor_battery import _signal_per_mode, seed_floor

_REPO = Path(__file__).resolve().parents[3]
_ARM_JSON = _REPO / "research" / "2026-07-19_f6-thermal-floor-arm_result.json"

# ── FROZEN config (matches the arm's primary comb; all ENGINEERING CHOICES) ──
PRIMARY_DW = 0.050
RHO_LADDER = (0.0, 0.3, 1.0, 2.0, 3.0, 5.0)
MC_REALIZATIONS = 20000          # phase-ensemble size for the first-principles MC
MC_BASE_SEED = 424242            # research-only RNG (NOT a floor seed used by the arm)
N_ARM_SEEDS = 6                  # the arm's frozen ensemble size (sets σ_point)
ANCHOR_RHO = 1.0                 # single calibration anchor (floor=signal)
SIGMA_FRAC = 1.0 / np.sqrt(2 * (N_ARM_SEEDS - 1))   # 0.316 — std-estimate uncertainty, N=6
FORM_MATCH_NSIGMA = 1.5          # FROZEN tolerance band (derivation §5)


def mc_floor_statistics() -> dict:
    """FIRST-PRINCIPLES: MC the ACTUAL seed_floor on real bath objects (no engine step).

    Validates (derivation §1): std of a linear functional ∝ √ρ (amplitude law);
    C-state and L-state each carry ½·(energy-per-mode) (Johnson-Nyquist equipartition).
    """
    m = _m_for(PRIMARY_DW)
    e_sig = _signal_per_mode(PRIMARY_DW)
    rng = np.random.default_rng(MC_BASE_SEED)
    rows = []
    for rho in RHO_LADDER:
        if rho == 0.0:
            rows.append({"rho": 0.0, "std_q": 0.0, "std_q_over_sqrtrho": float("nan"),
                         "c_state_mean": 0.0, "l_state_mean": 0.0, "half_M_efm": 0.0})
            continue
        efm = rho * e_sig
        qs = np.empty(MC_REALIZATIONS)
        cs = np.empty(MC_REALIZATIONS)
        ls = np.empty(MC_REALIZATIONS)
        for i in range(MC_REALIZATIONS):
            bath = OscillatorBath(M=m, omega_min=OMEGA_MIN, delta_omega=PRIMARY_DW)
            seed_floor(bath, efm, int(rng.integers(0, 2**31 - 1)))
            qs[i] = float(bath.x.sum())                             # drive-like linear functional
            cs[i] = float(0.5 * (bath.omega**2 * bath.x**2).sum())  # C-state (capacitor) energy
            ls[i] = float(0.5 * (bath.p**2).sum())                  # L-state (inductor) energy
        rows.append({
            "rho": rho, "std_q": float(qs.std()),
            "std_q_over_sqrtrho": float(qs.std() / np.sqrt(rho)),
            "c_state_mean": float(cs.mean()), "l_state_mean": float(ls.mean()),
            "half_M_efm": float(0.5 * m * efm),
        })
    # amplitude-law flatness: max fractional deviation of std_q/√ρ from its mean
    ratios = np.array([r["std_q_over_sqrtrho"] for r in rows if r["rho"] > 0])
    amp_law_flatness = float(np.max(np.abs(ratios - ratios.mean())) / ratios.mean())
    # quadrature symmetry: max |C−L|/(½ efm) over ρ>0
    quad = [abs(r["c_state_mean"] - r["l_state_mean"]) / r["half_M_efm"]
            for r in rows if r["rho"] > 0]
    return {"m": m, "e_sig": e_sig, "rows": rows,
            "amp_law_sqrt_rho_flatness": amp_law_flatness,
            "quadrature_split_max_asym": float(max(quad))}


def load_banked_fd() -> dict:
    """Read the banked (engine-read) FD leg: relax(ρ) [dissipation], std(R_rev), fd_ratio."""
    d = json.loads(_ARM_JSON.read_text())
    rows = d["fd_leg"]["rows"]
    return {
        "rho": [r["rho"] for r in rows],
        "relax": [r["relax_over_trec"] for r in rows],
        "fluct_sem": [r["fluct_proxy_sem"] for r in rows],
        "std_rrev": [r["fluct_proxy_sem"] * np.sqrt(N_ARM_SEEDS) for r in rows],
        "fd_ratio": [r["fd_ratio"] for r in rows],
    }


def predict_and_overlay(banked: dict) -> dict:
    """Forced FD = k·√ρ/relax (k anchored at ρ=1); overlay vs banked; frozen-bin verdict."""
    rho = np.array(banked["rho"])
    relax = np.array(banked["relax"])
    data = np.array(banked["fd_ratio"])
    i1 = int(np.where(rho == ANCHOR_RHO)[0][0])
    k = float(data[i1] * relax[i1] / np.sqrt(ANCHOR_RHO))   # single calibration prefactor (TAGGED)
    pred = np.where(rho > 0, k * np.sqrt(rho) / relax, 0.0)

    nz = rho > 0
    rel_err = np.where(nz, (pred - data) / np.where(nz, data, 1.0), 0.0)
    sigma_pt = data * SIGMA_FRAC                             # per-point N=6 std-estimate uncertainty
    nsig = np.where((rho > 0) & (data > 0), (pred - data) / np.where(data > 0, sigma_pt, 1.0), 0.0)
    max_nsig = float(np.max(np.abs(nsig[nz])))

    # numerator-only cross-check: std(R_rev) vs √ρ (anchor ρ=1)
    std_rrev = np.array(banked["std_rrev"])
    kn = float(std_rrev[i1] / np.sqrt(ANCHOR_RHO))
    pred_num = np.where(rho > 0, kn * np.sqrt(rho), 0.0)
    num_rel_err = np.where(nz, (pred_num - std_rrev) / np.where(nz, std_rrev, 1.0), 0.0)

    within = bool(max_nsig <= FORM_MATCH_NSIGMA)
    intercept_zero = bool(data[rho == 0.0][0] == 0.0)       # forced classical signature (D1)
    monotone = bool(np.all(np.diff(data[nz]) > 0))
    if within and monotone:
        verdict = "FORM-MATCH"
    elif not monotone or max_nsig > FORM_MATCH_NSIGMA:
        verdict = "FORM-MISMATCH"
    else:
        verdict = "UNDETERMINED"
    return {
        "k_calibration": k, "anchor_rho": ANCHOR_RHO,
        "pred_fd": pred.tolist(), "banked_fd": data.tolist(),
        "rel_err": rel_err.tolist(), "sigma_point": sigma_pt.tolist(),
        "pred_minus_data_over_sigma": nsig.tolist(), "max_abs_nsigma": max_nsig,
        "sigma_frac_N6": float(SIGMA_FRAC), "form_match_nsigma_band": FORM_MATCH_NSIGMA,
        "numerator_pred_std_rrev": pred_num.tolist(), "numerator_rel_err": num_rel_err.tolist(),
        "intercept_zero_forced": intercept_zero, "monotone_rising": monotone,
        "verdict": verdict,
    }


def zero_point_discriminator() -> dict:
    """Derived ℏ discriminator (coth, imported-for-comparison — NOT asserted classical)."""
    m = _m_for(PRIMARY_DW)
    omega = OMEGA_MIN + np.arange(m) * PRIMARY_DW
    return {
        "omega_min": float(omega[0]), "omega_max": float(omega[-1]),
        "D1_intercept_classical": 0.0,        # ρ→0 amplitude intercept (classical, forced)
        "D1_intercept_quantum": "sqrt(E_zp/e_sig) > 0",   # a quantum-seeded floor would show this
        "D2_omega_ratio_classical": 1.0,      # energy-per-mode flat in ω (equipartition)
        "D2_omega_ratio_quantum": float(omega[-1] / omega[0]),   # zero-point ∝ ω
        "note": "classical seeding forces D1=0, D2=1 (no zero-point term); reaching ℏ needs a "
                "quantum-seeded floor E_m=½ℏω·coth(ℏω/2kT) — routed SPEC, not built.",
    }


def run() -> dict:
    mc = mc_floor_statistics()
    banked = load_banked_fd()
    overlay = predict_and_overlay(banked)
    zp = zero_point_discriminator()
    return {
        "meta": {
            "lane": "F6 ℏ-as-FD — derived FD-ratio(ρ) vs the banked FD leg",
            "derivation": "research/2026-07-20_hbar-as-fd_DERIVATION_FROZEN.md",
            "consumes": "research/2026-07-19_f6-thermal-floor-arm_result.json (FENCED FD leg §5)",
            "instrument": "src/ave/thermal/f6_bath_meter.py (LatticeBathCoupler — BYTE-UNTOUCHED)",
            "class": "consistency (classical FD form-match); NOTHING at emergence-class",
        },
        "mc_first_principles": mc,
        "banked_fd_leg": banked,
        "overlay": overlay,
        "zero_point_discriminator": zp,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="F6 ℏ-as-FD derived FD-ratio(ρ) vs banked")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    out = run()
    if args.json:
        print(json.dumps(out, indent=2))
        return
    mc, ov, zp = out["mc_first_principles"], out["overlay"], out["zero_point_discriminator"]
    print("=" * 96)
    print("F6 ℏ-as-FD — derived FD-ratio(ρ) vs the banked floor-arm FD leg")
    print("=" * 96)
    print(f"  [1] FIRST-PRINCIPLES floor stats (MC on real seed_floor, no engine step): "
          f"M={mc['m']}, e_sig={mc['e_sig']:.5f}")
    print(f"      √ρ amplitude-law flatness  = {mc['amp_law_sqrt_rho_flatness']:.4f}  "
          f"(→0 ⇒ std ∝ √ρ FORCED)")
    print(f"      ½:½ quadrature max asym    = {mc['quadrature_split_max_asym']:.4f}  "
          f"(→0 ⇒ C-state = L-state = ½·energy)")
    print(f"  [2-4] forced FD = k·√ρ/relax, k(anchor ρ={ov['anchor_rho']}) = {ov['k_calibration']:.5f}")
    print(f"      {'ρ':>5} {'relax':>7} {'banked':>8} {'pred':>8} {'relerr':>7} {'(σ)':>6}")
    for i, r in enumerate(out["banked_fd_leg"]["rho"]):
        print(f"      {r:>5.1f} {out['banked_fd_leg']['relax'][i]:>7.4f} "
              f"{ov['banked_fd'][i]:>8.4f} {ov['pred_fd'][i]:>8.4f} "
              f"{ov['rel_err'][i]:>7.3f} {ov['pred_minus_data_over_sigma'][i]:>6.2f}")
    print(f"      max |Δ/σ| = {ov['max_abs_nsigma']:.2f}  (band = {ov['form_match_nsigma_band']}σ, "
          f"σ_frac[N=6] = {ov['sigma_frac_N6']:.3f})")
    print(f"  [5] zero-point discriminator: comb ω∈[{zp['omega_min']:.2f},{zp['omega_max']:.2f}]; "
          f"D2 quantum ω-ratio = {zp['D2_omega_ratio_quantum']:.3f} (classical 1.0); "
          f"D1 classical intercept = {zp['D1_intercept_classical']}")
    print("-" * 96)
    print(f"  ★ VERDICT (frozen bins): {ov['verdict']}")


if __name__ == "__main__":
    main()

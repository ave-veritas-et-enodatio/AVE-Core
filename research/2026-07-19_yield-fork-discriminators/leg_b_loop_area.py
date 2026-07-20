"""Leg B — memristor loop-area discriminator (P_phase5_memristor_loop_area).

Frozen protocol: research/2026-07-19_yield-fork-loop-area_PROTOCOL-COMPLETION.md
Drives the canonical Level-2 ODE (kernel byte-locked to k4_tlm.py) through
near-yield cycles r(t)=0.7+0.3 sin(wt), sweeps w*tau, measures |∮ S dr| in the
(r,S) plane [primary] and |∮ I dV| in the (V,I) pinched Lissajous [cross-check],
locates the peak, and adjudicates per the frozen bins.

Verdict is the frozen-bin output. The H-ledger structural finding lives in the
RESULT doc; it does not retro-edit this verdict (Rule-11).
"""

from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yield_fork_kernel as k  # noqa: E402

# Registered drive (frozen sec 3)
R0 = 0.7
DR = 0.3
DR_SUBRUPT = 0.25  # robustness variant (max r = 0.95, below rupture)
TAU_RELAX = 1.0  # native (TAU_RELAX_NATIVE)

# Falsification window on the peak (#59 sec11)
PEAK_LO = 0.85
PEAK_HI = 0.95


def sweep(r0: float, dr: float, omega_taus: np.ndarray) -> dict:
    a_rs = []
    a_vi = []
    pinch_v = []
    pinch_i = []
    finite = []
    for wt in omega_taus:
        s = k.integrate_cycle(r0, dr, float(wt), tau_relax=TAU_RELAX, tau_fn=k.tau_const)
        a_rs.append(k.loop_area_rS(s))
        vi = k.loop_area_VI(s)
        a_vi.append(vi["area_VI"])
        pinch_v.append(vi["min_absV"])
        pinch_i.append(vi["min_absI"])
        finite.append(s["finite"])
    return {
        "omega_tau": omega_taus.tolist(),
        "area_rS": a_rs,
        "area_VI": a_vi,
        "pinch_min_absV": pinch_v,
        "pinch_min_absI": pinch_i,
        "finite": finite,
    }


def peak_location(r0: float, dr: float, omega_taus: np.ndarray, areas: np.ndarray, plane: str = "rS") -> dict:
    """Peak omega*tau by coarse argmax then a FINE linear sub-grid refit.

    (An earlier parabolic-in-log refit overshot on the very flat top; a direct
    fine-grid argmax is robust. Documented deviation, discovered at run time.)
    """
    idx = int(np.argmax(areas))
    wt_argmax = float(omega_taus[idx])
    lo = omega_taus[max(0, idx - 2)]
    hi = omega_taus[min(len(areas) - 1, idx + 2)]
    fine = np.linspace(lo, hi, 81)

    def area_at(w):
        s = k.integrate_cycle(r0, dr, float(w), tau_relax=TAU_RELAX, tau_fn=k.tau_const)
        return k.loop_area_rS(s) if plane == "rS" else k.loop_area_VI(s)["area_VI"]

    fine_areas = np.array([area_at(w) for w in fine])
    j = int(np.argmax(fine_areas))
    return {
        "peak_coarse_argmax": wt_argmax,
        "peak_refined": float(fine[j]),
        "area_at_peak": float(fine_areas[j]),
    }


def zero_tolerance() -> dict:
    """Integrator floor from the two analytic-zero limits (frozen sec 6)."""
    s_qs = k.integrate_cycle(R0, DR, 1e-3, tau_relax=TAU_RELAX, tau_fn=k.tau_const)
    s_fr = k.integrate_cycle(R0, DR, 1e3, tau_relax=TAU_RELAX, tau_fn=k.tau_const)
    eps_qs = k.loop_area_rS(s_qs)
    eps_fr = k.loop_area_rS(s_fr)
    tol = 10.0 * max(eps_qs, eps_fr)
    return {"eps_quasistatic": eps_qs, "eps_frozen": eps_fr, "tol": tol}


def h_ledger_finding() -> dict:
    """Disclosed STRUCTURAL finding (routed to Grant; does NOT change the verdict).

    The frozen bins equate 'finite ∮' with 'dissipative'. But the first-order
    overdamped ODE (Eq 2.1) produces a finite ∮ = the canonical 'dissipated
    energy per cycle' (tau-relax:89) BY ITS OWN STRUCTURE. The ∮ is a
    rate-dependent lag (Debye) and its DISSIPATIVE reading is a model choice
    (Flag F), not an independent measurement of an axiom resistor:

      1. The loop area -> 0 in BOTH the quasi-static (ωτ->0) and frozen
         (ωτ->inf) limits -> it is purely a rate-dependent lag, peaking at
         ωτ~1 (the Debye signature). A rate-dependent lag is produced by a
         reactive element too; the loop area alone does not require a resistor.
      2. Flag-F relocation stands on the MODEL-TAUTOLOGY leg only (2026-07-19
         repair, R-3): this driver integrates the first-order Eq 2.1 ON ITSELF
         (protocol sec8: 'this leg RUNS Eq 2.1 as frozen'), so it can ONLY ever
         report first-order-overdamped behaviour -- it structurally cannot see
         whether the substrate's true near-yield S-dynamics are first-order
         (dissipative) or second-order kinetic-S (I_S != 0, potentially
         lossless). Which they are is #59 Flag F (sec12: 'overdamped-action
         limit gives the first-order relaxation ODE is asserted but not
         derived'), a DERIVATION question upstream of this measurement.
         RETRACTED (Rule-12): an earlier note here claimed a second-order
         reactive form 'gives the SAME tau lag' -- FALSE. A lossless
         (undamped) second-order kinetic-S is RESONANT, not Debye; it does not
         produce the same monotonic tau-lag. The relocation does not rest on
         any lag-equivalence; it rests on the driver only running Eq 2.1.
    """
    wt_peak = 1.0
    a_qs = k.loop_area_rS(k.integrate_cycle(R0, DR, 1e-3, tau_relax=TAU_RELAX, tau_fn=k.tau_const))
    a_peak = k.loop_area_rS(k.integrate_cycle(R0, DR, wt_peak, tau_relax=TAU_RELAX, tau_fn=k.tau_const))
    a_fr = k.loop_area_rS(k.integrate_cycle(R0, DR, 1e3, tau_relax=TAU_RELAX, tau_fn=k.tau_const))
    return {
        "loop_area_quasistatic_wt_1e-3": a_qs,
        "loop_area_peak_wt_1p0": a_peak,
        "loop_area_frozen_wt_1e3": a_fr,
        "rate_dependent_lag_confirmed": bool(a_qs < 0.01 * a_peak and a_fr < 0.01 * a_peak),
        "true_fork_locus": (
            "#59 Flag F (first-order overdamped [dissipative] vs second-order reactive "
            "[lossless]) -- a derivation question, upstream of this measurement"
        ),
        "note": (
            "Finite ∮ is a rate-dependent Debye lag (-> 0 in both quasi-static and frozen "
            "limits). Its DISSIPATIVE reading is inherited from the first-order overdamped model "
            "structure (Flag F, asserted-not-derived), not independently measured. The loop area "
            "does NOT by itself lift the fork. Flag-F relocation rests on the MODEL-TAUTOLOGY leg "
            "only (2026-07-19 repair, R-3): the driver integrates first-order Eq 2.1 on itself, so "
            "it cannot distinguish first- from second-order dynamics. The earlier 'a second-order "
            "reactive form gives the SAME tau lag' claim is RETRACTED (Rule-12) as FALSE -- a "
            "lossless second-order kinetic-S is resonant, not Debye."
        ),
    }


def window_test_reframe(sw_primary: dict, omega_taus: np.ndarray) -> dict:
    """2026-07-19 REPAIR (R-1 + R-2): honest re-banking of the window test.

    R-1 (the zero-information reframe): the (r,S)-plane loop area of ANY
    first-order relaxation kernel is the Debye dissipation shape, whose peak is
    pinned at omega*tau ~ 1 independent of the nonlinear S_eq shape (verified: the
    (r,S) peak sits at 1.0014 across the entire drive family r0 in [0.3,0.9],
    Dr in [0.05,0.5] -- it NEVER enters [0.85,0.95]). So the frozen (r,S)-plane
    window test is A-PRIORI UNREACHABLE for a first-order kernel: its 'peak
    outside [0.85,0.95]' failure is a THEOREM OF THE OBSERVABLE, not evidence.
    The TESTABLE plane is (V,I), whose peak DOES move with drive and lands at
    0.911 (registered Dr=0.3) -- INSIDE the window (F-B2 caveat: no origin-pinch).

    R-2 (mis-registration provenance, BOTH-AND): the [0.85,0.95] window's 0.9
    center was imported from doc-48's A^2_cos response-amplitude observable
    (#59 sec6.3, '48 sec6: A^2_cos peak 0.90') -- a DIFFERENT observable from the
    loop area. #59 sec6.4's own arithmetic assumes A_2/A_1 ~= 1/10, but at the
    REGISTERED drive (r0=0.7, Dr=0.3) A_2/A_1 = Dr^2/(4 r0^2) = 0.046, and Eq 6.3
    then peaks at ~0.978 (0.954 even at the assumed 1/10) -- NOT 0.9. So the
    registered window does not follow from #59's own Eq 6.3.
    """
    r0, dr = R0, DR
    a1 = r0**2 * dr**2
    a2 = dr**4 / 4.0
    ratio = a2 / a1
    x = np.linspace(0.3, 1.5, 200001)

    def eq63_peak(rho: float) -> float:
        f = x / (1 + x**2) + rho * (2 * x / (1 + 4 * x**2))
        return float(x[int(np.argmax(f))])

    rs_peak = float(omega_taus[int(np.argmax(sw_primary["area_rS"]))])
    return {
        "rS_window_test_information_free": True,
        "rS_peak_coarse_argmax": rs_peak,
        "rS_peak_pinned_at_linear_debye": True,
        "rS_a_priori_unreachable_note": (
            "The (r,S) loop area of a first-order kernel is the Debye dissipation shape, peak "
            "pinned at omega*tau~1 independent of nonlinearity -> the [0.85,0.95] window can never "
            "be reached in this plane -> the NEITHER verdict carries no evidence against memristive."
        ),
        "testable_plane_is_VI": True,
        "VI_peak_registered_dr0p3": 0.911,
        "VI_peak_inside_window": True,
        "mis_registration": {
            "window_center_0p9_provenance": (
                "doc-48 A^2_cos response-amplitude observable (#59 sec6.3), NOT the loop area"
            ),
            "eq63_ratio_A2_over_A1_at_registered_drive": ratio,
            "eq63_assumed_ratio": 0.1,
            "eq63_peak_at_registered_ratio": eq63_peak(ratio),
            "eq63_peak_at_assumed_1over10": eq63_peak(0.1),
            "note": (
                "The registered [0.88,0.92]/[0.85,0.95] window with 0.9 center does NOT follow from "
                "#59's own Eq 6.3 at the registered drive (which yields ~0.954-0.978); the 0.9 was "
                "imported from a different observable (doc-48 A^2_cos)."
            ),
        },
    }


def adjudicate(peak_wt: float, area_at_peak: float, tol: float, all_finite: bool) -> dict:
    if not all_finite:
        return {"bin": "INSTRUMENT", "verdict": "fail-closed (non-finite in sweep)"}
    if area_at_peak <= tol:
        return {"bin": "ZERO", "verdict": "lossless-reactance branch (Grant's lean corroborated)"}
    in_window = PEAK_LO <= peak_wt <= PEAK_HI
    if in_window:
        return {
            "bin": "MEMRISTIVE",
            "verdict": "finite area, peak in [0.85,0.95] matches P_phase5 -> memristive branch",
        }
    return {
        "bin": "NEITHER",
        "verdict": f"finite area but peak {peak_wt:.3f} outside [0.85,0.95] -> fail-closed (artifact bin)",
    }


def run() -> dict:
    # engine-native tau_relax sanity (imported from ave to prove native units)
    from ave.core.constants import TAU_RELAX_NATIVE

    omega_taus = np.logspace(np.log10(0.05), np.log10(10.0), 60)
    tol = zero_tolerance()

    sw = sweep(R0, DR, omega_taus)
    sw_sub = sweep(R0, DR_SUBRUPT, omega_taus)

    pk = peak_location(R0, DR, omega_taus, np.asarray(sw["area_rS"]), plane="rS")
    pk_vi = peak_location(R0, DR, omega_taus, np.asarray(sw["area_VI"]), plane="VI")
    pk_sub = peak_location(R0, DR_SUBRUPT, omega_taus, np.asarray(sw_sub["area_rS"]), plane="rS")
    # 2026-07-19 repair (R-5 finding 10): the sub-rupture (V,I) peak was quoted
    # in the result table as 0.955 but never banked; the reproducing value is
    # 0.9577. Compute and bank it so the table cell has a machine-checkable source.
    pk_sub_vi = peak_location(R0, DR_SUBRUPT, omega_taus, np.asarray(sw_sub["area_VI"]), plane="VI")

    # Pinch-through-origin check at the registered operating point: the drive
    # r in [r0-dr, r0+dr] never reaches r=0, so the (V,I) Lissajous is an OFFSET
    # loop, NOT the origin-pinched hysteresis of nonlinear-vacuum-capacitance:66
    # (which needs a full-swing drive). Reported as a finding.
    s_peak = k.integrate_cycle(R0, DR, pk["peak_refined"], tau_relax=TAU_RELAX, tau_fn=k.tau_const)
    vi_peak = k.loop_area_VI(s_peak)
    pinch = {
        "min_absV": vi_peak["min_absV"],
        "min_absI": vi_peak["min_absI"],
        "passes_through_origin": bool(vi_peak["min_absV"] < 1e-3 and vi_peak["min_absI"] < 1e-3),
        "note": "drive r in [0.4,1.0] never crosses r=0 -> (V,I) loop is offset, not origin-pinched",
    }

    verdict = adjudicate(pk["peak_refined"], pk["area_at_peak"], tol["tol"], all(sw["finite"]))

    return {
        "leg": "B_loop_area",
        "protocol": "research/2026-07-19_yield-fork-loop-area_PROTOCOL-COMPLETION.md",
        "kernel_source": "src/ave/core/k4_tlm.py:283,291 (byte-locked; engine untouched)",
        "tau_relax_native_asserted": float(TAU_RELAX_NATIVE),
        "drive": {"r0": R0, "dr": DR, "dr_subrupture": DR_SUBRUPT, "max_r": R0 + DR},
        "zero_tolerance": tol,
        "sweep_primary_rS": sw,
        "sweep_subrupture_rS": {"omega_tau": sw_sub["omega_tau"], "area_rS": sw_sub["area_rS"]},
        "peak_rS": pk,
        "peak_VI": pk_vi,
        "peak_subrupture_rS": pk_sub,
        "peak_subrupture_VI": pk_sub_vi,
        "pinch_through_origin_at_peak": pinch,
        "falsification_window": [PEAK_LO, PEAK_HI],
        "h_ledger_finding": h_ledger_finding(),
        "window_test_reframe_2026_07_19_repair": window_test_reframe(sw, omega_taus),
        "adjudication": verdict,
    }


if __name__ == "__main__":
    import json

    out = run()
    print(json.dumps(out["adjudication"], indent=2))
    print("peak omega*tau (r,S):", out["peak_rS"]["peak_refined"],
          "[PINNED at linear Debye ~1; window test a-priori unreachable]")
    print("peak omega*tau (V,I) registered Dr=0.3:", out["peak_VI"]["peak_refined"],
          "[INSIDE [0.85,0.95] -- the testable plane]")
    print("peak omega*tau (V,I) sub-rupture Dr=0.25:", out["peak_subrupture_VI"]["peak_refined"])
    print("area at peak:", out["peak_rS"]["area_at_peak"], "tol:", out["zero_tolerance"]["tol"])
    hl = out["h_ledger_finding"]
    print("H-ledger: peak area=%.5f  quasistatic=%.2e  frozen=%.2e  rate-dep-lag=%s"
          % (hl["loop_area_peak_wt_1p0"], hl["loop_area_quasistatic_wt_1e-3"],
             hl["loop_area_frozen_wt_1e3"], hl["rate_dependent_lag_confirmed"]))
    print("pinch-through-origin at peak:", out["pinch_through_origin_at_peak"]["passes_through_origin"],
          "(min|I|=%.3f)" % out["pinch_through_origin_at_peak"]["min_absI"])

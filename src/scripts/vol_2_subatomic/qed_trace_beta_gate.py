#!/usr/bin/env python3
"""
QED-TRACE BETA-FUNCTION GATE — kernel-ON log-vs-power-law category test.
========================================================================

FROZEN prereg (pushed before this ran):
    research/2026-07-14_qed-trace-beta-gate_prereg_FROZEN.md

THE ONE QUESTION: does the kernel-ON lattice (Axiom-4 saturation active) produce
any NON-POWER-LAW (logarithmic) scale dependence in the EFFECTIVE COUPLING, with
QED's sign (coupling GROWS at short distance)?  This is the QED-TRACE program's
only chord-class gate.  A-priori expectation (consensus-bias rail): WRONG-FORM or
NULL — the category-mismatch verdict — is the likely, corpus-improving outcome.

★ TRANSFER-REGISTER REQUIREMENT (Grant, load-bearing).  QED's running alpha is a
THROUGH-COUPLING (scattering-amplitude) quantity.  A reactive dress can raise
local stored energy while LOWERING through-coupling, flipping the sign by REGISTER
not physics.  So alpha_eff is defined as the TRANSFER reading (force between two
disturbances vs separation); the REACTIVE (stored-energy / impedance-ratio)
reading is reported KEEP-BOTH alongside.

PROBE HIERARCHY (Grant ruling 2026-07-14): (b) seeded winding pair = PRIMARY
(the two-winding force-vs-separation IS the vacuum-polarization-corrected Coulomb
law; the no-go leaves the inter-winding pair force clm-wcoul2 OPEN); (a) A44 form
factor = CONTROL null-comparator; (c) micropolar point-twist = collapses into (b)
(rotation sector quantized).  The >=2-decade coverage comes from the analytic
Op14 graded-Coulomb dress (universal_pairwise_energy, clm-gdd70j); the field
engine (charge_sector_two_winding, force-blind + dispersion-dominated + sub-decade,
audit w1ni1axfg) supplies a sub-decade empirical anchor with disclosure.

Sector header — MODE static/quasi-static two-body force (transfer class) + analytic
pairwise-dress eval; REGIME cold, KERNEL ON (Op14/Ax4 saturation) with a kernel-OFF
(bare Coulomb) null control; PHASE-STATE sub-yield reversible (r=d_sat wall = the
short-distance endpoint); SECTOR graded-Coulomb dress around a Cosserat (2,q)
micro-rotation winding = the charge screening cloud.  No new engine.

Run:  PYTHONPATH=src python src/scripts/vol_2_subatomic/qed_trace_beta_gate.py
      (add --with-field-engine for the sub-decade Cosserat anchor; heavier)
"""
from __future__ import annotations

import argparse
import json

import numpy as np

from ave.core.constants import ALPHA
from ave.core.universal_operators import universal_pairwise_energy
from ave_path_util import sim_output

# ── native units ────────────────────────────────────────────────────────────
K = 1.0          # bare coupling (native; the FORM/sign result is K-independent)
D_SAT = 1.0      # saturation radius (native yield scale)

# Perturbative scale window (the fair QED-running analog: a SMALL departure over
# many decades, never the non-perturbative Pauli wall).  ~3 decades.
R_LO, R_HI, N_SCALE = 3.0, 3000.0, 46
# 2-decade sub-window for the honest separability gate (the charter's >=2-decade
# claim is tested at exactly 2 decades, not the full 3).
R_LO_2DEC, R_HI_2DEC = 3.0, 300.0

DBIC_DECISIVE = 10.0     # |dBIC| > 10 = decisive model selection
P_GRID = np.linspace(0.3, 8.0, 155)   # power-law exponent grid (deterministic fit)


# ═════════════════════════════════════════════════════════════════════════════
# REGISTER DEFINITIONS  (transfer = through-coupling force ; reactive = Z-ratio)
# ═════════════════════════════════════════════════════════════════════════════
def _force(r: np.ndarray, kernel_on: bool) -> np.ndarray:
    """Central-difference force F = -dU/dr of the pairwise potential.

    kernel_on=True  -> Op14 graded-Coulomb dress (Ax4 saturation active).
    kernel_on=False -> bare Coulomb U = -K/r (the kernel-OFF null control).
    """
    h = 1e-5 * r
    if kernel_on:
        up = np.array([universal_pairwise_energy(float(ri + hi), K, D_SAT) for ri, hi in zip(r, h)])
        dn = np.array([universal_pairwise_energy(float(ri - hi), K, D_SAT) for ri, hi in zip(r, h)])
    else:
        up = -K / (r + h)
        dn = -K / (r - h)
    return -(up - dn) / (2.0 * h)


def transfer_alpha(r: np.ndarray, kernel_on: bool) -> np.ndarray:
    """TRANSFER register: alpha_eff = F(r) / F_coulomb(r).

    Bare Coulomb F_c = -K/r^2, so alpha_eff -> 1 far field (NO running by
    construction).  A departure from 1 that GROWS as r->d_sat with alpha_eff>1
    = QED sign (coupling grows at short distance); alpha_eff<1 = coupling weakens
    at short distance = WRONG-SIGN on the transfer reading.
    """
    F = _force(r, kernel_on)
    F_c = -K / r**2
    return F / F_c


def reactive_alpha(r: np.ndarray, kernel_on: bool) -> np.ndarray:
    """REACTIVE register: alpha_eff proportional to the local impedance/stored-energy
    dress Z(r)/Z0 = 1/(1-(d_sat/r)^2)^(1/4) — the SAME register simulate_running_alpha
    used (C_eff -> Z = sqrt(L/C)).  Kernel-OFF: Z/Z0 == 1 (flat)."""
    if not kernel_on:
        return np.ones_like(r)
    ratio_sq = np.clip((D_SAT / r) ** 2, 0.0, 1.0 - 1e-12)
    return 1.0 / (1.0 - ratio_sq) ** 0.25


# ═════════════════════════════════════════════════════════════════════════════
# THE FITTER — frozen log-vs-power model selection (fair 2-param budget each)
# ═════════════════════════════════════════════════════════════════════════════
def _sse(y, yhat):
    return float(np.sum((y - yhat) ** 2))


def fit_log_vs_power(r: np.ndarray, alpha: np.ndarray) -> dict:
    """Select between M_log and M_pow on the departure D = alpha - 1.

    M_log:  alpha = c0 + c1*ln(r)           {c0, c1}  (linear lstsq)
    M_pow:  alpha = 1 + a*(d_sat/r)^p        {a, p}   (p-grid + linear a; the far-
            field intercept is FIXED at the DERIVED bare value 1, not a free param)

    Both k=2 params, same n, same response space (alpha) -> BIC reduces to
    dBIC = BIC_pow - BIC_log = n*ln(SSE_pow/SSE_log).  dBIC>+10 decisive M_log;
    dBIC<-10 decisive M_pow (frozen).  Consensus-bias: the log is NOT privileged
    (see gate_plant_pow)."""
    n = len(r)
    # M_log
    A = np.vstack([np.ones_like(r), np.log(r)]).T
    coef, *_ = np.linalg.lstsq(A, alpha, rcond=None)
    yhat_log = A @ coef
    sse_log = _sse(alpha, yhat_log)
    # M_pow: for each p, x=(d_sat/r)^p, fit a by projection of (alpha-1) on x
    D = alpha - 1.0
    best = (np.inf, np.nan, np.nan)
    for p in P_GRID:
        x = (D_SAT / r) ** p
        a = float(x @ D / (x @ x)) if (x @ x) > 0 else 0.0
        sse = _sse(D, a * x)
        if sse < best[0]:
            best = (sse, a, float(p))
    sse_pow, a_pow, p_pow = best
    dbic = n * np.log(max(sse_pow, 1e-300) / max(sse_log, 1e-300))
    selected = "M_log" if dbic > DBIC_DECISIVE else ("M_pow" if dbic < -DBIC_DECISIVE else "INCONCLUSIVE")
    # QED sign witness on the log model: alpha grows at short distance
    # (small r) <=> c1<0 in alpha=c0+c1*ln(r).
    log_slope = float(coef[1])
    return {
        "n": n, "sse_log": sse_log, "sse_pow": sse_pow, "dBIC_pow_minus_log": float(dbic),
        "selected": selected,
        "M_log": {"c0": float(coef[0]), "c1_slope_in_ln_r": log_slope},
        "M_pow": {"a": a_pow, "p_exponent": p_pow},
        "alpha_grows_at_short_distance": bool(log_slope < 0),  # QED-sign witness
        "departure_at_r_lo": float(alpha[0] - 1.0), "departure_at_r_hi": float(alpha[-1] - 1.0),
    }


# ═════════════════════════════════════════════════════════════════════════════
# FIRST DELIVERABLE — the simulate_running_alpha.py AUTOPSY (register verdict)
# ═════════════════════════════════════════════════════════════════════════════
def autopsy_simulate_running_alpha() -> dict:
    """Reproduce the prior driver's alpha_eff, then classify its REGISTER.

    Its observable chain (docstring simulate_running_alpha.py:20-27):
        C_eff(dphi) = C_0 / sqrt(1-(dphi/alpha)^2)     [capacitance = STORED ENERGY]
        Z_eff       = sqrt(L/C_eff) = Z_0*(1-...)^(1/4) [characteristic impedance]
        alpha_eff   = Z_particle/Z_0  ->  alpha/sqrt(1-strain^2)
    There is NO transmission / scattering amplitude / force between two objects in
    that chain — it is the LOCAL reactive dress.  VERDICT: REACTIVE-CLASS.  Hence
    its wrong-sign result is a candidate REGISTER ARTIFACT: this re-opens the sign
    question honestly (a reactive dress reads the opposite sign a transfer dress
    reads from the SAME kernel — demonstrated by the two registers in this gate).
    """
    from scripts.vol_2_subatomic.simulate_running_alpha import alpha_eff_axiom4

    energies = [0.001, 0.511, 1.0, 10.0, 100.0, 1000.0, 10000.0, 91188.0, 200000.0]
    rows = [alpha_eff_axiom4(e) for e in energies]
    inv = [(r["energy_mev"], r["inv_alpha_eff"]) for r in rows if r["inv_alpha_eff"] > 0]
    lo_e_inv = inv[0][1]
    hi_e_inv = inv[-1][1]
    rises_with_energy = hi_e_inv > lo_e_inv   # 1/alpha rising with E = WRONG sign
    return {
        "register_verdict": "REACTIVE-CLASS",
        "why": "alpha_eff built from C_eff (capacitance=stored energy) -> Z=sqrt(L/C) "
               "(characteristic impedance); NO transmission/scattering/force term; the "
               "observable is the LOCAL reactive dress, not a through-coupling.",
        "reproduced_inv_alpha_low_E": lo_e_inv,
        "reproduced_inv_alpha_high_E": hi_e_inv,
        "inv_alpha_rises_with_energy_WRONG_SIGN": bool(rises_with_energy),
        "sign_error_source": "TWO artifacts: (1) REACTIVE register choice; (2) a backwards "
               "depth->strain->energy map (strain Sigma 1/d^2 accumulates at LOW energy / many "
               "hops, so its alpha_eff is enhanced at LOW energy) — NOT a computed physics sign.",
        "consequence": "The wrong sign is a register+mapping ARTIFACT, not a transfer-class "
               "physics datum -> the sign question is RE-OPENED honestly (per prereg §3c).",
        "reproduced_table": [{"E_MeV": e, **{k: rows[i][k] for k in
                              ("depth", "strain_ratio", "inv_alpha_eff")}}
                             for i, e in enumerate(energies)],
    }


# ═════════════════════════════════════════════════════════════════════════════
# PRIMARY (b) — analytic Op14 graded-Coulomb dress, both registers, >=2 decades
# ═════════════════════════════════════════════════════════════════════════════
def analytic_sweep() -> dict:
    r = np.geomspace(R_LO, R_HI, N_SCALE)
    tr = transfer_alpha(r, kernel_on=True)
    re = reactive_alpha(r, kernel_on=True)
    fit_tr = fit_log_vs_power(r, tr)
    fit_re = fit_log_vs_power(r, re)
    decades = float(np.log10(R_HI / R_LO))
    # QED-native display column: 1/alpha_eff vs ln(scale).  scale ~ 1/r (energy).
    table = [{"r_over_dsat": float(ri), "log10_energy_proxy": float(np.log10(D_SAT / ri)),
              "alpha_transfer": float(t), "inv_alpha_transfer": float(1.0 / t) if t != 0 else None,
              "alpha_reactive": float(x), "inv_alpha_reactive": float(1.0 / x)}
             for ri, t, x in zip(r, tr, re)]
    return {"scale_decades_covered": decades, "n_points": N_SCALE,
            "r_window": [R_LO, R_HI], "fit_transfer": fit_tr, "fit_reactive": fit_re,
            "alpha_transfer_table": table}


def kernel_off_control() -> dict:
    """G-null: bare Coulomb must show NO running (alpha_eff == 1, flat)."""
    r = np.geomspace(R_LO, R_HI, N_SCALE)
    tr = transfer_alpha(r, kernel_on=False)
    re = reactive_alpha(r, kernel_on=False)
    max_dev_tr = float(np.max(np.abs(tr - 1.0)))
    max_dev_re = float(np.max(np.abs(re - 1.0)))
    fit = fit_log_vs_power(r, tr)
    no_running = max_dev_tr < 1e-6 and max_dev_re < 1e-12
    return {"max_transfer_departure": max_dev_tr, "max_reactive_departure": max_dev_re,
            "no_running": bool(no_running), "fit_selected_on_flat": fit["selected"],
            "G_null_pass": bool(no_running)}


# ═════════════════════════════════════════════════════════════════════════════
# MACHINE GATES — planted-log detect, planted-power detect, separability
# ═════════════════════════════════════════════════════════════════════════════
def gate_plant_log(r: np.ndarray) -> dict:
    """Inject a genuine QED-form log (alpha grows at short distance) and confirm the
    fitter DETECTS it as log with the right sign."""
    # alpha = 1 + (alpha_fs/3pi)*ln(r_ref/r) with r_ref=R_HI -> alpha>1 at small r
    coeff = ALPHA / (3.0 * np.pi)
    alpha_synth = 1.0 + coeff * np.log(R_HI / r)
    fit = fit_log_vs_power(r, alpha_synth)
    ok = fit["selected"] == "M_log" and fit["alpha_grows_at_short_distance"]
    return {"planted": "QED-form log, coeff=alpha/3pi, grows at short distance",
            "selected": fit["selected"], "dBIC": fit["dBIC_pow_minus_log"],
            "sign_detected_grows_short": fit["alpha_grows_at_short_distance"],
            "G_plant_log_pass": bool(ok)}


def gate_plant_pow(r: np.ndarray) -> dict:
    """Inject a small-exponent power law and confirm the fitter DETECTS it as power
    (NOT mis-fit as log).  Guards against over-privileging the log (consensus-bias)."""
    alpha_synth = 1.0 + 0.25 * (D_SAT / r) ** 0.3   # p=0.3 = the hardest (log-like) case
    fit = fit_log_vs_power(r, alpha_synth)
    ok = fit["selected"] == "M_pow"
    return {"planted": "power law a=0.25, p=0.3 (small exponent, hardest case)",
            "selected": fit["selected"], "dBIC": fit["dBIC_pow_minus_log"],
            "recovered_p": fit["M_pow"]["p_exponent"], "G_plant_pow_pass": bool(ok)}


def gate_separability(n_dec_lo: float, n_dec_hi: float) -> dict:
    """G-separability: at the given scale range, confirm a planted true-log and a
    planted small-exponent power law are BOTH decisively classified (|dBIC|>10).
    If not, the INCONCLUSIVE-RANGE bin exists and fires honestly."""
    r = np.geomspace(n_dec_lo, n_dec_hi, N_SCALE)
    gl = gate_plant_log(r)
    gp = gate_plant_pow(r)
    decades = float(np.log10(n_dec_hi / n_dec_lo))
    separable = (abs(gl["dBIC"]) > DBIC_DECISIVE and abs(gp["dBIC"]) > DBIC_DECISIVE
                 and gl["G_plant_log_pass"] and gp["G_plant_pow_pass"])
    return {"decades": decades, "plant_log": gl, "plant_pow": gp,
            "log_and_power_separable_at_range": bool(separable),
            "INCONCLUSIVE_RANGE_fires": bool(not separable)}


# ═════════════════════════════════════════════════════════════════════════════
# CONTROL (a) — A44 form factor: analytic O_skin frequency-form-factor exponent
# ═════════════════════════════════════════════════════════════════════════════
def a44_control() -> dict:
    """Cheap analytic O_skin skin-suppression exponent across the two-tone carrier
    sweep (the existing bulk two-tone form factor collapses toward this = power law).
    Reported as the CONTROL null-comparator; cites the existing bulk result."""
    try:
        from scripts.vol_1_foundations.twotone_formfactor import CARRIERS, overlap_factor
    except Exception as exc:  # pragma: no cover
        return {"available": False, "note": f"twotone import unavailable: {exc}"}
    wbar = np.array(CARRIERS, dtype=float)
    O2 = np.array([overlap_factor((w - (w - 1.0) / 3.0), (w + (w - 1.0) / 3.0))["O_skin"] ** 2
                   for w in wbar])
    # log-log slope of the skin-suppression vs carrier frequency (a power law exponent)
    slope = float(np.polyfit(np.log10(wbar), np.log10(O2), 1)[0])
    return {"available": True, "form": "power-law skin-suppression (no log)",
            "O_skin2_loglog_slope_vs_carrier": slope,
            "cite": "research/2026-07-09_twotone-formfactor_result.json (bulk sep>=3 "
                    "collapses ~16 orders toward O_skin skin-suppression = power law)"}


# ═════════════════════════════════════════════════════════════════════════════
# PRIMARY (b) empirical anchor — Cosserat seeded winding pair (sub-decade, disclosed)
# ═════════════════════════════════════════════════════════════════════════════
def field_engine_anchor(seps, N=40, n_steps=36, pml=4, sigma=3.0, amp=0.05) -> dict:
    """Sub-decade empirical anchor.  DISCLOSED limitations (charge_sector_two_winding.py
    :20-25,378-382, audit w1ni1axfg): force-BLIND-to-charge (symmetric _reflection_density),
    dispersion-dominated (no A1 cage), sub-decade separation reach.  Confirms the
    generic Op14 saturation force-law + supplies the reactive C/L pair; does NOT extend
    the decade coverage."""
    from scripts.vol_1_foundations.charge_sector_two_winding import _fit_power_law, run_pair

    arm = []
    for d0 in seps:
        r = run_pair(N, float(d0), +1.0, +1.0, amp, sigma, n_steps, pml, use_saturation=True)
        rec0 = r["records"][0]
        arm.append({"d0": d0, "a_init": r["a_init"], "H_drift_frac": r["H_drift_frac"],
                    "dispersed_early": r["dispersed_early"],
                    "C_A_reactive": rec0["C_A"], "L_A_reactive": rec0["L_A"]})
    fit = _fit_power_law([{"d0": a["d0"], "a_init": a["a_init"]} for a in arm])
    return {"N": N, "n_steps": n_steps, "separations": list(seps),
            "decades_covered": float(np.log10(max(seps) / min(seps))),
            "disclosed_limitations": ["force-blind-to-charge (audit w1ni1axfg)",
                                      "dispersion-dominated (no A1 cage; Arms halt)",
                                      "sub-decade separation reach"],
            "force_law_exponent": fit.get("exponent"), "fit_r2": fit.get("r2"),
            "coulomb_force_target": -2.0, "arm": arm}


# ═════════════════════════════════════════════════════════════════════════════
# BINNING — the frozen 5-bin verdict, read on the TRANSFER register
# ═════════════════════════════════════════════════════════════════════════════
def classify(analytic, gnull, sep_2dec) -> dict:
    ft = analytic["fit_transfer"]
    fr = analytic["fit_reactive"]
    # INCONCLUSIVE-RANGE pre-empts if 2 decades cannot separate log from power
    if sep_2dec["INCONCLUSIVE_RANGE_fires"]:
        bin_name = "INCONCLUSIVE-RANGE"
    elif ft["selected"] == "M_log" and ft["alpha_grows_at_short_distance"]:
        bin_name = "LOG-EMERGES"  # (coefficient -> -alpha/3pi check is downstream)
    elif ft["selected"] == "M_pow":
        # power law: WRONG-FORM. Sub-note the transfer sign (weakens at short dist).
        weakens = ft["departure_at_r_lo"] < 0  # r_lo = short distance; alpha<1 = weakens
        bin_name = "WRONG-FORM"
        bin_name += " (transfer sign also WRONG: alpha weakens at short distance)" if weakens else ""
    elif abs(ft["departure_at_r_lo"]) < 1e-6:
        bin_name = "NULL-FLAT"
    else:
        bin_name = "INCONCLUSIVE-RANGE"
    return {
        "verdict_bin": bin_name,
        "read_on": "TRANSFER register (primary)",
        "transfer_selected": ft["selected"], "transfer_power_exponent": ft["M_pow"]["p_exponent"],
        "transfer_sign_grows_short": ft["alpha_grows_at_short_distance"],
        "reactive_selected": fr["selected"], "reactive_power_exponent": fr["M_pow"]["p_exponent"],
        "reactive_sign_grows_short": fr["alpha_grows_at_short_distance"],
        "register_flip_observed": bool(ft["alpha_grows_at_short_distance"] !=
                                       fr["alpha_grows_at_short_distance"]),
        "G_null_pass": gnull["G_null_pass"],
    }


# ═════════════════════════════════════════════════════════════════════════════
def main() -> dict:
    ap = argparse.ArgumentParser(description="QED-TRACE beta-function gate.")
    ap.add_argument("--with-field-engine", action="store_true",
                    help="run the sub-decade Cosserat seeded-winding anchor (heavier)")
    ap.add_argument("--fe-seps", type=float, nargs="+", default=[6.0, 8.0, 10.0, 12.0])
    ap.add_argument("--fe-N", type=int, default=40)
    ap.add_argument("--fe-steps", type=int, default=36)
    args = ap.parse_args()

    print("[qed-trace] autopsy: simulate_running_alpha register ...", flush=True)
    autopsy = autopsy_simulate_running_alpha()
    print(f"           register={autopsy['register_verdict']}  "
          f"wrong_sign={autopsy['inv_alpha_rises_with_energy_WRONG_SIGN']}", flush=True)

    print("[qed-trace] primary analytic sweep (both registers, ~3 decades) ...", flush=True)
    analytic = analytic_sweep()
    print("[qed-trace] kernel-OFF null control ...", flush=True)
    gnull = kernel_off_control()

    r_full = np.geomspace(R_LO, R_HI, N_SCALE)
    print("[qed-trace] machine gates (plant-log / plant-pow / separability) ...", flush=True)
    gates = {
        "G_plant_log": gate_plant_log(r_full),
        "G_plant_pow": gate_plant_pow(r_full),
        "G_separability_full_3dec": gate_separability(R_LO, R_HI),
        "G_separability_2dec": gate_separability(R_LO_2DEC, R_HI_2DEC),
    }
    print("[qed-trace] A44 control leg ...", flush=True)
    a44 = a44_control()

    fe = None
    if args.with_field_engine:
        print(f"[qed-trace] field-engine anchor N={args.fe_N} seps={args.fe_seps} ...", flush=True)
        fe = field_engine_anchor(args.fe_seps, N=args.fe_N, n_steps=args.fe_steps)

    verdict = classify(analytic, gnull, gates["G_separability_2dec"])

    result = {
        "prereg": "research/2026-07-14_qed-trace-beta-gate_prereg_FROZEN.md",
        "program": "QED-TRACE beta-function gate",
        "constants": {"K": K, "d_sat": D_SAT, "alpha_fs_CODATA": ALPHA},
        "class": "CONSISTENCY / ECHO (charge-agnostic Op14 saturation form-factor); "
                 "FORM/SIGN category answer is the earnable content, not a value",
        "autopsy_simulate_running_alpha": autopsy,
        "primary_analytic_seeded_winding_dress": analytic,
        "kernel_off_null_control": gnull,
        "machine_gates": gates,
        "a44_control_leg": a44,
        "field_engine_anchor": fe,
        "VERDICT": verdict,
    }

    out = sim_output("qed_trace_beta_gate.json")
    out.write_text(json.dumps(result, indent=2))
    print("\n" + "=" * 72)
    print(f"  VERDICT: {verdict['verdict_bin']}")
    print(f"  transfer: selected={verdict['transfer_selected']} p={verdict['transfer_power_exponent']:.3f} "
          f"grows_short={verdict['transfer_sign_grows_short']}")
    print(f"  reactive: selected={verdict['reactive_selected']} p={verdict['reactive_power_exponent']:.3f} "
          f"grows_short={verdict['reactive_sign_grows_short']}")
    print(f"  register_flip_observed={verdict['register_flip_observed']}")
    print(f"  autopsy register={autopsy['register_verdict']}  G_null_pass={gnull['G_null_pass']}")
    print(f"  scale decades (analytic)={analytic['scale_decades_covered']:.2f}")
    print(f"  separability @2dec: {'PASS' if not gates['G_separability_2dec']['INCONCLUSIVE_RANGE_fires'] else 'INCONCLUSIVE'}")
    print("=" * 72)
    print(f"[qed-trace] wrote {out}")
    _figure(analytic, gnull, verdict)
    return result


def _figure(analytic, gnull, verdict):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    from ave.viz import style
    style.apply()

    tbl = analytic["alpha_transfer_table"]
    r = np.array([t["r_over_dsat"] for t in tbl])
    a_tr = np.array([t["alpha_transfer"] for t in tbl])
    a_re = np.array([t["alpha_reactive"] for t in tbl])
    dsat_over_r = D_SAT / r

    fig, ax = plt.subplots(1, 2, figsize=(11.5, 4.6))

    # Panel 1: both registers vs (d_sat/r) [= energy proxy]; log-log departure.
    ax[0].loglog(dsat_over_r, np.abs(a_tr - 1.0), "o-", color="#0072B2",
                 label="TRANSFER |alpha_eff-1| (through-coupling)")
    ax[0].loglog(dsat_over_r, np.abs(a_re - 1.0), "s-", color="#D55E00",
                 label="REACTIVE |alpha_eff-1| (Z/Z0 stored-energy)")
    ft, fr = analytic["fit_transfer"], analytic["fit_reactive"]
    ax[0].loglog(dsat_over_r, np.abs(ft["M_pow"]["a"]) * dsat_over_r ** ft["M_pow"]["p_exponent"],
                 "--", color="#0072B2", alpha=0.5, label=f"transfer power fit p={ft['M_pow']['p_exponent']:.2f}")
    ax[0].loglog(dsat_over_r, np.abs(fr["M_pow"]["a"]) * dsat_over_r ** fr["M_pow"]["p_exponent"],
                 "--", color="#D55E00", alpha=0.5, label=f"reactive power fit p={fr['M_pow']['p_exponent']:.2f}")
    ax[0].set_xlabel(r"$d_{\mathrm{sat}}/r$   (energy proxy; larger = shorter)")
    ax[0].set_ylabel(r"$|\alpha_{\mathrm{eff}}-1|$  (departure from bare Coulomb)")
    ax[0].set_title("Kernel-ON departure: straight log-log = POWER LAW", fontsize=9)
    ax[0].legend(fontsize=7, loc="upper left")

    # Panel 2: the register-flip — 1/alpha_eff vs ln(energy proxy), QED-native axes.
    lnq = np.log(dsat_over_r)
    ax[1].plot(lnq, 1.0 / a_tr, "o-", color="#0072B2", label="TRANSFER 1/alpha_eff")
    ax[1].plot(lnq, 1.0 / a_re, "s-", color="#D55E00", label="REACTIVE 1/alpha_eff")
    ax[1].axhline(1.0, color="0.5", ls=":", lw=1.0, label="bare (kernel-OFF null, flat)")
    ax[1].set_xlabel(r"$\ln(d_{\mathrm{sat}}/r)$   (increasing energy $\rightarrow$)")
    ax[1].set_ylabel(r"$1/\alpha_{\mathrm{eff}}$  (native units)")
    flip = verdict["register_flip_observed"]
    ax[1].set_title(f"Register flip = {flip}: same kernel, opposite sign", fontsize=9)
    ax[1].legend(fontsize=7, loc="best")
    fig.suptitle("QED-TRACE beta gate: transfer weakens (wrong sign) / reactive grows — "
                 "both POWER LAW, no log", fontsize=10, y=1.02)
    txt = (f"VERDICT: {verdict['verdict_bin']}\nG-null (kernel-OFF flat): "
           f"{'PASS' if gnull['G_null_pass'] else 'FAIL'}")
    ax[1].text(0.02, 0.02, txt, transform=ax[1].transAxes, fontsize=7.5, va="bottom",
               bbox=dict(boxstyle="round", fc="white", ec="#999999", alpha=0.9))

    fig.tight_layout()
    out_png = sim_output("qed_trace_beta_gate.png")
    fig.savefig(out_png, dpi=150, bbox_inches="tight")
    print(f"[qed-trace] wrote {out_png}")


if __name__ == "__main__":
    main()

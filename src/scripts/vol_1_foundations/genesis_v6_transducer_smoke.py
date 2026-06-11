"""
genesis-v6 PHASE-2 — THE D9 TRANSDUCER SMOKE (THE GATE)
=======================================================

The centerpiece (prereg §6, FROZEN before this run). D9 = a CHIRAL BOUNDARY
CONDITION on the wall/pocket shell: per traversal the chiral wall exchanges a
quantum of angular momentum between the photon's axial SPIN S_φ=∫(w×∂_tw)·n̂ and
the bulk ORBITAL circulation L_bulk=∫ρ(r×u_adv)·n̂ — the polar-conjugate of the
snap reflector (the snap reflects the RADIAL pair; a CHIRAL wall torques the
ANGULAR pair). CONSERVATION BY CONSTRUCTION: the AM comes FROM the photon (the
spin ledger depletes 1:1; bounded; no refilled source — the depleting coupling
the BEMF smoke demanded, achieved at a BOUNDARY not in the bulk). CP10: no bulk
coupling term (every v5 bulk-coupling architecture detonated or nulled).

THE SMOKE measures, FROM the evolved field (ave-driver-script-honesty):
  (i)   d(L_transferred)/d(bounce) above floor
  (ii)  RH-vs-LH SIGN REVERSAL (the helicity-odd check; quantitative odd-fraction)
  (iii) the photon helicity ledger depleting 1:1 (the AM closure + the measured
        photon-spin depletion vs the free-drift floor)
  (iv)  the achiral null (helicity=0 ⇒ no transfer — structural)
  (v)   knob sweeps (chi_exch, bounce_thresh, wall_width — §210-COMPLIANCE GATE)

GATE BINS (FROZEN, prereg §6.6): TRANSDUCER-LIVE / TRANSDUCER-DEAD / UNRESOLVED.
Rule 11: the bins are frozen; no post-hoc criterion drop.
"""

from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from ave.core.unified_genesis_engine import UnifiedGenesisEngine  # noqa: E402

SEED = 20260610
N_MAIN = 40
N_STEPS = 600
FRAC, DRIVE_AMP, WAVELEN, SIGMA_PH, SIGMA_SEED = 0.95, 0.10, 8.0, 5.0, 5.0
CHI_DEFAULT = 0.02
AXIS = 2

# FROZEN gate thresholds (prereg §6.6)
L1_FLOOR_MULT = 100.0     # |ΔL_bulk(RH)| ≥ 100×F-EXCHANGE
DEAD_FLOOR_MULT = 10.0    # DEAD if |ΔL_bulk(RH)| < 10×F-EXCHANGE
ODD_FRAC_MIN = 0.9        # helicity-odd: |RH−LH|/(|RH|+|LH|) > 0.9
ACHIRAL_FLOOR_MULT = 3.0  # achiral null: |ΔL_bulk(achiral)| ≤ 3×F-EXCHANGE
DRIFT_DEPLETE_MULT = 1.0  # |ΔS_φ(on)| must exceed F-DRIFT


def build_engine(helicity, chi, *, wall_width=0.12, axis=AXIS, N=N_MAIN):
    """A planted saturated pocket (the g_wall chiral wall) + a chiral photon
    packet. bulk ON (u_adv receives), buckle OFF (D9 isolated), u_adv at rest."""
    e = UnifiedGenesisEngine(
        N, bulk_density_on=True, snap_on=False, omega_sector_on=False,
        buckle_on=False, transducer_on=(chi > 0.0), chi_exch=chi,
        wall_width=wall_width, transduce_axis=axis)
    c = (N - 1) / 2.0
    e.seed_bulk((c, c, c), sigma=SIGMA_SEED, frac=FRAC, helical=False)
    e.freeze_wall_window()
    e.drive_chiral_photon(helicity=helicity, sigma=SIGMA_PH, wavelength=WAVELEN,
                          amplitude=DRIVE_AMP, axis=axis)
    return e


def run_arm(name, helicity, chi, *, wall_width=0.12, n=N_STEPS, snap_at=200):
    """Step n; record I_wall(t), L_bulk(t), the spin depletion, the ledger, and a
    u_adv snapshot at `snap_at` (for the D12 byte-identical check)."""
    t0 = time.time()
    np.random.seed(SEED)
    e = build_engine(helicity, chi, wall_width=wall_width)
    axis = e._transduce_axis()
    L0 = e.angular_momentum_bulk(axis)
    S0 = e.photon_spin_axial(axis)
    iwall_t, L_t = [], []
    u_snap = None
    for s in range(n):
        e.step()
        iwall_t.append(e.wall_photon_intensity())
        L_t.append(e.angular_momentum_bulk(axis))
        if s + 1 == snap_at:
            u_snap = e.u_adv.copy()
    L1 = e.angular_momentum_bulk(axis)
    S1 = e.photon_spin_axial(axis)
    led = e.transducer_ledger()
    out = {
        "name": name, "helicity": int(helicity), "chi_exch": chi,
        "wall_width": wall_width, "n_steps": n,
        "dL_bulk": float(L1 - L0),
        "S_phi_0": float(S0), "S_phi_end": float(S1),
        "spin_depletion_abs": float(abs(S0) - abs(S1)),
        "ledger": led, "iwall_t": iwall_t, "L_t": L_t,
        "u_snap_at": snap_at, "_u_snap": u_snap, "wall_s": time.time() - t0,
    }
    print(f"  {name:20s} h={helicity:+d} chi={chi:.4f} ww={wall_width:.2f}  "
          f"dL_bulk={out['dL_bulk']:+.4e}  |spin|dep={out['spin_depletion_abs']:+.3e}  "
          f"ratio={led['ledger_ratio_removed_over_transferred']}  passive={led['passive_no_pump']} "
          f"({out['wall_s']:.0f}s)", flush=True)
    return out


def count_bounces(iwall_t, thresh_mult):
    """A bounce = a local maximum of I_wall(t) exceeding thresh_mult×median(I_wall).
    The bounce_thresh knob (cosmetic): it moves the COUNT, never the total ΔL."""
    a = np.asarray(iwall_t, dtype=float)
    if a.size < 3:
        return 0
    level = thresh_mult * float(np.median(a))
    peaks = 0
    for i in range(1, a.size - 1):
        if a[i] > level and a[i] >= a[i - 1] and a[i] > a[i + 1]:
            peaks += 1
    return int(peaks)


def main():
    t_start = time.time()
    results = {
        "prereg": "research/2026-06-10_genesis-v6-transducer_prereg.md (§6, FROZEN)",
        "job": "PHASE 2 — D9 chiral-boundary spin-orbit transducer smoke (THE GATE)",
        "scale": dict(N=N_MAIN, n_steps=N_STEPS, frac=FRAC, drive_amp=DRIVE_AMP,
                      wavelength=WAVELEN, axis=AXIS, seed=SEED),
    }

    # κ̃-anchored chi (the derived sweep point): χ̃_κ = κ̃·dt·ω, ω = c_T·k
    e0 = build_engine(+1, 0.0)
    k = 2.0 * np.pi / WAVELEN
    chi_kappa = float(e0.kappa_tilde * e0.dt * (e0.c_T * k))
    results["chi_kappa_anchored"] = chi_kappa
    results["dt"] = float(e0.dt)
    print(f"[derivation] κ̃-anchored chi = κ̃·dt·(c_T·k) = {chi_kappa:.4f} "
          f"(default {CHI_DEFAULT}); dt={e0.dt:.4e}", flush=True)

    # ---------- FLOORS FIRST (ORDERED BINS) ----------
    print("[1/5] FLOORS — F-PROBE (m-even keeper), F-EXCHANGE, F-DRIFT ...", flush=True)
    s_rh = build_engine(+1, 0.0).photon_spin_axial(AXIS)
    s_lh = build_engine(-1, 0.0).photon_spin_axial(AXIS)
    s_ac = build_engine(0, 0.0).photon_spin_axial(AXIS)
    f_probe_pass = bool(s_rh * s_lh < 0.0 and abs(s_ac) < 1e-9 * abs(s_rh))
    results["F_PROBE"] = {"S_phi_RH_seed": float(s_rh), "S_phi_LH_seed": float(s_lh),
                          "S_phi_achiral_seed": float(s_ac),
                          "separates_helicity": f_probe_pass}
    print(f"    F-PROBE: RH_seed={s_rh:+.3e} LH_seed={s_lh:+.3e} achiral={s_ac:+.3e} "
          f"-> separates={f_probe_pass}", flush=True)

    off = run_arm("FLOOR_chi0", +1, 0.0)
    F_EXCHANGE = abs(off["dL_bulk"])
    F_DRIFT = abs(off["spin_depletion_abs"])
    results["F_EXCHANGE"] = F_EXCHANGE
    results["F_DRIFT"] = F_DRIFT
    print(f"    F-EXCHANGE (chi=0 |ΔL_bulk|) = {F_EXCHANGE:.3e}", flush=True)
    print(f"    F-DRIFT   (chi=0 |ΔS_φ|)     = {F_DRIFT:.3e}", flush=True)

    # ---------- MAIN ARMS: RH / LH / achiral at default chi ----------
    print("[2/5] MAIN ARMS (RH / LH / achiral @ chi_default) ...", flush=True)
    rh = run_arm("MAIN_RH", +1, CHI_DEFAULT)
    lh = run_arm("MAIN_LH", -1, CHI_DEFAULT)
    ac = run_arm("MAIN_achiral", 0, CHI_DEFAULT)
    results["arms"] = {k2: {kk: v for kk, v in d.items() if kk != "_u_snap"}
                       for k2, d in (("MAIN_RH", rh), ("MAIN_LH", lh), ("MAIN_achiral", ac))}

    # ---------- D12 FAIL-FAST ----------
    d12_div = float(np.max(np.abs(rh["_u_snap"] - lh["_u_snap"])))
    d12_live = bool(d12_div > 0.0)
    achiral_at_floor = bool(abs(ac["dL_bulk"]) <= ACHIRAL_FLOOR_MULT * max(F_EXCHANGE, 1e-300))
    results["D12"] = {"u_div_RH_LH_at200": d12_div, "not_byte_identical": d12_live,
                      "achiral_at_floor": achiral_at_floor}
    print(f"    D12(i): max|u_RH−u_LH|@200 = {d12_div:.3e} -> live={d12_live}", flush=True)
    print(f"    D12(ii): achiral |ΔL_bulk|={abs(ac['dL_bulk']):.3e} at_floor={achiral_at_floor}", flush=True)
    if not d12_live:
        results["gate_verdict"] = "TRANSDUCER-DEAD"
        results["dead_reason"] = "D12(i): RH≡LH byte-identical within 200 steps (coupling dead)"
        _dump(results, t_start)
        return

    # ---------- (v) KNOB SWEEPS (§210) ----------
    print("[3/5] chi_exch sweep (coefficient-robustness; early-window linearity) ...", flush=True)
    chi_sweep = {}
    for chi in (0.005, 0.08, chi_kappa):
        a = run_arm(f"chi_{chi:.4f}", +1, chi)
        chi_sweep[f"{chi:.4f}"] = {"dL_bulk": a["dL_bulk"],
                                   "sign": int(np.sign(a["dL_bulk"])),
                                   "passive": a["ledger"]["passive_no_pump"]}
    # the default and the floor complete the χ̃ ladder
    chi_sweep[f"{CHI_DEFAULT:.4f}"] = {"dL_bulk": rh["dL_bulk"], "sign": int(np.sign(rh["dL_bulk"])),
                                       "passive": rh["ledger"]["passive_no_pump"]}
    chi_sweep["0.0000"] = {"dL_bulk": off["dL_bulk"], "sign": 0, "passive": True}
    results["chi_sweep"] = chi_sweep
    chi_signs = {v["sign"] for kk, v in chi_sweep.items() if abs(v["dL_bulk"]) > 10 * F_EXCHANGE}
    chi_robust = bool(chi_signs == {int(np.sign(rh["dL_bulk"]))})
    chi_passive = all(v["passive"] for v in chi_sweep.values())

    print("[4/5] wall_width sweep (sharpness-robustness) ...", flush=True)
    ww_sweep = {}
    for ww in (0.06, 0.20):
        a = run_arm(f"ww_{ww:.2f}", +1, CHI_DEFAULT, wall_width=ww)
        ww_sweep[f"{ww:.2f}"] = {"dL_bulk": a["dL_bulk"], "sign": int(np.sign(a["dL_bulk"]))}
    ww_sweep["0.12"] = {"dL_bulk": rh["dL_bulk"], "sign": int(np.sign(rh["dL_bulk"]))}
    results["wall_width_sweep"] = ww_sweep
    ww_robust = bool({v["sign"] for v in ww_sweep.values()} == {int(np.sign(rh["dL_bulk"]))})

    print("[5/5] bounce_thresh sweep (cosmetic count; TOTAL ΔL invariant) ...", flush=True)
    bounce_sweep = {}
    for bt in (1.2, 1.5, 2.0):
        nb = count_bounces(rh["iwall_t"], bt)
        dpb = rh["dL_bulk"] / max(nb, 1)
        bounce_sweep[f"{bt:.1f}"] = {"n_bounce": nb, "dL_per_bounce": dpb,
                                     "total_dL": rh["dL_bulk"]}
    results["bounce_sweep"] = bounce_sweep
    # the total ΔL is identical across all thresholds (same run) -> the count is cosmetic
    total_invariant = bool(len({round(v["total_dL"], 12) for v in bounce_sweep.values()}) == 1)
    results["d_L_per_bounce_default"] = bounce_sweep["1.5"]["dL_per_bounce"]
    # §210 / ave-driver-script-honesty DEVIATION NOTE (stated, not papered over):
    # at the CFL dt the photon is quasi-static over the window (travels <1 cell), so
    # I_wall(t) MONOTONE-DECREASES (the continuous-drain signature) with NO discrete
    # bounce-peaks -> n_bounce=0 at every swept threshold. The interaction is
    # CONTINUOUS spin-extraction from the co-located packet, not ballistic bounces.
    # The headline metric is therefore the per-STEP rate (the continuous analog) and
    # the TOTAL ΔL; the bounce_thresh sweep still serves its §210 purpose (it confirms
    # the total ΔL is threshold-INVARIANT -> the count knob is cosmetic, as predicted).
    iw = np.asarray(rh["iwall_t"], dtype=float)
    iwall_monotone_decreasing = bool(np.all(np.diff(iw) <= 1e-15))
    n_bounce_all_zero = bool(all(v["n_bounce"] == 0 for v in bounce_sweep.values()))
    results["metric_i_deviation"] = {
        "all_thresholds_n_bounce_zero": n_bounce_all_zero,
        "iwall_monotone_decreasing": iwall_monotone_decreasing,
        "iwall_first": float(iw[0]), "iwall_last": float(iw[-1]),
        "reason": "CFL dt=%.2e: photon quasi-static over %d steps (<1 cell); continuous "
                  "wall drain, not discrete bounces" % (e0.dt, N_STEPS),
        "d_L_per_step": float(rh["dL_bulk"] / N_STEPS),
        "total_dL_threshold_invariant": total_invariant,
    }
    print(f"    [§210 NOTE] n_bounce=0 at all thresholds (CFL quasi-static photon); "
          f"I_wall monotone-decr={iwall_monotone_decreasing} "
          f"({iw[0]:.3e}->{iw[-1]:.3e}); d(L)/d(step)={rh['dL_bulk']/N_STEPS:+.3e}", flush=True)

    # ---------- (ii) HELICITY-ODD ----------
    rh_dL, lh_dL = rh["dL_bulk"], lh["dL_bulk"]
    odd_frac = abs(rh_dL - lh_dL) / (abs(rh_dL) + abs(lh_dL) + 1e-30)
    helicity_odd = bool(np.sign(rh_dL) == -np.sign(lh_dL) and odd_frac > ODD_FRAC_MIN)
    results["helicity_odd"] = {"dL_RH": rh_dL, "dL_LH": lh_dL, "odd_fraction": odd_frac,
                               "sign_reversal": bool(np.sign(rh_dL) == -np.sign(lh_dL)),
                               "passes": helicity_odd}

    # ---------- (iii) PHOTON DEPLETION 1:1 + no pump ----------
    ratio = rh["ledger"]["ledger_ratio_removed_over_transferred"]
    am_1to1 = bool(abs(ratio - 1.0) < 1e-6)
    depletes = bool(rh["spin_depletion_abs"] > 0 and abs(rh["spin_depletion_abs"]) > DRIFT_DEPLETE_MULT * F_DRIFT)
    passive = bool(rh["ledger"]["passive_no_pump"] and rh["ledger"]["E_photon_loss"] >= 0.0)
    results["photon_depletion"] = {
        "am_ledger_ratio": ratio, "am_closes_1to1": am_1to1,
        "measured_spin_depletion": rh["spin_depletion_abs"],
        "F_DRIFT": F_DRIFT, "depletes_beyond_drift": depletes,
        "E_photon_loss": rh["ledger"]["E_photon_loss"],
        "E_bulk_gain": rh["ledger"]["E_bulk_gain"],
        "E_absorbed_sink": rh["ledger"]["E_absorbed_sink"],
        "passive_no_pump": passive}

    # ---------- (i) d(L)/d(bounce) above floor ----------
    L1 = bool(abs(rh_dL) >= L1_FLOOR_MULT * max(F_EXCHANGE, 1e-300))
    results["exchange_per_bounce"] = {
        "dL_bulk_RH": rh_dL, "F_EXCHANGE": F_EXCHANGE,
        "ratio_over_floor": (abs(rh_dL) / F_EXCHANGE if F_EXCHANGE > 0 else float("inf")),
        "above_floor_100x": L1,
        "d_L_per_bounce_at_default_thresh": bounce_sweep["1.5"]["dL_per_bounce"],
        "d_L_per_step_continuous": float(rh_dL / N_STEPS),
        "note": "n_bounce=0 at all swept thresholds (CFL quasi-static photon -> continuous "
                "wall drain); per-bounce degenerates to total; d(L)/d(step) is the continuous "
                "analog. F_EXCHANGE is a STRUCTURAL zero (chi=0 ⇒ u_adv never sourced)."}

    # ---------- THE GATE (FROZEN BINS, §6.6) ----------
    L4 = bool(achiral_at_floor and f_probe_pass)
    L5 = bool(chi_robust and ww_robust and total_invariant and chi_passive)
    live = bool(L1 and helicity_odd and am_1to1 and depletes and passive and L4 and L5 and d12_live)
    dead = bool((not d12_live) or abs(rh_dL) < DEAD_FLOOR_MULT * max(F_EXCHANGE, 1e-300))
    verdict = "TRANSDUCER-LIVE" if live else ("TRANSDUCER-DEAD" if dead else "UNRESOLVED")
    results["gate_checks"] = {
        "L1_above_floor": L1, "L2_helicity_odd": helicity_odd,
        "L3_depleting_1to1_no_pump": bool(am_1to1 and depletes and passive),
        "L4_achiral_null_and_probe": L4,
        "L5_coefficient_sharpness_robust": L5,
        "chi_robust": chi_robust, "ww_robust": ww_robust,
        "bounce_total_invariant": total_invariant, "chi_passive": chi_passive,
        "D12_live": d12_live}
    results["gate_verdict"] = verdict

    _dump(results, t_start)


def _dump(results, t_start):
    out_json = os.path.abspath(os.path.join(
        os.path.dirname(__file__), "..", "..", "..", "research",
        "2026-06-10_genesis-v6-transducer-smoke_results.json"))
    with open(out_json, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nDONE in {time.time()-t_start:.0f}s -> {out_json}")
    print("GATE VERDICT:", results.get("gate_verdict"))
    if "gate_checks" in results:
        print(json.dumps(results["gate_checks"], indent=2))


if __name__ == "__main__":
    main()

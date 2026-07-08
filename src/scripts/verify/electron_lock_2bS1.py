#!/usr/bin/env python3
"""Driver — electron-lock 2b-Stage-1 BINDING test (parallel coupling-mode sweep).

Prereg (FROZEN): research/2026-07-07_electron-lock-2bS1_prereg_FROZEN.md
Result:          research/2026-07-07_electron-lock-2bS1_RESULT.md
Harness:         src/ave/solvers/electron_lock_2bS1.py

Runs the three PARALLEL ARMS (mutual_M / co_equal / coupling_varactor) at the
(2,3) tuning (ω_q/ω_d=3/2) with the golden-ratio can-fire control, plus the
firewall scan, the double-count reconcile-gate (with can-fire self-test), the
scale-invariance control, the DOESN'T-FILL control, and the tautology-detector
can-fire proof. Emits JSON + a house-WHITE figure; prints the per-arm bins and
the hierarchy adjudication. ZERO external drive throughout.

Reproduce:
    PYTHONPATH=src python src/scripts/verify/electron_lock_2bS1.py
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from ave.solvers.electron_lock_2bS1 import (
    FILL_THRESH,
    PHI,
    SUSTAIN_THRESH,
    V_YIELD_HAT,
    ArmParams,
    ArmResult,
    classify,
    firewall_scan,
    reconcile_q_cap_energy,
    run_arm,
)
from ave.viz import style

ARMS = ("mutual_M", "co_equal", "coupling_varactor")
INDUCTIVE = ("mutual_M", "co_equal")
_HERE = Path(__file__).resolve().parent


def _route(mode: str, ratio: float = 1.5, **kw) -> tuple[str, ArmResult, ArmResult]:
    main = run_arm(ArmParams(mode, ratio=ratio, **kw), n_common=120, keep_series=True)
    golden = run_arm(ArmParams(mode, ratio=PHI, **kw), n_common=120)
    return classify(main, golden), main, golden


def _res_row(r: ArmResult) -> dict:
    return {
        "mode": r.params.mode,
        "ratio": r.params.ratio,
        "fill_max": r.fill_max,
        "fill_mean": r.fill_mean,
        "fill_min": r.fill_min,
        "h_drift": r.h_drift,
        "lock_drift": r.lock_drift,
        "w_d": r.w_d,
        "w_q": r.w_q,
        "div_corr": r.div_corr,
        "t_fill_frac": r.t_fill_frac if np.isfinite(r.t_fill_frac) else None,
        "ruptured": r.ruptured,
    }


def main() -> None:
    style.apply("print")
    out: dict = {"thresholds": {"FILL": FILL_THRESH, "SUSTAIN": SUSTAIN_THRESH}, "arms": {}, "controls": {}}

    # ── firewall (prereg §4) ────────────────────────────────────────────────
    fw = firewall_scan()
    out["firewall"] = fw
    assert fw["clean"], f"FIREWALL VIOLATION: {fw['hits']}"

    # ── the three arms at the (2,3) tuning + golden can-fire ────────────────
    print("=" * 78)
    print("ELECTRON-LOCK 2b-S1 — per-arm bins at (2,3) tuning (ω_q/ω_d=3/2), zero drive")
    print("=" * 78)
    series_32: dict[str, ArmResult] = {}
    for mode in ARMS:
        b, main_r, gold_r = _route(mode)
        series_32[mode] = main_r
        # double-count reconcile-gate (independent q-cap-energy recompute, can-fire proven)
        gate = reconcile_q_cap_energy(main_r.params)
        out["arms"][mode] = {
            "bin": b,
            "main": _res_row(main_r),
            "golden": _res_row(gold_r),
            "q_cap_reconcile": gate.as_dict(),
        }
        print(
            f"  {mode:<18s} -> {b:<18s}  fill(max/mean/min)={main_r.fill_max:.3f}/"
            f"{main_r.fill_mean:.3f}/{main_r.fill_min:.3f}  Hdrift={main_r.h_drift:.1e}  "
            f"w=({main_r.w_d:.0f},{main_r.w_q:.0f})  q-cap-reconcile={'PASS' if gate.passed else 'FAIL'}"
        )

    # ── controls (prereg §7, §10) ───────────────────────────────────────────
    ctl = out["controls"]

    # DOESN'T-FILL control: uncoupled
    b0, r0, g0 = _route("mutual_M", kappa=0.0)
    ctl["uncoupled_doesnt_fill"] = {"bin": b0, "fill_max": r0.fill_max}

    # scale-invariance: v_yield_hat x2 must not change the bin (α-echo magnitude excluded)
    ctl["scale_invariance"] = {}
    for mode in INDUCTIVE:
        b1, _, _ = _route(mode)
        b2, _, _ = _route(mode, v_yield_hat=2.0 * V_YIELD_HAT)
        ctl["scale_invariance"][mode] = {"v_yield_hat": b1, "v_yield_hat_x2": b2, "invariant": b1 == b2}

    # robustness: kappa x{0.7,1.4}, seed{0.2,0.4}
    ctl["robustness"] = {}
    for mode in INDUCTIVE:
        rows = {}
        for kf in (0.7, 1.4):
            rows[f"kappa_x{kf}"] = _route(mode, kappa=0.15 * kf)[0]
        for sf in (0.2, 0.4):
            rows[f"seed_{sf}"] = _route(mode, seed_frac=sf)[0]
        ctl["robustness"][mode] = rows

    # tautology-detector CAN-FIRE proof: a strong bridging cap MUST route TAUTOLOGY
    ctl["tautology_can_fire"] = {}
    for cf in (0.30, 2.0, 6.0):
        b, rm, rg = _route("coupling_varactor", c_frac=cf)
        ctl["tautology_can_fire"][f"c_frac_{cf}"] = {"bin": b, "div_corr": rm.div_corr, "fill_max": rm.fill_max}

    # FILLS-AND-SUSTAINS bin reachability (liveness — not dead plumbing)
    p = ArmParams("mutual_M", ratio=1.5)
    good = ArmResult(p, 0.3, 0.2, 0.08, 0.001, 0.4, 240, 360, 0.1, 2.0, False)
    gold = ArmResult(p, 0.01, 0.004, 0.0, 0.001, 180.0, 240, 388, 0.1, float("inf"), False)
    ctl["fills_and_sustains_reachable"] = classify(good, gold) == "FILLS-AND-SUSTAINS"

    # ── adjudication (prereg §8) ────────────────────────────────────────────
    bins = {m: out["arms"][m]["bin"] for m in ARMS}
    m_sus = bins["mutual_M"] == "FILLS-AND-SUSTAINS"
    c_sus = bins["co_equal"] == "FILLS-AND-SUSTAINS"
    if m_sus and not c_sus:
        verdict = "BIAS-HIERARCHY REAL (mutual_M fills+sustains, co_equal does not)"
    elif c_sus and not m_sus:
        verdict = "TWO-MODE RESONANCE (co_equal fills+sustains, mutual_M does not)"
    elif c_sus and m_sus:
        verdict = "BOTH WORK (both inductive arms fill+sustain)"
    else:
        verdict = "REACTIVE-PUMP CANDIDATE DEAD — the '3' needs a NON-reactive mechanism"
    out["adjudication"] = {"bins": bins, "verdict": verdict}

    print("-" * 78)
    print(f"  ADJUDICATION: {verdict}")
    print(
        f"  controls: DOESN'T-FILL={ctl['uncoupled_doesnt_fill']['bin']} | "
        f"FILLS-AND-SUSTAINS reachable={ctl['fills_and_sustains_reachable']} | "
        f"tautology can-fire c=6.0 -> {ctl['tautology_can_fire']['c_frac_6.0']['bin']}"
    )

    # ── figure (house-WHITE) ────────────────────────────────────────────────
    fig, (axL, axR) = plt.subplots(1, 2, figsize=style.figsize("wide"))
    colors = dict(zip(ARMS, style._PROP_CYCLE[:3]))
    # left: rolling MIN / MAX envelope of the q-tank fill over one (2,3) common
    # period. The MIN envelope hugging zero = the q-tank empties every beat
    # (reactive borrow/return) — the visual signature of FILLS-BUT-DECAYS.
    def _rolling(a: np.ndarray, w: int, fn) -> np.ndarray:
        w = max(1, w)
        return np.array([fn(a[i : i + w]) for i in range(0, len(a) - w + 1, max(1, w // 4))])

    for mode in ARMS:
        s = series_32[mode].series
        t = s["t"] / (2 * np.pi)  # in units of T_d
        win = int(round(2.0 * (2 * np.pi) / (t[1] - t[0]) / (2 * np.pi)))  # ~1 T_common in samples
        win = max(10, len(s["eq_frac"]) // 120)
        tt = _rolling(t, win, lambda z: z[len(z) // 2])
        emax = _rolling(s["eq_frac"], win, np.max)
        emin = _rolling(s["eq_frac"], win, np.min)
        axL.fill_between(tt, emin, emax, color=colors[mode], alpha=0.25, lw=0)
        axL.plot(tt, emax, lw=1.1, color=colors[mode], label=f"{mode} (env)")
        axL.plot(tt, emin, lw=1.1, ls="--", color=colors[mode])
    axL.axhline(FILL_THRESH, ls="--", lw=1.0, color="0.35")
    axL.axhline(SUSTAIN_THRESH, ls=":", lw=1.0, color="0.55")
    axL.set_xlabel(style.axis_label("Time", r"t/T_d", ""))
    axL.set_ylabel(style.axis_label("q-tank fill envelope", r"E_q/H_0", ""))
    style.legend(axL, where="right")
    # right: fill_max / mean / min per arm vs the thresholds (fills but min->0 = decays)
    x = np.arange(len(ARMS))
    w = 0.26
    fmax = [series_32[m].fill_max for m in ARMS]
    fmean = [series_32[m].fill_mean for m in ARMS]
    fmin = [series_32[m].fill_min for m in ARMS]
    axR.bar(x - w, fmax, w, label=r"$\max$", color=style._PROP_CYCLE[0])
    axR.bar(x, fmean, w, label=r"back-half $\langle\cdot\rangle$", color=style._PROP_CYCLE[1])
    axR.bar(x + w, fmin, w, label=r"back-half $\min$", color=style._PROP_CYCLE[3])
    axR.axhline(FILL_THRESH, ls="--", lw=1.0, color="0.35")
    axR.axhline(SUSTAIN_THRESH, ls=":", lw=1.0, color="0.55")
    axR.set_xticks(x)
    axR.set_xticklabels([m.replace("_", "\n") for m in ARMS], fontsize=8)
    axR.set_ylabel(style.axis_label("q-tank energy fraction", r"E_q/H_0", ""))
    style.legend(axR, where="right")

    fig_path = _HERE / "electron_lock_2bS1_fill.png"
    style.save(fig, fig_path, strict=True)
    out["figure"] = str(fig_path.name)

    json_path = _HERE / "electron_lock_2bS1_results.json"
    json_path.write_text(json.dumps(out, indent=2))
    print(f"  wrote {json_path.name} + {fig_path.name}")


if __name__ == "__main__":
    main()

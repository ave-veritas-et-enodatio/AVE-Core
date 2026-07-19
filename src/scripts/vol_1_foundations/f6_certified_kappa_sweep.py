#!/usr/bin/env python3
"""F6 certified-κ recurrence sweep — the SUFFICIENT test of the counting arrow.

Prereg (FROZEN): research/2026-07-18_f6-certified-kappa-sweep_prereg_FROZEN.md
  frozen-by-push 2026-07-19T16:16:32Z (API committedDate), BEFORE this driver.
Charters:        research/2026-07-15_f6-mode-count-door_CHARTER.md (bin (i), §5b)
                 research/2026-07-16_f6-bath-meter_CHARTER.md (§A/§B/§C + §C-post)
Certificate:     research/2026-07-18_f6-meter-kappa-reval_result.md
                 → METER-VALID-KAPPA-BAND[0.030,0.030] at MILD (the certified cell).
Instrument:      src/ave/thermal/f6_bath_meter.py (LatticeBathCoupler — BYTE-UNTOUCHED).
Reused (BYTE-UNTOUCHED): f6_counting_arrow_arm.py (#722 machinery: _build/_seed/grid),
                 f6_bath_meter_validate.py (#724 FROZEN placement _place_detuned_band).

SECTOR / REGIME (mandatory header):
  Sector    : E-sector ε-store (F6 ε→T2 candidate). NOT A1 mass, NOT Cosserat (2,3).
  Mode      : reactive K4 TLM lattice + external Foster comb bank (Caldeira-Leggett).
  Regime    : Regime I sub-yield, A_max≈0.10 MILD, at the CERTIFIED κ=0.030 EXACTLY.
  Phase-st. : driven-then-source-off, closed cavity (pml=0, energy-conserving).
  Plant     : STANDALONE-K4 — within the meter certificate (#721 R-1 SCOPE CAVEAT).
  Coord.    : R_return = scalar energy ledger; x = T·Δω/2π is SPECTRAL (A46-matched).

THE SUFFICIENT TEST. The #722 review-probe found the NECESSARY counting SHAPE at
κ=0.030 (fast transfer, quasi-continuum populating, dense R_cum≈0 with controls
passing). This sweep tests the SUFFICIENT SIGNATURE: do the R_return(x) curves
COLLAPSE in x = T_window·Δω/2π with the transition at x≈1 AND NOWHERE ELSE? A finite
lossless comb (spacing Δω) recurs exactly at T_rec = 2π/Δω, independent of M and
ω_min; the arrow is a Poincaré horizon-crossing (T_window < T_rec). If it is genuine
counting, T_rec is the ONLY return timescale ⇒ the curves collapse in x.

NO Re(Z) ELEMENT EXISTS ANYWHERE (the no-valve rail): comb lossless (friction=False),
symplectic CL kick + exact free rotation, back-reaction = phase-preserving energy-
matched rescale. Any real input resistance is EMERGENT FROM COUNTING.

Run: PYTHONPATH=src python src/scripts/vol_1_foundations/f6_certified_kappa_sweep.py \
        [--json] [--companion] [--self-check]
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, field

import numpy as np

# ── #724 FROZEN detuned-band placement (BYTE-UNTOUCHED import; prereg §7) ─────
from scripts.vol_1_foundations.f6_bath_meter_validate import (
    DELTA_OMEGA as DETUNE_DW,  # 0.030 — the frozen detuned-probe spacing
)
from scripts.vol_1_foundations.f6_bath_meter_validate import (
    DETUNE_M,  # 32 — the frozen detuned-probe mode count
    _place_detuned_band,
    _q_spectrum,
)

# ── #722 arm machinery (BYTE-UNTOUCHED import) ───────────────────────────────
from scripts.vol_1_foundations.f6_counting_arrow_arm import (
    DELTA_OMEGA_SWEEP,
    DENSE_MAX_DW,
    DT,
    HORIZON_RECURRENCES,
    OMEGA_MIN,
    TWO_TANK_DW,
    TWO_TANK_M,
    TWO_TANK_OMEGA_MIN,
    TWO_TANK_RECURRENCES,
    X_TABLE,
    _build,
    _m_for,
    run_companion,  # SECONDARY / non-gating (prereg §6) — reused verbatim
)

# ── THE CERTIFIED CELL (prereg §0/§3; the ONLY point this lane fires) ─────────
KAPPA_SWEEP = 0.030          # κ=0.030 EXACTLY — the single certified point [0.030,0.030]
SEED_SCALE_MILD = 0.6        # MILD, A_max≈0.10 — the certified operating point
DETUNE_SOUL_STEPS = 3000     # detuned-control window (matches the certified X2 soul-check)

# ── FROZEN verdict thresholds (prereg §4; DERIVED / inherited — no tuning) ────
CONS_TOL = 1e-3              # door bin (ii); identity holds ≪ this
T63_GATE = 0.5              # DERIVED regime gate: transfer ≥63%-done by the half-recurrence
NOCC_GATE = 10              # DERIVED regime gate: populated quasi-continuum (probe's 15)
E_BATH_MIN = 1e-2          # NULL / no-transfer floor; also the detuned-control gate
SPARSE_RETURN_MIN = 0.70   # sparse-control / grid-wide return-by-x=10
COLLAPSE_SPREAD_MAX = 0.30  # spread(x_50)
TRANSITION_LO, TRANSITION_HI = 0.7, 1.5  # mean(x_50) window bracketing x=1
DENSE_PLATEAU_MAX = 0.30   # dense R_return(x=0.3)
OFF_DRIFT_MAX = 1e-10      # OFF recovers Ax3
BIAS_TARE_TOL = 0.05       # core-bias (tared)
R_HALF = 0.5               # cumulative-return crossing level for x_50
INV_E = 1.0 - 1.0 / np.e   # 63% level for t63

DENSEST_DW = 0.010         # the densest comb — the regime-gate + X1/X5/X6 primary plant


# ── one comb run: sweep result + folded regime diagnostics (prereg §6) ───────
@dataclass
class CombResult:
    delta_omega: float
    M: int
    omega_max: float
    t_rec: float
    n_steps: int
    e0: float
    e_bath_peak: float
    peak_frac: float          # E_bath_peak / E0 (transfer health / NULL)
    n_occ: int
    max_cons_drift: float     # max |E_lat+E_bath−E0|/E0 (identity audit)
    t63: int                  # first step E_bath ≥ (1−1/e)·peak (transfer timescale)
    t63_over_trec: float      # t63 / T_rec (the REGIME-gate observable at densest)
    x_50: float               # x at first R_ret_cum ≥ 0.5 (nan if never) — transition midpoint
    omega_d: float            # re-measured drive line (rFFT of collar q) — diagnostics provenance
    linewidth_fwhm: float     # half-power width of ω_d
    r_return_table: dict = field(default_factory=dict)  # x -> R_return (instantaneous)
    r_cum_table: dict = field(default_factory=dict)     # x -> R_ret_cum (monotone)
    # reactance pair (Rule-10 corollary): bath C-state Σ½ω²x² AND L-state Σ½p²
    # sampled ACROSS the window (11-point x-grid) — not a single-phase snapshot.
    ebath_c_table: dict = field(default_factory=dict)   # x -> C-state / E0
    ebath_l_table: dict = field(default_factory=dict)   # x -> L-state / E0
    ebath_c_at_peak: float = 0.0
    ebath_l_at_peak: float = 0.0


def run_comb(delta_omega: float, horizon_recurrences: int = HORIZON_RECURRENCES,
             omega_min: float = OMEGA_MIN, m: int | None = None) -> CombResult:
    """One comb at the CERTIFIED κ=0.030 MILD. Records E_lat/E_bath, the collar q(t),
    and the bath C/L reactance split; derives R_return(x), t63, x_50, ω_d/linewidth.
    """
    if m is None:
        m = _m_for(delta_omega)
    t_rec = 2 * np.pi / delta_omega
    n_steps = int(round(horizon_recurrences * t_rec))
    cpl = _build(delta_omega, m, omega_min=omega_min, kappa=KAPPA_SWEEP, scale=SEED_SCALE_MILD)
    e0 = cpl.e_lat()
    etot0 = e0 + cpl.e_bath()
    steps = np.arange(1, n_steps + 1)
    e_bath = np.empty(n_steps)
    ebc = np.empty(n_steps)   # bath C-state Σ½ω²x²
    ebl = np.empty(n_steps)   # bath L-state Σ½p²
    q_ts = np.empty(n_steps)  # collar drive the bath sees this step (diagnostics)
    max_drift = 0.0
    for k, i in enumerate(steps):
        q_ts[k] = cpl.read_q()
        cpl.step(int(i))
        e_bath[k] = cpl.e_bath()
        ebc[k] = float(0.5 * (cpl.bath.omega**2 * cpl.bath.x**2).sum())
        ebl[k] = float(0.5 * (cpl.bath.p**2).sum())
        max_drift = max(max_drift, abs((cpl.e_lat() + e_bath[k]) - etot0) / e0)
    x = steps * delta_omega / (2 * np.pi)
    e_bath_peak = float(e_bath.max())
    t_peak_k = int(np.argmax(e_bath))
    # t63 = first step E_bath ≥ (1−1/e)·peak (the transfer timescale)
    hit63 = np.nonzero(e_bath >= INV_E * e_bath_peak)[0]
    t63 = int(steps[hit63[0]]) if hit63.size else n_steps
    # R_return(t) = 1 − E_bath/E_bath_peak for t≥t_peak, else 0 (transfer incomplete)
    r_ret = np.where(np.arange(n_steps) >= t_peak_k, 1.0 - e_bath / max(e_bath_peak, 1e-30), 0.0)
    r_cum = np.maximum.accumulate(r_ret)
    hit = np.nonzero(r_cum >= R_HALF)[0]
    x_50 = float(x[hit[0]]) if hit.size else float("nan")
    # re-measured drive line (rFFT of collar q) — provenance, not prose (F9)
    power = np.abs(np.fft.rfft(q_ts - q_ts.mean())) ** 2
    freqs = 2 * np.pi * np.fft.rfftfreq(n_steps, d=DT)
    kmax = int(np.argmax(power[1:])) + 1
    omega_d = float(freqs[kmax])
    half = power[kmax] / 2.0
    lo, hi = kmax, kmax
    while lo > 1 and power[lo] > half:
        lo -= 1
    while hi < len(power) - 1 and power[hi] > half:
        hi += 1
    linewidth = float(freqs[hi] - freqs[lo])

    def _at(xt: float, arr: np.ndarray) -> float:
        return float(arr[int(np.argmin(np.abs(x - xt)))])

    return CombResult(
        delta_omega=delta_omega, M=m, omega_max=float(cpl.bath.omega[-1]), t_rec=t_rec,
        n_steps=n_steps, e0=e0, e_bath_peak=e_bath_peak, peak_frac=e_bath_peak / e0,
        n_occ=cpl.bath.n_occ(), max_cons_drift=max_drift, t63=t63,
        t63_over_trec=t63 / t_rec, x_50=x_50, omega_d=omega_d, linewidth_fwhm=linewidth,
        r_return_table={xt: _at(xt, r_ret) for xt in X_TABLE},
        r_cum_table={xt: _at(xt, r_cum) for xt in X_TABLE},
        ebath_c_table={xt: _at(xt, ebc) / e0 for xt in X_TABLE},
        ebath_l_table={xt: _at(xt, ebl) / e0 for xt in X_TABLE},
        ebath_c_at_peak=float(ebc[t_peak_k]) / e0, ebath_l_at_peak=float(ebl[t_peak_k]) / e0,
    )


def run_detuned_control() -> dict:
    """Resonance-gating negative control (prereg §3/§7; the #724 F2 lesson).

    Record q(t) from the densest RESONANT plant, place a detuned comb OFF the plant's
    own measured q-power content via the FROZEN q-power-budget rule _place_detuned_band
    (NOT the harmonic-avoidance F1-bug helper), run it, and require negligible transfer
    (peak_frac < E_BATH_MIN) — i.e. the sweep's transfer is RESONANCE-GATED, not a
    broadband dump. Reproduces the certified X2 placement.
    """
    m = _m_for(DENSEST_DW)
    res = _build(DENSEST_DW, m, omega_min=OMEGA_MIN, kappa=KAPPA_SWEEP, scale=SEED_SCALE_MILD)
    e0 = res.e_lat()
    qs = np.empty(DETUNE_SOUL_STEPS)
    for k in range(DETUNE_SOUL_STEPS):
        qs[k] = res.read_q()
        res.step(k + 1)
    freqs, psd, dom, cum = _q_spectrum(qs)
    om_min_det, om_max_det, band_frac, omega_99 = _place_detuned_band(freqs, psd, cum)
    det = _build(DETUNE_DW, DETUNE_M, omega_min=om_min_det, kappa=KAPPA_SWEEP, scale=SEED_SCALE_MILD)
    e0_det = det.e_lat()
    e_bath_det = 0.0
    for k in range(DETUNE_SOUL_STEPS):
        det.step(k + 1)
        e_bath_det = max(e_bath_det, det.e_bath())
    peak_frac = e_bath_det / e0_det
    return {
        "omega_d_qspec": dom, "omega_99": omega_99,
        "detuned_band": [om_min_det, om_max_det], "band_power_frac": band_frac,
        "detune_m": DETUNE_M, "detune_dw": DETUNE_DW,
        "e0_resonant": e0, "n_occ_det": det.bath.n_occ(),
        "peak_frac": peak_frac, "gated": bool(peak_frac < E_BATH_MIN),
        "note": "FROZEN _place_detuned_band (q-power-budget; §7); gated ⇒ transfer is "
                "resonance-gated, not a broadband dump (the #724 F2 guard).",
    }


def run_off_control() -> float:
    """κ=0 closed-cavity drift over 200 steps (OFF recovers Ax3; κ-independent)."""
    cpl = _build(0.03, _m_for(0.03), kappa=0.0, scale=SEED_SCALE_MILD)
    e0 = cpl.e_lat()
    for i in range(1, 201):
        cpl.step(i)
    return abs(cpl.e_lat() - e0) / e0


def run_bias_tare() -> dict:
    """Protected-core bias ON(κ=0.030) vs OFF(κ=0), tared by c=√(1−E_bath/E0) (§4·8)."""
    dw = 0.03
    on = _build(dw, _m_for(dw), kappa=KAPPA_SWEEP, scale=SEED_SCALE_MILD)
    off = _build(dw, _m_for(dw), kappa=0.0, scale=SEED_SCALE_MILD)
    e0 = on.e_lat()
    for i in range(1, 201):
        on.step(i)
        off.step(i)

    def _amax(c):
        v = np.sqrt(np.sum(c.lat.V_inc**2, axis=-1))
        return float(v[c.lat.mask_active].max())

    a_on, a_off = _amax(on), _amax(off)
    c = float(np.sqrt(max(1.0 - on.e_bath() / e0, 0.0)))
    resid = abs(a_on - c * a_off) / max(a_off, 1e-30)
    return {"a_on": a_on, "a_off": a_off, "tare_c": c, "resid": resid,
            "ok": bool(resid < BIAS_TARE_TOL)}


# ── FROZEN classifier — prereg §4 decision tree, BYTE-FAITHFUL (Rule 11) ──────
def classify(sweep: list[CombResult], two_tank: CombResult, off_drift: float,
             bias: dict, det: dict) -> tuple[str, dict]:
    """Implements prereg §4's COMPLETE tree with the frozen precedence 1→6. No retune."""
    densest = min(sweep, key=lambda r: r.delta_omega)
    sparsest = max(sweep, key=lambda r: r.delta_omega)
    dense = [r for r in sweep if r.delta_omega <= DENSE_MAX_DW]

    # aggregates (all banked)
    max_cons = max(r.max_cons_drift for r in sweep + [two_tank])
    x50s = [r.x_50 for r in sweep if np.isfinite(r.x_50)]
    spread = (max(x50s) - min(x50s)) if len(x50s) >= 2 else float("nan")
    mean_x50 = float(np.mean(x50s)) if x50s else float("nan")
    # grid-wide return-by-x=10 (the #722 R-5 faithful FOREIGN-EATER: WHOLE grid, not narrowed)
    grid_returns = [r.r_cum_table[10.0] for r in sweep] + [two_tank.r_cum_table[10.0]]
    grid_return_min = min(grid_returns)
    dense_plateau = max((r.r_return_table[0.3] for r in dense), default=float("nan"))
    n_occ_dense = min(r.n_occ for r in dense) if dense else 0
    n_occ_sparse = sparsest.n_occ

    nan_seen = any(
        not np.isfinite(v)
        for r in sweep + [two_tank]
        for v in (r.max_cons_drift, r.e_bath_peak, r.peak_frac)
    )

    crit = {
        # regime gates (checked FIRST among physics)
        "t63_over_trec_densest": densest.t63_over_trec,
        "t63_gate_ok": bool(densest.t63_over_trec <= T63_GATE),
        "n_occ_densest": densest.n_occ,
        "nocc_gate_ok": bool(densest.n_occ >= NOCC_GATE),
        "peak_frac_densest": densest.peak_frac,
        "transfer_ok": bool(densest.peak_frac >= E_BATH_MIN),
        # ledger
        "max_cons": max_cons, "cons_ok": bool(max_cons < CONS_TOL), "nan_seen": bool(nan_seen),
        # collapse / transition
        "collapse_spread": spread,
        "collapse_ok": bool(np.isfinite(spread) and spread < COLLAPSE_SPREAD_MAX),
        "mean_x50": mean_x50,
        "transition_ok": bool(TRANSITION_LO <= mean_x50 <= TRANSITION_HI),
        # returns
        "grid_return_min": grid_return_min,
        "grid_return_ok": bool(grid_return_min >= SPARSE_RETURN_MIN),
        "two_tank_return": two_tank.r_cum_table[10.0],
        "sparsest_return": sparsest.r_cum_table[10.0],
        "controls_ok": bool(two_tank.r_cum_table[10.0] >= SPARSE_RETURN_MIN
                            and sparsest.r_cum_table[10.0] >= SPARSE_RETURN_MIN),
        "dense_plateau": dense_plateau,
        "dense_pins_low": bool(np.isfinite(dense_plateau) and dense_plateau < DENSE_PLATEAU_MAX),
        # mode-count / OFF / bias / detuned
        "n_occ_dense": n_occ_dense, "n_occ_sparse": n_occ_sparse,
        "mode_count_ok": bool(n_occ_dense > n_occ_sparse),
        "off_drift": off_drift, "off_ok": bool(off_drift < OFF_DRIFT_MAX),
        "bias_resid": bias["resid"], "bias_ok": bias["ok"],
        "det_peak_frac": det["peak_frac"], "det_gated": det["gated"],
    }

    # ── FROZEN precedence 1→6 (prereg §4) ──
    if crit["nan_seen"] or not crit["cons_ok"]:
        return "NUMERICAL/DETONATE", crit
    if not (crit["t63_gate_ok"] and crit["nocc_gate_ok"] and crit["transfer_ok"]):
        return "REGIME-NOT-REACHED", crit
    if not crit["grid_return_ok"]:
        return "FOREIGN-EATER", crit  # (a) grid-wide return failure — echo eaten
    if not crit["dense_pins_low"]:
        return "NO-ARROW", crit       # echo home before the recurrence
    if (crit["collapse_ok"] and crit["transition_ok"] and crit["controls_ok"]
            and crit["off_ok"] and crit["mode_count_ok"] and crit["bias_ok"]
            and crit["det_gated"]):
        return "COUNTING-ARROW", crit
    return "FOREIGN-EATER", crit       # (b) returns, NOT tracking x — the #722 signature


def run_sweep() -> dict:
    sweep = [run_comb(dw) for dw in DELTA_OMEGA_SWEEP]
    two_tank = run_comb(TWO_TANK_DW, horizon_recurrences=TWO_TANK_RECURRENCES,
                        omega_min=TWO_TANK_OMEGA_MIN, m=TWO_TANK_M)
    det = run_detuned_control()
    off_drift = run_off_control()
    bias = run_bias_tare()
    verdict, crit = classify(sweep, two_tank, off_drift, bias, det)
    return {
        "meta": {
            "lane": "F6 certified-κ recurrence sweep (SUFFICIENT test of the counting arrow)",
            "prereg": "research/2026-07-18_f6-certified-kappa-sweep_prereg_FROZEN.md",
            "kappa": KAPPA_SWEEP, "operating_point": "MILD (scale=0.6, A_max≈0.10)",
            "instrument": "src/ave/thermal/f6_bath_meter.py (BYTE-UNTOUCHED)",
            "plant": "STANDALONE-K4 (within meter certificate; #721 R-1 SCOPE CAVEAT)",
            "certificate": "METER-VALID-KAPPA-BAND[0.030,0.030] @ MILD (§C-post-review, PR #724)",
        },
        "verdict": verdict, "criteria": crit,
        "sweep": [asdict(r) for r in sweep], "two_tank": asdict(two_tank),
        "detuned_control": det, "off_drift": off_drift, "bias": bias,
    }


# ── VALIDATION: byte-faithful classifier cross-check (prereg § validation) ────
def self_check(out: dict) -> dict:
    """Re-derive the verdict from the banked criteria via an INDEPENDENT restatement
    of the prereg §4 tree, and assert it matches classify()'s output byte-for-byte.
    Catches any drift between the shipped tree and the frozen §4 text."""
    c = out["criteria"]
    if c["nan_seen"] or not c["cons_ok"]:
        v = "NUMERICAL/DETONATE"
    elif not (c["t63_gate_ok"] and c["nocc_gate_ok"] and c["transfer_ok"]):
        v = "REGIME-NOT-REACHED"
    elif not c["grid_return_ok"]:
        v = "FOREIGN-EATER"
    elif not c["dense_pins_low"]:
        v = "NO-ARROW"
    elif (c["collapse_ok"] and c["transition_ok"] and c["controls_ok"] and c["off_ok"]
          and c["mode_count_ok"] and c["bias_ok"] and c["det_gated"]):
        v = "COUNTING-ARROW"
    else:
        v = "FOREIGN-EATER"
    return {"recomputed": v, "banked": out["verdict"], "match": bool(v == out["verdict"])}


# ── output ────────────────────────────────────────────────────────────────────
def _fmt(r: dict) -> str:
    rc = r["r_cum_table"]
    return (f"Δω={r['delta_omega']:.3f} M={r['M']:>3d} T_rec={r['t_rec']:6.1f} "
            f"peak={r['peak_frac']:.3f} N_occ={r['n_occ']:>2d} "
            f"t63/T_rec={r['t63_over_trec']:.3f} x50={r['x_50']:.3f} "
            f"R[0.3]={r['r_return_table'][0.3]:.3f} R_cum[10]={rc[10.0]:.3f} "
            f"cons={r['max_cons_drift']:.1e} ω_d={r['omega_d']:.3f}")


def main() -> None:
    ap = argparse.ArgumentParser(description="F6 certified-κ recurrence sweep (κ=0.030, MILD)")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--companion", action="store_true", help="also run the SECONDARY self-termination leg")
    ap.add_argument("--self-check", action="store_true", help="print the byte-faithful classifier cross-check")
    args = ap.parse_args()

    out = run_sweep()
    if args.companion:
        out["companion"] = run_companion()
    check = self_check(out)
    out["self_check"] = check

    if args.json:
        print(json.dumps(out, indent=2, default=lambda o: None))
        return

    print("=" * 92)
    print("F6 CERTIFIED-κ RECURRENCE SWEEP — SUFFICIENT test of the counting arrow (κ=0.030, MILD)")
    print("=" * 92)
    for r in out["sweep"]:
        print("  " + _fmt(r))
    tt = out["two_tank"]
    print(f"  two-tank(M=2 ω=0.5/0.7): x50={tt['x_50']:.3f} R_cum[10]={tt['r_cum_table'][10.0]:.3f} "
          f"peak={tt['peak_frac']:.3f} (positive control)")
    d = out["detuned_control"]
    print(f"  detuned control: band[{d['detuned_band'][0]:.2f},{d['detuned_band'][1]:.2f}] "
          f"q-frac={d['band_power_frac']:.1e} peak={d['peak_frac']:.1e} gated={d['gated']} "
          f"(FROZEN _place_detuned_band; resonance-gating guard)")
    c = out["criteria"]
    print("-" * 92)
    print(f"  REGIME GATE (densest): t63/T_rec={c['t63_over_trec_densest']:.3f}(≤{T63_GATE}={c['t63_gate_ok']}); "
          f"N_occ={c['n_occ_densest']}(≥{NOCC_GATE}={c['nocc_gate_ok']}); "
          f"transfer peak={c['peak_frac_densest']:.3f}(≥{E_BATH_MIN}={c['transfer_ok']})")
    print(f"  collapse spread(x50)={c['collapse_spread']:.3f}(<{COLLAPSE_SPREAD_MAX}={c['collapse_ok']}); "
          f"mean(x50)={c['mean_x50']:.3f}∈[{TRANSITION_LO},{TRANSITION_HI}]={c['transition_ok']}")
    print(f"  grid_return_min={c['grid_return_min']:.3f}(≥{SPARSE_RETURN_MIN}={c['grid_return_ok']}); "
          f"dense_plateau R[0.3]={c['dense_plateau']:.3f}(<{DENSE_PLATEAU_MAX}={c['dense_pins_low']})")
    print(f"  N_occ dense={c['n_occ_dense']}>sparse={c['n_occ_sparse']}({c['mode_count_ok']}); "
          f"cons={c['max_cons']:.1e}({c['cons_ok']}); off={c['off_drift']:.1e}({c['off_ok']}); "
          f"bias={c['bias_resid']:.3f}({c['bias_ok']}); det_gated={c['det_gated']}")
    if "companion" in out:
        print("-" * 92)
        print("  COMPANION (secondary, non-gating):")
        for row in out["companion"]["rows"]:
            print(f"    N={row['N']:>2d} Re(Z_in)/Zc≈{row['re_z_in_over_zchar_proxy']:.3f} "
                  f"x_rev={row['x_revival']:.2f}")
    print("-" * 92)
    print(f"VERDICT: {out['verdict']}   [self-check recomputed={check['recomputed']} match={check['match']}]")
    print("=" * 92)


if __name__ == "__main__":
    main()

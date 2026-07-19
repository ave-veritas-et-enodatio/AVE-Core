#!/usr/bin/env python3
"""F6 certified-κ recurrence sweep — the SUFFICIENT test of the counting arrow.

★POST-REVIEW REPAIR (PR #726 review, 10 confirmed / 0 refuted): the FROZEN §4 verdict
(FOREIGN-EATER) and "question NOT decided" SURVIVE, but the ORIGINAL mechanism story was
wrong. R-1: the shipped observable resolved the prereg's frozen "first/global transfer
peak" ambiguity to GLOBAL argmax, which lands on the post-clamp plateau ⇒ R_return ≡ 0,
ERASING the real signal. This repair resolves it to the FIRST-PLATEAU reading (disclosed
in the prereg POST-FREEZE amendment + result §3/§7), which recovers RECURRENCE-TIMED
PARTIAL RETURNS at the densest comb (mildly FAVORABLE single-comb evidence). R-2: the
scale=0 back-reaction clamp is an ABSORBING state (E_lat ≡ 0) — post-clamp R ≡ 0 is
STRUCTURAL, and two combs spend 84-89% of their window dead. See the result doc.

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

# ── R-1 (PR #726 review): the observable resolves the prereg's FROZEN ambiguity ──
# The prereg §3 defines t_peak = "argmax_t E_bath(t) (… first/global transfer peak)"
# — a FROZEN AMBIGUITY ("first/global"). The originally-shipped driver resolved it to
# GLOBAL argmax, which at κ=0.030 lands on the POST-CLAMP plateau (E_bath ≡ E0 once the
# scale=0 clamp hard-zeroes the lattice) ⇒ R_return ≡ 0 over the whole physical run,
# ERASING the real signal. This repair resolves it to the OTHER frozen reading — the
# FIRST-PLATEAU / transfer-complete peak — which recovers the recurrence-timed partial
# returns the review found in the raw trace. Per the task RAILS + Rule 11 this is a
# DISCLOSED-RESOLUTION of the prereg's own ambiguity, NOT a retune (POST-FREEZE amendment
# + result §3/§7 disclose it; the superseded global-argmax tables are preserved in JSON).
EPS_CLAMP = 1e-12          # E_lat ≤ this ⇒ the scale=0 clamp has hard-zeroed the lattice
PLATEAU_PROM = 0.05        # transfer-complete prominence tol (frac of E0): a first-plateau
#                            peak is the first local E_bath max whose following dip exceeds
#                            this before recovery — rejects the rising-edge ripple, catches
#                            the ≥14% recurrence dips (same order as the other §4 tols).


def _clamp_onset(e_lat: np.ndarray) -> int:
    """First step index where the scale=0 back-reaction clamp has hard-zeroed the lattice
    (E_lat ≡ 0 for the remainder — the absorbing state, PR #726 review R-2). Returns
    len(e_lat) if no clamp fires (the physical window is the whole run)."""
    hit = np.nonzero(e_lat <= EPS_CLAMP)[0]
    return int(hit[0]) if hit.size else len(e_lat)


def _first_plateau_idx(e_bath: np.ndarray, e0: float, phys_end: int) -> int:
    """First-plateau / transfer-complete peak (the OTHER reading of the prereg's frozen
    'first/global transfer peak' ambiguity, R-1). The first local maximum of E_bath in
    the PHYSICAL (pre-clamp) window whose following dip exceeds PLATEAU_PROM·E0 before
    E_bath recovers to that peak. Falls back to the pre-clamp argmax if no prominent
    peak (e.g. a comb that clamps before its first recurrence — a NO-INFORMATION cell)."""
    prom = PLATEAU_PROM * e0
    for i in range(1, phys_end - 1):
        if e_bath[i] >= e_bath[i - 1] and e_bath[i] > e_bath[i + 1]:
            for j in range(i + 1, phys_end):
                if e_bath[j] >= e_bath[i]:
                    break  # recovered without a prominent dip ⇒ not the transfer peak
                if e_bath[i] - e_bath[j] >= prom:
                    return i
    return int(np.argmax(e_bath[:phys_end])) if phys_end > 0 else 0


# ── one comb run: sweep result + folded regime diagnostics (prereg §6) ───────
@dataclass
class CombResult:
    delta_omega: float
    M: int
    omega_max: float
    t_rec: float
    n_steps: int
    e0: float
    e_bath_peak: float        # E_bath at the FIRST-PLATEAU peak (the honest R-1 reference)
    peak_frac: float          # E_bath_peak / E0 (transfer health / NULL), first-plateau
    n_occ: int
    max_cons_drift: float     # max |E_lat+E_bath−E0|/E0 (identity audit)
    t63: int                  # first step E_bath ≥ (1−1/e)·peak (transfer timescale)
    t63_over_trec: float      # t63 / T_rec (the REGIME-gate observable at densest)
    x_50: float               # x at first R_ret_cum ≥ 0.5 (nan if never) — transition midpoint
    omega_d: float            # re-measured drive line (rFFT of collar q) — diagnostics provenance
    linewidth_fwhm: float     # half-power width of ω_d
    # ── R-1 CORRECTED (first-plateau) observable — the classifier consumes THESE ──
    r_return_table: dict = field(default_factory=dict)  # x -> R_return (first-plateau ref)
    r_cum_table: dict = field(default_factory=dict)     # x -> R_ret_cum (monotone)
    # ── R-2 clamp / absorbing-state disclosure (the no-information window) ──
    clamp_step: int = -1              # first step the scale=0 clamp hard-zeroes E_lat (-1 = none)
    clamp_x: float = float("nan")     # x at the clamp onset (nan = no clamp)
    frac_dead: float = 0.0            # fraction of the recording window that is post-clamp DEAD
    post_clamp_dead: bool = False     # did the absorbing clamp fire in this run?
    no_information: bool = False      # clamp fired before the FIRST recurrence completes (x<1)
    first_plateau_frac: float = 0.0   # E_bath_firstplateau / E0 (the honest transfer health)
    first_plateau_x: float = float("nan")  # x at the first-plateau peak
    # ── R-1 dip-vs-running-max diagnostic (parameter-free, over the physical window) ──
    dip_rmax_table: dict = field(default_factory=dict)  # x -> 1 − E_bath/running_max(E_bath)
    dip_rmax_peak: float = 0.0        # deepest dip below the running max (physical window)
    dip_rmax_x: float = float("nan")  # x of the deepest running-max dip
    # ── SUPERSEDED global-argmax reading (PRESERVED for audit; NON-gating) ──
    e_bath_peak_global_superseded: float = 0.0
    peak_frac_global_superseded: float = 0.0
    r_return_table_global_superseded: dict = field(default_factory=dict)
    r_cum_table_global_superseded: dict = field(default_factory=dict)
    # reactance pair (Rule-10 corollary): bath C-state Σ½ω²x² AND L-state Σ½p²
    # sampled ACROSS the window (11-point x-grid) — not a single-phase snapshot.
    ebath_c_table: dict = field(default_factory=dict)   # x -> C-state / E0
    ebath_l_table: dict = field(default_factory=dict)   # x -> L-state / E0
    ebath_c_at_peak: float = 0.0
    ebath_l_at_peak: float = 0.0


def run_comb(delta_omega: float, horizon_recurrences: int = HORIZON_RECURRENCES,
             omega_min: float = OMEGA_MIN, m: int | None = None) -> CombResult:
    """One comb at the CERTIFIED κ=0.030 MILD. Records E_lat/E_bath, the collar q(t),
    and the bath C/L reactance split; derives R_return(x) via the R-1 CORRECTED
    first-plateau reference (plus the superseded global-argmax reading + the dip-vs-
    running-max diagnostic), t63, x_50, ω_d/linewidth, and the R-2 clamp disclosure.
    """
    if m is None:
        m = _m_for(delta_omega)
    t_rec = 2 * np.pi / delta_omega
    n_steps = int(round(horizon_recurrences * t_rec))
    cpl = _build(delta_omega, m, omega_min=omega_min, kappa=KAPPA_SWEEP, scale=SEED_SCALE_MILD)
    e0 = cpl.e_lat()
    etot0 = e0 + cpl.e_bath()
    steps = np.arange(1, n_steps + 1)
    e_lat = np.empty(n_steps)  # R-2: needed to detect the scale=0 absorbing clamp
    e_bath = np.empty(n_steps)
    ebc = np.empty(n_steps)   # bath C-state Σ½ω²x²
    ebl = np.empty(n_steps)   # bath L-state Σ½p²
    q_ts = np.empty(n_steps)  # collar drive the bath sees this step (diagnostics)
    max_drift = 0.0
    for k, i in enumerate(steps):
        q_ts[k] = cpl.read_q()
        cpl.step(int(i))
        e_lat[k] = cpl.e_lat()
        e_bath[k] = cpl.e_bath()
        ebc[k] = float(0.5 * (cpl.bath.omega**2 * cpl.bath.x**2).sum())
        ebl[k] = float(0.5 * (cpl.bath.p**2).sum())
        max_drift = max(max_drift, abs((e_lat[k] + e_bath[k]) - etot0) / e0)
    x = steps * delta_omega / (2 * np.pi)

    # ── R-2: the scale=0 absorbing clamp (E_lat ≡ 0 for the remaining window) ──
    phys_end = _clamp_onset(e_lat)
    post_clamp_dead = phys_end < n_steps
    clamp_step = int(steps[phys_end]) if post_clamp_dead else -1
    clamp_x = float(x[phys_end]) if post_clamp_dead else float("nan")
    frac_dead = (n_steps - phys_end) / n_steps

    # ── R-1 CORRECTED reference: the FIRST-PLATEAU / transfer-complete peak ──
    t_fp = _first_plateau_idx(e_bath, e0, phys_end)
    e_bath_peak = float(e_bath[t_fp])            # first-plateau energy (the return reference)
    first_plateau_x = float(x[t_fp])
    # t63 = first step E_bath ≥ (1−1/e)·peak (the transfer timescale; first-plateau ref)
    hit63 = np.nonzero(e_bath >= INV_E * e_bath_peak)[0]
    t63 = int(steps[hit63[0]]) if hit63.size else n_steps

    # NO-INFORMATION (R-1): fewer than ONE full recurrence of observation window between
    # transfer-completion (t63) and the absorbing clamp ⇒ the recurrence RETURN (which
    # appears at x≈1 past the transfer, and whose GROWTH per recurrence is the signal)
    # cannot be observed at all. Marks the Δω=0.015/0.020 combs that clamp at x=1.17/1.72.
    obs_window = clamp_x - t63 / t_rec if post_clamp_dead else float("inf")
    no_information = bool(post_clamp_dead and obs_window < 1.0)
    # R_return(t) = 1 − E_bath/E_bath_firstplateau for t≥t_fp, else 0 (transfer incomplete).
    # Clipped at 0: the post-clamp plateau (E_bath ≈ E0 ≥ first-plateau) reads R_return = 0
    # STRUCTURALLY (the absorbing state cannot return — R-2), not a physical no-return.
    r_ret = np.where(np.arange(n_steps) >= t_fp,
                     np.clip(1.0 - e_bath / max(e_bath_peak, 1e-30), 0.0, None), 0.0)
    r_cum = np.maximum.accumulate(r_ret)
    hit = np.nonzero(r_cum >= R_HALF)[0]
    x_50 = float(x[hit[0]]) if hit.size else float("nan")

    # ── SUPERSEDED global-argmax reading (PRESERVED; NON-gating) ──
    e_bath_peak_g = float(e_bath.max())
    t_peak_g = int(np.argmax(e_bath))
    r_ret_g = np.where(np.arange(n_steps) >= t_peak_g,
                       1.0 - e_bath / max(e_bath_peak_g, 1e-30), 0.0)
    r_cum_g = np.maximum.accumulate(r_ret_g)

    # ── R-1 dip-vs-running-max diagnostic (parameter-free; physical window, post-t_fp) ──
    run_max = np.maximum.accumulate(e_bath)
    dip_rmax = np.clip(1.0 - e_bath / np.where(run_max > 0, run_max, np.nan), 0.0, None)
    phys_post_fp = np.arange(n_steps)
    dip_mask = (phys_post_fp >= t_fp) & (phys_post_fp < phys_end)
    if dip_mask.any():
        dip_vals = np.where(dip_mask, dip_rmax, -np.inf)
        dip_peak_k = int(np.argmax(dip_vals))
        dip_rmax_peak = float(dip_rmax[dip_peak_k])
        dip_rmax_x = float(x[dip_peak_k])
    else:
        dip_rmax_peak, dip_rmax_x = 0.0, float("nan")

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
        clamp_step=clamp_step, clamp_x=clamp_x, frac_dead=frac_dead,
        post_clamp_dead=post_clamp_dead, no_information=no_information,
        first_plateau_frac=e_bath_peak / e0, first_plateau_x=first_plateau_x,
        dip_rmax_table={xt: _at(xt, dip_rmax) for xt in X_TABLE},
        dip_rmax_peak=dip_rmax_peak, dip_rmax_x=dip_rmax_x,
        e_bath_peak_global_superseded=e_bath_peak_g,
        peak_frac_global_superseded=e_bath_peak_g / e0,
        r_return_table_global_superseded={xt: _at(xt, r_ret_g) for xt in X_TABLE},
        r_cum_table_global_superseded={xt: _at(xt, r_cum_g) for xt in X_TABLE},
        ebath_c_table={xt: _at(xt, ebc) / e0 for xt in X_TABLE},
        ebath_l_table={xt: _at(xt, ebl) / e0 for xt in X_TABLE},
        ebath_c_at_peak=float(ebc[t_fp]) / e0, ebath_l_at_peak=float(ebl[t_fp]) / e0,
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

    # ── R-1/R-2 DISCLOSURE (additive; NON-gating — the frozen tree below is untouched).
    # Which combs are NO-INFORMATION (the scale=0 clamp hard-zeroed the lattice before the
    # first recurrence — post-clamp R_return ≡ 0 is STRUCTURAL, cannot-fail)? And what is
    # grid_return_min if those clamp-dead rows are excluded (the honest, information-bearing
    # min)? Both readings are banked; the VERDICT uses the byte-faithful frozen grid.
    no_info_combs = [r.delta_omega for r in sweep + [two_tank] if r.no_information]
    clamped_combs = [r.delta_omega for r in sweep + [two_tank] if r.post_clamp_dead]
    informative = [r.r_cum_table[10.0] for r in sweep + [two_tank] if not r.no_information]
    grid_return_min_excl_noinfo = min(informative) if informative else float("nan")

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
        # R-1/R-2 disclosure (banked, NON-gating)
        "no_information_combs": no_info_combs,
        "clamped_combs": clamped_combs,
        "grid_return_min_excl_noinfo": grid_return_min_excl_noinfo,
        "densest_dip_rmax_peak": densest.dip_rmax_peak,
        "densest_dip_rmax_x": densest.dip_rmax_x,
        "densest_frac_dead": densest.frac_dead,
        "densest_clamp_x": densest.clamp_x,
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
            "observable": "R-1 CORRECTED — first-plateau/transfer-complete reference "
                          "(the OTHER reading of the prereg §3 'first/global transfer peak' "
                          "frozen ambiguity). Global-argmax reading PRESERVED as "
                          "*_global_superseded. Post-clamp window marked no_information (R-2).",
        },
        "verdict": verdict, "criteria": crit,
        "sweep": [asdict(r) for r in sweep], "two_tank": asdict(two_tank),
        "detuned_control": det, "off_drift": off_drift, "bias": bias,
    }


# ── VALIDATION: byte-faithful classifier cross-check (prereg § validation) ────
def self_check(out: dict) -> dict:
    """Re-derive the verdict from the banked criteria via a restatement of the prereg §4
    tree, and assert it matches classify()'s output byte-for-byte. Catches any PRECEDENCE
    drift between the shipped tree and the frozen §4 text.

    ★R-6 NON-INDEPENDENCE CAVEAT (PR #726 review): this cross-check CONSUMES classify()'s
    own boolean criteria (`grid_return_ok`, `collapse_ok`, …). It therefore catches only a
    precedence/wiring drift between the two tree restatements — it does NOT independently
    re-derive the booleans from the raw observable, so it CANNOT catch an observable-
    definition bug (exactly the R-1 argmax-gating that erased the signal in the first fire).
    The real independent check is the PR #726 review's re-derivation from the raw trace
    (see result §4/§7); this self_check is a precedence guard only, not that check."""
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
    cx = f"{r['clamp_x']:.2f}" if r["post_clamp_dead"] else " -- "
    tag = " ★NO-INFO" if r["no_information"] else (" (clamp)" if r["post_clamp_dead"] else "")
    return (f"Δω={r['delta_omega']:.3f} M={r['M']:>3d} T_rec={r['t_rec']:6.1f} "
            f"fp={r['first_plateau_frac']:.3f} N_occ={r['n_occ']:>2d} "
            f"t63/T_rec={r['t63_over_trec']:.3f} x50={r['x_50']:.3f} "
            f"R_cum[10]={rc[10.0]:.3f} dipRmax={r['dip_rmax_peak']:.3f}@{r['dip_rmax_x']:.2f} "
            f"clamp_x={cx} dead={r['frac_dead']*100:.0f}% cons={r['max_cons_drift']:.1e}{tag}")


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
    print(f"  ★R-1/R-2: NO-INFO combs (clamp <1 recurrence past transfer)={c['no_information_combs']}; "
          f"clamped={c['clamped_combs']}; grid_return_min(excl NO-INFO)={c['grid_return_min_excl_noinfo']:.3f}")
    print(f"  ★densest recurrence returns (dip-vs-running-max)={c['densest_dip_rmax_peak']:.3f} "
          f"@x={c['densest_dip_rmax_x']:.2f} before clamp@x={c['densest_clamp_x']:.2f} "
          f"(dead={c['densest_frac_dead']*100:.0f}%) — MILDLY FAVORABLE single-comb (question OPEN)")
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

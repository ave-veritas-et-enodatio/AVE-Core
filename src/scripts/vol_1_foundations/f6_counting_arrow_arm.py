#!/usr/bin/env python3
"""F6 counting-arrow arm — recurrence-sweep driver (Phase 1; sub-yield).

Prereg (FROZEN): research/2026-07-18_f6-counting-arrow-arm_prereg_FROZEN.md
Charters:        research/2026-07-15_f6-mode-count-door_CHARTER.md (bins §4, gate §5b)
                 research/2026-07-16_f6-bath-meter_CHARTER.md (§A/§B + §B-post R-1 caveat)
Instrument:      src/ave/thermal/f6_bath_meter.py (LatticeBathCoupler — BYTE-UNTOUCHED)
License tested:  manuscript/ave-kb/common/retention-transition-split.md (arrow-from-counting)

SECTOR / REGIME (mandatory header):
  Sector    : E-sector ε-store (F6 ε→T2 candidate). NOT A1 mass, NOT Cosserat (2,3).
  Mode      : reactive K4 TLM lattice + external Foster comb bank (Caldeira-Leggett).
  Regime    : Regime I sub-yield (Phase 1), A_max≈0.10 cold; op3 Γ(A) 2nd-order.
  Phase-st. : driven-then-source-off, closed cavity (pml=0, energy-conserving).
  Plant     : STANDALONE-K4 — within the meter certificate (#721 R-1 SCOPE CAVEAT).
              Conservation is IDENTITY-enforced here; CHANNEL-BOUNDED bin is defined
              energy-conserving ⇒ the identity ledger is CONSISTENT with the target.
  Coord.    : R_return = scalar energy ledger (coordinate-free); collapse var
              x = T·Δω/2π is SPECTRAL — matched to the mode-count claim (A46). No
              real-space φ² surrogate.

THE MECHANISM UNDER TEST. A finite comb of M equally-spaced oscillators (spacing Δω)
has an exact Poincaré recurrence at T_rec = 2π/Δω (phases ω_m t = ω_min t + mΔω t
re-cohere when Δω t ∈ 2πℤ, independent of M and ω_min). Energy transferred out RETURNS
at T_rec. The counting-arrow: energy fails to return iff T_window < T_rec, i.e. iff the
comb is dense enough (small Δω) that the recurrence outruns the window. The arrow is a
horizon-crossing (Poincaré-honest), the same epistemic status as radiation resistance.

NO Re(Z) ELEMENT EXISTS ANYWHERE (the no-valve rail): the comb is lossless
(friction=False, bath.damp OFF), the coupling is a symplectic CL kick + exact free
rotation, and the back-reaction is a phase-preserving energy-matched rescale. Any real
input resistance is EMERGENT FROM COUNTING.

Run: PYTHONPATH=src python src/scripts/vol_1_foundations/f6_counting_arrow_arm.py [--json] [--companion]
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass, field

import numpy as np

from ave.core.k4_tlm import K4Lattice3D
from ave.thermal import LatticeBathCoupler, OscillatorBath, make_collar_mask

# ── FROZEN grid (prereg §3; ENGINEERING CHOICES — tagged) ────────────────────
N_GRID = 12
CENTER = (N_GRID // 2, N_GRID // 2, N_GRID // 2)
COLLAR_R_IN, COLLAR_R_OUT = 2.0, 4.0
KAPPA = 0.012
OMEGA_MIN = 0.30
BAND_TOP = 1.0  # comb band top held fixed (ω_max≈1.0); M adjusts with Δω
BAND = BAND_TOP - OMEGA_MIN  # 0.70 — the dephasing-offset denominator (prereg §2)
SEED = 1
SEED_SCALE_P1 = 0.6  # Phase-1 mild (A_max≈0.10)
DT = 1.0

# Comb-density sweep (prereg §3 Knob-1). ω_max ≈ 1.0 for every row (Nyquist OK).
DELTA_OMEGA_SWEEP = (0.010, 0.015, 0.020, 0.030, 0.050, 0.080)
HORIZON_RECURRENCES = 11  # T_max = 11·T_rec ⇒ x reaches 11 > 10
DENSE_MAX_DW = 0.030  # combs at/below this feed the dense-end pinned-low check (prereg §2·4)

# Two-tank positive control (prereg §3): M=2, ω={0.50,0.70}, Δω=0.20.
TWO_TANK_OMEGA_MIN, TWO_TANK_DW, TWO_TANK_M = 0.50, 0.20, 2
TWO_TANK_RECURRENCES = 12

# x-grid table points (prereg §3 Knob-2): 11 points, ≥3/decade over [0.1,10].
X_TABLE = (0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0)

# ── FROZEN verdict thresholds (prereg §2/§4; DERIVED, not tuned) ─────────────
COLLAPSE_SPREAD_MAX = 0.30       # spread(x_50) < 0.30
TRANSITION_LO, TRANSITION_HI = 0.7, 1.5   # mean(x_50) ∈ [0.7,1.5]
SPARSE_RETURN_MIN = 0.70         # sparse-control R_ret_cum(x≫1) > 0.70
DENSE_PLATEAU_MAX = 0.30         # dense R_return(x=0.3) < 0.30
CONS_TOL = 1e-3                  # |E_lat+E_bath−E0|/E0 < 1e-3
OFF_DRIFT_MAX = 1e-10            # κ=0 closed-cavity drift < 1e-10
BIAS_TARE_TOL = 0.05            # protected-core bias (tared) < 0.05
E_BATH_MIN = 1e-2               # NULL floor (peak transfer)
R_HALF = 0.5                    # cumulative-return crossing level


def _m_for(delta_omega: float) -> int:
    """Band-fixed truncation count: ω_max = ω_min+(M−1)Δω ≈ BAND_TOP (prereg §3)."""
    return int(round(BAND / delta_omega)) + 1


def _seed_lattice(lat: K4Lattice3D, scale: float) -> None:
    """Deterministic broadband seed (byte-identical shape to the meter's _seed_lattice)."""
    rng = np.random.default_rng(SEED)
    ii, jj, kk = np.indices((lat.nx, lat.ny, lat.nz))
    c = CENTER
    env = np.exp(-((ii - c[0]) ** 2 + (jj - c[1]) ** 2 + (kk - c[2]) ** 2) / (2 * 1.5**2))
    env[~lat.mask_active] = 0.0
    for p in range(4):
        lat.V_inc[..., p] += scale * 0.08 * env
    fld = np.zeros_like(lat.V_inc)
    for _ in range(6):
        kv = rng.integers(1, lat.nx // 2, size=3) * (2 * np.pi / lat.nx) * rng.choice([-1, 1], size=3)
        ph = rng.uniform(0, 2 * np.pi)
        pw = np.cos(kv[0] * ii + kv[1] * jj + kv[2] * kk + ph)
        pw2 = rng.normal(size=4)
        for p in range(4):
            fld[..., p] += scale * 0.03 * pw * pw2[p]
    fld[~lat.mask_active] = 0.0
    lat.V_inc += fld


def _build(delta_omega: float, m: int, omega_min: float = OMEGA_MIN,
           kappa: float = KAPPA, scale: float = SEED_SCALE_P1) -> LatticeBathCoupler:
    """Coupled meter on a standalone-K4 plant; E0 captured on-shell (post-first-step)."""
    lat = K4Lattice3D(N_GRID, N_GRID, N_GRID, nonlinear=True, op3_bond_reflection=True, V_SNAP=1.0)
    _seed_lattice(lat, scale)
    lat.step()  # on-shell baseline
    bath = OscillatorBath(M=m, omega_min=omega_min, delta_omega=delta_omega)
    collar = make_collar_mask(lat, CENTER, COLLAR_R_IN, COLLAR_R_OUT)
    return LatticeBathCoupler(lat, bath, collar, kappa=kappa)


# ── one comb run ─────────────────────────────────────────────────────────────
@dataclass
class CombResult:
    delta_omega: float
    M: int
    omega_max: float
    t_rec: float          # 2π/Δω (steps)
    n_steps: int
    e0: float
    e_bath_peak: float
    peak_frac: float      # E_bath_peak / E0 (transfer health / NULL check)
    n_occ: int
    max_cons_drift: float  # max |E_lat+E_bath−E0|/E0 (identity audit)
    x_50: float           # x at first R_ret_cum ≥ 0.5 (nan if never)
    r_return_table: dict = field(default_factory=dict)  # x -> R_return (instantaneous)
    r_cum_table: dict = field(default_factory=dict)     # x -> R_ret_cum (monotone)
    # reactance-pair diagnostic (Rule-10 Checkpoint-6): bath C-state / L-state split
    ebath_c_at_peak: float = 0.0
    ebath_l_at_peak: float = 0.0


def run_comb(delta_omega: float, horizon_recurrences: int = HORIZON_RECURRENCES,
             omega_min: float = OMEGA_MIN, m: int | None = None) -> CombResult:
    """Run one comb, record the full E_lat/E_bath trajectory, derive R_return(x)."""
    if m is None:
        m = _m_for(delta_omega)
    t_rec = 2 * np.pi / delta_omega
    n_steps = int(round(horizon_recurrences * t_rec))
    cpl = _build(delta_omega, m, omega_min=omega_min)
    e0 = cpl.e_lat()
    etot0 = e0 + cpl.e_bath()
    steps = np.arange(1, n_steps + 1)
    e_bath = np.empty(n_steps)
    ebc = np.empty(n_steps)  # bath C-state energy Σ½ω²x²
    ebl = np.empty(n_steps)  # bath L-state energy Σ½p²
    max_drift = 0.0
    for k, i in enumerate(steps):
        cpl.step(int(i))
        e_bath[k] = cpl.e_bath()
        ebc[k] = float(0.5 * (cpl.bath.omega**2 * cpl.bath.x**2).sum())
        ebl[k] = float(0.5 * (cpl.bath.p**2).sum())
        max_drift = max(max_drift, abs((cpl.e_lat() + e_bath[k]) - etot0) / e0)
    x = steps * delta_omega / (2 * np.pi)
    e_bath_peak = float(e_bath.max())
    t_peak_k = int(np.argmax(e_bath))
    # R_return(t) = 1 − E_bath/E_bath_peak for t≥t_peak, else 0 (transfer incomplete)
    r_ret = np.where(np.arange(n_steps) >= t_peak_k, 1.0 - e_bath / max(e_bath_peak, 1e-30), 0.0)
    r_cum = np.maximum.accumulate(r_ret)
    # x_50 = first x with R_ret_cum ≥ 0.5
    hit = np.nonzero(r_cum >= R_HALF)[0]
    x_50 = float(x[hit[0]]) if hit.size else float("nan")

    def _at(xt: float, arr: np.ndarray) -> float:
        return float(arr[int(np.argmin(np.abs(x - xt)))])

    return CombResult(
        delta_omega=delta_omega, M=m, omega_max=float(cpl.bath.omega[-1]), t_rec=t_rec,
        n_steps=n_steps, e0=e0, e_bath_peak=e_bath_peak, peak_frac=e_bath_peak / e0,
        n_occ=cpl.bath.n_occ(), max_cons_drift=max_drift, x_50=x_50,
        r_return_table={xt: _at(xt, r_ret) for xt in X_TABLE},
        r_cum_table={xt: _at(xt, r_cum) for xt in X_TABLE},
        ebath_c_at_peak=float(ebc[t_peak_k]), ebath_l_at_peak=float(ebl[t_peak_k]),
    )


def run_off_control() -> float:
    """κ=0 closed-cavity drift over 200 steps (OFF recovers Ax3)."""
    cpl = _build(0.03, _m_for(0.03), kappa=0.0)
    e0 = cpl.e_lat()
    for i in range(1, 201):
        cpl.step(i)
    return abs(cpl.e_lat() - e0) / e0


def run_bias_tare() -> dict:
    """Protected-core bias ON vs OFF, tared by c=√(1−E_bath/E0) (prereg §4·8)."""
    dw = 0.03
    on = _build(dw, _m_for(dw))
    off = _build(dw, _m_for(dw), kappa=0.0)
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
    return {"a_on": a_on, "a_off": a_off, "tare_c": c, "resid": resid, "ok": resid < BIAS_TARE_TOL}


# ── Phase-1 orchestration + frozen classification ────────────────────────────
def classify(sweep: list[CombResult], two_tank: CombResult, off_drift: float,
             bias: dict) -> tuple[str, dict]:
    """Frozen §4 verdict. No retune (Rule 11)."""
    x50 = {r.delta_omega: r.x_50 for r in sweep if np.isfinite(r.x_50)}
    finite = list(x50.values())
    spread = (max(finite) - min(finite)) if len(finite) >= 2 else float("nan")
    mean_x50 = float(np.mean(finite)) if finite else float("nan")
    # sparse control: two-tank AND sparsest sweep comb return at x≫1 (use x=10 col)
    # ★DISCLOSED NARROWING (PR #722 review R-5): this checks ONLY the sparsest comb +
    # two-tank, narrowing the frozen FOREIGN-EATER fire condition ("return failure NOT
    # tracking x") down to its parenthetical example ("sparse control fails to return").
    # A FAITHFUL reading of the frozen §4 FOREIGN-EATER row FIRES on this data — the
    # return does NOT track x (x_50 spreads 3.6→11, the headline finding). So the honest
    # frozen-classifier answer here is FOREIGN-EATER, not the FRICTION-RENAMED this tree
    # returns. Code left UN-RETUNED per Rule 11; the bin is routed to Grant (result §4/§7).
    sparsest = max(sweep, key=lambda r: r.delta_omega)
    sparse_ret = min(two_tank.r_cum_table[10.0], sparsest.r_cum_table[10.0])
    # dense-end pinned-low: R_return(x=0.3) for combs with Δω ≤ DENSE_MAX_DW
    dense = [r for r in sweep if r.delta_omega <= DENSE_MAX_DW]
    dense_plateau = max((r.r_return_table[0.3] for r in dense), default=float("nan"))
    # mode-count fingerprint: dense N_occ > sparse N_occ
    n_occ_dense = min(r.n_occ for r in dense) if dense else 0
    n_occ_sparse = sparsest.n_occ
    mode_count_ok = n_occ_dense > n_occ_sparse
    # conservation identity + NULL
    max_drift = max(r.max_cons_drift for r in sweep + [two_tank])
    null = any(r.peak_frac < E_BATH_MIN for r in sweep)

    crit = {
        "collapse_spread": spread, "collapse_ok": bool(np.isfinite(spread) and spread < COLLAPSE_SPREAD_MAX),
        "mean_x50": mean_x50, "transition_ok": bool(TRANSITION_LO <= mean_x50 <= TRANSITION_HI),
        "sparse_return": sparse_ret, "sparse_ok": bool(sparse_ret > SPARSE_RETURN_MIN),
        "dense_plateau": dense_plateau, "dense_ok": bool(dense_plateau < DENSE_PLATEAU_MAX),
        "cons_drift": max_drift, "cons_ok": bool(max_drift < CONS_TOL),
        "off_drift": off_drift, "off_ok": bool(off_drift < OFF_DRIFT_MAX),
        "n_occ_dense": n_occ_dense, "n_occ_sparse": n_occ_sparse, "mode_count_ok": mode_count_ok,
        "bias_resid": bias["resid"], "bias_ok": bias["ok"], "null": null,
    }

    # frozen decision tree (prereg §4)
    if null:
        return "NULL", crit
    if not crit["cons_ok"]:
        return "NUMERICAL/DETONATE", crit
    if not crit["sparse_ok"]:
        # echo fails to return where it MUST (sparse) — something else eats it
        return "FOREIGN-EATER", crit
    if not crit["mode_count_ok"]:
        return "FRICTION-RENAMED", crit
    if not crit["bias_ok"]:
        return "BIAS-MOVED", crit
    if crit["collapse_ok"] and crit["transition_ok"] and crit["dense_ok"] and crit["off_ok"]:
        return "COUNTING-ARROW", crit
    # collapse/transition held sparse-return but dense never pinned low ⇒ echo always home
    if not crit["dense_ok"]:
        return "NO-ARROW", crit
    return "FOREIGN-EATER", crit


def run_phase1() -> dict:
    sweep = [run_comb(dw) for dw in DELTA_OMEGA_SWEEP]
    two_tank = run_comb(TWO_TANK_DW, horizon_recurrences=TWO_TANK_RECURRENCES,
                        omega_min=TWO_TANK_OMEGA_MIN, m=TWO_TANK_M)
    off_drift = run_off_control()
    bias = run_bias_tare()
    verdict, crit = classify(sweep, two_tank, off_drift, bias)
    return {
        "verdict": verdict, "criteria": crit,
        "sweep": [asdict(r) for r in sweep], "two_tank": asdict(two_tank),
        "off_drift": off_drift, "bias": bias,
    }


# ── REGIME DIAGNOSTICS (PR #722 review R-7: provenance for the prose numbers) ─
@dataclass
class CombDiag:
    """The regime-diagnosis triple the result-doc prose asserted, now COMPUTED.

    Definitions (documented so the number has provenance, not prose):
      omega_d           — dominant angular frequency of the collar coordinate q(t)
                          (rFFT power-spectrum peak; the narrowband drive line).
      linewidth_fwhm    — half-power (FWHM) width of that dominant line.
      n_pop_gt1pct      — bath modes with E_m > 1% of E_bath_peak, read at t_peak.
      tau_transfer_over_trec — t_peak / T_rec  (= x_peak; the transfer-complete time
                          in recurrence units — the τ_transfer≫T_rec inversion).
    """
    delta_omega: float
    M: int
    t_rec: float
    omega_d: float
    linewidth_fwhm: float
    n_pop_gt1pct: int
    tau_transfer_over_trec: float
    t_peak: int
    peak_frac: float


def run_comb_diagnostics(delta_omega: float, horizon_recurrences: int = HORIZON_RECURRENCES,
                         omega_min: float = OMEGA_MIN, m: int | None = None) -> CombDiag:
    """Re-measure the prose regime numbers deterministically. `run_comb` is NOT
    modified (the banked sweep stays bit-identical); this is a SEPARATE read that
    additionally records the collar coordinate q(t) and captures the per-mode bath
    energy at the transfer peak. NON-GATING (does not touch the frozen verdict)."""
    if m is None:
        m = _m_for(delta_omega)
    t_rec = 2 * np.pi / delta_omega
    n_steps = int(round(horizon_recurrences * t_rec))
    cpl = _build(delta_omega, m, omega_min=omega_min)
    e0 = cpl.e_lat()  # on-shell baseline (same reference as run_comb's peak_frac)
    q = np.empty(n_steps)
    e_bath = np.empty(n_steps)
    peak_e = -1.0
    peak_me = cpl.bath.mode_energy().copy()
    for k, i in enumerate(range(1, n_steps + 1)):
        q[k] = cpl.read_q()          # collar drive the bath sees this step
        cpl.step(int(i))
        eb = cpl.e_bath()
        e_bath[k] = eb
        if eb > peak_e:
            peak_e = eb
            peak_me = cpl.bath.mode_energy().copy()
    t_peak_k = int(np.argmax(e_bath))
    e_bath_peak = float(e_bath.max())
    # collar-drive spectrum (mean-subtracted rFFT power); dominant angular frequency
    power = np.abs(np.fft.rfft(q - q.mean())) ** 2
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
    n_pop = int(np.count_nonzero(peak_me > 0.01 * e_bath_peak)) if e_bath_peak > 0 else 0
    return CombDiag(
        delta_omega=delta_omega, M=m, t_rec=t_rec, omega_d=omega_d,
        linewidth_fwhm=linewidth, n_pop_gt1pct=n_pop,
        tau_transfer_over_trec=(t_peak_k + 1) / t_rec, t_peak=t_peak_k + 1,
        peak_frac=e_bath_peak / e0,
    )


def run_diagnostics() -> dict:
    """Bank the regime-diagnosis triple (ω_d + linewidth, n_pop(>1%), τ_transfer/T_rec)
    per sweep cell — the numbers the result-doc prose asserted but no shipped script
    computed (PR #722 review R-7 provenance gap). NON-GATING: the frozen verdict is
    untouched. The LOAD-BEARING few-mode count is the meter's N_occ (banked per-cell in
    `sweep`); n_pop here is corroborative color."""
    cells = [asdict(run_comb_diagnostics(dw)) for dw in DELTA_OMEGA_SWEEP]
    omegas = [c["omega_d"] for c in cells]
    return {
        "note": "R-7 provenance addendum (PR #722 review). Regime-diagnosis numbers the "
                "result-doc prose asserted (ω_d, n_pop, τ_transfer/T_rec) were prose-only "
                "at push; this shipped read computes them. NON-GATING (verdict unchanged). "
                "Load-bearing few-mode count is the meter's N_occ (banked in 'sweep').",
        "omega_d_representative": float(np.median(omegas)),
        "cells": cells,
    }


# ── COMPANION LEG (SECONDARY — non-gating; prereg §6) ────────────────────────
def _seed_local(lat: K4Lattice3D, amp: float = 0.6) -> None:
    """Localized central impulse (single-cell block) — the self-termination port."""
    c = CENTER
    for dp in ((0, 0, 0),):
        idx = (c[0] + dp[0], c[1] + dp[1], c[2] + dp[2])
        if lat.mask_active[idx]:
            lat.V_inc[idx][:] = amp


def run_companion(n_list=(8, 10, 12, 16)) -> dict:
    """Self-termination: local port into the lattice, size sweep N. Emergent Re(Z_in)
    born from the lattice's own mode count. SECONDARY — cannot change the arm verdict.
    Consistency target Z₀=√(L_bond/C_bond) is VALUE=calibration; the ratio is reported.
    """
    rows = []
    for n in n_list:
        c = (n // 2, n // 2, n // 2)
        lat = K4Lattice3D(n, n, n, nonlinear=True, op3_bond_reflection=True, V_SNAP=1.0)
        # local impulse at the port cell
        if lat.mask_active[c]:
            lat.V_inc[c][:] = 0.6
        lat.step()
        e0 = lat.total_energy()
        # port region = cells within r_port of the centre
        ii, jj, kk = np.indices((n, n, n))
        r2 = (ii - c[0]) ** 2 + (jj - c[1]) ** 2 + (kk - c[2]) ** 2
        port = (r2 <= 1.5**2) & lat.mask_active
        horizon = 6 * n  # a few round-trips
        e_port = np.empty(horizon)
        for k in range(horizon):
            lat.step()
            dens = lat.get_energy_density()
            e_port[k] = float(dens[port].sum())
        e_port_frac = e_port / max(e0, 1e-30)
        # initial dispersion minimum, then first revival (local recurrence)
        k_min = int(np.argmin(e_port_frac[: max(2, horizon // 2)]))
        rest = e_port_frac[k_min:]
        # first local maximum after the dispersion trough = revival
        rev_rel = 1
        for k in range(1, len(rest) - 1):
            if rest[k] > rest[k - 1] and rest[k] >= rest[k + 1] and rest[k] > e_port_frac[k_min] * 1.3:
                rev_rel = k
                break
        t_rec_lat = float(k_min + rev_rel + 1)
        dw_lat = 2 * np.pi / t_rec_lat if t_rec_lat > 0 else float("nan")
        # emergent Re(Z_in)/Z_char proxy = deepest dispersion before revival
        re_z_proxy = float(1.0 - e_port_frac[k_min])
        x_rev = t_rec_lat * dw_lat / (2 * np.pi)  # ≈ 1 by construction (self-consistency)
        rows.append({
            "N": n, "t_rec_lattice": t_rec_lat, "dw_lattice": dw_lat,
            "re_z_in_over_zchar_proxy": re_z_proxy, "x_revival": x_rev,
            "e_port_frac_min": float(e_port_frac[k_min]),
        })
    # FORM observable: does Re(Z_in) proxy grow (born) with N (finer comb)?
    proxies = [r["re_z_in_over_zchar_proxy"] for r in rows]
    born_with_n = all(proxies[i] <= proxies[i + 1] + 0.05 for i in range(len(proxies) - 1))
    return {
        "note": "SECONDARY / non-gating (prereg §6). Z₀=√(L_bond/C_bond) is VALUE=calibration; "
                "ratio reported at consistency-class, NOT a derivation of Z₀=377Ω.",
        "rows": rows, "re_z_proxy_monotone_in_N": born_with_n,
    }


# ── output ───────────────────────────────────────────────────────────────────
def _fmt_comb(r: dict) -> str:
    rc = r["r_cum_table"]
    return (f"Δω={r['delta_omega']:.3f} M={r['M']:>3d} T_rec={r['t_rec']:6.1f} "
            f"peak_frac={r['peak_frac']:.3f} N_occ={r['n_occ']:>2d} x50={r['x_50']:.3f} "
            f"R_cum[0.3]={rc[0.3]:.3f} R_cum[10]={rc[10.0]:.3f} cons={r['max_cons_drift']:.1e}")


def main() -> None:
    ap = argparse.ArgumentParser(description="F6 counting-arrow arm — recurrence sweep (Phase 1)")
    ap.add_argument("--json", action="store_true", help="emit JSON")
    ap.add_argument("--companion", action="store_true", help="also run the SECONDARY self-termination leg")
    ap.add_argument("--diagnostics", action="store_true",
                    help="also run the R-7 regime-diagnostics read (ω_d, n_pop, τ_transfer/T_rec)")
    args = ap.parse_args()

    out = run_phase1()
    if args.companion:
        out["companion"] = run_companion()
    if args.diagnostics:
        out["diagnostics"] = run_diagnostics()

    if args.json:
        print(json.dumps(out, indent=2, default=lambda o: None))
        return

    print("=" * 84)
    print("F6 COUNTING-ARROW ARM — recurrence sweep (Phase 1, sub-yield; standalone-K4)")
    print("=" * 84)
    for r in out["sweep"]:
        print("  " + _fmt_comb(r))
    tt = out["two_tank"]
    print(f"  two-tank(M=2 ω=0.5/0.7): x50={tt['x_50']:.3f} R_cum[10]={tt['r_cum_table'][10.0]:.3f} "
          f"peak_frac={tt['peak_frac']:.3f} (positive control)")
    c = out["criteria"]
    print("-" * 84)
    print(f"  collapse spread(x50)={c['collapse_spread']:.3f}(<{COLLAPSE_SPREAD_MAX}={c['collapse_ok']}); "
          f"mean(x50)={c['mean_x50']:.3f}∈[{TRANSITION_LO},{TRANSITION_HI}]={c['transition_ok']}")
    print(f"  sparse_return={c['sparse_return']:.3f}(>{SPARSE_RETURN_MIN}={c['sparse_ok']}); "
          f"dense_plateau R[0.3]={c['dense_plateau']:.3f}(<{DENSE_PLATEAU_MAX}={c['dense_ok']})")
    print(f"  N_occ dense={c['n_occ_dense']} > sparse={c['n_occ_sparse']} ({c['mode_count_ok']}); "
          f"cons_drift={c['cons_drift']:.1e}({c['cons_ok']}); off_drift={c['off_drift']:.1e}({c['off_ok']}); "
          f"bias_resid={c['bias_resid']:.3f}({c['bias_ok']})")
    if "companion" in out:
        print("-" * 84)
        print("  COMPANION (secondary, non-gating):")
        for row in out["companion"]["rows"]:
            print(f"    N={row['N']:>2d} T_rec_lat={row['t_rec_lattice']:.1f} "
                  f"Re(Z_in)/Zc≈{row['re_z_in_over_zchar_proxy']:.3f} x_rev={row['x_revival']:.2f}")
    if "diagnostics" in out:
        print("-" * 84)
        print(f"  REGIME DIAGNOSTICS (R-7 provenance; ω_d≈{out['diagnostics']['omega_d_representative']:.4f}):")
        for c in out["diagnostics"]["cells"]:
            print(f"    Δω={c['delta_omega']:.3f} ω_d={c['omega_d']:.4f} lw={c['linewidth_fwhm']:.4f} "
                  f"n_pop(>1%)={c['n_pop_gt1pct']:>2d} τ_transfer/T_rec={c['tau_transfer_over_trec']:.2f}")
    print("-" * 84)
    print(f"VERDICT: {out['verdict']}")
    print("=" * 84)


if __name__ == "__main__":
    main()

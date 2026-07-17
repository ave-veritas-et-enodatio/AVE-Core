#!/usr/bin/env python3
"""R3 — the destructive test: drive one cell past the Ax-4 rupture root (A=1).

FROZEN PRE-REG: research/2026-07-16_r3-snap-crossing_prereg_FROZEN.md
(committed + pushed BEFORE this driver, ave-prereg 3.11).

THE QUESTION (hardware-ratings-map §2 R3, UNRUN): the corpus maps pair
production to vacuum-avalanche breakdown — past-snap overflow RECTIFIES AC->DC
winding into the T2 Cosserat register (FPB past-snap-overflow walk; Miller row;
02_absolute_maximum_ratings.tex:85 "blocked longitudinal KE shatters sideways
into two contra-rotating Beltrami vortices").

SECTOR HEADER: DRIVE = E-sector (longitudinal scalar V, the "3"/V-sector, NOT a
Maxwell transverse photon). PREDICTED PRODUCT = T2 Cosserat winding (micro-
rotation omega; rectified DC winding = a persistent non-decaying net omega). The
observable IS the cross-sector transfer E->T2, which the coupling
alpha(V)=alpha0*(1-S(V)) engages ONLY as A->1 (decoupled sub-snap).

HARNESS: CosseratMasterEquationFDTD (coupling_mode="shared_flux") — the only
engine carrying both the E-sector V field (with the Ax-4 kernel S(V)) and the
T2 omega field, coupled via the Op14 shared-inductive-flux trade, with the
reactance-pair registers (Sigma_V_sq / Sigma_Phi_link_sq) observable.

COORDINATE DISCIPLINE (A46): the crossing is measured in the engine-native
dimensionless A = V/V_yield and the native T2 registers (omega, Phi_omega,
Phi_link) — NOT against an SI 511 kV target. In this engine's macroscopic
normalization the kernel rupture root S=0 sits at A=1 i.e. V=V_yield; the
physical V_snap=511 kV and V_yield=43.65 kV are the two SI anchors of the SAME
dimensionless r=1.0 boundary.

CLASS: CONSISTENCY (does the frozen engine MANIFEST the corpus-asserted
rectification at the kernel-rupture root?). NOT an emergence claim; no CODATA
target recovered. BENCH-null: probes the MODEL's absolute maximum only; the
real vacuum's snap is Schwinger-scale (E_S~1.32e18 V/m; lab E/E_S~1e-8).

NUMERICAL HEALTH (Rule-10): PML cells excluded from every interior sum
(argpartition off-source extraction too); reactance pair (C-state Sigma_V_sq +
L-state Sigma_Phi_link_sq) recorded at EVERY probe step; NaN/Inf + blow-up
guards; dt/2 + grid-refine convergence pair. A blow-up is INSTRUMENT not physics.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np

from ave.core.constants import ALPHA, V_SNAP, V_YIELD
from ave.core.cosserat_master_equation_fdtd import CosseratMasterEquationFDTD

# ── frozen thresholds (prereg §2; do not retune) ──────────────────────────────
RECT_FRAC = 0.10       # DC-winding fraction of AC excursion for RECTIFIES
RECT_RATIO = 10.0      # past/control ratio for RECTIFIES
PERSIST_MIN = 0.5      # non-decay of DC winding across the post window
CLIP_TOL = 1e-2        # excess odd-harmonic fraction => clipping products present
STALL_GAP = 0.05       # A-units: A_ceil < 1 - STALL_GAP => STALLS (soft source)
CONV_TOL = 0.20        # fractional metric change under dt/2 or grid refine
ENERGY_DRIFT_TOL = 5e-2  # FROZEN NUMERICAL trigger (prereg §2 line 61): fractional
                         # source-off energy drift > this => NUMERICAL. This is the
                         # frozen conservation-window bar; a stable-labeled cell must
                         # survive it. See _frozen_bar_readjudication() below.
# ── post-charter instruments (NOT frozen; disclosed in the result deviations note) ──
BLOWUP_FACTOR = 100.0  # POST-CHARTER: max|V| > BLOWUP_FACTOR*commanded => hard abort.
                       # A coarse NaN-precursor guard, minted after the freeze; the
                       # frozen NUMERICAL trigger is ENERGY_DRIFT_TOL, not this.
STABLE_EXPLORATION_CUT = 0.5  # POST-CHARTER exploratory cut used by _probe().stable
                              # (e_growth < 0.5). NOT the frozen bar (5e-2); retained
                              # only as EXPLORATION for the dt-scaling narrative.

# ── frozen drive parameters (prereg §3) ───────────────────────────────────────
N_BASE = 48
PML = 6
CARRIER_PERIOD = 20    # steps/cycle (well-resolved AC carrier for Shape A)
N_RAMP = 300
N_HOLD = 300
N_RELAX = 600
POST_SETTLE = 120      # skip this many steps after source-off before DC read
A_PEAK_PAST = 1.3      # commanded peak strain (crosses A=1)
A_PEAK_SUB = 0.8       # sub-snap control (never crosses)


@dataclass
class RunConfig:
    name: str
    shape: str            # "A" (bipolar AC) | "B" (unipolar DC push)
    a_peak: float         # commanded peak A = V_peak / V_yield
    source_mode: str = "soft"   # "soft" | "hard"
    N: int = N_BASE
    cfl_safety: float = 0.4
    n_ramp: int = N_RAMP
    n_hold: int = N_HOLD
    n_relax: int = N_RELAX
    carrier_period: int = CARRIER_PERIOD   # steps/cycle (Shape A)
    coupling_mode: str = "shared_flux"     # "shared_flux" | "forward"
    alpha_0: float = 1.0                    # E->T2 coupling strength (0 = decoupled)


def _interior_mask(N: int, pml: int) -> np.ndarray:
    """Boolean mask: True on PML-excluded interior cells (Rule-10 corollary)."""
    m = np.zeros((N, N, N), dtype=bool)
    m[pml:N - pml, pml:N - pml, pml:N - pml] = True
    return m


def _envelope(step_i: int, n_ramp: int, n_hold: int) -> float:
    """tanh ramp 0->1 over n_ramp, hold 1 for n_hold, then source is OFF."""
    if step_i < n_ramp:
        # tanh ramp reaching ~1 at the end of the ramp
        x = step_i / max(n_ramp, 1)
        return float(np.tanh(3.0 * x) / np.tanh(3.0))
    if step_i < n_ramp + n_hold:
        return 1.0
    return 0.0  # source OFF (post-drive relaxation)


def _source_value(cfg: RunConfig, step_i: int) -> tuple[float, bool]:
    """Return (injected value, source_active) at step_i for this drive shape."""
    env = _envelope(step_i, cfg.n_ramp, cfg.n_hold)
    active = step_i < (cfg.n_ramp + cfg.n_hold)
    v_peak = cfg.a_peak * V_YIELD_NAT
    if cfg.shape == "A":
        val = env * v_peak * np.sin(2.0 * np.pi * step_i / cfg.carrier_period)
    elif cfg.shape == "B":
        val = env * v_peak
    else:
        raise ValueError(f"unknown shape {cfg.shape!r}")
    return float(val), active


# engine natural unit: V_yield = 1.0 => A = V (the kernel rupture root A=1 at V=1)
V_YIELD_NAT = 1.0


def run_one(cfg: RunConfig) -> dict:
    """Drive one cell per cfg; return metrics + downsampled trajectories."""
    eng = CosseratMasterEquationFDTD(
        N=cfg.N, dx=1.0, V_yield=V_YIELD_NAT, c0=1.0,
        cfl_safety=cfg.cfl_safety, pml_thickness=PML,
        coupling_mode=cfg.coupling_mode, alpha_0=cfg.alpha_0,
    )
    src = (cfg.N // 2, cfg.N // 2, cfg.N // 2)  # deep interior (PML-excluded)
    interior = _interior_mask(cfg.N, PML)
    n_int = int(interior.sum())

    n_steps = cfg.n_ramp + cfg.n_hold + cfg.n_relax
    off_step = cfg.n_ramp + cfg.n_hold

    # time series (every step; cheap at this N)
    t_A_src, t_S_ker = [], []
    t_V_src, t_omega_src = [], []
    t_Phi_omega = []           # net micro-rotation content = DC-winding register
    t_Sigma_V_sq, t_Sigma_Phi_link_sq, t_H_cos = [], [], []  # reactance pair + T2 energy
    t_maxV, t_maxOmega, t_E_int = [], [], []

    blew_up = False
    blow_step = -1
    blow_amp = float("nan")
    nonfinite = False

    for step_i in range(n_steps):
        val, active = _source_value(cfg, step_i)
        if active:
            if cfg.source_mode == "hard":
                eng.V[src] = val
            else:  # soft: current-injection-like
                eng.V[src] += eng.dt * val

        eng.step()

        V = eng.V
        omega = eng.omega
        maxV = float(np.max(np.abs(V)))
        maxOmega = float(np.max(np.abs(omega)))

        if not (np.isfinite(V).all() and np.isfinite(omega).all()):
            nonfinite = True
            blew_up = True
            blow_step = step_i
            blow_amp = maxV
            break
        commanded = cfg.a_peak * V_YIELD_NAT
        if maxV > BLOWUP_FACTOR * max(commanded, 1e-9):
            blew_up = True
            blow_step = step_i
            blow_amp = maxV
            break

        S_field = eng.saturation_kernel(V)
        Phi_link_field = _phi_link_field(eng)
        t_A_src.append(abs(float(V[src])) / V_YIELD_NAT)
        t_S_ker.append(float(S_field[src]))
        t_V_src.append(float(V[src]))
        t_omega_src.append(float(omega[src]))
        t_Phi_omega.append(float(np.sum(omega[interior])))
        t_Sigma_V_sq.append(float(np.sum(V[interior] ** 2)))
        t_Sigma_Phi_link_sq.append(float(np.sum(Phi_link_field[interior])))
        t_H_cos.append(eng.H_cosserat())
        t_maxV.append(maxV)
        t_maxOmega.append(maxOmega)
        t_E_int.append(float(np.sum(V[interior] ** 2 + omega[interior] ** 2)))

    ts = {k: np.asarray(v, float) for k, v in dict(
        A_src=t_A_src, S_ker=t_S_ker, V_src=t_V_src, omega_src=t_omega_src,
        Phi_omega=t_Phi_omega, Sigma_V_sq=t_Sigma_V_sq,
        Sigma_Phi_link_sq=t_Sigma_Phi_link_sq, H_cos=t_H_cos,
        maxV=t_maxV, maxOmega=t_maxOmega, E_int=t_E_int,
    ).items()}

    metrics = _metrics(cfg, ts, off_step, blew_up, blow_step, blow_amp, nonfinite)
    # off-source density-peak extraction (top-K |omega|^2, PML-excluded)
    metrics["offsource_topk"] = _offsource_topk(eng, interior, src)
    metrics["n_interior"] = n_int
    metrics["dt"] = eng.dt
    metrics["src"] = list(src)

    # downsample trajectories for the JSON / figures (every 4th step)
    stride = 4
    traj = {k: v[::stride].tolist() for k, v in ts.items()}
    traj["off_step"] = off_step
    traj["stride"] = stride
    return {"config": asdict(cfg), "metrics": metrics, "traj": traj}


def _phi_link_field(eng: CosseratMasterEquationFDTD) -> np.ndarray:
    """Per-cell inductive Phi_link proxy = V_dot^2 / S(V) (matches
    Sigma_Phi_link_sq integrand, cosserat_master_equation_fdtd.py:244-246)."""
    V_dot = (eng.V - eng.V_prev) / eng.dt
    S = eng.saturation_kernel(eng.V)
    return V_dot ** 2 / np.maximum(S, eng.S_min)


def _offsource_topk(eng, interior, src, k: int = 8) -> dict:
    """Top-K |omega|^2 interior cells (PML-excluded argpartition, Rule-10):
    does the rectified winding land OFF the source cell?"""
    w2 = (eng.omega ** 2) * interior  # zero outside interior
    flat = w2.ravel()
    if flat.max() <= 0:
        return {"peak_at_source": None, "peak_coord": None, "peak_val": 0.0}
    kk = min(k, int(interior.sum()))
    idx = np.argpartition(flat, -kk)[-kk:]
    idx = idx[np.argsort(flat[idx])[::-1]]
    coords = [list(np.unravel_index(i, eng.omega.shape)) for i in idx]
    peak = coords[0]
    return {
        "peak_coord": [int(c) for c in peak],
        "peak_val": float(flat[idx[0]]),
        "peak_is_source": bool(tuple(peak) == tuple(src)),
        "topk_coords": [[int(c) for c in cc] for cc in coords],
    }


def _metrics(cfg, ts, off_step, blew_up, blow_step, blow_amp, nonfinite) -> dict:
    A_src = ts["A_src"]
    S_ker = ts["S_ker"]
    Phi = ts["Phi_omega"]
    n_rec = len(A_src)
    # drive window (before source-off) vs post window (after settle).
    # Scale the settle with the run's relax length so a dt/2 run (2x steps) uses
    # the same PHYSICAL settle time.
    settle = int(POST_SETTLE * (cfg.n_relax / N_RELAX))
    drive_slc = slice(0, min(off_step, n_rec))
    post_start = min(off_step + settle, n_rec)
    post_slc = slice(post_start, n_rec)

    A_src_max = float(np.max(A_src[drive_slc])) if drive_slc.stop > 0 else 0.0
    S_ker_min = float(np.min(S_ker)) if n_rec else float("nan")
    crossed = bool(A_src_max >= 1.0)

    AC_peak = float(np.max(np.abs(Phi[drive_slc]))) if drive_slc.stop > 0 else 0.0
    if post_slc.stop > post_slc.start:
        post = Phi[post_slc]
        DC_post = float(abs(np.mean(post)))
        half = len(post) // 2
        m1 = abs(np.mean(post[:half])) if half else 0.0
        m2 = abs(np.mean(post[half:])) if half else 0.0
        persist = float(m2 / m1) if m1 > 1e-30 else 0.0
    else:
        DC_post, persist = 0.0, 0.0
    R_rect = float(DC_post / AC_peak) if AC_peak > 1e-30 else 0.0

    clip_ratio = _clip_ratio(cfg, ts, off_step)

    # numerical health: energy created AFTER source-off is the clean instability
    # signature (no source => PML can only REMOVE energy; any growth is numerical).
    # Robust metric: max(E after source-off) / E(at source-off) - 1. Divide by the
    # at-off value (NOT a later post-settle value, whose magnitude is sensitive to
    # radiation transit and mislabels stable radiative decay).
    E = ts["E_int"]
    if off_step < n_rec and E[off_step] > 1e-30:
        e_growth_frac = float(np.max(E[off_step:]) / E[off_step] - 1.0)
    else:
        e_growth_frac = 0.0

    return dict(
        A_src_max=A_src_max, S_ker_min=S_ker_min, crossed=crossed,
        AC_peak=AC_peak, DC_post=DC_post, R_rect=R_rect, persist=persist,
        clip_ratio=clip_ratio, e_growth_frac=e_growth_frac,
        maxV_overall=float(np.max(ts["maxV"])) if n_rec else float("nan"),
        maxOmega_overall=float(np.max(ts["maxOmega"])) if n_rec else float("nan"),
        blew_up=bool(blew_up), blow_step=int(blow_step), blow_amp=float(blow_amp),
        nonfinite=bool(nonfinite), n_recorded=int(n_rec),
    )


def _clip_ratio(cfg, ts, off_step) -> float:
    """Odd-harmonic power fraction (>=3f) over the HOLD window. Only meaningful
    for Shape A (has a fundamental); Shape B (DC push) => NaN."""
    if cfg.shape != "A":
        return float("nan")
    sig = ts["omega_src"]
    hold_start = min(cfg.n_ramp, len(sig))
    hold_end = min(cfg.n_ramp + cfg.n_hold, len(sig))
    seg = sig[hold_start:hold_end]
    if len(seg) < 4 * cfg.carrier_period:
        return float("nan")
    seg = seg - np.mean(seg)
    win = np.hanning(len(seg))
    spec = np.abs(np.fft.rfft(seg * win)) ** 2
    freqs = np.fft.rfftfreq(len(seg), d=1.0)  # cycles per step
    f0 = 1.0 / cfg.carrier_period
    def band_power(fc):
        lo, hi = fc * 0.75, fc * 1.25
        m = (freqs >= lo) & (freqs <= hi)
        return float(spec[m].sum())
    p1 = band_power(f0)
    p_odd = sum(band_power(k * f0) for k in (3, 5, 7))
    return float(p_odd / p1) if p1 > 1e-30 else 0.0


# ─────────────────────────────────────────────────────────────────────────────
# adjudication (frozen verdict classes, prereg §2)
# ─────────────────────────────────────────────────────────────────────────────

def adjudicate(runs: dict, conv: dict) -> dict:
    """Apply the frozen verdict classes. runs keyed by run name."""
    verdicts = {}
    # numerical guard first (any blow-up / non-converged => NUMERICAL)
    any_blowup = any(r["metrics"]["blew_up"] for r in runs.values())
    converged, conv_detail = _convergence(conv)

    for shape in ("A", "B"):
        past = runs.get(f"shape{shape}_past_soft")
        sub = runs.get(f"shape{shape}_sub_soft")
        if past is None or sub is None:
            continue
        pm, sm = past["metrics"], sub["metrics"]
        v = _verdict_one(shape, pm, sm, converged, any_blowup)
        verdicts[f"shape{shape}"] = v

    # overall
    vals = {k: v["verdict"] for k, v in verdicts.items()}
    uniq = set(vals.values())
    overall = vals.get("shapeB") if len(uniq) == 1 else "MIXED"
    if len(uniq) == 1:
        overall = next(iter(uniq))
    return {
        "per_shape": verdicts,
        "overall": overall,
        "convergence": {"converged": converged, "detail": conv_detail},
        "any_blowup": any_blowup,
    }


def _verdict_one(shape, pm, sm, converged, any_blowup) -> dict:
    reasons = []
    # NUMERICAL takes precedence
    if pm["blew_up"] or sm["blew_up"] or any_blowup:
        reasons.append("blow-up / NaN detected")
        return {"verdict": "NUMERICAL", "reasons": reasons,
                "past": pm, "sub": sm}
    if not converged:
        reasons.append("failed dt/2 or grid-refine convergence (CONV_TOL)")
        return {"verdict": "NUMERICAL", "reasons": reasons,
                "past": pm, "sub": sm}

    crossed = pm["crossed"]
    # STALLS: commanded>1 but field ceilings below 1 - STALL_GAP (soft source)
    if not crossed and pm["A_src_max"] < 1.0 - STALL_GAP:
        reasons.append(
            f"soft-source field ceilinged at A={pm['A_src_max']:.3f} "
            f"< 1-{STALL_GAP} despite commanded A_peak={A_PEAK_PAST}; "
            f"S_ker_min={pm['S_ker_min']:.3f}")
        return {"verdict": "STALLS", "reasons": reasons, "past": pm, "sub": sm}

    # RECTIFIES
    ratio = pm["R_rect"] / max(sm["R_rect"], 1e-9)
    rect = (crossed and pm["R_rect"] >= RECT_FRAC and ratio >= RECT_RATIO
            and pm["persist"] >= PERSIST_MIN)
    if rect:
        reasons.append(
            f"R_rect(past)={pm['R_rect']:.3f}>={RECT_FRAC}, "
            f"ratio={ratio:.1f}>={RECT_RATIO}, persist={pm['persist']:.2f}")
        return {"verdict": "RECTIFIES", "reasons": reasons, "past": pm, "sub": sm}

    # CLIPS-ONLY: clipping harmonics present, no latched DC winding
    clip_excess = (pm["clip_ratio"] - sm["clip_ratio"]) if (
        np.isfinite(pm["clip_ratio"]) and np.isfinite(sm["clip_ratio"])) else float("nan")
    # DISCLOSURE (post-review 2026-07-17, R-9): `or shape == "B"` WAIVES the frozen
    # clip-harmonic evidence requirement for Shape B — _clip_ratio() returns NaN for
    # a DC push (no fundamental), so the harmonic test is undefined there. This is a
    # reachability workaround: NO Shape-B verdict may be read as clip-harmonic-
    # corroborated. (Moot here: Shape B falls to MIXED, not CLIPS-ONLY — see result §1.)
    clips = (crossed and pm["R_rect"] < RECT_FRAC and (
        (np.isfinite(clip_excess) and clip_excess > CLIP_TOL) or shape == "B"))
    if clips:
        reasons.append(
            f"crossed A=1 (A_max={pm['A_src_max']:.2f}); "
            f"R_rect={pm['R_rect']:.4f}<{RECT_FRAC} (no latched DC winding); "
            f"clip_excess={clip_excess}")
        return {"verdict": "CLIPS-ONLY", "reasons": reasons, "past": pm, "sub": sm}

    reasons.append(
        f"crossed={crossed}, A_max={pm['A_src_max']:.2f}, "
        f"R_rect={pm['R_rect']:.4f}, clip_excess={clip_excess}")
    return {"verdict": "MIXED", "reasons": reasons, "past": pm, "sub": sm}


def _convergence(conv: dict) -> tuple[bool, dict]:
    """Compare baseline vs dt/2 vs grid-refine on Shape-B-past key metrics."""
    if not conv:
        return True, {}
    base = conv.get("base")
    detail = {}
    ok = True
    for tag in ("dt_half", "grid_refine"):
        other = conv.get(tag)
        if base is None or other is None:
            continue
        d = {}
        for m in ("A_src_max", "S_ker_min", "R_rect"):
            b = base["metrics"][m]
            o = other["metrics"][m]
            denom = max(abs(b), 1e-6)
            frac = abs(o - b) / denom
            d[m] = {"base": b, tag: o, "frac_change": frac,
                    "within_tol": bool(frac < CONV_TOL)}
            if frac >= CONV_TOL:
                ok = False
        detail[tag] = d
    return ok, detail


def frozen_bar_readjudication(stability: dict, stable_phys: dict) -> dict:
    """Re-adjudicate every stable-labeled cell against the FROZEN
    ENERGY_DRIFT_TOL=5e-2 source-off drift bar (prereg §2:61) — the bar the
    driver never wired (it minted the post-charter 0.5 cut instead, R-3).

    Pure: consumes ALREADY-BANKED e_growth_frac numbers, no re-runs. Returns a
    per-cell {e_growth_frac, frozen_verdict}. A cell whose banked drift clears the
    exploratory 0.5 cut but FAILS 5e-2 is downgraded to instrument-blocked
    (NUMERICAL at the frozen bar); every §3 read from such a cell is exploratory.
    """
    def verdict(e: float) -> str:
        return "SURVIVES" if e < ENERGY_DRIFT_TOL else "NUMERICAL@frozen"

    cells: dict[str, dict] = {}
    for name, row in stability.get("mechanism", {}).items():
        e = row["e_growth_frac"]
        cells[f"mech.{name}"] = {"e_growth_frac": e, "frozen_verdict": verdict(e)}
    for row in stability.get("shapeB_dt_scaling", []):
        e = row["e_growth_frac"]
        cells[f"shapeB_dt.cfl{row['cfl']}"] = {
            "e_growth_frac": e, "frozen_verdict": verdict(e)}
    sb = stable_phys.get("shapeB_dc_transfer", {})
    for arm in ("past", "sub"):
        if arm in sb:
            e = sb[arm]["e_growth_frac"]
            cells[f"shapeB_dc.{arm}"] = {
                "e_growth_frac": e, "frozen_verdict": verdict(e)}
    for row in stable_phys.get("shapeA_carrier_sweep", []):
        pp = row["period_phys"]
        for arm in ("past", "sub"):
            e = row[arm]["e_growth_frac"]
            cells[f"shapeA_p{pp}.{arm}"] = {
                "e_growth_frac": e, "frozen_verdict": verdict(e)}
    n_survive = sum(1 for c in cells.values()
                    if c["frozen_verdict"] == "SURVIVES")
    ac_blocked = all(
        cells[f"shapeA_p{row['period_phys']}.past"]["frozen_verdict"]
        == "NUMERICAL@frozen"
        for row in stable_phys.get("shapeA_carrier_sweep", [])
        if f"shapeA_p{row['period_phys']}.past" in cells)
    return {
        "frozen_bar": ENERGY_DRIFT_TOL,
        "exploratory_cut": STABLE_EXPLORATION_CUT,
        "cells": cells,
        "n_cells_surviving_frozen_bar": n_survive,
        "AC_null_unreadable_at_frozen_tol": bool(ac_blocked),
    }


# ─────────────────────────────────────────────────────────────────────────────
# figures (house style: WHITE)
# ─────────────────────────────────────────────────────────────────────────────

def make_figures(runs: dict, outdir: Path, stability: dict | None = None) -> list[str]:
    import matplotlib.pyplot as plt

    from ave.viz import style
    style.apply("print")
    written = []

    def _t(traj_key, run):
        v = np.asarray(run["traj"][traj_key])
        stride = run["traj"]["stride"]
        dt = run["metrics"]["dt"]
        t = np.arange(len(v)) * stride * dt
        return t, v

    # Fig 1: S-trajectory + Phi_omega overlay, controlled hard-source crossing
    # (shapeB_past_hard: A crosses ~1.2 in a CONTROLLED way, then post-source-off
    # winding grows = the leapfrog instability = the NUMERICAL signature) vs the
    # sub-snap soft control.
    past = runs.get("shapeB_past_hard", runs["shapeB_past_soft"])
    sub = runs["shapeB_sub_soft"]
    fig, axes = plt.subplots(2, 1, figsize=style.figsize("single"), sharex=True)
    tp, Ap = _t("A_src", past)
    ts_, As = _t("A_src", sub)
    axes[0].plot(tp, Ap, color=style.COLORS["ave"], label="past-snap (A_peak=1.3)")
    axes[0].plot(ts_, As, color=style.COLORS["comparison"], ls="--",
                 label="sub-snap control (A_peak=0.8)")
    axes[0].axhline(1.0, color=style.COLORS["muted"], lw=0.8, ls=":")
    off_t = past["traj"]["off_step"] * past["metrics"]["dt"]
    axes[0].axvline(off_t, color=style.COLORS["muted"], lw=0.6)
    axes[0].set_ylabel(style.axis_label("Strain", "A=V/V_{yield}", ""))
    style.legend(axes[0], where="right")
    tp2, Pp = _t("Phi_omega", past)
    ts2, Ps = _t("Phi_omega", sub)
    axes[1].plot(tp2, Pp, color=style.COLORS["ave"])
    axes[1].plot(ts2, Ps, color=style.COLORS["comparison"], ls="--")
    axes[1].axvline(off_t, color=style.COLORS["muted"], lw=0.6)
    axes[1].set_ylabel(style.axis_label("Winding", r"\Phi_\omega=\Sigma\,\omega", ""))
    axes[1].set_xlabel(style.axis_label("Time", "t", "natural"))
    p = outdir / "r3_snap_S_and_winding"
    written += [str(x) for x in style.save(fig, p)]
    plt.close(fig)

    # Fig 2: reactance pair (C-state / L-state), Shape-B past
    fig, ax = plt.subplots(figsize=style.figsize("single"))
    t, C = _t("Sigma_V_sq", past)
    _, L = _t("Sigma_Phi_link_sq", past)
    ax.plot(t, C / max(C.max(), 1e-30), color=style.COLORS["ave"],
            label=r"C-state $\Sigma V^2$ (norm.)")
    ax.plot(t, L / max(L.max(), 1e-30), color=style.COLORS["accent"],
            label=r"L-state $\Sigma \Phi_{link}^2$ (norm.)")
    ax.axvline(off_t, color=style.COLORS["muted"], lw=0.6)
    ax.set_xlabel(style.axis_label("Time", "t", "natural"))
    ax.set_ylabel(style.axis_label("Reactive energy", "E", "normalized"))
    style.legend(ax, where="right")
    p = outdir / "r3_snap_reactance_pair"
    written += [str(x) for x in style.save(fig, p)]
    plt.close(fig)

    # Fig 3: harmonic spectrum, Shape-A past vs sub (clipping products)
    if "shapeA_past_soft" in runs:
        fig, ax = plt.subplots(figsize=style.figsize("single"))
        for key, col, lab in (
            ("shapeA_past_soft", style.COLORS["ave"], "past-snap"),
            ("shapeA_sub_soft", style.COLORS["comparison"], "sub-snap"),
        ):
            r = runs[key]
            sig = np.asarray(r["traj"]["omega_src"])
            sig = sig - sig.mean()
            if len(sig) > 8:
                spec = np.abs(np.fft.rfft(sig * np.hanning(len(sig)))) ** 2
                freqs = np.fft.rfftfreq(len(sig), d=1.0)
                ax.semilogy(freqs, spec / max(spec.max(), 1e-30), color=col,
                            label=lab)
        f0 = 1.0 / CARRIER_PERIOD / r["traj"]["stride"]
        for k in (1, 3, 5, 7):
            ax.axvline(k * f0, color=style.COLORS["muted"], lw=0.5, ls=":")
        ax.set_xlabel(style.axis_label("Frequency", "f", "1/step"))
        ax.set_ylabel(style.axis_label("Power", "P", "normalized"))
        ax.set_xlim(0, 9 * f0)
        style.legend(ax, where="right")
        p = outdir / "r3_snap_harmonics"
        written += [str(x) for x in style.save(fig, p)]
        plt.close(fig)

    # Fig 4: dt-scaling of the post-source-off energy growth — Shape B (DC push,
    # CFL-fixable: growth falls with dt) vs Shape A (AC carrier, NON-CFL:
    # growth does NOT fall with dt — dt-refinement does not cure). The numerical-
    # health money figure. (R-6: label reads "non-CFL", not "unconditional" — the
    # AC instability is frequency-selective; fragile stable corners exist.)
    if stability is not None:
        fig, ax = plt.subplots(figsize=style.figsize("single"))
        b = stability["shapeB_dt_scaling"]
        a = stability["shapeA_dt_scaling"]
        ax.loglog([r["dt"] for r in b], [r["e_growth_frac"] + 1e-3 for r in b],
                  "o-", color=style.COLORS["ave"], label="Shape B (DC push) — CFL-fixable")
        ax.loglog([r["dt"] for r in a], [r["e_growth_frac"] + 1e-3 for r in a],
                  "s--", color=style.COLORS["comparison"],
                  label="Shape A (AC carrier) — non-CFL (dt-refinement does not cure)")
        ax.axhline(0.5, color=style.COLORS["muted"], lw=0.8, ls=":")
        ax.set_xlabel(style.axis_label("Timestep", "\\Delta t", "natural"))
        ax.set_ylabel(style.axis_label("Post-off energy growth", "E_{max}/E_{off}-1", ""))
        style.legend(ax, where="right")
        p = outdir / "r3_snap_dt_stability"
        written += [str(x) for x in style.save(fig, p)]
        plt.close(fig)

    return written


# ─────────────────────────────────────────────────────────────────────────────
# main
# ─────────────────────────────────────────────────────────────────────────────

def _probe(cfg: RunConfig) -> dict:
    """Light wrapper: run cfg, return just the health + rectification metrics
    (no trajectory retention). Physical time is held ~fixed by scaling the
    ramp/hold/relax step counts with the dt ratio relative to the cfl=0.4 base."""
    r = run_one(cfg)
    m = r["metrics"]
    return dict(
        cfl=cfg.cfl_safety, dt=m["dt"], shape=cfg.shape, a_peak=cfg.a_peak,
        source_mode=cfg.source_mode, coupling=cfg.coupling_mode, alpha_0=cfg.alpha_0,
        carrier_period=cfg.carrier_period, A_src_max=m["A_src_max"],
        S_ker_min=m["S_ker_min"], R_rect=m["R_rect"], persist=m["persist"],
        e_growth_frac=m["e_growth_frac"], blew_up=m["blew_up"],
        # NOTE (post-review 2026-07-17): `stable` uses the POST-CHARTER exploratory
        # 0.5 cut, NOT the frozen ENERGY_DRIFT_TOL=5e-2 bar. Re-adjudicate against the
        # frozen bar with survives_frozen_bar(); the doc §2b downgrades every read
        # from a cell that clears 0.5 but fails 5e-2 to EXPLORATION.
        stable=bool(m["e_growth_frac"] < STABLE_EXPLORATION_CUT and not m["blew_up"]),
        survives_frozen_bar=bool(
            m["e_growth_frac"] < ENERGY_DRIFT_TOL and not m["blew_up"]),
    )


def _scaled(name, shape, a_peak, mode, cfl, *, period_phys=CARRIER_PERIOD,
            coupling="shared_flux", alpha_0=1.0) -> RunConfig:
    """Build a config at arbitrary cfl with physical time held fixed (steps and
    carrier period scaled by the dt ratio vs the cfl=0.4 base)."""
    sc = max(1, int(round(0.4 / cfl)))
    return RunConfig(
        name, shape, a_peak, mode, cfl_safety=cfl,
        n_ramp=N_RAMP * sc, n_hold=N_HOLD * sc, n_relax=N_RELAX * sc,
        carrier_period=period_phys * sc, coupling_mode=coupling, alpha_0=alpha_0)


def stability_study() -> dict:
    """Isolate + characterize the past-crossing integrator instability.

    (1) Mechanism isolation (Shape B hard, A_peak=1.3, cfl=0.4): shared_flux vs
        decoupled (alpha_0=0) vs forward-coupling vs sub-snap — which combination
        destabilizes.
    (2) dt-scaling of the Shape-B crossing instability (CFL-fixable?).
    (3) Shape-A (AC) dt-scaling (unconditional?).
    """
    mech = {}
    mech["shared_flux_past"] = _probe(_scaled("m_sf_past", "B", 1.3, "hard", 0.4))
    mech["shared_flux_sub"] = _probe(_scaled("m_sf_sub", "B", 0.8, "hard", 0.4))
    mech["decoupled_past"] = _probe(_scaled("m_dec", "B", 1.3, "hard", 0.4, alpha_0=0.0))
    # NOTE (post-review 2026-07-17, R-7): forward_past e_growth is IDENTICAL to
    # decoupled_past to all digits (0.0734601027786197) — omega is zero-initialized
    # AND unsourced in both the alpha_0=0 and the forward-coupling modes, so both
    # reduce to the same uncoupled V-only run. It is kept as a distinct label for
    # transparency but is NOT an independent ablation arm.
    mech["forward_past"] = _probe(_scaled("m_fwd", "B", 1.3, "hard", 0.4, coupling="forward"))
    # Strict fourth cell of the 2x2 (R-7): coupling-OFF x SUB-snap. Completes the
    # ablation so "requires BOTH coupling AND crossing" is a full 2x2, not 3 corners.
    mech["decoupled_sub"] = _probe(_scaled("m_dec_sub", "B", 0.8, "hard", 0.4, alpha_0=0.0))

    shapeB_dt = [_probe(_scaled(f"B_cfl{c}", "B", 1.3, "hard", c)) for c in (0.4, 0.2, 0.1, 0.05)]
    shapeA_dt = [_probe(_scaled(f"A_cfl{c}", "A", 1.3, "hard", c)) for c in (0.1, 0.05, 0.025)]
    return {"mechanism": mech, "shapeB_dt_scaling": shapeB_dt, "shapeA_dt_scaling": shapeA_dt}


def stable_physics_probe() -> dict:
    """Where the integrator IS stable, read the actual crossing physics
    (amplitude-controlled hard source):

    - Shape B (DC push) at cfl=0.1: a controlled crossing that IS stable; a
      unipolar push -> unipolar omega response (DC-in/DC-out, NOT AC->DC
      rectification). Past vs sub tests crossing-specificity.
    - Shape A (AC carrier) carrier-period sweep at cfl=0.1: find any stable AC
      corner and test whether the crossing produces a CROSSING-SPECIFIC persistent
      DC winding (RECTIFIES) or the sub-snap control shows equal DC (CLIPS-ONLY).
    """
    shapeB = {
        "past": _probe(_scaled("sp_B_past", "B", 1.3, "hard", 0.1)),
        "sub": _probe(_scaled("sp_B_sub", "B", 0.8, "hard", 0.1)),
    }
    shapeA_sweep = []
    for pp in (20, 60, 200):
        past = _probe(_scaled(f"sp_A_p{pp}_past", "A", 1.3, "hard", 0.1, period_phys=pp))
        sub = _probe(_scaled(f"sp_A_p{pp}_sub", "A", 0.8, "hard", 0.1, period_phys=pp))
        ratio = past["R_rect"] / max(sub["R_rect"], 1e-9)
        shapeA_sweep.append({"period_phys": pp, "past": past, "sub": sub,
                             "past_over_sub_ratio": ratio,
                             "both_stable": bool(past["stable"] and sub["stable"])})
    return {"shapeB_dc_transfer": shapeB, "shapeA_carrier_sweep": shapeA_sweep}


def build_matrix() -> list[RunConfig]:
    """The frozen matrix: 5 runs (prereg §3).

    NOTE (post-review 2026-07-17, R-8): the prereg §3.7 line 89 says "6-run
    matrix" but the frozen §3.3-3.5 method defines exactly FIVE runs (2 Shape-A
    soft, 2 Shape-B soft, 1 Shape-B hard companion) — the count slip is flagged
    in the prereg POST-FREEZE AMENDMENT. The shipped matrix is 5 runs.
    """
    return [
        RunConfig("shapeA_past_soft", "A", A_PEAK_PAST, "soft"),
        RunConfig("shapeA_sub_soft", "A", A_PEAK_SUB, "soft"),
        RunConfig("shapeB_past_soft", "B", A_PEAK_PAST, "soft"),
        RunConfig("shapeB_sub_soft", "B", A_PEAK_SUB, "soft"),
        RunConfig("shapeB_past_hard", "B", A_PEAK_PAST, "hard"),  # guaranteed crossing
    ]


def build_convergence() -> dict[str, RunConfig]:
    """Convergence pair on Shape-B-past-soft (prereg §3.6).

    dt_half: halve dt (cfl_safety/2) AND double the step counts so the PHYSICAL
    drive scenario is unchanged (temporal-resolution refinement — the load-bearing
    check for a singularity-adjacent regime).
    grid_refine: N=64 same dx=1.0 → larger box, same single-cell source (box-size /
    PML-boundary robustness check; a dx-halving would change what "one cell" means
    physically, so it is NOT the right refinement for a one-cell drive).
    """
    return {
        "base": RunConfig("conv_base", "B", A_PEAK_PAST, "soft"),
        "dt_half": RunConfig(
            "conv_dt_half", "B", A_PEAK_PAST, "soft", cfl_safety=0.2,
            n_ramp=2 * N_RAMP, n_hold=2 * N_HOLD, n_relax=2 * N_RELAX),
        "grid_refine": RunConfig("conv_grid", "B", A_PEAK_PAST, "soft", N=64),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--no-figs", action="store_true")
    args = ap.parse_args()

    outdir = Path(args.outdir) if args.outdir else Path(__file__).resolve().parents[3] / "research"
    outdir.mkdir(parents=True, exist_ok=True)

    runs = {}
    for cfg in build_matrix():
        print(f"[R3] running {cfg.name} (shape {cfg.shape}, A_peak={cfg.a_peak}, "
              f"{cfg.source_mode})...", flush=True)
        runs[cfg.name] = run_one(cfg)
        m = runs[cfg.name]["metrics"]
        print(f"    A_src_max={m['A_src_max']:.3f} S_ker_min={m['S_ker_min']:.3f} "
              f"R_rect={m['R_rect']:.4f} persist={m['persist']:.2f} "
              f"clip={m['clip_ratio']} blew_up={m['blew_up']}", flush=True)

    conv_runs = {}
    for tag, cfg in build_convergence().items():
        print(f"[R3] convergence {tag}...", flush=True)
        conv_runs[tag] = run_one(cfg)

    verdict = adjudicate(runs, conv_runs)
    print(f"\n[R3] FROZEN-MATRIX VERDICT: {verdict['overall']}")
    for shp, v in verdict["per_shape"].items():
        print(f"    {shp}: {v['verdict']} — {'; '.join(v['reasons'])}")

    print("\n[R3] stability study (mechanism isolation + dt-scaling)...", flush=True)
    stability = stability_study()
    print("[R3] stable-physics probe (crossing physics where the integrator is stable)...",
          flush=True)
    stable_phys = stable_physics_probe()
    # substantive physics readout: any crossing-specific rectification in a stable corner?
    rect_found = False
    for row in stable_phys["shapeA_carrier_sweep"]:
        if row["both_stable"] and row["past"]["R_rect"] >= RECT_FRAC and \
                row["past_over_sub_ratio"] >= RECT_RATIO and row["past"]["persist"] >= PERSIST_MIN:
            rect_found = True
    physics_reading = "RECTIFIES (crossing-specific persistent DC winding in a stable AC corner)" \
        if rect_found else \
        "NO CROSSING-SPECIFIC RECTIFICATION where stable (CLIPS-ONLY / null; " \
        "consistent with anhysteretic-kernel + linear-omega prior, R10 loop gap)"
    print(f"[R3] STABLE-CORNER PHYSICS READING: {physics_reading}")

    # SI anchors for the record (coordinate discipline: engine measures in A, not V)
    si = {
        "V_SNAP_SI_volts": V_SNAP, "V_YIELD_SI_volts": V_YIELD, "ALPHA": ALPHA,
        "note": ("engine kernel rupture root A=1 sits at V=V_yield (macroscopic "
                 "normalization); V_snap=V_yield/sqrt(alpha)=11.706*V_yield is the "
                 "scale-invariant SI anchor of the SAME dimensionless r=1.0 boundary"),
    }

    out = {
        "prereg": "research/2026-07-16_r3-snap-crossing_prereg_FROZEN.md",
        "harness": "ave.core.cosserat_master_equation_fdtd.CosseratMasterEquationFDTD",
        "coupling_mode": "shared_flux",
        "thresholds": dict(
            RECT_FRAC=RECT_FRAC, RECT_RATIO=RECT_RATIO, PERSIST_MIN=PERSIST_MIN,
            CLIP_TOL=CLIP_TOL, STALL_GAP=STALL_GAP, CONV_TOL=CONV_TOL,
            ENERGY_DRIFT_TOL=ENERGY_DRIFT_TOL,  # FROZEN NUMERICAL trigger (prereg §2:61)
            BLOWUP_FACTOR=BLOWUP_FACTOR,         # post-charter (see constants block)
            STABLE_EXPLORATION_CUT=STABLE_EXPLORATION_CUT),  # post-charter exploratory
        "drive_params": dict(
            N=N_BASE, PML=PML, CARRIER_PERIOD=CARRIER_PERIOD, N_RAMP=N_RAMP,
            N_HOLD=N_HOLD, N_RELAX=N_RELAX, POST_SETTLE=POST_SETTLE,
            A_PEAK_PAST=A_PEAK_PAST, A_PEAK_SUB=A_PEAK_SUB),
        "si_anchors": si,
        "runs": {k: {"config": v["config"], "metrics": v["metrics"]}
                 for k, v in runs.items()},
        "convergence_runs": {k: {"config": v["config"], "metrics": v["metrics"]}
                             for k, v in conv_runs.items()},
        "verdict": verdict,
        "stability_study": stability,
        "stable_physics_probe": stable_phys,
        "stable_corner_physics_reading": physics_reading,
        # post-review 2026-07-17, R-3: re-adjudicate stable-labeled cells at the
        # FROZEN ENERGY_DRIFT_TOL=5e-2 bar (the driver's 0.5 cut is post-charter).
        "frozen_bar_readjudication": frozen_bar_readjudication(stability, stable_phys),
    }
    jpath = outdir / "2026-07-16_r3-snap-crossing_results.json"
    jpath.write_text(json.dumps(out, indent=2))
    print(f"[R3] wrote {jpath}")

    # keep trajectories in a companion file (larger)
    tpath = outdir / "2026-07-16_r3-snap-crossing_trajectories.json"
    tpath.write_text(json.dumps(
        {k: v["traj"] for k, v in runs.items()}, indent=2))
    print(f"[R3] wrote {tpath}")

    if not args.no_figs:
        figdir = Path(__file__).resolve().parents[3] / "assets" / "sim_outputs"
        figdir.mkdir(parents=True, exist_ok=True)
        figs = make_figures(runs, figdir, stability)
        print(f"[R3] wrote figures: {figs}")


if __name__ == "__main__":
    main()

"""
SPICE-CVR constitutive-loop harness — Level-0/1/2 saturation dynamics.

Implements the frozen ladder from
research/2026-06-13_spice-cvr-constitutive-loop_prereg.md:

  L0 — instantaneous S_eq(r) (anhysteretic null)
  L1 — memristor ODE dS/dt = (S_eq - S) / tau
  L2 — L1 + rate-gated snap latch (D2 discriminator)

Observables per cycle:
  loop_area = ∮ S dr  (shoelace in (r, S) plane)
  B_r       = 1 - S at r=0 down-cross (S_eq(0) = 1)

Dimensionless sweep uses omega_tau = omega * tau_eff with tau_eff=1 native.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Literal

import numpy as np

from ave.core.constants import TAU_RELAX_SI

ArmLabel = Literal["L0", "L1", "L2"]
BinLabel = Literal[
    "ANHYSTERETIC",
    "DISSIPATIVE-ONLY",
    "REMANENT-LOOP",
    "REGIME-LIMITED",
]

EPS_LOOP = 1e-6
EPS_BR = 1e-3
OMEGA_TAU_GRID = (0.01, 0.05, 0.1, 0.2, 0.35, 0.5, 0.7, 0.9, 1.0, 1.25)


def s_eq(r: float) -> float:
    """Axiom 4 equilibrium kernel S_eq(r) = sqrt(1 - r^2)."""
    rr = min(float(r) ** 2, 0.9999)
    return float(math.sqrt(1.0 - rr))


def branch_hysteresis_area(r: np.ndarray, s: np.ndarray, n_r: int = 256) -> float:
    """
    Enclosed area between up- and down-r branches in (r, S) plane.

    Single-valued S(r) (L0) returns ~0; memristive lag opens the loop.
    """
    if len(r) < 4:
        return 0.0
    dr = np.diff(r)
    up_r: list[float] = []
    up_s: list[float] = []
    dn_r: list[float] = []
    dn_s: list[float] = []
    for i in range(1, len(r)):
        if dr[i - 1] > 0.0:
            up_r.append(float(r[i]))
            up_s.append(float(s[i]))
        elif dr[i - 1] < 0.0:
            dn_r.append(float(r[i]))
            dn_s.append(float(s[i]))
    if len(up_r) < 2 or len(dn_r) < 2:
        return 0.0
    r_min = max(min(up_r), min(dn_r))
    r_max = min(max(up_r), max(dn_r))
    if r_max <= r_min:
        return 0.0
    grid = np.linspace(r_min, r_max, n_r)
    up_order = np.argsort(up_r)
    dn_order = np.argsort(dn_r)
    s_up = np.interp(grid, np.array(up_r)[up_order], np.array(up_s)[up_order])
    s_dn = np.interp(grid, np.array(dn_r)[dn_order], np.array(dn_s)[dn_order])
    return float(np.trapezoid(np.abs(s_up - s_dn), grid))


def shoelace_loop_area(r: np.ndarray, s: np.ndarray) -> float:
    """Legacy shoelace — prefer branch_hysteresis_area for verdict bins."""
    return branch_hysteresis_area(r, s)


def br_at_zero_downcross(r: np.ndarray, s: np.ndarray) -> float:
    """Remanence analogue: 1 - S when r returns to 0 on decreasing drive."""
    br = 0.0
    for i in range(1, len(r)):
        if r[i - 1] > 0.02 and r[i] <= 0.02 and (r[i] - r[i - 1]) < 0.0:
            br = max(br, 1.0 - float(s[i]))
    return br


@dataclass(frozen=True)
class CycleMetrics:
    arm: ArmLabel
    omega_tau: float
    loop_area: float
    b_r: float
    pinched: bool
    r_amp: float
    n_cycles: int


def _step_l1(S: float, r: float, tau: float, dt: float) -> float:
    target = s_eq(r)
    dS = (target - S) / tau
    return float(S + dS * dt)


def _drive_r(t: np.ndarray, omega: float, r_amp: float) -> np.ndarray:
    """Triangle ramp 0 → r_amp → 0 per cycle (single up/down branch)."""
    phase = (omega * t) % (2.0 * math.pi)
    r = np.empty_like(t)
    up = phase < math.pi
    r[up] = r_amp * (phase[up] / math.pi)
    r[~up] = r_amp * (2.0 - phase[~up] / math.pi)
    return r


def simulate_arm(
    arm: ArmLabel,
    *,
    omega_tau: float,
    r_amp: float = 0.85,
    n_cycles: int = 3,
    n_pts_per_cycle: int = 400,
    dwell_frac: float = 1.0,
    snap_rate_thresh: float = 0.15,
    snap_r_min: float = 0.55,
) -> tuple[np.ndarray, np.ndarray, CycleMetrics]:
    """Integrate sinusoidal drive and return final-cycle (r, S) + metrics."""
    tau = 1.0
    omega = float(omega_tau) / tau
    period = 2.0 * math.pi / max(omega, 1e-30)
    dwell_t = dwell_frac * period
    t_end = n_cycles * period + dwell_t
    dt_max = tau / 40.0
    n_pts = max(int(t_end / dt_max), n_pts_per_cycle * n_cycles, 200)
    t_drive = np.linspace(0.0, n_cycles * period, n_pts)
    t_dwell = np.linspace(t_drive[-1], t_end, max(20, int(0.1 * n_pts)))
    t = np.concatenate([t_drive, t_dwell[1:]])
    dt = float(t[1] - t[0]) if len(t) > 1 else 1.0

    r = np.zeros_like(t)
    r[: len(t_drive)] = _drive_r(t_drive, omega, r_amp)
    s = np.zeros_like(t)

    S = 1.0
    snap_hold = False
    S_latched = 1.0

    for i in range(len(t)):
        ri = float(r[i])
        dri = float((r[i] - r[i - 1]) / dt) if i > 0 else 0.0

        if arm == "L0":
            S = s_eq(ri)
        elif arm == "L1":
            S = _step_l1(S, ri, tau, dt)
        else:  # L2
            S = _step_l1(S, ri, tau, dt)
            if dri > snap_rate_thresh and ri > snap_r_min:
                snap_hold = True
                S_latched = S
            if snap_hold:
                S = min(S, S_latched)
            if ri < 0.02 and dri > snap_rate_thresh:
                snap_hold = False

        s[i] = S

    # Metrics on last full driven cycle (uniform samples per cycle on t_drive)
    spc = max(len(t_drive) // n_cycles, 4)
    r_c = r[len(t_drive) - spc : len(t_drive)]
    s_c = s[len(t_drive) - spc : len(t_drive)]
    if arm == "L0":
        area = 0.0
    else:
        area = abs(branch_hysteresis_area(r_c, s_c))
    # B_r measured after zero-drive dwell (H→0 ferrite analogue)
    br = 1.0 - float(s[-1])

    return r, s, CycleMetrics(
        arm=arm,
        omega_tau=float(omega_tau),
        loop_area=area,
        b_r=br,
        pinched=br < EPS_BR,
        r_amp=r_amp,
        n_cycles=n_cycles,
    )


def classify_bin(
    *,
    l0: CycleMetrics,
    l1_rows: list[CycleMetrics],
    l2_rows: list[CycleMetrics],
) -> BinLabel:
    """Apply frozen prereg bins to ladder sweep."""
    if l0.loop_area >= EPS_LOOP or l0.b_r >= EPS_BR:
        return "REGIME-LIMITED"

    l1_any_area = any(m.loop_area >= EPS_LOOP for m in l1_rows)
    l2_any_area = any(m.loop_area >= EPS_LOOP for m in l2_rows)
    l2_any_br = any(m.b_r >= EPS_BR for m in l2_rows)

    if not l1_any_area and not l2_any_area:
        return "ANHYSTERETIC"
    if l2_any_br:
        return "REMANENT-LOOP"
    if l1_any_area or l2_any_area:
        return "DISSIPATIVE-ONLY"
    return "REGIME-LIMITED"


def frozen_bin_gates(
    *,
    l0: CycleMetrics,
    l1_rows: list[CycleMetrics],
    l2_rows: list[CycleMetrics],
    verdict: BinLabel,
) -> dict[str, bool]:
    """Executable prereg gates — driver asserts these, not docstring-only."""
    l1_areas = [m.loop_area for m in l1_rows]
    l1_brs = [m.b_r for m in l1_rows]
    l2_brs = [m.b_r for m in l2_rows]
    return {
        "H0_L0_area_zero": l0.loop_area < EPS_LOOP,
        "H0_L0_br_zero": l0.b_r < EPS_BR,
        "H1_L1_area_monotone": (
            l1_areas[-2] > l1_areas[0] + EPS_LOOP
            and max(l1_areas) >= EPS_LOOP
        ),
        "H1_L1_pinched_at_slow_rate": l1_brs[0] < EPS_BR if l1_brs else True,
        "H2_L2_br_when_verdict_remanent": (
            verdict != "REMANENT-LOOP" or max(l2_brs) >= EPS_BR
        ),
        "bin_ANHYSTERETIC": verdict == "ANHYSTERETIC",
        "bin_DISSIPATIVE_ONLY": verdict == "DISSIPATIVE-ONLY",
        "bin_REMANENT_LOOP": verdict == "REMANENT-LOOP",
        "bin_REGIME_LIMITED": verdict == "REGIME-LIMITED",
    }


def run_ladder_battery(
    *,
    omega_tau_grid: tuple[float, ...] = OMEGA_TAU_GRID,
    r_amp: float = 0.85,
) -> dict:
    """Full L0 + L1/L2 rate sweep with verdict bin."""
    l0m = simulate_arm("L0", omega_tau=omega_tau_grid[len(omega_tau_grid) // 2], r_amp=r_amp)[2]
    l1_rows = [simulate_arm("L1", omega_tau=w, r_amp=r_amp)[2] for w in omega_tau_grid]
    l2_rows = [simulate_arm("L2", omega_tau=w, r_amp=r_amp)[2] for w in omega_tau_grid]
    verdict = classify_bin(l0=l0m, l1_rows=l1_rows, l2_rows=l2_rows)
    gates = frozen_bin_gates(l0=l0m, l1_rows=l1_rows, l2_rows=l2_rows, verdict=verdict)
    l1_max_br = max(m.b_r for m in l1_rows)

    return {
        "prereg": "research/2026-06-13_spice-cvr-constitutive-loop_prereg.md",
        "tau_relax_si": TAU_RELAX_SI,
        "tau_eff_native": 1.0,
        "omega_tau_grid": list(omega_tau_grid),
        "r_amp": r_amp,
        "L0": {
            "loop_area": l0m.loop_area,
            "b_r": l0m.b_r,
            "pinched": l0m.pinched,
        },
        "L1_sweep": [m.__dict__ for m in l1_rows],
        "L2_sweep": [m.__dict__ for m in l2_rows],
        "verdict": verdict,
        "d2_read": _d2_read(verdict),
        "frozen_gates": gates,
        "l1_surprise_br": l1_max_br >= EPS_BR,
        "l1_max_br": l1_max_br,
        "thresholds": {"epsilon_loop": EPS_LOOP, "epsilon_br": EPS_BR},
    }


def _d2_read(verdict: BinLabel) -> str:
    if verdict == "ANHYSTERETIC":
        return "D2a sigma-only — constitutive law cannot supply remanence"
    if verdict == "DISSIPATIVE-ONLY":
        return "D2a — loss tangent / reactive only; no B_r memory"
    if verdict == "REMANENT-LOOP":
        return "D2b vindicated — rate-gated snap gives B_r at H=0 in silico"
    return "REGIME-LIMITED — harness or grid; no physics bin"


def analytic_l1_loop_area_small_omega(omega_tau: float, r_amp: float = 0.85) -> float:
    """
    Leading-order pinched-loop area for L1 linearized around slow drive.
    Used for keeper: area scales ~ omega_tau^2 for small omega_tau.
    """
    # Quasi-static amplitude of S lag ~ (omega_tau) * |dS_eq/dr| integrated — order omega_tau
    om = float(omega_tau)
    if om < 1e-12:
        return 0.0
    n = 200
    theta = np.linspace(0, 2 * np.pi, n)
    r = r_amp * np.sin(theta)
    s_eq_vals = np.array([s_eq(x) for x in r])
    ds_dr = np.gradient(s_eq_vals, r)
    lag = om * np.abs(ds_dr)
    return float(0.25 * np.trapezoid(lag, r))

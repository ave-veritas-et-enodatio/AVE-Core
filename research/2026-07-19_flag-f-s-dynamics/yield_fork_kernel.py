"""Shared canonical Level-2 saturation kernel for the yield-fork discriminators.

Byte-locked to the engine (engine itself is NOT edited):
  - S_eq(r) = sqrt(max(0, 1 - min(r,1)^2))        [k4_tlm.py:283]
  - backward Euler S_{n+1} = (S_n*tau + dt*S_eq)/(tau + dt)   [k4_tlm.py:291]

All in engine-native units (c=1, ell_node=1, V_SNAP=1, m_e c^2=1), so
r == V/V_SNAP and tau_relax == TAU_RELAX_NATIVE == 1.0.

Frozen protocols:
  research/2026-06-09_thixotropy-amplitude-dependent-tau_prereg.md  (Leg A, sec A.*)
  research/2026-07-19_yield-fork-loop-area_PROTOCOL-COMPLETION.md   (Leg B)
"""

from __future__ import annotations

import numpy as np


def s_eq(r: np.ndarray | float) -> np.ndarray | float:
    """Equilibrium Ax4 saturation kernel. Verbatim k4_tlm.py:283 form."""
    r = np.asarray(r, dtype=float)
    return np.sqrt(np.maximum(0.0, 1.0 - np.minimum(np.abs(r), 1.0) ** 2))


def be_step(S: float, Seq: float, tau: float, dt: float) -> float:
    """Backward-Euler step of dS/dt = (S_eq - S)/tau. Verbatim k4_tlm.py:291."""
    return (S * tau + dt * Seq) / (tau + dt)


def tau_const(_A: float, _dr_sign: int, tau_relax: float) -> float:
    """Single-tau canonical model: tau independent of amplitude AND rate sign."""
    return tau_relax


def tau_two(_A: float, dr_sign: int, tau_relax: float, ratio: float = 3.0) -> float:
    """Explicit two-tau positive control (sign(dr/dt) MEMORY).

    Fast-liquefy / slow-refreeze: tau_up on up-stroke (dr/dt>0), tau_down =
    ratio*tau_up on down-stroke. tau_up chosen so the geometric mean matches
    tau_relax (keeps the loop in the same omega*tau band as the canonical run).
    """
    tau_up = tau_relax / np.sqrt(ratio)
    return tau_up if dr_sign > 0 else ratio * tau_up


def tau_amp(A: float, _dr_sign: int, tau_relax: float, kappa: float = 1.0) -> float:
    """Amplitude-dependent EVEN tau(A) = tau_relax*(1 + kappa*A^2).

    The #59 Flag-A near-saturation L_eff(A) stiffening cast as an even
    function of A (no sign(dr/dt) dependence). kappa is an engineering probe
    value (tagged, not a canonical magnitude).
    """
    return tau_relax * (1.0 + kappa * A * A)


def drive(r0: float, dr: float, omega: float, t: np.ndarray) -> np.ndarray:
    """Symmetric drive r(t) = r0 + dr*sin(omega t)."""
    return r0 + dr * np.sin(omega * t)


def integrate_cycle(
    r0: float,
    dr: float,
    omega_tau: float,
    tau_relax: float = 1.0,
    tau_fn=tau_const,
    n_ppp: int = 512,
    settle_periods: int = 8,
    settle_tau: float = 20.0,
    tau_cap_frac: float = 50.0,
    S0: float = 1.0,
    **tau_kwargs,
) -> dict:
    """Drive the Level-2 ODE to steady state and return the last-period series.

    omega_tau = omega * tau_relax (native: omega since tau_relax=1).
    Returns dict with the last full period's t, r, S, Seq arrays plus dt, omega.
    """
    omega = omega_tau / tau_relax
    period = 2.0 * np.pi / omega
    # dt = min(period/n_ppp, tau/tau_cap_frac); steps-per-period from that dt.
    dt = min(period / n_ppp, tau_relax / tau_cap_frac)
    steps_per_period = int(np.ceil(period / dt))
    dt = period / steps_per_period  # make an integer number of steps per period

    settle_steps = int(np.ceil(max(settle_periods * period, settle_tau * tau_relax) / dt))

    S = float(S0)
    # settle
    r_prev = drive(r0, dr, omega, np.array([0.0]))[0]
    for n in range(settle_steps):
        t = (n + 1) * dt
        r = drive(r0, dr, omega, np.array([t]))[0]
        A = abs(r)
        dr_sign = 1 if (r - r_prev) >= 0.0 else -1
        tau = tau_fn(A, dr_sign, tau_relax, **tau_kwargs)
        S = be_step(S, float(s_eq(r)), tau, dt)
        r_prev = r

    # record last full period
    t_arr = np.empty(steps_per_period + 1)
    r_arr = np.empty(steps_per_period + 1)
    S_arr = np.empty(steps_per_period + 1)
    Seq_arr = np.empty(steps_per_period + 1)
    t0 = settle_steps * dt
    t_arr[0] = t0
    r_arr[0] = r_prev
    S_arr[0] = S
    Seq_arr[0] = float(s_eq(r_prev))
    for m in range(steps_per_period):
        t = t0 + (m + 1) * dt
        r = drive(r0, dr, omega, np.array([t]))[0]
        A = abs(r)
        dr_sign = 1 if (r - r_prev) >= 0.0 else -1
        tau = tau_fn(A, dr_sign, tau_relax, **tau_kwargs)
        S = be_step(S, float(s_eq(r)), tau, dt)
        t_arr[m + 1] = t
        r_arr[m + 1] = r
        S_arr[m + 1] = S
        Seq_arr[m + 1] = float(s_eq(r))
        r_prev = r

    return {
        "t": t_arr,
        "r": r_arr,
        "S": S_arr,
        "Seq": Seq_arr,
        "dt": dt,
        "omega": omega,
        "omega_tau": omega_tau,
        "period": period,
        "steps_per_period": steps_per_period,
        "finite": bool(np.all(np.isfinite(S_arr))),
    }


def loop_area_rS(series: dict) -> float:
    """|∮ S dr| over the closed last-period loop (trapezoid / shoelace)."""
    S = series["S"]
    r = series["r"]
    return abs(float(np.sum(0.5 * (S[:-1] + S[1:]) * (r[1:] - r[:-1]))))


def loop_area_VI(series: dict) -> dict:
    """(V,I) pinched-hysteresis Lissajous: V=r, I=r*sqrt(S). |∮ I dV| + pinch."""
    r = series["r"]
    S = series["S"]
    volt = r
    curr = r * np.sqrt(np.maximum(S, 0.0))  # I = V/Z_eff, Z_eff = Z_0/sqrt(S), native Z_0=1
    area = abs(float(np.sum(0.5 * (curr[:-1] + curr[1:]) * (volt[1:] - volt[:-1]))))
    return {"area_VI": area, "min_absV": float(np.min(np.abs(volt))), "min_absI": float(np.min(np.abs(curr)))}


def stroke_dissipations(series: dict) -> dict:
    """D_up, D_down = ∫_{stroke}(S-Seq)dr split by sign(dr). Both >= 0.
    loop_area = D_up + D_down; rectification R = (D_up - D_down)/(D_up + D_down).
    """
    S = series["S"]
    Seq = series["Seq"]
    r = series["r"]
    g = S - Seq
    d_up = 0.0
    d_down = 0.0
    for i in range(len(r) - 1):
        dr = r[i + 1] - r[i]
        contrib = 0.5 * (g[i] + g[i + 1]) * dr
        if dr >= 0.0:
            d_up += contrib
        else:
            d_down += contrib
    total = d_up + d_down
    R = (d_up - d_down) / total if abs(total) > 0.0 else 0.0
    return {
        "D_up": float(d_up),
        "D_down": float(d_down),
        "loop_area_signed_split": float(total),
        "R": float(R),
    }


def effective_tau_by_stroke(series: dict) -> dict:
    """Estimate tau_eff on up vs down stroke via S - Seq ~ -tau * dSeq/dt.

    Robust median over points where |dSeq/dt| is not near zero. Returns
    tau_up, tau_down, and Delta_tau_rel = |tau_up - tau_down|/tau_relax(=1 native).
    """
    S = series["S"]
    Seq = series["Seq"]
    r = series["r"]
    dt = series["dt"]
    # centred dSeq/dt and lag at interior points
    dSeq_dt = (Seq[2:] - Seq[:-2]) / (2.0 * dt)
    lag = (S[1:-1] - Seq[1:-1])
    dr = r[2:] - r[:-2]
    # tau_eff = -lag / dSeq_dt  (leading-order first-order-lag relation)
    with np.errstate(divide="ignore", invalid="ignore"):
        tau_eff = -lag / dSeq_dt
    # mask: rate not tiny (avoid turning points), tau_eff finite & positive
    scale = np.max(np.abs(dSeq_dt)) if dSeq_dt.size else 1.0
    mask_valid = np.isfinite(tau_eff) & (np.abs(dSeq_dt) > 0.05 * scale) & (tau_eff > 0.0)
    up = mask_valid & (dr > 0.0)
    down = mask_valid & (dr < 0.0)
    tau_up = float(np.median(tau_eff[up])) if np.any(up) else float("nan")
    tau_down = float(np.median(tau_eff[down])) if np.any(down) else float("nan")
    return {
        "tau_up": tau_up,
        "tau_down": tau_down,
        "delta_tau_rel": float(abs(tau_up - tau_down)),  # /tau_relax=1 native
    }

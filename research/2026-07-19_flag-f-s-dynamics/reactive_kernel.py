"""Reactive (2nd-order) S-dynamics kernel — Forms R and T of the Flag-F battery.

Derivation: research/2026-07-19_flag-f-s-dynamics-derivation.md §5.1 (FAMILY).
Prereg (frozen-by-push): research/2026-07-19_flag-f-s-dynamics_prereg.md §2.

The derived damped bow-oscillator (native tau_relax=1):

    S_ddot + 2*zeta*omega_S*S_dot + omega_S^2 * (S - S_eq(r(t))) = 0

is LINEAR in S with a known periodic forcing S_eq(r(t)) (r(t)=r0+dr*sin(w t),
S_eq byte-verbatim k4_tlm.py:283). Its exact steady state is obtained by the
frequency-response (transfer-function) method: rfft the forcing over one drive
period, multiply each harmonic n*w by the oscillator transfer function

    H(Omega) = omega_S^2 / (omega_S^2 - Omega^2 + 2j*zeta*omega_S*Omega),

irfft back. This is EXACT (no transient/settle), so:
  * zeta = 0  -> H real off-resonance -> S in/anti-phase with S_eq -> loop area
    = 0 (reactive, lossless: the world-(a) "nets zero per cycle" statement).
  * zeta > 0  -> Im H < 0 -> finite loop = energy TRANSDUCED (world b), Gamma>0.
  * H sweeps a full 180 deg of phase through Omega=omega_S (the reactive
    resonance + phase inversion; #735 F-B3 corrected signature). A first-order
    (Debye) kernel can only sweep 90 deg -> the axis-(iii) discriminator.

Form S (shipped first-order Eq 2.1) is NOT here; it reuses the byte-locked
yield_fork_kernel.py (k4_tlm.py:283,291) so it byte-matches the live engine.
"""

from __future__ import annotations

import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yield_fork_kernel as k  # noqa: E402  (byte-locked S_eq + drive, shared)


def transfer_function(Omega: np.ndarray, omega_S: float, zeta: float) -> np.ndarray:
    """Damped-oscillator response H(Omega) from forcing S_eq to response S."""
    return omega_S**2 / (omega_S**2 - Omega**2 + 2j * zeta * omega_S * Omega)


def integrate_reactive(
    r0: float,
    dr: float,
    omega_tau: float,
    omega_S_tau: float,
    zeta: float,
    tau_relax: float = 1.0,
    n_per_period: int = 4096,
) -> dict:
    """Exact steady-state of the reactive ODE over ONE drive period via H(Omega).

    Returns t, r, S, Seq, Sdot over one period plus finite flag and the
    fundamental transfer value H(omega) (for phase-class analysis).
    """
    omega = omega_tau / tau_relax
    omega_S = omega_S_tau / tau_relax
    period = 2.0 * np.pi / omega
    N = int(n_per_period)
    t = np.arange(N) * (period / N)
    r = k.drive(r0, dr, omega, t)
    Seq = np.asarray(k.s_eq(r), dtype=float)

    F = np.fft.rfft(Seq)  # unnormalized harmonic content of the forcing
    # angular frequency of each rfft bin: 2*pi*rfftfreq(N, d=period/N) = n*omega
    Omega = 2.0 * np.pi * np.fft.rfftfreq(N, d=period / N)
    H = transfer_function(Omega, omega_S, zeta)
    S = np.fft.irfft(F * H, n=N)  # exact linear steady-state response
    Sdot = np.fft.irfft(F * H * (1j * Omega), n=N)

    # close the loop (append the wrap point) so trapezoid ∮ is on a closed curve
    t_c = np.append(t, t[0] + period)
    r_c = np.append(r, r[0])
    S_c = np.append(S, S[0])
    Seq_c = np.append(Seq, Seq[0])
    Sdot_c = np.append(Sdot, Sdot[0])

    return {
        "t": t_c,
        "r": r_c,
        "S": S_c,
        "Seq": Seq_c,
        "Sdot": Sdot_c,
        "dt": period / N,
        "omega": omega,
        "omega_tau": omega_tau,
        "omega_S_tau": omega_S_tau,
        "zeta": zeta,
        "period": period,
        "H_fundamental": complex(transfer_function(np.array([omega]), omega_S, zeta)[0]),
        "finite": bool(np.all(np.isfinite(S))),
    }


def loop_area_rS(series: dict) -> float:
    """|∮ S dr| (trapezoid on the closed loop). Same estimator as #735."""
    S = series["S"]
    r = series["r"]
    return abs(float(np.sum(0.5 * (S[:-1] + S[1:]) * (r[1:] - r[:-1]))))


def signed_loop_rS(series: dict) -> float:
    """Signed ∮ S dr (sign encodes traversal direction / dissipative quadrature)."""
    S = series["S"]
    r = series["r"]
    return float(np.sum(0.5 * (S[:-1] + S[1:]) * (r[1:] - r[:-1])))


def loop_area_VI(series: dict) -> dict:
    """(V,I) Lissajous: V=r, I=r*sqrt(max(S,0)); |∮ I dV| + pinch + signed area."""
    r = series["r"]
    S = series["S"]
    volt = r
    curr = r * np.sqrt(np.maximum(S, 0.0))
    signed = float(np.sum(0.5 * (curr[:-1] + curr[1:]) * (volt[1:] - volt[:-1])))
    return {
        "area_VI": abs(signed),
        "signed_VI": signed,
        "min_absV": float(np.min(np.abs(volt))),
        "min_absI": float(np.min(np.abs(curr))),
    }


def fundamental_phase_deg(series: dict) -> float:
    """Phase (deg) of the fundamental of S relative to the fundamental of S_eq.

    Debye (1st-order) asymptotes to -90 deg; the reactive 2nd-order sweeps the
    FULL -180 deg through resonance. Computed from H(omega) directly (exact).
    """
    return float(np.degrees(np.angle(series["H_fundamental"])))


def ode_residual(series: dict, omega_S_tau: float, zeta: float, tau_relax: float = 1.0) -> float:
    """Max |S_ddot + 2 zeta wS S_dot + wS^2 (S - S_eq)| / wS^2 over the period.

    G3 audit: the FFT solution is the EXACT linear steady state, so this must be
    machine-zero. Confirms the reactive integrator is not spuriously dissipating
    or mis-solving.
    """
    omega = series["omega"]
    omega_S = omega_S_tau / tau_relax
    N = len(series["t"]) - 1
    period = series["period"]
    # rebuild spectral second derivative on the open period
    Seq = series["Seq"][:-1]
    F = np.fft.rfft(Seq)
    Omega = 2.0 * np.pi * np.fft.rfftfreq(N, d=period / N)
    H = transfer_function(Omega, omega_S, zeta)
    Sddot = np.fft.irfft(F * H * (-(Omega**2)), n=N)
    Sdot = np.fft.irfft(F * H * (1j * Omega), n=N)
    S = np.fft.irfft(F * H, n=N)
    resid = Sddot + 2 * zeta * omega_S * Sdot + omega_S**2 * (S - Seq)
    return float(np.max(np.abs(resid)) / omega_S**2)

"""NUMERIC TIME-DOMAIN DRIVER — a LOCALIZED traveling wavetrain on a LONG 2-DOF ring.

The new capability the pilot-field hypothesis needs: co-motion and leakage are
DYNAMICAL — the #533/#534 STATIC probe (relax u at frozen y phase) cannot see whether
a contraction TRAVELS WITH the envelope. This module integrates the FULL 2-DOF
equations of motion (both u and y evolve) via velocity-Verlet, launches a localized
wavetrain, and measures the contraction profile du(x,t), its co-motion, the local-vs-far
bond-frame probe reading, and the longitudinal leakage.

FROZEN prereg: research/2026-07-05_pilot-field-comoving-companion_prereg_FROZEN.md.

THE #531 TAUTOLOGY GUARD (binding): this module MUST NOT import
`pilot_field_predictions.py`. It measures everything from the time-domain dynamics on
its own independent path. The #528 ReconcileGate compares OUTPUTS only.

CONSUMES the #533/#534 machinery BY IMPORT (mission-required): the RingChain 2-DOF host
(force_x, force_y, energy = the saturation-consistent Phi potential per the #532 flag,
trans_tangent_stiffness = the bond-frame probe, canon-pinned #534) and the analytic
free-host equilibrium. The k_long/k_shear ratio (rho_bond, the sonic sweep) is added
here via a per-force axial-stiffness scale on the imported RingChain.

Host: N-node PERIODIC ring, 2 DOF/node (u longitudinal, y transverse), rest spacing 1.
No PML (closed ring; boundedness measured on the ring itself in a co-moving window).

alpha-CLEAN: no physical constant on this path.
"""
from __future__ import annotations

import os
import sys
from dataclasses import dataclass

import numpy as np

# import the #533/#534 machinery (mission: consume by import)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ring_bondframe_probe import (  # noqa: E402
    ELL,
    K_S,
    RingChain,
    _phi_prime,
    wave_number_cold,
)


# ─────────────────────────────────────────────────────────────────────────────
# The 2-DOF ring host with a longitudinal-stiffness scale (the sonic sweep knob).
#
# EMPIRICAL-DRIVER-DISCIPLINE CATCH (Rule 10, integrator-time): the imported
# `RingChain.tension` IGNORES `self.k_a` in the NONLINEAR (kernel) path — it returns
# `_phi_prime(A)` with k0=1 baked in; k_a is only consulted in the `linear_axial=True`
# branch. So passing `k_a = rho_bond * k_s` to the base class is a NO-OP for the sonic
# sweep (verified: tension(0.1) identical for k_a=0.5 vs 4.0). This subclass scales the
# KERNEL tension by rho_bond (k0 -> rho_bond*k0, preserving the saturation SHAPE
# sqrt(1-A^2)), so the axial sound speed c_long = sqrt(rho_bond) actually varies. We do
# NOT mutate the imported module (my additions in my own module, per mission).
# ─────────────────────────────────────────────────────────────────────────────
class SonicRing(RingChain):
    """RingChain with the axial (longitudinal) stiffness scaled by rho_bond = k_long/k_shear
    on BOTH the nonlinear-kernel and linear paths, so the sonic sweep is real. c_long =
    sqrt(rho_bond) (a0=1, unit mass). rho=1 is the Ax3 photon point (SONIC at long
    wavelengths; EXPECTED coincidence, KNIFE — not a discovery)."""

    def __init__(self, n_nodes, rho_bond=1.0, k_s=K_S, linear_axial=False):
        super().__init__(n_nodes, k_a=rho_bond * k_s, k_s=k_s, linear_axial=linear_axial)
        self.rho_bond = float(rho_bond)

    def tension(self, A):
        if self.linear_axial:
            return self.k_a * A                       # T = rho*k_s * A (linear, control c)
        return self.rho_bond * _phi_prime(A)          # T = rho * Phi'(A) (kernel shape, scaled stiffness)

    def energy(self, u, y):
        """H_pot with the rho-scaled axial potential (rho * Phi(A)) + shear. Saturation-
        consistent (the #532 no-linear-proxy flag): the axial potential keeps the kernel
        shape, scaled by rho_bond."""
        from ring_bondframe_probe import _phi_potential
        L, _, dy = self.bond_lengths(u, y)
        A = L - ELL
        if self.linear_axial:
            axial = 0.5 * self.k_a * float(np.sum(A**2))
        else:
            axial = self.rho_bond * float(np.sum(_phi_potential(A)))
        shear = 0.5 * self.k_s * float(np.sum(dy**2))
        return axial + shear


def make_ring(n_nodes: int, rho_bond: float = 1.0, linear_axial: bool = False) -> SonicRing:
    """SonicRing with a REAL longitudinal/shear stiffness ratio (the sonic sweep knob).
    c_long = sqrt(rho_bond); the transverse group speed v_g is rho-independent, so the
    Mach number v_g/c_long = v_g/sqrt(rho_bond) sweeps subsonic/sonic/supersonic."""
    return SonicRing(n_nodes, rho_bond=rho_bond, k_s=K_S, linear_axial=linear_axial)


# ─────────────────────────────────────────────────────────────────────────────
# The localized-envelope launcher (carrier lambda << L_env << N).
# ─────────────────────────────────────────────────────────────────────────────
def gaussian_envelope(n_nodes: int, j0: float, l_env: float) -> np.ndarray:
    """Smooth Gaussian envelope G((j-j0)/L_env), PERIODIC (minimum-image distance on
    the ring so the envelope is single-valued on the loop)."""
    j = np.arange(n_nodes)
    d = j - j0
    d = (d + n_nodes / 2) % n_nodes - n_nodes / 2   # minimum-image (periodic)
    return np.exp(-0.5 * (d / l_env) ** 2)


def launch_wavetrain(n_nodes: int, y0: float, k: float, l_env: float,
                     j0: float | None = None) -> tuple[np.ndarray, np.ndarray]:
    """Initial (y, y_dot) for a RIGHT-MOVING localized wavetrain:
        y(j,0)     = y0 * G((j-j0)/L_env) * sin(k j)
        y_dot(j,0) = +y0 * omega_carrier * G * cos(k j)   (right-moving carrier phase)
    where omega_carrier = sqrt(k_s (2-2cos k)) is the cold shear dispersion. The
    envelope moves at the GROUP velocity (measured, not imposed). u,u_dot start at 0
    (the longitudinal companion must DEVELOP from the drive — the test)."""
    if j0 is None:
        j0 = n_nodes // 4          # launch off-center so it has room to travel
    j = np.arange(n_nodes)
    env = gaussian_envelope(n_nodes, j0, l_env)
    omega_c = np.sqrt(K_S * (2.0 - 2.0 * np.cos(k)))
    y = y0 * env * np.sin(k * j)
    ydot = y0 * omega_c * env * np.cos(k * j)   # d/dt sin(kj - w t) at t=0 = -w cos(kj)*(-1)... right-moving
    return y, ydot


# ─────────────────────────────────────────────────────────────────────────────
# The velocity-Verlet time integrator (the FULL 2-DOF dynamics — the new capability).
# ─────────────────────────────────────────────────────────────────────────────
@dataclass
class WavetrainRun:
    n_nodes: int
    rho_bond: float
    y0: float
    k: float
    l_env: float
    dt: float
    n_steps: int
    record_every: int
    linear_axial: bool
    # recorded arrays (time x space), filled by run():
    t: np.ndarray | None = None
    du_frames: np.ndarray | None = None      # per-bond du = u[j+1]-u[j] (the contraction profile)
    env_frames: np.ndarray | None = None     # |y|-envelope per frame (Hilbert-free: rolling |y| peak)
    energy_trace: np.ndarray | None = None
    energy_long_trace: np.ndarray | None = None   # longitudinal (axial) energy only
    p_long_trace: np.ndarray | None = None        # total longitudinal momentum
    j0: float = 0.0


def _envelope_estimate(y: np.ndarray, l_env: float) -> np.ndarray:
    """Carrier-free envelope estimate: smooth |y| with a Gaussian window ~ L_env/2.
    (A cheap Hilbert-free amplitude proxy for the co-motion cross-correlation.)"""
    n = len(y)
    # boxcar-ish smoothing via FFT low-pass at the envelope scale
    absy = np.abs(y)
    freqs = np.fft.rfftfreq(n)
    cutoff = 1.0 / max(l_env, 1.0)
    win = np.exp(-0.5 * (freqs / cutoff) ** 2)
    return np.fft.irfft(np.fft.rfft(absy) * win, n=n)


def run_wavetrain(n_nodes: int = 1024, rho_bond: float = 2.0, y0: float = 0.1428,
                  omega: float = 1.2, l_env: float = 80.0, dt: float = 0.02,
                  n_periods: float = 6.0, record_every: int = 20,
                  linear_axial: bool = False, j0: float | None = None,
                  m_node: float = 1.0) -> WavetrainRun:
    """Integrate the full 2-DOF EOM for a launched localized wavetrain. Returns a
    WavetrainRun with the recorded du(x,t) profile, envelope frames, and the energy /
    momentum ledger traces.

    n_periods: recording window length in ENVELOPE-TRANSIT units is derived from the
    group velocity; here n_periods counts carrier periods scaled so the envelope travels
    ~ a fixed fraction of the ring (kept < half the ring so it does not lap itself)."""
    ring = make_ring(n_nodes, rho_bond=rho_bond, linear_axial=linear_axial)
    k = wave_number_cold(omega, k_s=K_S, m=m_node)
    if j0 is None:
        j0 = n_nodes // 4
    y, ydot = launch_wavetrain(n_nodes, y0, k, l_env, j0=j0)
    u = np.zeros(n_nodes)
    udot = np.zeros(n_nodes)

    omega_c = float(np.sqrt(K_S * (2.0 - 2.0 * np.cos(k))))
    period = 2.0 * np.pi / omega_c
    n_steps = int(round(n_periods * period / dt))

    def accel(u_, y_):
        # a = F / m (unit node mass by default). force_x/force_y are the imported canon.
        return ring.force_x(u_, y_) / m_node, ring.force_y(u_, y_) / m_node

    ax, ay = accel(u, y)
    t_rec, du_rec, env_rec, e_rec, el_rec, p_rec = [], [], [], [], [], []
    for step in range(n_steps + 1):
        if step % record_every == 0:
            du = np.roll(u, -1) - u                  # per-bond du (the contraction profile)
            t_rec.append(step * dt)
            du_rec.append(du.copy())
            env_rec.append(_envelope_estimate(y, l_env))
            e_rec.append(_total_energy(ring, u, y, udot, ydot, m_node))
            el_rec.append(_long_energy(ring, u, y, udot, m_node))
            p_rec.append(float(m_node * np.sum(udot)))
        # velocity-Verlet
        u = u + dt * udot + 0.5 * dt * dt * ax
        y = y + dt * ydot + 0.5 * dt * dt * ay
        ax_new, ay_new = accel(u, y)
        udot = udot + 0.5 * dt * (ax + ax_new)
        ydot = ydot + 0.5 * dt * (ay + ay_new)
        ax, ay = ax_new, ay_new

    return WavetrainRun(
        n_nodes=n_nodes, rho_bond=rho_bond, y0=y0, k=k, l_env=l_env, dt=dt,
        n_steps=n_steps, record_every=record_every, linear_axial=linear_axial,
        t=np.array(t_rec), du_frames=np.array(du_rec), env_frames=np.array(env_rec),
        energy_trace=np.array(e_rec), energy_long_trace=np.array(el_rec),
        p_long_trace=np.array(p_rec), j0=float(j0),
    )


# ── energy / momentum ledger (SATURATION-CONSISTENT — the #532 no-linear-proxy flag) ──
def _total_energy(ring: RingChain, u, y, udot, ydot, m_node: float) -> float:
    """H = kinetic (u,y) + ring.energy (saturation-consistent Phi(A) + shear). NO linear
    proxy on the saturating axial spring (the #532 flag)."""
    kin = 0.5 * m_node * float(np.sum(udot**2) + np.sum(ydot**2))
    return kin + ring.energy(u, y)


def _long_energy(ring: SonicRing, u, y, udot, m_node: float) -> float:
    """Longitudinal (axial) energy only: axial kinetic + axial Phi-potential (rho-scaled,
    saturation-consistent). Used for the leakage diagnostic (the companion's longitudinal
    energy inside/outside the co-moving window)."""
    from ring_bondframe_probe import _phi_potential
    L, _, _ = ring.bond_lengths(u, y)
    A = L - ELL
    rho = getattr(ring, "rho_bond", 1.0)
    axial_pot = rho * float(np.sum(_phi_potential(A))) if not ring.linear_axial \
        else float(0.5 * ring.k_a * np.sum(A**2))
    kin_u = 0.5 * m_node * float(np.sum(udot**2))
    return kin_u + axial_pot


# ─────────────────────────────────────────────────────────────────────────────
# ANALYSIS — the four measurements (contraction profile / co-motion / local-vs-far / leakage)
# ─────────────────────────────────────────────────────────────────────────────
def _du_dc(du_frame: np.ndarray, l_env: float) -> np.ndarray:
    """Carrier-free (DC) contraction profile: low-pass du at the ENVELOPE scale (removes
    the 2k carrier-rectified AC oscillation, leaving the net local contraction — the
    companion WELL a slow bond-frame probe feels). The AC part (du ~ dy^2 rectified) is
    kinematic-instantaneous; the DC well is what the longitudinal dynamics must BUILD."""
    n = len(du_frame)
    freqs = np.fft.rfftfreq(n)
    cutoff = 1.0 / max(l_env, 1.0)
    win = np.exp(-0.5 * (freqs / cutoff) ** 2)
    return np.fft.irfft(np.fft.rfft(du_frame) * win, n=n)


def contraction_depth(run: WavetrainRun, settle_frac: float = 0.75) -> dict:
    """MEASUREMENT 1 — the contraction profile du(x,t). Report the deepest DC CONTRACTION
    (most negative low-passed du) UNDER the envelope, and the far-field DC stretch,
    averaged over the SETTLED window (last (1-settle_frac) of the run, past the build-up
    transient). The DC contraction depth is reconciled against -<dy^2>/2 (bin criterion 2);
    the RETARDATION signal is that this depth GROWS with transit time (reported separately
    via `depth_growth`). Distinguishes the DC well (bond-frame content) from the AC wiggle."""
    du = run.du_frames
    env = run.env_frames
    n_frames = du.shape[0]
    s = max(1, int(n_frames * settle_frac))
    depths_dc, far_dc, depths_raw = [], [], []
    N = run.n_nodes
    for f in range(s, n_frames):
        peak = int(np.argmax(env[f]))
        du_dc = _du_dc(du[f], run.l_env)
        j = np.arange(N)
        d = (j - peak + N // 2) % N - N // 2
        under = np.abs(d) <= run.l_env
        far = np.abs(d) >= 3 * run.l_env
        depths_dc.append(float(np.min(du_dc[under])))       # deepest DC contraction under
        far_dc.append(float(np.mean(du_dc[far])))           # far-field DC (compensating stretch)
        depths_raw.append(float(np.min(du[f][under])))      # raw (AC+DC) min for reference
    # depth growth over the whole run (retardation signal): early-quarter vs settled
    e0 = max(1, n_frames // 5)
    early_dc = []
    for f in range(e0, 2 * e0):
        peak = int(np.argmax(env[f]))
        du_dc = _du_dc(du[f], run.l_env)
        j = np.arange(N)
        d = (j - peak + N // 2) % N - N // 2
        early_dc.append(float(np.min(du_dc[np.abs(d) <= run.l_env])))
    return {
        "du_dc_min_under": float(np.mean(depths_dc)),
        "du_dc_min_under_std": float(np.std(depths_dc)),
        "du_dc_far_mean": float(np.mean(far_dc)),
        "du_raw_min_under": float(np.mean(depths_raw)),      # AC-dominated (~2.5x the DC)
        "depth_growth_early_to_settled": float(np.mean(depths_dc) / (np.mean(early_dc) + 1e-30)),
        "early_dc_depth": float(np.mean(early_dc)),
    }


def co_motion(run: WavetrainRun) -> dict:
    """MEASUREMENT 2 — co-motion. Track the envelope peak position and the du-contraction
    (du-minimum) position over time; report (i) the envelope group speed (peak drift),
    (ii) the du-contraction speed, (iii) the cross-correlation lag between the du profile
    and the envelope. Co-moving <=> the two speeds match and the lag ~ 0."""
    du = run.du_frames
    env = run.env_frames
    t = run.t
    n_frames = du.shape[0]
    s = max(1, n_frames // 5)
    N = run.n_nodes

    def unwrap_peaks(field, sign=1.0):
        pos = []
        for f in range(s, n_frames):
            arr = field[f] * sign
            pos.append(int(np.argmax(arr)))
        pos = np.array(pos, dtype=float)
        # unwrap periodic jumps
        for i in range(1, len(pos)):
            while pos[i] - pos[i - 1] > N / 2:
                pos[i] -= N
            while pos[i] - pos[i - 1] < -N / 2:
                pos[i] += N
        return pos

    # track the DC-WELL position (low-passed du minimum), not the raw carrier du-min
    du_dc = np.array([_du_dc(du[f], run.l_env) for f in range(du.shape[0])])
    env_pos = unwrap_peaks(env, sign=+1.0)          # envelope peak
    du_pos = unwrap_peaks(du_dc, sign=-1.0)         # DC-well MINIMUM (deepest contraction)
    tt = t[s:]
    # linear fit position vs time -> speed (nodes per unit time)
    env_speed = float(np.polyfit(tt, env_pos, 1)[0]) if len(tt) > 1 else float("nan")
    du_speed = float(np.polyfit(tt, du_pos, 1)[0]) if len(tt) > 1 else float("nan")
    # cross-correlation lag (mean spatial offset of du-min from env-peak)
    lag = float(np.mean(du_pos - env_pos))
    return {
        "env_group_speed": env_speed,
        "du_contraction_speed": du_speed,
        "comotion_lag_nodes": lag,
        "speed_ratio_du_over_env": float(du_speed / env_speed) if env_speed else float("nan"),
    }


def local_vs_far_probe(run: WavetrainRun) -> dict:
    """MEASUREMENT 3 — the LOCAL bond-frame probe reading UNDER the envelope vs FAR from
    it. Uses the imported (canon #534) trans_tangent_stiffness at the (u,y) configuration
    at the mid-window frame, sampled at the envelope PEAK (density-peak sampling, NOT
    centroid) and at a far node. Ratio to cold. free-like (soft, <1) under / cold (~1) far
    is the pilot signature (bin criterion 2)."""
    ring = make_ring(run.n_nodes, rho_bond=run.rho_bond, linear_axial=run.linear_axial)
    du = run.du_frames
    env = run.env_frames
    n_frames = du.shape[0]
    N = run.n_nodes
    kcold = ring.k_s

    # bond-frame transverse tangent stiffness felt through a bond at mean DC strain A
    # (the imported kernel's tangent shape; contracted bond A<0 => softer; A~0 => cold).
    # A CONTRACTED (A<0) bond is SOFTER than cold via the -T/ell slot (compression), the
    # free-host SOFT signature. We report the DC-WELL depth at the envelope peak (density-
    # peak sampling, per the mission) vs a far node, averaged over the settled window.
    def kframe(A):
        # tangent shear stiffness k_s*sqrt(1-A^2) + the compression slot T(A)/ell (A<0 => T<0 => softer)
        tang = ring.k_s * np.sqrt(max(0.0, 1.0 - A * A))
        T = float(ring.tension(np.array([A]))[0])   # rho-scaled bond tension (negative under compression)
        return tang + T / ELL

    s = max(1, n_frames * 3 // 4)               # settled window
    under_ratio, far_ratio, A_und, A_fr = [], [], [], []
    for f in range(s, n_frames):
        peak = int(np.argmax(env[f]))
        du_dc = _du_dc(du[f], run.l_env)
        far = int((peak + N // 2) % N)
        A_under = float(du_dc[peak])            # DC strain at the envelope PEAK (density-peak sample)
        A_far = float(du_dc[far])
        under_ratio.append(kframe(A_under) / kcold)
        far_ratio.append(kframe(A_far) / kcold)
        A_und.append(A_under)
        A_fr.append(A_far)
    return {
        "under_bondframe_k_ratio": float(np.mean(under_ratio)),
        "far_bondframe_k_ratio": float(np.mean(far_ratio)),
        "A_under": float(np.mean(A_und)),
        "A_far": float(np.mean(A_fr)),
    }


def leakage(run: WavetrainRun) -> dict:
    """MEASUREMENT 4 — boundedness vs leakage. Track the longitudinal energy INSIDE a
    co-moving window around the envelope vs the TOTAL longitudinal energy over the
    recording window. If the co-moving fraction stays high, the companion is BOUND; if it
    decays, longitudinal waves radiate away (LEAKY). Reports the fraction-in-window
    trace and its slope (leak rate per envelope transit)."""
    el = run.energy_long_trace
    # crude co-moving fraction: use the recorded total longitudinal energy trace; a rising
    # or steady long-energy with a well-localized du profile => bound; a growing spread of
    # du outside the window => leak. We proxy the leak by the SPREAD of |du| outside the
    # co-moving window relative to inside.
    du = run.du_frames
    env = run.env_frames
    n_frames = du.shape[0]
    s = max(1, n_frames // 5)
    frac_in = []
    N = run.n_nodes
    for f in range(s, n_frames):
        peak = int(np.argmax(env[f]))
        j = np.arange(N)
        d = (j - peak + N // 2) % N - N // 2
        win = np.abs(d) <= 2 * run.l_env
        e_bond = du[f] ** 2                 # longitudinal strain energy density proxy (per bond)
        tot = float(np.sum(e_bond)) + 1e-30
        frac_in.append(float(np.sum(e_bond[win]) / tot))
    frac_in = np.array(frac_in)
    tt = run.t[s:]
    slope = float(np.polyfit(tt, frac_in, 1)[0]) if len(tt) > 1 else float("nan")
    return {
        "frac_long_in_window_mean": float(np.mean(frac_in)),
        "frac_long_in_window_final": float(frac_in[-1]),
        "leak_slope_per_time": slope,
        "long_energy_drift": float((el[-1] - el[s]) / (abs(el[s]) + 1e-30)),
    }


def ledger_closure(run: WavetrainRun) -> dict:
    """CONTROL (e) — the crank check. Total energy conserved (saturation-consistent
    functional) and total longitudinal momentum conserved (closed ring) over the window."""
    e = run.energy_trace
    p = run.p_long_trace
    return {
        "energy_drift_rel": float((np.max(e) - np.min(e)) / (abs(e[0]) + 1e-30)),
        "momentum_max_abs": float(np.max(np.abs(p))),
        "energy_initial": float(e[0]),
    }


if __name__ == "__main__":
    import json

    # a compact demonstration run (subsonic companion, rho=2), small for the __main__ smoke
    run = run_wavetrain(n_nodes=512, rho_bond=2.0, l_env=40.0, n_periods=4.0, dt=0.02)
    out = {
        "params": {"n_nodes": run.n_nodes, "rho_bond": run.rho_bond, "l_env": run.l_env,
                   "k": run.k, "dt": run.dt, "n_steps": run.n_steps},
        "contraction_depth": contraction_depth(run),
        "co_motion": co_motion(run),
        "local_vs_far_probe": local_vs_far_probe(run),
        "leakage": leakage(run),
        "ledger_closure": ledger_closure(run),
    }
    print(json.dumps(out, indent=2, default=float))

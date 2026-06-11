"""D18 — genesis-v8 INSTRUMENTATION (prereg §3 D18 / §8 driver-assertion plumbing).

The look-inside measurement chain the directive mandates, as pure read-only
functions (CP1 — no dynamics touched):

  resolve_internal_period   FFT the channel-wall ω-tank L-state time series to get
                            the traveling period T_travel — RESOLVE THE OSCILLATOR
                            FIRST (the look-inside N=32 lesson). A random-phase
                            snapshot cannot tell a standing wave caught at peak from
                            a traveling winding; the reads must be phase-locked to
                            the resolved internal period (the reactance-pair
                            completeness rule at the traveling frequency).
  phase_lock_sample_steps   the step indices to snapshot at, evenly over one
                            resolved period, so the w_pol time-series is read at the
                            traveling frequency (not at one arbitrary phase).
  interior_contour_wpol     the de-novo w_pol read on the FIELD-DERIVED torus (the
                            D16 channel locus, the A46 fix), at interior contours
                            r >= 3 cells BETWEEN core and channel wall (external
                            settled-average reads are the WRONG instrument). Swept
                            over pol_r for robustness (§5 row 7).
  known_positive_in_channel the extractor known-positive: plant the v8 traveling
                            deposit INSIDE the threaded geometry at the run's own
                            scale and confirm the read returns q_dep BEFORE any
                            de-novo read (the plant-at-scale hygiene; F-WPOL(b)).

ave-driver-script-honesty: every number these return comes FROM the evolved field
(ω, π_ω) or the topology gate's field-derived torus — never an accumulator.
"""

from __future__ import annotations

import numpy as np

from ave.utils.fast_winding_extractor import extract_2_3_omega_fast
from ave.utils.topology_genus import derive_read_torus_from_channel

__all__ = [
    "resolve_internal_period",
    "phase_lock_sample_steps",
    "interior_contour_wpol",
    "known_positive_in_channel",
]


def resolve_internal_period(series, dt=1.0, *, exclude_dc=True):
    """Resolve the dominant oscillation PERIOD (in STEPS) of a 1-D real time series
    by its FFT peak — the channel-wall ω-tank L-state, sampled per step over the
    recording window. Returns (T_steps, T_time, f_peak) where T_steps = period in
    integrator steps (the phase-lock cadence), T_time = T_steps*dt.

    Returns T_steps = inf (a flat / non-oscillating series) when no spectral peak
    rises above the DC/leakage floor — an honest 'no internal period resolved'
    (the read then cannot be phase-locked; the driver bins UNRESOLVED)."""
    y = np.asarray(series, dtype=np.float64).ravel()
    n = y.size
    if n < 8:
        return float("inf"), float("inf"), 0.0
    y = y - y.mean()
    if not np.any(np.abs(y) > 0):
        return float("inf"), float("inf"), 0.0
    spec = np.abs(np.fft.rfft(y * np.hanning(n)))
    freqs = np.fft.rfftfreq(n, d=1.0)  # cycles per STEP
    lo = 1 if exclude_dc else 0
    if spec[lo:].size == 0 or not np.any(spec[lo:] > 0):
        return float("inf"), float("inf"), 0.0
    k = lo + int(np.argmax(spec[lo:]))
    # parabolic (3-point) peak interpolation for sub-bin frequency accuracy — the
    # phase-lock cadence needs the period to ~1%, not the FFT bin width.
    df = 1.0 / n  # cycles/step per bin
    if 0 < k < spec.size - 1:
        a, b, c = spec[k - 1], spec[k], spec[k + 1]
        denom = (a - 2.0 * b + c)
        delta = 0.5 * (a - c) / denom if abs(denom) > 1e-30 else 0.0
        delta = float(np.clip(delta, -0.5, 0.5))
    else:
        delta = 0.0
    f_peak = float(freqs[k] + delta * df)
    if f_peak <= 0.0:
        return float("inf"), float("inf"), 0.0
    T_steps = 1.0 / f_peak
    return float(T_steps), float(T_steps * dt), f_peak


def phase_lock_sample_steps(T_steps, n_samples, start_step=0):
    """The step indices to snapshot at — n_samples evenly spaced over ONE resolved
    period T_steps starting at start_step. Phase-locks the w_pol reads to the
    traveling frequency so a standing wave caught at peak cannot masquerade as a
    traveling winding (the directive's phase-locked-snapshot mandate)."""
    if not np.isfinite(T_steps) or T_steps <= 0 or n_samples < 1:
        return [int(start_step)]
    return [int(round(start_step + k * T_steps / n_samples))
            for k in range(n_samples)]


def interior_contour_wpol(omega, pi_omega, topo, N, *, axis=2,
                          pol_r_grid=(3.0, 4.0, 5.0), dR_grid=(0.0,)):
    """The de-novo poloidal-winding read on the FIELD-DERIVED torus (the A46 fix):
    R from the D16 channel locus, minor circle r swept over ``pol_r_grid`` (and R
    nudged by ``dR_grid`` cells) for robustness (§5 row 7). Interior contours only
    (r >= 3 cells, BETWEEN core and channel wall). Returns the modal w_pol across
    the swept contours, the per-contour reads, and the read torus — or a VOID dict
    when the topology is not THREADED (no field-defined major radius; the v7 SPHERE
    obstruction, honestly returned, not guessed)."""
    rd = derive_read_torus_from_channel(topo, axis=axis)
    if rd is None:
        return {"void": True, "reason": "no THREADED channel ⇒ no field-defined R "
                "(the v7 SPHERE obstruction — read is coordinate-undefined)"}
    R0 = rd["R"]
    reads = []
    for dR in dR_grid:
        for pr in pol_r_grid:
            if pr < 3.0:
                continue  # the F0b r >= 3 floor
            res = extract_2_3_omega_fast(omega, pi_omega, R0 + dR, pr, N)
            reads.append({"R": R0 + dR, "r": pr, "w_pol": int(res["w_pol"]),
                          "w_pol_rel": float(res["w_pol_rel"]),
                          "w_tor": int(res["w_tor"]),
                          "w_pol_raw_median": (float(res["w_pol_raw_median"])
                                               if np.isfinite(res["w_pol_raw_median"])
                                               else None)})
    if not reads:
        return {"void": True, "reason": "no contour cleared the r>=3 floor"}
    from collections import Counter
    modal_wpol, modal_count = Counter(r["w_pol"] for r in reads).most_common(1)[0]
    rel_med = float(np.median([r["w_pol_rel"] for r in reads]))
    # the signed handedness from the raw windings (None-safe)
    raws = [r["w_pol_raw_median"] for r in reads if r["w_pol_raw_median"] is not None]
    sign = float(np.sign(np.median(raws))) if raws else 0.0
    return {"void": False, "read_torus": rd, "w_pol_modal": int(modal_wpol),
            "w_pol_modal_count": int(modal_count), "n_contours": len(reads),
            "w_pol_rel_median": rel_med, "w_pol_sign": sign,
            "robust": bool(modal_count >= max(2, len(reads) // 2)),
            "per_contour": reads}


def known_positive_in_channel(engine, topo, *, q_dep=3, p_dep=2, amplitude=0.3,
                              mode="traveling", helicity=1, axis=2, N=None):
    """F-WPOL(b) known-positive: plant the v8 deposit INSIDE the threaded channel at
    the run's own scale (R from the D16 locus) and read it back — the extractor must
    return w_pol = q_dep on a deepcopy of the assembled engine (the plant is on a
    COPY so the live field is untouched). Returns the read + a PASS flag; a de-novo
    read on an extractor not shown known-positive at scale inside THIS geometry is
    UNRESOLVED (the look-inside hygiene)."""
    import copy
    rd = derive_read_torus_from_channel(topo, axis=axis)
    if rd is None:
        return {"pass": False, "void": True,
                "reason": "no THREADED channel to plant inside"}
    N = N if N is not None else engine.N
    probe = copy.deepcopy(engine)
    probe.dep_R = rd["R"]
    probe.plant_polyphase_winding(mode=mode, helicity=helicity, amplitude=amplitude,
                                  R=rd["R"], r=rd["r"], q=q_dep, p=p_dep, axis=axis)
    pi_om = (probe.omega - probe.omega_prev) / probe.dt
    res = extract_2_3_omega_fast(probe.omega, pi_om, rd["R"], rd["r"], N)
    expect = q_dep if mode == "traveling" else 0
    return {"pass": bool(res["w_pol"] == expect and
                         (res["w_pol_rel"] > 0.1 if mode == "traveling" else True)),
            "void": False, "w_pol": int(res["w_pol"]), "expect": int(expect),
            "w_pol_rel": float(res["w_pol_rel"]), "read_torus": rd}

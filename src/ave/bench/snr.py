"""snr.py — shot-noise-limited SNR surface + time-to-Nsigma + signal-vs-floor.

FACTORED FROM: AVE-Bench-VacuumMirror/scripts/apd_snr_sweep.py
  - snr_direct(V_gap, N_total, t_int)  (apd_snr_sweep.py:82-86)
  - t_detection(V_gap, N_total, sigma) (apd_snr_sweep.py:89-95)
  - signal_rate / dark / confound table (apd_snr_sweep.py:77-95, :180-199)
AND: AVE-Core src/scripts/peer_review/experimental_noise_floor.py
  (the breakdown-envelope floors: dark count, thermal kT/C, shot-noise).

Produces a reusable SNR / time-to-Nsigma over (signal, noise-floor,
integration-time). The shot-noise-limited photon-counting contract
(apd_snr_sweep.py:14-18):

    SNR(t_int) = signal * t_int / sqrt((signal + floor) * t_int)
               ~ sqrt(signal * t_int)   for signal >> floor

and the inverted time-to-Nsigma (apd_snr_sweep.py:94):

    SNR = sqrt(s^2 t / (s + floor)) >= sigma  =>  t >= sigma^2 (s + floor) / s^2

DISCIPLINE: this module is dimensionless-rate machinery — no physical constants
are imported (the signal rate and noise floor are supplied by the caller, who
derives them from ave.core.constants via apparatus.py / a Born engine). It is
the SNR/timing contract factored out, nothing more.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class SNRPoint:
    """A single point on the SNR surface.

    Attributes
    ----------
    signal : float
        Detected signal rate [Hz].
    floor : float
        Additive noise floor rate [Hz] (dark count + background, the additive
        shot-noise contributor).
    t_int : float
        Integration time [s].
    snr : float
        Shot-noise-limited SNR at (signal, floor, t_int).
    """

    signal: float
    floor: float
    t_int: float
    snr: float


def snr_shot_noise(signal: float, floor: float, t_int: float) -> float:
    """Shot-noise-limited SNR (FACTORED FROM apd_snr_sweep.py snr_direct, :82-86).

        SNR = signal * t_int / sqrt((signal + floor) * t_int)

    Parameters
    ----------
    signal : float
        Detected signal rate [Hz].
    floor : float
        Additive noise floor rate [Hz] (e.g. APD dark count, 100 Hz in the
        exemplar; apd_snr_sweep.py:44).
    t_int : float
        Integration time [s].

    Returns
    -------
    float
        SNR. Returns 0.0 if the total counted rate is non-positive (matches the
        exemplar's `if n > 0` guard, apd_snr_sweep.py:86).
    """
    total = (signal + floor) * t_int
    if total <= 0:
        return 0.0
    return float(signal * t_int / np.sqrt(total))


def time_to_n_sigma(signal: float, floor: float, sigma_target: float = 5.0) -> float:
    """Integration time to reach sigma_target detection.

    FACTORED FROM apd_snr_sweep.py t_detection (:89-95):
        SNR = sqrt(s^2 t / (s + floor)) >= sigma  =>  t >= sigma^2 (s+floor)/s^2

    Parameters
    ----------
    signal : float
        Detected signal rate [Hz].
    floor : float
        Additive noise floor rate [Hz].
    sigma_target : float, optional
        Target detection significance (default 5.0 = 5-sigma, the exemplar
        default).

    Returns
    -------
    float
        Required integration time [s]; np.inf if signal <= 0 (no detection
        possible), matching the exemplar (apd_snr_sweep.py:92-93).
    """
    if signal <= 0:
        return float(np.inf)
    return float(sigma_target**2 * (signal + floor) / signal**2)


def signal_vs_floor(signal: float, floor: float) -> float:
    """Signal-to-floor ratio (the static detectability margin).

    The single-number "is the signal above the floor at all" margin, distinct
    from the integration-time-dependent SNR. Mirrors the confound-margin
    comparison in apd_snr_sweep.py Panel D (:180-199) where signal is compared
    against dark / SM / scatter floors. Returns np.inf if floor <= 0.
    """
    if floor <= 0:
        return float(np.inf)
    return float(signal / floor)


def snr_surface(
    signals: np.ndarray,
    floor: float,
    t_grid: np.ndarray,
) -> np.ndarray:
    """Parametric SNR surface over (signal, integration-time).

    Vectorized sweep producing SNR[i, j] = snr_shot_noise(signals[i], floor,
    t_grid[j]). Mirrors the apd_snr_sweep.py V-vs-t sweep block (:110-128, the
    snr_direct over V_array x t_array) generalized to arbitrary signal rates.

    Parameters
    ----------
    signals : np.ndarray
        1-D array of detected signal rates [Hz].
    floor : float
        Additive noise floor rate [Hz].
    t_grid : np.ndarray
        1-D array of integration times [s].

    Returns
    -------
    np.ndarray
        2-D SNR surface of shape (len(signals), len(t_grid)).
    """
    s = np.asarray(signals, dtype=float)
    t = np.asarray(t_grid, dtype=float)
    surface = np.empty((s.size, t.size), dtype=float)
    for i, si in enumerate(s):
        for j, tj in enumerate(t):
            surface[i, j] = snr_shot_noise(float(si), floor, float(tj))
    return surface

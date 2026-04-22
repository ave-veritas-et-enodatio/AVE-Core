from __future__ import annotations

r"""
Scale-Invariant Resonator Analysis
====================================

Tools for finding resonant modes of impedance cavities.  Every function
is domain-agnostic — the SAME code analyses:

  ==========================  ==================  ==================
  Domain                      Cavity              Mode
  ==========================  ==================  ==================
  Black hole photon sphere    Graded n(r) shell   ℓ=2 QNM
  Electron orbital            Coulomb potential    n,ℓ bound state
  Protein backbone            Peptide chain TL    Amide-V resonance
  PONDER-01 antenna           Meander stub line   λ/4 resonance
  ==========================  ==================  ==================

Key functions:
  graded_tl_eigenvalue    — S₁₁ frequency sweep → resonant f₀, Q
  cavity_q_from_spectrum  — Q extraction from |S₁₁|² peak
  impulse_response        — IFFT of S₂₁ → time-domain ringdown

Performance:
  NumPy backend — pre-computes all shell parameters, vectorises across
  frequency where possible, sequential 2×2 cascade only where required.
  JAX backend available via ``ave.solvers.transmission_line.abcd_cascade_jax``.
"""

from typing import Callable, List, Optional, Tuple

import numpy as np

from ave.core.constants import EPS_DIVZERO

# ====================================================================
# 1.  S₁₁ frequency sweep through a graded impedance profile
# ====================================================================


def graded_tl_eigenvalue(
    Z_func: Callable[[float], float],
    r_inner: float,
    r_outer: float,
    N_shells: int = 50,
    f_min: float = 0.0,
    f_max: float = 1.0,
    N_freq: int = 200,
    c_wave: float = 1.0,
    Z_source: float = 1.0,
    Z_load: Optional[float] = None,
    stub_length_func: Optional[Callable[[float], float]] = None,
    stub_termination: str = "open",
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, List[Tuple[float, float]]]:
    r"""
    S₁₁ frequency sweep through a graded impedance profile.

    Discretises the radial impedance gradient into *N_shells* TL
    segments, optionally attaching tangential stubs at each junction.
    Sweeps frequency to compute |S₁₁(f)|² and extracts resonant modes.

    The same function works at every scale:

    * **BH ringdown**: ``Z_func = lambda r: Z0 * n(r)``,
      ``stub_length_func = lambda r: 2*pi*r``
    * **Electron orbital**: ``Z_func = lambda r: Z0 / (1 + V(r)/E)``
    * **Protein backbone**: ``Z_func`` from bond constants

    Parameters
    ----------
    Z_func : callable(r) -> float
        Characteristic impedance at radius *r*.
    r_inner, r_outer : float
        Radial bounds of the graded region.
    N_shells : int
        Number of discrete TL segments.
    f_min, f_max : float
        Frequency sweep range.
    N_freq : int
        Number of frequency points.
    c_wave : float
        Wave speed in the medium.
    Z_source : float
        Source impedance (outer boundary).
    Z_load : float or None
        Load impedance (inner boundary).  None → matched.
    stub_length_func : callable(r) -> float or None
        Tangential stub length at each junction.
    stub_termination : str
        ``'open'`` or ``'short'`` for stubs.

    Returns
    -------
    freqs : ndarray, shape (N_freq,)
    s11_power : ndarray, shape (N_freq,)
    s21_power : ndarray, shape (N_freq,)
    modes : list of (f₀, Q)
    """
    # ── Pre-compute shell geometry (vectorised, once) ──
    r_edges = np.linspace(r_inner, r_outer, N_shells + 1)
    r_mids = 0.5 * (r_edges[:-1] + r_edges[1:])
    dr = np.diff(r_edges)  # (N_shells,)
    Z_shells = np.array([Z_func(r) for r in r_mids])  # (N_shells,)

    if Z_load is None:
        Z_load = float(Z_shells[0])

    # Pre-compute stub lengths if needed
    L_stubs = None
    if stub_length_func is not None:
        L_stubs = np.array([stub_length_func(r) for r in r_mids])

    # n_local for propagation constant: n = Z_shell / Z_source
    n_local = Z_shells / Z_source  # (N_shells,)

    # ── Frequency sweep (vectorised inner loop) ──
    freqs = np.linspace(f_min, f_max, N_freq)
    s11_power = np.zeros(N_freq)
    s21_power = np.zeros(N_freq)

    for fi in range(N_freq):
        f = freqs[fi]
        if f <= 0:
            continue

        omega = 2.0 * np.pi * f

        # Propagation constants for all shells at this frequency
        # β = ω·n/c,  γℓ = jβ·dr  (lossless)
        beta = omega * n_local / c_wave  # (N_shells,)
        gamma_l = 1j * beta * dr  # (N_shells,)

        # NOTE: No clamping needed.  When Z_func applies Axiom 4
        # saturation, n_eff ∈ [1, ~2.8] so |γℓ| stays bounded.
        # The saturation IS the natural bound (S → 0 near horizon).

        # Build ABCD matrices for all segments
        cosh_gl = np.cosh(gamma_l)  # (N_shells,)
        sinh_gl = np.sinh(gamma_l)  # (N_shells,)

        # Stub ABCD matrices (if tangential mode)
        if L_stubs is not None:
            beta_stub = omega * n_local / c_wave
            gamma_l_stub = 1j * beta_stub * L_stubs

        # Sequential ABCD cascade (inherently serial for matrix chain)
        # M = [[A,B],[C,D]], starting with identity
        A, B, C, D = 1.0 + 0j, 0.0 + 0j, 0.0 + 0j, 1.0 + 0j

        for i in range(N_shells):
            # Segment ABCD: [[cosh, Z*sinh], [sinh/Z, cosh]]
            c_gl = cosh_gl[i]
            s_gl = sinh_gl[i]
            Zc = Z_shells[i]

            sA = c_gl
            sB = Zc * s_gl
            sC = s_gl / Zc if abs(Zc) > EPS_DIVZERO else 0.0
            sD = c_gl

            # M = M @ segment
            nA = A * sA + B * sC
            nB = A * sB + B * sD
            nC = C * sA + D * sC
            nD = C * sB + D * sD
            A, B, C, D = nA, nB, nC, nD

            # Attach tangential stub (shunt admittance)
            if L_stubs is not None and i < N_shells - 1:
                gl_s = gamma_l_stub[i]
                Zs = Z_shells[i]
                if stub_termination == "open":
                    # Y_stub = (1/Z) * tanh(γℓ)
                    Y_stub = np.tanh(gl_s) / Zs if abs(Zs) > EPS_DIVZERO else 0.0
                else:
                    # Y_stub = (1/Z) / tanh(γℓ)
                    th = np.tanh(gl_s)
                    Y_stub = 1.0 / (Zs * th) if abs(Zs * th) > EPS_DIVZERO else 0.0

                # Shunt: M = M @ [[1,0],[Y,1]]
                nA = A
                nB = B
                nC = C + A * Y_stub
                nD = D + B * Y_stub
                A, B, C, D = nA, nB, nC, nD

        # S₁₁ and S₂₁ from ABCD
        denom = A + B / Z_load + C * Z_source + D
        if abs(denom) > EPS_DIVZERO:
            Gamma = (A + B / Z_load - C * Z_source - D) / denom
            T21 = 2.0 / denom
        else:
            Gamma = 1.0
            T21 = 0.0

        s11_power[fi] = abs(Gamma) ** 2
        s21_power[fi] = abs(T21) ** 2

    # ── Extract resonant modes ──
    modes = cavity_q_from_spectrum(freqs, s11_power)

    return freqs, s11_power, s21_power, modes


# ====================================================================
# 2.  Q extraction from S₁₁ spectrum
# ====================================================================


def cavity_q_from_spectrum(
    freqs: np.ndarray,
    s11_power: np.ndarray,
    min_prominence: float = 0.01,
) -> List[Tuple[float, float]]:
    r"""
    Extract resonant modes and Q-factors from an |S₁₁(f)|² spectrum.

    Finds peaks in the reflection spectrum and computes the loaded Q
    from the 3 dB bandwidth:

    .. math::
        Q = \frac{f_0}{\Delta f_{3\,\mathrm{dB}}}

    Parameters
    ----------
    freqs : ndarray
    s11_power : ndarray
    min_prominence : float

    Returns
    -------
    modes : list of (f₀, Q)
    """
    modes = []
    N = len(freqs)
    if N < 5:
        return modes

    for i in range(2, N - 2):
        if not (
            s11_power[i] > s11_power[i - 1]
            and s11_power[i] > s11_power[i + 1]
            and s11_power[i] > s11_power[i - 2]
            and s11_power[i] > s11_power[i + 2]
        ):
            continue

        peak_val = s11_power[i]
        lo = max(0, i - 20)
        hi = min(N, i + 21)
        local_min = min(np.min(s11_power[lo:i]), np.min(s11_power[i + 1 : hi]))
        if peak_val - local_min < min_prominence:
            continue

        f0 = freqs[i]
        half_power = peak_val / 2.0

        # 3 dB points
        f_low = f0
        for j in range(i, 0, -1):
            if s11_power[j] < half_power:
                frac = (half_power - s11_power[j]) / max(s11_power[j + 1] - s11_power[j], EPS_DIVZERO)
                f_low = freqs[j] + frac * (freqs[j + 1] - freqs[j])
                break

        f_high = f0
        for j in range(i, N - 1):
            if s11_power[j] < half_power:
                frac = (half_power - s11_power[j]) / max(s11_power[j - 1] - s11_power[j], EPS_DIVZERO)
                f_high = freqs[j] - frac * (freqs[j] - freqs[j - 1])
                break

        bw = f_high - f_low
        Q = f0 / bw if bw > 0 else float("inf")
        modes.append((f0, Q))

    modes.sort(key=lambda m: m[0])
    return modes


# ====================================================================
# 3.  Impulse response via IFFT
# ====================================================================


def impulse_response(
    freqs: np.ndarray,
    s21_spectrum: np.ndarray,
) -> Tuple[np.ndarray, np.ndarray]:
    r"""
    Time-domain impulse response from IFFT of S₂₁(f).

    Parameters
    ----------
    freqs : ndarray  (uniform spacing)
    s21_spectrum : ndarray  (complex S₂₁)

    Returns
    -------
    times : ndarray
    amplitude : ndarray
    """
    N = len(freqs)
    df = freqs[1] - freqs[0] if N > 1 else 1.0
    N_fft = int(2 ** np.ceil(np.log2(max(N, 64))))
    padded = np.zeros(N_fft, dtype=complex)
    padded[:N] = s21_spectrum
    h = np.fft.ifft(padded)
    dt = 1.0 / (N_fft * df)
    times = np.arange(N_fft) * dt
    return times, np.abs(h)

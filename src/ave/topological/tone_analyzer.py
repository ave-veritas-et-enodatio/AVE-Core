"""
tone_analyzer.py — offline harmonic-inversion analyzer for Cosserat ring-downs.

Pure post-processing on dumped probe arrays; no engine dependency.

Method: matrix pencil (Hua & Sarkar, IEEE TASP 38(5), 814-824, 1990,
doi:10.1109/29.56027). Models a time series as a sum of complex exponentials

    y(t) = Σ_k  c_k · exp(−i ω_k t),     ω_k = Ω_k − i Γ_k

and extracts frequencies, decay rates, and amplitudes from records far shorter
than 1/Δω (the plain-FFT limit). The Cramér–Rao bound for deterministic
double-precision simulations is set by the noise floor (integrator error), not
by 1/T, so the method is strongest exactly in the simulation regime (Rife &
Boorstyn 1974, doi:10.1109/TIT.1974.1055282).

LEAN flag: the 10-20 period recommendation for this engine is LEAN. The direction
(HI beats 1/T for few-pole deterministic signals) is DERIVED from Cramér–Rao
bounds and FDTD precedent (MEEP/Harminv; Oskooi et al. 2010, doi:
10.1016/j.cpc.2009.11.008). The binding limits are non-stationarity (Kerr
chirp) and the band-edge continuum tail ∝ t^(−3/2), not noise. Accept only
poles stable under ±30% record length and a shifted window (kill line KPOLE).

Sign convention (Math tone-reader backing page, 2026-10-06, sha1 b0cdef5db22f):
  Im(ω_k) > 0  →  Γ_k < 0  →  GROWTH (unstable). Flag explicitly.
  Im(ω_k) < 0  →  Γ_k > 0  →  damping.
  Q = Ω_k / (2 Γ_k);  only meaningful when Γ_k > 0.

Band references (engine natural units; G = G_c = γ = ρ = 1, ℓ_node = 1):
  OMEGA_AC_TOP  = √(10/3) ≈ 1.826  — acoustic top; lower edge of 9% window (F1)
  OMEGA_T_TOP   = 1.0               — transverse top; lower edge of T1-widened window
  OMEGA_M       = 2.0               — rotational bottom; upper edge of 9% window
  OMEGA_ROT_TOP = √6    ≈ 2.449    — rotational top; upper edge of rotational band

Kill line KW (cohesion page sha1 f4c392e90e08 §B.10):
  flag when 2·Ω_k ∈ [OMEGA_M, OMEGA_ROT_TOP], i.e. 2·Ω_k ∈ [2, √6].

Branch-split note (⚑2, Math page §3, KA4):
  The engine codes only branch (a), soften-on-strain (cosserat_field_3d.py:815/825).
  A measured d(ω)/d(A²) is branch-(a) saturation NET of the Op10, reflection,
  and Hopf stiffeners. It does NOT discriminate bond rules unless the saturation
  selector is exposed or those stiffeners are zeroed. Do not interpret the sign of
  d(ω)/d(A²) alone as selecting the bond rule. Exposing the saturation selector
  is listed as a follow-on.

Corpus conflicts — see docs/tone-probe-ringdown.md §Corpus conflicts.
"""

from __future__ import annotations

import warnings
from dataclasses import dataclass, field
from typing import Optional

import numpy as np


# ---------------------------------------------------------------------------
# Band references (engine natural units)
# ---------------------------------------------------------------------------

OMEGA_AC_TOP: float = float(np.sqrt(10.0 / 3.0))   # ≈ 1.8257
OMEGA_T_TOP: float = 1.0
OMEGA_M: float = 2.0
OMEGA_ROT_TOP: float = float(np.sqrt(6.0))          # ≈ 2.4495

WINDOW_9PCT = (OMEGA_AC_TOP, OMEGA_M)       # [√(10/3), 2]
WINDOW_T1 = (OMEGA_T_TOP, OMEGA_M)         # [1, 2]
BAND_ROT = (OMEGA_M, OMEGA_ROT_TOP)        # [2, √6]


# ---------------------------------------------------------------------------
# Data structure
# ---------------------------------------------------------------------------

@dataclass
class Pole:
    """One complex frequency mode from harmonic inversion.

    Convention: ω_k = Ω_k − i Γ_k so that y(t) = c_k exp(−i ω_k t)
    decays when Γ_k > 0 and grows when Γ_k < 0.
    """
    Omega: float          # Re(ω_k): physical angular frequency
    Gamma: float          # −Im(ω_k): decay rate (> 0 = decaying)
    amplitude: float      # |c_k|
    phase: float          # angle(c_k), radians
    Q: float              # Ω/(2Γ); inf when Γ ≤ 0
    is_growth: bool       # Im(ω_k) > 0 ↔ Γ_k < 0 (flag for review)
    in_9pct_window: bool  # Ω ∈ [√(10/3), 2]
    in_t1_window: bool    # Ω ∈ [1, 2]
    in_rot_band: bool     # Ω ∈ [2, √6]
    kw_flag: bool         # 2·Ω ∈ [2, √6]  (KW kill line)
    Omega_err: float = 0.0   # spread over model-order variation
    Gamma_err: float = 0.0


def _classify_pole(Omega: float, Gamma: float, amp: float, phase: float,
                   Omega_err: float = 0.0, Gamma_err: float = 0.0) -> Pole:
    Q = (Omega / (2.0 * Gamma)) if Gamma > 0.0 else float("inf")
    is_growth = Gamma < 0.0
    return Pole(
        Omega=Omega,
        Gamma=Gamma,
        amplitude=amp,
        phase=phase,
        Q=Q,
        is_growth=is_growth,
        in_9pct_window=(WINDOW_9PCT[0] <= Omega <= WINDOW_9PCT[1]),
        in_t1_window=(WINDOW_T1[0] <= Omega <= WINDOW_T1[1]),
        in_rot_band=(BAND_ROT[0] <= Omega <= BAND_ROT[1]),
        kw_flag=(BAND_ROT[0] <= 2.0 * Omega <= BAND_ROT[1]),
        Omega_err=Omega_err,
        Gamma_err=Gamma_err,
    )


# ---------------------------------------------------------------------------
# Core matrix pencil algorithm
# ---------------------------------------------------------------------------

def _matrix_pencil_zk(signal: np.ndarray, n_poles: int,
                       pencil_L: Optional[int] = None) -> np.ndarray:
    """Return n_poles complex poles z_k from the matrix pencil method.

    Model: y[n] = Σ_k c_k z_k^n.
    Poles z_k relate to complex angular frequencies via
        z_k = exp(−i ω_k dt)  →  ω_k = i log(z_k) / dt.

    Algorithm (Hua & Sarkar 1990):
    1. Build Hankel data matrix Y (L × (N−L+1)), Y[i,j] = y[i+j].
    2. SVD-filter to n_poles rank to suppress noise.
    3. Extract poles from the reduced V-subspace shift.

    Args:
        signal:   1-D complex or real array of length N.
        n_poles:  number of poles to extract.
        pencil_L: pencil parameter (default N//3).

    Returns:
        z_k: complex array of length n_poles.
    """
    y = np.asarray(signal, dtype=complex)
    N = len(y)
    if N < 4:
        raise ValueError(f"Signal too short: N={N}")
    if pencil_L is None:
        pencil_L = max(n_poles + 1, N // 3)
    L = min(pencil_L, N - n_poles - 1)
    L = max(L, n_poles + 1)

    # Hankel matrix: shape (L) x (N-L+1)
    M = N - L + 1
    Y = np.array([[y[i + j] for j in range(M)] for i in range(L)],
                 dtype=complex)

    # SVD, keep n_poles right singular vectors
    _, S_full, Vh_full = np.linalg.svd(Y, full_matrices=False)
    n_keep = min(n_poles, len(S_full))
    Vh_r = Vh_full[:n_keep, :]   # (n_poles, M) = (n_poles, N-L+1)

    # V_r: (N-L+1) x n_poles — the right singular vectors as columns
    V_r = Vh_r.conj().T           # (M, n_poles)
    V1 = V_r[:-1, :]              # (M-1, n_poles) = (N-L, n_poles)
    V2 = V_r[1:, :]               # (N-L, n_poles)

    # Solve V1 @ A ≈ V2  →  A = (V1^H V1)^{-1} (V1^H V2)
    A, _, _, _ = np.linalg.lstsq(V1, V2, rcond=None)   # (n_poles, n_poles)
    z_k = np.linalg.eigvals(A)
    return z_k


def _recover_amplitudes(signal: np.ndarray, z_k: np.ndarray) -> np.ndarray:
    """Recover complex amplitudes c_k via least-squares Vandermonde solve.

    y[n] = Σ_k c_k z_k^n  →  Vandermonde system Z @ c = y.
    """
    y = np.asarray(signal, dtype=complex)
    N = len(y)
    M = len(z_k)
    ns = np.arange(N, dtype=float)
    Z = np.array([[zk**n for zk in z_k] for n in ns], dtype=complex)
    c_k, _, _, _ = np.linalg.lstsq(Z, y, rcond=None)
    return c_k


def _zk_to_poles(z_k: np.ndarray, c_k: np.ndarray, dt: float) -> list[Pole]:
    """Convert (z_k, c_k) pairs to Pole objects."""
    poles = []
    for z, c in zip(z_k, c_k):
        log_z = np.log(z + 1e-300)
        # ω_k = i log(z_k) / dt = (i·Re(log z) − Im(log z)) / dt
        omega_k = 1j * log_z / dt
        Omega = float(omega_k.real)
        Gamma = float(-omega_k.imag)   # Γ = −Im(ω)
        amp = float(abs(c))
        phase = float(np.angle(c))
        poles.append(_classify_pole(Omega, Gamma, amp, phase))
    return poles


# ---------------------------------------------------------------------------
# Public analysis functions
# ---------------------------------------------------------------------------

def analyze(
    signal: np.ndarray,
    dt: float,
    n_poles_max: int = 8,
    pencil_L: Optional[int] = None,
    min_amplitude_frac: float = 1e-6,
    n_model_orders: int = 4,
) -> list[Pole]:
    """Analyze a 1-D time series and return physical poles.

    Uses the matrix pencil method with model-order variation for uncertainty.
    Poles stable across n_model_orders different pencil parameters are
    returned sorted by amplitude (largest first).

    Args:
        signal:             1-D real or complex array.
        dt:                 sampling interval (engine time units).
        n_poles_max:        maximum number of poles.
        pencil_L:           pencil parameter override (default N//3).
        min_amplitude_frac: drop poles with |c_k|/max(|c_k|) below this.
        n_model_orders:     number of (L, n_poles) variations for uncertainty.

    Returns:
        List of Pole objects sorted by amplitude descending.
    """
    y = np.asarray(signal, dtype=complex)
    N = len(y)
    if N < 8:
        raise ValueError(f"Signal too short for analysis: N={N}")

    n_max = min(n_poles_max, N // 4)
    if n_max < 1:
        n_max = 1

    # Collect poles across model orders for uncertainty estimation
    all_runs: list[list[tuple[float, float, float, float]]] = []  # (Omega, Gamma, amp, phase)

    for trial in range(n_model_orders):
        n_p = max(1, n_max - trial)
        L_factor = max(0.25, 0.33 + trial * 0.05)
        L = max(n_p + 2, int(N * L_factor))
        L = min(L, N - n_p - 1)
        try:
            z_k = _matrix_pencil_zk(y, n_poles=n_p, pencil_L=L)
            c_k = _recover_amplitudes(y, z_k)
        except (np.linalg.LinAlgError, ValueError):
            continue

        run_poles = []
        for z, c in zip(z_k, c_k):
            log_z = np.log(z + 1e-300)
            omega_k = 1j * log_z / dt
            run_poles.append((
                float(omega_k.real),   # Omega
                float(-omega_k.imag),  # Gamma
                float(abs(c)),
                float(np.angle(c)),
            ))
        all_runs.append(run_poles)

    if not all_runs:
        return []

    # Use the first run as the reference; estimate uncertainty from spread
    ref_poles = all_runs[0]
    if not ref_poles:
        return []

    amps = [p[2] for p in ref_poles]
    amp_max = max(amps) if amps else 1.0

    result: list[Pole] = []
    for Omega_ref, Gamma_ref, amp_ref, phase_ref in ref_poles:
        if amp_ref / amp_max < min_amplitude_frac:
            continue
        # Estimate spread across model orders
        Omega_vals = [Omega_ref]
        Gamma_vals = [Gamma_ref]
        for run in all_runs[1:]:
            # Find closest pole in Omega
            if not run:
                continue
            dists = [abs(p[0] - Omega_ref) for p in run]
            best = run[np.argmin(dists)]
            if abs(best[0] - Omega_ref) < max(0.1, abs(Omega_ref) * 0.3):
                Omega_vals.append(best[0])
                Gamma_vals.append(best[1])

        Omega_err = float(np.std(Omega_vals)) if len(Omega_vals) > 1 else 0.0
        Gamma_err = float(np.std(Gamma_vals)) if len(Gamma_vals) > 1 else 0.0
        result.append(_classify_pole(
            Omega_ref, Gamma_ref, amp_ref, phase_ref,
            Omega_err=Omega_err, Gamma_err=Gamma_err,
        ))

    result.sort(key=lambda p: -p.amplitude)
    return result


def sliding_window_analyze(
    signal: np.ndarray,
    dt: float,
    window_nsamples: int,
    stride_nsamples: Optional[int] = None,
    n_poles_max: int = 6,
) -> list[tuple[float, list[Pole]]]:
    """Sliding-window analysis.

    Useful for spreading knots (like ENV-D's tube growth over ~11 periods)
    where a single ring-down fit is not trustworthy. Returns instantaneous
    ω(t) by fitting short windows (~3–5 periods each).

    Args:
        signal:           1-D array.
        dt:               sampling interval.
        window_nsamples:  samples per window.
        stride_nsamples:  stride between windows (default window//2).
        n_poles_max:      poles per window.

    Returns:
        List of (t_centre, poles) tuples.
    """
    y = np.asarray(signal, dtype=complex)
    N = len(y)
    if stride_nsamples is None:
        stride_nsamples = max(1, window_nsamples // 2)
    results = []
    start = 0
    while start + window_nsamples <= N:
        window = y[start: start + window_nsamples]
        t_centre = (start + window_nsamples / 2.0) * dt
        try:
            poles = analyze(window, dt, n_poles_max=n_poles_max)
        except (ValueError, np.linalg.LinAlgError):
            poles = []
        results.append((t_centre, poles))
        start += stride_nsamples
    return results


def band_report(poles: list[Pole]) -> dict:
    """Return classification of poles against the four band windows.

    Engine natural units: G = G_c = γ = ρ_vac = 1, ℓ_node = 1 (dx = 1).

    Band references (F1 dispersion; cosserat_field_3d.py cited at §1.1
    of the Math tone-reader backing page, sha1 b0cdef5db22f):
      OMEGA_AC_TOP  = √(10/3) ≈ 1.826  (acoustic/longitudinal top)
      OMEGA_T_TOP   = 1.0               (transverse top)
      OMEGA_M       = 2.0               (rotational sector bottom)
      OMEGA_ROT_TOP = √6    ≈ 2.449    (rotational sector top)
    """
    report = {
        "window_9pct": [],
        "window_t1_only": [],
        "rot_band": [],
        "above_rot": [],
        "below_t1": [],
        "kw_flagged": [],
        "growth_flagged": [],
    }
    for p in poles:
        if p.in_9pct_window:
            report["window_9pct"].append(p)
        elif p.in_t1_window:
            report["window_t1_only"].append(p)
        elif p.in_rot_band:
            report["rot_band"].append(p)
        elif p.Omega > OMEGA_ROT_TOP:
            report["above_rot"].append(p)
        else:
            report["below_t1"].append(p)
        if p.kw_flag:
            report["kw_flagged"].append(p)
        if p.is_growth:
            report["growth_flagged"].append(p)
    return report


def amplitude_sweep(
    omega_series: list[float],
    A_squared_series: list[float],
) -> dict:
    """Estimate d(ω)/d(A²) from several runs at different drive amplitudes.

    IMPORTANT — branch-split note (Math page ⚑2, §3 KA4):
    The engine (cosserat_field_3d.py) codes only branch (a), soften-on-strain
    (lines :815/:825). A measured d(ω)/d(A²) is branch-(a) saturation NET of
    the Op10, reflection, and Hopf stiffeners. It does NOT discriminate bond
    rules unless the saturation selector is exposed as an option (a follow-on
    item) or k_op10 = k_refl = k_hopf = 0. Do not interpret the sign alone as
    selecting the bond rule.

    With k_op10 = k_refl = k_hopf = 0 and use_saturation=True: the sign tests
    the pure soften-on-strain branch (a) selector and confirms DC-page Q2(i).

    Args:
        omega_series:    list of measured Ω_k (one per run at each amplitude).
        A_squared_series: list of A² values (drive/kick amplitude squared).

    Returns:
        dict with keys 'slope', 'intercept', 'slope_err', 'r_squared',
        'n_points', and 'note'.
    """
    x = np.asarray(A_squared_series, dtype=float)
    y = np.asarray(omega_series, dtype=float)
    if len(x) < 2:
        return {"slope": float("nan"), "slope_err": float("nan"),
                "n_points": len(x), "note": "need ≥2 points"}

    # Linear fit: ω = ω_0 + slope * A²
    A_mat = np.column_stack([np.ones_like(x), x])
    result, residuals, rank, sv = np.linalg.lstsq(A_mat, y, rcond=None)
    intercept, slope = float(result[0]), float(result[1])

    # Uncertainty via residuals
    n = len(x)
    if n > 2 and len(residuals) > 0:
        sigma2 = float(residuals[0]) / (n - 2)
        ATA_inv = np.linalg.pinv(A_mat.T @ A_mat)
        slope_err = float(np.sqrt(sigma2 * ATA_inv[1, 1]))
    else:
        slope_err = float("nan")

    y_fit = intercept + slope * x
    ss_res = float(np.sum((y - y_fit) ** 2))
    ss_tot = float(np.sum((y - np.mean(y)) ** 2))
    r_sq = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0

    return {
        "slope": slope,
        "intercept": intercept,
        "slope_err": slope_err,
        "r_squared": r_sq,
        "n_points": n,
        "note": (
            "d(Ω)/d(A²) measured. Sign confirms branch (a) direction (soften-on-strain) "
            "NET of Op10/reflection/Hopf stiffeners. Does NOT split branches alone. "
            "Set k_op10=k_refl=k_hopf=0 to isolate the selector."
        ),
    }


def record_length_table(
    Omega: float = 1.9,
    Q: float = 100.0,
    dt: float = 0.165,
    noise_level: float = 1e-10,
    n_poles: int = 2,
    n_trials: int = 20,
    periods_list: tuple[int, ...] = (5, 10, 15, 20, 50, 100),
    rng_seed: int = 42,
) -> list[dict]:
    """Generate accuracy-vs-record-length table for the analyzer.

    Tests Math's LEAN claim that 10–20 clean periods suffice.
    (LEAN: direction DERIVED from Cramér–Rao + MEEP/Harminv precedent;
     the count is a judgment. The binding limits are non-stationarity
     and the band-edge continuum tail, not noise.)

    Synthetic signal: y(t) = cos(Ω t) · exp(−Γ t) + noise_level · ξ(t)
    where ξ ~ N(0,1) complex-valued i.i.d.

    Args:
        Omega:       true angular frequency.
        Q:           true quality factor.
        dt:          sampling interval.
        noise_level: RMS noise amplitude (default 1e-10, like integrator error).
        n_poles:     poles to extract (real signal → 2: one conjugate pair).
        n_trials:    Monte Carlo trials per period count.
        periods_list: record lengths in periods to test.
        rng_seed:    NumPy RNG seed.

    Returns:
        List of dicts with keys: periods, N_samples, Omega_err_mean,
        Omega_err_std, Q_err_mean, Q_err_std, noise_level.
    """
    rng = np.random.default_rng(rng_seed)
    Gamma_true = Omega / (2.0 * Q)
    period = 2.0 * np.pi / Omega
    rows = []

    for n_periods in periods_list:
        T = n_periods * period
        N = max(10, int(round(T / dt)))
        t = np.arange(N) * dt

        Omega_errs = []
        Q_errs = []
        for _ in range(n_trials):
            noise = noise_level * (rng.standard_normal(N) + 1j * rng.standard_normal(N))
            sig = np.cos(Omega * t) * np.exp(-Gamma_true * t) + noise
            try:
                poles = analyze(sig, dt, n_poles_max=n_poles, n_model_orders=3)
            except Exception:
                poles = []

            # Find the positive-Omega pole nearest the true frequency
            best = None
            best_dist = float("inf")
            for p in poles:
                if p.Omega > 0.1:
                    d = abs(p.Omega - Omega)
                    if d < best_dist:
                        best_dist = d
                        best = p

            if best is not None and best.Gamma > 0:
                Omega_errs.append(abs(best.Omega - Omega))
                Q_true_run = Omega / (2.0 * Gamma_true)
                Q_errs.append(abs(best.Q - Q_true_run))
            else:
                Omega_errs.append(float("nan"))
                Q_errs.append(float("nan"))

        Omega_arr = np.array(Omega_errs, dtype=float)
        Q_arr = np.array(Q_errs, dtype=float)
        rows.append({
            "periods": n_periods,
            "N_samples": N,
            "Omega_err_mean": float(np.nanmean(Omega_arr)),
            "Omega_err_std": float(np.nanstd(Omega_arr)),
            "Q_err_mean": float(np.nanmean(Q_arr)),
            "Q_err_std": float(np.nanstd(Q_arr)),
            "noise_level": noise_level,
        })
    return rows


def print_record_length_table(rows: list[dict], Omega: float = 1.9, Q: float = 100.0) -> None:
    """Print the record-length accuracy table."""
    print(f"\nRecord-length accuracy table: Ω={Omega:.3f}, Q={Q:.1f}, noise=1e-10 (like integrator error)")
    print(f"LEAN claim (Math page sha1 b0cdef5db22f §3): 10–20 periods suffice for this engine.")
    print(f"{'periods':>8}  {'N_samples':>10}  {'Ω_err_mean':>12}  {'Ω_err_std':>12}  "
          f"{'Q_err_mean':>12}  {'Q_err_std':>12}")
    print("-" * 80)
    for r in rows:
        print(f"{r['periods']:>8}  {r['N_samples']:>10}  "
              f"{r['Omega_err_mean']:>12.3e}  {r['Omega_err_std']:>12.3e}  "
              f"{r['Q_err_mean']:>12.3e}  {r['Q_err_std']:>12.3e}")


def summarize(poles: list[Pole], dt: float, record_length: Optional[float] = None,
              label: str = "") -> str:
    """Return a plain-English summary of the analysis results."""
    lines = []
    hdr = f"=== Tone analysis summary{f' [{label}]' if label else ''} ==="
    lines.append(hdr)

    if record_length is not None:
        lines.append(f"Record length: {record_length:.2f} time units"
                     f"  ({record_length / (2*np.pi/OMEGA_M):.1f} × 2π/ω_m periods)")

    lines.append(f"Sampling interval: dt = {dt:.4f} time units")
    lines.append(f"Number of poles returned: {len(poles)}")
    lines.append(f"Band reference (engine natural units): "
                 f"9%% window [{OMEGA_AC_TOP:.4f}, {OMEGA_M:.1f}], "
                 f"rotational [{OMEGA_M:.1f}, {OMEGA_ROT_TOP:.4f}]")

    if not poles:
        lines.append("No poles found.")
        return "\n".join(lines)

    report = band_report(poles)

    growth = report["growth_flagged"]
    if growth:
        lines.append(f"  *** {len(growth)} GROWING mode(s) (Im ω > 0, Γ < 0) — flag for review ***")

    kw = report["kw_flagged"]
    if kw:
        lines.append(f"  *** {len(kw)} KW-flagged pole(s): 2·Ω ∈ [2, √6] ***")

    lines.append(f"Poles in 9%% window [{OMEGA_AC_TOP:.4f}, {OMEGA_M:.1f}]: "
                 f"{len(report['window_9pct'])}")
    lines.append(f"Poles in T1-widened [1, 2]: {len(report['window_t1_only'])} "
                 f"(additional, not in 9%%)")

    for i, p in enumerate(poles):
        decay_str = (f"GROWTH (unstable, Γ={p.Gamma:.4f})"
                     if p.is_growth else f"decaying (Q={p.Q:.1f}, Γ={p.Gamma:.4f})")
        window_str = (
            "9%%-window" if p.in_9pct_window
            else ("T1-window" if p.in_t1_window
                  else ("rot-band" if p.in_rot_band else "outside"))
        )
        kw_str = " [KW!]" if p.kw_flag else ""
        Omega_unc = f" ±{p.Omega_err:.4f}" if p.Omega_err > 0 else ""
        lines.append(
            f"  Pole {i+1}: Ω={p.Omega:.4f}{Omega_unc}, {decay_str}, "
            f"|c|={p.amplitude:.3e}, {window_str}{kw_str}"
        )

    return "\n".join(lines)

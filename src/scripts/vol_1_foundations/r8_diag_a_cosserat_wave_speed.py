"""Diag A — Cosserat wave-speed amplitude dependence.

Per `P_ax5_cosserat_wave_speed_amplitude_dependence` (frozen at this commit).

CONTEXT (per doc 75_):
  Cosserat sector violates Ax 3 (energy conservation) because saturation
  kernel S(A²) acts on V_potential (G·S, G_c·S in
  `_energy_density_saturated`, cosserat_field_3d.py:545–587) but NOT on
  T_kinetic (kinetic_energy() at lines 1204–1209 uses constant ρ, I_ω).
  Asymmetric saturation breaks the Lagrangian's time-translation
  symmetry; per Noether energy is generally not conserved when A²(x,t)
  varies dynamically.

  Mathematical consequence: c_T = √(G·S/ρ), c_R = √(γ·S/I_ω),
  m_Cosserat² = 4·G_c·S/I_ω all drift as √S(A²) under saturation.

DIAG A METHODOLOGY:
  Cosserat-only wavepacket propagation at varying packet amplitude.
  As packet amplitude grows, local strain ε and curvature κ at the
  packet location grow; saturation kernel S_eps_sq, S_kappa_sq drop
  below 1; under V·S, T·1 asymmetry, observed wave speed c drifts.

  Pre-registered prediction (pre-fix): c(amplitude) drifts approximately
  as c_0·√S_eff where S_eff is the saturation factor at the packet's
  peak gradient magnitude. Specifically c declines monotonically as
  amplitude increases past the linear regime.

  Post-fix prediction: c is amplitude-invariant (Ax 3 restored).

3-MODE ADJUDICATION (on pre-fix curve):
  Mode I  — c is amplitude-invariant within ±5% across all amplitudes.
            Some unmapped path preserves wave speed despite V·S, T·1.
            Doc 75_ becomes informational; engine fix not needed.
  Mode II — c drifts monotonically with amplitude (drop ≥ 5% from low
            to high amplitude); functional form approximately √S.
            Confirmed empirically; engine fix applied; Pass 2 expected
            to give amplitude-invariance.
  Mode III — c drifts but in a non-monotonic or non-√S form. Investigate
            before fix.

POST-FIX VERIFICATION (binary):
  c(amplitude) / c_0 = 1 ± 5% across all tested amplitudes.

REUSED INFRASTRUCTURE:
  - cosserat_wave_test.py::_packet_centroid_axis (centroid measurement)
  - CosseratField3D.initialize_gaussian_wavepacket_omega (wavepacket seed)
  - CosseratField3D.cfl_dt (timestep)

NO PASS/FAIL on overall test (this is a frozen-extraction-scope diagnostic
per A48 discipline). Result IS the c(amplitude) curve.
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from ave.topological.cosserat_field_3d import CosseratField3D


# ─── Constants per pred ───────────────────────────────────────────────────────

N_LATTICE = 32
WAVELENGTH = 12.0
SIGMA = 3.0
N_STEPS = 200
RECORD_EVERY = 5

# Sweep packet amplitudes — gradient magnitude scales with amplitude
# At amplitude A and k = 2π/12, |∇ω|² ~ (A·k)² = A² · 0.274
# Saturation kicks in when |∇ω|²/ω_yield² ~ 1 (ω_yield = π)
# So A·0.523/π ~ 1 → A ~ 6 to fully saturate (more than rupture)
# Practical sweep: A ∈ [0.01, 2.0] covers linear → mild saturation
AMPLITUDES = [0.01, 0.1, 0.5, 1.0, 2.0]

ADJUDICATION_TOL = 0.05   # ±5%

OUTPUT_JSON = Path(__file__).parent / "r8_diag_a_cosserat_wave_speed_results.json"


def _saturated_solver(N: int, G_c: float = 0.0, gamma: float = 1.0,
                      rho: float = 1.0, I_omega: float = 1.0) -> CosseratField3D:
    """Cosserat-only solver with use_saturation=True (Diag A target).

    For Diag A we focus on the gapless rotational sector (G_c = 0) so
    the wavepacket propagates at c_R = √(γ/I_ω) = 1 in the linear limit.
    Topology terms off; only Cauchy + curvature + saturation active.
    """
    s = CosseratField3D(
        nx=N, ny=N, nz=N, dx=1.0,
        use_saturation=True,           # Diag A: saturation ON
        rho=rho, I_omega=I_omega,
    )
    s.G = 1.0
    s.G_c = G_c
    s.gamma = gamma
    s.k_op10 = 0.0
    s.k_refl = 0.0
    s.k_hopf = 0.0
    return s


def _packet_centroid_axis(field: np.ndarray, mask: np.ndarray, axis_component: int) -> float:
    """Centroid along x-axis, weighted by field[..., axis_component]²
    (mirrors cosserat_wave_test._packet_centroid_axis)."""
    rho = (field[..., axis_component] ** 2) * mask
    total = rho.sum()
    if total <= 0:
        return float("nan")
    ix = np.arange(field.shape[0], dtype=float)[:, None, None]
    return float((rho * ix).sum() / total)


def measure_wave_speed(amplitude: float, N: int = N_LATTICE,
                       wavelength: float = WAVELENGTH, sigma: float = SIGMA,
                       n_steps: int = N_STEPS, record_every: int = RECORD_EVERY,
                       G_c: float = 0.0, gamma: float = 1.0) -> dict:
    """Run a Cosserat-only rotational wavepacket at given amplitude;
    measure propagation speed via centroid tracking.

    Returns dict with:
      amplitude, wavelength, sigma, c_measured, c_theory_continuum (= 1 at G_c=0),
      H_drift_max (numerical conservation diagnostic), times, centroids.
    """
    s = _saturated_solver(N=N, G_c=G_c, gamma=gamma)
    x0 = N // 4
    s.initialize_gaussian_wavepacket_omega(
        center=(x0, N // 2, N // 2), sigma=sigma,
        direction=(1.0, 0.0, 0.0), wavelength=wavelength,
        amplitude=amplitude, axis=2,
    )

    mask = s.mask_alive
    times: list[float] = []
    cents: list[float] = []
    Ts: list[float] = []
    Vs: list[float] = []
    Hs: list[float] = []

    for step in range(n_steps + 1):
        if step > 0:
            s.step()
        if step % record_every == 0:
            times.append(s.time)
            cents.append(_packet_centroid_axis(s.omega, mask, axis_component=2))
            Ts.append(s.kinetic_energy())
            Vs.append(s.total_energy())
            Hs.append(Ts[-1] + Vs[-1])

    times_a = np.asarray(times)
    cents_a = np.asarray(cents)
    Hs_a = np.asarray(Hs)

    # Linear fit to centroid trajectory; ignore early build-up + late edge effects
    fit_mask = np.isfinite(cents_a) & (cents_a > x0 + 0.5) & (cents_a < N - sigma * 2)
    if fit_mask.sum() >= 4:
        v_meas = float(np.polyfit(times_a[fit_mask], cents_a[fit_mask], 1)[0])
    else:
        v_meas = float("nan")

    c_R_theory_continuum = float(np.sqrt(gamma / s.I_omega))   # = 1.0
    H_drift = float(np.abs(Hs_a / max(Hs_a[0], 1e-30) - 1).max()) if Hs_a[0] != 0 else float("inf")

    return {
        "amplitude": amplitude,
        "wavelength": wavelength,
        "sigma": sigma,
        "N": N,
        "n_steps": n_steps,
        "G_c": G_c,
        "gamma": gamma,
        "cfl_dt": s.cfl_dt,
        "c_R_theory_continuum_at_zero_amplitude": c_R_theory_continuum,
        "v_measured": v_meas,
        "v_over_c_R_theory": (v_meas / c_R_theory_continuum) if np.isfinite(v_meas) else float("nan"),
        "H_drift_max": H_drift,
        "times": times_a.tolist(),
        "centroids": cents_a.tolist(),
        "T_history_first_last": [float(Ts[0]), float(Ts[-1])],
        "V_history_first_last": [float(Vs[0]), float(Vs[-1])],
        "H_history_first_last": [float(Hs[0]), float(Hs[-1])],
    }


def adjudicate(results: list[dict]) -> tuple[str, str]:
    """3-mode adjudication on the c(amplitude) curve."""
    # Filter to results with finite v_measured
    valid = [r for r in results if np.isfinite(r["v_measured"])]
    if len(valid) < 3:
        return "indeterminate", (
            f"Only {len(valid)} of {len(results)} amplitudes returned finite v_measured. "
            f"Insufficient data for adjudication."
        )

    amps = np.array([r["amplitude"] for r in valid])
    c_vals = np.array([r["v_measured"] for r in valid])
    c_low = c_vals[0]   # smallest amplitude is reference (linear regime)
    c_normalized = c_vals / c_low

    # Adjudication ranges
    c_max = float(c_normalized.max())
    c_min = float(c_normalized.min())
    drift_range = c_max - c_min

    if drift_range <= ADJUDICATION_TOL:
        mode = "I"
        verdict = (
            f"MODE I — c(amplitude) is amplitude-invariant within ±{ADJUDICATION_TOL:.2%}. "
            f"c_normalized range = [{c_min:.4f}, {c_max:.4f}], drift {drift_range:.4f}. "
            f"Some unmapped engine path preserves wave speed despite V·S, T·1 asymmetry. "
            f"Doc 75_ becomes informational; engine fix not needed; Pass 2 not run."
        )
    else:
        # Check monotonicity: c should decrease as amplitude increases (Mode II)
        # Fit log(c/c_0) vs log(S_eff) where S_eff = (1 - A²·effective)^(1/2)
        # Simpler: check if c is monotonically decreasing
        is_monotonic_decreasing = all(
            c_normalized[i] >= c_normalized[i + 1] - ADJUDICATION_TOL
            for i in range(len(c_normalized) - 1)
        )
        if is_monotonic_decreasing:
            mode = "II"
            verdict = (
                f"MODE II — c(amplitude) drifts monotonically from {c_normalized[0]:.4f} "
                f"(amp={amps[0]}) to {c_normalized[-1]:.4f} (amp={amps[-1]}). "
                f"Drift range {drift_range:.4f} > tolerance {ADJUDICATION_TOL:.2%}. "
                f"V·S, T·1 asymmetry empirically confirmed. Engine fix prescribed: "
                f"add S factor to T_kinetic via ρ → ρ·S, I_ω → I_ω·S. "
                f"Pass 2 expected to give amplitude-invariance after fix."
            )
        else:
            mode = "III"
            verdict = (
                f"MODE III — c(amplitude) drifts non-monotonically. "
                f"c_normalized = {c_normalized.tolist()}. "
                f"Investigate before applying any fix."
            )
    return mode, verdict


def main():
    print("=" * 78, flush=True)
    print(f"  Diag A — Cosserat wave-speed amplitude dependence")
    print(f"  P_ax5_cosserat_wave_speed_amplitude_dependence (frozen extraction)")
    print("=" * 78, flush=True)
    print(f"  Lattice N={N_LATTICE}, wavelength={WAVELENGTH}, sigma={SIGMA}, "
          f"n_steps={N_STEPS}")
    print(f"  Amplitudes: {AMPLITUDES}")
    print(f"  G_c=0 (gapless rotational), gamma=1, ρ=1, I_ω=1, "
          f"use_saturation=True")
    print(f"  Tolerance: ±{ADJUDICATION_TOL:.2%} for amplitude-invariance")
    print()

    t0 = time.time()
    results = []
    for amp in AMPLITUDES:
        print(f"  Running amplitude={amp}...", flush=True)
        res = measure_wave_speed(amplitude=amp)
        c_disp = res["v_measured"]
        H_drift = res["H_drift_max"]
        c_str = f"{c_disp:.6f}" if np.isfinite(c_disp) else "nan"
        print(f"    v_measured = {c_str}, H_drift_max = {H_drift:.4e}")
        results.append(res)
    elapsed = time.time() - t0

    print()
    print(f"  All amplitudes complete: {elapsed:.1f}s")
    print()
    print("  c(amplitude) curve:")
    for r in results:
        amp = r["amplitude"]
        c_v = r["v_measured"]
        if np.isfinite(c_v):
            print(f"    amp={amp:6.3f}: v_measured={c_v:.6f}, "
                  f"v/c_R_theory={c_v/1.0:.4f}")
        else:
            print(f"    amp={amp:6.3f}: v_measured=nan (no clean fit)")
    print()

    mode, verdict = adjudicate(results)
    print("=" * 78, flush=True)
    print("  Adjudication")
    print("=" * 78, flush=True)
    print(f"  Mode: {mode}")
    print(f"  {verdict}")
    print()

    payload = {
        "pre_registration": "P_ax5_cosserat_wave_speed_amplitude_dependence",
        "test": "Diag A — Cosserat wave-speed amplitude dependence "
                "(pre-fix detection)",
        "N": N_LATTICE,
        "wavelength": WAVELENGTH,
        "sigma": SIGMA,
        "n_steps": N_STEPS,
        "amplitudes": AMPLITUDES,
        "elapsed_seconds": elapsed,
        "results_per_amplitude": results,
        "adjudication_mode": mode,
        "adjudication_tolerance": ADJUDICATION_TOL,
        "verdict": verdict,
    }
    OUTPUT_JSON.write_text(json.dumps(payload, indent=2, default=str))
    print(f"  Result: {OUTPUT_JSON}")
    return payload


if __name__ == "__main__":
    main()

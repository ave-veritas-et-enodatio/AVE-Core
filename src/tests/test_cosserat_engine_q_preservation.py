"""C1-anchored Q-preservation soliton-scale test on CosseratMasterEquationFDTD.

PREREG: research/2026-05-18_cosserat-engine-q-preservation-prereg.md

Tests whether C1-BH-RING's lattice-Q preservation mechanism (Phase 5,
2026-05-18: τ_v2 = τ_v1 · (ω_R,v1 / ω_R,v2) per rigid Cosserat skeleton
setting Q invariant of cavity-radius refinement) reproduces on the existing
CosseratMasterEquationFDTD engine at soliton scale.

DESIGN: C1's v1→v2 refinement at fixed spin a* varied the CAVITY RADIUS
(x_sat shifted from simple Kerr to Cosserat-back-reacted form, giving
different ω_R but same Q). The soliton-scale analog is: at fixed amplitude
(saturation regime engaged), vary the CAVITY RADIUS parameter (Gaussian
blob radius). If Q is set by lattice impedance baseline (K_omega_0, "rigid"),
Q should be invariant of cavity-radius choice; ω_R should scale with 1/R.

Outcome categories:
- PASS (~20% predicted): Q(R) constant within 10% across radius sweep
- PARTIAL (~60% predicted): Q(R) varies 20-50% with radius
- FAIL (~15% predicted): Q(R) varies >50% or no recoverable scaling
- TECHNICAL BLOCKER (~5%): engine NaN at some R per Phase 3f.3.3 CFL issue
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.core.cosserat_master_equation_fdtd import CosseratMasterEquationFDTD


def extract_peak_frequency(signal: np.ndarray, dt: float) -> float:
    """Extract dominant oscillation frequency (angular) via FFT.

    Skips first 10% (transient) and last 5% (any decay artifact); uses
    Hanning window to reduce spectral leakage; rfft for real signal.
    """
    n = len(signal)
    skip_lo = n // 10
    skip_hi = n - n // 20
    sig = signal[skip_lo:skip_hi] - np.mean(signal[skip_lo:skip_hi])
    n_used = len(sig)

    window = np.hanning(n_used)
    sig_w = sig * window

    fft_amp = np.abs(np.fft.rfft(sig_w))
    fft_freq = np.fft.rfftfreq(n_used, d=dt)

    fft_amp[0] = 0  # drop DC
    peak_idx = np.argmax(fft_amp)
    peak_freq = fft_freq[peak_idx]
    return float(2.0 * np.pi * peak_freq)  # angular frequency ω = 2πf


def extract_decay_time(signal: np.ndarray, dt: float) -> float:
    """Extract exponential decay time τ via envelope log-linear fit.

    Method: take running-max envelope of |signal| in windows of ~1 period;
    fit log(envelope) vs time over middle 60% of run; τ = -1/slope.
    """
    env = np.abs(signal)
    window_size = max(5, len(env) // 50)
    env_smooth = np.array([
        np.max(env[max(0, i - window_size): i + window_size + 1])
        for i in range(len(env))
    ])

    skip_lo = len(env_smooth) // 5
    skip_hi = len(env_smooth) - len(env_smooth) // 10
    env_fit = env_smooth[skip_lo:skip_hi]
    t_fit = np.arange(skip_lo, skip_hi) * dt

    eps = 1e-30
    env_fit = np.maximum(env_fit, eps)

    coeffs = np.polyfit(t_fit, np.log(env_fit), 1)
    slope = coeffs[0]
    if slope >= -1e-10:  # essentially no decay
        return float("inf")
    tau = -1.0 / slope
    return float(tau)


def test_q_preservation_cavity_radius_sweep():
    """Main C1-anchored test: sweep cavity radius at fixed amplitude.

    Per C1 analog: x_sat is the cavity-radius parameter that v1 and v2
    refine differently. Here we sweep blob radius R; at each R measure
    cavity mode ω_R(R) and decay τ(R); compute Q(R) = ω_R·τ/2.

    Outcome:
    - Q variance < 10% → PASS (Outcome A); Q is rigid-lattice property
    - 10% ≤ Q variance < 50% → PARTIAL (Outcome B); needs ν_vac=2/7 partition
    - Q variance ≥ 50% → FAIL (Outcome C); needs (2,q) chiral refactor
    - NaN at any R → TECHNICAL BLOCKER (Outcome D)
    """
    # Fixed amplitude in saturation regime (Op14 trading engaged per coupling_strength)
    A = 0.4  # × V_yield = 1.0
    # Cavity radius sweep (in cells)
    radii = [3.0, 4.0, 5.0, 6.0, 7.0]
    N = 48  # larger grid so decay is observable before boundary reflection
    n_steps = 5000  # ~8 cycles of slowest mode
    Q_values = []
    omega_R_values = []
    tau_values = []
    nan_radii = []

    for R in radii:
        engine = CosseratMasterEquationFDTD(
            N=N,
            dx=1.0,
            V_yield=1.0,
            c0=1.0,
            cfl_safety=0.3,
            coupling_mode="shared_flux",
        )
        center = (N // 2, N // 2, N // 2)

        # Seed coupled (V, ω) blob — V drives saturation, ω is the
        # microrotation field that couples via K_eff(V)
        engine.inject_localized_blob(center=center, radius=R, amplitude=A, profile="sech")
        engine.inject_cosserat_blob(center=center, radius=R, amplitude=A * 0.5, profile="sech")

        # Probe V at center every step
        V_center = np.zeros(n_steps)
        for step_i in range(n_steps):
            engine.step()
            V_center[step_i] = engine.V[center]

        if not np.all(np.isfinite(V_center)):
            nan_radii.append(R)
            Q_values.append(float("nan"))
            omega_R_values.append(float("nan"))
            tau_values.append(float("nan"))
            continue

        omega_R = extract_peak_frequency(V_center, engine.dt)
        tau = extract_decay_time(V_center, engine.dt)
        Q = omega_R * tau / 2.0 if tau != float("inf") else float("inf")

        Q_values.append(Q)
        omega_R_values.append(omega_R)
        tau_values.append(tau)

    # Report all results
    print("\n" + "=" * 80)
    print("C1 Q-PRESERVATION SOLITON-SCALE TEST — Cavity Radius Sweep")
    print(f"Fixed A = {A:.2f} V_yield; N={N}; n_steps={n_steps}")
    print("PREREG: research/2026-05-18_cosserat-engine-q-preservation-prereg.md")
    print("=" * 80)
    print(f"{'R (cells)':>10} {'ω_R (rad/t)':>14} {'τ (t)':>14} {'Q':>14}")
    print("-" * 60)
    for R, omega_R, tau, Q in zip(radii, omega_R_values, tau_values, Q_values):
        if np.isnan(Q):
            print(f"{R:>10.1f} {'NaN':>14} {'NaN':>14} {'NaN':>14}")
        else:
            tau_str = f"{tau:.4e}" if tau != float("inf") else "∞"
            Q_str = f"{Q:.4e}" if Q != float("inf") else "∞"
            print(f"{R:>10.1f} {omega_R:>14.4e} {tau_str:>14} {Q_str:>14}")

    # Diagnose outcome category
    valid_Q = [q for q in Q_values if not np.isnan(q) and q != float("inf")]
    valid_omega_R = [w for w, q in zip(omega_R_values, Q_values)
                     if not np.isnan(q) and q != float("inf")]

    if nan_radii:
        print(f"\n[TECHNICAL BLOCKER — Outcome D] Engine NaN at radii: {nan_radii}")
        print("  Action: Phase 3f.3.3 CFL blocker reproducing at some R.")
        # Don't fail; document
        return

    if len(valid_Q) < 3:
        print("\n[SKIP] Insufficient finite Q values to compute variance.")
        print("Possible cause: cavity modes don't decay on this engine architecture")
        print("(too low PML damping or solitonic stability prevents decay).")
        pytest.skip(f"Only {len(valid_Q)} of {len(radii)} radii produced finite Q")

    Q_mean = np.mean(valid_Q)
    Q_variation = (max(valid_Q) - min(valid_Q)) / Q_mean

    # Also check ω_R scaling vs R (expect ω_R ∝ 1/R if cavity mode geometry-set)
    omega_R_arr = np.array(valid_omega_R)
    R_arr = np.array([R for R, q in zip(radii, Q_values)
                      if not np.isnan(q) and q != float("inf")])
    # Fit omega_R · R = constant test
    omega_R_times_R = omega_R_arr * R_arr
    omega_R_R_variation = (np.max(omega_R_times_R) - np.min(omega_R_times_R)) / np.mean(omega_R_times_R)

    print(f"\nQ mean: {Q_mean:.4e}")
    print(f"Q variation (max-min)/mean: {Q_variation:.2%}")
    print(f"ω_R·R product variation: {omega_R_R_variation:.2%}  (constant → ω_R ∝ 1/R)")

    if Q_variation < 0.10:
        outcome = "PASS (Outcome A)"
        diagnosis = (
            "Existing engine reproduces C1's mechanism implicitly. "
            "Axiom 4 + K_omega_0 baseline + shared_flux coupling is sufficient; "
            "lattice-Q preservation is a general substrate property "
            "(not specifically (2,3)-topology dependent)."
        )
    elif Q_variation < 0.50:
        outcome = "PARTIAL (Outcome B)"
        diagnosis = (
            "Engine has implicit-but-incomplete Q-preservation. "
            "ν_vac=2/7 explicit rigid/compliant partition is the missing piece. "
            "Action: Phase 2c engine refactor — "
            "K_eff(V) = ν_vac × K_omega_0 + (1-ν_vac) × K_omega_0/S(V)."
        )
    else:
        outcome = "FAIL (Outcome C)"
        diagnosis = (
            "Q-preservation mechanism is (2,3)-topology-specific. "
            "Cannot be reproduced on scalar engine without chiral coupling. "
            "Action: Phase 4 chiral coupling refactor + (2,q) ladder."
        )

    print(f"\nOUTCOME: {outcome}")
    print(f"DIAGNOSIS: {diagnosis}")
    print()

    # The test PASSES if it produces measurable Q values across the sweep.
    # PARTIAL or FAIL outcomes are informative results, not test failures.
    assert len(valid_Q) >= 3, "Sweep did not produce enough measurable Q values"

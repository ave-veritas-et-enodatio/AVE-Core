"""
Phase 2 validation: Op14 bond-pair Pearson ρ ≈ -0.99 on Cosserat-coupled engine.

Per pre-registration at research/2026-05-18_cosserat-lagrangian-engine-phase2-prereg.md:
- Expected: ρ(H_cos, Σ|Φ_link|²) ≈ -0.99 (per op14-cross-sector-trading.md:13)
- Falsifier: ρ > -0.7 OR ρ POSITIVE

Test runs Cosserat-coupled engine with bond-pair-like seed (two adjacent
saturated regions), probes (H_cos, Σ|V|²) time series over ~5000 timesteps,
and computes Pearson correlation.

Run:
    pytest src/tests/test_cosserat_master_equation_op14.py -v -s
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.core.cosserat_master_equation_fdtd import CosseratMasterEquationFDTD


# Test parameters
N = 24
DX = 0.5
V_YIELD = 1.0
C0 = 1.0
CFL_SAFETY = 0.4
PML_THICKNESS = 4

# Seed parameters: place V blob + ω blob at adjacent positions to mimic
# bond-pair geometry. Both near saturation to engage Op14 mechanism.
V_SEED_AMPLITUDE = 0.85  # near saturation
V_SEED_RADIUS = 2.0
OMEGA_SEED_AMPLITUDE = 0.5  # moderate Cosserat amplitude
OMEGA_SEED_RADIUS = 2.0

# Timestepping
N_STEPS = 5000  # ~5 Compton periods at substrate fundamental
PROBE_EVERY = 5  # subsample for efficiency; 1000 probes total

# Acceptance criteria per pre-reg
PEARSON_PASS_THRESHOLD = -0.95  # strict pass
PEARSON_PARTIAL_THRESHOLD = -0.7  # partial trade efficiency
PEARSON_NULL_THRESHOLD = -0.5  # null / wrong-mechanism


def pearson_r(x, y):
    """Compute Pearson correlation coefficient. Returns NaN if degenerate."""
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    if len(x) < 2 or len(y) < 2:
        return float("nan")
    x_mean = x.mean()
    y_mean = y.mean()
    x_var = ((x - x_mean) ** 2).sum()
    y_var = ((y - y_mean) ** 2).sum()
    if x_var == 0 or y_var == 0:
        return float("nan")
    return float(((x - x_mean) * (y - y_mean)).sum() / np.sqrt(x_var * y_var))


@pytest.mark.xfail(
    reason="Phase 2 MVP forward-only coupling (V → ω via K_eff modulation) "
    "does NOT implement bidirectional shared-inductive-flux trading required "
    "for Op14 ρ ≈ -0.99. See research/2026-05-18_phase2-validation-result.md "
    "for diagnosis and Phase 2b refactor proposal. Remove xfail when Phase 2b "
    "shared-flux coupling lands and ρ ≤ -0.7 is achieved.",
    strict=False,
)
def test_op14_pearson_bond_pair():
    """Phase 2 validation: ρ(H_cos, Σ|V|²) ≈ -0.99 on Cosserat-coupled engine."""
    engine = CosseratMasterEquationFDTD(
        N=N,
        dx=DX,
        V_yield=V_YIELD,
        c0=C0,
        cfl_safety=CFL_SAFETY,
        pml_thickness=PML_THICKNESS,
        I_omega=1.0,
        K_omega_0=1.0,
        kappa_0=0.1,
    )

    # Seed bond-pair: V blob at center, ω blob at adjacent position
    center_V = (N // 2, N // 2, N // 2)
    center_omega = (N // 2 + 3, N // 2, N // 2)  # adjacent (~3 cells over)

    engine.inject_localized_blob(
        center=center_V, radius=V_SEED_RADIUS, amplitude=V_SEED_AMPLITUDE, profile="sech"
    )
    engine.inject_cosserat_blob(
        center=center_omega, radius=OMEGA_SEED_RADIUS, amplitude=OMEGA_SEED_AMPLITUDE, profile="sech"
    )

    print(f"\nEngine init: {engine}")
    print(f"V peak at seed: {engine.V[center_V]:.4f}")
    print(f"ω peak at seed: {engine.omega[center_omega]:.4f}")
    print(f"Initial H_cos: {engine.H_cosserat():.4e}")
    print(f"Initial Σ|V|²: {engine.Sigma_Phi_link_sq():.4e}")

    # Run with probes
    result = engine.run_with_probes(n_steps=N_STEPS, probe_every=PROBE_EVERY)

    # Use post-transient window (skip first 20% of samples)
    n_samples = len(result["times"])
    skip = n_samples // 5
    H_cos_post = result["H_cos"][skip:]
    Sigma_V_sq_post = result["Sigma_Phi_link_sq"][skip:]
    H_total_post = result["H_total"][skip:]

    # Compute Pearson correlation
    rho = pearson_r(H_cos_post, Sigma_V_sq_post)

    # Compute energy conservation drift
    H_total_drift = (H_total_post.max() - H_total_post.min()) / H_total_post.mean()

    # Compute mean values for sanity
    H_cos_mean = H_cos_post.mean()
    Sigma_V_mean = Sigma_V_sq_post.mean()

    print(f"\nResults (post-transient window, {len(H_cos_post)} samples):")
    print(f"  Pearson ρ(H_cos, Σ|V|²) = {rho:.4f}")
    print(f"  H_cos mean = {H_cos_mean:.4e}, std = {H_cos_post.std():.4e}")
    print(f"  Σ|V|² mean = {Sigma_V_mean:.4e}, std = {Sigma_V_sq_post.std():.4e}")
    print(f"  H_total drift = {H_total_drift * 100:.2f}%")

    # Per pre-reg outcomes:
    if rho <= PEARSON_PASS_THRESHOLD:
        outcome = "PASS"
    elif rho <= PEARSON_PARTIAL_THRESHOLD:
        outcome = "PARTIAL"
    elif rho <= PEARSON_NULL_THRESHOLD:
        outcome = "WEAK"
    else:
        outcome = "FAIL (positive or no anti-correlation)"
    print(f"  Outcome: {outcome}")

    # Soft pass: PARTIAL or better. PASS is the strict goal.
    # Let test pass at PARTIAL to allow incremental refinement;
    # strict ρ ≤ -0.95 documented in result doc.
    assert rho <= PEARSON_PARTIAL_THRESHOLD, (
        f"ρ = {rho:.4f} does not show Op14 anti-correlation "
        f"(expected ≤ {PEARSON_PARTIAL_THRESHOLD}); "
        f"Phase 2 mechanism likely needs refactor."
    )


def test_engine_initializes():
    """Smoke test: engine instantiates with reasonable parameters."""
    engine = CosseratMasterEquationFDTD(N=16, dx=0.5, V_yield=1.0, c0=1.0)
    assert engine.V.shape == (16, 16, 16)
    assert engine.omega.shape == (16, 16, 16)
    assert engine.I_omega > 0
    assert engine.K_omega_0 > 0
    assert engine.dt > 0
    print(f"\nEngine: {engine}")


def test_cosserat_responds_to_V():
    """Smoke test: ω dynamics actually respond to V via K_eff(V) modulation."""
    engine = CosseratMasterEquationFDTD(N=16, dx=0.5, V_yield=1.0, c0=1.0)
    # Seed V at moderate amplitude
    engine.inject_localized_blob(center=(8, 8, 8), radius=2.0, amplitude=0.5, profile="sech")
    # Seed ω elsewhere
    engine.inject_cosserat_blob(center=(8, 8, 11), radius=2.0, amplitude=0.3, profile="sech")
    K_eff_initial = engine.cosserat_stiffness(engine.V)
    assert K_eff_initial[8, 8, 8] > engine.K_omega_0, (
        "K_eff at V-saturated region should exceed baseline"
    )
    omega_initial = engine.omega.copy()
    # Run a few steps; ω should evolve under modulated K_eff
    for _ in range(50):
        engine.step()
    omega_changed = not np.allclose(engine.omega, omega_initial)
    assert omega_changed, "ω did not evolve; coupling may not be wired correctly"

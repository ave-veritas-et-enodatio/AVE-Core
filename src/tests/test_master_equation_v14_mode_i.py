"""
Regression test: v14 Mode I PASS on Master Equation FDTD breathing soliton.

Locks in the empirical canonical state from doc 113 (v14 Mode I closure,
commit 345d55d 2026-05-14): the Master Equation FDTD engine hosts a stable
breathing-soliton bound state on the K4 substrate.

Per closure-roadmap.md Tier 1: prevents future engine regressions from
breaking the bound-state hosting that took the Path B engine refactor
to achieve.

Run:
    pytest src/tests/test_master_equation_v14_mode_i.py -v

Acceptance criteria (breathing-soliton appropriate, NOT strict stationary):
  - V_peak mean over post-transient window > 0.2  (bound state persists)
  - V_peak std / V_peak mean > 0.05  (genuinely breathing, not damped)
  - V_peak std / V_peak mean < 0.5   (not catastrophically diverging)
  - n_refractive at boundary measurably > 1.0  (saturation engaged)
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.core.master_equation_fdtd import MasterEquationFDTD


# Test parameters — v14 canonical seed per doc 113 §3
N = 24  # lattice size (small for fast test; v14 canonical uses N=24-32)
DX = 0.5
V_YIELD = 1.0
C0 = 1.0
CFL_SAFETY = 0.4
PML_THICKNESS = 4
SEED_PROFILE = "sech"
SEED_AMPLITUDE = 0.85  # close to A=1 to engage saturation
SEED_RADIUS = 2.5

# Run window: post-transient steady state
N_STEPS_TOTAL = 600
N_STEPS_TRANSIENT = 200  # skip initial transient
N_STEPS_RECORD = N_STEPS_TOTAL - N_STEPS_TRANSIENT


@pytest.fixture(scope="module")
def v14_run_result():
    """Run the v14 canonical configuration once; share across assertions."""
    engine = MasterEquationFDTD(
        N=N,
        dx=DX,
        V_yield=V_YIELD,
        c0=C0,
        cfl_safety=CFL_SAFETY,
        pml_thickness=PML_THICKNESS,
    )

    # Seed: sech profile centered, amplitude 0.85 (saturation engaged)
    center = N // 2
    coords = np.arange(N) - center
    X, Y, Z = np.meshgrid(coords, coords, coords, indexing="ij")
    r = np.sqrt(X**2 + Y**2 + Z**2) * DX
    seed = SEED_AMPLITUDE * (1.0 / np.cosh(r / SEED_RADIUS))
    engine.V[:] = seed
    engine.V_prev[:] = seed.copy()

    # Run + record V_peak and n_refractive_min per step in post-transient window
    # Engine convention: refractive_index() = S^(1/4), goes from 1 (A=0) → 0 (A=1).
    # MIN of n_eff over the lattice captures the deepest saturation point (soliton core).
    v_peak_history = []
    n_refractive_min_history = []
    for step in range(N_STEPS_TOTAL):
        engine.step()
        if step >= N_STEPS_TRANSIENT:
            v_peak_history.append(float(np.abs(engine.V).max()))
            n_refractive_min_history.append(float(engine.refractive_index().min()))

    v_peak = np.array(v_peak_history)
    n_refractive_min = np.array(n_refractive_min_history)
    return {
        "engine": engine,
        "v_peak_history": v_peak,
        "v_peak_mean": v_peak.mean(),
        "v_peak_std": v_peak.std(),
        "v_peak_std_over_mean": v_peak.std() / max(v_peak.mean(), 1e-9),
        "n_refractive_min_over_window": float(n_refractive_min.min()),
    }


def test_v14_mode_i_v_peak_mean_above_threshold(v14_run_result):
    """V_peak mean > 0.2 → bound state persists (doesn't decay to zero)."""
    assert v14_run_result["v_peak_mean"] > 0.2, (
        f"V_peak mean = {v14_run_result['v_peak_mean']:.4f}, "
        "expected > 0.2 for persistent bound state."
    )


def test_v14_mode_i_breathing_signature(v14_run_result):
    """V_peak std/mean > 0.05 → genuine breathing oscillation, not damped."""
    assert v14_run_result["v_peak_std_over_mean"] > 0.05, (
        f"V_peak std/mean = {v14_run_result['v_peak_std_over_mean']:.4f}, "
        "expected > 0.05 for breathing-soliton oscillation."
    )


def test_v14_mode_i_not_diverging(v14_run_result):
    """V_peak std/mean < 0.5 → bound, not catastrophic divergence."""
    assert v14_run_result["v_peak_std_over_mean"] < 0.5, (
        f"V_peak std/mean = {v14_run_result['v_peak_std_over_mean']:.4f}, "
        "exceeds 0.5 — soliton may be diverging instead of breathing."
    )


def test_v14_mode_i_saturation_engaged(v14_run_result):
    """min n_eff = S^(1/4) over recorded window < 0.97 → saturation kernel is engaged at soliton core.

    Engine convention: refractive_index() = S(A)^(1/4) = (1 - A²)^(1/4)/sqrt — goes from 1.0 (no
    saturation, A=0) toward 0.0 (full saturation, A→1). MIN over the lattice captures the deepest
    saturation point (soliton core). For v14 canonical seed amplitude 0.85 with breathing
    dynamics settling to A ≈ 0.5-0.7 at core, expect min n_eff ≈ (1-0.5²)^(1/4) ≈ 0.93.
    """
    assert v14_run_result["n_refractive_min_over_window"] < 0.97, (
        f"min n_refractive over window = {v14_run_result['n_refractive_min_over_window']:.4f}, "
        "expected < 0.97 for saturation engagement at soliton core."
    )


def test_v14_mode_i_doc_113_canonical_state():
    """Smoke test: engine instantiates with canonical v14 parameters."""
    engine = MasterEquationFDTD(
        N=N, dx=DX, V_yield=V_YIELD, c0=C0, cfl_safety=CFL_SAFETY, pml_thickness=PML_THICKNESS
    )
    assert engine.V.shape == (N, N, N), f"Unexpected shape: {engine.V.shape}"
    assert engine.dt > 0, "dt must be positive"
    # CFL condition: dt < dx / (c * sqrt(3)) for 3D leapfrog
    cfl_limit = DX / (C0 * np.sqrt(3.0))
    assert engine.dt < cfl_limit, (
        f"dt={engine.dt:.6f} violates CFL limit {cfl_limit:.6f}"
    )

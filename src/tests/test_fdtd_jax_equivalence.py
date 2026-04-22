#!/usr/bin/env python3
"""
Verification: FDTD3DEngine (numpy) vs FDTD3DEngineJAX (JAX)
============================================================

Runs both engines side-by-side for a small test case and verifies
that field values match within floating-point tolerance.

This proves the JAX port is a faithful 1:1 translation of the
physics — every axiom-derived constant, every nonlinear saturation
curve, every curl stencil is numerically identical.
"""

import time

import numpy as np

from ave.core.fdtd_3d import FDTD3DEngine
from ave.core.fdtd_3d_jax import FDTD3DEngineJAX


def test_equivalence(nx=20, ny=20, nz=20, n_steps=50, linear_only=False, use_pml=False):
    """Compare numpy and JAX engines for n_steps with a point source."""
    label = f"{'linear' if linear_only else 'nonlinear'}, {'PML' if use_pml else 'Mur'}"
    print(f"\n  Test: {label}  ({nx}×{ny}×{nz}, {n_steps} steps)")

    # Numpy engine
    eng_np = FDTD3DEngine(nx, ny, nz, dx=0.01, linear_only=linear_only, use_pml=use_pml)

    # JAX engine
    eng_jax = FDTD3DEngineJAX(nx, ny, nz, dx=0.01, linear_only=linear_only, use_pml=use_pml)

    # Source: sinusoidal point source at center
    cx, cy, cz = nx // 2, ny // 2, nz // 2
    freq = 150e6

    t0 = time.time()
    for step in range(n_steps):
        t = eng_np.dt * step
        signal = np.sin(2 * np.pi * freq * t) * 100.0

        eng_np.inject_soft_source("Ez", cx, cy, cz, signal)
        eng_np.step()

        eng_jax.inject_soft_source("Ez", cx, cy, cz, signal)
        eng_jax.step()
    dt_total = time.time() - t0

    # Compare fields
    jax_fields = eng_jax.to_numpy()
    max_diffs = {}
    for name in ["Ex", "Ey", "Ez", "Hx", "Hy", "Hz"]:
        np_field = getattr(eng_np, name)
        jax_field = jax_fields[name]
        max_diff = np.max(np.abs(np_field - jax_field))
        # Use RMS of the field as denominator to avoid inflated relative
        # errors near zero-crossings where max(|field|) is tiny
        rms = np.sqrt(np.mean(np_field**2)) + 1e-30
        rel_diff = max_diff / rms
        max_diffs[name] = (max_diff, rel_diff)

    # Compare energy
    energy_np = eng_np.total_field_energy()
    energy_jax = eng_jax.total_field_energy()
    energy_diff = abs(energy_np - energy_jax) / (energy_np + 1e-30)

    # Print results
    all_pass = True
    for name, (abs_diff, rel_diff) in max_diffs.items():
        status = "✓" if rel_diff < 1e-4 else "✗"
        if rel_diff >= 1e-4:
            all_pass = False
        print(f"    {name}: max|Δ| = {abs_diff:.2e}, rel = {rel_diff:.2e}  {status}")

    energy_status = "✓" if energy_diff < 1e-4 else "✗"
    if energy_diff >= 1e-4:
        all_pass = False
    print(f"    Energy: numpy={energy_np:.6e}, jax={energy_jax:.6e}, rel_diff={energy_diff:.2e}  {energy_status}")
    print(f"    Time: {dt_total:.2f}s  {'PASS' if all_pass else 'FAIL'}")

    assert all_pass, f"JAX/numpy mismatch in {label}"


def main():
    print("=" * 60)
    print("  FDTD3DEngine: numpy vs JAX Numerical Equivalence Test")
    print("=" * 60)

    results = []

    # Test 1: Linear mode + Mur ABC
    results.append(test_equivalence(linear_only=True, use_pml=False))

    # Test 2: Nonlinear mode + Mur ABC (Axiom 4 saturation)
    results.append(test_equivalence(linear_only=False, use_pml=False))

    # Test 3: Linear mode + PML
    results.append(test_equivalence(linear_only=True, use_pml=True))

    # Test 4: Nonlinear mode + PML
    results.append(test_equivalence(linear_only=False, use_pml=True))

    print(f"\n{'=' * 60}")
    if all(results):
        print("  ALL TESTS PASSED — JAX port is numerically equivalent")
    else:
        print("  SOME TESTS FAILED — investigate discrepancies")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()

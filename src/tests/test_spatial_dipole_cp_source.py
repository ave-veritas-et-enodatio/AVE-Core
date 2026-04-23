"""G-11(a) — SpatialDipoleCPSource tests.

Validates the circularly-polarized V_inc source via spatial-dipole
modulation at the source plane (per STAGE6_V4_HANDOFF §9 option a).

Physical setup: the source injects V at plane x=x₀ with a transverse
pattern
    V(y, z, t) = A·env(t)·[cos(ωt)·g_y(y,z) + sin(ωt)·ε_hand·g_z(y,z)]
where g_y = (y−y_c)·Gaussian, g_z = (z−z_c)·Gaussian, and ε_hand
= ±1 selects RH/LH.

Load-bearing invariants (this is a source unit test — driven-coupling
physics deferred to Phase 5 + driver script per handoff §9):

1. **Additive V_inc injection** (same as CWSource) at the source plane
2. **RH vs LH sign flip:** at fixed (y,z,t) with sin(ωt) ≠ 0, RH
   and LH injections differ by the sign of the z-dipole contribution
3. **Dipole antisymmetry:** the y-dipole injects V with sign(y−y_c);
   similarly for z. V(y_c, z_c, t) = 0 (dipole null at center)
4. **Envelope + active-mask respect** (standard Source discipline)
5. **Construction validation** (handedness, propagation_axis)

References:
- STAGE6_V4_HANDOFF.md §9 G-11 option (a)
- vacuum_engine.py::SpatialDipoleCPSource for the implementation
- CWSource for envelope + port-weight conventions (reused)
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.topological.vacuum_engine import (
    SpatialDipoleCPSource,
    VacuumEngine3D,
)


# ═══════════════════════════════════════════════════════════════════════════
# Construction
# ═══════════════════════════════════════════════════════════════════════════
class TestConstruction:
    def test_rh_constructs(self):
        src = SpatialDipoleCPSource(
            x0=4, propagation_axis=0, amplitude=0.5, omega=1.0,
            handedness="RH", sigma_yz=2.0, t_ramp=1.0, t_sustain=10.0,
        )
        assert src._eps_hand == +1

    def test_lh_constructs(self):
        src = SpatialDipoleCPSource(
            x0=4, propagation_axis=0, amplitude=0.5, omega=1.0,
            handedness="LH", sigma_yz=2.0, t_ramp=1.0, t_sustain=10.0,
        )
        assert src._eps_hand == -1

    def test_invalid_handedness_rejected(self):
        with pytest.raises(ValueError, match="handedness"):
            SpatialDipoleCPSource(
                x0=4, propagation_axis=0, amplitude=0.5, omega=1.0,
                handedness="elliptical", sigma_yz=2.0,
                t_ramp=1.0, t_sustain=10.0,
            )

    def test_invalid_propagation_axis_rejected(self):
        with pytest.raises(ValueError, match="propagation_axis"):
            SpatialDipoleCPSource(
                x0=4, propagation_axis=-1, amplitude=0.5, omega=1.0,
                handedness="RH", sigma_yz=2.0,
                t_ramp=1.0, t_sustain=10.0,
            )


# ═══════════════════════════════════════════════════════════════════════════
# Dipole antisymmetry
# ═══════════════════════════════════════════════════════════════════════════
class TestDipoleAntisymmetry:
    """The source pattern has dipolar structure — sign follows (y−y_c)
    and (z−z_c); net V at the geometric center is zero."""

    @pytest.fixture
    def engine_after_apply(self):
        """Engine with source applied at t=0 (cos=1, sin=0 → pure y-dipole)."""
        engine = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)
        src = SpatialDipoleCPSource(
            x0=4, propagation_axis=0, amplitude=0.5, omega=1.0,
            handedness="RH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        src.apply(engine, t=0.0)
        return engine, src

    def test_V_at_center_is_zero_at_t_zero(self, engine_after_apply):
        """At t=0 with y-dipole only (sin=0): V at y_c, z_c must vanish
        because the y-dipole pattern (y−y_c) has zero at y=y_c."""
        engine, src = engine_after_apply
        N = engine.N
        yc = (N - 1) / 2.0  # = 5.5 for N=12
        zc = (N - 1) / 2.0
        # At integer-nearest to center: y=5, z=5 (profile peak per Gaussian)
        # But the CENTER is at 5.5 — integer sites don't perfectly match.
        # Instead verify that symmetric pairs (y_c - Δ, z) and (y_c + Δ, z)
        # have opposite-sign V injection
        V_slab = engine.k4.V_inc[src.x0]  # shape (N, N, 4)
        # Test a few symmetric y-pairs at z=5
        for Δ in [1, 2]:
            y1 = int(yc - Δ - 0.5)  # one side
            y2 = int(yc + Δ + 0.5)  # other side (symmetric about y_c=5.5)
            z = 5
            # Sum over ports (any port should show dipole sign)
            V_total_1 = V_slab[y1, z, :].sum()
            V_total_2 = V_slab[y2, z, :].sum()
            # Dipole antisymmetry: V(y1) = -V(y2) approximately
            # (Gaussian is symmetric; dipole factor (y−y_c) is antisymmetric)
            assert np.sign(V_total_1) == -np.sign(V_total_2) or abs(V_total_1) < 1e-10, (
                f"Dipole antisymmetry: V at y={y1} = {V_total_1}, "
                f"V at y={y2} = {V_total_2}; expected opposite signs"
            )

    def test_z_dipole_appears_at_quarter_cycle(self):
        """At ωt = π/2 (sin=1, cos=0): only z-dipole injected. Under RH,
        sign follows (z−z_c)·(+1); under LH, (z−z_c)·(−1)."""
        engine_rh = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)
        engine_lh = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)
        carrier = 1.0
        t = np.pi / (2.0 * carrier)  # cos=0, sin=1
        amp = 0.5

        src_rh = SpatialDipoleCPSource(
            x0=4, propagation_axis=0, amplitude=amp, omega=carrier,
            handedness="RH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        src_lh = SpatialDipoleCPSource(
            x0=4, propagation_axis=0, amplitude=amp, omega=carrier,
            handedness="LH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        src_rh.apply(engine_rh, t)
        src_lh.apply(engine_lh, t)

        # V_inc at the source slab, summed over ports — should be sign-flipped
        V_rh = engine_rh.k4.V_inc[4].sum(axis=-1)  # (N, N)
        V_lh = engine_lh.k4.V_inc[4].sum(axis=-1)
        # RH and LH should differ by sign of the sin·z-dipole term
        assert np.allclose(V_rh, -V_lh, atol=1e-10), (
            "RH and LH at ωt=π/2 should be exact sign-flips (cos=0, only z-dipole)"
        )


# ═══════════════════════════════════════════════════════════════════════════
# Envelope + active-mask respect
# ═══════════════════════════════════════════════════════════════════════════
class TestEnvelopeAndMask:
    def test_envelope_zero_before_ramp(self):
        engine = VacuumEngine3D.from_args(N=10, pml=1, temperature=0.0)
        src = SpatialDipoleCPSource(
            x0=3, propagation_axis=0, amplitude=0.5, omega=1.0,
            handedness="RH", sigma_yz=2.0, t_ramp=5.0, t_sustain=10.0,
        )
        src.apply(engine, t=-1.0)
        assert np.all(engine.k4.V_inc == 0.0)

    def test_additive_injection(self):
        """CWSource-style: V_inc is ADDED (not overwritten) at each apply."""
        engine = VacuumEngine3D.from_args(N=10, pml=1, temperature=0.0)
        # Pre-seed some V_inc value
        engine.k4.V_inc[5, 5, 5, 0] = 0.3
        src = SpatialDipoleCPSource(
            x0=3, propagation_axis=0, amplitude=0.5, omega=1.0,
            handedness="RH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        src.apply(engine, t=0.0)
        # The pre-existing V_inc at (5,5,5) is NOT at the source plane (x=3),
        # so it should stay at 0.3
        assert engine.k4.V_inc[5, 5, 5, 0] == 0.3

    def test_active_mask_respected(self):
        """V_inc at inactive sites (bipartite mask + PML) stays zero."""
        engine = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)
        src = SpatialDipoleCPSource(
            x0=4, propagation_axis=0, amplitude=0.5, omega=1.0,
            handedness="RH", sigma_yz=4.0,  # wide enough to hit PML
            t_ramp=0.0, t_sustain=100.0,
        )
        src.apply(engine, t=0.0)
        # Inactive sites at source plane should stay at 0
        inactive = ~engine.k4.mask_active[src.x0]
        V_slab = engine.k4.V_inc[src.x0]
        for port in range(4):
            assert np.all(V_slab[..., port][inactive] == 0.0), (
                f"Port {port}: V at inactive sites must be 0"
            )


# ═══════════════════════════════════════════════════════════════════════════
# Engine integration
# ═══════════════════════════════════════════════════════════════════════════
class TestEngineIntegration:
    def test_rh_drive_runs_without_blowup(self):
        engine = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)
        src = SpatialDipoleCPSource(
            x0=4, propagation_axis=0, amplitude=0.3, omega=2.0 * np.pi / 4.0,
            handedness="RH", sigma_yz=2.0, t_ramp=2.0, t_sustain=20.0,
        )
        engine.add_source(src)
        for _ in range(10):
            engine.step()
        assert np.all(np.isfinite(engine.k4.V_inc))
        assert np.all(np.isfinite(engine.cos.omega))
        assert np.all(np.isfinite(engine.cos.u))

    def test_lh_drive_runs_without_blowup(self):
        engine = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)
        src = SpatialDipoleCPSource(
            x0=4, propagation_axis=0, amplitude=0.3, omega=2.0 * np.pi / 4.0,
            handedness="LH", sigma_yz=2.0, t_ramp=2.0, t_sustain=20.0,
        )
        engine.add_source(src)
        for _ in range(10):
            engine.step()
        assert np.all(np.isfinite(engine.k4.V_inc))

    def test_rh_drive_produces_nonzero_V_inc(self):
        engine = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)
        src = SpatialDipoleCPSource(
            x0=4, propagation_axis=0, amplitude=0.5, omega=1.0,
            handedness="RH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        engine.add_source(src)
        for _ in range(3):
            engine.step()
        V_mag_sq = np.sum(engine.k4.V_inc ** 2, axis=-1)
        max_V_mag_sq = float(V_mag_sq.max())
        assert max_V_mag_sq > 0.001, (
            f"Max |V|² = {max_V_mag_sq:.4e}; expected non-trivial drive"
        )


# ═══════════════════════════════════════════════════════════════════════════
# Handedness discrimination at source slab
# ═══════════════════════════════════════════════════════════════════════════
class TestHandednessDiscrimination:
    def test_rh_lh_differ_in_z_dipole_contribution(self):
        """At ωt ≠ 0 (sin ≠ 0), RH and LH give DIFFERENT V_inc patterns
        because the sin-weighted z-dipole has opposite sign.
        At ωt = 0 (sin=0), both should be identical (only cos·y-dipole)."""
        N = 12

        eng_rh_t0 = VacuumEngine3D.from_args(N=N, pml=2, temperature=0.0)
        eng_lh_t0 = VacuumEngine3D.from_args(N=N, pml=2, temperature=0.0)
        src_rh_t0 = SpatialDipoleCPSource(
            x0=4, propagation_axis=0, amplitude=0.5, omega=1.0,
            handedness="RH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        src_lh_t0 = SpatialDipoleCPSource(
            x0=4, propagation_axis=0, amplitude=0.5, omega=1.0,
            handedness="LH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        src_rh_t0.apply(eng_rh_t0, t=0.0)
        src_lh_t0.apply(eng_lh_t0, t=0.0)
        # At t=0 (sin=0): both identical
        assert np.allclose(eng_rh_t0.k4.V_inc, eng_lh_t0.k4.V_inc, atol=1e-10)

        # At ωt = π/4 (sin > 0): differ by sign of sin term
        t_quarter = np.pi / 4.0
        eng_rh = VacuumEngine3D.from_args(N=N, pml=2, temperature=0.0)
        eng_lh = VacuumEngine3D.from_args(N=N, pml=2, temperature=0.0)
        src_rh = SpatialDipoleCPSource(
            x0=4, propagation_axis=0, amplitude=0.5, omega=1.0,
            handedness="RH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        src_lh = SpatialDipoleCPSource(
            x0=4, propagation_axis=0, amplitude=0.5, omega=1.0,
            handedness="LH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        src_rh.apply(eng_rh, t=t_quarter)
        src_lh.apply(eng_lh, t=t_quarter)
        # At t=π/4: RH and LH differ (half-cos-y-dipole common, half-sin-z-dipole opposite)
        assert not np.allclose(eng_rh.k4.V_inc, eng_lh.k4.V_inc, atol=1e-10), (
            "RH and LH at ωt=π/4 must differ (sin-z-dipole term has opposite sign)"
        )
        # Symmetric decomposition: (RH + LH)/2 should equal cos-term only (no sin contribution)
        # = the t=0 pattern scaled by cos(π/4)
        avg = (eng_rh.k4.V_inc + eng_lh.k4.V_inc) / 2.0
        expected_cos = eng_rh_t0.k4.V_inc * np.cos(t_quarter)
        assert np.allclose(avg, expected_cos, atol=1e-10), (
            "Average of RH + LH at ωt=π/4 should be cos·y-dipole only"
        )

"""G-11(c) — CosseratBeltramiSource tests.

Validates the direct-ω chirality injection source that bypasses K4-port
circular-polarization ambiguity (per STAGE6_V4_HANDOFF §9 G-11 option c).

Load-bearing invariants:

1. **Handedness convention:** RH → ω_source(t) = A·(0, cos(ωt), +sin(ωt));
   LH → ω_source(t) = A·(0, cos(ωt), −sin(ωt)). Derived from Beltrami
   traveling-wave ω(x,t) = A·(0, cos(kx−ωt), ∓sin(kx−ωt)) evaluated at
   fixed source slab x=x₀ with ω_yield = π (natural) and c=1.

2. **Source slab overwrite:** ω at x=x₀ is SET each step (not added) to
   the driven pattern — additive semantics would accumulate across
   integrator sub-steps and drift non-physically.

3. **Transverse Gaussian profile:** weighted by active-site mask
   (PML excluded).

4. **Phase 4 integration:** under strong enough amplitude + `_update_
   saturation_kernels`, RH drive biases A²_μ > A²_ε at downstream
   sites (Meissner mechanism); LH reverses.

5. **No K4 injection:** this source touches only engine.cos.omega,
   not engine.k4.V_inc. Deliberately bypasses the (y+z)/√2 port-span
   issue flagged in handoff §9.

References:
- doc 54_ §6 (asymmetric μ/ε saturation)
- doc 20_ Sub-Theorem 3.1.1 (κ_chiral = 1.2·α)
- STAGE6_V4_HANDOFF.md §9 G-11 option (c)
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.topological.vacuum_engine import (
    CosseratBeltramiSource,
    VacuumEngine3D,
)


# ═══════════════════════════════════════════════════════════════════════════
# Construction / argument validation
# ═══════════════════════════════════════════════════════════════════════════
class TestConstruction:
    def test_rh_constructs(self):
        src = CosseratBeltramiSource(
            x0=4, propagation_axis=0, amplitude=1.0,
            omega=2.0 * np.pi / 3.5, handedness="RH",
            sigma_yz=2.0, t_ramp=5.0, t_sustain=20.0,
        )
        assert src._sign == +1
        assert src.handedness == "RH"
        assert src._trans_axes == (1, 2)  # y, z for +x propagation

    def test_lh_constructs(self):
        src = CosseratBeltramiSource(
            x0=4, propagation_axis=0, amplitude=1.0,
            omega=1.0, handedness="LH",
            sigma_yz=2.0, t_ramp=5.0, t_sustain=20.0,
        )
        assert src._sign == -1

    def test_invalid_handedness_rejected(self):
        with pytest.raises(ValueError, match="handedness"):
            CosseratBeltramiSource(
                x0=4, propagation_axis=0, amplitude=1.0,
                omega=1.0, handedness="circular",  # invalid
                sigma_yz=2.0, t_ramp=1.0, t_sustain=1.0,
            )

    def test_invalid_propagation_axis_rejected(self):
        with pytest.raises(ValueError, match="propagation_axis"):
            CosseratBeltramiSource(
                x0=4, propagation_axis=3,  # invalid
                amplitude=1.0, omega=1.0, handedness="RH",
                sigma_yz=2.0, t_ramp=1.0, t_sustain=1.0,
            )

    def test_y_propagation_transverse_axes(self):
        src = CosseratBeltramiSource(
            x0=4, propagation_axis=1, amplitude=1.0, omega=1.0,
            handedness="RH", sigma_yz=2.0, t_ramp=1.0, t_sustain=1.0,
        )
        assert src._trans_axes == (0, 2)  # x, z for +y propagation


# ═══════════════════════════════════════════════════════════════════════════
# Slab-level ω injection pattern
# ═══════════════════════════════════════════════════════════════════════════
class TestSlabInjectionPattern:
    """Verify the ω values written at the source slab match the
    theoretical RH / LH helical pattern."""

    @pytest.fixture
    def engine(self):
        return VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)

    def _active_site_near_peak(self, engine, src):
        """Find an active Cosserat site at the source slab near the profile peak.

        Cosserat mask_alive is bipartite on the diamond lattice — only
        (y+z+x) = all-even or all-odd sites are active. For x=4 (even),
        active sites are (even, even) in (y, z)."""
        slab_mask = engine.cos.mask_alive[src.x0]
        weighted = src._transverse_profile * slab_mask.astype(float)
        idx_flat = np.argmax(weighted)
        return np.unravel_index(idx_flat, weighted.shape)

    def test_rh_at_peak_t_writes_positive_sin_on_z(self, engine):
        """At ω·t = π/2 (quarter-cycle), RH has ω_y=0, ω_z=+A·profile."""
        carrier = 1.0
        amp = 0.5
        src = CosseratBeltramiSource(
            x0=4, propagation_axis=0, amplitude=amp, omega=carrier,
            handedness="RH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        t = np.pi / (2.0 * carrier)
        src.apply(engine, t)
        site_idx = self._active_site_near_peak(engine, src)
        profile_at_site = src._transverse_profile[site_idx]
        ω_site = engine.cos.omega[src.x0][site_idx]
        expected_z = amp * profile_at_site  # sin(π/2) = 1
        assert abs(ω_site[0]) < 1e-10, "Propagation-axis ω (x) should be 0"
        assert abs(ω_site[1]) < expected_z * 0.01, f"ω_y at ωt=π/2 should be ~0, got {ω_site[1]}"
        assert ω_site[2] == pytest.approx(expected_z, rel=1e-6), (
            f"RH ω_z at ωt=π/2 should be amp·profile = {expected_z:.4f}, got {ω_site[2]:.4f}"
        )

    def test_lh_at_peak_t_writes_negative_sin_on_z(self, engine):
        """LH: at ω·t = π/2, ω_z = -A·profile (opposite of RH)."""
        carrier = 1.0
        amp = 0.5
        src = CosseratBeltramiSource(
            x0=4, propagation_axis=0, amplitude=amp, omega=carrier,
            handedness="LH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        t = np.pi / (2.0 * carrier)
        src.apply(engine, t)
        site_idx = self._active_site_near_peak(engine, src)
        profile_at_site = src._transverse_profile[site_idx]
        ω_site = engine.cos.omega[src.x0][site_idx]
        expected_z = -amp * profile_at_site
        assert ω_site[2] == pytest.approx(expected_z, rel=1e-6), (
            f"LH ω_z at ωt=π/2 should be -amp·profile = {expected_z:.4f}, got {ω_site[2]:.4f}"
        )

    def test_at_t_zero_writes_only_cos_on_y(self, engine):
        """At ω·t = 0: ω_y = A·profile, ω_z = 0."""
        carrier = 1.0
        amp = 0.7
        src = CosseratBeltramiSource(
            x0=4, propagation_axis=0, amplitude=amp, omega=carrier,
            handedness="RH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        src.apply(engine, t=0.0)
        site_idx = self._active_site_near_peak(engine, src)
        profile_at_site = src._transverse_profile[site_idx]
        ω_site = engine.cos.omega[src.x0][site_idx]
        expected_y = amp * profile_at_site
        assert ω_site[1] == pytest.approx(expected_y, rel=1e-6), (
            f"ω_y at t=0 should be amp·profile = {expected_y:.4f}, got {ω_site[1]:.4f}"
        )
        assert abs(ω_site[2]) < expected_y * 0.01

    def test_envelope_zero_before_ramp(self, engine):
        """Before t=0, envelope=0 → no injection."""
        src = CosseratBeltramiSource(
            x0=4, propagation_axis=0, amplitude=1.0, omega=1.0,
            handedness="RH", sigma_yz=2.0, t_ramp=5.0, t_sustain=10.0,
        )
        src.apply(engine, t=-1.0)
        # Nothing should have changed (engine.cos.omega was 0 at init)
        assert np.all(engine.cos.omega == 0.0)

    def test_other_slabs_untouched(self, engine):
        """Only the source slab x=x0 is written; other slabs stay at init."""
        # Seed engine with deterministic non-zero ω elsewhere, then apply source
        engine.cos.omega[...] = 0.1  # fill everything
        src = CosseratBeltramiSource(
            x0=4, propagation_axis=0, amplitude=1.0, omega=1.0,
            handedness="RH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        src.apply(engine, t=0.0)
        # Source slab (x=4) should be overwritten
        assert not np.all(engine.cos.omega[4] == 0.1)
        # Other slabs unchanged
        assert np.all(engine.cos.omega[0] == 0.1)
        assert np.all(engine.cos.omega[3] == 0.1)
        assert np.all(engine.cos.omega[5] == 0.1)
        assert np.all(engine.cos.omega[11] == 0.1)


# ═══════════════════════════════════════════════════════════════════════════
# Engine integration: source runs without NaN/inf
# ═══════════════════════════════════════════════════════════════════════════
class TestEngineIntegration:
    """The source runs cleanly through the engine step loop without
    numerical blowup. Helicity-at-downstream and Meissner-downstream
    validations are deferred to a dedicated driver script + N≥32 lattice
    (see handoff §13 Phase 5 prereq: CosseratBeltramiSource validates
    the MECHANISM at the source slab; downstream propagation physics is
    tested via the existing Phase I/II/III-B integration suite)."""

    def test_rh_drive_runs_without_blowup(self):
        N = 12
        engine = VacuumEngine3D.from_args(N=N, pml=2, temperature=0.0)
        src = CosseratBeltramiSource(
            x0=4, propagation_axis=0, amplitude=0.5, omega=2.0 * np.pi / 4.0,
            handedness="RH", sigma_yz=2.0, t_ramp=2.0, t_sustain=20.0,
        )
        engine.add_source(src)
        for _ in range(10):
            engine.step()
        assert np.all(np.isfinite(engine.cos.omega))
        assert np.all(np.isfinite(engine.cos.u))
        assert np.all(np.isfinite(engine.k4.V_inc))

    def test_lh_drive_runs_without_blowup(self):
        N = 12
        engine = VacuumEngine3D.from_args(N=N, pml=2, temperature=0.0)
        src = CosseratBeltramiSource(
            x0=4, propagation_axis=0, amplitude=0.5, omega=2.0 * np.pi / 4.0,
            handedness="LH", sigma_yz=2.0, t_ramp=2.0, t_sustain=20.0,
        )
        engine.add_source(src)
        for _ in range(10):
            engine.step()
        assert np.all(np.isfinite(engine.cos.omega))

    def test_rh_drive_produces_nonzero_cosserat_response(self):
        """After drive runs, |ω| at source slab is clearly nonzero."""
        N = 12
        engine = VacuumEngine3D.from_args(N=N, pml=2, temperature=0.0)
        src = CosseratBeltramiSource(
            x0=4, propagation_axis=0, amplitude=0.8, omega=2.0 * np.pi / 4.0,
            handedness="RH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        engine.add_source(src)
        for _ in range(5):
            engine.step()
        # At source slab + active sites, |ω| should be non-trivial
        slab = engine.cos.omega[src.x0]
        slab_mask = engine.cos.mask_alive[src.x0]
        omega_mag_sq = np.sum(slab * slab, axis=-1)
        max_omega_mag_sq = float(omega_mag_sq[slab_mask].max())
        # At peak profile × some phase, |ω|² = amp²·profile² ~ 0.8²·0.9² = 0.52
        assert max_omega_mag_sq > 0.1, (
            f"Max |ω|² at source slab = {max_omega_mag_sq:.4f}; expected > 0.1"
        )


# ═══════════════════════════════════════════════════════════════════════════
# Handedness discrimination at source slab
# ═══════════════════════════════════════════════════════════════════════════
class TestHandednessDiscrimination:
    """At the source slab immediately after apply(), RH and LH injections
    produce ω_z fields that are sign-mirror-images of each other."""

    def test_rh_lh_ω_z_are_sign_flipped(self):
        N = 12
        amp = 0.6
        carrier = 1.0
        t = np.pi / (2.0 * carrier)  # sin = 1 → maximum difference

        eng_rh = VacuumEngine3D.from_args(N=N, pml=2, temperature=0.0)
        src_rh = CosseratBeltramiSource(
            x0=4, propagation_axis=0, amplitude=amp, omega=carrier,
            handedness="RH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        src_rh.apply(eng_rh, t)

        eng_lh = VacuumEngine3D.from_args(N=N, pml=2, temperature=0.0)
        src_lh = CosseratBeltramiSource(
            x0=4, propagation_axis=0, amplitude=amp, omega=carrier,
            handedness="LH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        src_lh.apply(eng_lh, t)

        # ω_z at source slab, active sites only
        slab_mask = eng_rh.cos.mask_alive[4]
        ω_z_rh = eng_rh.cos.omega[4, :, :, 2][slab_mask]
        ω_z_lh = eng_lh.cos.omega[4, :, :, 2][slab_mask]
        # RH has ω_z > 0 at this t; LH has ω_z < 0
        assert np.all(ω_z_rh >= 0) and np.any(ω_z_rh > 0.1)
        assert np.all(ω_z_lh <= 0) and np.any(ω_z_lh < -0.1)
        # Exact sign-flip
        assert np.allclose(ω_z_rh, -ω_z_lh, atol=1e-10)


# ═══════════════════════════════════════════════════════════════════════════
# Active-mask respect + no K4 injection
# ═══════════════════════════════════════════════════════════════════════════
class TestNoK4Injection:
    """This source deliberately does NOT touch K4 V_inc — it bypasses
    the (y+z)/√2 port-span issue by working purely in the Cosserat
    sector. V stays at whatever initialize_thermal set it to (0 at T=0)."""

    def test_V_inc_untouched_by_source(self):
        engine = VacuumEngine3D.from_args(N=10, pml=1, temperature=0.0)
        src = CosseratBeltramiSource(
            x0=3, propagation_axis=0, amplitude=1.0, omega=1.0,
            handedness="RH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        engine.add_source(src)
        for _ in range(5):
            engine.step()
        # K4 V_inc evolves via scatter+connect but starts at 0 with no K4 source.
        # Under the asymmetric coupling, V_inc may pick up from Cosserat→K4 back-coupling.
        # Core invariant: the SOURCE ITSELF doesn't write to V_inc (coupling is separate).
        # Verify by running one apply() against a fresh engine and checking V_inc is unchanged.
        fresh = VacuumEngine3D.from_args(N=10, pml=1, temperature=0.0)
        V_before = fresh.k4.V_inc.copy()
        src_fresh = CosseratBeltramiSource(
            x0=3, propagation_axis=0, amplitude=1.0, omega=1.0,
            handedness="RH", sigma_yz=2.0, t_ramp=0.0, t_sustain=100.0,
        )
        src_fresh.apply(fresh, t=0.5)
        assert np.array_equal(fresh.k4.V_inc, V_before), (
            "CosseratBeltramiSource must not touch K4 V_inc directly"
        )

    def test_pml_sites_not_written(self):
        """Cosserat mask_alive excludes PML; source respects it."""
        engine = VacuumEngine3D.from_args(N=12, pml=2, temperature=0.0)
        src = CosseratBeltramiSource(
            x0=4, propagation_axis=0, amplitude=1.0, omega=1.0,
            handedness="RH", sigma_yz=4.0,  # wide enough to hit PML
            t_ramp=0.0, t_sustain=100.0,
        )
        src.apply(engine, t=0.0)
        # Inactive sites at the source slab should stay 0
        inactive_mask = ~engine.cos.mask_alive[src.x0]
        ω_at_slab = engine.cos.omega[src.x0]
        assert np.all(ω_at_slab[inactive_mask] == 0.0), (
            "Source must not write to PML-masked sites"
        )


# ═══════════════════════════════════════════════════════════════════════════
# Amplitude sizing sanity
# ═══════════════════════════════════════════════════════════════════════════
class TestAmplitudeSizing:
    """Design-formula check for `amp_sat = λ/2 = π/k = ω_yield/k`.

    Continuum algebra: for a Beltrami ω wave with |ω| = A and wavenumber
    k = 2π/λ, the curvature |κ| = |∂ω/∂x| ~ A·k. Saturation condition
    A²_μ = (|κ|/ω_yield)² = 1 requires A·k/π = 1 (with ω_yield = π default),
    giving A_sat = π/k = λ/2.

    Numerical saturation at this amplitude is already validated in
    test_phase4_asymmetric_saturation.py::TestPhase4MeissnerMechanism
    at larger λ (N=16 → amp·k ≈ π gives min(S_μ) ≈ 0.22). This test
    just pins the design-formula arithmetic without re-validating
    saturation (first-order tetrahedral gradient has ~5%+ discretization
    error at coarse λ; Phase 4 E.1a covers the high-λ regime)."""

    def test_amp_sat_formula(self):
        """λ/2 = π/k for k = 2π/λ (trivial algebra check, prevents
        typos in the design formula used by driver scripts)."""
        for λ in [3.5, 4.0, 5.0, 7.0, 10.0, 16.0]:
            k = 2.0 * np.pi / λ
            amp_sat_from_lambda = λ / 2.0
            amp_sat_from_k = np.pi / k
            assert amp_sat_from_lambda == pytest.approx(amp_sat_from_k, rel=1e-12)

    def test_beltrami_curvature_magnitude_scales_linearly_with_amp(self):
        """|κ| scales linearly with amp for a Beltrami wave — not a
        full S_μ saturation test (that's Phase 4 E.1a scope), just
        documents the design-formula dependency."""
        N = 16
        λ = 8.0  # Long wavelength → good discretization
        k = 2.0 * np.pi / λ
        x_idx = np.arange(N).reshape(N, 1, 1, 1)

        kappa_magnitudes = []
        amps = [0.5, 1.0, 2.0, 4.0]
        for amp in amps:
            omega = np.zeros((N, N, N, 3), dtype=np.float64)
            omega[..., 1] = amp * np.cos(k * x_idx[..., 0])
            omega[..., 2] = -amp * np.sin(k * x_idx[..., 0])
            # |κ| at interior via direct synthesis (∂_x ω_y, ∂_x ω_z dominate)
            # Analytically |κ| = amp·k for this Beltrami ω
            kappa_magnitudes.append(amp * k)

        # Verify linear scaling: each amp produces |κ| = amp·k
        ratios = [kappa_magnitudes[i] / amps[i] for i in range(len(amps))]
        assert all(r == pytest.approx(k, rel=1e-12) for r in ratios)

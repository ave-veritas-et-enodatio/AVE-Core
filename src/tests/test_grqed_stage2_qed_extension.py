r"""Stage-2 QED-extension — the BZ-cutoff propagator + the E-route birefringence.

Tests the SECOND increment of the GR/QED-extension engine: two dormant-in-the-QED-
regime corrections ON the inherited QED / Maxwell solver. The inherited LINEAR /
continuum QED core is the weak-field / low-momentum limit and is NOT re-derived
here — these tests target ONLY the corrections.

TWO-TEST DOCTRINE (every correction gets BOTH):

  (1) THE BRILLOUIN-CUTOFF PROPAGATOR — a FORM-DERIVED 1-loop regulator.
      (i)  RECOVER-QED (consistency): at qℓ ≪ 1, the lattice dispersion
           (2/ℓ²)Σ_b(1−cos(k·b̂·ℓ)) → |k|² (continuum QED propagator), so the
           loop integrand → the QED integrand to the (kℓ)²/12 Taylor remainder.
      (ii) ACTIVATE-AT-CUTOFF (manifestation): the loop integral over the FIRST
           Brillouin zone is FINITE by mode-count (the band-limited dispersion
           saturates at the BZ edge); the continuum integral DIVERGES with Λ.

  (2) THE E-ROUTE VACUUM BIREFRINGENCE — the bankable chord (clm-pp3qwf).
      (i)  RECOVER-QED (consistency): at E ≪ E_yield, δn_bir → 0 (no tree-level
           birefringence — like QED at tree level).
      (ii) ACTIVATE: the O(1) differential appears as E → E_yield.

DISTINCT-CUTOFF DISCIPLINE (constants.py:286-294): the loop-integral bound is the
SPATIAL k_max = π/ℓ_node (K_MAX_SPATIAL), NOT the temporal ω_C = c/ℓ_node (the
μ-grade bound); the exact ratio is π. A guard test asserts the ratio and the
DECLARED bound.

FORM/VALUE: the cutoff FORM is FORM-DERIVED (Axiom 1); the saturating-ε is
FORM-POSTULATED (Axiom 4); α is IMPORTED (QED's coupling). The 7.5/α³ magnitude
is an α-ECHO; the CHORD is the EXISTENCE of the tree-level O(1) structure.

The brillouin_cutoff module is α-CLEAN (a guard test asserts no ALPHA reaches the
regulator). The heavy BZ convergence + continuum-divergence sweeps are routed to
the engine_sim lane (conftest allowlist; #411 OOM-class cost+role discipline).
"""

import numpy as np
import pytest

from ave.core.constants import ALPHA, C_0, E_CRIT, E_YIELD, L_NODE, OMEGA_C
from ave.qed.birefringence import (
    QED_EH_DIFFERENCED_COEFF,
    birefringence_dn,
    birefringence_eigenindices,
    chord_magnitude_ratio,
)
from ave.qed.brillouin_cutoff import (
    K_MAX_SPATIAL,
    continuum_loop_integral,
    lattice_dispersion_denominator,
    loop_integral_brillouin_zone,
)

# IR regulator mass² in lattice units (a small positive scale; the loop tests are
# insensitive to its exact value — it only keeps the integrand bounded at k → 0).
_M_SQ = 0.5 / L_NODE**2


# ═══════════════════════════════════════════════════════════════════════════════
# (1) THE BRILLOUIN-CUTOFF PROPAGATOR
# ═══════════════════════════════════════════════════════════════════════════════


class TestBZPropagatorRecoverQED:
    """(1)(i) RECOVER-QED (consistency-class): qℓ ≪ 1 → continuum QED propagator."""

    def test_lattice_dispersion_recovers_continuum_at_small_kl(self):
        # At |k|ℓ ≪ 1: cos(kℓ) → 1 − ½(kℓ)², so D_lat → |k|² (continuum). The
        # relative error is the Taylor remainder (kℓ)²/12.
        for kl in (1e-3, 1e-2, 1e-1):
            k = np.array([kl / L_NODE, 0.0, 0.0])
            d_lat = lattice_dispersion_denominator(k)
            d_cont = float(np.sum(k**2))
            rel = abs(d_lat - d_cont) / d_cont
            # the leading remainder is (kℓ)²/12
            assert rel < (kl**2 / 12.0) * 1.01, (kl, rel)
            # and it shrinks quadratically with kℓ
            assert rel < 1e-3 if kl <= 1e-1 else True

    def test_recover_qed_is_quadratic_in_kl(self):
        # the recover-QED error scales as (kℓ)² — halving kℓ quarters the error.
        def rel_err(kl):
            k = np.array([kl / L_NODE, 0.0, 0.0])
            d_lat = lattice_dispersion_denominator(k)
            d_cont = float(np.sum(k**2))
            return abs(d_lat - d_cont) / d_cont

        e1, e2 = rel_err(2e-2), rel_err(1e-2)
        assert np.isclose(e1 / e2, 4.0, rtol=2e-2)  # quadratic scaling

    def test_full_diagonal_direction_also_recovers(self):
        # recover-QED holds for an off-axis (diagonal) momentum too.
        kl = 1e-2
        k = (kl / L_NODE) * np.array([1.0, 1.0, 1.0]) / np.sqrt(3.0)
        d_lat = lattice_dispersion_denominator(k)
        d_cont = float(np.sum(k**2))
        assert abs(d_lat - d_cont) / d_cont < 1e-3


class TestBZPropagatorActivateAtCutoff:
    """(1)(ii) ACTIVATE-AT-CUTOFF (manifestation-class): BZ-edge band-limit ⇒ finite."""

    def test_dispersion_saturates_at_brillouin_edge(self):
        # at the BZ edge k_b = π/ℓ the per-axis term saturates at 4/ℓ² (band-limit).
        k_edge = np.array([np.pi / L_NODE, 0.0, 0.0])
        d_edge = lattice_dispersion_denominator(k_edge)
        assert np.isclose(d_edge, 4.0 / L_NODE**2, rtol=1e-12)
        # the (π,π,π) corner saturates at 12/ℓ² — the maximum of the band.
        k_corner = (np.pi / L_NODE) * np.ones(3)
        d_corner = lattice_dispersion_denominator(k_corner)
        assert np.isclose(d_corner, 12.0 / L_NODE**2, rtol=1e-12)

    def test_dispersion_is_bounded_over_the_whole_bz(self):
        # the band-limited dispersion never exceeds 12/ℓ² anywhere in the BZ —
        # this boundedness is WHY the loop integral is finite.
        rng = np.random.default_rng(0)
        k = (np.pi / L_NODE) * (2.0 * rng.random((10000, 3)) - 1.0)
        d = lattice_dispersion_denominator(k)
        assert np.all(d >= -1e-6)
        assert np.all(d <= 12.0 / L_NODE**2 + 1e-6)

    def test_bz_loop_integral_is_finite(self):
        # the loop integral over the first BZ is finite (not NaN/inf) by mode-count.
        i_lat = loop_integral_brillouin_zone(m_sq=_M_SQ, ell=L_NODE, n_grid=32)
        assert np.isfinite(i_lat)
        assert i_lat > 0.0

    def test_continuum_loop_integral_diverges_with_cutoff(self):
        # the SAME integrand in the continuum GROWS without bound as Λ → ∞ — the
        # UV divergence the BZ cutoff removes (QED needs a counterterm here).
        vals = [
            continuum_loop_integral(f * K_MAX_SPATIAL, m_sq=_M_SQ)
            for f in (1, 2, 4, 8)
        ]
        # strictly increasing with Λ (monotone divergence, ~Λ³)
        assert all(vals[i + 1] > vals[i] for i in range(len(vals) - 1))
        # doubling Λ roughly doubles-and-more (super-linear, Λ³-dominated tail)
        assert vals[-1] / vals[0] > 5.0  # 8× Λ → > 5× integral


class TestBZLoopIntegralConvergence:
    """BZ loop-integral CONVERGENCE (heavy quadrature → engine_sim lane)."""

    def test_bz_loop_integral_converges_with_grid(self):
        # the finite BZ value converges as the mode-grid refines (N=48 ≈ N=72).
        i48 = loop_integral_brillouin_zone(m_sq=_M_SQ, ell=L_NODE, n_grid=48)
        i72 = loop_integral_brillouin_zone(m_sq=_M_SQ, ell=L_NODE, n_grid=72)
        assert np.isfinite(i48) and np.isfinite(i72)
        assert abs(i48 - i72) / i72 < 1e-3  # converged (the value is well-defined)

    def test_bz_finite_while_continuum_diverges_same_integrand(self):
        # the discriminating contrast: SAME integrand, FINITE on the BZ vs
        # ARBITRARILY LARGE in the continuum as the cutoff is lifted.
        i_bz = loop_integral_brillouin_zone(m_sq=_M_SQ, ell=L_NODE, n_grid=48)
        # push the continuum cutoff far past k_max — it keeps growing past i_bz-scale
        i_cont_far = continuum_loop_integral(8 * K_MAX_SPATIAL, m_sq=_M_SQ)
        i_cont_near = continuum_loop_integral(1 * K_MAX_SPATIAL, m_sq=_M_SQ)
        assert np.isfinite(i_bz)
        # the continuum is NOT cutoff-stable (the divergence) — far ≫ near
        assert i_cont_far > 3.0 * i_cont_near


# ═══════════════════════════════════════════════════════════════════════════════
# (2) THE E-ROUTE VACUUM BIREFRINGENCE
# ═══════════════════════════════════════════════════════════════════════════════


class TestBirefringenceRecoverQED:
    """(2)(i) RECOVER-QED (consistency-class): E ≪ E_yield → δn_bir → 0 (no tree biref)."""

    def test_dn_vanishes_at_low_field(self):
        # at E ≪ E_yield the differential → 0 — no tree-level birefringence (QED-like).
        for frac in (1e-4, 1e-3, 1e-2):
            dn = birefringence_dn(frac * E_YIELD)
            assert abs(dn) < frac**2  # bounded by A² (and below it)

    def test_leading_term_is_minus_half_A_squared(self):
        # the leading differential is exactly −½A² (E²-leading, NEGATIVE).
        for frac in (1e-4, 1e-3, 1e-2):
            dn = birefringence_dn(frac * E_YIELD)
            expected = -0.5 * frac**2
            assert np.isclose(dn, expected, rtol=2e-2)
            assert dn < 0.0  # negative

    def test_dn_is_E_squared_leading_not_E_to_the_fourth(self):
        # halving E quarters δn (E²-leading) — NOT sixteenths (would be E⁴). This is
        # the corrected discriminator: an E² slope does NOT falsify AVE (clm-pp3qwf).
        dn1 = birefringence_dn(2e-3 * E_YIELD)
        dn2 = birefringence_dn(1e-3 * E_YIELD)
        assert np.isclose(dn1 / dn2, 4.0, rtol=1e-2)  # E²-leading

    def test_zero_field_is_exactly_zero(self):
        assert birefringence_dn(0.0) == 0.0


class TestBirefringenceActivate:
    """(2)(ii) ACTIVATE: the O(1) differential appears as E → E_yield."""

    def test_birefringence_grows_with_field(self):
        fracs = np.array([0.1, 0.3, 0.5, 0.7])
        dns = np.array([birefringence_dn(f * E_YIELD) for f in fracs])
        # monotone in |δn| with field
        assert np.all(np.diff(np.abs(dns)) > 0.0)

    def test_O1_birefringence_at_high_field(self):
        # near yield the differential is O(0.1-1) — a tree-level O(1) structure.
        dn = birefringence_dn(0.5 * E_YIELD)
        assert abs(dn) > 0.1  # O(1)-scale, not loop-suppressed

    def test_eigenindices_split_under_drive(self):
        # the two probe eigen-indices separate (uniaxial) and n_⊥ uses the SAME
        # canonical Op14 kernel S(A): n_⊥ = √S = (1−A²)^(1/4).
        A = 0.3
        n_perp, n_par = birefringence_eigenindices(A)
        assert n_par < n_perp  # δn = n_∥ − n_⊥ < 0
        assert np.isclose(n_perp, (1.0 - A**2) ** 0.25, rtol=1e-12)


# ═══════════════════════════════════════════════════════════════════════════════
# DISTINCT-CUTOFF DISCIPLINE + THE α-ECHO MAGNITUDE + FORM/VALUE GUARDS
# ═══════════════════════════════════════════════════════════════════════════════


class TestDistinctCutoffDiscipline:
    """The SPATIAL loop bound vs the TEMPORAL μ-grade bound — not conflated."""

    def test_loop_bound_is_the_spatial_k_max(self):
        # the DECLARED loop bound is the SPATIAL k_max = π/ℓ_node (NOT ω_C).
        assert np.isclose(K_MAX_SPATIAL, np.pi / L_NODE, rtol=1e-12)

    def test_spatial_and_temporal_cutoffs_differ_by_pi(self):
        # k_max = π/ℓ_node (spatial loop bound) vs ω_C/c = 1/ℓ_node (temporal
        # μ-grade bound, in 1/m). The exact ratio is π. Conflating them is a π-error.
        temporal_in_inverse_m = OMEGA_C / C_0
        assert np.isclose(temporal_in_inverse_m, 1.0 / L_NODE, rtol=1e-12)
        assert np.isclose(K_MAX_SPATIAL / temporal_in_inverse_m, np.pi, rtol=1e-12)

    def test_loop_integral_domain_uses_spatial_bound(self):
        # the BZ quadrature domain edge is k_max = π/ℓ — using ω_C/c (= 1/ℓ) would
        # shrink the zone by π and change the (finite) value. Guard the domain edge:
        # the dispersion saturates at 4/ℓ² exactly AT k = K_MAX_SPATIAL on one axis.
        k_at_bound = np.array([K_MAX_SPATIAL, 0.0, 0.0])
        d = lattice_dispersion_denominator(k_at_bound)
        assert np.isclose(d, 4.0 / L_NODE**2, rtol=1e-12)


class TestChordMagnitudeAlphaEcho:
    """The 7.5/α³ magnitude — an α-ECHO (value-level), NOT the chord."""

    def test_chord_magnitude_equals_7p5_over_alpha_cubed(self):
        ratio = chord_magnitude_ratio()
        assert np.isclose(ratio, 7.5 / ALPHA**3, rtol=1e-9)
        assert np.isclose(ratio, 1.93e7, rtol=2e-2)  # ≈ 1.93×10⁷

    def test_magnitude_rides_alpha_inverse_cubed(self):
        # the magnitude IS an α-echo: it is exactly (45/6)·α⁻³, i.e. it rides α⁻³.
        # (Symmetric standard: QED's a_EH·α² is equally α-rooted.) This is the
        # value-level dependence on the IMPORTED α — flagged, not hidden.
        ratio = chord_magnitude_ratio()
        assert np.isclose(ratio * ALPHA**3, 45.0 / 6.0, rtol=1e-9)

    def test_qed_differenced_coeff_is_three_over_45(self):
        # the matched QED comparison uses the DIFFERENCED Euler-Heisenberg
        # coefficient 3/45 (par 7/45 − perp 4/45), not the single 7/45.
        assert np.isclose(QED_EH_DIFFERENCED_COEFF, 3.0 / 45.0, rtol=1e-12)

    def test_e_crit_over_e_yield_squared_is_one_over_alpha(self):
        # the (E_crit/E_yield)² = 1/α relation that turns α² → α³ in the ratio.
        assert np.isclose((E_CRIT / E_YIELD) ** 2, 1.0 / ALPHA, rtol=1e-9)


class TestFormValueGuards:
    """FORM/VALUE honesty — machine-checkable: regulator α-clean; kernel REUSED."""

    def test_brillouin_cutoff_module_is_alpha_clean(self):
        # the regulator FORM is purely geometric (ℓ_node) — α must NOT reach it.
        import inspect

        import ave.qed.brillouin_cutoff as mod

        src = inspect.getsource(mod)
        # the loop-regulator functions must not import or use ALPHA / Q_TANK.
        assert "ALPHA" not in src.replace("# α", "")  # no ALPHA symbol in code
        assert "Q_TANK" not in src
        # the only constants import is the geometric ℓ_node
        assert "from ave.core.constants import L_NODE" in src

    def test_birefringence_reuses_canonical_op14_kernel(self):
        # the saturating-ε is NOT re-minted: the module imports the SAME
        # saturation_factor that fdtd_3d uses (scale_invariant), and n_⊥ = √S.
        import inspect

        import ave.qed.birefringence as mod

        src = inspect.getsource(mod)
        assert "from ave.axioms.scale_invariant import saturation_factor" in src
        # numeric proof of reuse: n_⊥ from the module == √S from the canonical kernel.
        from ave.axioms.scale_invariant import saturation_factor

        A = 0.25
        n_perp, _ = birefringence_eigenindices(A)
        assert np.isclose(n_perp, np.sqrt(saturation_factor(A, yield_limit=1.0)), rtol=1e-12)

    def test_birefringence_matches_fdtd_local_epsilon_kernel(self):
        # cross-check: the module's ε-softening S(A) is bit-identical to the kernel
        # inside fdtd_3d._compute_local_epsilon (ε_eff = ε₀·saturation_factor).
        from ave.axioms.scale_invariant import saturation_factor

        A = 0.4
        # n_⊥² = √(1−A²) = S(A) — the SAME S the FDTD ε-update applies.
        n_perp, _ = birefringence_eigenindices(A)
        assert np.isclose(n_perp**2, saturation_factor(A, yield_limit=1.0), rtol=1e-12)

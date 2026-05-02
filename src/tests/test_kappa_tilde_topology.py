"""
test_kappa_tilde_topology.py
==============================

Unit tests for the κ̃ (kappa tilde) topological factor exposed by the
2026-05-02 refactor of `cosserat_field_3d.py`.

Per doc 108 §11.5 + Grant directive 2026-05-02 ("p_c is where the chiral
LC vacuum hits K/G=2"), the chiral coupling κ_chiral = α · κ̃ where κ̃ is
the dimensionless topological factor (independent of α). The refactor
exposes κ̃ as a separate constant + helper function so emergence tests
can use it as a substrate-physics-native input without α.

Verifies:
  - KAPPA_TILDE_ELECTRON = 6/5 = 1.2 (purely topological)
  - kappa_tilde_torus(2, 3) = 1.2 (electron winding)
  - kappa_tilde_torus(1, 1) = 0.5 ((1,1) Beltrami)
  - kappa_tilde_torus(p, q) = pq/(p+q) general formula
  - KAPPA_CHIRAL_ELECTRON = ALPHA × KAPPA_TILDE_ELECTRON (refactor consistency)
  - kappa_chiral_from_topology(2, 3) = 1.2 × ALPHA (electron full coupling)

References:
  - cosserat_field_3d.py:30-100 (refactored module-level structure)
  - doc 20_ Sub-Theorem 3.1.1 (κ_chiral derivation per Ax 2)
  - doc 108 §11.5 emergence-test framework
"""
from __future__ import annotations

import pytest

from ave.core.constants import ALPHA
from ave.topological.cosserat_field_3d import (
    KAPPA_CHIRAL_ELECTRON,
    KAPPA_TILDE_ELECTRON,
    KAPPA_TILDE_BELTRAMI_11,
    kappa_chiral_from_topology,
    kappa_tilde_torus,
)


class TestKappaTildeTopology:
    """Pure topological factor κ̃ — independent of α."""

    def test_kappa_tilde_electron_is_six_fifths(self):
        """κ̃(electron) = 2·3/(2+3) = 6/5 = 1.2."""
        assert KAPPA_TILDE_ELECTRON == 1.2
        # Exact: 6/5 (rational)
        assert KAPPA_TILDE_ELECTRON == pytest.approx(6.0 / 5.0, abs=1e-15)

    def test_kappa_tilde_beltrami_is_one_half(self):
        """κ̃(1,1 Beltrami) = 1·1/(1+1) = 1/2 = 0.5."""
        assert KAPPA_TILDE_BELTRAMI_11 == 0.5

    def test_kappa_tilde_torus_2_3(self):
        """kappa_tilde_torus(2, 3) = 6/5 = 1.2 (electron)."""
        assert kappa_tilde_torus(2, 3) == pytest.approx(1.2, abs=1e-15)

    def test_kappa_tilde_torus_1_1(self):
        """kappa_tilde_torus(1, 1) = 0.5 (Beltrami)."""
        assert kappa_tilde_torus(1, 1) == 0.5

    def test_kappa_tilde_general_formula(self):
        """kappa_tilde_torus(p, q) = pq/(p+q) for general (p,q)."""
        for p, q in [(2, 3), (3, 5), (5, 7), (2, 5), (3, 4), (1, 3)]:
            expected = (p * q) / (p + q)
            assert kappa_tilde_torus(p, q) == pytest.approx(expected, abs=1e-15)

    def test_kappa_tilde_symmetric_in_p_q(self):
        """κ̃(p, q) = κ̃(q, p) — winding-direction-symmetric."""
        for p, q in [(2, 3), (3, 5), (1, 4)]:
            assert kappa_tilde_torus(p, q) == kappa_tilde_torus(q, p)

    def test_kappa_tilde_zero_p_zero_q_raises(self):
        """p+q=0 should raise (degenerate topology)."""
        with pytest.raises(ValueError):
            kappa_tilde_torus(0, 0)


class TestKappaChiralFromTopology:
    """Total chiral coupling κ_chiral = α · κ̃."""

    def test_electron_full_coupling(self):
        """kappa_chiral_from_topology(2, 3) = 1.2 × ALPHA."""
        assert kappa_chiral_from_topology(2, 3) == pytest.approx(
            1.2 * ALPHA, abs=1e-15
        )

    def test_alpha_explicitly_passed(self):
        """Custom α can be passed (for emergence test scenarios)."""
        custom_alpha = 0.01  # arbitrary
        assert kappa_chiral_from_topology(2, 3, alpha=custom_alpha) == pytest.approx(
            1.2 * custom_alpha, abs=1e-15
        )

    def test_alpha_default_is_codata_alpha(self):
        """Default α is constants.ALPHA."""
        assert kappa_chiral_from_topology(2, 3) == kappa_chiral_from_topology(
            2, 3, alpha=ALPHA
        )


class TestRefactorConsistency:
    """Refactor preserves backward-compatible numerical values."""

    def test_kappa_chiral_electron_unchanged(self):
        """KAPPA_CHIRAL_ELECTRON numerical value matches pre-refactor (1.2 × ALPHA)."""
        assert KAPPA_CHIRAL_ELECTRON == pytest.approx(1.2 * ALPHA, abs=1e-15)

    def test_kappa_chiral_electron_from_helper(self):
        """KAPPA_CHIRAL_ELECTRON == kappa_chiral_from_topology(2, 3) — round-trip."""
        assert KAPPA_CHIRAL_ELECTRON == pytest.approx(
            kappa_chiral_from_topology(2, 3), abs=1e-15
        )

    def test_kappa_chiral_decomposes(self):
        """KAPPA_CHIRAL_ELECTRON = ALPHA × KAPPA_TILDE_ELECTRON exactly."""
        assert KAPPA_CHIRAL_ELECTRON == ALPHA * KAPPA_TILDE_ELECTRON

    def test_kappa_chiral_numerical_value(self):
        """KAPPA_CHIRAL_ELECTRON ≈ 8.757e-3 (sanity check)."""
        assert KAPPA_CHIRAL_ELECTRON == pytest.approx(8.7568e-3, rel=1e-4)


class TestEmergenceTestPrerequisite:
    """The refactor enables emergence testing — verify the structure is usable."""

    def test_kappa_tilde_can_be_used_without_alpha(self):
        """For emergence test: κ̃ is dimensionless geometric input only."""
        # In an emergence test, κ̃ is set from topology, NOT from α
        kappa_tilde = kappa_tilde_torus(2, 3)
        # Verify it's just a pure number, computable without ALPHA
        assert kappa_tilde == 1.2
        # Verify it doesn't depend on the value of ALPHA
        # (no ALPHA-dependence in the formula pq/(p+q))
        assert kappa_tilde > 0
        assert kappa_tilde < 10  # reasonable topological factor range

    def test_emergence_test_can_set_alpha_freely(self):
        """For α-emergence test: pass any α (including unity) to compute κ_chiral."""
        # Natural-units alpha (=1):
        kappa_at_unity = kappa_chiral_from_topology(2, 3, alpha=1.0)
        assert kappa_at_unity == 1.2
        # CODATA alpha:
        kappa_codata = kappa_chiral_from_topology(2, 3, alpha=ALPHA)
        assert kappa_codata == pytest.approx(1.2 * ALPHA)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

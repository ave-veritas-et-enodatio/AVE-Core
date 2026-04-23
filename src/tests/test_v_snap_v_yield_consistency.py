"""
Pre-registered unit tests for the V_SNAP / V_yield normalization
conventions — Stage 6 Phase 1.

Pins the engine's normalization conventions against the AVE axioms so
that the V_SNAP-vs-V_yield conflation flagged in
[45_lattice_impedance_first_principles.md §3.1] cannot regress once
Stage 6 Phases 2-5 start adding V_yield-normalized engine state.

Pinned identities (all Axiom 1 + 4):

  1. V_SNAP = m_e c² / e              (Axiom 1 + charge quantum)
  2. V_YIELD = √α · V_SNAP            (Axiom 4 engineering yield)
  3. V_YIELD / V_SNAP = √α ≈ 0.0854   (conversion factor)
  4. E_YIELD = V_YIELD / ℓ_node       (field-strength yield)
  5. E_crit / E_YIELD = 1/√α ≈ 11.7   (Vol 1 Ch 7:130 Schwinger-deep ratio)

And the convention clarification:

  6. A²_SNAP = V²/V_SNAP²  ≠  A²_yield = V²/V_yield²
     Conversion: A²_yield = A²_SNAP / α
     At V = V_yield: A²_SNAP = α ≈ 0.0073, A²_yield = 1.0
     At V = V_SNAP: A²_SNAP = 1.0, A²_yield = 1/α ≈ 137

The engine today uses A² = V²/V_SNAP² in k4_tlm.py:203 and
cosserat_field_3d.py's _reflection_density, so "Regime IV rupture at
A²=1" is the Schwinger-limit full saturation, NOT the Regime-III yield
onset. The Vacuum Varactor (Vol 4 Ch 1:132) crashes at V_yield, i.e. at
A²_SNAP = α. Any new Stage 6 code that uses V_yield normalization must
convert explicitly via the factor 1/α.

Reference:
  - manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:104
    (V_YIELD definition, INVARIANT-C1 in ave-kb/CLAUDE.md)
  - manuscript/vol_1_foundations/chapters/07_regime_map.tex:130
    (Schwinger critical field r = V_SNAP/V_yield = 1/√α)
  - research/L3_electron_soliton/45_lattice_impedance_first_principles.md §3.1
    (conflation flag)
  - research/L3_electron_soliton/54_pair_production_axiom_derivation.md §5
    (resolution for Stage 6 engine work)

Predictions.yaml entry: P_phase0_varactor (also covers this consistency).
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.core.constants import (
    ALPHA,
    C_0,
    E_CRIT,
    E_YIELD,
    HBAR,
    L_NODE,
    M_E,
    V_SNAP,
    V_YIELD,
    e_charge,
)


# ═══════════════════════════════════════════════════════════════════════════
# 1. V_SNAP = m_e c² / e  (Axiom 1 + charge quantum)
# ═══════════════════════════════════════════════════════════════════════════
class TestVSnapDefinition:
    """V_SNAP is the absolute nodal breakdown voltage, constants.py:266."""

    def test_v_snap_equals_rest_energy_over_charge(self):
        """V_SNAP = m_e c² / e ≈ 511 kV (Vol 4 Ch 11:232 tensile limit)."""
        expected = (M_E * C_0**2) / e_charge
        assert V_SNAP == pytest.approx(expected, rel=1e-12)

    def test_v_snap_value_is_511_kV(self):
        """V_SNAP ≈ 5.110e5 V (511 kV), the electron rest-mass voltage."""
        assert V_SNAP == pytest.approx(5.110e5, rel=2e-3)


# ═══════════════════════════════════════════════════════════════════════════
# 2. V_YIELD = √α · V_SNAP  (Axiom 4 engineering yield)
# ═══════════════════════════════════════════════════════════════════════════
class TestVYieldDefinition:
    """V_YIELD is the engineering yield threshold, constants.py:275."""

    def test_v_yield_equals_sqrt_alpha_times_v_snap(self):
        """V_YIELD = √α · V_SNAP (Vol 4 Ch 1:129, INVARIANT-C1)."""
        assert V_YIELD == pytest.approx(np.sqrt(ALPHA) * V_SNAP, rel=1e-12)

    def test_v_yield_value_is_43_65_kV(self):
        """V_YIELD ≈ 43.65 kV (INVARIANT-C1 canonical value)."""
        assert V_YIELD == pytest.approx(43.65e3, rel=5e-3)


# ═══════════════════════════════════════════════════════════════════════════
# 3. Conversion factor V_YIELD / V_SNAP = √α
# ═══════════════════════════════════════════════════════════════════════════
class TestVSnapVYieldRatio:
    """The conversion factor between V_SNAP and V_yield normalizations."""

    def test_ratio_is_sqrt_alpha(self):
        """V_YIELD / V_SNAP = √α ≈ 0.0854 (Vol 1 Ch 7:104)."""
        assert V_YIELD / V_SNAP == pytest.approx(np.sqrt(ALPHA), rel=1e-12)

    def test_ratio_inverse_is_1_over_sqrt_alpha(self):
        """V_SNAP / V_YIELD = 1/√α ≈ 11.7 (Vol 1 Ch 7:130 Schwinger-deep)."""
        assert V_SNAP / V_YIELD == pytest.approx(1.0 / np.sqrt(ALPHA), rel=1e-12)
        assert V_SNAP / V_YIELD == pytest.approx(11.7, abs=0.1)

    def test_a_squared_conversion_factor(self):
        """A²_yield = A²_SNAP / α (doc 54_ §5 resolution)."""
        # At any common voltage V, compute both normalizations
        V = 0.3 * V_YIELD  # arbitrary test voltage below yield
        A_sq_snap = (V / V_SNAP) ** 2
        A_sq_yield = (V / V_YIELD) ** 2
        assert A_sq_yield == pytest.approx(A_sq_snap / ALPHA, rel=1e-12)

    def test_yield_voltage_in_engine_a_squared(self):
        """At V = V_yield: A²_SNAP = α, A²_yield = 1.0 (doc 54_ §5 crossover)."""
        A_sq_snap = (V_YIELD / V_SNAP) ** 2
        A_sq_yield = (V_YIELD / V_YIELD) ** 2
        assert A_sq_snap == pytest.approx(ALPHA, rel=1e-12)
        assert A_sq_yield == pytest.approx(1.0, abs=1e-12)

    def test_snap_voltage_in_engine_a_squared(self):
        """At V = V_SNAP: A²_SNAP = 1.0, A²_yield = 1/α ≈ 137 (Schwinger
        limit is deep Regime IV per Vol 1 Ch 7:130)."""
        A_sq_snap = (V_SNAP / V_SNAP) ** 2
        A_sq_yield = (V_SNAP / V_YIELD) ** 2
        assert A_sq_snap == pytest.approx(1.0, abs=1e-12)
        assert A_sq_yield == pytest.approx(1.0 / ALPHA, rel=1e-12)
        # Also directly: 1/α ≈ 137.036
        assert A_sq_yield == pytest.approx(1.0 / ALPHA, rel=1e-12)


# ═══════════════════════════════════════════════════════════════════════════
# 4. E_YIELD field-strength identity
# ═══════════════════════════════════════════════════════════════════════════
class TestEYieldIdentity:
    """E_YIELD = V_YIELD / ℓ_node (constants.py:286)."""

    def test_e_yield_equals_v_yield_over_l_node(self):
        """E_YIELD = V_YIELD / ℓ_node (Vol 1 Ch 7:124)."""
        assert E_YIELD == pytest.approx(V_YIELD / L_NODE, rel=1e-12)

    def test_e_yield_value(self):
        """E_YIELD ≈ 1.13e17 V/m (Vol 1 Ch 7:124 canonical value)."""
        assert E_YIELD == pytest.approx(1.13e17, rel=1e-2)


# ═══════════════════════════════════════════════════════════════════════════
# 5. Schwinger critical field relation (Vol 1 Ch 7:130)
# ═══════════════════════════════════════════════════════════════════════════
class TestSchwingerCriticalField:
    """E_crit / E_YIELD = 1/√α — Schwinger limit is deep Regime IV."""

    def test_e_crit_definition(self):
        """E_crit = m_e² c³ / (e ℏ) ≈ 1.32e18 V/m."""
        expected = (M_E**2 * C_0**3) / (e_charge * HBAR)
        assert E_CRIT == pytest.approx(expected, rel=1e-12)
        assert E_CRIT == pytest.approx(1.32e18, rel=5e-3)

    def test_e_crit_over_e_yield_is_1_over_sqrt_alpha(self):
        """E_crit / E_YIELD = V_SNAP / V_YIELD = 1/√α ≈ 11.7 (Vol 1 Ch 7:130).

        This is the Schwinger-limit-vs-yield-onset ratio. The engine's
        "A²=1 rupture" lives at E_crit (deep Regime IV), not at E_YIELD
        (Regime IV boundary). Any Stage 6 engine code that uses V_yield
        normalization must account for this factor-of-11.7 between the
        two conventions.
        """
        assert E_CRIT / E_YIELD == pytest.approx(1.0 / np.sqrt(ALPHA), rel=1e-3)


# ═══════════════════════════════════════════════════════════════════════════
# 6. Manifest consistency: predictions.yaml does not conflate normalizations
# ═══════════════════════════════════════════════════════════════════════════
class TestManifestNormalizationConsistency:
    """No pre_registered entry may silently conflate V_SNAP and V_yield."""

    def test_pre_registered_entries_reference_correct_normalization(self):
        """Pre_registered prediction notes must explicitly use V_yield
        when referring to yield-onset physics, NOT V_SNAP. This is a
        text-level check guarding against the conflation doc 54_ §5
        flags as load-bearing for Stage 6."""
        import pathlib
        import yaml

        manifest_path = pathlib.Path(__file__).resolve().parents[2] / (
            "manuscript/predictions.yaml"
        )
        with manifest_path.open() as f:
            manifest = yaml.safe_load(f)

        # Pre-registered entries whose notes discuss V_yield physics
        # (varactor, node resonance, asymmetric saturation) must mention
        # V_yield OR explicitly note the V_SNAP/α conversion.
        yield_physics_entries = {
            "P_phase0_varactor",
            "P_phase2_omega",
            "P_phase4_asymmetric",
        }
        checked = 0
        for entry in manifest.get("predictions", []):
            if not entry.get("pre_registered"):
                continue
            if entry["id"] not in yield_physics_entries:
                continue
            notes = entry.get("notes", "") or ""
            # Either V_yield naming, OR an explicit α-conversion, must
            # appear somewhere in the entry's notes / name
            combined = (entry.get("name", "") + " " + notes).lower()
            has_yield = ("v_yield" in combined or "yield" in combined
                         or "vol 4 ch 1" in combined
                         or "varactor" in combined)
            assert has_yield, (
                f"Entry {entry['id']}: yield-physics entry must reference "
                f"V_yield, varactor, or α-conversion in its name or notes"
            )
            checked += 1
        assert checked == len(yield_physics_entries), (
            f"Expected to check {len(yield_physics_entries)} entries, "
            f"only found {checked} — are they all present and pre_registered?"
        )

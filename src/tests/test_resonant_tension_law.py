"""Tests for the RESONANT time-averaged tension law + the radiation control.

Prereg (FROZEN): research/2026-07-04_resonant-tension-law_prereg_FROZEN.md.

🔴 VERDICT (post orchestrator re-run, 2026-07-04): **[RADIATION-CONTAMINATED]** — the
carrier as formulated DIES. Part 1 law is derived (⟨T⟩=(k_a/ℓ)y0², ⟨sin²⟩=½ DERIVED),
but the make-or-break Part-2 control FAILS on the quantity the mechanism CONSUMES: a
matched CW traveling wave carries a PERSISTENT per-bond ⟨T⟩ (both independent paths
agree — the phasor path AND the genuinely Γ-free ABCD-propagation path), which the
#526 remap consumes and which stiffens ρ' identically in kind to the confined hum. The
resonant-tension carrier cannot distinguish matter from radiation ⟹ contradicts #518 §7.
Rule 11: reported as the negative, no rescue. (The original PR gated the GRADIENT of
⟨T⟩, trivially zero for a uniform traveling wave — the CRITICAL error.)

These lock the LOAD-BEARING physics of the honest negative: the derived Part-1 law
(unchanged), the CONSUMED-observable re-gate (⟨T⟩ persists under the traveling wave),
the genuinely Γ-free reference path (reconcile can now disagree), the remap-stiffens-
radiation consequence, the [RADIATION-CONTAMINATED] verdict, and the symmetric identity
twins. T2 homonym guard: the resonance is the mechanical bow, never the Cosserat winding.
"""
from __future__ import annotations

import numpy as np
import pytest

from scripts.vol_1_foundations.resonant_tension_law import (
    A_CORE_SQRT_ALPHA,
    field_from_abcd_propagation,
    field_from_phasor,
    matched_line_reflection,
    part1_law_and_band,
    part2_radiation_control,
    reconcile_matched_T,
    reflecting_termination_reflection,
    resonant_tension_exact,
    resonant_tension_leading,
    run_positive_controls,
    select_bin,
    symbolic_backbone,
)
from scripts.vol_1_foundations.srs_elastic_tensor import srs_primitive


@pytest.fixture(scope="module")
def srs():
    return srs_primitive("right")


@pytest.fixture(scope="module")
def part1(srs):
    return part1_law_and_band(*srs)


@pytest.fixture(scope="module")
def part2(srs):
    return part2_radiation_control(*srs)


# --------------------------------------------------------------------------
# The sympy backbone -- ⟨sin²⟩=½ and the ⟨T⟩ law EXACT ZERO (the one derived half)
# --------------------------------------------------------------------------
def test_symbolic_backbone_all_exact_zero():
    """The DERIVED ½ (⟨sin²⟩) and ⟨T⟩=(k_a/ℓ)y0² -- every residual exactly 0 (sympy)."""
    res = symbolic_backbone()
    for name, val in res.items():
        assert val == 0, f"symbolic residual {name} = {val} (must be exactly 0)"


def test_half_factor_is_derived_not_asserted():
    """The ½ time-average factor is the DERIVED ⟨sin²⟩ -- proven exact by sympy."""
    res = symbolic_backbone()
    assert res["sin2_avg_minus_half"] == 0
    assert res["y2_avg_minus_y0sq_over_2"] == 0


def test_leading_ties_to_527_exact_tent_series():
    """The resonant leading law IS the 2nd-order series of the #527 exact tent law."""
    res = symbolic_backbone()
    assert res["exact_leading_coeff_minus_2ka_over_ell"] == 0


# --------------------------------------------------------------------------
# PART 1 -- the resonant tension law (leading + exact) -- UNCHANGED by the re-run
# --------------------------------------------------------------------------
def test_leading_law_value():
    """⟨T⟩_lead = (k_a/ℓ) y0² exactly (k_a=ℓ=1 ⟹ y0²)."""
    assert resonant_tension_leading(0.1) == pytest.approx(0.01)
    assert resonant_tension_leading(0.3) == pytest.approx(0.09)


def test_noload_gives_zero_tension():
    """y0→0 ⟹ ⟨T⟩→0 (both laws); the no-hum anchor."""
    assert resonant_tension_leading(0.0) == 0.0
    assert resonant_tension_exact(0.0) == 0.0


def test_leading_is_strict_upper_bound_on_exact():
    """The leading law over-predicts the exact cycle-average (concavity in y²)."""
    for y0 in (0.01, 0.05, 0.14, 0.42):
        assert resonant_tension_leading(y0) >= resonant_tension_exact(y0) - 1e-12


def test_quadratic_breaks_at_elastica_edge():
    """The quadratic approximation breaks progressively: ~4% (tent) / ~36% (elastica)."""
    dev_tent = (resonant_tension_leading(0.1428) - resonant_tension_exact(0.1428)) \
        / resonant_tension_exact(0.1428)
    dev_elastica = (resonant_tension_leading(0.4153) - resonant_tension_exact(0.4153)) \
        / resonant_tension_exact(0.4153)
    assert 0.03 < dev_tent < 0.06
    assert 0.30 < dev_elastica < 0.40


# --------------------------------------------------------------------------
# PART 1 -- the matter re-band (MAJOR-3: honest grid, identity twins EXCLUDED)
# --------------------------------------------------------------------------
def test_matter_track_reband_present(part1):
    """The matter track is re-banded over the in-regime hum amplitude (both edges)."""
    assert "lo_elastica" in part1["band"]
    assert "hi_tent" in part1["band"]
    assert part1["matter_track"]["rho_prime_band_exact"] is not None


def test_hum_tension_caps_rho_prime(part1):
    """⟨T⟩>0 (tension) CAPS ρ' (grows k_shear_eff) -- ρ' falls below the cold 9.7734."""
    for edge in ("lo_elastica", "hi_tent"):
        rows = part1["band"][edge]["rows"]
        rp0 = rows[0]["rho_prime_exact"]
        assert rp0 == pytest.approx(9.7733, abs=1e-3)  # T→0 identity anchor
        assert rows[-1]["rho_prime_exact"] < rp0, "tension must cap (lower) ρ'"


def test_identity_twins_labeled_and_excluded(part1):
    """MAJOR-3: BOTH y0→0 twins (ρ'→9.7734 AND ν→2/7) labeled + excluded (symmetric)."""
    mt = part1["matter_track"]
    assert mt["identity_limit_rho_prime"] == pytest.approx(9.7734, abs=1e-3)
    assert mt["identity_limit_nu"] == pytest.approx(2.0 / 7.0)
    for edge in part1["band"].values():
        for r in edge["rows"]:
            if r["y0"] <= 1e-3 * edge["y0_in_regime_max"]:
                assert r["is_identity_limit"] is True


def test_op_point_is_sqrt_alpha(part1):
    """The A1 mass-core op-point is A=√α (read-off, Class-C echo; never tuned)."""
    assert part1["op_point"]["A_axial_sqrt_alpha"] == pytest.approx(A_CORE_SQRT_ALPHA)


def test_reband_interior_does_not_reach_rho_2(part1):
    """KNIFE: the re-banded interior ρ' band does NOT reach ρ'=2."""
    lo, hi = part1["matter_track"]["rho_prime_band_exact"]
    assert lo > 2.0, "no interior edge lands on the ρ'=2 canon crossing"


# --------------------------------------------------------------------------
# PART 2 -- the CRITICAL re-gate: control (i) FAILS on the CONSUMED ⟨T⟩
# --------------------------------------------------------------------------
def test_matched_traveling_wave_carries_persistent_tension(part2):
    """CRITICAL: the matched CW traveling wave leaves a PERSISTENT per-bond ⟨T⟩ ≠ 0."""
    i = part2["i_matched"]
    assert i["T_bond_phasor"] == pytest.approx(1.0, rel=1e-6)
    assert i["T_bond_gamma_free"] == pytest.approx(1.0, rel=1e-6)
    assert i["T_vanishes"] is False, "the consumed ⟨T⟩ does NOT vanish (the CRITICAL)"


def test_two_paths_are_genuinely_independent_and_agree(part2):
    """MAJOR-1: the phasor and Γ-FREE ABCD paths agree on ⟨T⟩ (real reconcile)."""
    i = part2["i_matched"]
    assert i["T_bond_reconcile_rel"] < 1e-9
    gf = field_from_abcd_propagation(0.3, y0=1.0)
    assert gf["gamma_free"] is True
    assert gf["T_bond_mean"] == pytest.approx(1.0, rel=1e-6)


def test_radiation_stiffens_through_the_remap(part2):
    """CRITICAL: fed through the SAME remap, the traveling wave stiffens ρ' (9.77→0.90)."""
    i = part2["i_matched"]
    assert i["rho_prime_cold"] == pytest.approx(9.7733, abs=1e-3)
    assert i["rho_prime_under_traveling_wave"] < 1.0
    assert i["radiation_stiffens"] is True


def test_phasor_field_path_is_not_independent_of_gamma():
    """MAJOR-1: the old 'field' gradient path = 1.4244·|Γ| (the SAME Γ, NOT independent)."""
    for g in (1e-3, 0.1, 0.5, 1.0):
        f = field_from_phasor(complex(g), 0.3, y0=1.0)
        assert f["grad_rms_norm"] / g == pytest.approx(1.424354, rel=1e-4)


def test_ii_standing_wave_recovers_on_field_integrand(part2):
    """MAJOR-2: (ii) gated on the FIELD-INTEGRAND antinode (not the |Γ|=1 tautology)."""
    ii = part2["ii_standing"]
    assert ii["gamma_mag_short"] == pytest.approx(1.0, abs=1e-9)
    assert ii["T_antinode_field_analytic"] == pytest.approx(4.0, rel=1e-9)
    assert ii["T_antinode_field_grid"] == pytest.approx(4.0, rel=1e-3)
    assert ii["recovers_part1_law"] is True


# --------------------------------------------------------------------------
# The verdict + bin routing (SAME frozen bins, corrected observable)
# --------------------------------------------------------------------------
def test_verdict_is_radiation_contaminated(part2):
    """The honest re-run verdict is [RADIATION-CONTAMINATED]."""
    v = select_bin(part2)
    assert v["verdict"] == "RADIATION-CONTAMINATED"
    assert v["i_vanishes_in_T"] is False


def test_resonant_carrier_derived_bin_reachable():
    """[RESONANT-CARRIER-DERIVED] bin still reachable: synthetic (i)-vanishes hits it."""
    synthetic = {
        "i_matched": {"T_vanishes": True},
        "ii_standing": {"recovers_part1_law": True},
    }
    assert select_bin(synthetic)["verdict"] == "RESONANT-CARRIER-DERIVED"


def test_discriminator_underdetermined_bin_reachable():
    """[DISCRIMINATOR-UNDERDETERMINED] reachable: (i) vanishes but (ii) doesn't recover."""
    synthetic = {
        "i_matched": {"T_vanishes": True},
        "ii_standing": {"recovers_part1_law": False},
    }
    assert select_bin(synthetic)["verdict"] == "DISCRIMINATOR-UNDERDETERMINED"


# --------------------------------------------------------------------------
# DISCREPANT-HALT -- now a REAL value-reconcile of two independent ⟨T⟩ paths
# --------------------------------------------------------------------------
def test_reconcile_agrees_on_true_matched_line(part2):
    """The two genuinely-independent ⟨T⟩ paths agree on the real matched line."""
    assert part2["i_matched"]["T_bond_reconcile_rel"] < 1e-9


def test_discrepant_halt_fires_when_T_paths_diverge():
    """Synthetic trigger: the two ⟨T⟩ paths DIVERGE in value ⟹ HALT reachable.

    Now a VALUE reconcile (not a shared-boolean check on 1.4244·|Γ| twice). The 4th
    recurrence of the reconcile-gate defect is closed: this gate can genuinely disagree.
    """
    assert reconcile_matched_T(1.0, 2.0) is False        # divergent values
    assert reconcile_matched_T(1.0, 1.0 + 1e-6) is False  # beyond tol


def test_discrepant_halt_does_not_fire_when_T_paths_agree():
    """Equal ⟨T⟩ values reconcile (the gate is not trivially always-true/false)."""
    assert reconcile_matched_T(1.0, 1.0) is True
    assert reconcile_matched_T(1.0, 1.0 + 1e-12) is True


# --------------------------------------------------------------------------
# Positive controls + liveness (of BOTH the reflection instrument AND the ⟨T⟩ path)
# --------------------------------------------------------------------------
def test_positive_controls_all_pass():
    """All HALT-gated positive controls pass (incl. the new PC-gammafree liveness)."""
    pc = run_positive_controls()
    assert pc["ALL_PC_PASS"] is True


def test_pc_gammafree_liveness():
    """PC-gammafree-live: the Γ-free path CAN read a nonzero ⟨T⟩ (makes 'vanish' meaningful)."""
    pc = run_positive_controls()
    assert pc["PC_gammafree_live_ok"] is True
    assert pc["PC_gammafree_travel_T"] == pytest.approx(1.0, rel=1e-6)


def test_pc_reflect_is_liveness_positive_control():
    """PC-reflect proves the instrument reads a KNOWN reflecting wall (|Γ|=1)."""
    pc = run_positive_controls()
    assert pc["PC_reflect_ok"] is True
    assert pc["PC_matched_ok"] is True
    assert matched_line_reflection(0.3) < 1e-12
    assert reflecting_termination_reflection(0.3, "short") == pytest.approx(1.0, abs=1e-9)

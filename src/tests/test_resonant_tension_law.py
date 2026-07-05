"""Tests for the RESONANT time-averaged tension law + the radiation control.

Prereg (FROZEN): research/2026-07-04_resonant-tension-law_prereg_FROZEN.md.
Verdict: [RESONANT-CARRIER-DERIVED] -- Part 1 law derived (⟨T⟩=(k_a/ℓ)y0², ⟨sin²⟩=½
DERIVED) AND the make-or-break Part-2 radiation control passes: (i) the traveling wave
on the Ax3-matched line exerts NO time-averaged axial reaction (two INDEPENDENT paths),
while (ii) the standing wave between Γ=−1 reflecting terminations recovers the Part-1
tent-law ⟨T⟩. The plucking fork resolves: the matter arm's carrier is the confined
resonance.

These lock the LOAD-BEARING physics: the sympy backbone (⟨sin²⟩=½ + the ⟨T⟩ law,
exact-zero), the leading-vs-exact upper-bound relation, the matter re-band bands, the
Part-2 discriminator BOTH arms, the two-path reconcile, and -- critically -- the
DISCREPANT-HALT synthetic trigger (the reconcile-gate defect that recurred at
#521/#526/#527). T2 homonym guard: the resonance is the mechanical bow, never the
Cosserat winding.
"""
from __future__ import annotations

import numpy as np
import pytest

from scripts.vol_1_foundations.resonant_tension_law import (
    ARC_STAR_BAND,
    A_CORE_SQRT_ALPHA,
    DiscrepantHalt,
    axial_reaction_from_field,
    matched_line_reflection,
    part1_law_and_band,
    part2_radiation_control,
    reconcile_matched_reaction,
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
def part2():
    return part2_radiation_control()


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
# PART 1 -- the resonant tension law (leading + exact)
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


def test_leading_matches_exact_at_small_amplitude():
    """At tiny hum the leading law tracks the exact to O(y0²): <0.05% at y0=0.01."""
    y0 = 0.01
    rel = (resonant_tension_leading(y0) - resonant_tension_exact(y0)) \
        / resonant_tension_exact(y0)
    assert rel < 5e-4


def test_quadratic_breaks_at_elastica_edge():
    """The quadratic approximation breaks progressively: ~4% (tent) / ~36% (elastica)."""
    dev_tent = (resonant_tension_leading(0.1428) - resonant_tension_exact(0.1428)) \
        / resonant_tension_exact(0.1428)
    dev_elastica = (resonant_tension_leading(0.4153) - resonant_tension_exact(0.4153)) \
        / resonant_tension_exact(0.4153)
    assert 0.03 < dev_tent < 0.06
    assert 0.30 < dev_elastica < 0.40


# --------------------------------------------------------------------------
# PART 1 -- the matter re-band through the #526 remap
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
        # y0=0 anchor is the cold 9.7733; every y0>0 row must have SMALLER ρ'
        rp0 = rows[0]["rho_prime_exact"]
        assert rp0 == pytest.approx(9.7733, abs=1e-3)  # T→0 identity anchor
        for r in rows[1:]:
            assert r["rho_prime_exact"] < rp0, "tension must cap (lower) ρ'"


def test_op_point_is_sqrt_alpha(part1):
    """The A1 mass-core op-point is A=√α (read-off, Class-C echo; never tuned)."""
    assert part1["op_point"]["A_axial_sqrt_alpha"] == pytest.approx(A_CORE_SQRT_ALPHA)


def test_reband_interior_does_not_reach_rho_2(part1):
    """KNIFE: the re-banded interior ρ' band [~4.36, ~9.65] does NOT reach ρ'=2."""
    lo, hi = part1["matter_track"]["rho_prime_band_exact"]
    assert lo > 2.0, "no interior edge lands on the ρ'=2 canon crossing"


# --------------------------------------------------------------------------
# PART 2 -- the radiation control (make-or-break) BOTH arms
# --------------------------------------------------------------------------
def test_i_matched_line_reaction_vanishes(part2):
    """(i) traveling wave on the matched line: BOTH independent paths vanish."""
    i = part2["i_matched"]
    assert i["gamma_mag"] < 1e-9, "Γ-read path must vanish (matched line)"
    assert i["field_reaction_rms_norm"] < 1e-9, "field momentum-flux path must vanish"
    assert i["field_T_uniform"] is True
    assert i["vanishes"] is True


def test_ii_standing_wave_reaction_nonzero_and_recovers(part2):
    """(ii) standing wave: nonzero reaction that recovers the Part-1 tent-law ⟨T⟩."""
    ii = part2["ii_standing"]
    assert ii["gamma_mag_short"] == pytest.approx(1.0, abs=1e-9)  # Γ=−1 wall
    assert ii["nonzero"] is True
    assert ii["recovers_part1_law"] is True
    # antinode ⟨T⟩ = 4× the Part-1 unit law (constructive |Γ|=1)
    assert ii["T_antinode_field_short_analytic"] == pytest.approx(
        ii["T_antinode_expected_part1"], rel=1e-9)


def test_discriminator_is_real_matched_vs_reflecting():
    """The discriminator: matched Γ≈0 (traveling) vs reflecting |Γ|=1 (standing)."""
    assert matched_line_reflection(0.3) < 1e-12
    assert reflecting_termination_reflection(0.3, "short") == pytest.approx(1.0, abs=1e-9)
    assert reflecting_termination_reflection(0.3, "open") == pytest.approx(1.0, abs=1e-9)


def test_traveling_wave_field_is_uniform_standing_is_not():
    """The field integrand: traveling ⟨T⟩(x) uniform (grad=0) vs standing (grad≠0)."""
    trav = axial_reaction_from_field(0.0 + 0j, 0.3)        # Γ=0 traveling
    stand = axial_reaction_from_field(-1.0 + 0j, 0.3)      # Γ=−1 standing
    assert trav["is_uniform"] is True
    assert trav["net_axial_reaction_rms_norm"] < 1e-9
    assert stand["is_uniform"] is False
    assert stand["net_axial_reaction_rms_norm"] > 1e-3


# --------------------------------------------------------------------------
# The verdict + bin routing (no fall-through)
# --------------------------------------------------------------------------
def test_verdict_is_resonant_carrier_derived(part2):
    """The live verdict is [RESONANT-CARRIER-DERIVED]."""
    v = select_bin(part2)
    assert v["verdict"] == "RESONANT-CARRIER-DERIVED"
    assert v["i_vanishes"] and v["ii_recovers"] and v["ii_nonzero"]


def test_radiation_contaminated_bin_reachable():
    """[RADIATION-CONTAMINATED] bin is reachable: synthetic (i)-nonzero hits it."""
    synthetic = {
        "i_matched": {"vanishes": False},
        "ii_standing": {"recovers_part1_law": True, "nonzero": True},
    }
    assert select_bin(synthetic)["verdict"] == "RADIATION-CONTAMINATED"


def test_discriminator_underdetermined_bin_reachable():
    """[DISCRIMINATOR-UNDERDETERMINED] reachable: (i) vanishes but (ii) neither clean."""
    synthetic = {
        "i_matched": {"vanishes": True},
        "ii_standing": {"recovers_part1_law": False, "nonzero": True},
    }
    assert select_bin(synthetic)["verdict"] == "DISCRIMINATOR-UNDERDETERMINED"


# --------------------------------------------------------------------------
# DISCREPANT-HALT -- reachable AND triggers on synthetic input (the recurring gap)
# --------------------------------------------------------------------------
def test_reconcile_agrees_on_true_matched_line(part2):
    """On the real matched line both paths vanish ⟹ reconcile agrees (no HALT)."""
    assert part2["reconcile"]["agree"] is True
    assert part2["reconcile"]["both_vanish"] is True


def test_discrepant_halt_fires_when_paths_disagree():
    """Synthetic trigger: one path vanishes while the other does not ⟹ HALT reachable.

    This is the reconcile-gate defect that recurred at #521/#526/#527 -- the gate MUST
    be able to fire, proven here on hand-mismatched inputs.
    """
    # Γ-read says vanished (0), field path says NOT vanished (1.0) -> disagree
    assert reconcile_matched_reaction(0.0, 1.0) is False
    # and the disagreement is symmetric
    assert reconcile_matched_reaction(1.0, 0.0) is False


def test_discrepant_halt_does_not_fire_when_paths_agree():
    """Both-vanish and both-nonzero are consistent ⟹ no HALT (the gate is not trivial)."""
    assert reconcile_matched_reaction(1e-18, 1e-15) is True   # both vanish
    assert reconcile_matched_reaction(1.0, 1.0) is True        # both nonzero


# --------------------------------------------------------------------------
# Positive controls + liveness
# --------------------------------------------------------------------------
def test_positive_controls_all_pass():
    """All HALT-gated positive controls pass (incl. PC-reflect liveness)."""
    pc = run_positive_controls()
    assert pc["ALL_PC_PASS"] is True


def test_pc_reflect_is_liveness_positive_control():
    """PC-reflect proves the discriminator instrument reads a KNOWN reflecting wall.

    The (i)→0 null is only bookable because the SAME cascade_gamma reads |Γ|=1 on the
    known reflecting case (ave-prereg Step 3.8a liveness).
    """
    pc = run_positive_controls()
    assert pc["PC_reflect_ok"] is True
    assert pc["PC_reflect_gamma_short"] == pytest.approx(1.0, abs=1e-9)
    assert pc["PC_matched_ok"] is True
    assert pc["PC_matched_gamma_mag"] < 1e-12

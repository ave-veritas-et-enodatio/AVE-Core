"""Tests for the channel-resolved loading discriminator.

Prereg (FROZEN): research/2026-07-05_channel-resolved-loading_prereg_FROZEN.md.

VERDICT: **[ASYMMETRIC-BOTH]** — both a matched CW traveling wave and a confined Γ=−1
standing mode MOVE ρ' via the transverse hum, by an INDISTINGUISHABLE amount (hum_factor
diff ≤ machine ε). The #526 +T/ℓ denominator remap moves ρ' for the traveling wave too,
which CONFLICTS with canon's #518 §7 radiation null (S_axial=S_shear ⟹ ρ invariant). The
conflict is surfaced verbatim (flag-don't-fix), NOT resolved. The only travel/confined
difference is the constant numerator DC-bias S(√α) — the pre-existing #518 matter operating
point, NOT a hum discriminator.

These lock the LOAD-BEARING physics: the 9 sympy exact-zero residuals (incl. the axial-4th-
order numerator-untouched proof and the A_y=1/2 cancellation KNIFE tell), the hum-factor-
identical finding (the carrier is not a discriminator), the [ASYMMETRIC-BOTH] verdict, the
#529 uniform-⟨T⟩ consistency reproduction, the 5 positive controls, and the mandatory
synthetic DISCREPANT-HALT / DeadGate triggers on the #528 reconcile-gate (can-fire proofs).

Grant 2026-07-05 (Q-point ruling): S keyed on DEFORMATION not stress; no-double-count.
T2 homonym guard (#527): the resonance is the mechanical bow, never the Cosserat winding.
"""
from __future__ import annotations

import numpy as np
import pytest

from ave.axioms.scale_invariant import saturation_factor
from ave.validation.reconcile_gate import DeadGateError, DiscrepantHalt, ReconcileGate
from scripts.vol_1_foundations.channel_resolved_loading import (
    A_CORE_SQRT_ALPHA,
    A_Y,
    RHO_COLD,
    channel_loading,
    consistency_gate_529,
    rho_prime_both_arms,
    rho_prime_both_cases,
    run_positive_controls,
    select_bin,
    symbolic_backbone,
)
from scripts.vol_1_foundations.srs_elastic_tensor import srs_primitive


@pytest.fixture(scope="module")
def geom():
    return srs_primitive("right")


@pytest.fixture(scope="module")
def arms(geom):
    pos, bonds, rho = geom
    return rho_prime_both_arms(pos, bonds, rho)


@pytest.fixture(scope="module")
def cases(arms):
    # legacy fixture: the EXTENDED arm (this arc's re-keying) -- the [ASYMMETRIC-BOTH] arm
    return arms["EXTENDED"]


# --------------------------------------------------------------------------------------
# S1 -- the symbolic backbone (every 2nd-order term, exact-zero residuals)
# --------------------------------------------------------------------------------------
def test_symbolic_backbone_all_exact_zero():
    r = symbolic_backbone()
    assert r["residuals_all_zero"], r["residuals"]


def test_denominator_does_not_cancel_at_canonical_yield():
    """dD/k0 = +3/4 y0^2 at A_y=1 (the geometric stiffening dominates the saturation softening 4:1)."""
    r = symbolic_backbone()
    assert r["residuals"]["dD_over_k0_D1_at_Ay1"] == "0"  # the +3/4 y0^2 form is exact


def test_cancellation_requires_Ay_half_the_knife_tell():
    """Cancellation of the denominator requires A_y=1/2 -- NOT the canonical yield. This is the
    KNIFE tell: a cancellation at A_y=1/2 would be the imported yield in a costume, not a theorem."""
    r = symbolic_backbone()
    assert r["residuals"]["cancellation_requires_Ay_half"] == "0"


def test_axial_deformation_oscillation_is_4th_order():
    """Numerator S_axial is untouched by a ⟨A⟩=0 transverse wave: the axial deformation OSCILLATION
    variance is 4th-order in y0 (Grant consequence 1, no-double-count)."""
    r = symbolic_backbone()
    assert r["residuals"]["axial_osc_variance_is_4th_order"] == "0"


# --------------------------------------------------------------------------------------
# S2 -- per-channel loading + the hum-factor-identical finding
# --------------------------------------------------------------------------------------
def test_numerator_untouched_by_travelling_hum():
    """S_axial does NOT depend on y0 for the traveling wave (A_dc=0): stays cold=1 at every hum."""
    for y0 in (0.0, 0.05, 0.1428, 0.42):
        cl = channel_loading(y0, A_dc=0.0, dictionary="D1_angle")
        assert cl["S_axial_numerator"] == pytest.approx(1.0)


def test_confined_numerator_is_biased_cold_not_the_hum():
    """The confined mode's numerator is S(√α) (the DC bias), y0-independent -- the hum does NOT move it."""
    S_dc = float(saturation_factor(A_CORE_SQRT_ALPHA, yield_limit=A_Y))
    for y0 in (0.0, 0.1428, 0.42):
        cl = channel_loading(y0, A_dc=A_CORE_SQRT_ALPHA, dictionary="D1_angle")
        assert cl["S_axial_numerator"] == pytest.approx(S_dc)


def test_denominator_has_both_competing_terms():
    """The denominator carries soft (k_s·S, <1) AND stiff (+T/ℓ, >0) at nonzero hum."""
    cl = channel_loading(0.1428, A_dc=0.0, dictionary="D1_angle")
    assert cl["k_shear_soft"] < 1.0      # softening
    assert cl["T_over_ell_stiff"] > 0.0  # stiffening
    # net: stiffening dominates (denominator > 1 -> rho' < 1)
    assert cl["k_shear_eff_denominator"] > 1.0
    assert cl["rho_prime"] < 1.0


def test_hum_factor_identical_travel_vs_confined():
    """THE CENTRAL FINDING: the y0-dependent hum factor of ρ' is bit-identical between travel and
    confined (the hum is NOT a discriminator; the only difference is the constant numerator S(√α))."""
    S_dc = float(saturation_factor(A_CORE_SQRT_ALPHA, yield_limit=A_Y))
    for y0 in (0.05, 0.1428, 0.42):
        trav = channel_loading(y0, 0.0, "D1_angle")["rho_prime"] / RHO_COLD
        conf = channel_loading(y0, A_CORE_SQRT_ALPHA, "D1_angle")["rho_prime"] / S_dc
        assert trav == pytest.approx(conf, abs=1e-14)


def test_dictionaries_coincide_at_ell_one():
    """On srs ℓ=1 the two y0↔A_shear dictionaries coincide (they diverge only if ℓ≠1)."""
    d1 = channel_loading(0.1428, 0.0, "D1_angle")["rho_prime"]
    d2 = channel_loading(0.1428, 0.0, "D2_displacement")["rho_prime"]
    assert d1 == pytest.approx(d2)


# --------------------------------------------------------------------------------------
# S3 -- the #529 uniform-<T> consistency reproduction (pump-null constraint)
# --------------------------------------------------------------------------------------
def test_consistency_reproduces_529_uniform_T(geom):
    """Before going channel-resolved, the per-bond scalar ⟨T⟩ reconciles with the #529 Γ-free ABCD
    field to rtol=1e-9 (my stiff term = the traveling-wave field's ⟨T⟩ = (k_a/ℓ)y0²)."""
    pos, bonds, rho = geom
    r = consistency_gate_529(pos, bonds, rho, theta=0.3, y0=1.0)
    assert r["reconciled"] is True
    assert r["can_fire_proven"] is True
    assert r["max_rel_discrepancy"] < 1e-9


# --------------------------------------------------------------------------------------
# S4/S6 -- the verdict (EXTENDED arm; the DC_ONLY arm + the fork are below)
# --------------------------------------------------------------------------------------
def test_both_cases_hum_move_rho_prime_extended(cases):
    """[EXTENDED arm] Both travel and confined HUM-move ρ' (not preserved) -- under this arc's
    AC-cycle-averaged re-keying the traveling wave is NOT ratio-preserving."""
    v = select_bin(cases)
    assert v["arm"] == "EXTENDED"
    assert v["travel_hum_move"] > v["tol"]
    assert v["confined_hum_move"] > v["tol"]


def test_hum_factor_identity_is_by_construction(cases):
    """[EXTENDED arm] The hum responses are identical BY CONSTRUCTION, not by measurement: ρ' =
    S_axial · [1/(k_s·S_shear + T/ℓ)], and S_axial is a CONSTANT (the DC bias) that divides out of
    the hum factor. The shared denominator (same S_shear, same T for both wave types under this arm)
    forces hum_factor_travel ≡ hum_factor_confined. The ≤1.1e-16 is machine round-off on an ALGEBRAIC
    identity -- NOT a measured null (item 5a). We assert it lands at round-off, and label it so."""
    v = select_bin(cases)
    assert v["hum_factor_max_diff_travel_vs_confined"] < 1e-13  # algebraic identity ⇒ round-off only


def test_verdict_extended_arm_is_asymmetric_both(cases):
    """[EXTENDED arm] The frozen routing lands [ASYMMETRIC-BOTH]: both HUM-move, indistinguishably."""
    v = select_bin(cases)
    assert v["bin"] == "ASYMMETRIC-BOTH"


def test_dictionary_does_not_flip_verdict(cases):
    v = select_bin(cases)
    assert v["dictionary_verdict_flips"] is False


# --------------------------------------------------------------------------------------
# THE T-SLOT SCOPE FORK -- both arms (Grant's to resolve; we report both, do NOT pick)
# --------------------------------------------------------------------------------------
def test_dc_only_arm_radiation_preserves_rho_exactly():
    """[DC_ONLY arm, canon keying] a pure-AC ⟨A⟩=0 traveling wave loads NOTHING: T=Φ'(0)=0 and no DC
    S-shift, so ρ'=ρ_cold EXACTLY at every hum amplitude (radiation transparent)."""
    for y0 in (0.0, 0.1428, 0.42):
        cl = channel_loading(y0, A_dc=0.0, dictionary="D1_angle", arm="DC_ONLY")
        assert cl["rho_prime"] == pytest.approx(1.0, abs=1e-14)
        assert cl["T_over_ell_stiff"] == pytest.approx(0.0, abs=1e-14)  # canon keying: T=Phi'(0)=0


def test_dc_only_arm_hum_enters_nothing():
    """[DC_ONLY arm] the confined mode's ρ' is y0-INDEPENDENT: the hum (an AC quantity) cannot enter
    the DC-scoped slot; only the static DC bias Φ'(√α) loads (legitimately in-slot, y0-independent)."""
    base = channel_loading(0.0, A_CORE_SQRT_ALPHA, "D1_angle", arm="DC_ONLY")["rho_prime"]
    for y0 in (0.0, 0.1428, 0.42):
        cl = channel_loading(y0, A_dc=A_CORE_SQRT_ALPHA, dictionary="D1_angle", arm="DC_ONLY")
        assert cl["rho_prime"] == pytest.approx(base, abs=1e-14)  # NO hum dependence


def test_dc_only_verdict_is_symmetric_both(arms):
    """[DC_ONLY arm] the HUM moves neither wave type -> [SYMMETRIC-BOTH] at the hum level (carrier
    family dead; matter/radiation split = #518's DC S-ratio asymmetry alone)."""
    v = select_bin(arms["DC_ONLY"])
    assert v["arm"] == "DC_ONLY"
    assert v["travel_hum_move"] == pytest.approx(0.0, abs=1e-12)
    assert v["confined_hum_move"] == pytest.approx(0.0, abs=1e-12)
    assert v["bin"] == "SYMMETRIC-BOTH"


def test_dc_only_confined_dc_bias_matches_bond_tension():
    """[DC_ONLY arm] the confined mode's in-slot tension is exactly canon's keying T=bond_tension(√α)
    (Φ'(√α)), proving the DC_ONLY slot uses canon's own tension function, not a re-keyed AC average."""
    from scripts.vol_1_foundations.prestress_elastic_tensor import bond_tension
    cl = channel_loading(0.1428, A_dc=A_CORE_SQRT_ALPHA, dictionary="D1_angle", arm="DC_ONLY")
    assert cl["T_stiff"] == pytest.approx(float(bond_tension(A_CORE_SQRT_ALPHA)))


def test_fork_arms_give_opposite_verdicts(arms):
    """The two arms of the T-slot scope fork give OPPOSITE verdicts -- which is why the fork is
    load-bearing and Grant's to resolve, not ours to pick."""
    dc = select_bin(arms["DC_ONLY"])["bin"]
    ext = select_bin(arms["EXTENDED"])["bin"]
    assert dc == "SYMMETRIC-BOTH"
    assert ext == "ASYMMETRIC-BOTH"
    assert dc != ext


def test_identity_endpoints_excluded_from_moved_band(cases):
    """The y0→0 identity rows are LABELED and excluded; the reported interior band excludes them."""
    rows = cases["i_travel"]["per_dictionary"]["D1_angle"]["hi_tent"]["rows"]
    identity_rows = [r for r in rows if r["is_identity_limit"]]
    assert identity_rows  # at least the y0=0 row is labeled
    # the labeled identity row is at (or approaching) rho'=1 (the unstressed cold point)
    assert identity_rows[0]["rho_prime"] == pytest.approx(1.0, abs=1e-3)


# --------------------------------------------------------------------------------------
# S5 -- positive controls (all via the #528 helper, can-fire proven)
# --------------------------------------------------------------------------------------
def test_all_positive_controls_pass(geom):
    pos, bonds, rho = geom
    pc = run_positive_controls(pos, bonds, rho)
    assert pc["all_passed"] is True


def test_cold_recovery_exact(geom):
    """y0→0 recovers cold exactly (travel→ρ_cold=1)."""
    pos, bonds, rho = geom
    pc = run_positive_controls(pos, bonds, rho)
    assert pc["PC_cold"]["rho_prime_at_y0_zero"] == pytest.approx(1.0, abs=1e-10)


def test_numerator_shifted_off_cold(geom):
    """PC-numerator: the confined S_axial is genuinely shifted off cold (not a blind 1.0)."""
    pos, bonds, rho = geom
    pc = run_positive_controls(pos, bonds, rho)
    assert pc["PC_numerator"]["is_shifted_off_cold"] is True


def test_null_liveness_confined_reads_biased_ratio(geom):
    """PC-null-liveness (Step 3.8a): the confined pipeline reads the biased ratio ≠ ρ_cold through
    the IDENTICAL remap -- the preservation-null's known-nonzero positive control."""
    pos, bonds, rho = geom
    pc = run_positive_controls(pos, bonds, rho)
    assert pc["PC_null_liveness"]["reads_nonzero_shift"] is True
    S_dc = float(saturation_factor(A_CORE_SQRT_ALPHA, yield_limit=A_Y))
    assert pc["PC_null_liveness"]["confined_rho_prime_y0_zero"] == pytest.approx(S_dc)


# --------------------------------------------------------------------------------------
# The mandatory synthetic DISCREPANT-HALT / DeadGate triggers (can-fire on real data paths)
# --------------------------------------------------------------------------------------
def test_reconcile_gate_fires_on_synthetic_discrepancy():
    """A hand-mismatched (claimed, independent) pair MUST fire DiscrepantHalt through the SAME
    comparator+halt path the live gates use (the #521/#526/#527 dead-gate defect cannot recur)."""
    gate = ReconcileGate(label="synthetic-mismatch", claimed=1.0, independent=2.0, rtol=1e-9)
    with pytest.raises(DiscrepantHalt):
        gate.enforce(prove_first=True)


def test_reconcile_gate_can_fire_proven_on_consistency_path(geom):
    """The consistency gate's can-fire self-test is proven on its REAL data pair (not a toy)."""
    pos, bonds, rho = geom
    r = consistency_gate_529(pos, bonds, rho)
    assert r["can_fire_proven"] is True


def test_dead_gate_detected_for_vacuous_tolerance():
    """A gate registered with a non-finite tolerance is refused at construction (a checklist by
    construction) -- proving the #528 helper rejects vacuous gates."""
    with pytest.raises(ValueError):
        ReconcileGate(label="vacuous", claimed=1.0, independent=1.0, rtol=float("inf"))


def test_prove_can_fire_raises_dead_gate_on_equal_reference():
    """prove_can_fire on an exact-equality gate (rtol=atol=0) still injects a nonzero corruption and
    fires -- if it did NOT, DeadGateError would raise. Here it fires cleanly (gate is live)."""
    gate = ReconcileGate(label="exact", claimed=3.0, independent=3.0, rtol=0.0, atol=0.0)
    res = gate.prove_can_fire()  # must NOT raise DeadGateError -- the corruption fires the halt
    assert res.can_fire_proven is True


# --------------------------------------------------------------------------------------
# T2 homonym guard (#527) + knife
# --------------------------------------------------------------------------------------
def test_only_derived_half_quarter_factors_enter():
    """The ½ (⟨sin²⟩) and ¼ (soft term from S-Taylor) are DERIVED; the ¾ in dD is 1−¼ (derived).
    No un-derived ½/¼ enters (the residuals prove the forms)."""
    r = symbolic_backbone()
    # the soft term's ¼ and the dD's ¾ are locked by exact-zero residuals
    assert r["residuals"]["soft_D1_minus_form"] == "0"
    assert r["residuals"]["dD_over_k0_D1_at_Ay1"] == "0"


def test_no_landing_on_visible_knife_targets(cases):
    """No interior ρ' band edge lands on a visible knife target (2, 9.7734, 7.10, 11.68). The bands
    sit in (0.88, 1.0) -- well away from every armed target (the move is a small stiffening, not a
    chord-shaped landing)."""
    for name in ("i_travel", "ii_confined"):
        band = cases[name]["per_dictionary"]["D1_angle"]["hi_tent"]["interior_rho_prime_range"]
        lo, hi = band
        for target in (2.0, 9.7734, 7.10, 11.68):
            assert not (lo <= target <= hi)

"""Regression gate for the Witten-via-body-angular-momentum dressing result
(2026-06-23; research/2026-06-23_witten-angular-momentum-charge_result.md).

Locks: (1) the tool is interpretable (validate-on-known recovers the electron
INTEGER charge with zero dressing); (2) the RECONCILIATION-IN-FORM finding (the
integer linking 𝒬 is invariant under a rigid body-frame rotation, so a separate
body angular momentum CAN dress it); (3) the load-bearing CAVEAT (the q-poloidal
winding is a FACTOR in the linking, so it is NOT the separate frame rotation);
(4) the NEGATIVE chord verdict (denominator 3 is the observed proton loop count
fed in, NOT forced — same free dial Lane D #393 caught). Rule 11 honest-closure:
a future debug-toward-rescue cannot silently flip the chord verdict without
tripping this gate.
"""
from __future__ import annotations

from scripts.vol_2_subatomic.witten_angmom_charge import (
    c1_denominator_forcing,
    r1_separability,
    run,
    validate_on_known,
)


def test_validate_on_known_recovers_electron_integer_charge():
    """The brief's required validate-on-known: recover the electron integer
    charge. Hopf link recovers, (2,3) self-links to the integer, sign=chirality,
    and with ZERO dressing the lepton charge is an exact integer."""
    k = validate_on_known()
    assert k["HALT"] is False
    assert abs(k["hopf_link"]) == 1.0
    assert k["electron_single_component"] is True
    assert k["electron_self_linking_int"] == -6  # p*q signed
    assert k["sign_flips_with_handedness"]
    # zero θ-dressing → integer charge exactly (the reconciliation's base case)
    assert k["electron_q_eff_zero_dressing"] == float(k["electron_self_linking_int"])


def test_linking_integer_invariant_under_rigid_frame_rotation():
    """R1: a genuine SEPARATE body angular momentum (rigid frame rotation of the
    whole soliton) leaves the linking integer 𝒬 fixed — so the dressing picture
    is structurally possible (𝒬 fundamental, 𝒥 can dress it)."""
    r1 = r1_separability()
    assert r1["linking_invariant_under_rigid_frame_rotation"] is True
    assert all(rw["linking_int"] == r1["base_linking_int"]
               for rw in r1["frame_rotation_sweep"])
    assert r1["reconciliation_structurally_possible"] is True


def test_q_poloidal_winding_is_inside_the_linking_not_separate():
    """The load-bearing CAVEAT: the q-poloidal winding (which carries spin) is a
    FACTOR in the charge linking (Q_H = p*q): q=3→6, q=5→10. So the q-winding is
    NOT the separate frame rotation; the dressing 𝒥 must be the rigid frame DOF,
    not the internal q-lap. This keeps the reconciliation honest."""
    r1 = r1_separability()
    assert r1["self_linking_q3"] == -6
    assert r1["self_linking_q5"] == -10
    assert r1["q_poloidal_winding_is_a_factor_in_linking"] is True


def test_denominator_3_is_fed_in_not_forced():
    """C1 (the decider): the per-constituent angular-momentum share is 1/N by
    symmetry for ANY N; the substrate EXCLUDES no N. So denominator-3 is the
    OBSERVED proton loop count fed in — NOT a chord. Same free dial Lane D
    #393 caught (ℤ_N → 1/N for any N)."""
    c1 = c1_denominator_forcing()
    for row in c1["rows"]:
        assert row["fractional_charge_denominator"] == row["N"]
        assert row["substrate_excludes_this_N"] is False
    assert c1["three_is_forced_by_substrate"] is False
    assert c1["three_is_the_observed_proton_loop_count_fed_in"] is True


def test_verdicts_locked_reconciled_in_form_but_no_chord():
    """Lock the headline verdicts: reconciliation succeeds IN FORM, but the
    denominator-3 is FIT (not a chord) and up/down is FIT. A rescue flipping the
    chord verdict must update the result doc and trip this gate deliberately."""
    v = run()["VERDICTS"]
    assert v["reconciliation"] == "RECONCILED-IN-FORM"
    assert v["denominator_3"] == "effective-reconciliation-but-3-still-FIT"
    assert v["up_down"] == "FIT"
    # belt-and-suspenders: no verdict claims a chord on the forcing question
    assert "CHORD" not in v["denominator_3"]

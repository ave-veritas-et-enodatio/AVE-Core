"""Regression gate for the winding charge-closure refute-by-default result
(Lane D, 2026-06-23; research/2026-06-23_winding-charge-quantization_result.md).

Locks the NEGATIVE verdicts so a future debug-toward-rescue cannot silently
flip a FIT/ECHO to a CHORD without tripping this gate (Rule 11 honest-closure).
"""
from __future__ import annotations

from scripts.vol_2_subatomic.winding_charge_closure import (
    closes_as_single_component,
    main,
    self_linking_pushoff,
    validate_on_known,
)


def test_validate_on_known_no_halt():
    """The tool must be interpretable: Hopf link recovers, electron (2,3)
    self-links to the integer, sign flips with handedness."""
    k = validate_on_known()
    assert k["HALT"] is False
    assert abs(k["hopf_link"]) == 1.0
    assert k["electron_single_component"] is True
    assert round(k["electron_self_linking_raw"]) == -6  # p*q = 6, signed
    assert k["sign_flips_with_handedness"]


def test_p1_carries_unit_charge_so_p2_is_not_forced():
    """The decisive PART-1 refutation: a p=1 unknot carries integer charge.
    (1,1) closes as one component and self-links to 1 -> the substrate does
    NOT forbid p=1, so p=2 is minimality (FIT), not a charge-closure forcing."""
    assert closes_as_single_component(1, 1) is True
    assert round(self_linking_pushoff(1, 1)) == -1  # unit charge at p=1
    assert round(self_linking_pushoff(1, 3)) == -3   # p=1 still closes to integer


def test_zN_gives_one_over_N_so_denominator_3_not_forced():
    """The Z_N theta-vacuum construction gives denominator N for ANY N;
    N=3 is the observed proton loop count, not forced."""
    out = main()
    table = out["part2_quark_closure"]["Q2_denominator_table"]
    for N_str, row in table.items():
        assert row["denominator"] == int(N_str)
    assert out["part2_quark_closure"]["Q2_denominator_3_forced"] is False


def test_headline_verdicts_are_refute_by_default():
    """Lock the four per-result verdicts as NEGATIVE (FIT/ECHO or CONSISTENCY).
    No CHORD. A rescue that flips any of these must update the result doc and
    trip this gate deliberately."""
    v = main()["RESULT_VERDICTS"]
    assert v["electron_p"].startswith("FIT/ECHO")
    assert v["quark_denominator_3"].startswith("FIT/ECHO")
    assert v["confinement"].startswith("CONSISTENCY")
    assert v["up_down_split"].startswith("FIT/ECHO")
    # Belt-and-suspenders: no verdict claims a chord.
    assert not any("CHORD" in val for val in v.values())

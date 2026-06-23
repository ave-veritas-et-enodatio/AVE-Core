"""test_bench_model.py — the channel-agnostic BenchModel spine (GAP-1).

Exercises ave.bench.model: the 8-gate bankability record + the Fork-2 graded
ladder verdict. Tests use SYNTHETIC specs (hermetic, fast — no channel physics)
to pin each gate evaluator and each verdict tier. The REAL reference adopters
(birefringence + cRIO) are tested in test_bench_adopters.py.

Style mirrors test_ave_bench.py: `import ave.bench as bench`, class-organized.
"""

from __future__ import annotations

import json

import numpy as np
import pytest

import ave.bench as bench
from ave.bench.model import (
    AxisTag,
    BenchSpec,
    BindingSpec,
    ChordEcho,
    CorpusState,
    DimensionalIngredient,
    DiscriminatorAxis,
    EvidenceFraming,
    GateStatus,
    InterpretiveAlternative,
    LedgerAspect,
    LedgerRow,
    LedgerStatus,
    OutcomeKind,
    Prereg,
    SensitivitySpec,
    SharedWith,
    ValidateOnKnownSpec,
    Verdict,
    run_bench_model,
)

IA = InterpretiveAlternative


# ============================================================================
# Spec builders — minimal valid declarations, overridable per-test.
# ============================================================================
def _ledger(mag_status=LedgerStatus.DERIVED, mag_sm_also=True, asserted=False, drop=None):
    rows = [
        LedgerRow(LedgerAspect.COUPLING, LedgerStatus.DERIVED, "constants.py:471", sm_also=True),
        LedgerRow(LedgerAspect.PROBE, LedgerStatus.ENGINEERING_CHOICE, "polarimeter (apparatus)", sm_also=True),
        LedgerRow(
            LedgerAspect.MAGNITUDE,
            mag_status,
            "alpha-echo both sides" if mag_status is not LedgerStatus.DERIVED else "derived file:line",
            sm_also=mag_sm_also,
        ),
        LedgerRow(LedgerAspect.OBSERVABLE, LedgerStatus.DERIVED, "vacuum-birefringence-e4.md", sm_also=False),
    ]
    if asserted:
        rows[0] = LedgerRow(LedgerAspect.COUPLING, LedgerStatus.ASSERTED, "FLAG: ungrounded coupling", sm_also=False)
    if drop is not None:
        rows = [r for r in rows if r.aspect is not drop]
    return tuple(rows)


def _prereg(magnitude=False, frozen=True, with_inconclusive=True):
    outcomes = [(OutcomeKind.POSITIVE, "a"), (OutcomeKind.NEGATIVE, "b")]
    if with_inconclusive:
        outcomes.append((OutcomeKind.INCONCLUSIVE, "c"))
    return Prereg(
        ref="research/some_prereg_FROZEN.md",
        frozen=frozen,
        corpus_state=CorpusState.PARTIAL,
        prior_work_refs=("vacuum-birefringence-e4.md:24",),
        prediction="AVE diverges from the counterpart",
        rationale="tree-vs-loop structure",
        discriminating_outcomes=tuple(outcomes),
        falsifier="no divergence on the swept grid",
        expected_magnitude_eval=(
            (DimensionalIngredient("alpha", 7.2973525693e-3, "constants.py:154"),) if magnitude else ()
        ),
    )


def _framing(gating_axis="rotation", n_displayed=5, n_total=5, omitted=()):
    return EvidenceFraming(
        gating_axis=gating_axis,
        non_gating_axes=("aux",),
        binding_spec=BindingSpec.SINGLE_SHOT,
        verifiability_class=bench.VerifiabilityClass.A_DIRECT,
        verification_artifact_ref="closed-form",
        n_displayed=n_displayed,
        n_total_run=n_total,
        omitted_instances=omitted,
    )


_VOK = ValidateOnKnownSpec("PVLAS A_e", 1.32e-24, 1.32e-24, 1e-6, inconclusive_bin="within 3x floor -> UNRESOLVED")
_ROBUST_SENS = SensitivitySpec(
    observable_of=lambda **k: 1.0, param_grids={"L": (0.1, 0.2, 0.3)}, verdict_fn=lambda o: o > 0.5
)


def _zero_vs_nonzero_spec(**over):
    """Optical-activity-shaped spec: QED == 0, AVE != 0 -> fully BANKABLE."""
    base = dict(
        name="zero-vs-nonzero",
        channel="EM-photon",
        ave_observable=lambda E: 75.0 * E,
        sm_observable=lambda E: 0.0,
        sweep_grid=np.array([1.0, 2.0, 3.0]),
        validate_on_known=_VOK,
        ledger_rows=_ledger(),
        axis_tags=(
            AxisTag(
                "rotation",
                ChordEcho.CHORD,
                ChordEcho.ECHO,
                DiscriminatorAxis.ZERO_VS_NONZERO,
                SharedWith.NONE,
                is_gating_axis=True,
                calibration_free=False,
                interpretive_alternatives=(IA.FLOOR, IA.COINCIDENCE, IA.EXACT),
                rationale="parity-odd, QED identically zero",
            ),
        ),
        prereg=_prereg(False),
        evidence_framing=_framing("rotation"),
        sensitivity=_ROBUST_SENS,
        is_physics_test=True,
        magnitude_is_claimed=False,
    )
    base.update(over)
    return BenchSpec(**base)


def _shared_form_ratio_spec(**over):
    """Birefringence-shaped spec: shared E^2 FORM, RATIO discriminator, magnitude
    is an alpha-echo, rescued by a tree-vs-loop FORM chord -> BANKABLE_AS_DISCRIMINATOR."""
    base = dict(
        name="shared-form-ratio",
        channel="EM-photon",
        ave_observable=lambda E: 1.93e7 * E**2,
        sm_observable=lambda E: 1.0 * E**2,
        sweep_grid=np.array([1.0, 2.0, 3.0]),
        validate_on_known=_VOK,
        ledger_rows=_ledger(mag_status=LedgerStatus.ENGINEERING_CHOICE, mag_sm_also=True),
        axis_tags=(
            AxisTag(
                "coefficient-ratio",
                ChordEcho.CHORD,
                ChordEcho.ECHO,
                DiscriminatorAxis.RATIO,
                SharedWith.FORM,
                is_gating_axis=True,
                calibration_free=False,
                interpretive_alternatives=(IA.APPROX_WITH_RESIDUAL, IA.COINCIDENCE, IA.FLOOR),
                rationale="tree-vs-loop chord; magnitude an alpha-echo",
            ),
            AxisTag(
                "tree-vs-loop-form",
                ChordEcho.CHORD,
                ChordEcho.CHORD,
                DiscriminatorAxis.SLOPE,
                SharedWith.NONE,
                is_gating_axis=False,
                calibration_free=True,
                rationale="structural tree-vs-loop FORM-within-form",
            ),
        ),
        prereg=_prereg(magnitude=True),
        evidence_framing=_framing("coefficient-ratio"),
        sensitivity=_ROBUST_SENS,
        is_physics_test=True,
        magnitude_is_claimed=True,
        result_is_numerical=False,
    )
    base.update(over)
    return BenchSpec(**base)


def _pilot_spec(**over):
    """cRIO-shaped validate-on-known pilot: is_physics_test=False -> VALIDATE_ON_KNOWN_*."""
    base = dict(
        name="cRIO C_eff(V) pilot",
        channel="EE-capacitance",
        ave_observable=lambda V: 1.0,
        sm_observable=lambda V: 1.0,
        sweep_grid=np.array([1.0, 2.0]),
        validate_on_known=ValidateOnKnownSpec(
            "X7R MLCC datasheet C-V", 0.95, 1.0, 0.15, inconclusive_bin="within 3x drift floor -> UNRESOLVED (BIN1)"
        ),
        ledger_rows=_ledger(),
        axis_tags=(
            AxisTag(
                "dC/dV sign",
                ChordEcho.MIXED,
                ChordEcho.ECHO,
                DiscriminatorAxis.MAGNITUDE,
                SharedWith.FORM,
                is_gating_axis=True,
                calibration_free=False,
                interpretive_alternatives=(IA.FLOOR, IA.COINCIDENCE, IA.STRATIFICATION),
                rationale="GAP-6 Branch-R/F sign tension",
            ),
        ),
        prereg=_prereg(False),
        evidence_framing=_framing("dC/dV sign"),
        sensitivity=None,
        is_physics_test=False,
        regime_note="deep Regime I, per-node A0 ~ 1e-11",
    )
    base.update(over)
    return BenchSpec(**base)


# ============================================================================
# The four verdict tiers.
# ============================================================================
class TestVerdictTiers:
    def test_bankable_zero_vs_nonzero(self):
        r = run_bench_model(_zero_vs_nonzero_spec())
        assert r.verdict is Verdict.BANKABLE
        assert r.hard_gates_pass
        assert r.g3.sm_identically_zero
        assert r.g3.shared_with is SharedWith.NONE

    def test_bankable_as_discriminator_shared_form_ratio(self):
        r = run_bench_model(_shared_form_ratio_spec())
        assert r.verdict is Verdict.BANKABLE_AS_DISCRIMINATOR
        assert r.hard_gates_pass
        # field-independent ratio recovered as the constant value
        assert r.g3.field_independent
        assert r.g3.ratio_value == pytest.approx(1.93e7, rel=1e-9)
        # rescued by the independent FORM-within-form chord
        assert r.g3.non_discriminating_on_shared_axis
        assert r.g3.has_independent_form_chord

    def test_validate_on_known_pass_pilot(self):
        r = run_bench_model(_pilot_spec())
        assert r.verdict is Verdict.VALIDATE_ON_KNOWN_PASS
        assert not r.is_physics_test
        assert r.g5 is None  # bankability sensitivity N/A for a pilot
        assert "Regime I" in r.regime_note

    def test_validate_on_known_fail_pilot(self):
        # computed 0.5 vs reference 1.0 at tol 0.15 -> fails recovery
        r = run_bench_model(
            _pilot_spec(validate_on_known=ValidateOnKnownSpec("X7R MLCC C-V", 0.5, 1.0, 0.15, inconclusive_bin="BIN1"))
        )
        assert r.verdict is Verdict.VALIDATE_ON_KNOWN_FAIL


# ============================================================================
# G1 — validate-on-known.
# ============================================================================
class TestG1:
    def test_pass(self):
        r = run_bench_model(_zero_vs_nonzero_spec())
        assert r.g1.status is GateStatus.PASS
        assert r.g1.resolution_margin > 0

    def test_missing_inconclusive_bin_fails(self):
        spec = _zero_vs_nonzero_spec(validate_on_known=ValidateOnKnownSpec("ref", 1.0, 1.0, 1e-6, inconclusive_bin=""))
        r = run_bench_model(spec)
        assert r.g1.status is GateStatus.FAIL
        assert r.verdict is Verdict.NOT_BANKABLE

    def test_not_through_identical_chain_fails(self):
        spec = _zero_vs_nonzero_spec(
            validate_on_known=ValidateOnKnownSpec(
                "ref", 1.0, 1.0, 1e-6, inconclusive_bin="x", through_identical_chain=False
            )
        )
        assert run_bench_model(spec).g1.status is GateStatus.FAIL


# ============================================================================
# G2 — forced FORM, not echoed VALUE (Fork-3).
# ============================================================================
class TestG2:
    def test_fork3_refuses_echo_gating_axis(self):
        spec = _zero_vs_nonzero_spec(
            axis_tags=(
                AxisTag(
                    "echo-axis",
                    ChordEcho.ECHO,  # gating-axis FORM is an echo -> Fork-3 refusal
                    ChordEcho.ECHO,
                    DiscriminatorAxis.MAGNITUDE,
                    SharedWith.FORM,
                    is_gating_axis=True,
                    calibration_free=False,
                    interpretive_alternatives=(IA.FLOOR, IA.COINCIDENCE, IA.EXACT),
                    rationale="declared axis is an imported value",
                ),
            )
        )
        r = run_bench_model(spec)
        assert r.g2.fork3_refused
        assert r.g2.status is GateStatus.FAIL
        assert r.verdict is Verdict.NOT_BANKABLE

    def test_too_few_interpretive_alternatives_flags(self):
        spec = _zero_vs_nonzero_spec(
            axis_tags=(
                AxisTag(
                    "rotation",
                    ChordEcho.CHORD,
                    ChordEcho.ECHO,
                    DiscriminatorAxis.ZERO_VS_NONZERO,
                    SharedWith.NONE,
                    is_gating_axis=True,
                    calibration_free=False,
                    interpretive_alternatives=(IA.FLOOR,),  # < 3
                    rationale="under-enumerated",
                ),
            )
        )
        r = run_bench_model(spec)
        assert not r.g2.interpretive_alternatives_ok
        assert r.g2.status is GateStatus.FRAMING_FLAG


# ============================================================================
# G3 — SM co-computed, discriminator-axis classification (Step 2.5).
# ============================================================================
class TestG3:
    def test_shared_form_ratio_without_form_chord_fails(self):
        # RATIO on a shared FORM with NO independent form chord -> non-discriminating
        spec = _shared_form_ratio_spec(
            axis_tags=(
                AxisTag(
                    "coefficient-ratio",
                    ChordEcho.CHORD,
                    ChordEcho.ECHO,
                    DiscriminatorAxis.RATIO,
                    SharedWith.FORM,
                    is_gating_axis=True,
                    calibration_free=False,
                    interpretive_alternatives=(IA.APPROX_WITH_RESIDUAL, IA.COINCIDENCE, IA.FLOOR),
                    rationale="no rescuing form chord",
                ),
            )
        )
        r = run_bench_model(spec)
        assert r.g3.status is GateStatus.FAIL
        assert r.g3.non_discriminating_on_shared_axis
        assert not r.g3.has_independent_form_chord
        assert r.verdict is Verdict.NOT_BANKABLE

    def test_same_grid_no_strawman(self):
        # The sweep drives both callables over the identical grid (sweep contract).
        spec = _shared_form_ratio_spec()
        r = run_bench_model(spec)
        assert r.g3.n_grid == 3

    def test_degenerate_observables_fail(self):
        # AVE == SM numerically (ratio ~ 1) on a MAGNITUDE axis -> degenerate, FAIL.
        spec = _zero_vs_nonzero_spec(
            ave_observable=lambda E: 5.0,
            sm_observable=lambda E: 5.0,
            axis_tags=(
                AxisTag(
                    "magnitude",
                    ChordEcho.CHORD,
                    ChordEcho.ECHO,
                    DiscriminatorAxis.MAGNITUDE,
                    SharedWith.FORM,
                    is_gating_axis=True,
                    calibration_free=False,
                    interpretive_alternatives=(IA.FLOOR, IA.COINCIDENCE, IA.EXACT),
                    rationale="observables do not diverge",
                ),
            ),
        )
        r = run_bench_model(spec)
        assert r.g3.status is GateStatus.FAIL
        assert "degenerate" in r.g3.note
        assert r.verdict is Verdict.NOT_BANKABLE


# ============================================================================
# G4 — derived-vs-asserted ledger.
# ============================================================================
class TestG4:
    def test_asserted_row_forks(self):
        r = run_bench_model(_zero_vs_nonzero_spec(ledger_rows=_ledger(asserted=True)))
        assert r.g4.has_asserted_row
        assert r.g4.status is GateStatus.FAIL
        assert r.verdict is Verdict.NOT_BANKABLE

    def test_missing_mandatory_aspect_fails(self):
        r = run_bench_model(_zero_vs_nonzero_spec(ledger_rows=_ledger(drop=LedgerAspect.PROBE)))
        assert not r.g4.all_aspects_present
        assert r.g4.status is GateStatus.FAIL

    def test_magnitude_row_status_recorded(self):
        r = run_bench_model(_shared_form_ratio_spec())
        assert r.g4.magnitude_row_status is LedgerStatus.ENGINEERING_CHOICE


# ============================================================================
# G5 — sensitivity sweep, not single-point.
# ============================================================================
class TestG5:
    def test_tuned_point_only_books_negative(self):
        tuned = SensitivitySpec(
            observable_of=lambda **k: 10.0 if k["x"] == 2.0 else 0.0,
            param_grids={"x": (1.0, 2.0, 3.0, 4.0)},
            verdict_fn=lambda o: o > 5.0,
        )
        r = run_bench_model(_zero_vs_nonzero_spec(sensitivity=tuned))
        assert r.g5.tuned_point_only
        assert r.g5.result_kind == "tuned_positive"
        assert r.g5.status is GateStatus.FAIL
        assert r.verdict is Verdict.NOT_BANKABLE

    def test_no_positive_anywhere_fails(self):
        dead = SensitivitySpec(
            observable_of=lambda **k: 0.0, param_grids={"x": (1.0, 2.0, 3.0)}, verdict_fn=lambda o: o > 5.0
        )
        r = run_bench_model(_zero_vs_nonzero_spec(sensitivity=dead))
        assert r.g5.result_kind == "no_positive"
        assert r.g5.status is GateStatus.FAIL

    def test_missing_sweep_on_physics_test_fails(self):
        r = run_bench_model(_zero_vs_nonzero_spec(sensitivity=None))
        assert r.g5.status is GateStatus.FAIL
        assert r.g5.result_kind == "no_sweep"

    def test_numerical_magnitude_needs_convergence_sweep(self):
        # numerical magnitude claim with no convergence axis -> BLOCKED
        r = run_bench_model(_shared_form_ratio_spec(result_is_numerical=True))
        assert r.g5.magnitude_claim_blocked
        assert r.verdict is Verdict.NOT_BANKABLE

    def test_numerical_magnitude_with_convergence_ok(self):
        sens_conv = SensitivitySpec(
            observable_of=lambda **k: 1.0,
            param_grids={"L": (0.1, 0.2, 0.3), "N": (16.0, 32.0, 64.0)},
            verdict_fn=lambda o: o > 0.5,
            convergence_param="N",
        )
        r = run_bench_model(_shared_form_ratio_spec(result_is_numerical=True, sensitivity=sens_conv))
        assert r.g5.convergence_sweep_present
        assert r.verdict is Verdict.BANKABLE_AS_DISCRIMINATOR

    def test_flip_boundary_detected(self):
        # observable rises with x; verdict flips around x=2.5
        sens = SensitivitySpec(
            observable_of=lambda **k: k["x"], param_grids={"x": (1.0, 2.0, 3.0, 4.0)}, verdict_fn=lambda o: o > 2.5
        )
        r = run_bench_model(_zero_vs_nonzero_spec(sensitivity=sens))
        boundary = r.g5.per_param[0].flip_boundary
        assert boundary == pytest.approx(2.5, abs=0.6)
        assert r.g5.verdict_flips_within_range


# ============================================================================
# G6 — symmetric standard.
# ============================================================================
class TestG6:
    def test_peer_vs_shortfall_split(self):
        # PROBE is ENGINEERING-CHOICE with sm_also=True -> PEER, not a shortfall.
        r = run_bench_model(_zero_vs_nonzero_spec())
        assert "probe" in r.g6.peer_rows
        assert r.g6.status is GateStatus.FRAMING_FLAG

    def test_ave_only_shortfall_stands(self):
        rows = (
            LedgerRow(LedgerAspect.COUPLING, LedgerStatus.DERIVED, "x", sm_also=True),
            LedgerRow(LedgerAspect.PROBE, LedgerStatus.ENGINEERING_CHOICE, "ave-only", sm_also=False),
            LedgerRow(LedgerAspect.MAGNITUDE, LedgerStatus.DERIVED, "y", sm_also=True),
            LedgerRow(LedgerAspect.OBSERVABLE, LedgerStatus.DERIVED, "z", sm_also=False),
        )
        r = run_bench_model(_zero_vs_nonzero_spec(ledger_rows=rows))
        assert "probe" in r.g6.ave_only_shortfalls


# ============================================================================
# G7 — frozen prereg.
# ============================================================================
class TestG7:
    def test_unfrozen_prereg_fails(self):
        r = run_bench_model(_zero_vs_nonzero_spec(prereg=_prereg(frozen=False)))
        assert r.g7.status is GateStatus.FAIL

    def test_missing_inconclusive_bin_fails(self):
        r = run_bench_model(_zero_vs_nonzero_spec(prereg=_prereg(with_inconclusive=False)))
        assert r.g7.status is GateStatus.FAIL
        assert not r.g7.has_inconclusive_bin

    def test_magnitude_claim_needs_dimensional_eval(self):
        # magnitude claimed but prereg has no expected_magnitude_eval
        r = run_bench_model(_shared_form_ratio_spec(prereg=_prereg(magnitude=False)))
        assert r.g7.status is GateStatus.FAIL
        assert r.g7.dimensional_eval_required and not r.g7.dimensional_eval_present


# ============================================================================
# G8 — evidence-framing.
# ============================================================================
class TestG8:
    def test_clean_pass(self):
        r = run_bench_model(_zero_vs_nonzero_spec())
        assert r.g8.status is GateStatus.PASS
        assert r.g8.selection_from_pool_clean

    def test_undisclosed_selection_from_pool_fails(self):
        spec = _zero_vs_nonzero_spec(evidence_framing=_framing("rotation", n_displayed=2, n_total=10, omitted=()))
        r = run_bench_model(spec)
        assert not r.g8.selection_from_pool_clean
        assert r.g8.status is GateStatus.FAIL

    def test_disclosed_subset_is_clean(self):
        spec = _zero_vs_nonzero_spec(
            evidence_framing=_framing("rotation", n_displayed=2, n_total=4, omitted=("null-1", "null-2"))
        )
        assert run_bench_model(spec).g8.selection_from_pool_clean


# ============================================================================
# Record serialization + summary.
# ============================================================================
class TestRecordSerialization:
    def test_as_dict_is_json_serializable(self):
        for spec in (_zero_vs_nonzero_spec(), _shared_form_ratio_spec(), _pilot_spec()):
            d = run_bench_model(spec).as_dict()
            s = json.dumps(d)  # must not raise (no enums / numpy left)
            assert "verdict" in d and "gates" in d
            assert len(json.loads(s)["gates"]) == 8

    def test_summary_renders(self):
        out = run_bench_model(_shared_form_ratio_spec()).summary()
        assert "VERDICT" in out
        assert "BANKABLE_AS_DISCRIMINATOR" in out

    def test_snr_window_populated_when_supplied(self):
        r = run_bench_model(_zero_vs_nonzero_spec(snr_signal=1e6, snr_floor=1e2))
        assert r.snr_time_to_5sigma_s is not None
        assert r.snr_signal_vs_floor == pytest.approx(1e4, rel=1e-9)


# ============================================================================
# Package export surface.
# ============================================================================
class TestExports:
    def test_spine_reexported_flat(self):
        for name in (
            "run_bench_model",
            "BenchSpec",
            "BankabilityRecord",
            "Verdict",
            "GateStatus",
            "LedgerRow",
            "AxisTag",
            "Prereg",
            "EvidenceFraming",
            "ValidateOnKnownSpec",
            "SensitivitySpec",
        ):
            assert hasattr(bench, name), name
            assert name in bench.__all__, name

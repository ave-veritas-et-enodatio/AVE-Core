"""test_bench_adopters.py — the reference BenchSpec adopters (GAP-1).

Exercises ave.bench.adopters: the two reference adopters that prove the
channel-agnostic spine shape against real charter targets —
  - birefringence coefficient bench -> BANKABLE_AS_DISCRIMINATOR
  - cRIO C_eff(V) validate-on-known pilot -> VALIDATE_ON_KNOWN_PASS

These assert the adopters IMPORT the canonical ave.bench.birefringence physics
layer (not hand-rolled numbers) and route through the spine to the charter-
expected tiers.
"""

from __future__ import annotations

import json

import pytest

import ave.bench as bench
from ave.bench.adopters import birefringence_bench_spec, crio_validate_on_known_spec
from ave.bench.model import (
    GateStatus,
    LedgerStatus,
    SharedWith,
    Verdict,
    run_bench_model,
)


class TestBirefringenceAdopter:
    def test_verdict_bankable_as_discriminator(self):
        r = run_bench_model(birefringence_bench_spec())
        assert r.verdict is Verdict.BANKABLE_AS_DISCRIMINATOR
        assert r.hard_gates_pass

    def test_ratio_rides_canonical_physics_layer(self):
        # the discriminator ratio must match the canonical closed form (proof the
        # adopter imports the physics layer rather than hand-rolling a number).
        r = run_bench_model(birefringence_bench_spec())
        assert r.g3.field_independent
        assert r.g3.ratio_value == pytest.approx(bench.coefficient_ratio_differential(), rel=1e-9)

    def test_headlines_differential_not_single_arm(self):
        # ~1.93e7 differential, NOT the demoted single-arm ~4.14e6 (FLAG-A).
        r = run_bench_model(birefringence_bench_spec())
        assert abs(r.g3.ratio_value - 1.93e7) / 1.93e7 < 0.02
        assert abs(r.g3.ratio_value - 4.14e6) / 4.14e6 > 0.5

    def test_g1_recovers_pvlas_A_e(self):
        r = run_bench_model(birefringence_bench_spec())
        assert r.g1.status is GateStatus.PASS
        assert r.g1.comparison.reference == 1.32e-24

    def test_magnitude_row_is_echo_open_sizing(self):
        # the open G4 sizing row is what holds it at the discriminator tier.
        r = run_bench_model(birefringence_bench_spec())
        assert r.g4.magnitude_row_status is LedgerStatus.ENGINEERING_CHOICE
        assert r.g3.has_independent_form_chord  # tree-vs-loop rescue

    def test_shared_form_recorded(self):
        r = run_bench_model(birefringence_bench_spec())
        assert r.g3.shared_with is SharedWith.FORM
        assert r.g3.non_discriminating_on_shared_axis


class TestCrioPilot:
    def test_verdict_validate_on_known_pass(self):
        r = run_bench_model(crio_validate_on_known_spec())
        assert r.verdict is Verdict.VALIDATE_ON_KNOWN_PASS
        assert not r.is_physics_test

    def test_g1_recovers_datasheet(self):
        r = run_bench_model(crio_validate_on_known_spec())
        assert r.g1.status is GateStatus.PASS
        assert r.g1.comparison.passed

    def test_prereg_draft_g7_honestly_fails_but_does_not_gate(self):
        # the cRIO prereg is a DRAFT (not frozen) -> G7 FAIL, but the pilot verdict
        # is unaffected (only G1 gates a validate-on-known pilot).
        r = run_bench_model(crio_validate_on_known_spec())
        assert r.g7.status is GateStatus.FAIL
        assert not r.g7.frozen
        assert r.verdict is Verdict.VALIDATE_ON_KNOWN_PASS

    def test_material_analog_g3_degenerate_non_gating(self):
        # the material analog shares the saturating FORM (GAP-6) -> G3 honestly
        # reports non-discriminating, but it does not gate the pilot verdict.
        r = run_bench_model(crio_validate_on_known_spec())
        assert r.g3.status is GateStatus.FAIL
        assert r.verdict is Verdict.VALIDATE_ON_KNOWN_PASS

    def test_regime_note_records_unreachability_and_gap6(self):
        r = run_bench_model(crio_validate_on_known_spec())
        assert "Regime I" in r.regime_note
        assert "GAP-6" in r.regime_note


class TestAdopterSerialization:
    def test_both_records_json_serializable(self):
        for spec_fn in (birefringence_bench_spec, crio_validate_on_known_spec):
            d = run_bench_model(spec_fn()).as_dict()
            json.dumps(d)
            assert len(d["gates"]) == 8

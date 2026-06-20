"""Unit + validate-on-known tests for the shared ave.bench package.

Each test class targets one factored module and pins it against its NAMED
exemplar. The load-bearing tests are the validate-on-known regressions: they
drive the factored module with the SAME inputs the exemplar uses internally and
assert the factored module REPRODUCES the exemplar's numeric output. The
factoring is not done until proven faithful.

Exemplars:
  sweep.py     <- AVE-Bench-VacuumMirror/scripts/analytical_gamma_v_sweep.py
  apparatus.py <- AVE-Core src/scripts/vol_4_engineering/qg42_vsign_deltaf.py
  snr.py       <- AVE-Bench-VacuumMirror/scripts/apd_snr_sweep.py
  validate.py  <- AVE-Core src/scripts/verify/*_anchor.py (muon_g2_fermilab)
"""

from __future__ import annotations

import numpy as np

import ave.bench as bench


class TestPackageSkeleton:
    """Commit-1 skeleton smoke: the package imports and exposes its contract."""

    def test_public_api_present(self):
        for name in [
            "run_divergence_sweep",
            "DivergenceSweepResult",
            "ApparatusCoupling",
            "saturation_amplitude",
            "v_yield_apparatus",
            "fn_dark_current",
            "fn_safe_max_amplitude",
            "snr_shot_noise",
            "time_to_n_sigma",
            "signal_vs_floor",
            "SNRPoint",
            "assert_recovers_known",
            "KnownComparison",
        ]:
            assert hasattr(bench, name), f"ave.bench missing public symbol {name}"

    def test_modules_importable(self):
        from ave.bench import apparatus, snr, sweep, validate  # noqa: F401

        assert callable(sweep.run_divergence_sweep)
        assert callable(apparatus.saturation_amplitude)
        assert callable(snr.snr_shot_noise)
        assert callable(validate.assert_recovers_known)

"""Pytest collection policy for src/tests.

Default ``make test`` runs the BEDROCK KEEPERS (per the loop-gap coverage ledger
§0). Two opt-in lanes carry the rest:
  * ``make test-genesis`` — the srs chiral genesis archive (file-ignored below).
  * ``make test-engine``  — the slow tier-1/2 engine-simulation tests, marked
    ``engine_sim`` by the partition below and run via ``-m engine_sim``.

CI partition: research/2026-06-13_ci-engine-sim-partition_prereg.md.
INVARIANT (§7): the engine_sim partition is selected by test COST + ROLE (the
ledger's T0 keeper / T1 wiring / T2 driver tiers) ONLY — never by an engine
capability-matrix grade. Re-grading a capability cell must change nothing here.
"""

import pytest

# srs chiral genesis archive — not collected by default; run via `make test-genesis`.
collect_ignore_glob = [
    "test_chiral_lattice_v*.py",
    "test_chiral_lattice_phase*.py",
    "test_chiral_lattice_vector_phase*.py",
    "test_genesis_*.py",
]

# --- engine_sim partition (single source of truth) --------------------------
# WHOLE-FILE: uniformly research-tier engine drivers / resolution-dependent eigensolve.
_ENGINE_SIM_FILES = {
    "test_unified_threaded_v8.py",            # T2 genesis-v8 D15-D18 drivers
    "test_unified_quadrature_v7.py",          # T2 genesis-v8 v7 quadrature
    "test_unified_transducer_v6.py",          # T2 genesis-v8 v6 transducer
    "test_unified_genesis_engine.py",         # T2 genesis-v8 engine
    "test_unified_snap_machine.py",           # T2 genesis-v8 snap-machine
    "test_electron_tlm_eigenmode.py",         # N=48 eigensolve, resolution-DEPENDENT + xfail-strict (Ruling 3)
    "test_cosserat_engine_q_preservation.py", # `>=3 Q before boundary reflection` moves with N (resolution-DEPENDENT, §2b)
}
# SPECIFIC TESTS in MIXED files (fast keepers in the same file STAY gating):
_ENGINE_SIM_TESTS = {
    "test_loop_gap_harness.py::test_loop_gap_probe_runs",                  # T1 wiring "runs"
    "test_loop_gap_harness.py::test_graded_a0_seed_runs",                  # T1 wiring "runs"
    "test_loop_gap_harness_rank1_regime.py::test_dlite_probe_fields",      # T1 instrument
    "test_loop_gap_harness_rank1_regime.py::test_dlite_battery_smoke",     # T2 battery
    "test_loop_gap_harness_bulk_channel.py::test_f1_bulk_on_differs_from_off",   # borderline-wiring + redundant w/ fast keepers
    "test_loop_gap_harness_bulk_channel.py::test_f2_channel_tags_on_bulk_probe", # T1 (flag/tag presence; mistagged T0 in ledger)
}


def pytest_collection_modifyitems(config, items):
    """Apply the ``engine_sim`` marker to the partition above (cost+role, not physics)."""
    for item in items:
        if item.path.name in _ENGINE_SIM_FILES or any(
            item.nodeid.endswith(t) for t in _ENGINE_SIM_TESTS
        ):
            item.add_marker(pytest.mark.engine_sim)

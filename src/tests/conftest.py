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
    "test_stage0_alpha_clean_spine.py",       # Stage-0 spine: N=72 cage-build + closed-port eigensolve (T2 engine-acceptance cost+role, matches its siblings)
}
# SPECIFIC TESTS in MIXED files (fast keepers in the same file STAY gating):
_ENGINE_SIM_TESTS = {
    "test_loop_gap_harness.py::test_loop_gap_probe_runs",                  # T1 wiring "runs"
    "test_loop_gap_harness.py::test_graded_a0_seed_runs",                  # T1 wiring "runs"
    "test_loop_gap_harness_rank1_regime.py::test_dlite_probe_fields",      # T1 instrument
    "test_loop_gap_harness_rank1_regime.py::test_dlite_battery_smoke",     # T2 battery
    "test_loop_gap_harness_bulk_channel.py::test_f1_bulk_on_differs_from_off",   # borderline-wiring + redundant w/ fast keepers
    "test_loop_gap_harness_bulk_channel.py::test_f2_channel_tags_on_bulk_probe", # T1 (flag/tag presence; mistagged T0 in ledger)
    # Phase-1 chiral-OA Gate-2 convergence cascades (T2 drivers; 15-238s each, ~656s total
    # of the PR-gate wall-clock). The gate1/gate3/loop keepers in the same file STAY gating
    # (fast operator/lossless/holonomy checks). Coverage preserved via `make test-engine`.
    "test_chiral_vector_tlm_phase1.py::test_gate2_bulk_forward_channel_rate_converges_to_screw_pitch",
    "test_chiral_vector_tlm_phase1.py::test_gate2_bulk_rate_enantiomorph_sign_flip_is_exact",
    "test_chiral_vector_tlm_phase1.py::test_gate2_dispersion_free_cascade_confirms_screw_pitch",
    "test_chiral_vector_tlm_phase1.py::test_gate2_transient_skip_kills_the_outcome_c_swing",
    "test_chiral_vector_tlm_phase1.py::test_gate2_legacy_packet_probe_is_a_known_artifact",
    "test_chiral_vector_tlm_phase1.py::test_gate2_aggregate_pass",
    # L3 mass-cage bound-eigenmode solve (T2 resolution-dependent eigensolve, 64s).
    "test_l3_mass_cage.py::test_t3_4_bound_eigenmode_of_posited_cage",
    # Fork-B saturation-tank reconfine-rate sweep (T2 convergence sweep, ~50s + memory-heavy):
    # OOM-crashed its xdist worker on the CI runner under parallel memory pressure (#386 run 1,
    # "node down: Not properly terminated"). Same cost+role tier; coverage via make test-engine.
    "test_fork_b_saturation_tank.py::test_gate2_armB_pooled_reconfine_rate_sweep",
    # S2 H_couple criterion-3 + full-gate: invoke the REAL CrystalGraftV4 (S1
    # reachable-False slaved-arm discriminator, N=48 engine evolution). T2 driver
    # cost+role; the rest of the S2 suite (pure-numpy skew-Hermitian dynamics) STAYS
    # gating. Coverage via make test-engine.
    "test_s2_hcouple.py::test_s2_criterion_3_independence_slaved_arm_reachable_false",
    "test_s2_hcouple.py::test_s2_full_gate_verdict_pass",
    # Coupled A1+winding eigensolve: the N=32 resolution-dependent eigensolves (T2
    # drivers). T0/T2/T7 (α-clean, Hermitian, ladder-shape on small N) STAY gating.
    "test_coupled_eigensolve.py::test_t1_halt_winding_off_recovers_forkb",
    "test_coupled_eigensolve.py::test_t3_seeded_winding_reads_2_3",
    "test_coupled_eigensolve.py::test_t4_winding_bled_out_of_bound_mode",
    "test_coupled_eigensolve.py::test_t5_arm_b_deconfines",
    "test_coupled_eigensolve.py::test_t6_committed_verdict_does_not_exist",
}
# EXCEPTIONS — kept in the GATING lane despite living in a whole-file engine_sim
# module: the genesis INHERITANCE/DORMANCY-CONTRACT keepers, which
# research/2026-06-10_genesis-v7-quadrature_result.md:5 calls "the D-INHERIT
# keeper ... must stay green". They gate the contract during active v7/v8 dev.
#
# SCOPING PRINCIPLE (draw the boundary by CONFIG, not by the test's NAME — the
# name carries a salience bias that has mis-drawn this line twice):
#   keep-gating == a STRICT default-off contract: feature-OFF (`*_on=False`,
#   `frac=0`, snap_u_mode="inherited", ...) ⇒ inherited sectors UNCHANGED
#   (byte/bit-identical to parent/vN-1) AND the new sector INERT (stays zero).
#   The two halves are distinct: null1 asserts V/w/omega==parent (inheritance);
#   null2 asserts rho_bar/u_adv/step_count==0 (dormancy) — null1 passes a
#   new-sector-activates-by-default regression straight through, so BOTH gate.
# DELIBERATELY NOT here (recorded, not missed): the PROBE-FLOOR / reading
#   controls — `chi0_is_the_known_null_floor`, `k_rigid_null`, `d15_chi_zero`.
#   They are also default-off but assert a PROBE's null reading (apparatus-floor
#   class), not the inheritance/dormancy contract — they stay opt-in.
# NOTE (scope, honest): these are RELATIVE identities ⇒ common-mode-blind to a
#   silent crystal_engine BASE shift. The base REGIME is gated separately and
#   already, by test_master_equation_v14_mode_i.py + test_cosserat_master_
#   equation_op14.py (LOOSE regime bounds, NOT goldens — a tight golden would
#   violate the apparatus-qualified-magnitude discipline). So this gates the
#   contract, not the base. (2026-06-13 audit of the unified_* whole-file marks.)
_ENGINE_SIM_KEEP_GATING = {
    "test_unified_genesis_engine.py::test_null1_bit_identical_to_parent",       # inheritance half
    "test_unified_genesis_engine.py::test_null2_dormant_bulk_stays_zero",       # dormancy half (config-signal 8th)
    "test_unified_quadrature_v7.py::test_k_off_quadrature_defaults_off_byte_identical_to_v6",
    "test_unified_transducer_v6.py::test_v6_transducer_defaults_off_byte_identical",
    "test_unified_transducer_v6.py::test_v6_omega_recipient_frac0_is_byte_identical_pure_u_adv",
    "test_unified_threaded_v8.py::test_d17_inherited_is_byte_identical_default",
    "test_unified_threaded_v8.py::test_d15_off_byte_identical",
    "test_unified_snap_machine.py::test_null_byte_identical_under_snap_when_no_crossing",
}


def pytest_collection_modifyitems(config, items):
    """Apply the ``engine_sim`` marker to the partition above (cost+role, not physics)."""
    for item in items:
        if any(item.nodeid.endswith(k) for k in _ENGINE_SIM_KEEP_GATING):
            continue  # inheritance-contract keeper: stays in the gating lane
        if item.path.name in _ENGINE_SIM_FILES or any(
            item.nodeid.endswith(t) for t in _ENGINE_SIM_TESTS
        ):
            item.add_marker(pytest.mark.engine_sim)

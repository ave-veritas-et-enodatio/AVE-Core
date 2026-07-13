"""Genesis node-birth D1–D3 gates (prereg FROZEN on main via #654).

Fast keepers: D1 cardinality + D3 necessity + bin logic.
Slow: D2 harness persistence → engine_sim partition.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_SCRIPTS = Path(__file__).resolve().parents[1] / "scripts" / "vol_1_foundations"
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

import itertools

from ave.core.categorization import ClaimClass
from ave.core.genesis_v18_coupled import P11_A_PERSIST_MIN, P11_E_PERSIST_MIN

from genesis_node_birth_discriminator import (  # noqa: E402
    D1_VIOLATION_HALT,
    LANDED_SEED_MODES,
    adjudicate_bin,
    d1_crystal_engine,
    d1_master_equation,
    d2_battery_persists,
    d2_loop_gap_persistence,
    d3_necessity_corpus,
    run_suite,
)


def test_d1_crystal_and_me_cardinality_invariant():
    c = d1_crystal_engine(N=8, n_steps=10)
    m = d1_master_equation(N=8, n_steps=10)
    assert c.invariant and m.invariant
    assert c.n_sites_t0 == 8**3 == c.n_sites_tend
    assert m.n_sites_t0 == 8**3 == m.n_sites_tend
    assert c.claim_class == ClaimClass.CERTIFICATION_ENTAILED.value
    assert m.claim_class != ClaimClass.EMERGENCE.value


def test_d3_not_entailed_with_cites():
    r = d3_necessity_corpus()
    assert r.not_entailed is True
    assert len(r.cites) >= 3
    leaves = " ".join(c["leaf"] for c in r.cites)
    assert "historical-precedents" in leaves
    assert "engine-capability-map" in leaves


def test_adjudicate_bins_frozen():
    assert (
        adjudicate_bin(d1_ok=True, d2_persist=True, d3_not_entailed=True)
        == "i_A_SUPPORTED"
    )
    assert (
        adjudicate_bin(d1_ok=True, d2_persist=False, d3_not_entailed=True)
        == "ii_A_WEAKENED"
    )
    assert (
        adjudicate_bin(d1_ok=True, d2_persist=True, d3_not_entailed=False)
        == "iii_B_NECESSITY_CLAIM_FAILS"
    )
    assert (
        adjudicate_bin(
            d1_ok=True, d2_persist=True, d3_not_entailed=True, d4_ran=True, d4_absurd=True
        )
        == "iv_B_COSMOLOGY_ABSURD"
    )


def test_adjudicate_d1_violation_halts_all_combinations():
    """R2: every d1_ok=False case → OUT-OF-BIN halt, NOT ii_A_WEAKENED.

    A real cardinality mutation is the fork-(B) signature; the shipped adjudicator
    mislabelled it as an (A)-weakening. The halt dominates D2/D3/D4.
    """
    for d2p, d3ne, d4r, d4a in itertools.product([True, False], repeat=4):
        assert (
            adjudicate_bin(
                d1_ok=False,
                d2_persist=d2p,
                d3_not_entailed=d3ne,
                d4_ran=d4r,
                d4_absurd=d4a,
            )
            == D1_VIOLATION_HALT
        )
    # d1_ok=True must NEVER return the halt (guards against over-firing).
    for d2p, d3ne in itertools.product([True, False], repeat=2):
        assert (
            adjudicate_bin(d1_ok=True, d2_persist=d2p, d3_not_entailed=d3ne)
            != D1_VIOLATION_HALT
        )


def test_d2_battery_persists_needs_only_one_path():
    """bin (i) D2 criterion: persistence PASS on ≥1 landed fixed-N path."""
    from dataclasses import replace

    from genesis_node_birth_discriminator import D2Report

    base = D2Report(
        path="loop_gap_harness",
        N=10,
        E_persist_ratio=0.0,
        phi_persist_ratio=0.0,
        gamma_min_drive=0.0,
        gamma_bulk_min_end=0.0,
        v_inc_peak=0.0,
        rank4_pass=False,
        persistence_pass=False,
        claim_class=ClaimClass.CONSISTENCY.value,
    )
    all_fail = [replace(base, seed_mode=m) for m in LANDED_SEED_MODES]
    assert d2_battery_persists(all_fail) is False
    one_pass = list(all_fail)
    one_pass[0] = replace(one_pass[0], persistence_pass=True)
    assert d2_battery_persists(one_pass) is True
    assert LANDED_SEED_MODES == ("pair", "photon_lock", "graded_a0")


def test_run_suite_d1_d3_without_d2():
    out = run_suite(include_d2=False, N_harness=8)
    assert out["bin"] == "PENDING_D2"
    assert all(r["invariant"] for r in out["d1"])
    # R3: 2 measured (crystal/ME, genuinely stepped) + 1 structural (harness).
    assert out["d1_measured_paths"] == 2
    assert out["d1_structural_paths"] == 1
    assert out["d3"]["not_entailed"] is True
    assert out["d4"]["status"] == "SKIPPED_WITH_REASON"
    assert out["d2"] is None


def test_d2_persistence_harness_smoke():
    """T2 cost+role — listed in conftest engine_sim partition.

    photon_lock leg of the R1 battery. FAIL leg (E≈0.82<0.85, φ_persist=0 —
    φ-channel structurally dead at write-time, R5). Fireable, not a CI kill.
    """
    r = d2_loop_gap_persistence(N=10, seed_mode="photon_lock")
    assert r.path == "loop_gap_harness"
    assert r.seed_mode == "photon_lock"
    assert r.claim_class == ClaimClass.CONSISTENCY.value
    # Fireable: ratios are finite; PASS/FAIL is result-doc adjudication, not CI kill.
    assert r.E_persist_ratio == r.E_persist_ratio  # not NaN
    assert r.phi_persist_ratio == r.phi_persist_ratio


def test_d2_persistence_plant_pair_seed_fires():
    """R4: PASS-CONTROL for the persistence detector (P11-style plant).

    The pair seed at the banked smoke config drives BOTH ratios above their
    floors (E_persist≥0.85 AND φ_persist≥0.80 ⇒ persistence_pass), proving the
    detector CAN fire — the photon_lock FAIL is a real physics miss, not a dead
    apparatus. T2 cost+role (engine_sim; ~160s). Banked receipt: pair smoke
    E=0.8639, φ=7.7295 (research/2026-07-12_genesis-node-birth-discriminator_result.md).
    """
    r = d2_loop_gap_persistence(N=10, seed_mode="pair")
    assert r.seed_mode == "pair"
    assert r.E_persist_ratio >= P11_E_PERSIST_MIN
    assert r.phi_persist_ratio >= P11_A_PERSIST_MIN
    assert r.persistence_pass is True

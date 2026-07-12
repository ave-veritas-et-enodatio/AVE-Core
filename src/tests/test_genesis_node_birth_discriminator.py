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

from ave.core.categorization import ClaimClass

from genesis_node_birth_discriminator import (  # noqa: E402
    adjudicate_bin,
    d1_crystal_engine,
    d1_master_equation,
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


def test_run_suite_d1_d3_without_d2():
    out = run_suite(include_d2=False, N_harness=8)
    assert out["bin"] == "PENDING_D2"
    assert all(r["invariant"] for r in out["d1"])
    assert out["d3"]["not_entailed"] is True
    assert out["d4"]["status"] == "SKIPPED_WITH_REASON"
    assert out["d2"] is None


def test_d2_persistence_harness_smoke():
    """T2 cost+role — listed in conftest engine_sim partition."""
    r = d2_loop_gap_persistence(N=10)
    assert r.path == "loop_gap_harness"
    assert r.claim_class == ClaimClass.CONSISTENCY.value
    # Fireable: ratios are finite; PASS/FAIL is result-doc adjudication, not CI kill.
    assert r.E_persist_ratio == r.E_persist_ratio  # not NaN
    assert r.phi_persist_ratio == r.phi_persist_ratio

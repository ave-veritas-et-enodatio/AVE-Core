"""D2 tests: count_charge_k4 adapter (Gate §11 items 1–8, N1, N3).

Each test exercises one contract item of the K4 charge adapter. All use BCC
32³ or 48³ grids (unit scale; ~60 s serial per test max). Fixtures are
function-scoped (no module-scope field allocation) to keep peak RSS safe in the
serial tail.

Canonical seeds verified here against the charge_counters pinned values.
"""

import numpy as np
import pytest

from ave.topological.k4_quaternion import count_charge_k4
from ave.topological.charge_counters import (
    bcc_alive_mask, hedgehog, random_regular_values, random_n_vectors,
    BCC_TETS, c_exact,
)


# ── helpers ──────────────────────────────────────────────────────────────────

def _make_hedgehog_q(n, rc, mirror=False):
    """BCC-padded hedgehog: dead sites → identity."""
    q = hedgehog(n, rc, mirror=mirror)
    alive = bcc_alive_mask((n, n, n))
    q[~alive] = np.array([1.0, 0.0, 0.0, 0.0])
    return q, alive


# ── positive controls ─────────────────────────────────────────────────────────


def test_adapter_hedgehog_plus1():
    """D2: hedgehog(n=32, rc=4) → count_charge_k4 resolves +1."""
    n, rc = 32, 4
    q, alive = _make_hedgehog_q(n, rc)
    result = count_charge_k4(q, alive)
    assert result['resolved'], (
        f"hedgehog +1 UNRESOLVED: {result['reason']}")
    assert result['value'] == 1, (
        f"hedgehog value={result['value']}, expected 1")


def test_adapter_hedgehog_mirror_minus1():
    """D2: mirror hedgehog(n=32, rc=4) → count_charge_k4 resolves −1."""
    n, rc = 32, 4
    q, alive = _make_hedgehog_q(n, rc, mirror=True)
    result = count_charge_k4(q, alive)
    assert result['resolved'], (
        f"hedgehog −1 UNRESOLVED: {result['reason']}")
    assert result['value'] == -1, (
        f"hedgehog mirror value={result['value']}, expected −1")


# ── renormalization (N3) ──────────────────────────────────────────────────────


def test_adapter_renormalize_times10_becomes_nonunit():
    """D2 F3 (v5, INVERTED): ×10 non-unit q → NONUNIT, NOT a renorm'd verdict.

    The adapter must NOT renormalize a grossly non-unit field into an integer
    verdict — a |q|≠1 of this magnitude signals a broken upstream invariant.
    A pre-renorm deviation > 1e-6 returns resolved=False with reason NONUNIT.
    """
    n, rc = 32, 4
    q, alive = _make_hedgehog_q(n, rc)
    q_times10 = q.copy()
    q_times10[alive] *= 10.0  # alive sites ×10; dead sites untouched (identity)

    result = count_charge_k4(q_times10, alive)
    assert not result['resolved'], (
        f"×10 hedgehog should be NONUNIT (resolved=False), got resolved="
        f"{result['resolved']} value={result['value']}")
    assert 'NONUNIT' in (result.get('reason') or ''), (
        f"expected NONUNIT in reason, got: {result.get('reason')!r}")

    # Raw ×10 q passed straight to c_exact also returns NONUNIT (N3 cross-check).
    qstars = random_regular_values(5, 20261008)
    raw_result = c_exact(q_times10, qstars, tets=BCC_TETS, s=2)
    assert not raw_result['resolved'], "raw ×10 q should be NONUNIT-UNRESOLVED"
    assert 'NONUNIT' in (raw_result['reason'] or ''), (
        f"expected NONUNIT reason, got: {raw_result['reason']!r}")


def test_adapter_small_deviation_nonunit():
    """D2 F3: alive sites at 1+1e-5 deviation → NONUNIT (above the 1e-6 band)."""
    n, rc = 32, 4
    q, alive = _make_hedgehog_q(n, rc)
    q[alive, 0] += 1e-5   # breaks |q|=1 by ~1e-5, above the 1e-6 renorm band
    result = count_charge_k4(q, alive)
    assert not result['resolved'], (
        f"1+1e-5 deviation should be NONUNIT, got resolved={result['resolved']}")
    assert 'NONUNIT' in (result.get('reason') or ''), (
        f"expected NONUNIT in reason, got: {result.get('reason')!r}")


def test_adapter_tiny_deviation_resolves():
    """D2 F3: alive sites at 1+1e-8 deviation → RESOLVED (within the 1e-6 band)."""
    n, rc = 32, 4
    q, alive = _make_hedgehog_q(n, rc)
    q[alive, 0] += 1e-8   # round-off-scale; pre-renorm dev ≈ 1e-8 << 1e-6
    result = count_charge_k4(q, alive)
    assert result['resolved'], (
        f"1+1e-8 (round-off) should resolve after renorm: {result.get('reason')}")
    assert result['value'] == 1, f"value={result['value']}, expected 1"


# ── C-link-only / disagreement rules (N1) ────────────────────────────────────


def test_adapter_clink_only_unresolved(monkeypatch):
    """D2 N1: C-link RESOLVED but C-exact UNRESOLVED → adapter returns UNRESOLVED.

    Monkeypatches c_exact to return UNRESOLVED to isolate the N1 rule.
    """
    n, rc = 32, 4
    q, alive = _make_hedgehog_q(n, rc)

    import ave.topological.k4_quaternion as k4mod
    import ave.topological.charge_counters as cc_mod

    original_c_exact = cc_mod.c_exact

    def fake_c_exact(q_, qstars, tets=None, s=1):
        return dict(resolved=False, value=None, per_qstar=[], n_bad=0,
                    n_degen=0, n_warn=0, n_hits=[], reason='MONKEYPATCHED_UNRESOLVED')

    monkeypatch.setattr(cc_mod, 'c_exact', fake_c_exact)
    try:
        result = count_charge_k4(q, alive)
    finally:
        monkeypatch.setattr(cc_mod, 'c_exact', original_c_exact)

    assert not result['resolved'], "expected UNRESOLVED when c_exact UNRESOLVED"
    assert 'N1' in (result['reason'] or '') or 'c_exact' in (result['reason'] or ''), (
        f"reason should mention c_exact/N1: {result['reason']!r}")


def test_adapter_disagreeing_counters_unresolved(monkeypatch):
    """D2: c_exact and c_link resolve to different values → UNRESOLVED."""
    n, rc = 32, 4
    q, alive = _make_hedgehog_q(n, rc)

    import ave.topological.charge_counters as cc_mod

    original_c_link = cc_mod.c_link

    def fake_c_link(n_, nstars, h=1.0, tets=None, s=1):
        return dict(resolved=True, value=99, raw_lk=99.0,
                    pair_lk=[99.0, 99.0], n_open=0, n_broken=0,
                    n_comps=None, reason=None)

    monkeypatch.setattr(cc_mod, 'c_link', fake_c_link)
    try:
        result = count_charge_k4(q, alive)
    finally:
        monkeypatch.setattr(cc_mod, 'c_link', original_c_link)

    assert not result['resolved'], "expected UNRESOLVED when c_exact ≠ c_link"
    assert 'disagree' in (result['reason'] or '').lower() or \
           'c_exact' in (result['reason'] or ''), (
        f"reason should mention disagreement: {result['reason']!r}")


# ── wrong mask raises ─────────────────────────────────────────────────────────


def test_adapter_wrong_mask_raises():
    """D2: a mask with shifted parity (index 0 treated as odd-start) raises ValueError."""
    n, rc = 32, 4
    q, _ = _make_hedgehog_q(n, rc)
    # Shift the mask by rolling one step (wrong parity origin)
    correct_alive = bcc_alive_mask((n, n, n))
    wrong_alive = np.roll(correct_alive, 1, axis=0)
    with pytest.raises(ValueError, match='mask_alive'):
        count_charge_k4(q, wrong_alive)


# ── non-finite raises ─────────────────────────────────────────────────────────


def test_adapter_nan_on_dead_raises():
    """D2: NaN on a dead site raises ValueError."""
    n, rc = 32, 4
    q, alive = _make_hedgehog_q(n, rc)
    dead_idx = tuple(np.argwhere(~alive)[0])
    q[dead_idx] = np.array([float('nan'), 0.0, 0.0, 0.0])
    with pytest.raises(ValueError, match='non-finite.*dead'):
        count_charge_k4(q, alive)


def test_adapter_nan_on_alive_nonfinite():
    """D2 F3 (v5): NaN on an alive site → NONFINITE (resolved=False), NOT a raise.

    Dead-site non-finite still RAISES (test_adapter_nan_on_dead_raises, R0-P4:
    dead sites must be finite); an alive-site non-finite is a soft UNRESOLVED
    verdict so the R2 aggregator can log it and continue, not crash the run.

    Kills adapter_no_alive_nan (if False: guard removed): the adapter guard returns
    reason='NONFINITE: non-finite q on alive sites' (starts with NONFINITE). With
    the guard removed, c_exact's own NONFINITE check returns reason='NONFINITE' and
    the adapter wraps it as 'UNRESOLVED: c_exact NONFINITE' — which does NOT start
    with 'NONFINITE', so startswith() detects the bypass.
    """
    n, rc = 32, 4
    q, alive = _make_hedgehog_q(n, rc)
    alive_idx = tuple(np.argwhere(alive)[0])
    q[alive_idx] = np.array([float('nan'), 0.0, 0.0, 0.0])
    result = count_charge_k4(q, alive)
    assert not result['resolved'], "NaN on alive site should give resolved=False"
    assert result.get('reason', '').startswith('NONFINITE'), (
        f"expected reason to start with 'NONFINITE', got: {result.get('reason')!r}")
    assert result['value'] is None, (
        f"expected value=None for NONFINITE, got: {result['value']!r}")
    assert result.get('c_exact_result') is None, (
        f"expected c_exact_result=None for NONFINITE (adapter short-circuits before "
        f"c_exact), got: {result.get('c_exact_result')!r}")


def test_adapter_clink_exact_resolves_clink_unresolved(monkeypatch):
    """D2: c_exact RESOLVED + c_link UNRESOLVED → UNRESOLVED mentioning c_link (N1).

    Kills adapter_clink_unresolved_ignored (if False: c_link UNRESOLVED guard
    removed): without the guard, the disagreement branch fires (c_exact=+1 vs
    c_link=None), returning reason='UNRESOLVED: c_exact=1 disagrees with c_link=None'.
    Assertion 'disagrees' not in reason fails → kill confirmed.
    """
    n, rc = 32, 4
    q, alive = _make_hedgehog_q(n, rc)

    import ave.topological.charge_counters as cc_mod

    original_c_link = cc_mod.c_link

    def fake_c_link_unresolved(n_, nstars, h=1.0, tets=None, s=1):
        return dict(resolved=False, value=None, raw_lk=0.0,
                    pair_lk=[0.0, 0.0], n_open=0, n_broken=0,
                    n_comps=None, reason='MONKEYPATCHED_UNRESOLVED')

    monkeypatch.setattr(cc_mod, 'c_link', fake_c_link_unresolved)
    try:
        result = count_charge_k4(q, alive)
    finally:
        monkeypatch.setattr(cc_mod, 'c_link', original_c_link)

    assert not result['resolved'], (
        "expected UNRESOLVED when c_link UNRESOLVED")
    reason = result.get('reason') or ''
    assert reason.startswith('UNRESOLVED: c_link'), (
        f"reason should start with 'UNRESOLVED: c_link' (N1 guard), got: {reason!r}")


# ── boundary margin ───────────────────────────────────────────────────────────


def test_adapter_boundary_margin_unresolved():
    """D2: q0 = 0.3 on a face site gives UNRESOLVED 'boundary margin'."""
    n, rc = 32, 4
    q, alive = _make_hedgehog_q(n, rc)
    # Force a low q0 on an alive site on the x=0 face
    face_alive = np.argwhere(alive[0])  # alive sites on x=0 face
    if len(face_alive) == 0:
        pytest.skip("No alive sites on x=0 face for n=32")
    j0, k0 = face_alive[0]
    # Unit quaternion with q0=0.3 (|q|=1): q1 = sqrt(1 − 0.3²)
    q[0, j0, k0] = np.array([0.3, np.sqrt(1.0 - 0.3 ** 2), 0.0, 0.0])
    result = count_charge_k4(q, alive)
    assert not result['resolved'], "expected UNRESOLVED for boundary q0=0.3"
    assert 'boundary' in (result['reason'] or '').lower(), (
        f"reason should mention boundary: {result['reason']!r}")


# ── canonical seed values ─────────────────────────────────────────────────────


def test_adapter_canonical_seeds_match_pin():
    """D2: the canonical seeds used by count_charge_k4 match charge_counters pins.

    Verifies that random_regular_values(5, 20261008)[0] and
    random_n_vectors(4, 20261009)[0] are the pinned values from the Gate audit
    (charge_counters.py test_qstars_first_row_pinned / test_nstars_first_row_pinned).
    """
    qstars = random_regular_values(5, 20261008)
    nstars = random_n_vectors(4, 20261009)
    # Pinned row 0 values from Gate §7 (AUDIT-PR1066-reaudit-d2c7da09)
    expected_q0 = np.array([-0.0038962475, -0.5089801527, 0.8592503618, -0.0511159380])
    expected_n0 = np.array([0.6937011536, -0.6809262742, -0.2347724824])
    np.testing.assert_allclose(qstars[0], expected_q0, atol=1e-10,
        err_msg="QSTARS[0] does not match Gate pin")
    np.testing.assert_allclose(nstars[0], expected_n0, atol=1e-10,
        err_msg="NSTARS[0] does not match Gate pin")


def test_adapter_seed_constants_pinned():
    """D2 F3: the adapter's canonical seeds are pinned (q*=20261008, n*=20261009).

    Kills adapter_nstar_seed_20261008 (swapping the n* seed to 20261008): the two
    seeds produce different arrays, and the n* array is value-pinned to the
    20261009 draw. A seed swap trips either the constant pin or the value pin.
    """
    from ave.topological.k4_quaternion import (
        _CANONICAL_QSTARS_SEED, _CANONICAL_NSTARS_SEED)
    assert _CANONICAL_QSTARS_SEED == 20261008, (
        f"q* seed changed: {_CANONICAL_QSTARS_SEED}")
    assert _CANONICAL_NSTARS_SEED == 20261009, (
        f"n* seed changed: {_CANONICAL_NSTARS_SEED}")

    # The two seeds give genuinely different n* arrays (seed-swap would change n).
    n_20261009 = random_n_vectors(4, 20261009)
    n_20261008 = random_n_vectors(4, 20261008)
    assert not np.allclose(n_20261009, n_20261008), (
        "n* seeds 20261009 and 20261008 give the same array — seed swap undetectable")

    # Value-pin the actual n* array drawn by the canonical seed.
    nstars = random_n_vectors(4, _CANONICAL_NSTARS_SEED)
    expected_n0 = np.array([0.6937011536, -0.6809262742, -0.2347724824])
    np.testing.assert_allclose(nstars[0], expected_n0, atol=1e-10,
        err_msg="n* array for seed 20261009 does not match the pinned draw")


# ── c_det_alive4 is alarm only, not verdict ───────────────────────────────────


def test_adapter_cdet_logged_not_verdict():
    """D2: c_det_alive4 is present in the result dict as alarm/log field."""
    n, rc = 32, 4
    q, alive = _make_hedgehog_q(n, rc)
    result = count_charge_k4(q, alive)
    assert 'c_det_alive4' in result, "c_det_alive4 should be in result dict"
    cdet = result['c_det_alive4']
    assert np.isfinite(cdet), f"c_det_alive4 should be finite, got {cdet}"

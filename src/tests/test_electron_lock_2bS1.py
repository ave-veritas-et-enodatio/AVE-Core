"""Tests + standing falsifiers — electron-lock 2b-Stage-1 BINDING test.

Prereg (FROZEN): research/2026-07-07_electron-lock-2bS1_prereg_FROZEN.md
Harness:         src/ave/solvers/electron_lock_2bS1.py
Result:          research/2026-07-07_electron-lock-2bS1_RESULT.md

Coverage:
  * conservation (Ax3-lossless): the coupled harness is Hamiltonian — H-drift is a
    pure numerical diagnostic (validates the canonical coupling derivation);
  * firewall: no m_e/α token on the FILL/SUSTAIN/SELECT outcome path;
  * double-count guard: the q-cap collapse energy reconciles from v_q ALONE, via an
    INDEPENDENT quadrature, with the can-fire self-test proven live;
  * the FROZEN verdict as a STANDING FALSIFIER: all three arms route
    FILLS-BUT-DECAYS at (2,3); NEITHER inductive arm self-sustains. If a future
    engine/coupling change makes an arm FILLS-AND-SUSTAINS, these tests flip and
    force a re-adjudication (they are not a rubber stamp);
  * bin liveness: DOESN'T-FILL, FILLS-AND-SUSTAINS, and TAUTOLOGY are each shown
    REACHABLE (no dead plumbing), so "neither arm sustains" is informative;
  * scale-invariance: the α-echo magnitude in V_yield does not reach the verdict.
"""

from __future__ import annotations

import numpy as np
import pytest

from ave.solvers.electron_lock_2bS1 import (
    FILL_THRESH,
    PHI,
    SUSTAIN_THRESH,
    V_YIELD_HAT,
    ArmParams,
    ArmResult,
    classify,
    firewall_scan,
    reconcile_q_cap_energy,
    run_arm,
)

INDUCTIVE = ("mutual_M", "co_equal")
ALL_ARMS = ("mutual_M", "co_equal", "coupling_varactor")
N = 80  # common periods — decisive and fast; the frozen headline run uses 120


def _route(mode: str, ratio: float = 1.5, n: int = N, **kw) -> tuple[str, ArmResult, ArmResult]:
    main = run_arm(ArmParams(mode, ratio=ratio, **kw), n_common=n)
    golden = run_arm(ArmParams(mode, ratio=PHI, **kw), n_common=n)
    return classify(main, golden), main, golden


# ── conservation: the canonical coupling is genuinely lossless (Ax3) ─────────
@pytest.mark.parametrize("mode", ALL_ARMS)
def test_harness_is_lossless(mode: str) -> None:
    """H-drift ≪ the H_GATE — the coupled harness conserves energy, so the
    coupling forces are consistent with E_c (the canonical derivation is right) and
    H-drift is a pure numerical/pump diagnostic, not physics."""
    r = run_arm(ArmParams(mode, ratio=1.5), n_common=N)
    assert r.h_drift < 1e-3, f"{mode}: H-drift {r.h_drift:.2e} — coupling is not conservative"
    assert not r.ruptured, f"{mode}: ruptured (amplitude crossed the yield/saturation wall)"


# ── firewall: no m_e/α on the outcome path (prereg §4) ───────────────────────
def test_firewall_no_me_alpha_on_outcome_path() -> None:
    fw = firewall_scan()
    assert fw["clean"], f"firewall violation — m_e/α token on outcome path: {fw['hits']}"


# ── double-count guard: q-cap energy reconciles from v_q alone (prereg §5) ────
@pytest.mark.parametrize("mode", ALL_ARMS)
def test_q_cap_energy_double_count_reconcile(mode: str) -> None:
    """The Op14 collapse-cap energy used in the fill metric recomputes (closed form)
    == an INDEPENDENT numerical quadrature depending ONLY on v_q — so the varactor is
    carried once (no genesis-24 double-count). The gate's can-fire self-test is run."""
    gate = reconcile_q_cap_energy(ArmParams(mode, ratio=1.5))
    assert gate.passed, f"{mode}: q-cap energy did not reconcile (max_rel={gate.max_rel_discrepancy:.2e})"
    assert gate.can_fire_proven, f"{mode}: reconcile-gate can-fire self-test not proven"


# ── THE FROZEN VERDICT as a STANDING FALSIFIER (prereg §7, §8) ───────────────
@pytest.mark.parametrize("mode", ALL_ARMS)
def test_every_arm_fills(mode: str) -> None:
    """Every coupling mode POPULATES the empty q-tank above FILL_THRESH from a pure
    inductive d-seed (a forward step past genesis-23 max|V_inc|=0). MEASURED, not
    planted (the q-tank starts identically empty)."""
    _, main, _ = _route(mode)
    assert main.fill_max >= FILL_THRESH, f"{mode}: fill_max {main.fill_max:.3f} < {FILL_THRESH}"


@pytest.mark.parametrize("mode", INDUCTIVE)
def test_neither_inductive_arm_self_sustains(mode: str) -> None:
    """STANDING FALSIFIER (the headline negative). Neither inductive arm holds a
    persistent (2,3) partition: the back-half minimum q-energy returns below
    SUSTAIN_THRESH (reactive borrow/return = NOT mass). If a future change makes an
    arm sustain, this flips → re-adjudicate the §8 fork (do not delete the criterion)."""
    _, main, _ = _route(mode)
    assert main.fill_min < SUSTAIN_THRESH, (
        f"{mode}: fill_min {main.fill_min:.3f} ≥ {SUSTAIN_THRESH} — an arm now SELF-SUSTAINS; "
        "the reactive-pump-is-dead verdict is falsified — re-adjudicate prereg §8"
    )


def test_adjudication_is_reactive_pump_dead() -> None:
    """The frozen §8 route: NEITHER inductive arm FILLS-AND-SUSTAINS ⇒ the reactive
    candidate is dead (the '3' needs a non-reactive mechanism)."""
    bins = {m: _route(m, n=120)[0] for m in INDUCTIVE}
    assert not any(b == "FILLS-AND-SUSTAINS" for b in bins.values()), f"an arm sustains: {bins}"
    for m in INDUCTIVE:
        assert bins[m] == "FILLS-BUT-DECAYS", f"{m} routed {bins[m]} (expected FILLS-BUT-DECAYS)"


# ── bin liveness: each bin is REACHABLE (no dead plumbing) ────────────────────
def test_doesnt_fill_is_reachable() -> None:
    """Uncoupled (κ=0) leaves the q-tank empty → DOESN'T-FILL. Proves the fill metric
    is not spuriously nonzero and the bin is reachable."""
    b, main, _ = _route("mutual_M", kappa=0.0)
    assert b == "DOESN'T-FILL" and main.fill_max < FILL_THRESH


def test_fills_and_sustains_bin_is_reachable() -> None:
    """A synthetic locked-partition result routes FILLS-AND-SUSTAINS — the bin is LIVE
    plumbing, so 'no physical arm reaches it' is an informative negative, not a dead
    classifier branch."""
    p = ArmParams("mutual_M", ratio=1.5)
    good = ArmResult(p, 0.3, 0.2, 0.08, 0.001, 0.4, 240, 360, 0.1, 2.0, False)
    gold = ArmResult(p, 0.01, 0.004, 0.0, 0.001, 180.0, 240, 388, 0.1, float("inf"), False)
    assert classify(good, gold) == "FILLS-AND-SUSTAINS"


def test_tautology_detector_can_fire() -> None:
    """A STRONG bridging cap co-keys the tanks and MUST route TAUTOLOGY — the
    anti-tautology detector is live (the frozen c_frac=0.3 control sits sub-threshold
    and honestly routes FILLS-BUT-DECAYS instead)."""
    b_strong, _, _ = _route("coupling_varactor", c_frac=6.0)
    assert b_strong == "TAUTOLOGY", f"strong bridging cap routed {b_strong}, tautology detector is dead"


# ── scale-invariance: the α-echo magnitude in V_yield does not reach the verdict ─
@pytest.mark.parametrize("mode", INDUCTIVE)
def test_verdict_scale_invariant_to_v_yield(mode: str) -> None:
    b1, _, _ = _route(mode)
    b2, _, _ = _route(mode, v_yield_hat=2.0 * V_YIELD_HAT)
    assert b1 == b2, f"{mode}: bin changed with V_yield magnitude ({b1} → {b2}) — firewall breach"


# ── phase-space winding readout matches the (2,3) tuning (A46) ────────────────
@pytest.mark.parametrize("mode", INDUCTIVE)
def test_winding_readout_is_2_3(mode: str) -> None:
    """The measured phase-space winding ratio w_q/w_d ≈ 3/2 (the (2,3) tuning holds
    and both tanks ring coherently — the fill is a real two-tank exchange)."""
    r = run_arm(ArmParams(mode, ratio=1.5), n_common=N)
    assert r.w_d > 1.0 and r.w_q > 1.0
    assert abs((r.w_q / r.w_d) - 1.5) < 0.1, f"{mode}: w_q/w_d = {r.w_q / r.w_d:.3f} ≠ 3/2"

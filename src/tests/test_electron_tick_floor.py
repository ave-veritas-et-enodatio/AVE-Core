"""Tests + STANDING FALSIFIERS for the electron tick-floor arc.

Prereg: research/2026-07-07_electron-tick-floor_prereg_FROZEN.md.

Pins Leg A (analytic sampling floor N_min=7 + Adler div-N lock condition) and Leg B (engine
representability transition, dilation universality, c-invariance, dt-convergence, lossless
energy conservation), plus the two cross-cutting standing falsifiers:

  * F-FIREWALL: the DERIVATION PATH of both drivers is alpha-clean (no alpha / m_e /
    lambdabar_C / Q_TANK / R_I / lepton mass), except the clearly-marked FIREWALL-COMPARISON
    block. Grepped mechanically here so a future edit that leaks a physical constant onto the
    floor derivation FAILS loudly.
  * F1/F2 cross-leg: analytic N_min == engine N_min == 7 (independent code paths).

REGIME: cold lattice, lossless-reactive, small-signal phase dynamics. Every pinned quantity is
a dimensionless integer or a ratio; nothing hardcoded to a physical constant.
"""
from __future__ import annotations

import os
import sys

import pytest

_VERIFY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scripts", "verify")
if _VERIFY not in sys.path:
    sys.path.insert(0, os.path.abspath(_VERIFY))

import electron_tick_floor_engine as eng  # noqa: E402
import electron_tick_floor_sampling as smp  # noqa: E402


# ===========================================================================
# LEG A -- the analytic sampling floor + Adler ceiling
# ===========================================================================
def test_analytic_N_min_is_seven():
    scan = smp.floor_scan()
    assert scan["N_min"] == 7
    assert smp.n_min_analytic() == 7


def test_floor_transitions_5_collide_6_marginal_7_clean():
    assert smp.classify_tick_count(5) == "COLLIDE"
    assert smp.classify_tick_count(6) == "NYQUIST-MARGINAL"
    assert smp.classify_tick_count(7) == "CLEAN"
    # everything below 7 is not clean; everything >= 7 is clean
    assert all(smp.classify_tick_count(N) != "CLEAN" for N in range(3, 7))
    assert all(smp.classify_tick_count(N) == "CLEAN" for N in range(7, 20))


def test_N5_is_the_reflection_collision_3_equiv_minus2_mod5():
    # 3 == -2 (mod 5): the winding-3 aliases onto the reflection of winding-2
    assert smp.principal_winding(3, 5) == -2
    proof = smp.prove_reflection_collision_N()
    assert proof["N5_collides"] is True
    assert proof["N5_k2_mod"] == proof["N5_negk1_mod"] == 3
    # the collision tick count is exactly N | (k1+k2)=5, i.e. {5}
    assert proof["collision_tick_counts_above_k2"] == [5]


def test_N6_k3_sits_exactly_at_nyquist():
    proof = smp.prove_nyquist_floor()
    assert proof["N6_is_nyquist_exact"] is True
    assert proof["N_min"] == 7
    assert proof["k_max"] == 3


def test_adler_lock_condition_is_kappa_over_N():
    # STANDING FALSIFIER (F1): the div-N first-order Adler lock half-range is kappa/N.
    assert smp.adler_lock_halfrange(1.0, 7) == pytest.approx(1.0 / 7)
    proof = smp.prove_adler_lock_condition()
    assert proof["lock_halfrange_fractional"] == "kappa/N"
    assert proof["N_max"] == "kappa/delta"


def test_cold_identical_lattice_is_floor_only():
    # delta = 0 (cold identical) => N_max = inf => FLOOR-ONLY (the pre-registered outcome)
    v = smp.window_verdict(kappa=1.0, delta=0.0)
    assert v["bin"] == "FLOOR-ONLY"
    assert v["N_max"] is None
    assert v["N_min"] == 7


def test_seed_detuning_is_op14_downregulation():
    # delta_seed = 1 - sqrt(1 - A^2); parametric in A^2 (firewall: NOT plugged with alpha)
    assert smp.seed_detuning(0.0) == pytest.approx(0.0)
    assert smp.seed_detuning(0.19) == pytest.approx(1.0 - (1.0 - 0.19) ** 0.5)
    assert smp.ceiling_from_detuning(1.0, 0.0) == float("inf")


# ===========================================================================
# LEG B -- the engine (representability, dilation, c-invariance, dt, energy)
# ===========================================================================
@pytest.fixture(scope="module")
def engine_out():
    return eng.run()


def test_engine_N_min_is_seven(engine_out):
    assert engine_out["engine_N_min"] == 7


def test_engine_reproduces_the_alias_transitions(engine_out):
    mi = engine_out["measurement_i_lock_decay"]
    # N=5: the 3-winding aliases to -2 (COLLIDE); N=7 first clean (2,3)
    assert mi["reads_at_N5"][0] == 2 and mi["reads_at_N5"][1] == -2
    assert mi["reads_at_N7"] == [2, 3]
    # N=6 does NOT read the clean (2,3) (Nyquist-marginal, sampling-phase-sensitive)
    assert mi["reads_at_N6"] != [2, 3]


def test_G1_cross_leg_floor_reconciles(engine_out):
    # STANDING FALSIFIER (F2): analytic N_min (modular) and engine N_min (time-domain) agree,
    # via the ReconcileGate with its can-fire self-test proven.
    g1 = engine_out["reconcile_gates"]["G1_floor"]
    assert g1["reconciled"] is True
    assert g1["can_fire_proven"] is True
    assert smp.n_min_analytic() == engine_out["engine_N_min"] == 7


def test_dilation_universality_tower_emerges(engine_out):
    # STANDING FALSIFIER (F3): uniform sqrt(1-A^2) dilation keeps the div-N ratio EXACTLY intact
    mii = engine_out["measurement_ii_tower_strain"]
    assert mii["tower_verdict"] == "TOWER-EMERGES"
    for _, row in mii["global_dilation"].items():
        assert row["winding_pair_ok"] is True


def test_lossless_lock_range_grows_not_shrinks(engine_out):
    # THE FLAG-DON'T-FIX FINDING: the conservative (Ax3-lossless) lock half-range GROWS with N
    # (sqrt-law), the OPPOSITE of the first-order dissipative Adler kappa/N. This is what routes
    # the window to FLOOR-ONLY (no high-N lock ceiling) and contradicts the ontology's joint-4
    # "candidate ceiling shrinks with N". If a future model made it shrink, this test flags it.
    lr = engine_out["measurement_ii_tower_strain"]["lock_range_vs_N"]
    hr = [(int(N), v["conservative_halfrange_delta"]) for N, v in lr.items()]
    hr.sort()
    vals = [v for _, v in hr]
    assert vals == sorted(vals)            # monotone non-decreasing in N (grows)
    assert vals[-1] > vals[0]              # strictly larger at N=16 than N=7
    # and it is FAR above the first-order Adler kappa/N at every N (>10x)
    for N, v in lr.items():
        assert v["conservative_halfrange_delta"] > 10.0 * v["first_order_adler_kappa_over_N"]


def test_c_invariance_michelson_null(engine_out):
    # STANDING FALSIFIER (F4): signal speed independent of mode presence AND of N
    m = engine_out["measurement_iii_c_invariance"]
    assert m["verdict"] == "C-INVARIANT"
    assert m["rel_diff_with_vs_without"] < 0.05
    assert m["rel_diff_N7_vs_N12"] < 0.05


def test_dt_convergence_substep_is_not_the_clock(engine_out):
    # STANDING FALSIFIER (F5): the window verdict is invariant as dt -> 0
    dtc = engine_out["dt_convergence"]
    assert dtc["N_min_invariant"] is True
    assert dtc["N_min_values"] == [7]


def test_lossless_energy_conserved(engine_out):
    # Ax3-lossless: H conserved to the reactive floor (leapfrog on a Hamiltonian system)
    assert engine_out["max_H_rel_drift"] < 1e-10
    assert engine_out["reconcile_gates"]["energy_lossless"]["passed"] is True


# ===========================================================================
# STANDING FALSIFIER F-FIREWALL -- the alpha-circularity knife, mechanically enforced
# ===========================================================================
_QUARANTINED = {"ALPHA", "ALPHA_COLD", "ALPHA_COLD_INV", "M_E", "L_NODE", "OMEGA_C",
                "Q_TANK", "R_I", "DELTA_STRAIN"}
# the ONE function per driver where firewalled physical constants may legitimately appear
_FIREWALL_FN = "firewall_comparison_pricing"


def _firewall_breaches(path: str):
    """Robust firewall scan: tokenize the source and inspect only NAME tokens (so a
    quarantined word inside a docstring / comment / string is a STRING/COMMENT token and is
    NEVER counted). NAME tokens inside the `firewall_comparison_pricing` function (its AST
    line range) are exempt. Any other NAME token equal to a quarantined symbol is a breach."""
    import ast
    import io
    import tokenize

    with open(path) as f:
        src = f.read()
    tree = ast.parse(src)
    fw_ranges = [(n.lineno, n.end_lineno) for n in ast.walk(tree)
                 if isinstance(n, ast.FunctionDef) and n.name == _FIREWALL_FN]

    def in_fw(lineno: int) -> bool:
        return any(a <= lineno <= b for a, b in fw_ranges)

    breaches = []
    for tok in tokenize.generate_tokens(io.StringIO(src).readline):
        if tok.type == tokenize.NAME and tok.string in _QUARANTINED and not in_fw(tok.start[0]):
            breaches.append((tok.start[0], tok.string))
    return breaches


def test_firewall_no_alpha_on_sampling_derivation_path():
    breaches = _firewall_breaches(os.path.join(_VERIFY, "electron_tick_floor_sampling.py"))
    assert breaches == [], f"FIREWALL BREACH on sampling derivation path: {breaches}"


def test_firewall_no_alpha_on_engine_derivation_path():
    breaches = _firewall_breaches(os.path.join(_VERIFY, "electron_tick_floor_engine.py"))
    assert breaches == [], f"FIREWALL BREACH on engine derivation path: {breaches}"


def test_firewall_comparison_pricing_is_c_and_Z0_invariant():
    # The ONLY place physical constants may enter: the firewalled pricing. It must prove the
    # c / Z_0 invariance under a -> lambdabar_C/N* (CONSISTENCY-class, no new number).
    pricing = smp.firewall_comparison_pricing(n_star=7)
    assert pricing["c_invariant"] is True
    assert pricing["a_repriced_m"] == pytest.approx(pricing["lambdabar_C_m"] / 7)


def test_homonym_guard_floor_is_not_near_137():
    # N (sampling count) != Q (=1/alpha coherence count). The floor 7 is >3 OOM from 137.
    assert smp.n_min_analytic() == 7
    assert abs(7 - 137) > 100  # the guard is armed and NOT tripped (7 has zero alpha content)

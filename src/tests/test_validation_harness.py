"""Keepers for the ave.validation harness library (ENGINE-HARDENING ARC item 2).

Each of the five guards gets a positive + a negative test (the guard must both
PASS when it should and FAIL when it should — a guard that only ever passes is a
checklist, not a gate). Deterministic; canonical constants only; sub-second.
Gating-lane.
"""

import numpy as np
import pytest

import ave.validation as V
from ave.core.chiral_lattice import build_srs_net
from ave.solvers.srs_cage_winding import assemble_L_srs, build_incidence


@pytest.fixture(scope="module")
def srs_L():
    net = build_srs_net(L=3)
    B, bonds = build_incidence(net)
    L = assemble_L_srs(B, bonds, np.ones(net.n_nodes))
    return net, B, bonds, L


# ─────────────────────────────────────────────────────────────────────────────
# package wiring
# ─────────────────────────────────────────────────────────────────────────────
def test_all_guards_exported():
    for name in (
        "planted_source_control",
        "detect_global_sum_degeneracy",
        "detect_symmetry_forced_zero",
        "assert_runtime_independent",
        "stub_and_compare",
        "audit_solve_path",
        "spectral_liveness",
        "localized_eigenmode",
        "ReconcileGate",
        "reconcile",
        "assert_reconciled",
    ):
        assert hasattr(V, name), f"ave.validation must export {name}"


def test_spectral_liveness_is_reexport_not_duplicate():
    """(e) must be the SAME object as the solvers module (single source of truth)."""
    from ave.solvers import spectral_liveness as canonical

    assert V.spectral_liveness is canonical.spectral_liveness


# ─────────────────────────────────────────────────────────────────────────────
# (a) planted-source positive control
# ─────────────────────────────────────────────────────────────────────────────
def test_planted_source_registers_live_signal(srs_L):
    net, B, bonds, L = srs_L
    seed = np.random.default_rng(1).standard_normal(net.n_nodes)
    live_seed = V.project_out_nullspace(seed, L)

    def pipe(x):  # |L x|_max
        return float(np.max(np.abs(B.T @ (B @ x))))

    res = V.planted_source_control(pipe, live_seed, floor=1e-9, label="srs_live")
    assert res.passed
    assert res.registered and res.baseline_ok
    assert res.baseline < 1e-9  # zero-input hallucinates nothing


def test_planted_source_fails_dead_readout(srs_L):
    """A readout that returns 0 for EVERYTHING (a blind instrument) must NOT pass."""
    net, B, bonds, L = srs_L
    seed = V.project_out_nullspace(np.random.default_rng(2).standard_normal(net.n_nodes), L)

    def dead_pipe(x):
        return 0.0

    res = V.planted_source_control(dead_pipe, seed, floor=1e-9)
    assert not res.passed
    assert not res.registered  # the blind readout could not register the planted signal


def test_planted_source_rejects_null_input(srs_L):
    net, B, bonds, L = srs_L

    def const_pipe(x):
        return 1.0

    with pytest.raises(ValueError):
        V.planted_source_control(const_pipe, np.zeros(net.n_nodes))


# ─────────────────────────────────────────────────────────────────────────────
# (b) structural-degeneracy
# ─────────────────────────────────────────────────────────────────────────────
def test_global_sum_degeneracy_detected_on_closed_graph(srs_L):
    """L_srs annihilates the constant ⇒ the global divergence sum is forced to 0."""
    net, B, bonds, L = srs_L
    res = V.detect_global_sum_degeneracy(L)
    assert res.degenerate
    assert not res.safe_to_use  # the Stage-1 blind-readout trap: don't use the global sum
    assert res.kind == "global_sum_nullspace"


def test_global_sum_not_degenerate_for_full_rank_operator():
    """An operator WITHOUT the constant in its nullspace has an informative global sum."""
    rng = np.random.default_rng(3)
    M = rng.standard_normal((12, 12))
    M = M @ M.T + 3.0 * np.eye(12)  # SPD, full rank, constant NOT a null vector
    res = V.detect_global_sum_degeneracy(M)
    assert not res.degenerate
    assert res.safe_to_use


def test_symmetry_forced_zero_detected():
    """An observable that is odd under a flip is forced to zero for symmetric fields."""
    x = np.array([1.0, 2.0, 3.0, 4.0])

    def flip(v):  # reversal
        return v[::-1]

    def odd(v):  # genuinely odd under flip: o(v) = v[0]-v[-1] ⇒ o(flip v) = -o(v)
        return float(v[0] - v[-1])

    res = V.detect_symmetry_forced_zero(odd, x, flip)
    assert res.degenerate and not res.safe_to_use
    assert res.kind == "symmetry_forced_zero"


def test_symmetry_not_forced_for_even_observable():
    x = np.array([1.0, 2.0, 3.0, 4.0])

    def even(v):  # symmetric under reversal
        return float(v[0] + v[-1])

    def flip(v):
        return v[::-1]

    res = V.detect_symmetry_forced_zero(even, x, flip)
    assert not res.degenerate and res.safe_to_use


# ─────────────────────────────────────────────────────────────────────────────
# (c) runtime-independence
# ─────────────────────────────────────────────────────────────────────────────
def test_runtime_independent_when_dependency_unused(srs_L):
    net, B, bonds, L = srs_L

    def compute():
        return B.T @ (B @ np.ones(net.n_nodes))

    res = V.stub_and_compare(
        compute,
        module_path="ave.solvers.srs_cage_winding",
        attr="compute_Q_link_srs",
        stub=lambda *a, **k: {"Q_link": 999999},
        label="indep_of_Qlink",
    )
    assert res.passed and res.max_abs_diff == 0.0


def test_runtime_dependence_detected_when_dependency_used(srs_L):
    """If the compute DOES consume the stubbed attr, the output must move."""
    net, B, bonds, L = srs_L
    import ave.solvers.srs_cage_winding as scw

    omega = np.random.default_rng(4).standard_normal((net.n_nodes, 3))

    def compute_dep():
        r = scw.compute_Q_link_srs(net, omega, 7.0, 2.3, frame_N=16)
        return np.array([float(r["Q_link"])])

    res = V.stub_and_compare(
        compute_dep,
        module_path="ave.solvers.srs_cage_winding",
        attr="compute_Q_link_srs",
        stub=lambda net, om, R, r, *, frame_N, **k: {"Q_link": 999999, "w_tor": -7},
    )
    assert res.independent is False
    assert res.max_abs_diff > 0

    def compute_dep2():
        r = scw.compute_Q_link_srs(net, omega, 7.0, 2.3, frame_N=16)
        return np.array([float(r["Q_link"])])

    with pytest.raises(AssertionError):
        V.assert_runtime_independent(
            compute_dep2,
            module_path="ave.solvers.srs_cage_winding",
            attr="compute_Q_link_srs",
            stub=lambda net, om, R, r, *, frame_N, **k: {"Q_link": 999999, "w_tor": -7},
        )


# ─────────────────────────────────────────────────────────────────────────────
# (d) equation-audit
# ─────────────────────────────────────────────────────────────────────────────
def test_equation_audit_driver_clean_on_alpha_free_module():
    """srs_dec is α-clean in its OWN code (integer incidence); its guard-asserts
    must NOT self-fire, and its transitive closure α-leak is honestly reported."""

    def exercise():
        from ave.topological.srs_dec import build_srs_dec

        build_srs_dec(L=3)

    res = V.audit_solve_path("src/ave/topological/srs_dec.py", exercise=exercise)
    assert res.driver_clean, f"srs_dec falsely flagged: {res.forbidden_in_driver}"
    assert res.passed
    # scope honesty: the transitive closure DOES carry α (constants.py) — reported.
    assert any("constants.py" in h for h in res.forbidden_in_closure)


def test_equation_audit_flags_unallowlisted_solve_arg(tmp_path):
    """A driver whose solve-call routes an un-allowlisted arg must FAIL the audit."""
    rig = tmp_path / "rigged_driver.py"
    rig.write_text("def solve_static(x):\n    return x\n\n" "def run():\n    return solve_static(Q_link_source)\n")
    res = V.audit_solve_path(
        str(rig),
        solve_call_name="solve_static",
        allowed_solve_args=("source", "np.zeros(n"),
    )
    assert not res.solve_args_ok
    assert not res.passed
    assert any("Q_link_source" in u for u in res.unexpected_solve_args)


def test_equation_audit_scan_strips_comments_and_docstrings(tmp_path):
    """The grep-completeness trap: a module that only MENTIONS ALPHA in a comment /
    docstring is clean; only executable use counts."""
    from pathlib import Path

    from ave.validation.equation_audit import scan_forbidden_constants

    f = tmp_path / "mentions_only.py"
    f.write_text(
        '"""This module must never import ALPHA or Q_TANK."""\n'
        "# ALPHA is forbidden here\n"
        "x = 1  # not a use of Q_TANK\n"
    )
    hits = scan_forbidden_constants([Path(f)])
    assert hits == [], f"comment/docstring mention wrongly flagged: {hits}"

    g = tmp_path / "real_use.py"
    g.write_text("from ave.core.constants import ALPHA\ny = ALPHA * 2\n")
    hits2 = scan_forbidden_constants([Path(g)])
    assert any("ALPHA" in h for h in hits2), "a real import+use must be flagged"


# ─────────────────────────────────────────────────────────────────────────────
# (f) reconcile-gate — claim vs INDEPENDENT recompute; the halt MUST be able to fire
# ─────────────────────────────────────────────────────────────────────────────
def test_reconcile_gate_passes_on_true_reconcile():
    """POSITIVE: a claim that agrees with a genuinely different-code-path
    recomputation (trace vs eigenvalue sum) reconciles; the can-fire proof runs
    first and is recorded on the result."""
    A = np.random.default_rng(5).standard_normal((6, 6))
    A = A + A.T
    gate = V.ReconcileGate(
        label="trace_vs_eigsum",
        claimed=float(np.trace(A)),
        independent=lambda: float(np.sum(np.linalg.eigvalsh(A))),
        rtol=1e-10,
        atol=1e-12,
    )
    res = gate.enforce()  # prove_first=True default: liveness proven, THEN reconciled
    assert res.passed
    assert res.can_fire_proven
    assert res.max_rel_discrepancy < 1e-10


def test_reconcile_gate_halts_on_discrepancy():
    """NEGATIVE: a claim that disagrees with its independent recomputation must
    raise the loud DISCREPANT-HALT (hard path) and report not-passed (soft path)."""
    from ave.validation import DiscrepantHalt

    with pytest.raises(DiscrepantHalt):
        V.assert_reconciled(6.5, lambda: 6.3, rtol=1e-9, label="corrupted_claim")

    soft = V.reconcile(6.5, 6.3, rtol=1e-9, label="corrupted_claim_soft")
    assert not soft.passed
    assert soft.max_rel_discrepancy > 1e-2


def test_reconcile_gate_selftest_proves_can_fire():
    """POSITIVE (self-test): prove_can_fire injects a synthetic discrepancy through
    the SAME comparator+halt path and confirms the halt triggers — including for an
    exact-equality gate (rtol=atol=0)."""
    gate = V.ReconcileGate(label="live_plumbing", claimed=1.0, independent=1.0, rtol=1e-9)
    proof = gate.prove_can_fire()
    assert proof.passed and proof.can_fire_proven

    exact = V.ReconcileGate(label="exact_equality", claimed=1.0, independent=1.0, rtol=0.0)
    assert exact.prove_can_fire().can_fire_proven


def test_reconcile_gate_detects_dead_gate(monkeypatch):
    """NEGATIVE (self-test — THE #521/#526/#527 defect): a comparator that can
    never report disagreement must be caught by prove_can_fire as DeadGateError.
    Simulated by deadening the comparator, standing in for any future edit that
    makes the halt unreachable or algebraically incapable of firing."""
    import ave.validation.reconcile_gate as rg

    monkeypatch.setattr(rg, "_compare", lambda x, y, rtol, atol: (True, 0.0, 0.0, int(x.size)))
    gate = rg.ReconcileGate(label="deadened", claimed=1.0, independent=1.0, rtol=1e-9)
    with pytest.raises(rg.DeadGateError):
        gate.prove_can_fire()


def test_reconcile_gate_rejects_vacuous_tolerance():
    """NEGATIVE (registration): an infinite/NaN/negative tolerance is a checklist
    by construction — registration must refuse it."""
    for bad in (float("inf"), float("nan"), -1e-9):
        with pytest.raises(ValueError):
            V.ReconcileGate(label="vacuous", claimed=1.0, independent=1.0, rtol=bad)
        with pytest.raises(ValueError):
            V.ReconcileGate(label="vacuous", claimed=1.0, independent=1.0, rtol=1e-9, atol=bad)


def test_reconcile_gate_nan_and_shape_mismatch_never_reconcile():
    """NEGATIVE (rubber-stamp guards): a NaN claim or a shape-mismatched pair must
    never read as reconciled (NaN comparisons are False, not silently true)."""
    assert not V.reconcile(float("nan"), 1.0, rtol=1e-9).passed
    assert not V.reconcile(np.ones(2), np.ones(3), rtol=1e-9).passed


def test_reconcile_gate_soft_path_surfaces_evaluation_error():
    """A reference that cannot be computed is surfaced as an error string on the
    soft path (never a silent pass); the hard path lets the exception propagate."""
    res = V.reconcile(lambda: 1 / 0, 1.0, rtol=1e-9, label="broken_claim")
    assert not res.passed
    assert isinstance(res.reconciled, str) and "error" in res.reconciled

    with pytest.raises(ZeroDivisionError):
        V.assert_reconciled(lambda: 1 / 0, 1.0, rtol=1e-9, prove_first=False)

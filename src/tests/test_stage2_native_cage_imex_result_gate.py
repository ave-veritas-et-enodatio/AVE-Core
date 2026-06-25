"""Stage-2 native-cage IMEX make-or-break — RESULT GATE (CI-blocking, fast).

This asserts the COMMITTED make-or-break results JSON
(results/engine_stage2_native_cage_imex_makeorbreak_results.json) carries the
energy-certified MODE-III DISPERSE FALSIFICATION at the certification tolerance,
so the corpus's reported Stage-2 verdict cannot silently drift from the
committed evidence. It is the fast, deterministic complement to the live-run
GX1-GX5 gates in test_stage2_native_cage_imex.py (GX2 is THE energy-conservation
gate; this gate binds the resulting VERDICT + bins + energy proof).

WHAT THIS GATE IS (settled negative, framing-locked):
  bulk self-trap RULED OUT (Cartesian-grid artifact) ; boundary/topological
  localization STANDS. mass = A1 (PR#260) is UNTOUCHED — only the localization
  MECHANISM changed (bulk self-focus -> winding + H_couple pin the A1 core).

LOCALIZER RELABEL (2026-06-24 second pass — supersedes "winding + H_couple pin the
A1 core" above; the Stage-2 DISPERSE verdict this gate binds is UNCHANGED): the
S3 cavity-pinning result (DISPERSE-FALSIFIED) + the coupled eigensolve (#415) +
the phase-space coupling-winding BREAK (#417) read NEGATIVE in BOTH internal
dynamical loci — winding + H_couple does NOT pin the dispersing A1 core. The
surviving localizer is the Γ=−1 boundary CAVITY-eigenmode (fork-b A1 mass cavity
EXISTS); the (2,3) winding RIDES the cage as STATIC charge (Link, un-walked-back).
mass = A1 (#260) untouched. See research/2026-06-24_engine-reroute-epic-summary.md.

Re-generate the JSON with:
  PYTHONPATH=src python src/scripts/engine_stage2_native_cage_imex_makeorbreak.py

α-CLEAN: no ALPHA / Q_TANK / 137 / 0.00729 anywhere.
"""

import json
import pathlib

import pytest

_REPO = pathlib.Path(__file__).resolve().parents[2]
_RESULTS = _REPO / "results" / "engine_stage2_native_cage_imex_makeorbreak_results.json"


@pytest.fixture(scope="module")
def result():
    assert _RESULTS.exists(), f"committed make-or-break results JSON missing: {_RESULTS}"
    return json.loads(_RESULTS.read_text())


def test_final_verdict_is_energy_certified_mode_iii_falsification(result):
    """The headline: MODE-III DISPERSE FALSIFICATION, energy-gate certified.
    This is the make-or-break verdict — a clean negative, NOT debugged to rescue."""
    final = result["FINAL"]
    assert final["mode"] == "MODE_III_DISPERSE_FALSIFICATION", (
        f"committed verdict drifted: {final['mode']!r} != MODE_III_DISPERSE_FALSIFICATION"
    )
    assert result["primary_N24"]["verdict"] == "MODE_III_DISPERSE"


def test_energy_conservation_certified_at_tolerance(result):
    """THE certification: the integrator is non-dissipative, so the dispersal is
    PHYSICS not numerical damping. Bind the certified tolerances (the analog of
    the live GX2 gate, frozen against the committed run)."""
    proof = result["FINAL"]["energy_conservation_proof"]
    assert proof["verdict_is_physical_not_numerical"] is True
    # rel_drift over the whole run is ~1e-5 — energy is conserved to 5 digits.
    assert abs(proof["rel_drift_end"]) < 1e-3, (
        f"energy rel_drift {proof['rel_drift_end']:.2e} exceeds certification tol 1e-3"
    )
    # numerical 1/Q must be << any physical O(1) effect over the run.
    assert abs(proof["inv_Q_numerical"]) < 1e-3, (
        f"numerical 1/Q {proof['inv_Q_numerical']:.2e} not << physical effect"
    )
    assert proof["Q_numerical"] > 1e6, (
        f"Q_numerical {proof['Q_numerical']:.2e} too low — instrument bleeds energy"
    )
    assert proof["n_periods_resolved"] >= 5.0, (
        f"energy proof must span >=5 periods, got {proof['n_periods_resolved']:.1f}"
    )
    # The production N=24 energy gate itself must have PASSED.
    assert result["energy_conservation_gate_N24"]["passed"] is True


def test_mode_i_persist_bins_fail_as_designed(result):
    """The A-stall signature: the seeded sech does NOT clear the Mode-I PERSIST
    bar. Mode-I requires ALL bins true; here I-5 (above the radiation floor) is
    FALSE — the core stalls AT the seed level then sheds (disperses), it does NOT
    self-focus into a persistent bound core. Bind that exact failing bin so a
    silent bin-redefinition (dropping the discriminator) is caught."""
    bins = result["primary_N24"]["bins"]
    assert bins["I-5 above radiation floor (>1.5x gaussian late)"] is False, (
        "the radiation-floor discriminator must FAIL (Mode-III) — a True here "
        "would be Mode-I PERSIST; do not relax/drop the discriminator post-hoc"
    )
    assert not all(bins.values()), "all-bins-true would be Mode-I — must NOT hold"


def test_core_stalls_at_seed_does_not_self_focus(result):
    """A-stall, quantitatively: max|V| over the run stays at the seed amplitude
    (~0.85) and does NOT self-focus above it. The earlier explicit run's apparent
    self-focus past A->1 was the CFL blow-up + PML sponge-injection artifact."""
    sech = result["primary_N24"]["sech"]
    assert sech["max_abs_over_run"] <= 0.85 * (1.0 + 1e-2), (
        f"core self-focused above seed (max|V|={sech['max_abs_over_run']:.4f}) — "
        "the artifact has regressed"
    )
    assert result["primary_N24"]["physical_adjudication"]["physical_rupture"] is False
    assert result["primary_N24"]["physical_adjudication"]["bounded_under_stable_integration"] is True


def test_verdict_is_dt_stable_and_n_robust(result):
    """The verdict the explicit run could NOT deliver: dt-convergence-stable and
    N-robust. Every finer dt and every N agrees on MODE_III_DISPERSE."""
    assert result["dt_verdict_stable"] is True
    assert result["dt_no_detonation"] is True
    for tag, d in result["dt_convergence"].items():
        assert d["verdict"] == "MODE_III_DISPERSE", f"dt sweep {tag} disagrees: {d['verdict']}"
        assert d["physical_rupture"] is False, f"dt sweep {tag} ruptured"
    assert result["n_robust_agree"] is True
    for Nn, d in result["n_robustness"].items():
        assert d["verdict"] == "MODE_III_DISPERSE", f"N={Nn} disagrees: {d['verdict']}"


def test_apparatus_validity_known_goods(result):
    """The instrument is valid: the Cartesian v14 reference DOES self-trap
    (Mode-I reproduced) and the matched Gaussian control DOES disperse — so the
    native sech's dispersal is the substrate's verdict, not a dead apparatus."""
    assert result["known_good_cartesian_v14_C1"]["reproduces_v14_mode_i"] is True, (
        "Cartesian v14 reference must reproduce Mode-I (continuum cross-check) — "
        "if it doesn't, the apparatus is broken, not the substrate"
    )
    assert result["known_good_gaussian_control"]["disperses"] is True
    assert result["apparatus_valid_control_disperses"] is True

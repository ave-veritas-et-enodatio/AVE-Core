"""Regression tests for manuscript/ave-kb/tools/verify-solidity-ratchet.py.

Asserts:
  * the tool's own can-it-fire + negative-control gate holds, driven through the
    real scan() against a throwaway git repo;
  * the mutation receipt holds: each listed rule, switched off, breaks every fixture
    it names by changing a verdict, and a rule that does less fails the receipt;
  * the JSONL reconstruction agrees with the Markdown pipeline on the live KB. That is
    a property of the tree and pins no count, so it survives any KB edit. The live KB
    has no numeric support or run experiment, so the fixtures carry those branches;
  * the verdict numbers on the fixtures, computed here by hand from the min rule;
  * what the report says, including why a line was refused, and that the exit codes
    hold from a subdirectory;
  * the exit codes: 1 on an unexplained cut, 0 on a receipted one, 2 on each failure
    the gate must not read as clean, a crash included, in every mode.

The tests of main() that are not about the self-gate stub it, because they would each
pay for the whole of it again.
"""

import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace

import pytest

_TOOL = Path(__file__).resolve().parent.parent / "verify-solidity-ratchet.py"
_REPO_ROOT = Path(__file__).resolve().parents[4]


def _load_module():
    spec = importlib.util.spec_from_file_location("verify_solidity_ratchet", _TOOL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ratchet = _load_module()
lib = ratchet.lib


@pytest.fixture
def fixture_repo():
    root = tempfile.mkdtemp(prefix="solidity-ratchet-test-")
    repo = ratchet.Repo(cwd=root, scrub_env=True)
    repo.git("init", "-q")
    yield repo, root
    shutil.rmtree(root, ignore_errors=True)


@pytest.fixture
def no_self_gate(monkeypatch):
    monkeypatch.setattr(ratchet, "run_gate", lambda out=None: [])


def _scan(fixture_repo, tip_spec, tip_files=(), base_spec=None):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec() if base_spec is None else base_spec)
    tip = ratchet.tree(repo, root, tip_spec, tip_files)
    return repo, base, tip, ratchet.scan(repo, base, tip)


def _case(fixture_repo, name):
    c = ratchet.CASES[name]
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, c["base"], c["base_files"])
    return ratchet.scan(repo, base, ratchet.tree(repo, root, c["tip"], c["files"]))


def _flagged(res, field="holds"):
    return {ratchet.pair(f["edge"]): f[field] for f in res["findings"]}


def test_self_gate_holds():
    assert ratchet.run_gate(out=lambda line: None) == []


def test_a_hook_git_dir_cannot_reach_the_fixtures(monkeypatch):
    monkeypatch.setenv("GIT_DIR", "/nonexistent/.git")
    assert ratchet.run_gate(out=lambda line: None, only=("cut-binding",)) == []


def test_a_real_run_scrubs_trace_output_and_keeps_the_rest_of_git_env(monkeypatch):
    monkeypatch.setenv("GIT_TRACE", "1")
    monkeypatch.setenv("GIT_TRACE2_EVENT", "1")
    monkeypatch.setenv("GIT_DIR", "/kept/.git")
    env = ratchet.Repo().env
    assert "GIT_TRACE" not in env and "GIT_TRACE2_EVENT" not in env and env["GIT_DIR"] == "/kept/.git"


@pytest.mark.parametrize("stderr, clean", [
    (b"", True), (b"warning: core.fsyncObjectFiles is deprecated\n", True), (b"warning: \xff\n", True),
    (b"warned: nothing\n", False),
    (b"error: unable to read 1234\n", False), (b"warning: x\nfatal: y\n", False),
    (b"Auto packing the repository\n", False), (b"error: a warning: inside\n", False)])
def test_strict_passes_a_warning_and_nothing_else(monkeypatch, stderr, clean):
    monkeypatch.setattr(ratchet.subprocess, "run", lambda *a, **k: SimpleNamespace(
        returncode=0, stdout=b"out", stderr=stderr))
    if clean:
        assert ratchet.Repo().git("grep", strict=True) == "out"
    else:
        with pytest.raises(ratchet.GateError):
            ratchet.Repo().git("grep", strict=True)
    assert ratchet.Repo().git("grep") == "out"


def test_mutation_receipt_holds_and_leaves_no_mutation_on():
    assert ratchet.mutation_receipt() == 0
    assert ratchet.MUTATE == set()


def test_every_mutation_names_fixtures_that_exist():
    named = {name for cases, _ in ratchet.MUTATIONS.values() for name in cases}
    assert named <= set(ratchet.CASES) | set(ratchet.ABORTS)


def test_a_rule_that_breaks_nothing_fails_the_receipt(monkeypatch):
    monkeypatch.setattr(ratchet, "MUTATIONS", {"not-a-rule": (("unchanged",), "does nothing")})
    assert ratchet.mutation_receipt() == 1


def test_a_rule_must_break_every_fixture_it_names(monkeypatch):
    monkeypatch.setattr(ratchet, "MUTATIONS", {"no-restore": (("cut-binding", "unchanged"), "half a probe")})
    assert ratchet.mutation_receipt() == 1


def test_a_probe_that_only_crashes_fails_the_receipt_as_a_2(monkeypatch):
    def boom(*args):
        raise ratchet.GateError("crashed")

    monkeypatch.setattr(ratchet, "MUTATIONS", {"no-restore": (("cut-binding",), "crashes")})
    monkeypatch.setattr(ratchet, "scan", boom)
    assert ratchet.mutation_receipt() == 2


def test_a_crash_on_any_rule_of_the_receipt_is_a_2_not_only_on_the_last(monkeypatch):
    real = ratchet.scan

    def boom(*args):
        if "no-restore" in ratchet.MUTATE:
            raise ratchet.GateError("crashed")
        return real(*args)

    monkeypatch.setattr(ratchet, "MUTATIONS", {"no-restore": (("cut-binding",), "crashes"),
                                               "any-rise": (("unchanged",), "breaks nothing")})
    monkeypatch.setattr(ratchet, "scan", boom)
    assert ratchet.mutation_receipt() == 2


def test_a_fixture_that_raises_is_a_2_and_a_wrong_verdict_a_1_in_the_selftest(monkeypatch):
    monkeypatch.setitem(ratchet.CASES, "unchanged", {**ratchet.CASES["unchanged"], "rc": 1})
    assert ratchet.selftest() == 1

    def boom(*args):
        raise ratchet.GateError("git grep exited 128")

    monkeypatch.setattr(ratchet, "scan", boom)
    assert ratchet.selftest() == 2


def test_only_a_gate_error_counts_as_an_abort(monkeypatch):
    def boom(*args):
        raise KeyError("source")

    monkeypatch.setattr(ratchet, "scan", boom)
    with pytest.raises(KeyError):
        ratchet.run_gate(out=lambda line: None, only=("stale-index",))


@pytest.mark.parametrize("wrong", [{"rc": 1}, {"flagged": {ratchet.CUT}}, {"others": {ratchet.CITE}}])
def test_the_self_gate_compares_every_expected_field(monkeypatch, wrong):
    monkeypatch.setitem(ratchet.CASES, "unchanged", {**ratchet.CASES["unchanged"], **wrong})
    assert ratchet.run_gate(out=lambda line: None, only=("unchanged",)) != []


def test_committed_index_reproduces_from_its_own_records():
    index = _REPO_ROOT / "manuscript/ave-kb/.index"
    read = lambda name: [json.loads(line) for line in (index / name).read_text(encoding="utf-8").split("\n") if line]
    graph = ratchet.Graph(read("claims.jsonl"), read("depends-on.jsonl"))
    assert graph.claims and graph.edges
    ratchet.check_whole(graph, "working tree")
    ratchet.reconcile(graph, "working tree")


def test_reconstruction_agrees_with_the_markdown_pipeline():
    index = _REPO_ROOT / "manuscript/ave-kb/.index"
    read = lambda name: [json.loads(line) for line in (index / name).read_text(encoding="utf-8").split("\n") if line]
    finals, sups = ratchet.solve(ratchet.Graph(read("claims.jsonl"), read("depends-on.jsonl")))
    state = lib.discover_kb(_REPO_ROOT / "manuscript/ave-kb", diagnostic_stream=None)
    full = lib.compute_solidity_full(state.claim_entries, state.experiments, state.supports)
    assert finals == {c: r.final for c, r in full.items()}
    assert sups == dict(full.sup_solidity)


def test_bands_run_lowest_first_and_pending_sits_below_every_number():
    assert ratchet.rank(None) == 0
    values = [n / 100 for n in range(101)]
    assert [ratchet.rank(v) for v in values] == sorted(ratchet.rank(v) for v in values)
    assert len(ratchet.BANDS) == 6


def test_cut_binding_reports_the_hand_computed_values(fixture_repo):
    _, _, _, res = _scan(fixture_repo, ratchet.spec(deps=ratchet.without(ratchet.CUT)))
    # base CITE = min(0.85, 0.30, 0.90) = 0.30; the cut frees it to min(0.85, 0.90) = 0.85.
    assert res["tip"][ratchet.CITE] == 0.85 and res["base"][ratchet.CITE] == 0.30
    assert [f["holds"] for f in res["findings"]] == [{ratchet.CITE: 0.30, ratchet.DOWN: 0.30}]


def test_a_claim_a_single_edge_reaches_is_not_also_called_joint(fixture_repo):
    res = _case(fixture_repo, "cut-two-binding")
    # X reads 0.30 and 0.50 through its two deps. The lower one alone explains 0.30.
    assert _flagged(res) == {(ratchet.X, ratchet.W): {ratchet.X: 0.30}, (ratchet.X, ratchet.Z): {ratchet.X: 0.50}}
    assert all(f["jointly"] == {} for f in res["findings"])


def test_cut_that_stops_a_fall_never_rose_and_still_fires(fixture_repo):
    claims = {**ratchet.spec()["claims"], ratchet.WEAK: 0.10, ratchet.CITE: 0.40}
    _, _, _, res = _scan(fixture_repo, ratchet.spec(deps=ratchet.without(ratchet.CUT), claims=claims))
    assert res["base"][ratchet.CITE] == 0.30 and res["tip"][ratchet.CITE] == 0.40
    assert lib.derive_build_band(0.30) == lib.derive_build_band(0.40)
    assert res["findings"][0]["holds"] == {ratchet.CITE: 0.10, ratchet.DOWN: 0.10}


def test_joint_only_lift_flags_both_edges(fixture_repo):
    res = _case(fixture_repo, "joint-only")
    # Either support alone keeps LIFT at 0.90; both restored read 0.30 x 1.0.
    assert res["tip"][ratchet.LIFT] == 0.90
    assert _flagged(res, "jointly") == {pair: {ratchet.LIFT: 0.30} for pair in ratchet.SUPS}
    assert _flagged(res) == {pair: {} for pair in ratchet.SUPS}


def test_a_named_claim_cannot_hide_a_lower_joint_reading(fixture_repo):
    res = _case(fixture_repo, "joint-masked-series")
    # X single-handedly reads 0.50 through Z; X -> M -> W takes it to 0.30 together.
    assert _flagged(res)[(ratchet.X, ratchet.Z)] == {ratchet.X: 0.50}
    assert _flagged(res, "jointly")[(ratchet.X, ratchet.M)] == {ratchet.X: 0.30}
    assert _flagged(res, "jointly")[(ratchet.M, ratchet.W)] == {ratchet.X: 0.30}
    assert _flagged(res, "jointly")[(ratchet.X, ratchet.Z)] == {}


def test_a_receipt_on_one_edge_leaves_the_others_owed(fixture_repo):
    res = _case(fixture_repo, "joint-after-receipt")
    # M at 0.20 caps X alone, below the 0.30 the two support edges reach. With X -> M
    # receipted those two still take X from 0.90 to 0.30.
    assert _flagged(res, "receipt")[(ratchet.X, ratchet.M)] == ratchet.NOTE
    assert _flagged(res, "jointly")[(ratchet.SUP1, ratchet.W)] == {ratchet.X: 0.30}
    assert _flagged(res, "receipt")[(ratchet.SUP2, ratchet.W)] is None


def test_every_layer_of_a_joint_shows_in_one_report(fixture_repo):
    res = _case(fixture_repo, "joint-two-layers")
    assert _flagged(res, "jointly") == {
        (ratchet.SUP1, ratchet.W): {ratchet.X: 0.30}, (ratchet.SUP2, ratchet.W): {ratchet.X: 0.30},
        (ratchet.SUP1, ratchet.M): {ratchet.X: 0.50}, (ratchet.SUP2, ratchet.M): {ratchet.X: 0.50}}


@pytest.mark.parametrize("name, edge, carried", [
    ("receipt-frees-series", ("M", "W"), "X"), ("receipt-frees-parallel", ("SUP1", "W"), "X")])
def test_a_receipt_can_free_a_partner_and_what_it_carries_still_prints(fixture_repo, capsys, name, edge, carried):
    # With M -> W gone for good, X -> M binds X to 0.90, which is where X reads. With one of
    # two parallel support edges gone for good, that support lifts X, so the other is slack.
    res = _case(fixture_repo, name)
    assert [ratchet.pair(f["edge"]) for f in res["findings"]] == [(getattr(ratchet, edge[0]), ratchet.W)]
    assert res["carried"] == [ratchet.X]
    assert ratchet.report(res, "b" * 8, "t" * 8) == 0
    assert "held up by the removed edges: %s at ok-to-build (0.9); with them back it reads do-not-build (0.3)" % (
        ratchet.X) in capsys.readouterr().out


def test_a_claim_a_line_already_names_is_not_printed_again(fixture_repo):
    for name in ("cut-binding", "receipt", "cut-two-binding", "joint-only"):
        assert _case(fixture_repo, name)["carried"] == []


def test_two_routes_name_one_set_and_never_a_bystander(fixture_repo):
    res = _case(fixture_repo, "joint-bystander")
    assert _flagged(res, "jointly") == {
        (ratchet.X, ratchet.M2): {ratchet.X: 0.30}, (ratchet.M2, ratchet.W): {ratchet.X: 0.30},
        (ratchet.M, ratchet.W): {}}
    assert len(res["gone"]) == 5


def test_a_slack_dep_that_rounds_a_reading_up_is_not_blamed(fixture_repo):
    res = _case(fixture_repo, "slack-rounds-up")
    # The solve rounds only with a dep, so X -> Z restored reads 0.65 where the two
    # support edges alone read 0.648. Z is 0.99 and holds nothing.
    assert res["tip"][ratchet.X] == 0.855
    assert _flagged(res, "jointly") == {
        (ratchet.SUP1, ratchet.W): {ratchet.X: 0.648}, (ratchet.SUP2, ratchet.W): {ratchet.X: 0.648}}


def test_slack_edge_is_not_blamed_for_a_joint_effect(fixture_repo):
    res = _case(fixture_repo, "joint-plus-slack")
    assert (ratchet.CITE, ratchet.SOLID) not in _flagged(res)


def test_reversed_edge_fails_closed_as_uncomputable(fixture_repo):
    res = _case(fixture_repo, "reversed-edge")
    assert [f["cycle"] for f in res["findings"]] == ["alone"]
    assert res["stuck"] == [ratchet.CUT]


def test_cycle_closed_only_by_two_edges_flags_those_two(fixture_repo):
    res = _case(fixture_repo, "joint-cycle-plus-slack")
    assert {ratchet.pair(f["edge"]) for f in res["findings"] if f["cycle"]} == {
        (ratchet.X, ratchet.Y), (ratchet.Z, ratchet.M)}
    assert {f["cycle"] for f in res["findings"]} == {"jointly"}
    assert len(res["gone"]) == 3


def test_two_cycles_blame_their_own_edges_and_a_binding_edge_keeps_its_cause(fixture_repo, capsys):
    res = _case(fixture_repo, "two-cycles")
    assert _flagged(res, "cycle") == {
        (ratchet.X, ratchet.Y): "jointly", (ratchet.Z, ratchet.M): "jointly",
        (ratchet.P, ratchet.Q): "jointly", (ratchet.R, ratchet.S): "jointly", (ratchet.M2, ratchet.W): None}
    assert len(res["stuck"]) == 2 and res["others"] == []
    ratchet.report(res, "b" * 8, "t" * 8)
    out = capsys.readouterr().out
    assert "%s -x-> %s  UNEXPLAINED\n     holds %s at" % (ratchet.M2, ratchet.W, ratchet.M2) in out
    assert ratchet.NEAR not in out
    assert "restoring it with %s -> %s closes a cycle" % (ratchet.Z, ratchet.M) in out
    assert "restoring it with %s -> %s closes a cycle" % (ratchet.R, ratchet.S) in out


def test_raised_confidence_is_reported_but_not_gated(fixture_repo, capsys):
    res = _case(fixture_repo, "raised-confidence")
    assert res["findings"] == []
    assert ratchet.CITE in res["others"] and ratchet.DOWN in res["others"]
    assert ratchet.report(res, "b" * 8, "t" * 8) == 0
    assert "not gated: %s" % ratchet.CITE in capsys.readouterr().out


def test_a_claim_that_rose_both_ways_shows_both(fixture_repo, capsys):
    res = _case(fixture_repo, "rise-by-two-routes")
    # CITE reads 0.30 at the base and 0.85 at the tip. Restoring the edge gives 0.60:
    # the cut owns 0.60 -> 0.85, the raised confidence owns 0.30 -> 0.60.
    assert _flagged(res)[ratchet.CUT][ratchet.CITE] == 0.60
    assert res["others"] == [ratchet.CITE, ratchet.DOWN]
    assert res["after"][ratchet.CITE] == 0.60
    assert ratchet.report(res, "b" * 8, "t" * 8) == 1
    out = capsys.readouterr().out
    assert "holds %s at ok-to-build (0.85); restored it reads input-only (0.6)" % ratchet.CITE in out
    assert "not gated: %s  do-not-build -> input-only" % ratchet.CITE in out


def test_retiring_an_intermediate_does_not_freeze_it(fixture_repo):
    res = _case(fixture_repo, "retired-dep-moved")
    # Z fell to 0.10. X only escapes that because M went with its edges.
    assert res["tip"][ratchet.X] == 0.85
    assert _flagged(res, "jointly")[(ratchet.X, ratchet.M)] == {ratchet.X: 0.10}


def test_remint_is_tested_as_if_the_claim_had_stayed(fixture_repo):
    res = _case(fixture_repo, "remint-no-citers")
    assert _flagged(res) == {(ratchet.X, ratchet.W): {ratchet.X: 0.63}}
    assert res["retired"] == [ratchet.X]
    assert res["tip"][ratchet.X] == 0.95


def test_a_retired_claim_keeps_its_authored_lifts_and_experiments(fixture_repo):
    lifted = ratchet.graph_spec({ratchet.X: .10, ratchet.W: .30}, [(ratchet.X, ratchet.W)],
                                {ratchet.SUP1: .90}, [(ratchet.SUP1, ratchet.X)])
    res = _scan(fixture_repo, ratchet.graph_spec({ratchet.W: .30}), base_spec=lifted)[-1]
    assert res["tip"][ratchet.X] == 0.90
    assert _flagged(res) == {(ratchet.X, ratchet.W): {ratchet.X: 0.30}}
    # W left and read 0.90 only through a run experiment, so X -> W binds nothing.
    res = _case(fixture_repo, "retired-run-lift")
    assert res["tip"][ratchet.W] == 0.90 and res["findings"] == []


@pytest.mark.parametrize("name", ["remint-keeps-dep", "split-keeps-dep", "retired-dead-leaf"])
def test_a_faithful_remint_or_a_dead_leaf_fires_on_the_retired_reading_alone(fixture_repo, name):
    res = _case(fixture_repo, name)
    assert _flagged(res) == {(ratchet.X, ratchet.W): {ratchet.X: 0.55}}
    assert res["retired"] == [ratchet.X]


def test_a_remint_that_raises_confidence_clears_the_fire_and_prints_the_new_id(fixture_repo, capsys):
    res = _case(fixture_repo, "remint-raised")
    assert res["findings"] == [] and res["new"] == [ratchet.Y]
    assert ratchet.report(res, "b" * 8, "t" * 8) == 0
    assert "new at the tip: %s  ok-to-build (0.95)" % ratchet.Y in capsys.readouterr().out


def test_remint_of_a_support_counts_the_edge_and_prints_the_lift_as_untested(fixture_repo, capsys):
    res = _case(fixture_repo, "remint-support")
    # The old support does not come back with its lifts, so its edge has nothing to bind to.
    assert len(res["gone"]) == 1 and res["findings"] == [] and res["stuck"] == [(ratchet.SUP1, ratchet.W)]
    assert res["others"] == [ratchet.X]
    assert ratchet.report(res, "b" * 8, "t" * 8) == 0
    out = capsys.readouterr().out
    assert "not tested: %s  do-not-build -> ok-to-build  (0.3 -> 0.9)" % ratchet.X in out
    assert "left out of the restore: %s -> %s." % (ratchet.SUP1, ratchet.W) in out


def test_a_support_back_only_for_a_retired_claim_still_counts_as_left_out(fixture_repo, capsys):
    base = ratchet.graph_spec({ratchet.X: .10, ratchet.W: .30, ratchet.M: .95, ratchet.Z: .99},
                              [(ratchet.SUP1, ratchet.W), (ratchet.M, ratchet.Z)], {ratchet.SUP1: .90},
                              [(ratchet.SUP1, ratchet.X), (ratchet.SUP1, ratchet.M)])
    tip = ratchet.graph_spec({ratchet.X: .10, ratchet.W: .30, ratchet.Z: .99}, sups={ratchet.SUP2: .90},
                             gives=[(ratchet.SUP2, ratchet.X)])
    res = _scan(fixture_repo, tip, base_spec=base)[-1]
    assert (ratchet.SUP1, ratchet.W) in res["stuck"] and res["others"] == [ratchet.X]
    assert ratchet.report(res, "b" * 8, "t" * 8) == 0
    assert "not tested: %s" % ratchet.X in capsys.readouterr().out


def test_a_cycle_leaves_out_only_the_edges_that_would_close_it(fixture_repo):
    assert len(_case(fixture_repo, "joint-cycle")["stuck"]) == 1
    assert len(_case(fixture_repo, "joint-cycle-half-receipted")["stuck"]) == 1


@pytest.mark.parametrize("name", ["joint-cycle", "joint-cycle-half-receipted"])
def test_an_edge_left_out_is_named_even_with_no_rise(fixture_repo, capsys, name):
    res = _case(fixture_repo, name)
    assert res["stuck"] and res["others"] == []
    ratchet.report(res, "b" * 8, "t" * 8)
    out = capsys.readouterr().out
    assert "other-band-rises=0 (not gated)" in out
    assert "left out of the restore: %s -> %s." % res["stuck"][0] in out


def test_a_claim_named_at_a_shallow_reading_still_shows_the_band_receipts_carry(fixture_repo, capsys):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.SERIES)
    lines = "\n".join(ratchet.says(*e) for e in ratchet.SERIES["deps"])
    tip = ratchet.tree(repo, root, ratchet.no_deps(ratchet.SERIES), ratchet.note(lines))
    res = ratchet.scan(repo, base, tip)
    # X -> Z alone reads 0.50. The chain through M, receipted, takes X to 0.30.
    assert res["carried"] == [ratchet.X]
    assert ratchet.report(res, "b" * 8, "t" * 8) == 0
    assert "with them back it reads do-not-build (0.3)" in capsys.readouterr().out


def test_a_rise_the_tip_never_made_is_not_printed(fixture_repo):
    res = _case(fixture_repo, "rounding-no-phantom-rise")
    # The tip reads 0.648, the band of the base's 0.54. Only the restore rounds it to 0.65.
    assert res["tip"][ratchet.X] == 0.648 and res["after"][ratchet.X] == 0.65 and res["others"] == []


def test_only_an_edge_into_a_claim_counts_as_removed(fixture_repo):
    assert _case(fixture_repo, "axiom-cut")["gone"] == []


def test_a_restore_that_raises_a_band_holds_nothing(fixture_repo):
    res = _case(fixture_repo, "restore-raises")
    # The solve rounds only with a dep: X reads 0.648 at the tip and 0.65 restored.
    assert res["tip"][ratchet.X] == 0.648 and res["after"][ratchet.X] == 0.65
    assert res["findings"] == [] and res["carried"] == []


def test_rounding_can_fire_with_no_band_moved(fixture_repo):
    res = _case(fixture_repo, "rounding-holds-a-band")
    # 0.93 x 0.9 at the tip, 0.648 with the support's dep back, 0.65 with both back.
    band = lib.derive_build_band(0.65)
    assert [lib.derive_build_band(res[k][ratchet.X]) for k in ("base", "tip", "after")] == [band] * 3
    assert _flagged(res) == {(ratchet.SUP1, ratchet.W): {ratchet.X: 0.648}}


def test_fractional_lift_and_run_experiment_values(fixture_repo):
    res = _case(fixture_repo, "sup-fraction")
    # 0.90 x 0.5 at the tip, 0.30 x 0.5 restored.
    assert res["tip"][ratchet.LIFT] == 0.45
    assert all(f["jointly"] == {ratchet.LIFT: 0.15} for f in res["findings"])
    assert _case(fixture_repo, "exp-rescue")["tip"][ratchet.CITE] == 0.90


def test_receipt_paths_survive_spaces_and_lines_may_end_in_crlf(fixture_repo):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    tip = ratchet.tree(repo, root, ratchet.spec(), ((
        "research/a b.md", ratchet.LINE + "\r\n"),))
    assert ratchet.receipts(repo, base, tip, ())[0] == {ratchet.CUT: "research/a b.md"}


def test_an_edge_receipted_twice_names_the_first_file(fixture_repo):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    tip = ratchet.tree(repo, root, ratchet.spec(), ratchet.note(ratchet.LINE, "research/a.md")
                       + ratchet.note(ratchet.LINE, "research/b.md"))
    assert ratchet.receipts(repo, base, tip, ())[0] == {ratchet.CUT: "research/a.md"}


def _edge(source, target):
    return {"source": source, "target": target}


def test_a_line_behind_a_bare_cr_is_not_a_receipt(fixture_repo):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    tip = ratchet.tree(repo, root, ratchet.spec(), ((ratchet.NOTE, "old\r" + ratchet.LINE + "\n"),))
    found, refused = ratchet.receipts(repo, base, tip, [_edge(*ratchet.CUT)])
    assert found == {} and [p for p, _ in refused[ratchet.CUT]] == [ratchet.NOTE]


def test_a_newline_in_a_path_cannot_pose_as_a_receipt_path(fixture_repo):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    spoof = "notes/x\nY:research/fake.md"
    tip = ratchet.tree(repo, root, ratchet.spec(), ((spoof, ratchet.LINE + "\n"),))
    found, refused = ratchet.receipts(repo, base, tip, [_edge(*ratchet.CUT)])
    assert found == {} and [p for p, _ in refused[ratchet.CUT]] == [spoof]
    honest = "research/a\nb.md"
    tip = ratchet.tree(repo, root, ratchet.spec(), ((honest, ratchet.LINE + "\n"),))
    assert ratchet.receipts(repo, base, tip, ())[0] == {ratchet.CUT: honest}


def test_a_line_holding_a_nul_past_the_binary_check_keeps_its_row(fixture_repo):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    text = "x\n" * 5000 + "a\0b\n" + ratchet.LINE + "\n"
    tip = ratchet.tree(repo, root, ratchet.spec(), ((ratchet.NOTE, text),))
    assert ratchet.receipts(repo, base, tip, ())[0] == {ratchet.CUT: ratchet.NOTE}


def test_an_id_of_any_length_parses():
    line = ratchet.RECEIPT.match(ratchet.says("clm-abcdefgh", "sup-a"))
    assert line.group(1, 2) == ("clm-abcdefgh", "sup-a")


def test_records_split_only_on_a_newline(fixture_repo):
    repo, root = fixture_repo
    Path(root, ratchet.CLAIMS).parent.mkdir(parents=True)
    Path(root, ratchet.CLAIMS).write_text('{"a": "x\u2028y"}\n{"b": 1}\n', encoding="utf-8")
    repo.git("add", "-A")
    assert len(ratchet.records(repo, repo.git("write-tree").strip(), ratchet.CLAIMS)) == 2


def test_a_latin1_byte_beside_a_receipt_does_not_crash(fixture_repo):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    tip = ratchet.tree(repo, root, ratchet.spec(), ratchet.note(ratchet.LINE))
    Path(root, ratchet.NOTE).write_bytes(ratchet.LINE.encode() + b" caf\xe9\n")
    repo.git("add", "-A", "-f")
    assert ratchet.receipts(repo, base, repo.git("write-tree").strip(), ())[0] == {ratchet.CUT: ratchet.NOTE}


def test_a_whitespace_line_in_the_index_aborts(fixture_repo):
    repo, root = fixture_repo
    Path(root, ratchet.CLAIMS).parent.mkdir(parents=True)
    Path(root, ratchet.CLAIMS).write_text('{"a": 1}\n   \n', encoding="utf-8")
    repo.git("add", "-A")
    with pytest.raises(ratchet.GateError):
        ratchet.records(repo, repo.git("write-tree").strip(), ratchet.CLAIMS)


def test_a_failed_grep_is_not_an_empty_one(fixture_repo):
    repo, _ = fixture_repo
    with pytest.raises(ratchet.GateError):
        ratchet.token_lines(repo, "no-such-rev")


@pytest.mark.parametrize("name, cause", [
    ("receipt-numbered", "it does not read `dep-removed: clm-cite00 -> clm-weak00: <why>`"),
    ("receipt-backticked", "it does not read `dep-removed: clm-cite00 -> clm-weak00: <why>`"),
    ("receipt-upper-token", "it does not read `dep-removed: clm-cite00 -> clm-weak00: <why>`"),
    ("receipt-reversed", "it does not read `dep-removed: clm-cite00 -> clm-weak00: <why>`"),
    ("receipt-two-on-a-line", "it does not read `dep-removed: clm-xxxxxx -> clm-zzzzzz: <why>`, one edge to a line"),
    ("receipt-reason-past-cr", "it gives no reason"),
    ("receipt-wrong-root", "it is not under research/"),
    ("receipt-json", "it is not in a .md file"),
    ("receipt-archived", "it is in an _archive/ directory"),
    ("receipt-old-file", "the base has this file"),
    ("receipt-placeholder", "it gives no reason"),
    ("receipt-moved-in", "a base line holding dep-removed: already holds both ids and this reason"),
    ("receipt-was-json", "a base line holding dep-removed: already holds both ids and this reason"),
    ("receipt-fragment", "a base line holding dep-removed: already holds both ids and this reason"),
])
def test_a_refused_line_says_why(fixture_repo, capsys, name, cause):
    res = _case(fixture_repo, name)
    assert ratchet.report(res, "b" * 8, "t" * 8) == 1
    out = capsys.readouterr().out
    path = ratchet.CASES[name]["files"][0][0]
    assert "the line in %s does not count: %s" % (path, cause) in out


def test_a_slack_edge_owes_nothing_so_its_refused_line_prints_nothing(fixture_repo, capsys):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    tip = ratchet.tree(repo, root, ratchet.spec(deps=ratchet.without((ratchet.CITE, ratchet.SOLID))),
                       ratchet.note(ratchet.says(ratchet.CITE, ratchet.SOLID), "notes/n.md"))
    assert ratchet.report(ratchet.scan(repo, base, tip), base, tip) == 0
    assert "does not count" not in capsys.readouterr().out


def test_a_line_that_names_no_removed_edge_prints_nothing(fixture_repo, capsys):
    res = _case(fixture_repo, "receipt-other-edge")
    assert ratchet.report(res, "b" * 8, "t" * 8) == 1
    assert "does not count" not in capsys.readouterr().out


def test_a_token_line_holding_one_id_of_the_edge_names_nothing(fixture_repo, capsys):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    tip = ratchet.tree(repo, root, ratchet.CUTTING, ratchet.note("the %s token, on %s" % (ratchet.TOKEN, ratchet.CITE)))
    assert ratchet.report(ratchet.scan(repo, base, tip), base, tip) == 1
    assert "does not count" not in capsys.readouterr().out


def test_a_refused_line_beside_a_good_one_does_not_print(fixture_repo, capsys):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    tip = ratchet.tree(repo, root, ratchet.CUTTING, ratchet.note(ratchet.LINE) + ratchet.note(ratchet.LINE, "notes/n.md"))
    assert ratchet.report(ratchet.scan(repo, base, tip), base, tip) == 0
    assert "does not count" not in capsys.readouterr().out


def test_report_says_what_is_joint_what_left_and_what_is_not_gated(fixture_repo, capsys):
    res = _case(fixture_repo, "joint-only")
    assert ratchet.report(res, "b" * 8, "t" * 8) == 1
    out = capsys.readouterr().out
    first, second = ratchet.SUPS
    assert "with %s -> %s, holds %s at ok-to-build (0.9); restored together it reads do-not-build" % (
        *second, ratchet.LIFT) in out
    assert "with %s -> %s, holds %s at ok-to-build (0.9)" % (*first, ratchet.LIFT) in out
    assert ratchet.TOKEN + " <source> -> <target>: <why>" in out
    assert "listed=2  receipted=0  UNEXPLAINED=2" in out
    assert "The solver reads no prose" in out and "a new Markdown file" in out

    res = _case(fixture_repo, "joint-after-receipt")
    ratchet.report(res, "b" * 8, "t" * 8)
    assert "listed=3  receipted=1  UNEXPLAINED=2" in capsys.readouterr().out

    res = _case(fixture_repo, "joint-cycle")
    res["findings"][0]["edge"]["context"] = "the bullet"
    ratchet.report(res, "b" * 8, "t" * 8)
    out = capsys.readouterr().out
    assert "restoring it with %s -> %s closes a cycle, so they cannot go back together" % (ratchet.Z, ratchet.M) in out
    assert "break a tip edge on that\n    loop" in out
    assert "dropped: the bullet" in out

    res = _case(fixture_repo, "remint-no-citers")
    ratchet.report(res, "b" * 8, "t" * 8)
    out = capsys.readouterr().out
    assert "retired-claims=1" in out and "removed-edges=1" in out
    assert "holds %s (gone from the tip, read as if it stayed) at ok-to-build (0.95)" % ratchet.X in out
    assert "the edge cannot come back under that id" in out
    assert "gone from the tip: %s" % ratchet.X in out

    res = _case(fixture_repo, "rise-by-two-routes")
    ratchet.report(res, "b" * 8, "t" * 8)
    assert "not gated: %s  do-not-build -> input-only  (0.3 -> 0.6)" % ratchet.CITE in capsys.readouterr().out

    res = _case(fixture_repo, "reversed-edge")
    ratchet.report(res, "b" * 8, "t" * 8)
    out = capsys.readouterr().out
    assert "not tested: %s  do-not-build -> ok-to-build  (0.3 -> 0.85)" % ratchet.CITE in out
    assert "other-band-rises=2 (not tested)" in out and "not gated" not in out
    assert "left out of the restore: %s -> %s. What they hold or lift" % ratchet.CUT in out
    assert "restoring it closes a cycle, so its effect cannot be computed" in out


def test_main_exits_1_on_an_unexplained_cut(no_self_gate, fixture_repo, capsys):
    repo, base, tip, _ = _scan(fixture_repo, ratchet.spec(deps=ratchet.without(ratchet.CUT)))
    assert ratchet.main(base, tip, repo) == 1
    out = capsys.readouterr().out
    assert "%s -x-> %s  UNEXPLAINED" % ratchet.CUT in out
    assert "holds %s at ok-to-build (0.85); restored it reads do-not-build (0.3)" % ratchet.CITE in out


def test_main_exits_0_and_names_the_receipt(no_self_gate, fixture_repo, capsys):
    repo, base, tip, _ = _scan(fixture_repo, ratchet.CUTTING, ratchet.note(ratchet.LINE))
    assert ratchet.main(base, tip, repo) == 0
    assert "receipt: " + ratchet.NOTE in capsys.readouterr().out


def test_main_exits_2_on_an_unresolvable_rev(no_self_gate, fixture_repo):
    repo, root = fixture_repo
    assert ratchet.main("no-such-rev", ratchet.tree(repo, root, ratchet.spec()), repo) == 2


def test_main_exits_2_on_a_rev_with_no_index(no_self_gate, fixture_repo):
    repo, root = fixture_repo
    Path(root, "unrelated.txt").write_text("x\n", encoding="utf-8")
    repo.git("add", "unrelated.txt")
    empty = repo.git("write-tree").strip()
    assert ratchet.main(empty, empty, repo) == 2


def test_main_exits_2_on_a_stale_index(no_self_gate, fixture_repo, capsys):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    stale = ratchet.tree(repo, root, ratchet.spec(), stale=ratchet.WEAK)
    assert ratchet.main(base, stale, repo) == 2
    assert "either the index is stale" in capsys.readouterr().out


def test_main_exits_2_on_a_malformed_record(no_self_gate, fixture_repo):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    Path(root, ratchet.CLAIMS).write_text('{"node_type": "claim"}\n', encoding="utf-8")
    repo.git("add", "-A")
    assert ratchet.main(base, repo.git("write-tree").strip(), repo) == 2


def test_main_exits_2_when_the_self_gate_is_dead(fixture_repo, monkeypatch):
    repo, root = fixture_repo
    tree = ratchet.tree(repo, root, ratchet.spec())
    monkeypatch.setattr(ratchet, "run_gate", lambda out=None: ["planted"])
    assert ratchet.main(tree, tree, repo) == 2


def test_main_exits_2_when_the_self_gate_raises(fixture_repo, monkeypatch):
    repo, root = fixture_repo
    tree = ratchet.tree(repo, root, ratchet.spec())

    def boom(out=None):
        raise ratchet.GateError("git init exited 128")

    monkeypatch.setattr(ratchet, "run_gate", boom)
    assert ratchet.main(tree, tree, repo) == 2


def test_main_exits_2_when_git_is_missing(monkeypatch):
    monkeypatch.setenv("PATH", "/nonexistent")
    assert ratchet.main("HEAD", "HEAD") == 2


def test_main_exits_2_on_a_record_that_only_fails_after_load(no_self_gate, fixture_repo):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    Path(root, ratchet.CLAIMS).write_text(
        '{"node_type": "claim", "id": "clm-a", "confidence": "x", "solidity": "x"}\n', encoding="utf-8")
    Path(root, ratchet.EDGES).write_text("", encoding="utf-8")
    repo.git("add", "-A")
    assert ratchet.main(base, repo.git("write-tree").strip(), repo) == 2


def test_main_exits_2_on_any_other_crash(no_self_gate, fixture_repo, monkeypatch):
    repo, root = fixture_repo
    tree = ratchet.tree(repo, root, ratchet.spec())

    def boom(*args):
        raise KeyError("source")

    monkeypatch.setattr(ratchet, "scan", boom)
    assert ratchet.main(tree, tree, repo) == 2


def test_a_subdirectory_run_reads_the_same_receipts(no_self_gate, fixture_repo, monkeypatch, capsys):
    _, base, tip, _ = _scan(fixture_repo, ratchet.CUTTING, ratchet.note(ratchet.LINE))
    _, root = fixture_repo
    for name in [k for k in os.environ if k.startswith("GIT_")]:
        monkeypatch.delenv(name)
    monkeypatch.chdir(Path(root, "manuscript/ave-kb"))
    assert ratchet.main(base, tip) == 0
    assert "receipt: " + ratchet.NOTE in capsys.readouterr().out


def test_failed_import_is_exit_2_and_not_a_traceback(tmp_path):
    shutil.copy(_TOOL, tmp_path / _TOOL.name)
    (tmp_path / "kb_index_lib.py").write_text("raise TypeError('below python 3.11')\n", encoding="utf-8")
    result = subprocess.run([sys.executable, str(tmp_path / _TOOL.name), "--selftest"],
                            capture_output=True, text=True)
    assert result.returncode == 2
    assert "cannot use kb_index_lib" in result.stdout


def test_a_library_with_a_renamed_function_is_exit_2(tmp_path):
    shutil.copy(_TOOL, tmp_path / _TOOL.name)
    (tmp_path / "kb_index_lib.py").write_text("derive_band = None\n", encoding="utf-8")
    result = subprocess.run([sys.executable, str(tmp_path / _TOOL.name), "HEAD", "HEAD"],
                            capture_output=True, text=True)
    assert result.returncode == 2
    assert "cannot use kb_index_lib" in result.stdout


@pytest.mark.parametrize("mode", ["--selftest", "--mutation-receipt"])
def test_a_crash_in_either_check_mode_is_exit_2(mode):
    result = subprocess.run([sys.executable, str(_TOOL), mode], capture_output=True, text=True,
                            env={**os.environ, "PATH": "/nonexistent"})
    assert result.returncode == 2
    assert "ABORT: FileNotFoundError" in result.stdout


@pytest.mark.parametrize("revs", [["HEAD"], ["HEAD", "HEAD", "HEAD"]])
def test_cli_without_two_revs_is_a_usage_failure_and_not_a_pass(revs):
    result = subprocess.run([sys.executable, str(_TOOL), *revs], capture_output=True, text=True)
    assert result.returncode == 2
    assert "usage:" in result.stdout

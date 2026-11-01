"""Regression tests for manuscript/ave-kb/tools/verify-solidity-ratchet.py.

Asserts:
  * the tool's own can-it-fire + negative-control gate holds, driven through the
    real scan() against a throwaway git repo;
  * the mutation receipt holds: each listed rule, switched off, breaks its named
    fixtures, and a rule that breaks nothing fails the receipt;
  * the JSONL reconstruction agrees with the Markdown pipeline on the live KB. That is
    a property of the tree and pins no count, so it survives any KB edit. The live KB
    has no numeric support or run experiment, so the fixtures carry those branches;
  * the verdict numbers on the fixtures, computed here by hand from the min rule;
  * what the report says, and that the exit codes hold from a subdirectory;
  * main()'s exit codes: 1 on an unexplained cut, 0 on a receipted one, 2 on each
    failure the gate must not read as clean, a crash included.
"""

import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

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


def _scan(fixture_repo, tip_spec, tip_files=(), base_spec=None):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec() if base_spec is None else base_spec)
    tip = ratchet.tree(repo, root, tip_spec, tip_files)
    return repo, base, tip, ratchet.scan(repo, base, tip)


def _case(fixture_repo, name):
    c = ratchet.CASES[name]
    return _scan(fixture_repo, c["tip"], c["files"], c["base"])[-1]


def _flagged(res, field="holds"):
    return {ratchet.pair(f["edge"]): f[field] for f in res["findings"]}


def test_self_gate_holds():
    assert ratchet.run_gate(out=lambda line: None) == []


def test_mutation_receipt_holds_and_leaves_no_mutation_on():
    assert ratchet.mutation_receipt() == 0
    assert ratchet.MUTATE == set()


def test_every_mutation_names_fixtures_that_exist():
    named = {name for cases, _ in ratchet.MUTATIONS.values() for name in cases}
    assert named <= set(ratchet.CASES) | set(ratchet.ABORTS)


def test_a_rule_that_breaks_nothing_fails_the_receipt(monkeypatch):
    monkeypatch.setattr(ratchet, "MUTATIONS", {"not-a-rule": (("unchanged",), "does nothing")})
    assert ratchet.mutation_receipt() == 1


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


def test_two_routes_to_one_band_blame_both_routes(fixture_repo):
    res = _case(fixture_repo, "joint-two-routes")
    assert all(f["jointly"] == {ratchet.X: 0.30} for f in res["findings"])


def test_slack_edge_is_not_blamed_for_a_joint_effect(fixture_repo):
    res = _case(fixture_repo, "joint-plus-slack")
    assert (ratchet.CITE, ratchet.SOLID) not in _flagged(res)


def test_reversed_edge_fails_closed_as_uncomputable(fixture_repo):
    res = _case(fixture_repo, "reversed-edge")
    assert [f["cycle"] for f in res["findings"]] == [True]


def test_cycle_closed_only_by_two_edges_flags_those_two(fixture_repo):
    res = _case(fixture_repo, "joint-cycle-plus-slack")
    assert {ratchet.pair(f["edge"]) for f in res["findings"] if f["cycle"]} == {
        (ratchet.X, ratchet.Y), (ratchet.Z, ratchet.M)}
    assert len(res["gone"]) == 3


def test_raised_confidence_is_reported_but_not_gated(fixture_repo):
    res = _case(fixture_repo, "raised-confidence")
    assert res["findings"] == []
    assert ratchet.CITE in res["others"] and ratchet.DOWN in res["others"]


def test_a_claim_that_rose_both_ways_shows_both(fixture_repo):
    res = _case(fixture_repo, "rise-by-two-routes")
    # CITE reads 0.30 at the base and 0.85 at the tip. Restoring the edge gives 0.60:
    # the cut owns 0.60 -> 0.85, the raised confidence owns 0.30 -> 0.60.
    assert _flagged(res)[ratchet.CUT][ratchet.CITE] == 0.60
    assert res["others"] == [ratchet.CITE, ratchet.DOWN]
    assert res["after"][ratchet.CITE] == 0.60


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


def test_remint_of_a_support_counts_the_edge_and_prints_the_lift(fixture_repo):
    res = _case(fixture_repo, "remint-support")
    assert len(res["gone"]) == 1 and res["findings"] == []
    assert res["others"] == [ratchet.X]


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
    assert ratchet.receipts(repo, base, tip) == {ratchet.CUT: "research/a b.md"}


def test_a_line_behind_a_bare_cr_is_not_a_receipt(fixture_repo):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    tip = ratchet.tree(repo, root, ratchet.spec(), ((ratchet.NOTE, "old\r" + ratchet.LINE + "\n"),))
    assert ratchet.receipts(repo, base, tip) == {}


def test_report_says_what_is_joint_what_left_and_what_is_not_gated(fixture_repo, capsys):
    res = _case(fixture_repo, "joint-only")
    assert ratchet.report(res, "b" * 8, "t" * 8) == 1
    out = capsys.readouterr().out
    assert "with other removed edges, holds %s at ok-to-build (0.9); restored together" % ratchet.LIFT in out
    assert ratchet.TOKEN + " <source> -> <target>: <why>" in out
    assert "no alternative" in out

    res = _case(fixture_repo, "remint-no-citers")
    ratchet.report(res, "b" * 8, "t" * 8)
    out = capsys.readouterr().out
    assert "retired-claims=1" in out and "removed-edges=1" in out
    assert "holds %s (gone from the tip) at ok-to-build (0.95)" % ratchet.X in out
    assert "gone from the tip: %s" % ratchet.X in out

    res = _case(fixture_repo, "rise-by-two-routes")
    ratchet.report(res, "b" * 8, "t" * 8)
    assert "not gated: %s  do-not-build -> input-only  (0.3 -> 0.6)" % ratchet.CITE in capsys.readouterr().out


def test_main_exits_1_on_an_unexplained_cut(fixture_repo, capsys):
    repo, base, tip, _ = _scan(fixture_repo, ratchet.spec(deps=ratchet.without(ratchet.CUT)))
    assert ratchet.main(base, tip, repo) == 1
    out = capsys.readouterr().out
    assert "%s -x-> %s  UNEXPLAINED" % ratchet.CUT in out
    assert "holds %s at ok-to-build (0.85); restored it reads do-not-build (0.3)" % ratchet.CITE in out


def test_main_exits_0_and_names_the_receipt(fixture_repo, capsys):
    repo, base, tip, _ = _scan(fixture_repo, ratchet.CUTTING, ratchet.note(ratchet.LINE))
    assert ratchet.main(base, tip, repo) == 0
    assert "receipt: " + ratchet.NOTE in capsys.readouterr().out


def test_main_exits_2_on_an_unresolvable_rev(fixture_repo):
    repo, root = fixture_repo
    assert ratchet.main("no-such-rev", ratchet.tree(repo, root, ratchet.spec()), repo) == 2


def test_main_exits_2_on_a_rev_with_no_index(fixture_repo):
    repo, root = fixture_repo
    Path(root, "unrelated.txt").write_text("x\n", encoding="utf-8")
    repo.git("add", "unrelated.txt")
    empty = repo.git("write-tree").strip()
    assert ratchet.main(empty, empty, repo) == 2


def test_main_exits_2_on_a_stale_index(fixture_repo, capsys):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    stale = ratchet.tree(repo, root, ratchet.spec(), stale=ratchet.WEAK)
    assert ratchet.main(base, stale, repo) == 2
    assert "either the index is stale" in capsys.readouterr().out


def test_main_exits_2_on_a_malformed_record(fixture_repo):
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


def test_main_exits_2_on_a_record_that_only_fails_after_load(fixture_repo, monkeypatch):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    Path(root, ratchet.CLAIMS).write_text(
        '{"node_type": "claim", "id": "clm-a", "confidence": "x", "solidity": "x"}\n', encoding="utf-8")
    Path(root, ratchet.EDGES).write_text("", encoding="utf-8")
    repo.git("add", "-A")
    assert ratchet.main(base, repo.git("write-tree").strip(), repo) == 2


def test_main_exits_2_on_any_other_crash(fixture_repo, monkeypatch):
    repo, root = fixture_repo
    tree = ratchet.tree(repo, root, ratchet.spec())

    def boom(*args):
        raise KeyError("source")

    monkeypatch.setattr(ratchet, "scan", boom)
    assert ratchet.main(tree, tree, repo) == 2


def test_a_subdirectory_run_reads_the_same_receipts(fixture_repo, monkeypatch, capsys):
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
    assert "cannot import kb_index_lib" in result.stdout


def test_cli_without_revs_is_a_usage_failure_and_not_a_pass():
    result = subprocess.run([sys.executable, str(_TOOL), "HEAD"], capture_output=True, text=True)
    assert result.returncode == 2

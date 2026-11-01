"""Regression tests for manuscript/ave-kb/tools/verify-solidity-ratchet.py.

Asserts:
  * the tool's own can-it-fire + negative-control gate holds, driven through the
    real scan() against a throwaway git repo;
  * the mutation receipt holds: every rule, switched off, breaks its named fixture;
  * the JSONL reconstruction agrees with the Markdown pipeline on the live KB. That is
    a property of the tree and pins no count, so it survives any KB edit;
  * the verdict numbers on the fixtures, computed here by hand from the min rule;
  * added_lines() counts hunks, so a Markdown line beginning `++ ` is not a file header;
  * main()'s exit codes: 1 on an unexplained cut, 0 on a receipted one, 2 on each
    failure the gate must not read as clean.
"""

import importlib.util
import json
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


def _scan(fixture_repo, tip_spec, tip_files=()):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    tip = ratchet.tree(repo, root, tip_spec, tip_files)
    return repo, base, tip, ratchet.scan(repo, base, tip)


def test_self_gate_holds():
    assert ratchet.run_gate(out=lambda line: None) == []


def test_mutation_receipt_holds_and_leaves_no_mutation_on():
    assert ratchet.mutation_receipt() == 0
    assert ratchet.MUTATE == set()


def test_every_mutation_names_a_fixture_that_exists():
    assert {case for case, _ in ratchet.MUTATIONS.values()} <= set(ratchet.CASES)


def test_committed_index_reproduces_from_its_own_records():
    index = _REPO_ROOT / "manuscript/ave-kb/.index"
    read = lambda name: [json.loads(line) for line in (index / name).read_text(encoding="utf-8").split("\n") if line]
    graph = ratchet.Graph(read("claims.jsonl"), read("depends-on.jsonl"))
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
    pairs = ((ratchet.SUP1, ratchet.WEAK), (ratchet.SUP2, ratchet.WEAK))
    _, _, _, res = _scan(fixture_repo, ratchet.spec(deps=ratchet.without(*pairs)))
    # Either support alone keeps LIFT at 0.90; both restored read 0.30 x 1.0.
    assert res["tip"][ratchet.LIFT] == 0.90
    assert [f["holds"] for f in res["findings"]] == [{ratchet.LIFT: 0.30}, {ratchet.LIFT: 0.30}]


def test_reversed_edge_fails_closed_as_uncomputable(fixture_repo):
    deps = ratchet.without(ratchet.CUT) + [(ratchet.WEAK, ratchet.CITE)]
    _, _, _, res = _scan(fixture_repo, ratchet.spec(deps=deps))
    assert [f["holds"] for f in res["findings"]] == [None]


def test_raised_confidence_is_reported_but_not_gated(fixture_repo):
    claims = {**ratchet.spec()["claims"], ratchet.WEAK: 0.90}
    _, _, _, res = _scan(fixture_repo, ratchet.spec(claims=claims))
    assert res["findings"] == []
    assert ratchet.CITE in res["others"] and ratchet.DOWN in res["others"]


def test_added_lines_counts_hunks_instead_of_trusting_line_prefixes(fixture_repo):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec())
    files = (("research/a.md", "++ b/not-a-header\nkept\n"), ("research/b.md", "second\n"))
    tip = ratchet.tree(repo, root, ratchet.spec(), files)
    assert ratchet.added_lines(repo, base, tip) == [
        ("research/a.md", "++ b/not-a-header"), ("research/a.md", "kept"), ("research/b.md", "second")]


def test_added_lines_reads_a_replaced_line_without_counting_the_removal(fixture_repo):
    repo, root = fixture_repo
    base = ratchet.tree(repo, root, ratchet.spec(), (("research/a.md", "old\nsame\n"),))
    tip = ratchet.tree(repo, root, ratchet.spec(), (("research/a.md", "new\nsame\n"),))
    assert ratchet.added_lines(repo, base, tip) == [("research/a.md", "new")]


def test_main_exits_1_on_an_unexplained_cut(fixture_repo, capsys):
    repo, base, tip, _ = _scan(fixture_repo, ratchet.spec(deps=ratchet.without(ratchet.CUT)))
    assert ratchet.main(base, tip, repo) == 1
    out = capsys.readouterr().out
    assert "%s -x-> %s  UNEXPLAINED" % ratchet.CUT in out
    assert "holds %s at ok-to-build (0.85); restored it reads do-not-build (0.3)" % ratchet.CITE in out


def test_main_exits_0_and_names_the_receipt(fixture_repo, capsys):
    files = ((ratchet.NOTE, ratchet.BOTH_IDS + "\n"),)
    repo, base, tip, _ = _scan(fixture_repo, ratchet.spec(deps=ratchet.without(ratchet.CUT)), files)
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
    stale = ratchet.tree(repo, root, ratchet.spec(), tamper=True)
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


def test_cli_without_revs_is_a_usage_failure_and_not_a_pass():
    result = subprocess.run([sys.executable, str(_TOOL), "HEAD"], capture_output=True, text=True)
    assert result.returncode == 2

"""Tests for the R2 pin census + migration helper.

FIXTURES ARE SYNTHETIC. Every repo under test is built here from scratch, with
its own commits and therefore its own SHAs; nothing pins a live corpus line
number, claim id, filename or branch shape. A fixture that encoded live state
would go green on the day the corpus moved under it and prove nothing.

NEITHER DOES ANY TEST HERE ENCODE THIS LANE'S OWN SCOPE. An earlier revision
asserted that the marker appeared nowhere outside `_orchestration/` and
`manuscript/ave-kb/tools/` -- an allow-list of the directories this lane happened
to be piloting in. That assertion fails the first time R2's actual purpose
happens: a corpus-wide sweep, or an author hand-writing a legitimate pin in a KB
leaf. What it was reaching for -- "the token means one thing" -- is a property,
and the property tests below are what replaced it. The one-time "0 prior corpus
hits" measurement is a dated fact and lives in the docket, not in a test.
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

TOOLS = Path(__file__).resolve().parents[1]


def _load(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, TOOLS / filename)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


lib = _load("pin_census_lib", "pin_census_lib.py")
mig = _load("migrate_pin_markers", "migrate-pin-markers.py")


def _git(repo: Path, *args: str) -> str:
    proc = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    assert proc.returncode == 0, proc.stderr
    return proc.stdout.strip()


def _commit(repo: Path, message: str) -> str:
    _git(repo, "add", "-A")
    _git(repo, "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-q", "-m", message)
    return _git(repo, "rev-parse", "HEAD")


@pytest.fixture
def repo(tmp_path: Path) -> tuple[Path, str]:
    """A two-commit repo whose OLD state is reachable only through the SHA.

    OLD: `target.md` 30 lines, `renamed-away.md` 20 lines.
    NEW: `target.md` truncated to 10 lines, `renamed-away.md` gone.

    So at HEAD, line 5 of target.md exists, line 25 does not, line 99 never
    did, and renamed-away.md resolves nowhere.
    """
    root = tmp_path / "repo"
    root.mkdir()
    _git(root, "init", "-q")
    (root / "target.md").write_text("".join(f"old target line {i}\n" for i in range(1, 31)))
    (root / "renamed-away.md").write_text("".join(f"gone line {i}\n" for i in range(1, 21)))
    old = _commit(root, "old")
    (root / "target.md").write_text("".join(f"new target line {i}\n" for i in range(1, 11)))
    (root / "renamed-away.md").unlink()
    _commit(root, "new")
    return root, old[:8]


def _bare(row) -> str:
    """The cite WITHOUT its marker — a key that survives being marked.

    ★ `CensusRow.as_written` is not that key. At the R2 pin-marker landing
    `LineCite.as_written` began INCLUDING the marker, so an already-marked
    `` `renamed-away.md:15` `` reports as `renamed-away.md:15 pin:`<sha>``.
    These tests keyed on it and started raising KeyError the moment the two
    lanes were merged — a test-only break (the census computes
    `already_marked` from `marked_occurrences` and the migrator matches with
    `cite_occurrence_re`, neither of which reads `as_written`), but the fix
    belongs here rather than in a rewritten expectation: the identity of a
    cite is its path and line, before and after marking.
    """
    if row.start is None:
        return row.path
    if row.end is not None and row.end != row.start:
        return f"{row.path}:{row.start}-{row.end}"
    return f"{row.path}:{row.start}"


def _classify(root: Path):
    vml = lib.load_vml()
    file_index, _ = vml.build_kbleaf_target_index(root)
    md = list(vml.iter_markdown_files(root))
    return {_bare(r): r for r in lib.classify(root, vml, file_index, md)}


def _write(root: Path, rel: str, body: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# doc\n\n{body}\n")
    return path


def _write_doc(root: Path, rel: str, sha: str) -> Path:
    """One ledger-style row carrying a provenance SHA and three cites.

    This is the shape R2 is about: ONE row-level SHA, several cites, of which
    exactly one is genuinely historical. The prose phrase is deliberate -- see
    `test_prose_alone_cannot_make_a_pin`.
    """
    return _write(
        root, rel,
        f"| run at the time of `{sha}` | live `target.md:5` | pinned `renamed-away.md:15` "
        "| rotten `target.md:99` |",
    )


# --- classification ----------------------------------------------------------


def test_three_classes_on_one_row(repo):
    root, sha = repo
    _write_doc(root, "doc.md", sha)
    _commit(root, "doc")
    rows = _classify(root)
    assert rows["target.md:5"].klass == "LIVE"
    assert rows["renamed-away.md:15"].klass == "TRUE-PIN"
    assert rows["renamed-away.md:15"].resolving_shas == (sha,)
    assert rows["target.md:99"].klass == "DEAD"


def test_prose_alone_cannot_make_a_pin(repo):
    """BAD INPUT (D2): a cite that resolves at NEITHER end, with pin prose.

    `target.md:99` is out of range at HEAD (10 lines) AND at the SHA (30
    lines), and its row says *"run at the time of"* -- one of the historical-pin
    phrases. An earlier `elif resolving or prose` ladder called that TRUE-PIN
    and the migrator rewrote it, which converts undiscovered rot into a signed
    author declaration that the rot is deliberate.
    """
    root, sha = repo
    doc = _write_doc(root, "doc.md", sha)
    _commit(root, "doc")
    row = _classify(root)["target.md:99"]

    assert row.prose_marker is True, "fixture must actually carry pin prose"
    assert row.resolving_shas == (), "fixture must resolve at no SHA on its row"
    assert row.klass == "DEAD", "prose must not be sufficient"

    before = doc.read_text()
    assert mig.main(["--repo-root", str(root), "--allow-unverified", "--apply"]) == 0
    after = doc.read_text()
    assert "`target.md:99` " not in after.replace("| rotten `target.md:99` |", "")
    assert "target.md:99` pin:" not in after, "rot must never be marked"
    assert before.count("pin:`") == 0


def test_sha_resolution_alone_is_enough_without_any_prose(repo):
    """GOOD INPUT (D2, other direction): no pin prose at all, still a pin.

    The necessary-and-sufficient condition is resolution at a SHA on the row.
    Prose may corroborate; its absence must not veto.
    """
    root, sha = repo
    _write(root, "doc.md", f"| stamp `{sha}` | pinned `renamed-away.md:15` |")
    _commit(root, "doc")
    row = _classify(root)["renamed-away.md:15"]
    assert row.prose_marker is False
    assert row.klass == "TRUE-PIN"


# --- the marker's grammar (property, not scope) ------------------------------


@pytest.mark.parametrize(
    "text,hits",
    [
        ("per `x.md:42` pin:`c4a546dc` — quote", 1),          # canonical form
        ("pin:`" + "a" * 7 + "`", 1),                          # 7 hex, the floor
        ("pin:`" + "0" * 41 + "`", 0),                         # 41 hex, over the ceiling
        ("pin:`" + "0" * 40 + "`", 1),                         # 40 hex, the ceiling
        ("pin:`abcdef`", 0),                                   # 6 hex, too short
        ("pin:`ABCDEF1`", 0),                                  # uppercase is not the token
        ("pin:`nothex1`", 0),                                  # not hex
        ("pin:abcdef1", 0),                                    # backticks are part of it
        ("pin `abcdef1`", 0),                                  # so is the colon
        ("as shipped on `abcdef1`", 0),                        # a bare SHA is the HERITAGE rule
        ("spin:`abcdef1`", 1),                                 # documented: not left-anchored
    ],
)
def test_marker_grammar_both_directions(text, hits):
    assert lib.count_markers(text) == hits


def test_marker_binds_the_cite_on_its_left_and_no_other(repo):
    """CONVENTIONS' scope rule is the whole content of R2 — test it directly."""
    root, sha = repo
    _write(root, "doc.md",
           f"| stamp `{sha}` | `target.md:5` | `renamed-away.md:15` pin:`{sha}` |")
    _commit(root, "doc")
    rows = _classify(root)
    assert rows["renamed-away.md:15"].already_marked is True
    assert rows["target.md:5"].already_marked is False, "the marker must not bind leftward past a cite"


def test_a_hand_written_marker_is_honoured_wherever_it_lives(tmp_path):
    """The property the old scope allow-list was groping at.

    An author writes a pin marker by hand, in a KB leaf this lane has never
    touched. The census must see it as binding and the migrator must leave the
    file byte-identical — the token is not owned by the migration's scope.
    """
    root = tmp_path / "repo"
    root.mkdir()
    _git(root, "init", "-q")
    (root / "target.md").write_text("".join(f"old line {i}\n" for i in range(1, 31)))
    old = _commit(root, "old")[:8]
    (root / "target.md").write_text("".join(f"new line {i}\n" for i in range(1, 11)))
    _commit(root, "shrink")
    leaf = _write(root, "manuscript/ave-kb/vol1/leaf.md",
                  f"per `target.md:25` pin:`{old}` — *\"old line 25\"*, run `{old}`")
    _commit(root, "leaf")

    row = _classify(root)["target.md:25"]
    assert row.klass == "TRUE-PIN"
    assert row.already_marked is True

    before = leaf.read_text()
    assert mig.main(["--repo-root", str(root), "--allow-unverified", "--apply"]) == 0
    assert leaf.read_text() == before, "an author's own marker must not be re-marked"


# --- migration ---------------------------------------------------------------


def test_migrator_marks_only_true_pin_and_is_idempotent(repo):
    root, sha = repo
    doc = _write_doc(root, "doc.md", sha)
    _commit(root, "doc")

    code = mig.main(["--repo-root", str(root), "--allow-unverified", "--apply"])
    assert code == 0
    after_first = doc.read_text()
    assert f"`renamed-away.md:15` pin:`{sha}`" in after_first
    # LIVE and DEAD are untouched -- no marker anywhere near them.
    assert "`target.md:5` |" in after_first
    assert "`target.md:99` |" in after_first

    # IDEMPOTENCE: a second apply changes nothing, byte for byte. Unlike the
    # `@sha` spelling, the marked cite is STILL a cite, so this is a real
    # property of the rewriter rather than an artefact of leaving the grammar.
    assert mig.main(["--repo-root", str(root), "--allow-unverified", "--apply"]) == 0
    assert doc.read_text() == after_first
    still = _classify(root)["renamed-away.md:15"]
    assert still.klass == "TRUE-PIN" and still.already_marked is True


def test_all_three_cite_forms_are_marked_at_their_own_right_edge(repo):
    root, sha = repo
    doc = _write(
        root, "doc.md",
        f"| stamp `{sha}` | `renamed-away.md:15` | [a](renamed-away.md:15) "
        "| [b](renamed-away.md):15 |",
    )
    _commit(root, "doc")
    assert mig.main(["--repo-root", str(root), "--allow-unverified", "--apply"]) == 0
    out = doc.read_text()
    assert f"`renamed-away.md:15` pin:`{sha}`" in out
    assert f"[a](renamed-away.md:15) pin:`{sha}`" in out
    assert f"[b](renamed-away.md):15 pin:`{sha}`" in out
    assert mig.main(["--repo-root", str(root), "--allow-unverified", "--apply"]) == 0
    assert doc.read_text() == out


def test_a_double_dash_range_is_matched_and_marked(repo):
    """`LineCite.as_written` normalises `:1--2` to `:1-2`; the rewriter must not.

    A migrator that searched for the normalised string would silently skip every
    double-dash range in the corpus and report success.
    """
    root, sha = repo
    doc = _write(root, "doc.md", f"| stamp `{sha}` | `renamed-away.md:14--15` |")
    _commit(root, "doc")
    assert mig.main(["--repo-root", str(root), "--allow-unverified", "--apply"]) == 0
    assert f"`renamed-away.md:14--15` pin:`{sha}`" in doc.read_text()


def test_dry_run_is_the_default_and_writes_nothing(repo):
    root, sha = repo
    doc = _write_doc(root, "doc.md", sha)
    _commit(root, "doc")
    before = doc.read_text()
    assert mig.main(["--repo-root", str(root), "--allow-unverified"]) == 0
    assert doc.read_text() == before


# --- both directions on the frozen-file refusal -----------------------------


def test_frozen_refusal_FIRES_on_a_frozen_prereg(repo, capsys):
    """BAD INPUT: the same TRUE-PIN inside a *prereg-FROZEN* doc."""
    root, sha = repo
    doc = _write_doc(root, "research/2020-01-01_lane_prereg-FROZEN.md", sha)
    _commit(root, "doc")
    before = doc.read_text()
    code = mig.main(["--repo-root", str(root), "--allow-unverified", "--apply"])
    assert code == 2, "refusal must be visible in the exit code, not just in stdout"
    assert doc.read_text() == before, "a frozen doc must come out byte-identical"
    assert "REFUSED" in capsys.readouterr().out


def test_frozen_refusal_PASSES_on_an_ordinary_doc(repo, capsys):
    """GOOD INPUT: byte-identical content at a path the guard does not own."""
    root, sha = repo
    doc = _write_doc(root, "notes/2020-01-01_lane_notes.md", sha)
    _commit(root, "doc")
    code = mig.main(["--repo-root", str(root), "--allow-unverified", "--apply"])
    assert code == 0
    assert f"`renamed-away.md:15` pin:`{sha}`" in doc.read_text()
    assert "REFUSED" not in capsys.readouterr().out


@pytest.mark.parametrize(
    "rel,refused",
    [
        ("research/x_prereg-FROZEN.md", True),
        ("research/x_prereg.md", True),
        ("research/x_result.md", True),
        ("research/x-RESULT.md", True),
        ("research/x_derivation.md", False),
        ("_orchestration/x.md", False),
        ("manuscript/ave-kb/x.md", False),
    ],
)
def test_frozen_guard_predicate_both_directions(rel, refused):
    assert (mig.frozen_guarded(rel) is not None) is refused


# --- both directions on the allow-list --------------------------------------


def test_allowlist_excludes_a_true_pin_it_does_not_name(repo, tmp_path):
    root, sha = repo
    doc = _write_doc(root, "doc.md", sha)
    _commit(root, "doc")
    empty = tmp_path / "allow.tsv"
    empty.write_text("# nothing verified yet\n")
    before = doc.read_text()
    assert mig.main(["--repo-root", str(root), "--verified", str(empty), "--apply"]) == 0
    assert doc.read_text() == before


def test_allowlist_includes_the_true_pin_it_does_name(repo, tmp_path):
    root, sha = repo
    doc = _write_doc(root, "doc.md", sha)
    _commit(root, "doc")
    allow = tmp_path / "allow.tsv"
    allow.write_text("doc.md\t3\trenamed-away.md:15\n")
    assert mig.main(["--repo-root", str(root), "--verified", str(allow), "--apply"]) == 0
    assert f"`renamed-away.md:15` pin:`{sha}`" in doc.read_text()


def test_migrator_refuses_to_run_with_no_verification_posture(repo):
    root, _ = repo
    with pytest.raises(SystemExit):
        mig.main(["--repo-root", str(root)])


# --- the rewrite primitive ---------------------------------------------------


class _Row:
    """Minimal stand-in for a CensusRow — the rewriter reads four fields."""

    def __init__(self, form, path, start, end):
        self.form, self.path, self.start, self.end = form, path, start, end


def test_rewrite_line_does_not_swallow_a_longer_line_number():
    line = "`a.md:8` and `a.md:80`"
    out, n = mig.rewrite_line(line, _Row("backticked", "a.md", 8, 8), "deadbee", lib)
    assert n == 1 and out == "`a.md:8` pin:`deadbee` and `a.md:80`"


def test_rewrite_line_is_a_no_op_on_an_already_marked_cite():
    line = "`a.md:8` pin:`deadbee`"
    out, n = mig.rewrite_line(line, _Row("backticked", "a.md", 8, 8), "deadbee", lib)
    assert n == 0 and out == line


def test_rewrite_line_marks_a_second_bare_occurrence_but_not_the_marked_one():
    line = "`a.md:8` pin:`deadbee` then `a.md:8` again"
    out, n = mig.rewrite_line(line, _Row("backticked", "a.md", 8, 8), "deadbee", lib)
    assert n == 1
    assert out == "`a.md:8` pin:`deadbee` then `a.md:8` pin:`deadbee` again"

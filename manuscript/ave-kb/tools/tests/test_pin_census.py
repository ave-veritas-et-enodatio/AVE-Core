"""Tests for the R2 pin census + migration helper.

FIXTURES ARE SYNTHETIC. Every repo under test is built here from scratch, with
its own commits and therefore its own SHAs; nothing pins a live corpus line
number, claim id, filename or branch shape. A fixture that encoded live state
would go green on the day the corpus moved under it and prove nothing.
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


def _classify(root: Path):
    vml = lib.load_vml()
    file_index, _ = vml.build_kbleaf_target_index(root)
    md = list(vml.iter_markdown_files(root))
    return {r.as_written: r for r in lib.classify(root, vml, file_index, md)}


def _write_doc(root: Path, rel: str, sha: str) -> Path:
    """One ledger-style row carrying a provenance SHA and three cites.

    This is the shape R2 is about: ONE row-level SHA, several cites, of which
    exactly one is genuinely historical.
    """
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "# doc\n\n"
        f"| run at `{sha}` | live `target.md:5` | pinned `renamed-away.md:15` "
        "| rotten `target.md:99` |\n"
    )
    return path


def test_three_classes_on_one_row(repo):
    root, sha = repo
    _write_doc(root, "doc.md", sha)
    _commit(root, "doc")
    rows = _classify(root)
    assert rows["target.md:5"].klass == "LIVE"
    assert rows["renamed-away.md:15"].klass == "TRUE-PIN"
    assert rows["renamed-away.md:15"].resolving_shas == (sha,)
    assert rows["target.md:99"].klass == "DEAD"


def test_migrator_marks_only_true_pin_and_is_idempotent(repo):
    root, sha = repo
    doc = _write_doc(root, "doc.md", sha)
    _commit(root, "doc")

    code = mig.main(["--repo-root", str(root), "--allow-unverified", "--apply"])
    assert code == 0
    after_first = doc.read_text()
    assert f"renamed-away.md:15@{sha}" in after_first
    # LIVE and DEAD are untouched -- no marker anywhere near them.
    assert "`target.md:5`" in after_first
    assert "`target.md:99`" in after_first
    assert "target.md:5@" not in after_first
    assert "target.md:99@" not in after_first

    # IDEMPOTENCE: a second apply changes nothing, byte for byte.
    assert mig.main(["--repo-root", str(root), "--allow-unverified", "--apply"]) == 0
    assert doc.read_text() == after_first
    # ... and the marked cite is no longer classified at all (the marker moved
    # it out of the bare-cite grammar), so there is nothing left to re-mark.
    assert "renamed-away.md:15" not in _classify(root)


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
    assert f"renamed-away.md:15@{sha}" in doc.read_text()
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
    assert f"renamed-away.md:15@{sha}" in doc.read_text()


def test_migrator_refuses_to_run_with_no_verification_posture(repo):
    root, _ = repo
    with pytest.raises(SystemExit):
        mig.main(["--repo-root", str(root)])


# --- the rewrite primitive ---------------------------------------------------


def test_rewrite_line_does_not_swallow_a_longer_line_number():
    line = "`a.md:8` and `a.md:80`"
    out, n = mig.rewrite_line(line, "a.md:8", "deadbee")
    assert n == 1 and out == "`a.md:8@deadbee` and `a.md:80`"


def test_rewrite_line_is_a_no_op_on_an_already_marked_cite():
    line = "`a.md:8@deadbee`"
    out, n = mig.rewrite_line(line, "a.md:8", "deadbee")
    assert n == 0 and out == line


def test_marker_is_not_yet_a_homonym_in_this_repo():
    """The coinage must not collide with anything already written.

    Run against the REAL repo on purpose: a coinage check is a claim about the
    live corpus and cannot be made against a synthetic fixture. It is a
    one-directional assertion (the token is absent), so it cannot go stale
    silently -- the first real marker landing outside the census's own
    migration would fail it loudly, which is the intent.
    """
    repo_root = TOOLS.parents[2]
    if not (repo_root / ".git").exists():
        pytest.skip("not a git checkout")
    # Range-aware on purpose: `:[0-9]+@...` misses `foo.md:50-57@sha`.
    out = subprocess.run(
        ["git", "-C", str(repo_root), "grep", "-lIE", r":[0-9]+(-{1,2}[0-9]+)?@[0-9a-f]{7}", "--",
         "*.md"],
        capture_output=True, text=True,
    ).stdout.split()
    stray = [
        f for f in out
        if not f.startswith(("_orchestration/", "manuscript/ave-kb/tools/"))
    ]
    assert not stray, f"@sha marker appeared outside the migrated scope: {stray}"

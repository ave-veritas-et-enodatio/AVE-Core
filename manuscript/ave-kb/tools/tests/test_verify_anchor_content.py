"""Regression test for manuscript/ave-kb/tools/verify-anchor-content.py CITE_RE.

Guards the 2026-08-03 fix: before it, CITE_RE required the `:NN` to follow the
file extension IMMEDIATELY, so the markdown-link anchor form used throughout the
KB — `[text](path.md):NN` — was INVISIBLE to the drift checker (the `)` broke the
match). A whole cite class went unscanned; three stale KB-leaf anchors shipped in
the #832 arc under a measured "advisory delta 0" because the tool never saw them.

Asserts, on one throwaway tree:
  * a STALE BARE-form anchor is caught          (pre-existing behaviour, unbroken)
  * a STALE LINK-form anchor is caught          (the regression this test exists for)
  * a CORRECT anchor in either form is NOT flagged
  * a prose parenthetical `(... path.md):NN` — no `](` opener — is NOT matched,
    i.e. the fix does not swallow unrelated `):` sequences
  * exit-code semantics are unchanged (the scan path always returns 0)

The tree is built in a tmpdir rather than under tests/fixtures/. That was
originally forced — verify-anchor-content's crawl did NOT prune `tests/fixtures`
(unlike its sibling verify-md-links), so on-disk stale-anchor fixtures would
have been scanned as corpus. The 2026-08-05 cite-rot change added
SKIP_SEGMENT_RUNS to this tool, so the constraint is lifted; the tmpdir form is
retained because these cases also need a THROWAWAY GIT REPO for the --new-cites
ratchet below.

Also covers the NEW-cite excerpt ratchet (cite-rot option 3): every line-cite a
branch ADDS to the canonical-authority surface must carry an adjacent verbatim
excerpt, so the ~13k-cite backlog stops growing.

Run directly (`python tools/tests/test_verify_anchor_content.py`) or via pytest.
"""

import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path

_TOOL = Path(__file__).resolve().parent.parent / "verify-anchor-content.py"

_ANCHOR = "the quick brown fox anchor phrase"
_DRIFTED = "a drifted excerpt that moved down here"


def _load_module():
    spec = importlib.util.spec_from_file_location("verify_anchor_content", _TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    # Register before exec so dataclasses resolve string annotations (PEP 563)
    # against the module's own namespace.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _build_tree(root: Path) -> Path:
    """Target file with known content at :10 and :30, plus the citing file."""
    (root / "Makefile").write_text("# sentinel\n")
    (root / "manuscript").mkdir()
    target_lines = ["\n"] * 40
    target_lines[9] = _ANCHOR + "\n"  # line 10
    target_lines[29] = _DRIFTED + "\n"  # line 30
    (root / "target.md").write_text("".join(target_lines))

    citing = root / "research"
    citing.mkdir()
    cite_md = citing / "cites.md"
    cite_md.write_text(
        "\n".join(
            [
                # 1. BARE form, STALE: :10 cited, excerpt actually at :30.
                f"BARE-STALE: per `target.md:10` the `{_DRIFTED}` note.",
                # 2. LINK form, STALE: the form the pre-fix regex could not see.
                f"LINK-STALE: per [target](target.md):10 the `{_DRIFTED}` note.",
                # 3. BARE form, CORRECT.
                f"BARE-OK: see `target.md:10` for `{_ANCHOR}` here.",
                # 4. LINK form, CORRECT.
                f"LINK-OK: see [target](target.md):10 for `{_ANCHOR}` here.",
                # 5. NEGATIVE CONTROL: a prose parenthetical, no `](` opener.
                #    Must not be read as a cite at all.
                f"PAREN-NOT-A-LINK: (as noted in target.md):10 with `{_DRIFTED}`.",
            ]
        )
        + "\n"
    )
    return cite_md


def test_link_form_and_bare_form_stale_anchors_are_both_caught() -> None:
    vac = _load_module()
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        cite_md = _build_tree(root)
        counts, findings = vac.scan([cite_md], root)

        # The prose parenthetical must NOT be counted as a cite: 4 cites, not 5.
        assert counts.cites == 4, f"expected 4 cites (paren form excluded), got {counts.cites}"
        # Two correct anchors resolve; two stale ones are flagged as moved.
        assert counts.checked_ok == 2, counts
        assert counts.drift_moved == 2, counts
        assert counts.drift_absent == 0, counts
        assert counts.unresolved == 0, counts

        moved = sorted(findings, key=lambda f: f.citing_line)
        assert [f.citing_line for f in moved] == [1, 2], [f.citing_line for f in moved]
        for f in moved:
            assert f.target == "target.md", f.target
            assert f.target_line == 10
            assert f.found_at == [30], f.found_at
        # Line 1 is the bare form; line 2 is the markdown-link form. Before the
        # fix, only line 1 appeared here.
        assert len([f for f in moved if f.citing_line == 2]) == 1


def test_cite_re_branches_and_cite_path_helper() -> None:
    vac = _load_module()

    line = "see [text](common/foo.md):159 here"
    link = vac.CITE_RE.search(line)
    assert link is not None
    assert link.group("lpath") == "common/foo.md"
    assert link.group("path") is None
    assert vac.cite_path(link) == "common/foo.md"
    assert link.group("line") == "159"
    # The `](` opener is asserted by lookbehind, NOT consumed, so the match still
    # starts at the path. associate_quote ranks quote-proximity against this
    # column, so both branches must agree on it.
    assert link.start() == line.index("common/foo.md"), link.start()

    bare = vac.CITE_RE.search("see `common/foo.md:159` here")
    assert bare is not None
    assert bare.group("path") == "common/foo.md"
    assert bare.group("lpath") is None
    assert vac.cite_path(bare) == "common/foo.md"

    # Line number inside the link target keeps working (bare branch).
    inner = vac.CITE_RE.search("see [text](common/foo.md:159) here")
    assert inner is not None and vac.cite_path(inner) == "common/foo.md"
    assert inner.group("line") == "159"

    # No `](` opener -> not a cite.
    assert vac.CITE_RE.search("(as noted in common/foo.md):159") is None


def test_scan_path_exit_code_is_still_zero() -> None:
    vac = _load_module()
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _build_tree(root)
        # WARN-CLASS contract: findings are reported, never gated.
        assert vac.main(["--root", str(root), "--top", "5"]) == 0


# --- NEW-cite excerpt ratchet (cite-rot option 3) ---------------------------


def _git(root: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=root, capture_output=True, text=True, check=True,
        env={"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t", "GIT_COMMITTER_NAME": "t",
             "GIT_COMMITTER_EMAIL": "t@t", "PATH": "/usr/bin:/bin:/usr/local/bin"},
    )
    return proc.stdout


def _ratchet_repo(root: Path) -> None:
    """A throwaway repo with a `base` commit and one branch commit on top."""
    (root / "Makefile").write_text("# sentinel\n")
    kb = root / "manuscript" / "ave-kb" / "common"
    kb.mkdir(parents=True)
    (root / "research").mkdir()
    target = ["filler"] * 40
    target[9] = _ANCHOR
    (kb / "target.md").write_text("\n".join(target) + "\n")
    (kb / "leaf.md").write_text("# Leaf\n\npre-existing bare cite: `target.md:10`\n")
    _git(root, "init", "-q", "-b", "main")
    _git(root, "add", "-A")
    _git(root, "commit", "-q", "-m", "base")
    _git(root, "branch", "base")


def test_new_cite_ratchet_flags_only_added_unexcerpted_kb_cites() -> None:
    vac = _load_module()
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _ratchet_repo(root)
        kb = root / "manuscript" / "ave-kb" / "common"

        # The branch adds: one KB cite WITH an excerpt (ok), one KB cite with
        # NO excerpt (violation), and one research/ cite with no excerpt
        # (out of scope — research/ is not the canonical-authority surface).
        (kb / "leaf.md").write_text(
            "# Leaf\n\n"
            "pre-existing bare cite: `target.md:10`\n"
            f"added WITH excerpt: `target.md:10` — `{_ANCHOR}`\n"
            "added WITHOUT excerpt: `target.md:10`\n"
        )
        (root / "research" / "note.md").write_text("warn-class cite: `target.md:10`\n")
        _git(root, "add", "-A")
        _git(root, "commit", "-q", "-m", "branch work")

        violations = vac.check_new_cites("base", root)
        assert len(violations) == 1, violations
        rel, lineno, cited = violations[0]
        assert str(rel) == "manuscript/ave-kb/common/leaf.md", rel
        assert lineno == 5 and cited == "target.md:10", violations
        # Gating: the CLI path exits nonzero on a violation.
        assert vac.main(["--root", str(root), "--new-cites", "base"]) == 1


def test_new_cite_ratchet_passes_when_every_added_cite_is_excerpted() -> None:
    vac = _load_module()
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _ratchet_repo(root)
        kb = root / "manuscript" / "ave-kb" / "common"
        (kb / "leaf.md").write_text(
            "# Leaf\n\n"
            "pre-existing bare cite: `target.md:10`\n"
            f"added, excerpt on the line above:\n`{_ANCHOR}`\n`target.md:10`\n"
        )
        _git(root, "add", "-A")
        _git(root, "commit", "-q", "-m", "branch work")

        assert vac.check_new_cites("base", root) == []
        assert vac.main(["--root", str(root), "--new-cites", "base"]) == 0


def test_new_cite_ratchet_scope_predicate() -> None:
    vac = _load_module()
    for load_bearing in ("manuscript/ave-kb/common/leaf.md", "README.md", "AGENTS.md"):
        assert vac.is_load_bearing_source(Path(load_bearing)), load_bearing
    for out_of_scope in (
        "research/note.md",  # warn-class lane, never blocked
        "_orchestration/board.md",
        "manuscript/ave-kb/session/scratch.md",  # session subtree
        "manuscript/ave-kb/_archive/old.md",  # frozen archive
        "manuscript/ave-kb/tools/tests/fixtures/linecheck/manuscript/ave-kb/x.md",
        "docs/README.md",  # non-root README
    ):
        assert not vac.is_load_bearing_source(Path(out_of_scope)), out_of_scope


def test_emphasis_quote_excerpts_satisfy_the_ratchet() -> None:
    """The corpus's OTHER excerpt house style — *"…"* — must satisfy the gate.

    Back-tested when this was added: 6 of 21 blocked cites over the last-25-merge
    window (29%) carried a real excerpt written this way and were flagged anyway.
    A gate that rejects a convention the corpus actually uses trains lanes to
    work around it.
    """
    vac = _load_module()
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _ratchet_repo(root)
        kb = root / "manuscript" / "ave-kb" / "common"
        (kb / "leaf.md").write_text(
            "# Leaf\n\n"
            "pre-existing bare cite: `target.md:10`\n"
            f'added, italic-quote excerpt: `target.md:10` (*"{_ANCHOR}"*)\n'
            f'added, bold-quote excerpt: `target.md:10` (**"{_ANCHOR}"**)\n'
            f'added, underscore-quote excerpt: `target.md:10` (_"{_ANCHOR}"_)\n'
        )
        _git(root, "add", "-A")
        _git(root, "commit", "-q", "-m", "branch work")

        assert vac.check_new_cites("base", root) == []
        assert vac.main(["--root", str(root), "--new-cites", "base"]) == 0


def test_emphasis_quote_excerpt_across_a_hard_line_wrap_is_seen() -> None:
    """A prose excerpt that straddles a hard wrap still anchors its cite.

    The KB hard-wraps prose, so the opening `*"` and the closing `"*` routinely
    land on different lines and a per-line regex sees neither half. Both halves
    of the wrap are asserted: cite on the CLOSING line, and cite on the OPENING
    line. The verbatim corpus instances are `transfer-cost-theorem.md:86` and
    `:117` as they stood at PR #878's head `1e74b38d`.
    """
    vac = _load_module()
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _ratchet_repo(root)
        kb = root / "manuscript" / "ave-kb" / "common"
        head, tail = _ANCHOR[:18], _ANCHOR[18:]
        (kb / "leaf.md").write_text(
            "# Leaf\n\n"
            "pre-existing bare cite: `target.md:10`\n"
            f'wrap, cite on the closing line — *"{head}\n'
            f'{tail}"* (`target.md:10`)\n'
            f'wrap, cite on the opening line — `target.md:10` *"{head}\n'
            f'{tail}"*\n'
        )
        _git(root, "add", "-A")
        _git(root, "commit", "-q", "-m", "branch work")

        assert vac.check_new_cites("base", root) == []
        assert vac.main(["--root", str(root), "--new-cites", "base"]) == 0


def test_quote_recognizer_does_not_swallow_non_excerpts() -> None:
    """Widening the recognizer must not turn decoration into an anchor.

    A quoted path-cite is a cite, not content; and a quoted fragment under
    MIN_QUOTE_LEN stays trivial. Each must still leave the cite unanchored, or
    the ratchet degrades into a checklist. Both hold for ALL THREE recognized
    forms, because `is_checkable_quote` filters the span body after the match
    and is form-blind.

    ★SUPERSEDED ARM, recorded rather than dropped (ruling R27, 2026-08-07). This
    test used to carry a third arm asserting that a bullet marker followed by a
    space and a quote — `* "a bulleted quoted sentence"` — is ordinary prose and
    must NOT anchor a cite. R27 admits the BARE `"…"` form, and there is no way
    to admit it while excluding the instances that happen to follow a bullet:
    the two are the same span. Carving `* "` out would re-open the exact escape
    route R27 closes (write the excerpt after a bullet and no gate sees it). The
    arm is therefore retired ON PURPOSE, and the fact that decided it is asserted
    below instead — the bulleted sentence is NOT an emphasis span and IS a bare
    span, which is precisely why its status changed.
    """
    vac = _load_module()
    assert vac.EMPHASIS_QUOTE_RE.search('* "a bulleted quoted sentence"') is None
    assert vac.BARE_QUOTE_RE.search('* "a bulleted quoted sentence"') is not None
    assert vac.EMPHASIS_QUOTE_RE.search('the word *"cage"* here') is not None
    assert not vac.is_checkable_quote("abc")  # under MIN_QUOTE_LEN
    assert not vac.is_checkable_quote("some/path/leaf.md:42")  # a cite, not content

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _ratchet_repo(root)
        kb = root / "manuscript" / "ave-kb" / "common"
        (kb / "leaf.md").write_text(
            "# Leaf\n\n"
            "pre-existing bare cite: `target.md:10`\n"
            'quoted PATH is not content: "some/path/leaf.md:42" then `target.md:10`\n'
            'quote under MIN_QUOTE_LEN: "abc" then `target.md:10`\n'
        )
        _git(root, "add", "-A")
        _git(root, "commit", "-q", "-m", "branch work")

        violations = vac.check_new_cites("base", root)
        # Line 4 carries TWO cites (the quoted path is itself a cite) and line 5
        # one; none of the three finds a checkable span in any form.
        assert [(v[1], v[2]) for v in violations] == [
            (4, "some/path/leaf.md:42"),
            (4, "target.md:10"),
            (5, "target.md:10"),
        ], violations


def test_bare_double_quote_excerpts_satisfy_the_ratchet() -> None:
    """The THIRD excerpt form — plain `"…"` — must satisfy the gate (R27).

    Before this, a bare-quoted excerpt was invisible to BOTH consumers: the
    ratchet blocked the cite as excerpt-less, and — the reason it matters — the
    advisory drift check never compared that excerpt to its target, so a
    misquote written in bare quotes was unreachable by any gate in the repo.
    That was the escape route around the #915 primer-misquote blocker.

    Measured on the corpus at the landing commit: the gate's blocked set falls
    169 -> 127 over the origin/main~120 window and 572 -> 357 over ~400, with
    ZERO cites added to either blocked set.
    """
    vac = _load_module()
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _ratchet_repo(root)
        kb = root / "manuscript" / "ave-kb" / "common"
        (kb / "leaf.md").write_text(
            "# Leaf\n\n"
            "pre-existing bare cite: `target.md:10`\n"
            f'added, straight-quote excerpt: `target.md:10` ("{_ANCHOR}")\n'
            f'added, excerpt on the line above:\n"{_ANCHOR}"\n`target.md:10`\n'
            f'added, curly-quote excerpt: `target.md:10` (“{_ANCHOR}”)\n'
        )
        _git(root, "add", "-A")
        _git(root, "commit", "-q", "-m", "branch work")

        assert vac.check_new_cites("base", root) == []
        assert vac.main(["--root", str(root), "--new-cites", "base"]) == 0


def test_bare_quotes_are_a_last_resort_and_never_displace_a_house_style_span() -> None:
    """The ordering that makes the widening purely additive — asserted, not assumed.

    A bare `"…"` sitting CLOSER to the cite than a back-ticked excerpt must not
    win: the first association pass admits only the house styles, so it returns
    before the bare form is ever considered. Both controls execute:
      * FORCED-OFF arm — the same line run through `_associate(..., bare=True)`,
        i.e. the peer ordering, DOES select the bare span. That is what proves
        the two-pass structure (and not the fixture) is doing the work.
      * a bare span with NO house-style competitor is still selected, so the
        last-resort pass is reachable rather than dead code.
    """
    vac = _load_module()
    line = f'`{_ANCHOR}` cited at `target.md:10` right after "a nearer bare quote here"'
    lines = [line]
    col = line.index("target.md:10")

    assert vac.associate_quote(lines, 0, col) == _ANCHOR
    # FORCED-OFF: peer ordering selects the nearer bare span instead.
    assert vac._associate(lines, 0, col, bare=True) == "a nearer bare quote here"
    # Reachability: with no house-style span present, the bare form is used.
    solo = ['cited at `target.md:10` with only "a bare quoted excerpt here"']
    assert vac.associate_quote(solo, 0, solo[0].index("target.md:10")) == (
        "a bare quoted excerpt here"
    )


def test_fixture_trees_are_pruned_from_the_advisory_crawl() -> None:
    """tests/fixtures holds deliberately broken cites — never scanned as corpus."""
    vac = _load_module()
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "Makefile").write_text("# sentinel\n")
        (root / "manuscript").mkdir()
        kb = root / "manuscript" / "ave-kb"
        (kb / "tools" / "tests" / "fixtures" / "x").mkdir(parents=True)
        (kb / "tools" / "tests" / "fixtures" / "x" / "broken.md").write_text("`gone.md:9`\n")
        (kb / "live.md").write_text("`gone.md:9`\n")
        crawled = {p.name for p in vac.iter_citing_files(root)}
        assert "live.md" in crawled
        assert "broken.md" not in crawled


def test_freeze_stamp_exemption_is_exact():
    """A Rule-12 freeze stamp is not authorship — but only when it is ALL that changed.

    Driven with synthetic DIFF TEXT rather than a worktree edit, because that
    is the only way to exercise this code path at all: `added_lines_by_file`
    diffs `<base>...HEAD`, the COMMITTED tree, so an uncommitted edit is never
    in the diff. The first attempt to verify this exemption did exactly that and
    got the same answer for a stamp-only change and for a real content change —
    a probe that never ran, reported as a result.

    The three cases that matter, and the middle one is the can-it-still-fire arm
    without which this exemption would be a silent hole in the ratchet.
    """
    mod = _load_module()
    stamp = ("  <!-- rule12-freeze: base=" + "a" * 40 + " region=above offset=0 "
             "lines=3 bytes=99 sha256=" + "b" * 64 + " -->")
    body = "See [`x.md`](../x.md):73 for the wall."

    def diff(minus: str, plus: str) -> str:
        return (
            "diff --git a/doc.md b/doc.md\n"
            "--- a/doc.md\n"
            "+++ b/doc.md\n"
            "@@ -97 +97 @@\n"
            f"-{minus}\n"
            f"+{plus}\n"
        )

    # (1) STAMP ONLY -> not authorship, line is NOT counted.
    assert mod._added_from_diff_text(diff(body, body + stamp)) == {}, (
        "a line whose only change is an appended freeze stamp was counted as added"
    )

    # (2) STAMP *AND* REAL CONTENT -> still counted. The arm that keeps the
    #     exemption from becoming a hole: a new cite smuggled onto a stamped line.
    grew = body + " also [`y.md`](../y.md):12" + stamp
    assert mod._added_from_diff_text(diff(body, grew)) == {Path("doc.md"): {97}}, (
        "a NEW cite added to a line that also got stamped slipped through the "
        "freeze-stamp exemption -- the ratchet has a hole"
    )

    # (3) A PLAIN added line with no stamp anywhere -> counted, as always.
    plain = (
        "diff --git a/doc.md b/doc.md\n"
        "--- a/doc.md\n"
        "+++ b/doc.md\n"
        "@@ -0,0 +5 @@\n"
        f"+{body}\n"
    )
    assert mod._added_from_diff_text(plain) == {Path("doc.md"): {5}}

    # (4) A stamp-shaped suffix on a line with NO `-` twin (a pure insertion)
    #     is still an added line: there is nothing it could be identical to.
    inserted = (
        "diff --git a/doc.md b/doc.md\n"
        "--- a/doc.md\n"
        "+++ b/doc.md\n"
        "@@ -0,0 +8 @@\n"
        f"+{body + stamp}\n"
    )
    assert mod._added_from_diff_text(inserted) == {Path("doc.md"): {8}}, (
        "a newly INSERTED line was waved through because it happened to carry a stamp"
    )


if __name__ == "__main__":
    test_link_form_and_bare_form_stale_anchors_are_both_caught()
    test_cite_re_branches_and_cite_path_helper()
    test_scan_path_exit_code_is_still_zero()
    test_new_cite_ratchet_flags_only_added_unexcerpted_kb_cites()
    test_new_cite_ratchet_passes_when_every_added_cite_is_excerpted()
    test_new_cite_ratchet_scope_predicate()
    test_emphasis_quote_excerpts_satisfy_the_ratchet()
    test_emphasis_quote_excerpt_across_a_hard_line_wrap_is_seen()
    test_quote_recognizer_does_not_swallow_non_excerpts()
    test_bare_double_quote_excerpts_satisfy_the_ratchet()
    test_bare_quotes_are_a_last_resort_and_never_displace_a_house_style_span()
    test_fixture_trees_are_pruned_from_the_advisory_crawl()
    print("test_verify_anchor_content: PASSED")

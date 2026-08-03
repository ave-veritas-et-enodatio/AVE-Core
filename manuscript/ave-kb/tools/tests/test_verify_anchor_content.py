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

The tree is built in a tmpdir rather than under tests/fixtures/ on purpose:
verify-anchor-content's SKIP_DIRS does NOT prune `tests/fixtures` (unlike its
sibling verify-md-links), so on-disk stale-anchor fixtures would be scanned as
corpus and would show up as permanent findings in the advisory count.

Run directly (`python tools/tests/test_verify_anchor_content.py`) or via pytest.
"""

import importlib.util
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


if __name__ == "__main__":
    test_link_form_and_bare_form_stale_anchors_are_both_caught()
    test_cite_re_branches_and_cite_path_helper()
    test_scan_path_exit_code_is_still_zero()
    print("test_verify_anchor_content: PASSED")

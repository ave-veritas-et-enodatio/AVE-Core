"""Self-test for manuscript/ave-kb/tools/verify-md-links.py.

Runs the checker against the fixture pair under tools/tests/fixtures/ and
asserts the exact finding set: a good link resolves, a broken intra link, a
broken inter link, a code-fence/inline example link is ignored, and an
unknown-id citation is flagged while the literal placeholder is not.

Run directly (`python tools/tests/test_verify_md_links.py`) or via pytest.
"""

import importlib.util
import sys
import tempfile
from pathlib import Path

_TOOL = Path(__file__).resolve().parent.parent / "verify-md-links.py"
_FIXTURES = Path(__file__).resolve().parent / "fixtures"


def _load_module():
    spec = importlib.util.spec_from_file_location("verify_md_links", _TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    # Register before exec so dataclasses can resolve string annotations
    # (PEP 563) against the module's namespace.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_fixture_findings() -> None:
    vml = _load_module()
    sample = _FIXTURES / "sample.md"
    # Treat the fixtures dir as the repo root so the inter-repo link escapes it.
    repo_root = _FIXTURES.resolve()
    body = vml.strip_code(sample.read_text(encoding="utf-8"))

    link_findings = vml.check_links(sample, body, repo_root)
    kinds = sorted((f.kind, f.target) for f in link_findings)

    # Good links (neighbor.md, with anchor, with :linenum) must NOT appear.
    assert ("broken intra", "neighbor.md") not in kinds
    # Broken intra link is flagged.
    assert ("broken intra", "does-not-exist.md") in kinds
    # Broken inter link (escapes fixtures root) is flagged as inter.
    assert ("broken inter", "../../../../AVE-HOPF/nope.md") in kinds
    # External link is skipped entirely.
    assert all("example.com" not in t for _, t in kinds)
    # Fenced and inline-code example links are ignored.
    assert all("not-real" not in t for _, t in kinds)
    # Exactly one broken intra + one broken inter from prose.
    assert sum(1 for k, _ in kinds if k == "broken intra") == 1
    assert sum(1 for k, _ in kinds if k == "broken inter") == 1

    # Id-validity: known set deliberately omits clm-zzzzzz.
    known_ids = {"clm-abc123"}
    id_findings = vml.check_ids(sample, body, known_ids)
    id_targets = sorted(f.target for f in id_findings)
    assert id_targets == ["clm-zzzzzz"], id_targets  # placeholder + fence excluded


def test_tex_and_home_targets_skipped() -> None:
    vml = _load_module()
    sample = _FIXTURES / "sample.md"
    repo_root = _FIXTURES.resolve()
    body = vml.strip_code(sample.read_text(encoding="utf-8"))

    targets = {f.target for f in vml.check_links(sample, body, repo_root)}
    # .tex targets (with and without a :linenum suffix) are never classified.
    assert not any(t.endswith(".tex") or ".tex:" in t for t in targets)
    assert "manuscript/vol_1/main.tex" not in targets
    assert "nope.tex:42" not in targets
    # Home-dir (~) targets are never classified.
    assert not any(t.startswith("~") for t in targets)


def test_skip_trees_excluded_from_crawl() -> None:
    vml = _load_module()
    repo_root = _FIXTURES.resolve()
    crawled = {p.resolve() for p in vml.iter_markdown_files(repo_root)}

    # _archive/ trees are skipped entirely; non-skipped siblings under the same
    # parent are still crawled.
    assert (repo_root / "skiptrees" / "_archive" / "arch.md").resolve() not in crawled
    assert (repo_root / "skiptrees" / "live.md").resolve() in crawled
    assert (repo_root / "skiptrees" / "scratch.md").resolve() in crawled

    # The .agents/ skip can't use a committed fixture (.agents/ is gitignored
    # repo-wide), so build the tree at runtime to exercise the crawl skip.
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / ".agents").mkdir()
        (root / ".agents" / "note.md").write_text("x", encoding="utf-8")
        (root / "keep.md").write_text("y", encoding="utf-8")
        tmp_crawled = {p.resolve() for p in vml.iter_markdown_files(root)}
        assert (root / ".agents" / "note.md").resolve() not in tmp_crawled
        assert (root / "keep.md").resolve() in tmp_crawled


def test_source_gating_predicate() -> None:
    vml = _load_module()
    repo_root = Path("/repo")

    def src(rel: str) -> Path:
        return repo_root / rel

    # KB tree (excluding session/) is an error source -> gates.
    assert vml.is_error_source(src("manuscript/ave-kb/common/foo.md"), repo_root)
    # KB session/ subtree is NOT an error source.
    assert not vml.is_error_source(src("manuscript/ave-kb/session/note.md"), repo_root)
    # Repo-root user-facing docs gate.
    assert vml.is_error_source(src("README.md"), repo_root)
    assert vml.is_error_source(src("LIVING_REFERENCE.md"), repo_root)
    assert vml.is_error_source(src("AGENTS.md"), repo_root)
    # research/ and other trees are warn-only.
    assert not vml.is_error_source(src("research/analysis.md"), repo_root)
    assert not vml.is_error_source(src("src/ave/notes.md"), repo_root)
    # A non-root README (nested) does not gate.
    assert not vml.is_error_source(src("docs/README.md"), repo_root)


def test_source_gating_exit_code() -> None:
    """KB-source broken-intra gates (exit 1); research-source broken-intra warns (exit 0)."""
    vml = _load_module()
    repo_root = Path("/repo")
    Finding = vml.Finding

    kb = Finding(repo_root / "manuscript/ave-kb/common/foo.md", 1, "broken intra", "missing.md")
    research = Finding(repo_root / "research/r.md", 1, "broken intra", "missing.md")

    assert vml.is_gating(kb, repo_root)
    assert not vml.is_gating(research, repo_root)
    # broken inter is never gating here (handled by --inter-repo).
    inter = Finding(repo_root / "manuscript/ave-kb/common/foo.md", 1, "broken inter", "../x.md")
    assert not vml.is_gating(inter, repo_root)


def test_ignored_paths_carveout() -> None:
    """Broken links into an IGNORED_PATHS dir (e.g. assets/sim_outputs/) are never reported."""
    vml = _load_module()
    repo_root = Path("/repo")

    # A missing target under assets/sim_outputs/ is exempt (gitignored artifact dir).
    under = (repo_root / "manuscript/ave-kb/common").joinpath(
        "../../../assets/sim_outputs/trampoline_framework/missing.png"
    ).resolve()
    assert vml._under_ignored_path(under, repo_root)
    # The carved-out dir itself, referenced directly, is also exempt.
    assert vml._under_ignored_path((repo_root / "assets/sim_outputs").resolve(), repo_root)
    # A sibling asset path NOT in the carveout is not exempt.
    assert not vml._under_ignored_path((repo_root / "assets/figures/x.png").resolve(), repo_root)
    # A path outside the repo is not exempt.
    assert not vml._under_ignored_path(Path("/elsewhere/assets/sim_outputs/x.png"), repo_root)


def test_strip_code_preserves_line_numbers() -> None:
    vml = _load_module()
    text = "a\n```\nb\nc\n```\nd `e` f\n"
    stripped = vml.strip_code(text)
    assert len(stripped.splitlines()) == len(text.splitlines())
    assert "b" not in stripped and "c" not in stripped  # fence body blanked
    assert "`e`" not in stripped  # inline span blanked
    assert stripped.splitlines()[0] == "a"


def test_kbleaf_normalize() -> None:
    vml = _load_module()
    norm = vml.normalize_kbleaf_target
    assert norm(r"a\_b/c\_d.md") == "a_b/c_d.md"
    assert norm("leaf.md:42") == "leaf.md"
    assert norm("leaf.md:8-24") == "leaf.md"
    assert norm("leaf.md:133--147") == "leaf.md"
    assert norm("mod.py::fn") == "mod.py"
    assert norm("mod.py::fn()") == "mod.py"
    assert norm("mod.py:fn()") == "mod.py"


def test_kbleaf_fixture_findings() -> None:
    vml = _load_module()
    repo_root = (_FIXTURES / "texcheck").resolve()
    findings, checked, skipped = vml.scan_kbleaf(repo_root, waived=frozenset())
    by_kind = {}
    for f in findings:
        by_kind.setdefault(f.kind, set()).add(f.target)

    # Dead: wrong-directory cite (same basename elsewhere), bare missing file,
    # dead ellipsis glob, dead directory ref, and the split cite's bare tail.
    assert by_kind.get("dead kbleaf") == {
        "ave-kb/vol1/nested-leaf.md",
        r"missing\_leaf.md",
        "ave-kb/.../gone.md",
        "ave-kb/vol4/void/",
        "leaf.md",
    }, by_kind.get("dead kbleaf")
    # Split \texttt{prefix-} \kbleaf{tail} pattern is flagged.
    assert by_kind.get("split kbleaf") == {r"\texttt{nested-} \kbleaf{leaf.md}"}
    # Missing sibling repo is inter-class; present sibling resolves.
    assert by_kind.get("broken inter") == {"AVE-Nope/manuscript/x.tex"}
    # Everything resolvable resolved: no good target appears in any finding.
    flagged = {t for ts in by_kind.values() for t in ts}
    for good in (
        "ave-kb/vol1/good-leaf.md",
        "manuscript/ave-kb/vol1/good-leaf.md:12",
        "deep/nested-leaf.md:5--9",
        r"tool\_script.py",
        r"tool\_script.py::some_fn()",
        "ave-kb/vol1/good-leaf.[a-z]d",
        "ave-kb/.../nested-leaf.md",
        "AVE-Sib/manuscript/doc.tex",
        "ave-kb/vol4/deep/",
        "commented/out/path.md",
    ):
        assert good not in flagged, good
    # Non-path args (identifiers, shell snippets, extensionless stems) skipped.
    assert skipped == 4, skipped  # grep-snippet, M.ELECTRON, formula, stem
    assert checked == 15, checked


def test_kbleaf_waiver_and_staleness() -> None:
    vml = _load_module()
    repo_root = (_FIXTURES / "texcheck").resolve()
    src = "manuscript/chapters/sample.tex"

    # A waived (source, arg) pair downgrades to `waived kbleaf` (non-gating).
    waived = frozenset({(src, "ave-kb/vol1/nested-leaf.md")})
    findings, _, _ = vml.scan_kbleaf(repo_root, waived=waived)
    kinds = {(f.kind, f.target) for f in findings}
    assert ("waived kbleaf", "ave-kb/vol1/nested-leaf.md") in kinds
    assert ("dead kbleaf", "ave-kb/vol1/nested-leaf.md") not in kinds
    assert ("stale kbleaf waiver", "ave-kb/vol1/nested-leaf.md") not in kinds

    # A waiver matching no live dead cite is reported stale (gating).
    stale = frozenset({(src, "already-fixed.md")})
    findings, _, _ = vml.scan_kbleaf(repo_root, waived=stale)
    assert ("stale kbleaf waiver", "already-fixed.md") in {(f.kind, f.target) for f in findings}


def test_kbleaf_gating_kinds() -> None:
    vml = _load_module()
    repo_root = Path("/repo")
    Finding = vml.Finding
    tex = repo_root / "manuscript/vol_1_foundations/chapters/x.tex"

    assert vml.is_gating(Finding(tex, 1, "dead kbleaf", "gone.md"), repo_root)
    assert vml.is_gating(Finding(tex, 1, "split kbleaf", "..."), repo_root)
    assert vml.is_gating(Finding(tex, 0, "stale kbleaf waiver", "x.md"), repo_root)
    assert not vml.is_gating(Finding(tex, 1, "waived kbleaf", "x.md"), repo_root)
    # kbleaf sibling-repo misses stay inter-class (never gating here).
    assert not vml.is_gating(Finding(tex, 1, "broken inter", "AVE-X/y.tex"), repo_root)


# --- line-cite existence pass (cite-rot options 2+3) ------------------------

_LINECHECK = _FIXTURES / "linecheck"
_CITER = "manuscript/ave-kb/common/citer.md"
_FROZEN = "research/2026-01-01_fixture_prereg-FROZEN.md"


def _scan_linecheck(vml, waived=frozenset()):
    """Run the line-cite pass over the linecheck fixture repo."""
    repo_root = _LINECHECK.resolve()
    file_index, _ = vml.build_kbleaf_target_index(repo_root)
    findings, stats = vml.scan(
        repo_root, check_ids_enabled=False, file_index=file_index, waived_line_cites=waived
    )
    return repo_root, findings, stats


def _cites(findings, repo_root, kind, source):
    return sorted(
        f.target
        for f in findings
        if f.kind == kind and str(f.file.resolve().relative_to(repo_root)) == source
    )


def test_line_cite_mutation_now_fails() -> None:
    """THE REGRESSION TEST: the mutation that proved the gap must now gate.

    The #847 auditor rewrote a live KB cite to a bogus path plus an absurd line
    number and re-ran the checker: exit 0, `gating errors: 0`, finding list
    byte-identical. Both halves of that mutation are reproduced in the fixture
    (`no-such-file-anywhere.md:12` and `target.md:999`), and both must now be
    seen — the line half as a GATING `dead line cite`, the path half as an
    advisory `broken backtick path` (it was previously invisible end-to-end).
    """
    vml = _load_module()
    repo_root, findings, _ = _scan_linecheck(vml)

    dead = _cites(findings, repo_root, "dead line cite", _CITER)
    assert "target.md:999" in dead, dead
    gating = [f for f in findings if f.kind == "dead line cite" and vml.is_gating(f, repo_root)]
    assert gating, "a KB-source dead line cite must flip the exit code"

    bogus = _cites(findings, repo_root, "broken backtick path", _CITER)
    assert bogus == ["no-such-file-anywhere.md:12"], bogus


def test_line_cite_valid_cites_pass() -> None:
    """A cite whose line exists produces no finding, in every written form."""
    vml = _load_module()
    repo_root, findings, _ = _scan_linecheck(vml)
    flagged = {f.target for f in findings}

    for good in (
        "target.md:5",  # backticked, content line
        "target.md:5-9",  # backticked range, fully inside the file
        "../../../src/tool.py:5",  # parent-dir hop (the `..` regression)
        "twin.md:300",  # ambiguous basename, one candidate is long enough
    ):
        assert good not in flagged, good


def test_line_cite_sees_all_three_written_forms() -> None:
    """Backticked-bare, link-in and link-ext cites are all parsed and checked."""
    vml = _load_module()
    text = (_LINECHECK / _CITER).read_text(encoding="utf-8")
    forms = {(c.form, c.as_written) for c in vml.iter_line_cites(text)}

    assert ("backticked", "target.md:999") in forms  # invisible before this pass
    assert ("link-ext", "target.md:999") in forms  # KB house convention
    assert ("link-in", "target.md:998") in forms
    # A backticked span that is not wholly a path is not a cite.
    assert not any(w == "the quick brown fox" for _, w in forms)
    # Fenced-block cites stay illustrative: the fixture's last prose cite is on
    # line 26 and its fenced examples are on line 32, so nothing past 26 parses.
    assert max(c.lineno for c in vml.iter_line_cites(text)) == 26

    repo_root, findings, _ = _scan_linecheck(vml)
    dead = _cites(findings, repo_root, "dead line cite", _CITER)
    assert dead.count("target.md:999") == 2, dead  # backticked + link-ext
    assert "target.md:998" in dead  # link-in


def test_line_cite_historical_pin_not_flagged() -> None:
    """A cite on a line carrying a backticked SHA is deliberately past-state."""
    vml = _load_module()
    text = (_LINECHECK / _CITER).read_text(encoding="utf-8")
    pinned = [c for c in vml.iter_line_cites(text) if c.pinned]
    assert [c.as_written for c in pinned] == ["target.md:999"], pinned

    _, _, stats = _scan_linecheck(vml)
    assert stats["skipped_historical_pin"] == 1, stats
    # The same cite text appears unpinned twice elsewhere in the fixture and
    # IS flagged there, so the skip is the pin's doing, not the target's.
    assert stats["dead"] >= 3


def test_line_cite_frozen_doc_reported_not_gated() -> None:
    """A dead cite in a byte-frozen research doc warns; it never forces an edit."""
    vml = _load_module()
    repo_root, findings, _ = _scan_linecheck(vml)

    frozen = [
        f
        for f in findings
        if f.kind == "dead line cite"
        and str(f.file.resolve().relative_to(repo_root)) == _FROZEN
    ]
    assert len(frozen) == 1, frozen
    assert not vml.is_gating(frozen[0], repo_root), "frozen research doc must not gate"


def test_line_cite_zero_fp_guards() -> None:
    """The shapes that must never be flagged: ambiguity, patterns, blanks, skips."""
    vml = _load_module()
    repo_root, findings, stats = _scan_linecheck(vml)
    dead = _cites(findings, repo_root, "dead line cite", _CITER)

    # Ambiguous basename: flagged only when NO candidate is long enough.
    assert "twin.md:300" not in dead
    assert "twin.md:900" in dead
    # Range: flagged on the END overrunning, not just the start.
    assert "target.md:28-44" in dead
    # Shape skips never become findings.
    for skipped in ("vol9/.../gone.md:4", "AVE-HOPF/docs/glossary.md:9", "~/.claude/notes.md:3"):
        assert skipped not in {f.target for f in findings}, skipped
    # Two of those three reach `cite_target_uncheckable`; the `~/...` one never
    # parses as a cite at all (`~` is outside the path grammar), so it is
    # dropped one layer earlier and is not counted as a shape skip.
    assert stats["skipped_shape"] == 2, stats
    # A bare path with no :NN is counted, never flagged.
    assert stats["path_only"] == 1, stats

    # Blank / decoration-only cited lines are ADVISORY, never gating.
    blank = _cites(findings, repo_root, "blank line cite", _CITER)
    assert blank == ["target.md:12", "target.md:18"], blank
    for finding in findings:
        if finding.kind in vml._ADVISORY_CITE_KINDS:
            assert not vml.is_gating(finding, repo_root), finding


def test_line_cite_waiver_and_staleness() -> None:
    """A waived dead cite downgrades; a waiver with no live subject gates."""
    vml = _load_module()

    waived = frozenset({(_CITER, "target.md:999")})
    repo_root, findings, stats = _scan_linecheck(vml, waived=waived)
    kinds = {(f.kind, f.target) for f in findings}
    assert ("waived line cite", "target.md:999") in kinds
    assert stats["dead_waived"] == 2, stats  # backticked + link-ext, both waived
    waived_findings = [f for f in findings if f.kind == "waived line cite"]
    assert all(not vml.is_gating(f, repo_root) for f in waived_findings)

    stale = frozenset({(_CITER, "already-repaired.md:1")})
    _, findings, _ = _scan_linecheck(vml, waived=stale)
    stale_findings = [f for f in findings if f.kind == "stale line-cite waiver"]
    assert [f.target for f in stale_findings] == ["already-repaired.md:1"]
    assert vml.is_gating(stale_findings[0], _LINECHECK.resolve())


def test_line_cite_union_resolution_kills_the_wrong_file_fp() -> None:
    """Bare-basename cites resolve to EVERY candidate, not the first one found.

    Direct-only resolution fires falsely on live corpus cites: `CLAUDE.md:182`
    resolves to the 125-line repo-root copy before the 353-line KB copy the
    author meant. The union is what makes the check zero-FP.
    """
    vml = _load_module()
    repo_root = _LINECHECK.resolve()
    file_index, _ = vml.build_kbleaf_target_index(repo_root)
    citer = repo_root / _CITER

    candidates = vml.resolve_cite_candidates("twin.md", citer, repo_root, file_index)
    rels = sorted(str(c.relative_to(repo_root)) for c in candidates)
    assert rels == [
        "manuscript/ave-kb/common/twin.md",
        "manuscript/ave-kb/vol9/deep/twin.md",
    ], rels


def test_strip_fences_keeps_inline_spans() -> None:
    """strip_fences is the complement of strip_code — inline spans SURVIVE."""
    vml = _load_module()
    text = "a `keep.md:1`\n```\n`drop.md:2`\n```\nb `keep.md:3`\n"
    fenced = vml.strip_fences(text)
    assert len(fenced.splitlines()) == len(text.splitlines())
    assert "`keep.md:1`" in fenced and "`keep.md:3`" in fenced
    assert "drop.md" not in fenced
    # strip_code (used by the LINK pass) still blanks them — that difference is
    # the whole reason the backticked form was invisible.
    assert "keep.md" not in vml.strip_code(text)


def test_cite_target_uncheckable_shapes() -> None:
    vml = _load_module()
    for pattern in (
        "~/.claude/x.md",
        "/abs/x.md",
        "AVE-HOPF/docs/glossary.md",
        "Applied-Vacuum-Engineering/manuscript/x.md",
        "vol3/.../leaf.md",
        "core/chiral_lattice_v9..v17.py",
        "leaf.[a-z]d",
        ".agents/handoffs/note.md",
        "assets/sim_outputs/figure.csv",
    ):
        assert vml.cite_target_uncheckable(pattern), pattern
    for real in (
        "manuscript/ave-kb/common/leaf.md",
        "../../src/ave/core/constants.py",
        "../common/interlock-register.md",
        "leaf.md",
    ):
        assert not vml.cite_target_uncheckable(real), real


if __name__ == "__main__":
    test_fixture_findings()
    test_tex_and_home_targets_skipped()
    test_skip_trees_excluded_from_crawl()
    test_source_gating_predicate()
    test_source_gating_exit_code()
    test_ignored_paths_carveout()
    test_strip_code_preserves_line_numbers()
    test_kbleaf_normalize()
    test_kbleaf_fixture_findings()
    test_kbleaf_waiver_and_staleness()
    test_kbleaf_gating_kinds()
    test_line_cite_mutation_now_fails()
    test_line_cite_valid_cites_pass()
    test_line_cite_sees_all_three_written_forms()
    test_line_cite_historical_pin_not_flagged()
    test_line_cite_frozen_doc_reported_not_gated()
    test_line_cite_zero_fp_guards()
    test_line_cite_waiver_and_staleness()
    test_line_cite_union_resolution_kills_the_wrong_file_fp()
    test_strip_fences_keeps_inline_spans()
    test_cite_target_uncheckable_shapes()
    print("OK: all self-tests passed")

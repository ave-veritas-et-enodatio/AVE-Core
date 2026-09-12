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


def _scan_linecheck(vml, waived=frozenset(), heritage=True):
    """Run the line-cite pass over the linecheck fixture repo.

    `heritage` is pinned ON by default rather than inherited from
    `HERITAGE_PIN_EXEMPTION`. These fixtures were written when the exemption
    was the shipped default and their expected finding sets encode that arm;
    the flip of 2026-09-12 changed the DEFAULT, not the arm, and the arm is
    still reachable and still has to behave. `test_linecheck_fixture_under_the
    _shipped_default` below asserts the post-flip default separately, so both
    states are covered rather than one silently replacing the other.
    """
    repo_root = _LINECHECK.resolve()
    file_index, _ = vml.build_kbleaf_target_index(repo_root)
    findings, stats = vml.scan(
        repo_root,
        check_ids_enabled=False,
        file_index=file_index,
        waived_line_cites=waived,
        heritage_exemption=heritage,
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
    # Counter renamed at the R2 pin-marker landing: this is the HERITAGE
    # disposition, now counted apart from the marker one.
    assert stats["exempt_heritage"] == 1, stats
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


# --- R2 author-declared pin marker (`` pin:`<sha>` ``) ----------------------
#
# The token is the CORPUS'S OWN, defined at manuscript/ave-kb/CONVENTIONS.md on
# 2026-08-06. These tests split into two halves on purpose:
#
#   GRAMMAR / BINDING — the static `pincheck/` fixture tree. Synthetic repo
#     root, synthetic 20-line target, synthetic SHAs, pin validation OFF. No
#     live line number, no live commit, no branch shape, nothing about this
#     repo's own state is asserted anywhere.
#   OBJECT STORE — `test_pin_resolution_*`, against a throwaway git repo the
#     test BUILDS in a temp dir. Real commits, real trees, real shallow clone.
#     Also nothing to do with this repo.

_PINCHECK = _FIXTURES / "pincheck"
_PIN_CITER = "manuscript/ave-kb/common/citer.md"
_PIN_NOTES = "research/2026-01-01_fixture_notes.md"


def _scan_pincheck(vml, heritage=True, pin_store=None):
    """Run the line-cite pass over the pin fixture repo (validation off)."""
    repo_root = _PINCHECK.resolve()
    file_index, _ = vml.build_kbleaf_target_index(repo_root)
    findings, stats = vml.scan(
        repo_root,
        check_ids_enabled=False,
        file_index=file_index,
        heritage_exemption=heritage,
        pin_store=pin_store,
    )
    return repo_root, findings, stats


def _pin_cites(vml):
    text = (_PINCHECK / _PIN_CITER).read_text(encoding="utf-8")
    return {c.as_written: c for c in vml.iter_line_cites(text)}


def test_pin_marker_is_per_cite_not_per_line() -> None:
    """★ THE R2 PROPERTY. One long row; the marker exempts ITS cite and no other.

    The heritage heuristic skips every line-cite on any SHA-bearing line, and
    the KB's rows run to thousands of characters mixing one provenance SHA with
    several live cites. The marker must not inherit that. The fixture's star row
    carries a marker-pinned cite that is DEAD at HEAD (``target.md:900``
    ``pin:`aaaaaaa1` ``, against a 20-line target) beside an unmarked cite that
    is equally dead (`target.md:901`).

    Note what makes this test possible at all: the marker spells its SHA in
    backticks, so the row WOULD read as heritage-exempt on the marker's own
    SHA — handing back the row-scoped coarseness. `iter_line_cites` masks
    markers before asking the heritage question, and `cite.pinned` being False
    for both cites here is that mask being load-bearing.

    If this test fails, nothing else in the change matters.
    """
    vml = _load_module()
    repo_root, findings, _ = _scan_pincheck(vml)

    by_written = _pin_cites(vml)
    star = [by_written["target.md:900 pin:`aaaaaaa1`"], by_written["target.md:901"]]
    assert len({c.lineno for c in star}) == 1, "both cites must share one line"
    row = (_PINCHECK / _PIN_CITER).read_text(encoding="utf-8").splitlines()[star[0].lineno - 1]
    assert len(row) > 500, len(row)  # ledger-row shaped, like the real corpus
    assert vml._HISTORICAL_PIN_RE.search(row), "the raw row DOES carry a backticked sha ..."
    assert not any(c.pinned for c in star), "... and it must not count as heritage"

    dead = _cites(findings, repo_root, "dead line cite", _PIN_CITER)
    # The unmarked neighbour FAILS ...
    assert "target.md:901" in dead, dead
    # ... and the marked one does not, though it is just as dead at HEAD.
    assert "target.md:900 pin:`aaaaaaa1`" not in dead, dead
    gating = [
        f
        for f in findings
        if f.kind == "dead line cite"
        and f.target == "target.md:901"
        and vml.is_gating(f, repo_root)
    ]
    assert gating, "the unmarked dead cite on the star row must flip the exit code"


def test_pin_marker_all_three_written_forms() -> None:
    """The marker rides the backticked, link-in and link-ext cite forms alike."""
    vml = _load_module()
    repo_root, findings, stats = _scan_pincheck(vml)
    reported = {f.target for f in findings}
    for marked in (
        "target.md:900 pin:`aaaaaaa1`",  # backticked
        "target.md:905 pin:`aaaaaaa1`",  # link-ext
        "target.md:906 pin:`aaaaaaa1`",  # link-in
        "target.md:5 pin:`aaaaaaa1`",  # marked and still live
        "gone-in-a-rename.md:7 pin:`aaaaaaa1`",  # marked, path itself gone
    ):
        assert marked in _pin_cites(vml), f"{marked} must PARSE as a marked cite"
        assert marked not in reported, f"{marked} must not be reported"
    # A marker on a since-renamed path is exempt, not a `broken backtick path`:
    # the disposition is decided before HEAD resolution runs.
    assert _cites(findings, repo_root, "broken backtick path", _PIN_CITER) == []
    assert stats["exempt_marker"] == 14, stats


def test_pin_marker_survives_trailing_punctuation() -> None:
    """★ DEFECT (1). Sentence punctuation after a marker must not break it.

    A glued `@<sha>` marker has no closing delimiter, so `...:900@1cde93ca.`
    captures the SHA as `1cde93ca.`, calls it malformed, and red-lights
    `make verify` on a legitimate pin at the end of a sentence. The corpus's
    token closes with a backtick, so the SHA cannot absorb what follows it.
    Every cite below is dead at HEAD; each must be silently exempt.
    """
    vml = _load_module()
    repo_root, findings, _ = _scan_pincheck(vml)
    by_written = _pin_cites(vml)
    reported = {f.target for f in findings}
    dead = _cites(findings, repo_root, "dead line cite", _PIN_CITER)

    cases = {
        920: "full stop",
        921: "comma",
        922: "semicolon",
        923: "close paren",
        924: "single emphasis",
        925: "double emphasis",
        926: "end of line",
        930: "inside a pipe-delimited table cell",
        940: "inside a blockquote",
    }
    for line, why in cases.items():
        written = f"target.md:{line} pin:`aaaaaaa1`"
        cite = by_written.get(written)
        assert cite is not None, f"{why}: marker did not bind ({written})"
        assert cite.pin == "aaaaaaa1", f"{why}: captured {cite.pin!r}, punctuation swallowed"
        assert cite.pin_wellformed, why
        assert written not in reported, f"{why}: reported {written}"
        assert f"target.md:{line}" not in dead, why

    # CONTROL, same table: the unmarked neighbour in the next row IS dead, so
    # the table cases above are exempt by their marker and not by the table.
    assert "target.md:931" in dead, dead


def test_pin_marker_rejections_both_directions() -> None:
    """A marker the tool cannot read exempts NOTHING, and says so."""
    vml = _load_module()
    repo_root, findings, stats = _scan_pincheck(vml)
    dead = _cites(findings, repo_root, "dead line cite", _PIN_CITER)
    malformed = _cites(findings, repo_root, "malformed pin marker", _PIN_CITER)
    orphan = _cites(findings, repo_root, "orphan pin marker", _PIN_CITER)

    assert malformed == [
        "target.md pin:`aaaaaaa1`",  # nothing to pin — no :NN
        "target.md:903 pin:`zzz`",  # not hex
        "target.md:904 pin:`12`",  # too short
        "target.md:909 pin:aaaaaaa1",  # unbackticked: no closing delimiter
    ], malformed
    # ... and each of those cites is then CHECKED, so both halves land. The
    # dead finding carries the marker in its text, because the author has to be
    # shown the marker that did not work.
    for still_checked in (
        "target.md:903 pin:`zzz`",
        "target.md:904 pin:`12`",
        "target.md:909 pin:aaaaaaa1",
    ):
        assert still_checked in dead, (still_checked, dead)

    # A well-formed marker that MISSED the cite on its row is reported rather
    # than dropped, and the cite it was aimed at stays gated.
    assert orphan == ["pin:`aaaaaaa3`"], orphan
    assert "target.md:910" in dead, dead
    # BOTH DIRECTIONS on the narrowing: the same token, on a row carrying no
    # location cite, is documentation and must NOT be reported. Without this
    # arm the gate red-lights any file that DESCRIBES the marker — which the
    # KB's own CONVENTIONS.md does, in a table, with real-looking SHAs.
    assert "pin:`aaaaaaa2`" not in orphan, orphan
    assert stats["pin_orphan"] == 1 and stats["pin_malformed"] == 5, stats  # +1 non-KB


def test_pin_marker_source_gating_respected() -> None:
    """The new kinds are source-scoped like `dead line cite`, not unconditional."""
    vml = _load_module()
    repo_root, findings, _ = _scan_pincheck(vml)
    inside = [
        f
        for f in findings
        if f.kind in vml._PIN_MARKER_KINDS
        and str(f.file.resolve().relative_to(repo_root)) == _PIN_CITER
    ]
    assert inside and all(vml.is_gating(f, repo_root) for f in inside), inside

    outside = [
        f
        for f in findings
        if f.kind in vml._PIN_MARKER_KINDS
        and str(f.file.resolve().relative_to(repo_root)) == _PIN_NOTES
    ]
    assert [f.target for f in outside] == ["target.md:908 pin:`zzz`"], outside
    assert not vml.is_gating(outside[0], repo_root), "non-KB source must warn, not gate"


def test_three_dispositions_counted_separately() -> None:
    """MARKER-EXEMPT / HERITAGE-EXEMPT / CHECKED are three distinct counters."""
    vml = _load_module()
    _, _, stats = _scan_pincheck(vml)
    assert stats["exempt_marker"] == 14, stats
    assert stats["exempt_heritage"] == 1, stats  # the one bare-SHA prose row
    assert stats["checked"] >= 4, stats
    # ★ NO CITE IS COUNTED IN TWO DISPOSITIONS AT ONCE, and none falls between
    # them: the three counters must partition every parsed `:NN` cite in the
    # whole fixture tree. Counted from a LIST over every file `scan` walks —
    # not from a by-text mapping, since two cites may be written identically.
    parsed = [
        c
        for md in vml.iter_markdown_files(_PINCHECK.resolve())
        for c in vml.iter_line_cites(md.read_text(encoding="utf-8"))
        if c.start is not None
    ]
    assert parsed, "the fixture must actually contain cites"
    assert stats["exempt_marker"] + stats["exempt_heritage"] + stats["checked"] == len(parsed)


def test_heritage_switch_shipped_off_and_both_arms_still_fire() -> None:
    """R2's re-key switch exists, fires both ways, and now ships OFF.

    Flipped 2026-09-12 (R2 terminal step), measured free on the live corpus:
    485 cites moved HERITAGE-EXEMPT -> CHECKED, `dead line cite` stayed at 11
    and stayed the SAME eleven, GATING dead 0 -> 0.
    """
    vml = _load_module()
    assert vml.HERITAGE_PIN_EXEMPTION is False, "the switch ships OFF since 2026-09-12"

    # ON (default): the grandfathered cite is exempt.
    repo_root, findings, on_stats = _scan_pincheck(vml, heritage=True)
    assert "target.md:902" not in _cites(findings, repo_root, "dead line cite", _PIN_CITER)
    assert on_stats["exempt_heritage"] == 1 and on_stats["heritage_demoted"] == 0, on_stats

    # OFF: the same cite is checked, and it is dead.
    repo_root, findings, off_stats = _scan_pincheck(vml, heritage=False)
    assert "target.md:902" in _cites(findings, repo_root, "dead line cite", _PIN_CITER)
    assert off_stats["exempt_heritage"] == 0 and off_stats["heritage_demoted"] == 1, off_stats
    # Marker exemption is untouched by the switch — that is the point of re-keying.
    assert off_stats["exempt_marker"] == 14, off_stats


def test_linecheck_fixture_under_the_shipped_default() -> None:
    """The post-flip DEFAULT checks the grandfathered cite instead of skipping it.

    `_scan_linecheck` pins the heritage arm ON so the pre-flip fixtures keep
    testing what they were written to test. This is the other half: run the
    same fixture with the arm left at whatever the module ships, and assert
    the shipped state is the demoting one. Without this the suite would go on
    proving the OLD default forever while `make verify` ran the new one.
    """
    vml = _load_module()
    repo_root = _LINECHECK.resolve()
    file_index, _ = vml.build_kbleaf_target_index(repo_root)
    findings, stats = vml.scan(repo_root, check_ids_enabled=False, file_index=file_index)

    assert stats["exempt_heritage"] == 0, stats
    assert stats["heritage_demoted"] == 1, stats
    # The demoted cite is the fixture's one SHA-on-the-line cite, and it is dead.
    assert "target.md:999" in _cites(findings, repo_root, "dead line cite", _CITER)


def test_main_honours_the_constant_not_only_the_flag() -> None:
    """★ THE FLIP MUST BE THE ONE LINE THE COMMENT PROMISES.

    Regression on a real defect found at the 2026-09-12 landing: `main()` bound
    `heritage_exemption=not args.no_heritage_pin_exemption`, reading the CLI
    flag and NEVER the constant. Setting `HERITAGE_PIN_EXEMPTION = False` was
    therefore a no-op for every ordinary run, `make verify` included — the
    switch was decorative and the migration's terminal step could have been
    "landed" without changing a single check.

    Both directions, through `main()` itself and WITH NO FLAG ON THE COMMAND
    LINE, on a throwaway repo whose one heritage-exempt cite is dead: constant
    OFF -> exit 1; constant monkeypatched back ON -> exit 0. If the binding
    ever stops reading the constant, the second arm keeps passing and the
    first one flips.
    """
    vml = _load_module()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        leaf = root / "manuscript" / "ave-kb" / "common"
        leaf.mkdir(parents=True)
        # 3 lines. `:99` is rot; `:2` is live. Both sit on a line carrying a
        # backticked SHA, so both are HERITAGE-EXEMPT while the arm is ON.
        (leaf / "target.md").write_text("one\ntwo\nthree\n", encoding="utf-8")
        (leaf / "citer.md").write_text(
            "# citer\n\n"
            "- measured at `b649f9f2` — see `target.md:99` for the claim.\n",
            encoding="utf-8",
        )
        argv = ["--root", str(root), "--no-id-check", "--no-kbleaf-check",
                "--no-pin-sha-check"]

        # The whole point: NO FLAG IS PASSED. Whatever decides this run is the
        # module-level constant, or the constant is decorative.
        assert vml.HERITAGE_PIN_EXEMPTION is False
        assert vml.main(argv) == 1, "shipped default must CHECK the grandfathered dead cite"

        vml.HERITAGE_PIN_EXEMPTION = True
        try:
            assert vml.main(argv) == 0, "with the exemption ON the same cite is skipped"
        finally:
            vml.HERITAGE_PIN_EXEMPTION = False

        # And the flag still works as an override in the one direction it has.
        assert vml.main(argv + ["--no-heritage-pin-exemption"]) == 1


def test_heritage_flip_preview_equals_the_actual_flip() -> None:
    """The printed cost of the flip is the SAME arithmetic as the flip.

    A preview that is computed a second way is a second implementation, and it
    drifts. Both arms call `_cite_verdict`, so the preview counted with the
    exemption ON must equal the deltas measured with it OFF — on any corpus.
    """
    vml = _load_module()
    _, _, on_stats = _scan_pincheck(vml, heritage=True)
    _, _, off_stats = _scan_pincheck(vml, heritage=False)

    assert on_stats["heritage_flip_dead"] == off_stats["dead"] - on_stats["dead"], (
        on_stats,
        off_stats,
    )
    assert on_stats["heritage_flip_blank"] == off_stats["blank"] - on_stats["blank"]
    assert off_stats["checked"] - on_stats["checked"] == on_stats["exempt_heritage"]
    # The fixture's one heritage cite is dead, so the preview is non-trivially
    # exercised rather than passing on a pair of zeroes.
    assert on_stats["heritage_flip_dead"] == 1, on_stats
    assert on_stats["heritage_flip_dead_gating"] == 1, on_stats


def test_pin_marker_grammar_unit_both_directions() -> None:
    """Unit-level both-directions on the marker grammar itself."""
    vml = _load_module()
    by_written = _pin_cites(vml)

    assert by_written["target.md:900 pin:`aaaaaaa1`"].pin_wellformed is True
    assert by_written["target.md:903 pin:`zzz`"].pin_wellformed is False  # not hex
    assert by_written["target.md:904 pin:`12`"].pin_wellformed is False  # too short
    assert by_written["target.md:909 pin:aaaaaaa1"].pin_wellformed is False  # unbackticked
    # A cite with no marker is not "malformed", it simply has none.
    assert by_written["target.md:907"].pin is None
    assert by_written["target.md:907"].pin_wellformed is False
    # A malformed marker still parses as a cite (path + line survive), which is
    # what makes it checkable rather than silently invisible.
    assert by_written["target.md:903 pin:`zzz`"].path == "target.md"
    assert by_written["target.md:903 pin:`zzz`"].start == 903
    # Uppercase hex is not the token.
    assert not vml._PIN_SHA_RE.match("AAAAAAA1")
    assert vml._PIN_SHA_RE.match("a" * 40) and not vml._PIN_SHA_RE.match("a" * 41)


def test_marker_regex_does_not_match_inside_another_word() -> None:
    """`` spin:`...` `` is not a pin marker, and "spin" is everywhere here.

    An unguarded `pin:` matches inside `spin:`, `unpin:`, `repin:`. Guarding it
    is one lookbehind; not guarding it turns a physics word into a gating
    finding on any row that also carries a cite.
    """
    vml = _load_module()
    for decoy in ("spin", "unpin", "repin", "Xpin", "a_pin"):
        line = f"the {decoy}:`aaaaaaa1` of it, per `some/leaf.md:12`"
        assert not list(vml.iter_orphan_pins(line)), decoy
        assert vml._PIN_ANYWHERE_RE.search(line) is None, decoy
    # ... and the bare token on the same shape still IS one.
    real = "the pin:`aaaaaaa1` of it, per `some/leaf.md:12`"
    assert [n for n, _ in vml.iter_orphan_pins(real)] == [1], real
    # A marker bound to its cite is not an orphan, on the same line shape.
    bound = "per `some/leaf.md:12` pin:`aaaaaaa1` of it"
    assert not list(vml.iter_orphan_pins(bound)), bound


def test_strip_target_has_no_pin_arm() -> None:
    """The marker lives OUTSIDE the link, so the link pass never meets one.

    This is the cross-pass property: `[t](leaf.md:42) pin:`sha`` gives the link
    pass exactly the target it always saw, so the two passes cannot disagree
    about one token — and a filename that legitimately contains `@` is not
    mangled on its way through.
    """
    vml = _load_module()
    assert vml.strip_target("a/b.md:42") == "a/b.md"
    assert vml.strip_target("a/b.md#anchor") == "a/b.md"
    assert vml.strip_target("a/mail@host.md:9") == "a/mail@host.md"
    assert vml.strip_target("a/b.md") == "a/b.md"


# --- the object-store arm: does the pin resolve AT ITS OWN SHA? -------------


def _git(repo, *args):
    import subprocess

    return subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True, check=True
    ).stdout.strip()


def _build_pin_repo(root):
    """A two-commit repo: `doc.md` is 30 lines at c1, 5 lines at c2 (HEAD)."""
    import subprocess

    root.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "-C", str(root), "init", "-q", "-b", "main"], check=True)
    _git(root, "config", "user.email", "fixture@example.invalid")
    _git(root, "config", "user.name", "fixture")
    nested = root / "deep" / "dir"
    nested.mkdir(parents=True)
    (nested / "doc.md").write_text("\n".join(f"line {i}" for i in range(1, 31)) + "\n")
    _git(root, "add", "-A")
    _git(root, "commit", "-qm", "thirty lines")
    first = _git(root, "rev-parse", "HEAD")
    (nested / "doc.md").write_text("\n".join(f"line {i}" for i in range(1, 6)) + "\n")
    _git(root, "add", "-A")
    _git(root, "commit", "-qm", "truncated to five")
    return first, _git(root, "rev-parse", "HEAD")


def test_pin_resolution_both_directions() -> None:
    """★ DEFECT (2). A pin is honoured only when its own claim is TRUE.

    Before this arm the marker was an opt-out by assertion: `dead.md:99999`
    plus ANY real short SHA exited 0. Now the cited path AND line must exist at
    the pinned commit.
    """
    vml = _load_module()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "repo"
        first, head = _build_pin_repo(root)
        store = vml.PinStore(root)
        assert store.enabled and not store.incomplete

        # TRUE: line 25 existed at the first commit (30 lines), by the direct
        # resolution and by the corpus's bare-basename shorthand alike.
        assert store.verdict(first[:8], "deep/dir/doc.md", 25, "")[0] == vml.PIN_OK
        assert store.verdict(first[:8], "doc.md", 25, "")[0] == vml.PIN_OK
        assert store.verdict(first[:8], "dir/doc.md", 25, "deep")[0] == vml.PIN_OK

        # FALSE, and this is the arm that was missing: the commit is real, and
        # the file was never that long at it.
        assert store.verdict(head[:8], "deep/dir/doc.md", 25, "")[0] == vml.PIN_NO_RESOLVE
        assert store.verdict(first[:8], "deep/dir/doc.md", 9999, "")[0] == vml.PIN_NO_RESOLVE
        # FALSE: no such path at that commit, however real the commit is.
        assert store.verdict(first[:8], "never/existed.md", 1, "")[0] == vml.PIN_NO_RESOLVE

        # FALSE: a well-formed sha that is in no complete checkout.
        assert store.verdict("f" * 12, "deep/dir/doc.md", 1, "")[0] == vml.PIN_NO_SHA


def test_pin_resolution_fails_open_on_a_shallow_clone() -> None:
    """★ THE FAIL-OPEN BOUNDARY. A truncated history must never red-light.

    `make verify` runs this tool, so "the commit is not in MY checkout" must
    not read as "the pin is bad" when the checkout is the incomplete thing.
    Same missing sha, two checkouts, two verdicts — that is the boundary being
    a boundary and not a mood.
    """
    import subprocess

    vml = _load_module()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "repo"
        first, _ = _build_pin_repo(root)
        shallow = Path(tmp) / "shallow"
        subprocess.run(
            ["git", "clone", "-q", "--depth", "1", "--no-local", root.as_uri(), str(shallow)],
            check=True,
            capture_output=True,
        )
        deep_store, shallow_store = vml.PinStore(root), vml.PinStore(shallow)
        assert deep_store.incomplete is False
        assert shallow_store.incomplete is True, "clone --depth 1 must read as incomplete"
        assert first not in _git(shallow, "log", "--format=%H"), "sha must be absent there"

        # COMPLETE checkout, sha absent  -> GATING.
        assert deep_store.verdict("f" * 12, "deep/dir/doc.md", 1, "")[0] == vml.PIN_NO_SHA
        # INCOMPLETE checkout, sha absent -> honoured, never a manufactured fail.
        assert shallow_store.verdict(first, "deep/dir/doc.md", 25, "")[0] == vml.PIN_UNVERIFIED
        # ... but a sha the shallow clone DOES have is still judged on merit.
        head = _git(shallow, "rev-parse", "HEAD")
        assert shallow_store.verdict(head, "deep/dir/doc.md", 3, "")[0] == vml.PIN_OK
        assert shallow_store.verdict(head, "deep/dir/doc.md", 25, "")[0] == vml.PIN_NO_RESOLVE


def test_pin_validation_disabled_when_there_is_no_store() -> None:
    """No object store at all -> every marker honoured, nothing manufactured."""
    vml = _load_module()
    with tempfile.TemporaryDirectory() as tmp:
        store = vml.PinStore(Path(tmp))
        assert store.enabled is False
        assert store.verdict("a" * 8, "anything.md", 1, "")[0] == vml.PIN_UNVERIFIED
    # And the switch honours --no-pin-sha-check the same way.
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "repo"
        _build_pin_repo(root)
        assert vml.PinStore(root, enabled=False).enabled is False


def test_pin_resolution_end_to_end_through_the_gate() -> None:
    """The verdicts reach the exit code: a false pin GATES, a true pin does not.

    Driven through `scan` over a real repo whose KB tree cites its own history,
    so the finding, its gating status and the marker's effect are all observed
    together rather than at the unit boundary.
    """
    vml = _load_module()
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "repo"
        first, _ = _build_pin_repo(root)
        kb = root / "manuscript" / "ave-kb"
        kb.mkdir(parents=True)
        (kb / "leaf.md").write_text(
            "# leaf\n"
            f"true pin: `deep/dir/doc.md:25` pin:`{first[:8]}`\n"
            f"false pin, never that long: `deep/dir/doc.md:9999` pin:`{first[:8]}`\n"
            "unknown sha: `deep/dir/doc.md:25` pin:`ffffff09`\n"
        )
        root = root.resolve()  # macOS /var -> /private/var; is_error_source resolves
        file_index, _ = vml.build_kbleaf_target_index(root)
        findings, stats = vml.scan(
            root,
            check_ids_enabled=False,
            file_index=file_index,
            pin_store=vml.PinStore(root),
        )
        by_kind = {}
        for f in findings:
            by_kind.setdefault(f.kind, []).append(f.target)

        assert by_kind.get("pin does not resolve at its own sha") == [
            f"deep/dir/doc.md:9999 pin:`{first[:8]}`"
        ], by_kind
        assert by_kind.get("unknown pin sha") == [
            "deep/dir/doc.md:25 pin:`ffffff09`"
        ], by_kind
        # The true pin is exempt and reported nowhere.
        assert stats["exempt_marker"] == 1, stats
        assert stats["pin_unresolved"] == 1 and stats["pin_unknown_sha"] == 1, stats
        # Both rejections gate — a KB leaf is an error source.
        rejected = [f for f in findings if f.kind in vml._PIN_MARKER_KINDS]
        assert len(rejected) == 2 and all(vml.is_gating(f, root) for f in rejected)

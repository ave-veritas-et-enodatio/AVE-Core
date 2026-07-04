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
    print("OK: all self-tests passed")

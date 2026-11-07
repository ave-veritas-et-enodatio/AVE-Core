"""Regression tests for manuscript/ave-kb/tools/verify-inbound-cite-shift.py.

Guards the 2026-09-19 ADDRESSING RULE. Before it, the checker collected candidate
citers by basename and then tested every cite against EVERY changed file sharing
that basename -- the path the author wrote was never read. Measured instance: a
13-line insertion into `manuscript/vol_1_foundations/main.tex` reported SHIFTED=4;
one citer spelled out `papers/2026_birefringence_letter/main.tex:60`, three were
bare `main.tex:53` in a ledger about the Letter. Nine tracked files are named
`main.tex`, and none of the four cites addressed vol_1's.

Asserts:
  * the tool's own can-it-fire + negative-control gate holds, driven through the
    real scan() against a throwaway two-tree git repo;
  * the mutation receipt holds -- in particular that the negative control is NOT
    vacuous: under the pre-fix basename-only rule the same fixture DOES fire;
  * the pure addressing functions read the path spellings this corpus actually
    uses (full, manuscript-relative, abbreviated, elided, repo-rooted, sibling
    repo, LaTeX-escaped, truncated by a non-ASCII ellipsis) the way the docstring
    says they do;
  * main()'s exit codes: 1 on a pinned shift, 0 on the replayed false positive,
    0 on a changed file that nobody cites (the honest zero the yield-inferred
    liveness control used to call a broken finder), and 2 on each failure the
    control now tests directly -- an unresolvable rev, an erroring `git grep`,
    a dead self-gate;
  * exit 2, never 1, when no verdict was reached (2026-11-07): a crash in any mode,
    a usage error, and a lost citer blob, changed-file blob or subtree -- each of
    which git reports out of band, and each of which the pre-fix tool read as an
    absent file and printed a clean zero. Plus the fix's own edges: an added or
    deleted file, a gitlink, and GIT_TRACE are still not aborts.

Run directly (`python tools/tests/test_verify_inbound_cite_shift.py`) or via pytest.
"""

import importlib.util
import re
import subprocess
import sys
from pathlib import Path

_TOOL = Path(__file__).resolve().parent.parent / "verify-inbound-cite-shift.py"

#: The nine tracked `main.tex` files of the measured instance.
_MAINS = sorted(
    ["manuscript/vol_%s/main.tex" % v for v in (
        "0_engineering_compendium", "1_foundations", "2_subatomic", "3_macroscopic",
        "4_engineering", "5_biology", "6_periodic_table", "9_vacuum_datasheet")]
    + ["papers/2026_birefringence_letter/main.tex"]
)
_VOL1 = "manuscript/vol_1_foundations/main.tex"
_LETTER = "papers/2026_birefringence_letter/main.tex"


def _load_module():
    spec = importlib.util.spec_from_file_location("verify_inbound_cite_shift", _TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _candidates(mod, text, same=_MAINS):
    comps, anchored, sibling = mod.cite_comps(text)
    return mod.path_candidates(comps, anchored, sibling, same)


# ------------------------------------------------------------ the fixture gate

def test_gate_can_fire_and_negative_controls_hold():
    mod = _load_module()
    lines = []
    assert mod.run_gate(out=lines.append), "\n".join(lines)
    assert any("can-it-fire" in l for l in lines)
    assert any("negative control" in l for l in lines)
    assert all("[PASS]" in l for l in lines), "\n".join(lines)


def test_mutation_receipt_holds():
    mod = _load_module()
    assert mod.mutation_receipt() == 0
    assert not mod.MUTATE, "a mutation leaked out of the receipt"


def test_explicit_path_to_sibling_does_not_fire_but_a_real_shift_does():
    """The two fixtures the fix exists for, asserted directly rather than via the gate."""
    mod = _load_module()
    pinned, amb, rc, res = mod.fixture_scan(mod.ALL, moved=[mod.B])
    assert "explicit-A" not in pinned and "explicit-A" not in amb      # cite to A, B moved
    assert pinned.get("explicit-B") == "SHIFTED" and rc == 1           # cite to B, B moved
    assert amb.get("bare-ambiguous") == "SHIFTED"                      # advisory, not gating
    assert "bare-ambiguous" not in pinned
    assert res["found"] > res["tested"] > 0 and res["elsewhere"] > 0


def test_pre_fix_rule_reproduces_the_false_positive():
    mod = _load_module()
    mod.MUTATE.add("basename-only")
    try:
        pinned, _, rc, _ = mod.fixture_scan(["explicit-A"], moved=[mod.B])
    finally:
        mod.MUTATE.discard("basename-only")
    assert pinned.get("explicit-A") == "SHIFTED" and rc == 1
    pinned, amb, rc, _ = mod.fixture_scan(["explicit-A"], moved=[mod.B])
    assert not pinned and not amb and rc == 0


# ------------------------------------------------ liveness + main()'s exit codes
#
# Until 2026-09-19 liveness was INFERRED from yield ("changed files but zero cites
# resolved => the finder is broken"), which exited 2 on 15 of the 30 most recent
# merges into main -- every one a branch whose changed files were un-cited or
# newly added. It is now a fixed positive control proven before the scan.

def _main_rc(mod, keys, moved, base=None, repo_cls=None):
    with mod.fixture_repo(keys, moved) as (repo, b, t):
        if repo_cls is not None:
            repo = repo_cls(cwd=repo.cwd, scrub_env=True)
        return mod.main(base or b, t, repo=repo)


def test_main_exit_1_on_a_pinned_shift():
    mod = _load_module()
    assert _main_rc(mod, mod.ALL, [mod.B]) == 1


def test_main_exit_0_on_the_replayed_false_positive():
    mod = _load_module()
    assert _main_rc(mod, ["explicit-A", "bare-ambiguous"], [mod.B]) == 0


def test_main_exit_0_when_nobody_cites_the_changed_file():
    """The honest zero. The pre-fix control called this "the FINDER is broken"."""
    mod = _load_module()
    assert _main_rc(mod, [], [mod.UNIQUE]) == 0


def test_main_exit_2_on_a_rev_that_does_not_resolve():
    mod = _load_module()
    assert _main_rc(mod, mod.ALL, [mod.B], base="no-such-rev") == 2


def test_main_exit_2_when_git_grep_errors():
    mod = _load_module()

    class GrepFails(mod.Repo):
        def raw(self, *a, stdin=None):
            if a and a[0] == "grep":
                return 128, b""
            return super().raw(*a, stdin=stdin)

    # without the return-code check this reads as a clean zero
    assert _main_rc(mod, mod.ALL, [mod.B], repo_cls=GrepFails) == 2


def test_main_exit_2_when_the_gate_is_dead():
    mod = _load_module()
    mod.MUTATE.add("address-nothing")
    try:
        assert _main_rc(mod, mod.ALL, [mod.B]) == 2
    finally:
        mod.MUTATE.discard("address-nothing")


def test_main_exit_2_names_the_environment_when_the_fixture_cannot_be_built():
    """The gate runs on every invocation, so a git that will not `init` must not be
    reported as "this build cannot fire" -- still exit 2, but with the true cause."""
    import contextlib
    import io

    mod = _load_module()
    real = mod.Repo.raw

    def no_init(self, *a, stdin=None):
        if a and a[0] == "init":
            self.err = "fatal: cannot mkdir: Read-only file system"
            return 128, b""
        return real(self, *a, stdin=stdin)

    buf = io.StringIO()
    mod.Repo.raw = no_init
    try:
        with contextlib.redirect_stdout(buf):
            rc = mod.main("HEAD", "HEAD", repo=mod.Repo())
    finally:
        mod.Repo.raw = real
    assert rc == 2
    assert "could not be BUILT" in buf.getvalue() and "Read-only file system" in buf.getvalue()
    assert "cannot fire" not in buf.getvalue()


# ------------------------------------- exit 2, never 1, when no verdict was reached
#
# Exit 1 is the verdict "a pinned cite moved". Until 2026-11-07 two routes reached it
# without any verdict: an uncaught exception (Python exits 1 on a traceback) and an
# object git could not read, which every call read as an empty answer -- a citer
# never found, a changed file skipped, "no changed files" -- and the run printed a
# clean zero. Each test below fails at f88f49e9.

def _git_free_env(**extra):
    """os.environ minus GIT_*: a hook exporting GIT_DIR must not aim a test at the real repo."""
    import os
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update(extra)
    return env


def _lose(repo, rev, path):
    """Delete the object `rev:path` names (blob or subtree) after the tree is written,
    as the solidity ratchet's `unreadable-base` fixture does. Independent of the tool's
    own fixture `lose=` so these tests fail on the pre-fix tool for the right reason."""
    import os
    oid = repo.sh("rev-parse", "%s:%s" % (rev, path)).strip()
    os.remove(os.path.join(repo.cwd, ".git", "objects", oid[:2], oid[2:]))


def _main_out(mod, keys, moved, lose=()):
    import contextlib
    import io

    buf = io.StringIO()
    with mod.fixture_repo(keys, moved) as (repo, b, t):
        for side, path in lose:
            _lose(repo, b if side == "base" else t, path)
        with contextlib.redirect_stdout(buf):
            rc = mod.main(b, t, repo=repo)
    return rc, buf.getvalue()


def test_main_exit_2_on_a_crash_inside_scan():
    mod = _load_module()
    real = mod.scan

    def crash(*a, **k):
        raise RuntimeError("forced crash inside scan()")

    mod.scan = crash
    try:
        rc, out = _main_out(mod, mod.ALL, [mod.B])
    finally:
        mod.scan = real
    assert rc == 2
    assert "the gate crashed (RuntimeError: forced crash inside scan())" in out


def test_cli_exit_2_on_a_crash():
    """The process exit code, through the tool's own __main__: the real repo's `git diff`
    raises (fixtures run with a tmp cwd, the real run with cwd=None)."""
    driver = (
        "import runpy, subprocess, sys\n"
        "real = subprocess.run\n"
        "def fake(args, *a, **kw):\n"
        "    if kw.get('cwd') is None and args[1:2] == ('diff',):\n"
        "        raise RuntimeError('forced crash inside scan()')\n"
        "    return real(args, *a, **kw)\n"
        "subprocess.run = fake\n"
        "sys.argv = sys.argv[1:]\n"
        "runpy.run_path(sys.argv[0], run_name='__main__')\n"
    )
    mod = _load_module()
    with mod.fixture_repo(["explicit-B"], [mod.B]) as (repo, b, t):
        r = subprocess.run([sys.executable, "-c", driver, str(_TOOL), b, t], capture_output=True,
                           text=True, cwd=repo.cwd, env=_git_free_env())
    assert r.returncode == 2, r.stdout + r.stderr
    assert "the gate crashed (RuntimeError" in r.stdout


def test_cli_usage_exits_2():
    """An empty `$(git merge-base ...)` in the Makefile leaves ONE argument."""
    r = subprocess.run([sys.executable, str(_TOOL), "HEAD"], capture_output=True, text=True)
    assert r.returncode == 2, r.stdout + r.stderr
    assert "usage:" in r.stderr


def test_selftest_and_receipt_exit_2_when_the_fixture_cannot_be_built():
    """Exit 1 from these modes means "the gate is broken"; an environment that cannot
    build the throwaway repo has proved nothing about the gate either way."""
    mod = _load_module()
    real = mod.Repo.raw

    def no_init(self, *a, stdin=None):
        if a and a[0] == "init":
            self.err = "fatal: cannot mkdir: Read-only file system"
            return 128, b""
        return real(self, *a, stdin=stdin)

    mod.Repo.raw = no_init
    try:
        assert mod.selftest() == 2
        assert mod.mutation_receipt() == 2
    finally:
        mod.Repo.raw = real
    assert not mod.MUTATE, "a mutation leaked out of the receipt"


def test_main_exit_2_when_a_citer_blob_cannot_be_read():
    """git grep reports the lost blob only on stderr and exits 1 ("no match")."""
    mod = _load_module()
    assert _main_out(mod, ["explicit-B"], [mod.B])[0] == 1          # the control: it fires
    rc, out = _main_out(mod, ["explicit-B"], [mod.B], lose=[("tip", mod.CITERS)])
    assert rc == 2, out
    assert "unable to read" in out and "clean —" not in out


def test_main_exit_2_when_a_changed_files_blob_cannot_be_read():
    """`cat-file --batch` answers `missing` for it, exactly as for a path not in the tree."""
    mod = _load_module()
    rc, out = _main_out(mod, ["explicit-B"], [mod.B], lose=[("base", mod.B)])
    assert rc == 2, out
    assert "is a blob in that tree" in out and mod.B in out and "clean —" not in out


def test_main_exit_2_when_a_subtree_cannot_be_read():
    """`git diff` exits 128 with an empty stdout -- read naively, "no changed files"."""
    mod = _load_module()
    rc, out = _main_out(mod, ["explicit-B"], [mod.B], lose=[("tip", "manuscript")])
    assert rc == 2, out
    assert "exited 128" in out and "no changed files" not in out


# The fix must not turn ordinary absence into an abort. These pass on the pre-fix tool
# too; they guard the fix's own edges.

def _two_trees(base_files, tip_files, gitlinks=None):
    """A throwaway repo with the given trees; gitlinks = {path: (base oid, tip oid)}."""
    import contextlib

    mod = _load_module()

    @contextlib.contextmanager
    def ctx():
        with mod.fixture_repo([], []) as (repo, _, _t):
            trees = []
            for k, files in enumerate((base_files, tip_files)):
                tree = mod._write_tree(repo, repo.cwd, files)
                if gitlinks:
                    for path, oids in gitlinks.items():
                        repo.raw("update-index", "--add", "--cacheinfo", "160000,%s,%s" % (oids[k], path))
                    tree = repo.sh("write-tree").strip()
                trees.append(tree)
            yield mod, repo, trees[0], trees[1]
    return ctx()


def test_a_file_the_tree_does_not_hold_is_absent_not_unreadable():
    """Added and deleted files answer `missing` from cat-file -- and are really absent."""
    old = ["old %d" % i for i in range(1, 9)]
    base = {"docs/gone.md": old, "a/same.md": old, "docs/cites.md": ["see `gone.md:3` and `same.md:2`"]}
    tip = {"a/same.md": ["new"] + old, "b/same.md": old, "docs/cites.md": base["docs/cites.md"]}
    with _two_trees(base, tip) as (mod, repo, b, t):
        res = mod.scan(repo, b, t)
        assert mod.main(b, t, repo=repo) == 0
    assert not res["grep_errors"]
    # gone.md has no tip and b/same.md no base: neither is "found"; a/same.md is, and the
    # bare name it shares with the added b/same.md makes it advisory
    assert res["found"] == 1 and [f.target for f in res["ambiguous"]] == ["a/same.md"]


def test_a_gitlink_is_absent_not_unreadable():
    """A submodule pointer is `commit` in the tree; its object is never in this repo."""
    one, two = "1" * 40, "2" * 40
    files = {"docs/cites.md": ["the pin is at `vendor/sub:3`"]}
    with _two_trees(files, files, gitlinks={"vendor/sub": (one, two)}) as (mod, repo, b, t):
        assert "vendor/sub" in repo.sh("diff", "--name-only", b, t)
        assert mod.main(b, t, repo=repo) == 0


def test_git_trace_does_not_abort_a_real_run():
    """GIT_TRACE writes to stderr, now read as a grep error: the real run scrubs it."""
    import os

    mod = _load_module()
    saved = dict(os.environ)
    with mod.fixture_repo(["explicit-B"], [mod.B]) as (fixture, b, t):
        try:
            os.environ.clear()
            os.environ.update(_git_free_env(GIT_TRACE="1"))
            repo = mod.Repo(cwd=fixture.cwd)                   # the real-run constructor
        finally:
            os.environ.clear()
            os.environ.update(saved)
        assert "GIT_TRACE" not in (repo.env or {})
        assert mod.main(b, t, repo=repo) == 1


def test_report_names_the_rule_behind_every_verdict():
    """A disputed report has to be arguable: each one says which rule produced it."""
    import contextlib
    import io

    mod = _load_module()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = _main_rc(mod, ["explicit-B", "abbreviated-B", "bare-ambiguous"], [mod.B])
    out = buf.getvalue()
    assert rc == 1
    assert "liveness OK" in out
    assert out.count("[SHIFTED]") == 2
    assert "pinned by: path" in out and "pinned by: abbreviated path" in out
    assert "[AMBIGUOUS-BASENAME, 3 candidates after: bare basename]" in out
    assert "it could equally mean: " + mod.THIRD in out


def test_cli_selftest_exit_code():
    r = subprocess.run([sys.executable, str(_TOOL), "--selftest"], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "SELF-TEST OK" in r.stdout


# ------------------------------------------------- the pure addressing functions

def test_explicit_path_is_a_component_suffix_of_exactly_one_file():
    mod = _load_module()
    assert _candidates(mod, _LETTER) == ([_LETTER], "path")
    assert _VOL1 not in _candidates(mod, _LETTER)[0]


def test_leading_manuscript_dir_is_optional():
    mod = _load_module()
    assert _candidates(mod, "vol_1_foundations/main.tex") == ([_VOL1], "path")
    assert _candidates(mod, "manuscript/vol_1_foundations/main.tex") == ([_VOL1], "path")
    assert _candidates(mod, "../../manuscript/vol_1_foundations/main.tex") == ([_VOL1], "path")


def test_component_suffix_not_string_suffix():
    mod = _load_module()
    same = ["a/vol_1_foundations/main.tex", "a/xvol_1_foundations/main.tex"]
    assert _candidates(mod, "vol_1_foundations/main.tex", same)[0] == ["a/vol_1_foundations/main.tex"]


def test_abbreviation_only_when_no_strict_match():
    mod = _load_module()
    assert _candidates(mod, "vol_1/main.tex") == ([_VOL1], "abbreviated path")
    assert _candidates(mod, "papers/.../main.tex") == ([_LETTER], "abbreviated path")
    assert _candidates(mod, "vol_9.../main.tex") == (
        ["manuscript/vol_9_vacuum_datasheet/main.tex"], "abbreviated path")
    # `vol_1` is a word-boundary prefix: it must not reach a hypothetical vol_10
    same = ["manuscript/vol_10_later/main.tex", _VOL1]
    assert _candidates(mod, "vol_1/main.tex", same)[0] == [_VOL1]
    # gaps are allowed: the chapters/ directory is routinely dropped
    chap = ["manuscript/vol_1_foundations/chapters/02_macroscopic_moduli.tex"]
    assert _candidates(mod, "vol_1/02_macroscopic_moduli.tex", chap) == (chap, "abbreviated path")


def test_unmatched_path_falls_back_to_the_basename():
    mod = _load_module()
    cands, how = _candidates(mod, "manuscript/vol_1_quantum/main.tex")     # a renamed directory
    assert how == "unmatched path" and cands == _MAINS
    only = ["manuscript/vol_2_subatomic/chapters/02_baryon_sector.tex"]
    assert _candidates(mod, "manuscript/vol_2_quantum/chapters/02_baryon_sector.tex", only) == (
        only, "unmatched path")


def test_repo_roots():
    mod = _load_module()
    assert _candidates(mod, "AVE-Core/manuscript/vol_1_foundations/main.tex") == ([_VOL1], "repo-root path")
    assert _candidates(mod, "AVE-HOPF/manuscript/vol_1_foundations/main.tex") == ([], "sibling repo")
    assert _candidates(mod, "Applied-Vacuum-Engineering/src/main.tex") == ([], "sibling repo")
    # rooted at THIS repo means exactly that path, not any file ending in it
    same = ["CLAUDE.md", "manuscript/ave-kb/CLAUDE.md"]
    assert _candidates(mod, "AVE-Core/CLAUDE.md", same) == (["CLAUDE.md"], "repo-root path")


def test_absolute_path_through_the_umbrella_dir_is_this_repo():
    """`.../AVE-staging/AVE-Core/...`: the umbrella directory's own name matches the
    sibling pattern, so THIS repo's name has to be looked for first. Live instance
    when this was written: research/2026-09-13_vol2-kb-manuscript-sync_INVENTORY.md:1702."""
    mod = _load_module()
    text = "/Users/someone/AVE-staging/AVE-Core/manuscript/vol_1_foundations/main.tex"
    assert _candidates(mod, text) == ([_VOL1], "repo-root path")
    # ...while the same umbrella leading into a DIFFERENT repo is still out of this one
    assert _candidates(mod, "/Users/someone/AVE-staging/AVE-HOPF/manuscript/main.tex") == ([], "sibling repo")


def test_directory_in_this_repo_named_like_a_sibling():
    """`manuscript/ave-kb/tools/tests/fixtures/AVE-Sib/` is tracked here."""
    mod = _load_module()
    same = ["manuscript/ave-kb/tools/tests/fixtures/AVE-Sib/manuscript/doc.tex", "manuscript/other/doc.tex"]
    assert _candidates(mod, "fixtures/AVE-Sib/manuscript/doc.tex", same) == ([same[0]], "path")
    assert _candidates(mod, "AVE-Sib/somewhere/else/doc.tex", same) == ([], "sibling repo")


def test_bare_and_degenerate_spellings_are_bare():
    mod = _load_module()
    for text in ("main.tex", "/main.tex", "./main.tex", "../main.tex", ".../main.tex"):
        assert _candidates(mod, text) == (_MAINS, "bare basename"), text


def test_latex_escaped_underscores():
    mod = _load_module()
    assert _candidates(mod, r"vol\_1\_foundations/main.tex") == ([_VOL1], "path")


def test_name_that_merely_ends_in_the_leaf_is_not_a_cite_of_it():
    mod = _load_module()
    m = re.search(mod.PAT_TMPL % re.escape("main.tex"), "see `domain.tex:5`")
    assert m and mod.cite_comps(m.group(1))[0][-1] != "main.tex"


def test_non_ascii_ellipsis_truncates_to_bare():
    """`papers/…/main.tex:488`: the capture class is ASCII, so the text read is `/main.tex`."""
    mod = _load_module()
    m = re.search(mod.PAT_TMPL % re.escape("main.tex"), "| `papers/…/main.tex:488` |")
    assert m and m.group(1) == "/main.tex"
    assert _candidates(mod, m.group(1)) == (_MAINS, "bare basename")


if __name__ == "__main__":
    failed = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print("PASS", name)
            except AssertionError as exc:
                failed += 1
                print("FAIL", name, exc)
    sys.exit(1 if failed else 0)

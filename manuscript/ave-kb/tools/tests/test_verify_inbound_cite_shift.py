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
    a usage error, and a citer blob, changed-file blob or subtree git cannot read
    (deleted, or cut short mid-stream) -- each reported out of band, each read by
    the pre-fix tool as an absent or shorter file, ending in a clean zero; and a
    run from a subdirectory, which read only that subtree. Plus the fix's own
    edges: an added or deleted file, a gitlink, and git tracing from env or config
    are still not aborts;
  * a file has exactly the lines `git grep -n` numbers (2026-11-08): no phantom line
    N+1 after a final newline, so a cite past the last line was never valid at base,
    and has-line narrowing drops a file one line too short.

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
    # the damaged-object probes are part of every run's liveness: pin them, so that
    # dropping one (or the loop) is a test failure and not a quieter self-gate
    damaged = ["citer blob (the only match)", "citer blob (beside a match)",
               "changed-file blob (deleted)", "changed-file blob (cut short)", "subtree (deleted)"]
    for name in damaged:
        assert any(l.lstrip().startswith("[PASS] a damaged %s aborts" % name) for l in lines), name
    assert len(lines) == 10 + len(damaged)
    assert sorted(mod.LOST) == sorted(damaged)


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


def _damage(repo, rev, path, how="delete"):
    """Delete the object `rev:path` names (blob or subtree), or cut its loose file to half,
    after the tree is written -- as the solidity ratchet's `unreadable-base` fixture does.
    Independent of the tool's own fixture `damage=`, so these tests fail on the pre-fix
    tool for the behavioural reason, not on a missing helper."""
    import os
    oid = repo.sh("rev-parse", "%s:%s" % (rev, path)).strip()
    loose = os.path.join(repo.cwd, ".git", "objects", oid[:2], oid[2:])
    if how == "delete":
        os.remove(loose)
        return
    with open(loose, "rb") as fh:
        data = fh.read()
    os.chmod(loose, 0o644)
    with open(loose, "wb") as fh:
        fh.write(data[:len(data) // 2])


def _main_out(mod, keys, moved, damage=()):
    import contextlib
    import io

    buf = io.StringIO()
    with mod.fixture_repo(keys, moved) as (repo, b, t):
        for side, path, how in damage:
            _damage(repo, b if side == "base" else t, path, how)
        with contextlib.redirect_stdout(buf):
            rc = mod.main(b, t, repo=repo)
    return rc, buf.getvalue()


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


def test_main_exit_2_on_a_crash_inside_scan():
    """A ValueError -- the type the colour-config crash raises -- in the REAL scan; the
    self-gate's fixture scans run untouched first."""
    import contextlib
    import io

    mod = _load_module()
    real = mod.scan
    with mod.fixture_repo(["explicit-B"], [mod.B]) as (repo, b, t):
        def crash(r, *a, **k):
            if r is repo:
                raise ValueError("forced crash inside scan()")
            return real(r, *a, **k)

        buf = io.StringIO()
        mod.scan = crash
        try:
            with contextlib.redirect_stdout(buf):
                rc = mod.main(b, t, repo=repo)
        finally:
            mod.scan = real
    assert rc == 2, buf.getvalue()
    assert "the gate crashed (ValueError: forced crash inside scan())" in buf.getvalue()


def test_cli_exit_2_on_a_crash():
    """The process exit code, through the tool's own __main__: `git diff` raises in the
    repo under test only (the self-gate's fixtures are other directories)."""
    driver = (
        "import os, runpy, subprocess, sys\n"
        "real = subprocess.run\n"
        "target = os.path.realpath(os.environ['CRASH_IN'])\n"
        "def fake(args, *a, **kw):\n"
        "    if args[1:2] == ('diff',) and os.path.realpath(kw.get('cwd') or '') == target:\n"
        "        raise ValueError('forced crash inside scan()')\n"
        "    return real(args, *a, **kw)\n"
        "subprocess.run = fake\n"
        "sys.argv = sys.argv[1:]\n"
        "runpy.run_path(sys.argv[0], run_name='__main__')\n"
    )
    mod = _load_module()
    with _two_trees({"docs/c.md": ["x"]}, {"docs/c.md": ["y"]}) as (_, repo, b, t):
        r = subprocess.run([sys.executable, "-c", driver, str(_TOOL), b, t], capture_output=True,
                           text=True, cwd=repo.cwd, env=_git_free_env(CRASH_IN=repo.cwd))
    assert r.returncode == 2, r.stdout + r.stderr
    assert "the gate crashed (ValueError" in r.stdout


def test_cli_usage_exits_2():
    """An empty `$(git merge-base ...)` in the Makefile leaves ONE argument."""
    r = subprocess.run([sys.executable, str(_TOOL), "HEAD"], capture_output=True, text=True)
    assert r.returncode == 2, r.stdout + r.stderr
    assert "usage:" in r.stderr


def test_cli_from_a_subdirectory_reads_the_whole_repo():
    """From a subdirectory git grep searches only that subtree: the pre-fix run, started
    in docs/, found the shifted cite's citer nowhere and exited 0."""
    mod = _load_module()
    with mod.fixture_repo(["explicit-B"], [mod.B]) as (repo, b, t):
        rcs = [subprocess.run([sys.executable, str(_TOOL), b, t], capture_output=True, text=True,
                              cwd=cwd, env=_git_free_env()).returncode
               for cwd in (repo.cwd, repo.cwd + "/manuscript")]
    assert rcs == [1, 1], rcs


def test_cli_without_a_work_tree_and_with_odd_paths():
    """Moving to the top level is for a work tree only. A bare repo and a cwd inside .git/
    have no subtree to miss and no top level to move to; a relative GIT_DIR/GIT_WORK_TREE
    must survive the move; a top level whose name ends in a space must too. Each exits 1,
    like the run at the root."""
    import shutil
    import tempfile

    mod = _load_module()
    env = _git_free_env()

    def rc(cwd, **extra):
        return subprocess.run([sys.executable, str(_TOOL), b, t], capture_output=True, text=True,
                              cwd=cwd, env=dict(env, **extra)).returncode

    scratch = tempfile.mkdtemp(prefix="inbound-cite-odd-")
    try:
        with mod.fixture_repo(["explicit-B"], [mod.B]) as (repo, b, t):
            bare = scratch + "/bare.git"
            subprocess.run(["git", "init", "-q", "--bare", bare], env=env, check=True)
            shutil.rmtree(bare + "/objects")
            shutil.copytree(repo.cwd + "/.git/objects", bare + "/objects")
            spaced = scratch + "/repo "
            shutil.copytree(repo.cwd, spaced, symlinks=True)
            got = {"root": rc(repo.cwd), "bare repo": rc(bare), "cwd inside .git": rc(repo.cwd + "/.git"),
                   "relative GIT_DIR from docs/": rc(repo.cwd + "/docs", GIT_DIR="../.git", GIT_WORK_TREE=".."),
                   "top level ending in a space": rc(spaced + "/docs")}
    finally:
        shutil.rmtree(scratch, ignore_errors=True)
    assert got == {k: 1 for k in got}, got


def test_cli_outside_a_repo_cannot_start():
    import shutil
    import tempfile

    cwd = tempfile.mkdtemp(prefix="inbound-cite-norepo-")
    try:
        r = subprocess.run([sys.executable, str(_TOOL), "HEAD~1", "HEAD"], capture_output=True,
                           text=True, cwd=cwd, env=_git_free_env(GIT_CEILING_DIRECTORIES=cwd))
    finally:
        shutil.rmtree(cwd, ignore_errors=True)
    assert r.returncode == 2, r.stdout + r.stderr
    assert "cannot start" in r.stdout and "crashed" not in r.stdout


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
    """git grep reports the lost blob only on stderr -- and its exit code says nothing:
    1 ("no match") when the lost file was the only match, 0 beside any other match."""
    mod = _load_module()
    for keys in (["explicit-B"], ["explicit-B", "beside-B-bare"]):
        assert _main_out(mod, keys, [mod.B])[0] == 1                 # the control: it fires
        rc, out = _main_out(mod, keys, [mod.B], damage=[("tip", mod.CITERS, "delete")])
        assert rc == 2, (keys, out)
        assert "unable to read" in out and mod.CITERS in out and "clean —" not in out


def test_main_exit_2_when_a_changed_files_blob_cannot_be_read():
    """`cat-file --batch` answers `missing` for it, exactly as for a path not in the tree."""
    mod = _load_module()
    rc, out = _main_out(mod, ["explicit-B"], [mod.B], damage=[("base", mod.B, "delete")])
    assert rc == 2, out
    assert "is a blob in that tree" in out and mod.B in out and "clean —" not in out


def test_main_exit_2_when_a_changed_files_blob_is_cut_short():
    """A blob big enough to stream: cat-file prints its full-size header, part of the body,
    then exits 128. The pre-fix run kept the part, read the cited line as never valid at
    base, and printed a clean."""
    import contextlib
    import io

    rows = ["row %d of a long table" % i for i in range(1, 301)]
    cite = {"docs/c.md": ["see `big.txt:290`"]}
    for cut in (False, True):
        with _two_trees(dict(cite, **{"big.txt": rows}),
                        dict(cite, **{"big.txt": ["new"] + rows})) as (mod, repo, b, t):
            if cut:
                _damage(repo, b, "big.txt", "truncate")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = mod.main(b, t, repo=repo)
        assert rc == (2 if cut else 1), buf.getvalue()
    assert "clean —" not in buf.getvalue()


def _fake_catfile(mod, rc, reply):
    """A Repo whose `cat-file --batch` answers `reply` with exit `rc`, and whose tree
    lists `f.txt` as a blob."""
    class Fake(mod.Repo):
        def raw(self, *a, stdin=None):
            if a[:1] == ("cat-file",):
                self.err = "fatal: unable to stream" if rc else ""
                return rc, reply
            return 0, b""

        def tree(self, rev):
            return {"f.txt": "blob"}
    return Fake(cwd="/nonexistent")


def test_load_rejects_each_kind_of_short_read_on_its_own():
    """The exit-code check and the body-length check each stand alone: a git that sent
    the whole body and still failed, or exited 0 with the body cut short, is not read."""
    mod = _load_module()
    body = b"line 1\nline 2\n"
    whole = b"%s blob %d\n%s\n" % (b"a" * 40, len(body), body)
    assert _fake_catfile(mod, 0, whole).blob("t", "f.txt") == ["line 1", "line 2"]   # control
    for rc, reply in ((128, whole), (0, whole[:-6]), (0, whole[:whole.index(b"\n") + 1])):
        try:
            got = _fake_catfile(mod, rc, reply).blob("t", "f.txt")
        except mod.GateError:
            continue
        raise AssertionError("rc=%d reply=%r was read as %r" % (rc, reply, got))


def test_an_abort_that_does_not_name_the_damaged_object_proves_nothing():
    """The self-gate's damaged-object probes count an abort only when it names the
    damaged `<tree>:<path>` or object id. Not the bare path: `manuscript` (the subtree
    probe) is a substring of every fixture file beneath it."""
    mod = _load_module()
    real = mod.scan

    def unrelated(*a, **k):
        raise mod.GateError("an unrelated fault while reading manuscript/vol_2_subatomic/main.tex")

    mod.scan = unrelated
    try:
        got = {name: mod.lost_object_verdict(name) for name in mod.LOST}
    finally:
        mod.scan = real
    assert all(v.startswith("ABORT, but not naming it") for v in got.values()), got


def test_main_exit_2_when_a_subtree_cannot_be_read():
    """`git diff` exits 128 with an empty stdout -- read naively, "no changed files"."""
    mod = _load_module()
    rc, out = _main_out(mod, ["explicit-B"], [mod.B], damage=[("tip", "manuscript", "delete")])
    assert rc == 2, out
    assert "exited 128" in out and "no changed files" not in out


# ----------------------------------------- line N+1 of an N-line file (2026-11-08)
#
# split('\n') on a file ending in a newline leaves a '' after the last line, so every
# N-line file "had" a line N+1. A cite to it, dead at base, passed the never-valid-at-
# base test: a tip one line shorter exited 1 on it with empty was/now lines (review A6
# on #1081), a longer tip made it EDITED-IN-PLACE. The same phantom line kept a file
# one line too short alive through has-line narrowing. Each test below fails at ad19aec8.

def _scan_and_exit(base, tip):
    import contextlib
    import io

    with _two_trees(base, tip) as (mod, repo, b, t):
        res = mod.scan(repo, b, t)
        with contextlib.redirect_stdout(io.StringIO()):
            rc = mod.main(b, t, repo=repo)
    return res, rc


def test_a_cite_past_the_last_line_was_never_valid_at_base():
    rows = ["row %d" % i for i in range(1, 15)]                        # 14 lines
    for n, tip_rows, want in (
            (15, rows[1:], []),                                         # the review's repro
            (15, rows + ["row 15, new"], []),                           # the line exists only at tip
            (14, rows + ["row 15, new"], []),                           # control: the last line holds
            (14, rows[1:], [("OUT-OF-RANGE", "row 14", "")]),           # control: ...and can move
            (14, ["new"] + rows, [("SHIFTED", "row 14", "row 13")]),
            (14, rows[:-1], [("OUT-OF-RANGE", "row 14", "")])):         # the last line deleted
                                                                        # (was EDITED-IN-PLACE, exit 0)
        cite = {"docs/c.md": ["see `f.txt:%d`" % n]}
        res, rc = _scan_and_exit(dict(cite, **{"f.txt": rows}), dict(cite, **{"f.txt": tip_rows}))
        got = [(f.kind, f.was, f.now) for f in res["pinned"]]
        assert res["found"] == 1 and got == want and rc == (1 if want else 0), (n, len(tip_rows), got, rc)


def test_has_line_drops_a_file_one_line_too_short():
    """A bare `g.md:15` with a/g.md 14 lines long and b/g.md 40: only b/g.md has line 15."""
    short, long_ = ["short %d" % i for i in range(1, 15)], ["long %d" % i for i in range(1, 41)]
    base = {"docs/c.md": ["see `g.md:15`"], "a/g.md": short, "b/g.md": long_}
    res, rc = _scan_and_exit(base, dict(base, **{"b/g.md": ["inserted"] + long_}))
    assert [(f.target, f.kind, f.how) for f in res["pinned"]] == [
        ("b/g.md", "SHIFTED", "bare basename + has-line")] and not res["ambiguous"] and rc == 1
    res, rc = _scan_and_exit(base, dict(base, **{"a/g.md": short[1:]}))
    assert res["elsewhere"] == 1 and not res["pinned"] and not res["ambiguous"] and rc == 0


def test_line_count_is_git_greps():
    """The lines `load()` returns are the lines `git grep -n` numbers, the numbering every
    citer's `:NNN` was read off: empty file, no final newline, a trailing blank line, CRLF.
    Only `\\n` ends a line for git: a lone `\\r`, VT, FF, NEL and U+2028 do not, though
    `str.splitlines()` splits on each (a tracked file holds a VT today)."""
    mod = _load_module()
    bodies = [b"", b"\n", b"a", b"a\n", b"a\nb", b"a\n\n", b"a\r\nb\r\n",
              b"a\rb\n", b"a\x0bb\n", b"a\x0cb\n", "a\x85b\n".encode(), "a b\n".encode()]
    with mod.fixture_repo([], []) as (repo, _, _t):
        rows = []
        for k, body in enumerate(bodies):
            rc, out = repo.raw("hash-object", "-w", "--stdin", stdin=body)
            assert rc == 0, repo.err
            rows.append("100644 blob %s\tf%d" % (out.decode().strip(), k))
        rc, out = repo.raw("mktree", stdin=("\n".join(rows) + "\n").encode())
        assert rc == 0, repo.err
        tree = out.decode().strip()
        for k, body in enumerate(bodies):
            rc, out = repo.raw("grep", "-c", "-e", "", tree, "--", "f%d" % k)
            assert rc in (0, 1), repo.err
            want = int(out.decode().rsplit(":", 1)[1]) if out.strip() else 0
            got = repo.blob(tree, "f%d" % k)
            assert len(got) == want, (body, got, want)
    assert _fake_catfile(mod, 0, b"%s blob 0\n\n" % (b"a" * 40)).blob("t", "f.txt") == []


# The fix must not turn ordinary absence into an abort. These pass on the pre-fix tool
# too; they guard the fix's own edges.

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


def test_git_tracing_does_not_abort_a_run():
    """Tracing writes to stderr, which is now read as a grep error. GIT_TRACE* is env-only
    and scrubbed; trace2 can come from git CONFIG too -- `~/.gitconfig` reaches the
    self-gate's fixtures as well as the real run -- and is switched off by env."""
    import os
    import tempfile

    mod = _load_module()
    saved = dict(os.environ)
    home = tempfile.mkdtemp(prefix="inbound-cite-home-")
    try:
        with open(os.path.join(home, ".gitconfig"), "w") as fh:
            fh.write("[trace2]\n\tnormalTarget = 2\n\tperfTarget = 2\n")
        with mod.fixture_repo(["explicit-B"], [mod.B]) as (fixture, b, t):
            env = _git_free_env(HOME=home, GIT_TRACE="1", GIT_TRACE2="1", GIT_TRACE_PERFORMANCE="1")
            env.pop("XDG_CONFIG_HOME", None)
            os.environ.clear()                                 # built BEFORE the clear: PATH kept
            os.environ.update(env)
            repo = mod.Repo(cwd=fixture.cwd)                   # the real-run constructor
            assert mod.main(b, t, repo=repo) == 1
    finally:
        os.environ.clear()
        os.environ.update(saved)
        import shutil
        shutil.rmtree(home, ignore_errors=True)


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
            except Exception as exc:          # a crash is a failure too, not the end of the run
                failed += 1
                print("FAIL", name, exc)
    sys.exit(1 if failed else 0)

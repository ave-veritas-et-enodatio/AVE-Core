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
    control now tests directly -- an unresolvable rev, an erroring `git grep` or
    `git diff-tree`, a dead self-gate;
  * exit 2, never 1, when no verdict was reached (2026-11-07): a crash in any mode,
    a usage error, and a citer blob, changed-file blob or subtree git cannot read
    (deleted, or cut short mid-stream) -- each reported out of band, each read by
    the pre-fix tool as an absent or shorter file, ending in a clean zero; and a
    run from a subdirectory, which read only that subtree. Plus the fix's own
    edges: an added or deleted file, a gitlink, and git tracing from env or config
    are still not aborts.

And the 2026-11-01 rules. Re-pinning stale cites on #1037-#1039 showed the checker
could not confirm a repair: it tested base[new] against tip[new], so a correct
re-pin read SHIFTED with a wrong next number and a wrong one read the same. And
`moved_to` took the first identical line in the file, so a `\\begin{itemize}` at
:717 reported :6 when it had gone to :719. Asserts:
  * a correct re-pin passes, a wrong one still fails, a repeated line maps to
    where it went -- directly, through the gate, and through main()'s exit codes;
  * every row of the tool's own REPINS table holds;
  * the pure functions read hunk headers, zero-length sides and line pairing the
    way the docstring says they do.

And their repairs. A diff that gives no address has not agreed; a blank line asks
the diff; either side of a tie passes; has-line reads a re-pin at both numbers; a
pair needs no rival and a line moved whole is nobody's re-pin; a final newline is
not a line. Two things the REPINS table cannot hold are pinned here: a target with a
NUL byte, and rows alike but for their digits pairing in order.

And the line count end to end (2026-11-08). Line N is the Nth line as `git grep -n`
numbers it: `line_count()` of a blob as `load()` reads it is checked against git
itself, including the breaks `str.splitlines()` sees and git does not; a plain cite
past the last line was never valid at base, whichever way the tip moves, and a re-pin
from it keeps the plain test; has-line drops a file one line too short, at the number
a cite held and at the number a re-pin moved it to; and the '' after a final newline
is no neighbour when put-back lines tie at the end of a file, and no landing for a diff
that lies.

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
               "changed-file blob (deleted)", "changed-file blob (cut short)",
               "re-pinning citer blob (deleted)", "subtree (deleted)"]
    for name in damaged:
        assert any(l.lstrip().startswith("[PASS] a damaged %s aborts" % name) for l in lines), name
    assert sum(l.lstrip().startswith("[PASS] a damaged ") for l in lines) == len(damaged)
    # and the whole gate: 10 original probes, one per REPINS row plus #1079's 7 re-pin
    # checks, the damaged objects, and the -U0 context-lines probe -- so dropping ANY
    # probe, from either side of the #1079 merge, fails here (78 at the merge)
    assert len(lines) == 10 + len(mod.REPINS) + 7 + len(damaged) + 1, len(lines)
    assert any(l.lstrip().startswith("[PASS] a `-U0` diff that comes back with context lines") for l in lines)
    assert sorted(mod.LOST) == sorted(damaged)


def test_mutation_receipt_holds():
    import contextlib
    import io

    mod = _load_module()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        assert mod.mutation_receipt() == 0
    assert not mod.MUTATE, "a mutation leaked out of the receipt"
    # Every row present, under its own number. Merging #1079 interleaved #1081's rows
    # into M6-M39 without a conflict marker; a dropped or renumbered row must fail here.
    rows = re.findall(r"\[(OK|BROKEN)\] M(\d+) ", buf.getvalue())
    assert {int(n) for _, n in rows} == set(range(1, 47)), sorted({int(n) for _, n in rows})
    assert all(status == "OK" for status, _ in rows)


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
    assert _fake_catfile(mod, 0, whole).blob("t", "f.txt") == ["line 1", "line 2", ""]   # control
    for rc, reply in ((128, whole), (0, whole[:-6]), (0, whole[:whole.index(b"\n") + 1])):
        try:
            got = _fake_catfile(mod, rc, reply).blob("t", "f.txt")
        except mod.GateError:
            continue
        raise AssertionError("rc=%d reply=%r was read as %r" % (rc, reply, got))


def test_each_damaged_object_fixture_gives_its_verdict_whole():
    """The control under every LOST row, pinned as literals: the fixture must reach this
    verdict with every object present, or the abort it shows when damaged proves
    nothing. The re-pin row's control is a PASS: its false verdict, with the rule off,
    is a false SHIFTED."""
    mod = _load_module()
    want = {"citer blob (the only match)": "exit 1", "citer blob (beside a match)": "exit 1",
            "changed-file blob (deleted)": "exit 1", "changed-file blob (cut short)": "exit 1",
            "re-pinning citer blob (deleted)": "exit 0", "subtree (deleted)": "exit 1"}
    got = {name: mod.lost_object_verdict(name, damaged=False).split(",")[0] for name in mod.LOST}
    assert got == want, got


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


def test_git_diff_opts_does_not_reach_the_real_run():
    """GIT_DIFF_OPTS=--unified=N overrides even plumbing's -U0. Through #1079's re-pin
    check, a hunk widened by context lines let a WRONG re-pin "land on the row that
    replaced it" and the run exited 0. The real run scrubs the variable."""
    import os

    mod = _load_module()
    saved = dict(os.environ)
    with mod.two_trees(*mod._context_trees()) as (fixture, b, t):
        try:
            env = _git_free_env(GIT_DIFF_OPTS="--unified=3")
            os.environ.clear()
            os.environ.update(env)
            repo = mod.Repo(cwd=fixture.cwd)                   # the real-run constructor
        finally:
            os.environ.clear()
            os.environ.update(saved)
        assert "GIT_DIFF_OPTS" not in repo.env
        assert mod.main(b, t, repo=repo) == 1


def test_a_diff_with_context_lines_voids_the_run():
    """The belt behind the scrub: a -U0 diff that comes back with context lines, from
    any source, is a `git diff-tree` error, not a smaller set of changes."""
    mod = _load_module()
    assert mod.diff_context_verdict(inject=False) == "exit 1"         # the wrong re-pin fails
    assert mod.diff_context_verdict() == "ABORT"
    mod.MUTATE.add("diff-context-ok")
    try:
        assert mod.diff_context_verdict() == "exit 0"                   # what the belt prevents
        # ...and an abort for another reason (a stray grep error) is not the belt firing
        real = mod.Repo.raw

        def stray(self, *a, stdin=None):
            rc, out = real(self, *a, stdin=stdin)
            if a[:1] == ("grep",):
                self.err = "error: something unrelated"
            return rc, out

        mod.Repo.raw = stray
        try:
            assert mod.diff_context_verdict().startswith("ABORT, but not on docs/t.md")
        finally:
            mod.Repo.raw = real
    finally:
        mod.MUTATE.discard("diff-context-ok")


def test_the_self_gate_runs_its_object_probes_rather_than_printing_them():
    """A probe's [PASS] line is only worth the probe behind it: if a damaged-object or
    context-lines probe stops aborting, run_gate() must fail, not print the same line."""
    mod = _load_module()
    for name in ("lost_object_verdict", "diff_context_verdict"):
        real = getattr(mod, name)
        setattr(mod, name, lambda *a, **k: "exit 0, cites-found=0")
        try:
            lines = []
            assert not mod.run_gate(out=lines.append), name
            assert any("[FAIL]" in l for l in lines), name
        finally:
            setattr(mod, name, real)


def test_a_file_without_a_final_newline_is_no_context_line():
    """`\\ No newline at end of file` is part of healthy -U0 output; only a line that starts
    with a space is context. A cited last line rewritten in a file with no final newline
    reads EDITED-IN-PLACE (advisory, exit 0), never a diff error."""
    import os

    mod = _load_module()
    with mod.two_trees({}, {}) as (repo, _, _t):
        trees = []
        for last in (b"row 5", b"row 5, rewritten"):
            os.makedirs(os.path.join(repo.cwd, "docs"), exist_ok=True)
            with open(os.path.join(repo.cwd, "docs", "t.md"), "wb") as fh:
                fh.write(b"row 1\nrow 2\nrow 3\nrow 4\n" + last)       # no final newline
            with open(os.path.join(repo.cwd, "docs", "c.md"), "wb") as fh:
                fh.write(b"see `docs/t.md:5`\n")
            repo.raw("add", "-A", "-f", ".")
            trees.append(repo.sh("write-tree").strip())
        b, t = trees
        diff = repo.sh("diff-tree", "-p", "-U0", b, t, "--", "docs/t.md")
        assert "No newline at end of file" in diff                     # the case is real
        res = mod.scan(repo, b, t)
    assert not res["diff_errors"], res["diff_errors"]
    assert not mod.scan_errors(res)
    assert [f.kind for f in res["pinned"]] == ["EDITED-IN-PLACE"]       # advisory: exit 0


def test_main_exit_2_when_git_diff_tree_errors():
    mod = _load_module()

    class DiffFails(mod.Repo):
        def raw(self, *a, stdin=None):
            if "diff-tree" in a:
                return 128, b""
            return super().raw(*a, stdin=stdin)

    # without the return-code check every re-pin quietly loses its base number
    assert _main_rc(mod, mod.ALL, [mod.B], repo_cls=DiffFails) == 2


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


# ------------------------------------------------------- which number, which line

def _repin_rc(mod, keys):
    with mod.two_trees(*mod._repin_trees(keys)) as (repo, base, tip):
        return mod.main(base, tip, repo=repo)


def test_correct_repin_passes():
    """The defect as measured: the citer moved from :old to :new with its target and
    still read SHIFTED, because base[new] was tested instead of base[old]."""
    mod = _load_module()
    got, rc = mod.repin_scan(["correct"])
    assert got == {"correct": [(9, 12, "RE-PINNED", 12)]} and rc == 0


def test_correct_repin_reads_shifted_without_the_rule():
    mod = _load_module()
    mod.MUTATE.add("no-repin")
    try:
        got, rc = mod.repin_scan(["correct"])
    finally:
        mod.MUTATE.discard("no-repin")
    assert got["correct"][0][2] == "SHIFTED" and rc == 1


def test_wrong_repin_still_fails_and_names_the_right_number():
    mod = _load_module()
    got, rc = mod.repin_scan(["wrong"])
    assert got == {"wrong": [(9, 13, "SHIFTED", 12)]} and rc == 1


def test_repin_onto_an_identical_line_still_fails():
    """Equal text is not proof on a repeated line: base[6] and tip[2] are both
    `\\begin{itemize}`, but the diff says the cited one went to :9."""
    mod = _load_module()
    assert mod.repin_scan(["lookalike"])[0] == {"lookalike": [(6, 2, "SHIFTED", 9)]}


def test_repeated_line_maps_to_where_it_went():
    mod = _load_module()
    assert mod.TARGET_BASE[7] == mod.TARGET_TIP[3] == mod.TARGET_TIP[10] == mod.ENDIZE
    assert mod.repin_scan(["repeated"])[0] == {"repeated": [(8, 8, "SHIFTED", 11)]}
    mod.MUTATE.add("first-identical")
    try:
        assert mod.repin_scan(["repeated"])[0] == {"repeated": [(8, 8, "SHIFTED", 4)]}
    finally:
        mod.MUTATE.discard("first-identical")


def test_every_row_of_the_fixture_table():
    mod = _load_module()
    got, rc = mod.repin_scan()
    assert rc == 1
    for key, row in mod.REPINS.items():
        assert got.get(key, []) == row[2], key


def test_only_correct_repins_pass_the_run_and_one_wrong_one_fails_it():
    mod = _load_module()
    assert _repin_rc(mod, ["correct", "prose", "moved", "two", "untouched"]) == 0
    assert _repin_rc(mod, ["correct", "prose", "moved", "two", "untouched", "wrong"]) == 1


def test_report_confirms_a_repin_and_names_both_numbers():
    import contextlib
    import io

    mod = _load_module()
    buf = io.StringIO()
    with mod.two_trees(*mod._repin_trees(["correct", "wrong", "gone"])) as (repo, base, tip):
        with contextlib.redirect_stdout(buf):
            mod.report(mod.scan(repo, base, tip), verbose=True)
    out = buf.getvalue()
    assert "RE-PINNED=1 (confirmed repairs)" in out and "SHIFTED=2 (real rot)" in out
    assert ":12   [RE-PINNED] -- re-pinned from :9, confirmed" in out
    assert ":13   [SHIFTED] -- re-pinned from :9; base content is now at :12" in out
    assert ":5   [UNCONFIRMED-RE-PIN] -- re-pinned from :10; the base content is gone" in out
    assert "RETARGETED=0 (advisory)" in out


def test_report_says_what_a_retarget_is_without_guessing_why():
    import contextlib
    import io

    mod = _load_module()
    buf = io.StringIO()
    with mod.two_trees(*mod._repin_trees(["retargeted"])) as (repo, base, tip):
        with contextlib.redirect_stdout(buf):
            mod.report(mod.scan(repo, base, tip), verbose=True)
    out = buf.getvalue()
    assert "[RETARGETED] -- re-pinned from :1; no repair to confirm: the cited line stayed put and" in out
    assert "on purpose" not in out


def test_retarget_is_advisory_and_a_miss_onto_a_still_line_is_not():
    """#915 moved nothing in `trampoline-framework.md` and corrected `:188` to `:192`,
    a cite wrong at the base: comparing the two lines alone called that rot. But a
    re-pin whose content DID move must fail even when it lands on a still line, where
    the plain test passes it."""
    mod = _load_module()
    assert mod.repin_scan(["retargeted"]) == ({"retargeted": [(1, 3, "RETARGETED", 0)]}, 0)
    assert mod.repin_scan(["missed-onto-still"]) == (
        {"missed-onto-still": [(9, 2, "SHIFTED", 12)]}, 1)


def test_a_repin_from_a_blank_onto_text_has_nothing_to_compare():
    """A blank base line has no text to reach for, so onto a line with text the diff
    is not asked and the cited line is never seen to stay put. That is gone content:
    onto a moved line or a still one alike, nothing confirms it."""
    mod = _load_module()
    base, tip = ["a", "", "c"], ["x", "a", "", "c"]
    repo = _Stub(base, tip, [(1, 0, 1, 1)])
    assert mod.verdict(repo, "B", "T", "t.md", base, tip, 2, 1) == ("UNCONFIRMED-RE-PIN", 0)   # :1 moved
    still = ["a", "", "c", "d"]
    repo = _Stub(still, still, [])
    assert mod.verdict(repo, "B", "T", "t.md", still, still, 2, 3) == ("UNCONFIRMED-RE-PIN", 0)


def test_report_does_not_call_a_blank_cited_line_gone():
    """A blank line can still be there: it is unconfirmable, not gone."""
    mod = _load_module()
    blank = mod.Finding("a.md", 1, "b.md", 3, "UNCONFIRMED-RE-PIN", "", "c", 0, ("b.md",), "path", 2)
    assert "gone" not in mod._arrow(blank) and "blank" in mod._arrow(blank)
    text = blank._replace(was="old text")
    assert "the base content is gone" in mod._arrow(text)


def test_a_repin_of_a_blank_line_onto_a_blank_line_asks_the_diff():
    mod = _load_module()
    base, tip = ["a", "", "b", "", "c"], ["x", "a", "", "b", "", "c"]
    repo = _Stub(base, tip, [(1, 0, 1, 1)])
    assert mod.verdict(repo, "B", "T", "t.md", base, tip, 2, 3) == ("RE-PINNED", 3)
    assert mod.verdict(repo, "B", "T", "t.md", base, tip, 2, 5) == ("SHIFTED", 3)


def test_a_repin_onto_a_look_alike_of_a_deleted_line_fails_with_no_address():
    """The regression: the diff took :5 out, so it gave no address, and that read as
    agreement. main's tool exits 1 here."""
    mod = _load_module()
    base, tip = ["a", "dup", "b", "c", "dup", "d"], ["a", "dup", "b", "c", "d"]
    repo = _Stub(base, tip, [(5, 1, 5, 0)])
    assert mod.verdict(repo, "B", "T", "t.md", base, tip, 5, 2) == ("SHIFTED", 0)


def test_lines_at_tip_keeps_both_sides_of_a_tie_and_the_address_keeps_neither():
    mod = _load_module()
    base, tip = ["p", "same", "q"], ["same", "p", "q", "same"]
    hunks = [(1, 0, 1, 1), (2, 1, 3, 0), (4, 0, 4, 1)]
    assert mod.lines_at_tip(hunks, base, tip, 2) == [1, 4]
    assert mod.address_at_tip(hunks, base, tip, 2) == 0


def test_a_correct_repin_exits_0_and_a_look_alike_exits_1_through_main():
    mod = _load_module()
    assert _repin_rc(mod, ["blank-right", "tie-near", "tie-far"]) == 0
    assert _repin_rc(mod, ["lookalike-gone"]) == 1
    assert _repin_rc(mod, ["blank-wrong"]) == 1
    assert _repin_rc(mod, ["tie-off"]) == 1


def test_has_line_reads_a_repin_at_both_numbers():
    """Three ways round, on a short and a long file sharing a name. A re-pin the short
    file cannot hold at tip gates; one that crossed files stays with the file that held
    it, so a shift in the short one goes unreported, on purpose: its text names neither."""
    mod = _load_module()
    long_, short = "a/main.tex", "b/main.tex"
    lines = lambda tag, k: ["%s %d" % (tag, i) for i in range(1, k + 1)]

    def scanned(moved, was, now):
        base = {long_: lines("long", 60), short: lines("short", 20), "c.md": ["bare `main.tex:%d`" % was]}
        tip = dict(base, **{"c.md": ["bare `main.tex:%d`" % now]})
        for p in moved:
            tip[p] = ["new"] * 3 + base[p]
        with mod.two_trees(base, tip) as (repo, b, t):
            return mod.scan(repo, b, t)

    res = scanned([long_], 10, 50)                          # wrong: the content went to :13
    assert [(f.held, f.n, f.kind, f.moved_to) for f in res["pinned"]] == [(10, 50, "SHIFTED", 13)]
    assert not res["ambiguous"]
    res = scanned([long_, short], 50, 13)                   # only the long file held :50
    assert [(f.target, f.kind, f.moved_to) for f in res["pinned"]] == [(long_, "SHIFTED", 53)]
    res = scanned([short], 50, 13)                          # the long file did not change
    assert not res["pinned"] and not res["ambiguous"]


def test_has_line_falls_back_to_the_base_number_past_every_tip_end():
    """No file holds :99 at tip. That is an advisory OUT-OF-RANGE, not a vanished cite."""
    mod = _load_module()
    assert mod.repin_scan(["past-tip-end"])[0] == {"past-tip-end": [(9, 99, "OUT-OF-RANGE", 0)]}
    base = {"a/m.md": ["x"] * 30, "b/m.md": ["y"] * 30, "c.md": ["bare `m.md:9`"]}
    tip = dict(base, **{"a/m.md": ["new"] + base["a/m.md"], "c.md": ["bare `m.md:99`"]})
    with mod.two_trees(base, tip) as (repo, b, t):
        res = mod.scan(repo, b, t)
    assert [(f.held, f.n, f.kind) for f in res["ambiguous"]] == [(9, 99, "OUT-OF-RANGE")]


def test_line_count_ignores_only_the_final_newline():
    mod = _load_module()
    assert mod.line_count("a\nb\n".split("\n")) == 2
    assert mod.line_count("a\nb".split("\n")) == 2
    assert mod.line_count("a\n\n".split("\n")) == 2
    assert mod.line_count("".split("\n")) == 0


def test_line_count_of_a_loaded_blob_is_git_greps():
    """`line_count()` of a blob as `load()` reads it is the count `git grep -c ''` gives,
    the numbering every citer's `:NNN` was read off: an empty file, no final newline, a
    trailing blank line, CRLF. Only `\\n` ends a line for git: a lone `\\r`, VT, FF, NEL
    and U+2028 do not, though `str.splitlines()` splits on each (a tracked file holds a
    VT today). The pure test above cannot see `load()`: a second trim of the final ''
    there, or a splitlines(), fails here."""
    mod = _load_module()
    bodies = [b"", b"\n", b"a", b"a\n", b"a\nb", b"a\n\n", b"a\r\nb\r\n",
              b"a\rb\n", b"a\x0bb\n", b"a\x0cb\n", "a\x85b\n".encode(), "a\u2028b\n".encode()]
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
            assert mod.line_count(got) == want, (body, got, want)


def _scan_and_exit(mod, base, tip):
    """scan(), and the exit code main() gives it once liveness has passed (repin_scan's rule)."""
    import contextlib
    import io

    with mod.two_trees(base, tip) as (repo, b, t):
        res = mod.scan(repo, b, t)
    with contextlib.redirect_stdout(io.StringIO()):
        rc = 2 if mod.scan_errors(res) else mod.report(res)
    return res, rc


def test_a_plain_cite_past_the_last_line_was_never_valid_at_base():
    """A cite that kept its number, at the end of a 14-line file. :15 never existed, so
    nothing moved under it whichever way the tip changes; :14 can move, run off the end
    of a shorter tip, or lose its line outright."""
    mod = _load_module()
    rows = ["row %d" % i for i in range(1, 15)]                        # 14 lines
    for n, tip_rows, want in (
            (15, rows[1:], []),                                         # tip one line shorter
            (15, rows + ["row 15, new"], []),                           # the line exists only at tip
            (14, rows + ["row 15, new"], []),                           # control: the last line holds
            (14, rows[1:], [("OUT-OF-RANGE", "row 14", "")]),           # ...runs off a shorter tip
            (14, ["new"] + rows, [("SHIFTED", "row 14", "row 13")]),    # ...moves
            (14, rows[:-1], [("OUT-OF-RANGE", "row 14", "")])):         # ...is deleted
        cite = {"docs/c.md": ["see `f.txt:%d`" % n]}
        res, rc = _scan_and_exit(mod, dict(cite, **{"f.txt": rows}), dict(cite, **{"f.txt": tip_rows}))
        got = [(f.kind, f.was, f.now) for f in res["pinned"]]
        assert res["found"] == 1 and got == want and rc == (1 if want else 0), (n, len(tip_rows), got, rc)
    # A re-pin FROM :15 holds a number dead at base, so it keeps the plain test at its new one.
    for tip_rows, want in ((["new"] + rows, [("SHIFTED", "row 3", "row 2", 4)]),
                           (rows[:9] + ["row 10, edited"] + rows[10:], [])):
        res, rc = _scan_and_exit(mod, {"docs/c.md": ["see `f.txt:15`"], "f.txt": rows},
                                 {"docs/c.md": ["see `f.txt:3`"], "f.txt": tip_rows})
        got = [(f.kind, f.was, f.now, f.moved_to) for f in res["pinned"]]
        assert res["tested"] == 1 and got == want and rc == (1 if want else 0), (got, rc)


def test_has_line_drops_a_file_one_line_too_short():
    """A bare `g.md:15` with a/g.md 14 lines long and b/g.md 40: only b/g.md has line 15,
    whether the cite held :15 at base or a re-pin moved it there."""
    mod = _load_module()
    short, long_ = ["short %d" % i for i in range(1, 15)], ["long %d" % i for i in range(1, 41)]
    base = {"docs/c.md": ["see `g.md:15`"], "a/g.md": short, "b/g.md": long_}
    res, rc = _scan_and_exit(mod, base, dict(base, **{"b/g.md": ["inserted"] + long_}))
    assert [(f.target, f.kind, f.how) for f in res["pinned"]] == [
        ("b/g.md", "SHIFTED", "bare basename + has-line")] and not res["ambiguous"] and rc == 1
    res, rc = _scan_and_exit(mod, base, dict(base, **{"a/g.md": short[1:]}))
    assert res["elsewhere"] == 1 and not res["pinned"] and not res["ambiguous"] and rc == 0
    # A bare re-pin onto :15 asks each file for :15 at tip: a/g.md, still 14 lines, has none.
    res, rc = _scan_and_exit(mod, dict(base, **{"docs/c.md": ["see `g.md:10`"]}),
                             dict(base, **{"docs/c.md": ["see `g.md:15`"], "b/g.md": ["inserted"] + long_}))
    assert [(f.target, f.held, f.n, f.kind, f.moved_to) for f in res["pinned"]] == [
        ("b/g.md", 10, 15, "SHIFTED", 11)] and not res["ambiguous"] and rc == 1


def test_a_tie_at_the_end_of_a_file_counts_no_phantom_neighbour():
    """The cited base line sits at or next to the end of its file; the diff takes it out
    and puts it back at two tip lines (they differ from it only in whitespace, which git
    sees and strip() does not). The '' after a final newline is no line, so it agrees with
    nothing. Counted, it forged a tie in A, where only :2 has a real neighbour; broke the
    true ties in B, C and D; and turned a correct re-pin into a fail and a wrong one into
    a pass. The start of a file, with no '' before line 1, was always read right (A
    mirrored). Real lines still agree: the last line of a file with no final newline, and
    two real blanks -- mid-file (E) or as the last line of both files (F), where only the
    phantom after them is discounted."""
    mod = _load_module()
    for key, base, tip, n, put, addr in (
            ("A", ["a", "w", "X"], ["w ", "X ", "c", "d", "X\t"], 3, [2], 2),    # only :2 has a neighbour
            ("A mirrored", ["X", "w", "a"], ["X\t", "d", "c", "X ", "w "], 1, [4], 4),
            ("B", ["a", "b", "X"], ["X ", "c", "d", "e", "X\t"], 3, [1, 5], 0),   # neither has one
            ("C", ["a", "X"], ["X ", "", "c", "X\t", "d"], 2, [1, 4], 0),         # base '' vs a real blank
            ("D", ["a", "X", ""], ["X ", "c", "X\t"], 2, [1, 3], 0),             # a real blank vs tip ''
            ("E", ["a", "", "X", "q"], ["X ", "r", "", "X\t", "s"], 3, [4], 4),   # two real blanks agree
            ("F", ["p", "X", ""], ["X ", "c", "X\t", ""], 2, [3], 3)):           # two real last-line blanks
        with mod.two_trees({"f.md": base}, {"f.md": tip}) as (repo, b, t):
            B, T, H = repo.blob(b, "f.md"), repo.blob(t, "f.md"), repo.hunks(b, t, "f.md")
        assert (mod.lines_at_tip(H, B, T, n), mod.address_at_tip(H, B, T, n)) == (put, addr), key
    # No final newline: the real last line `z` is a neighbour like any other.
    with mod.fixture_repo([], []) as (repo, _, _t):
        trees = []
        for body in (b"X\nz", b"X \nz\nX\t\nq"):
            rc, out = repo.raw("hash-object", "-w", "--stdin", stdin=body)
            assert rc == 0, repo.err
            rc, out = repo.raw("mktree", stdin=("100644 blob %s\tf.md\n" % out.decode().strip()).encode())
            assert rc == 0, repo.err
            trees.append(out.decode().strip())
        B, T, H = repo.blob(trees[0], "f.md"), repo.blob(trees[1], "f.md"), repo.hunks(trees[0], trees[1], "f.md")
        assert (mod.lines_at_tip(H, B, T, 1), mod.address_at_tip(H, B, T, 1)) == ([1], 1), (B, T, H)
    for base, tip, was, now, want in (
            (["a", "w", "X"], ["w ", "X ", "c", "d", "X\t"], 3, 5, [("SHIFTED", 2)]),   # a wrong re-pin
            (["a", "b", "X"], ["X ", "c", "d", "e", "X\t"], 3, 1, [("RE-PINNED", 1)]),   # one side of a tie
            (["p", "X", ""], ["X ", "c", "X\t", ""], 2, 1, [("SHIFTED", 3)])):          # F, a wrong re-pin
        res, rc = _scan_and_exit(mod, {"docs/c.md": ["see `f.md:%d`" % was], "f.md": base},
                                 {"docs/c.md": ["see `f.md:%d`" % now], "f.md": tip})
        got = [(f.kind, f.moved_to) for f in res["pinned"]]
        assert got == want and rc == (1 if want[0][0] == "SHIFTED" else 0), (was, now, got, rc)


def test_a_diff_that_lies_cannot_land_a_line_on_the_phantom():
    """A wrong hunk costs the address and never invents one: the confirm step reads the
    tip's lines, and the '' after its final newline is not one. Base `x y <blank>` (3
    lines), tip `x y` (2); a diff that reports no change aligns the blank :3 with the tip's
    '' -- equal text, no line."""
    mod = _load_module()
    base, tip = "x\ny\n\n".split("\n"), "x\ny\n".split("\n")
    assert mod.lines_at_tip([], base, tip, 3) == [] and mod.address_at_tip([], base, tip, 3) == 0


def test_report_does_not_invent_an_address():
    import contextlib
    import io

    mod = _load_module()
    buf = io.StringIO()
    with mod.two_trees(*mod._repin_trees(["taken-out"])) as (repo, base, tip):
        with contextlib.redirect_stdout(buf):
            mod.report(mod.scan(repo, base, tip))
    assert "the diff took this line out" in buf.getvalue()
    assert "is now at" not in buf.getvalue()


def test_report_leaves_nothing_dangling_on_a_plain_out_of_range():
    mod = _load_module()
    f = mod.Finding("a.md", 1, "b.md", 9, "OUT-OF-RANGE", "x", "", 0, ("b.md",), "path", 9)
    assert mod._arrow(f) == ""


def test_repins_are_listed_only_under_verbose():
    import contextlib
    import io

    mod = _load_module()
    with mod.two_trees(*mod._repin_trees(["correct"])) as (repo, base, tip):
        res = mod.scan(repo, base, tip)
    plain, verbose = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(plain):
        assert mod.report(res) == 0
    with contextlib.redirect_stdout(verbose):
        assert mod.report(res, verbose=True) == 0
    assert "re-pinned from" not in plain.getvalue() and "clean" in plain.getvalue()
    assert "re-pinned from :9" in verbose.getvalue()


class _Stub:
    """The two Repo calls the pairing reads, over literal blobs and hunks."""

    def __init__(self, base, tip, hunks):
        self.lines, self._hunks = {"B": base, "T": tip}, hunks

    def blob(self, rev, path):
        return self.lines[rev]

    def hunks(self, base, tip, path):
        return self._hunks


def test_hunk_headers_including_zero_length_sides():
    mod = _load_module()
    files = ({"a.md": ["1", "2", "3", "4"]}, {"a.md": ["1", "x", "2", "4", "5"]})
    with mod.two_trees(*files) as (repo, base, tip):
        hunks = repo.hunks(base, tip, "a.md")
        assert hunks == [(2, 0, 2, 1), (3, 1, 4, 0), (5, 0, 5, 1)]
        assert hunks == repo.hunks(base, tip, "a.md") and not repo.diff_errors


def test_hunks_of_a_path_with_pathspec_magic():
    mod = _load_module()
    path = "docs/[draft]*.md"
    with mod.two_trees({path: ["a"], "docs/dx.md": ["b"]}, {path: ["c"], "docs/dx.md": ["d", "e"]}) as (repo, b, t):
        assert repo.hunks(b, t, path) == [(1, 1, 1, 1)]


def test_address_reads_the_shift_off_the_hunks():
    mod = _load_module()
    base, tip = ["a", "b", "c"], ["x", "y", "a", "b", "c"]
    hunks = [(1, 0, 1, 2)]
    assert mod.address_at_tip(hunks, base, tip, 1) == 3
    assert mod.address_at_tip(hunks, base, tip, 3) == 5


def test_address_of_a_line_above_every_hunk_is_itself():
    mod = _load_module()
    assert mod.address_at_tip([(3, 0, 3, 1)], ["a", "b", "c"], ["a", "b", "x", "c"], 2) == 2


def test_address_is_zero_when_the_line_is_gone_and_not_put_back():
    mod = _load_module()
    assert mod.address_at_tip([(2, 1, 2, 0)], ["a", "b", "c"], ["a", "c"], 2) == 0


def test_address_gives_up_when_two_put_back_lines_cannot_be_told_apart():
    mod = _load_module()
    base, tip = ["p", "same", "q"], ["same", "p", "q", "same"]
    assert mod.address_at_tip([(1, 0, 1, 1), (2, 1, 3, 0), (4, 0, 4, 1)], base, tip, 2) == 0


def test_address_confirms_equal_after_strip_as_the_verdict_does():
    mod = _load_module()
    assert mod.address_at_tip([(1, 2, 1, 2)], ["  a", "b"], ["x", "a"], 1) == 2


def test_number_is_recovered_only_from_a_line_the_branch_rewrote():
    mod = _load_module()
    cites = mod.leaf_cites("see `a.md:9`", "a.md")
    assert mod.number_at_base("see `a.md:5`", "a.md", 0, cites) == 5
    assert mod.number_at_base(None, "a.md", 0, cites) == 9


def test_number_is_not_recovered_from_a_line_with_a_different_count():
    mod = _load_module()
    cites = mod.leaf_cites("`a.md:9` and `a.md:12`", "a.md")
    assert mod.number_at_base("`a.md:5`", "a.md", 1, cites) == 12


def test_pairing_is_computed_once_per_citer():
    mod = _load_module()
    calls = []
    real = mod.rewritten_lines

    def counted(repo, base, tip, src):
        calls.append(src)
        return real(repo, base, tip, src)

    mod.rewritten_lines = counted
    try:
        mod.repin_scan()
    finally:
        mod.rewritten_lines = real
    assert calls == [mod.REPINNED]


def test_a_new_line_in_a_longer_hunk_recovers_nothing():
    mod = _load_module()
    base, tip = ["unrelated"], ["first `a.md:5`", "second `a.md:6`"]
    assert mod.rewritten_lines(_Stub(base, tip, [(1, 1, 1, 2)]), "B", "T", "src.md") == {}


def test_numberless_pairing_survives_a_longer_hunk():
    mod = _load_module()
    base, tip = ["see `a.md:5`"], ["a new line", "see `a.md:9`"]
    assert mod.rewritten_lines(_Stub(base, tip, [(1, 1, 1, 2)]), "B", "T", "src.md") == {2: 1}


def test_a_line_moved_whole_pairs_with_itself_before_any_lookalike():
    mod = _load_module()
    base, tip = ["see `a.md:1`", "x", "see `a.md:2`"], ["see `a.md:2`", "x", "see `a.md:1`"]
    pairs = mod.rewritten_lines(_Stub(base, tip, [(1, 1, 1, 1), (3, 1, 3, 1)]), "B", "T", "s.md")
    assert pairs == {1: 3, 3: 1}


def test_a_lone_pair_needs_no_rival_on_the_tip_side_either():
    """A new row beside a re-pinned one: which replaced the base row is a guess."""
    mod = _load_module()
    base, tip = ["see `a.md:5`"], ["see `a.md:7`", "see `a.md:9`"]
    assert mod.rewritten_lines(_Stub(base, tip, [(1, 1, 1, 2)]), "B", "T", "s.md") == {}


def test_rows_alike_but_for_their_digits_keep_their_order_in_a_hunk():
    """Two near-identical rows, both re-pinned. Numberless pairing refuses them, so the
    hunk has to give the k-th new row the k-th old one. On #1039 the four re-pins into
    `mathematical-closure.md` are this shape."""
    mod = _load_module()
    base = {"t.md": ["t%d" % i for i in range(1, 9)], "c.md": ["see `t.md:2`", "gap", "see `t.md:4`"]}
    tip = {"t.md": ["new"] + base["t.md"], "c.md": ["see `t.md:3`", "gap", "see `t.md:5`"]}
    with mod.two_trees(base, tip) as (repo, b, t):
        res = mod.scan(repo, b, t)
    assert [(f.lno, f.held, f.n, f.kind) for f in res["pinned"]] == [
        (1, 2, 3, "RE-PINNED"), (3, 4, 5, "RE-PINNED")]
    base["c.md"], tip["c.md"] = ["see `t.md:2`", "see `t.md:4`"], ["see `t.md:3`", "see `t.md:5`"]
    with mod.two_trees(base, tip) as (repo, b, t):
        res = mod.scan(repo, b, t)
    assert [(f.held, f.n, f.kind) for f in res["pinned"]] == [(2, 3, "RE-PINNED"), (4, 5, "RE-PINNED")]


def test_a_target_holding_a_nul_byte_is_still_read_as_text():
    """Without --text git calls the file binary and prints no hunks, so the address
    of every line in it is lost."""
    mod = _load_module()
    base = {"t.md": ["a\0", "b", "c"], "c.md": ["see `t.md:2`"]}
    tip = {"t.md": ["new", "a\0", "b", "c"], "c.md": ["see `t.md:2`"]}
    with mod.two_trees(base, tip) as (repo, b, t):
        assert repo.hunks(b, t, "t.md") == [(1, 0, 1, 1)]
        res = mod.scan(repo, b, t)
    assert [(f.kind, f.moved_to) for f in res["pinned"]] == [("SHIFTED", 3)]


def test_leaf_cites_skips_a_name_that_merely_ends_in_the_leaf():
    mod = _load_module()
    cites = mod.leaf_cites("`universal-operators.md:3` then `common/operators.md:4`", "operators.md")
    assert [int(m.group(2)) for m in cites] == [4]


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

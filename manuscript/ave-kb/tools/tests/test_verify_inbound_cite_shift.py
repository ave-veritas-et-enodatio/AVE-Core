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
    are still not aborts;
  * the citer `git grep` reads every row whole (2026-11-08): under `color.ui` /
    `color.grep = always` (pre-fix: with git's default slot colours, `int()` of a
    colour-wrapped line number raised, exit 2; with only the match slot coloured, set in
    the environment or the scanned repo's own config, each leaf came back wrapped, no cite
    matched, and the run printed a clean exit 0 -- from global or system config the
    self-gate saw it too and the run exited 2), `grep.column` (pre-fix: every text read as
    `<col>:<text>`) and `diff.default.binary` in the environment or the repo's own config
    (pre-fix: every file skipped as binary, exit 0), from a citer
    path holding `:` (exit 2) or a non-ASCII byte (C-quoted, so its link pinned nothing:
    exit 0 where the ASCII control exits 1; and #1079's re-pin of such a citer was never
    recognised), for a changed file named `-...` (git read it as options: exit 2 for
    `-notes.md`, a silent exit 0 for a whole option such as `-q`), past a checked-out
    submodule under `submodule.recurse` (its own files read as citers: a false SHIFTED,
    exit 1), for a citer that gitattributes declare binary (pre-fix: skipped, exit 0)
    and for a tip named by a ref git echoes in another form; a row that does not parse
    aborts (pre-fix: skipped, exit 0); and a user's init.templateDir reaches no fixture;
  * every path is read as its own bytes (2026-11-09): a citer path, a changed path and a
    link that are not UTF-8 never pass for another file's (decoded with 'replace' they
    did: the self-cite skip dropped a cite, a re-pin went unread, a link landed on the
    wrong file); a changed citer named with a carriage return or a newline is read, not
    the file named without it (asked for as `<rev>:<path>`, git read that one: a wrong
    re-pin passed); a file whose name holds a newline, absent at base, aborts nothing; a
    changed citer named in NFD keeps its re-pin on macOS; and the report prints each
    path in one form of its own;
  * each rev is read once, and every line as its own bytes (2026-11-10): a tip named by a
    ref that moves mid-run, or by a name that means two commits on macOS (one recomposed,
    one as typed), never hands the changed list one commit and the diff another (a clean
    exit 0); a changed file whose name is not UTF-8 keeps its re-pins, and a cited line
    holding such a byte compares as its own bytes; a cut-off character counts as one, as
    'replace' counted it (byte by byte, a cite or a link was dropped); a changed file named
    in NFD is looked for as its own bytes on macOS (in NFC, a clean that read none of its
    cites); the report prints every path in ASCII, so paths that look alike print apart;
    and the self-gate's object-store trees hold their files whatever the index config;

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

Run directly (`python tools/tests/test_verify_inbound_cite_shift.py`) or via pytest.
"""

import importlib.util
import re
import subprocess
import sys
import unittest
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
    assert any(l.lstrip().startswith("[PASS] a `-U0` diff that comes back with context lines") for l in lines)
    grep = ["colour config", "column config", "citer path holding a colon", "citer path not ASCII",
            "changed file named -x", "checked-out submodule", "citer declared binary",
            "diff.default.binary config", "binary file naming the leaf",
            "changed file named like a pattern", "line-number config", "citer path not UTF-8",
            "citer line holding a NUL", "changed citer named with a CR", "changed citer not UTF-8",
            "citer link not UTF-8", "changed citer named in NFD", "changed file named not UTF-8",
            "cite gap holding a cut-off character", "link text holding cut-off characters",
            "changed file named in NFD", "tip named by a ref that moves"]
    for name in grep:
        assert any(l.lstrip().startswith("[PASS] a %s: every citer row read whole" % name) for l in lines), name
    # and the whole gate: 10 original probes, one per REPINS row plus #1079's 7 re-pin
    # checks, the damaged objects, the -U0 context-lines probe, and the citer-grep cases --
    # so dropping ANY probe, from any of the merged branches, fails here
    assert len(lines) == 10 + len(mod.REPINS) + 7 + len(damaged) + 1 + len(grep), len(lines)
    assert sorted(mod.LOST) == sorted(damaged)
    assert sorted(mod.GREP) == sorted(grep)


def test_mutation_receipt_holds():
    import contextlib
    import io

    mod = _load_module()
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        assert mod.mutation_receipt() == 0, buf.getvalue()
    assert not mod.MUTATE, "a mutation leaked out of the receipt"
    # Every row present, under its own number. Merging #1079 interleaved #1081's rows
    # into M6-M39 without a conflict marker; a dropped or renumbered row must fail here.
    rows = re.findall(r"\[(OK|BROKEN)\] M(\d+) ", buf.getvalue())
    assert {int(n) for _, n in rows} == set(range(1, 47 + len(mod.GREP))), sorted({int(n) for _, n in rows})
    assert all(status == "OK" for status, _ in rows)
    # one row per citer-grep case, each with its rule off (grep-config-unpinned drops two flags,
    # one per case it serves; grep-no-z also brings back the pre-fix split)
    for rule in ("grep-config-unpinned", "grep-no-z", "grep-no-e", "grep-recurses", "grep-commit",
                 "grep-binary-config", "grep-binary", "grep-no-F", "grep-no-n", "grep-path-lossy",
                 "grep-text-no-nul", "load-by-name", "paths-lossy", "grep-text-lossy", "diff-precomposed",
                 "blob-lossy", "gap-per-byte", "link-per-byte", "grep-precomposed", "revs-as-typed"):
        assert "(%s): with only that rule off the run must read" % rule in buf.getvalue(), rule
    # ...and by case: two rules serve two cases each, so a receipt that ran one of those cases
    # twice and the other never would pass the rule check. Each case's whole row, once.
    for name, c in mod.GREP.items():
        row = ("read the citer rows of a %s with one rule off (%s): with only that rule off the run must "
               "read %s -- got %s; with it on they must read whole and fire -- got %s"
               % (name, c.rule, c.unpinned, c.unpinned, mod.GREP_WANT))
        assert buf.getvalue().count(row) == 1, name


def test_the_default_fixture_repo_carries_the_hostile_config():
    """Every self-gate verdict is reached under it, not only the GREP probes' (the colour and
    the column probe each set the other's trigger benign, to isolate their own). Read as git
    resolves each key, not from the repo's own file alone: a worktree config copied in from a
    template would outrank that file."""
    mod = _load_module()
    with mod.fixture_repo(["explicit-B"], [mod.B]) as (repo, _, _t):
        got = {key: repo.sh("config", key).strip() for key, _v in mod.HOSTILE}
    assert got == dict(mod.HOSTILE)
    # By name, not read off HOSTILE itself: a dropped entry must fail here, on every platform
    # (core.precomposeUnicode does nothing off macOS;
    # test_git_add_in_a_fixture_keeps_a_non_ascii_name_as_written holds what it does there).
    assert sorted(dict(mod.HOSTILE)) == sorted([
        "color.ui", "color.grep", "color.grep.filename", "color.grep.lineNumber", "color.grep.column",
        "color.grep.separator", "color.grep.match", "grep.column", "grep.lineNumber", "core.quotePath",
        "submodule.recurse", "grep.patternType", "core.precomposeUnicode"])
    assert {"color.ui": "always", "color.grep": "always", "grep.column": "true", "grep.lineNumber": "false",
            "core.quotePath": "true", "submodule.recurse": "true", "grep.patternType": "basic",
            "core.precomposeUnicode": "true"}.items() <= got.items()


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
            if "grep" in a[:5]:
                return 128, b""
            return super().raw(*a, stdin=stdin)

    # without the return-code check this reads as a clean zero
    assert _main_rc(mod, mod.ALL, [mod.B], repo_cls=GrepFails) == 2

    class GrepKilled(mod.Repo):                     # a signal: subprocess returns it NEGATIVE
        def raw(self, *a, stdin=None):
            if "grep" in a[:5]:
                self.err = ""
                return -9, b""
            return super().raw(*a, stdin=stdin)

    assert _main_rc(mod, mod.ALL, [mod.B], repo_cls=GrepKilled) == 2


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
    lists `f.txt` as a blob (with the object ID load() asks for it by)."""
    class Fake(mod.Repo):
        def raw(self, *a, stdin=None):
            if a[:1] == ("cat-file",):
                self.err = "fatal: unable to stream" if rc else ""
                return rc, reply
            return 0, b""

        def tree(self, rev):
            self._oids[rev] = {"f.txt": "a" * 40}
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
            if "grep" in a[:5]:
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


# ------------------------------------------- the citer `git grep` reads every row whole
#
# Each test below fails, for the behavioural reason, on a gate without the fix it guards:
# #1081's head 7f71bc71d, unless its docstring names a later commit or a platform. Most
# build their own trees and config. Some use this gate's own tables or helpers and so cannot
# run on a gate older than those, where they fail for want of the helper: each of those names
# the commit that brought the helper in and the first where it fails for its own reason.

_VOL = ["vol line %d" % i for i in range(1, 15)]
_LONG_MAIN = ["letter line %d" % i for i in range(1, 41)]


def _shifted(files, path):
    out = dict(files)
    out[path] = ["inserted 1", "inserted 2", "inserted 3"] + files[path]
    return out


def _run_seeing_texts(mod, repo, b, t):
    """main()'s exit code and stdout, plus every (citer, text) the scan of `repo` -- not the
    self-gate's fixture scans before it -- read a cite from."""
    import contextlib
    import io

    seen, real_scan, real_addr = [], mod.scan, mod.addressees

    def spy(m, leaf, src, text, *a):
        seen.append((src, text))
        return real_addr(m, leaf, src, text, *a)

    def scan(r, *a, **k):
        if r is not repo:
            return real_scan(r, *a, **k)
        mod.addressees = spy
        try:
            return real_scan(r, *a, **k)
        finally:
            mod.addressees = real_addr

    buf = io.StringIO()
    mod.scan = scan
    try:
        with contextlib.redirect_stdout(buf):
            rc = mod.main(b, t, repo=repo)
    finally:
        mod.scan = real_scan
    return rc, buf.getvalue(), seen


def _bare_minimum_config(repo):
    """Rewrite the repo's own config to what git needs to read the repo -- its format
    version and extensions (a SHA-256 repo cannot lose `objectformat`) -- and return what
    `config --list` shows then."""
    import os

    version = repo.sh("config", "--local", "core.repositoryformatversion").strip() or "0"
    ext = [l.split(" ", 1) for l in repo.sh("config", "--local", "--get-regexp", r"^extensions\.").splitlines()]
    text = "[core]\n\trepositoryformatversion = %s\n\tbare = false\n" % version
    keep = ["core.repositoryformatversion=" + version, "core.bare=false"]
    for key, value in ext:
        text += "[extensions]\n\t%s = %s\n" % (key.split(".", 1)[1], value)
        keep.append("%s=%s" % (key, value))
    with open(os.path.join(repo.cwd, ".git", "config"), "w") as fh:
        fh.write(text)
    return keep


def test_citer_grep_reads_through_hostile_grep_and_colour_config():
    """One key at a time, as the ONLY config git sees: an empty HOME, no system config, and a
    repo config rewritten to the bare minimum (so `color.ui` is not outranked by a
    `color.grep` from anywhere). Pre-fix: colour wrapped the line number in ANSI codes and
    `int()` raised (exit 2); `grep.column` prefixed every text with `<col>:`; and
    `diff.default.binary` made -I skip every file, the citer too (exit 0)."""
    import shutil
    import tempfile

    line = "vol frontmatter, `docs/vol/main.tex:5`"
    files = {"docs/vol/main.tex": _VOL, "docs/citers.md": [line]}
    home = tempfile.mkdtemp(prefix="inbound-cite-home-")
    try:
        # (`grep.lineNumber = false` is git's own default: as the only config it changes nothing.
        # HOSTILE's entry is pinned by test_every_grep_rule_holds_under_a_hostile_global_config.)
        for key, value in (("color.ui", "always"), ("color.grep", "always"), ("grep.column", "true"),
                           ("diff.default.binary", "true")):
            with _two_trees(files, _shifted(files, "docs/vol/main.tex")) as (mod, repo, b, t):
                repo.env.update(HOME=home, XDG_CONFIG_HOME=home, GIT_CONFIG_NOSYSTEM="1")
                keep = _bare_minimum_config(repo)
                assert repo.raw("config", key, value)[0] == 0
                assert repo.sh("config", "--list").split() == keep + ["%s=%s" % (key.lower(), value)]
                rc, out, seen = _run_seeing_texts(mod, repo, b, t)
            assert rc == 1, (key, out)
            assert seen == [("docs/citers.md", line)], (key, seen)
    finally:
        shutil.rmtree(home, ignore_errors=True)


def test_citer_grep_under_hostile_global_config():
    """Pre-fix, `color.ui = always` in ~/.gitconfig broke both the gate and --selftest (exit 2);
    in GIT_CONFIG_* env alone it broke the gate run while --selftest passed, because the
    fixtures scrub every GIT_* variable. The repo under test keeps only its format version
    (and extensions), so ~/.gitconfig or the env is all git sees. The self-gate's fixtures now carry
    HOSTILE in their own config, which outranks ~/.gitconfig -- what --selftest shows here is
    that it runs at all; the column and colour READING is test_..._hostile_grep_and_colour_config."""
    import os
    import shutil
    import tempfile

    line = "vol frontmatter, `docs/vol/main.tex:5`"
    files = {"docs/vol/main.tex": _VOL, "docs/citers.md": [line]}
    home = tempfile.mkdtemp(prefix="inbound-cite-home-")
    try:
        # (no `grep.lineNumber = false`: it is git's own default, and HOSTILE's entry is pinned by
        # test_every_grep_rule_holds_under_a_hostile_global_config)
        with open(os.path.join(home, ".gitconfig"), "w") as fh:
            fh.write("[color]\n\tui = always\n[grep]\n\tcolumn = true\n")
        env = _git_free_env(HOME=home, XDG_CONFIG_HOME=home, GIT_CONFIG_NOSYSTEM="1")
        selftest = subprocess.run([sys.executable, str(_TOOL), "--selftest"], capture_output=True,
                                  text=True, env=env)
        with _two_trees(files, _shifted(files, "docs/vol/main.tex")) as (mod, repo, b, t):
            _bare_minimum_config(repo)
            run = subprocess.run([sys.executable, str(_TOOL), b, t], capture_output=True, text=True,
                                 cwd=repo.cwd, env=env)
            env_cfg = subprocess.run(
                [sys.executable, str(_TOOL), b, t], capture_output=True, text=True, cwd=repo.cwd,
                env=_git_free_env(HOME=home + "/none", XDG_CONFIG_HOME=home + "/none",
                                  GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_COUNT="1",
                                  GIT_CONFIG_KEY_0="color.ui", GIT_CONFIG_VALUE_0="always"))
    finally:
        shutil.rmtree(home, ignore_errors=True)
    assert selftest.returncode == 0, selftest.stdout + selftest.stderr
    assert run.returncode == 1 and "[SHIFTED]" in run.stdout, run.stdout + run.stderr
    assert env_cfg.returncode == 1 and "[SHIFTED]" in env_cfg.stdout, env_cfg.stdout + env_cfg.stderr


def test_citer_path_holding_a_colon_is_read():
    """Pre-fix: `split(':', 3)` cut `docs/a:b.md` at its colon and `int('b.md')` raised."""
    line = "see `docs/vol/main.tex:5`"
    for citer, want in (("docs/ab.md", 1), ("docs/a:b.md", 1)):
        files = {"docs/vol/main.tex": _VOL, citer: [line]}
        with _two_trees(files, _shifted(files, "docs/vol/main.tex")) as (mod, repo, b, t):
            rc, out, seen = _run_seeing_texts(mod, repo, b, t)
        assert rc == want and seen == [(citer, line)], (citer, rc, seen, out)


def test_non_ascii_citer_path_keeps_its_link_pin():
    """A link resolves against the CITING file's directory. Pre-fix the non-ASCII citer came
    back C-quoted (`"docs/vol/not\\303\\251s.md"`), the link resolved to no file, and the cite
    fell to an ambiguous bare name: exit 0 where the ASCII control exits 1."""
    link = "frontmatter: [the abstract](main.tex):11"
    for citer in ("docs/vol/notes.md", "docs/vol/not\u00e9s.md"):
        files = {"docs/vol/main.tex": _VOL, "papers/main.tex": _LONG_MAIN, citer: [link]}
        with _two_trees(files, _shifted(files, "docs/vol/main.tex")) as (mod, repo, b, t):
            assert repo.raw("config", "core.quotePath", "true")[0] == 0     # git's default
            rc, out, seen = _run_seeing_texts(mod, repo, b, t)
        assert rc == 1 and "pinned by: link target" in out, (citer, out)
        assert seen == [(citer, link)], seen


def test_changed_file_whose_name_starts_with_a_dash():
    """Pre-fix `git grep -nIF -notes.md` read the leaf as options: exit 129, gate exit 2. (A leaf
    that is a whole option, such as `-q`, was worse: git took it as --quiet and printed
    nothing, a clean exit 0.)"""
    rows = ["row %d" % i for i in range(1, 15)]
    for leaf in ("notes.md", "-notes.md", "-q"):
        files = {"docs/" + leaf: rows, "docs/c.md": ["see `docs/%s:5`" % leaf]}
        with _two_trees(files, _shifted(files, "docs/" + leaf)) as (mod, repo, b, t):
            rc, out, _ = _run_seeing_texts(mod, repo, b, t)
        assert rc == 1 and "[SHIFTED]" in out, (leaf, out)


def test_a_checked_out_submodule_is_not_read_as_citers():
    """`submodule.recurse = true` sends git grep into a checked-out submodule; pre-fix its own
    notes.md, citing its own `docs/vol/main.tex:5`, read as a citer HERE: a false SHIFTED,
    exit 1, though no file of this repo cites the changed file. Built with commit-tree under a
    fixed identity, unsigned -- no `git commit`, no `git submodule add`."""
    import os

    files = {"docs/vol/main.tex": _VOL, "README.md": ["readme"]}
    with _two_trees(files, _shifted(files, "docs/vol/main.tex")) as (mod, repo, b, t):
        sub = mod.Repo(cwd=os.path.join(repo.cwd, "sibling"), scrub_env=True)
        sub.env.update(GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@invalid", GIT_COMMITTER_NAME="t",
                       GIT_COMMITTER_EMAIL="t@invalid")
        os.makedirs(sub.cwd)
        with open(os.path.join(sub.cwd, "notes.md"), "w") as fh:
            fh.write("its own `docs/vol/main.tex:5` says so\n")
        modules = '[submodule "sibling"]\n\tpath = sibling\n\turl = ./sibling\n'
        with open(os.path.join(repo.cwd, ".gitmodules"), "w") as fh:
            fh.write(modules)
        assert sub.raw("init", "-q", "--template=")[0] == 0 and sub.raw("add", "-A", "-f")[0] == 0
        commit = sub.sh("commit-tree", "--no-gpg-sign", "-m", "s", sub.sh("write-tree").strip()).strip()
        blob = repo.raw("hash-object", "-w", "--stdin", stdin=modules.encode())[1].decode().strip()
        for args in (("config", "submodule.sibling.url", "./sibling"), ("config", "submodule.sibling.active", "true"),
                     ("config", "submodule.recurse", "true"),
                     ("read-tree", "--no-recurse-submodules", t),
                     ("update-index", "--add", "--cacheinfo", "100644,%s,.gitmodules" % blob,
                      "--cacheinfo", "160000,%s,sibling" % commit)):
            assert repo.raw(*args)[0] == 0, (args, repo.err)
        tip = repo.sh("write-tree").strip()
        assert "sibling/notes.md" in repo.sh("grep", "--recurse-submodules", "-F", "-e", "main.tex", tip, "--")
        rc, out, seen = _run_seeing_texts(mod, repo, b, tip)
    assert rc == 0 and not seen and "sibling/notes.md" not in out, (rc, seen, out)


def test_tip_named_by_a_ref_git_echoes_in_another_form():
    """git grep prefixes each row with the rev as it ECHOES it, and on macOS
    (core.precomposeUnicode) a ref typed in NFD comes back in NFC: b6417a9db's prefix check
    (c8c63be19 before the rebase) then aborted (exit 2) where 7f71bc71d exits 1 -- this guards
    that regression, so it passes at 7f71bc71d and fails at b6417a9db on macOS. Rows are now
    read against the tip's tree ID, and every git call is handed the one object resolve()
    reads the name as, so no call reads the name again. Where git echoes the name as typed
    (Linux), this passes either way. Under reftable with core.precomposeUnicode set in
    ~/.gitconfig, 28d2a1ad8 and 239a44a74 aborted here (exit 2): one call read the NFD name as
    typed (the pinned `git diff-tree`, the cat-file request), and no ref holds it so. Skipped if
    the name resolves neither recomposed nor as typed."""
    nfd = "cafe\u0301"
    files = {"docs/vol/main.tex": _VOL, "docs/citers.md": ["see `docs/vol/main.tex:5`"]}
    with _two_trees(files, _shifted(files, "docs/vol/main.tex")) as (mod, repo, b, t):
        assert repo.raw("-c", "core.hooksPath=/dev/null", "update-ref", "refs/tags/" + nfd, t)[0] == 0, repo.err
        if all(repo.raw("-c", "core.precomposeUnicode=" + v, "rev-parse", "--verify", "--quiet",
                        nfd + "^{tree}")[0] != 0 for v in ("true", "false")):
            raise unittest.SkipTest("the NFD ref name resolves neither way here")
        rc, out, _ = _run_seeing_texts(mod, repo, b, nfd)
    assert rc == 1 and "[SHIFTED]" in out, out


def test_a_tip_name_that_means_two_commits_is_refused():
    """macOS only. Two refs whose names differ only in normalization, one in NFC and one in NFD,
    can coexist packed, and a tip typed in NFD then means one commit to the git calls that
    recompose it and the other to those that do not -- which calls, depending on where
    core.precomposeUnicode is set. 28d2a1ad8 read the changed list from one and the citer grep
    from the other: in macOS's default config (the key in the repo's own config) a clean exit 0
    where the NFC tip exits 1. The name is read both ways and refused, exit 2, with the key in
    the repo config and with it in ~/.gitconfig too. A name typed in NFD for a packed ref stored
    in NFC alone means that ref, and the run reaches its verdict, where 28d2a1ad8 aborted
    (exit 2): its liveness read the name as typed, or its pinned `git diff-tree` did."""
    import os
    import shutil
    import tempfile

    if sys.platform != "darwin":
        raise unittest.SkipTest("git recomposes names only on macOS")
    nfc, nfd = "refs/tags/rel-caf\u00e9", "refs/tags/rel-cafe\u0301"
    off = ("-c", "core.precomposeUnicode=false", "-c", "core.hooksPath=/dev/null")
    plain = {"docs/vol/main.tex": _VOL}
    files = dict(plain, **{"docs/citers.md": ["see `docs/vol/main.tex:5`"]})
    home = tempfile.mkdtemp(prefix="inbound-cite-home-")
    saved = dict(os.environ)
    try:
        for config in ("", "[core]\n\tprecomposeUnicode = true\n"):
            with open(os.path.join(home, ".gitconfig"), "w") as fh:
                fh.write(config)
            os.environ.update(HOME=home, XDG_CONFIG_HOME=home)
            with _two_trees(files, _shifted(files, "docs/vol/main.tex")) as (mod, repo, b, t):
                other = mod._write_tree(repo, repo.cwd, plain)        # no citer: its grep finds nothing
                for args in (("update-ref", nfc, t), ("pack-refs", "--all"), ("update-ref", nfd, other),
                             ("pack-refs", "--all")):
                    assert repo.raw(*off, *args)[0] == 0, (args, repo.err)
                rc, out, _ = _run_seeing_texts(mod, repo, b, nfd)
                assert rc == 2 and "names two objects" in out, (config, rc, out)
                rc, out, _ = _run_seeing_texts(mod, repo, b, nfc)
                assert rc == 1 and "[SHIFTED]" in out, (config, rc, out)
            with _two_trees(files, _shifted(files, "docs/vol/main.tex")) as (mod, repo, b, t):
                for args in (("update-ref", nfc, t), ("pack-refs", "--all")):
                    assert repo.raw(*off, *args)[0] == 0, (args, repo.err)
                rc, out, _ = _run_seeing_texts(mod, repo, b, nfd)
                assert rc == 1 and "[SHIFTED]" in out, (config, rc, out)
    finally:
        os.environ.clear()
        os.environ.update(saved)
        shutil.rmtree(home, ignore_errors=True)


def test_an_unparseable_grep_row_aborts_and_is_never_skipped():
    """Pre-fix a row that did not split into four fields was skipped: a citer never found,
    and the run printed a clean zero."""
    mod = _load_module()
    with mod.fixture_repo(["explicit-B"], [mod.B]) as (fixture, b, t):
        good = b"%s:docs/citers.md\x001\x00see `manuscript/vol_1_foundations/main.tex:5`\n" % t.encode()
        for reply in (b"not a grep row\n",                         # no field separators at all
                      good.replace(t.encode(), b"other-rev"),      # another rev's row
                      good + good[:len(good) // 2],                # a whole row, then a cut one
                      good + good[:-1]):                           # ...one that lost only its LF
            class Garbled(mod.Repo):
                def raw(self, *a, stdin=None):
                    if "grep" in a[:5]:
                        self.err = ""
                        return 0, reply
                    return super().raw(*a, stdin=stdin)

            rc, out, _ = _run_seeing_texts(mod, Garbled(cwd=fixture.cwd, scrub_env=True), b, t)
            assert rc == 2, (reply, out)
            # the scan's own abort, not the self-gate's, whose [FAIL] lines read "unparseable row" too
            assert "`git grep` failed while collecting citers of 'main.tex' (unparseable row" in out, (reply, out)
            assert "self-gate FAILED" not in out and "clean —" not in out, (reply, out)


def test_a_citer_declared_binary_is_still_read():
    """git looks gitattributes up for binary-ness only when it greps a COMMIT. The pre-fix gate
    grepped the tip as named -- in CI, a commit -- so a text citer that any attribute source
    declared binary was skipped and the run printed a clean zero. The gate greps the tip's
    tree. Each case first proves that a grep of the commit really skips the citer."""
    import os

    line = "see `docs/vol/main.tex:5`"
    files = {"docs/vol/main.tex": _VOL, "docs/citers.md": [line]}
    for where, text in ((".gitattributes", "docs/citers.md binary"), (".gitattributes", "*.md -diff"),
                        ("info/attributes", "docs/citers.md binary"), ("core.attributesFile", "*.md -diff")):
        base, tip = dict(files), _shifted(files, "docs/vol/main.tex")
        if where == ".gitattributes":
            base[where] = tip[where] = [text]
        with _two_trees(base, tip) as (mod, repo, b, t):
            if where != ".gitattributes":
                attrs = os.path.join(repo.cwd, ".git", "info" if where == "info/attributes" else "", "attributes")
                os.makedirs(os.path.dirname(attrs), exist_ok=True)
                with open(attrs, "w") as fh:
                    fh.write(text + "\n")
                if where == "core.attributesFile":
                    assert repo.raw("config", "core.attributesFile", attrs)[0] == 0
            repo.env.update(GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@invalid", GIT_COMMITTER_NAME="t",
                            GIT_COMMITTER_EMAIL="t@invalid")
            commit = repo.sh("commit-tree", "--no-gpg-sign", "-m", "tip", t).strip()
            listed = {rev: repo.sh("-c", "diff.default.binary=auto", "grep", "-I", "-l", "--no-color",
                                   "-F", "-e", "main.tex", rev, "--") for rev in (commit, t)}
            assert "docs/citers.md" not in listed[commit], (where, listed)      # the case is armed
            assert "docs/citers.md" in listed[t], (where, listed)
            res = mod.scan(repo, b, commit)
        assert not mod.scan_errors(res), (where, mod.scan_errors(res))
        assert [(f.src, f.kind) for f in res["pinned"]] == [("docs/citers.md", "SHIFTED")], (where, res["pinned"])


def test_a_correct_repin_in_a_citer_whose_path_git_would_quote_passes():
    """#1079 recognises a re-pin only in a citer the branch changed, keyed by the path
    `diff -z` prints, unquoted. Before -z the citer grep handed back `docs/\u00e9/c.md`
    C-quoted, never matched it, and read a correct re-pin as SHIFTED (exit 1); a citer at
    `docs/a:b.md` crashed the split (exit 2). Fails at #1081's head, 7f71bc71d."""
    for citer in ("docs/e/c.md", "docs/\u00e9/c.md", "docs/a:b.md"):
        files = {"docs/vol/main.tex": _VOL, citer: ["see `docs/vol/main.tex:5`"]}
        tip = _shifted(files, "docs/vol/main.tex")
        tip[citer] = ["see `docs/vol/main.tex:8`"]                     # the cite follows its line
        with _two_trees(files, tip) as (mod, repo, b, t):
            rc, out, seen = _run_seeing_texts(mod, repo, b, t)
        assert rc == 0 and "[SHIFTED]" not in out, (citer, rc, out)
        assert (citer, "see `docs/vol/main.tex:8`") in seen, (citer, seen)


def test_every_grep_rule_holds_under_a_hostile_global_config():
    """The GREP receipt rows, on a machine whose ~/.gitconfig sets the grep slot colours to
    `normal`, `color.grep = never`, `grep.column = false`, `grep.lineNumber = true`,
    `grep.patternType = fixed`, `diff.default.binary = true`, `core.quotePath = false`,
    `core.precomposeUnicode = false`, an excludesFile listing notes.md and a
    `submodule.active` pathspec that leaves the fixture's submodule out. With its pin off each
    case must still read its unpinned verdict, and with it on read whole. Without the
    fixtures' slot colours, `grep.lineNumber = false`, `grep.patternType = basic`,
    `core.quotePath = true`, `add -f` or `active = true`, rows go BROKEN on such a machine
    (test_the_default_fixture_repo_carries_the_hostile_config pins each HOSTILE key by name;
    only this test shows what they do, and nothing else pins `add -f` or `active = true`).
    (`core.precomposeUnicode = false` changes no row: every fixture tree with a non-ASCII path
    is built in the object store; the next test holds what the fixtures' `true` does.) Needs
    Odd.unpinned, from 2d4f8eab7; checked against copies of this gate with one fixture fix
    reverted."""
    import os
    import shutil
    import tempfile

    mod = _load_module()
    home = tempfile.mkdtemp(prefix="inbound-cite-home-")
    saved = dict(os.environ)
    try:
        with open(os.path.join(home, "excludes"), "w") as fh:
            fh.write("notes.md\n")
        with open(os.path.join(home, ".gitconfig"), "w") as fh:
            fh.write('[color]\n\tgrep = never\n[color "grep"]\n\tfilename = normal\n\tlineNumber = normal\n'
                     '\tcolumn = normal\n\tseparator = normal\n\tmatch = normal\n[grep]\n\tcolumn = false\n'
                     '\tlineNumber = true\n\tpatternType = fixed\n'
                     '[diff "default"]\n\tbinary = true\n'
                     '[core]\n\tquotePath = false\n\tprecomposeUnicode = false\n\texcludesFile = %s\n'
                     '[submodule]\n\tactive = docs\n\trecurse = false\n' % os.path.join(home, "excludes"))
        os.environ.update(HOME=home, XDG_CONFIG_HOME=home)
        for name, c in mod.GREP.items():
            mod.MUTATE.add(c.rule)
            try:
                v = mod.grep_case_verdict(name)
            finally:
                mod.MUTATE.discard(c.rule)
            assert v == c.unpinned, (name, v)
            assert mod.grep_case_verdict(name) == mod.GREP_WANT, name
    finally:
        os.environ.clear()
        os.environ.update(saved)
        shutil.rmtree(home, ignore_errors=True)


def test_git_add_in_a_fixture_keeps_a_non_ascii_name_as_written():
    """macOS only. Under a global `core.precomposeUnicode = false`, on a filesystem that stores
    names in NFD (HFS+; here each file is written under its NFD name, as HFS+ would store it),
    `git add` records the NFD bytes of a non-ASCII name. The fixtures' own `true` (HOSTILE)
    makes it record the NFC name the test wrote, which every test that builds a tree with
    _write_tree() relies on. Shown without the entry first, so this cannot pass vacuously.
    Round 4 added the entry when the self-gate's own non-ASCII probe depended on it, with no
    test; that probe's tree is now built in the object store. Needs HOSTILE and
    two_trees(config=), from b6417a9db; fails there and through 2d4f8eab7, where both arms record
    the NFD name, and passes from 239a44a74."""
    import builtins
    import os
    import shutil
    import tempfile
    import unicodedata

    if sys.platform != "darwin":
        raise unittest.SkipTest("git recomposes names only on macOS")
    mod = _load_module()
    name = "docs/not\u00e9s.md"
    without = tuple(kv for kv in mod.HOSTILE if kv[0] != "core.precomposeUnicode")
    got = {}
    saved = dict(os.environ)
    home = tempfile.mkdtemp(prefix="inbound-cite-home-")
    try:
        with open(os.path.join(home, ".gitconfig"), "w") as fh:
            fh.write("[core]\n\tprecomposeUnicode = false\n")
        os.environ.update(HOME=home, XDG_CONFIG_HOME=home)
        mod.open = lambda p, *a, **k: builtins.open(unicodedata.normalize("NFD", p), *a, **k)
        for label, config in (("without", without), ("with", mod.HOSTILE)):
            with mod.two_trees({"a.md": ["a"]}, {"a.md": ["a"]}, config=config) as (repo, _b, _t):
                tree = mod._write_tree(repo, repo.cwd, {name: ["x"]})
                got[label] = repo.raw("ls-tree", "-r", "-z", "--name-only", tree)[1]
    finally:
        os.environ.clear()
        os.environ.update(saved)
        shutil.rmtree(home, ignore_errors=True)
    assert got["without"] == unicodedata.normalize("NFD", name).encode() + b"\0", got    # armed
    assert got["with"] == name.encode() + b"\0", got


def test_config_text_survives_a_round_trip_through_git():
    """config_text() writes values and subsections git reads back unchanged -- `#`, `;`, a
    leading space, `"` and a backslash included -- and refuses a name whose section or key
    is empty. Fails at 8f529d35f (21382a0f9 before the rebase), whose config_text did not
    quote."""
    import os
    import shutil
    import tempfile

    mod = _load_module()
    pairs = [("a.b", "#x"), ("a.c", ";y"), ("a.d", " lead"), ("a.e", 'q"q'), ("a.f", "b\\b"),
             ('s.sub"q.k', "v")]
    d = tempfile.mkdtemp(prefix="inbound-cite-cfg-")
    try:
        cfg = os.path.join(d, "config")
        with open(cfg, "w", encoding="utf-8") as fh:
            fh.write(mod.config_text(pairs))
        for key, value in pairs:
            r = subprocess.run(["git", "config", "--file", cfg, "--get", key], capture_output=True, text=True)
            assert r.returncode == 0 and r.stdout == value + "\n", (key, r.stdout, r.stderr)
    finally:
        shutil.rmtree(d, ignore_errors=True)
    for bad in ("nodot", ".key", "section."):
        try:
            mod.config_text([(bad, "v")])
        except mod.FixtureError:
            continue
        raise AssertionError("config_text accepted %r" % bad)


def test_a_template_config_without_a_final_newline_reaches_no_fixture():
    """init.templateDir copies its config into every `git init`, and the fixture config was
    appended to it: a template config ending without a newline ran on into the first
    appended line (`ui = auto[color]`), and every fixture -- so every run -- died, exit 2.
    The fixtures init with --template=. Needs HOSTILE, from b6417a9db (c8c63be19 before the
    rebase), and fails there: it added the append. The submodule's own `git init` is the next
    test's."""
    import os
    import shutil
    import tempfile

    mod = _load_module()
    home = tempfile.mkdtemp(prefix="inbound-cite-home-")
    saved = dict(os.environ)
    try:
        tpl = os.path.join(home, "template")
        os.makedirs(tpl)
        with open(os.path.join(tpl, "config"), "w") as fh:
            # [core] first: `git init` edits its keys in place, so the tail stays unrepaired
            fh.write("[core]\n\tbare = false\n[color]\n\tui = auto")        # no final newline
        with open(os.path.join(home, ".gitconfig"), "w") as fh:
            fh.write("[init]\n\ttemplateDir = %s\n" % tpl)
        os.environ.update(HOME=home, XDG_CONFIG_HOME=home)
        with mod.fixture_repo(["explicit-B"], [mod.B]) as (repo, b, t):
            res = mod.scan(repo, b, t)
            colour = repo.sh("config", "--local", "color.ui").strip()
    finally:
        os.environ.clear()
        os.environ.update(saved)
        shutil.rmtree(home, ignore_errors=True)
    assert colour == "always", colour
    assert not mod.scan_errors(res) and [f.kind for f in res["pinned"]] == ["SHIFTED"], res["pinned"]


def test_a_template_reaches_neither_fixture_init():
    """Both `git init`s a fixture runs -- its own and its submodule's -- take --template=. A
    template's config that is a symlink is copied as one, and `git init` then writes its
    [core] block through it, into the user's own file. Fails with --template= taken off
    either init: off the submodule's, nothing else notices (the submodule's config is never
    appended to). Needs fixture_repo(submodule=), from 8f529d35f; fails at 8f529d35f and
    8d0e14416, and passes from 2d4f8eab7."""
    import os
    import shutil
    import tempfile

    mod = _load_module()
    home = tempfile.mkdtemp(prefix="inbound-cite-home-")
    saved = dict(os.environ)
    try:
        tpl = os.path.join(home, "template")
        os.makedirs(tpl)
        real = os.path.join(home, "my-config")
        with open(real, "w") as fh:
            fh.write("[user]\n\tname = me\n")
        os.symlink(real, os.path.join(tpl, "config"))
        with open(os.path.join(home, ".gitconfig"), "w") as fh:
            fh.write("[init]\n\ttemplateDir = %s\n" % tpl)
        before = (open(real).read(), os.stat(real).st_mode)
        os.environ.update(HOME=home, XDG_CONFIG_HOME=home)
        with mod.fixture_repo(["explicit-B"], [mod.B], submodule=True) as (repo, b, t):
            res = mod.scan(repo, b, t)
        after = (open(real).read(), os.stat(real).st_mode)
    finally:
        os.environ.clear()
        os.environ.update(saved)
        shutil.rmtree(home, ignore_errors=True)
    assert after == before, after
    assert not mod.scan_errors(res) and [f.kind for f in res["pinned"]] == ["SHIFTED"], res["pinned"]


def test_a_citer_path_cannot_forge_a_report_line():
    """Read with -z, a citer path comes back as its own bytes, a newline or an ESC included,
    where before -z git C-quoted it. Printed raw, `docs/x<LF>  clean ...` forged a report
    line and an ESC restyled the log; the report prints each control character as its escape.
    Fails at b6417a9db (c8c63be19 before the rebase); at 7f71bc71d git C-quoted the path. The
    em dash prints as `\\u2014`, as every path prints in ASCII, so this fails at 239a44a74 and
    28d2a1ad8 too, which printed it as itself."""
    line = "see `docs/vol/main.tex:5`"
    citer = "docs/x\n  clean \u2014 nothing moved\x1b[8m.md"
    files = {"docs/vol/main.tex": _VOL, citer: [line]}
    with _two_trees(files, _shifted(files, "docs/vol/main.tex")) as (mod, repo, b, t):
        rc, out, seen = _run_seeing_texts(mod, repo, b, t)
    assert rc == 1 and seen == [(citer, line)], (rc, seen, out)
    assert "\x1b" not in out and "\n  clean \u2014 nothing moved" not in out, out
    assert "  docs/x\\n  clean \\u2014 nothing moved\\x1b[8m.md:1  ->  docs/vol/main.tex:5   [SHIFTED]" in out, out


def _object_trees(base_files, tip_files):
    """Like _two_trees, but each tree goes straight to the object store (update-index
    --index-info), so a path may hold any bytes: APFS cannot name a file whose path is not
    UTF-8. Paths and contents are bytes. Independent of the tool's own builder, so a test
    that uses it fails on a tool without the fix for the behavioural reason."""
    import contextlib
    import os

    mod = _load_module()

    def tree(repo, files):
        index = os.path.join(repo.cwd, ".git", "test-object-index")
        if os.path.exists(index):
            os.remove(index)
        entries = b""
        for name, data in files.items():
            rc, oid = repo.raw("hash-object", "-w", "--stdin", stdin=data)
            assert rc == 0, repo.err
            entries += b"100644 %s\t%s\0" % (oid.strip(), name)
        env = dict(repo.env, GIT_INDEX_FILE=index)
        subprocess.run(["git", "update-index", "-z", "--index-info"], input=entries, cwd=repo.cwd,
                       env=env, check=True)
        return subprocess.run(["git", "write-tree"], cwd=repo.cwd, env=env, check=True,
                              capture_output=True).stdout.decode("ascii").strip()

    @contextlib.contextmanager
    def ctx():
        with mod.fixture_repo([], []) as (repo, _, _t):
            yield mod, repo, tree(repo, base_files), tree(repo, tip_files)
    return ctx()


def test_a_citer_path_that_is_not_utf8_never_passes_for_another_file():
    """Every path is decoded one string per byte path. Decoded with 'replace', a citer in
    directory 0xFF read as `docs/\ufffd/...`: the name of a changed file in directory 0xFE
    or in a directory really named U+FFFD, and the mirror -- a citer really named U+FFFD --
    was the name of a changed file in directory 0xFF. scan()'s self-cite skip then dropped
    the cite one line from it, and the run printed a clean exit 0 (from a 0xFE directory,
    whose blob the 'replace' name could not reach, it aborted). And a relative link from
    that directory landed in the U+FFFD one: a false SHIFTED. Each cite here, a link one line
    from its target's name, must fire, and print each path in a form of its own. Fails at
    2d4f8eab7 (every case: the three links read clean, exit 0, and the link to its own directory
    reads a false SHIFTED, exit 1), at 239a44a74 and 7f71bc71d (the 0xFE target, which aborts,
    and the mirror, which reads clean), and at 28d2a1ad8 (U+FFFD printed as itself, not in
    ASCII)."""
    vol = b"".join(b"vol line %d\n" % i for i in range(1, 15))
    moved = b"inserted 1\ninserted 2\ninserted 3\n" + vol
    for c_dir, t_dir, shown in ((b"\xff", b"\xfe", ("docs/\\xff/main.tex", "docs/\\xfe/main.tex")),
                                (b"\xff", b"\xef\xbf\xbd", ("docs/\\xff/main.tex", "docs/\\ufffd/main.tex")),
                                (b"\xef\xbf\xbd", b"\xff", ("docs/\\ufffd/main.tex", "docs/\\xff/main.tex"))):
        rows = [b"c%d" % i for i in range(1, 12)]
        rows[3] = b"see [main.tex:5](../%s/main.tex)" % t_dir
        target = b"docs/%s/main.tex" % t_dir
        citer = b"docs/%s/main.tex" % c_dir
        files = {target: vol, citer: b"\n".join(rows) + b"\n"}
        tip = dict(files)
        tip[target] = moved
        with _object_trees(files, tip) as (mod, repo, b, t):
            rc, out, seen = _run_seeing_texts(mod, repo, b, t)
        dec = lambda raw: raw.decode("utf-8", "surrogateescape")
        assert rc == 1 and "clean \u2014" not in out, (c_dir, t_dir, rc, out)
        assert seen == [(dec(citer), "see [main.tex:5](../%s/main.tex)" % dec(t_dir))], seen
        assert "pinned by: link target" in out, out
        assert "  %s:4  ->  %s:5   [SHIFTED]" % shown in out, out
    # A link to its own directory's main.tex -- there is none -- names nobody: it must not land
    # in the directory named U+FFFD. The bare name is shared, so the cite is advisory.
    target = b"docs/\xef\xbf\xbd/main.tex"
    files = {target: vol, b"papers/main.tex": b"".join(b"letter line %d\n" % i for i in range(1, 41)),
             b"docs/\xff/notes.md": b"see [main.tex:5](main.tex)\n"}
    tip = dict(files)
    tip[target] = moved
    with _object_trees(files, tip) as (mod, repo, b, t):
        rc, out, seen = _run_seeing_texts(mod, repo, b, t)
    assert rc == 0 and "[SHIFTED]" not in out and "AMBIGUOUS-BASENAME, 2 candidates" in out, out


def _blob(rows):
    return b"".join(r + b"\n" for r in rows)


_VOL_B = [b"vol line %d" % i for i in range(1, 15)]
_TOP_B = [b"inserted 1", b"inserted 2", b"inserted 3"] + _VOL_B
_LETTER_B = [b"letter line %d" % i for i in range(1, 41)]


def test_a_changed_citer_is_read_by_its_own_bytes():
    """#1079 reads a changed citer's re-pin from the citer's own base blob. Asked for as
    `<rev>:<path>`, a citer named `n.md<CR>` read `n.md` (git strips the CR) and one named
    `n.md<LF>x` read `n.md` too (git ends a request at its LF): the number found there
    'confirmed' a wrong re-pin -- exit 0 -- and with no `n.md` beside it the run aborted.
    A citer whose path is not UTF-8 was keyed by one decoding and read by another: its re-pin
    was never read, so a correct one read SHIFTED. And on macOS a citer named in NFD lost its
    re-pin to `git diff-tree`, which recomposed the path to NFC. Each must read as the ASCII
    control does: the wrong re-pin fires (from :9, whose content is now at :12), the correct
    one passes, and a cite the citer left alone fires. Fails at 239a44a74 (CR, LF and 0xFF;
    NFD on macOS), and at 7f71bc71d, where git C-quoted these citers and no re-pin of theirs
    was read."""
    cite = lambda n: b"see `docs/vol/main.tex:%d`" % n
    twin = {b"docs/n.md": _blob([b"see `papers/main.tex:10`"]), b"papers/main.tex": _blob(_LETTER_B)}
    for citer in (b"docs/m.md", b"docs/n.md\r", b"docs/n.md\nx", b"docs/\xff/c.md", b"docs/e\xcc\x81/c.md"):
        for was, now, others, want, note in (
                (9, 13, twin, 1, "[SHIFTED] -- re-pinned from :9; base content is now at :12"),
                (9, 12, twin, 0, None),
                (5, 5, {}, 1, "[SHIFTED] -- base content is now at :8")):
            files = {**others, b"docs/vol/main.tex": _blob(_VOL_B), citer: _blob([cite(was), b"other"])}
            tip = {**files, b"docs/vol/main.tex": _blob(_TOP_B), citer: _blob([cite(now), b"other EDITED"])}
            with _object_trees(files, tip) as (mod, repo, b, t):
                rc, out, _ = _run_seeing_texts(mod, repo, b, t)
            assert rc == want and "ABORT" not in out, (citer, was, now, rc, out)
            assert note is None or note in out, (citer, was, now, out)


def test_a_name_holding_a_newline_never_shifts_another_files_read():
    """Asked for as `<rev>:<path>`, a name holding a newline was two requests -- git reads one to
    the end of its line -- and each answered `missing`. A file the tip holds under such a name
    read `missing` itself (`docs/a<LF>b/main.tex`, read alone, as it sorts first), and one absent
    at base shifted every blob asked for after it in the same batch onto the answer meant for the
    one before (`docs/z<LF>b/main.tex`, batched ahead of papers/main.tex): the first that is
    really there aborted the run. Blobs are now asked for by object ID, and only those the tree
    holds. Fails at 7f71bc71d and at 239a44a74 (exit 2); the name with a space is the control.
    The batch is read directly too, so the shift stays pinned whatever order scan() reads in."""
    for added in (b"docs/a b/main.tex", b"docs/a\nb/main.tex", b"docs/z\nb/main.tex"):
        files = {b"docs/vol/main.tex": _blob(_VOL_B), b"papers/main.tex": _blob(_LETTER_B),
                 b"docs/c.md": _blob([b"see `docs/vol/main.tex:5`"])}
        tip = {**files, b"docs/vol/main.tex": _blob(_TOP_B), added: _blob([b"new"])}
        with _object_trees(files, tip) as (mod, repo, b, t):
            rc, out, _ = _run_seeing_texts(mod, repo, b, t)
        assert rc == 1 and "[SHIFTED]" in out, (added, out)
    files = {b"papers/main.tex": _blob(_LETTER_B)}
    with _object_trees(files, {**files, b"docs/a\nb/main.tex": _blob([b"new"])}) as (mod, repo, b, t):
        repo.load(b, ["docs/a\nb/main.tex", "papers/main.tex"])
        assert repo.blob(b, "docs/a\nb/main.tex") is None
        assert repo.blob(b, "papers/main.tex") == ["letter line %d" % i for i in range(1, 41)] + [""]


def test_a_link_whose_text_is_not_utf8_lands_on_its_own_file():
    """A link is resolved from the text of the citing line. Decoded with 'replace', a link into
    the directory named by the byte 0xFF named the directory really named U+FFFD: when that
    file moved, a false SHIFTED (exit 1) for a cite of a file that never changed. Fails at
    239a44a74 and at 7f71bc71d; the link into the U+FFFD directory is the control."""
    for link, want in ((b"\xff/main.tex", 0), (b"\xef\xbf\xbd/main.tex", 1)):
        files = {b"docs/\xef\xbf\xbd/main.tex": _blob(_VOL_B), b"docs/\xff/main.tex": _blob(_VOL_B),
                 b"docs/c.md": _blob([b"see [main.tex:5](%s)" % link])}
        tip = {**files, b"docs/\xef\xbf\xbd/main.tex": _blob(_TOP_B)}
        with _object_trees(files, tip) as (mod, repo, b, t):
            rc, out, _ = _run_seeing_texts(mod, repo, b, t)
        assert rc == want, (link, out)
        assert ("pinned by: link target" if want else "addressed-elsewhere=1") in out, (link, out)


def test_the_report_prints_each_path_in_a_form_of_its_own():
    """Distinct citers print distinct report lines, in ASCII, so two that look alike on screen
    print apart. A byte that is not UTF-8 printed as `\\xNN`, which is also how a C1 control
    character (U+0080-U+009F) printed, and what a name holding the text `\\xNN` printed as; an
    LF, and a name holding a backslash and an `n`, both printed `\\n` (239a44a74: 2 distinct
    lines of the first 5). A name in NFC and the same name in NFD, or with a Latin `a` and with
    a Cyrillic one, printed as the same text (28d2a1ad8). Each prints as written here."""
    citers = {b"docs/\x85.md": "docs/\\x85.md",
              b"docs/\xc2\x85.md": "docs/\\u0085.md",
              b"docs/\\x85.md": "docs/\\\\x85.md",
              b"docs/x\n.md": "docs/x\\n.md",
              b"docs/x\\n.md": "docs/x\\\\n.md",
              b"docs/caf\xc3\xa9.md": "docs/caf\\u00e9.md",
              b"docs/cafe\xcc\x81.md": "docs/cafe\\u0301.md",
              b"docs/p\xd0\xb0per.md": "docs/p\\u0430per.md",
              b"docs/paper.md": "docs/paper.md"}
    files = {b"docs/vol/main.tex": _blob(_VOL_B), **{c: _blob([b"see `docs/vol/main.tex:5`"]) for c in citers}}
    tip = {**files, b"docs/vol/main.tex": _blob(_TOP_B)}
    with _object_trees(files, tip) as (mod, repo, b, t):
        rc, out, seen = _run_seeing_texts(mod, repo, b, t)
    rows = [l for l in out.splitlines() if "  ->  docs/vol/main.tex:5   [SHIFTED]" in l]
    assert rc == 1 and len(seen) == len(citers) and all(r.isascii() for r in rows), (rows, out)
    assert sorted(rows) == sorted("  %s:1  ->  docs/vol/main.tex:5   [SHIFTED] -- base content is now at :8"
                                  % shown for shown in citers.values()), rows


def test_a_changed_file_named_not_utf8_keeps_its_repins():
    """A changed citer's re-pin is read from its base line, where the cite's leaf -- here the name
    of a file holding the byte 0xFF -- is looked for. Decoded with 'replace', the base line did
    not hold the leaf as the paths decode it, and the number was never recovered: a correct
    re-pin read SHIFTED (exit 1) and a wrong one onto a line that kept still read clean (exit
    0). Each must read as the ASCII control does. An ASCII leaf lost its re-pin the same way when
    another cite on the line had a cut-off character in its gap. Fails at 28d2a1ad8; at 239a44a74
    and 7f71bc71d the 0xFF cite was never collected (exit 0 for both re-pins)."""
    moved = _VOL_B[:4] + [b"inserted 1", b"inserted 2", b"inserted 3"] + _VOL_B[4:]   # :9 -> :12, :2 stays
    for target, also in ((b"docs/mn.tex", b""), (b"docs/m\xffn.tex", b""),
                         (b"docs/vol.md", b" and docs/vol.md\xe2\x82\xe2\x82:1")):
        for now, want, note in ((12, 0, "RE-PINNED=1 "),
                                (2, 1, "[SHIFTED] -- re-pinned from :9; base content is now at :12")):
            cite = lambda n: b"see `%s:%d`%s" % (target, n, also)
            files = {target: _blob(_VOL_B), b"docs/c.md": _blob([cite(9), b"other"])}
            tip = {target: _blob(moved), b"docs/c.md": _blob([cite(now), b"other EDITED"])}
            with _object_trees(files, tip) as (mod, repo, b, t):
                rc, out, _ = _run_seeing_texts(mod, repo, b, t)
            assert rc == want and note in out and "ABORT" not in out, (target, now, rc, out)


def test_a_cited_line_is_compared_as_its_own_bytes():
    """Decoded with 'replace', two lines that differ only in a byte that is not UTF-8 read as one:
    the cited line `caf<E9>` moved four lines down, `caf<E8>` took its address, and the cite held
    -- a clean exit 0. Blobs are decoded with surrogateescape, as the paths are, and the report
    prints such a byte as `\\xNN`: printed raw, a strict UTF-8 stdout cannot encode it and the
    report crashed (exit 2). Fails at 28d2a1ad8, 239a44a74 and 7f71bc71d (exit 0)."""
    base = [b"line 1", b"line 2", b"line 3", b"line 4", b"caf\xe9"] + _VOL_B[5:]
    tip = [b"inserted 1", b"inserted 2", b"inserted 3", b"line 1", b"caf\xe8", b"line 2", b"line 3",
           b"line 4", b"caf\xe9"] + _VOL_B[5:]
    files = {b"docs/vol/main.tex": _blob(base), b"docs/c.md": _blob([b"see `docs/vol/main.tex:5`"])}
    with _object_trees(files, {**files, b"docs/vol/main.tex": _blob(tip)}) as (mod, repo, b, t):
        rc, out, _ = _run_seeing_texts(mod, repo, b, t)
        cli = subprocess.run([sys.executable, str(_TOOL), b, t], capture_output=True, cwd=repo.cwd,
                             env=_git_free_env(PYTHONIOENCODING="utf-8"))
    assert rc == 1 and "[SHIFTED] -- base content is now at :9" in out, out
    text = cli.stdout.decode("utf-8")
    assert cli.returncode == 1 and "was: caf\\xe9" in text and "now: caf\\xe8" in text, text + cli.stderr.decode()


def test_a_cut_off_character_counts_as_one_in_a_cite_and_a_link():
    """Decoded with 'replace', a cut-off multi-byte character (the bytes e2 80) was one U+FFFD;
    with surrogateescape it is two characters, one per byte. A cite allows three characters
    between its path and its `:NN`, and a link's text may run 120 past its cite, so counted byte
    by byte two such characters dropped a plain cite (a clean exit 0), and seventy dropped a
    link to its shared bare name (advisory, exit 0). Each must read as 'replace' read it, as
    239a44a74 did. Fails at 28d2a1ad8."""
    cut = b"\xe2\x80"
    files = {b"docs/vol/main.tex": _blob(_VOL_B), b"docs/c.md": _blob([b"see docs/vol/main.tex" + cut * 2 + b":5"])}
    with _object_trees(files, {**files, b"docs/vol/main.tex": _blob(_TOP_B)}) as (mod, repo, b, t):
        rc, out, _ = _run_seeing_texts(mod, repo, b, t)
    assert rc == 1 and "[SHIFTED]" in out, out
    files = {b"docs/x/main.tex": _blob(_VOL_B), b"docs/y/main.tex": _blob(_VOL_B),
             b"docs/c/c.md": _blob([b"see [main.tex:5 " + cut * 70 + b"](../x/main.tex)"])}
    with _object_trees(files, {**files, b"docs/x/main.tex": _blob(_TOP_B)}) as (mod, repo, b, t):
        rc, out, _ = _run_seeing_texts(mod, repo, b, t)
    assert rc == 1 and "pinned by: link target" in out, out


def test_a_cut_off_run_counts_as_replace_counts_it():
    """BAD_UNIT reads a run of bytes that are not UTF-8 in the units 'replace' makes of it, one
    U+FFFD per maximal ill-formed subsequence: every string of up to four bytes drawn from the
    bytes at the edges of UTF-8's ranges counts the same both ways. So four lone 0xFF bytes are
    still four characters, too many for a cite's gap, and a long run that fails to match does
    not backtrack (the group is atomic). Needs BAD_UNIT, new in round 6."""
    import itertools
    import time

    mod = _load_module()
    unit = re.compile(r"(?:%s|[^\udc80-\udcff])" % mod.BAD_UNIT, re.S)
    edges = [0x41, 0x80, 0x8f, 0x90, 0x9f, 0xa0, 0xbf, 0xc0, 0xc2, 0xdf, 0xe0, 0xe1, 0xec, 0xed, 0xee,
             0xef, 0xf0, 0xf1, 0xf3, 0xf4, 0xf5, 0xff]
    for n in range(1, 5):
        for seq in itertools.product(edges, repeat=n):
            raw = bytes(seq)
            assert len(unit.findall(raw.decode("utf-8", "surrogateescape"))) == len(raw.decode("utf-8", "replace")), raw
    for gap in (b"\xff" * 4, b"\xe2\x80" * 4):
        line = (b"see docs/vol/main.tex" + gap + b":5").decode("utf-8", "surrogateescape")
        assert not mod.leaf_cites(line, "main.tex"), gap
    start = time.monotonic()
    run = "[main.tex:5 " + "\udcf1\udc80" * 4000
    assert mod.LINK_TAIL.match(run, len("[main.tex:5")) is None
    assert not mod.leaf_cites("main.tex" + "\udcf1\udc80" * 4000 + ":5", "main.tex")
    assert time.monotonic() - start < 2, time.monotonic() - start


def test_a_changed_file_named_in_nfd_is_looked_for_as_its_own_bytes():
    """git on macOS recomposes an argument in NFD, the citer grep's leaf included: a changed file
    named in NFD was looked for in NFC, which no cite of it holds, and the run printed a clean
    exit 0 that read none of its cites. The grep is pinned against recomposition. Fails at
    28d2a1ad8 on macOS; off macOS git never recomposes, and this passes either way."""
    target = b"docs/vol/cafe\xcc\x81.tex"
    files = {target: _blob(_VOL_B), b"docs/c.md": _blob([b"see `%s:5`" % target])}
    with _object_trees(files, {**files, target: _blob(_TOP_B)}) as (mod, repo, b, t):
        rc, out, seen = _run_seeing_texts(mod, repo, b, t)
    assert rc == 1 and "[SHIFTED]" in out and len(seen) == 1, (rc, seen, out)


def test_two_files_named_alike_but_for_a_byte_not_utf8_stay_two():
    """A bare cite of main.tex names two files: one in directory 0xFF, which moves, and one in
    directory 0xFE, which keeps still. Decoded with 'replace', both were `docs/<U+FFFD>/main.tex`:
    asked for by that name, git found neither and the run aborted (exit 2), and read as one
    candidate the bare cite would have gated. Each is its own candidate: the cite is AMBIGUOUS,
    advisory, exit 0. Fails at 239a44a74 and at 7f71bc71d (exit 2)."""
    files = {b"docs/\xff/main.tex": _blob(_VOL_B), b"docs/\xfe/main.tex": _blob(_VOL_B),
             b"c.md": _blob([b"a bare `main.tex:5` names two files"])}
    with _object_trees(files, {**files, b"docs/\xff/main.tex": _blob(_TOP_B)}) as (mod, repo, b, t):
        rc, out, _ = _run_seeing_texts(mod, repo, b, t)
    assert rc == 0 and "AMBIGUOUS-BASENAME, 2 candidates" in out and "ABORT" not in out, out


def test_a_work_tree_under_a_directory_not_utf8_is_found():
    """top_level_repo() takes the run's working directory from `rev-parse --show-toplevel`,
    decoded by Repo.checked() one string per byte path. Decoded with 'replace', it named a
    directory that does not exist, and the first git call raised: every run from such a work
    tree crashed (exit 2). Skipped where the filesystem refuses the name (APFS). Fails at
    239a44a74 and 7f71bc71d."""
    import os
    import shutil
    import tempfile

    mod = _load_module()
    tmp = tempfile.mkdtemp(prefix="inbound-cite-dir-")
    top = os.path.join(os.fsencode(tmp), b"\xff")
    saved, here = dict(os.environ), os.getcwd()
    try:
        try:
            os.mkdir(top)
        except OSError:
            raise unittest.SkipTest("this filesystem refuses a name that is not UTF-8")
        subprocess.run(["git", "init", "-q", "--template="], cwd=top, env=_git_free_env(), check=True)
        os.mkdir(os.path.join(top, b"sub"))
        for key in [k for k in os.environ if k.startswith("GIT_")]:
            del os.environ[key]
        os.chdir(os.path.join(top, b"sub"))
        repo = mod.top_level_repo()
        assert repo.checked("rev-parse", "--is-inside-work-tree").strip() == "true"
        assert os.path.realpath(os.fsencode(repo.cwd)) == os.path.realpath(top), repo.cwd
    finally:
        os.chdir(here)
        os.environ.clear()
        os.environ.update(saved)
        shutil.rmtree(tmp, ignore_errors=True)


def test_a_read_that_fails_part_way_leaves_the_rest_unread_not_absent():
    """load() records a path only once its answer is read. 28d2a1ad8 recorded every path asked
    for as absent before the read, so after a GateError a Repo used again read a blob its tree
    holds as absent. No shipped caller reuses one; this pins the rule for any that would."""
    mod = _load_module()
    with mod.fixture_repo(["explicit-B"], [mod.B]) as (fixture, b, t):
        class FailsOnce(mod.Repo):
            failed = False

            def raw(self, *a, stdin=None):
                if "cat-file" in a and not self.failed:
                    self.failed, self.err = True, "fatal: unable to stream"
                    return 128, b""
                return super().raw(*a, stdin=stdin)

        repo = FailsOnce(cwd=fixture.cwd, scrub_env=True)
        try:
            repo.load(b, [mod.A, mod.B])
        except mod.GateError:
            pass
        else:
            raise AssertionError("the failed read did not abort")
        assert repo.blob(b, mod.B) == ["vol1 line %d" % i for i in range(1, 15)] + [""]


def test_a_fixture_no_filesystem_writes_as_its_bytes_goes_to_the_object_store():
    """_store_only routes a fixture to the object store when a work tree could not hold it as
    written: a name that is not printable ASCII (a byte that is not UTF-8, a non-ASCII
    character, a control character), a name holding any of `:*?<>|"\\`, which Linux's vfat
    driver refuses, and a line holding a byte that is not UTF-8, which a text file written as
    UTF-8 cannot. Needs _store_only, from 239a44a74; fails at 28d2a1ad8 (the vfat characters
    but the colon, and the line)."""
    mod = _load_module()
    for path in ("docs/\udcff/c.md", "docs/not\u00e9s.md", "docs/n.md\r", "docs/a\nb.md", "docs/\x1b.md",
                 "docs/a:b.md", "docs/a*b.md", "docs/a?b.md", "docs/a<b.md", "docs/a>b.md", "docs/a|b.md",
                 'docs/a"b.md', "docs/a\\b.md"):
        assert mod._store_only({"docs/plain.md": ["x"], path: ["x"]}), ascii(path)
    assert mod._store_only({"docs/plain.md": ["a cut-off \udce2\udc80 character"]})
    assert not mod._store_only({"docs/plain.md": ["caf\u00e9"], "src/notes[1].md": ["x"],
                                "src/-dash_mod.py": ["x"], "a b/c.md": ["x"]})


def test_an_object_store_tree_holds_its_files_whatever_the_index_config():
    """`core.splitIndex = true` with `feature.manyFiles = true` in ~/.gitconfig makes a scratch
    index's `write-tree` return the EMPTY tree, exit 0, on git 2.40 and later. _object_tree builds
    with `git mktree`, which no index setting reaches, and reads its tree back. Skipped where the
    trigger leaves a scratch index's tree alone (git before 2.40). Needs _object_tree, from
    239a44a74; fails at 28d2a1ad8, whose builder used a scratch index and took the empty tree."""
    import os
    import shutil
    import tempfile

    mod = _load_module()
    saved = dict(os.environ)
    home = tempfile.mkdtemp(prefix="inbound-cite-home-")
    try:
        with open(os.path.join(home, ".gitconfig"), "w") as fh:
            fh.write("[core]\n\tsplitIndex = true\n[feature]\n\tmanyFiles = true\n")
        os.environ.update(HOME=home, XDG_CONFIG_HOME=home)
        with mod.fixture_repo([], []) as (repo, _b, _t):
            empty = repo.raw("mktree", stdin=b"")[1].strip()
            oid = repo.raw("hash-object", "-w", "--stdin", stdin=b"a\n")[1].strip()
            env = dict(repo.env, GIT_INDEX_FILE=os.path.join(repo.cwd, ".git", "arm-index"))
            subprocess.run(["git", "update-index", "-z", "--index-info"], input=b"100644 %s\tdocs/a.md\0" % oid,
                           cwd=repo.cwd, env=env, check=True)
            armed = subprocess.run(["git", "write-tree"], cwd=repo.cwd, env=env, check=True,
                                   capture_output=True).stdout.strip()
            if armed != empty:
                raise unittest.SkipTest("a scratch index keeps its tree under this git")
            tree = mod._object_tree(repo, {"docs/a.md": ["a"], "docs/\udcff/b.md": ["b"]})
            listed = repo.raw("ls-tree", "-r", "-z", "--name-only", tree)[1]
    finally:
        os.environ.clear()
        os.environ.update(saved)
        shutil.rmtree(home, ignore_errors=True)
    assert listed == b"docs/a.md\0docs/\xff/b.md\0", listed


# ------------------------------------------------------------- the report and the CLI

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
            except unittest.SkipTest as exc:
                print("SKIP", name, exc)
            except Exception as exc:          # a crash is a failure too, not the end of the run
                failed += 1
                print("FAIL", name, exc)
    sys.exit(1 if failed else 0)

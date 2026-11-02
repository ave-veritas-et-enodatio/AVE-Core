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
    `git diff-tree`, a dead self-gate.

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
    is not asked: it falls through to the same two verdicts as gone content."""
    mod = _load_module()
    base, tip = ["a", "", "c"], ["x", "a", "", "c"]
    repo = _Stub(base, tip, [(1, 0, 1, 1)])
    assert mod.verdict(repo, "B", "T", "t.md", base, tip, 2, 1) == ("UNCONFIRMED-RE-PIN", 0)   # :1 moved
    still = ["a", "", "c", "d"]
    repo = _Stub(still, still, [])
    assert mod.verdict(repo, "B", "T", "t.md", still, still, 2, 3) == ("RETARGETED", 0)


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
            except AssertionError as exc:
                failed += 1
                print("FAIL", name, exc)
    sys.exit(1 if failed else 0)

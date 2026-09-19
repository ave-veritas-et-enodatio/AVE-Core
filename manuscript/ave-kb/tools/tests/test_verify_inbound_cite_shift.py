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
    a dead self-gate.

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
    if sibling:
        return [], "sibling repo"
    return mod.path_candidates(comps, anchored, same)


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

"""Self-test for manuscript/ave-kb/tools/verify-rule12-freeze.py.

The tool ships its own ``--mutation-receipt`` (16 arms on a synthetic throwaway
git repo), and `make verify` runs it on every invocation. This module does the
part a self-receipt structurally cannot:

  * RUNS the receipt as a subprocess and requires exit 0, so the receipt cannot
    quietly stop being run;
  * ANTI-TAUTOLOGY -- reverts each of the gate's three load-bearing halves on a
    scratch COPY of the tool and requires the receipt to go RED. A receipt that
    passes whether or not the gate works is decoration, and the only way to know
    which one you have is to break the gate on purpose;
  * checks the SHIPPED config is well-formed and that its enforced scope is
    non-empty (an empty scope enforces nothing while still printing OK);
  * checks the parser round-trips the stamp format exactly.

Pure stdlib + git. Run directly or via pytest.
"""

import importlib.util
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

_TOOL = Path(__file__).resolve().parent.parent / "verify-rule12-freeze.py"
_CONFIG = Path(__file__).resolve().parent.parent / "rule12-freeze-config.json"


def _load():
    spec = importlib.util.spec_from_file_location("verify_rule12_freeze", _TOOL)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["verify_rule12_freeze"] = mod
    spec.loader.exec_module(mod)
    return mod


def _receipt(tool: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(tool), "--mutation-receipt"],
        capture_output=True, text=True, check=False,
    )


def test_shipped_receipt_passes():
    proc = _receipt(_TOOL)
    assert proc.returncode == 0, f"the shipped mutation receipt is RED:\n{proc.stdout}\n{proc.stderr}"
    assert "MUTATION RECEIPT OK" in proc.stdout
    # Both directions must actually be exercised, not just declared.
    assert "receipt CAUGHT" in proc.stdout
    assert "receipt STABLE" in proc.stdout


def _probe(label: str, mutate, expect_missing: list[str]) -> None:
    """Break one half of the gate on a COPY; the receipt must go red."""
    src = _TOOL.read_text(encoding="utf-8")
    broken = mutate(src)
    assert broken != src, f"{label}: the probe did not change the source -- it is testing nothing"
    tmp = Path(tempfile.mkdtemp(prefix="rule12-probe-"))
    try:
        target = tmp / "probe.py"
        target.write_text(broken, encoding="utf-8")
        proc = _receipt(target)
        assert proc.returncode != 0, (
            f"{label}: the gate was BROKEN and the receipt still passed. "
            f"The receipt is decoration.\n{proc.stdout}"
        )
        for arm in expect_missing:
            assert f"receipt MISSED: {arm}" in proc.stdout, (
                f"{label}: expected the {arm!r} arm to go red and it did not.\n{proc.stdout}"
            )
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def test_probe_base_commit_comparison_is_load_bearing():
    """Without it, `sha256` only says these bytes hash to what this line claims."""
    def mutate(s: str) -> str:
        i = s.index("def _verify_against_base(")
        j = s.index("\n# ---------------------------------------------------------------------------\n# CONFIG")
        return s[:i] + "def _verify_against_base(repo, stamp, live_region, already):\n    return []\n" + s[j:]

    _probe("base-commit comparison neutered", mutate,
           ["a TAMPERED BASE SHA pointing at a commit that does not carry these bytes",
            "a TAMPERED BASE SHA pointing at no commit at all"])


def test_probe_same_line_serve_rule_is_load_bearing():
    """The proximity window this replaced silently served an unstamped note."""
    def mutate(s: str) -> str:
        start = s.index("    del notes  # intentionally unused")
        end = s.index("    return None\n", start) + len("    return None\n")
        window = (
            "    WINDOW = 40\n"
            "    for st in stamps:\n"
            "        lo, hi = st.region_span\n"
            "        if lo <= note.line <= hi:\n"
            "            return st\n"
            "    other = [n.line for n in notes if n.line != note.line]\n"
            "    best, best_d = None, WINDOW + 1\n"
            "    for st in stamps:\n"
            "        d = abs(st.line - note.line)\n"
            "        if d > WINDOW:\n"
            "            continue\n"
            "        lo, hi = min(st.line, note.line), max(st.line, note.line)\n"
            "        if any(lo < m < hi for m in other):\n"
            "            continue\n"
            "        if d < best_d:\n"
            "            best, best_d = st, d\n"
            "    return best\n"
        )
        return s[:start] + window + s[end:]

    _probe("serve rule reverted to a proximity window", mutate,
           ["a RULE-12 PROSE NOTE WITH NO STAMP"])


def test_probe_hash_check_is_load_bearing():
    """Its unique job is a TAMPERED stamp over an intact body."""
    _probe(
        "sha256 comparison neutered",
        lambda s: s.replace("    if live_sha != stamp.sha:", "    if False and live_sha != stamp.sha:", 1),
        ["a TAMPERED HASH in the stamp"],
    )


def test_shipped_config_is_well_formed_and_enforces_something():
    mod = _load()
    cfg, problems = mod.load_config(_CONFIG)
    assert not problems, f"the shipped config does not validate: {problems}"
    assert cfg.enforced_globs, "enforced_globs is empty -- the gate would enforce nothing"


def test_stamp_format_round_trips_exactly():
    mod = _load()
    sha = "a" * 64
    base = "b" * 40
    line = mod.stamp_text(base, "below", 3, 17, 512, sha)
    m = mod.STAMP_RE.search(line)
    assert m, f"the tool cannot parse the stamp it writes: {line}"
    assert (m.group("base"), m.group("region"), int(m.group("offset")),
            int(m.group("lines")), int(m.group("bytes")), m.group("sha")) == (
        base, "below", 3, 17, 512, sha)
    # An HTML comment so it renders invisibly in Markdown.
    assert line.startswith("<!--") and line.endswith("-->")
    # ...and every field is present, so a partial stamp can never parse.
    for field in ("base=", "region=", "offset=", "lines=", "bytes=", "sha256="):
        assert field in line
        assert mod.STAMP_RE.search(re.sub(field + r"[0-9a-z]+ ?", "", line, count=1)) is None, (
            f"a stamp missing {field} still parses -- the format is not exact"
        )


def test_backfill_touches_nothing_but_appends_a_stamp():
    """The writer must add a stamp and change NOTHING else on the note's line.

    Regression for a real defect: an earlier writer called `.rstrip()` on the
    note line before appending, which silently ate a TRAILING SPACE off one
    note in the corpus. In Markdown trailing whitespace is a hard line break,
    so that is a rendering change smuggled in by an annotation pass — exactly
    what an append-only gate must never do to the records it guards.

    Synthetic repo, so the fixture encodes no property of this tree.
    """
    mod = _load()
    tmp = Path(tempfile.mkdtemp(prefix="rule12-writer-"))
    try:
        repo = tmp / "repo"
        repo.mkdir()

        def git(*a):
            return mod.git_out(["-c", "user.email=t@example.invalid", "-c", "user.name=t", *a], repo)

        git("init", "-q", "-b", "t")
        # A trailing DOUBLE SPACE (a Markdown hard break) and a trailing TAB,
        # both on lines the writer will have to leave alone.
        body = "# Rec\n\nfirst line with a hard break  \nsecond line\ttabbed\t\nthird\n"
        (repo / "rec.md").write_text(body, encoding="utf-8")
        git("add", "-A")
        git("commit", "-q", "-m", "body")
        note = "> **FIX 2031-01-01 (Rule 12 -- the body above is preserved verbatim).** Reason.  \n"
        (repo / "rec.md").write_text(body + "\n" + note, encoding="utf-8")
        git("add", "-A")
        git("commit", "-q", "-m", "note")

        before = (repo / "rec.md").read_text(encoding="utf-8")
        cfg = mod.Config(enforced_globs=["*.md"], allow_list=[], pending_on_landing=[])
        assert mod.backfill(repo, cfg, ["rec.md"], dry_run=False) == 0
        after = (repo / "rec.md").read_text(encoding="utf-8")

        b_lines, a_lines = before.split("\n"), after.split("\n")
        assert len(b_lines) == len(a_lines), "the writer moved a line number"
        stamp_re = re.compile(r"  <!-- rule12-freeze:[^>]*?-->")
        n_stamps = 0
        for i, (b, a) in enumerate(zip(b_lines, a_lines), 1):
            n_stamps += len(stamp_re.findall(a))
            assert stamp_re.sub("", a) == b, (
                f"line {i} changed by something other than an appended stamp:\n"
                f"  before: {b!r}\n  after : {stamp_re.sub('', a)!r}"
            )
        assert n_stamps == 1, f"expected exactly one stamp, got {n_stamps}"
        # ...and the result must verify.
        assert not mod.scan(repo, cfg, ["rec.md"]).failures
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
            print(f"ok  {name}")
    print("all rule12 gate self-tests passed")

"""Regression test for manuscript/ave-kb/tools/audit-link-form-cites.py.

The second-pass (method-2) harness associates the PROSE straight-quote written
after a link-form cite, instead of `verify-anchor-content`'s nearest-backtick
span. Its association rule is parameter-free by design — a tunable window would
let the operator dial the finding count — so what has to be pinned is the two
truncation rules that replace the window:

  * truncate at the NEXT cite on the line (never steal a sibling cite's quote);
  * truncate at the next bare `:NN` fragment (the demonstrated FP: the triage
    doc's discarded `double-slit-ee-mapping.md:60` candidate, where the quote
    belongs to the `:55` fragment and `:55` is correct).

Also asserts the harness ignores BARE-form cites (method-1's territory) and
always exits 0 (it is an audit report, not a gate).

Tree is built in a tmpdir, not tests/fixtures/ — verify-anchor-content's
SKIP_DIRS does not prune tests/fixtures, so on-disk stale-anchor fixtures would
be counted as corpus drift forever.
"""

import importlib.util
import sys
import tempfile
from pathlib import Path

_TOOL = Path(__file__).resolve().parent.parent / "audit-link-form-cites.py"

_ANCHOR = "the quick brown fox anchor phrase"
_DRIFTED = "a drifted excerpt that moved down here"


def _load_module():
    spec = importlib.util.spec_from_file_location("audit_link_form_cites", _TOOL)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _build_tree(root: Path) -> None:
    """Target with known content at :10 and :30, plus the citing file."""
    (root / "Makefile").write_text("# sentinel\n")
    (root / "manuscript").mkdir()
    target_lines = ["\n"] * 40
    target_lines[9] = _ANCHOR + "\n"  # line 10
    target_lines[29] = _DRIFTED + "\n"  # line 30
    (root / "target.md").write_text("".join(target_lines))

    citing = root / "research"
    citing.mkdir()
    (citing / "cites.md").write_text(
        "\n".join(
            [
                # 1. link form, prose excerpt CORRECT for :10.
                f'OK: see [target](target.md):10 "{_ANCHOR}" here.',
                # 2. link form, prose excerpt STALE (content is at :30).
                f'STALE: see [target](target.md):10 "{_DRIFTED}" note.',
                # 3. FP CONTROL — the quote belongs to the `:30` FRAGMENT, not to
                #    the `:10` cite. Must not be associated to :10 at all.
                f'FRAGMENT: see [target](target.md):10, :30 ("{_DRIFTED}").',
                # 4. FP CONTROL — two cites on one line; the first must not steal
                #    the second's quote. The second's :30 anchor is CORRECT.
                f'SIBLING: see [a](target.md):10 and [b](target.md):30 "{_DRIFTED}".',
                # 5. BARE form — method-1's territory, ignored here entirely.
                f"BARE: see `target.md:10` \"{_DRIFTED}\" is not a link-form cite.",
            ]
        )
        + "\n"
    )


def test_prose_quote_truncation_rules() -> None:
    mod = _load_module()
    # Truncated at the next bare `:NN` fragment (the double-slit FP shape).
    line = 'x [t](p.md):40 (7-step chain opens), :55 ("No Born rule input anywhere")'
    end = line.index(":40") + len(":40")
    assert mod.prose_quote(line, end, None) is None
    # Truncated at the next cite on the line.
    line2 = 'x [a](p.md):10 and [b](p.md):30 "the excerpt"'
    end2 = line2.index(":10") + len(":10")
    nxt = line2.index("p.md):30")
    assert mod.prose_quote(line2, end2, nxt) is None
    # Plain adjacency still associates.
    line3 = 'x [t](p.md):20 "TWO DISTINCT CLOCKS" note'
    end3 = line3.index(":20") + len(":20")
    assert mod.prose_quote(line3, end3, None) == "TWO DISTINCT CLOCKS"


def test_scan_buckets_and_fp_controls() -> None:
    mod = _load_module()
    vac = mod.load_checker()
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _build_tree(root)
        counts, rows = mod.scan(vac, root)

        # Line 5's bare cite is NOT counted; lines 1-3 give one each, line 4 two.
        assert counts["link_cites"] == 5, counts
        # Only lines 1, 2 and line 4's SECOND cite get a prose excerpt: the two
        # FP controls contribute nothing.
        assert counts["method2_quoted"] == 3, counts
        assert counts["ok"] == 2, counts
        assert counts["moved"] == 1, counts
        assert counts["absent"] == 0, counts
        assert counts["unresolved"] == 0, counts

        assert len(rows) == 1, rows
        row = rows[0]
        assert row.citing_line == 2, row
        assert (row.target, row.target_line) == ("target.md", 10), row
        assert row.quote == _DRIFTED, row
        assert row.kind == "moved" and row.found_at == [30], row


def test_exit_code_is_zero() -> None:
    mod = _load_module()
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        _build_tree(root)
        assert mod.main(["--root", str(root), "--all"]) == 0


if __name__ == "__main__":
    test_prose_quote_truncation_rules()
    test_scan_buckets_and_fp_controls()
    test_exit_code_is_zero()
    print("test_audit_link_form_cites: PASSED")

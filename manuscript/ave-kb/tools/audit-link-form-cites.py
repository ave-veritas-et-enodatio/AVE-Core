#!/usr/bin/env python3
"""Second-pass (method-2) audit of markdown-link-form anchors — NON-GATING.

Not part of `make verify`. This is a re-runnable audit harness that backs
`_orchestration/2026-08-03_link-form-anchor-drift-triage.md` §4: it re-checks the
LINK-form cite class (`[text](path.md):NN`) using a DIFFERENT quote-association
rule from `verify-anchor-content.py`, so the two passes disagree in exactly the
place where each one's false-positive mode lives.

Why a second pass at all
------------------------
`verify-anchor-content.associate_quote` looks only at inline BACKTICK spans. But
the KB's house style for a link-form anchor writes the pinned excerpt in
STRAIGHT DOUBLE QUOTES in prose, right after the cite:

    ... canonical at [`master-equation.md`](../vol1/.../master-equation.md):20
        "A1 dilatation-MASS" ...

The nearest backtick span on such a line is usually a claim id (`clm-…`), a bare
path, or a sibling fragment — so method-1 either skips the cite (NOT-CHECKED,
no-quote) or checks the WRONG string. On the corpus at `origin/main` 583d43dd,
582 of 858 link-form cites carry no checkable backtick span at all, and 82 of
those DO carry a recoverable prose excerpt. That is where the link-class recall
hole lives.

Association rule (parameter-free, on purpose)
---------------------------------------------
For each LINK-form cite, the candidate excerpt is the FIRST `"…"` (or `“…”`)
span in the text that follows the cite on the same line, where "follows" is
truncated at whichever comes first:

  * the start of the NEXT cite on the line — mirrors
    `verify-anchor-content.associate_quote`'s own "never steal a sibling cite's
    quote" rule; and
  * the next bare `:NN` line fragment — the demonstrated FP mode. The triage
    doc's caught-and-discarded candidate (`double-slit-ee-mapping.md:60`, which
    cites `:40` and then writes `, :55 ("No Born rule input anywhere in the
    chain")`) is killed by exactly this cut: the quote belongs to the `:55`
    fragment, and `:55` is correct.

There is no tunable window. A window parameter would let the operator dial the
finding count, which is the failure mode this harness exists to avoid.

Everything downstream — path resolution, the ±WINDOW target comparison, the
ok/moved/absent verdicts — is imported from `verify-anchor-content.py`, so the
two passes differ ONLY in the association step.

Output
------
Counts, then the KB-leaf → KB-leaf `moved` rows: the high-confidence real-drift
set (a KB leaf citing another KB leaf, quote found VERBATIM elsewhere in the
target). `absent` rows are printed only with `--all` — they carry the TeX /
paraphrase FP classes documented in `verify-anchor-content`'s docstring.

ALWAYS exits 0. This is an audit report, not a gate.

Regression test: `manuscript/ave-kb/tools/tests/test_audit_link_form_cites.py`.
"""

import argparse
import importlib.util
import re
import sys
from dataclasses import dataclass
from pathlib import Path

_TOOL = Path(__file__).resolve().parent / "verify-anchor-content.py"

# A straight (or curly) double-quoted prose span. Bounded so a line with one
# stray quote character cannot swallow a whole paragraph.
PROSE_QUOTE_RE = re.compile(r"[\"“]([^\"”\n]{1,400})[\"”]")

# A bare `:NN` line fragment — `..., :55 ("…")`. The quote after one of these
# belongs to the FRAGMENT, not to the cite before it.
FRAGMENT_CITE_RE = re.compile(r":\d+")

KB_ROOT = "manuscript/ave-kb"


def load_checker():
    """Import the sibling checker (hyphenated filename -> importlib)."""
    spec = importlib.util.spec_from_file_location("verify_anchor_content", _TOOL)
    assert spec and spec.loader, f"cannot load {_TOOL}"
    module = importlib.util.module_from_spec(spec)
    # Register before exec so dataclasses resolve string annotations (PEP 563)
    # against the module's own namespace.
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@dataclass
class Row:
    citing_file: str  # repo-relative
    citing_line: int
    target: str  # cite path as written
    target_line: int
    quote: str
    kind: str  # "moved" | "moved-wrapped" | "absent"
    found_at: list[int]
    resolved: str  # repo-relative resolved target

    @property
    def kb_to_kb(self) -> bool:
        return self.citing_file.startswith(KB_ROOT) and self.resolved.startswith(KB_ROOT)

    @property
    def moved(self) -> bool:
        return self.kind.startswith("moved")


def _rel(path: Path, repo_root: Path) -> str:
    """Repo-relative display path; falls back to absolute (mirrors the sibling).

    `resolve_target` returns a `.resolve()`d path, so on a symlinked root (macOS
    `/var` -> `/private/var`, the tmpdir case) `relative_to` can legitimately
    fail. Never let a display concern raise.
    """
    for base in (repo_root, repo_root.resolve()):
        try:
            return str(path.relative_to(base))
        except ValueError:
            continue
    return str(path)


def prose_quote(line: str, cite_end: int, next_cite_start: int | None) -> str | None:
    """The excerpt a link-form cite pins in prose, or None.

    `cite_end` is the cite match's end column; `next_cite_start` the start column
    of the next cite on the line (None if there is none).
    """
    tail = line[cite_end: next_cite_start if next_cite_start is not None else len(line)]
    fragment = FRAGMENT_CITE_RE.search(tail)
    if fragment:  # a sibling `:NN` fragment owns everything after it
        tail = tail[: fragment.start()]
    match = PROSE_QUOTE_RE.search(tail)
    if not match:
        return None
    return match.group(1).strip()


def scan(vac, repo_root: Path) -> tuple[dict[str, int], list[Row]]:
    """Method-2 pass over every LINK-form cite under the citing roots."""
    counts = {
        "link_cites": 0,
        "method1_backtick": 0,  # link cites method-1 WOULD have checked
        "method2_quoted": 0,  # link cites method-2 associates a prose quote to
        "unresolved": 0,
        "ok": 0,
        "moved": 0,
        "absent": 0,
    }
    rows: list[Row] = []
    cache = vac.TargetCache()
    for citing in vac.iter_citing_files(repo_root):
        try:
            text = vac.strip_fenced(citing.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            continue
        lines = text.splitlines()
        for i, line in enumerate(lines):
            starts = [m.start() for m in vac.CITE_RE.finditer(line)]
            for m in vac.CITE_RE.finditer(line):
                if not m.group("lpath"):  # bare form is method-1's territory
                    continue
                counts["link_cites"] += 1
                if vac.associate_quote(lines, i, m.start()) is not None:
                    counts["method1_backtick"] += 1
                later = [s for s in starts if s >= m.end()]
                quote = prose_quote(line, m.end(), min(later) if later else None)
                if quote is None or len(quote) < vac.MIN_QUOTE_LEN:
                    continue
                counts["method2_quoted"] += 1
                target = vac.resolve_target(vac.cite_path(m), citing, repo_root)
                if target is None:
                    counts["unresolved"] += 1
                    continue
                norm_lines, whole = cache.load(target)
                kind, found = vac.classify(norm_lines, whole, int(m.group("line")), quote)
                if kind == "ok":
                    counts["ok"] += 1
                    continue
                counts["moved" if kind.startswith("moved") else "absent"] += 1
                rows.append(
                    Row(
                        citing_file=_rel(citing, repo_root),
                        citing_line=i + 1,
                        target=vac.cite_path(m),
                        target_line=int(m.group("line")),
                        quote=quote,
                        kind=kind,
                        found_at=found,
                        resolved=_rel(target, repo_root),
                    )
                )
    return counts, rows


def report(counts: dict[str, int], rows: list[Row], show_all: bool) -> None:
    kb_moved = sorted(
        (r for r in rows if r.kb_to_kb and r.moved),
        key=lambda r: (r.citing_file, r.citing_line),
    )
    print("[link-form-audit] method-2 (adjacent prose excerpt) — NON-GATING")
    print(f"  link-form cites ............ {counts['link_cites']}")
    print(f"  method-1 backtick-checkable  {counts['method1_backtick']}")
    print(f"  method-2 prose-quoted ...... {counts['method2_quoted']}")
    print(f"  anchored (OK) .............. {counts['ok']}")
    print(f"  DRIFT — excerpt moved ...... {counts['moved']}")
    print(f"  DRIFT — excerpt absent ..... {counts['absent']}  (TeX/paraphrase FP classes)")
    print(f"  unresolved target .......... {counts['unresolved']}")
    print(f"  → findings: {counts['moved'] + counts['absent']}; "
          f"KB-leaf→KB-leaf moved: {len(kb_moved)}")

    print(f"\n  KB-leaf → KB-leaf `moved` (the high-confidence real-drift set, "
          f"{len(kb_moved)} rows):")
    for r in kb_moved:
        near = ", ".join(str(n) for n in r.found_at[:5]) or "wrapped"
        print(f"   · {r.citing_file}:{r.citing_line}")
        print(f"       cites {r.target}:{r.target_line}  →  excerpt at [{near}]")
        print(f"       quote: \"{r.quote[:100]}\"")

    if show_all:
        rest = [r for r in rows if not (r.kb_to_kb and r.moved)]
        print(f"\n  all other findings ({len(rest)}):")
        for r in sorted(rest, key=lambda r: (r.kind, r.citing_file, r.citing_line)):
            print(f"   · [{r.kind:13s}] {r.citing_file}:{r.citing_line} "
                  f"→ {r.target}:{r.target_line}  \"{r.quote[:60]}\"")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--root", type=Path, default=None, help="repo root (default: auto-detect)")
    parser.add_argument("--all", action="store_true", help="also print absent / non-KB rows")
    args = parser.parse_args(argv)

    vac = load_checker()
    repo_root = args.root.resolve() if args.root else vac.find_repo_root(Path(__file__).resolve().parent)
    counts, rows = scan(vac, repo_root)
    report(counts, rows, args.all)
    return 0  # audit report, never a gate


if __name__ == "__main__":
    raise SystemExit(main())

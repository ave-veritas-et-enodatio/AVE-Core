#!/usr/bin/env python3
"""

Known false-positive classes (do NOT promote to gating without an FP-triage pass):
- range citations `:NN-MM` (window anchors to NN; content at MM flags falsely)
- table cross-row quote/cite mis-association
- TeX/ASCII notation paraphrase
- generic short strings (def/return/origin-main class)
Anchor-content drift checker for AVE-Core — WARN-CLASS, NON-GATING.

Motivation
----------
Across research/, _orchestration/, and manuscript/ave-kb/ the corpus cites
locations as `path.ext:NN` and frequently pins a verbatim excerpt next to the
cite in `backticks`. When the target file drifts (lines inserted/removed above
the cited spot), the `:NN` goes stale while the quoted excerpt still names the
real content — a "line-anchor drift" the review lane kept catching by hand.

This tool automates that catch: for every `path.ext:NN` cite that carries a
NEARBY backtick-quoted excerpt, it verifies the excerpt actually occurs within
±10 lines of the cited line in the target file. If the excerpt appears MOVED (a candidate — still FP-contaminated: range cites :NN-MM anchor only to range start, cross-row table associations, TeX/ASCII paraphrase; spot-check base rate ~1-in-5 real), (it is
elsewhere in the file) the `:NN` is stale; if it is ABSENT the quote/target may
be reworded or the FP classes below apply.

WARN-CLASS ONLY. This tool prints a summary + the worst offenders and ALWAYS
exits 0. It is wired into `make verify` as an advisory step. Gating is a
deliberate later promotion, not a default — the false-positive classes below
must be driven down first.

Scope
-----
  * Citing files: `.md` under research/ + _orchestration/ + manuscript/ave-kb/
    (SKIP_DIRS pruned — .git, build, session/, _archive, .index, ...).
  * Cite pattern: `path.ext:NN` where ext ∈ TARGET_EXTS (md, py, tex, json, ...),
    optionally wrapped in backticks or a Markdown link.
  * Target files: resolved relative to the citing file's directory first, then
    the repo root. Unresolvable targets are counted UNRESOLVED and skipped
    (broken-link territory — that is `verify-md-links`'s job, not ours).
  * Association: a cite is paired with the nearest CHECKABLE backtick span on
    the same line or ±QUOTE_ADJACENCY lines. A backtick span is checkable when
    it is not itself a path-cite / bare-path reference and is not trivially
    short (see MIN_QUOTE_LEN). Cites with no checkable adjacent quote are
    counted NOT-CHECKED (no-quote) and are NOT failures.

Matching is whitespace-normalized (`\\s+` → single space) and case-sensitive;
the ±10-line target window is joined before matching so a target-side line wrap
does not cause a spurious miss.

Known false-positive / false-negative classes (why this is WARN-CLASS)
----------------------------------------------------------------------
  * TeX escaping. A quote carrying LaTeX (`$\\alpha$`, `\\text{sat}`, `$1/r^2$`)
    may differ character-for-character from the target source (one side escapes,
    the other renders), yielding a spurious ABSENT.
  * Multi-line / structural quotes. Inline backtick spans are single-line; the
    ±10 window is whitespace-joined to absorb target-side wrapping, but a quote
    meant to span a table row or block may still fragment.
  * Markdown decoration. Bold/italic markers (`**`, `_`) and differing internal
    whitespace inside the quoted excerpt can defeat the substring test.
  * Paraphrase quotes. Some backtick spans paraphrase rather than transcribe;
    an ABSENT verdict there is not a line-anchor problem.
  * Short / symbol-only quotes. Excerpts shorter than MIN_QUOTE_LEN are skipped
    (counted trivial) because they match almost any window (false OK), so they
    carry no anchor signal.
  * Multi-cite lines. A line with several cites and one quote may associate that
    quote with more than one cite (double-count). Warn-class tolerates this.

Self-test
---------
`--self-test` builds a throwaway tree exercising OK / drift-moved / drift-absent
/ no-quote / trivial cases and asserts the classifier buckets them correctly.
Returns nonzero on self-test failure (a dev-time signal); the normal scan run
always returns 0.
"""

import argparse
import re
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

# Directories pruned at any depth (mirrors verify-md-links SKIP_DIRS + session/).
SKIP_DIRS = {
    ".venv",
    "venv",
    ".git",
    "build",
    "node_modules",
    ".index",
    ".agents",
    "_archive",
    "session",
    "__pycache__",
}

# Roots whose .md files we scan for cites (repo-root-relative).
CITING_ROOTS = ("research", "_orchestration", "manuscript/ave-kb")

# Target extensions a `path.EXT:NN` cite may point at.
TARGET_EXTS = (
    "md",
    "py",
    "tex",
    "json",
    "jsonl",
    "csv",
    "txt",
    "yaml",
    "yml",
    "toml",
    "cfg",
    "ini",
    "sh",
)

# A `path.ext:NN` cite. Path may carry directory segments; ext is a known target
# extension; line is a positive integer. Word boundary after the digits keeps
# `foo.md:12` from swallowing a trailing `:34` range half.
CITE_RE = re.compile(
    r"(?P<path>(?:[\w.+-]+/)*[\w.+-]+\.(?:" + "|".join(TARGET_EXTS) + r")):(?P<line>\d+)(?!\d)"
)

# One inline backtick span (no nested backticks).
BACKTICK_RE = re.compile(r"`([^`\n]+)`")

# A span whose whole (stripped) body is a bare path or path-cite — NOT content.
PATHISH_RE = re.compile(r"^[\w./+-]+\.[A-Za-z0-9]+(:\d+)?$")

# Reference fragments that are decoration, not target-line content: a bare
# `:NN` line-number fragment or a bare `.ext` extension. These appear all over
# the corpus and match everywhere, so treating them as anchors is pure noise.
FRAGMENT_RE = re.compile(r"^(:\d+|\.[A-Za-z0-9]+)$")

WINDOW = 10  # ±N lines around the cited line in the TARGET file
QUOTE_ADJACENCY = 1  # ±N lines around the cite in the CITING file to find a quote
MIN_QUOTE_LEN = 4  # min stripped length of a backtick span to count as an anchor
DEFAULT_TOP = 25  # worst-offenders printed


@dataclass
class Finding:
    citing_file: Path
    citing_line: int
    target: str  # cite path as written
    target_line: int
    quote: str
    kind: str  # "moved" | "moved-wrapped" | "absent"
    found_at: list[int] = field(default_factory=list)


@dataclass
class Counts:
    cites: int = 0
    checked_ok: int = 0
    drift_moved: int = 0
    drift_absent: int = 0
    not_checked_noquote: int = 0
    not_checked_trivial: int = 0
    unresolved: int = 0


def find_repo_root(start: Path) -> Path:
    """Walk up from `start` to the AVE-Core repo root (Makefile + manuscript/)."""
    for parent in (start, *start.parents):
        if (parent / "Makefile").is_file() and (parent / "manuscript").is_dir():
            return parent
    for parent in (start, *start.parents):
        if (parent / ".git").exists():
            return parent
    return start


def strip_fenced(text: str) -> str:
    """Blank ``` / ~~~ fenced blocks (line-count preserved); KEEP inline spans.

    Unlike verify-md-links.strip_code, inline `code` spans are preserved — they
    ARE the quoted content this tool inspects. Only multi-line fences (example
    snippets) are dropped, since cites inside them are illustrative.
    """
    out: list[str] = []
    fence: str | None = None
    for raw in text.splitlines():
        stripped = raw.lstrip()
        if fence is None:
            if stripped.startswith("```") or stripped.startswith("~~~"):
                fence = stripped[:3]
                out.append("")
                continue
            out.append(raw)
        else:
            out.append("")
            if stripped.startswith(fence):
                fence = None
    return "\n".join(out)


def iter_citing_files(repo_root: Path):
    """Yield .md files under the citing roots, pruning SKIP_DIRS at any depth."""
    for root_name in CITING_ROOTS:
        root = repo_root / root_name
        if not root.is_dir():
            continue
        for path in sorted(root.rglob("*.md")):
            parts = path.relative_to(repo_root).parts
            if any(part in SKIP_DIRS for part in parts):
                continue
            yield path


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def is_checkable_quote(body: str) -> bool:
    """True if a backtick span is a substantive anchor (not a path / trivial)."""
    s = body.strip()
    if len(s) < MIN_QUOTE_LEN:
        return False
    if FRAGMENT_RE.match(s):  # bare `:NN` or `.ext` reference fragment
        return False
    if PATHISH_RE.match(s):  # bare path or path-cite reference
        return False
    if CITE_RE.search(s):  # contains a path:line cite — it IS a cite, not content
        return False
    if not any(c.isalnum() for c in s):  # pure punctuation / symbols
        return False
    return True


def _quote_spans(line: str) -> list[tuple[int, str]]:
    """Checkable backtick spans on a line as (start_col, body)."""
    return [(m.start(), m.group(1)) for m in BACKTICK_RE.finditer(line) if is_checkable_quote(m.group(1))]


def associate_quote(lines: list[str], cite_line_idx: int, cite_col: int) -> str | None:
    """Nearest checkable backtick span to a cite (same line, then ±ADJACENCY).

    Same-line spans are ranked by |column distance| to the cite; adjacent lines
    are considered only if the cite line has none AND the adjacent line carries
    no cite of its own (so a sibling cite's quote is never stolen — this is what
    keeps dense cite-lists from cross-contaminating). Returns the body or None.
    """
    same = _quote_spans(lines[cite_line_idx])
    if same:
        same.sort(key=lambda cb: abs(cb[0] - cite_col))
        return same[0][1]
    for delta in range(1, QUOTE_ADJACENCY + 1):
        for idx in (cite_line_idx - delta, cite_line_idx + delta):
            if 0 <= idx < len(lines):
                if CITE_RE.search(lines[idx]):  # that quote belongs to its own cite
                    continue
                spans = _quote_spans(lines[idx])
                if spans:
                    return spans[0][1]
    return None


class TargetCache:
    """Lazily read + normalize target files once."""

    def __init__(self) -> None:
        self._norm_lines: dict[Path, list[str]] = {}
        self._whole: dict[Path, str] = {}

    def load(self, path: Path) -> tuple[list[str], str]:
        if path not in self._norm_lines:
            try:
                raw = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                self._norm_lines[path] = []
                self._whole[path] = ""
                return [], ""
            lines = raw.splitlines()
            self._norm_lines[path] = [normalize(ln) for ln in lines]
            self._whole[path] = normalize(" ".join(lines))
        return self._norm_lines[path], self._whole[path]


def resolve_target(cite_path: str, citing_file: Path, repo_root: Path) -> Path | None:
    """Resolve a cite path relative to the citing file, then the repo root."""
    for base in (citing_file.parent, repo_root):
        cand = (base / cite_path).resolve()
        if cand.is_file():
            return cand
    return None


def classify(
    norm_lines: list[str], whole: str, cited_line: int, quote: str
) -> tuple[str, list[int]]:
    """Classify a (cited_line, quote) against a target file.

    Returns ("ok"|"moved"|"moved-wrapped"|"absent", found_line_numbers).
    """
    q = normalize(quote)
    if not q or not norm_lines:
        return "absent", []
    lo = max(0, cited_line - 1 - WINDOW)
    hi = min(len(norm_lines), cited_line - 1 + WINDOW + 1)
    window = " ".join(norm_lines[lo:hi])
    if q in window:
        return "ok", []
    hits = [i + 1 for i, ln in enumerate(norm_lines) if q in ln]
    if hits:
        return "moved", hits
    if q in whole:  # wrapped across lines somewhere outside the window
        return "moved-wrapped", []
    return "absent", []


def scan(citing_files, repo_root: Path) -> tuple[Counts, list[Finding]]:
    counts = Counts()
    findings: list[Finding] = []
    cache = TargetCache()
    for cf in citing_files:
        try:
            text = strip_fenced(cf.read_text(encoding="utf-8", errors="replace"))
        except OSError:
            continue
        lines = text.splitlines()
        for i, line in enumerate(lines):
            for m in CITE_RE.finditer(line):
                counts.cites += 1
                cite_path = m.group("path")
                cited_line = int(m.group("line"))
                quote = associate_quote(lines, i, m.start())
                if quote is None:
                    # Distinguish "there was a nearby span but it was trivial"
                    # from "no span at all" for an honest not-checked breakdown.
                    raw_spans = [
                        b for _, b in ((mm.start(), mm.group(1)) for mm in BACKTICK_RE.finditer(line))
                    ]
                    if any(len(b.strip()) < MIN_QUOTE_LEN for b in raw_spans):
                        counts.not_checked_trivial += 1
                    else:
                        counts.not_checked_noquote += 1
                    continue
                target = resolve_target(cite_path, cf, repo_root)
                if target is None:
                    counts.unresolved += 1
                    continue
                norm_lines, whole = cache.load(target)
                kind, found = classify(norm_lines, whole, cited_line, quote)
                if kind == "ok":
                    counts.checked_ok += 1
                elif kind in ("moved", "moved-wrapped"):
                    counts.drift_moved += 1
                    findings.append(
                        Finding(cf, i + 1, cite_path, cited_line, quote, kind, found)
                    )
                else:
                    counts.drift_absent += 1
                    findings.append(
                        Finding(cf, i + 1, cite_path, cited_line, quote, kind, found)
                    )
    return counts, findings


def _fmt_quote(q: str, width: int = 60) -> str:
    q = normalize(q)
    return q if len(q) <= width else q[: width - 1] + "…"


def report(counts: Counts, findings: list[Finding], repo_root: Path, top: int) -> None:
    print("[anchor-content] WARN-CLASS advisory — quoted-excerpt vs cited line drift")
    print(f"  cites scanned .............. {counts.cites}")
    print(f"  checked & anchored (OK) .... {counts.checked_ok}")
    print(f"  DRIFT — excerpt moved ...... {counts.drift_moved}  (stale :NN, excerpt found elsewhere)")
    print(f"  DRIFT — excerpt absent ..... {counts.drift_absent}  (not in target; see FP classes)")
    print(f"  not-checked (no quote) ..... {counts.not_checked_noquote}")
    print(f"  not-checked (trivial quote)  {counts.not_checked_trivial}")
    print(f"  unresolved target .......... {counts.unresolved}  (verify-md-links territory)")
    checked = counts.checked_ok + counts.drift_moved + counts.drift_absent
    drift = counts.drift_moved + counts.drift_absent
    rate = (drift / checked * 100.0) if checked else 0.0
    print(f"  → checked cites: {checked}; drift: {drift} ({rate:.1f}% of checked)")

    if not findings:
        print("  No drift among checkable cites.")
        return
    # Moved (stale-line, strongest signal) first, then absent.
    order = {"moved": 0, "moved-wrapped": 1, "absent": 2}
    findings.sort(key=lambda f: (order.get(f.kind, 3), str(f.citing_file), f.citing_line))
    print(f"\n  worst offenders (up to {top}; moved-line drift first):")
    for f in findings[:top]:
        try:
            rel = f.citing_file.relative_to(repo_root)
        except ValueError:
            rel = f.citing_file
        loc = ""
        if f.kind == "moved" and f.found_at:
            near = ", ".join(str(n) for n in f.found_at[:5])
            loc = f" [found at {target_line_summary(f.target, near)}]"
        elif f.kind == "moved-wrapped":
            loc = " [found wrapped elsewhere]"
        print(f"   · {rel}:{f.citing_line}  →  {f.target}:{f.target_line}  {f.kind}{loc}")
        print(f"       excerpt: `{_fmt_quote(f.quote)}`")


def target_line_summary(target: str, near: str) -> str:
    name = target.rsplit("/", 1)[-1]
    return f"{name}:{near}"


def run_self_test() -> int:
    print("[anchor-content] self-test ...")
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "Makefile").write_text("# sentinel\n")
        (root / "manuscript").mkdir()
        # Target file: known content at known lines.
        target_lines = ["\n"] * 40
        target_lines[9] = "the quick brown fox anchor phrase\n"  # line 10
        target_lines[29] = "a drifted excerpt that moved down here\n"  # line 30
        target = root / "target.md"
        target.write_text("".join(target_lines))
        # Citing file exercising each bucket.
        citing = root / "research"
        citing.mkdir()
        cite_md = citing / "cites.md"
        cite_md.write_text(
            "\n".join(
                [
                    "GOOD:   see `target.md:10` for `the quick brown fox anchor phrase` here.",
                    "MOVED:  per `target.md:10` the `a drifted excerpt that moved down here` note.",
                    "ABSENT: `target.md:10` claims `a phrase that exists nowhere at all`.",
                    "NOQUOTE: `target.md:10` with no adjacent quoted excerpt whatsoever.",
                    "TRIVIAL: `target.md:10` near `S` only.",
                ]
            )
            + "\n"
        )
        counts, findings = scan([cite_md], root)
        expect = {
            "cites": 5,
            "checked_ok": 1,
            "drift_moved": 1,
            "drift_absent": 1,
            "not_checked_noquote": 1,
            "not_checked_trivial": 1,
            "unresolved": 0,
        }
        ok = True
        for k, v in expect.items():
            got = getattr(counts, k)
            status = "ok" if got == v else "FAIL"
            if got != v:
                ok = False
            print(f"   {status}: {k} = {got} (expected {v})")
        moved = [f for f in findings if f.kind == "moved"]
        if not (len(moved) == 1 and 30 in moved[0].found_at):
            ok = False
            print(f"   FAIL: expected 1 moved finding located at line 30; got {[ (f.kind,f.found_at) for f in findings]}")
        else:
            print("   ok: moved finding correctly located at target line 30")
        print("[anchor-content] self-test", "PASSED" if ok else "FAILED")
        return 0 if ok else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--self-test", action="store_true", help="run the built-in self-test and exit")
    parser.add_argument("--top", type=int, default=DEFAULT_TOP, help="max worst-offenders to print")
    parser.add_argument("--root", type=Path, default=None, help="repo root (default: auto-detect)")
    args = parser.parse_args(argv)

    if args.self_test:
        return run_self_test()

    repo_root = args.root.resolve() if args.root else find_repo_root(Path(__file__).resolve().parent)
    counts, findings = scan(list(iter_citing_files(repo_root)), repo_root)
    report(counts, findings, repo_root, args.top)
    # WARN-CLASS: never gate. Gating is a later, deliberate promotion.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

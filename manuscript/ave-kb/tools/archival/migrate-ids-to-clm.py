#!/usr/bin/env python3
"""One-time migration: prefix every canonical claim ID with ``clm-``.

Bare 6-char IDs like ``0ktpcn`` collide lexically with English/physics words
when grepped. This tool rewrites every occurrence of a *real* claim ID (one of
the 199 canonical IDs declared by ``<!-- id: ... -->`` markers) to ``clm-`` +
that ID, everywhere it appears in KB markdown — canonical markers, leaf
frontmatter ``claims:``, Tier 2 inline markers, index ``subtree-claims:``,
``depends-on`` bullets, and prose mentions.

Only registered canonical IDs are rewritten; 6-char English words that merely
look like IDs are left alone. The tool collects *bare* (un-prefixed) canonical
IDs only — once the KB is migrated there are none, so re-running is a clean
no-op. A negative lookbehind ``(?<!clm-)`` additionally prevents re-prefixing
within a single run.

Self-contained: stdlib only, no dependency on the live KB toolchain — a drift
in that toolchain cannot retroactively break this archival tool.

Run from the repository root::

    python manuscript/ave-kb/tools/archival/migrate-ids-to-clm.py [--dry-run]

ARCHIVAL — one-shot tool, executed 2026-05-15; retained for reference.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

KB = Path("manuscript/ave-kb")
EXCLUDE_DIRS = {"session", ".index"}

# Per-position-type classifiers, applied line-by-line for the breakdown report.
_CANONICAL_MARKER = re.compile(r"<!--\s*id:\s*clm-[a-z0-9]{6}\s*-->")
_TIER2_MARKER = re.compile(r"<!--\s*claim-quality:")
_CLAIMS_LINE = re.compile(r"^\s*claims:")
_SUBTREE_LINE = re.compile(r"^\s*subtree-claims:")
_DEPENDS_BULLET = re.compile(r"^\s*-\s+`?(?:clm-)?[a-z0-9]{6}`?\s+—")

# A canonical claim-ID declaration in its *bare* (pre-migration) form.
_BARE_CANONICAL_ID = re.compile(r"<!--\s*id:\s*([a-z0-9]{6})\s*-->")


def _classify(line_before: str) -> str:
    """Return the position-type bucket a rewritten occurrence belongs to.

    Classification uses the pre-rewrite line so the heuristics match the
    documented canonical forms.
    """
    if _CANONICAL_MARKER.search(line_before) or "<!-- id:" in line_before:
        return "canonical_marker"
    if _TIER2_MARKER.search(line_before):
        return "tier2_marker"
    if _CLAIMS_LINE.match(line_before):
        return "claims_list"
    if _SUBTREE_LINE.match(line_before):
        return "subtree_claims"
    if _DEPENDS_BULLET.match(line_before):
        return "depends_on_bullet"
    return "prose_mention"


def _strip_code_fences(text: str) -> str:
    """Blank out fenced code-block content so example placeholders inside
    ``` fences are not mistaken for real canonical-ID declarations."""
    out: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else line)
    return "\n".join(out)


def collect_bare_canonical_ids(kb_root: Path) -> set[str]:
    """Return the set of bare 6-char canonical IDs declared by `<!-- id: ... -->`
    markers across all claim-quality.md files (code-fence content excluded).

    Post-migration the KB has no bare canonical markers — every marker is
    `clm-`-prefixed — so this returns the empty set and migrate() is a no-op.
    """
    ids: set[str] = set()
    for path in kb_root.rglob("claim-quality.md"):
        ids.update(_BARE_CANONICAL_ID.findall(_strip_code_fences(path.read_text())))
    return ids


def build_migration_regex(known_ids: set[str]) -> re.Pattern:
    """One combined regex over all known IDs, idempotent via lookbehind."""
    alternation = "|".join(re.escape(i) for i in sorted(known_ids))
    return re.compile(rf"(?<!clm-)\b({alternation})\b")


def kb_markdown_files(kb_root: Path):
    """Iterate every .md file under kb_root except under session/ and .index/."""
    for root, dirs, files in os.walk(kb_root):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in sorted(files):
            if f.endswith(".md"):
                yield Path(root) / f


def migrate(kb_root: Path, dry_run: bool) -> dict:
    """Rewrite every real claim ID to its clm- form across KB markdown.

    Returns a stats dict: files_changed, occurrences, and a per-position-type
    breakdown.
    """
    known_ids = collect_bare_canonical_ids(kb_root)

    breakdown: dict[str, int] = {
        "canonical_marker": 0,
        "claims_list": 0,
        "tier2_marker": 0,
        "subtree_claims": 0,
        "depends_on_bullet": 0,
        "prose_mention": 0,
    }

    # No bare canonical IDs => the KB is already migrated (or empty). No-op.
    if not known_ids:
        return {
            "known_ids": 0,
            "files_changed": 0,
            "occurrences": 0,
            "breakdown": breakdown,
        }

    pattern = build_migration_regex(known_ids)
    files_changed = 0
    occurrences = 0

    for path in kb_markdown_files(kb_root):
        text = path.read_text()
        if not pattern.search(text):
            continue
        new_lines = []
        file_hits = 0
        for line in text.split("\n"):
            hits = len(pattern.findall(line))
            if hits:
                bucket = _classify(line)
                breakdown[bucket] += hits
                file_hits += hits
                line = pattern.sub(r"clm-\1", line)
            new_lines.append(line)
        new_text = "\n".join(new_lines)
        if new_text == text:
            continue
        files_changed += 1
        occurrences += file_hits
        if not dry_run:
            tmp = path.with_suffix(path.suffix + ".tmp")
            tmp.write_text(new_text)
            os.replace(tmp, path)

    return {
        "known_ids": len(known_ids),
        "files_changed": files_changed,
        "occurrences": occurrences,
        "breakdown": breakdown,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Report what would change without writing any file.",
    )
    args = parser.parse_args(argv)

    if not KB.is_dir():
        print(f"FAIL: {KB} not found. Run from repository root.", file=sys.stderr)
        return 2

    stats = migrate(KB, dry_run=args.dry_run)

    mode = "DRY RUN" if args.dry_run else "MIGRATED"
    print(f"[migrate-ids] {mode}: {stats['known_ids']} known canonical IDs.")
    print(
        f"[migrate-ids] {stats['files_changed']} files changed, "
        f"{stats['occurrences']} occurrences rewritten."
    )
    print("[migrate-ids] breakdown by position type:")
    for bucket, count in stats["breakdown"].items():
        print(f"  {bucket}: {count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

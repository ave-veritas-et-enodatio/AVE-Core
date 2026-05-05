#!/usr/bin/env python3
"""Regenerate derived KB metadata fields from leaf claims.

Side-effecting: writes to index.md and entry-point.md frontmatter blocks.
Idempotent. Run via ``make refresh-kb-metadata``.

Currently regenerates:
    * ``subtree-claims`` on every ``kind: index`` file
    * ``subtree-claims`` on the ``kind: entry-point`` file

Future: bootstrap directive blockquote text (currently hand-maintained).

This script does NOT verify; it ONLY refreshes. Run ``make verify-claim-quality``
afterward to confirm the result is internally consistent.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

KB = Path("manuscript/ave-kb")

EXCLUDE_DIRS = {"session"}
EXCLUDE_NAMES = {"claim-quality.md", "CLAUDE.md", "CONVENTIONS.md", "README.md"}

FRONTMATTER_BLOCK = re.compile(
    r"<!--\s*kb-frontmatter\s*\n(.*?)\n-->", re.DOTALL
)
ID_LIST = re.compile(r"\[(.*?)\]")
ID_RE = re.compile(r"\b([a-z0-9]{6})\b")


def parse_frontmatter(text: str) -> dict | None:
    """Return parsed frontmatter fields, or None if no block found."""
    m = FRONTMATTER_BLOCK.search(text)
    if not m:
        return None
    body = m.group(1)
    fields: dict = {}
    for line in body.splitlines():
        line = line.rstrip()
        if not line:
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and value.endswith("]"):
            fields[key] = ID_RE.findall(value)
        elif value.startswith('"') and value.endswith('"'):
            fields[key] = value[1:-1]
        elif value in ("true", "false"):
            fields[key] = value == "true"
        else:
            fields[key] = value
    return fields


def replace_subtree_claims(text: str, new_ids: list[str]) -> str:
    """Replace the subtree-claims line in the frontmatter block (or insert it)."""
    new_value = "[" + ", ".join(new_ids) + "]"

    def repl(match: re.Match) -> str:
        body = match.group(1)
        lines = body.splitlines()
        replaced = False
        new_lines = []
        for line in lines:
            if line.strip().startswith("subtree-claims:"):
                indent = line[: len(line) - len(line.lstrip())]
                new_lines.append(f"{indent}subtree-claims: {new_value}")
                replaced = True
            else:
                new_lines.append(line)
        if not replaced:
            # Insert after kind: line if present, else at top
            inserted = False
            out = []
            for line in new_lines:
                out.append(line)
                if not inserted and line.strip().startswith("kind:"):
                    out.append(f"subtree-claims: {new_value}")
                    inserted = True
            if not inserted:
                out.insert(0, f"subtree-claims: {new_value}")
            new_lines = out
        return "<!-- kb-frontmatter\n" + "\n".join(new_lines) + "\n-->"

    return FRONTMATTER_BLOCK.sub(repl, text, count=1)


def collect_leaves() -> dict[Path, list[str]]:
    """Return {leaf_path: [claim_ids]} for every leaf and leaf-as-index in the KB."""
    leaves: dict[Path, list[str]] = {}
    for root, dirs, files in os.walk(KB):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in files:
            if not f.endswith(".md") or f in EXCLUDE_NAMES:
                continue
            p = Path(root) / f
            text = p.read_text()
            fm = parse_frontmatter(text)
            if not fm:
                continue
            kind = fm.get("kind", "")
            if kind in ("leaf", "leaf-as-index"):
                leaves[p] = fm.get("claims", [])
    return leaves


def main() -> int:
    if not KB.is_dir():
        print(f"FAIL: {KB} not found. Run from repository root.", file=sys.stderr)
        return 2

    leaves = collect_leaves()

    updated = 0
    skipped = 0

    # Update each kind: index file
    for root, dirs, files in os.walk(KB):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in files:
            if f != "index.md":
                continue
            p = Path(root) / f
            text = p.read_text()
            fm = parse_frontmatter(text)
            if not fm:
                skipped += 1
                continue
            if fm.get("kind") != "index":
                continue  # leaf-as-index has no subtree
            idx_dir = p.parent
            expected = set()
            for leaf, ids in leaves.items():
                try:
                    leaf.relative_to(idx_dir)
                    expected.update(ids)
                except ValueError:
                    continue
            sorted_ids = sorted(expected)
            new_text = replace_subtree_claims(text, sorted_ids)
            if new_text != text:
                p.write_text(new_text)
                updated += 1

    # Update entry-point.md
    ep = KB / "entry-point.md"
    if ep.exists():
        text = ep.read_text()
        fm = parse_frontmatter(text)
        if fm and fm.get("kind") == "entry-point":
            all_ids = set()
            for ids in leaves.values():
                all_ids.update(ids)
            sorted_ids = sorted(all_ids)
            new_text = replace_subtree_claims(text, sorted_ids)
            if new_text != text:
                ep.write_text(new_text)
                updated += 1

    print(f"[refresh] Updated {updated} subtree-claims field(s).")
    if skipped:
        print(f"[refresh] Skipped {skipped} index files lacking frontmatter.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

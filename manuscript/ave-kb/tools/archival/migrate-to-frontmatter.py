#!/usr/bin/env python3
#
# ARCHIVAL — one-shot tool, already executed; retained for reference only.
#
# NOTE: the claim-quality ID format has changed since this tool last ran.
# IDs are now `clm-`-prefixed (e.g. `clm-h9aqmt`); this script predates that
# change and operates on the bare 6-char form (`h9aqmt`). If ever resurrected,
# its ID handling must be updated to the `clm-` prefix. The prefix migration
# itself is the sibling tool ./migrate-ids-to-clm.py.
#
"""One-shot migration: convert existing top-of-file comment annotations to a
unified YAML-in-HTML-comment frontmatter block.

See ``mad-review/kb-metadata-spine-spec.md`` for the format. Idempotent.

Two modes::

    ./.venv/bin/python manuscript/ave-kb/tools/archival/migrate-to-frontmatter.py --dry-run
    ./.venv/bin/python manuscript/ave-kb/tools/archival/migrate-to-frontmatter.py

Run dry first; only run live after dry-run summary is acceptable.

Files that don't match expected patterns are reported as **defects**, not
silently rewritten. Defects must be repaired by hand before the migration
will touch them. The script never invents a leaf marker, never drops an
unrecognized HTML comment, and never re-migrates an already-migrated file.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

KB = Path("manuscript/ave-kb")

# Subdirectories of KB to exclude entirely from the migration walk.
EXCLUDE_DIRS = {"session"}

# Filenames that are KB infrastructure, not content.
EXCLUDE_NAMES = {"claim-quality.md", "CLAUDE.md", "CONVENTIONS.md", "README.md"}

LEAF_MARKER = re.compile(r"^\s*<!--\s*leaf:\s*verbatim\s*-->\s*$")
PATH_STABLE = re.compile(r"^\s*<!--\s*path-stable:\s*(.+?)\s*-->\s*$")
TIER1 = re.compile(r"^\s*<!--\s*claim-quality:\s*([^(]*?)(?:\s*\(.*?\))?\s*-->\s*$")
NO_CLAIM = re.compile(r"^\s*<!--\s*no-claim:\s*(.+?)\s*-->\s*$")
SUBTREE = re.compile(r"^\s*<!--\s*claim-quality \(subtree\):\s*(.*?)\s*-->\s*$")
HTML_COMMENT_OPEN = re.compile(r"^\s*<!--")
KB_FRONTMATTER_OPEN = re.compile(r"^\s*<!--\s*kb-frontmatter\s*$")
ID_RE = re.compile(r"\b([a-z0-9]{6})\b")


def emit_frontmatter(fields: dict) -> str:
    """Render fields as a YAML-in-HTML-comment block (no trailing newline)."""

    def fmt_str(s: str) -> str:
        if any(c in s for c in ":#[]{},&*?|>'\"%@`") or s.startswith(" ") or s.endswith(" "):
            return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'
        return s

    def fmt_id_list(ids) -> str:
        return "[" + ", ".join(ids) + "]"

    out = ["<!-- kb-frontmatter"]
    if "kind" in fields:
        out.append(f"kind: {fields['kind']}")
    if "claims" in fields:
        out.append(f"claims: {fmt_id_list(fields['claims'])}")
    if "no-claim" in fields:
        out.append(f"no-claim: {fmt_str(fields['no-claim'])}")
    if "path-stable" in fields:
        out.append(f"path-stable: {fmt_str(fields['path-stable'])}")
    if "subtree-claims" in fields:
        out.append(f"subtree-claims: {fmt_id_list(fields['subtree-claims'])}")
    if "bootstrap" in fields:
        out.append(f"bootstrap: {'true' if fields['bootstrap'] else 'false'}")
    out.append("-->")
    return "\n".join(out)


def classify(line: str):
    """Classify a single line. Returns (kind, payload) where kind is one of:
    'blank', 'leaf-marker', 'path-stable', 'tier1', 'no-claim', 'subtree',
    'unknown-comment', 'uplink', 'content'."""
    s = line.strip()
    if not s:
        return ("blank", None)
    if LEAF_MARKER.match(s):
        return ("leaf-marker", None)
    m = PATH_STABLE.match(s)
    if m:
        return ("path-stable", m.group(1))
    m = NO_CLAIM.match(s)
    if m:
        return ("no-claim", m.group(1))
    m = SUBTREE.match(s)
    if m:
        return ("subtree", ID_RE.findall(m.group(1)))
    # Tier 1 claim line: starts with claim-quality but not subtree
    if "claim-quality:" in s and "subtree" not in s and HTML_COMMENT_OPEN.match(s):
        m = TIER1.match(s)
        if m:
            ids = ID_RE.findall(m.group(1))
            return ("tier1", ids)
    if HTML_COMMENT_OPEN.match(s):
        return ("unknown-comment", line)
    if s.startswith("[↑"):
        return ("uplink", line)
    return ("content", line)


def parse_top(lines: list[str], start: int):
    """Walk top-of-file lines from index `start`. Stop at first content line.
    Returns (extracted_fields, preserved_unknown_comments, has_leaf_marker,
    body_start_index)."""
    extracted: dict = {}
    unknown: list[str] = []
    has_leaf_marker = False
    i = start
    while i < len(lines):
        kind, payload = classify(lines[i])
        if kind == "blank":
            i += 1
            continue
        if kind == "leaf-marker":
            has_leaf_marker = True
            i += 1
            continue
        if kind == "path-stable":
            extracted["path-stable"] = payload
            i += 1
            continue
        if kind == "tier1":
            if payload:
                extracted["claims"] = payload
            i += 1
            continue
        if kind == "no-claim":
            extracted["no-claim"] = payload
            i += 1
            continue
        if kind == "subtree":
            extracted["subtree-claims"] = payload
            i += 1
            continue
        if kind == "unknown-comment":
            unknown.append(lines[i])
            i += 1
            continue
        # 'content' or 'uplink' — body has started
        break
    return extracted, unknown, has_leaf_marker, i


def detect_kind(p: Path, lines: list[str]):
    """Detect kind from existing file structure. Returns (kind, defect_msg).
    defect_msg is None on success."""
    rel = str(p.relative_to(KB))
    if rel == "entry-point.md":
        return ("entry-point", None)
    if p.name == "index.md":
        # Leaf-as-index: line 2 is leaf marker
        if len(lines) >= 2 and LEAF_MARKER.match(lines[1]):
            return ("leaf-as-index", None)
        return ("index", None)
    # Regular leaf: line 2 must be leaf marker
    if len(lines) >= 2 and LEAF_MARKER.match(lines[1]):
        return ("leaf", None)
    return (None, "non-index .md file missing <!-- leaf: verbatim --> on line 2")


def already_migrated(text: str) -> bool:
    for line in text.splitlines()[:30]:
        if KB_FRONTMATTER_OPEN.match(line):
            return True
    return False


def migrate_file(p: Path, dry_run: bool):
    """Returns (status, message). status in:
    'migrated' | 'would-migrate' | 'already' | 'no-changes' | 'defect' | 'excluded'."""
    if p.name in EXCLUDE_NAMES:
        return ("excluded", "infrastructure file")
    text = p.read_text()
    if already_migrated(text):
        return ("already", "already migrated")
    lines = text.splitlines()
    if not lines:
        return ("defect", "empty file")

    rel = str(p.relative_to(KB))

    # Detect kind first; entry-point has no up-link
    if rel == "entry-point.md":
        kind = "entry-point"
    else:
        if not lines[0].startswith("[↑"):
            return ("defect", f"line 1 is not an up-link: {lines[0][:60]!r}")
        kind, defect = detect_kind(p, lines)
        if defect:
            return ("defect", defect)

    # Build the new top-of-file
    if kind == "entry-point":
        # Find H1
        try:
            h1_idx = next(i for i, line in enumerate(lines) if line.startswith("# "))
        except StopIteration:
            return ("defect", "entry-point.md missing H1")
        # Parse anything before H1 (rare) and after H1
        pre_extracted, pre_unknown, _, _ = parse_top(lines, 0)
        post_extracted, post_unknown, _, post_body = parse_top(lines, h1_idx + 1)
        merged = {**pre_extracted, **post_extracted}
        merged_unknown = pre_unknown + post_unknown
        fields = {"kind": "entry-point", "bootstrap": True}
        fields["subtree-claims"] = merged.get("subtree-claims", [])
        # Build: [H1] [blank] [frontmatter] [blank] [unknown comments if any] [blank] [body]
        new_lines = [lines[h1_idx], "", emit_frontmatter(fields)]
        if merged_unknown:
            new_lines.append("")
            new_lines.extend(merged_unknown)
        new_lines.append("")
        new_lines.extend(lines[post_body:])
    else:
        # Standard file: line 0 = up-link
        extracted, unknown, has_lm, body_start = parse_top(lines, 1)
        # If kind expected leaf-marker but absent, defect
        if kind in ("leaf", "leaf-as-index") and not has_lm:
            return ("defect", "expected leaf marker on line 2 was not found by parser")
        # Build fields
        fields = {"kind": kind}
        if kind in ("leaf", "leaf-as-index"):
            if "claims" in extracted:
                fields["claims"] = extracted["claims"]
            if "no-claim" in extracted:
                fields["no-claim"] = extracted["no-claim"]
            if "path-stable" in extracted:
                fields["path-stable"] = extracted["path-stable"]
            # Validation: must have either claims or no-claim
            if "claims" not in fields and "no-claim" not in fields:
                return ("defect", "leaf has neither claim-quality line nor no-claim marker")
            if "claims" in fields and "no-claim" in fields:
                return ("defect", "leaf has BOTH claims and no-claim (mutually exclusive)")
        elif kind == "index":
            fields["subtree-claims"] = extracted.get("subtree-claims", [])
            depth = rel.count("/")
            if depth == 1 and rel.endswith("/index.md"):
                fields["bootstrap"] = True
        # Build new structure
        new_lines = [lines[0], "", emit_frontmatter(fields)]
        if unknown:
            new_lines.append("")
            new_lines.extend(unknown)
        new_lines.append("")
        new_lines.extend(lines[body_start:])

    new_text = "\n".join(new_lines)
    if not new_text.endswith("\n"):
        new_text += "\n"
    if new_text == text:
        return ("no-changes", "")
    if dry_run:
        return ("would-migrate", "")
    p.write_text(new_text)
    return ("migrated", "")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true",
                        help="Report what would change; touch nothing.")
    args = parser.parse_args()

    if not KB.is_dir():
        print(f"FAIL: {KB} not found. Run from repository root.", file=sys.stderr)
        return 2

    counts = {"migrated": 0, "would-migrate": 0, "already": 0,
              "no-changes": 0, "defect": 0, "excluded": 0}
    defects: list[tuple[str, str]] = []

    for root, dirs, files in os.walk(KB):
        # Prune excluded directories in place
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in files:
            if not f.endswith(".md"):
                continue
            p = Path(root) / f
            if p.name in EXCLUDE_NAMES:
                counts["excluded"] += 1
                continue
            try:
                status, msg = migrate_file(p, dry_run=args.dry_run)
            except Exception as e:  # pragma: no cover
                defects.append((str(p.relative_to(KB)), f"error: {e}"))
                counts["defect"] += 1
                continue
            counts[status] += 1
            if status == "defect":
                defects.append((str(p.relative_to(KB)), msg))

    mode = "DRY RUN" if args.dry_run else "LIVE"
    print(f"\n=== Migration {mode} summary ===")
    if args.dry_run:
        print(f"  would-migrate:    {counts['would-migrate']}")
    else:
        print(f"  migrated:         {counts['migrated']}")
    print(f"  already-migrated: {counts['already']}")
    print(f"  no-changes:       {counts['no-changes']}")
    print(f"  excluded:         {counts['excluded']}")
    print(f"  defects:          {counts['defect']}")

    if defects:
        print(f"\nDefects (must be fixed by hand before migration):")
        for path, reason in defects:
            print(f"  {path}: {reason}")

    return 0 if counts["defect"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Regenerate derived KB metadata fields from leaf claims.

Side-effecting: writes to index.md / entry-point.md frontmatter blocks and to
the derived ``solidity`` fields of every ``claim-quality.md`` register.
Idempotent. Run via ``make refresh-kb-metadata``.

Currently regenerates:
    * ``subtree-claims`` on every ``kind: index`` file
    * ``subtree-claims`` on the ``kind: entry-point`` file
    * the ``- solidity:`` line of every claim entry in every ``claim-quality.md``
      register — value, build-status phrase, and arithmetic trace are all
      derived from the hand-authored ``confidence`` values via
      ``kb_index_lib.compute_solidity``
    * the ``(solidity X)`` annotation in every claim-target depends-on bullet,
      synced to the depended-on claim's computed solidity

Future: bootstrap directive blockquote text (currently hand-maintained).

This script does NOT verify; it ONLY refreshes. Run ``make verify-claim-quality``
afterward to confirm the result is internally consistent.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

# Make the sibling kb_index_lib importable regardless of invocation cwd.
_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

import kb_index_lib  # noqa: E402

KB = Path("manuscript/ave-kb")
INDEX_DIR = KB / ".index"

# JSONL files emitted by the index-emission phase. Order is the documented
# file inventory order from SCHEMA.md.
INDEX_FILES = (
    "claims",
    "depends-on",
    "strengthen-by",
    "cites",
    "subtree-aggregates",
)

EXCLUDE_DIRS = {"session", ".index"}
EXCLUDE_NAMES = {"claim-quality.md", "CLAUDE.md", "CONVENTIONS.md", "README.md"}

FRONTMATTER_BLOCK = re.compile(
    r"<!--\s*kb-frontmatter\s*\n(.*?)\n-->", re.DOTALL
)
ID_LIST = re.compile(r"\[(.*?)\]")
ID_RE = re.compile(r"\b(clm-[a-z0-9]{6})\b")


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


CANONICAL_ID_LINE = re.compile(r"<!--\s*id:\s*(clm-[a-z0-9]{6})\s*-->")
SOLIDITY_LINE = re.compile(r"^(\s*)-\s*solidity:")
# Matches a depends-on (solidity X) annotation in either rendering: a numeric
# value or the *pending* form (target has no computable solidity). Matching
# both keeps the annotation sync correct across numeric<->pending transitions.
SOLIDITY_ANNOTATION = re.compile(
    r"\(solidity\s+(?:-?\d+(?:\.\d+)?|\*pending\*)\)"
)
CLAIM_ID_TOKEN = re.compile(r"\b(clm-[a-z0-9]{6})\b")


def _fmt(value: float) -> str:
    """Format a solidity / confidence value as a 2-dp decimal string.

    Mirrors the existing claim-quality.md convention (every value is written
    with two decimal places, e.g. ``0.90``, ``0.41``).
    """
    return f"{value:.2f}"


SOLIDITY_PENDING_LINE = "- solidity: *pending*"


def _solidity_line(entry, solidity, min_dep) -> str:
    """Build the canonical ``- solidity:`` line for one claim entry.

    ``solidity`` is the entry's computed value; ``min_dep`` is the minimum
    dependency solidity (or ``None`` when the entry has no depends-on edges).
    With dependencies the line carries an arithmetic trace
    ``[= <confidence> × <min-dep-solidity>]``; without, the trace is omitted
    (solidity trivially equals confidence).

    When ``solidity`` is ``None`` the claim has no computable solidity — its
    ``confidence`` is ``*pending*`` OR a dependency's solidity is ``*pending*``
    (pending-ness propagates transitively, like NaN). Both render the same:
    the bare ``- solidity: *pending*`` form, no phrase, no arithmetic trace.
    """
    if solidity is None:
        return SOLIDITY_PENDING_LINE
    phrase = kb_index_lib.build_status_phrase(solidity)
    base = f"- solidity: {_fmt(solidity)} ({phrase})"
    if min_dep is None:
        return base
    return f"{base} [= {_fmt(entry.confidence)} × {_fmt(min_dep)}]"


def _quality_section_ranges(lines: list[str]) -> dict[str, tuple[int, int]]:
    """Map each claim id to the raw line range of its ``### Quality`` section.

    Mirrors ``kb_index_lib.parse_claim_quality_file``'s section-location
    logic, but returns raw line indices (``[start, end)`` over ``lines``,
    where ``start`` is the line AFTER the ``### Quality`` heading) so the
    write-back can edit lines surgically. Code fences do not shift line
    numbers, so indices computed on fence-scrubbed text equal raw indices.

    An entry with no ``### Quality`` section is omitted.
    """
    scrubbed = kb_index_lib._strip_code_fences("\n".join(lines)).splitlines()
    # Locate every (id_line_idx, claim_id).
    id_lines: list[tuple[int, str]] = []
    for i, line in enumerate(scrubbed):
        m = CANONICAL_ID_LINE.match(line.strip())
        if m:
            id_lines.append((i, m.group(1)))

    ranges: dict[str, tuple[int, int]] = {}
    for id_line, claim_id in id_lines:
        qstart: int | None = None
        for j in range(id_line + 1, len(scrubbed)):
            if scrubbed[j].strip() == "### Quality":
                qstart = j
                break
            # The next `## ` H2 is a sibling-entry title; stop. An H3
            # `### Quality` heading does not start with `## `.
            if scrubbed[j].startswith("## "):
                break
        if qstart is None:
            continue
        qend = len(scrubbed)
        for j in range(qstart + 1, len(scrubbed)):
            if scrubbed[j].startswith("## "):
                qend = j
                break
        ranges[claim_id] = (qstart + 1, qend)
    return ranges


def _rewrite_claim_quality_solidity(
    path: Path, entries, solidity: dict[str, float]
) -> tuple[int, list[tuple[str, str, str]], list[tuple[str, str, str]]]:
    """Rewrite derived solidity content in a single ``claim-quality.md`` file.

    For every claim entry, rewrites:

    * the ``- solidity:`` line in its ``### Quality`` section. A claim with a
      computable solidity gets the numeric form (value, build-status phrase,
      arithmetic trace); a claim with no computable solidity — confidence is
      ``*pending*`` OR a dependency is ``*pending*`` — gets the bare
      ``- solidity: *pending*`` form. Pending-ness propagates transitively
      (like NaN through arithmetic): "absent from the ``compute_solidity``
      result" is treated identically to "pending-confidence", regardless of
      the claim's own local confidence.
    * the ``(solidity X)`` annotation on each claim-target depends-on bullet,
      synced to the depended-on claim's solidity. A bullet whose target has
      no computable solidity gets ``(solidity *pending*)``.

    Framework-target depends-on bullets carry no ``(solidity X)`` token and
    are untouched. Lines already in their canonical form are left
    byte-identical, so the rewrite is idempotent.

    Returns ``(files_changed, solidity_changes, annotation_changes)`` where
    ``files_changed`` is 0 or 1 and the change lists hold ``(claim_id, old,
    new)`` tuples for reporting.
    """
    text = path.read_text()
    had_final_newline = text.endswith("\n")
    lines = text.split("\n")
    if had_final_newline:
        # split() leaves a trailing "" element; drop it so indices line up
        # with the visible content lines, restore the newline at write time.
        lines = lines[:-1]

    by_id = {e.id: e for e in entries}
    ranges = _quality_section_ranges(lines)

    solidity_changes: list[tuple[str, str, str]] = []
    annotation_changes: list[tuple[str, str, str]] = []

    for claim_id, (qstart, qend) in ranges.items():
        entry = by_id.get(claim_id)
        if entry is None:
            continue
        # ``computed`` is None when this claim has no computable solidity:
        # its confidence is *pending* OR a dependency is *pending*. Both
        # cases render as the *pending* solidity line — pending-ness is
        # decided by presence in ``solidity``, NOT by local confidence.
        computed = solidity.get(claim_id)
        min_dep = kb_index_lib.min_dependency_solidity(entry, solidity)

        for idx in range(qstart, qend):
            line = lines[idx]
            # (1) The solidity line.
            if SOLIDITY_LINE.match(line):
                new_line = _solidity_line(entry, computed, min_dep)
                if new_line != line:
                    solidity_changes.append((claim_id, line, new_line))
                    lines[idx] = new_line
                continue
            # (2) A claim-target depends-on bullet's (solidity X) annotation.
            if "(solidity" not in line:
                continue
            head = kb_index_lib._depends_on_bullet_head(
                re.sub(r"^\s*-\s*", "", line.strip())
            )
            targets = CLAIM_ID_TOKEN.findall(head)
            if not targets:
                continue
            # A claim depends-on bullet leads with exactly one claim id; its
            # (solidity X) annotation is that target's solidity. A target
            # with no computable solidity renders as (solidity *pending*).
            target_solidity = solidity.get(targets[0])
            if target_solidity is None:
                replacement = "(solidity *pending*)"
            else:
                replacement = f"(solidity {_fmt(target_solidity)})"
            new_line = SOLIDITY_ANNOTATION.sub(replacement, line, count=1)
            if new_line != line:
                annotation_changes.append((claim_id, line, new_line))
                lines[idx] = new_line

    new_text = "\n".join(lines)
    if had_final_newline:
        new_text += "\n"
    if new_text != text:
        path.write_text(new_text)
        return 1, solidity_changes, annotation_changes
    return 0, solidity_changes, annotation_changes


def _refresh_solidity() -> tuple[int, list, list]:
    """Rewrite derived solidity content across every ``claim-quality.md``.

    ``solidity`` is computed ONCE via ``kb_index_lib.compute_solidity`` over
    the whole KB claim graph; the same map drives both the solidity-line
    write-back and the depends-on annotation sync (and, downstream, the
    ``.index/claims.jsonl`` fields). Raises ``kb_index_lib.SolidityCycleError``
    if the claim depends-on graph has a cycle — refresh refuses to write
    solidity in that case rather than emit undefined values.

    Returns ``(files_changed, solidity_changes, annotation_changes)``.
    """
    state = kb_index_lib.discover_kb(KB, diagnostic_stream=None)
    solidity = kb_index_lib.compute_solidity(state.claim_entries)

    # Group parsed entries by their canonical claim-quality.md file.
    entries_by_file: dict[str, list] = {}
    for entry in state.claim_entries:
        entries_by_file.setdefault(entry.canonical_path, []).append(entry)

    files_changed = 0
    all_solidity_changes: list = []
    all_annotation_changes: list = []
    for rel_path, entries in sorted(entries_by_file.items()):
        path = KB / rel_path
        changed, sol_ch, ann_ch = _rewrite_claim_quality_solidity(
            path, entries, solidity
        )
        files_changed += changed
        all_solidity_changes.extend((rel_path, *c) for c in sol_ch)
        all_annotation_changes.extend((rel_path, *c) for c in ann_ch)
    return files_changed, all_solidity_changes, all_annotation_changes


def _emit_jsonl_indexes() -> tuple[int, int]:
    """Write the five JSONL files under ``KB/.index/``.

    Returns ``(written, unchanged)``. A file is "unchanged" when its on-disk
    bytes already match the freshly serialized payload; in that case the
    write is skipped to keep mtime stable and avoid spurious ``git status``
    noise. Otherwise the file is written atomically (rename over existing).
    """
    INDEX_DIR.mkdir(exist_ok=True)
    state = kb_index_lib.discover_kb(KB)
    all_records = kb_index_lib.build_all_records(state)

    written = 0
    unchanged = 0
    for short_name in INDEX_FILES:
        records = all_records[short_name]
        out_path = INDEX_DIR / f"{short_name}.jsonl"
        # Re-serialize using the library's canonical format so we can compare
        # byte-for-byte against the on-disk file before deciding to write.
        lines = [
            json.dumps(rec, ensure_ascii=False, separators=(", ", ": "))
            for rec in records
        ]
        body = "\n".join(lines)
        if body:
            body += "\n"
        new_bytes = body.encode("utf-8")
        if out_path.exists() and out_path.read_bytes() == new_bytes:
            unchanged += 1
            continue
        # Atomic rewrite: write to sibling temp file, then rename.
        tmp_path = out_path.with_suffix(out_path.suffix + ".tmp")
        tmp_path.write_bytes(new_bytes)
        os.replace(tmp_path, out_path)
        written += 1
    return written, unchanged


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

    # Phase 1b: rewrite the derived solidity content (solidity lines +
    # depends-on (solidity X) annotations) in every claim-quality.md register.
    try:
        sol_files, sol_changes, ann_changes = _refresh_solidity()
    except kb_index_lib.SolidityCycleError as exc:
        print(f"\nFAIL: {exc}", file=sys.stderr)
        print(
            "  → solidity is undefined for cycle members; refusing to write. "
            "Break the cycle in the claim depends-on graph and re-run.",
            file=sys.stderr,
        )
        return 1
    print(
        f"[refresh] Rewrote solidity in {sol_files} claim-quality.md file(s) "
        f"({len(sol_changes)} solidity line(s), "
        f"{len(ann_changes)} depends-on annotation(s) changed)."
    )
    for rel, cid, old, new in sol_changes:
        print(f"  [solidity] {rel}:{cid}")
        print(f"    - {old.strip()}")
        print(f"    + {new.strip()}")
    for rel, cid, old, new in ann_changes:
        print(f"  [depends-on] {rel}:{cid}")
        print(f"    - {old.strip()}")
        print(f"    + {new.strip()}")

    # Phase 2: emit derived JSONL index files. The frontmatter writes above
    # are already on disk, so discover_kb here picks up the just-written
    # subtree-claims values when materializing subtree-aggregates.jsonl.
    written, unchanged = _emit_jsonl_indexes()
    print(
        f"[refresh-index] Wrote {written} file(s) under "
        f"{INDEX_DIR.as_posix()}/ ({unchanged} unchanged)."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

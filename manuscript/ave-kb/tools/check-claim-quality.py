#!/usr/bin/env python3
"""Mechanical integrity check for the AVE knowledge-base claim-quality framework.

Read-only. Never modifies any file. Reads the unified ``kb-frontmatter`` block
(see ``mad-review/kb-metadata-spine-spec.md``).

Eight checks, all hard fail-loud:

    1. Tier 1 coverage: every leaf has either ``claims:`` or ``no-claim:`` in
       its frontmatter (mutually exclusive).
    2. Tier 2 coverage: every multi-claim leaf has proximal inline markers
       (``<!-- claim-quality: <id> ... -->``) for each ID in its claims list.
    3. ID uniqueness: no canonical ``<!-- id: xxxxxx -->`` appears twice in
       any ``claim-quality.md`` register.
    4. Orphan refs: every Tier 1 ID resolves to a canonical entry.
    5. Frontmatter presence: every non-excluded .md file has a frontmatter
       block (refresh-fixable for indexes; manual fix for leaves).
    6. Subtree consistency: each ``kind: index`` file's ``subtree-claims``
       equals the union of leaf claims under its directory; entry-point's
       equals the global union. (refresh-fixable.)
    7. Bidirectional coverage: every canonical entry is back-linked by at
       least one leaf's frontmatter.
    8. No-claim/claims exclusivity: no leaf carries both fields.

Failure categories are tagged refresh-fixable or manual-fix. If any
refresh-fixable failures are present, the report ends with a hint to run
``make refresh-kb-metadata`` first; verify is read-only and never auto-fixes.

Run via::

    ./.venv/bin/python manuscript/ave-kb/tools/check-claim-quality.py
    make verify-claim-quality
"""

from __future__ import annotations

import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

KB = Path("manuscript/ave-kb")

EXCLUDE_DIRS = {"session"}
EXCLUDE_NAMES = {"claim-quality.md", "CLAUDE.md", "CONVENTIONS.md", "README.md"}

FRONTMATTER_BLOCK = re.compile(
    r"<!--\s*kb-frontmatter\s*\n(.*?)\n-->", re.DOTALL
)
CANONICAL_ID = re.compile(r"<!-- id: ([a-z0-9]{6}) -->")
TIER2_INLINE = re.compile(r"<!--\s*claim-quality:\s*(.*?)\s*-->", re.DOTALL)
ID_RE = re.compile(r"\b([a-z0-9]{6})\b")
FENCE = re.compile(r"^```")


def strip_code_fences(text: str) -> str:
    out = []
    in_fence = False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else line)
    return "\n".join(out)


def parse_frontmatter(text: str) -> dict | None:
    m = FRONTMATTER_BLOCK.search(text)
    if not m:
        return None
    body = m.group(1)
    fields: dict = {}
    for line in body.splitlines():
        line = line.rstrip()
        if not line or ":" not in line:
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


def collect_files() -> list[tuple[Path, dict | None]]:
    out: list[tuple[Path, dict | None]] = []
    for root, dirs, files in os.walk(KB):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for f in files:
            if not f.endswith(".md") or f in EXCLUDE_NAMES:
                continue
            p = Path(root) / f
            text = p.read_text()
            out.append((p, parse_frontmatter(text)))
    return out


def collect_canonical_ids() -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for p in KB.rglob("claim-quality.md"):
        scrubbed = strip_code_fences(p.read_text())
        for m in CANONICAL_ID.findall(scrubbed):
            out.append((m, str(p.relative_to(KB))))
    return out


def check_frontmatter_presence(files: list[tuple[Path, dict | None]]):
    """Return list of (path, kind-guessed) for files without frontmatter."""
    failures = []
    for p, fm in files:
        if fm is None:
            failures.append(str(p.relative_to(KB)))
    return failures


def check_tier1_coverage(files: list[tuple[Path, dict | None]]):
    """Leaf or leaf-as-index missing both claims and no-claim, OR with both."""
    failures = []
    for p, fm in files:
        if fm is None:
            continue
        kind = fm.get("kind")
        if kind not in ("leaf", "leaf-as-index"):
            continue
        has_claims = "claims" in fm and bool(fm["claims"])
        has_no_claim = "no-claim" in fm and bool(fm["no-claim"])
        if not has_claims and not has_no_claim:
            failures.append((str(p.relative_to(KB)), "neither claims nor no-claim"))
        elif has_claims and has_no_claim:
            failures.append((str(p.relative_to(KB)), "BOTH claims and no-claim"))
    return failures


def check_tier2_coverage(files: list[tuple[Path, dict | None]]):
    failures = []
    for p, fm in files:
        if fm is None:
            continue
        ids = fm.get("claims", [])
        if len(ids) < 2:
            continue
        text = p.read_text()
        # Scrub the frontmatter block so its own claims line doesn't count
        scrubbed = FRONTMATTER_BLOCK.sub("", text)
        markers = TIER2_INLINE.findall(scrubbed)
        missing = [
            i
            for i in ids
            if not any(re.search(rf"\b{re.escape(i)}\b", body) for body in markers)
        ]
        if missing:
            failures.append((str(p.relative_to(KB)), ids, missing))
    return failures


def check_id_uniqueness(canonical: list[tuple[str, str]]):
    locations: dict[str, list[str]] = defaultdict(list)
    for cid, path in canonical:
        locations[cid].append(path)
    return {cid: paths for cid, paths in locations.items() if len(paths) > 1}


def check_orphan_refs(files: list[tuple[Path, dict | None]], canonical_set: set[str]):
    orphans: dict[str, list[str]] = defaultdict(list)
    for p, fm in files:
        if fm is None:
            continue
        for i in fm.get("claims", []):
            if i not in canonical_set:
                orphans[i].append(str(p.relative_to(KB)))
    return dict(orphans)


def check_subtree_consistency(files: list[tuple[Path, dict | None]]):
    """For each kind: index, subtree-claims must equal union of leaf claims under it.
    For kind: entry-point, must equal global union."""
    failures = []
    leaves = [(p, fm) for p, fm in files
              if fm and fm.get("kind") in ("leaf", "leaf-as-index")]
    for p, fm in files:
        if fm is None:
            continue
        kind = fm.get("kind")
        if kind == "index":
            idx_dir = p.parent
            expected = set()
            for leaf, lfm in leaves:
                try:
                    leaf.relative_to(idx_dir)
                    expected.update(lfm.get("claims", []))
                except ValueError:
                    continue
            declared = set(fm.get("subtree-claims", []))
            if declared != expected:
                failures.append((
                    str(p.relative_to(KB)),
                    sorted(expected - declared),
                    sorted(declared - expected),
                ))
        elif kind == "entry-point":
            expected = set()
            for _, lfm in leaves:
                expected.update(lfm.get("claims", []))
            declared = set(fm.get("subtree-claims", []))
            if declared != expected:
                failures.append((
                    str(p.relative_to(KB)),
                    sorted(expected - declared),
                    sorted(declared - expected),
                ))
    return failures


def check_uncited_entries(canonical: list[tuple[str, str]],
                          files: list[tuple[Path, dict | None]]):
    cited: set[str] = set()
    for _, fm in files:
        if fm:
            cited.update(fm.get("claims", []))
    return [(cid, path) for cid, path in canonical if cid not in cited]


def main() -> int:
    if not KB.is_dir():
        print(f"FAIL: {KB} not found. Run from repository root.", file=sys.stderr)
        return 2

    files = collect_files()
    canonical = collect_canonical_ids()
    canonical_set = {cid for cid, _ in canonical}

    fm_missing = check_frontmatter_presence(files)
    t1_failures = check_tier1_coverage(files)
    t2_failures = check_tier2_coverage(files)
    id_dupes = check_id_uniqueness(canonical)
    orphans = check_orphan_refs(files, canonical_set)
    subtree_failures = check_subtree_consistency(files)
    uncited = check_uncited_entries(canonical, files)

    n_files = len(files)
    n_with_fm = sum(1 for _, fm in files if fm is not None)
    n_leaves = sum(1 for _, fm in files if fm and fm.get("kind") in ("leaf", "leaf-as-index"))
    n_with_claims = sum(1 for _, fm in files if fm and fm.get("claims"))
    n_no_claim = sum(1 for _, fm in files if fm and fm.get("no-claim"))
    n_multi = sum(1 for _, fm in files if fm and len(fm.get("claims", [])) >= 2)

    print(
        f"[claim-quality] Scanned {n_files} files "
        f"({n_with_fm} with frontmatter, {n_leaves} leaves, "
        f"{n_with_claims} with claims, {n_no_claim} no-claim, "
        f"{n_multi} multi-claim) and {len(canonical)} canonical entries."
    )

    has_failures = False
    refresh_fixable = False

    if fm_missing:
        has_failures = True
        # Index files without frontmatter are refresh-fixable; leaves are not.
        for p in fm_missing:
            if p.endswith("/index.md") or p == "entry-point.md":
                refresh_fixable = True
        print(f"\n[FAIL] {len(fm_missing)} files missing frontmatter:")
        for p in fm_missing:
            print(f"  {p}")

    if t1_failures:
        has_failures = True
        print(f"\n[FAIL] {len(t1_failures)} leaves with malformed claims/no-claim:")
        for p, reason in t1_failures:
            print(f"  {p}: {reason}")

    if t2_failures:
        has_failures = True
        print(f"\n[FAIL] {len(t2_failures)} multi-claim leaves missing Tier 2 markers:")
        for p, ids, miss in t2_failures:
            print(f"  {p}")
            print(f"    claims: {ids}, missing inline markers for: {miss}")

    if id_dupes:
        has_failures = True
        print(f"\n[FAIL] {len(id_dupes)} duplicate canonical IDs:")
        for cid, paths in id_dupes.items():
            print(f"  {cid} ({len(paths)} occurrences)")
            for path in paths:
                print(f"    in {path}")

    if orphans:
        has_failures = True
        print(f"\n[FAIL] {len(orphans)} Tier 1 IDs don't resolve to a canonical entry:")
        for cid, paths in orphans.items():
            n = len(paths)
            print(f"  {cid} (cited by {n} leaf{'s' if n != 1 else ''})")
            for path in paths[:3]:
                print(f"    {path}")
            if n > 3:
                print(f"    ... and {n - 3} more")

    if subtree_failures:
        has_failures = True
        refresh_fixable = True
        print(f"\n[FAIL] {len(subtree_failures)} indexes with subtree-claims drift:")
        for p, missing, extra in subtree_failures:
            print(f"  {p}")
            if missing:
                print(f"    missing from declared: {missing}")
            if extra:
                print(f"    extra in declared: {extra}")

    if uncited:
        has_failures = True
        print(f"\n[FAIL] {len(uncited)} canonical entries have no leaf citation:")
        for cid, path in uncited:
            print(f"  {cid} (in {path})")
        print(
            "  → Either back-link from a leaf's claims, or remove the entry. "
            "Meta-claims and reading-hazards belong in CLAUDE.md / "
            "CONVENTIONS.md / LIVING_REFERENCE.md, not here."
        )

    if has_failures:
        if refresh_fixable:
            print(
                "\n[claim-quality] FAIL — some failures are derivation-only "
                "(subtree drift, missing index frontmatter). Try "
                "`make refresh-kb-metadata` first; if anything remains, "
                "those are real defects."
            )
        else:
            print("\n[claim-quality] FAIL — fix the above and re-run.")
        return 1

    print("[claim-quality] PASS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

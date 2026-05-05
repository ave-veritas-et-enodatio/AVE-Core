#!/usr/bin/env python3
"""Mechanical integrity check for the AVE knowledge-base claim-quality framework.

Enforces INVARIANT-S5, INVARIANT-S7, and INVARIANT-S8 from
``manuscript/ave-kb/CLAUDE.md``. Eight checks, all hard fail-loud:

    1. Tier 1 coverage: every leaf has either a Tier 1 line OR an inline
       ``<!-- no-claim: <reason> -->`` marker. The reason lives with the
       leaf (not in this script).
    2. Tier 2 coverage: every multi-claim leaf has proximal markers for
       each ID in its Tier 1 list.
    3. ID uniqueness: no canonical ``<!-- id: xxxxxx -->`` appears twice.
       Canonical IDs are detected outside fenced code blocks only —
       example IDs inside docs don't count.
    4. Orphan refs: every Tier 1 ID resolves to a canonical entry.
    5. Index subtree-ID line: every ``index.md`` carries a subtree
       line, except leaf-as-index documents (line 2 = leaf marker).
    6. Subtree consistency: each index's declared subtree-ID list
       equals the union of Tier 1 IDs from leaves below it.
    7. Bidirectional coverage: every canonical entry is back-linked by
       at least one leaf's Tier 1 line. Meta-claims and reading-hazards
       have no leaf origin and don't belong here — they live in
       CLAUDE.md / CONVENTIONS.md / LIVING_REFERENCE.md instead.
    8. No-claim consistency: a leaf cannot carry both a Tier 1 line and
       a no-claim marker.

Run from the repository root::

    ./.venv/bin/python manuscript/ave-kb/tools/check-claim-quality.py

Or via the build system::

    make verify-claim-quality
"""

from __future__ import annotations

import os
import re
import sys
from collections import defaultdict
from pathlib import Path

KB = Path("manuscript/ave-kb")

ID_PATTERN = re.compile(r"\b([a-z0-9]{6})\b")
CQ_BLOCK = re.compile(r"<!--\s*claim-quality:\s*(.*?)\s*-->", re.DOTALL)
CANONICAL_ID = re.compile(r"<!-- id: ([a-z0-9]{6}) -->")
SUBTREE_LINE = re.compile(r"<!--\s*claim-quality \(subtree\):\s*([^>]*?)\s*-->")
NO_CLAIM_MARKER = re.compile(r"<!--\s*no-claim:\s*(.+?)\s*-->", re.DOTALL)
FENCE = re.compile(r"^```")


def strip_code_fences(text: str) -> str:
    """Return text with fenced code blocks removed (keeping line count via blanks).

    Canonical-ID detection should ignore example IDs that appear inside
    documentation code blocks; only IDs in actual entry positions count.
    """
    out_lines = []
    in_fence = False
    for line in text.splitlines():
        if FENCE.match(line):
            in_fence = not in_fence
            out_lines.append("")
            continue
        out_lines.append("" if in_fence else line)
    return "\n".join(out_lines)


def find_leaves() -> list[tuple[Path, list[str], str | None]]:
    """Return ``[(path, tier1_ids, no_claim_reason)]`` for every leaf in the KB.

    A leaf is any ``.md`` file (not ``claim-quality.md``) whose line 2 is
    ``<!-- leaf: verbatim -->``. ``no_claim_reason`` is the body of the
    inline ``<!-- no-claim: ... -->`` marker if present, else ``None``.
    """
    leaves: list[tuple[Path, list[str], str | None]] = []
    for root, _, files in os.walk(KB):
        for f in files:
            if not f.endswith(".md") or f == "claim-quality.md":
                continue
            p = Path(root) / f
            text = p.read_text()
            lines = text.splitlines()
            if len(lines) < 2 or "<!-- leaf: verbatim -->" not in lines[1]:
                continue
            t1_line = next(
                (
                    line
                    for line in lines[:12]
                    if line.startswith("<!-- claim-quality:") and "subtree" not in line
                ),
                None,
            )
            ids: list[str] = []
            if t1_line:
                m = re.match(
                    r"<!--\s*claim-quality:\s*([^(]*?)(?:\s*\(|\s*-->)",
                    t1_line,
                )
                if m:
                    ids = ID_PATTERN.findall(m.group(1))
            no_claim_reason = None
            for line in lines[:12]:
                m = NO_CLAIM_MARKER.match(line.strip())
                if m:
                    no_claim_reason = m.group(1).strip()
                    break
            leaves.append((p, ids, no_claim_reason))
    return leaves


def collect_canonical_ids() -> list[tuple[str, str]]:
    """Return ``[(id, claim-quality.md path)]`` for every canonical entry.

    IDs inside fenced code blocks are ignored — they are documentation
    examples, not actual entries.
    """
    out: list[tuple[str, str]] = []
    for p in KB.rglob("claim-quality.md"):
        scrubbed = strip_code_fences(p.read_text())
        for m in CANONICAL_ID.findall(scrubbed):
            out.append((m, str(p.relative_to(KB))))
    return out


def check_tier1_coverage(leaves: list[tuple[Path, list[str], str | None]]) -> list[str]:
    failures = []
    for p, ids, no_claim in leaves:
        if not ids and not no_claim:
            failures.append(str(p.relative_to(KB)))
    return failures


def check_tier2_coverage(
    leaves: list[tuple[Path, list[str], str | None]],
) -> list[tuple[str, list[str], list[str]]]:
    failures = []
    for p, ids, _ in leaves:
        if len(ids) < 2:
            continue
        text = p.read_text()
        matches = CQ_BLOCK.findall(text)
        real = [m for m in matches if "subtree" not in m]
        t2_bodies = real[1:]
        missing = [
            i
            for i in ids
            if not any(re.search(rf"\b{re.escape(i)}\b", body) for body in t2_bodies)
        ]
        if missing:
            failures.append((str(p.relative_to(KB)), ids, missing))
    return failures


def check_id_uniqueness(canonical: list[tuple[str, str]]) -> dict[str, list[str]]:
    """Return ``{duplicate_id: [paths]}`` for IDs that appear more than once."""
    locations: dict[str, list[str]] = defaultdict(list)
    for cid, path in canonical:
        locations[cid].append(path)
    return {cid: paths for cid, paths in locations.items() if len(paths) > 1}


def check_orphan_refs(
    leaves: list[tuple[Path, list[str], str | None]],
    canonical_set: set[str],
) -> dict[str, list[str]]:
    orphans: dict[str, list[str]] = defaultdict(list)
    for p, ids, _ in leaves:
        for i in ids:
            if i not in canonical_set:
                orphans[i].append(str(p.relative_to(KB)))
    return dict(orphans)


def check_index_subtree_lines() -> list[str]:
    failures = []
    for p in KB.rglob("index.md"):
        text = p.read_text()
        lines = text.splitlines()
        is_leaf_as_index = (
            len(lines) >= 2 and "<!-- leaf: verbatim -->" in lines[1]
        )
        has_subtree = "<!-- claim-quality (subtree):" in text
        if not has_subtree and not is_leaf_as_index:
            failures.append(str(p.relative_to(KB)))
    return failures


def check_subtree_consistency(
    leaves: list[tuple[Path, list[str], str | None]],
) -> list[tuple[str, list[str], list[str]]]:
    """Each index's declared subtree-ID list must equal the union of Tier 1
    IDs from leaves under its directory. Leaf-as-index documents are
    exempt — their Tier 1 line subsumes the subtree summary.
    """
    failures = []
    for idx in KB.rglob("index.md"):
        text = idx.read_text()
        lines = text.splitlines()
        is_leaf_as_index = (
            len(lines) >= 2 and "<!-- leaf: verbatim -->" in lines[1]
        )
        if is_leaf_as_index:
            continue
        m = SUBTREE_LINE.search(text)
        if not m:
            continue
        declared = set(ID_PATTERN.findall(m.group(1)))

        idx_dir = idx.parent
        expected: set[str] = set()
        for leaf, ids, _ in leaves:
            try:
                leaf.relative_to(idx_dir)
            except ValueError:
                continue
            expected.update(ids)

        if declared != expected:
            missing = sorted(expected - declared)
            extra = sorted(declared - expected)
            failures.append((str(idx.relative_to(KB)), missing, extra))
    return failures


def check_uncited_entries(
    canonical: list[tuple[str, str]],
    leaves: list[tuple[Path, list[str], str | None]],
) -> list[tuple[str, str]]:
    """Every canonical entry must be cited by ≥1 leaf. Meta-claims that
    don't bind to a leaf belong in CLAUDE.md / CONVENTIONS.md /
    LIVING_REFERENCE.md, not in claim-quality.md.
    """
    cited: set[str] = set()
    for _, ids, _ in leaves:
        cited.update(ids)
    return [(cid, path) for cid, path in canonical if cid not in cited]


def check_no_claim_consistency(
    leaves: list[tuple[Path, list[str], str | None]],
) -> list[str]:
    """A leaf cannot carry both a Tier 1 line and a no-claim marker."""
    failures = []
    for p, ids, no_claim in leaves:
        if ids and no_claim:
            failures.append(str(p.relative_to(KB)))
    return failures


def main() -> int:
    if not KB.is_dir():
        print(
            f"[claim-quality] FAIL — {KB} not found. Run from repository root.",
            file=sys.stderr,
        )
        return 2

    leaves = find_leaves()
    canonical = collect_canonical_ids()
    canonical_set = {cid for cid, _ in canonical}

    failures = {
        "tier1_coverage": check_tier1_coverage(leaves),
        "tier2_coverage": check_tier2_coverage(leaves),
        "id_uniqueness": check_id_uniqueness(canonical),
        "orphan_refs": check_orphan_refs(leaves, canonical_set),
        "index_subtree_lines": check_index_subtree_lines(),
        "subtree_consistency": check_subtree_consistency(leaves),
        "uncited_entries": check_uncited_entries(canonical, leaves),
        "no_claim_consistency": check_no_claim_consistency(leaves),
    }

    n_with_t1 = sum(1 for _, ids, _ in leaves if ids)
    n_no_claim = sum(1 for _, _, nc in leaves if nc)
    n_multi = sum(1 for _, ids, _ in leaves if len(ids) >= 2)
    print(
        f"[claim-quality] Scanned {len(leaves)} leaves "
        f"({n_with_t1} with Tier 1, {n_no_claim} no-claim, "
        f"{n_multi} multi-claim) and {len(canonical)} canonical entries."
    )

    has_failures = False

    if failures["tier1_coverage"]:
        has_failures = True
        print(
            f"\n[FAIL] {len(failures['tier1_coverage'])} leaves have neither "
            f"a Tier 1 line nor a no-claim marker:"
        )
        for p in failures["tier1_coverage"]:
            print(f"  {p}")
        print(
            "  → Add `<!-- claim-quality: <id>, ... -->` after the leaf marker, "
            "OR add `<!-- no-claim: <reason> -->` if the leaf carries no claim."
        )

    if failures["tier2_coverage"]:
        has_failures = True
        print(
            f"\n[FAIL] {len(failures['tier2_coverage'])} multi-claim leaves "
            f"missing proximal Tier 2 markers:"
        )
        for p, ids, miss in failures["tier2_coverage"]:
            print(f"  {p}")
            print(f"    Tier 1: {ids}, missing markers for: {miss}")

    if failures["id_uniqueness"]:
        has_failures = True
        print(f"\n[FAIL] {len(failures['id_uniqueness'])} duplicate canonical IDs:")
        for cid, paths in failures["id_uniqueness"].items():
            print(f"  {cid} ({len(paths)} occurrences)")
            for path in paths:
                print(f"    in {path}")

    if failures["orphan_refs"]:
        has_failures = True
        print(
            f"\n[FAIL] {len(failures['orphan_refs'])} Tier 1 IDs don't resolve "
            f"to a canonical entry:"
        )
        for cid, leaves_citing in failures["orphan_refs"].items():
            n = len(leaves_citing)
            print(f"  {cid} (cited by {n} leaf{'s' if n != 1 else ''})")
            for path in leaves_citing[:3]:
                print(f"    {path}")
            if n > 3:
                print(f"    ... and {n - 3} more")

    if failures["index_subtree_lines"]:
        has_failures = True
        print(
            f"\n[FAIL] {len(failures['index_subtree_lines'])} indexes "
            f"missing the subtree-ID line:"
        )
        for p in failures["index_subtree_lines"]:
            print(f"  {p}")
        print("  → Add `<!-- claim-quality (subtree): ... -->` after the up-link line.")

    if failures["subtree_consistency"]:
        has_failures = True
        print(
            f"\n[FAIL] {len(failures['subtree_consistency'])} indexes "
            f"with subtree-ID drift:"
        )
        for p, missing, extra in failures["subtree_consistency"]:
            print(f"  {p}")
            if missing:
                print(f"    missing from declared list: {missing}")
            if extra:
                print(f"    extra in declared list: {extra}")
        print("  → Regenerate the subtree-ID line from the union of leaf Tier 1 IDs.")

    if failures["uncited_entries"]:
        has_failures = True
        print(
            f"\n[FAIL] {len(failures['uncited_entries'])} canonical entries "
            f"have no leaf citation:"
        )
        for cid, path in failures["uncited_entries"]:
            print(f"  {cid} (in {path})")
        print(
            "  → Either back-link each from the relevant leaves' Tier 1 lines, "
            "or remove the entry. Meta-claims and reading-hazards belong in "
            "CLAUDE.md / CONVENTIONS.md / LIVING_REFERENCE.md, not here."
        )

    if failures["no_claim_consistency"]:
        has_failures = True
        print(
            f"\n[FAIL] {len(failures['no_claim_consistency'])} leaves carry "
            f"BOTH a Tier 1 line and a no-claim marker (mutually exclusive):"
        )
        for p in failures["no_claim_consistency"]:
            print(f"  {p}")
        print("  → Remove one or the other.")

    if has_failures:
        print("\n[claim-quality] FAIL — fix the above and re-run.")
        return 1

    print("[claim-quality] PASS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

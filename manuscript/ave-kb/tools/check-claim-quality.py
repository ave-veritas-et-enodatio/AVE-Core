#!/usr/bin/env python3
"""Mechanical integrity check for the AVE knowledge-base claim-quality framework.

Read-only. Never modifies any file. Reads the unified ``kb-frontmatter`` block
(see ``mad-review/kb-metadata-spine-spec.md``).

Eleven checks, all hard fail-loud:

    1. Tier 1 coverage: every leaf has either ``claims:`` or ``no-claim:`` in
       its frontmatter (mutually exclusive).
    2. Tier 2 coverage: every multi-claim leaf has proximal inline markers
       (``<!-- claim-quality: <id> ... -->``) for each ID in its claims list.
    3. ID uniqueness: no canonical ``<!-- id: clm-xxxxxx -->`` appears twice
       in any ``claim-quality.md`` register.
    4. Orphan refs: every Tier 1 ID resolves to a canonical entry.
    5. Frontmatter presence: every non-excluded .md file has a frontmatter
       block (refresh-fixable for indexes; manual fix for leaves).
    6. Subtree consistency: each ``kind: index`` file's ``subtree-claims``
       equals the union of leaf claims under its directory; entry-point's
       equals the global union. (refresh-fixable.)
    7. Bidirectional coverage: every canonical entry is back-linked by at
       least one leaf's frontmatter.
    8. No-claim/claims exclusivity: no leaf carries both fields.
    9. Index files well-formed: each ``.index/*.jsonl`` exists, every line
       parses as a JSON object, and the file ends with exactly one ``\\n``.
       Missing files and EOF defects are refresh-fixable; malformed JSON is
       not (indicates a bug or merge corruption).
   10. Index freshness: each ``.index/*.jsonl`` matches the canonical
       byte-for-byte serialization of the in-memory record set built from
       the canonical KB sources. (refresh-fixable.)
   11. Index referential integrity: every claim id referenced in
       depends-on / strengthen-by / cites / subtree-aggregates appears as
       a record in claims.jsonl. (Not refresh-fixable; symptom of a build
       bug.)

Failure categories are tagged refresh-fixable or manual-fix. If any
refresh-fixable failures are present, the report ends with a hint to run
``make refresh-kb-metadata`` first; verify is read-only and never auto-fixes.

Run via::

    ./.venv/bin/python manuscript/ave-kb/tools/check-claim-quality.py
    make verify-claim-quality
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# Make the sibling kb_index_lib importable regardless of invocation cwd.
_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

import kb_index_lib  # noqa: E402

KB = Path("manuscript/ave-kb")

# Documented JSONL files emitted by the index pipeline (short names).
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
CANONICAL_ID = re.compile(r"<!-- id: (clm-[a-z0-9]{6}) -->")
TIER2_INLINE = re.compile(r"<!--\s*claim-quality:\s*(.*?)\s*-->", re.DOTALL)
ID_RE = re.compile(r"\b(clm-[a-z0-9]{6})\b")
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


def check_index_well_formed(index_dir: Path):
    """Validate each .index JSONL file: exists, parses, has clean EOF.

    Returns (missing, malformed, eof_defects):

    * ``missing``: list of short names absent from disk. Refresh-fixable.
    * ``malformed``: list of (short_name, lineno, snippet) for lines that
      either fail to parse as JSON or parse to a non-object. NOT
      refresh-fixable; signals a deeper bug.
    * ``eof_defects``: list of (short_name, reason) for files with a
      missing or doubled trailing newline. Refresh-fixable.
    """
    missing: list[str] = []
    malformed: list[tuple[str, int, str]] = []
    eof_defects: list[tuple[str, str]] = []
    for short in INDEX_FILES:
        path = index_dir / f"{short}.jsonl"
        if not path.exists():
            missing.append(short)
            continue
        raw = path.read_bytes()
        if not raw:
            # An empty file is well-formed per write_jsonl semantics, but
            # for the real KB every file is non-empty; if it is empty we
            # treat that as a freshness defect, caught by check_index_fresh.
            continue
        if not raw.endswith(b"\n"):
            eof_defects.append((short, "missing final newline"))
        elif raw.endswith(b"\n\n"):
            eof_defects.append((short, "multiple trailing newlines"))
        text = raw.decode("utf-8", errors="replace")
        for lineno, line in enumerate(text.split("\n"), start=1):
            # Last element after a trailing newline is the empty string;
            # don't treat it as a malformed record.
            if line == "":
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                snippet = line if len(line) <= 80 else line[:77] + "..."
                malformed.append((short, lineno, f"{exc.msg}: {snippet}"))
                continue
            if not isinstance(obj, dict):
                malformed.append(
                    (short, lineno, f"line is not a JSON object: {type(obj).__name__}")
                )
    return missing, malformed, eof_defects


def check_index_fresh(index_dir: Path):
    """Diff each on-disk JSONL against canonical serialization of expected records.

    Returns a list of (short_name, expected_count, actual_count) for files
    whose bytes diverge from canonical. Refresh-fixable.

    Files that are missing or malformed are skipped here — the well-formed
    check already surfaces those; running a byte-diff on a malformed file
    would be misleading noise.
    """
    state = kb_index_lib.discover_kb(KB, diagnostic_stream=None)
    expected = kb_index_lib.build_all_records(state)

    drift: list[tuple[str, int, int]] = []
    for short in INDEX_FILES:
        path = index_dir / f"{short}.jsonl"
        if not path.exists():
            continue
        expected_bytes = kb_index_lib.serialize_records(expected[short])
        actual_bytes = path.read_bytes()
        if actual_bytes == expected_bytes:
            continue
        expected_count = len(expected[short])
        actual_count = sum(1 for ln in actual_bytes.decode("utf-8", errors="replace").split("\n") if ln)
        drift.append((short, expected_count, actual_count))
    return drift, expected


def check_index_referential_integrity(index_dir: Path):
    """Every claim id in any non-claims index file must appear in claims.jsonl.

    Returns a list of (short_name, claim_id, location) tuples for orphan
    references. NOT refresh-fixable; indicates a build bug (refresh should
    never emit an orphan).

    Skipped silently if claims.jsonl is missing or malformed — the
    well-formed check surfaces that.
    """
    claims_path = index_dir / "claims.jsonl"
    if not claims_path.exists():
        return []
    try:
        canonical = {
            json.loads(ln)["id"]
            for ln in claims_path.read_text(encoding="utf-8").split("\n")
            if ln
        }
    except (json.JSONDecodeError, KeyError):
        return []

    violations: list[tuple[str, str, str]] = []

    def _check_lines(short: str, key_funcs):
        path = index_dir / f"{short}.jsonl"
        if not path.exists():
            return
        for lineno, line in enumerate(
            path.read_text(encoding="utf-8").split("\n"), start=1
        ):
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            for key, getter in key_funcs:
                ids = getter(rec)
                for cid in ids:
                    if cid not in canonical:
                        violations.append((short, cid, f"line {lineno}, {key}"))

    _check_lines(
        "depends-on",
        [
            ("source", lambda r: [r.get("source")] if r.get("source") else []),
            ("target", lambda r: [r.get("target")] if r.get("target") else []),
        ],
    )
    _check_lines(
        "strengthen-by",
        [("claim_id", lambda r: [r.get("claim_id")] if r.get("claim_id") else [])],
    )
    _check_lines(
        "cites",
        [("claim_id", lambda r: [r.get("claim_id")] if r.get("claim_id") else [])],
    )
    _check_lines(
        "subtree-aggregates",
        [("subtree_claims", lambda r: list(r.get("subtree_claims") or []))],
    )

    return violations


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Mechanical KB claim-quality and derived-index verifier."
    )
    parser.add_argument(
        "--index-dir",
        type=Path,
        default=None,
        help=(
            "Directory containing the .index/*.jsonl files. Defaults to "
            "manuscript/ave-kb/.index/. Used by tests to point at a synthetic "
            "index tree without disturbing the canonical one."
        ),
    )
    args = parser.parse_args(argv)
    index_dir = args.index_dir if args.index_dir is not None else (KB / ".index")

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

    # Index-state checks.
    missing_index, malformed_index, eof_defects = check_index_well_formed(index_dir)
    fresh_drift, expected_records = check_index_fresh(index_dir)
    ref_violations = check_index_referential_integrity(index_dir)

    # Index summary line — counts come from the canonical (expected) record
    # set so the line is meaningful even when on-disk files are stale.
    print(
        f"[index] {len(INDEX_FILES)} JSONL files "
        f"({len(expected_records['claims'])} claims, "
        f"{len(expected_records['depends-on'])} depends-on, "
        f"{len(expected_records['strengthen-by'])} strengthen-by, "
        f"{len(expected_records['cites'])} citations, "
        f"{len(expected_records['subtree-aggregates'])} aggregates)."
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

    if missing_index:
        has_failures = True
        refresh_fixable = True
        print(
            f"\n[FAIL] {len(missing_index)} .index JSONL file(s) missing from "
            f"{index_dir}:"
        )
        for short in missing_index:
            print(f"  {short}.jsonl")

    if eof_defects:
        has_failures = True
        refresh_fixable = True
        print(f"\n[FAIL] {len(eof_defects)} .index file(s) with EOF defects:")
        for short, reason in eof_defects:
            print(f"  {short}.jsonl: {reason}")

    if malformed_index:
        has_failures = True
        print(
            f"\n[FAIL] {len(malformed_index)} malformed line(s) in .index "
            f"JSONL (not well-formed JSON):"
        )
        for short, lineno, detail in malformed_index:
            print(f"  {short}.jsonl:{lineno}: {detail}")
        print(
            "  → This is not refresh-fixable. Investigate the build pipeline "
            "or a merge corruption; the file should be regenerable from "
            "canonical sources only after the cause is identified."
        )

    if fresh_drift:
        has_failures = True
        refresh_fixable = True
        print(f"\n[FAIL] {len(fresh_drift)} .index file(s) stale vs canonical state:")
        for short, expected_count, actual_count in fresh_drift:
            print(
                f"  {short}.jsonl: {expected_count} expected vs "
                f"{actual_count} actual records"
            )

    if ref_violations:
        has_failures = True
        print(
            f"\n[FAIL] {len(ref_violations)} referential-integrity violation(s) "
            f"in .index/ — claim ids cited outside claims.jsonl:"
        )
        # Group by (short, cid) to keep output compact.
        grouped: dict[tuple[str, str], list[str]] = defaultdict(list)
        for short, cid, location in ref_violations:
            grouped[(short, cid)].append(location)
        for (short, cid), locations in grouped.items():
            n = len(locations)
            print(f"  {short}.jsonl: orphan id {cid!r} ({n} occurrence{'s' if n != 1 else ''})")
            for loc in locations[:3]:
                print(f"    {loc}")
            if n > 3:
                print(f"    ... and {n - 3} more")
        print(
            "  → Not refresh-fixable. Indicates a bug in the index builder "
            "(refresh should never emit an orphan reference)."
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

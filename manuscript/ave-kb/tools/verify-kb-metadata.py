#!/usr/bin/env python3
"""Mechanical integrity check for the AVE knowledge-base claim-quality framework.

Read-only. Never modifies any file. Reads the unified ``kb-frontmatter`` block
(see ``mad-review/kb-metadata-spine-spec.md``).

Fourteen checks, all hard fail-loud:

    0. Quality-block integrity: every ``### Quality`` heading in a
       ``claim-quality.md`` register sits within a ``---``-delimited section
       that also carries the claim's ``## <title>`` heading and its
       ``<!-- id: clm-xxxxxx -->`` marker. An orphan ``### Quality`` block is
       a hard failure. (Not refresh-fixable; delete the orphan or restore the
       missing title/id.)
    1. Tier 1 coverage: every leaf declares its content via at least one of
       ``{claims:, no-claim:, exp-id:}`` (hosting an experiment node satisfies
       coverage on its own). ``claims`` and ``no-claim`` stay mutually exclusive
       with each other; ``exp-id`` is orthogonal and may co-exist with either.
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
   11. Index referential integrity: every id referenced in depends-on /
       strengthen-by / cites / subtree-aggregates resolves to a record in
       claims.jsonl (which holds claim + framework nodes), and every
       depends-on edge's target_kind matches the resolved node's node_type.
       (Not refresh-fixable; symptom of a build bug.)
   12. Solidity-graph acyclicity: the claim depends-on graph must be a DAG.
       A cycle makes solidity undefined for its members. (Not refresh-fixable;
       the cycle must be broken in the claim depends-on declarations.)
   13. Solidity freshness: every claim entry's on-disk ``solidity`` line and
       the depends-on ``(solidity X)`` annotations must equal what
       ``kb_index_lib.compute_solidity`` derives, and the ``.index/claims.jsonl``
       solidity fields must match. ``solidity`` is a derived field — drift
       means refresh has not been run. (refresh-fixable.)
   14. Leaf-references freshness: every claim-quality entry's on-disk
       ``> **Leaf references:**`` footer must equal what
       ``kb_index_lib.build_leaf_references`` derives from the reverse-citation
       map (which leaves host the entry's id). The footer is a derived field;
       a hand-edited, stale, or missing footer is drift. (refresh-fixable.)

Future / queued (not implemented):

* A relative-link integrity check — verify that each Markdown
  cross-reference in a leaf resolves to an existing file, and surface dead
  *forward* links (a foundational common/ or vol1 leaf pointing to a
  not-yet-migrated later-volume leaf) as an optional warning rather than a
  hard failure. Such forward links are intentional threads for later
  cross-reference stitching passes; only their dead-ness is worth flagging,
  not their existence.

Failure categories are tagged refresh-fixable or manual-fix. If any
refresh-fixable failures are present, the report ends with a hint to run
``make refresh-kb-metadata`` first; verify is read-only and never auto-fixes.

Run via::

    ./.venv/bin/python manuscript/ave-kb/tools/verify-kb-metadata.py
    make verify-kb-metadata
"""

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# Sibling kb_index_lib resolves via PYTHONPATH (set by the make target).
import kb_index_lib

KB = Path("manuscript/ave-kb")

# Documented JSONL files emitted by the index pipeline (short names).
INDEX_FILES = (
    "claims",
    "depends-on",
    "strengthen-by",
    "supported-by",
    "cites",
    "subtree-aggregates",
)

EXCLUDE_DIRS = {"session", ".index", "tools"}
EXCLUDE_NAMES = {"claim-quality.md", "claim-quality-closure-roadmap.md", "CLAUDE.md", "CONVENTIONS.md", "README.md"}

FRONTMATTER_BLOCK = re.compile(
    r"<!--\s*kb-frontmatter\s*\n(.*?)\n-->", re.DOTALL
)
CANONICAL_ID = re.compile(r"<!-- id: (clm-[a-z0-9]{6}) -->")
# A claim OR support entry marker — both carry a `### Quality` block, so the
# quality-block integrity check accepts either prefix (INVARIANT-S10).
CANONICAL_ANY_ID = re.compile(r"<!-- id: ((?:clm|sup)-[a-z0-9]{6}) -->")
TIER2_INLINE = re.compile(r"<!--\s*claim-quality:\s*(.*?)\s*-->", re.DOTALL)
ID_RE = re.compile(r"\b(clm-[a-z0-9]{6})\b")
EXP_ID_RE = re.compile(r"\bexp-[a-z0-9]{6}\b")
SUP_ID_RE = re.compile(r"\bsup-[a-z0-9]{6}\b")
# Either prefix — for id-list frontmatter values that may hold clm- ids
# (claims:, subtree-claims:) or exp- ids (experiments:, subtree-experiments:).
ANY_ID_RE = re.compile(r"\b((?:clm|exp)-[a-z0-9]{6})\b")
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
            # clm- ids (claims:, subtree-claims:) or exp- ids (experiments:,
            # subtree-experiments:) — accept both prefixes.
            fields[key] = ANY_ID_RE.findall(value)
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
        if any(part in EXCLUDE_DIRS for part in p.relative_to(KB).parts[:-1]):
            continue
        scrubbed = strip_code_fences(p.read_text())
        for m in CANONICAL_ID.findall(scrubbed):
            out.append((m, str(p.relative_to(KB))))
    return out


def check_quality_block_integrity():
    """Every `### Quality` heading must sit in a well-formed claim section.

    Walks each ``claim-quality.md`` register, splits it into ``---``-delimited
    sections (after blanking fenced code blocks so the Quality Convention
    preamble's format-example snippet does not count), and requires that any
    section carrying a ``### Quality`` heading also carries a ``## <title>``
    heading AND a ``<!-- id: clm-xxxxxx -->`` marker. An orphan ``### Quality``
    block — one with no claim title and no canonical id — is a hard failure;
    it is the defect this check makes non-recurring.

    Returns a list of (register_path, line, reason) for each malformed block.
    Line numbers are 1-based and point at the offending ``### Quality``
    heading. Scoped to the registers; the preamble's ``## Quality Convention``
    section is exempt because its example ``### Quality`` lives inside a code
    fence (blanked by ``strip_code_fences``).
    """
    failures: list[tuple[str, int, str]] = []
    for p in sorted(KB.rglob("claim-quality.md")):
        if any(part in EXCLUDE_DIRS for part in p.relative_to(KB).parts[:-1]):
            continue
        rel = str(p.relative_to(KB))
        # Scrub fenced code blocks so the preamble's format-example snippet
        # (a fenced `### Quality` / `<!-- id: clm-xxxxxx -->`) is not parsed
        # as a real claim section.
        lines = strip_code_fences(p.read_text()).splitlines()

        # Split into `---`-delimited sections, tracking 1-based start lines.
        # A bare `---` line is a section separator.
        sections: list[tuple[int, list[str]]] = []
        current: list[str] = []
        current_start = 1
        for lineno, line in enumerate(lines, start=1):
            if line.strip() == "---":
                sections.append((current_start, current))
                current = []
                current_start = lineno + 1
            else:
                current.append(line)
        sections.append((current_start, current))

        for sec_start, sec_lines in sections:
            quality_idx = next(
                (i for i, ln in enumerate(sec_lines)
                 if ln.strip() == "### Quality"),
                None,
            )
            if quality_idx is None:
                continue
            has_title = any(ln.startswith("## ") for ln in sec_lines)
            has_id = any(CANONICAL_ANY_ID.match(ln.strip()) for ln in sec_lines)
            if has_title and has_id:
                continue
            missing = []
            if not has_title:
                missing.append("`## <title>` heading")
            if not has_id:
                missing.append("`<!-- id: clm-... -->` marker")
            failures.append(
                (rel, sec_start + quality_idx,
                 "orphan/malformed `### Quality` block — missing "
                 + " and ".join(missing))
            )
    return failures


def check_frontmatter_presence(files: list[tuple[Path, dict | None]]):
    """Return list of (path, kind-guessed) for files without frontmatter."""
    failures = []
    for p, fm in files:
        if fm is None:
            failures.append(str(p.relative_to(KB)))
    return failures


def check_tier1_coverage(files: list[tuple[Path, dict | None]]):
    """Leaf coverage: a leaf must declare its content via at least one of
    ``{claims, no-claim, exp-id}``.

    Hosting an experiment node (``exp-id``) satisfies coverage on its own — a
    leaf that originates only an experiment needs neither ``claims:`` nor
    ``no-claim:`` (INVARIANT-S9). ``claims`` and ``no-claim`` remain mutually
    exclusive *with each other*; ``exp-id`` is orthogonal to both and may
    co-exist with either.
    """
    failures = []
    for p, fm in files:
        if fm is None:
            continue
        kind = fm.get("kind")
        if kind not in ("leaf", "leaf-as-index"):
            continue
        has_claims = "claims" in fm and bool(fm["claims"])
        has_no_claim = "no-claim" in fm and bool(fm["no-claim"])
        has_exp = "exp-id" in fm and bool(fm["exp-id"])
        if not has_claims and not has_no_claim and not has_exp:
            failures.append(
                (str(p.relative_to(KB)), "none of claims / no-claim / exp-id")
            )
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


def check_experiments_ref_integrity(
    files: list[tuple[Path, dict | None]],
    experiment_ids: set[str],
    claim_ids: set[str],
):
    """Every leaf ``experiments:`` ref must resolve to an experiment node.

    A leaf may carry an optional ``experiments: [exp-xxxxxx, ...]`` field that
    REFERENCES experiments it does not own (the analog of ``claims:`` for
    claims). Each referenced id must:

    * be a well-formed ``\\bexp-[a-z0-9]{6}\\b`` id, and
    * resolve to an actual experiment node (an ``exp-id``-declaring leaf).

    Two hard-failure modes are reported per (leaf, id):

    * ``orphan`` — the id matches no experiment node (and is not a known claim
      id either): a dangling reference.
    * ``kind-mismatch`` — the id resolves to a CLAIM (``clm-``) rather than an
      experiment: an id that points at the wrong node class.
    * ``malformed`` — the id is not a syntactically valid exp-id.

    Returns a list of ``(leaf_path, id, reason)`` tuples. Mirrors the style of
    ``check_orphan_refs`` / the index referential-integrity check. NOT
    refresh-fixable — the leaf's ``experiments:`` field must be corrected.
    """
    failures: list[tuple[str, str, str]] = []
    for p, fm in files:
        if fm is None:
            continue
        refs = fm.get("experiments", [])
        if not refs:
            continue
        rel = str(p.relative_to(KB))
        for rid in refs:
            if not EXP_ID_RE.fullmatch(rid):
                if rid in claim_ids or ID_RE.fullmatch(rid):
                    failures.append(
                        (rel, rid, "resolves to a claim, not an experiment")
                    )
                else:
                    failures.append(
                        (rel, rid, "malformed exp-id (expected exp-[a-z0-9]{6})")
                    )
                continue
            if rid not in experiment_ids:
                failures.append(
                    (rel, rid, "no such experiment node (orphan reference)")
                )
    return failures


def check_subtree_experiments_consistency(state) -> list[tuple[str, list, list]]:
    """Declared ``subtree-experiments`` must equal the computed owned union.

    Owned-only, parallel to ``check_subtree_consistency`` for subtree-claims:
    each index / entry-point node's declared ``subtree-experiments`` must equal
    the union of exp-ids OWNED by experiment leaves under it (a leaf's
    ``experiments:`` REFERENCES do NOT contribute). The expected union comes
    from ``kb_index_lib.compute_subtree_aggregates`` — the SAME shared
    computation refresh writes from, so this checker and the emitter cannot
    drift. (refresh-fixable.)

    Returns ``(node_path, missing_from_declared, extra_in_declared)`` tuples.
    """
    aggregates = kb_index_lib.compute_subtree_aggregates(state)
    failures: list[tuple[str, list, list]] = []
    for idx in state.indexes:
        _, expected_exp = aggregates.get(idx.path, ([], []))
        declared = set(idx.declared_subtree_experiments)
        expected = set(expected_exp)
        if declared != expected:
            failures.append(
                (
                    idx.path,
                    sorted(expected - declared),
                    sorted(declared - expected),
                )
            )
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
        text = path.read_text(encoding="utf-8")
        if not text:
            # An empty file is well-formed per write_jsonl semantics, but
            # for the real KB every file is non-empty; if it is empty we
            # treat that as a freshness defect, caught by check_index_fresh.
            continue
        if not text.endswith("\n"):
            eof_defects.append((short, "missing final newline"))
        elif text.endswith("\n\n"):
            eof_defects.append((short, "multiple trailing newlines"))
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
        expected_text = kb_index_lib.serialize_records(expected[short])
        actual_text = path.read_text(encoding="utf-8")
        if actual_text == expected_text:
            continue
        expected_count = len(expected[short])
        actual_count = sum(1 for ln in actual_text.split("\n") if ln)
        drift.append((short, expected_count, actual_count))
    return drift, expected


def check_index_referential_integrity(index_dir: Path):
    """Every id referenced in any non-claims index file resolves in claims.jsonl.

    With framework nodes (Push 2), ``claims.jsonl`` is a type-tagged union of
    ``claim`` / ``invariant`` / ``axiom`` nodes. This check spans all three:

    * ``depends-on`` ``source`` must resolve to a record (it is always a
      claim); ``target`` must resolve to a record AND its ``target_kind``
      must equal the resolved record's ``node_type``.
    * ``strengthen-by`` / ``cites`` ``claim_id`` and ``subtree-aggregates``
      ``subtree_claims`` ids must each resolve to a record. (These reference
      claim ids only, which are a subset of the node id space.)

    Returns a list of (short_name, id, location) tuples for orphan or
    kind-mismatched references. NOT refresh-fixable; indicates a build bug
    (refresh should never emit one).

    Skipped silently if claims.jsonl is missing or malformed — the
    well-formed check surfaces that.
    """
    claims_path = index_dir / "claims.jsonl"
    if not claims_path.exists():
        return []
    try:
        node_type_by_id: dict[str, str] = {}
        for ln in claims_path.read_text(encoding="utf-8").split("\n"):
            if not ln:
                continue
            rec = json.loads(ln)
            node_type_by_id[rec["id"]] = rec.get("node_type", "claim")
    except (json.JSONDecodeError, KeyError):
        return []

    canonical = set(node_type_by_id)
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
        "supported-by",
        [
            ("claim_id", lambda r: [r.get("claim_id")] if r.get("claim_id") else []),
            ("sup_id", lambda r: [r.get("sup_id")] if r.get("sup_id") else []),
        ],
    )
    _check_lines(
        "subtree-aggregates",
        [
            ("subtree_claims", lambda r: list(r.get("subtree_claims") or [])),
            (
                "subtree_experiments",
                lambda r: list(r.get("subtree_experiments") or []),
            ),
        ],
    )

    # Per-edge consistency, relation-aware (depends vs strengthens).
    #
    # * depends:     source resolves to a claim OR a support (a support's own
    #                deps are depends edges sourced at the sup-id); target
    #                resolves to any node; target_kind == resolved target
    #                node_type (kind-match); strength is null; fraction is null.
    # * strengthens: source resolves to an experiment; target resolves to a
    #                claim AND target_kind == "claim"; an experiment node is
    #                never an edge target; strength is non-null; fraction null.
    # * supports:    source resolves to a SUPPORT; target resolves to a claim
    #                AND target_kind == "claim"; strength is null; fraction is
    #                in (0, 1] OR the literal "*pending*" (INVARIANT-S10).
    dep_path = index_dir / "depends-on.jsonl"
    if dep_path.exists():
        for lineno, line in enumerate(
            dep_path.read_text(encoding="utf-8").split("\n"), start=1
        ):
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            source = rec.get("source")
            target = rec.get("target")
            kind = rec.get("target_kind")
            relation = rec.get("relation")
            strength = rec.get("strength")
            fraction = rec.get("fraction")
            src_type = node_type_by_id.get(source)
            tgt_type = node_type_by_id.get(target)

            if relation == "supports":
                if src_type is not None and src_type != "support":
                    violations.append(
                        ("depends-on", source,
                         f"line {lineno}, supports edge source resolves to "
                         f"{src_type!r}, expected support")
                    )
                if tgt_type is not None and tgt_type != "claim":
                    violations.append(
                        ("depends-on", target,
                         f"line {lineno}, supports edge target resolves to "
                         f"{tgt_type!r}, expected claim")
                    )
                if kind != "claim":
                    violations.append(
                        ("depends-on", target,
                         f"line {lineno}, supports edge target_kind {kind!r} "
                         f"!= 'claim'")
                    )
                if strength is not None:
                    violations.append(
                        ("depends-on", source,
                         f"line {lineno}, supports edge has non-null strength "
                         f"{strength!r}")
                    )
                # A pending on-point fraction (literal "*pending*") is a valid
                # authored value (intended-but-unassessed); it is distinct from
                # a depends edge's null fraction. A numeric fraction must be in
                # (0, 1]; null or out-of-range is a violation (INVARIANT-S10).
                if fraction == kb_index_lib.PENDING_LITERAL:
                    pass
                elif (
                    not isinstance(fraction, (int, float))
                    or isinstance(fraction, bool)
                    or not (0.0 < fraction <= 1.0)
                ):
                    violations.append(
                        ("depends-on", source,
                         f"line {lineno}, supports edge on-point fraction "
                         f"{fraction!r} not in (0, 1] or *pending*")
                    )
            elif relation == "strengthens":
                if src_type is not None and src_type != "experiment":
                    violations.append(
                        ("depends-on", source,
                         f"line {lineno}, strengthens edge source resolves to "
                         f"{src_type!r}, expected experiment")
                    )
                if tgt_type is not None and tgt_type != "claim":
                    violations.append(
                        ("depends-on", target,
                         f"line {lineno}, strengthens edge target resolves to "
                         f"{tgt_type!r}, expected claim")
                    )
                if kind != "claim":
                    violations.append(
                        ("depends-on", target,
                         f"line {lineno}, strengthens edge target_kind {kind!r} "
                         f"!= 'claim'")
                    )
                if strength is None:
                    violations.append(
                        ("depends-on", source,
                         f"line {lineno}, strengthens edge has null strength")
                    )
            elif relation == "depends":
                if src_type is not None and src_type not in ("claim", "support"):
                    violations.append(
                        ("depends-on", source,
                         f"line {lineno}, depends edge source resolves to "
                         f"{src_type!r}, expected claim or support")
                    )
                if tgt_type is not None and kind != tgt_type:
                    violations.append(
                        ("depends-on", target,
                         f"line {lineno}, target_kind {kind!r} != "
                         f"node_type {tgt_type!r}")
                    )
                if tgt_type == "experiment":
                    violations.append(
                        ("depends-on", target,
                         f"line {lineno}, depends edge targets an experiment "
                         f"node (experiments are never edge targets)")
                    )
                if strength is not None:
                    violations.append(
                        ("depends-on", source,
                         f"line {lineno}, depends edge has non-null strength "
                         f"{strength!r}")
                    )
            else:
                violations.append(
                    ("depends-on", source or "?",
                     f"line {lineno}, unknown relation {relation!r}")
                )

    # exp-id format + experiment-node placement: every experiment node id must
    # match \bexp-[a-z0-9]{6}\b, and no experiment id may appear in cites /
    # subtree-aggregates (those reference claim ids only). depends-on target
    # placement is covered above.
    for nid, ntype in node_type_by_id.items():
        if ntype == "experiment" and not EXP_ID_RE.fullmatch(nid):
            violations.append(
                ("claims", nid, "experiment node id is not \\bexp-[a-z0-9]{6}\\b")
            )
        if ntype == "support" and not SUP_ID_RE.fullmatch(nid):
            violations.append(
                ("claims", nid, "support node id is not \\bsup-[a-z0-9]{6}\\b")
            )

    experiment_ids = {
        nid for nid, t in node_type_by_id.items() if t == "experiment"
    }
    for short in ("cites", "subtree-aggregates"):
        path = index_dir / f"{short}.jsonl"
        if not path.exists():
            continue
        for lineno, line in enumerate(
            path.read_text(encoding="utf-8").split("\n"), start=1
        ):
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            if short == "cites":
                ids = [rec.get("claim_id")]
            else:
                ids = list(rec.get("subtree_claims") or [])
            for cid in ids:
                if cid in experiment_ids:
                    violations.append(
                        (short, cid,
                         f"line {lineno}, experiment node referenced where a "
                         f"claim id is expected")
                    )
            # subtree-aggregates subtree_experiments holds exp-ids only; each
            # must resolve to an experiment node (a claim id here is a kind
            # mismatch — the inverse of the subtree_claims check above).
            if short == "subtree-aggregates":
                for eid in list(rec.get("subtree_experiments") or []):
                    if eid in node_type_by_id and eid not in experiment_ids:
                        violations.append(
                            (short, eid,
                             f"line {lineno}, subtree_experiments id resolves to "
                             f"{node_type_by_id[eid]!r}, expected experiment")
                        )

    # supported-by kind-match: claim_id must resolve to a claim, sup_id to a
    # support (INVARIANT-S10). The reverse view is untraversed for solidity, but
    # a kind mismatch still signals a build bug.
    sb_path = index_dir / "supported-by.jsonl"
    if sb_path.exists():
        for lineno, line in enumerate(
            sb_path.read_text(encoding="utf-8").split("\n"), start=1
        ):
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            cid = rec.get("claim_id")
            sid = rec.get("sup_id")
            if cid in node_type_by_id and node_type_by_id[cid] != "claim":
                violations.append(
                    ("supported-by", cid,
                     f"line {lineno}, claim_id resolves to "
                     f"{node_type_by_id[cid]!r}, expected claim")
                )
            if sid in node_type_by_id and node_type_by_id[sid] != "support":
                violations.append(
                    ("supported-by", sid,
                     f"line {lineno}, sup_id resolves to "
                     f"{node_type_by_id[sid]!r}, expected support")
                )

    return violations


LEAF_REFERENCES_PREFIX = kb_index_lib.LEAF_REFERENCES_PREFIX


def check_leaf_references_fresh(state) -> list[tuple[str, str, str, str]]:
    """Verify each entry's on-disk leaf-references footer matches the derived one.

    The ``> **Leaf references:**`` footer is a derived field (INVARIANT-S8):
    regenerated by ``make refresh-kb-metadata`` from the reverse-citation map
    (which leaves host the entry's id) and gated here. The reverse map comes
    from the SAME ``kb_index_lib.build_leaf_references`` the refresher writes
    from, so this checker and the emitter cannot drift.

    For every ``clm-`` / ``sup-`` entry in every register, locates the footer
    line in the band between the entry's ``<!-- id: ... -->`` marker and its
    ``### Quality`` heading and compares it byte-for-byte to the regenerated
    footer. Three drift kinds (all refresh-fixable):

    * a present footer whose text disagrees with the regenerated one (the rot
      this gate eliminates — a hand-edited or stale footer);
    * a MISSING footer where the entry should carry one;
    * an entry whose id has no citing leaf at all (the footer regenerates to the
      explicit ``*(none …)*`` marker; bidirectional-coverage flags the deeper
      defect, but the footer drift is still reported).

    Returns ``(register_path, node_id, got, want)`` tuples. ``got`` is the
    on-disk footer (or ``"(missing)"``); ``want`` is the regenerated footer.
    Code fences are scrubbed so a fenced example footer is never parsed.
    """
    leaf_references = kb_index_lib.build_leaf_references(state)
    drift: list[tuple[str, str, str, str]] = []
    for p in sorted(KB.rglob("claim-quality.md")):
        if any(part in EXCLUDE_DIRS for part in p.relative_to(KB).parts[:-1]):
            continue
        register_rel = p.relative_to(KB).as_posix()
        scrubbed = strip_code_fences(p.read_text()).splitlines()

        # Locate every (id_line, node_id, quality_line) entry region.
        id_lines: list[tuple[int, str]] = []
        for i, line in enumerate(scrubbed):
            m = CANONICAL_ANY_ID.match(line.strip())
            if m:
                id_lines.append((i, m.group(1)))
        for id_line, node_id in id_lines:
            qstart: int | None = None
            for j in range(id_line + 1, len(scrubbed)):
                if scrubbed[j].strip() == "### Quality":
                    qstart = j
                    break
                if scrubbed[j].startswith("## "):
                    break
            if qstart is None:
                continue
            want = kb_index_lib.render_leaf_references(
                register_rel, leaf_references.get(node_id, [])
            )
            got: str | None = None
            for idx in range(id_line + 1, qstart):
                if scrubbed[idx].startswith(LEAF_REFERENCES_PREFIX):
                    got = scrubbed[idx]
                    break
            if got is None:
                drift.append((register_rel, node_id, "(missing)", want))
            elif got != want:
                drift.append((register_rel, node_id, got, want))
    return drift


def check_solidity_cycle(state) -> list[str]:
    """Detect a cycle in the claim depends-on graph.

    ``solidity`` is computed bottom-up over the claim depends-on DAG; a cycle
    leaves solidity undefined for its members. Returns the sorted list of
    cycle-member claim ids (empty when the graph is acyclic). Not
    refresh-fixable — the cycle must be broken in the claim declarations.
    """
    try:
        kb_index_lib.compute_solidity(
            state.claim_entries, state.experiments, state.supports
        )
    except kb_index_lib.SolidityCycleError as exc:
        return exc.cycle_members
    return []


def _approx(a: float | None, b: float | None) -> bool:
    """Compare two 2-dp solidity values with a tiny tolerance."""
    if a is None or b is None:
        return a is b
    return abs(a - b) < 1e-9


def check_solidity_fresh(state, index_dir: Path):
    """Verify on-disk solidity matches ``compute_solidity``'s derived output.

    ``solidity``, the build-status phrase, and depends-on ``(solidity X)``
    annotations are derived fields — regenerated by ``make refresh-kb-metadata``.
    This check recomputes them and diffs against what is written on disk.

    Three drift kinds are reported (all refresh-fixable):

    * ``line``  — a claim entry's ``- solidity:`` value or build-status phrase
      disagrees with the computed value.
    * ``annotation`` — a depends-on ``(solidity X)`` annotation disagrees with
      its target claim's computed solidity.
    * ``jsonl`` — a ``claims.jsonl`` record's ``solidity`` field disagrees with
      the computed value.

    Returns ``(line_drift, annotation_drift, jsonl_drift)``. A claim with no
    computable solidity — its confidence is ``*pending*`` OR a dependency is
    ``*pending*`` (pending-ness propagates transitively, like NaN) — must
    carry the ``*pending*`` solidity line on disk; a numeric on-disk value
    for such a claim IS drift (a stale value left behind after a dependency
    went pending). Returns empty lists when the graph has a cycle (the cycle
    check already fails loudly in that case).
    """
    try:
        solidity = kb_index_lib.compute_solidity(
            state.claim_entries, state.experiments, state.supports
        )
        sup_solidity = kb_index_lib.compute_support_solidity(
            state.claim_entries, state.experiments, state.supports
        )
    except kb_index_lib.SolidityCycleError:
        return [], [], []

    by_id = {e.id: e for e in state.claim_entries}

    line_drift: list[tuple[str, str, str]] = []
    annotation_drift: list[tuple[str, str, str, str]] = []

    # Support entries carry the same derived ``- solidity:`` line + claim-target
    # depends-on annotations (INVARIANT-S10); their solidity is sup_solidity.
    for sup in state.supports:
        computed = sup_solidity.get(sup.id)
        if computed is None:
            if sup.solidity is not None:
                line_drift.append(
                    (sup.id, f"solidity {sup.solidity}", "expected *pending*")
                )
        elif not _approx(sup.solidity, computed):
            line_drift.append(
                (sup.id, f"solidity {sup.solidity}", f"expected {computed:.2f}")
            )
        for edge in sup.depends_on:
            if edge.target_kind != "claim":
                continue
            target_solidity = solidity.get(edge.target)
            if target_solidity is None:
                if edge.target_solidity_recorded is not None:
                    annotation_drift.append(
                        (sup.id, edge.target,
                         f"recorded {edge.target_solidity_recorded}",
                         "expected *pending*")
                    )
                continue
            if edge.target_solidity_recorded is None:
                continue
            if not _approx(edge.target_solidity_recorded, target_solidity):
                annotation_drift.append(
                    (sup.id, edge.target,
                     f"recorded {edge.target_solidity_recorded}",
                     f"expected {target_solidity:.2f}")
                )

    for entry in state.claim_entries:
        computed = solidity.get(entry.id)
        if computed is None:
            # No computable solidity (pending confidence OR a pending
            # dependency): the on-disk solidity must be the *pending* form
            # (parsed as None). A numeric on-disk value is stale drift.
            if entry.solidity is not None:
                line_drift.append(
                    (
                        entry.id,
                        f"solidity {entry.solidity}",
                        "expected *pending*",
                    )
                )
            continue
        expected_phrase = kb_index_lib.build_status_phrase(computed)
        if not _approx(entry.solidity, computed):
            line_drift.append(
                (
                    entry.id,
                    f"solidity {entry.solidity}",
                    f"expected {computed:.2f}",
                )
            )
        elif entry.build_status != expected_phrase:
            line_drift.append(
                (
                    entry.id,
                    f"build-status {entry.build_status!r}",
                    f"expected {expected_phrase!r}",
                )
            )
        # Depends-on (solidity X) annotation freshness.
        for edge in entry.depends_on:
            if edge.target_kind != "claim":
                continue
            target_solidity = solidity.get(edge.target)
            if target_solidity is None:
                # Target has no computable solidity (pending confidence OR a
                # pending dependency). Its annotation must be the *pending*
                # form (parsed as None); a stale numeric value is drift.
                if edge.target_solidity_recorded is not None:
                    annotation_drift.append(
                        (
                            entry.id,
                            edge.target,
                            f"recorded {edge.target_solidity_recorded}",
                            "expected *pending*",
                        )
                    )
                continue
            if edge.target_solidity_recorded is None:
                continue  # no annotation present — nothing to verify
            if not _approx(edge.target_solidity_recorded, target_solidity):
                annotation_drift.append(
                    (
                        entry.id,
                        edge.target,
                        f"recorded {edge.target_solidity_recorded}",
                        f"expected {target_solidity:.2f}",
                    )
                )

    # claims.jsonl solidity field freshness.
    jsonl_drift: list[tuple[str, str, str]] = []
    claims_path = index_dir / "claims.jsonl"
    if claims_path.exists():
        try:
            for line in claims_path.read_text(encoding="utf-8").split("\n"):
                if not line:
                    continue
                rec = json.loads(line)
                node_type = rec.get("node_type", "claim")
                if node_type == "support":
                    # A support record's solidity must equal its computed
                    # sup_solidity (null when pending).
                    sid = rec.get("id")
                    computed = sup_solidity.get(sid)
                    if computed is None:
                        if rec.get("solidity") is not None:
                            jsonl_drift.append(
                                (sid, f"solidity {rec.get('solidity')}",
                                 "expected null")
                            )
                    elif not _approx(rec.get("solidity"), computed):
                        jsonl_drift.append(
                            (sid, f"solidity {rec.get('solidity')}",
                             f"expected {computed:.2f}")
                        )
                    continue
                if node_type != "claim":
                    continue
                cid = rec.get("id")
                computed = solidity.get(cid)
                if computed is None:
                    # No computable solidity: the record's solidity must be
                    # null. A numeric value is stale drift.
                    if rec.get("solidity") is not None:
                        jsonl_drift.append(
                            (
                                cid,
                                f"solidity {rec.get('solidity')}",
                                "expected null",
                            )
                        )
                    continue
                if not _approx(rec.get("solidity"), computed):
                    jsonl_drift.append(
                        (
                            cid,
                            f"solidity {rec.get('solidity')}",
                            f"expected {computed:.2f}",
                        )
                    )
        except json.JSONDecodeError:
            pass  # malformed claims.jsonl is surfaced by the well-formed check

    return line_drift, annotation_drift, jsonl_drift


def main(argv: list[str] | None = None) -> int:
    global KB
    parser = argparse.ArgumentParser(
        description="Mechanical KB claim-quality and derived-index verifier."
    )
    parser.add_argument(
        "--kb-root",
        type=Path,
        default=None,
        help=(
            "KB root directory to operate on. Defaults to manuscript/ave-kb/ "
            "(computed relative to the invocation cwd). Used by tests to point "
            "the verifier at a synthetic fixture KB instead of the canonical one."
        ),
    )
    parser.add_argument(
        "--index-dir",
        type=Path,
        default=None,
        help=(
            "Directory containing the .index/*.jsonl files. Defaults to "
            "<kb-root>/.index/. Used by tests to point at a synthetic "
            "index tree without disturbing the canonical one."
        ),
    )
    args = parser.parse_args(argv)
    if args.kb_root is not None:
        KB = args.kb_root
    index_dir = args.index_dir if args.index_dir is not None else (KB / ".index")

    if not KB.is_dir():
        print(f"FAIL: {KB} not found. Run from repository root.", file=sys.stderr)
        return 2

    files = collect_files()
    canonical = collect_canonical_ids()
    canonical_set = {cid for cid, _ in canonical}

    fm_missing = check_frontmatter_presence(files)
    quality_block_failures = check_quality_block_integrity()
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

    # Solidity-graph checks. ``solidity`` is a derived field; these verify the
    # claim depends-on graph is acyclic and the on-disk solidity content
    # matches what ``compute_solidity`` derives.
    kb_state = kb_index_lib.discover_kb(KB, diagnostic_stream=None)
    solidity_cycle = check_solidity_cycle(kb_state)
    sol_line_drift, sol_anno_drift, sol_jsonl_drift = check_solidity_fresh(
        kb_state, index_dir
    )

    # Leaf-references footer freshness. The `> **Leaf references:**` footer is a
    # derived field (INVARIANT-S8); this recomputes it from the reverse-citation
    # map and diffs against on-disk. A hand-edited or stale footer is drift.
    leaf_ref_drift = check_leaf_references_fresh(kb_state)

    # Experiments-reference checks (the optional `experiments:` leaf field):
    # every reference must resolve to an experiment node, and the derived
    # subtree-experiments aggregate must match the owned union.
    experiment_ids = {exp.id for exp in kb_state.experiments}
    claim_ids = {entry.id for entry in kb_state.claim_entries}
    exp_ref_failures = check_experiments_ref_integrity(
        files, experiment_ids, claim_ids
    )
    subtree_exp_failures = check_subtree_experiments_consistency(kb_state)

    # Index summary line — counts come from the canonical (expected) record
    # set so the line is meaningful even when on-disk files are stale.
    # claims.jsonl is a type-tagged union; report the node-type breakdown.
    node_type_counts = Counter(
        rec.get("node_type", "claim") for rec in expected_records["claims"]
    )
    print(
        f"[index] {len(INDEX_FILES)} JSONL files "
        f"({len(expected_records['claims'])} nodes: "
        f"{node_type_counts.get('claim', 0)} claims / "
        f"{node_type_counts.get('experiment', 0)} experiments / "
        f"{node_type_counts.get('support', 0)} support / "
        f"{node_type_counts.get('invariant', 0)} invariants / "
        f"{node_type_counts.get('axiom', 0)} axioms, "
        f"{len(expected_records['depends-on'])} depends-on, "
        f"{len(expected_records['strengthen-by'])} strengthen-by, "
        f"{len(expected_records['supported-by'])} supported-by, "
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

    if quality_block_failures:
        has_failures = True
        print(
            f"\n[FAIL] {len(quality_block_failures)} orphan/malformed "
            f"`### Quality` block(s) in claim-quality registers:"
        )
        for rel, line, reason in quality_block_failures:
            print(f"  {rel}:{line}: {reason}")
        print(
            "  → Each `### Quality` block must sit within a `---`-delimited "
            "section that also carries the claim's `## <title>` heading and "
            "its `<!-- id: clm-... -->` marker. Not refresh-fixable; delete "
            "the orphan block or restore its missing title/id."
        )

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

    if subtree_exp_failures:
        has_failures = True
        refresh_fixable = True
        print(
            f"\n[FAIL] {len(subtree_exp_failures)} indexes with "
            f"subtree-experiments drift:"
        )
        for p, missing, extra in subtree_exp_failures:
            print(f"  {p}")
            if missing:
                print(f"    missing from declared: {missing}")
            if extra:
                print(f"    extra in declared: {extra}")

    if exp_ref_failures:
        has_failures = True
        print(
            f"\n[FAIL] {len(exp_ref_failures)} leaf experiments: reference(s) "
            f"do not resolve to an experiment node:"
        )
        for rel, rid, reason in exp_ref_failures:
            print(f"  {rel}: {rid} — {reason}")
        print(
            "  → Not refresh-fixable. Every id in a leaf's experiments: field "
            "must resolve to an exp-id-declaring experiment leaf. Fix the "
            "reference or add the experiment."
        )

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

    if solidity_cycle:
        has_failures = True
        print(
            f"\n[FAIL] claim depends-on graph has a cycle "
            f"({len(solidity_cycle)} claim(s) involved):"
        )
        for cid in solidity_cycle:
            print(f"  {cid}")
        print(
            "  → solidity is undefined for cycle members. Not refresh-fixable; "
            "break the cycle in the claim depends-on declarations."
        )

    if sol_line_drift or sol_anno_drift or sol_jsonl_drift:
        has_failures = True
        refresh_fixable = True
        total = len(sol_line_drift) + len(sol_anno_drift) + len(sol_jsonl_drift)
        print(
            f"\n[FAIL] {total} solidity freshness defect(s) — derived solidity "
            f"is stale vs canonical confidence + depends-on graph:"
        )
        for cid, got, want in sol_line_drift:
            print(f"  {cid}: solidity line — {got}, {want}")
        for cid, target, got, want in sol_anno_drift:
            print(
                f"  {cid}: depends-on annotation for {target} — {got}, {want}"
            )
        for cid, got, want in sol_jsonl_drift:
            print(f"  {cid}: claims.jsonl — {got}, {want}")
        print("  → Run `make refresh-kb-metadata` to regenerate solidity.")

    if leaf_ref_drift:
        has_failures = True
        refresh_fixable = True
        print(
            f"\n[FAIL] {len(leaf_ref_drift)} leaf-references footer(s) stale vs "
            f"the reverse-citation map (which leaves host the entry's id):"
        )
        for rel, nid, got, want in leaf_ref_drift:
            print(f"  {rel}:{nid}")
            print(f"    - {got.strip()}")
            print(f"    + {want.strip()}")
        print(
            "  → The `> **Leaf references:**` footer is a derived field; do not "
            "hand-edit it. Run `make refresh-kb-metadata` to regenerate."
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

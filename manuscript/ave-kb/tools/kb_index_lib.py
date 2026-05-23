"""Foundation library for the AVE Knowledge Base derived-index pipeline.

Pure-function parsing and record building for the JSONL files documented in
``manuscript/ave-kb/.index/SCHEMA.md``. This module is the canonical parser for
KB frontmatter, claim-quality entries, and leaf metadata; downstream tools
(``refresh-kb-metadata``, ``verify-kb-metadata``) will be unified onto it in
later phases. The library is side-effect-free with respect to KB content; the
only file I/O it performs is reading canonical sources via pathlib and writing
JSONL through ``write_jsonl`` for callers that own a destination path.

Stdlib only. No timestamps, no environment-dependent paths in emitted records.
Same canonical input -> byte-identical output.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass, field
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path
from typing import TextIO

KB_ROOT_DEFAULT = Path("manuscript/ave-kb")

EXCLUDE_DIRS = {"session", ".index", "tools"}
EXCLUDE_NAMES = {"claim-quality.md", "CLAUDE.md", "CONVENTIONS.md", "README.md"}

# Claim-ID pattern: the `clm-` prefix plus 6 lowercase alphanumeric chars.
# The prefix makes the pattern exact — it cannot match incidental prose words.
_CLAIM_ID_RE = re.compile(r"\b(clm-[a-z0-9]{6})\b")
# Either an exp- or clm- id — used to extract id-list frontmatter values that
# may hold either prefix (a `claims:` list holds clm- ids, an `experiments:`
# list holds exp- ids). Longest alternative first is irrelevant here (fixed
# six-char bodies), but the prefix keeps each match exact.
_ANY_ID_RE = re.compile(r"\b((?:clm|exp)-[a-z0-9]{6})\b")
_CANONICAL_ID_RE = re.compile(r"<!--\s*id:\s*(clm-[a-z0-9]{6})\s*-->")
# Experiment-ID pattern (INVARIANT-S9): `exp-` prefix plus 6 lowercase
# alphanumeric chars. Exact, like the claim-id pattern.
_EXP_ID_RE = re.compile(r"\b(exp-[a-z0-9]{6})\b")
# A `strengthens:` block pair line: `clm-<id>: <strength>` (strength a float
# in [0,1]). Indented under the `strengthens:` frontmatter key.
_STRENGTHENS_PAIR_RE = re.compile(
    r"^\s*-?\s*(clm-[a-z0-9]{6})\s*:\s*(-?\d+(?:\.\d+)?)\s*$"
)
_FRONTMATTER_RE = re.compile(r"<!--\s*kb-frontmatter\s*\n(.*?)\n-->", re.DOTALL)
_TIER2_INLINE_RE = re.compile(r"<!--\s*claim-quality:\s*(.*?)\s*-->", re.DOTALL)
_CODE_FENCE_RE = re.compile(r"^```")

# Framework-node parsing (from manuscript/ave-kb/CLAUDE.md).
# Invariant headings: `### INVARIANT-XX: <title>`.
_INVARIANT_HEADING_RE = re.compile(r"^### (INVARIANT-[A-Z]+[0-9]+):\s*(.+)$")
# Axiom bullets in the INVARIANT-S2 section: `- Axiom N: **<title>** — ...`.
_AXIOM_BULLET_RE = re.compile(r"^- Axiom ([1-4]): \*\*(.+?)\*\*")
# In-bullet target tokens for depends-on head extraction.
_INVARIANT_TOKEN_RE = re.compile(r"\b(INVARIANT-[A-Z]+[0-9]+)\b")
_AXIOM_TOKEN_RE = re.compile(r"\bAxiom ([1-4])\b")

# Quality-field parsing.
# `confidence: 0.X` and `solidity: 0.X (build-status phrase) [optional arithmetic]`
_NUMBER_RE = re.compile(r"-?\d+(?:\.\d+)?")
# Captures a parenthetical group that does not start with `=` (which marks the
# arithmetic annotation). Build-status is the first parenthetical after the
# numeric value.
_FIRST_PAREN_RE = re.compile(r"\(([^()]*)\)")
# A depends-on entry line: `- <id> — ... (solidity <num>) [optional context]`.
# The placeholder is detected separately and produces no edge.
_DEPENDS_ON_PLACEHOLDER_RE = re.compile(r"^\s*-\s*\*\(")
_DEPENDS_ON_BRACKET_RE = re.compile(r"\[([^\[\]]*)\]\s*$")
_DEPENDS_ON_PAREN_RE = re.compile(r"\(([^()]*)\)")
_SOLIDITY_IN_PAREN_RE = re.compile(r"solidity\s+(-?\d+(?:\.\d+)?)")


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class DependsOnEdge:
    """A forward edge in the claim graph — a ``depends`` or ``strengthens`` edge.

    ``relation`` discriminates the edge class:

    * ``"depends"`` (gating, min-branch): ``source`` is a claim; ``target`` is
      a claim / invariant / axiom. ``strength`` is ``None``.
    * ``"strengthens"`` (max-branch): ``source`` is an experiment; ``target``
      is a claim; ``strength`` is the conferred experimental solidity in
      ``[0, 1]``; ``target_kind`` is ``"claim"`` and ``target_solidity_recorded``
      is ``None``.

    ``target_kind`` discriminates the target node type: ``"claim"`` for an
    edge to another claim, ``"invariant"`` / ``"axiom"`` for an edge to a
    framework node. For framework targets ``target_solidity_recorded`` is
    always ``None`` (framework nodes carry no scoring fields).
    """

    source: str
    target: str
    relation: str  # "depends" | "strengthens"
    target_kind: str
    target_solidity_recorded: float | None
    strength: float | None
    context: str | None


@dataclass(frozen=True)
class ExperimentNode:
    """A physical experiment — a first-class, terminal graph node (INVARIANT-S9).

    Experiments are strength-sources: they have NO ``depends`` edges and never
    gate; they only emit ``strengthens`` edges to the claims their result bears
    on. ``status`` is ``"run"`` (its strengthens edges count toward
    experimental solidity) or ``"pending"`` (unrun — its edges contribute
    nothing). ``strengthens`` is the tuple of ``(claim_id, strength)`` pairs
    parsed from the leaf's ``strengthens:`` frontmatter block.
    """

    id: str
    title: str
    canonical_path: str
    canonical_anchor: str
    status: str  # "run" | "pending"
    strengthens: tuple[tuple[str, float], ...]


@dataclass(frozen=True)
class FrameworkNode:
    """A structural invariant or AVE axiom — a first-class graph node.

    Framework nodes are parsed from ``manuscript/ave-kb/CLAUDE.md``. They are
    solidity-1.0 by definition (framework bedrock) — a documented rule, not a
    stored field. The record carries only the five identifying fields.
    """

    node_type: str  # "invariant" | "axiom"
    id: str
    title: str
    canonical_path: str
    canonical_anchor: str


@dataclass(frozen=True)
class StrengthenByItem:
    """A single strengthen-by bullet from a claim's Quality section."""

    claim_id: str
    item_idx: int
    text: str
    mentioned_ids: tuple[str, ...]


@dataclass(frozen=True)
class ClaimEntry:
    """A canonical claim-quality entry, parsed from a claim-quality.md file."""

    id: str
    title: str
    canonical_path: str
    canonical_anchor: str
    confidence: float | None
    solidity: float | None
    build_status: str | None
    rationale: str
    depends_on: tuple[DependsOnEdge, ...]
    strengthen_by: tuple[StrengthenByItem, ...]


@dataclass(frozen=True)
class LeafRecord:
    """A leaf or leaf-as-index file's parsed metadata.

    ``experiments_ref`` holds the exp-ids a leaf REFERENCES via its optional
    ``experiments:`` frontmatter field (the exact analog of ``claims:`` for
    claims — a leaf-level citation, the inverse of an experiment's
    Leaf-references). It is additive: a referencing leaf still declares
    ``claims:`` or ``no-claim:`` as its primary field. References do NOT roll
    up into ``subtree-experiments`` (that aggregate is owned-only — see
    :func:`build_subtree_aggregate_records`).
    """

    path: str
    kind: str
    claims: tuple[str, ...]
    tier2_marked: frozenset[str]
    no_claim_reason: str | None
    experiments_ref: tuple[str, ...] = ()


@dataclass(frozen=True)
class IndexRecord:
    """An index or entry-point file's parsed metadata.

    ``declared_subtree_experiments`` is the derived ``subtree-experiments:``
    field — the union of exp-ids OWNED (declared via ``exp-id:``) by
    experiment leaves under this node's directory. Owned-only, parallel to
    how ``declared_subtree_claims`` aggregates owned leaf claims.
    """

    path: str
    kind: str
    declared_subtree_claims: tuple[str, ...]
    declared_subtree_experiments: tuple[str, ...] = ()


@dataclass(frozen=True)
class KbState:
    """The full discovered state of the KB after a one-shot load."""

    claim_entries: tuple[ClaimEntry, ...]
    leaves: tuple[LeafRecord, ...]
    indexes: tuple[IndexRecord, ...]
    framework_nodes: tuple[FrameworkNode, ...]
    experiments: tuple[ExperimentNode, ...]


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------


def parse_frontmatter(text: str) -> dict | None:
    """Return parsed kb-frontmatter fields, or None if no block found.

    Same semantics as the existing parsers in refresh-kb-metadata.py and
    verify-kb-metadata.py: ID-lists return as ``list[str]``, quoted strings
    are unquoted, booleans become Python bool, everything else stays a string.
    """
    m = _FRONTMATTER_RE.search(text)
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
            # Id-list values hold clm- ids (e.g. claims:, subtree-claims:) or
            # exp- ids (experiments:, subtree-experiments:); accept both.
            fields[key] = _ANY_ID_RE.findall(value)
        elif value.startswith('"') and value.endswith('"'):
            fields[key] = value[1:-1]
        elif value in ("true", "false"):
            fields[key] = value == "true"
        else:
            fields[key] = value
    return fields


# ---------------------------------------------------------------------------
# Framework-node parsing (CLAUDE.md)
# ---------------------------------------------------------------------------


def parse_framework_nodes(kb_root: Path = KB_ROOT_DEFAULT) -> list[FrameworkNode]:
    """Parse invariant and axiom nodes from ``manuscript/ave-kb/CLAUDE.md``.

    Invariants come from ``### INVARIANT-XX: <title>`` headings; each node's
    ``canonical_anchor`` is the GitHub-style slug of its own heading.

    Axioms come from the ``- Axiom N: **<title>** — ...`` bullets in the
    INVARIANT-S2 section; all four point at the INVARIANT-S2 heading's slug
    (the KB's axiom-numbering authority). Node ids are ``axiom-1``..``axiom-4``.

    Returns an empty list if ``CLAUDE.md`` is absent. ``canonical_path`` is
    ``"CLAUDE.md"`` for every framework node.
    """
    claude_md = kb_root / "CLAUDE.md"
    if not claude_md.is_file():
        return []
    lines = claude_md.read_text().splitlines()

    nodes: list[FrameworkNode] = []
    s2_anchor: str | None = None
    for line in lines:
        m = _INVARIANT_HEADING_RE.match(line)
        if m:
            label, title = m.group(1), m.group(2).strip()
            anchor = _slugify_heading(line[4:].strip())
            nodes.append(
                FrameworkNode(
                    node_type="invariant",
                    id=label,
                    title=title,
                    canonical_path="CLAUDE.md",
                    canonical_anchor=anchor,
                )
            )
            if label == "INVARIANT-S2":
                s2_anchor = anchor

    for line in lines:
        m = _AXIOM_BULLET_RE.match(line)
        if m:
            num, title = m.group(1), m.group(2).strip()
            nodes.append(
                FrameworkNode(
                    node_type="axiom",
                    id=f"axiom-{num}",
                    title=title,
                    canonical_path="CLAUDE.md",
                    canonical_anchor=s2_anchor or "",
                )
            )
    return nodes


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _strip_code_fences(text: str) -> str:
    """Blank out lines inside ``` fenced code blocks.

    Used to scrub claim-quality.md content before regex extraction so the
    example snippet in the Quality Convention preamble does not contribute
    false ID matches.
    """
    out = []
    in_fence = False
    for line in text.splitlines():
        if _CODE_FENCE_RE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else line)
    return "\n".join(out)


def _slugify_heading(text: str) -> str:
    """GitHub-style heading anchor.

    Lowercase, replace whitespace with '-', drop characters outside
    [a-z0-9-_]. Mirrors GitHub's behavior closely enough for KB anchors;
    AVE headings are short and rarely collide.
    """
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"\s+", "-", s)
    return s.strip("-")


def _posix_relative(path: Path, kb_root: Path) -> str:
    """Return POSIX-style path relative to kb_root."""
    return path.relative_to(kb_root).as_posix()


def _kb_files(kb_root: Path):
    """Iterate non-excluded .md files under kb_root."""
    for p in sorted(kb_root.rglob("*.md")):
        if any(part in EXCLUDE_DIRS for part in p.relative_to(kb_root).parts[:-1]):
            continue
        if p.name in EXCLUDE_NAMES:
            continue
        yield p


def _parse_solidity_line(line: str) -> tuple[float | None, str | None]:
    """Parse `- solidity: 0.X (build-status phrase) [optional arithmetic]`.

    Returns (solidity, build_status). The first parenthetical is the
    build-status phrase; trailing `[...]` arithmetic annotations are ignored.
    """
    value = line.split(":", 1)[1].strip() if ":" in line else line.strip()
    num_match = _NUMBER_RE.search(value)
    solidity = float(num_match.group(0)) if num_match else None
    paren = _FIRST_PAREN_RE.search(value)
    status = paren.group(1).strip() if paren else None
    return solidity, status


def _parse_confidence_line(line: str) -> float | None:
    """Parse `- confidence: 0.X`."""
    value = line.split(":", 1)[1].strip() if ":" in line else ""
    num_match = _NUMBER_RE.search(value)
    return float(num_match.group(0)) if num_match else None


def _normalize_text(s: str) -> str:
    """Collapse internal whitespace runs and line breaks to single spaces."""
    return re.sub(r"\s+", " ", s).strip()


def _depends_on_bullet_head(stripped: str) -> str:
    """Extract the head of a depends-on bullet.

    The head is the bullet text (already stripped of the leading ``- ``)
    truncated at the EARLIER of the first ` — ` (em-dash title separator) or
    the first ` (` (paren). The dependency target token(s) live in the head;
    the title/context after the separator is not scanned for targets.
    """
    cut = len(stripped)
    dash = stripped.find(" — ")
    if dash != -1:
        cut = min(cut, dash)
    paren = stripped.find(" (")
    if paren != -1:
        cut = min(cut, paren)
    return stripped[:cut]


def _parse_depends_on_line(
    line: str,
    source_id: str,
    known_ids: set[str] | None = None,
    diagnostic_stream: TextIO | None = None,
    canonical_path: str | None = None,
) -> list[DependsOnEdge]:
    """Parse a depends-on bullet into zero or more edges (head-extraction).

    A bullet's dependency target(s) live in its *head* — the text before the
    first ` — ` or ` (`. The head is scanned for every recognized target
    token; one edge is emitted per token:

    * ``clm-xxxxxx`` -> a ``claim`` edge; ``target_solidity_recorded`` parsed
      from a ``(solidity <num>)`` group; ``context`` from a trailing ``[...]``.
    * ``INVARIANT-XX`` -> an ``invariant`` edge; ``target_solidity_recorded``
      is ``None``; ``context`` from the bullet's first ``(...)`` paren content.
    * ``Axiom N`` -> an ``axiom`` edge with ``target`` normalized to
      ``axiom-N``; ``target_solidity_recorded`` is ``None``; ``context`` from
      the first ``(...)`` paren content.

    Placeholder bullets (``- *(none entry-local — ...)*``) and bullets whose
    head contains no recognized token produce zero edges.

    When ``known_ids`` is provided, a ``clm-``-shaped target outside that set
    is dropped (with a diagnostic on ``diagnostic_stream`` if non-None) —
    catching a typo or stale reference. ``known_ids`` does not gate framework
    targets; their resolution is checked by the verifier's referential
    integrity check.
    """
    if _DEPENDS_ON_PLACEHOLDER_RE.match(line):
        return []
    stripped = re.sub(r"^\s*-\s*", "", line).strip()
    head = _depends_on_bullet_head(stripped)

    # Context shared by framework edges: the first `(...)` paren content.
    paren_match = _DEPENDS_ON_PAREN_RE.search(stripped)
    paren_context = paren_match.group(1).strip() if paren_match else None

    # Context for claim edges: a trailing `[...]` group (skip `[= ...]`
    # arithmetic annotations).
    bracket_match = _DEPENDS_ON_BRACKET_RE.search(stripped)
    bracket_context: str | None = None
    if bracket_match:
        raw = bracket_match.group(1).strip()
        if not raw.startswith("="):
            bracket_context = raw

    sol_match = _SOLIDITY_IN_PAREN_RE.search(stripped)
    target_sol = float(sol_match.group(1)) if sol_match else None

    edges: list[DependsOnEdge] = []
    for cid in _CLAIM_ID_RE.findall(head):
        if known_ids is not None and cid not in known_ids:
            if diagnostic_stream is not None:
                location = (
                    f"{canonical_path}:{source_id}" if canonical_path else source_id
                )
                diagnostic_stream.write(
                    f"[kb_index_lib] dropped non-claim depends-on target in "
                    f'{location}: "{cid}" (bullet: "{_normalize_text(stripped)}")\n'
                )
            continue
        edges.append(
            DependsOnEdge(
                source=source_id,
                target=cid,
                relation="depends",
                target_kind="claim",
                target_solidity_recorded=target_sol,
                strength=None,
                context=bracket_context,
            )
        )
    for label in _INVARIANT_TOKEN_RE.findall(head):
        edges.append(
            DependsOnEdge(
                source=source_id,
                target=label,
                relation="depends",
                target_kind="invariant",
                target_solidity_recorded=None,
                strength=None,
                context=paren_context,
            )
        )
    for num in _AXIOM_TOKEN_RE.findall(head):
        edges.append(
            DependsOnEdge(
                source=source_id,
                target=f"axiom-{num}",
                relation="depends",
                target_kind="axiom",
                target_solidity_recorded=None,
                strength=None,
                context=paren_context,
            )
        )
    return edges


def _parse_strengthen_by_lines(
    lines: list[str],
    source_id: str,
    known_ids: set[str] | None = None,
    diagnostic_stream: TextIO | None = None,
) -> tuple[StrengthenByItem, ...]:
    """Each top-level `- ` bullet becomes one item; continuation lines fold in.

    When ``known_ids`` is provided, mentioned IDs are filtered against that
    set; dropped candidates produce a diagnostic line on ``diagnostic_stream``
    if non-None.
    """
    items: list[tuple[list[str]]] = []
    current: list[str] | None = None
    for line in lines:
        # Top-level bullet detection: exactly two leading spaces is the typical
        # convention for the strengthen-by sub-bullets (under `- strengthen-by:`).
        # We accept any indentation depth that begins with `-` after at least
        # two leading spaces, treating deeper indents as continuations.
        m = re.match(r"^(\s+)-\s+(.*)$", line)
        if m and len(m.group(1)) <= 4:
            if current is not None:
                items.append((current,))
            current = [m.group(2)]
        else:
            if current is not None:
                current.append(line.strip())
    if current is not None:
        items.append((current,))

    out: list[StrengthenByItem] = []
    for idx, (chunks,) in enumerate(items):
        text = _normalize_text(" ".join(chunks))
        if not text:
            continue
        # Reject placeholders mirrored from depends-on: "*(none entry-local — ...)*"
        # is itself a strengthen-by item in some entries (legitimately - it
        # documents "no entry-local work would help"), so we keep it; but
        # mentioned_ids will simply be empty for it.
        candidates = sorted(set(_CLAIM_ID_RE.findall(text)))
        if known_ids is None:
            mentioned = candidates
        else:
            mentioned = []
            for cand in candidates:
                if cand in known_ids:
                    mentioned.append(cand)
                elif diagnostic_stream is not None:
                    diagnostic_stream.write(
                        f"[kb_index_lib] dropped non-claim mention in "
                        f'strengthen-by for {source_id} item #{idx}: "{cand}"\n'
                    )
        out.append(
            StrengthenByItem(
                claim_id=source_id,
                item_idx=idx,
                text=text,
                mentioned_ids=tuple(mentioned),
            )
        )
    return tuple(out)


# ---------------------------------------------------------------------------
# Claim-quality file parsing
# ---------------------------------------------------------------------------


def parse_claim_quality_file(
    path: Path,
    kb_root: Path,
    known_ids: set[str] | None = None,
    diagnostic_stream: TextIO | None = None,
) -> list[ClaimEntry]:
    """Parse every canonical entry in a single claim-quality.md file.

    For each `<!-- id: xxxxxx -->` marker, locates the preceding `##` heading
    and the following `### Quality` section. Confidence / solidity /
    build_status / rationale / depends-on / strengthen-by are extracted from
    the Quality section.

    When ``known_ids`` is provided, depends-on edges with a target outside
    that set are dropped, and strengthen-by ``mentioned_ids`` are filtered to
    members of that set. Post-`clm-`-migration the ID regex is exact, so this
    filter only catches a `clm-`-shaped token that isn't a registered ID (a
    typo or stale reference) — incidental English words are never matched.
    Drops emit one diagnostic line each on ``diagnostic_stream`` (default
    ``None`` = silent). When ``known_ids`` is ``None``, no filtering occurs
    and the function preserves the pre-filter behavior.
    """
    raw = path.read_text()
    scrubbed = _strip_code_fences(raw)
    lines = scrubbed.splitlines()
    canonical_rel = _posix_relative(path, kb_root)

    # Locate every (id_line_idx, claim_id, heading_line_idx, heading_text).
    entries_meta: list[tuple[int, str, int, str]] = []
    last_heading_idx: int | None = None
    last_heading_text: str | None = None
    for i, line in enumerate(lines):
        if line.startswith("## "):
            last_heading_idx = i
            last_heading_text = line[3:].strip()
            continue
        m = _CANONICAL_ID_RE.match(line.strip())
        if m and last_heading_idx is not None and last_heading_text is not None:
            entries_meta.append((i, m.group(1), last_heading_idx, last_heading_text))

    # For each entry, find its Quality section: the next `### Quality` heading
    # after the id-marker line (the Quality heading is an H3 nested under the
    # claim's `## <Title>` H2). Section ends at the next `## ` heading or EOF.
    quality_starts: list[int | None] = []
    quality_ends: list[int | None] = []
    for idx, (id_line, _claim_id, _hd_idx, _hd_text) in enumerate(entries_meta):
        qstart: int | None = None
        for j in range(id_line + 1, len(lines)):
            if lines[j].strip() == "### Quality":
                qstart = j
                break
            # Stop searching if we hit the next entry's `## ` title heading;
            # the Quality block is typically very close to the id-marker line.
            # An H3 `### Quality` heading does not start with `## `, so it is
            # never mistaken for a sibling-entry title.
            if lines[j].startswith("## "):
                break
        qend: int | None = None
        if qstart is not None:
            for j in range(qstart + 1, len(lines)):
                if lines[j].startswith("## "):
                    qend = j
                    break
            if qend is None:
                qend = len(lines)
        quality_starts.append(qstart)
        quality_ends.append(qend)

    out: list[ClaimEntry] = []
    for (id_line, claim_id, _hd_idx, hd_text), qstart, qend in zip(
        entries_meta, quality_starts, quality_ends
    ):
        confidence: float | None = None
        solidity: float | None = None
        build_status: str | None = None
        rationale = ""
        depends_on: list[DependsOnEdge] = []
        strengthen_items: tuple[StrengthenByItem, ...] = ()

        if qstart is not None and qend is not None:
            qlines = lines[qstart + 1 : qend]
            i = 0
            while i < len(qlines):
                ln = qlines[i]
                stripped = ln.strip()
                if stripped.startswith("- confidence:"):
                    confidence = _parse_confidence_line(stripped)
                    i += 1
                elif stripped.startswith("- solidity:"):
                    solidity, build_status = _parse_solidity_line(stripped)
                    i += 1
                elif stripped.startswith("- rationale:"):
                    rationale_chunks = [stripped.split(":", 1)[1].strip()]
                    i += 1
                    # Fold continuation lines until the next top-level `- key:`
                    # or list-bullet for depends-on/strengthen-by.
                    while i < len(qlines):
                        nxt = qlines[i]
                        nxt_strip = nxt.strip()
                        if re.match(r"^- (confidence|solidity|rationale|depends-on|strengthen-by):", nxt_strip):
                            break
                        if not nxt_strip:
                            break
                        rationale_chunks.append(nxt_strip)
                        i += 1
                    rationale = _normalize_text(" ".join(rationale_chunks))
                elif stripped.startswith("- depends-on:"):
                    i += 1
                    dep_lines: list[str] = []
                    while i < len(qlines):
                        nxt = qlines[i]
                        nxt_strip = nxt.strip()
                        if re.match(r"^- (confidence|solidity|rationale|strengthen-by):", nxt_strip):
                            break
                        # A sub-bullet starts with `- ` and at least one leading space.
                        if re.match(r"^\s+-\s+", nxt):
                            dep_lines.append(nxt)
                        elif not nxt_strip:
                            pass
                        else:
                            # Continuation of the previous sub-bullet; tack on.
                            if dep_lines:
                                dep_lines[-1] = dep_lines[-1] + " " + nxt_strip
                        i += 1
                    for dep_line in dep_lines:
                        depends_on.extend(
                            _parse_depends_on_line(
                                dep_line,
                                claim_id,
                                known_ids=known_ids,
                                diagnostic_stream=diagnostic_stream,
                                canonical_path=canonical_rel,
                            )
                        )
                elif stripped.startswith("- strengthen-by:"):
                    i += 1
                    sb_lines: list[str] = []
                    while i < len(qlines):
                        nxt = qlines[i]
                        nxt_strip = nxt.strip()
                        if re.match(r"^- (confidence|solidity|rationale|depends-on):", nxt_strip):
                            break
                        # The Quality section is bounded by the next `## `
                        # heading, so qlines includes the entry-separating
                        # `---` rule. strengthen-by is the last field, so its
                        # loop must stop there or it swallows `---` into the
                        # final bullet's text.
                        if nxt_strip == "---":
                            break
                        sb_lines.append(nxt)
                        i += 1
                    strengthen_items = _parse_strengthen_by_lines(
                        sb_lines,
                        claim_id,
                        known_ids=known_ids,
                        diagnostic_stream=diagnostic_stream,
                    )
                else:
                    i += 1

        out.append(
            ClaimEntry(
                id=claim_id,
                title=hd_text,
                canonical_path=canonical_rel,
                canonical_anchor=_slugify_heading(hd_text),
                confidence=confidence,
                solidity=solidity,
                build_status=build_status,
                rationale=rationale,
                depends_on=tuple(depends_on),
                strengthen_by=strengthen_items,
            )
        )
    return out


# ---------------------------------------------------------------------------
# Leaf / index discovery
# ---------------------------------------------------------------------------


def parse_leaf(path: Path, kb_root: Path) -> LeafRecord | None:
    """Parse a leaf or leaf-as-index file's frontmatter and Tier 2 markers.

    Returns None if the file has no frontmatter or its kind is not
    ``leaf``/``leaf-as-index``.
    """
    text = path.read_text()
    fm = parse_frontmatter(text)
    if not fm:
        return None
    kind = fm.get("kind", "")
    if kind not in ("leaf", "leaf-as-index"):
        return None
    claims = tuple(fm.get("claims", []) or ())
    no_claim_value = fm.get("no-claim")
    no_claim_reason = (
        no_claim_value if isinstance(no_claim_value, str) and no_claim_value else None
    )
    # Optional `experiments:` references — exp-ids this leaf cites but does
    # NOT own. Additive to claims:/no-claim:; never a primary field.
    experiments_ref = tuple(
        i for i in (fm.get("experiments", []) or ()) if i.startswith("exp-")
    )
    # Tier 2 markers: scan body (minus the frontmatter block) for
    # `<!-- claim-quality: <id> ... -->` markers and intersect with claims.
    scrubbed = _FRONTMATTER_RE.sub("", text)
    marker_bodies = _TIER2_INLINE_RE.findall(scrubbed)
    marked: set[str] = set()
    for body in marker_bodies:
        for cid in _CLAIM_ID_RE.findall(body):
            if cid in claims:
                marked.add(cid)
    return LeafRecord(
        path=_posix_relative(path, kb_root),
        kind=kind,
        claims=claims,
        tier2_marked=frozenset(marked),
        no_claim_reason=no_claim_reason,
        experiments_ref=experiments_ref,
    )


class ExperimentLeafError(ValueError):
    """Raised when an ``kind: experiment`` leaf is malformed.

    The leaf either carries a claim-bearing field (``claims:`` / ``no-claim:``,
    mutually exclusive with ``exp-id:`` per INVARIANT-S9) or an ``exp-id`` that
    does not match the ``\\bexp-[a-z0-9]{6}\\b`` format.
    """


def _experiment_heading(text: str) -> str:
    """Return the first Markdown heading text at any level (``#`` … ``######``), or ''.

    The experiment node's ``title``/``canonical_anchor`` come from the leaf's
    title heading. KB leaves use ``##`` for their title heading (a few use
    ``#``); match any level so the title is captured regardless.
    """
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            return m.group(2).strip()
    return ""


def parse_experiment_leaf(path: Path, kb_root: Path) -> ExperimentNode | None:
    """Parse a ``kind: experiment`` leaf into an ExperimentNode (INVARIANT-S9).

    Returns ``None`` if the file has no frontmatter or its kind is not
    ``experiment``. The frontmatter carries ``exp-id``, ``status``, and a
    ``strengthens:`` block of ``clm-<id>: <strength>`` pairs (one per line,
    indented under the ``strengthens:`` key). ``strengthens`` pairs are
    returned in source order.

    Raises :class:`ExperimentLeafError` when the leaf violates INVARIANT-S9:
    it carries ``claims:`` / ``no-claim:`` (mutually exclusive with ``exp-id``),
    it carries an ``experiments:`` reference field (an owning experiment leaf
    must not also reference other experiments), or its ``exp-id`` is malformed.
    """
    text = path.read_text()
    m = _FRONTMATTER_RE.search(text)
    if not m:
        return None
    body = m.group(1)
    lines = body.splitlines()

    # Quick top-level scan: kind, exp-id, status, and detection of the
    # claim-bearing fields. ``strengthens:`` opens an indented sub-block.
    kind = ""
    exp_id: str | None = None
    status: str | None = None
    has_claims = False
    has_experiments_ref = False
    in_strengthens = False
    pairs: list[tuple[str, float]] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        # A `strengthens:` pair sub-line (e.g. `  - clm-xxxxxx: 1.0` or
        # `  clm-xxxxxx: 1.0`) — only collected while inside the block.
        pair = _STRENGTHENS_PAIR_RE.match(line)
        if in_strengthens and pair:
            pairs.append((pair.group(1), float(pair.group(2))))
            continue
        # A new top-level key ends the strengthens block.
        if ":" in stripped:
            key = stripped.split(":", 1)[0].strip().lstrip("- ").strip()
            value = stripped.split(":", 1)[1].strip()
            if key == "strengthens":
                in_strengthens = True
                continue
            in_strengthens = False
            if key == "kind":
                kind = value
            elif key == "exp-id":
                exp_id = value
            elif key == "status":
                status = value
            elif key in ("claims", "no-claim"):
                if value:
                    has_claims = True
            elif key == "experiments":
                if value:
                    has_experiments_ref = True

    if kind != "experiment":
        return None

    rel = _posix_relative(path, kb_root)
    if has_claims:
        raise ExperimentLeafError(
            f"{rel}: kind: experiment leaf carries claims:/no-claim: — "
            f"mutually exclusive with exp-id (INVARIANT-S9)."
        )
    if has_experiments_ref:
        raise ExperimentLeafError(
            f"{rel}: kind: experiment leaf carries experiments: — an owning "
            f"experiment leaf must not also reference other experiments."
        )
    if exp_id is None or not _EXP_ID_RE.fullmatch(exp_id):
        raise ExperimentLeafError(
            f"{rel}: kind: experiment leaf has missing or malformed exp-id "
            f"{exp_id!r} (expected \\bexp-[a-z0-9]{{6}}\\b)."
        )
    if status not in ("run", "pending"):
        raise ExperimentLeafError(
            f"{rel}: kind: experiment leaf has invalid status {status!r} "
            f"(expected 'run' or 'pending')."
        )

    return ExperimentNode(
        id=exp_id,
        title=_experiment_heading(text),
        canonical_path=rel,
        canonical_anchor=_slugify_heading(_experiment_heading(text)),
        status=status,
        strengthens=tuple(pairs),
    )


def _parse_index(path: Path, kb_root: Path) -> IndexRecord | None:
    """Parse an ``index`` or ``entry-point`` kind file."""
    text = path.read_text()
    fm = parse_frontmatter(text)
    if not fm:
        return None
    kind = fm.get("kind", "")
    if kind not in ("index", "entry-point"):
        return None
    declared = tuple(fm.get("subtree-claims", []) or ())
    declared_exp = tuple(
        i for i in (fm.get("subtree-experiments", []) or ()) if i.startswith("exp-")
    )
    return IndexRecord(
        path=_posix_relative(path, kb_root),
        kind=kind,
        declared_subtree_claims=declared,
        declared_subtree_experiments=declared_exp,
    )


def collect_known_claim_ids(kb_root: Path = KB_ROOT_DEFAULT) -> set[str]:
    """First-pass scan of every ``claim-quality.md`` for canonical IDs.

    Returns the set of IDs marked by ``<!-- id: clm-xxxxxx -->`` in any
    non-excluded ``claim-quality.md`` register, after stripping fenced code
    blocks (so example placeholders inside ```` ``` ```` blocks do not count).
    """
    known: set[str] = set()
    for cq in sorted(kb_root.rglob("claim-quality.md")):
        if any(part in EXCLUDE_DIRS for part in cq.relative_to(kb_root).parts[:-1]):
            continue
        scrubbed = _strip_code_fences(cq.read_text())
        for line in scrubbed.splitlines():
            m = _CANONICAL_ID_RE.match(line.strip())
            if m:
                known.add(m.group(1))
    return known


def discover_kb(
    kb_root: Path = KB_ROOT_DEFAULT,
    diagnostic_stream: TextIO | None = sys.stderr,
) -> KbState:
    """One-shot load of the KB. Reads every non-excluded .md file under
    kb_root plus every claim-quality.md register and ``CLAUDE.md`` (for the
    framework nodes — invariants and axioms).

    Two passes over claim-quality registers: the first collects the canonical
    set of claim IDs; the second parses entries with that set in hand so a
    `clm-`-shaped token that isn't a registered ID (a typo or stale reference)
    is rejected as a depends-on target or strengthen-by mention. Diagnostics
    for rejected candidates are written to ``diagnostic_stream`` (default
    ``sys.stderr``; pass ``None`` to silence).
    """
    known_ids = collect_known_claim_ids(kb_root)

    claim_entries: list[ClaimEntry] = []
    for cq in sorted(kb_root.rglob("claim-quality.md")):
        # Exclude session-tree claim-quality files if any.
        if any(part in EXCLUDE_DIRS for part in cq.relative_to(kb_root).parts[:-1]):
            continue
        claim_entries.extend(
            parse_claim_quality_file(
                cq,
                kb_root,
                known_ids=known_ids,
                diagnostic_stream=diagnostic_stream,
            )
        )

    leaves: list[LeafRecord] = []
    indexes: list[IndexRecord] = []
    experiments: list[ExperimentNode] = []
    for p in _kb_files(kb_root):
        leaf = parse_leaf(p, kb_root)
        if leaf is not None:
            leaves.append(leaf)
            continue
        exp = parse_experiment_leaf(p, kb_root)
        if exp is not None:
            experiments.append(exp)
            continue
        idx = _parse_index(p, kb_root)
        if idx is not None:
            indexes.append(idx)

    framework_nodes = parse_framework_nodes(kb_root)

    return KbState(
        claim_entries=tuple(claim_entries),
        leaves=tuple(leaves),
        indexes=tuple(indexes),
        framework_nodes=tuple(framework_nodes),
        experiments=tuple(experiments),
    )


# ---------------------------------------------------------------------------
# Build-band derivation
# ---------------------------------------------------------------------------


def derive_build_band(solidity: float | None) -> str:
    """Map solidity in [0, 1] to a stable build_band enum per SCHEMA.md."""
    if solidity is None:
        return "unknown"
    if solidity >= 0.85:
        return "ok-to-build"
    if solidity >= 0.65:
        return "ok-with-caveats"
    if solidity >= 0.45:
        return "input-only"
    if solidity >= 0.20:
        return "do-not-build"
    return "refuted"


# ---------------------------------------------------------------------------
# Solidity computation (derived field)
# ---------------------------------------------------------------------------
#
# ``solidity`` is a *derived* quality field: it is computed mechanically from
# the hand-authored ``confidence`` values and the claim depends-on graph, not
# hand-maintained. The build-status phrase and the depends-on ``(solidity X)``
# annotations are likewise derived. ``refresh-kb-metadata`` owns writing all
# three back; ``verify-kb-metadata`` verifies the on-disk values match.

# Build-status phrase bands (mapped from solidity), mirroring the
# "Build-status legend" table in the root claim-quality.md preamble. The
# phrases here are the parenthetical text WITHOUT the surrounding parens.
_BUILD_STATUS_BANDS: tuple[tuple[float, str], ...] = (
    (0.85, "ok to build on"),
    (0.65, "ok to build on, see caveats"),
    (0.45, "use as input only, don't build deeper"),
    (0.20, "do not build on, rework needed"),
    (0.00, "refuted, do not use"),
)


def build_status_phrase(solidity: float | None) -> str | None:
    """Map a solidity value to its build-status phrase.

    Returns the band phrase (without surrounding parens) for a numeric
    solidity, or ``None`` when ``solidity`` is ``None`` (an entry whose
    confidence is unset — its solidity is undefined and not written).
    The bands mirror the legend table in the root ``claim-quality.md``.
    """
    if solidity is None:
        return None
    for threshold, phrase in _BUILD_STATUS_BANDS:
        if solidity >= threshold:
            return phrase
    # solidity < 0.0 is out of the documented [0, 1] domain; treat as refuted.
    return _BUILD_STATUS_BANDS[-1][1]


def round_half_up_2dp(value: float) -> float:
    """Round ``value`` to 2 decimal places using round-half-up.

    The KB convention rounds solidity at the 0.005 boundary AWAY from zero
    (round-half-up), NOT with Python's built-in banker's rounding. Using
    ``Decimal`` keeps the boundary deterministic and matches what a human
    auditing the arithmetic by hand would write.
    """
    return float(
        Decimal(str(value)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    )


class SolidityCycleError(ValueError):
    """Raised when the claim depends-on graph contains a cycle.

    Solidity is undefined for the members of a dependency cycle (the
    bottom-up recurrence has no base case). The offending claim ids are
    available on ``cycle_members``.
    """

    def __init__(self, cycle_members: list[str]) -> None:
        self.cycle_members = cycle_members
        joined = ", ".join(cycle_members)
        super().__init__(
            f"claim depends-on graph has a cycle among {len(cycle_members)} "
            f"claim(s): {joined}"
        )


@dataclass(frozen=True)
class SolidityResult:
    """The three derived solidity branches for one claim (SCHEMA definitive rule).

    * ``derivation`` — min-branch: ``round2(confidence × min(dep final
      solidities))``; ``None`` (pending) if confidence is pending or any claim
      dependency's *final* solidity is pending. Framework deps contribute 1.0.
    * ``experimental`` — max-branch: ``max`` of ``strength`` over every
      ``run``-experiment ``strengthens`` edge into this claim; ``None`` if no
      run experiment strengthens it.
    * ``final`` — ``max`` over the non-None of ``{derivation, experimental}``;
      ``None`` (pending) iff BOTH are None.
    """

    derivation: float | None
    experimental: float | None
    final: float | None


def compute_solidity_full(
    claim_entries, experiments=()
) -> dict[str, SolidityResult]:
    """Compute derivation / experimental / final solidity for every claim.

    THE definitive solidity rule (SCHEMA "Solidity branches"). One result per
    claim with a numeric ``confidence`` OR a run-experiment strengthens edge
    (a claim with neither is fully pending and is omitted — treat absence as
    ``*pending*``, i.e. ``SolidityResult(None, None, None)``).

    Algorithm:

    * **experimental_solidity[C]** = ``max`` of ``edge.strength`` over all
      ``relation:"strengthens"`` edges with ``target == C`` whose source
      experiment has ``status == "run"``. ``None`` if no such edge. Unrun
      experiments contribute NOTHING (excluded from the max — no NaN, no 0.0
      floor). Computed upfront, independent of topo order.
    * **derivation_solidity[C]** (Kahn topo over claim→claim ``depends`` edges):
      each claim-dep contributes the dep's *final* solidity (``final[dep]``),
      each framework dep contributes ``1.0``. If C's confidence is ``None`` →
      ``None``. Else if any claim-dep's final is ``None`` (pending) → ``None``.
      Else if C has deps → ``round2(confidence × min(dep finals))``; else →
      ``confidence``.
    * **final[C]** = ``max`` over the non-None of ``{derivation, experimental}``;
      ``None`` iff both are None.

    A claim with pending derivation but a run experiment is RESCUED (final =
    experimental) and its final propagates to its dependents' min — so the
    rescue benefits downstream claims. Strengthening is NON-transitive: a
    ``strengthens`` edge lifts only its directly-targeted claim, never that
    claim's upstream inputs.

    Raises :class:`SolidityCycleError` if the claim→claim ``depends`` subgraph
    has a cycle. Experiments are terminal (no deps) and introduce no cycles.
    """
    entries = {e.id: e for e in claim_entries}

    # --- experimental_solidity[C]: max strength over run-experiment edges ---
    run_status = {exp.id: exp.status for exp in experiments}
    experimental: dict[str, float] = {}
    for exp in experiments:
        if exp.status != "run":
            continue
        for claim_id, strength in exp.strengthens:
            prev = experimental.get(claim_id)
            if prev is None or strength > prev:
                experimental[claim_id] = strength
    # Defensive: any strengthens edge whose source is unknown / not "run" is
    # already excluded above (only "run" experiments iterated). run_status is
    # retained for the verifier-shared semantics; reference it to satisfy
    # linters without changing behavior.
    del run_status

    # --- topo order over the claim→claim depends subgraph ---
    # The graph and Kahn machinery mirror the original derivation-only path:
    # only claims with numeric confidence participate as nodes; a depends edge
    # to a non-numeric-confidence claim blocks the source's derivation.
    numeric = {eid for eid, e in entries.items() if e.confidence is not None}
    indegree: dict[str, int] = {eid: 0 for eid in numeric}
    dependents: dict[str, list[str]] = {eid: [] for eid in numeric}
    for eid in numeric:
        for edge in entries[eid].depends_on:
            if edge.relation != "depends" or edge.target_kind != "claim":
                continue
            if edge.target in numeric:
                indegree[eid] += 1
                dependents[edge.target].append(eid)
            # A depends edge to a non-numeric claim does NOT block the source
            # here: derivation may still be pending, but the source can be
            # rescued experimentally. The per-claim derivation pass below
            # decides pending-ness by checking each claim-dep's final.

    queue = sorted(eid for eid in numeric if indegree[eid] == 0)
    order: list[str] = []
    while queue:
        node = queue.pop(0)
        order.append(node)
        for dep in sorted(dependents[node]):
            indegree[dep] -= 1
            if indegree[dep] == 0:
                queue.append(dep)
                queue.sort()

    if len(order) != len(numeric):
        cycle_members = sorted(eid for eid in numeric if indegree[eid] > 0)
        raise SolidityCycleError(cycle_members)

    # Claims with no numeric confidence have a pending derivation (no
    # confidence to multiply). Seed their final UPFRONT from experimental
    # rescue so a numeric claim that depends on a rescued pending-confidence
    # claim sees the rescued final in its min during the topo pass below.
    # (Their derivation never depends on topo order — it is always pending.)
    results: dict[str, SolidityResult] = {}
    final: dict[str, float | None] = {}
    for eid, entry in entries.items():
        if entry.confidence is not None:
            continue
        exp_sol = experimental.get(eid)
        results[eid] = SolidityResult(None, exp_sol, exp_sol)
        final[eid] = exp_sol

    def _final_of(claim_id: str) -> float | None:
        return final.get(claim_id)

    # Process numeric-confidence claims in topo order so each dep's final is
    # known before the depender.
    for eid in order:
        entry = entries[eid]
        # derivation: confidence × min(claim-dep finals), framework deps = 1.0.
        dep_finals: list[float] = []
        derivation: float | None
        pending = False
        for edge in entry.depends_on:
            if edge.relation != "depends":
                continue
            if edge.target_kind == "claim":
                dep_final = _final_of(edge.target)
                if dep_final is None:
                    pending = True
                    break
                dep_finals.append(dep_final)
            else:
                dep_finals.append(1.0)
        if pending:
            derivation = None
        elif dep_finals:
            derivation = round_half_up_2dp(entry.confidence * min(dep_finals))
        else:
            derivation = entry.confidence
        exp_sol = experimental.get(eid)
        fin = _max_nonnull(derivation, exp_sol)
        final[eid] = fin
        results[eid] = SolidityResult(derivation, exp_sol, fin)

    return results


def _max_nonnull(a: float | None, b: float | None) -> float | None:
    """Return the max of the non-None values; None iff both are None."""
    if a is None:
        return b
    if b is None:
        return a
    return max(a, b)


def compute_solidity(claim_entries, experiments=()) -> dict[str, float]:
    """Compute the derived FINAL ``solidity`` for every scorable claim.

    Backward-compatible thin wrapper over :func:`compute_solidity_full`:
    returns ``{claim_id: final_solidity}`` for every claim whose final solidity
    is non-pending (numeric). A claim with a pending final (``*pending*``) is
    OMITTED from the mapping — every consumer treats "absent" identically to
    "pending". With zero experiments, ``final == derivation`` for every claim,
    so this returns exactly the historical min-branch result.

    ``solidity = round_half_up_2dp(confidence × min(dependency solidities))``,
    computed bottom-up over the claim depends-on DAG (Kahn topological sort):

    * A claim's dependencies are its ``depends-on`` edges. A ``claim``-target
      edge contributes that dependency's already-computed (and already-rounded)
      solidity; an ``invariant`` / ``axiom`` edge contributes ``1.0``
      (framework bedrock — solidity-1.0 by definition).
    * A claim with no depends-on edges has ``solidity = confidence``.
    * Propagation uses each dependency's *rounded* solidity, so a human
      auditing ``0.85 × min(0.41, 0.28)`` against the written values gets the
      same answer the tool does.

    HARD RULE — ``*pending*`` propagates transitively, exactly like NaN
    through arithmetic. A claim's solidity is ``*pending*`` (undefined) if its
    ``confidence`` is ``*pending*`` (parsed as ``None`` — not yet quality
    assessed) OR any of its dependencies' solidity is ``*pending*``,
    REGARDLESS of the claim's own local ``confidence``. A claim with
    ``confidence: 1.0`` that depends on one pending claim still has a pending
    solidity. Framework-node dependencies (invariant / axiom targets) are
    never pending — they are solidity-1.0 bedrock by definition, so a claim
    that depends only on framework nodes is NOT pending (its solidity equals
    its confidence).

    A claim with a pending solidity is OMITTED from the returned mapping: the
    dict contains an entry only for claims with a fully-computable numeric
    solidity. Every consumer must treat "absent from this result" identically
    to "pending" — render/record it as ``*pending*`` / ``null``. The current
    KB is a closed subgraph (no numeric-confidence claim depends on a pending
    claim), so the blocked-by-pending-dependency path is dormant; it activates
    the first time a volume is assessed while a volume it depends on is still
    pending.

    Returns ``{claim_id: solidity}`` for every claim with a computable
    solidity. Raises :class:`SolidityCycleError` if the claim depends-on
    subgraph contains a cycle (Kahn's algorithm detects this for free).
    """
    full = compute_solidity_full(claim_entries, experiments)
    return {cid: r.final for cid, r in full.items() if r.final is not None}


def min_dependency_solidity(
    entry: ClaimEntry, solidity: dict[str, float]
) -> float | None:
    """Return the minimum dependency solidity feeding ``entry``.

    A ``claim``-target edge contributes the dependency's computed solidity
    (from ``solidity``); an ``invariant`` / ``axiom`` edge contributes ``1.0``.
    Returns ``None`` when ``entry`` has no depends-on edges (``solidity``
    trivially equals ``confidence`` — no arithmetic trace) or when any claim
    dependency is itself uncomputable (so the minimum is undefined).

    This is the value ``refresh-kb-metadata`` writes into the
    ``[= <confidence> × <min-dep-solidity>]`` trace on the solidity line.
    """
    dep_solidities: list[float] = []
    for edge in entry.depends_on:
        if edge.relation != "depends":
            continue
        if edge.target_kind == "claim":
            if edge.target not in solidity:
                return None
            dep_solidities.append(solidity[edge.target])
        else:
            dep_solidities.append(1.0)
    if not dep_solidities:
        return None
    return min(dep_solidities)


# ---------------------------------------------------------------------------
# Record builders
# ---------------------------------------------------------------------------


def build_claims_records(state: KbState) -> list[dict]:
    """One record per graph node, sorted by ``(node_type, id)``.

    ``claims.jsonl`` holds a type-tagged union of FOUR node types,
    discriminated by ``node_type``:

    * ``claim`` records carry the full 15-field shape (``node_type`` first,
      then the 14 claim fields, including ``derivation_solidity`` and
      ``experimental_solidity`` before ``solidity``).
    * ``experiment`` records are minimal — six fields (``node_type``, ``id``,
      ``title``, ``canonical_path``, ``canonical_anchor``, ``status``).
    * ``invariant`` / ``axiom`` records are minimal — exactly the five
      identifying fields. Framework nodes are solidity-1.0 by definition, so
      they carry no scoring fields.

    The sort key ``(node_type, id)`` groups axioms, then claims, then
    experiments, then invariants (ASCII order of the discriminator).

    Claim counts (depends_on_count, strengthen_by_count, citation_count) are
    derived from the same state so they're internally consistent with the
    other record files this module emits. ``depends_on_count`` counts only
    ``relation:"depends"`` edges.

    ``derivation_solidity`` / ``experimental_solidity`` / ``solidity`` /
    ``build_status`` / ``build_band`` are **derived** — computed by
    :func:`compute_solidity_full` from the hand-authored ``confidence`` values,
    the depends-on DAG, and run-experiment strengthens edges, NOT re-parsed
    from the claim-quality.md ``solidity`` line. ``build_status`` / ``build_band``
    derive from the FINAL solidity. A claim whose final solidity is pending
    carries ``null`` for ``solidity`` / ``build_status``.
    """
    # Citation counts derived from leaves once.
    cite_counts: dict[str, int] = {}
    for leaf in state.leaves:
        for cid in leaf.claims:
            cite_counts[cid] = cite_counts.get(cid, 0) + 1

    # Solidity is the single derived computation — shared with the
    # claim-quality.md write-back; never computed twice.
    full = compute_solidity_full(state.claim_entries, state.experiments)

    out: list[dict] = []
    for entry in state.claim_entries:
        result = full.get(entry.id)
        derivation = result.derivation if result else None
        experimental = result.experimental if result else None
        final = result.final if result else None
        depends_count = sum(
            1 for e in entry.depends_on if e.relation == "depends"
        )
        out.append(
            {
                "node_type": "claim",
                "id": entry.id,
                "title": entry.title,
                "canonical_path": entry.canonical_path,
                "canonical_anchor": entry.canonical_anchor,
                "confidence": entry.confidence,
                "derivation_solidity": derivation,
                "experimental_solidity": experimental,
                "solidity": final,
                "build_status": build_status_phrase(final),
                "build_band": derive_build_band(final),
                "rationale": entry.rationale,
                "depends_on_count": depends_count,
                "strengthen_by_count": len(entry.strengthen_by),
                "citation_count": cite_counts.get(entry.id, 0),
            }
        )
    for exp in state.experiments:
        out.append(
            {
                "node_type": "experiment",
                "id": exp.id,
                "title": exp.title,
                "canonical_path": exp.canonical_path,
                "canonical_anchor": exp.canonical_anchor,
                "status": exp.status,
            }
        )
    for node in state.framework_nodes:
        out.append(
            {
                "node_type": node.node_type,
                "id": node.id,
                "title": node.title,
                "canonical_path": node.canonical_path,
                "canonical_anchor": node.canonical_anchor,
            }
        )
    out.sort(key=lambda r: (r["node_type"], r["id"]))
    return out


def build_depends_on_records(state: KbState) -> list[dict]:
    """One record per forward graph edge — ``depends`` and ``strengthens``.

    Field order per SCHEMA: ``source``, ``target``, ``relation``,
    ``target_kind``, ``target_solidity_recorded``, ``strength``, ``context``.

    ``depends`` edges come from claim Quality sections (every pre-existing edge
    is ``relation:"depends"``, ``strength:null``). ``strengthens`` edges come
    from each experiment leaf's ``strengthens:`` block — one edge per pair
    (``source: exp-id``, ``target: clm-id``, ``relation:"strengthens"``,
    ``target_kind:"claim"``, ``target_solidity_recorded:null``,
    ``strength:<value>``, ``context:null``).

    Sorted by ``(source, target, context)`` — a null context sorts as the
    empty string — so two edges from the same source to the same target with
    different context notes stay deterministically ordered.
    """
    edges: list[dict] = []
    for entry in state.claim_entries:
        for edge in entry.depends_on:
            edges.append(
                {
                    "source": edge.source,
                    "target": edge.target,
                    "relation": edge.relation,
                    "target_kind": edge.target_kind,
                    "target_solidity_recorded": edge.target_solidity_recorded,
                    "strength": edge.strength,
                    "context": edge.context,
                }
            )
    for exp in state.experiments:
        for claim_id, strength in exp.strengthens:
            edges.append(
                {
                    "source": exp.id,
                    "target": claim_id,
                    "relation": "strengthens",
                    "target_kind": "claim",
                    "target_solidity_recorded": None,
                    "strength": strength,
                    "context": None,
                }
            )
    edges.sort(key=lambda r: (r["source"], r["target"], r["context"] or ""))
    return edges


def build_strengthen_by_records(state: KbState) -> list[dict]:
    """One record per strengthen-by item, sorted by (claim_id, item_idx).

    item_idx is 0-indexed within each claim. Records are emitted in the
    original bullet order so item_idx is contiguous within each claim.
    """
    items: list[dict] = []
    for entry in state.claim_entries:
        for sb in entry.strengthen_by:
            items.append(
                {
                    "claim_id": sb.claim_id,
                    "item_idx": sb.item_idx,
                    "text": sb.text,
                    "mentioned_ids": list(sb.mentioned_ids),
                }
            )
    items.sort(key=lambda r: (r["claim_id"], r["item_idx"]))
    return items


def build_cites_records(state: KbState) -> list[dict]:
    """One record per (claim, leaf) edge, sorted by (claim_id, leaf_path)."""
    rows: list[dict] = []
    for leaf in state.leaves:
        for cid in leaf.claims:
            rows.append(
                {
                    "claim_id": cid,
                    "leaf_path": leaf.path,
                    "leaf_kind": leaf.kind,
                    "tier2_marked": cid in leaf.tier2_marked,
                }
            )
    rows.sort(key=lambda r: (r["claim_id"], r["leaf_path"]))
    return rows


def _is_under(leaf_path: Path, idx_dir: Path) -> bool:
    """True if ``leaf_path`` lies within ``idx_dir`` (the index's directory)."""
    try:
        leaf_path.relative_to(idx_dir)
        return True
    except ValueError:
        return False


def compute_subtree_aggregates(
    state: KbState,
) -> dict[str, tuple[list[str], list[str]]]:
    """THE single computation of every index/entry-point subtree aggregate.

    Returns ``{node_path: (subtree_claims, subtree_experiments)}`` with both
    lists sorted. This is the one place either aggregate is derived; refresh
    (emitter) and verify (checker) both consume this same function from the
    same :class:`KbState`, so the two cannot drift (the dual-compute trap).

    * ``subtree_claims`` — union of OWNED leaf ``claims`` under the node's
      directory (a leaf's foreign depends-on references do not roll up).
    * ``subtree_experiments`` — union of exp-ids OWNED (declared via
      ``exp-id:``) by experiment leaves under the node's directory. OWNED-ONLY:
      a leaf's ``experiments:`` REFERENCES never propagate here, exactly as a
      leaf's foreign claim references never enter ``subtree_claims``.

    A ``kind: entry-point`` node aggregates the whole KB; a ``kind: index``
    node aggregates everything under its own directory.
    """
    leaf_claims = [(Path(leaf.path), leaf.claims) for leaf in state.leaves]
    exp_paths = [(Path(exp.canonical_path), exp.id) for exp in state.experiments]

    out: dict[str, tuple[list[str], list[str]]] = {}
    for idx in state.indexes:
        idx_dir = Path(idx.path).parent
        is_ep = idx.kind == "entry-point"
        claims: set[str] = set()
        experiments: set[str] = set()
        for leaf_path, ids in leaf_claims:
            if is_ep or _is_under(leaf_path, idx_dir):
                claims.update(ids)
        for exp_path, exp_id in exp_paths:
            if is_ep or _is_under(exp_path, idx_dir):
                experiments.add(exp_id)
        out[idx.path] = (sorted(claims), sorted(experiments))
    return out


def build_subtree_aggregate_records(state: KbState) -> list[dict]:
    """One record per index/entry-point node, sorted by node_path.

    Both ``subtree_claims`` and ``subtree_experiments`` come from the single
    shared :func:`compute_subtree_aggregates` so the materialized JSONL cannot
    diverge from what the frontmatter refresh and the verify check derive.
    ``subtree_experiments`` is owned-only (see that function).
    """
    aggregates = compute_subtree_aggregates(state)
    rows: list[dict] = []
    for idx in state.indexes:
        subtree_claims, subtree_experiments = aggregates[idx.path]
        rows.append(
            {
                "node_path": idx.path,
                "node_kind": idx.kind,
                "subtree_claims": subtree_claims,
                "subtree_experiments": subtree_experiments,
            }
        )
    rows.sort(key=lambda r: r["node_path"])
    return rows


def build_all_records(state: KbState) -> dict[str, list[dict]]:
    """Return every JSONL file's records keyed by short file name."""
    return {
        "claims": build_claims_records(state),
        "depends-on": build_depends_on_records(state),
        "strengthen-by": build_strengthen_by_records(state),
        "cites": build_cites_records(state),
        "subtree-aggregates": build_subtree_aggregate_records(state),
    }


# ---------------------------------------------------------------------------
# JSONL I/O
# ---------------------------------------------------------------------------


def serialize_records(records: list[dict]) -> bytes:
    """Serialize records to canonical JSONL bytes.

    Each line is ``json.dumps(rec, ensure_ascii=False, separators=(', ', ': '))``.
    Keys appear in the dict's insertion order (Python 3.7+), so callers must
    construct records with keys in the documented order. The result has one
    trailing ``\\n`` for non-empty inputs and is empty bytes for ``[]``.
    """
    lines = [
        json.dumps(rec, ensure_ascii=False, separators=(", ", ": "))
        for rec in records
    ]
    body = "\n".join(lines)
    if body:
        body += "\n"
    return body.encode("utf-8")


def write_jsonl(path: Path, records: list[dict]) -> None:
    """Write records as JSONL, one object per line, single trailing newline.

    Thin wrapper around :func:`serialize_records` that writes the canonical
    bytes to ``path``.
    """
    path.write_bytes(serialize_records(records))


def read_jsonl(path: Path) -> list[dict]:
    """Parse JSONL file. Blank lines skipped; malformed lines raise ValueError."""
    out: list[dict] = []
    text = path.read_text(encoding="utf-8")
    for lineno, line in enumerate(text.splitlines(), start=1):
        if not line.strip():
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"{path}:{lineno}: malformed JSON: {exc.msg}"
            ) from exc
    return out


__all__ = [
    "KB_ROOT_DEFAULT",
    "EXCLUDE_DIRS",
    "EXCLUDE_NAMES",
    "ClaimEntry",
    "DependsOnEdge",
    "FrameworkNode",
    "ExperimentNode",
    "ExperimentLeafError",
    "StrengthenByItem",
    "LeafRecord",
    "IndexRecord",
    "KbState",
    "SolidityResult",
    "parse_frontmatter",
    "parse_framework_nodes",
    "parse_leaf",
    "parse_experiment_leaf",
    "parse_claim_quality_file",
    "collect_known_claim_ids",
    "discover_kb",
    "derive_build_band",
    "build_status_phrase",
    "round_half_up_2dp",
    "compute_solidity",
    "compute_solidity_full",
    "min_dependency_solidity",
    "SolidityCycleError",
    "build_claims_records",
    "build_depends_on_records",
    "build_strengthen_by_records",
    "build_cites_records",
    "compute_subtree_aggregates",
    "build_subtree_aggregate_records",
    "build_all_records",
    "serialize_records",
    "write_jsonl",
    "read_jsonl",
]

"""Foundation library for the AVE Knowledge Base derived-index pipeline.

Pure-function parsing and record building for the JSONL files documented in
``manuscript/ave-kb/.index/SCHEMA.md``. This module is the canonical parser for
KB frontmatter, claim-quality entries, and leaf metadata; downstream tools
(``refresh-kb-metadata``, ``check-claim-quality``) will be unified onto it in
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

EXCLUDE_DIRS = {"session", ".index"}
EXCLUDE_NAMES = {"claim-quality.md", "CLAUDE.md", "CONVENTIONS.md", "README.md"}

# Claim-ID pattern: the `clm-` prefix plus 6 lowercase alphanumeric chars.
# The prefix makes the pattern exact — it cannot match incidental prose words.
_CLAIM_ID_RE = re.compile(r"\b(clm-[a-z0-9]{6})\b")
_CANONICAL_ID_RE = re.compile(r"<!--\s*id:\s*(clm-[a-z0-9]{6})\s*-->")
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
    """A forward dependency edge from a claim to another graph node.

    ``target_kind`` discriminates the target node type: ``"claim"`` for an
    edge to another claim, ``"invariant"`` / ``"axiom"`` for an edge to a
    framework node. For framework targets ``target_solidity_recorded`` is
    always ``None`` (framework nodes carry no scoring fields).
    """

    source: str
    target: str
    target_kind: str
    target_solidity_recorded: float | None
    context: str | None


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
    """A leaf or leaf-as-index file's parsed metadata."""

    path: str
    kind: str
    claims: tuple[str, ...]
    tier2_marked: frozenset[str]
    no_claim_reason: str | None


@dataclass(frozen=True)
class IndexRecord:
    """An index or entry-point file's parsed metadata."""

    path: str
    kind: str
    declared_subtree_claims: tuple[str, ...]


@dataclass(frozen=True)
class KbState:
    """The full discovered state of the KB after a one-shot load."""

    claim_entries: tuple[ClaimEntry, ...]
    leaves: tuple[LeafRecord, ...]
    indexes: tuple[IndexRecord, ...]
    framework_nodes: tuple[FrameworkNode, ...]


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------


def parse_frontmatter(text: str) -> dict | None:
    """Return parsed kb-frontmatter fields, or None if no block found.

    Same semantics as the existing parsers in refresh-kb-metadata.py and
    check-claim-quality.py: ID-lists return as ``list[str]``, quoted strings
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
            fields[key] = _CLAIM_ID_RE.findall(value)
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
                target_kind="claim",
                target_solidity_recorded=target_sol,
                context=bracket_context,
            )
        )
    for label in _INVARIANT_TOKEN_RE.findall(head):
        edges.append(
            DependsOnEdge(
                source=source_id,
                target=label,
                target_kind="invariant",
                target_solidity_recorded=None,
                context=paren_context,
            )
        )
    for num in _AXIOM_TOKEN_RE.findall(head):
        edges.append(
            DependsOnEdge(
                source=source_id,
                target=f"axiom-{num}",
                target_kind="axiom",
                target_solidity_recorded=None,
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
    and the following `## Quality` section. Confidence / solidity /
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

    # For each entry, find its Quality section: the next `## Quality` heading
    # after the id-marker line. Section ends at the next `## ` heading or EOF.
    quality_starts: list[int | None] = []
    quality_ends: list[int | None] = []
    for idx, (id_line, _claim_id, _hd_idx, _hd_text) in enumerate(entries_meta):
        qstart: int | None = None
        for j in range(id_line + 1, len(lines)):
            if lines[j].strip() == "## Quality":
                qstart = j
                break
            # Stop searching if we hit the next entry's id-marker or the next
            # non-Quality `## ` heading that owns a different entry; the
            # Quality block is typically very close to the id-marker line.
            if lines[j].startswith("## ") and lines[j].strip() != "## Quality":
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
    return IndexRecord(
        path=_posix_relative(path, kb_root),
        kind=kind,
        declared_subtree_claims=declared,
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
    for p in _kb_files(kb_root):
        leaf = parse_leaf(p, kb_root)
        if leaf is not None:
            leaves.append(leaf)
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
# three back; ``check-claim-quality`` verifies the on-disk values match.

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


def compute_solidity(claim_entries) -> dict[str, float]:
    """Compute the derived ``solidity`` for every numeric-confidence claim.

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
    entries = {e.id: e for e in claim_entries}

    # Restrict the computation to claims whose confidence is set; a claim with
    # None confidence cannot be scored and is excluded from the graph.
    computable = {eid for eid, e in entries.items() if e.confidence is not None}

    # Claim-target dependency edges, restricted to edges whose target is itself
    # a computable claim. (Framework targets and pending/unknown claim targets
    # do not become graph edges — framework deps contribute a constant 1.0;
    # a pending/unknown claim target makes the depender uncomputable, handled
    # below.)
    indegree: dict[str, int] = {eid: 0 for eid in computable}
    dependents: dict[str, list[str]] = {eid: [] for eid in computable}
    # A computable claim is "blocked" if it depends on a non-computable claim
    # (pending confidence or an unknown id) — its solidity cannot be derived.
    blocked: set[str] = set()
    for eid in computable:
        for edge in entries[eid].depends_on:
            if edge.target_kind != "claim":
                continue
            if edge.target in computable:
                indegree[eid] += 1
                dependents[edge.target].append(eid)
            else:
                blocked.add(eid)

    # Kahn's algorithm over the computable subgraph.
    queue = sorted(eid for eid in computable if indegree[eid] == 0)
    order: list[str] = []
    while queue:
        node = queue.pop(0)
        order.append(node)
        for dep in sorted(dependents[node]):
            indegree[dep] -= 1
            if indegree[dep] == 0:
                queue.append(dep)
                queue.sort()

    if len(order) != len(computable):
        # Nodes never reaching indegree 0 are exactly the cycle members
        # (plus claims downstream of a cycle). Report the still-blocked set.
        cycle_members = sorted(eid for eid in computable if indegree[eid] > 0)
        raise SolidityCycleError(cycle_members)

    solidity: dict[str, float] = {}
    for eid in order:
        if eid in blocked:
            # Depends on a non-computable claim — solidity is undefined.
            continue
        entry = entries[eid]
        claim_dep_solidities: list[float] = []
        ok = True
        for edge in entry.depends_on:
            if edge.target_kind == "claim":
                if edge.target not in solidity:
                    # Dependency itself uncomputable (blocked upstream).
                    ok = False
                    break
                claim_dep_solidities.append(solidity[edge.target])
            else:
                # Framework dependency (invariant / axiom): solidity 1.0.
                claim_dep_solidities.append(1.0)
        if not ok:
            continue
        confidence = entry.confidence
        assert confidence is not None  # computable ⇒ confidence is set
        if claim_dep_solidities:
            raw = confidence * min(claim_dep_solidities)
        else:
            raw = confidence
        solidity[eid] = round_half_up_2dp(raw)
    return solidity


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

    ``claims.jsonl`` holds a type-tagged union of three node types,
    discriminated by ``node_type``:

    * ``claim`` records carry the full 13-field shape (``node_type`` first,
      then the 12 pre-existing claim fields).
    * ``invariant`` / ``axiom`` records are minimal — exactly the five
      identifying fields (``node_type``, ``id``, ``title``,
      ``canonical_path``, ``canonical_anchor``). Framework nodes are
      solidity-1.0 by definition, so they carry no scoring fields.

    The sort key ``(node_type, id)`` groups axioms, then claims, then
    invariants (ASCII order of the discriminator).

    Claim counts (depends_on_count, strengthen_by_count, citation_count) are
    derived from the same state so they're internally consistent with the
    other record files this module emits.

    ``solidity`` / ``build_status`` / ``build_band`` are **derived** — computed
    by :func:`compute_solidity` from the hand-authored ``confidence`` values
    and the depends-on DAG, NOT re-parsed from the claim-quality.md ``solidity``
    line. A claim whose confidence is unset (so solidity is uncomputable)
    carries ``null`` for all three fields.
    """
    # Citation counts derived from leaves once.
    cite_counts: dict[str, int] = {}
    for leaf in state.leaves:
        for cid in leaf.claims:
            cite_counts[cid] = cite_counts.get(cid, 0) + 1

    # Solidity is the single derived computation — shared with the
    # claim-quality.md write-back; never computed twice.
    solidity = compute_solidity(state.claim_entries)

    out: list[dict] = []
    for entry in state.claim_entries:
        computed_solidity = solidity.get(entry.id)
        out.append(
            {
                "node_type": "claim",
                "id": entry.id,
                "title": entry.title,
                "canonical_path": entry.canonical_path,
                "canonical_anchor": entry.canonical_anchor,
                "confidence": entry.confidence,
                "solidity": computed_solidity,
                "build_status": build_status_phrase(computed_solidity),
                "build_band": derive_build_band(computed_solidity),
                "rationale": entry.rationale,
                "depends_on_count": len(entry.depends_on),
                "strengthen_by_count": len(entry.strengthen_by),
                "citation_count": cite_counts.get(entry.id, 0),
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
    """One record per forward dependency edge.

    ``target_kind`` (``claim`` | ``invariant`` | ``axiom``) is placed right
    after ``target``. Sorted by ``(source, target, context)`` — a null
    context sorts as the empty string — so two edges from the same source to
    the same target with different context notes stay deterministically
    ordered.
    """
    edges: list[dict] = []
    for entry in state.claim_entries:
        for edge in entry.depends_on:
            edges.append(
                {
                    "source": edge.source,
                    "target": edge.target,
                    "target_kind": edge.target_kind,
                    "target_solidity_recorded": edge.target_solidity_recorded,
                    "context": edge.context,
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


def build_subtree_aggregate_records(state: KbState) -> list[dict]:
    """One record per index/entry-point node, sorted by node_path.

    The subtree_claims list is computed from the leaves under each index's
    directory (mirroring the existing refresh-kb-metadata behavior). The
    entry-point aggregates every leaf in the KB.
    """
    # Map of leaf POSIX path -> claims list, keyed for fast lookup.
    leaf_paths = [(Path(leaf.path), leaf.claims) for leaf in state.leaves]
    rows: list[dict] = []
    for idx in state.indexes:
        if idx.kind == "entry-point":
            all_claims: set[str] = set()
            for _, claims in leaf_paths:
                all_claims.update(claims)
            rows.append(
                {
                    "node_path": idx.path,
                    "node_kind": idx.kind,
                    "subtree_claims": sorted(all_claims),
                }
            )
            continue
        # For a kind: index file, the subtree is every leaf whose POSIX path
        # is under the index's parent directory.
        idx_path = Path(idx.path)
        idx_dir = idx_path.parent
        subtree: set[str] = set()
        for leaf_path, claims in leaf_paths:
            try:
                leaf_path.relative_to(idx_dir)
            except ValueError:
                continue
            subtree.update(claims)
        rows.append(
            {
                "node_path": idx.path,
                "node_kind": idx.kind,
                "subtree_claims": sorted(subtree),
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
    "StrengthenByItem",
    "LeafRecord",
    "IndexRecord",
    "KbState",
    "parse_frontmatter",
    "parse_framework_nodes",
    "parse_leaf",
    "parse_claim_quality_file",
    "collect_known_claim_ids",
    "discover_kb",
    "derive_build_band",
    "build_status_phrase",
    "round_half_up_2dp",
    "compute_solidity",
    "min_dependency_solidity",
    "SolidityCycleError",
    "build_claims_records",
    "build_depends_on_records",
    "build_strengthen_by_records",
    "build_cites_records",
    "build_subtree_aggregate_records",
    "build_all_records",
    "serialize_records",
    "write_jsonl",
    "read_jsonl",
]

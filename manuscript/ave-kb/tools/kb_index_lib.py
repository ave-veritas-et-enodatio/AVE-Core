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
EXCLUDE_NAMES = {"claim-quality.md", "claim-quality-closure-roadmap.md", "CLAUDE.md", "CONVENTIONS.md", "README.md"}

# Claim-ID pattern: the `clm-` prefix plus 6 lowercase alphanumeric chars.
# The prefix makes the pattern exact — it cannot match incidental prose words.
_CLAIM_ID_RE = re.compile(r"\b(clm-[a-z0-9]{6})\b")
# Either an exp- or clm- id — used to extract id-list frontmatter values that
# may hold either prefix (a `claims:` list holds clm- ids, an `experiments:`
# list holds exp- ids). Longest alternative first is irrelevant here (fixed
# six-char bodies), but the prefix keeps each match exact.
_ANY_ID_RE = re.compile(r"\b((?:clm|exp)-[a-z0-9]{6})\b")
# A canonical-id marker keys either a claim entry (`clm-`) or a support entry
# (`sup-`) in a claim-quality.md register. Both share the same `### Quality`
# entry shape; the discriminating prefix selects how the entry is consumed.
_CANONICAL_ID_RE = re.compile(r"<!--\s*id:\s*(clm-[a-z0-9]{6})\s*-->")
_CANONICAL_SUP_ID_RE = re.compile(r"<!--\s*id:\s*(sup-[a-z0-9]{6})\s*-->")
_CANONICAL_ANY_ID_RE = re.compile(r"<!--\s*id:\s*((?:clm|sup)-[a-z0-9]{6})\s*-->")
# Experiment-ID pattern (INVARIANT-S9): `exp-` prefix plus 6 lowercase
# alphanumeric chars. Exact, like the claim-id pattern.
_EXP_ID_RE = re.compile(r"\b(exp-[a-z0-9]{6})\b")
# Support-ID pattern (INVARIANT-S10): `sup-` prefix plus 6 lowercase
# alphanumeric chars. Exact, like the claim- and exp-id patterns.
_SUP_ID_RE = re.compile(r"\b(sup-[a-z0-9]{6})\b")
# A `strengthens:` block pair line: `clm-<id>: <strength>` (strength a float
# in [0,1]). Indented under the `strengthens:` frontmatter key.
_STRENGTHENS_PAIR_RE = re.compile(
    r"^\s*-?\s*(clm-[a-z0-9]{6})\s*:\s*(-?\d+(?:\.\d+)?)\s*$"
)
# A `supports:` block pair line: `clm-<id>: <fraction>` (on-point fraction a
# float in (0,1]). Indented under the `supports:` frontmatter key. Same shape
# as a strengthens pair; the hosting key disambiguates.
_SUPPORTS_PAIR_RE = re.compile(
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
    relation: str  # "depends" | "strengthens" | "supports"
    target_kind: str
    target_solidity_recorded: float | None
    strength: float | None
    context: str | None
    fraction: float | None = None  # on-point fraction f ∈ (0,1] for "supports"


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
class SupportNode:
    """A non-physical analytical support node (INVARIANT-S10).

    A ``sup-`` is claim-like inside (carries a local-rigor ``quality`` and may
    consume its own ``depends_on`` claims), experiment-like in fan-out (one
    support may help many claims), and contributes to the DERIVATION branch of
    each beneficiary (never the experimental/max branch).

    Its own solidity is computed exactly like a claim:
    ``round2(quality × min(dependency final solidities))``; framework deps
    contribute 1.0; pending propagates (pending ``quality`` OR a pending dep =>
    pending ``sup_solidity``). A free-standing support (no deps) has
    ``sup_solidity == quality``.

    ``supports`` is the tuple of ``(claim_id, fraction)`` beneficiary pairs
    parsed from the hosting leaf's ``supports:`` frontmatter block; each
    ``fraction`` is the on-point fraction f ∈ (0, 1] for that claim. ``quality``
    / ``depends_on`` / ``rationale`` come from the support's claim-quality entry
    (keyed by ``<!-- id: sup-xxxxxx -->``), parallel to a claim entry.
    """

    id: str
    title: str
    canonical_path: str
    canonical_anchor: str
    quality: float | None
    depends_on: tuple[DependsOnEdge, ...]
    supports: tuple[tuple[str, float], ...]
    rationale: str = ""
    # The on-disk ``- solidity:`` value parsed from the support's claim-quality
    # entry (NOT recomputed). Used only by the freshness verifier to detect a
    # stale write-back; the authoritative value is the computed sup_solidity.
    solidity: float | None = None


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
    supports: tuple[SupportNode, ...] = ()


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


def _parse_scalar_number_line(line: str) -> float | None:
    """Parse a `- key: 0.X` line into its leading float (or None if absent).

    Used for a support entry's ``- quality:`` line — the support analog of a
    claim's ``- confidence:`` line, scored by the same rubric. ``*pending*``
    (no numeric token) yields ``None``.
    """
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


def parse_support_quality_entries(
    path: Path,
    kb_root: Path,
    known_ids: set[str] | None = None,
    diagnostic_stream: TextIO | None = None,
) -> dict[str, dict]:
    """Parse every ``<!-- id: sup-xxxxxx -->`` entry in a claim-quality.md file.

    A support entry uses the SAME ``### Quality`` shape as a claim entry, with
    ``quality:`` in place of ``confidence:`` (INVARIANT-S10). This returns the
    claim-quality-resident half of a support node — its local rigor and its own
    dependencies — keyed by sup-id::

        {sup_id: {"quality": float|None, "depends_on": tuple[DependsOnEdge],
                  "rationale": str, "title": str, "canonical_path": str,
                  "canonical_anchor": str, "solidity": float|None}}

    The beneficiary fan-out (``supports:``) is NOT here — it is authored in the
    hosting leaf's frontmatter (parallel to an experiment's ``strengthens:``)
    and parsed by :func:`parse_support_leaf`. The two halves are joined in
    :func:`discover_kb`.

    ``known_ids`` (the set of canonical claim ids) filters a support's
    depends-on targets exactly as for a claim entry; a ``clm-``-shaped target
    outside the set is dropped with a diagnostic.
    """
    raw = path.read_text()
    scrubbed = _strip_code_fences(raw)
    lines = scrubbed.splitlines()
    canonical_rel = _posix_relative(path, kb_root)

    entries_meta: list[tuple[int, str, int, str]] = []
    last_heading_idx: int | None = None
    last_heading_text: str | None = None
    for i, line in enumerate(lines):
        if line.startswith("## "):
            last_heading_idx = i
            last_heading_text = line[3:].strip()
            continue
        m = _CANONICAL_SUP_ID_RE.match(line.strip())
        if m and last_heading_idx is not None and last_heading_text is not None:
            entries_meta.append((i, m.group(1), last_heading_idx, last_heading_text))

    out: dict[str, dict] = {}
    for id_line, sup_id, _hd_idx, hd_text in entries_meta:
        qstart: int | None = None
        for j in range(id_line + 1, len(lines)):
            if lines[j].strip() == "### Quality":
                qstart = j
                break
            if lines[j].startswith("## "):
                break
        qend = len(lines)
        if qstart is not None:
            for j in range(qstart + 1, len(lines)):
                if lines[j].startswith("## "):
                    qend = j
                    break

        quality: float | None = None
        solidity: float | None = None
        rationale = ""
        depends_on: list[DependsOnEdge] = []

        if qstart is not None:
            qlines = lines[qstart + 1 : qend]
            i = 0
            while i < len(qlines):
                stripped = qlines[i].strip()
                if stripped.startswith("- quality:"):
                    quality = _parse_scalar_number_line(stripped)
                    i += 1
                elif stripped.startswith("- solidity:"):
                    solidity, _ = _parse_solidity_line(stripped)
                    i += 1
                elif stripped.startswith("- rationale:"):
                    chunks = [stripped.split(":", 1)[1].strip()]
                    i += 1
                    while i < len(qlines):
                        nxt_strip = qlines[i].strip()
                        if re.match(
                            r"^- (quality|solidity|rationale|depends-on|supports):",
                            nxt_strip,
                        ):
                            break
                        if not nxt_strip:
                            break
                        chunks.append(nxt_strip)
                        i += 1
                    rationale = _normalize_text(" ".join(chunks))
                elif stripped.startswith("- depends-on:"):
                    i += 1
                    dep_lines: list[str] = []
                    while i < len(qlines):
                        nxt = qlines[i]
                        nxt_strip = nxt.strip()
                        if re.match(
                            r"^- (quality|solidity|rationale|supports):", nxt_strip
                        ):
                            break
                        if nxt_strip == "---":
                            break
                        if re.match(r"^\s+-\s+", nxt):
                            dep_lines.append(nxt)
                        elif not nxt_strip:
                            pass
                        elif dep_lines:
                            dep_lines[-1] = dep_lines[-1] + " " + nxt_strip
                        i += 1
                    for dep_line in dep_lines:
                        depends_on.extend(
                            _parse_depends_on_line(
                                dep_line,
                                sup_id,
                                known_ids=known_ids,
                                diagnostic_stream=diagnostic_stream,
                                canonical_path=canonical_rel,
                            )
                        )
                else:
                    i += 1

        out[sup_id] = {
            "quality": quality,
            "solidity": solidity,
            "rationale": rationale,
            "title": hd_text,
            "canonical_path": canonical_rel,
            "canonical_anchor": _slugify_heading(hd_text),
            "depends_on": tuple(depends_on),
        }
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
    """Raised when a leaf hosting an ``exp-id`` experiment node is malformed.

    The leaf carries an ``exp-id`` that does not match the
    ``\\bexp-[a-z0-9]{6}\\b`` format, a ``status`` outside ``{run, pending}``,
    or an ``experiments:`` reference field (an owning experiment-hosting leaf
    must not also reference other experiments). Co-hosting ``claims:`` is
    allowed — ``exp-id`` and ``claims:`` are orthogonal node-bodies (INVARIANT-S9).
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
    """Parse an experiment-hosting leaf into an ExperimentNode (INVARIANT-S9).

    Experiment-ness is conferred by a leaf HOSTING an ``exp-id``, not by a
    ``kind``: any ``kind: leaf`` or ``kind: leaf-as-index`` container that
    carries a well-formed ``exp-id:`` originates an experiment node, regardless
    of whether it ALSO carries ``claims:`` (the two are orthogonal node-bodies
    in one container). Returns ``None`` if the file has no frontmatter, is not a
    leaf-kind container, or declares no ``exp-id``.

    The frontmatter carries ``exp-id``, ``status``, and a ``strengthens:`` block
    of ``clm-<id>: <strength>`` pairs (one per line, indented under the
    ``strengthens:`` key). ``strengthens`` pairs are returned in source order;
    a target may include a claim originated by this same leaf (a node→node edge
    between two distinct co-located node-bodies — not a self-loop).

    Raises :class:`ExperimentLeafError` when the leaf carries an
    ``experiments:`` reference field (an owning experiment-hosting leaf must not
    also reference other experiments), its ``exp-id`` is malformed, or its
    ``status`` is outside ``{run, pending}``.
    """
    text = path.read_text()
    m = _FRONTMATTER_RE.search(text)
    if not m:
        return None
    body = m.group(1)
    lines = body.splitlines()

    # Quick top-level scan: kind, exp-id, status, and detection of an
    # `experiments:` reference field. ``strengthens:`` opens an indented
    # sub-block. ``claims:`` / ``no-claim:`` are NOT inspected here — they are
    # the leaf's separate claim node-body, orthogonal to the experiment.
    kind = ""
    exp_id: str | None = None
    status: str | None = None
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
            elif key == "experiments":
                if value:
                    has_experiments_ref = True

    # Only leaf-kind containers host experiment node-bodies; a container with
    # no exp-id originates no experiment (the common case — return None).
    if kind not in ("leaf", "leaf-as-index"):
        return None
    if exp_id is None:
        return None

    rel = _posix_relative(path, kb_root)
    if has_experiments_ref:
        raise ExperimentLeafError(
            f"{rel}: experiment-hosting leaf carries experiments: — an owning "
            f"experiment leaf must not also reference other experiments."
        )
    if not _EXP_ID_RE.fullmatch(exp_id):
        raise ExperimentLeafError(
            f"{rel}: experiment-hosting leaf has malformed exp-id "
            f"{exp_id!r} (expected \\bexp-[a-z0-9]{{6}}\\b)."
        )
    if status not in ("run", "pending"):
        raise ExperimentLeafError(
            f"{rel}: experiment-hosting leaf has invalid status {status!r} "
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


class SupportLeafError(ValueError):
    """Raised when a leaf hosting a ``sup-id`` support node is malformed.

    The leaf carries a ``sup-id`` that does not match ``\\bsup-[a-z0-9]{6}\\b``,
    or a ``supports:`` block with a malformed claim id or an on-point
    ``fraction`` outside ``(0, 1]`` (0 is excluded — a zero-relevance support
    edge is not authored; > 1 is out of range). Co-hosting ``claims:`` /
    ``exp-id:`` / ``no-claim:`` is allowed — they are orthogonal node-bodies
    (INVARIANT-S10).
    """


def parse_support_leaf(path: Path, kb_root: Path) -> SupportNode | None:
    """Parse a support-hosting leaf into a partial SupportNode (INVARIANT-S10).

    Support-ness is conferred by a leaf HOSTING a ``sup-id`` (parallel to how
    an ``exp-id`` confers experiment-ness): any ``kind: leaf`` /
    ``leaf-as-index`` container carrying a well-formed ``sup-id:`` originates a
    support node, regardless of whether it ALSO carries ``claims:`` /
    ``exp-id:`` / ``no-claim:`` (orthogonal node-bodies). Returns ``None`` if the
    file has no frontmatter, is not a leaf-kind container, or declares no
    ``sup-id``.

    The frontmatter carries ``sup-id`` and a ``supports:`` block of
    ``clm-<id>: <fraction>`` beneficiary pairs (one per line, indented under the
    ``supports:`` key), where ``fraction`` is the on-point fraction f ∈ (0, 1].
    The returned node carries the canonical_path/anchor/title from the leaf and
    the ``supports`` fan-out; its ``quality`` / ``depends_on`` / ``rationale``
    are filled in from the support's claim-quality entry by :func:`discover_kb`.

    Raises :class:`SupportLeafError` for a malformed ``sup-id``, a malformed
    ``supports:`` claim id, or an on-point fraction outside ``(0, 1]``.
    """
    text = path.read_text()
    m = _FRONTMATTER_RE.search(text)
    if not m:
        return None
    lines = m.group(1).splitlines()

    kind = ""
    sup_id: str | None = None
    in_supports = False
    pairs: list[tuple[str, float]] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        pair = _SUPPORTS_PAIR_RE.match(line)
        if in_supports and pair:
            pairs.append((pair.group(1), float(pair.group(2))))
            continue
        if ":" in stripped:
            key = stripped.split(":", 1)[0].strip().lstrip("- ").strip()
            value = stripped.split(":", 1)[1].strip()
            if key == "supports":
                in_supports = True
                continue
            in_supports = False
            if key == "kind":
                kind = value
            elif key == "sup-id":
                sup_id = value

    if kind not in ("leaf", "leaf-as-index"):
        return None
    if sup_id is None:
        return None

    rel = _posix_relative(path, kb_root)
    if not _SUP_ID_RE.fullmatch(sup_id):
        raise SupportLeafError(
            f"{rel}: support-hosting leaf has malformed sup-id {sup_id!r} "
            f"(expected \\bsup-[a-z0-9]{{6}}\\b)."
        )
    for claim_id, fraction in pairs:
        if not (0.0 < fraction <= 1.0):
            raise SupportLeafError(
                f"{rel}: support {sup_id} on-point fraction for {claim_id} is "
                f"{fraction} — must be in (0, 1] (0 is excluded; > 1 invalid)."
            )

    title = _experiment_heading(text)
    return SupportNode(
        id=sup_id,
        title=title,
        canonical_path=rel,
        canonical_anchor=_slugify_heading(title),
        quality=None,  # filled from the claim-quality entry in discover_kb
        depends_on=(),  # filled from the claim-quality entry in discover_kb
        supports=tuple(pairs),
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
    support_quality: dict[str, dict] = {}
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
        # Support entries (`<!-- id: sup-xxxxxx -->`) share the register and
        # the `### Quality` shape; collect their claim-quality-resident half
        # (quality + own depends-on + rationale) keyed by sup-id (INVARIANT-S10).
        support_quality.update(
            parse_support_quality_entries(
                cq,
                kb_root,
                known_ids=known_ids,
                diagnostic_stream=diagnostic_stream,
            )
        )

    leaves: list[LeafRecord] = []
    indexes: list[IndexRecord] = []
    experiments: list[ExperimentNode] = []
    support_leaves: list[SupportNode] = []
    for p in _kb_files(kb_root):
        # A single container may host SEVERAL orthogonal node-bodies — a claim
        # list (LeafRecord), an experiment (ExperimentNode), and/or a support
        # (SupportNode): `kind` is the container's topography role, while
        # `claims:` / `exp-id:` / `sup-id:` are independent claim-graph
        # node-bodies it originates. Run every parser; do not short-circuit
        # (INVARIANT-S9 / S10).
        leaf = parse_leaf(p, kb_root)
        if leaf is not None:
            leaves.append(leaf)
        exp = parse_experiment_leaf(p, kb_root)
        if exp is not None:
            experiments.append(exp)
        sup = parse_support_leaf(p, kb_root)
        if sup is not None:
            support_leaves.append(sup)
        if leaf is None and exp is None and sup is None:
            idx = _parse_index(p, kb_root)
            if idx is not None:
                indexes.append(idx)

    # Join each support leaf's fan-out (supports edges, canonical home) with its
    # claim-quality-resident internals (quality, own deps, rationale). A support
    # leaf with no matching claim-quality entry stays pending-quality with no
    # own deps — the verifier flags the missing entry as an orphan.
    supports: list[SupportNode] = []
    for sup in support_leaves:
        cq_half = support_quality.get(sup.id, {})
        supports.append(
            SupportNode(
                id=sup.id,
                title=sup.title,
                canonical_path=sup.canonical_path,
                canonical_anchor=sup.canonical_anchor,
                quality=cq_half.get("quality"),
                depends_on=cq_half.get("depends_on", ()),
                supports=sup.supports,
                rationale=cq_half.get("rationale", ""),
                solidity=cq_half.get("solidity"),
            )
        )

    framework_nodes = parse_framework_nodes(kb_root)

    return KbState(
        claim_entries=tuple(claim_entries),
        leaves=tuple(leaves),
        indexes=tuple(indexes),
        framework_nodes=tuple(framework_nodes),
        experiments=tuple(experiments),
        supports=tuple(supports),
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


class _SolidityResults(dict):
    """A ``{claim_id: SolidityResult}`` dict that also carries support solidities.

    Subclasses ``dict`` so every existing caller (which indexes by claim id and
    iterates ``.items()``) is unaffected, while exposing the computed
    ``sup_solidity`` map as a sidecar attribute. The single computation in
    :func:`compute_solidity_full` populates both, so the support record builder,
    the claim-quality write-back, and the verifier all read the SAME values —
    never re-deriving sup_solidity at a second call site (the dual-compute trap).
    """

    sup_solidity: dict[str, float | None]

    def __init__(self, results: dict | None = None) -> None:
        super().__init__(results or {})
        self.sup_solidity = {}


def _sup_solidity_from_deps(
    quality: float | None,
    depends_on,
    final_of,
) -> float | None:
    """Claim-style derivation of a support node's own solidity.

    ``round2(quality × min(dependency final solidities))``; framework deps
    contribute 1.0; a free-standing support (no deps) has ``sup_solidity ==
    quality``. Returns ``None`` (pending) if ``quality`` is pending OR any claim
    dependency's final is pending — exactly the claim derivation rule, applied
    with the support's ``quality`` in place of a claim's ``confidence``.
    """
    if quality is None:
        return None
    dep_finals: list[float] = []
    for edge in depends_on:
        if edge.relation != "depends":
            continue
        if edge.target_kind == "claim":
            dep_final = final_of(edge.target)
            if dep_final is None:
                return None  # pending dep poisons the support's own solidity
            dep_finals.append(dep_final)
        else:
            dep_finals.append(1.0)
    if not dep_finals:
        return quality
    return round_half_up_2dp(quality * min(dep_finals))


def compute_solidity_full(
    claim_entries, experiments=(), supports=()
) -> dict[str, SolidityResult]:
    """Compute derivation / experimental / final solidity for every claim.

    THE definitive solidity rule (SCHEMA "Solidity branches"), now including the
    DERIVATION-branch lift from support nodes (INVARIANT-S10). One result per
    claim with a numeric ``confidence`` OR a non-pending lift source (a run
    experiment, or a support edge with a non-pending ``sup_solidity``). A claim
    with none is fully pending and omitted (treat absence as ``*pending*``).

    Algorithm:

    * **experimental_solidity[C]** = ``max`` of ``edge.strength`` over all
      ``relation:"strengthens"`` run-experiment edges into ``C``; ``None`` if
      none. Unrun experiments contribute nothing. The MAX/experimental branch.
    * **sup_solidity[S]** (computed in unified topo order — see below) =
      ``round2(quality × min(S's dep finals))``; pending propagates. Each
      support feeds the DERIVATION branch of its beneficiaries, never the
      experimental/max branch.
    * **local_quality[C]** = ``max(confidence[C], max over supporting sups S of
      sup_solidity[S] × f)``, where a pending ``sup_solidity`` is EXCLUDED from
      the max (no NaN, no poison). A support lift never drags a beneficiary with
      otherwise-valid quality to pending — pending flows ONLY from a claim's own
      load-bearing ``depends-on``.
    * **derivation_solidity[C]** = ``round2(local_quality[C] × min(C's claim-dep
      finals))``, framework deps 1.0; ``None`` if ``local_quality`` is pending
      (confidence pending AND no support lift) OR any claim-dep's final is
      pending. So a support lift is still dep-gated — it does NOT bypass C's own
      deps the way an experiment's max-branch does.
    * **final[C]** = ``max`` over the non-None of ``{derivation, experimental}``;
      ``None`` iff both are None.

    Unified Kahn topo over the combined claim+support graph: a claim/support is
    processed after every claim it depends on (so dep finals are known) and a
    claim after every support that supports it (so the lift is known). Raises
    :class:`SolidityCycleError` if that combined graph has a cycle. Experiments
    are terminal and introduce no cycles.

    With ``supports=()`` this reduces exactly to the prior behavior:
    ``local_quality[C] == confidence[C]`` and the support machinery is inert.
    """
    entries = {e.id: e for e in claim_entries}
    sups = {s.id: s for s in supports}

    # --- experimental_solidity[C]: max strength over run-experiment edges ---
    experimental: dict[str, float] = {}
    for exp in experiments:
        if exp.status != "run":
            continue
        for claim_id, strength in exp.strengthens:
            prev = experimental.get(claim_id)
            if prev is None or strength > prev:
                experimental[claim_id] = strength

    # --- supporters[C]: list of (sup_id, fraction) supporting claim C ---
    supporters: dict[str, list[tuple[str, float]]] = {}
    for sup in supports:
        for claim_id, fraction in sup.supports:
            supporters.setdefault(claim_id, []).append((sup.id, fraction))

    # --- unified topo over the combined claim + support graph ---
    # A claim participates as a topo node when it has numeric confidence OR is
    # lifted by ≥1 support (its derivation may be authored from a support even
    # with pending confidence). A support always participates (its solidity is
    # always defined, possibly pending). Edges (X before Y): claim/support → its
    # claim-deps; claim → each support that supports it.
    numeric_claims = {eid for eid, e in entries.items() if e.confidence is not None}
    lifted_claims = set(supporters)
    claim_nodes = numeric_claims | (lifted_claims & set(entries))
    sup_nodes = set(sups)
    topo_nodes = claim_nodes | sup_nodes

    indegree: dict[str, int] = {n: 0 for n in topo_nodes}
    dependents: dict[str, list[str]] = {n: [] for n in topo_nodes}

    def _add_edge(before: str, after: str) -> None:
        # `after` cannot be processed until `before` is done.
        if before in topo_nodes and after in topo_nodes:
            indegree[after] += 1
            dependents[before].append(after)

    for cid in claim_nodes:
        for edge in entries[cid].depends_on:
            if edge.relation == "depends" and edge.target_kind == "claim":
                _add_edge(edge.target, cid)
        for sup_id, _f in supporters.get(cid, ()):
            _add_edge(sup_id, cid)
    for sid, sup in sups.items():
        for edge in sup.depends_on:
            if edge.relation == "depends" and edge.target_kind == "claim":
                _add_edge(edge.target, sid)

    queue = sorted(n for n in topo_nodes if indegree[n] == 0)
    order: list[str] = []
    while queue:
        node = queue.pop(0)
        order.append(node)
        for dep in sorted(dependents[node]):
            indegree[dep] -= 1
            if indegree[dep] == 0:
                queue.append(dep)
                queue.sort()

    if len(order) != len(topo_nodes):
        cycle_members = sorted(n for n in topo_nodes if indegree[n] > 0)
        raise SolidityCycleError(cycle_members)

    results: dict[str, SolidityResult] = {}
    final: dict[str, float | None] = {}
    sup_solidity: dict[str, float | None] = {}

    # Claims that are neither topo nodes (pending confidence, no support lift)
    # may still be experimentally rescued; seed their final from the max-branch
    # so a numeric claim depending on a rescued pending-confidence claim sees
    # the rescued final. (Their derivation is always pending — no topo needed.)
    for eid, entry in entries.items():
        if eid in claim_nodes:
            continue
        exp_sol = experimental.get(eid)
        results[eid] = SolidityResult(None, exp_sol, exp_sol)
        final[eid] = exp_sol

    def _final_of(claim_id: str) -> float | None:
        return final.get(claim_id)

    for node in order:
        if node in sup_nodes:
            sup = sups[node]
            sup_solidity[node] = _sup_solidity_from_deps(
                sup.quality, sup.depends_on, _final_of
            )
            continue

        entry = entries[node]
        # local_quality: max(confidence, max over supporting sups of
        # sup_solidity × f), pending sup excluded (no poison). Confidence
        # pending contributes nothing to the max.
        local_quality: float | None = entry.confidence
        for sup_id, fraction in supporters.get(node, ()):
            s_sol = sup_solidity.get(sup_id)
            if s_sol is None:
                continue  # pending support — excluded from the max
            lift = s_sol * fraction
            if local_quality is None or lift > local_quality:
                local_quality = lift

        # derivation: local_quality × min(claim-dep finals), framework deps 1.0.
        dep_finals: list[float] = []
        derivation: float | None
        pending = local_quality is None
        if not pending:
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
            derivation = round_half_up_2dp(local_quality * min(dep_finals))
        else:
            derivation = local_quality
        exp_sol = experimental.get(node)
        fin = _max_nonnull(derivation, exp_sol)
        final[node] = fin
        results[node] = SolidityResult(derivation, exp_sol, fin)

    # Expose support solidities via a private sidecar attribute on the result
    # dict so callers that need them (record builder, write-back, verifier) read
    # the SAME computed values — no second derivation (the dual-compute trap).
    results_sidecar = _SolidityResults(results)
    results_sidecar.sup_solidity = dict(sup_solidity)
    return results_sidecar


def _max_nonnull(a: float | None, b: float | None) -> float | None:
    """Return the max of the non-None values; None iff both are None."""
    if a is None:
        return b
    if b is None:
        return a
    return max(a, b)


def compute_solidity(claim_entries, experiments=(), supports=()) -> dict[str, float]:
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
    full = compute_solidity_full(claim_entries, experiments, supports)
    return {cid: r.final for cid, r in full.items() if r.final is not None}


def compute_support_solidity(
    claim_entries, experiments=(), supports=()
) -> dict[str, float]:
    """Compute the FINAL ``sup_solidity`` for every scorable support node.

    Reads the SAME single computation as :func:`compute_solidity` /
    :func:`compute_solidity_full` (no second derivation): returns
    ``{sup_id: sup_solidity}`` for every support whose solidity is non-pending.
    A support with a pending solidity (pending ``quality`` OR a pending claim
    dependency) is OMITTED — every consumer treats "absent" identically to
    "pending", exactly as for a pending claim.
    """
    full = compute_solidity_full(claim_entries, experiments, supports)
    return {
        sid: sol
        for sid, sol in full.sup_solidity.items()
        if sol is not None
    }


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
    # claim-quality.md write-back; never computed twice. It carries both the
    # per-claim results AND the per-support sup_solidity sidecar.
    full = compute_solidity_full(
        state.claim_entries, state.experiments, state.supports
    )

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
    for sup in state.supports:
        # A support node's own computed solidity comes from the SAME shared
        # computation (sup_solidity sidecar) — never re-derived here.
        out.append(
            {
                "node_type": "support",
                "id": sup.id,
                "title": sup.title,
                "canonical_path": sup.canonical_path,
                "canonical_anchor": sup.canonical_anchor,
                "quality": sup.quality,
                "solidity": full.sup_solidity.get(sup.id),
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
    """One record per forward graph edge — ``depends`` / ``strengthens`` / ``supports``.

    Field order per SCHEMA: ``source``, ``target``, ``relation``,
    ``target_kind``, ``target_solidity_recorded``, ``strength``, ``context``,
    ``fraction``. Every record carries all eight keys (schema closure); only the
    relevant ones are non-null per edge class.

    * ``depends`` edges come from claim (and now SUPPORT) Quality sections —
      ``strength:null``, ``fraction:null``. A support's own deps are ``depends``
      edges with ``source`` the sup-id (INVARIANT-S10).
    * ``strengthens`` edges come from each experiment leaf's ``strengthens:``
      block (``source: exp-id``, ``target: clm-id``, ``strength:<value>``,
      ``fraction:null``).
    * ``supports`` edges come from each support leaf's ``supports:`` block
      (``source: sup-id``, ``target: clm-id``, ``relation:"supports"``,
      ``target_kind:"claim"``, ``strength:null``, ``fraction:<f>`` where
      f ∈ (0, 1]). The DERIVATION-branch analog of a ``strengthens`` edge.

    Sorted by ``(source, target, context)`` — a null context sorts as the empty
    string — so two edges from one source to one target with different context
    notes stay deterministically ordered.
    """
    edges: list[dict] = []

    def _emit(
        source, target, relation, target_kind,
        target_solidity_recorded=None, strength=None, context=None, fraction=None,
    ):
        edges.append(
            {
                "source": source,
                "target": target,
                "relation": relation,
                "target_kind": target_kind,
                "target_solidity_recorded": target_solidity_recorded,
                "strength": strength,
                "context": context,
                "fraction": fraction,
            }
        )

    for entry in state.claim_entries:
        for edge in entry.depends_on:
            _emit(
                edge.source, edge.target, edge.relation, edge.target_kind,
                edge.target_solidity_recorded, edge.strength, edge.context,
                edge.fraction,
            )
    for sup in state.supports:
        # A support's OWN dependencies — depends edges sourced at the sup-id.
        for edge in sup.depends_on:
            _emit(
                edge.source, edge.target, edge.relation, edge.target_kind,
                edge.target_solidity_recorded, edge.strength, edge.context,
                edge.fraction,
            )
        # A support's beneficiary fan-out — supports edges sourced at the sup-id.
        for claim_id, fraction in sup.supports:
            _emit(
                sup.id, claim_id, "supports", "claim",
                fraction=fraction,
            )
    for exp in state.experiments:
        for claim_id, strength in exp.strengthens:
            _emit(
                exp.id, claim_id, "strengthens", "claim", strength=strength,
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


def build_supported_by_records(state: KbState) -> list[dict]:
    """One record per (claim, supporting support) edge — the reverse view.

    The ``supported-by`` view answers "which support nodes lift claim X, and by
    how much?" — analogous to ``strengthen-by`` as untraversed bookkeeping
    (INVARIANT-S10). It is NOT consulted for solidity (that flows forward
    through the ``supports`` edges in ``depends-on.jsonl``); it is a convenience
    reverse index. Each record carries the on-point ``fraction`` and the
    support's computed ``sup_solidity`` (the SAME shared computation; pending =>
    ``null``) so a reviewer sees the realized lift contribution at a glance.

    Sorted by ``(claim_id, sup_id)``.
    """
    sup_solidity = compute_solidity_full(
        state.claim_entries, state.experiments, state.supports
    ).sup_solidity
    rows: list[dict] = []
    for sup in state.supports:
        for claim_id, fraction in sup.supports:
            rows.append(
                {
                    "claim_id": claim_id,
                    "sup_id": sup.id,
                    "fraction": fraction,
                    "sup_solidity": sup_solidity.get(sup.id),
                }
            )
    rows.sort(key=lambda r: (r["claim_id"], r["sup_id"]))
    return rows


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
        "supported-by": build_supported_by_records(state),
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
    "SupportNode",
    "SupportLeafError",
    "StrengthenByItem",
    "LeafRecord",
    "IndexRecord",
    "KbState",
    "SolidityResult",
    "parse_frontmatter",
    "parse_framework_nodes",
    "parse_leaf",
    "parse_experiment_leaf",
    "parse_support_leaf",
    "parse_claim_quality_file",
    "parse_support_quality_entries",
    "collect_known_claim_ids",
    "discover_kb",
    "derive_build_band",
    "build_status_phrase",
    "round_half_up_2dp",
    "compute_solidity",
    "compute_solidity_full",
    "compute_support_solidity",
    "min_dependency_solidity",
    "SolidityCycleError",
    "build_claims_records",
    "build_depends_on_records",
    "build_strengthen_by_records",
    "build_supported_by_records",
    "build_cites_records",
    "compute_subtree_aggregates",
    "build_subtree_aggregate_records",
    "build_all_records",
    "serialize_records",
    "write_jsonl",
    "read_jsonl",
]

"""Runtime query interface over the AVE-KB derived index.

Consumes the JSONL artifact set under ``manuscript/ave-kb/.index/`` and exposes
the canonical question shapes from ``SCHEMA.md`` §"Query semantics" as pure
in-memory lookups. The module is self-contained: it does not import from
``manuscript/ave-kb/tools/`` and uses stdlib only.

Construct an ``Index`` via ``load()``; all queries are dict lookups against
pre-built inverse indices.
"""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

DEFAULT_INDEX_DIR_HINT = "manuscript/ave-kb/.index"

_REQUIRED_FILES = (
    "claims.jsonl",
    "depends-on.jsonl",
    "strengthen-by.jsonl",
    "cites.jsonl",
    "subtree-aggregates.jsonl",
)


# ---------------------------------------------------------------------------
# Dataclasses
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class Claim:
    """A canonical claim-quality entry."""

    id: str
    title: str
    canonical_path: str
    canonical_anchor: str
    confidence: float | None
    solidity: float | None
    build_status: str | None
    build_band: str
    rationale: str
    depends_on_count: int
    strengthen_by_count: int
    citation_count: int


@dataclass(frozen=True, slots=True)
class DependsOnEdge:
    """A forward dependency edge from ``source`` to ``target``."""

    source: str
    target: str
    target_solidity_recorded: float | None
    context: str | None


@dataclass(frozen=True, slots=True)
class StrengthenByItem:
    """A single strengthen-by bullet from a claim's Quality section."""

    claim_id: str
    item_idx: int
    text: str
    mentioned_ids: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class CitationEdge:
    """A (claim, leaf) citation edge."""

    claim_id: str
    leaf_path: str
    leaf_kind: str
    tier2_marked: bool


@dataclass(frozen=True, slots=True)
class SubtreeAggregate:
    """A precomputed subtree-claims aggregation for one index/entry-point node."""

    node_path: str
    node_kind: str
    subtree_claims: tuple[str, ...]


# ---------------------------------------------------------------------------
# Default index location resolution
# ---------------------------------------------------------------------------


def _default_index_dir() -> Path:
    """Resolve the default .index directory.

    Walks up from this module's location looking for a directory that contains
    both ``src/`` and ``manuscript/`` (the AVE-Core repo root). If found,
    returns ``<root>/manuscript/ave-kb/.index``. Otherwise falls back to
    ``<cwd>/manuscript/ave-kb/.index``.
    """
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "src").is_dir() and (parent / "manuscript").is_dir():
            return parent / DEFAULT_INDEX_DIR_HINT
    return Path.cwd() / DEFAULT_INDEX_DIR_HINT


# ---------------------------------------------------------------------------
# JSONL parsing
# ---------------------------------------------------------------------------


def _read_jsonl(path: Path) -> list[dict]:
    """Parse a JSONL file. Blank lines skipped; malformed lines raise ValueError."""
    out: list[dict] = []
    with path.open("r", encoding="utf-8") as fh:
        for lineno, line in enumerate(fh, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                obj = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{lineno}: malformed JSON: {exc.msg}") from exc
            if not isinstance(obj, dict):
                raise ValueError(f"{path}:{lineno}: expected JSON object, got {type(obj).__name__}")
            out.append(obj)
    return out


def _claim_from_record(rec: dict) -> Claim:
    return Claim(
        id=rec["id"],
        title=rec["title"],
        canonical_path=rec["canonical_path"],
        canonical_anchor=rec["canonical_anchor"],
        confidence=rec.get("confidence"),
        solidity=rec.get("solidity"),
        build_status=rec.get("build_status"),
        build_band=rec["build_band"],
        rationale=rec["rationale"],
        depends_on_count=rec["depends_on_count"],
        strengthen_by_count=rec["strengthen_by_count"],
        citation_count=rec["citation_count"],
    )


def _depends_on_from_record(rec: dict) -> DependsOnEdge:
    return DependsOnEdge(
        source=rec["source"],
        target=rec["target"],
        target_solidity_recorded=rec.get("target_solidity_recorded"),
        context=rec.get("context"),
    )


def _strengthen_by_from_record(rec: dict) -> StrengthenByItem:
    return StrengthenByItem(
        claim_id=rec["claim_id"],
        item_idx=rec["item_idx"],
        text=rec["text"],
        mentioned_ids=tuple(rec.get("mentioned_ids") or ()),
    )


def _citation_from_record(rec: dict) -> CitationEdge:
    return CitationEdge(
        claim_id=rec["claim_id"],
        leaf_path=rec["leaf_path"],
        leaf_kind=rec["leaf_kind"],
        tier2_marked=bool(rec["tier2_marked"]),
    )


def _subtree_from_record(rec: dict) -> SubtreeAggregate:
    return SubtreeAggregate(
        node_path=rec["node_path"],
        node_kind=rec["node_kind"],
        subtree_claims=tuple(rec.get("subtree_claims") or ()),
    )


# ---------------------------------------------------------------------------
# Index class
# ---------------------------------------------------------------------------


def _unique_sorted(values: Iterable[str]) -> list[str]:
    """Deduplicate and sort a list of strings."""
    return sorted(set(values))


class Index:
    """In-memory query interface over the .index/*.jsonl artifact set.

    Construct via :func:`load`. After construction, all queries are dict lookups
    against pre-built indices — microseconds at current KB scale.
    """

    def __init__(
        self,
        claims: list[Claim],
        depends_on: list[DependsOnEdge],
        strengthen_by: list[StrengthenByItem],
        cites: list[CitationEdge],
        subtree_aggregates: list[SubtreeAggregate],
    ) -> None:
        self._claims: list[Claim] = sorted(claims, key=lambda c: c.id)
        self._depends_on: list[DependsOnEdge] = list(depends_on)
        self._strengthen_by: list[StrengthenByItem] = list(strengthen_by)
        self._cites: list[CitationEdge] = list(cites)
        self._subtree_aggregates: list[SubtreeAggregate] = list(subtree_aggregates)

        self._by_id: dict[str, Claim] = {c.id: c for c in self._claims}

        # Forward / inverse dependency adjacency.
        deps_fwd: dict[str, set[str]] = defaultdict(set)
        deps_rev: dict[str, set[str]] = defaultdict(set)
        deps_fwd_edges: dict[str, list[DependsOnEdge]] = defaultdict(list)
        for edge in self._depends_on:
            deps_fwd[edge.source].add(edge.target)
            deps_rev[edge.target].add(edge.source)
            deps_fwd_edges[edge.source].append(edge)
        self._deps_fwd: dict[str, list[str]] = {k: sorted(v) for k, v in deps_fwd.items()}
        self._deps_rev: dict[str, list[str]] = {k: sorted(v) for k, v in deps_rev.items()}
        self._deps_fwd_edges: dict[str, list[DependsOnEdge]] = {
            k: sorted(v, key=lambda e: e.target) for k, v in deps_fwd_edges.items()
        }

        # Strengthen-by — grouped by claim_id (ordered by item_idx) and inverse
        # mention map (mentioned_id -> claims that mention it).
        sb_by_claim: dict[str, list[StrengthenByItem]] = defaultdict(list)
        sb_mentions: dict[str, set[str]] = defaultdict(set)
        for item in self._strengthen_by:
            sb_by_claim[item.claim_id].append(item)
            for mid in item.mentioned_ids:
                sb_mentions[mid].add(item.claim_id)
        self._strengthen_by_claim: dict[str, list[StrengthenByItem]] = {
            k: sorted(v, key=lambda it: it.item_idx) for k, v in sb_by_claim.items()
        }
        self._strengthen_mentions: dict[str, list[str]] = {k: sorted(v) for k, v in sb_mentions.items()}

        # Citations — by claim and by leaf path.
        cited_by: dict[str, list[CitationEdge]] = defaultdict(list)
        leaf_claims: dict[str, set[str]] = defaultdict(set)
        for cite in self._cites:
            cited_by[cite.claim_id].append(cite)
            leaf_claims[cite.leaf_path].add(cite.claim_id)
        self._cited_by: dict[str, list[CitationEdge]] = {
            k: sorted(v, key=lambda e: e.leaf_path) for k, v in cited_by.items()
        }
        self._leaf_claims: dict[str, list[str]] = {k: sorted(v) for k, v in leaf_claims.items()}

        # Subtree aggregates — keyed by node_path.
        self._subtree_by_path: dict[str, SubtreeAggregate] = {agg.node_path: agg for agg in self._subtree_aggregates}
        # Identify the entry-point node so callers can pass "" / "." for it.
        self._entry_point: SubtreeAggregate | None = next(
            (agg for agg in self._subtree_aggregates if agg.node_kind == "entry-point"),
            None,
        )

    # ---- Forward dependency edges --------------------------------------

    def depends_on(self, claim_id: str) -> list[str]:
        """Claim ids that ``claim_id`` depends on (deduplicated, sorted)."""
        return list(self._deps_fwd.get(claim_id, ()))

    def dependents_of(self, claim_id: str) -> list[str]:
        """Claim ids that depend on ``claim_id`` (inverse, deduplicated, sorted)."""
        return list(self._deps_rev.get(claim_id, ()))

    def depends_on_edges(self, claim_id: str) -> list[DependsOnEdge]:
        """Full forward edge records sourced from ``claim_id`` (sorted by target)."""
        return list(self._deps_fwd_edges.get(claim_id, ()))

    # ---- Open work ------------------------------------------------------

    def strengthen_by(self, claim_id: str) -> list[StrengthenByItem]:
        """Strengthen-by items for ``claim_id`` (ordered by ``item_idx``)."""
        return list(self._strengthen_by_claim.get(claim_id, ()))

    def gated_on(self, claim_id: str) -> list[str]:
        """Claim ids whose strengthen-by items mention ``claim_id`` (sorted)."""
        return list(self._strengthen_mentions.get(claim_id, ()))

    # ---- Citations ------------------------------------------------------

    def cited_by(self, claim_id: str) -> list[CitationEdge]:
        """Citation edges naming this claim (sorted by leaf_path)."""
        return list(self._cited_by.get(claim_id, ()))

    def claims_in_leaf(self, leaf_path: str) -> list[str]:
        """Claim ids cited by ``leaf_path`` (sorted)."""
        return list(self._leaf_claims.get(leaf_path, ()))

    # ---- Subtree aggregation -------------------------------------------

    def subtree_claims(self, node_path: str) -> list[str]:
        """All claim ids under ``node_path``.

        Accepts:
          - ``""`` or ``"."`` -> the entry-point's aggregate (whole tree)
          - a node-file path like ``"vol1/index.md"`` -> exact match
          - a directory path like ``"vol1"`` -> matches ``"vol1/index.md"``
        """
        if node_path in ("", "."):
            if self._entry_point is None:
                return []
            return list(self._entry_point.subtree_claims)
        # Try exact node_path first (e.g., "vol1/index.md").
        agg = self._subtree_by_path.get(node_path)
        if agg is None:
            # Try directory-style: strip trailing slash, append "/index.md".
            candidate = node_path.rstrip("/") + "/index.md"
            agg = self._subtree_by_path.get(candidate)
        if agg is None:
            return []
        return list(agg.subtree_claims)

    # ---- Filters --------------------------------------------------------

    def solidity_below(self, threshold: float) -> list[Claim]:
        """Claims with non-null ``solidity`` below ``threshold``.

        Sort: by solidity ascending, then by id (stable lexicographic).
        Claims with ``solidity is None`` are excluded.
        """
        matching = [c for c in self._claims if c.solidity is not None and c.solidity < threshold]
        matching.sort(key=lambda c: (c.solidity, c.id))  # type: ignore[arg-type]
        return matching

    def in_band(self, band: str) -> list[Claim]:
        """Claims in the given ``build_band`` (sorted by id)."""
        return [c for c in self._claims if c.build_band == band]

    # ---- Lookup ---------------------------------------------------------

    def claim(self, claim_id: str) -> Claim | None:
        """Return the Claim record, or None if not present."""
        return self._by_id.get(claim_id)

    def __len__(self) -> int:
        return len(self._claims)

    # ---- Inspection -----------------------------------------------------

    @property
    def all_claims(self) -> list[Claim]:
        """All claim records, sorted by id."""
        return list(self._claims)

    @property
    def stats(self) -> dict[str, int]:
        """Counts useful for ``ave-kb stats``-style introspection."""
        return {
            "claims": len(self._claims),
            "depends_on_edges": len(self._depends_on),
            "strengthen_by_items": len(self._strengthen_by),
            "citation_edges": len(self._cites),
            "subtree_aggregates": len(self._subtree_aggregates),
        }


# ---------------------------------------------------------------------------
# Loader
# ---------------------------------------------------------------------------


def load(path: Path | str | None = None) -> Index:
    """Load the index from a directory of ``.index/*.jsonl`` files.

    If ``path`` is None, the directory is auto-resolved via
    :func:`_default_index_dir` (walks up to find the AVE-Core repo root).

    Raises:
        FileNotFoundError: if any required JSONL file is missing.
        ValueError: if any JSONL line fails to parse.
    """
    base = Path(path) if path is not None else _default_index_dir()
    missing = [name for name in _REQUIRED_FILES if not (base / name).is_file()]
    if missing:
        bullet_list = "\n".join(f"  - {name}" for name in missing)
        raise FileNotFoundError(
            f"Index files missing under {base}:\n{bullet_list}\n"
            f"Run `make refresh-kb-metadata` from the repository root to regenerate."
        )

    claims = [_claim_from_record(r) for r in _read_jsonl(base / "claims.jsonl")]
    depends_on = [_depends_on_from_record(r) for r in _read_jsonl(base / "depends-on.jsonl")]
    strengthen_by = [_strengthen_by_from_record(r) for r in _read_jsonl(base / "strengthen-by.jsonl")]
    cites = [_citation_from_record(r) for r in _read_jsonl(base / "cites.jsonl")]
    subtree_aggregates = [_subtree_from_record(r) for r in _read_jsonl(base / "subtree-aggregates.jsonl")]

    return Index(
        claims=claims,
        depends_on=depends_on,
        strengthen_by=strengthen_by,
        cites=cites,
        subtree_aggregates=subtree_aggregates,
    )


__all__ = [
    "Claim",
    "DependsOnEdge",
    "StrengthenByItem",
    "CitationEdge",
    "SubtreeAggregate",
    "Index",
    "load",
    "DEFAULT_INDEX_DIR_HINT",
]

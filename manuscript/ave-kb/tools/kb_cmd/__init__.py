"""Runtime query interface over the AVE-KB derived index (Phase 3 consumer).

The query side is intentionally decoupled from the build side
(``manuscript/ave-kb/tools/kb_index_lib.py``); this package reads the
on-disk JSONL artifacts under ``manuscript/ave-kb/.index/`` and exposes
question-shaped lookups via :class:`Index`.

Typical use::

    from kb_cmd import load
    idx = load()
    idx.depends_on("0ktpcn")
"""

from .index import (
    CitationEdge,
    Claim,
    Definition,
    DependsOnEdge,
    Index,
    StrengthenByItem,
    SubtreeAggregate,
    load,
)

__all__ = [
    "Claim",
    "CitationEdge",
    "Definition",
    "DependsOnEdge",
    "Index",
    "StrengthenByItem",
    "SubtreeAggregate",
    "load",
]

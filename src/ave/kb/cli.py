"""Thin CLI wrapper around :mod:`ave.kb.index`.

Subcommand surface mirrors ``SCHEMA.md`` §"CLI surface". Text output is one
item per line for list-returning commands; ``show`` prints a key/value block.
``--json`` emits a single JSON document (array, object, or scalar map) so the
output can be piped to ``jq``.
"""

from __future__ import annotations

import argparse
import dataclasses
import json
import sys
from pathlib import Path

from .index import CitationEdge, Claim, FrameworkNode, Index, StrengthenByItem, WeakPoint, load

# ---------------------------------------------------------------------------
# Exit codes
# ---------------------------------------------------------------------------

EXIT_OK = 0
EXIT_USER_ERROR = 1
EXIT_SYSTEM_ERROR = 2


# ---------------------------------------------------------------------------
# Argparse setup
# ---------------------------------------------------------------------------


def _add_global_flags(p: argparse.ArgumentParser) -> None:
    """Attach the global flags so they work either before or after the subcommand."""
    p.add_argument(
        "--json",
        dest="emit_json",
        action="store_true",
        help="Emit machine-readable JSON instead of human-readable text.",
    )
    p.add_argument(
        "--index-dir",
        type=Path,
        default=None,
        help="Override the default .index directory.",
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ave-kb",
        description="Query the AVE Knowledge Base derived index.",
    )
    _add_global_flags(parser)

    sub = parser.add_subparsers(dest="cmd", required=True, metavar="<command>")

    p_deps = sub.add_parser("deps", help="Forward dependencies of a claim (or inverse with -i).")
    _add_global_flags(p_deps)
    p_deps.add_argument("claim_id")
    p_deps.add_argument(
        "-i",
        "--inverse",
        action="store_true",
        help="Return ids that depend on <claim_id> rather than ids it depends on.",
    )

    p_gated = sub.add_parser("gated-on", help="Claims whose strengthen-by items mention the given claim_id.")
    _add_global_flags(p_gated)
    p_gated.add_argument("claim_id")

    p_cited = sub.add_parser("cited-by", help="Leaves citing the given claim_id.")
    _add_global_flags(p_cited)
    p_cited.add_argument("claim_id")

    p_sol = sub.add_parser("solidity-below", help="Claims with solidity strictly below threshold.")
    _add_global_flags(p_sol)
    p_sol.add_argument("threshold", type=float)

    p_sub = sub.add_parser(
        "subtree",
        help='Claim ids in the subtree under <path> ("" or "." for entry-point).',
    )
    _add_global_flags(p_sub)
    p_sub.add_argument("path")

    p_show = sub.add_parser("show", help="Full record for one node (claim, invariant, or axiom).")
    _add_global_flags(p_show)
    p_show.add_argument("claim_id")

    p_weak = sub.add_parser(
        "weak-points",
        help="Highest-leverage claim-rework targets: shaky and load-bearing claims.",
    )
    _add_global_flags(p_weak)
    p_weak.add_argument(
        "--max-solidity",
        type=float,
        default=0.65,
        help="Only claims with solidity strictly below this count as shaky (default: 0.65).",
    )
    p_weak.add_argument(
        "--min-dependents",
        type=int,
        default=1,
        help="Only claims with at least this many dependents count (default: 1).",
    )

    p_stats = sub.add_parser("stats", help="Counts summary.")
    _add_global_flags(p_stats)

    return parser


# ---------------------------------------------------------------------------
# Serialization helpers
# ---------------------------------------------------------------------------


def _claim_to_dict(c: Claim) -> dict:
    return dataclasses.asdict(c)


def _citation_to_dict(e: CitationEdge) -> dict:
    return dataclasses.asdict(e)


def _weak_point_to_dict(wp: WeakPoint) -> dict:
    c = wp.claim
    return {
        "id": c.id,
        "solidity": c.solidity,
        "build_band": c.build_band,
        "dependents": wp.dependents,
        "title": c.title,
    }


def _strengthen_to_dict(it: StrengthenByItem) -> dict:
    d = dataclasses.asdict(it)
    # mentioned_ids is a tuple in the dataclass; asdict yields a tuple,
    # which JSON serializes as a list, but be explicit for clarity.
    d["mentioned_ids"] = list(it.mentioned_ids)
    return d


def _format_show_text(node: Claim | FrameworkNode) -> str:
    if isinstance(node, FrameworkNode):
        fields: list[tuple[str, object]] = [
            ("node_type", node.node_type),
            ("id", node.id),
            ("title", node.title),
            ("canonical_path", node.canonical_path),
            ("canonical_anchor", node.canonical_anchor),
        ]
    else:
        fields = [
            ("node_type", node.node_type),
            ("id", node.id),
            ("title", node.title),
            ("canonical_path", node.canonical_path),
            ("canonical_anchor", node.canonical_anchor),
            ("confidence", node.confidence),
            ("solidity", node.solidity),
            ("build_status", node.build_status),
            ("build_band", node.build_band),
            ("rationale", node.rationale),
            ("depends_on_count", node.depends_on_count),
            ("strengthen_by_count", node.strengthen_by_count),
            ("citation_count", node.citation_count),
        ]
    return "\n".join(f"{k}: {'' if v is None else v}" for k, v in fields)


# ---------------------------------------------------------------------------
# Command dispatch
# ---------------------------------------------------------------------------


def _print_lines(lines: list[str], out) -> None:
    for line in lines:
        print(line, file=out)


def _emit(value, *, emit_json: bool, out) -> None:
    if emit_json:
        print(json.dumps(value, ensure_ascii=False), file=out)


def _dispatch(args: argparse.Namespace, idx: Index, out, err) -> int:
    cmd = args.cmd
    emit_json = args.emit_json

    if cmd == "deps":
        results = idx.dependents_of(args.claim_id) if args.inverse else idx.depends_on(args.claim_id)
        if emit_json:
            _emit(results, emit_json=True, out=out)
        else:
            _print_lines(results, out)
        return EXIT_OK

    if cmd == "gated-on":
        results = idx.gated_on(args.claim_id)
        if emit_json:
            _emit(results, emit_json=True, out=out)
        else:
            _print_lines(results, out)
        return EXIT_OK

    if cmd == "cited-by":
        edges = idx.cited_by(args.claim_id)
        if emit_json:
            _emit([_citation_to_dict(e) for e in edges], emit_json=True, out=out)
        else:
            _print_lines([e.leaf_path for e in edges], out)
        return EXIT_OK

    if cmd == "solidity-below":
        claims = idx.solidity_below(args.threshold)
        if emit_json:
            _emit([_claim_to_dict(c) for c in claims], emit_json=True, out=out)
        else:
            _print_lines([f"{c.id}\t{c.solidity}\t{c.title}" for c in claims], out)
        return EXIT_OK

    if cmd == "subtree":
        results = idx.subtree_claims(args.path)
        if emit_json:
            _emit(results, emit_json=True, out=out)
        else:
            _print_lines(results, out)
        return EXIT_OK

    if cmd == "show":
        node = idx.node(args.claim_id)
        if node is None:
            print(f"error: unknown node id: {args.claim_id}", file=err)
            return EXIT_USER_ERROR
        if emit_json:
            _emit(dataclasses.asdict(node), emit_json=True, out=out)
        else:
            print(_format_show_text(node), file=out)
        return EXIT_OK

    if cmd == "weak-points":
        weak = idx.weak_points(max_solidity=args.max_solidity, min_dependents=args.min_dependents)
        if emit_json:
            _emit([_weak_point_to_dict(wp) for wp in weak], emit_json=True, out=out)
        else:
            print(
                f"# weak points\tmax-solidity<{args.max_solidity}\tmin-dependents>={args.min_dependents}",
                file=out,
            )
            _print_lines(
                [f"{wp.claim.id}\t{wp.claim.solidity}\t{wp.dependents}\t{wp.claim.title}" for wp in weak],
                out,
            )
            print(f"# ({idx.pending_count} claims pending, excluded)", file=out)
        return EXIT_OK

    if cmd == "stats":
        s = idx.stats
        if emit_json:
            _emit(s, emit_json=True, out=out)
        else:
            for key in (
                "claims",
                "invariants",
                "axioms",
                "depends_on_edges",
                "strengthen_by_items",
                "citation_edges",
                "subtree_aggregates",
            ):
                print(f"{key}: {s[key]}", file=out)
        return EXIT_OK

    # argparse with required=True should never let us reach here.
    print(f"error: unknown command: {cmd}", file=err)
    return EXIT_USER_ERROR


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    try:
        idx = load(args.index_dir)
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return EXIT_SYSTEM_ERROR
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return EXIT_SYSTEM_ERROR

    return _dispatch(args, idx, out=sys.stdout, err=sys.stderr)


if __name__ == "__main__":
    sys.exit(main())

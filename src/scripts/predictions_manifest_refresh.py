#!/usr/bin/env python3
"""
Predictions Manifest Refresh — regenerate derived fields in
manuscript/predictions.yaml.

Currently regenerates one derived field:

  axioms_used  — for every BRIDGED entry (one with a `clm:` into the claim
                 DAG), the axiom basis is the sorted transitive `depends_on`
                 axiom cone of that claim (see
                 predictions_manifest_validator.derive_axioms_used). The shared
                 derivation function is the single source of truth; the
                 validator's `check_axioms` gate drift-checks against the same
                 function (no dual-compute). Unbridged entries (P10/P41/P47 etc.)
                 have no DAG cone, so their hand-authored axioms_used is left
                 untouched.

This is the write-side counterpart to predictions_manifest_validator.py
(read-only verify), mirroring the KB's refresh-kb-metadata / verify-kb-metadata
split. It edits the YAML surgically (line-level), NOT via a yaml round-trip, so
the manifest's hand-authored notes/comments/formatting are preserved.

Usage:
  python src/scripts/predictions_manifest_refresh.py            # write in place
  python src/scripts/predictions_manifest_refresh.py --dry-run  # show diff only
"""
import argparse
import re
import sys

import yaml

from scripts.predictions_manifest_validator import (
    MANIFEST_PATH,
    collect_dependency_edges,
    derive_axioms_used,
)

# A manifest entry boundary: `  - id: <token>` at list-item indent.
_ID_LINE_RE = re.compile(r"^  - id: (\S+)\s*$")
# The `axioms_used:` line within an entry (4-space field indent).
_AXIOMS_LINE_RE = re.compile(r"^    axioms_used:\s*(.*)$")
# Where to insert a missing axioms_used line: after the entry's `clm:` line.
_CLM_LINE_RE = re.compile(r"^    clm:\s*\S+\s*$")


def _fmt_axioms(axioms: list[int]) -> str:
    return "[" + ", ".join(str(a) for a in axioms) + "]"


def refresh(dry_run: bool = False) -> int:
    """Rewrite axioms_used for bridged entries. Returns the number of entries
    whose axioms_used changed (or would change, in dry-run)."""
    adjacency = collect_dependency_edges()
    if not adjacency:
        print(
            "[refresh] KB depends-on index empty/missing — run `make refresh-kb-metadata` first.",
            file=sys.stderr,
        )
        return -1

    # Map id -> derived axioms (only for bridged entries).
    manifest = yaml.safe_load(MANIFEST_PATH.read_text(encoding="utf-8"))
    derived: dict[str, list[int]] = {}
    for entry in manifest.get("predictions", []):
        clm = entry.get("clm")
        if clm:
            derived[entry["id"]] = derive_axioms_used(clm, adjacency)

    lines = MANIFEST_PATH.read_text(encoding="utf-8").split("\n")
    out: list[str] = []
    changes: list[tuple[str, object, list[int]]] = []
    cur_id: str | None = None
    cur_target: list[int] | None = None
    cur_has_axioms = False
    cur_clm_idx: int | None = None  # index in `out` of this entry's clm line

    def _flush_missing_axioms() -> None:
        # If the just-finished entry was bridged but had no axioms_used line,
        # insert one right after its clm: line.
        nonlocal cur_clm_idx, cur_target
        if cur_target is not None and not cur_has_axioms and cur_clm_idx is not None:
            out.insert(cur_clm_idx + 1, f"    axioms_used: {_fmt_axioms(cur_target)}")

    for line in lines:
        m_id = _ID_LINE_RE.match(line)
        if m_id:
            _flush_missing_axioms()
            cur_id = m_id.group(1)
            cur_target = derived.get(cur_id)  # None if unbridged
            cur_has_axioms = False
            cur_clm_idx = None
            out.append(line)
            continue

        if cur_id is not None and _CLM_LINE_RE.match(line):
            out.append(line)
            cur_clm_idx = len(out) - 1
            continue

        m_ax = _AXIOMS_LINE_RE.match(line)
        if m_ax and cur_id is not None and cur_target is not None:
            cur_has_axioms = True
            try:
                stored = yaml.safe_load(m_ax.group(1))
            except yaml.YAMLError:
                stored = None
            stored_sorted = sorted(stored) if isinstance(stored, list) else stored
            if stored_sorted != cur_target:
                changes.append((cur_id, stored, cur_target))
            out.append(f"    axioms_used: {_fmt_axioms(cur_target)}")
            continue

        out.append(line)
    _flush_missing_axioms()

    for pid, old, new in changes:
        print(f"  {pid}: {old} -> {new}")
    if dry_run:
        print(f"[refresh] DRY-RUN: {len(changes)} bridged entries would change axioms_used.")
        return len(changes)

    MANIFEST_PATH.write_text("\n".join(out), encoding="utf-8")
    print(f"[refresh] wrote axioms_used for bridged entries; {len(changes)} changed.")
    return len(changes)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Refresh derived fields in predictions.yaml (axioms_used).")
    parser.add_argument("--dry-run", action="store_true", help="Show what would change; do not write.")
    args = parser.parse_args(argv)
    rc = refresh(dry_run=args.dry_run)
    return 2 if rc < 0 else 0


if __name__ == "__main__":
    sys.exit(main())

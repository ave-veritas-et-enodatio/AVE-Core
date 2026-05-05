#!/usr/bin/env python3
"""Mechanical integrity check for the AVE knowledge-base claim-quality framework.

Enforces INVARIANT-S5, INVARIANT-S7, and INVARIANT-S8 from
``manuscript/ave-kb/CLAUDE.md``. Six checks, all hard fail-loud:

    1. Tier 1 coverage: every leaf has a Tier 1 line, OR is in the
       documented NO_CLAIM allowlist below.
    2. Tier 2 coverage: every multi-claim leaf has proximal markers
       for each ID in its Tier 1 list.
    3. ID uniqueness: no canonical ``<!-- id: xxxxxx -->`` appears twice.
    4. Orphan refs: every Tier 1 ID resolves to a canonical entry.
    5. Index subtree-ID line: every ``index.md`` carries a subtree
       line, except leaf-as-index documents (line 2 = leaf marker).
    6. Subtree consistency: each index's declared subtree-ID list
       equals the union of Tier 1 IDs from leaves below it.

A seventh diagnostic (warning, not failure) reports canonical entries
with no back-linking leaf — entries that exist in a claim-quality.md
but no leaf cites their ID via Tier 1. That's a hygiene signal, not
a structural defect.

Run from the repository root::

    ./.venv/bin/python manuscript/ave-kb/tools/check-claim-quality.py

Or via the build system::

    make verify
"""

from __future__ import annotations

import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

KB = Path("manuscript/ave-kb")

# Documented no-claim leaves. Each entry MUST have a one-line reason.
# Add to this allowlist when promoting a leaf to no-claim status; remove
# when a previously-no-claim leaf gains substantive content.
NO_CLAIM: dict[str, str] = {
    # vol1
    "vol1/axioms-and-lattice/ch1-fundamental-axioms/lattice-structure.md":
        "pure forward-reference to kirchhoff-network-method.md",
    # vol2 — translation-table forwarders (8 leaves)
    "vol2/appendices/app-a-translation-matrix/translation-circuit.md":
        "routing forwarder to common/translation-tables/",
    "vol2/appendices/app-a-translation-matrix/translation-condensed-matter.md":
        "routing forwarder to common/translation-tables/",
    "vol2/appendices/app-a-translation-matrix/translation-cosmology.md":
        "routing forwarder to common/translation-tables/",
    "vol2/appendices/app-a-translation-matrix/translation-gravity.md":
        "routing forwarder to common/translation-tables/",
    "vol2/appendices/app-a-translation-matrix/translation-particle-physics.md":
        "routing forwarder to common/translation-tables/",
    "vol2/appendices/app-a-translation-matrix/translation-protein-solver.md":
        "routing forwarder to common/translation-tables/",
    "vol2/appendices/app-a-translation-matrix/translation-protein.md":
        "routing forwarder to common/translation-tables/",
    "vol2/appendices/app-a-translation-matrix/translation-qm.md":
        "routing forwarder to common/translation-tables/",
    # vol2 — other no-claim
    "vol2/nuclear-field/ch12-millennium-prizes/knot-vs-orbital-table-ch12.md":
        "placeholder/routing — content lives in sibling millennium-prize leaves",
    "vol2/particle-physics/ch03-neutrino-sector/neutrino-translation-table.md":
        "routing forwarder to common/translation-tables/",
    "vol2/particle-physics/ch06-electroweak-higgs/sm-ave-translation.md":
        "routing forwarder to common/translation-tables/",
    "vol2/proofs-computation/ch09-computational-proof/anomaly-catalog.md":
        "research agenda / future work — no falsifiable claim asserted",
    "vol2/proofs-computation/ch11-overdrive/axiom-survey.md":
        "placeholder/routing index over ch11 overdrive content",
    # vol3 — aggregators and routing
    "vol3/condensed-matter/ch09-condensed-matter-superconductivity/cm-ave-translation.md":
        "routing forwarder to common/translation-tables/",
    "vol3/condensed-matter/ch09-condensed-matter-superconductivity/remaining-ch09-results.md":
        "aggregator/forward-reference to sibling resultboxes",
    "vol3/condensed-matter/ch11-thermodynamics/ch11-remaining-resultboxes.md":
        "aggregator/forward-reference to sibling resultboxes",
    "vol3/cosmology/ch04-generative-cosmology/remaining-ch04-results.md":
        "aggregator/forward-reference to sibling resultboxes",
    "vol3/cosmology/ch15-black-hole-orbitals/remaining-ch15-results.md":
        "aggregator/forward-reference to sibling resultboxes",
    "vol3/gravity/ch01-gravity-yield/remaining-ch01-results.md":
        "aggregator/forward-reference to sibling resultboxes",
    "vol3/gravity/ch02-general-relativity/gr-ave-translation-dictionary.md":
        "routing/dispatcher to GR↔AVE translation content",
    # vol5
    "vol5/molecular-foundations/organic-circuitry/r-group-filter-stack.md":
        "notational framework / pure structural definition",
    # vol6 — figure-only and code listings
    "vol6/appendix/heavy-element-catalog/selected-heavy-circuit-models.md":
        "figure captions only — circuit diagram visualisations",
    "vol6/appendix/heavy-element-catalog/selected-heavy-strain-fields.md":
        "figure captions only — strain-field visualisations",
    "vol6/framework/computational-mass-defect/python-simulator.md":
        "code listing / methodology pointer — no standalone claim",
}

ID_PATTERN = re.compile(r"\b([a-z0-9]{6})\b")
CQ_BLOCK = re.compile(r"<!--\s*claim-quality:\s*(.*?)\s*-->", re.DOTALL)
CANONICAL_ID = re.compile(r"<!-- id: ([a-z0-9]{6}) -->")
SUBTREE_LINE = re.compile(r"<!--\s*claim-quality \(subtree\):\s*([^>]*?)\s*-->")


def find_leaves() -> list[tuple[Path, list[str]]]:
    """Return ``[(path, tier1_ids)]`` for every leaf in the KB."""
    leaves: list[tuple[Path, list[str]]] = []
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
            leaves.append((p, ids))
    return leaves


def collect_canonical_ids() -> list[tuple[str, str]]:
    """Return ``[(id, claim-quality.md path)]`` for every canonical entry."""
    out: list[tuple[str, str]] = []
    for p in KB.rglob("claim-quality.md"):
        for m in CANONICAL_ID.findall(p.read_text()):
            out.append((m, str(p.relative_to(KB))))
    return out


def check_tier1_coverage(
    leaves: list[tuple[Path, list[str]]],
) -> list[str]:
    failures = []
    for p, ids in leaves:
        rel = str(p.relative_to(KB))
        if not ids and rel not in NO_CLAIM:
            failures.append(rel)
    return failures


def check_tier2_coverage(
    leaves: list[tuple[Path, list[str]]],
) -> list[tuple[str, list[str], list[str]]]:
    failures = []
    for p, ids in leaves:
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
    leaves: list[tuple[Path, list[str]]],
    canonical_set: set[str],
) -> dict[str, list[str]]:
    orphans: dict[str, list[str]] = defaultdict(list)
    for p, ids in leaves:
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
    leaves: list[tuple[Path, list[str]]],
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
            continue  # caught by check_index_subtree_lines
        declared = set(ID_PATTERN.findall(m.group(1)))

        idx_dir = idx.parent
        expected: set[str] = set()
        for leaf, ids in leaves:
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
    leaves: list[tuple[Path, list[str]]],
) -> list[tuple[str, str]]:
    """Diagnostic (warning): canonical entries that no leaf cites via Tier 1."""
    cited: set[str] = set()
    for _, ids in leaves:
        cited.update(ids)
    return [(cid, path) for cid, path in canonical if cid not in cited]


def main() -> int:
    if not KB.is_dir():
        print(f"[claim-quality] FAIL — {KB} not found. Run from repository root.", file=sys.stderr)
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
    }
    warnings = {
        "uncited_entries": check_uncited_entries(canonical, leaves),
    }

    # Stale NO_CLAIM entries — leaves that were marked no-claim but no longer exist
    leaf_paths = {str(p.relative_to(KB)) for p, _ in leaves}
    stale_no_claim = sorted(p for p in NO_CLAIM if p not in leaf_paths)

    n_with_t1 = sum(1 for _, ids in leaves if ids)
    n_multi = sum(1 for _, ids in leaves if len(ids) >= 2)
    print(
        f"[claim-quality] Scanned {len(leaves)} leaves "
        f"({n_with_t1} with Tier 1, {len(NO_CLAIM)} documented no-claim, "
        f"{n_multi} multi-claim) and {len(canonical)} canonical entries."
    )

    has_failures = False

    if failures["tier1_coverage"]:
        has_failures = True
        print(f"\n[FAIL] {len(failures['tier1_coverage'])} leaves missing Tier 1 annotation:")
        for p in failures["tier1_coverage"]:
            print(f"  {p}")
        print(
            "  → Add a Tier 1 line, OR add the file to NO_CLAIM in this script "
            "with a one-line reason."
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
            print(f"  {cid} (cited by {len(leaves_citing)} leaf{'s' if len(leaves_citing) != 1 else ''})")
            for path in leaves_citing[:3]:
                print(f"    {path}")
            if len(leaves_citing) > 3:
                print(f"    ... and {len(leaves_citing) - 3} more")

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

    if stale_no_claim:
        has_failures = True
        print(
            f"\n[FAIL] {len(stale_no_claim)} stale NO_CLAIM entries point to "
            f"non-existent leaves:"
        )
        for p in stale_no_claim:
            print(f"  {p}")
        print("  → Remove these from NO_CLAIM in this script.")

    if warnings["uncited_entries"]:
        print(
            f"\n[WARN] {len(warnings['uncited_entries'])} canonical entries are "
            f"not back-linked by any leaf Tier 1:"
        )
        for cid, path in warnings["uncited_entries"]:
            print(f"  {cid} (in {path})")
        print(
            "  → Either back-link them from the relevant leaves, or remove the "
            "canonical entry. (Warning only; does not fail the check.)"
        )

    if has_failures:
        print("\n[claim-quality] FAIL — fix the above and re-run.")
        return 1

    print("[claim-quality] PASS.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Unit tests for ``kb_index_lib`` against a synthetic fixture KB.

Run from the repo root (``manuscript`` path is hyphenated, so the dotted
module form needs ``manuscript/ave-kb/tools`` on ``sys.path`` rather than
``manuscript.ave-kb.tools.tests``)::

    cd /Users/benn/projects/AVE-Umbrella/AVE-Core/manuscript/ave-kb/tools
    python -m unittest tests.test_kb_index_lib

Or, equivalently from the repo root::

    PYTHONPATH=manuscript/ave-kb/tools python -m unittest tests.test_kb_index_lib

Tests are fully independent of live KB state. Every test runs against the
small, stable hand-built fixture under ``tests/fixtures/mini-kb/`` (its claim
graph is known exactly, so expected values are derivable from the fixture) or
against inline synthetic data. The live KB's own structural health is covered
by ``make verify-kb-metadata``; nothing in this module reads or asserts on
``manuscript/ave-kb/`` proper. All tests are read-only and never mutate any
file in the fixture or the live KB.
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

# Make the tools dir importable regardless of how the test is invoked.
_THIS_DIR = Path(__file__).resolve().parent
_TOOLS_DIR = _THIS_DIR.parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

import kb_index_lib as lib  # noqa: E402

# The synthetic fixture KB — the stable graph behavioral tests run against.
# Lives entirely under ``tests/fixtures/mini-kb/``; this module never touches
# the live ``manuscript/ave-kb/`` tree.
_FIXTURE = _THIS_DIR / "fixtures" / "mini-kb"


class TestParseFrontmatter(unittest.TestCase):
    """parse_frontmatter scalar / list / boolean handling."""

    def test_missing_block_returns_none(self):
        self.assertIsNone(lib.parse_frontmatter("# Title\n\nNo frontmatter here."))

    def test_kind_leaf_field(self):
        text = "<!-- kb-frontmatter\nkind: leaf\n-->\n"
        fm = lib.parse_frontmatter(text)
        self.assertEqual(fm, {"kind": "leaf"})

    def test_claims_list(self):
        text = "<!-- kb-frontmatter\nkind: leaf\nclaims: [clm-aaa111, clm-bbb222, clm-ccc333]\n-->\n"
        fm = lib.parse_frontmatter(text)
        self.assertEqual(fm["kind"], "leaf")
        self.assertEqual(fm["claims"], ["clm-aaa111", "clm-bbb222", "clm-ccc333"])

    def test_no_claim_string(self):
        text = "<!-- kb-frontmatter\nkind: leaf\nno-claim: navigation only\n-->\n"
        fm = lib.parse_frontmatter(text)
        self.assertEqual(fm["no-claim"], "navigation only")

    def test_subtree_claims_list(self):
        text = "<!-- kb-frontmatter\nkind: index\nsubtree-claims: [clm-abc123, clm-def456]\n-->\n"
        fm = lib.parse_frontmatter(text)
        self.assertEqual(fm["subtree-claims"], ["clm-abc123", "clm-def456"])

    def test_path_stable_quoted_string(self):
        text = '<!-- kb-frontmatter\nkind: leaf\npath-stable: "ref label"\n-->\n'
        fm = lib.parse_frontmatter(text)
        self.assertEqual(fm["path-stable"], "ref label")

    def test_bootstrap_boolean_true(self):
        text = "<!-- kb-frontmatter\nkind: index\nbootstrap: true\n-->\n"
        fm = lib.parse_frontmatter(text)
        self.assertIs(fm["bootstrap"], True)


class TestParseClaimQualityFile(unittest.TestCase):
    """parse_claim_quality_file against the fixture's root claim-quality.md.

    The root register holds five claims: two no-dependency claims
    (clm-aa1111, clm-bb2222), a single-claim-dependency claim (clm-cc3333),
    a multi-dependency claim (clm-dd4444), and a framework-only-dependency
    claim (clm-ee5555).
    """

    @classmethod
    def setUpClass(cls):
        cls.path = _FIXTURE / "claim-quality.md"
        cls.entries = lib.parse_claim_quality_file(cls.path, _FIXTURE)
        cls.by_id = {e.id: e for e in cls.entries}

    def test_entry_count(self):
        # Five real claims; the fenced `<!-- id: -->` example is not counted.
        self.assertEqual(len(self.entries), 5)

    def test_no_dependency_claim_metadata(self):
        e = self.by_id["clm-aa1111"]
        self.assertIn("Foundation Claim A", e.title)
        self.assertEqual(e.confidence, 0.90)
        # The on-disk solidity line is deliberately stale (0.10); the parsed
        # entry carries exactly what the line says — it is not recomputed.
        self.assertEqual(e.solidity, 0.10)
        self.assertIsNotNone(e.build_status)
        # No depends-on bullets → no edges.
        self.assertEqual(e.depends_on, ())

    def test_claim_dependency_edge_carries_recorded_solidity(self):
        e = self.by_id["clm-cc3333"]
        targets = {edge.target: edge for edge in e.depends_on}
        self.assertIn("clm-aa1111", targets)
        edge = targets["clm-aa1111"]
        self.assertEqual(edge.source, "clm-cc3333")
        self.assertEqual(edge.target_kind, "claim")
        self.assertEqual(edge.target_solidity_recorded, 0.90)

    def test_strengthen_by_item_mentions_two_fixture_ids(self):
        # clm-dd4444's first strengthen-by item names both clm-aa1111 and
        # clm-bb2222 in its text.
        e = self.by_id["clm-dd4444"]
        joint = [
            sb
            for sb in e.strengthen_by
            if "clm-aa1111" in sb.mentioned_ids and "clm-bb2222" in sb.mentioned_ids
        ]
        self.assertTrue(
            joint,
            "expected at least one strengthen-by item mentioning both ids",
        )

    def test_framework_dependency_claim_edges(self):
        # clm-ee5555 depends on a framework invariant and a framework axiom;
        # neither carries a recorded solidity.
        e = self.by_id["clm-ee5555"]
        kinds = sorted(edge.target_kind for edge in e.depends_on)
        self.assertEqual(kinds, ["axiom", "invariant"])
        for edge in e.depends_on:
            self.assertIsNone(edge.target_solidity_recorded)


class TestParseFrameworkNodes(unittest.TestCase):
    """parse_framework_nodes against the fixture's CLAUDE.md.

    The fixture declares four invariant headings (INVARIANT-S1, S2, S3, and
    the subsumed-tombstone S6) and four axiom bullets in the INVARIANT-S2
    section.
    """

    @classmethod
    def setUpClass(cls):
        cls.nodes = lib.parse_framework_nodes(_FIXTURE)
        cls.by_id = {n.id: n for n in cls.nodes}

    def test_invariant_count(self):
        invariants = [n for n in self.nodes if n.node_type == "invariant"]
        self.assertEqual(len(invariants), 4)

    def test_axiom_count(self):
        axioms = [n for n in self.nodes if n.node_type == "axiom"]
        self.assertEqual(len(axioms), 4)
        self.assertEqual(
            sorted(a.id for a in axioms),
            ["axiom-1", "axiom-2", "axiom-3", "axiom-4"],
        )

    def test_tombstone_invariant_present(self):
        # The subsumed S6 heading is still a real heading; a reference must
        # resolve, so the node must exist.
        self.assertIn("INVARIANT-S6", self.by_id)
        self.assertEqual(self.by_id["INVARIANT-S6"].node_type, "invariant")

    def test_invariant_anchor_is_own_heading_slug(self):
        s2 = self.by_id["INVARIANT-S2"]
        self.assertEqual(s2.canonical_path, "CLAUDE.md")
        self.assertEqual(s2.canonical_anchor, "invariant-s2-ave-axiom-numbering")
        self.assertEqual(s2.title, "AVE Axiom numbering")

    def test_axioms_share_the_s2_anchor(self):
        # All four axioms point at the INVARIANT-S2 heading slug.
        s2_anchor = self.by_id["INVARIANT-S2"].canonical_anchor
        for num in (1, 2, 3, 4):
            self.assertEqual(
                self.by_id[f"axiom-{num}"].canonical_anchor, s2_anchor
            )
            self.assertEqual(self.by_id[f"axiom-{num}"].canonical_path, "CLAUDE.md")


class TestDependsOnFrameworkEdges(unittest.TestCase):
    """Head-extraction depends-on parser: framework targets and multi-token.

    Edge-count and shape assertions run against the fixture's known graph:
    9 ``relation:"depends"`` edges total — 5 claim-target, 4 framework-target.
    (4 claim-target + 4 framework-target are sourced by claims; the 5th
    claim-target depends edge is the support sup-dep001's OWN dependency on
    clm-aa1111. The fixture also carries ``strengthens`` edges from experiments
    and ``supports`` edges from support nodes; both are scoped out of these
    depends-edge counts.)
    """

    @classmethod
    def setUpClass(cls):
        cls.state = lib.discover_kb(_FIXTURE, diagnostic_stream=None)
        cls.records = lib.build_depends_on_records(cls.state)
        cls.depends = [
            r for r in cls.records if r["relation"] == "depends"
        ]

    def test_total_edge_count(self):
        self.assertEqual(len(self.depends), 9)

    def test_claim_edge_count(self):
        claim_edges = [r for r in self.depends if r["target_kind"] == "claim"]
        self.assertEqual(len(claim_edges), 5)

    def test_framework_edge_count(self):
        fw = [r for r in self.depends if r["target_kind"] != "claim"]
        self.assertEqual(len(fw), 4)

    def test_target_kind_matches_target_shape(self):
        for r in self.records:
            kind = r["target_kind"]
            target = r["target"]
            if kind == "claim":
                self.assertTrue(target.startswith("clm-"))
            elif kind == "invariant":
                self.assertTrue(target.startswith("INVARIANT-"))
            elif kind == "axiom":
                self.assertTrue(target.startswith("axiom-"))
            else:
                self.fail(f"unexpected target_kind {kind!r}")

    def test_framework_targets_have_null_solidity(self):
        for r in self.records:
            if r["target_kind"] != "claim":
                self.assertIsNone(r["target_solidity_recorded"])

    def test_double_invariant_s2_edges_from_one_owner(self):
        # clm-hh8888 declares INVARIANT-S2 via two separate bullets with
        # different context — both edge records must survive.
        s2_edges = [
            r
            for r in self.records
            if r["target"] == "INVARIANT-S2" and r["source"] == "clm-hh8888"
        ]
        self.assertEqual(len(s2_edges), 2)
        contexts = sorted(r["context"] or "" for r in s2_edges)
        self.assertEqual(len(set(contexts)), 2, "expected two distinct contexts")

    def test_sorted_by_source_target_context(self):
        keys = [
            (r["source"], r["target"], r["context"] or "") for r in self.records
        ]
        self.assertEqual(keys, sorted(keys))

    def test_non_token_none_line_yields_zero_edges(self):
        # `- none entry-local — Axiom 4 is framework input...` — the head is
        # `none entry-local` (truncated at the em-dash), no recognized token.
        line = (
            "  - none entry-local — Axiom 4 is framework input; the "
            "case identification is structural"
        )
        edges = lib._parse_depends_on_line(line, "clm-test01")
        self.assertEqual(edges, [])

    def test_multi_token_bullet_yields_one_edge_per_token(self):
        line = "  - INVARIANT-S2 / Axiom 4 (saturation kernel — for the sketch)"
        edges = lib._parse_depends_on_line(line, "clm-test01")
        kinds = sorted(e.target_kind for e in edges)
        self.assertEqual(kinds, ["axiom", "invariant"])
        for e in edges:
            self.assertEqual(e.context, "saturation kernel — for the sketch")

    def test_plain_claim_bullet_yields_one_claim_edge(self):
        line = "  - clm-unk0bd — Some Title (solidity 0.4)"
        edges = lib._parse_depends_on_line(line, "clm-test01")
        self.assertEqual(len(edges), 1)
        self.assertEqual(edges[0].target, "clm-unk0bd")
        self.assertEqual(edges[0].target_kind, "claim")
        self.assertEqual(edges[0].target_solidity_recorded, 0.4)


class TestParseLeaf(unittest.TestCase):
    """parse_leaf against the fixture's leaves."""

    def test_multi_claim_leaf(self):
        path = _FIXTURE / "common" / "leaf-multi.md"
        leaf = lib.parse_leaf(path, _FIXTURE)
        self.assertIsNotNone(leaf)
        self.assertEqual(leaf.kind, "leaf")
        self.assertEqual(
            set(leaf.claims),
            {"clm-aa1111", "clm-bb2222", "clm-cc3333", "clm-dd4444"},
        )
        # A multi-claim leaf carries a Tier-2 marker for every id.
        self.assertEqual(set(leaf.tier2_marked), set(leaf.claims))

    def test_single_claim_leaf_may_have_empty_tier2(self):
        path = _FIXTURE / "common" / "leaf-single.md"
        leaf = lib.parse_leaf(path, _FIXTURE)
        self.assertIsNotNone(leaf)
        self.assertEqual(leaf.claims, ("clm-aa1111",))
        # The fixture's single-claim leaf carries no inline marker — Tier-2
        # is not required for single-claim leaves.
        self.assertEqual(leaf.tier2_marked, frozenset())

    def test_no_claim_leaf(self):
        path = _FIXTURE / "common" / "leaf-noclaim.md"
        leaf = lib.parse_leaf(path, _FIXTURE)
        self.assertIsNotNone(leaf)
        self.assertEqual(leaf.claims, ())
        self.assertIsNotNone(leaf.no_claim_reason)


class TestDiscoverKb(unittest.TestCase):
    """discover_kb against the synthetic fixture."""

    @classmethod
    def setUpClass(cls):
        cls.state = lib.discover_kb(_FIXTURE, diagnostic_stream=None)

    def test_claim_count_matches_canonical_extraction(self):
        # The fixture's root claim-quality.md carries one placeholder
        # `<!-- id: clm-xxxxxx -->` inside a fenced ``markdown`` code block in
        # the Quality Convention example. The library strips code fences
        # before extracting canonical IDs, so that example is NOT counted.
        # Five real entries in the root register + eleven in common/ = 16
        # (common/ adds clm-co1111, the co-hosted claim+experiment leaf, plus
        # the seven support-beneficiary claims clm-sb1111..clm-sb7777). Support
        # entries (sup-*) are NOT claims and are not counted here.
        self.assertEqual(len(self.state.claim_entries), 16)

    def test_support_node_count(self):
        # Six support nodes (INVARIANT-S10): sup-free01 (free-standing),
        # sup-dep001 (own deps), sup-pend01 (pending quality), sup-coh001
        # (co-hosted with a claim on one leaf), plus sup-mlt001 + sup-mlt002 —
        # TWO supports hosted on ONE container (multi-sup; no one-per-leaf cap).
        self.assertEqual(len(self.state.supports), 6)

    def test_multi_sup_container_hosts_two_supports(self):
        # A single container (leaf-multi-sup.md) originates BOTH sup-mlt001 and
        # sup-mlt002 — N sup node-bodies on one leaf (INVARIANT-S10 container
        # model). Both share the leaf's canonical home.
        by_id = {s.id: s for s in self.state.supports}
        self.assertIn("sup-mlt001", by_id)
        self.assertIn("sup-mlt002", by_id)
        self.assertEqual(
            by_id["sup-mlt001"].canonical_path, "common/leaf-multi-sup.md"
        )
        self.assertEqual(
            by_id["sup-mlt002"].canonical_path, "common/leaf-multi-sup.md"
        )
        # sup-mlt002's second beneficiary edge carries the pending sentinel.
        by_claim = dict(by_id["sup-mlt002"].supports)
        self.assertIs(by_claim["clm-sb6666"], lib.PENDING_FRACTION)
        self.assertEqual(by_claim["clm-sb7777"], 0.50)

    def test_every_leaf_with_claims_present(self):
        # Build the set of leaf paths from a parallel walk and intersect.
        from kb_index_lib import _kb_files  # local import to use private walker

        expected: set[str] = set()
        for p in _kb_files(_FIXTURE):
            leaf = lib.parse_leaf(p, _FIXTURE)
            if leaf is not None and leaf.claims:
                expected.add(leaf.path)
        actual = {leaf.path for leaf in self.state.leaves if leaf.claims}
        self.assertEqual(actual, expected)

    def test_indexes_count_positive(self):
        self.assertGreater(len(self.state.indexes), 0)
        # And both an entry-point and an index are discovered.
        kinds = {idx.kind for idx in self.state.indexes}
        self.assertIn("entry-point", kinds)
        self.assertIn("index", kinds)


class TestBuildClaimsRecords(unittest.TestCase):
    """build_claims_records: length, ordering, key order, derived fields."""

    @classmethod
    def setUpClass(cls):
        cls.state = lib.discover_kb(_FIXTURE, diagnostic_stream=None)
        cls.records = lib.build_claims_records(cls.state)
        cls.by_id = {r["id"]: r for r in cls.records}

    def test_length_is_union_of_all_node_types(self):
        # claims.jsonl is a type-tagged union: claims + framework nodes +
        # experiment nodes + support nodes.
        self.assertEqual(
            len(self.records),
            len(self.state.claim_entries)
            + len(self.state.framework_nodes)
            + len(self.state.experiments)
            + len(self.state.supports),
        )

    def test_node_type_distribution(self):
        from collections import Counter

        counts = Counter(r["node_type"] for r in self.records)
        # 16 claims + 2 experiments + 6 support + 4 invariants + 4 axioms = 32.
        self.assertEqual(counts["claim"], 16)
        self.assertEqual(counts["experiment"], 2)
        self.assertEqual(counts["support"], 6)
        self.assertEqual(counts["invariant"], 4)
        self.assertEqual(counts["axiom"], 4)
        self.assertEqual(len(self.records), 32)

    def test_support_record_documented_key_order(self):
        expected_keys = [
            "node_type",
            "id",
            "title",
            "canonical_path",
            "canonical_anchor",
            "quality",
            "solidity",
        ]
        sup_recs = [r for r in self.records if r["node_type"] == "support"]
        self.assertEqual(len(sup_recs), 6)
        for rec in sup_recs:
            self.assertEqual(list(rec.keys()), expected_keys)

    def test_support_sorts_last_after_invariant(self):
        # Sort key (node_type, id): support sorts AFTER invariant
        # (ASCII: axiom < claim < experiment < invariant < support).
        order = [r["node_type"] for r in self.records]
        last_invariant = max(i for i, t in enumerate(order) if t == "invariant")
        first_support = min(i for i, t in enumerate(order) if t == "support")
        self.assertLess(last_invariant, first_support)

    def test_sorted_by_node_type_then_id(self):
        keys = [(r["node_type"], r["id"]) for r in self.records]
        self.assertEqual(keys, sorted(keys))

    def test_claim_record_documented_key_order(self):
        expected_keys = [
            "node_type",
            "id",
            "title",
            "canonical_path",
            "canonical_anchor",
            "confidence",
            "derivation_solidity",
            "experimental_solidity",
            "solidity",
            "build_status",
            "build_band",
            "rationale",
            "depends_on_count",
            "strengthen_by_count",
            "citation_count",
        ]
        claim_recs = [r for r in self.records if r["node_type"] == "claim"]
        self.assertEqual(len(claim_recs), 16)
        for rec in claim_recs:
            self.assertEqual(list(rec.keys()), expected_keys)

    def test_framework_record_has_exactly_five_fields(self):
        expected_keys = [
            "node_type",
            "id",
            "title",
            "canonical_path",
            "canonical_anchor",
        ]
        fw_recs = [
            r
            for r in self.records
            if r["node_type"] in ("invariant", "axiom")
        ]
        self.assertEqual(len(fw_recs), 8)
        for rec in fw_recs:
            self.assertEqual(list(rec.keys()), expected_keys)
            self.assertEqual(rec["canonical_path"], "CLAUDE.md")

    def test_build_band_derived(self):
        # clm-aa1111 computed solidity 0.90 -> ok-to-build.
        self.assertEqual(self.by_id["clm-aa1111"]["build_band"], "ok-to-build")
        # clm-bb2222 solidity 0.60 -> input-only.
        self.assertEqual(self.by_id["clm-bb2222"]["build_band"], "input-only")
        # clm-cc3333 solidity 0.80 -> ok-with-caveats.
        self.assertEqual(self.by_id["clm-cc3333"]["build_band"], "ok-with-caveats")

    def test_solidity_field_is_computed_not_parsed(self):
        # claims.jsonl solidity must match compute_solidity, NOT the value
        # parsed off the claim-quality.md solidity line. clm-aa1111's on-disk
        # line is the stale 0.10; its record must carry the computed 0.90.
        sol = lib.compute_solidity(
            self.state.claim_entries, self.state.experiments
        )
        for cid in ("clm-aa1111", "clm-cc3333", "clm-dd4444", "clm-ee5555"):
            self.assertEqual(self.by_id[cid]["solidity"], sol[cid])
        self.assertEqual(self.by_id["clm-aa1111"]["solidity"], 0.90)
        # clm-dd4444 is a multi-dep entry: min(0.90,0.90,0.60)=0.60, build-status follows.
        self.assertEqual(self.by_id["clm-dd4444"]["solidity"], 0.60)
        self.assertEqual(
            self.by_id["clm-dd4444"]["build_status"],
            "use as input only, don't build deeper",
        )

    def test_pending_confidence_claim_has_null_derived_fields(self):
        # clm-ff6666 confidence is *pending* → solidity uncomputable → null.
        rec = self.by_id["clm-ff6666"]
        self.assertIsNone(rec["confidence"])
        self.assertIsNone(rec["solidity"])
        self.assertIsNone(rec["build_status"])

    def test_experiment_rescued_claim_has_experimental_solidity(self):
        # clm-gg7777 has a pending derivation (dependency clm-ff6666 pending),
        # but a `run` experiment (exp-bench1) strengthens it at 0.80 → its
        # experimental branch is the only non-null branch, so final solidity
        # is RESCUED to 0.80 (the max-branch).
        rec = self.by_id["clm-gg7777"]
        self.assertEqual(rec["confidence"], 0.95)
        self.assertIsNone(rec["derivation_solidity"])
        self.assertEqual(rec["experimental_solidity"], 0.80)
        self.assertEqual(rec["solidity"], 0.80)
        self.assertEqual(rec["build_status"], "ok to build on, see caveats")

    def test_counts_are_accurate(self):
        # clm-cc3333 depends on clm-aa1111 (1 edge).
        self.assertEqual(self.by_id["clm-cc3333"]["depends_on_count"], 1)
        # clm-dd4444 has 2 strengthen-by items.
        self.assertEqual(self.by_id["clm-dd4444"]["strengthen_by_count"], 2)
        # clm-aa1111 is cited by the multi-claim and single-claim leaves.
        self.assertEqual(self.by_id["clm-aa1111"]["citation_count"], 2)


class TestBuildDependsOnRecords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state = lib.discover_kb(_FIXTURE, diagnostic_stream=None)
        cls.records = lib.build_depends_on_records(cls.state)

    def test_claim_edge_records_recorded_solidity(self):
        edges = [
            r
            for r in self.records
            if r["source"] == "clm-cc3333" and r["target"] == "clm-aa1111"
        ]
        self.assertEqual(len(edges), 1)
        self.assertEqual(edges[0]["target_solidity_recorded"], 0.90)

    def test_sorted_by_source_then_target(self):
        keys = [(r["source"], r["target"]) for r in self.records]
        self.assertEqual(keys, sorted(keys))

    def test_no_dependency_claim_produces_zero_edges(self):
        # clm-aa1111 has no depends-on bullets; it must produce no edges.
        from_aa = [r for r in self.records if r["source"] == "clm-aa1111"]
        self.assertEqual(from_aa, [])


class TestBuildStrengthenByRecords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state = lib.discover_kb(_FIXTURE, diagnostic_stream=None)
        cls.records = lib.build_strengthen_by_records(cls.state)

    def test_sorted_by_claim_id_then_item_idx(self):
        keys = [(r["claim_id"], r["item_idx"]) for r in self.records]
        self.assertEqual(keys, sorted(keys))

    def test_item_idx_contiguous_per_claim(self):
        by_claim: dict[str, list[int]] = {}
        for r in self.records:
            by_claim.setdefault(r["claim_id"], []).append(r["item_idx"])
        for claim_id, indices in by_claim.items():
            self.assertEqual(
                indices,
                list(range(len(indices))),
                f"{claim_id}: indices {indices} not contiguous starting from 0",
            )


class TestBuildCitesRecords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state = lib.discover_kb(_FIXTURE, diagnostic_stream=None)
        cls.records = lib.build_cites_records(cls.state)

    def test_sorted_by_claim_id_then_leaf_path(self):
        keys = [(r["claim_id"], r["leaf_path"]) for r in self.records]
        self.assertEqual(keys, sorted(keys))

    def test_total_edges_matches_leaf_claim_sum(self):
        expected = sum(len(leaf.claims) for leaf in self.state.leaves)
        self.assertEqual(len(self.records), expected)


class TestBuildSubtreeAggregateRecords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state = lib.discover_kb(_FIXTURE, diagnostic_stream=None)
        cls.records = lib.build_subtree_aggregate_records(cls.state)

    def test_one_record_per_index_or_entry_point(self):
        self.assertEqual(len(self.records), len(self.state.indexes))

    def test_subtree_claims_sorted_and_unique(self):
        for r in self.records:
            ids = r["subtree_claims"]
            self.assertEqual(ids, sorted(ids))
            self.assertEqual(len(ids), len(set(ids)))


class TestDeterminism(unittest.TestCase):
    def test_build_all_records_byte_identical(self):
        state = lib.discover_kb(_FIXTURE, diagnostic_stream=None)
        first = lib.build_all_records(state)
        second = lib.build_all_records(state)
        self.assertEqual(set(first.keys()), set(second.keys()))
        for key in first:
            rows_a = [json.dumps(r, ensure_ascii=False, sort_keys=False) for r in first[key]]
            rows_b = [json.dumps(r, ensure_ascii=False, sort_keys=False) for r in second[key]]
            self.assertEqual(rows_a, rows_b, f"non-deterministic output for {key}")


class TestJsonlIo(unittest.TestCase):
    def test_round_trip(self):
        records = [
            {"id": "abc123", "value": 1, "list": ["a", "b"]},
            {"id": "def456", "value": None, "list": []},
        ]
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "out.jsonl"
            lib.write_jsonl(p, records)
            roundtripped = lib.read_jsonl(p)
        self.assertEqual(roundtripped, records)

    def test_write_is_byte_identical_across_calls(self):
        records = [
            {"a": 1, "b": "two", "c": [1, 2, 3]},
            {"a": 4, "b": "five", "c": []},
        ]
        with tempfile.TemporaryDirectory() as tmp:
            p1 = Path(tmp) / "first.jsonl"
            p2 = Path(tmp) / "second.jsonl"
            lib.write_jsonl(p1, records)
            lib.write_jsonl(p2, records)
            self.assertEqual(p1.read_bytes(), p2.read_bytes())

    def test_empty_records_writes_empty_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "empty.jsonl"
            lib.write_jsonl(p, [])
            self.assertEqual(p.read_bytes(), b"")
            self.assertEqual(lib.read_jsonl(p), [])

    def test_malformed_jsonl_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "bad.jsonl"
            p.write_text('{"ok": 1}\nnot-json\n', encoding="utf-8")
            with self.assertRaises(ValueError):
                lib.read_jsonl(p)


def _edge(source, target, kind="claim", recorded=None):
    """Build a depends DependsOnEdge for synthetic-graph tests."""
    return lib.DependsOnEdge(
        source=source,
        target=target,
        relation="depends",
        target_kind=kind,
        target_solidity_recorded=recorded,
        strength=None,
        context=None,
    )


def _claim(cid, confidence, depends_on=()):
    """Build a minimal ClaimEntry for synthetic compute_solidity tests."""
    return lib.ClaimEntry(
        id=cid,
        title=cid,
        canonical_path="test/claim-quality.md",
        canonical_anchor=cid,
        confidence=confidence,
        solidity=None,
        build_status=None,
        rationale="",
        depends_on=tuple(depends_on),
        strengthen_by=(),
    )


class TestRoundHalfUp(unittest.TestCase):
    """round_half_up_2dp rounds AWAY from zero at the 0.005 boundary."""

    def test_boundary_rounds_up(self):
        # Banker's rounding (Python round()) would give 0.12 for 0.125.
        self.assertEqual(lib.round_half_up_2dp(0.125), 0.13)
        self.assertEqual(lib.round_half_up_2dp(0.005), 0.01)
        self.assertEqual(lib.round_half_up_2dp(0.015), 0.02)

    def test_below_boundary_rounds_down(self):
        self.assertEqual(lib.round_half_up_2dp(0.1249), 0.12)
        self.assertEqual(lib.round_half_up_2dp(0.324), 0.32)

    def test_lv3uw1_boundary_case(self):
        # 0.65 × 0.50 = 0.325 → round-half-up → 0.33.
        self.assertEqual(lib.round_half_up_2dp(0.65 * 0.50), 0.33)


class TestBuildStatusPhrase(unittest.TestCase):
    """build_status_phrase maps solidity bands to legend phrases."""

    def test_band_boundaries(self):
        self.assertEqual(lib.build_status_phrase(1.00), "ok to build on")
        self.assertEqual(lib.build_status_phrase(0.85), "ok to build on")
        self.assertEqual(
            lib.build_status_phrase(0.84), "ok to build on, see caveats"
        )
        self.assertEqual(
            lib.build_status_phrase(0.65), "ok to build on, see caveats"
        )
        self.assertEqual(
            lib.build_status_phrase(0.45),
            "use as input only, don't build deeper",
        )
        self.assertEqual(
            lib.build_status_phrase(0.20), "do not build on, rework needed"
        )
        self.assertEqual(
            lib.build_status_phrase(0.19), "refuted, do not use"
        )
        self.assertEqual(lib.build_status_phrase(0.0), "refuted, do not use")

    def test_none_returns_none(self):
        self.assertIsNone(lib.build_status_phrase(None))


class TestComputeSolidity(unittest.TestCase):
    """compute_solidity over synthetic graphs: the core derivation."""

    def test_no_dependencies_equals_confidence(self):
        sol = lib.compute_solidity([_claim("clm-aaaaaa", 0.85)])
        self.assertEqual(sol["clm-aaaaaa"], 0.85)

    def test_clean_two_link_chain_is_weakest_link_not_product(self):
        # THE distinguishing case for the min model: a clean 2-link chain
        # q=0.9 → dep=0.9 yields 0.9 (the weakest link), NOT 0.81 (the product).
        # Under multiplication this clean derivation would decay purely because
        # it has one extra link; min keeps it at its honest floor.
        a = _claim("clm-aaaaaa", 0.90)
        b = _claim("clm-bbbbbb", 0.90, [_edge("clm-bbbbbb", "clm-aaaaaa")])
        sol = lib.compute_solidity([a, b])
        self.assertEqual(sol["clm-bbbbbb"], 0.90)

    def test_solidity_is_refactor_invariant_under_node_splitting(self):
        # Granularity invariance: splitting one derivation step into two
        # same-quality steps must NOT change the endpoint's solidity. A single
        # 0.90 leaf and a 3-node chain of identical 0.90 confidences both end at
        # 0.90 under min; under a product they would diverge (0.90 vs 0.729),
        # which is the bookkeeping artifact this model eliminates.
        single = lib.compute_solidity([_claim("clm-solo01", 0.90)])

        n1 = _claim("clm-chain1", 0.90)
        n2 = _claim("clm-chain2", 0.90, [_edge("clm-chain2", "clm-chain1")])
        n3 = _claim("clm-chain3", 0.90, [_edge("clm-chain3", "clm-chain2")])
        chained = lib.compute_solidity([n1, n2, n3])

        self.assertEqual(single["clm-solo01"], 0.90)
        self.assertEqual(chained["clm-chain3"], single["clm-solo01"])
        # Every node along the clean chain holds the same value — no decay.
        self.assertEqual(chained["clm-chain1"], 0.90)
        self.assertEqual(chained["clm-chain2"], 0.90)

    def test_single_claim_dependency(self):
        a = _claim("clm-aaaaaa", 0.75)
        b = _claim("clm-bbbbbb", 0.55, [_edge("clm-bbbbbb", "clm-aaaaaa")])
        sol = lib.compute_solidity([a, b])
        self.assertEqual(sol["clm-aaaaaa"], 0.75)
        # min(0.55, 0.75) = 0.55 — weakest link is b's own confidence.
        self.assertEqual(sol["clm-bbbbbb"], 0.55)

    def test_framework_dependency_contributes_one(self):
        # An entry depending only on framework nodes → solidity == confidence.
        e = _claim(
            "clm-aaaaaa",
            0.90,
            [
                _edge("clm-aaaaaa", "INVARIANT-S2", kind="invariant"),
                _edge("clm-aaaaaa", "axiom-4", kind="axiom"),
            ],
        )
        sol = lib.compute_solidity([e])
        self.assertEqual(sol["clm-aaaaaa"], 0.90)

    def test_min_over_multiple_dependencies(self):
        a = _claim("clm-aaaaaa", 0.41)  # leaf, solidity 0.41
        b = _claim("clm-bbbbbb", 0.28)  # leaf, solidity 0.28
        c = _claim(
            "clm-cccccc",
            0.85,
            [_edge("clm-cccccc", "clm-aaaaaa"), _edge("clm-cccccc", "clm-bbbbbb")],
        )
        sol = lib.compute_solidity([a, b, c])
        # min(0.85, 0.41, 0.28) = 0.28 — weakest link in the cone.
        self.assertEqual(sol["clm-cccccc"], 0.28)

    def test_framework_and_claim_dependency_mixed(self):
        a = _claim("clm-aaaaaa", 0.50)
        b = _claim(
            "clm-bbbbbb",
            0.80,
            [
                _edge("clm-bbbbbb", "clm-aaaaaa"),
                _edge("clm-bbbbbb", "INVARIANT-S2", kind="invariant"),
            ],
        )
        sol = lib.compute_solidity([a, b])
        # min(0.80 [local], 0.50 [claim dep], 1.0 [framework]) = 0.50
        self.assertEqual(sol["clm-bbbbbb"], 0.50)

    def test_propagation_uses_dependency_final(self):
        # Each claim's final feeds its dependents: the weakest link propagates
        # down the chain. a: 0.40 → leaf. b: min(0.90, 0.40) = 0.40. c depends
        # on b: min(0.95, 0.40) = 0.40 — the chain is gated by the weakest node,
        # not decayed by repeated multiplication.
        a = _claim("clm-aaaaaa", 0.40)
        b = _claim("clm-bbbbbb", 0.90, [_edge("clm-bbbbbb", "clm-aaaaaa")])
        c = _claim("clm-cccccc", 0.95, [_edge("clm-cccccc", "clm-bbbbbb")])
        sol = lib.compute_solidity([a, b, c])
        self.assertEqual(sol["clm-bbbbbb"], 0.40)
        self.assertEqual(sol["clm-cccccc"], 0.40)

    def test_pending_confidence_omitted(self):
        # An entry with confidence None is uncomputable — omitted from output.
        a = _claim("clm-aaaaaa", None)
        b = _claim("clm-bbbbbb", 0.85)
        sol = lib.compute_solidity([a, b])
        self.assertNotIn("clm-aaaaaa", sol)
        self.assertIn("clm-bbbbbb", sol)

    def test_entry_depending_on_pending_claim_omitted(self):
        # A numeric entry whose dependency is pending cannot be scored.
        a = _claim("clm-aaaaaa", None)
        b = _claim("clm-bbbbbb", 0.85, [_edge("clm-bbbbbb", "clm-aaaaaa")])
        sol = lib.compute_solidity([a, b])
        self.assertNotIn("clm-bbbbbb", sol)

    def test_cycle_raises(self):
        a = _claim("clm-aaaaaa", 0.80, [_edge("clm-aaaaaa", "clm-bbbbbb")])
        b = _claim("clm-bbbbbb", 0.80, [_edge("clm-bbbbbb", "clm-aaaaaa")])
        with self.assertRaises(lib.SolidityCycleError) as ctx:
            lib.compute_solidity([a, b])
        self.assertEqual(
            set(ctx.exception.cycle_members), {"clm-aaaaaa", "clm-bbbbbb"}
        )

    def test_self_loop_raises(self):
        a = _claim("clm-aaaaaa", 0.80, [_edge("clm-aaaaaa", "clm-aaaaaa")])
        with self.assertRaises(lib.SolidityCycleError):
            lib.compute_solidity([a])


class TestSolidityPendingPropagation(unittest.TestCase):
    """The hard rule: ``*pending*`` propagates transitively, like NaN.

    A claim's solidity is ``*pending*`` (omitted from ``compute_solidity``'s
    result) if its confidence is ``*pending*`` OR any dependency's solidity is
    ``*pending*`` — regardless of its own local confidence. Framework-node
    dependencies are never pending.
    """

    def test_direct_dependency_on_pending_claim_is_pending(self):
        # A (numeric) depends directly on P (pending) → A is pending.
        p = _claim("clm-pppppp", None)
        a = _claim("clm-aaaaaa", 0.85, [_edge("clm-aaaaaa", "clm-pppppp")])
        sol = lib.compute_solidity([p, a])
        self.assertNotIn("clm-pppppp", sol)
        self.assertNotIn("clm-aaaaaa", sol)

    def test_transitive_propagation_through_numeric_chain(self):
        # A (numeric) → B (numeric) → P (pending). Both A and B are pending:
        # pending-ness propagates the full length of the dependency chain.
        p = _claim("clm-pppppp", None)
        b = _claim("clm-bbbbbb", 0.90, [_edge("clm-bbbbbb", "clm-pppppp")])
        a = _claim("clm-aaaaaa", 0.90, [_edge("clm-aaaaaa", "clm-bbbbbb")])
        sol = lib.compute_solidity([p, b, a])
        self.assertNotIn("clm-bbbbbb", sol)
        self.assertNotIn("clm-aaaaaa", sol)

    def test_pending_regardless_of_local_confidence(self):
        # confidence 1.0 does NOT rescue a claim that depends on a pending
        # one — "regardless of local confidence" is load-bearing.
        p = _claim("clm-pppppp", None)
        a = _claim("clm-aaaaaa", 1.0, [_edge("clm-aaaaaa", "clm-pppppp")])
        sol = lib.compute_solidity([p, a])
        self.assertNotIn("clm-aaaaaa", sol)

    def test_framework_only_dependency_is_not_pending(self):
        # Framework nodes (invariant / axiom) are solidity-1.0 bedrock, never
        # pending → a claim depending only on them is NOT pending.
        a = _claim(
            "clm-aaaaaa",
            0.77,
            [
                _edge("clm-aaaaaa", "INVARIANT-S2", kind="invariant"),
                _edge("clm-aaaaaa", "axiom-3", kind="axiom"),
            ],
        )
        sol = lib.compute_solidity([a])
        self.assertIn("clm-aaaaaa", sol)
        self.assertEqual(sol["clm-aaaaaa"], 0.77)  # solidity == confidence

    def test_one_pending_dep_poisons_a_numeric_dep_mix(self):
        # A claim with one numeric claim-dep AND one pending claim-dep is
        # pending — the pending dependency poisons the result.
        good = _claim("clm-gggggg", 0.60)
        pend = _claim("clm-pppppp", None)
        a = _claim(
            "clm-aaaaaa",
            0.95,
            [
                _edge("clm-aaaaaa", "clm-gggggg"),
                _edge("clm-aaaaaa", "clm-pppppp"),
            ],
        )
        sol = lib.compute_solidity([good, pend, a])
        self.assertEqual(sol["clm-gggggg"], 0.60)  # the numeric dep is fine
        self.assertNotIn("clm-aaaaaa", sol)        # but A is poisoned

    def test_numeric_sibling_of_blocked_claim_still_scored(self):
        # Pending-ness does not leak sideways: a numeric claim that does NOT
        # depend on the pending one is still scored normally.
        p = _claim("clm-pppppp", None)
        blocked = _claim(
            "clm-bbbbbb", 0.85, [_edge("clm-bbbbbb", "clm-pppppp")]
        )
        sibling = _claim("clm-ssssss", 0.70)
        sol = lib.compute_solidity([p, blocked, sibling])
        self.assertNotIn("clm-bbbbbb", sol)
        self.assertEqual(sol["clm-ssssss"], 0.70)


def _experiment(exp_id, status, strengthens):
    """Build an ExperimentNode for synthetic strengthens-graph tests."""
    return lib.ExperimentNode(
        id=exp_id,
        title=exp_id,
        canonical_path="test/exp.md",
        canonical_anchor=exp_id,
        status=status,
        strengthens=tuple(strengthens),
    )


class TestExperimentalSolidity(unittest.TestCase):
    """The max-branch: run-experiment strengthens edges rescue/lift claims.

    Covers the SCHEMA "Solidity branches (definitive rule)" max-branch and the
    INVARIANT-S9 non-transitivity rule, with no real leaves (synthetic
    in-memory KbState fragments).
    """

    def test_run_experiment_rescues_pending_derivation(self):
        # (a) clm-aaaaaa has a PENDING derivation (its claim-dep clm-pppppp is
        # confidence-pending). A run experiment strengthens it at 1.0 →
        # final = 1.0 even though derivation is pending.
        p = _claim("clm-pppppp", None)  # pending confidence
        a = _claim("clm-aaaaaa", 0.90, [_edge("clm-aaaaaa", "clm-pppppp")])
        exp = _experiment("exp-aaaaaa", "run", [("clm-aaaaaa", 1.0)])
        full = lib.compute_solidity_full([p, a], [exp])
        ra = full["clm-aaaaaa"]
        self.assertIsNone(ra.derivation)       # derivation pending (dep pending)
        self.assertEqual(ra.experimental, 1.0)
        self.assertEqual(ra.final, 1.0)         # RESCUED
        # The wrapper surfaces the non-pending final.
        self.assertEqual(lib.compute_solidity([p, a], [exp])["clm-aaaaaa"], 1.0)

    def test_strengthens_is_non_transitive(self):
        # (b) The experiment edge targets only clm-aaaaaa; its pending upstream
        # input clm-pppppp is NOT touched and stays pending.
        p = _claim("clm-pppppp", None)
        a = _claim("clm-aaaaaa", 0.90, [_edge("clm-aaaaaa", "clm-pppppp")])
        exp = _experiment("exp-aaaaaa", "run", [("clm-aaaaaa", 1.0)])
        full = lib.compute_solidity_full([p, a], [exp])
        self.assertEqual(full["clm-pppppp"].final, None)  # upstream still pending
        self.assertNotIn("clm-pppppp", lib.compute_solidity([p, a], [exp]))

    def test_rescued_final_propagates_downstream(self):
        # (c) clm-dddddd depends on the rescued clm-aaaaaa; its min sees the
        # rescued final 1.0, so it scores normally instead of going pending.
        p = _claim("clm-pppppp", None)
        a = _claim("clm-aaaaaa", 0.90, [_edge("clm-aaaaaa", "clm-pppppp")])
        d = _claim("clm-dddddd", 0.80, [_edge("clm-dddddd", "clm-aaaaaa")])
        exp = _experiment("exp-aaaaaa", "run", [("clm-aaaaaa", 1.0)])
        full = lib.compute_solidity_full([p, a, d], [exp])
        self.assertEqual(full["clm-aaaaaa"].final, 1.0)
        # 0.80 × min(1.0) = 0.80 — downstream benefits from the rescue.
        self.assertEqual(full["clm-dddddd"].derivation, 0.80)
        self.assertEqual(full["clm-dddddd"].final, 0.80)

    def test_unrun_experiment_contributes_nothing(self):
        # (d) An UNRUN (pending) experiment strengthens clm-aaaaaa, but its
        # derivation is pending (dep pending) → no rescue → claim stays pending.
        p = _claim("clm-pppppp", None)
        a = _claim("clm-aaaaaa", 0.90, [_edge("clm-aaaaaa", "clm-pppppp")])
        exp = _experiment("exp-aaaaaa", "pending", [("clm-aaaaaa", 1.0)])
        full = lib.compute_solidity_full([p, a], [exp])
        ra = full["clm-aaaaaa"]
        self.assertIsNone(ra.derivation)
        self.assertIsNone(ra.experimental)  # unrun → excluded from the max
        self.assertIsNone(ra.final)         # still pending
        self.assertNotIn("clm-aaaaaa", lib.compute_solidity([p, a], [exp]))

    def test_experimental_is_max_over_run_edges(self):
        # Multiple run experiments → experimental_solidity is the MAX strength.
        a = _claim("clm-aaaaaa", None)  # pending derivation
        e1 = _experiment("exp-aaaaaa", "run", [("clm-aaaaaa", 0.6)])
        e2 = _experiment("exp-bbbbbb", "run", [("clm-aaaaaa", 0.9)])
        full = lib.compute_solidity_full([a], [e1, e2])
        self.assertEqual(full["clm-aaaaaa"].experimental, 0.9)

    def test_final_is_max_of_derivation_and_experimental(self):
        # A claim with a strong derivation and a weaker experiment keeps the
        # higher derivation; the experiment never floors it down.
        a = _claim("clm-aaaaaa", 0.95)  # derivation 0.95, no deps
        exp = _experiment("exp-aaaaaa", "run", [("clm-aaaaaa", 0.40)])
        full = lib.compute_solidity_full([a], [exp])
        self.assertEqual(full["clm-aaaaaa"].derivation, 0.95)
        self.assertEqual(full["clm-aaaaaa"].experimental, 0.40)
        self.assertEqual(full["clm-aaaaaa"].final, 0.95)  # max keeps derivation

    def test_zero_experiments_final_equals_derivation(self):
        # The HARD-GATE invariant: with no experiments, final == derivation and
        # experimental is None for every claim.
        a = _claim("clm-aaaaaa", 0.75)
        b = _claim("clm-bbbbbb", 0.55, [_edge("clm-bbbbbb", "clm-aaaaaa")])
        full = lib.compute_solidity_full([a, b], [])
        for cid in ("clm-aaaaaa", "clm-bbbbbb"):
            self.assertIsNone(full[cid].experimental)
            self.assertEqual(full[cid].final, full[cid].derivation)


def _support(sup_id, quality, supports, depends_on=()):
    """Build a SupportNode for synthetic support-graph tests."""
    return lib.SupportNode(
        id=sup_id,
        title=sup_id,
        canonical_path="test/sup.md",
        canonical_anchor=sup_id,
        quality=quality,
        depends_on=tuple(depends_on),
        supports=tuple(supports),
    )


class TestSupportSolidity(unittest.TestCase):
    """INVARIANT-S10: support nodes lift the DERIVATION branch, dep-gated.

    Synthetic in-memory KbState fragments — no real leaves. Covers sup_solidity
    derivation, the local_quality lift, on-point fractions, pending no-poison,
    multi-beneficiary fan-out, and dep-gating.
    """

    def test_free_standing_support_solidity_equals_quality(self):
        # A free-standing support (no deps) has sup_solidity == quality.
        s = _support("sup-aaaaaa", 0.90, [("clm-aaaaaa", 1.0)])
        a = _claim("clm-aaaaaa", 0.40)
        sup = lib.compute_support_solidity([a], (), [s])
        self.assertEqual(sup["sup-aaaaaa"], 0.90)

    def test_free_standing_support_lifts_beneficiary(self):
        # (a) A free-standing evaluated support lifts a beneficiary's solidity:
        # local_quality = max(0.40, 0.90×1.0) = 0.90, no deps to gate → 0.90.
        s = _support("sup-aaaaaa", 0.90, [("clm-aaaaaa", 1.0)])
        a = _claim("clm-aaaaaa", 0.40)
        full = lib.compute_solidity_full([a], (), [s])
        self.assertEqual(full["clm-aaaaaa"].derivation, 0.90)
        self.assertEqual(full["clm-aaaaaa"].final, 0.90)

    def test_support_with_own_deps_is_dep_gated(self):
        # (b) A support with its own depends-on is dep-gated below its quality:
        # sup_solidity = round2(min(0.90, dep final 0.50)) = 0.50 (weakest link).
        dep = _claim("clm-dddddd", 0.50)
        s = _support(
            "sup-aaaaaa", 0.90, [("clm-aaaaaa", 1.0)],
            depends_on=[_edge("sup-aaaaaa", "clm-dddddd")],
        )
        a = _claim("clm-aaaaaa", 0.20)
        full = lib.compute_solidity_full([dep, a], (), [s])
        self.assertEqual(full.sup_solidity["sup-aaaaaa"], 0.50)
        # The lift into clm-aaaaaa is the dep-gated 0.50, not the raw 0.90.
        self.assertEqual(full["clm-aaaaaa"].derivation, 0.50)

    def test_pending_support_contributes_nothing_and_no_poison(self):
        # (c) A pending-quality support contributes nothing to the max AND does
        # not poison a beneficiary with otherwise-valid quality.
        s = _support("sup-aaaaaa", None, [("clm-aaaaaa", 1.0)])
        a = _claim("clm-aaaaaa", 0.55)
        full = lib.compute_solidity_full([a], (), [s])
        self.assertIsNone(full.sup_solidity["sup-aaaaaa"])  # pending
        self.assertEqual(full["clm-aaaaaa"].derivation, 0.55)  # not lifted
        self.assertEqual(full["clm-aaaaaa"].final, 0.55)       # not poisoned

    def test_pending_support_does_not_poison_pending_beneficiary_dep(self):
        # Poison flows ONLY from a claim's own load-bearing depends-on, never
        # from an inbound supports edge: a pending support over a claim that
        # ALSO depends on a numeric claim leaves the claim scorable.
        good = _claim("clm-gggggg", 0.80)
        s = _support("sup-aaaaaa", None, [("clm-aaaaaa", 1.0)])
        a = _claim("clm-aaaaaa", 0.50, [_edge("clm-aaaaaa", "clm-gggggg")])
        full = lib.compute_solidity_full([good, a], (), [s])
        # min(0.50, 0.80) = 0.50; the pending support is simply ignored.
        self.assertEqual(full["clm-aaaaaa"].derivation, 0.50)

    def test_pending_fraction_contributes_nothing_and_no_poison(self):
        # An EVALUATED support whose on-point fraction is *pending* contributes
        # nothing to the beneficiary's local_quality max (excluded, exactly like
        # a pending sup_solidity) and never poisons an otherwise-valid claim.
        s = _support(
            "sup-aaaaaa", 0.90, [("clm-aaaaaa", lib.PENDING_FRACTION)]
        )
        a = _claim("clm-aaaaaa", 0.55)
        full = lib.compute_solidity_full([a], (), [s])
        self.assertEqual(full.sup_solidity["sup-aaaaaa"], 0.90)  # support scored
        self.assertEqual(full["clm-aaaaaa"].derivation, 0.55)    # not lifted
        self.assertEqual(full["clm-aaaaaa"].final, 0.55)         # not poisoned

    def test_pending_fraction_excluded_but_sibling_numeric_lift_applies(self):
        # One support fans out to two claims: a *pending* fraction to one, a
        # numeric fraction to the other. The pending edge is excluded; the
        # numeric edge still lifts its beneficiary.
        s = _support(
            "sup-aaaaaa", 0.90,
            [("clm-aaaaaa", lib.PENDING_FRACTION), ("clm-bbbbbb", 0.50)],
        )
        a = _claim("clm-aaaaaa", 0.20)
        b = _claim("clm-bbbbbb", 0.20)
        full = lib.compute_solidity_full([a, b], (), [s])
        self.assertEqual(full["clm-aaaaaa"].derivation, 0.20)  # pending f, no lift
        self.assertEqual(full["clm-bbbbbb"].derivation, 0.45)  # 0.90×0.50

    def test_pending_fraction_materializes_as_literal_distinct_from_null(self):
        # On disk a pending supports-fraction is the literal "*pending*", DISTINCT
        # from a depends edge's null fraction (the sentinel-distinctness contract).
        dep = _claim("clm-dddddd", 0.50)
        s = _support(
            "sup-aaaaaa", 0.90, [("clm-aaaaaa", lib.PENDING_FRACTION)],
            depends_on=[_edge("sup-aaaaaa", "clm-dddddd")],
        )
        a = _claim("clm-aaaaaa", 0.20)
        state = lib.KbState(
            claim_entries=(dep, a), leaves=(), indexes=(),
            framework_nodes=(), experiments=(), supports=(s,),
        )
        edges = lib.build_depends_on_records(state)
        supports = [e for e in edges if e["relation"] == "supports"]
        depends = [
            e for e in edges
            if e["relation"] == "depends" and e["source"] == "sup-aaaaaa"
        ]
        self.assertEqual(supports[0]["fraction"], lib.PENDING_LITERAL)
        self.assertIsNone(depends[0]["fraction"])
        # And the serialized line distinguishes them: "*pending*" vs null.
        blob = lib.serialize_records(edges).decode("utf-8")
        self.assertIn('"fraction": "*pending*"', blob)
        self.assertIn('"fraction": null', blob)

    def test_fraction_below_one_reduces_contribution(self):
        # (d) An on-point fraction < 1.0 reduces the lift vs f=1.0.
        s = _support("sup-aaaaaa", 0.90, [("clm-aaaaaa", 0.50)])
        a = _claim("clm-aaaaaa", 0.20)
        full = lib.compute_solidity_full([a], (), [s])
        # local_quality = max(0.20, 0.90×0.50=0.45) = 0.45.
        self.assertEqual(full["clm-aaaaaa"].derivation, 0.45)

    def test_multi_beneficiary_support(self):
        # (e) One support → two claims at different fractions.
        s = _support(
            "sup-aaaaaa", 0.90, [("clm-aaaaaa", 1.0), ("clm-bbbbbb", 0.50)]
        )
        a = _claim("clm-aaaaaa", 0.20)
        b = _claim("clm-bbbbbb", 0.20)
        full = lib.compute_solidity_full([a, b], (), [s])
        self.assertEqual(full["clm-aaaaaa"].derivation, 0.90)
        self.assertEqual(full["clm-bbbbbb"].derivation, 0.45)

    def test_support_lift_is_dep_gated_on_beneficiary_deps(self):
        # The support lift is throttled by the BENEFICIARY's own deps — it does
        # NOT bypass them the way an experiment's max-branch does.
        dep = _claim("clm-dddddd", 0.50)
        s = _support("sup-aaaaaa", 0.90, [("clm-aaaaaa", 1.0)])
        a = _claim("clm-aaaaaa", 0.20, [_edge("clm-aaaaaa", "clm-dddddd")])
        full = lib.compute_solidity_full([dep, a], (), [s])
        # local_quality 0.90, but min(0.90, dep 0.50) = 0.50 — dep-gated.
        self.assertEqual(full["clm-aaaaaa"].derivation, 0.50)

    def test_support_lift_never_floors_a_higher_confidence(self):
        # A support weaker than the claim's own confidence does not lower it.
        s = _support("sup-aaaaaa", 0.30, [("clm-aaaaaa", 1.0)])
        a = _claim("clm-aaaaaa", 0.80)
        full = lib.compute_solidity_full([a], (), [s])
        self.assertEqual(full["clm-aaaaaa"].derivation, 0.80)  # max keeps 0.80

    def test_support_lift_is_derivation_branch_not_experimental(self):
        # A support feeds derivation, never the experimental/max branch.
        s = _support("sup-aaaaaa", 0.90, [("clm-aaaaaa", 1.0)])
        a = _claim("clm-aaaaaa", 0.40)
        full = lib.compute_solidity_full([a], (), [s])
        self.assertIsNone(full["clm-aaaaaa"].experimental)
        self.assertEqual(full["clm-aaaaaa"].derivation, 0.90)

    def test_support_cycle_raises(self):
        # A support depending on a claim that the support also supports would
        # cycle; the unified topo detects it.
        s = _support(
            "sup-aaaaaa", 0.90, [("clm-aaaaaa", 1.0)],
            depends_on=[_edge("sup-aaaaaa", "clm-aaaaaa")],
        )
        a = _claim("clm-aaaaaa", 0.40)
        with self.assertRaises(lib.SolidityCycleError):
            lib.compute_solidity_full([a], (), [s])


class TestSupportPendingFractionParse(unittest.TestCase):
    """parse_support_leaf accepts a *pending* on-point fraction (INVARIANT-S10).

    A ``supports`` pair may carry the literal ``*pending*`` (intended-but-
    unassessed) — stored as the PENDING_FRACTION sentinel, distinct from a
    depends edge's null. Numeric fractions must still validate to (0, 1].
    """

    _LEAF = (
        "[↑ Parent](index.md)\n\n"
        "<!-- kb-frontmatter\n"
        "kind: leaf\n"
        "no-claim: \"hosts a support node only\"\n"
        "sup-id: sup-aaaaaa\n"
        "supports:\n"
        "  - clm-aaaaaa: *pending*\n"
        "  - clm-bbbbbb: 0.50\n"
        "-->\n\n"
        "## Pending-Fraction Support\n"
    )

    def _parse(self, text):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            leaf = root / "leaf.md"
            leaf.write_text(text)
            return lib.parse_support_leaf(leaf, root)

    def test_pending_fraction_parses_as_sentinel(self):
        sups = self._parse(self._LEAF)
        self.assertEqual(len(sups), 1)
        sup = sups[0]
        self.assertEqual(sup.id, "sup-aaaaaa")
        by_claim = dict(sup.supports)
        self.assertIs(by_claim["clm-aaaaaa"], lib.PENDING_FRACTION)
        self.assertEqual(by_claim["clm-bbbbbb"], 0.50)

    def test_pending_sentinel_is_distinct_from_none(self):
        # The pending sentinel must NOT be None (which a depends edge uses).
        self.assertIsNotNone(lib.PENDING_FRACTION)
        self.assertIsNot(lib.PENDING_FRACTION, None)

    def test_zero_fraction_still_rejected(self):
        bad = self._LEAF.replace("clm-bbbbbb: 0.50", "clm-bbbbbb: 0")
        with self.assertRaises(lib.SupportLeafError):
            self._parse(bad)

    def test_above_one_fraction_still_rejected(self):
        bad = self._LEAF.replace("clm-bbbbbb: 0.50", "clm-bbbbbb: 1.5")
        with self.assertRaises(lib.SupportLeafError):
            self._parse(bad)


class TestSupportFixture(unittest.TestCase):
    """Support nodes against the fixture graph — the committed answer key.

    * sup-free01 (free-standing, q 0.90)  → sup_solidity 0.90
    * sup-dep001 (q 0.90, dep clm-aa1111 0.90) → min(0.90, 0.90) = 0.90 (dep-gated)
    * sup-pend01 (q *pending*)            → *pending* (omitted)
    * sup-coh001 (free-standing, q 0.85)  → 0.85
    Beneficiary lifts: sb1111→0.90, sb2222→0.45, sb3333→0.90, sb4444→0.55
    (not lifted), sb5555→0.85.
    """

    @classmethod
    def setUpClass(cls):
        cls.state = lib.discover_kb(_FIXTURE, diagnostic_stream=None)
        cls.sol = lib.compute_solidity(
            cls.state.claim_entries, cls.state.experiments, cls.state.supports
        )
        cls.sup = lib.compute_support_solidity(
            cls.state.claim_entries, cls.state.experiments, cls.state.supports
        )

    def test_support_solidities(self):
        self.assertEqual(self.sup["sup-free01"], 0.90)
        self.assertEqual(self.sup["sup-dep001"], 0.90)
        self.assertEqual(self.sup["sup-coh001"], 0.85)
        self.assertNotIn("sup-pend01", self.sup)  # pending → omitted
        # Both supports on the multi-sup container are free-standing.
        self.assertEqual(self.sup["sup-mlt001"], 0.80)
        self.assertEqual(self.sup["sup-mlt002"], 0.70)

    def test_beneficiary_lifts(self):
        self.assertEqual(self.sol["clm-sb1111"], 0.90)
        self.assertEqual(self.sol["clm-sb2222"], 0.45)
        self.assertEqual(self.sol["clm-sb3333"], 0.90)
        self.assertEqual(self.sol["clm-sb4444"], 0.55)  # pending sup, not lifted
        self.assertEqual(self.sol["clm-sb5555"], 0.85)
        # clm-sb6666: lifted by sup-mlt001 (0.80 × f=1.0 = 0.80); sup-mlt002's
        # pending-fraction edge to it contributes nothing.
        self.assertEqual(self.sol["clm-sb6666"], 0.80)
        # clm-sb7777: lifted by sup-mlt002 (0.70 × f=0.50 = 0.35).
        self.assertEqual(self.sol["clm-sb7777"], 0.35)

    def test_pending_support_does_not_poison_fixture_beneficiary(self):
        # clm-sb4444 has valid confidence (0.55) and a pending support; it must
        # remain scorable, never dragged to pending.
        self.assertIn("clm-sb4444", self.sol)

    def test_cohost_leaf_parses_as_both_claim_and_support(self):
        # (f) leaf-sup-cohost.md hosts BOTH a claim (clm-sb5555) and a support
        # (sup-coh001) — orthogonal node-bodies in one container.
        path = _FIXTURE / "common" / "leaf-sup-cohost.md"
        leaf = lib.parse_leaf(path, _FIXTURE)
        self.assertEqual(leaf.claims, ("clm-sb5555",))
        sups = lib.parse_support_leaf(path, _FIXTURE)
        self.assertEqual(len(sups), 1)
        sup = sups[0]
        self.assertEqual(sup.id, "sup-coh001")
        self.assertEqual(sup.supports, (("clm-sb5555", 1.0),))

    def test_support_depends_edge_emitted(self):
        # sup-dep001's OWN dependency is a depends edge sourced at the sup-id.
        edges = lib.build_depends_on_records(self.state)
        own = [
            e for e in edges
            if e["source"] == "sup-dep001" and e["relation"] == "depends"
        ]
        self.assertEqual(len(own), 1)
        self.assertEqual(own[0]["target"], "clm-aa1111")

    def test_supports_edges_carry_fraction(self):
        edges = lib.build_depends_on_records(self.state)
        supports = [e for e in edges if e["relation"] == "supports"]
        # 5 from the single-sup leaves + 3 from the multi-sup container
        # (sup-mlt001→sb6666, sup-mlt002→sb6666 *pending*, sup-mlt002→sb7777).
        self.assertEqual(len(supports), 8)
        for e in supports:
            self.assertEqual(e["target_kind"], "claim")
            self.assertIsNone(e["strength"])
            self.assertIsNotNone(e["fraction"])
        # The pending on-point fraction serializes as the literal "*pending*".
        pending = [
            e for e in supports
            if e["source"] == "sup-mlt002" and e["target"] == "clm-sb6666"
        ]
        self.assertEqual(len(pending), 1)
        self.assertEqual(pending[0]["fraction"], lib.PENDING_LITERAL)

    def test_supported_by_reverse_view(self):
        rows = lib.build_supported_by_records(self.state)
        self.assertEqual(len(rows), 8)
        by_claim = {r["claim_id"]: r for r in rows}
        self.assertEqual(by_claim["clm-sb2222"]["fraction"], 0.50)
        self.assertEqual(by_claim["clm-sb2222"]["sup_solidity"], 0.90)
        self.assertIsNone(by_claim["clm-sb4444"]["sup_solidity"])  # pending sup


class TestComputeSolidityFixture(unittest.TestCase):
    """compute_solidity and min_dependency_solidity against the fixture graph.

    The fixture's known answer key:

    * clm-aa1111 (conf 0.90, no deps)         → solidity 0.90
    * clm-bb2222 (conf 0.60, no deps)         → solidity 0.60
    * clm-cc3333 (conf 0.80, dep aa1111)      → min(0.80, 0.90) = 0.80
    * clm-dd4444 (conf 0.90, deps aa+bb)      → min(0.90, 0.90, 0.60) = 0.60
    * clm-ee5555 (conf 0.75, framework deps)  → 0.75 (framework contributes 1.0)
    * clm-hh8888 (conf 0.70, double INV-S2)   → 0.70
    """

    @classmethod
    def setUpClass(cls):
        cls.state = lib.discover_kb(_FIXTURE, diagnostic_stream=None)
        cls.sol = lib.compute_solidity(
            cls.state.claim_entries, cls.state.experiments
        )
        cls.by_id = {e.id: e for e in cls.state.claim_entries}

    def test_known_entry_solidities(self):
        self.assertEqual(self.sol["clm-aa1111"], 0.90)
        self.assertEqual(self.sol["clm-bb2222"], 0.60)
        self.assertEqual(self.sol["clm-cc3333"], 0.80)
        self.assertEqual(self.sol["clm-dd4444"], 0.60)
        self.assertEqual(self.sol["clm-ee5555"], 0.75)
        self.assertEqual(self.sol["clm-hh8888"], 0.70)
        # clm-gg7777 is rescued by run-experiment exp-bench1 → 0.80.
        self.assertEqual(self.sol["clm-gg7777"], 0.80)

    def test_no_deps_entry_solidity_equals_confidence(self):
        # clm-aa1111 has no entry-level dependencies → solidity == confidence.
        aa = self.by_id["clm-aa1111"]
        self.assertEqual(self.sol["clm-aa1111"], aa.confidence)

    def test_framework_only_entry_solidity_equals_confidence(self):
        # clm-ee5555 depends only on framework nodes → solidity == confidence.
        ee = self.by_id["clm-ee5555"]
        self.assertEqual(self.sol["clm-ee5555"], ee.confidence)

    def test_min_dependency_solidity_no_deps_is_none(self):
        aa = self.by_id["clm-aa1111"]
        self.assertIsNone(lib.min_dependency_solidity(aa, self.sol))

    def test_min_dependency_solidity_picks_minimum(self):
        # clm-dd4444 depends on clm-aa1111 (0.90) and clm-bb2222 (0.60).
        dd = self.by_id["clm-dd4444"]
        self.assertEqual(lib.min_dependency_solidity(dd, self.sol), 0.60)

    def test_min_dependency_solidity_framework_contributes_one(self):
        # clm-ee5555's deps are all framework nodes → min is 1.0.
        ee = self.by_id["clm-ee5555"]
        self.assertEqual(lib.min_dependency_solidity(ee, self.sol), 1.0)


if __name__ == "__main__":
    unittest.main()

"""Unit tests for ``kb_index_lib`` against the real KB and synthetic fixtures.

Run from the repo root (``manuscript`` path is hyphenated, so the dotted
module form needs ``manuscript/ave-kb/tools`` on ``sys.path`` rather than
``manuscript.ave-kb.tools.tests``)::

    cd /Users/benn/projects/AVE-Umbrella/AVE-Core/manuscript/ave-kb/tools
    python -m unittest tests.test_kb_index_lib

Or, equivalently from the repo root::

    PYTHONPATH=manuscript/ave-kb/tools python -m unittest tests.test_kb_index_lib

The tests load the real KB as their fixture for most cases. They are
read-only and never mutate any KB file.
"""

from __future__ import annotations

import io
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

# Repo root: tools/tests -> tools -> ave-kb -> manuscript -> repo
_REPO_ROOT = _TOOLS_DIR.parents[2]
_KB_ROOT = _REPO_ROOT / "manuscript" / "ave-kb"


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
    """parse_claim_quality_file against vol1/claim-quality.md (real KB)."""

    @classmethod
    def setUpClass(cls):
        cls.path = _KB_ROOT / "vol1" / "claim-quality.md"
        cls.entries = lib.parse_claim_quality_file(cls.path, _KB_ROOT)
        cls.by_id = {e.id: e for e in cls.entries}

    def test_count_matches_grep(self):
        self.assertEqual(len(self.entries), 32)

    def test_trf3bd_metadata(self):
        e = self.by_id["clm-trf3bd"]
        self.assertIn("Trefoil", e.title)
        self.assertEqual(e.confidence, 0.75)
        self.assertEqual(e.solidity, 0.75)
        self.assertIsNotNone(e.build_status)
        self.assertIn("ok to build on", e.build_status)
        self.assertIn("caveats", e.build_status)
        # Placeholder depends-on entry produces zero edges.
        self.assertEqual(e.depends_on, ())
        # Three strengthen-by items per the KB.
        self.assertEqual(len(e.strengthen_by), 3)

    def test_unk0bd_metadata(self):
        e = self.by_id["clm-unk0bd"]
        self.assertEqual(e.confidence, 0.40)
        self.assertEqual(e.solidity, 0.40)

    def test_5xon03_depends_on_includes_unk0bd(self):
        e = self.by_id["clm-5xon03"]
        targets = {edge.target: edge for edge in e.depends_on}
        self.assertIn("clm-unk0bd", targets)
        edge = targets["clm-unk0bd"]
        self.assertEqual(edge.source, "clm-5xon03")
        self.assertEqual(edge.target_solidity_recorded, 0.40)

    def test_5xon03_strengthen_by_mentions_trf3bd_and_unk0bd(self):
        e = self.by_id["clm-5xon03"]
        joint = [
            sb
            for sb in e.strengthen_by
            if "clm-trf3bd" in sb.mentioned_ids and "clm-unk0bd" in sb.mentioned_ids
        ]
        self.assertTrue(
            joint,
            "expected at least one strengthen-by item mentioning both ids",
        )


class TestParseFrameworkNodes(unittest.TestCase):
    """parse_framework_nodes against the real CLAUDE.md."""

    @classmethod
    def setUpClass(cls):
        cls.nodes = lib.parse_framework_nodes(_KB_ROOT)
        cls.by_id = {n.id: n for n in cls.nodes}

    def test_eighteen_invariants(self):
        invariants = [n for n in self.nodes if n.node_type == "invariant"]
        self.assertEqual(len(invariants), 18)

    def test_four_axioms(self):
        axioms = [n for n in self.nodes if n.node_type == "axiom"]
        self.assertEqual(len(axioms), 4)
        self.assertEqual(
            sorted(a.id for a in axioms),
            ["axiom-1", "axiom-2", "axiom-3", "axiom-4"],
        )

    def test_invariant_s6_tombstone_present(self):
        # The subsumed S6 heading is still a real heading; a reference must
        # resolve, so the node must exist.
        self.assertIn("INVARIANT-S6", self.by_id)

    def test_invariant_anchor_is_own_heading_slug(self):
        s2 = self.by_id["INVARIANT-S2"]
        self.assertEqual(s2.canonical_path, "CLAUDE.md")
        self.assertEqual(s2.canonical_anchor, "invariant-s2-ave-axiom-numbering")
        self.assertEqual(s2.title, "AVE Axiom numbering")

    def test_axiom_titles_and_shared_anchor(self):
        # All four axioms point at the INVARIANT-S2 heading slug.
        s2_anchor = self.by_id["INVARIANT-S2"].canonical_anchor
        self.assertEqual(self.by_id["axiom-1"].title, "Impedance")
        self.assertEqual(self.by_id["axiom-2"].title, "Fine Structure")
        self.assertEqual(self.by_id["axiom-3"].title, "Gravity")
        self.assertEqual(
            self.by_id["axiom-4"].title, "Universal Saturation Kernel"
        )
        for num in (1, 2, 3, 4):
            self.assertEqual(
                self.by_id[f"axiom-{num}"].canonical_anchor, s2_anchor
            )
            self.assertEqual(self.by_id[f"axiom-{num}"].canonical_path, "CLAUDE.md")


class TestDependsOnFrameworkEdges(unittest.TestCase):
    """Head-extraction depends-on parser: framework targets and multi-token."""

    @classmethod
    def setUpClass(cls):
        cls.state = lib.discover_kb(_KB_ROOT, diagnostic_stream=None)
        cls.records = lib.build_depends_on_records(cls.state)

    def test_total_edge_count(self):
        self.assertEqual(len(self.records), 40)

    def test_claim_edge_count_unchanged(self):
        claim_edges = [r for r in self.records if r["target_kind"] == "claim"]
        self.assertEqual(len(claim_edges), 33)

    def test_framework_edge_count(self):
        fw = [r for r in self.records if r["target_kind"] != "claim"]
        self.assertEqual(len(fw), 7)

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

    def test_double_invariant_s2_edges_from_vol2_owner(self):
        # The vol2 claim-quality entry declares INVARIANT-S2 via two separate
        # bullets with different context — both edge records must survive.
        s2_edges = [
            r
            for r in self.records
            if r["target"] == "INVARIANT-S2"
            and r["source"] == "clm-h9aqmt"
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
    """parse_leaf against real KB leaves."""

    def test_ch8_alpha_golden_torus(self):
        path = _KB_ROOT / "vol1" / "ch8-alpha-golden-torus.md"
        leaf = lib.parse_leaf(path, _KB_ROOT)
        self.assertIsNotNone(leaf)
        self.assertEqual(leaf.kind, "leaf")
        self.assertIn("clm-trf3bd", leaf.claims)
        # ch8 is a multi-claim leaf so tier2_marked should be non-empty.
        self.assertTrue(leaf.tier2_marked)

    def test_single_claim_leaf_may_have_empty_tier2(self):
        # Find any single-claim leaf in the KB.
        state = lib.discover_kb(_KB_ROOT, diagnostic_stream=None)
        singles = [leaf for leaf in state.leaves if len(leaf.claims) == 1]
        self.assertTrue(singles, "expected at least one single-claim leaf")
        # The invariant: tier2_marked may be empty for single-claim leaves.
        # Assert the leaves we find conform (presence of any marker is allowed
        # but not required).
        for leaf in singles:
            # tier2_marked subset of claims is enforced by construction in parse_leaf.
            self.assertLessEqual(set(leaf.tier2_marked), set(leaf.claims))

    def test_multi_claim_leaf_tier2_non_empty(self):
        state = lib.discover_kb(_KB_ROOT, diagnostic_stream=None)
        multis = [leaf for leaf in state.leaves if len(leaf.claims) >= 2]
        self.assertTrue(multis, "expected multi-claim leaves")
        # Verifier-enforced INVARIANT-S8: every multi-claim leaf has Tier 2 markers.
        for leaf in multis:
            self.assertTrue(
                leaf.tier2_marked,
                f"multi-claim leaf {leaf.path} missing tier2 markers",
            )


class TestDiscoverKb(unittest.TestCase):
    """discover_kb against the real KB."""

    @classmethod
    def setUpClass(cls):
        cls.state = lib.discover_kb(_KB_ROOT, diagnostic_stream=None)

    def test_claim_count_matches_canonical_extraction(self):
        # The naive ``grep -c '<!-- id: '`` count is 200, but it includes one
        # placeholder ``<!-- id: clm-xxxxxx -->`` inside a fenced ``markdown`` code
        # block in the root ``claim-quality.md`` Quality Convention example.
        # The library (like the existing check-claim-quality verifier) strips
        # code fences before extracting canonical IDs, so the real entry count
        # is 199.
        self.assertEqual(len(self.state.claim_entries), 199)

    def test_every_leaf_with_claims_present(self):
        # Build the set of leaf paths from a parallel walk and intersect.
        from kb_index_lib import _kb_files  # local import to use private walker

        expected: set[str] = set()
        for p in _kb_files(_KB_ROOT):
            leaf = lib.parse_leaf(p, _KB_ROOT)
            if leaf is not None and leaf.claims:
                expected.add(leaf.path)
        actual = {leaf.path for leaf in self.state.leaves if leaf.claims}
        self.assertEqual(actual, expected)

    def test_indexes_count_positive(self):
        self.assertGreater(len(self.state.indexes), 0)
        # And at least one entry-point.
        kinds = {idx.kind for idx in self.state.indexes}
        self.assertIn("entry-point", kinds)
        self.assertIn("index", kinds)


class TestKnownIdFiltering(unittest.TestCase):
    """Post-`clm-`-migration the ID regex is exact: a `clm-`-shaped token is
    only ever a real ID candidate, never an incidental prose word.
    """

    def test_depends_on_claim_targets_are_all_canonical(self):
        """Every ``claim``-kind depends-on target is a canonical claim ID."""
        state = lib.discover_kb(_KB_ROOT, diagnostic_stream=io.StringIO())
        canonical = {entry.id for entry in state.claim_entries}
        offenders: list[tuple[str, str]] = []
        for entry in state.claim_entries:
            for edge in entry.depends_on:
                if edge.target_kind == "claim" and edge.target not in canonical:
                    offenders.append((edge.source, edge.target))
        self.assertEqual(
            offenders,
            [],
            f"depends-on claim edges with non-claim targets: {offenders}",
        )

    def test_strengthen_by_mentioned_ids_only_real_ids(self):
        """Every strengthen-by mentioned_id is a canonical claim ID.

        Still meaningful post-migration: every extracted `clm-` token must
        resolve to a registered canonical ID; an unregistered one would
        signal a typo or stale reference.
        """
        state = lib.discover_kb(_KB_ROOT, diagnostic_stream=io.StringIO())
        canonical = {entry.id for entry in state.claim_entries}
        offenders: list[tuple[str, int, str]] = []
        for entry in state.claim_entries:
            for sb in entry.strengthen_by:
                for cid in sb.mentioned_ids:
                    if cid not in canonical:
                        offenders.append((sb.claim_id, sb.item_idx, cid))
        self.assertEqual(
            offenders,
            [],
            f"strengthen-by mentioned_ids referencing non-canonical IDs: {offenders}",
        )

    def test_diagnostic_silenceable(self):
        """Passing diagnostic_stream=None is a true no-op (no error raised).

        On a clean post-migration KB the exact ID regex has no false
        positives, so a buffered run also emits nothing — there is no
        `clm-`-shaped token outside the canonical set. The silenceability
        contract is: passing ``None`` must not raise and must yield the same
        state shape as a buffered run.
        """
        silent = lib.discover_kb(_KB_ROOT, diagnostic_stream=None)
        self.assertGreater(len(silent.claim_entries), 0)
        buf = io.StringIO()
        buffered = lib.discover_kb(_KB_ROOT, diagnostic_stream=buf)
        self.assertEqual(
            len(silent.claim_entries), len(buffered.claim_entries)
        )


class TestBuildClaimsRecords(unittest.TestCase):
    """build_claims_records: length, ordering, key order, derived fields."""

    @classmethod
    def setUpClass(cls):
        cls.state = lib.discover_kb(_KB_ROOT, diagnostic_stream=None)
        cls.records = lib.build_claims_records(cls.state)
        cls.by_id = {r["id"]: r for r in cls.records}

    def test_length_is_union_of_all_node_types(self):
        # claims.jsonl is a type-tagged union: claims + framework nodes.
        self.assertEqual(
            len(self.records),
            len(self.state.claim_entries) + len(self.state.framework_nodes),
        )

    def test_node_type_distribution(self):
        from collections import Counter

        counts = Counter(r["node_type"] for r in self.records)
        self.assertEqual(counts["claim"], 199)
        self.assertEqual(counts["invariant"], 18)
        self.assertEqual(counts["axiom"], 4)
        self.assertEqual(len(self.records), 221)

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
            "solidity",
            "build_status",
            "build_band",
            "rationale",
            "depends_on_count",
            "strengthen_by_count",
            "citation_count",
        ]
        claim_recs = [r for r in self.records if r["node_type"] == "claim"]
        self.assertEqual(len(claim_recs), 199)
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
        fw_recs = [r for r in self.records if r["node_type"] != "claim"]
        self.assertEqual(len(fw_recs), 22)
        for rec in fw_recs:
            self.assertEqual(list(rec.keys()), expected_keys)
            self.assertEqual(rec["canonical_path"], "CLAUDE.md")

    def test_build_band_derived(self):
        # clm-trf3bd has solidity 0.75 -> ok-with-caveats
        self.assertEqual(self.by_id["clm-trf3bd"]["build_band"], "ok-with-caveats")
        # clm-unk0bd has solidity 0.40 -> do-not-build
        self.assertEqual(self.by_id["clm-unk0bd"]["build_band"], "do-not-build")

    def test_counts_are_accurate(self):
        # clm-5xon03 depends on clm-unk0bd (1 edge).
        self.assertEqual(self.by_id["clm-5xon03"]["depends_on_count"], 1)
        # clm-trf3bd has 3 strengthen-by items.
        self.assertEqual(self.by_id["clm-trf3bd"]["strengthen_by_count"], 3)
        # clm-trf3bd is cited by ch8-alpha-golden-torus.md at minimum.
        self.assertGreaterEqual(self.by_id["clm-trf3bd"]["citation_count"], 1)


class TestBuildDependsOnRecords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state = lib.discover_kb(_KB_ROOT, diagnostic_stream=None)
        cls.records = lib.build_depends_on_records(cls.state)

    def test_5xon03_to_unk0bd_present(self):
        edges = [r for r in self.records if r["source"] == "clm-5xon03" and r["target"] == "clm-unk0bd"]
        self.assertEqual(len(edges), 1)
        self.assertEqual(edges[0]["target_solidity_recorded"], 0.40)

    def test_sorted_by_source_then_target(self):
        keys = [(r["source"], r["target"]) for r in self.records]
        self.assertEqual(keys, sorted(keys))

    def test_placeholder_lines_produce_zero_edges(self):
        # clm-trf3bd's depends-on is a placeholder; it must produce no edges.
        from_trf = [r for r in self.records if r["source"] == "clm-trf3bd"]
        self.assertEqual(from_trf, [])


class TestBuildStrengthenByRecords(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.state = lib.discover_kb(_KB_ROOT, diagnostic_stream=None)
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
        cls.state = lib.discover_kb(_KB_ROOT, diagnostic_stream=None)
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
        cls.state = lib.discover_kb(_KB_ROOT, diagnostic_stream=None)
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
        state = lib.discover_kb(_KB_ROOT, diagnostic_stream=None)
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


if __name__ == "__main__":
    unittest.main()

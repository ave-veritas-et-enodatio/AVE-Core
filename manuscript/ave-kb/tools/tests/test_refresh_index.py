"""Integration tests for the JSONL index emission in ``refresh-kb-metadata.py``.

Runs the refresh script as a subprocess against the real KB and verifies the
contract documented in ``manuscript/ave-kb/.index/SCHEMA.md``:

* All five JSONL files are emitted under ``.index/``.
* The script is idempotent — a second run produces byte-identical files.
* Record counts match what ``kb_index_lib`` produces in-process.
* Every emitted line is a well-formed JSON object; files end with one ``\\n``.
* Referential integrity: every claim id referenced in non-claims files
  appears as a record in ``claims.jsonl``.
* Records are sorted by the per-file sort key documented in SCHEMA.md.

Run from the repo root::

    cd /Users/benn/projects/AVE-Umbrella/AVE-Core/manuscript/ave-kb/tools
    python -m unittest tests.test_refresh_index

These tests write the real ``.index/*.jsonl`` files in place. The
``refresh-kb-metadata.py`` script is idempotent against a clean canonical
state, so this leaves the working tree in the same state it found.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

# Make the sibling tools dir importable.
_THIS_DIR = Path(__file__).resolve().parent
_TOOLS_DIR = _THIS_DIR.parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

import kb_index_lib as lib  # noqa: E402

# Repo root: tools/tests -> tools -> ave-kb -> manuscript -> repo
_REPO_ROOT = _TOOLS_DIR.parents[2]
_KB_ROOT = _REPO_ROOT / "manuscript" / "ave-kb"
_INDEX_DIR = _KB_ROOT / ".index"
_SCRIPT = _REPO_ROOT / "manuscript" / "ave-kb" / "tools" / "refresh-kb-metadata.py"

_INDEX_FILES = (
    "claims.jsonl",
    "depends-on.jsonl",
    "strengthen-by.jsonl",
    "cites.jsonl",
    "subtree-aggregates.jsonl",
)


def _run_refresh() -> subprocess.CompletedProcess:
    """Run refresh-kb-metadata.py from the repo root and return the result."""
    return subprocess.run(
        [sys.executable, str(_SCRIPT)],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )


def _hash_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _read_jsonl_lines(path: Path) -> list[str]:
    """Return raw (non-empty) lines preserving exact bytes for sort checks."""
    text = path.read_text(encoding="utf-8")
    return [ln for ln in text.split("\n") if ln]


class TestRefreshIndexJsonlEmission(unittest.TestCase):
    """End-to-end tests; share a single refresh run across test methods."""

    @classmethod
    def setUpClass(cls):
        result = _run_refresh()
        cls.first_result = result
        cls.first_hashes = {
            name: _hash_file(_INDEX_DIR / name) for name in _INDEX_FILES
        }

    def test_jsonl_files_emitted(self):
        self.assertEqual(
            self.first_result.returncode,
            0,
            f"refresh exited non-zero: stderr={self.first_result.stderr}",
        )
        for name in _INDEX_FILES:
            with self.subTest(name=name):
                self.assertTrue(
                    (_INDEX_DIR / name).exists(),
                    f"missing emitted file: {name}",
                )

    def test_idempotence(self):
        # Run again and compare hashes.
        second_result = _run_refresh()
        self.assertEqual(second_result.returncode, 0)
        for name in _INDEX_FILES:
            with self.subTest(name=name):
                self.assertEqual(
                    self.first_hashes[name],
                    _hash_file(_INDEX_DIR / name),
                    f"{name} changed between runs (not idempotent)",
                )

    def test_record_counts_match_state(self):
        state = lib.discover_kb(_KB_ROOT)
        all_records = lib.build_all_records(state)
        expected = {
            "claims.jsonl": len(all_records["claims"]),
            "depends-on.jsonl": len(all_records["depends-on"]),
            "strengthen-by.jsonl": len(all_records["strengthen-by"]),
            "cites.jsonl": len(all_records["cites"]),
            "subtree-aggregates.jsonl": len(all_records["subtree-aggregates"]),
        }
        for name, want in expected.items():
            with self.subTest(name=name):
                got = len(_read_jsonl_lines(_INDEX_DIR / name))
                self.assertEqual(
                    got,
                    want,
                    f"{name}: on-disk count {got} != build_all_records count {want}",
                )

    def test_jsonl_well_formed(self):
        for name in _INDEX_FILES:
            with self.subTest(name=name):
                path = _INDEX_DIR / name
                raw = path.read_bytes()
                # Empty file is acceptable per write_jsonl semantics, but we
                # expect every file in this KB to be non-empty.
                self.assertTrue(raw, f"{name} is empty")
                # File ends with exactly one trailing newline.
                self.assertEqual(
                    raw[-1:],
                    b"\n",
                    f"{name} does not end with a newline",
                )
                self.assertNotEqual(
                    raw[-2:],
                    b"\n\n",
                    f"{name} has multiple trailing newlines",
                )
                text = raw.decode("utf-8")
                for lineno, line in enumerate(text.split("\n"), start=1):
                    if lineno == len(text.split("\n")):
                        # Last element is empty string from terminal "\n".
                        self.assertEqual(line, "", f"{name}: trailing content after final newline")
                        continue
                    obj = json.loads(line)
                    self.assertIsInstance(
                        obj,
                        dict,
                        f"{name}:{lineno}: not a JSON object",
                    )

    def test_claims_jsonl_node_type_distribution(self):
        from collections import Counter

        recs = [
            json.loads(ln)
            for ln in _read_jsonl_lines(_INDEX_DIR / "claims.jsonl")
        ]
        counts = Counter(r.get("node_type", "claim") for r in recs)
        self.assertEqual(len(recs), 221)
        self.assertEqual(counts["claim"], 199)
        self.assertEqual(counts["invariant"], 18)
        self.assertEqual(counts["axiom"], 4)

    def test_depends_on_target_kind_distribution(self):
        from collections import Counter

        recs = [
            json.loads(ln)
            for ln in _read_jsonl_lines(_INDEX_DIR / "depends-on.jsonl")
        ]
        counts = Counter(r["target_kind"] for r in recs)
        self.assertEqual(len(recs), 40)
        self.assertEqual(counts["claim"], 33)
        self.assertEqual(counts["invariant"] + counts["axiom"], 7)

    def test_depends_on_target_kind_matches_resolved_node_type(self):
        # Every edge's target_kind must equal the node_type of the record it
        # resolves to in claims.jsonl.
        node_type = {
            json.loads(ln)["id"]: json.loads(ln).get("node_type", "claim")
            for ln in _read_jsonl_lines(_INDEX_DIR / "claims.jsonl")
        }
        for ln in _read_jsonl_lines(_INDEX_DIR / "depends-on.jsonl"):
            rec = json.loads(ln)
            self.assertIn(rec["target"], node_type, f"orphan target: {rec}")
            self.assertEqual(
                rec["target_kind"],
                node_type[rec["target"]],
                f"target_kind mismatch: {rec}",
            )

    def test_referential_integrity(self):
        # Build the set of canonical claim ids from claims.jsonl.
        claims_path = _INDEX_DIR / "claims.jsonl"
        canonical_ids = {
            json.loads(ln)["id"] for ln in _read_jsonl_lines(claims_path)
        }

        # depends-on: source and target must each appear in claims.jsonl.
        dep_path = _INDEX_DIR / "depends-on.jsonl"
        for ln in _read_jsonl_lines(dep_path):
            rec = json.loads(ln)
            self.assertIn(rec["source"], canonical_ids, f"depends-on source orphan: {rec}")
            self.assertIn(rec["target"], canonical_ids, f"depends-on target orphan: {rec}")

        # strengthen-by: claim_id must appear in claims.jsonl. (mentioned_ids
        # may include ids that are not canonical — SCHEMA.md notes orphan
        # detection is global, not per-file.)
        sb_path = _INDEX_DIR / "strengthen-by.jsonl"
        for ln in _read_jsonl_lines(sb_path):
            rec = json.loads(ln)
            self.assertIn(
                rec["claim_id"],
                canonical_ids,
                f"strengthen-by claim_id orphan: {rec}",
            )

        # cites: claim_id must appear in claims.jsonl.
        cites_path = _INDEX_DIR / "cites.jsonl"
        for ln in _read_jsonl_lines(cites_path):
            rec = json.loads(ln)
            self.assertIn(
                rec["claim_id"],
                canonical_ids,
                f"cites claim_id orphan: {rec}",
            )

        # subtree-aggregates: every id within each subtree_claims must
        # appear in claims.jsonl.
        agg_path = _INDEX_DIR / "subtree-aggregates.jsonl"
        for ln in _read_jsonl_lines(agg_path):
            rec = json.loads(ln)
            for cid in rec["subtree_claims"]:
                self.assertIn(
                    cid,
                    canonical_ids,
                    f"subtree-aggregates orphan id {cid} in {rec['node_path']}",
                )

    def test_sort_order(self):
        # claims.jsonl sorted by (node_type, id)
        claims_keys = [
            (json.loads(ln).get("node_type", "claim"), json.loads(ln)["id"])
            for ln in _read_jsonl_lines(_INDEX_DIR / "claims.jsonl")
        ]
        self.assertEqual(claims_keys, sorted(claims_keys))

        # depends-on.jsonl sorted by (source, target, context)
        dep_keys = [
            (
                json.loads(ln)["source"],
                json.loads(ln)["target"],
                json.loads(ln).get("context") or "",
            )
            for ln in _read_jsonl_lines(_INDEX_DIR / "depends-on.jsonl")
        ]
        self.assertEqual(dep_keys, sorted(dep_keys))

        # strengthen-by.jsonl sorted by (claim_id, item_idx)
        sb_keys = [
            (json.loads(ln)["claim_id"], json.loads(ln)["item_idx"])
            for ln in _read_jsonl_lines(_INDEX_DIR / "strengthen-by.jsonl")
        ]
        self.assertEqual(sb_keys, sorted(sb_keys))

        # cites.jsonl sorted by (claim_id, leaf_path)
        cite_keys = [
            (json.loads(ln)["claim_id"], json.loads(ln)["leaf_path"])
            for ln in _read_jsonl_lines(_INDEX_DIR / "cites.jsonl")
        ]
        self.assertEqual(cite_keys, sorted(cite_keys))

        # subtree-aggregates.jsonl sorted by node_path
        agg_keys = [
            json.loads(ln)["node_path"]
            for ln in _read_jsonl_lines(_INDEX_DIR / "subtree-aggregates.jsonl")
        ]
        self.assertEqual(agg_keys, sorted(agg_keys))


_CQ_FILES = (
    "claim-quality.md",
    "vol1/claim-quality.md",
    "vol2/claim-quality.md",
    "vol3/claim-quality.md",
    "vol4/claim-quality.md",
    "vol5/claim-quality.md",
    "vol6/claim-quality.md",
    "common/claim-quality.md",
)


class TestRefreshSolidityWriteBack(unittest.TestCase):
    """Refresh writes derived solidity into claim-quality.md, idempotently.

    These tests run refresh against the real KB. Refresh is idempotent, so on
    an already-refreshed KB they are non-mutating; the assertions hold whether
    or not the KB needed correction.
    """

    @classmethod
    def setUpClass(cls):
        # First run: bring the KB to a fully-refreshed state.
        first = _run_refresh()
        assert first.returncode == 0, first.stderr
        cls.cq_hashes = {
            rel: _hash_file(_KB_ROOT / rel) for rel in _CQ_FILES
        }

    def test_solidity_lines_idempotent(self):
        # A second refresh must leave every claim-quality.md byte-identical.
        second = _run_refresh()
        self.assertEqual(second.returncode, 0, second.stderr)
        for rel in _CQ_FILES:
            with self.subTest(file=rel):
                self.assertEqual(
                    self.cq_hashes[rel],
                    _hash_file(_KB_ROOT / rel),
                    f"{rel} changed on a second refresh (not idempotent)",
                )

    def test_known_entries_carry_derived_solidity(self):
        # After refresh, on-disk solidity equals compute_solidity output.
        state = lib.discover_kb(_KB_ROOT, diagnostic_stream=None)
        sol = lib.compute_solidity(state.claim_entries)
        by_id = {e.id: e for e in state.claim_entries}
        for cid, expected in (
            ("clm-0ktpcn", 0.41),
            ("clm-2e9j97", 0.24),
            ("clm-zi6t1e", 0.29),
            ("clm-ibfyda", 0.27),
            ("clm-m7qd0w", 0.27),
        ):
            with self.subTest(claim=cid):
                self.assertEqual(sol[cid], expected)
                # The on-disk solidity line (parsed back) matches.
                self.assertEqual(by_id[cid].solidity, expected)

    def test_solidity_line_has_arithmetic_trace_when_deps_present(self):
        # clm-2e9j97 has dependencies → its solidity line carries a [= ...]
        # trace; clm-trf3bd has none → no trace.
        text = (_KB_ROOT / "claim-quality.md").read_text()
        line = next(
            ln
            for ln in text.splitlines()
            if ln.startswith("- solidity:") and "0.24" in ln
        )
        self.assertIn("[= 0.85 × 0.28]", line)

    def test_depends_on_annotations_synced(self):
        # Every claim-target depends-on (solidity X) annotation equals the
        # target's computed solidity after refresh.
        state = lib.discover_kb(_KB_ROOT, diagnostic_stream=None)
        sol = lib.compute_solidity(state.claim_entries)
        for entry in state.claim_entries:
            for edge in entry.depends_on:
                if edge.target_kind != "claim":
                    continue
                if edge.target_solidity_recorded is None:
                    continue
                with self.subTest(claim=entry.id, target=edge.target):
                    self.assertAlmostEqual(
                        edge.target_solidity_recorded,
                        sol[edge.target],
                        places=2,
                    )


def _load_refresh_module():
    """Import refresh-kb-metadata.py as a module (its name has a hyphen)."""
    if "_refresh_kb_metadata_mod" in sys.modules:
        return sys.modules["_refresh_kb_metadata_mod"]
    spec = importlib.util.spec_from_file_location(
        "_refresh_kb_metadata_mod", str(_SCRIPT)
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["_refresh_kb_metadata_mod"] = mod
    spec.loader.exec_module(mod)
    return mod


# A synthetic claim-quality.md exercising the dormant numeric-confidence-
# blocked-by-pending-dependency path. ``clm-pppppp`` has pending confidence;
# ``clm-aaaaaa`` has numeric confidence (0.90) but depends on it — so its
# solidity is *pending* too. Both the solidity line and the (solidity X)
# annotation below carry STALE numeric values that refresh must correct to
# the *pending* form.
_SYNTHETIC_BLOCKED_CQ = """\
## Pending Upstream Claim
<!-- id: clm-pppppp -->

Body.

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - Assess this claim.

---

## Numeric Claim Blocked By A Pending Dependency
<!-- id: clm-aaaaaa -->

Body.

### Quality
- confidence: 0.90
- depends-on:
  - clm-pppppp — Pending Upstream Claim (solidity 0.42) [stale numeric annotation]
- solidity: 0.85 (ok to build on) [= 0.90 × 0.95]
- rationale: A numeric-confidence claim whose only dependency is pending.
- strengthen-by:
  - Assess the upstream claim.
"""


class TestRefreshSolidityPendingWriteBack(unittest.TestCase):
    """Refresh renders a numeric-confidence-blocked claim as ``*pending*``.

    The real KB is a closed subgraph — no numeric-confidence claim depends on
    a pending one — so this consumer path is dormant against canonical
    content. This test drives the solidity write-back over a synthetic
    fixture that DOES exercise it, locking the audit-item-1 fix: a numeric
    claim blocked by a pending dependency must get the ``- solidity:
    *pending*`` line (not a stale numeric value, not a crash), and a
    depends-on bullet pointing at it must get ``(solidity *pending*)``.
    """

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.kb_root = Path(self._tmp.name)
        self.cq_path = self.kb_root / "claim-quality.md"
        self.cq_path.write_text(_SYNTHETIC_BLOCKED_CQ, encoding="utf-8")
        self.refresh = _load_refresh_module()

    def tearDown(self):
        self._tmp.cleanup()

    def _rewrite(self):
        entries = lib.parse_claim_quality_file(self.cq_path, self.kb_root)
        solidity = lib.compute_solidity(entries)
        # The blocked claim must be absent from compute_solidity's result.
        self.assertNotIn("clm-aaaaaa", solidity)
        self.assertNotIn("clm-pppppp", solidity)
        self.refresh._rewrite_claim_quality_solidity(
            self.cq_path, entries, solidity
        )
        return self.cq_path.read_text(encoding="utf-8")

    def test_blocked_claim_solidity_line_rewritten_to_pending(self):
        text = self._rewrite()
        # The stale numeric solidity line is gone; the *pending* form is in.
        self.assertNotIn("- solidity: 0.85", text)
        self.assertNotIn("ok to build on", text)
        # Exactly two *pending* solidity lines: the upstream claim and the
        # now-corrected blocked claim.
        pending_lines = [
            ln for ln in text.splitlines()
            if ln.strip() == "- solidity: *pending*"
        ]
        self.assertEqual(len(pending_lines), 2)

    def test_blocked_target_annotation_rewritten_to_pending(self):
        text = self._rewrite()
        # The depends-on bullet's stale (solidity 0.42) annotation is synced
        # to the pending form.
        self.assertNotIn("(solidity 0.42)", text)
        self.assertIn("(solidity *pending*)", text)

    def test_rewrite_is_idempotent(self):
        first = self._rewrite()
        # A second pass over the now-corrected content changes nothing.
        entries = lib.parse_claim_quality_file(self.cq_path, self.kb_root)
        solidity = lib.compute_solidity(entries)
        self.refresh._rewrite_claim_quality_solidity(
            self.cq_path, entries, solidity
        )
        self.assertEqual(first, self.cq_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()

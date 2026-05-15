"""Tests for ``ave.kb.index`` (Phase 3 runtime query module).

Loads the live ``.index/*.jsonl`` artifact under ``manuscript/ave-kb/`` and
exercises both the in-process query API and the CLI surface.

Run via stdlib unittest::

    PYTHONPATH=src python -m unittest tests.kb.test_index

or, equivalently from the repo root, ``python -m unittest discover -s src``.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from ave.kb import index as kb_index
from ave.kb.index import CitationEdge, Claim, StrengthenByItem


def _repo_root() -> Path:
    """Walk up from this file to the AVE-Core repo root (contains src/ and manuscript/)."""
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "src").is_dir() and (parent / "manuscript").is_dir():
            return parent
    raise RuntimeError("could not locate AVE-Core repo root from test file")


REPO_ROOT = _repo_root()
INDEX_DIR = REPO_ROOT / "manuscript" / "ave-kb" / ".index"


class TestLoad(unittest.TestCase):
    def test_load_succeeds(self) -> None:
        idx = kb_index.load()
        self.assertGreater(len(idx), 0)
        # Explicit-path load should produce the same population.
        idx_explicit = kb_index.load(INDEX_DIR)
        self.assertEqual(len(idx), len(idx_explicit))

    def test_load_missing_files(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaises(FileNotFoundError) as ctx:
                kb_index.load(td)
            msg = str(ctx.exception)
            self.assertIn("missing", msg)
            self.assertIn("make refresh-kb-metadata", msg)
            # Each required file should appear as a bullet in the message.
            for name in (
                "claims.jsonl",
                "depends-on.jsonl",
                "strengthen-by.jsonl",
                "cites.jsonl",
                "subtree-aggregates.jsonl",
            ):
                self.assertIn(name, msg)


class TestQueries(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.idx = kb_index.load()

    # ---- Claim lookup --------------------------------------------------

    def test_claim_lookup(self) -> None:
        c = self.idx.claim("trf3bd")
        self.assertIsNotNone(c)
        assert c is not None  # narrow for type checker
        self.assertIn("Trefoil", c.title)
        self.assertEqual(c.confidence, 0.75)
        self.assertIsInstance(c, Claim)

    def test_claim_missing(self) -> None:
        self.assertIsNone(self.idx.claim("nope01"))

    # ---- Dependency edges ----------------------------------------------

    def test_depends_on_forward(self) -> None:
        deps = self.idx.depends_on("5xon03")
        self.assertIn("unk0bd", deps)
        # Result must be sorted and deduplicated.
        self.assertEqual(deps, sorted(set(deps)))

    def test_depends_on_inverse(self) -> None:
        dependents = self.idx.dependents_of("unk0bd")
        self.assertIn("5xon03", dependents)

    # ---- Strengthen-by --------------------------------------------------

    def test_strengthen_by_for_claim(self) -> None:
        items = self.idx.strengthen_by("trf3bd")
        self.assertEqual(len(items), 3)
        self.assertEqual([it.item_idx for it in items], [0, 1, 2])
        for it in items:
            self.assertIsInstance(it, StrengthenByItem)
            self.assertEqual(it.claim_id, "trf3bd")

    def test_gated_on(self) -> None:
        gated = self.idx.gated_on("unk0bd")
        self.assertIn("5xon03", gated)

    # ---- Citations ------------------------------------------------------

    def test_cited_by(self) -> None:
        cites = self.idx.cited_by("trf3bd")
        self.assertGreater(len(cites), 0)
        for c in cites:
            self.assertIsInstance(c, CitationEdge)
            self.assertEqual(c.claim_id, "trf3bd")

    def test_claims_in_leaf(self) -> None:
        # trf3bd is cited by vol1/ch8-alpha-golden-torus.md (per the on-disk index).
        leaf_path = "vol1/ch8-alpha-golden-torus.md"
        claims = self.idx.claims_in_leaf(leaf_path)
        self.assertIn("trf3bd", claims)

    # ---- Subtree aggregation -------------------------------------------

    def test_subtree_claims_volumes(self) -> None:
        vol1 = self.idx.subtree_claims("vol1")
        self.assertGreater(len(vol1), 0)
        all_ids = {c.id for c in self.idx.all_claims}
        for cid in vol1:
            self.assertIn(cid, all_ids)
        # Union of every volume subtree should be a subset of the entry-point.
        ep = set(self.idx.subtree_claims(""))
        union: set[str] = set()
        for vol in ("vol1", "vol2", "vol3", "vol4", "vol5", "vol6"):
            union.update(self.idx.subtree_claims(vol))
        self.assertTrue(union.issubset(ep))

    def test_subtree_claims_entry_point(self) -> None:
        empty = self.idx.subtree_claims("")
        dot = self.idx.subtree_claims(".")
        self.assertEqual(set(empty), set(dot))
        self.assertEqual(len(empty), 199)
        # Sanity-check a few canonical IDs.
        for cid in ("trf3bd", "unk0bd", "5xon03", "0ktpcn"):
            self.assertIn(cid, empty)

    # ---- Filters --------------------------------------------------------

    def test_solidity_below(self) -> None:
        below_half = {c.id for c in self.idx.solidity_below(0.5)}
        self.assertIn("unk0bd", below_half)  # solidity 0.40
        self.assertNotIn("trf3bd", below_half)  # solidity 0.75
        # Sort: solidity ascending, then id.
        seq = self.idx.solidity_below(0.5)
        prev = (-1.0, "")
        for c in seq:
            assert c.solidity is not None
            cur = (c.solidity, c.id)
            self.assertGreaterEqual(cur, prev)
            prev = cur

    def test_in_band(self) -> None:
        do_not_build = {c.id for c in self.idx.in_band("do-not-build")}
        self.assertIn("unk0bd", do_not_build)

    # ---- Stats ----------------------------------------------------------

    def test_stats(self) -> None:
        s = self.idx.stats
        self.assertEqual(s["claims"], 199)
        self.assertEqual(s["depends_on_edges"], 33)
        self.assertEqual(s["strengthen_by_items"], 259)
        self.assertEqual(s["citation_edges"], 621)
        self.assertEqual(s["subtree_aggregates"], 111)


class TestCli(unittest.TestCase):
    """Smoke tests for the CLI; invoked via subprocess against the live index."""

    def _run(self, *args: str, expect_exit: int = 0) -> subprocess.CompletedProcess:
        env = {**os.environ, "PYTHONPATH": str(REPO_ROOT / "src")}
        proc = subprocess.run(
            [sys.executable, "-m", "ave.kb", *args],
            cwd=REPO_ROOT,
            env=env,
            capture_output=True,
            text=True,
            timeout=30,
        )
        self.assertEqual(
            proc.returncode,
            expect_exit,
            msg=f"argv={args!r} stderr={proc.stderr!r} stdout={proc.stdout!r}",
        )
        return proc

    def test_deps_forward(self) -> None:
        proc = self._run("deps", "5xon03")
        self.assertIn("unk0bd", proc.stdout)

    def test_deps_inverse(self) -> None:
        proc = self._run("deps", "-i", "unk0bd")
        self.assertIn("5xon03", proc.stdout)

    def test_gated_on(self) -> None:
        proc = self._run("gated-on", "unk0bd")
        self.assertIn("5xon03", proc.stdout)

    def test_cited_by(self) -> None:
        proc = self._run("cited-by", "trf3bd")
        self.assertTrue(proc.stdout.strip())

    def test_solidity_below(self) -> None:
        proc = self._run("solidity-below", "0.5")
        self.assertIn("unk0bd", proc.stdout)

    def test_subtree_entrypoint(self) -> None:
        proc = self._run("subtree", "")
        lines = [ln for ln in proc.stdout.splitlines() if ln.strip()]
        self.assertEqual(len(lines), 199)

    def test_show(self) -> None:
        proc = self._run("show", "trf3bd")
        self.assertIn("Trefoil", proc.stdout)
        self.assertIn("build_band", proc.stdout)

    def test_show_unknown(self) -> None:
        self._run("show", "nope01", expect_exit=1)

    def test_stats(self) -> None:
        proc = self._run("stats")
        self.assertIn("claims:", proc.stdout)
        self.assertIn("199", proc.stdout)

    def test_json_parses(self) -> None:
        proc = self._run("solidity-below", "0.5", "--json")
        data = json.loads(proc.stdout)
        self.assertIsInstance(data, list)
        self.assertTrue(any(rec.get("id") == "unk0bd" for rec in data))


if __name__ == "__main__":
    unittest.main()

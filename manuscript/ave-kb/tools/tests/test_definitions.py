"""Unit tests for the `def-` definition spine (INVARIANT-S12, Stage 2).

Covers the vocabulary-register parser (`parse_definition_entries`), the
`node_type: definition` materialization in `build_claims_records`, and the
malformed-entry drift-gate (`DefinitionEntryError`). Fully self-contained:
every test builds a synthetic register under a `tmp` KB root, so nothing here
reads or asserts on `manuscript/ave-kb/` proper or the shared `mini-kb`
fixture. The live register's own health is covered by `make verify-kb-metadata`.

Run via the `test-tools` make target (sets `PYTHONPATH=manuscript/ave-kb/tools`).
"""

import tempfile
import unittest
from pathlib import Path

# kb_index_lib resolves via PYTHONPATH (set by the test-tools make target).
import kb_index_lib as lib  # noqa: E402


# A synthetic register exercising every status class + the orthogonal
# (SOLID + open-ambiguity) case + the inline `def-xxxxxx` field-legend
# placeholder that must NOT parse as an entry.
_REGISTER = """[↑ Parent](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "register"
-->

# Vocabulary Register

## Per-node field legend

Each `## <term>` heading carries a `<!-- id: def-xxxxxx -->` marker and a
field block (this inline placeholder must never parse as an entry).

---

## node
<!-- id: def-aaaaaa -->

- **term:** node
- **adjudicated-meaning:** the spatial-Nyquist sampling boundary of the lattice
  — one Brillouin cell at pitch $\\ell_{node}$.
- **axis:** spatial-Brillouin
- **dimension/type:** length (L)
- **status:** SOLID
- **canonical-home:** `vol1/paley-wiener-hilbert.md:10`
- **clm-cross-links:** clm-bbbbbb, clm-aaaaaa
- **open-ambiguity-flag:** YES — the surface form is overloaded elsewhere.
  - conflicting sites: graph-vertex usage `docs/glossary.md:20` ("..."); core `src/ave/core/x.py:68` ("...").
  - **OPEN sub-flag (over-read guard):** a paraphrase cited to `should-not-appear.md:99` that did NOT verify.
- **verification:** VERIFIED.

---

## carrier
<!-- id: def-cccccc -->

- **term:** carrier
- **adjudicated-meaning:** the fast internal phase oscillation.
- **axis:** phase-carrier
- **dimension/type:** frequency (T⁻¹)
- **status:** ambiguous
- **canonical-home:** *(none locked)*
- **clm-cross-links:** *(none verified-specific yet)*
- **open-ambiguity-flag:** YES — two readings.
  - conflicting sites: carrier-frequency `a.md:5`; charge-carrier `b.md:9`.
- **verification:** VERIFIED.

---

## kappa_share *(proposed)*
<!-- id: def-dddddd -->

- **term:** kappa_share
- **adjudicated-meaning:** *(PROPOSED, gated)* the dimensionless coupling-budget ratio.
- **axis:** dimensionless
- **dimension/type:** dimensionless
- **status:** proposed
- **canonical-home:** *(none — coinage)*
- **clm-cross-links:** clm-bbbbbb
- **open-ambiguity-flag:** no (a fresh coinage carries no prior overloading)
- **verification:** VERIFIED 0 prior corpus hits.
"""


def _write_register(root: Path, body: str = _REGISTER) -> Path:
    common = root / "common"
    common.mkdir(parents=True, exist_ok=True)
    path = common / lib.VOCAB_REGISTER_NAME
    path.write_text(body, encoding="utf-8")
    return path


class TestParseDefinitionEntries(unittest.TestCase):
    def _parse(self, body: str = _REGISTER):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            path = _write_register(root, body)
            return lib.parse_definition_entries(path, root)

    def test_entry_count_excludes_inline_placeholder(self):
        nodes = self._parse()
        # Three real entries; the inline `def-xxxxxx` placeholder is excluded
        # (it does not begin its line).
        self.assertEqual(len(nodes), 3)
        self.assertEqual(
            [n.id for n in nodes], ["def-aaaaaa", "def-cccccc", "def-dddddd"]
        )

    def test_field_extraction(self):
        node = next(n for n in self._parse() if n.id == "def-aaaaaa")
        self.assertEqual(node.term, "node")
        self.assertIn("spatial-Nyquist sampling boundary", node.adjudicated_meaning)
        # Wrapped meaning folds to a single line.
        self.assertNotIn("\n", node.adjudicated_meaning)
        self.assertEqual(node.axis, "spatial-Brillouin")
        self.assertEqual(node.dimension, "length (L)")
        self.assertEqual(node.status, "SOLID")

    def test_canonical_path_is_register_anchor_is_heading(self):
        node = next(n for n in self._parse() if n.id == "def-aaaaaa")
        # canonical_path is the register leaf (NOT the editorial canonical-home).
        self.assertEqual(
            node.canonical_path, "common/" + lib.VOCAB_REGISTER_NAME
        )
        self.assertEqual(node.canonical_anchor, "node")

    def test_clm_cross_links_sorted_unique(self):
        node = next(n for n in self._parse() if n.id == "def-aaaaaa")
        self.assertEqual(node.clm_cross_links, ("clm-aaaaaa", "clm-bbbbbb"))

    def test_empty_clm_cross_links(self):
        node = next(n for n in self._parse() if n.id == "def-cccccc")
        self.assertEqual(node.clm_cross_links, ())

    def test_open_ambiguity_orthogonal_to_solid(self):
        # SOLID status AND open_ambiguity True is the canonical orthogonal case.
        node = next(n for n in self._parse() if n.id == "def-aaaaaa")
        self.assertEqual(node.status, "SOLID")
        self.assertTrue(node.open_ambiguity)

    def test_conflicting_sites_only_from_conflicting_bullet(self):
        # Cites come ONLY from the `- conflicting sites:` sub-bullet; the
        # OPEN-sub-flag guard's cite (`should-not-appear.md:99`) is excluded.
        node = next(n for n in self._parse() if n.id == "def-aaaaaa")
        self.assertEqual(
            node.conflicting_sites,
            ("docs/glossary.md:20", "src/ave/core/x.py:68"),
        )
        self.assertNotIn("should-not-appear.md:99", node.conflicting_sites)

    def test_no_open_ambiguity_empty_conflicting_sites(self):
        node = next(n for n in self._parse() if n.id == "def-dddddd")
        self.assertFalse(node.open_ambiguity)
        self.assertEqual(node.conflicting_sites, ())
        self.assertEqual(node.status, "proposed")


class TestDefinitionDriftGate(unittest.TestCase):
    """A perturbed/malformed entry must raise DefinitionEntryError (drift-gate)."""

    def _parse_with(self, body: str):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            path = _write_register(root, body)
            return lib.parse_definition_entries(path, root)

    def test_unknown_status_raises(self):
        bad = _REGISTER.replace("- **status:** SOLID", "- **status:** SOLDI")
        with self.assertRaises(lib.DefinitionEntryError):
            self._parse_with(bad)

    def test_missing_required_field_raises(self):
        bad = _REGISTER.replace("- **axis:** spatial-Brillouin\n", "")
        with self.assertRaises(lib.DefinitionEntryError):
            self._parse_with(bad)

    def test_ambiguous_without_open_flag_raises(self):
        # An `ambiguous` term that drops its mandatory open-ambiguity YES.
        bad = _REGISTER.replace(
            "- **status:** ambiguous\n- **canonical-home:** *(none locked)*\n"
            "- **clm-cross-links:** *(none verified-specific yet)*\n"
            "- **open-ambiguity-flag:** YES — two readings.",
            "- **status:** ambiguous\n- **canonical-home:** *(none locked)*\n"
            "- **clm-cross-links:** *(none verified-specific yet)*\n"
            "- **open-ambiguity-flag:** no",
        )
        with self.assertRaises(lib.DefinitionEntryError):
            self._parse_with(bad)


class TestDefinitionMaterialization(unittest.TestCase):
    """`build_claims_records` emits the definition group in sort order."""

    def _records(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            path = _write_register(root)
            defs = lib.parse_definition_entries(path, root)
        state = lib.KbState(
            claim_entries=(),
            leaves=(),
            indexes=(),
            framework_nodes=(),
            experiments=(),
            supports=(),
            definitions=tuple(defs),
        )
        return lib.build_claims_records(state)

    def test_definition_records_emitted(self):
        recs = self._records()
        defs = [r for r in recs if r["node_type"] == "definition"]
        self.assertEqual(len(defs), 3)

    def test_field_order_matches_schema(self):
        recs = self._records()
        first = next(r for r in recs if r["node_type"] == "definition")
        self.assertEqual(
            list(first.keys()),
            [
                "node_type",
                "id",
                "term",
                "adjudicated_meaning",
                "axis",
                "dimension",
                "status",
                "canonical_path",
                "canonical_anchor",
                "clm_cross_links",
                "open_ambiguity",
                "conflicting_sites",
            ],
        )

    def test_terminal_node_no_scoring_fields(self):
        recs = self._records()
        first = next(r for r in recs if r["node_type"] == "definition")
        for forbidden in ("confidence", "solidity", "quality", "build_band"):
            self.assertNotIn(forbidden, first)

    def test_clm_cross_links_serialize_as_list(self):
        recs = self._records()
        node_rec = next(r for r in recs if r["id"] == "def-aaaaaa")
        self.assertEqual(node_rec["clm_cross_links"], ["clm-aaaaaa", "clm-bbbbbb"])
        self.assertIsInstance(node_rec["conflicting_sites"], list)

    def test_definition_sorts_between_claim_and_experiment(self):
        # Build a mixed state so the group ordering is observable. Definitions
        # sort between claim and experiment (axiom < claim < definition <
        # experiment < invariant < support).
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            path = _write_register(root)
            defs = lib.parse_definition_entries(path, root)
        exp = lib.ExperimentNode(
            id="exp-zzzzzz",
            title="t",
            canonical_path="p.md",
            canonical_anchor="t",
            status="run",
            strengthens=(),
        )
        state = lib.KbState(
            claim_entries=(),
            leaves=(),
            indexes=(),
            framework_nodes=(),
            experiments=(exp,),
            supports=(),
            definitions=tuple(defs),
        )
        recs = lib.build_claims_records(state)
        types = [r["node_type"] for r in recs]
        last_def = max(i for i, t in enumerate(types) if t == "definition")
        first_exp = min(i for i, t in enumerate(types) if t == "experiment")
        self.assertLess(last_def, first_exp)


if __name__ == "__main__":
    unittest.main()

"""Tests for the derived ``> **Leaf references:**`` footer.

The footer is the reverse-citation map of a claim-quality entry — which leaves
host the entry's id. It is a derived field: ``refresh-kb-metadata`` regenerates
it from leaf frontmatter and ``verify-kb-metadata`` drift-gates it, exactly like
``subtree-claims`` and the derived ``solidity`` line (INVARIANT-S8).

Three layers exercised here:

* Unit — :func:`kb_index_lib.build_leaf_references` (the reverse map) and
  :func:`kb_index_lib.render_leaf_references` (footer text), verified directly.
* Integration (generation) — run ``refresh-kb-metadata.py`` against a small
  synthetic KB built in a tempdir; assert the footer it writes matches the
  derived one for the single-leaf, multi-leaf, exp-, and sup- cases, and that a
  second run is byte-identical (idempotent).
* Integration (drift gate) — hand-edit a footer in the refreshed KB and assert
  ``verify-kb-metadata.py`` fails with a leaf-references drift report.

Nothing here reads, writes, or asserts on ``manuscript/ave-kb/`` proper — the KB
is constructed file-by-file in a per-test tempdir.

Run from the tools dir::

    python -m unittest tests.test_leaf_references
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_TOOLS_DIR = _THIS_DIR.parent

# kb_index_lib resolves via PYTHONPATH (set by the test-tools make target).
import kb_index_lib as lib  # noqa: E402

_REFRESH = _TOOLS_DIR / "refresh-kb-metadata.py"
_VERIFY = _TOOLS_DIR / "verify-kb-metadata.py"


def _run(script: Path, kb_root: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(script), "--kb-root", str(kb_root)],
        capture_output=True, text=True, check=False,
    )


# ---------------------------------------------------------------------------
# A minimal but realistic synthetic KB. One register at vol-root, leaves under
# its directory citing claims, hosting one experiment and one support.
# ---------------------------------------------------------------------------

_CLAUDE_MD = """# Mini Invariants

### INVARIANT-S2: AVE Axiom numbering

- Axiom 4: **Universal Saturation Kernel** — S(A).
"""

_ENTRY_POINT = """[↑ root](entry-point.md)

<!-- kb-frontmatter
kind: entry-point
subtree-claims: []
bootstrap: true
-->

# Entry
"""

_VOL_INDEX = """[↑ root](../entry-point.md)

<!-- kb-frontmatter
kind: index
subtree-claims: []
-->

# Vol Index
"""

# A register with NO footers authored — refresh must INSERT them. The single
# leaf cites clm-aa1111; the multi leaf cites clm-aa1111 + clm-bb2222 (so
# clm-aa1111 is cited by two leaves — the multi-leaf case). A support sup-ss1111
# and an experiment exp-ee1111 live in their own leaves.
_REGISTER = """# Vol Register

> **Canonicality preamble.** Synthetic register.

```markdown
## Example
<!-- id: clm-example -->
> **Leaf references:** fenced example must be ignored.
### Quality
```

---

## Anchor Claim
<!-- id: clm-aa1111 -->

Body prose for the anchor claim.

### Quality
- confidence: 0.90
- solidity: 0.90 (ok to build on)
- rationale: synthetic.
- strengthen-by:
  - work.

---

## Second Claim
<!-- id: clm-bb2222 -->

Body prose. This entry has a STALE hand-authored footer that refresh must fix.

> **Leaf references:** `wrong/path/that/does-not-exist.md` §5 (bogus annotation).

### Quality
- confidence: 0.60
- solidity: 0.60 (use as input only, don't build deeper)
- rationale: synthetic.
- strengthen-by:
  - work.

---

## Free-standing Support
<!-- id: sup-ss1111 -->

### Quality
- quality: 0.80
- solidity: 0.80 (ok to build on, see caveats)
- rationale: synthetic support.
- supports:
  - clm-aa1111 (f=1.0)
"""

_LEAF_SINGLE = """[↑ idx](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-aa1111]
-->

# Single
Body.
"""

_LEAF_MULTI = """[↑ idx](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-aa1111, clm-bb2222]
-->

# Multi

<!-- claim-quality: clm-aa1111 -->
A.

<!-- claim-quality: clm-bb2222 -->
B.
"""

_LEAF_EXP = """[↑ idx](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "hosts an experiment"
exp-id: exp-ee1111
status: run
strengthens:
  - clm-aa1111: 1.0
-->

# Experiment Leaf
Body.
"""

_LEAF_SUP = """[↑ idx](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "hosts a support"
sup-id: sup-ss1111
supports:
  - clm-aa1111: 1.0
-->

# Support Leaf
Body.
"""


def _build_kb(root: Path) -> None:
    """Materialize the synthetic KB under ``root``."""
    (root / "CLAUDE.md").write_text(_CLAUDE_MD)
    (root / "entry-point.md").write_text(_ENTRY_POINT)
    vol = root / "vol"
    vol.mkdir()
    (vol / "index.md").write_text(_VOL_INDEX)
    (vol / "claim-quality.md").write_text(_REGISTER)
    (vol / "leaf-single.md").write_text(_LEAF_SINGLE)
    (vol / "leaf-multi.md").write_text(_LEAF_MULTI)
    (vol / "leaf-exp.md").write_text(_LEAF_EXP)
    (vol / "leaf-sup.md").write_text(_LEAF_SUP)


class TestReverseMapUnit(unittest.TestCase):
    """Direct unit tests of build_leaf_references / render_leaf_references."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.kb = Path(self._tmp.name) / "kb"
        self.kb.mkdir()
        _build_kb(self.kb)
        self.state = lib.discover_kb(self.kb, diagnostic_stream=None)
        self.refs = lib.build_leaf_references(self.state)

    def test_claim_cited_by_multiple_leaves_lists_all_sorted(self):
        # clm-aa1111 is cited by leaf-single AND leaf-multi (and the exp leaf
        # strengthens it but does NOT host its id — strengthens is not a
        # citation, so it must NOT appear). Stable-sorted by path.
        self.assertEqual(
            self.refs["clm-aa1111"],
            ["vol/leaf-multi.md", "vol/leaf-single.md"],
        )

    def test_single_leaf_claim(self):
        self.assertEqual(self.refs["clm-bb2222"], ["vol/leaf-multi.md"])

    def test_experiment_home_is_its_hosting_leaf(self):
        self.assertEqual(self.refs["exp-ee1111"], ["vol/leaf-exp.md"])

    def test_support_home_is_its_hosting_leaf(self):
        self.assertEqual(self.refs["sup-ss1111"], ["vol/leaf-sup.md"])

    def test_render_relative_to_register_dir(self):
        footer = lib.render_leaf_references(
            "vol/claim-quality.md", ["vol/leaf-single.md", "vol/leaf-multi.md"]
        )
        self.assertEqual(
            footer,
            "> **Leaf references:** [leaf-single](./leaf-single.md), "
            "[leaf-multi](./leaf-multi.md).",
        )

    def test_render_root_register_keeps_full_path(self):
        footer = lib.render_leaf_references(
            "claim-quality.md", ["vol/leaf-single.md"]
        )
        self.assertEqual(
            footer,
            "> **Leaf references:** [leaf-single](./vol/leaf-single.md).",
        )

    def test_render_cross_directory_citation_climbs(self):
        # A per-volume register cited by a leaf OUTSIDE its directory (e.g. a
        # vol1 claim hosted by a common/ leaf) must climb with ../, not emit a
        # ./-prefixed path that resolves under the register dir and 404s.
        footer = lib.render_leaf_references(
            "vol1/claim-quality.md", ["common/operators.md"]
        )
        self.assertEqual(
            footer,
            "> **Leaf references:** [operators](../common/operators.md).",
        )

    def test_render_empty_is_explicit_marker(self):
        footer = lib.render_leaf_references("vol/claim-quality.md", [])
        self.assertTrue(footer.startswith("> **Leaf references:** *(none"))
        self.assertIn("bidirectional-coverage", footer)


class TestRefreshGeneration(unittest.TestCase):
    """Run refresh against the synthetic KB; assert footers + idempotency."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.kb = Path(self._tmp.name) / "kb"
        self.kb.mkdir()
        _build_kb(self.kb)
        self.register = self.kb / "vol" / "claim-quality.md"
        result = _run(_REFRESH, self.kb)
        self.assertEqual(
            result.returncode, 0, f"refresh failed: {result.stderr}"
        )
        self.text = self.register.read_text()

    def _footer_for(self, node_id: str) -> str:
        """Return the footer line within the entry whose id is ``node_id``."""
        lines = self.text.splitlines()
        in_entry = False
        for line in lines:
            if line.strip() == f"<!-- id: {node_id} -->":
                in_entry = True
                continue
            if in_entry:
                if line.startswith(lib.LEAF_REFERENCES_PREFIX):
                    return line
                if line.strip() == "### Quality":
                    self.fail(f"no footer found for {node_id}")
        self.fail(f"id {node_id} not located")

    def test_inserted_footer_for_footerless_entry(self):
        # clm-aa1111 had no footer; refresh inserts the two-leaf footer.
        self.assertEqual(
            self._footer_for("clm-aa1111"),
            "> **Leaf references:** [leaf-multi](./leaf-multi.md), "
            "[leaf-single](./leaf-single.md).",
        )

    def test_stale_footer_overwritten(self):
        # clm-bb2222 had a bogus hand-authored footer with a dead path + prose
        # annotation; refresh replaces it with the accurate single-leaf list.
        footer = self._footer_for("clm-bb2222")
        self.assertEqual(
            footer, "> **Leaf references:** [leaf-multi](./leaf-multi.md)."
        )
        self.assertNotIn("does-not-exist", footer)
        self.assertNotIn("bogus", footer)

    def test_support_entry_footer(self):
        self.assertEqual(
            self._footer_for("sup-ss1111"),
            "> **Leaf references:** [leaf-sup](./leaf-sup.md).",
        )

    def test_idempotent(self):
        before = self.register.read_bytes()
        result = _run(_REFRESH, self.kb)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(
            self.register.read_bytes(),
            before,
            "leaf-references footer not idempotent across refresh runs",
        )

    def test_quality_block_intact(self):
        # Inserting the footer must not disturb the `### Quality` section.
        self.assertIn("- confidence: 0.90", self.text)
        self.assertIn("### Quality", self.text)


class TestVerifyDriftGate(unittest.TestCase):
    """A hand-edited footer must fail verify as refresh-fixable drift."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.kb = Path(self._tmp.name) / "kb"
        self.kb.mkdir()
        _build_kb(self.kb)
        self.register = self.kb / "vol" / "claim-quality.md"
        self.assertEqual(_run(_REFRESH, self.kb).returncode, 0)

    def test_clean_after_refresh(self):
        result = _run(_VERIFY, self.kb)
        self.assertEqual(
            result.returncode, 0,
            f"verify should pass on a freshly-refreshed KB:\n{result.stdout}",
        )

    def test_hand_edited_footer_fails(self):
        text = self.register.read_text()
        edited = text.replace(
            "> **Leaf references:** [leaf-sup](./leaf-sup.md).",
            "> **Leaf references:** [leaf-sup](./leaf-sup.md) (hand-added prose).",
        )
        self.assertNotEqual(text, edited, "test setup failed to edit a footer")
        self.register.write_text(edited)
        result = _run(_VERIFY, self.kb)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("leaf-references footer", result.stdout)

    def test_deleted_footer_fails_as_missing(self):
        text = self.register.read_text()
        edited = text.replace(
            "> **Leaf references:** [leaf-sup](./leaf-sup.md).\n",
            "",
        )
        self.assertNotEqual(text, edited, "test setup failed to delete a footer")
        self.register.write_text(edited)
        result = _run(_VERIFY, self.kb)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("(missing)", result.stdout)


if __name__ == "__main__":
    unittest.main()

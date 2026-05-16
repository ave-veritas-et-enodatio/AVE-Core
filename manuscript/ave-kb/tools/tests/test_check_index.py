"""Tests for the extended ``check-claim-quality.py`` verifier — index checks.

Exercises the three new checks (well-formed, freshness, referential
integrity) by mutating the canonical ``.index/*.jsonl`` files under
``manuscript/ave-kb/.index/`` and restoring them in a ``try/finally`` so
the working tree is left untouched even on failure.

Run from the repo root::

    cd /Users/benn/projects/AVE-Umbrella/AVE-Core/manuscript/ave-kb/tools
    python -m unittest tests.test_check_index

The synthetic-corruption test (referential integrity) avoids touching the
canonical KB by pointing the verifier at a temp ``.index/`` directory via
``--index-dir``.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

_THIS_DIR = Path(__file__).resolve().parent
_TOOLS_DIR = _THIS_DIR.parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

# Repo root: tools/tests -> tools -> ave-kb -> manuscript -> repo
_REPO_ROOT = _TOOLS_DIR.parents[2]
_KB_ROOT = _REPO_ROOT / "manuscript" / "ave-kb"
_INDEX_DIR = _KB_ROOT / ".index"
_CHECK_SCRIPT = _TOOLS_DIR / "check-claim-quality.py"
_REFRESH_SCRIPT = _TOOLS_DIR / "refresh-kb-metadata.py"


def _run_checker(extra_args: list[str] | None = None) -> subprocess.CompletedProcess:
    cmd = [sys.executable, str(_CHECK_SCRIPT)]
    if extra_args:
        cmd.extend(extra_args)
    return subprocess.run(
        cmd,
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )


def _run_refresh() -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(_REFRESH_SCRIPT)],
        cwd=str(_REPO_ROOT),
        capture_output=True,
        text=True,
        check=False,
    )


def _backup_index_file(name: str) -> bytes:
    return (_INDEX_DIR / name).read_bytes()


def _restore_index_file(name: str, content: bytes) -> None:
    (_INDEX_DIR / name).write_bytes(content)


class TestCheckIndex(unittest.TestCase):
    """Verifier extended-check behavior on real and mutated KB state."""

    @classmethod
    def setUpClass(cls):
        # Guarantee a clean canonical baseline before mutating anything.
        result = _run_refresh()
        if result.returncode != 0:
            raise AssertionError(
                f"refresh-kb-metadata exited non-zero before test setup: "
                f"stderr={result.stderr}"
            )

    def test_check_passes_on_fresh_state(self):
        """After refresh, the verifier exits 0 and reports PASS + index line."""
        result = _run_checker()
        self.assertEqual(
            result.returncode,
            0,
            f"verifier failed unexpectedly: stdout={result.stdout}, "
            f"stderr={result.stderr}",
        )
        self.assertIn("[claim-quality] PASS.", result.stdout)
        # Index summary line present on PASS.
        self.assertIn("[index] 5 JSONL files", result.stdout)

    def test_index_line_reports_node_type_breakdown(self):
        """The [index] summary reports claims / invariants / axioms counts."""
        result = _run_checker()
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("221 nodes", result.stdout)
        self.assertIn("199 claims", result.stdout)
        self.assertIn("18 invariants", result.stdout)
        self.assertIn("4 axioms", result.stdout)

    def test_check_detects_target_kind_mismatch(self):
        """A depends-on edge whose target_kind contradicts the resolved node
        fails referential integrity (kind-match)."""
        with tempfile.TemporaryDirectory() as tmp:
            tmp_index = Path(tmp) / ".index"
            tmp_index.mkdir()
            for short in (
                "claims.jsonl",
                "depends-on.jsonl",
                "strengthen-by.jsonl",
                "cites.jsonl",
                "subtree-aggregates.jsonl",
            ):
                shutil.copy2(_INDEX_DIR / short, tmp_index / short)

            # Inject an edge to a real INVARIANT node but mislabel its kind.
            dep_path = tmp_index / "depends-on.jsonl"
            existing = dep_path.read_bytes().decode("utf-8")
            first_source = existing.split("\n")[0].split('"source": "')[1].split('"')[0]
            extra = (
                '{"source": "' + first_source + '", "target": "INVARIANT-S2"'
                ', "target_kind": "claim", "target_solidity_recorded": null'
                ', "context": null}\n'
            )
            dep_path.write_bytes(existing.encode("utf-8") + extra.encode("utf-8"))

            result = _run_checker(["--index-dir", str(tmp_index)])
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("referential-integrity", result.stdout)
            self.assertIn("INVARIANT-S2", result.stdout)

    def test_check_detects_stale_jsonl(self):
        """A truncated cites.jsonl fails freshness with the refresh hint."""
        name = "cites.jsonl"
        original = _backup_index_file(name)
        try:
            text = original.decode("utf-8")
            lines = [ln for ln in text.split("\n") if ln]
            # Drop the first 5 lines.
            truncated = "\n".join(lines[5:]) + "\n"
            (_INDEX_DIR / name).write_bytes(truncated.encode("utf-8"))

            result = _run_checker()
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(name, result.stdout)
            # Freshness failures must surface the refresh-fixable hint.
            self.assertIn("make refresh-kb-metadata", result.stdout)
        finally:
            _restore_index_file(name, original)

    def test_check_detects_missing_jsonl(self):
        """A renamed JSONL file fails with a clear 'missing' message."""
        name = "strengthen-by.jsonl"
        src = _INDEX_DIR / name
        dst = _INDEX_DIR / (name + ".bak")
        src.rename(dst)
        try:
            result = _run_checker()
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("missing", result.stdout.lower())
            self.assertIn(name, result.stdout)
            self.assertIn("make refresh-kb-metadata", result.stdout)
        finally:
            dst.rename(src)

    def test_check_detects_malformed_jsonl(self):
        """Appending a non-JSON line fails the well-formed check (not refresh-fixable)."""
        name = "claims.jsonl"
        original = _backup_index_file(name)
        try:
            (_INDEX_DIR / name).write_bytes(original + b"not-a-json\n")
            result = _run_checker()
            self.assertNotEqual(result.returncode, 0)
            output = result.stdout.lower()
            # The malformed-line block uses "well-formed JSON" phrasing.
            self.assertTrue(
                "well-formed" in output or "json" in output,
                f"expected JSON well-formedness mention in output: {result.stdout}",
            )
            self.assertIn(name, result.stdout)
        finally:
            _restore_index_file(name, original)

    def test_check_detects_referential_integrity_violation(self):
        """A synthetic depends-on edge to a nonexistent target fails ref-integrity.

        Uses ``--index-dir`` to point at a temp index tree so the canonical
        ``.index/`` is never touched. Copies the real index files in, then
        rewrites ``depends-on.jsonl`` with one extra orphan edge.
        """
        with tempfile.TemporaryDirectory() as tmp:
            tmp_index = Path(tmp) / ".index"
            tmp_index.mkdir()
            for short in (
                "claims.jsonl",
                "depends-on.jsonl",
                "strengthen-by.jsonl",
                "cites.jsonl",
                "subtree-aggregates.jsonl",
            ):
                shutil.copy2(_INDEX_DIR / short, tmp_index / short)

            # Inject an edge whose target is a syntactically-valid clm- id
            # that does not appear in claims.jsonl.
            dep_path = tmp_index / "depends-on.jsonl"
            orphan_target = "clm-zzz999"
            existing = dep_path.read_bytes().decode("utf-8")
            # Pick a real source id (first edge's source); appending keeps
            # the file parseable even if sort order is broken.
            first_source = (existing.split("\n")[0].split('"source": "')[1].split('"')[0])
            extra = (
                '{"source": "' + first_source + '", "target": "' + orphan_target
                + '", "target_solidity_recorded": null, "context": null}\n'
            )
            dep_path.write_bytes(existing.encode("utf-8") + extra.encode("utf-8"))

            result = _run_checker(["--index-dir", str(tmp_index)])
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("referential-integrity", result.stdout)
            self.assertIn(orphan_target, result.stdout)

    def test_existing_checks_still_pass(self):
        """Smoke test: existing 8 checks pass on the fresh KB.

        Implicitly covered by ``test_check_passes_on_fresh_state``, but kept
        as a separate test case so a future regression in any of the
        pre-existing check functions has a dedicated red mark.
        """
        result = _run_checker()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        # The Scanned-line is the load-bearing signal that the original
        # checks ran in their original shape.
        self.assertIn("[claim-quality] Scanned", result.stdout)
        self.assertIn("canonical entries.", result.stdout)

    def test_check_detects_stale_solidity_line(self):
        """Hand-editing a solidity value fails the freshness check.

        Mutates a real claim-quality.md solidity line, runs the verifier,
        expects a refresh-fixable failure, then restores the file.
        """
        cq = _KB_ROOT / "common" / "claim-quality.md"
        original = cq.read_bytes()
        try:
            text = original.decode("utf-8")
            # clm-ibfyda's correct solidity is 0.27; inject 0.99.
            stale = text.replace(
                "- solidity: 0.27 (do not build on, rework needed) "
                "[= 0.65 × 0.41]",
                "- solidity: 0.99 (ok to build on) [= 0.65 × 0.41]",
                1,
            )
            self.assertNotEqual(stale, text, "fixture solidity line not found")
            cq.write_bytes(stale.encode("utf-8"))
            result = _run_checker()
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("solidity freshness", result.stdout)
            self.assertIn("clm-ibfyda", result.stdout)
            self.assertIn("make refresh-kb-metadata", result.stdout)
        finally:
            cq.write_bytes(original)

    def test_check_detects_stale_depends_on_annotation(self):
        """A wrong (solidity X) annotation fails the freshness check."""
        cq = _KB_ROOT / "claim-quality.md"
        original = cq.read_bytes()
        try:
            text = original.decode("utf-8")
            # clm-2e9j97 depends on clm-0ktpcn at solidity 0.41; inject 0.55.
            stale = text.replace(
                "clm-0ktpcn — Golden Torus α Derivation (solidity 0.41)",
                "clm-0ktpcn — Golden Torus α Derivation (solidity 0.55)",
                1,
            )
            self.assertNotEqual(stale, text, "fixture annotation not found")
            cq.write_bytes(stale.encode("utf-8"))
            result = _run_checker()
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("solidity freshness", result.stdout)
            self.assertIn("clm-0ktpcn", result.stdout)
        finally:
            cq.write_bytes(original)

    def test_solidity_cycle_check_function(self):
        """check_solidity_cycle reports cycle members on a cyclic graph.

        The real KB is acyclic, so this exercises the check directly with a
        synthetic two-node cycle.
        """
        check = _load_checker_module()
        lib = sys.modules["kb_index_lib"]

        def mk(cid, deps):
            return lib.ClaimEntry(
                id=cid, title=cid, canonical_path="t/claim-quality.md",
                canonical_anchor=cid, confidence=0.8, solidity=None,
                build_status=None, rationale="", strengthen_by=(),
                depends_on=tuple(
                    lib.DependsOnEdge(cid, d, "claim", None, None) for d in deps
                ),
            )

        cyclic = lib.KbState(
            claim_entries=(mk("clm-aaaaaa", ["clm-bbbbbb"]),
                           mk("clm-bbbbbb", ["clm-aaaaaa"])),
            leaves=(), indexes=(), framework_nodes=(),
        )
        members = check.check_solidity_cycle(cyclic)
        self.assertEqual(set(members), {"clm-aaaaaa", "clm-bbbbbb"})

        acyclic = lib.KbState(
            claim_entries=(mk("clm-aaaaaa", []),
                           mk("clm-bbbbbb", ["clm-aaaaaa"])),
            leaves=(), indexes=(), framework_nodes=(),
        )
        self.assertEqual(check.check_solidity_cycle(acyclic), [])

    def test_real_kb_passes_cycle_check(self):
        """The real KB's claim depends-on graph is acyclic."""
        check = _load_checker_module()
        lib = sys.modules["kb_index_lib"]
        state = lib.discover_kb(_KB_ROOT, diagnostic_stream=None)
        self.assertEqual(check.check_solidity_cycle(state), [])


# A clean synthetic register: one well-formed claim with a `### Quality` block
# that carries both its `## <title>` heading and its `<!-- id: -->` marker.
_CLEAN_REGISTER = """\
# Synthetic Register

## A Real Claim
<!-- id: clm-abc123 -->

Body text.

### Quality
- confidence: 0.50
- solidity: 0.50 (use as input only, don't build deeper)
- rationale: synthetic.
- strengthen-by:
  - assess.
"""

# Same register with an orphan `### Quality` block appended after a `---`
# separator: it has no `## <title>` and no `<!-- id: -->` marker.
_ORPHAN_REGISTER = _CLEAN_REGISTER + """\

---

### Quality
- confidence: *pending*
- solidity: *pending*
- rationale: *pending*
- strengthen-by:
  - *pending*
"""

# A register whose only `### Quality` heading sits inside a fenced code block
# (the format-example case from the Quality Convention preamble). It must NOT
# be flagged — strip_code_fences blanks it before the section scan.
_FENCED_EXAMPLE_REGISTER = """\
# Quality Convention Preamble

The format of a Quality section:

```markdown
### Quality
- confidence: 0.X
- solidity: 0.X (build-status phrase)
```

Prose continues.
"""


class TestQualityBlockIntegrity(unittest.TestCase):
    """The orphan/malformed `### Quality` detection check.

    Drives ``check_quality_block_integrity`` against synthetic register
    trees by repointing the checker module's ``KB`` global at a temp dir.
    This is the regression guard that makes the orphan-Quality defect class
    non-recurring.
    """

    def _run_against(self, register_text: str):
        """Write a synthetic claim-quality.md and run the integrity check."""
        check = _load_checker_module()
        with tempfile.TemporaryDirectory() as tmp:
            kb = Path(tmp)
            (kb / "claim-quality.md").write_text(register_text, encoding="utf-8")
            original_kb = check.KB
            try:
                check.KB = kb
                return check.check_quality_block_integrity()
            finally:
                check.KB = original_kb

    def test_clean_register_passes(self):
        """A well-formed register reports zero failures."""
        self.assertEqual(self._run_against(_CLEAN_REGISTER), [])

    def test_orphan_block_is_flagged(self):
        """An orphan `### Quality` block (no title, no id) is a failure."""
        failures = self._run_against(_ORPHAN_REGISTER)
        self.assertEqual(len(failures), 1)
        rel, line, reason = failures[0]
        self.assertEqual(rel, "claim-quality.md")
        self.assertIn("orphan", reason.lower())
        self.assertIn("title", reason)
        self.assertIn("marker", reason)

    def test_fenced_example_quality_not_flagged(self):
        """A `### Quality` heading inside a code fence is exempt."""
        self.assertEqual(self._run_against(_FENCED_EXAMPLE_REGISTER), [])

    def test_real_kb_passes_quality_block_integrity(self):
        """The canonical KB has zero orphan/malformed `### Quality` blocks."""
        check = _load_checker_module()
        self.assertEqual(check.check_quality_block_integrity(), [])

    def test_orphan_block_fails_full_verifier(self):
        """An orphan block in a real register fails the end-to-end verifier.

        Appends an orphan `### Quality` block to vol5/claim-quality.md, runs
        the verifier, expects a non-zero exit naming the file, then restores.
        """
        cq = _KB_ROOT / "vol5" / "claim-quality.md"
        original = cq.read_bytes()
        try:
            orphan = (
                b"\n\n---\n\n### Quality\n- confidence: *pending*\n"
                b"- solidity: *pending*\n- rationale: *pending*\n"
                b"- strengthen-by:\n  - *pending*\n"
            )
            cq.write_bytes(original + orphan)
            result = _run_checker()
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("orphan/malformed", result.stdout)
            self.assertIn("vol5/claim-quality.md", result.stdout)
        finally:
            cq.write_bytes(original)


def _load_checker_module():
    """Import check-claim-quality.py as a module (its name has a hyphen)."""
    import importlib.util

    if "_check_claim_quality_mod" in sys.modules:
        return sys.modules["_check_claim_quality_mod"]
    spec = importlib.util.spec_from_file_location(
        "_check_claim_quality_mod", str(_CHECK_SCRIPT)
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["_check_claim_quality_mod"] = mod
    spec.loader.exec_module(mod)
    return mod


if __name__ == "__main__":
    unittest.main()

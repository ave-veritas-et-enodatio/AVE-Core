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

            # Inject an edge whose target is a syntactically-valid 6-char id
            # that does not appear in claims.jsonl.
            dep_path = tmp_index / "depends-on.jsonl"
            orphan_target = "zzz999"
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


if __name__ == "__main__":
    unittest.main()

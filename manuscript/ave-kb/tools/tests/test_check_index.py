"""Tests for the extended ``verify-kb-metadata.py`` verifier — index checks.

Exercises the verifier's behavioral checks (well-formed, freshness,
referential integrity, quality-block integrity) against the hand-built
synthetic fixture under ``tests/fixtures/mini-kb/``. The fixture is copied
to a per-class tempdir at setup so mutating tests cannot pollute the
committed fixture even on failure; ``refresh-kb-metadata`` is run against the
copy once to bring its ``.index/`` and derived solidity content to canonical
shape before tests start.

Run from the repo root::

    cd /Users/benn/projects/AVE-Umbrella/AVE-Core/manuscript/ave-kb/tools
    python -m unittest tests.test_check_index

Tests are fully independent of live KB state. Nothing here reads or asserts
on ``manuscript/ave-kb/`` proper; the live KB's "does it currently pass"
status is covered by ``make verify-kb-metadata``.
"""

from __future__ import annotations

import json
import re
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

_FIXTURE_SRC = _THIS_DIR / "fixtures" / "mini-kb"
_CHECK_SCRIPT = _TOOLS_DIR / "verify-kb-metadata.py"
_REFRESH_SCRIPT = _TOOLS_DIR / "refresh-kb-metadata.py"


def _run_checker(
    kb_root: Path, extra_args: list[str] | None = None
) -> subprocess.CompletedProcess:
    cmd = [sys.executable, str(_CHECK_SCRIPT), "--kb-root", str(kb_root)]
    if extra_args:
        cmd.extend(extra_args)
    return subprocess.run(
        cmd, capture_output=True, text=True, check=False
    )


def _run_refresh(kb_root: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(_REFRESH_SCRIPT), "--kb-root", str(kb_root)],
        capture_output=True, text=True, check=False,
    )


def _materialize_fixture(parent: Path) -> Path:
    """Copy the committed fixture into ``parent`` and refresh it.

    Returns the path to the materialized fixture KB root.
    """
    kb = parent / "mini-kb"
    shutil.copytree(_FIXTURE_SRC, kb)
    result = _run_refresh(kb)
    if result.returncode != 0:
        raise AssertionError(
            f"refresh-kb-metadata failed against fixture copy: "
            f"stdout={result.stdout}\nstderr={result.stderr}"
        )
    return kb


class TestCheckIndex(unittest.TestCase):
    """Verifier extended-check behavior on the fixture KB.

    A single per-class fixture tempdir is materialized once. Tests that
    mutate a file in the tempdir restore it via try/finally so each test in
    the class sees the fresh canonical state.
    """

    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls._tmp.cleanup)
        cls.kb_root = _materialize_fixture(Path(cls._tmp.name))
        cls.index_dir = cls.kb_root / ".index"

    def _backup_index_file(self, name: str) -> bytes:
        return (self.index_dir / name).read_bytes()

    def _restore_index_file(self, name: str, content: bytes) -> None:
        (self.index_dir / name).write_bytes(content)

    def test_index_line_reports_node_type_breakdown(self):
        """The [index] summary reports a claims / invariants / axioms breakdown.

        Asserts the line's *format* — content-independent — not the specific
        node counts.
        """
        result = _run_checker(self.kb_root)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertRegex(
            result.stdout,
            r"\d+ nodes: \d+ claims / \d+ experiments / "
            r"\d+ invariants / \d+ axioms",
        )

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
                shutil.copy2(self.index_dir / short, tmp_index / short)

            # Inject an edge to a real INVARIANT node but mislabel its kind.
            dep_path = tmp_index / "depends-on.jsonl"
            existing = dep_path.read_bytes().decode("utf-8")
            first_source = existing.split("\n")[0].split('"source": "')[1].split('"')[0]
            extra = (
                '{"source": "' + first_source + '", "target": "INVARIANT-S2"'
                ', "relation": "depends", "target_kind": "claim"'
                ', "target_solidity_recorded": null, "strength": null'
                ', "context": null}\n'
            )
            dep_path.write_bytes(existing.encode("utf-8") + extra.encode("utf-8"))

            result = _run_checker(
                self.kb_root, ["--index-dir", str(tmp_index)]
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("referential-integrity", result.stdout)
            self.assertIn("INVARIANT-S2", result.stdout)

    def test_check_detects_stale_jsonl(self):
        """A truncated cites.jsonl fails freshness with the refresh hint."""
        name = "cites.jsonl"
        original = self._backup_index_file(name)
        try:
            text = original.decode("utf-8")
            lines = [ln for ln in text.split("\n") if ln]
            # Drop the first line (the fixture has too few rows for 5).
            truncated = "\n".join(lines[1:]) + "\n"
            (self.index_dir / name).write_bytes(truncated.encode("utf-8"))

            result = _run_checker(self.kb_root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn(name, result.stdout)
            # Freshness failures must surface the refresh-fixable hint.
            self.assertIn("make refresh-kb-metadata", result.stdout)
        finally:
            self._restore_index_file(name, original)

    def test_check_detects_missing_jsonl(self):
        """A renamed JSONL file fails with a clear 'missing' message."""
        name = "strengthen-by.jsonl"
        src = self.index_dir / name
        dst = self.index_dir / (name + ".bak")
        src.rename(dst)
        try:
            result = _run_checker(self.kb_root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("missing", result.stdout.lower())
            self.assertIn(name, result.stdout)
            self.assertIn("make refresh-kb-metadata", result.stdout)
        finally:
            dst.rename(src)

    def test_check_detects_malformed_jsonl(self):
        """Appending a non-JSON line fails the well-formed check (not refresh-fixable)."""
        name = "claims.jsonl"
        original = self._backup_index_file(name)
        try:
            (self.index_dir / name).write_bytes(original + b"not-a-json\n")
            result = _run_checker(self.kb_root)
            self.assertNotEqual(result.returncode, 0)
            output = result.stdout.lower()
            # The malformed-line block uses "well-formed JSON" phrasing.
            self.assertTrue(
                "well-formed" in output or "json" in output,
                f"expected JSON well-formedness mention in output: {result.stdout}",
            )
            self.assertIn(name, result.stdout)
        finally:
            self._restore_index_file(name, original)

    def test_check_detects_referential_integrity_violation(self):
        """A synthetic depends-on edge to a nonexistent target fails ref-integrity.

        Uses ``--index-dir`` to point at a temp index tree so the fixture
        ``.index/`` is never touched. Copies the fixture index files in, then
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
                shutil.copy2(self.index_dir / short, tmp_index / short)

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

            result = _run_checker(
                self.kb_root, ["--index-dir", str(tmp_index)]
            )
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("referential-integrity", result.stdout)
            self.assertIn(orphan_target, result.stdout)

    def test_check_detects_stale_solidity_line(self):
        """Hand-editing a solidity value fails the freshness check.

        Picks the mutation target dynamically: the first ``- solidity: 0.NN
        (...)`` line in the fixture's ``common/`` register. Replaces its
        numeric value with a clearly-wrong one, runs the verifier, expects a
        refresh-fixable freshness failure, then restores the file.
        """
        cq = self.kb_root / "common" / "claim-quality.md"
        original = cq.read_bytes()
        try:
            text = original.decode("utf-8")
            m = re.search(r"^- solidity: (0\.\d+) \(", text, flags=re.MULTILINE)
            self.assertIsNotNone(m, "no `- solidity: 0.NN (` line in fixture")
            current = float(m.group(1))
            # A value clearly distinct from the real one — far enough that the
            # 2-dp freshness comparison cannot treat it as equal.
            wrong = "0.99" if current < 0.50 else "0.01"
            stale = text[: m.start(1)] + wrong + text[m.end(1) :]
            self.assertNotEqual(stale, text)
            cq.write_bytes(stale.encode("utf-8"))

            result = _run_checker(self.kb_root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("solidity freshness", result.stdout)
            self.assertIn("make refresh-kb-metadata", result.stdout)
        finally:
            cq.write_bytes(original)

    def test_check_detects_stale_depends_on_annotation(self):
        """A wrong (solidity X) annotation fails the freshness check.

        Picks the mutation target dynamically: the first numeric ``(solidity
        0.NN)`` depends-on annotation in the fixture's root register.
        """
        cq = self.kb_root / "claim-quality.md"
        original = cq.read_bytes()
        try:
            text = original.decode("utf-8")
            m = re.search(r"\(solidity (0\.\d+)\)", text)
            self.assertIsNotNone(m, "no numeric (solidity 0.NN) annotation in fixture")
            current = float(m.group(1))
            wrong = "0.99" if current < 0.50 else "0.01"
            stale = text[: m.start(1)] + wrong + text[m.end(1) :]
            self.assertNotEqual(stale, text)
            cq.write_bytes(stale.encode("utf-8"))

            result = _run_checker(self.kb_root)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("solidity freshness", result.stdout)
        finally:
            cq.write_bytes(original)

    def test_solidity_cycle_check_function(self):
        """check_solidity_cycle reports cycle members on a cyclic graph.

        Synthetic two-node cycle — does not touch any KB state.
        """
        check = _load_checker_module()
        lib = sys.modules["kb_index_lib"]

        def mk(cid, deps):
            return lib.ClaimEntry(
                id=cid, title=cid, canonical_path="t/claim-quality.md",
                canonical_anchor=cid, confidence=0.8, solidity=None,
                build_status=None, rationale="", strengthen_by=(),
                depends_on=tuple(
                    lib.DependsOnEdge(cid, d, "depends", "claim", None, None, None)
                    for d in deps
                ),
            )

        cyclic = lib.KbState(
            claim_entries=(mk("clm-aaaaaa", ["clm-bbbbbb"]),
                           mk("clm-bbbbbb", ["clm-aaaaaa"])),
            leaves=(), indexes=(), framework_nodes=(), experiments=(),
        )
        members = check.check_solidity_cycle(cyclic)
        self.assertEqual(set(members), {"clm-aaaaaa", "clm-bbbbbb"})

        acyclic = lib.KbState(
            claim_entries=(mk("clm-aaaaaa", []),
                           mk("clm-bbbbbb", ["clm-aaaaaa"])),
            leaves=(), indexes=(), framework_nodes=(), experiments=(),
        )
        self.assertEqual(check.check_solidity_cycle(acyclic), [])


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
    Fully independent of any KB state.
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

    def test_orphan_block_fails_full_verifier(self):
        """An orphan block in a register fails the end-to-end verifier.

        Appends an orphan `### Quality` block to the fixture's root
        claim-quality.md (in the per-class tempdir copy), runs the verifier,
        expects a non-zero exit naming the file, then restores. Operates
        purely on the tempdir; the committed fixture is never touched.
        """
        # Re-use the per-class fixture from TestCheckIndex: a fresh tempdir
        # and refresh would also work, but the fixture is already canonical.
        with tempfile.TemporaryDirectory() as tmp:
            kb = _materialize_fixture(Path(tmp))
            cq = kb / "claim-quality.md"
            orphan = (
                b"\n\n---\n\n### Quality\n- confidence: *pending*\n"
                b"- solidity: *pending*\n- rationale: *pending*\n"
                b"- strengthen-by:\n  - *pending*\n"
            )
            cq.write_bytes(cq.read_bytes() + orphan)
            result = _run_checker(kb)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("orphan/malformed", result.stdout)
            self.assertIn("claim-quality.md", result.stdout)


def _read_jsonl(path: Path) -> list[dict]:
    """Parse a JSONL file into a list of dicts (skipping blank lines)."""
    return [
        json.loads(ln)
        for ln in path.read_text(encoding="utf-8").splitlines()
        if ln.strip()
    ]


# A minimal valid experiment leaf, parameterized so negative variants can
# perturb a single field. Frontmatter mirrors common/exp-bench.md.
_EXP_LEAF_TEMPLATE = """\
[↑ Mini-KB Common](index.md)

<!-- kb-frontmatter
kind: experiment
{fields}
-->

# {title}

Synthetic experiment leaf body.
"""


def _exp_leaf(
    *,
    exp_id: str = "exp-neg001",
    status: str = "run",
    strengthens: str = "  - clm-gg7777: 0.50",
    extra: str = "",
    title: str = "Negative Experiment",
) -> str:
    fields = [f"exp-id: {exp_id}", f"status: {status}"]
    if extra:
        fields.append(extra)
    fields.append("strengthens:")
    body = "\n".join(fields)
    if strengthens:
        body += "\n" + strengthens
    return _EXP_LEAF_TEMPLATE.format(fields=body, title=title)


class TestExperimentEndToEnd(unittest.TestCase):
    """End-to-end: the experiment node + strengthens edge + rescue, on the
    fixture-with-experiment, through the real refresh -> verify pipeline.

    A fresh fixture is materialized (and refreshed) per class so the emitted
    ``.index/`` reflects the committed ``common/exp-bench.md`` leaf.
    """

    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls._tmp.cleanup)
        cls.kb_root = _materialize_fixture(Path(cls._tmp.name))
        cls.index_dir = cls.kb_root / ".index"
        cls.claims = _read_jsonl(cls.index_dir / "claims.jsonl")
        cls.edges = _read_jsonl(cls.index_dir / "depends-on.jsonl")
        cls.by_id = {r["id"]: r for r in cls.claims if "id" in r}

    def test_experiment_node_emitted_into_claims_jsonl(self):
        """The experiment is a 6-field, schema-ordered claims.jsonl node."""
        exps = [r for r in self.claims if r["node_type"] == "experiment"]
        self.assertEqual(len(exps), 1)
        rec = exps[0]
        self.assertEqual(
            list(rec.keys()),
            [
                "node_type",
                "id",
                "title",
                "canonical_path",
                "canonical_anchor",
                "status",
            ],
        )
        self.assertEqual(rec["id"], "exp-bench1")
        self.assertEqual(rec["canonical_path"], "common/exp-bench.md")
        self.assertEqual(rec["status"], "run")
        # title + anchor must come from the leaf's `##` heading — regression
        # guard for _experiment_heading (KB leaves use `##`, not `#`).
        self.assertEqual(rec["title"], "Synthetic Bench Experiment")
        self.assertEqual(rec["canonical_anchor"], "synthetic-bench-experiment")

    def test_claims_jsonl_sorted_experiment_after_claims_before_invariants(self):
        """Sort key (node_type, id): experiments sit after claims, before
        invariants (ASCII: axiom < claim < experiment < invariant)."""
        keys = [(r["node_type"], r["id"]) for r in self.claims]
        self.assertEqual(keys, sorted(keys))
        order = [r["node_type"] for r in self.claims]
        # The experiment must appear after the last claim and before the
        # first invariant.
        last_claim = max(i for i, t in enumerate(order) if t == "claim")
        exp_idx = order.index("experiment")
        first_invariant = min(
            i for i, t in enumerate(order) if t == "invariant"
        )
        self.assertLess(last_claim, exp_idx)
        self.assertLess(exp_idx, first_invariant)

    def test_strengthens_edge_in_depends_on_jsonl(self):
        """The strengthens edge has the schema's relation/kind/strength shape."""
        edges = [
            e
            for e in self.edges
            if e["source"] == "exp-bench1" and e["target"] == "clm-gg7777"
        ]
        self.assertEqual(len(edges), 1)
        e = edges[0]
        self.assertEqual(e["relation"], "strengthens")
        self.assertEqual(e["target_kind"], "claim")
        self.assertEqual(e["strength"], 0.80)
        self.assertIsNone(e["target_solidity_recorded"])

    def test_rescued_claim_reflects_run_experiment(self):
        """clm-gg7777: derivation pending, experimental 0.80, final 0.80."""
        rec = self.by_id["clm-gg7777"]
        self.assertIsNone(rec["derivation_solidity"])
        self.assertEqual(rec["experimental_solidity"], 0.80)
        self.assertEqual(rec["solidity"], 0.80)
        self.assertEqual(rec["build_band"], "ok-with-caveats")

    def test_rescued_solidity_written_to_claim_quality(self):
        """The rescued value is written back to common/claim-quality.md."""
        cq = (self.kb_root / "common" / "claim-quality.md").read_text(
            encoding="utf-8"
        )
        block = cq.split("clm-gg7777")[1]
        m = re.search(r"^- solidity: (\S+)", block, flags=re.MULTILINE)
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "0.80")

    def test_pipeline_passes_with_experiment(self):
        """The full refresh -> verify pipeline exits 0 on the fixture."""
        result = _run_checker(self.kb_root)
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_refresh_is_deterministic(self):
        """A second refresh writes byte-identical index files (idempotent)."""
        before = {
            p.name: p.read_bytes() for p in sorted(self.index_dir.glob("*.jsonl"))
        }
        result = _run_refresh(self.kb_root)
        self.assertEqual(result.returncode, 0, result.stderr)
        after = {
            p.name: p.read_bytes() for p in sorted(self.index_dir.glob("*.jsonl"))
        }
        self.assertEqual(before, after)


class TestExperimentLeafRejection(unittest.TestCase):
    """Negative coverage: malformed experiment leaves are rejected.

    In-memory cases call ``parse_experiment_leaf`` directly for a precise
    ``ExperimentLeafError`` assertion; the bad-target and pending-status cases
    run the full pipeline against a fixture copy carrying the bad leaf.
    """

    def _parse(self, leaf_text: str):
        lib = sys.modules.get("kb_index_lib")
        if lib is None:
            import kb_index_lib as lib  # noqa: F811
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            leaf = root / "exp-bad.md"
            leaf.write_text(leaf_text, encoding="utf-8")
            return lib.parse_experiment_leaf(leaf, root), lib

    def test_claim_bearing_experiment_leaf_rejected(self):
        """(a) An experiment leaf that also carries claims: is rejected."""
        text = _exp_leaf(extra="claims: [clm-aa1111]")
        _, lib = self._parse(_exp_leaf())  # warm import
        with self.assertRaises(lib.ExperimentLeafError):
            self._parse(text)

    def test_bad_exp_id_format_rejected(self):
        """(b) A malformed exp-id (wrong shape) is rejected."""
        text = _exp_leaf(exp_id="exp-TOOLONG9")
        _, lib = self._parse(_exp_leaf())
        with self.assertRaises(lib.ExperimentLeafError):
            self._parse(text)

    def test_bad_status_rejected(self):
        """(c) A status outside {run, pending} is rejected."""
        text = _exp_leaf(status="halfway")
        _, lib = self._parse(_exp_leaf())
        with self.assertRaises(lib.ExperimentLeafError):
            self._parse(text)

    def test_strengthens_target_not_a_real_claim_fails_verify(self):
        """(d) A strengthens edge to a non-existent claim id fails the
        pipeline (referential integrity / orphan target)."""
        with tempfile.TemporaryDirectory() as tmp:
            kb = _materialize_fixture(Path(tmp))
            bad = _exp_leaf(
                exp_id="exp-orph01",
                strengthens="  - clm-zzz999: 1.0",
                title="Orphan-Target Experiment",
            )
            (kb / "common" / "exp-orphan.md").write_text(bad, encoding="utf-8")
            _run_refresh(kb)
            result = _run_checker(kb)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("clm-zzz999", result.stdout)

    def test_pending_experiment_contributes_nothing(self):
        """(e) A status:pending experiment confers no experimental solidity:
        its target stays pending (derivation pending, no run experiment)."""
        with tempfile.TemporaryDirectory() as tmp:
            kb = _materialize_fixture(Path(tmp))
            # Replace the run experiment with a pending one targeting the same
            # pending-derivation claim clm-gg7777.
            exp = kb / "common" / "exp-bench.md"
            exp.write_text(
                _exp_leaf(
                    exp_id="exp-bench1",
                    status="pending",
                    strengthens="  - clm-gg7777: 0.80",
                    title="Pending Bench Experiment",
                ),
                encoding="utf-8",
            )
            # clm-gg7777 must go back to *pending* on disk for refresh to be a
            # clean no-op-or-rewrite; let refresh author the canonical value.
            result = _run_refresh(kb)
            self.assertEqual(result.returncode, 0, result.stderr)
            claims = _read_jsonl(kb / ".index" / "claims.jsonl")
            gg = next(r for r in claims if r.get("id") == "clm-gg7777")
            self.assertIsNone(gg["experimental_solidity"])
            self.assertIsNone(gg["derivation_solidity"])
            self.assertIsNone(gg["solidity"])
            # And the pipeline still passes (pending is valid, not an error).
            self.assertEqual(_run_checker(kb).returncode, 0)


# A leaf that REFERENCES an experiment via the optional `experiments:` field
# (the analog of `claims:` for claims). Parameterized so negative variants can
# perturb the primary field or the experiments list. Mirrors the real
# bench-protocols.md fixture leaf.
_REF_LEAF_TEMPLATE = """\
[↑ Mini-KB Common](index.md)

<!-- kb-frontmatter
kind: leaf
{primary}
experiments: [{experiments}]
-->

## {title}

Synthetic by-methodology leaf referencing an experiment.
"""


def _ref_leaf(
    *,
    primary: str = 'no-claim: "references the bench experiment only"',
    experiments: str = "exp-bench1",
    title: str = "Reference Leaf",
) -> str:
    return _REF_LEAF_TEMPLATE.format(
        primary=primary, experiments=experiments, title=title
    )


class TestExperimentsReferenceEndToEnd(unittest.TestCase):
    """End-to-end for the `experiments:` reference field (feature 2a).

    Exercises the genuinely-new path — a leaf REFERENCING an experiment it does
    not own — through the real refresh -> verify pipeline on the committed
    fixture (which carries common/bench-protocols.md referencing exp-bench1).
    """

    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        cls.addClassCleanup(cls._tmp.cleanup)
        cls.kb_root = _materialize_fixture(Path(cls._tmp.name))
        cls.index_dir = cls.kb_root / ".index"

    def test_referencing_leaf_parses_experiments_ref(self):
        """The leaf's experiments_ref parses to ("exp-bench1",)."""
        lib = sys.modules.get("kb_index_lib")
        if lib is None:
            import kb_index_lib as lib  # noqa: F811
        leaf = lib.parse_leaf(
            self.kb_root / "common" / "bench-protocols.md", self.kb_root
        )
        self.assertIsNotNone(leaf)
        self.assertEqual(leaf.experiments_ref, ("exp-bench1",))
        # The reference is additive — the leaf is still a no-claim leaf.
        self.assertEqual(leaf.claims, ())
        self.assertIsNotNone(leaf.no_claim_reason)

    def test_common_index_subtree_experiments_lists_exp(self):
        """After refresh, common/ index subtree-experiments lists exp-bench1."""
        agg = _read_jsonl(self.index_dir / "subtree-aggregates.jsonl")
        common = next(r for r in agg if r["node_path"] == "common/index.md")
        self.assertEqual(common["subtree_experiments"], ["exp-bench1"])

    def test_subtree_experiments_is_owned_only_not_reference(self):
        """The aggregate counts the OWNED experiment, not the referencing leaf.

        bench-protocols.md REFERENCES exp-bench1 but exp-bench.md OWNS it; the
        single entry comes from ownership, so a reference adds nothing beyond
        what ownership already contributes (owned-only aggregation).
        """
        agg = _read_jsonl(self.index_dir / "subtree-aggregates.jsonl")
        for rec in agg:
            # No duplication: exp-bench1 appears at most once per node.
            self.assertEqual(
                rec["subtree_experiments"].count("exp-bench1"),
                len(rec["subtree_experiments"]),
            )

    def test_pipeline_passes_with_reference_leaf(self):
        """The full refresh -> verify pipeline exits 0 (byte-green)."""
        result = _run_checker(self.kb_root)
        self.assertEqual(result.returncode, 0, result.stdout)


class TestExperimentsReferenceRejection(unittest.TestCase):
    """Negative coverage for the `experiments:` reference field (feature 2a).

    Each case must make verify FAIL with a clear message. The orphan and
    kind-mismatch cases run the full pipeline against a fixture copy carrying
    the bad leaf; the exclusivity case calls parse_experiment_leaf directly
    for a precise ExperimentLeafError assertion (and is also exercised
    end-to-end). None pollute the committed fixture with broken files.
    """

    def test_orphan_experiment_reference_fails_verify(self):
        """(a) experiments: [exp-zzzzzz] — no such experiment → orphan failure."""
        with tempfile.TemporaryDirectory() as tmp:
            kb = _materialize_fixture(Path(tmp))
            (kb / "common" / "ref-orphan.md").write_text(
                _ref_leaf(experiments="exp-zzzzzz", title="Orphan Ref Leaf"),
                encoding="utf-8",
            )
            _run_refresh(kb)
            result = _run_checker(kb)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("exp-zzzzzz", result.stdout)
            self.assertIn("experiments:", result.stdout)

    def test_reference_to_claim_id_fails_verify(self):
        """(b) experiments: [clm-gg7777] — id resolves to a CLAIM → kind mismatch."""
        with tempfile.TemporaryDirectory() as tmp:
            kb = _materialize_fixture(Path(tmp))
            (kb / "common" / "ref-claim.md").write_text(
                _ref_leaf(experiments="clm-gg7777", title="Claim-Ref Leaf"),
                encoding="utf-8",
            )
            _run_refresh(kb)
            result = _run_checker(kb)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("clm-gg7777", result.stdout)
            self.assertIn("claim", result.stdout.lower())

    def test_experiment_leaf_with_experiments_ref_rejected(self):
        """(c) An exp-id leaf that ALSO carries experiments: is rejected.

        Direct parse assertion for the precise ExperimentLeafError, plus an
        end-to-end check that the pipeline fails.
        """
        lib = sys.modules.get("kb_index_lib")
        if lib is None:
            import kb_index_lib as lib  # noqa: F811
        bad = _exp_leaf(
            exp_id="exp-bench1",
            strengthens="  - clm-gg7777: 0.80",
            extra="experiments: [exp-bench1]",
            title="Self-Referencing Experiment",
        )
        with tempfile.TemporaryDirectory() as tmp:
            leaf = Path(tmp) / "exp-bad.md"
            leaf.write_text(bad, encoding="utf-8")
            with self.assertRaises(lib.ExperimentLeafError):
                lib.parse_experiment_leaf(leaf, Path(tmp))

        with tempfile.TemporaryDirectory() as tmp:
            kb = _materialize_fixture(Path(tmp))
            (kb / "common" / "exp-bench.md").write_text(bad, encoding="utf-8")
            _run_refresh(kb)
            result = _run_checker(kb)
            self.assertNotEqual(result.returncode, 0)

    def test_subtree_experiments_drift_fails_verify(self):
        """A hand-edited (wrong) subtree-experiments value fails consistency.

        Confirms the verify checker independently recomputes the owned union
        rather than trusting the declared field — the dual-compute guard.
        """
        with tempfile.TemporaryDirectory() as tmp:
            kb = _materialize_fixture(Path(tmp))
            idx = kb / "common" / "index.md"
            text = idx.read_text(encoding="utf-8")
            self.assertIn("subtree-experiments: [exp-bench1]", text)
            idx.write_text(
                text.replace(
                    "subtree-experiments: [exp-bench1]",
                    "subtree-experiments: []",
                ),
                encoding="utf-8",
            )
            result = _run_checker(kb)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("subtree-experiments drift", result.stdout)


def _load_checker_module():
    """Import verify-kb-metadata.py as a module (its name has a hyphen)."""
    import importlib.util

    if "_verify_kb_metadata_mod" in sys.modules:
        return sys.modules["_verify_kb_metadata_mod"]
    spec = importlib.util.spec_from_file_location(
        "_verify_kb_metadata_mod", str(_CHECK_SCRIPT)
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["_verify_kb_metadata_mod"] = mod
    spec.loader.exec_module(mod)
    return mod


if __name__ == "__main__":
    unittest.main()

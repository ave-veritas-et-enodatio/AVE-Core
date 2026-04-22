"""
Unit tests for the claim-graph validator.

Covers each of the 4 structural checks (schema, label, engine, parity) with
both happy-path and failure fixtures, plus an end-to-end assertion that the
live manifest has zero critical findings (its quality gate for CI).

Reference: src/scripts/claim_graph_validator.py,
           manuscript/predictions.yaml
"""

from __future__ import annotations

from scripts.claim_graph_validator import (
    ALLOWED_TYPES,
    check_engine,
    check_labels,
    check_living_reference_parity,
    check_readme_parity,
    check_schema,
    collect_constants_symbols,
    collect_manuscript_labels,
    extract_living_reference_prediction_rows,
    load_manifest,
    run,
    MANIFEST_PATH,
    REPO_ROOT,
)


def _manifest(entries: list[dict]) -> dict:
    return {"version": 1, "predictions": entries}


# ───────────────────────────────────────────────────────────────────────────
# check_schema
# ───────────────────────────────────────────────────────────────────────────
class TestSchema:
    def test_valid_entry_no_findings(self):
        m = _manifest(
            [
                {
                    "id": "P01",
                    "name": "test",
                    "type": "derived_prediction",
                    "derivation_label": "ch:test",
                }
            ]
        )
        assert check_schema(m) == []

    def test_missing_required_field_fires(self):
        m = _manifest([{"id": "P01", "name": "missing-type", "derivation_label": "ch:x"}])
        findings = check_schema(m)
        # At least one finding must flag the missing-field violation; may
        # also fire the type-invalid check since type=None ∉ ALLOWED_TYPES.
        missing_findings = [f for f in findings if "missing required fields" in f.message.lower()]
        assert len(missing_findings) == 1
        assert missing_findings[0].severity == "critical"

    def test_invalid_type_fires(self):
        m = _manifest(
            [
                {
                    "id": "P01",
                    "name": "x",
                    "type": "phenomenology",  # not in ALLOWED_TYPES
                    "derivation_label": "ch:x",
                }
            ]
        )
        findings = [f for f in check_schema(m) if "Invalid type" in f.message]
        assert len(findings) == 1
        assert findings[0].severity == "critical"

    def test_duplicate_ids_fires(self):
        m = _manifest(
            [
                {
                    "id": "P01",
                    "name": "a",
                    "type": "derived_prediction",
                    "derivation_label": "ch:x",
                },
                {
                    "id": "P01",
                    "name": "b",
                    "type": "derived_prediction",
                    "derivation_label": "ch:y",
                },
            ]
        )
        findings = [f for f in check_schema(m) if "Duplicate" in f.message]
        assert len(findings) == 1


# ───────────────────────────────────────────────────────────────────────────
# check_labels
# ───────────────────────────────────────────────────────────────────────────
class TestLabels:
    def test_resolved_label_no_findings(self):
        m = _manifest(
            [
                {
                    "id": "P01",
                    "name": "x",
                    "type": "derived_prediction",
                    "derivation_label": "ch:real",
                }
            ]
        )
        findings = check_labels(m, labels={"ch:real", "ch:other"})
        assert findings == []

    def test_unresolved_label_fires(self):
        m = _manifest(
            [
                {
                    "id": "P01",
                    "name": "x",
                    "type": "derived_prediction",
                    "derivation_label": "ch:missing",
                }
            ]
        )
        findings = check_labels(m, labels={"ch:other"})
        assert len(findings) == 1
        assert findings[0].severity == "critical"
        assert "ch:missing" in findings[0].message

    def test_unresolved_equation_label_is_warn(self):
        m = _manifest(
            [
                {
                    "id": "P01",
                    "name": "x",
                    "type": "derived_prediction",
                    "derivation_label": "ch:real",
                    "derivation_equation": "eq:missing",
                }
            ]
        )
        findings = check_labels(m, labels={"ch:real"})
        assert len(findings) == 1
        assert findings[0].severity == "warn"


# ───────────────────────────────────────────────────────────────────────────
# check_engine
# ───────────────────────────────────────────────────────────────────────────
class TestEngine:
    def test_matching_symbol_and_value_no_findings(self):
        m = _manifest(
            [
                {
                    "id": "P01",
                    "name": "x",
                    "type": "derived_prediction",
                    "derivation_label": "ch:x",
                    "constants_py_symbol": "Z_0",
                    "predicted_value": 376.7303,
                }
            ]
        )
        findings = check_engine(m, constants={"Z_0": 376.730313668})
        assert findings == []

    def test_missing_symbol_fires(self):
        m = _manifest(
            [
                {
                    "id": "P01",
                    "name": "x",
                    "type": "derived_prediction",
                    "derivation_label": "ch:x",
                    "constants_py_symbol": "BOGUS",
                    "predicted_value": 1.0,
                }
            ]
        )
        findings = check_engine(m, constants={"Z_0": 377.0})
        assert len(findings) == 1
        assert findings[0].severity == "critical"
        assert "BOGUS" in findings[0].message

    def test_numeric_drift_fires(self):
        m = _manifest(
            [
                {
                    "id": "P01",
                    "name": "x",
                    "type": "derived_prediction",
                    "derivation_label": "ch:x",
                    "constants_py_symbol": "Z_0",
                    "predicted_value": 400.0,  # way off
                }
            ]
        )
        findings = check_engine(m, constants={"Z_0": 376.730}, rtol=1e-5)
        assert len(findings) == 1
        assert findings[0].severity == "critical"
        assert "disagrees" in findings[0].message

    def test_symbol_without_value_is_info(self):
        m = _manifest(
            [
                {
                    "id": "P01",
                    "name": "x",
                    "type": "derived_prediction",
                    "derivation_label": "ch:x",
                    "constants_py_symbol": "Z_0",
                    # no predicted_value
                }
            ]
        )
        findings = check_engine(m, constants={"Z_0": 376.730})
        assert len(findings) == 1
        assert findings[0].severity == "info"

    def test_entry_without_symbol_skipped(self):
        m = _manifest(
            [
                {
                    "id": "P01",
                    "name": "x",
                    "type": "derived_prediction",
                    "derivation_label": "ch:x",
                }
            ]
        )
        assert check_engine(m, constants={}) == []


# ───────────────────────────────────────────────────────────────────────────
# End-to-end: live manifest + live repo
# ───────────────────────────────────────────────────────────────────────────
class TestLiveManifest:
    def test_manifest_loads(self):
        m = load_manifest(MANIFEST_PATH)
        assert "predictions" in m
        assert isinstance(m["predictions"], list)
        assert len(m["predictions"]) > 0

    def test_manifest_schema_clean(self):
        m = load_manifest(MANIFEST_PATH)
        findings = check_schema(m)
        criticals = [f for f in findings if f.severity == "critical"]
        assert criticals == [], "Live manifest has schema violations:\n" + "\n".join(
            f"  [{f.severity}] P={f.entry_id} {f.message}" for f in criticals
        )

    def test_manifest_labels_resolve(self):
        m = load_manifest(MANIFEST_PATH)
        labels = collect_manuscript_labels(REPO_ROOT)
        findings = check_labels(m, labels=labels)
        criticals = [f for f in findings if f.severity == "critical"]
        assert criticals == [], "Live manifest has unresolved derivation_labels:\n" + "\n".join(
            f"  P={f.entry_id} {f.message}" for f in criticals
        )

    def test_manifest_engine_agrees(self):
        m = load_manifest(MANIFEST_PATH)
        constants = collect_constants_symbols()
        findings = check_engine(m, constants=constants)
        criticals = [f for f in findings if f.severity == "critical"]
        assert criticals == [], "Live manifest disagrees with engine:\n" + "\n".join(
            f"  P={f.entry_id} {f.message}" for f in criticals
        )

    def test_readme_parity(self):
        m = load_manifest(MANIFEST_PATH)
        findings = check_readme_parity(m)
        warns = [f for f in findings if f.severity == "warn"]
        # Parity is WARN level — if a README row has no entry it should be
        # flagged. Live assertion: zero such findings (every public claim
        # is tracked in the manifest).
        assert warns == [], "README master table has rows with no manifest entry:\n" + "\n".join(
            f"  {f.message}" for f in warns
        )

    def test_living_reference_parity(self):
        m = load_manifest(MANIFEST_PATH)
        findings = check_living_reference_parity(m)
        warns = [f for f in findings if f.severity == "warn"]
        # Same semantics as README parity, but checks LIVING_REFERENCE.md
        # master table. LR may split bundled README rows (e.g., rows 11/12
        # appear separately for Δ(1600) and Δ(1900) while the manifest
        # bundles as P11_12); the check accepts both via range-inclusion.
        assert warns == [], "LIVING_REFERENCE master table has rows with no manifest entry:\n" + "\n".join(
            f"  {f.message}" for f in warns
        )

    def test_living_reference_parser_finds_rows(self):
        # Sanity: the parser returns a non-empty list on the live doc.
        rows = extract_living_reference_prediction_rows()
        assert len(rows) >= 40, f"Expected ≥40 LIVING_REFERENCE prediction rows, got {len(rows)}"
        # Row ids should be numeric or ranges; names non-empty.
        for row_id, name in rows:
            assert row_id, "row_id should not be empty"
            assert name, "name should not be empty"

    def test_all_entries_use_allowed_types(self):
        m = load_manifest(MANIFEST_PATH)
        for entry in m["predictions"]:
            assert entry["type"] in ALLOWED_TYPES, f"Entry {entry['id']} uses unknown type: {entry['type']}"

    def test_all_entries_have_unique_ids(self):
        m = load_manifest(MANIFEST_PATH)
        ids = [e["id"] for e in m["predictions"]]
        assert len(ids) == len(set(ids)), f"Duplicate IDs: {ids}"


class TestOrchestration:
    def test_run_with_all_checks(self):
        findings = run()
        # Same assertion as above but via the top-level `run()` entry point.
        criticals = [f for f in findings if f.severity == "critical"]
        assert criticals == [], "run() reports critical findings on live manifest:\n" + "\n".join(
            f"  [{f.check}] P={f.entry_id} {f.message}" for f in criticals
        )

    def test_run_selective_check(self):
        findings = run(checks=["schema"])
        # schema-only on a valid manifest should have no criticals
        criticals = [f for f in findings if f.severity == "critical"]
        assert criticals == []

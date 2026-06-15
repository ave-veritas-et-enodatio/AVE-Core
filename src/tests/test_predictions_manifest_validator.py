"""
Unit tests for the predictions-manifest validator.

Covers each of the 4 structural checks (schema, label, engine, parity) with
both happy-path and failure fixtures, plus an end-to-end assertion that the
live manifest has zero critical findings (its quality gate for CI).

Reference: src/scripts/predictions_manifest_validator.py,
           manuscript/predictions.yaml
"""

from scripts.predictions_manifest_validator import (
    ALLOWED_TYPES,
    MANIFEST_PATH,
    REPO_ROOT,
    check_axioms,
    check_bridge,
    check_engine,
    check_labels,
    check_living_reference_parity,
    check_readme_parity,
    check_schema,
    collect_constants_symbols,
    collect_dependency_edges,
    collect_manuscript_labels,
    collect_spine_nodes,
    derive_axioms_used,
    extract_living_reference_prediction_rows,
    load_manifest,
    run,
)


def _manifest(entries: list[dict]) -> dict:
    return {"version": 1, "predictions": entries}


# ───────────────────────────────────────────────────────────────────────────
# check_schema
# ───────────────────────────────────────────────────────────────────────────
class TestSchema:
    def test_valid_entry_no_findings(self) -> None:
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

    def test_missing_required_field_fires(self) -> None:
        m = _manifest([{"id": "P01", "name": "missing-type", "derivation_label": "ch:x"}])
        findings = check_schema(m)
        # At least one finding must flag the missing-field violation; may
        # also fire the type-invalid check since type=None ∉ ALLOWED_TYPES.
        missing_findings = [f for f in findings if "missing required fields" in f.message.lower()]
        assert len(missing_findings) == 1
        assert missing_findings[0].severity == "critical"

    def test_invalid_type_fires(self) -> None:
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

    def test_duplicate_ids_fires(self) -> None:
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

    def test_well_formed_ids_pass(self) -> None:
        # P01 (shipped), P11_12 (range), P_A034_x (evolved category) all valid.
        for good in ("P01", "P11_12", "P_A034_solar_flare", "P_phase5_x"):
            m = _manifest([{"id": good, "name": "x", "type": "identity", "derivation_label": "ch:x"}])
            assert [f for f in check_schema(m) if "well-formed P-token" in f.message] == []

    def test_malformed_id_fires(self) -> None:
        for bad in ("X01", "01", "p01", "P-01"):
            m = _manifest([{"id": bad, "name": "x", "type": "identity", "derivation_label": "ch:x"}])
            findings = [f for f in check_schema(m) if "well-formed P-token" in f.message]
            assert len(findings) == 1, f"{bad!r} should be flagged"
            assert findings[0].severity == "critical"


# ───────────────────────────────────────────────────────────────────────────
# check_labels
# ───────────────────────────────────────────────────────────────────────────
class TestLabels:
    def test_resolved_label_no_findings(self) -> None:
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

    def test_unresolved_label_fires(self) -> None:
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

    def test_unresolved_equation_label_is_warn(self) -> None:
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
    def test_matching_symbol_and_value_no_findings(self) -> None:
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

    def test_missing_symbol_fires(self) -> None:
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

    def test_numeric_drift_fires(self) -> None:
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

    def test_symbol_without_value_is_info(self) -> None:
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

    def test_entry_without_symbol_skipped(self) -> None:
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
# check_bridge — manifest as one-directional consumer of the claim DAG
# ───────────────────────────────────────────────────────────────────────────
class TestBridge:
    # A synthetic spine: one claim node, one experiment node.
    NODES = {"clm-aaaaaa": "claim", "exp-bbbbbb": "experiment"}

    def test_valid_clm_bridge_no_findings(self) -> None:
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa"}])
        assert check_bridge(m, spine_nodes=self.NODES) == []

    def test_valid_exp_bridge_no_findings(self) -> None:
        m = _manifest([{"id": "P01", "exp": "exp-bbbbbb"}])
        assert check_bridge(m, spine_nodes=self.NODES) == []

    def test_dangling_bridge_is_critical(self) -> None:
        m = _manifest([{"id": "P01", "clm": "clm-zzzzzz"}])
        findings = check_bridge(m, spine_nodes=self.NODES)
        assert len(findings) == 1
        assert findings[0].severity == "critical"
        assert "does not resolve" in findings[0].message

    def test_malformed_bridge_is_critical(self) -> None:
        m = _manifest([{"id": "P01", "clm": "clm-BAD"}])
        findings = check_bridge(m, spine_nodes=self.NODES)
        assert len(findings) == 1
        assert findings[0].severity == "critical"
        assert "malformed" in findings[0].message

    def test_type_mismatch_is_critical(self) -> None:
        # `clm:` field pointing at an id that the index registers as an
        # experiment node — resolves, but wrong node_type.
        nodes = {"clm-aaaaaa": "experiment"}
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa"}])
        findings = check_bridge(m, spine_nodes=nodes)
        assert len(findings) == 1
        assert findings[0].severity == "critical"
        assert "expected 'claim'" in findings[0].message

    def test_unbridged_entries_aggregate_to_one_critical(self) -> None:
        # Bridge is corpus-complete (D14): an unbridged entry is now a hard
        # failure, not a pending-migration warning (INVARIANT-S11).
        m = _manifest([{"id": "P01"}, {"id": "P02"}, {"id": "P03", "clm": "clm-aaaaaa"}])
        findings = check_bridge(m, spine_nodes=self.NODES)
        assert len(findings) == 1
        assert findings[0].severity == "critical"
        assert findings[0].details["unbridged"] == ["P01", "P02"]

    def test_missing_index_warns_not_crashes(self) -> None:
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa"}])
        findings = check_bridge(m, spine_nodes={})
        assert len(findings) == 1
        assert findings[0].severity == "warn"

    def test_live_index_loads_real_nodes(self) -> None:
        nodes = collect_spine_nodes()
        assert len(nodes) > 0
        assert "claim" in set(nodes.values())
        # every id is a known spine prefix (def- = vocabulary node-type, the
        # sixth spine node-type materialized into the index per INVARIANT-S12;
        # ilk- = interlock-mechanism, the seventh spine node-type per INVARIANT-S13)
        assert all(nid.split("-", 1)[0] in {"clm", "exp", "sup", "axiom", "INVARIANT", "def", "ilk"} for nid in nodes)


# ───────────────────────────────────────────────────────────────────────────
# derive_axioms_used + check_axioms (axioms_used is a derived field)
# ───────────────────────────────────────────────────────────────────────────
class TestAxioms:
    # Synthetic DAG: clm-aaaaaa -> clm-bbbbbb -> axiom-2 ; clm-aaaaaa -> axiom-1
    ADJ = {
        "clm-aaaaaa": {"clm-bbbbbb", "axiom-1"},
        "clm-bbbbbb": {"axiom-2"},
    }

    def test_derive_transitive_cone(self) -> None:
        # Reaches axiom-1 directly and axiom-2 transitively via clm-bbbbbb.
        assert derive_axioms_used("clm-aaaaaa", self.ADJ) == [1, 2]
        assert derive_axioms_used("clm-bbbbbb", self.ADJ) == [2]

    def test_derive_no_axioms(self) -> None:
        assert derive_axioms_used("clm-zzzzzz", self.ADJ) == []

    def test_derive_is_cycle_safe(self) -> None:
        adj = {"clm-a": {"clm-b"}, "clm-b": {"clm-a", "axiom-3"}}
        assert derive_axioms_used("clm-a", adj) == [3]

    def test_check_axioms_match_no_finding(self) -> None:
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "axioms_used": [1, 2]}])
        assert check_axioms(m, adjacency=self.ADJ) == []

    def test_check_axioms_unsorted_stored_still_matches(self) -> None:
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "axioms_used": [2, 1]}])
        assert check_axioms(m, adjacency=self.ADJ) == []

    def test_check_axioms_drift_is_critical(self) -> None:
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "axioms_used": [1, 2, 4]}])
        findings = check_axioms(m, adjacency=self.ADJ)
        assert len(findings) == 1
        assert findings[0].severity == "critical"
        assert "drifts" in findings[0].message

    def test_check_axioms_skips_unbridged(self) -> None:
        # No clm: -> axioms_used stays hand-authored, not gated.
        m = _manifest([{"id": "P10", "axioms_used": [1, 2, 3]}])
        assert check_axioms(m, adjacency=self.ADJ) == []

    def test_check_axioms_missing_index_warns(self) -> None:
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "axioms_used": [1, 2]}])
        findings = check_axioms(m, adjacency={})
        assert len(findings) == 1
        assert findings[0].severity == "warn"

    def test_live_dependency_index_loads(self) -> None:
        adj = collect_dependency_edges()
        assert len(adj) > 0
        # at least one claim depends directly on an axiom node
        assert any(any(t.startswith("axiom-") for t in tgts) for tgts in adj.values())


# ───────────────────────────────────────────────────────────────────────────
# End-to-end: live manifest + live repo
# ───────────────────────────────────────────────────────────────────────────
class TestLiveManifest:
    def test_manifest_loads(self) -> None:
        m = load_manifest(MANIFEST_PATH)
        assert "predictions" in m
        assert isinstance(m["predictions"], list)
        assert len(m["predictions"]) > 0

    def test_manifest_schema_clean(self) -> None:
        m = load_manifest(MANIFEST_PATH)
        findings = check_schema(m)
        criticals = [f for f in findings if f.severity == "critical"]
        assert criticals == [], "Live manifest has schema violations:\n" + "\n".join(
            f"  [{f.severity}] P={f.entry_id} {f.message}" for f in criticals
        )

    def test_manifest_labels_resolve(self) -> None:
        m = load_manifest(MANIFEST_PATH)
        labels = collect_manuscript_labels(REPO_ROOT)
        findings = check_labels(m, labels=labels)
        criticals = [f for f in findings if f.severity == "critical"]
        assert criticals == [], "Live manifest has unresolved derivation_labels:\n" + "\n".join(
            f"  P={f.entry_id} {f.message}" for f in criticals
        )

    def test_manifest_engine_agrees(self) -> None:
        m = load_manifest(MANIFEST_PATH)
        constants = collect_constants_symbols()
        findings = check_engine(m, constants=constants)
        criticals = [f for f in findings if f.severity == "critical"]
        assert criticals == [], "Live manifest disagrees with engine:\n" + "\n".join(
            f"  P={f.entry_id} {f.message}" for f in criticals
        )

    def test_readme_parity(self) -> None:
        m = load_manifest(MANIFEST_PATH)
        findings = check_readme_parity(m)
        warns = [f for f in findings if f.severity == "warn"]
        # Parity is WARN level — if a README row has no entry it should be
        # flagged. Live assertion: zero such findings (every public claim
        # is tracked in the manifest).
        assert warns == [], "README master table has rows with no manifest entry:\n" + "\n".join(
            f"  {f.message}" for f in warns
        )

    def test_living_reference_parity(self) -> None:
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

    def test_living_reference_parser_finds_rows(self) -> None:
        # Sanity: the parser returns a non-empty list on the live doc.
        rows = extract_living_reference_prediction_rows()
        assert len(rows) >= 40, f"Expected ≥40 LIVING_REFERENCE prediction rows, got {len(rows)}"
        # Row ids should be numeric or ranges; names non-empty.
        for row_id, name in rows:
            assert row_id, "row_id should not be empty"
            assert name, "name should not be empty"

    def test_all_entries_use_allowed_types(self) -> None:
        m = load_manifest(MANIFEST_PATH)
        for entry in m["predictions"]:
            assert entry["type"] in ALLOWED_TYPES, f"Entry {entry['id']} uses unknown type: {entry['type']}"

    def test_all_entries_have_unique_ids(self) -> None:
        m = load_manifest(MANIFEST_PATH)
        ids = [e["id"] for e in m["predictions"]]
        assert len(ids) == len(set(ids)), f"Duplicate IDs: {ids}"


class TestOrchestration:
    def test_run_with_all_checks(self) -> None:
        findings = run()
        # Same assertion as above but via the top-level `run()` entry point.
        criticals = [f for f in findings if f.severity == "critical"]
        assert criticals == [], "run() reports critical findings on live manifest:\n" + "\n".join(
            f"  [{f.check}] P={f.entry_id} {f.message}" for f in criticals
        )

    def test_run_selective_check(self) -> None:
        findings = run(checks=["schema"])
        # schema-only on a valid manifest should have no criticals
        criticals = [f for f in findings if f.severity == "critical"]
        assert criticals == []

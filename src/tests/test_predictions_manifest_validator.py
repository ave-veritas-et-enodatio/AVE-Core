"""
Unit tests for the predictions-manifest validator.

Covers each structural check (schema, label, engine, bridge, axioms,
calibration_role, parity) with both happy-path and failure fixtures, plus an
end-to-end assertion that the live manifest has zero critical findings (its
quality gate for CI).

Reference: src/scripts/predictions_manifest_validator.py,
           manuscript/predictions.yaml
"""

import re

from scripts.predictions_manifest_validator import (
    ALL_CHECKS,
    ALLOWED_CALIBRATION_ROLES,
    ALLOWED_TYPES,
    MANIFEST_PATH,
    PROVENANCE_MARKERS,
    REPO_ROOT,
    check_axioms,
    check_bridge,
    check_calibration_role,
    check_engine,
    check_labels,
    check_living_reference_parity,
    check_readme_parity,
    check_schema,
    collect_claim_cards,
    collect_constants_symbols,
    collect_dependency_edges,
    collect_manuscript_labels,
    collect_spine_nodes,
    derive_axioms_used,
    extract_living_reference_prediction_rows,
    load_manifest,
    run,
    scan_provenance,
    suggest_role,
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
# check_calibration_role — declared provenance vs CORPUS-DERIVED truth
# ───────────────────────────────────────────────────────────────────────────
class TestCalibrationRole:
    """The reconciler's contract: the verdict comes from the claim CARD, never
    from the manifest itself. Every fixture below supplies a synthetic card so
    the corpus half of the comparison is explicit — if a test could pass with
    an empty card dict, it would be testing a checklist, not a gate.
    """

    @staticmethod
    def _cards(**bodies: str) -> dict[str, tuple[str, str, int]]:
        """Build a {clm_id: (card_text, path, line)} map from kwargs keyed by
        the trailing 6 chars of a clm id (kwargs can't contain a hyphen)."""
        return {f"clm-{k}": (v, "manuscript/ave-kb/volX/claim-quality.md", 1) for k, v in bodies.items()}

    # ── happy path ─────────────────────────────────────────────────────────
    def test_reconciled_role_no_findings(self) -> None:
        # Card grades the claim a consistency check; `consistency` is not in
        # that marker's forbidden set -> RECONCILED, silent.
        cards = self._cards(aaaaaa="- Classification is a consistency check (reproduces a known result).")
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "calibration_role": "consistency"}])
        assert check_calibration_role(m, cards=cards) == []

    def test_undeclared_role_is_skipped(self) -> None:
        # calibration_role is optional (predictions.yaml:29). Absent -> nothing
        # to reconcile, not a failure.
        cards = self._cards(aaaaaa="- The value is GR-imported.")
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa"}])
        assert check_calibration_role(m, cards=cards) == []

    def test_unbridged_entry_is_skipped(self) -> None:
        # No clm bridge -> no corpus card exists to reconcile against.
        cards = self._cards(aaaaaa="- The value is GR-imported.")
        m = _manifest([{"id": "P01", "calibration_role": "chord"}])
        assert check_calibration_role(m, cards=cards) == []

    # ── failure mode 1: an imported VALUE contradicts `chord` ───────────────
    def test_value_imported_contradicts_chord(self) -> None:
        cards = self._cards(
            aaaaaa=("- clm-iouqn9 [the vacuum Poisson ratio is the GR-imported trace-reversal value]"),
        )
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "calibration_role": "chord"}])
        findings = check_calibration_role(m, cards=cards)
        assert len(findings) == 1
        assert findings[0].details["verdict"] == "CONTRADICTED"
        assert findings[0].details["signals"] == ["VALUE_IMPORTED"]
        # The receipt must be carried, not just the verdict.
        assert "GR-imported" in findings[0].details["forbidding_signals"]["VALUE_IMPORTED"][0]

    def test_form_vs_value_split_contradicts_chord_and_suggests_mixed(self) -> None:
        cards = self._cards(
            aaaaaa=("- so the FORM $\\sin^2\\theta_W$ is derived but the VALUE $2/9$ is import-capped"),
        )
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "calibration_role": "chord"}])
        findings = check_calibration_role(m, cards=cards)
        assert len(findings) == 1
        assert "FORM_VS_VALUE_SPLIT" in findings[0].details["signals"]
        assert findings[0].details["suggested"] == "mixed"

    # ── failure mode 2: a fitted / phenomenological VALUE contradicts `chord`
    def test_value_fitted_contradicts_chord(self) -> None:
        cards = self._cards(aaaaaa="- Mapping-conditional, disclosed-phenomenological match.")
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "calibration_role": "chord"}])
        findings = check_calibration_role(m, cards=cards)
        assert len(findings) == 1
        assert findings[0].details["signals"] == ["VALUE_FITTED"]

    # ── failure mode 3: a consistency grading contradicts forward-prediction
    def test_consistency_class_contradicts_forward_prediction(self) -> None:
        cards = self._cards(aaaaaa="- This is a **consistency check** (category iii).")
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "calibration_role": "forward-prediction"}])
        findings = check_calibration_role(m, cards=cards)
        assert len(findings) == 1
        assert findings[0].details["verdict"] == "CONTRADICTED"

    # ── failure mode 4: the REVERSE direction — a card that refuses the
    #    consistency grading contradicts a declared `consistency` ────────────
    def test_consistency_denied_contradicts_consistency(self) -> None:
        cards = self._cards(
            aaaaaa=("- error 1.7% — a category (iv) derived prediction, not an identity or consistency check."),
        )
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "calibration_role": "consistency"}])
        findings = check_calibration_role(m, cards=cards)
        assert len(findings) == 1
        assert findings[0].details["forbidding_signals"].keys() == {"CONSISTENCY_DENIED"}

    # ── failure mode 5: an unknown role is a precondition failure ───────────
    def test_unknown_role_is_critical(self) -> None:
        cards = self._cards(aaaaaa="- anything")
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "calibration_role": "vibes"}])
        findings = check_calibration_role(m, cards=cards)
        assert len(findings) == 1
        assert findings[0].severity == "critical"
        assert findings[0].details["verdict"] == "UNKNOWN_ROLE"

    # ── the UNRECONCILED case — corpus silent, no guess ─────────────────────
    def test_silent_card_is_unreconciled_not_a_guess(self) -> None:
        cards = self._cards(aaaaaa="- A clean algebraic chain with no provenance statement.")
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "calibration_role": "chord"}])
        findings = check_calibration_role(m, cards=cards)
        assert len(findings) == 1
        assert findings[0].severity == "info"
        assert findings[0].details["verdict"] == "UNRECONCILED"
        assert "suggested" not in findings[0].details

    def test_missing_card_warns(self) -> None:
        m = _manifest([{"id": "P01", "clm": "clm-zzzzzz", "calibration_role": "chord"}])
        findings = check_calibration_role(m, cards=self._cards(aaaaaa="x"))
        assert len(findings) == 1
        assert findings[0].severity == "warn"
        assert findings[0].details["verdict"] == "NO_CARD"

    def test_empty_kb_warns_not_crashes(self) -> None:
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "calibration_role": "chord"}])
        findings = check_calibration_role(m, cards={})
        assert len(findings) == 1
        assert findings[0].severity == "warn"

    # ── the negation guard (the false-positive class that would kill the gate)
    def test_negated_marker_does_not_fire(self) -> None:
        # Live text from vol3/claim-quality.md clm-395gps: the phrase
        # "consistency check" appears, but NEGATED. A naive scanner would
        # mis-grade a category-(iv) derived prediction as consistency-class.
        body = "- a category (iv) derived prediction, not an identity or consistency check."
        signals = {mk.signal for mk, _ in scan_provenance(body)}
        assert "CONSISTENCY_CLASS" not in signals
        assert "CONSISTENCY_DENIED" in signals

    def test_vs_listing_does_not_fire_consistency(self) -> None:
        # Live text from vol2/claim-quality.md:903 (clm-xhdai6 strengthen-by): a
        # task line enumerating taxonomy categories, not a grading of this
        # claim. Suppressed by the ENUMERATION guard (`vs` on BOTH sides), not
        # by the negation guard — `vs` is a comparison marker, not a negation.
        body = "- Tabulate which of the 26 are derived predictions vs consistency checks vs identities."
        assert "CONSISTENCY_CLASS" not in {mk.signal for mk, _ in scan_provenance(body)}

    def test_negated_comma_list_stays_suppressed(self) -> None:
        # The comma clause-boundary must NOT release an appositive inside a
        # negated list. "not a chord, a consistency check, or an identity" is
        # one negation over three items.
        body = "- This is not a chord, a consistency check, or an identity."
        assert "CONSISTENCY_CLASS" not in {mk.signal for mk, _ in scan_provenance(body)}

    # ── ANTI-OVER-SUPPRESSION: the guard must not manufacture false negatives ─
    #
    # The mirror image of the two tests above, and the more dangerous failure:
    # an over-broad guard silently downgrades CONTRADICTED to UNRECONCILED, so
    # the gate reports "the corpus is silent" about a card that is shouting.
    # Every fixture below is VERBATIM live corpus text, re-verified by two
    # methods (line-addressed read + content grep) at the line cited.
    def test_affirmed_import_after_semicolon_fires(self) -> None:
        # vol2/claim-quality.md:120 (clm-5zuo7g depends-on note). The "NOT"
        # scopes over "a free framework input" — it AFFIRMS the import — and
        # the affirmation sits on the far side of a ';'.
        body = (
            "  - clm-iouqn9 — K4 Magic-Angle $K=2G$ (solidity 0.55) [the vacuum Poisson ratio "
            "$2/7$ is the GR-imported trace-reversal value, NOT a free framework input; so the "
            "FORM $\\sin^2\\theta_W = 1-1/(1+\\nu_{vac})$ is derived but the VALUE $2/9$ is "
            "import-capped at $K=2G$'s solidity]"
        )
        assert "FORM_VS_VALUE_SPLIT" in {mk.signal for mk, _ in scan_provenance(body)}

    def test_denial_then_affirmation_across_em_dash_fires(self) -> None:
        # common/claim-quality.md:1477 (clm-strreg). "NOT A DERIVATION" is
        # denied, then the consistency-class grading is affirmed after an
        # em-dash. An em-dash separates the assertion from its clause.
        body = (
            "  - **RULED CONVENTION, NOT A DERIVATION — consistency-class.** Grant ruled which "
            "strain the kernel eats; the VALUES ride CODATA-derived imports."
        )
        assert "CONSISTENCY_CLASS" in {mk.signal for mk, _ in scan_provenance(body)}

    def test_comparison_vs_is_not_a_negation_rationale(self) -> None:
        # vol2/claim-quality.md:861 (clm-qde5gn rationale). "sub-1 ppm vs
        # CODATA" is a COMPARISON. Carrying `vs` in the negation lexicon killed
        # an explicit consistency-check grading one sentence later.
        body = (
            "- rationale: the leaf states they are algebraically identical to Bohr, sub-1 ppm vs "
            "CODATA). Classification is largely a consistency check / identity-rearrangement "
            "carrying an ontological reinterpretation."
        )
        assert "CONSISTENCY_CLASS" in {mk.signal for mk, _ in scan_provenance(body)}

    def test_comparison_vs_is_not_a_negation_form_forced(self) -> None:
        # common/claim-quality.md:134 (clm-m7qd0w). "(−5.2% vs measured)" is a
        # comparison inside a parenthetical; it must not eat the FORM_FORCED
        # statement that follows it in the same sentence.
        body = (
            "  - The sub-derivation of $v_{backbone}$ from the soliton bond solver yields "
            "5470 m/s (−5.2% vs measured), zero free parameters."
        )
        assert "FORM_FORCED" in {mk.signal for mk, _ in scan_provenance(body)}

    def test_previous_sentence_negation_does_not_reach(self) -> None:
        # vol2/claim-quality.md:1531 (clm-3i66gp). The negation lives in the
        # PREVIOUS sentence; the character window crossed the '.' and killed an
        # explicit "Structural/consistency-class only." grading.
        body = (
            "  - **NOT** a clean $0.65\\%$ AVE precision prediction: the dominant self-energy "
            "($+1010$ MHz) is QED-imported, not an AVE numerical output. "
            "Structural/consistency-class only."
        )
        assert "CONSISTENCY_CLASS" in {mk.signal for mk, _ in scan_provenance(body)}

    def test_negation_sealed_in_parenthetical_does_not_reach(self) -> None:
        # vol3/claim-quality.md:1254 (clm-zbvfpi). "REUSED not minted)" is a
        # parenthetical aside; a negation sealed inside it cannot govern the
        # "**Engine-capability / consistency-class**" grading outside it.
        body = (
            "The FIRST increment of the GR-QED extension engine (the ONE canonical Op14 kernel, "
            "REUSED not minted). **Engine-capability / consistency-class** — a correction ON the "
            "linear GR core, NOT a re-derivation of it."
        )
        assert "CONSISTENCY_CLASS" in {mk.signal for mk, _ in scan_provenance(body)}

    def test_denial_then_independent_clause_affirmation_fires(self) -> None:
        # Constructed, but the near-canonical AVE self-description form: a
        # denial of novelty followed by a comma and an independent clause that
        # affirms the consistency grading.
        body = "- This is not novel, it is a consistency check."
        assert "CONSISTENCY_CLASS" in {mk.signal for mk, _ in scan_provenance(body)}

    def test_live_corpus_suppression_set_is_exactly_the_two_true_cases(self) -> None:
        # The census-level statement of the same contract, run against the real
        # registers: across all live claim cards, the ONLY matches the guards
        # discard are the two regression cases above. Any third suppression is
        # a new false negative and must be adjudicated, not absorbed silently.
        import re as _re

        from scripts.predictions_manifest_validator import (  # noqa: PLC0415
            _is_enumeration,
            _is_negated,
        )

        suppressed: set[tuple[str, str]] = set()
        for clm_id, (body, _, _) in collect_claim_cards().items():
            for mk in PROVENANCE_MARKERS:
                for m in _re.finditer(mk.pattern, body):
                    if _is_negated(body, m.start()) or _is_enumeration(body, m.start(), m.end()):
                        suppressed.add((clm_id, mk.signal))
                        continue
                    break
        assert suppressed == {
            ("clm-395gps", "CONSISTENCY_CLASS"),  # vol3/claim-quality.md:199, negation
            ("clm-xhdai6", "CONSISTENCY_CLASS"),  # vol2/claim-quality.md:903, enumeration
        }, f"guard suppression set drifted: {sorted(suppressed)}"

    # ── the design invariant: positive derivation language licenses nothing ──
    def test_form_forced_forbids_nothing(self) -> None:
        # "zero free parameters" is equally consistent with `chord` and with
        # `mixed` (form-derived / value-imported), so it must never clear or
        # create a contradiction on its own.
        assert all(mk.forbids == frozenset() for mk in PROVENANCE_MARKERS if mk.signal == "FORM_FORCED")
        cards = self._cards(aaaaaa="- Derived with zero free parameters.")
        for role in sorted(ALLOWED_CALIBRATION_ROLES):
            m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "calibration_role": role}])
            assert check_calibration_role(m, cards=cards) == []

    def test_no_marker_reads_solidity_or_confidence(self) -> None:
        # calibration_role is a PROVENANCE axis; solidity is a CONFIDENCE axis.
        # Conflating them is a category error, so no pattern may key on either.
        #
        # NOTE this test is LEXICAL and therefore BYPASSABLE: a pattern keyed on
        # the solidity NUMBER rather than the word (e.g. r"\(s\w+ity 0\.[0-5]\d?\)")
        # slips straight through it. That is not a hole to widen the token list
        # for — a blocklist can always be spelled around. The actual freeze is
        # `TestProvenanceMarkerTableIsFrozen` below, which is a SNAPSHOT: any
        # addition or edit to the table shows up as a test diff and needs a
        # reviewer. Keep both; they fail on different things.
        banned = ("solidity", "confidence", "build_status", "build_band", "use as input only")
        for mk in PROVENANCE_MARKERS:
            for token in banned:
                assert token not in mk.pattern, f"{mk.signal} pattern keys on {token!r}"

    # ── suggest_role is advisory-only ──────────────────────────────────────
    def test_suggest_role_mapping(self) -> None:
        assert suggest_role({"FORM_VS_VALUE_SPLIT"}) == "mixed"
        assert suggest_role({"FORM_FORCED", "VALUE_FITTED"}) == "mixed"
        assert suggest_role({"VALUE_IMPORTED"}) == "echo"
        assert suggest_role({"CONSISTENCY_CLASS"}) == "consistency"
        assert suggest_role({"FORM_FORCED"}) is None
        assert suggest_role(set()) is None

    def test_severity_knob_switches_gating_posture(self) -> None:
        cards = self._cards(aaaaaa="- Mapping-conditional, disclosed-phenomenological match.")
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "calibration_role": "chord"}])
        assert check_calibration_role(m, cards=cards)[0].severity == "warn"
        assert check_calibration_role(m, cards=cards, severity="critical")[0].severity == "critical"

    # ── live corpus ────────────────────────────────────────────────────────
    def test_live_cards_load(self) -> None:
        cards = collect_claim_cards()
        assert len(cards) > 100, f"expected the live KB registers to yield >100 claim cards, got {len(cards)}"
        for clm_id, (body, path, line) in cards.items():
            assert clm_id.startswith("clm-")
            assert body.lstrip().startswith("## "), f"{clm_id} card does not start at its ## heading"
            assert path.startswith("manuscript/ave-kb/")
            assert "tools/tests" not in path, "test fixtures must not be read as corpus authority"
            assert line >= 1

    def test_live_card_sections_do_not_bleed(self) -> None:
        # Each card must own exactly one clm id marker — a slice that ran past
        # the next `## ` heading would attribute a neighbour's provenance.
        cards = collect_claim_cards()
        for clm_id, (body, _, _) in cards.items():
            assert body.count("<!-- id: clm-") == 1, f"{clm_id} card slice spans multiple claim entries"

    def test_form_vs_value_split_fires_on_its_live_receipt(self) -> None:
        # This marker shipped DEAD (0 of 329 cards) because the unclamped
        # negation window discarded its only match — which was its own claimed
        # receipt. Pin the re-measurement: it must fire on the LIVE clm-5zuo7g
        # card, and that card must remain its sole live site (if a second site
        # appears, the receipt is stale and needs re-verifying).
        cards = collect_claim_cards()
        firing = {
            clm_id
            for clm_id, (body, _, _) in cards.items()
            if "FORM_VS_VALUE_SPLIT" in {mk.signal for mk, _ in scan_provenance(body)}
        }
        assert firing == {"clm-5zuo7g"}, f"FORM_VS_VALUE_SPLIT live sites drifted: {sorted(firing)}"

    def test_deviation_disclaimed_forbids_only_forward_prediction(self) -> None:
        # A card that refuses to predict a non-zero deviation is stating a NULL
        # matching the standard expectation, so it cannot be
        # "divergent-from-SM" (predictions.yaml:35). But a null can still be a
        # forced FORM — α-invariance under symmetric gravity IS a forced
        # cancellation — so the marker must leave every other role alone.
        body = "  - Does NOT claim the framework predicts $\\Delta\\alpha \\neq 0$ in any gravitational regime."
        assert "DEVIATION_DISCLAIMED" in {mk.signal for mk, _ in scan_provenance(body)}
        cards = self._cards(aaaaaa=body)
        for role in sorted(ALLOWED_CALIBRATION_ROLES):
            m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "calibration_role": role}])
            findings = check_calibration_role(m, cards=cards)
            contradicted = [f for f in findings if f.details.get("verdict") == "CONTRADICTED"]
            assert bool(contradicted) is (role == "forward-prediction"), (
                f"DEVIATION_DISCLAIMED must contradict only 'forward-prediction', got {role} -> {findings}"
            )

    def test_live_manifest_has_no_unknown_roles(self) -> None:
        # The reconciler's precondition holds on the live manifest.
        m = load_manifest(MANIFEST_PATH)
        criticals = [f for f in check_calibration_role(m) if f.severity == "critical"]
        assert criticals == [], "Live manifest declares a calibration_role outside the taxonomy:\n" + "\n".join(
            f"  P={f.entry_id} {f.message}" for f in criticals
        )

    def test_registered_check_gates_at_critical(self) -> None:
        # The 2026-08-05 flip lives at the ALL_CHECKS registration, NOT at the
        # function's default (which stays "warn" for ad-hoc callers). Pin the
        # registration, or the flip can be reverted by a keyword edit that no
        # test notices.
        registered = ALL_CHECKS["calibration_role"]
        assert getattr(registered, "keywords", {}).get("severity") == "critical", (
            "calibration_role must be REGISTERED at severity='critical' "
            "(flip condition discharged 2026-08-05: P04 + P42 both ruled and landed)"
        )
        cards = self._cards(aaaaaa="- Mapping-conditional, disclosed-phenomenological match.")
        m = _manifest([{"id": "P01", "clm": "clm-aaaaaa", "calibration_role": "chord"}])
        assert check_calibration_role(m, cards=cards, severity="critical")[0].severity == "critical"

    def test_live_manifest_has_no_contradicted_roles(self) -> None:
        # The flip's precondition, asserted as a standing gate rather than a
        # one-off census: a CONTRADICTED row would now red-gate `make verify`.
        m = load_manifest(MANIFEST_PATH)
        contradicted = [
            f for f in check_calibration_role(m) if f.details.get("verdict") == "CONTRADICTED"
        ]
        assert contradicted == [], "Live manifest has contradicted calibration_role rows:\n" + "\n".join(
            f"  P={f.entry_id} {f.message}" for f in contradicted
        )


# ───────────────────────────────────────────────────────────────────────────
# The marker table is FROZEN — snapshot, not blocklist
# ───────────────────────────────────────────────────────────────────────────
# The table is described as "frozen" throughout this branch. Before this class
# the only thing enforcing that was `test_no_marker_reads_solidity_or_confidence`,
# which is LEXICAL: it bans the token "solidity". An independent auditor bypassed
# it in one line by adding a marker keyed on the solidity NUMBER instead of the
# word — r"\(s\w+ity 0\.[0-5]\d?\)" — and every test still passed. A CONFIDENCE-axis
# rule in a PROVENANCE costume walked straight in, and the walk-in surface is real:
# `collect_claim_cards()` reads whole cards off disk, so "- solidity: 0.55 ..." and
# "- confidence: 0.85" ARE inside the scan text. Only the lexicon kept them out, and
# a blocklist can always be spelled around.
#
# A snapshot cannot be spelled around. Any addition, deletion or edit to a signal,
# pattern or forbid-set shows up as a diff on the literal below, in the test file,
# where a reviewer has to look at it and say yes.
FROZEN_MARKER_TABLE: tuple[tuple[str, str, tuple[str, ...]], ...] = (
    ("VALUE_IMPORTED", r"\bGR-imported\b", ("chord",)),
    ("VALUE_IMPORTED", r"\bimport-capped\b", ("chord",)),
    ("VALUE_IMPORTED", r"disclosed imports? (?:are|is)\b", ("chord",)),
    ("VALUE_IMPORTED", r"back-?solved\b", ("chord",)),
    ("VALUE_IMPORTED", r"\bimported, not derived\b", ("chord",)),
    ("VALUE_FITTED", r"disclosed[- ]phenomenological", ("chord",)),
    ("VALUE_FITTED", r"phenomenological[^.]{0,120}(?:formula|shift|fit\b)", ("chord",)),
    ("VALUE_FITTED", r"\bis \*{0,2}FITTED\b", ("chord",)),
    ("VALUE_FITTED", r"\brefined post-hoc\b|\bpost-hoc against\b", ("chord",)),
    ("VALUE_FITTED", r"back-reaction fit\b", ("chord",)),
    ("FORM_VS_VALUE_SPLIT", r"FORM[^.]{0,220}is derived but the VALUE", ("chord",)),
    ("CONSISTENCY_CLASS", r"consistency check", ("chord", "forward-prediction")),
    ("CONSISTENCY_CLASS", r"category \(iii\)", ("chord", "forward-prediction")),
    ("CONSISTENCY_CLASS", r"consistency-class", ("chord", "forward-prediction")),
    ("IDENTITY_CLASS", r"definitional[- ](?:identity|residual)", ("chord", "forward-prediction")),
    (
        "CONSISTENCY_DENIED",
        r"not an identity or consistency check|NOT a consistency check",
        ("consistency",),
    ),
    (
        "NOT_SM_DISTINGUISHABLE",
        r"not (?:a )?(?:novel )?[a-z ]{0,30}distinguishable from",
        ("forward-prediction",),
    ),
    (
        "DEVIATION_DISCLAIMED",
        r"[Dd]oes NOT claim[^.]{0,160}(?:\\neq|\\ne)\s*0",
        ("forward-prediction",),
    ),
    ("FORM_FORCED", r"zero free parameters", ()),
    ("FORM_FORCED", r"category[ -]\(iv\)[ -]derived prediction", ()),
)


class TestProvenanceMarkerTableIsFrozen:
    def test_table_matches_the_snapshot(self) -> None:
        live = tuple((mk.signal, mk.pattern, tuple(sorted(mk.forbids))) for mk in PROVENANCE_MARKERS)
        assert live == FROZEN_MARKER_TABLE, (
            "PROVENANCE_MARKERS changed. This table is FROZEN: a marker is a rule about what "
            "the corpus is allowed to mean, so adding or editing one is a reviewed act, not a "
            "refactor. Update FROZEN_MARKER_TABLE in the same commit, and in the commit message "
            "state (a) the corpus receipt the new/edited pattern was grep-verified against and "
            "(b) that it keys on PROVENANCE, never on solidity / confidence / build_status / "
            "build_band.\n"
            f"  live     = {live}\n"
            f"  snapshot = {FROZEN_MARKER_TABLE}"
        )

    def test_snapshot_is_the_complete_freeze_surface(self) -> None:
        # The snapshot must pin every field that can change a VERDICT. `receipt`
        # is deliberately outside it (prose, no verdict effect); `signal`,
        # `pattern` and `forbids` are all of the rest.
        verdict_fields = {"signal", "pattern", "forbids"}
        fields = set(PROVENANCE_MARKERS[0].__dataclass_fields__)
        assert fields - {"receipt"} == verdict_fields, (
            f"ProvenanceMarker gained/lost a field ({sorted(fields)}); if it can affect a "
            f"verdict it must be added to FROZEN_MARKER_TABLE."
        )


# ───────────────────────────────────────────────────────────────────────────
# Every marker must FIRE on the receipt it claims (the G3 gap)
# ───────────────────────────────────────────────────────────────────────────
# `receipt` asserts "this pattern was grep-confirmed against the live cards".
# Nothing checked that. FORM_VS_VALUE_SPLIT shipped firing on 0 of 329 cards
# with a receipt pointing at its own suppression site; these two tests would
# have caught it on day one.
class TestMarkerReceipts:
    def test_every_marker_fires_somewhere_in_the_live_corpus(self) -> None:
        cards = collect_claim_cards()
        assert cards, "live KB registers did not load"
        counts: dict[tuple[str, str], int] = {(mk.signal, mk.pattern): 0 for mk in PROVENANCE_MARKERS}
        for _, (body, _, _) in cards.items():
            for mk, _excerpt in scan_provenance(body):
                counts[(mk.signal, mk.pattern)] += 1
        dead = sorted(k for k, v in counts.items() if v == 0)
        assert not dead, (
            "Dead marker(s) — a frozen-table row that never fires is decoration, and if its "
            "receipt is its own suppression site the receipt is self-referential. Either the "
            "corpus phrasing moved (re-verify and re-derive the pattern) or the row should be "
            f"retracted from the table AND from the PR body: {dead}"
        )

    def test_every_marker_fires_on_the_cards_its_receipt_names(self) -> None:
        # Receipts name claim ids inline ("vol2/claim-quality.md:120 clm-5zuo7g
        # depends-on note"). Every id a receipt names must be a real card that
        # the marker actually fires on, or the receipt is stale.
        cards = collect_claim_cards()
        broken: list[str] = []
        checked = 0
        for mk in PROVENANCE_MARKERS:
            named = sorted(set(re.findall(r"clm-[a-z0-9]{6}", mk.receipt)))
            assert named, f"{mk.signal} {mk.pattern!r} receipt names no claim card to check against"
            for clm_id in named:
                checked += 1
                if clm_id not in cards:
                    broken.append(f"{mk.signal} {mk.pattern!r} -> {clm_id} has no card")
                elif mk.signal not in {s.signal for s, _ in scan_provenance(cards[clm_id][0])}:
                    broken.append(f"{mk.signal} {mk.pattern!r} -> does NOT fire on {clm_id}")
        assert not broken, "Marker receipts do not hold:\n  " + "\n  ".join(broken)
        assert checked >= len(PROVENANCE_MARKERS), "every marker must contribute at least one receipt card"


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

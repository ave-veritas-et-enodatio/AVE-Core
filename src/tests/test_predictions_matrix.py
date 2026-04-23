"""
Pre-registered predictions matrix — Stage 6 Phase 1 CI gate.

Loops over `manuscript/predictions.yaml` entries flagged
`pre_registered: true` and verifies that each has:

  - a `research_doc` pointing at a file that exists on disk
  - a `test_file` pointing at a pytest file that exists on disk
  - `axioms_used` populated (forward predictions must declare which
    axioms they lean on)
  - `type` ∈ ALLOWED_TYPES (same schema as regular predictions)
  - `public_in_readme` and `public_in_living_ref` both false (forward-
    looking predictions are not published in master tables yet)
  - ID prefix `P_phase` — stable naming convention for Stage 6 entries

Why this test exists: the plan (Stage 6 §"Test infrastructure plan")
requires a CI gate that prevents a pre-registered prediction from
drifting away from its test — e.g., renaming the test file without
updating the manifest entry, or adding a prediction without writing
the corresponding test.

Reference:
  - manuscript/predictions.yaml (manifest)
  - src/scripts/claim_graph_validator.py PRE_REGISTERED_REQUIRED_FIELDS
  - research/L3_electron_soliton/54_pair_production_axiom_derivation.md §8
    (full predictions matrix)
  - ~/.claude/plans/review-the-collaboration-md-and-lexical-wombat.md
    (Stage 6 approved plan, "Test infrastructure plan" section)
"""
from __future__ import annotations

import pathlib

import pytest
import yaml

from scripts.claim_graph_validator import (
    ALLOWED_TYPES,
    PRE_REGISTERED_REQUIRED_FIELDS,
    REPO_ROOT,
)


MANIFEST_PATH = REPO_ROOT / "manuscript" / "predictions.yaml"


def _load_manifest() -> dict:
    with MANIFEST_PATH.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def _pre_registered_entries() -> list[dict]:
    manifest = _load_manifest()
    return [
        e for e in manifest.get("predictions", [])
        if e.get("pre_registered") is True
    ]


# ═══════════════════════════════════════════════════════════════════════════
# Sanity: manifest contains the expected Stage 6 entries
# ═══════════════════════════════════════════════════════════════════════════
class TestManifestHasStage6Entries:
    """Stage 6's 6 pre-registered predictions must all be present."""

    EXPECTED_IDS = {
        "P_phase0_varactor",
        "P_phase2_omega",
        "P_phase3_flux_tube",
        "P_phase4_asymmetric",
        "P_phase5_nucleation",
        "P_phase6_autoresonant",
    }

    def test_all_six_entries_present(self):
        """All six Stage 6 pre_registered IDs live in predictions.yaml."""
        entries = _pre_registered_entries()
        ids = {e["id"] for e in entries}
        missing = self.EXPECTED_IDS - ids
        assert not missing, f"Missing pre_registered entries: {sorted(missing)}"

    def test_count_matches_expected(self):
        """Exactly the expected count of pre_registered entries exist.

        If you're adding a new pre_registered entry, update EXPECTED_IDS
        and the corresponding docs (doc 54_ §8, plan file §"Predictions
        matrix") in the same commit.
        """
        entries = _pre_registered_entries()
        assert len(entries) == len(self.EXPECTED_IDS), (
            f"Expected {len(self.EXPECTED_IDS)} pre_registered entries, "
            f"found {len(entries)}. If intentional, update EXPECTED_IDS "
            f"and doc 54_ §8."
        )


# ═══════════════════════════════════════════════════════════════════════════
# Schema: every pre_registered entry has the required fields
# ═══════════════════════════════════════════════════════════════════════════
class TestPreRegisteredSchema:
    """Each pre_registered entry must satisfy PRE_REGISTERED_REQUIRED_FIELDS."""

    @pytest.mark.parametrize("entry", _pre_registered_entries(),
                             ids=lambda e: e["id"])
    def test_required_fields_present(self, entry: dict):
        missing = PRE_REGISTERED_REQUIRED_FIELDS - entry.keys()
        assert not missing, (
            f"Entry {entry.get('id')} missing required fields: "
            f"{sorted(missing)}"
        )

    @pytest.mark.parametrize("entry", _pre_registered_entries(),
                             ids=lambda e: e["id"])
    def test_type_is_allowed(self, entry: dict):
        """type ∈ ALLOWED_TYPES (pre_registered entries still classify)."""
        assert entry["type"] in ALLOWED_TYPES, (
            f"Entry {entry['id']}: type '{entry['type']}' "
            f"not in {sorted(ALLOWED_TYPES)}"
        )

    @pytest.mark.parametrize("entry", _pre_registered_entries(),
                             ids=lambda e: e["id"])
    def test_axioms_used_populated(self, entry: dict):
        """axioms_used must be a non-empty list of ints in {1, 2, 3, 4}."""
        axioms = entry.get("axioms_used")
        assert isinstance(axioms, list) and len(axioms) > 0, (
            f"Entry {entry['id']}: axioms_used must be a non-empty list"
        )
        assert all(a in (1, 2, 3, 4) for a in axioms), (
            f"Entry {entry['id']}: axioms_used contains invalid values "
            f"{axioms}; must be in {{1, 2, 3, 4}}"
        )


# ═══════════════════════════════════════════════════════════════════════════
# File existence: research_doc and test_file must point at real files
# ═══════════════════════════════════════════════════════════════════════════
class TestPreRegisteredPaths:
    """research_doc and test_file fields must resolve to files that exist."""

    @pytest.mark.parametrize("entry", _pre_registered_entries(),
                             ids=lambda e: e["id"])
    def test_research_doc_exists(self, entry: dict):
        path_str = entry["research_doc"].split("#")[0]
        full = REPO_ROOT / path_str
        assert full.exists(), (
            f"Entry {entry['id']}: research_doc '{entry['research_doc']}' "
            f"does not resolve to a file on disk"
        )

    @pytest.mark.parametrize("entry", _pre_registered_entries(),
                             ids=lambda e: e["id"])
    def test_test_file_exists_or_is_upcoming(self, entry: dict):
        """test_file must either exist (phase landed) or be in the set of
        upcoming phase-N test filenames (plan-declared but not yet written).

        Stage 6 convention: test_file is committed in the same PR that
        introduces the prediction, EXCEPT for forward phases whose engine
        work hasn't started yet. For those, the filename is reserved
        and the test will land when the corresponding phase ships.
        """
        path_str = entry["test_file"].split("#")[0]
        full = REPO_ROOT / path_str

        # Phase 1 tests ship with the manifest (this commit)
        phase_1_tests = {
            "src/tests/test_axiom_4_vacuum_varactor.py",
            "src/tests/test_v_snap_v_yield_consistency.py",
            "src/tests/test_predictions_matrix.py",
        }
        # Phases 2-6 tests land when each phase ships
        upcoming = {
            "src/tests/test_phase2_node_resonance.py",
            "src/tests/test_phase3_bond_state.py",
            "src/tests/test_phase4_asymmetric_saturation.py",
            "src/tests/test_phase5_pair_nucleation_gate.py",
            "src/tests/test_phase6_autoresonant_advantage.py",
        }

        if path_str in phase_1_tests:
            assert full.exists(), (
                f"Entry {entry['id']}: Phase 1 test_file '{path_str}' "
                f"must exist in this commit"
            )
        elif path_str in upcoming:
            # Acceptable to not-yet-exist; will be added when the phase ships
            pass
        else:
            pytest.fail(
                f"Entry {entry['id']}: test_file '{path_str}' is neither "
                f"a Phase 1 test nor a planned Phase 2-6 test. If this is "
                f"intentional, update the plan and this test's whitelist."
            )


# ═══════════════════════════════════════════════════════════════════════════
# Publication status: pre_registered are NOT in master tables yet
# ═══════════════════════════════════════════════════════════════════════════
class TestPreRegisteredNotPublished:
    """Pre_registered predictions are forward-looking; they must not appear
    in the public README / LIVING_REFERENCE master tables until the
    corresponding engine work lands and the prediction is validated."""

    @pytest.mark.parametrize("entry", _pre_registered_entries(),
                             ids=lambda e: e["id"])
    def test_not_public_in_readme(self, entry: dict):
        assert entry.get("public_in_readme") is False, (
            f"Entry {entry['id']}: pre_registered entries must have "
            f"public_in_readme=false until engine validation lands"
        )

    @pytest.mark.parametrize("entry", _pre_registered_entries(),
                             ids=lambda e: e["id"])
    def test_not_public_in_living_ref(self, entry: dict):
        assert entry.get("public_in_living_ref") is False, (
            f"Entry {entry['id']}: pre_registered entries must have "
            f"public_in_living_ref=false until engine validation lands"
        )


# ═══════════════════════════════════════════════════════════════════════════
# ID naming convention: P_phaseN_<short_name>
# ═══════════════════════════════════════════════════════════════════════════
class TestPreRegisteredIdConvention:
    """Pre_registered IDs follow the P_phaseN_<short> convention so that
    they sort next to their phase and don't collide with the P01-P47
    numerical series already in use."""

    @pytest.mark.parametrize("entry", _pre_registered_entries(),
                             ids=lambda e: e["id"])
    def test_id_starts_with_p_phase(self, entry: dict):
        eid = entry["id"]
        assert eid.startswith("P_phase"), (
            f"Entry {eid}: pre_registered IDs must start with 'P_phase' "
            f"to avoid collision with the P01-P47 numerical series"
        )

    @pytest.mark.parametrize("entry", _pre_registered_entries(),
                             ids=lambda e: e["id"])
    def test_id_has_phase_number(self, entry: dict):
        """ID format: P_phaseN_<short>, where N ∈ {0..6}."""
        eid = entry["id"]
        # Strip "P_phase" prefix, grab digit(s) up to next underscore
        remainder = eid[len("P_phase"):]
        phase_str = remainder.split("_")[0]
        assert phase_str.isdigit(), (
            f"Entry {eid}: expected P_phaseN_<short> format; "
            f"could not parse phase number from '{remainder}'"
        )
        phase_num = int(phase_str)
        assert 0 <= phase_num <= 6, (
            f"Entry {eid}: phase number {phase_num} out of range 0..6"
        )

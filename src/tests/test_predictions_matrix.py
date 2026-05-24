"""
Pre-registered predictions matrix — manifest-integrity gate.

Loops over `manuscript/predictions.yaml` entries flagged
`pre_registered: true` and verifies the manifest is internally well-formed,
without freezing any particular set, count, or naming scheme. The manifest
grows legitimately (new phases, new prediction categories, versioned
variants), so this gate checks structural integrity only:

  - every pre_registered entry carries the required fields, non-empty
  - `axioms_used` is a non-empty list of ints
  - IDs are unique across all pre_registered entries
  - each ID is a well-formed `P_<...>` token

Why this test exists: catch the real failure modes of editing the manifest
by hand — a new entry missing a field, a copy-pasted duplicate ID, or a
junk/empty ID — while staying silent on legitimate growth.

Reference:
  - manuscript/predictions.yaml (manifest)
  - src/scripts/claim_graph_validator.py REPO_ROOT
"""

from __future__ import annotations

import re

import pytest
import yaml

from scripts.claim_graph_validator import REPO_ROOT

MANIFEST_PATH = REPO_ROOT / "manuscript" / "predictions.yaml"

# Fields every pre_registered entry must carry, non-empty.
REQUIRED_FIELDS = ("id", "name", "type", "test_file", "research_doc", "axioms_used")

# Permissive ID shape: a "P_" prefix followed by word characters. Allows any
# phase number and any evolved category (P_ax5_*, P_basin_*, _v2…_v8, etc.);
# rejects only empty or junk IDs.
ID_PATTERN = re.compile(r"^P_[A-Za-z0-9_]+$")


def _load_manifest() -> dict:
    with MANIFEST_PATH.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def _pre_registered_entries() -> list[dict]:
    manifest = _load_manifest()
    return [e for e in manifest.get("predictions", []) if e.get("pre_registered") is True]


# ═══════════════════════════════════════════════════════════════════════════
# Per-entry schema: required fields present + non-empty
# ═══════════════════════════════════════════════════════════════════════════
class TestPreRegisteredSchema:
    """Each pre_registered entry must carry the required fields, non-empty."""

    @pytest.mark.parametrize("entry", _pre_registered_entries(), ids=lambda e: e["id"])
    def test_required_fields_present(self, entry: dict):
        for field in REQUIRED_FIELDS:
            value = entry.get(field)
            assert value not in (
                None,
                "",
                [],
            ), f"Entry {entry.get('id')}: required field '{field}' is missing or empty"

    @pytest.mark.parametrize("entry", _pre_registered_entries(), ids=lambda e: e["id"])
    def test_axioms_used_well_formed(self, entry: dict):
        """axioms_used must be a non-empty list of ints."""
        axioms = entry.get("axioms_used")
        assert (
            isinstance(axioms, list) and len(axioms) > 0
        ), f"Entry {entry['id']}: axioms_used must be a non-empty list"
        assert all(
            isinstance(a, int) for a in axioms
        ), f"Entry {entry['id']}: axioms_used must contain only ints; got {axioms}"


# ═══════════════════════════════════════════════════════════════════════════
# ID integrity: unique + well-formed across all pre_registered entries
# ═══════════════════════════════════════════════════════════════════════════
class TestPreRegisteredIds:
    """IDs must be unique (no copy-paste dups) and well-formed (no junk)."""

    def test_ids_unique(self):
        ids = [e["id"] for e in _pre_registered_entries()]
        duplicates = sorted({i for i in ids if ids.count(i) > 1})
        assert not duplicates, f"Duplicate pre_registered IDs: {duplicates}"

    @pytest.mark.parametrize("entry", _pre_registered_entries(), ids=lambda e: e["id"])
    def test_id_well_formed(self, entry: dict):
        eid = entry["id"]
        assert isinstance(eid, str) and ID_PATTERN.match(eid), f"Entry id '{eid}' is not a well-formed P_<...> token"

#!/usr/bin/env python3
"""
Predictions Manifest Validator — verifies the structured prediction manifest
in manuscript/predictions.yaml against the manuscript and physics engine.

(Validates the public PREDICTION manifest — the P-numbered Master Prediction
Table rows — NOT the ave-kb clm-/exp-/sup- claim DAG, which is a separate
graph validated by the ave-kb metadata-spine tooling.)

This is the Tier-2 rigor upgrade (see session handoff). Where the
defense_context_checker catches FRAMING anti-patterns via regex, this
validator catches STRUCTURAL inconsistencies:

  1. Manifest schema  — every entry has required fields; no duplicate IDs
  2. Label resolution — every derivation_label resolves to a real
                        \\label{} target in manuscript/**/*.tex (xr-hyper
                        cross-volume refs resolve via the backmatter)
  3. Engine agreement — every constants_py_symbol exists and its live
                        numeric value agrees with predicted_value to rtol=1e-5
  4. DAG bridge       — every `clm:`/`exp:` bridge resolves to a real node of
                        the matching type in the KB claim DAG (.index); the
                        manifest is a one-directional consumer of the spine,
                        not a parallel id system (INVARIANT-S11). Unbridged
                        entries fail (bridge is corpus-complete); broken
                        bridges fail.
  5. Public parity    — every row in the README master table maps to a
                        manifest entry (no undocumented public claims)
  6. Provenance
     reconcile        — every declared `calibration_role` is reconciled against
                        CORPUS-DERIVED provenance statements in the bridged
                        claim's `claim-quality.md` card. NOT a self-check: the
                        field is never validated against itself, against
                        `type`, or against any other hand-written manifest
                        field. See `check_calibration_role` for the frozen
                        marker table + receipts.

Exit codes:
  0 — clean (all structural checks pass)
  1 — validation failures found
  2 — script error (missing manifest, bad YAML, etc.)

Usage:
  python src/scripts/predictions_manifest_validator.py                 # full run
  python src/scripts/predictions_manifest_validator.py --json          # machine output
  python src/scripts/predictions_manifest_validator.py --warn-only     # exit 0 on failures
  python src/scripts/predictions_manifest_validator.py --check label   # one check

Reference: docs/framing_and_presentation.md (Tier 2 proposal),
           manuscript/predictions.yaml (the manifest).
"""
import argparse
import json
import math
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = REPO_ROOT / "manuscript" / "predictions.yaml"
CONSTANTS_PY = REPO_ROOT / "src" / "ave" / "core" / "constants.py"
README_PATH = REPO_ROOT / "README.md"
LIVING_REFERENCE_PATH = REPO_ROOT / "LIVING_REFERENCE.md"
# The KB claim-DAG node index (INVARIANT-S8/S9/S10/S11). The manifest is a
# one-directional reference *consumer* of this graph: an entry bridges INTO
# the spine by `clm:`/`exp:` id, exactly like the closure-roadmap's inline
# annotations. Nothing flows back into the KB — discovery of "which
# predictions cite clm-X" is by grepping this manifest, never a KB reverse edge.
KB_CLAIMS_INDEX = REPO_ROOT / "manuscript" / "ave-kb" / ".index" / "claims.jsonl"

# A manifest entry's bridge into the claim DAG. `clm:` points at a clm- claim
# node; `exp:` points at an exp- experiment node. The bridged id is the
# prediction's identity in the knowledge graph; the entry's own `id:` (the
# P-number) remains its stable public catalog label (README / LIVING_REF rows).
BRIDGE_FIELDS = {"clm": "claim", "exp": "experiment"}
# id-shape guards (parallel to INVARIANT-S8/S9 greppable forms)
_BRIDGE_ID_RE = {
    "clm": re.compile(r"^clm-[a-z0-9]{6}$"),
    "exp": re.compile(r"^exp-[a-z0-9]{6}$"),
}

ALLOWED_TYPES = {
    "derived_prediction",
    "axiom_manifestation",
    "identity",
    "consistency_check",
    "operating_point_projection",  # Class E per `consistency-vs-emergence` v1.1
    "engineering_limit",
}

# Manifest entry-id (public catalog label) shape. Accepts the shipped forms
# `P01`, a range `P11_12`, and the evolved-category form `P_A034_solar_flare`
# / `P_phase5_*`. (Transplanted from the retired test_predictions_matrix.py,
# widened from its pre_registered-only `^P_…` to cover all entries.)
ID_RE = re.compile(r"^P(?:[0-9]+(?:_[0-9]+)?|_[A-Za-z0-9_]+)$")

REQUIRED_FIELDS = {"id", "name", "type", "derivation_label"}

# Entries flagged `pre_registered: true` are forward-looking predictions whose
# derivation lives in a research doc (not yet a manuscript chapter) and whose
# test file is introduced in the same commit as the prediction. They substitute
# `research_doc` + `test_file` for `derivation_label`, and skip label
# resolution. Once the derivation is promoted to a manuscript chapter, the
# entry sheds `pre_registered` and gains a real `derivation_label`.
PRE_REGISTERED_REQUIRED_FIELDS = {
    "id",
    "name",
    "type",
    "pre_registered",
    "research_doc",
    "test_file",
}


# ───────────────────────────────────────────────────────────────────────────
# Findings
# ───────────────────────────────────────────────────────────────────────────
@dataclass
class Finding:
    check: str  # "schema"|"label"|"engine"|"bridge"|"axioms"|"calibration_role"|"parity"
    severity: str  # "critical" | "warn" | "info"
    entry_id: str | None
    message: str
    details: dict[str, Any] = field(default_factory=dict)


# ───────────────────────────────────────────────────────────────────────────
# Loaders
# ───────────────────────────────────────────────────────────────────────────
def load_manifest(path: Path = MANIFEST_PATH) -> dict:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def collect_manuscript_labels(root: Path = REPO_ROOT) -> set[str]:
    """Return all \\label{...} targets across manuscript/**/*.tex."""
    pattern = re.compile(r"\\label\{([^}]+)\}")
    labels: set[str] = set()
    manuscript_dir = root / "manuscript"
    for tex in manuscript_dir.rglob("*.tex"):
        # Exclude build-output / latex-aux .tex by REPO-RELATIVE path component,
        # not an absolute-path substring: a checkout whose worktree dir contains
        # "build" (e.g. /tmp/vol1-build/...) must not skip the real manuscript.
        rel_parts = tex.relative_to(root).parts
        if "build" in rel_parts or "aux" in rel_parts:
            continue
        try:
            text = tex.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for m in pattern.finditer(text):
            labels.add(m.group(1))
    return labels


def collect_constants_symbols(path: Path = CONSTANTS_PY) -> dict[str, float]:
    """
    Import constants.py and read the live values of every float/int
    module-level symbol. Used to cross-check manifest predicted_value
    against the engine's actual output.

    Returns a {symbol: value} map. Symbols whose values are not
    numerically convertible are skipped.
    """
    # Import the module rather than parsing the file — the constants are
    # derived by arithmetic at import time, and we want the same values the
    # test suite and derivation scripts see.
    import importlib
    import sys as _sys

    # (Re-)import to pick up any changes in an interactive session
    if "ave.core.constants" in _sys.modules:
        del _sys.modules["ave.core.constants"]
    module = importlib.import_module("ave.core.constants")

    values: dict[str, float] = {}
    for name in dir(module):
        if name.startswith("_"):
            continue
        v = getattr(module, name)
        if isinstance(v, (int, float)) and not isinstance(v, bool):
            values[name] = float(v)
    return values


def collect_spine_nodes(path: Path = KB_CLAIMS_INDEX) -> dict[str, str]:
    """
    Read the KB claim-DAG node index and return {node_id: node_type} for every
    node (claim / experiment / support / axiom / invariant). Stdlib `json`
    only — the manifest reads the KB as an external graph; it never imports the
    KB tooling. A missing/unbuilt index returns an empty map (the bridge check
    degrades to a warning rather than crashing).
    """
    nodes: dict[str, str] = {}
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return nodes
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        nid = rec.get("id")
        if nid:
            nodes[nid] = rec.get("node_type", "")
    return nodes


KB_DEPENDS_INDEX = REPO_ROOT / "manuscript" / "ave-kb" / ".index" / "depends-on.jsonl"


def collect_dependency_edges(path: Path = KB_DEPENDS_INDEX) -> dict[str, set[str]]:
    """Read the KB depends-on index and return adjacency {source: {targets}}
    for `relation: depends` edges only (not strengthens / supports). Stdlib
    `json`. Missing index → empty map.
    """
    adj: dict[str, set[str]] = {}
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return adj
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            continue
        if e.get("relation") == "depends":
            adj.setdefault(e["source"], set()).add(e["target"])
    return adj


def derive_axioms_used(clm_id: str, adjacency: dict[str, set[str]] | None = None) -> list[int]:
    """Derive a claim's axiom basis by walking its transitive `depends_on`
    cone and collecting every `axiom-N` node reached, returned as a sorted
    list of ints. This is the single source for both the refresh-writer (which
    writes `axioms_used` into bridged manifest entries) and the `check_axioms`
    drift-gate — they must agree, so they share this one function.

    Note: this is a *source-grounded lower bound* — it returns only the axioms
    the claim DAG explicitly chains to. It tightens as more `clm->axiom` edges
    are wired (each grounded in a claim's own cited axiom basis).
    """
    if adjacency is None:
        adjacency = collect_dependency_edges()
    seen: set[str] = set()
    stack = [clm_id]
    axioms: set[int] = set()
    while stack:
        node = stack.pop()
        for target in adjacency.get(node, ()):
            if target.startswith("axiom-"):
                try:
                    axioms.add(int(target.split("-", 1)[1]))
                except ValueError:
                    pass
            elif target not in seen:
                seen.add(target)
                stack.append(target)
    return sorted(axioms)


def _extract_prediction_table_rows(
    path: Path,
    section_header_pattern: str,
) -> list[tuple[str, str]]:
    """
    Shared parser for "Master Prediction Table" style markdown tables.
    Returns (row_id, name) tuples; row_id preserves range syntax like '14–16'.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return []

    match = re.search(
        section_header_pattern + r"(.*?)(?=\n##\s|\Z)",
        text,
        flags=re.DOTALL,
    )
    if not match:
        return []
    table = match.group(1)

    rows: list[tuple[str, str]] = []
    for line in table.split("\n"):
        line = line.strip()
        if not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) < 4:
            continue
        if cols[0] in {"#", "---", ":---"} or set(cols[0]) <= set("-:"):
            continue
        row_id = cols[0]
        name = cols[1]
        name_clean = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", name)
        name_clean = name_clean.strip()
        rows.append((row_id, name_clean))
    return rows


def extract_readme_prediction_rows(readme: Path = README_PATH) -> list[tuple[str, str]]:
    """
    Extract the Master Prediction Table rows from the README. Returns a
    list of (row_id, name) tuples where row_id is the leading '#' column
    (possibly a range like '14–16' or '11–12').
    """
    return _extract_prediction_table_rows(
        readme,
        r"##\s+Master\s+Prediction\s+Table\s*\n",
    )


def extract_living_reference_prediction_rows(
    path: Path = LIVING_REFERENCE_PATH,
) -> list[tuple[str, str]]:
    """
    Extract the Master Prediction Table rows from LIVING_REFERENCE.md.
    The LIVING_REFERENCE header includes a count suffix (e.g. "(47 entries)").
    Rows may be split (separate rows for Δ(1600) and Δ(1900)) where the
    README bundles them — the parity check handles both cases via
    range-inclusion matching.
    """
    return _extract_prediction_table_rows(
        path,
        r"##\s+Master\s+Prediction\s+Table[^\n]*\n",
    )


# ───────────────────────────────────────────────────────────────────────────
# Checks
# ───────────────────────────────────────────────────────────────────────────
def check_schema(manifest: dict) -> list[Finding]:
    """Every entry has required fields; type is allowed; IDs are unique."""
    findings: list[Finding] = []
    entries = manifest.get("predictions", [])
    seen_ids: set[str] = set()

    for entry in entries:
        eid = entry.get("id", "<missing-id>")

        # Required fields — pre_registered entries use a different set
        if entry.get("pre_registered") is True:
            required = PRE_REGISTERED_REQUIRED_FIELDS
        else:
            required = REQUIRED_FIELDS
        missing = required - entry.keys()
        if missing:
            findings.append(
                Finding(
                    check="schema",
                    severity="critical",
                    entry_id=eid,
                    message=f"Entry missing required fields: {sorted(missing)}",
                )
            )

        # Type allowed
        type_val = entry.get("type")
        if type_val not in ALLOWED_TYPES:
            findings.append(
                Finding(
                    check="schema",
                    severity="critical",
                    entry_id=eid,
                    message=(f"Invalid type '{type_val}'. Allowed: {sorted(ALLOWED_TYPES)}"),
                )
            )

        # ID shape (public catalog label must be a well-formed P-token)
        if "id" in entry and not ID_RE.match(str(eid)):
            findings.append(
                Finding(
                    check="schema",
                    severity="critical",
                    entry_id=eid,
                    message=(f"Entry id '{eid}' is not a well-formed P-token (expected P01 / P11_12 / P_<category>)"),
                )
            )

        # Duplicate ID
        if eid in seen_ids:
            findings.append(
                Finding(
                    check="schema",
                    severity="critical",
                    entry_id=eid,
                    message=f"Duplicate entry id '{eid}'",
                )
            )
        seen_ids.add(eid)

        # pre_registered entries must have research_doc + test_file. The
        # research_doc MUST exist (the derivation itself lives there);
        # test_file is a forward commitment — the test lands when the
        # corresponding phase ships, so a missing test_file is a warning
        # (prediction declared, implementation pending) not a critical
        # failure. Once the test exists the warning clears automatically.
        if entry.get("pre_registered") is True:
            # research_doc: MUST exist (critical)
            path_str = entry.get("research_doc")
            if path_str:
                raw = path_str.split("#")[0]
                full = REPO_ROOT / raw
                if not full.exists():
                    findings.append(
                        Finding(
                            check="schema",
                            severity="critical",
                            entry_id=eid,
                            message=(
                                f"pre_registered entry research_doc "
                                f"'{path_str}' does not resolve to a file "
                                f"on disk"
                            ),
                            details={"field": "research_doc", "path": path_str},
                        )
                    )
            # test_file: WARN if missing (phase not yet shipped)
            path_str = entry.get("test_file")
            if path_str:
                raw = path_str.split("#")[0]
                full = REPO_ROOT / raw
                if not full.exists():
                    findings.append(
                        Finding(
                            check="schema",
                            severity="warn",
                            entry_id=eid,
                            message=(
                                f"pre_registered entry test_file "
                                f"'{path_str}' does not exist yet — phase "
                                f"has not shipped. This is expected for "
                                f"forward phases."
                            ),
                            details={"field": "test_file", "path": path_str},
                        )
                    )

    return findings


def check_labels(manifest: dict, labels: set[str] | None = None) -> list[Finding]:
    """Every entry's derivation_label resolves to a \\label{} in the manuscript."""
    findings: list[Finding] = []
    if labels is None:
        labels = collect_manuscript_labels()

    for entry in manifest.get("predictions", []):
        eid = entry.get("id", "<missing-id>")
        # pre_registered entries derive in a research doc, not yet a
        # manuscript chapter; skip label resolution for them
        if entry.get("pre_registered") is True:
            continue
        label = entry.get("derivation_label")
        if label is None:
            continue  # schema check will flag it
        if label not in labels:
            findings.append(
                Finding(
                    check="label",
                    severity="critical",
                    entry_id=eid,
                    message=(
                        f"derivation_label '{label}' does not resolve to any " f"\\label{{}} in manuscript/**/*.tex"
                    ),
                    details={"label": label},
                )
            )

        # Optional eq label
        eq_label = entry.get("derivation_equation")
        if eq_label is not None and eq_label not in labels:
            findings.append(
                Finding(
                    check="label",
                    severity="warn",
                    entry_id=eid,
                    message=(
                        f"derivation_equation '{eq_label}' does not resolve to any "
                        f"\\label{{}} in manuscript/**/*.tex"
                    ),
                    details={"label": eq_label},
                )
            )

    return findings


def check_engine(
    manifest: dict,
    constants: dict[str, float] | None = None,
    rtol: float = 1e-5,
) -> list[Finding]:
    """
    Every entry's constants_py_symbol (if present) resolves, and its live
    value agrees with predicted_value to the given relative tolerance.
    """
    findings: list[Finding] = []
    if constants is None:
        constants = collect_constants_symbols()

    for entry in manifest.get("predictions", []):
        eid = entry.get("id", "<missing-id>")
        symbol = entry.get("constants_py_symbol")
        if symbol is None:
            continue

        if symbol not in constants:
            findings.append(
                Finding(
                    check="engine",
                    severity="critical",
                    entry_id=eid,
                    message=(
                        f"constants_py_symbol '{symbol}' not found in "
                        f"src/ave/core/constants.py module-level float/int "
                        f"symbols"
                    ),
                    details={"symbol": symbol},
                )
            )
            continue

        predicted = entry.get("predicted_value")
        if predicted is None:
            # Symbol present in entry but no value to cross-check — info
            findings.append(
                Finding(
                    check="engine",
                    severity="info",
                    entry_id=eid,
                    message=(
                        f"constants_py_symbol '{symbol}' declared but no " f"predicted_value to cross-check against"
                    ),
                    details={"symbol": symbol, "engine_value": constants[symbol]},
                )
            )
            continue

        engine_value = constants[symbol]
        if engine_value == 0:
            match = predicted == 0
        else:
            match = math.isclose(predicted, engine_value, rel_tol=rtol)

        if not match:
            findings.append(
                Finding(
                    check="engine",
                    severity="critical",
                    entry_id=eid,
                    message=(
                        f"predicted_value {predicted} disagrees with "
                        f"constants.{symbol} = {engine_value} (rtol={rtol})"
                    ),
                    details={
                        "symbol": symbol,
                        "manifest_value": predicted,
                        "engine_value": engine_value,
                        "rtol": rtol,
                    },
                )
            )

    return findings


def check_bridge(
    manifest: dict,
    spine_nodes: dict[str, str] | None = None,
) -> list[Finding]:
    """
    The manifest is a one-directional consumer of the KB claim DAG: each entry
    may bridge INTO the spine via `clm:` (→ a claim node) and/or `exp:` (→ an
    experiment node). This check enforces that every bridge present is:
      - well-formed (`clm-`/`exp-` + 6 lowercase-alphanumerics), and
      - resolves to a real node of the matching node_type in the KB index.

    A *missing* bridge is CRITICAL: as of the corpus-complete bridge (all
    entries bridged), an unbridged prediction is a structural error — it would
    re-open the parallel-id-space that INVARIANT-S11 closes (a prediction that
    references KB knowledge without resolving into the claim DAG). A
    *present-but-broken* bridge is likewise critical — a dangling or mistyped id
    is exactly the silent-rot failure the spine exists to prevent.
    """
    findings: list[Finding] = []
    if spine_nodes is None:
        spine_nodes = collect_spine_nodes()

    if not spine_nodes:
        return [
            Finding(
                check="bridge",
                severity="warn",
                entry_id=None,
                message=(
                    f"KB claim index not found or empty at {KB_CLAIMS_INDEX} — "
                    f"cannot resolve manifest→DAG bridges. Run "
                    f"`make refresh-kb-metadata` to build it."
                ),
            )
        ]

    unbridged: list[str] = []
    for entry in manifest.get("predictions", []):
        eid = entry.get("id", "<missing-id>")
        bridges_present = [f for f in BRIDGE_FIELDS if entry.get(f)]

        if not bridges_present:
            unbridged.append(eid)
            continue

        for fieldname in bridges_present:
            expected_type = BRIDGE_FIELDS[fieldname]
            bridge_id = entry.get(fieldname)
            if not _BRIDGE_ID_RE[fieldname].match(str(bridge_id)):
                findings.append(
                    Finding(
                        check="bridge",
                        severity="critical",
                        entry_id=eid,
                        message=(
                            f"{fieldname} bridge '{bridge_id}' is malformed "
                            f"(expected {fieldname}-<6 lowercase-alphanumerics>)"
                        ),
                        details={"field": fieldname, "bridge": bridge_id},
                    )
                )
                continue
            actual_type = spine_nodes.get(bridge_id)
            if actual_type is None:
                findings.append(
                    Finding(
                        check="bridge",
                        severity="critical",
                        entry_id=eid,
                        message=(f"{fieldname} bridge '{bridge_id}' does not resolve to any node in the KB claim DAG"),
                        details={"field": fieldname, "bridge": bridge_id},
                    )
                )
            elif actual_type != expected_type:
                findings.append(
                    Finding(
                        check="bridge",
                        severity="critical",
                        entry_id=eid,
                        message=(
                            f"{fieldname} bridge '{bridge_id}' resolves to a "
                            f"'{actual_type}' node, expected '{expected_type}'"
                        ),
                        details={
                            "field": fieldname,
                            "bridge": bridge_id,
                            "actual_type": actual_type,
                            "expected_type": expected_type,
                        },
                    )
                )

    if unbridged:
        findings.append(
            Finding(
                check="bridge",
                severity="critical",
                entry_id=None,
                message=(
                    f"{len(unbridged)} of {len(manifest.get('predictions', []))} "
                    f"entries are unbridged (no `clm:`/`exp:` into the claim DAG) "
                    f"— every prediction must resolve into the spine (INVARIANT-S11)"
                ),
                details={"unbridged": unbridged},
            )
        )

    return findings


def check_axioms(
    manifest: dict,
    adjacency: dict[str, set[str]] | None = None,
) -> list[Finding]:
    """`axioms_used` is a DERIVED field for bridged entries: it must equal the
    sorted axiom cone of the entry's `clm:` bridge (see derive_axioms_used).
    `predictions_manifest_refresh.py` writes it; this gate fails if the stored
    value drifts from the recomputed one (refresh-fixable, like the KB's
    subtree-claims / solidity derived fields).

    Only bridged entries are gated — an unbridged entry (no clm/exp) has no DAG
    cone to derive from, so its `axioms_used` stays hand-authored and untouched.
    """
    findings: list[Finding] = []
    if adjacency is None:
        adjacency = collect_dependency_edges()
    if not adjacency:
        return [
            Finding(
                check="axioms",
                severity="warn",
                entry_id=None,
                message=(f"KB depends-on index not found/empty at {KB_DEPENDS_INDEX} — cannot derive axioms_used"),
            )
        ]
    for entry in manifest.get("predictions", []):
        clm = entry.get("clm")
        if not clm:
            continue  # unbridged: axioms_used stays hand-authored
        eid = entry.get("id", "<missing-id>")
        derived = derive_axioms_used(clm, adjacency)
        stored = entry.get("axioms_used")
        stored_sorted = sorted(stored) if isinstance(stored, list) else stored
        if stored_sorted != derived:
            findings.append(
                Finding(
                    check="axioms",
                    severity="critical",
                    entry_id=eid,
                    message=(
                        f"axioms_used {stored} drifts from the derived cone of "
                        f"{clm} = {derived} (run predictions_manifest_refresh.py)"
                    ),
                    details={"clm": clm, "stored": stored, "derived": derived},
                )
            )
    return findings


# ───────────────────────────────────────────────────────────────────────────
# calibration_role reconciler — declared provenance vs CORPUS-DERIVED truth
# ───────────────────────────────────────────────────────────────────────────
# WHY THIS EXISTS. `calibration_role` (manuscript/predictions.yaml:29-35) is a
# self-declared honesty field. Before this check it had ZERO consumers
# corpus-wide: checks 1-5 gate schema / labels / engine / bridge / parity but
# none of them read it, so it was free to drift from the corpus grading forever.
#
# THE DISCIPLINE THIS CHECK IS BUILT TO SATISFY. A gate that consumes a
# self-declared field is a checklist, not a gate. So this check NEVER validates
# `calibration_role` against itself, against `type`, against `notes`, or against
# any other hand-authored manifest field. Its only authority is the CORPUS: the
# bridged claim's card in `manuscript/ave-kb/**/claim-quality.md` — the same
# authority that grades solidity, written by a different pass, in a different
# file, under a different review gate.
#
# THE AXIS. `calibration_role` is the value-PROVENANCE axis of the FORM-deriving
# / VALUE-importing meta-finding (canonical:
# manuscript/ave-kb/common/form-deriving-value-importing.md — "The geometry and
# topology of the chiral K4 Cosserat substrate FORCE the dimensionless FORMS
# (the 'chords'). The dimensionful VALUES ... are calibration INPUTS it does not
# independently select (the 'echoes')."). Its machine-enforced per-mechanism
# sibling is `real_or_fitted` on `ilk-` nodes (INVARIANT-S13,
# manuscript/ave-kb/common/interlock-register.md) — but that register is
# per-CALIBRATION-CONSTANT (4 nodes), not per-prediction-row, so it cannot
# adjudicate the 36 manifest rows. The per-row authority is the claim card.
#
# NOT SOLIDITY. `solidity` is a CONFIDENCE axis; `calibration_role` is a
# PROVENANCE axis. They are orthogonal — a 0.9-solidity claim can be a pure echo
# and a 0.3-solidity claim can be a chord. No rule below reads solidity,
# confidence, build_status, or build_band. Deriving a role from solidity would
# be a category error that makes the gate wrong, so it is not done. Solidity
# never enters this check at all: not as an input, and not as context in the
# finding `details` either — the details dict carries declared / clm / card /
# verdict / signals / forbidding_signals / surviving_roles / suggested /
# receipts, and nothing else.
#
# THE `check_axioms` PRECEDENT — SAME ARCHITECTURE, WEAKER EPISTEMICS. This is
# check #6 inside the existing validator rather than a new script because
# `check_axioms` is the same SHAPE: a manifest field reconciled against
# KB-derived truth (there the axiom cone, here the provenance card). But the
# two are NOT epistemic peers, and that difference is exactly why their gating
# postures differ:
#
#   check_axioms       `axioms_used` is MACHINE-WRITTEN (by
#                      predictions_manifest_refresh.py) and GRAPH-DERIVED (the
#                      transitive axiom cone of the clm bridge). Recomputing it
#                      is deterministic and the drift is refresh-fixable, so it
#                      gates at severity="critical".
#   this check         `calibration_role` is HAND-AUTHORED, and the truth it is
#                      reconciled against is REGEX-OVER-PROSE. There is no
#                      recompute-and-diff; there is pattern-matching on English
#                      written by humans for humans, with two suppression
#                      guards whose scope is itself a judgement call. So it
#                      reports at severity="warn" until its named backlog is
#                      ruled (see the flip condition in check_calibration_role).
#
# Claiming these as equal precedent would overstate the gate. The architecture
# is borrowed; the authority is not.
#
# HOW A ROLE IS FALSIFIED, NOT GUESSED. The corpus rarely says "this row is a
# chord" in so many words, but it very often says the opposite in plain text:
# "GR-imported", "import-capped", "disclosed-phenomenological", "the magnitude
# is FITTED", "a category (iii) consistency check". So the reconciler is a
# CONTRADICTION detector over a frozen table of EXPLICIT corpus phrases. Each
# marker forbids a role SET; a declared role inside the forbidden set is a
# contradiction. Where the card states no provenance at all the verdict is
# UNRECONCILED — reported, never guessed. That asymmetry is deliberate:
# positive derivation language ("zero free parameters") CANNOT license `chord`,
# because a forced FORM is equally consistent with `mixed` (form-derived,
# value-imported). So FORM_FORCED forbids nothing; it only informs the advisory
# `suggested` field.

KB_ROOT = REPO_ROOT / "manuscript" / "ave-kb"

# The taxonomy declared at manuscript/predictions.yaml:30-35. An entry outside
# this set is a precondition failure (the reconciler cannot reason about an
# unknown role) — NOT a reconciliation verdict.
ALLOWED_CALIBRATION_ROLES = {
    "chord",
    "echo",
    "mixed",
    "fitted",
    "consistency",
    "forward-prediction",
}


@dataclass(frozen=True)
class ProvenanceMarker:
    """An EXPLICIT corpus phrase that constrains a row's value-provenance.

    `forbids` is the set of `calibration_role` values the phrase rules out.
    `receipt` names the corpus site where the phrase was verified to carry that
    meaning (verify-before-cite: every pattern below was grep-confirmed against
    the live cards, not inferred).
    """

    signal: str
    pattern: str
    forbids: frozenset[str]
    receipt: str


# ── Two independent suppression guards ────────────────────────────────────
# Both exist to stop FALSE POSITIVES. Both are themselves bounded, because an
# over-broad suppressor is a FALSE NEGATIVE generator — and a detector that
# silently declines to fire is a checklist wearing a gate's clothes, which is
# the exact failure mode this whole check exists to kill. Every relaxation
# below is regression-tested in BOTH directions: `TestCalibrationRole`'s
# false-positive tests (the guard must fire) and its anti-over-suppression
# tests (the guard must NOT fire), the latter keyed to live corpus sites.
#
# GUARD 1 — NEGATION, clause-scoped. A marker match is discarded only if a
# negation token governs it: the token must lie inside `_NEGATION_WINDOW`
# characters AND inside the SAME CLAUSE. The clause clamp is the repair for a
# measured over-suppression: a bare character window reaches backwards across
# sentence and clause boundaries and kills affirmations. Five live sites were
# being silently discarded by the unclamped window, e.g.
#   vol2/claim-quality.md:120 (clm-5zuo7g) "…value, NOT a free framework
#     input; so the FORM … is derived but the VALUE …" — the NOT scopes over
#     "a free framework input" and AFFIRMS the import, on the far side of a ';'
#   vol2/claim-quality.md:1531 (clm-3i66gp) "…not an AVE numerical output.
#     Structural/consistency-class only." — negation in the PREVIOUS sentence
#   common/claim-quality.md:1477 (clm-strreg) "**RULED CONVENTION, NOT A
#     DERIVATION — consistency-class.**" — denial, em-dash, then affirmation
# A '.' ';' ':' '!' '?' only counts as a boundary when followed by whitespace,
# so decimals ("solidity 0.55") and version strings cannot fake one; ')' counts
# because a negation sealed inside a parenthetical cannot govern text outside
# it; '—'/'–' count because an em-dash separates an assertion from its clause.
# A bare ',' does NOT count — "not an identity or consistency check" must stay
# suppressed, and so must a negated comma list ("not a chord, a consistency
# check, or an identity") — but a comma followed by a clause-initial
# pronoun+copula DOES ("This is not novel, it is a consistency check", the
# near-canonical AVE self-description form). Measured: the comma rule changes
# NOTHING on the live corpus today (suppression-event set identical with and
# without it); it is carried for the constructed class, and its scope is
# pinned by tests in both directions.
_NEGATION_WINDOW = 40
_NEGATION_RE = re.compile(r"\bnot\b", re.I)
_CLAUSE_BOUNDARY_RE = re.compile(
    r"(?:[.;:!?](?=\s|$)"
    r"|[\n—–)]"
    r"|,(?=\s+(?:it|this|that|they|these|those|which)\s+(?:is|are|was|were)\b))"
)

# GUARD 2 — ENUMERATION. `vs` was previously carried in the negation lexicon.
# It is not a negation, it is a COMPARISON marker, and treating it as one
# produced false negatives on ordinary comparative prose ("sub-1 ppm vs
# CODATA). Classification is largely a consistency check…", clm-qde5gn;
# "(−5.2% vs measured), zero free parameters", clm-m7qd0w). What actually
# needs suppressing is the narrower ENUMERATION form — a list of taxonomy
# CATEGORY NAMES being distinguished from one another rather than a grading of
# this claim: "derived predictions vs consistency checks vs identities"
# (vol2/claim-quality.md:903, clm-xhdai6, a strengthen-by task line). The tell
# is that `vs` flanks the match on BOTH sides inside one clause; a single
# trailing or leading `vs` is just a comparison and suppresses nothing.
_ENUM_BEFORE_RE = re.compile(r"\b(?:vs\.?|versus)\s+$")
_ENUM_AFTER_RE = re.compile(r"^\w*[\s,]+(?:vs\.?|versus)\b")
_ENUM_WINDOW = 40

PROVENANCE_MARKERS: tuple[ProvenanceMarker, ...] = (
    # ── VALUE_IMPORTED ── the card states the row's value comes from outside
    # the substrate. Forbids `chord` only: an imported value is by definition
    # not "a FORM/ratio/selection-rule AVE genuinely forces" (predictions.yaml:30).
    ProvenanceMarker(
        "VALUE_IMPORTED",
        r"\bGR-imported\b",
        frozenset({"chord"}),
        "vol2/claim-quality.md clm-5zuo7g depends-on note; taxonomy row "
        "'K = 2G ... GR-IMPORTED (echo for the value)' in "
        "common/form-deriving-value-importing.md",
    ),
    ProvenanceMarker(
        "VALUE_IMPORTED",
        r"\bimport-capped\b",
        frozenset({"chord"}),
        "vol2/claim-quality.md clm-5zuo7g: 'the FORM ... is derived but the "
        "VALUE $2/9$ is import-capped'",
    ),
    ProvenanceMarker(
        "VALUE_IMPORTED",
        r"disclosed imports? (?:are|is)\b",
        frozenset({"chord"}),
        "vol2/claim-quality.md clm-5zuo7g rationale + clm-d9ivj1 rationale",
    ),
    ProvenanceMarker(
        "VALUE_IMPORTED",
        r"back-?solved\b",
        frozenset({"chord"}),
        "common/claim-quality.md:452 clm-dsb560 (live firing site: 'u₀* is "
        "back-solved from CODATA α, G'); meaning verified at "
        "common/interlock-register.md:216 ilk-gravmb: 'back-solved from CODATA "
        "G ... circular by construction'",
    ),
    ProvenanceMarker(
        "VALUE_IMPORTED",
        r"\bimported, not derived\b",
        frozenset({"chord"}),
        "vol3/claim-quality.md clm-c6k5om rationale: 'the standard formula "
        "imported, not derived'",
    ),
    # ── VALUE_FITTED ── the card states the value / its extension is fitted,
    # tuned, or disclosed-phenomenological. Same forbid set, different evidence
    # class (a fit is not an import).
    ProvenanceMarker(
        "VALUE_FITTED",
        r"disclosed[- ]phenomenological",
        frozenset({"chord"}),
        "vol3/claim-quality.md clm-395gps Non-Claims + rationale; "
        "vol2/claim-quality.md clm-d9ivj1",
    ),
    ProvenanceMarker(
        "VALUE_FITTED",
        r"phenomenological[^.]{0,120}(?:formula|shift|fit\b)",
        frozenset({"chord"}),
        "vol3/claim-quality.md clm-395gps: 'a phenomenological photon-sphere "
        "shift formula'; vol2/claim-quality.md clm-4vwsjc",
    ),
    ProvenanceMarker(
        "VALUE_FITTED",
        r"\bis \*{0,2}FITTED\b",
        frozenset({"chord"}),
        "vol1/claim-quality.md clm-009nkt rationale: 'the magnitude "
        "$\\delta_{strain}$ ... is FITTED'",
    ),
    ProvenanceMarker(
        "VALUE_FITTED",
        r"\brefined post-hoc\b|\bpost-hoc against\b",
        frozenset({"chord"}),
        "vol3/claim-quality.md clm-395gps rationale: 'Cosserat back-reaction "
        "fit (v2, refined post-hoc against LIGO)'",
    ),
    ProvenanceMarker(
        "VALUE_FITTED",
        r"back-reaction fit\b",
        frozenset({"chord"}),
        "vol3/claim-quality.md clm-395gps rationale",
    ),
    # ── FORM_VS_VALUE_SPLIT ── the card states the FORM/VALUE split verbatim.
    # This is the `mixed` definition (predictions.yaml:32) written out longhand,
    # so it forbids `chord` and drives the `mixed` suggestion.
    #
    # AUDIT NOTE (2026-08-04). This marker shipped DEAD: it fired on 0 of 329
    # cards, because the only site it matches is its own receipt and the
    # unclamped negation window discarded it there. A table row that has never
    # fired, whose receipt is its own suppression site, is decoration. The
    # clause-scoped guard repair released it; re-measured, it fires on exactly
    # 1 of 329 cards — clm-5zuo7g, the receipt below — so the receipt is honest
    # and the row is kept. `test_form_vs_value_split_fires_on_its_live_receipt`
    # pins that, and `test_every_marker_fires_somewhere_in_the_live_corpus`
    # stops any marker from going dead again unnoticed.
    ProvenanceMarker(
        "FORM_VS_VALUE_SPLIT",
        r"FORM[^.]{0,220}is derived but the VALUE",
        frozenset({"chord"}),
        "vol2/claim-quality.md:120 clm-5zuo7g depends-on note (sole live site, "
        "verified firing); the axis itself is "
        "common/form-deriving-value-importing.md",
    ),
    # ── CONSISTENCY_CLASS ── the card grades the claim as reproducing a known
    # result. Forbids `chord` (not AVE-forced-novel) and `forward-prediction`
    # (predictions.yaml:35 — 'untested, divergent-from-SM, AVE-distinct').
    ProvenanceMarker(
        "CONSISTENCY_CLASS",
        r"consistency check",
        frozenset({"chord", "forward-prediction"}),
        "vol3/claim-quality.md clm-zf8eah: 'This is a **consistency check** "
        "(category iii)'; 8 further live sites",
    ),
    ProvenanceMarker(
        "CONSISTENCY_CLASS",
        r"category \(iii\)",
        frozenset({"chord", "forward-prediction"}),
        "vol3/claim-quality.md clm-3kmt3p Non-Claims",
    ),
    ProvenanceMarker(
        "CONSISTENCY_CLASS",
        r"consistency-class",
        frozenset({"chord", "forward-prediction"}),
        "vol3/claim-quality.md clm-395gps: 'the spinning match is "
        "consistency-class'",
    ),
    # ── IDENTITY_CLASS ── the card grades the value as definitional.
    ProvenanceMarker(
        "IDENTITY_CLASS",
        r"definitional[- ](?:identity|residual)",
        frozenset({"chord", "forward-prediction"}),
        "vol1/claim-quality.md clm-009nkt + clm-0ktpcn rationale",
    ),
    # ── CONSISTENCY_DENIED ── the card explicitly refuses the consistency
    # grading. The reverse direction: this forbids `consistency`, not `chord`.
    ProvenanceMarker(
        "CONSISTENCY_DENIED",
        r"not an identity or consistency check|NOT a consistency check",
        frozenset({"consistency"}),
        "vol3/claim-quality.md clm-395gps Specific Claims: 'a category (iv) "
        "derived prediction, not an identity or consistency check'",
    ),
    # ── NOT_SM_DISTINGUISHABLE ── the card says the result is not
    # distinguishable from the standard one. Forbids `forward-prediction`.
    ProvenanceMarker(
        "NOT_SM_DISTINGUISHABLE",
        r"not (?:a )?(?:novel )?[a-z ]{0,30}distinguishable from",
        frozenset({"forward-prediction"}),
        "vol3/claim-quality.md clm-3kmt3p: 'not a novel mechanism "
        "distinguishable from classical resonance theory'; vol2 clm-7o8clt",
    ),
    # ── DEVIATION_DISCLAIMED ── the card explicitly disclaims predicting a
    # NON-ZERO deviation. `forward-prediction` is defined at
    # predictions.yaml:35 as "untested, divergent-from-SM, AVE-distinct"; a card
    # that refuses to predict a departure is stating a null that matches the
    # standard expectation, so it cannot be divergent-from-SM. Forbids ONLY
    # `forward-prediction` — a null can still be a forced form (α-invariance
    # under symmetric gravity IS a forced cancellation), so `chord` is untouched
    # and no import/fit is implied.
    ProvenanceMarker(
        "DEVIATION_DISCLAIMED",
        r"[Dd]oes NOT claim[^.]{0,160}(?:\\neq|\\ne)\s*0",
        frozenset({"forward-prediction"}),
        "claim-quality.md:145 clm-3zz0f6 Non-Claims: 'Does NOT claim the "
        "framework predicts $\\Delta\\alpha \\neq 0$ in any gravitational "
        "regime.' (sole live site; 1 of 329 cards)",
    ),
    # ── FORM_FORCED ── EVIDENCE ONLY, forbids NOTHING. A forced FORM is equally
    # consistent with `chord` and with `mixed`, so it can neither license nor
    # rule out a role. It only informs the advisory `suggested` field. Encoding
    # it as a licence would be the exact failure this check exists to prevent.
    ProvenanceMarker(
        "FORM_FORCED",
        r"zero free parameters",
        frozenset(),
        "vol3/claim-quality.md clm-395gps, vol2 clm-5zuo7g / clm-gfs4j8 / "
        "clm-oltvwy",
    ),
    ProvenanceMarker(
        "FORM_FORCED",
        r"category[ -]\(iv\)[ -]derived prediction",
        frozenset(),
        "vol3/claim-quality.md clm-395gps + 4 further live sites",
    ),
)

_CLAIM_CARD_ID_RE = re.compile(r"^<!--\s*id:\s*(clm-[a-z0-9]{6})\s*-->\s*$", re.M)
_CARD_HEADING_RE = re.compile(r"^## ", re.M)


def collect_claim_cards(kb_root: Path = KB_ROOT) -> dict[str, tuple[str, str, int]]:
    """Return {clm_id: (card_text, repo_relative_path, start_line)} for every
    claim card in the KB's `claim-quality.md` registers.

    A "card" is the full `## <title>` section that owns the `<!-- id: clm-… -->`
    marker — Specific Claims, Specific Non-Claims and Caveats, and the Quality
    block (confidence / depends-on / solidity / rationale / strengthen-by).

    WHY FROM DISK AND NOT FROM `.index/`. Two reasons, and the first one has to
    be stated narrowly or it is wrong:

    1. `.index/claims.jsonl` materializes `rationale` but NOT the Specific
       Non-Claims lines, and the Non-Claims block is where the corpus most
       often states provenance outright ("Does NOT claim derivation of …",
       "disclosed phenomenological …"). That is the real gap.
       It is NOT true that "the index drops the evidence" in general:
       `.index/depends-on.jsonl` carries P04's evidence VERBATIM in its
       `context` field — "the vacuum Poisson ratio $2/7$ is the GR-imported
       trace-reversal value, NOT a free framework input; so the FORM … is
       derived but the VALUE $2/9$ is import-capped" — which is the exact text
       both VALUE_IMPORTED and FORM_VS_VALUE_SPLIT fire on. So the index would
       have served P04; it would not serve the Non-Claims class.

    2. Reading raw markdown also keeps the CONFIDENCE axis out of the gate's
       reach as STRUCTURED data. A `claims.jsonl` record exposes `solidity`,
       `derivation_solidity`, `build_status` and `build_band` as typed fields
       sitting next to `rationale`, and `depends-on.jsonl` exposes
       `target_solidity_recorded`. On disk those are just prose lines inside a
       card, indistinguishable from any other text and matched by no marker.
       Provenance and confidence are orthogonal axes; the loader should not
       hand the gate a convenient typed handle on the wrong one.

    Test fixtures under `tools/tests/` are excluded — they carry synthetic ids.
    A missing/unreadable KB returns an empty map (the check degrades to a
    single warn rather than crashing).
    """
    cards: dict[str, tuple[str, str, int]] = {}
    if not kb_root.is_dir():
        return cards
    for path in sorted(kb_root.rglob("claim-quality.md")):
        rel_parts = path.relative_to(kb_root).parts
        if "tools" in rel_parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        rel = str(path.relative_to(REPO_ROOT))
        for m in _CLAIM_CARD_ID_RE.finditer(text):
            clm_id = m.group(1)
            head = text.rfind("\n## ", 0, m.start())
            start = head + 1 if head >= 0 else m.start()
            nxt = _CARD_HEADING_RE.search(text, m.end())
            end = nxt.start() if nxt else len(text)
            start_line = text.count("\n", 0, start) + 1
            cards[clm_id] = (text[start:end], rel, start_line)
    return cards


def _clause_prefix(card_text: str, start: int) -> str:
    """The text governing `start`: back to the nearest clause boundary, capped
    at `_NEGATION_WINDOW` characters. A negation outside this span is in a
    different clause or sentence and does not govern the match."""
    window = card_text[max(0, start - _NEGATION_WINDOW) : start]
    bounds = list(_CLAUSE_BOUNDARY_RE.finditer(window))
    return window[bounds[-1].end() :] if bounds else window


def _is_negated(card_text: str, start: int) -> bool:
    """True if a negation token governs the match at `start` (GUARD 1)."""
    return bool(_NEGATION_RE.search(_clause_prefix(card_text, start)))


def _is_enumeration(card_text: str, start: int, end: int) -> bool:
    """True if the match is an item in an `X vs Y vs Z` category list (GUARD 2).

    Requires `vs`/`versus` on BOTH sides within the governing clause — a single
    `vs` is a comparison, not an enumeration, and must not suppress.
    """
    if not _ENUM_BEFORE_RE.search(_clause_prefix(card_text, start)):
        return False
    tail = card_text[end : end + _ENUM_WINDOW]
    bound = _CLAUSE_BOUNDARY_RE.search(tail)
    return bool(_ENUM_AFTER_RE.search(tail[: bound.start()] if bound else tail))


def scan_provenance(card_text: str) -> list[tuple[ProvenanceMarker, str]]:
    """Return the (marker, verbatim excerpt) pairs the card text supports.

    A match is discarded only if GUARD 1 (a negation token governing it inside
    the same clause) or GUARD 2 (an `X vs Y vs Z` category enumeration) applies
    — see the two guard blocks above. Every surviving hit carries its verbatim
    excerpt so a reviewer can audit the verdict without re-reading the card: a
    gate that cannot show its receipt is a checklist.
    """
    hits: list[tuple[ProvenanceMarker, str]] = []
    for marker in PROVENANCE_MARKERS:
        for m in re.finditer(marker.pattern, card_text):
            if _is_negated(card_text, m.start()) or _is_enumeration(
                card_text, m.start(), m.end()
            ):
                continue
            lo = max(0, m.start() - 70)
            hi = min(len(card_text), m.end() + 70)
            excerpt = " ".join(card_text[lo:hi].split())
            hits.append((marker, excerpt))
            break  # one receipt per marker is enough
    return hits


def suggest_role(signals: set[str]) -> str | None:
    """ADVISORY only — never a verdict input, never auto-applied.

    Reads the corpus signal set and names the taxonomy value it most nearly
    matches (predictions.yaml:30-35). `mixed` = "form-derived but value rides
    echoes ± a fitted scalar", so a card carrying BOTH a forced form and an
    imported/fitted value maps there; an import/fit with no forced form maps to
    `echo`; a consistency/identity grading maps to `consistency`.
    """
    imported_or_fitted = signals & {"VALUE_IMPORTED", "VALUE_FITTED"}
    if "FORM_VS_VALUE_SPLIT" in signals:
        return "mixed"
    if imported_or_fitted and "FORM_FORCED" in signals:
        return "mixed"
    if imported_or_fitted:
        return "echo"
    if signals & {"CONSISTENCY_CLASS", "IDENTITY_CLASS"}:
        return "consistency"
    return None


def check_calibration_role(
    manifest: dict,
    cards: dict[str, tuple[str, str, int]] | None = None,
    severity: str = "warn",
) -> list[Finding]:
    """Reconcile each declared `calibration_role` against its bridged claim card.

    Verdicts:
      RECONCILED   — declared role is not in any forbidden set. No finding.
      CONTRADICTED — declared role IS forbidden by ≥1 explicit corpus marker.
                     One finding at `severity`, carrying the verbatim excerpt,
                     the marker receipt, and the card's file:line.
      UNRECONCILED — the card states no provenance at all. Reported at `info`;
                     never guessed, never defaulted to a role.
      (unbridged / undeclared rows are skipped — nothing to reconcile.)

    `severity` is the gating knob: "warn" = report-only (the tool's exit code
    keys on criticals), "critical" = gating.

    FIRST-RUN CENSUS (2026-08-04, 36 manifest rows, HEAD 2b30d9eb) — the
    measurement that set the initial posture:

        UNDECLARED    12   (field absent; optional, nothing to reconcile)
        RECONCILED    11
        UNRECONCILED  11   (card states no provenance — info, never gating)
        CONTRADICTED   2   P04 (chord) and P_A034_bh_ringdown (chord)

    Both contradictions were the manifest's only two `chord` rows, and the
    corpus contradicts both — the expected shape, since `chord` is the one role
    that asserts "AVE genuinely forces this" and therefore the one role an
    import/fit statement can falsify.

    CENSUS AFTER THE AUDIT REPAIR PASS (2026-08-04, same 36 rows), i.e. after
    the one authorized relabel + the clause-scoped guard + DEVIATION_DISCLAIMED:

        UNDECLARED    12
        RECONCILED    12   (+1: P_A034_bh_ringdown, relabelled chord -> mixed)
        UNRECONCILED  10   (-1: P42, now detected)
        CONTRADICTED   2   P04 (chord) and P42 (forward-prediction)

    The guard repair alone moved NO row — it only strengthened P04's receipt
    (VALUE_IMPORTED -> VALUE_IMPORTED + FORM_VS_VALUE_SPLIT), because the five
    other markers it released sit on cards no manifest row bridges to. P42
    moved because DEVIATION_DISCLAIMED mechanized a judgement that was
    previously carried as a prose footnote for human eyes.

    CENSUS AFTER THE P04 RULING (2026-08-05, same 36 rows) — Grant ruled P04
    `chord` -> `mixed`, the role the reconciler's corpus-derived suggestion
    named, and the relabel landed with its two execution riders on the row:

        UNDECLARED    12
        RECONCILED    13   (+1: P04, relabelled chord -> mixed)
        UNRECONCILED  10
        CONTRADICTED   1   P42 (forward-prediction)

    POSTURE = REPORT-ONLY (`severity="warn"`), not gating. ONE contradiction
    remains open, and it is an adjudication rather than a sweep:

      P04  RULED AND LANDED 2026-08-05 (Grant): `chord` -> `mixed`. The card
           states the value is GR-imported and import-capped, so the FORM is
           derived while the VALUE rides `K = 2G` — the `mixed` shape. The
           row now also carries the K=2G upgrade path (the R11 forced-form
           lane, whose attack is the clm-satnec static-existence test) and an
           explicit on-shell scheme declaration. Reconciles clean; not a
           backlog item any more.
      P42  declares `forward-prediction` on clm-3zz0f6, whose card says α is
           "exactly invariant", "Multi-species $\\Delta\\alpha/\\alpha = 0$",
           and "Does NOT claim the framework predicts $\\Delta\\alpha \\neq 0$
           in any gravitational regime" — a null matching the standard
           expectation, which is the opposite of predictions.yaml:35's
           "untested, divergent-from-SM, AVE-distinct". Grant approved
           re-roling it off `forward-prediction` on 2026-08-05 with a
           MANDATORY condition: an independent Tier-1 language-and-logic read
           of the replacement wording BEFORE it lands. So the row is ruled in
           direction but NOT yet landed, and the gate stays `warn`.

    Gating now would fail `make verify` repo-wide on an open adjudication,
    and the gate would get bypassed.

    FLIP CONDITION (named, so this does not drift into permanent advisory):
    once BOTH P04 and P42 are ruled AND their relabels have LANDED, register
    this check with `severity="critical"`. The backlog is two named rows, not
    a class of rows. Flipping with either still contradicting would red-gate
    the repo on a label a human already suspects is wrong — which is how gates
    get disabled.

      P04  DONE — ruled and landed 2026-08-05; verdict RECONCILED.
      P42  REMAINING — ruled in direction 2026-08-05, wording pending the
           independent Tier-1 read; verdict still CONTRADICTED.

    So exactly one row now stands between this check and `critical`.
    """
    findings: list[Finding] = []
    if cards is None:
        cards = collect_claim_cards()
    if not cards:
        return [
            Finding(
                check="calibration_role",
                severity="warn",
                entry_id=None,
                message=(
                    f"No claim cards found under {KB_ROOT} — cannot reconcile "
                    f"declared calibration_role against corpus provenance."
                ),
            )
        ]

    for entry in manifest.get("predictions", []):
        eid = entry.get("id", "<missing-id>")
        declared = entry.get("calibration_role")
        if declared is None:
            continue  # optional field, not declared — nothing to reconcile

        if declared not in ALLOWED_CALIBRATION_ROLES:
            findings.append(
                Finding(
                    check="calibration_role",
                    severity="critical",
                    entry_id=eid,
                    message=(
                        f"calibration_role '{declared}' is not in the declared "
                        f"taxonomy {sorted(ALLOWED_CALIBRATION_ROLES)} "
                        f"(manuscript/predictions.yaml:30-35) — the reconciler "
                        f"cannot reason about an unknown role"
                    ),
                    details={"declared": declared, "verdict": "UNKNOWN_ROLE"},
                )
            )
            continue

        clm = entry.get("clm")
        if not clm:
            continue  # unbridged: no corpus card to reconcile against
        card = cards.get(clm)
        if card is None:
            findings.append(
                Finding(
                    check="calibration_role",
                    severity="warn",
                    entry_id=eid,
                    message=(
                        f"calibration_role '{declared}' declared but bridged "
                        f"claim {clm} has no claim-quality card to reconcile "
                        f"against"
                    ),
                    details={"declared": declared, "clm": clm, "verdict": "NO_CARD"},
                )
            )
            continue

        card_text, card_path, card_line = card
        hits = scan_provenance(card_text)
        if not hits:
            findings.append(
                Finding(
                    check="calibration_role",
                    severity="info",
                    entry_id=eid,
                    message=(
                        f"calibration_role '{declared}' is UNRECONCILED — the "
                        f"card for {clm} ({card_path}:{card_line}) states no "
                        f"explicit value-provenance. Not a contradiction; the "
                        f"corpus is silent, so no role is inferred."
                    ),
                    details={
                        "declared": declared,
                        "clm": clm,
                        "card": f"{card_path}:{card_line}",
                        "verdict": "UNRECONCILED",
                    },
                )
            )
            continue

        signals = {mk.signal for mk, _ in hits}
        forbidden: dict[str, list[str]] = {}
        for mk, excerpt in hits:
            if declared in mk.forbids:
                forbidden.setdefault(mk.signal, []).append(excerpt)

        if not forbidden:
            continue  # RECONCILED

        # The rules ELIMINATE; they do not select. Report what survives, and
        # say plainly when the advisory has nothing to offer rather than
        # printing 'None' as though it were a role.
        suggested = suggest_role(signals)
        survivors = sorted(
            ALLOWED_CALIBRATION_ROLES - {r for mk, _ in hits for r in mk.forbids}
        )
        advice = (
            f"Corpus-derived suggestion: '{suggested}'"
            if suggested
            else "No suggestion — the corpus eliminates but does not select here"
        )

        findings.append(
            Finding(
                check="calibration_role",
                severity=severity,
                entry_id=eid,
                message=(
                    f"calibration_role '{declared}' CONTRADICTS the corpus "
                    f"grading of {clm} ({card_path}:{card_line}): the card "
                    f"carries {sorted(forbidden)}, which rule(s) out "
                    f"'{declared}'. Roles not eliminated: {survivors}. {advice}"
                ),
                details={
                    "declared": declared,
                    "clm": clm,
                    "card": f"{card_path}:{card_line}",
                    "verdict": "CONTRADICTED",
                    "signals": sorted(signals),
                    "forbidding_signals": {k: v for k, v in sorted(forbidden.items())},
                    "surviving_roles": survivors,
                    "suggested": suggested,
                    "receipts": sorted(
                        {mk.receipt for mk, _ in hits if mk.signal in forbidden}
                    ),
                },
            )
        )

    return findings


def check_readme_parity(manifest: dict) -> list[Finding]:
    """
    Every row in the README Master Prediction Table maps to a manifest
    entry. Mapping is by id: the README '#' column '14–16' maps to entry
    id 'P14_16' or 'P14-16'.
    """
    findings: list[Finding] = []
    rows = extract_readme_prediction_rows()
    if not rows:
        return [
            Finding(
                check="parity",
                severity="warn",
                entry_id=None,
                message="Could not parse the Master Prediction Table from README.md",
            )
        ]

    # Index manifest by id and by normalized id
    entries_by_id: dict[str, dict] = {e["id"]: e for e in manifest.get("predictions", []) if "id" in e}

    def normalize_row_id(raw: str) -> str:
        # Remove markdown emphasis / whitespace
        cleaned = raw.strip()
        # "14–16" / "14-16" → P14_16
        cleaned = cleaned.replace("–", "-").replace("—", "-")
        cleaned = cleaned.replace("-", "_")
        return f"P{cleaned.zfill(0)}" if cleaned.isdigit() else f"P{cleaned}"

    def candidate_ids(raw: str) -> list[str]:
        """Yield possible manifest IDs for a README row id."""
        cleaned = raw.strip().replace("–", "-").replace("—", "-")
        out = [f"P{cleaned.replace('-', '_')}"]
        if cleaned.isdigit():
            # "1" → "P01" (zero-padded)
            out.append(f"P{int(cleaned):02d}")
        return out

    for row_id, name in rows:
        matched = False
        for cand in candidate_ids(row_id):
            if cand in entries_by_id:
                matched = True
                break
        if not matched:
            findings.append(
                Finding(
                    check="parity",
                    severity="warn",
                    entry_id=None,
                    message=(
                        f"README prediction row '{row_id}' ({name!r}) has no "
                        f"matching entry in manuscript/predictions.yaml"
                    ),
                    details={"row_id": row_id, "name": name},
                )
            )

    return findings


def _id_range_contains(eid: str, row_num: int) -> bool:
    """True if manifest ID is a range (e.g., 'P11_12') covering row_num."""
    m = re.fullmatch(r"P(\d+)_(\d+)", eid)
    if not m:
        return False
    lo, hi = int(m.group(1)), int(m.group(2))
    return lo <= row_num <= hi


def check_living_reference_parity(manifest: dict) -> list[Finding]:
    """
    Every row in the LIVING_REFERENCE.md Master Prediction Table maps to a
    manifest entry. Matches via (a) exact ID, (b) zero-padded ID, or
    (c) range-inclusion (a split LR row like '11' or '12' both map to the
    bundled manifest entry 'P11_12').
    """
    findings: list[Finding] = []
    rows = extract_living_reference_prediction_rows()
    if not rows:
        return [
            Finding(
                check="parity",
                severity="warn",
                entry_id=None,
                message=("Could not parse the Master Prediction Table from " "LIVING_REFERENCE.md"),
            )
        ]

    entries_by_id: dict[str, dict] = {e["id"]: e for e in manifest.get("predictions", []) if "id" in e}

    def candidate_ids(raw: str) -> list[str]:
        cleaned = raw.strip().replace("–", "-").replace("—", "-")
        out = [f"P{cleaned.replace('-', '_')}"]
        if cleaned.isdigit():
            out.append(f"P{int(cleaned):02d}")
        return out

    for row_id, name in rows:
        matched = False
        for cand in candidate_ids(row_id):
            if cand in entries_by_id:
                matched = True
                break
        if not matched and row_id.isdigit():
            row_num = int(row_id)
            if any(_id_range_contains(eid, row_num) for eid in entries_by_id):
                matched = True
        if not matched:
            findings.append(
                Finding(
                    check="parity",
                    severity="warn",
                    entry_id=None,
                    message=(
                        f"LIVING_REFERENCE prediction row '{row_id}' "
                        f"({name!r}) has no matching entry in "
                        f"manuscript/predictions.yaml"
                    ),
                    details={
                        "row_id": row_id,
                        "name": name,
                        "source": "LIVING_REFERENCE.md",
                    },
                )
            )

    return findings


# ───────────────────────────────────────────────────────────────────────────
# Orchestration
# ───────────────────────────────────────────────────────────────────────────
ALL_CHECKS = {
    "schema": check_schema,
    "label": check_labels,
    "engine": check_engine,
    "bridge": check_bridge,
    "axioms": check_axioms,
    "calibration_role": check_calibration_role,
    "parity": check_readme_parity,
    "lr_parity": check_living_reference_parity,
}


def run(
    manifest_path: Path = MANIFEST_PATH,
    checks: list[str] | None = None,
) -> list[Finding]:
    manifest = load_manifest(manifest_path)
    checks = checks or list(ALL_CHECKS.keys())

    findings: list[Finding] = []
    for check_name in checks:
        if check_name not in ALL_CHECKS:
            raise ValueError(f"Unknown check: {check_name}")
        findings.extend(ALL_CHECKS[check_name](manifest))
    return findings


def format_text(findings: list[Finding], n_entries: int) -> str:
    if not findings:
        return f"[predictions] {n_entries} manifest entries; " "all structural checks pass."

    by_sev: dict[str, int] = {}
    for f in findings:
        by_sev[f.severity] = by_sev.get(f.severity, 0) + 1

    out = [f"[predictions] {n_entries} manifest entries; {len(findings)} findings."]
    for sev in ("critical", "warn", "info"):
        if sev in by_sev:
            out.append(f"  {sev.upper():<8} {by_sev[sev]}")
    out.append("")

    for sev in ("critical", "warn", "info"):
        sev_findings = [f for f in findings if f.severity == sev]
        if not sev_findings:
            continue
        out.append(f"─── {sev.upper()} ({len(sev_findings)}) " + "─" * 50)
        for f in sev_findings:
            prefix = f"[{f.check}]"
            entry = f" (P={f.entry_id})" if f.entry_id else ""
            out.append(f"  {prefix}{entry}  {f.message}")
        out.append("")

    return "\n".join(out)


def format_json(findings: list[Finding], n_entries: int) -> str:
    return json.dumps(
        {
            "manifest_entries": n_entries,
            "findings": [
                {
                    "check": f.check,
                    "severity": f.severity,
                    "entry_id": f.entry_id,
                    "message": f.message,
                    "details": f.details,
                }
                for f in findings
            ],
        },
        indent=2,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the AVE predictions manifest (manuscript/predictions.yaml).")
    parser.add_argument(
        "--manifest",
        type=Path,
        default=MANIFEST_PATH,
        help="Path to predictions.yaml (default: manuscript/predictions.yaml)",
    )
    parser.add_argument(
        "--check",
        choices=sorted(ALL_CHECKS.keys()),
        action="append",
        help="Run specific checks only (may be repeated). Default: all",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON",
    )
    parser.add_argument(
        "--warn-only",
        action="store_true",
        help="Exit 0 even if critical findings are present (warning mode)",
    )
    args = parser.parse_args(argv)

    try:
        manifest = load_manifest(args.manifest)
    except FileNotFoundError:
        print(
            f"[predictions] Manifest not found: {args.manifest}",
            file=sys.stderr,
        )
        return 2
    except yaml.YAMLError as e:
        print(f"[predictions] Manifest parse error: {e}", file=sys.stderr)
        return 2

    n_entries = len(manifest.get("predictions", []))

    try:
        findings = run(args.manifest, checks=args.check)
    except Exception as e:
        print(f"[predictions] Error during validation: {e}", file=sys.stderr)
        return 2

    if args.json:
        print(format_json(findings, n_entries))
    else:
        print(format_text(findings, n_entries))

    if args.warn_only:
        return 0
    has_critical = any(f.severity == "critical" for f in findings)
    return 1 if has_critical else 0


if __name__ == "__main__":
    sys.exit(main())

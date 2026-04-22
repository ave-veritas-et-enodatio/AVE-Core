#!/usr/bin/env python3
"""
Claim Graph Validator — verifies the structured claim graph in
manuscript/predictions.yaml against the manuscript and physics engine.

This is the Tier-2 rigor upgrade (see session handoff). Where the
defense_context_checker catches FRAMING anti-patterns via regex, this
validator catches STRUCTURAL inconsistencies:

  1. Manifest schema  — every entry has required fields; no duplicate IDs
  2. Label resolution — every derivation_label resolves to a real
                        \\label{} target in manuscript/**/*.tex (xr-hyper
                        cross-volume refs resolve via the backmatter)
  3. Engine agreement — every constants_py_symbol exists and its live
                        numeric value agrees with predicted_value to rtol=1e-5
  4. Public parity    — every row in the README master table maps to a
                        manifest entry (no undocumented public claims)

Exit codes:
  0 — clean (all structural checks pass)
  1 — validation failures found
  2 — script error (missing manifest, bad YAML, etc.)

Usage:
  python src/scripts/claim_graph_validator.py                 # full run
  python src/scripts/claim_graph_validator.py --json          # machine output
  python src/scripts/claim_graph_validator.py --warn-only     # exit 0 on failures
  python src/scripts/claim_graph_validator.py --check label   # one check

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

ALLOWED_TYPES = {
    "derived_prediction",
    "axiom_manifestation",
    "identity",
    "consistency_check",
    "engineering_limit",
}

REQUIRED_FIELDS = {"id", "name", "type", "derivation_label"}


# ───────────────────────────────────────────────────────────────────────────
# Findings
# ───────────────────────────────────────────────────────────────────────────
@dataclass
class Finding:
    check: str  # "schema" | "label" | "engine" | "parity"
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
        if "build/" in str(tex) or "/aux/" in str(tex):
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

        # Required fields
        missing = REQUIRED_FIELDS - entry.keys()
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

    return findings


def check_labels(manifest: dict, labels: set[str] | None = None) -> list[Finding]:
    """Every entry's derivation_label resolves to a \\label{} in the manuscript."""
    findings: list[Finding] = []
    if labels is None:
        labels = collect_manuscript_labels()

    for entry in manifest.get("predictions", []):
        eid = entry.get("id", "<missing-id>")
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
        return f"[claim-graph] {n_entries} manifest entries; " "all structural checks pass."

    by_sev: dict[str, int] = {}
    for f in findings:
        by_sev[f.severity] = by_sev.get(f.severity, 0) + 1

    out = [f"[claim-graph] {n_entries} manifest entries; {len(findings)} findings."]
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
    parser = argparse.ArgumentParser(description="Validate the AVE claim graph (manuscript/predictions.yaml).")
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
            f"[claim-graph] Manifest not found: {args.manifest}",
            file=sys.stderr,
        )
        return 2
    except yaml.YAMLError as e:
        print(f"[claim-graph] Manifest parse error: {e}", file=sys.stderr)
        return 2

    n_entries = len(manifest.get("predictions", []))

    try:
        findings = run(args.manifest, checks=args.check)
    except Exception as e:
        print(f"[claim-graph] Error during validation: {e}", file=sys.stderr)
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

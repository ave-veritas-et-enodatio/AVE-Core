#!/usr/bin/env python3
"""Drift-gate verifier for the AVE CODE-PROVENANCE INDEX.

Mirrors ``manuscript/ave-kb/tools/verify-kb-metadata.py`` (which gates the
*claim* registry) but for the *code* registry: one record per load-bearing
computed quantity in ``code_provenance.jsonl``.

This is a 6-seed PROTOTYPE, not an all-code-tracked guarantee. Records are
POPULATED by two skills (live-fire-derivation-provenance ->
provenance/solver/ci_gate/dead_inputs/magnitude; dimensional-provenance-check
-> dim_type) and MAINTAINED by this verifier.

Checks per record (read-only; never modifies any file):
  (a) impl-exists  : every ``*.py`` path named in ``impl`` exists on disk.
                     MISSING -> hard fail (drift-gate, exit 1).
  (b) symbol-present: every ``path.py:symbol`` token in ``impl`` greps to a
                     definition/occurrence of ``symbol`` in that file.
                     Not-found -> WARN (locals/dict-keys are legitimately
                     non-greppable; not a drift failure for the prototype).
  (c) ci-gate      : ``ci_gate`` is null -> UNGATED warning; else the named
                     test file exists and the test function is present
                     (drift WARN if the named test cannot be located).
  (d) dim-consistency: ``dim_type`` is present and is one of the known kinds.
  (e) canonical cross-check (ave-canonical-source): import the named values
                     ``from ave.core.constants import ...`` (and cosserat)
                     and echo them as live evidence the import path resolves.

Exit code:
  1  if any record has a MISSING impl path (drift-gate) or malformed record.
  0  otherwise. UNGATED / symbol-not-found / ci-not-located are WARNINGS,
     not failures, for the prototype.

Usage:
    python src/scripts/verify/verify_code_provenance.py
    PYTHONPATH=src python src/scripts/verify/verify_code_provenance.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# --- locate repo root + registry ------------------------------------------
# This file lives at <repo>/src/scripts/verify/verify_code_provenance.py
HERE = Path(__file__).resolve()
REPO_ROOT = HERE.parents[3]
REGISTRY = HERE.parent / "code_provenance.jsonl"
SRC = REPO_ROOT / "src"

# Make the local (this-checkout) ``ave`` importable so the canonical
# cross-check reads THIS tree, not a globally-installed copy.
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

KNOWN_DIM_TYPES = {"ratio", "mass", "length", "dimensionless", "energy", "frequency", "angle"}
KNOWN_PROVENANCE = {"solver-forward", "matched-closed-form", "empirical-input", "geometric-constant"}

# token forms inside the ``impl`` string
PY_PATH_RE = re.compile(r"[\w./-]+\.py")
PY_SYMBOL_RE = re.compile(r"([\w./-]+\.py):([A-Za-z_][A-Za-z0-9_]*)")


def _grep_symbol(path: Path, symbol: str) -> bool:
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    return re.search(rf"\b{re.escape(symbol)}\b", text) is not None


def _ci_test_present(ci_gate: str) -> tuple[bool, str]:
    """Return (located, detail). ci_gate form: 'path::Test::func' or 'path::func[param]'."""
    file_part = ci_gate.split("::", 1)[0]
    p = REPO_ROOT / file_part
    if not p.exists():
        return False, f"ci file missing: {file_part}"
    # last :: segment is the test function (strip pytest param suffix [..])
    func = ci_gate.split("::")[-1].split("[")[0]
    if _grep_symbol(p, func):
        return True, f"{file_part} :: {func}"
    return False, f"test func '{func}' not found in {file_part}"


def _canonical_cross_check() -> list[str]:
    """ave-canonical-source: import the literals the registry cites, echo them."""
    out: list[str] = []
    try:
        from ave.core.constants import (  # type: ignore
            BARYON_LADDER,
            M_N_MEV_TARGET,
            M_P_MEV_CODATA,
        )

        out.append(
            f"  m_p/m_e  BARYON_LADDER[5]['ratio'] = {BARYON_LADDER[5]['ratio']!r}"
        )
        out.append(
            f"  m_D/m_e  BARYON_LADDER[7]['ratio'] = {BARYON_LADDER[7]['ratio']!r}"
        )
        dm = M_N_MEV_TARGET - M_P_MEV_CODATA
        out.append(
            f"  m_n      M_N_MEV_TARGET={M_N_MEV_TARGET} - M_P_MEV_CODATA={M_P_MEV_CODATA} -> Dm={dm:.6f} MeV"
        )
    except Exception as exc:  # noqa: BLE001 - prototype: import issues warn, not fail
        out.append(f"  [WARN] constants import failed: {exc!r}")
    try:
        from ave.topological.cosserat import M_MU_MEV, M_TAU_MEV  # type: ignore

        out.append(f"  m_mu/m_e M_MU_MEV  = {M_MU_MEV:.4f}  (PDG 105.658, +1.24%)")
        out.append(f"  m_tau/m_e M_TAU_MEV = {M_TAU_MEV:.4f} (PDG 1776.86, -0.95%)")
    except Exception as exc:  # noqa: BLE001
        out.append(f"  [WARN] cosserat import failed: {exc!r}")
    return out


def main() -> int:
    if not REGISTRY.exists():
        print(f"[FAIL] registry not found: {REGISTRY}")
        return 1

    records: list[dict] = []
    malformed = 0
    for lineno, raw in enumerate(REGISTRY.read_text().splitlines(), start=1):
        if not raw.strip():
            continue
        try:
            records.append(json.loads(raw))
        except json.JSONDecodeError as exc:
            print(f"[FAIL] line {lineno}: malformed JSON: {exc}")
            malformed += 1

    print("=" * 72)
    print("AVE CODE-PROVENANCE INDEX  --  verify_code_provenance.py")
    print(f"registry: {REGISTRY.relative_to(REPO_ROOT)}")
    print(f"records : {len(records)}")
    print("=" * 72)

    n_missing = 0
    n_ungated = 0
    n_solver = 0
    n_symbol_warn = 0
    n_ci_warn = 0
    n_dim_bad = 0
    n_flags = 0

    for rec in records:
        q = rec.get("quantity", "<no-quantity>")
        impl = rec.get("impl", "")
        clm = rec.get("clm", [])
        prov = rec.get("provenance", "<none>")
        solver = bool(rec.get("solver", False))
        ci_gate = rec.get("ci_gate")
        dim = rec.get("dim_type")
        dead = rec.get("dead_inputs", []) or []
        flags = rec.get("flags", []) or []

        if solver:
            n_solver += 1
        n_flags += len(flags)

        print(f"\n[{q}]  provenance={prov}  solver={solver}  clm={','.join(clm) if clm else '-'}")

        # (a) impl-exists (drift-gate)
        paths = {m for m in PY_PATH_RE.findall(impl)}
        for rel in sorted(paths):
            p = REPO_ROOT / rel
            if p.exists():
                print(f"  [ok]   impl path exists: {rel}")
            else:
                print(f"  [FAIL] impl path MISSING: {rel}")
                n_missing += 1

        # (b) symbol-present (warn-only)
        for rel, sym in PY_SYMBOL_RE.findall(impl):
            p = REPO_ROOT / rel
            if not p.exists():
                continue  # already counted as MISSING above
            if _grep_symbol(p, sym):
                print(f"  [ok]   symbol present: {rel}:{sym}")
            else:
                print(f"  [WARN] symbol not greppable (local/dict-key?): {rel}:{sym}")
                n_symbol_warn += 1

        # (c) ci-gate
        if ci_gate is None:
            print(f"  [WARN] UNGATED: no CI gate for '{q}'")
            n_ungated += 1
        else:
            located, detail = _ci_test_present(ci_gate)
            if located:
                print(f"  [ok]   ci gate located: {detail}")
            else:
                print(f"  [WARN] ci gate NOT located: {detail}")
                n_ci_warn += 1

        # (d) dim-consistency
        if dim is None:
            print(f"  [FAIL] dim_type MISSING for '{q}'")
            n_dim_bad += 1
        elif dim not in KNOWN_DIM_TYPES:
            print(f"  [WARN] dim_type '{dim}' not in known set {sorted(KNOWN_DIM_TYPES)}")
            n_dim_bad += 1
        else:
            print(f"  [ok]   dim_type={dim}")

        if dead:
            print(f"  [note] dead_inputs: {', '.join(dead)}")
        for fl in flags:
            print(f"  [flag] {fl}")

    # (e) canonical cross-check
    print("\n" + "-" * 72)
    print("canonical cross-check (ave-canonical-source: import + echo):")
    for line in _canonical_cross_check():
        print(line)

    # summary
    print("\n" + "=" * 72)
    print("SUMMARY")
    print(
        f"  {len(records)} quantities | {n_solver} solver-backed | "
        f"{n_ungated} ungated | {n_flags} flags"
    )
    print(
        f"  warnings: symbol-not-greppable={n_symbol_warn}  ci-not-located={n_ci_warn}"
    )
    print(
        f"  drift-gate: impl-missing={n_missing}  dim-missing={n_dim_bad}  malformed-json={malformed}"
    )
    print("  NOTE: 6-seed PROTOTYPE -- NOT all-code-tracked. Grow per-check.")
    print("=" * 72)

    fail = n_missing > 0 or malformed > 0 or n_dim_bad > 0
    if fail:
        print("RESULT: FAIL (drift-gate tripped)")
        return 1
    print("RESULT: PASS (impl-exists + dim-consistency OK; warnings are advisory)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

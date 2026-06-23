"""Static import-resolution smoke gate for ``src/scripts/``.

Every ``from ave.core.<module> import NAME`` in a script under ``src/scripts/``
must name a symbol that is actually defined at module level in the target
``ave/core/<module>.py`` file.  This catches two failure modes that only ever
surface at integrator time (and which static type-checkers were not catching in
this tree):

  * a renamed / nonexistent constant — e.g. importing ``GRAVITATIONAL_CONSTANT``
    when ``constants.py`` defines the Newton constant as ``G``; and
  * a wrong-module import — e.g. importing ``_compute_i_scalar_dynamic`` from
    ``ave.core.constants`` when it is actually defined in
    ``ave.core._constants_compute``.

The check is purely AST-based: NO script is imported or executed (several
scripts run heavy work at module scope), so the gate is fast and side-effect
free.  It is the exact check that would have flagged all four stale imports
fixed on branch ``analysis/stale-import-sweep``.

Dependency-light by design: standard-library ``ast`` + ``pathlib`` only.
"""

from __future__ import annotations

import ast
from pathlib import Path

import pytest

# ``src/tests/`` -> ``src`` is parents[1]; the repo root is parents[2].
_SRC_DIR = Path(__file__).resolve().parents[1]
_SCRIPTS_DIR = _SRC_DIR / "scripts"
_AVE_CORE_DIR = _SRC_DIR / "ave" / "core"

# ``_archive`` holds frozen, intentionally-stale scripts — excluded from the walk.
_EXCLUDED_DIR_NAMES = {"_archive"}

_TARGET_PACKAGE_PREFIX = "ave.core."

# --- Known-broken allowlist (xfail, strict) ---------------------------------
# Imports that are *genuinely* broken today but are NOT this branch's to fix.
# Each entry is keyed by the gate's ``file:line:NAME`` label and carries the
# owning effort + the correct symbol so the trail is auditable.  TWO mechanisms
# together ensure an allowlist entry cannot silently outlive its bug:
#   1. ``strict=True`` xfail — if an allowlisted import is *still generated* as a
#      violation yet somehow resolves, the XPASS hard-fails the suite.
#   2. ``test_known_broken_allowlist_is_live`` (below) — if an owner lands their
#      fix, the import stops generating a violation at all (so mechanism 1 never
#      fires); the liveness guard then hard-fails because the now-dead allowlist
#      key no longer matches any live violation, forcing its removal.
# (Mechanism 1 alone is NOT sufficient for the import-fix case — a fixed import
# simply drops from parametrization with no XPASS; mechanism 2 closes that gap.)
#
# This is the KEEP-BOTH / flag-don't-fix posture: the gate is green for what
# this branch controls, the out-of-scope breakages stay VISIBLE (as xfail),
# and nothing is silently fixed or silently swallowed.
_KNOWN_BROKEN: dict[str, str] = {
    # (simulate_geodynamo_vca.py:12:GRAVITATIONAL_CONSTANT was here; merged PR #377
    #  fixed it to G, so the violation is no longer generated. Per the liveness
    #  guard below, the now-dead allowlist key was removed — the gate worked as
    #  designed: a fixed-upstream entry hard-fails until dropped.)
    # Surfaced by THIS gate (not in the D3 scope): k4_tlm.py defines
    # 'build_scattering_matrix', these two scripts import 'build_k4_scattering_matrix'.
    # Flagged for the k4_tlm owner; NOT fixed here per flag-don't-fix.
    "scripts/vol_3_macroscopic/animate_k4_tlm_lensing_ultra.py:18:build_k4_scattering_matrix": (
        "wrong symbol; ave.core.k4_tlm defines 'build_scattering_matrix' — owner: k4_tlm"
    ),
    "scripts/vol_3_macroscopic/k4_tlm_gravitational_lensing.py:34:build_k4_scattering_matrix": (
        "wrong symbol; ave.core.k4_tlm defines 'build_scattering_matrix' — owner: k4_tlm"
    ),
}


def _iter_script_files() -> list[Path]:
    """All ``*.py`` under ``src/scripts/`` except anything inside an excluded dir."""
    files: list[Path] = []
    for path in sorted(_SCRIPTS_DIR.rglob("*.py")):
        if _EXCLUDED_DIR_NAMES.intersection(part for part in path.relative_to(_SCRIPTS_DIR).parts):
            continue
        files.append(path)
    return files


def _module_to_file(module: str) -> Path | None:
    """Map a dotted ``ave.core.<sub>`` module to its source file, or ``None``."""
    if not module.startswith(_TARGET_PACKAGE_PREFIX):
        return None
    rel = module[len("ave.core.") :].replace(".", "/")
    candidate = _AVE_CORE_DIR / f"{rel}.py"
    if candidate.is_file():
        return candidate
    pkg_init = _AVE_CORE_DIR / rel / "__init__.py"
    if pkg_init.is_file():
        return pkg_init
    return None


def _module_level_names(tree: ast.Module) -> tuple[set[str], bool]:
    """Names bound at module scope, plus whether resolution must be skipped.

    The second element is ``True`` when the module uses a wildcard import or a
    module-level ``__getattr__``, either of which makes a name statically
    unprovable-absent; such targets are treated as resolving everything.
    """
    names: set[str] = set()
    opaque = False
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.add(node.name)
            if isinstance(node, ast.FunctionDef) and node.name == "__getattr__":
                opaque = True
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                names.update(_assign_target_names(target))
        elif isinstance(node, ast.AnnAssign):
            names.update(_assign_target_names(node.target))
        elif isinstance(node, ast.Import):
            for alias in node.names:
                names.add(alias.asname or alias.name.split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                if alias.name == "*":
                    opaque = True
                else:
                    names.add(alias.asname or alias.name)
    return names, opaque


def _assign_target_names(target: ast.expr) -> set[str]:
    names: set[str] = set()
    if isinstance(target, ast.Name):
        names.add(target.id)
    elif isinstance(target, (ast.Tuple, ast.List)):
        for elt in target.elts:
            names.update(_assign_target_names(elt))
    return names


def _collect_violations(script: Path) -> list[tuple[str, str]]:
    """Return ``(label, message)`` for each unresolved ``ave.core`` import.

    A ``label`` is a stable, human-readable parametrization id; ``message`` is
    the assertion text naming ``file:line:NAME`` and the target module.
    """
    rel = script.relative_to(_SRC_DIR).as_posix()
    try:
        tree = ast.parse(script.read_text(encoding="utf-8"), filename=str(script))
    except (SyntaxError, UnicodeDecodeError) as exc:  # pragma: no cover - defensive
        return [(f"{rel}::PARSE", f"{rel}: could not parse ({exc})")]

    # Cache target-module name sets across the imports within a single script.
    cache: dict[Path, tuple[set[str], bool]] = {}
    violations: list[tuple[str, str]] = []

    for node in ast.walk(tree):
        if not isinstance(node, ast.ImportFrom) or node.level:
            continue
        module = node.module or ""
        if not module.startswith(_TARGET_PACKAGE_PREFIX):
            continue
        target_file = _module_to_file(module)
        if target_file is None:
            # Target module file does not exist at all -> every name is broken.
            for alias in node.names:
                if alias.name == "*":
                    continue
                violations.append(
                    (
                        f"{rel}:{node.lineno}:{alias.name}",
                        f"{rel}:{node.lineno}: 'from {module} import {alias.name}' -> "
                        f"target module '{module}' has no source file under src/ave/core/.",
                    )
                )
            continue
        if target_file not in cache:
            target_tree = ast.parse(target_file.read_text(encoding="utf-8"), filename=str(target_file))
            cache[target_file] = _module_level_names(target_tree)
        defined, opaque = cache[target_file]
        if opaque:
            continue
        for alias in node.names:
            if alias.name == "*":
                continue
            if alias.name not in defined:
                violations.append(
                    (
                        f"{rel}:{node.lineno}:{alias.name}",
                        f"{rel}:{node.lineno}: 'from {module} import {alias.name}' -> "
                        f"name '{alias.name}' is not defined at module level in "
                        f"{target_file.relative_to(_SRC_DIR).as_posix()}.",
                    )
                )
    return violations


def _build_cases() -> list[tuple[str, str]]:
    cases: list[tuple[str, str]] = []
    for script in _iter_script_files():
        cases.extend(_collect_violations(script))
    return cases


_SCRIPT_FILES = _iter_script_files()
_VIOLATIONS = _build_cases()


def test_scripts_present() -> None:
    """Guard against a broken walk silently testing nothing."""
    assert _SCRIPTS_DIR.is_dir(), f"missing scripts dir: {_SCRIPTS_DIR}"
    assert _SCRIPT_FILES, "found no scripts under src/scripts/ — walk is misconfigured"


def test_known_broken_allowlist_is_live() -> None:
    """Every allowlist entry must still correspond to a live violation.

    Liveness guard (mechanism 2 above): a strict-xfail entry stops being
    exercised the moment its underlying import is fixed upstream — the violation
    is simply no longer generated, so no XPASS fires and the dead entry would
    otherwise linger untested. This asserts every ``_KNOWN_BROKEN`` key still
    matches a currently-generated violation; when an owner lands their fix
    (e.g. the k4_tlm build_scattering_matrix symbol), the corresponding key
    goes stale and this test hard-fails, forcing its removal. That is what makes
    'the allowlist cannot silently outlive the bug' actually true. (Demonstrated:
    merged PR #377 fixed geodynamo, so its key was removed here.)
    """
    live_labels = {label for label, _ in _VIOLATIONS}
    stale = sorted(key for key in _KNOWN_BROKEN if key not in live_labels)
    assert not stale, (
        "Allowlisted import(s) no longer generate a violation — their bug was "
        f"fixed upstream; remove the now-stale _KNOWN_BROKEN entr{'y' if len(stale) == 1 else 'ies'}: "
        + ", ".join(stale)
    )


def _parametrize_cases() -> list:
    """Build pytest params, marking allowlisted breakages as strict xfail."""
    if not _VIOLATIONS:
        return [pytest.param("__no_violations__", "", id="__no_violations__")]
    params = []
    for label, message in _VIOLATIONS:
        if label in _KNOWN_BROKEN:
            marks = [pytest.mark.xfail(reason=_KNOWN_BROKEN[label], strict=True)]
        else:
            marks = []
        params.append(pytest.param(label, message, id=label, marks=marks))
    return params


@pytest.mark.parametrize("label,message", _parametrize_cases())
def test_ave_core_imports_resolve(label: str, message: str) -> None:
    """Each ``from ave.core.<module> import NAME`` must name a defined symbol."""
    if label == "__no_violations__":
        return
    pytest.fail(message)

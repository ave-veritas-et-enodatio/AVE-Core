"""Static import-resolution smoke gate for ``src/scripts/``.

TWO independent gates live here.

GATE 1 — ``ave.core`` symbol resolution
---------------------------------------
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

GATE 2 — script-tree (package-style) import resolution
------------------------------------------------------
Gate 1 scopes to the ``from ave.core.<mod> import NAME`` shape only, so it was
structurally blind to the failure the vol_6 provenance hole exposed: 13
``src/scripts/vol_6_periodic_table/animations/animate_*.py`` drivers imported
``from periodic_table.simulations.simulate_element import …`` while
``importlib.util.find_spec('periodic_table')`` returned ``None`` — every one of
them died at line 1 (open item ``vol6-figure-provenance-hole``, discharged
2026-08-23 under Grant's option (b) ruling).

Gate 2 covers the two package-style shapes a ``src/scripts`` driver can use to
reach its own tree, and checks BOTH halves of what makes such an import work:

  A. *Symbol resolution.*  ``from X.Y import NAME`` where ``X`` names a sibling
     module/package beside the importing script — or the documented
     ``periodic_table`` alias for ``src/scripts/vol_6_periodic_table/``
     (``src/scripts/AGENTS.md`` §"The ``periodic_table`` import namespace") —
     must resolve to a real source file that defines ``NAME`` at module level.
     Third-party roots are never in scope: the shape only triggers when the
     root actually exists as a file/dir next to the script.

  B. *Alias reachability.*  Symbol resolution alone would NOT have caught the
     vol_6 bug — the alias target file existed and did define the symbol; what
     was missing was the alias REGISTRATION.  ``periodic_table`` is not a real
     package anywhere on disk, so any script importing from it must register it
     at module level (``sys.modules["periodic_table"] = …``, the namespace-
     package bootstrap proven at ``regenerate_all_figures.py:42-46``) or import
     a sibling module that does.  A script that does neither cannot run, and
     Gate 2B fails it.  Sibling-module imports need no such rule: running
     ``python path/to/driver.py`` puts the driver's own directory on
     ``sys.path[0]`` by construction.

Both gates are purely AST-based: NO script is imported or executed (several
scripts run heavy work at module scope), so they are fast and side-effect free.
Gate 1 is the exact check that would have flagged all four stale imports fixed
on branch ``analysis/stale-import-sweep``; Gate 2B is the exact check that
would have flagged all 13 vol_6 animation drivers.

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

# --- Gate 2 constants -------------------------------------------------------
# The legacy import alias documented at src/scripts/AGENTS.md §"The
# periodic_table import namespace": the directory on disk is
# ``vol_6_periodic_table``, the import name is ``periodic_table``.
_PT_ALIAS = "periodic_table"
_PT_ALIAS_DIR = _SCRIPTS_DIR / "vol_6_periodic_table"

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


# ============================================================================
# GATE 2 — script-tree (package-style) import resolution.  See module docstring.
# ============================================================================

# Known-broken allowlist for Gate 2, same KEEP-BOTH / flag-don't-fix posture and
# same two mechanisms (strict xfail + liveness guard) as ``_KNOWN_BROKEN`` above.
# These five sites are the SAME class of breakage as the 13 vol_6 animation
# drivers repaired on branch ``cleanup/2026-08-23-vol6-imports`` — they import
# through the ``periodic_table`` alias without registering it — but they are
# outside that branch's scope (the open item scoped to the animation drivers
# only), so they stay VISIBLE here rather than being silently swept in.
_SCRIPT_TREE_KNOWN_BROKEN: dict[str, str] = {
    # Gate 2B: alias never registered -> ModuleNotFoundError at import time.
    "scripts/vol_2_subatomic/analyze_c12_emitter.py::alias-unregistered": (
        "same class as the vol_6 animation drivers; out of scope for the "
        "vol6-figure-provenance-hole discharge — owner: vol_2 driver upkeep"
    ),
    "scripts/vol_4_engineering/calculate_conductivity.py::alias-unregistered": (
        "same class as the vol_6 animation drivers; out of scope for the "
        "vol6-figure-provenance-hole discharge — owner: vol_4 driver upkeep"
    ),
    "scripts/vol_4_engineering/visualize_magnetism.py::alias-unregistered": (
        "same class as the vol_6 animation drivers; out of scope for the "
        "vol6-figure-provenance-hole discharge — owner: vol_4 driver upkeep"
    ),
    "scripts/vol_6_periodic_table/simulations/generate_3d_meshes.py::alias-unregistered": (
        "same class as the vol_6 animation drivers; out of scope for the "
        "vol6-figure-provenance-hole discharge — owner: vol_6 simulations upkeep"
    ),
    "scripts/vol_6_periodic_table/simulations/solve_fluorine.py::alias-unregistered": (
        "same class as the vol_6 animation drivers; out of scope for the "
        "vol6-figure-provenance-hole discharge — owner: vol_6 simulations upkeep"
    ),
    # Gate 2A note (2026-08-23): the SECOND-ORDER IP-partition casualty this dict
    # used to carry — simulate_dt_fusion.py:5 importing 'generate_fusion_netlist',
    # a symbol the surviving spice_exporter.py stub does not define — was ruled
    # option (c) and RETIRED to src/scripts/_archive/vol_6_periodic_table/
    # (docket-entries/2026-08-23-dt-fusion-ruling.md).  _archive is excluded from
    # this walk, so both of its entries left this dict under the stale-entry
    # liveness guard.
}


def _resolve_under(base: Path, parts: list[str]) -> Path | None:
    """Resolve dotted ``parts`` to a source file under ``base`` (module or pkg init)."""
    if not parts:
        init = base / "__init__.py"
        return init if init.is_file() else None
    module_file = base.joinpath(*parts).with_suffix(".py")
    if module_file.is_file():
        return module_file
    pkg_init = base.joinpath(*parts) / "__init__.py"
    return pkg_init if pkg_init.is_file() else None


def _registers_pt_alias(tree: ast.Module) -> bool:
    """True if the module assigns ``sys.modules["periodic_table"] = …`` anywhere."""
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if (
                isinstance(target, ast.Subscript)
                and isinstance(target.value, ast.Attribute)
                and target.value.attr == "modules"
                and isinstance(target.slice, ast.Constant)
                and target.slice.value == _PT_ALIAS
            ):
                return True
    return False


def _parse(path: Path) -> ast.Module | None:
    try:
        return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (SyntaxError, UnicodeDecodeError):  # pragma: no cover - defensive
        return None


def _script_tree_scope(script: Path, tree: ast.Module) -> list[tuple[ast.ImportFrom, Path, list[str], str]]:
    """In-scope ``ImportFrom`` nodes for *script*, as ``(node, base, rest, root)``.

    Shape triggers ONLY when the import root is the ``periodic_table`` alias or
    actually exists as a sibling module/package beside the script — so an
    uninstalled third-party root (``skimage``, ``imageio``, …) is never in scope.
    """
    directory = script.parent
    scope: list[tuple[ast.ImportFrom, Path, list[str], str]] = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.ImportFrom) or node.level or not node.module:
            continue
        parts = node.module.split(".")
        root = parts[0]
        if root == _PT_ALIAS:
            scope.append((node, _PT_ALIAS_DIR, parts[1:], root))
        elif (directory / f"{root}.py").is_file() or (directory / root).is_dir():
            scope.append((node, directory, parts, root))
    return scope


def _collect_script_tree_violations(script: Path, tree: ast.Module) -> list[tuple[str, str]]:
    """Gate-2 ``(label, message)`` pairs for one script."""
    rel = script.relative_to(_SRC_DIR).as_posix()
    directory = script.parent
    scope = _script_tree_scope(script, tree)
    violations: list[tuple[str, str]] = []
    cache: dict[Path, tuple[set[str], bool]] = {}

    # --- 2A: symbol resolution ---------------------------------------------
    for node, base, rest, _root in scope:
        target = _resolve_under(base, rest)
        if target is None:
            for alias in node.names:
                if alias.name == "*":
                    continue
                violations.append(
                    (
                        f"{rel}:{node.lineno}:{alias.name}",
                        f"{rel}:{node.lineno}: 'from {node.module} import {alias.name}' -> "
                        f"target module '{node.module}' has no source file under "
                        f"{base.relative_to(_SRC_DIR).as_posix()}/.",
                    )
                )
            continue
        if target not in cache:
            target_tree = _parse(target)
            cache[target] = (set(), True) if target_tree is None else _module_level_names(target_tree)
        defined, opaque = cache[target]
        if opaque:
            continue
        for alias in node.names:
            if alias.name == "*" or alias.name in defined:
                continue
            violations.append(
                (
                    f"{rel}:{node.lineno}:{alias.name}",
                    f"{rel}:{node.lineno}: 'from {node.module} import {alias.name}' -> "
                    f"name '{alias.name}' is not defined at module level in "
                    f"{target.relative_to(_SRC_DIR).as_posix()}.",
                )
            )

    # --- 2B: alias reachability --------------------------------------------
    if any(root == _PT_ALIAS for _n, _b, _r, root in scope) and not _registers_pt_alias(tree):
        bootstrapped_by = []
        for _node, base, _rest, root in scope:
            if root == _PT_ALIAS or base != directory:
                continue
            sibling = directory / f"{_node.module.split('.')[0]}.py"
            sibling_tree = _parse(sibling) if sibling.is_file() else None
            if sibling_tree is not None and _registers_pt_alias(sibling_tree):
                bootstrapped_by.append(sibling.name)
        if not bootstrapped_by:
            violations.append(
                (
                    f"{rel}::alias-unregistered",
                    f"{rel}: imports from the '{_PT_ALIAS}' alias but neither registers "
                    f"sys.modules['{_PT_ALIAS}'] itself nor imports a sibling module that does — "
                    f"'{_PT_ALIAS}' is not a real package on disk, so the import raises "
                    f"ModuleNotFoundError at run time. Bootstrap pattern: "
                    f"scripts/vol_6_periodic_table/simulations/regenerate_all_figures.py:42-46 "
                    f"(or import the shared animations/_pt_bootstrap.py).",
                )
            )
    return violations


def _build_script_tree_cases() -> tuple[list[tuple[str, str]], int, int]:
    """Return ``(violations, in_scope_site_count, animations_site_count)``."""
    cases: list[tuple[str, str]] = []
    sites = 0
    anim_sites = 0
    anim_dir = _PT_ALIAS_DIR / "animations"
    for script in _SCRIPT_FILES:
        tree = _parse(script)
        if tree is None:
            continue
        scope = _script_tree_scope(script, tree)
        sites += len(scope)
        if script.parent == anim_dir:
            anim_sites += len(scope)
        cases.extend(_collect_script_tree_violations(script, tree))
    return cases, sites, anim_sites


_TREE_VIOLATIONS, _TREE_SITES, _TREE_ANIM_SITES = _build_script_tree_cases()


def test_script_tree_gate_is_not_vacuous() -> None:
    """The Gate-2 walk must actually be looking at something.

    Anti-tautology guard: a refactor that renames the alias, moves the vol_6
    tree, or breaks the sibling-detection shape would otherwise silently reduce
    Gate 2 to a no-op that passes forever. The animations directory is named
    explicitly because it is the directory the gate was minted for.
    """
    assert _PT_ALIAS_DIR.is_dir(), f"vol_6 alias target dir is missing: {_PT_ALIAS_DIR}"
    assert _TREE_SITES > 0, "Gate 2 found no in-scope package-style imports under src/scripts/ — walk is misconfigured"
    assert _TREE_ANIM_SITES >= 13, (
        "Gate 2 sees only "
        f"{_TREE_ANIM_SITES} in-scope import site(s) in vol_6_periodic_table/animations/, "
        "but the 13 repaired animation drivers each carry one. The shape the gate keys on has drifted."
    )


def test_script_tree_allowlist_is_live() -> None:
    """Every Gate-2 allowlist entry must still correspond to a live violation."""
    live_labels = {label for label, _ in _TREE_VIOLATIONS}
    stale = sorted(key for key in _SCRIPT_TREE_KNOWN_BROKEN if key not in live_labels)
    assert not stale, (
        "Allowlisted script-tree import(s) no longer generate a violation — their bug was "
        f"fixed upstream; remove the now-stale entr{'y' if len(stale) == 1 else 'ies'}: " + ", ".join(stale)
    )


def _parametrize_script_tree_cases() -> list:
    if not _TREE_VIOLATIONS:
        return [pytest.param("__no_violations__", "", id="__no_violations__")]
    params = []
    for label, message in _TREE_VIOLATIONS:
        marks = (
            [pytest.mark.xfail(reason=_SCRIPT_TREE_KNOWN_BROKEN[label], strict=True)]
            if label in _SCRIPT_TREE_KNOWN_BROKEN
            else []
        )
        params.append(pytest.param(label, message, id=label, marks=marks))
    return params


@pytest.mark.parametrize("label,message", _parametrize_script_tree_cases())
def test_script_tree_imports_resolve(label: str, message: str) -> None:
    """Sibling-module and ``periodic_table``-alias imports must resolve AND be reachable."""
    if label == "__no_violations__":
        return
    pytest.fail(message)

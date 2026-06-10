"""
Structural α-freedom CI gate for the Crystal-Graft v3 engine chain
==================================================================

Panel measurement-fix #5 (Grant 2026-06-09): α-freedom must be ENFORCED
STRUCTURALLY at the engine-module level, NOT merely asserted per-driver. A false
Class-D chord (α leaking in through a constants import) is strictly worse than an
honest C — so this gate fails the build if ANY module in the v3 engine chain
imports a symbol from `ave.core.constants` whose definition transitively depends
on ALPHA.

Method (AST, no execution):
  1. Parse `constants.py`; mark a module-level name "α-tainted" if its assignment
     RHS references `ALPHA` (or `alpha`, the CODATA value) OR any already-tainted
     name. Iterate to a fixed point (transitive closure).
  2. Parse each engine module; collect every name imported via
     `from ave.core.constants import ...`.
  3. Assert the intersection is empty.

This catches e.g. R_I=√(2α), V_YIELD=√α·V_SNAP, P_C=8πα (α-tainted) while allowing
R_II=√3/2, R_III=1, NU_VAC=2/7, PHI, RR_GOLDEN_TORUS (α-free geometry).
"""

import ast
from pathlib import Path

import pytest

SRC = Path(__file__).resolve().parents[1]
CONSTANTS = SRC / "ave" / "core" / "constants.py"
ENGINE_CHAIN = [
    SRC / "ave" / "core" / "crystal_graft_v3.py",
    SRC / "ave" / "core" / "crystal_graft_v2.py",
    SRC / "ave" / "core" / "crystal_engine.py",
]
ALPHA_ROOTS = {"ALPHA", "alpha"}


def _names_in(node):
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


def _alpha_tainted_symbols():
    """Transitive closure of constants whose definition references ALPHA."""
    tree = ast.parse(CONSTANTS.read_text())
    rhs = {}  # name -> set of Names referenced on its RHS
    for stmt in tree.body:
        targets = []
        if isinstance(stmt, ast.Assign):
            targets = [t.id for t in stmt.targets if isinstance(t, ast.Name)]
            val = stmt.value
        elif isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
            targets = [stmt.target.id]
            val = stmt.value
        else:
            continue
        if val is None:
            continue
        refs = _names_in(val)
        for t in targets:
            rhs[t] = refs
    tainted = set(ALPHA_ROOTS)
    changed = True
    while changed:
        changed = False
        for name, refs in rhs.items():
            if name not in tainted and (refs & tainted):
                tainted.add(name)
                changed = True
    return tainted


def _constants_imports(module_path):
    tree = ast.parse(module_path.read_text())
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module == "ave.core.constants":
            for a in node.names:
                names.add(a.name)
    return names


def test_alpha_tainted_set_is_sane():
    """Sanity: the AST taint analysis flags the known α-bearing constants and
    clears the known α-free ones (so a green gate below is meaningful)."""
    tainted = _alpha_tainted_symbols()
    for known_alpha in ("R_I", "V_YIELD", "P_C", "ALPHA_S"):
        assert known_alpha in tainted, f"{known_alpha} should be α-tainted"
    for known_free in ("R_II", "R_III", "NU_VAC", "PHI", "RR_GOLDEN_TORUS"):
        assert known_free not in tainted, f"{known_free} should be α-free"


@pytest.mark.parametrize("module_path", ENGINE_CHAIN, ids=lambda p: p.name)
def test_engine_module_imports_no_alpha(module_path):
    """The v3 engine chain imports NO α-bearing symbol from constants.py."""
    tainted = _alpha_tainted_symbols()
    imported = _constants_imports(module_path)
    leaked = imported & tainted
    assert not leaked, (
        f"{module_path.name} imports α-bearing constant(s) {sorted(leaked)} — "
        f"α-freedom violated (a false-chord vector). Use the α-free geometry "
        f"constants or define the value locally."
    )

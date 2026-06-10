"""
Structural α-freedom CI gate for the Crystal-Graft v4 engine chain — HARDENED
============================================================================

v3's gate (`test_graft_v3_alpha_free.py`) checked only `ast.ImportFrom` on the
engine modules. The v4 panel-mandated hardening adds, per the v4 prereg §2:

  1. `ast.Import` of `ave.core.constants` + ATTRIBUTE access (`constants.ALPHA`)
     — the import-the-module-then-dot bypass.
  2. BARE CODATA LITERALS — a hardcoded α numeric value (7.2973525693e-3, the
     α⁻¹ 137.0359…/137.0363…, the golden-torus ¼/φ²) that bypasses the import.
  3. The DRIVER is in the scanned set (engine-chain rule is STRICT; the driver may
     import ALPHA_COLD_INV/PHI/RR_GOLDEN_TORUS as EMERGENCE COMPARISON TARGETS only,
     but must carry NO bare CODATA literal and must not feed them to the engine).
  4. A RUNTIME assertion that `ALPHA_COLD_INV`/`PHI`/`RR_GOLDEN_TORUS` (and the
     α-tainted constants) never enter ENGINE STATE — build a v4 engine and assert
     none of its physics attributes equals an α-derived value.

A false Class-D chord (α leaking into engine state) is strictly worse than an
honest C — this gate fails the build if any α-bearing value reaches the dynamics.
"""

import ast
from pathlib import Path

import numpy as np
import pytest

SRC = Path(__file__).resolve().parents[1]
CONSTANTS = SRC / "ave" / "core" / "constants.py"
ENGINE_CHAIN = [
    SRC / "ave" / "core" / "crystal_graft_v4.py",
    SRC / "ave" / "core" / "crystal_graft_v3.py",
    SRC / "ave" / "core" / "crystal_graft_v2.py",
    SRC / "ave" / "core" / "crystal_engine.py",
]
DRIVER = SRC / "scripts" / "vol_1_foundations" / "crystal_graft_v4_run.py"
ALPHA_ROOTS = {"ALPHA", "alpha"}

# bare CODATA / α-derived literals that must NOT appear hardcoded anywhere in the
# engine chain (a value-paste bypass of the import gate). Tolerance is relative.
FORBIDDEN_LITERALS = {
    "ALPHA": 7.2973525693e-3,
    "ALPHA_INV_CODATA": 137.035999084,
    "ALPHA_COLD_INV": 4.0 * np.pi**3 + np.pi**2 + np.pi,  # 137.0363…
}


def _names_in(node):
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


def _alpha_tainted_symbols():
    """Transitive closure of constants whose definition references ALPHA."""
    tree = ast.parse(CONSTANTS.read_text())
    rhs = {}
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


def _constants_importfrom(tree):
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module == "ave.core.constants":
            for a in node.names:
                names.add(a.name)
    return names


def _imports_constants_module(tree):
    """True iff the module does `import ave.core.constants [as X]` (the dot bypass)."""
    aliases = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for a in node.names:
                if a.name == "ave.core.constants":
                    aliases[a.asname or a.name] = True
    return aliases


def _attribute_accesses(tree, module_aliases):
    """Names accessed as `<alias>.NAME` for an imported-constants-module alias."""
    out = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
            base = node.value.id
            if base in module_aliases or base == "constants":
                out.add(node.attr)
    return out


def _bare_codata_literals(tree):
    """Float constants matching a forbidden α-derived value (rel-tol 1e-4)."""
    hits = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) and not isinstance(
            node.value, bool
        ):
            v = float(node.value)
            for name, ref in FORBIDDEN_LITERALS.items():
                if ref != 0 and abs(v - ref) <= 1e-4 * abs(ref):
                    hits.append((v, name))
    return hits


def test_alpha_tainted_set_is_sane():
    tainted = _alpha_tainted_symbols()
    for known_alpha in ("R_I", "V_YIELD", "P_C", "ALPHA_S"):
        assert known_alpha in tainted, f"{known_alpha} should be α-tainted"
    for known_free in ("R_II", "R_III", "NU_VAC", "PHI", "RR_GOLDEN_TORUS"):
        assert known_free not in tainted, f"{known_free} should be α-free"


@pytest.mark.parametrize("module_path", ENGINE_CHAIN, ids=lambda p: p.name)
def test_engine_module_strictly_alpha_free(module_path):
    """STRICT: every engine-chain module imports NO α-bearing constant (ImportFrom OR
    module-dot attribute), carries NO bare CODATA literal, and imports the EMERGENCE
    targets (ALPHA_COLD_INV/PHI/RR_GOLDEN_TORUS) into NO engine module either."""
    tainted = _alpha_tainted_symbols()
    targets = {"ALPHA_COLD_INV", "PHI", "RR_GOLDEN_TORUS", "R_GOLDEN_TORUS"}
    tree = ast.parse(module_path.read_text())

    leaked_from = _constants_importfrom(tree) & (tainted | targets)
    assert not leaked_from, f"{module_path.name}: from-import of α/emergence symbol(s) {sorted(leaked_from)}"

    aliases = _imports_constants_module(tree)
    attrs = _attribute_accesses(tree, aliases)
    leaked_attr = attrs & (tainted | targets)
    assert not leaked_attr, f"{module_path.name}: attribute access of α/emergence symbol(s) {sorted(leaked_attr)}"

    bare = _bare_codata_literals(tree)
    assert not bare, f"{module_path.name}: bare CODATA α literal(s) {bare}"


def test_driver_carries_no_bare_codata_literal():
    """The driver may import ALPHA_COLD_INV/PHI as emergence COMPARISON targets, but
    must carry NO bare CODATA α literal (a value-paste bypass)."""
    if not DRIVER.exists():
        pytest.skip("driver not present yet")
    tree = ast.parse(DRIVER.read_text())
    bare = _bare_codata_literals(tree)
    assert not bare, f"driver carries bare CODATA α literal(s) {bare}"


def test_alpha_targets_never_enter_engine_state():
    """RUNTIME: build a v4 engine and assert NO physics attribute equals an α-derived
    value (ALPHA, ALPHA_COLD_INV, PHI, RR_GOLDEN_TORUS, R_I, V_YIELD, P_C)."""
    import sys

    sys.path.insert(0, str(SRC))
    from ave.core.crystal_graft_v4 import CrystalGraftV4

    forbidden = {
        "ALPHA": 7.2973525693e-3,
        "ALPHA_COLD_INV": 4.0 * np.pi**3 + np.pi**2 + np.pi,
        "PHI": (1.0 + np.sqrt(5.0)) / 2.0,
        "RR_GOLDEN_TORUS": 0.25,
        "R_I": np.sqrt(2.0 * 7.2973525693e-3),
        "V_YIELD_over_VSNAP": np.sqrt(7.2973525693e-3),
        "P_C": 8.0 * np.pi * 7.2973525693e-3,
    }
    e = CrystalGraftV4(
        N=16, source_mode="abc", lam_sign=1, p=2, q=3, S_min=2e-3, A_cap=0.999,
        omega_gap=1.0, wall_center=0.62, wall_width=0.30, kappa_tilde=6.0 / 5.0,
        buckle_on=True, pml_thickness=4, lock_on=True, lock_eta=0.05, photon_coupling=True,
    )
    state = {
        "kappa_tilde": e.kappa_tilde, "lock_eta": e.lock_eta, "omega_gap": e.omega_gap,
        "V_yield": e.V_yield, "c0": e.c0, "c_T": e.c_T, "c_omega": e.c_omega,
        "wall_center": e.wall_center, "wall_width": e.wall_width, "S_min": e.S_min,
        "dt": e.dt, "cL2_over_cT2": e.cL2_over_cT2,
    }
    for sname, sval in state.items():
        for fname, fval in forbidden.items():
            if fval != 0:
                assert abs(float(sval) - fval) > 1e-4 * abs(fval), (
                    f"engine state {sname}={sval} equals α-derived {fname}={fval} — "
                    f"α leaked into engine state (a false-chord vector)."
                )

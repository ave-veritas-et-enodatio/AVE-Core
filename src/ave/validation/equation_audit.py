"""(d) hardened equation-audit — live import-closure scan + forbidden-constant guard.

ENGINE-HARDENING ARC item 2(d). Generalizes the #482-era equation-audit machinery
(lifted from `src/scripts/vol_2_subatomic/em_readout_vsector_transducer.py::
equation_audit`) into a reusable driver-agnostic guard. It answers: "does a
forbidden quantity (e.g. a calibrated constant like ALPHA / Q_TANK) enter the LIVE
import closure of this solve path, and does the solve RHS route only ALLOWED
arguments?"

The three hardening lessons the em_readout code learned, all preserved here:
  1. LIVE import-closure (not a hardcoded module list): exercise the solve path,
     then snapshot every `ave.*` module in sys.modules — this catches transitive
     imports (cosserat_field_3d imports ALPHA) a hardcoded subset misses.
  2. COMMENT/DOCSTRING STRIP before grep: the ledger + comments DESCRIBE the
     forbidden patterns, so a naive grep false-fires on the description (the
     grep-completeness trap). We scan executable code only.
  3. EXACT-MATCH allowlists (not prefix regex): a prefix regex passed rigged names
     (`source_from_Qlink`, `srcQ`). Anchor to the full token.

SCOPE HONESTY (the em_readout lesson, preserved). An α-carrier appearing in the
IMPORT CLOSURE is NOT the same as α entering the RESULT. The load-bearing guarantee
is the runtime-independence check (module (c)); this audit reports the closure
α-leak honestly but does not, by itself, claim the result is α-free. The two guards
compose: closure-scan (this) + runtime-independence (c).

α-CLEAN: this module NAMES forbidden constants as strings to scan for; it never
imports their values.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

# The default forbidden-constant set (the α-family calibration carriers). Matches
# the em_readout _FORBIDDEN_ALPHA guard. Callers may extend per driver.
DEFAULT_FORBIDDEN_CONSTANTS: tuple[str, ...] = (
    "ALPHA",
    "ALPHA_COLD_INV",
    "Q_TANK",
    "V_SNAP",
)


@dataclass(frozen=True)
class EquationAuditResult:
    """Outcome of a hardened equation audit over a solve path's import closure."""

    scanned_modules: tuple[str, ...]
    forbidden_in_closure: tuple[str, ...]  # "CONST@module.py" hits anywhere in closure
    forbidden_in_driver: tuple[str, ...]  # hits in the DRIVER module itself
    driver_clean: bool  # driver imports/uses no forbidden constant
    unexpected_solve_args: tuple[str, ...]  # solve-call args not in the allowlist
    solve_args_ok: bool
    detail: str = ""

    @property
    def passed(self) -> bool:
        """The audit passes iff the DRIVER routes no forbidden constant AND every
        solve-call argument is allowlisted. (Closure α-leak is REPORTED, not fatal
        by itself — see the module scope-honesty note; pair with runtime-independence.)"""
        return bool(self.driver_clean and self.solve_args_ok)

    def as_dict(self) -> dict:
        return {
            "test": "equation_audit_hardened",
            "n_scanned_modules": len(self.scanned_modules),
            "scanned_modules": list(self.scanned_modules),
            "forbidden_in_closure": list(self.forbidden_in_closure),
            "forbidden_in_driver": list(self.forbidden_in_driver),
            "driver_clean": self.driver_clean,
            "unexpected_solve_args": list(self.unexpected_solve_args),
            "solve_args_ok": self.solve_args_ok,
            "passed": self.passed,
        }


def _strip_code(text: str) -> str:
    """Return executable code only: drop trailing comments + triple-quoted blocks
    (the grep-completeness trap — comments DESCRIBE the forbidden patterns)."""
    lines = [ln.split("#", 1)[0] for ln in text.splitlines()]
    stripped = "\n".join(lines)
    return re.sub(r'(?:"""(?:.|\n)*?""")|(?:\'\'\'(?:.|\n)*?\'\'\')', "", stripped)


def import_closure_modules(exercise: Callable[[], object] | None = None) -> list[Path]:
    """The LIVE import closure: optionally exercise a path, then every `ave.*`
    module file currently in sys.modules. Not a hardcoded list — catches transitive
    imports the hardcoded subset misses."""
    if exercise is not None:
        try:
            exercise()
        except Exception:  # pragma: no cover - exercising is best-effort
            pass
    files: list[Path] = []
    for name, mod in list(sys.modules.items()):
        if name.startswith("ave.") and getattr(mod, "__file__", None):
            p = Path(mod.__file__)
            if p.suffix == ".py" and p not in files:
                files.append(p)
    return files


def scan_forbidden_constants(
    files: list[Path],
    *,
    forbidden: tuple[str, ...] = DEFAULT_FORBIDDEN_CONSTANTS,
    guard_decl_file: Path | None = None,
) -> list[str]:
    """Scan executable code of each file for a forbidden-constant import / use /
    call-arg. Returns "CONST@filename" hits. `guard_decl_file` (a driver's own
    forbidden-set declaration line) is exempted in that file only, so the guard
    does not flag its own allowlist declaration."""
    hits: list[str] = []
    for f in files:
        try:
            s = _strip_code(f.read_text())
        except OSError:  # pragma: no cover
            continue
        # α-leak GUARD assertions are defensive (they ASSERT the constant is ABSENT),
        # not a use — strip them in EVERY file so `assert "ALPHA" not in globals()`
        # does not self-fire (the grep-completeness trap). This is the import-time
        # guard the DEC modules ship (srs_dec.py:73-75); flagging it would invert
        # the guard's meaning.
        s = re.sub(r'assert\s+["\'][A-Z_]+["\']\s+not in\s+globals\(\)[^\n]*', "", s)
        if guard_decl_file is not None and f == guard_decl_file:
            s = re.sub(r"_FORBIDDEN[_A-Z]*\s*=\s*\([^)]*\)", "", s)
            s = re.sub(r"DEFAULT_FORBIDDEN_CONSTANTS\s*[:=][^\n]*", "", s)
        for a in forbidden:
            # import X | = X | (X, bare call-arg | , X | X*  | X( | X[
            if re.search(
                rf"(import\s+[^\n]*\b{a}\b|=\s*{a}\b|\(\s*{a}\b|,\s*{a}\b|\b{a}\s*[*(\[])",
                s,
            ):
                hits.append(f"{a}@{f.name}")
    return sorted(set(hits))


def audit_solve_path(
    driver_file: str | Path,
    *,
    exercise: Callable[[], object] | None = None,
    solve_call_name: str = "solve_static",
    allowed_solve_args: tuple[str, ...] = (),
    forbidden: tuple[str, ...] = DEFAULT_FORBIDDEN_CONSTANTS,
) -> EquationAuditResult:
    """Hardened equation-audit over a driver's solve path.

    Args:
        driver_file        : path to the driver module being audited.
        exercise           : optional zero-arg callable that loads the solve path
                             (so the import closure is fully populated before scan).
        solve_call_name    : the solve function whose call-args are allowlist-checked
                             (e.g. "solve_static"). Every `solve_call_name(<args>)`
                             call in the closure code must have `<args>` in
                             `allowed_solve_args` (EXACT match, anchored — no prefix
                             evasion).
        allowed_solve_args : the exact-match allowlist of permitted solve arguments.
        forbidden          : forbidden constants to scan for.

    Returns EquationAuditResult; `.passed` iff the driver itself is forbidden-clean
    AND every solve-call arg is allowlisted. Closure-wide α-leak is REPORTED (pair
    with runtime-independence for the load-bearing α-free guarantee).
    """
    driver_path = Path(driver_file)
    files = import_closure_modules(exercise)
    if driver_path not in files:
        files = [driver_path, *files]

    closure_hits = scan_forbidden_constants(files, forbidden=forbidden, guard_decl_file=driver_path)
    driver_hits = tuple(h for h in closure_hits if h.endswith(f"@{driver_path.name}"))
    driver_clean = len(driver_hits) == 0

    # exact-match solve-arg allowlist over the whole closure code.
    allowed = {a.strip() for a in allowed_solve_args}
    unexpected: list[str] = []
    for f in files:
        try:
            s = _strip_code(f.read_text())
        except OSError:  # pragma: no cover
            continue
        for call in re.findall(rf"{re.escape(solve_call_name)}\(([^)]*)\)", s):
            if call.strip() not in allowed:
                unexpected.append(f"{call.strip()}@{f.name}")
    unexpected = sorted(set(unexpected))
    solve_args_ok = len(unexpected) == 0

    return EquationAuditResult(
        scanned_modules=tuple(sorted(f.name for f in files)),
        forbidden_in_closure=tuple(closure_hits),
        forbidden_in_driver=driver_hits,
        driver_clean=driver_clean,
        unexpected_solve_args=tuple(unexpected),
        solve_args_ok=solve_args_ok,
        detail=(
            f"{len(files)} closure modules scanned; "
            f"{len(closure_hits)} α-carrier hits in closure ({len(driver_hits)} in driver); "
            f"{len(unexpected)} un-allowlisted {solve_call_name}() calls."
        ),
    )


__all__ = [
    "audit_solve_path",
    "scan_forbidden_constants",
    "import_closure_modules",
    "EquationAuditResult",
    "DEFAULT_FORBIDDEN_CONSTANTS",
]

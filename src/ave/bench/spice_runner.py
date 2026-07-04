#!/usr/bin/env python3
"""
ngspice batch-mode runner — the SPICE PHASE-1 validation-ladder engine hook.
============================================================================

The SPICE lane charter (``_orchestration/2026-07-03_spice-lane-charter.md``)
chartered an *emit-only* lane: a netlist compiler + a canonical ``.lib`` that
had **never been parsed by a SPICE engine**. This module is the missing
engine hook — a thin, dependency-light wrapper around the ``ngspice -b``
(batch) subprocess that PHASE-1 uses to run the five-rung validation ladder
for the first time.

Scope (deliberately minimal — this is a cross-check tool, not a solver;
charter design-(f)):
  * write a ``.cir`` to disk, invoke ``ngspice -b``, capture stdout/stderr,
  * parse ``wrdata``-emitted columnar output (the batch-safe data channel),
  * parse ``.OP`` node voltages from the printed operating point.

ngspice-46 batch-mode contract (established empirically, SPICE PHASE-1
2026-07-04): ``.AC`` / ``.TRAN`` analyses under ``-b`` produce **no output
and error "no simulations run"** unless the netlist carries an explicit
``.control ... run ... .endc`` block with a ``wrdata`` / ``print`` directive.
Bare ``.OP`` + ``.END`` prints the operating point automatically. All rung
drivers therefore emit a ``.control`` block and export data via ``wrdata``.

This module lives in the SPICE lane (charter-scoped); it does NOT touch the
srs engine, solvers, or topological code.
"""

from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

NGSPICE_BIN = "ngspice"


def ngspice_available() -> bool:
    """True iff an ``ngspice`` binary is on PATH."""
    return shutil.which(NGSPICE_BIN) is not None


def ngspice_version() -> str:
    """Return the ngspice banner version string (e.g. 'ngspice-46'), or ''."""
    if not ngspice_available():
        return ""
    try:
        out = subprocess.run(
            [NGSPICE_BIN, "--version"],
            capture_output=True,
            text=True,
            timeout=15,
        )
    except (subprocess.SubprocessError, OSError):
        return ""
    for line in (out.stdout + out.stderr).splitlines():
        if "ngspice-" in line:
            # e.g. "** ngspice-46 : Circuit level simulation program"
            for tok in line.replace("*", " ").split():
                if tok.startswith("ngspice-"):
                    return tok
    return ""


@dataclass
class NgspiceResult:
    """Outcome of one ``ngspice -b`` invocation."""

    returncode: int
    stdout: str
    stderr: str
    cir_path: Path
    data: dict[str, np.ndarray] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        """Ran without a fatal error.

        ngspice returns 0 on a clean batch run; a nonzero code OR the
        "no simulations run" / "fatal error" strings mean failure.
        """
        blob = (self.stdout + self.stderr).lower()
        if "fatal error" in blob or "no simulations run" in blob:
            return False
        return self.returncode == 0


def run_ngspice(
    netlist: str,
    cir_path: str | Path,
    *,
    timeout: float = 60.0,
) -> NgspiceResult:
    """
    Write ``netlist`` to ``cir_path`` and run ``ngspice -b`` on it.

    Returns an :class:`NgspiceResult`. Does NOT parse data — pair with
    :func:`read_wrdata` on any file the netlist's ``wrdata`` wrote.
    """
    cir_path = Path(cir_path)
    cir_path.parent.mkdir(parents=True, exist_ok=True)
    cir_path.write_text(netlist, encoding="utf-8")

    if not ngspice_available():
        raise RuntimeError(
            "ngspice not on PATH. SPICE PHASE-1 requires a live ngspice "
            "(brew install ngspice)."
        )

    proc = subprocess.run(
        [NGSPICE_BIN, "-b", str(cir_path)],
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return NgspiceResult(
        returncode=proc.returncode,
        stdout=proc.stdout,
        stderr=proc.stderr,
        cir_path=cir_path,
    )


def read_wrdata(path: str | Path, columns: list[str]) -> dict[str, np.ndarray]:
    """
    Parse an ngspice ``wrdata``-emitted file into named columns.

    ``wrdata`` writes whitespace-separated columns. For a real-valued
    analysis (``.op`` / ``.dc`` / ``.tran``) each requested vector is ONE
    column, preceded by the sweep column. For a complex analysis (``.ac``)
    each vector is TWO columns (real, imag) preceded by the (real) sweep
    column that is itself duplicated as (value, 0).

    ``columns`` is the list of column NAMES the caller expects, in file
    order (including any leading sweep column). Returns a name->array dict.

    The caller is responsible for knowing its own column layout — this is a
    dumb columnar reader, not a ngspice-format interpreter.
    """
    path = Path(path)
    raw = np.loadtxt(path)
    if raw.ndim == 1:
        raw = raw.reshape(1, -1)
    if raw.shape[1] != len(columns):
        raise ValueError(
            f"wrdata column count mismatch: file {path.name} has "
            f"{raw.shape[1]} columns, caller named {len(columns)} "
            f"({columns})."
        )
    return {name: raw[:, idx] for idx, name in enumerate(columns)}


def parse_op_voltages(stdout: str) -> dict[str, float]:
    """
    Parse node voltages from an ngspice ``.OP`` batch print.

    ngspice-46 prints the operating point as lines like::

        V(1)                             1.000000e+00
        v(n2)                           -3.210000e-03

    Returns a lowercased-node-name -> voltage dict. Robust to the two
    print forms (``V(node)`` header table and ``print``-style ``v(node) =``).
    """
    volts: dict[str, float] = {}
    for line in stdout.splitlines():
        s = line.strip()
        low = s.lower()
        if not low.startswith("v(") and "v(" not in low[:4]:
            continue
        # Two forms: "V(1)   1.0e+00"  and  "v(1) = 1.0e+00"
        cleaned = s.replace("=", " ")
        toks = cleaned.split()
        if len(toks) < 2:
            continue
        name = toks[0]
        if not (name.lower().startswith("v(") and name.endswith(")")):
            continue
        node = name[2:-1].lower()
        try:
            volts[node] = float(toks[-1])
        except ValueError:
            continue
    return volts

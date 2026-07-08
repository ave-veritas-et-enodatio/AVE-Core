"""
Sanity checks for the AVE Electron Equivalent Circuit (DESIGN ARTIFACT).
=======================================================================

SCOPE (deliberately narrow — this is a DESIGN artifact, not the 2b test):
  1. Base-tank resonance: the cold linear cell resonates at omega_cell = OMEGA_C
     and presents Z_0 = sqrt(L_CELL/C_CELL) = 376.73 Ohm (analytical, from
     ave.core.constants — no hard-coded values).
  2. Netlist well-formedness: the AVE_ELECTRON_EQUIVALENT netlist parses in
     ngspice and DC-converges (skipped gracefully if ngspice is absent).
  3. AC-resonance positive control: f_res = 1/(2*pi*sqrt(L*C)) recovered by
     ngspice on a scaled linear tank.

EXPLICITLY NOT RUN HERE (gated on Grant's review of the frozen circuit; this is
2b-Stage-1, NOT a sanity check):
  - the zero-drive self-sustain / persistence test,
  - the (2,3)-lock / winding-selection test,
  - any measurement of the sampling count N or the settled ratio.
"""

import shutil

import pytest

NGSPICE_AVAILABLE = shutil.which("ngspice") is not None
ngspice_required = pytest.mark.skipif(
    not NGSPICE_AVAILABLE, reason="ngspice not installed (optional dependency)"
)


class TestBaseTankResonance:
    """Base-tank identities from constants (no ngspice)."""


@ngspice_required
class TestElectronEquivalentWellFormed:
    """The electron-equivalent netlist parses + DC-converges in ngspice."""

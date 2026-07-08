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
import subprocess
import tempfile
from pathlib import Path

import numpy as np
import pytest

from ave.core.constants import C_CELL, EPSILON_0, L_CELL, L_NODE, MU_0, OMEGA_C, V_YIELD, Z_0
from ave.solvers.spice_netlist_compiler import (
    compile_electron_equivalent_dc_probe,
    electron_equivalent_lib_path,
    lib_path,
    write_netlist,
)

NGSPICE_AVAILABLE = shutil.which("ngspice") is not None
ngspice_required = pytest.mark.skipif(
    not NGSPICE_AVAILABLE, reason="ngspice not installed (optional dependency)"
)


class TestBaseTankResonance:
    """
    Base-tank identities from constants (no ngspice).

    The equivalent circuit's base cell is the K4-bond LC tank:
      L_cell = mu_0 * ell_node,  C_cell = eps_0 * ell_node
      Z_0    = sqrt(L_cell/C_cell) = sqrt(mu_0/eps_0) = 376.73 Ohm
      omega_cell = 1/sqrt(L_cell*C_cell) = OMEGA_C (the Compton frequency)
    """

    def test_lib_files_exist(self) -> None:
        """Both the base cell lib and the electron-equivalent lib resolve in-tree."""
        assert lib_path().exists(), "base cell lib missing"
        assert electron_equivalent_lib_path().exists(), "electron-equivalent lib missing"

    def test_cell_values_are_lumped_per_node(self) -> None:
        """L_cell = mu_0*ell_node and C_cell = eps_0*ell_node (the cell tank)."""
        assert np.isclose(L_CELL, MU_0 * L_NODE, rtol=1e-12)
        assert np.isclose(C_CELL, EPSILON_0 * L_NODE, rtol=1e-12)

    def test_base_tank_impedance_is_Z0(self) -> None:
        """Z_0 = sqrt(L_cell/C_cell) = 376.73 Ohm (the matched-port anchor)."""
        z_from_tank = np.sqrt(L_CELL / C_CELL)
        assert np.isclose(z_from_tank, Z_0, rtol=1e-9)
        assert np.isclose(z_from_tank, np.sqrt(MU_0 / EPSILON_0), rtol=1e-9)
        assert abs(z_from_tank - 376.730313) < 1e-3

    def test_base_tank_resonates_at_omega_cell(self) -> None:
        """omega_cell = 1/sqrt(L_cell*C_cell) = OMEGA_C (Compton frequency)."""
        omega_from_tank = 1.0 / np.sqrt(L_CELL * C_CELL)
        assert np.isclose(omega_from_tank, OMEGA_C, rtol=1e-9)


@ngspice_required
class TestElectronEquivalentWellFormed:
    """The electron-equivalent netlist parses + DC-converges in ngspice."""

    def _run(self, netlist: str, name: str) -> subprocess.CompletedProcess:
        with tempfile.TemporaryDirectory() as tmpdir:
            cir = write_netlist(netlist, Path(tmpdir) / name)
            return subprocess.run(
                ["ngspice", "-b", str(cir)],
                capture_output=True,
                text=True,
                timeout=60,
            )

    def test_dc_probe_parses_and_converges(self) -> None:
        """The frozen electron equivalent circuit parses + finds a DC op point."""
        netlist = compile_electron_equivalent_dc_probe(l0=1e-9, c0=1e-12, v_a1=V_YIELD)
        result = self._run(netlist, "electron_eq_dc.cir")

        # ngspice returns 0 on a clean run; a parse/convergence failure is non-zero
        # or leaves 'aborted'/'fatal' in the output.
        assert result.returncode == 0, f"ngspice failed:\n{result.stdout}\n{result.stderr}"
        combined = (result.stdout + result.stderr).lower()
        for bad in ("aborted", "fatal error", "singular matrix", "no such"):
            assert bad not in combined, f"ngspice reported '{bad}':\n{result.stdout}"

    def test_a1_bias_node_holds_operating_point(self) -> None:
        """The A1 mass-bias node sits at the applied static bias V_A1 = V_YIELD."""
        netlist = compile_electron_equivalent_dc_probe(l0=1e-9, c0=1e-12, v_a1=V_YIELD)
        result = self._run(netlist, "electron_eq_dc.cir")
        assert result.returncode == 0, result.stdout

        v_a1b = None
        for line in result.stdout.splitlines():
            if "v(a1b)" in line.lower():
                v_a1b = float(line.split("=")[-1].strip())
        assert v_a1b is not None, f"v(a1b) not reported:\n{result.stdout}"
        # zero-drive: the tanks sit at 0; only the biased A1 node is energized.
        assert np.isclose(v_a1b, V_YIELD, rtol=1e-4)


@ngspice_required
class TestACResonancePositiveControl:
    """
    Positive control: ngspice recovers f_res = 1/(2*pi*sqrt(L*C)) for the scaled
    linear base cell, confirming the resonance formula the analytical base-tank
    identities assert at the physical (OMEGA_C) scale.
    """

    def test_linear_tank_ac_resonance(self) -> None:
        l0, c0 = 1e-9, 1e-12
        f_res = 1.0 / (2.0 * np.pi * np.sqrt(l0 * c0))
        netlist = f"""\
* AC resonance positive control — scaled linear base cell tank
.INCLUDE {lib_path()}
I_AC N1 0 AC 1
X1 N1 0 AVE_VACUUM_CELL_LINEAR L0={l0:.6e} C0={c0:.6e} R0=0
.AC DEC 400 1e8 1e11
.control
run
meas ac fpeak max_at vm(N1) from=1e8 to=1e11
print fpeak
.endc
.END
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            cir = write_netlist(netlist, Path(tmpdir) / "ac_res.cir")
            result = subprocess.run(
                ["ngspice", "-b", str(cir)],
                capture_output=True,
                text=True,
                timeout=60,
            )
        assert result.returncode == 0, result.stdout

        fpeak = None
        for line in result.stdout.splitlines():
            if line.strip().lower().startswith("fpeak") and "=" in line:
                fpeak = float(line.split("=")[-1].strip())
        assert fpeak is not None, f"fpeak not reported:\n{result.stdout}"
        # log-sweep grid resolution limits agreement to ~1%.
        assert np.isclose(fpeak, f_res, rtol=2e-2), f"fpeak={fpeak:.4e} vs f_res={f_res:.4e}"

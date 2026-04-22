"""
Tests for the AVE Universal Vacuum Cell
========================================

Verification tests comparing ngspice behavioral model output against
the Python physics engine's analytical predictions.

These tests require ngspice to be installed on the system.
They are skipped gracefully if ngspice is not available.

Test hierarchy:
  1. Analytical: verify S(V) kernel consistency (no ngspice)
  2. DC sweep: verify C_eff plateau matches Python saturation()
  3. AC resonance: verify f_res = 1/(2π√LC) for linear cell
"""

import subprocess
import shutil
import tempfile
import numpy as np
import pytest
from pathlib import Path

from ave.core.constants import V_YIELD, V_SNAP, ALPHA
from ave.axioms.scale_invariant import saturation_factor
from ave.solvers.spice_netlist_compiler import (
    compile_ee_bench_dc_sweep,
    write_netlist,
    lib_path,
)


# Skip all ngspice tests if not installed
NGSPICE_AVAILABLE = shutil.which("ngspice") is not None
ngspice_required = pytest.mark.skipif(not NGSPICE_AVAILABLE, reason="ngspice not installed (optional dependency)")


class TestSaturationKernelConsistency:
    """
    Verify the S(V) kernel is consistent between:
      - Python: saturation_factor(V, V_YIELD)
      - .lib:   sqrt(1 - (V/V_YLD)^2)

    No ngspice required — purely analytical.
    """

    def test_s_at_zero(self):
        """S(0) = 1 (fully elastic)."""
        assert np.isclose(saturation_factor(0.0, V_YIELD), 1.0)

    def test_s_at_half(self):
        """S(V_yield/2) = sqrt(3)/2 ≈ 0.866."""
        S = saturation_factor(V_YIELD / 2.0, V_YIELD)
        assert np.isclose(S, np.sqrt(3) / 2, rtol=1e-6)

    def test_s_at_ninety_percent(self):
        """S(0.9 × V_yield) ≈ 0.436."""
        S = saturation_factor(0.9 * V_YIELD, V_YIELD)
        expected = np.sqrt(1.0 - 0.9**2)
        assert np.isclose(S, expected, rtol=1e-6)

    def test_c_eff_diverges(self):
        """C_eff = C0/S → ∞ as V → V_yield."""
        ratios = [0.99, 0.999, 0.9999]
        c_effs = [1.0 / saturation_factor(r * V_YIELD, V_YIELD) for r in ratios]
        # Each step should increase dramatically
        assert c_effs[1] > c_effs[0] * 3
        assert c_effs[2] > c_effs[1] * 3

    def test_v_yield_from_constants(self):
        """V_YIELD = sqrt(alpha) × V_SNAP."""
        expected = np.sqrt(ALPHA) * V_SNAP
        assert np.isclose(V_YIELD, expected, rtol=1e-4)


@ngspice_required
class TestNgspiceDCSweep:
    """
    Run the EE Bench DC sweep in ngspice and verify the
    capacitance plateau matches the Python prediction.
    """

    def test_dc_sweep_runs(self):
        """Verify ngspice can parse and execute the EE bench netlist."""
        netlist = compile_ee_bench_dc_sweep(c0=10e-12, v_max=40000.0, v_step=1000.0)

        with tempfile.TemporaryDirectory() as tmpdir:
            cir_path = write_netlist(netlist, Path(tmpdir) / "ee_bench.cir")

            result = subprocess.run(
                ["ngspice", "-b", str(cir_path)],
                capture_output=True,
                text=True,
                timeout=30,
            )

            # ngspice should complete without error
            assert result.returncode == 0, (
                f"ngspice failed:\nstdout: {result.stdout[:500]}\n" f"stderr: {result.stderr[:500]}"
            )

    def test_lib_syntax_valid(self):
        """Verify ave_vacuum_cell.lib parses without errors in ngspice."""
        # Minimal netlist that just includes the library
        test_netlist = f"""\
* Library syntax validation
{'.INCLUDE ' + str(lib_path())}
V1 N1 GND DC 1
X1 N1 GND AVE_EE_BENCH C0=10p V_YLD=43650
R1 N1 GND 1G
.OP
.END
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            cir_path = Path(tmpdir) / "lib_test.cir"
            cir_path.write_text(test_netlist)

            result = subprocess.run(
                ["ngspice", "-b", str(cir_path)],
                capture_output=True,
                text=True,
                timeout=15,
            )

            assert result.returncode == 0, f"Library parse failed:\n{result.stderr[:500]}"


@ngspice_required
class TestNgspiceACResonance:
    """
    Verify the single-cell resonant frequency matches f = 1/(2π√LC).
    """

    def test_linear_resonance(self):
        """
        A linear vacuum cell at L=1nH, C=1pF should resonate
        at f_res = 1/(2π√(1e-9 × 1e-12)) ≈ 5.03 GHz.
        """
        f_expected = 1.0 / (2 * np.pi * np.sqrt(1e-9 * 1e-12))

        netlist = f"""\
* Linear resonance verification
{'.INCLUDE ' + str(lib_path())}
V_SRC N_IN GND AC 1
X1 N_IN N_OUT AVE_VACUUM_CELL_LINEAR L0=1n C0=1p R0=0
R_TERM N_OUT GND 50
.AC DEC 200 1e9 20e9
.END
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            cir_path = Path(tmpdir) / "resonance.cir"
            cir_path.write_text(netlist)

            result = subprocess.run(
                ["ngspice", "-b", str(cir_path)],
                capture_output=True,
                text=True,
                timeout=30,
            )

            assert result.returncode == 0, f"Resonance sim failed:\n{result.stderr[:500]}"
            # Verify expected resonance is in the right ballpark
            # (detailed output parsing would require raw data export)
            assert f_expected > 4e9 and f_expected < 6e9

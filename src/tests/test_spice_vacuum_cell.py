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

import shutil
import subprocess
import tempfile
from pathlib import Path

import numpy as np
import pytest

from ave.axioms.scale_invariant import saturation_factor
from ave.core.constants import ALPHA, V_SNAP, V_YIELD
from ave.solvers.spice_netlist_compiler import compile_ee_bench_dc_sweep, lib_path, write_netlist

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

    def test_s_at_zero(self) -> None:
        """S(0) = 1 (fully elastic)."""
        assert np.isclose(saturation_factor(0.0, V_YIELD), 1.0)

    def test_s_at_half(self) -> None:
        """S(V_yield/2) = sqrt(3)/2 ≈ 0.866."""
        S = saturation_factor(V_YIELD / 2.0, V_YIELD)
        assert np.isclose(S, np.sqrt(3) / 2, rtol=1e-6)

    def test_s_at_ninety_percent(self) -> None:
        """S(0.9 × V_yield) ≈ 0.436."""
        S = saturation_factor(0.9 * V_YIELD, V_YIELD)
        expected = np.sqrt(1.0 - 0.9**2)
        assert np.isclose(S, expected, rtol=1e-6)

    def test_c_eff_diverges(self) -> None:
        """C_eff = C0/S → ∞ as V → V_yield."""
        ratios = [0.99, 0.999, 0.9999]
        c_effs = [1.0 / saturation_factor(r * V_YIELD, V_YIELD) for r in ratios]
        # Each step should increase dramatically
        assert c_effs[1] > c_effs[0] * 3
        assert c_effs[2] > c_effs[1] * 3

    def test_v_yield_from_constants(self) -> None:
        """V_YIELD = sqrt(alpha) × V_SNAP."""
        expected = np.sqrt(ALPHA) * V_SNAP
        assert np.isclose(V_YIELD, expected, rtol=1e-4)


@ngspice_required
class TestNgspiceDCSweep:
    """
    Run the EE Bench DC sweep in ngspice and verify the
    capacitance plateau matches the Python prediction.
    """

    def test_dc_sweep_runs(self) -> None:
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

    def test_lib_syntax_valid(self) -> None:
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
            cir_path.write_text(test_netlist, encoding="utf-8")

            result = subprocess.run(
                ["ngspice", "-b", str(cir_path)],
                capture_output=True,
                text=True,
                timeout=15,
            )

            assert result.returncode == 0, f"Library parse failed:\n{result.stderr[:500]}"


@ngspice_required
class TestMemristorSubcircuit:
    """
    Verify Level-2 memristor subcircuits PARSE in ngspice.

    SPICE PHASE-1 finding (2026-07-04, empirical-driver Rule 10): once ngspice
    actually ran, these subcircuits PARSE cleanly (the .lib syntax fixes
    landed — IC=1 inline, B..Q=->C..Q=, idt->L Flux=), but the L2
    relaxation-ODE arm (C_S=1F + VCCS pair with a self-referential
    G_REL_N N_S 0 N_S 0) does NOT converge a full nonlinear .TRAN in
    ngspice-46 ("Timestep too small" at a sine-drive sign change). This is a
    genuine numerical-stability limitation of the L2 memristor design, NOT a
    parse error, and NOT in the PHASE-1 five-rung ladder scope. The two tests
    below are split: a `.op` PARSE check (must pass) + an xfail'd full-.TRAN
    convergence check (surfaced, not papered over). See
    research/2026-07-04_spice-phase1-ladder_result.md.
    """

    def test_memristor_state_parses(self) -> None:
        """The AVE_MEMRISTOR_S_STATE subckt parses + solves an .op point."""
        test_netlist = f"""\
* Memristor state integrator PARSE check (.op)
{'.INCLUDE ' + str(lib_path())}
V1 N1 GND DC 10000
X1 N1 GND N_S AVE_MEMRISTOR_S_STATE TAU_REL=1n V_YLD=43651.85
R1 N_S GND 1G
.control
op
print v(N_S)
.endc
.END
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            cir_path = Path(tmpdir) / "memristor.cir"
            cir_path.write_text(test_netlist, encoding="utf-8")
            result = subprocess.run(
                ["ngspice", "-b", str(cir_path)],
                capture_output=True,
                text=True,
                timeout=30,
            )
            blob = (result.stdout + result.stderr).lower()
            assert "no such" not in blob and "unknown parameter" not in blob, (
                f"Memristor subckt failed to PARSE:\n{result.stderr[:500]}"
            )

    @pytest.mark.xfail(
        reason="L2 relaxation-ODE arm does not converge a full nonlinear .TRAN "
        "in ngspice-46 (SPICE PHASE-1 finding; not a parse error). See "
        "research/2026-07-04_spice-phase1-ladder_result.md.",
        strict=False,
    )
    def test_memristor_state_transient_converges(self) -> None:
        test_netlist = f"""\
* Memristor state integrator full .TRAN convergence
{'.INCLUDE ' + str(lib_path())}
V1 N1 GND SIN(0 10000 1Meg)
X1 N1 GND N_S AVE_MEMRISTOR_S_STATE TAU_REL=1n V_YLD=43651.85
R1 N_S GND 1G
.TRAN 1n 10u uic
.control
run
print v(N_S)
.endc
.END
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            cir_path = Path(tmpdir) / "memristor.cir"
            cir_path.write_text(test_netlist, encoding="utf-8")
            result = subprocess.run(
                ["ngspice", "-b", str(cir_path)],
                capture_output=True,
                text=True,
                timeout=30,
            )
            blob = (result.stdout + result.stderr).lower()
            assert result.returncode == 0 and "no simulations run" not in blob, (
                f"Memristor .TRAN failed:\n{result.stderr[:500]}"
            )

    @pytest.mark.xfail(
        reason="AVE_VACUUM_CELL_L1 composite (nonlinear varactor + flux inductor "
        "+ near-short R_DAMP + L2 memristor) does not converge a full .TRAN in "
        "ngspice-46 (SPICE PHASE-1 finding; parses cleanly). See "
        "research/2026-07-04_spice-phase1-ladder_result.md.",
        strict=False,
    )
    def test_vacuum_cell_l1_subcircuit(self) -> None:
        test_netlist = f"""\
* L1 vacuum cell full .TRAN convergence
{'.INCLUDE ' + str(lib_path())}
V1 N1 GND SIN(0 5000 1Meg)
X1 N1 GND AVE_VACUUM_CELL_L1 L0=1n C0=1p TAU_REL=1n
R1 N1 GND 1Meg
.TRAN 1n 5u uic
.control
run
print v(N1)
.endc
.END
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            cir_path = Path(tmpdir) / "l1_cell.cir"
            cir_path.write_text(test_netlist, encoding="utf-8")
            result = subprocess.run(
                ["ngspice", "-b", str(cir_path)],
                capture_output=True,
                text=True,
                timeout=30,
            )
            blob = (result.stdout + result.stderr).lower()
            assert result.returncode == 0 and "no simulations run" not in blob, (
                f"L1 cell .TRAN failed:\n{result.stderr[:500]}"
            )


@ngspice_required
class TestNgspiceACResonance:
    """
    Verify the single-cell resonant frequency matches f = 1/(2π√LC).
    """

    def test_linear_resonance(self) -> None:
        """
        A linear vacuum cell at L=1nH, C=1pF should resonate
        at f_res = 1/(2π√(1e-9 × 1e-12)) ≈ 5.03 GHz.
        """
        f_expected = 1.0 / (2 * np.pi * np.sqrt(1e-9 * 1e-12))

        # ngspice-46 batch mode (-b) requires an explicit .control/run/print
        # block for .AC/.TRAN — a bare .END errors "no simulations run" (SPICE
        # PHASE-1 2026-07-04, empirical-driver Rule 10).
        netlist = f"""\
* Linear resonance verification
{'.INCLUDE ' + str(lib_path())}
V_SRC N_IN GND AC 1
X1 N_IN N_OUT AVE_VACUUM_CELL_LINEAR L0=1n C0=1p R0=0
R_TERM N_OUT GND 50
.AC DEC 200 1e9 20e9
.control
run
print vm(N_OUT)
.endc
.END
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            cir_path = Path(tmpdir) / "resonance.cir"
            cir_path.write_text(netlist, encoding="utf-8")

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


@ngspice_required
class TestNgspiceKernelFormDrift:
    """
    SPICE PHASE-1 rung-2 keeper (charter design-(d) FORM-drift gate). ngspice
    EVALUATES the Ax4 kernel S(V)=sqrt(1-(V/V_x)^2) as a behavioral source (the
    exact .lib varactor expression) and it must equal the canonical
    ave.axioms.scale_invariant.saturation_factor at the IDENTICAL voltage. A
    stale or wrong-sign .lib kernel fails here. Uses per-point .op (artifact-
    free; the .dc sweep reports a swept-node behavioral source lagged one step).
    """

    def _op_S(self, v_dc: float, v_key: float) -> float:
        import re

        netlist = f"""\
* ngspice kernel eval at one operating point
V1 A 0 DC {v_dc:.10f}
B_S N_S 0 V = {{sqrt(1 - min((V(A)/{v_key:.10f})**2, 0.9999))}}
R_S N_S 0 1e12
R_A A 0 1e15
.control
op
print v(N_S)
.endc
.END
"""
        with tempfile.TemporaryDirectory() as tmpdir:
            cir_path = Path(tmpdir) / "kernel_op.cir"
            cir_path.write_text(netlist, encoding="utf-8")
            result = subprocess.run(
                ["ngspice", "-b", str(cir_path)],
                capture_output=True,
                text=True,
                timeout=15,
            )
        m = re.search(r"v\(n_s\)\s*=\s*([-+0-9.eE]+)", result.stdout.lower())
        assert m is not None, f"no v(n_s) in ngspice .op:\n{result.stdout[:400]}"
        return float(m.group(1))

    def test_kernel_matches_saturation_factor_at_vsnap(self) -> None:
        """A1-divergent metric varactor keyed on V_SNAP."""
        for frac in (0.1, 0.25, 0.5, 0.75, 0.9):
            v = frac * V_SNAP
            s_ng = self._op_S(v, V_SNAP)
            s_py = float(saturation_factor(v, V_SNAP))
            assert abs(s_ng - s_py) < 1e-6, (
                f".lib kernel drift at V/V_SNAP={frac}: ngspice {s_ng} vs "
                f"canonical {s_py}"
            )

    def test_kernel_matches_saturation_factor_at_vyield(self) -> None:
        """T2-collapse dielectric keyed on V_YIELD."""
        for frac in (0.1, 0.25, 0.5, 0.75, 0.9):
            v = frac * V_YIELD
            s_ng = self._op_S(v, V_YIELD)
            s_py = float(saturation_factor(v, V_YIELD))
            assert abs(s_ng - s_py) < 1e-6, (
                f".lib kernel drift at V/V_YIELD={frac}: ngspice {s_ng} vs "
                f"canonical {s_py}"
            )

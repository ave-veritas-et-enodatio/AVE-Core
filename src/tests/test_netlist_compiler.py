"""
Tests for the AVE SPICE Netlist Compiler
========================================

Unit tests for netlist string generation (no ngspice required).
Verifies .INCLUDE paths, component naming, .CONTROL blocks,
and round-trip topology consistency.
"""

import pytest
from pathlib import Path

from ave.solvers.spice_netlist_compiler import (
    compile_ee_bench_dc_sweep,
    compile_lcr_network,
    compile_amino_acid_network,
    lib_path,
    write_netlist,
)


class TestLibPath:
    """Verify the .lib file exists and is reachable."""

    def test_lib_file_exists(self):
        p = lib_path()
        assert p.exists(), f"Universal cell library not found: {p}"

    def test_lib_contains_subcircuit(self):
        content = lib_path().read_text()
        assert ".subckt AVE_VACUUM_CELL " in content
        assert ".subckt AVE_VACUUM_CELL_LINEAR " in content
        assert ".subckt AVE_EE_BENCH " in content


class TestEEBenchNetlist:
    """Verify the EE Bench DC sweep netlist."""

    def test_generates_valid_netlist(self):
        netlist = compile_ee_bench_dc_sweep()
        assert "V_SWEEP" in netlist
        assert "AVE_EE_BENCH" in netlist
        assert ".DC" in netlist
        assert ".END" in netlist

    def test_includes_lib(self):
        netlist = compile_ee_bench_dc_sweep()
        assert ".INCLUDE" in netlist
        assert "ave_vacuum_cell.lib" in netlist

    def test_custom_parameters(self):
        netlist = compile_ee_bench_dc_sweep(c0=20e-12, v_yield=50000.0, v_max=55000.0, v_step=50.0)
        assert "2.000000e-11" in netlist  # 20 pF
        assert "50000.0" in netlist
        assert ".DC V_SWEEP 0 55000 50" in netlist

    def test_contains_control_block(self):
        netlist = compile_ee_bench_dc_sweep()
        assert ".control" in netlist
        assert ".endc" in netlist
        assert "deriv" in netlist  # C_eff = dQ/dV


class TestLCRNetwork:
    """Verify generic LCR network compilation."""

    def _simple_network(self, use_nonlinear=True):
        nodes = [{"id": "N_IN"}, {"id": "N1"}, {"id": "N_OUT"}]
        edges = [
            {"from": "N_IN", "to": "N1", "L": 1e-9, "C": 1e-12, "R": 0.0},
            {"from": "N1", "to": "N_OUT", "L": 2e-9, "C": 0.5e-12, "R": 100.0},
        ]
        return compile_lcr_network(
            nodes=nodes,
            edges=edges,
            use_nonlinear=use_nonlinear,
        )

    def test_nonlinear_network(self):
        netlist = self._simple_network(use_nonlinear=True)
        assert "AVE_VACUUM_CELL" in netlist
        assert "V_YLD=" in netlist
        assert "I_YMAX=" in netlist

    def test_linear_network(self):
        netlist = self._simple_network(use_nonlinear=False)
        assert "AVE_VACUUM_CELL_LINEAR" in netlist
        assert "V_YLD=" not in netlist

    def test_correct_edge_count(self):
        netlist = self._simple_network()
        assert "X0 " in netlist
        assert "X1 " in netlist

    def test_termination_resistor(self):
        netlist = self._simple_network()
        assert "R_TERM N_OUT GND 50" in netlist

    def test_ac_analysis_default(self):
        netlist = self._simple_network()
        assert ".AC DEC" in netlist

    def test_shunt_resistors(self):
        nodes = [
            {"id": "N_IN"},
            {"id": "N1", "shunt_r": 1e6},
            {"id": "N_OUT"},
        ]
        edges = [
            {"from": "N_IN", "to": "N1", "L": 1e-9, "C": 1e-12},
            {"from": "N1", "to": "N_OUT", "L": 1e-9, "C": 1e-12},
        ]
        netlist = compile_lcr_network(nodes=nodes, edges=edges)
        assert "R_SH_N1" in netlist


class TestAminoAcidNetwork:
    """Verify amino acid SPICE model generation."""

    def test_glycine_netlist(self):
        bonds = [
            {"from": "N", "to": "CA", "L": 1.2e-18, "C": 3.5e-24, "R": 0.0},
            {"from": "CA", "to": "C", "L": 1.0e-18, "C": 4.0e-24, "R": 0.0},
            {"from": "C", "to": "O", "L": 1.3e-18, "C": 3.0e-24, "R": 0.0},
        ]
        netlist = compile_amino_acid_network("glycine", bonds)
        assert "glycine" in netlist
        assert "AVE_VACUUM_CELL" in netlist
        assert ".AC DEC" in netlist
        # Should cover FTIR range
        assert "1.000000e+12" in netlist  # 1 THz start
        assert "1.000000e+14" in netlist  # 100 THz stop


class TestWriteNetlist:
    """Verify file output."""

    def test_write_and_read(self, tmp_path):
        netlist = compile_ee_bench_dc_sweep()
        out = write_netlist(netlist, tmp_path / "test.cir")
        assert out.exists()
        content = out.read_text()
        assert content == netlist

    def test_creates_parent_dirs(self, tmp_path):
        out = write_netlist("* test", tmp_path / "sub" / "dir" / "test.cir")
        assert out.exists()

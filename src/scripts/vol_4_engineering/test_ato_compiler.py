"""
ATO to VCA Topological Compiler Bridge
======================================

This script maps declarative electronic schema (ato DSL) directly into
Vacuum Circuit Analysis (VCA) kinematic arrays, bridging LLM VLSI design
to fundamental physical lattice testing.
"""

import json
import re

import numpy as np

from ave.core.constants import EE_TO_TOPO_RESISTANCE, M_E, V_YIELD
from ave.solvers.spice_transient import explicit_euler_step

# ═══════════════════════════════════════════════════════════════════
# PARSER AND NETLIST GENERATOR
# ═══════════════════════════════════════════════════════════════════


def parse_ato_to_vca(ato_source: str) -> dict:
    """
    Parses a declarative atopile script snippet and emits a VCA Topological node layout.
    """
    print("--- PARSING ATO SOURCE ---")
    lines = ato_source.strip().split("\n")

    netlist = {
        "status": "VCA_CALIBRATED",
        "module_name": None,
        "nodes": [],
        "kinematic_properties": {"viscosity_R": 0.0, "max_strain_S11": 1.0},
    }

    for line in lines:
        line = line.strip()
        if not line or line.startswith("from"):
            continue

        # Match Module Definition
        mod_match = re.match(r"module\s+(\w+):", line)
        if mod_match:
            netlist["module_name"] = mod_match.group(1)

        # Match Resistance Parameter (e.g. "resistance: ohm = 4.7kohm")
        res_match = re.match(r"resistance:\s*ohm\s*=\s*([\d\.]+)kohm", line)
        if res_match:
            kohm_val = float(res_match.group(1))
            ohms = kohm_val * 1000.0

            # Map Ohms directly to Topological Viscosity [kg/s]
            vca_viscosity = ohms * EE_TO_TOPO_RESISTANCE
            netlist["kinematic_properties"]["viscosity_R"] = vca_viscosity

        # Match Voltage Constraint (e.g. "max_voltage: V = 5V")
        vol_match = re.match(r"max_voltage:\s*V\s*=\s*([\d\.]+)V", line)
        if vol_match:
            volts = float(vol_match.group(1))

            # Strain mapping: Fraction of Dielectric yield (S11 matrix mapping)
            vca_strain = volts / V_YIELD
            netlist["kinematic_properties"]["max_strain_S11"] = vca_strain

        # Match Pin Interfaces (e.g. "p1 = new Electrical")
        pin_match = re.match(r"(\w+)\s*=\s*new\s*Electrical", line)
        if pin_match:
            pin_name = pin_match.group(1)
            netlist["nodes"].append(f"M_A_Port_{pin_name.upper()}")

    return netlist


# ═══════════════════════════════════════════════════════════════════
# EXECUTION
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    MOCK_ATO_CODE = """
from "atopile/interfaces" import Electrical

module Resistor:
    resistance: ohm = 4.7kohm +/- 5%
    max_voltage: V = 5V
    p1 = new Electrical
    p2 = new Electrical
"""

    print("MOCK ATO SCRIPT:")
    print(MOCK_ATO_CODE.strip())
    print("\n----------------\n")

    vca_netlist = parse_ato_to_vca(MOCK_ATO_CODE)
    print(json.dumps(vca_netlist, indent=2))
    print("\n----------------\n")

    print("Testing SPICE explicit Euler simulation on compiled physics constraints...")

    # Run a physical simulation step using the topological mapped R (viscosity)
    theta_current = np.array([1.0])  # Signal amplitude
    velocity_current = np.array([5.0])  # Signal incoming velocity
    grad_potential = np.array([0.5])  # Arbitrary field gradient (restoring force)

    R_topo = vca_netlist["kinematic_properties"]["viscosity_R"]

    # 1 Euler step: dt = 1e-21 (native topological timescale)
    theta_next, vel_next = explicit_euler_step(
        theta=theta_current,
        velocity=velocity_current,
        grad_f=grad_potential,
        L=M_E,
        R=R_topo,
        dt=1e-21,
    )

    print(f"Initial Transmission Velocity: {velocity_current[0]:.6f}")
    print(f"VCA Matrix Viscosity (R_eff, kg/s): {R_topo:.4e}")
    print(f"Decayed Velocity Post-Waveguide Element Transit: {vel_next[0]:.6f}")

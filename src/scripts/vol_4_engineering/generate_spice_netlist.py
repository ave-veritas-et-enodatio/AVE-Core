#!/usr/bin/env python3
"""
Netlist Generation Script
=========================
Extracts Topo-Kinematic bounding matrices from the Python physics engine
and compiles them down to executable SPICE `.cir` netlists.
"""

import os
from ave.condensed.silicon_doping import pn_junction
from ave.condensed.spice_exporter import generate_ave_diode_subcircuit


def generate():
    print("Extracting physical Silicon matrix bounds...")
    junction = pn_junction()

    print("Compiling AVE Macro Model Subcircuit...")
    spice_block = generate_ave_diode_subcircuit(junction, model_name="AVE_DIODE_SI")

    output_path = os.path.join(os.path.dirname(__file__), "ave_topo_diode.cir")
    with open(output_path, "w") as f:
        f.write(spice_block)

    print(f"Successfully generated SPICE layout at: {output_path}")
    print("\nNetlist Preview:")
    print("-" * 50)
    print(spice_block)
    print("-" * 50)


if __name__ == "__main__":
    generate()

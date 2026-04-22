import os
import pathlib

# Ensure the core framework is in PATH
project_root = pathlib.Path(__file__).parent.parent.parent.absolute()

from periodic_table.simulations.spice_exporter import generate_fusion_netlist


def simulate_dt_fusion():
    print("[*] Simulating D-T Fusion Transient Macro-Topology...")

    # Deuterium (Z=1, A=2)
    # A single proton and neutron bounded at optimal distance 1.5d
    d_nodes = [[0.0, 0.75, 0.0], [0.0, -0.75, 0.0]]

    # Tritium (Z=1, A=3)
    # 1 proton, 2 neutrons. Equilateral triangle
    t = 0.866  # sqrt(3)/2
    r = 1.0
    t_nodes = [[0.0, r, 0.0], [-t * r, -0.5 * r, 0.0], [t * r, -0.5 * r, 0.0]]

    output_dir = os.path.join(project_root, "periodic_table", "simulations", "spice_netlists")

    generate_fusion_netlist(
        fusion_name="dt_fusion_transient",
        nodes_a=d_nodes,
        name_a="Deuterium (2H)",
        nodes_b=t_nodes,
        name_b="Tritium (3H)",
        output_dir=output_dir,
    )


if __name__ == "__main__":
    simulate_dt_fusion()

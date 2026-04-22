"""
Stub for SPICE netlist exporter.

The full SPICE export functionality has been moved to a private repository
as part of the IP partition. This stub preserves the import interface so
that the core simulation and test modules continue to function.
"""


def generate_spice_netlist(element_name, Z, A, nodes, output_dir):
    """Generate a SPICE netlist for a given element topology.

    This is a stub — the full implementation resides in a private IP
    repository. The function signature is preserved for API compatibility.
    """

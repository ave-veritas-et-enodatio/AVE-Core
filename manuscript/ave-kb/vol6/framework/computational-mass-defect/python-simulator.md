[↑ Computational Mass Defect](../index.md)
<!-- leaf: verbatim -->
<!-- no-claim: code listing / methodology pointer - no standalone claim -->

## The Python Simulator: EE-Based Thermodynamic Integration

The following Python subroutine demonstrates this analytical realization. By mapping the exact 3D discrete coordinates of the underlying $6^3_2$ nucleon knots, the total mass of the atomic cluster is rapidly calculated by simply subtracting the $1/d$ mutual coupling energy from the raw isolated rest masses.

```
def calculate_topological_mass(Z, A):
    """
    Computes theoretical mass defect using EE Mutual Impedance.
    U_total = sum(U_self) - sum(M_ij)
    """
    N = A - Z
    raw_mass = (Z * M_P_RAW) + (N * M_N_RAW)

    nodes = get_nucleon_coordinates(Z, A)
    if len(nodes) <= 1:
        return raw_mass

    # Calculate Mutual Reactive Coupling (Binding Energy)
    binding_energy = 0.0
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            # Distance between localized topological defect centers
            dist = np.linalg.norm(np.array(nodes[i]) - np.array(nodes[j]))
            binding_energy += K_MUTUAL / dist

    return raw_mass - binding_energy
```

---

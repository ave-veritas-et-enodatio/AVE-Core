# HANDOFF: Atomic Orbital Geometric Penalties

## Branch Goal
Resolve the remaining atomic chemistry TODOs inside the Periodic Table Engine. Mathematically formalize the geometric scattering limits preventing total overlapping states in the core orbitals, specifically $s$-orbital penetration repulsion for Lithium/Beryllium and $p$-orbital spin-pairing structural penalties for Oxygen/Fluorine.

## Context Audit
- **Classical Problem**: Standard QM uses the Pauli exclusion principle as an abstract boolean rule, treating orbitals as probability clouds. Elements like Oxygen have lower ionization energies than expected due to "spin pairing repulsion", empirically curve-fitted by hand in the Schrodinger equation.
- **AVE Axiomatic Resolution**: In the Topological Isomorphism, electron orbitals are resonant LC cavities. Identical topological knot structures placed tightly into the same topological subspace cause discrete physical standing-wave interference (phase collision). $S$-orbital penetration is exactly the near-field scattering of inner Toroidal boundary walls forcing outer cavity deformation. $P$-orbital spin-pairing penalties directly derive from two identical structural gyroscopes trying to precess identically within the same orthogonal locus, suffering continuous topological friction. 
- **Target File**: `src/ave/solvers/coupled_resonator.py`
  - See `Line 432`: `# TODO: s-orbital penetration for Li, Be`
  - See `Line 433`: `# TODO: p-orbital pairing penalty for O, F`

## Architecture Requirements
1. **Solver File (`coupled_resonator.py`)**:
   - Extract the phase geometry for the secondary recursive cascade in atoms $Z=3,4$ (Li, Be). Determine the strict volumetric volume limits (via Axiom 1) proving why the outer valence ring suffers structural decoupling due to passing inside the $1s^2$ Borromean lattice.
   - For $Z=8,9$ (O, F), geometrically derive the scattering factor when a 4th orbital shell is added to a 3-axis $p$-orbital Cartesian sub-lattice. Calculate the topological frictional capacitance required to bend the 4th state away from exact resonance.
   - Inject these parameter-free constants directly into the `predict_atom_mass_and_ionization` recursive cascade.
2. **Workflow Rules**:
   - Execute `/audit-code` to guarantee zero empirical curve fitting parameters were used in the new geometry code.
   - Execute `make vol6` to assure no equations or constants break dynamically in the periodic table generation stack.

## Next Agent Instructions
1. Navigate directly to `src/ave/solvers/coupled_resonator.py` and isolate the Periodic cascade solver logic.
2. Formally derive the two scattering penalties from pure structural knot intersections natively and wire them in to overwrite the TODO lines.
3. Validate the Ionization Energy benchmark against Volume 6 experimental data.
4. Update the corresponding `manuscript/vol_6_periodic_table/` text to thoroughly document the continuous mechanical origin of the Pauli "spin-pairing" abstract jump.

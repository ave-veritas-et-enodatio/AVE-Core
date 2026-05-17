[↑ Ch.7 Quantum Mechanics](index.md)
<!-- leaf: verbatim -->

# Orbital Penetration Penalties (1/d ABCD Matrix)

**Volume:** 2 (Subatomic Scale)
**Chapter:** 7

## The Classical Interpretation

In standard quantum mechanics, "orbital penetration" is a probabilistic phenomenon: the 2s orbital ($l = 0$) has a nonzero probability of being found inside the 1s shell, thereby experiencing less screening and binding more tightly than the 2p ($l = 1$).  This explanation relies on the Born rule and statistical interpretation.

## Axiomatic Reinterpretation

In the AVE framework, orbital penetration is a **deterministic macroscopic LC spatial resonance constraint**.  The ABCD transmission-line cascade solver naturally produces $l$-degeneracy splitting through impedance boundary conditions:

### Op3 Shunt Admittance Penalty

When an outer orbital ($n = 2$, $l = 0$) geometrically intersects an inner filled shell ($n = 1$), the inner shell presents a shunt admittance penalty — a $1/d$ impedance discontinuity at the crossing radius.  This penalty lowers the eigenfrequency of the penetrating mode (stronger binding).

For $l > 0$ orbitals, the centrifugal barrier prevents geometric intersection with the core, and the shunt penalty is not applied.  This breaks the $l$-degeneracy purely from geometry.

### Lithium Validation (Z = 3)

The ABCD cascade solver `radial_eigenvalue_abcd(Z, n, l, shells)` computes:

| State | $l$ | Penetrates Core? | Binding Energy |
|---|---|---|---|
| 2s | 0 | Yes — $1/d$ shunt applied | More negative (tighter bound) |
| 2p | 1 | No — centrifugal barrier | Less negative |

The energy splitting $\Delta E = E_{2s} - E_{2p}$ emerges entirely from the geometric impedance boundary, with zero probabilistic input.

## Key Results

| Result | Statement |
|---|---|
| Mechanism | $1/d$ acoustic reflection penalty at inner-shell crossing radius |
| $l$-degeneracy breaking | Deterministic from impedance geometry, not probabilistic |
| Solver | `radial_eigenvalue_abcd(Z, n, l, shells)` — ABCD cascade |
| Validation | Lithium 2s/2p splitting matches experimental data |

*Cross-references*:
- `src/scripts/vol_2_subatomic/simulate_orbital_penetration.py`
- `src/scripts/vol_2_subatomic/audit_radial_solver.py`
- `src/ave/solvers/radial_eigenvalue.py` (`radial_eigenvalue_abcd`)
- [Radial Eigenvalue Solver](./radial-eigenvalue-solver.md) — the underlying ABCD cascade solver
- [Atom as Radial Waveguide](./atom-as-radial-waveguide.md) — graded impedance profile interpretation

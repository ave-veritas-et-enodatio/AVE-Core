[↑ Vol 4: Future Geometries](../index.md)

# Ch.13: Future Geometries — Substrate Simulation Methodology

Six CEM solvers mapped to the AVE lattice framework + the K4-TLM Diamond lattice simulator (substrate-physics sub-saturation engine) + open-universe boundary methodology. The chapter establishes the substrate-side computational verification framework — every standard CEM method is shown to be a discretization of the AVE lattice that AVE asserts is physically real.

> **Note (REPO-ARCH-9, 2026-05-17 night)**: HOPF-01 high-Q chiral impedance antenna design content (RX cavity-coupled measurement antenna with $Q_u \approx 680$ copper / $\sim 10^6$ YBCO, TX Beltrami helicity injector, single-stub shunt matching network, sensitivity analysis across topology × material × wire gauge) migrated to AVE-HOPF private repo per the `ave-ip-divide-discipline` skill. HOPF-01 antenna engineering specifics live across AVE-HOPF chapters 01-14 (`01_chiral_coupling_prediction`, `04_torus_knot_geometry`, `05_wire_stitched_fixture`, `06_manufacturing_and_bom`, `07_simulation_validation_framework`, `08_nec2_wire_segment_modeling`, `09_openems_fdtd_status`, `10_s11_falsification_protocol`, `11_pilot_results_methodology`, `13_l3_chirality_review`, `14_decision_gate`). Substrate-physics anchors (Chiral Figure of Merit factorization, Beltrami eigenvalue formula, helicity-per-unit-energy formula) are general physics — remain canonical in core via the surviving K4-TLM + CEM-methods-survey leaves below; the application-specific antenna design lives in private.

## Key Results

| Result | Expression | Source |
|---|---|---|
| MoM impedance equation | $[\mathbf{Z}][\mathbf{I}] = [\mathbf{V}]$ | cem-methods-survey |
| FEM resonance equation | $[\mathbf{S}]\{\mathbf{E}\} = k_0^2 [\mathbf{T}]\{\mathbf{E}\}$ | cem-methods-survey |
| CMA eigenvalue equation | $[\mathbf{X}]\mathbf{J}_n = \lambda_n [\mathbf{R}]\mathbf{J}_n$ | cem-methods-survey |
| K4-TLM scattering matrix | $S^{(0)}_{ij} = \frac{1}{2} - \delta_{ij}$; unitary to $2.2 \times 10^{-16}$ | k4-tlm-simulator |
| 3D antenna chiral coupling | $(7,11)$ torus knot: $\alpha \cdot pq/(p+q) = 3.12 \times 10^{-2}$, strongest chiral coupling | k4-tlm-simulator |

## Derivations and Detail

| Document | Contents |
|---|---|
| [CEM Methods Survey](cem-methods-survey.md) | MoM, FDTD, FEM, TLM, CMA, PO/GO — core equations and AVE lattice mappings; unified comparison table; solver recommendation hierarchy |
| [K4-TLM Simulator](k4-tlm-simulator.md) | K4 Diamond graph topology; 4-port scattering matrix; computational loop; Axiom 4 frame-dragging; validation results; 2D and 3D wire antenna resonance analysis. **Two-engine architecture (A-027): K4-TLM is the sub-saturation engine; bound-state regime requires Master Equation FDTD.** |
| [Open-Universe Boundaries](open-universe-boundaries.md) | Continuous Sponge PML; elimination of far-field wrap-around artifacts; 3D torus knot antenna simulation on $40^3$ lattice |

> **Note:** `summarybox` and `exercisebox` environments in the source chapter are not extracted as leaves in this KB.

---

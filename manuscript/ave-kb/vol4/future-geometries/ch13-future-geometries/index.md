[↑ Vol 4: Future Geometries](../index.md)

<!-- kb-frontmatter
kind: index
subtree-claims: [clm-hd9bee, clm-u462e4, clm-wzezvt]
-->

# Ch.13: Future Geometries — Hopf Coils and Phased Arrays

Electromagnetic knot engineering for the chiral $\mathcal{M}_A$ vacuum. The chapter develops Hopf coil topology (toroidal-poloidal fusion with nonzero magnetic helicity density $h = \mathbf{E} \cdot \mathbf{B} \neq 0$), establishes the Chiral Figure of Merit for antenna optimization, surveys six CEM solvers and maps each to the AVE lattice framework, and presents the K4-TLM Diamond lattice simulator.

## Key Results

| Result | Expression | Source |
|---|---|---|
| Magnetic helicity density | $h = \mathbf{E} \cdot \mathbf{B} \neq 0$ for Hopf coil topology | high-q-chiral-antenna |
| Chiral Figure of Merit | $\text{FoM} = Q_u \times \alpha \frac{pq}{p+q} \times \eta_{\mathcal{H}}$, where $\eta_{\mathcal{H}} = \text{SL}(p,q)/N_{cross}$ | high-q-chiral-antenna |
| Beltrami eigenvalue | $\lambda(p,q) = \sqrt{p^2/R^2 + q^2/r^2}$; helicity per unit energy $\mathcal{H}/U = 2\mu_0/\lambda$ | high-q-chiral-antenna |
| MoM impedance equation | $[\mathbf{Z}][\mathbf{I}] = [\mathbf{V}]$ | cem-methods-survey |
| FEM resonance equation | $[\mathbf{S}]\{\mathbf{E}\} = k_0^2 [\mathbf{T}]\{\mathbf{E}\}$ | cem-methods-survey |
| CMA eigenvalue equation | $[\mathbf{X}]\mathbf{J}_n = \lambda_n [\mathbf{R}]\mathbf{J}_n$ | cem-methods-survey |
| K4-TLM scattering matrix | $S^{(0)}_{ij} = \frac{1}{2} - \delta_{ij}$; unitary to $2.2 \times 10^{-16}$ | k4-tlm-simulator |
| 3D antenna chiral coupling | $(7,11)$ torus knot: $\alpha \cdot pq/(p+q) = 3.12 \times 10^{-2}$, strongest chiral coupling | k4-tlm-simulator |

## Derivations and Detail

| Document | Contents |
|---|---|
| [High-Q Chiral Antenna](high-q-chiral-antenna.md) | Hopf coil helicity; thruster topology comparison; RX cavity-coupled design ($Q_u \approx 680$ copper, $\sim 10^6$ YBCO); TX Beltrami helicity injector; matching network; sensitivity analysis |
| [CEM Methods Survey](cem-methods-survey.md) | MoM, FDTD, FEM, TLM, CMA, PO/GO — core equations and AVE lattice mappings; unified comparison table; solver recommendation hierarchy |
| [K4-TLM Simulator](k4-tlm-simulator.md) | K4 Diamond graph topology; 4-port scattering matrix; computational loop; Axiom 4 frame-dragging; validation results; 2D and 3D wire antenna resonance analysis |
| [Open-Universe Boundaries](open-universe-boundaries.md) | Continuous Sponge PML; elimination of far-field wrap-around artifacts; 3D torus knot antenna simulation on $40^3$ lattice |

> **Note:** `summarybox` and `exercisebox` environments in the source chapter are not extracted as leaves in this KB.

---

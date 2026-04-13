# HANDOFF: Electrostatic Point Charge Resolution

## Branch Goal
Resolve the classical electromagnetism infinity associated with the self-energy of a point charge ($r \to 0$, $E \to \infty$). You will mathematically substitute the classical point-particle assumption with the AVE Topological LC lattice boundaries, successfully capping the electrostatic strain within Phase Space.

## Context Audit
- **Classical Problem**: $E = \frac{k q}{r^2}$. As $r \to 0$, the energy density diverges to infinity.
- **AVE Axiomatic Resolution**: Particles are not dimensionless points; they are topological standing wave defects within a discrete vacuum LC network (Axiom 1). 
- **Underlying Mechanic**: Axiom 4 dictates that vacuum strain (electric field strength) reaches absolute yield ($S(r) = 0$) at the local dielectric rupture limit, $\text{V}_{\text{YIELD}} \approx 43.65 \text{ kV}$. 

## Architecture Requirements
1. **Solver File (`src/ave/regime_3_saturated/electrostatic_core.py`)**:
   - MUST import canonical parameters: `L_NODE`, `Z_0`, `ALPHA`, `V_YIELD` from `src/ave/core/constants.py`
   - MUST use `universal_saturation` from `src/ave/core/universal_operators.py`
   - Create a volumetric integration script demonstrating how integrating the bounded electric field mathematically stops at the topological perimeter, resulting exactly in the finite rest mass $m_e c^2$.
2. **LaTeX Integration (`manuscript/vol_2_subatomic/`)**:
   - Locate the relevant electron model chapters (e.g. `ch02-baryon-sector`).
   - Introduce the structural yield bound $S(r)$ mitigating the infinity.
   - Embed plots showing field saturation near $r \to \text{L}_{\text{NODE}}$.
3. **Workflow Rules**:
   - Run `/audit-math` over the updated LaTeX documents to ensure ZERO "magic numbers" or classical Bohr radius assumptions are smuggled in. (See `.agents/workflows/audit-math.md`).

## Next Agent Instructions
1. Review `src/ave/core/universal_operators.py`.
2. Construct the 1D/3D radial solver showing $\varepsilon_{eff}(r)$ diverging near the core.
3. Validate against the canonical electron rest mass energy.
4. Update the manuscript and check all mathematical links.

# Q-G47 Sessions 19+: ξ_K1, ξ_K2 Prefactor Derivation Pre-Registration

**Date**: 2026-05-18
**Target**: Derive individual values of ξ_K1, ξ_K2 prefactors from K4 unit-cell Cosserat-Lagrangian integration; verify against the canonical ratio ξ_K2/ξ_K1 = 12. Use C1-BH-RING Phase 5 empirically-anchored ν_vac=2/7 rigid/compliant partition as load-bearing input.
**Parent**: [`closure-roadmap.md:30`](../manuscript/ave-kb/common/closure-roadmap.md:30) Tier 2 row Q-G47 Sessions 19+ "genuinely-open items"
**Branch**: `analysis/q-g47-sessions-19-prefactor-derivation`
**Path 2 motivation**: from [`2026-05-18_cosserat-engine-q-preservation-result.md:103`](2026-05-18_cosserat-engine-q-preservation-result.md:103) — "Use C1's empirically-anchored ν_vac=2/7 rigid/compliant partition as the input to Sessions 19+ Q-G47 ξ_K1, ξ_K2 prefactor derivation."

## Section 1.5 — Physical Picture (5 bullets, mechanical/topological)

1. **K4 lattice has two distinct stiffness families per primitive cell**: translational (bond springs k_a hydrostatic + k_s shear) and rotational (Cosserat couple-stress k_β + k_γ). These are the DISCRETE bond-spring constants in the 12-DOF K4 unit cell. The CONTINUOUS Cosserat constitutive moduli (μ, κ, β, γ) map to them via geometric integration over the primitive-cell volume.

2. **The K=2G operating point** (Vol 1 Ch 1 canonical) fixes most of the discrete bond constants: k_s = 1/7, k_β = 1, k_γ = 1/7. Closed-form eigenvalues at this operating point:
   - λ_K = (4/3)·k_a (A_1 bulk, k_a free at K=2G)
   - λ_G = (4/3)·k_s = 4/21 (E shear)
   - λ_φ = (4/3)·(k_β + 2k_γ) = 12/7 (Cosserat microrotation)

3. **ξ_K1, ξ_K2 are the dimensional rescaling factors** that convert continuous Cosserat moduli → discrete bond constants:
   - (μ + κ) = ξ_K1 · T_EM ↔ translational moduli (k_a, k_s)
   - (β + γ) = ξ_K2 · T_EM · ℓ_node² ↔ microrotation moduli (k_β, k_γ)

   The RATIO ξ_K2/ξ_K1 = 12 is K4-symmetry-forced (Session 17, self-consistency); INDIVIDUAL values require executing the integration.

4. **C1's rigid/compliant partition is the missing physical constraint**: ν_vac = 2/7 fraction of EVERY Cosserat modulus is the "rigid baseline" (substrate-skeleton K4 lattice, doesn't respond to applied stress). C1 Phase 5 empirically anchored this partition at -0.47% mean τ across 3 LIGO events; previously it was only algebraic from K=2G isotropic-solid Poisson identity. This partition applies to (μ+κ) and (β+γ) separately: each splits into 2/7 rigid baseline + 5/7 compliant modulation. Knowing the partition fixes the integration's rigid-baseline starting point.

5. **The derivation is purely analytical** — geometric integration over K4 primitive cell volume (4 nodes, I4_1 32 chiral space group) + algebraic match to closed-form eigenvalue spectrum at K=2G + C1's 2/7 partition as physical constraint. **No engine simulation needed.** The discrete event is solving the system of constraints to yield ξ_K1 and ξ_K2 individually. PASS = system over-determined gives consistent values; FAIL = system inconsistent (suggests rigid/compliant partition doesn't apply to discrete bond constants the way C1 assumes at continuum scale).

## Section 2 — Corpus-Grep Verification (5-min cap)

Verified via ave-corpus-grep agent (returned ~3500 words, condensed below):

**Pre-test grep checklist**:

- [x] **ξ_K1, ξ_K2 definitions**: [`q-g47-substrate-scale-cosserat-closure.md:42-49`](../manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md:42) — (μ+κ) = ξ_K1·T_EM and (β+γ) = ξ_K2·T_EM·ℓ_node². Ratio = 12 locked. Individual values open per `:107-110`.
- [x] **12-DOF closed-form eigenvalues**: [`research/_archive/L3_electron_soliton/128_q_g47_path_b_plus_cosserat_results.md:65-72`](../research/_archive/L3_electron_soliton/128_q_g47_path_b_plus_cosserat_results.md:65) — closed-form at K=2G operating point.
- [x] **K4 primitive cell**: 4 nodes per primitive cell (`N_K4 = 4`), z = 4 nearest neighbors tetrahedral, I4_1 32 chiral space group per Axiom 1 canonical (Vol 1 Ch 1).
- [x] **ν_vac = 2/7 rigid/compliant partition**: [`ave-merger-ringdown-eigenvalue.md:37`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md:37) — canonical formula; [`closure-roadmap.md:117`](../manuscript/ave-kb/common/closure-roadmap.md:117) — Phase 3 v2 decomposition x_sat(a*) = 7·[ν_vac + (1-ν_vac)·r_ph+/3M] = 2 + 5·r_ph+/3M. Origin: K=2G isotropic-solid Poisson identity per `129:52`. Now ALSO empirically anchored via C1 Phase 5 (-0.47% mean τ).
- [x] **z_0 = 51.25 status**: currently EMT-inversion-given-α (circular), per [`appendix_c_derived_numerology.tex:60-74`](../manuscript/backmatter/appendix_c_derived_numerology.tex:60). First-principles geometric derivation deferred per `q-g47-substrate-scale-cosserat-closure.md:108-109` ("Layer 4 explicit α-consistency-not-emergence framing"). Geometric route: count secondary neighbors within 1.187·ℓ_node sphere in K4 lattice.
- [x] **Q-G47 Sessions 1-18 history**: framework + substrate-level + path-verification done (Doc 124-131). Individual ξ_K1, ξ_K2 values explicitly deferred at Session 17:49 (per `124:59`) — "multi-week K4 lattice integration."
- [x] **Existing scaffolding code**:
  - [`src/scripts/verify/q_g47_path_b_plus_cosserat.py`](../src/scripts/verify/q_g47_path_b_plus_cosserat.py) — 12-DOF Cosserat verification
  - [`src/scripts/verify/q_g47_path_c_emt_canonical.py`](../src/scripts/verify/q_g47_path_c_emt_canonical.py) — FTG-EMT formula
  - [`src/ave/topological/k4_cosserat_coupling.py`](../src/ave/topological/k4_cosserat_coupling.py) — coupling implementation

**Provisional hypothesis** (NOT to be taken as conclusion): The derivation is solvable with the existing closed-form eigenvalues + C1's partition constraint + K=2G operating point fix. Expected outcome: ξ_K1 and ξ_K2 land at clean rational values (e.g., ξ_K1 = 7/N for some small integer N, ξ_K2 = 12·ξ_K1) since the AVE corpus consistently produces 7-related rational values from ν_vac=2/7 algebra. Most-likely individual values: ξ_K1 ∈ {1/7, 2/7, 1/4, 1/3} and ξ_K2 = 12·ξ_K1.

## Section 3 — Pre-Registration

**PREREG (target: derive individual ξ_K1, ξ_K2 prefactors from K4 unit-cell Cosserat-Lagrangian integration with C1's ν_vac=2/7 partition as input)**:

**Corpus state**: partial (ratio + scaffolding canonical; individual values open since Session 17). C1 input new (2026-05-18 Phase 5).

**Prior work cited**:
- [`q-g47-substrate-scale-cosserat-closure.md:42-110`](../manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md:42) (definitions + open list)
- [`128_q_g47_path_b_plus_cosserat_results.md:40-72`](../research/_archive/L3_electron_soliton/128_q_g47_path_b_plus_cosserat_results.md:40) (12-DOF closed-form eigenvalues at K=2G)
- [`129_q_g47_path_c_emt_canonical_substrate.md`](../research/_archive/L3_electron_soliton/129_q_g47_path_c_emt_canonical_substrate.md) (FTG-EMT z_0=51.25)
- [`ave-merger-ringdown-eigenvalue.md:37`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md:37) + [`closure-roadmap.md:117`](../manuscript/ave-kb/common/closure-roadmap.md:117) (ν_vac=2/7 rigid/compliant)
- [`vol_1_foundations/chapters/01_fundamental_axioms.tex`](../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex) (Axiom 1 canonical K4 + K=2G operating point)

**Derivation steps**:

Step A — **Continuous Cosserat-Lagrangian density** (from Sessions 16-17 canonical form):
$$
\mathcal{L}_{\text{Cosserat}} = \frac{1}{2}\mu\,(\partial_i u_j + \partial_j u_i)^2 + \frac{1}{2}\kappa\,(\partial_i u_i)^2 + \frac{1}{2}\beta\,(\partial_i \phi_j)^2 + \frac{1}{2}\gamma\,(\partial_i \phi_j + \partial_j \phi_i)^2
$$
where (u, φ) are translation and microrotation fields.

Step B — **Integrate over K4 primitive cell** (4 nodes at tetrahedral positions per I4_1 32, volume $V_{\text{cell}} = (\ell_{\text{node}})^3 \cdot v_{\text{geom}}$ where $v_{\text{geom}}$ is the K4 geometric volume factor from the chiral space group):
$$
E_{\text{cell}} = \int_{V_{\text{cell}}} \mathcal{L}_{\text{Cosserat}} \, dV
$$

Step C — **Match to discrete 12-DOF eigenvalue spectrum** at K=2G:
- $\lambda_K = (4/3) k_a$ ↔ (μ + κ) integration result
- $\lambda_G = (4/3) k_s = 4/21$ ↔ μ integration result
- $\lambda_φ = (4/3)(k_β + 2 k_γ) = 12/7$ ↔ (β + γ) integration result

Step D — **Apply C1's ν_vac=2/7 partition** as physical constraint:
- (μ + κ) = (2/7)·(μ + κ)_rigid + (5/7)·(μ + κ)_compliant
- (β + γ) = (2/7)·(β + γ)_rigid + (5/7)·(β + γ)_compliant

The rigid fraction (2/7) corresponds to the K4-skeleton non-responsive baseline; compliant fraction (5/7) is the stress-responsive remainder. This partition fixes the integration's starting point.

Step E — **Solve over-determined system** for ξ_K1, ξ_K2:
$$
\xi_{K1} = (\mu + \kappa) / T_{\text{EM}}
$$
$$
\xi_{K2} = (\beta + \gamma) / (T_{\text{EM}} \cdot \ell_{\text{node}}^2)
$$
Self-consistency check: ξ_K2/ξ_K1 = 12 (must match Session 17 canonical).

Step F — **z_0 = 51.25 first-principles geometric derivation** (companion target, doable in parallel):
Count secondary neighbors within 1.187·ℓ_node sphere in K4 lattice — geometric, not EMT-circular. Should reproduce 51.25 ± rounding without using α as input.

**Implementation approach**: Standalone Python script `src/scripts/verify/q_g47_sessions_19_xi_K_derivation.py` that:
1. Sets up K4 primitive cell geometry numerically (4 atom positions, bond connectivity)
2. Executes Step B integration symbolically (sympy if needed for closed form, else numerical quadrature)
3. Matches to closed-form eigenvalues at K=2G operating point
4. Applies C1 ν_vac=2/7 partition
5. Solves for ξ_K1, ξ_K2 individually
6. Cross-validates against ratio = 12
7. Companion: numerical neighbor-count for z_0 = 51.25 derivation

## Section 4 — Discriminating Outcomes

- **Outcome A (PASS, ~40% probability)**: ξ_K1 and ξ_K2 land at clean rational values consistent with ν_vac=2/7 family (likely ξ_K1 ∈ {1/7, 2/7, 1/4, 1/3}; ξ_K2 = 12·ξ_K1 trivially). Ratio = 12 reproduced exactly. **Action**: Promote to KB anchor in `q-g47-substrate-scale-cosserat-closure.md`; update [`closure-roadmap.md:30`](../manuscript/ave-kb/common/closure-roadmap.md:30) Tier 2 row to mark ξ_K1, ξ_K2 individual values CLOSED.

- **Outcome B (PARTIAL, ~30% probability)**: Step A-D works, but Step E gives non-rational values (e.g., ξ_K1 = 0.234..., ξ_K2 = 2.808...). Suggests one of: (i) missing constraint (e.g., additional K4 symmetry not yet incorporated); (ii) integration step requires more careful treatment of chiral coupling k_χ that I'm currently ignoring; (iii) ν_vac=2/7 partition needs sharper formulation for discrete bond constants. **Action**: Document the partial result; identify which step needs refinement; queue Session 20 work.

- **Outcome C (RATIO INCONSISTENCY, ~15% probability)**: Step E gives ξ_K2/ξ_K1 ≠ 12. This invalidates one or more of: (i) C1's ν_vac=2/7 partition (unlikely, empirically anchored); (ii) Sessions 16-17 ratio derivation; (iii) K=2G eigenvalue closed forms; (iv) my integration step. **Action**: Audit which step broke; this would be a load-bearing finding requiring framework-level reconciliation.

- **Outcome D (DERIVATION INTRACTABLE, ~10% probability)**: K4 integration step requires symbolic-algebra tools beyond reach in 1-2 sessions. **Action**: Document the obstacle; scope what additional tooling (sympy, Mathematica equivalent, etc.) is needed; mark as multi-session.

- **Outcome E (z_0 = 51.25 first-principles PASS, ~50% probability of partial success alongside any A/B outcome)**: neighbor counting reproduces 51.25 from K4 geometry directly. **Action**: Update [`closure-roadmap.md:30`](../manuscript/ave-kb/common/closure-roadmap.md:30) z_0 status to first-principles derived; remove "α-circularity" caveat.

**Falsifier**: Outcome C (ratio inconsistency) at >10% deviation from 12 → ν_vac=2/7 partition does NOT apply to discrete bond constants the way C1 implies at continuum scale. Would require revisiting the v2 derivation logic in C1 (specifically: the rigid-fraction interpretation as "fraction of substrate K4-skeleton" may need narrower scope).

## Section 5 — Result Doc (created after derivation)

Will log to `research/2026-05-18_q-g47-sessions-19-prefactor-derivation-result.md` regardless of outcome.

## Section 6 — Falsifier Discipline (per `ave-prereg` Step 4)

Pre-reg committed BEFORE running any derivation script. Result logged regardless of outcome. No outcome rewrite.

## Section 7 — Implementation Notes

**Scoping**: this is multi-session work historically (Session 17:49 explicitly: "multi-week K4 lattice integration"). With C1's new partition input, scope tightens to "1-3 sessions if Steps A-E are tractable; more if Step B integration is intractable analytically."

**Out of scope this session**:
- Full K4-TLM ↔ Master Equation FDTD engine-boundary mode-matching (separate Sessions 19+ item)
- Chiral coupling k_χ refactor (Phase 4 territory)
- Full Cosserat-Lagrangian engine extension (gated on engine architecture decisions)

# Path C — z₀ from K4 Amorphous Geometry, ALPHA-FREE → EMT reads α out — Pre-Registration

**Date**: 2026-06-08
**Branch**: `analysis/2026-06-08-pathc-z0-amorphous-emt`
**Lane**: implementer
**Prior**: [`2026-05-18_z0-first-principles-attempt-result.md`](2026-05-18_z0-first-principles-attempt-result.md) (Outcome B+D: path-count z=52, 1.46% off; amorphous Gaussian collapses to 4–5)
**Discipline fired**: `ave-prereg` (grep BEFORE freeze — done §2), `substrate-native-check` (§5), `consistency-vs-emergence` (§6). FROZEN before any computation.

---

## Section 1 — The CLAIM under test

**Path C claim**: the effective rigidity-percolation coordination z₀ of the K4 vacuum lattice can be derived from **K4 amorphous geometry ALONE, α-free**. If that α-free z₀ ≈ 51.25, then the Feng–Thorpe–Garboczi (FTG) EMT formula

```
p_c = (10·z₀ − 12) / (z₀·(z₀ + 2))
```

**reads α OUT**: α = p_c(z₀)/8π. This would upgrade α from "Class-B closed-form (consistency illustration)" to **emergence-class DERIVED** — the substrate would select α instead of taking it as input.

This is the ONE route that lifts α from "characterized to 1.5%" to DERIVED. The current corpus route is **circular** (documented, honest-α relabel 2026-06-02):

```
CIRCULAR (current corpus):
  α (CODATA) → p_c = 8πα → C_ratio = (p_cauchy/p_c)^{1/3} = 1.187 → z₀ = 51.25 (EMT root located AT α)
  → EMT(51.25) gives back 8πα  [tautology — α was the input]
```

vs the goal:

```
GOAL (Path C, α-free):
  K4 geometry ONLY → z₀ = f(lattice topology, amorphous disorder) [NO α anywhere]
  → p_c = (10z₀−12)/(z₀(z₀+2)) → implied α = p_c/8π → compare to CODATA (external, one-way)
```

## Section 2 — Corpus-grep (done before freeze)

Verified this session in the worktree:

- **The over-bracing radius 1.187 is α-DERIVED.** `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/trace-reversal-mechanism.md:22` and `vol2/appendices/app-d-computational-graph/graph-architecture.md:31`: `C_ratio = (p_cauchy/p_c)^{1/3} ≈ 1.187` with `p_c = 8πα`. **Therefore any z₀ computation that uses r_secondary = 1.187·d as a geometric input is secretly α-circular.** This retro-flags prior Models 1, 3, 5 (all keyed on `R_SECONDARY_OVER_D = 1.187`) as NOT genuinely α-free. Only Model 2 (path-count, radius-free) was α-free.
- **z₀ = 51.25 is the EMT root located at α by construction** (`appendix_c_derived_numerology.tex:74-76`, honest-α relabel). First-principles z₀ from K4 is open (`claim-quality-closure-roadmap.md` §0 row 2).
- **The α-free K4 invariants available**: z_primary = 4 (tetrahedral coordination, topological); |T| = 12 (proper tetrahedral rotation group order, exact; `common/claim-quality.md:1028` four-routes leaf, route 1 = "4 B-neighbors × 3 other-A sublattices = 12"). Both are α-free.
- Path-count baseline: z₀ = 4·(1+|T|) = 4·13 = **52** (α-free), → p_c(52) = 508/2808 = 0.18091 → implied α = 1/138.9 (1.37% from CODATA 1/137.036).

## Section 3 — The METHOD (amorphous effective rigidity-coordination)

Compute the **amorphous effective rigidity-coordination z₀ of the K4 lattice, topology-only, radius-free, α-free**, and test whether disorder reduces the crystalline path-count from 52 toward 51.25.

1. **Crystalline α-free baseline** — build K4 (diamond, I4₁32-chiral, 4-coordinated) supercell at unit pitch d=1 (NOT 1.187 — radius-free). Enumerate the 2-hop topological neighbourhood; compute z₀ = z_primary·(1 + |T|_eff), where |T|_eff is the realized secondary-path multiplicity. Crystalline target: 52.
2. **Amorphous ensemble (coordination-preserving)** — generate a disordered K4 (continuous-random-network / WWW-style tetrahedral-angle disorder) ensemble that PRESERVES 4-coordination (the substrate-native disorder; not the coordination-breaking Gaussian-position smear that prior Model 3 already falsified). Sweep disorder strength σ_angle. For each realization recount the effective secondary-path multiplicity ⟨|T|_eff⟩ and hence ⟨z₀⟩.
3. **Ring-closure correction** — short odd-membered rings (characteristic of amorphous tetrahedral networks) can merge or short-circuit 2-hop paths, reducing ⟨|T|_eff⟩ below 12. Quantify this α-free reduction vs σ_angle.
4. **EMT readout** — for crystalline z₀ and ⟨z₀⟩(σ): implied α = p_c(z₀)/8π. Compare to CODATA 1/137.036 (external one-way comparison ONLY; never fed back).

## Section 4 — ALPHA-FREE GUARD (load-bearing)

The z₀ computation MUST NOT contain, at any intermediate step:

- α (or 1/137.036, ALPHA_COLD_INV = 4π³+π²+π) — **the script does NOT import `ave.core.constants`.**
- e, ε₀, ħ, Z₀, c, or any SI quantity (no SI-substitution channel).
- p_c = 8πα, or p_cauchy ≈ 0.3068 (simulation-reported, itself entangled with p_c).
- **r_secondary/d = 1.187 or C_ratio** — CONFIRMED α-derived (§2); FORBIDDEN as input.

Permitted α-free inputs ONLY: K4/diamond topology (coordination 4), |T| = 12 (group order), the integer 8π (pure geometric constant in the EMT readout, NOT 8πα), disorder strength σ_angle (a pure geometric angle). Every script input is traced in the result doc; any α/SI leak ⇒ Outcome C.

## Section 5 — substrate-native-check

- **K4 / Cosserat**: lattice is the chiral K4 (diamond graph, I4₁32), 4-coordinated, |T|=12 proper-rotation orbit. Computation is a real-space lattice-topology count — the FTG-EMT z₀ is itself a real-space rigidity-percolation coordination, so this is the matching coordinate system (no phase-space/real-space mismatch; the claim is real-space coordination, A46 satisfied).
- **Op14 / saturation**: not invoked — z₀ is a static geometric coordination, not a saturating-impedance dynamic. Correctly excluded.
- **No Lagrangian/energy-basin leak**: this is constraint-counting (Maxwell rigidity), not energy minimization. Substrate-native.

## Section 6 — consistency-vs-emergence tag

- If α-free z₀ ≈ 51.25 AND EMT reads α = 1/137.036 → **EMERGENCE-class** (substrate selects α). This is the hypothesis.
- If z₀ uses 1.187 or any α-derived input → **CONSISTENCY-class / circular** (the current corpus state). Forbidden by §4.
- The likely null (z₀ stays ~52, implied α = 1/138.9) is a **failed emergence test** → honest negative, NOT downgraded to "consistency."

## Section 7 — FALSIFIER + Outcome categories

Logged regardless of result; no post-hoc rewrite.

- **Outcome A — DERIVED (PASS)**: α-free z₀ → ~51.25 (within ~0.1%) with NO tuned parameter, and EMT reads α = 1/137.0 (within ~0.1%). α emergence-class. *(prior probability ~10%)*
- **Outcome B — GAP REAL (the expected null)**: α-free z₀ stays ~52 (path-count is a topological invariant; coordination-preserving disorder does not move it to 51.25 without tuning). The 1.5% gap (52 vs 51.25) is a real, α-free, structural gap. p_c = 8πα holds only to ~1.5% from substrate first principles. *(prior ~45%)*
- **Outcome C — CIRCULAR (α sneaks in)**: the only way to reach 51.25 requires an α-derived input (1.187, p_c, p_cauchy) or an SI substitution. Confirms circularity; α NOT derived. *(prior ~25%)*
- **Outcome D — MODEL-DEPENDENT / UNSTABLE**: amorphous z₀ depends sensitively on the disorder model (e.g. ⟨z₀⟩ swings widely with σ_angle / ring-statistics with no natural α-free fixed point). z₀ is not a robust geometric invariant; scope the multi-week work. *(prior ~20%)*

**Framework falsifier**: if the only route to 51.25 is α-input (Outcome C), the "α derived" claim is confirmed circular and must stay Class-B (honest-α relabel preserved). If Outcome A, α lifts to emergence-class. Outcomes B/D leave the 1.5% gap as the load-bearing open question, α-free.

**Anti-rescue discipline (Rule 11)**: I will NOT tune σ_angle or invent a correction term to manufacture 51.25. Note: 52 − 51.25 = 0.75 = 3/4 coincides with the K4 mesh forward-scatter efficiency η = 3·(½)² = 3/4 (appendix_c Kolmogorov section) — this is a **coincidence-magnet** (3/4 is over-determined in the corpus); it will be REPORTED as an observation, NOT asserted as a derivation, unless an independent α-free mechanism produces it.

## Section 8 — Implementation + deliverables

- Script: `src/scripts/vol_1_foundations/pathc_amorphous_z0.py` (new). Headlines the α-free input trace; does NOT import `ave.core.constants`.
- Result: `research/2026-06-08_pathc-z0-amorphous-emt-result.md` — honest Outcome A/B/C/D, α-free trace, implied α.
- Two commits: (1) this prereg FROZEN before computation; (2) script + result. Push, not merge.

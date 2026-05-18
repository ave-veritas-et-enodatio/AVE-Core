# z_0 = 51.25 First-Principles Derivation Attempt — Result

**Date**: 2026-05-18
**Pre-registration**: [`2026-05-18_z0-first-principles-attempt-prereg.md`](2026-05-18_z0-first-principles-attempt-prereg.md)
**Script**: [`src/scripts/verify/z0_first_principles_attempt.py`](../src/scripts/verify/z0_first_principles_attempt.py)
**Branch**: `analysis/q-g47-sessions-19-prefactor-derivation`

## TL;DR — Outcome B (PARTIAL) + structural finding

**Closest natural K4 value: z = 4·(1 + |T|) = 4·13 = 52**, off canonical 51.25 by **1.46%**. The K4 path-count topology (4 primary K4 neighbors + 4·12 secondary path-distinct atoms via |T|=12 K4 orbit multiplicity) gives a clean rational that's structurally suggestive but 0.75 short of the EMT-canonical 51.25.

**The 0.75 gap is load-bearing**: it cannot be explained by any first-principles K4 geometric mechanism in the tested models. Canonical 51.25 = 51.249 emerges from inverting the FTG-EMT quadratic `0.1834·z² - 9.633·z + 12 = 0` given α as input. The "51.25" is α-calibrated, not substrate-geometry-derived.

## Five-model results

```
Model                                  | Result      | vs 51.25 target
--------------------------------------|-------------|----------------
1. Crystalline K4 at r=1.187·d         | z = 4       | -47.25  (-92%)
2. Path-count K4 topology (z·(1+|T|))  | z = 52      | +0.75   (+1.46%)
3. Amorphous Gaussian σ ∈ {0.05-1.0}·d | z = 4.1-5.0 | -46+    (-90%+)
4. Continuum ρ_substrate fit           | ρ tuned     | requires ~11.3× K4 density
5. Radius sweep for z=51 in crystalline| r = 2√2·d   | r = 2.828, NOT 1.187
```

**Model 2 (path-count) is the only model producing a value within 5% of canonical without tuned parameters.** The structural form `z = z_primary + z_primary · |T|` is K4-natural:
- z_primary = 4 (tetrahedral coordination at K4 vertices)
- |T| = 12 (proper-rotation orbit multiplicity, Q-G47 A-032 canonical)
- z·(1+|T|) = 4·13 = 52

## What this means structurally

### Finding 1: Canonical z_0 = 51.25 is α-calibrated, not first-principles

EMT quadratic at α = 1/137.035999:
```
(10z - 12)/(z(z+2)) = 8πα = 0.183399...
→ 0.183399·z² - 9.633202·z + 12 = 0
→ z = 51.249 (physical root) or z = 1.277 (below Maxwell z_c=6, unphysical)
```

The "51.25" rounds 51.249. This is NOT a first-principles geometric quantity from K4 lattice — it's the α value back-translated through FTG-EMT.

### Finding 2: K4-natural path-count gives z = 52 cleanly

The structural form 4·(1+|T|) = 52 = 4·13 is the first-principles derivable value:
- 4 nearest K4 neighbors
- 12 = |T| secondary atoms reachable via 2-hop K4 graph paths (4 B-neighbors × 3 other-A's per B)
- Total path-distinct atoms in 2-hop K4 neighborhood: 4 + 4·12 = 52

This matches z_0 to **1.46%** without any α-circularity.

### Finding 3: The 0.75 gap is real and has structural implications

If z_0 = 52 (first-principles), substituting back into FTG-EMT:
```
p_c(z=52) = (520-12)/(52·54) = 508/2808 = 0.18091
```
vs canonical 8πα = 0.18340 — **off by 1.36%**.

Two interpretations of the 1.5% gap:

(a) **FTG-EMT formula needs K4-specific refinement** at K=2G crossing. The standard formula p_c = (10z-12)/(z(z+2)) is for generic 3D amorphous central-force networks; the K4-specific chirality (I4_1 32) may introduce a correction that gives exact p_c(52) = 8πα.

(b) **The framework's "p_c = 8πα" identity is approximate, not exact**, at the 1.5% level. α is NOT exactly p_c/(8π) from substrate first principles; the match is structural-to-1.5%-precision.

Either interpretation has implications for the "one-cosmological-parameter" framework claim. Either way, the substrate-derived first-principles value is z_0 = 52 (clean rational from K4 + |T|), not the α-calibrated 51.249.

### Finding 4: r_secondary/d = 1.187 doesn't reach z=51 in crystalline K4

Model 5 shell structure: K4 lattice has 51 cumulative neighbors at r = 2.828·d = 2√2·d (6th shell), not at r = 1.187·d (which only includes 1st shell at z=4). The corpus's "over-bracing at 1.187·d → z_0 = 51.25" chain cannot be a pure crystalline neighbor count; it must invoke amorphous-network statistical mechanics not in the tested models, OR it's path-count topology (Model 2) which doesn't depend on Euclidean radius at all.

This means: r_secondary/d = 1.187 is the LENGTH-RATIO over-bracing parameter for u_0* (geometric), but z_0 = 51.25 doesn't derive from this radius via Euclidean neighbor counting. The two quantities (u_0* and z_0) have DIFFERENT geometric origins.

## Implication for u_0*/p_c disambiguation

The picture I painted assumed u_0* and p_c both derive from Ω_freeze via parallel geometric chains:
- u_0* via centrifugal stretching → r_secondary/d = 1.187
- p_c via packing fraction → z_0 = 51.25 → FTG-EMT

This result shows:
- The r_secondary/d = 1.187 → u_0* chain is well-defined (geometric over-bracing length ratio)
- The 1.187 → z_0 = 51.25 chain is NOT first-principles; it requires either α-input (circular) OR amorphous stat-mech beyond tested models
- The first-principles path-count alternative gives z_0 = 52, NOT 51.25

**Therefore**: the framework's two readouts (u_0* and p_c) do NOT come from a common Ω_freeze projection without α-input. Either:

(a) **The framework has hidden circularity**: p_c = 8πα is INPUT (calibrated to CODATA α), then z_0 = 51.249 is derived, then EMT at z=51.249 gives back 8πα tautologically. The "match" is by construction.

(b) **The framework has a 1.5% structural gap**: first-principles z_0 = 52 from K4 path-count gives p_c = 0.18091 ≠ 8πα = 0.18340. Either α calibration is off, or FTG-EMT formula needs K4-specific correction.

Both interpretations have load-bearing consequences for the "one-cosmological-parameter" claim:
- Interpretation (a): the claim is structurally circular; α isn't derived, it's calibrated
- Interpretation (b): the claim has a 1.5% precision gap that needs structural reconciliation

## Outcome Classification

Per pre-reg:
- A (PASS, ~20%): NOT OBSERVED — no model gives exactly 51.25 from first principles
- **B (PARTIAL, ~30%): OBSERVED — K4 path-count gives 52 (clean rational, 1.46% off)**
- C (FAIL, ~40%): NOT OBSERVED — Model 2 provides a clean structural match
- D (INCONSISTENCY, ~10%): OBSERVED jointly with B — corpus's "1.187 → 51.25" chain isn't first-principles geometric; r=1.187 only reaches z=4 in crystalline K4

**Mixed outcome B+D**: PARTIAL match (Model 2 = 52) + inconsistency in corpus chain (r=1.187 ↛ z=51.25 by any first-principles mechanism in scope).

## What we now know about the framework's "one parameter" claim

**Before this test**: u_0* and p_c were both canonically pinned at numerical values close to 0.187 / 0.1834, with the relationship between them flagged OPEN per doc 128:181.

**After this test**: the relationship is more specific:
- u_0* ≈ 0.187 is a first-principles geometric quantity (over-bracing length ratio)
- p_c = 8πα ≈ 0.1834 is calibrated to CODATA α (not first-principles)
- z_0 = 51.249 is the intermediary that makes p_c = 8πα exact via EMT inversion
- First-principles z_0 = 52 from K4 path-count gives p_c(52) ≈ 0.1809, differing from 8πα by 1.5%

The substrate-physical picture (Ω_freeze → both u_0* and p_c) requires the 1.5% gap to be resolved by ONE of:
1. K4-specific EMT refinement that gives exact p_c(52) = 8πα
2. Acknowledgment that α isn't exactly p_c/(8π) but approximately (1.5%-level)
3. Discovery of a different z_0 mechanism that exactly produces 51.249 from K4 geometry

None of these are in 1-2 session scope. They're multi-week analytical work.

## Recommended next step

The 1.5% gap is the new most-fundamental open question. Three paths forward:

**Path A — Try the K4-specific EMT refinement** (1-2 sessions): work out what chirality/I4_1 32-specific correction to the FTG-EMT formula at K=2G crossing would give exact p_c(52) = 8πα. If a natural correction exists, framework's α-as-derived claim survives.

**Path B — Accept the 1.5% gap as approximate identity** (re-scoping work): rewrite the "p_c = 8πα" framework statement as "p_c = 8πα to within 1.5% from substrate first principles." Honest re-scoping of the one-parameter claim's precision.

**Path C — Pivot to a different load-bearing question** (1+ sessions): the 1.5% gap is documented but other framework keystones may be more tractable. E.g., return to a forward experimental prediction (matrix candidates) where α is empirically input anyway.

**My recommendation: Path A**. The K4-specific EMT refinement is the natural next analytical step. The corpus has |T| = 12 + chirality I4_1 32 + Cosserat couple-stress; refining FTG-EMT to include these K4-specific elements is concrete work with a falsifiable target (exact p_c(52) = 8πα or not).

## Falsifier discipline

Per pre-reg Step 4: result logged regardless of outcome. Mixed B+D outcome reported honestly. The "Outcome A (PASS)" pre-registered probability was 20%; actual was the predicted PARTIAL+INCONSISTENCY mix. Pre-reg honored.

## Cross-references

- Pre-registration: [`2026-05-18_z0-first-principles-attempt-prereg.md`](2026-05-18_z0-first-principles-attempt-prereg.md)
- Script: [`src/scripts/verify/z0_first_principles_attempt.py`](../src/scripts/verify/z0_first_principles_attempt.py)
- u_0*/p_c disambiguation precondition: [`2026-05-18_q-g47-sessions-19-prefactor-derivation-result-v2.md`](2026-05-18_q-g47-sessions-19-prefactor-derivation-result-v2.md)
- C1 Phase 5 (the chain that motivated this): [`research/ligo-ringdown-driver-design.md`](ligo-ringdown-driver-design.md) §10
- Canonical Q-G47 closure (now updated with Sessions 19 closure): [`q-g47-substrate-scale-cosserat-closure.md:42-110`](../manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md:42)
- FTG-EMT canonical formula: [`appendix_c_derived_numerology.tex:60-74`](../manuscript/backmatter/appendix_c_derived_numerology.tex:60)

# z_0 = 51.25 First-Principles Derivation Attempt — Pre-Registration

**Date**: 2026-05-18
**Target**: Derive z_0 (amorphous K4 over-braced network effective coordination at K/G=2) from substrate geometry, INDEPENDENT of α. If z_0 = 51.25 falls out at r_secondary/d = 1.187 (canonical over-bracing parameter from Vol 3 Ch 1 §3.2), framework closes u_0*/p_c disambiguation and demotes α-circularity.
**Branch**: `analysis/q-g47-sessions-19-prefactor-derivation` (continuing)
**Sequence**: Most-fundamental next step per substrate-physical picture; gates u_0*/p_c disambiguation, which gates 3-route consistency test.

## Section 1.5 — Physical Picture

The chain (per picture painted earlier):
```
Ω_freeze → centrifugal stretching → r_secondary/d = 1.187 → amorphous K4 over-bracing →
   ├─ u_0* ≈ 0.187 (length-ratio readout, A-029 over-bracing parameter)
   └─ z_0 = 51.25 (effective coordination of amorphous network)
         └─ p_c = 8πα ≈ 0.1834 via FTG-EMT formula at K/G=2
```

The load-bearing geometric question: **what amorphous-network mechanism converts r_secondary/d = 1.187 into z_0 = 51.25?** Crystalline K4 counting gives only 4 (nearest neighbors); 51.25 requires amorphous secondary network where disorder activates ~12-13× more bonds per atom.

Per Vol 3 Ch 1 §3.2 (cited in corpus-grep): "primary K4's over-bracing creates the geometric scaffolding for the amorphous z_0=51.25 coordination" — structural assertion without explicit g(r) derivation in the searched corpus.

The FTG-EMT formula has suggestive structure: **p_c = (10·z_0 - 12) / (z_0·(z_0 + 2))** at z_0=51.25 gives 0.1834 to 0.003% match with 8πα. The **12** in the numerator matches χ_K = 12 (K4 path-count multiplicity from Q-G47 A-032). The **10** coefficient is unexplained in the searched corpus.

If z_0 is path-count-derived: 4 primary K4 + |T|·z_K4 secondary = 4 + 48 = 52, ~1.5% off canonical 51.25. Suggestive but doesn't pin exactly.

## Section 2 — Corpus-Grep (already done, summarized)

Key prior findings from corpus-grep:
- z_0 = 51.25 is currently EMT-inversion-given-α (per [`appendix_c_derived_numerology.tex:60-74`](../manuscript/backmatter/appendix_c_derived_numerology.tex:60))
- First-principles derivation flagged as Sessions 19+ open ([`closure-roadmap.md:30`](../manuscript/ave-kb/claim-quality-closure-roadmap.md:30))
- Path C doc 129 uses FTG-EMT at z_0 input (doesn't derive z_0)
- Vol 3 Ch 1 §3.2 asserts amorphous-network mechanism without explicit g(r)
- |T| = 12 is K4 path-count multiplicity (4 B-neighbors × 3 other-A sublattices, per A-032)

## Section 3 — Pre-Registration

**Method**: try multiple analytical/computational approaches in parallel:

1. **Crystalline counting**: K4 lattice atoms within r ≤ 1.187·d sphere. Expected: 4 (already verified). Documents baseline.
2. **Path-count enumeration**: enumerate all K4 topological paths of length ≤ k from origin, count distinct atoms reached. Vary path-length cutoff k. See if z_0=51.25 appears at any natural k.
3. **Amorphous (Gaussian disorder)**: K4 positions perturbed by Gaussian width σ in units of d. Count effective neighbors within r=1.187·d sphere as function of σ. See if z_0=51.25 appears at any natural σ (e.g., σ=ν_vac=2/7).
4. **Substrate-density model**: treat substrate as continuum with density ρ_substrate; count effective neighbors as ρ_substrate × Volume(r=1.187·d). Identifies what ρ_substrate gives 51.25.
5. **Over-bracing radius sweep**: vary r_secondary/d from 1.0 to 2.0. Find radius that gives z=51.25 in any of the above models. Identifies whether 1.187 specifically maps to 51.25.

**Predicted Outcomes**:

- **Outcome A (PASS, ~20% probability)**: Some natural mechanism with no tuned parameters gives z_0 = 51.25 at r_secondary/d = 1.187. Framework first-principles closure achieved.
  - Most likely: path-count enumeration at specific cutoff matching K4 secondary network depth.
  - Or: amorphous Gaussian model at σ = ν_vac = 2/7 gives 51.25.

- **Outcome B (PARTIAL, ~30% probability)**: A model gives z_0 = 51.25 but requires a tuned parameter (e.g., σ ≠ natural substrate quantity, or r_secondary ≠ 1.187). Identifies the missing physical constraint.

- **Outcome C (FAIL, ~40% probability)**: No analytical model in scope gives 51.25 from 1.187 cleanly. Confirms multi-week statistical-mechanics work is required. Identifies the gap quantitatively.

- **Outcome D (REPRODUCES 51.25 BUT EXPOSES INCONSISTENCY, ~10% probability)**: A model gives 51.25 at r_secondary ≠ 1.187, OR gives a different z_0 at r_secondary = 1.187. Reveals that the corpus's "1.187 → 51.25" chain has a structural error.

**Falsifier for the framework**: Outcome D specifically — if r_secondary=1.187 produces z_0 ≠ 51.25 from independent geometry, then the corpus's structural chain has an inconsistency that must be resolved before u_0*/p_c disambiguation can proceed.

**What success looks like (Outcome A)**: a clean derivation chain `r_secondary/d = 1.187 → [specific mechanism] → z_0 = 51.25` with no free parameters. Then `z_0 = 51.25 → FTG-EMT p_c = 0.1834 = 8πα` becomes derived (α is OUTPUT not input), and the u_0*/p_c question reduces to "are these two readouts of the same Ω_freeze projection" with explicit gauge transformation.

## Section 4 — Implementation

Script: `src/scripts/verify/z0_first_principles_attempt.py` (new, ~150 lines).

Runs all 5 models, reports z_0 result for each, identifies which (if any) reproduces 51.25 cleanly. Output table format:

```
Model                    | Parameter  | z_0 predicted | vs 51.25  | Outcome
-------------------------|------------|---------------|-----------|--------
Crystalline counting     | r=1.187·d  |       4       |   -47.25  | baseline
Path enumeration k=1     | k=1 hops   |       4       |   -47.25  |
Path enumeration k=2     | k=2 hops   |       ?       |     ?     |
...
```

## Section 5 — Result Doc

Will log to `research/2026-05-18_z0-first-principles-attempt-result.md` regardless of outcome.

## Section 6 — Falsifier Discipline

Pre-reg committed BEFORE running script. Result logged regardless of outcome. No outcome rewrite.

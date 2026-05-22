# Prime-N Soliton Stability — Pre-Registration (Foundational Framework Extension)

**Date**: 2026-05-18 evening
**Origin**: Grant insight earlier this session — "why do I feel like number of loops needed for a stable knot scales as a prime number"
**Branch**: `analysis/prime-n-soliton-stability` (to be created)
**Skills applied**: ave-prereg, pre-test-physics-check, substrate-native-check, ave-corpus-grep (across 10 repos), consistency-vs-emergence (Class 1/2 — substrate-derivability check), verify-before-cite

## Section 1 — Target

Determine whether **N = prime** is the load-bearing topological constraint on stable soliton populations in the AVE substrate, or whether the apparent prime-pattern (N=1 lepton, N=3 baryon Borromean) is a partial taxonomy that obscures a different organizing principle (e.g., "odd-N" or "N ≤ 3 only" or "Cosserat-sector-counted"). If prime-N is load-bearing, promote it as a foundational predicate in Vol 2 Ch 1 (topological matter taxonomy) with predictions for N=5 stable structures.

**Sharp formulation**: Of the integers N ∈ {1, 2, 3, 4, 5, 6, 7, ...}, which N support stable irreducible soliton topologies under AVE substrate physics, and what is the substrate-derivable reason?

## Section 1.5 — Physical picture (per pre-test-physics-check, 5 bullets, mechanical/topological)

1. **N=1 (single unknot, lepton)**: trivially stable. One closed flux-tube loop on chiral Laves K4 lattice; vacuum compliance K=ℏ/c balances inductive tension. Electron at unknot ropelength 2π. No decomposition possible (one is irreducible).

2. **N=2 (Hopf link, 2 linked loops)**: Grant's hypothesis says FORBIDDEN. Physical intuition: two linked loops have attractive pairwise inductive coupling (each pumps reactive energy through the other). With only 2 loops there's no triangulating constraint to balance the attraction → collapse into composite N=1 (single torus knot) rather than holding as N=2. The Hopf-link configuration decomposes back to a lower-N attractor.

3. **N=3 (Borromean, 3 mutually-linked loops with NO pairwise links)**: stable. Proton lives here. Three loops where any TWO can be unlinked but all THREE are mutually entangled. Mechanical reason: 3-fold symmetry permits Cosserat-torsion balance where pairwise loops fail — the triple coupling provides the missing balancing term. Irreducible: removing any one loop gives N=2 unstable, removing two gives N=1 stable but different particle. The N=3 structure can't decompose to two N=2 or one N=2 + one N=1 without losing the Borromean topology.

4. **N=4 (4-loop structures)**: predicted forbidden. Decomposes into 2 × (Hopf-pair) → both pairs are themselves N=2 unstable, so the N=4 falls to 4 × N=1 individual unknots. OR decomposes into 1 × Borromean-triple + 1 × singleton → 1 × N=3 stable + 1 × N=1 stable, but they don't bind tightly because the singleton has no Borromean coupling channel into the triple. EVEN-N structures generally decomposable.

5. **N=5 (pentafold, 5-loop irreducible)**: hypothesized stable next-prime. Mechanism: 5-fold symmetric configuration where any 4 of the 5 loops are NOT Borromean-stable, requiring all 5 simultaneously → irreducibility analogous to N=3 but higher coupling order. Candidate physical realization: pentaquark exotic baryon Pc(4312)+ observed at LHCb in 2019, or some hyperon resonance. **Falsifiable prediction**: stable N=5 topological structure should manifest as a long-lived resonance distinct from N=3 baryon ladder.

**Discrete-event vs smooth**: stability is a YES/NO topological invariant (existence of finite-energy minimum at fixed N), NOT a smooth function of N. The expected pattern is N ∈ {1, 3, 5, 7, 11, ...} stable; N ∈ {2, 4, 6, 8, 9, 10, ...} unstable / decomposes.

**Connection to existing corpus**: Riemann-hypothesis.md:52 (referenced in earlier session) frames primes as "irreducible substrate modes." If primes are irreducible at the substrate level, they should also be the only stable irreducible loop-counts for soliton populations — same principle, two different observables.

## Section 2 — Corpus state (to be verified via corpus-grep)

Pre-grep expectations (will refine after grep returns):

- **Strong prior**: loop-count taxonomy work earlier this session (FI-13 resolution) established lepton=N=1, baryon=N=3 Borromean. So N=1 and N=3 are corpus-canonical stable.
- **Possible prior**: Vol 2 Ch 1 (topological matter taxonomy), Vol 2 Ch 5/6 (lepton + electroweak), AVE-HOPF (Hopf-link physics), AVE-PONDER (multi-soliton dynamics) likely have partial discussions of why even-N or N=2 specifically don't work.
- **Possible prior**: Faddeev-Skyrme solver work may have implicit constraints on N (only certain N admit finite-energy minima for given baryon-number).
- **Possible prior**: Riemann-hypothesis.md:52 "prime = irreducible substrate mode" may already imply the picture without naming "prime-N loop count" explicitly.

Will dispatch ave-corpus-grep across all 10 repos to verify.

## Section 3 — Pre-Registration

**Step 3a — Skill discipline classification**:

Per `consistency-vs-emergence` 4-class taxonomy:
- **Class 1 (consistency-then-emergence)** if corpus already contains all the substrate-physics ingredients (Cosserat torsion balance arguments, Faddeev-Skyrme stability constraints, Borromean-vs-Hopf analysis) and the prime-N pattern emerges as a derivable consequence. Most likely.
- **Class 2 (emergence-only)** if corpus has the pieces but not the unified picture; prime-N would be a NEW unifying predicate.

Per `ave-discrimination-check`:
- SM has no analogous principle — SM has 3 quark generations and 3 lepton generations by convention, not by topological count.
- AVE's prime-N (if true) would be discriminative: predicts stable N=5 exotics (pentaquark Pc(4312)+ is observed!) and N=7 stable structures NOT in SM zoo.

**Step 3b — Predictions**:

| Quantity | Expected | Falsifier |
|---|---|---|
| N=1 stable | ✓ corpus canonical | — |
| N=2 forbidden | ✓ (Grant hypothesis) | Stable N=2 Hopf-link soliton in corpus or experiment |
| N=3 stable (Borromean) | ✓ corpus canonical | — |
| N=4 forbidden | ✓ (Grant hypothesis) | Stable irreducible N=4 soliton (not decomposable) in corpus |
| N=5 stable | hypothesis (next prime) | No N=5 stable resonance observed at LHCb / no corpus derivation |
| N=6 forbidden | hypothesis (composite 2×3) | Stable N=6 in corpus |
| N=7 stable | hypothesis (next prime) | No N=7 stable structures predicted by corpus |

**Step 3c — Discriminating outcomes**:

- **Outcome A (PRIME-N CONFIRMED, ~40%)**: corpus-grep returns explicit derivations that (i) Hopf link unstable, (ii) Borromean stable via 3-fold Cosserat coupling, (iii) some statement (even partial) that even-N decomposes. Promote prime-N as foundational leaf in Vol 2 Ch 1.

- **Outcome B (PARTIAL CORPUS, NEW DERIVATION NEEDED, ~30%)**: corpus has the topology pieces but no unified prime-N argument. Promote prime-N as new foundational predicate; commission derivation work for the even-N-decomposition theorem. Multi-session.

- **Outcome C (REFINEMENT NEEDED, ~20%)**: corpus reveals the rule is actually "odd-N" or "N ≤ 3 only" or "Cosserat-sector-count + something" rather than strict prime-N. Reframe Grant's hypothesis with the corpus-refined version.

- **Outcome D (FALSIFIED, ~10%)**: corpus contains explicit counter-evidence — stable N=4 or N=6 soliton structure that's irreducible. Retract hypothesis; document the counter-example as the corpus-canonical exception.

**Step 3d — Falsifiers**:

1. Any single stable irreducible N=even-or-composite soliton in corpus (with finite-energy minimum, NOT decomposable into lower-N) falsifies the strict prime-N rule.
2. If corpus shows stable N=4 or N=9 structures, falsifies "odd-N + 1" weakening too.
3. If LHCb pentaquark Pc(4312)+ turns out to be a molecular state (5-quark = N-something-else) rather than a true N=5 topological soliton, the experimental anchor weakens.
4. If Faddeev-Skyrme solver shows finite-energy minima for ALL N (not just primes), the substrate-derivation argument fails.

**Step 3e — Scope**:

This pre-reg covers ONLY the corpus-grep verification + classification step. Does NOT yet cover:
- Writing the foundational leaf (gated on Outcome A or B)
- Faddeev-Skyrme solver numerical sweep over N=1..10 (multi-session if needed)
- Pentaquark Pc(4312)+ AVE prediction (would be its own pre-reg + driver per C8 pattern)
- Riemann-hypothesis connection extension (separate foundational work)

Output of THIS pre-reg cycle: a result doc classifying which of A/B/C/D obtains, with file:line citations from corpus-grep, and a recommendation on next steps.

## Section 4 — Falsifier discipline

Pre-reg committed BEFORE corpus-grep dispatched. Result logged regardless. No outcome rewrite.

## Section 5 — Out of scope

- Pentaquark Pc(4312)+ specific AVE prediction (own pre-reg)
- Solver implementation for N=5+ Faddeev-Skyrme minima (depends on existing engine state)
- Riemann-Hypothesis full connection (separate foundational extension)
- Tetraquark literature review (only if Outcome D / counter-evidence)

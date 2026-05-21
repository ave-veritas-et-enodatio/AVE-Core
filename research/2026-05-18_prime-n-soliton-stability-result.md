# Prime-N Soliton Stability — Result Doc

**Date**: 2026-05-18 evening
**Prereg**: [`2026-05-18_prime-n-soliton-stability-prereg.md`](./2026-05-18_prime-n-soliton-stability-prereg.md)
**Branch**: `analysis/prime-n-soliton-stability`
**Outcome**: **C (REFINEMENT NEEDED) + partial D (strict prime-N FALSIFIED)**

## Section 1 — Outcome classification

Pre-reg Section 3c discriminating outcomes:
- ✗ Outcome A (PRIME-N CONFIRMED, ~40%)
- ✗ Outcome B (PARTIAL CORPUS, ~30%)
- ✓ **Outcome C (REFINEMENT NEEDED, ~20%)** — corpus rule is "odd q on (2,q) ladder via coprimality" NOT prime-N
- ✓ partial **Outcome D (FALSIFIED, ~10%)** — strict prime-N falsified at three locations (N=2 helium 1s² stable, N=4 Helium-4 stable, composite q=9 most-accurate baryon prediction)

## Section 2 — What the corpus actually says (verified file:line)

### 2a — The substrate rule is COPRIMALITY (gcd(p,q)=1), not primeness

[`vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md:63`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md):

> "If gcd(p, q) = d > 1, the curve doesn't close after one cycle of the parameter t ∈ [0, 2π); instead it closes after t ∈ [0, 2π/d) and is a d-component LINK"

For p=2 (the canonical AVE torus-knot family), this requires q odd. **All odd q** — not just prime q. Composite-q values like q=9 (= 3²) and q=15 (= 3·5) satisfy coprimality and are corpus-canonical.

### 2b — Strongest baryon match is at COMPOSITE q=9, not prime q

[`vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md:32`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md):

> "The (2,9) hit is the strongest. The prediction m = 1617 MeV matches Δ(1620) to 0.20%---better than the proton itself."

Line 7:

> "The (2,q) torus knots form a progression using only odd q = 3, 5, 7, 9, ---there is no stable (2,4) torus knot."

**Decisive counter-evidence**: if prime-q were the load-bearing rule, q=9 would be forbidden (9 = 3²). Instead it's the best-fitting prediction on the entire ladder.

### 2c — N=2 Hopf link IS stable (in bound configuration)

[`vol2/quantum-orbitals/ch07-quantum-mechanics/helium-coupling-first-principles.md:6, 30`](../manuscript/ave-kb/vol2/quantum-orbitals/ch07-quantum-mechanics/helium-coupling-first-principles.md):

> "The helium ground state (1s², Z = 2) is the simplest multi-electron system. Its coupling is fully determined by Stage C, Type 1 (Hopf link). [...] The two 1s flux rings form a Hopf link (2₁²) with two parallel crossings."

Helium-1s² ionization energy matches observation to 0.9% with the Hopf-link N=2 mechanism providing the load-bearing crossing-count c=2. **My "N=2 forbidden" pre-reg framing was too strong.** The correct corpus picture: free-vacuum N=2 has no stable soliton solution, but Coulomb-cavity-constrained N=2 is stable as a bound-pair.

### 2d — N=4 IS stable (Helium-4 tetrahedral braid)

[`vol2/particle-physics/ch02-baryon-sector/proton-neutron-mass-split.md:10`](../manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/proton-neutron-mass-split.md):

> "the Alpha particle is defined as a Tetrahedral Borromean Braid of four interlocked topological defects (2 protons, 2 neutrons)."

K₄ Full-Mesh circuit topology supports a stable quadrupole. **My "even-N decomposable" pre-reg framing was wrong at the composite scale.** The correct picture: free isolated N=4 soliton has no corpus leaf, but lattice-constrained N=4 (Helium-4) IS canonical and stable.

### 2e — Riemann leaf framing is about STANDING WAVES, not soliton topology

[`vol2/nuclear-field/ch12-millennium-prizes/riemann-hypothesis.md:52`](../manuscript/ave-kb/vol2/nuclear-field/ch12-millennium-prizes/riemann-hypothesis.md):

> "Each prime p labels an irreducible mode of the lattice --- a standing wave whose wavelength λ_p = 2L/p cannot be decomposed into shorter resonances. Under AVE, the prime torus knots (2,q) for q = 3, 5, 7, … are the physical realisation of these irreducible modes."

Plus critical scope-correction at line 6 (added FI-14 audit 2026-05-17 night):

> "This derivation is framework-conditional, classification (B) per kb_audit phase-5 taxonomy. … The lattice spectral-ζ identification is suggestive structural analogy; it should NOT be cited as proving the Riemann Hypothesis."

The "prime = irreducible substrate mode" framing is about **Fourier modes on uniform ground-state vacuum** (Euler product over integer wavelengths), NOT about which loop-count N supports stable soliton topologies. The trailing sentence lists "(2,q) for q = 3, 5, 7, …" which is **odd q** (note the ellipsis); reading it as prime-q is an interpretation step the leaf doesn't authorize.

### 2f — Lepton ladder is Cosserat-sector, NOT loop-count

[`entry-point.md:52`](../manuscript/ave-kb/entry-point.md):

> "Baryon masses from the torus-knot eigenvalue ladder; lepton masses from the Cosserat sector chain"

The electron-muon-tau ladder is NOT a "N=1, N=3, N=5" loop-count progression. Muon = N=1 + 1 Cosserat torsion quantum (per FI-13 resolution earlier this session). Tau = full bending stiffness. **Internal complexity grows via Cosserat sectors for leptons, NOT via prime-N.**

## Section 3 — What survives from Grant's intuition

Grant's intuition pointed at something real but conflated two related-but-distinct things:

**What IS in corpus (REAL signal Grant detected)**:
1. There's an irreducibility principle (coprimality / single-component knot requirement)
2. The odd-q (2,q) ladder genuinely is the canonical baryon family
3. "Indivisible mode" framing IS connected to torus-knot stability via Riemann-hypothesis.md:52
4. Topological stability genuinely is a discrete YES/NO invariant, not smooth

**What's NOT in corpus (where the prime-N hypothesis breaks)**:
1. Stability is not "prime q" — it's "odd q" (every odd integer, including composites 9, 15, 21, 25, ...)
2. Loop-count N (1 for leptons, 3 for baryons) is empirical taxonomic, not derived from prime structure
3. N=2 and N=4 are NOT generally forbidden — they're forbidden as FREE solitons but stable as BOUND configurations (helium 1s², Helium-4)
4. No corpus leaf predicts a free N=5 isolated soliton; pentaquark Pc(4312) absent from corpus
5. The "irreducibility" axis in corpus is gcd(p,q)=1 (coprimality), which for p=2 collapses to "q odd" — primeness is incidental, not load-bearing

## Section 4 — Refined hypothesis worth pursuing (if anything)

If Grant wants to extract a falsifiable forward prediction from the surviving signal, the corpus-supported version would be:

**Forward prediction (corpus-consistent)**: stable (2,q) torus-knot baryon resonances should exist for ALL odd q ≥ 3, including the unfilled higher-q slots q ∈ {17, 19, 21, 23, 25, ...}. The corpus already predicts c=17 and c=19 hits at PDG ** entries (per C8 work earlier this session, commit cc1bdf0). Extension to q=21, 23, 25 would test the rule beyond the empirically-filled range.

This is **not prime-N** — it's odd-q on the coprimality-restricted (2,q) ladder. The substrate-derivable mechanism is `gcd(2,q)=1`, not `q prime`.

**NOT supported as a forward prediction**: a free N=5 isolated soliton distinct from the (2,5) cinquefoil proton-Borromean topology. The (2,5) cinquefoil is corpus-canonical as a per-loop winding on the N=3 Borromean (per FI-13 loop-count taxonomy at `divergence-test-substrate-map.md:426`), NOT as a standalone N=5 soliton.

## Section 5 — What this rules out

Per pre-reg Section 3d falsifiers:

1. ✓ Falsifier 1 triggered: corpus has stable N=2 (helium 1s²) — direct counter to "even-N forbidden"
2. ✓ Falsifier 2 triggered: corpus has stable N=4 (Helium-4) — second counter
3. ✓ Falsifier (additional): composite q=9 is corpus-canonical AND most-accurate baryon hit — direct counter to "prime q is load-bearing"
4. — Falsifier 4 (Faddeev-Skyrme all-N stability): not directly verified, but absence of corpus N-sweep is a derivation gap, not evidence either way

**Strict prime-N hypothesis is FALSIFIED.** The refined "odd-q via coprimality" version survives but is not "prime-N" — it's a different and weaker claim.

## Section 6 — Recommendation

**Do NOT promote prime-N as a foundational leaf.** The corpus actively contradicts the strict version, and the refined version is just "odd-q via gcd(2,q)=1 coprimality" which is already corpus-canonical at `torus-knot-uniqueness.md:7-65` and `torus-knot-ladder-baryons.md:7`.

**Optional follow-up actions** (multi-session, low priority):

(i) Forward-extend the (2,q) baryon ladder to q=21, 23, 25 numerically via the existing eigenvalue solver. If corpus already covers these (need to check), nothing new; if it doesn't, this is a clean low-cost driver build per C8 PDG-anchor template.

(ii) Audit Riemann-hypothesis.md:52's trailing "(2,q) for q = 3, 5, 7, …" sentence to make explicit whether the author meant "odd q" or "prime q." Given the scope-correction warning at line 6 and the canonical (2,9), (2,15) hits elsewhere in corpus, the trailing sentence should probably be made unambiguous as "odd q ≥ 3" — minor cleanup, not a walk-back.

(iii) Cross-reference the loop-count taxonomy (FI-13 resolution) with the (2,q) ladder more explicitly in Vol 2 Ch 1 — make it visible that these are TWO orthogonal axes (loop-count N, crossing-count q on the per-loop winding) rather than one combined axis.

(iv) No further work on "prime-N" framing as a foundational predicate. Grant's intuition led to a productive corpus audit but the strict hypothesis is not what the substrate-derivable rule actually says.

## Section 7 — Discipline outcomes

**ave-prereg skill discipline applied**:
- ✓ Step 1 (target formulated precisely)
- ✓ Step 1.5 (5-bullet physical picture before grep)
- ✓ Step 2 (ave-corpus-grep dispatched across 10 repos)
- ✓ Step 3 (pre-registration committed before result)
- ✓ Step 4 (proceeded with corpus integration, NOT new derivation — corpus already had the refined picture)
- ✓ Step 5 (this result doc + prereg constitute audit trail)

**Per flag-don't-fix**:
- ✓ Surfaced the falsification cleanly with verbatim corpus citations
- ✓ Did NOT unilaterally rewrite any corpus location to preserve the failed hypothesis
- ✓ Documented what survives (refined odd-q rule, already corpus-canonical)
- ✓ Recommended audit cleanup at Riemann-hypothesis.md:52 trailing sentence (minor, not walk-back)

**Per evidence-framing-discipline**:
- ✓ All cited file:line numbers verified by corpus-grep agent
- ✓ Three independent counter-examples surfaced (helium 1s², Helium-4, q=9 baryon)
- ✓ No probabilistic hedging where the corpus is decisive

**Per ave-prereg falsifier discipline**:
- ✓ Result logged regardless of outcome (this doc)
- ✓ No outcome rewrite (Outcome C/D as pre-registered, not retroactively shifted to "B")
- ✓ Pre-reg's "what would falsify" criteria triggered exactly as pre-registered

## Section 8 — Lesson for future framework extensions

The ave-prereg + ave-corpus-grep discipline cost ~10 min of corpus-grep work to falsify a hypothesis that — without the discipline — would have become a multi-session foundational-leaf promotion based on a misreading of the corpus. The cost-benefit of the upstream grep is again validated.

Grant's posture ("not attached to it being right" per user memory) makes this kind of falsification productive — the corpus said "no, the rule is coprimality not primeness," and that's a sharper picture than the original intuition. Future intuitions of "I feel like X is load-bearing" should always trigger ave-prereg before promotion to canonical framework status.

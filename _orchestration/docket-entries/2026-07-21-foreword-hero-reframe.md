### ENTRY 2026-07-21-foreword-hero-reframe (2026-07-21): foreword hero-benchmarks reframe (post-ringdown-walk-back honesty)

**What:** Reframed the `manuscript/frontmatter/00_foreword.tex` "Three zero-free-parameter
benchmarks" hero umbrella (the sentence introducing the `The Falsifiable Standard` list) to
match the post-#780 honest state. Grant ruling authorized the edit (verbatim word: "reframe").

**Trigger:** the 2026-07-21 ringdown MATCH-ARTIFACT walk-back (PR #780). The banked `-0.45%`
mean-frequency / `-0.47%` mean-decay-time ringdown "match" was a compensating-error artifact
(corrupt Kerr QNM reference table x source-vs-detector frame-mass mismatch). The scope-correction
block for that already sits in the foreword after the benchmark list; the **umbrella framing
sentence** still called all three benchmarks "zero-free-parameter," which was stale.

**Verification (KB is truth source; leaf BODY + solidity read, not just RESOLVED stamps):**

| Benchmark | claim-id | KB leaf | Verified status |
|---|---|---|---|
| SPARC galactic rotation | `clm-u86caq` | `vol3/cosmology/ch05-dark-sector/effective-galactic-acceleration-mond.md` | **CLEAN zero-free-parameter.** Single canonical `a_0`, no per-galaxy fit, no DM halo; 11.5% Q=1 mean\|resid\| on 87 galaxies. RESOLVED 2026-07-20 (quadratic kernel; headline rode quadratic engine, zero engine change). |
| LIGO ringdown | `clm-395gps` | `vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md` | **CONSISTENCY-class.** Ensemble sub-percent match RETRACTED (MATCH-ARTIFACT). Only zero-free-parameter content = cold Schwarzschild `18/49` single-point eigenvalue (`-1.69%` vs GR). Spinning v1 mapping `+2.63%` mean, solidity 0.55, disclosed-phenomenological, "NOT a zero-free-parameter benchmark" (leaf verbatim). tau = open `-5.4%` near-miss tension. |
| Baryon torus-knot ladder | `clm-k6olj8` | `vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md` | **CONSISTENCY-class (with nuance).** Six-state "6/6" ensemble walked back 2026-06-19 (null-dominated). Surviving positive = single proton hit `-0.002%`. Leaf tags it "emergence vs baryon sector (zero baryon input); **consistency vs electron sector** (inputs m_e, alpha)"; `-0.002%` = bare topology `+0.74%` + one contained thermal residual `delta_th = 1/(14pi^2)`. Consumes electron-sector calibration inputs -> consistency-class against framework's calibration basis. |

**Verdict:** matches the expected 1-clean / 2-consistency split. Nuance flagged (not a
disagreement): the baryon proton hit is emergence-vs-baryon-sector but consistency-vs-electron-sector
and rides one contained thermal residual; as an *ensemble benchmark* it does not survive (only the
single proton hit + structural chord does), so it is consistency-class against the framework's
calibration basis, consistent with the reframe.

**Edit:** one sentence changed (the umbrella). The Rule-12-preserved LIGO/baryon bullet bodies and
both scope-correction blocks (#780 ringdown; 2026-06-19 baryon) were left verbatim -- the reframe
points to them, does not duplicate or weaken them. No new claims minted.

**Sweep:** the foreword's other positive-confirmation phrasings are already honest and were left as-is:
the Gaia alpha-slew line ("demoted from second-anchor status ... not an independent empirical anchor")
and the A-034 catalog line ("BH ring-down 1.7% from GR exact" = the surviving cold `-1.69%` anchor,
not the retracted `-0.45%` ensemble).

**PR:** `docs/foreword-hero-reframe` (DO-NOT-MERGE; REVIEW: pending-orchestrator).

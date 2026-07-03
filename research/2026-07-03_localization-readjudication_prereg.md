# FROZEN PRE-REGISTRATION — Localization Re-Adjudication

**Date frozen:** 2026-07-03
**Arc:** LOCALIZATION RE-ADJUDICATION (Grant-fired 2026-07-03, "kick off 1")
**Branch:** `analysis/localization-readjudication`
**Consumes:** ave-prereg v1.4 Step 3.8 (readout-liveness + structural-degeneracy);
pre-test-physics-check trigger 10 (null-verdict liveness).
**This arc is the FIRST NATIVE CONSUMER of Step 3.8.** Every decision observable
below carries its named positive control AND its structural-degeneracy self-check
BEFORE any run. No null verdict is bookable until the same pipeline has read a
known-bound case correctly.

---

## 0. SCOPE-LOCKS (carried verbatim — NOT at stake)

- **mass = A1 (PR#260, PR#311 ECHO-final).** The mass sector is CLOSED and is
  NOT re-opened here. Only the **localization MECHANISM** (does a bound core
  persist in the BULK, vs. reroute to boundary/topological) is re-adjudicated.
- **This is an INSTRUMENT re-adjudication, not a lattice-ontology claim.** The
  D1 section compares the diamond-z4 and srs-z3 nets **as instruments** (statics
  well-posedness, nullspace burden, positive-control constructibility). It does
  NOT claim one net "is" the vacuum. D1 production-carrier ratification is
  Grant's, downstream.
- **The α-echo keystone is untouched.** All operators here are α-free (pure
  (1−A²) Op14 kernel). No ALPHA / Q_TANK / V_SNAP on any path.

---

## 1. THE QUESTION (open-goal framing — prove-OR-disprove)

> **Does a smooth localized A1 core, seeded on the CANONICAL carrier with a
> PROVEN-LIVE readout, self-trap and persist in the bulk (a localized breathing
> core that does not disperse) — OR does it disperse?**

The target is **the truth of bulk self-trapping**, not either answer. The
2026-07-03 verdict-exposure sweep found the merged DISPERSE falsifications
(PRs #403/#404, Stage-2/S3) evidence-exposed on THREE counts (all re-verified at
HEAD this session — §2). This arc re-asks the question with a proven-live
instrument on the Axiom-1 canonical lattice.

### 1.1 The SEDUCTION-TRAP, named and rejected

The tempting wrong reaction to the exposure is: *"the DISPERSE verdicts were
artifacts, therefore the electron localizes in the bulk after all."* **This is
rejected in advance.** Exposing that the diamond instrument could not READ a
bound state does NOT establish that a bound state EXISTS. A `[BINDS-ON-SRS]`
reading is a MEDIUM-scaffold finding that gets its OWN adversarial panel before
ANY canon change — it does not, by itself, revert PRs #403/#404's mechanism
conclusion. The falsification-exposure and the positive-existence claim are
INDEPENDENT; this prereg keeps them independent.

---

## 2. THE EXPOSURE, RE-VERIFIED AT HEAD (verify-before-cite, this session)

All three re-run by me this session by extracting the ORIGIN operator verbatim
(`native_cage_imex.build_grad_div_periodic` + `assemble_L_D`) into scratchpad and
running it read-only. Numbers:

- **(a) Sublattice decoupling.** `L_D = Div·diag(D)·Grad` on the diamond
  TETRA_OFFSETS stencil couples ONLY same-parity nodes: off-diagonal |mass|
  same-parity = 384/750/1296 (N=8/10/12), cross-parity = **0.0000** at all N →
  100.00% same-parity. The four TETRA_OFFSETS all have ODD coordinate-sum
  (`cosserat_field_3d.py:134-139`; sums 3,−1,−1,−1), so the periodic diamond box
  splits into two non-communicating sublattices.
- **(b) Nullspace-heavy.** L_D has 16/8/16 near-zero eigenvalues (|λ|<1e-9) at
  N=8/10/12 — a genuine frozen kernel (`‖L_D · Nullbasis‖ = 2.6e-15`).
- **(c) v14 sech projects onto the dead-leg.** The v14 Mode-I sech seed
  (amp 0.85, radius 2.5, dx 0.5) projects **93.5%** of its L²-energy onto the
  L_D nullspace at N=12 (sweep reported ~98% at N=24; scale-dependent, same
  qualitative finding). The live (operator-governed) fraction is **6.5%**. An
  at-rest seed sitting in the frozen kernel stays put under the CN update
  (`V^{n+1}=2V^n−V^{n-1}` with L_D·V=0) — a spurious "PERSIST", NOT physics; and
  the smooth part L_D DOES govern disperses. Either way the DISPERSE observable
  (interior peak) is dominated by an operator artifact, not bulk self-focusing.

**Corpus half-knows this:** commit `78e7d403` records "engine is degree-4 ACHIRAL
diamond, NOT canonical degree-3 chiral srs; corpus self-contradictory."

**The positive-control gap (Class-2).** The ONLY "the instrument can SEE a
self-trap" control in Stage-2/S3 runs on the **Cartesian MasterEquationFDTD**
engine (`engine_stage2..._makeorbreak.py:100-127` `run_cartesian_reference`;
`s3_cavity_pinning_gate.py`), NEVER the native TETRA pipeline that renders the
DISPERSE verdict. No demonstration exists that the native `classify()` can read
PERSIST for ANY input.

---

## 3. FROZEN OUTCOME BINS (the verdict lives in exactly one)

- **`[BINDS-ON-SRS]`** — a localized A1 core persists on the canonical chiral
  srs-z3 carrier WITH a live readout (positive control on that carrier reads
  PERSIST first). MEDIUM-scaffold finding; pre-registered to require its OWN
  adversarial panel before ANY canon change. The seduction-trap (§1.1) is named
  and rejected: this does NOT by itself revert #403/#404.
- **`[DISPERSES-ON-SRS-LIVE]`** — the seeded core disperses on srs WITH a
  proven-live readout (srs positive control read PERSIST, then the smooth core
  disperses). The falsification RE-BOOKS with solid evidence; the
  boundary/topological reroute (#403/#404) stands, now properly grounded on the
  canonical carrier rather than on the exposed diamond instrument.
- **`[INSTRUMENT-DEAD]`** — no bound-reading configuration constructible on
  EITHER carrier after a genuine attempt (§4 step-1 and §6 srs positive control
  both fail to read PERSIST for any input). A named engine-capability blocker;
  NO physics verdict on bulk self-trapping. The #403/#404 DISPERSE verdicts are
  then instrument-dead (the native readout cannot register bound for any input).
- **`[STUCK-FRAMING]`** — a framing fork the axioms cannot settle (e.g. what
  counts as "the same test" across carriers beyond canon-derived
  parameterization). Surface to Grant (trigger 8/9); do NOT self-resolve.

Both **Grant's standing expectation** and the **engine verdict** are recorded
regardless of which bin lands.

---

## 4. STEP 1 — NATIVE-DIAMOND POSITIVE CONTROL (the make-or-break for the instrument)

**Goal:** construct a configuration KNOWN to bind on the diamond stencil and push
it through the ORIGINAL Stage-2/S3 `classify()` pipeline UNMODIFIED. Which bin?

**Candidate routes (attempt in order; first success suffices):**
1. An explicit eigenmode of L_D at a LOW nonzero eigenvalue, localized
   (participation ratio ≪ N³) — the operator's own bound-like mode.
2. An analytically bound state on ONE parity sublattice (respecting the
   decoupling: a seed supported on even-sublattice sites only).
3. A deliberately nullspace-ORTHOGONAL seed (project the v14 sech OUT of the
   nullspace; evolve only the 6.5% live part).

**Readout:** push through `engine_stage2_native_cage_imex_makeorbreak.classify()`
VERBATIM (same solve, same bins, same thresholds — the IDENTICAL pipeline).

**Adjudication (both outcomes decisive):**
- Reads **MODE_I_PERSIST** → the instrument CAN see a trap; the original DISPERSE
  verdicts regain PARTIAL standing (the readout is live, at least for this
  input). Report honestly; this LEANS the srs re-run toward being the real test.
- After a GENUINE attempt at all three routes, NO configuration reads PERSIST →
  the native readout cannot register bound for ANY input → `[INSTRUMENT-DEAD]`
  for the diamond carrier. Decisive.

### 4.1 Step-1 readout-liveness (Step 3.8a) + structural-degeneracy (3.8b)

- **Positive control OF the positive control:** the constructed config is ITSELF
  the known case; its expected reading is PERSIST BY CONSTRUCTION (an L_D
  eigenmode at nonzero λ oscillates without dispersing under energy-conserving
  CN). If it does not read PERSIST, that is the `[INSTRUMENT-DEAD]` finding.
- **Structural-degeneracy self-check on `classify()`'s observables:**
  - `v_peak_mean_post > 0.2` (bin I-1): a nullspace seed is FROZEN → trivially
    passes I-1 (peak never moves). **This is the degeneracy the whole arc
    exposes.** Guard: require the config to have NONZERO live-fraction (report
    nullspace-fraction §5 BEFORE reading the bin) — a purely-nullspace "PERSIST"
    is DISQUALIFIED as a bookkeeping-frozen artifact, NOT a bound state.
  - `std/mean ∈ (0.05, 0.5)` (I-2/I-3, "breathing"): a frozen seed has std≈0 →
    FAILS I-2 → reads MODE_III. So a purely-frozen nullspace seed does NOT
    spuriously read Mode-I via `classify()` (it fails the breathing bin). Good:
    the ORIGINAL bins already partially guard this. Verified: the arc must show a
    config that reads PERSIST **with genuine breathing AND nonzero live-fraction**.

---

## 5. STEP 2 — SPECTRAL-DECOMPOSITION DIAGNOSTIC (first-class, reusable)

A small module `spectral_liveness.py`: decompose any seed against a given
operator's spectrum; report **nullspace-energy fraction** + spectral-weight
profile (energy vs eigenvalue bands). This is the STANDING pre-run liveness
diagnostic for localization tests — it runs on EVERY seed BEFORE its verdict is
read (Step 3.8 made operational).

**Validation (reproduce the exposure independently):**
- v14 sech vs diamond L_D → must reproduce the ~93–98% nullspace fraction.
- The step-1 positive-control config → must show LOW nullspace fraction (it lives
  in the governed subspace by construction).
- Every srs seed (§6) → nullspace fraction reported BEFORE its verdict.

**Consistency-vs-emergence tag:** INFRASTRUCTURE (a diagnostic instrument). No
physics claim; no CODATA input.

---

## 6. STEP 3 — THE srs-z3 RE-RUN (the physics reading)

Port the Stage-2 bulk-self-trap test to the **chiral srs z=3 carrier** — the
Axiom-1 canonical lattice. Rule-14: ADAPT the certified core, do NOT rebuild.

### 6.1 Canon-derived parameterization (NO tuning-to-match-diamond)

- **Operator:** the srs-native graph Laplacian `L_srs = Bᵀ·diag(D_bond)·B`
  ALREADY EXISTS and is canon (`srs_cage_winding.assemble_L_srs`, built on
  `build_srs_net`'s z=3 connectivity). Verified this session: **nullspace dim = 1
  (the constant mode ONLY) at L=4/6/8** — NOT the diamond's 8-16 dim frozen
  kernel. This is the instrument the arc needs; it is derived from canon, not
  reinvented.
- **Saturation kernel:** `S(A)=(1−A²)^exponent`, `D=1/S` — the SAME α-free Op14
  kernel (`graded_vacuum_network`), per-site scalar function of local strain,
  geometry-agnostic → carries to srs unchanged.
- **Bulk impedance / speed:** `Z_bulk=√2·ρ_bulk·c0`, `c_bulk=√2·c0` at K=2G
  (three-channel-impedances.md:22-24, pytest-gated). The bulk dilatational speed
  scale is CANON, not a diamond match.
- **Bond geometry:** from the srs builder (z=3, girth-10, I4₁32).

### 6.2 ENGINEERING-CHOICE tags (genuinely-free translation choices)

Each tagged with rationale (substrate-first-for-numbers discipline):
- **timestep dt** — ENGINEERING-CHOICE: accuracy-set, NOT stability-set (CN is
  unconditionally stable). dt-convergence check required (same discipline as the
  diamond driver's dt sweep).
- **box size L (srs supercell edge)** — ENGINEERING-CHOICE: L∈{4,6,8}; verdict
  must be L-robust (the diamond driver required N-robustness). Rationale: finite-
  size cross-check, not a physics knob.
- **seed width (in node-pitch cells)** — ENGINEERING-CHOICE: matched to the v14
  sech radius in the shared cube-frame (`frame_N`) so the (2,3) geometry is
  identical across carriers, per `seed_A1_sech`'s node-pitch scaling. Rationale:
  same physical core size, not tuned to force a verdict.

### 6.3 Seeds + controls (every one gets its §5 nullspace-fraction BEFORE verdict)

1. **Smooth core (the equivalent of the v14 sech)** — `seed_A1_sech` on srs.
   The primary test seed.
2. **srs POSITIVE CONTROL** — a KNOWN-BOUND srs config, constructed the SAME way
   as step 1 (a low-nonzero-λ localized L_srs eigenmode, OR a nullspace-orthogonal
   localized seed). Must read PERSIST through the srs classify FIRST (readout-
   liveness); its expected reading is named: PERSIST with genuine breathing.
3. **Null controls** — (a) a delocalized/uniform seed (should NOT read a
   localized core); (b) the constant mode itself (srs nullspace — should read as
   the degenerate frozen case, DISQUALIFIED like §4.1).

### 6.4 Classify with the ORIGINAL frozen Stage-2 bins (KEEP-BOTH)

Apply the frozen §8a Stage-2 bins where they still apply (I-1..I-6, the
`classify()` thresholds). **KEEP-BOTH:** if the srs carrier needs a bin
refinement (e.g. an srs-native localization metric distinct from the cube-
interior peak), ADD it ALONGSIDE the legacy bins, NEVER redefine in place. The
legacy verdict is always reported next to any refinement.

### 6.5 srs readout-liveness (Step 3.8a) + structural-degeneracy (3.8b)

- **Positive control:** §6.3.2, its PERSIST reading named, pushed through the
  IDENTICAL srs classify path BEFORE the smooth-core verdict is booked.
- **Structural-degeneracy self-check on the srs decision observable:**
  - The srs "localized core persists" observable is the interior-masked
    energy-density PEAK on the node cloud (NOT centroid — shell-degeneracy
    guard). Is it forced null/nonzero by bookkeeping? The srs L_srs nullspace is
    ONE dimension (constant mode) → a localized seed has ~100% live fraction →
    NO large frozen-kernel degeneracy (verified §6.1). The constant-mode overlap
    is reported and subtracted (the §5 diagnostic). This is the KEY instrument
    contrast with the diamond.
  - **Global-sum degeneracy guard:** the decision observable is a LOCAL peak /
    per-node localization, NOT a global sum over the closed periodic graph (which
    telescopes to zero by bond antisymmetry — the exact EM-readout Stage-1 killer
    the Step 3.8 provenance names). Confirmed local.

---

## 7. STEP 4 — THE D1 EVIDENCE SECTION (instrument comparison only)

The result doc gets a dedicated section comparing the two carriers AS
INSTRUMENTS, feeding Grant's pending D1 ratification (srs-z3 as production
carrier). Axes:
1. **Statics well-posedness** (srs: Stage-1 EM-readout proved statics; diamond:
   sublattice-decoupled).
2. **Nullspace burden** (diamond: 8-16 dim frozen kernel; srs: 1 dim constant
   mode). VERIFIED this session.
3. **Positive-control constructibility** (can each carrier read PERSIST for a
   known-bound input? — §4 vs §6.3.2).
4. **Chirality** (srs carries writhe/handedness = the (2,3) charge; diamond
   achiral, writhe≡0 — `srs_cage_winding.py:11-16`).

**Instrument comparison ONLY. NO lattice-ontology claim.** Whether the srs "is"
the vacuum is Grant's D1 call; this section provides the instrument evidence.

---

## 8. GRANT'S STANDING EXPECTATION + THE ONE PLUMBER QUESTION (trigger 10)

**Standing expectation (from corpus):** the localization arc already leaned
toward BOUNDARY/TOPOLOGICAL localization (electron-localization / engine-reroute
arc: "localization = BOUNDARY/TOPOLOGICAL", bulk-cage FALSIFIED+MERGED #403/#404).
Grant's prior is that the bulk does NOT self-trap; the reroute stands.

**The one plumber-physical question surfaced to Grant BEFORE the framing locks
(trigger 10 / trigger 8 ontology):**

> If the diamond box is really two plumbing manifolds that never share a pipe,
> and the smooth seed sits 93% in the manifold's dead-leg (the frozen nullspace)
> that the wave operator can't push — is "the core disperses" measuring the water,
> or measuring the dead-leg? And on the srs net (one connected manifold, no
> dead-leg), if the same smooth core STILL disperses, is that the real answer —
> or is a bulk self-trap the WRONG NOUN entirely, because the electron's
> localization was never a bulk-pressure basin but a boundary/topological
> pin (the reroute you already merged)?

This question is recorded here as a framing surface; the arc proceeds with the
open-goal (prove-or-disprove) framing regardless of Grant's answer, and records
both his expectation and the engine verdict.

---

## 9. CONSISTENCY-VS-EMERGENCE TAGS

- **Step 1 (diamond positive control):** INFRASTRUCTURE (instrument liveness).
- **Step 2 (spectral diagnostic):** INFRASTRUCTURE.
- **Step 3 (srs re-run VERDICT):** the PHYSICS reading (manifestation-class: a
  time-domain dynamical property of the canon operator; no CODATA input, α-free).
- **Step 4 (D1 section):** INFRASTRUCTURE (instrument comparison).

No emergence-class claim is headlined anywhere. The only physics reading is the
srs re-run bin, and it is a manifestation (dynamical behavior of the canon
operator on the canon carrier), not an emergence claim.

---

## 10. RELATIONSHIP TO THE EXPOSED STAGE-2/S3 DOCS (cite, do NOT edit)

Per the collision guard, this arc does NOT edit the Stage-2/S3 result docs (a
sibling agent owns the exposure caveats). The relationship recorded in the
result doc will be one of:
- **SUPERSEDES-WITH-EVIDENCE** — if `[DISPERSES-ON-SRS-LIVE]` or `[BINDS-ON-SRS]`
  lands (a live-instrument reading on the canonical carrier supersedes the
  exposed diamond reading).
- **CORROBORATES** — if the srs live reading agrees with the #403/#404 DISPERSE
  direction (the reroute stands, now grounded).
- **INSTRUMENT-BLOCKED** — if `[INSTRUMENT-DEAD]` (no verdict; the exposure
  stands as the whole finding).

Citations only. The exposed docs:
`research/2026-06-24_engine-stage2-native-cage_result.md`,
`research/2026-06-24_engine-s3-cavity-pinning_result.md`.

---

**FROZEN. No run may alter the bins, the positive-control requirement, or the
structural-degeneracy guards above.**

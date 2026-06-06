# Trampoline-Metaphor Audit — Result (Inductance as Wound Spherical Gyroscope)

**Date:** 2026-06-05
**Branch:** `analysis/2026-06-05-trampoline-metaphor-audit`
**Prereg:** [`_orchestration/2026-06-05_trampoline-metaphor-inductance-gyroscope-audit.md`](../_orchestration/2026-06-05_trampoline-metaphor-inductance-gyroscope-audit.md)
**Method:** 6 independent `ave-auditor` lenses → 6 `ave-corpus-grep` adversarial verifiers (re-grep every cited quote) → synthesis. **All findings below are verification-clean: 55/55 quotes verified verbatim, 0 unverified, every `assessment_holds=true`.**
**Status:** FINDINGS FROZEN. Queue pending Grant adjudication on scope (pedagogy vs surfaced-correctness) + execution.

---

## §0 Headline

The locked substrate-picture — **node = chirally-wound spherical gyroscope rotor (ω=0 at rest), bonds = chiral winding springs** — is **the corpus's own canonical position** at the *local* level, and survives all three adversarial probes (net-B, cubic, θ-vs-ω). Both audit targets confirmed. But the audit bounded two priors:

1. **The single-rotor picture BREAKS spin-½ under the strong reading.** A lone per-node rotor is the falsified *point-defect* case; spin-½ lives on the **extended closed loop** (the electron 0₁ unknot threading many nodes), via the belt-trick double-cover. The gyroscope is the *local inductive DOF*, NOT "the electron's spin-½."
2. **The orchestrator's proposed reconciliation ("L at nodes, C at bonds") was REFUTED by the corpus.** Both `L_cell=μ₀ℓ_node` and `C_cell=ε₀ℓ_node` are per-bond; the node *also* carries both sectors. The real split axis is **lumped-at-node vs distributed-on-bond** (standard TLM), not L-vs-C.

---

## §1 T1 — C/L balance: **HOLDS** (presentation defect, NOT missing physics)

The trampoline pedagogy lopsides toward the capacitive/translational sector and buries the inductive gyroscope half — but the L-sector *physics* is present in canon; the *pedagogy* is unbalanced.

- **Gyroscope avatar absent.** `gyroscope/flywheel/rotor/spin-up/Larmor` → **0 hits** as picture-elements in the primer, **1** in the framework — and that one ([`trampoline-framework.md:223`](../manuscript/ave-kb/common/trampoline-framework.md)) is an outbound cross-ref to the spin-½ *paradox* appendix, not the canonical flywheel chapter. The capacitive sector gets named avatars throughout ("press down", "bowling ball", "depress").
- **Inductive sector buried to Step 6 of 6.** B-field role-assignment first appears at [`primer:314`](../manuscript/ave-kb/common/trampoline-analogy-primer.md) as a sub-bullet; the load-bearing dynamical variable `A` is defined ([`primer:147`](../manuscript/ave-kb/common/trampoline-analogy-primer.md)) as "degree of unbuckling" — a *displacement* coordinate; `S(A)=√(1−A²)` is a Pythagorean constraint on bond-*tip position*, zero rotational content.
- **Canonical-elsewhere-but-uncited.** The gyroscope electron is canonical `clm-salw2h` (conf 0.8 / sol 0.70, [`vol2/claim-quality.md:367`](../manuscript/ave-kb/vol2/claim-quality.md)), reaching 6 leaves — yet `grep clm-salw2h` against both trampoline docs exits 1 (no match).
- **Honest counter-evidence (keeps T1 scoped).** The storage-mode table ([`framework:369`](../manuscript/ave-kb/common/trampoline-framework.md)) gives the inductive sector EQUAL billing (`κ² | Cosserat curvature ∇ω | magnetic/inductive | θ↔ω`), and Axiom 1 ([`axiom-definitions.md:16`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md)) states microrotation IS spin. **Modal accounting is balanced; the defect is lead-ordering + avatar + figure.**

**Fix class:** lead-ordering / named-avatar / figure — NOT re-derivation. KEEP-BOTH: preserve the balanced storage-mode table.

---

## §2 T2 — node-vs-bond LC: **PARTIALLY-HOLDS** (unreconciled framing split; 3 locales, not 2; not a hard contradiction)

- **The split is real and grep-confirmed on both sides, with no cross-pointer.** Same full LC tank placed at the **node** ([`dual-reactance-storage-taxonomy.md:13`](../manuscript/ave-kb/common/dual-reactance-storage-taxonomy.md): "the node's TWO reactance sectors") AND the **bond** ([`framework:395`](../manuscript/ave-kb/common/trampoline-framework.md): "The bond is also an LC tank").
- **Three locales, not two:** node / single-bond ([`framework:544`](../manuscript/ave-kb/common/trampoline-framework.md)) / bond-pair ([`primer:313`](../manuscript/ave-kb/common/trampoline-analogy-primer.md), [`cosserat-mass-gap:11`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md)).
- **NOT a hard contradiction.** [`translation-circuit.md:97-104`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md) supplies a coherent dual description: NODE = lumped LC oscillator; BOND = distributed transmission-line + Cosserat couple-stress as mutual-inductance gradient. Textbook lumped-node + distributed-line TLM decomposition of ONE medium — but it lives only implicitly and is never cross-linked from the split sites.
- **Orchestrator reconciliation refuted (L2-F7):** both `L_cell=μ₀ℓ_node` AND `C_cell=ε₀ℓ_node` are per-bond ([`vol1/claim-quality.md:1596`](../manuscript/ave-kb/vol1/claim-quality.md)); inductance lives on both sides. Real axis = lumped-vs-distributed.
- **Sharper unreconciled point surfaced:** "single-bond LC tank" vs "bond-pair LC tank" are used **interchangeably** for the electron rest-energy Virial sum `m_e c² = ħω_C` — load-bearing for the α derivation ([`ch8-alpha-golden-torus.md:50-54`](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md)). This is sharper than node-vs-bond.

---

## §3 Spin-½ — the swing finding: **BREAKS (strong) / PRESERVES (weak)**

- **WEAK reading PASSES:** "node = wound rotor" correctly identifies *where* spin lives — the Cosserat microrotational DOF IS the substrate-native origin of spin + the inductive/B sector ([`axiom-definitions.md:16`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md)).
- **STRONG reading FAILS** ("a single per-node rotor hosts spin-½ on its own"). Three unanimous corpus routes:
  1. **Topological:** a per-node point-rotor IS the "point-defect" case the corpus says "would indeed fail" — only integer spin; spin-½ recovered ONLY on the extended 0₁ unknot ([`spin-half-paradox.md:12`](../manuscript/ave-kb/vol2/appendices/app-b-paradoxes/spin-half-paradox.md)).
  2. **Mechanistic:** "the *extended* nature of the defect is what picks up the 2T double-cover" ([`finkelstein-misner-spin-half-derivation.md:61`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md)) — belt-trick needs a body to unwind through; one rotor has none.
  3. **Group-theoretic:** single-node rotation lives in T=A₄, preserves A/B sublattices; the A↔B swap needs "reflections... or some other physical mechanism" ([`k4-rotation-group.md:123`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md)).
  - The framework's OWN Step 5 builds spin-½ from TWO geared rotations SO(3)_frame × SO(3)_field 2:1 ([`framework:214`](../manuscript/ave-kb/common/trampoline-framework.md)); a single gyroscope is one SO(3) with nothing to gear against.
- **What bounds the reframe:** (a) the rotor must be the local inductive DOF distributed around a CLOSED EXTENDED loop, not an isolated node; (b) the 4π half-cover is a property of that extended topology + the (2,3) phase-space Clifford-torus winding ([`spin-as-precession.md:10`](../manuscript/ave-kb/vol2/particle-physics/ch04-quantum-spin/spin-as-precession.md)) — a SECOND structure in a different coordinate system.
- **CAVEAT:** the g=2 / Larmor / flywheel **10⁻⁸ isomorphism is single-particle precession only** and does NOT certify the 4π bookkeeping (`clm-salw2h` open strengthen-by, [`vol2/claim-quality.md:389`](../manuscript/ave-kb/vol2/claim-quality.md)). It cannot be cited as evidence the lone rotor "is" spin-½.

---

## §4 Adversarial probes — locked picture HOLDS on all three; two real corpus gaps surfaced

- **(a) net-B — picture HOLDS.** Frozen chirality is spatial-PARITY (buckling direction, I4₁32; [`primer:53`](../manuscript/ave-kb/common/trampoline-analogy-primer.md)), time-even, orthogonal to the time-odd ω/B sector; rest ω oscillates about zero ([`cosserat-mass-gap.md:70-72`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/cosserat-mass-gap.md)). **GAP:** the corpus NOWHERE states "magnetically neutral rest vacuum" (zero grep hits) — load-bearing discriminator, corpus-UNSTATED.
- **(b) cubic-vs-spherical — picture HOLDS, but exposed a live internal contradiction (predates the picture; flag-don't-fix).** Isotropic per-node inertia is compatible with collective cubic lattice anisotropy. BUT: the dedicated leaf says cubic at HIGH amplitude (`A²→1`, [`cubic-k4-empirical-anisotropy.md:11`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/cubic-k4-empirical-anisotropy.md)) while the framework's own data says cubic at LOW / spherical at high (Pearson(V_peak, asphericity) = −0.191, "0.937 spherical at high phase", [`framework:786-787`](../manuscript/ave-kb/common/trampoline-framework.md)). Negative Pearson settles it AGAINST the leaf wording; [`framework:837`](../manuscript/ave-kb/common/trampoline-framework.md) instantiates the "collapse" vs "saturation collapse" equivocation.
- **(c) θ-vs-ω + cosmic-boundary — picture HOLDS on all three sub-claims (15/15 verified).** ω=0 at rest is the STRONGEST finding and is canonically **load-bearing**: ω=0 is an EXACT FIXED POINT of the even-in-ω coupling — "a linear V→ω term would manufacture spin below threshold (wrong physics)" ([`photon-ee-mapping.md:84`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/photon-ee-mapping.md); Grant-adjudicated canonical 2026-06-04). Net ω is an excited-soliton flywheel property, never a rest DC field. Ω_freeze = cosmic-boundary 𝒥/I ([`framework:137`](../manuscript/ave-kb/common/trampoline-framework.md)); its only per-node imprint is the STATIC over-bracing u₀ (θ-like, [`framework:103`](../manuscript/ave-kb/common/trampoline-framework.md)).

---

## §5 Doc-structure verdict: **(c) BOTH — build-tail is load-bearing**

A co-equal capacitive-bowling-ball / inductive-gyroscope avatar pair is **necessary** to fix the T1 prominence asymmetry, but **insufficient and, done naively, wrong**: a stand-alone "one gyroscope = the electron" avatar hard-codes the falsified strong reading (§3). The avatar must be introduced as the **local inductive DOF**, with spin-½ / 4π half-cover explicitly deferred to the **extended-loop closure** — which is exactly what framework Steps 5–6 already gesture at. So the build-tail upgrade carries the gearing + extended-defect content that keeps the avatar honest. Introduce avatar (P1) and sharpen Steps 5–6 in the SAME pass.

---

## §6 Improvement queue

### A. Trampoline-pedagogy fixes (THIS audit's deliverable)
- **P1 [primer, structural]** New primer Step (parallel to Step 2 buckling, BEFORE Step 4 "press"): node-as-wound-gyroscope-rotor — rest-angle θ (ω=0, magnetically-neutral rest) vs spin-up to net ω. Highest-leverage edit.
- **P1 [both docs, lexical]** Introduce "gyroscope" (+ "flywheel" for the spun-up electron) as the named inductive avatar, mirroring "bowling ball / press".
- **P2 [framework, figure]** Figure whose subject is the spin-up / magnetic-moment mechanism; add a twist/spin-up/magnetic-moment ROW to the Fig-4 mapping table ([`framework:447-461`](../manuscript/ave-kb/common/trampoline-framework.md)).
- **P2 [both docs, cross-ref]** Link primer Cross-references + framework §2.4/§3 to ch04-quantum-spin (spin-as-precession, larmor-derivation, visual-equivalence) + spin-gyroscopic-isomorphism / clm-salw2h.
- **P2 [framework §2.2 + dual-reactance leaf, cross-pointer]** One cross-pointer to [`translation-circuit.md:97-104`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md) framing the split as lumped-LC-at-node / distributed-TL-on-bond (KEEP-BOTH). Same edit locus as the cross-ref above — execute together.
- **P3 [terminology]** Coin a consolidated label for "rest-angle θ" (assembled from framework:85 + :103 + :369).

### B. Surfaced correctness items (FLAG-DON'T-FIX — Grant adjudication; may warrant separate sessions)
- **#6 [α-chain, adjudication]** Decide which locale owns the electron rest-energy Virial sum — single-bond vs bond-pair LC tank — load-bearing for [`ch8-alpha-golden-torus.md:50-54`](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md). **Sharper than node-vs-bond.**
- **#7 [cubic-anisotropy leaf, correctness]** Reconcile cubic-vs-spherical amplitude-ordering: leaf says `A²→1` (high), framework data (Pearson −0.191) says low. Correct the leaf or KEEP-BOTH if two distinct regimes; disambiguate "collapse" vs "saturation collapse".
- **#8 [axiom-definitions or new leaf, stipulation]** Write down the "magnetically neutral rest vacuum / net per-node B=0 at rest" discriminator explicitly (currently corpus-unstated); anchor to the ω=0-fixed-point result + Machian no-preferred-frame.

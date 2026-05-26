# Epic: clm-0ktpcn Golden Torus α Strengthening

**Status**: PHASE 1 COMPLETE (sub-item 2 FM chain promotion landed at `226241cd` + `audit/2026-05-25_clm-0ktpcn-phase-1-fm-chain-promotion`)
**Target claim**: `clm-0ktpcn` — Golden Torus α Derivation (Three-Regime Closure)
**Branch**: `analysis/golden-torus-alpha-strengthen` off `main` @ `c655526b`
**Workstream started**: 2026-05-25
**Phase 1 completed**: 2026-05-25 — 8 claims propagated 0.45 → 0.50 via depends-on cascade after closing sub-item 2 (FM chain promotion)

## Why this workstream

`clm-0ktpcn` is the **highest-leverage shaky-load-bearing claim in the AVE corpus** per `make kb-claim-stats`:

- **Solidity**: 0.45 (bottom edge of "use as input only, don't build deeper")
- **Dependents**: **21** (highest single-claim dependent count)
- **Canonical location**: `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md`
- **LaTeX source**: `manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex`
- **Claim entry**: `manuscript/ave-kb/vol1/claim-quality.md` (clm-0ktpcn block)

Every percent of solidity gained on clm-0ktpcn propagates to 21 downstream claims via the depends-on graph. This is the single highest-impact place to invest theory work right now.

## What the claim says

$\alpha^{-1}_{\text{ideal}} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038$ derived via 3-regime closure on the electron unknot's **phase-space (2,3) Clifford-torus winding**:

| Regime | Physical principle | Equation |
|---|---|---|
| (a) Nyquist | Discrete lattice sampling cutoff (Ax 1) | $d = \ell_{node}$ |
| (b) Crossings | Transverse self-avoidance at phase-space crossings (Ax 2) | $R - r = 1/2$ |
| (c) Screening | Spin-1/2 half-cover of Clifford torus $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ via $SU(2) \to SO(3)$ 2-to-1 cover | $R \cdot r = 1/4$ |

These three jointly fix the Golden Torus geometry $(R, r, d)$ uniquely; from which the multipole sum collapses to $4\pi^3 + \pi^2 + \pi$.

## What's open (4 sub-items from claim-quality strengthen-by lists)

**Attribution clarification (per audit 2026-05-25)**: clm-0ktpcn has its own 4-item strengthen-by list (orthogonality of sum-decomposition, prose reframe, (2,3) uniqueness, δ_strain magnitude derivation). clm-0ktpcn ALSO depends-on clm-unk0bd (body-topology) whose strengthen-by list carries the 4 open caveats listed below. Strengthening either claim transitively lifts clm-0ktpcn's solidity via the `min(confidence, depends-on-solidities)` chain. The 4 items below are sourced from **clm-unk0bd**'s strengthen-by (the body-topology root), which is the actual confidence-bump target for Phase 1 sub-item 2 (FM chain promotion) per the cascade-propagation discipline.

1. **(2,3) phase-space winding uniqueness** — currently asserted as "simplest stable winding," not derived. Why not (4,3), (5,2), (3,2)? Open work.
2. **Finkelstein–Misner spin-1/2 derivation explicit in leaves** — the $K_4 \to A_4 \to 2T \subset SU(2)$ chain is referenced but not spelled out at leaf level.
3. **Photon-720° compatibility resolution** — "a final determination deferred to a more intense review after the porting effort is complete." Open call.
4. **Real-space topological protection vs phase-space-winding-as-protection** — "phase-space-winding-as-protection is the framework's current position; not yet rigorously established."

## Phase plan

| Phase | Goal | Status |
|---|---|---|
| **0a** | Orchestration epic doc + corpus-grep survey (ave-prereg) | ✓ COMPLETE 2026-05-25 |
| **0b** | Workstream-level pre-registration doc | ✓ COMPLETE 2026-05-25 |
| **0c** | Grant plumber-physical adjudication (which sub-item to tackle first + mechanism intuition) | ✓ COMPLETE 2026-05-25 — sub-item 2 selected |
| **1** | Sub-item 2 (FM chain promotion) — new leaf finkelstein-misner-spin-half-derivation.md drafted + cross-refs + clm-unk0bd confidence bump | ✓ COMPLETE 2026-05-25 (`226241cd`) |
| **2** | KB leaf update + claim-quality entry update + solidity score recalculation | ✓ COMPLETE 2026-05-25 — 8 claims propagated 0.45 → 0.50 |
| **3** | Sub-agent audit (ave-auditor) on derivation rigor | ✓ COMPLETE 2026-05-25 — GO-WITH-AMENDMENTS; all 4 amendments applied before commit |
| **4** | Cascade propagation to dependent leaves (if claim re-classified) | ✓ COMPLETE 2026-05-25 — auto-cascaded via depends-on graph |
| **5** | Closure-roadmap §0.5 entry (if walk-back) or §0 dashboard update (if strengthen) | PENDING (post-push deliverable) |
| **6** | Commit + audit tag + push to remote | ✓ COMMIT + TAG 2026-05-25; push pending Grant adjudication |
| **2+** | Sub-items 1/3/4 (remaining 3 of 4 strengthen-by items on clm-unk0bd) | PENDING (Grant adjudication on which next) |

## Phase 0a corpus-grep findings (2026-05-25)

Per `ave-prereg` discipline corpus survey across 10 AVE-staging repos + Applied-Vacuum-Engineering archive. Full findings in agent return; key state per sub-item:

| Sub-item | Prior work state | Classification | Easiest promotion path |
|---|---|---|---|
| **1. (2,3) uniqueness** | `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md` (clm-8c3yhs) + L3 doc 25 carry a minimality-from-knot-theory argument (coprimality + both ≥2 + smallest non-trivial). Doc 25 §9 explicitly admits: "Doesn't prove that the K4 substrate STABILIZES (2,3) bound states dynamically." | **DERIVED-WEAK** (minimality, not dynamical-stability) | Accept minimality OR derive dynamical-stability separately (green-field) |
| **2. FM chain explicit** | L3 doc 23 (`research/_archive/L3_electron_soliton/23_step2_spin_half_from_k4.md`, 272 lines) is the most detailed FM-on-K4 derivation. §2.2 applies belt-trick to K4 unknot; §3 provides gyroscopic-isomorphism numerical anchor (10⁻⁸ deviation to Pauli evolution); §7 admits limitation: "Does not provide a discrete-lattice computation of FM kink on K4." KB version (`spin-half-paradox.md` clm-salw2h) just ASSERTS-BY-IMPORT. | **DERIVED-HYBRID in L3, ASSERTED-BY-IMPORT in KB** | Promote doc 23 §2-3 to a KB leaf (mostly framing, not new derivation) |
| **3. Photon-720° compat** | L3 doc 06 (`research/_archive/L3_electron_soliton/06_winding_index_projection.md`) is the most extensive photon-720° treatment. Works projection from AVE Level-1 (SU(2) windings, where 720° lives) → Hopf fibration → polarization → geometric trajectory (where 720° invisible). §5 gives falsifiable consistency prediction (3 tube-wraps per Clifford-minor cycle). §8 lists 720° as queue item [3], unresolved pending Phase-3 numerical work. Stale framing at `manuscript/frontmatter/00_foreword.tex:98` (Möbius-K4 framing) needs walk-back if sub-item closes. | **PARTIAL-DERIVATION (L3) + DEFERRED (KB)** | Promote doc 06 §projection-map argument to KB leaf; walk back stale foreword framing |
| **4. Topological protection** | clm-unk0bd:23 admits "not established at real-space-body level; phase-space-winding-as-protection is the framework's current position; not yet rigorously established." `phase-locked-topological-thread.md:187-199` gives numerical/empirical support via K4-TLM 32³ simulation with Ax4 saturation enabled. **`VACUUM_ENGINE_MANUAL.md` A30/A32/A34 documents that K4-Cosserat engine does NOT dynamically protect localized topology — protection must be ansatz-injected.** | **ASSERTED + EMPIRICALLY-CONTESTED** | Real green-field — either derive rigorously OR concede stability is purely energetic + acknowledge ansatz-only protection in engine |

### Corpus inconsistency surfaced

- `electron-identification.md:56` (clm-uatcql Two-Reason-Trap row): "Stability (non-decay) | Ax1 topological protection ✅ **axiom-derived**"
- `claim-quality.md:23` (clm-unk0bd Caveat 1): "Topological protection is **not established** at the real-space-body level"
- `VACUUM_ENGINE_MANUAL.md` A30/A32/A34: engine does NOT dynamically stabilize localized topology

The KB claim-quality caveat contradicts the canonical leaf's status marker. **Flagged for separate audit follow-up** — not in scope for this workstream but should be tracked.

### Agent's promotion-ROI ranking

- **Sub-item 2** (FM chain): highest-ROI mechanical promotion — doc 23 is essentially ready
- **Sub-item 4** (topological protection): highest-truth-discovery — corpus has internal contradiction + negative empirical evidence
- **Sub-item 1** (dynamical-stability uniqueness, as distinct from minimality): green-field
- **Sub-item 3** (photon-720°): middle complexity — promote doc 06 + walk-back stale framing

## Adjudication queue (Grant decisions needed)

| Item | Status | Notes |
|---|---|---|
| Which sub-item to tackle first | PENDING — surfaced post Phase 0 corpus survey | Initial agent read: sub-item 1 ((2,3) uniqueness) is most upstream |
| Plumber-physical mechanism intuition for chosen sub-item | PENDING | Triggers ave-prereg pre-reg writing |
| Classification per consistency-vs-emergence | PENDING | Likely axiom-manifestation but Grant adjudicates |
| Closure-path acceptance after Phase 1 | PENDING | Whether derivation is rigorous enough to bump solidity |

## Skills firing on this workstream

- **`ave-prereg`** (Phase 0 mandatory — corpus-grep before any derivation)
- **`pre-test-physics-check`** (Phase 0 — one plumber-physical question to Grant before framing locks)
- **`ave-canonical-leaf-pull`** (Phase 0+ — enumerate canonical leaves for the chosen sub-item)
- **`ave-analytical-tool-selection`** (Phase 0+ — Mode/Boundary class for (2,3) uniqueness)
- **`consistency-vs-emergence`** (Phase 0+ — classify the derivation type before writing)
- **`phase-space-coordinate-check`** (Phase 1+ — CRITICAL for any (2,3) test/derivation; (2,3) is a phase-space pattern)
- **`verify-before-cite`** (continuous)
- **`ave-evidence-framing-discipline`** (continuous)
- **`ave-directory-enumeration-discipline`** (continuous for counts)
- **`substrate-native-check`** (Phase 1+ if numerical work)
- **`ave-canonical-source`** (Phase 1+ if Python scripts written)
- **`ave-handoff-canonical-locale`** (this doc lives at canonical locale ✓)

## Branch + commits

- **Branch**: `analysis/golden-torus-alpha-strengthen` (off `main` @ `c655526b`)
- **Commits**: (none yet)
- **Audit tags planned**: `audit/<date>_clm-0ktpcn-golden-torus-alpha-strengthen-phase-N` at each phase boundary

## Cross-references

- Claim entry: [`manuscript/ave-kb/vol1/claim-quality.md`](../manuscript/ave-kb/vol1/claim-quality.md) (clm-0ktpcn)
- Canonical leaf: [`manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md`](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md)
- LaTeX source: [`manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex`](../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex)
- Pre-reg (Phase 0 deliverable): `research/2026-05-25_clm-0ktpcn-golden-torus-alpha-strengthen-prereg.md` (PENDING)
- Closure-roadmap status-dashboard row: PENDING addition

## Failure-mode awareness

This workstream involves derivation work on the highest-leverage shaky claim. Failure modes to watch:

- **Solidity 0.45 → "not really moved"**: closing 1 of 4 sub-items doesn't necessarily promote solidity to 0.65; depends on which sub-item and how much the rationale block's "load-bearing structural elements as not established" softens.
- **Over-claim**: deriving (2,3) from a "uniqueness argument" that's actually a plausibility argument or a post-hoc selection. `ave-evidence-framing-discipline` should catch.
- **Wrong-coordinate test design**: testing (2,3) properties in real-space coordinates when the claim is phase-space. `phase-space-coordinate-check` should catch.
- **Cherry-pick from corpus**: finding a prior corpus argument that LOOKS like a derivation but actually re-asserts the (2,3) selection. `ave-prereg` corpus survey should catch.
- **Independence-check failure**: claiming N "independent reasons" for (2,3) that turn out to be algebraically derivable from each other. `ave-independence-check` discipline applies.

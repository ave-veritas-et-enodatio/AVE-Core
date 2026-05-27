# Epic: clm-0ktpcn Golden Torus α Strengthening

**Status**: PHASE 2 ALL SUB-ITEMS COMPLETE (4/4 strengthen-by items on clm-unk0bd closed)
**Target claim**: `clm-0ktpcn` — Golden Torus α Derivation (Three-Regime Closure)
**Branch**: `analysis/golden-torus-alpha-strengthen` off `main` @ `c655526b`
**Workstream started**: 2026-05-25
**Phase 1 completed**: 2026-05-25 — 8 claims propagated 0.45 → 0.50 via depends-on cascade after closing sub-item 2 (FM chain promotion); commit `226241cd` + tag `audit/2026-05-25_clm-0ktpcn-phase-1-fm-chain-promotion`
**Phase 2 sub-item 1 completed**: 2026-05-25 — (2,3) torus-knot uniqueness derivation bridged into clm-unk0bd + clm-0ktpcn depends-on cone via Path A1+tweak chain promotion (no new leaf; canonical home is `torus-knot-uniqueness.md` / clm-8c3yhs). Confidence bumps clm-unk0bd 0.50 → 0.55, clm-0ktpcn 0.50 → 0.55. Option β follow-on wired 4 downstream claims (clm-jupq56, clm-mnb3lt, clm-k6olj8, clm-cmic3e) into the (2,3)-uniqueness depends-on cone for graph symmetry; clm-to41c7 NOT wired per Grant Option-1 adjudication. 12-claim cascade; verify PASS on 692 files / 281 claims / 682 depends-on edges. Commit `f80a5f46` + tag `audit/2026-05-25_clm-0ktpcn-phase-2-sub-item-1-23-uniqueness-chain-promotion`.
**Phase 2 sub-items 3+4 completed**: 2026-05-25 — photon-720° compatibility closed via new §6.5 in FM leaf (two arguments: FM extended-defect requirement + Hopf-fibration projection drops U(1) fibre); topological-protection caveat closed via depends-on edge clm-unk0bd → clm-zuf7g1 (K4-TLM 32³ simulation empirical protection below T_pair; topology change above T_pair via canonical Schwinger pair creation). Confidence on clm-unk0bd bumps 0.55 → 0.65 (closing all 4 strengthen-by items: FM derivation, (2,3) uniqueness, photon-720°, topological protection). Solidity stays at 0.55 because clm-zuf7g1 at solidity 0.55 introduces a new dep-cap; strengthening clm-zuf7g1 is the next move to lift the cascade further. Auditor returned HOLD with 4 amendments (Möbius framing not strawman-retracted; L3 doc 06 → 07 supersession acknowledged; same-leaf hosting flagged; solidity-vs-confidence clarified); all 4 applied; second auditor pass returned COMMIT.

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
| **2+** | Sub-items 1/3/4 (remaining 3 of 4 strengthen-by items on clm-unk0bd) | sub-item 1 ((2,3) uniqueness) ✓ COMPLETE 2026-05-25 via Path A1+tweak chain promotion + Option β downstream wirings; sub-items 3 (photon-720°) + 4 (protection mechanism) remain PENDING |

## Phase 2 sub-item 1 — (2,3) uniqueness chain promotion (2026-05-25)

**Path chosen**: A1+tweak (pure chain promotion + one content tweak; no new leaf). Existing `vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md` (clm-8c3yhs, confidence 0.70) already contained the substantive derivation (§1-9: enumeration table + coprimality + both-windings-≥2 + minimality + electron-is-lightest premise). The structural fix was the missing depends-on edges into clm-unk0bd + clm-0ktpcn, not a new leaf — file-churn discipline applied (CONVENTIONS.md INVARIANT-S7: leaves are canonical, don't multiply files).

**Skills compliance check fired before edits**: ave-prereg ✓, pre-test-physics-check ✓, ave-handoff-canonical-locale ✓, verify-before-cite ✓ (rescued corpus-grep agent miss of 2026-05-18 prime-N work via direct git-log on analysis/integration), ave-canonical-leaf-pull ✓ (enumerated 5 prior leaves), consistency-vs-emergence ✓ (Class 2 axiom-manifestation), phase-space-coordinate-check ✓ (3 coordinate systems separated: real-space 0_1 unknot ≠ phase-space (2,3) Clifford-torus ≠ (p,q) charge-counting label), ave-independence-check ✓ (3 premises non-circular with clm-0ktpcn: coprimality, minimality, electron-is-lightest), ave-discipline-translate explicitly NOT firing (no classical-physics borrowed framing).

**Edits landed**:

1. `manuscript/ave-kb/vol1/claim-quality.md` clm-unk0bd — added depends-on clm-8c3yhs; removed resolved strengthen-by item; updated rationale; confidence 0.50 → 0.55.
2. `manuscript/ave-kb/vol1/claim-quality.md` clm-0ktpcn — added direct depends-on clm-8c3yhs (the (2,3) winding is load-bearing in regimes (b) self-avoidance AND (c) half-cover, so direct edge beyond transitive-via-clm-unk0bd is semantically appropriate); removed resolved strengthen-by item; updated rationale; confidence 0.50 → 0.55.
3. `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md` — added INVARIANT-F1 `> → Primary:` cross-ref to torus-knot-uniqueness.md right after the "Topological identity of the electron" header where (2,3) is first declared in the chapter.
4. `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md` — added self-aware "Bridging role of this leaf" callout in header documenting it is canonical home for the (2,3) uniqueness derivation that clm-unk0bd + clm-0ktpcn depend on; updated path-stable frontmatter to reflect the 2026-05-25 Phase 2 sub-item 1 wiring.

**Auditor review** (ave-auditor): "COMMIT WITH MINOR AMENDMENT." 8 findings — 6 PASS, 2 WARN (non-blocking). Both warnings addressed in Option β follow-on (4 downstream wirings) or queued for separate workstream (Q2 stale narrative-tail breadcrumb cleanup on cascaded entries from prior sessions).

**Option β downstream wirings** (Grant Q1 adjudication):

5. `manuscript/ave-kb/vol2/claim-quality.md` clm-jupq56 (substrate-perspective-electron) — added depends-on clm-8c3yhs (K4-phasor Layer 3 IS the (2,3) phase-space winding; genuine content-load dependency).
6. `manuscript/ave-kb/vol2/claim-quality.md` clm-mnb3lt (proton mass eigenvalue) — added depends-on clm-8c3yhs (the (2,5) cinquefoil assignment rests on the (2,q_odd) ladder starting at (2,3); structural-convention dependency; no solidity impact — clm-mnb3lt already at 0.55).
7. `manuscript/ave-kb/vol2/claim-quality.md` clm-k6olj8 (torus knot baryon ladder) — added depends-on clm-8c3yhs (auditor's primary downstream target; (2,q_odd) family math rests on same coprimality + minimality foundation).
8. `manuscript/ave-kb/vol2/claim-quality.md` clm-cmic3e (proton-identification) — added depends-on clm-8c3yhs ((2,5) "next after electron's (2,3)" structural framing).

**clm-to41c7 NOT wired (Grant Option-1 adjudication)**: Torus Knot Baryon Forward Predictions (2,17/19/21), confidence 0.85, solidity 0.85. Wiring would have capped solidity at min(0.85, 0.70) = 0.70 — a real epistemic drop. Decision: the (2,17/19/21) MeV predictions' physical math doesn't load on (2,3) being the electron specifically — it loads on (2,q_odd) coprimality (the q-ladder math). This is a *structural-convention* reference to (2,3) as ladder starting point, not a *content* dependency. depends-on graph is binary; flagship forward-prediction claim should not be capped by a structural-convention dependency. Solidity 0.85 preserved.

**Refresh + verify pipeline**: 12-claim solidity cascade through depends-on graph (clm-unk0bd, clm-0ktpcn, clm-5xon03, clm-2dwzib, clm-3kzmt9, clm-8ep2b4, clm-zw6mut, clm-b2anl4, clm-82dxbj, clm-ibfyda, clm-m7qd0w, clm-zi6t1e all bumped 0.50 → 0.55). `make verify-kb-metadata` PASS on 692 files / 281 canonical entries / 682 depends-on edges (+4 new edges from Option β) / 0 failures.

**Queued follow-ons**:
- Sub-item 3: Photon-720° compatibility determination ("deferred to post-porting review").
- Sub-item 4: Topological-protection mechanism (real-space-trivial vs phase-space-winding-as-protection).
- Q2 cleanup: stale narrative-tail breadcrumbs on cascaded entries (clm-5xon03 "drops to 0.28", clm-3kzmt9 "0.50 to 0.25", clm-zw6mut "solidity 0.40", clm-b2anl4 "from 0.41 to 0.31") — leftovers from prior sessions, now inconsistent with current 0.55 solidity lines. Separate maintenance commit.
- Path B framing extension (Grant insight 2026-05-25): "photon → (2,3)-mode propagation on K4 → closure at saturation → electron" framing may bypass Faddeev-Skyrme variational analysis for Path B. Maps to AVE-canonical pair-production-axiom-derivation.md + mass-closure-theorem.md + electron-identification.md "self-trapped photon" canonical identity at high fidelity. Novel piece: whether K4 transverse EM modes are ALREADY (p,q)-classified in the linear regime (vs only emerging at closure). Worth a future single-leaf "K4 transverse-mode classification → (2,q) closure mapping" workstream, separate prereg. Banked as queued framework-extension candidate.

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

## Phase 3 plan — clm-0ktpcn own-confidence strengthening (2026-05-26 forward)

**Context update (post-Phase 2-A close 2026-05-26)**: cascade math from `clm-zuf7g1-strengthen.md` confirms:
- Phase 2-A closed (master-equation-derivation-path of quadratic-in-amplitude boundary-Joule extraction-rate scaling; the standard community calls this "Born rule p=2") → cascade lifted clm-zuf7g1 + clm-unk0bd + clm-5xon03 from 0.55 → 0.65
- **clm-0ktpcn stays at solidity 0.55** because its own confidence is still 0.55 (the dep-gate is no longer the cap; clm-0ktpcn's own confidence is now the cap)
- Therefore: the next solidity-lift lever on clm-0ktpcn is **strengthening clm-0ktpcn's own confidence**, not lifting a dependency

This is a different shape of workstream than Phases 1+2 (which were chain-promotions via clm-unk0bd). Phase 3 attacks clm-0ktpcn's own strengthen-by list directly.

### clm-0ktpcn's own strengthen-by list (per `claim-quality.md` clm-0ktpcn block)

Per the canonical 2026-05-25 entry, clm-0ktpcn's own 4-item list (DIFFERENT from clm-unk0bd's list addressed in Phases 1+2):

1. **Sum-decomposition orthogonality** — the multipole sum that yields $4\pi^3 + \pi^2 + \pi$ assumes orthogonal contributions from the three regimes (Nyquist + crossings + screening). Currently asserted; needs Schur orthogonality demonstration or analogous orthogonal-basis argument.
2. **A1 prose reframe** — the chapter's "derivation" prose blends derivation-from-axioms with reverse-engineering-from-CODATA. Reframe the chapter prose to clearly separate Class 2 axiom-manifestation steps from Class 4 consistency checks (per `consistency-vs-emergence` v1.2 master-equation-derivation-path discipline).
3. **δ_strain magnitude derivation** — the saturation strain δ_strain that appears in the three-regime closure as a substrate-physics parameter is asserted at order-of-magnitude rather than derived from Ax 4 (saturation kernel) parameters. Multi-step derivation: K4 lattice spacing × saturation-onset amplitude ratio → δ_strain.
4. **Q2 cleanup** — stale narrative-tail breadcrumbs on cascaded claim-quality entries (clm-5xon03 "drops to 0.28", clm-3kzmt9 "0.50 to 0.25", clm-zw6mut "solidity 0.40", clm-b2anl4 "from 0.41 to 0.31") — leftovers from prior sessions inconsistent with current 0.55/0.65 lines. Pure hygiene, no derivation.

### Phase 3 sub-phase plan

| Sub-phase | Goal | Status | Spawn shape |
|---|---|---|---|
| **3-Q2** | **Pre-clean stale narrative breadcrumbs on 4 cascaded claim-quality entries (no derivation; hygiene only)** | OPEN — fastest closure, parallel-safe with 3-A1 / 3-A2 | Single implementor; ~30-min hygiene pass; no auditor needed |
| **3-A1** | **Prose reframe of ch8 chapter to separate Class 2 axiom-manifestation steps from Class 4 consistency checks** per consistency-vs-emergence v1.2 master-equation-derivation-path discipline | OPEN — likely combinable with 3-Q2 (same files, similar mechanical-edit shape) | Combined implementor with 3-Q2 (sub-agent A) recommended for batching |
| **3-A2** | **Attempt Schur orthogonality argument for the sum-decomposition** — if orthogonality is genuinely Schur-derivable, this lifts confidence 0.55 → 0.65; if not, walk back the "sum is orthogonal" framing | ✓ CLOSED 2026-05-26 — WALK-BACK with structural reframe; confidence STAYS at 0.60; substrate-mechanism path identified (Op21 multi-mode mode-counting at Γ=-1 saturation boundary); strengthen-by item REFORMULATED from Schur to Op21-formalization. Branch `analysis/clm-0ktpcn-phase-3-A2-schur-orthogonality` pushed; PR pending orchestration session. See §"Phase 3-A2 execution log (2026-05-26)" below | Standalone implementor (sub-agent B) per epic brief; spawned 2026-05-26 |
| **3-A3** | **δ_strain magnitude derivation from Ax 4 saturation kernel parameters** — independent of 3-A2 result | OPEN — deferred to Phase 4 unless 3-A2 walks back and we need a different lift lever | Future workstream |
| **3-A4 (NEW, surfaced by Phase 3-A2)** | **Promote Op21 multi-mode generalization from paragraph-level statement (`theorem-3-1-q-factor.md` §Op21) to fully-derived canonical leaf** — formalize Nyquist-cell-count additivity at Γ=-1 saturation boundary as substrate-mechanism path for three-Λ assembly, with step-by-step trace to Ax 1 + Ax 3 + codimensional mode-category independence | OPEN — this is the actual remaining open derivation step on clm-0ktpcn after Phase 3-A2 WALK-BACK closure | Future workstream; could be standalone implementor |
| **3-A5 (NEW, surfaced by Phase 3-A2 — speculative)** | **Identify canonical substrate Hilbert space on which T = A_4 acts with irrep decomposition A + E + T (dims 1+2+3)** — if such a substrate Hilbert space can be identified and the (R, r, d)-fixed substrate kernel decomposes onto its irreps, Schur orthogonality WOULD close the additive assembly at Class 2 axiom-manifestation level | OPEN — substantive future workstream, NOT a near-term tweak; Phase 3-A2 surfaces this as the most promising structural-match candidate among the explored alternatives | Future workstream; requires substantive group-theory + substrate-Hilbert-space work |

### Phase 3a-A1+Q2 combined brief (implementor sub-agent A)

**Scope**: prose reframe of `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md` to apply consistency-vs-emergence v1.2 discipline (separate Class 2 axiom-manifestation from Class 4 consistency at the prose level), PLUS Q2 hygiene cleanup of stale narrative-tail breadcrumbs on 4 cascaded claim-quality entries.

**Why combined**: both are mechanical-edit shape (no derivation), both touch claim-quality.md, both benefit from one auditor pass at end. Estimated combined effort ~2 hours; parallel-safe with 3-A2 spawn.

**Files in scope**:
- `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md` — chapter prose reframe (3-A1 main work)
- `manuscript/ave-kb/vol1/claim-quality.md` — 4 entries (clm-5xon03 / clm-3kzmt9 / clm-zw6mut / clm-b2anl4) breadcrumb cleanup (3-Q2)
- `manuscript/ave-kb/vol1/claim-quality.md` — clm-0ktpcn strengthen-by list update (remove 3-A1 + 3-Q2 items as closed)

**Expected confidence lift**: 0.55 → 0.60 (prose-reframe alone, no derivation). Pairs with 3-A2 success (orthogonality argument) to potentially lift further to 0.65.

**Skills expected to fire**:
- `consistency-vs-emergence` v1.2 — the DRIVING skill; the reframe IS application of the v1.2 derivation-path-tracing discipline
- `verify-before-cite` — every file:line citation grep-verified
- `ave-evidence-framing-discipline` — "derived" vs "matches" vs "consistent-with" precision (this is the main editorial task)
- `ave-canonical-leaf-pull` — pull ch8 + Nyquist + crossings + screening leaves before reframing
- `ave-directory-enumeration-discipline` — accurate counts on entries cleaned
- `ave-walk-back` v1.1 Type E — likely fires for any value-amendment caught mid-reframe

**Auditor pass**: ave-auditor after edits; confirm reframe doesn't accidentally walk back the (R,r,d) derivation itself; confirm Q2 cleanups don't break any other cross-references.

**Branch**: `analysis/clm-0ktpcn-phase-3-A1-Q2-prose-reframe` off `main` @ post-PR-38-merge.

### Phase 3a-A2 brief (implementor sub-agent B — standalone, parallel-safe)

**Scope**: attempt Schur orthogonality (or alternative orthogonal-basis argument) for the three-regime sum-decomposition (Nyquist + crossings + screening contributing additively, orthogonally, to $\alpha^{-1} = 4\pi^3 + \pi^2 + \pi$).

**Why a standalone implementor**: this is genuine derivation work, not mechanical reframe. Either Schur orthogonality goes through (closing the gap, lifting confidence) or it doesn't (walk-back). The result drives the Phase 3 confidence lift independent of 3-A1+Q2.

**Pre-survey corpus-grep targets (mandatory before deriving)**:

```bash
grep -rn "Schur\|orthogonal.*decomposition\|multipole.*sum\|4 pi\^3\|4π³\|three.*regime" \
  manuscript/ave-kb/vol1/ research/_archive/L3_electron_soliton/
grep -rn "orthogonality\|orthogonal basis\|Peter-Weyl" manuscript/ave-kb/ research/
```

Likely already-canonical anchors:
- `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md` — sum decomposition lives here
- `research/_archive/L3_electron_soliton/` — possibly some L3 doc has a prior orthogonality attempt
- Group-theory leaves (if any) — SU(2) representation theory has Schur orthogonality as canonical theorem

**What I expect (forward pre-registration)**:

The three regimes correspond to distinct symmetry sectors of the phase-space (2,3) Clifford-torus mode space:
- Regime (a) Nyquist — lattice-cutoff sector (Ax 1 discrete spacing)
- Regime (b) Crossings — self-avoidance sector (Ax 2 ν_vac geometric prefactor)
- Regime (c) Screening — half-cover topological sector (Ax 3 spinor structure / SU(2)→SO(3))

If these correspond to orthogonal irreducible representations of the relevant symmetry group (likely the substrate's tetrahedral or octahedral symmetry group acting on the (2,3) torus mode space), Schur orthogonality applies AT THE GROUP-THEORY LEVEL, not as an ad-hoc orthogonality assumption.

If yes → derivation closure, confidence 0.55 → 0.65 (+0.05 for 3-A1 prose reframe, +0.05 for 3-A2 orthogonality derivation).

If the symmetry decomposition doesn't go through cleanly → walk back the "orthogonal sum" framing in chapter prose; reframe as "additive at leading order with documented sub-leading corrections", confidence stays at 0.55 (or drops to 0.50 if the walk-back exposes a load-bearing assumption).

**Adjudication criteria (PASS / WALK-BACK / RESCOPE)**:

- **PASS**: Schur orthogonality (or alternative orthogonal-basis argument) derives the sum-decomposition rigorously. Confidence lift 0.55 → 0.60 (3-A2 alone) or 0.55 → 0.65 (paired with 3-A1).
- **WALK-BACK**: orthogonality not derivable; reframe as additive-at-leading-order; document honestly. No solidity lift. Trigger ave-walk-back Type D (mechanism re-scope) propagation.
- **RESCOPE**: derivation gets stuck on a sub-problem (e.g., the symmetry group acting on (2,3) torus mode space isn't fully canonical in the AVE corpus). Spin off a sub-prereg to identify the symmetry group, then return to orthogonality.

**Skills expected to fire**:
- `ave-prereg` — corpus-grep as above
- `ave-canonical-leaf-pull` — ch8 + Schur + group-theory + multipole leaves
- `ave-analytical-tool-selection` — Mode class (irreducible-rep decomposition); check `ave-analytical-toolkit-index.md`
- `ave-discipline-translate` v1.1 — Schur orthogonality is a compact-group representation-theory theorem (substrate-applicable to any compact symmetry group acting on the substrate mode space); the substrate-native framing is "decomposition into orthogonal eigenspaces of the substrate's tetrahedral/octahedral symmetry group acting on the (2,3) Clifford-torus mode space". The standard-physics community uses Schur orthogonality in QM representation-theory contexts; check `translation-qm.md` to confirm the substrate-native usage doesn't conflict with canonical translations. Trigger 6 fires during prose composition; substrate-native vocabulary mandatory throughout
- `substrate-native-check` — symmetry group must come from K4-TLM substrate structure, not imported from particle-physics convention
- `consistency-vs-emergence` v1.2 — explicit Class 2 vs Class 4 classification; orthogonality derivation IS Class 2 if symmetry group emerges from substrate, Class 4 if imported
- `phase-space-coordinate-check` — group acts on (2,3) phase-space mode space, not real-space; coordinate distinction critical
- `ave-independence-check` — three regimes claimed as INDEPENDENT contributions; verify via Schur (or document non-independence honestly)
- `ave-evidence-framing-discipline` — "derived" vs "asserted" precision
- `ave-walk-back` v1.1 Type E — likely fires for any value-amendment caught mid-derivation
- `ave-discrimination-check` — SM-counterfactual + interpretive-alternatives before asserting "AVE-native derivation"

**Branch**: `analysis/clm-0ktpcn-phase-3-A2-schur-orthogonality` off `main` @ post-PR-38-merge.

### Honest closure-probability estimate

- 3-A1+Q2 combined: ~85% probability of clean closure (mechanical work; main risk is the auditor catching prose-precision gaps that need ave-walk-back Type E sweeps)
- 3-A2 standalone: ~40% probability of Schur closure; ~60% probability of walk-back with honest reframe (still a valuable outcome — corpus gets more honest)

Combined Phase 3 expected confidence lift: 0.55 → 0.60-0.65 (probability-weighted).

### Phase 3-A2 execution log (2026-05-26)

**Branch**: `analysis/clm-0ktpcn-phase-3-A2-schur-orthogonality` off `main` @ `453c335e`

**Verdict**: **WALK-BACK with structural reframe**. The Schur-orthogonality-strict hypothesis is NOT the load-bearing theorem; the substrate-mechanism path is Op21 multi-mode mode-counting at the $\Gamma = -1$ saturation boundary, canonical (paragraph-level) at `theorem-3-1-q-factor.md` §"Op21 multi-mode generalization". Outcome lands in the ~60% pre-registered walk-back probability band.

**Commits**:

1. `3de0b411` — `research(clm-0ktpcn): Phase 3-A2 pre-registration — Schur orthogonality attempt for sum-decomposition` (266 lines; 12 corpus anchors identified; 4 routes pre-registered)
2. `21aa99ae` — `research(clm-0ktpcn): Phase 3-A2 result — WALK-BACK with structural reframe (Schur not achievable, Op21 mode-counting IS the substrate path)` (265 lines; full route-by-route walkthrough + honest classification + discrimination check + independence check + phase-space-coordinate check + self-audit checklist)
3. `6217411b` — `kb+research(clm-0ktpcn): Phase 3-A2 WALK-BACK closure — Op21 mode-counting reframe of additive-assembly framing` (chapter prose reframe at 3 sites in ch8-alpha-golden-torus.md + clm-0ktpcn rationale append + strengthen-by reformulation + auto-regenerated index)
4. (this commit) — `orch(clm-0ktpcn): Phase 3-A2 execution log + epic doc update`

**Key findings**:

1. **Schur orthogonality (specific theorem-anchor named in original strengthen-by item) is NOT achievable** as a Class 2 substrate-mechanism step. The canonical substrate group action ($T_d$ on $V_{\text{4-port}}$ per `k4-port-irrep-decomposition.md`) gives 2 irreps ($A_1 \oplus T_2$, dims $1 + 3 = 4$), not three irreps matching the $1 + 2 + 3$ codimensional ordering of $\Lambda_{\text{line}}, \Lambda_{\text{surf}}, \Lambda_{\text{vol}}$. No canonical substrate Hilbert space carrying a three-irrep decomposition was found in the corpus survey.

2. **Op21 multi-mode mode-counting at the $\Gamma = -1$ saturation boundary IS the substrate-mechanism path**. The substrate-mechanism content traces to Ax 1 (Nyquist cell size in natural units) + Ax 3 (saturation TIR mode-leak fraction $1/\ell$) + codimensional mode-category independence (volume cells, surface cells, line cells are mutually exclusive Nyquist-cell categories). This is **already canonical** at `theorem-3-1-q-factor.md` §"Op21 multi-mode generalization" — Phase 3-A2's contribution is recognizing this as the load-bearing theorem-anchor and cross-citing it from `ch8-alpha-golden-torus.md`.

3. **The $(R \cdot r)$-collinearity issue is reframed**: $\Lambda_{\text{vol}} / \Lambda_{\text{surf}} = 4\pi$ IS the spinor-temporal phase factor (substrate SU(2) double-cover per ch8 line 105), consistent with substrate-mechanism mode-category independence even where $(R, r)$ parameter-space collinearity holds. The strengthen-by item's "nested supports defeat domain-disjointness" objection is partially correct (point-set supports are nested) but overstated — mode categories at the saturation boundary are mutually exclusive Nyquist-cell categories even where point-set supports are nested.

4. **Confidence STAYS at 0.60**. No derivation-rigor improvement because the substrate-mechanism path was already canonical (Op21 multi-mode generalization), just under-cited from ch8 before this commit. The strengthen-by item is reformulated from "Schur orthogonality" to "promote Op21 multi-mode generalization to fully-derived canonical leaf" — same physics, accurate theorem-anchor.

**Newly-opened workstreams** (queued, not in Phase 3-A2 scope):

- **Phase 3-A4**: Promote Op21 multi-mode generalization from paragraph-level statement to fully-derived canonical leaf (the actual remaining open derivation step replacing the Schur framing).
- **Phase 3-A5** (speculative): Identify canonical substrate Hilbert space on which $T = A_4$ acts with irreps $A + E + T$ (dims $1 + 2 + 3$ matching codimensional ordering). If such a Hilbert space exists and the (R, r, d)-fixed substrate kernel decomposes onto its irreps, Schur orthogonality WOULD close at Class 2. This is a substantive future workstream, not a near-term tweak — Phase 3-A2 establishes it as the most promising structural-match candidate.

**Pollution check**: pre-commit `git diff --cached --stat` scope-screening was run for each of the three commits during Phase 3-A2 execution. No out-of-scope files committed. Worktree-isolation discipline maintained (all file edits in `/Users/grantlindblom/AVE-staging/AVE-Core/.claude/worktrees/agent-ac6b94f2cbade9ce4/`, no edits at parent path `/Users/grantlindblom/AVE-staging/AVE-Core/`).

**Verify pipeline (pre-push)**:
- `make refresh-kb-metadata`: 0 leaf-claim / solidity changes; 1 .index regeneration (strengthen-by 2→3 items)
- `make verify-kb-metadata`: PASS (694 files, 281 canonical entries)
- `make verify-md-links`: my new docs link-clean; only pre-existing broken links in older research docs remain
- `make verify`: ALL PHYSICS PROTOCOLS PASSED (predictions WARN unrelated, 3 unbridged manifest entries pending separate migration)

**Self-audit verdict**: PASS. Honest closure per Rule 11; substitution-not-retraction per Rule 12; all skill firings documented; cross-agent pollution check passed. Push branch ready for orchestration session PR open.

### Spawn protocol (orchestration session)

Per CLAUDE.md "Pre-commit discipline" + "Spawning implementors via the Agent tool":

```python
# Sub-agent A (3-A1+Q2 combined) — spawn in worktree
Agent(
    description="clm-0ktpcn Phase 3-A1+Q2 implementor",
    subagent_type="ave-implementer",
    isolation="worktree",  # CRITICAL: prevents branch-state leak into orchestration tree
    prompt="<full brief from Phase 3a-A1+Q2 section>"
)

# Sub-agent B (3-A2 Schur) — spawn in worktree, parallel
Agent(
    description="clm-0ktpcn Phase 3-A2 Schur orthogonality implementor",
    subagent_type="ave-implementer",
    isolation="worktree",
    prompt="<full brief from Phase 3a-A2 section>"
)
```

Both sub-agents push their branches but do NOT merge (per session-conventions). Orchestration session does `--no-ff` merge with audit-tag + branch-cleanup pattern.

## Failure-mode awareness

This workstream involves derivation work on the highest-leverage shaky claim. Failure modes to watch:

- **Solidity 0.45 → "not really moved"**: closing 1 of 4 sub-items doesn't necessarily promote solidity to 0.65; depends on which sub-item and how much the rationale block's "load-bearing structural elements as not established" softens.
- **Over-claim**: deriving (2,3) from a "uniqueness argument" that's actually a plausibility argument or a post-hoc selection. `ave-evidence-framing-discipline` should catch.
- **Wrong-coordinate test design**: testing (2,3) properties in real-space coordinates when the claim is phase-space. `phase-space-coordinate-check` should catch.
- **Cherry-pick from corpus**: finding a prior corpus argument that LOOKS like a derivation but actually re-asserts the (2,3) selection. `ave-prereg` corpus survey should catch.
- **Independence-check failure**: claiming N "independent reasons" for (2,3) that turn out to be algebraically derivable from each other. `ave-independence-check` discipline applies.

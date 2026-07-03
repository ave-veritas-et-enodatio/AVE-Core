# Cold-Eyes Program Audit — the 2026-07-03 ruling chain, open-list completeness, next allocation

**Date:** 2026-07-03 · **Type:** INSTRUMENT-AUDIT / meta (fresh-context adversarial review of the orchestrator's own synthesis) · **Verification posture:** all citations re-verified at `origin/main` HEAD `67504dc9` by the implementer landing this doc (verify-before-cite; the auditor lanes ran read-only at the same HEAD).

> **What this doc is.** A **meta-audit record**, not a physics result. On 2026-07-03 a single orchestrated session merged PRs #476–#494 (the EM-readout epic's four-lock cascade, the D1 srs-z3 ratification, the AC/DC carve, the G2 photon relabel, lanes Z + W). Three fresh-context auditor lanes — with no access to the orchestrator's chat narrative — audited that synthesis for circularity, open-list completeness, and next-allocation soundness. This doc canonizes their findings (condensed, file:line re-verified) and records the framing adjudication they surfaced to Grant. It mints **no** new physics claim; it grades the evidentiary and framing standing of the day's synthesis. Tagged INSTRUMENT-AUDIT/meta, consistency-class.

## 0. Methodology

Three read-only auditor lanes, each dispatched fresh-context (no orchestrator narrative, no shared session state), all working at `origin/main` HEAD `67504dc9`:

- **Lane 1 — ruling-chain circularity audit.** Is the day's adjudication chain (D1 ratification → localization re-adjudication → exposure sweep → four-lock cascade → AC/DC carve → G2 relabel) a real circle, or benign dependence? Where is the single point of maximum blast?
- **Lane 2 — forgotten-opens sweep.** Is the "what's left open" list materially complete, or does narrative-saturation hide load-bearing open items?
- **Lane 3 — strategy + closure-framing challenge.** Is the proposed next-allocation ranking sound, and does the proposed epic-closure framing match the charter's pre-registered outcome branches?

The three-lane redundancy is the immune-system pattern (MEMORY: multi-lane orchestration): the shared failure-mode a single reviewer misses is the seductive synthesis narrative, caught here by an adversarial lens reading the operative claim registers rather than the prose summary.

## 1. Findings — Lane 1 (ruling-chain circularity)

**Verdict: BENIGN-DEPENDENCE, not REAL-CIRCLE.** The chain is not bootstrapped by the day's srs-favorable arcs; but the "four independent locks" headline over-counts and the AC/DC carve's "empirical validation" is mildly circular.

- **D1's true independence is the PRE-SESSION 2026-06-25 Grant ratification, not the day's arcs (MAJOR).** srs-z3 as production carrier was already ratified by Grant on 2026-06-25 — verified verbatim at [`unified-engine-design-doctrine.md:211`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/unified-engine-design-doctrine.md): *"Decision 1 (RATIFIED, Grant 2026-06-25): the production engine substrate is the chiral z=3 srs net."* The 2026-07-03 "ratification" is a re-confirmation + a deferred wording restoration. So D1 is NOT bootstrapped by the day's srs-favorable arcs — the arcs supplied confirming instrument evidence for a decision substantially already made. This is the load-bearing reason the chain is not a real circle. **Corrective (landed):** the D1 memo addendum foregrounds the 2026-06-25 anchor as the PRIMARY independence (deliverable 3c).

- **The srs positive control is BENIGN-DEPENDENCE, not the feared circle (MINOR).** The srs positive control ("a localized L_srs eigenmode stays localized under L_srs dynamics") is self-referential by construction (an eigenmode is a persistent mode by definition) — but it is tagged INFRASTRUCTURE not physics, its only job is instrument-liveness, and the load-bearing D1 evidence is the diamond-side nullspace pathology reproduced by an operator-AGNOSTIC diagnostic (`spectral_liveness.py` accepts either operator). Load-non-bearing for the ratification.

- **"Four INDEPENDENT locks" OVERSTATES: ~2 independent physical closures (MAJOR).** The cascade leaf's own unification paragraph concedes it: Locks 1–2 are instrument-class (the leaf tags them "INSTRUMENT-AUDIT" / "INSTRUMENT/identity"), and Locks 3–4 are "one theorem operating twice." The genuinely-independent physical closures are (A) Lock 3's maximum principle (a texture is not a source) and (B) the ∂₁∂₂=0 curl-neutrality (a curl is not a source) — complementary halves of "only the co-exact/gradient sector carries charge." The closure is real; the "4 independent" HEADLINE contradicts the leaf's own honest body. **Corrective (landed):** retitle to "two structural closures + two instrument gates," KEEP-BOTH the original title as superseded (deliverable 3a).

- **The AC/DC carve's "empirical validation" IS mildly circular (MAJOR).** The carve's selection rule (iv) predicts distinctive content lives DC-side or in DC→AC coupling; the cascade's arc designs were steered by exactly that routing logic (Stage-2 survivors routed to lane Z "harmonic-DC" + lane W "DC-linking"). So the cascade "validating" the carve is the carve's own selection rule producing the routing it reads back as confirmation. Mitigant (real): the carve is honestly booked as an ORGANIZING PRINCIPLE not a theorem, floored at solidity 0.55, and the cascade's core facts (∂₁∂₂=0, the maximum principle) are TRUE independent of the carve. Independent validation would be a forward DC→AC FALSIFIER landing (`clm-pp3qwf` E-route birefringence — the non-circular leg). **Corrective (landed):** downgrade "empirical validation" to "consistent-with / illustration"; reserve "validation" for forward-falsifier-class evidence (deliverable 3b).

- **G2 eigenvector read: BENIGN-DEPENDENCE (MINOR).** The G2 relabel runs on the diamond-tetra band-structure operator D1 just demoted, BUT the exposure sweep graded that operator's band-structure use CLASS-2-not-CLASS-1 (the statics Div·Grad nullspace bite does not fire for a dynamical rank-2 eigensolve). The u-fraction-vs-ω-fraction mode-content read is faithful; chirality is not being tested. Independent-enough.

- **SINGLE POINT OF MAXIMUM BLAST — `srs_dec.py` ∂₁∂₂=0; Lock 3 is the firewall (MAJOR).** If ∂₁∂₂=0 were wrong it unwinds Lock 4, the β-arc net-neutrality, the "one theorem twice" unification, lane-Z's harmonic survivor definition, and the Stage-2b continuity closure. Mitigant: it is a combinatorial integer identity (14 gating keepers, `test_srs_dec_operators.py` asserts `int(|∂₁∂₂|.max())==0` EXACT) whose truth depends only on srs being a valid girth-10 graph, NOT on srs being "the vacuum." CRITICAL FIREWALL: Lock 3 (the NO-FLUX maximum principle) does NOT depend on ∂₁∂₂=0 — it is an elementary Dirichlet-energy positivity argument requiring only ε_eff>0 + connectivity. So even a total ∂₁∂₂=0 collapse leaves the STATICS sourced-route closed by Lock 3. The route-closure is robust to its own largest single point of failure.

## 2. Findings — Lane 2 (forgotten-opens sweep)

**Verdict: the day's open-list was materially incomplete.** The consolidated open-gaps ledger (deliverable 4, `_orchestration/index.md`) folds in the missing items. Summary of what was missing:

- The four historical survival-class exposure gaps (Grant-authorized 2026-07-03) — collider-compositeness/LEP-Λ = HIGH severity, the single sharpest exposure; longitudinal energy budget; Ω_freeze; two already landed as in-situ warningboxes.
- The terminal "what IS the electron's charge" framing fork (net-monopole ∇·E vs harmonic-holonomy far-field) — the load-bearing Grant-gated adjudication the whole EM-readout epic routes to.
- The exterior electric-field-profile derivation — OPEN, self-contradictory, ENGINE-BLOCKED ([`vol4/claim-quality.md:1311`](../manuscript/ave-kb/vol4/claim-quality.md): "WHY topological strain equals ℓ_node/r rather than α·ℓ_node/r from first principles is an open multi-week analytical item").
- The srs-migration's real make-or-break — the α/Lorentz-chain re-clearance (a P1 acceptance gate that can HALT the migration), not the ~29-site mechanical inventory.
- The crystalline-vs-amorphous isotropy seam ([`the-abandoned-interior.md:183`](../manuscript/ave-kb/common/the-abandoned-interior.md)) + the owed forward Lorentz/SME-bounds campaign (only 1-of-N channels paid).
- The two freshly-created varactor sector-keying forks (AVE_EE_BENCH form contradiction + L1 memristor cross-sector) — ADJUDICATION-PENDING, born today via the V_SNAP value change.
- Sibling-repo cross-wires (AVE-Fusion V_yield-as-rupture; AVE-Bench-FemtoElectrometer stale sites).
- The auditor-landing backlog + the forward-prediction-register provenance re-grep (hygiene).

## 3. Findings — Lane 3 (strategy + closure-framing)

**Verdict: the physics is solid; the two framing decisions in front of Grant each carried a laundering risk.**

- **The #86 recommendation is stale — two-way back-reaction already LANDED 2026-06-29 (CRITICAL).** [`engine-capability-map.md:139-144`](../manuscript/ave-kb/common/engine-capability-map.md) books "#86 two-way gravitational back-reaction" as PRESENT/landed (2026-06-29, `clm-w5ez6i`, `backreaction.solve_backreaction`, all 4 at-risk gates + recover-GR green). #86 is CONSISTENCY-class (recover-GR, imports G), NOT the DC→AC chord. The actual DC→AC chord candidate is the **F6 irreversible depletion primitive** (UNBUILT, HARD-BLOCKED: a bounded norm-preserving ε→T2 depletion primitive that does not detonate + a ρ_latent numeric prerequisite, both ABSENT). **Corrective (landed):** the open-gaps ledger books #86-as-landed and names F6 as the unbuilt DC→AC chord object (deliverable 4).

- **"Sourcing-peer-with-SM" does not match the charter — the epic landed on BRANCH 3 (CRITICAL).** The charter §2 pre-committed three asymmetric branches; the epic's own leaves land on branch 3 (the lane-Z step-0 note books "[DOORWAY-NO-PINNING] — the charter's 'posited forever' stakes branch fires"). "Sourcing-peer" is a fourth label appearing NOWHERE in the tracked corpus (grep-confirmed zero hits). **Corrective (landed):** the epic closes on charter branch 3, verbatim to the charter (deliverable 2).

- **The topological-quantization surplus is HALF-real (MAJOR × 2).** The integer FORM is derived; the charge-quantization VALUE is imported (the ξ_topo / London-analog conversion — echo). And the counterfactual knife "SM doesn't derive quantization" does NOT cleanly survive the symmetric standard: SM's gauge anomaly cancellation DOES structurally constrain the charge RATIOS of a generation. The honest comparand: BOTH frameworks force the quantization FORM by a consistency/topology argument and import the absolute scale. The genuine AVE surplus is narrower — forced NEUTRALITY (sum(∇·J)=0 exact) + the ball-vs-torus Δb₁ prediction — NOT "quantization SM can't derive." **Corrective (landed):** the peer-with-SM comparison is included as CONTEXT ONLY, the surplus claim halved, the "SM doesn't derive quantization" line retired (deliverable 2).

- **P1-first is mis-sized — α is NOT on the diamond (MAJOR).** The load-bearing α negative (the Q~30.8 cold-cage clean negative, Q=1/α identity) runs on CrystalEngine Cartesian 7-point, NOT diamond — so "re-clear α on srs" is not a migration necessity. The Lorentz leg IS a genuine open re-derivation (diamond-cubic (qℓ)⁴ quartic → chiral-srs point group; it may FLIP). **Corrective (landed):** the next-allocation ranking drops the α leg (α's negative is Cartesian-hosted) and re-scopes Lorentz-on-srs as a genuine re-derivation (deliverable 4).

- **The obscured RANK-1 — the E-route birefringence bench is the corpus's ONLY bankable forward falsifier (MAJOR).** The day's momentum was all internal (consistency/FORM-class, none testable); per AVE's own AC/DC selection rule every internal derivation is peer-by-construction, so the only lane where a chord OR a fatal kill can be earned is DC→AC coupling — and E-route birefringence (`clm-pp3qwf`, HIBEF @ European XFEL) is the one near-term-reachable instrument in that class. **Corrective (landed):** RANK 1 = E-route birefringence bench advancement (deliverable 4).

## 4. The framing adjudication (branch-3, ratified)

The Lane-3 finding surfaced the charter-vs-proposed-grade conflict to Grant (flag-don't-fix). **Grant ratified (2026-07-03, verbatim: "ratify it"):** the EM-readout epic closes on **charter §2 branch 3** — the "posited forever" FORM-level ceiling, named — with the ceiling LOCATED at the London-analog integer→flux-value conversion (the lane-Z pinning ledger). The peer-with-SM comparison is retained as context only, corrected per the halved-surplus finding. See the branch-3 closure booking (deliverable 2): the cascade leaf's closure section, the Ax2 axiom-register row, and the dated outcome annotation in the charter file itself.

## 5. Watch item (carried to Grant, flag-don't-fix)

`clm-nogo4l` is canonized at confidence 0.80 while the net-monopole-vs-holonomy framing fork underneath it is explicitly un-adjudicated (surfaced to Grant, β-note §6). If that fork resolves against the net-monopole reading, the risk is substitution-not-retraction (Rule 12 / A47 v11b). This is honestly disclosed in-corpus; recorded here so the ratification is over the full state, not the headline. The fork is item (ii) of the consolidated open-gaps ledger.

## Disciplines applied

verify-before-cite (all §1–§3 citations re-grepped at HEAD `67504dc9` by the landing implementer) · flag-don't-fix (§4 charter-vs-grade conflict surfaced to Grant, not silently resolved; §5 watch item) · consistency-vs-emergence (this doc is INSTRUMENT-AUDIT/meta, mints no emergence content) · honest-closure / Rule 11 (the branch-3 booking records the FORM-ceiling as the honest state, no rescue).

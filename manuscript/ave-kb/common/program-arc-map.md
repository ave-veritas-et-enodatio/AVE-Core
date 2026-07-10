[↑ Common Resources](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Navigational meta-leaf: the TEMPORAL/causal view of the corpus (which arc opened which question, what killed what, what each verdict unlocked). Originates no derivation and hosts no claim — it is a map over the existing claim graph, the release/tag history, and the orchestration record. The claim-quality register remains the source of truth for every verdict cited here; this leaf only routes to it. Maintained at era boundaries and release tags by orchestration sessions, via PR."
-->

# The Program Arc Map — the historical arc as navigational infrastructure

> ⛔ **This leaf is a MAP, not a diary.** It is the *temporal/causal* view of the AVE corpus: which arc opened which question, what verdict killed what, and what each closure unlocked. The [claim graph](claim-quality.md) is the *logical* view (what depends on what); this leaf is the *causal* view (what came from what). Every verdict quoted here is a pointer — the cited `clm-`/`exp-` entry, PR, audit tag, or research doc is the source of truth. Where this map and a leaf disagree, **the leaf wins and the drift is a bug in this map** (flag it, do not reframe the leaf).

Ratified 2026-07-10 (Grant): *"we need to start treating the historical arch as a map."*

---

## §1 — The Contract (how sessions use this map)

This leaf carries a **navigational contract**, parallel to and extending the `ave-prereg` corpus-grep discipline from the *claim* level up to the *arc* level:

1. **Check before opening an arc.** Before a session opens a new investigative arc, it greps §3 (the Arc Registry) and §5 (Standing Negatives) for a prior traversal of the same territory. `ave-prereg` asks "has this *claim* been made?"; this map asks "has this *question* already been opened, and with what verdict?" A pretty mechanism that a prior arc already killed does not get re-derived; it gets cited.

2. **The anti-repetition function.** §5 (Standing Negatives Index) is the arc-level analogue of the [Genesis / Chord Falsification Ledger](genesis-chord-falsification-ledger.md): a falsified mechanism, once banked, must not be silently re-walked. A new session proposing a mechanism in §5's table must either (a) cite a *new discriminator* the original arc lacked, or (b) not run it. This is Rule 11 (honest closure) enforced across sessions, not just within one.

3. **The open-forks function.** §6 (Standing Open Forks) shows every live question with its *assigned resolution route*. A session picking up a fork checks §6 first for the route already assigned, rather than minting a parallel plan (Rule 16 — corpus + Grant before a new methodology pivot).

4. **Maintenance rule.** This map is updated at **era boundaries** and **release tags** by orchestration sessions, via PR like everything else (no self-merge; `[REVIEW: pending-orchestrator]`). It is deliberately *not* updated per-PR — it is a coarse causal skeleton, not a commit log. When a release ships (`gh release`), the shipping session adds/closes the arcs that release summarizes. Between releases it is allowed to lag; the claim graph, not this map, is the live truth.

**What this map is NOT:** it is not a claim source (INVARIANT-S7 — leaves are canonical; this is a routing aid), not a substitute for reading the cited `clm-` entry, and not a place to litigate a verdict. A verdict changes in its home leaf first; this map follows.

---

## §2 — Era Timeline

The program's coarse phases. Each era's *character* is one line; the release/tag column is the receipt anchor. Windows before `2026-04-13` predate the AVE-Core git history (the repo's initial commit is `de9d2293`, 2026-04-13) and are anchored by the archived electron-soliton thread rather than by git dates.

| Era | Window | Character | Release / tag anchor |
|---|---|---|---|
| **E1 — the spark** | pre-repo → 2026-04-13 | Vacuum as an engineerable EE medium; the K4 / chiral-LC lattice picture; the α⁻¹ = 4π³+π²+π keystone posited as a zero-parameter closure. | initial commit `de9d2293` (2026-04-13); `v0.0` (2026-04-15) |
| **E2 — corpus building** | 2026-04-13 → ~2026-05-15 | Manuscript volumes + engine v1 + the L3 electron-soliton thread (137 `.md` docs, now archived). | `v0.5` "Remerged alpha" (2026-04-19); `research/_archive/L3_electron_soliton/` |
| **E3 — collaboration forms** | (pre-repo) → surfaces 2026-07 | The physics program acquires coauthors; the earliest git-receiptable coauthorship is the three-author Letter. | `v0.7` Letter authorship: G. Lindblom, K. Mertens, B. Herrera |
| **E4 — the honesty turn** | 2026-05-16 → ~2026-06-15 | α keystone resolved = Class-B ECHO; "real chord or echo?" becomes the north star; EE-as-substrate-native ratified; multi-lane adversarial orchestration built. | first audit tag `audit/2026-05-16_*`; `audit/2026-06-02_honest-alpha-relabel` |
| **E5 — the interior gauntlet** | ~2026-06-13 → 2026-06-29 | Sector-ownership canon; genesis energize-lock negative; K=2G = GR-imported; FORM/VALUE meta-finding named; mass sector closed ECHO-final; carrier sector closed-at-peer. Verdict: NO AVE-distinct chord *inside*. | PRs #220, #260–#264, #311, #313–#315, #433–#435 |
| **E6 — the testing pivot** | ~2026-06-22 → 2026-06-24 | Grant pivots to infrastructure-first testing; bench-model spine; birefringence flagship survives PVLAS via circulation-keyed μ (Route C); cleave-01 + impedance-probe primitives scoped. | PR #384; `audit/2026-06-22_*` handoffs; `audit/2026-07-03_birefringence-*` |
| **E7 — the Letter era** | ~2026-07-03 → 2026-07-09 | SVE Letter v1→v5 through 3 adversarial rounds; muonic-H self-kill → static-sector scoping; single-footing 3.75π/α²; NIST XCOM verify; OTS pre-reg chain Bitcoin-anchored; γγ/ATLAS → EFT-domain scoping. | `v0.6` / `v0.7` / `v0.8`; PRs #582–#600 |
| **E8 — the machine-fork nights** | 2026-07-09 / 2026-07-10 | srs band structure closed-form; the PARITY THEOREM; clock / tethered-pivot / node-shunt forks; the **X36→X37→X38 vertex arc** (install-tautology → reactive-low-pass extraction → Op6 point-junction selection); **X41** radiative-scoping-why (UNDERDETERMINED, frozen tie); operator-typing pass; the two navigational maps (arc + lineage); the corrections wave (Cauchy algebra, S₁₁ honesty-lag); breakthrough-patterns methods note (P1–P12). Pretty mechanisms killed / underdetermined-fenced by pre-registered discriminators; Letter v6 round-4. | PRs #603–#627 |

---

## §3 — Arc Registry

The heart of the map. Each arc: the **question as opened** (prove-or-disprove framing), the method, the **verdict + class** (ECHO / negative / derived / degenerate / fork-open / peer / built), what it **closed**, what it **opened**, the **receipts**, and the **successor** arc. Grouped by era. Every PR#, tag, and date below was gh/grep-confirmed this session; rows the receipts could not confirm are marked `[RECEIPT-PENDING]`.

### E1–E2 — spark + corpus building

**ARC-01 · the α keystone (as posited).** Window: pre-repo → E2.
- *Q:* does α⁻¹ = 4π³ + π² + π *derive* α zero-parameter from the K4 / Golden-Torus (2,3) winding geometry?
- *Method:* closed-form geometry of the electron's phase-space winding portrait.
- *Verdict:* **posited-chord** (at the time) — headlined as a zero-parameter closure. Later resolved → ECHO in E4 (see ARC-06).
- *Closed / Opened:* opened the entire keystone question that E4 had to resolve.
- *Receipts:* `v0.5` "Remerged alpha" (2026-04-19); `vol1/ch8-alpha-golden-torus.md`.
- *Successor:* ARC-06 (honest-α relabel).

**ARC-02 · the L3 electron-soliton thread.** Window: pre-repo → archived 2026-07-03.
- *Q:* is the electron a Faddeev–Skyrme / knotted-vortex soliton derivable from the substrate?
- *Method:* a 137-`.md`-doc soliton-synthesis research thread (pre-AVE-Core-repo).
- *Verdict:* **superseded / archived** — folded into the E5 genesis + carrier arcs and finally the electron-def canon.
- *Receipts:* `research/_archive/L3_electron_soliton/` (137 `.md` docs); `audit/2026-07-03_research-l3-electron-soliton`.
- *Successor:* ARC-08 (genesis), ARC-13 (carrier), the electron-def canon (ARC-27).

### E4 — the honesty turn

**ARC-06 · honest-α relabel (keystone → ECHO).** Window: 2026-06-02 → 2026-06-19.
- *Q (prove-or-disprove):* does the substrate *independently force* α's VALUE, or is 4π³+π²+π a calibration identity (echo)?
- *Method:* three named α-lift routes tested — dynamical *selection* (flat); kinematic *bijection* / unit-bridge (Class-B); z₀-from-K4 rigidity-percolation (exact Maxwell–Calladine z_eff→6) — plus doc-34.
- *Verdict:* **ECHO (Class-B)** — all three named routes closed-negative; the *scale* ~1/137 is forced (Compton-resonance trap), the exact *value* rests on the one identification (R·r = 1/4) the substrate does not independently select. Flip-condition live (R·r = 1/4 forced without α-circularity ⇒ chord); route-space not provably exhausted.
- *Closed:* the "zero-parameter closure" headline.
- *Opened:* the **"real chord or echo?"** north star; the scoped-echo register.
- *Receipts:* `audit/2026-06-02_honest-alpha-relabel`; `audit/2026-06-04_alpha-class2-bijection`; `audit/2026-06-15_k2g-provenance` (z₀ route); `audit/2026-06-19_alpha-three-route-honest-register`; PRs #263, #264.
- *Successor:* ARC-11 (FORM/VALUE meta-finding).

**ARC-07 · EE-as-substrate-native ratification.** Window: E4 (ratified into 2026-06-18).
- *Q:* which discipline's vocabulary is substrate-native (least-leaky) for the vacuum medium?
- *Method:* leak-check each borrowed word's defining property against the lossless / reactive / discrete / saturable substrate; retire disorder/dissipation-leaking nouns.
- *Verdict:* **derived-convention** — EE is the reference language (ε₀/μ₀/Z₀/c ARE vacuum constants); the substrate object-symbol 𝓜_A retired (2026-06-18); sector-declaration discipline adopted.
- *Receipts:* `substrate-native-terminology.md`; CLAUDE.md INVARIANT-N1 (substrate-noun retirement 2026-06-18).
- *Successor:* the operator-typing / sector-ownership columns (ARC-09, ARC-30).

**ARC-05 · multi-lane adversarial orchestration machinery.** Window: 2026-05-20 → ongoing.
- *Q:* how to avoid the shared-seductive-narrative blind spot that a single lane cannot see?
- *Method:* redundant fact/fork lanes + adversarial review; worktree-isolation + background spawn.
- *Verdict:* **built** — the immune-system posture; ratified and carried forward.
- *Receipts:* `audit/2026-05-20_orchestration-reorg`; `audit/2026-05-25_main-into-integration-merge`; `_orchestration/index.md`.
- *Successor:* the E8 walk→prereg→run→bank loop (see §7); PR #603 methods note.

### E5 — the interior gauntlet

**ARC-08 · genesis / electron self-assembly (energize-lock).** Window: → 2026-06-16.
- *Q (prove-or-disprove):* does a free precursor self-assemble the (2,3) winding + Γ=−1 confinement (electron genesis from a free precursor)?
- *Method:* coupled-engine genesis drivers (v5→v15); energy-ledger discrimination.
- *Verdict:* **NEGATIVE (leans-falsified)** — the engine pumps H at dt→0 (not a physical pump); scoped as a category error (the interior-field route is sub-Nyquist / phase-space, so the α-free *boundary-observable* emergence test was never run).
- *Closed:* electron-genesis-from-free-precursor at the interior-field level; three escape hatches.
- *Opened:* the α-free boundary-observable re-aim; the two-sector engine.
- *Receipts:* `audit/2026-06-16_keystone-energize-lock-substrate-pump`; `audit/2026-06-13_loop-gap-genesis-archive`; `genesis-chord-falsification-ledger.md`.
- *Successor:* ARC-12 (bulk-cage reroute).

**ARC-09 · sector-ownership canon (the two "3"s).** Window: 2026-06-13.
- *Q:* does A1 (dilatation MASS) confine/hold the Cosserat (2,3) winding CHARGE, or are they orthogonal DOFs?
- *Method:* the two-"3"s ownership table; SECTOR ⊥ GAUGE.
- *Verdict:* **derived** — mass = A1 ⊥ charge = Cosserat (2,3) winding; μ = sign-selector; never cross-wire.
- *Closed:* the "A1 confines the charge" cross-wiring.
- *Receipts:* PR #220 (CVR EE-sweep + two-"3"s documentation).
- *Successor:* ARC-10, ARC-11.

**ARC-10 · K=2G provenance.** Window: 2026-06-15/16.
- *Q:* is K=2G crystalline-geometric / constitutively-forced, or GR-imported?
- *Method:* two-gate test (crystalline? constitutively-forced?).
- *Verdict:* **GR-imported** — both gates pass (NOT crystalline, NOT constitutively forced).
- *Closed:* K=2G-as-derived. *Opened:* eigenmode-existence as the only remaining open physics.
- *Receipts:* PR #261; `audit/2026-06-15_k2g-provenance`.
- *Successor:* ARC-11.

**ARC-04 · wall-branch fork (H3).** Window: 2026-06-15/16.
- *Q:* is the electron's Γ=−1 wall an independent magnetic-vs-capacitive *branch*?
- *Method:* magnetic-vs-capacitive Γ=−1 wall comparison.
- *Verdict:* **DEGENERATE (B3)** — the wall is a sign/spin *selector*, not a branch; mass=A1 settled independently.
- *Receipts:* PR #260; `audit/2026-06-15_wall-branch-fork`.
- *Successor:* the #260 selector-null probe reused in ARC-32 (x34).

**ARC-11 · FORM/VALUE meta-finding.** Window: 2026-06-16.
- *Q:* what *class* of thing does AVE derive vs import?
- *Method:* cross-constant accounting (α, G, m_e, K=2G).
- *Verdict:* **meta-finding named** — AVE forces the dimensionless FORMS (chords), imports the dimensionful VALUES (echoes): α = echo, G = MIXED, m_e = definitional, K=2G = GR-imported.
- *Closed:* the ambiguity over what "zero-parameter" meant.
- *Opened:* the doctrine that the AVE-distinct chord lives ONLY in forward predictions.
- *Receipts:* PRs #262, #263, #264; `form-deriving-value-importing.md` (`clm-acdc07`).
- *Successor:* ARC-14 (mass close), ARC-13 (carrier close), the testing pivot (E6).

**ARC-14 · mass-sector closure.** Window: 2026-06-20.
- *Q:* is the mass sector an AVE-distinct chord or a peer?
- *Method:* the graded vacuum-impedance network (Z_EM / shear / bulk; topology-forced confinement).
- *Verdict:* **CLOSED — ECHO-final** (peer-with-SM on interior structure).
- *Receipts:* PR #311 (ECHO-FINAL); `audit/2026-06-20_mass-sector-characterization`.
- *Successor:* ARC-13.

**ARC-13 · carrier-sector closure.** Window: 2026-06-20.
- *Q:* charge / spin-½ / Pauli on the Cosserat (2,3) — chord or peer?
- *Method:* the Frank–Read two-loop braid spin-statistics gate.
- *Verdict:* **CLOSED-AT-PEER** — spin-statistics DERIVED (PASS, peer-ahead) but peer-not-chord; the chord lives in forward predictions.
- *Receipts:* PRs #313, #314 (η walk-back, Rule 12), #315; `audit/2026-06-19_spin-doublecover-gate`.
- *Successor:* the electron-def canon (ARC-27, E8).

**ARC-12 · bulk-cage / electron-localization reroute.** Window: 2026-06-24.
- *Q:* does a native bulk-cage lattice localize/confine the electron?
- *Method:* Stage-2 native-cage IMEX make-or-break (energy-certified).
- *Verdict:* **NEGATIVE (Mode-III falsification)** — localization is BOUNDARY / TOPOLOGICAL, not bulk.
- *Closed:* bulk-cage localization. *Opened:* the engine reroute (boundary/topological localization; α-circularity ⇒ the chord must be a dimensionless ratio).
- *Receipts:* PR #403 (GATE-0), PR #404 (settled-negative + Rule-12 banners), PR #405 (reroute).
- *Successor:* the engine reroute + biquaternion coupled-network arc (PRs #433–#435, 2026-06-29).

### E6 — the testing pivot

**ARC-15 · testing pivot / bench-model spine.** Window: 2026-06-23.
- *Q:* how to test AVE where the chord actually lives (forward predictions), infrastructure-first?
- *Method:* a channel-agnostic BenchModel + 8-gate machine-checkable bankability record.
- *Verdict:* **built** — GAP-1 spine (reviewed-PR / no-self-merge workstream).
- *Receipts:* PR #384; `_orchestration/2026-06-23_testing-infra-gate-charter.md`.
- *Successor:* cleave-01 + impedance-probe primitives; the birefringence bench.

**ARC-16 · birefringence Route C (circulation-keyed μ) — FORK-1.** Window: 2026-06-04 → 2026-07-03.
- *Q:* does static-B produce vacuum birefringence (the flagship falsifier), and does the flagship survive PVLAS?
- *Method:* circulation-keyed vacuum μ-grade (capacitor/inductor duality; μ keyed on circulation, not flux).
- *Verdict:* **FORK-1 RESOLVED** — static-B birefringence NULL made EMERGENT (static-B transparent, no ∂B/∂t to load μ); flagship **SURVIVES** PVLAS. Real test = E-route / HIBEF pump–probe (magnitude = echo).
- *Receipts:* `audit/2026-06-04_birefringence-coefficient-reframe`; `audit/2026-07-03_birefringence-campaign-opening`; `audit/2026-07-03_birefringence-letter`; `audit/2026-07-03_birefringence-prediction-doc`.
- *Successor:* the SVE Letter (ARC-17).

**ARC-18 · cleave-01 + vacuum-impedance-probe primitives.** Window: 2026-06-01 → 2026-06-22.
- *Q:* can a benchtop discriminate AVE from SM (the gap-independence chord)?
- *Method:* cleave-01 femto-electrometer (kill-test = gap-INDEPENDENCE, not the slope echo) + vacuum-impedance-probe (channel-Z; minimize Re(Z)/Z₀ in read-mode, Ax3-lossless).
- *Verdict:* **scoped** — cleave-01 kill-test defined; impedance-probe Phase-A feasibility INFEASIBLE (gated-not-dead). cRIO bench resume DEFERRED (the one hardware-discriminating item in-hand).
- *Receipts:* `audit/2026-06-01_cleave-01-phase3-prereg`; `audit/2026-06-11_2026-06-10-crio-bench-prereg`; `_orchestration/2026-06-22_vacuum-impedance-probe-handoff.md`.
- *Successor:* cRIO bench (deferred; flagged in the 2026-07-09 board step-back audit).

### E7 — the Letter era

**ARC-17 · the SVE vacuum-birefringence Letter (v1→v6).** Window: 2026-07-03 → 2026-07-10.
- *Q:* is vacuum birefringence a submission-ready, falsifiable AVE-distinct chord?
- *Method:* four adversarial/co-author review rounds; sector functionals S_B written parameter-free and *computed* not asserted.
- *Verdict:* **hardened / submission-ready** — the flagship forward prediction is a Lorentz-violating sidereal signature (a covariant theory predicts exactly zero); it survived a three-part falsification gauntlet and is unconstrained-yet-testable. **v6 (round-4, #625):** the last limb recast Branch-no; six measured-footing alignments; K.M.'s harmonic catch confirmed (the genuine cos2θ amplitude is **3β²**; the printed 5β² is the θ-independent DC O(β²) offset, mislabeled — both re-hedged to order β²); a **second validation, all-PASS**, via an independent **raw-CODATA route** (base quantities typed directly, not through `constants.py`'s derived chain); the frozen Table-I prediction is **byte-unchanged**.
- *Receipts:* `v0.7` (Letter v3, three-author: G. Lindblom, K. Mertens, B. Herrera); `v0.8` (v4, Bitcoin-anchored); PRs #582, #587, #591, #594, **#625 (v6)**.
- *Successor:* the OTS chain (ARC-21); the γγ/ATLAS confrontation (ARC-22); X41 (ARC-34, the radiative-scoping "why").

**ARC-19 · the muonic-hydrogen self-kill → static-sector scoping (the acquired boundary).** Window: 2026-07-05/06.
- *Q (prove-or-disprove):* does the continuum static-E constitutive law ε_eff = ε₀√(1−(E/E_c)²) survive the best-measured static-field system in physics?
- *Method:* the muonic-H 2S–2P Lamb-shift adjudicator vs the FROZEN CREMA window (202.3706(23) meV); two independent code paths + a live ReconcileGate.
- *Verdict:* **EXCLUDED — [C-EXCLUDED]** — the near-nucleus tail overshoots the window by 4–7 OOM non-perturbatively (still ~2×10⁴× at ℓ_node); falsification/consistency-class (E_c is CODATA-derived through α, m_e — NOT an emergence claim). Pre-registered against FROZEN bins, no post-hoc criterion drops (Rule 11).
- *Closed:* the continuum static-E extrapolation. *Kept:* the deep-cold weak-field AC pump–probe birefringence falsifier (a different dynamic sector) survives; Branch-no hardened.
- *Receipts:* `v0.6` "the electrostatic gauntlet" (`clm-sve3xc`, solidity 0.80); PRs #538/#539/#540; `research/2026-07-05_electrostatic-sector-fork-memo_FROZEN.md`.
- *Successor:* the static-field scope P4 in the Letter; the FORM/VALUE honest-fence pattern (§7 P3).

**ARC-20 · single-footing 3.75π/α² + NIST XCOM verify.** Window: 2026-07-08/09.
- *Q:* reconcile the birefringence footing-lag (7.5π/α² vs 3.75π/α²) and verify the X-ray transport margin against an independent cross-section source.
- *Method:* 20-file single-footing reconcile (OPTION-B); NIST XCOM verification.
- *Verdict:* **reconciled / verified** — 3.75π/α² single-footing; the Fe **7.80 b (not 77 b)** reviewer-ledger correction (margin 220×, verdict unchanged).
- *Receipts:* PR #600 (footing reconcile); PR #591 (XCOM verify); `research/2026-07-08_paper-hardening-ledger.md`.
- *Successor:* Letter v5.

**ARC-21 · OTS pre-registration chain (V1→V4→V5).** Window: 2026-07-04 → 2026-07-09.
- *Q:* instrument-honesty — can the predictions be pre-registered tamper-evidently *before* the test?
- *Method:* OpenTimestamps, Bitcoin-anchored + calendar-attested.
- *Verdict:* **built** — V1 (`f34e7559`) → V4 (`42c760c1`, Bitcoin-anchored) → V5 (`9988dc39`, calendar-attested; `ots upgrade` owed).
- *Receipts:* PRs #592, #596; `audit/2026-07-04_ots-receipt`; `audit/2026-07-09_letter-v4-ots-prereg`; `audit/2026-07-09_letter-v5-ots-prereg`.
- *Successor:* the prereg-commit-first rule (§7, ratified 2026-07-10).

**ARC-22 · clean-field deep scan + γγ/ATLAS confrontation → EFT-domain scoping.** Window: 2026-07-09.
- *Q:* is the birefringence field clean of prior art, and does the ATLAS light-by-light γγ tension survive a make-or-break?
- *Method:* an 8-vector prior-art scan + an ATLAS make-or-break adjudication (five lenses).
- *Verdict:* **CLEAN-FIELD CONFIRMED** (DeLLight = standing matched-regime watch); ATLAS contact-NED reading excluded ~11 OOM, the coherent-forward defense REFUTED → **EFT-domain scoping adopted (asserts nothing)**; in-band FWM added as the 4th testable consequence (Letter v5).
- *Receipts:* PR #593 (clean-field scan, `research/2026-07-09_birefringence-cleanfield-prior-art-scan_result.md`); PR #594 (Letter v5, γγ/LbL); `clm-gg4wmx`.
- *Successor:* the substrate four-photon form factor / two-tone object (ARC-25, E8).

### E8 — the machine-fork nights (2026-07-09 / 2026-07-10)

**ARC-23 · x29 super-band carrier — the fail-and-bank that seeded E8.** Window: 2026-07-09/10.
- *Q:* does the super-band carrier show soliton mobility and a p≈8 coupling law?
- *Method:* single-tone above-band drive; five-lens adversarial review.
- *Verdict:* **NULL-mobility banked** (repaired per review; the p=8.29 coupling-law leg was a turn-on-transient artifact and was dropped → fork A). Structural lesson: a single-tone drive *cannot* measure the γγ 2→2 vertex (odd χ³ ⇒ odd harmonics, all above band) → the **two-tone difference-frequency** protocol.
- *Receipts:* PR #598; `research/2026-07-09_superband-carrier-fork_result.md`.
- *Successor:* ARC-25 (parity theorem / two-tone); ARC-24 (band survey defines "above-band").

**ARC-24 · srs band structure (closed-form).** Window: 2026-07-09/10.
- *Q:* what is the srs lattice band top (which defines "above-band" for every future claim)?
- *Method:* Bloch / Ybus linear survey (scalar TLM + vector/Cosserat-translational).
- *Verdict:* **derived** — scalar band top = π√3 ω_C ≈ 5.44 ω_C (#604); vector/Cosserat-translational band top = a **BRACKET [5.44, 17.0] ω_C** (#607); canon leaf (#609).
- *Opened:* the **single-scale vs stiffness-lifted** band-top fork (does NOT gate fork A; orchestrator lean = stiffness-lifted).
- *Receipts:* PRs #604, #607, #609; `research/2026-07-09_srs-band-survey_result.md`; `research/2026-07-09_srs-vector-band-survey_result.md`.
- *Successor:* fork A (two-tone, ARC-25); fork B (3D nonlinear).

**ARC-25 · the PARITY THEOREM (x31-A two-tone; fork A).** Window: 2026-07-09/10. **STATUS: PR #610 MERGED 2026-07-10; canonically propagated via PR #624 (`clm-invmtr` 0.80, `clm-a6chi3` 0.78).**
- *Q (fork A):* what is the substrate's four-photon (χ³) coupling law above the band edge — the object the ATLAS comparison actually needs?
- *Method:* the two-tone difference-frequency four-photon form-factor measurement on the 1D mechanism substrate, with the parity theorem pre-registered and frozen.
- *Verdict:* **PARITY THEOREM (confirmed)** — the reversible even kernel `U = 1−√(1−r²)` ⇒ `F = r + ½r³` odd ⇒ a two-tone line at `m·ω_lo + n·ω_hi` exists only when `m+n` is ODD ⇒ the literal difference `ω_hi−ω_lo` is **structurally forbidden below yield** (measured 10⁻¹¹× below the FWM product); the four-photon channel is `2ω_lo−ω_hi`, with the **A⁶ amplitude law confirmed (exponent 6.16, predict 6)**. Branch verdict = **(i) DRIVE-TRACKING (fork-record, no preferred outcome)**: the χ³ vertex is frequency-blind above the band → the ATLAS-tension-is-real reading holds *on the 1D mechanism substrate*. The kernel result is **interface-scoped**; the bulk vertex is OPEN.
- *Closed:* the "single-tone can measure the vertex" error (ARC-23).
- *Opened:* the 3D clamp-free bulk four-photon vertex (§6); the participation-normalization KEEP-BOTH adjudication.
- *Receipts:* PR #610 (MERGED); PR #624 (canonical propagation, task #35 Tier-1; `universal-saturation-kernel-catalog.md`).
- *Note (flag-don't-fix):* the orchestrator skeleton described this as "an inversion-symmetry meter with measured **β²** response" — the receipted signature is the **A⁶ (sixth-power)** amplitude law + odd-parity FWM, not a β² response. Recorded per the leaf's file-wins rule.
- *Successor:* fork B (3D srs nonlinear); the substrate four-photon form factor (open).

**ARC-30 · operator-typing pass (x35).** Window: 2026-07-10.
- *Q:* across the 22-operator registry, where do the predictions hide?
- *Method:* four latent type-axes (RATING swing/slew, AXIS-of-action amp/freq/topo, BC-vs-DYN + settled-sector, CLOCK) + a SECTOR column + a gap table.
- *Verdict:* **registry hygiene / candidate-generation** — mints no proposition (every typing reads an existing `operators.md` formula, cites a walked-framing note as FRAMING, or flags AMBIGUOUS for Grant). The swing/slew 1:1 map was **CORRECTED by Grant 2026-07-10 to an orthogonal 2×2** (the μ-kernel is slew-KEYED, not slew-*is*-μ).
- *Receipts:* PR #608; `research/2026-07-10_operator-typing-pass_result.md`.
- *Note (flag-don't-fix):* the skeleton labeled #608 "the 2×2 rating matrix ratified" — #608 is the **4-axis / 22-operator typing pass** (the swing/slew 2×2 is one corrected axis within it); the K4-graph/srs × small/large-signal 2×2 model-register is a *separate* object (PRs #597/#609, `lattice-model-register.md`). Recorded, not silently merged.
- *Successor:* the collapse-target sweep (X33/X34/X36 forks).

**ARC-26 · X33 clock-architecture fork.** Window: 2026-07-09/10.
- *Q:* is the substrate clock synchronous-universal-tick or per-channel-continuous?
- *Method:* the clock-architecture discriminator (Op5).
- *Verdict:* **BRANCH S** (synchronous walk lifts vs pins).
- *Receipts:* PR #611; `research/2026-07-09_x33-clock-architecture_result.md`.
- *Successor:* X36 sharpens it (ARC-28); the clock/topology resolution route is assigned to X37 (ARC-29).

**ARC-32 · X34 tethered-pivot (the #260 selector probe) + the X34b bank.** Window: 2026-07-10. **STATUS: PR #612 MERGED; the X34b re-run PR #626 MERGED 2026-07-10.**
- *Q:* does an anchored (2,3) mode-lock — reusing the #260 wall-selector null?
- *Method:* the tethered-pivot two-axis test (frozen-detector prereg axis + control-subtracted post-hoc axis); then the **X34b re-run** the #612 review prescribed — the control-subtracted (excess) detector **frozen a priori as THE primary rule**, its saturation-zone blindness disclosed up front, the sweep designed so the bank does not rest on the blind zone.
- *Verdict:* **BANKED NEGATIVE (TRACK, single a-priori-frozen excess axis).** #612 gave the KEEP-BOTH two-axis outcome (frozen-absolute PARTIAL + post-hoc excess TRACK); **X34b (#626) converted it to a single frozen-axis bank** — excess_staircase 0.0435 / track_R² 0.9901 on the non-saturated window → anchored (2,3) does **NOT** mode-lock (banks negative next to #417). Flag: the absolute axis is **grid-fragile** (spurious LOCK@29pt from refinement alone); the excess axis is grid-stable — concrete evidence the excess axis is the right detector to freeze.
- *Closed:* the anchored-(2,3) mode-lock reading (BC-quantization). *Ledger:* the hopeful-mechanism miss-ledger advances **0-for-6 → 0-for-7**.
- *Receipts:* PR #612 (MERGED; merge `6ec6222b`); PR #626 (MERGED; prereg `6dbf6b26` pushed before any driver; result `3088e429`); `research/2026-07-10_tethered-pivot-rerun_{prereg,result}.md`.
- *Successor:* the tethered-pivot BC-quantization standing negative (§5, N9 — now BANKED).

**ARC-28 · X36 node-shunt characterization.** Window: 2026-07-10. **STATUS: PR #613 MERGED 2026-07-10.**
- *Q:* is there a Branch-P (node-shunt) ceiling distinct from the installed node resonance?
- *Method:* node-shunt characterization at η=1.
- *Verdict:* the **ceiling = the installed node resonance** — the engine-cannot-adjudicate-its-own-primitives law (an install-tautology); **Branch P iff a series-anti-resonant topology at η=1**; the X33 clock fork is **SHARPENED, not collapsed**.
- *Closed:* the node-shunt-ceiling-as-independent reading (install-tautology). *Opened:* the D-I resolution route (extract, don't install) → X37.
- *Receipts:* PR #613 (MERGED 2026-07-10).
- *Note (flag-don't-fix):* the install-tautology *spirit* is the verdict, but the PR verdict is conditional (Branch P is topology-gated; X33 sharpened not collapsed), not a flat BLOCK.
- *Successor:* X37 (ARC-29) — the extraction that surfaced the underdetermination.

**ARC-29 · X37 junction-parasitic extraction (the D-I layout-parasitic route).** Window: 2026-07-10. **STATUS: PR #616 MERGED 2026-07-10 (+ C2 escape correction #620 MERGED).**
- *Q:* the assigned resolution route for the clock/topology fork (X33/X36) — EXTRACT the srs vertex equivalent circuit from bond geometry (install nothing).
- *Method:* TL-discontinuity / mode-matching extraction of the scalar/compression-channel vertex; freeze-by-push (prereg `167f28ce` pushed before any driver, gh-api-audited); G-A anti-install AST gate.
- *Verdict:* **REACTIVE LOW-PASS** — a shunt accumulator C_j + a series throat L_j, both pin the ceiling DOWN (no lift); **BRANCH (iii)** — the FORM `ω_vertex = g·c/ℓ_node` derives but the MAGNITUDE is **extent-dominated** (g swings 31.4% over f∈[0,0.5]) and is **not closable at the TL abstraction** because canon fixes no transverse bond scale. Class = MIXED (g value derived-geometric; scale ω_C = c/ℓ_node identity-forced). **C2 escape correction (#620):** the matched-lossless-reciprocal-3-port theorem binds the ENTIRE lossless reciprocal C₃ vertex class — no reciprocal model can present a matched bypass; the **sole surviving escape is non-reciprocity** (a circulator, requiring a T-breaking bias — PENDING-GRANT).
- *Closed:* any vertex-lift / reciprocal matched-bypass reading. *Opened:* the bond-bore fork {closures (a)/(b)/(c)} (→ X38); the circulator / T-breaking walk (§6, task #37).
- *Receipts:* PR #616 (MERGED; commits `167f28ce` prereg → `36fcbea7` result); PR #620 (MERGED; C8 KEEP-BOTH log); `research/2026-07-10_x37-junction-parasitics_{prereg_FROZEN,derivation,result}.md`.
- *Successor:* X38 (ARC-33) — the Op6 selection that dissolves the bond-bore fork.

**ARC-27 · electron-definition canonization.** Window: 2026-07-09/10.
- *Q:* consolidate the electron's interior verdict into one canonical definition (5-lane reconciliation).
- *Method:* the FORM/VALUE frame applied to the electron interior; adversarial verification.
- *Verdict:* **closed as import** — the framework derives the FORMS and imports the VALUES of the electron; spin-½ is SELECTION-posited / STRUCTURE-derived (π₁(SO(3))=ℤ₂ gives the double-cover *structure*, but the fermion sign is imported); g=2 from the (2,3) self-orbit A1⊥T2 split (value peer-with-Dirac); five "forced-interior" hypotheses died (longitudinal weld, √α fence, NDC genesis seat, forced sector ratios, forced disclination spectrum). The dislocation/core reframe: the interior is not a place, it is a boundary condition.
- *Receipts:* `v0.8` "the electron gauntlet"; PR #599 (MERGED, task #27; supersedes #590); PRs #583/#584/#585/#588 (spin-½/g-2 lanes); PR #586 (SVE-EE network).
- *Successor:* the standing-negatives index (§5); the forward-prediction program.

**ARC-31 · breakthrough-patterns methods note (P1–P8).** Window: 2026-07-09/10.
- *Q:* what patterns produced the month's breakthroughs (methods knowledge, no physics claims)?
- *Method:* extraction from the 2026-06-09 → 2026-07-09 arcs.
- *Verdict:* **methods knowledge banked** — P1–P8 + "the loop" (walk → identity compression → prereg-with-predicted-numbers → adversarial run → honest bank → register → next walk). **Extended 2026-07-10:** P9 (freeze-by-push), P10 (entailed-branch check), P11 (sabotage test) via PR #622; P12 (frozen bins enforce, flags don't) via the 2026-07-10 methods addendum.
- *Receipts:* PR #603 (P1–P8); PR #622 (P9–P11); `_orchestration/2026-07-09_breakthrough-patterns-methods-note.md` (P12 addendum, 2026-07-10).
- *Successor:* §7 (Methods Evolution).

**ARC-33 · X38 S₁₁-min bore selection (the Op6-selector at the vertex).** Window: 2026-07-10. **STATUS: PR #619 MERGED 2026-07-10.**
- *Q:* does the substrate SELECT the bond's junction extent f (route d for the X37 bond-bore fork)?
- *Method:* apply canon's OWN geometry-selection operator — Universal Operator #6 (`λ_min(S†S)→0`, `clm-gdd70j`, the operator that selected the trefoil `R·r=1/4`) — at the srs vertex, importing no scale; freeze-by-push (prereg `cc386be1` pushed before any driver).
- *Verdict:* **BRANCH (ii) — the POINT JUNCTION.** All three frozen objectives pick **f\*=0** (obj-1 the Op6 primary exactly f\*=0; obj-2/obj-3 single-tone a degenerate float-tie f\*=0.010 on a flat plateau) → the X37 bond-bore fork is **dissolved**, closure (c): `π√3 ω_C` is the Op6-selected ceiling, exact. **branch (i) does NOT fire** (f\*=0 ∉ {1/2π, 1}) — the resonant-locus branch is unadjudicated on the 1/(2π) locus. **New structural fact:** the z=3 star is an intrinsic **1/9-power branch back-scatterer** (Γ=−1/3, no bore removes it; a z=2 through-junction matches perfectly).
- *Closed:* the "substrate selects a bore" reading; the X37 bond-bore fork. *Opened (Grant ontology Q, surfaced not landed):* is the 1/9 per-vertex reflection a real network loss or an idealization a distributed merge smooths out?
- *Receipts:* PR #619 (MERGED; prereg `cc386be1` → module `46366dbe` → driver `4e0afe44`); 22 X38 tests pass; `research/2026-07-10_x38-*`.
- *Successor:* the vertex-ontology question (§6); the circulator escape (ARC-29 / #620).

**ARC-34 · X41 radiative-scoping "why" (the "not-yet-why" arc; fork-record).** Window: 2026-07-10. **STATUS: PR #627 MERGED 2026-07-10.**
- *Q:* the SVE Letter states THAT the constitutive law is radiative-sector, not yet WHY — which key (K1/K2/K3) forces it?
- *Method:* challenge-canonical-negative inventory of the round-3 ε-DC exclusions verbatim; three keys tested against the merged #547 config-fact; prereg froze the branch set; five-lens adversarial review.
- *Verdict:* **UNDERDETERMINED — [K1 ∧ K2, frozen tie].** K3 = **DEAD ON ARRIVAL** (= the round-3 exclusion family). **#547 config-fact confirmed** (the muon loads the full \|E\| into the V_yield / T2 key, no Helmholtz split — [DERIVED: CHARGE-KEYED]). K1 (transverse projection) and K2 (impedance/mode-basis) both survive, both must overturn #547, both reproduce both anchors, and **split only on the transverse-reactive near-zone** (K1 loads / K2 nulls — an unbuilt probe). The #627 review (12 findings) **demoted K1** from "DERIVED-EXACT / strongest" to **"axiom-level reinterpretation, PENDING-GRANT"** (repair `89f3991b`): K1's "drive-direction corollary" was an unlicensed bidirectional extension of #624's READOUT-scoped guarantee; the claimed `:73`+#624-vs-`:75` contradiction was WITHDRAWN (canon is internally consistent) and the fork **re-framed K1-vs-STANDING-CANON** (a new axiom-level ruling, not a contradiction-resolution); a fabricated "verbatim" #547 quote was replaced with genuine text; the **frozen honest tie was restored** (K1 ranking removed).
- *Closed:* K3 as a radiative key; the K1-is-strongest reading. *Opened:* the K1-vs-canon axiom ruling (§6); the CVR held-DC-E bench as empirical adjudicator; the transverse-reactive near-zone probe.
- *Receipts:* PR #627 (MERGED; prereg `0180f85a` FROZEN pushed before derivation; result `6e1e2804`; repair `89f3991b`); merged #547 (2026-07-06, the config-fact).
- *Note (flag-don't-fix / discipline):* Rule 11 (routed UNDERDETERMINED, no `[DERIVED-WHY]` headline); Rule 12 (no #547 retraction, no fourth key); P12 (frozen bins enforce, flags don't — the ranking leaked past the prereg's own seduction flag, caught by review).
- *Successor:* the K1-vs-canon fork (§6, OF10); the CVR bench spec (fresh-session slate).

**ARC-35 · the navigational maps + the corrections wave.** Window: 2026-07-10.
- *Q:* stand up the temporal/causal and history-of-physics navigation layers; reconcile the honesty-lags and algebra defects surfaced en route.
- *Method:* two new no-claim meta-leaves + a KEEP-BOTH / Rule-12 corrections sweep.
- *Verdict:* **built / reconciled** — (i) the **program-arc-map** (this leaf, #614) + the **physics-lineage-map** (#617, 12-fork registry + 14 capsules + 20-entry standing-killers register), with the Kelvin-1888 labile-aether node amendment (#623); (ii) the **implosion-paradox algebra correction** (#618: λ=−2μ ⇒ K=**−4μ/3**, not −μ/3; MacCullagh re-attributed as escape-prototype; no-go strengthened; solidity 0.85 unchanged); (iii) the **S₁₁-selection honesty-lag sweep** (#621: 5 derivative sites reconciled to the 2026-06-14 closed-negative — S₁₁-min does NOT select R·r=1/4, the landscape is FLAT in R·r — via Rule-12/KEEP-BOTH, all value-numbers unchanged); (iv) the Kron-1944 citation confirm (#615).
- *Closed:* the vol1 implosion-algebra internal inconsistency; the S₁₁-selection reading at 5 sites. *Opened:* the W1 uniform-far-field question (§6; whether the "uniform Z₀ far-field bath" framing escapes doc-34's exterior-Γ²=0 flatness, PENDING-GRANT).
- *Receipts:* PRs #614, #615, #617, #618, #621, #623.
- *Successor:* maintained at era boundaries per §1's contract.

---

## §4 — Epistemic State Transitions

The theory's phase changes, in causal order. Each is a *before → after* shift in what the framework believes about itself, not a single result. The canonical home for the whole family is [`form-deriving-value-importing.md`](form-deriving-value-importing.md) (`clm-acdc07`); this list is the temporal index into it.

1. **Keystone → echo** (2026-06-02). *Before:* α⁻¹ = 4π³+π²+π is a zero-parameter *derivation* (a chord). *After:* it is a **Class-B ECHO** — the scale is forced, the exact value is a calibration identity (R·r = 1/4, not independently selected). → ARC-06.

2. **FORM-derives / VALUE-imports** (2026-06-16). *Before:* AVE "derives everything from three scales." *After:* AVE **forces the dimensionless FORMS** (chords) and **imports the dimensionful VALUES** (echoes) of {m_e, α, G}; the organizing principle of the whole corpus. → ARC-11.

3. **Interior = peer, not chord** (2026-06-20 → 2026-07-09). *Before:* the electron's interior structure might carry an AVE-distinct chord. *After:* mass sector ECHO-final, carrier sector closed-at-peer, electron-def closed-as-import — the framework is **uniformly peer-with-SM on interior structure**. Companion leaf: [`the-abandoned-interior.md`](the-abandoned-interior.md). → ARC-14, ARC-13, ARC-27.

4. **Chord → forward predictions** (2026-06 onward). *Before:* the discriminating chord is somewhere inside the derivation. *After:* the AVE-distinct chord lives **only in the forward predictions** (FORM-existence divergences + non-2/7-rooted forced ratios + the Lorentz-violating sidereal signature). This is *why* the testing pivot followed. → ARC-11 successor, ARC-17.

5. **The testing pivot** (2026-06-23). *Before:* progress = more interior derivation / rigor-polishing. *After:* progress = **infrastructure-first testing** where the chord lives (bench + beam). The 2026-07-09 board step-back audit flags that the pivot is declared but the cRIO bench (the one in-hand hardware discriminator) is still untouched. → ARC-15.

6. **The AC/DC epistemological carve** (2026-07-03). *Before:* all substrate statements are on equal footing. *After:* **AC = shared ground** (agreed with SM/QED), **DC = contested**; a real test must live in the **DC→AC coupling**, not in either alone. Refines the phase-only epistemology. → `clm-acdc07`; `audit/2026-07-03_acdc-carve-canonization`.

7. **Instrument-honesty era (prereg-commit-first)** (2026-07-04 → 2026-07-10). *Before:* predictions are argued, then tested. *After:* predictions are **pre-registered tamper-evidently before the test** (OTS, Bitcoin-anchored), and every prereg carries its picture-predicted numbers as first-class frozen criteria (ratified 2026-07-10). → ARC-21; §7 (P5).

---

## §5 — Standing Negatives Index

The arc-level anti-repetition table. **This index does not replace [`genesis-chord-falsification-ledger.md`](genesis-chord-falsification-ledger.md)** — that leaf is the diagnosed, branch-recoverable ledger of the genesis/chord/motion-stability negatives, with the load-bearing `ave-discrimination-check` tags (GENUINE-FALSIFICATION vs WRONG-CARRIER/REGIME vs INCONCLUSIVE). This table is the *arc-map view*: one row per falsified mechanism, its kill receipt, and the arc that closed it, so a session opening a new arc greps here first. For the *why-it-failed* diagnostic, follow the pointer into the ledger.

> **Discrimination-check reminder (per `ave-discrimination-check`):** a null where the effect *cannot exist* in the tested regime/carrier is an **artifact, not a falsification** — it must not be canonized as a kill. Rows below tagged WRONG-REGIME carry a specified re-test and are NOT closed physics.

| # | Falsified mechanism / route | Verdict class | Kill receipt | Arc |
|---|---|---|---|---|
| N1 | Electron genesis from a free precursor (energize-lock / interior-field self-assembly) | NEGATIVE (leans-falsified; interior-field route scoped as category-error) | `audit/2026-06-16_keystone-energize-lock-substrate-pump`; `genesis-chord-falsification-ledger.md` | ARC-08 |
| N2 | The **longitudinal weld** (a derived fermion-sign weld) | GENUINE-FALSIFICATION | `v0.8` release; PR #599; PR #603 (P3); `research/2026-07-08_electron-halfflux-selection_result.md` | ARC-27 |
| N3 | The **√α fence** (forced-interior scale fence) | GENUINE-FALSIFICATION | `v0.8` release; PR #599; PR #603 (P3) | ARC-27 |
| N4 | The **NDC genesis seat** (negative-differential-capacitance genesis correspondence) | GENUINE-FALSIFICATION (a real reactive instability at V_yield/√2 ≈ 30.9 kV, but genesis no-correspondence) | `v0.8` release; PR #599 | ARC-27 |
| N5 | **Forced sector ratios** (interior ratios forced by the substrate) | GENUINE-FALSIFICATION | `v0.8` release; PR #599; PR #603 (P3) | ARC-27 |
| N6 | **Forced disclination spectrum** (a forced interior spectrum) | GENUINE-FALSIFICATION | `v0.8` release; PR #599; PR #603 (P3) | ARC-27 |
| N7 | **Bulk-cage** electron localization | NEGATIVE (Mode-III, energy-certified) → localization is boundary/topological | PR #403, PR #404 | ARC-12 |
| N8 | **Drive-tracking vertex** (the χ³ four-photon *kernel*, interface-scoped) | fork-record verdict (i) DRIVE-TRACKING; **kernel interface-scoped, bulk vertex OPEN** | PR #610 (MERGED); PR #624 (canonical) | ARC-25 |
| N9 | **Tethered-pivot** anchored-(2,3) mode-locking (BC-quantization) | **BANKED NEGATIVE (TRACK, single a-priori-frozen excess axis)** — anchored (2,3) does NOT mode-lock (#260 selector null; banks next to #417); the #612 KEEP-BOTH two-axis outcome converted to a frozen-axis bank; miss-ledger → **0-for-7** | PR #612 (MERGED) + **PR #626 (MERGED, the X34b frozen-axis re-run)** | ARC-32 |
| N10 | **X36 node-shunt ceiling** as an independent Branch-P | install-tautology (ceiling = installed node resonance); Branch P only iff series-anti-resonant at η=1 — verdict conditional | PR #613 (MERGED) | ARC-28 |
| N15 | **X41 K3** — the far-field / dynamical-content radiative key | **DEAD ON ARRIVAL** — = the round-3b far-field exclusion family ([RADIATIVE-KEY-REFUTED]); not a new route (Rule 11: cite the kill, don't re-walk) | PR #627 (MERGED); `research/2026-07-08_p5-radiative-far-field-keying_RESULT.md` | ARC-34 |
| N11 | The continuum **static-E constitutive law** ε_eff = ε₀√(1−(E/E_c)²) at atomic scale | EXCLUDED [C-EXCLUDED] (falsification/consistency-class) | `v0.6` release; `clm-sve3xc`; PRs #538/#539/#540 | ARC-19 |
| N12 | **Dark-wake** cross-scale thrust (Phases 1–5) | WRONG-REGIME artifact (Outcome-C) — re-test = bulk near-yield compression | `audit/2026-05-31_ft-darkwake-crossscale`; `audit/2026-05-31_dark-wake-vocab-scrub`; `dark-back-reaction-taxonomy.md` | E4 |
| N13 | **Protein impedance-folding** (impedance carries the fold) | NEGATIVE (all EE-reflection channels dead) — **cross-repo (AVE-Protein lane); Core walk-back STAGED, B4 row may be STALE** `[PARTIAL-RECEIPT]` | `research/2026-06-07_vol0-kb-reconciliation-ledger.md` (referenced); AVE-Protein lane | (cross-repo) |
| N14 | **Breather-gap** (A1-breather genesis gapping) | `[RECEIPT-PENDING]` — named in the orchestrator skeleton; no dedicated tag/PR/research doc at HEAD `ba662d57` (may correspond to a `genesis-chord-falsification-ledger.md` held-BC entry — verify before citing) | `[RECEIPT-PENDING]` | ARC-08 (candidate) |

Additional genesis/chord negatives (omega-wave WRONG-CARRIER, Q0-blocked INCONCLUSIVE, held-BC DISQUALIFY, Casimir/cold-fusion/Hopf-Sagnac walk-backs) live in `genesis-chord-falsification-ledger.md` and the `audit/2026-06-03_*` / `audit/2026-05-31_ft-*` tags; not duplicated here.

---

## §6 — Standing Open Forks

Every live fork with its *assigned resolution route*. A session picking up a fork checks this table first (Rule 16 — do not mint a parallel plan). Where a route has been dispatched but not yet landed, the status says so; a fork is not "resolved" until its home leaf says so.

| # | Open fork (question) | Assigned resolution route | Status / receipt |
|---|---|---|---|
| OF1 | **Clock / topology architecture** — synchronous-universal-tick vs per-channel-continuous | X37 junction-parasitic extraction → X38 Op6 vertex selection | X33 = BRANCH S (#611); X36 SHARPENED (#613, MERGED); **X37 landed** (#616, MERGED) = REACTIVE LOW-PASS, branch (iii) extent-dominated, not closable at TL abstraction; **X38 landed** (#619, MERGED) = **Op6 selects the POINT JUNCTION (f\*=0)** → the vertex parasitic → 0, memoryless `π√3 ω_C` exact (the two-clock closes in-engine). The extent-conditional part is resolved; the residual synchronous-vs-per-channel question rides the vertex-ontology Q (§ below, OF11-adjacent) |
| OF2 | **The bulk four-photon vertex** — is the χ³ drive-tracking verdict a bulk property or an interface artifact? | 3D clamp-free srs run (board "fork B", 3D srs nonlinear) | PR #610 kernel is **interface-scoped, bulk vertex OPEN**; fork B cheapest, gates all above-band claims |
| OF3 | **The DE-tracks-matter chord (F6)** — does dark energy track matter (the ΛCDM-distinct payoff)? | Build the F6 / irreversible chord on the two-way back-reaction engine | The two-way back-reaction capability (engine item **#86**) is **LANDED** (`clm-w5ez6i`, PRs #433–#435; all gates green); only the REVERSIBLE half is built — the **F6 chord is UNBUILT**. **Flag:** engine item "#86" is an internal capability-tracker number, NOT GitHub PR #86 (a double-slit viz) |
| OF4 | **Band-top scale** — vector/Cosserat band top single-scale (≈5.44 ω_C) vs stiffness-lifted (≈17.0 ω_C) | The per-channel local-c LC-clock walk (orchestrator lean = stiffness-lifted) | PR #607 BRACKET [5.44, 17.0] ω_C; does NOT gate fork A (tone floor safe under both endpoints) |
| OF5 | **UV completion of the Letter kernel** — the high-E completion above the FPB corner (the object the ATLAS comparison needs) | The two-tone χ³ form factor (fork A) + the FPB-corner walked framing | FRAMING only (PR #595, FRAMING-not-derivation); feeds the closure-above-ω₀ open item (`clm-gg4wmx`, Letter v5) |
| OF6 | **η / anchor** — the ξ Machian-boundary anchor is back-solved from CODATA G (circular); can G be forced form-first? | The G-flip-test (Chain B′: form-first ⇒ lift G `mixed → real`) | G = MIXED (echo until the flip closes); `interlock-register.md`, `form-deriving-value-importing.md`, `omega-freeze-cosmic-grain-cascade.md`. The exploratory grip=loss=η=1/Q cosmic-rotation thread is a separate, un-promoted lens |
| OF7 | **Core-envelope constitution** — the abandoned-interior Thread C, scoped as an envelope question (not identity) | Grant-gated; precursor-vs-end-state sub-fork (`clm-uatcql`, flagged OPEN by design) | Parked/standing per the 2026-07-09 board §5 |
| OF8 | **LEP compositeness exposure** (severity HIGH) — does the Γ=−1 wall screen a hard high-q² probe of an extended electron (Λ≳10 TeV)? | EFT-scoping / defect-sector-ownership (same family as the ATLAS defense) | Pre-existing, Grant-question; 2026-07-09 board §5 item 8; candidate next picture-walk |
| OF9 | **D-II / D-III / D-IV batch** | (as assigned in the datasheet-cleanup / divergence program) | **`[RECEIPT-PENDING]`** — the roman-numeral "D-II/III/IV" labels could not be located at HEAD; `divergence-test-substrate-map.md` uses letter-number IDs (e.g. `D5-HTS-MEISSNER`). Verify the label scheme before citing |
| OF10 | **K1-vs-standing-canon** (X41) — does the Ax-4 T2 saturation key on `\|E_T\|` (K1), or does a held bias LOAD the shunt-C (standing canon, K2-adjacent)? | A **new axiom-level Grant ruling** (not a contradiction-resolution) + the **CVR held-DC-E bench** (the empirical adjudicator, K1 vs K2 on the transverse-reactive near-zone) | **UNDERDETERMINED — frozen tie** (PR #627, MERGED); K1 = axiom-level reinterpretation PENDING-GRANT; K3 DEAD (N15); the near-zone split is an unbuilt probe. CVR bench spec = fresh-session slate item |
| OF11 | **Circulator / T-breaking** — the sole surviving vertex-match escape is a non-reciprocal circulator; does the vacuum supply a T-breaking bias? | The circulator / T-breaking picture-walk with Grant (P2: walk input is a circuit), then a fork-record | Opened by the #620 C2 correction (reciprocal C₃ vertex cannot match; N-R is the only escape). Axiom-1's srs chirality is parity-breaking but a circulator needs a *T*-breaking bias additionally — **PENDING-GRANT**; assigned to task #37 (X39 fork-record-both) |
| OF12 | **Branch-(i) locus + W1 far-field** — (a) X38 landed at f\*=0 (branch ii); is the branch-(i) resonant locus at **f = 1/(2π)** a live alternative or Op6-flat-floor-excluded? (b) does the "uniform Z₀ far-field bath" framing escape doc-34's exterior-Γ²=0 flatness? | (a) direct Op6 evaluation on the 1/(2π) locus; (b) Grant ruling on the W1 walk (#621 site 2) | Both **PENDING-GRANT** — (a) f\*=0 ∉ {1/2π, 1} so branch (i) neither fires nor is directly tested (#619); (b) flagged not silently resolved (#621) |

---

## §7 — Methods Evolution

One compact section on the machinery. The canonical extraction is PR #603 / `_orchestration/2026-07-09_breakthrough-patterns-methods-note.md` (patterns **P1–P8**); this section is the temporal index into it, not a re-derivation.

- **Multi-lane adversarial machinery (the immune system).** Redundant fact/fork lanes + adversarial review + worktree isolation. The stated failure mode is the *shared seductive-narrative blind spot* a single lane cannot see; the countermeasure is redundancy tuned to REFUTE (P4). Built in E4 (ARC-05), load-bearing through E8 — the month's real catches (the sidereal-harmonic error, the rolloff error, the x29 no-op actuator + ramp artifact that passed CI *and* prereg) were all cross-lane, not in-lane.

- **The miss-ledger (an instrument, not a lament).** The orchestrator's hopeful-interior-mechanism record is **0-for-6/7** (P4c) — and that track record is itself cited as evidence when weighing the next pretty mechanism. This is *why* §5 (standing negatives) is a first-class navigational surface: the program's measured edge is honest fences + identity compressions + the bench/beam, NOT interior mechanism-hunting.

- **`evidence-void ≠ conclusion-wrong` (harness M4).** Adversarial verdicts now carry a defect class distinguishing a broken instrument from a wrong conclusion (x29: kick broken, pinning real → repair-and-bank, not discard). Receipt: PR #605.

- **Prereg-commit-first (ratified 2026-07-10).** Two coupled rules: (1) no load-bearing ontology ships without the physical-picture walk, and the walk input must be a *circuit*, not a formalism (P2); (2) every prereg carries an **"analytic expectations"** section — the walked picture's predicted observables, with numbers, as first-class frozen criteria (P5). The one x29 leg that survived review (skin depth, matched <1%) was the one the picture predicted in advance. Corollary: pre-declare which discreteness effects are physics vs integrator when the engine lattice IS the physical lattice.

- **The forbidden-knob discriminator + fork-record-both (P7).** Name the fork → pre-state the signature each branch CANNOT fake → run the cheapest separator → bank either way. Cycle time collapsed from weeks (genesis arcs) to hours (x29 fail→review→repair→banked-null). Combined with Grant's standing fork-record ruling (a fork-record PR merges with the fork still open and a resolution arc assigned).

- **The loop (the meta-pattern).** Velocity came from tightening one loop: **walk → identity compression → prereg with predicted numbers → adversarial run → honest bank either way → register into canon → next walk.** The loop period is the program's effective speed; each pattern above hardens one segment. This map is the *register-into-canon* segment operating at arc granularity.


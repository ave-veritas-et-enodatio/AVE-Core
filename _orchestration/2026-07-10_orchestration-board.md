# Orchestration board — 2026-07-10 (session close: the vertex arc + X41 underdetermined fork + Letter v6 + the corrections wave)

**Purpose:** the durable session-state record (track-in-repo, not memory/context). Everything below points at git-tracked artifacts or merged PRs; nothing load-bearing lives only in a chat transcript. Every PR#, date, and verdict below was gh/git-log-confirmed this session (verify-before-cite); the day's merge window is **#608 → #627 (all MERGED)**, HEAD `e3071e70`.

---

## Continuation — 2026-07-11: x40 (task #38) landed

| Finding | Durable home |
|---|---|
| **x40 ring-closure transient (task #38)** — the derivable stick/slip split. At a growth-front nucleation, a closing bond traps **1/10** of the donated circulation and radiates 9/10 (substrate-native TLM, N=10 girth, DERIVED via BFS-witnessed enumeration); flux linkage Λ banks **whole** (exact conservation theorem, independent of stub outflow). **Hodge split:** the trapped 1/10 is the **T-odd cycle-space loop current** (the field-cooled gyrotropic-fossil candidate; Ω_parent as a Barnett-type field); the complementary 9/10 is **T-even cut-space bond strain** — the cut-space fate is model-dependent (radiates in the matched-bath reading / freezes as strain in the strain-holding-lattice reading, **KEEP-BOTH**). Geometric 2nd axis (mixed footing, off-headline): **Σm_jk = 0.6448522896**. Ring-plane ensemble **isotropic** (orientation tensor ⅓·I; \|Σn̂\|/N = 0.047) → **BOUNDS** a coherent CMB-swirl, does not predict one. Branch (iii) fired = consistency demo + one computed characterization, **NOT emergence**. The gyrotropic-fossil reading is a **FRAMING candidate, NOT canonized** (KB propagation is a gated follow-on). Feeds the **D-IV capture** (owes I_parent) + the **CMB-swirl amplitude bound**. | merged **#632** (merge `d73f9a8c`) → `research/2026-07-10_x40-ring-closure-transient_{prereg_FROZEN,result}.md`; driver `src/scripts/vol_1_foundations/x40_ring_closure_transient.py`; tag `audit/2026-07-10_x40-ring-closure-transient` @ `aba70a30` |

**Review + CI.** 4-lens adversarial review (live-fire · Hodge · anti-install · prereg-vs-shipped), **3 findings all MINOR / EVIDENCE-VOID**, all repaired + orchestrator-spot-checked: G-D made fireable via an independent BFS girth (fires on an L=2 girth-8 net), G-E name-keyed (catches an aliased forbidden-constant import), prereg locator erratum (`srs_dec.py:138`→`:137`). Hodge + freeze-integrity lenses CLEAN. Freeze-by-push (P9) held for both the E1–E4 prereg and the E5 cut/cycle amendment (git-audited). CI first went red on a **sabotage-fixture** dangling import (S2b imported `OMEGA_C` from a module that doesn't re-export it) — fixed by re-pointing to `L_NODE`, a genuine forbidden re-export (`aba70a30`); required gate `make verify + make test` green. Trail recorded on the PR (orchestrator verification + CI-resolution comments), not only in chat.

**Gated follow-on:** if the gyrotropic-fossil framing graduates past candidate → a KB canonical-propagation pass (deliberately undone this session per the do-not-canonize scope).

**Orchestrator miss-ledger #10 (2026-07-11).** Ran only the touched test file (`pytest test_x40_ring_closure.py`, 23 green) rather than the full `make test` before calling the repair verified — so the S2b dangling import reached CI red instead of being caught locally. Lesson banked: verify against the gate CI actually runs (full `make test`), not the touched file alone.

---

## 1. Findings register (what was established today, and where it durably lives)

| Finding | Durable home |
|---|---|
| **X36 node-shunt = install-tautology** — the ceiling is the installed node resonance (the engine cannot adjudicate its own primitives); Branch-P only iff a series-anti-resonant topology at η=1; X33 clock fork **SHARPENED, not collapsed** | merged #613 → `research/2026-07-10_x36-*` |
| **X37 junction-parasitic extraction = REACTIVE LOW-PASS** (derived, not installed): shunt accumulator C_j + series throat L_j, both pin the ceiling DOWN; **branch (iii)** — the FORM `ω_vertex=g·c/ℓ_node` derives but the MAGNITUDE is **extent-dominated** and NOT closable at TL abstraction (canon fixes no transverse bond scale) → the underdetermination is surfaced, not hidden | merged #616 → `research/2026-07-10_x37-junction-parasitics_{prereg_FROZEN,derivation,result}.md` |
| **X37 C2 escape-clause correction** — the matched-lossless-reciprocal-3-port theorem (Pozar-class) binds **any** lossless reciprocal C₃ vertex of any internal complexity; **no reciprocal model can present a matched bypass**; sole surviving escape class = **non-reciprocity** (circulator; needs a **T-breaking bias**, PENDING-GRANT) | merged #620 → `research/2026-07-10_x37-junction-parasitics_result.md` (C8 KEEP-BOTH log) |
| **X38 S₁₁-min bore selection** — canon's own Op6 selector (`λ_min(S†S)→0`, `clm-gdd70j`) applied at the vertex: all three frozen objectives pick **f\*=0, the POINT JUNCTION → BRANCH (ii)**, dissolving the X37 bond-bore fork (`π√3 ω_C` is the Op6-selected ceiling, exact); the z=3 star is an intrinsic **1/9-power branch back-scatterer** (Γ=−1/3, no bore removes it); branch (i) does NOT fire (f\*=0 ∉ {1/2π, 1}) | merged #619 → `research/2026-07-10_x38-*` |
| **X34b tethered-pivot re-run = TRACK (single a-priori-frozen excess axis)** — the #612 review consequence-2 re-run: control-subtracted detector frozen a priori; excess_staircase 0.0435 / track_R² 0.9901 on the non-saturated window → anchored (2,3) does NOT mode-lock (banks NEGATIVE next to #417); flag: the absolute axis is grid-fragile (spurious LOCK@29pt), the excess axis grid-stable | merged #626 → `research/2026-07-10_tethered-pivot-rerun_{prereg,result}.md` |
| **X41 radiative-scoping "why" = UNDERDETERMINED [K1 ∧ K2, frozen tie]** — K3 DEAD-on-arrival (= the round-3 ε-DC-exclusion family); **#547 config-fact confirmed** (muon loads full \|E\| into V_yield/T2 key, no Helmholtz split); **K1 demoted to axiom-level reinterpretation, PENDING-GRANT** (the fork = K1's drive-side split **vs standing canon**, not a resolved contradiction); the CVR held-DC-E bench = the empirical adjudicator | merged #627 → `research/2026-07-10_x41-radiative-scoping-why_{prereg_FROZEN,RESULT}.md` |
| **Letter v6 (Keith round-4 integration)** — the last limb recast Branch-no; six measured-footing alignments; Keith's **harmonic catch confirmed** (the genuine cos2θ amplitude is **3β²**; the printed 5β² is the θ-independent DC O(β²) offset, mislabeled — both re-hedged to "order β²"); **second validation all-PASS** with an independent **raw-CODATA route** (base quantities typed directly, not via `constants.py`); frozen Table-I prediction byte-unchanged | merged #625 → `papers/2026_birefringence_letter/main.tex` + provenance §13 |
| **Program-arc-map leaf** (temporal/causal view; 31 receipt-verified arcs, 8 eras, standing-negatives + open-forks indices) | merged #614 → `manuscript/ave-kb/common/program-arc-map.md` |
| **Physics-lineage-map leaf** (history-of-physics as navigational infrastructure; 12-fork registry + 14 thread capsules + 20-entry standing-killers register) | merged #617 → `manuscript/ave-kb/common/physics-lineage-map.md` |
| **Lineage-map 1888 amendment** — the Kelvin-1888 labile-aether node added at all three sites; the PR-#618-resolved upstream-flag retired KEEP-BOTH | merged #623 → `manuscript/ave-kb/common/physics-lineage-map.md` |
| **Cauchy/implosion algebra correction** — λ=−2μ ⇒ K=**−4μ/3** (not λ=−μ ⇒ −μ/3; the old condition deleted nothing); MacCullagh re-attributed as the escape-prototype, not the author; no-go **strengthened** (−4μ/3 < −μ/3); solidity 0.85 unchanged | merged #618 → `implosion-paradox.md` (clm-9gh0a1) + vol1 .tex lockstep |
| **S₁₁-selection honesty-lag sweep** — 5 derivative sites reconciled to the 2026-06-14 closed-negative (S₁₁-min does NOT select R·r=1/4; the landscape is FLAT in R·r) via Rule-12 / KEEP-BOTH; all value-numbers unchanged | merged #621 → 5 sites (KB leaf, 2 research walks, 2 scripts) |
| **Parity-theorem canonical propagation** (task #35 Tier-1) — `clm-invmtr` (0.80) + `clm-a6chi3` (0.78); interface-scoped, bulk vertex OPEN | merged #624 → `universal-saturation-kernel-catalog.md` + Vol-4/Vol-1 mirror |
| **Methods note P9–P11 addendum** — freeze-by-push / entailed-branch check / sabotage test (mirrors AVE-Skills `ave-prereg` v1.7 + `ave-driver-script-honesty` v1.2, commit `7721edc`) | merged #622 → `_orchestration/2026-07-09_breakthrough-patterns-methods-note.md` |
| **Kron-1944 citation confirm** (Proc. IRE volume/pages/DOI) | merged #615 → vol4 leaf |

## 2. PR board — all MERGED this session (#608 → #627)

| PR | Content | Merged (UTC) |
|---|---|---|
| #608 | x35 operator-typing pass (4 axes + gap table) | 2026-07-10T04:58 |
| #609 | srs band-structure canon + model-register fence (task #32) | 2026-07-10T04:55 |
| #610 | x31-A two-tone form-factor + PARITY THEOREM (fork-record repaired) | 2026-07-10T20:00 |
| #611 | x33 clock-architecture — BRANCH S | 2026-07-10T05:00 |
| #612 | x34 tethered-pivot — KEEP-BOTH (PARTIAL + TRACK) | 2026-07-10T06:27 |
| #613 | x36 node-shunt — install-tautology; Branch-P iff series-anti-resonant at η=1 | 2026-07-10T14:20 |
| #614 | program-arc-map leaf | 2026-07-10T14:22 |
| #615 | Kron-1944 cite confirm | 2026-07-10T14:24 |
| #616 | x37 junction-parasitic extraction (D-I route) | 2026-07-10T14:47 |
| #617 | physics-lineage-map leaf | 2026-07-10T14:48 |
| #618 | implosion-paradox algebra correction (λ=−2μ ⇒ K=−4μ/3) | 2026-07-10T16:09 |
| #619 | x38 S₁₁-min bore selection — BRANCH (ii), point junction | 2026-07-10T20:18 |
| #620 | x37 C2 escape-clause correction (reciprocal-vertex theorem-bound) | 2026-07-10T20:08 |
| #621 | S₁₁-selection honesty-lag — 5 sites reconciled | 2026-07-10T20:09 |
| #622 | methods P9–P11 addendum | 2026-07-10T20:19 |
| #623 | lineage-map Kelvin-1888 labile-aether node (task #36) | 2026-07-10T20:31 |
| #624 | parity-theorem canonical propagation (task #35 Tier-1) | 2026-07-10T22:17 |
| #625 | Letter v6 — round-4 integration | 2026-07-10T22:30 |
| #626 | x34b tethered-pivot re-run — TRACK (frozen axis) | 2026-07-10T22:30 |
| #627 | x41 radiative-scoping "why" — UNDERDETERMINED (K1∧K2) | 2026-07-10T22:30 |

## 3. The vertex arc (X36 → X37 → X38) — the day's spine

One object walked through three lanes: **what fixes the srs vertex clock, and can the vertex be matched?**

1. **X36 (#613) — install-tautology BLOCKED.** Node-shunt characterization at η=1 found the ceiling *is* the installed node resonance: the engine cannot adjudicate a primitive it installed. Branch-P (an independent node-shunt ceiling) survives only iff a **series-anti-resonant topology at η=1**. The X33 clock fork is **SHARPENED, not collapsed**. (The install-tautology *spirit* is the verdict; the PR verdict is conditional, not a flat block.)
2. **X37 (#616) — lumped characterization, then the underdetermination surfaces.** The D-I resolution route: **EXTRACT** the vertex equivalent circuit from bond geometry instead of installing a tank. Verdict = **REACTIVE LOW-PASS** (shunt accumulator + series throat, both pin the ceiling down; refutes any lift). But **branch (iii)** fired: the FORM `ω_vertex = g·c/ℓ_node` derives, the MAGNITUDE is **extent-dominated** (`g` swings 31.4% over f∈[0,0.5]) and is **not closable at the TL abstraction** because canon fixes no transverse bond scale. The bond-bore fork {closures (a)/(b)/(c)} opened here. **#620** then closed the escape hatch C2 left open: the matched-lossless-reciprocal-3-port theorem binds the entire reciprocal C₃ vertex class — **the sole surviving escape is non-reciprocity** (a circulator, requiring a **T-breaking bias** the vacuum may or may not supply — PENDING-GRANT).
3. **X38 (#619) — S₁₁ selection dissolves the fork.** Canon's own Op6 geometry-selector (the operator that selected the trefoil `R·r=1/4`) applied at the vertex. **Two-axis result:** the broadband / band-integrated objective (obj-1, the Op6 primary) picks **f\*=0 exactly**; the single-tone objectives (obj-2/obj-3) land on a **degenerate float-tie** (f\*=0.010 on a flat plateau, depth ~6e-10). All three ⇒ **BRANCH (ii), the point junction**, closure (c): `π√3 ω_C` is the Op6-selected ceiling, exact. **branch (i) is unadjudicated on the 1/(2π) locus** — f\*=0 ∉ {1/2π, 1}, so the resonant-locus branch neither fires nor is directly tested. **New structural fact + Grant ontology question (surfaced, not landed):** the z=3 star is an intrinsic **1/9-power branch back-scatterer** (Γ=−1/3, no bore removes it) — a real per-vertex reflection loss, or an idealization a distributed merge smooths out?

## 4. X41 — the radiative-scoping "why" (UNDERDETERMINED, frozen tie)

The SVE Letter states THAT the constitutive law is radiative-sector, not yet WHY. X41 inventoried the round-3 ε-DC exclusions verbatim and tested three keys against the merged **#547** config-fact:

- **K3 = DEAD ON ARRIVAL** — it is the round-3 exclusion family (net-flux / time-variance), already killed.
- **#547 config-fact CONFIRMED** — the muon overshoot loads the **full \|E\| into the V_yield / T2 key, no Helmholtz split** ([DERIVED: CHARGE-KEYED], merged 2026-07-06).
- **K1 (transverse projection)** and **K2 (impedance/mode-basis)** both survive, both must overturn #547, both reproduce both anchors (pump full-load exact; muon zero) — and **split only** on the transverse-reactive near-zone (K1 loads / K2 nulls), an **unbuilt probe**.
- **The #627 adversarial review (12 findings, all confirmed) demoted K1** from "DERIVED-EXACT / strongest" to **"axiom-level reinterpretation, PENDING-GRANT"** (repair `89f3991b`): K1's "drive-direction corollary" was an unlicensed bidirectional extension of #624's READOUT-scoped guarantee; the claimed `:73`+#624-vs-`:75` canon contradiction was WITHDRAWN (canon is internally consistent) and the fork **re-framed as K1's drive-side split vs STANDING CANON** — a Grant ruling for K1 would be a **new axiom-level decision against the current reading**, not the resolution of an existing contradiction. A fabricated "verbatim" #547 quote was replaced with genuine text (fabricated-quote-class catch); the **frozen honest tie was restored** with per-key cost ledgers, K1's ranking removed.
- **Adjudicators:** Grant (the K1 axiom-level ruling) + the **CVR held-DC-E bench** (K1 vs K2, empirical) + the unbuilt transverse-reactive near-zone probe.

## 5. Grant's open adjudications

- **D-V weekend** — the divergence-program D-V item, queued for the weekend session.
- **K1-vs-standing-canon axiom ruling** — does the T2 saturation key on `\|E_T\|` (K1), against the standing canon in which a held bias LOADS the shunt-C (`CLAUDE.md`:75 + #624:179-188)? A **new axiom-level decision**, not a contradiction-resolution. **The CVR held-DC-E bench is the empirical judge.**
- **Circulator / T-breaking walk** — the sole surviving vertex-match escape (#620) is a non-reciprocal circulator; does the vacuum supply a T-breaking bias? Assigned to **task #37** (see slate).
- **Branch-(i) locus** — X38 landed at f\*=0 (branch ii); the branch-(i) resonant locus at **f = 1/(2π)** was not directly adjudicated. Is it a live alternative or excluded by the Op6 flat-floor?
- **W1 uniform-far-field question** — from the Op6-scope / S₁₁ honesty-lag audit (#621 site 2): does the "match into the uniform Z₀ far-field bath" framing escape doc-34's exterior-Γ²=0 flatness, or is it the closed exterior match renamed? Flagged PENDING-GRANT, not silently resolved. *(The collapse-target registry §"anti-target caution" logged 4+ additional sites carrying the identical "external bath coupled ONLY through boundary-impedance-mismatch" object — reported, not resolved; this is the W1 register-mint call.)*

**New adjudications surfaced by the collapse-target registry (task #33, merged #631) — flag-don't-fix, Grant's to rule:**

- **T3 — Γ=−1 loss-character.** When the vacuum is driven *past* V_yield in a fast transient (ZENER-04 / TORSION-05 / muon leaky-cavity), is the node a **lossless short** (Γ=−1, full 180° reaction) or a **blown fuse** (|Γ|<1, dissipative)? The benches write "Γ=−1" but describe the fuse; a possible sign/loss error in the thrust + decay predictions rides on it. A NEW axis alongside the already-flagged `cq:1612` Γ_spinor/Γ_EM homonym (KEEP-BOTH).
- **T4 — MOND external-field-effect keying (forward-prediction opener).** Does the galactic `η_eff` Axiom-4 saturation amplitude `A` key on the **internal source's** `g_N` only (→ AVE predicts **NO EFE**) or the **total local** field (→ EFE ~ standard MOND)? `g_ext ≈ 1.8 a₀` at the solar neighborhood makes this a live, currently-tested discriminator (Crater II, wide binaries) — the one registry target that opens a NEW forward prediction rather than cleaning up.
- **T6 — mass→inductance sector contradiction.** `boundary-observables-m-q-j.md:19` (`clm-ze4clw`) projects MASS→inductance `L`, colliding with the 2026-06-20 ratified ruling `X_L = spin flywheel, rest mass = A1 dilatation` (`dual-reactance:221` + `def-portmp`). Is the M-row "inductance" the TKI translation-image (a dictionary entry, no conflict) or a genuine A1↔T2 cross-wire? The registry surfaces the conflict; does not pick the winner.
- **T13 — N13 protein-folding scope.** Is the AVE-Protein impedance-folding NEGATIVE a **full** falsification of the vol5 `|S₁₁|²`-folding mechanism, or does it kill only a narrower channel? `program-arc-map` N13 says "all EE-reflection channels dead" while the vol5 subtree + divergence-map B4 assert it live, none carrying a Rule-12 header. One sentence decides whether vol5/B4 get walk-back headers or N13 gets demoted to its `[PARTIAL-RECEIPT]` status. (Cross-repo; receipt lives in the AVE-Protein lane.)
- **T15 — S₁₁ INVARIANT-N4 (touches a solidity-1.00 invariant).** N4 declares `S₁₁` a homonym (reflection coefficient vs "folding objective function"); the substrate suggests ONE reflection object with the vol5 "objective" being the derived `min|S₁₁(ω₀)|²`. Needs Grant + the out-of-repo `eq:s11_energy` before any edit, because it contradicts a canonical invariant.
- **T17 / circulator (folds into the existing "Circulator / T-breaking walk" above).** The registry's P8 lane inventoried the **ferrite / Polder gyrotropic-μ-tensor** as the undeployed non-reciprocity *mechanism* (`polder`=0, `off-diagonal (mu|permeab)`=0 corpus-wide; the Larmor/g=2 hits are all the spin-flywheel *ratio*). INVENTORY-ONLY — the mechanism-transfer question **is** the PENDING-GRANT T-breaking-bias fork (task #37).

## 6. The fresh-session slate

| Task | What | Note |
|---|---|---|
| **#33** | ~~collapse-target sweep (X35 main body)~~ **DONE — MERGED #631** (merge `9c795272`, tag `audit/2026-07-10_collapse-target-registry`) | Ranked registry `research/2026-07-10_collapse-target-registry.md` — 19 targets + RHYME tier + anti-target cautions; 7-lane sweep, 2-lens adversarial review (2 MINOR EVIDENCE-VOID findings repaired). **The registry is the INPUT to the core planning session's "which fire" decision** — it executes no collapse. See §9. |
| **#34** | the D-IV nucleation-capture spec (the "writes-a-bias" thread) | **sector-bridge first** — resolve A1↔T2 sector ownership before the capture spec, so the meter and the source are in matched coordinates (A46 phase-space discipline) |
| **#37** | the circulator / T-breaking walk (the vertex non-reciprocity escape) | Grant picture-walk before any prereg (P2 — walk input is a circuit, not a formalism) |
| **#38** | ~~the ring-quantization transient (a kill-test for the u₀\* triple-convergence)~~ | **DONE 2026-07-11 → merged #632** (see Continuation §): trapped 1/10 = T-odd cycle-space; rhyme SHARPENED not killed (isotropic ensemble bounds the swirl); gyro-fossil framing candidate, not canonized |
| **bench-spec follow-on** | the CVR held-DC-E bench specification (the K1/K2 empirical adjudicator) | Requirements-derived + trade-study-open per the bench-doc pattern |

## 7. Orchestrator miss-ledger — this session (#5–#9)

The relay/reading miss-ledger (distinct from the 0-for-7 hopeful-interior-mechanism ledger). Each a departure from the picture or from verify-before-cite, each caught:

- **#5 (2026-07-10) — X34-TRACK over-relay.** Relayed X34 as a clean TRACK before the frozen-axis re-run (x34b/#626) had confirmed it; flattened the #612 KEEP-BOTH two-axis nuance (frozen-absolute PARTIAL) to a single TRACK in the relay.
- **#6 (2026-07-10) — rev-list misread.** Misread a `git rev-list`/merge ordering when reporting session state.
- **#7 (2026-07-10) — "confirmed pushed" error.** Asserted a commit was pushed to origin before the push had actually landed (the exact failure P9's freeze-by-push exists to make git-checkable).
- **#8 (2026-07-10) — Op6-trefoil premise.** Over-relayed that Op6 *selected* the trefoil `R·r=1/4` — the very premise the S₁₁ honesty-lag sweep (#621) corrected: Op6 is eigenmode-finding for a GIVEN network, never geometry-selection.
- **#9 (2026-07-10) — K1-corollary amplification.** Amplified K1's "drive-direction corollary" as strongest / DERIVED-EXACT; caught and demoted by the #627 review (R1) to axiom-level reinterpretation, PENDING-GRANT.

## 8. Review posture (this session)

**5 adversarial review cycles** ran over the day's implementer output (the #624/#625/#626/#627 wrappers + the vertex-arc gates), **61 confirmed findings** in aggregate, **2 fabricated-quote-class catches** — the load-bearing one verified here is the x41 **R3** fabricated "verbatim" #547 quote (replaced with genuine `:272-273/:300` text, its supporting role for the muon re-attribution withdrawn). The gates carried planted-violation proofs throughout (P11 sabotage test): X38's G-B fired exactly because the disabled parasitic path fell back to π, the reference constant. The freeze-by-push ordering (P9) was git-checkable on X37 (#616, prereg `167f28ce` pushed 26 min before code, survived a gh-api timestamp audit) and X38 (#619).

## 9. Collapse-target registry — the fire-decision slate (task #33, merged #631)

The registry (`research/2026-07-10_collapse-target-registry.md`) ranks 19 targets + a RHYME tier + anti-target cautions. It executes **no** collapse; the core planning session decides which fire. Triage for that decision:

**Fire-ready CLEAN (shared mechanism verified, low seduction, no Grant ruling needed) — a collapse session can execute these:**
- **T1** quantization homonym → a **TRIAD** def-node (mode-count ⊥ winding ⊥ Nyquist-sampling); S-cost, mint already staged by the corpus. *The strongest single mint.*
- **T2** slew↔hysteresis-§1 cross-link (the "un-catalogued" rate-keyed family); M-cost, KEEP-BOTH, the "slew" *label* A4-gated.
- **T5** `θ`↔EM-`tan δ` de-orthogonalization (`tan δ = cot θ`, kills the `:331` all-orthogonal over-claim); S-cost — the `θ`↔`δ_AVE` tie stays the `:310` taxonomic bridge, NOT a phasor identity (narrowed by the #631 review).
- **T7** "Cauchy relation" mislabel on K=2G (the genuine Cauchy relation forces `ν=1/4`, not `2/7`); S-cost, reinforces the standing GR-import negative.
- **T8** four-bin taxonomy → 3rd axis on `lattice-model-register` (3/4 already Axis-A; bin-3 gated on X41); M-cost deflation.
- **T10** `Q`-glyph ownership row (≥4 electron-scale objects); S-cost janitorial.
- **T12** `u₀*` def-node (SYM operating-point vs T-breaking bias) — the fireable DEFLATION of the §b triple-convergence; S-cost.
- **T14** "strain" `δ_strain`↔`ε₁₁` register row; **T16** "register" hygiene note; **T19** vol5 conjugate-impedance table reconcile — all S-cost, low value.

**Grant-gated (need a ruling first) — see §5:** T3 (Γ loss-character), T4 (MOND EFE keying — forward-prediction opener), T6 (mass→inductance sector), T13 (N13 scope, cross-repo), T15 (S₁₁ invariant-touch), T17 (circulator/Polder = task #37).

**RHYME tier — do NOT fire without the kill-test passing (0-for-7 ledger):** R1 Manley–Rowe, R2 Q-linewidth (gated on the T9 complex-Poynting Re/Im split), R3 AC-Josephson f=2eV/h, R4 Kolmogorov mis-shelf, R5 the §b `u₀*` triple-convergence *as a convergence*. **T9** (complex Poynting as the off-line register's formal home) is ranked in-tier but self-labeled seduction-adjacent — its first output could be the sector-gate *kill*.

**Anti-target caution (must NOT fire):** band-curvature effective mass `m*=ℏ²(d²E/dk²)⁻¹` — minting it validates the A1⊥T2 cross-wire the corpus already deleted; the undeployed remainder is sector-neutral wave-packet dispersion, NOT "effective mass."

---

## Continuation 2 — 2026-07-11: second review wave + correction set

Second review wave over the three Grant-launched satellite PRs of the day (#631 collapse registry, #632 X40, #634 X42), plus the correction-PR set that absorbed a bulk-merge-during-review race. Every PR#, tag, and file cite below was git/gh-confirmed this session (verify-before-cite); nothing here canonizes.

### 1. Review wave — three orchestrator adversarial reviews

| PR reviewed | Lenses | Findings | Load-bearing content |
|---|---|---|---|
| **#631** collapse-target registry | 2 | **8 confirmed** (1 MAJOR + 7 MINOR) | **MAJOR** — the anti-target caution grounded "m* actively rejected as an SM crutch" on a KB cite that in fact grants the object **peer-with-SM** status: an **authority-order inversion** (the caution over-read its own source). The genuinely-rejection-grade quote lives in the **superseded vol-4 tex register**, not the cited leaf. **7 MINOR** = receipt hygiene, incl. a **vacuous no-`-E` grep** (a completeness claim that a shell-escaped pattern silently could not have found) and a **mixed-a₀ arithmetic slip** (two `a₀` conventions crossed in one line). Corrected in **#637**. |
| **#632** X40 ring-closure | 3 | **4 MINOR** | deviation-ledger **"no deviation" row contradicted by its own repair log**; **stale PR body**; the E3 **"(gated in sabotage)" intra-prereg over-claim**; the **"BALANCED (net ~0)"** leg measured the **DFS sign convention**, not a physical net swirl → **DEMOTED** (`research/2026-07-10_x40-ring-closure-transient_result.md:200,206`). The **sign-free Q-tensor plane-isotropy** stays load-bearing (`:196` cycle-fraction / isotropy tensor — bounds branch (ii), does not measure a swirl). Corrected in **#638**. |
| **#634** X42 eigencavity | 2 | **6 confirmed** | **M2 eigenmode-scale extraction was code-void** (the ✅ rode only the algebraic identity `ℓ_node/α == A_0`, no length extracted — `research/2026-07-10_x42-atomic-eigencavity_RESULT.md:398`); the **muonic branch (i)** rides **post-freeze `saturate=False`** (a two-argument-honesty flag: the discriminator's regime toggle was set after freeze); **D1 port-language was dead code** + a **`Z(r)` named-quantity hazard** (`:78-84`, the `vol2/claim-quality.md:344` named-quantity guard); the **RY-keyed search window narrowed the branch-(ii) recording channel** (`e_hi = e_ground·1.03` could not record a >3% more-bound offset — `:401`); **freeze-by-push = artifact-level only** (the pilot had pre-landed the numbers); **stale constants self-cites**. Corrected in **#639**. |

**Totals: 18 confirmed, 0 refuted, ALL EVIDENCE-VOID, ZERO conclusion flips.** Every headline number was independently reproduced during review — X40: **1/10** via a dimensionful scipy-ODE cross-realization + the girth generalization **N=7→1/7, N=13→1/13** (`research/2026-07-10_x40-ring-closure-transient_result.md:104`); X42: all marks + the sabotage receipts. No verdict moved; the findings are receipt/hygiene/scope, not physics reversals.

### 2. Correction set — the pre-fix-merge pattern applied ×3

**#631/#632/#634 were bulk-merged BEFORE their post-review repairs landed** (the `[DO-NOT-MERGE]` labels notwithstanding — see the workflow note). The established **pre-fix-merge correction-PR pattern** absorbed the race three times:

- **#637** — collapse-registry receipt repairs (**MERGED**). Fixes the MAJOR authority-order inversion + the 7 MINOR receipt items.
- **#638** — X40 repairs (**MERGED**). Includes the **BALANCED demotion** (DFS-sign-convention artifact struck from the swirl claim), the **E3 honesty ledger row**, and an **S6 declined-with-reason** entry.
- **#639** — X42 repairs (**MERGED**) — carries **TWO UPGRADES**, not just fixes:
  1. **M2 now GENUINELY MEASURED.** The ground-state `⟨r⟩/a_scale = 1.5` (the 1s shape factor; extracted 1.500001, **0.0000%** deviation vs the **frozen 0.5% tolerance**) is now extracted from the numerical eigenfunction by inward integration — a box-independent property (`r_max ≈ 133×⟨r⟩`), not a restatement of the identity (`research/2026-07-10_x42-atomic-eigencavity_RESULT.md:125,264,398`).
  2. **Branch-(ii) window widened to 1.5×** (`hi_factor=1.5`), with a **no-more-bound-roots receipt** for H (7 roots) / muonic (6) / He⁺ (5) — none deeper (`:401`).

**Audit tags (all verified on origin via `git ls-remote --tags`):** `audit/2026-07-10_rb-fossil-walk-docket`, `audit/2026-07-11_x40-board-update`, `audit/2026-07-11_board-task33-close`, `audit/2026-07-11_collapse-registry-correction`, `audit/2026-07-11_x40-correction`, `audit/2026-07-11_x42-correction`.

### 3. Workflow note — the bulk-merge-during-review race (process, not blame)

The **bulk-merge-during-review race** is now a **named hazard**: a satellite's `[DO-NOT-MERGE][REVIEW: pending-orchestrator]` PR can be swept into a bulk merge before the orchestrator's review + repairs land. Read the board's **merge column** and its **in-review column** as **distinct states** — a merged SHA is not a reviewed SHA. When a race happens, **corrections follow automatically** via the pre-fix-merge correction-PR pattern (#637/#638/#639 are the receipts). No blame is assigned; the process absorbed it and the record is complete.

### 4. Reconciliation with #636 (KEEP-BOTH)

The task #33-close PR **#636** folded the registry into the board with the line:

> "…7-lane sweep, **2-lens adversarial review (2 MINOR EVIDENCE-VOID findings repaired)**. The registry is the INPUT to the core planning session's 'which fire' decision…" (§6 slate, `#33` row)

That line describes only the **satellite's own pre-PR review** (2 findings). It is **not edited** (KEEP-BOTH). The orchestrator's **8-finding review + #637** completes that trail: the two counts are two different review passes on the same registry (satellite pre-PR = 2; orchestrator post-merge = 8), and both stand.

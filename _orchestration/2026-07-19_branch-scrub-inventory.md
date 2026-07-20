# Branch-scrub disposition inventory — 2026-07-19

**Purpose:** the durable record of the 2026-07-19 Grant-fired unmerged-branch scrub. 46 unmerged
branches were archive-tagged and adjudicated by an 8-agent workflow; 43 pointers deleted (lossless —
every tag preserves the full branch head), 3 kept for genuinely unbanked content. This doc is the
disposition table + the three KEEP branches' unbanked-content detail as flagged follow-ups. Track-in-repo,
not memory/context.

**Companion:** the rulings docket continuation `_orchestration/2026-07-10_rulings-docket.md`
(2026-07-19 branch-scrub block) routes the three follow-ups into the KB-debt queue.

---

## Method

- **Archive-tag-first = lossless.** Before any deletion, every one of the 46 branches got an annotated
  tag `archive/<branch-name>` pinned to its head commit. A deleted pointer is fully recoverable via
  `git checkout archive/<branch-name>` (or `git branch <name> archive/<name>`); the tag holds the exact
  head SHA. Deletion removes only the mutable pointer, never the commits.
- **Per-branch adjudication.** Each branch was walked by the 8-agent workflow (`wf_7957ec36-42c`):
  its unique commits enumerated, its content classified against `origin/main` (FULLY-BANKED /
  SUPERSEDED-CLOSED-ARC / UNBANKED-CONTENT), banked receipts resolved where claimed, and any unbanked
  items extracted.
- **Default DELETE; KEEP needs a named reason.** The default disposition is DELETE-POINTER (content is
  either banked on main, superseded by a later arc, or a closed-negative whose record is preserved by the
  tag). A KEEP-POINTER verdict requires a *named* piece of unbanked content of real value — content
  findable today only on that branch. The three KEEP branches each carry such an item, detailed below as
  flagged follow-ups.
- **Verify-before-cite spot-checks (this session).** 6 archive tags confirmed to exist and resolve to
  head SHAs (the 3 KEEP tags match the adjudication's cited SHAs exactly: `cc63c420`, `f647f58b`,
  `205d6e6b`); the 3 additional DELETE tags checked resolve to `ee48d01c` / `121e811c` / `2ef4990f`.
  2 banked receipts resolved: `9b12ee8f` = "docs(kb): BH Γ=−1 is the SHEAR/GW sector … (3 sites,
  Grant-confirmed)"; `c18cd480` = "Merge pull request #100 … analysis/2026-06-06-open-short-relabel".
  All 3 KEEP live-claim flags re-verified still-live on `origin/main` (see the detail sections). Raw
  adjudication data: workflow `wf_7957ec36-42c`; 60 raw chunk-entries deduped by name to 46 (3 names
  had duplicate chunk-entries: `analysis/electron-canonical-definition`,
  `analysis/paper-hardening-ledger`, `engine/mu-circulation-keying`; richer entry kept in each case).

---

## Disposition table (46 branches, deduped)

Recovery for **every** row: `git checkout archive/<branch>` — the tag equals the branch head at scrub
time, so deletion is lossless. Banked-status legend: **FB** = FULLY-BANKED, **SCA** =
SUPERSEDED-CLOSED-ARC, **UBC** = UNBANKED-CONTENT.

| # | Branch | Commits | Banked | Verdict | One-line summary |
|---|---|---|---|---|---|
| 1 | analysis/2026-06-06-cosserat-geometric-integrator | 7 | SCA | DELETE | Sector-split + Phase-0.5 quasi-stable survival diagnostics: planted all-C (2,3) degrades amplitude-independently even 14× below rupture → not a self-consistent standing solution (CP8 plant anti-pattern). |
| 2 | analysis/2026-06-06-electron-genesis-drop | 4 | FB | DELETE | CP8 photon→(2,3) "drop" self-trap, VERDICT III: A→1 pinch-off hosts ℓ_node droplets (e⁺e⁻ geometric split) but they stay over-yield/lossy, (2,3) never assembles, Cosserat ω stays exactly 0 (Q0 fixed point). |
| 3 | analysis/2026-06-06-genesis-armB-flywheel-seed | 2 | FB | DELETE | Minimal-IC {ω,R,chirality} Lundquist B-flywheel seed, VERDICT III: Beltrami flux rope is NOT an attractor, force-free residual grows, flywheel de-collimates and disperses. |
| 4 | analysis/2026-06-06-genesis-omega-wave | 3 | FB | DELETE | Canonical ω-shear photon does NOT self-trap under energy-conserving wave dynamics; falsified across full sub→over-yield bracket; own re-aim = the saturation-TIR moving Γ=−1 boundary. |
| 5 | analysis/2026-06-06-open-short-relabel | 1 | UBC | **KEEP** | ★ Orphan post-merge commit `cc63c420`: the Grant-confirmed BH-mechanism primer fix (never landed) + a 10-item contradiction-audit backlog. **[FOLLOW-UP #1]** |
| 6 | analysis/2026-06-06-saturation-tir-moving-boundary | 5 | FB | DELETE | Engine fix — saturation as a moving Γ=−1 reflective wall (KEEP-BOTH, default OFF), VERDICT II: boundary converts collapse→confinement, ω-photon self-traps; + WIP-preserve V²-live cross-sector port held for cage-arc. |
| 7 | analysis/2026-06-08-pathc-z0-amorphous-emt | 2 | FB | DELETE | Path-C α-free amorphous z0, Outcome D: WWW disorder straddles 51.25 but no α-free principle selects it; steady-state z0≈51.65 → 1/α=138.0. None of the 3 files on main. |
| 8 | analysis/2026-06-08-vacuum-z4-coordination-walkback | 2 | SCA | DELETE | Tier-C z=4 walk-back: 9 re-groundings of "3"-claims from lattice coordination to Cosserat sector counts (vacuum = z=4 diamond net); Gates A/B held, never ruled. |
| 9 | analysis/2026-06-09-a2mu-vs-Q-crux | 1 | FB | DELETE | CRUX negative: A²_μ does NOT scale with resonant Q — WALL not KNOB; flat across 10× A²_K4 build-up, hard cliff at rupture; Q=α⁻¹ cavity-lift falsified. None of the 5 files on main. |
| 10 | analysis/2026-06-09-crystal-k4-graft | 1 | FB | DELETE | K4 crystal graft SMOKE-FAIL: real-space trap and phase-space winding decouple (SMOKE-3 fails); frozen guard refuses the α-emergence run. None on main. |
| 11 | analysis/2026-06-09-rectifier-stage1-biased-diode | 1 | FB | DELETE | Rectifier Stage-1 Outcome C: real but mundane rectifier — ε-only static-E load gives chromatic n<1 (∝λ²); engineered-gravity chord falsified at Stage 1 by chromaticity. None on main. |
| 12 | analysis/2026-06-11-alpha-a3-reservoir | 2 | UBC | DELETE | PREREG-ONLY (314-line frozen prereg + AMENDMENT-1): a3 reservoir-partition successor to the turns-ratio α route; frozen rule "a3 miss → turns-ratio family fully dead". No result — run never executed. |
| 13 | analysis/2026-06-11-chiral-angle-of-attack | 8 | UBC | DELETE | Single 409-line hypothesis-class doc: the "slats" mechanism (chiral boundary as helical slats), 4 observable surfaces each tagged with the number owed. Self-declared NOT a promotion, auditor-gated. No prereg/driver/runs. |
| 14 | analysis/2026-06-11-screened-winding-probe | 3 | FB | DELETE | Clean prereg→result→panel arc: BIN=NO-SCREENING (w_pol==0 genuine absence), then panel DEMOTION (ARM1 tautological); "panel not clean ⇒ unpushed". |
| 15 | analysis/2026-06-13-loop-gap-scalar-grade | 3 | SCA | DELETE | C′ scalar-grade restoration on the loop-gap harness: H1/H2 confirmed, H3 NOT supported (S3 source doesn't deepen Γ_bulk or lift \|ω\| at smoke budget) + WIP D-stack adjudication docs. |
| 16 | analysis/2026-06-15-eigenmode-heldbc | 31 | FB | DELETE | Held-BC OPTION C/C′ arc on the passive-eigenmode driver: OPTION C DISQUALIFY ((2,3)-hold PUMPS 56.8×), C′ no-work H_bel hold NEGATIVE-earned (single global scalar under-determines the (2,3) pair) + Rule-12 re-bins. |
| 17 | analysis/2026-06-15-passive-eigenmode-solve | 50 | FB | DELETE | Orchestration branch of the electron-existence/passive-eigenmode arc: 25-phase log (Phase 24 SUBSTRATE-PUMP preliminary → Phase 25 OVERTURNED to SCOPED/UNADJUDICATED by adversarial panel). |
| 18 | analysis/2026-06-16-boundary-mqj-selftrap-integrator-zwall | 6 | FB | DELETE | Stage-1 gate (Op17-bounded engine + Z-AT-WALL discriminator + LOCK/PUMP bins): VERDICT = c_eff(V)-STRUCTURAL-GAP (Z does NOT collapse at the wall on the coupled engine; panel-verified, not echo). |
| 19 | analysis/2026-06-16-boundary-mqj-stage15-alphafree-emergence | 10 | SCA | DELETE | Stage-1.5 α-free two-sector convergence: Layer-A PASS (α-free A1 c_eff(V) self-trap), Layer-B energize-LOCK loop INERT, Layer-C EMERGENCE-NEGATIVE — (2,3) doesn't self-form from generic IC. |
| 20 | analysis/2026-06-16-boundary-mqj-stage16-moving-wall-sectorB | 14 | SCA | DELETE | Stage-1.6 external moving Γ=−1 wall on Sector B: wall confines (Γ→−0.993) but coupling_work≡0 for the whole trace = Cartesian-vs-tetrahedral grid-registration ARTIFACT → vacuous on loop-closure. |
| 21 | analysis/2026-06-16-keystone-discriminator-ladder | 26 | FB | DELETE | Corrected discriminator spec (PR #274): RUNG-0 baseline-clean, RUNG-1 +projection, RUNG-2 = SUBSTRATE-PUMP (dt→0 excess plateau, R∞/R0=0.842) PRELIMINARY pending freeze-g control. |
| 22 | analysis/2026-06-16-keystone-discriminator-proof | 21 | SCA | DELETE | PIECE-1 continuum dH_c/dt conservation proof with boundary term (the window-model-pump escape hatch); self-marked "do NOT bank a keystone verdict until adversarial [VERIFY] clears" — never cleared. |
| 23 | analysis/2026-06-16-keystone-freeze-g-control | 29 | FB | DELETE | Engine-lane INDEPENDENT verification of RUNG-2: frozen-g plateau persists (99.6% survives), directly-measured residual accounts for only 0.77% of the excess → SUBSTRATE-PUMP CONFIRMED, window-model-pump hatch closed. |
| 24 | analysis/2026-06-16-keystone-freezeg | 29 | FB | DELETE | Parallel freezeg lane: N=20 & N=32 configs (gap 0.019%, pump holds) + handedness-flip control (RUNG-2 pump symmetric under ω-seed hand flip → chirality-ref artifact does NOT rescue keystone). |
| 25 | analysis/2026-06-16-stage16-k4tlm-bounded-wall | 20 | FB | DELETE | Full boundary-MQJ genesis lineage ending in the K4-TLM unitary-scatter bounded wall: PUMPS with corrected attribution (wall honest, \|ω\| bounded 279.9; pump = pre-existing energize-LOCK, not the wall). ~8.5k lines, none on main. |
| 26 | analysis/2026-06-16-stage16-rerun-amendments | 17 | SCA | DELETE | Strict subset of k4tlm-bounded-wall (16 shared commits) + 1 unique `54fa23cd`: a 2-line CONTESTED marker flagging layer-c EMERGENCE-NEGATIVE as suspect (same Cartesian-stencil-disabled coupling), flag-to-rerun not retraction. |
| 27 | analysis/back-reaction-loop-scope | 1 | FB | DELETE | Scoping pass for the two-way gravitational back-reaction loop (#86): BUILDABLE-WITH-FIXES (Stages 1-2), BLOCKED (Stage 3 DE read-out, pending a depletion primitive); specifies the sourcing law + diamond-net choice. |
| 28 | analysis/coprime-odd-q-selection-rule | 1 | SCA | DELETE | Lane-D (PR #388) derivation: the coprime-odd-q (2,q) selection rule FORCED (chord-candidate) via C-α/β/γ, one Hopf-fibre-wrap bridge theorem-pending; DRAFT for audit + Grant. |
| 29 | analysis/cosserat-band-structure | 1 | SCA | DELETE | Lane-B (PR #389): full 6-DOF Cosserat band structure, validate-on-known PASS at single-node 6×6, phenomenological tile-and-scale two-sublattice ansatz. |
| 30 | analysis/electron-canonical-definition | 1 | FB | DELETE | DRAFT synthesis of the post-#583/#588 electron picture (0₁ unknot ⊥ (2,3) winding ⊥ A1 mass; FORM/VALUE law; honest-PEER) + Part-2 KB-leaf-first propagation scope. Self-declared DO-NOT-MERGE-as-canon. |
| 31 | analysis/engine-architecture-plan | 1 | SCA | DELETE | Framing/planning standing reference for "QED+GR as ONE ENGINE": sector-module inventory, coupling ledger, replacement-is-PARTIAL posture. No code, no clm-IDs. |
| 32 | analysis/engine-stage2-native-cage-imex | 5 | FB | DELETE | Stage-2 native-cage make-or-break: prereg re-freeze + leapfrog (INCONCLUSIVE Rule-10) + IMEX Crank-Nicolson build, certified MAKE-OR-BREAK verdict = MODE-III DISPERSE. |
| 33 | analysis/engine-stage2-native-cage-run | 3 | SCA | DELETE | Strict ancestor of native-cage-imex: prereg re-freeze + explicit leapfrog stepper, make-or-break run INCONCLUSIVE (Rule-10 CFL instability, "not a clean falsification"). |
| 34 | analysis/grqed-extension-scope | 1 | SCA | DELETE | Scoping for the GR/QED-extension engine: BUILDABLE-WITH-FIXES but "consistency-engine-plus-a-thin-chord-set … AVE-distinct only when #86 back-reaction lands"; saturated ε₁₁ shell, singularity RELOCATED-not-removed. |
| 35 | analysis/matter-de-pressure-test | 1 | FB | DELETE | Framing-class 4-lens pressure-test of "matter and DE are one A1 sector": FRAMING-ONLY, DE=A1 REFUTED (DE is Op14 cross-sector trading + ε-sector saturation, not A1; mass=A1 stands per #260). |
| 36 | analysis/motion-stability-bemf | 5 | FB | DELETE | Transverse-engine probe of stability-FROM-motion: VERDICT NULL leaning CONTRADICTS (linear control rises as much; saturation depth falls with v; corr(τ_zx,gain)=−0.81). |
| 37 | analysis/motion-stability-bemf-cosserat | 2 | FB | DELETE | Native-Cosserat Arm-C version: CONTRADICTS-via-PIN (linear pulse advects ±0.053 cell/τ, saturated (2,3) knot does not move — frozen-clock pin S=0⇒c_eff→0; corr(τ_zx,gain)=−0.40 anti-tracks). |
| 38 | analysis/moving-electron-probe | 9 | SCA | DELETE | CP8-class Master-Equation FDTD arc: claimed VERDICT=MOVES (v14 breather translates +13.9 cells at 0.674c₀, 9% match to de-Broglie v_g, phase-scrambled baseline ~20× static) + velocity-floor finding. |
| 39 | analysis/moving-front-freezein | 4 | UBC | **KEEP** | ★ Honest NEGATIVE refuting clm-exjfai's ≥100-Compton-period residue-persistence (STILL LIVE on main) + confirmed memristive S-lag + the only engine realization of moving-front freeze-in. **[FOLLOW-UP #2 — PRIORITY]** |
| 40 | analysis/paper-hardening-ledger | 9 | SCA | DELETE | Orchestrator-side in-flight ledger updates (single file, +189/−8): P4/P5/P6/H1 rulings, P6 make-or-break Parts 1-3, pump inventory [PUMP-SAFE] flagship CERTIFIED. |
| 41 | analysis/preserve-alpha-deltastrain-electron-wip | 1 | FB | DELETE | Safety-preservation commit `f2fab0b2` of multi-session WIP: the α/δ_strain closed-negative arc (5 prereg/result sets) + stabilized-electron-feedback result + engine edits. 34 files, ~15k insertions. |
| 42 | analysis/problem3-muonic-lamb | 6 | FB | DELETE | Fix-stack (fixes 1-6 of 8) on the Problem-3 muonic-H Lamb-shift arc: sign-convention→µ⁻-frame + measured-Lamb-shift relabel, prereg-drift disclosure, [B]-defeat cutoff, tail-coefficient test. |
| 43 | analysis/stage4-a1-eos-scope | 1 | UBC | **KEEP** | ★ Live un-named kernel-conflict: MOND leaf LINEAR √(1−g_N/a₀) vs engine QUADRATIC √(1−r²) under a headline-confirmed 11.5% SPARC residual. **[FOLLOW-UP #3]** |
| 44 | engine/mu-circulation-keying | 7 | FB | DELETE | Route-C μ-keying arc: circulation-key the free-EM vacuum μ-grade in numpy+JAX fdtd, the load-bearing LOADED-μ energy-conservation test (\|dH/H\|≈1.4e-3), step-1 observable-derivation memo + de-circularize fixes A–F. |
| 45 | fix/2026-06-22-kit-hex-clocking | 1 | SCA | DELETE | Despite the name, NO hex-clocking physics fix (that's already on main, `a22f05ca`) — only `make kit` / `kit-verify` / `kit-release` Makefile targets + kit README rewrite. |
| 46 | research/alpha-strain-projection-variational | 2 | SCA | DELETE | Scoping memo framing Open A (variational strain-projection α-value) + Open B (EMT-percolation running) as flip-routes, then Rule-12 self-retraction: both ALREADY run and CLOSED-NEGATIVE (A: +5% at K/G~1.83; B: −4.3 dex short). |

**Totals:** 46 branches · 43 DELETE-POINTER · 3 KEEP-POINTER · every branch recoverable via
`archive/<branch>`.

---

## The three KEEP branches — unbanked-content detail (FLAGGED FOLLOW-UPS)

Each KEEP is unbanked content of real value: a live claim, a canonical fix, or a functional-form conflict
findable today only on that branch. Deletion of each pointer is technically lossless (tag == head,
verified) — but the pointer is **held** as a live signal until the bank job lands. Detail below is
extracted verbatim-faithful from the adjudication (workflow `wf_7957ec36-42c`).

> **🟡 FOLLOW-UP numbering reconcile (dated 2026-07-20; flag-don't-fix — inventory-side note, docket append-only).** This inventory numbers `open-short-relabel` as **FOLLOW-UP #1** (`:53`) and `moving-front-freezein` as **FOLLOW-UP #2** (`:87`). The rulings docket ENTRY 22 (landed via PR #738) **SWAPS** them — its D1 calls `moving-front-freezein` "the still-open remainder of **FOLLOW-UP #1**" and D6 calls the primer/`open-short` fix "scrub **FOLLOW-UP #2** discharged." The two docs' numbers are transposed. The archive tags + head SHAs (`open-short` @ `cc63c420`; `moving-front` @ `f647f58b`) are unambiguous and identify each branch regardless of the label, so **no work target is in doubt**. This note reconciles the mismatch on the inventory side; docket ENTRY 22 is append-only and is **NOT edited** (pointer only).

### FOLLOW-UP #1 — `analysis/2026-06-06-open-short-relabel` (1 commit · head `cc63c420` · tag `archive/analysis/2026-06-06-open-short-relabel`)

**Content.** Single post-merge orphan commit `cc63c420` (2026-06-06 18:23, four minutes AFTER the PR #100
merge `c18cd480` at 18:19) containing: (a) a one-hunk edit to
`manuscript/ave-kb/common/trampoline-analogy-primer.md` replacing the universal-horizon over-unification
(`all four are the same fully-straight bond at A=1`) with the Grant-confirmed BH-mechanism distinction
(electron/Schwinger = EM impedance-mismatch wall vs BH = shear-mode phase transition G_shear→0, Γ=0 for
EM; `do not flatten them into one |Γ|=1 EM wall`); (b) `_orchestration/2026-06-06_contradiction-audit.md`
— a 57-line ranked 10-item corpus-contradiction backlog with file:line evidence table + 6 Grant
adjudication questions.

**Banked receipts.** The PR itself merged (`c18cd480` = PR #100; `90f0b968` open/short relabel on main).
The distinction PHYSICS is banked: main commit `9b12ee8f` relabeled 3 sites
(`universal-saturation-kernel-catalog.md:53`, `existing-experimental-signatures.md`,
`existing-signatures.md`) to shear/GW-sector Γ=−1 with Γ=0 for EM; the #102 retitle landed
(`black-holes-impedance-mismatch.md` gone from main; `bulk-impedance-at-saturation-boundary.md` present);
the audit's Grant-gated backlog is banked COMPRESSED at `_orchestration/2026-06-06_session-handoff.md:28`
(`Backlog (6): cardinal v=c √2 ontology, Q-PROTEIN-21, INVARIANT-N3 op-namespace, single-vs-bond-pair,
Sagnac discriminator, the FDTD-EM-vs-shear flag`).

**Unbanked items.** ★ **the primer hunk.** Main's `trampoline-analogy-primer.md:280` STILL reads
`all four are **the same fully-straight bond at $A = 1$** viewed through different observable channels`;
grep of the main primer for `do not flatten` / `shear-mode phase transition` = 0 hits (re-verified this
session — note the literal string match false-negatives on the `**` markdown bold, so grep the phrase
`same fully-straight bond`, which is present at :280). Worse, main-side `9b12ee8f`'s commit message claims
`#100 primer` landed — grep-verified FALSE: the primer fix exists only in `cc63c420`. **Bank via:**
cherry-pick the `trampoline-analogy-primer.md` hunk of `cc63c420` into a 1-line docs PR (target line
~280, the universal-horizon closing sentence). Secondary (optional): the full 57-line contradiction-audit
table (file:line evidence + 6 Grant questions) exists only here; the compressed 6-item backlog is on main
and its file:line refs are now largely stale against the evolved corpus, so port only if the evidence
table is wanted; items #1 (cardinal √2 — `cubic-k4-empirical-anisotropy.md` still carries v=c·√2 rows with
no resolution flag) and #8 (Li residual) were not conclusively verified resolved on main this pass.

**Note.** Archive tag `archive/analysis/2026-06-06-open-short-relabel` verified = branch head `cc63c420`,
so deletion would be lossless — but per the KEEP criterion this is unbanked content of real value: a
canonical-KB honest-labeling fix that main's own history falsely records as landed. **Delete the pointer
after the primer hunk is banked.**

### FOLLOW-UP #2 — `analysis/moving-front-freezein` (4 commits · head `f647f58b` · tag `archive/analysis/moving-front-freezein`) — ★ PRIORITY: live claim on main refuted by unbanked branch work

**Content.** 2026-06-30 falsification-first arc (frozen prereg `7b97e76d`): moving cosmological
crystallization front + memristive-lagged clamp engine module
(`src/ave/topological/moving_front_freezein.py`, 435 lines) + tests + result. Split verdict: (a)
memristive S-lag mechanism CONFIRMED rate-dependent exactly as derived (S_min 0.04→0.19→0.56 with
v_front); (b) honest NEGATIVE on the lasting-freeze claim — real-space ω-defect persistence ≤3.04 Compton
periods vs the pre-registered ≥100 Cp target (30× short), single mechanism named: the re-solidified
Cosserat solid is linear-elastic with NO topological-pinning term (`_bulk_accel → _bare_linear_gradient`,
`cosserat_field_3d.py:1999`); (c) FLAG: derived freeze direction is FAST-crossing→freeze, so
`dark-wake-bemf-foc-synthesis.md:54` (clm-exjfai, "crossing takes ≥ τ_relax → FREEZES") is BACKWARDS as
literally stated.

**Banked receipts.** None found. `git grep -iE 'moving.front.freeze|freezein' origin/main` = 0 hits;
`git grep 'moving_front_freezein' origin/main -- src/` = 0; genesis-chord-falsification-ledger has no
freeze entry; `gh pr list --state all --head analysis/moving-front-freezein` = []; `git log --all
--grep=freezein` shows the 4 commits exist ONLY on this branch. Second method: read main's
`dark-wake-bemf-foc-synthesis.md` §1.2 and `substrate-hysteresis-index.md:51` — clm-exjfai still live
verbatim, uncorrected. **(Re-verified this session:** `dark-wake-bemf-foc-synthesis.md:54` on
`origin/main` still asserts "Residues persist for ≥ 100 Compton periods in the post-heal solid regime".)

**Unbanked items.** (1) The honest NEGATIVE refuting clm-exjfai's "≥ 100 Compton periods"
residue-persistence claim, which is still asserted live on main at
`manuscript/ave-kb/common/dark-wake-bemf-foc-synthesis.md` §1.2 and propagated at
`manuscript/ave-kb/common/substrate-hysteresis-index.md:51`. (2) The direction conflict: clm-exjfai reads
slow→freeze; the arc's memristive-lag ODE derivation + two-arm run corroborate fast→freeze
(grounding-pass direction) — flagged for a Grant/auditor Rule-12 dated correction, never landed. (3) The
confirmed rate-dependent memristive S-lag result (a positive mechanism finding). (4) The engine module +
tests (`moving_front_freezein.py`, `test_moving_front_freezein.py`) and `results.json`. **Bank via:** a
reviewed PR landing the prereg_FROZEN/result/results.json + module/tests into main `research/` + `src/`; a
falsification-ledger entry for the lasting-freeze negative; auditor-lane clm-exjfai adjudication
(dark-wake doc §1.2 + hysteresis-index row) per the arc's own flag-don't-fix posture.

**Note.** ★ The only branch of the six with **live** unbanked value: it contradicts a canonical KB claim
(clm-exjfai) that remains uncorrected on main, and it carries the only engine realization of the
moving-front freeze-in mechanism. July's "moving-front" mentions on main (electron-lock-barrier Op17
reactive wall) are a different object — no supersession found. Deletion would be technically lossless
(tag == head `f647f58b` verified on origin) but KEEP signals the pending bank job; **drop the pointer only
after the PR + clm-exjfai adjudication land.**

### FOLLOW-UP #3 — `analysis/stage4-a1-eos-scope` (1 commit · head `205d6e6b` · tag `archive/analysis/stage4-a1-eos-scope`)

**Content.** Single 80-line design/scoping doc
`research/2026-06-30_stage4-a1-eos-cosmology_scope.md` (commit `205d6e6b`): Stage-4 A1-EOS three-branch
frame ruled PARTIAL-RHYME; DE-sector ruling (DE = ε-sector Op14 cross-sector trade, A1-tension =
scaffolding only); F6 DE-tracks-matter depletion named the one chord-candidate; S4-0..S4-5 build plan;
forks F1-F4 for Grant.

**Banked receipts.** Core verdicts banked+superseded on main: (a) DE ε-sector/Op14 placement →
`manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/dark-energy-latent-heat-definition.md:14,29-54,124`
("the ε-sector cross-sector-trade placement"); (b) F6 →
`_orchestration/2026-07-13_f6-depletion-tier1-charter-handoff.md` AND the leaf's line 128 "Update (F6
tier-1, PR #674, ruled 2026-07-13)… bin (i) LEDGER-CONSISTENT" — SUPERSEDES the scope's S4-4 item; (c)
S4-0 gate landed: `src/ave/gravity/backreaction.py` +
`research/2026-06-29_grqed-stage3-backreaction_result.md` on main; (d) main-side
`research/2026-06-30_thermo-lifecycle-map_result.md:5,198` cites this branch by name + SHA `205d6e6b`
(stays resolvable via tag `archive/analysis/stage4-a1-eos-scope` after pointer deletion).

**Unbanked items.** (1) **S4-5 drag KERNEL-CONFLICT flag — still LIVE and un-named at HEAD:** KB leaf
`manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/effective-galactic-acceleration-mond.md:15` states
LINEAR √(1 − g_N/a₀) while engine `src/ave/gravity/galactic_mond_drag.py:49` computes QUADRATIC
`np.sqrt(1.0 - r**2)`; the quoted 11.5% Q=1 SPARC residual rode the quadratic engine kernel. Two-method
searched: grep `kernel-conflict|galactic_mond_drag` across `research/`/`_orchestration/`/KB on origin/main
= no conflict doc; grep `quadratic` filtered by mond/drag = nothing; direct read of both sites confirms
the discrepancy persists. **(Re-verified this session:** MOND leaf :15 = `\sqrt{1 - \frac{g_N}{a_0}}`
LINEAR; engine :49 = `np.sqrt(1.0 - r**2)` QUADRATIC — conflict persists live on `origin/main`.) Should be
banked as a debt/reconciliation entry (e.g. an `_orchestration` debt row or a caveat on the MOND leaf) per
the scope doc's S4-5 gate. (2) **F3 flag** —
`manuscript/ave-kb/vol2/nuclear-field/ch10-open-problems/g-star-prediction.md` asserts g*=7³/4 as a
falsifiable prediction with NO /7-provenance-discriminator caveat (grep `provenance|discriminator|rhyme`
in that leaf = empty).

**Note.** KEEP reason (named): the S4-5 kernel-conflict flag is unbanked content of real value — a
KB-vs-engine functional-form discrepancy under a headline confirmed prediction, findable today only in
this branch's doc. Once the flag (and optionally the F3 g* caveat) is banked on main, DELETE is clean:
tag `archive/analysis/stage4-a1-eos-scope` == branch head `205d6e6b` (verified), so deletion is lossless
and the thermo-lifecycle doc's SHA citation remains resolvable.

---

*Discipline: archive-tag-first = lossless; verify-before-cite run on the 6 spot-check tags + 2 banked
receipts + all 3 KEEP live-claim flags this session; pure-corpus. This doc records disposition + the three
routed follow-ups (KB-debt queue items — FOLLOW-UP #2 flagged priority: a live canonical claim on main
stands refuted by unbanked branch work). It banks nothing at result-class and canonizes no physics. Raw
adjudication: workflow `wf_7957ec36-42c` (60 chunk-entries → 46 deduped by name).*

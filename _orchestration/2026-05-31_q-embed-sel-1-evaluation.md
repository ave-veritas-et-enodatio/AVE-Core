# Epic: Q-EMBED-SEL-1 Evaluation (Path α v2-phasor + Path B analytical + C1/C2 internal inconsistency + AVE-HOPF reconciliation)

**Opened**: 2026-05-31 (orchestration session, Grant).
**Origin**: parameter-count framing walkback Phase 3 §3.3 framing-decision needs a concrete evaluation of Path (a) phase-space framing before the gating-clause replacement language can lock in. Grant directive 2026-05-31: *"I want to actually run out what's needed to evaluate/check for path a, what is left for us to model/simulate/derive."*
**Branch**: `analysis/q-embed-sel-1-investigation` (off main, created earlier this session).
**Draft PR**: [#59](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/59) — routes per memory v2 (`feedback_branch_discipline_colleagues.md`).
**Skill discipline applied at scoping**: `ave-prereg` (corpus-grep across 10 repos via agent `ab2555d4`), `pre-test-physics-check` (plumber question surfaced to Grant; Grant clarified `"phase space is what I think it is, but walk me through if we've adequately proved it"` 2026-05-31), `verify-before-cite` v1.4 (all citations grep-confirmed), `phase-space-coordinate-check` (the missing skill in Phase 1+2 of the walkback; load-bearing for this epic), `ave-handoff-canonical-locale` (this doc locale = `_orchestration/`), `ave-evidence-framing-discipline` (precision check on what's proven vs asserted vs failed).

---

## §0 Why this epic exists

The parameter-count framing walkback's Phase 1+2 stamped a spatial-coordinate gating clause that the corpus had retired 4+ weeks earlier per docs 28/29/38 + Grant 2026-04-27 adjudication + AVE-HOPF glossary:32 Grant 2026-04-30 bracketing. Walkback Phase 3 surfaced this gap (corpus-context audit missed those 4 docs in the original scoping). Phase 3 §3.3 lays out three framing-replacement options (a phase-space / b calibration-input / c multi-path).

**Honest evidence state** (per Grant 2026-05-31 walk-through):
- Spatial reading: **FALSIFIED** (doc 38 numerical refutation — canonical Clifford ropelength = 26 vs actual min ≈ 24 at asymmetric (0.75, 0.66); Golden Torus maps to ropelength ≈ 50)
- Phase-space reading: **ASSERTED** (doc 29 §2.4 elimination argument) + **ADOPTED** (Grant 2026-04-27) + **EMPIRICALLY TESTED ONCE AND FAILED** (Path α v1 / r9, commit `466d8c4`: C1 R/r=3.84 vs target φ²=2.62 FAIL, C2 chirality TIE FAIL, persistence 33%) + **4 A59 methodology gaps documented but not re-run**
- Calibration-input position: matches the *actual* evidence state; neither alternative reading has positively succeeded

This epic is the concrete work needed to either (i) close Path (a) with positive evidence or (ii) honestly walk back to Path (b). It does NOT itself adjudicate the walkback Phase 3 §3.3 framing choice — that adjudication waits on this epic's empirical + analytical outcomes.

## §1 Phase decomposition

Four phases. Phase 0 is mechanical (corpus inconsistency fix). Phases 1 and 2 are the load-bearing evaluation tracks (empirical + analytical). Phase 3 is cross-repo reconciliation gated on Phase 1+2 outcomes.

### Phase 0 — C1/C2 internal corpus-inconsistency fix (IMMEDIATE / mechanical)

**Diagnostic** (caught while drafting the runway 2026-05-31): the Phase 2 gating clause as stamped is *mathematically inconsistent*. Verbatim text:

> *"ropelength-minimality on K4 uniquely selects the canonical Clifford-torus embedding $r_1 = r_2 = 1/\sqrt{2}$ fixing $R \cdot r = 1/4$"*

Problem:
- $r_1 = r_2 = 1/\sqrt{2}$ ⇒ $r_1 \cdot r_2 = 1/2$, **NOT** $1/4$
- ch8's Golden Torus $R = \varphi/2, r = (\varphi-1)/2$ ⇒ $R \cdot r = 1/4$ ✓ but $R \neq r$ (asymmetric)
- Doc 38 confirmed: Golden Torus maps to Clifford coordinates $(r_1 \approx 0.966, r_2 \approx 0.258)$ — **highly asymmetric**, not canonical Clifford symmetric

The clause conflates two distinct geometric configurations: "symmetric Clifford" ($r_1 = r_2$) and "Golden Torus" (asymmetric Clifford, $R \cdot r = 1/4$). Pick one and write it correctly.

**Independent of Path (a)/(b)/(c) framing choice** — the mathematical inconsistency exists regardless.

#### §0.1 Deliverables

| # | Item | Effort | Skill discipline |
|---|---|---|---|
| 0.1 | **Grant decision (PENDING)**: which configuration does the framework actually claim — symmetric Clifford ($R \cdot r = 1/2$) or Golden Torus (asymmetric, $R \cdot r = 1/4$)? | 10 min Grant call | `pre-test-physics-check` |
| 0.2 | Implementor pass: corpus-wide Step-3h-exhaustive grep + correction of all ~30 sites Phase 2 stamped | 1 implementor session | `ave-walk-back` v1.2 Step 3h-exhaustive, `ave-sweep-audit` (N=30 ≥ 10), `verify-before-cite`, `phase-space-coordinate-check`, `ave-evidence-framing-discipline` |
| 0.3 | Sweep-audit of the diff | 1 auditor session | `ave-audit-of-audit` |
| 0.4 | PR-routed merge (per memory v2): `gh pr ready` on #59 → review → `gh pr merge` | Standard | `feedback_branch_discipline_colleagues` v2 |

#### §0.2 Closure criteria

Phase 0 closed when: corpus-wide grep for "ropelength-minimality on K4 uniquely selects" returns 0 sites with the inconsistent dual claim. All remaining sites use either symmetric-Clifford language ($R \cdot r = 1/2$, no Golden Torus reference) OR Golden Torus language ($R \cdot r = 1/4$, asymmetric, references doc 28 phase-space framing).

---

### Phase 1 — Path α v(latest+1)-phasor empirical evaluation

**Goal**: rerun the (V_inc, V_ref) phase-space phasor test of doc 28's two-node hypothesis with the four A59 methodology fixes baked in at pre-reg time (per A40 prospective discipline). Adjudicate whether the phase-space framing is empirically supported.

#### §1.1 Pre-reg requirements (per `ave-prereg` Step 3 + Step 3.5)

Required content for the pre-reg doc at `research/2026-XX-XX_Q-EMBED-SEL-1_path_alpha_v2_phasor_prereg.md`:

- **Physical picture** (per `ave-prereg` Step 1.5, 3-5 mechanical bullets, no equations): K4-TLM bond carries (V_inc, V_ref) voltage waves; bond's state lives on $S^3 \subset \mathbb{C}^2$ via normalization; periodic trajectory traces a 2-torus; phasor radii $r_1 = |V_\text{inc}|$ and $r_2 = |V_\text{ref}|$ should equal $\varphi/2$ and $(\varphi-1)/2$ at the (2,3) trefoil eigenmode IF the corpus's two-node hypothesis is right.
- **Discriminating outcomes**:
  - Outcome A (most likely pass): R/r = φ² ± 5% in dominant cluster + Hilbert-chirality ≥ 75% consensus + persistence ≥ 40% over recording window → Path (a) empirically supported
  - Outcome B (alternative): R/r passes but chirality TIE → coupling-mechanism uncertain
  - Outcome C (null/FAIL): R/r ≠ φ² + chirality TIE → phase-space framing also fails; framework drops to Path (b)
- **Falsifier**: persistence ≥ 40% but R/r FAIL in BOTH clusters and chirality consensus < 50% → Path (a) refuted at v2 methodology level
- **Dimensional analysis subsection** (per `ave-prereg` v1.1 Step 3.5): explicit dimensional check of the phasor coordinates vs canonical constants; substrate-mechanism derivation of why R/r = φ² is the expected leading-order eigenmode value

#### §1.2 Deliverables

| # | Item | State | Effort | Skill discipline |
|---|---|---|---|---|
| 1.1 | Pre-reg doc with A59 fixes + dimensional analysis + adjudication criteria | NEW | 2-3 hours | `ave-prereg`, `pre-test-physics-check`, `phase-space-coordinate-check`, `consistency-vs-emergence`, `ave-fundamental-ground-up-implementation` (threshold-locking) |
| 1.2 | Driver script: extend `src/scripts/vol_1_foundations/r9_canonical_phase_space_phasor.py` → `r12_path_alpha_v2_phasor_a59.py` (~150 LOC additions) | EXTENDS EXISTING | 1 session | `ave-canonical-source`, `ave-driver-script-honesty`, `ave-worktree-paths`, `substrate-native-check` |
| 1.3 | A59-fix 1 — persistence-guard pre-characterization: Move 5→6→7 chain to find fresh attractor window (t=[10, 50]P likely; v1's [50, 200]P caught decayed attractor at 33%) | NEW | included in 1.2 | `phase-space-coordinate-check`, `ave-analytical-tool-selection` (Time-domain class) |
| 1.4 | A59-fix 2 — Hilbert-transform chirality estimator (replace mean P × dP/dt which gave std/\|mean\|=600-1200×) | NEW | included in 1.2 (~20 LOC) | `ave-analytical-tool-selection` (Mode class) |
| 1.5 | A59-fix 3 — per-cluster bipolar R/r adjudication (v1's +x R/r≈5.5 vs −x R/r≈2.2 split was masked by median) + symmetric ansatz | NEW | included in 1.2 | `ave-discrimination-check` (multi-cluster as 2 instances not 1 mean) |
| 1.6 | A59-fix 4 — sampling strategy: top-K single-cell vs bond-pair (open; needs prereg call) | DECIDE | 30 min | `ave-independence-check` (pairwise vs single sampling distinction) |
| 1.7 | Lattice scale: v1 at N=32 (interior 24³); N=96 is canonical TLM scale (compute cost ~30× larger). Honest pre-reg: validate methodology at 32 first, then re-run at 96 for canonical | DECIDE | Grant call | `ave-fundamental-ground-up-implementation` |
| 1.8 | Run + extract phasor trajectory + compute R/r per cluster + Hilbert chirality + persistence | EXECUTES | depends on N | `ave-driver-script-honesty` (live-fire validation) |
| 1.9 | Result doc with adjudication against criteria | NEW | 1-2 hours | `verify-before-cite`, `ave-evidence-framing-discipline`, `ave-discrimination-check`, `ave-multi-falsifier-triangulation-discipline` (C1+C2+persistence as joint criteria) |

#### §1.3 Adjudication criteria (FROZEN at pre-reg time per A40 prospective discipline)

- **C1 (R/r value)**: R/r = φ² = 2.618 ± 5% in dominant cluster (≥ 60% of bonds sampled)
- **C2 (chirality)**: ≥ 75% Hilbert-transform consensus (CW vs CCW) across dominant cluster
- **Persistence guard**: peak \|ω\| ≥ 40% of initial over recording window
- **Pass**: C1 AND C2 AND persistence-guard all pass
- **Mode II/III taxonomy**: per existing prereg discipline (Mode I = full PASS; Mode II = N/4 pass; Mode III = all FAIL or methodology gap)

#### §1.4 Closure criteria

Phase 1 closed when: result doc written, adjudication frozen against pre-reg criteria, and the verdict (PASS / FAIL / methodology gap) lands as a Mode I/II/III outcome with full diagnostic trail.

---

### Phase 2 — Analytical derivation (substrate-primitive eigenmode in phase-space coordinates)

**Goal**: derive from substrate primitives why the (V_inc, V_ref) phasor at the (2,3) trefoil eigenmode lands at R/r = φ². Closes doc 28 §5.4's explicit open question.

#### §2.1 Pre-reg requirements

Pre-reg at `research/2026-XX-XX_Q-EMBED-SEL-1_path_b_analytical_prereg.md`:

- **Physical picture**: substrate K4-TLM bond LC tank + Cosserat field + Op operators force a specific eigenmode at the (2,3) trefoil. The eigenmode determines the bond's natural (V_inc, V_ref) phasor trajectory. Show analytically that this trajectory's radii satisfy R/r = φ² (or R = φ/2, r = (φ-1)/2 if asymmetric per Golden Torus).
- **Discriminating outcomes**:
  - Outcome A: closed-form derivation lands at R/r = φ² via substrate primitives → Path (a) analytically supported
  - Outcome B: derivation lands at canonical Clifford symmetric (R/r = 1) → resolves C1 inconsistency in favor of symmetric reading + falsifies ch8's Golden-Torus framing
  - Outcome C: derivation requires an additional postulate beyond AVE axioms → doc 39's calibration-input position validated; Path (b) is honest
  - Outcome D: derivation lands at neither — corpus framing is internally inconsistent at deeper level
- **Falsifier**: substrate-primitive derivation requires a step that imports SM/QED concepts without K4-native equivalent → doc 39 position validated

#### §2.2 Deliverables

| # | Item | State | Effort | Skill discipline |
|---|---|---|---|---|
| 2.1 | Pre-reg doc | NEW | 2-3 hours | `ave-prereg`, `pre-test-physics-check`, `phase-space-coordinate-check`, `ave-discipline-translate` (caught translation gaps before deriving), `ave-ee-first-mapping` (EE substrate-native baseline), `consistency-vs-emergence`, `ave-fundamental-ground-up-implementation` |
| 2.2 | Substrate-primitive derivation of (V_inc, V_ref) phasor at K4-TLM bond at (2,3) trefoil eigenmode | NEW | open (1-N sessions) | `substrate-native-check`, `ave-analytical-tool-selection` (Resonance + Mode + Time-domain classes), `ave-canonical-leaf-pull` (LC tank, Q-factor, matched-LC-coupling, Op14 saturation leaves), `ave-power-category-check` (real-vs-reactive at eigenmode) |
| 2.3 | Doc 28 §5.4 closure: real-space-to-phase-space coordinate relationship | NEW | included in 2.2 | `phase-space-coordinate-check`, `ave-discipline-translate` |
| 2.4 | Reproduce ch8 three regimes (Nyquist d=1; Crossings R−r=1/2; Screening R·r=1/4) from phase-space primitives, OR identify which are spatial-only artifacts | NEW | included in 2.2 | `consistency-vs-emergence` (classify each regime), `ave-fundamental-ground-up-implementation` |
| 2.5 | Cross-check: does phasor analysis match for muon, proton, Δ baryon? (Vol 2 sectors) | OPTIONAL | extends Phase 2 | `ave-independence-check` (each particle as independent instance), `phase-space-coordinate-check` |
| 2.6 | Result doc | NEW | 1-2 hours | `verify-before-cite`, `ave-evidence-framing-discipline`, `consistency-vs-emergence` (re-classify after derivation), `ave-multi-falsifier-triangulation-discipline` |

#### §2.3 Closure criteria

Phase 2 closed when: derivation result doc lands an Outcome A/B/C/D verdict per §2.1 with explicit substrate-primitive derivation chain (or honest gap identification) per `consistency-vs-emergence` v1.3 classification discipline.

---

### Phase 3 — AVE-HOPF cross-repo reconciliation (GATED on Phase 1+2 outcomes)

**Goal**: reconcile AVE-Core's gating-clause position with AVE-HOPF's `docs/glossary.md:32` Grant 2026-04-30 bracketing. Net outcome should be: ONE position across both repos, consistent with the Phase 1+2 verdicts.

#### §3.1 Deliverables

| # | Item | State | Effort | Skill discipline |
|---|---|---|---|---|
| 3.1 | Conditional on Phase 1 PASS + Phase 2 Outcome A → restate AVE-HOPF bracketing as "bracketed pending phase-space v2 confirmation (now confirmed; lifting bracket)" → un-bracket Golden Torus in AVE-HOPF glossary | CONDITIONAL | 30 min | `ave-walk-back` (cross-repo), `verify-before-cite` |
| 3.2 | Conditional on Phase 1 FAIL OR Phase 2 Outcome C → ratify AVE-HOPF Grant 2026-04-30 bracketing as canonical; walk AVE-Core back to "α is calibration input" position; retitle `zero-parameter-universe.md` etc. (the title-retitle pass becomes part of THIS reconciliation) | CONDITIONAL | 1-2 implementor sessions | `ave-walk-back` v1.2 Step 3h-exhaustive, `ave-sweep-audit`, `phase-space-coordinate-check`, `ave-evidence-framing-discipline` |
| 3.3 | HOPF-01 empirical correlation (Δf/f = 1.2α per doc 79 §6.7, lab boards in hand 2026-05-02 per memory `project_hopf_01_status`): does lab data bear on phasor framing? Surface to Grant + AVE-HOPF lab team | INVESTIGATE | open | `verify-before-cite`, `ave-ip-divide-discipline` (lab data is application-side) |
| 3.4 | Cross-repo PR coordination: PR in AVE-HOPF mirroring whichever direction Phase 1+2 lands | CONDITIONAL | standard | `feedback_branch_discipline_colleagues` v2 |

#### §3.2 Closure criteria

Phase 3 closed when: AVE-Core and AVE-HOPF carry consistent positions on the Golden Torus / phase-space-phasor / zero-parameter-vs-calibration-input claim, with both positions citable to the same evidence (Phase 1+2 outcomes).

---

## §2 Skill matrix (full suite, by phase)

Per Grant directive 2026-05-31: *"apply the full suite of tasks/skills it requires."*

| Skill | Phase 0 | Phase 1 | Phase 2 | Phase 3 | Session-wide |
|---|:-:|:-:|:-:|:-:|:-:|
| `ave-prereg` | — | ✅ | ✅ | — | ✅ |
| `pre-test-physics-check` | ✅ | ✅ | ✅ | — | ✅ |
| `phase-space-coordinate-check` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ave-walk-back` v1.2 | ✅ | — | — | ✅ | ✅ |
| `ave-sweep-audit` | ✅ | — | — | ✅ | ✅ |
| `ave-canonical-source` | — | ✅ | — | — | — |
| `ave-driver-script-honesty` | — | ✅ | — | — | — |
| `ave-canonical-leaf-pull` | — | ✅ | ✅ | — | — |
| `ave-discipline-translate` | — | — | ✅ | — | — |
| `ave-ee-first-mapping` | — | — | ✅ | — | — |
| `substrate-native-check` | — | ✅ | ✅ | — | — |
| `consistency-vs-emergence` | — | ✅ | ✅ | — | — |
| `ave-discrimination-check` | — | ✅ | — | — | — |
| `ave-fundamental-ground-up-implementation` | — | ✅ | ✅ | — | — |
| `ave-analytical-tool-selection` | — | ✅ | ✅ | — | — |
| `ave-power-category-check` | — | — | ✅ | — | — |
| `ave-independence-check` | — | ✅ | ✅ | — | — |
| `ave-multi-falsifier-triangulation-discipline` | — | ✅ | ✅ | — | — |
| `ave-cavity-class-identification` | — | — | ⚠️ if applied | — | — |
| `ave-ip-divide-discipline` | — | — | — | ✅ | — |
| `ave-worktree-paths` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ave-audit` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ave-audit-of-audit` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `verify-before-cite` v1.4 | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ave-evidence-framing-discipline` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ave-directory-enumeration-discipline` | ✅ | ✅ | ✅ | ✅ | ✅ |
| `ave-handoff-canonical-locale` | — | — | — | — | ✅ |
| `ave-newly-created-skill-self-audit` | — | ⚠️ if new skill | ⚠️ if new skill | — | — |

Routing convention (memory v2): every phase that lands commits routes via `gh pr create --base main --head <branch> [--draft]` → review → `gh pr merge`. No direct main commits.

## §3 Sequencing

```
[Phase 0 — C1/C2 fix]
        ↓ (closes regardless of framing)
[Grant §0.1 call: symmetric Clifford or Golden Torus?]
        ↓
[Phase 0 implementor + sweep-audit + PR merge]
        ↓
   ─────────────────┬───────────────────
   ↓                                    ↓
[Phase 1 empirical]              [Phase 2 analytical]
[Path α v2-phasor]               [Substrate-primitive derivation]
   ↓                                    ↓
[Phase 1 verdict]                 [Phase 2 verdict]
   └───────────────┬────────────────────┘
                   ↓
        [Joint adjudication]
        [Resolves walkback §3.3 framing choice]
                   ↓
            [Phase 3 cross-repo]
            [AVE-HOPF reconciliation]
                   ↓
            [Both epics CLOSE]
```

Phase 1 and Phase 2 are parallelizable (empirical track + analytical track operate independently until joint adjudication). Phase 3 is gated on both.

## §4 Cross-references

- **Walkback epic** (parent, paused on §3.3 awaiting this evaluation): [`_orchestration/2026-05-28_parameter-count-framing-walkback.md`](2026-05-28_parameter-count-framing-walkback.md) §Phase 3
- **Routing-convention slip retroactive record**: [issue #58](https://github.com/ave-veritas-et-enodatio/AVE-Core/issues/58)
- **This epic's draft PR**: [#59](https://github.com/ave-veritas-et-enodatio/AVE-Core/pull/59)
- **Canonical corpus context** (cited at every step):
  - [`research/_archive/L3_electron_soliton/28_two_node_electron_synthesis.md`](../research/_archive/L3_electron_soliton/28_two_node_electron_synthesis.md) §5.4 (open question: real-to-phase-space relationship)
  - [`research/_archive/L3_electron_soliton/29_ch8_audit.md`](../research/_archive/L3_electron_soliton/29_ch8_audit.md) F4-F9, §2.4 (spatial reading falsified; phase-space is the only surviving reading)
  - [`research/_archive/L3_electron_soliton/38_ropelength_minimality.md`](../research/_archive/L3_electron_soliton/38_ropelength_minimality.md) §2 (numerical refutation of canonical-Clifford-as-spatial-ropelength-min)
  - [`research/_archive/L3_electron_soliton/39_alpha_is_calibration.md`](../research/_archive/L3_electron_soliton/39_alpha_is_calibration.md) (calibration-input dissent position)
  - [`research/_archive/L3_electron_soliton/78_canonical_phase_space_phasor.md`](../research/_archive/L3_electron_soliton/78_canonical_phase_space_phasor.md) §7 (A59 4 methodology fixes verbatim)
  - [`research/_archive/L3_electron_soliton/VACUUM_ENGINE_MANUAL.md:3713`](../research/_archive/L3_electron_soliton/VACUUM_ENGINE_MANUAL.md) (Grant 2026-04-27 adjudication: R, r as phase-space)
  - [`AVE-HOPF/docs/glossary.md:32`](../../AVE-HOPF/docs/glossary.md) (Grant 2026-04-30 bracketing as "post-IP-separation patch-attempt")
- **Canonical KB leaves**:
  - [`manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md`](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md) (the three-regime substrate-mechanism canonical anchor)
  - [`manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md) (K4 → 2T ⊂ SU(2) → SO(3) chain)
  - [`manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md`](../manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/finkelstein-misner-spin-half-derivation.md) (spin-½ K4-native derivation)
- **Existing Phase 1 infrastructure** (extends, doesn't rebuild):
  - `src/scripts/vol_1_foundations/r9_canonical_phase_space_phasor.py` (v1 driver)
  - `src/scripts/vol_1_foundations/r9_canonical_phase_space_phasor_results.json` (v1 result)
  - `src/scripts/vol_1_foundations/r7_k4tlm_scattering_lctank.py` (K4-TLM substrate sim)
  - `src/scripts/vol_1_foundations/tlm_electron_soliton_eigenmode.py` (eigenmode driver)
  - `src/scripts/vol_1_foundations/k4tlm_dispersion_analytical.py` (analytical dispersion)
- **Path α version archive** (lineage):
  - `78_canonical_phase_space_phasor.md` (v1, phase-space phasor framing, 2026-04-27, FAILED)
  - `84_path_alpha_v6_first_run_results.md` (v6, helical Beltrami branch)
  - `86_path_alpha_v7_helical_beltrami_thermal_sweep.md` (v7)
  - `87_path_alpha_v8_round_11_ignition.md` (v8, "Round 11 framework reframe AUTO-FIRED")
  - `88_round_11_vi_stride_1_a43_v14.md` (v14 stride-1 work)
  - The phase-space PHASOR test specifically hasn't been re-run with A59 fixes since v1 — that's the target of this epic's Phase 1

## §5 Status

- [x] **Epic scoping complete** (2026-05-31 orchestration session) — §0-§4 drafted on `analysis/q-embed-sel-1-investigation`; draft PR #59 covers Phase 3 walkback scoping AND this evaluation epic
- [ ] **Phase 0 §0.1 Grant decision**: symmetric Clifford or Golden Torus? Independent of Path (a)/(b)/(c) framing choice
- [ ] **Phase 0 implementor + sweep-audit + PR merge**
- [ ] **Phase 1 empirical pre-reg drafted** — gated on §0
- [ ] **Phase 1 driver built + run + adjudicated** — gated on pre-reg + Grant §1.7 lattice-scale call
- [ ] **Phase 2 analytical pre-reg drafted** — can start in parallel with Phase 1
- [ ] **Phase 2 derivation completed + adjudicated** — open ended
- [ ] **Joint Phase 1+2 verdict** — resolves walkback §3.3 framing choice
- [ ] **Phase 3 AVE-HOPF cross-repo reconciliation** — gated on Phase 1+2
- [ ] **Both epics CLOSED** — gated on Phase 3

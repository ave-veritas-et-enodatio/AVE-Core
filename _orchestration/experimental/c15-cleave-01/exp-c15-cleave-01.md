# EXP-C15-CLEAVE-01: Femto-Coulomb Electrometer ($Q = \xi_{topo} \cdot x$)

**Parent epic**: [`../experimental-arc.md`](../experimental-arc.md)
**Phase tag**: **[PREP]** — Phase 1a-rev1 is implementor + design work (atopile walk-back + Q-C15-12 Stage A bug fixes + Stage B revision); flips to **[EXEC]** when Phase 2 fab queue activates (~$7670 full BOM mid-range: chamber refurb + PZT + ADA4530-1 + PCB fab + auxiliary instrumentation)
**Status**: **PHASE 1a-rev1 ✓ COMPLETE — both stages MERGED to main + audit tags pushed.** Stage A landed at `AVE-Hardware-Modules` main @ `8b0626b` (audit tag `audit/2026-05-20_q-c15-12-stage-a-fix` at `a68b2f4`); Stage B landed at `AVE-Bench-FemtoElectrometer` main @ `7f9c721` (audit tag `audit/2026-05-20_phase-1a-rev1-atopile-walkback` at `132bf14`). Q-C15-10 + Q-C15-11 + Q-C15-12 + Q1.2 + Q-HWMOD-04 all CLOSED. Clean atopile module-level imports from `cleave_01.ato`; KB-leaf prediction verbatim preserved; pure-AVE-corpus zero matches across new artifacts. **`ave-module-library-discipline v1.0` skill first-fire** (Rules 1-5 applied + cited in Stage A + Stage B commits). Atopile 0.12.5 upstream `FileDependencySpec` bug noted (commented `dependencies:` block; relative-path imports as workaround; backlog: retest after atopile 0.15.x upgrade).
**Owner**: **AVE-Bench-FemtoElectrometer** sibling repo at GitHub + `/Users/grantlindblom/AVE-staging/AVE-Bench-FemtoElectrometer/` — parallels AVE-Bench-VacuumMirror precedent
**Established**: 2026-05-20 from Phase 2 cascade-emphasis ranking

## Tier (per parent epic Phase 2 audit)

Cascade SIZE winner — largest single-row cascade in matrix (6+ dependent rows in ξ_topo family). Composite Σ=10. R=0 (PCBA spec in KB only), D=3 (U-D, KB-explicit falsification: "if 0.0 mV, the framework is falsified"), S=3 (F-severity, Ax2 dies), C=2 (~$1-5k bench), X=3 (ξ_topo family: B4 + C9 + C16 + B5 + B6 + B7).

## Premise

Cleave-01 tests **Axiom 2 (Topo-Kinematic Isomorphism, [Q] ≡ [L])** directly at the bench. The canonical electromechanical-transduction constant $\xi_{topo} = e/\ell_{node}$ (INVARIANT-C2 per [`ave-kb/CLAUDE.md`](../../../manuscript/ave-kb/CLAUDE.md)) bridges AVE lattice parameters and mechanical/biological quantities. If a mechanical displacement $x$ induces topological charge $Q = \xi_{topo} \cdot x$, then a precision electrometer reading the charge across a PZT-stepped capacitor measures $\xi_{topo}$ directly.

**KB explicit prediction**: $41.5 \,\text{mV}$ per $1 \,\mu\text{m}$ displacement on a $10 \,\text{pF}$ input. $0.415 \,\text{pC}$ charge per step.

**KB explicit falsification statement** (literal, original round-1 framing): *"if 0.0 mV, the framework is falsified."* **Chord-gated framing (2026-06-22, supersedes the round-1 magnitude framing for adjudication):** the falsifier is **no gap-INDEPENDENT integer charge floor surviving the $\ge4\times$ gap-sweep at fixed $C_{in}$** (Outcome C), NOT a 0.0 mV reading per se — CPD also gives a non-zero step, and a non-zero step is not by itself a GO. The slope magnitude (41.5 mV/µm) is a consistency-class echo ($\xi_{topo}=\sqrt{\alpha}$ + Compton-$\ell_{node}$, doubly over-determined), demoted to a non-gating secondary corroborator. See Phase-3 prereg §4/§6/§7 + KB leaf.

**Cascade reach** — ξ_topo appears in:
- **B4-PROTEIN** (Ramachandran enforcement uses ξ_topo per Vol 5 protein-folding engine)
- **C9-LEVITATION** ($m_{max} = V_{yield} \cdot \xi_{topo} / g$)
- **C16-TORSION-05** (Project TORSION-05 thrust uses ξ_topo for V↔M coupling)
- **B5-PONDER-01** + **B6-PONDER-02** + **B7-PONDER-05** (all PONDER thrust derivations use ξ_topo at V_yield boundary)

If C15-CLEAVE-01 fails (no gap-independent integer charge floor survives the gap-sweep — Outcome C), Ax2 dies → ALL 6 downstream rows fall + the framework's electromechanical-bridge axiom is killed.

## Standard EE counterfactual

A standard capacitor with PZT actuator generates charge via mechanical strain on the dielectric (piezoelectric effect $d_{31}$ etc.), but NOT via a TOPOLOGICAL charge-length identity. **Round-2 correction (2026-06-04):** the round-1 "SM predicts exactly 0.0" was FALSE — contact-potential-difference (CPD / moving-Kelvin-probe) gives a polarity-odd, ~21%-of-floor charge that is gap-DEPENDENT ($\propto V_{CPD}/g^2$). The AVE prediction is a $Q_{topo} = \xi_{topo} \cdot x$ floor that is the **4-corner conjunction** {linear ∧ polarity-odd ∧ material-independent ∧ gap-INDEPENDENT}. Discriminator: a $\ge4\times$ gap-sweep at fixed $C_{in}$ separates the gap-flat floor from the $\propto1/g^2$ CPD background; polarity-reversal removes even-in-$V$ fakers (electrostriction/flexo/secondary-piezo); time-gating removes decaying tribo; dielectric-swap removes material-dependent piezo. SM predicts no gap-independent floor; AVE predicts one — two-sided, non-fakeable on the chord.

## Phase table

| Phase | Status | Brief / docs | Adjudication needed | Audit trail entry |
|---|---|---|---|---|
| **Phase 0 — Scoping + scaffold** | ✓ COMPLETE 2026-05-20 EOD+++++ | (archived) [`_archive/exp-c15-cleave-01-phase-0-scaffolding.md`](_archive/exp-c15-cleave-01-phase-0-scaffolding.md) | Grant A3 scaffold-only + B1 standalone sibling repo ✓ adjudicated 2026-05-20 EOD++++ | 2026-05-20 EOD++++ + EOD+++++ entries below |
| **Q-C15-01 chamber priority** | ✓ CLOSED — dedicated chamber path C1 (2026-05-20 EOD+++++) | (archived) [`_archive/exp-c15-cleave-01-q-c15-01-chamber-scoping.md`](_archive/exp-c15-cleave-01-q-c15-01-chamber-scoping.md) | Grant C1 dedicated ✓ adjudicated 2026-05-20 EOD+++++ | 2026-05-20 EOD+++++ entries below |
| **Phase 1 KiCad (predecessor)** | ✓ MERGED `331a778` (2026-05-20 EOD++++++++), then walked back to atopile per Q-C15-10 | (archived) [`_archive/exp-c15-cleave-01-phase-1-kicad-brief.md`](_archive/exp-c15-cleave-01-phase-1-kicad-brief.md) | Grant Q-C15-07/08/09 + Q1.2 ✓ adjudicated 2026-05-20 EOD++++++++ | 2026-05-20 EOD+++++++ + EOD++++++++ entries below |
| **Q-C15-10 atopile walk-back** | ✓ ADJUDICATED — Option A new sibling repo `AVE-Hardware-Modules` (2026-05-20 EOD+++++++++) | (archived) [`_archive/exp-c15-cleave-01-phase-1a-rev1-atopile-walkback-brief.md`](_archive/exp-c15-cleave-01-phase-1a-rev1-atopile-walkback-brief.md) | Grant Path: atopile + Option A new HWMOD sibling ✓ adjudicated 2026-05-20 EOD+++++++++ | 2026-05-20 EOD+++++++++ entry below |
| **Phase 1a-rev1 Stage A** | ✓ COMPLETE — `AVE-Hardware-Modules` main @ `e2171cb` | (archived) Stage A scope in phase-1a-rev1 brief above | Stage A success criteria PASSED in implementor verification | 2026-05-20 EOD+++++++++++ entry below |
| **Phase 1a-rev1 Stage A** | ✓ MERGED `AVE-Hardware-Modules` main @ `8b0626b` (audit tag at `a68b2f4`); Q-HWMOD-04 ✓ CLOSED | [`q-c15-12-stage-a-fix-brief.md`](q-c15-12-stage-a-fix-brief.md) | Grant Path 1 ✓ adjudicated 2026-05-20 EOD+++++++++++++; Stage A auto-merged per Path 1 authorization | 2026-05-20 EOD++++++++++++++ entry below |
| **Phase 1a-rev1 Stage B** | ✓ MERGED `AVE-Bench-FemtoElectrometer` main @ `7f9c721` (audit tag `audit/2026-05-20_phase-1a-rev1-atopile-walkback` at `132bf14`); Q-C15-10/11/12 + Q1.2 all CLOSED; clean module-level imports | (closure log) [`q-c15-12-stage-a-fix-brief.md`](q-c15-12-stage-a-fix-brief.md) | Pre-merge review PASSED 2026-05-20 EOD++++++++++++++; merged `--no-ff` + audit tag + branch cleanup | 2026-05-20 EOD++++++++++++++ entry below |
| **Phase 1b PCB layout** | ⏳ PENDING | TBD post Q-C15-12 + merge | Gated on Phase 1a-rev1 merge | — |
| **Phase 1c Gerbers** | ⏳ PENDING | TBD post Phase 1b | Gated on Phase 1b | — |
| **Phase 2 fab + assembly** | ⏳ PENDING | TBD | ~$7670 mid-range BOM rollup | — |
| **Phase 3 measurement** | 📋 PREREG DRAFTED 2026-06-01 (frozen at framing/discriminator level; gated on hardware for execution) | [`exp-c15-cleave-01-phase-3-measurement-prereg.md`](exp-c15-cleave-01-phase-3-measurement-prereg.md) — charge-pinned 2-level discriminator (Level-1 binary $C$-independent / Level-2 0.415 pC/µm) | Level-2 precision target = Q-C15-02 closure (in-situ $C$) | 2026-06-01 prereg-draft |
| **Phase 4 outcome adjudication** | ⏳ CONDITIONAL on Phase 3 | TBD per KB-leaf §"Outcome adjudication" | Outcome A/B/C/D per KB leaf | — |

Detailed prose for **active phases** (Phase 1a-rev1 forward to Phase 4) lives in the per-phase sections below. **Closed phases** (Phase 0, Q-C15-01, Phase 1 KiCad, Q-C15-10 adjudication, Stage A) have their original briefs preserved in [`_archive/`](_archive/) for full reference; the phase-table audit-trail-entry column points to the canonical dated entry in the audit trail at the bottom of this doc.

## Active phase detail

### Phase 1a-rev1 Stage B — merge decision (current — Q-C15-12 pending)

**State**: Branch `analysis/phase-1a-rev1-atopile-walkback` in AVE-Bench-FemtoElectrometer at `b44b1f7` (3 commits; pushed to origin; NOT merged). `ato build` clean on atopile 0.12.5 via direct-part-import workaround.

**Blocker**: Q-C15-12 merge path adjudication pending Grant.
- **Path 1 (recommended)**: Fix Stage A first in AVE-Hardware-Modules (separate fix-branch addresses the 2 latent bugs + ato.yaml `package:` block); then revise Stage B to use clean module imports instead of direct-part-import workaround. Cleaner long-term; defers C15 merge by ~1 implementor session.
- **Path 2**: Merge Stage B as-is + queue Q-HWMOD-04 fix-branch in AVE-Hardware-Modules for later. Ships workaround in main; risks divergence between cleve_01.ato direct-imports and what other consumers might do once HWMOD is fixed.

**Stage B integration findings (Q-C15-12 specifics)**:
1. `AVE-Hardware-Modules/modules/mill_max_ptfe_socket.ato` line 17: exposes `signal = new Electrical` — `signal` is reserved `signaldef_stmt` keyword in atopile 0.12.5; consumer-side `.signal` access fails parsing.
2. `AVE-Hardware-Modules/modules/ptfe_turret_post_standoff.ato` line 85: references nonexistent `tp.2 ~ pad_b` pin; `Keystone_1610_3_package` declares only `pin 1`.
3. `AVE-Hardware-Modules/ato.yaml` lacks `package:` block prerequisite for `ato install` consumability in atopile 0.12.5 (Stage A's `git+https://` syntax from brief was forward-looking; actual 0.12.5 syntax: `registry://` / `git://` / `file://`).

**3 atopile 0.12.5 workflow surprises captured** (per Rule 10 empirical-driver discipline):
- (a) `dependencies:` in 0.12.5 uses `registry://` / `git://` / `file://`, NOT `git+https://` from brief
- (b) fp-lib-table per-build seeding requires 5 `../` URI depth at consumer scale (vs Stage A smoke-test 3 `../`)
- (c) net resolution stub on first build (atopile emits minimal `.kicad_pcb` + empty `(nets)` in `.net`; KiCad GUI fills on first open)

**Stage B success-criteria pass (verified in implementor verification 2026-05-20 EOD++++++++++++)**:
- All 9 deliverables COMPLETE (D1-D9 per archived brief)
- All 12 success criteria PASSED
- KB-leaf prediction preserved verbatim (9 grep hits for "41.5"/"0.415"/"OUTCOME"/"Ax2 DIES" unchanged)
- Pure-AVE-corpus grep zero matches
- `ato build` clean

### Phase 1b PCB layout (PENDING — gated on Phase 1a-rev1 merge)

**Action (deferred)**: Grant manual KiCad GUI work from `ato build` output (`build/cleave_01.kicad_pcb`). Schematic ERC clean + PCB layout + guard-ring polygon + DRC. Phase 1a-rev1 walk-back established the atopile + KiCad round-trip workflow (edit `.ato` source → `ato build` → open `.kicad_pcb` in KiCad GUI for layout).

**Output**: Layout-complete `.kicad_pcb` ready for Gerbers export.

### Phase 1c Gerbers + ordering (PENDING — gated on Phase 1b)

**Action**: `kicad-cli pcb export gerbers` on layout-complete board. Populate `AVE-Bench-FemtoElectrometer/hardware/ORDERING.md` §2 PCB fab section (skeleton landed in Phase 1a). Generate JLCPCB-ready Gerbers + drill files + pick-and-place.

**Output**: `hardware/Gerbers_cleave_01/` directory + ORDERING populated for fab submission.

### Phase 2 fab + assembly (PENDING — gated on Phase 1c)

**Action**: Submit Gerbers to JLCPCB; order BOM components per `AVE-Bench-FemtoElectrometer/hardware/BOM.md` finalized SKUs ($7670 mid-range rollup); assemble; install in dedicated vacuum chamber (Q-C15-01 ✓ adjudicated: bell-jar/4''-6'' CF refurb, ≤10⁻⁶ Torr, no HV) with PZT actuator + off-PCBA DAC + off-PCBA HV amp (Q1.2 ✓ adjudicated).

**Time**: 2-3 weeks (fab + parts + assembly + chamber procurement + integration)
**Cost**: ~$7670 mid-range BOM rollup (per Phase 1a procurement_action_items.md §E)

**Grant adjudications honored at Phase 2**:
- Q-C15-01 ✓ dedicated chamber (bell-jar/4''-6'' CF refurb, ≤10⁻⁶ Torr, no HV)
- Q-C15-05 commodity PI N-216-grade PZT (UHV-specialty deferred)
- Q-C15-07 ✓ dedicated FT2 PZT feedthrough
- Q-C15-08 ✓ dedicated PTFE-socket floating-plate return
- Q-C15-09 ✓ external-only ground via FT1 BNC shield
- Q1.2 ✓ off-PCBA DAC + HV amp

### Phase 3 measurement (PENDING — gated on Phase 2)

**Action**: ave-prereg-format pre-registration FROZEN before any measurement (closes Q-C15-02 precision target). Then the **$\ge4\times$ gap-sweep at fixed $C_{in}$** (the chord measurement) + polarity-reversal + dielectric-swap + time-gating + calibrated positive-control per Phase-3 prereg §5; adjudicate the 4-corner conjunction (chord) per §6. The 0.415 pC/µm (41.5 mV/µm at 10 pF) slope is recorded as a non-gating secondary corroborator, NOT the GO axis. Discriminator dielectric test (Q-C15-03 ✓ adjudicated: vacuum-gap-only as Phase 3 default).

**Primary observable (the chord)**: a gap-INDEPENDENT, polarity-odd, material-independent, linear-in-$x$ integer charge floor ($\mathcal{Q}=\mathrm{Link}\in\mathbb{Z}$) surviving the gap-sweep. **Secondary corroborator (non-gating)**: $V_{out} = \xi_{topo} \cdot x / C_{in} = 41.5 \,\text{mV/μm}$ at $C_{in} = 10 \,\text{pF}$ (the over-determined $\sqrt{\alpha}$/Compton echo).

**Time**: ~1 week measurement + analysis
**Skill discipline**: ave-prereg + ave-discrimination-check Step 1.5 + ave-evidence-framing-discipline + verify-before-cite on all canonical-constant citations

### Phase 4 outcome adjudication (CONDITIONAL on Phase 3)

GO/NO-GO gates on the **chord** (4-corner gap-independent integer floor), NOT the slope (the echo). Per the Phase-3 prereg §6 + KB-leaf "Outcome adjudication":

| Outcome | Adjudication axis | Interpretation |
|---|---|---|
| **A — chord confirmed (GO)** | 4-corner {linear ∧ polarity-odd ∧ material-indep ∧ gap-INDEPENDENT} survives $\ge4\times$ gap-sweep at fixed $C_{in}$; positive-control passed | **Ax2 confirmed at bench**. ξ_topo cascade (B4 + C9 + C16 + B5-7) gains bench-scale corroboration. **Foreword-promotion-grade**. Slope-match to 0.415 pC/µm = non-gating secondary corroborator (slope deviation = A-with-$\alpha$-chain-flag, NOT a demotion). |
| **B — partial (chord ambiguous)** | floor detected but gap-sweep inconclusive | Integer-charge chord suggested; gap-independence corner not established. Re-run gap-sweep. NOT a GO. |
| **C — null (chord falsified, NO-GO)** | no gap-INDEPENDENT floor survives the sweep (absent or fully CPD-$1/g^2$); positive-control passing | **Ax2 dies. Framework falsified at substrate-foundational axiom level.** Cascade walk-back: B4 + C9 + C16 + B5-7 ALL fail. Framework-killing. |
| **D — confound** | floor fails a corner OR positive-control did not register | Discriminate from C via re-design with better guards; re-test |

**Outcome A** → write canonical result doc + matrix update across ENTIRE ξ_topo family + foreword promotion + skill-amendment (this becomes the canonical Ax2-bench-validation citation across all volumes).

**Outcome C** → framework-killing-level walk-back. Cosserat substrate hypothesis falsified at the electromechanical-transduction axiom. Major theoretical re-derivation needed.

## Open questions (forward-active)

| # | Question | Status | Resolution path |
|---|---|---|---|
| Q-C15-02 | Pre-reg precision target — at what slope-precision (per ADA4530-1 noise floor) is Outcome A vs B vs C confidently distinguished? | OPEN — Phase 3 gate | Requires ADA4530-1 noise-floor measurement + parasitic-rejection characterization at Phase 2 bench-up |
| Q-C15-03 | Discriminator dielectric test | ✓ ADJUDICATED — vacuum-gap-only as Phase 3 default | Phase 3 design; secondary PTFE/polyimide configurations may be added as Phase 3 contingency |
| Q-C15-04 | Parasitic input $C_{in}$ control | OPEN (10 pF NP0/C0G ±1% target with Kemet ±0.25 pF alt) | Phase 1b design discipline; LCR meter calibration + guard-ring effective $C$ measurement at Phase 2 bench-up |
| Q-C15-06 | Triboelectric confound discrimination | OPEN — Phase 3 design | Static-only step + relaxation-time monitoring + Outcome D adjudication discipline |
| **Q-C15-11** | Cross-repo atopile module synchronization (paired with Q-HWMOD-01 in AVE-Hardware-Modules) | OPEN — TRACK-ONLY | Phase 1a-rev1 → Phase 4. No active migration unless module evolution blocks pre-existing design improvement OR >2 design repos use same inline definition |
| **Q-C15-12** | **Phase 1a-rev1 Stage B merge path** | **✓ CLOSED 2026-05-20 EOD++++++++++++++** | Grant adjudicated Path 1; Stage A fix + Stage B revision landed clean; paired Q-HWMOD-04 in AVE-Hardware-Modules also CLOSED |

## Sibling-repo update queue

The following sibling-repo files contain cross-refs to old `_orchestration/exp-c15-cleave-01-*.md` paths that need walk-back to the new `_orchestration/experimental/c15-cleave-01/...` structure. **NOT modified in this implementor session — orchestrator dispatches sibling-repo cross-ref updates on separate branches per sibling.**

| Sibling repo | File | Cross-ref count to update |
|---|---|---|
| `AVE-Bench-FemtoElectrometer` | `CLAUDE.md` | TBD (grep `_orchestration/exp-c15` returns multiple matches) |
| `AVE-Bench-FemtoElectrometer` | `hardware/DESIGN_LOG.md` | TBD |
| `AVE-Bench-FemtoElectrometer` | `hardware/cad/_archive/2026-05-20_phase-1a-kicad-draft/README.md` | TBD |
| `AVE-Bench-FemtoElectrometer` | `.agents/HANDOFF.md` | TBD |
| `AVE-Bench-FemtoElectrometer` | `docs/procurement_action_items.md` | TBD |
| `AVE-Bench-FemtoElectrometer` | `docs/design/2026-05-20_initial_scoping.md` | TBD |
| `AVE-Bench-FemtoElectrometer` | `docs/open_questions.md` | TBD |
| `AVE-Bench-FemtoElectrometer` | `docs/glossary.md` | TBD |
| `AVE-Hardware-Modules` | `.agents/workflows/audit-modules.md` | TBD |
| `AVE-Hardware-Modules` | `.agents/HANDOFF.md` | TBD |

Walk-back rules:
- `AVE-Core/_orchestration/exp-c15-cleave-01.md` → `AVE-Core/_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md`
- `AVE-Core/_orchestration/exp-c15-cleave-01-sim-audit.md` → `AVE-Core/_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01-sim-audit.md`
- `AVE-Core/_orchestration/exp-c15-cleave-01-phase-0-scaffolding.md` → `AVE-Core/_orchestration/experimental/c15-cleave-01/_archive/exp-c15-cleave-01-phase-0-scaffolding.md`
- `AVE-Core/_orchestration/exp-c15-cleave-01-q-c15-01-chamber-scoping.md` → `AVE-Core/_orchestration/experimental/c15-cleave-01/_archive/exp-c15-cleave-01-q-c15-01-chamber-scoping.md`
- `AVE-Core/_orchestration/exp-c15-cleave-01-phase-1-kicad-brief.md` → `AVE-Core/_orchestration/experimental/c15-cleave-01/_archive/exp-c15-cleave-01-phase-1-kicad-brief.md`
- `AVE-Core/_orchestration/exp-c15-cleave-01-phase-1a-rev1-atopile-walkback-brief.md` → `AVE-Core/_orchestration/experimental/c15-cleave-01/_archive/exp-c15-cleave-01-phase-1a-rev1-atopile-walkback-brief.md`
- `AVE-Core/_orchestration/experimental-arc.md` → `AVE-Core/_orchestration/experimental/experimental-arc.md`
- `AVE-Core/_orchestration/promotion-workflow-template.md` → `AVE-Core/_orchestration/experimental/promotion-workflow-template.md`

## Substrate readiness

| Asset | State |
|---|---|
| KB leaf | [`vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md`](../../../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md) — REFRESHED 2026-05-20 EOD+++++++++ post Phase 1a merge |
| PCBA design | atopile-native at `AVE-Bench-FemtoElectrometer/hardware/cleave_01.ato` (Stage B branch `b44b1f7`); imports 8 modules from `AVE-Hardware-Modules` (main `e2171cb`) via direct-part-import workaround |
| Driver | None — bench-only experiment |
| Hardware | NONE physical yet; Phase 1c Gerbers → Phase 2 fab |

## Skill discipline

- `ave-canonical-leaf-pull` v1.2 trigger 8: this is a NEW HARDWARE BUILD touching Ax2 — leaf-pull enumerated ξ_topo canon (INVARIANT-C2 + translation-tables/translation-circuit + Vol 4 Ch 1 VCA) before KiCad design started; honored across Phase 0 → Phase 1a-rev1.
- `ave-prereg` discipline at Phase 3 BEFORE measurement (Q-C15-02 closure gate).
- `ave-discrimination-check` Step 1.5: Outcome A/B/C/D enumerated above; pre-register before Phase 3 measurement.
- `substrate-native-check`: electrometer model verified K4-substrate-native (Phase 0 implementor confirmed; ξ_topo bridges K4 lattice geometry to bench charge via Ax2 [Q]≡[L]).
- `ave-evidence-framing-discipline`: precision claims on slope vs noise floor.
- `verify-before-cite` v1.4: all cross-references to ξ_topo numerical value (e/ℓ_node) verified against [`src/ave/core/constants.py`](../../../src/ave/core/constants.py).
- `ave-walk-back`: applied across Q-C15-10 atopile walk-back (preserved KiCad-native artifacts in `_archive/` rather than delete).
- `ave-ip-divide-discipline`: PATENTS.md in `AVE-Hardware-Modules` adapts VacuumMirror precedent for module-library IP scope (modules = bench-engineering IP separable from any specific design).

## Cross-references

### Canonical AVE physics
- [INVARIANT-C2 ξ_topo electromechanical transduction constant](../../../manuscript/ave-kb/CLAUDE.md) — canonical definition
- [Translation-Tables: Circuit Analysis (Topo-Kinematic Identity)](../../../manuscript/ave-kb/common/translation-tables/translation-circuit.md) — [Q]≡[L] full translation
- [Universal Saturation-Kernel Catalog A-034](../../../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) — Cleave operates at sub-V_yield Regime I
- [Four Universal Regimes — Regime I](../../../manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) — Cleave is small-signal linear regime
- [Power-Domain Classification](../../../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md) — reactive-only electrometer cycling
- [Temporal Saturation Regime Classifier](../../../manuscript/ave-kb/common/temporal-saturation-regime-classifier.md) — Cleave is in **lossless temporal regime** ($\delta_{AVE} \to 0$); pure-reactive electrometer

### Matrix + downstream cascade
- [Matrix row C15-CLEAVE-01](../../../manuscript/ave-kb/common/divergence-test-substrate-map.md)
- **Cascade dependents** (all fall if C15 returns Outcome C):
  - B4-PROTEIN (ξ_topo in Ramachandran enforcement)
  - C9-LEVITATION ($m_{max} = V_{yield} \cdot \xi_{topo} / g$)
  - C16-TORSION-05 (thrust uses ξ_topo)
  - B5-PONDER-01 (thrust uses ξ_topo)
  - B6-PONDER-02 (microwave probe uses ξ_topo)
  - B7-PONDER-05 (differential parallax uses ξ_topo)

### KB leaf
- [`project-cleave-01.md`](../../../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md) — refreshed 2026-05-20 EOD+++++++++ post Phase 1a merge

### Engine constants
- [`src/ave/core/constants.py`](../../../src/ave/core/constants.py) — ξ_topo canonical numerical value (verify before any KiCad design)

### Sibling-repo cross-refs
- **AVE-Bench-FemtoElectrometer** ([GitHub](https://github.com/ave-veritas-et-enodatio/AVE-Bench-FemtoElectrometer)) — bench-engineering sibling; main @ `331a778`; Phase 1a-rev1 branch @ `b44b1f7` pushed not merged
- **AVE-Hardware-Modules** ([GitHub](https://github.com/ave-veritas-et-enodatio/AVE-Hardware-Modules)) — atopile-modules sibling; main @ `e2171cb`; established 2026-05-20 EOD+++++++++++ via Q-C15-10 walk-back

### Archived briefs (closed phases)
- [`_archive/exp-c15-cleave-01-phase-0-scaffolding.md`](_archive/exp-c15-cleave-01-phase-0-scaffolding.md) — Phase 0 scaffold brief (closed 2026-05-20 EOD+++++)
- [`_archive/exp-c15-cleave-01-q-c15-01-chamber-scoping.md`](_archive/exp-c15-cleave-01-q-c15-01-chamber-scoping.md) — Q-C15-01 chamber scoping (closed 2026-05-20 EOD+++++)
- [`_archive/exp-c15-cleave-01-phase-1-kicad-brief.md`](_archive/exp-c15-cleave-01-phase-1-kicad-brief.md) — Phase 1 KiCad brief, predecessor (closed 2026-05-20 EOD++++++++ then walked back via Q-C15-10)
- [`_archive/exp-c15-cleave-01-phase-1a-rev1-atopile-walkback-brief.md`](_archive/exp-c15-cleave-01-phase-1a-rev1-atopile-walkback-brief.md) — Phase 1a-rev1 atopile walk-back brief (Stages A + B both landed; Stage B branch pushed not merged pending Q-C15-12)

### Sibling audit
- [`exp-c15-cleave-01-sim-audit.md`](exp-c15-cleave-01-sim-audit.md) — Framework-readiness audit (2026-05-20 EOD+++) — 🟢 NO BLOCKING DRIFT verified on 5 axes (ξ_topo + Ax2 + 6 cascade dependents + KB-leaf prediction + recent corpus spot-check)

## Audit trail

Note: full original-brief content for each closed phase is preserved at [`_archive/`](_archive/) — these entries are the dated canonical audit-trail summary. Per ave-walk-back discipline: archived briefs retain their as-of-archive state (banner header redirects readers to this consolidated doc).

- 2026-05-20 — Sub-epic established from Phase 2 cascade-emphasis ranking (Σ=10, cascade SIZE winner — largest single-row cascade 6+ dependents). Phase 0 scoping decision pending.
- 2026-05-20 EOD+++ — **Framework-readiness audit** landed at [`exp-c15-cleave-01-sim-audit.md`](exp-c15-cleave-01-sim-audit.md). Five axes verified empirically: ξ_topo canonical 4.149×10⁻⁷ C/m (per `src/ave/core/constants.py:205`), Ax2 [Q]≡[L] canonical statement preserved (per `ave-kb/CLAUDE.md` INVARIANT-S2 Axiom 2), 6 cascade dependents still load-bearing (B4 + C9 + C16 + B5/B6/B7), KB-leaf 41.5 mV/μm prediction reproduces arithmetically from current canonical constants (computed: 41.490 mV at 10 pF on 1 μm displacement), recent corpus drift spot-check (A-034 + Class E + temporal regime + FI-13 + C8 + Q-G47 + C1 + C11 + A1-HOPF) → all orthogonal to C15 axes. Q-G47 Sessions 19 ξ_K1/K2 vs ξ_topo identified as naming-collision (different ξ; not a drift). **Verdict 🟢 NO BLOCKING DRIFT.** Phase 0 theoretical-side ready; design-side gated on Grant scoping decision (not theoretical re-derivation).
- 2026-05-20 EOD++++ — **Phase 0 Grant adjudication ✓ A3 scaffold-only + B1 standalone sibling repo.** Scaffold brief landed at [`_archive/exp-c15-cleave-01-phase-0-scaffolding.md`](_archive/exp-c15-cleave-01-phase-0-scaffolding.md). Target sibling repo: `AVE-Bench-FemtoElectrometer` (NEW; parallels AVE-Bench-VacuumMirror precedent). Decision rationale: A3 chosen over A1 pure-pursue because VacuumMirror precedent shows value of open-questions discipline before KiCad work; B1 chosen because per-experiment-sibling-repo pattern + IP boundary alignment + PEP 420 namespace cleanliness; B3 PONDER rejected (atopile vs KiCad tooling collision + PONDER transferable-knowledge claim was at SCIENCE not BENCH level). Six open questions (Q-C15-01 to Q-C15-06) drafted in brief: chamber priority, pre-reg precision target, discriminator dielectric choice, parasitic-C control, PZT outgassing, triboelectric confound discrimination. Implementor dispatch follows orchestration commit.
- 2026-05-20 EOD+++++ — **PHASE 0 SCAFFOLD ✓ LANDED.** `ave-implementer` returned with single clean commit `0b05bd4` on `main` at `/Users/grantlindblom/AVE-staging/AVE-Bench-FemtoElectrometer/`. 36 files (29 substantive + 7 .gitkeep), 2686 lines added. All 8 success criteria from brief met: repo exists + structure-parity with VacuumMirror + KB-leaf prediction preserved verbatim (41.5 mV/μm + 0.415 pC + outcome A/B/C/D + "if 0.0 mV the framework is falsified") + 6 open questions captured (Q-C15-01 to Q-C15-06) + cross-references back to AVE-Core valid + no KiCad/no measurement scripts (hardware/cad + scripts/ are placeholders) + pure-AVE-corpus grep returns zero + framework-readiness audit cross-ref captured in docs/design/2026-05-20_initial_scoping.md. `substrate-native-check` PASSED on electrometer model (ξ_topo bridges K4 lattice geometry to bench charge via Ax2 [Q]≡[L]; substrate-native, not QED-borrowed); no Q-C15-07 surfaced. No remote configured per brief constraint #6 — Grant handles `gh repo create ave-veritas-et-enodatio/AVE-Bench-FemtoElectrometer --private` + `git remote add origin` + `git push -u origin main`. Phase 0 deliverable list passed verification audit (commit hash + file count + grep checks confirmed). Phase 0→1 promotion blocked on (i) GitHub remote setup [trivial, Grant authorization needed] + (ii) Q-C15-01 chamber priority resolution [Phase 1 KiCad entry gate].
- 2026-05-20 EOD+++++ — **Cross-precedent flag (FLAG-DON'T-FIX)**: brief §"Post-scaffold orchestration walk-back" claimed `vacuum-impedance-mirror.md` cross-refs to AVE-Bench-VacuumMirror sibling — empirical check found this is NOT the case (grep returned 0 matches for "vacuummirror|vacuum-mirror|sibling repo|AVE-Bench" in that KB leaf). The actual precedent is **one-way from sibling repo → AVE-Core**, not bidirectional. C15 KB-leaf refresh proceeds independently of the precedent claim because the KB leaf has a STALE "Engineering substrate status" section that explicitly says "no KiCad / no hardware in any AVE repo yet" (now false — scaffold sibling repo exists). Refresh is justified on stale-section grounds, not bidirectional-cross-ref grounds.
- 2026-05-20 EOD+++++ — **Q-C15-01 chamber priority scoping doc landed** at [`_archive/exp-c15-cleave-01-q-c15-01-chamber-scoping.md`](_archive/exp-c15-cleave-01-q-c15-01-chamber-scoping.md). Four-experiment chamber-profile comparison surveyed via verify-before-cite v1.4 grep on bench-engineering TEST_PROCEDUREs + KB leaves + PONDER ch.5 manuscript: C15 (≤10⁻⁶ Torr, NONE HV, NONE optical, fixed-mount PCBA + PZT) vs AVE-Bench-VacuumMirror (≤10⁻⁹ UHV, 35-43 kV DC, YES optical + 10" CF chamber) vs C16-TORSION-05 (10⁻⁶ Torr, ±75 kV inductive spike, Cavendish torsion balance + suspension) vs B5-PONDER-01 (10⁻⁵ Torr, multi-axis HV + AC modulation, quartz piezo / torsion balance). Three candidate paths evaluated: C1 dedicated chamber RECOMMENDED, C2 share-with-VacuumMirror REJECTED (pressure-tier overkill + HV-noise floor risk + optical-port contention), C3 share-with-PONDER/TORSION REJECTED (EXTREME ±75 kV noise + suspended-vs-fixed-mount incompatibility + future-tense schedule risk).
- 2026-05-20 EOD+++++ — **Q-C15-01 ✓ RESOLVED — Grant adjudicated DEDICATED CHAMBER** (path C1). Walk-back propagated to AVE-Bench-FemtoElectrometer at commit `9a768bd` (local-only): `docs/open_questions.md` Q-C15-01 OPEN → CLOSED with rejected-paths rationale + implementation notes; Q-C15-05 (PZT outgassing UHV) scope-narrowing note added (10⁻⁶ Torr is NOT UHV → commodity PI N-216-grade PZT likely sufficient; UHV-specialty path deferred); `docs/procurement_action_items.md` §A header walked back from "Q-C15-01 decision pending" to "Q-C15-01 ✓ RESOLVED dedicated path active"; A.1 decision-gate Q-C15-01 checked off; A.2-A.4 sourcing actions activated. **Cost reconciliation flag**: scoping doc estimated "$500-2k" chamber-alone (bell-jar tier); procurement doc full subsystem-A (chamber refurb ≤$1.5k + pumping ≤$3k + feedthroughs ≤$500) is ~$4-5k mid-range; both numbers correct at their respective scopes. Phase 0→1 promotion blocker (ii) flipped OPEN → CLOSED; remaining blockers: (i) Grant GitHub remote authorization + (iii) Grant Phase 0→1 promotion adjudication.
- 2026-05-20 EOD++++++ — **(i) GitHub remote ✓ LIVE + (iii) Phase 0→1 ✓ PROMOTED.** Grant authorized both remaining blockers. (i) `gh repo create ave-veritas-et-enodatio/AVE-Bench-FemtoElectrometer --private --source=. --remote=origin --push` executed cleanly; repo live at `https://github.com/ave-veritas-et-enodatio/AVE-Bench-FemtoElectrometer` (private); branch `main` tracks `origin/main`; both commits `0b05bd4` scaffold + `9a768bd` Q-C15-01 walk-back pushed. (iii) Phase 1 KiCad design brief landed at [`_archive/exp-c15-cleave-01-phase-1-kicad-brief.md`](_archive/exp-c15-cleave-01-phase-1-kicad-brief.md) — full Phase 1 scope (D1.1-D1.10) decomposed into Phase 1a (sub-agent-doable: ADA4530-1 reference notes + finalized BOM + KiCad schematic DRAFT + TEST_PROCEDURE update + procurement SKU population + ORDERING + DESIGN_LOG skeletons), Phase 1b (PCB layout — Grant manual or specialized session), Phase 1c (Gerbers + DRC — Grant manual via kicad-cli). Phase 1a implementor dispatched in background; branch `analysis/phase-1a-kicad-design` off `main`; implementor instructions include 11 constraints (pure-AVE-corpus, canonical-source compliance, KB-leaf prediction verbatim preservation, Q-C15-01/04/05 resolution honoring, etc.) + 10 success criteria + cross-reference list to AVE-Core canonical content + sibling-repo state + orchestration docs.
- 2026-05-20 EOD+++++++ — **Phase 1a ✓ LANDED on branch `analysis/phase-1a-kicad-design` (commit `f743bae`; pushed to origin; NOT merged to main per brief constraint #9).** 9 files / 1607 insertions + 134 deletions. All 7 in-scope deliverables COMPLETE (D1.1 + D1.2 + D1.3-draft + D1.7 + D1.8 + D1.9 + D1.10). Verification via verify-before-cite v1.4: branch + remote push confirmed; KB-leaf prediction verbatim preserved (9 grep hits for "41.5"/"0.415 pC"/"framework is falsified" in TEST_PROCEDURE.md); Q-C15-07/08/09 surfaced in docs/open_questions.md (3 grep hits); pure-AVE-corpus grep on new hardware files returns ZERO matches. Files delivered: `hardware/cad/reference_design.md` (NEW 321L, D1.1 ADA4530-1 + EVAL-board topology + guard-ring + Teflon + supply network + sub-D feedthrough pinout), `hardware/BOM.md` (REPLACED 172L, D1.2 concrete Mouser/Digi-Key/KJL/LabX/PI/PiezoDrive/Thorlabs/Pico/DER-EE SKUs), `hardware/cad/cleave_01_schematic.kicad_sch` (NEW 382L S-expression, D1.3 canonical; ERC-clean NOT pursued per brief best-effort clause), `hardware/cad/cleave_01_schematic.md` (NEW 168L ASCII companion, D1.3 fallback contingency), `hardware/TEST_PROCEDURE.md` (MODIFIED, D1.7 SKU refresh; KB-leaf prediction verbatim), `docs/procurement_action_items.md` (MODIFIED 137L, D1.8 SKU population + budget rollup), `hardware/ORDERING.md` (NEW 223L, D1.9 skeleton; §2 PCB fab marked PENDING until Phase 1b/1c), `hardware/DESIGN_LOG.md` (NEW 235L, D1.10 design-decision log + KB-leaf→KiCad translation rationale + open decisions). BOM mid-range rollup: $7670 ($5450 chamber subsystem + $1230 PCBA + drive + $994 auxiliary) — within procurement §E mid-range estimate. **3 new open questions surfaced (per flag-don't-fix discipline)**: Q-C15-07 PZT drive line routing (shared FT3 vs dedicated FT2 — $245 cost decision), Q-C15-08 floating-plate ground return (chamber-wall implicit vs PTFE-socket explicit), Q-C15-09 PCBA chassis ground tie (external-only via FT1 BNC shield vs chamber-internal lug). **Implementor surface deviations**: D1.3 ASCII companion engaged per brief contingency clause; WebFetch tool blocked by sandbox timeout (ADI datasheet URLs preserved in citations table for Grant Phase 1b verification pass — no content shortfall, all pinouts/topology/supply ranges reproduced from canonical ADA4530-1 knowledge); C1 alt SKU (Kemet C0805 ±0.25 pF) added as Phase 2 contingency for Q-C15-04 tighter-tolerance escalation if needed. Pre-existing `.agents/workflows/audit-math.md` (Phase 0 scaffold) contains "pitch" in physics-legitimate "lattice pitch" — flagged for Grant awareness but NOT in Phase 1a cleanup scope (pre-existing not introduced). **Implementor recommended next-step entry**: Grant pre-merge review on (a) schematic topology, (b) BOM SKU choices, (c) Q-C15-07/08/09 adjudication, (d) DESIGN_LOG §3 decision 1.2 (DAC + HV amp on-PCBA vs off-PCBA — affects schematic topology if flipped) BEFORE Phase 1b dispatch; if review passes: merge to main with `--no-ff` + audit tag per AVE-Bench-FemtoElectrometer/AVE-HOPF branching pattern, then Phase 1b PCB layout (Grant manual KiCad GUI work highest-confidence path given sub-agent tooling limitation on DRC + Gerbers).
- 2026-05-20 EOD++++++++ — **Phase 1a ✓ MERGED to main** at merge commit `331a778` on `main`; audit tag `audit/2026-05-20_phase-1a-kicad-design` at `6d6552f` (branch tip pre-merge); analysis branch deleted local + remote. Grant pre-merge review adjudicated all 4 items: (a) schematic topology OK (KiCad GUI cleanup deferred to Phase 1b per brief best-effort clause), (b) BOM SKU choices approved ($7670 mid-range rollup accepted), (c) Q-C15-07 ✓ CLOSED dedicated FT2 feedthrough, Q-C15-08 ✓ CLOSED dedicated PTFE-socket explicit return, Q-C15-09 ✓ CLOSED external-only via FT1 BNC shield, (d) Q1.2 DESIGN_LOG §3 ✓ CLOSED off-PCBA DAC + HV amp (Phase 1a default confirmed as final; Phase 2.5 on-PCBA consolidation NOT pursued). **Combined Q-C15-08 + Q-C15-09 topology**: ALL grounds (floating-plate signal return + chassis ground) leave the chamber via explicit dedicated paths; no chamber wall in the ground network → cleanest electrical isolation for femto-Coulomb measurement. Adjudications captured on branch commit `6d6552f` before merge (docs/open_questions.md Q-C15-07/08/09 OPEN → CLOSED + hardware/DESIGN_LOG.md §3 decision 1.2 + §4 Q-C15-07/08/09 candidate headers walked back to ✓ CLOSED). Phase 1b pending Grant manual KiCad GUI work (schematic ERC clean + PCB layout + guard-ring polygon + DRC) per DESIGN_LOG §5.1-5.2; Phase 1c Gerbers via `kicad-cli pcb export gerbers` per DESIGN_LOG §5.3.
- 2026-05-20 EOD+++++++++ — **Q-C15-10 ✓ Grant adjudicated atopile (HOPF pattern + new sibling repo `AVE-Hardware-Modules`).** Phase 1a delivered KiCad-native `.kicad_sch` — a workspace deviation from the established atopile-first pattern across AVE-PONDER (`metric_decoherence.ato`) + AVE-HOPF (`hopf_01.ato` + `hopf_02.ato`). Grant adjudicated Option A: new sibling repo for atopile modules. **Phase 1a-rev1 atopile walk-back brief landed** at [`_archive/exp-c15-cleave-01-phase-1a-rev1-atopile-walkback-brief.md`](_archive/exp-c15-cleave-01-phase-1a-rev1-atopile-walkback-brief.md). Two-stage execution: Stage A (`AVE-Hardware-Modules` sibling repo scaffold + 8 modules + tests + remote create + push); Stage B (gated on A return; C15 atopile walk-back at `hardware/cleave_01.ato` + decommission orphan `.kicad_sch` + ASCII companion to `hardware/cad/_archive/` + Q-C15-10 OPEN → CLOSED + Q-C15-11 NEW OPEN). Module-audit pass expanded initial 5-module decomposition to 8 modules after gap analysis: precision_input_cap_10pf pulled out (Q-C15-04 KB-loadbearing); ptfe_turret_post_standoff added (missed in first pass); sub-D interface split into subd9_supply_header + molex3_pzt_header (Q-C15-07 dedicated FT2 topology). Cross-repo sync tracking Q-C15-11 / Q-HWMOD-01 paired in both repos (track-only; no active migration). AVE-Bench-FemtoElectrometer `main` at `331a778` remains as predecessor state being walked back; Phase 1a-rev1 lands on new branch `analysis/phase-1a-rev1-atopile-walkback`.
- 2026-05-20 EOD+++++++++++ — **Stage 1a-rev1-A ✓ COMPLETE.** `ave-implementer` returned with single clean initial commit `e2171cb` on `main` at `/Users/grantlindblom/AVE-staging/AVE-Hardware-Modules/`. 68 tracked files (~2018 lines of textual content across .ato + .md + .yaml + .toml + .sh + .kicad_sym + .kicad_mod + Makefile + LICENSE + fp-lib-table). **All 9 Stage A success criteria PASSED**: repo created on GitHub + structure parity with VacuumMirror + 8 modules present + 9 parts subdirs (8 primary + 1 Kemet ±0.25 pF alt) + 8 smoke tests `ato build` clean on atopile 0.12.5 + ato.yaml valid + Q-HWMOD-01 captured + pure-AVE-corpus grep clean (matches in AGENTS.md/CLAUDE.md are rule-statement lines per word-boundary discipline) + remote `https://github.com/ave-veritas-et-enodatio/AVE-Hardware-Modules` LIVE (private). **Atopile syntax notes captured by implementor** (Q-HWMOD-03 closed inline): atopile 0.12.5 requires `#pragma experiment("TRAITS")` for trait keyword (PONDER LCSC-generated parts pattern); implementor used HOPF inline `footprint = "..."` pattern instead (cleaner for hand-authored module-library); `footprint` value must be `<libname>:<footprint>` format (bare-name fails at PCB-update with LibNotInTable); atopile auto-creates `elec/layout/<build>/` but does NOT auto-seed `fp-lib-table` (implementor scaffolded per-build with `${KIPRJMOD}/../../../parts/` relative URIs); atopile 0.12.5 builds ALL `builds:` entries from CLI invocation (convenient for full smoke verification). **2 new open questions surfaced + 1 closed inline**: Q-HWMOD-01 cross-repo sync (paired with Q-C15-11 in AVE-Bench-FemtoElectrometer) track-only; Q-HWMOD-02 Mill-Max + Keystone specialty-part footprint accuracy (Phase 1b PCB layout review); Q-HWMOD-03 smoke-test PCB-update plumbing CLOSED 2026-05-20 inline (resolved via footprint lib:name format + fp-lib-table seeding). **Implementor deviations from brief**: no datasheet.pdf files committed (gitignored per .gitignore; URLs in .ato docstrings); no .step 3D model files (optional per brief); fp-lib-table files added per-build (required for `ato build` clean-pass; documented as Q-HWMOD-03 resolution). Stage B dispatch follows orchestration commit.
- 2026-05-20 EOD++++++++++++ — **Stage 1a-rev1-B ✓ LANDED on branch `analysis/phase-1a-rev1-atopile-walkback` (3 commits at `b44b1f7`; pushed to origin; NOT merged).** Commits: `b7e9a1e` D3 archive orphan KiCad-native draft + `eb70e77` D1+D2 atopile-first PCBA design + `b44b1f7` D4-D8 docs walk-back propagation. **All 9 deliverables COMPLETE + 12 success criteria PASSED** (verified via Read + grep): cleave_01.ato (16031 bytes; module CleaveOne composes 8 module imports + 4 direct-part imports per Q-C15-12 workaround); ato.yaml (`requires-atopile: ^0.12.0`; build entry `cleave_01.ato:CleaveOne`); orphan archive to `hardware/cad/_archive/2026-05-20_phase-1a-kicad-draft/` with README.md (verified files present + git mv preserved); DESIGN_LOG §7 NEW with 10 subsections; BOM Subsystem 1.5 module-of-origin cross-ref; TEST_PROCEDURE path refresh (KB-leaf verbatim preserved — 9 grep hits for "41.5"/"0.415"/"OUTCOME"/"Ax2 DIES" unchanged); ORDERING §2.0 atopile workflow; docs/open_questions.md Q-C15-10 ✓ CLOSED + Q-C15-11 + Q-C15-12 NEW OPEN; pure-AVE-corpus grep ZERO matches; `ato build` clean on atopile 0.12.5. **Q-C15-12 NEW OPEN — Stage A latent bugs surfaced at integration time** (per Rule 10 empirical-driver discipline): (i) `AVE-Hardware-Modules/modules/mill_max_ptfe_socket.ato` line 17 exposes `signal = new Electrical` — verified by grep — but `signal` is reserved `signaldef_stmt` keyword in atopile 0.12.5; consumer-side `.signal` access fails parsing; (ii) `AVE-Hardware-Modules/modules/ptfe_turret_post_standoff.ato` line 85 references `tp.2 ~ pad_b` — verified by grep — but Keystone_1610_3_package declares only `pin 1`; module compile fails at consumer instantiation; (iii) `AVE-Hardware-Modules/ato.yaml` lacks `package:` block required for `ato install` consumability in atopile 0.12.5 (Stage A's `git+https://` syntax in brief was forward-looking; actual 0.12.5 syntax: `registry://` / `git://` / `file://`, with target `package:` block prerequisite). **Stage B workaround**: direct-part imports of `MillMax_3320_2_package` + `Keystone_1610_3_package` parts in cleave_01.ato (semantically equivalent to module-level imports). Stage A smoke tests passed because they never accessed broken fields (black-box per-module compile); Stage B's integration-time consumer wiring caught the bugs. **3 atopile 0.12.5 workflow surprises captured**: (a) `dependencies:` spec in 0.12.5 is `registry://` / `git://` / `file://`, NOT `git+https://` from brief; (b) fp-lib-table per-build seeding required at consumer scale 5 `../` URI depth (vs Stage A smoke-test 3 `../`); (c) net resolution stub on first build (atopile emits minimal `.kicad_pcb` with footprints but empty `(nets)` in `.net`; KiCad GUI fills on first open). **Merge decision pending Grant**: Q-C15-12 path (fix Stage A first vs merge Stage B as-is + separate fix-branch in AVE-Hardware-Modules) gates the audit-tag + merge sequence. Stage B branch held at origin; pre-merge review queue includes Q-HWMOD-04 paired entry needed in AVE-Hardware-Modules.
- 2026-05-20 EOD+++++++++++++ — **Phase B orchestration-hygiene reorganization** (this commit): `_orchestration/` subdirectory hierarchy established (`experimental/c15-cleave-01/` + `_archive/`). C15 sub-epic consolidated into single doc with phase table + per-active-phase detail; 4 closed-phase briefs (phase-0-scaffolding + q-c15-01-chamber-scoping + phase-1-kicad-brief + phase-1a-rev1-atopile-walkback-brief) archived to `_archive/` with ARCHIVED header banners pointing back to this consolidated doc. All cross-refs in AVE-Core (CLAUDE.md + index.md + KB leaves) updated to new paths. Sibling-repo cross-ref updates queued for orchestrator follow-up per `## Sibling-repo update queue` section above. No content loss; all original briefs preserved verbatim in `_archive/`; all dated audit-trail entries above preserved.
- 2026-05-20 EOD++++++++++++++ — **Q-C15-12 ✓ CLOSED via Path 1 — Phase 1a-rev1 FULLY MERGED.** Stage A landed at `AVE-Hardware-Modules` main @ `8b0626b` (audit tag `audit/2026-05-20_q-c15-12-stage-a-fix` at `a68b2f4`; pushed to origin; branch deleted local+remote): D1 `signal`→`sig` rename in `mill_max_ptfe_socket.ato:80,86`; D2 phantom `tp.2~pad_b` removed in `ptfe_turret_post_standoff.ato` (Keystone 1610-3 declares only pin 1; pad_b was architectural error); D3 `package:` block added to `ato.yaml` (with atopile 0.12.5 PackageConfig schema drift surfaced: `identifier:` not `name:`, `summary:` not `description:`, `authors: [{name,email}]` not `[str]`); D4 all 8 smoke tests rewritten for consumer-wiring exercise (Rule 1 of `ave-module-library-discipline v1.0`; each test creates dummy `interface Electrical` + nets + wires every exposed field; all 8 `ato build` clean); D5 Q-HWMOD-04 OPEN→CLOSED in AVE-Hardware-Modules/docs/open_questions.md. Stage B landed at `AVE-Bench-FemtoElectrometer` main @ `7f9c721` (audit tag `audit/2026-05-20_phase-1a-rev1-atopile-walkback` at `132bf14`; pushed to origin; branch deleted): D7 cleave_01.ato direct-part workarounds removed + clean `MillMaxPtfeSocket` + `PtfeTurretPostStandoff` module-level imports added (wiring uses `.sig` + `.pad_a` accessors); D8 `dependencies:` block COMMENTED due to atopile 0.12.5 upstream bug — `FileDependencySpec` triggers `AssertionError` in `faebryk/libs/project/dependencies.py:147` (`target_path` reads `.dist.identifier` before `load_dist()` populates `.dist`); workaround = relative-path imports active; backlog: retest after atopile 0.15.x upgrade; D9 Q-C15-12 OPEN→CLOSED; D10 DESIGN_LOG §7.11 closure note; D11 `ato build` clean. Pre-merge sanity check on `j3_ground.sig ~ n_gnd` confirmed semantically clean (`MillMaxPtfeSocket` is intentionally role-agnostic at interface level; both instances expose `sig`; consumer wiring assigns to signal or gnd net based on role per Q-C15-08 dedicated PTFE-socket explicit ground return). **All Q-C15-10/11/12 + Q1.2 + Q-HWMOD-04 now CLOSED.** **`ave-module-library-discipline v1.0` first-fire** — Rules 1-5 all applied + cited in both Stage A `a68b2f4` + Stage B `132bf14` commits. KB-leaf prediction verbatim preserved (9 grep hits for "41.5"/"0.415 pC"/"OUTCOME"/"framework is falsified" unchanged); pure-AVE-corpus grep ZERO matches across all new artifacts in both repos.

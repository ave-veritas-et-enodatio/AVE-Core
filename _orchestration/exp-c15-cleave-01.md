# EXP-C15-CLEAVE-01: Femto-Coulomb Electrometer ($Q = \xi_{topo} \cdot x$)

**Parent epic**: [`experimental-arc.md`](experimental-arc.md)
**Status**: **PHASE 1 ACTIVE — Phase 0→1 PROMOTED + GitHub remote ✓ LIVE + Phase 1a implementor dispatched** ([`exp-c15-cleave-01-phase-1-kicad-brief.md`](exp-c15-cleave-01-phase-1-kicad-brief.md), 2026-05-20 EOD++++++). Sibling repo: `https://github.com/ave-veritas-et-enodatio/AVE-Bench-FemtoElectrometer` (private; commits `0b05bd4` scaffold + `9a768bd` Q-C15-01 walk-back pushed to origin/main). Phase 0 ✓ COMPLETE: scaffold landed + Q-C15-01 ✓ RESOLVED dedicated chamber + Q-C15-05 scope narrowed + framework-readiness audit NO DRIFT.
**Owner**: **AVE-Bench-FemtoElectrometer** sibling repo at GitHub + `/Users/grantlindblom/AVE-staging/AVE-Bench-FemtoElectrometer/` — parallels AVE-Bench-VacuumMirror precedent
**Established**: 2026-05-20 from Phase 2 cascade-emphasis ranking

## Tier (per parent epic Phase 2 audit)

Cascade SIZE winner — largest single-row cascade in matrix (6+ dependent rows in ξ_topo family). Composite Σ=10. R=0 (PCBA spec in KB only), D=3 (U-D, KB-explicit falsification: "if 0.0 mV, the framework is falsified"), S=3 (F-severity, Ax2 dies), C=2 (~$1-5k bench), X=3 (ξ_topo family: B4 + C9 + C16 + B5 + B6 + B7).

## Premise

Cleave-01 tests **Axiom 2 (Topo-Kinematic Isomorphism, [Q] ≡ [L])** directly at the bench. The canonical electromechanical-transduction constant $\xi_{topo} = e/\ell_{node}$ (INVARIANT-C2 per [`ave-kb/CLAUDE.md`](../manuscript/ave-kb/CLAUDE.md)) bridges AVE lattice parameters and mechanical/biological quantities. If a mechanical displacement $x$ induces topological charge $Q = \xi_{topo} \cdot x$, then a precision electrometer reading the charge across a PZT-stepped capacitor measures $\xi_{topo}$ directly.

**KB explicit prediction**: $41.5 \,\text{mV}$ per $1 \,\mu\text{m}$ displacement on a $10 \,\text{pF}$ input. $0.415 \,\text{pC}$ charge per step.

**KB explicit falsification statement** (literal): *"if 0.0 mV, the framework is falsified."*

**Cascade reach** — ξ_topo appears in:
- **B4-PROTEIN** (Ramachandran enforcement uses ξ_topo per Vol 5 protein-folding engine)
- **C9-LEVITATION** ($m_{max} = V_{yield} \cdot \xi_{topo} / g$)
- **C16-TORSION-05** (Project TORSION-05 thrust uses ξ_topo for V↔M coupling)
- **B5-PONDER-01** + **B6-PONDER-02** + **B7-PONDER-05** (all PONDER thrust derivations use ξ_topo at V_yield boundary)

If C15-CLEAVE-01 fails (0.0 mV observed), Ax2 dies → ALL 6 downstream rows fall + the framework's electromechanical-bridge axiom is killed.

## Standard EE counterfactual

A standard capacitor with PZT actuator generates charge via mechanical strain on the dielectric (piezoelectric effect $d_{31}$ etc.), but NOT via a TOPOLOGICAL charge-length identity. The AVE prediction is that the OBSERVED charge has an additional component $Q_{topo} = \xi_{topo} \cdot x$ that scales LINEARLY with displacement (not with the dielectric's $d_{ij}$ coefficients). Discriminator: vary dielectric without changing PZT displacement — standard EE predicts $Q$ varies with dielectric; AVE predicts the $\xi_{topo} \cdot x$ component is dielectric-independent.

## Current state

### Substrate readiness

| Asset | State |
|---|---|
| KB leaf | [`vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md) (2026-04-13) — STALE; needs walk-back |
| PCBA design | Spec only in KB leaf; **no KiCad / no hardware in any AVE repo** |
| Driver | None — bench-only experiment |
| Hardware | None |

### KB-specified BOM (extracted from leaf)
- ADA4530-1 electrometer-grade op-amp (Texas Instruments)
- 10 pF precision capacitor input
- PZT actuator (1 μm step resolution; commercial)
- DAC for PZT drive
- Vacuum chamber (eliminate humidity-induced parasitic conductance)
- Guard ring enclosure (per ADA4530-1 datasheet recommendation)
- Estimated cost: $1-5k bench (low-end of bench-class)

### Walk-back targets (Phase 1 of parent epic)

| Leaf | Stale state | Refresh |
|---|---|---|
| [`project-cleave-01.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md) (2026-04-13) | Pre-canonical ξ_topo framing; missing cross-references to translation-tables/translation-circuit + temporal classifier + four-regimes | Refresh with explicit ξ_topo INVARIANT-C2 citation; add Power-Domain θ classification (electrometer is reactive cycling); add temporal-regime classification (lossless DC reactive at sub-yield); add cross-refs to translation-circuit table |

## Phase ladder

### Phase 0 (ACTIVE — A3 scaffold-only + B1 standalone sibling repo, Grant adjudicated 2026-05-20 EOD++++) — Sibling-repo scaffolding

**Action**: Spin up `AVE-Bench-FemtoElectrometer` standalone sibling repo per AVE-Bench-VacuumMirror precedent. Scaffold manuscript sub-volume + TEST_PROCEDURE.md + open-questions doc + design docs + glossary + .agents/ + cross-references back to AVE-Core canonical content. NO KiCad cycle yet (gated on Phase 0→1 promotion adjudication).

**Brief**: [`exp-c15-cleave-01-phase-0-scaffolding.md`](exp-c15-cleave-01-phase-0-scaffolding.md) — detailed implementor brief with deliverables, cross-references, skill discipline, success criteria.

**Decision context preserved**:
- A3 scaffold-only chosen over A1 pure-pursue: VacuumMirror precedent shows value of surfacing open-questions BEFORE KiCad work starts; low-cost (~1 implementor session) preserves optionality on chamber + dielectric + pre-reg-precision decisions
- B1 standalone sibling repo chosen over B2 AVE-Core/hardware/: matches VacuumMirror precedent; aligns with per-experiment-sibling-repo pattern; IP boundary clean; PEP 420 namespace extension keeps AVE-Core import-clean
- B3 in AVE-PONDER hardware/ REJECTED: PONDER hardware is atopile-based (single design); would create infrastructure tooling collision; "PONDER transferable knowledge" claim from sub-epic establishment was at SCIENCE level (V_yield + ξ_topo) not BENCH level (no PZT / ADA4530 / vacuum chamber in PONDER)

### Phase 1 (PENDING, gated on Grant Phase 0→1 promotion adjudication) — KiCad design from KB spec

**Action**: Translate [`project-cleave-01.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md) PCBA spec → KiCad schematic + layout. Reference ADA4530-1 evaluation board + datasheet guard-ring recommendations.

**Candidate implementor session brief**: scaffold KiCad design from KB spec + ADA4530-1 reference design + vacuum-chamber interface; deliver hopf-pattern fab package (Gerbers + BOM + assembly guide + test procedure).

**Time**: 1-2 weeks (typical KiCad design cycle for electrometer-class precision)

**Output**: `AVE-Core/hardware/cleave_01/` directory OR new `AVE-CLEAVE-01` sub-repo per workspace pattern (Grant decision)

### Phase 2 (PENDING, gated on Phase 1) — Fab + assembly

**Action**: Submit Gerbers to JLCPCB; order BOM components from Mouser/Digi-Key; assemble; install in vacuum chamber with PZT actuator + DAC drive.

**Time**: 2-3 weeks (fab + parts + assembly)
**Cost**: ~$1-5k

### Phase 3 (PENDING, gated on Phase 2) — Measurement

**Action**: Sweep PZT in 1 μm steps; record output voltage; verify $41.5 \,\text{mV} / \mu\text{m}$ slope on 10 pF input.

**Predicted observable**: $V_{out} = \xi_{topo} \cdot x / C_{in} = 41.5 \,\text{mV/μm}$ at $C_{in} = 10 \,\text{pF}$. Linear in $x$. Dielectric-independent (discriminator test: swap dielectric, verify slope unchanged within AVE prediction).

**Time**: ~1 week measurement + analysis

### Phase 4 (CONDITIONAL on Phase 3 outcome) — Outcome adjudication

| Outcome | Interpretation |
|---|---|
| **A**: $V_{out}$ matches $41.5 \,\text{mV/μm}$ within ADA4530-1 noise floor | **Ax2 confirmed at bench**. ξ_topo cascade (B4 + C9 + C16 + B5-7) all gain bench-scale corroboration. **Major positive — foreword-promotion-grade**. |
| **B**: $V_{out}$ detected but slope differs from $41.5 \,\text{mV/μm}$ | Partial. Topological charge-length identity holds (qualitatively positive), but $\xi_{topo}$ coefficient needs structural revision |
| **C**: $V_{out} \approx 0$ within noise floor (KB-explicit falsification condition) | **Ax2 dies. Framework falsified at substrate-foundational axiom level.** Cascade walk-back: B4 + C9 + C16 + B5-7 ALL fail. Major structural finding (framework-killing). |
| **D**: Confound (parasitic leakage / triboelectric / outgassing) | Discriminate from C via re-design with better guards; re-test |

**Outcome A** → write canonical result doc + matrix update across ENTIRE ξ_topo family + foreword promotion + skill-amendment (this becomes the canonical Ax2-bench-validation citation across all volumes).

**Outcome C** → framework-killing-level walk-back. Cosserat substrate hypothesis falsified at the electromechanical-transduction axiom. Major theoretical re-derivation needed.

## Open questions

1. **Sub-repo split**: should C15-CLEAVE-01 hardware live at `AVE-Core/hardware/cleave_01/` OR get its own `AVE-CLEAVE-01` sub-repo per workspace pattern? Grant call.
2. **Vacuum chamber priority**: chamber is shared apparatus with B5/B6/B7 PONDER + C16 TORSION-05 + others. Build dedicated vs schedule shared time?
3. **Pre-reg precision target**: at what slope-precision (per ADA4530-1 noise floor) is Outcome A vs B vs C confidently distinguished?
4. **Discriminator dielectric test**: which dielectric to swap for the dielectric-independence test? PTFE vs polyimide vs PCB FR-4?

## Skill discipline

- `ave-canonical-leaf-pull` v1.2 trigger 8: this is a NEW HARDWARE BUILD touching Ax2 — leaf-pull must enumerate ξ_topo canon (INVARIANT-C2 + translation-tables/translation-circuit + Vol 4 Ch 1 VCA) before any KiCad design starts.
- `ave-prereg` discipline at Phase 3 BEFORE measurement.
- `ave-discrimination-check` Step 1.5: Outcome A/B/C/D enumerated above; pre-register before Phase 3 measurement.
- `substrate-native-check`: verify the electrometer model is K4-substrate-native (not just QM-borrowing).
- `ave-evidence-framing-discipline`: precision claims on slope vs noise floor.
- `verify-before-cite` v1.4: all cross-references to ξ_topo numerical value (e/ℓ_node) verified against [`src/ave/core/constants.py`](../src/ave/core/constants.py).

## Sibling-repo coordination

No existing sibling-repo owner. Decision in Phase 0: candidate for new `AVE-CLEAVE-01` sub-repo OR live at `AVE-Core/hardware/cleave_01/`. AVE-PONDER scope overlaps (both use ξ_topo at V_yield boundary); PONDER ch.5 contains transferable knowledge on PZT + vacuum bench setup.

## Cross-references

### Canonical AVE physics
- [INVARIANT-C2 ξ_topo electromechanical transduction constant](../manuscript/ave-kb/CLAUDE.md) — canonical definition
- [Translation-Tables: Circuit Analysis (Topo-Kinematic Identity)](../manuscript/ave-kb/common/translation-tables/translation-circuit.md) — [Q]≡[L] full translation
- [Universal Saturation-Kernel Catalog A-034](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) — Cleave operates at sub-V_yield Regime I
- [Four Universal Regimes — Regime I](../manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/four-regimes.md) — Cleave is small-signal linear regime
- [Power-Domain Classification](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md) — reactive-only electrometer cycling
- [Temporal Saturation Regime Classifier](../manuscript/ave-kb/common/temporal-saturation-regime-classifier.md) — Cleave is in **lossless temporal regime** ($\delta_{AVE} \to 0$); pure-reactive electrometer

### Matrix + downstream cascade
- [Matrix row C15-CLEAVE-01](../manuscript/ave-kb/common/divergence-test-substrate-map.md)
- **Cascade dependents** (all fall if C15 returns Outcome C):
  - B4-PROTEIN (ξ_topo in Ramachandran enforcement)
  - C9-LEVITATION ($m_{max} = V_{yield} \cdot \xi_{topo} / g$)
  - C16-TORSION-05 (thrust uses ξ_topo)
  - B5-PONDER-01 (thrust uses ξ_topo)
  - B6-PONDER-02 (microwave probe uses ξ_topo)
  - B7-PONDER-05 (differential parallax uses ξ_topo)

### KB leaf (currently STALE)
- [`project-cleave-01.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md) (last touched 2026-04-13; Phase 1 walk-back target)

### Engine constants
- [`src/ave/core/constants.py`](../src/ave/core/constants.py) — ξ_topo canonical numerical value (verify before any KiCad design)

## Audit trail

- 2026-05-20 — Sub-epic established from Phase 2 cascade-emphasis ranking (Σ=10, cascade SIZE winner — largest single-row cascade 6+ dependents). Phase 0 scoping decision pending.
- 2026-05-20 EOD+++ — **Framework-readiness audit** landed at [`exp-c15-cleave-01-sim-audit.md`](exp-c15-cleave-01-sim-audit.md). Five axes verified empirically: ξ_topo canonical 4.149×10⁻⁷ C/m (per `src/ave/core/constants.py:205`), Ax2 [Q]≡[L] canonical statement preserved (per `ave-kb/CLAUDE.md` INVARIANT-S2 Axiom 2), 6 cascade dependents still load-bearing (B4 + C9 + C16 + B5/B6/B7), KB-leaf 41.5 mV/μm prediction reproduces arithmetically from current canonical constants (computed: 41.490 mV at 10 pF on 1 μm displacement), recent corpus drift spot-check (A-034 + Class E + temporal regime + FI-13 + C8 + Q-G47 + C1 + C11 + A1-HOPF) → all orthogonal to C15 axes. Q-G47 Sessions 19 ξ_K1/K2 vs ξ_topo identified as naming-collision (different ξ; not a drift). **Verdict 🟢 NO BLOCKING DRIFT.** Phase 0 theoretical-side ready; design-side gated on Grant scoping decision (not theoretical re-derivation).
- 2026-05-20 EOD++++ — **Phase 0 Grant adjudication ✓ A3 scaffold-only + B1 standalone sibling repo.** Scaffold brief landed at [`exp-c15-cleave-01-phase-0-scaffolding.md`](exp-c15-cleave-01-phase-0-scaffolding.md). Target sibling repo: `AVE-Bench-FemtoElectrometer` (NEW; parallels AVE-Bench-VacuumMirror precedent). Decision rationale: A3 chosen over A1 pure-pursue because VacuumMirror precedent shows value of open-questions discipline before KiCad work; B1 chosen because per-experiment-sibling-repo pattern + IP boundary alignment + PEP 420 namespace cleanliness; B3 PONDER rejected (atopile vs KiCad tooling collision + PONDER transferable-knowledge claim was at SCIENCE not BENCH level). Six open questions (Q-C15-01 to Q-C15-06) drafted in brief: chamber priority, pre-reg precision target, discriminator dielectric choice, parasitic-C control, PZT outgassing, triboelectric confound discrimination. Implementor dispatch follows orchestration commit.
- 2026-05-20 EOD+++++ — **PHASE 0 SCAFFOLD ✓ LANDED.** `ave-implementer` returned with single clean commit `0b05bd4` on `main` at `/Users/grantlindblom/AVE-staging/AVE-Bench-FemtoElectrometer/`. 36 files (29 substantive + 7 .gitkeep), 2686 lines added. All 8 success criteria from brief met: repo exists + structure-parity with VacuumMirror + KB-leaf prediction preserved verbatim (41.5 mV/μm + 0.415 pC + outcome A/B/C/D + "if 0.0 mV the framework is falsified") + 6 open questions captured (Q-C15-01 to Q-C15-06) + cross-references back to AVE-Core valid + no KiCad/no measurement scripts (hardware/cad + scripts/ are placeholders) + pure-AVE-corpus grep returns zero + framework-readiness audit cross-ref captured in docs/design/2026-05-20_initial_scoping.md. `substrate-native-check` PASSED on electrometer model (ξ_topo bridges K4 lattice geometry to bench charge via Ax2 [Q]≡[L]; substrate-native, not QED-borrowed); no Q-C15-07 surfaced. No remote configured per brief constraint #6 — Grant handles `gh repo create ave-veritas-et-enodatio/AVE-Bench-FemtoElectrometer --private` + `git remote add origin` + `git push -u origin main`. Phase 0 deliverable list passed verification audit (commit hash + file count + grep checks confirmed). Phase 0→1 promotion blocked on (i) GitHub remote setup [trivial, Grant authorization needed] + (ii) Q-C15-01 chamber priority resolution [Phase 1 KiCad entry gate].
- 2026-05-20 EOD+++++ — **Cross-precedent flag (FLAG-DON'T-FIX)**: brief §"Post-scaffold orchestration walk-back" claimed `vacuum-impedance-mirror.md` cross-refs to AVE-Bench-VacuumMirror sibling — empirical check found this is NOT the case (grep returned 0 matches for "vacuummirror|vacuum-mirror|sibling repo|AVE-Bench" in that KB leaf). The actual precedent is **one-way from sibling repo → AVE-Core**, not bidirectional. C15 KB-leaf refresh proceeds independently of the precedent claim because the KB leaf has a STALE "Engineering substrate status" section that explicitly says "no KiCad / no hardware in any AVE repo yet" (now false — scaffold sibling repo exists). Refresh is justified on stale-section grounds, not bidirectional-cross-ref grounds.
- 2026-05-20 EOD+++++ — **Q-C15-01 chamber priority scoping doc landed** at [`exp-c15-cleave-01-q-c15-01-chamber-scoping.md`](exp-c15-cleave-01-q-c15-01-chamber-scoping.md). Four-experiment chamber-profile comparison surveyed via verify-before-cite v1.4 grep on bench-engineering TEST_PROCEDUREs + KB leaves + PONDER ch.5 manuscript: C15 (≤10⁻⁶ Torr, NONE HV, NONE optical, fixed-mount PCBA + PZT) vs AVE-Bench-VacuumMirror (≤10⁻⁹ UHV, 35-43 kV DC, YES optical + 10" CF chamber) vs C16-TORSION-05 (10⁻⁶ Torr, ±75 kV inductive spike, Cavendish torsion balance + suspension) vs B5-PONDER-01 (10⁻⁵ Torr, multi-axis HV + AC modulation, quartz piezo / torsion balance). Three candidate paths evaluated: C1 dedicated chamber RECOMMENDED, C2 share-with-VacuumMirror REJECTED (pressure-tier overkill + HV-noise floor risk + optical-port contention), C3 share-with-PONDER/TORSION REJECTED (EXTREME ±75 kV noise + suspended-vs-fixed-mount incompatibility + future-tense schedule risk).
- 2026-05-20 EOD+++++ — **Q-C15-01 ✓ RESOLVED — Grant adjudicated DEDICATED CHAMBER** (path C1). Walk-back propagated to AVE-Bench-FemtoElectrometer at commit `9a768bd` (local-only): `docs/open_questions.md` Q-C15-01 OPEN → CLOSED with rejected-paths rationale + implementation notes; Q-C15-05 (PZT outgassing UHV) scope-narrowing note added (10⁻⁶ Torr is NOT UHV → commodity PI N-216-grade PZT likely sufficient; UHV-specialty path deferred); `docs/procurement_action_items.md` §A header walked back from "Q-C15-01 decision pending" to "Q-C15-01 ✓ RESOLVED dedicated path active"; A.1 decision-gate Q-C15-01 checked off; A.2-A.4 sourcing actions activated. **Cost reconciliation flag**: scoping doc estimated "$500-2k" chamber-alone (bell-jar tier); procurement doc full subsystem-A (chamber refurb ≤$1.5k + pumping ≤$3k + feedthroughs ≤$500) is ~$4-5k mid-range; both numbers correct at their respective scopes. Phase 0→1 promotion blocker (ii) flipped OPEN → CLOSED; remaining blockers: (i) Grant GitHub remote authorization + (iii) Grant Phase 0→1 promotion adjudication.
- 2026-05-20 EOD++++++ — **(i) GitHub remote ✓ LIVE + (iii) Phase 0→1 ✓ PROMOTED.** Grant authorized both remaining blockers. (i) `gh repo create ave-veritas-et-enodatio/AVE-Bench-FemtoElectrometer --private --source=. --remote=origin --push` executed cleanly; repo live at `https://github.com/ave-veritas-et-enodatio/AVE-Bench-FemtoElectrometer` (private); branch `main` tracks `origin/main`; both commits `0b05bd4` scaffold + `9a768bd` Q-C15-01 walk-back pushed. (iii) Phase 1 KiCad design brief landed at [`exp-c15-cleave-01-phase-1-kicad-brief.md`](exp-c15-cleave-01-phase-1-kicad-brief.md) — full Phase 1 scope (D1.1-D1.10) decomposed into Phase 1a (sub-agent-doable: ADA4530-1 reference notes + finalized BOM + KiCad schematic DRAFT + TEST_PROCEDURE update + procurement SKU population + ORDERING + DESIGN_LOG skeletons), Phase 1b (PCB layout — Grant manual or specialized session), Phase 1c (Gerbers + DRC — Grant manual via kicad-cli). Phase 1a implementor dispatched in background; branch `analysis/phase-1a-kicad-design` off `main`; implementor instructions include 11 constraints (pure-AVE-corpus, canonical-source compliance, KB-leaf prediction verbatim preservation, Q-C15-01/04/05 resolution honoring, etc.) + 10 success criteria + cross-reference list to AVE-Core canonical content + sibling-repo state + orchestration docs.

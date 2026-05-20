> **ARCHIVED 2026-05-20 EOD+++++++++++++** — content preserved per ave-walk-back discipline. Canonical reference: [`exp-c15-cleave-01.md`](../exp-c15-cleave-01.md) consolidated sub-epic. This brief was the active doc during phase execution; phase is now closed/superseded per the consolidated doc's phase table (Phase 0 ✓ COMPLETE 2026-05-20 EOD+++++).

# EXP-C15-CLEAVE-01 — Phase 0 Scaffolding Brief (AVE-Bench-FemtoElectrometer sibling-repo establishment)

**Parent sub-epic**: [`exp-c15-cleave-01.md`](../exp-c15-cleave-01.md)
**Parent epic**: [`../../experimental-arc.md`](../../experimental-arc.md)
**Phase**: 0 — Scoping + standalone sibling-repo scaffold (no KiCad cycle yet)
**Grant adjudication**: 2026-05-20 EOD++++ — **A3 scaffold-only + B1 standalone sibling repo**
**Target sibling repo**: `AVE-Bench-FemtoElectrometer` (new)
**Precedent template**: [`AVE-Bench-VacuumMirror`](/Users/grantlindblom/AVE-staging/AVE-Bench-VacuumMirror/) — only existing `AVE-Bench-*` sibling; bench-class scaffold-stage template

## Phase 0 scope statement

This phase establishes the **canonical home** for C15-CLEAVE-01 bench-class engineering work BEFORE any KiCad cycle commits. It scaffolds the sibling-repo structural pattern per AVE-Bench-VacuumMirror precedent, captures the canonical KB-leaf prediction as a standalone manuscript sub-volume, surfaces open questions, and creates the structural scaffold the next phase (KiCad design + ADA4530-1 eval board + chamber interface) can build on.

**EXPLICITLY OUT OF SCOPE in Phase 0**:
- KiCad schematic + layout design — Phase 1 work; gated on Grant Phase 0→1 promotion adjudication
- Hardware fab / BOM ordering — Phase 2
- PZT actuator + DAC + vacuum chamber procurement — Phase 2
- Bench measurement — Phase 3
- Outcome paper — Phase 4
- ave-prereg-format pre-registration — Phase 3 gate

The job here is **scaffold + scoping discipline**, not engineering.

## Why A3 + B1 (Grant's adjudication context)

**A3 scaffold-only chosen over A1 pure-pursue because**:
- VacuumMirror precedent (also scaffold-stage; unbuilt bench) demonstrates the value of surfacing open questions BEFORE KiCad work starts — avoids false-start ($1-5k) sunk-cost on design that gets re-spun after design-discipline questions surface
- Low-cost (~1 implementor session) preserves optionality on chamber decision + dielectric-discriminator decision + pre-reg precision target
- Bottleneck is Grant scoping priority adjudication, NOT theoretical drift (per just-landed framework-readiness sim audit)

**B1 standalone sibling repo chosen over B2 AVE-Core/hardware/cleave_01/ because**:
- Matches AVE-Bench-VacuumMirror precedent (the only existing `AVE-Bench-*` sibling)
- Aligns with per-experiment-sibling-repo pattern (AVE-HOPF, AVE-PONDER, AVE-Fusion, AVE-Protein, AVE-Propulsion)
- IP boundary aligns with existing sibling-repo + PATENTS.md convention
- PEP 420 namespace extension keeps AVE-Core import-clean
- Bench-class hardware artifacts don't bloat AVE-Core engine/manuscript scope

**B3 in AVE-PONDER hardware/** rejected because:
- PONDER hardware is atopile-based (.ato + Makefile + ato.yaml); single design (`metric_decoherence.ato`); would create infrastructure tooling collision with KiCad
- "PONDER ch.5 transferable knowledge" claim in sub-epic doc (2026-05-20 establishment) is overstated at the BENCH level — PONDER has no PZT, no ADA4530, no vacuum chamber; transferable knowledge is at SCIENCE level (V_yield + ξ_topo at boundary) only

## Deliverables (scaffold-stage)

| Deliverable | Source / template | Notes |
|---|---|---|
| **Repo structure init** | AVE-Bench-VacuumMirror layout | `git init`; remote at `https://github.com/ave-veritas-et-enodatio/AVE-Bench-FemtoElectrometer` (Grant creates on GitHub OR implementor uses `gh repo create` if Grant pre-authorizes); private by default per AVE pattern |
| **README.md** | VacuumMirror README | Adapt boilerplate: status + depends-on-AVE-Core + falsifies-Axiom-2 (NOT Axiom 4); one-line prediction `Q = ξ_topo · x = (4.149×10⁻⁷ C/m) · x ⇒ 41.5 mV/μm on 10 pF input`; contents listing per VacuumMirror; installation + relationship-to-AVE-Core sections |
| **LICENSE** | Copy VacuumMirror LICENSE | Same license terms |
| **PATENTS.md** | VacuumMirror PATENTS.md | Adapt to C15 IP framing (PCBA design + chamber interface as bench-class engineering IP; framework IP stays in AVE-Core) |
| **AGENTS.md** + **CLAUDE.md** | VacuumMirror precedent | Sibling-repo agent orientation: first-read order, scope vs AVE-Core, IP-divide discipline reference, pure-AVE-corpus rule |
| **.agents/HANDOFF.md** | VacuumMirror precedent | Initial handoff capturing scaffold state + next-phase entry point (Phase 1 KiCad design gated on Grant adjudication) |
| **.agents/workflows/** + **.agents/infrastructure_blueprint.md** | VacuumMirror precedent | Same patterns |
| **manuscript/vol_cleave_01/** sub-volume | KB leaf `project-cleave-01.md` + INVARIANT-C2 + Translation-Circuit table + regime classification | Standalone derivation chapter: 01_axiom_2_topo_kinematic_isomorphism.tex (Ax2 statement) → 02_xi_topo_derivation.tex (canonical ξ_topo = e/ℓ_node) → 03_bench_geometry.tex (PCBA layout) → 04_falsification_metric.tex (41.5 mV/μm prediction + outcome A/B/C/D) → 05_open_questions.tex |
| **hardware/TEST_PROCEDURE.md** | KB leaf §"The PCBA Implementation" + §"The Falsification Metric" | Step-by-step measurement protocol: PZT step + voltage readout + dielectric-independence discriminator test; capture noise-floor + parasitic-rejection requirements |
| **hardware/BOM.md** | KB leaf §"KB-specified BOM" | ADA4530-1 + 10 pF precision cap + PZT actuator (1 μm step) + DAC for PZT drive + vacuum chamber + Teflon standoffs + guard ring enclosure |
| **hardware/cad/** directory | Empty placeholder | Future home for KiCad schematic + layout + Gerbers |
| **hardware/diagrams/** | Empty placeholder | Future home for bench geometry diagrams |
| **docs/open_questions.md** | 4 open questions from sub-epic + new ones surfaced by scaffolding | OPEN/DEFERRED/CLOSED tracking per VacuumMirror precedent |
| **docs/glossary.md** | VacuumMirror precedent | C15 + ξ_topo terminology |
| **docs/design/2026-05-20_initial_scoping.md** | This brief + sub-epic Phase 0 framing | Initial scoping rationale + repo establishment context |
| **docs/procurement_action_items.md** | KB leaf BOM | Phase 2 entry-point doc (deferred but tracked) |
| **docs/runs/** + **docs/analysis/** | Empty placeholders | Future homes for measurement runs + analysis |
| **scripts/** + **data/** | Placeholder + .gitkeep | Phase 1+ entry points |
| **pyproject.toml** + **setup.sh** + **Makefile** + **uv.lock** | VacuumMirror precedent | PEP 420 namespace extension; combined-env setup |
| **tests/** | VacuumMirror precedent | Initial test scaffold (will populate in Phase 1) |

## Open questions to surface in `docs/open_questions.md`

Carry-forward from sub-epic doc + new questions surfaced during scaffolding:

| # | Question | Status | Resolution path |
|---|---|---|---|
| **Q-C15-01** | Vacuum chamber priority — dedicated vs shared with AVE-Bench-VacuumMirror vs shared with future B5/B6/B7 PONDER + C16 TORSION-05? | OPEN | Phase 1 entry decision; depends on chamber size requirements (PCBA + PZT + DAC + cabling vs optical bench) |
| **Q-C15-02** | Pre-reg precision target — at what slope-precision (per ADA4530-1 noise floor) is Outcome A vs B vs C confidently distinguished? | OPEN | Phase 3 gate; requires ADA4530-1 noise-floor measurement + parasitic-rejection characterization |
| **Q-C15-03** | Discriminator dielectric test — which dielectric to swap for the dielectric-independence test? PTFE vs polyimide vs PCB FR-4 vs vacuum-gap-only? | OPEN | Phase 3 design; vacuum-gap-only is cleanest discriminator (no dielectric → standard EE predicts $Q \to 0$; AVE predicts $Q = \xi_{topo} \cdot x$ unchanged) |
| **Q-C15-04** | Parasitic input capacitance control — KB leaf assumes exactly 10 pF; how to characterize + verify the actual $C_{in}$ on the assembled PCBA within tolerance for 41.5 mV/μm slope claim? | OPEN | Phase 1 design discipline; LCR meter calibration + guard-ring effective $C$ measurement |
| **Q-C15-05** | Outgassing of PZT actuator under vacuum — commercial PZT actuators often have epoxy / glass-frit components that outgas; will this contaminate vacuum + drift parasitic conductance? | OPEN | Phase 2 procurement gate; UHV-compatible PZT actuator search (e.g., PI N-216 vs commodity options) |
| **Q-C15-06** | Triboelectric confound on PZT plate motion — sliding PZT could generate spurious tribo charges that look like AVE prediction; how to discriminate? | OPEN | Phase 3 design; static-only step + relaxation-time monitoring + Outcome D adjudication discipline |

## Cross-references the implementor must capture

All cross-references back to AVE-Core canonical content (per AVE-Bench-VacuumMirror precedent of pointing to canonical AVE-Core entries):

### Canonical AVE physics (link, never copy)

- **INVARIANT-C2 ξ_topo electromechanical transduction constant** → [`AVE-Core/manuscript/ave-kb/CLAUDE.md`](../manuscript/ave-kb/CLAUDE.md)
- **Canonical ξ_topo derivation** → [`AVE-Core/manuscript/ave-kb/vol5/molecular-foundations/organic-circuitry/electromechanical-transduction-constant.md`](../manuscript/ave-kb/vol5/molecular-foundations/organic-circuitry/electromechanical-transduction-constant.md)
- **Ax2 [Q]≡[L] canonical statement** → [`AVE-Core/manuscript/ave-kb/CLAUDE.md`](../manuscript/ave-kb/CLAUDE.md) INVARIANT-S2 Axiom 2
- **KB leaf project-cleave-01.md** → [`AVE-Core/manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md) — primary AVE-Core entry; this sibling repo is its bench-engineering counterpart
- **Translation-Tables: Circuit Analysis (Topo-Kinematic Identity)** → [`AVE-Core/manuscript/ave-kb/common/translation-tables/translation-circuit.md`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md)
- **Temporal Saturation Regime Classifier** (C15 in lossless temporal regime) → [`AVE-Core/manuscript/ave-kb/common/temporal-saturation-regime-classifier.md`](../manuscript/ave-kb/common/temporal-saturation-regime-classifier.md)
- **Power-Domain θ classification** (C15 reactive cycling) → [`AVE-Core/manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/orbital-friction-paradox.md)
- **Four Universal Regimes — Regime I** (sub-yield linear) → [`AVE-Core/manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/four-regimes.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch7-regime-map/four-regimes.md)

### Orchestration

- **Sub-epic** → [`AVE-Core/_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md`](../exp-c15-cleave-01.md)
- **Framework-readiness audit** → [`AVE-Core/_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01-sim-audit.md`](../exp-c15-cleave-01-sim-audit.md)
- **Parent epic** → [`AVE-Core/_orchestration/experimental/experimental-arc.md`](../../experimental-arc.md)
- **Promotion workflow** (for any engine code that later promotes back to AVE-Core) → [`AVE-Core/_orchestration/experimental/promotion-workflow-template.md`](../../promotion-workflow-template.md)

### Cascade dependents (6 downstream rows)

All depend on ξ_topo + Ax2:
- B4-PROTEIN — AVE-Protein sibling repo (Ramachandran enforcement uses ξ_topo)
- C9-LEVITATION — AVE-Propulsion sibling repo? (TBD; $m_{max} = V_{yield} \cdot \xi_{topo} / g$)
- C16-TORSION-05 — AVE-Propulsion sibling repo? (asymmetric sawtooth DC thrust)
- B5-PONDER-01 — AVE-PONDER sibling repo (thrust at V_yield boundary)
- B6-PONDER-02 — AVE-PONDER sibling repo (microwave bistatic probe)
- B7-PONDER-05 — AVE-PONDER sibling repo (differential saturation parallax)

### Engine constants

- $\xi_{topo}$ canonical numerical value → [`AVE-Core/src/ave/core/constants.py`](../src/ave/core/constants.py) line 205 — `XI_TOPO = e_charge / L_NODE  # ≈ 4.149e-7 C/m`

## Skill discipline (Phase 0 scaffold)

- **ave-canonical-source** — any reference to ξ_topo numerical value MUST cite `src/ave/core/constants.py:205`; never hard-code 4.149e-7 in this sibling repo
- **ave-canonical-leaf-pull v1.2 trigger 8** — this is NEW bench-engineering work touching Ax2; canonical leaves enumerated above must all be linked (NOT copied) per AVE-Bench-VacuumMirror precedent
- **verify-before-cite v1.4** — all cross-references to KB leaves verified via Read at file:line
- **substrate-native-check** — the electrometer model in manuscript/vol_cleave_01/ MUST be K4-substrate-native (not just QM-borrowing); ξ_topo = e/ℓ_node is the substrate-native bridge
- **ave-discrimination-check Step 1.5** — outcome A/B/C/D already enumerated in KB leaf; preserve verbatim
- **ave-evidence-framing-discipline** — README + manuscript must not overstate ("FAB-READY" not allowed; "SCAFFOLD STAGE. BENCH UNBUILT." is the truthful framing per VacuumMirror's precedent statement)
- **ave-ip-divide-discipline** — bench-class engineering IP lives here; framework IP stays in AVE-Core; PATENTS.md adapts VacuumMirror precedent
- **Pure-AVE-corpus rule** — NO investor / fund / interview / 1517 / external-pitch refs anywhere in tracked files (README, manuscript, hardware, docs, scripts, commits, branch names)

## Constraints (orchestrator → implementor)

1. **No KiCad work** — this is scaffold-only. Hardware/cad/ + hardware/diagrams/ are placeholders only.
2. **No measurement-script work** — scripts/ is a placeholder only.
3. **No engine code** — engine constants stay in AVE-Core; this repo imports from AVE-Core via PEP 420 namespace extension when needed (Phase 1+ work).
4. **Preserve KB-leaf prediction verbatim** — 41.5 mV/μm on 10 pF input + 0.415 pC per μm + outcome A/B/C/D wording must match `project-cleave-01.md` verbatim. Any rephrasing risks framework-readiness audit drift.
5. **Pure-AVE-corpus rule** — apply everywhere including in commit messages.
6. **First commit is initial scaffold** — multiple sub-commits OK but the final state is the scaffold-stage tip; don't push partial scaffold.
7. **Remote setup** — Grant has option to create the GitHub repo (private) BEFORE implementor pushes OR implementor uses `gh repo create ave-veritas-et-enodatio/AVE-Bench-FemtoElectrometer --private` if Grant pre-authorizes. Confirm with Grant before push if unclear.
8. **Worktree leak prevention** — implementor spawned in isolated worktree per AVE-Core CLAUDE.md "Spawning implementors via the Agent tool — discipline". This is a NEW REPO not on a branch of AVE-Core, so worktree applies only if any AVE-Core changes are made (e.g., cross-ref additions).

## Success criteria

| Axis | Criterion |
|---|---|
| **Repo exists** | `AVE-Bench-FemtoElectrometer` is a git repo with initial commit; pushed to GitHub remote `ave-veritas-et-enodatio/AVE-Bench-FemtoElectrometer` (or staged for Grant push if remote not yet created) |
| **Structure parity** | Top-level structure matches AVE-Bench-VacuumMirror within reason: README + LICENSE + PATENTS + AGENTS + manuscript + hardware + docs + scripts + data + tests + setup.sh + pyproject.toml + Makefile + .agents/ + CLAUDE.md |
| **KB-leaf prediction preserved** | 41.5 mV/μm + 0.415 pC + outcome A/B/C/D wording matches `project-cleave-01.md` verbatim |
| **Open questions captured** | docs/open_questions.md has 6 questions (Q-C15-01 to Q-C15-06) with OPEN status + resolution paths |
| **Cross-references valid** | All cross-references back to AVE-Core resolve (via relative paths or absolute URLs as appropriate per VacuumMirror precedent) |
| **No KiCad / no measurement scripts** | hardware/cad/ + scripts/ are placeholders (.gitkeep) |
| **Pure-AVE-corpus** | grep audit: no investor/fund/interview/1517/pitch refs anywhere |
| **Framework-readiness audit cross-ref** | docs/design/2026-05-20_initial_scoping.md references the just-landed AVE-Core framework-readiness audit |

## Post-scaffold orchestration walk-back (orchestrator handles)

After implementor returns, orchestrator updates AVE-Core:
- `_orchestration/exp-c15-cleave-01.md` sub-epic — Phase 0 status update + cross-ref to new sibling repo + Phase 1 entry-point
- `_orchestration/experimental-arc.md` C15 row — sibling-repo cross-ref added
- `_orchestration/index.md` C15 row + Last-updated header — sibling-repo + scaffold-landed status
- `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md` — engineering-status section updated with cross-ref to new sibling repo (just like vacuum-impedance-mirror.md does for AVE-Bench-VacuumMirror)

## Audit trail

- 2026-05-20 EOD++++ — Phase 0 scaffolding brief established. Grant adjudication captured (A3 scaffold-only + B1 standalone sibling repo). Implementor dispatch follows after brief commit lands.

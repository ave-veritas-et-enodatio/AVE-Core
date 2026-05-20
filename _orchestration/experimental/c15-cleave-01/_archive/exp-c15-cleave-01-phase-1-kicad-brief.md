> **ARCHIVED 2026-05-20 EOD+++++++++++++** — content preserved per ave-walk-back discipline. Canonical reference: [`exp-c15-cleave-01.md`](../exp-c15-cleave-01.md) consolidated sub-epic. This brief was the active doc during Phase 1 KiCad execution; predecessor merged at `331a778` then walked back to atopile via Q-C15-10 (2026-05-20 EOD++++++++++).

# EXP-C15-CLEAVE-01 — Phase 1 KiCad Design Brief (Phase 0→1 promotion)

**Parent sub-epic**: [`exp-c15-cleave-01.md`](../exp-c15-cleave-01.md)
**Parent epic**: [`../../experimental-arc.md`](../../experimental-arc.md)
**Sibling repo**: [`AVE-Bench-FemtoElectrometer`](https://github.com/ave-veritas-et-enodatio/AVE-Bench-FemtoElectrometer) — local at `/Users/grantlindblom/AVE-staging/AVE-Bench-FemtoElectrometer/`; remote at GitHub (private), tracking `main`
**Phase**: 1 — KiCad design from KB spec (translate PCBA spec + Q-C15-01 chamber resolution into fab-ready hardware design)
**Grant promotion adjudication**: 2026-05-20 EOD++++++ — Phase 0→1 PROMOTED (per Q-C15-01 ✓ RESOLVED dedicated chamber path)

## Phase 1 promotion context

Phase 0 closed cleanly:
- ✓ Scaffold sibling repo established at commit `0b05bd4`
- ✓ Q-C15-01 chamber priority resolved (dedicated chamber, bell-jar/4''-6'' CF refurb, ≤10⁻⁶ Torr, no HV feedthroughs)
- ✓ Q-C15-05 PZT outgassing scope narrowed (commodity PI N-216-grade PZT likely sufficient)
- ✓ GitHub remote configured + push complete
- ✓ Framework-readiness audit NO DRIFT on ξ_topo + Ax2 + cascade dependents

Phase 1 is the design-cycle phase. The full Phase 1 deliverable is a **fab-ready hardware package** parallel to the AVE-HOPF `hopf_02a/` pattern (Gerbers + BOM + ORDERING + DESIGN_LOG). Estimated cycle 1-2 weeks per hardware engineer-equivalent.

## Phase 1 scope (full deliverable set)

| Deliverable | Type | Difficulty | Owner |
|---|---|---|---|
| **D1.1** ADA4530-1 reference-design notes consolidated | Markdown doc | Easy (data consolidation) | Implementor session |
| **D1.2** Finalized BOM with concrete SKUs (Mouser/Digi-Key/etc.) | Markdown table update | Easy (search + pin SKUs) | Implementor session |
| **D1.3** KiCad schematic capture (`.kicad_sch` S-expression text) | KiCad text-format file | Medium (domain expertise needed) | Implementor session OR Grant manual |
| **D1.4** PCB layout (`.kicad_pcb` S-expression text) — guard-ring topology + Teflon-standoff annotations + chamber-mount geometry | KiCad text-format file | Hard (manual placement + routing) | Grant manual OR specialized session |
| **D1.5** Schematic ERC + PCB DRC clean | KiCad CLI run | Tooling-dependent | Grant manual (KiCad GUI/CLI access) |
| **D1.6** Gerbers export | KiCad CLI run | Tooling-dependent | Grant manual (`kicad-cli pcb export gerbers`) |
| **D1.7** TEST_PROCEDURE.md updated to reflect actual hardware | Markdown update | Easy | Implementor session |
| **D1.8** procurement_action_items.md updated with concrete SKUs | Markdown update | Easy | Implementor session |
| **D1.9** ORDERING.md (JLCPCB-equivalent ordering guide) | Markdown new doc | Easy | Implementor session |
| **D1.10** DESIGN_LOG.md (per AVE-HOPF precedent) | Markdown new doc | Easy | Implementor session |

## Phase 1a — first implementor dispatch (this brief's scope)

**Scope**: D1.1 + D1.2 + D1.3-draft + D1.7 + D1.8 + D1.9 + D1.10

Specifically:
- Consolidate ADA4530-1 reference-design notes from Analog Devices datasheet + EVAL-ADA4530-1RZ user guide into `hardware/cad/reference_design.md`
- Finalize BOM with concrete Mouser/Digi-Key/etc. SKUs in `hardware/BOM.md` (replace TBD entries)
- Draft KiCad schematic in `hardware/cad/cleave_01_schematic.kicad_sch` (S-expression text format) — best-effort first pass; ERC clean not required (Grant cleans in Phase 1b)
- Update `hardware/TEST_PROCEDURE.md` to reflect finalized hardware (DAC SKU, ADA4530-1 pinout, 10 pF cap SKU + tolerance, etc.)
- Update `docs/procurement_action_items.md` with concrete SKUs (replace TBD entries; A.2-A.4 chamber sourcing + B.3 DAC + C.1 ADA4530-1 + C.2 10 pF cap + etc.)
- New `hardware/ORDERING.md` (skeleton; populated when D1.4-D1.6 land)
- New `hardware/DESIGN_LOG.md` (skeleton tracking design decisions + KB-leaf-spec → KiCad translation rationale)

**OUT OF SCOPE for Phase 1a**: PCB layout (D1.4), DRC (D1.5), Gerbers (D1.6) — these need KiCad GUI/CLI tooling that sub-agents don't have reliable access to. Grant pulls these manually in Phase 1b after reviewing the schematic + BOM.

## Phase 1a constraints

1. **Pure-AVE-corpus rule**: no investor/fund/interview/1517/pitch refs anywhere
2. **Canonical-source discipline**: ξ_topo numerical value MUST cite `AVE-Core/src/ave/core/constants.py:205`; never hard-code `4.149e-7`
3. **No engine code modification**: implementor reads from AVE-Core but does not modify it; AVE-Core orchestration walk-back done by orchestrator post-return
4. **Preserve KB-leaf prediction verbatim**: 41.5 mV/μm + 0.415 pC + outcome A/B/C/D + falsification clause must continue to match `project-cleave-01.md` verbatim in any TEST_PROCEDURE updates
5. **Q-C15-01 resolution honored**: PCBA-mount geometry = rigid fixed-mount (NOT suspended-payload); cabling-feedthrough layout = standard low-cost (NOT HV); chamber spec ≤10⁻⁶ Torr (NOT UHV)
6. **Q-C15-04 + Q-C15-05 resolutions honored**: 10 pF NP0/C0G ±1% target for C_in; commodity PI N-216-grade PZT preferred (UHV-specialty PZT deferred)
7. **Q-C15-03 default preserved**: discriminator test = vacuum-gap-only as Phase 3 default (per implementor open_questions.md note); test procedure can include PTFE/polyimide as secondary configurations
8. **Pre-commit branch check** (per AVE-Bench-FemtoElectrometer CLAUDE.md): verify `git branch --show-current` before each commit
9. **No remote push without confirmation**: implementor can push to branch on origin but **must NOT merge to main** — orchestrator + Grant do merge-review
10. **Branch naming convention**: implementor branches from `main`; branch name `analysis/phase-1a-kicad-design` (per AVE-HOPF + AVE-Core branch-naming pattern)
11. **Skill discipline**: ave-canonical-source + ave-canonical-leaf-pull v1.2 trigger 8 + verify-before-cite v1.4 + substrate-native-check + ave-evidence-framing-discipline + ave-ip-divide-discipline + pure-AVE-corpus

## Cross-references the implementor must consult

### Canonical AVE physics

- **INVARIANT-C2 ξ_topo** → `AVE-Core/manuscript/ave-kb/CLAUDE.md`
- **Canonical ξ_topo numerical value** → `AVE-Core/src/ave/core/constants.py:205` (`XI_TOPO = e_charge / L_NODE`)
- **Ax2 [Q]≡[L] canonical statement** → `AVE-Core/manuscript/ave-kb/CLAUDE.md` INVARIANT-S2 Axiom 2
- **KB leaf project-cleave-01.md** → `AVE-Core/manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-cleave-01.md` — primary content source for PCBA spec
- **Engineering substrate status** → `AVE-Core/manuscript/ave-kb/.../project-cleave-01.md` §"Engineering substrate status (2026-05-20 EOD+++++)" — current Phase 0+1 state

### Sibling-repo state

- **AVE-Bench-FemtoElectrometer hardware/TEST_PROCEDURE.md** — current bench protocol; update to reflect actual hardware SKUs
- **AVE-Bench-FemtoElectrometer hardware/BOM.md** — current TBD entries; replace with concrete SKUs
- **AVE-Bench-FemtoElectrometer docs/open_questions.md** — Q-C15-01 ✓ CLOSED (dedicated chamber); Q-C15-02 OPEN (pre-reg precision); Q-C15-03 OPEN (vacuum-gap-only default); Q-C15-04 OPEN (10 pF NP0/C0G ±1% target); Q-C15-05 OPEN (commodity PI N-216 preferred per Q-C15-01 scope-narrowing); Q-C15-06 OPEN (triboelectric discrimination via time-constant signature)
- **AVE-Bench-FemtoElectrometer docs/procurement_action_items.md** — current SKU-population state; update A.2-A.4 + B.3 + C.1-C.4 with concrete SKUs

### Orchestration

- **Sub-epic** → `AVE-Core/_orchestration/exp-c15-cleave-01.md`
- **Framework-readiness audit** → `AVE-Core/_orchestration/exp-c15-cleave-01-sim-audit.md`
- **Phase 0 scaffold brief** → `AVE-Core/_orchestration/exp-c15-cleave-01-phase-0-scaffolding.md`
- **Q-C15-01 chamber scoping** → `AVE-Core/_orchestration/exp-c15-cleave-01-q-c15-01-chamber-scoping.md`
- **Parent epic** → `AVE-Core/_orchestration/experimental-arc.md`
- **Promotion workflow template** (for any engine code reverse-promotion back to AVE-Core) → `AVE-Core/_orchestration/promotion-workflow-template.md`

### Precedent repos

- **AVE-Bench-VacuumMirror** — sibling-repo structural template; `manuscript/vol_vacuum_mirror/` for sub-volume pattern; `hardware/cad/` for KiCad cad layout pattern (if applicable)
- **AVE-HOPF** — hardware design + Gerbers + DRC.rpt + DESIGN_LOG.md + ORDERING.md precedent; specifically `hardware/Gerbers_hopf_02a/` + `hardware/hopf_02a_ORDERING.md` + `hardware/hopf_02a_BOM.md` + `hardware/DESIGN_LOG.md` patterns

## Phase 1a success criteria

| Axis | Criterion |
|---|---|
| **D1.1 reference-design notes** | `hardware/cad/reference_design.md` exists; covers ADA4530-1 pinout + EVAL-ADA4530-1RZ topology + guard-ring drive + Teflon-standoff layout; cites ADI datasheet + eval-board user guide |
| **D1.2 BOM finalized** | `hardware/BOM.md` replaces all TBD entries with concrete Mouser/Digi-Key/manufacturer SKUs; cost rollup matches procurement_action_items.md §E mid-range estimate (~$4-5k chamber subsystem + $1-2k PCBA + auxiliary) |
| **D1.3 schematic draft** | `hardware/cad/cleave_01_schematic.kicad_sch` exists in S-expression text format; best-effort first pass; ERC-clean not required (Grant cleans in Phase 1b) |
| **D1.7 TEST_PROCEDURE refresh** | `hardware/TEST_PROCEDURE.md` reflects finalized hardware SKUs; KB-leaf prediction wording preserved verbatim (no rephrasing risk) |
| **D1.8 procurement update** | `docs/procurement_action_items.md` §A-D have concrete SKUs replacing TBD entries |
| **D1.9 ORDERING skeleton** | `hardware/ORDERING.md` exists with sections: parts ordering checklist (per BOM) + PCB fab ordering (skeleton for JLCPCB/OSH Park; will populate after D1.4-D1.6 land) + assembly checklist |
| **D1.10 DESIGN_LOG** | `hardware/DESIGN_LOG.md` exists; tracks KB-leaf-spec → KiCad-translation decisions + reference-design adaptations + any open design questions surfaced |
| **Branch + commit hygiene** | Implementor branched `main` → `analysis/phase-1a-kicad-design`; commits on branch; **pushed to origin but NOT merged to main**; orchestrator + Grant review pre-merge |
| **Pure-AVE-corpus** | grep audit returns zero matches for investor/fund/interview/1517/pitch anywhere in new files |
| **Canonical-source compliance** | ξ_topo numerical value referenced via citation to `AVE-Core/src/ave/core/constants.py:205`, NOT hard-coded |

## What this Phase 1a unblocks

If Phase 1a delivers cleanly:
- **D1.4 PCB layout** can start with the schematic as input (Grant manual KiCad work OR future implementor session with dedicated KiCad tooling)
- **D1.5 ERC + D1.6 Gerbers** require Grant KiCad GUI/CLI access (sub-agent tooling limitation)
- **Phase 1 review** with orchestrator + Grant for schematic correctness + BOM completeness + SKU verification
- **Phase 1 merge** to `main` after Grant sign-off

If Phase 1a surfaces critical-path issues (e.g., ADA4530-1 alternative needed, BOM sourcing gap, schematic constraint that requires KB-leaf walk-back), surface them as new open questions (Q-C15-07+) in `docs/open_questions.md` rather than fixing inline (per flag-don't-fix discipline).

## Adjacent Phase 1b/1c roadmap (NOT this brief's scope)

| Phase | Deliverables | Owner |
|---|---|---|
| **1b** PCB layout | D1.4 (KiCad layout) + D1.5 (DRC) | Grant manual OR specialized implementor session with KiCad tooling |
| **1c** Gerbers + ordering | D1.6 Gerbers ZIP + D1.9 ORDERING populated + DESIGN_LOG.md final | Grant manual (`kicad-cli pcb export gerbers`) |
| **2** Fab + assembly | JLCPCB submission + parts ordering + assembly + vacuum chamber procurement + bench install | Grant + procurement lead |
| **3** Measurement | ave-prereg-format pre-registration (Q-C15-02 closure) + PZT step sweep + slope measurement + dielectric-independence test | Bench operator (Grant or designate) |
| **4** Outcome adjudication | Outcome A/B/C/D adjudication per KB leaf §"Outcome adjudication" + paper template + cascade walk-back if Outcome C | Grant + orchestrator |

## Implementor dispatch (Phase 1a)

Brief is self-contained for the Phase 1a implementor session. After this orchestration commit lands, the next action is `Agent({subagent_type: "ave-implementer", run_in_background: true, prompt: <Phase 1a brief consumption + deliverables D1.1-D1.10 minus D1.4-D1.6>})`. Implementor will return with branch + commits ready for orchestrator review.

## Post-Phase-1a walk-back checklist (orchestrator handles after implementor return)

- `_orchestration/exp-c15-cleave-01.md` — Phase 1a status update + cross-ref to new branch + Phase 1b entry-point (if any)
- `_orchestration/experimental-arc.md` C15 row — Phase 1a status + branch ref
- `_orchestration/index.md` C15 row + Last-updated bump
- Optionally: `manuscript/ave-kb/vol4/falsification/.../project-cleave-01.md` Engineering substrate status — refresh from "scaffold landed" to "scaffold + Phase 1a design draft landed; Phase 1b PCB layout pending Grant" (only if Grant approves the schematic; flag-don't-fix until then)

## Audit trail

- 2026-05-20 EOD++++++ — Phase 0→1 promotion brief established. Grant adjudication captured (Phase 0→1 PROMOTED per Q-C15-01 ✓ RESOLVED). Implementor dispatch follows after brief commit lands.

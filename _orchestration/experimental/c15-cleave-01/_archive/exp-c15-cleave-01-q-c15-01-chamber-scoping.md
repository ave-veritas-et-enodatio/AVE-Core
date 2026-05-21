> **ARCHIVED 2026-05-20 EOD+++++++++++++** — content preserved per ave-walk-back discipline. Canonical reference: [`exp-c15-cleave-01.md`](../exp-c15-cleave-01.md) consolidated sub-epic. This brief was the active doc during phase execution; phase is now closed/superseded per the consolidated doc's phase table (Q-C15-01 ✓ CLOSED — dedicated chamber, Grant adjudicated C1, 2026-05-20 EOD+++++).

# Q-C15-01 — Vacuum Chamber Priority Scoping (C15-CLEAVE-01 Phase 0→1 entry gate)

**Parent sub-epic**: [`exp-c15-cleave-01.md`](../exp-c15-cleave-01.md)
**Phase 0 scaffold**: [`exp-c15-cleave-01-phase-0-scaffolding.md`](exp-c15-cleave-01-phase-0-scaffolding.md) — Phase 0 ✓ SCAFFOLD LANDED at commit `0b05bd4` in `AVE-Bench-FemtoElectrometer`
**Open question source**: `AVE-Bench-FemtoElectrometer/docs/open_questions.md` Q-C15-01 (and brief §"Open questions to surface" Q-C15-01)
**Decision gate**: Phase 0→1 KiCad design entry (PCBA-mount geometry + cabling-feedthrough constraints depend on chamber decision)

## Q-C15-01 verbatim (from brief)

> Vacuum chamber priority — dedicated vs shared with AVE-Bench-VacuumMirror vs shared with future B5/B6/B7 PONDER + C16 TORSION-05?

Three candidate paths from sub-epic open-questions:
- **C1**: Dedicated chamber for C15
- **C2**: Shared with `AVE-Bench-VacuumMirror`
- **C3**: Shared with future B5/B6/B7 PONDER + C16 TORSION-05

## 4-experiment chamber-profile comparison

Surveyed empirically across the 4 candidate co-tenant experiments:

| Experiment | Pressure target | HV path | Optical path | Apparatus | Substrate mechanism | Source |
|---|---|---|---|---|---|---|
| **C15-CLEAVE-01** | $\le 10^{-6}$ Torr | **NONE** (sub-yield only; only PZT drive voltage ≪ V_yield) | NONE | PCBA + PZT actuator + DAC + cabling-feedthrough | Ax2 [Q]≡[L] (linear sub-yield) | `AVE-Bench-FemtoElectrometer/hardware/TEST_PROCEDURE.md` |
| **AVE-Bench-VacuumMirror** | $\le 1 \times 10^{-9}$ Torr **UHV** | 35-43 kV DC (sub-V_yield) | **YES** — laser + APD + 3 UV-grade viewports | 10" CF chamber + 6+ ports + tungsten needle electrodes + optical bench | Ax4 saturation at V_yield boundary | `AVE-Bench-VacuumMirror/hardware/TEST_PROCEDURE.md` §"Vacuum integrity"; `docs/procurement_action_items.md` C.1 |
| **C16-TORSION-05** | $10^{-6}$ Torr | **YES** ±75 kV (above V_yield; impedance-rupture spike) | NONE | Cavendish torsion balance + suspension wire + heavy potted PCBA + SiC MOSFET drive | Ax4 rupture (above V_yield) | `manuscript/ave-kb/vol4/.../project-torsion-05.md` |
| **B5-PONDER-01** | $10^{-5}$ Torr (vacuum operation; alternative: degassed mineral oil submerged) | **YES** multi-axis HV + AC modulation | NONE | Quartz piezo OR vacuum torsion balance | Ax2+Ax4 at V_yield boundary | `AVE-PONDER/manuscript/vol_ponder/chapters/05_vacuum_torsion_metrology.tex` |

## Cross-tenancy analysis

### C2 (shared with AVE-Bench-VacuumMirror) — REJECTED

**Pressure mismatch**: C15 needs $10^{-6}$ Torr; VacuumMirror needs $10^{-9}$ Torr (3 orders tighter). C15 in a VacuumMirror chamber means co-tenant inherits expensive UHV infrastructure (10" CF, baked, NEG-pumped, $3-8k used / $8-15k new per VacuumMirror procurement docs) that C15 simply doesn't need.

**HV-feedthrough overhead**: VacuumMirror chamber has 35-43 kV HV path. C15 femto-Coulomb electrometer (ADA4530-1, 20 fA bias) is among the most HV-sensitive instruments in the matrix — sharing a chamber with 35-43 kV switching introduces parasitic-conduction + noise-floor risks that overwhelm the 41.5 mV/μm signal.

**Optical-path geometry**: VacuumMirror chamber has 3 UV-grade viewports + laser arm + APD arm. C15 has no optical path. Geometric port budget gets contested.

**Schedule contention**: VacuumMirror bench is in scaffold-stage (unbuilt). Putting C15 dependent on VacuumMirror chamber readiness compounds 2 unbuilt benches into 1 sequential dependency.

**Verdict**: REJECTED. Pressure-tier overkill + HV-noise floor risk + optical-port contention + schedule-sequence coupling.

### C3 (shared with B5/B6/B7 PONDER + C16-TORSION-05) — REJECTED

**Pressure match (only)**: B5 ($10^{-5}$ Torr) and C16 ($10^{-6}$ Torr) and C15 ($10^{-6}$ Torr) are all in the same pressure tier ✓ — but this is the only compatibility axis.

**HV-noise overwhelms**: C16 has ±75 kV inductive spike (above V_yield rupture); B5/B6/B7 have multi-axis HV + AC modulation. C15's femto-Coulomb electrometer cannot tolerate co-resident HV switching — Outcome D (parasitic confound) becomes nearly certain by design, not just risk. The KB leaf's discriminator test (dielectric-independence) requires a low-noise floor; shared HV destroys that.

**Apparatus geometry incompatible**: C16 uses Cavendish torsion balance + suspension wire; B5 uses quartz piezo OR torsion balance; B6 uses microwave bistatic probe; B7 uses differential parallax. **All are suspended-payload geometries**. C15 needs **fixed-mount PCBA + fixed-PZT stage on rigid mount** — incompatible with torsion-pendulum suspension. Cannot occupy the same chamber simultaneously without ripping out one or the other.

**Future-tense uncertainty**: B5/B6/B7 + C16 chambers are *future* — none built yet (B5-PONDER-01 confounded; B6/B7 spec-only; C16 spec-only per matrix). Coupling C15 chamber decision to an unbuilt future apparatus adds risk without payoff.

**Verdict**: REJECTED. HV-noise floor incompatibility + suspended-payload-vs-fixed-mount geometry incompatibility + future-tense schedule risk.

### C1 (dedicated chamber for C15) — RECOMMENDED

**Pressure target modest**: $10^{-6}$ Torr is achievable with bell-jar class chambers + small turbo + roughing pump. **NOT UHV** — no NEG pump, no 10" CF flange tier, no $3-8k chamber. Estimated cost: **~$500-2k commodity / used class** for a 6-10" bell jar + small turbo pump (e.g., Edwards, Pfeiffer, used surplus options).

**Apparatus simplicity**: Tabletop fixed-mount PCBA + PZT + DAC + cabling. No torsion-pendulum suspension, no HV feedthrough (PZT drive voltage is low), no optical viewports. Feedthrough requirements: low-current DAC drive + ADA4530-1 output cabling (BNC + guard ring drive) — standard low-cost feedthroughs.

**Noise floor clean**: Isolated chamber means no co-tenant HV switching to inject parasitic noise into the femto-Coulomb signal path. ADA4530-1 datasheet noise floor (20 fA bias + sub-mV/√Hz) is achievable with proper guard-ring + Teflon-standoff design (per KB leaf §"The PCBA Implementation") without external interference.

**Schedule independence**: C15 chamber procurement decoupled from VacuumMirror, PONDER, and TORSION-05 build sequences. Each bench can proceed at its own cadence.

**PZT outgassing co-design**: UHV-rated PZT (Q-C15-05) is a Phase 2 procurement gate. With a dedicated $10^{-6}$ Torr chamber, the PZT outgassing budget is generous (chamber is in bell-jar class, not UHV); commodity PI N-216-grade actuators would suffice, falling outside the "UHV-only" PZT specialty market.

**Verdict**: RECOMMENDED. Pressure-tier appropriate + apparatus geometry clean + noise floor protected + schedule independent + cost-economical.

## Cost comparison

| Option | Chamber capex | Co-tenant overhead | Schedule risk | Noise risk |
|---|---|---|---|---|
| **C1 dedicated** | ~$500-2k bell jar class | $0 | LOW (independent) | LOW (isolated) |
| **C2 share with VacuumMirror** | $0 (use existing) | $3-8k VacuumMirror chamber already in proc-pipe; C15 inherits 3-OOM-tighter pressure overhead | HIGH (sequenced after VacuumMirror build) | HIGH (35-43 kV co-resident) |
| **C3 share with PONDER/TORSION** | $0 (notional; PONDER/TORSION chambers unbuilt) | UNKNOWN (future chambers) | HIGH (waits on B5/B6/B7/C16 build sequence) | EXTREME (±75 kV C16 co-resident) |

The capex differential ($500-2k for C1 vs $0 nominal for C2/C3) is **less than the femto-Coulomb noise floor cost** that C2 or C3 would impose. C1 dominates on noise + schedule + apparatus-geometry axes; C2/C3 only "win" on chamber capex which is dwarfed by their noise/schedule downsides.

## Recommendation

**C1 dedicated chamber** for C15-CLEAVE-01.

Subsidiary specs (Phase 2 procurement entry-point):
- **Chamber class**: bell-jar or 6-10" small chamber; commodity tier
- **Pressure target**: $\le 10^{-6}$ Torr (per TEST_PROCEDURE §1)
- **Pump train**: small turbo (e.g., HiPace 80 or similar, ~80 L/s) + roughing pump
- **Feedthroughs**: low-current DAC drive (PZT) + BNC for ADA4530-1 output + guard-ring drive + ground reference + vacuum gauge
- **NOT needed**: HV feedthroughs (>1 kV), UV-grade viewports, NEG pumping, bakeable to UHV temperatures (light bakeout for PZT outgassing baseline — Q-C15-05 — sufficient)
- **Estimated capex**: $500-2k commodity / used surplus class

## What this scoping unblocks

If Grant adjudicates **C1**:
1. **Phase 1 KiCad design entry**: PCBA-mount geometry fixes to rigid fixed-mount (not suspended); cabling-feedthrough layout assumes standard low-cost feedthroughs (not HV); chamber dimensions enter design constraints
2. **Phase 2 procurement entry-point**: chamber sourcing added to `AVE-Bench-FemtoElectrometer/docs/procurement_action_items.md`
3. **Q-C15-01 status flips OPEN → CLOSED** with resolution path "dedicated chamber, bell-jar class, $\le 10^{-6}$ Torr" recorded
4. **Q-C15-05 (PZT outgassing UHV) scope narrows**: $10^{-6}$ Torr is not UHV, so commodity PZT (PI N-216 or equivalent) likely sufficient; "UHV-rated PZT" specialty search deferred
5. **No collision with VacuumMirror or PONDER chamber timelines**: each bench independent

## Adjudication options for Grant

- **C1 RECOMMENDED**: dedicated chamber path
- **C2**: still want to share with VacuumMirror despite pressure-tier + HV-noise risks (cost savings argument)
- **C3**: still want to share with PONDER/TORSION despite HV-noise + suspended-payload geometry incompatibility (logistics argument)
- **Other**: defer adjudication — what additional data would close the gap?

## Skill discipline (applied)

- `verify-before-cite v1.4`: chamber-spec citations verified via grep on `AVE-Bench-FemtoElectrometer/hardware/TEST_PROCEDURE.md` + `AVE-Bench-VacuumMirror/hardware/TEST_PROCEDURE.md` + `AVE-Bench-VacuumMirror/docs/procurement_action_items.md` + `AVE-Core/manuscript/ave-kb/vol4/.../project-torsion-05.md` + `AVE-PONDER/manuscript/vol_ponder/chapters/05_vacuum_torsion_metrology.tex`
- `ave-canonical-leaf-pull`: V_yield = 43.65 kV canonical per `ave-kb/CLAUDE.md` INVARIANT-C1 referenced in comparison matrix; chamber-pressure values pulled from primary bench-engineering docs (not derived)
- `ave-evidence-framing-discipline`: C1 framed as "RECOMMENDED" with verdict reasons + C2/C3 framed as "REJECTED" with specific failure-mode citations; precision claims (e.g., "ADA4530-1 datasheet noise floor", "3 OOM tighter pressure") sourced from primary docs
- `substrate-native-check`: not applicable (chamber-priority is engineering/logistics, not substrate physics)
- Pure-AVE-corpus rule: all rationale framed as physics + engineering, no external-context refs

## Audit trail

- 2026-05-20 EOD+++++ — Q-C15-01 chamber priority scoping doc landed. C1 dedicated chamber RECOMMENDED based on 4-experiment chamber-profile comparison (C15 + AVE-Bench-VacuumMirror + C16-TORSION-05 + B5-PONDER-01). C2 + C3 REJECTED on HV-noise floor + apparatus-geometry incompatibility + schedule-coupling grounds. Grant adjudication pending; outcome flips Phase 0→1 promotion blocker (ii) from OPEN → CLOSED if C1 adjudicated.

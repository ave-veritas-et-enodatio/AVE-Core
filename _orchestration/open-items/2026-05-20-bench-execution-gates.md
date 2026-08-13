---
id: bench-execution-gates
title: C11 facility outreach and C15 KiCad — two bench gates that are Grant-manual, plus a rescope
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-05-20
source: _orchestration/experimental/c11-mach-zehnder/exp-c11-mach-zehnder.md
anchor: "Phase 0 is facility partnership search"
---

- **C11-MACH-ZEHNDER Phase 0** — facility partnership outreach (literature survey + contact with
  Hasselbach / LENS / NIST / TEM holography centres). Agent-prep complete. Status still `[PREP]` at
  `exp-c11-mach-zehnder.md:4`; **no outreach record exists anywhere** — every `facility partnership`
  hit is in a tracker, not a log.
- **C15-CLEAVE-01 Phase 1b** — KiCad GUI work (schematic ERC clean, PCB layout, guard-ring polygon,
  DRC). Grant-manual by sub-agent tooling limitation. Still at Phase 1a-rev1;
  AVE-Bench-FemtoElectrometer's last commit is `2f113e0` (2026-07-02) and the only KiCad artifacts
  are under `hardware/cad/_archive/2026-05-20_phase-1a-kicad-draft/`.

★ **C15 has been RESCOPED since the ask.** Docket `2026-08-01-bench-staleness-propagation.md:47`
quotes `project-cleave-01.md:39-40`: *"COUPLING-STATUS — NULL-CONFIRMED-FINAL (2026-07-02,
`clm-clvchn`) … the bench is a **corroborative-null discriminator**."* Decide against that scope,
not the original flagship framing.

Companion to `hopf-phase0b-hardware-mismatch`. Verified 2026-08-13 by sweep.

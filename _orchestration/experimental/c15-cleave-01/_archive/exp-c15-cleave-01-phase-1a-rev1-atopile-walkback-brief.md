# EXP-C15-CLEAVE-01 — Phase 1a-rev1 atopile walk-back brief (Q-C15-10 ✓ ADJUDICATED)

**Parent sub-epic**: [`exp-c15-cleave-01.md`](exp-c15-cleave-01.md)
**Parent epic**: [`experimental-arc.md`](experimental-arc.md)
**Predecessor**: [`exp-c15-cleave-01-phase-1-kicad-brief.md`](exp-c15-cleave-01-phase-1-kicad-brief.md) Phase 1a (delivered KiCad-native; merged at `331a778` on AVE-Bench-FemtoElectrometer)
**Phase**: 1a-rev1 — atopile walk-back + standalone module repo scaffold
**Grant adjudication**: 2026-05-20 EOD+++++++++ — Q-C15-10 ✓ ATOPILE (HOPF-style atopile-first pattern); modules live in **new sibling repo `AVE-Hardware-Modules`**

## Q-C15-10 adjudication context

Phase 1a delivered KiCad-native `.kicad_sch` S-expression — a workspace deviation from the established atopile-first pattern across AVE-PONDER (`metric_decoherence.ato`) + AVE-HOPF (`hopf_01.ato` + `hopf_02.ato`). Grant adjudicated walk-back to atopile.

Architectural decision: modules live in a **new sibling repo `AVE-Hardware-Modules`** (Option A from inline Q-C15-10 framing). Future bench/design repos `ato install` from this canonical home. Walks back C15 + establishes the workspace's first dedicated atopile-modules library.

## Phase 1a-rev1 scope decomposition

**Two-stage execution** (sequential, A → B):

| Stage | Implementor | Scope |
|---|---|---|
| **1a-rev1-A** | Implementor A | Scaffold `AVE-Hardware-Modules` sibling repo + create 8 modules + atopile package config + tests |
| **1a-rev1-B** | Implementor B (gated on A return) | Walk back AVE-Bench-FemtoElectrometer hardware to atopile (`cleave_01.ato` + `ato.yaml`) + decommission orphan `.kicad_sch` + `.md` companion + Q-C15-10 ✓ CLOSED + Q-C15-11 OPEN |

Sequencing rationale: Stage A creates the modules; Stage B imports them. B cannot proceed without A's modules existing + package metadata being installable.

## Module audit (the "audit your audit" pass)

Initial 5-module decomposition expanded to **8 modules** after rigorous schematic + BOM + adjudication audit. Gaps closed:

- **`precision_input_cap_10pf.ato`** — initially bundled into electrometer frontend; pulled out because C1 is KB-loadbearing with Q-C15-04 tolerance discipline + Phase 2 contingency (Kemet ±0.25 pF alt)
- **`ptfe_turret_post_standoff.ato`** — missed entirely in first pass; 4× Keystone 1610-3 standoffs for signal-path mechanical insulation (femto-Coulomb noise floor discipline)
- **Split** `subd_vacuum_feedthrough_interface.ato` into `subd9_supply_header.ato` + `molex3_pzt_header.ato` — Q-C15-07 adjudicated dedicated FT2 (no J1↔J2 pass-through); J1 and J2 are topologically independent

## Stage 1a-rev1-A — AVE-Hardware-Modules sibling repo scaffold + 8 modules

### Repo scope

Standalone sibling repo at `/Users/grantlindblom/AVE-staging/AVE-Hardware-Modules/`. **NOT** an experiment repo; it's a **pure atopile-modules package** for cross-repo reuse. Parallels AVE-Bench-VacuumMirror + AVE-Bench-FemtoElectrometer precedent for sibling-repo structural pattern but adapts for module-library semantics.

### Repo structure (deliverables)

| Path | Purpose | Template precedent |
|---|---|---|
| `README.md` | Status + depends-on AVE-Core + module catalog + install instructions | VacuumMirror README; adapt for module-library framing |
| `LICENSE` | Same license terms as VacuumMirror | Copy verbatim |
| `PATENTS.md` | IP-divide framing: modules are bench-engineering IP separate from framework IP | VacuumMirror PATENTS; adapt for module-library scope |
| `AGENTS.md` | Agent orientation for module-library work | VacuumMirror AGENTS; adapt |
| `CLAUDE.md` | Sibling-repo orientation (first read, structure, branch + commit hygiene, skill ecosystem) | AVE-Bench-FemtoElectrometer CLAUDE.md; adapt |
| `.agents/HANDOFF.md` + `.agents/workflows/` + `.agents/infrastructure_blueprint.md` | Agent doctrine | VacuumMirror precedent |
| `ato.yaml` | atopile package config: `requires-atopile: ^0.12.0` (match HOPF); `paths: {src: ., build: build}`; no top-level build entry (this is a modules package, not a buildable design) | HOPF precedent: `requires-atopile: ^0.12.0` + `paths` block |
| `modules/` directory | Home for the 8 standalone module `.ato` files (one per module) | NEW pattern — no precedent (PONDER + HOPF have inline definitions, not modular files) |
| `parts/` directory | Per-vendor-component KiCad symbols + footprints + 3D models referenced by the modules | PONDER `parts/` precedent (e.g., `parts/Murata_Electronics_GRM0335C1H101JA01D/`) |
| `tests/` directory | atopile build-tests per module: each module has a smoke-test build that instantiates it standalone + verifies ato compile succeeds | NEW pattern; tests/ subdirectory with per-module `test_<modulename>.ato` smoke tests |
| `docs/open_questions.md` | NEW Q-HWMOD-01 cross-repo sync tracking (= Q-C15-11 in AVE-Bench-FemtoElectrometer) + future open questions | VacuumMirror docs/open_questions precedent |
| `docs/glossary.md` | Module-library terminology (module / part / footprint / interface) | VacuumMirror docs/glossary precedent |
| `docs/design/2026-05-20_module-library-establishment.md` | Initial scoping rationale + Q-C15-10 walk-back context | VacuumMirror docs/design precedent |
| `pyproject.toml` + `setup.sh` + `Makefile` | PEP 420 namespace extension + combined-env setup | VacuumMirror precedent |
| `.gitignore` | atopile `build/` directory + Python `__pycache__` + venv | VacuumMirror precedent |

### 8 modules to create (in `modules/` directory)

Each module is a standalone `.ato` file. Each MUST: (a) declare its interface contract (input/output nets); (b) instantiate the canonical part(s) from `parts/`; (c) document its reuse class + Q-C15-XX adjudication backing inline; (d) carry a smoke-test in `tests/test_<modulename>.ato` that instantiates it standalone.

#### Module 1: `modules/ada4530_electrometer_frontend.ato`

**Captures**: U1 ADA4530-1ARZ (SOIC-8) + supply decoupling (C2-C5: 100 nF HF + 10 μF LF on each rail) + guard-ring net declaration + unity-gain feedback wiring (OUT → -IN).

**Parameters**:
- `v_supply`: nominal supply rail voltage (default ±15 V; ADA4530-1 supports ±5 V to ±18 V per datasheet)
- `supply_decoupling_hf`: HF decoupling cap value (default 100 nF X7R 0603)
- `supply_decoupling_lf`: LF decoupling cap value (default 10 μF X7R 0805)

**Interface (exposed nets)**:
- `signal_in` (input — connect to +IN through external C_in)
- `out` (output — Pin 6 OUT)
- `vcc`, `vee`, `gnd` (supply network)
- `guard` (guard-ring drive — Pin 4 GRD; consumer connects to PCB layout polygon)

**Reuse class**: any ultra-low-bias electrometer (femto-amp bias, electrostatic-charge measurement, ion-beam current, etc.)

**Adjudication refs**: none direct (KB-leaf §"The PCBA Implementation"); guard-ring discipline per ADI datasheet §"Guarding"

**Parts deps**: `parts/ADI_ADA4530-1ARZ/` (symbol + footprint + 3D model + datasheet PDF)

#### Module 2: `modules/precision_input_cap_10pf.ato`

**Captures**: 1× precision capacitor for electrometer signal input (default Murata GRM1885 NP0/C0G ±1% 10 pF 50 V 0603).

**Parameters**:
- `value`: cap value (default 10 pF; parameterize for non-10-pF reuse cases)
- `tolerance`: tolerance class (default 1% NP0/C0G; supports ±0.25 pF alt class via Kemet C0805C100D1GAC)
- `mpn`: manufacturer part number (default Murata GRM1885C1H100FA01D)

**Interface (exposed nets)**:
- `pin_in`
- `pin_out`

**Reuse class**: any femto-amp / electrometer needing precision $C_{in}$ for $V = Q/C$ readout

**Adjudication refs**: Q-C15-04 (parasitic $C_{in}$ control); KB-leaf §"The Falsification Metric"

**Parts deps**: `parts/Murata_GRM1885C1H100FA01D/` + `parts/Kemet_C0805C100D1GAC/` (alt)

#### Module 3: `modules/lm4040_voltage_reference.ato`

**Captures**: U2 LM4040 shunt voltage reference + R1 bias resistor (10 kΩ default).

**Parameters**:
- `vref`: reference voltage class (default 5.0 V; LM4040 family supports 2.048/2.5/3.0/4.096/5.0/8.192/10.0 V variants)
- `r_bias`: bias resistor (default 10 kΩ 1% 0603)
- `mpn`: manufacturer part number (default LM4040AIM3-5.0/NOPB)

**Interface (exposed nets)**:
- `vref_out` (precision reference voltage)
- `vcc` (positive supply)
- `gnd` (ground)

**Reuse class**: any bench needing precision voltage reference (DAC reference, ADC reference, bias generation)

**Adjudication refs**: none direct (bench supply discipline per reference_design.md §4.1)

**Parts deps**: `parts/TI_LM4040AIM3-5.0/`

#### Module 4: `modules/mill_max_ptfe_socket.ato`

**Captures**: 1× Mill-Max 3320-2-00-15-00-00-08-0 PTFE-insulated socket. Single instance per module; consumer instantiates as many as needed for their bench's role.

**Parameters**:
- `role`: human-readable label (e.g., `"signal_input"`, `"ground_return"`); doesn't affect electrical, just for clarity in higher-level designs

**Interface (exposed nets)**:
- `signal` (the central pin)
- `gnd` (the shield — for socket variants with shield; check Mill-Max 3320-2 datasheet — may be signal-only)

**Reuse class**: any vacuum-bench floating-plate signal connection OR explicit ground return (Q-C15-08 use case = 2 instances on same PCBA)

**Adjudication refs**: Q-C15-08 (dedicated PTFE-socket explicit floating-plate return; 2 instances on PCBA)

**Parts deps**: `parts/Mill-Max_3320-2/`

#### Module 5: `modules/ptfe_turret_post_standoff.ato`

**Captures**: 1× Keystone Electronics 1610-3 (or Cambion 450-2902-01-03-00 equivalent) PTFE turret post. Single instance per module; consumer instantiates 4× per ADI eval-board reference for signal-path insulation.

**Parameters**:
- `mpn`: manufacturer part number (default Keystone 1610-3)

**Interface (exposed nets)**:
- `pad_a` (top of turret, swaged wire termination)
- `pad_b` (bottom of turret, PCB pad)

**Reuse class**: any vacuum-bench needing PTFE-insulated mechanical signal-path support (electrometer benches, low-leakage analog front-ends)

**Adjudication refs**: none direct (reference_design.md §6 insulation discipline; ADI datasheet §"Guarding")

**Parts deps**: `parts/Keystone_1610-3/`

#### Module 6: `modules/subd9_supply_header.ato`

**Captures**: 1× TE Connectivity 5747840-3 9-pin sub-D right-angle through-hole PCB-mount male connector. Configured per Q-C15-07 adjudication (supply rails + Vref + ground only; **NO PZT pass-through**).

**Parameters**:
- `pin_assignment`: dict mapping pin numbers to net names (default: 1=vcc, 2=vee, 3=gnd, 4=vref_out, 5-7=spare, 8-9=spare)

**Interface (exposed nets)**:
- `vcc`, `vee`, `gnd`, `vref_out` (active pins)
- `spare_5`, `spare_6`, `spare_7`, `spare_8`, `spare_9` (NC pins; consumer can override pin assignment if needed)

**Reuse class**: any vacuum-bench using KJL `EFT0093033` 9-pin sub-D vacuum feedthrough for supply rails

**Adjudication refs**: Q-C15-07 (dedicated FT2; supply connector does NOT carry PZT drive)

**Parts deps**: `parts/TE_5747840-3/`

#### Module 7: `modules/molex3_pzt_header.ato`

**Captures**: 1× Molex 0022272031 3-pin KK 0.100" header for PZT drive lines. Configured per Q-C15-07 adjudication (PZT-only, routes through dedicated FT2 feedthrough).

**Parameters**:
- `pin_assignment`: dict (default: 1=pzt_out_hi, 2=pzt_out_lo, 3=pzt_rtn)

**Interface (exposed nets)**:
- `pzt_out_hi`, `pzt_out_lo`, `pzt_rtn`

**Reuse class**: any vacuum-bench with PZT drive interface; pairs with KJL `EFT0093033` dedicated PZT-feedthrough

**Adjudication refs**: Q-C15-07 (dedicated FT2 for PZT lines)

**Parts deps**: `parts/Molex_0022272031/`

#### Module 8: `modules/bnc_signal_output.ato`

**Captures**: 1× Amphenol B6252A1-ND3G-50 BNC vertical PCB-mount jack. Configured per Q-C15-09 adjudication (BNC shield IS the only external ground exit; single-point ground topology).

**Parameters**: none (this is a fixed-topology module — Q-C15-09 single-point ground means shield ties to PCBA GND star)

**Interface (exposed nets)**:
- `signal_in` (center pin — connects to upstream OUT signal)
- `gnd_shield` (shield + PCBA GND star tie; per Q-C15-09 this is the ONLY chassis-ground exit)

**Reuse class**: any vacuum-bench using KJL `EFT0013033` BNC feedthrough for signal output AND single-point external-ground topology

**Adjudication refs**: Q-C15-09 (external-only ground via FT1 BNC shield)

**Parts deps**: `parts/Amphenol_B6252A1/`

### Stage 1a-rev1-A deliverables list

1. Scaffold AVE-Hardware-Modules sibling repo per structure table above
2. Create the 8 module `.ato` files in `modules/` with full interface contracts + parameters + part instantiations
3. Create the 8 `parts/<vendor>_<mpn>/` subdirectories with symbol + footprint + 3D-model files (download from manufacturer or KiCad libraries; verify against vendor datasheets)
4. Create 8 smoke-test `.ato` files in `tests/test_<modulename>.ato` (each test instantiates one module standalone + verifies ato compile)
5. Configure `ato.yaml` with `requires-atopile: ^0.12.0` + `paths` block + per-module build entries in `tests/` for smoke verification
6. README.md with module catalog table + install instructions (`ato install git+https://github.com/ave-veritas-et-enodatio/AVE-Hardware-Modules.git`)
7. PATENTS.md applying ave-ip-divide-discipline: modules are bench-engineering IP, separable from any specific design
8. AGENTS.md + CLAUDE.md + .agents/ orientation per sibling-repo precedent
9. docs/open_questions.md with Q-HWMOD-01 cross-repo sync tracking entry (paired with Q-C15-11 in AVE-Bench-FemtoElectrometer)
10. docs/glossary.md + docs/design/2026-05-20_module-library-establishment.md
11. pyproject.toml + setup.sh + Makefile + .gitignore per precedent
12. `git init` + initial commit on `main` + `gh repo create ave-veritas-et-enodatio/AVE-Hardware-Modules --private --source=. --remote=origin --push` (Grant pre-authorized this remote setup per Q-C15-10 walk-back authorization; execute inline)
13. Run `ato build` on each smoke-test to verify all 8 modules compile (Phase 1a-rev1-A success gate)

## Stage 1a-rev1-B — AVE-Bench-FemtoElectrometer atopile walk-back

Gated on Stage A return + smoke-test pass.

### Deliverables

1. **New: `AVE-Bench-FemtoElectrometer/hardware/cleave_01.ato`** — top-level atopile design that imports the 8 modules + composes them per the post-adjudication topology:
   - 1× `ada4530_electrometer_frontend` (front_end)
   - 1× `precision_input_cap_10pf` (c_in)
   - 1× `lm4040_voltage_reference` (vref)
   - 2× `mill_max_ptfe_socket` (j3_signal role="signal_input"; j3_ground role="ground_return" per Q-C15-08)
   - 4× `ptfe_turret_post_standoff` (tp1-tp4)
   - 1× `subd9_supply_header` (j1; supply only per Q-C15-07)
   - 1× `molex3_pzt_header` (j2; dedicated FT2 per Q-C15-07)
   - 1× `bnc_signal_output` (j4; single-point external ground per Q-C15-09)
   - Wiring per ASCII signal-chain in [`AVE-Bench-FemtoElectrometer/hardware/cad/cleave_01_schematic.md`](AVE-Bench-FemtoElectrometer/hardware/cad/cleave_01_schematic.md) — BUT with adjudicated topology corrections:
     - J3_ground.signal → front_end.gnd (Q-C15-08 explicit return; new wiring)
     - J1 carries ONLY vcc + vee + gnd + vref_out (NO PZT pass-through; Q-C15-07)
     - J2 carries ONLY pzt lines, routes to dedicated FT2 (Q-C15-07)
     - J4 BNC shield = front_end GND ONLY external ground exit (Q-C15-09)

2. **New: `AVE-Bench-FemtoElectrometer/hardware/ato.yaml`** — atopile package config:
   - `requires-atopile: ^0.12.0`
   - `paths: {src: ., build: build}`
   - `builds: {default: {entry: cleave_01.ato:CleaveOne}}`
   - Dependency on AVE-Hardware-Modules via `ato install git+https://github.com/ave-veritas-et-enodatio/AVE-Hardware-Modules.git`

3. **Decommission orphan KiCad-native files**:
   - `hardware/cad/cleave_01_schematic.kicad_sch` (Phase 1a S-expression draft) — **delete** OR **move to `hardware/cad/_archive/`** with explicit "Phase 1a-rev1 atopile walk-back deprecated this" annotation
   - `hardware/cad/cleave_01_schematic.md` (ASCII companion) — **delete** OR **move to `hardware/cad/_archive/`** with same annotation
   - Implementor decision: prefer **archive** path (preserves audit trail via _archive subdirectory) over delete; ave-walk-back discipline favors preserving "what was tried" over outright removal

4. **Update `hardware/DESIGN_LOG.md`**:
   - New §7 "Phase 1a-rev1 atopile walk-back" — captures Q-C15-10 adjudication + scope + decommission path + cross-repo sync tracking via Q-C15-11
   - §3 decision 1.2 (off-PCBA DAC + HV amp) carried forward; module-level decisions logged per module

5. **Update `hardware/BOM.md`**:
   - No SKU changes (atopile walk-back doesn't change parts)
   - Update intro to reference `cleave_01.ato` + AVE-Hardware-Modules import as source-of-truth for component instantiation
   - Add cross-ref table mapping BOM rows to module-of-origin (e.g., U1 → `ada4530_electrometer_frontend.ato`)

6. **Update `hardware/TEST_PROCEDURE.md`**:
   - No procedure changes (atopile walk-back doesn't change test protocol)
   - Update references from `cleave_01_schematic.kicad_sch` → `cleave_01.ato` build output (`build/cleave_01.kicad_sch` after ato build)

7. **Update `hardware/ORDERING.md`**:
   - §2 PCB fab section updated: Gerbers come from `ato build` output (`build/cleave_01.kicad_pcb` + `build/cleave_01.kicad_sch`); Phase 1b/1c KiCad GUI work proceeds from build artifacts, not from source
   - Phase 1b workflow note: edit `.ato` source → `ato build` → opens `.kicad_pcb` in KiCad GUI for layout (atopile + KiCad round-trip)

8. **Update `docs/open_questions.md`**:
   - **Q-C15-10** OPEN → CLOSED 2026-05-20 EOD+++++++++++ — Grant adjudicated atopile (HOPF pattern, modules in AVE-Hardware-Modules sibling repo)
   - **Q-C15-11** NEW OPEN — cross-repo module synchronization tracking (paired with Q-HWMOD-01 in AVE-Hardware-Modules); scope: track changes in AVE-Hardware-Modules that obsolete inline definitions in PONDER/HOPF; phase: track-only, no active migration

9. **Branch + commit hygiene**:
   - Branch `analysis/phase-1a-rev1-atopile-walkback` off `main` in AVE-Bench-FemtoElectrometer
   - Commit on branch; push to origin
   - **DO NOT merge to main** — orchestrator + Grant review per Phase 1a precedent

### Decommission path rationale (preserve over delete)

Per ave-walk-back discipline: when a workspace pattern shifts (KiCad-native → atopile), preserve the prior artifacts as `_archive/` subdirectories rather than deleting outright. This preserves:
- Audit trail of "what was tried" before the adjudication
- Reference material for future cross-precedent questions (e.g., "what did the Phase 1a draft schematic look like?")
- Q-C15-10 walk-back evidence (the .kicad_sch + .md companion ARE the deviation that was walked back)

Naming: `hardware/cad/_archive/2026-05-20_phase-1a-kicad-draft/cleave_01_schematic.kicad_sch` + `cleave_01_schematic.md` + a `README.md` in the _archive subdirectory explaining what these were + why they're archived.

## Constraints (apply to both Stage A + Stage B implementors)

1. **Pure-AVE-corpus rule**: no investor/fund/interview/1517/pitch refs anywhere
2. **Canonical-source compliance**: ξ_topo numerical value MUST cite `AVE-Core/src/ave/core/constants.py:205`; never hard-code `4.149e-7` in any module or top-level
3. **ave-ip-divide-discipline**: AVE-Hardware-Modules contains bench-engineering IP (component definitions, footprints, interface contracts); framework IP stays in AVE-Core. PATENTS.md in AVE-Hardware-Modules adapts VacuumMirror precedent for module-library IP scope.
4. **Preserve KB-leaf prediction verbatim**: 41.5 mV/μm + 0.415 pC + outcome A/B/C/D + falsification clause continue to match `project-cleave-01.md` verbatim in any TEST_PROCEDURE updates
5. **Honor all prior Q-C15-XX adjudications**:
   - Q-C15-01 dedicated chamber (≤10⁻⁶ Torr, bell-jar/4''-6'' CF refurb)
   - Q-C15-03 vacuum-gap-only Phase 3 default
   - Q-C15-04 NP0/C0G ±1% target (with Kemet ±0.25 pF alt)
   - Q-C15-05 commodity PI N-216 PZT preferred
   - Q-C15-07 dedicated FT2 (J1+J2 topologically independent)
   - Q-C15-08 dedicated PTFE-socket explicit floating-plate ground return (2 instances of mill_max_ptfe_socket)
   - Q-C15-09 external-only ground via FT1 BNC shield (single-point ground topology)
   - Q1.2 off-PCBA DAC + HV amp (PCBA has only PZT header J2, NO on-PCBA HV)
6. **Pre-commit branch check**: verify `git branch --show-current` before each commit (mandatory after any sub-agent invocation)
7. **No merge to main**: implementor branches push to origin but do NOT merge; orchestrator + Grant review pre-merge per Phase 1a precedent
8. **Notation compliance** (per AVE-Core ave-kb/CLAUDE.md INVARIANT-N2): use `$\ell_{node}$` script-ell in any manuscript-style markdown content
9. **Skill discipline**: ave-canonical-source + ave-canonical-leaf-pull + verify-before-cite v1.4 + ave-evidence-framing-discipline + ave-ip-divide-discipline + ave-walk-back + pure-AVE-corpus throughout
10. **No engine code modification**: implementors read from AVE-Core but do not modify; AVE-Core orchestration walk-back is orchestrator's job post-implementor return

## Tool access

- `WebFetch` (deferred) — implementors load via `ToolSearch(query="select:WebFetch")` if they need to fetch atopile docs OR vendor part datasheets
- `gh` via Bash for GitHub queries + repo creation
- `ato` CLI via Bash for atopile package management + build verification
- `git` for branch + commit + push + tag

## Stage 1a-rev1-A success criteria

| Axis | Criterion |
|---|---|
| **Repo created** | `AVE-Hardware-Modules` live at `https://github.com/ave-veritas-et-enodatio/AVE-Hardware-Modules` (private) with `main` branch + initial commit |
| **Structure parity** | Top-level structure matches VacuumMirror within reason: README + LICENSE + PATENTS + AGENTS + CLAUDE + .agents/ + modules/ + parts/ + tests/ + docs/ + ato.yaml + setup.sh + pyproject.toml + Makefile + .gitignore |
| **8 modules present** | `modules/{ada4530_electrometer_frontend,precision_input_cap_10pf,lm4040_voltage_reference,mill_max_ptfe_socket,ptfe_turret_post_standoff,subd9_supply_header,molex3_pzt_header,bnc_signal_output}.ato` all present + each declares interface contract + parameters + part instantiation + reuse class doc-block |
| **Parts subdirs present** | `parts/{ADI_ADA4530-1ARZ, Murata_GRM1885C1H100FA01D, Kemet_C0805C100D1GAC (alt), TI_LM4040AIM3-5.0, Mill-Max_3320-2, Keystone_1610-3, TE_5747840-3, Molex_0022272031, Amphenol_B6252A1}/` directories with symbol + footprint + 3D-model files |
| **Smoke tests pass** | `tests/test_<modulename>.ato` for each module + `ato build` runs clean on each smoke test |
| **ato.yaml valid** | `requires-atopile: ^0.12.0` + paths + tests builds entry; passes `ato pkg validate` |
| **Q-HWMOD-01 captured** | `docs/open_questions.md` has Q-HWMOD-01 cross-repo sync tracking (paired with Q-C15-11) |
| **Pure-AVE-corpus** | grep audit returns zero matches for investor/fund/interview/1517/pitch anywhere in new files |
| **Remote configured + push** | `gh repo create` executed + `main` pushed to origin |

## Stage 1a-rev1-B success criteria

| Axis | Criterion |
|---|---|
| **Branch + commit** | `analysis/phase-1a-rev1-atopile-walkback` off `main` in AVE-Bench-FemtoElectrometer; commits on branch; pushed to origin; NOT merged to main |
| **cleave_01.ato exists** | `hardware/cleave_01.ato` declares 8-module composition per post-adjudication topology; imports from AVE-Hardware-Modules via `ato install` |
| **ato.yaml exists** | `hardware/ato.yaml` declares build entry `cleave_01.ato:CleaveOne` |
| **ato build succeeds** | `cd hardware && ato build` runs clean; emits `build/cleave_01.kicad_sch` + `build/cleave_01.kicad_pcb` |
| **Orphan KiCad files archived** | `hardware/cad/cleave_01_schematic.kicad_sch` + `cleave_01_schematic.md` moved to `hardware/cad/_archive/2026-05-20_phase-1a-kicad-draft/` with README.md explaining deprecation |
| **Q-C15-10 ✓ CLOSED** | `docs/open_questions.md` Q-C15-10 OPEN → CLOSED with Grant adjudication notes |
| **Q-C15-11 NEW OPEN** | `docs/open_questions.md` Q-C15-11 cross-repo sync tracking (paired with Q-HWMOD-01) |
| **DESIGN_LOG update** | `hardware/DESIGN_LOG.md` §7 NEW "Phase 1a-rev1 atopile walk-back" captures Q-C15-10 adjudication + decommission path + module list |
| **BOM cross-ref** | `hardware/BOM.md` adds table mapping BOM rows to module-of-origin |
| **TEST_PROCEDURE update** | references shifted from `.kicad_sch` to `cleave_01.ato` build outputs |
| **ORDERING update** | §2 PCB fab references `ato build` workflow |
| **KB-leaf prediction verbatim** | 41.5 mV/μm + 0.415 pC + outcome A/B/C/D + falsification clause unchanged across all updated files |
| **Pure-AVE-corpus** | grep audit returns zero matches |

## AVE-Core orchestration walk-back (orchestrator handles after BOTH stages return + merge)

1. Update `_orchestration/exp-c15-cleave-01.md` Phase 1a-rev1 entry + audit trail (Q-C15-10 closure + AVE-Hardware-Modules establishment + atopile walk-back merge)
2. Update `_orchestration/experimental-arc.md` C15 row + add new "AVE-Hardware-Modules sibling repo" cross-ref
3. Update `_orchestration/index.md` C15 row + Last-updated + add new active-epic-adjacent entry for AVE-Hardware-Modules if appropriate
4. Refresh `manuscript/ave-kb/vol4/falsification/.../project-cleave-01.md` Engineering substrate status — Phase 1a-rev1 atopile-walk-back state
5. Audit tag the Phase 1a-rev1 merge per AVE-HOPF/Phase-1a pattern (`audit/2026-05-20_phase-1a-rev1-atopile-walkback`)

## Q-C15-11 / Q-HWMOD-01 cross-repo sync tracking spec

To land in **both** `AVE-Bench-FemtoElectrometer/docs/open_questions.md` (as Q-C15-11) AND `AVE-Hardware-Modules/docs/open_questions.md` (as Q-HWMOD-01):

```markdown
## Q-C15-11 / Q-HWMOD-01. Cross-repo atopile module synchronization — OPEN 2026-05-20 EOD+++++++++

**Status:** OPEN (track-only; no active migration scope).

**Context:** Phase 1a-rev1 walk-back established `AVE-Hardware-Modules` as the canonical home for cross-repo atopile module reuse. New designs (starting with C15-CLEAVE-01) import modules from this sibling repo. Pre-existing designs (AVE-PONDER `metric_decoherence.ato`, AVE-HOPF `hopf_01.ato` + `hopf_02.ato`) have inline component definitions + hand-rolled parts/ subdirectories that predate this module-library pattern.

**Question:** When modules in `AVE-Hardware-Modules` evolve (e.g., bug fix to a part footprint, parameter expansion, new variant), how do pre-existing designs in PONDER + HOPF surface or absorb these changes? And conversely, when PONDER + HOPF surface useful component definitions inline, when should those be promoted to `AVE-Hardware-Modules` for cross-repo reuse?

**Resolution path:** Track-only Phase 1a-rev1 → Phase 4. Active migration is OUT OF SCOPE until: (a) a specific module evolution would block a PONDER/HOPF design improvement, or (b) >2 design repos use the same inline definition and the migration cost-benefit flips. No proactive migration planned.

**Tracking convention:** Open this question identically in both `AVE-Bench-FemtoElectrometer/docs/open_questions.md` (Q-C15-11) AND `AVE-Hardware-Modules/docs/open_questions.md` (Q-HWMOD-01). Phase 4 outcome review for C15 includes a status check on this tracking item.
```

## Audit trail

- 2026-05-20 EOD+++++++++ — Phase 1a-rev1 atopile walk-back brief established. Grant adjudication captured (Q-C15-10 ✓ ATOPILE, Option A new sibling repo). 8-module decomposition audited (initial 5 → expanded to 8 after gap analysis: precision_input_cap_10pf pulled out, ptfe_turret_post_standoff added, sub-D split into supply + PZT modules per Q-C15-07). Two-stage implementor scope: Stage A AVE-Hardware-Modules scaffold + 8 modules + tests; Stage B AVE-Bench-FemtoElectrometer atopile walk-back + decommission orphans + Q-C15-11 NEW OPEN. Stage B gated on Stage A return. Brief constraints (10) + success criteria (Stage A: 9 / Stage B: 12) explicit. Cross-repo sync tracking spec for Q-C15-11 / Q-HWMOD-01 included.

# Q-C15-12 Stage A Fix + Stage B Revision Brief (Path 1 — clean module-level imports)

**Parent sub-epic**: [`exp-c15-cleave-01.md`](exp-c15-cleave-01.md)
**Predecessor**: [`_archive/exp-c15-cleave-01-phase-1a-rev1-atopile-walkback-brief.md`](_archive/exp-c15-cleave-01-phase-1a-rev1-atopile-walkback-brief.md)
**Phase**: 1a-rev1 closure — Q-C15-12 Path 1
**Grant adjudication**: 2026-05-20 EOD+++++++++++++ — Path 1 (fix Stage A first then revise Stage B clean)
**New skill applies**: [`ave-module-library-discipline` v1.0](~/.claude/skills/ave-module-library-discipline/SKILL.md) (created 2026-05-20 from Q-C15-12 case study; this brief is the first to require Rules 1-5 as explicit success criteria)

## Path 1 adjudication context

Phase 1a-rev1 Stage A delivered `AVE-Hardware-Modules` with all smoke tests passing black-box compile (per the Phase 1a-rev1-A brief's success criteria). Stage B integration caught 2 latent module bugs + 1 ato.yaml gap:

- **Bug (i)** `mill_max_ptfe_socket.ato:76` declares `signal = new Electrical` — `signal` is reserved `signaldef_stmt` keyword in atopile 0.12+. Consumer-side `.signal` access fails parsing.
- **Bug (ii)** `ptfe_turret_post_standoff.ato:85` references `tp.2 ~ pad_b` — Keystone_1610_3_package declares only `pin 1`. Phantom pin reference; module compile fails at consumer instantiation.
- **Gap (iii)** `AVE-Hardware-Modules/ato.yaml` lacks `package:` block required for `ato install` consumability in atopile 0.12.5.

Stage B workaround: direct-part imports (semantically equivalent but bypasses module abstraction).

Grant adjudicated **Path 1**: fix Stage A first, then revise Stage B's `cleave_01.ato` to use clean module-level imports (drop the workaround). Outcome: `AVE-Hardware-Modules/main` ships clean; `AVE-Bench-FemtoElectrometer/main` after Phase 1a-rev1 merge has clean module imports.

## Combined two-repo scope (single implementor session, sequential)

| Stage | Repo | Branch | Scope |
|---|---|---|---|
| **A-fix** | AVE-Hardware-Modules | `analysis/q-c15-12-stage-a-fix` off `main` (`e2171cb`) | 3 module/yaml fixes + 8 new consumer-wiring smoke tests + Q-HWMOD-04 NEW OPEN + merge `--no-ff` + audit tag |
| **B-rev** | AVE-Bench-FemtoElectrometer | `analysis/phase-1a-rev1-atopile-walkback` (existing, at `b44b1f7`) | Revise `cleave_01.ato` to swap direct-part workaround → clean module imports + Q-C15-12 OPEN → CLOSED + DESIGN_LOG §7 update + verify `ato build` clean + (orchestrator merges with audit tag post-return) |

Sequential ordering: A-fix MUST merge first (B-rev's clean imports reference fixed modules). Single implementor session executes both stages in order; combined `ato build` verification at end exercises both repos' clean state.

## Stage A-fix deliverables (in order)

### D1 — Rename `signal` → `sig` in `mill_max_ptfe_socket.ato`

Edit `AVE-Hardware-Modules/modules/mill_max_ptfe_socket.ato`:
- Line 76: `signal = new Electrical` → `sig = new Electrical`
- Line 82: `j.1 ~ signal` → `j.1 ~ sig`
- Docstring lines 12, 17, 21, 58, 62: every `.signal` consumer-doc reference → `.sig`

Justification: HOPF precedent (`AVE-HOPF/hardware/hopf_01.ato:30` `interface RF_Port` uses `sig`) — established workspace safe-naming convention. `signal` is reserved in atopile 0.12+ `signaldef_stmt`.

### D2 — Remove phantom `tp.2 ~ pad_b` in `ptfe_turret_post_standoff.ato`

Edit `AVE-Hardware-Modules/modules/ptfe_turret_post_standoff.ato`:
- Delete line 85: `tp.2 ~ pad_b`
- The module's exposed `pad_b` field becomes either: (a) deleted entirely if `pad_b` is unused elsewhere, OR (b) renamed/rewired to a different topology if `pad_b` was intentional but landed on wrong part-pin

Investigation step: grep the module for all `pad_a` and `pad_b` references; verify whether `pad_b` is a valid second pin (which the Keystone 1610-3 doesn't have — it's a single-pin turret post) or whether the module's interface declared 2 pads as an architectural error.

Most likely fix: delete `pad_b` field entirely from module's interface; consumer code (in `cleave_01.ato`) wires only `pad_a`. If `pad_b` was load-bearing for a different consumer use case, surface as Q-HWMOD-05 NEW OPEN for module-interface scoping.

### D3 — Add `package:` block to `AVE-Hardware-Modules/ato.yaml`

Edit `AVE-Hardware-Modules/ato.yaml`:
- Add `package:` block at top with `name: ave-hardware-modules`, `version: 0.1.0`, `description: AVE shared atopile module library`, `authors: ["Grant Lindblom <grant6t@gmail.com>"]`
- Preserve existing `requires-atopile: ^0.12.0` + `paths` + `builds` blocks

Verify: run `ato build` against an existing smoke test to confirm `package:` block doesn't break in-repo testing.

### D4 — Consumer-wiring smoke tests for ALL 8 modules (per `ave-module-library-discipline` Rule 1)

Replace each `tests/test_<modulename>.ato` to exercise consumer-side wiring of every exposed interface field, NOT just black-box instantiation.

**Anti-pattern (current Stage A — what the new skill catches):**
```ato
module SmokeTest_MillMaxPtfeSocket:
    dut = new MillMaxPtfeSocket
    # Never accesses .signal, .gnd — black-box compile only
```

**Required pattern:**
```ato
module SmokeTest_MillMaxPtfeSocket:
    dut = new MillMaxPtfeSocket
    test_sig_net = new Electrical
    dut.sig ~ test_sig_net   # Exercises consumer-side access on renamed field
    # Repeat for every exposed interface field
```

Apply this pattern to all 8 modules:
1. `test_ada4530_electrometer_frontend.ato` — wire through `signal_in`, `out`, `vcc`, `vee`, `gnd`, `guard`
2. `test_precision_input_cap_10pf.ato` — wire through `pin_in`, `pin_out`
3. `test_lm4040_voltage_reference.ato` — wire through `vref_out`, `vcc`, `gnd`
4. `test_mill_max_ptfe_socket.ato` — wire through `sig` (renamed from `signal`), `gnd`
5. `test_ptfe_turret_post_standoff.ato` — wire through `pad_a` (only; `pad_b` removed per D2)
6. `test_subd9_supply_header.ato` — wire through `vcc`, `vee`, `gnd`, `vref_out`, spare pins as needed
7. `test_molex3_pzt_header.ato` — wire through `pzt_out_hi`, `pzt_out_lo`, `pzt_rtn`
8. `test_bnc_signal_output.ato` — wire through `signal_in`, `gnd_shield`

Run `ato build` for each updated smoke test; verify ALL 8 pass clean. The consumer-wiring exercise is the gate that would have caught bugs (i) + (ii) in Stage A.

### D5 — Q-HWMOD-04 NEW OPEN in `AVE-Hardware-Modules/docs/open_questions.md`

Append:
```markdown
## Q-HWMOD-04. Module-library testing discipline gap (paired with Q-C15-12 in AVE-Bench-FemtoElectrometer) — CLOSED 2026-05-20 EOD+++++++++++++ (Q-C15-12 Path 1 Stage A fix landed)

**Status:** CLOSED 2026-05-20 EOD+++++++++++++ via Stage A fix (this commit).

**Question:** Phase 1a-rev1-A black-box smoke tests passed (compile-only) but missed 2 latent bugs + 1 ato.yaml gap that surfaced at consumer-side integration in Stage B. What testing discipline closes the gap?

**Resolution:** `ave-module-library-discipline v1.0` skill (created 2026-05-20 at ~/.claude/skills/ave-module-library-discipline/SKILL.md) formalizes Rules 1-5 for module-library publishing:
- Rule 1: smoke tests exercise consumer-side wiring of every exposed interface field
- Rule 2: reserved-keyword scan on interface field names
- Rule 3: `package:` block required in ato.yaml for ato-install consumability
- Rule 4: part-instantiation pin references must match part declaration
- Rule 5: cross-version atopile syntax check

This Stage A fix applies all 5 rules retroactively: D1 (Rule 2 rename signal→sig), D2 (Rule 4 remove phantom pin), D3 (Rule 3 package block), D4 (Rule 1 consumer-wiring smoke tests). Brief-level discipline gap (Rule 1 not required in Phase 1a-rev1-A brief success criteria) is the upstream cause; future module-library briefs must invoke the skill explicitly.

**Cross-ref**: Q-C15-12 in AVE-Bench-FemtoElectrometer/docs/open_questions.md (paired closure).
```

### D6 — Stage A fix branch + commit + push + merge `--no-ff` + audit tag

Branch + commit hygiene per AVE-HOPF / AVE-Bench-FemtoElectrometer precedent:

1. `git checkout -b analysis/q-c15-12-stage-a-fix` off `main` (`e2171cb`)
2. Commit D1-D5 changes (1 combined commit OK or multiple per-deliverable)
3. Push branch to origin
4. Run all 8 smoke tests `ato build` clean — VERIFY before merge
5. **Implementor MAY merge Stage A immediately** (per Grant Path 1 authorization, this stage is pre-authorized; no separate Grant review gate):
   - Tag branch tip: `git tag audit/2026-05-20_q-c15-12-stage-a-fix <branch-tip>`
   - Switch to main: `git checkout main`
   - Merge `--no-ff` with detailed merge-commit message
   - Push main + tag to origin
   - Delete branch (local + remote)

Audit tag: `audit/2026-05-20_q-c15-12-stage-a-fix`. Preserves immutable branch tip + tree + ancestry per AVE-HOPF/AVE-Bench-FemtoElectrometer pattern.

## Stage B-rev deliverables (after Stage A merge lands)

### D7 — Revise `cleave_01.ato` for clean module-level imports

Edit `AVE-Bench-FemtoElectrometer/hardware/cleave_01.ato` on existing branch `analysis/phase-1a-rev1-atopile-walkback`:

- Replace direct-part imports (workaround) with clean module-level imports:
  - `MillMax_3320_2_package` direct import → `mill_max_ptfe_socket.MillMaxPtfeSocket` module import (now that Stage A bug is fixed)
  - `Keystone_1610_3_package` direct import → `ptfe_turret_post_standoff.PtfeTurretPostStandoff` module import (now that Stage A bug is fixed)
- Update wiring to use renamed `sig` field on mill_max_ptfe_socket (was `signal` pre-Stage-A-fix)
- Verify other 6 module imports still resolve clean

### D8 — Update `cleave_01.ato` ato.yaml dependencies

Now that `AVE-Hardware-Modules` has `package:` block (Stage A D3), update `AVE-Bench-FemtoElectrometer/hardware/ato.yaml`:
- Add `dependencies:` block referencing AVE-Hardware-Modules per atopile 0.12.5 syntax (`registry://` / `git://` / `file://` — verify exact form via atopile docs or `ato install --help`)
- Drop relative-path imports if `ato install` workflow now works

### D9 — Update `docs/open_questions.md` Q-C15-12 OPEN → CLOSED

Edit `AVE-Bench-FemtoElectrometer/docs/open_questions.md`:
- Q-C15-12 status: OPEN → CLOSED 2026-05-20 EOD+++++++++++++ via Stage A fix landed at `<audit tag commit hash>` + Stage B revision in this branch
- Cross-ref to `AVE-Hardware-Modules/docs/open_questions.md` Q-HWMOD-04

### D10 — Update `hardware/DESIGN_LOG.md` §7 closure note

Append §7 note documenting Q-C15-12 closure path:
- Stage A fix landed at `audit/2026-05-20_q-c15-12-stage-a-fix`
- Stage B revision in this branch: clean module imports (4 direct-part imports → matching module imports)
- `ave-module-library-discipline v1.0` skill applied retroactively

### D11 — Verify `ato build` clean on revised `cleave_01.ato`

Run `cd AVE-Bench-FemtoElectrometer/hardware && ato build` — must succeed clean on the revised composition.

### D12 — Commit on existing branch (do NOT merge)

- `git branch --show-current` should show `analysis/phase-1a-rev1-atopile-walkback`
- Commit D7-D11 with message documenting Q-C15-12 closure path
- Push to origin
- **DO NOT merge** — orchestrator + Grant pre-merge review + final merge per Phase 1a precedent

## Constraints (apply to both Stages A-fix + B-rev)

1. **Pure-AVE-corpus rule** — no investor/fund/interview/1517/pitch refs anywhere
2. **Canonical-source compliance** — ξ_topo via `AVE-Core/src/ave/core/constants.py:205`; never hard-code in any module or in cleave_01.ato
3. **No engine code modification** — read from AVE-Core but do not modify
4. **KB-leaf prediction verbatim** — 41.5 mV/μm + 0.415 pC + outcome A/B/C/D + falsification clause preserved in any TEST_PROCEDURE updates
5. **All prior Q-C15-XX adjudications honored** — Q-C15-01 dedicated chamber + Q-C15-03 vacuum-gap-only default + Q-C15-04 NP0/C0G ±1% + Q-C15-05 commodity PZT + Q-C15-07 dedicated FT2 + Q-C15-08 dedicated PTFE-socket return + Q-C15-09 external-only ground + Q1.2 off-PCBA HV amp + Q-C15-10 atopile + Q-C15-11 cross-repo sync tracking
6. **Pre-commit branch check** — `git branch --show-current` before each commit (mandatory after any sub-task that might switch branch)
7. **ave-module-library-discipline Rules 1-5 applied** (per the new skill at `~/.claude/skills/ave-module-library-discipline/SKILL.md`):
   - Rule 1: consumer-wiring smoke tests for ALL 8 modules in Stage A D4
   - Rule 2: signal → sig rename in D1 (HOPF precedent)
   - Rule 3: package: block in D3
   - Rule 4: phantom pin reference fix in D2
   - Rule 5: verify atopile 0.12.5 syntax compatibility throughout
8. **Stage A may auto-merge** per Grant Path 1 authorization (no separate review gate); Stage B does NOT auto-merge — orchestrator + Grant review
9. **Cross-repo sync (Q-C15-11/Q-HWMOD-01)** — track-only; no active migration of PONDER/HOPF inline definitions in this stage
10. **`ato build` clean verification** required for BOTH Stage A all-8-smoke-tests AND Stage B cleave_01.ato top-level

## Tool access

- `WebFetch` deferred — load via `ToolSearch(query="select:WebFetch", max_results=1)` if needed for atopile 0.12.5 `dependencies:` block syntax verification
- `gh` via Bash for GitHub queries
- `ato` CLI via Bash (atopile 0.12.5 per Stage A confirmation; per-repo `.venv-ato/` workaround per Stage B implementor's documentation if local install broken)
- `git` for branch + commit + push + tag + merge

## Success criteria (combined Stages A-fix + B-rev)

### Stage A-fix

| Axis | Criterion |
|---|---|
| Branch + push + merge | `analysis/q-c15-12-stage-a-fix` pushed to origin, merged `--no-ff` to `main`, audit tag `audit/2026-05-20_q-c15-12-stage-a-fix` pushed, branch deleted (local + remote) |
| D1 signal rename | `grep -n "signal" mill_max_ptfe_socket.ato` returns ZERO matches outside docstrings; `grep -n "sig\b" mill_max_ptfe_socket.ato` shows renamed field |
| D2 phantom pin removed | `grep -n "tp.2" ptfe_turret_post_standoff.ato` returns ZERO matches |
| D3 package: block | `grep -A4 "^package:" ato.yaml` shows valid name/version/description block |
| D4 consumer-wiring tests | All 8 `tests/test_*.ato` files exercise `.field ~ test_net` for every exposed interface field; `ato build` clean on each |
| D5 Q-HWMOD-04 captured | `docs/open_questions.md` has Q-HWMOD-04 paired with Q-C15-12 |
| ave-module-library-discipline | Rules 1-5 all applied; commit message cites skill |
| Pure-AVE-corpus | grep audit returns zero matches |

### Stage B-rev

| Axis | Criterion |
|---|---|
| Branch on existing | Branch `analysis/phase-1a-rev1-atopile-walkback` extended with new commit(s); NOT merged |
| D7 cleave_01.ato clean | grep for `MillMax_3320_2_package` direct-imports returns ZERO matches; matching module-import statements visible |
| D8 ato.yaml dependencies | `dependencies:` block references AVE-Hardware-Modules per 0.12.5 syntax; `ato install` workflow tested (if possible) |
| D9 Q-C15-12 CLOSED | `docs/open_questions.md` Q-C15-12 OPEN → CLOSED with Stage A audit-tag commit hash cross-ref |
| D10 DESIGN_LOG §7 | Closure note appended with Q-C15-12 + Q-HWMOD-04 + ave-module-library-discipline cross-refs |
| D11 ato build clean | `ato build` on `cleave_01.ato` succeeds; new clean module-import composition verified |
| KB-leaf verbatim | 41.5 mV/μm + 0.415 pC + outcome A/B/C/D unchanged |
| Pure-AVE-corpus | grep audit zero matches |
| NOT merged | Branch pushed to origin; orchestrator/Grant pre-merge review |

## Post-Stage-B walk-back (orchestrator handles)

After Stage B return + verification:
1. Update `_orchestration/experimental/c15-cleave-01/exp-c15-cleave-01.md` Phase table: Phase 1a-rev1 status → "Stage B revision LANDED + clean module imports + Q-C15-12 CLOSED"
2. Orchestrator + Grant pre-merge review on Stage B branch
3. Merge `--no-ff` + audit tag `audit/2026-05-20_phase-1a-rev1-atopile-walkback` on AVE-Bench-FemtoElectrometer main
4. Update KB leaf `project-cleave-01.md` Engineering substrate status — Phase 1a-rev1 ✓ MERGED with clean atopile module imports
5. Update AVE-Core orchestration: index.md adjudication queue (Q-C15-12 removed from queue); experimental-arc.md C15 row; consolidated sub-epic doc

## Audit trail

- 2026-05-20 EOD+++++++++++++ — Q-C15-12 Path 1 Stage A fix + Stage B revision brief established. Grant adjudicated Path 1 inline. `ave-module-library-discipline v1.0` skill created same session; first brief to require Rules 1-5 as explicit success criteria. Implementor dispatch follows orchestration commit.

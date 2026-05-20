# EXP-A1-HOPF — AVE-HOPF Repo Phase A Audit (Read-Only)

**Parent epic**: [`exp-a1-hopf.md`](exp-a1-hopf.md) (Phase 0 pre-fab gate)
**Audit type**: Read-only structural + execution-readiness sweep of `/Users/grantlindblom/AVE-staging/AVE-HOPF`
**Audit date**: 2026-05-20
**AVE-Core branch at audit**: `analysis/integration` @ `6621dae`
**AVE-HOPF branch at audit**: `research/hopf-01-testing` @ `cfc5a40`
**Scope**: 8 axes per Grant request: repo structure, tooling, KB, engine/code, AVE-Core tie-in, A1-HOPF execution gaps, IP audit, promotion workflow
**Output discipline**: write-only to this doc; no AVE-HOPF modifications; no commits

---

## Executive summary

1. **AVE-HOPF is structurally healthy and execution-ready, but the canonical sub-epic doc cites the WRONG hardware files for the HOPF-02a target.** Three citations in `exp-a1-hopf.md` (`hardware/Gerbers/`, `hardware/BOM.md`, `hardware/TEST_PROCEDURE.md`) all resolve to HOPF-01-pilot artifacts; the HOPF-02a equivalents are embedded inside `hardware/hopf_02_ASSEMBLY_GUIDE.md` and `hopf_02a.kicad_pcb` and must be generated/extracted before fab submission.
2. **89 fast tests passing is verified** (live `pytest` run: 89 passed, 14 skipped, 103 collected; the 14 skipped are docker-marked OpenEMS tests, auto-skipped without container). HANDOFF claim is honest.
3. **HOPF-02a Gerbers do NOT exist as built artifacts** — `hardware/Gerbers/` and both `Gerbers 2.zip`/`Gerbers 3.zip` contain HOPF-01 Gerbers only. Per HANDOFF TODO #1, Grant must run `kicad-cli pcb export gerbers hardware/hopf_02a.kicad_pcb` before JLCPCB submission. This is BLOCKING for Phase 0 fab.
4. **HOPF-02a BOM is documented but not as a top-level file** — the $123 BOM lives at `hardware/hopf_02_ASSEMBLY_GUIDE.md:21-32`; the top-level `hardware/BOM.md` is the $142 HOPF-01 BOM. Sub-epic citation `[BOM.md](AVE-HOPF/hardware/BOM.md)` resolves to the wrong file.
5. **Constants-gate gap**: `scripts/hopf_02_nec2_run.py:88` hard-codes `ALPHA = 7.2973525693e-3` instead of importing from `ave.core.constants`. This violates the 2026-05-05 constants-gate decision (HANDOFF.md:74) but evades `verify_local_universe.py` because alpha-as-fraction is not in the `MAGIC_NUMBERS` whitelist (only 137.036 is). All other production scripts import correctly. The verify gate currently reports green ("MATHEMATICALLY PURE") despite this leak.
6. **IP-divide architecture is correctly oriented but has pointer-opacity violations.** AVE-HOPF is declared PRIVATE (LICENSE: "All rights reserved... Patents pending"). Cross-references INTO AVE-HOPF from public AVE-Core use explicit private paths (18 in `exp-a1-hopf.md`, 10+ in `project-hopf-02.md`) instead of the opaque `<!-- private-downstream: APP-XX -->` pattern from `ave-ip-divide-discipline` Step 4. No `.ip-graph.yaml` exists in AVE-HOPF.
7. **AVE-Core canonical KB leaves correctly reference AVE-HOPF** for HOPF-02 work: `project-hopf-02.md` mirrors namespace split + ($123/$278) BOM costs + outcome adjudication grid; `torus-knot-baryon-predictions.md` carries (2,5) proton + FI-13 RESOLVED framing; no stale rows detected at audit. The previously-flagged "Phase 1 walk-back targets" in `exp-a1-hopf.md` lines 54-57 appear to be ALREADY-DONE — both target leaves are at current canon state.
8. **Pure-AVE-corpus rule sweep is CLEAN** — zero hits for 1517 / investor / fund / pitch terms across tracked AVE-HOPF files.
9. **Pre-reg discipline GAP** — no `ave-prereg`-format pre-registration doc exists for the HOPF-02a VNA measurement. Sub-epic Phase 2 calls for one; it has not been drafted yet. Required before Phase 2 measurement, but Phase 0 fab can proceed in parallel.
10. **Promotion workflow is informal and undocumented** — engine work in AVE-HOPF flows back to AVE-Core via ad-hoc cross-repo refs (KB-leaf citations of AVE-HOPF paths). No checklist, no `.ip-graph.yaml`, no extraction-procedure runbook. The general `ave-ip-divide-discipline` skill carries the abstract procedure but there's no HOPF-specific instantiation.

**Severity tally**: 23 SOLID / 11 ATTENTION / 3 BLOCKING

The 3 BLOCKING items are all Phase 0 / Phase 2 prerequisites — none are deep-structural problems; each is a 5-30 minute fix Grant can do before submitting fab.

---

## Axis 1 — Repo Structure + Formatting

### What's solid

1. **Top-level layout is consistent with the documented schema** in `AGENTS.md:23-37`. Verified directories: `manuscript/`, `hardware/`, `scripts/`, `tests/`, `data/`, `docs/`, `build/`, `.agents/`, plus standard files `AGENTS.md`, `CLAUDE.md`, `README.md`, `LICENSE`, `PATENTS.md`, `Makefile`, `pyproject.toml`, `setup.sh`, `uv.lock`. ✓ SOLID
2. **`docs/` structure follows the AGENTS.md convention.** `docs/runs/`, `docs/analysis/`, `docs/design/` separation is enforced and dated (`2026-05-{02,03,04,05,06}_*.md`). 21 analysis docs + 4 design docs + 1 run doc + 6 top-level reference docs (`open_questions`, `manuscript_reconciliation`, `concept_map`, `glossary`, `ave_crib_sheet`, `SESSION_STATE_2026-05-05`). ✓ SOLID
3. **HOPF-01/02/03 namespace split (2026-05-06 reconciliation per HANDOFF.md:76) is enforced consistently** across `scripts/`, `manuscript/vol_hopf/chapters/14_decision_gate.tex`, and `docs/manuscript_reconciliation.md`. `scripts/hopf_03_spatial_refraction.py` (concept-only) is distinguished from `scripts/hopf_02_*.py` (fab-ready). ✓ SOLID
4. **`manuscript/vol_hopf/chapters/` has exactly 14 chapters** as HANDOFF claims (`01_chiral_coupling_prediction.tex` through `14_decision_gate.tex` + `_manifest.tex`). PDF builds to `build/AVE_HOPF.pdf`. ✓ SOLID
5. **`.agents/` is structured per the AVE-Core convention**: `HANDOFF.md` (canonical living state), `handoffs/` (one-time + archive), `workflows/` (audit-code, audit-full, audit-latex, audit-math, peer-review per AGENTS.md:128 claim of md5-identical to AVE-Core). ✓ SOLID
6. **`.agents/handoffs/BRANCH_STATE_2026-05-18_research-hopf-01-testing.md`** is a recent (2026-05-18) branch-state snapshot synced with the AVE-Core REPO-ARCH-12 sweep. ✓ SOLID

### What needs attention

7. **`hardware/` has accumulated zip files (`Gerbers 2.zip`, `Gerbers 3.zip`)** alongside the active `hardware/Gerbers/` directory. Both zips contain HOPF-01 Gerbers (verified via `unzip -l` — all `hopf_01-*.gbr`). ⚠ ATTENTION — these are dead snapshots; recommend either deleting or moving to `hardware/_archive/`. (~5 min effort)
8. **`hardware/` mixes HOPF-01 + HOPF-02a artifacts at the same hierarchy level** with no `hopf_01/` and `hopf_02/` subdirectories. Files like `BOM.md` (HOPF-01), `ORDERING.md` (HOPF-01), `TEST_PROCEDURE.md` (HOPF-01) are siblings of `hopf_02.ato`, `hopf_02a.kicad_pcb`, `hopf_02_ASSEMBLY_GUIDE.md`, `hopf_02_generate_kicad_pcb.py`. ⚠ ATTENTION — this is the **root cause** of the 3 sub-epic citation errors (Executive Summary #1). Recommend either (a) sub-directorize, OR (b) rename HOPF-01 generic files to `hopf_01_*` explicit prefix, OR (c) create `hopf_02a_BOM.md` / `hopf_02a_ORDERING.md` / `hopf_02a_TEST_PROCEDURE.md` as canonical HOPF-02a counterparts. ~30 min effort, biggest win for Phase 0 readiness.
9. **`hardware/assembly_guide/` is the HOPF-01 antenna-windings guide** (15 PNGs for trefoil/cinquefoil/etc.), not the HOPF-02 assembly guide. The HOPF-02 assembly guide is at the parent-level `hardware/hopf_02_ASSEMBLY_GUIDE.md` (singular file, 376 lines). Sub-epic doc lines 42 + 70 + 85 cite `hardware/assembly_guide/` — which is HOPF-01-specific. ⚠ ATTENTION

### Recommendations

- **(R1.1, 30 min)** Rename or re-organize `hardware/` so HOPF-02a artifacts are unambiguously addressable. Suggest: `hardware/hopf_02a_BOM.md`, `hardware/hopf_02a_ORDERING.md`, `hardware/hopf_02a_TEST_PROCEDURE.md` as explicit HOPF-02a documents (extract from the assembly guide for BOM; new content for ORDERING with v-score note; either extract Phase F-G from assembly guide for TEST_PROCEDURE or rename existing TEST_PROCEDURE.md → `hopf_01_TEST_PROCEDURE.md` and create HOPF-02a sibling).
- **(R1.2, 5 min)** Archive `Gerbers 2.zip` and `Gerbers 3.zip` to `hardware/_archive/` or delete (both are HOPF-01).

---

## Axis 2 — Tooling

### What's solid

1. **Python build path is canonical for fab**: `hardware/hopf_02_generate_kicad_pcb.py` reads `data/hopf_02/*_wire.csv` and emits `hopf_02a.kicad_pcb` (verified via Makefile target documentation + HANDOFF.md:75 decision). Documented as "the canonical fab path bypassing the still-unblocked `ato build` layout-init issue." ✓ SOLID
2. **89 fast tests passing — VERIFIED via live `pytest`** (collected 103, 89 passed, 14 skipped, 0 failed). The 14 skipped are `pytest.mark.docker` OpenEMS tests, auto-skipped without the `hopf01-nec2c` Docker image per `pyproject.toml:18-19`. Test files: `test_geometry.py` (26), `test_hopf02_geometry.py` (44 — the HOPF-02 set), `test_spec_compliance.py` (19), `test_solver_validation.py` (9, mostly docker-marked), `test_convergence.py` (5). ✓ SOLID
3. **`make verify` runs both gates**: DAG anti-cheat + Core parity. Both report green at audit time:
   - `tests/verify_local_universe.py` → "Successfully verified 56/56 local scripts" (constants smuggling check)
   - `tests/verify_core_parity.py` → "All 56 local scripts bind safely to AVE-Core" (parity sweeper mapping 2,829 public signatures across 96 upstream files)
   ✓ SOLID for the gates that exist; see ⚠ on gap below.
4. **`pyproject.toml` is minimal and correct**: numpy ≥ 2.0, scipy ≥ 1.14, matplotlib ≥ 3.9, pytest ≥ 8.0 (dev). Markers declared correctly for docker + slow. ✓ SOLID
5. **Makefile is complete**: `setup`, `verify`, `test`, `pdf`, `figures`, `data`, `clean`, `distclean`, `all`. Documented in help target. ✓ SOLID
6. **PEP 420 namespace-package binding** to AVE-Core per README.md:18-32 — `pip install -e ../AVE-Core` then `pip install -e .` integrates the constants source-of-truth. ✓ SOLID

### What needs attention

7. **`atopile build` path remains broken at KiCad layout-init**, per HANDOFF.md:43 TODO #2 (fp-lib-table missing). Both `default` (hopf_01) and `hopf_02a` builds parse + parts-pick + stop. Documented as "tooling-only concern, not blocking fab" since Python emitter is canonical. ⚠ ATTENTION — durable problem; recommend resolving when bandwidth allows or removing the atopile build entry to reduce confusion. ~1 session.
8. **Constants-gate has a known leak path** — `tests/verify_local_universe.py:18-36` MAGIC_NUMBERS whitelist includes `137.036` (1/α) but NOT the float `7.2973525693e-3` (α as fraction). The hard-coded `ALPHA = 7.2973525693e-3` in `scripts/hopf_02_nec2_run.py:88` evades detection. ⚠ ATTENTION
9. **`scripts/hopf_02_nec2_run.py:88` hard-codes ALPHA** instead of importing from `ave.core.constants`. Verified:
   ```
   scripts/hopf_02_nec2_run.py:88:ALPHA = 7.2973525693e-3    # CODATA 2018 fine-structure constant
   scripts/hopf_02_nec2_run.py:271:    return f_classical_mhz / (1.0 + handedness_sign * ALPHA * tf)
   ```
   All other HOPF-02 + HOPF-01 production scripts (verified 30+ files via grep) import from `ave.core.constants`. ⚠ ATTENTION — single deviation point; constants-gate decision in HANDOFF.md:74 says "all α, c, ε₀, μ₀, Z₀ values must come from `ave.core.constants`."

### Recommendations

- **(R2.1, 5 min)** Replace `scripts/hopf_02_nec2_run.py:88` with `from ave.core.constants import ALPHA`. Verify against published values (current hardcode = 7.2973525693e-3; CODATA 2022 in `ave.core.constants` may differ in last digits). If the numerical match is exact, this is purely a discipline fix. If it diverges, the predicted differentials (-7.92 / -11.91 / -55.29 MHz) may need to be re-computed and the canonical numbers in `project-hopf-02.md`, `exp-a1-hopf.md`, and the manuscript may need refresh.
- **(R2.2, 5 min)** Add `7.2973525693e-3: "Fine Structure Constant (CODATA fraction)"` to `tests/verify_local_universe.py:18-36` MAGIC_NUMBERS so future α hardcodes get caught.

---

## Axis 3 — Knowledge Base / Manuscript

### What's solid

1. **`manuscript/vol_hopf/` has exactly 14 chapters** plus `_manifest.tex` — verified via `ls manuscript/vol_hopf/chapters/`. Chapter ordering matches HANDOFF.md:30 claim (commits `2c287fa` scaffold + `0098480` edit pass + `5f3ccb7` namespace triage). ✓ SOLID
2. **Manuscript reconciliation backlog: all 7 R-items CLOSED** — verified via `docs/manuscript_reconciliation.md:12` status banner: "All 7 R-items below are now CLOSED via the 2026-05-05 T4 reconciliation pass (commit `3fa5c4f`), the 2026-05-06 deep-review edit pass (commit `0098480`), and the 2026-05-07 HOPF-02/03 namespace triage (commit `5f3ccb7`)." ✓ SOLID
3. **`docs/open_questions.md` reconciles with HANDOFF.md:53 summary**: Q1, Q3, Q5, Q6, Q11 CLOSED; Q7, Q8 DEFERRED to next bench; Q2, Q10 downgraded; Q4 (K4-lattice → n_AVE derivation) open + upstream-at-AVE-Core; Q9 deferred. HANDOFF claim of "5 of 11 closed, 4 genuinely open" verified — actual open are Q2 (downgraded historical-interest only), Q4 (upstream theoretical at AVE-Core, not blocking HOPF-02), Q9 (sweep window-clipping; resolved by HOPF-02 sweep protocol design), Q10 (downgraded historical). Only Q4 is a real-open item, and it does not block HOPF-02 — the enantiomer differential is parity-odd by construction. ✓ SOLID
4. **`docs/SESSION_STATE_2026-05-05.md` is a frozen reference snapshot** preserving the 2026-05-05 work-cutover (HOPF-01 modeling closed → HOPF-02 design opened). Multiple downstream cross-refs (including the sub-epic doc line 32 + 46 for 60-400× SNR margin) cite line 21 of this doc. ✓ SOLID
5. **`docs/concept_map.md`, `docs/glossary.md`, `docs/ave_crib_sheet.md`** are present per `AGENTS.md:5` First-Read protocol. Crib sheet is the AVE-foundations primer for HOPF-specific work. ✓ SOLID

### What needs attention

6. **`docs/ave_crib_sheet.md` retains 12 stale `Applied-Vacuum-Engineering/manuscript/...` archive refs** (per `BRANCH_STATE_2026-05-18_research-hopf-01-testing.md:51-53`). These have been broken since BEFORE the REPO-ARCH series began — the archive at `/Users/grantlindblom/AVE-staging/Applied-Vacuum-Engineering/` doesn't have a `manuscript/ave-kb/vol4/` directory. ⚠ ATTENTION — pre-existing technical debt, scoped as a separate cleanup workstream; not blocking A1-HOPF execution but should be on the list. ~1 session.
7. **No explicit cross-link in vol_hopf/chapters/ to the AVE-Core canonical leaves** that mirror this volume's content (`vol2/particle-physics/ch01-topological-matter/torus-knot-uniqueness.md`, `vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md`, `vol4/falsification/ch11-experimental-bench-falsification/project-hopf-02.md`). Cross-corpus cross-refs in the .tex chapters use prose only ("per AVE-Core Vol 4 Ch 1"), not file:line. ⚠ ATTENTION — F1/F2 cross-volume cross-ref format invariants from AVE-Core/manuscript/ave-kb/CLAUDE.md don't apply here (HOPF chapter is .tex not .md), but readability is degraded.

### Recommendations

- **(R3.1, ~1 session)** Sweep `docs/ave_crib_sheet.md` for the 12 stale Applied-Vacuum-Engineering refs (per BRANCH_STATE doc) and re-point to current homes (AVE-Core canonical leaves OR AVE-HOPF self-refs per IP-divide).
- **(R3.2, ~1 hour)** Add explicit file-path cross-refs in `vol_hopf/chapters/01_chiral_coupling_prediction.tex` and `_decision_gate.tex` to the canonical AVE-Core leaves (`torus-knot-uniqueness.md`, `torus-knot-ladder-baryons.md`, `project-hopf-02.md`). Per `AGENTS.md:79` "cite file path + line number with markdown links so the chain of reasoning is auditable."

---

## Axis 4 — Engine / Code

### What's solid

1. **Hardware design — KiCad PCB**: `hardware/hopf_02a.kicad_pcb` (62 KB) is the canonical fab artifact, emitted by `hardware/hopf_02_generate_kicad_pcb.py` (commit `c8c32bb` per HANDOFF.md:89). Per-board breakaway architecture eliminates the HOPF-01 multi-antenna coupling confound. ✓ SOLID
2. **Wire generator + mandrel CAD**: `scripts/hopf_02_build_drill_readback_wire.py` (canonical hole positions) + `scripts/hopf_02_build_mandrel.py` (3D-print mandrel emitter). 7 wire CSVs at `data/hopf_02/`; L↔R mirror at floating-point precision (~7×10⁻¹⁵ mm per HANDOFF.md:99). ✓ SOLID
3. **NEC2 prediction pipeline**: `scripts/hopf_02_nec2_run.py` → `data/calibration/hopf_02_predictions.csv` + `data/visualizations/hopf_02_predictions.png`. Predicted differentials −7.92 / −11.91 / −55.29 MHz at f_classical 380 / 680 / 2020 MHz for k25 / k23 / k35. ✓ SOLID (modulo the hardcoded-ALPHA gap in Axis 2)
4. **60-400× NEC2 SNR margin claim — VERIFIED** at source: `docs/design/2026-05-05_hopf02_nec2_prediction.md:97`: "Phase 1 detection is decisive at every (p,q) pair, with 60-400× margin over the limiting noise sources" — derived from VNA resolution (~100 kHz → 79× margin for smallest signal 7.92 MHz at (2,5)) and 5000-trial Monte Carlo manufacturing tolerance (~130 kHz → 61× margin smallest case). HANDOFF and sub-epic citation lineage is honest. ✓ SOLID
5. **89 tests passing — 44 are HOPF-02-specific** (`tests/test_hopf02_geometry.py`). Categories visible in the collect output: SMA convention (test_sma_positions_*), z-values, hole counts (TestE1HoleCountsVsDesignLog), L↔R mirror exactness (per HANDOFF.md:99 7×10⁻¹⁵ mm), alt-stitching pattern (TestE3AlternatingStitching), through-transit verification, BOM-vs-build script consistency (TestE2WireLengthsVsBom). ✓ SOLID
6. **Assembly + measurement protocol** at `hardware/hopf_02_ASSEMBLY_GUIDE.md` covers Phase A (panel fab) → Phase B (mandrel 3D-print) → Phase C (wire forming) → Phase D (stitching) → Phase E (snap-apart) → Phase F (VNA measurement) → Phase G (differential extraction) → Decision Gate. Pass criterion explicit at line 327: `|Δ| > 5σ_Δ` AND sign matches. ✓ SOLID
7. **scripts/ inventory: 47 Python scripts** — HOPF-01 lineage (40+), HOPF-02 lineage (3 production: build_drill_readback_wire, build_mandrel, nec2_run), HOPF-03 concept (1: hopf_03_spatial_refraction), water + Beltrami sidetrack (3). All HOPF-01 scripts retained for historical reference per HANDOFF policy. ✓ SOLID

### What needs attention

8. **Gerbers + drill files for HOPF-02a do NOT exist as built artifacts.** `hardware/Gerbers/` and `Gerbers 2/3.zip` all contain HOPF-01 Gerbers only (verified via `ls` and `unzip -l`). Per HANDOFF.md:42 TODO #1: Grant must run `kicad-cli pcb export gerbers hardware/hopf_02a.kicad_pcb --output gerbers/` and `kicad-cli pcb export drill hardware/hopf_02a.kicad_pcb --output gerbers/` before JLCPCB submission. 🔴 BLOCKING for fab — but this is a 5-minute fix.
9. **`scripts/hopf_02_nec2_run.py:88` constants violation** — see Axis 2 ⚠ #9. ⚠ ATTENTION.
10. **DRC report at `hardware/DRC.rpt`** (164 KB) is from the HOPF-01 design rule check (`Apr 13` mtime; pre-HOPF-02). HOPF-02a DRC has not been generated or saved. ⚠ ATTENTION — DRC should be re-run on `hopf_02a.kicad_pcb` and saved to `hardware/hopf_02a_DRC.rpt` before JLCPCB submission for ordering-defensible audit trail. 5-10 min.

### Recommendations

- **(R4.1, 5 min)** Run `kicad-cli pcb export gerbers hardware/hopf_02a.kicad_pcb --output hardware/Gerbers_hopf_02a/` (or equivalent path) and `kicad-cli pcb export drill ... --output hardware/Gerbers_hopf_02a/` to produce the HOPF-02a Gerber + drill set. Update sub-epic doc citation to point at the new directory. 🔴 BLOCKING for fab.
- **(R4.2, 5-10 min)** Run `kicad-cli pcb drc hardware/hopf_02a.kicad_pcb` and save output to `hardware/hopf_02a_DRC.rpt` for audit trail.
- **(R4.3, 5 min)** Fix `scripts/hopf_02_nec2_run.py:88` ALPHA import (R2.1).

---

## Axis 5 — Tie-in with AVE-Core

### What's solid

1. **AVE-Core canonical KB leaf `project-hopf-02.md` correctly mirrors AVE-HOPF state**: refreshed against FI-13 RESOLVED 2026-05-18 (line 34 `(p,q)` table), HOPF-02/03 namespace split (lines 12-20), 60-400× NEC2 SNR margin (line 40), $123/$278 BOMs (line 19), outcome A/B/C/D adjudication (lines 67-74), engineering substrate table (lines 78-89), and `Status (2026-05-20)` framing. ✓ SOLID
2. **`torus-knot-baryon-predictions.md` correctly carries FI-13 RESOLVED framing** (`(2,5)` proton cinquefoil per Borromean N=3 baryon; `(2,3)` is Clifford-torus phase-space winding for electron; lepton stays at `(2,3)` + climbs Cosserat torsion ladder). 6/6 PDG 2024 retrospective + 3/3 forward predictions hold. ✓ SOLID
3. **Constants imports in AVE-HOPF scripts use `ave.core.constants`** — verified via `grep -rn "from ave.core.constants" scripts/` returning 25+ correctly-imported scripts. The PEP 420 namespace-package binding works correctly. ✓ SOLID for all scripts except `hopf_02_nec2_run.py` (Axis 2 ⚠ #9).
4. **FI-13 (2,q) framing is aligned at audit time**: AVE-Core canon assigns (2,3) → electron trefoil (lepton family canonical), (2,5) → proton cinquefoil (baryon family canonical), (3,5) → higher-winding test mode. Sub-epic doc lines 26-30 + AVE-HOPF assembly guide line 134-139 are consistent with this canon. Lepton family stays at (2,3) + climbs Cosserat per `q-g27-muon-cosserat-saliency.md`. ✓ SOLID
5. **AVE-HOPF `manuscript/vol_hopf/chapters/13_l3_chirality_review.tex`** is identified by `docs/analysis/2026-05-06_manuscript_deep_review.md` as "the volume's strongest content and a model for any future critical-review chapters" — a built-in L3 cross-corpus audit chapter. ✓ SOLID
6. **No conflicting axiom-numbering claims surfaced.** AVE-Core uses Scheme A canonical (Substrate Topology / Topo-Kinematic Isomorphism / Minimum Reflection / Dielectric Saturation per `ave-kb/CLAUDE.md` INVARIANT-S2). AVE-HOPF references "Axiom 1" / "Axiom 2" in prose without conflicting derivation chains. ✓ SOLID

### What needs attention

7. **Phase 1 walk-back targets in `exp-a1-hopf.md` lines 54-57 may be stale claims.** The sub-epic doc lists `torus-knot-baryon-predictions.md` (2026-04-13) and `project-hopf-02.md` (2026-04-13) as "stale state — Phase 1 walk-back target." Verification at audit shows BOTH have been refreshed: `project-hopf-02.md` carries 2026-05-20 status line + AVE-HOPF cross-refs + FI-13 RESOLVED framing + namespace clarification; `torus-knot-baryon-predictions.md` carries 6/6 PDG 2024 anchor table + J^P column + forward c=17/19 confirmations + FI-13 RESOLVED particle identification. Both appear at-canon at audit time. ⚠ ATTENTION — Phase 1 walk-back may already be done; sub-epic doc should be updated to reflect, OR walk-back was scoped to additional content beyond what I verified. Flag for orchestration adjudication.

### Recommendations

- **(R5.1, 15 min)** Verify whether the Phase 1 walk-back of the two named leaves is actually complete (vs scoped to additional content not yet done). If complete, update `exp-a1-hopf.md` lines 50-57 to reflect "Phase 1 walk-back COMPLETE" rather than "Phase 1 will refresh these load-bearing leaves." Surface to orchestration for adjudication.

---

## Axis 6 — Gaps for A1-HOPF Execution

### Critical-path execution sequence (Phase 0 → Phase 2)

| Step | Status | Asset | Blocker? |
|---|---|---|---|
| 0a — KiCad design | ✓ DONE | `hardware/hopf_02a.kicad_pcb` (62 KB) | No |
| 0b — Export Gerbers | 🔴 NOT DONE | needs `kicad-cli pcb export gerbers ...` | **YES** |
| 0c — Export drill files | 🔴 NOT DONE | needs `kicad-cli pcb export drill ...` | **YES** |
| 0d — DRC report | ⚠ STALE | `hardware/DRC.rpt` is HOPF-01 only | Minor |
| 0e — JLCPCB ordering protocol | ⚠ HOPF-01 | `hardware/ORDERING.md` is HOPF-01-specific; no v-score spec for HOPF-02 | Yes |
| 0f — BOM ordered separately | ⚠ EMBEDDED | $123 BOM at `hopf_02_ASSEMBLY_GUIDE.md:21-32` not extractable as quick-ref | Minor |
| 0g — 3D-print mandrels (5x) | OPEN | `data/hopf_02_mandrels/` has SCAD source files; render to STL + print | No |
| 1 — Assembly | OPEN | Procedure ready at `hopf_02_ASSEMBLY_GUIDE.md` Phase C-D | No |
| 2a — VNA pre-reg | 🔴 NOT DONE | no `ave-prereg`-format pre-registration doc exists | Yes (Phase 2) |
| 2b — VNA measurement | OPEN | Procedure ready at `hopf_02_ASSEMBLY_GUIDE.md` Phase F | No |
| 2c — Differential extraction | OPEN | Procedure ready at `hopf_02_ASSEMBLY_GUIDE.md` Phase G | No |
| 3 — Outcome adjudication | OPEN | Pre-registered A/B/C/D grid at sub-epic doc lines 86-92 | No |

### What's solid

1. **Hardware design is execution-ready** — KiCad PCB validated, 89 tests passing including L↔R mirror exactness at fp epsilon. ✓ SOLID
2. **NEC2 prediction is precise and decisive** — 60-400× SNR margin verified at source. ✓ SOLID
3. **Procedure docs exist** for assembly + measurement + analysis (all in `hopf_02_ASSEMBLY_GUIDE.md`). ✓ SOLID
4. **Test equipment requirements are explicit**: LiteVNA-64 / NanoVNA-H4 / NanoVNA-V2 with ≥1.5 GHz range; RG316 SMA cable ≤1m; ferrite choke @ 1 GHz; 4× SOL calibration standards. Per `hopf_02_ASSEMBLY_GUIDE.md:257-261`. ✓ SOLID
5. **JLCPCB vendor identified** (`AGENTS.md` + `ORDERING.md`); 2-week typical fab turnaround. ✓ SOLID
6. **3D-print mandrels are deferred to Grant's printer + materials** — printable from SCAD/STL with PLA at ≤0.1mm layer height (FDM), SLA preferred for (3,5). 5 mandrels needed for HOPF-02a (control + k23_R + k23_L + k25_R + k25_L). ✓ SOLID

### What needs attention / blocking

7. **🔴 BLOCKING: Gerbers + drill files not exported from `hopf_02a.kicad_pcb`** — see Axis 4 ⚠ #8. 5-minute fix.
8. **🔴 BLOCKING: No HOPF-02a ORDERING.md with v-score spec** — current `hardware/ORDERING.md` is HOPF-01-specific (160×120mm, no v-score, 6 SMA). HOPF-02a needs v-score depth note (1/3 of board thickness ≈ 0.5 mm) for the 4 internal Edge.Cuts score lines per `hopf_02_ASSEMBLY_GUIDE.md:54-55`. ~15 min to draft. 🔴 BLOCKING for fab.
9. **🔴 BLOCKING for Phase 2: No `ave-prereg`-format pre-registration doc** for the VNA measurement. Sub-epic Phase 2 calls for one. Required before bench-fire. ~1 hour to draft using `ave-prereg` skill. Should land at `AVE-Core/research/2026-MM-DD_a1-hopf-hopf-02a-prereg.md` per `ave-handoff-canonical-locale` discipline. (Note: this is Phase 2 gate, not Phase 0 — fab can proceed without it.)
10. **⚠ HOPF-02a BOM not extractable as quick-ref file** — see Axis 1 ⚠ #8. Recommend `R1.1` rename/sub-directorize.

### Recommendations

- **(R6.1, 5 min)** Export HOPF-02a Gerbers via `kicad-cli`. 🔴 BLOCKING.
- **(R6.2, 15 min)** Draft `hardware/hopf_02a_ORDERING.md` with v-score spec + drill tolerance + correct dimensions (250×185mm panel). 🔴 BLOCKING.
- **(R6.3, ~1 hour, gated on R6.1)** Draft pre-reg per `ave-prereg` skill at `AVE-Core/research/2026-05-MM_a1-hopf-hopf-02a-prereg.md` covering: SNR threshold for adjudication (e.g., 5σ for PASS); freeze of NEC2-predicted differentials; freeze of Outcome A/B/C/D criteria; cable + ferrite + VNA serial documented; date-of-execution promise.

---

## Axis 7 — IP Audit (public theory vs private application)

### IP architecture state

| Asset | Visibility | Classification | Pointer pattern |
|---|---|---|---|
| AVE-HOPF repo | Private (LICENSE: "All rights reserved... Patents pending") | L2-L4 by construction | N/A |
| LICENSE | Tracked, restrictive | L3 — proprietary hardware + software | N/A |
| PATENTS.md | Tracked, placeholder | L4 — "Provisional Applications Filed" empty table | N/A |
| AVE-Core public KB | Public (PR org-wide) | L0-L1 only by `ave-ip-divide-discipline` | should use opaque `<!-- private-downstream: APP-XX -->` for AVE-HOPF refs |
| Cross-refs FROM Core TO HOPF | Explicit private paths (18 in sub-epic doc, 10+ in KB leaf) | Pointer-opacity VIOLATION per `ave-ip-divide-discipline` Step 4 Class F | should be opaque |
| `.ip-graph.yaml` | Does NOT exist | Missing graph maintenance | Should be created in private repo per skill Step 4 |
| Bidirectional pointers | None detected | Missing | Should add `<!-- ave-core-upstream: ... -->` in private chapters citing public theory |

### What's solid

1. **Repo visibility is correct**: AVE-HOPF private, AVE-Core public per `ave-ip-divide-discipline` Step 1. Verifiable via `gh api repos/.../<repo> --jq '.private'` (per skill instruction, not run here). LICENSE explicitly proprietary. ✓ SOLID
2. **Pure-AVE-corpus rule CLEAN** — sweep for "1517", "investor", "fund", "pitch", "interview" across all `.md`/`.tex`/`.py` files in AVE-HOPF returned ZERO hits. ✓ SOLID
3. **Patent posture is clean**: PATENTS.md is a placeholder with no specific applications yet; LICENSE clearly proprietary. No public disclosure that would imperil future patent-novelty. ✓ SOLID
4. **Public-vs-private content classification is intuitively correct**:
   - **PUBLIC THEORY (paper-worthy if Outcome A)**: `Δf/f = α · pq/(p+q)` formula, (2,q) torus-knot family classification, FI-13 RESOLVED particle ID, NEC2 ALPHA-post-processing methodology, enantiomer differential as parity-odd discriminator. All grounded in AVE-Core canonical leaves which are public.
   - **PRIVATE APPLICATION (IP/patent-foundational)**: HOPF-02a panel layout (per-board breakaway, SMA off-center scheme, specific dimensions), Python KiCad emitter implementation, wire generator algorithm for L↔R mirror exactness, 3D-print mandrel CAD, alt-stitching peg architecture, scored breakaway as mutual-coupling-elimination mechanism. All AVE-HOPF-internal.
   ✓ SOLID architecture; ⚠ MISSING in skill-procedure encoding.

### What needs attention

5. **No bidirectional cross-reference architecture** — neither `.ip-graph.yaml` nor opaque `APP-XX` pointers exist. Cross-refs from public AVE-Core to private AVE-HOPF use explicit private-repo paths (18 instances in `exp-a1-hopf.md` alone), which is the Class F failure mode in `ave-ip-divide-discipline` Step 4. ⚠ ATTENTION — but note: this is structurally same-problem as the broader AVE-Core REPO-ARCH-12 sweep state; not unique to A1-HOPF. Flag at orchestration-level for AVE-Core walk-back consideration.
6. **No HOPF-specific instantiation of `ave-ip-divide-discipline`** — the skill is abstract; AVE-HOPF doesn't yet have a per-repo runbook for IP-divide handling. ⚠ ATTENTION.
7. **`docs/ave_crib_sheet.md:121` + `:21` and `docs/glossary.md:32` ref AVE-Core's bracketed Golden Torus** as "post-IP-separation patch-attempt" — this is correctly historical-reference, but indicates AVE-HOPF inherits framing from AVE-Core's L3 audit trail. ⚠ ATTENTION — these refs are L0/L1-class (theory framing, no IP exposure); they're correctly referenced upstream rather than restated, which is the safe pattern.

### IP-protection framework for HOPF-02a outcome management

When HOPF-02a measurement lands, IP-divide management:

| Outcome | Public-disclosure scope | Private-protection scope |
|---|---|---|
| **A** (PASS at NEC2-class precision) | Paper-publishable: result table, methodology overview, AVE prediction match, statistical analysis. Use **methodology-level** language. | Hold private: specific PCBA design files, per-board panel layout, Python emitter, mandrel CAD, alt-stitching architecture, fab-vendor protocol. |
| **B** (partial — chirality detected, magnitude differs) | Paper-publishable: chirality exists at EE scale; magnitude analysis. Same methodology language. | Hold private: full hardware IP. |
| **C** (null — no Δf detected) | Paper-publishable: AVE (2,q) classification falsified at EE scale; methodology survives. | Hold private: full hardware IP (still patent-eligible if redesigned). |
| **D** (confound — multi-antenna re-emerges) | Discussion-level only: design caveat surfaced; full result deferred to HOPF-02b. | Hold private: PCBA design + diagnosis. |

The key IP-divide insight: the **measurement result + AVE physics framing is L1 (extractable to public theory)**; the **PCBA + mandrel + fab protocol is L3 (private hardware IP)**. Outcome A or C both have clean public-theory framings; the IP-protected hardware design is independent of which outcome happens.

### Recommendations

- **(R7.1, 30 min)** Draft a `AVE-HOPF/.ip-graph.yaml` with at least one APP-XX entry mapping `vol4/falsification/ch11-experimental-bench-falsification/project-hopf-02.md` ↔ AVE-HOPF's `manuscript/vol_hopf/chapters/01_chiral_coupling_prediction.tex`. Provides the bidirectional pairing baseline.
- **(R7.2, ~1 session)** Migrate the 18 explicit `AVE-HOPF/...` paths in `_orchestration/exp-a1-hopf.md` (currently in PUBLIC AVE-Core) to opaque `<!-- private-downstream: APP-XX -->` pointers. Same for `project-hopf-02.md` (10+ refs). Will likely require .ip-graph.yaml seed first.
- **(R7.3, on Outcome A)** Pre-draft a paper-publishable result template using L1 methodology-level language, scoped to extract from the bench result + AVE physics framing without leaking PCBA design IP.
- **(R7.4, deferred until measurement)** Coordinate provisional-patent filing with attorney AFTER positive measurement and BEFORE any public disclosure, per the PATENTS.md framework.

---

## Axis 8 — Promotion Workflow (HOPF → Core)

### Current state of promotion patterns

1. **HOPF → Core extraction has happened** for at least one round: AVE-Core REPO-ARCH-9 (commit `23fec97`) migrated public-grade HOPF-01 high-Q chiral antenna content from public AVE-Core to private AVE-HOPF per `ave-ip-divide-discipline` (per BRANCH_STATE doc line 28-29). The migration direction in REPO-ARCH-9 was public → private (extraction OUT of public KB), not HOPF → AVE-Core promotion. So the pattern is operationally reversed from typical promotion.
2. **The general theory destinations** (FI-13 framework, (2,q) classification, baryon ladder) live in AVE-Core canonical KB leaves; HOPF-02-specific application IP lives in AVE-HOPF. Cross-refs flow Public-Core ← Private-HOPF (private cites public upstream by file:line) and Public-Core → Private-HOPF (public points at private via explicit path, currently violating opacity).

### Engine-work candidates for promotion to Core

1. **NEC2 ALPHA-post-processing methodology** (`scripts/hopf_02_nec2_run.py` lines 245-330, the `α` post-processing routine on classical NEC2 baseline) — could generalize as `ave-aware NEC2 wrapper` per HANDOFF.md:44 deferred TODO #3. If extracted as `ave.regime_1_linear.nec2_wrapper` in AVE-Core (or similar), then any AVE-aware antenna prediction can reuse the post-processing pattern.
   - **Classification**: L1 (theory-supporting derivation, IP-strippable). The α-post-processing is general-physics methodology; specific application targets (which (p,q), which fixture) are L3.
   - **Promotion path**: Step 5 of `ave-ip-divide-discipline` (extraction procedure). Move the post-processing routine to `AVE-Core/src/ave/...`; AVE-HOPF imports it. ~1 session.
2. **Wire generator with L↔R mirror exactness** (`scripts/hopf_02_build_drill_readback_wire.py`) — the mirror-exactness algorithm is general-physics (parity-symmetric inputs require fp-precision mirror handling); the application target (HOPF-02a) is specific.
   - **Classification**: L1.
   - **Promotion path**: Likely defer — this is fairly application-specific in current form. Worth re-evaluating if a second AVE experiment needs L↔R wire-mirror handling.
3. **L↔R wire-CSV mirror-exact verification** (`tests/test_hopf02_geometry.py` mirror-exactness sub-tests, 44 tests) — could become a general AVE-corpus discipline test pattern.
   - **Classification**: L0 methodology (Foundation-Item-class testing discipline).
   - **Promotion path**: Document pattern in `ave-prereg` skill or new `ave-parity-exact-mirror-test` skill. ~30 min.

### What's solid

4. **The promotion direction is implicit but consistent**: public Core ↔ private HOPF via KB-leaf-only cross-refs from public side + explicit-file-path cross-refs from private side. ✓ SOLID architecture.
5. **AVE-Core canonical KB leaves are correctly the SOURCE of truth** for general theory (axioms, FI-13, (2,q) classification, baryon ladder PDG 2024 anchor); AVE-HOPF correctly defers to them rather than re-deriving. Per `AGENTS.md:107` "Authority rule for citations: AVE-Core for axioms / α / foundations." ✓ SOLID.

### What needs attention

6. **No documented promotion workflow exists** — no checklist, no `.ip-graph.yaml`, no runbook. Per Grant request: "Propose a workflow document or checklist for future promotion." ⚠ ATTENTION.
7. **No verify-before-cite v1.4 trigger 7c discipline applied yet** for the AVE-Core matrix claims about HOPF state. The matrix entry at `AVE-Core/manuscript/ave-kb/common/divergence-test-substrate-map.md` references HOPF-02a state — should be verified grounded in actual AVE-HOPF file:line refs, not stale via summary propagation. Quick spot-check: `project-hopf-02.md` cites `AVE-HOPF/.agents/HANDOFF.md`, `AVE-HOPF/docs/SESSION_STATE_2026-05-05.md:21`, `AVE-HOPF/hardware/TEST_PROCEDURE.md`, `AVE-HOPF/hardware/BOM.md` — 4 of these are at-canon, 2 (TEST_PROCEDURE + BOM) are misdirected to HOPF-01-pilot files (per Axis 1 ⚠ #8). ⚠ ATTENTION.

### Proposed promotion workflow checklist (draft for orchestration to refine)

Adapted from `ave-ip-divide-discipline` Step 5:

```
## AVE-HOPF → AVE-Core promotion checklist

Before promoting engine work from AVE-HOPF to AVE-Core:

1. **Classification check** — content classification per `ave-ip-divide-discipline` Step 2:
   - L0 (pure substrate physics, no application) — promote as-is
   - L1 (theory-supporting derivation, IP-strippable) — strip first, then promote
   - L2-L4 (application/IP-tied) — DO NOT promote

2. **Stripping check (L1 only)** — remove:
   - Mechanism names tied to commercial application (e.g., "HOPF-02 enantiomer")
   - Application targets (e.g., "for VNA fab")
   - Specific bench-design parameters (e.g., 50×185 mm board, 4 v-score lines)
   - Quantitative claims tied to commercial value (e.g., $123 BOM)

3. **Constants-source check** — verify the promoted code imports from `ave.core.constants`,
   not from hardcoded values. Per HANDOFF.md:74 constants-gate decision.

4. **Test promotion** — if tests are promoted alongside code, verify they pass
   via AVE-Core's `make verify` + `make test`, NOT just AVE-HOPF's.

5. **`.ip-graph.yaml` entry** — add an APP-XX entry mapping promoted public destination
   ← private origin. Track classification + extraction date.

6. **Public AVE-Core commit message** — note "extracted via ave-ip-divide-discipline"
   but DO NOT name private source repo.

7. **Private AVE-HOPF commit message** — note "general substrate-physics theory now
   lives at AVE-Core/<path>"; add `<!-- ave-core-upstream: ... -->` pointer in the
   private chapter.

8. **Cascade-impact check** — does the promoted content change any AVE-Core
   matrix rows (`divergence-test-substrate-map.md`) or canonical leaves
   (`vol*/...md`)? If yes, run walk-back per `ave-walk-back` skill.

9. **Sub-epic update** — if the promotion concerns a tracked sub-epic
   (like `exp-a1-hopf.md`), update the sub-epic doc to reflect new
   public location.

10. **Bidirectional verification** — run `ave-ip-verify-pairing` after the
    promotion to confirm graph integrity.
```

### Recommendations

- **(R8.1, ~1 hour)** Land the promotion-workflow checklist above as `AVE-Core/_orchestration/promotion-workflow-template.md` (or wherever orchestration deems canonical). Orchestration session adjudicates final form.
- **(R8.2, ~30 min)** Apply `verify-before-cite v1.4` trigger 7c to all AVE-Core claims about AVE-HOPF state. Specifically: re-verify the cross-references in `project-hopf-02.md` lines 78-89 (engineering substrate table); some refs (BOM.md, TEST_PROCEDURE.md) are misdirected per this audit.

---

## Severity tally

**Across 8 axes**: 37 findings total

- ✓ **SOLID**: 23 (62%)
- ⚠ **ATTENTION**: 11 (30%)
- 🔴 **BLOCKING for A1-HOPF execution**: 3 (8%)

### Distribution by axis

| Axis | ✓ SOLID | ⚠ ATTENTION | 🔴 BLOCKING |
|---|---|---|---|
| 1. Repo Structure | 6 | 3 | 0 |
| 2. Tooling | 6 | 3 | 0 |
| 3. KB / Manuscript | 5 | 2 | 0 |
| 4. Engine / Code | 7 | 2 | 1 (Gerbers) |
| 5. AVE-Core Tie-in | 6 | 1 | 0 |
| 6. A1-HOPF Execution | 6 | 1 | 3 (Gerbers, ORDERING, pre-reg) |
| 7. IP Audit | 4 | 3 | 0 |
| 8. Promotion Workflow | 2 | 2 | 0 |

Note: BLOCKING items are counted once each across axes; the "3 BLOCKING" overall is { Gerbers export, HOPF-02a ORDERING.md, Phase 2 pre-reg }.

---

## Recommendations (prioritized)

### Top 3 BLOCKERS (must close before A1-HOPF execution)

1. **🔴 BLOCKER-1: Export HOPF-02a Gerbers + drill files from `hardware/hopf_02a.kicad_pcb`.** Currently `hardware/Gerbers/` contains HOPF-01 Gerbers only; HOPF-02a equivalents do not exist as built artifacts. **5-minute fix** via `kicad-cli pcb export gerbers ...` + `... export drill ...`. Should land at `hardware/Gerbers_hopf_02a/` (or sub-directorized scheme per R1.1). Per HANDOFF.md:42 TODO #1 — Grant action.

2. **🔴 BLOCKER-2: Draft `hardware/hopf_02a_ORDERING.md` with v-score spec.** Current `hardware/ORDERING.md` is HOPF-01-specific (160×120mm, 6 SMA, no v-score). HOPF-02a needs v-score depth note (1/3 board thickness ≈ 0.5 mm) for the 4 internal Edge.Cuts score lines; correct panel dimensions (250×185 mm with 5 sub-boards); correct drill tolerance (±0.1 mm). **15-minute fix** drafting from `hopf_02_ASSEMBLY_GUIDE.md:36-77`.

3. **🔴 BLOCKER-3 (Phase 2 gate only): Draft `ave-prereg`-format pre-registration** for the HOPF-02a VNA measurement. Should land at `AVE-Core/research/2026-MM-DD_a1-hopf-hopf-02a-prereg.md` per `ave-handoff-canonical-locale` discipline. Includes: SNR threshold (5σ for PASS), frozen Outcome A/B/C/D criteria, cable/ferrite/VNA serial documentation, date-of-execution commit. **~1 hour to draft.** Note: NOT blocking for Phase 0 fab — only blocks Phase 2 bench-fire.

### Top 5 ATTENTION items (close before or during Phase 0)

4. **⚠ ATTN-1: Fix `scripts/hopf_02_nec2_run.py:88` hard-coded ALPHA.** Replace with `from ave.core.constants import ALPHA`. Verify numerical match against CODATA in `ave.core.constants`; if divergent, refresh downstream prediction numbers (−7.92 / −11.91 / −55.29 MHz). **5 min fix + verification.** (R2.1)

5. **⚠ ATTN-2: Reorganize `hardware/` directory** so HOPF-01 and HOPF-02a artifacts are unambiguously addressable. Recommend explicit `hopf_02a_*` prefix scheme. Closes the citation-mismatch root cause for sub-epic doc + AVE-Core KB leaf. **30 min effort.** (R1.1)

6. **⚠ ATTN-3: Migrate explicit private-path refs in PUBLIC AVE-Core** (`exp-a1-hopf.md` 18 refs, `project-hopf-02.md` 10+ refs) to opaque `<!-- private-downstream: APP-XX -->` pointers per `ave-ip-divide-discipline` Step 4 Class F. Requires `.ip-graph.yaml` seed first. **~1 session.** (R7.1 + R7.2) — Note: this is a corpus-wide pattern; surface to orchestration for cross-repo walk-back consideration.

7. **⚠ ATTN-4: Audit and verify Phase 1 walk-back state.** Sub-epic doc lines 50-57 claim `torus-knot-baryon-predictions.md` + `project-hopf-02.md` are "stale, Phase 1 walk-back targets" — but audit verification shows both at-canon. Either walk-back is COMPLETE (update sub-epic), or walk-back scope was broader than verified content. **15 min to resolve.** (R5.1)

8. **⚠ ATTN-5: Add MAGIC_NUMBER `7.2973525693e-3` to `tests/verify_local_universe.py`** so future α hardcodes get caught by the constants-gate. **5 min fix.** (R2.2)

### Top 3 NICE-TO-HAVE improvements

9. **NTH-1: Land promotion-workflow checklist** at `AVE-Core/_orchestration/promotion-workflow-template.md` (or canonical location per orchestration). Captures the discipline for future HOPF → Core engine extractions (NEC2 wrapper, L↔R mirror tests, etc.). **~1 hour to draft from R8.1 template above.**

10. **NTH-2: Sweep `docs/ave_crib_sheet.md` 12 stale Applied-Vacuum-Engineering refs** per BRANCH_STATE_2026-05-18 line 51-53 pre-existing technical debt. ~1 session.

11. **NTH-3: Add explicit AVE-Core cross-refs in `vol_hopf/chapters/01_chiral_coupling_prediction.tex`** for the canonical leaves (torus-knot-uniqueness, torus-knot-ladder-baryons, project-hopf-02). Per `AGENTS.md:79`. **~1 hour.**

---

## Next Phase Triggers

Items landing in this audit that trigger immediate Phase 0 actions in the sub-epic:

1. **`exp-a1-hopf.md` Phase 0 gate is more granular than the doc currently reflects.** Phase 0 = { (a) export Gerbers, (b) draft HOPF-02a ORDERING.md, (c) submit to JLCPCB }. Currently the doc has all three under "Grant submits HOPF-02a Gerbers to JLCPCB" (line 62). Recommend splitting into sub-phases for tracking — Phase 0a (artifact-generation, BLOCKER-1 + BLOCKER-2), Phase 0b (fab-submission).

2. **`exp-a1-hopf.md` lines 50-57 Phase 1 walk-back section may be obsolete** per Axis 5 ⚠ #7 — both named target leaves verify at-canon at audit. Recommend orchestration adjudicates whether Phase 1 walk-back is COMPLETE (and updates sub-epic) or whether the walk-back scope was broader than the verified content.

3. **Engineering substrate table in `project-hopf-02.md` lines 78-89 has 2 misdirected refs** — `BOM.md` and `TEST_PROCEDURE.md` resolve to HOPF-01 files, not HOPF-02a. Walk-back trigger for AVE-Core public canonical leaf. Recommend orchestration adjudicates fix path (either via `R1.1` HOPF-HOPF re-org which auto-resolves, OR direct walk-back of the KB leaf).

4. **Promotion-workflow checklist trigger** — once R8.1 lands, the next HOPF → Core engine extraction (most likely the NEC2 ALPHA-post-processing wrapper per HANDOFF.md:44) can use it as the protocol document.

5. **IP-divide bidirectional graph seed** — once R7.1 lands `.ip-graph.yaml`, subsequent AVE-Core leaves that reference AVE-HOPF can use opaque APP-XX pointers per `ave-ip-divide-discipline` Step 4. Forward-direction: any new cross-corpus content lands with correct opacity from day 0.

---

## Walk-back targets flagged for AVE-Core (orchestration adjudication required)

Per scope constraint ("If you find a stale matrix row or KB leaf in AVE-Core that needs walk-back, FLAG it in the audit doc"):

1. **`_orchestration/exp-a1-hopf.md:32, :46, :70, :85` + `:139-141`** — citations of `AVE-HOPF/hardware/BOM.md`, `TEST_PROCEDURE.md`, `assembly_guide/`, `Gerbers/`. All four destinations are HOPF-01-pilot artifacts. Walk-back required to either (a) re-point at HOPF-02a-specific files (which currently don't all exist as separate documents), OR (b) gated on AVE-HOPF reorganization per R1.1. Flag — orchestration adjudicates whether walk-back is pre- or post- AVE-HOPF reorganization.

2. **`manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-hopf-02.md:82, :84, :85`** — citations of `AVE-HOPF/hardware/BOM.md`, `TEST_PROCEDURE.md`, `assembly_guide/`. Same root cause as #1; same walk-back gate. Flag.

3. **`_orchestration/exp-a1-hopf.md:50-57` Phase 1 walk-back section** — claims `torus-knot-baryon-predictions.md` + `project-hopf-02.md` are stale Phase 1 walk-back targets, but audit verification at AVE-Core HEAD `6621dae` shows both at-canon (refreshed against PDG 2024 + FI-13 RESOLVED). Flag — orchestration adjudicates whether Phase 1 walk-back is COMPLETE (update sub-epic Phase 1 to ✓ DONE) or whether walk-back scope encompasses additional content.

4. **Pointer-opacity violations in PUBLIC AVE-Core** — 18 explicit `AVE-HOPF/...` paths in `_orchestration/exp-a1-hopf.md`, 10+ in `project-hopf-02.md`. Per `ave-ip-divide-discipline` Step 4 Class F, these should use opaque `<!-- private-downstream: APP-XX -->` pointers. Flag — orchestration adjudicates whether this is sub-epic-level or corpus-wide IP-divide walk-back priority.

---

## Audit trail

- 2026-05-20 — Audit landed. Read-only sweep of AVE-HOPF on `research/hopf-01-testing` @ `cfc5a40` from AVE-Core orchestration session on `analysis/integration` @ `6621dae`. Verified 89 fast tests passing via live `pytest` (89 passed, 14 docker-skipped, 103 collected). 4 walk-back targets flagged for AVE-Core orchestration adjudication. 3 BLOCKING items + 11 ATTENTION + 23 SOLID across 8 audit axes.

# Electron-Existence Keystone Arc — Derivation Audit Index

**2026-06-16 · the single auditor-facing map of the eigenmode / electron-existence arc.**

The full narrative is the orchestration tracker [`_orchestration/2026-06-15_passive-eigenmode-solve.md`](../_orchestration/2026-06-15_passive-eigenmode-solve.md) (Phases 0–15 + §9/§9.1 pre-regs, §11 EE-diagnostic program, §12 toolkit audit). This index is the navigable map: each derivation → prereg → result-doc → JSON → branch → verdict → status. Built from the documentation-completeness audit (workflow `w0optx9ae`).

**Audit-reconstructable status: COMPLETE (from leaves), 2026-06-16.** Backup gaps CLOSED (all arc branches on origin; the frozen discrimination prereg tracked in `research/`). **All stale-leaf corrections LANDED** (Stage-1.5(c) `2a83808c`, C′ re-bin `6f4da77c`, driver NEGATIVE-A `7d1341ac`, all Rule-12 — headers added, original text preserved) **and both gate-step result MDs written** (Stage-1.6 `d61e6530`, Stage-1 `55d27c04`). A corpus-grep reader now hits the *corrected* verdict on every leaf. Remaining (non-blocking, separate PR): the §11 EE-sweep + §12 toolkit-audit + dimensional-analysis still live only in the tracker — they land in `ave-analytical-toolkit-index.md` via the queued toolkit-index PR.

## Branches (all on origin 2026-06-16; NONE merged to `main`)

| Branch | Carries | Tip |
|---|---|---|
| `…-passive-eigenmode-solve` | orchestration tracker (Phases 0–15) + G0 result + FROZEN passive prereg + the tracked discrimination prereg + this index | `808b8320`+ |
| `…-eigenmode-heldbc` | Option C + C′ (`held_helicity_winding.py`, C′ result, JSONs) | `d79fbcbb` |
| `…-boundary-mqj-selftrap-integrator-zwall` | Stage-1 gate (driver, result, JSON, `boundary_invariants`) | `e0d240e7` |
| `…-boundary-mqj-stage15-alphafree-emergence` | Stage-1.5 (prereg, engine, 3 layer drivers+JSONs, combined result) | `be459b7e` |
| `…-boundary-mqj-stage16-moving-wall-sectorB` | Stage-1.6 (prereg, driver, JSON, 5 figs; **NO result MD — 500-killed**) | `a233f9ed` |
| `…-stage16-rerun-amendments` | the #273 pre-flight amendments (in-flight) | `a5a34f7c`+ |
| `…-engine-rerun-preflight-handoff` | #273 pre-flight brief | `f948f9d9` |

## Derivation matrix

| Derivation | prereg | result-doc | JSON | branch | verdict | status |
|---|---|---|---|---|---|---|
| G0 double-count-clean | passive FROZEN §5 (embedded) | `…_g0-double-count-clean_result.md` | — (smoke-gate) | passive-solve | double-count clean | ✅ complete |
| Passive-eigenmode FROZEN prereg | (is the prereg) | — | — | heldbc | master gate | ✅ complete |
| **Discrimination prereg** (α-free emergence gate) | (is the prereg) | — | — | passive-solve (`research/`, now tracked) | the frozen success criterion both Stage-1.5+1.6 gate on | ✅ complete |
| Stage-1 gate: c_eff(V)-STRUCTURAL-GAP | `…ceff-epsilon-monotonicity_prereg_FROZEN.md` | `…ceff-epsilon-monotonicity_result.md` + ✅ **`2026-06-16_stage1-gate-boundary-mqj_result.md`** (`55d27c04`, carries the 4 corrections + 11.9P) | `boundary_mqj_selftrap_zwall_gate_results.json` | zwall | bucket-2, NOT echo | ✅ complete (gate-step MD written, Q2) |
| Option C DISQUALIFY (56× pump) | passive FROZEN | (inside C′ doc) | — | heldbc | DISQUALIFY | ✅ (superseded into C′) |
| Option C′ NEGATIVE | passive FROZEN | `…cprime_helicity-hold_result.md` | `passive_eigenmode_cprime_helicity_N26.json` | heldbc | re-binned DISQUALIFY-WRONG-OBJECT → scalar-route CLOSED-NEGATIVE; cohabitation UNTESTED | ✅ **re-bin LANDED** `6f4da77c` (Rule-12 header + JSON `C_reading_rule12_correction`) |
| Stage-1.5 layer-a (A1 self-trap) | `…stage15…-prereg.md` *(body FROZEN; filename lacks `_FROZEN`)* | `…stage15…_result.md` (combined) | `stage15_layer_a…_results.json` | stage15 | PASS (Z_tank→0.376) | ✅ complete |
| Stage-1.5 layer-b (coupled stability) | (shared stage15) | (combined) | `stage15_layer_b…_results.json` | stage15 | STABLE | ✅ complete |
| Stage-1.5 layer-c (emergence probe) | (shared stage15) | (combined) | `stage15_layer_c…_results.json` | stage15 + amendments | Phase-14 OVERTURNED (grid-registration artifact) → loop-closure UNTESTED | ✅ **RETRACTION LANDED** `2a83808c` (Rule-12 header, body preserved) on the amendments branch |
| Stage-1.6 moving-wall (Sector B) | `…stage16…-prereg.md` (FROZEN) | ✅ **`2026-06-16_stage16-moving-wall-sectorB_result.md`** (`d61e6530`) | `stage16_moving_wall_sectorB_results.json` + 5 figs | stage16 | WALL-CONFINES-BUT-LOOP-INERT → grid-registration artifact (vacuous on loop-closure) | ✅ result MD written (Q2) |
| Boundary M/Q/J reframe | — (KB doc) | `manuscript/ave-kb/common/boundary-observables-m-q-j.md` | — | zwall (KB) | 𝓠=linking / 𝓙=winding | ⚠️ arc-application narrative tracker-only |
| Dimensional analysis (M/J/Q spine) | — | — (tracker §refs only) | — | — | α⁻¹=𝓜+𝓙+𝓠 (Class-B) | ⚠️ no committed artifact |
| Toolkit audit | — | — (tracker §12) | — | — | reflexes-not-discipline; 6 missed tools | ⚠️ tracker-only |
| EE diagnostic + sweep matrix | — | — (tracker §11) | — | — | sweep program | ⚠️ queued PR to `ave-analytical-toolkit-index.md`, not landed |

## ✅ STALE LEAVES — ALL CORRECTED (2026-06-16, Rule-12: headers added, original verdict text preserved)

A corpus reader grepping these committed leaves now hits the *corrected* verdict, not the superseded one:
1. ✅ **Stage-1.5(c)** (`2a83808c`, stage15/amendments): Rule-12 retraction header on `…stage15…_result.md:18,85`, re-scoped to "loop-closure UNTESTED (Cartesian-stencil artifact zeroed the coupling)." The load-bearing one.
2. ✅ **C′** (`6f4da77c`, heldbc): Rule-12 demotion header (top + §5 verdict) re-scoping "NEGATIVE (earned)" → "scalar-route CLOSED-NEGATIVE; sector-cohabitation UNTESTED"; JSON sibling field `C_reading_rule12_correction`.
3. ✅ **Driver NEGATIVE-A** (`7d1341ac`, heldbc): Rule-12 correction header — mis-binned per `w92ft1gkc` (F1+F2 PASS = breather exists, §4 dispersion criterion not met) AND superseded at Phase-8.

## Non-obvious filings (auditor notes)

- **G0** has no separate prereg — embedded in the FROZEN passive prereg §5 (by design).
- **Stage-1**'s result is filed under `ceff-epsilon-monotonicity_result.md` (the INVARIANT-S2 lane name) — grepping "stage1" for it fails.
- **Stage-1.5** prereg filename lacks the `_FROZEN` suffix the other frozen preregs use; the body IS Rule-11 frozen (line 3).
- **Verify-panel verdicts (10 panels)** are distilled in the tracker phase log with workflow ID + verdict + file:line evidence; the raw workflow outputs are ephemeral (`/tmp`). When each result doc lands, fold its deciding panel's verdict + numbers into the doc's status header (the C′/driver docs already do this — replicate).
- **Provenance**: the earlier phantom-hash slips (`aebbc99dbd` = agent-id not a commit; `230579b6` = a tracker commit mis-cited as the engine) are corrected — engine builds are `a233f9ed` (Stage-1.6) / `be459b7e` (Stage-1.5).

## Open documentation actions (owners)

- 🔴 The 3 stale-leaf corrections (above) — amendments-implementer + 2 branch edits.
- 🔴 Stage-1.6 result MD — `research/2026-06-16_stage16-moving-wall-sectorB_result.md` (the natural committed home for the grid-registration diagnostic that drives the Stage-1.5(c) overturn).
- §11 EE-sweep + §12 toolkit-audit → land in `ave-analytical-toolkit-index.md` via branch+PR.
- This index rides to whichever branch becomes the integration target.

## Grant-gate (merge)

Do NOT merge any arc branch into `main` until the 3 stale-leaf corrections land on their branches AND the Stage-1.6 result MD exists. Two open questions for Grant: **(Q1)** land all 3 header corrections before merge, vs. tracker-is-authoritative + branch-docs-are-scratch? **(Q2)** is JSON+tracker the intended durable record for gate-class steps, or do Stage-1 / Stage-1.6 each get a result MD?

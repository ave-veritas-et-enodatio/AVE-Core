# P1 Lint-Sweep Findings — consolidated lane tables (HEAD `2a7d01dc`, 2026-07-04)

**Status:** CLOSED — last-verified 2026-07-04 (owner: orchestration-session). P1 ran as four parallel read-only auditor lanes; this doc banks their disposition tables as the durable record. Adjudication surface: [`2026-07-04_p2-adjudication-batch.md`](2026-07-04_p2-adjudication-batch.md). Nothing here executed anything.

**P3 currency note:** every line number below was verified at `2a7d01dc`. Line-drift accrues continuously; P3 implementors re-verify each target at their own HEAD before editing (the tables tell them where to look and what class of fix applies, not final byte offsets).

**Lane methodology (all four):** two-method extraction with reconciled counts on every completeness claim; flag-don't-fix; honesty-trail rows marked exempt; sober classifications. Live catch this epic: three separate single-method greps false-negatived (§D2 family rows; the `_orchestration` subdir scope gap; the Part-1 citer loop word-splitting) — each caught by the second method.

## §A — Lane (a): citation-currency

**Headline: 0 DEAD citations corpus-wide.** Verified: 477 pairs fully + 150 sampled. Drift is line-number-only in all but one case.

**T1 — forward-prediction register (12 cites):** 1 CURRENT, 11 LINE-DRIFT. Register provenance was accurate at its pinned HEAD `dc9e1791` (verified via `git show` at that commit); stale-by-construction since. Key remaps at `2a7d01dc`: `vol4/claim-quality.md:389→417` (clm-pp3qwf), `:399→433/447/460` (7.5/α³ ratio — surrounding derivation REWRITTEN 2026-07-03 KEEP-BOTH split, value preserved), `constants.py:460→472` (V_YIELD), `claim-quality.md:437→486` (clm-k4d4ph), `:448→496`, `:449→497`, `vocabulary-register.md:545→581` (def-0pt1ac), `:551→587` (ETA decree). `chiral_lattice_vector.py:27,93` CURRENT.

**T2 — corpus `.py:NNN` cites:** 2067 instances (KB 275 / orch-top 220 / research 1572; both methods exact). KB+orch fully verified → 425 unique pairs: **152 CURRENT · 205 LINE-DRIFT · 1 CONTENT-CHANGED · 43 unresolved-by-scope (25 cross-repo AVE-Protein hand-off cites + 18 non-src tools) · rest prose/heuristic-resolved.** Research tier sampled 110/1333 pairs: same class mix (49 CURRENT / 37 LINE-DRIFT / 0 DEAD). Heavy-drift drivers: `constants.py` (930c5964 re-key; +15…+180), `cosserat_field_3d.py` (1550→2426 lines; `_reflection_density` 266→441, `extract_crossing_count` 1468→2336, `total_energy` 935→1462, `_energy_density_saturated` 545→712), `k4_tlm.py`, `test_l0_axioms.py`/`test_l3_mass_cage.py` (vol9/claim-quality ×5, +16…+27).

**The one CONTENT-CHANGED (P3 repair-with-care):** `manuscript/ave-kb/common/engine-capability-map.md:195` cites the Q≈30.8 cold-cage clean-negative at `crystal_engine.py:154` — at HEAD that line is `_laplacian` and the 30.8/cold-cage content is absent from the whole file; it lives in `graded_vacuum_network.py:13`, `vacuum_varactor_scatter.py:269+`, `test_l3_mass_cage.py`. P3 verifies the canonical host before repointing (the cite anchors the load-bearing α-negative instrument).

**T3 — `.md`/`.tex` cite drift-rate (40-cite stratified sample of 4184):** 25 CURRENT / 13 LINE-DRIFT (all small) / 0 DEAD / 2 shorthand-elision (dateless shorthand resolving fine). Rate by age: pre-Jun 54% → Jun 31% → Jul 17%; blended ~35-45%, all LINE-DRIFT class.

**Anomalies:** A1 cross-repo `src/ave_protein/...` cites in `2026-06-22_vol5-ave-protein-solver-handoff.md` (25; documented hand-off, P4 linter needs exemption). A3 FPR provenance header globally stale (quantified; queued item). A4 two T3 cites point INTO preserved Rule-12 bodies — CURRENT, marked honesty-trail-context. A5 20 heuristic-flagged KB/orch pairs all resolved prose-current/LINE-DRIFT on hand-check (cheap full exhaustion optional in P3).

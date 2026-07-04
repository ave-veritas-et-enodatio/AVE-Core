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

## §B — Lane (b): stale-marker sweep

**Baseline for the P4 warn-mode linter: 181 marker lines** (`RUNNING|PENDING|IN-FLIGHT|MID-FLIGHT`, word-boundary, `_orchestration/**` 130 + `research/**` 51, excl `_archive`; two methods exact, symmetric-diff empty). Classes: COMPLIANT 3 · FENCED-OR-EXAMPLE 21 · PROSE-FALSE-POSITIVE 30 (incl. 14 hyphen-compounds — the §5 amendment) · **RECONCILE-DEAD 27** · **ADD-ATTRIB 89** · UNCLEAR 11 (→7 after the stage16 git-check; →0 on the loop-gap ruling).

**RECONCILE-DEAD (27) — P3 lands dated terminal-state notes; evidence verified per row:**

| Site | Evidence |
|---|---|
| `2026-06-02_alpha-class2-lift…md:178,:200,:306,:313` (4) | doc's own §8/§10 CLOSED verdicts; branches gone; `audit/2026-06-02_alpha-lift-*` ×4 on origin; relabel merged (#76/#229) |
| `2026-06-10_genesis-session-workflow-ledger.md` rows `:29,:31,:33,:34,:35,:36,:38,:42` (8) | branches gone + matching `audit/2026-06-11_*` tags (s11-de-novo, dark-sector, bubble-physics, fbd-v2, genesis-v8…); index.md:252 "20 audit tags pushed, implementor branches deleted". **Recommended fix = ONE dated CLOSED header (P2 §4)** |
| `2026-06-09_ion-compression-rectifier-arc.md:149,:171` (2) | `:171` Rule-12 append narrates the landed verdict; PR #144 merged |
| `2026-06-06_session-handoff.md:14` (1) | superseded by 06-07 epic + 06-09 handoff; arc closed |
| `2026-06-09_SESSION-HANDOFF.md:21,:23,:54,:100` (4) | `:54` self-annotates "~~(RUNNING)~~ — RESOLVED 2026-06-10"; Rule-12 appends record landings |
| `2026-06-07_electron-synthesis-epic.md:158` (1) | G2 thread resolved 2026-07-03 (`:320` append) |
| `2026-06-23_lattice-discovery-program.md:45,:48` + `index.md:67` (3) | PR #391 + #392 MERGED 2026-06-24 (`:67` RE-RUNNING row = the landed re-run) |
| `research/2026-06-10_quarter-fence-verdict_note.md:80` (1) | PR #164 MERGED 2026-06-10 |
| `research/2026-05-26_clm-ldmvwi…prereg.md:145` (1) | one-shot "(this commit)" registration marker, historical |
| `research/2026-05-19_c5-pantheon…:254` + `research/2026-06-20_mass-sector…:25,:42,:169` (4) | lines narrate completed PENDING→CLOSED/RESOLVED-ECHO transitions (prior-state quotes) |

**ADD-ATTRIB (89) — live markers needing `(owner: <name>, DATE)` backfill.** Concentrations: experimental benches (`exp-c15-cleave-01` 7, `exp-c11-mach-zehnder` 5, `experimental-arc` 4, `a1-hopf` 2), `clm-0ktpcn-golden-torus` tracker 8, loop-gap first-principles brief 7 (ruling-dependent), `2026-05-28_parameter-count-framing-walkback` 5, biquaternion Phase-2 doc 4, `index.md` 4 (incl. the **stage16 MERGE-PENDING at `:160` — CONFIRMED genuinely live: `54fa23cd` not in main ancestry, branch on origin; cross-links to P2 §1 row 2b**), electron-device-datasheet_draft 6, genesis-program-status 3, chiral-srs-OA result 4, + long tail. Full per-line dump preserved in the P1 lane transcript.

**UNCLEAR (7 pending P2 §4 loop-gap ruling):** v11 charter ×4, v12 ×1, v15 ×4→(some rows may already be closed per the LIVE LEDGER — P3 cross-checks per-row), unified-harness ×2, + genesis-ledger unverified-scout rows ×3 (chiral-angle-of-attack has a live resumable branch; two scouts unresolvable).

**P4 linter-precision inputs:** fence/example-skip must subtract exactly 21 (incl. the conventions doc's own §(e) block + epic-brief paraphrase — else the linter self-flags every run); compound-token handling per P2 §5; `DEAD-MID-FLIGHT` is terminal not live; physics term "RUNNING COUPLING" (`electron-coverage-matrix.md:111`) is a known false-positive shape.

## §C — Lane (c): figure/artifact placement + orphans

**Part 1 — the 79 tracked script-output files:** CITED-FIGURE 27 · CITED-DATA 38 · UNCITED-SCRATCH 14. Basename grep is the load-bearing citer method (docs cite `_output/foo.json` relative forms; full-path grep systematically under-counts). `.py` driver path-refs are NOT citations (policy).

**CITED-FIGURE → per-volume `figures/` (27).** Vol_1: `chiral_orbital_holonomy.png`, `secondshell_screw_holonomy.png`, `two_node_alpha_projection.png` (→ `vol_1_foundations/figures/`); `window_blind_two_threes.png` → `ave-kb/common/figures/` (common citer). Vol_4: `vvs_fig_{a,b,c,d}*.png` ×4, `optical_caustic_resolution.png`, + the 6 `cvr_ee_sweep/_output/fig{1..6}*.png` (vol4 KB citers) → `vol_4_engineering/figures/`. Vol_9: 11 files (`a1_spatial_cavity_mode_fft`, `electron_s11_{gate,unknown}`, `s11_denovo_{gate,made,paired,planted}`, `two_natured_electron_native_engine`, 3× `vacuum_birefringence_facility_sweep_*`) → `vol_9_vacuum_datasheet/figures/`. SPECIAL: `carbon_strain.png` — do-not-place walk-back citer only (P2 §2); die-by-allowlist-removal. Allowlist lines dying with the migration: `.gitignore:65-94` block (25 migration + 1 removal); `:95-101` are `src/tests/outputs` (out of scope, part of the stale "38" arithmetic — HEAD-true allowlist figure lines = 37). Wildcard citer `engine-capability-map.md:320` (`_output/*.png`) needs pattern-rewrite-or-reword (P2 §5). Tex-side: `vol_9 main.tex:7` graphicspath includes the cvr `_output/` path — dies on move; KB citers use deep relative image paths — all rewritten in the move commits.

**CITED-DATA → per-volume `results/` (38, ratified Option 1).** Vol_1 ×20 (D1-D20: alpha-identity/coax-ring ×2 (Rule-12-addendum citers)/cosserat-band/α-leak ×2/genesis ×3/mfg-rr/g2-eigvec★/native-model ×2 (one emf-lenz sign-correction citer)/propagation/γ-ceiling/screw-holonomy/two-node/unified ×2) → `vol_1_foundations/results/` EXCEPT ★`g2_photon_eigvec_composition.json` → `ave-kb/common/results/` (cross-vol: common+vol1; honesty-trail citer = g2-relabel note). Vol_4 ×7 (cavitation/k4-bloch/sonic-horizon/spice-cvr/spice-lane `.cir`+`.json`/srs-bloch) → `vol_4_engineering/results/`. Vol_9 ×10 (birefringence ×3 incl. hibef-predictions/electron-s11/im3/node ×2/oq1/per-dof/s11-denovo — note `alpha_boundary_forward_check.py` READS s11_denovo_results.json, driver-repoint needed) → `vol_9_vacuum_datasheet/results/`. Cross-vol: `cvr_ee_sweep_metrics.json` → `ave-kb/common/results/` (common+vol4, 5 citers). **ANOM-3 (structural):** cited data is force-tracked with NO allowlist lines — a clean-worktree regenerate-then-readd would silently drop all 38; the `results/` migration fixes this structurally.

**UNCITED-SCRATCH (14, all driver-regenerable, all `git rm --cached`-safe):** 6 vol_1 `*_results.json`, 8 vol_9 (incl. 3 facility-sweep PDF twins of cited PNGs — confirm-unused before drop; json siblings of cited renders). No allowlist lines exist for these.

**Part 2 — orphans: 91 files, 35.2 MB** (498 scanned; 405 basename-cited + 2 tex-stem-rescued; down from PR #502's ~106/~122MB — #507 placed figures). Recommend tally: KEEP-IN-PLACE 21 · DELETE-CANDIDATE 40 · ARCHIVE 4 · GRANT-CALL 26. Group tables + named sub-rulings = P2 §2. Per-group inventories (full paths verified at HEAD, lane transcript carries per-row sizes):
- **A vol_6 (28):** 3 `*_topological_strain.png` top-level (ARCHIVE), 14 `figures/*_{dynamic_flux,density_equator}.png` (regenerable, DELETE-CANDIDATE), 10 `circuit_*.png` twins in `figures/`+`circuits/` (chapters cite the `.pdf` copies — basename-collision false-CITED caught and corrected), 1 `figures/ie_validation_z1_14.pdf` (GRANT-CALL, ledger context).
- **B assets/figures (17):** 15 NO-driver panels (decoherence frames 11MB, impedance/astro panels — GRANT-CALL), `cross_scale_universality.png` + `galactic_rotation_curve.png` regenerable (DELETE-CANDIDATE; `.pdf` twin of the latter is the cited copy).
- **C templates/lab-notebook (12):** source-assets, KEEP.
- **D vol_9 (11):** 7 `gen_*.py` generated-not-placed (KEEP pending P2 ruling), 4 `T*_debug.png` duplicates (DELETE-CANDIDATE; regen.py writes the research/ tier; `17_engine_requirements.tex` cites other stems only).
- **E vol_4 (7):** hopf_01 ×3, fusion ×2, chiral-acoustic, doping-svg — mostly NO-driver, GRANT-CALL.
- **F research/figures/engine_acceptance (4):** regen.py-regenerable uncited debug frames, DELETE-CANDIDATE.
- **G assets misc (8):** 3 chiral-yee gifs regenerable (DELETE-CANDIDATE), 3 `sim_outputs` canonical-asset (KEEP), research svg + archived gif (KEEP/leave).
- **H tail (4):** vol_3 ×2 regenerable (DELETE-CANDIDATE), vol_5 tau-fold pdf + vol_2 ie_validation pdf (GRANT-CALL, ANOM-7).

**Key lane-(c) anomalies:** ANOM-2 carbon_strain do-not-place walk-back; ANOM-5 PDF-vs-PNG twin splits (confirm before drop); ANOM-6 pdf-vs-png basename collisions adjudicated per-file via graphicspath; ANOM-7 ie_validation dual-copy w/ ledger ruling; ANOM-8 galactic-rotation png/pdf twin; ANOM-9 debug-frame dual placement (vol_9 graphicspath lists BOTH tiers); ANOM-11 the citer-loop word-splitting false-negative (caught, re-run, cross-checked).

## §D — Lane (d): format consistency

**Root CLAUDE.md (8 claims checked: 3 CURRENT / 3 STALE / 2 DEAD):** `:87` "109 audit tags" (HEAD 216); `:37` `analysis/integration` row — branch GONE from origin; `:38` `research/l3-electron-soliton` row — branch GONE; `:29` L3-archive "129 docs" (HEAD 137); `:97-99` pre-commit prose keyed to the dead `analysis/integration` default. CURRENT: hook exists+wired, pyproject pythonpath claim, structure paths. P3: one doc-fix PR rewrites the branching table + counts to HEAD truth.

**README accounting (5 surfaces, 0 basis declarations):** badge `:6`, prose `:28`, `:61` header, `:179` classification note (kind-taxonomy, needs one basis sentence), table `:181+` (33 physical rows displaying 1..47 via 7 compound rows — the conventions "40 displayed rows" descriptor is wrong, fix to 33). Fourth surface: `LIVING_REFERENCE.md:375,:387` "46 predictions" ×2 → P2 §3 ruling. Corpus-wide two-pattern-family grep found no further count surfaces.

**.tex spot-check (15 files, 20% of the 75-file volume set — frame: vol_1 ×5, vol_4 ×5, backmatter ×3, vol_9 ×2):** N1 15/15 CLEAN (no substrate glyph, no condensate-noun, no bare trefoil-electron). N2 rule holds everywhere sampled (roman instances within allowance) BUT the invariant's own confirmed-by counts are stale (vol_1 script 52→114; vol_4 roman 4→6, all 6 in `11_experimental_falsification.tex`). S1: shared-set envs all in-set; out-of-set = raw `tcolorbox` (`11_experimental_falsification.tex:233,299,311`; `15_autoresonant_breakdown_spice.tex:60,79`) + `warningbox` (`backmatter/02:1226`, `03:430`; 16 corpus uses) → P2 §5 ruling. P3 extends the check to the 60 unsampled files.

**Status-header snapshot (96 epic docs):** 40 have some Status line (17 enum-token / 23 non-enum: READY, COMPLETE, PENDING, LIVE, DRAFT, CHARTER-ACTIVE, …); 56 have NONE; **0 fully (c)-compliant**; `index.md` exempt but lacks a machine-readable last-updated line. State-triage evidence per doc in the lane transcript; UNCLEAR-pending-owner: `2026-06-23_owed-derivations-scoping`, `2026-06-06_biquaternion-node-algebra`, `2026-06-05_observable-battery-infrastructure`, `2026-06-12_vol9-kb-discipline-pass`, `motion-stability-bemf-longitudinal`.

# AVE-Core Orchestration Index

**Last updated**: 2026-05-20 EOD++++++++++ — **Q-C15-10 ✓ Grant adjudicated atopile walk-back (Option A: new sibling repo `AVE-Hardware-Modules`)**. Phase 1a delivered KiCad-native `.kicad_sch` — workspace deviation from established atopile-first pattern (AVE-PONDER + AVE-HOPF both atopile). Walk-back brief landed at [`exp-c15-cleave-01-phase-1a-rev1-atopile-walkback-brief.md`](exp-c15-cleave-01-phase-1a-rev1-atopile-walkback-brief.md). Module-audit expanded initial 5-module decomposition to **8 modules** after gap analysis (precision_input_cap_10pf pulled out as KB-loadbearing per Q-C15-04; ptfe_turret_post_standoff added — was missed in first pass; sub-D interface split into subd9_supply_header + molex3_pzt_header per Q-C15-07 dedicated FT2 topology). Two-stage execution: **Stage A** scaffolds `AVE-Hardware-Modules` sibling repo + creates 8 modules + tests + atopile package config + remote create + push; **Stage B** (gated on A return) walks back AVE-Bench-FemtoElectrometer `hardware/` to `cleave_01.ato` + 8-module composition with post-adjudication topology + archives orphan KiCad files to `hardware/cad/_archive/` + closes Q-C15-10 + opens Q-C15-11 (paired Q-HWMOD-01) cross-repo sync tracking. AVE-Bench-FemtoElectrometer `main` at `331a778` (Phase 1a merged KiCad-native) preserved as predecessor; Phase 1a-rev1 lands on new branch `analysis/phase-1a-rev1-atopile-walkback`. Earlier today: Phase 1a ✓ MERGED to main (KiCad-native; audit tag `audit/2026-05-20_phase-1a-kicad-design`) + 4 Grant adjudications Q-C15-07/08/09 + Q1.2 closed; Phase 0→1 ✓ PROMOTED + GitHub remote ✓ LIVE; Q-C15-01 ✓ RESOLVED dedicated chamber; Phase 0 ✓ SCAFFOLD LANDED; framework-readiness audit ✓ NO DRIFT; all 3 Experimental-Arc sub-epics audited (A1-HOPF + C11 + C15) — all NO DRIFT. C11-MACH-ZEHNDER Pattern B canonical KB leaf landed (driver live-fire 249.6394 rad). A1-HOPF Phase 0a ✓ COMPLETE + Phase B walk-back. C11 Phase 0 facility partnership search initiating. A1-HOPF Phase 0b ready for Grant fab submission. Phase 1b/1c on C15 deferred until Phase 1a-rev1 atopile walk-back lands (KiCad GUI work proceeds from `ato build` outputs).
**Current HEAD on `analysis/integration`**: `f9b2e55` — Shamir 2022 merge tip (advances with this commit)
**Audit tag count**: 33 (`git tag -l "audit/*" | wc -l`)
**Active branches** (local): 6 — `analysis/integration`, `analysis/c8-baryon-ladder-pdg-anchor`, `benn/long-running`, `golden-torus-update`, `main`, `research/l3-electron-soliton`. All 11 May-19 implementor branches merged + deleted (local + remote).
**Cross-repo state**: AVE-Skills `main` at `4f504c0` (v1.2 ave-canonical-leaf-pull); other AVE sibling repos not touched this session.

This is the cross-cutting carry-forward for AVE-Core orchestration. Per-epic state lives in adjacent `<epic-slug>.md` files; this doc carries the priority ladder, open decisions, skill-ecosystem state, and active-epic table. **For canonical full handoff content, this file is authoritative**; per-epic docs hold phase plans.

## Session summary (2026-05-19 EOD, 3 batches)

This session executed three sequential batches with 11 implementor sessions + 4 orchestration-session commits + 33 audit tags landed. **Post-session addendum (2026-05-19 EOD+)**: c8-baryon-ladder-pdg-anchor branch merged via `f4c9ffa` (12-commit merge resolving corpus-coherence breakage where matrix + closure-roadmap cited a driver missing from integration); audit tag count now 34. Skill update v1.3 → v1.4 (trigger 9 — merge-conflict-shape claims) from in-session failure #5 (agent generated 3-path adjudication speculation when empirical `git merge --no-commit` produced only 2 actual conflicts vs predicted "minimal-to-moderate" surface).

**Batch 1 (early-session)**: cosmic-axis glossary epic + h-infinity 3-epic arc (derivation-audit + framing-forward + downstream-cascade) + SDSS DR17 → 5 closed epics, 5 audit tags.

**Batch 2 (mid-session)**: γ A-034 catalog ε/μ extension + α `ave-canonical-leaf-pull` v1.1 trigger 16 + #5 Longo 2011 corpus pin walk-back + soliton-coupling Session 1 scoping refactor + #6 GZ-DECaLS Outcome-E + closed-epic archive move + β cosmic-ε / DE projection Session 1 scoping → 3 closed epics, 3 audit tags, 2 skill versions.

**Batch 3 (late-session, parallel)**: v1.2 `ave-canonical-leaf-pull` sub-case (e-i)/(e-ii)/(e-iii) for projection-vs-measurement + soliton-coupling Session 2 (4 catalog rows + planetary scoring 14-15/16) + β cosmic-ε Session 2 (Op14 cosmic-horizon profile + projection chain + cosmic-DE ASYM-N(ε) row) + Shamir 2022 cross-catalog → 3 closed/half-closed epics, 3 audit tags, 1 skill version.

**Net session result**: A-034 catalog 21 → 26 instances. 1 new canonical leaf (`op14-cosmic-horizon-profile.md`). 8 new research docs. 3 process anomalies surfaced. 5+ adjudications queued for next orchestrator.

## Active epics

| Epic | Doc | Status | Last phase landed | Next |
|---|---|---|---|---|
| Section E cascade | [`section-e-cascade.md`](section-e-cascade.md) | ACTIVE — E1b-prime CLOSED Outcome Marginal-D; SDSS DR17 + Shamir 2022 cross-catalogs CLOSED; methodology-systematic at 2.99σ surfaced | E1b-prime merged via `c587573` audit `audit/2026-05-19_c5-pantheon-tightening` | (a) Methodology-systematic adjudication (Ganalyzer vs Longo cos-γ); (b) Observable 5/6/7 execution; (c) Joint Pantheon+ + SDSS + Shamir-DESI constraint |
| Soliton-lattice coupling operator | [`soliton-lattice-coupling-operator.md`](soliton-lattice-coupling-operator.md) | ACTIVE — Sessions 1+2 CLOSED; Sessions 3-5 queued. Catalog row additions complete (Row 9-a, 9-b, 11-a, 14-a). Planetary scoring 14-15/16 class match + 3/3 anomalies resolved as stable kernel-branch equilibria. Neptune class-mismatch sub-anomaly surfaced (flag-don't-fix). | Session 2 merged via `78b9770` audit `audit/2026-05-19_soliton-lattice-coupling-operator-session2` | Session 3 (planetary finalization + Neptune sub-class adjudication) OR Session 4 (galactic-scale extension to SDSS DR17 via Row 11-a) |
| Cosmic-ε / DE projection | [`cosmic-epsilon-de-projection-scoping.md`](cosmic-epsilon-de-projection-scoping.md) | ACTIVE — Sessions 1+2 CLOSED; Sessions 3-4 conditional. Op14 cosmic-horizon profile leaf landed. Projection chain (6 components, no magnitude-matching). γ verdict (composite Class E + ASYM-N(ε)) structurally confirmed. Row 14b cosmic-DE catalog row added. Anomaly A3 closed. A1 (MOND classification) + A2 (`cosmological-constant-closure.md` dual framing) carried forward. | Session 2 merged via `8e09046` (+ conflict fixup `4e99d77`); audit `audit/2026-05-19_cosmic-epsilon-de-projection-session2` | Session 3 (downstream walk-back: `cosmological-constant-closure.md` framing reconciliation per A2) OR Session 4 conditional (4th-category "thermodynamic latent-heat flow" if load-bearing) |
| **Experimental Arc** (parent) | [`experimental-arc.md`](experimental-arc.md) | ACTIVE — Phase 2 audit complete 2026-05-20; 3 sub-epics spawned per cascade-emphasis ranking. Adjudication queue items EXP-1 / EXP-3 / EXP-4 promoted to sub-epics. EXP-2 (walk-back scope) RESOLVED to surgical (4-5 leaves). EXP-6 (B4-PROTEIN) + EXP-7 (C2-T-PAIR) DEFERRED outside cascade-emphasis top-3. | Phase 1 walk-back bundled with sub-epic-establishment commit | Phase 3 driver readiness audit (after sub-epic Phase 1 measurements land); Phase 4 cross-repo coordination on-demand; Phase 5 continuous canonical tie-back |
| ↳ EXP-A1-HOPF (cascade × executability) | [`exp-a1-hopf.md`](exp-a1-hopf.md) + [Phase A audit](exp-a1-hopf-repo-audit.md) + [Sim audit](exp-a1-hopf-sim-audit.md) | **PHASE 0a ✓ COMPLETE + SIM AUDIT ✓ NO DRIFT — Phase 0b READY**. Phase B walk-back 6 commits on AVE-HOPF `analysis/a1-hopf-audit-walkback-2026-05-20` (local, not pushed): BLOCKER-1 Gerbers exported to `Gerbers_hopf_02a/`; BLOCKER-2 `hopf_02a_ORDERING.md` + `hopf_02a_BOM.md` drafted; R1.1 hardware/ reorg (hopf_01_* + hopf_02a_* prefix); ALPHA constants-gate fix in `hopf_02_nec2_run.py`; MAGIC_NUMBERS whitelist extension. Sim audit verified α + (p,q) + C8 axes: exact α match, (p,q) aligned with FI-13 RESOLVED, C8 PASS strengthens Outcome A/C interpretation without formula drift. 7 misdirected AVE-Core citations walked-back inline. | Phase A audit + Sim audit + Phase B walk-back all landed 2026-05-20 | Grant uploads `Gerbers_hopf_02a/` to JLCPCB per `hopf_02a_ORDERING.md`; orders mandrels per `hopf_02a_BOM.md`; optionally PR + squash-merge AVE-HOPF branch to main per AVE-HOPF AGENTS.md §3 |
| ↳ EXP-C15-CLEAVE-01 (cascade SIZE — largest) | [`exp-c15-cleave-01.md`](exp-c15-cleave-01.md) + [Framework-readiness audit](exp-c15-cleave-01-sim-audit.md) + [Phase 0 scaffold brief](exp-c15-cleave-01-phase-0-scaffolding.md) + [Q-C15-01 chamber scoping](exp-c15-cleave-01-q-c15-01-chamber-scoping.md) + [Phase 1 KiCad brief (predecessor)](exp-c15-cleave-01-phase-1-kicad-brief.md) + [Phase 1a-rev1 atopile walk-back brief](exp-c15-cleave-01-phase-1a-rev1-atopile-walkback-brief.md) + **sibling repos: `AVE-Bench-FemtoElectrometer` main @ `331a778` (Phase 1a KiCad-native; predecessor) + `AVE-Hardware-Modules` (NEW; Stage A scaffolding pending dispatch)** | **PHASE 1a ✓ MERGED to main at `331a778`** (audit tag `audit/2026-05-20_phase-1a-kicad-design` at `6d6552f`) → **PHASE 1a-rev1 ATOPILE WALK-BACK ACTIVE** (Q-C15-10 Grant adjudicated). Two-stage execution: **Stage A** scaffolds new `AVE-Hardware-Modules` sibling repo + 8 modules (ada4530_electrometer_frontend + precision_input_cap_10pf + lm4040_voltage_reference + mill_max_ptfe_socket + ptfe_turret_post_standoff + subd9_supply_header + molex3_pzt_header + bnc_signal_output) + smoke tests + atopile package config + remote create + push; **Stage B** (gated on A return) walks back C15 hardware to `cleave_01.ato` + 8-module composition with post-adjudication topology + archives orphan `.kicad_sch` + ASCII companion to `hardware/cad/_archive/2026-05-20_phase-1a-kicad-draft/` + Q-C15-10 OPEN → CLOSED + Q-C15-11 NEW OPEN (cross-repo sync tracking paired with Q-HWMOD-01 in AVE-Hardware-Modules). All prior adjudications honored: Q-C15-01 dedicated chamber + Q-C15-03 vacuum-gap default + Q-C15-04 NP0/C0G ±1% + Q-C15-05 commodity PZT + Q-C15-07 dedicated FT2 + Q-C15-08 dedicated PTFE-socket return + Q-C15-09 external-only ground + Q1.2 off-PCBA HV amp. KB-leaf prediction verbatim preserved; pure-AVE-corpus zero. F-severity (Ax2 dies if 0.0 mV); U-D 41.5 mV/μm; ξ_topo family cascade (6+ dependents, largest single-row cascade in matrix). | Phase 1a-rev1 brief landed 2026-05-20 EOD++++++++++; Stage A implementor dispatch IMMEDIATELY | Stage A implementor return → Stage B implementor dispatch (gated) → orchestrator + Grant pre-merge review → merge `--no-ff` + audit tag `audit/2026-05-20_phase-1a-rev1-atopile-walkback` → Phase 1b/1c KiCad GUI work from `ato build` outputs → Phase 2 fab + assembly (~$7670 full BOM mid-range) → Phase 3 measurement (ave-prereg + sweep) → Phase 4 outcome adjudication |
| ↳ EXP-C11-MACH-ZEHNDER (cascade × severity F) | [`exp-c11-mach-zehnder.md`](exp-c11-mach-zehnder.md) + [Sim audit](exp-c11-mach-zehnder-sim-audit.md) + [project-c11-mach-zehnder.md canonical KB leaf](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/project-c11-mach-zehnder.md) | **PHASE 0 — Facility partnership search initiating + Sim audit ✓ NO DRIFT.** Driver canonical (live-fire 249.6394 rad ≈ ~250 rad prediction at 1m + 100 eV); Pattern B canonical KB leaf landed at vol4/ch11/. F-severity (Ax3 + Ax1 die); ν_vac=2/7 cascade triangulation (C1 FULL PASS Phase 5 + C11 PENDING + C12 LISA-wait); 2-of-3 triangulation enabled if C11 PASS. Sim audit verified ν_vac=2/7 canonical + ε_11=7GM/c²r engine + n_s/n_t formula + Q-G47 Sessions 19 closure preserved ν_vac. | Sim audit + project KB leaf landed 2026-05-20 EOD+++ | Phase 0 facility partnership search: literature survey of electron-interferometer SOTA (Hasselbach Tübingen / LENS Italy / NIST / TEM holography centers) → candidate verification → cold-email outreach. Phase 2 ave-prereg gated on facility partnership. |

## Recently closed epics (this session — 8 epics, 7 with audit tags)

| Epic | Doc location | Closure | Audit tag |
|---|---|---|---|
| Cosmic-axis glossary | [`_archive/cosmic-axis-glossary.md`](_archive/cosmic-axis-glossary.md) | Merged 2026-05-19 EOD via `fb62fa8` | `audit/2026-05-19_cosmic-axis-glossary` |
| H_∞ derivation audit | [`_archive/h-infinity-derivation-audit.md`](_archive/h-infinity-derivation-audit.md) | Merged 2026-05-19 EOD via `ceb8205` | `audit/2026-05-19_h-infinity-derivation-audit` |
| H_∞ framing-forward | [`_archive/h-infinity-framing-forward.md`](_archive/h-infinity-framing-forward.md) | Merged 2026-05-19 EOD via `a7e555e` | `audit/2026-05-19_h-infinity-framing-forward` |
| H_∞ downstream cascade | [`_archive/h-infinity-downstream-cascade.md`](_archive/h-infinity-downstream-cascade.md) | Merged 2026-05-19 EOD via `d2d38de` (Class C → Class E reclass + 5 anomalies + Class E candidate sweep) | `audit/2026-05-19_h-infinity-downstream-cascade` |
| C5 SDSS DR17 spin-orientation | [`_archive/c5-sdss-dr17-spin-orientation.md`](_archive/c5-sdss-dr17-spin-orientation.md) | Merged 2026-05-19 EOD via `9f976e0` (Marginal-D, σ_LSS=6.83°, axis (l=129°, b=79°); CMB-LSS separation 36.75° at 5.33σ from zero) | `audit/2026-05-19_c5-sdss-dr17-spin-orientation` |
| C5 corpus pin fix (no epic doc; implementor-only) | n/a | Merged via `7e3d807` (Longo 2011 (32°, 32°) → (52°, 68.5°) walk-back) | `audit/2026-05-19_c5-corpus-pin-fix` |
| C5 GZ-DECaLS cross-catalog (Outcome E; no epic doc) | n/a | Merged via `0275a6a` (Walmsley+2022 lacks chirality observable; retarget identified) | `audit/2026-05-19_c5-gz-decals-spin-orientation` |
| Soliton-coupling Session 1 (scoping refactor — multi-session epic) | (in active epic doc) | Merged via `d413726` (refactor to A-034 catalog-extension framing) | `audit/2026-05-19_soliton-lattice-coupling-operator-scoping` |
| β cosmic-ε Session 1 (scoping — multi-session epic) | (in active epic doc) | Merged via `af8c522` (scoping doc + 3 plumber-physical questions) | `audit/2026-05-19_cosmic-epsilon-de-projection-scoping` |
| Soliton-coupling Session 2 | (in active epic doc) | Merged via `78b9770` (4 catalog rows + 14-15/16 planetary class match + 3/3 anomalies) | `audit/2026-05-19_soliton-lattice-coupling-operator-session2` |
| β cosmic-ε Session 2 | (in active epic doc) | Merged via `8e09046` + fixup `4e99d77` (Op14 cosmic-horizon profile + projection chain + Row 14b) | `audit/2026-05-19_cosmic-epsilon-de-projection-session2` |
| C5 Shamir 2022 cross-catalog | [`_archive/c5-shamir-2022-cross-catalog.md`](_archive/c5-shamir-2022-cross-catalog.md) | Merged via `f9b2e55` (Outcome A WEAK + E2 catalog-access sub-finding + 2.99σ methodology-systematic) | `audit/2026-05-19_c5-shamir-2022-cross-catalog` |

## Queued epics (not yet kicked off)

| Epic | Doc | Trigger | Notes |
|---|---|---|---|
| DM META closure | (no doc yet) | Grant greenlight | Independent of Section E. Closes C13c META row. ~1-2 sessions. |
| Phase 2 mass-spectrum activation | (no doc yet) | Grant greenlight | Pre-greenlit 2026-04-30 per [`research/_archive/L3_electron_soliton/98_framework_decision_ii_mass_spectrum_activation.md:5`](../research/_archive/L3_electron_soliton/98_framework_decision_ii_mass_spectrum_activation.md). W/Z/Higgs eigenvalue solver; ~1 week scope. |
| Lossless-dynamics framing extension | (no doc yet) | Grant-greenlight — adjudication on Option (a) vs (b) | Grant 2026-05-19 EOD observation: "orbital dynamics as lossless fluid dynamics" suggests adding (a) "Lossless dynamics" as new row class to A-034 OR (b) "lossless vs lossy" as new axis (alongside ε/μ). Option (b) cleaner — each row gets a (SYM/ASYM × ε/μ × lossless/lossy) tag. Refines Reynolds/N-body predictability scaling for Q3' adjudication. ~1-2 hr corpus edit + companion-row-link update. |
| Soliton-coupling Session 3 | [`soliton-lattice-coupling-operator.md`](soliton-lattice-coupling-operator.md) | Grant adjudication on Neptune class-mismatch (sub-class refinement vs operator class-prediction-granularity) | Per epic doc Phase plan: planetary finalization. Estimated 1-2 hr. |
| Soliton-coupling Session 4 | [`soliton-lattice-coupling-operator.md`](soliton-lattice-coupling-operator.md) | Session 3 verdict | Galactic-scale extension to SDSS DR17 via Row 11-a; per Ax 2 TKI scaling from Row 9-a planetary form. Estimated 1-2 hr. |
| β cosmic-ε Session 3 | [`cosmic-epsilon-de-projection-scoping.md`](cosmic-epsilon-de-projection-scoping.md) | Triggered by Anomaly A2 (`cosmological-constant-closure.md` dual framing) | Downstream walk-back if Session 2 reveals corpus framing inconsistencies. Estimated 1-2 hr. |

## Adjudication queue for next orchestrator (5 substantive items + 4 hygiene)

Grant has 5 substantive items + 4 hygiene items pending. Prioritized roughly by urgency / impact:

### Substantive (physics / framework)

| # | Item | Origin | Recommendation |
|---|---|---|---|
| 1 | **Methodology-systematic adjudication**: Ganalyzer (Shamir 2022) vs Longo cos-γ (AVE SDSS DR17) — same SDSS-class input galaxies, 74° axis separation = 2.99σ_combined. AVE-Longo gets 5.33σ EXCLUSION of CMB-LSS alignment; Shamir's DESI Legacy gets 3.77° AGREEMENT. | Shamir 2022 epic | **PROVISIONAL** (walked back from RESOLVED-BY-IMPLICATION 2026-05-19 EOD+++ per external review). Initial temporal-classifier framing misclassified Ganalyzer + Longo as bulk-vs-individual estimators; per [shamir-result.md:39+62](../../research/2026-05-19_c5-shamir-2022-cross-catalog-result.md) + [sdss-result.md:62](../../research/2026-05-19_c5-sdss-spin-orientation-result.md), BOTH are per-galaxy chirality classifiers ($\chi_i \in \{-1,+1\}$) aggregated to population dipole. Difference is per-galaxy classification feature (algorithmic peripheral-pixel vs crowdsourced isophotal-twist). 2.99σ is per-galaxy-estimator-systematic. **Discriminating test**: McAdam & Shamir 2023 cross-comparison ([shamir-result.md:371](../../research/2026-05-19_c5-shamir-2022-cross-catalog-result.md)) — Shamir's Ganalyzer on the SAME GZ1 catalog AVE uses. If methodology-systematic dominant → Ganalyzer/GZ1 reproduces Shamir DESI axis (l=242°, b=-47°); if catalog-systematic dominant → reproduces AVE Longo axis (l=129°, b=79°). 4 interpretive alternatives enumerated in leaf §Methodology-systematic (Alt 1 estimator-systematic / Alt 2 bulk-vs-individual / Alt 3 catalog-selection / Alt 4 image-resolution). Adjudication NOT resolved by temporal-regime axis. |
| 2 | **Neptune spin-axis class-mismatch** (Soliton Session 2 sub-anomaly): operator predicts orthogonal-branch for icy-mantle class (Uranus + Neptune same class with comparable mass + rotation period); Neptune observed at 28° moderate. Neptune's mag-axis (47°) CONFIRMS class; spin-axis FAILS. Two paths: (A) sub-class refinement within icy-mantle (Neptune has higher internal heat-flux — could be on lossy branch per the lossless-dynamics framing), (B) acknowledged operator class-prediction-granularity limitation. Per Q1' adjudication, this is class-match-but-specific-value-fail — NOT a Class E joint-constraint kill. | Soliton Session 2 | Path A recommended given the lossless-dynamics observation (Neptune-as-lossy-branch is a substantive structural explanation, not an ad-hoc patch). Triggers Soliton-coupling Session 3 with refined per-internal-heat-flux sub-class taxonomy. |
| 3 | **Lossless-dynamics framing** | Grant observation | **RESOLVED 2026-05-19 EOD+++ via [temporal-saturation-regime-classifier.md](../manuscript/ave-kb/common/temporal-saturation-regime-classifier.md)** — Option (c) selected (companion KB leaf, NOT catalog row mutation NOR orthogonal axis tag). Trichotomy (lossless / cyclic / lossy) per $\delta_{\text{AVE}} = t_{\text{sat}}/t_{\text{period}}$ — TAXONOMIC bridge classifying EM tan δ + fluid Reynolds + cavity QED g/κ under common substrate-physics axis (NOT yet derivational; forward-prediction of one classical value from S(A) + t_sat structure is the upgrade path). 14 classical-physics field analogues mapped with CANONICAL/EXTENSION/NEW-MAPPING/PARTIAL tags. Closes Q3' predictability scaling via Reynolds-analogue δ_AVE × N with corrected empirical anchor (6/8 spin-axis class match per Soliton Session 2:167, NOT 8/8 as originally drafted). |
| 4 | **C5 threshold-policy adjudication** (still open from earlier): SDSS DR17 result outcome label depends on adjudication criterion — `20° + 3σ_combined` (Marginal-D stands) OR `σ_combined-only` (Outcome A formal disconfirmation) OR `cascade-loose` (need N≥3 disconfirmations). Soliton Session 2 + β Session 2 results may change framing — operator-output reframing makes "alignment threshold" a soft criterion since the operator predicts class-direction not exact value. | Earlier session | **PROVISIONAL** — operator-output reframing structurally maps threshold-policy onto Q1' class-prediction-tolerance (±15°), but landing as RESOLVED requires Grant explicit confirmation (procedural lesson from Item 1 walk-back: RESOLVED-BY-IMPLICATION framing is procedurally weak; default to PROVISIONAL + explicit confirmation step). Surface for Grant call. |
| 5 | **4th-category "thermodynamic latent-heat flow"** framing (β Session 1 Q3 4th option): if neither Class E (joint-constraint) nor ASYM-N(ε) (saturation event) fully captures DE structurally, a new class for "thermodynamic flow observables" may be warranted. Session 2 confirmed γ (composite Class E + ASYM-N(ε)) suffices for now — but reserves option to extend. | β Session 1 Q3 | Hold pending downstream signals; not load-bearing unless Session 3 walk-back reveals tension. |

### Process / discipline

| # | Item | Recurrence | Recommendation |
|---|---|---|---|
| 6 | **Worktree-spawn branch-state leak** | 3rd recurrence this session | `isolation: "worktree"` spawn-default leaks the implementor's branch checkout into the orchestration session's main worktree. Per-spawn observed: scoping refactor, Shamir, β Session 2. The v1.3 pre-commit branch-check discipline catches it each time, but the leak is structural. **Recommended fix**: extend `ave-handoff-canonical-locale` v1.0 → v1.1 with explicit `orchestration-resets-to-integration-post-spawn` step. Alternatively, the implementor-spawn workflow in `_orchestration/README.md` "Spawning implementors via the Agent tool — discipline" section can add an explicit checkout after each spawn. |
| 7 | **Merge-conflict-marker commit-slip** | 1 instance this session (commit `8e09046` β Session 2 merge had conflict markers at lines 46-50 and 136-147 of `universal-saturation-kernel-catalog.md`; cleaned up at `4e99d77`) | `git commit --no-edit` on a merge-in-progress accepted markers without refusing. **Recommended fix**: (a) add pre-commit hook checking `<<<<<<<` patterns in staged files; (b) extend `ave-walk-back` skill to mandate `grep -ln '<<<<<<<' --staged` check before commit; (c) extend `verify-before-cite` v1.3 with "post-merge sanity check before push" trigger. Option (a) is most reliable; (b)/(c) are agent-discipline backups. |
| 8 | **Closed-epic archive move** | Done (item 5 from earlier session) | Resolved 2026-05-19 EOD: 5 closed epic docs moved to `_orchestration/_archive/` via `d8eb117`; inbound refs updated in 10 files. Shamir 2022 epic added to archive in this commit. |
| 9 | **Sibling-repo hygiene** (carry-forward from earlier sessions) | Long-standing | Items 6-9 from open-decisions table below remain queued: AVE-Protein WIP, AVE-Metamaterials WIP, AVE-QED PDF, c8-baryon-ladder branch fate. ~30 min each; batchable. |

## Next-move priority ladder

### Immediate (can spawn in parallel via `isolation: "worktree"`)

1. **Soliton-coupling Session 3** — planetary finalization + Neptune sub-class adjudication. Triggered by adjudication item 2 (Neptune class-mismatch path A); Neptune-on-lossy-branch substantive structural explanation now available via [temporal-saturation-regime-classifier.md](../manuscript/ave-kb/common/temporal-saturation-regime-classifier.md) (item 3 RESOLVED). ~1-2 hr. Depends on Grant Path A vs B call.
2. **McAdam & Shamir 2023 cross-comparison** — discriminating test for Item 1 PROVISIONAL adjudication. Tests whether Shamir Ganalyzer applied to AVE's GZ1 catalog reproduces Shamir DESI axis (methodology-systematic) OR AVE Longo axis (catalog-systematic). Catalog redistribution required first. ~1 session if catalog accessible.
3. **DM META closure** — independent of all above. ~1-2 sessions. Depends on Grant greenlight.

### Medium-term (multi-session)

4. **β cosmic-ε Session 3** — downstream walk-back of `cosmological-constant-closure.md` per Anomaly A2. Triggered by β Session 2 framing reconciliation.
5. **Soliton-coupling Session 4** — galactic-scale extension to SDSS DR17 via Row 11-a (Ax 2 TKI scaling from Row 9-a planetary form). Depends on Session 3 outcome.
6. **Phase 2 mass-spectrum activation** (W/Z/Higgs eigenvalue solver) per doc 98 §3.2. Grant pre-greenlit 2026-04-30. Not gated. ~1 week scope.
7. **Observable 5/6/7 execution** (E/B polarization, orbital alignments, G P_2 anisotropy) — each multi-session, deferred until C5 settles or methodology-systematic adjudication (item 1) resolves.
8. **Joint Pantheon+ + SDSS + Shamir-DESI Option B constraint** — if methodology-systematic adjudication (item 1) supports it.

### Hygiene tier

9. Items 6-9 from "Open decisions" below. Each ≤30 min; batchable into single hygiene-pass session.
10. Process-discipline fixes (items 6-7 from adjudication queue): pre-commit hook + skill amendments.

## Open decisions (carry-forward + new)

| # | Item | Detail |
|---|---|---|
| 1 | **Methodology-systematic adjudication** (NEW this session — adjudication item #1) | Ganalyzer vs Longo cos-γ; 2.99σ separation on same SDSS data. Load-bearing for C5 cascade interpretation. |
| 2 | **Neptune spin-axis class-mismatch** (NEW this session — adjudication item #2) | Path A (sub-class refinement, lossless-vs-lossy axis) vs Path B (granularity limitation). Recommend A. |
| 3 | **Lossless-dynamics framing** (NEW this session — adjudication item #3) | Option (a) new row class vs Option (b) new axis. Recommend (b). |
| 4 | **C5 threshold-policy adjudication** (carry-forward, refined) | 20° + 3σ_combined vs σ_combined-only vs cascade-loose. Probably resolved-by-implication via operator-output reframing. |
| 5 | **4th-category "thermodynamic latent-heat flow"** (carry-forward, β Session 1 Q3) | Hold pending downstream signals. |
| 6 | **C3-MUON-DELTA Run-4/5 update** (carry-forward) | Fermilab Run-4/5 expected 2026-2027 at ±10 ppm. Timing-dependent. |
| 7 | **AVE-Protein 51 uncommitted files** (carry-forward) | Mass deletions of engines + manuscript chapters. Surface: intentional WIP or accidental? Grant decides commit / stash / restore. |
| 8 | **AVE-Metamaterials SOLAR_PANEL_INITIATIVE WIP** (8 uncommitted, carry-forward) | Active workstream not yet committed. Grant decides when to commit. |
| 9 | **AVE-QED PDF gitignore + .tex commit** (2 uncommitted, carry-forward) | 1 modified `09_anomalous_moment.tex` + 1 untracked `main.pdf` (build artifact). Should gitignore the PDF, commit the .tex when ready. |
| 10 | **`analysis/c8-baryon-ladder-pdg-anchor` branch fate** (carry-forward) | 2 unpushed Q-G47 retrofit commits pushed earlier; branch still alive on local + origin. Keep as historical or delete via audit-tag pattern? |
| 11 | **Pre-commit hook for conflict markers** (NEW this session — process adjudication item #7) | Recommend installation. Triggered by `8e09046` merge-conflict-slip + `4e99d77` cleanup. |
| 12 | **Worktree-spawn branch-state-leak discipline** (NEW this session — process adjudication item #6) | Recommend extending `ave-handoff-canonical-locale` v1.0 → v1.1 OR `_orchestration/README.md` spawn-section. |
| 13 | **Soliton-coupling Session 3 kickoff** (NEW — gated on item #2 adjudication) | Implementor session ready when Neptune path A/B decided. |
| 14 | **β cosmic-ε Session 3 kickoff** (NEW — gated on Anomaly A2 from β Session 2) | Implementor session ready when downstream-walk-back greenlit. |

## Skill ecosystem state (current versions)

| Skill | Version | Location | Last amended | Purpose |
|---|---|---|---|---|
| `verify-before-cite` | **v1.4** (was 1.3 mid-session, 1.2 pre-session) | `~/.claude/skills/verify-before-cite/SKILL.md` | 2026-05-19 EOD+ (v1.4 post-c8-merge) | Trigger 9 added (merge-conflict-shape claims — empirical `git merge --no-commit` before adjudication). 7th instance of bilateral-axis pattern; FUTURE-STATE axis projection. Origin: failure #5 (c8-baryon-ladder merge speculation; Grant: "this is ridiculous"). |
| `consistency-vs-emergence` | **v1.1** (was 1.0 pre-session) | `~/.claude/skills/consistency-vs-emergence/SKILL.md` | 2026-05-19 EOD via skills commit `8dfc31d` | Class E added (operating-point projection / topological equilibrium observable). Closes H_∞ Class C miscategorization. |
| `ave-canonical-leaf-pull` | **v1.2** (was 1.0 pre-session) | `~/.claude/skills/ave-canonical-leaf-pull/SKILL.md` | 2026-05-19 EOD via skills commits `41e6b47` (v1.1) + `4f504c0` (v1.2) | Trigger 16 added (framework-extension proposals / SM/QED-creeper at design layer) at v1.1; sub-case (e-i)/(e-ii)/(e-iii) for projection-vs-measurement conflation at v1.2. Closes "cosmic polarization field" + "QFT cosmological constant problem" failure modes. |
| `ave-handoff-canonical-locale` | **v1.0** (added this session) | `~/.claude/skills/ave-handoff-canonical-locale/SKILL.md` | 2026-05-19 EOD | This directory's write-time discipline. Closes E1a + E1b loose-plans failure mode. |
| `ave-discipline-translate` | **v1.0** (NEW this session ++) | `~/.claude/skills/ave-discipline-translate/SKILL.md` | 2026-05-19 EOD++ post temporal-saturation-regime-classifier leaf (98994c1) | Cross-disciplinary translation check. Forces consultation of translation-tables/ + four-regimes.md + temporal-saturation-regime-classifier.md + chemistry-translation/ + ave-analytical-toolkit-index.md + VCA-translation-matrix + trampoline-analogy-primer BEFORE invoking classical-physics analogue (Reynolds, tan δ, MOSFET regime, Cooper pair, Kerr, Purcell, T1/T2, etc.). Closes "reach for classical-physics language reflexively" failure mode + discoverability gap on 8-location cross-disciplinary infrastructure. 5th skill in "before deriving" cluster (with ave-prereg + ave-canonical-leaf-pull + ave-analytical-tool-selection + substrate-native-check). Probationary until first formal probe 2026-08-19. |
| AVE-Core directives | n/a (corpus) | [`CLAUDE.md`](../CLAUDE.md) + [`_orchestration/README.md`](README.md) | 2026-05-19 EOD via integration commit `e9245cc` | Pre-commit branch-check discipline + implementor-spawn worktree-isolation default. Closes branch-confusion failure mode (subagent leaves working tree on its own branch). |

**25 active skills total**; adversarial probes at 14-for-14 finding orthogonal-axis gaps. The 4 skill updates this session (verify-before-cite v1.3 → v1.4 + consistency-vs-emergence v1.1 + ave-canonical-leaf-pull v1.2 + ave-discipline-translate v1.0 NEW) all closed real failure-modes that fired this session — pure-corpus-validation cycle working as intended.

## Data caching state

- **Pantheon+SH0ES canonical cache** at `data/pantheon_plus/` — `.dat` (579 KB, regular git) + `.cov` (33 MB, git-LFS) + `README.md` with re-download instructions and MD5 checksums. Required by `c5_pantheon_bulk_flow_tightening.py`. LFS filter at `.gitattributes` + gitignore allowlist override of `data/*` pattern.
- **SDSS DR17 Galaxy Zoo 1 cache** at `data/sdss_dr17/` — `.csv.gz` (19.4 MB, regular git via gitignore allowlist; not LFS) + `README.md`. Required by `c5_sdss_spin_orientation.py`. Galaxy Zoo 1 Table 2 (Lintott+2011, ~668k SDSS DR7 galaxies, crowdsourced visual classification).
- **Shamir 2022 cache** at `data/shamir_2022/` — README only (no catalog data; per-galaxy classifications not publicly redistributed per Phase 0 verification; E2 sub-finding). Driver uses paper-quoted Table 3 axis (RA, Dec) → galactic 68%-containment radius via 200×200 uniform sampling.

## Catalog state (A-034 universal-saturation-kernel-catalog)

**26 instances** at `manuscript/ave-kb/common/universal-saturation-kernel-catalog.md` (was 21 at session start). 5 new rows added:

- Row 9-a: Planetary spin-axis (SYM, branch structure aligned/moderate/orthogonal/retrograde; ε-channel via Cosserat)
- Row 9-b: Planetary mag-vs-spin offset (ASYM-N candidate, μ-channel-vs-spin-channel)
- Row 11-a: Galactic spin-axis (TBD, scoped Session 4)
- Row 14-a: LSS spin-axis (TBD conjectural, scoped Session 5 conditional)
- Row 14b: Cosmic DE / ε-sector (ASYM-N ε, companion to Row 14 K4-crystallisation-SYM*)

**ε/μ axis classification** + **gap-cells table** + **companion-row links** all extended this session. Catalog now has explicit cross-section structure (SYM/ASYM-N(ε)/ASYM-N(μ)/ASYM-E × scale × observable-channel).

**Internal inconsistency carried forward**: Row 11 MOND classified SYM at line 38 of catalog; canonical leaf `saturated-lattice-mutual-inductance.md:4` classifies as ASYM-N(μ). Both classifications appear in catalog (the SYM at original line + the ASYM-N(μ) treatment in gap-cells table). Queued for adjudication.

## Reference paths (canonical, tracked)

| Path | Purpose |
|---|---|
| [`_orchestration/section-e-cascade.md`](section-e-cascade.md) | Section E cascade (ACTIVE — E1b-prime CLOSED Marginal-D; SDSS DR17 + Shamir CLOSED) |
| [`_orchestration/soliton-lattice-coupling-operator.md`](soliton-lattice-coupling-operator.md) | Soliton-coupling epic (ACTIVE — Sessions 1+2 CLOSED; Sessions 3-5 queued) |
| [`_orchestration/cosmic-epsilon-de-projection-scoping.md`](cosmic-epsilon-de-projection-scoping.md) | β cosmic-ε / DE projection epic (ACTIVE — Sessions 1+2 CLOSED; Sessions 3-4 conditional) |
| [`_orchestration/_archive/`](_archive/) | 7 closed-epic docs (cosmic-axis-glossary + h-infinity 3 + c5-sdss-dr17 + c5-shamir-2022) |
| [`_orchestration/README.md`](README.md) | Convention doc; spawn discipline; lifecycle pattern |
| [`CLAUDE.md`](../CLAUDE.md) | AVE-Core agent orientation; pre-commit branch-check; merge pattern |
| [`manuscript/ave-kb/CLAUDE.md`](../manuscript/ave-kb/CLAUDE.md) | Cross-cutting KB invariants |
| [`manuscript/ave-kb/common/universal-saturation-kernel-catalog.md`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) | A-034 catalog (26 instances, 4-axis classification) |
| [`manuscript/ave-kb/common/divergence-test-substrate-map.md`](../manuscript/ave-kb/common/divergence-test-substrate-map.md) | 33-row experimental-claim landscape; C5 row Marginal-D + cross-catalog sub-findings |
| [`manuscript/ave-kb/common/closure-roadmap.md`](../manuscript/ave-kb/common/closure-roadmap.md) | Running changelog |
| [`manuscript/ave-kb/common/cosmic-axes-and-frames-glossary.md`](../manuscript/ave-kb/common/cosmic-axes-and-frames-glossary.md) | K4 rest frame ↔ Ω_freeze definitional leaf (NEW earlier in session) |
| [`manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/op14-cosmic-horizon-profile.md) | Op14 cosmic-horizon profile leaf (NEW β Session 2) |
| `data/pantheon_plus/README.md` + `data/sdss_dr17/README.md` + `data/shamir_2022/README.md` | Canonical data caches with re-download instructions |
| `git tag -l "audit/*" \| wc -l` | 34 immutable audit tags (13 new this session, including c8-baryon-ladder post-session) |
| [`.agents/handoffs/`](../.agents/handoffs/) | Ephemeral scratch (gitignored; NOT canonical) |

## Playbook for the next orchestration session

1. **First read**: this file (`index.md`) + the relevant active epic doc(s) — particularly `soliton-lattice-coupling-operator.md` and `cosmic-epsilon-de-projection-scoping.md` (both multi-session, Sessions 3+ queued).
2. **Phase 0 state verification**:
   - `git log analysis/integration -1 --oneline` should match HEAD `f9b2e55` (or have advanced).
   - `git tag -l "audit/*" | wc -l` should match 33 (or higher).
   - `git branch --show-current` should report `analysis/integration` — if not, `git checkout analysis/integration` BEFORE any commit per CLAUDE.md "Pre-commit discipline" section.
   - Verify no leftover worktrees at `.claude/worktrees/` (none expected at handoff).
3. **Don't trust corpus-state claims here without re-verifying** (per `verify-before-cite` v1.4 triggers 7c + 8 + 9): facts here are accurate as of 2026-05-19 EOD+; re-verify if days/weeks later. For any merge decision, fire trigger 9 — attempt `git merge --no-commit --no-ff` with audit-tag safety BEFORE generating adjudication options.
4. **Ask Grant**: which adjudication item to action first. Default if not specified: priority ladder item 1 (Soliton-coupling Session 3 with Neptune sub-class refinement). The methodology-systematic adjudication (item 1) is the most physically interesting but has multi-session downstream cascade.
5. **For implementor-session kickoff**: append a `## Phase X (PENDING)` section to the relevant epic doc with assumptions A1-AN, scope boundary, phase plan, adjudication criteria, verification — that's the implementor briefing. Spawn `ave-implementer` agent with `isolation: "worktree"`. **Immediately after spawn, run `git checkout analysis/integration` to defensively avoid the worktree-spawn branch-state leak failure (3rd recurrence this session — pattern, not instance)**.
6. **At session close**: update this file (`index.md`) — bump HEAD ref, audit count, active-epic statuses, closed-epic table, adjudication queue. Per `ave-handoff-canonical-locale` v1.0 discipline.

## Pure-AVE-corpus rule

All content in this directory is pure physics. No external context (no investor / fund / interview references). Tracked files MUST be scrubbed before commit.

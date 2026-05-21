# L3 Migration — Post-Migration TODO

Captures the working state of the `AVE-Core_L3` branch (`analysis/integration`) that sits **outside the primary migration effort** (KB content under `manuscript/ave-kb/` + Python source under `src/`). These are the open issues, parked files, dangling forward-references, and environment reconciliations needed to fully capture the L3 branch's working state once the primary porting passes are done.

Primary effort (tracked elsewhere, NOT in this doc): the round-2 `common`+`vol1` KB port + rescore is complete; the `vol2-6` KB sweep and the `src/` engine/driver migration are primary-but-deferred.

---

## 1. `_orchestration/` directory reconciliation

L3 carries a tracked `_orchestration/` directory: per-epic phase logs, `index.md` (priority ladder + active-epic table + HEAD/tag count), `README.md` (implementor-spawning discipline), and `_orchestration/experimental/<exp>/` sub-epic docs. It is L3's project-management spine.

- The newly-ported root `CLAUDE.md` references it as required first-read (`_orchestration/index.md`, `_orchestration/<epic>.md`, `_orchestration/README.md`) — these are **forward-links** until the dir is dealt with.
- `divergence-test-substrate-map.md` (C11-MACH-ZEHNDER row) links `_orchestration/experimental/c11-mach-zehnder/exp-c11-mach-zehnder.md` + its sim-audit.
- **Decision needed** (deferred per 2026-05-21): port wholesale / port a curated subset / drop and rewrite the CLAUDE.md + leaf references. Figure out what is redundant vs load-bearing once the primary KB+src porting is done.
- **UPDATE 2026-05-21**: `_orchestration/` theirs-only files PORTED wholesale (25 files, byte-identical to L3) in the non-src/non-kb sweep — see §11. The redundant-vs-load-bearing curation + the CLAUDE.md path genericization (§2) remain open; porting was the sane first step (preserves the state; curation is non-destructive afterward).

## 2. Root `CLAUDE.md` environment reconciliation

Ported 2026-05-21 from L3 `analysis/integration`, replacing an **atopile/PCB-design DSL template** that had contaminated `AVE-Core/CLAUDE.md` since the `de9d2293` "Initial release" commit (2026-04-13). The ported doc is the correct AVE orientation, but carries L3/author-specific references that need adapting to this workspace:

- `_orchestration/` paths (see #1).
- Author home paths: sibling repos at `/Users/grantlindblom/AVE-staging/`; memory path `~/.claude/projects/-Users-grantlindblom-AVE-staging/memory/`. This workspace is `/Users/benn/projects/AVE-Umbrella/`.
- Branch-naming / workflow model (`analysis/integration`, `research/l3-electron-soliton`, `audit/<date>_<topic>` tags, `--no-ff` merge pattern, "20 audit tags") — describes L3's orchestration model, not necessarily this branch's.
- Skill-ecosystem references (`~/.claude/skills/ave-*/SKILL.md`) and the orchestration/implementor session split.

**Decision needed**: genericize/repoint the author-specific paths and branch conventions to match this workspace, or trim to a minimal AVE-correct orientation doc.

## 3. `research/` docs

Many round-2 `common`+`vol1` leaves cite `research/2026-05-*` docs (preregs, results, walk-backs) that live outside the KB and are not migrated:

- SPARC 135-galaxy ingest; Gaia DR3 substrate-equilibrium velocity (prereg + result + FLOOR-test + directional); DAMA amplitude prereg/result/walk-back + Q-factor; Chain-B' showstoppers + h-infinity-derivation-audit; cosmic-ε DE projection; SDSS spin-orientation; planetary-scoring Session 2; C5 CMB-axis executable-observer.
- `research/_archive/L3_electron_soliton/` (129 docs, Q-G47 thread) — reference-only per round-1 convention.

**Decision needed**: migrate `research/` wholesale, migrate the cited subset, or treat as external-forward-link (resolve in the cross-reference stitching pass).

- **UPDATE 2026-05-21**: `research/` PORTED wholesale (theirs-only: 94 active docs + `_archive/L3_electron_soliton` 143 + `_archive/L5` 7 + discussions 2) — see §11. The `L3_electron_soliton` archive port closes the predictions-matrix `test_research_doc_exists` regression (17 backing docs for pre_registered predictions now resolve on disk).

## 4. Dangling forward cross-refs from migrated `common`+`vol1` leaves

Migrated leaves point at targets not yet in this branch (dead until the relevant later phase):

- **Other-volume KB leaves**: `vol4/.../project-c11-mach-zehnder.md`; `vol3/.../op14-cosmic-horizon-profile.md`; `vol3/.../saturated-lattice-mutual-inductance.md` (MOND SYM adjudication propagated here in spirit, but the leaf itself is vol3); `vol3/.../dama-alpha-slew-derivation.md`; `vol3/.../gordon-optical-metric.md`; etc.
- **Sibling repos**: `AVE-PONDER/...` (PONDER bench specs), `AVE-Fusion` (REPO-ARCH-6 migration note in `xi-topo-traceability.md`), `AVE-Skills` (closure-roadmap), `AVE-Bench-FemtoElectrometer`.
- **`_orchestration/` links** (see #1).

Resolve in the cross-reference stitching pass after vol2-6 + research + sibling-repo decisions land. (Forward links are intentional threads; only their dead-ness is the open item.)

## 5. Parked working docs (already moved to `session/l3-migration/`)

Not canonical KB leaves; parked verbatim from L3:

- `grants-random-tangents.md` — rolling-capture intuitions inbox (`[OPEN]` entries, append-only).
- `closure-roadmap.md` — process/roadmap doc (re-synced from L3 c7996256).
- `axiom-homologation.md` — spec doc (copied earlier).

**Decision needed**: final disposition — keep parked as session artifacts, promote any to canonical, or discard once their content is otherwise captured.

## 6. Entry-body drift residue — RESOLVED 2026-05-21

All known entry-body drift fixed: `clm-zfqd9v` (c_eff form), `clm-hvvvop` (21→26 + tally), A-034 catalog leaf (SYM 20→19), and `clm-bjceop` (ξ_K1/ξ_K2 closure: added the Sessions-19 closure claim, replaced the stale "STILL OPEN" caveat with the residual k_a/k_s upstream gap, and de-staled the rationale). No remaining known register-entry/leaf drift in `common`+`vol1`.

## 7. Primary-but-deferred pointers (NOT post-migration-misc — listed so they aren't lost)

- **`vol2-6` KB sweep**: 152 pending claims + leaf ports. Held until the `common`+`vol1` sub-0.65 claims are reworked solid (standing hold). Part of the primary KB effort.
- **`src/` migration**: engine + driver corrections that round-2 KB leaves now reference must land — e.g. `ave.gravity.principal_radial_strain` (ε₁₁ = 7GM/c²r), `sparc_catalog_ingest.py`, `gaia_substrate_equilibrium_test.py` + directional, `electron_interferometry_parallax.py` (factor-7 fix), `lbm_3d.py` (viscosity docstring), `q_g47_sessions_19_xi_K_derivation.py`. Part of the primary Python-source effort.

## 8. Experiment DAG-id category (`exp-NNNNNN`) — forthcoming metadata-model extension

Add a new category of DAG id for **physical experiments** to the KB metadata, parallel to the `clm-` claim ids.

- **Id scheme**: experiment ids are generated as `exp-` + 6 alphanum (`exp-[a-z0-9]{6}`). (same as claim-id alphabet)
- **Attachment**: `exp-` ids attach to all *physical experiments* described in the KB.
  - Like unevaluated claims, an **unrun experiment has a solidity contribution of *pending***.
- **Simulations are NOT experiments** — a simulation is part of the existing derivation + claim process (it feeds confidence / derivation-solidity, not experimental-solidity). Only *physical* experiments get `exp-` ids.
- **Physical experiments that validate a claim are inputs to that claim** (a new edge type into the claim node, alongside the existing derivation `depends-on` edges):
  - A physical validation goes **straight to solidity** and **can supersede** the quality/solidity obtained via derivation + simulation.
  - The **experimental solidity** is derived from the strength of the interpretation of the result as applying to / validating the claim:
    - if the experiment produces a result **exactly on-point** for the prediction/claim → experimental-solidity = **1.0** (it worked; it was true).
    - if the result is merely **indicative** of the claim being true → a **subjective call** is required on how strongly the result aligns with the claim.
  - **Combination rule**: $\text{claim solidity} = \max(s_{\text{experimental}}, s_{\text{derivation}})$, where a *pending* solidity maps to **0.0 for the max comparison** (so *pending* does not poison the operation — it simply does not contribute).

**Implementation surface** (derived implications, for scoping — not additional decisions):
- New node type + id scheme in `.index/` JSONL (experiment nodes) and a new edge type (experiment → claim validation input).
- Solidity computation in `kb_index_lib` extended to `max(derivation-solidity, experimental-solidity)` with `*pending* → 0.0`.
- `refresh-kb-metadata` + `verify-kb-metadata` updates; a frontmatter/marker convention for attaching `exp-` ids to physical-experiment leaves (parallel to the `clm-` Tier-1/Tier-2 propagation); and a new `CLAUDE.md` invariant documenting the `exp-` category (parallel to INVARIANT-S8).
- Natural anchor points already in the KB: `appendix-experiments.md` (narrative falsification catalog) and `divergence-test-substrate-map.md` (operational falsification-test index) — the physical experiments enumerated there are the initial `exp-` id population.

## 9. vol2-6 KB migration — DONE 2026-05-21; open decisions surfaced

vol2-6 L3 KB content migrated: **35 new claim-bearing leaves** (vol2:14, vol3:8, vol4:9, vol5:4) + **~73 body-delta merges**, all new claims `confidence: *pending*` (deferred rescore). `verify` PASS (721 files / 289 claims). 435 frontmatter-only diffs were correctly no-action. Decisions surfaced by the waves, NOT yet actioned:

- **vol4 REPO-ARCH restructure — DECIDED + EXECUTED 2026-05-21**: adopted L3's relocation (the canonical organizational decision). Deleted the 30 only-in-ours files (`advanced-applications/` subtree ch7/8/9/10/18/19/20 + 2 loose leaves: `high-q-chiral-antenna` → AVE-HOPF, `ponder-01-stack-netlist` → AVE-PONDER). Removed the 7 orphaned register entries (clm-07wvul, clm-0hwopi, clm-5rigtn, clm-6btlq3, clm-ffa5sq, clm-pcute0, clm-uosu8w); kept the 3 shared claims still cited by surviving leaves (clm-7tynm2, clm-qagkgy, clm-wzezvt). Scrubbed all dangling nav/cross-refs from surviving files (entry-point, vol4/index, ch13/ch17 indexes, vol3-ch11 see-also, divergence-test-substrate-map de-linked to relocation notes). Did NOT create `hardware-programs/` stubs or pull any sibling-repo content (extending KB coverage to private sibling repos is out of remit). verify PASS, zero dangling links KB-wide.
- **Neutrino model — ours canonical, NO back-port (RESOLVED)**: L3 is transitional (its `analysis/integration` + `research/l3-electron-soliton` branches will be deleted; this branch PRs to main as canonical) — there is no back-port to L3, ever. Our branch carries the helical-torsional-screw-dislocation neutrino body language + 2026-05-06 Corrigendum; L3 kept the merge-base "$0_1$ twisted unknot" framing and added only the FI-13 PMNS scope-correction (c₁=5 derivation-gap honesty + σ-tension columns + JUNO falsifier). The migration kept our body language and ported L3's FI-13 (clean 3-way merge across delta-cp-violation, ch03 index, particle-physics index). Physics-authority verification tracked as a post-merge item — see §10.
- **Migration-direction audit (2026-05-21, RESOLVED — zero regressions)**: the vol2-6 survey used direction-agnostic content-diff, which over-includes files where *we* are ahead. Git-merge-base audit (mb `05e2a45`) cleared the entire 114-file body-delta set: 38 were purely ours-ahead (agents left 31 untouched; the 7 "modified" had only `subtree-claims` auto-regenerated by refresh — no content reverted); our only physics-content divergence since mb was the electron-body/unknot corrigendum, touching exactly the 3 neutrino-sector leaves above (all flagged + correctly merged). No silent regressions. **Methodology note for future syncs: gate candidate selection on git merge-base direction (L3-changed / ours-ahead / both-changed), not raw content-diff.**
- **Rigor-regression deletions KEPT (L3 silently dropped, not applied)**: vol2 thermal-softening Gaussian-ansatz caveat + app-c saturation qualifier; vol3 `einstein-field-equation.md` (L3 simplification conflicts with our $Z_0$-invariance theorem — left entirely unchanged) + vol3/index Hubble caveat; vol4 `ybco-phased-array` + autoresonant-breakdown INVALIDATED headers; vol5 repo-scope-note + consciousness-cavity dangling-link; vol6 `radioactive-decay-impedance` (L3 added a "~11.3 MeV" figure while deleting our empirical-magnitude guardrail — 11.3 MeV doesn't match the tritium→He-3 Q-value ~0.529 MeV; likely L3 error). Review individually if desired.
- **Claim-state shifts ported (affect rescore solidity)**: vol4 `geo-synchronous-impedance` + `sagnac-parallax` flipped positive-forward-prediction → corroborative-null; `project-hopf-02` Snell-parallax derivation dropped by L3 (→ deferred HOPF-03 sub-epic).
- **L3 error reverted**: vol4 `tabletop-graveyard` Axiom 2→1 (kept correct Axiom 2 per INVARIANT-S2).
- **Inherited dangling relative-links** (→ folds into §4 cross-ref stitching): vol3 new BH leaves → `common/` targets; vol5 new protein-folding leaves → `../../common/` wrong depth (catalog actually at KB-root `common/`); a few L3-source path-depth bugs were fixed inline by the vol3 wave.

(Section 7 "vol2-6 KB sweep": the *migration* is now done; the *rescore* of the resulting pending claims remains on the standing hold.)

## 10. Post-merge verification items

- **Neutrino body-wording ↔ PMNS-derivation coherence (physics authority)**: confirm our helical-torsional-screw-dislocation neutrino body language (2026-05-06 Corrigendum) is consistent with the c₁=5 / c₃=9 torus-knot PMNS mixing derivation that L3's FI-13 scope-correction audits. The two appear orthogonal (body-topology vs mode-space crossing numbers), but verify the merged leaves (`delta-cp-violation.md`, `ch03-neutrino-sector/index.md`, `particle-physics/index.md`) read coherently.
  - **Blast radius: low / bounded.** The 2 neutrino claims (`clm-7o8clt` PMNS angles + δ_CP; `clm-rji99i` mass/hierarchy) are DAG terminals — zero depends-on edges point into them. `clm-rji99i` is co-cited by `lepton-spectrum.md` (ch06). Only conceptual coupling: the aggregate "26 SM parameters" (`clm-xhdai6`) + zero-parameter-closure (`clm-sxn6eo`, `clm-ibfyda`) scorecards include the 4 PMNS params + 3 neutrino masses, so a body-wording inconsistency would touch those scorecard rows but does NOT propagate solidity through the DAG. Verification is self-contained to the neutrino sector + those scorecard rows.

## 11. Non-src / non-kb migration sweep — 2026-05-21

Full tabulation of L3 (`analysis/integration` @ `c7996256`) changes **outside** `src/` and `manuscript/ave-kb/` since merge-base `05e2a45`. Direction split (git-merge-base, per the §9 methodology): **357 theirs-only · 27 both-changed · 13 ours-ahead**.

### Ported 2026-05-21 — 356 theirs-only, byte-identical to L3 (verified 0 mismatches)
- `research/_archive/L3_electron_soliton/` (143) — **includes the 17 predictions-backing docs** → closes the `test_research_doc_exists` regression.
- `research/` active docs (94); `research/_archive/L5` (7) + `discussions` (2).
- `assets/` (21), `_orchestration/` (25 — see §1), `results/` (7), `data/` pantheon_plus + sdss_dr17 (6), `.claude/` (8), `docs/` (2).
- `manuscript/*.tex` theirs-only (38 — "L3-only changes and new docs" per Grant 2026-05-21).
- `manuscript/predictions.yaml` (the regression fix: 33→80 entries, 0→44 pre_registered; ours' IDs were a strict subset of L3's).
- root theirs-only (2).

**predictions regression CLOSED**: ours now passes all 356 predictions-matrix + v_snap tests that L3 passes (zero L3-pass-but-ours-fail violations). `test_count_matches_expected` still fails — but it fails on L3 too (44 pre_registered ≠ hardcoded EXPECTED 10), so it is allowed under the "green-on-L3 ⇒ green-here" rule.

### Protected — 13 ours-ahead (NOT ported; ours is newer)
`pyproject.toml`, `uv.lock`, `.github/workflows/{build_pdf,verify}.yml`, `.claude/{kb-docent.md, commands/kb-next.md, commands/kb-start.md}`, and `.tex`: `backmatter/{01_appendices, 05_universal_solver_toolchain}`, `common/translation_particle_physics`, `vol_0/02_analytical_summaries`, `vol_1/03_quantum_and_signal_dynamics`, `vol_2/03_neutrino_sector`.

### QUEUED — both-changed reconciliation pass (dedicated, KB-leaf-referenced)
27 both-changed files need a true 3-way reconciliation. **The 23 `.tex` must be reconciled against the canonical KB leaves already ported** to nail final language (the leaf is canonical; the `.tex` is derived per [[kb-canonical-not-tex]]).

**Critical methodology (Grant 2026-05-21):** for each both-changed `.tex`, check whether L3's `.tex` carries edits dated *later* than L3's last edit to the corresponding KB leaf. In theory the leaf is always newer (canonical) and the `.tex` merely lags; in practice **verify per-file** — a `.tex` newer than its leaf may carry physics content never captured in the canonical leaf ("reality eats cornflakes out of theory's skull").
- **Neutrino — CHECKED, CLEAN:** L3 leaf `vol2/.../ch03-neutrino-sector` (2026-05-17, FI-13) is *later* than L3 `vol_2/.../03_neutrino_sector.tex` (2026-04-19). KB newer; no `.tex`-ahead risk. (Our neutrino `.tex` is ours-ahead regardless.)
- **Risk window:** the 23 both-changed `.tex` were L3-edited **2026-05-15 … 05-19** — squarely inside the KB-closure window. Per-file date checks are therefore mandatory, not pro-forma. Latest-edited (highest risk first): `frontmatter/00_foreword`, `backmatter/02_full_derivation_chain` (both 05-19 22:10); `vol_1/{01_fundamental_axioms, 04_continuum_electrodynamics}` + `vol_3/04_generative_cosmology` (05-19 18:08); then the 05-16/05-17 cluster.

**both-changed `.tex` (23):**
  - manuscript/backmatter/02_full_derivation_chain.tex
  - manuscript/backmatter/12_mathematical_closure.tex
  - manuscript/backmatter/appendix_c_derived_numerology.tex
  - manuscript/backmatter/appendix_vacuum_engineering.tex
  - manuscript/common/translation_gravity.tex
  - manuscript/common_equations/eq_axiom_1.tex
  - manuscript/common_equations/eq_axiom_2.tex
  - manuscript/common_equations/eq_axiom_3.tex
  - manuscript/common_equations/eq_axiom_4.tex
  - manuscript/common_equations/eq_calibration_constants.tex
  - manuscript/common_equations/eq_gravity_derived.tex
  - manuscript/frontmatter/00_foreword.tex
  - manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex
  - manuscript/vol_1_foundations/chapters/02_macroscopic_moduli.tex
  - manuscript/vol_1_foundations/chapters/04_continuum_electrodynamics.tex
  - manuscript/vol_1_foundations/chapters/05_universal_spatial_tension.tex
  - manuscript/vol_1_foundations/chapters/07_regime_map.tex
  - manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex
  - manuscript/vol_2_subatomic/chapters/02_baryon_sector.tex
  - manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex
  - manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex
  - manuscript/vol_3_macroscopic/chapters/20_white_dwarf_predictions.tex
  - manuscript/vol_4_engineering/chapters/11_experimental_falsification.tex

**both-changed config/root (3 — simple 3-way merge, NOT KB-leaf reconciliation):** `.gitignore`, `Makefile`, `LIVING_REFERENCE.md`. (`CLAUDE.md` — the 4th both-changed root file — already ported, §2.)

### L3 deletion — pending decision (1)
`manuscript/frontmatter/00_foreword_lean.tex` — L3 deleted it (lean-foreword variant; the main `00_foreword.tex` is both-changed). Not deleted unilaterally (destructive op on manuscript content). Adopt the deletion per the vol4 REPO-ARCH canonical-decision precedent (§9), or keep — confirm before removing.

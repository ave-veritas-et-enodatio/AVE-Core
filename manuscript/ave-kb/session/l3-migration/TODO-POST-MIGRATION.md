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

### Ownership + edge-direction architecture (Grant canonized 2026-05-21 — design basis for the exp-id sweep)

These principles emerged from the `n_spatial` reconciliation (the `clm-rd9cjm` case below) and govern how the exp-id sweep wires experiment→claim edges. Promote to `CONVENTIONS.md` / `claim-quality.md` preamble **when the edge-class tooling is built** (don't canonicalize an invariant whose enforcement doesn't exist yet).

1. **Ownership = earliest-asserting claim, not the deriving volume.** A claim id is anchored where a proposition is first asserted *as a claim* (with a `### Quality` block) — not where it is later derived. A bare assertion is owned at birth (low confidence per the rubric: `0.1` "asserted without supporting derivation", or `*pending*` if unassessed/deferred-debt); a later derivation in any volume **strengthens** it. Reuses the existing solidity mechanism — no new quality rule (the `0.1`/`0.3`/`*pending*` bands already cover the assertion/ansatz spectrum). A pure ansatz *as a claim* is `0.1`/`*pending*`; the claim that derives a result *given* the ansatz is a separate, higher-confidence node with the ansatz as a `depends-on`.
2. **Two edge classes, two directions:**
   - **Hand-authored edges (`depends-on` / built-on, and `strengthens`) point ≤ current volume** — a human only ever references backward toward foundations. This makes the authored graph volume-monotone ⇒ acyclic by construction ⇒ volume order is a topological order.
   - **Reverse views (`strengthened-by`, `cited-by`, `subtree-claims`) are machine-generated bookkeeping** and may point forward (higher volume). Never hand-authored.
3. **Derivations and experiments are both backward `strengthens` inputs.** A physical experiment is not a claim that originates physics — it is a falsification/validation input that *targets* (strengthens) the claim it tests. This is why the Mach-Zehnder experiment should not own a `clm-` re-asserting the decomposition (see below).
4. **Audit blind spot:** the recorded `depends-on` DAG is already volume-monotone across numbered volumes (0 upward edges, verified 2026-05-21), but the `n_spatial` anomaly was a **prose forward-reference**, invisible to the edge check. A complete ownership audit must also grep leaf *bodies* for upward cross-volume references, not just the edge graph.

### `clm-rd9cjm` (refractive-index decomposition) ownership — DECISION DEFERRED to exp-id sweep

Resolved now: the `n_spatial` form was corrected to the canonical "1+" (`n_s = 1 + (9/7)ε₁₁`, `n_t = 1 + (2/7)ε₁₁`, `Δn = ε₁₁`) across all 9 source files; `verify-kb-metadata` PASS. Two structural items remain for the sweep:
- **(i) vs (ii) ownership:** today `clm-rd9cjm` is owned in vol3 (gravity); vol2 ch7 asserts the decomposition in prose (in support of its interferometry prediction `clm-qde5gn`) and forward-cites vol3 — an upward prose reference. **(i)** keep vol3 ownership, treat vol2 ch7's use as Axiom-3-direct (no upward claim edge); **(ii)** relocate ownership to the earliest assertion (vol2) per the architecture above, recast vol3's trace-reversal derivation as a backward `strengthens` edge. (ii) is principled but relocates a claim cited by ~25 vol3 leaves. Decide with the sweep.
- **`clm-6kqvyp` (C11-MACH-ZEHNDER) is a physical experiment mis-modeled as a `clm-`** (no exp-id category existed). Reclassify to `exp-…` targeting `clm-rd9cjm`; it should *reference* the decomposition, not re-assert it. **Do NOT wire a claim→claim `depends-on` edge in the interim** — it would be undone by the exp-id remap. **DONE 2026-05-22 → `exp-7jekc6`.**

### exp- population pass — classification locked 2026-05-22 (ACTIVE pass)

**The `exp-` gate (Grant, 2026-05-22):** an `exp-id` is assigned ONLY to an experiment **we design, originate, and control** — physical apparatus/project, even if unbuilt/facility-class and `status: pending`. "Physical apparatus + measurement" is necessary but not sufficient; authorship/control is the deciding axis.
- **NOT `exp-`:** data re-analyses of outside measurements (LIGO ringdown, CMB axis, SPARC) and kill switches tested by others' facilities (C6 neutrino parity, C7 GRB dispersion) — we are *analytical consumers*. These are `sup-` work (see S10 below), NOT experiments. Simulations remain derivation-side (unchanged).
- **PONDER-01/02/05 deferred** to the "other repos later" bucket (no dedicated AVE-Core experiment leaf; canonical apparatus lives in AVE-PONDER).

**Conversion set (this pass — 10 leaves → `kind: experiment`, all `status: pending`).** Each converts on the `clm-6kqvyp` template (frontmatter → `kind: experiment` + `exp-id` + `status` + `strengthens:`; remove the experiment-as-claim entry from `vol4/claim-quality.md`; `refresh`):

| leaf | clm- (retire) | strengthens (surviving physics claim) |
|---|---|---|
| project-hopf-02 | clm-wzezvt ⚠ | clm-oygz1i (topological mass / Hopf charge) |
| sagnac-rlve | clm-wqmb19 ⚠ | clm-qx9bb8 (material-dependent entrainment law) |
| project-roentgen-03 | clm-qsgl7d | clm-qx9bb8 |
| sapphire-phonon-centrifuge | clm-iz3svl | clm-qx9bb8 |
| project-zener-04 | clm-cltls0 | clm-pp3qwf (E⁴ vs E² birefringence) |
| vacuum-impedance-mirror | clm-5s5b0d | clm-pp3qwf |
| metric-levitation-limit | clm-ui3m8a *(keep)* | clm-ui3m8a (√α yield limit — self) |
| metric-refraction-capacitor | clm-ui3m8a *(keep)* | clm-ui3m8a |
| project-cleave-01 | clm-ydksh6 | clm-dfaiwj (TKI [Q]≡[L]) |
| project-torsion-05 | clm-kl1ern | clm-2dwzib (V_snap vs V_yield thresholds) |

- **Decision A (locked):** clm-ui3m8a (√α yield limits) stays the physics claim; only the two genuine apparatus leaves (metric-levitation, metric-refraction-capacitor) convert and strengthen it. ybco-phased-array (Tier-D mechanism) + zero-parameter-derivations (meta) remain plain `clm-` citers — NOT converted.
- **⚠ Two shared experiment-as-claims are NOT pure-deletes** (unlike clm-6kqvyp which had no citers): `clm-wqmb19` is also cited by `sagnac-parallax` (C17 null) + `active-sagnac-impedance-drag` (ch12 prediction); `clm-wzezvt` is also cited by `open-source-hardware` (meta). Conversion = **re-point those sibling leaves' `claims:` to the surviving physics claim** (clm-qx9bb8 / clm-oygz1i), not orphan them.
- **Stays `clm-`:** kill switches (clm-gw2wgc); predictions (clm-pp3qwf, clm-to41c7, clm-trgqtf, clm-9sujp8, clm-i02mhk, clm-qx9bb8, + C2/C8/C10/C12/C14/C19); meta (clm-om0rtq, clm-fh6w3y, clm-baoa36, clm-oiw6cb, clm-p12mem, epistemology leaves); corroborative-null C17/C18; Tier D D1–D5.

### INVARIANT-S10 (`sup-` support nodes) — DESIGN LOCKED 2026-05-22, BUILD QUEUED after the exp- pass

A `sup-` node represents **non-physical analytical work that strengthens an existing claim without originating a new one** — parallel to `exp-` but on the *other* branch of the two-branch solidity model.

- **`sup-` is non-physical / derivation-side.** Its `strengthens` edge slots into the **derivation branch (min-side)**, lifting the target claim's **local quality** (the `confidence` baseline). It does NOT touch `experimental_solidity`. (`exp-` = physical, max-branch, empirical; `sup-` = analytical, min-branch, local-quality. They plug into opposite halves of the model with opposite pending-semantics — so two distinct node types, NOT one type with an `origin` field.)
- **Pending logic (refined):** a **pending** `sup-` contributes nothing and **never NaN-poisons** a claim that already has valid quality/solidity (a strengthening attempt is non-load-bearing; pending-poison flows only from load-bearing derivation *dependencies*). A **done** `sup-` lifts `local_quality`.
- **Mechanic:** `derivation_solidity = local_quality × min(dep solidities)`, where `local_quality` is the authored `confidence` lifted by *done* `sup-` contributions; `solidity = max(derivation_solidity, experimental_solidity)`. A `sup-` lift "may or may not" move final solidity — `min(deps)` can cap it and `max(experimental)` can override it.
- **Bright line `sup-` vs. citation:** a `sup-` exists iff *additional work or an on-point observation that justifiably adds weight* was done; a passive reference is not a `sup-`.
- **Scope / what is NOT a `sup-`:** (a) pure derivation improvement to an existing claim → edit the claim at source; (b) strengthening that is a byproduct of a *later* claim → that later `clm-` is already the node. `sup-` is for: outside-data re-analyses with no other home (LIGO/CMB/SPARC; C5 Outcome-D becomes a `done`-but-low-strength `sup-`), and the **exploratory** workflow (park free-standing strengthening work as a node to chase an idea).
- **Deletability requirement:** `sup-` nodes must be safely dissolvable — the author can later fold the work back into the source claim and delete the node without breaking referential integrity (a derivation-flavored `sup-` folded into canonical derivation is the correct signal of a reorg, not a bug).
- **Build arc (mirror S9):** `.index/SCHEMA.md` `sup-` node + derivation-branch `strengthens` edge; `kb_index_lib` local-quality computation; `refresh`/`verify` extensions; frontmatter convention; new `INVARIANT-S10` in KB `CLAUDE.md`; fixtures + e2e + negative tests exercising the pending-non-poison path. **Do this as its own pass, after the exp- population pass lands.**

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

### DONE 2026-05-21 — both-changed reconciliation pass (21 files; 1 held)

Refined scope: 6 of the original 27 had **converged** (HEAD == L3, no action): `CLAUDE.md` (ported earlier) + 5 `eq_axiom_{1,2,3,4}.tex` / `eq_calibration_constants.tex` (both sides independently reached identical content — verified `base≠ours`, `base≠theirs`, `ours==theirs`). Real reconciliation set = **21** (3 config + 18 `.tex`).

**Method:** 3-way merge (base = merge-base `05e2a45`, ours = HEAD, theirs = L3), conflicts adjudicated against the canonical (converged) `eq_axiom_*.tex` and KB leaves. Outcomes:
- **Config (3):** `.gitignore` clean union (= L3 superset; carries the data-allowlist our ported pantheon/sdss data needs + our mad-review/guest-session/*.tgz). `Makefile` combined (theirs's `verify_atomic_ie` line + ours's `verify-kb-metadata`/`refresh`/`framing-audit` targets + ours's hardened critical-tier defense gate). `LIVING_REFERENCE.md`: ours's axiom block kept — it matches canonical (`Substrate Topology`/`Minimum Reflection`); **L3's was stale** (`Impedance`/`Gravity`) despite L3's own `eq_axiom_*.tex` being current.
- **`.tex` clean auto-merges (9):** all preserved ours's honesty/rigor + axiom-homologation corrections (α-is-consistency-not-derivation, Neon-20 one-fitted-scalar + R 72→81d, Gaussian-ansatz gap, Higgs VEV +1.1%, gravity-derived-from-Ax1+4) AND gained L3's orthogonal A-034/engine-pointer enrichments. Verified non-contradicting.
- **`.tex` conflicts resolved (8):** `00_foreword`, `08_alpha_golden_torus`, `04_generative_cosmology`, `02_full_derivation_chain` → **theirs** (canonical-correct framing / corrigendum-consistent / strict superset; ours was stale on the axiom names in the two backmatter files). `11_experimental_falsification`, `01_fundamental_axioms` → **ours** (01: theirs's summary recap reverted to stale axiom names — ours is internally consistent + numbered + references A-034). `appendix_vacuum_engineering` → ours's correct axiom-attribution column + theirs's "; A-034" enrichment. `12_mathematical_closure` → **combined**: kept ours's crown-jewel "Explicit Closure DAG + Outstanding Rigour Gaps" honesty block, appended theirs's "A-034 Empirical Anchors" section, fixed the stale "Gravity (Axiom 3)" attribution → "(derived from Axioms 1 & 4)".

**✅ RESOLVED 2026-05-21 — `eq_gravity_derived.tex` (`n_spatial` divergence):** adopted the "1+" form corpus-wide (Grant call, by time/clarity + physical correctness — the "1+" form is the later 2026-05-17 deliberate cleanup, gives `Δn = ε₁₁`, and reduces to `n=1` in flat vacuum). Corrected across **9 source files**: `eq_gravity_derived.tex` (took L3), `translation_gravity.tex`, `common/translation-tables/translation-gravity.md` (canonical KB leaf), `temporal-spatial-lattice-decomposition.md` (`clm-rd9cjm` + fixed its stale `eq_axiom_3.tex`→`eq_gravity_derived.tex` source pointer), `vol3/gravity/index.md`, `vol3/gravity/ch01-gravity-yield/index.md`, root + vol2 + vol3 `claim-quality.md`. `.index` regenerated (solidity/subtree unchanged — pure content fix); `verify-kb-metadata` PASS. Ownership/edge architecture + the `clm-rd9cjm` (i)/(ii) + `clm-6kqvyp`-reclassification follow-ups logged in §8. Original analysis retained below.

**(superseded) ⚠ HELD — `eq_gravity_derived.tex` (`n_spatial` divergence, needs Grant's physics-authority call + a corpus-wide sweep):**
The genuine "cornflakes" case. The KB is **internally inconsistent** on the spatial gravitational refractive index:
- **bare** `n_spatial = (9/7)ε₁₁`: canonical decomposition leaf `clm-rd9cjm` (`vol3/.../temporal-spatial-lattice-decomposition.md`), `vol3/gravity` indexes, `common/claim-quality.md`, and `translation_gravity.tex` (ours).
- **`n_spatial = 1 + (9/7)ε₁₁`**: vol4 Mach-Zehnder leaf `project-c11-mach-zehnder.md` (the C11 falsifiable prediction) + `vol4/claim-quality.md` + L3's `eq_gravity_derived.tex` (2026-05-17 "parallelism" cleanup, explicitly reasoned: both indices carry the DC "1+", index →1 in flat vacuum, fixes driver-script confusion).

Only the "1+" form yields the published `Δn = n_s − n_t = ε₁₁` (bare gives `ε₁₁ − 1`) and behaves as a physical refractive index (→1 in flat vacuum). So L3's `.tex` is **ahead** of the canonical decomposition leaf, which still carries the "shorthand" bare form. This is exactly the `.tex`-newer-than-leaf case. **Decision needed:** adopt "1+" form corpus-wide — update `eq_gravity_derived.tex` (take L3), `translation_gravity.tex` (already merged with bare form — would need re-edit), and the canonical leaf `clm-rd9cjm` + vol3 indexes — so the whole corpus matches the physically-correct Mach-Zehnder form; OR confirm the bare form is intended shorthand and reconcile the Mach-Zehnder leaf the other way. Touches a claim (`clm-rd9cjm`) + a falsifiable prediction → not resolved unilaterally.

**Residual corpus item (not a merge conflict):** L3 prose retains some stale "Axiom 3 = gravity / Effective Action" references (e.g. `appendix_c_derived_numerology.tex` intro: "G from the Machian boundary condition of Axiom 3") that the canonical `eq_gravity_derived.tex` + `eq_axiom_3.tex` supersede. A corpus-wide prose-consistency sweep for stale axiom-name references is a separate follow-up (the canonical single-source `eq_axiom_*.tex` are correct; only derived prose mentions lag).

---
**(Original queue notes retained below for reference.)**

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

### L3 deletion — RESOLVED 2026-05-21 (adopted)
`manuscript/frontmatter/00_foreword_lean.tex` — L3 deleted it (lean-foreword variant). **Deletion adopted** (Grant 2026-05-21) per the vol4 REPO-ARCH canonical-decision precedent (§9). Confirmed zero `\input`/references anywhere in ours or L3 before removal; the main `00_foreword.tex` survives.

## 12. KB Markdown link-integrity checker — DEFERRED tooling (build after KB-usage unblocking)

A standing crawler to permanently close the broken-cross-reference class surfaced during migration (off-by-one `../` depths, parked-doc relocations, sibling-repo staleness). **Build this AFTER the immediate KB-usage blockers are cleared** (the over-counted `../` links, the parked-doc disposition, the Grant-home `file://` link). Design (Grant 2026-05-23):

- **`tools/verify-md-links.py`** crawls **ALL markdown in the repo** (not just `manuscript/ave-kb/`) — KB leaves, docs, READMEs, `research/`, `_orchestration/`, etc. For each markdown link target, resolve relative to the file's dir and check existence (strip `#anchor` + trailing `:linenum`; skip `http(s)`/`mailto`/absolute).
- **Doc/example links are checked too** (Grant 2026-05-23): the checker is repo-wide precisely so it catches broken links in documentation `.md` (e.g. the over-counted `../claim-quality.md` / `../entry-point.md` snippets in `CONVENTIONS.md`/`CLAUDE.md`). Do NOT blanket-skip fenced code blocks. **Open sub-design:** distinguish genuine illustrative *placeholders* (e.g. `relative/path/to/target.md`, which can never resolve) from real-looking-but-broken links — options: a recognized sentinel/placeholder convention exempted from checking, or rewrite doc examples to use resolvable real paths. Real-looking broken links in docs are caught and fixed.
- **Exhaustive:** displays **all** broken links by **file + line number** (does NOT exit on first error).
- **Exit code:** `1` if any broken links, `0` if none.
- **Intra- vs inter-repo split:** by default **errors** on broken **intra-repo** links (targets within AVE-Core: `manuscript/`, `research/`, `_orchestration/`, `src/`) and **warns** on broken **inter-repo** links (sibling repos: `../AVE-HOPF`, `../AVE-QED`, `../AVE-Metamaterials`, … — these can legitimately be stale/in-flux). An option selects inter-repo handling: **don't-check | warn-if-broken | error-if-broken**.
- **Make targets:** `verify-md-links` runs with inter-repo = **warn**, and is added as a dependency of the `verify` target (alongside `verify-kb-metadata`). `verify-inter-repo-links` runs with inter-repo = **error** (the strict cross-repo gate, run when sibling-repo state is expected current).
- (Future extension, not v1: anchor (`#section`) validation.)

## 13. closure-roadmap → external DAG-consumer relocation (IN PROGRESS, Grant 2026-05-23)

`closure-roadmap.md` is a **manually-maintained todo list** — its status-dashboard layer is redundant with claim-DAG-derivable stats (weakest via `ave-kb weak-points --max-solidity`, highest-leverage via `--min-dependents`), but it also carries irreplaceable human **notes + intentions** + a research-action plan keyed by `L5`/`Q-G`/`A-` thread ids (NOT `clm-` ids currently). Architecture decision: make it a one-directional **external consumer of the claim DAG** — it points *into* the graph by id; the KB never points back at it.

Sequence:
1. **DONE (`ef2fcfb7`)** — de-linked the 27 KB→roadmap markdown links (wrong-direction status pointers; status is intrinsic to a claim's `*pending*` solidity).
2. **NEXT** — hand-clean the ~23 residual *plain-text* `` `closure-roadmap.md` `` path mentions in KB leaves (remove the "tracked at closure-roadmap §X/Tier N" clause, keep the "open work / open gap" status prose; per-instance — clauses vary, not regex-safe).
3. `git mv session/l3-migration/closure-roadmap.md → manuscript/ave-kb/claim-quality-closure-roadmap.md`; re-relativize its outbound KB links (authored relative to `common/`; from the new ave-kb-root location each loses one `../`); fix line-1 up-link (→ `entry-point.md`); add `claim-quality-closure-roadmap.md` to `verify-kb-metadata.py` `EXCLUDE_NAMES` (it's a reference/planning doc, not a claim-bearing leaf — like `claim-quality.md`).
4. `ave-kb/README.md` note: document the doc's purpose (**human staging area for claims-to-work-on + how-to-proceed ideas**) + one sentence on extracting the DAG stats it partly mirrors (`ave-kb weak-points`: `--max-solidity` for weakest, `--min-dependents` for highest-leverage).
5. Add `clm-`/`exp-`/`sup-` ids to the roadmap entries — connect each action item to the claim(s) it concerns (roadmap → DAG by id).
6. **New verification** — a consumer-side id-validity check: every `clm-`/`exp-`/`sup-` id cited in the roadmap (and, generally, any external DAG-consumer doc) must resolve to a real node in `.index/claims.jsonl`. One-directional (no back-pointer / no leaf-citation coverage required). Fold into `verify-md-links` (§12) or a small dedicated check.

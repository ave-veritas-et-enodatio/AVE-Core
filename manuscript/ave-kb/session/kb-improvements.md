# AVE-KB Improvements / Remaining Work

Running list of open work scoped specifically to the AVE-KB (canonical markdown tree at `AVE-Core/manuscript/ave-kb/`). Broader design questions about future agentic systems live elsewhere; items here are about making the existing KB better as it stands. Completed items are removed — git history holds them.

> Absorbed the post-L3-migration remaining-work tracker 2026-05-23 (the migration burndown itself is complete: exp- population, the `sup-` node type, the cross-reference / corpus-purity / orientation nav cleanup, and the planning-doc decoupling all landed). Lives in `session/` (excluded from `verify-kb-metadata`). Deep design specs for the metadata spine live in the auto-memory entry `project_kb_exp_id_design` and in git history.

---

## Near-term (sup- claims + md-link tooling branch)

### N1. Populate the real `sup-` nodes
The S10 `sup-` support-node type is built. Populate the confirmed outside-data re-analyses as `sup-` nodes (one-directional analytical support; derivation-branch, non-physical):
- C1 LIGO ringdown (PASS −0.45%, 2026-05-18) → supports `clm-395gps` (ω_R M_g = 18/49).
- C13a SPARC galactic rotation (CONFIRMED 15.5%, 2026-05-17) → supports `clm-u86caq` (MOND a₀).
- C5 CMB axis (Outcome-D, 2026-05-19) → supports the cosmic-axis claim.
- **Host** the `sup-` ids in `common/divergence-test-substrate-map.md` (the C1/C5/C13a rows; already claim-bearing), with `### Quality` entries in `common/claim-quality.md`.
- **Propagate, not evaluate** — both `quality` and the `supports` on-point `fraction` land `*pending*`.
- **PREREQUISITE (tooling extension):** the S10 build hard-requires `supports` `fraction ∈ (0,1]` (parse raises at `kb_index_lib.py:1199`; verify rejects at `verify-kb-metadata.py:681`). Extend parse/compute/verify/materialization to accept a `*pending*` fraction — a sentinel distinct from the `null` that marks a `depends` edge; a pending fraction contributes nothing and never poisons (parallel to pending quality).

### N2. `verify-md-links` checker (+ wire into `verify`)
Repo-wide Markdown link-integrity crawler (`tools/verify-md-links.py`):
- Crawls **all** `.md` in the repo (not just `manuscript/ave-kb/`). Resolve each link relative to its file; strip `#anchor` + trailing `:linenum`; skip `http(s)`/`mailto`/absolute.
- **Exhaustive** — reports every broken link by **file + line** (no exit-on-first); exit `1` if any, `0` if none.
- **Intra- vs inter-repo:** default **error** on broken intra-repo links (within AVE-Core: `manuscript/`, `research/`, `_orchestration/`, `src/`); **warn** on broken inter-repo links (sibling repos `../AVE-HOPF`, `../AVE-QED`, `../AVE-Metamaterials`, … — legitimately stale/in-flux). Option `{dont-check | warn | error}` for inter-repo.
- **Checks doc/example links too** (catches over-counted snippets in `CONVENTIONS.md`/`CLAUDE.md`). Open sub-design: distinguish genuine placeholders (`relative/path/to/target.md`) — sentinel exemption vs make-resolvable.
- **Make targets:** `verify-md-links` (inter=warn) added as a dependency of `verify` alongside `verify-kb-metadata`; `verify-inter-repo-links` (inter=error) for the strict cross-repo gate.
- **Folds in the consumer-side id-validity check (N3):** every `clm-`/`exp-`/`sup-` id cited by an external DAG-consumer doc must resolve to a node in `.index/claims.jsonl`. One-directional (no back-pointer required).

### N3. closure-roadmap → external DAG consumer (finish)
The move + de-link are DONE (`claim-quality-closure-roadmap.md` at KB root, links re-relativized, verify-excluded). Remaining: **add `clm-`/`exp-`/`sup-` ids to its entries** (it currently keys by `L5`/`Q-G`/`A-` thread ids) so it points INTO the DAG by id — a one-directional external consumer; the KB never points back. The N2 id-validity check then guards it.

---

## Deferred

### D0. KB-vs-LaTeX divergence as a staleness signal
The KB markdown tree is canonical; the LaTeX manuscript (`manuscript/vol_*/`) is a derived publication artifact (effective 2026-05-07; documented in `kb-docent.md` "Canonical Source" + INVARIANT-S7). **Open:** decide whether to add a verifier step that flags KB-vs-LaTeX divergence as a *derivation-staleness* signal ("the LaTeX has not caught up to this leaf") rather than a KB error. No automated LaTeX-lag detection currently exists.

### D1. vol2-6 claim-quality rescore
~152 `*pending*` claims. **Standing hold** behind the sub-0.65 vol1+common rework. (Once scored, `ave-kb weak-points` can rank weakest / highest-leverage claims directly — superseding the manual closure-roadmap status layer.)

### D2. `src/` engine + driver migration
Round-2 KB leaves reference engine functions that must land: `ave.gravity.principal_radial_strain` (ε₁₁ = 7GM/c²r), `sparc_catalog_ingest.py`, `gaia_substrate_equilibrium_test.py` + directional, `electron_interferometry_parallax.py` (factor-7 fix), `lbm_3d.py` viscosity docstring, `q_g47_sessions_19_xi_K_derivation.py`.

### D3. `clm-rd9cjm` (i)/(ii) ownership
Keep vol3 ownership (i) vs relocate to vol2 earliest-assertion (ii). Defer with the quality pass.

### D4. `n_spatial` corpus-prose sweep
Stale "Axiom 3 = gravity" references in derived prose (canonical `eq_*` are correct; prose lags).

### D5. Upstream `depends-on` edges (quality pass)
`clm-wzezvt→clm-oygz1i`, `clm-ydksh6→Ax2 clm-dfaiwj`, `clm-kl1ern→Ax4 clm-2dwzib`, etc. — deferred to claim-quality evaluation.

### D6. INVARIANT-S9 doc clause
Add the "experiments we design / originate / control" gate to S9 text in `CLAUDE.md` + `.index/SCHEMA.md` (currently says only "physical experiment (apparatus + measurement)", which under-specifies — would wrongly admit outside-data re-analyses).

### D7. `_orchestration/` curation
Redundant-vs-load-bearing pass over the wholesale-ported `_orchestration/` files.

### D8. Strip redundant identification-system remnants
The now-deprecated `axiom-homologation.md` (`session/`) called for unifying the framework's identification systems; the unified `clm-`/`exp-`/`sup-` metadata spine fulfilled that. Its residual value is a pointer to *strip out truly redundant/unnecessary identification-system remains* still scattered in the corpus. (Mine the historical doc for specifics when picked up.)

# AVE-KB Improvements / Remaining Work

Running list of open work scoped specifically to the AVE-KB (canonical markdown tree at `AVE-Core/manuscript/ave-kb/`). Broader design questions about future agentic systems live elsewhere; items here are about making the existing KB better as it stands. Completed items are removed — git history holds them.

> Absorbed the post-L3-migration remaining-work tracker 2026-05-23 (the migration burndown itself is complete: exp- population, the `sup-` node type, the cross-reference / corpus-purity / orientation nav cleanup, and the planning-doc decoupling all landed). Lives in `session/` (excluded from `verify-kb-metadata`). Deep design specs for the metadata spine live in the auto-memory entry `project_kb_exp_id_design` and in git history.

> **The sup-claims + md-link-tooling branch landed 2026-05-23** (commits on `kb-node-type-claim-support`): the `verify-md-links` repo-wide link checker (source-gated, `.tex`/`.agents`/`_archive`/`assets/sim_outputs` carve-outs, wired into `make verify` + strict `verify-inter-repo-links`); the **container model** in tooling + docs (a leaf hosts any number of any combination of `clm`/`exp`/`sup` node-bodies — repeated `exp-id:`/`sup-id:` keys) with the `*pending*` support-fraction sentinel; the three real `sup-` re-analysis nodes (`sup-5zs5s6`→LIGO/`clm-395gps`, `sup-s1h0og`→SPARC/`clm-u86caq`, `sup-msv2xy`→CMB/`clm-pe8lpx`), all `quality` + fractions `*pending*`; and the KB→tex provenance-backlink strip across 39 leaves.

> **D6 + axiom-attribution consistency pass landed 2026-05-23.** INVARIANT-S9 now carries the **design/originate/control gate** for `exp-` (re-analyses of outside data → `sup-`/`clm-`, never `exp-`; CLAUDE.md + SCHEMA.md). D4 (`n_spatial` / "Axiom 3 = gravity") was scanned and closed as moot (homologation already scrubbed it). Macroscopic-gravity/G source attribution harmonized to the canonical leaf framing (symmetric volumetric compression → **Axioms 1 + 4** / Machian boundary; Axiom 3 is *satisfied* by the Z₀-match, not the source) — fixed the generated `entry-point.md` summary + the `claim-quality.md` α-invariance premise. Established + applied the **`(clm-XXXXXX via Axiom N)`** attribution form for derived quantities mis-credited to a bare `(Axiom N)` — **complete**: the `p_c = 8πα` packing-fraction class (4 sites → `clm-9s9apq`, local lens Ax3 algebraic / Ax4 saturation) and the Hopf linking number (`scale-separation.md` → `clm-dfaiwj via Axiom 2`). The full `(Axiom [1-4])` scan (198 hits) surfaced no other derived-identity misattributions; the `ξ_topo = e/ℓ_node` "(Axiom 2)" sites are correct (ξ_topo *is* the Axiom-2 isomorphism constant) and **left as-is**. **D3 closed** (`clm-rd9cjm` ownership): keep vol3 (26 citations + the canonical derivation); vol2's mentions forward-reference it per INVARIANT-F1 ("Per Vol 3 Ch 2"), so option (ii)'s earliest-assertion premise is refuted — no relocation.

---

## Near-term

### N1. closure-roadmap → external DAG consumer (finish)
The move + de-link are DONE (`claim-quality-closure-roadmap.md` at KB root, links re-relativized, verify-excluded). Remaining: **add `clm-`/`exp-`/`sup-` ids to its entries** (it currently keys by `L5`/`Q-G`/`A-` thread ids) so it points INTO the DAG by id — a one-directional external consumer; the KB never points back. The `verify-md-links` consumer-side id-validity check (now live) then guards it.

---

## Deferred

### D0. KB-vs-LaTeX divergence as a staleness signal
The KB markdown tree is canonical; the LaTeX manuscript (`manuscript/vol_*/`) is a derived publication artifact (effective 2026-05-07; documented in `kb-docent.md` "Canonical Source" + INVARIANT-S7). **Open:** decide whether to add a verifier step that flags KB-vs-LaTeX divergence as a *derivation-staleness* signal ("the LaTeX has not caught up to this leaf") rather than a KB error. No automated LaTeX-lag detection currently exists.

### D1. vol2-6 claim-quality rescore
~152 `*pending*` claims. **Standing hold** behind the sub-0.65 vol1+common rework. (Once scored, `ave-kb weak-points` can rank weakest / highest-leverage claims directly — superseding the manual closure-roadmap status layer.)

### D2. `src/` engine + driver migration
***RE-EXAMINE STATE FOLLOWING MIGRATION OF GRANT'S L3 WORK TO NEW KB***
Round-2 KB leaves reference engine functions that must land: `ave.gravity.principal_radial_strain` (ε₁₁ = 7GM/c²r), `sparc_catalog_ingest.py`, `gaia_substrate_equilibrium_test.py` + directional, `electron_interferometry_parallax.py` (factor-7 fix), `lbm_3d.py` viscosity docstring, `q_g47_sessions_19_xi_K_derivation.py`.

### D5. Upstream `depends-on` edges (quality pass)
`clm-wzezvt→clm-oygz1i`, `clm-ydksh6→Ax2 clm-dfaiwj`, `clm-kl1ern→Ax4 clm-2dwzib`, etc. — deferred to claim-quality evaluation.

### D7. `_orchestration/` curation
- Redundant-vs-load-bearing pass over the wholesale-ported `_orchestration/` files.
- **NOTE**: deprecation note added to `_orchestration/` entry point documents.

### D8. Strip redundant identification-system remnants
The now-deprecated `axiom-homologation.md` (`session/`) called for unifying the framework's identification systems; the unified `clm-`/`exp-`/`sup-` metadata spine fulfilled that. Its residual value is a pointer to *strip out truly redundant/unnecessary identification-system remains* still scattered in the corpus. (Mine the historical doc for specifics when picked up.)

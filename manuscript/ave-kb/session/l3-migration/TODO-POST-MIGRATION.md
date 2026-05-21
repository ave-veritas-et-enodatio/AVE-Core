# L3 Migration — Post-Migration TODO

Captures the working state of the `AVE-Core_L3` branch (`analysis/integration`) that sits **outside the primary migration effort** (KB content under `manuscript/ave-kb/` + Python source under `src/`). These are the open issues, parked files, dangling forward-references, and environment reconciliations needed to fully capture the L3 branch's working state once the primary porting passes are done.

Primary effort (tracked elsewhere, NOT in this doc): the round-2 `common`+`vol1` KB port + rescore is complete; the `vol2-6` KB sweep and the `src/` engine/driver migration are primary-but-deferred.

---

## 1. `_orchestration/` directory reconciliation

L3 carries a tracked `_orchestration/` directory: per-epic phase logs, `index.md` (priority ladder + active-epic table + HEAD/tag count), `README.md` (implementor-spawning discipline), and `_orchestration/experimental/<exp>/` sub-epic docs. It is L3's project-management spine.

- The newly-ported root `CLAUDE.md` references it as required first-read (`_orchestration/index.md`, `_orchestration/<epic>.md`, `_orchestration/README.md`) — these are **forward-links** until the dir is dealt with.
- `divergence-test-substrate-map.md` (C11-MACH-ZEHNDER row) links `_orchestration/experimental/c11-mach-zehnder/exp-c11-mach-zehnder.md` + its sim-audit.
- **Decision needed** (deferred per 2026-05-21): port wholesale / port a curated subset / drop and rewrite the CLAUDE.md + leaf references. Figure out what is redundant vs load-bearing once the primary KB+src porting is done.

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

## 6. Entry-body drift residue

Register-entry bodies that lag their (now-correct) leaves. Three were fixed 2026-05-21 (`clm-zfqd9v` c_eff form, `clm-hvvvop` 21→26 + tally, A-034 catalog SYM 20→19). Remaining:

- **`clm-bjceop`** entry caveat still states ξ_K1/ξ_K2 are "still open / multi-week work"; the leaf shows them closed 2026-05-18 (ξ_K1 = 8/3, ξ_K2 = 32 with full derivation chain). The Quality rescore (0.70) already reflects the closure; the entry *body* caveat text is stale.

## 7. Primary-but-deferred pointers (NOT post-migration-misc — listed so they aren't lost)

- **`vol2-6` KB sweep**: 152 pending claims + leaf ports. Held until the `common`+`vol1` sub-0.65 claims are reworked solid (standing hold). Part of the primary KB effort.
- **`src/` migration**: engine + driver corrections that round-2 KB leaves now reference must land — e.g. `ave.gravity.principal_radial_strain` (ε₁₁ = 7GM/c²r), `sparc_catalog_ingest.py`, `gaia_substrate_equilibrium_test.py` + directional, `electron_interferometry_parallax.py` (factor-7 fix), `lbm_3d.py` (viscosity docstring), `q_g47_sessions_19_xi_K_derivation.py`. Part of the primary Python-source effort.

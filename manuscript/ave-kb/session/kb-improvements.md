# AVE-KB Improvements / Remaining Work

Running list of open work scoped specifically to the AVE-KB (canonical markdown tree at `AVE-Core/manuscript/ave-kb/`). Broader design questions about future agentic systems live elsewhere; items here are about making the existing KB better as it stands. Completed items are removed — git history holds them.

---

## Deferred

### D0. KB-vs-LaTeX divergence as a staleness signal
The KB markdown tree is canonical; the LaTeX manuscript (`manuscript/vol_*/`) is a derived publication artifact (effective 2026-05-07; documented in `kb-docent.md` "Canonical Source" + INVARIANT-S7). **Open:** decide whether to add a verifier step that flags KB-vs-LaTeX divergence as a *derivation-staleness* signal ("the LaTeX has not caught up to this leaf") rather than a KB error. No automated LaTeX-lag detection currently exists.

### D8. Strip redundant identification-system remnants
The now-deprecated `axiom-homologation.md` (`session/`) called for unifying the framework's identification systems; the unified `clm-`/`exp-`/`sup-` metadata spine fulfilled that. Its residual value is a pointer to *strip out truly redundant/unnecessary identification-system remains* still scattered in the corpus. (Mine the historical doc for specifics when picked up.)

### D11. Split vol4 — relocate the circuit-theory/operator core to vol1, keep applied engineering in vol4 (**coordinate with Grant**)
**Root cause of the vol3→vol4 forward-dependency edges** (the `depends-on` edges tagged `[vol3→vol4 exception, D11]` in vol3's `claim-quality.md`): vol4 is *internally mixed* in dependency-depth. Ch1 circuit theory + the universal operators (Op14 `clm-1eg13f`, etc.), Theorem 3.1′ (`clm-rtdmsn`), and the parametric-coupling kernel (`clm-6t3p6x`) are **near-foundational machinery** that vol1/vol2/vol3 build on — while ch8 (fusion), ch11–12 (falsification benches), ch15 (autoresonant), and the chiral-thrust work are genuine *applications* that correctly sit late. A vol3 macroscopic result depending on vol4 is the signature of that foundational machinery being mis-volumed.

**The fix (decided as the right move 2026-05-24, NOT yet scheduled):** relocate the foundational circuit-theory/operator content out of vol4 into **vol1** (foundations) / `common/`, leaving vol4 as purely applied engineering (chiral thrust stays in vol4). This makes every vol3→vol4 edge point backward, and is **solidity-neutral** (pure relocation = same node/edges, just refiled — the location-juggling invariant). It eliminates those forward-edge exceptions at the root and is the structurally-correct alternative to renumbering volumes (a wholesale vol3↔vol4 swap was considered and rejected: vol4 is mixed, not uniformly more foundational, so a swap would just relocate the forward edges while detonating every path / cross-ref / `path-stable` label / `.tex` citation).

**Why deferred:** big cross-volume change (claim/leaf re-homing + every reference update); **requires coordination with Grant** before execution.

**Execution notes for when picked up:**
- Relocation candidates: Op14 (`clm-1eg13f`), Theorem 3.1′ (`clm-rtdmsn`), parametric-coupling kernel (`clm-6t3p6x`), `clm-v6ti0v`, `clm-p2tp9i`. **Verify each target's *own* dependency feet are axioms/common/vol1 only before moving** — a target that itself rests on vol4-specific content cannot move to vol1 cleanly (would create a *new* forward edge) and must be split or held.
- Keep applied content in vol4: chiral thrust (`clm-7tynm2`) and the bench/device/fusion/autoresonant chapters.
- On landing, drop the vol3→vol4 forward-edge exceptions (tagged `[vol3→vol4 exception, D11]` in their `depends-on` rationales) — they become ordinary backward edges to the relocated claims.

### D12. Tooling Fixes
Planned 2026-05-25 (scan + decisions firmed; execution deferred). Three independent sub-items — land each as its own commit. Sequence them (per the no-mixing-complex-ops rule): D12.2 and D12.3 are mechanical and independent; D12.1 is structural and should go first or last on its own.

**D12.1 — Move `src/ave/kb/` → `manuscript/ave-kb/tools/kb_cmd/`** (all kb tooling together).
- `src/ave/kb/` is the Phase-3 *query/consumer* package (`__init__.py`, `__main__.py`, `cli.py`, `index.py`), deliberately decoupled from the build-side `kb_index_lib.py`. After the move it's no longer a top-level `ave.kb` src package — the **only external importer is `src/tests/kb/test_index.py`**, which relocates into `tools/tests/` and imports `kb_cmd` as a sibling.
- **Dir name uses an underscore (`kb_cmd`), not the hyphenated `kb-cmd`** from the original note — must stay importable as a sibling (same reason `kb_index_lib.py` is underscored while the path-run scripts are hyphenated).
- **Import resolution = PYTHONPATH in the Makefile, NOT `sys.path` manipulation** (sys.path.insert is forbidden — see D12.4). The relocated test imports `kb_cmd` because the make target that runs it sets `PYTHONPATH=manuscript/ave-kb/tools`.
- **There is currently NO make target that runs `tools/tests`** — `make test` is scoped to `src/tests` only, so the existing `tools/tests/` are orphaned from the build. D12.1 adds a **`test-tools`** target (`PYTHONPATH=manuscript/ave-kb/tools $(PYTEST) manuscript/ave-kb/tools/tests`) and folds it into `make test`, so the relocated `test_index.py` is actually exercised. (Add to `.PHONY` + help section. Decided 2026-05-25; deferred to land WITH the move, not standalone.)
- Steps: (1) `git mv src/ave/kb/ → manuscript/ave-kb/tools/kb_cmd/`; (2) move `src/tests/kb/test_index.py` → `manuscript/ave-kb/tools/tests/`, switch its `from ave.kb...` imports to `from kb_cmd...`, and its `python -m ave.kb` subprocess call to `python -m kb_cmd` (with `PYTHONPATH=manuscript/ave-kb/tools` in the spawning env); (3) Makefile `kb-claim-stats` (line 95) — replace `PYTHONPATH=src python -m ave.kb stats` with `PYTHONPATH=manuscript/ave-kb/tools python -m kb_cmd stats`; (4) add the `tools/tests` make target above + wire into `make test`; (5) confirm nothing else references `ave.kb` (grep was clean except tests + Makefile); (6) remove now-empty `src/ave/kb/` + `src/tests/kb/`.

**D12.2 — `read_bytes()`/`write_bytes()` → utf-8 `read_text()`/`write_text()`** in ave-kb/tools + test code.
- 32 call sites across 7 files (`refresh-kb-metadata.py` 2, `verify-kb-metadata.py` 2, `kb_index_lib.py` 1, `tools/tests/*` the rest) **+ ~67 `b"..."` fixture literals** in the kb tests that flip to `str`.
- Per-site check: confirm no site relies on binary semantics (content-hashing, explicit newline bytes) before converting. Land worker+verifier (mechanical-coverage-gate): **done = 0 `read_bytes`/`write_bytes` in those dirs AND suite green.**

**D12.3 — make-target literals → defined constant** (Runtime + Makefile only; docstrings/comments stay as prose).
- Honest scope is ~10 runtime sites, NOT the raw ~35/~20 grep counts (most are docstrings). Two classes:
  - **Makefile**: dedupe the target name on the `.PHONY` (line 19) + help-echo (line 27) lines via a make variable; the `target:` rule line itself must stay a literal.
  - **Python user-facing error strings** ("run `make refresh-kb-metadata`"): ~6 sites (`index.py:548` [→ `kb_cmd` after D12.1], `verify-kb-metadata.py` ×4, `predictions_manifest_refresh.py`) → reference a module constant.

**D12.4 — Rip out `sys.path.insert` in ave-kb/tools; import resolution via PYTHONPATH only** (surfaced 2026-05-25 while planning D12.1). `sys.path` manipulation is forbidden; the canonical mechanism is `PYTHONPATH` set by the Makefile target. The tools dir currently violates this in **9 sites**: `refresh-kb-metadata.py`, `verify-kb-metadata.py`, `verify-md-links.py`, and `tools/tests/{test_leaf_references,test_check_index,test_refresh_index,test_kb_index_lib}.py` each do `if str(_TOOLS_DIR) not in sys.path: sys.path.insert(0, str(_TOOLS_DIR))` to reach `kb_index_lib`.
- Fix: delete those blocks; set `PYTHONPATH=manuscript/ave-kb/tools` on every make target that runs a tools script (`refresh-kb-metadata`, `verify-kb-metadata`, `verify-md-links`) and on the new `tools/tests` target (D12.1). The path-load-by-spec harness in `test_refresh_index.py` (hyphenated-script import) is a separate mechanism and stays.
- **Couples to D12.1** (same Makefile targets + same `tools/tests` runner gets created). Reasonable to land D12.1 + D12.4 as one structural commit, keeping D12.2/D12.3 separate mechanical commits.

### D13. Distill 3 manuscript derivations the KB never captured, then bridge P10/P41/P47
Surfaced 2026-05-25 during the predictions-manifest → claim-DAG bridge (Phase 2). Three **shipped** predictions point at `.tex` derivations that exist in the manuscript but were never distilled into KB leaves, so `predictions.yaml` cannot bridge them to a `clm-` (they sit in the unbridged-warn set). Distillation must be verbatim-faithful per INVARIANT-S7 (leaves canonical). After minting each clm, add the bridge to `predictions.yaml` (`clm:` field) + run `make refresh-predictions`; the entry then leaves the unbridged set.

- **P47 — α thermal running (δ_strain)** → `manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex` (`sec:alpha_thermal_running`). KB **has** this chapter as a leaf (`vol1/ch8-alpha-golden-torus.md`, hosts cold-α `clm-0ktpcn`). **Update the leaf**: add the δ_strain thermal-running sub-result (CMB thermal metric expansion; distinct from QED vacuum polarization) as a new clm.
- **P10 — Solar light deflection** → `manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex` (`sec:double_deflection`; δ = 4GM/bc² via the ν_vac = 2/7 transverse Poisson coupling = exactly 2× Newtonian). KB **has** `vol3/gravity/ch02-general-relativity/` leaves (incl. `k4-tlm-lensing-validation.md`, `gravitational-refractive-index-gradient.md`). **Update a leaf**: add the weak-field double-deflection result as a new clm.
- **P41 — WD redshift (Sirius B)** → `manuscript/vol_3_macroscopic/chapters/20_white_dwarf_predictions.tex` (`ch:white_dwarf_predictions`, a real 282-line chapter). KB has **zero** white-dwarf leaves. **New leaf(s)** needed for vol3 ch20.

### D14. Flip the predictions-manifest bridge check warn→critical (blocked on D13)
`src/scripts/predictions_manifest_validator.py` `check_bridge` currently emits one aggregated **warn** for entries lacking a `clm:`/`exp:` bridge into the claim DAG. As of 2026-05-25, 33/36 entries are bridged; the 3 unbridged are exactly P10/P41/P47 (blocked on D13). **When D13 lands and all 36 are bridged, flip the unbridged case from `warn` to `critical`** so any future unbridged prediction fails `make verify` — closing the door on silent re-accretion of a parallel id space (INVARIANT-S11). One-line severity change in `check_bridge` + update `test_check_axioms`/`TestBridge` expectations.

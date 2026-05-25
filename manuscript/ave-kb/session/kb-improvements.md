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

### D15. Pin `encoding="utf-8"` on all text `read_text()`/`write_text()` (cross-platform)
Surfaced 2026-05-25 while doing D12.2 (which converted byte ops → text ops). Distinct from D12.2: these are *already* text ops, but **unpinned** — they rely on the platform-default encoding (`utf-8` on macOS/Linux, `cp1252` on Windows), which silently corrupts non-ASCII content on Windows. The standing python-coder rule now requires `encoding="utf-8"` on every text read/write.
- **47 unpinned sites in `manuscript/ave-kb/tools/`** (`refresh-kb-metadata.py` 9, `kb_index_lib.py` 8, `verify-kb-metadata.py` 5, `tools/tests/*` 14+, `tools/archival/*` 5) — and **almost certainly more across `src/`** (the 33-days-ago code-quality pass did annotations + sys.path removal + flake8, but did NOT pin encodings). Scope the full repo before executing: `grep -rn 'read_text()\|write_text(' --include='*.py' | grep -v encoding=`.
- Mechanical; land worker+verifier (mechanical-coverage-gate): **done = 0 unpinned `read_text()`/`write_text(` across the chosen scope AND suite green.** Note the kb tools tree is outside pre-commit's `^src/` flake8 scope, so the verifier is the grep, not the linter (see D12.4 follow-up below).
- **Related lint blind-spot** (also surfaced 2026-05-25): pre-commit/flake8 is scoped to `^src/`, so `manuscript/ave-kb/tools/` gets NO automated style/import/encoding enforcement — which is how the `sys.path`/byte-op/unpinned-encoding debt accreted there unnoticed. Consider extending the flake8/pre-commit scope (or a dedicated tools-lint hook) to cover the tools tree. Beware: a first run may surface a backlog of pre-existing violations in the large `kb_index_lib.py`.

### D13. Distill 3 manuscript derivations the KB never captured, then bridge P10/P41/P47
Surfaced 2026-05-25 during the predictions-manifest → claim-DAG bridge (Phase 2). Three **shipped** predictions point at `.tex` derivations that exist in the manuscript but were never distilled into KB leaves, so `predictions.yaml` cannot bridge them to a `clm-` (they sit in the unbridged-warn set). Distillation must be verbatim-faithful per INVARIANT-S7 (leaves canonical). After minting each clm, add the bridge to `predictions.yaml` (`clm:` field) + run `make refresh-predictions`; the entry then leaves the unbridged set.

- **P47 — α thermal running (δ_strain)** → `manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex` (`sec:alpha_thermal_running`). KB **has** this chapter as a leaf (`vol1/ch8-alpha-golden-torus.md`, hosts cold-α `clm-0ktpcn`). **Update the leaf**: add the δ_strain thermal-running sub-result (CMB thermal metric expansion; distinct from QED vacuum polarization) as a new clm.
- **P10 — Solar light deflection** → `manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex` (`sec:double_deflection`; δ = 4GM/bc² via the ν_vac = 2/7 transverse Poisson coupling = exactly 2× Newtonian). KB **has** `vol3/gravity/ch02-general-relativity/` leaves (incl. `k4-tlm-lensing-validation.md`, `gravitational-refractive-index-gradient.md`). **Update a leaf**: add the weak-field double-deflection result as a new clm.
- **P41 — WD redshift (Sirius B)** → `manuscript/vol_3_macroscopic/chapters/20_white_dwarf_predictions.tex` (`ch:white_dwarf_predictions`, a real 282-line chapter). KB has **zero** white-dwarf leaves. **New leaf(s)** needed for vol3 ch20.

### D14. Flip the predictions-manifest bridge check warn→critical (blocked on D13)
`src/scripts/predictions_manifest_validator.py` `check_bridge` currently emits one aggregated **warn** for entries lacking a `clm:`/`exp:` bridge into the claim DAG. As of 2026-05-25, 33/36 entries are bridged; the 3 unbridged are exactly P10/P41/P47 (blocked on D13). **When D13 lands and all 36 are bridged, flip the unbridged case from `warn` to `critical`** so any future unbridged prediction fails `make verify` — closing the door on silent re-accretion of a parallel id space (INVARIANT-S11). One-line severity change in `check_bridge` + update `test_check_axioms`/`TestBridge` expectations.

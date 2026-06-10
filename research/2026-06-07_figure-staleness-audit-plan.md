# PLAN (frozen) — Manuscript-wide figure-staleness audit

**Date:** 2026-06-07
**Lane:** auditor — produce a READ-ONLY figure-staleness ledger. **No figure edits, no regeneration committed.** Deliverable = the worklist (which figures are stale, why, and what regenerates them).
**Branch:** `analysis/2026-06-07-vol0-kb-reconciliation-ledger` (off `main` @ `f1f927c8`), isolated worktree `/tmp/ave-vol0-recon-wt`.
**Trigger:** Grant — "audit all figures for staleness as well, fully plan out" (extending the Vol 0 ↔ KB text reconciliation).
**Depends on:** the text-reconciliation ledger (workflow `w5buxjxvr`, in flight) — its Class-D/Class-O drifts ARE the structural-staleness target list for figures.

## Source-of-truth axis

**KB (`manuscript/ave-kb/`) is canonical.** A figure is *stale* when the artifact (the rendered image OR its caption) depicts a value / structure / mechanism / prediction-status that the **current KB no longer supports**. The text-reconciliation ledger (running now) enumerates exactly those drifts; the figure audit **consumes that ledger** as its structural-staleness checklist, then adds the figure-specific surfaces (rendered content, caption claims, generation provenance, reference integrity).

## The figure surface (enumerated, verify-before-cite @ f1f927c8)

- **208 `\includegraphics` references** across 6 volumes: Vol 6 = 75, Vol 3 = 42, Vol 4 = 30, Vol 2 = 29, Vol 1 = 22, Vol 5 = 7; backmatter = 2. (Vol 0 chapters = 0; Vol 0 reaches figures only via its 2 backmatter refs.)
- **252 image assets** in 3 pools: `assets/figures/` (41), `assets/sim_outputs/` (58), `assets/` (8), and per-volume `manuscript/<vol>/figures/` (Vol 6 = **100**, Vol 3 = 12, Vol 4 = 12, Vol 2 = 9, Vol 1 = 6, Vol 5 = 3, backmatter = 2).
- **203 figure-generating scripts** (`savefig`) in `src/` (mix of `src/tests/` and `src/scripts/`).
- **Oldest assets last regenerated 2026-04-13** (much of `assets/figures/`), while the manuscript has churned heavily since — age-based drift candidates.

## Grounding findings that shape the method

1. **Provenance chain is BROKEN for figures.** `src/scripts/` savefig targets write to `/tmp/*.png`, not into `assets/`; figures are hand-copied in. So there is no automated asset→generator→SHA link. The A47 `numerical-provenance-manifest.md` SHA-anchors numerical *tables*, **not figures**. ⇒ full "re-run script, pixel-diff the committed asset" (S6) is **mostly infeasible** until the asset→script map is reconstructed. This is itself a headline finding (figure-provenance debt).
2. **Captions assert live values** (confirmed): `H_∞=69.32`, `κ=8π/κ_eff`, `6³₂ Borromean proton`, `235 nucleons`, etc. ⇒ caption-claim staleness (S4) is real and checkable against the KB + text ledger without re-rendering.
3. **Vol 6 is figure-dominated** (100 assets / 75 refs — element & structure renders). It needs its own batch and likely shares one generator family (`solve_*.py` per element).

## Staleness taxonomy (the class set the audit assigns per figure)

- **S1 — Structural drift (HIGH):** the rendered image depicts a superseded structure/mechanism. Primary targets = the text-ledger's Class-D/O drifts: z=3/SRS lattice renders vs canonical z=4 diamond; gravity `(9/7)` deflection geometry; any walked-back soliton/topology. Cross-checked against the running reconciliation.
- **S2 — Numerical drift (HIGH):** a plotted curve/value differs from the current canonical constant or solver output (the `radial_eigenvalue` 5–15% drift pattern; T_EM-era OOM errors). Verifiable only where the generator is discoverable.
- **S3 — Provenance gap (MEDIUM):** no discoverable generating script for the asset (orphan, unverifiable), or generator exists but is not registered/SHA-anchored. Every figure gets a provenance verdict: {mapped-to-script | orphan | manual-artifact}.
- **S4 — Caption/claim drift (HIGH):** caption asserts a value/topology/prediction-status the KB has changed, rescoped, or retired (e.g. a caption stating a now-walked-back prediction as live). Checked against KB + text ledger.
- **S5 — Reference integrity (LOW, cheap):** `\includegraphics` → missing file (broken), or asset → zero references (orphan to prune). Mechanical.
- **S6 — Regeneration drift (HIGH, gated):** re-run the generator today → materially different image than the committed asset. **Only feasible for the discoverable-generator subset**; the rest are flagged S3.

Per-figure verdict = the highest-severity class that applies, with file:line evidence (figure path, the `\includegraphics`+`\caption` site, the governing KB leaf, and the generator path or "orphan").

## Enumeration method (Step 1 — scope-bound, reproducible)

1. Parse all 208 `\includegraphics` → (figure-file, volume, ref-site:line, caption text). Resolve each against the 5 `graphicspath` roots → flag S5 broken.
2. Cross-list the 252 assets against the reference set → flag S5 orphans (asset, zero refs).
3. Best-effort asset→generator map: grep `src/` for each asset basename + for `/tmp/<base>` savefig targets + naming-convention matches → produces {mapped | orphan} per figure (the S3 surface).
4. Tag every figure with its volume-batch + a drift-risk prior (touches z=3/z=4? gravity? a walked-back prediction? oldest-git asset?) to prioritize.

## Fan-out architecture (Step 2–5 — sweep-audit discipline)

Per-volume batches (Vol 6 split into ~3 sub-batches given 100 assets). One `ave-corpus-grep` auditor per batch:

- **Phase ENUMERATE** (1 agent): build the figure→(ref, caption, asset, generator?) table for the whole manuscript; emit broken (S5) + orphans (S5) + provenance-gap (S3) immediately.
- **Phase CLASSIFY** (pipeline, 1 agent per volume-batch): for each figure, read its caption + (where an image-describing source/generator exists) its generator, check the depicted/asserted content against the governing KB leaf AND the text-reconciliation ledger's confirmed drifts; assign S1/S2/S4 with evidence.
- **Phase VERIFY** (pipeline stage 2): independent skeptic re-reads the KB leaf for each S1/S2/S4 finding; downgrades non-real flags (a figure age ≠ stale; a caption value that still matches KB = clean).
- **Phase S6-GATED** (only if Grant picks depth ≥ B): run the discoverable-generator subset; diff fresh output vs committed asset; report material deltas. Uses `ave-canonical-source` (generator must import canonical constants) + `ave-driver-script-honesty` (the generator's own print-vs-compute honesty).
- **Phase CRITIC** (1 agent): completeness — which volume/asset-pool/claim-class went unchecked; which text-ledger drift has a figure contact point not yet flagged.

## Depth options (the one decision for Grant)

- **(A) Content + provenance audit, no regeneration.** Classify every figure S1–S5 from caption/content vs KB + text ledger; build the asset→generator map; flag all provenance gaps. Honest, complete worklist; fast; surfaces *which* figures need re-rendering without re-rendering them. **Recommended as the first pass.**
- **(B) = (A) + targeted regeneration (S6) of the high-risk discoverable subset.** Re-run only the generators that ARE mappable and whose physics the text ledger shows drifted; pixel/value-diff vs committed asset. Partial S6 coverage (bounded by the broken provenance chain).
- **(C) Full provenance reconstruction + regenerate all 203 generators.** Rebuild the asset→script map as a prerequisite, then re-render everything. Large — effectively its own epic; the asset→script reconstruction alone is a workstream.

## Sequencing

Run the figure audit **after** the text-reconciliation ledger (`w5buxjxvr`) returns, so its confirmed Class-D/O drifts seed the S1/S4 structural+caption checklist. The two share the branch and the closure-roadmap §0.5 log.

## Skills applied

`ave-sweep-audit` (spine — 208-figure class-prioritized batch sweep), `ave-canonical-source` (S6: generators must trace constants to `ave.core.constants`), `ave-driver-script-honesty` (S6: generator print-vs-compute honesty), `verify-before-cite` (every figure-row file:line grep/Read-verified, skeptic-checked), `ave-evidence-framing-discipline` (strongest-accurate staleness language; age≠stale), `flag-don't-fix` (ledger is the worklist — no figure edits/regeneration committed), `ave-prereg` (this frozen plan).

## Deliverable

`research/2026-06-07_figure-staleness-ledger.md` — per-figure table {figure, volume, ref-site, caption-claim, governing-KB-leaf, generator-or-orphan, staleness-class S1–S6, skeptic verdict, regenerates-via}, sorted by severity — plus a `claim-quality-closure-roadmap.md §0.5` row and a handoff. This is the figure-regeneration worklist, to run after the O-class adjudications close.

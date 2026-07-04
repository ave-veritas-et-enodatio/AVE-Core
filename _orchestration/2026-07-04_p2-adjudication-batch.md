# P2 Adjudication Batch — Repo Formatting & Cleanup Epic

**Status:** ACTIVE — PENDING (owner: Grant, 2026-07-04) — awaiting per-section rulings; assembled by the orchestration session from the four P1 lane reports at HEAD `2a7d01dc`.
**Companion:** full P1 disposition tables in [`2026-07-04_p1-lint-sweep-findings.md`](2026-07-04_p1-lint-sweep-findings.md). Conventions: [`2026-07_repo-conventions.md`](2026-07_repo-conventions.md) (ratified 2026-07-04).
**Scope reminder:** organization/formatting only. DELETE-CANDIDATE below applies ONLY to driver-regenerable renders (the PR #502 §D3 DELETE-SAFE class); non-regenerable artifacts are GRANT-CALL, never auto-deleted; content docs are never deleted. Honesty-trail docs untouchable throughout.

Each section is a one-word-per-row (or one-word-per-group) ruling surface. "Recommend" columns are the auditors' + orchestrator's; every row awaits Grant's word.

---

## §1 — The 44 unmerged-branch dispositions (PR #502 §D2, re-verified at HEAD)

The adjudication set = the 44 branches enumerated in PR #502 §D2 (pinned; verified 1:1 against origin at assembly HEAD `2a7d01dc`). The live origin count drifts transiently as concurrent arcs merge — post-merge close-outs (audit-tag-then-delete) of non-set branches are routine hygiene, not adjudication rows. Family table (branch inventory verbatim in PR #502 §D2; `u=` unique commits):

| # | Family | Branches / u | Recommend | Grant |
|---|---|---|---|---|
| 1 | Stage-2/S3 engine (`engine-stage2-native-cage-imex` u=5, `-run` u=3) | operator + verdict already in main; DISPERSE re-booked on srs (D1) | TAG-AND-DELETE | ___ |
| 2 | **keystone substrate-pump** (6 branches, u=29/29/26/21/20/17) | verdicts propagated to corpus prose; raw result docs NOT in main | GRANT-CALL: land-docs vs archive | ___ |
| 2b | ↳ special row: `stage16-rerun-amendments` (u=17) | carries the Stage-1.5 **Rule-12 retraction + CONTESTED marker** still stranded — `54fa23cd` confirmed NOT in main ancestry; `index.md:160` names merging branch-stranded retractions as the durable stale-read fix | **LAND (merge the retraction)** | ___ |
| 3 | **boundary-MQJ stage1.5/1.6** (3 branches, u=14/10/6) | verdict docs not in main; direction superseded by D1, moving-wall content distinct | GRANT-CALL: land vs archive | ___ |
| 4 | **passive-eigenmode** (`passive-eigenmode-solve` u=50, `eigenmode-heldbc` u=31) | largest un-landed content; Phase-25 substrate-pump OVERTURNED-to-scoped + Rule-12 mis-binning annotation | GRANT-CALL: land vs archive | ___ |
| 5 | genesis series (4 branches, u=4/3/2/7) | (III) negatives; exploratory-not-adjudicated | GRANT-CALL | ___ |
| 6 | motion/moving (4 branches, u=9/5/2/4) | un-landed transport negatives (absent `boost` DOF) | GRANT-CALL | ___ |
| 7 | α / winding probes (7 branches, u=8/3/2/1/1/2/2) | mixed; `vacuum-z4-coordination-walkback` may be redundant post-D1 | GRANT-CALL | ___ |
| 8 | scope/plan docs (7 branches, u=1 each) | small single-commit scope memos; `#86` back-reaction scope now realized | LAND (as history) | ___ |
| 9 | μ-keying (`engine/mu-circulation-keying` u=2) | content landed via PR #500; 2 commits are patch-variants | TAG-AND-DELETE | ___ |
| 10 | WIP-preserve / misc (8 branches, u=1-5) | intentional snapshots + tooling; `open-timestamp-claims` + `kit-hex-clocking` may be LAND-candidates | GRANT-CALL (tooling rows: LAND) | ___ |
| 11 | 2026-06-11 resumables (3 branches: `alpha-a3-reservoir`, `chiral-angle-of-attack`, `screened-winding-probe`) | ~3.5 weeks old; ratified SLA N=30d — re-affirm-or-tag decision is due now | re-affirm OR TAG-AND-DELETE per branch | ___ |

Note the physics-history weight sits in rows 2/2b/3/4 (result docs that exist nowhere on main). A LAND ruling means a P3 implementor opens a docs-landing PR per family (result docs only, honestly framed); an ARCHIVE ruling means audit-tag-then-delete (tags preserve everything immutably; re-open later = `git checkout -b <topic> <tag>`).

---

## §2 — The orphan set (91 files, 35.2 MB; down from ~106 at PR #502 — shrink is real, #507 placed figures)

Full 91-row table with per-file evidence: companion doc §C. Group-level ruling surface (per-row overrides welcome):

| Group | n | Size | Character | Recommend | Grant |
|---|---|---|---|---|---|
| A vol_6 strain/flux/circuit renders | 28 | ~7 MB | driver-regenerable duplicates + superseded renders (incl. `circuit_*.png` twins of the cited `.pdf`s) | DELETE-CANDIDATE (25) / ARCHIVE (3 strain) | ___ |
| B `assets/figures/` panels | 17 | ~14 MB | mostly NO-driver (non-regenerable) | GRANT-CALL each (15) / DELETE-CANDIDATE (2 with drivers) | ___ |
| C lab-notebook template assets | 12 | ~6 MB | source-assets, not derived | KEEP-IN-PLACE | ___ |
| D vol_9 datasheet generated-not-placed (7) + debug frames (4) | 11 | ~1 MB | `gen_*.py` drivers exist, no `\includegraphics` places the 7; the 4 `T*_debug` are uncited duplicates | KEEP (7, pending-placement) / DELETE-CANDIDATE (4) | ___ |
| E vol_4 fusion/HOPF/doping renders | 7 | ~2.8 MB | NO-driver mostly | GRANT-CALL | ___ |
| F `research/figures/engine_acceptance/` debug frames | 4 | ~0.3 MB | regen.py-regenerable, uncited | DELETE-CANDIDATE | ___ |
| G assets gifs + sim_outputs + misc | 8 | ~5.7 MB | 3 regenerable gifs; sim_outputs = canonical-asset policy; 2 keep | DELETE-CANDIDATE (3 gifs) / KEEP (5) | ___ |
| H vol_2/3/5 tail | 4 | ~0.2 MB | 2 regenerable, 2 no-driver | DELETE-CANDIDATE (2) / GRANT-CALL (2) | ___ |

Named sub-rulings inside the groups (from lane (c) anomalies):
- **`carbon_strain.png`** — only "citer" is the figure-audit ledger's *do-not-place walk-back* (wrong element labeling). Recommend: remove from allowlist (die-by-removal, not migration); ledger keeps resolving (honesty-trail citer). Grant: ___
- **`ie_validation_z1_14.pdf` (vol_2 + vol_6 copies, both uncited)** — ledger ruled "use the corrected copy, not the vol_2 Al-Z13-OPEN one". Keep-corrected / delete-stale-vol_2 / delete-both? Grant: ___
- **Group D generated-not-placed (7 `gen_*.py` renders)** — pending-placement (keep) vs abandoned (delete)? Recommend keep. Grant: ___

---

## §3 — Predictions-count accounting

The ratified (f) rule covers README badge/prose/table + manifest. P1(d) found a **fourth surface with a third number**:

- **`LIVING_REFERENCE.md:375` + `:387` say "46 predictions"** (README says 47; manifest 36 entries; 47↔36 closes exactly). Is 46 (i) stale drift → P3 fixes to 47 + basis declaration, or (ii) an intentional distinct count (e.g. excluding a walked-back row) → P3 documents its basis instead? **Grant: ___**
- Mechanical (no ruling needed, listed for visibility): basis declarations added to the 5 README surfaces; the conventions doc's "40 displayed rows" descriptor corrected to the HEAD-true 33; the badge derive-and-compare gate builds in P4 as ratified.

---

## §4 — Orchestration-doc dispositions

P1(d): of 96 epic docs, 56 have NO status header, 23 use non-enum tokens, 0 are fully (c)-compliant. P1(b): 27 markers are RECONCILE-DEAD with evidence, 89 need attribution, 7 UNCLEAR remain. Rulings that unblock the P3 backfill:

- **Loop-gap v11/v12/v15 charters + unified-harness rows** — program froze srs at v17; charters self-label ACTIVE with no supersession note. Superseded-by-v17 (terminal-stamp them) vs still-resumable (attribute them)? Settles all 7 remaining UNCLEAR markers. **Grant: ___**
- **2026-06-10 genesis workflow ledger** — frozen snapshot whose RUNNING scout-table is fully subsumed by the 2026-06-11 audit tags. Recommend ONE dated CLOSED header (not 9 row edits). **Grant: ___**
- **Header backfill mode** — P3 backfills the 56 missing headers using lane (d)'s per-doc state evidence, marking undeterminable docs UNCLEAR-pending-owner rather than guessing (5 docs currently in that bucket). Recommend: proceed as stated. **Grant: ___**

---

## §5 — Convention amendments surfaced by P1 (the sweep testing the new rules against reality)

- **(e) regex compound-token gap** — the ratified regex false-positives on 14 hyphen-compound labels (`RESEARCH-PENDING`, `AUDIT-PENDING`, `ADJUDICATION-PENDING`, `REVIEW-PENDING`, `RITUAL-PENDING`, `DEAD-MID-FLIGHT`). Options: (i) compound-allowlist in the linter **[RECOMMENDED — explicit, greppable]**, (ii) lookaround excluding `X-`/`-X` forms. **Grant: ___**
- **KB CLAUDE.md INVARIANT-S1 environment set incomplete** — `warningbox` (16 corpus uses, cross-volume) and raw `tcolorbox` (16) absent from the allowed list. Extend the S1 set to admit `warningbox` (+ decide raw-`tcolorbox`: admit or normalize to named envs) **[RECOMMENDED: admit warningbox; normalize raw tcolorbox in P3]** vs treat all 32 as violations. **Grant: ___**
- Mechanical (visibility only): INVARIANT-N2's stale confirmed-by counts refreshed at next KB CLAUDE.md touch; `engine-capability-map.md:320` wildcard citer — recommend reword to past-tense policy-note on migration (it names the smell, it is not a live figure link) — flag if you want a live repoint instead. **Grant: ___ (default reword)**

---

## §6 — What your rulings unleash (P3 execution preview, bounded per-domain PRs)

1. **Citation-currency PR(s):** ~220 mechanical line-bumps (KB+orch, fully enumerated), FPR provenance refresh, 1 content-repair (`engine-capability-map.md:195` → verify canonical host of the Q≈30.8 cold-cage negative, now in `graded_vacuum_network.py:13`), research-tier sweep in the same pattern (~1200 pairs, same drift class per sample).
2. **Figure/data migration PR(s):** 26 figures → per-volume `figures/` (+1 removal), 38 data files → per-volume/common `results/`, ~26 allowlist lines retired, wildcard + graphicspath + KB relative-path rewrites, drivers repointed — all link-coupled, gates green per commit.
3. **Marker/header PR:** 27 dated terminal-state reconciliations (evidence in hand), 89 attributions, 56 header backfills + 23 enum rewrites + index.md last-updated line — per §4 rulings.
4. **Branch executions:** per §1 rulings (tag-and-delete batches; docs-landing PRs for LAND families).
5. **Doc-fix PR:** root CLAUDE.md rewrite (tag count, dead branch rows, dead-branch guidance), LIVING_REFERENCE + README basis declarations per §3, conventions 40→33 descriptor.
6. **P4 (after P3):** `lint-status-markers` (warn mode, backlog = the 181-line baseline), figure-placement checker, badge derive-and-compare, sampled citation-currency check; PROPOSED monthly hygiene routine (created only on your explicit go).

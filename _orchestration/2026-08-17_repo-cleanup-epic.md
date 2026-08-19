# Epic: Repo cleanup — census-driven, decisions batched, waves serialized

**Status:** ACTIVE — Wave 0 in flight (electron-identity closeout); Wave 1 GO pending; Wave 2 = one Grant adjudication sitting
**Opened:** 2026-08-17
**Census basis:** six-domain read-only sweep at HEAD `36ce03b9` (2026-08-17) — every open-item read in full, git-object litter enumerated, status lines cross-checked against docket + merged PRs, tooling debt measured by running the tools, KB/manuscript hygiene link-graphed, plus a completeness critic over the domains the first five missed. Receipts inline below; commands stated where a count is load-bearing.

REPO-CLEANUP-EPIC-ANCHOR: waves serialized, decisions batched into one sitting, mechanical work receipted before dispatch.

**Filter for every wave:** does this remove a false statement from a live surface, retire dead weight, or unblock a Grant decision that is currently invisible? If none, stop.

---

## The three findings that shape the plan

1. **The open-items board is healthy; the bottleneck is adjudication bandwidth.** All 60 anchors resolve exactly-once (re-verified by reproducing `validate_anchor` read-only). Only 2 items are closeable and 2 stale. But **29 of 60 are ROUTED-TO-GRANT** (34 Grant-owned). The plan therefore batches decisions into one sitting rather than scattering them.
2. **The largest single obligation is arithmetic, not physics.** The LaTeX+README follow-ups tracker as scoped demands 10 F-rows × (166 LaTeX + 9 README) = **1,750 full-document reads** (~413,500 line-reads; the same 3.57 MB surface read ten times). A single combined pass with per-row hit ledgers cuts it ~10×. Amending the protocol is Grant's word (it is his signed read-discharge rule).
3. **"869 remote branches" was a mirage.** Origin has exactly **9** branches (`git ls-remote --heads origin | wc -l`). 859 of the local remote-tracking refs are stale `pr/*` PR-head refs orphaned by a removed fetch refspec — `git fetch --prune` can never clean them; one config removal + prune kills all of them.

## Wave 0 — electron-identity closeout (in flight, not this epic's work)

Audit-1 sentence (Grant) → correction PR (K3 banner on `axiom-definitions.md:33`; text-anchors for the 8 line-pinned YAML anchors; repoint + excerpt the `the-abandoned-interior.md:111/:127` inbound cites; `**` into the C6 excerpt; filter-answer APPEND semantics; dated ledger count note src 90→93 + `--hidden`) → merge #976 → audit-tag the missing lanes (#971 `analysis/electron-identity-phase-a-closeout`, #973 phase-b) → prune the four finished phase worktrees.

## Wave 1 — mechanical batch (receipts in hand, zero rulings needed) — GO pending

### Local machine (no PR)

| action | count | receipt |
|---|---|---|
| delete merged local branches | **89** now (16 more unpin as worktrees clear) | `git branch --merged origin/main` minus main; `research/l3-electron-soliton` no longer exists anywhere (only its audit tag) |
| purge stale `pr/*` tracking refs | **859** (852 merged, 6 abandoned-unmerged, 1 other) | orphaned by a removed fetch refspec; `git ls-remote` shows 9 real branches |
| prune broken tmp worktrees | **7** | broken gitdir links under `/private/tmp/claude-501/*/scratchpad/` |
| remove stale-CLEAN worktrees | **10** | branch merged + `status --porcelain` empty — fully recoverable from git |
| **HOLD: stale-DIRTY worktrees** | **3** | staged content that **differs from origin/main by blob-hash** (6 of 12 dirty files sampled, all differ) — inspect before any removal; Wave-2 decision |

### One status-hygiene PR

Fifteen false status lines, all flipped Rule-12 style (`SUPERSEDED <date> — <why> (receipt). Was: <verbatim prior>`):

- `2026-06-15_wall-branch-fork.md:5` "ACTIVE — Phase 1" — fork resolved B3-DEGENERATE (#260)
- `2026-06-11_lattice-d1-test-gated.md:5` "ACTIVE — test not pick" — D1 RATIFIED 2026-07-03
- `2026-06-02_alpha-class2-lift-radiation-resistance.md:3` — lift-path closed negative 2026-06-04
- `2026-06-23_lattice-discovery-program.md:3` "all PRs HELD" — every named PR resolved (gh-verified)
- `2026-06-16_standing-decisions-audit-lane.md:5` — ruled PRs merged; residual Smith-chart item fell off every surface (→ Wave 2 docket)
- `2026-06-27_biquaternion-coupled-network-integration.md:4` — abandoned same-day; names a phantom worktree
- `2026-06-09_ion-compression-rectifier-arc.md:3` — arc landed 2026-06-10; gated v5 successor died with the genesis kills
- `2026-06-11_orchestration-branch-plan.md:3` — false on every clause ("Main @ 0b4b9d5c. 0 open PRs")
- `double-slit-ee-mapping.md:6` "Ready for orchestrator audit + merge" — audited and merged
- `research/2026-05-31_Q-EMBED-SEL-1_step_c…prereg.md:3` "DRAFT, NOT LOCKED" — locked and run to result
- `research/2026-06-10_electron-device-datasheet_draft.md:141` "ALL PENDING (v5 run in flight)" — v5 completed same day; stack later K3-killed
- `research/2026-05-18_phase3f3-first-attempt-result.md:5` + `research/2026-05-17_…GAIA_DIRECTIONAL_result.md:3` — low-severity currentness claims, dated notes only
- `2026-07-04_repo-formatting-cleanup-epic.md:3` + `2026-07-04_p2-adjudication-batch.md:3` — status stays ACTIVE (the P2 ruling IS owed) but each gains a pointer to the new open-item so the owed ruling is on the board
- board regenerate (header one merge behind; misses #976)

Plus, same PR: `anisotropy-observable` open-item body refresh (its scoping lane ran 2026-07-31 — verdict "NOT an independent frontier item", W1–W8 walk questions routed to Grant, none of which the item shows) · root `AGENTS.md` replaced with a pointer to `CLAUDE.md` (currently 10,969 bytes of atopile PCB-DSL boilerplate at the exact filename agent harnesses read) · `src/TODO.md` dangling `ARCHITECTURE_REVIEW.md` pointer · `make help` rows for `refresh-predictions` and `test-genesis`.

### One deletion PR

The **88 MB duplicate SPICE netlist tree**: `manuscript/vol_6_periodic_table/simulations/spice_netlists/` duplicates the live `src/scripts/vol_6_periodic_table/simulations/spice_netlists/` — 107 identical-blob pairs, frozen at the 2026-04-13 IP-partition commit, referenced by **no `.tex`** (only `src/` code references the path). Delete the manuscript copy; the live copy stays.

## Wave 2 — one Grant adjudication sitting (~30 min, batched)

**One-word rulings** (pre-assembled, receipts in the census):

| # | ruling | recommend |
|---|---|---|
| W2-1 | close `open-items/2026-06-17-l5-scope` — answered by signed K3 kill + Phase E "No genesis vN" | close |
| W2-2 | close `open-items/2026-06-17-s-exponent-fork` — code fork dead since `dc0e7d1b` (2026-06-17); respawn narrow residue: T1.6 docstrings state the def-lock backwards | close + respawn |
| W2-3 | `open-items/2026-08-14-board-check-date-blanking` — pick closure; census: option 1 (header-line-only date normalization) is cheapest | option 1 |
| W2-4 | docket key `32` collision — rename the INFRA+HYGIENE header (`2026-07-10_rulings-docket.md:2368`) with dated renumber note; key `22` is a by-design continuation, leave | rename |
| W2-5 | F-row tracker re-scope: one combined read pass with per-row hit ledgers (10× cut) | re-scope |
| W2-6 | `.agents/`: 11 force-tracked files inside a `.gitignore`d directory — pick tracked or ignored, not both | untrack or carve out |

**Need a short walk** (existing open-items where noted):

- `manifest-type-residue` (18 rows confirmed at HEAD) · `p19-flyby-readjudication` · `seventh-calibration-role` — already on the desk
- `stage16-rerun-amendments` — its branch is gone; tip `54fa23cd` survives only as tags; a Rule-12 retraction is stranded off main. Re-point at the tag + re-scope post-K3
- **the orphaned P2 formatting ruling** — new open-item `2026-08-17-repo-formatting-p2-orphaned-ruling` (the owed adjudication was tracked on no current surface; third instance of the untracked-authorization class)
- disposition of the **3 stale-DIRTY worktrees** (staged divergent content — inspect, then land-or-discard per file)
- **95 unreferenced drivers** policy — new open-item `2026-08-17-unreferenced-drivers-policy`
- **repo weight** policy (162 MB in 8 files >10 MB ≈ 24 % of pack; 29 MB build outputs tracked under `src/`) — new open-item `2026-08-17-repo-weight-policy`
- the Smith-chart residual from the standing-decisions lane (fell off every tracked surface — locate + re-track or declare dead in the sitting)

## Wave 3 — serialized lanes, after Waves 1–2

1. **Figure/data migration lane (REVIVED 2026-08-18, Wave-2 D15f-3)** — the ratified P1
   Option-1 migration, bundled with the D13 drivers-verification lane: verify generators →
   migrate cited figures/data + repoint drivers → archive confirmed-dead drivers. One
   link-coupled discipline, one sequencing.
2. **research/ archive sweep**
   > ★ **Census-methodology note (2026-08-19, banked from the PR-7 execution — MANDATORY for
   > this sweep and any future orphan census).** Literal basename grep over-reports orphans.
   > Four citer classes were caught only by extra methods, three of them live catches that
   > would have deleted cited figures: (1) **ledger-only citers** (the D15c axis, ~24 files);
   > (2) **brace-expansion citers** (`fig_v5_{reach,…}.png`); (3) **brace+glob citers**
   > (`coax_ring_fig{1,2,3}_*.png`); (4) **directory-level citers** (a doc citing the
   > figures' *directory* with a count, no filenames). Minimum method set: python
   > basename+stem walk ∪ `git grep -F` ∪ brace/glob expansion ∪ parent-directory scan.
   > **Addendum (2026-08-19, PR-8):** the methods err in BOTH directions. Stem matching
   > MANUFACTURES citers — a `.png` reads as cited because docs cite its `.pdf` sibling, and a
   > LaTeX `\label{fig:...}` matches a stem without referencing any file — so method-1 stem
   > hits must be validated line-by-line (extension-less `\includegraphics` = real;
   > sibling-extension or label = false). Method-4 must distinguish a directory cited AS a
   > figure container from one appearing inside another file's path. Fifth citer class found:
   > **generator-named-as-figure** (a result doc citing the producing `.py` as "Figure:").
 — policy exists, unenforced; 1,153 files outside `_archive`, heuristic upper bound ~76 candidates. One lane, batch PRs.
2. **F-row combined read pass** — after the W2-5 re-scope; discharge the ten rows in one 175-document read with per-row hit ledgers.
3. **Ringdown wave** — vol3 ch08+ch15, backmatter/07, vol9 ch03:205 (12 gated findings). **Correctly gated on cold-Q; no action until the gate lifts.** Listed so its silence reads as gated, not forgotten.
4. Owed reconciliation tail — 4 board corrections + the addenda micro-lane from the manuscript-reconciliation epic.

## Explicitly NOT worth doing (truth-per-token)

- Manual burn-down of the **2,996** link advisories or **2,571** anchor-drift warns — FP-dominated (2,128 of the drifts are the tool's documented false-positive classes, e.g. TeX-escaping). Tool-precision problem; a reading lane would be waste.
- The 51 figure-duplicate groups (8 MB) without a propagation-policy ruling first.
- Sweeping all 778 driver docstrings (10-sample found 2 stale; rate does not justify a sweep).
- Anything in `research/_archive/` or L3 bodies — Q1 by standing rule.

## Census count appendix (for later drift checks)

open-items 60 (29 ROUTED-TO-GRANT / 19 OPEN / 6 QUEUED / 3 PARKED / 2 REGISTERED / 1 OPEN-IN-WALK; 60/60 anchors resolve) · local branches 172 (105 merged; 89 free-now) · origin branches 9 (3 merged-undeleted-untagged: `docs/substrate-noun-ontology`, `open-timestamp-claims`, + 1; 4 parked-unmerged) · stale `pr/*` refs 859 · worktrees 23 (1 main, 2 active, 7 broken-tmp, 10 stale-clean, 3 stale-dirty) · tags 340 (282 audit, 52 archive) · false status lines 15 (11 orchestration + 4 research) · verify-md-links: 0 gating / 2,996 warn · verify-anchor-content: 2,571 drift of 3,513 checked · KB orphans: effectively nil (1 real non-fixture of 851 files) · duplicate blobs: 158 groups / 96 MB (88 MB = the one netlist tree) · unreferenced drivers 95 of 778 (`src/ave` modules: 0 of 179) · skip/xfail sites 23 · tracked >10 MB: 8 files / 162 MB.

### ENTRY 2026-08-23-research-archive-sweep-census (2026-08-23): implementer — Wave-3 lane 2, the `research/` archive-tier census and its zero-move outturn

- **Class: census + adjudication against a RATIFIED policy, NOT a policy change.** This entry
  applies `_orchestration/2026-07_repo-conventions.md` §(b) archive-tier criteria (`:97-110`,
  RATIFIED at `:13`) to the flat `research/` corpus. It mints no claim, moves no grade, opens no
  physics question, and does **not** amend the criteria. Where the criteria turn out to be
  near-empty on this corpus, that is reported as a measurement, not repaired by loosening them.

**Outturn: 30 candidates adjudicated, 0 moved, 30 HELD.** No file in `research/` passes the
ALL-of criteria cleanly at this HEAD.

---

#### §1 — Scope and the HEAD-true denominator

Measured at branch base `9dd64664` (`origin/main` at lane start), `git ls-files` over `research/`:

| set | count |
|:--|--:|
| tracked under `research/` | 1,321 |
| outside `research/_archive/` | **1,168** |
| of those, `.md` | **875** (874 flat + 1 in a data subdir) |
| non-`.md` outside `_archive` | 293 (`drivers/` 135, `figures/` 101, `data/` 2, plus flat artifacts) |

The epic's lane line (`_orchestration/2026-08-17_repo-cleanup-epic.md:198`) states *"1,153 files
outside `_archive`"*. HEAD-true is **1,168** — a +15 drift, flagged not fixed (the epic doc is
another lane's frozen text).

**Sweep scope = the 875 `.md` docs.** §(b) is a policy about research *documents*; the non-`.md`
artifacts under `research/drivers|figures|data/` are the figure/data axis already discharged by
PR #991 / #992 and are out of this lane.

#### §2 — Method: the six mandated citer classes, plus a seventh

The mandatory method set (epic doc `:177-197`) was run in full. Corpus searched = **4,283 tracked
text files** (`.md .py .tex .json .jsonl .yaml .yml .txt .sh .bib .toml .cfg .ini .html .js .csv`).

| # | class | method | outturn on this sweep |
|:--|:--|:--|:--|
| 1 | ledger-only | python basename walk + citer-file ranking | dominant class; see §5 |
| 2 | brace-expansion | brace expander over `{a,b}` groups | **3 live catches** — decisive |
| 3 | brace+glob | expander ∪ `fnmatch` | 0 beyond class 2 |
| 4 | directory-level | parent-dir scan (1,439 lines) | 0 file-level citations |
| 5 | generator-named-as-figure | `.py` citers scanned separately | 0 for `.md` targets |
| 6 | f-string loop generators | n/a — `.md` docs are not loop-generated | not applicable |
| **7** | **corpus-sweep result artifacts** | **new this sweep — see below** | **13 candidates re-tiered** |

**Second independent method, as required.** Every "0 citers" claim was re-probed with
`git grep -F` on both the full basename and the bare stem (33 candidates × 2 probes). The shell's
`grep` is ugrep and was not used for any receipt. The two methods agreed on every candidate.

**Both-directions validation (the PR-8 addendum).** `git grep` returned 3 hits my python walk did
not, and all 3 were **sibling-extension false positives** — code citing the `.json` twin, not the
`.md`:

- `src/scripts/vol_1_foundations/genesis_v6_pump_isolation.py:229` → `..._result*s*.json`
- `src/scripts/vol_1_foundations/genesis_v6_snap_channel_adjudication.py:194` → `..._result*s*.json`
- `src/ave/solvers/tethered_pivot_x34b.py:78,577` + `src/tests/test_tethered_pivot_x34b.py:12`
  → `research/2026-07-10_tethered-pivot-rerun_result.json`

Validated line-by-line and discarded as citers of the `.md`. (They do establish that those docs
have live, test-consumed data siblings — which bears on "superseded", and is recorded in §4.)

**Class 2 paid for itself.** Three docs that both literal methods scored as zero-citer are in fact
cited, via `{prereg,result}` brace forms no basename grep can see:

| doc | brace citer |
|:--|:--|
| `research/2026-06-11_alpha-boundary-energy_result.md` | `_orchestration/2026-06-11_session-handoff.md:135` |
| `research/2026-07-10_tethered-pivot-rerun_result.md` | `manuscript/ave-kb/common/program-arc-map.md:269`; `_orchestration/2026-07-10_orchestration-board.md:29` |
| `research/2026-05-18_prime-n-soliton-stability-result.md` | `research/2026-07-09_superband-carrier-fork_prereg_FROZEN.md:43` |

A widened re-run (any `{a,b}` group on any line containing `.md`, no `research/` prefix required)
confirmed exactly these 3 and no others.

**★ Seventh citer class, banked: corpus-sweep result artifacts.** Two machine-generated driver
dumps inside `research/drivers/` embed hundreds of corpus paths as grep-hit receipts:
`bound_response_carve_results.json` names **346** distinct research docs and
`ag_derivation_lane_results.json` names **218**. A literal citer count scores every one of those
as "cited". They are **frozen scan receipts, not live-claim citations** — the path appears because
a sweep matched a line, not because a claim depends on the doc. Any future orphan census over a
corpus that contains its own sweep dumps must tier these out, or the citer count is meaningless.
Note the converse hazard: because the dumps are frozen receipts of a scan at a date, **repointing
a path inside them would falsify the receipt** (vacated-cite pattern — the old path *is* the
record). This is a reason such docs are hard to move, not a reason to rewrite the dumps.

#### §3 — The candidate funnel, and the delta against the ~76 heuristic

| stage | count |
|:--|--:|
| `research/*.md` outside `_archive` | 875 |
| less: has a live non-generated citer (criterion 2 fails) | −842 |
| **zero live citers by any literal method** | **20** |
| **only machine-generated-artifact citers (class 7)** | **13** |
| less: brace-expansion citers found (class 2) | −3 |
| **candidates carried to per-file adjudication** | **30** |
| pass ALL-of criteria cleanly | **0** |
| **HELD** | **30** |

**Delta against the heuristic.** The lane line asserts *"heuristic upper bound ~76 candidates"*
(`_orchestration/2026-08-17_repo-cleanup-epic.md:198`). **That number carries no derivation
anywhere in the epic doc** — `git grep -n -F '76'` over the epic returns only `:198` itself plus
unrelated hits (a PR number, a line reference, a figure count). It is an unsourced estimate, so
the delta cannot be reconciled against its method; it can only be replaced. Measured funnel:
**33 pre-adjudication, 30 post-brace-screen, 0 clean-pass.**

Two independent screen directions were run so the funnel is not an artifact of screen order:

- **Criterion-2 first** (zero-citer → read for supersession) — the funnel above: 30 → 0.
- **Criterion-1 first** (self-declared supersession → check citers): **49** docs declare
  supersession in their first 25 lines. Of those, **exactly one** has zero live citers —
  `research/2026-06-15_passive-eigenmode_result.md` — and its supersession marker *is* a
  `🔴 RULE-12 CORRECTION` banner at `:5`, i.e. the NEVER-if fires on the very line that
  establishes criterion 1. The other 48 are blocked by criterion 2.

Both directions converge on zero. That convergence is the substance of §5.

#### §4 — Per-file adjudication (the 30)

#### §5 — The structural finding: why the ALL-of criteria are near-empty by construction

#### §6 — This ledger is itself a citer (self-referential disclaimer)

#### §7 — Routed, not ruled

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

Every candidate was **read**, not grepped, for criteria (1) superseded and (3) honesty-trail — a
search can report the state of a marker, it cannot establish that a later doc carries a doc's
claims. Each row names the criterion that fails and the receipt for it. Grouped by HELD reason.

**H1 — honesty-trail record; the NEVER-if at `:106-107` fires directly (8 docs).**
These are *"RETRACTED / walk-back / correction record"* by their own construction. Policy: *"These
are UNTOUCHABLE — never archived, never rewritten, never banner-stamped."*

| doc | receipt |
|:--|:--|
| `2026-05-17_substrate-velocity-honest-scoping-meta-doc.md` | `:69` — `\| αc/(2π) is FLOOR for decoupled populations \| … \| FALSIFIED \| WALKED BACK \|`; the doc's §1 is titled *"The three walk-back iterations (timeline)"* |
| `2026-06-15_passive-eigenmode_result.md` | `:5` — `🔴 RULE-12 CORRECTION (2026-06-16; original NEGATIVE-A text below PRESERVED unedited)`; `:1` carries a `SURFACE-NOTE 2026-08-19` explicitly *"flagged for the pre-merge audit + Grant"* |
| `2026-07-14_reflection-coefficient-correction-note.md` | `:1` — `# CORRECTION NOTE — _reflection_density Γ² coefficient 1/64 → 1/16`; the doc *is* the correction record |
| `2026-08-12_layer-carve_walk-record.md` | `:24` — `## §1 — THE FOUR CORRECTIONS (orchestrator claims, withdrawn or repaired)` |
| `2026-08-12_common-mode-continuum-image_derivation.md` | `:201` — `🔴 STRUCK 2026-08-12 (PR #963 adversarial audit)`; plus a `🔴 RETRACTED` block at `:256`. Also 11 days old — nothing has had time to supersede it |
| `2026-06-10_genesis-v6-snap-channel-adjudication_result.md` | `:70` — `Rule 12 (substitution-not-retraction): the v5 SNAP-LOCKED slot's 🔴 demotion stands` |
| `2026-06-10_coax-ring-secondary_result.md` | `:3` — `🔴 SUPERSEDED IN PART (2026-06-10) — see the VERDICT ADDENDUM at the foot of this doc`; the addendum lives *in* this doc, so archiving moves the correction away from the claim |
| `2026-07-20_constituent-cage-ensemble_derivation.md` | `:45` — `🔴 The self-labeled "load-bearing result" below the strike is INVERTED (Rule 12, body preserved)`; further Rule-12 strikes at `:33`, `:51` |

**H2 — frozen prereg, or the analytic companion of one, with no evidence the claim is dead (5 docs).**
The NEVER-if names *"a frozen prereg of a live claim"*. Establishing a claim is **not** live is a
matrix adjudication this lane has no mandate to perform, so these are held by construction.

| doc | receipt |
|:--|:--|
| `2026-06-06_electron-genesis-phase2-moving-bulk-prereg.md` | `:5` — `**Status:** PREREG FROZEN — **GATED on Phase-1**` |
| `2026-06-07_two-node-alpha-projection-test.md` | `:3` — `**Status:** FROZEN PREREG before driver run; result appended after execution.` (result at `:117` = Outcome C negative) |
| `2026-06-25_alpha-delta-strain-selector_prereg-v3.md` | `:3` — `**Date frozen:** 2026-06-25 · **Supersedes v1/v2 functional targets**` — it supersedes others; nothing supersedes it |
| `2026-07-21_boundary-strain-amplitude_derivation.md` | `:4` — `**Class:** DERIVATION (analytic Leg A of the frozen prereg research/2026-07-21_boundary-strain-amplitude_prereg-FROZEN.md)`; carries its own `★RE-SCOPE` correction at `:62` |
| `2026-06-10_genesis-v6-pump-isolation_result.md` | `:4` names a frozen prereg; the doc's data sibling `..._results.json` is written by a live driver (`genesis_v6_pump_isolation.py:229`) |

**H3 — open / gated / pending: criterion (1) fails, nothing supersedes an unfinished item (10 docs).**

| doc | receipt |
|:--|:--|
| `2026-07-02_ruptured-core-compactness_result.md` | `:7` — `**Verdict: EOS-GATED — Outcome C** (prereg §6), pending` one Grant physics ruling |
| `2026-07-02_arcstar-yield-anchor-scope_result.md` | `:4` — `HOLD canonization. Do NOT merge — push + report.` |
| `2026-06-23_quaternion-left-right-derivative-vsector-crosscheck.md` | `:4` — `**Status:** for review — orchestrator adversarial audit + Grant merge pending.` |
| `2026-06-21_vacuum-cell-representative-print.md` | `:3` — `**Status:** DRAFT / skeleton (sections marked ⏳ are gated on the in-flight audit workflow …)` |
| `2026-06-07_vol0-hold-items-physical-pictures.md` | `:3` — `Each is a Class-O (open) item from the Vol 0 ↔ KB ledger` |
| `cmb-axis-alignment-driver-design.md` | `:164` — `Outcome cell: TBD → **TBD-pending-corpus-citation-resolution**` |
| `2026-07-08_pump-inventory-astrophysical_RESULT.md` | `:6` — `the FINAL make-or-break gate for the P6 sidereal Lorentz-violation flagship`. A live flagship gate result; archiving it would bury the gate |
| `2026-06-23_chiral-srs-optical-activity_result.md` | best-looking candidate in the corpus — it carries an explicit successor pointer at `:10-12`. **Fails anyway:** its own `:15` reads `top-level verdict is UNCHANGED — still FORM-distinct, magnitude-pending, NOT bankable`, and the successor's `:8` names a *different* doc as its prereg context. The successor carries the Phase-1 execution, **not** this doc's claims. Also `:3` classes it a `refute-by-default DEFLATION` record |
| `2026-06-07_sim-math-audit-vs-kb-ledger.md` | `:16` — `## THE headline finding (meta) — the provenance gate itself is stale`; an open findings ledger with unrepaired items |
| `2026-06-20_state-of-program-and-node-characterization.md` | `:7` — `**Scope note.** This is a *snapshot*` with three load-bearing groundings that were `**OPEN PRs** at snapshot time`. A dated snapshot is historical by construction, not superseded; no later state-of-program doc exists in `research/` (checked) |

**H4 — current documentation of artifacts that still exist: criterion (1) fails (3 docs).**
Verified by existence check, not by marker grep.

| doc | receipt |
|:--|:--|
| `2026-06-09_genesis-perf-utils_note.md` | `:3` describes *"Two reusable library modules under `src/ave/utils/`"* — both present: `src/ave/utils/genesis_parallel_runner.py`, `src/ave/utils/fast_winding_extractor.py` |
| `2026-07-12_engine-categorization-guards.md` | `:4` — `**Class:** tooling / methodology (L0)`; all three shipped artifacts present: `src/ave/core/categorization.py`, `src/tests/test_categorization_guards.py`, `src/scripts/verify/categorization_smoke.py` |
| `2026-06-04_qg42-vsign-deltaf-derivation-result.md` | `:3` — `**Status:** PHASE-1 COMPLETE (2026-06-04)`; no Phase-2 doc supersedes it in `research/` |

**H5 — incomplete artifact; nothing to supersede yet (1 doc).**

| doc | receipt |
|:--|:--|
| `2026-06-05_2-3-winding-extractor-result.md` | three unfilled sections — `:14`, `:58`, `:64` all read `_(filled on run completion)_`. An unrun result doc is not a superseded one |

**H6 — in-doc auditor supersession, which is the honesty trail itself (1 doc).**

| doc | receipt |
|:--|:--|
| `2026-05-31_FT-2_delta-AVE-loss-tangent_result.md` | `:5` — `Implementor graded Outcome B; **AUDITOR VERDICT (orchestration) supersedes → leans Outcome C…**`. The supersession is *internal* — the corrected verdict lives in this same doc, so the doc is the record, not the superseded thing |

**Tally: 8 + 5 + 10 + 3 + 1 + 1 = 28.** The remaining 2 of the 30 are
`2026-06-07_figure-staleness-audit-plan.md` (`:1` `# PLAN (frozen)`; no executed successor ledger
exists in `research/` — the figure work was executed under `_orchestration/` PR #991/#992 against
a different scope, so criterion 1 cannot be evidenced) and `2026-06-11_s11-de-novo_result.md`
(`:9` records `refuted=true` on the driver-emitted bin with `demotion executed here (§4.2)` — an
in-doc demotion record, H1-class in substance).

#### §5 — The structural finding: why the ALL-of criteria are near-empty by construction

The zero is not a measurement accident and it is not a conservative reading. **The two ALL-of
criteria are in structural tension with the corpus's own ratified correction discipline**, and the
tension is tight enough that the passing set is nearly empty by construction:

1. **Criterion (1) needs supersession; in `research/` supersession is executed in-place.** This is
   an *empirical* claim about observed practice, not a policy entailment — §(c)'s append-only
   `🔴 RESOLUTION`/`🔴 CORRECTION` rule (`_orchestration/2026-07_repo-conventions.md:142`) is scoped
   to `_orchestration/` epic docs and does **not** formally govern `research/`. What governs
   `research/` is Rule 12 (substitution-not-retraction: preserve the body, add a 🔴 header), and
   this census measured its effect directly: the H1 group in §4 is eight docs whose supersession
   lives inside them as a preserved-body 🔴 banner. So when a research doc is superseded, the
   observed outcome is **not** a replacement doc — it is the same doc, now carrying a correction
   banner. That banner makes it *"a RETRACTED / walk-back / correction record"*, which is exactly
   what the NEVER-if at `:107` declares UNTOUCHABLE. **Satisfying criterion (1) therefore tends to
   trip criterion (3).** The sharpest instance: of 49 docs self-declaring supersession, the single
   one with zero live citers is `2026-06-15_passive-eigenmode_result.md`, whose supersession marker
   *is* its Rule-12 correction banner.
2. **Criterion (2) needs zero live citers. Supersession is normally announced by a citer.** When
   a successor or a ledger does record the supersession, it does so by naming the superseded doc —
   which is a live citation. That is the other 48 of the 49.

Between them, the passing set is: *superseded, but by a mechanism that neither annotated the
original nor named it anywhere live.* On this corpus that set is empty.

**What this means for the epic.** The lane's premise — *"policy exists, unenforced; … heuristic
upper bound ~76 candidates"* — over-estimated yield by assuming an unenforced policy implies a
backlog. The measured position is the opposite: **the policy is already satisfied**, not because a
sweep ran, but because the append-only correction discipline and the citation habit jointly keep
docs out of archive-eligibility. `research/_archive/` holds 153 files; nothing at HEAD qualifies to
join them.

**This is a measurement, not a complaint about the criteria.** The criteria are doing what
cross-cutting invariant 2 asks — protecting the honesty trail — and the correct reading is that the
archive tier is a narrow instrument, not a hygiene sweep. No amendment is proposed here; §7 routes
the question rather than answering it.

**Symmetric-standard check.** Before banking the zero, the funnel was re-derived from the opposite
end (criterion-1-first, §3) precisely because a conservative adjudicator can manufacture a
null by screening in a favourable order. Both orders return zero, and the single doc that survives
the criterion-1-first screen fails on a banner quoted verbatim rather than on judgement.

#### §6 — This ledger is itself a citer (self-referential disclaimer)

⚑ **This entry names all 30 candidates by path.** Any future citer census run over the tracked tree
will therefore score every one of them as *"cited by a live non-`_archive` doc"* — a citer this
lane manufactured. That is the class-1 (ledger-only) hazard, created by the act of recording the
census.

**Handling for future sweeps: this file is a LEDGER-ONLY citer and must be tiered out of any
citer count over `research/*.md`, exactly as the two `research/drivers/*_results.json` sweep dumps
are (class 7, §2).** It is listed here so the exclusion is discoverable from the corpus rather
than rediscovered. The general rule this instance supports: *a census that records its own subjects
by name becomes a citer of them; the receipts doc must declare itself excluded, or it silently
freezes its own candidate pool.*

#### §7 — Routed, not ruled

Three questions surfaced that this lane has no mandate to answer. None is a physics question.

1. **Is the archive tier the right instrument for `research/` hygiene at all?** §5 measures its
   yield at zero and explains why that is structural rather than incidental. Whether §(b)'s
   archive criteria should be re-scoped, or whether `research/` navigability should be addressed by
   some other means entirely, is a conventions-level decision for Grant + the auditor lane. **No
   amendment is drafted here** — per lane discipline, an implementer surfacing a policy gap does
   not also draft the policy.
2. **The two `research/drivers/*_results.json` corpus-sweep dumps are an unmanaged coupling
   surface.** They embed 346 and 218 corpus paths respectively as frozen grep receipts. Any future
   move of any research doc either breaks a path inside them or falsifies a receipt by rewriting it
   (§2). No move is proposed; the surface is flagged so it is priced into whatever the answer to
   (1) is.
3. **Epic doc `:198` carries two numbers that do not survive re-measurement** — *"1,153 files
   outside `_archive`"* (HEAD-true **1,168**) and *"heuristic upper bound ~76 candidates"* (no
   derivation exists in the doc; measured funnel is 33 → 30 → 0). Flagged, not fixed: the epic doc
   is another lane's text and the auditor lane lands corrections to it.

**Gates at tip.** `make verify` PASSED · `verify-md-links` gating **0** (unchanged from base
`9dd64664`) · `verify-docket-keys` no new duplicate keys · `generate_board.py --check` green.
This entry adds one file and moves none, so the link-coupling rule at `:110` is satisfied vacuously.

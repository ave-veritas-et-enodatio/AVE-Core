### ENTRY 2026-08-05-cite-rot-line-existence (2026-08-05): infra — the gating checker now asserts cited lines EXIST and sees backticked cites; posture measured, not assumed

- **Class: tooling, EXECUTED. No physics, no corpus claim.** Discharges options **(2)** and **(3)** of `2026-08-02-cite-rot-checker-gap.md`. Option (1) (promoting the excerpt-anchored content check to gating) is **explicitly NOT implemented** — it still wants its FP-triage pass first, and nothing here half-implements it.

---

#### 1. Re-measured at HEAD (`d5a1b06b`) — the 2026-08-02 numbers were NOT inherited

The 2026-08-02 entry measured through the advisory checker's own summary, which only counts cites it can see. The counts below come from an independent parser that reads all three written forms.

| quantity | count |
|---|---|
| location cites parsed, corpus-wide (`path.ext:NN` + bare `path.ext`) | **32,643** |
| — carrying a `:NN` | **12,505** |
| — backticked-bare, carrying a `:NN` | **11,168** |
| backticked-bare `:NN` cites inside `manuscript/ave-kb/` | **1,697** |
| label-external `[`x`](x.md):NN` (the KB house convention) | **1,219** (984 in KB) |
| in-target `](path.md:NN)` | **118** |
| **line-cites the new pass actually checks** | **11,539** |
| — of those, in the gating (error-source) class (independent probe) | **~2,590** |
| skipped: shape (glob/elision, sibling repo, ephemeral dirs) | 553 |
| skipped: deliberately-historical (backticked SHA on the line) | 361 |

The 2026-08-02 shape held: the backticked-bare form dominates, and it was invisible **end-to-end** — `strip_code()` blanks inline spans before the link regex runs, so neither its path nor its line was ever checked.

**Previously-invisible cites now checked: 11,168 backticked-bare `:NN` cites are parsed for the first time** (1,697 of them in the KB). Their paths are now checked (advisory) and their lines are now checked (gating from a KB source).

---

#### 2. The violation set, and what is real

**GATING class — `dead line cite` (no resolvable candidate file HAS the cited line):**

| source class | count |
|---|---|
| error-source (KB tree + `README`/`LIVING_REFERENCE`/`AGENTS`) | **0** |
| warn-source (`_orchestration/`, `research/`, `papers/`) | **5** |

All five triaged as REAL (not FP), and all five are warn-only under the **pre-existing** source-gating rule — no new exemption was written for them:

1. `_orchestration/2026-06-16_groundup-engine-acceptance-plan.md:221` → `gw-impedance-perturbation.md:30` (file is 20 lines).
2. `_orchestration/clm-0ktpcn-golden-torus-alpha-strengthen.md:100` → `phase-locked-topological-thread.md:187-199` (file is 189 lines; the range end overruns).
3. `research/2026-05-25_clm-0ktpcn-golden-torus-alpha-strengthen-prereg.md:51` → same cite, same overrun (the pair travelled together).
4. `research/2026-06-15_grid-definition-cartography.md:125` → `rupture_solver.py:60-150` (file is 142 lines).
5. `research/2026-07-18_f6-meter-kappa-reval_result.md:281` → `validate.py:1005` (longest of 2 candidates is 193 lines).

*(Quoting those five here re-flags four of them from this fragment — `make verify` reports `dead: 9 (gating: 0)`, not 5. That is the checker being correct about its own evidence list, not noise: this file really does contain four dead cites, deliberately. `_orchestration/` is warn-class, so the gating count is unaffected.)*

**ADVISORY class, at HEAD:**

| kind | total | error-source |
|---|---|---|
| `blank line cite` (line exists, but is empty / decoration-only) | 1,068 | **255** |
| `broken backtick path` (backticked cite whose path resolves nowhere) | 1,682 | **203** |

**⚠ MEASUREMENT BASIS — these counts are CHECKOUT-SENSITIVE, and the first version of this table got that wrong.** The pass walks the filesystem, so a working checkout carrying untracked / gitignored / generated files resolves cite paths that a fresh clone cannot. Measured with this branch's tool: on a **pristine `git worktree` checkout of `d5a1b06b`** the error-source populations are **255** and **203**; on a long-lived local working checkout of the same tree they read **255** and **181** (total 1,626, not 1,682) because local artifacts satisfy paths CI would not have. The row above is the **pristine** measurement — the one CI reproduces — and it is what the flip conditions in §3 are keyed to. This table's originally-published `196` was a dirty-checkout artifact of exactly this kind; corrected here after an independent re-measurement (two methods: the tool's own `is_error_source` split, and a recount of `--advisory-cites report` through a separately-written source-class predicate).

Triage of the 203 error-source broken paths: the large majority are **not cites at all** — they are pattern/placeholder strings that happen to be path-shaped (`volN/claim-quality.md`, `A-NNN-prereg.md`, `_result.md`, `_prereg_FROZEN.md`), references to files that were never tracked (`mad-review/…`), or gitignored trees. A minority are genuinely dead pointers. **This is a triage pool, not 203 confirmed breaks** — the same caveat the 2026-08-02 entry attached to its 1,012.

Sample of the `blank line cite` class, checked by hand: `master-equation.md:78` (content at `:79`), `refractive-index-of-gravity.md:11` (resultbox at `:12`), `pmns-eigenvalues.md:23` (equation at `:24`), `constants.py:589` (comment block at `:590`). Almost all are **one-line drift** — the pointer names the right neighbourhood and the wrong line.

---

#### 3. POSTURE — and the counts that drove it

**`dead line cite` GATES from day one.** Its error-source population is **0**, so nothing is red-lighted, no backlog is gated into existence, and no waiver is needed (`WAIVED_LINE_CITE` ships empty). **The `make verify` 0 is because the gating class is genuinely CLEAN, not because the check was softened.**

**`blank line cite` and `broken backtick path` do NOT gate.** Their error-source populations are 255 and 203 (pristine-checkout basis, §2). Gating either would fail the build on the first merge after landing, and a gate that fails on merge gets bypassed, not obeyed — which is the cite-rot failure mode this work exists to close, reproduced one level up.

**Named flip conditions** (each is a measurement, not a vibe). **Both are keyed to the PRISTINE-checkout population per §2** — a lane proposing a flip must re-measure in a fresh `git worktree`, not in its own working checkout, or it will read a number that is low by the count of its local untracked files:

- **`blank line cite` → gating** when its error-source population reaches **0**, reachable by a repair sweep that re-points each cite to the adjacent content line. The count is printed by every `make verify` run, so the burn-down is visible without a tracker; `--advisory-cites report` emits the full list as the work queue.
- **`broken backtick path` → gating** when its error-source population reaches **0**, which requires a *classification* pass first, not just repairs: the placeholder/pattern strings (`volN/…`, `A-NNN-…`, `_result.md`) need either a documented non-cite spelling or an extension of `cite_target_uncheckable`. **Do not flip this one by widening the skip set to make the number go to zero** — that converts a real check into a checklist.

---

#### 4. Two corrections to the routing entry's own framing (flag-don't-fix)

**(i) "assert the line has at least N lines" does NOT catch the blank-line class.** The 2026-08-02 entry described option (2) as catching "the blank-line / deleted-tail / bogus-path cites, e.g. the `q-g19a:108` instances". Verified at HEAD: `q-g19a-petermann-saliency-closure.md` is **256 lines**, and line 108 is `>` — a blockquote continuation. **A blank line is a line that exists**, so a pure existence check passes it. That is why the `blank line cite` kind was added alongside — it is the check that actually reaches the entry's motivating instance, and it is advisory for the reason in §3.

**(ii) the second motivating instance is not in this class at all.** `04_generative_cosmology.tex:467` — the entry's "cites a string absent from that file at every line" case — resolves to a **613-line** file, so `:467` exists. That is **content drift**, which option (2) explicitly does not attempt and which remains `verify-anchor-content`'s (advisory) territory. Recorded, not rescued.

---

#### 5. SHA-pinned and frozen cites

**SHA-pinned: the corpus has NO machine-readable marker.** Searched at HEAD: the convention is free prose — *"as shipped on"*, *"at commit"*, *"frozen at"*, *"was correct at"* — always adjacent to a **backticked short hex SHA**. That backticked SHA is therefore the only reliable signal, and the pass uses it: any line carrying one has its line-cites skipped. **Measured coverage cost: 96 of the KB's 2,681 `:NN` line-cites (3.6%) sit on a SHA-bearing line** — accepted, and recorded here rather than buried. The named example from the brief — `wall-taxonomy.md` §9 *(as shipped on `c4a546dc`)* in `research/2026-08-05_last-bond-kernel-collapse_prereg-FROZEN.md` — is a **§-section** cite carrying no `:NN`, so it was never in reach of this check regardless.

**PRECISION of that exemption — added 2026-08-05 after the independent verify, because the coverage COST was disclosed and the PRECISION was not.** The exemption is **line-scoped**, and KB lines are not sentences: it skips *every* line-cite on any line carrying a SHA anywhere, while the KB's ledger rows routinely mix one provenance SHA with several **live** derivation cites. Re-measured on a pristine checkout of `d5a1b06b` (identical at branch HEAD):

| quantity | measured |
|---|---|
| KB `:NN` cites on a SHA-bearing line | **96** (3.6% of 2,681) |
| — of those, actually exempted by this rule | **85** (the other 11 are skipped anyway: 3 by shape, 8 unresolvable path) |
| distinct source lines carrying those 96 | **55** |
| — cites sitting on a line of 500+ characters | **89 of 96** (median line 1,655 chars, max 6,112) |
| — cites sharing their line with ≥1 other line-cite | **66 of 96** |
| corroborated by one of the four free-prose phrases the rule is modelled on | **7 of 96 (7%)** — residue **89** |
| corroborated by *any* historical-ish phrasing (deliberately generous superset, built by reading all 55 lines) | **65 of 96 (68%)** — residue **31** |
| **dead cites the exemption hides today** | **0** (re-ran the line check over the 85 with the exemption disabled: 0 dead, 9 blank-line advisory) |

The corroboration rate is **vocabulary-dependent by an order of magnitude**, which is itself the finding: the SHA is a *row-level* token, not a per-cite marker, so no regex over the line can tell which cite (if any) the SHA is pinning. Worked instances, each a live cite riding a SHA's exemption — all three re-verified this session:

1. `manuscript/ave-kb/claim-quality-closure-roadmap.md:76` — a 625-char table row whose provenance column is `[`57b36e5`](…/commit/57b36e5)`, and which also carries **three live derivation cites** (`electron-bh-isomorphism.md:20,39`, `regime-eigenvalue-method.md:43`, `ave-merger-ringdown-eigenvalue.md:29`). All three are exempted by a SHA that pins none of them.
2. `manuscript/ave-kb/CLAUDE.md:75` — 3,941 chars. Here the historical prose is **genuine** (*"byte-identical at `:439` from 2026-05-18 (`b0b9d4ea`) through 2026-05-31 (`367669ef`)"*) — and it exempts the live `operators.md:54` sitting on the same line. A correct pin and an unrelated live cite are indistinguishable to a line-scoped rule.
3. `manuscript/ave-kb/claim-quality-closure-roadmap.md:32` — 2,731 chars, five SHAs, live `q_g47_path_b_k4_eigenmode.py:54` among the exempted.

**Forward risk, stated plainly:** a dead cite that lands on a ledger row which happens to mention a commit passes the gate silently — and ledger rows are exactly where cite-rot concentrates. Today that risk is **realised zero times** (row above), so this is a precision disclosure, not a defect. **Do not "fix" it by widening the SHA regex** — that lowers precision further. The fix, if the residue ever bites, is an explicit per-cite historical marker convention, which is a corpus-convention decision, not an implementer's.

**Frozen documents are never forced to change.** `research/*_prereg-FROZEN.md`, dated result docs, and `_orchestration/docket-entries/*` are all **outside** the error-source set, so their findings are warn-only under the pre-existing source-gating rule — no new carveout was written, and this fragment's four warn-class hits (§2) prove the path. A regression test asserts it directly. If a byte-frozen document ever lands *inside* the KB tree, `WAIVED_LINE_CITE` is the escape hatch, and it carries the same anti-rot property as `WAIVED_KBLEAF`: a waiver that outlives its subject is itself a gating failure.

---

#### 6. Option (3) — the NEW-cite excerpt ratchet

`make verify-new-cite-excerpts` (`CITE_BASE=<ref>`, default `origin/main`) requires a verbatim excerpt beside every line-cite a branch **ADDS** to the canonical-authority surface. Backlog-free by construction; the ~13k existing cites are untouched. Convention documented in `manuscript/ave-kb/CONVENTIONS.md` (new "Location cites" section, incl. a gate-coverage table).

**Back-tested over the last 25 merges to `main`: 4 of the PR merges would have been blocked**, each adding 1–8 excerpt-less KB cites (`wall-taxonomy.md`, `translation-circuit.md`, `common/claim-quality.md`). That is the intended behaviour, not a defect — but it is a workflow change with blast radius past the checker, so it lands as a **SEPARATE, NON-REQUIRED CI job**, matching the repo's existing `engine-sims` posture. **Flipping it to required in branch protection is the orchestrator's call, not the implementer's** — it is a one-line branch-protection change, no code edit. (The window slides: re-running the back-test today reads 21 PR merges among the last 25, same 4 blocked. The finding is the shape, not the integer. Those 4 are the **backtick-only** figure; after the recognizer widening recorded below it is **3**.)

**RECOGNIZER WIDENED 2026-08-05 after the independent verify — the ratchet was rejecting a convention the corpus actually uses.** The first version recognized excerpts in **backticks only**. The corpus also writes verbatim excerpts as **emphasised quotes** — `*"…"*`, `**"…"**`, `_"…"_` — which is the register most KB rulings quote prose in. Measured over the same back-test window by re-running the whole back-test with the widened recognizer and differencing the blocked sets (PR #878's five were additionally read by hand):

| back-test finding | count |
|---|---|
| blocked cites, backtick-only recognizer | **21** (across **4** PR merges) |
| — that DO carry an excerpt, written as an emphasised quote | **6 (29%)** — style false positives |
| — genuinely excerpt-less | **15** |
| blocked cites, widened recognizer | **15** (across **3** PR merges) |
| PR #878's blocked cites | **5 of 5** were style false positives — 3 on the cite's own line, 2 straddling a hard line-wrap; it now passes clean |

Two verbatim instances, at PR #878's head `1e74b38d`: `manuscript/ave-kb/common/claim-quality.md:1678` cites `src/ave/core/k4_tlm.py:396-398` next to *"Conserves total power"* on the same line; `manuscript/ave-kb/common/transfer-cost-theorem.md:86` closes *"…mode-count or a click, never a valve"* that OPENED on line 85, with the cite on 86. (The first line number is PR-#878-relative: that content sits at `common/claim-quality.md:1735` on today's `main` — a 57-line drift in one day, and a small demonstration of why the excerpt requirement exists. The `transfer-cost-theorem.md:86` wrap is unmoved and verifiable at HEAD as written.)

**Fix taken: option (a) — widen the recognizer**, not option (b) (document that backticks specifically satisfy the gate). Reasoning: a gate that rejects a live convention does not teach the convention, it teaches the workaround, and the workaround here is to reword correct provenance into a form the tool likes. The widening is applied to the **shared** `associate_quote`, so the ratchet and the advisory drift check agree on what an excerpt is — accepting a style the drift checker could not then re-anchor would make the cite "self-verifying" in name only, which is the whole rationale of the requirement.

Measured effect on the advisory pass (same tree, tool before vs after): cites gaining an excerpt association **+626**; checked 2,050 → **2,308**; anchored-OK 525 → **640**; drift 1,525 → **1,668**, i.e. the drift RATE falls 74.4% → **72.3%**. Runtime +7%. Nothing moves in the gating class — `verify-anchor-content` is advisory and the ratchet is a non-required job. PR #878 back-tested against the widened recognizer now reports **OK — every added load-bearing line-cite carries an adjacent excerpt**.

Guard against the obvious failure mode of a wider recognizer: three regression tests assert it does **not** swallow decoration (a `* "bulleted quote"` bullet-plus-space is not the excerpt style, a quoted path-cite is a cite not content, and sub-`MIN_QUOTE_LEN` fragments stay trivial). **This must be settled before anyone considers flipping the ratchet to required** — it now is.

---

#### 7. Bug caught by running it (Rule 10)

The first implementation's pattern filter used `\.{2,}`, which swallowed `..` **parent-dir hops** as if they were `...` elisions — silently skipping **639 of the KB's 2,650 line-cites (24%)**, the entire `../vol1/.../leaf.md` house style. Static reading did not catch it; the mutation regression test did, because its planted link-ext cite never fired. Fixed to a per-segment test: shape-skips fell 2,025 → 553 and checked lines rose 10,625 → 11,539. The mutation is now a permanent test.

A second instance of the same class, caught by two-method verify-before-cite during authoring: an *illustrative* cite drafted for the new CONVENTIONS section quoted an excerpt that is **not** at the line it named. It was replaced with a deliberately synthetic path, and the section now says so in as many words — an example cite that names a real file is the seed of the next stale pointer.

---

- **Receipts:** `manuscript/ave-kb/tools/verify-md-links.py` (new line-cite pass + module docstring carrying the posture); `manuscript/ave-kb/tools/verify-anchor-content.py` (`--new-cites` ratchet + `tests/fixtures` crawl prune); `manuscript/ave-kb/tools/tests/test_verify_md_links.py` (**10** new tests incl. the mutation regression) and `.../test_verify_anchor_content.py` (**7** new: 4 for the ratchet, 3 for the widened excerpt recognizer) — **17 new tests**, counted two ways (`def test_` delta vs `d5a1b06b`, and pytest collection: 11→21 and 3→10); fixture repo at `manuscript/ave-kb/tools/tests/fixtures/linecheck/`; `Makefile` target `verify-new-cite-excerpts`; `.github/workflows/verify.yml` job `new-cite-excerpts`; `manuscript/ave-kb/CONVENTIONS.md` "Location cites" section. All counts above reproducible via `make verify-md-links` and `--advisory-cites report`.

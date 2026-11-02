# Handoff brief — PR-triage wave 1, mechanical lane (park seven PRs, extract residue, repair #1054)

**Date:** 2026-09-30 · **Lane:** mechanical / hygiene. Polish tier: one pass plus machine checks, no panel. **Authority:** R61 ([`docket-entries/2026-09-30-ruling-r61-pr-triage-wave1.md`](docket-entries/2026-09-30-ruling-r61-pr-triage-wave1.md)), and for #1054 Grant's 2026-09-27 GO quoted in that PR's body. **Author:** orchestrator. **Grant launches and picks model and effort; a cheaper model is appropriate.**

**Expected truth-yield:** none. This lane preserves content and removes clutter. It changes no belief, band or number. Findings you cannot fix in one pass go into your report as declared residue, not into repair rounds.

**Line numbers and quoted values in this brief are DISPATCH-GLOSS.** Re-read every one at edit time. Where the file disagrees with this brief, the file wins and you report the difference.

---

## Step −1 — precondition

`git fetch origin` and then `git cat-file -e origin/main:_orchestration/docket-entries/2026-09-30-ruling-r61-pr-triage-wave1.md` must succeed. `git grep -l -E '^# R61 ' origin/main -- _orchestration/docket-entries` must list exactly the R61 file. R60's provisional note also mentions R61, which is expected and not a claim. If R61 is not on main, or its number collides, STOP. Tag messages are immutable, so they must not cite a path or number that could still move.

## Step 0 — protect #1054 first

#1054's title carries no review tag, and the PR has a known defect. Retitle it before anything else:

```
gh pr edit 1054 --title '[DO-NOT-MERGE][REVIEW: pending-orchestrator] README/CLAUDE.md: α is a calibration input, not derived'
```

Read it back with `gh pr view 1054 --json title`.

## Step 1 — archive tags (lossless; nothing closes in this step)

Method: archive-tag-first, as in the 2026-07-19 branch scrub (`_orchestration/2026-07-10_rulings-docket.md`, search `archive-tag-first (lossless)`), but **annotated**. Most scrub-era tags on origin are lightweight, so do not copy them.

| PR | branch | head at 2026-09-30 | tag |
|---|---|---|---|
| #1021 | `research/2026-08-26-wall-first-walk` | `ff37a7fb` | `archive/research/2026-08-26-wall-first-walk` |
| #1023 | `research/2026-08-26-virtual-neutral-prereg` | `2db3aa98` | `archive/research/2026-08-26-virtual-neutral-prereg` |
| #1024 | `research/2026-08-26-build-eo1-t2x` | `696a21bc` | `archive/research/2026-08-26-build-eo1-t2x` |
| #1025 | `research/2026-08-26-virtual-neutral-arc` | `e0b771cd` | `archive/research/2026-08-26-virtual-neutral-arc` |
| #1026 | `infra/2026-08-26-rule12-append-only-gate` | `4580efa5` | `archive/infra/2026-08-26-rule12-append-only-gate` |
| #1027 | `research/2026-08-27-cold-vacuum-ee-mapping` | `2190a157` | `archive/research/2026-08-27-cold-vacuum-ee-mapping` |
| #1033 | `research/2026-08-28-qpoint-constitutive` | `596b408e` | `archive/research/2026-08-28-qpoint-constitutive` |

For each row:
1. `gh pr view <N> --json headRefName,headRefOid` must match the table. **If a head moved, STOP**: someone is working on it.
2. `git ls-remote origin 'refs/tags/archive/<branch>*'` must print nothing. A local `git tag -l` does not prove the remote is clear.
3. `git tag -a archive/<branch> <full-sha> -m 'PR #<N> parked 2026-09-30 per R61 (_orchestration/docket-entries/2026-09-30-ruling-r61-pr-triage-wave1.md)'`
4. `git push origin refs/tags/archive/<branch>`
5. Verify on the remote: `git ls-remote origin 'refs/tags/archive/<branch>^{}'` must print the full head SHA. Do not trust the exit code; a push can exit 0 and push nothing.

**Do not delete any branch.** R61 does not rule on branch deletion. The pointers stay, so a parked PR can simply be reopened.

## Step 2 — residue PR (one branch, one PR)

Work in a throwaway worktree off `origin/main` on branch `orchestration/2026-09-30-wave1-park-residue`. Every edit is either a **new file** or an **end-of-file / same-line** change, so no existing cite shifts. **Rule for every new open item: `source` must be a file that exists on `origin/main`. Archive-tag paths go in the body only.** Frontmatter follows `_orchestration/open-items/README.md` exactly: `id`, `title`, `status`, `owner`, `opened`, `source`, and `anchor` (verbatim text that occurs exactly once in `source`). **Wrap every `anchor` and `title` value in double quotes**: both anchors below contain `#` or `'`, and the parser takes quoted values verbatim.

**2a. Open item `_orchestration/open-items/2026-09-30-wall-arc-residue.md`** (owner `lane`, status `OPEN`, source = the R61 docket file, anchor `The A1-vs-T2 wall contradiction becomes one two-sided question for a later sitting.`). Body sections, each citing its source as `archive/<branch>:<path>` after you re-read it:
- **Evidence for the A1-vs-T2 wall question (recording only; not a Grant ask; nothing is corrected).** The question itself (which wall confines the single electron: the A1 mass wall, the T2 self-trap wall, or each a different channel?) already has a home. It is open PR #1040's item `cage-ownership-provenance`, which is not yet on main. Record here, as seeds for that item:
  - Side A, quoted verbatim in its LaTeX source form: the `device-circuit-models.md` blockquote beginning `**Two coincident $\Gamma=-1$ walls — do NOT re-collide.**`, and the `def-cf1srf` block in `manuscript/ave-kb/common/vocabulary-register.md`. Include the date side A's sentence was written; `git log -S` finds the commit.
  - Side B, verbatim: the `def-vyvsn1` block as it stands on `origin/main`. Its confining clause's 2026-06-30 attribution is **disputed by #1040**, which removes that clause.
  - Write "to be merged into `cage-ownership-provenance` when #1040 lands". Cross-link `_orchestration/open-items/2026-08-25-invariant-s2-sector-split.md`. Edit neither item.
  - The reopen trigger for #1023 and #1025 is Grant's answer to that question.
- **Polish residue:**
  - T3.3 off the operating point (#1025): `sup-1ecv2m` was probed at A = 0.95/0.99 while the electron's A1 core sits at A = √α. `device-circuit-models.md` cites T3.3 as support (search `T3.3`). Recompute Γ_bulk(√α) yourself before writing a number.
  - W4-4 (#1021): `peierls-nabarro-paradox.md` (the moving electron is matched) vs `de-broglie-standing-wave.md` (a Γ=−1 mismatch). Both are already weak-graded on main; record the pair and rule nothing.
  - R-2 (#1021): is `cosserat-mass-gap.md`'s "T2/ω" the same object as `port-register.md`'s "channel 4 (micro-rot.)"?
  - VN-F1, restated (#1023): "unreachable at the default cap, reachable via an A_cap override", not "dead code".
  - VN-F5 (#1023): the scalar `solve_tone` accepts `term=None` and returns the trivial zero as converged (`src/ave/solvers/harmonic_balance_srs.py`, search `def solve_tone`). This is already routed by R58 §4; cross-link it, do not re-route it.
  - The parked virtual-neutral register-move line, with both tags.
- **Open items that die with the parks.** Re-read each on its branch before writing its line:
  - #1021 `electron-rest-energy-channel`: dropped, because its content is already canon (confirm in `cosserat-mass-gap.md`).
  - #1021 `wall-first-reframe-audit`: dropped, because the record parks and its lead item W1-1 is answered in `harmonic_balance_srs.py`'s docstring (search `T2/Cosserat channel is NOT`; the sentence wraps onto the next line).
  - #1023 `prereg-control-termination`: dropped; the prereg parks and the reopen trigger is above.
  - #1025 `device-circuit-models-165-correction` and `virtual-neutral-register-move`: folded into this item.

**2b. Open item `_orchestration/open-items/2026-09-30-constitutive-arc-residue.md`** (owner `lane`, status `OPEN`, checker tier, source = the R61 docket file, anchor `#1033's Phase-1 stays resumable from its tag.`). Body:
- Mercury regime axis: the Mercury row of `vol3/cosmology/ch14-orbital-mechanics/orbital-regime-table.md` ("II (Yield)") vs the solar-surface row of `vol1/operators-and-regimes/ch7-regime-map/domain-catalog.md` ("Regime I"). Do both use the same axis? Cross-link open PR #1030, whose DELTA-3 targets the same ch14 row, and the gravity audit's Q0.
- The `domain-catalog.md` white-dwarf row: the kernel is used as an index.
- The scope qualifier on INVARIANT-S2 in `manuscript/ave-kb/CLAUDE.md` (search `INVARIANT-S2`).
- From #1027: its C4 question (the clause-Q ε11 reference vs the port-amplitude symmetry), cross-linked to `_orchestration/open-items/2026-08-29-phase-space-tank-state.md`. That item is Grant's fragment: **do not edit it** (open-items README rule 3). Also record that #1027's own item `cold-vacuum-ee-mapping-audit` is dropped because the record parks.
- #1026's item `rule12-drift-survey` is dropped because the gate parks; the survey is preserved at the tag. Note that #1026's modification to `electron-identity-latex-readme-followups` does not land.
- The resume point for #1033's Phase-1: the question (does the substrate force a gap S(ε11) independent of LC?) and the tag.

**2c. Dated surface note (end-of-file append)** on `research/2026-08-29_h1-dc-circuit-objects_WALK.md`. Its fence line beginning `**Bond \(L,C\leftrightarrow\mu,\varepsilon\) graded map is unlicensed**` cites `[branch:#1033]`. Quote that anchor text rather than a line number, and write two parts:
- **Always:** "#1033 is parked at `archive/research/2026-08-28-qpoint-constitutive` (R61)."
- **Only if verified:** "#1033's own amendment A4 channel-scoped this fence: on the T2/EM channel L = μ0 and C = ε0 is canon Class A." To verify, find the commit with `git log origin/main..archive/research/2026-08-28-qpoint-constitutive --grep='A4 APPENDED'` (expected `9d985eb3`), and quote the Class-A line from `manuscript/ave-kb/common/translation-tables/translation-circuit.md` verbatim. If either fails, write only the first part and report the failure.

**2d. VN-F4 cite fix (same-line edits).** Change `cvr_model.py:161` to `cvr_model.py:170` in both live KB leaves. Each names `gamma_mag_sq_leak`, which is defined at `:170` of `src/scripts/vol_9_device/cvr_ee_sweep/cvr_model.py`; re-check that at edit time.
- `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-bound-resonator-coverage.md`
- `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md`

Do not change the `cvr_model.py:161` cites inside `research/` records; they are frozen. The 2c end-of-file note is this lane's only `research/` edit. Afterwards run `git grep -n -F 'cvr_model.py:161'` and list what remains in your report.

**2e. The generated board.** Run `python3 _orchestration/tools/generate_board.py` once to validate the new items: it fails loud on bad frontmatter or an anchor that does not resolve exactly once. Then restore the board (`git checkout -- _orchestration/BOARD.md`) and **do not commit it**. The post-merge chore regeneration (#1043/#1045 pattern) writes it.

**Checks before opening the PR:**
- `make verify`;
- `make verify-inbound-cite-shift CITE_BASE=origin/main` shows SHIFTED=0;
- `wc -l` unchanged on every edited existing file, except the 2c end-of-file append.

**Open the PR** with a body file, so backticks survive:

```
gh pr create --base main --title '[DO-NOT-MERGE][REVIEW: pending-orchestrator] orchestration: wave-1 park residue — 2 open items, 1 surface note, 1 cite fix (R61)' --body-file <file>
```

Then check that the remote branch SHA equals your local HEAD.

## Step 3 — close the seven PRs (GATED: only after the residue PR is merged)

R61 promises the residue is extracted first. Before closing, both `git cat-file -e origin/main:_orchestration/open-items/2026-09-30-wall-arc-residue.md` and the same check for `2026-09-30-constitutive-arc-residue.md` must succeed. **If the residue PR is not merged when you reach this step, do not close anything.** Report that Step 3 is pending; it runs later, from a relaunch of this step or by the orchestrator.

When the gate is open, for each PR write the comment to a file and post it with:

```
gh pr comment <N> --body-file <file>
gh pr close <N>
```

Never pass comment text inside double quotes: backticks would run as command substitution and silently strip every pointer. Read each comment back with `gh pr view <N> --json comments` and confirm the tag name and SHA are present.

Comment shape:

> Parked 2026-09-30 per R61 (`_orchestration/docket-entries/2026-09-30-ruling-r61-pr-triage-wave1.md`). Head preserved at annotated tag `archive/<branch>` (`<sha>`); the branch is kept. Residue: <item id(s), or "none">. Open items on this branch: <each: folded into X / dropped because Y>. Reopen trigger: <trigger>.

| PR | residue | reopen trigger |
|---|---|---|
| #1021 | `wall-arc-residue` (W4-4, R-2) | none; the record is preserved |
| #1023 | `wall-arc-residue` (VN-F1, VN-F5, the wall-question evidence) | Grant's answer to the wall question (home: #1040's `cage-ownership-provenance`) |
| #1024 | none | a transverse P2 prereg exists (P2 is gated on #1022 and the G2 decisions) |
| #1025 | `wall-arc-residue` (T3.3, register-move line, the wall-question evidence) | same as #1023 |
| #1026 | `constitutive-arc-residue` (drift-survey line) | Grant funds a successor: tool-only, as a non-required CI job (R59 posture). The R59 HOLD becomes a close under R61. |
| #1027 | `constitutive-arc-residue` (C4) | none; the record is preserved |
| #1033 | `constitutive-arc-residue`; the h1-walk surface note | Grant schedules the Phase-1 discriminator |

## Step 4 — repair #1054 (same-line edits; for an auditor read, not self-cleared)

On branch `fix/2026-09-27-alpha-calibration-input`, in a throwaway worktree. Check that each string occurs exactly once before you replace it.

- `manuscript/ave-kb/README.md`. Replace this string:
  ```
  $\ell_{node}$ and $G$ are themselves derived; $\alpha$ is **not** — AVE does not derive $\alpha$:
  ```
  with:
  ```
  For each scale's FORM/VALUE status see [common/form-deriving-value-importing.md](common/form-deriving-value-importing.md). AVE does not derive $\alpha$:
  ```
- `manuscript/ave-kb/CLAUDE.md`. Replace this string:
  ```
  all except $\alpha$ are **derived** from these axioms, while $\alpha$ is a **calibration input**
  ```
  with:
  ```
  $\alpha$ is a **calibration input**
  ```
  The line then reads "… are not axioms themselves; $\alpha$ is a **calibration input** (CODATA) — …". No pointer to the FORM/VALUE leaf goes here: that leaf has no rows for $Z_0$, $\xi_{topo}$ or $V_{snap}$/$V_{yield}$.

The α clause stays exactly as it is. Assert no status for any other constant. Leave the later sentence "Specifically, gravity is the Machian boundary impedance, derived from Ax 1 + Ax 4 symmetric scaling…" untouched (it is a FORM statement) and mention it in your report.

PR body, updated through `gh pr edit 1054 --body-file <file>`:
- Add `_orchestration/docket-entries/2026-08-14-electron-identity-calibration-inputs.md` as authority next to Grant's 09-27 GO.
- Replace the sentence claiming the repo-root README contains no α-is-derived claim. The exact statement: the root README's "On axiom count after Ch 8" paragraph is FORM/VALUE-honest within the same line, but its lead verb ("derives") and a script label ("Run the cold-lattice α derivation") are loose.
- Rewrite both **After:** blocks to the new line text. Delete the sentence "The wording about the other constants is left as it was." (the repair changes exactly that wording).
- The replaced sentence also covered root `CLAUDE.md`. Re-check it with `git grep -n -i 'deriv' origin/main -- CLAUDE.md`, reading the α-adjacent hits, and state that half separately and accurately.
- List the other α-derived sites as **seeds** for the existing item `_orchestration/open-items/2026-08-16-electron-identity-latex-readme-followups.md`, which owns full-read sweeps of these surfaces: the `eq_calibration_constants.tex` header, root `README.md`, `LIVING_REFERENCE.md`, `manuscript/ave-kb/entry-point.md`, `manuscript/ave-kb/common/appendix-derived-numerology.md`. **Do not create a new item and do not edit that one.**

Checks: `make verify`, CI green, `wc -l` unchanged on both files. Leave the title DO-NOT-MERGE; the orchestrator sends one auditor read before any CLEARED.

## Step 5 — report

**Your final message is the report**; Grant relays it to the orchestrator. Also post the same report as one comment on the residue PR, through `--body-file`. Include:
- Step −1 result, and #1054's title after Step 0.
- One row per tag: name, full SHA, and the `ls-remote … ^{}` line.
- Residue PR number and head SHA (remote-verified), the SHIFTED count and the `make verify` result.
- Step 3 status: done, with comment links, or pending the residue merge.
- #1054 new head SHA and check results, plus the untouched gravity sentence.
- The `cvr_model.py:161` cites that remain.
- **Owed to wave 2:** #1022's `repair-round-residuals` item and #1036's picture-lock `[branch:#1033]` line now point at parked PRs.
- **Proposed for the next sitting:** delete the seven parked branch pointers now that their tags verify? (yes/no)
- Every STUCK-POINT and every skipped step.

## Out of scope

- No merges, no CLEARED titles, no branch deletions.
- No edits to canon beyond 2d and the two #1054 lines.
- Nothing on #1022, #1028–#1032 or #1036–#1040.
- Do not touch `.claude/worktrees/wf_144abcf5-325-1`: it holds staged, uncommitted edits on #1038's branch, queued for their own decision.
- No hygiene beyond this list, and no structural fixes.

## Binding disciplines

- **Skill plan:**
  - `ave-worktree-paths` on the first call in every worktree;
  - `verify-before-cite` on every quote and pointer;
  - `ave-vocab-discipline` for the open-item wording;
  - `ave-assertion-gate` on 2a's recorded question, which states both sides and asserts neither.
- **Self-isolation:** never check out a branch in the main checkout (`/Users/grantlindblom/AVE-staging/AVE-Core`); other sessions use it.
- **Pushes:** push from a named branch, never a detached HEAD. After every push compare `git ls-remote` with your local SHA.
- **Commits:** commit before you probe; one commit per step; never `--no-verify`.
- **STOP-AND-ASK.** Triggers:
  - a fork this brief does not resolve;
  - a corpus contradiction;
  - a question about what something physically is;
  - the same step failing twice.

  At a trigger, end your turn with a STUCK-POINT report:
  1. the blocker, exact, file:line;
  2. what was tried (≤2 attempts);
  3. the ONE physical question whose answer unblocks, phrased plumber-physical;
  4. candidate readings, one line each.

  A clean STUCK-POINT report is a successful turn.
- **Pure-AVE-corpus rule** on every tracked byte, commit message and PR comment.

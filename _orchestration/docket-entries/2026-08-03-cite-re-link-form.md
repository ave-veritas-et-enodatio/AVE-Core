### ENTRY 2026-08-03-cite-re-link-form (2026-08-03): implementer — teach `verify-anchor-content` the markdown-link anchor form; report the newly-visible drift, repair none of it

- **Class: tooling defect repair + triage report. NOT an adjudication.** No physics question opens or closes, no grade moves, no `clm-` / `def-` / `exp-` / `sup-` / `ilk-` is minted, no leaf is re-binned, no anchor is repaired. Executes the follow-on named verbatim in [`2026-08-02-paperclip-canonization.md`](2026-08-02-paperclip-canonization.md) — *"Named follow-on, NOT repaired here — `verify-anchor-content.py` is blind to link-form anchors … Named as a follow-on for a closeout-class lane."*

#### The defect

`manuscript/ave-kb/tools/verify-anchor-content.py` defined `CITE_RE` so the `:NN` had to follow the file extension **immediately**. The KB house-style anchor puts a closing paren in between, so the `)` broke the match and **the entire markdown-link anchor class was never scanned**. That is how three broken KB-leaf anchors shipped in the #832 arc under a *measured* anchor-content advisory delta of `0` — the tool never looked at them; the breakage was caught only by adversarial audit.

#### The fix — a lookbehind branch, not a bare `\)?`

Both candidate forms were **measured on the corpus before choosing**, and they are empirically identical here: `\)?` and an `](…)`-anchored branch each add exactly **857** cites, and a scan for *closing-paren-but-no-`](`-opener* returns **0** sites. The lookbehind branch was taken anyway because it is structurally exact — it cannot swallow a future prose parenthetical like `(as noted in foo.md):12`. The `](` is **asserted, not consumed**, so `m.start()` still lands on the path (the column `associate_quote` ranks quote-proximity against) and the two branches stay comparable. A `cite_path(m)` helper reads the path from whichever branch matched — Python `re` forbids two groups of the same name in one pattern, so the alternative was a silent group rename at the call site.

The Scope docstring was also sharpened: it previously read *"optionally wrapped in backticks or a Markdown link"*, which is ambiguous between the in-parens form `[t](p.md:12)` the tool **did** see and the after-parens form `[t](p.md):12` it **did not**. Both are now named explicitly.

#### Measurement — both runs at ONE tree, same arguments

`origin/main` @ `2fcde4db`, throwaway worktree, `--top 5000` (the #832 receipt argument set); only the tool file differs between runs.

| | cites scanned | checked | findings |
|---|---|---|---|
| BEFORE | `13249` | `1376` | **`1012`** |
| AFTER | `14106` | `1652` | **`1220`** |

**`+208` findings. Finding-set diff: `208` new, `0` removed** — purely additive. Re-scanning with branch attribution returns **`208` link-branch findings**, exactly equalling the report delta: every new finding is link-form, no bare-form finding changed. Per-bucket deltas sum to exactly `+857` (the independently-measured link-form cite count), including a real `-2` on `unresolved` — `associate_quote` skips adjacent lines carrying their own cite, and link-form cites now count for that test, so two bare cites lost a mis-associated quote. Full verbatim runs + the complete `208`-row list: [`_orchestration/2026-08-03_link-form-anchor-drift-triage.md`](../2026-08-03_link-form-anchor-drift-triage.md).

> ⚑ **Baseline-number reconciliation, surfaced not smoothed.** The #832 receipts record the pre-change baseline at **`1006`** / `1368` checked. At `2fcde4db` the same command returns **`1012`** / `1376`. The `+6` is corpus drift between the two tips, not a measurement disagreement — both are re-runnable. This lane's delta is computed `1012 → 1220` at a single tree, so the difference does not enter it.

#### What the 208 are — reported honestly, NOT headlined as 208 broken anchors

The new class carries the **same FP contamination as the pre-existing set** (the tool is WARN-CLASS for exactly that reason). By associated-excerpt class: `62` id-token (`clm-`/`def-`/… ids in backticks — pure noise), `56` short-token, `37` bare-path/identifier, **`53` genuine prose excerpts**. **Zero** cite an out-of-range line. A second, independent pass — extracting the `*"…"*` prose quote written immediately after each cite instead of the checker's nearest-backtick heuristic — returns `65` findings, **`13` of them KB-leaf→KB-leaf `moved`**: the high-confidence set.

**Seven rows hand-verified** (cited line printed AND target grepped for the excerpt), the sharpest being `photon-ee-mapping.md:79` → `translation-circuit.md:178` — a line literally labelled `**Anchors (verbatim, ✓-VERIFIED):**` whose excerpt is at `:190`, with its companion `:238` fragment actually at `:255`. Also: `electron-identification.md:92` → `:637` (the `"$g = 2$ is POSITED, not derived"` caveat, actually at `:767`); `photon-ee-mapping.md:96` → `:235` (**a blank line**; the R·r=1/4 Class-B adjudication text is at `:252`); `photon-ee-mapping.md:88` → `:237` (blank; text at `:254`); `photon-ee-mapping.md:105` → `:207` (row at `:224`); `dual-reactance-storage-taxonomy.md:221` **and** `trampoline-framework.md:681` → `master-equation.md:20` (`"TWO DISTINCT CLOCKS"` at `:38`); `cvr-transfer-function.md:41` → `theorem-3-1-q-factor.md:81` (text at `:85`).

**Mechanism, not coincidence:** four of the seven point into `common/translation-tables/translation-circuit.md` and are stale by a uniform **`+17`**. One high-churn hub leaf absorbed insertions and every inbound link-form anchor went stale together — invisibly, because the class was unscanned.

**One candidate was caught and DISCARDED rather than banked:** `double-slit-ee-mapping.md:60` cites `:40` and `:55` on one line; the second method attached the `:55` quote to the `:40` cite. `:55` is **correct**. Recorded in the triage doc as a demonstration that a multi-cite line defeats *any* nearest-quote heuristic — method-1 and method-2 alike.

#### NOT repaired — deliberately (flag-don't-fix)

**Not one of the 208 anchors is touched by this branch.** Repair is per-owner triage on the owning lane; a tooling branch that also rewrote 208 anchors across five volumes would be unreviewable, and the *right* repair (re-point `:NN` vs. convert to anchor-slug links vs. retire line anchors into `path-stable` frontmatter for high-churn hub leaves) is an owner/Grant decision, not a tooling-lane one.

> ⚑ **FLAGGED, not fixed — the checker scans its own test fixtures.** `verify-anchor-content.SKIP_DIRS` does not prune `tests/fixtures`, unlike sibling `verify-md-links` (explicit `("tests", "fixtures")` skip pair). Harmless today (`0` findings from there) but a latent trap: an on-disk stale-anchor fixture would count as corpus drift forever. This branch **sidesteps rather than fixes** it — the new regression test builds its tree in a tmpdir, as the tool's own `--self-test` already does. Changing `SKIP_DIRS` mid-audit would move the baseline this lane is measuring against.

#### Regression test — and proof it would have caught the bug

`manuscript/ave-kb/tools/tests/test_verify_anchor_content.py`, following the existing `tools/tests/` convention (importlib load of the hyphenated tool, as `test_verify_md_links.py` does). One tree carries a stale **bare**-form anchor, a stale **link**-form anchor, a correct anchor in each form, and a negative control (`(as noted in target.md):10`, no `](` opener) that must **not** be read as a cite at all — asserted via `cites == 4`, not `5`. **Verified against the pre-fix regex: `2` of `3` tests FAIL; after the fix, `3` of `3` pass.** A regression test that passes on the broken code is not a regression test.

#### Exit-code / battery-consumption check (read, not assumed)

The Makefile was read before asserting: `make verify` invokes the tool at line `130` with a **leading `-`** (make ignores its status) and **no `--top`**; the standalone `verify-anchor-content` target at line `188` invokes it bare. The tool returns `0` on every scan path before and after — `--self-test` remains the only nonzero path, and nothing in the battery invokes it. **WARN-CLASS contract unchanged**; a dedicated test asserts `main()` returns `0` on a tree containing drift.

#### Battery

`make verify` **exit `0`**; `make test-tools` PASS (`test_verify_anchor_content.py` `3` passed; full tools suite green); `python -c` compile check on the tool PASS; tool `--self-test` PASSED (unchanged expectations — the built-in fixture carries no link-form cite, so the pre-existing self-test is untouched by design); `verify-docket-keys` PASS (key `2026-08-03-cite-re-link-form` unique); `verify-md-links` gating `0`; `make verify-kb-metadata` PASS. **Anchor-content self-suppression verified**: the triage artifact's `208`-row list is inside a fenced block, which `strip_fenced` blanks before scanning, so the artifact does not inject its own contents into the count it reports — re-measured at this branch head. Pure-corpus. No `Frozen`-labelled text, no prereg, no result doc, and **no KB leaf** edited.

#### Discipline skills applied

`verify-before-cite` (every `file:line` in §4 of the triage doc re-grepped on this branch — one candidate discarded when the re-grep showed the anchor was correct) · `flag-don't-fix` (the `208` reported and routed, none repaired; the `tests/fixtures` scan-gap surfaced, not patched) · grep-completeness two-method discipline (the finding set measured by report-diff **and** by branch-attributed re-scan; the real-drift set by nearest-backtick **and** by adjacent-prose-quote extraction) · Rule 12 (nothing overwritten; the docstring change adds the missing form rather than replacing a claim) · `ave-evidence-framing-discipline` (`+208` reported as *newly-visible findings in a known-FP-contaminated warn class*, not as 208 broken anchors).

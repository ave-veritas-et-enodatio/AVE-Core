### ENTRY 2026-08-02-cite-rot-checker-gap (2026-08-02): infra — line-cites rot silently; the gating checker is path-only and the drift checker is advisory + structurally partial

- **Class: tooling gap, ROUTED for a decision. No physics, no corpus claim.** Surfaced by the KB-lockstep lane (#847 flag 5) and independently verified at source by the orchestrator. The manuscript-reconciliation epic has been paying for this by hand all session — every lane's "verify-before-cite two-method" pass is manual compensation for a check the toolchain does not perform.

**The gap, verified at source.**
- `manuscript/ave-kb/tools/verify-md-links.py:216-221` — `strip_target()` does exactly what its docstring says: `target = re.sub(r":\d+$", "", target)`. The **gating** link checker validates the PATH and, by construction, **never the line number**. A cite that says `foo.md:42` passes gating whether the content is at `:42`, at `:900`, or gone.
- There IS a dedicated drift checker — `manuscript/ave-kb/tools/verify-anchor-content.py`, wired into `make verify` at `Makefile:129` — but it is **WARN-CLASS, NON-GATING** (leading `-`, output labelled advisory), and its coverage model is *structurally partial*: it can only check a cite that happens to carry a **nearby backtick excerpt**, which it then searches for within ±10 lines of the cited line.

**Measured exposure (run at `origin/main`, 2026-08-02).** From the advisory checker's own summary:

| quantity | count |
|---|---|
| cites scanned (corpus-wide) | **13,249** |
| checked cites (carry a usable excerpt) | **1,376** (10.4%) |
| not-checked — **no quote at all** | **6,349** |
| not-checked — trivial quote | 176 |
| checked & anchored OK | 364 |
| **drift among checked** | **1,012 (73.5%)** |
| high-confidence "moved" candidates surfaced | 25 |

Two independent readings of the same table: (i) roughly **half of all cites carry no excerpt and are therefore uncheckable by any tool we have**; (ii) among cites the tool *can* check, **73.5% are already drifted** — and none of that gates a commit. (The checker's header documents its own FP classes — range cites `:NN-MM`, cross-row table associations, TeX/ASCII paraphrase — with a spot-check base rate of ~1-in-5 real, so the 1,012 is a candidate pool, not 1,012 confirmed breaks. The 25 "moved" rows are the high-confidence subset.)

**AMENDMENT 2026-08-02 (#847 audit, independently reproduced by the orchestrator) — the hole is WIDER than the entry above states, in two ways.**

**(i) The dominant KB cite form is invisible to the gating checker ENTIRELY — neither line nor path is validated.** `verify-md-links.py` blanks inline code spans before parsing (`strip_code()`), and its link regex only matches `[text](target)`. So:

| cite form | count in `manuscript/ave-kb/*.md` | path checked? | line checked? |
|---|---|---|---|
| `` `path.md:NN` `` (backticked bare) | **1,802** | **NO** | **NO** |
| `[`x.md`](x.md):NN` (label-external — the KB house convention) | **729** | yes | **NO** |
| `](path.md:NN)` (in-target) | 1 | yes | **NO** |

(Orchestrator's independent counts; the #847 auditor measured 1,283 / 708 / 1 with a narrower pattern set. Both agree on the shape: the backticked-bare form is the most common, and it is wholly unchecked — a cite can name a file that **does not exist** and gating stays green.)

**(ii) Proven by mutation, not inference.** The auditor rewrote a live cite to `device-circuit-models.md):999991-999992,999993-999994` plus `` `vocabulary-register.md:999999` `` and re-ran the checker: **exit 0, `gating errors: 0`, and the finding list byte-identical to the unmutated run.** An absurd line number and a bogus backticked path produce zero new findings.

This upgrades option (2) below from "nice hardening" to "closes a class of silent corpus breakage": asserting the line EXISTS is zero-FP, and extending the parser to see backticked-bare cites would put ~1,800 currently-invisible pointers under the path check for the first time.

**Why it matters here.** Line-cites are the corpus's load-bearing provenance form: every claim card, every KB leaf pointer, every `\kbleaf{...:NN}` in print. This session alone produced repeated real instances — `pending-rulings:26→:113` (stale in PRINT), `theorem-thesaurus:223→:227` (asserted HEAD-verified while stale), `vocabulary-register:536→:534` (inherited into two lanes from the board), `srs-band-structure:81→:116`, `q-g19a:121→:123` / `:110→:112`, three in-KB cites to a `q-g19a:108` that is a BLANK LINE at HEAD. Every one was caught by a human-directed grep, never by a gate.

**A second, cheaper failure mode found while measuring this (recorded, not fixed).** The workspace's own documented zsh false-negative bit again during this very verification: `grep -rn ... --include=*.md` (unquoted) returns **zero matches** under this shell, silently. Quoted (`--include='*.md'`) it returns 1,910. Any "0 hits / complete / all-sites" claim made with an unquoted `--include` or a `**` pathspec is worthless in this repo. `git grep -- 'manuscript/ave-kb/**'` likewise returns zero (#847 flag 5, independently reproduced).

**ROUTED — decision needed, options as walked (NOT adjudicated here):**
1. **Promote the excerpt-anchored check to gating** for the ~1,376 checkable cites, after an FP-triage pass on the documented FP classes. Cheap, but leaves the ~6,349 no-excerpt cites untouched and would gate red on day one against a 1,012-candidate backlog.
2. **Extend `verify-md-links` to resolve `:NN`** — make the gating checker assert the target file simply *has* that many lines (a weak but zero-FP check that catches the blank-line / deleted-tail class, e.g. the `q-g19a:108` instances), leaving content-drift to the advisory tool.
3. **Convention change**: require a backtick excerpt beside every NEW load-bearing line-cite, making cites self-verifying going forward without touching the 13k backlog. Pairs naturally with (1) or (2).
4. **Accept and document**: keep manual two-method verify-before-cite as the only guard, and stop implying the toolchain covers it.

Orchestrator's walked lean, for what it is worth: **(2) + (3)** — (2) is zero-FP and closes the hard-fail class immediately; (3) stops the backlog growing. (1) is the right eventual state but wants its FP-triage first. **Not executed — this fragment routes the decision, it does not take it.**

- **Receipts:** `manuscript/ave-kb/tools/verify-md-links.py:216-221` (strip_target, verbatim); `Makefile:102` (gating set — `verify-md-links` present, `verify-anchor-content` absent); `Makefile:128-130` (advisory block, leading `-`); `manuscript/ave-kb/tools/verify-anchor-content.py` header (coverage model + FP classes, verbatim); checker summary counts as tabulated above, reproducible via `python3 manuscript/ave-kb/tools/verify-anchor-content.py`.

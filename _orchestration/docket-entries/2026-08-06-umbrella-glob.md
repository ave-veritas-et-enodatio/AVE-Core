### ENTRY 2026-08-06-umbrella-glob

# Core-infra — umbrella-glob lane-checker discovery (kills the Makefile shared-line conflict class)

**Lane:** core-infra. **Class:** INFRA edit — mints no `clm-`/`def-`, touches no KB solidity, changes
no gate tolerance, computes no physics. Engine `src/ave` byte-untouched and never imported. **No
checker script was modified**: the diff is `Makefile` plus this fragment, nothing else.
**Base:** `origin/main` = `d129e7ac`.

---

## 1. The conflict class, and why it was worth a lane

Every research lane that shipped a number-check added four things to `Makefile`: its name to the
`.PHONY` line, its name to the `verify:` prerequisite line, an echo to the `help` recipe, and its
own target block. The first three are **shared lines**. Two concurrently open lanes therefore
conflict on those lines at merge, every time — and GitHub's server-side merge ignores the `union`
driver in `.gitattributes`, so the union resolution the lanes kept prescribing had to be done by
hand. **Ten receipts** across recent lanes, five of which **disclosed the class at freeze** rather
than discovering it at merge, with the fix already written down as a standing proposal each lane
declined to adopt unilaterally.

This is the same mechanism, on a different file, that the docket news-fragments convention was
adopted for; the README in this directory says in as many words that the convention "retires the
docket instance of the union-append conflict class, not the whole class." This lane retires the
`Makefile` instance.

## 2. What shipped

`verify-lane-number-checks` is now an auto-discovery umbrella over
`research/drivers/*_number_check.py`. It runs every discovered checker plain, then runs each one
again with `--mutation-receipt`, fail-fast, naming the failing checker and its mode and its exit
code. Discovery is measured at RUN time by the shell rather than at parse time by `$(wildcard)`, and
an empty discovery set is a **hard error**, not a silent pass — a glob that matches nothing is
exactly how this class of gate rots into a no-op.

**The receipt pass is conditional, and this is the one subtle point in the change.** Every checker
in the repo parses that flag by `"--mutation-receipt" in sys.argv` — not one uses `argparse` — so a
checker that does *not* implement a receipt silently ignores the flag and **re-runs the plain
check**. Unconditional receipts would therefore have manufactured nine double-runs wearing a gate's
clothes. The umbrella source-greps each checker for the literal flag and only then runs the receipt.
Measured over all 17 files: the grep set is **byte-identical** to the set of 8 lanes that had
hand-wired a receipt line — 0 false positives, 0 false negatives.

## 3. Reference census, and the alias decision

Two engines, both run 2026-08-06 on the full working tree: `git grep -F` (tracked files) and
`grep -rF` (working tree, untracked included). **They agree exactly**, file-for-file, on all
thirteen names.

> **CORRECTED 2026-08-06 (review finding A2).** The first version of this section said **24
> references** with a breakdown of 4/5/4/5/6. That number was **wrong, and wrong in a specific,
> instructive way**: the census script counted **files** (`git grep -c … | wc -l`) while the prose
> claimed **references**. Several files carry more than one citing line, so the file count
> under-reported the reference count. The auditor's independent re-measure found **28 distinct
> lines**; re-taken here with both engines, it reproduces **exactly, line for line**. The
> *decision* is unaffected — a larger reference surface strengthens the case for keeping the
> aliases — but a census that does not reproduce is not a census, so the corrected numbers are
> below and the superseded ones are named above rather than quietly overwritten.

**28 distinct citing lines** name the thirteen per-lane targets outside `Makefile`, in the
pre-existing corpus. They are not all the same kind of reference, and that is what settled the
decision:

| where | lines | can it be rewritten? |
|---|---|---|
| FROZEN prereg documents (approach-leak v2 ×4, echo-delay, echo-delay v2) | **6** | **No** — frozen text |
| frozen result documents (approach-leak v2 ×4, cold-Q v2.4) | **5** | **No** — frozen text |
| checker-script docstrings (`coldq_pole_v2p2` ×2, `approach_leak_v2` ×2, `coldq_pole_v2`) | **5** | **No** — a concurrent implementer holds one of these files; no checker was touched by this lane |
| KB canonical (`wall-taxonomy` ×3, `translation-circuit`, `claim-quality`) | **5** | possible, but they are user-facing "run this" instructions |
| docket entries (approach-leak-v2 ×3, +correction, srs-twist, coldq-axial-rhob, coldq-v2p4-root) | **7** | historical record |

**Count pin, per the measure-then-edit rule.** Re-measured **after** the repairs in §4a were
written, not before: whole-tree **29** distinct lines, of which **1** is in this fragment itself
(the help-drift sentence in §3), leaving the pre-existing corpus at **28**. Both engines agree at
that measurement. The §4a additions quote *script stems* and `LANE_CHECK_FILTER` values rather than
`verify-*-number-check` target names, so they did not move the count — which is why the figure is
the same as at the first commit (`85f2ea1a`) and is stated here as measured rather than predicted.
Anyone re-running the census should subtract this fragment's own line before comparing to the 28.

**DECISION: keep all thirteen names, as thin one-line aliases.** Removing them would break `make`
invocations printed inside documents that are frozen against rewriting, and would require editing a
checker script this lane is not permitted to touch. Each alias is one delegation line —
`$(MAKE) verify-lane-number-checks LANE_CHECK_FILTER=<script-stem>` — so an alias and the umbrella
can never drift apart in *how* a checker is invoked, and a renamed checker makes its alias fail
loudly (`*** FILTER ERROR: no such checker`) instead of silently gating nothing.

**The shared lines stop growing regardless**, which is the actual point. The thirteen names moved
off `.PHONY` into a `LEGACY_LANE_CHECK_ALIASES` variable marked **FROZEN — APPEND NOTHING**; the
`verify:` prerequisite line lost all thirteen and now carries `verify-lane-number-checks` alone;
the eleven per-lane `help` echoes collapsed to one umbrella line plus one line that prints the
frozen alias list from that same variable. All three lines are now **structurally final**: a new
lane adds nothing to any of them.

**Incidental finding, repaired by construction:** the per-lane `help` block had already drifted —
`verify-two-band-kp-number-check` and `verify-last-bond-number-check` were **missing** from it, so
`make help` had been under-reporting the gate surface. The replacement line renders the alias list
from the variable, so that drift mode is gone rather than fixed once.

## 4. Receipts

**Checker-count invariant, BEFORE vs AFTER on the same tree, two independent methods.**

*Method 1 — log-text extraction* (regex over `make verify` stdout, normalising the pre-conversion
recipe echo and the post-conversion `[lane-checks]` echo to the same `(checker, mode)` pairs):

```
BEFORE  distinct checkers=17  plain runs=17  mutation receipts=8  TOTAL invocations=25
BEFORE  double-run entries (count>1): NONE
AFTER   distinct checkers=17  plain runs=17  mutation receipts=8  TOTAL invocations=25
AFTER   double-run entries (count>1): NONE
INVARIANT: PASS -- execution multisets are IDENTICAL (same checkers, same modes, same multiplicities).
```

*Method 2 — process-level accounting*, which trusts no log text at all: `make verify PYTHON=<wrapper>`
where the wrapper appends its argv to a file and then `exec`s the real interpreter. Both runs exit 0.

```
BEFORE distinct=17 total=25
AFTER  distinct=17 total=25
=== diff of sorted process-level invocation multisets ===
IDENTICAL (diff empty, exit 0)
```

Nothing dropped, nothing double-run, and the eight receipts are the same eight.

**Perturbed-tree receipt A — a new lane needs ZERO Makefile edits.** A trivial
`research/drivers/zz_dummy_number_check.py` (exit 0, `--mutation-receipt` accepted as a no-op,
named `zz_` so it sorts last and the umbrella must reach the end of the glob) was dropped in with
**no Makefile change whatsoever** — `git diff -- Makefile | grep -c zz_dummy` returns `0`:

```
[lane-checks] auto-discovered 18 checker(s) via research/drivers/*_number_check.py
[lane-checks] RUN      research/drivers/zz_dummy_number_check.py
ZZ-DUMMY: hello from the perturbed tree (mode=plain, exiting 0)
[lane-checks] RECEIPT  research/drivers/zz_dummy_number_check.py --mutation-receipt
ZZ-DUMMY: hello from the perturbed tree (mode=mutation-receipt, exiting 0)
[lane-checks] OK -- 18 plain run(s), 9 mutation receipt(s), 9 checker(s) with no receipt support
```

**Perturbed-tree receipt B — failure propagates.** Same file, perturbed to `sys.exit(1)`:

```
[lane-checks] RUN      research/drivers/zz_dummy_number_check.py
ZZ-DUMMY: hello from the perturbed tree (mode=plain, exiting 1)
[lane-checks] *** FAILED (plain run): research/drivers/zz_dummy_number_check.py  [exit 1]
make: *** [verify-lane-number-checks] Error 1
make-verify-exit=2
```

That last block is from **`make verify`**, not from the umbrella target alone: a broken
newly-discovered checker turns the whole gate red. The dummy was **removed before staging**;
`git status` shows `M Makefile` and the new fragment only, and the glob is back to 17.

**Acceptance:** `make verify` exit 0 and `make test` green on the converted tree.

## 4a. Tier-2 review repairs (2026-08-06) — two real escape hatches, both closed

The Tier-2 review returned **NOT CONFIRMED: 1 blocking, 4 advisory**. The core design held (the
collision attack was refuted on exact paths; receipt detection independently verified 8/8 by
reading each checker's argv handling; the count invariant reproduced 17/25 on both sides via an
independent `execve` recorder; both failure modes propagate; Rule 12 clean; the help-drift
incidental confirmed true). Two findings were real defects in the umbrella recipe. Both are fixed
on this branch, and **each control was forced false first** — the escape was reproduced before the
fix, so the fix is demonstrably load-bearing rather than decorative.

### B1 (BLOCKING) — `LANE_CHECK_FILTER` could escape the discovery glob

The filtered branch **built** a path (`$(LANE_CHECK_DIR)/$(LANE_CHECK_FILTER).py`) and gated it on
`[ -f ]` alone. Any `.py` in `research/drivers/` was therefore reachable — including the **bare lane
drivers**, 14 of which are same-prefix siblings of a checker (`approach_leak.py` beside
`approach_leak_number_check.py`), and 31 non-checker files in total. This is not a cosmetic scoping
bug: **drivers write their results JSON**, so the auditor's `LANE_CHECK_FILTER=approach_leak` ran the
bare driver, printed `gates_failed=['G-NC-SLAST']`, still reported `[lane-checks] OK` with **exit 0**,
and **mutated a gated baseline** (`approach_leak_results.json`, `_runtime_sec` moved). A `verify-*`
target must never be able to write the thing it gates.

**Fix:** the filter now **selects from** the expanded discovery set by exact path equality instead
of constructing a path. Everything outside `research/drivers/*_number_check.py` is unreachable by
construction, not by a filename convention.

**Control, forced false on the pre-fix code.** A harmless probe was used rather than re-running the
destructive form — same escape mechanism (string concat + `[ -f ]`), no gated baseline touched:

```
[lane-checks] filtered to 1 checker (LANE_CHECK_FILTER=zz_probe_notachecker)
[lane-checks] RUN      research/drivers/zz_probe_notachecker.py
ZZ-PROBE: I AM NOT A CHECKER and I just got EXECUTED by a verify-* target (argv tail: none)
[lane-checks] OK -- 1 plain run(s), 0 mutation receipt(s), 1 checker(s) with no receipt support
make-exit=0
```

MISSED, green, exit 0 — the defect reproduces. **Post-fix, direction 1** (the real escape target):

```
[lane-checks] *** FILTER ERROR: LANE_CHECK_FILTER=approach_leak does not name a MEMBER of the discovery set.
[lane-checks]     The filter SELECTS FROM research/drivers/*_number_check.py by exact path equality.
[lane-checks]     It can never reach a path outside that set -- in particular it can
[lane-checks]     never execute a bare driver, which may WRITE a gated JSON baseline.
make: *** [verify-lane-number-checks] Error 2
make-exit=2
```

`git status` **byte-identical before and after** that run — no `approach_leak_results.json` write.
**Post-fix, direction 2** (the legitimate name still works, and runs exactly one checker):

```
[lane-checks] filtered to 1 checker (LANE_CHECK_FILTER=approach_leak_number_check)
[lane-checks] RUN      research/drivers/approach_leak_number_check.py
[lane-checks] RECEIPT  research/drivers/approach_leak_number_check.py --mutation-receipt
[lane-checks] OK -- 1 plain run(s), 1 mutation receipt(s), 0 checker(s) with no receipt support
make-exit=0
```

The same probe that escaped pre-fix is now **CAUGHT** (`*** FILTER ERROR`, exit 2), and was removed
before staging.

### A1 (advisory, fixed) — the receipt detector conflated "no match" with "grep broke"

`if grep -qF …; then … else …` folds grep's exit **1** (no match) and exit **≥2** (grep itself
failed) into the same branch. A broken detector therefore narrows the receipt set **toward zero**
while every checker is reported `no-receipt` and the gate still reports OK — the exact failure shape
this umbrella was built to prevent, reintroduced one level up.

**Control, forced false on the pre-fix code** (PATH shim making `grep` exit 2, test-only), on a
checker that genuinely *has* a receipt:

```
[lane-checks] RUN      research/drivers/srs_twist_coefficient_number_check.py
grep: SIMULATED INTERNAL FAILURE
[lane-checks] no-receipt research/drivers/srs_twist_coefficient_number_check.py (source declares no --mutation-receipt handler; …)
[lane-checks] OK -- 1 plain run(s), 0 mutation receipt(s), 1 checker(s) with no receipt support
make-exit=0
```

A real receipt silently vanished and the gate stayed green. **Post-fix**, the detector branches on
grep's exit status explicitly — 0 → receipt, 1 → no-receipt, anything else → hard failure:

```
[lane-checks] *** RECEIPT-DETECTOR ERROR: grep exited 2 on research/drivers/srs_twist_coefficient_number_check.py.
[lane-checks]     grep exit 0 = match, 1 = no match, >=2 = grep ITSELF failed.
[lane-checks]     Refusing to report a green gate on an unknown receipt set.
make: *** [verify-lane-number-checks] Error 3
```

Sanity re-check that the fix did not collapse the two legitimate branches: unshimmed,
`coldq_pole_v2_number_check` still classifies as `no-receipt` and exits 0, while
`approach_leak_number_check` still classifies as `RECEIPT`. Both grep outcomes remain reachable.

### A3 (informational) — the receipt detector matches the literal flag anywhere in the file

Detection is a fixed-string search over the whole source, **prose and comments included**. A checker
that *documents* `--mutation-receipt` in its docstring without implementing it would be classified
as receipt-bearing and would then **double-run its plain check silently** — precisely the failure
mode the conditional detector exists to avoid, entering through the other door. **Tolerated today**:
verified 0 false positives across all 17 checkers, every one of which parses the flag in code.
**Tighten to a code-shaped pattern** (e.g. requiring `sys.argv`/`argv` on the matching line) if this
is ever tripped. Recorded so the next lane inherits the caveat rather than rediscovering it.

### PENDING-GRANT — the root condition behind B1

B1 was reachable at all because **`research/drivers/` mixes read-only checkers and
baseline-writing drivers under one naming family**, distinguished only by a filename suffix. The
fix makes the umbrella safe; it does not address the arrangement that made the umbrella unsafe.
**Question for Grant, routed and not resolved here:** should a `verify-*` target ever be able to
execute a bare driver at all — or should write-capable drivers be separated from read-only checkers
structurally (different directory, or a declared read-only contract the gate can check), so that
"a gate mutated its own baseline" is impossible rather than merely blocked at one call site?

## 5. Rule 12 preservation, and what this does NOT claim

No rationale was deleted. All thirteen per-lane comment blocks stay **in place, verbatim** — only
their recipe bodies became one-line delegations — and the three blocks that describe the umbrella
proposal as `PENDING` each gained a **dated `ADOPTED 2026-08-06` note** underneath rather than an
edit. Those blocks' diagnosis of the conflict class was correct and is the reason it is now retired.
Their stated reason for deferring — "adopting it unilaterally would change the gate surface of every
other open lane" — was **discharged by measurement, not waived**: the execution multiset is
identical on both sides.

This changes **no physics and no gate strength**. It is a wiring change with a measured-identical
execution multiset. It does not make any checker stronger, does not add receipts to the nine
checkers that have none (that would have been a double-run, not a gate), and takes no position on
whether those nine should grow one — that is each lane's call, and under auto-discovery a lane can
now make it by editing its own checker and nothing else.

**Verified, not assumed:** CI calls only `make verify`, `make test`, `make test-engine` and
`make verify-new-cite-excerpts` — checked directly in `.github/workflows/verify.yml`, not carried
from a brief. No CI job names a per-lane target, so no workflow edit is required or made.

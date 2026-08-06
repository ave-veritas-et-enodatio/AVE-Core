# Records — `G-RHO2` supersession pointer + `NC-BYTES` re-pin (LOCKSTEP, 2026-08-06)

**Lane:** records (core-side). **Class:** RECORDS edit — mints no `clm-`/`def-`, propagates to no KB
solidity, changes no gate tolerance, computes no new physics. Engine `src/ave` byte-untouched and
never imported.
**Ruling:** decision-batch **R4** (LOCKSTEP route), recorded in the 2026-08-06 rulings decision-batch
docket entry (**PR #905, pending merge**) — cited by record name, not by a path that must resolve at
HEAD.
**Base:** `origin/main` = `dcc11323`.

---

## 1. What moved, and why it is one commit

The frozen v1 kernel-collapse result document records `G-RHO2` as **FAIL** and TASK 2 as
`ROW-NOT-CERTIFIED`. The rerun **that document's own §1.3 named** — inject `k_0 = ε·ω·Z_1`, not
`ε·k_cold` — has since landed `ROW-CERTIFIED` (PR `#902`, **MERGED** 2026-08-06 at merge commit
`b06cbeb1`; verified with `gh pr view`, not carried from a brief). The corpus therefore held a FAIL
record with no forward pointer to the certified successor.

**Three things had to move together or not at all**, which is the R4 LOCKSTEP route:

1. the **dated supersession pointer** on the v1 record;
2. the **`NC-BYTES` byte-pin** that the v1 record's blob is nailed to — editing the record moves its
   blob, and `G-DET-V2` re-runs the driver on every `make verify`, so an un-re-pinned edit turns the
   gate red repo-wide the moment it lands;
3. a **dated surface-note** on the vacated wall-taxonomy PENDING-REFRESH note, whose two premises
   both flipped when #902 merged.

## 2. The record edit — additive, and the FAIL is not softened

`research/2026-08-05_last-bond-kernel-collapse_result.md` gains **three lines and loses none**: a
dated surface-note inside the headline blockquote beside the TASK-2 verdict, and a second one in
§1.3 beside the diagnosis that named the repair. Both say the same thing in the corpus's dated-note
style — **the record is FROZEN and the FAIL stands as the v1 run's true verdict**; the v1 instrument
at the v1 siting measured the plateau correctly, and a correctly-sited successor does not un-make
that measurement. The verdict row is byte-identical: it still reads
`| **G-RHO2** ✗ | 2 | fitted exponent of` … `| **FAIL** |`.

**No back-ticked token in either addition starts with a digit or a sign**, which is what the v1
numeral registry keys on (`last_bond_kernel_collapse_number_check.py`:131 fullmatches
`[-+]?[0-9][0-9._eE+\-]*`). Dates are written **un-back-ticked** for that reason. `#902`,
`b06cbeb1`, `ROW-CERTIFIED` and `G-RHO2` are safe back-ticked; bare `902` and a back-ticked date are
not, and neither appears.

## 3. `AMENDMENT-NCBYTES-2026-08-06-B` — the disclosed byte-move and the re-pin

`approach_leak_v2.py`'s `NC-BYTES` pins ten read-only predecessor artifacts and **live-hashes each
one** (`git hash-object` against the working tree), and
`approach_leak_v2_number_check.py` machine-gates `G-DET-V2` by re-running that driver and demanding
a byte-equal JSON apart from `_runtime_sec`. The v1 record is artifact ten. So the edit in §2 is a
**disclosed move of a gated artifact**, and the gate has to reconcile it.

**Re-pin kind: a PER-ARTIFACT BLOB PIN, not a commit pin.** Amendment A could re-pin to a commit
(`f3607be8`) because the move was authored upstream and had already landed. This move is authored
**here**, so the commit carrying it does not exist until this branch commits — a commit pin would
make the gate un-runnable pre-commit. One 40-hex blob object nails the move exactly, and any
**further** drift, by this lane or anyone, fails.

**Nothing dropped. Three conjuncts ADDED, and all three gate the re-pin itself:**

| conjunct | what it forbids |
|---|---|
| COMPUTED left-the-v1-pin set == DECLARED supersession set | an **undisclosed** edit to any of the other nine hiding inside this one |
| **ADDITIVE-ONLY** — the pinned text must survive as a line subsequence of the live text | the frozen record being **rewritten** under cover of a "note" |
| the record's **own verdict strings** must still be present byte-exactly | a note that quietly **re-grades** the FAIL — a blob pin says *which bytes*, never *which claim* |

Subsequence is decided in-process rather than with `git diff` on two blobs, because the live blob is
not in the object database until commit time and **a gate must not write objects as a side effect of
running**. Measured: `594` → `597` lines, additive-only **true**, `3` of `3` verdict probes present.

**The receipt is CHAINED, not re-based.** Re-running the single amendment-A receipt from the
pre-amendment blob to the current JSON would have silently re-scoped amendment A's shipped receipt
and left the v2 result doc's §9 table (`297` / `350` / `5` / `53` / `0` / `0`) stale in place — the
vacated-cite failure class. Instead receipt A is now frozen at **both** ends (pre-amendment blob →
the blob PR `#904` merged, `1ba0cfc1`) and reproduces those six numbers verbatim on every
`make verify`; receipt B runs from that blob to the JSON on disk: `350` → `417` leaves, CHANGED `3`,
ADDED `67` (**all inside `NC-BYTES`**), REMOVED `0`, **outside the permitted set: `0`**. The composed
pre-amendment-to-disk comparison is checked too, so nothing hides in the seam. Digest
`4da48b39074d9fbc` → `f336bc5fe6281368`.

Mutations `M7`–`M10` were added so each new conjunct is provably fireable: a physics leaf moved
under receipt B; the blob pin perturbed; a frozen-verdict probe made unsatisfiable; and the
supersession moved-set over-declared. All ten mutations are CAUGHT.

## 4. ⚑ DISCLOSURE — the rerun lane's "BYTE-UNTOUCHED" claim is now HISTORICALLY SCOPED

`research/2026-08-05_last-bond-g-rho2-rerun_result.md`:9 carries
`**Predecessor (merged, BYTE-UNTOUCHED by this lane — gated,` `NC-BYTES`\ `):**`. That claim was true
of that lane's own run and is **no longer true of the tree**: the records edit above moved one of the
four artifacts it names.

**This is disclosed rather than repaired, and the reason is that its gate does not re-derive it.**
`last_bond_g_rho2_rerun_number_check.py`:169 reads the **shipped** JSON only —
`if nc["NC-BYTES"]["n_modified"] != 0:` — and that module imports no `subprocess`, so it never
re-runs its driver. Shipped `n_modified` is `0` and stays `0`; `make verify` stays green.

**Measured, not assumed.** Calling `last_bond_g_rho2_rerun.build_nc_bytes()` against this branch tree
returns `n_modified` = `1`, `pass` = `False`, naming exactly
`research/2026-08-05_last-bond-kernel-collapse_result.md`. So: **the shipped record is green and
honest about its own run; a re-derivation at HEAD is red; and the two do not contradict each other
because they quote different runs.** That is precisely the corpus-state divergence the wall-taxonomy
note routed — *"the refresh must say which run each sentence is quoting"* — now instantiated a second
time, on the byte gate rather than on the certification wording.

**Not fixed here, and deliberately.** Re-pinning that lane's `NC-BYTES` would mean editing a merged
research lane's frozen instrument to accommodate a later records edit, which is the move the freeze
rule exists to prevent. **Routed:** if that driver is ever re-run, its pin must be amended the same
disclosed way this one was. → **core lane / Grant.**

## 5. Wall-taxonomy: premises vacated, routed item untouched

`manuscript/ave-kb/common/wall-taxonomy.md` gains a dated surface-note beside — **not inside** — the
PENDING-REFRESH note. Both of that note's premises flipped: `gh pr view 902` now returns
`state: MERGED`, and `git cat-file -e origin/main:research/2026-08-05_last-bond-g-rho2-rerun_result.md`
now succeeds. **The argument is DEAD rather than wrong**, so the body is preserved and the note is
not rewritten.

Two cite-drifts are re-derived at this commit rather than carried: `Makefile`:111 → `:115` (the
`verify:` prerequisite line) and `:250` → `:275` (the target definition), both re-measured here; and
the `:NN` anchors into the v1 record shift by the map **`:24` unmoved / `:25`–`:78` +1 / `:79`+ +3**,
because this commit lengthened that file additively by three lines. The paragraph's substance is
re-verified and still exact: `last_bond_kernel_collapse_number_check.py`:171 still reads
`G-RHO2 is recorded as PASS but the doc reports it as FAIL`, so the v1 gate still hard-asserts the
first run's FAIL and `make verify` is green with #902 landed.

**The routed item stays OPEN**: each refresh sentence must name which run it quotes. This lane does
not pre-write those sentences, and the surface-note declares itself **non-payload** on the same fence
the original note already set for its own occurrence counts.

## 6. Deviations from the dispatch brief, surfaced not silently absorbed

The brief named four files. **Two more were forced by the lockstep**, both discovered by reading the
checker rather than by assumption:

- **`research/drivers/approach_leak_v2_number_check.py`** — required. The checker's amendment receipt
  registers its own leaf counts, and the v2 result doc back-ticks them at §9. A single re-based
  receipt would have made the doc's `297` / `350` / `53` unregistered numerals and turned
  `make verify` **red**. Chaining the receipt is what keeps them registered **and true**.
- **`research/2026-08-06_approach-leak-v2_result.md`** — a dated surface-note only, no rewrite. The
  `_digest` necessarily moves when `NC-BYTES` leaves change, so §4's `G-DET-V2` digest reading and
  §9's *"the digest moved"* sentence became historically scoped. Leaving a superseded digest
  unmarked in a shipped result doc is the honesty-lag class, so it is marked at the section rather
  than corrected in place.

Everything else is as briefed: line 52 of the v1 record is byte-identical (now line 53, `md5`
unchanged), staging was by explicit filename, and the wall-taxonomy note body was not rewritten.

## 7. Receipts

- `make verify` — green on the branch tree.
- `make test` — green.
- `last_bond_kernel_collapse_number_check.py` + `--mutation-receipt` — both green (the v1 `G-RHO2`
  FAIL flag assertion still holds; the additive prose registers no new numerals).
- `approach_leak_number_check.py` (v1) + `--mutation-receipt` — green.
- `approach_leak_v2_number_check.py` + `--mutation-receipt` — green, `M1`–`M10` all CAUGHT,
  `G-DET-V2` re-run matched.
- `last_bond_g_rho2_rerun_number_check.py` + `--mutation-receipt` — green.
- Two-method absence receipts for the absence claims asserted above are recorded in the PR body.

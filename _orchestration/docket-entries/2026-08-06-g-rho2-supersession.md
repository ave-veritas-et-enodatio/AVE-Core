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

Mutations `M7`–`M11` were added so each new conjunct is provably fireable: a physics leaf moved
under receipt B; the blob pin perturbed; a frozen-verdict probe made unsatisfiable; the supersession
moved-set over-declared; and the **ADDITIVE-ONLY** conjunct violated by deleting a line from the
PINNED side. **All eleven mutations are CAUGHT.**

`M11` carries **two** controls, and they answer different objections — both are now **executed in
code**, not asserted here:

- a **NEGATIVE control** — `nc_bytes()` is called **before** perturbing and must return `pass` =
  `True` with `ADDITIVE-ONLY` = `True`. Without it, "CAUGHT" is consistent with a conjunct that was
  already false for some unrelated standing reason, i.e. a no-op that looks like a gate;
- an **ISOLATION control** — under perturbation the blob pin still matches and the verdict probes
  still pass, so `ADDITIVE-ONLY` is the **only** conjunct that flipped, and the catch is attributable
  to it alone.

**🔴 CORRECTED, 2026-08-06 (residual R2).** An earlier version of this fragment, and the commit
message of `c7f9426f`, claimed a *"negative control recorded (unperturbed `pass=True`)"* when the
code called `nc_bytes()` **only under perturbation** — what actually shipped was the isolation
control. The negative control has since been added in code, and both are named separately above.

**⚑ CORRECTED, 2026-08-06, at Tier-2 (finding B2).** As first written this paragraph said `M7`–`M10`
and claimed each new conjunct was provably fireable. **It was one short.** `ADDITIVE-ONLY` sat in
`nc_bytes()`'s `pass` conjunction with **no mutation of its own**, so the claim over-stated the
coverage it had. `M11` closes it, and is built to be **isolating**: it appends a line to the
**pinned** side only, so the blob pin still matches and the verdict probes are still present, and
`ADDITIVE-ONLY` is the only conjunct that can catch it. A mutation that trips three conjuncts at
once proves none of them. **The commit message of `0c13a367` still says `M7`–`M10` and cannot be
amended after push; this fragment is the correction of record.**

## 4. ⚑ DISCLOSURE — the rerun lane's `NC-BYTES` INSTRUMENT no longer re-derives; its SENTENCE is still true

**⚑ SHARPENED, 2026-08-06, at Tier-2 (finding A6). The first version of this section conflated a
sentence with an instrument, and the distinction is the whole content.**

`research/2026-08-05_last-bond-g-rho2-rerun_result.md`:9 carries
`**Predecessor (merged, BYTE-UNTOUCHED by this lane — gated,` `NC-BYTES`\ `):**`.

- **The SENTENCE is STILL TRUE, and always will be.** It is scoped *"by this lane"*. The rerun lane
  did not touch the v1 record; the **records lane** did, months of provenance later. Nothing that
  happens in this PR can falsify a claim about what the rerun lane wrote. **The earlier wording here
  — *"no longer true of the tree"* — was wrong about which proposition was at stake, and is
  withdrawn.**
- **What went historically scoped is the INSTRUMENT.** `NC-BYTES` as that lane implements it does not
  test *"did this lane write it"*; it tests *"is the predecessor byte-identical to its pin"*, which
  reads FAIL at **any** tree where the predecessor moved **for any reason, by any author**. So the
  gate no longer re-derives the sentence it was built to certify. **The gate under-specifies its own
  claim** — the same class as amendment A's finding upstream, and the reason amendment B carries a
  COMPUTED/DECLARED reconciliation instead of a bare byte-identity.

**This is disclosed rather than repaired, and the reason is that its gate does not re-derive it.**
`last_bond_g_rho2_rerun_number_check.py`:169 reads the **shipped** JSON only —
`if nc["NC-BYTES"]["n_modified"] != 0:` — and that module imports no `subprocess`, so it never
re-runs its driver. Shipped `n_modified` is `0` and stays `0`; `make verify` stays green.

**Measured, not assumed.** Calling `last_bond_g_rho2_rerun.build_nc_bytes()` against this branch tree
returns `n_modified` = `1`, `pass` = `False`, naming exactly
`research/2026-08-05_last-bond-kernel-collapse_result.md`. So: **the shipped record is green and
honest about its own run; a re-derivation at HEAD is red; and the two do not contradict each other —
because the red is the instrument's under-specification firing, not the sentence turning false.** That is precisely the corpus-state divergence the wall-taxonomy
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

- **`research/drivers/approach_leak_v2_number_check.py`** — required, but **NOT for the reason this
  fragment first gave.**

  **🔴 RETRACTED, 2026-08-06, at Tier-2 (finding B1).** The original clause read: *"A single re-based
  receipt would have made the doc's `297` / `350` / `53` unregistered numerals and turned
  `make verify` **red**."* **That is measurably false and is withdrawn.** Measured: the BASE
  (`dcc11323`) number check, run verbatim against this branch tree, returns **rc = `0`** with its
  mutation receipt green. **Root cause, and it is a pre-existing corpus defect, not a fact about this
  lane:** raw line `471` of the v2 result doc carries an **odd** back-tick count (`7`) — it is the
  line that *describes* back-tick pairing, using a doubled span — and after `strip_fences` it is the
  **only** odd-parity line in the document, so global pairing flips there and **everything below it
  is never scanned**. Verified directly: `297`, `350`, `417`, `67` and `53` are all **absent** from
  the scanned token set. §9's numerals were never checked, so nothing about them could have turned
  anything red. Routed as **A3** below.

  **The true justification, which is stronger and survives the correction:**

  1. **Vacated-cite avoidance — a re-based receipt would make §9's shipped table a FALSE
     STATEMENT.** §9 states pre `297`, post `350`, CHANGED `5`, ADDED `53`. Measured, a re-based
     single receipt now computes pre `297`, post **`417`**, CHANGED **`6`**, ADDED **`120`** —
     contradicting the shipped table on **three of six cells**. Whether or not a scanner happens to
     look, a document that states `350` while its own instrument computes `417` is wrong. Chaining
     keeps §9 **true**; that it also keeps it registered is secondary, and — per A3 — currently moot.
  2. **Mutation coverage.** Without the new checker, amendment B's added conjuncts would ship with
     **zero** mutation coverage. `M7`–`M11` live in this file and are what make them gates rather
     than assertions.

  **The chaining decision is unchanged and is not softened by this retraction** — only its stated
  rationale is corrected.
- **`research/2026-08-06_approach-leak-v2_result.md`** — a dated surface-note only, no rewrite. The
  `_digest` necessarily moves when `NC-BYTES` leaves change, so §4's `G-DET-V2` digest reading and
  §9's *"the digest moved"* sentence became historically scoped. Leaving a superseded digest
  unmarked in a shipped result doc is the honesty-lag class, so it is marked at the section rather
  than corrected in place.

Everything else is as briefed: line 52 of the v1 record is byte-identical (now line 53, `md5`
unchanged), staging was by explicit filename, and the wall-taxonomy note body was not rewritten.

## 7. Routed, NOT repaired here

**A3 — the back-tick parity gap in `scan_doc` (→ approach-leak-v2 / infra lane).** Raw line `471` of
`research/2026-08-06_approach-leak-v2_result.md` carries an **odd** back-tick count (`7`): it is the
line that *describes* the pairing regex, and it uses a doubled span to quote it. After
`strip_fences` it is the **only** odd-parity line in the document, so `NUM_RE`'s global pairing
flips there and **every back-ticked token below it lands in an unscanned gap** — measured: `297`,
`350`, `417`, `67`, `53` are all absent from the scanned set.

**Pre-existing at base `dcc11323`, and widened by this lane** (two new numerals, `417` and `67`,
land in the gap). **Not fixed here**, because a real fix is not a one-liner: per-line pairing or
explicit double-back-tick handling changes which tokens reach the registry **for the whole
document**, which needs its own `ALLOWED_LITERAL` reconciliation and its own mutation receipt. That
is instrument work on the approach-leak-v2 lane's own checker, not a records edit. **This is the
same defect class the v2 lane already caught once and repaired with `strip_fences`** — the fence fix
restored balanced pairing for fences and left doubled inline spans unhandled.

### PENDING-GRANT — three framing questions surfaced by Tier-2, not answerable in-lane

1. **Registered-vs-scanned: what is the standard?** A3 makes the two come apart. A numeral can be
   *registered* (the instrument re-derives it every run) while never being *scanned* (no gate reads
   the document's rendering of it). Which one does "gated numeral" mean in the corpus? The answer
   changes how many result-doc numerals across the corpus are actually load-bearing.
2. **Is subsequence + verdict-probes the right strength for a frozen-record pin?** Amendment B
   proves *additive-only* and *these three strings survive*. It does **not** prove the added text is
   non-contradictory — a note could be additive, preserve every probe, and still mislead. Is that
   the intended ceiling for a mechanical gate, with the rest left to review?
3. **`V1_PIN_COMMIT` is a self-declared pin.** `NC-BYTES` compares against a commit named **in the
   file it is defending**. Nothing external certifies that `f3607be8` is the right pin; a lane could
   re-pin to any commit and the gate would still read green. Amendment B inherits this. Should pins
   be anchored to something the lane cannot choose?

## 8. Receipts

- `make verify` — green on the branch tree.
- `make test` — green.
- `last_bond_kernel_collapse_number_check.py` + `--mutation-receipt` — both green (the v1 `G-RHO2`
  FAIL flag assertion still holds; the additive prose registers no new numerals).
- `approach_leak_number_check.py` (v1) + `--mutation-receipt` — green.
- `approach_leak_v2_number_check.py` + `--mutation-receipt` — green, `M1`–`M11` all CAUGHT,
  `G-DET-V2` re-run matched.
- `last_bond_g_rho2_rerun_number_check.py` + `--mutation-receipt` — green.
- Two-method absence receipts for the absence claims asserted above are recorded in the PR body.

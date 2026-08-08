# Infra — R27 batch: excerpt-gate bare-quote form, parity immunisation, label nit (2026-08-07)

### ENTRY 2026-08-07-r27-infra-batch

**Lane:** infra (core-side background implementer, the #911/#912 pattern named by R27).
**Class:** INSTRUMENT repair. Mints no `clm-`/`def-`, propagates to no KB solidity, moves no
gate tolerance, computes no new physics. Engine `src/ave` byte-untouched and never imported. **No
result document, prereg or KB leaf is edited by this lane** — the eight documents the five repaired
checkers read are byte-untouched, which is why the repair needed no registry churn.

**Ruling:** **R27** — *"the next infra batch, queued: (a) the excerpt gate's bare-double-quote regex
(the #915 blocker's escape route); (b) the corpus immunization (five latent global-paired parity
checkers, pin-membership check per module first); … (d) the Makefile:448 B1/A1 comment-label nit"* —
`_orchestration/docket-entries/2026-08-07-rulings-r23-r27.md`. Item **(c)**, the bare-driver
root-condition split, is NOT in this batch: R27 conditions it on a Grant ruling still open.

**Base:** `origin/main` = `051887c4`.

---

## 1. Item (a) — the excerpt gate learns the third excerpt form

`manuscript/ave-kb/tools/verify-anchor-content.py` recognized excerpts in **two** written forms:
`` `backticks` `` and `*"emphasised quotes"*`. A **bare** `"…"` excerpt was invisible to **both**
consumers — the gating `--new-cites` ratchet counted the cite as excerpt-less and blocked it, and,
the part that matters, the advisory drift check never compared that excerpt against its target. A
misquote written in bare double quotes was **unreachable by any gate in the repo**. That is the
escape route around the #915 primer-misquote blocker. `BARE_QUOTE_RE` is now the third form.

### 1.1 Admitted as a LAST RESORT, and the ordering is a measurement not a preference

Bare double quotes are ubiquitous in ordinary prose, so admitting them as a *peer* of the house
styles lets a passing quoted phrase **displace** a deliberate excerpt a lane put beside its cite.
Three orderings were implemented and measured corpus-wide (15,659 cites, per-cite verdicts keyed on
citing-file/line/column/target/target-line and differenced against the shipped recognizer):

| ordering | newly-checked cites | previously-checked cites whose excerpt CHANGED | OK → not-OK flips |
|---|---|---|---|
| bare as a peer, nearest span wins | `+700` | `315` | `43` |
| bare as a same-line fallback | `+700` | `55` | `4` |
| **bare as a whole-pass last resort (SHIPPED)** | **`+700`** | **`0`** | **`0`** |

Coverage is **identical** in all three. The peer ordering therefore costs 43 displaced anchors and
buys nothing. `associate_quote` now runs the SAME search twice — house styles only, then, only if
that comes up empty, again with bare spans admitted — so every association that existed before is
returned unchanged **by construction**, not by luck.

### 1.2 Gate receipts — before / after, on the shipped file

Because the widening can only turn a `None` into a quote, the ratchet's blocked set can only
SHRINK. Measured rather than argued, on two back-test windows (`git diff BASE...HEAD` over the
canonical-authority surface):

| window | blocked before | blocked after | cites ADDED to the blocked set |
|---|---|---|---|
| `origin/main~120` (2026-07-28 →) | `169` | `127` | **`0`** |
| `origin/main~400` | `572` | `357` | **`0`** |

So `42` and `215` cites respectively carried a real excerpt the recognizer could not see, and **not
one cite anywhere flipped PASS → FAIL**. The subset check is a `comm -13` over the two sorted
violation listings, not an inference from the totals.

On the **current tree** (`CITE_BASE=origin/main`, this branch): `OK — every added load-bearing
line-cite carries an adjacent excerpt`, exit `0`, before and after.

Advisory pass, same tree, tool before → after: checked `2542` → **`3242`**; anchored-OK `700` →
**`841`**; not-checked-no-quote `6731` → **`4619`**; drift rate `72.5%` → **`74.1%`**. The drift rate
rises because the newly-visible excerpts carry the corpus's standing FP base rate, not because
anything regressed — `verify-anchor-content` is advisory and always exits `0`. The gain that
matters: **`700` cites that no checker could previously read are now drift-checked.**

### 1.3 ⚑ One existing test flipped PASS → FAIL, and it is the ruled change, not a defect

`test_emphasis_quote_recognizer_does_not_swallow_non_excerpts` carried an arm asserting that
`* "a bulleted quoted sentence"` is ordinary prose and must NOT anchor a cite. **It is now a
recognized bare span, so that arm fails.** There is no way to admit the bare form while excluding
the instances that happen to follow a bullet marker — they are the same span — and carving `* "` out
would re-open exactly the escape route R27 closes. The arm is **retired on purpose**; the test is
renamed `test_quote_recognizer_does_not_swallow_non_excerpts`, the fact that decided it is asserted
in its place (`EMPHASIS_QUOTE_RE` does NOT match it, `BARE_QUOTE_RE` does), and its two surviving
discriminators (a quoted path-cite is a cite not content; a quote under `MIN_QUOTE_LEN` stays
trivial) are re-pointed at fixtures that still fail under the widened recognizer. **This is the only
test in the repo that changed verdict.**

Two new tests: bare-quote excerpts (straight, curly, and on the line above) satisfy the ratchet; and
the last-resort ordering is asserted with its **forced-off arm executed** — the same line run
through `_associate(..., bare=True)`, i.e. the peer ordering, DOES select the nearer bare span, which
is what proves the two-pass structure rather than the fixture is doing the work.

## 2. Item (b) — corpus immunisation of the five latent parity checkers

### 2.1 Pin-membership FIRST, two independent methods, before a byte was edited

The #912 §3.1 lesson (a checker can be another lane's byte-pinned artifact, and it only shows up when
the drivers actually run) is the reason this ran first rather than after.

- **Method 1 — filename reachability.** `git grep` each checker's basename across the whole tree.
  Outside its own file, the five appear only in prose (result docs, dockets) and in two *docstrings*
  (`coldq_pole_v2p4_root_number_check.py:62`, `subc_kubc_bracket_number_check.py:9`), plus one
  Makefile alias (`Makefile:230`). No pin.
- **Method 2 — roster enumeration.** Enumerate every byte-pin roster in the repo and read its full
  membership rather than searching it. Three exist: `approach_leak.py`'s frozen set,
  `approach_leak_v2.py:165 READ_ONLY_ARTIFACTS` (10 artifacts, the `NC-BYTES` gate), and
  `last_bond_g_rho2_rerun.py:61 V1_ARTIFACTS`. Their union of pinned `.py` files is
  `approach_leak.py`, `approach_leak_number_check.py`, `approach_leak_v2*`,
  `last_bond_kernel_collapse.py`, `last_bond_kernel_collapse_number_check.py`. **None of the five.**
- Also checked: none of the five publishes a digest of its own source into any document.
  `continuum_radial_solver_number_check.py:374` reads its own source, but only for the structural
  `NON_REGISTRABLE` self-check, which splits on the `REGISTERED = {` / `ALLOWED = {` markers — both
  untouched here.

**Verdict: all five are EDITABLE.** Zero flagged-not-edited. (The two checkers that ARE pinned —
`approach_leak_number_check.py` — remain blocked by `NC-BYTES` exactly as #912 §3.1 routed them;
this lane does not touch them, and the routed follow-on stands.)

### 2.2 The defect list, re-derived rather than inherited

Re-derived on this tree by grepping every module's own token regex — **18** `*_number_check.py`
modules now, not the 17 the #912 audit saw (`iomega_law_number_check.py` landed since; it carries no
general back-tick numeral scan). The modules whose token class is ``[^`]+`` (no newline exclusion):
`approach_leak_number_check` and `approach_leak_v2_number_check` (the #912 lane's own — one blocked,
one already repaired), plus the five below. **The re-derived list is identical to the docket's.**

### 2.3 Token reconciliation — all counts RE-TAKEN AFTER the edits

Measured with each module's OWN shipped `scan_spans` against its OWN retained
`_scan_spans_legacy_global`, over exactly the text `main` assembles:

| module | docs | global spans | per-line spans | LOST | GAINED | odd-parity lines |
|---|---|---|---|---|---|---|
| `coldq_pole_derivation_number_check` | `1` | `474` / `267` | `474` / `267` | `0` | `0` | `0` |
| `coldq_pole_v2p2_root_number_check` | `1` | `536` / `296` | `536` / `296` | `0` | `0` | `0` |
| `continuum_radial_solver_number_check` | `1` | `781` / `462` | `781` / `462` | `0` | `0` | `0` |
| `pasteur_kappa_desk_calc_number_check` | `2` | `398` / `200` | `398` / `200` | `0` | `0` | `0` |
| `subc_kubc_bracket_number_check` | `3` | `1562` / `762` | `1562` / `762` | `0` | `0` | `0` |

**`+0` / `−0` across all five modules and all eight documents**, as the routing measurement
predicted. Stronger than a numeral-count match: the raw SPAN multisets are equal, so every
downstream stage is equal by construction. Independently confirmed end-to-end — **each checker's
full stdout is BYTE-IDENTICAL to its `origin/main` run** (captured from a detached worktree at
`051887c4`), so no self-reported count in any of the eight documents moves.

*(Counting-surface note, so this is not read as contradicting the routing docket: §6 of
`2026-08-06-backtick-parity.md` tabulated NUMERAL tokens — e.g. `184`/`105` for
`coldq_pole_derivation` — while the table above counts RAW BACK-TICK SPANS. Both are re-measured
here and they agree where they overlap: that checker still reports `numeric tokens: 105`.)*

### 2.4 Why a measured no-op ships anyway, and what makes it honest

A no-op repair is exactly the kind that rots into decoration. The two documents #912 measured as
FIRING prove the failure mode is real, and these eight are **time bombs**: the first odd-parity line
anyone adds silently unscans everything below it — in the two multi-document checkers, **across
document boundaries**, since `main` joins its `DOCS` before scanning. Per-line pairing fails SAFE: a
malformed line can only ever ADD spans on its own line.

**SCOPE, stated in each module and not a general theorem:** a CommonMark code span may straddle a
newline; such a span is read by global pairing and MISSED per-line. None of the eight documents
contains one — which is why `LOST` is `0` by MEASUREMENT. That bounded hole is the repo's standing
convention for this scan (the sibling checkers whose class is ``[^`\n]+`` have always had it), not a
regression introduced here. What the repair removes is the **unbounded** hole.

### 2.5 The mutation receipt, and the proof every arm is load-bearing

None of the five had a `--mutation-receipt` before; all five do now, so the umbrella's receipt
detector (`Makefile` `verify-lane-number-checks`) picks them up and `make verify` runs them. Measured
on the branch: `[lane-checks] OK -- 18 plain run(s), 13 mutation receipt(s), 5 checker(s) with no
receipt support` — receipts `8` → **`13`**, no-receipt `10` → **`5`**, discovery unchanged at `18`.

The plant is two lines appended **in memory only**: an odd-back-tick probe line, then an
unregistered back-ticked numeral below it — the exact position global pairing leaves unscanned. Five
arms, every one **executed against the shipped `main`**, none asserted: `anti-vacuity`,
`negative-control`, `scanner-level`, `CATCH`, `forced-off MISS`. The last is the counterfactual that
makes it a receipt for **the fix** rather than for the checker in general: the SAME planted text is
re-run through `main` with the retained pre-repair scanner injected, and must **MISS**.

`main` grew two private seams (`_text_override`, `_scanner`) with **no argv spelling**, so nothing a
caller can type reaches them; both default to the shipped behaviour.

**Executed forcing matrix — 5 modules × 5 forcings = 25 cells, every cell run, file restored and
re-hashed after each:**

| forcing | receipt verdict |
|---|---|
| `F1` the repair backed out (global pairing restored) | **FAIL** on all `5` |
| `F2` the planted numeral made allow-listed | **FAIL** on all `5` |
| `F3` the negative control broken (clean run made red) | **FAIL** on all `5` |
| `F4` one arm dropped from the results set | **FAIL** on all `5` |
| `F5` the forced-off arm defanged (repaired scanner injected) | **FAIL** on all `5` |

`25` of `25` forcings turn the receipt FAIL. `F1` is the row that matters: **back the repair out and
the mutation this batch adds goes MISSED.** `F4` fires because the arms are compared against an
ENUMERATED set (`PARITY_ARMS`), not counted — a dropped arm is a FAIL, never a quietly smaller
receipt.

## 3. Item (d) — the `Makefile:448` comment-label nit

Both labels confirmed at HEAD before editing, against the source docket
`_orchestration/docket-entries/2026-08-06-umbrella-glob.md`, whose section headers read verbatim
`### A1 (advisory, fixed) — the receipt detector conflated "no match" with "grep broke"` and
`### B1 (BLOCKING) — LANE_CHECK_FILTER could escape the discovery glob`. `Makefile:448` (the
three-way grep-outcome hardening of the receipt detector) said **B1** and is now **A1**;
`Makefile:460` (the filter escape) said **B1** and is correct, unchanged. Comment text only — no
recipe line, no variable, no target.

## 4. Receipts

- `make verify` — **green, exit `0`** on the branch tree (green at base `051887c4` beforehand as
  well, captured before any edit).
- `make test` — **green**.
- `make test-tools` — **`351` passed** (base: `349`; `+2` new tests, `1` renamed — §1.3).
- All five repaired checkers, plain run: exit `0`, **stdout byte-identical to `origin/main`**.
- All five, `--mutation-receipt`: **PASS, 5 arms each**; forcing matrix **25/25 FAIL** (§2.5).
- `verify-anchor-content.py --self-test`: **PASSED**.
- `make verify-new-cite-excerpts` on this branch: **OK**, exit `0`.
- Back-test windows `~120` / `~400`: blocked `169 → 127` and `572 → 357`, **`0` cites added to
  either blocked set**.
- **Nine files change**: the anchor tool + its test, the five checkers, the `Makefile` comment, and
  this fragment. No result doc, no prereg, no KB leaf, no JSON, no engine file.

## 5. What this does NOT do

- **Item (c) is untouched.** The bare-driver root-condition split (`research/drivers/` mixing
  read-only checkers with result-writing drivers — the `PENDING-GRANT` item behind B1) awaits
  Grant's ruling and is not pre-empted here.
- **The `approach_leak_number_check.py` per-line repair stays BLOCKED.** `NC-BYTES` pins it
  byte-exactly; #912 §6.1 routed it with its measured cost (`+47` distinct, `0` lost, `1` new
  `ALLOWED_LITERAL`, needs amendment C + a v2 JSON regeneration). Re-confirmed in-lane, not retried.
- **The advisory drift rate is not improved by this batch** — it rises `72.5% → 74.1%` because 700
  previously-unreadable excerpts joined the denominator. Driving the FP classes down is the standing
  separate promotion path for `verify-anchor-content`, untouched here.

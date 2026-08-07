# Infra — per-line back-tick pairing in the approach-leak v2 number check (2026-08-06)

### ENTRY 2026-08-06-backtick-parity

**Lane:** infra (core-side). **Class:** INSTRUMENT repair — mints no `clm-`/`def-`, propagates to no
KB solidity, moves no gate tolerance, computes no new physics. Engine `src/ave` byte-untouched and
never imported. The v1 result doc and the v1 checker are byte-identical to `origin/main`. The v2
result doc gains **one appended dated surface-note inside §9** and nothing else — no sentence above
it is rewritten, and the v2 `_digest` is unchanged (§4).

**Ruling:** **R11** — *"registered-vs-unscanned: SCAN-COVERAGE IS THE STANDARD"* — in the
2026-08-06 rulings final batch (`_orchestration/docket-entries/2026-08-06-rulings-final-batch.md`).
R11 makes registry membership alone bookkeeping and the parity gap a **BUG**, routed here with its
own `ALLOWED_LITERAL` reconciliation and mutation receipt. Grant: *"follow your rec."*

**Routed from:** `_orchestration/docket-entries/2026-08-06-g-rho2-supersession.md` §7, item **A3**.

**Base:** `origin/main` = `d129e7ac`.

---

## 1. The defect, re-measured in-lane

`scan_doc` paired back-ticks **globally** over `strip_fences(text)`. The token class `` `([^`]+)` ``
does not exclude newlines, so a single line with an **odd** back-tick count flips the open/close
phase for the **entire rest of the document**, and every numeral below it lands in a gap the scanner
never reads — silently, with the gate green.

Raw line **471** of `research/2026-08-06_approach-leak-v2_result.md` carries **7** back-ticks: it is
the line that *describes* the pairing regex and quotes it inside a doubled span. Re-measured here,
it is the **only** odd-parity line surviving `strip_fences`.

This is the same defect class the v2 lane already caught once and repaired with `strip_fences`. That
repair restored pairing for triple-back-tick **fences** and left inline **doubled spans** unhandled.

## 2. The fix, and why per-line rather than run-aware

Pairing in the v2 checker's `scan_doc` is now **per line**. A CommonMark back-tick-**RUN** parser was
implemented and measured as the alternative; it is **not** shipped. Two reasons:

- **Per-line fails SAFE.** A malformed line can now only *add* spans on its own line — a non-numeral
  span is dropped, a numeral goes RED and a human looks. It can never again silently *remove*
  coverage from everything below it, which is exactly the failure class R11 names. It also confines
  the **general** defect, not merely the doubled-span instance that exposed it.
- **Run-aware buys nothing here.** Re-measured after all edits, on both documents these checkers
  read, the run-aware token set is **identical** to the per-line set (`241`/`84` and `143`/`80`). It
  would add a hand-rolled parser that could itself under-scan — the very thing being repaired.

**A second scan site exists and is NOT repaired.** `main()` in the v1 checker keeps its own copy of
the scan loop alongside `_scan_doc`, so that lane has two defective sites, not one. Both are inside
the byte-pinned file of §3.1 and are routed with it.

## 3. Token reconciliation (all counts re-taken AFTER the edits)

| path | before (global) | after (per-line) | newly scanned | LOST | unregistered after | status |
|---|---|---|---|---|---|---|
| v2 result doc | `186` tok / `70` distinct | `241` tok / `84` distinct | `14` distinct | `0` | **none** | **FIXED** |
| v1-preserved content path | `55` tok / `33` distinct | `143` tok / `80` distinct | `47` distinct | `0` | `520` | **BLOCKED — §3.1** |

Nothing is LOST on either path: **on these two documents** the per-line set is a strict **superset**
of the global set. The v2 registry grows `88` → `94`. The v1 checker is **byte-unchanged** from
`origin/main`; its measured row above is the *counterfactual* the fix would produce.

**SCOPE — this is not a general theorem** (Tier-2 probe C). A CommonMark code span may straddle a
newline; such a span is read by global pairing and **missed** per-line, so a back-ticked numeral
written across a line break would be LOST. Neither document contains one — that is why `LOST` is `0`
by **measurement** and not by argument. The same bounded hole is shared by the nine sibling checkers
whose token class excludes newlines: it is the repo's standing convention for this scan, **not a
regression introduced here**. What the repair removes is the *unbounded* hole — one odd line
silently unscanning everything below it.

**The 14 newly-scanned v2 tokens.** `297` / `350` / `417` / `53` / `67` (the §9 amendment counts) and
`3` were already registry-resident; `11` / `32` / `520` / `59` / `60` / `73` were already in
`ALLOWED_LITERAL`. **Two were genuinely unregistered** and are the reason this was not a one-liner:

- **`120`** — §9's *re-based* counterfactual, *"a re-based receipt would compute `417` / `6` / `120`"*.
  Given a **derived** home: `amendment_registry` already computed the composed pre-amendment-to-disk
  delta but registered only its `other` count. The whole composed delta is now registered
  (`amend_chain_leaves_pre` `297`, `amend_chain_leaves_post` `417`, `amend_chain_changed` `6`,
  `amend_chain_added` `120`, `amend_chain_removed` `0`, `amend_chain_other` `0`), re-derived from the
  two git blobs on every run. Not allow-listed.
- **`471`** — the document's cite of **its own raw line number**. Registered **COMPUTED** by
  `doc_selfref_registry`, which re-derives the odd-parity line set from the document and FAILS unless
  exactly one exists. A self-cite that no gate re-derives is a declaration, not a receipt.

### 3.1 ⚑ The v1-preserved path fix is BLOCKED, and the blocker is the v2 lane's own gate

The same repair was written for `approach_leak_number_check.py` — per-line `_scan_doc`, `main()`
calling it instead of keeping a second copy of the loop, `520` added to `ALLOWED_LITERAL`, and a
fourth mutation with its own counterfactual arm. It ran **green in isolation** (`96` registered
values, `M1`–`M4` all CAUGHT, the v1 result doc byte-untouched). It was then **reverted**, because
`make verify` — not static reading — showed it breaks the v2 lane:

- `research/drivers/approach_leak_number_check.py` is **one of the ten read-only artifacts the v2
  driver's `NC-BYTES` gate pins byte-exactly** at `V1_PIN_COMMIT` = `f3607be8`. Measured with the
  edit in place: `byte_identical` = `False`, `NC-BYTES` `pass` = `False`.
- That moves the v2 digest: `f336bc5fe6281368` → `3499c1ef3c4c1494`, so `G-DET-V2` fails and
  `make verify` exits `2`.
- Landing it would require a **third disclosed amendment** (its own blob pin, declared moved-set,
  frozen-verdict probes and mutations), a **regeneration of `approach_leak_v2_results.json`**, and a
  **third link on the §9 receipt chain** — with the frozen v2 result doc's §9 table going stale in
  place, which is the vacated-cite failure class that chain exists to prevent.

`NC-BYTES` is doing exactly its job here: its purpose is *"this lane wrote none of the predecessors"*,
and this lane tried to write one. **Measured token delta of the blocked fix: `+47` distinct
(`33` → `80`), `0` lost, one token (`520`) needing an `ALLOWED_LITERAL` entry.** Routed, not forced.

**⚑ SELF-DECLARED, not reproducible from this tree.** The reverted patch is not in the repo, so two
claims above cannot be re-derived by a reviewer at this commit and are marked rather than dressed up
as receipts: **(a)** the moved digest `3499c1ef3c4c1494`, and **(b)** the "ran green in isolation"
run of the reverted patch. Everything else in this section IS reproducible now — that
`approach_leak_number_check.py` is a byte-pinned `NC-BYTES` artifact, and the `+47`/`0`-lost token
delta, are both measurable against the tree as it stands.

**⚑ Correction to the routed item's own measurement.** §7 of the g-rho2 docket records the gap as
`297` / `350` / `417` / `67` / `53` — five numerals. The full newly-scanned set measured here is
**14** distinct, of which **two** (`120`, `471`) were unregistered rather than merely unscanned. The
routed count was not wrong about the five it named; it was **incomplete**. Flagged rather than
silently absorbed.

## 4. What this makes stale — and the dated surface-note that records it

The v2 result doc's §9.1 note states that its `297` / `350` / `417` / `53` / `67` *"is never
scanned"*, and §9.3 routes the parity gap as *"not fixed in this lane"*. **Both are now false of the
shipped checker.** Per the standing vacated-cite rule — frozen text gets a dated surface-note, never
a rewrite — a **dated surface-note is appended inside §9**, below the line it is about. Nothing above
it is edited.

**⚑ CORRECTION to this fragment's first draft, which stated the wrong blocker.** That draft said the
result doc was *"frozen with downstream pins"* and could not be touched. **That is not true and was
not the reason.** The doc is **not** in the `NC-BYTES` read-only set — it is in `V2_OWN_ARTIFACTS`,
i.e. this lane's own, and the v1 scan surface that would otherwise notice it is commit-pinned at
`SCAN_PIN`. Verified after the edit: the v2 `_digest` is **unchanged** at `f336bc5fe6281368`. The
two real constraints are:

1. **The new self-cite gate.** `doc_selfref_registry` computes the odd-parity line and this page
   cites it as `471`. Any insertion **above** that line shifts it and turns the gate red. The note is
   therefore appended **below** raw line `471`, and every inserted line is **even**-parity so the
   odd-parity set stays exactly one element.
2. **The note-only convention.** Superseded sentences are left standing and answered below, not
   rewritten in place.

The `amendment_registry` docstring, which carried the same caveat **in code**, IS updated: a comment
that contradicts its own gate is the checklist-not-gate tell this file already corrected once at A4.

## 5. Receipts

- `make verify` — green on the branch tree (green at base `d129e7ac` beforehand as well).
- `make test` — green.
- `approach_leak_v2_number_check.py` — green, `94` registered values, `G-DET-V2` re-run matched.
- `approach_leak_v2_number_check.py --mutation-receipt` — **`M1`–`M13` all CAUGHT**.
- `approach_leak_number_check.py` (v1) + `--mutation-receipt` — green, `M1`–`M3` CAUGHT, **unchanged
  from base**: this PR reverts its repair (§3.1) and leaves the file byte-identical to `origin/main`.
- `NC-BYTES` `pass` = `True`, `10` artifacts, all `byte_identical` — re-confirmed after the revert.
- The v1 result doc and the v1 checker: `git diff` clean against `origin/main`.
- The v2 `_digest` is **unchanged** at `f336bc5fe6281368` with the §9 surface-note in place, and the
  self-cite gate still computes `471` — the doc edit moves no gate.
- **Three files change**: the v2 number-check, the v2 result doc's appended §9 surface-note, and this
  fragment.

### 5.1 The new mutations, and the proof they are load-bearing

`M12` plants an unregistered numeral on a new line immediately **below** the document's odd-back-tick
line — the exact position the pre-repair scanner left unscanned — in an **in-memory copy only**. It
carries **three executed controls**: an unperturbed **negative control** (the clean document must
scan clean), the catch itself, and a **counterfactual arm** that runs the *same planted text* through
the retained pre-repair scanner and requires a **MISS**. Without the third arm the mutation would
pass just as happily against the bug it exists to prove fixed.

`M13` plants a **second** odd-parity line and requires `doc_selfref_registry` to refuse, since §9
cites raw line `471` as the *only* one.

**⚑ `M13` WAS DECORATIVE IN THE FIRST DRAFT, and Tier-2 falsified it.** That draft **re-derived** the
"exactly one odd line" predicate at the mutation site instead of calling the gate. Weakening the real
criterion from `!= 1` to `< 1` left the draft **CAUGHT** — it was testing its own restatement, not
the function it named. `M13` now **calls `doc_selfref_registry`** on the planted text and requires
its verdict (empty registry + a failure surfaced), with the clean document as the executed negative
control. Failures go to a **local sink** so the receipt cannot pollute a real run. Acceptance receipt,
executed **both directions**:

| criterion in `doc_selfref_registry` | `M13` |
|---|---|
| shipped `len(odd) != 1` | **CAUGHT** |
| weakened to `len(odd) < 1` (forcing-E, scratch copy) | **MISSED** |
| restored | **CAUGHT** |

That is the difference between a mutation that receipts a gate and one that receipts a copy of it.

Every control was **forced false** and the receipt re-run; each forcing turns the mutation `MISSED`,
so none is decoration:

| forcing | result |
|---|---|
| `scan_doc` reverted to pre-repair global pairing | `M12` **MISSED** |
| planted numeral made registered | `M12` **MISSED** |
| negative control broken (clean doc scans dirty) | `M12` **MISSED** |
| `M13`'s planted line made even-parity | `M13` **MISSED** |

The first row is the one that matters: with the repair backed out, the mutation this PR adds goes
`MISSED`. That is what makes `M12` a receipt for the **fix** rather than for the scanner in general.

## 6. Sibling audit — `research/drivers/*_number_check.py`

**Two independent methods.** *Method 1 (static)*: grep every module's back-tick token regex and
classify by whether the character class excludes `\n`. A class that excludes newlines cannot span a
line break, so the newline is a hard barrier and pairing is already confined per line. *Method 2
(dynamic)*: import each module, run **its own** regex and **its own** `strip_fences` (where it has
one) over **its own** declared documents, and measure global-vs-per-line token counts plus the count
of odd-parity lines. Method 1 says whether the defect is *present*; method 2 says whether it *fires*.

| module | regex class | verdict | doc measure (global → per-line) | odd lines |
|---|---|---|---|---|
| `approach_leak_v2_number_check` | `` [^`]+ `` | **DEFECT, FIRING — FIXED HERE** | `186`/`70` → `241`/`84` | `1` |
| `approach_leak_number_check` | `` [^`]+ `` | **DEFECT, FIRING — BLOCKED, §3.1** | `55`/`33` → `143`/`80` | `20` |
| `coldq_pole_derivation_number_check` | `` [^`]+ `` | DEFECT, **latent** — FLAGGED | `184`/`105` → `184`/`105` | `0` |
| `coldq_pole_v2p2_root_number_check` | `` [^`]+ `` | DEFECT, **latent** — FLAGGED | `203`/`96` → `203`/`96` | `0` |
| `continuum_radial_solver_number_check` | `` [^`]+ `` | DEFECT, **latent** — FLAGGED | `195`/`108` → `195`/`108` | `0` |
| `pasteur_kappa_desk_calc_number_check` | `` [^`]+ `` | DEFECT, **latent** — FLAGGED | `167`/`99` and `81`/`62`, both → unchanged | `0`, `0` |
| `subc_kubc_bracket_number_check` | `` [^`]+ `` | DEFECT, **latent** — FLAGGED | `309`/`183`, `111`/`74`, `3`/`1`, all → unchanged | `0`, `0`, `0` |
| `coldq_axial_rhob_number_check` | `` [^`\n]+ `` | SAFE | `183`/`111` → unchanged | `2` |
| `coldq_polar_family_number_check` | `` [^`\n]+ `` | SAFE | `31`/`20` → unchanged | `0` |
| `coldq_pole_v2_number_check` | `` [^`\n]+ `` | SAFE | `211`/`110` → unchanged | `2` |
| `coldq_pole_v2p4_root_number_check` | `` [^`\n]+ `` | SAFE | `176`/`125` → unchanged | `3` |
| `echo_delay_regulated_sum_number_check` | `` [^`\n]+ `` | SAFE | `175`/`132` → unchanged | `4` |
| `echo_delay_v2_number_check` | `` [^`\n]+ `` | SAFE | `299`/`193` → unchanged | `8` |
| `last_bond_g_rho2_rerun_number_check` | `` [^`\n]+ `` | SAFE | `52`/`36` → unchanged | `4` |
| `last_bond_kernel_collapse_number_check` | `` [^`\n]+ `` | SAFE | `118`/`50` → unchanged | `8` |
| `two_band_kp_kinematics_number_check` | `` [^`\n]+ `` | SAFE | `59`/`36` → unchanged | `2` |
| `srs_twist_coefficient_number_check` | — | no back-tick numeral scan | n/a | n/a |

**7 of 17 modules carry the defect in code. 2 of those fire on their current documents. 1 is fixed
here; the other is blocked by §3.1.** The `SAFE` rows are safe *by construction*, not by luck:
several have odd-parity lines and are still unaffected, because the newline barrier confines pairing
to a line already. The cheap corpus-wide immunisation, for whoever picks up the routed items, is to
add `\n` to the token class — that is what the nine safe modules already do.

**⚑ CORRECTION, and the counting surface.** The `last_bond_kernel_collapse` cell read `4` in this
fragment's first draft; the measured value is **`8`** (raw lines `218`, `223`, `229`, `233`, `280`,
`282`, `288`, `293`) — a transcription error, the dynamic-audit output said `8` all along. Re-taken
after the edits, across the nine `SAFE` documents: **`33`** odd-parity lines total, of which **`30`
are ``` fence markers** and only **`3` are genuine inline** unbalanced back-ticks
(`coldq-pole-v2.4-root` line `348`; `two-band-kinematics` lines `249` and `250`). The odd-line column
is therefore mostly counting fences, which is exactly why it is a poor proxy for risk on its own and
why the global-vs-per-line token delta is the column that adjudicates. *(Tier-2 quoted `22` of `25`
for the same split; that total omits the `8` it was simultaneously correcting — `33 − 8 = 25`. The
`3` genuine-inline figure agrees exactly. Both numbers here are mine, re-measured.)*

**The 5 latent modules are FLAGGED and ROUTED, not fixed.** Measured delta is **`+0`/`-0` distinct
tokens on every one of their eight documents**, so the per-line repair would be a **no-op today** and
would need no doc edit and no registry churn. They are not fixed here on purpose: each would need its
own mutation with its own executed counterfactual to be worth anything, and — as §3.1 demonstrated at
cost — a checker file can be a **byte-pinned artifact of some other lane's gate**, which only shows up
when the drivers actually run. Routing them, with the measurement above, is the "do not force it"
call. **They remain time-bombs**: the first odd-parity line added to any of those eight documents
silently unscans everything below it.

### 6.1 Routed follow-ons

| item | measured cost | blocker |
|---|---|---|
| `approach_leak_number_check` per-line repair | `+47` distinct, `0` lost, `1` new `ALLOWED_LITERAL` | `NC-BYTES` byte-pin; needs amendment C + v2 JSON regen (§3.1) |
| 5 latent modules (8 docs) | `+0`/`-0` distinct | none measured; needs 5 mutation receipts + a per-module byte-pin check |

## 7. Standing question this does NOT answer

§7's `PENDING-GRANT` item 3 — *`V1_PIN_COMMIT` is a self-declared pin* — is untouched here. Scan
coverage and pin provenance are different gates; this lane closed the first.

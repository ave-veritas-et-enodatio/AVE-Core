# `G-RHO2` rerun v2 — the last-bond lane's TASK 2 certifies (2026-08-05)

**Dispatch:** certification rerun of the ONE failed gate of the merged last-bond lane, so that the
print-language question — *does `ROW-NOT-CERTIFIED` license a "mechanism confirmed" phrasing?* —
**moots** rather than being adjudicated on wording.
**Lane:** core mini-lane, RERUN class (versioned prereg supersede; derivation-only; no engine run,
no KB edit).
**Branch:** `research/last-bond-g-rho2-rerun` · **Base:** `origin/main` at `c4fdced0`.
**Prereg (frozen ALONE, pre-code):** `research/2026-08-05_last-bond-g-rho2-rerun_prereg-FROZEN.md`
at `503579b0`.
**Result:** `research/2026-08-05_last-bond-g-rho2-rerun_result.md`.
**Predecessor (merged, BYTE-UNTOUCHED — gated):**
`research/2026-08-05_last-bond-kernel-collapse_result.md` §1.3, which diagnosed the failure and
**named this exact repair**.

## Verdict

**TASK 2 of the last-bond lane is `ROW-CERTIFIED`.** `G-RHO2` PASSES at a fitted off-limit
sensitivity exponent of `1.99999999999966070743940658186`, inside the **unchanged** v1 acceptance
interval `[1.9, 2.1]`. Theorem 3(b) — the beyond-wall load enters the terminal row at **second**
order in the last-bond stiffness — is now measured rather than assumed.

**TASK 1 remains `SCAN-NOT-CERTIFIED` and was not touched. TASK 3 was not touched.
`BIN-C-DISJOINT` was not revisited.**

## What was wrong, and what changed

Theorem 3(b) is an **asymptotic** statement, and an asymptotic statement has a **domain**. The
domain is `k_0 ≪ ω|Z_beyond|`; the crossover, derived here from the shipped v1 parameters alone, is
`k_0 = ω·Z_1 = 0.00000524955352488372143529667589330` — equivalently the dimensionless probe
coordinate `δ ≡ k_0/(ωZ_1) = 1`. **v1's three injections sat at `δ` = `31622.7766016837933199889354443`,
`316.227766016837933199889354443` and `3.16227766016837933199889354443` — all ABOVE the crossover,
on the plateau where the exponent is genuinely `0`.** The instrument measured the plateau correctly;
the freeze pointed it at the wrong place.

**Exactly one thing changed:** the injection siting, `k_0 = ε·k_cold` → `k_0 = ε·ω·Z_1`, at
`ε ∈ {1e-6, 1e-8, 1e-10}`, i.e. `6`/`8`/`10` decades **below** the crossover. **No tolerance, bin
boundary, sweep grid or frozen numeric moved.** The repair is not this lane's invention — it is the
one the predecessor named verbatim and its Tier-2 verify independently confirmed.

## The number was predicted before it was measured

The prereg §3.2 derived the exact closed form
`|Δ|(δ) = 2δ²/[√(1+4δ²)·√(4+9δ²)]` and from it the expected exponent `2` with a predicted deviation
of `3.39333930000000000000000000000e-13`, written down before any v2 code existed. **Measured
deviation: `3.39292560593418140000000000000e-13`.** The plateau self-test was predicted the same way
and landed the same way. Nothing was fitted.

The same closed form reproduces the **v1 shipped failing exponent** to every digit — which is how
the diagnosis was independently confirmed before the repair was frozen.

## Certification receipts

| receipt | measured |
|---|---|
| `G-RHO2` (v2 siting, sub-crossover) | `1.99999999999966070743940658186` — **PASS**, interval unchanged |
| `FT-RHO2` (same code, plateau siting) | `3.76991733993251474861640528204e-14` — **FIRES** (outside the interval) |
| `D-RHO2-PRED` (DIAGNOSTIC, not a gate) | `3.39292560593418140000000000000e-13` — **AGREES** |
| `G-DET-V2` (double run) | digest `a69cf1c2e710a473` twice; diff empty apart from `_runtime_sec` |
| `NC-GATES+NC-FT` (exact string equality vs the v1 shipped renderings) | `20` blocks, `80` fields, **`0` mismatches** |
| `NC-RHO2-V1` (v1 siting through the v2 code path) | `0.00370115115631918737071374823881` + both per-pair values, **byte-exact** |
| `NC-ROWS` | `3360` = `3360` |
| `NC-BYTES` (predecessor artifacts vs `c4fdced0`) | `4` checked, **`0` modified** |

**`FT-RHO2` is why the PASS is a measurement and not a construction:** same code, same tolerance,
probe coordinate moved across `δ = 1`, opposite verdicts.

## Declared limits (not discovered — frozen in the prereg §5)

**`G-SCAN` and `FT-SCAN` are REPLAYED, NOT re-run and NOT reproduced.** The v1 corpus scan is
tree-state-dependent by the predecessor's own §1.3 — its outputs live inside the scanned tree, and
this lane adds three more files to it — so re-running it here could not reproduce the shipped numbers
and its failure to do so would carry no information. Those two entries are bookkeeping in the
reproduction-class ledger, not evidence. **TASK 1 is not certified by this lane and the ruling's
routed premise remains unadjudicated.**

**Scope of the certification, stated narrowly:** Theorem 3(a) (`G-RHO`, exact independence AT the
limit, PASS at exactly zero in v1) is the load-bearing one for any `ρ`-independence statement.
Certifying 3(b) adds no new licence beyond what 3(a) already carried; it removes an
open FAIL from the lane's gate table.

## ROUTED — the print-language consequence (RECORDED, NOT EXECUTED)

The question that motivated the rerun **moots on this certification**. It is recorded here for the
**propagation pass** and executed nowhere in this lane: **no KB leaf, manuscript file, solidity,
matrix row or falsification-ledger entry was edited, and the predecessor's result doc was not
rewritten and not annotated** — the v1 record stands as the v1 record (Rule 12,
substitution-not-retraction). Whoever runs the propagation pass inherits:

1. the last-bond lane's TASK-2 status line, wherever it is quoted, moves
   `ROW-NOT-CERTIFIED` → `ROW-CERTIFIED`, **for TASK 2 only**;
2. any downstream phrasing that leaned on the TASK-2 status — in either direction — is now
   re-checkable against a certified row;
3. **TASK 1's `SCAN-NOT-CERTIFIED` is unchanged and must not be swept along with it.**

## Routed follow-ons

- **FLAG-A (minor, predecessor prose, NOT fixed here):** the v1 result §1.3 describes the frozen
  injections as landing *"between roughly two parts in a hundred thousand and two parts in ten"*
  relative to the crossover. Re-derived here the ratios are `3.16e-5` and `0.316` — *three* parts,
  not two. The load-bearing claim (all three on the wrong side of the crossover) is confirmed; only
  the prose rounding is off. **Flagged, not fixed:** the v1 doc is frozen and this lane does not
  annotate it.
- **FLAG-B (SVA v0.2, routed to whoever lands the leaf):** a *rerun* lane wants a row-2 sub-prompt —
  *"if this lane re-measures a prior null, state the domain of validity of the statement being
  measured and where the prior measurement sat relative to it."* That single question would have
  caught the v1 sizing error at v1's own freeze. **SVA pilot case 8**; per-row fill notes in the
  result doc §5.

## Fence

No `clm-`/`def-` minted. No solidity change. No KB/manuscript/ledger edit. `src/ave` byte-untouched
and never imported. No observable, no chord, no discriminator, and none headlined.

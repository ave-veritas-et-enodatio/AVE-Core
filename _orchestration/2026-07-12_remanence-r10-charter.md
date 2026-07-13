# Remanence R10 fixed-\(N\) discriminator

**Status.** CHARTER + FREEZE — no driver yet.  
**Gate.** ★PROPOSED-RULED G-PERSIST (#661) — pending Grant confirmation; G-PERSIST's banked bin (ii) is under #655 re-adjudication (repair R9). The R10 remanence question this charter addresses is a **standing gap independent of #655's D2** — motivation survives either bin outcome. KEEP-BOTH: superseded line read "★RULED G-PERSIST (#661)".  
**Merge policy.** HOLD / do-not-merge.

## Charter intent

Fixed-\(N\) constitutive remanence discriminator on `loop_gap_harness` rank 4.
Physical picture = Level-2 loop / ferrite \(B_r\) analogue; circuit = memristive
lag + zero-drive P11; map = LOOP GAP rank-4 under G-PERSIST (node-mint closed).

## Phase log

| Phase | Status | Notes |
|---|---|---|
| 0 — Charter walk + freeze prereg | DONE | freeze `ce34f9d5`; charter `74004e37` |
| 0b — Adversarial-review repair (R6–R9) | DONE | charter §Ax3 reconciliation (R6) + authorization honesty (R9); frozen-prereg dated amendment (R7 fireable ablations / R8 pin N=10); frozen body byte-untouched |
| 1 — Driver (harness rank-4 + ablations) | PENDING | After Grant OK on charter; **R7 route (i)**: build harness-level `latch_clamp` (P11 receipt) before firing |
| 2 — Result + HOLD PR | PENDING | |

## Links

- Charter: [`../research/2026-07-12_remanence-r10-fixed-n_CHARTER.md`](../research/2026-07-12_remanence-r10-fixed-n_CHARTER.md)
- Prereg: [`../research/2026-07-12_remanence-r10-fixed-n_prereg_FROZEN.md`](../research/2026-07-12_remanence-r10-fixed-n_prereg_FROZEN.md)
- G-PERSIST: [`2026-07-12_ave-native-rulings_g-persist_x-ledger.md`](2026-07-12_ave-native-rulings_g-persist_x-ledger.md)
- Branch: `analysis/remanence-r10-charter`

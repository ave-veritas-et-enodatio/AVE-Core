# A3 — Universe return path (exterior → local)

**Status.** Driver landed — **bin (i) RETURN-RECEIVED**. HOLD / do-not-merge.
**Gate.** A2 bin (i) STUB-PASSIVE-BIASED (HOLD #657). Grant: A2 passed → A3.
**Merge policy.** HOLD / do-not-merge until Grant.

## Charter

Thin Rule-14 bidirectional stub: after A1 leave-taking, inject a known exterior
return packet on the port face and gate interior reception — no outer mesh, no
live Machian integral, no fourth engine.

## Phase log

| Phase | Status | Notes |
|---|---|---|
| 0 — Freeze prereg by push | DONE | `cfd2e690` |
| 1 — Driver + tests + result | DONE | bin (i) |
| 2 — HOLD PR | IN PROGRESS | No merge |

## Links

- Prereg: [`../research/2026-07-12_universe-return-a3_prereg_FROZEN.md`](../research/2026-07-12_universe-return-a3_prereg_FROZEN.md)
- Result: [`../research/2026-07-12_universe-return-a3_result.md`](../research/2026-07-12_universe-return-a3_result.md)
- Parent A2: [`2026-07-12_universe-stub-a2.md`](2026-07-12_universe-stub-a2.md)
- Branch: `analysis/universe-return-a3` (off A2 tip)

# Correction — approach-leak v2 fragment (2026-08-06, post Tier-2 verify, PRE-MERGE)

Corrections to [`2026-08-06-approach-leak-v2.md`](2026-08-06-approach-leak-v2.md) (one-per-lane
rule; original untouched). All of them land on `research/approach-leak-v2` **before** PR #904
merges, as dated amendment commits. Body: result doc
[`research/2026-08-06_approach-leak-v2_result.md`](../../research/2026-08-06_approach-leak-v2_result.md) §9.

## 1. The stack was reconciled: the repaired v1 tip is merged in

The original fragment records **Base:** `research/approach-leak` = `5e2694c0`. That is the
**pre-repair** v1 ship. The orchestrator then executed the SCANFRAG repair this lane's own
`FLAG-SCANFRAG` routed to it, landing v1 at `f3607be8`. The v2 branch now **merges `f3607be8`**, so
the merge order #903 → #904 lands green. The merge commit itself is a **pure merge** and is
knowingly RED — that red state is the finding it exists to expose — and the branch tip is green.

## 2. `AMENDMENT-NCBYTES-2026-08-06` — the read-only pin re-sited (Rule 11: pre-merge, disclosed, purpose-preserving)

The repair rewrote 2 of `NC-BYTES`'s 10 read-only predecessor artifacts
(`research/2026-08-05_approach-leak_result.md`, `research/drivers/approach_leak.py`). The gate pinned
all ten at `5e2694c0` and therefore went false on the merged tree — misreporting an **extrinsic,
disclosed, orchestrator-authored** event as a lane-authored write. The gate's frozen purpose ("this
lane wrote none of them") is still true.

**Re-pin choice: ALL TEN at the repaired tip `f3607be8`, one pin, not a split pin.** `f3607be8` is a
descendant of `5e2694c0` touching exactly 2 of the 10, so for the other 8 the blob object is
identical at both commits and the re-pin is a no-op **that the gate now computes rather than
claims**. One pin = one truth-source, no two-commit bookkeeping to drift, and the repaired tip is the
predecessor state that actually reaches `main`. The superseded `5e2694c0` hash is retained per
artifact in the shipped JSON.

**Nothing dropped; two conjuncts ADDED**, both gating the re-pin itself: (i) the COMPUTED moved-set
must equal the DECLARED moved-set (an undisclosed extra rewrite fails); (ii) every unmoved artifact
must be identical at BOTH commits.

**Receipt (v2.1 vs shipped v2, leaf-level, driver's own `flatten`):** 297 → 350 leaves; CHANGED 5
(`_digest`, `_runtime_sec`, `NC-BYTES/frozen`, two `blob_live`); ADDED 53, all inside `NC-BYTES`;
REMOVED 0; **outside `NC-BYTES` ∪ `_digest` ∪ `_runtime_sec`: 0**. Every physics leaf byte-identical.
Digest `b38c6c269b5dd301` → `4da48b39074d9fbc`. The receipt is **recomputed from the pre-amendment
JSON blob out of git on every `make verify`** and mutation `M6` proves it fireable.

The FROZEN prereg §3.3 is deliberately **not** rewritten; it still reads `5e2694c0`. An amendment to
a frozen instrument is disclosed beside it, never written back into it.

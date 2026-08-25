---
id: storage-response-clock-identity
title: "The storage clock and the response clock are the same number exactly — canon's 1.4e-5 near-collision is a linearization artifact"
status: OPEN
owner: grant
opened: 2026-08-25
source: _orchestration/docket-entries/2026-08-25-ruling-r58-g2-decisions.md
anchor: "a LINEARIZATION ARTIFACT of canon's own leading-order"
---

Found by the A3 collapse-check lane (2026-08-25), sympy-verified, banked in
R58 §5. **Nothing edited in canon — flag-don't-fix.**

**The finding.** Canon flags the storage clock `√(1−α) = 0.996345` and the
response clock `(1−2α)^{1/4} = 0.996331` as *"near-colliding, Δ = 1.4e-5 …
two readings of one kernel one Taylor order apart"*, with the standing
instruction *"the rate alone cannot discriminate the contour — always carry
the tag."* But the response criterion is written at leading order. Solve it
exactly — `ΔS = 1 − √(1−A²) = α ⇒ A² = 2α − α²` — and `1−A² = (1−α)²`, so
the response clock `(1−A²)^{1/4} = (1−α)^{1/2} ≡` the storage clock,
**identically, for all α**. One-line reason: the exact response condition
defines `S_resp = 1−α` and the storage condition gives `S_store = √(1−α)`, so
`S_resp = S_store²` and the ¼-vs-½ exponent difference exactly cancels the
argument difference.

**What this does and does not change.** Canon's practical guidance is
**correct and strengthened** — you cannot discriminate the two contours by
the reflection magnitude, and now for a stronger reason (they are the same
number, not merely close). What needs re-scoping is the stated basis: the
1.4e-5 gap is an artifact of canon's own truncation, not a physical
near-collision, and any downstream argument that treats the gap as a small
real quantity is resting on a rounding error.

**The ruling needed:** re-scope the contour tag's stated basis (dated Rule-12
note at `cvr-reflection-smith.md`:49-55 and the Op14 companion), or rule that
the leading-order form is the canonical definition of the response criterion —
in which case the two criteria differ by `α²` and the tag stands as written.
Either way the practical instruction survives; only its justification moves.

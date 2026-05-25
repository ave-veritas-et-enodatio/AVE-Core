[↑ Mini-KB Common](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "hosts a pending-quality support node only"
sup-id: sup-pend01
supports:
  - clm-sb4444: 1.0
-->

## Pending-Quality Analytical Support

A support whose local rigor has not been evaluated (`quality: *pending*`), so
its sup_solidity is `*pending*`. It supports clm-sb4444 at f=1.0 but contributes
NOTHING to that claim's local_quality (a pending sup_solidity is excluded from
the max — no NaN, no poison), so clm-sb4444 keeps its own valid confidence and
is never dragged to pending by this inbound support edge (INVARIANT-S10).

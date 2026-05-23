[↑ Mini-KB Common](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "hosts a support node only"
sup-id: sup-dep001
supports:
  - clm-sb3333: 1.0
-->

## Dep-Gated Analytical Support

A support that consumes its own dependency (clm-aa1111). Its sup_solidity is
dep-gated: round2(quality 0.90 × dep final 0.90) = 0.81, below its quality —
exactly the claim derivation rule applied with `quality` in place of
`confidence`. It supports clm-sb3333 at f=1.0; the lift into clm-sb3333 is the
dep-gated 0.81, not the raw quality.

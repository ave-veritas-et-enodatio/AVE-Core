[↑ Mini-KB Common](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-co1111]
exp-id: exp-cohst1
status: run
strengthens:
  - clm-co1111: 0.90
-->

## Co-Hosted Prediction And Its Bench Test

A single container that originates BOTH a claim node and an experiment node
(INVARIANT-S9). It STATES the prediction clm-co1111 (via `claims:`) and
DESCRIBES the `run` bench experiment exp-cohst1 (via `exp-id:` + `strengthens:`)
that tests it. The experiment strengthens this leaf's own co-located claim — a
node→node edge between two distinct node-bodies in one container, not a
self-loop. `kind` stays `leaf`: experiment-ness is conferred by hosting an
`exp-id`, not by a `kind`.

clm-co1111's derivation is pending, so the `run` experiment's 0.90 strength is
the only non-null solidity branch and governs the final value.

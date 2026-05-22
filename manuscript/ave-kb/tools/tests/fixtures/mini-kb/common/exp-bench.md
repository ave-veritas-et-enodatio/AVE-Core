[↑ Mini-KB Common](index.md)

<!-- kb-frontmatter
kind: experiment
exp-id: exp-bench1
status: run
strengthens:
  - clm-gg7777: 0.80
-->

## Synthetic Bench Experiment

A physical bench experiment (apparatus + measurement) whose result strengthens
claim clm-gg7777. clm-gg7777 has a numeric authored confidence but a *pending*
derivation (its dependency clm-ff6666 is confidence-pending), so its
derivation-branch solidity is null. As a `run` experiment, this leaf confers an
experimental solidity of 0.80 on clm-gg7777 — the only non-null branch — so the
claim's final solidity is RESCUED to 0.80 (the max-branch).

Experiment leaves are NOT claim-bearing (INVARIANT-S9): this leaf carries
`exp-id` + `strengthens`, never `claims:`.

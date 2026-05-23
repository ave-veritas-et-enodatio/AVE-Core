[↑ Mini-KB Common](index.md)

<!-- kb-frontmatter
kind: leaf
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

Experiment-ness is conferred by HOSTING an `exp-id`, not by a `kind`
(INVARIANT-S9). The container `kind` is `leaf`; this leaf carries `exp-id` +
`strengthens` and originates only an experiment node (no `claims:` of its own),
which on its own satisfies tier-1 coverage.

[↑ Mini-KB Common](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "hosts TWO support nodes only — no claim-quality entries of its own"
sup-id: sup-mlt001
supports:
  - clm-sb6666: 1.0
sup-id: sup-mlt002
supports:
  - clm-sb6666: *pending*
  - clm-sb7777: 0.50
-->

## A Container Hosting Multiple Analytical Supports

A single container (a KB leaf) hosts ANY number of any combination of
`clm` / `exp` / `sup` node-bodies — there is no one-per-leaf cap (INVARIANT-S10).
Here it originates TWO distinct support nodes via repeated `sup-id:` keys, each
opening its own `supports:` fan-out block:

- `sup-mlt001` (free-standing, quality 0.80) supports clm-sb6666 at f=1.0.
- `sup-mlt002` (free-standing, quality 0.70) supports clm-sb6666 at a
  `*pending*` on-point fraction (an intended-but-unassessed edge) and clm-sb7777
  at f=0.50.

Both materialize their own `node_type: support` record and their own
`relation: supports` edges; the pending fraction serializes as the literal
`*pending*`, distinct from a depends edge's null. `kind` stays `leaf`.

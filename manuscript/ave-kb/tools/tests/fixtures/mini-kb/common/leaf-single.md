[↑ Mini-KB Common](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-aa1111]
-->

# Single-Claim Synthetic Leaf

A leaf citing exactly one claim. For a single-claim leaf, Tier-2 inline
markers are not required — the frontmatter is unambiguous. This leaf
deliberately carries no `<!-- claim-quality: ... -->` marker so a test can
assert single-claim leaves may have an empty `tier2_marked` set.

## Anchor result, restated

This leaf restates the anchor result A in a second location, so claim
clm-aa1111 is cited by more than one leaf.

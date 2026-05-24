[↑ Mini-KB Common](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-aa1111, clm-bb2222, clm-cc3333, clm-dd4444]
-->

# Multi-Claim Synthetic Leaf

A leaf citing four claims. Because its `claims` list has 2+ ids, every id
carries a proximal Tier-2 inline marker adjacent to the block that maps to it.

## Foundation results

<!-- claim-quality: clm-aa1111 -->
The anchor result A is established here with no entry-level dependency.

<!-- claim-quality: clm-bb2222 -->
The mid-band result B is established here, also dependency-free.

## Derived results

<!-- claim-quality: clm-cc3333 -->
Result C builds on result A — a single-dependency derivation.

<!-- claim-quality: clm-dd4444 -->
Result D builds on both A and B — the min() over the dependency set governs
its solidity.

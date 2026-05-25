[↑ Mini-KB Common](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-sb1111, clm-sb2222, clm-sb3333, clm-sb4444, clm-sb6666, clm-sb7777]
-->

# Support-Beneficiary Synthetic Leaf

A multi-claim leaf citing the support-beneficiary claims. Each id carries a
proximal Tier-2 inline marker.

## Full and fractional support

<!-- claim-quality: clm-sb1111 -->
Beneficiary J is lifted to 0.90 by the free-standing support at full on-point
relevance (f=1.0).

<!-- claim-quality: clm-sb2222 -->
Beneficiary K is lifted to 0.45 by the same support at half on-point relevance
(f=0.50).

## Dep-gated and pending supports

<!-- claim-quality: clm-sb3333 -->
Beneficiary L is lifted to 0.81 by a support whose own dependency throttles it.

<!-- claim-quality: clm-sb4444 -->
Beneficiary M keeps its own 0.55 — a pending support contributes nothing and
does not poison it.

## Multi-sup container beneficiaries

<!-- claim-quality: clm-sb6666 -->
Beneficiary O is lifted to 0.80 by the first of two supports co-hosted on one
container; the second names it at a pending fraction (no contribution).

<!-- claim-quality: clm-sb7777 -->
Beneficiary P is lifted to 0.35 by the second of the two co-hosted supports at
half on-point relevance (f=0.50).

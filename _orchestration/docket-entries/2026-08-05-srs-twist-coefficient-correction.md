# Correction — srs-twist fragment (orchestrator, 2026-08-05, post Tier-2 verify)

Corrections to `2026-08-05-srs-twist-coefficient.md` (one-per-lane rule; original untouched):

1. The headline law reads κ/ε = ĉ₂q²/ℓ_node — dimensionally inverted; the correct form (the
   lane's own §6.3) is **κ/ε = ĉ₂·ℓ_node·q²**. Downstream numbers unaffected.
2. "max τ = 0.0 exact" → ĉ₂ and κ/ε are the exact zeros; τ's worst shipped value is 9.5e-34.
3. Audit-supplied positive control on the record: a 1e-3 single-bond tilt (432 broken) yields
   τ = 1.06e-7, linear in the tilt — the NO-TWIST null is a symmetry null.
4. Routed follow-ons: the signed-ĉ₂ sign flip across the wall sweep (artifact vs crossover);
   the "57 orders" derivation; the FLAG-1 back-reaction question (PR #508 Δν) as the lane
   already routed it.

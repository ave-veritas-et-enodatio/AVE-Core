---
id: ell-c-name-collision
title: "Two different lengths may share the name ell_c — the sqrt(6) Cosserat coupling length vs the weak-range construction"
status: OPEN
owner: grant
opened: 2026-08-25
source: manuscript/ave-kb/common/q-g47-substrate-scale-cosserat-closure.md
anchor: "Spatial scale of substrate's saturation boundary"
---

Surfaced by the 2026-08-25 Cosserat-DOF walk. **A QUESTION, not an asserted
collision** — one side was verified directly, the other was not.

**Verified side.** Canon's **Cosserat coupling length** is
`ℓ_c / ℓ_node ≈ √6`, derived (not fitted) from the discrete moduli at the
K=2G operating point: `k_a = 2/7`, `k_s = 1/7` → `K_0 = 16/7`, `G_0 = 8/7` →
`ξ_K1 = 8/3`, `ξ_K2 = 32` → `ℓ_c²/ℓ_node² = 32/(2·8/3) = 6`. Clean rationals.
Canon's own gloss for the row: *"Spatial scale of substrate's saturation
boundary."* With `ℓ_node = ħ/(m_e c) ≈ 3.86e-13 m`, that puts
`ℓ_c ≈ 9.4e-13 m`.

**Unverified side.** The EE-mapping corpus carries *"Weak force range
`ℓ_c = √(γ_c/G_vac)` ↔ transformer leakage-inductance characteristic
length"*. A weak-interaction range is ~1e-18 m — some fifteen orders from the
√6 value above.

**The question.** Are these two different lengths sharing a name (the
`ℓ_c` / `ELL_C` glyph already sits on the symbol-collision watch list), or is
one mapping misattributed? **This is a concrete instance of the open
`gammac-gc-modulus-identity` item** — the same L²-apart dimensional question,
now with a specific pair of numbers attached. Recommend folding it into that
ruling as evidence rather than adjudicating separately.

**Why it matters beyond hygiene:** the √6 row is canon's statement that the
**Cosserat sector sets the spatial scale of the saturation boundary** — i.e.
that a bound A1 core's extent is a T2 property. Any downstream use of `ℓ_c`
inherits whichever length the name resolves to.

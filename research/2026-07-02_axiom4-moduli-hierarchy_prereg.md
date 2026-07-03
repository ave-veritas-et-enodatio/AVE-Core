# FROZEN PREREG — Axiom-4 final gate: does the K4 lattice have `k_stretch ≫ k_bend` (→ inextensible → shape is a full Axiom-1 theorem)?

**Date:** 2026-07-02
**Lane:** derivation (the FINAL gate of the Axiom-4 arc; prove-or-disprove). Analysis + adversarial verification.
**Branch:** `analysis/axiom4-moduli-hierarchy` (off `origin/main` @ `c9a1188c`)
**Parent:** buckling-kernel result (PR #459, Outcome B) — the kernel shape `S(A)=√(1−A²)` is an α-free geometric theorem of the fixed bond length `A_yield=ℓ_node`, **GIVEN inextensibility** (bow-without-stretch); the ONE residual is whether inextensibility (`k_stretch ≫ k_bend`) is Axiom-1-forced.
**Disciplines:** `ave-prereg`, `substrate-native-check`, `pre-test-physics-check`, `consistency-vs-emergence`.

> **SHA-PIN (Rule-16).** The prove-or-disprove target (§1), the discriminator (§3), the classification axis (§5) locked before the verdict.

## 0. Open-goal framing (prove-or-disprove, per feedback_open_goal_framing_before_proof)

Determine whether the vacuum K4 lattice's bond-stretch stiffness `k_a` dominates its bond-bend stiffness `k_s`
strongly enough (`k_stretch ≫ k_bend`) that a loaded bond **bows at fixed arc-length (inextensible)** — which
would make the buckling `√(1−A²)` a FULL Axiom-1 theorem (Outcome A) — OR whether `k_a`/`k_s` is comparable (bond
**extensible**, the √ approximate — Outcome NEGATIVE), OR whether the ratio inherits from GR-imported K=2G rather
than Axiom-1 (Outcome C). **Both a rigorous YES and a rigorous NO are full, valuable results — do NOT force either.**

## 1. The quantitative state (ave-prereg — validated numbers, NOT green field)

From `research/2026-06-15_k2g-crystalline-provenance_result.md` (standard z=4 Keating lattice dynamics, **validated
against carbon diamond to 0.4%**: predicted relaxed C44 = 575.9 vs measured 578.0 GPa):

- **z=4 K4 is sub-isostatic** (Maxwell count `z < 2d = 6`): central-force-only (`k_s→0`) ⟹ all shear moduli → 0,
  bulk K stays finite. **Shear rigidity comes ENTIRELY from bond-bending `k_s`; bulk from stretch `k_a`.**
- **`K/G` is a one-parameter family in `ρ ≡ k_a/k_s`** (`k2g-provenance` Finding 2): `K/G(ρ)` smooth, monotone.
  Table: `ρ=2 → K/G≈0.97`; `ρ=5.30 → K/G=2.00`. (Simple model `K_0=4k_a+8k_s, G_0=8k_s` gives `K=2G ⟺ k_a=2k_s`,
  `ρ=2`; canonical AVE `k_a=2/7, k_s=1/7` (`q-g47:58`) ⟹ **`ρ=2`**; full-Keating+Kleinman gives `ρ=5.30`.)
- **`ℓ_c/ℓ_node = √6 ≈ 2.45`** (`q-g47:84`, `continuous-springs-reframing.md:40`), `ℓ_c²=(β+γ)/(2(μ+κ))` — the
  Cosserat length EXCEEDS the bond length ⟹ **bending is a stiff, long-range object, NOT a soft local mode.**
- **The K=2G lock is GR-imported / back-fit** (`secondary-scale-shared-b-node.md:35`; `k2g-provenance` §4: "geometry
  fixes the FORM `K/G=f(k_a/k_s)`; it cannot fix the VALUE; to land on K=2G you must supply `ρ*` from outside").

**Diagnostic:** `k_stretch/k_bend = ρ ∈ [2, 5.3]` — a few×, NOT `≫`. The ratio at the vacuum point is *set by K=2G*,
which is GR-imported. `ℓ_c/ℓ_node=√6` corroborates bend-not-soft. This LEANS strongly toward inextensibility FAILING.

## 2. Physical picture (Step 1.5)

- A pre-compressed (over-braced, `L_0 > d`) K4 bond sits past its Euler threshold — buckled at rest.
- An applied field straightens it (`A`: 0=buckled → 1=straight). The √ requires the bond to *unbend at fixed
  arc-length* (inextensible) so its tip traces a circle (`A²+S²=ℓ²`, Pythagoras).
- Inextensibility ⟺ unbending is cheap vs stretching (`k_bend ≪ k_stretch`): the bond prefers to bend/unbend (fixed
  length) rather than compress/extend. If `k_bend ~ k_stretch` (`ρ~2`), straightening involves BOTH unbending AND
  length change ⟹ arc-length NOT conserved ⟹ the √ is only approximate.

## 3. The discriminator (LOCKED)

**Inextensibility holds (Outcome A) iff, at the vacuum operating point, unbending a K4 bond conserves its arc-length
to leading order — i.e. `k_stretch ≫ k_bend` in the sense that the fractional length change during a full unbend is
`≪` the bow amplitude.** Pre-registered outcomes:

- **Outcome A (gate CLOSES — inextensible).** `k_a/k_s` (or the relevant slenderness/arc-length measure) is large
  enough that arc-length is conserved to leading order, AND this is Axiom-1-forced (NOT via GR-imported K=2G). ⟹
  the buckling √ is a full Axiom-1 theorem; Axiom 4's shape demotes from postulated to Axiom-1-derived.
- **Outcome NEGATIVE (inextensible FAILS — the honest-expected).** `k_a/k_s = ρ ∈ [2, 5.3]` is comparable, not `≫`;
  the bond stretches appreciably while unbending (arc-length NOT conserved); `ℓ_c/ℓ_node=√6` confirms bend-not-soft.
  ⟹ the inextensible-rod √ is an APPROXIMATION; Axiom 4's shape stays postulated at the geometry level. Quantify the
  approximation error (how far is the true, extensible-bond `S(A)` from `√(1−A²)`?).
- **Outcome C (inherits, not Axiom-1).** The ratio `ρ*` that would give inextensibility is set by K=2G (GR-imported)
  or the back-fit — so even a favorable `ρ` is not Axiom-1-forced. (Note: `ρ=2 ⟺ K=2G` already suggests this.)

**Adversarial tell (the null to defend):** `ℓ_c/ℓ_node=√6 > 1` + `ρ∈[2,5.3]` + `ρ⟺K=2G-imported` all point NEGATIVE.
The super-adversary's job is to SAVE Outcome A — find a regime (pre-buckled near-threshold limit? small-deflection?
a slenderness argument independent of `ρ`?) where the √ is exact regardless of the modest `ρ`. If it cannot, NEGATIVE stands.

## 4. Method / lanes (LOCKED)

- Analysis + adversarial verification. Numpy: the extensible-bond `S(A)` (unbend a strut with finite `k_a`, `k_s`)
  vs the inextensible `√(1−A²)`; quantify the deviation at `ρ=2` and `ρ=5.3`. Read the `k2g-provenance` Keating
  relations + the engine moduli.
- **substrate-native-check:** the K4 DISCRETE bond stiffnesses (`k_a`, `k_s`) → continuum Cosserat moduli (`G`, `γ`)
  via the lattice sum (`χ_K=(ℓ_c/d)²`), NOT a generic continuum-elasticity default. Rupture = Γ=−1 boundary.
- **do-not-force-a-positive AND do-not-force-a-negative:** the tell leans NEGATIVE, but Outcome A must be genuinely
  killable, not assumed dead — give the super-adversary a real shot at saving it. **retract-don't-refill.**

## 5. Classification (consistency-vs-emergence)

If Outcome A: name the NEW primitive (the Axiom-1-forced `k_stretch≫k_bend` hierarchy) and verify it does NOT route
through K=2G. If NEGATIVE/C: the buckling √ is a consistency-class approximation, NOT an Axiom-1 emergence; Axiom 4's
shape stays SHAPE-DERIVED(conditional). Do NOT inflate a `ρ~2` (comparable, GR-inherited) into "≫".

## 6. Decision points → Grant

1. The verdict (A / NEGATIVE / C) + the final canonical status of Axiom-4's shape (Axiom-1-theorem vs
   postulated-at-geometry). Recommend, Grant rules.
2. If NEGATIVE: whether to canonize "the buckling √ is an approximation; the true extensible-bond shape deviates by
   X%" — a forward, falsifiable statement (the deviation is an AVE prediction). Recommend, Grant rules.

## 7. Outputs

This prereg + `2026-07-02_axiom4-moduli-hierarchy_result.md` (the `ρ=k_a/k_s` derivation, the arc-length-conservation
test, the K=2G-provenance audit, the extensible-vs-inextensible deviation, the verdict + classification). Branch + PR.

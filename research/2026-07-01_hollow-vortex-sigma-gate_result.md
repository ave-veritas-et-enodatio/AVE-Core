# RESULT — the σ-gate: is the electron a viable HOLLOW VORTEX?

**Date:** 2026-07-01
**Lane:** implementer (analysis / derivation — NO simulation)
**Prereg (SHA-pinned, frozen BEFORE any number):**
`research/2026-07-01_hollow-vortex-sigma-gate_prereg_FROZEN.md` (commit `4fae5367`)
**Class tag (frozen):** **Class-C consistency** (see prereg §3; not a chord).
**Disciplines applied:** `ave-prereg`, `ave-canonical-source`, `consistency-vs-emergence`,
`substrate-native-check`, `phase-space-coordinate-check`, `verify-before-cite`.

> **★ GUARD (from prereg).** The structural bind (opener ∝ R⁻³ vs closer ∝ R⁻¹) is a
> near-tautology (the PR#443 trap). The RESULT here is NOT "it binds" — it is the DERIVED
> value **R\*** and the DIMENSIONLESS **R\*/ℓ_node**, which is what discriminates
> electron-scale-viable from DEAD.

---

## Headline (fill order: σ → Γ → R* → verdict)

| quantity | derived value (engine units) | provenance |
|---|---|---|
| σ (void↔vacuum interface tension) | **3√6/10 − √30/10 = 0.18712** ρ₀c₀²·ℓ_node | §1, from scratch |
| — coincides with existing 0.187? | **YES** (identity, §1.4) | finding, not plug-in |
| Γ (conserved circulation) | *(§2)* | |
| R* = C_geo·Γ/√σ | *(§3)* | |
| **R\*/ℓ_node** | *(§3)* | |
| **GATE VERDICT** | *(§4)* | |

---

## 1. Part 1 — σ DERIVED FROM SCRATCH (no 0.187 plug-in)

**substrate-native-check:** CP2 bulk-K density-step interface (the void↔vacuum boundary is a
dilatation-sector density step, NOT a Cartesian gradient); CP4 the interface energy is a
real-space per-area integral across the diffuse boundary; CP10 the interface is the impedance
step of a density void, not a confining force.

### 1.1 The substrate primitives (all canonical, cited)

| primitive | value | canonical source |
|---|---|---|
| golden ratio φ | (1+√5)/2 = 1.6180 | `constants.py:238` |
| cavitation floor ρ̄_cav | −1/φ = −0.61803 | `cavitation_flow.py:64` |
| density jump Δρ̄ = 0 → ρ̄_cav | 1/φ = 0.61803; (Δρ̄)² = 1/φ² = 2−φ = 0.38197 | derived from above |
| couple-stress interface width ℓ_c | √6·ℓ_node = 2.4495 | `constants.py:298-302` |
| bulk modulus K = 2G | 0.6 (G = 0.3) | `constants.py`, K=2G canon |
| P-wave modulus M = ρ₀c₀² | 1.0 | `cavitation_flow.py:103` (c_bulk(0)=c₀=1) |

### 1.2 The square-gradient (Cahn–Hilliard / Korteweg) interface energy

The void↔vacuum boundary is a diffuse density interface. Its per-area energy is the
square-gradient functional

```
σ = ∫ [Δf₀(ρ̄) + ½ λ_grad (dρ̄/dx)²] dx ,     λ_grad = K · ℓ_c²
```

with the interface width set by the Cosserat couple-stress length ℓ_c (dimensional closure:
the gradient stiffness λ_grad carries the bulk-energy scale K over the couple-stress length ℓ_c;
`bubble-physics-completion.md:45-51`). For a tanh kink profile
`ρ̄(x) = (Δρ̄/2)·tanh(x/ℓ_c)` at gradient/bulk equipartition, the integral is analytic.

### 1.3 The DERIVED prefactor and value (sympy, from scratch)

I did **not** assume c_σ = 1/3 or the value 0.187. sympy integrates the gradient functional
across the tanh kink and returns the prefactor:

```
σ = ∫_{-∞}^{∞} λ_grad (dρ̄/dx)² dx  =  (1/3) · K · ℓ_c · (Δρ̄)²      ⇒  c_σ = 1/3  (DERIVED)
```

Substituting the substrate primitives (K = 2G = 0.6, ℓ_c = √6, (Δρ̄)² = 1/φ²):

```
σ[K=2G] = (1/3)·(0.6)·√6·(1/φ²) = 3√6/10 − √30/10 = 0.18712436…   ρ₀c₀²·ℓ_node
σ[M=1 ] = (1/3)·(1.0)·√6·(1/φ²) = √6/2 − √30/6      = 0.31187…      ρ₀c₀²·ℓ_node
```

**Exact closed form (headline, K=2G):**  **σ = 3√6/10 − √30/10 ≈ 0.18712**.

The M-branch (0.31187) is retained as the honest upper edge (the P-wave modulus is the physical
radial-dilatation stiffness; K=2G is the static bulk modulus). The gate (§4) carries both.

**Cross-check (B) — exact bulk-energy excess.** Integrating the canonical rarefaction EOS
pressure `p(ρ̄) = ρ̄ − ½ln(1−ρ̄²)` (`cavitation_flow.py:166`) from 0 to ρ̄_cav gives the exact
work to create the void: `e_bulk = 0.14606` per volume, so `|e_bulk|·ℓ_c = 0.3578` per area.
This is the same ORDER as the gradient σ, confirming the two interface-energy contributions are
co-equal (as `bubble-physics-completion.md:85` found) — the tanh-CH σ is not an over- or
under-estimate by orders. It does NOT change the headline (the CH square-gradient σ is the
interface tension; e_bulk is the bulk driving energy, a consistency cross-check).

### 1.4 THE INTERFACE IDENTITY (the honesty hinge — pre-committed finding rule)

**FINDING: the independently-derived cavity-boundary σ EQUALS the existing σ ≈ 0.187.** The
exact form is 3√6/10 − √30/10 = 0.187124; the existing corpus value (`bubble-physics-
completion.md:67`) is the rounded 0.187 — the 0.00012 gap is pure decimal rounding, not a
physical difference.

**Why they coincide (the identity, stated explicitly).** The existing 0.187 is the surface
tension of a *generic bulk-density step* of depth Δρ̄ = 1/φ. The hollow-vortex cavity boundary
is *precisely such a step*: the void interior sits at exactly the cavitation floor ρ̄_cav = −1/φ
(the deepest reversible tensile state the incompressible-melt EOS allows), and the exterior is
ambient ρ̄ = 0. Same Δρ̄ = 1/φ, same couple-stress width ℓ_c = √6, same modulus K = 2G ⇒ **the
void↔vacuum interface IS the canonical bulk-density-step interface.** This is a genuine
coincidence of the two derivations, not a circular plug-in: the value was rebuilt from φ, √6,
and K=2G with the c_σ=1/3 prefactor derived symbolically, and only *then* compared.

**Honest ceiling (carried from #190).** This σ is a *gradient-energy scaling* with an assumed
tanh profile across a NON-double-well EOS (the canonical cavitation branch is a dynamical
tensile-failure state, not a coexistence phase; `cavitation_flow.py:28`,
`bubble-physics-completion.md:89`). So σ is **CANDIDATE-class** in absolute value (the O(1)
prefactor c_σ=1/3 and the K-vs-M modulus choice are the sources of ~1.7× spread). The gate band
(§4) is a decade wide precisely to absorb this.

**σ (frozen for §3):  σ = 3√6/10 − √30/10 = 0.18712  (K=2G headline); 0.31187 (M edge).**

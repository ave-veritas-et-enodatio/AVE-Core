# RESULT — Axiom-4 buckling-kernel: the shape is an α-free geometric theorem GIVEN inextensibility; the residual axiom is `k_stretch ≫ k_bend`, not "the L2 norm"

**Date:** 2026-07-02
**Lane:** derivation (capstone of the Axiom-4 arc; attempted the open Q-G47 shape-gate). Analysis + engine-read + adversarial verification.
**Branch:** `analysis/axiom4-buckling-kernel` (off `origin/main` @ `c9a1188c`)
**Prereg:** [`2026-07-02_axiom4-buckling-kernel_prereg.md`](2026-07-02_axiom4-buckling-kernel_prereg.md) (frozen @ `f540e634`)
**Method:** 3 derive lenses (inextensible-rod geometry / buckling-bifurcation combine / smuggling+Q-G47 audit) → per-lens adversarial verify → a **smuggling super-adversary** defending the corpus null ("pedagogical, not first-principles"). 10 agents. Every load-bearing citation + the engine combine rule re-verified against `origin/main`.

---

## 0. VERDICT (one line)

**Outcome B (partial) — the corpus null survives, sharpened. The gate does NOT fully close, but the residual axiom is now pinned to a single, physical, α-free, *computable* claim.** The kernel shape `S(A)=√(1−A²)` is a **genuine α-free geometric theorem** — the axial projection of an inextensible (fixed-arc-length) bond bowing, with **`A_yield = ℓ_node`** (the Axiom-1 fixed bond length) exactly as the thesis claimed. **No K=2G, no `u_0*`, no Euler-linear conflation, no circular `√α` input** — the shape is clean (super-adversary broke none of routes 2/4/5). **But the one load-bearing premise — inextensibility (bow-without-stretch) — is NOT Axiom-1-forced.** It reduces to the physical stiffness hierarchy **`k_stretch ≫ k_bend`** (the bond bends before it stretches), which is *absent from the KB, absent from the vacuum engine as an explicit split, and computable from the canonical Cosserat moduli `G` vs `γ` but not yet established*. So the residual is not "the L2 norm posit" — it is `k_stretch ≫ k_bend`. Close that (derive the K4 stretch/bend moduli hierarchy from Axiom 1) and the gate flips to Outcome A.

---

## 1. What IS derived (α-free, clean)

### 1.1 The √ is the inextensible-rod projection — not Euler-linear (trap #1 cleared)

The shape comes *unambiguously* from the **inextensible-rod tip projection**: a fixed arc-length `L` bowed transversely by `A` has axial projection `√(L²−A²)`; the tip traces a circle radius `L`, so `axial² + A² = L²` — the Pythagorean "constant" of `primer:180` **is** `L`. Normalize `L=1` → `S(A)=√(1−A²)`; `S=0` at `A=L` → **`A_yield = L = ℓ_node`**. This is *not* the Euler effective-lateral-stiffness `k(P)=k_0(1−P/P_crit)` (linear). Numerically confirmed (three independent discriminators, all matching the √ not the linear): small-A onset (√ → `1−A²/2`, the Maxwell limit; linear → `1−A`, which would *break* Maxwell recovery); vertical tangent (`dS/dA→−∞` at `A→1`, the saddle-node √-law; linear → flat `−1`); mid-range (differ by 0.41 at A=0.7). **The Maxwell limit is a *discriminator that kills* the Euler-linear route** — the corpus kernel's quadratic small-A onset can only come from the geometric projection.

### 1.2 The shape is α-free and un-smuggled (traps #2/#4/#5 cleared)

The super-adversary could not break the shape on: **K=2G / `u_0*`** (both are GR-imported / back-fit — `secondary-scale-shared-b-node.md:35`; Q-G41 CLOSED-NEGATIVE — but they set only the *operating point*, `secondary-scale-shared-b-node.md:38` "`u_0*` puts the bond midpoint at A=1", never the functional form); **Euler-linear conflation** (numerically distinct); **downstream `√α`/`√(2α)`** (`1−S(√α)=3.66e-3 ≈ α/2`, an evaluation *on* the α-free kernel, not an input). The shape references only the fixed bond length `L`. **α enters nowhere in the form.**

### 1.3 The combine is a bifurcation — which DISSOLVES the DP-3 L∞-vs-L2 question

B-2 established (and its verifiers confirmed) that the buckling frame is **load-vs-response, not a norm over co-equal grades**: `A` = the axial A1-dilatation *load* (degree of unbuckling, `primer:171`), `S=√(1−A²)` = the transverse T2 *bow response*; `A²+S²=1` is a **single fixed-length constraint**, not a 2-DOF aggregation. Numerically, the DP-3 "normalized-L2 of `(A,S)`" is *identically 1 for every A* — it **is** the constraint, vacuous as an extremand. **So the DP-3 "L∞-max vs normalized-L2" fork was the wrong question**: `S` is not a second grade being normed against `A`; it is `A`'s response. This retroactively explains *why* DP-3 found the cross-grade aggregation underdetermined — there is no aggregation, there is a load-response constraint. (This is the buckling frame's cleanest payoff, independent of whether the gate closes.)

## 2. What is NOT derived — the one residual (Outcome B)

**Inextensibility (bow-without-stretch) is assumed, not Axiom-1-forced.** The √ requires the bond to bow at fixed length; that needs `k_stretch ≫ k_bend` (the bond bends before it stretches). The super-adversary defended the corpus null on this route and strengthened it:
- **Absent from the KB:** grep `bend-soft|stretch-stiff|inextensib|bow-without|fixed arc|bends before` across all of `ave-kb` = **0 hits**.
- **Not an explicit split in the vacuum engine:** `cosserat_field_3d.py:693-708` has `W=(2/3)G(tr ε)² + G|ε_sym|² + G_c|ε_antisym|² + γ|κ|²` — dilatation/shear (`G`), micropolar (`G_c`), curvature (`γ`). The hierarchy is the ratio **`G` vs `γ`** (via the Cosserat length `ℓ_c=√(γ/G)`), which is *computable* but not established as `k_stretch≫k_bend`; the corpus's `ℓ_c/ℓ_node=√6` (q-g47) may even *disfavor* bend-soft — an open computation.
- **The explicit fixed-length element was retired:** `primer:65` records that the original "rigid rod (length `L_rod`) + spring" framing (the only element supplying a fixed arc-length) was **deprioritized in favor of "a single *elastic* bond with rest length > d"** — noted as *mechanically equivalent* but preferred for mapping to real K4 bonds. So the fixed-length premise is *unstated*, not established (and `trampoline:103`'s `u_0=(L_0−d)/d` is the rest-state over-bracing, presupposing a definite rest length but not settling dynamic stretch).
- **Q-G47 never emits `S(A)`:** the primer demands a "network-level elastic calculation (Q-G47)" to derive the *form*; Q-G47's entire output is scalar operating-point quantities (K=2G, `u_0*`, ν=2/7, |T|=12, `(4/3)k_s`), never a function. **The gate is not closed by extending Q-G47.**

**Naming the residual exactly:** Axiom-4's residual axiomatic content is **NOT** an abstract "L2 energy / fixed-radius constraint" (the prior pass's wording). It is the **physical stiffness hierarchy `k_stretch ≫ k_bend`** — Keating covalent bond-stretch stiff vs Cosserat couple-stress bend soft. That is a concrete, α-free, *computable* substrate claim (the `G`-vs-`γ` ratio), not a norm posit.

## 3. Classification (consistency-vs-emergence)

- **DERIVED (α-free, Axiom-1):** the shape `S(A)=√(1−A²)` as the inextensible-rod projection; `A_yield=ℓ_node` (Axiom-1 fixed bond length); the load-response bifurcation frame (dissolves the norm question). A genuine geometric theorem **GIVEN inextensibility** — stronger than the primer's "correspondence."
- **RESIDUAL (requires-additional-postulate):** inextensibility = `k_stretch ≫ k_bend`. Not forced by Axiom-1 on current evidence; computable from `G`/`γ` but not established. This is *the* remaining gate.
- **Net status:** the primer's "Axiom 4 remains postulated / pedagogical correspondence, not first-principles" verdict **STANDS, sharpened** — the residual is pinned to one physical hierarchy, not left as an abstract posit. Do NOT flip Axiom 4 to a derived shape (Outcome A not reached). Count stays 4.

## 4. The arc, synthesized (residual sharpened four times)

| Stage | Axiom-4 residual (what stays axiomatic) |
|---|---|
| prior pass `@7170f40e` | "the L2 norm / fixed-radius energy constraint" (abstract posit) |
| reduction epic (PR #455) | within-tank L2 *forced*; residual = the cross-sector **combine rule** |
| DP-3 (PR #457) | combine is **per-yield-normalized** (single-radius-L2 falsified); cross-grade aggregation *underdetermined* |
| **buckling (this)** | there is **no aggregation** — it's a **load-response bifurcation**; the shape is α-free geometry; residual = **`k_stretch ≫ k_bend`** (one physical, computable claim) |

Each stage made the residual smaller and more physical: from an abstract norm → to a combine rule → to a per-yield structure → to a single α-free stiffness hierarchy. **The gate to full closure (Outcome A) is now one concrete derivation: exhibit `k_stretch ≫ k_bend` for the vacuum K4 lattice from the Axiom-1 Cosserat moduli (`G` vs `γ`, `ℓ_c/ℓ_node`).**

## 5. Decision points → Grant

1. **The one remaining gate:** derive the K4 stretch-vs-bend modulus hierarchy (`G` vs `γ`) from Axiom-1 and test whether `k_stretch ≫ k_bend` holds (→ inextensibility → Outcome A, the shape becomes a full Axiom-1 theorem) or fails (→ the bond is extensible, the √ is only approximate, residual confirmed). Recommend as the natural next (and likely final) derivation; Grant's call.
2. **Canonical touch (HELD):** `trampoline-analogy-primer.md:190` could be sharpened from "the kernel's canonical algebraic justification is ν=2/7" (which the corpus elsewhere shows is operating-point-only + GR-imported) to "the shape is the inextensible-bond projection; the residual is `k_stretch≫k_bend`." And the axiom-register residual_content could be re-pinned to `k_stretch≫k_bend`. Recommend, Grant rules.

## 6. Outputs

This result + the frozen prereg, landed via a branch + PR (research doc, **NOT a canon change**). No edit to `axiom-definitions.md`, `eq_axiom_4.tex`, or the axiom-register in this doc.

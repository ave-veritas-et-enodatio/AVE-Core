# DERIVATION — X38: S₁₁-minimization bore selection (the symmetric 3-port junction S-matrix + the canonical Op6 argmin)

**Date:** 2026-07-10 · **Branch:** `analysis/x38-s11-bore-selection` · **Prereg (FROZEN):** [`2026-07-10_x38-s11-bore-selection_prereg_FROZEN.md`](2026-07-10_x38-s11-bore-selection_prereg_FROZEN.md) (commit `cc386be1`, committed 2026-07-10T14:46:25Z / pushed 14:46:55Z — before this doc, before any driver code)

**SECTOR HEADER.** MODE = linear small-signal (S-parameters). REGIME = cold, sub-yield, lossless (reactive-only). SECTOR = bare-bond network primitive (scalar/compression channel, Phase 1); soliton scales are frozen comparison marks only. Vector/torsion scoped out (prereg §8).

**CLASS.** MIXED: the selected `f*` is derived-geometric (§3 shows μ₀/ε₀/ℓ cancel; the argmin is a pure number); the SCALE `ω_C = c/ℓ_node` is dimensional-forced/identity, reporting only.

---

## 1. The memoryless baseline (what X38 must recover) — Rule-14 reuse of #604 / X37

The srs vacuum is a distributed TL network: bonds are TLs (`L′ = μ₀`, `C′ = ε₀`; `Z₀ = √(L′/C′)`, `c = 1/√(L′C′)`). Two independent memoryless facts anchor the recovery gates:

**(a) The bare-junction reflection (X38's own baseline).** `z` identical semi-infinite lines meet at a memoryless node. A wave incident down port 1 sees the other `z−1` lines in parallel (each presents its characteristic `Z₀`):
```
Z_load = Z₀ / (z − 1),     Γ = S₁₁ = (Z_load − Z₀)/(Z_load + Z₀) = (2 − z)/z.
```
For the srs coordination **z = 3**: `Z_load = Z₀/2`, **S₁₁ = −1/3, |S₁₁| = 1/3.** (Equivalently the memoryless star `S_ij = 2/3 − δ_ij` gives `S₁₁ = 2/3 − 1 = −1/3`.) **The memoryless junction is NOT matched** — it back-scatters `|Γ|² = 1/9` of the incident power. This is the whole reason a nontrivial `f*` could exist, and it is the G-B(i) recovery target.

**(b) The scalar band top (X37 / #604's ceiling).** Embedded in the periodic srs net, the memoryless dispersion is `ω = ω_link·arccos(μ/3)`, `ω_link = √3·ω_C`, band top at `μ = −3`: `ω_top = π√3 ω_C = 5.441398 ω_C` ([`2026-07-09_srs-band-survey_result.md:18`](2026-07-09_srs-band-survey_result.md), closed form `π/ANALYTIC_NETWORK_FACTOR`). This is the G-B(ii) recovery target, reached through X37's LOADED `junction_parasitics.g_scalar(f→0)`.

**Same junction, two terminations.** X37 embeds the parasitic junction in the *periodic* lattice (Bloch), giving the band ceiling `g(f)`. X38 terminates the far arms in *matched semi-infinite lines*, giving the isolated-junction reflection `S₁₁(θ;f)`. The parasitic elements are IDENTICAL (`x = s_L f θ`, `p = s_C f θ`); the two observables are complementary readings of the one vertex.

---

## 2. The vertex as a symmetric 3-port TL discontinuity — the C₃ᵥ scattering structure

Three identical lines meet at 120° (C₃ᵥ). A lossless reciprocal symmetric 3-port has a scattering matrix fixed by symmetry up to two eigen-reflections (X37 §2):
- **symmetric / breathing** `(1,1,1)/√3`: memoryless `Γ_S = +1` (the node sees an OPEN — KCL `ΣI=0` has nowhere to go);
- **differential** `(1,−1,0),(1,1,−2)`: memoryless `Γ_A = −1` (a virtual SHORT).

The star `S_ij = 2/3 − δ_ij` has row-sum 1 (`Γ_S = +1`) and `S_ii − S_ij = −1` (`Γ_A = −1`). The single-port reflection `S₁₁ = (Γ_S + 2Γ_A)/3 = (1 − 2)/3 = −1/3` — consistent with §1(a). The scalar band TOP couples to the **breathing** combination (the π-mode is fully staggered ⇒ at each node all three arms are equivalent), i.e. the compression ceiling sees the dressed symmetric-mode reflection.

**Lossless-multiport caveat (load-bearing for the Op6 reading, §4).** A lossless reciprocal 3-port has a UNITARY `S`, so `S†S = I` and `λ_min(S†S) ≡ 1` — the FULL-multiport Op6 target is degenerate at any lossless vertex. The non-trivial Op6 object is the **1-port reflection block** `[S₁₁]` (the vertex as a 1-port load; the other two arms radiate power into the network, so the 1-port is NOT lossless and `λ_min = |S₁₁|²` CAN reach 0). This is exactly how the trefoil derivation applied Op6 — to the reflection at a boundary, not to a unitary multiport (§4).

---

## 3. The loaded S₁₁ — exact algebra, and why it is dimensionless (G-A)

Dress the vertex with the X37 leading-order lumped parasitics: series throat `L_j = s_L·μ₀·d` in each arm, shunt accumulator `C_j = s_C·ε₀·d` at the node, `d = f·ℓ_node`. Normalize all impedances to `Z₀`. The junction enters ONLY through the dimensionless products
```
x = ωL_j/Z₀ = ω s_L μ₀ f ℓ / √(μ₀/ε₀) = s_L f · (ωℓ√(μ₀ε₀)) = s_L f · θ
p = ωC_j·Z₀ = ω s_C ε₀ f ℓ · √(μ₀/ε₀) = s_C f · (ωℓ√(μ₀ε₀)) = s_C f · θ
```
**μ₀ and ε₀ cancel; ℓ_node folds into `θ = ω/ω_C`** (a reporting unit). Incident down port 1, the other `z−1` arms are matched semi-infinite lines (normalized impedance 1):
```
z_far  = 1 + j x                          (far arm: series throat then matched line)
y_node = (z − 1)/z_far + j p              ((z−1) far arms in parallel + shunt accumulator)
z_in   = j x + 1/y_node                   (series throat on the incident arm + node)
S₁₁(θ; f, s_L, s_C) = (z_in − 1)/(z_in + 1).
```
This is a pure function of `(θ, f, s_L, s_C, z)` — all geometric. **No physical scale is an input** (anti-install; the module imports none; the Op6 evaluator `universal_operators.universal_eigenvalue_target` is a linear-algebra operator on the dimensionless block — importing it introduces no scale, and the per-file G-A AST scan sees only this module).

**Bare recovery (`f→0` or `θ→0`):** `x,p→0` ⇒ `y_node = (z−1)`, `z_in = 1/(z−1)`, `S₁₁ = (2−z)/z`. For `z=3`: **−1/3** (§1a). ✓ Verified through the LOADED path (small nonzero f), not an early return (G-B, X37 R3 lesson).

---

## 4. The canonical objective (Op6) — pulled, not invented

**Universal Operator #6** ([`eigenvalue-target.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/eigenvalue-target.md), claim `clm-gdd70j`; [`operators.md`](../manuscript/ave-kb/common/operators.md) §2 line 46, CANONICAL):
```
λ_min(S†S) → 0        (ground state = one mode perfectly absorbed / reflectionless)
```
Code path `universal_operators.universal_eigenvalue_target(S)` ([`src/ave/core/universal_operators.py:322`](../src/ave/core/universal_operators.py)) — computes the smallest eigenvalue of `S†S`. **How the trefoil applied it** (constants.py:191-206): "S₁₁ minimization (Universal Operator #6, `λ_min(S†S)→0`) enforces `R−r=1/2`, `R·r=1/4`" — the α-chain Golden Torus. X38 applies the SAME operator at the vertex. For the 1×1 reflection block `[S₁₁]`, `universal_eigenvalue_target([S₁₁]) = |S₁₁|²` — the canonical code path reduces to reflection-power minimization, exactly the trefoil usage.

**NAMED AMBIGUITY / LIMITATION (frozen in prereg §4).** Op6's leaf gives the TARGET, not (a) the S-block or (b) the evaluation frequency at a *broadband* vertex. Frozen readings:
- (a) **S-block = the 1×1 `[S₁₁]`** (1-port reflection). The full-3×3 reading is degenerate (`λ_min ≡ 1`, §2) and is reported as a diagnostic only.
- (b) **frequency:** obj-1 evaluates Op6 at the band-top mode `θ = π` (`μ=−3`, the load-bearing ceiling mode, f-independent). The literal deepest-notch reading `min_θ λ_min` is a SEPARATE diagnostic (§5 shows it is pinned at the trivial `θ→0` floor `1/9` for all f — the reflectionless target is UNREACHABLE, so it selects nothing; this is the named limitation, not the objective).

**The three frozen objectives** (obj-1 primary; obj-2/3 robustness comparators):
```
obj-1 (Op6):            J₁(f) = universal_eigenvalue_target([S₁₁(π; f)]) = |S₁₁(π; f)|²
obj-2 (band-integrated): J₂(f) = (1/θ_top)∫₀^{θ_top} |S₁₁(θ; f)|² dθ      (θ_top = X37 connected-band ceiling)
obj-3 (single-freq):     J₃(f) = |S₁₁(π/2; f)|²
f* = argmin_{f∈[0,0.5]} J.
```

---

## 5. The L-match analysis + the argmin (the deliverable)

### 5a. The L-match observation — CONFIRMED as a network fact, REFUTED at the physical vertex

The bare mismatch is a 2:1 impedance step (source `Z₀` → load `Z₀/2`). The **ideal 2-element L-match** that nulls it has
```
Q = √(Z_hi/Z_lo − 1) = √(2 − 1) = 1,
```
with (normalized) series reactance on the LOW side `X_se = Q·Z_lo = 1·½ = ½` and shunt susceptance on the HIGH side `B_sh = Q/Z_hi = 1`. **Verified exactly:** series `+j½` toward the load + shunt `+j1` on the source (port-1) side ⇒ `z_in = 1`, `|S₁₁| = 0`. So the L-match physics is REAL and `Q=1` is CONFIRMED for the ideal 2-element network.

**But the substrate's parasitic geometry is the OPPOSITE orientation:**
- the accumulator (shunt `C`) sits **at the node** — the LOW-impedance (`Z₀/2`) side;
- the throat (series `L`) sits **in the arms**.

This is the impedance step-DOWN L-network (shunt-on-low), which transforms a `Z₀/2` *source* into a `Z₀` *load* — the WRONG direction. It cannot raise the far-arm `Z₀/2` up to `Z₀` seen from port 1. Two independent reasons the matching network is unavailable at the vertex:
1. **Orientation:** the accumulator is physically the extra node *volume* — it is a shunt to ground AT the node (low side) by construction; there is no accumulator on the "port-1 side" to serve as the L-match's high-side shunt.
2. **C₃ᵥ symmetry:** the node is the shared point of all three arms; the shunt is symmetric to all of them. A matching L-network needs an ASYMMETRIC shunt privileging the incident arm — **symmetry-forbidden** at the vertex.

⇒ **Frozen prediction CONFIRMED-as-refutation: the bore does NOT dip `|S₁₁|` below the bare 1/3; it only adds reflection.**

### 5b. Analytic proof (small-θ expansion) — parasitics only INCREASE reflection

Expand `S₁₁` for small `θ` (`x = s_L f θ`, `p = s_C f θ`, both O(θ)), `z = 3`:
```
z_in = ½ + j b + O(θ²),   b = [ (3/2) s_L − (1/4) s_C ] · f · θ,
S₁₁  = (z_in − 1)/(z_in + 1),
|S₁₁|² = (¼ + b²) / (9/4 + b²).
```
`d|S₁₁|²/d(b²) = 2/(9/4 + b²)² > 0` — **`|S₁₁|²` is monotone increasing in `b²`, minimized at `b = 0`** (i.e. `θ = 0` or `f = 0`), where `|S₁₁|² = ¼/(9/4) = 1/9`. For any `f > 0` the reactance `b` is nonzero across the band, so `|S₁₁| > 1/3` everywhere except the trivial `θ→0` point. (The leading coefficient `(3/2)s_L − (1/4)s_C` vanishes only on the measure-zero curve `s_C = 6 s_L`; even there higher-order terms keep `|S₁₁| ≥ 1/3`.) *This expansion matches the exact `S₁₁` to 6 digits at `θ = 10⁻³` across the `s`-grid.*

### 5c. The argmin (all three objectives → f* = 0) — branch (ii)

Because `|S₁₁(θ; f)| ≥ |S₁₁(θ; 0)| = 1/3` with equality only at `θ→0`:
- **obj-1** `J₁(f) = |S₁₁(π; f)|²`: `= 1/9` at `f=0`, `> 1/9` for all `f>0` ⇒ **argmin at f = 0**.
- **obj-2** band-integrated: `= 1/9` at `f=0` (flat `1/3` over the band), `> 1/9` for `f>0` ⇒ **argmin at f = 0**.
- **obj-3** `|S₁₁(π/2; f)|²`: same ⇒ **argmin at f = 0**.

**All three objectives select `f* = 0` for every `(s_L, s_C) ∈ [0.3, 3]²` (driver s-sweep; spread = 0 everywhere).** This is **branch (ii)**: the matched junction is the point junction; the walk ceiling `π√3` is exact (X37 `g(0)`); the bore stays a non-object at this abstraction.

**The Op6 target is UNREACHABLE (the honest core).** The deepest notch any bore presents is `min_θ |S₁₁|² = 1/9` (the `θ→0` floor, shared by ALL f) — the reflectionless target `λ_min → 0` is never reached. The srs vertex is an **intrinsic `1/9`-power back-scatterer** — a structural feature of `z = 3` (a `z = 2` through-junction would match perfectly, `S₁₁ = 0`). Op6 cannot zero the vertex reflection; it can only pick the LEAST-reflecting realizable bore, which is `f = 0`.

### 5d. Self-consistency + comparison marks (frozen reporting)

- `f* = 0 < f_crit ≈ 0.184` (X37): the lumped quasi-static abstraction is self-consistent at its own minimum — **the answer does NOT self-invalidate.**
- Soliton comparison marks (NOT inputs): `1/(2π) ≈ 0.159` (tube radius, constants.py:76), `1` (core-tube thickness, constants.py:189). `f* = 0` matches NEITHER ⇒ branch (i) (identity candidate at `1/(2π)`) does NOT fire; the bore is not the winding-is-the-wire radius. The X37-repaired unasserted observation `1/(2π) ≈ f_crit` (where `ω_vertex ≈ π√3`) is noted but not load-bearing for this negative.

---

## 6. Which branch this points to (the driver decides by the frozen rule)

The physics points to **branch (ii)** (f* = 0, robust across objectives and s). The FROZEN rule (prereg §6) is applied by the driver on the COMPUTED f* and objective-spread, not pre-ordained here. The exact `S₁₁` algebra (§3), the Op6 pull (§4), the L-match refutation (§5a), and the monotone-reflection expansion (§5b) stand regardless of branch.

**What would flip it:** a mechanism outside the leading-order positive-element lumped class (X37 C2 — an evanescent-mode stub / finite-volume resonant shunt branch presenting a NEGATIVE-reactance or resonant bypass) could, in principle, present a matching notch; that is the named model-fidelity follow-on, not modeled here. Within this class the refutation is exact.

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>

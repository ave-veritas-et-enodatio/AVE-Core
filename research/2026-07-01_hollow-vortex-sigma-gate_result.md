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
| Γ (conserved Kelvin circulation, drill n=1) | **n·ℓ_node·M_edge*·c₀ = 0.75–0.80** (mid 0.775) | §2, from winding + cavitation Mach |
| R* = Γ/√σ (prereg headline, Model 1) | **Γ·√(ρ₀ℓ_node/σ)** | §3 |
| **R\*/ℓ_node (headline, drill n=1)** | **1.34 – 1.85 (mid ≈ 1.6)** | §3 |
| — robust band (self-consistent Models 1+3) | **0.59 – 3.58** | §3 |
| **GATE VERDICT** | **SIM-GREENLIT** (O(1), inside [0.1,10]) | §4 |

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

---

## 2. Part 2 — Γ DERIVED (the (2,3) winding's conserved Kelvin circulation)

**substrate-native-check:** CP2 the circulation lives in the Cosserat micro-rotation / swirl
sector (the only engine that hosts circulation is `cavitation_flow`, `engine-capability-map.md:47`);
CP6 Γ is the energize+lock Kelvin invariant (conserved, free-drift 0.044%,
`cavitation-core-probe_result.md:167`), fixed once at genesis — never pumped.

**C-Γ homonym flag (`field-symbol-registry.md:317`).** This is the **Kelvin circulation** Γ =
∮u·dl [dimension L²/T], NOT the Smith reflection coefficient Γ=V_ref/V_inc, and NOT the built
genesis-v5 seed value Γ=80.75 (a specific initial condition, not the topological quantum).

### 2.1 The substrate-native contour and swirl speed (no imports)

Γ = ∮ u·dl around the vortex core. Three substrate-native inputs, all corpus-derived:

1. **The winding integer n** — the (2,3) winding: w_tor=2 toroidal, poloidal |Link|=1
   (`field-symbol-registry.md:149,167`). The number of phase circulations around the core
   contour is n.
2. **The swirl speed — DERIVED, not imported.** A circulating core CROSSES the cavitation floor
   ρ̄_cav=−1/φ at edge Mach **M_edge\* ≈ 0.75–0.80** (`cavitation-core-probe_result.md:39,115`).
   This is the corpus cavitation-ONSET result: to drill the void open, the wall swirl must reach
   v_θ = M_edge*·c₀. So the void-wall swirl is **fixed** at v_θ = M_edge*·c₀ — this is the
   substrate-derived swirl, read off the cavitation threshold, not a free parameter.
3. **The contour length — ropelength-fixed.** The 0₁ unknot has tube radius a = ℓ_node/(2π)
   (ropelength 2π; `de-broglie-standing-wave.md:141`, `constants.py:75-77`). The tube
   circumference is 2πa = **ℓ_node exactly** — and this equals the loop circumference C_loop =
   ℓ_node. sympy confirms the identity 2π·(ℓ_node/2π) = ℓ_node. So both the poloidal (around the
   tube) and toroidal (around the loop) contours have length ℓ_node. Clean substrate identity.

### 2.2 The value

```
Γ = n · (contour length = ℓ_node) · v_θ = n · ℓ_node · (M_edge* · c₀)      [engine units, L²/T]
```

| contour | n | M_edge* range | Γ (engine units) |
|---|---|---|---|
| **drill (azimuthal void-opener, n=1)** | 1 | 0.75–0.80 | **0.75 – 0.80** (mid 0.775) |
| toroidal winding (n=2, upper bracket) | 2 | 0.75–0.80 | 1.50 – 1.60 (mid 1.55) |

**INDICATED Γ (the void OPENER = the azimuthal swirl that drills the core):** the corpus
cavitation-core-probe is a 2-D column whose *single azimuthal circulation* (n=1) at edge Mach
M_edge* is what cavitates the core. So the drill circulation is **Γ = 0.75–0.80** (mid 0.775).
The toroidal n=2 (the charge winding around the big loop) is a *distinct contour* and is carried
as the upper bracket. Both are O(1) engine units — Γ is NOT the 80.75 seed value.

**Γ (frozen for §3): Γ_drill = 0.75–0.80 (mid 0.775) engine units; Γ_tor = 1.55 upper bracket.**

---

## 3. Part 3 — R* = Γ/√σ, and the dimensionless R*/ℓ_node

**substrate-native-check:** incompressible-vacuum FBD — the **bulk-compression restoring term
is DELETED** (prereg §0.1). The void wall sees only the outward swirl push and the inward Laplace
σ/R. CP4: R is the real-space void radius; the balance is real-space (phase-space-coordinate-check:
Γ enters only as its conserved scalar magnitude; no φ²-in-phase-space vs Cartesian mismatch, A46).

### 3.1 Dimensional closure (the pre-registered REQUIRED check)

The prereg (§1) required carrying ρ₀ explicitly. The R⁻³ opener that yields R*=Γ/√σ is a
curved-filament hoop/line-tension pressure `P_open = a·ρ₀·Γ²·ℓ_node/R³` (the extra ℓ_node makes
it dimensionally a pressure). Balanced by the cylindrical Laplace closer `P_close = b·σ/R`:

```
ρ₀·Γ²·ℓ_node/R*³ = σ/R*   ⇒   R*² = ρ₀·Γ²·ℓ_node/σ   ⇒   R* = Γ·√(ρ₀·ℓ_node/σ)
```

In engine units (ρ₀ = 1, ℓ_node = 1) this is exactly the **prereg-frozen headline R* = Γ/√σ**
(C_geo = 1). The ρ₀ and ℓ_node are what make the bare Γ/√σ dimensionally a length — as the
prereg required. ✓

### 3.2 THREE opener models — flag-don't-fix (an honest fork surfaced)

While deriving I found the balance FORM is not unique: the void-opener pressure can be modeled
three ways, giving different R*-vs-Γ laws. Rather than silently pick one, I report all three and
audit each for self-consistency **with the Part-2 Γ derivation** (whose premise is: wall swirl
v_θ is FIXED at M_edge*·c₀).

| model | opener | R* (engine units) | self-consistent w/ Part-2? |
|---|---|---|---|
| **1 (prereg headline)** | filament hoop ρ₀Γ²ℓ_node/R³ | **R* = Γ/√σ** | ✓ yes (fixed swirl, ropelength ℓ_node) |
| 2 | Bernoulli wall, v_θ=Γ/(2πR) | R* = ρ₀Γ²/(8π²σ) | ✗ NO — re-floats swirl as 1/R (contradicts fixed M_edge*) |
| **3 (most substrate-native)** | Bernoulli wall, v_θ=M_edge*c₀ fixed | **R* = 2σ/(ρ₀M_edge*²)** | ✓ yes (swirl fixed at cavitation Mach) |

**Model 2 is REJECTED** for the verdict: it re-floats the wall swirl as Γ/(2πR), which
contradicts the Part-2 premise that v_θ is fixed at the cavitation Mach M_edge*·c₀. Using it
would double-count the swirl. (For the record it gives R*/ℓ_node = 0.02–0.16, mostly sub-band —
but on a self-inconsistent premise, so it does not enter the verdict.)

**The two SELF-CONSISTENT models (1 and 3) are the verdict basis.** Note Model 3 is
n-independent (the opener pressure sees only the wall swirl speed, not the winding count) — a
distinct physical statement, carried honestly.

### 3.3 The computed R*/ℓ_node (sympy)

**Model 1 (prereg headline, R* = Γ/√σ):**

| Γ | σ = 0.18712 (K=2G) | σ = 0.31187 (M) |
|---|---|---|
| drill n=1 (0.775) | **1.79** | **1.39** |
| toroidal n=2 (1.55) | 3.58 | 2.78 |

**Model 3 (R* = 2σ/(ρ₀M_edge*²)):**

| M_edge* | σ = 0.18712 (K=2G) | σ = 0.31187 (M) |
|---|---|---|
| 0.75 | 0.67 | 1.11 |
| 0.775 | 0.62 | 1.04 |
| 0.80 | 0.58 | 0.97 |

**Consolidated self-consistent band (Models 1 + 3, all σ and Γ choices):**

```
R*/ℓ_node ∈ [0.59, 3.58]        — ENTIRELY inside the frozen [0.1, 10] band.
```

**Headline (prereg-frozen Model 1, drill n=1 azimuthal opener):**

```
R*/ℓ_node = 1.34 – 1.85   (midpoint ≈ 1.6)          [O(1) — squarely electron-scale]
```

---

## 4. THE GATE VERDICT

Against the FROZEN band (prereg §4): `R*/ℓ_node ∈ [0.1, 10]` → SIM-GREENLIT; else DEAD-ON-PAPER.

- Headline (Model 1, drill n=1): **R*/ℓ_node = 1.34–1.85** → INSIDE [0.1, 10].
- Robust self-consistent band (Models 1+3, all σ/Γ/M choices): **[0.59, 3.58]** → INSIDE [0.1, 10].

### ➤ VERDICT: **SIM-GREENLIT.**

The hollow vortex binds at **R\* ≈ 1.6 ℓ_node** — an O(1) multiple of the reduced Compton
wavelength, i.e. **electron-scale**. This is NOT the sub-lattice R* that killed the co-compress
sim (PR #443): R* sits at ~1.6 ℓ_node, comfortably resolvable on any lattice with dx < ℓ_node.
A hollow-vortex dynamical-stability sim is greenlit, seeded at R ≈ 1.6 ℓ_node with the void
interior at ρ̄_cav = −1/φ and wall swirl at M_edge* ≈ 0.775·c₀.

**What the ★ guard means we did NOT claim.** We did NOT report "it binds" as the result (that is
the near-tautology / PR#443 trap). The result is the DIMENSIONLESS coefficient R*/ℓ_node ≈ 1.6,
which is what discriminates viable-electron-scale from DEAD. It landed O(1) — that is the content.

### 4.1 Why this is a real (non-trivial) pass, not the tautology

The tautology guarantees a *stable crossing exists* for any σ,Γ>0. It does NOT guarantee the
crossing lands near ℓ_node. It landed near ℓ_node because the two O(1) engine-native quantities
that set the scale — Γ ≈ 0.775 (the cavitation-Mach swirl on the ropelength contour) and √σ ≈
0.43 (the golden-ratio/√6 interface tension) — are BOTH O(1) in ℓ_node units, and their ratio
is O(1). Had either been O(10±) off, R*/ℓ_node would have failed the band. The pass is that the
substrate's own cavitation-onset swirl and its own interface tension conspire to O(1) — a
genuine (if consistency-class) coincidence, not a structural inevitability.

---

## 5. Class, solidity, scope

### 5.1 consistency-vs-emergence tag (frozen at prereg): **Class-C (consistency)**

Per prereg §3, even on PASS this is **Class-C consistency**, NOT a chord:

- **FORM (substrate content):** the hollow-vortex open/close mechanism — an incompressible-melt
  void held open by the (2,3) cavitation swirl and closed by the void↔vacuum interface tension —
  is a genuine substrate-derived structure. The balance law and the σ=3√6/10−√30/10 identity are
  earned.
- **SCALE (rides imports):** R*/ℓ_node is dimensionless, but ℓ_node itself = ℏ/(m_e c) is
  CODATA-derived (through m_e). The O(1) landing is a **consistency check** that the mechanism is
  self-consistent at electron scale — it is NOT an independent prediction of the electron scale,
  and NOT an AVE-distinct chord. We do NOT headline it as emergence.
- Per the corpus meta-finding (AVE forces FORMS, imports VALUES): this is another FORM-derived /
  SCALE-consistency instance. The chord, if any, lives in a FORWARD prediction the greenlit sim
  might expose (e.g. an R*-vs-drive law), not in this O(1) coefficient.

### 5.2 Honest solidity

- σ: **CANDIDATE-class** value (tanh-CH gradient scaling across a non-double-well EOS; O(1)
  prefactor c_σ=1/3; K-vs-M modulus ~1.7× spread). The FORM and the interface IDENTITY (σ_cavity
  = σ_bulk-step) are solid; the absolute value carries the #190 ceiling.
- Γ: **CANDIDATE-class** value. The winding integer (n) and ropelength contour (ℓ_node) are
  solid; the swirl speed rides the corpus M_edge*≈0.75–0.80 cavitation-onset result (itself a
  probe result with a ~7% range and a stabilizer-bias caveat, `cavitation-core-probe_result.md`).
- balance FORM: an honest FORK (three opener models, §3.2). Two are self-consistent with Part-2;
  they bracket R*/ℓ_node ∈ [0.59, 3.58]. The verdict is ROBUST across this fork (all inside the
  band), which is why the fork does not weaken the SIM-GREENLIT call — but it IS the first thing
  the greenlit sim should resolve (which opener law the dynamics actually realize).
- Overall: **the VERDICT (O(1), sim-greenlit) is solid** (robust across the self-consistent fork
  and the σ/Γ ranges); the **specific R\* number (~1.6 ℓ_node) is CANDIDATE-class** (rides the
  σ, Γ, and opener-law ranges).

### 5.3 Findings surfaced (flag-don't-fix), for the auditor/Grant

1. **σ interface IDENTITY** (§1.4): the independently-derived void↔vacuum σ EQUALS the existing
   bulk-density-step σ ≈ 0.187 (exact: 3√6/10−√30/10). This is a genuine identity (same Δρ̄=1/φ,
   ℓ_c=√6, K=2G), surfaced as a finding — not a plug-in.
2. **Opener-law FORK** (§3.2): three physical models for the void-opener pressure give different
   R*-vs-Γ laws; Model 2 is self-inconsistent with the fixed-Mach Γ and is rejected; Models 1 & 3
   both land O(1). The greenlit sim should resolve which the dynamics realize. Surfaced, not
   silently collapsed.
3. **Model 3 is n-independent** (§3.2): the most substrate-native opener (fixed-Mach Bernoulli
   wall) does not reference the winding integer — a distinct physical statement worth noting for
   the sim design.

---

## 6. Scope / what this does NOT establish

- **NOT a sim.** This is analytic paper-gate only. Dynamical stability at R*≈1.6 ℓ_node is the
  greenlit next step, not established here.
- **NOT an emergence claim / NOT a chord.** Class-C consistency (§5.1); the O(1) coefficient
  rides imported ℓ_node.
- **NOT a promotion.** research/ only; no KB/manuscript edits. Any canonization is a separate
  session after independent audit (per lane discipline: the auditor lands manuscript entries).
- **Does NOT resolve** the stiffening-vs-softening bubble-identity firewall
  (`cavitation_flow.py:28`) — this gate uses the softening cavitation void (correct for a hollow
  vortex); the firewall to the stiffening V-breather is untouched and remains open.

---

## 7. Reproducibility

Symbolic derivations (sympy 1.14.0), engine-native units (c₀=1, ρ₀=1, ℓ_node=1):
- σ: `σ = (1/3)·K·ℓ_c·(Δρ̄)²`, c_σ=1/3 derived by tanh-kink integration; value 3√6/10−√30/10.
- Γ: `Γ = n·ℓ_node·M_edge*·c₀`; ropelength identity 2π·(ℓ_node/2π)=ℓ_node verified.
- R*: Model 1 `Γ/√σ`, Model 3 `2σ/(ρ₀M²)`; self-consistency audit vs fixed-Mach Γ.
- All three scratch scripts reproduce the tables above (values in §1.3, §2.2, §3.3).
- `make verify` PASS.

**BOTTOM LINE:** σ = 3√6/10−√30/10 = 0.18712 (= 0.187, interface identity, derived not plugged);
Γ = 0.775 engine units (drill n=1, cavitation-Mach swirl on ropelength contour); R*/ℓ_node ≈ 1.6
(robust band 0.59–3.58, all inside [0.1,10]). **VERDICT: SIM-GREENLIT.** Class-C consistency.

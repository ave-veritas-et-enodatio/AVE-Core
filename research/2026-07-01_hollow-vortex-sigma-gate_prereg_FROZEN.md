# FROZEN PREREG — the σ-gate: is the electron a viable HOLLOW VORTEX?

**Date:** 2026-07-01
**Lane:** implementer (analysis / derivation pass — NO simulation)
**Branch:** `analysis/hollow-vortex-sigma-gate` (off main `a93b8692`)
**Disciplines fired:** `ave-prereg`, `ave-canonical-source`, `consistency-vs-emergence`,
`substrate-native-check`, `phase-space-coordinate-check`
**Status at freeze:** predictions + PASS/FAIL band locked BEFORE any σ, Γ, or R* number is computed.

> **SHA-PIN.** This file is frozen at commit time. Any change to the balance law, the
> PASS/FAIL band, or the class-tag after the σ/Γ/R* numbers are known is a Rule-16
> violation and must be a NEW prereg with its own version, not an edit here.

---

## 0. The physical frame (Grant, 2026-07-01) — NEW

Treating the vacuum's melted/liquid state as **INCOMPRESSIBLE**, the electron is **NOT a
compression soliton** — it is a **HOLLOW VORTEX**:

- The (2,3) Cosserat circulation drills a **CAVITY (void)** at its core — cavitation, the
  canonical `ρ̄_cav = −1/φ` tensile floor (`src/ave/core/cavitation_flow.py:64`).
- The **circulation holds the void OPEN** (a centrifugal / hoop outward pressure that scales
  steeply with 1/R).
- The **surface tension σ of the void↔vacuum boundary holds it CLOSED** (a Laplace inward
  pressure ∝ 1/R).
- Force balance ⇒ a stable equilibrium radius **R\***.

### 0.1 The incompressible-vacuum FBD (substrate-native-check, CP2 + CP10)

Incompressibility is the load-bearing new premise. Under it, the **bulk-compression restoring
term is DELETED** from the free-body diagram: the melted substrate does not store energy in
volumetric compression (K-channel PE is not the container). What remains on the void boundary:

| term | direction | R-scaling | substrate origin |
|---|---|---|---|
| circulation / hoop (opener) | outward | steep (≈ R⁻³ pressure) | (2,3) Cosserat swirl kinetic store |
| surface tension (closer) | inward | shallow (R⁻¹ Laplace) | void↔vacuum interface energy σ |

This is a Cosserat-swirl vs dilatation-void-interface FBD, NOT a Cartesian gradient-descent
energy basin (substrate-native-check CP1/CP10: dynamical reactive balance, no minimization
narrative; CP4: the balance is stated in the real-space radial coordinate of the void wall).

---

## ★ THE GUARD THAT MAKES THIS A REAL TEST (do NOT skip)

The STRUCTURAL bind is **GUARANTEED**: an inward pressure ∝ R⁻¹ vs an outward pressure ∝ R⁻³
gives a stable well for ANY σ, Γ > 0 (the steeper opener wins at small R, the shallower closer
wins at large R → exactly one crossing → stable). So **"it binds" is a NEAR-TAUTOLOGY** — this
is precisely the trap that sank the prior co-compress sim (PR #443).

**We do NOT report "it binds" as the result.** The result is the **VALUE R\*** and specifically
the **DIMENSIONLESS ratio R\*/ℓ_node**. The dimensionless coefficient IS the discriminating content.

---

## 1. The balance law (pre-registered FORM — frozen)

Force / pressure balance on the void wall of radius R, incompressible medium:

- Opener (circulation, hollow-vortex hoop): outward pressure `P_open(R) = a · Γ² / R³`
  for some O(1) geometric constant `a`, with Γ the conserved circulation `∮ u·dl`
  (dimensions [velocity·length] = [L²/T]).
- Closer (surface tension, Laplace on a curved void): inward pressure `P_close(R) = b · σ / R`
  for some O(1) geometric constant `b`, σ the interface tension (dimensions
  [energy/area] = [M/T²] → in engine ρ₀c₀²ℓ_node units, dimension [velocity²·length]/[length²]·… see §3).

Balance `P_open(R*) = P_close(R*)`:

```
a·Γ²/R*³ = b·σ/R*     ⇒     R*² = (a/b)·Γ²/σ     ⇒     R* = √(a/b) · Γ/√σ
```

**Pre-registered balance form (frozen):**

```
                    R* = C_geo · Γ / √σ            (C_geo = √(a/b), an O(1) geometric prefactor)
```

The mission task states the balance as **R\* = Γ/√σ** (i.e. `C_geo` absorbed to 1). We carry
`C_geo` explicitly through the derivation and report R* both with `C_geo=1` (the task headline)
and with the honestly-derived `C_geo`. **The verdict band (§4) is wide enough (decade) that any
O(1) `C_geo` does not flip it** — this is stated now, before the numbers, so the band choice is
not retrofit to `C_geo`.

**Dimensional self-consistency (frozen, must hold):** with `[Γ]=L²/T` and `[σ]` such that
`P=σ/R` is a pressure `[M/(L T²)]`, we need `[σ]=M/T²` (force/length = energy/area). Then
`[Γ²/σ] = (L⁴/T²)/(M/T²) = L⁴/M`. For `R*=Γ/√σ` to be a LENGTH, we require the medium density
ρ₀ to close the units: `R* = C_geo·Γ/√(σ/ρ₀)` with `[σ/ρ₀]=L³/T²`, giving `[Γ²/(σ/ρ₀)]=L`.
**In engine-native units ρ₀ ≡ 1, so `√σ` and `√(σ/ρ₀)` coincide numerically** — but the
derivation (§3) must carry ρ₀ explicitly and state that the engine ρ₀=1 is what makes the
task's bare `Γ/√σ` dimensionally a length. This is pre-registered as a REQUIRED check, not an
afterthought.

---

## 2. The three derivations (pre-committed method — NO numbers yet)

### Part 1 — σ (the void↔vacuum interface surface tension), FROM SCRATCH

**Grant's explicit instruction:** derive the cavity-boundary σ **independently** from the
substrate interface energy — the energy per unit area of the boundary between the cavitated
void (`ρ̄_cav = −1/φ`, tensile) and the surrounding incompressible vacuum. **NO ASSUMPTION that
it equals the existing σ ≈ 0.187.** The existing 0.187 derivation
(`research/2026-06-11_bubble-physics-completion.md` §1; #190 thread), the ρ̄_cav cavitation
thread (`cavitation_flow.py`), and the incompressible-vacuum treatment are **REFERENCE, not
the answer**.

- **Method (pre-committed):** square-gradient (Cahn-Hilliard / Korteweg) interface energy
  `σ = ∫[Δf₀ + ½λ_grad(dρ̄/dx)²]dx` across the void↔vacuum diffuse interface, with the
  interface width set by the Cosserat couple-stress length `ℓ_c = √6·ℓ_node`
  (`constants.py:298-302`) and the density jump Δρ̄ = 1/φ (0 → ρ̄_cav).
- **PRE-COMMITTED FINDING RULE (the honesty hinge):** if the independently-derived cavity-σ
  **equals 0.187**, that is a FINDING — the two interfaces coincide — to be REPORTED as such.
  If it **differs**, that is ALSO a finding, reported with the numeric gap. **We do NOT plug in
  0.187.** The whole gate's honesty rides on this.
- State σ symbolically AND its value in engine units (ρ₀c₀²·ℓ_node), with the interface
  identity explicit.

### Part 2 — Γ (the (2,3) winding's conserved circulation)

Substrate-native, from the winding integer.

- **Method (pre-committed):** Γ = ∮ u·dl around the vortex core. Substrate-native inputs:
  the (2,3) winding integer (Link = −1 topological quantum; `w_tor=2`, poloidal |Link|=1,
  `crystal-engine` / field-symbol-registry), the loop geometry (0₁ unknot, circumference
  C_loop = ℓ_node, tube radius ℓ_node/(2π), ropelength 2π; `de-broglie-standing-wave.md:141`,
  `constants.py:75-77`), and the substrate-derived swirl-speed **at the cavitation threshold**
  — the edge Mach `M_edge* ≈ 0.75–0.8` at which a circulating core CROSSES `ρ̄_cav=−1/φ`
  (`research/2026-06-10_cavitation-core-probe_result.md:39,115`). This M_edge* is the
  substrate-DERIVED swirl velocity (v_θ = M_edge*·c₀) required to open the void — it is NOT
  imported, it is the corpus cavitation-onset result.
- Carry Γ symbolically; report its engine-unit value and the winding-integer / M_edge*
  provenance explicitly. Flag the C-Γ homonym (`field-symbol-registry.md:317`): this is the
  **Kelvin circulation** Γ, NOT the Smith reflection Γ, and NOT the built genesis-v5 value
  Γ=80.75 (a specific seed, not the topological quantum).

### Part 3 — R* = C_geo·Γ/√σ, then R*/ℓ_node (sympy)

- Compute R* analytically (sympy symbolic + numeric).
- Compute the dimensionless **R\*/ℓ_node** (ℓ_node ≡ ℏ/m_e c ≈ 3.86e-13 m; engine ℓ_node = 1).
- Report with C_geo = 1 (task headline) AND with the derived C_geo.

---

## 3. Coordinate + class discipline (frozen)

- **phase-space-coordinate-check:** the balance is a REAL-SPACE radial force balance on the
  void wall (the void radius R is a real-space length). The (2,3) winding lives in phase space
  `(V_inc,V_ref)`, but Γ enters only as its conserved scalar magnitude (a Kelvin invariant),
  and σ, R are real-space. So the balance and the R*/ℓ_node ratio are stated in matching
  (real-space length) coordinates. No φ²-in-phase-space vs Cartesian-lattice mismatch (A46).
- **consistency-vs-emergence (frozen tag):** **Class-C (consistency)** even on PASS. The FORM
  (the hollow-vortex open/close mechanism, the balance law) is the substrate content; the R*
  SCALE rides imported `ℓ_node = ℏ/m_e c` (CODATA-derived through m_e) and the α/φ geometry.
  The O(1) coefficient R*/ℓ_node is a **consistency check**, NOT an AVE-distinct chord. On PASS
  we tag it Class-C consistency; we do NOT headline it as emergence.

---

## 4. THE GATE VERDICT — PASS/FAIL band (FROZEN before any number)

Compute **R\*/ℓ_node**. The band:

- **R\*/ℓ_node ∈ [0.1, 10]  (O(1), within one decade either side)**
  → the hollow vortex is a VIABLE electron-scale structure
  → **SIM-GREENLIT** (a hollow-vortex sim to confirm dynamical stability at the now-resolvable
     R*; the sub-lattice R* that killed PR #443 is fixed by construction since R* is checked
     ~ ℓ_node).

- **R\*/ℓ_node > 10  OR  R\*/ℓ_node < 0.1  (wrong scale by more than a decade)**
  → **DEAD ON PAPER** (honest negative, NO sim) → the hollow-vortex frame does not give an
     electron-sized bound state.

**Band rationale (pre-committed):** the electron's characteristic length IS ℓ_node (the reduced
Compton wavelength, the loop circumference). A viable electron-scale hollow vortex must bind at
R* within an O(1) factor of ℓ_node. One decade each side [0.1, 10] is deliberately GENEROUS
(it absorbs the O(1) geometric prefactors C_geo, c_σ, b, the M_edge* range 0.75–0.8, and the
K-vs-M modulus ambiguity in σ) so that PASS is not knife-edge and FAIL is unambiguous. A result
landing ≫10 or ≪0.1 (many decades off) is the honest DEAD outcome and will be reported as such.

**HOLD REAL ODDS this comes out DEAD.** This is the 5th electron-binding attempt. A wrong-scale
R* is a legitimate honest negative (Rule 11). We do NOT rescue-narrate; we do NOT tune σ or Γ or
C_geo to force the ratio into [0.1, 10]. The band is frozen HERE, before the numbers.

---

## 5. Deliverable

`research/2026-07-01_hollow-vortex-sigma-gate_result.md`: the DERIVED σ (+ interface identity +
whether it coincides with 0.187), the DERIVED Γ, the computed R* = C_geo·Γ/√σ, the dimensionless
R*/ℓ_node, and the GATE VERDICT (SIM-GREENLIT vs DEAD-ON-PAPER). Honest solidity, Class-C.
NO sim, NO KB/manuscript edits (research/ only). Symbolic work validated with sympy + `make verify`.

---

## 6. What would make this WRONG (pre-committed failure modes)

- σ silently defaulted to 0.187 instead of independently derived → honesty violation; the
  finding-rule (§2 Part 1) is the guard.
- "It binds" reported as the result → the ★ guard; the tautology trap (PR #443).
- Band widened post-hoc to convert DEAD → PASS → Rule-16 / Rule-11 violation.
- Γ taken as the built genesis-v5 value 80.75 (a seed) rather than the topological quantum →
  C-Γ homonym error (`field-symbol-registry.md:317`).
- Real-space R compared against a phase-space φ² winding target → A46 coordinate mismatch
  (guarded in §3).
- Incompressibility premise forgotten and a K-compression restoring term smuggled back into the
  FBD → §0.1 guard (the bulk term is DELETED).

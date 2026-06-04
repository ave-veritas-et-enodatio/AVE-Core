[↑ Research](index.md)

# Phasor↔real-space area bijection — Class-B→Class-2 lift candidate (PREREG, FROZEN)

**Status**: PREREG FROZEN (result + verdict appended after the derivation). NO driver code yet.
**Question (Q-EMBED-SEL-1 §7.3 workstream)**: can the phasor-enclosed-area = Nyquist-cell-area identification — the one named substrate-mechanism step that holds α⁻¹ = 4π³+π²+π at **Class B** — be **derived** from K4 + Cosserat primitives (Ax 1 + Ax 2/TKI + Ax 4 + the bond LC tank), lifting it to **Class 2**? Or is it an irreducible normalization?
**Canonical anchors**: [`ch8-alpha-golden-torus.md:11`](../manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md) (the Class-B caveat), [`2026-05-31_Q-EMBED-SEL-1_step_c_result.md`](2026-05-31_Q-EMBED-SEL-1_step_c_result.md) §2.3 + §7.3 (the named identification + the lift workstream), `constants.py` (V_SNAP, L_NODE, Z0, ξ_topo, ALPHA_COLD).
**Predecessors on the same object (all closed/hardened this session)**: the ¼ *selection* question (Class B, hardened — `2026-06-04_alpha-quarter-adversarial-rechallenge.md`); the δ_strain *residual* (definitional, not an observable). This bijection is the **one remaining lift-path** the flatness did not already close.

---

## §0 — The load-bearing finding (what the bijection actually rests on)

Per Q-EMBED-SEL-1 §2.3(ii) **verbatim**, the identification equates a phasor **reactive energy** (∮V dI around the (V_inc,V_ref) ellipse, semi-axes R,r) to a real-space **area** (Nyquist cell cross-section π(d/2)²) —

> *"the enclosed area πR·r in ℓ_node² units equals the bond's per-Compton-cycle reactive energy (up to the **unit-system overall constant that the lattice-natural-units choice sets to unity**)."*

The bridge between [reactive energy] and [length²] is a **dimensionful constant K**, set to 1 by the lattice-natural-units choice (Z₀=1, ℓ_node=1, V_snap→1/√α). **The entire Class-B↔Class-2 question is the status of K.**

- **Class 2 (lift)**: the canonical substrate constants {V_SNAP, ℓ_node, Z₀, e, ξ_topo, C_bond, L_bond, m_e c²} **force** K to its ¼-compatible value as a derived dimensionless identity — no free normalization, no α fed in.
- **Class B (confirmed)**: K is a free dimensionful ratio the natural-unit choice merely *sets* to 1, **or** K=1 holds only because α was already in V_snap (circular).

**TKI clarification (the "TKI?" check):** Ax 2/TKI is [Q]≡[L] (charge↔length, ξ_topo=e/ℓ_node) — it is *named* in §2.3 but does NOT by itself bridge voltage↔length. The full candidate bridge is **C_bond (V↔Q) ∘ ξ_topo (Q↔L)**. The derivation must build K from that explicit chain, not assert "TKI bridges it."

## §1 — The α-circularity hazard (possibly dispositive — resolve FIRST)

The natural-units cheatsheet sets **V_snap → 1/√α**. If the phasor enclosed area carries V_snap (it is the saturation-onset amplitude), then **α is on the input side**, and "deriving" R·r=¼ ⇒ α⁻¹=4π³+π²+π from a scale containing α is **fit-as-prediction circularity** (`ave-driver-script-honesty`). 

**Guard (HARD, Step 0 of the derivation):** compute K in **physical SI units** from {V_SNAP=m_e c²/e (α-free), ℓ_node=ℏ/m_e c (α-free), Z₀=√(μ₀/ε₀) (α-free), e, C_bond, L_bond}. Track every appearance of α. **If α appears on the input side of K, the lift is impossible and the verdict is Class B (circular).** Only if K is α-free on input AND comes out ¼-compatible is a Class-2 lift live.

> **Pre-registered expectation (anti-tuning, registered BEFORE the compute) — UPDATED 2026-06-04 by Grant's Q2/Q3 reframe:** Q2 verified that **V_yield is the geometric mean of the LATTICE string-tension (F_yield = m_e c²/ℓ_node) and the EM/Coulomb coupling (e²/4πε₀)** — `kinetic-yield-threshold.md` clm-rd9cjm — so **α is the soliton↔lattice coupling, not a free input** (`constants.py:273`). That makes the lift *meaningful and non-trivially-circular*: the target is to **DERIVE that coupling geometrically** (does a transverse-wave phasor filling exactly one lattice cell *force* √α to the golden-torus value?), NOT to substitute it. The HARD honesty line: the existing derivations (kinetic-yield, §2.3) **substitute** α (e²/4πε₀ = αℏc); a Class-2 lift requires deriving the bridge from {Z₀, C_bond, ξ_topo, ℓ_node, m_e, e} **without** substituting α. Outcome is now **genuinely open** — not pre-judged Class B. The discriminator: derive-the-coupling (Class 2) vs substitute-the-coupling (Class B).

## §2 — The derivation (Steps, frozen)

1. **(Step 0 — circularity audit)** Express K in physical SI from α-free canonical constants; locate α. If α is an input → STOP, Outcome B (circular).
2. **(Step 1 — build K from the explicit bridge)** phasor reactive energy U_φ = ∮V dI over the (V_inc,V_ref) ellipse (NOT assuming R·r=¼ — keep R,r symbolic) ; real-space cell area A_cell = π(d/2)², d=ℓ_node. Build K = [the dimensionful factor that makes U_φ and A_cell commensurable] via C_bond (V↔Q) ∘ ξ_topo (Q↔L). 
3. **(Step 2 — forced vs free)** Is K's value fixed by {V_SNAP, ℓ_node, Z₀, e, C_bond, L_bond} with NO residual free normalization? Compute it; check whether setting K=1 is *forced* or *chosen*.
4. **(Step 3 — the bijection)** Only with K resolved: does πR·r = A_cell follow as a derived identity (⇒ R·r=¼ emergent) or does it require imposing K=1 (⇒ R·r=¼ is the named identification)?
5. **(Step 4 — classify)** `consistency-vs-emergence` v1.3: does the work add a NEW K4+Cosserat primitive (the derived bridge), or formalize an existing identification? Class 2 iff a new primitive is genuinely derived.

## §3 — PASS criteria (substrate-derived, registered)

| Bar | Condition | Verdict |
|---|---|---|
| **B1 — non-circular** | K is α-free on input | required for any Class-2 path; fail → **Class B (circular)** |
| **B2 — forced** | K's value fixed by canonical constants, no free normalization | required for Class 2 |
| **B3 — bijection emergent** | πR·r = A_cell follows WITHOUT imposing K=1 or R·r=¼ | **Class 2 lift** if B1∧B2∧B3 |
| **B-fallback** | K is a free normalization OR α-circular | **Class B confirmed** — the last lift-path closes; α⁻¹=4π³+π²+π is a named identification, full stop |

## §4 — Guards

- **ave-driver-script-honesty**: no fit-to-¼; R,r symbolic until the end; no α imported into K.
- **ave-canonical-source**: V_SNAP, L_NODE, Z0, e, ξ_topo, C_bond from `constants.py`; no hardcoded literals.
- **phase-space-coordinate-check**: K is exactly the phasor↔real-space coordinate-bridge; the whole derivation lives at that seam — do not silently equate the two coordinate areas (that equation IS the thing under test).
- **consistency-vs-emergence v1.3**: classify by NEW-primitive test, not by whether the arithmetic matches ¼.
- **No re-litigation of selection**: the dressed-eigenmode flatness (selection, dynamical) is NOT this test (kinematic unit-bridge). Keep them distinct; do not import the flat-landscape result as if it settles the bijection.

## §5 — Surfaced-for-Grant questions (pre-test-physics-check, BEFORE dispatch)

**Q1 (the crux — your gut-check):** the §2.3 bridge is "an overall constant that the lattice-natural-units choice sets to unity." Physically: **is the phasor-voltage scale (V_SNAP) fixed *relative to* the lattice-length scale (ℓ_node) by the substrate — a real, forced [voltage]↔[length] via C_bond∘ξ_topo — or is that scale-ratio a gauge you set?** If forced → the derivation hunts a real Class-2 identity; if gauge → it confirms Class B. Your intuition on whether the bond LC tank's C is independently substrate-fixed (so V↔Q↔L has no slack) is the load-bearing call.

**Q2 — RESOLVED 2026-06-04 (Grant):** V_yield is a JOINT lattice×wave quantity — `kinetic-yield-threshold.md` (clm-rd9cjm): E_k = √(F_yield·e²/4πε₀) = √(LATTICE string-tension · EM/Coulomb coupling) = √α·m_e c². V_SNAP itself is α-free (m_e c²/e); the √α is the **soliton↔lattice coupling** (`constants.py:273`), NOT a circular pass-through. So the lift is **not trivially circular** — the target is to derive that coupling from the cell-filling geometry. Residual guard (HARD): the existing chains *substitute* α (e²/4πε₀ = αℏc); Class 2 requires deriving the bridge WITHOUT substituting α.

**Q3 — RESOLVED 2026-06-04 (Grant: "challenge by EE mapping + definitions"):** EE-native, R,r are **voltage**-phasor semi-axes — `translation-circuit:173`: "the bond's incident/reflected **voltage** waves… E ~ (V_inc+V_ref), B ~ (V_inc−V_ref)/Z." The "R=0.809 ℓ_node" quotes are therefore **POST-BRIDGE** (Z₀ = 376.73 Ω, the canonical EE primitive, does the V↔L work). **Mandate for the derivation:** START from the voltage-phasor (R,r in V-units), DERIVE the ℓ_node expression via the explicit Z₀ ∘ C_bond ∘ ξ_topo bridge. Starting from ℓ_node-unit R,r begs the question and is disallowed.

## §6 — Skills (mapped, per `feedback_skill_selection_planning`)

`ave-prereg` (corpus pull — done, §0 anchors) · `ave-canonical-leaf-pull` (energy-quantum + cross-scale-bridge class: ch8, Q-EMBED-SEL-1 §2.3, l3-electron-soliton-synthesis, theorem-3-1-q-factor, op21) · **`phase-space-coordinate-check`** (the K-bridge IS the coordinate seam) · **`consistency-vs-emergence` v1.3** (NEW-primitive test) · `substrate-native-check` (K4 bond LC tank + ξ_topo) · `ave-ee-first-mapping` (C_bond∘ξ_topo voltage→charge→length) · `ave-canonical-source` · **`ave-driver-script-honesty`** (α-circularity guard) · `ave-discrimination-check` (SM-counterfactual on any Class-2 claim) · `pre-test-physics-check` (Q1–Q3 surfaced above before lock).

## §7 — Pure-AVE-corpus rule

Pure substrate physics throughout. No external-context references.

## §8 — POST-FREEZE COMPLETENESS ADDENDUM (Grant's audit, 2026-06-04)

Grant's two post-freeze checks ("is V_yield a phasor?" + "have we captured all axioms/calibrations/regimes/BCs?") surfaced load-bearing items §0–§6 under-captured. The dispatched implementor's anchors (Q-EMBED-SEL-1 §2.2-2.3) carry these; verified in review.

**(a) V_yield IS a phasor boundary, not a scalar — load-bearing for the Step-0 circularity audit.** Q-EMBED-SEL-1 §2.2: at yield, S(A)→0, Z_local→0, **Γ→−1 TIR forms**, and *"the TIR boundary surface is the **locus in (V_inc, V_ref) phasor coordinates** at which the first-saturating channel hits yield."* Under Meissner-asymmetric bias it is an **ELLIPSE** — R along the slower-saturating V_inc, r along the faster-saturating V_ref. So **the (R,r) electron ellipse IS the yield boundary**; the scalar V_yield = √α·V_snap is its equivalent-isotropic radius √(R·r). **CONSEQUENCE: R·r carries V_yield² = α·V_snap² — it is NOT α-free.** Step 0 must resolve whether that α (the soliton↔lattice coupling in V_yield) is FORCED by the cell-filling (derived → Class 2) or inherited (→ Class B). This sharpens the crux.

**(b) Ax 3 (Minimum Reflection / Γ=−1 TIR) was under-listed.** §0 cited Ax 1+2+4; the Γ=−1 TIR wall **is** the yield boundary where R,r live (§2.2). Full axiom set: {**Ax 1** Nyquist cell · **Ax 2** TKI bridge · **Ax 3** Γ=−1 TIR yield-locus · **Ax 4** saturation kernel}.

**(c) Chirality calibration χ_(2,3) = 1.2α** — the Meissner-asymmetry driver splitting R≠r (a SECOND α-carrier, in the R/r *aspect*; R·r the *product* is the bijection's invariant per §2.3, since the asymmetry redistributes between channels without changing the product). Must be in the calibration set.

**(d) Four-regime placement** (`four-regimes.md`): the bijection lives at saturation onset = the **Regime III/IV (yield) boundary**. Boundary-condition set: {Γ=−1 TIR · Nyquist λ_min=2ℓ_node · self-avoidance d=diameter · Meissner-asymmetry χ_(2,3)}.

**Net:** (a)+(c) make the α-circularity audit STRICTER — R·r carries α via V_yield AND R/r via χ_(2,3); the lift requires *deriving* those couplings from cell-filling, not inheriting them. Honest expectation tightens toward Class B unless the cell-filling geometry independently forces V_yield's √α.

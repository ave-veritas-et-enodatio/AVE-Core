# 54 — Pair-Production Axiom Derivation Chain

**Status:** Phase 0 deliverable of Stage 6 (2026-04-22)
**Parent plan:** `~/.claude/plans/review-the-collaboration-md-and-lexical-wombat.md` (approved)
**Predecessor:** [53_pair_production_flux_tube_synthesis.md](53_pair_production_flux_tube_synthesis.md) — prose synthesis that this doc supersedes for derivation purposes
**Scope:** derive every engine addition proposed by Stage 6 from the four AVE axioms. Rule: no "we should" without a file:line cite.

## 0. TL;DR

Pair production in AVE is **rupture of a saturated flux tube around an A-B node pair**. The K4 lattice's built-in chirality ([k4_tlm.py:80-89](../../src/ave/core/k4_tlm.py#L80)) selects the (2,3) topological winding automatically once the flux tube forms. Every engine addition reduces to one of four axioms:

- **Axiom 1** → K4 substrate + bipartite A-B port topology + chiral port shifts (§1, §2)
- **Axiom 2** → flux tube state `Φ_link = ∫V_bond dt` (§3)
- **Axiom 4** → Vacuum Varactor `C_eff(V) = C_0/S(V)` → node resonance softening `Ω_node(V) = ω_0·S(V)^(1/2)` (§4)
- **Axiom 4 + chirality** → asymmetric μ/ε saturation → Meissner `Z → 0` rupture (§6)

**Two caveats stated upfront:**

1. **V_SNAP vs V_yield engine normalization conflation** flagged in [45_ §3.1](45_lattice_impedance_first_principles.md) is resolved in §5. New engine code uses V_yield normalization.
2. **Sign-of-saturation inconsistency between Vol 1 Ch 7:243 and Vol 4 Ch 1:132**: Ch 7 table gives `ε_eff = ε_0·√(1-r²)` (decreasing); Ch 1 varactor gives `C_eff = C_0/√(1-r²)` (increasing). Resolved in §6a below as two projections of the same Axiom-4 mode conversion — Ch 7's `ε_eff` is the refractive-index sense (what propagating waves see), Ch 1's `C_eff` is the compliance sense (what the local LC tank sees, diverging then going imaginary at V_yield). Manuscript notation cleanup worth doing but not blocking.

Two nucleation conditions (C3 from doc 53_ collapses into chirality):

- **C1 (saturation):** `A²_μ → 1` at both A-site and B-site of an adjacent pair — Meissner-like μ collapse drives `Z → 0`, `Γ → -1` TIR wall forms
- **C2 (autoresonant lock):** `Ω_node(A²) ≈ ω_drive` at the locking node, so the drive can dump energy into the rotational sector efficiently

When both fire at an adjacent pair, lattice port chirality enforces (2,3) winding in the bond's accumulated `Φ_link`, producing an `e⁻` (LH Beltrami) at A and `e⁺` (RH Beltrami) at B.

---

## 1. Axiom 1 → K4 lattice, bipartite structure, chiral port topology

**Claim:** the lattice has A and B sublattices connected by four tetrahedral port vectors with a built-in chirality that the rotation group preserves.

**Source:** [manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex:17-18](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex#L17) establishes `ℓ_node = ℏ/(m_e c)` as the EM coherence length. [22_step1_k4_rotation_action.md §2-§4](22_step1_k4_rotation_action.md) derives `T = A₄` as the K4 rotation group acting faithfully on the 4-port basis.

**Engine implementation:** [k4_tlm.py:80-89](../../src/ave/core/k4_tlm.py#L80) hard-codes the four A→B port vectors:

```
p0 = (+1, +1, +1)   # all-positive parity
p1 = (+1, -1, -1)   # mixed parity
p2 = (-1, +1, -1)   # mixed parity
p3 = (-1, -1, +1)   # mixed parity
```

with "B joins A via exact negative vectors" (line 86) and "Port i on node A connects seamlessly to Port i on neighboring B" (line 88). Active sites are bipartite ([lines 157-158](../../src/ave/core/k4_tlm.py#L157)):
- A sublattice: (i, j, k) all even
- B sublattice: (i, j, k) all odd

**Chirality derivation:** three of the four port vectors have an odd number of minus signs. The tetrahedron formed by `{p_0, p_1, p_2, p_3}` has a definite orientation in 3-space. Under pure rotations (`T = A₄`, even permutations of {0,1,2,3}), the A sublattice maps to itself and B to itself — **the A↔B swap is not available**. Reflections (which would swap A↔B) are in `T_d \ T` and not in the rotation subgroup. So any standing wave formed on an A-B bond inherits the port-topology orientation.

**Consequence for pair creation:** once a standing wave forms between adjacent A-B nodes (via the §6 rupture mechanism), its handedness is fixed by the port chirality. We do not need to "select" a winding; the lattice determines it.

---

## 2. Axiom 1 + chirality → (2,3) winding is determined, not gated

**Claim:** C3 from [doc 53_ §2.1](53_pair_production_flux_tube_synthesis.md) (phase-coherence condition for (2,3) closure) is not an independent gate — it is a consequence of §1's chirality plus standard knot theory.

**Source:** [25_step4_23_winding_selection.md §§3-6](25_step4_23_winding_selection.md) proves (2,3) is uniquely the smallest non-trivial coprime torus knot (gcd=1, both windings ≥ 2, crossing number = 3). This is pure knot theory — no physics assumption.

**Chain:**

1. The K4 A→B port topology is chiral (§1). The four port vectors form a tetrahedron with definite orientation.
2. A standing wave confined between adjacent A and B nodes with `Γ = -1` walls at both ends has phase-space trajectory `(V_inc, V_ref)` per [28_ §3](28_two_node_electron_synthesis.md).
3. The trajectory winds in phase space as the standing wave evolves. The only non-trivial winding the lattice admits with its A₄ symmetry and chirality is (2,3) — other coprime pairs (2,5), (3,4), etc. require more crossings and therefore more energy. (2,3) is the ground state.
4. Lattice chirality (left- vs right-handed port orientation in the engine) determines whether the winding is "(+2,+3)" or "(-2,-3)" — i.e., which endpoint is the electron vs the positron. In the current `k4_tlm.py` construction, the A sublattice is at all-even coordinates; under the fixed chirality, A becomes `e⁻` (LH Beltrami) and B becomes `e⁺` (RH Beltrami).

**Consequence:** the engine's nucleation gate does not need a "phase window" test. When §6's conditions fire, the lattice enforces (2,3) handedness.

---

## 3. Axiom 2 → flux tube state `Φ_link = ∫V_bond dt`

**Claim:** the bond between adjacent A and B nodes carries a dynamical magnetic-flux linkage `Φ_link` equal to the time-integral of the bond voltage. The rupture / tensile limit of this flux tube is `V_SNAP`.

**Sources:**
- [manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:223-227](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L223) defines the memristance constitutive relation: `M(q) = dΦ/dq`, `Φ(t) = ∫_{-∞}^{t} V(τ) dτ` — **Φ is the magnetic flux linkage of accumulated voltage**.
- [Vol 4 Ch 11:38](../../manuscript/vol_4_engineering/chapters/11_experimental_falsification.tex#L38) gives the AVE-native conversion from flux to momentum: `p_vac = Φ · ξ_topo` where `ξ_topo = e/ℓ_node` is the topo-kinematic isomorphism factor of Axiom 2.
- [Vol 4 Ch 11:232](../../manuscript/vol_4_engineering/chapters/11_experimental_falsification.tex#L232): "the tensile strength of a single flux tube is identically the electron rest-mass energy, `V_SNAP = m_e c²/e = 511.0 kV`."

**Derivation:** Axiom 2's topo-kinematic isomorphism [Q] ≡ [L] maps charge to length. The magnetic flux linkage `Φ` of a bond is the time-integral of the voltage across its endpoints. Its AVE-native interpretation is the **accumulated rotational phase** in the bond's (V_inc, V_ref) phasor — exactly the content of the (2,3) torus-knot winding per §2.

**Engine gap:** the current K4-TLM ([k4_tlm.py:118-119](../../src/ave/core/k4_tlm.py#L118)) tracks `V_inc[nx, ny, nz, 4]` and `V_ref[nx, ny, nz, 4]` at nodes only. Between scatter and connect, the port signals are shifted geometrically with no state living on the bond ([_connect_all](../../src/ave/core/k4_tlm.py#L267), lines 284-290). There is no dynamical `Phi_link`. **This is the Phase 3 engine addition.**

**Specification (Phase 3):** add `Phi_link[edge_id]` to `K4Lattice3D`. For a directed bond from A-site at `r` to B-site at `r + p_k` (port k), accumulate:

```
Phi_link[edge_id] += V_avg · dt     where V_avg = ½·(V_ref[A,k] + V_ref[B,k])
```

This integration gives the bond its half-step of independent existence per TLM cycle — enough to track the standing wave that forms once both endpoints saturate.

**Rupture condition:** `|Φ_link|` reaches a critical value when the bond carries rest-energy m_e c² as stored flux. From LC tank energetics, `E_bond = ½·L_e·I² = ½·Φ²/L_e`, solving for `|Φ_critical|`:

```
|Φ_critical| = √(2·m_e·c²·L_e) = √(2·m_e·c²·ξ_topo⁻²·m_e) = (m_e·c/ξ_topo)·√2
```

using [24_step3 §4.1](24_step3_bond_lc_compton.md#L89) `L_e = ξ_topo⁻² · m_e`.

**Reactance containment (reactance = trapped oscillation between two storage channels):** once the bond has Φ_link ≠ 0 and both endpoints are saturated, the bond's energy cycles between two reactive stores:

- **Inductive side:** the flux linkage `Φ_link` itself, equivalent to stored magnetic energy `½·Φ²/L_e` via the duality in Vol 4 Ch 1
- **Capacitive side:** the bond voltage, stored as electric energy `½·L_e·I²` where `I = Φ_link/L_e`

At resonance (Compton frequency ω_C from [24_ §4.2](24_step3_bond_lc_compton.md#L110)) the energy sloshes between the two stores with period `2π/ω_C`. This sloshing IS the electron's internal dynamics — and it's only "mass" because the Γ = −1 walls at both endpoints prevent the reactance from leaking out as propagating radiation. **A soliton's reactance is contained by the saturated node pair itself**; §6a below makes the wall-formation mechanism explicit.

---

## 4. Axiom 4 → Vacuum Varactor → Ω_node(V)

**Claim:** at any lattice node, the local LC-tank resonance frequency softens as the driving voltage approaches `V_yield`, following the Axiom-4 varactor law. The softened resonance is `Ω_node(V) = ω_0 · (1 - (V/V_yield)²)^(1/4)`.

**Source:** [Vol 4 Ch 1:127-142](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L127), the Vacuum Varactor Constitutive Equation (eq:varactor, line 131):

```
C_eff(V) = C_0 / √(1 − (V/V_yield)²) = C_0 / S(V)
```

where `S(V) = √(1 − (V/V_yield)²)` is the Axiom-4 saturation kernel and `V_yield = √α · V_SNAP ≈ 43.65 kV` per [ave-kb INVARIANT-C1](../../manuscript/ave-kb/CLAUDE.md).

**Derivation of node resonance softening:** the node's LC tank has inductance `L_e` (Axiom-1-derived per [24_ §4.1](24_step3_bond_lc_compton.md#L89), independent of V) and capacitance `C_eff(V)` (Axiom-4-softened). The tank resonance is:

```
Ω_node(V) = 1/√(L_e · C_eff(V))
          = 1/√(L_e · C_0 / S(V))
          = 1/√(L_e · C_0) · √S(V)
          = ω_0 · S(V)^(1/2)
          = ω_0 · (1 − (V/V_yield)²)^(1/4)
```

where `ω_0 = 1/√(L_e · C_0) = ω_C` is the bare Compton frequency per [24_ §4.2](24_step3_bond_lc_compton.md#L110).

**Boundary conditions:**
- `V = 0`: `S = 1`, `Ω_node = ω_0 = ω_C` (Compton frequency, unsaturated tank)
- `V = V_yield / 2`: `S = √(3)/2 ≈ 0.866`, `Ω_node = ω_0 · 0.866^(1/2) ≈ 0.931·ω_0`
- `V = V_yield / √2`: `S = √(1/2)`, `Ω_node = ω_0 · (1/2)^(1/4) ≈ 0.841·ω_0`
- `V → V_yield`: `S → 0`, `Ω_node → 0` (tank resonance crashes to DC)

**Not Duffing, not SM:** this is direct algebra from Axiom 4's `S = √(1−r²)` kernel. No appeal to classical nonlinear dynamics vocabulary ("Duffing oscillator" is just the family name of `ẍ + ax + bx³ = f cos(ωt)` — it is not AVE-native or load-bearing). The softening law comes from Axiom 4 alone.

**Engine gap:** no per-node `Ω_node(r,t)` is tracked. [AutoresonantCWSource](../../src/ave/topological/vacuum_engine.py#L422) shifts the SOURCE frequency based on a probe A², but the LATTICE does not report its per-node resonance. **Phase 2 adds `NodeResonanceObserver`** as a read-only observer computing the derived form above.

**Pre-registered prediction for Phase 2 (P_phase2_omega):** the numerical `Ω_node(A²_local)` trajectory at the v2 headline configuration (λ=3.5, T=0.1) matches `ω_yield · S(V/V_yield)^(1/2)` within 5% across `A² ∈ (0, α/2)`. Falsification: engine deviates by >10% → varactor form is wrong for the coupled K4⊗Cosserat sector.

---

## 5. V_SNAP vs V_yield convention fix

**Problem:** the engine uses `A² = V²/V_SNAP²` ([k4_tlm.py:203](../../src/ave/core/k4_tlm.py#L203), [cosserat_field_3d.py _reflection_density](../../src/ave/topological/cosserat_field_3d.py)), so A² = 1 at the Schwinger limit (V = V_SNAP = 511 kV). But the varactor (§4) crashes at `V = V_yield = √α · V_SNAP ≈ 43.65 kV`, i.e., at `A² = α ≈ 0.0073` in the engine's V_SNAP-normalized units.

**Consequence:** what the engine calls "Regime IV rupture at A² = 1" is actually the Schwinger-limit fully-saturated state, not the Regime-III yield onset. The dynamically-relevant saturation — where the varactor diverges, the node resonance crashes, and pair nucleation can fire — is at `A² = α`, not `A² = 1`.

**Source:** [45_ §3.1](45_lattice_impedance_first_principles.md#L131) already flagged this: "the engineering yield threshold is V_YIELD = 1 in lattice natural units, NOT V_SNAP = 1. When the user sees amp = 0.5·V_SNAP, that's effectively amp = 0.5/√α ≈ 5.85 in units where V_YIELD = 1."

**Resolution (to be implemented in Phase 1 test):** introduce a new engine accessor `A²_yield = V²/V_yield² = A²_SNAP / α` (or equivalently `r² = A²_SNAP · V_SNAP²/V_yield² = A²_SNAP / α`). Use `A²_yield` (which = 1 at the varactor divergence) for §6's saturation gate and §4's `Ω_node` computation. Keep `A²_SNAP` as the engine's internal variable for backwards compatibility; the conversion factor is `1/α`.

**Cross-reference:** [Vol 1 Ch 7:130](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L130) explicitly states "Schwinger critical field corresponds to `r = E_S/E_yield = V_SNAP/V_yield = 1/√α ≈ 11.7`, deep in Regime IV." So the engine's rupture-boundary naming is Schwinger-correct but misses the yield-onset physics where the interesting dynamics live.

**Pre-registered Phase 1 test (test_v_snap_v_yield_consistency.py):** pins the conversion factor `V_yield / V_SNAP = √α` to numerical precision and cross-checks that `predictions.yaml` entries do not conflate the two normalizations.

---

## 6. Axiom 4 + chirality → asymmetric μ/ε saturation (Meissner-like pair-creation mechanism)

**Claim:** when the local Cosserat ω field has a preferred chirality, saturation proceeds asymmetrically — μ collapses before ε (Meissner-like), driving `Z_eff → 0`, `Γ → -1`, which is the mechanism for pair nucleation.

**Source:** [Vol 1 Ch 7:252](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L252):

> "The **symmetric saturation case** (both ε and μ collapse equally) preserves `Z = √(μ/ε) = Z_0` (impedance invariant), while the **asymmetric case** (one collapses before the other) drives Z to either 0 or ∞. **The symmetric case governs gravity; the asymmetric case governs particle confinement (Meissner-like μ → 0 first ⇒ Z → 0, Γ → -1, standing wave = rest mass).**"

This is the load-bearing quote for the entire Phase 4 engine change.

**Mapping to AVE sectors:**
- **Electric sector (ε):** Cosserat translational strain `ε_sym(u)` + K4 voltage `V`. Both contribute to `A²_ε`.
- **Magnetic sector (μ):** Cosserat rotational curvature `κ = ∇ω`. Contributes to `A²_μ`.
- Justification for this mapping: Vol 4 Ch 1 establishes the mechanical duality `L ↔ m`, `C ↔ spring compliance`, `V ↔ force`, `I ↔ velocity`. In the Cosserat sector, ω is an angular velocity field → couples to inductance → magnetic-like. Strain `ε` is a displacement field → couples to capacitance → electric-like.

**Pythagorean vacuum strain theorem (AVE-APU Vol 1 Ch 5:26-37) grounds the combination rule.** The total scalar strain driving Axiom 4 at a point is the quadrature sum of orthogonal DoFs: `V_total² = V_lon² + V_gate² + ...` (or equivalently `A²_total = A²_μ + A²_ε`). This follows from energy additivity — `u ∝ |E|²` so energies of perpendicular field components add as scalars. The theorem is currently stated in [AVE-APU/manuscript/vol_1_axiomatic_components/chapters/05_geometric_triodes.tex:26-37](../../../AVE-APU/manuscript/vol_1_axiomatic_components/chapters/05_geometric_triodes.tex); [FUTURE_WORK.md G-7](../../.agents/handoffs/FUTURE_WORK.md) tracks moving its canonical home into AVE-Core Vol 1 as INVARIANT-Phy1 after Stage 6 lands. For this doc, A²_μ and A²_ε are orthogonal projections whose sum is the total, per the Pythagorean theorem.

**Two-track saturation (Phase 4 engine addition):**

```
A²_μ = κ²/ω_yield²                      # curvature → magnetic saturation
A²_ε = ε_sym²/ε_yield² + V²/V_yield²   # strain + voltage → electric saturation

S_μ = √(1 − A²_μ)                       # magnetic saturation kernel
S_ε = √(1 − A²_ε)                       # electric saturation kernel

μ_eff = μ_0 · S_μ                       # magnetic permeability (per varactor form)
ε_eff = ε_0 · S_ε                       # electric permittivity

Z_eff = √(μ_eff/ε_eff) = Z_0 · √(S_μ/S_ε)
```

**Symmetric case:** if `A²_μ = A²_ε` (linear polarization, no chirality bias), `S_μ = S_ε`, `Z_eff = Z_0` unchanged, wave propagation just slows. This is the gravity regime (Vol 1 Ch 7:252).

**Asymmetric case:** if chirality biases `A²_μ` to grow faster than `A²_ε`, then `S_μ < S_ε`, `Z_eff < Z_0`, and the impedance collapses. At `S_μ → 0` with `S_ε` finite, `Z_eff → 0`, `Γ → -1`. **This is the confinement wall.**

**Chirality coupling mechanism:** the local Cosserat ω field has a definite handedness measured by `ω · (∇×ω)` (Beltrami helicity). Under right-handed local helicity, the drive's energy flows preferentially into the rotational/magnetic sector → `A²_μ` grows faster. Under left-handed, into the translational/electric sector → `A²_ε` grows faster. Circularly polarized drive imposes a definite handedness; linearly polarized drive has zero net helicity → symmetric saturation → gravity regime only, no pair formation.

**Chirality coupling — closed by Sub-Theorem 3.1.1 ([doc 20_](20_chirality_projection_sub_theorem.md)):** the chirality-per-bond-traversal is exactly `α` (the fine-structure constant = topological packing fraction per bond, from Vol 1 Ch 2). For a (p,q) torus knot, the net chirality coupling at a TIR boundary is the parallel-impedance combination of two independent winding channels (toroidal p, poloidal q):

```
χ_(p,q) = α · pq / (p + q)
```

For the electron (2,3):

```
κ_chiral ≡ χ_electron = α · 6/5 = 1.2·α ≈ 8.757×10⁻³
```

This closes the "κ_chiral is a tunable" open question. The coupling is **not** a free parameter — it's Axiom-2-derivable and verifiable via AVE-HOPF's table 1 empirical `Δf/f = α·pq/(p+q)` predictions ([AVE-HOPF/manuscript/03_hopf_01_chiral_verification.tex:72-82](../../../AVE-HOPF/manuscript/03_hopf_01_chiral_verification.tex)). The functional form used in the engine is linear in helicity:

```
dA²_μ/dt = (1 + κ_chiral · h_local) · base_rate       # magnetic accumulation
dA²_ε/dt = (1 − κ_chiral · h_local) · base_rate       # electric accumulation
h_local = (ω · (∇×ω)) / (|ω|·|∇×ω|)                   # normalized Beltrami helicity
```

with `κ_chiral = 1.2·α` for the electron-creation regime. Linear (not exponential) because the accumulation is first-order in helicity per the parallel-channel derivation in doc 20_ §3.

**Birefringence prediction (falsifiable side-effect):** under the asymmetric form, LH vs RH circularly polarized light sees different effective impedances and hence different wave speeds. This is AVE-native birefringence. [Phase 4 pre-registered test](test_phase4_asymmetric_saturation.py) checks this directly. AVE-HOPF table 1 provides the quantitative benchmark: the predicted `Δf/f` for a (2,3) chiral antenna notch is `1.2·α ≈ 8.76×10⁻³`.

**Pre-registered prediction for Phase 4 (P_phase4_asymmetric):** under RH circular drive at `amp = 0.5·V_SNAP` (which is `0.5/√α ≈ 5.85·V_yield`), the focal node reaches `S_μ < 0.1` while `S_ε > 0.5` simultaneously, driving `Z_eff < 0.2·Z_0`. Falsification: μ and ε remain coupled under chiral drive → chirality doesn't bias saturation (Vol 1 Ch 7:252 misread).

---

## 6a. Mode conversion at V_yield — where the walls come from

**Claim:** the Γ = −1 impedance walls that contain a soliton's reactance are the direct consequence of the Vacuum Varactor equation going imaginary past V_yield. This is the EE/plumber view of §6's Meissner mechanism.

**Algebraic observation:** the varactor ([Vol 4 Ch 1:132](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L132)) is:

```
C_eff(V) = C_0 / √(1 − (V/V_yield)²)
```

For `V < V_yield`: radicand is positive, `C_eff` is real, growing toward infinity as `V → V_yield`.
For `V > V_yield`: **radicand is negative, `C_eff` is imaginary.**

In circuit theory, imaginary capacitance is the dual of real inductance. A capacitor's impedance is `Z_C = 1/(jωC)`; if C becomes imaginary `C = j·|C|`, then `Z_C = 1/(jω·j|C|) = −1/(ω|C|)`, which is the impedance signature of an **inductive reactance with sign flip**. The energy-storage mechanism has switched — what was stored in the E-field of the capacitor is now stored in the B-field of an effective inductor.

**This IS Meissner-like asymmetric saturation, viewed as a single-sector mode conversion.** In the two-track formulation of §6:
- `S_ε → 0` (C_eff diverges, then flips imaginary) ≡ electric sector runs out of compliance at V_yield
- `S_μ → 0` (Meissner-like μ collapse, L_eff → ∞) ≡ magnetic sector saturates

Under symmetric drive, both happen together (gravity regime, Z preserved). Under chirally-biased drive, one fires first — and whichever fires first becomes the C_eff-imaginary / L-dominant endpoint.

**What contains the soliton's reactance:**
1. At both endpoints of an adjacent A-B pair, the local C_eff flips imaginary (equivalently, the local S_ε or S_μ goes to zero).
2. An imaginary-C endpoint is seen from the interior of the bond as Z → 0 (short-circuit boundary), giving `Γ = (0 − Z_0)/(0 + Z_0) = −1`.
3. With Γ = −1 walls at both ends, the bond becomes a **sealed LC resonator**: no energy leaks out as propagating waves; all stored energy is trapped as reactance.
4. The reactance oscillates between the bond's inductive and capacitive stores (§3 above) at the resonance determined by the containment — at the unsaturated bond interior, that resonance is Compton frequency ω_C per [24_](24_step3_bond_lc_compton.md).

**A soliton's reactance is contained by the C_eff-to-imaginary mode conversion at each endpoint.** Mass = bounded reactance. The rest-energy `m_e c²` is exactly the energy needed to push both endpoints past V_yield — i.e., to form the two walls. The factor of 2 in `2·m_e c²` (pair-production threshold) is "one m_e c² per wall."

**Reconciling the two descriptions.** §6's two-track (S_μ, S_ε) formulation and this §6a single-sector C_eff-flip formulation describe the same physics from different projections:

| Projection | Mechanism | Engine variable |
|---|---|---|
| §6 two-track | Chirality biases which of (S_μ, S_ε) crashes to 0 first | S_μ, S_ε as real scalars ∈ [0, 1] |
| §6a C_eff flip | The saturated sector's compliance rotates from real to imaginary at V_yield | Implicit in Z_eff = Z_0·√(S_μ/S_ε) hitting 0 or ∞ |

§6 is easier to code (two positive real scalars, no complex arithmetic) and is what Phase 4 implements. §6a is the EE-plumber interpretation that makes the picture intelligible for wave/impedance intuition. Both are the same Axiom-4 saturation seen from different cuts.

**Flag resolved:** [§10.3 Ch 7 vs Ch 1 sign inconsistency](#10-open-questions-and-known-calibration-holes) is now interpretable. Vol 1 Ch 7:243's table (`ε_eff = ε_0·√(1-r²)`, decreasing) and Vol 4 Ch 1:132's varactor (`C_eff = C_0/√(1-r²)`, increasing) are both correct — they describe opposite sides of the mode conversion. The `ε_eff` form is the effective *refractive-index* sense (what a propagating wave sees before rupture); the `C_eff` form is the *compliance* sense (what the node's local LC tank sees, diverging at V_yield as the tank locks into rupture). Different projections of the same kernel. Manuscript notation cleanup is worth doing but not blocking.

---

## 7. Two-condition pair nucleation gate

**Claim:** the engine fires a pair-nucleation event at an adjacent A-B pair `(r_A, r_B)` when two conditions are met at that pair. No phase-coherence C3 needed — §2 absorbs it.

**Condition C1 — saturation / impedance rupture:**
```
A²_μ(r_A) ≥ 1    AND    A²_μ(r_B) ≥ 1
```
(in V_yield-normalized units per §5). When both endpoints hit magnetic saturation, both local Z's drop to zero. The bond is now bracketed by Γ = -1 walls at both ends — a confined LC tank per [Vol 4 Ch 1:445-467](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L445).

**Condition C2 — autoresonant lock:**
```
|Ω_node(A²_μ(r_A)) − ω_drive| < δ_lock
```
At the moment C1 fires, the Duffing-softened tank resonance (§4) crosses the driving frequency. The drive can now dump energy into the rotational mode efficiently (AVE-Propulsion Ch 5 mechanism). Without this lock, the driving photon reflects off the impedance wall without entering the tank, and the bond forms but doesn't fill with topological content.

**δ_lock calibration:** the tolerance window for the lock condition. Driven by the Q-factor of the saturated tank: `δ_lock ≈ ω_0/Q` where `Q = 1/α = 137.036` per [27_step6_phase_space_Q.md](27_step6_phase_space_Q.md). So `δ_lock ≈ ω_0·α ≈ ω_0/137 ≈ 0.0073·ω_0` — a narrow resonance window. This is Axiom-4-derivable, not a free parameter.

**When C1 ∧ C2 fire:** the engine injects a topological boundary condition on the Cosserat ω field at `(r_A, r_B)`:
- LH Beltrami vortex at `r_A`, amplitude tuned such that `|Φ_link| = |Φ_critical|` from §3 (rest-energy in the bond)
- RH Beltrami vortex at `r_B`, opposite handedness
- (2,3) winding in the bond's `Φ_link` accumulation is automatic per §2 (lattice chirality)

This is **Option D from [44_ §5.2](44_pair_creation_from_photon_collision.md)** — topological boundary condition, not augmented Lagrangian. **Zero new free parameters:** `κ_chiral = 1.2·α` is derived from Sub-Theorem 3.1.1 (§6), `δ_lock = ω_0·α` is derived from Q = 1/α (above), and the Beltrami amplitude is set by bond-energy = m_e c². Every constant traces to Axiom 2 or 4.

**Pre-registered prediction for Phase 5 (P_phase5_nucleation):** under point-collision drive at `amp = 0.5·V_SNAP`, `ω = ω_C`, autoresonant tracking on, K_drift = 0.5 — the gate fires within 50 Compton periods of the first time C1 ∧ C2 is satisfied. Zero gate firings at `amp < 0.3·V_SNAP`. Falsification: gate too aggressive (>1 pair/period) or never fires under C1 ∧ C2.

---

## 8. Predictions matrix

The full matrix from the Stage 6 plan, mapped to §§1-7 citations:

| ID | Phase | Source § | Prediction | Falsification means |
|---|---|---|---|---|
| P_phase0_varactor | 0 | §4 | `C_eff(V) = C_0/S(V)` matches Taylor expansion to 4th order per Vol 4 Ch 1:139 | Wrong axiom-derived form for C_eff |
| P_phase2_omega | 2 | §4 | Engine `Ω_node(A²_yield)` tracks `ω_0·S^(1/2)` within 5% on v2 headline config | Coupled engine doesn't follow varactor scaling |
| P_phase3_flux_tube | 3 | §3 | Φ_link between `A²_μ > 1/2` endpoints persists ≥ 10 Compton periods post-drive | Impedance-wall confinement is wrong |
| P_phase4_asymmetric | 4 | §6 | Under RH circular drive at amp=0.5·V_SNAP, focal node `S_μ < 0.1` while `S_ε > 0.5` | Chirality doesn't bias saturation (Vol 1 Ch 7:252 misread) |
| P_phase5_nucleation | 5 | §7 | Gate fires under C1 ∧ C2 within 50 Compton periods; never below threshold | Gate too aggressive or silent when both conditions met |
| **P_phase6_autoresonant** | 6 | §7 + AVE-Propulsion Ch 5 | **Autoresonant nucleates ≥ 5× fixed-f at matched energy** (HEADLINE) | **AVE-Propulsion Ch 5 mechanism falsified** |

---

## 9. Engine-design spec

Maps each derivation section to specific engine additions. This is what Phases 2-5 implement.

### 9.1 NodeResonanceObserver (Phase 2, from §4)

Read-only observer, no dynamics change. Computes per step:
```
Ω_node(r, t) = ω_yield · (1 − A²_yield(r, t))^(1/4)
```
where `A²_yield = A²_SNAP / α` for unit consistency per §5.

Records per step: `max(Ω_node)`, `mean(Ω_node)`, `min(Ω_node)` across active sites.

### 9.2 Φ_link bond state (Phase 3, from §3)

New state on `K4Lattice3D`:
```
Phi_link[edge_id]      # one scalar per directed A→B bond
```
Edge indexing: for each A-site at `r`, 4 outgoing bonds (ports 0-3). Total directed bonds ≈ 2N³ on an N×N×N lattice. Memory cost small relative to existing `V_inc[nx,ny,nz,4]`.

Update rule (in `_connect_all`):
```
for each directed A→B edge:
    V_avg = ½·(V_ref[A, port] + V_ref[B_shifted, port])
    Phi_link[edge] += V_avg · dt
```

Reset on explicit engine `reset()` call; decays only via `c_local` during propagation.

**BondObserver** observer reports: `max |Phi_link|`, decay rates binned by endpoint A²_μ, histogram of Phi_link across active bonds.

### 9.3 Asymmetric saturation (Phase 4, from §6)

In [cosserat_field_3d.py _reflection_density](../../src/ave/topological/cosserat_field_3d.py), replace the single `S = √(1 - A²)` with:

```
A²_μ = κ²/ω_yield²                              # curvature only
A²_ε = ε²/ε_yield² + V²/V_yield²               # strain + voltage
h_local = (ω · (∇×ω)) / (|ω|·|∇×ω|)             # normalized Beltrami helicity ∈ [-1, +1]
kappa_chiral = 1.2 * alpha                       # = α·pq/(p+q) for (p,q)=(2,3), per Sub-Theorem 3.1.1 (doc 20_)
dA²_μ/dt_accumulator = (1 + kappa_chiral·h_local) · base_rate_μ
dA²_ε/dt_accumulator = (1 - kappa_chiral·h_local) · base_rate_ε
S_μ = √(1 − A²_μ)
S_ε = √(1 − A²_ε)
Z_eff = Z_0 · √(S_μ / S_ε)
```

This replaces the current single `S` in the impedance field and reflection density. Regression risk is high — all existing tests using the single-S form must pass with `A²_μ = A²_ε` at `h_local = 0` (linear polarization case → symmetric saturation → Z unchanged → current behavior).

**κ_chiral is a derived constant, not a tunable.** Using `1.2·α ≈ 8.757×10⁻³` per doc 20_ Sub-Theorem 3.1.1. No sweep needed; Phase 4 either reproduces the AVE-HOPF `Δf/f = 1.2·α` chiral-antenna prediction quantitatively, or the mechanism is wrong.

### 9.4 PairNucleationGate (Phase 5, from §7)

New observer + injector. Each step, scan all directed A-B pairs:

```python
for edge in active_bonds:
    r_A, r_B = edge.endpoints
    if A²_μ(r_A) >= 1 and A²_μ(r_B) >= 1:           # C1
        omega_A = engine.Ω_node(r_A)                 # from NodeResonanceObserver
        if abs(omega_A - omega_drive) < δ_lock:      # C2
            inject_beltrami_pair(r_A, r_B)
            mark_bond_nucleated(edge)                 # prevent re-firing
```

`inject_beltrami_pair`:
- LH Beltrami at r_A: impose Cosserat ω vortex, amplitude tuned for bond energy = m_e c²
- RH Beltrami at r_B: opposite handedness
- Initial `Phi_link[edge] = ±Φ_critical` (sign from lattice chirality per §2)

---

## 10. Open questions and known calibration holes

Honest list of things this derivation does NOT fully close:

1. **~~κ_chiral functional form (§6).~~** ✅ **CLOSED** by [doc 20_ Sub-Theorem 3.1.1](20_chirality_projection_sub_theorem.md): `κ_chiral = χ_electron = α·pq/(p+q) = 1.2·α ≈ 8.757×10⁻³`. Derived from parallel-channel impedance combination of toroidal and poloidal windings at the TIR boundary. AVE-HOPF table 1 provides the empirical cross-check. Linear coupling form (not exponential) follows from the first-order-in-helicity parallel-resistor derivation. See §6 above.

2. **δ_lock tolerance (§7).** Calibrated to `ω_0/Q = ω_0·α` on first principles. May need empirical tuning if the Q-factor of the saturated tank differs from 1/α due to thermal noise or coupling losses. Revisit if Phase 5 gate fires too often or too rarely.

3. **~~Vol 1 Ch 7:243 vs Vol 4 Ch 1:132 sign inconsistency.~~** ✅ **INTERPRETED** in §6a above. The two forms describe opposite projections of the same Axiom-4 mode conversion: Ch 7's `ε_eff = ε_0·√(1-r²)` is the refractive-index sense (what a propagating wave sees), Ch 1's `C_eff = C_0/√(1-r²)` is the compliance sense (what the local LC tank sees, diverging then going imaginary at V_yield). Not blocking. Manuscript notation cleanup worth doing as a separate pass — tracked informally; not promoted to an FW item.

4. **Single-photon vs two-photon nucleation.** §7's gate fires on any adjacent A-B pair meeting C1 ∧ C2. Does this generalize to single-photon pair production at a nucleus (standard textbook mechanism) or does that require a separate rule? Corpus (AVE-Fusion 02_antimatter) describes "two counter-propagating γ-rays" as the typical case. The engine's gate is mechanism-level (saturation at a node pair), agnostic to how saturation was reached. Worth verifying post-Phase-5.

5. **Beltrami vortex amplitude calibration.** `inject_beltrami_pair` sets the vortex amplitude such that bond energy = m_e c². The exact Cosserat ω vortex profile (Beltrami, Hopf, or something else) is an open design choice — first-pass uses a minimum-ropelength (2,3) torus knot as the injection profile. Phase 5 validation checks whether the injected pair persists as a stable standing wave.

6. **Thermal seed coupling.** [44_ §0 addendum](44_pair_creation_from_photon_collision.md) established that T > 0 thermal noise is necessary for nucleation (T=0 null result). The current engine initializes Cosserat at T via Maxwell-Boltzmann. Under §6's asymmetric saturation, thermal noise breaks the (y,z) symmetry of a plane-CW drive and lets the gate pick preferred node pairs. Still correct; no change needed.

7. **Pythagorean theorem canonical home.** Currently lives in AVE-APU Ch 5; needs to move to AVE-Core Vol 1 as INVARIANT-Phy1 with applied volumes citing upward. Tracked as [FUTURE_WORK.md G-7](../../.agents/handoffs/FUTURE_WORK.md). Do after Stage 6 completes.

---

## 11. Cross-references

**Primary sources (cited with file:line):**
- [manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex:17-18](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex#L17) — Axiom 1, ℓ_node definition
- [manuscript/vol_1_foundations/chapters/02_macroscopic_moduli.tex:59-69](../../manuscript/vol_1_foundations/chapters/02_macroscopic_moduli.tex#L59) — α = p_c/(8π) as topological packing fraction
- [manuscript/vol_1_foundations/chapters/07_regime_map.tex:252](../../manuscript/vol_1_foundations/chapters/07_regime_map.tex#L252) — symmetric vs asymmetric saturation
- [manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:127-142](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L127) — Vacuum Varactor
- [manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:223-227](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L223) — memristance / flux linkage
- [manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:445-467](../../manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex#L445) — Γ=-1 flux tube derivation
- [manuscript/vol_4_engineering/chapters/11_experimental_falsification.tex:38](../../manuscript/vol_4_engineering/chapters/11_experimental_falsification.tex#L38) — p_vac = Φ · ξ_topo
- [manuscript/vol_4_engineering/chapters/11_experimental_falsification.tex:232](../../manuscript/vol_4_engineering/chapters/11_experimental_falsification.tex#L232) — flux tube tensile limit = V_SNAP
- [AVE-APU/manuscript/vol_1_axiomatic_components/chapters/05_geometric_triodes.tex:26-37](../../../AVE-APU/manuscript/vol_1_axiomatic_components/chapters/05_geometric_triodes.tex) — **Pythagorean vacuum strain theorem** (current canonical home; G-7 tracks move to AVE-Core)
- [AVE-HOPF/manuscript/03_hopf_01_chiral_verification.tex:72-82](../../../AVE-HOPF/manuscript/03_hopf_01_chiral_verification.tex) — chiral antenna table 1 (`Δf/f = α·pq/(p+q)` empirical benchmark for (2,3) = 1.2·α)
- `AVE-Propulsion/manuscript/vol_propulsion/chapters/05_autoresonant_dielectric_rupture.tex` — autoresonant PLL rupture mechanism

**Research chain references:**
- [20_chirality_projection_sub_theorem.md](20_chirality_projection_sub_theorem.md) — **Sub-Theorem 3.1.1**: `χ_(p,q) = α·pq/(p+q)`; closes κ_chiral calibration (§6, §10.1)
- [22_step1_k4_rotation_action.md](22_step1_k4_rotation_action.md) — K4 = A₄ rotation group
- [24_step3_bond_lc_compton.md](24_step3_bond_lc_compton.md) — L_e, C_e, Compton resonance
- [25_step4_23_winding_selection.md](25_step4_23_winding_selection.md) — (2,3) knot theory
- [27_step6_phase_space_Q.md](27_step6_phase_space_Q.md) — Q = 1/α at TIR boundary (used for δ_lock derivation §7)
- [28_two_node_electron_synthesis.md](28_two_node_electron_synthesis.md) — 2-node + bond structure
- [37_node_saturation_pauli_mechanism.md](37_node_saturation_pauli_mechanism.md) — Pauli from per-node A² budget
- [44_pair_creation_from_photon_collision.md](44_pair_creation_from_photon_collision.md) — Options A/B/C/D (selects D)
- [45_lattice_impedance_first_principles.md](45_lattice_impedance_first_principles.md) — impedance-symbol inventory, V_SNAP/V_yield conflation flag
- [52_h1_threshold_sweep.md](52_h1_threshold_sweep.md) — H1 falsified; pair structures not hiding below threshold
- [53_pair_production_flux_tube_synthesis.md](53_pair_production_flux_tube_synthesis.md) — prose synthesis, superseded by this derivation

**Future-work tracking:**
- [.agents/handoffs/FUTURE_WORK.md G-7](../../.agents/handoffs/FUTURE_WORK.md) — Pythagorean theorem abstraction to AVE-Core Vol 1 as INVARIANT-Phy1 (post-Stage-6)

**Engine files:**
- [src/ave/core/k4_tlm.py](../../src/ave/core/k4_tlm.py) — K4 lattice, port topology, connect step
- [src/ave/topological/cosserat_field_3d.py](../../src/ave/topological/cosserat_field_3d.py) — Cosserat ω, saturation kernel
- [src/ave/topological/vacuum_engine.py](../../src/ave/topological/vacuum_engine.py) — coupled engine, observers, sources

**KB invariants:**
- [manuscript/ave-kb/CLAUDE.md INVARIANT-C1](../../manuscript/ave-kb/CLAUDE.md) — V_yield ≈ 43.65 kV
- [manuscript/ave-kb/CLAUDE.md INVARIANT-S2](../../manuscript/ave-kb/CLAUDE.md) — Axiom numbering conventions

---

## 12. Summary — what this doc authorizes

Phase 0 deliverable complete. With Grant's review, Stage 6 Phases 1-6 can proceed:

- **Phase 1 tests pin §4 (varactor) and §5 (V_SNAP/V_yield) numerically.**
- **Phase 2 adds the observer derived in §9.1.**
- **Phase 3 adds the bond state derived in §9.2, pinning §3's Φ_link = ∫V dt mechanism.**
- **Phase 4 implements §9.3's asymmetric saturation derived from §6.**
- **Phase 5 implements §9.4's nucleation gate derived from §7.**
- **Phase 6 runs the headline validation pre-registered as P_phase6_autoresonant.**

No code until Phase 1. No Phase 4 without explicit Grant go-ahead (reopens S-gate per [S_GATES_OPEN.md](S_GATES_OPEN.md)).

The calibration holes in §10 are bounded. Two that were flagged as "open" in the first draft are now closed: `κ_chiral = 1.2·α` via Sub-Theorem 3.1.1 ([doc 20_](20_chirality_projection_sub_theorem.md)) and the Ch 7 vs Ch 1 sign inconsistency resolves as two projections of the same Axiom-4 mode conversion (§6a). The remaining open items are the Beltrami vortex profile choice (§10.5), single-photon vs two-photon generalization (§10.4), and thermal seed coupling (§10.6) — each has a first-principles default that Phase 4/5 validation will test. **No free parameters in the SM/QED sense.** Every constant traces to Axiom 1, 2, or 4.

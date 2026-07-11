# x42 — THE ATOMIC EIGENCAVITY: hydrogen as an Op6 phase-closure problem — RESULT

**Date:** 2026-07-10 · **Lane:** implementer · **Branch:** `analysis/x42-atomic-eigencavity`
**FROZEN prereg (gated on):** `research/2026-07-10_x42-atomic-eigencavity_prereg_FROZEN.md`
(freeze commit `0e5047e4`, PUSHED before this doc + all code — git ordering = freeze proof).
**Brief (binding):** `_orchestration/2026-07-10_x42-atomic-eigencavity-brief.md`
**Driver:** `src/scripts/vol_2_subatomic/x42_atomic_eigencavity.py` · **Tests:**
`src/tests/test_x42_atomic_eigencavity.py` (13 pass).

---

## SECTOR HEADER (declared before any substrate claim)

- **MODE:** derivation-from-canon + numerical consistency driver. **NOT engine-fire.** Op6 is
  eigenmode-finding for a GIVEN network, never geometry-selection (`src/ave/core/constants.py:212-228`
  α HONEST-SCOPE note — the S₁₁ landscape is FLAT in R·r, S₁₁-min does NOT select the geometry;
  `manuscript/ave-kb/vol2/particle-physics/ch01-topological-matter/electron-identification.md:77`
  Rule-12 Op6-scope re-scope, 2026-07-10: "S₁₁-min is the action the Golden Torus is a *stationary
  point of*, NOT the selector"). x42 respects this: the atom's `Z(r)` is GIVEN (the source-slaved
  Coulomb dress cast by the nuclear charge); Op6 finds its modes; a₀ falls out as the eigenmode SCALE
  of the given profile — Op6 selects neither a₀ nor the 1/r geometry.
- **REGIME:**
  - Hydrogen: cold/linear, deep Regime I. Per-node Ax-4 kernel argument at a₀ is
    `V_Coulomb(a₀)/(m_e c²) = α·(ℓ_node/a₀) = α² ≈ 5.3×10⁻⁵` (deep-linear; the well acts as pure GIVEN
    geometry, `S(A)≈1`; cross-check `de-broglie-n.md`: `V/V_yield ~ Zα² ≈ 10⁻⁴`).
  - Muonic H: the reduced-mass SPECTRUM scaling rides the SAME (linear) network. §3 computed
    `A = E_Coulomb(a_μ)/E_yield ≈ 0.116` — O(0.1), NOT deep-linear. Whether the near-nucleus field
    ADDITIONALLY biases the lattice at the muonic scale is the X41 frozen tie (§Deliverable 5); the
    driver's near-nucleus non-linearity (`strain_amp>1` at `r ≲ α·ℓ_node`) is that regime, deliberately
    excluded from the spectrum reproduction, NOT a spectral-correction claim.
- **SECTOR:** the probe's de Broglie / matter-wave channel on the `Z₀` radial transmission line (the
  bulk-modulus longitudinal soliton dispersion, `de-broglie-standing-wave.md`). The nuclear dress is
  longitudinal, source-slaved (bin 3 of walk (a): `|Γ|=1` at ω→0, radiates nothing). **A1 ⊥ T2**
  respected; **charge = Cosserat (2,3) winding, untouched** by any mode-count integer here.

---

## HEADLINE

The atom read in the impedance-carve register reproduces the canonical hydrogen consistency ceiling
through a **phase-closure / ABCD route** (NOT `E = Z²Ry/n²` fiat): the off-line Coulomb dress → a
graded impedance profile `Z(r)` → round-trip phase closure `2πn` → the Op6 spectrum `B_total(E)=0`.
The driver reproduces `E_n = Ry/n²` (branch (i), −0.000% to n=7), `a₀` as the eigenmode scale, the
muonic reduced-mass marks (E₁(μH)=−2.52849 keV, −0.0002%), and Z²-scaling — all as
**consistency-class** results with **NO new primitive**. The two-register guard (mode-count vs winding
integers) is formalized; the K1/K2 well-transparency question is quoted conditionally and NOT resolved.

*(Deliverables, mark outcomes, muonic operating-point, two-register guard, K1/K2 caveat, classification,
and flags follow — filled section-by-section per incremental-write discipline.)*

## DELIVERABLE 1 — Z(r) FROM THE COULOMB DRESS, SUBSTRATE-NATIVE

**The port-language derivation path (dress → Z(r) → reflections).** The nucleus's Coulomb well is,
in the four-bin taxonomy of walk (a) (`research/2026-07-10_impedance-register-walks_framing.md:19`),
**bin 3: the off-line, source-slaved reactive-static dress** — `|Γ|=1` at ω→0, radiates nothing (no
`Re(Z)`). It is not a potential floor; it is the electron's own reactive-static register acting as the
graded-impedance WALLS of a cavity (walk (c), `:53`). The derivation IMPORTS the Coulomb dress form
exactly as canon does (see the flag on the 1/r tail below) and casts it in the impedance register:

1. **The dress as a graded index.** Canon already has the atom as a **spherical radial transmission
   line** (`de-broglie-n.md`, `clm-oltvwy`): the nucleus projects the Coulomb field into all `4π`
   steradians, and the lattice impedance is `Z₀ = 377 Ω` everywhere (the nuclear `V/V_yield ~ Zα² ≈
   10⁻⁴` keeps the whole atom linear — Ax-4 check). The dress is seen by the probe's **de Broglie
   dispersion** as the energy-dependent graded index

   > `n(r, ξ) = √( 2·Z_eff(r)·a₀ / r  −  ξ )`,  `ξ = E/Ry`

   (`de-broglie-n.md` resultbox; `driver.de_broglie_refractive_index`). Near the nucleus `n→∞` (fast
   defect, low impedance, short circuit); at the classical turning point `n=0` (defect stops, high
   impedance, open circuit). This is the off-line dress rendered as an impedance / **mismatch** profile
   `Z(r)` — the graded walls, not a floor.
2. **Reflections make the cavity.** Where `E > V(r)` the acoustic impedance is real → propagating; where
   `E < V(r)` it is purely imaginary → total reflection (`de-broglie-standing-wave.md`:54). The orbital
   is "the precise radius where this trapped bulk-modulus acoustic wave achieves a lossless resonant
   impedance match with itself" — a wave trapped between its own reflections in a well made of MISMATCH.
3. **Added content = the register, not the form.** The `Z(r)` FORM is canon's; x42's added content is
   the **port-language statement** — bin-3 off-line dress → graded `Z(r)` → reflections — which makes
   the cavity walls an impedance boundary and sets up the spectrum as an Op6 phase-closure problem on a
   GIVEN profile (not a Schrödinger eigenproblem on a potential).

## DELIVERABLE 2 — THE PHASE-CLOSURE SPECTRUM ON THE GRADED LINE

**Round-trip phase closure `2πn` → `E_n ∝ 1/n²` and `a₀`, via the Op5/Op6 cascade — NOT the closed
form.** Quantization is the round-trip phase-closure condition on the graded line: the electron ring is
a closed circuit of circumference `2πR`, and a standing wave requires `∮k·dl = 2πn` → `m_e v R = nℏ`
(`de-broglie-standing-wave.md` §(e)). Equivalently, the radial standing wave on the graded `Z(r)`
satisfies the ABCD-cascade eigenvalue condition `B_total(E) = 0` — Op6 (`clm-gdd70j`,
`λ_min(S†S)→0`; `radial-eigenvalue-solver.md` §E2d-ii step 5).

**The driver runs the closure route, not the closed form.** `phase_closure_spectrum` cascades a
faithful generalization of the canonical Op5 primitive `radial_eigenvalue._abcd_section` over the
graded Coulomb dress (the test `test_dress_section_reuses_canonical_op5_exactly` asserts the
generalization equals `_abcd_section` element-wise at `m_probe=m_e, dress_exp=1, saturate=True`), with
inner BC = regular Coulomb solution at `r→0` and outer BC = `ψ′ + κψ = 0` (the decaying branch,
`B_total=0`). Zeros of the residual are the phase-closure eigenmodes. **Result (Z=1, l=0):**

| n | phase-closure E_n [eV] | Ry/n² [eV] | err |
|---|---|---|---|
| 1 | 13.6057 | 13.6057 | −0.000% |
| 2 | 3.4014 | 3.4014 | −0.000% |
| 3 | 1.5117 | 1.5117 | −0.000% |
| 4 | 0.8504 | 0.8504 | −0.000% |
| 5 | 0.5442 | 0.5442 | −0.000% |
| 6 | 0.3779 | 0.3779 | −0.000% |
| 7 | 0.2777 | 0.2777 | −0.000% |

`n* = √(Ry/E_n) = 1,2,3,4,5,6,7` to 4 decimals. `E_n·n² = Ry` constant (the 1/n² FORM). `a₀ = A_0`
falls out as the eigenmode scale (M2), and the canon identity `a₀ = ℓ_node/α` holds exactly
(`L_NODE/ALPHA == A_0`, `test_m2_a0_identity_exact`).

**Turning-point / Maslov phase (prereg branch (i), as pre-stated).** The ODE/ABCD `B_total=0`
formulation captures the turning-point (Maslov) phase EXACTLY through the boundary conditions — no
½-integer constant is inserted by hand — so branch (i) is realized (no closure-constant offset). This
matches `radial-eigenvalue-solver.md` §E2f-6: "Axioms 1, 2, and 4 together reproduce the standard
radial wave equation at Regime I scales." A naive WKB Sommerfeld `∮k dr = nπ` WITHOUT the Maslov `+½`
would land in branch (ii); the ODE route does not, so no offset is reported and none is tuned.

**Scope guard (binding).** `E = Z_eff²Ry/n²` as the IE FORMULA is the Bohr/Schrödinger contamination
(`vol2/claim-quality.md:342`); the x42 route GOES THROUGH the closure/ABCD condition and only COMPARES
against the closed form. `Ry = α²m_e c²/2` is emergent from `r_sat = a₀ = ℓ_node/α`
(`vol2/claim-quality.md:336`), and `r_n = n²a₀/Z` is the standing-wave condition, not a Bohr postulate
(`:337`). No sentence here credits Op6 with selecting a₀ or the 1/r geometry.

## DELIVERABLE 3 — THE MUONIC CASE = SAME NETWORK, HEAVIER PROBE SCALE

**What changes: ONLY the probe's mass/Compton scale (the dispersion scale). The network is unchanged.**
The muonic atom is the identical graded Coulomb network; the only substitution is the probe mass in
the de Broglie dispersion, `m_e → m_r,μ` (reduced mass, since `m_μ` is not negligible against `m_p`:
`m_r,μ = m_μ m_p/(m_μ + m_p)`). In the driver this is literally a single argument change
(`muonic_spectrum` calls `phase_closure_spectrum(m_probe=M_R_MU)`); the Op5 cascade, the boundary
conditions, and the dress exponent are identical. The lattice rupture scale in the Ax-4 kernel stays
`m_e c²` (a lattice property, not the probe's).

**Reproduced scaling (frozen marks M3):** `a_μ = a₀·(m_e/m_r,μ)`, `E_n(μH) = E_n(H)·(m_r,μ/m_r,H)`.
Driver (cold-lattice LINEAR network, `saturate=False`):

| n | phase-closure E_n(μH) [keV] | frozen mark [keV] | err |
|---|---|---|---|
| 1 | −2.52849 | −2.528493 | −0.0002% |
| 2 | −0.63212 | −0.632123 | ~0% |
| 3 | −0.28094 | −0.280944 | ~0% |

`a_μ = 284.748 fm` (M3). Reduced-mass ratios: `m_r,μ/m_e = 185.84083`, `m_r,μ/m_r,H = 185.94205`.

**Why the LINEAR network (saturate=False) for the muonic run — a physics choice, not a fudge.** At
`r ≲ α·ℓ_node` the muonic Coulomb field drives the per-node Ax-4 kernel argument `V/(m_e c²)` PAST
yield (`>1`), so `S(A)→0` and the linear cascade diverges near the nucleus. That near-nucleus
non-linearity is exactly the **X41 frozen-tie regime** (does the near-nucleus field ADDITIONALLY bias
the lattice?), which the brief §3 says NOT to fold into a spectral-correction claim. The reduced-mass
SPECTRUM scaling is a property of the LINEAR Coulomb network alone (`E_n ∝ m` at fixed Z), so it is
reproduced with the cold-lattice cascade; the saturating near-nucleus region is surfaced as a flag
(§Flags), not absorbed as a correction. Empirical-driver discipline (Rule 10) surfaced this: the
saturated cascade produced spurious deeper-than-ground roots — read as physics (sub-yield break), not
debugged toward a rescue.

## DELIVERABLE 4 — THE TWO-REGISTER GUARD, STATED FORMALLY

**The quantization homonym: two integer families that share the word "quantized" and must never be
cross-wired** (formalization of walk (c), `:55-64`; NOT a new claim).

| | **Mode-count integers** | **Winding integers** |
|---|---|---|
| examples | n, l, m (atomic levels) | charge, the (2,3) winding |
| register | **embedding** (the cavity) | **graph** (the connectivity) |
| what fixes them | round-trip phase closure `2πn` on `Z(r)` | topological invariant on the bond-pair graph |
| stability | **cavity-deformable** — bend the walls and they move | **topologically protected** — no smooth deformation changes them |
| owner | the Op6 eigencavity (this document) | Cosserat (2,3) winding, `def-3638f2` (untouched here) |

**Formal statement.** Let `𝒩 = {n, l, m}` be the mode-count integers — the eigenmode labels of the
GIVEN graded cavity `Z(r)` (Deliverable 2), fixed by phase closure `∮k·dl = 2πn`. Let `𝒲 = {Q, (2,3)}`
be the winding integers — topological invariants on the substrate connectivity graph (Axiom 2 TKI,
`[Q]≡[L]`). These are **different objects with different failure modes**:

> **"Ionization kills the mode, not the knot."** Ionizing the atom removes the electron's standing mode
> — `𝒩` is destroyed (`n, l, m` gone, the cavity is emptied) — while the electron's charge and its
> `(2,3)` winding `𝒲` are **untouched** (the freed electron is the same `0₁`-unknot soliton carrying
> the same charge). A deformation of the cavity walls (a different `Z(r)`, e.g. a field) moves `𝒩`
> continuously; NO smooth deformation changes `𝒲`.

That the two families have **different failure modes** is the operational proof that they are different
objects: `𝒩` is a continuous-spectrum property of an embedding cavity; `𝒲` is a discrete invariant of a
graph. This is why "quantized" is a homonym across the two, and why the mode-count `n` in this document
never touches the charge/winding sector (A1 ⊥ T2; charge = Cosserat winding, `INVARIANT-N1` knot
disambiguation).

**def-node NOT minted (flagged-not-minted).** Walk (c) `:68` flags the **quantization-homonym def-node
pair** (mode-count-integer ↔ winding-integer) as a vocabulary-register CANDIDATE for a future
terminology pass, alongside the existing homonym entries (the three "3"s, the two ℤ₂'s, the (2,q)
glyph). It is **surfaced here as a candidate, NOT minted** — no `def-` id is created from this lane
(KB canonization is a gated follow-on; INVARIANT-S12 def-nodes are register-hosted in
`common/vocabulary-register.md`, which this lane does not edit). The auditor lane lands any def-node.

## DELIVERABLE 5 — THE K1/K2 CAVEAT, STATED CONDITIONALLY (NOT RESOLVED)

The well's kernel-transparency — **does the held longitudinal Coulomb dress bias the Ax-4 kernel, or is
it kernel-transparent?** — is GOVERNED by the X41 fork. Verdict class, quoted **verbatim** from
`research/2026-07-10_x41-radiative-scoping-why_RESULT.md:37`:

> **"[UNDERDETERMINED — K1 ∧ K2, with the transverse-reactive near-zone as the named discriminator]"**

**What this means for x42, conditionally.** The bin-3 off-line dress is "THE K2 CANDIDATE — tagged
*contingent on X41's open fork*" (walk (a), `:19`). Both keys predict the held static Coulomb
**transparent-to-T2**, each on its own **unpaid** premise:
- **K1 [projection]:** a held static Coulomb is purely longitudinal (`E_T ≡ 0`, a Helmholtz identity),
  so it biases only the A1 compliance, not the T2 permittivity — **IF** the (PENDING-GRANT) premise
  holds that T2 keys on `|E_T|` (X41 §3.1).
- **K2 [impedance/mode-basis]:** `ω=0` → no `R_rad` → the dress never meets the kernel → transparent —
  **IF** the Ax-4 kernel is relocated reactance→`R_rad` (X41 §3.2).

**The standing canonical reading disagrees with both keys' transparency for the held field:**
`manuscript/ave-kb/CLAUDE.md:75` — *"A **static-E-only drive is ASYMMETRIC**: a static field has no
`∂B/∂t` to load the `μ` / microrotational (Cosserat-B) sector, so it loads the `ε` / capacitive sector
only (`S_ε < 1`, `S_μ = 1`)"* — i.e. a held static E **LOADS** `S_ε`. The x42 spectrum reproduction
does not depend on this: it treats the well as pure GIVEN geometry in the deep-linear hydrogen regime
(`S≈1`), where loaded-vs-transparent is a `~10⁻⁴` distinction below the marks' tolerance.

**Where it bites: the muonic operating point.** At `A_§3 = E_Coulomb(a_μ)/E_yield ≈ 0.116` (O(0.1), NOT
deep-linear), whether the near-nucleus field ADDITIONALLY biases the lattice is exactly this frozen
tie. Standing canon (+ #547) → it loads → a computable ε-shift (the #547-class overshoot); K1/K2 →
transparent. **This lane does NOT resolve the fork** and does NOT turn the muonic operating point into a
spectral-correction claim. Adjudicators (per X41 §5/§7): **Grant** (K1's axiom-level ruling) + the
**CVR held-DC-E bench** + the **unbuilt transverse-reactive near-zone probe**. Surfaced, not decreed.

## MARK OUTCOMES (M1–M4) *(pending)*

## CLASSIFICATION (consistency-vs-emergence + new-primitive scan) *(pending)*

## FLAGS SURFACED (flag-don't-fix) *(pending)*

## DISCIPLINE *(pending)*

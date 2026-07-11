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

## DELIVERABLE 1 — Z(r) FROM THE COULOMB DRESS *(pending)*

## DELIVERABLE 2 — THE PHASE-CLOSURE SPECTRUM *(pending)*

## DELIVERABLE 3 — THE MUONIC CASE *(pending)*

## DELIVERABLE 4 — THE TWO-REGISTER GUARD *(pending)*

## DELIVERABLE 5 — THE K1/K2 CAVEAT *(pending)*

## MARK OUTCOMES (M1–M4) *(pending)*

## CLASSIFICATION (consistency-vs-emergence + new-primitive scan) *(pending)*

## FLAGS SURFACED (flag-don't-fix) *(pending)*

## DISCIPLINE *(pending)*

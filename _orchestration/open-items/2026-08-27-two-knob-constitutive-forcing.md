---
id: two-knob-constitutive-forcing
title: "Is (a1,b1,b2) = (2,1,1/2) forced by the constitutive map, or is it a two-measurement calibration plus one assertion?"
status: ROUTED-TO-GRANT
owner: grant
opened: 2026-08-27
source: research/2026-08-27_two-knob-gravity-repair_result.md
anchor: "currently WORKS. Nothing yet FORCES it"
---

**The result this gates.** Posed as wave mechanics with no metric, the closed-orbit
precession is `Δφ = (πGM/c²ℓ_p)(4a₁ − b₁ − 2b₂/b₁)`, where `c_eff = c(1 − a₁U + …)`
is the medium's local characteristic speed and `Ω = Ω_∞(1 − b₁U + b₂U² …)` is the
packet's own internal rest frequency. Canon's matter channel feeds **one** number
into **both** slots (a Gordon scalar index forces `a₁ = b₁`, `b₂ = a₁²` — an
identity, not an approximation), collapsing the bracket to the bare index slope
`= 1` and giving Mercury `7.163″`/cy against `42.98 ± 0.04` (**−895σ**).
Setting `(2, 1, ½)` returns Mercury `42.981″`/cy, Hulse-Taylor `4.2266°`/yr,
solar limb `1.751″`, `γ = β = 1`.

**The question. Does anything in the substrate compel those three numbers?**
As the ledger stands the answer looks like *no*, three times over:

| number | current standing |
|---|---|
| `a₁ = 2` | **GR-IMPORTED.** It is `ν_vac · 7`, and canon stamps both factors: `eq_axiom_5.tex`:134 *"kappa = c^4/7G and nu = 2/7 stay GR-imported (#261 untouched)"*; `double-deflection.md`:60 *"ν=2/7 is **not** crystalline-lattice-forced"*. |
| `b₁ = 1` | **CALIBRATED to Newton.** The FORM `a = −c²∇ln Ω` is derived; the VALUE is whatever makes it Newtonian. |
| `b₂ = ½` | **ASSERTED.** Equivalent to "the clock grades multiplicatively, `Ω = Ω_∞ e^(−U)`". No axiom, no leaf, no lane derives it. Worth **179σ** on Mercury if it is 0 instead. |

**And the L3 lane found the map itself does not exist.** Canon's only bias→index
object is Op19 (`operators.md`:59, CANONICAL), whose licensed coefficient the
2026-08-11 linearity audit calls *"a kinematic ratio (transverse strain per
longitudinal strain), not a modulus"* — a strain-per-strain ratio doing a
strain-per-**index** job. The object that performs that conversion in any real
medium is the rank-4 photoelastic tensor `p_ijkl`, which this corpus has never
named (separate item: `2026-08-27-bias-to-index-photoelastic-map`). Working in
L3's own labels (`γ_∥ = 1 + P·U`, `γ_⊥ = 1 + Q·U`, `f` = the bound mode's radial
`k`-power fraction): deflection fixes `Q = 2` **independent of P**, the Newtonian
limit fixes `[f·Q + (1−f)(P+Q)/2] = 1` — **three unknowns, two measurements, so a
one-parameter family survives.** `b₂` is a *fourth* number that ledger does not
reach at all.

**What is being asked of Grant — a physics ruling, not a bookkeeping one.**

1. **Is `Ω(r)` a free constitutive function, or is it a second projection of the
   same graded tensor light rides?** The L1 lane says two knobs
   (`c_eff² = 1/(LC)` is the product, achromatic-impedance pins only the ratio
   `L/C`; `Ω² = S/C` rides the Cosserat stiffness `4G_c/I_ω` which no impedance
   theorem constrains). The L3 and reconciliation lanes say that in a Z-matched
   medium a bound mode is a **cavity mode of the same tensor**, so its clock is
   not free. **These give different answers to "can `b₂` be derived at all."**
2. **Does a bound matter packet ride light's own `c_eff(r)`?** The repair needs
   yes. `temporal-spatial-lattice-decomposition.md`:24 calls the slope-2 index
   *"what a signal traversing the gradient accumulates"*, which reads
   channel-agnostic — but the same line also calls it `≈ 1/g₀₀`, a
   temporal-metric object, and labels it "temporal". **This interpretive step is
   what the whole repair rests on and canon does not state it.**
3. **Additive or multiplicative?** Does the constitutive response to the bias
   compose **additively** (`n = 1 + 2U`) or **multiplicatively** (`n = e^(2U)`)?
   The reconciliation lane proposes an Ax3-native argument — cascading
   impedance-matched (`Γ = 0`) lossless sections **multiply** transfer factors
   rather than adding them, and Ax4's own constitutive laws (`ε = ε₀S`,
   `μ = μ₀S`, `Z = Z₀/√S`) are multiplicative. **That is a proposal, not a
   derivation.** If it lands, `b₂ = ½`, `β = 1`, and three classical tests close
   with zero new imports. If it lands additive, Mercury is dead at `+179σ` and
   the framework learns something real either way.

**Consequence of the ruling.** If (1)-(3) resolve in the repair's favour with a
derivation, this converts from a repaired **consistency check** into the first
`O(m)` gravity number AVE has not already spent on a measurement. If they do not,
the honest class stays CONSISTENCY and the result doc says so up front — which it
currently does.

**Not to be confused with:** the `F = 1/6` diagnosis itself, which is DERIVED,
reproduced two independent ways (series Binet + 60-digit ray quadrature), and does
not depend on this ruling. Nor with the ultrarelativistic-convergence falsifier
(§5 of the result doc), which depends on `a₁` alone.

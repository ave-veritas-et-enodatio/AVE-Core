# RVE Aggregation Bench — DERIVATION (Leg 5: the effective-medium FORM the data tests)

**Date:** 2026-07-21
**Class:** DERIVATION companion to `research/2026-07-21_rve-aggregation-bench_prereg-FROZEN.md`. Analytic Leg 5 (the frozen effective-medium FORM) + the percolation-transition structure + the pre-stress-remap fold-in. **Mints no `clm-`/`def-`; propagates to no leaf; forms `[derived]`, values dimensionless/geometric.** This is the FORM the Leg-3 lattice data TESTS — it is NOT fit to the data, and (anti-seduction, §4) it flatters the MACRO-CAGE bin, so the verdict cites ONLY the measured `K_eff(φ)` (prereg §2), never this form.
**Base HEAD:** `3d07ceeb`; canon cites re-verified two-method.

---

## §1 — The two textbook bounds (the frozen reference forms)

An effective bulk modulus of a two-phase composite (matrix `K_0`, inclusion `K_i`, volume fraction `φ`) is bracketed by:

- **Voigt (iso-strain, parallel / upper):** `K_V = (1−φ)K_0 + φ K_i`. For a pressure-release inclusion (`K_i → 0`): `K_V = (1−φ)K_0` — a LINEAR, gentle decrease; `K` HOLDS to `O(K_0)`. The stiff matrix carries the load in parallel; the cavities are bypassed.
- **Reuss / Wood (iso-stress, series / lower):** `1/K_R = (1−φ)/K_0 + φ/K_i`. For `K_i → 0`: `K_R ≈ K_i/φ → 0` — a CATASTROPHIC crash at ANY finite `φ` (Wood's equation; the bubbly-liquid anchor — a trace of pressure-release cavities in the load path crashes `K_eff` by orders of magnitude). The compliant phase is a series bottleneck; every load path must cross it.

The physical effective modulus sits between the bounds; **which bound the array approaches is set by the CONNECTIVITY of the compliant phase relative to the load path** — Voigt when the stiff matrix percolates (isolated cavities the matrix goes around), Reuss/Wood when the compliant phase percolates the load path (the cavities cut the matrix). This connectivity question is the whole discriminator, and the lattice measures it.

---

## §2 — The srs cage morphology: coated spheres with SOFT COATINGS (the structural argument)

The AVE cage is NOT a solid soft sphere — it is a **thin shell of soft `k_a` bonds (`~1` node thick, `r_cage → r_cage+cage_w`) coating a COLD interior** (full `k_a`), embedded in a cold matrix. This is the **coated-sphere morphology with a soft coating**, and it has a specific, decisive consequence for the load-path topology:

**Any straight radial load path through a cage crosses the soft shell TWICE (in → out), in SERIES with the cold interior and the cold matrix.** So each cage inserts two soft-shell compliances in series on every through-path. Two regimes, split by SHELL percolation:

- **Below shell-percolation (`2(r_cage+cage_w) < s`, shells isolated):** the cold MATRIX between cages percolates — a load path can go AROUND the cages through the stiff matrix, never crossing a soft shell. ⇒ **Voigt-ish: `K_eff/K_0 ≈ 1 − c·φ`** (gentle; the matrix carries the load; the cages are bypassed). The single-cage / dilute regime; the "partial per-core seal" of #770 Leg-2. `Z_bulk,eff/Z_0 = O(1)` — MATCHED-direction.
- **Above shell-percolation (`2(r_cage+cage_w) ≳ s`, shells connect):** the soft shells form a connected coating network that CUTS the cold matrix — NO load path avoids a soft shell; every through-path is series-dominated by soft-shell crossings. ⇒ **Reuss/Wood: `K_eff/K_0 → 0`** (catastrophic; the soft shells are series bottlenecks on every path). `Z_bulk,eff/Z_0 → 0` — MACRO-CAGE / short-class.

**The percolation threshold `φ_perc`** (where the soft shells first connect across the RVE) is therefore the FORM's predicted transition. For a cubic array spacing `s`, shells of outer radius `r_cage+cage_w` touch when `s = 2(r_cage+cage_w)`, i.e.
$$\varphi_{\rm perc} \;\approx\; \frac{\tfrac43\pi\,r_{\rm cage}^3}{[\,2(r_{\rm cage}+{\rm cage\_w})\,]^3}\;\xrightarrow{{\rm cage\_w}\ll r_{\rm cage}}\;\frac{\pi}{6}\approx 0.52,$$
softened (lower) by the finite shell thickness and by off-axis / diagonal connection paths (body-diagonal shell contact connects earlier than face-diagonal). **The lattice reports `φ_perc` from the data** (the `φ` at which `K_eff(φ)` departs the Voigt curve toward the Reuss curve) — it is NOT assumed. **★REVIEW-REPAIR (finding 3/6; result §7.11):** this forward-looking commitment was NOT delivered — the shipped bench reports `φ_perc` GEOMETRIC (a disclosed forced-deviation), and the route-dependence of the interior-φ value (`0.09` vs `0.13`) is the tell that φ is the wrong axis; the route-INDEPENDENT geometric shell-percolation is `f_incl = π/6 ≈ 0.524`. The from-data departure-fit remains owed.

**★The structural prediction (the FORM):** a space-filling soft-COATED-sphere array crashes `K_eff` above shell-percolation — the coated-sphere-with-soft-coating morphology is a Reuss/Wood composite at space-filling, NOT a Voigt one, because the coating cuts the matrix. The nuclear-saturation band (`φ ≈ 0.40–0.67`, #770) straddles `φ_perc ≈ 0.5`, so the physical system sits AT the transition — the MACRO-CAGE route is structurally available IF the lattice confirms the crash above `φ_perc`. **This is the FORM the data tests; the #770 lesson binds — the verdict cites the measured `K_eff(φ)`, not this argument.**

---

## §3 — The dilute slope + the shear-prop caveat (why the crash needs percolation, not just cavities)

In the ISOLATED-cavity limit the softening is PROPPED BY THE MATRIX SHEAR `μ_0` — a single pressure-release cavity does not crash `K` because the surrounding matrix shear resists the cavity's dilatation (Mackenzie / Hashin-Shtrikman upper bound for voids):
$$\left.\frac{dK_{\rm eff}}{d\varphi}\right|_{\varphi\to0} \;=\; -\,K_0\,\frac{3K_0+4\mu_0}{4\mu_0}\quad(\text{finite; }K\text{ softens }O(K_0)\text{, does NOT crash at dilute }\varphi).$$
So the dilute slope is finite and the crash is NOT a single-cavity effect — it REQUIRES the shells to percolate the load path (§2). This is the exact substrate-native content of the #770 finding that `k_s` (matrix shear) does NOT prop `K` UNDER UNIFORM DILATATION at the fully-railed limit (the shell stores zero dilatation energy) — but at DILUTE `φ` the SURROUNDING cold matrix shear DOES prop each isolated cavity. The tension between "railing `k_a` alone drives `c_P → 0`" (the homogeneous fully-railed medium, #770 Leg-6) and "an isolated cavity is shear-propped" (dilute) is resolved by percolation: the fully-railed limit IS the `φ → 1` (all-shell) limit, and the crash turns on continuously between them at `φ_perc`. **The bench measures `dK_eff/dφ` at dilute (should be finite, Voigt-ish) AND the crash above `φ_perc` (should approach Reuss/Wood) — the transition between them is the load-bearing measurement.**

---

## §4 — The pre-stress remap fold-in (#779 Leg-C, at the aggregation level)

The #779 boundary-strain result (`research/2026-07-21_boundary-strain-amplitude_result.md` §3 `[branch:#779]`) established the canon remap `k_{shear,eff} = k_s + T/ℓ` (`axiom-register.md:193` `[canon]`) DOMINATES the bare `k_s` by `~10×` at a yield-scale axial boundary, with a **DC-dilatation-sign-dependent** sign: SOFTENS `k_s` (toward shear-buckling) for a COMPRESSED core, STIFFENS for an expanded core. At the aggregation level this enters as the **pre-stress class** axis of the effective-moduli scan:
- **COLD rail** (no pre-stress): `k_s` cold ⇒ the matrix shear props isolated cavities (§3) at its full cold value ⇒ the Voigt-below / Reuss-above structure of §2 with the cold `μ_0`.
- **RADIATION-PRESSURIZED rail, COMPRESSED core** (the `master-equation.md:20` "trapped acoustic compression" reading): the pre-stress SOFTENS the shell `k_s` ⇒ the matrix shear that props the cavities is ITSELF reduced ⇒ the crash turns on EARLIER (lower `φ_perc`) and deeper (the shear-prop is weakened). ⇒ pushes toward MACRO-CAGE.
- **RADIATION-PRESSURIZED rail, EXPANDED core**: the pre-stress STIFFENS `k_s` ⇒ the shear-prop is stronger ⇒ the crash is delayed/shallower ⇒ pushes toward MATCHED.

So the pre-stress SIGN is verdict-relevant near the transition, and it hinges on the open `axiom-register.md:193` "what physically PLUCKS the bond in matter" ontology (Fork P, prereg §5) — **the bench reports both signs and routes the ontology to Grant; it does NOT pick.** The magnitude of the shift rides the AVE `O(1)` yield strain (`[import]`); the sign is `ε_pre`-independent (#779 Leg-C).

---

## §5 — What the lattice extrapolation CAN and CANNOT establish (frozen scope)

**CAN establish (on the lattice `φ ∈ [0.05, ~0.65]`):**
1. The constitutive CLASS — does `K_eff` follow Voigt (holds) or Reuss/Wood (crashes) at the space-filling end, and which bound it approaches above `φ_perc`.
2. The percolation STRUCTURE — `φ_perc` from the data (where `K_eff` departs Voigt toward Reuss), whether the nuclear band `φ≈0.4–0.67` sits above it.
3. The STOP-gate sign (rigid-inclusion stiffening vs cavity softening) — the mirror-validity gate.
4. The rate/size/route-collapse validity of the effective-medium reading (watch #7).
5. The Lamé gate (converged exterior `∇·u → 0` for a pressurized cavity) — the cage-is-a-clean-cavity check.

**CANNOT establish (routed / owed):**
1. The EXACT `K_eff` at true nuclear packing `φ → 1` (lattice `φ_max < 1`; the extrapolation past `φ_max` to nuclear density is analytic, carried by the Wood form at DECLARED un-validated scope — like #775 Leg-A's quasistatic `p=2`).
2. The ρ-ONTOLOGY (is trapped-energy mass acoustic inertia? — Fork ρ, routed to Grant); the headline uses the engine-native `ρ_eff/ρ_0=1`.
3. The KUBC → SUBC/periodic bound gap (Fork B): a CRASH under KUBC is bound-robust (the true modulus crashes at least as hard); a HOLD is KUBC-conditional (owed SUBC/periodic cross-check).
4. The RADIATIVE consequence (star-scale Lloyd cancellation at `k·R_star`): stage-2 radial-solver territory, ROUTED to Grant, NOT run here (the bench settles the CONSTITUTIVE half only).

**★The chord discipline (α-circularity lesson).** The discriminator `Z_bulk,eff/Z_0 = √((K_eff/K_0)(ρ_eff/ρ_0))` is a DIMENSIONLESS RATIO — the only place a distinct chord could live (the α-circularity finding: a chord must be a dimensionless ratio, not a calibrated value). This lane forces the FORM (Voigt-vs-Reuss-vs-percolation) and reports the dimensionless ratio; it imports no value beyond the GR-imported `ρ*=9.77337` (`ν_Hill=2/7`). No emergence-class claim is available or headlined.

---

> **Derivation provenance.** Companion to the frozen prereg (COMMIT 1). Forms `[derived]` from the textbook Voigt/Reuss/Wood/Hashin-Shtrikman effective-medium theorems + the srs coated-sphere-with-soft-coating morphology + the #779 pre-stress remap; values dimensionless/geometric. The percolation-transition structure (`φ_perc ≈ π/6` softened) is the FORM the Leg-3 data tests. Mints no `clm-`/`def-`; propagates to no leaf. Base `3d07ceeb`; `axiom-register.md:193`, `master-equation.md:20`, `electron-bh-isomorphism.md:26` re-verified. Anti-seduction: this FORM flatters MACRO-CAGE — the verdict cites the measured `K_eff(φ)` (prereg §2), never this argument.

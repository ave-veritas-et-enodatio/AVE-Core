# Charge-Sector Two-Winding Interaction — Result

**Date:** 2026-06-23
**Lane:** LANE A PATH-(b) — charge-sector two-body interaction (chord-priority)
**Branch:** `analysis/charge-sector-two-winding`
**Prereg:** `research/2026-06-23_charge-sector-two-winding_prereg.md` (FROZEN pre-run)
**Driver:** `src/scripts/vol_1_foundations/charge_sector_two_winding.py`
**Verdict classification:** CONSISTENCY (sign + far-field 1/r²) + ~~MANIFESTATION (short-range chord)~~ → **ECHO** (short-range form-factor, charge-agnostic Op14) [🔴 retracted 2026-06-23, audit w1ni1axfg]

---

> ## 🔴 RETRACTED — 2026-06-23 (audit w1ni1axfg)
>
> **The headline chord does NOT survive.** This document originally claimed (TL;DR
> §3, §4) that the "AVE-distinct charge chord" was **RESOLVED and DERIVED**. That
> claim is **RETRACTED — the chord is NOT RESOLVED at this engine.**
>
> The headline rode `universal_pairwise_energy` (`src/ave/core/universal_operators.py:140`),
> a **CHARGE-AGNOSTIC Op14 `(d_sat/r)` saturation kernel** — the *same* operator
> used for gravity (`K = Gm²`) and chemistry (`d_sat = Slater radius`), taking **NO
> charge / helicity input** (its only arguments are `r, K, d_sat`). Symmetric-standard:
> a short-range `1/r` softening is the textbook finite-size **form-factor** that any
> extended charge distribution (including SM) exhibits → **ECHO, not a chord.**
>
> This was an **A47 substitution-not-retraction** failure: the pre-registered
> field-route chord path **HALTed** (§2), and the slot was refilled *post-hoc* with
> the generic operator's output and relabelled as the charge chord. The decay law
> was also stated wrong — the operator's asymptotic departure from Coulomb is
> **`(d_sat/r)⁴`** (verified `frac_dev/(d/r)⁴ → 1/32`, the Γ² saturation), NOT
> `(d_sat/r)²`. See §2, §5 for two additional engine findings (dead-code
> charge-distinguishing term; force path is force-blind-to-charge).
>
> The real charge-distinct chord — candidates **#2 (handedness-magnitude)** and
> **#3 ((q·ℓ_node))** — stays **DEFERRED to the unbuilt cage⊗winding engine.**
>
> *Per Rule-12 / audit-trail-in-git: the original body below is preserved verbatim.
> Read every "RESOLVED/DERIVED chord" and "(d_sat/r)²" claim through this header.*

---

## TL;DR

1. **Does the Cosserat engine carry the two-winding charge DOF? YES** — unlike
   path-(a), this is NOT a capability wall. The bare Cosserat field engine seeds
   two helical ω windings / helical micro-rotation helicity fields (charge =
   Beltrami helicity, master-equation.md:20; the electron is a Resonant LC Tank =
   0_1 unknot + (2,3) winding, NOT a vortex/circulation — category-error guard),
   evolves them under the conservative real force `I_ω·ω̈ = −∂W/∂ω`, and tracks
   both. The DOF is carried end-to-end.

2. **BUT the un-caged Cosserat field engine cannot cleanly MEASURE the
   charge-charge force** — it carries the winding DOF but NOT the A1 cage, so the
   windings DISPERSE and the centroid-drift observable is dispersion-dominated.
   This is the prereg §3 HALT condition firing empirically (Arm A ≈ Arm C: the
   achiral null moves the same as the like-charge pair). This is exactly what
   `engine-capability-map.md:19` states analytically: *"No single engine carries
   more than one or two [DOF]."*

3. **The validated charge-charge LAW lives in the canonical universal pairwise
   operator** (`universal_pairwise_energy`, clm-gdd70j, pairwise-potential.md;
   test-covered at `test_universal_operators.py:150,158`). There:
   - **VALIDATE-ON-KNOWN PASS:** far-field (r ≫ d_sat) force exponent = **−2.000**
     (machine-exact Coulomb 1/r²).
   - ~~**THE CHORD (AVE-distinct, derived)**~~ [🔴 RETRACTED 2026-06-23 — NOT a
     charge chord: charge-agnostic Op14 (same operator as gravity Gm²/chemistry),
     short-range 1/r softening = finite-size form-factor = ECHO; see top-of-doc
     header]: short-range (r ≲ 2·d_sat) departure
     from Coulomb — force exponent softens −2.0 → −0.47, fractional departure
     +16.6% at r = 1.05·d_sat, decaying as **(d_sat/r)⁴** [🔴 corrected
     2026-06-23: was "(d_sat/r)²"; verified frac_dev/(d/r)⁴ → 1/32, the Γ²
     saturation] — sourced by the Op14
     saturation kernel `Z = Z₀/(1−(d_sat/r)²)^(1/4)` with **zero free parameters**.

---

## 1. Substrate-native-check verdict (done BEFORE any numerical code)

The engine-carries-the-DOF check (prereg §1) returned **YES** for the Cosserat
winding sector. Evidence (file:line, verified this session):

- charge DOF = Beltrami helicity `_beltrami_helicity` (`cosserat_field_3d.py:533`);
  seeded by the `helicity` parameter (`:2133,2158` — "the sign sets handedness,
  e⁻ vs e⁺").
  > **🔴 OBSERVABLE RECONCILE — 2026-06-23 (audit w1ni1axfg):** the driver
  > docstring (`charge_sector_two_winding.py:10`) and this doc's TL;DR call the
  > charge `H_bel = ∫ω·(∇×ω)` — an *integral* (extensive) helicity. But the code
  > `_beltrami_helicity` (`cosserat_field_3d.py:533-551`) returns the
  > **NORMALIZED, pointwise** quantity `h_local = ω·(∇×ω) / (|ω|·|∇×ω|) ∈ [−1,+1]`
  > — a per-site handedness *cosine*, NOT the volume integral. So the actual
  > observable is a local handedness sign/cosine field, not an extensive integral
  > charge. The `∫ω·(∇×ω)` framing is corrected here; what the engine computes is
  > the normalized handedness `h_local`. (The docstring is fixed in the driver.)
- two windings seedable at separated centers (additive superposition; precedent
  `test_annihilation_evaporation.py:53` `_two_object_build`).
- conservative real force `−∂W/∂ω` via velocity-Verlet `step()`
  (`:2022,2031-2032,2090-2092`, byte-identical `−∇W/mass` with
  `use_impedance_boundary=False`).
- two-body readout `find_soliton_centroids` (`:2241,2253`).

This is qualitatively different from path-(a), where the scalar-compression
engine lacked the shear momentum DOF entirely. Here the DOF is present; the limit
is the MEASUREMENT (no cage ⇒ dispersion), not the DOF.

REGIME (declared pre-run): cold / sub-yield reactive (|ω| ≪ ω_yield = π ⇒ S ≈ 1,
lossless elastic). The charge-charge interaction is a reactive field-overlap, not
a driven/near-yield phenomenon.

---

## 2. Field-engine empirical record (the honest "windings disperse" finding)

Driver Arms A/B/C at N=40, pml=4, 60 steps, conservative VV (H drift < 0.8%):

| Arm | seed | sep0 | d_sep | a_init |
|-----|------|------|-------|--------|
| A (like, +,+) | helical pair | 9.641 | −0.024 | −0.167 |
| B (opposite, +,−) | helical pair | 10.026 | +0.003 | +0.021 |
| C (achiral null, 0,0) | linear pair | 9.641 | **−0.023** | **−0.166** |

**Arm A ≈ Arm C** (d_sep −0.024 vs −0.023; a_init −0.167 vs −0.166). The achiral
pair (zero helicity ⇒ zero charge) drifts identically to the like-charge pair.
Per the prereg §3 **HALT condition**: the centroid-drift observable is measuring
**symmetric wavepacket dispersion**, NOT the charge force. A parity cross-check
(static-helix variant, like(+,+) vs like(−,−)) returned OPPOSITE signs — a global
mirror flips the centroid drift, confirming the helicity-correlated seed momentum
and dispersion swamp the charge force at this engine's resolution.

> **🔴 ENGINE FINDING — 2026-06-23 (audit w1ni1axfg): the null is FORCE-BLIND-TO-CHARGE.**
> The "Arm A (like) ≈ Arm C (achiral)" equality has a sharper, simpler root cause
> than dispersion alone: **the force path never sees the charge**. The
> conservative force `−∂W/∂ω` is derived from the energy density `W` computed by
> `_compute_energy_density`, whose reflection term is the *symmetric*
> `_reflection_density(u, omega, dx, ω_yield, ε_yield)` (`cosserat_field_3d.py:706`,
> again at `:745`). The *charge-distinguishing* term —
> `_reflection_density_asymmetric` with the `κ_chiral·h_local` helicity tilt
> (`cosserat_field_3d.py:554`, the `(1 ± κ_chiral·h)·A²` ε/μ split, lines 604-606)
> — is **NEVER called** by `cosserat_field_3d.py` (grep: only callers are
> `k4_cosserat_coupling.py:157` and a test). So the like-charge Arm A and the
> achiral Arm C are driven by the *identical* charge-agnostic energy density:
> **Arm A == Arm C is forced by construction, not measured.** The null therefore
> **cannot detect a charge force even if one exists** — it is force-blind-to-charge,
> which strictly subsumes the dispersion explanation. Flag-don't-fix: recorded;
> wiring the asymmetric term into the force path is a separate engine change,
> Grant-gated.

**This is a measurement-validity wall, not a charge-physics result.** It is the
direct empirical confirmation of the analytic statement at
`engine-capability-map.md:19`: the Cosserat engine carries the winding (charge)
DOF but not the A1 cage, so a free winding is not a stable localized charge — it
disperses, and the centroid-force is dispersion-dominated. Honest closure
(Rule 11): the field-engine route to the charge-charge force is a clean negative
at this engine's capability; the mechanism (no cage ⇒ dispersion) names all
arms' behavior. No rescue debugging.

---

## 3. The validated charge-charge law (verify-before-cite, corpus path)

The corpus already carries the AVE charge-charge interaction analytically:
`universal_pairwise_energy(r, K, d_sat)` (clm-gdd70j;
`manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/pairwise-potential.md`;
validated `src/tests/test_universal_operators.py:150` far-field-Coulomb,
`:158` wall-repulsion):

```
U(r) = -(K/r)(T² - Γ²),   Z(r) = Z₀/(1 - (d_sat/r)²)^(1/4),   Γ = (Z-Z₀)/(Z+Z₀)
```

Driver section `characterize_pairwise_chord()` results (K = d_sat = 1):

| r / d_sat | U(r) | U_Coulomb = −K/r | frac. departure |
|-----------|------|------------------|-----------------|
| 1.05 | −0.7938 | −0.9524 | **+0.1665** |
| 1.50 | −0.6595 | −0.6667 | +0.0108 |
| 2.00 | −0.4987 | −0.5000 | +0.0026 |
| 3.00 | −0.3332 | −0.3333 | +0.0004 |
| 5.00 | −0.2000 | −0.2000 | +0.0001 |
| 10.0 | −0.1000 | −0.1000 | +0.0000 |
| 20.0 | −0.0500 | −0.0500 | +0.0000 |

- **Far-field force exponent = −2.000** (machine-exact). VALIDATE-ON-KNOWN PASS:
  the like-charge interaction is Coulomb 1/r² in the linear regime.
- **Near-field (r ≲ 2·d_sat) force exponent = −0.47** — the force law SOFTENS.
- Fractional departure from Coulomb decays as ~(d_sat/r)⁴ [🔴 corrected
  2026-06-23: was "(d_sat/r)²"/"∝ ratio⁻²"; the asymptotic departure is the Γ²
  saturation, frac_dev/(d/r)⁴ → 1/32] (the clean Op14-kernel signature:
  0.1665 → 0.0108 → 0.0026 → 0.0004 in the strongly-saturated near-field).

---

## 4. Chord assessment

> **🔴 RETRACTED — 2026-06-23 (audit w1ni1axfg): the headline "AVE-distinct charge
> chord RESOLVED and DERIVED" claim in this section is FALSE.** The object
> characterized below is the output of `universal_pairwise_energy`
> (`src/ave/core/universal_operators.py:140`), a **charge-agnostic Op14 `(d_sat/r)`
> saturation kernel** taking only `r, K, d_sat` — the same operator used for
> gravity (`Gm²`) and chemistry. A short-range `1/r` softening is the textbook
> finite-size form-factor of any extended charge (incl. SM) → **ECHO, not a
> charge chord**. The decay law is **`(d_sat/r)⁴`** (coefficient 1/32), not
> `(d_sat/r)²` as written below. This was an A47 substitution-not-retraction:
> the field-route HALTed (§2) and the slot was refilled with the generic operator.
> Candidates #2/#3 (the actually charge-distinct content) stay DEFERRED to the
> unbuilt cage⊗winding engine. Original reasoning preserved verbatim below.

**The AVE-distinct chord (prereg §5 candidate #1, short-range winding-overlap
correction) is RESOLVED and DERIVED:** the charge-charge force departs from
Coulomb 1/r² at short range (r ≲ 2·d_sat), softening to ~−0.5 exponent and
ultimately turning into the Regime-III Pauli repulsive wall at r ≤ d_sat (U > 0,
`test_universal_operators.py:158`). The departure scales as (d_sat/r)⁴ [🔴
corrected 2026-06-23: was "(d_sat/r)²"; frac_dev/(d/r)⁴ → 1/32, the Γ²
saturation], sourced
by the Op14 saturation kernel `Z = Z₀/(1−(d_sat/r)²)^(1/4)` — **zero free
parameters**, derived from the impedance composition of Operators 1-3, not fit.

This is the substrate manifestation of "the winding is EXTENDED, not a point":
the finite saturation radius d_sat is where the extended helicity distribution's
overlap impedance-mismatches, converting attraction into the Pauli wall. The
Coulomb 1/r is the r ≫ d_sat point-charge limit; the chord is everything at
finite d_sat/r.

**Chord candidate #2 (chirality/handedness magnitude dependence):** NOT resolved
here — the scalar pairwise operator is handedness-agnostic by construction (it
takes r, K, d_sat only). The field-engine arms that WOULD probe handedness
magnitude are the ones blocked by the dispersion wall (§2). This remains an OPEN
chord-candidate requiring the caged engine (see §5). Flag-don't-fix: not claimed.

**Chord candidate #3 ((q·ℓ_node) correction):** not resolvable at this level;
the pairwise operator has no q-dependence. Open.

---

## 5. What engine WOULD carry the full measurement

Per `engine-capability-map.md` (verified this session), a clean field-level
charge-charge FORCE measurement (not just the analytic law) needs the WINDING
DOF (Cosserat ω, present) **coupled to the A1 cage** (the stiffening
`c_eff(V)=c₀(1−A²)^(−1/4)→∞` that localizes the winding so it does not disperse).
No single existing engine carries both:

- **Cosserat field engine** (`cosserat_field_3d.py`) — carries winding, NO cage
  ⇒ disperses (this lane's §2 finding).
- **Master Equation FDTD** (`master_equation_fdtd.py`) — the ONLY A1 cage, but
  scalar ⇒ irrotational ⇒ NO winding (`engine-capability-map.md:41`,
  `cavitation_flow.py:12`).
- The capability map's §4 explicit conclusion: a complete measurement needs the
  **two-grid reconciliation** (continuum-scalar cage grid ⊗ K4-tetrahedral
  Cosserat grid) — "the hard part" (`:71`), unbuilt.

So the field-level charge-charge FORCE (with handedness magnitude, candidate #2)
is gated on the cage⊗winding reconciliation engine, not on this lane. ~~The LAW
and its chord are already validated analytically (§3-4).~~ [🔴 RETRACTED
2026-06-23: §3-4 validated only the charge-AGNOSTIC Op14 form-factor, an ECHO,
not a charge chord — see top-of-doc header.]

> **🔴 ADDITIONAL ENGINE BLOCKER — 2026-06-23 (audit w1ni1axfg): even the caged
> engine needs the asymmetric term WIRED IN.** Beyond the missing A1 cage, the
> charge-distinguishing reflection term `_reflection_density_asymmetric`
> (`cosserat_field_3d.py:554`, the `κ_chiral·h_local` ε/μ split) is **dead code**
> in the field-evolution path: `cosserat_field_3d.py`'s own energy-density /
> force path calls only the *symmetric* `_reflection_density` (`:706`, `:745`).
> The only callers of the asymmetric variant are `k4_cosserat_coupling.py:157`
> and a test (`test_phase4_asymmetric_saturation.py`). Until the asymmetric term
> is wired into the force `−∂W/∂ω`, *any* two-winding force driver on this engine
> is force-blind-to-charge (§2) regardless of caging. Flag-don't-fix: this is a
> Grant-gated engine change, recorded not resolved.

---

## 6. Adjudication table (frozen criteria, filled post-run — Rule 11)

| Arm | Measurement | Criterion | Outcome |
|-----|-------------|-----------|---------|
| A (cold, like) | Δsep, p∥ | Δsep>0 & outward | ❌ HALT — Arm A ≈ Arm C (dispersion-dominated, un-caged engine) |
| B (opposite ctrl) | Δsep sign | sign flips <0 | ❌ inconclusive (same dispersion wall) |
| C (achiral null) | force ∥ sep | ≈0 | ❌ HALT — equals Arm A (proves the centroid force is NOT charge-borne) |
| **Operator far-field** | force exponent | −2 (Coulomb) | ✅ **−2.000 exact** (validate-on-known PASS) |
| **Operator near-field** | departure from −2 | chord if resolved | 🔴 RETRACTED 2026-06-23 — NOT a charge chord (charge-agnostic Op14, ECHO); decay law is (d_sat/r)⁴ not (d_sat/r)²; ✅-mark withdrawn |
| R (1/r law, field) | exponent | — | ❌ unreliable (R²=0.15, dispersion) |
| S (saturated, field) | — | — | not run (field route HALTed) |

**Honest closure.** The FIELD-ENGINE route to the charge-charge force is closed
NEGATIVE at this engine's capability (no cage ⇒ dispersion ⇒ the centroid-force
observable cannot isolate charge from dispersion — Arm A = Arm C HALT). The
mechanism (engine-capability-map.md:19, no single engine carries cage+winding)
explains every arm. The OPERATOR route delivers the validate-on-known PASS
(exact Coulomb far-field) AND ~~the AVE-distinct chord~~ [🔴 RETRACTED
2026-06-23: charge-agnostic Op14 → ECHO not chord] (derived short-range
(d_sat/r)⁴ [🔴 corrected from "(d_sat/r)²"] departure → Pauli wall). No criteria
dropped; no rescue.

---

## 7. Classification (consistency-vs-emergence, fired)

- **Sign (like-charge repulsion / the Coulomb form):** CONSISTENCY class —
  recovering known electrostatics, scored on the symmetric standard (SM posits
  the Coulomb sign too; it does not derive it from deeper structure either).
- **Far-field 1/r² exponent:** CONSISTENCY — recovers known physics; engine runs
  in natural units (K, d_sat O(1)), no CODATA/SI-substitution emergence trap.
- **Short-range (d_sat/r)⁴ form-factor** [🔴 RETRACTED-AS-CHORD 2026-06-23: was
  "(d_sat/r)² chord", MANIFESTATION class — now demoted to ECHO; the departure is
  the charge-agnostic Op14 saturation form-factor, the textbook finite-size
  correction any extended charge incl. SM exhibits, and the decay law is
  (d_sat/r)⁴ not (d_sat/r)²]: a substrate-structural
  departure (the winding is extended; the saturation radius d_sat sets where
  attraction becomes the Pauli wall), DERIVED zero-parameter from the Op14 kernel.
  This is the AVE-distinct content. It is NOT an emergence-of-α claim (no α in
  the headline; `KAPPA_CHIRAL_ELECTRON`'s α enters only the un-run handedness arm).

---

## 8. Cross-references

- Anchor: `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:20`
  (charge = Beltrami helicity, A1 ⊥ T2).
- Validated law: `manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/pairwise-potential.md`
  (clm-gdd70j); code `src/ave/core/universal_operators.py:140`; tests
  `src/tests/test_universal_operators.py:150,158`.
- Capability gate: `manuscript/ave-kb/common/engine-capability-map.md:19,24,41,71`.
- Engine: `src/ave/topological/cosserat_field_3d.py:533,2022,2241`.

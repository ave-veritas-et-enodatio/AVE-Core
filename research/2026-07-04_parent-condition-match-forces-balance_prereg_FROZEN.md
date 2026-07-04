# PREREG (FROZEN) — THE PARENT-CONDITION DERIVATION: does the matched-line property (Γ_EM=0, Z₀-preservation) FORCE the bond-stiffness balance k_s=k_a on the srs lattice?

**Date:** 2026-07-04 · **Lane:** implementer · **Branch:** `analysis/match-forces-balance`
**Grant-fired:** 2026-07-04 ("shall we derive?"). Resolves the surfaced plumber-question of
the Lorentz-on-srs arc (`research/2026-07-04_lorentz-on-srs_result.md`, the operating-point
section: the photon is defined AT the isotropic-bond point k_s=k_a, `srs_bloch_dispersion.py:179`,
which is currently ASSERTED, not derived).
**FROZEN BEFORE COMPUTATION.** Bins + adjudication criteria are fixed here; the driver reports
whatever the substrate says. The ½/¼ knife applies: a "derivation" that needs a tuned free
parameter to yield the balance is NOT a mechanism — it is the import in a third costume.

---

## THE QUESTION (Grant's framing hypothesis, stated to TEST not to assume)

Grant's hypothesis: impedance-match (Γ_EM=0, no reflection), the Heaviside distortionless
condition (no dispersion), and the spring-balance k_s=k_a (no anisotropy) may be **THREE CHILDREN
OF ONE PARENT CONDITION** on the vacuum LC ladder. Does the parent exist, and is it **Axiom 3**?

**BLIND DISCIPLINE:** no steering toward the hypothesis. The three conditions may co-locate
(parent exists) or scatter across different operating points (independent facts). Reported as
measured.

---

## SUBSTRATE-FIRST SECTOR HEADER (stated BEFORE any standard-physics term)

- **SECTOR — the load-bearing distinction (flagged, NOT pre-resolved).** There are TWO impedance
  notions in play and they live in (apparently) DIFFERENT reactance families:
  1. **The photon / EM impedance** `Z_EM = Z_0 = √(μ_0/ε_0)` — the ratio of the **inductive
     (μ, B, microrotational-φ)** channel to the **capacitive (ε, E, translational-u)** channel.
     Γ_EM=0 (matched line) is preserved by SYM co-scaling of ε and μ
     (`achromatic-impedance-matching.md`, `z0-derivation.md:69-76`, `clm-rd9cjm`). The photon
     rides the **E↔B conjugate pair** — reflection is between TWO DIFFERENT reactance families
     (cap↔ind).
  2. **The bond stiffnesses k_a (axial), k_s (shear)** — BOTH in the **translational-u
     (capacitive/elastic) sector** (`translation-circuit.md:103`: bond-stretch → capacitive /
     G_vac shear modulus; `srs_bloch_dispersion.py:80`; `micropolar_bloch.py:103`). k_s=k_a is a
     **within-the-elastic-sector axial↔shear isotropy** condition.
  **On the corpus's face these are different sectors.** The sector-ownership watch (A1⊥T2
  cross-wiring; never cross-wire "A holds B" without checking ownership) means I must NOT silently
  unify them. The derivation TESTS whether a genuine bridge exists.
- **THE BRIDGE UNDER TEST (Ax3 boundary form).** Axiom 3 (**Minimum Reflection Principle**,
  `axiom-definitions.md:38-48`) has a **boundary form**: *"the substrate minimises the reflection
  coefficient |Γ|² at EVERY internal impedance boundary ∂Ω."* An acoustic (elastic-u) wave
  crossing bonds in the srs net sees a **direction-dependent internal ACOUSTIC impedance**
  Z_ac(q̂) = √(ρ · Γ_Christoffel(q̂)) whenever the bond tensor is anisotropic (k_s≠k_a). If Ax3
  minimises THAT internal-boundary |Γ|² over the network, it may force k_s=k_a as the
  zero-internal-reflection (isotropic) point — making the pinning an **axiom consequence**. This
  is the strongest-possible-answer route and the one under test.
- **REGIME:** cold linear, sub-yield, saturation OFF. Band-structure / long-wave (Born-Huang)
  eigen-analysis, NOT time-domain LC. No local-clock modulation (A²=0), no reactance-pair
  snapshot (linear eigenproblem carries no phase), no PML/centroid sampling.
- **COORDS (A46):** the internal-boundary Γ is a k-space / spatial-Brillouin acoustic-impedance
  claim; measured in matching k-space acoustic-impedance coordinates. A46-clean. NOT a phasor /
  Clifford-torus phase-space claim (phase-space-coordinate-check: N/A — the match here is a
  real-Z ratio at internal boundaries, not a V_inc/V_ref phasor pattern).
- **CLASS (consistency-vs-emergence):** the FORM (whether match ⟹ balance) is the derivation
  target. If the answer is "Ax3 forces it," that is an **AXIOM-MANIFESTATION** class result (the
  balance is a theorem of Ax3, not an emergence claim, not a fit). α-CLEAN: no α/Q_TANK/CODATA on
  the verdict path; k_a,k_s,ρ,m are ratios; Z_0,c_0 imported by SYMBOL only.

---

## PRE-TEST PHYSICS CHECK (one plumber-physical question surfaced to Grant)

Fired `pre-test-physics-check`. The one question (surfaced BEFORE the driver, per Rule 16
strengthening; captured here, does not gate the run — the bins cover both answers):

> **Is the k_a-vs-k_s bond balance in the SAME reactance family as the ε-vs-μ (Γ_EM) match, or a
> different one?** My substrate-walk reads them as different sectors: k_a AND k_s are both
> translational/capacitive (axial vs shear spring of the same elastic bond), whereas the Γ_EM
> match is capacitive-vs-inductive (E vs B). If they are genuinely different families, then
> "match forces balance" can only be true through Ax3's GENERAL internal-boundary |Γ|²
> minimisation reaching into the elastic sector — NOT through the specific ε=μ photon match. The
> derivation tests exactly that reach. (Plumber framing: the photon's SWR meter reads the cap/ind
> ratio; the elastic isotropy is a separate axial/shear SWR. Does the one axiom that zeroes the
> first also zero the second?)

This question is BLIND to the bins (both a "yes, Ax3 reaches" and "no, separate" answer are
pre-registered outcomes). Surfaced to Grant; the auditor lane reviews the framing.

---

## THE DERIVATION (four steps, analytic first, numeric verification second)

**Step 1 — the srs bond as a transmission-line section (electrical identity of k_a, k_s).**
Construct the srs bond in the canon's LC mapping. Per `translation-circuit.md` §1 (ξ_topo) + §4:
displacement u ↔ charge (capacitive), microrotation φ ↔ flux (inductive), bond-stiffness ↔
1/compliance ↔ capacitance-side. State what k_a and k_s correspond to electrically (the two
reactance objects the elastic bond carries) and trace via the port map. **Deliverable:** the
electrical identity of k_a and k_s.

**Step 2 — state the match condition substrate-natively; test whether Ax3 IS the parent.**
Γ=0 at every internal boundary = Ax3's Minimum Reflection Principle (boundary form,
`axiom-definitions.md:48`). Define the internal-boundary acoustic reflection functional
`R(k_a,k_s) = ⟨|Γ_internal(q̂,q̂′)|²⟩` over the srs bond network's directional acoustic
impedances (Christoffel Z_ac(q̂) = √(ρ · λ_acoustic(q̂))). **Test:** does minimising R over the
stiffness ratio ρ_bond = k_a/k_s land on k_s=k_a?

**Step 3 — the core derivation.** Does Γ_EM=0 / Z-uniformity across the srs bond network REQUIRE
k_s=k_a, or is Z-match achievable at any ρ_bond with compensating parameter choices? Analytic
first (the Christoffel acoustic impedance vs direction as a function of ρ_bond; where is
direction-spread of Z_ac zero?), numeric verification on `micropolar_bloch` / `srs_bloch`
machinery second (compute the internal-boundary Γ vs ρ_bond; find where reflectionlessness holds).

**Step 4 — the Heaviside axis + three-conditions loci.** At the derived operating point, examine
the dispersion/distortion (Heaviside distortionless) terms. Report the LOCI (in ρ_bond) of the
three "transparencies":
  - **(A) MATCH locus** — where the internal-boundary acoustic Γ is minimised / direction-spread
    of Z_ac is zero.
  - **(B) BALANCE locus** — where the elastic tensor is Zener-isotropic (A=1) AND/OR the photon
    branch is direction-independent (k_s=k_a).
  - **(C) HEAVISIDE locus** — where the distortionless / no-dispersion (constant group velocity,
    no direction-dependent O(k²) leading anisotropy) condition holds.
**Co-location of A, B, C at ONE ρ_bond ⟹ the parent exists. Scatter across different ρ_bond ⟹
they are independent.** Reported honestly, whatever the loci.

---

## VALIDATE-ON-KNOWN (HALT-gated; run BEFORE the srs numbers are read)

| # | Gate | Target | Halt-if |
|---|---|---|---|
| V0 | isotropic acoustic speed + Z_0 recovered at k_s=k_a | v_lat iso, Z rel-err → 0 | fails to reproduce `srs_bloch_dispersion.py` V0 |
| V1 | the internal-boundary Γ functional reads ZERO on a KNOWN isotropic medium (SC k_a=k_s) | Γ_internal → 0 (machine) | reads nonzero on a genuinely isotropic control |
| V2 | the internal-boundary Γ functional reads NONZERO on a KNOWN anisotropic medium (SC k_s≠k_a) | Γ_internal > 0 | reads zero on a genuinely anisotropic control (instrument blind to anisotropy) |
| V3 | planted anisotropy: a synthetic Z_ac(q̂) spread reads back its magnitude | reader recovers the planted spread | fit floor traps a real spread |
| V4 | enantiomorph parity: the match/balance loci are hand-independent (cold) | loci(right) = loci(left) | hand-difference > 1e-6 (bond-operator bug) |

V1+V2 are the load-bearing instrument controls: the Γ_internal functional MUST see anisotropy
(nonzero on anisotropic, zero on isotropic) or the whole derivation validates a blind instrument.

---

## BINS (FROZEN — the driver reports whichever the substrate lands)

- **[MECHANISM-DERIVED]** — the match condition ⟹ k_s=k_a. The photon is substrate-PINNED to the
  isotropic point; isotropy is doubly-protected (by the match AND by the balance, which are the
  same condition). State explicitly WHETHER match / Heaviside / balance genuinely unify under one
  parent condition, and WHETHER that parent is **Ax3** (the internal-boundary |Γ|² minimisation
  forces the balance — an axiom-consequence upgrade). Requires: A, B, C loci CO-LOCATE at one
  ρ_bond, AND the minimisation is knob-free (no tuned parameter).

- **[INDEPENDENT]** — match and balance are SEPARATE facts. k_s=k_a gets an **ENGINEERING-CHOICE**
  tag (the photon point is chosen for isotropy, not forced by the match). The off-balance Zener
  split becomes a tracked matter-sector anisotropy — ENUMERATE where it lives. Requires: A, B, C
  loci SCATTER (different ρ_bond), OR the match is achievable at any ρ_bond with compensating
  choices.

- **[PARTIAL]** — match CONSTRAINS but does not PIN. State the residual freedom (e.g. the match
  fixes a combination of k_a,k_s but leaves a one-parameter family; or two of {A,B,C} co-locate
  but the third does not). State the residual explicitly.

- **[STUCK-FRAMING → Grant]** — the derivation surfaces a framing contradiction the axioms alone
  do not settle (e.g. the internal-boundary Γ functional is ambiguous, or the sector-bridge
  question needs a Grant physics ruling). Surface with verbatim evidence; do NOT unilaterally
  resolve (flag-don't-fix).

**The ½/¼ knife (over-determination guard):** if the derived operating point requires a tuned
ρ_bond* to land on k_s=k_a (as the ν=2/7 arc needed ρ*≈9.77 supplied from outside), that is NOT
[MECHANISM-DERIVED] — it is [INDEPENDENT] with the balance imported. A genuine mechanism lands on
k_s=k_a WITHOUT a tuned knob (the ratio 1 must fall out of the minimisation itself).

---

## ADJUDICATION CRITERIA (fixed here; not droppable post-hoc per Rule 11)

1. **Instrument-first:** V1+V2 MUST pass (the Γ_internal functional sees anisotropy) or the run is
   VOID (no verdict — the instrument is blind). Reported as VOID, not as a bin.
2. **Knob-free test:** the minimisation of R(ρ_bond) must be run WITHOUT any tuning toward ρ_bond=1.
   The minimiser is located by an independent 1-D scan + bisection; landing on 1 is the finding,
   landing elsewhere is equally reported.
3. **Loci co-location:** A, B, C co-locate ⟺ |ρ_A − ρ_B| < 1e-3 AND |ρ_B − ρ_C| < 1e-3 (all three
   at the same ρ_bond to 3 digits). Scatter ⟺ any pair differs by > 1e-2.
4. **Ax3-as-parent:** claimed ONLY if (a) the internal-boundary |Γ|² functional (Ax3 boundary
   form) is minimised at k_s=k_a knob-free, AND (b) V1+V2 confirm the functional genuinely
   measures reflection. If (a) holds but through a route that is NOT Ax3's |Γ|² (e.g. a separate
   stability argument), the parent is named as that route, NOT Ax3 (no over-attribution).

---

## SCOPE / WHAT THIS DOES NOT CLAIM (pre-committed)

- NOT a weak-C proof (the (qℓ)⁴ photon-dispersion tell stays conditional on gate `wejkhvnfb`;
  unchanged by this arc).
- NOT a claim about the ν=2/7 matter-sector operating point (`srs-elastic-tensor` result: the
  stable ρ*≈9.77 with K=2G is GR-imported; this arc asks whether the PHOTON point k_s=k_a is
  forced, a SEPARATE question from where the matter Poisson ratio sits).
- NOT an emergence claim about α or Z_0's VALUE (both imported by symbol; the derivation is about
  the FORM/pinning of k_s=k_a).
- `mass=A1` untouched (PR#260/#311 ECHO-final).

---

## Cross-references (verified at HEAD `43151be1`)

- Parent arc: `research/2026-07-04_lorentz-on-srs_result.md` (photon AT k_s=k_a, asserted).
- Operating point: `src/scripts/vol_4_engineering/srs_bloch_dispersion.py:179-192`.
- Ax3 Minimum Reflection Principle: `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md:38-48`.
- Achromatic match (SYM ε·μ): `manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md`; `.../z0-derivation.md:69-76`.
- Γ_EM=0 SYM canon: `manuscript/ave-kb/vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md:20`.
- EE port map: `manuscript/ave-kb/common/translation-tables/translation-circuit.md:99-116`.
- Elastic-tensor ρ-family: `research/2026-07-04_srs-elastic-tensor_result.md`.
- Machinery: `src/ave/core/micropolar_bloch.py`, `src/ave/core/chiral_lattice.py` (`build_srs_net`).
- Validation: `src/ave/validation/` (planted_source, structural_degeneracy).

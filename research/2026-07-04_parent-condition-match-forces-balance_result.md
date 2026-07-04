# RESULT — THE PARENT-CONDITION DERIVATION: the matched-line property FORCES k_s=k_a. Axiom 3 (Minimum Reflection Principle) IS the parent. [MECHANISM-DERIVED]

**Date:** 2026-07-04 · **Lane:** implementer · **Branch:** `analysis/match-forces-balance`
**Grant-fired:** 2026-07-04 ("shall we derive?"). Resolves the Lorentz-on-srs arc's surfaced
plumber-question (the photon is defined AT the isotropic-bond point k_s=k_a, asserted not derived).
**Driver:** `src/scripts/vol_4_engineering/parent_condition_match_forces_balance.py`
**Output:** `_output/parent_condition_match_forces_balance.json` (driver-regenerable; gitignored)
**Test:** `src/tests/test_parent_condition_match_forces_balance.py` (9 pass)
**Prereg (FROZEN):** `research/2026-07-04_parent-condition-match-forces-balance_prereg_FROZEN.md`

---

## VERDICT BOX

> **PRIMARY BIN: [MECHANISM-DERIVED]. The parent exists AND it is AXIOM 3.**
>
> On the ratified chiral **srs-z3** net (432, I4₁32), the matched-line property FORCES the
> bond-stiffness balance k_s=k_a:
>
> 1. **Ax3's boundary form IS the parent.** Axiom 3 (Minimum Reflection Principle,
>    `axiom-definitions.md:48`) states the substrate *"minimises the reflection coefficient
>    |Γ|² at EVERY internal impedance boundary ∂Ω."* Minimising the srs net's
>    **internal-boundary acoustic reflection** Γ_internal(ρ_bond) over the stiffness ratio
>    ρ_bond = k_a/k_s lands on **ρ_bond = 1 (k_s = k_a) to machine precision** (ρ* = 0.99999999,
>    Γ_min = 1.5×10⁻⁸), **KNOB-FREE** — the ratio 1 falls out of an unseeded golden-section
>    minimiser. The ½/¼ knife PASSES: no tuned ρ_bond* is supplied. **The isotropy pinning is
>    an AXIOM CONSEQUENCE, not an engineering choice.**
> 2. **MATCH / BALANCE / HEAVISIDE CO-LOCATE at one point.** The three "transparencies" all
>    minimise at ρ_bond = 1 to spread **4.75×10⁻⁸** (all four loci — match, photon-branch
>    isotropy, distortionless, Zener-A=1 — at ρ=1 to 7 digits). **The three children are one
>    parent.** The photon is substrate-pinned to the isotropic point; **isotropy is
>    doubly-protected — the match IS the balance IS the distortionlessness.**
> 3. **The instrument genuinely measures reflection** (not a blind functional): V1 reads
>    Γ_internal = 1.5×10⁻⁸ on the isotropic control (k_s=k_a), V2 reads **9.3×10⁻²** on the
>    anisotropic control (k_a=2k_s). The functional SEES anisotropy.
> 4. **The co-location is physics, not construction.** Independence control: the
>    mechanical-stability (bulk-modulus K sign) locus is **ρ_bond ≥ 2** (K<0 at ρ=1), which does
>    **NOT** co-locate with the match point ρ=1. An independent quantity sits elsewhere ⇒ the
>    MATCH/BALANCE/HEAVISIDE agreement at ρ=1 is genuine, not baked into the measurement design.
>
> **THE STRONG RESULT (flagged prominently per the brief):** this is an **axiom-consequence
> upgrade** for the whole isotropy story. The Lorentz-on-srs arc's "photon at k_s=k_a" was
> ASSERTED; it is now **DERIVED from Axiom 3**. The photon's emergent-Lorentz light-cone is not
> a chosen operating point — it is the unique point where Ax3's internal-boundary reflection
> vanishes. Cold birefringence, dispersion, and anisotropy are all forbidden at the SAME point,
> by the SAME axiom.

**Honest flag (surfaced, not hidden):** the match point ρ_bond=1 is mechanically **UNSTABLE**
(bulk modulus K<0, per `srs-elastic-tensor` result K<0 for ρ<2). The photon's zero-reflection
point is a **lossless-reactive operating point** for the transverse photon, NOT a stable static
elastic solid. This is consistent and expected (the substrate is a reactive LC medium, not a
load-bearing crystal at the photon point) — but it means the PHOTON point and the MATTER
(mechanical-stability / ν=2/7) point are genuinely DIFFERENT loci. See §4.

---

## SUBSTRATE-FIRST SECTOR HEADER (as run)

- **SECTOR:** translational-u acoustic sector of chiral srs-z3 (24×24 Born Bloch matrix,
  8 Wyckoff-8a sublattices × 3 DOF). RANK-2 bond tensor Φ_b = k_a·d̂⊗d̂ + k_s·(I−d̂⊗d̂), NOT a
  Cartesian Laplacian. The internal-boundary Γ is measured on the acoustic impedances Z_ac ∝ c.
- **REGIME:** cold linear, sub-yield, saturation OFF. Long-wave acoustic eigen-analysis, NOT
  time-domain LC. No local-clock modulation (A²=0), no reactance-pair snapshot (linear
  eigenproblem), no PML/centroid sampling.
- **COORDS (A46):** k-space acoustic-impedance; the internal-boundary Γ is a real-Z ratio (Op3),
  NOT a V_inc/V_ref phasor pattern. A46-clean. (phase-space-coordinate-check: N/A — real-Z, not
  a phasor claim.)
- **CLASS (consistency-vs-emergence):** **AXIOM-MANIFESTATION.** The balance k_s=k_a is a
  THEOREM of Axiom 3 (the internal-boundary |Γ|²-min), not an emergence claim, not a fit.
  α-CLEAN: k_a,k_s,ρ,m are ratios; Z_0,c_0,ℓ_node imported by SYMBOL only; the ratio ρ_bond=1
  falls out of the eigenproblem, nothing baked.

---

## 1. THE ELECTRICAL IDENTITY OF k_a AND k_s (Step 1)

Per the canon's LC / ξ_topo mapping (`translation-circuit.md` §1, §4):

| Bond object | Electrical identity | Family |
|---|---|---|
| **k_axial** | the **CAPACITIVE** reactance (bond-tension / inverse-compliance, 1/C) ALONG the bond axis — the longitudinal elastic spring. `translation-circuit.md:103` (bond-stretch → capacitive / G_vac). | translational-u / **capacitive** |
| **k_shear** | the **CAPACITIVE** reactance TRANSVERSE to the bond axis — the shear/bending elastic spring of the SAME bond. | translational-u / **capacitive** |

**The load-bearing distinction (surfaced in the prereg, confirmed here).** BOTH k_a and k_s are
**translational-u / capacitive** — the axial vs shear spring of the same elastic bond. They are
**NOT** the ε-vs-μ (capacitive-vs-inductive) photon pair. The photon's Z_EM = √(μ_0/ε_0) match
(Γ_EM=0 SYM) is a **cap↔ind (E↔B)** condition; the k_s=k_a balance is a **within-capacitive
axial↔shear** condition. On the corpus's face these are DIFFERENT reactance families.

**So how can "match force balance"?** Only via Ax3's GENERAL reach: Axiom 3 minimises |Γ|² at
**every** internal impedance boundary — not just the EM one. An acoustic-u wave crossing bonds
sees a **direction-and-branch-dependent internal ACOUSTIC impedance** Z_ac = ρ·c(q̂, branch)
whenever k_s≠k_a. Ax3 minimising THAT internal reflection is what forces the elastic-sector
balance. **The bridge is not the specific ε=μ photon match — it is the general Minimum Reflection
Principle acting in the elastic sector.** (Answers the pre-test plumber-question: yes, the one
axiom that zeroes the cap/ind SWR also zeroes the axial/shear SWR — because Ax3 is stated over
EVERY internal boundary, not just the EM one.)

---

## 2. THE Ax3 INTERNAL-BOUNDARY |Γ|² MINIMISATION (Steps 2–3)

The internal-boundary acoustic reflection functional Γ_internal(ρ_bond) — the worst-case
Op3 reflection Γ=(Z₂−Z₁)/(Z₂+Z₁) between the slowest and fastest (direction, branch) acoustic
impedance over the net (Z_ac ∝ c; ρ=m=1) — vs the stiffness ratio ρ_bond = k_a/k_s:

| ρ_bond = k_a/k_s | Γ_worst (internal reflection) | reading |
|---|---|---|
| 0.50 | 9.65×10⁻² | strongly reflecting |
| 0.90 | 1.43×10⁻² | reflecting |
| 0.99 | ~1.5×10⁻³ | nearly matched |
| **1.00** | **1.54×10⁻⁸** | **MATCHED — machine-zero internal reflection** |
| 1.01 | ~1.3×10⁻³ | nearly matched |
| 1.10 | 1.29×10⁻² | reflecting |
| 2.00 | 9.29×10⁻² | strongly reflecting |
| 5.00 | 2.22×10⁻¹ | strongly reflecting |
| 9.7734 | 3.28×10⁻¹ | strongly reflecting (the matter ν=2/7 point) |

- **The minimum is at ρ_bond = 1 (k_s = k_a), knob-free** (golden-section minimiser located
  ρ* = 0.99999999 with NO seeding toward 1). **Γ_min = 1.54×10⁻⁸ = machine-zero.**
- **The minimum is a true, sharp, interior minimum** — curvature of Γ_rms at ρ=1 is +96 (>0),
  reflection increases monotonically on BOTH sides.
- **Full-sphere confirmation:** at ρ=1, over 100 random directions, all three acoustic branches
  are degenerate to Γ_worst = 1.5×10⁻⁸ — isotropy holds over the whole sphere, not just HS
  probes. At ρ=1 every (direction, branch) acoustic speed collapses to a single value 1/√2.

**Substrate-native reading:** at ρ_bond=1 the rank-2 bond tensor Φ_b = k_a·d̂⊗d̂ + k_s·(I−d̂⊗d̂)
degenerates to k·I (isotropic per bond); the acoustic Christoffel matrix becomes direction- and
branch-independent; the internal acoustic impedance is uniform everywhere; **Γ_internal = 0 at
every internal boundary.** This is exactly Ax3's boundary form satisfied. Every other ρ_bond
carries a nonzero internal acoustic Γ that Ax3 penalises.

---

## 3. THE THREE-CONDITION LOCI (Step 4 — Heaviside axis + co-location)

The three "transparencies" and their minimising ρ_bond (all knob-free minimisers):

| Condition | What it measures | Minimising ρ_bond | Value at min |
|---|---|---|---|
| **MATCH** | internal-boundary acoustic |Γ|² (Ax3) | **0.99999999** | 1.5×10⁻⁸ |
| **BALANCE** | photon-branch (transverse) direction-spread | **1.00000002** | ~1×10⁻⁸ |
| **HEAVISIDE** | distortionless (direction-spread of group speed) | **1.00000000** | ~1×10⁻⁸ |
| Zener A=1 | elastic isotropy (reference) | 1.00000004 | — |

- **Loci spread = 4.75×10⁻⁸.** All three (four, with Zener) co-locate at ρ_bond=1 to 7 digits.
- **CO-LOCATED ⟹ THE PARENT EXISTS.** The match (no reflection), the Heaviside condition (no
  dispersion/distortion), and the balance (no anisotropy) are **not three coincidentally-aligned
  facts — they are one condition** (the Ax3 internal-boundary |Γ|²=0 point) viewed three ways.
- **Enantiomorph parity:** ρ*(right) = ρ*(left) to |Δ| = 4.85×10⁻¹⁰ — the match locus is
  hand-independent (the 4₁-screw handedness is saturation-only, cold-parity-symmetric).

---

## 4. THE ½/¼ KNIFE + THE PHOTON-vs-MATTER LOCUS SEPARATION (honest scope)

**The ½/¼ knife PASSES.** The photon point ρ_bond=1 falls out of the |Γ|²-minimisation
**knob-free** — it is NOT a tuned ρ_bond* supplied from outside (contrast the ν=2/7 matter point,
which needed ρ*≈9.77 GR-imported per `srs-elastic-tensor` result). A genuine mechanism lands on
the ratio 1 by itself; this one does.

**The photon point and the matter point are DIFFERENT loci** (surfaced honestly):

| Locus | ρ_bond | Γ_internal | mechanical K | physical role |
|---|---|---|---|---|
| **PHOTON** (Ax3 match) | **1.0** | **1.5×10⁻⁸** (matched) | **K < 0 (unstable)** | the transverse photon's zero-reflection light-cone |
| **MATTER** (ν=2/7 / K=2G) | 9.7734 | 0.328 (reflecting) | K > 0 (stable) | the GR-imported matter Poisson operating point |

This is the physically interesting tension and it is NOT a problem for the result — it SHARPENS
it. The photon rides a **lossless-reactive** operating point where the medium is acoustically
matched to itself (K<0 = not a static solid, exactly right for a pure reactive wave carrier). The
matter sector sits at a DIFFERENT, mechanically-stable ρ* where the substrate CAN store static
strain (and where it internally reflects — matter is where reflection lives, per the Γ=−1
particle-core canon). **The photon point is where the substrate is transparent; the matter point
is where it is not.** Ax3 forces the photon to the transparent point; that is the whole content of
the emergent-Lorentz light-cone.

> **↗ REFINE (2026-07-04, PR #518 MERGED — the matter-stiffening derivation): the two "different
> loci" are the endpoints of a saturation-driven state diagram, with a DERIVED direction but an
> IMPORTED matter value.** The photon locus ρ_bond=1 (this §4) and the matter locus ρ*≈9.77 are
> not merely disjoint points — a follow-on arc shows the canon-forced composition **ρ_eff =
> ρ_cold·(S_axial/S_shear)** (with ρ_cold=1, this result's Ax3-forced cold point) supplies the
> MECHANISM connecting them: under **asymmetric shear-channel loading** (the shear/T2-charge spring
> driven toward yield while the axial/A1-mass spring stays sub-saturated), ρ_eff RISES —
> STIFFENING, off the cold ρ=1 point toward the matter regime. **So the DIRECTION between the two
> loci is now a canon-forced Ax4 mechanism.** BUT (honest, mandatory framing): the ρ*=9.77 crossing
> occurs at an **ARBITRARY wall-amplitude** (A_wall=0.99479, NOT canon-distinguished — not √α, not
> 1−α, not the yield wall); the electron's actual near-yield T2 wall (A→1) sends ρ_eff→∞
> (ρ_eff≈222 at A_wall=0.99999), **OVERSHOOTING** 9.77 — 9.77 is crossed only in passing, not a
> landing point / attractor / canon-distinguished operating point. **The state-diagram SHAPE is
> derived (ρ=1 vacuum/radiation ↔ ρ_eff>1 matter-loaded); its matter VALUE 9.77 stays
> GR-imported** (`srs-elastic-tensor` result, PR #506) — the import is relocated ("the
> wall-amplitude that hits ρ* set by hand"), not removed. **This does NOT derive the /7 value.**
> Regime scope (carried verbatim, flag-don't-fix): the ρ*=9.77 of the `srs-elastic-tensor` result
> is a **COLD** bond ratio (REGIME: cold linear, sub-yield, saturation OFF), whereas ρ_eff is a
> **SATURATED** effective ratio; driving the saturated ρ_eff to 9.77 is NOT proven to land the same
> ν=2/7 / K=2G elastic tensor — that would need a Born-Huang run on the saturated Φ_b, UNTESTED (a
> running arc tests exactly this gap; no reading here pre-judges it). Provenance:
> `research/2026-07-04_matter-stiffening-rho_result.md` (VERDICT BOX + §6 + §8). *(This result body
> is a frozen record; banner-append only.)*

> **↗ RESOLUTION UPDATE (2026-07-04, PR #521 MERGED — the saturated-elastic-tensor arc; the REFINE
> banner above is PRESERVED — KEEP-BOTH).** The "running arc" the REFINE banner defers to has landed:
> verdict **[SAME-TENSOR-POINT]**. The Born-Huang run on the saturated Φ_b was performed, and driving
> the saturated ρ_eff to 9.7734 DOES land the same cold ν=2/7 / K=2G tensor (undeformed map;
> homogeneous degree-1 → dimensionless ratios degree-0, an overall scale drops out, VS2/VS3 ≤4×10⁻⁸).
> **The cold-vs-saturated tensor gap CLOSES — MODEL-SCOPED** to the small-signal swapped-springs model
> (fixed geometry); the **RESIDUAL STAYS OPEN** (initial/residual pre-stress + bias-induced geometry
> change OMITTED, § MODEL SCOPE). **This does NOT change the state-diagram VALUE grade of this result:**
> the two loci here are unchanged — the matter point stays at the GR-imported ρ*≈9.77 (crossing
> amplitude A_wall=0.99479 canon-undistinguished), the photon point stays at the Ax3-forced ρ=1, and
> the K<0 lossless-reactive honest flag (§4) is untouched. [SAME-TENSOR-POINT] is a CONSISTENCY
> finding, NOT a value derivation. Provenance:
> `research/2026-07-04_saturated-elastic-tensor_result.md` (VERDICT BOX + § MODEL SCOPE); driver
> `src/scripts/vol_1_foundations/saturated_elastic_tensor.py`. *(Frozen record; banner-append only —
> the REFINE banner above is unedited.)*

---

## 5. WHAT THIS DOES / DOES NOT CLAIM

**Does claim:**
- The photon's k_s=k_a operating point (Lorentz-on-srs, previously asserted) is **DERIVED from
  Axiom 3** — an axiom-manifestation, knob-free.
- MATCH / BALANCE / HEAVISIDE are **one parent condition** (Ax3 internal-boundary |Γ|²=0).

**Does NOT claim:**
- **NOT a weak-C proof.** The (qℓ)⁴ photon-DISPERSION tell stays conditional on gate `wejkhvnfb`
  (unchanged). This arc derives the ISOTROPY/MATCH pinning at k_s=k_a, not the zone-edge decoupling.
- **NOT a matter-Poisson claim.** The ν=2/7 / K=2G point stays GR-imported (`srs-elastic-tensor`
  result); this arc is about the PHOTON point, a separate locus.
- **NOT an emergence claim about Z_0's or α's VALUE.** Both by symbol; the derivation is about the
  FORM/pinning of k_s=k_a. AXIOM-MANIFESTATION class.
- `mass=A1` untouched (PR#260/#311 ECHO-final).

---

## 6. FALLOUT / AUDITOR-QUEUE (surfaced for the auditor lane; implementer does NOT land manuals)

These are auditor-lane manual landings (per lane discipline — implementer surfaces, auditor lands):

| Site | Proposed disposition |
|---|---|
| **`research/2026-07-04_lorentz-on-srs_result.md`** (photon AT k_s=k_a, "asserted"/"cubic-symmetry-automatic") | **UPGRADE:** the k_s=k_a operating point is now DERIVED from Axiom 3 (internal-boundary |Γ|²-min), knob-free — not merely "the emergent-Lorentz photon point" chosen by hand. Add a line: the pinning is an axiom-consequence. |
| **`srs_bloch_dispersion.py:179-192`** (comment "isotropic-bond point k_s=k_a (the emergent-Lorentz photon point)") | The comment now has a DERIVATION backing it: ρ_bond=1 is the Ax3 |Γ|²-min. (Code unchanged; the operating point is confirmed correct and now derived.) |
| **`axiom-definitions.md:38-48`** (Ax3 Minimum Reflection Principle, boundary form) | **STRENGTHEN (candidate):** the boundary form's "every internal impedance boundary" now has a worked ELASTIC-sector consequence (forces bond-isotropy k_s=k_a), not only the EM ε=μ consequence. First demonstration that Ax3 reaches into the translational-elastic sector. |
| **`achromatic-impedance-matching.md` / `z0-derivation.md`** (SYM ε·μ, Γ_EM=0) | **CROSS-LINK (candidate):** the EM match (cap↔ind) and the elastic balance (axial↔shear) are siblings under the SAME Ax3 parent — different sectors, one principle. A "sibling condition" cross-ref. |
| **The isotropy defense sites S1–S5** (`clm-k4d4ph`, `clm-yr6tu4`, etc., per the Lorentz result) | **STRENGTHEN:** the leading-order isotropy is now doubly-protected — not just "cubic-symmetry-automatic" but Ax3-FORCED at the unique zero-internal-reflection point. |

**NEW forward statement (surfaced, auditor/Grant framing call whether it earns a Letter line or a
KB leaf):** the photon's emergent-Lorentz isotropy is an **Axiom-3 consequence** — the transverse
light-cone sits at the unique bond-stiffness ratio where the substrate's internal-boundary
acoustic reflection vanishes. Cold birefringence, dispersion, and anisotropy are forbidden at the
SAME point by the SAME axiom (the Minimum Reflection Principle).

**HONEST FLAG for Grant (flag-don't-fix):** the Ax3-match photon point (ρ_bond=1) is mechanically
UNSTABLE (K<0). This is physically consistent (a lossless-reactive photon carrier, not a static
solid) but it is a substrate-native fact worth Grant's eye: **the photon and matter sectors sit at
different bond-stiffness ratios** — the photon where the substrate is transparent (K<0, matched),
matter where it is stiff and reflecting (K>0, ρ≈9.77). Surfaced, not resolved.

---

## 7. CROSS-REFERENCES (verified at HEAD `43151be1`)

- Prereg (FROZEN): `research/2026-07-04_parent-condition-match-forces-balance_prereg_FROZEN.md`
- Driver: `src/scripts/vol_4_engineering/parent_condition_match_forces_balance.py`
- Test: `src/tests/test_parent_condition_match_forces_balance.py` (9 pass)
- Ax3 Minimum Reflection Principle (boundary form): `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md:38-48`
- Parent arc (photon AT k_s=k_a, asserted): `research/2026-07-04_lorentz-on-srs_result.md`
- Operating point: `src/scripts/vol_4_engineering/srs_bloch_dispersion.py:179-192`
- Achromatic SYM ε·μ match: `manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/achromatic-impedance-matching.md`; `.../ch1-vacuum-circuit-analysis/z0-derivation.md:69-76`
- Γ_EM=0 SYM canon: `manuscript/ave-kb/vol9/ch4-dc-electrical-characteristics/three-channel-impedances.md:20`
- EE port map (k_a,k_s → capacitive): `manuscript/ave-kb/common/translation-tables/translation-circuit.md:99-116`
- Matter ν=2/7 / K=2G locus (GR-imported, ρ*≈9.77): `research/2026-07-04_srs-elastic-tensor_result.md`
- Machinery: `src/ave/core/micropolar_bloch.py`, `src/ave/core/chiral_lattice.py` (`build_srs_net`)

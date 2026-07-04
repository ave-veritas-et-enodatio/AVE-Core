# FROZEN PREREG — The srs Elastic-Tensor Arc: Cauchy-grade C_ij of the chiral srs-z3 net from the canonical bond model

**Date:** 2026-07-04 · **Lane:** implementer (Grant-fired "fire away")
**Branch:** `analysis/srs-elastic-tensor` · **Status:** FROZEN — the fallout map and all
adjudication bins below are frozen BEFORE any srs elastic number is read.
**Driver (to build):** `src/scripts/vol_1_foundations/srs_elastic_tensor.py`
**Carrier declaration (D1 policy 3):** the RATIFIED **chiral srs-z3** net (`build_srs_net`,
degree-3, I4₁32, Wyckoff-8a, 8 sublattices/cell). NOT the diamond-z4 instrument.

---

## SUBSTRATE-FIRST SECTOR HEADER (mandatory, BEFORE any standard-physics word)

- **WHICH SECTOR.** The **translational (Cauchy-grade) sector** of the chiral srs-z3 net.
  Per node: 3 translational DOF `u`. 8 Wyckoff-8a sublattices/cell → a **24×24 Bloch
  dynamical matrix `D(k)`** (the same object `srs_bloch_dispersion.py` builds). Each z=3
  bond carries the substrate-native **general-force-constant RANK-2 bond tensor**
  `Φ_b = k_a·d̂⊗d̂ + k_s·(I − d̂⊗d̂)` — `k_a` = axial/STRETCH stiffness, `k_s` = transverse/
  SHEAR (bond-bend) stiffness — on the lattice's OWN z=3 bonds (NOT a Cartesian Laplacian,
  which would fake an O(k²) anisotropy: the disabled-flag-stencil bug the RANK-2 lesson
  warns of). This is EXACTLY the corpus's canonical Cauchy-grade bond model
  (`clm-bjceop:1073` `K_0=4k_a+8k_s, G_0=8k_s`; the K=2G-provenance driver
  `k2g_crystalline_provenance.py`, which ran it analytically on z=4 diamond).

- **SCOPE DECLARATION (Cauchy grade; Cosserat is STAGE 2 only).** This arc computes the
  **CAUCHY-grade elastic tensor** from the translational sector: `C11, C12, C44` for the
  cubic I4₁32 crystal, read from the long-wavelength acoustic-branch slopes (Born-Huang).
  The Cosserat couple-stress constants (`G_c, γ` micro-rotation) are **STAGE 2, and ONLY
  if the Cauchy answer is ambiguous** (declared, not ballooned). Per the moduli-hierarchy
  finding (`2026-07-02_axiom4-moduli-hierarchy_result.md:22-24`): `ℓ_c²=γ/G` is a
  *within-bend-sector* ratio, ORTHOGONAL to the stretch/bend ratio `ρ=k_a/k_s` that sets
  K/G. So the Cauchy tensor is `(k_a, k_s)`-determined; the couple-stress modifies the
  band structure at finite kℓ, not the k→0 elastic slopes. Cauchy grade is the right
  first cut. (FRAMING FORK ALREADY RESOLVED BY CORPUS — see §0.5.)

- **REGIME.** Cold linear (small-signal) band structure, sub-yield, saturation OFF. The
  4₁-screw handedness is **SATURATION-ONLY** (`κ_chiral` biases the saturation kernel,
  `cosserat_field_3d.py:562/605`, and does NOT enter the bare cold energy). So the cold
  linear bands are **parity-symmetric BY CONSTRUCTION** — no chiral chord expected in the
  elastic constants; a Zener anisotropy, if present, is a lattice-geometry effect (the
  cubic I4₁32 point group), NOT a handedness chord. Both enantiomorphs must give the SAME
  C_ij (handedness must not change the cold elastic tensor).

- **PHASE-STATE / MODE / Op14.** MODE = translational (Cauchy: bulk via `k_a`, shear via
  `k_s`). REGIME = linear / sub-yield. Op14 saturation = OFF. PHASE-STATE = unbroken
  free-wave. Local-clock modulation N/A (cold).

- **PHASE-SPACE vs REAL-SPACE (A46).** This is a **real-space / spatial-Brillouin**
  measurement: `ω(k)` acoustic slopes → `C_ij` → ν, Zener, K/G. The corpus claim being
  tested (`ν_vac = 2/7`, a Poisson ratio = a real-space moduli ratio;
  `vacuum-poisson-ratio.md` `ν=(3K−2G)/(2(3K+G))`) is ITSELF a real-space moduli ratio.
  Coordinates match. This is NOT a phase-space (V_inc, V_ref)/Clifford-torus claim — no
  φ²/winding comparison is made.

- **CONSISTENCY-vs-EMERGENCE class.** ν, Zener, K/G are computed as **dimensionless RATIOS
  from the lattice geometry + the bond stiffness ratio ρ=k_a/k_s** — NO CODATA input, NO α,
  NO Q_TANK on the verdict path (α-CLEAN). The verdict is **CONSISTENCY-class** (does the
  crystalline srs bond model reproduce the amorphous-EMT ν=2/7, or not?), NOT emergence
  (we are not claiming ν=2/7 is "predicted" — we are testing whether the crystalline
  carrier grounds the number the amorphous averaging produced).

---

## 0. North star — the seam this closes (verified at HEAD)

The corpus's `ν_vac = 2/7` (and the /7 PPN coupling family riding it) derives from
**EFFECTIVE-MEDIUM AVERAGING** over a **disordered/amorphous** network with non-integer
coordination `z₀ ≈ 51.25` (Feng-Thorpe-Garboczi EMT):
- `trace-reversal-mechanism.md:18-22` (verified 2026-07-04): "the Effective Medium Theory
  of Feng, Thorpe, and Garboczi analytically verifies this requirement … 3D amorphous
  diluted central-force network with (non-integer) coordination z₀ ≈ 51.25 … crosses
  K/G = 2 at p* = 8πα … (ν = 2/7)."
- `topological-packing-fraction.md:16` (verified): "z₀ ≈ 51.25 is the effective coordination
  number of the chiral **amorphous** (disordered, non-crystalline) lattice."

But the RATIFIED carrier (D1, 2026-07-03) is the **crystalline srs-z3** (integer z=3).
The crystalline-vs-amorphous seam is flagged OPEN at
`the-abandoned-interior.md:183` (verified 2026-07-04): "the *crystalline-vs-amorphous*
description doing the isotropy work is **not unified** … This is a real open seam in the
isotropy defense; the auditor lane + Grant adjudicate whether one structural picture
subsumes the other."

K=2G is booked **GR-IMPORTED** (PR#261, `k2g-crystalline-provenance_result.md`), NOT
lattice-forced. The prior provenance work did the crystalline elastic-tensor calc **on z=4
diamond** and found ν≈0.067 (K/G≈0.82), FAR from 2/7 — the z=4 crystal does NOT force
K=2G. **The srs-z3 elastic-tensor calc has NEVER been done.** This arc does it.

## 0.5. FRAMING FORK — RESOLVED BY CORPUS (no Grant escalation on this axis)

The brief flagged a possible STOP-and-surface fork: "which bond stiffnesses the Cosserat
sector contributes at Cauchy grade." **This is resolved by the existing corpus** and does
NOT require Grant adjudication:

- The Cauchy-grade bond model is the **2-parameter general-force-constant tensor**
  `Φ_b = k_a·d̂⊗d̂ + k_s·(I−d̂⊗d̂)` — `k_a` (axial STRETCH, the central-force spring),
  `k_s` (transverse SHEAR/bend, the non-central spring). This is canonical:
  `clm-bjceop:1073` (`K_0=4k_a+8k_s, G_0=8k_s`), the K=2G-provenance driver
  (`k2g_crystalline_provenance.py:11-13`), and the moduli-hierarchy result
  (`2026-07-02_axiom4-moduli-hierarchy_result.md:22` "`ρ=k_a/k_s` IS the slenderness²").
- The **Cosserat micro-rotation** (`G_c, γ`) is a SEPARATE grade (couple-stress), ORTHOGONAL
  to `ρ=k_a/k_s` at the k→0 Cauchy slopes (`axiom4-moduli:24` "`ℓ_c²=γ/G` … orthogonal to
  the stretch/bend ratio ρ"). It does NOT contribute to the Cauchy C_ij at k→0.
- Therefore the Cauchy tensor is a function of `(k_a, k_s)` — equivalently the single ratio
  `ρ=k_a/k_s` — read off the srs lattice geometry. **No fork to Grant here.** A NEW fork
  the axioms cannot settle (should one arise mid-run) STILL stops and surfaces.

## 0.6. THE CANONICAL BOND STIFFNESS RATIO ρ (the load-bearing input, α-CLEAN provenance)

The Cauchy C_ij depend on the lattice geometry AND the single bond ratio `ρ=k_a/k_s`.
Provenance of ρ, ledgered:
- **K=2G ⟺ a specific ρ\*** — the GR-imported condition. On z=4 diamond,
  K=2G ⟺ k_a=2k_s (ρ=2) in the corpus's K4-specific normalization (`clm-bjceop`), or
  ρ\*∈{3.67, 5.30, 6.62} in the standard-Keating normalization depending on which shear
  modulus (C44/C′/Voigt) — they DISAGREE because z=4 diamond is Zener-anisotropic (A=1.21)
  (`k2g-crystalline-provenance_result.md:41,62`).
- **The isotropic-bond point ρ=1 (k_a=k_s)** — the emergent-Lorentz photon point used by
  `srs_bloch_dispersion.py:183`. This is an ENGINEERING-CHOICE reference (the point where
  the transverse photon rides), NOT a K=2G point.
- **REPORTING DISCIPLINE (no tuning toward 2/7).** The driver computes the FULL curve
  ν(ρ), Zener(ρ), K/G(ρ) across ρ ∈ [0.5, 10] — the same range as the z=4 provenance
  table — and reads off, HONESTLY: (i) the srs ν at the K=2G point ρ\* (if K=2G is even
  achievable on srs); (ii) whether srs is Zener-isotropic (A=1) at any ρ; (iii) whether a
  geometrically-distinguished ρ exists. NO tuning of ρ toward 2/7. The fallout map being
  frozen FIRST is the guard: whatever ν the srs geometry+ρ produces is booked against the
  fallout map, not reverse-engineered.

---

## FALLOUT MAP — FROZEN BEFORE ANY SRS NUMBER (challenge-canonical-number discipline)

Every claim/constant/leaf riding `ν=2/7` / the three /7 PPN couplings / trace-reversal /
the C11 relabel, enumerated so the [DIFFERENT-ν] bin executes as HONEST status-demotions
(flag-don't-fix), never silent rewrites. Grep-sourced at HEAD 2026-07-04.

### F.A — Code constants riding the /7 family (`src/ave/core/constants.py`)

| Site | Constant | Rides ν=2/7 how | If ν≠2/7 |
|---|---|---|---|
| `:573` | `NU_VAC = 2/7` | the number itself | DIRECT — the value under test |
| `:356` | `N_NU = 2/7` "(Axiom 2)" | duplicate of NU_VAC | DIRECT |
| `:570` | `ISOTROPIC_PROJECTION = 1/7` | 1D→3D bulk projection in a trace-reversed ν=2/7 solid (`one-seventh-impedance-projection.md:16`) | STATUS-DEMOTE if the 2/7 grounding shifts |
| `:449` | `ETA_EQ = P_C·(1−2/7)` | uses 5/7 = 1−ν_vac | RE-EXPRESS if ν changes |
| `:580` | `ALPHA_S = α^(3/7)` | "3 spatial / 7 compliance modes (from ν_vac=2/7)" (`:578`) | STATUS-DEMOTE the 3/7-from-ν_vac rationale (value α_s itself is an α-echo, separate) |
| `:694` | `SIN2_THETA_12 = NU_VAC + 1/45` | neutrino mixing rides ν_vac literally | RE-EXPRESS / status-demote |
| `:608` | `M_W_MEV` uses `√(3/7)` | 3/7 projection factor | check if 3/7 tied to ν_vac or independent |
| `:717` | `V_LONG = √(2G/ρ)` "From K=2G (EMT, Ch 2)" | longitudinal speed HARD-SET by K=2G | the direct K=2G consumer — re-derive from srs C11 if ν≠2/7 |
| `:1086` | `_OMEGA_1` uses `(1+NU_VAC)` | proton-scale frequency | RE-EXPRESS |

### F.B — Manuscript /7-family leaves (the foundational cluster, `vol3/gravity/ch01-gravity-yield/`)

| Leaf | Claim | Rides ν=2/7 how |
|---|---|---|
| `vacuum-poisson-ratio.md` (`clm-x19btt`) | ν=(3K−2G)/(2(3K+G))=2/7 given K=2G | the algebraic identity ν=2/7 ⟺ K=2G |
| `trace-reversal-mechanism.md` (`clm-rd9cjm`) | the amorphous-EMT z₀≈51.25 crossing at K/G=2 | THE SEAM — the amorphous averaging argument this arc replaces |
| `one-seventh-impedance-projection.md` | 1/7 projection "within a trace-reversed (ν=2/7) solid" | the 1/7 root |
| `topological-packing-fraction.md` | p*=(10z₀−12)/(z₀(z₀+2))=8πα at z₀≈51.25 | the amorphous z₀ that sets ν |
| `temporal-spatial-lattice-decomposition.md` (`clm-rd9cjm`) | n_t=1+(2/7)ε₁₁, n_s=1+(9/7)ε₁₁ | the (2/7) and (9/7) PPN indices |
| `optical-refraction-gravity.md` | n(r)=1+ν_vac·χ_vol=1+(2/7)χ_vol | the photon deflection index |

### F.C — The three /7 PPN couplings (`2026-06-05_gravity-ppn-coherence-result.md`)

| Coupling | Value | Status at HEAD | Rides ν=2/7 how |
|---|---|---|---|
| photon transverse index (S2, Op19) | `n_⊥ = 1+(2/7)ε₁₁` → δ=4GM/bc², γ=1 | COHERENT (the surviving chain) | ν_vac=2/7 IS the transverse projection |
| n_spatial "controls deflection" (S1 label) | `1+(9/7)ε₁₁` | ALREADY WALKED-BACK (outlier, 4.5× GR) | (9/7)=(2/7)+1 bookkeeping sum |
| temporal redshift index | `n_t=1+(2/7)ε₁₁=1+2GM/c²r` | flagged 2× redshift knot | ν_vac=2/7 temporal projection |

Note: the PPN result already tags these Class-C **consistency checks** (`predictions.yaml`
P10 `type: consistency_check`) and states ν_vac=2/7 is "axiom-derived (K=2G trace-reversal),
with the honest-α caveat" (`gravity-ppn-coherence-result.md:138`). The /7 family's GR
agreement is STRUCTURAL (the 2/7 index is calibrated to √(g_ij/−g₀₀)_GR), NOT predictive.
**A DIFFERENT srs ν does not break GR agreement** (that is calibrated in independently at
the deflection-integral level) — it removes the *substrate grounding* for WHY ν=2/7, which
is what trace-reversal-mechanism.md claims to supply. That is the honest scope of the
[DIFFERENT-ν] fallout: it re-opens the *provenance* of 2/7, not the GR numbers.

### F.D — The C11 relabel

Per the memory note "(9/7)-light label WRONG but LOAD-BEARING for C11 (relabel)": the C11
relabel is the gravity-PPN C11 claim, NOT the elastic C11 this arc computes. NAME COLLISION
flagged: this arc's `C11` = the elastic stiffness (Voigt cubic); the corpus's "C11 relabel"
= a claim-ID relabel in the PPN coherence merge (#90/91/92). The driver's output uses
`C11_elastic` to avoid the collision. No fallout linkage — flagged to prevent a false one.

---

## FROZEN ADJUDICATION BINS (frozen before any srs number)

- **[SRS-REPRODUCES-2/7].** The srs Cauchy tensor gives ν = 2/7 (within tolerance) at a
  geometrically-motivated / K=2G-consistent ρ, AND srs is Zener-isotropic enough that "a
  single ν" is meaningful. → **The seam closes**; the /7 family gains a crystalline tensor
  grounding to REPLACE the amorphous-EMT averaging. Report as a strengthen (the amorphous
  z₀≈51.25 argument is superseded by the crystalline calc, same answer).

- **[DIFFERENT-ν].** The srs Cauchy tensor gives ν ≠ 2/7 at every physically-motivated ρ
  (as z=4 diamond gave ν≈0.067). → **The /7 family re-opens at the provenance level**; the
  fallout map (F.A–F.D) executes as HONEST STATUS-DEMOTIONS (flag-don't-fix). The amorphous
  averaging does NOT transfer to the crystalline carrier; ν=2/7 stays GR-imported (via
  K=2G) with NO crystalline substrate grounding. Surface with both file paths + verbatim.

- **[ANISOTROPIC-BREAKDOWN].** The Zener ratio `A = 2C44/(C11−C12)` is materially ≠ 1 (as
  z=4 diamond's A=1.21). → The isotropic-ν framing itself is invalid for srs: "a single ν"
  is an averaging choice (Voigt/Reuss/Hill spread), not a lattice output. **Surface this;
  do NOT rebuild the isotropy defense unilaterally** — the auditor lane + Grant adjudicate
  whether the cubic-averaging (`Fd3̄m`/`I4₁32` symmetry suppression) picture subsumes it.
  Report the Zener ratio and the VRH ν-spread; the isotropy defense is the-abandoned-
  interior.md's open seam, not this arc's to close.

- **[STUCK-FRAMING → Grant].** A framing fork the axioms + corpus cannot settle (a NEW one
  beyond the §0.5-resolved bond-model fork). STOP and surface.

---

## VALIDATE-ON-KNOWN (frozen targets, run BEFORE the srs verdict — HALT if fail)

The numeric Bloch-slope → C_ij pipeline MUST reproduce a lattice whose elastic constants are
known analytically, BEFORE the srs numbers count. Two independent knowns:

| # | Known lattice | Analytic target | Tolerance | Rationale |
|---|---|---|---|---|
| V1 | **simple-cubic central-force** (k_a on 6 axial bonds, k_s=0) | C11=k_a/a, C12=0, C44=0 (textbook; ν=0) | rel-err < 1e-2 | the cleanest closed-form Born-Huang check: pure axial springs on a cubic lattice give C11=k_a/a, C12=C44=0 |
| V2 | **z=4 diamond Keating** (the K=2G-provenance driver's analytic model) | C11=k_a+3k_s, C12=k_a−k_s, C44_relaxed=4k_a k_s/(k_a+k_s); at carbon-diamond ρ → ν≈0.068, Zener≈1.21 | rel-err < 5e-2 (numeric-vs-analytic; internal-strain relaxation must be captured) | reproduces the EXACT prior corpus result (`k2g_crystalline_provenance.py`) on the SAME numeric pipeline the srs uses — the direct cross-check that the srs number is trustworthy |
| V3 | **isotropy sanity** — simple-cubic with k_a=k_s (fully isotropic bond) | Zener A=1 (isotropic) | abs(A−1) < 1e-2 | confirms the pipeline reads Zener correctly (a lattice that SHOULD be isotropic reads A=1) |

If V1/V2/V3 fail → the extraction pipeline is wrong; HALT, report no srs verdict.

Internal-strain (Kleinman) note: multi-sublattice lattices (diamond, srs) relax internal
DOF under macroscopic shear — the acoustic-slope extraction captures this AUTOMATICALLY
(the lowest eigenvalue branch already includes the optic-mode relaxation), UNLIKE the
clamped-ion analytic C44. V2 tests exactly this against the relaxed analytic value.

---

## THE THREE READOUTS (frozen; reported whatever they say)

1. **ν vs 2/7.** The srs Cauchy Poisson ratio ν(ρ) across ρ∈[0.5,10]; the value at the
   K=2G-consistent ρ\* (if achievable) and at the isotropic-bond ρ=1; compared to 2/7.
2. **Zener ratio A = 2C44/(C11−C12).** The isotropy test. A=1 ⟺ isotropic; A≠1 ⟹
   [ANISOTROPIC-BREAKDOWN] risk (the isotropic-ν framing is invalid).
3. **K=2G test.** Compute K and G from the srs constants; is `2G/K = 1` FORCED by the srs
   bond model at a geometrically-distinguished ρ, or is it (as on z=4) a one-parameter
   family needing an externally-supplied ρ\*? Book against the GR-imported status honestly
   (Rule 11: whatever it says, the discipline is the same as the z=4 finding).

## OUTPUT

`src/scripts/vol_1_foundations/srs_elastic_tensor.py` → `_output/srs_elastic_tensor.json`
(the validate-on-known table, the per-direction slope table [100]/[110]/[111], the ν(ρ)/
Zener(ρ)/K-G(ρ) curves, the bin verdict). Result doc:
`research/2026-07-04_srs-elastic-tensor_result.md`. Claims-register: status-demotion /
strengthen rows ONLY per the bin (no rewrites). NO self-merge; REVIEW: pending-orchestrator.

---

## Cross-references (verified at HEAD 2026-07-04)

- Carrier: `src/ave/core/chiral_lattice.py` `build_srs_net` (z=3, I4₁32, Wyckoff-8a)
- srs Bloch machinery (extends): `src/scripts/vol_4_engineering/srs_bloch_dispersion.py`
- z=4 analytic template + validate-on-known ref: `src/scripts/verify/k2g_crystalline_provenance.py`
- The seam: `manuscript/ave-kb/common/the-abandoned-interior.md:183`
- ν=2/7 amorphous provenance: `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/trace-reversal-mechanism.md:18-22`
- K=2G GR-imported: `research/2026-06-15_k2g-crystalline-provenance_result.md`
- Bond stiffness ρ=k_a/k_s: `research/2026-07-02_axiom4-moduli-hierarchy_result.md:22-29`
- /7 PPN couplings: `research/2026-06-05_gravity-ppn-coherence-result.md`
- D1 migration policy: `_orchestration/2026-07-03_srs-migration-policy.md`

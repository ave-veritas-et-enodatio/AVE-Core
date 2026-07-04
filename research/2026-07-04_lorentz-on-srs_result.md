# RESULT — LORENTZ-ON-SRS: the photon-sector isotropy / emergent-Lorentz chain RE-CLEARS on the chiral srs-z3 carrier. The migration's P1 acceptance gate PASSES.

**Date:** 2026-07-04 · **Lane:** implementer · **Branch:** `analysis/lorentz-on-srs`
**Arc:** the srs-migration policy's **P1 acceptance gate** (engine-upgrade program item-3,
the FINAL item).
**Driver:** `src/scripts/vol_4_engineering/lorentz_on_srs.py`
**Output:** `_output/lorentz_on_srs.json` (driver-regenerable; gitignored)
**Test:** `src/tests/test_lorentz_on_srs.py` (12 pass)
**Prereg (FROZEN):** `research/2026-07-04_lorentz-on-srs_prereg_FROZEN.md`
**Parent (P1b.3, merged `19a31836`):** `src/scripts/vol_4_engineering/srs_bloch_dispersion.py`
**Grant standing order (2026-07-03 D1 RATIFICATION):** *"the Lorentz chain must re-clear on
srs or the migration STOPS."*

---

## VERDICT BOX

> **PRIMARY BIN: [ISOTROPY-EMERGES]. carrier: srs-z3. The P1 GATE CLEARS — the migration PROCEEDS.**
>
> On the ratified chiral **srs-z3** net (point group **432**, space group **I4₁32**, z=3),
> the photon-sector isotropy / emergent-Lorentz chain re-clears node-up, carrier-native:
>
> 1. **Leading-order c is ISOTROPIC** — both transverse (u-dominated) photon branches have
>    c(k→0) direction-independent to **machine precision** (cross-direction spread
>    extrapolated to k=0 = **0.0**; [100]/[110]/[111] speeds agree to <1e-6). Z₀ recovered
>    exactly (rel-err 0). The emergent-Lorentz light-cone is carrier-native on srs.
> 2. **NO cold birefringence** — the two transverse photon branches are **DEGENERATE**
>    (share c): max|ω_T1−ω_T2| = **1.7×10⁻¹⁴** at a floor-clear probe, for every direction
>    including the low-symmetry [110]/[210]. The cold lattice is NOT birefringent — the
>    Letter's implicit baseline HOLDS.
> 3. **The (qℓ)⁴ anisotropy-suppression FORM re-clears** — on srs (432), the FIRST
>    direction-dependent bond-moment invariant is the **QUARTIC** cubic harmonic:
>    ⟨(q̂·d̂)²⟩ isotropic (spread 1.7×10⁻¹⁶, no angular dependence), ⟨(q̂·d̂)⁴⟩ = pure cubic
>    harmonic (κ_srs = **−1/12**, residual 1.9×10⁻¹⁶) — **IDENTICALLY to diamond** (m3̄m,
>    κ_diamond = **−2/9**). The (qℓ)⁴ FORM the corpus argued on Fd3̄m diamond-cubic
>    averaging is a property of BOTH cubic point groups; the migration does NOT lose it.
> 4. **The chiral k-linear gyrotropy is srs-DISTINCT and negligible** — point group 432
>    PERMITS an acoustic-gyrotropy (optical-activity analog) k-LINEAR term (B_signed =
>    −4.30×10⁻⁴, parity-odd: flips to +4.30×10⁻⁴ under enantiomorph swap). Diamond (m3̄m,
>    centrosymmetric) FORBIDS it (4.8×10⁻³⁷, machine null). At optical scale δ_chiral ≈
>    **1.7×10⁻⁹·(qℓ_node)** — well below LIV bounds; a genuine new-but-tiny srs channel.
>
> **The raw acoustic-branch dispersion anisotropy is O(k²)** (order n = 2.0001) on BOTH
> carriers — the isotropic zone-edge term. This is UNCHANGED from the merged
> `srs_bloch_dispersion.py` (slope 1.9999) and does NOT re-open its verdict: the distinctive
> **(qℓ)⁴ photon-DISPERSION** tell stays **CONDITIONAL on the unproven weak-C no-zone-edge
> theorem** (gate `wejkhvnfb`, OPEN). This arc re-clears the FORM + the isotropy, not the
> weak-C lever.
>
> **All validation guards PASS:** planted n=2 reads 2.000 and n=4 reads 4.000 (the fit floor
> is clean — the exact §2-caveat trap is guarded); the direction-sphere fit is non-degenerate;
> the chiral scalar is parity-odd (`detect_symmetry_forced_zero` harness — so the diamond
> null is symmetry-protected, not accidental); the anisotropy order n is parity-even.

> **↗ UPGRADE (2026-07-04, PR #516 MERGED — the parent-condition derivation): the k_s=k_a
> operating point is now DERIVED, not asserted.** This result took the photon's isotropic-bond
> point k_s=k_a as an INPUT — established at leading order as **cubic-symmetry-automatic**
> (§Readout (1+2), verbatim: "The c-isotropy is cubic-symmetry-automatic at leading order (a
> rank-2 velocity tensor is forced isotropic by any cubic point group — 432 included)"). The
> operating-point choice itself — that the photon is *defined AT* k_s=k_a — was ASSERTED, not
> derived (paraphrase; the parent-condition prereg states the photon "is defined AT the
> isotropic-bond point k_s=k_a … which is currently ASSERTED, not derived",
> `parent-condition-match-forces-balance_prereg_FROZEN.md:7`; the result records it as "asserted
> not derived", `..._result.md:5`). The follow-on parent-condition arc CLOSES
> that surfaced plumber-question: minimising the srs net's **internal-boundary acoustic
> reflection** Γ_internal(ρ_bond) under Axiom 3 (Minimum Reflection Principle, boundary form,
> `axiom-definitions.md:48`) lands on **ρ_bond = k_a/k_s = 1 (k_s = k_a) to machine precision,
> KNOB-FREE** — the ½/¼ knife passes, no tuned ρ_bond* supplied. So the k_s=k_a operating point
> this result runs at is an **AXIOM-3 CONSEQUENCE** ([MECHANISM-DERIVED], axiom-manifestation
> class), not a hand-chosen locus. MATCH / BALANCE / HEAVISIDE co-locate at ρ_bond=1 as **one
> parent condition**. Scope note (KEEP-BOTH): this upgrades the OPERATING-POINT PINNING only —
> the 🟡 weak-C demotion of the (qℓ)⁴ photon-DISPERSION tell (gate `wejkhvnfb`, §4-S1) is
> UNCHANGED; this arc derives the isotropy/MATCH pinning, not the zone-edge decoupling.
> Provenance: `research/2026-07-04_parent-condition-match-forces-balance_result.md` (VERDICT BOX
> + §5); driver `src/scripts/vol_4_engineering/parent_condition_match_forces_balance.py`. *(This
> result body is a frozen record; banner-append only.)*

---

## SUBSTRATE-FIRST SECTOR HEADER (as run)

- **SECTOR:** translational (u) sector of the chiral srs-z3 net — the 24×24 Bloch dynamical
  matrix D(k) (8 Wyckoff-8a sublattices × 3 translational DOF). The photon = the two
  transverse (u-dominated, massless) acoustic branches at the isotropic-bond point k_s=k_a.
- **REGIME:** cold linear, sub-yield, saturation OFF. A band-structure / dispersion
  calculation (NOT time-domain LC) — no local-clock modulation (A²=0), no reactance-pair
  snapshot (no phase in a linear eigenproblem), no PML/centroid sampling. Substrate-native:
  RANK-2 bond tensor Φ_b = k_a·d̂⊗d̂ + k_s·(I−d̂⊗d̂), NOT a Cartesian Laplacian.
- **COORDS (A46):** spatial-Brillouin k-space; the corpus claim IS a k-space dispersion
  claim; ω(k) measured in the SAME k-space. Coordinates MATCH; A46-clean.
- **CLASS (consistency-vs-emergence):** CONSISTENCY / FORM-class. The FORM (isotropy,
  leading-anisotropy order, the 432-permitted form) is node-up; the MAGNITUDE (coefficient,
  δ at optical scale) is an ECHO. α-CLEAN: c₀,Z₀,ℓ_node imported by SYMBOL; n and c read off
  the EIGENVALUES, NOT baked.

---

## 1. VALIDATE-ON-KNOWN (all PASS, HALT-gated)

| # | Gate | Target | Result | Verdict |
|---|---|---|---|---|
| **V0** | srs acoustic speed isotropic + Z₀ recovered | v_lat iso, Z rel-err → 0 | v_lat=0.707107, **Z rel-err = 0.0** | **PASS** |
| **V1** | diamond validate-on-known reproduces the corpus (qℓ)⁴ FORM | quartic, Ξ-form | κ_diamond = **−2/9** (= the doc's −8/9 over 4 bonds), resid 2.8e-16 | **PASS** |
| **V2** | planted n=2 AND n=4 read back their order | reader recovers 2 and 4 | n=2 → **2.000**, n=4 → **4.000** | **PASS** |
| **V3** | diamond chiral term ≈ 0 (centrosymmetry null) | < 1e-8 | **4.8×10⁻³⁷** | **PASS** |
| **V4** | enantiomorph parity: n even, chiral term odd | n(R)=n(L); B_signed flips | Δn < 1e-3; sign-flip resid 5.6e-13 | **PASS** |

**V1 is the load-bearing validate-on-known:** the diamond INSTRUMENT (instrument-scoped per
the carrier guard) reproduces the corpus's OWN claimed (qℓ)⁴ FORM at its primitive cell —
so when srs reads the SAME quartic FORM, the reading is trusted. **V3 (diamond chiral null)
is the elegant symmetry control:** centrosymmetry FORBIDS the piezo-class gyrotropy, and
diamond reads machine-zero — the exact analog of the srs-micropolar M1 null-control.

---

## 2. THE FOUR READOUTS (frozen; reported whatever they say)

### Readout (1+2) — photon-branch isotropy + light-cone universality

The two transverse (u-dominated) photon branches at the isotropic-bond point k_s=k_a:

| Quantity | Value | Reading |
|---|---|---|
| c(k→0) light-cone | 0.707107 (= 1/√2 in bond units) | the isotropic emergent-Lorentz speed |
| c-isotropy spread, T1 (extrap. to k=0) | **0.0** (machine) | leading-order c direction-INDEPENDENT |
| c-isotropy spread, T2 (extrap. to k=0) | **0.0** (machine) | both transverse branches isotropic |
| max\|ω_T1 − ω_T2\| (kl=0.05, floor-clear) | **1.7×10⁻¹⁴** | the two transverse branches DEGENERATE — NO cold birefringence |

**The c-isotropy is cubic-symmetry-automatic at leading order** (a rank-2 velocity tensor is
forced isotropic by any cubic point group — 432 included), as the prereg anticipated. The
NON-trivial finding is that it holds to MACHINE precision (the spread scales as (kl_probe)²
and extrapolates to exactly 0), and that **the two transverse branches SHARE c** (degenerate
to 1.7×10⁻¹⁴) — so the cold srs lattice is not birefringent, the Letter's baseline holds.

> **Rule-10 empirical catches (running the driver surfaced both — flag, not silent-fix):**
> 1. **Direction-normalization.** A bare Miller index [1,1,0] passed un-normalized injects a
>    √2/√3 direction-dependent |k| and FAKES an O(k⁰) anisotropy (a normalization artifact,
>    NOT physics). Fixed: `acoustic_branches` unit-normalizes q̂ internally. Caught because
>    the raw HS speeds read 0.707/1.0/1.225 (a √3 spread) before the fix, vs the merged
>    driver's isotropic 0.707 — the flag-don't-fix cross-check against the merged upstream.
> 2. **Tiny-kl eigsolve floor.** The two transverse branches are a DEGENERATE eigenvalue
>    pair; at tiny kl (1e-4..1e-6) their ω differ by the eigsolve absolute float floor
>    (~1e-15), so |c_T1−c_T2| = floor/kl² BLOWS UP as kl→0 (larger at kl=1e-6 than at 1e-3 —
>    a 1/kl² artifact, NOT a k→0 splitting). Fixed: probe the degeneracy by the ABSOLUTE
>    ω-splitting at a floor-clear kl=0.05, where it reads 1.7×10⁻¹⁴ for every direction. The
>    first-pass single-kl-at-1e-4 measurement mis-binned to COLD-BIREFRINGENCE; the
>    multi-kl-scaling investigation corrected it to the true degeneracy.

### Readout (3) — the chiral k-linear (rotatory / acoustic-activity) term

Point group **432 PERMITS gyrotropy** (one of the 15 gyrotropic classes); m3̄m forbids it by
centrosymmetry. The acoustic-gyrotropy scalar (the `micropolar_bloch` translation↔rotation
coupling B_signed = tr(M_tr)):

| Lattice | B_signed | Reading |
|---|---|---|
| srs (right, 432) | **−4.2979×10⁻⁴** | nonzero — 432 permits acoustic activity |
| srs (left, 432) | **+4.2979×10⁻⁴** | exact sign flip (parity-odd, sign-flip resid 5.6×10⁻¹³) |
| diamond (m3̄m) | **+4.8×10⁻³⁷** | machine null — centrosymmetry forbids it |

This is the **mechanical sibling of the A44 EM gyrotropic converter** and the k-space
dispersion face of the same micropolar pseudo-tensor B the Stage-2 srs-chiral-micropolar arc
found (`research/2026-07-04_srs-chiral-micropolar_result.md`: σ^A/lever channel, geometry-
fixed). **Its size at physical scale (honest, not waved):**

| Scale | qℓ_node | δ_chiral ∼ \|B_signed\|·(qℓ_node) | δ_quartic ∼ \|κ\|·(qℓ_node)⁴ |
|---|---|---|---|
| optical (633 nm) | 3.83×10⁻⁶ | **1.65×10⁻⁹** | 1.80×10⁻²³ |
| X-ray (1 Å) | 2.43×10⁻² | 1.04×10⁻⁵ | 2.9×10⁻⁸ |

The chiral term is **k-LINEAR** (vs the quartic anisotropy) so it dominates the quartic at
long wavelength — but its coefficient is tiny: δ_chiral(optical) ≈ 1.7×10⁻⁹ is ~11 OOM below
the ~10⁻¹⁹–10⁻²⁰ SME cavity bounds. **Negligible at optical/X-ray scales, quantified.** It
is a genuine srs-DISTINCT prediction (a vacuum optical-activity that diamond structurally
cannot host), living far below current bounds — surfaced honestly, not as a near-term chord.

### Readout (4) — the diamond reference + the (qℓ)⁴ FORM comparison

The bond-moment identities (the corpus's ACTUAL node-up (qℓ)⁴ claim, `clm-k4d4ph` §2):

| Carrier | point group | ⟨(q̂·d̂)²⟩ spread | ⟨(q̂·d̂)⁴⟩ = κ·(q̂ₓ⁴+q̂ᵧ⁴+q̂_z⁴)+c, κ | cubic-harmonic resid | first anisotropic invariant |
|---|---|---|---|---|---|
| **srs** | 432 (chiral cubic) | **1.7×10⁻¹⁶** (isotropic) | **−1/12** | 1.9×10⁻¹⁶ | **QUARTIC** |
| **diamond** | m3̄m (centro cubic) | **2.2×10⁻¹⁶** (isotropic) | **−2/9** | 2.8×10⁻¹⁶ | **QUARTIC** |

**The (qℓ)⁴ suppression FORM is a property of BOTH cubic point groups**, not a diamond-
specific fact. The corpus argued it on "Fd3̄m diamond-cubic averaging" — but the load-bearing
mechanism (the 2nd bond moment carries no angular dependence, the 4th is the pure cubic
harmonic) holds identically on the chiral z=3 srs net. **The migration re-clears the FORM;
only the coefficient value changes (−1/12 vs −2/9), which is an ECHO either way.**

---

## 3. THE PHYSICAL PICTURE (what re-cleared, and what did not)

**What re-cleared on srs (the P1 gate content):**
- The **leading-order emergent-Lorentz light-cone** (c isotropic to machine precision, both
  transverse branches degenerate) — cubic-symmetry-automatic, now carrier-native.
- The **(qℓ)⁴ anisotropy-suppression FORM** — the first cubic anisotropy is quartic on 432
  exactly as on m3̄m. The isotropy defense is NOT diamond-specific; it survives the migration.
- **No cold birefringence** — the transverse pair is degenerate; the Letter's baseline holds.

**What is srs-DISTINCT (new on the ratified carrier):**
- A **chiral k-linear acoustic-gyrotropy** term (432 permits, m3̄m forbids) — parity-odd,
  geometry-fixed, and negligible (~10⁻⁹ at optical). A genuine but tiny new channel; the
  diamond never had it.

**What is UNCHANGED (this arc did NOT re-open it):**
- The **raw acoustic-branch dispersion anisotropy is O(k²)** on both carriers (order n=2.0001,
  matching the merged srs_bloch slope 1.9999). The distinctive **(qℓ)⁴ photon-DISPERSION**
  tell remains **CONDITIONAL on the unproven weak-C no-zone-edge theorem** (gate `wejkhvnfb`,
  Grant-confirmed OPEN). The migration re-clears the FORM + the isotropy; it does not prove
  weak-C. The 🟡 demotion of `clm-k4d4ph` STANDS.

This is the FORM-deriving / VALUE-importing meta-finding once more: the isotropy FORM is
carrier-native (holds on 432 as on m3̄m), the coefficient VALUE is an ECHO (−1/12 vs −2/9,
both below LIV bounds), and the weak-C lever that would upgrade the (qℓ)⁴ dispersion from
conditional to derived is untouched by the carrier change.

---

## 4. FALLOUT DISPOSITIONS (per the frozen fallout map — [ISOTROPY-EMERGES] column)

The isotropy-defense sites S1–S5 are **RE-CLEARED** on srs. These are auditor-lane manual
landings (the implementer surfaces; the auditor lands per lane discipline) — enumerated for
the auditor queue:

| Site | Disposition |
|---|---|
| **S1** `clm-k4d4ph` (`k4-bloch-dispersion-quartic.md`) | RE-CLEARED: the (qℓ)⁴ bond-moment FORM is carrier-native (holds on srs-432 with κ=−1/12, and on diamond-m3̄m with κ=−2/9). The 🟡 weak-C demotion is UNCHANGED (the raw eigensolve is O(k²) on BOTH carriers). **Add a carrier line:** the FORM re-clears on the ratified srs-z3 carrier; the diamond was an equivalent-order instrument, not the sole host. |
| **S2** `preferred-frame-and-emergent-lorentz.md:22,56` (`clm-yr6tu4`) | RE-CLEARED: the (qℓ)ⁿ suppression + SME-bound comparison survives on srs. The "first anisotropic invariant for cubic point group is quartic" statement is TRUE for 432 as for m3̄m. **Re-state:** the suppression is a cubic-point-group fact (432 ∈ cubic), carrier-native; the diamond-cubic phrasing over-specifies. The δ_aniso ≈ 2.2×10⁻²² optical number is an ECHO either way (below SME bounds). |
| **S3** `00_foreword.tex:106` | ok — the "optical isotropy of a diamond crystal despite anisotropic unit cell" ANALOGY stays valid (a chiral-cubic crystal is equally optically isotropic at O(k⁰)). Optional re-word "diamond crystal" → "cubic crystal" for carrier-neutrality (cosmetic; not load-bearing). |
| **S4** `the-abandoned-interior.md:180,185` | The crystalline-side isotropy defense is RE-CLEARED on the ratified carrier: the srs crystal delivers the cubic averaging (the (qℓ)⁴ FORM) node-up. The **crystalline-vs-amorphous seam (line 185) is PARTIALLY closed** on the crystalline side; the amorphous trace-reversal (ν=2/7) side stays a separate open item (per the srs-micropolar result: K=2G stays GR-imported). The seam narrows but does not fully close — surface as such. |
| **S5** the c′ Fd3̄m-averaging site (`axiom1-dof-restoration_note.md` §c′) | CLEARED for migration: srs delivers equivalent isotropy. This specific c′ derivation-use (the Fd3̄m averaging → (qℓ)⁴) is re-derived on srs here; it is NO LONGER a migration STOP. (The other ~28 c′ sites — Bethe-lattice admittance, K=2G form, water z/3, etc. — are OUT of this arc's scope; they migrate on their own P2 gates.) |

**NEW forward statement to add (srs-distinct):** the chiral k-linear vacuum acoustic-activity
δ_chiral ≈ 1.7×10⁻⁹·(qℓ_node) — a 432-permitted, diamond-forbidden, parity-odd term ~11 OOM
below current LIV bounds. Not a near-term falsifier; a genuine carrier-native prediction the
diamond could not host. (Auditor-lane: whether this earns a Letter line or a KB-leaf entry is
an auditor/Grant framing call — surfaced, not landed here.)

**Migration P1 disposition:** the P1 acceptance gate CLEARS. The α-chain re-clearance is a
SEPARATE P1 leg (this arc did the Lorentz leg); the migration proceeds on the Lorentz
finding. The diamond stays a documented instrument (its (qℓ)⁴ story is reproduced here as
V1); it is NOT retained as the sole α/Lorentz host — the Lorentz chain is now carrier-native.

---

## 5. HONEST SCOPE / WHAT THIS DOES NOT CLAIM

- **Not a weak-C proof.** The (qℓ)⁴ photon-DISPERSION stays conditional on gate `wejkhvnfb`.
  This arc re-clears the isotropy FORM + the light-cone, not the zone-edge decoupling.
- **Not an emergence claim.** CONSISTENCY / FORM-class throughout; α-CLEAN. The isotropy is a
  cubic-symmetry FORM fact, the coefficients are ECHOs.
- **The chiral term is negligible, stated as such** — a real srs-distinct channel far below
  bounds, not a bankable near-term chord.
- **`mass = A1` untouched.** (PR#260 / #311 ECHO-final.)
- **The α-chain P1 leg is separate** and not addressed here (the migration policy's P1 gate
  named α AND Lorentz; this is the Lorentz leg).

---

## 6. UPSTREAM / CROSS-REFS (verified at HEAD `43151be1`)

- Parent: `src/scripts/vol_4_engineering/srs_bloch_dispersion.py` (P1b.3, merged `19a31836`)
  — the 24×24 srs eigensolve slope 1.9999. This arc extends it (dense sphere, both transverse
  branches, chiral term, diamond reference, guards); does NOT re-open its weak-C verdict.
- Stage-2 micropolar: `research/2026-07-04_srs-chiral-micropolar_result.md` — B parity-odd,
  σ^A/lever channel, diamond null M1, enantiomorph M2. The chiral term here is its k-space face.
- Infrastructure consumed (first full consumer): `ave.core.micropolar_bloch`,
  `ave.core.carrier` (diamond instrument-scoped), `ave.validation.structural_degeneracy`
  (`detect_symmetry_forced_zero` chiral-parity guard).
- Migration policy: `_orchestration/2026-07-03_srs-migration-policy.md` (P1 gate).
- Tracker: `_orchestration/2026-07-04_engine-upgrade-program.md` (item-3).
- Demoted (qℓ)⁴ claim: `clm-k4d4ph`; weak-C gate `wejkhvnfb` OPEN.

# PREREG (FROZEN) — LORENTZ-ON-SRS: photon-sector isotropy / emergent-Lorentz chain on the chiral srs-z3 carrier

**Date:** 2026-07-04 · **Lane:** implementer · **Branch:** `analysis/lorentz-on-srs`
**Arc:** the srs-migration policy's **P1 acceptance gate** (the FINAL item of the
engine-upgrade program, item-3).
**FROZEN AT:** commit prior to any srs anisotropy number (this file lands before the driver).
**Grant standing order (2026-07-03 D1 RATIFICATION / migration policy):** *"the Lorentz
chain must re-clear on srs or the migration STOPS."*

> **STATUS: FROZEN.** Bins, fallout map, adjudication criteria, and validation gates below
> are frozen BEFORE any srs anisotropy number is computed. No post-hoc bin invention; no
> dropping adjudication criteria to convert a bin. If a prediction fails decisively and a
> single mechanism explains it, that is honest closure (Rule 11); the migration STOP
> condition is a legitimate bin, not a failure to be rescued.

---

## SUBSTRATE-FIRST SECTOR HEADER (stated before any standard-physics term)

- **SECTOR:** the **translational (u) sector** of the chiral srs-z3 net — the 24×24
  Bloch dynamical matrix D(k) (8 Wyckoff-8a sublattices × 3 translational DOF). The
  **photon** is the long-wavelength, sub-saturation, Z₀-matched LC-ladder regime of the
  substrate's transverse-translational acoustic branches (the two u-dominated massless
  transverse branches; the corpus's "unlocked continuum photon"). This is the SAME sector
  and the SAME operator the merged `srs_bloch_dispersion.py` (P1b.3, on `main` @
  `19a31836`) already runs — this arc EXTENDS it (dense direction sphere, symmetry-allowed
  form, both transverse branches, chiral k-linear term, diamond reference, harness guards).
- **REGIME:** **cold linear, sub-yield, saturation OFF.** This is a band-structure /
  dispersion-relation calculation, NOT a time-domain LC run. Consequences (substrate-native-check):
  - No Op14 saturation ⇒ **no local-clock modulation** `ω_local = ω_global·√(1−A²)` (A²=0);
    the uniform-σ eigensolve is the correct instrument (Checkpoint 5 N/A).
  - No time-domain evolution ⇒ **no reactance-pair (C-state/L-state) tracking** required
    (Checkpoint 6 N/A — a linear eigenvalue problem has no phase to snapshot).
  - No PML, no field-density top-K extraction ⇒ **sampling discipline N/A** (Checkpoint 7).
  - The photon isotropy point is the **isotropic-bond point k_s = k_a** (Zener A=1, the
    emergent-Lorentz point where the elastic tensor's O(k⁰) directional split vanishes).
    The generic-ρ (k_s≠k_a) acoustic branch carries an O(k⁰) Zener split — that is the
    MATTER branch's elastic anisotropy, NOT the photon. The photon rides the iso point.
- **COORDS (A46):** **spatial-Brillouin k-space.** The corpus claim — δ_aniso ∼ (qℓ_node)ⁿ,
  c-isotropy, the SME cavity bounds — is itself a k-space dispersion-relation claim. The
  test measures ω(k) in the SAME k-space. **Coordinates MATCH; A46-clean.** This is NOT a
  (V_inc,V_ref) Clifford-torus phase-space claim; no phase-space↔real-space mismatch risk.
- **CLASS (consistency-vs-emergence):** **CONSISTENCY / FORM-class.** The FORM facts
  (leading-order c isotropic; the leading anisotropic correction order n; which n the point
  group 432 PERMITS) are node-up from-geometry eigensolve facts, matching the parent leaf
  `clm-k4d4ph`'s own CONSISTENCY/FORM-class tag. The MAGNITUDE (a coefficient, a δ at
  optical scale) is an ECHO (a lattice-geometry number, quantified honestly, ~OOM vs LIV
  bounds). **α-CLEAN:** no α / Q_TANK on the verdict path; c₀, Z₀, ℓ_node imported by
  SYMBOL from `ave.core.constants`. The anisotropy order n and the c-isotropy are read off
  the eigenvalues, NOT a baked exponent (the exact failure `srs_bloch_dispersion.py` §2
  demotion caveat names for the old hardcoded slope-4).

---

## 1. THE CORPUS CLAIM BEING RE-CLEARED (the isotropy-defense sites)

The corpus's photon-sector isotropy / emergent-Lorentz defense is **diamond-cubic-tied**:
every load-bearing statement argues the anisotropy suppression on **Fd3̄m diamond-cubic
averaging**. Enumerated (verify-before-cite'd at this arc's HEAD):

| # | Site (file:line) | The diamond-tied statement | Class |
|:--:|:--|:--|:--|
| S1 | `manuscript/ave-kb/vol4/falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md` (`clm-k4d4ph`) | "first directional anisotropy is the cubic harmonic Ξ=q̂ₓ⁴+q̂ᵧ⁴+q̂_z⁴ at order (qℓ)⁴ … symmetry-protected by the diamond-cubic (Fd3̄m) point group" | CONSISTENCY/FORM (already 🟡 DEMOTED: genuine srs eigensolve measured slope 1.9999, a₄ SUBDOMINANT to a₂; quartic conditional on the unproven weak-C no-zone-edge theorem, gate `wejkhvnfb`) |
| S2 | `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md:22,56` (`clm-yr6tu4`) | "δ_aniso ∼ (qℓ_node)⁴ ≈ 2.2×10⁻²² at λ=633 nm; current cavity bounds ∼10⁻¹⁹–10⁻²⁰ per SME operator (Nagel 2015, Sanner 2019); 2–3 OOM below bound" + "first anisotropic invariant for cubic point group is quartic" | consistency; the SME-facing statement |
| S3 | `manuscript/frontmatter/00_foreword.tex:106` | "$\delta_{aniso}\sim(q\ell_{node})^4\approx2.2\times10^{-22}$" + "optical isotropy of a diamond crystal despite anisotropic unit cell" | framing |
| S4 | `manuscript/ave-kb/common/the-abandoned-interior.md:180,185` | "The diamond-cubic (Fd3̄m) symmetry … averages directional anisotropy away … suppressing optical-scale anisotropy to (qℓ_node)⁴ ≈ 10⁻²²" + the flag-don't-fix crystalline-vs-amorphous seam | CONSISTENCY framing; explicitly names this as an open seam in the isotropy defense |
| S5 | the c′ site list, `research/2026-07-03_axiom1-dof-restoration_note.md` §(c′) | ~29 z=4-as-K4-coordination derivation-uses; the isotropy defense is the load-bearing one this arc addresses (the Fd3̄m averaging) | migration P1/P2 territory (physics re-derivation, NOT documentation edit) |

**The re-clearance question (frozen):** does the isotropy/emergent-Lorentz chain hold when
the carrier is the RATIFIED chiral **srs-z3** net (point group **432**, chiral cubic,
space group **I4₁32**) instead of the achiral **diamond** (point group m3̄m, Fd3̄m)? The
change of carrier changes: (a) the point group (432 chiral vs m3̄m centrosymmetric); (b) the
coordination (z=3 vs z=4); (c) whether a chiral k-linear (gyrotropic / optical-activity)
term is symmetry-PERMITTED (432 permits it; m3̄m forbids it by centrosymmetry).

---

## 2. THE COMPUTATION (uses the NEW hardened infrastructure — first full consumer)

Infrastructure consumed (all merged at HEAD `43151be1`):
- **`ave.core.micropolar_bloch`** — the 6-DOF (u,φ) Bloch machinery; the translational
  sub-block is the photon sector. Its `B_signed` extraction (the tr(M_tr) acoustic-gyrotropy
  pseudoscalar) is the chiral k-linear term of #3.
- **`ave.core.chiral_lattice.build_srs_net`** / `build_diamond_net` — the srs (carrier) and
  diamond (instrument) lattices, with the new `carrier` field.
- **`ave.core.carrier`** — the `require_instrument_scope` guard (the diamond reference of #4
  passes `instrument_scope=`).
- **`ave.validation`** — `planted_source_control`, `structural_degeneracy`
  (`detect_symmetry_forced_zero` for the chiral-term parity guard), the harness guards of #5.
- **`ave.topological.operator_registry`** — the certified `srs_incidence` set (carrier-tag).

### Step 1 — Photon-branch isotropy at low k + the leading anisotropic correction order n
- Extract the two transverse-translational (u-dominated massless) branches of the 24×24
  srs Bloch D(k) at the **isotropic-bond point k_s = k_a** (the emergent-Lorentz point).
- Compute ω(k) along **[100], [110], [111]** and a **dense direction sphere** (≥50 directions,
  Fibonacci-sphere) at small |k|.
- Extract **c(θ,φ) at leading order** (k→0) and the **leading ANISOTROPIC correction**: fit
  ω²/(c₀²k²) = 1 + Σₙ aₙ(kℓ)ⁿ, report the LOWEST n with a DIRECTION-DEPENDENT coefficient
  (the leading anisotropic order) and its coefficient. Read n off the eigenvalues (NOT baked).
- **Symmetry check (HALT-gated, instrument-bug guard):** derive analytically what leading
  anisotropy point group **432** PERMITS (the cubic-harmonic argument: the first
  direction-dependent cubic invariant is the QUARTIC Ξ=q̂ₓ⁴+q̂ᵧ⁴+q̂_z⁴; rank-2 and the
  isotropic |q|² are cubic-invariant, so O(k⁰) and O(k²) directional splits are
  symmetry-FORBIDDEN at the iso point). Verify the numerics land on the symmetry-allowed
  form. **A mismatch (a direction-dependent term at an order 432 forbids) = instrument bug
  ⇒ HALT** (run the planted-reference check before calling it physics).

### Step 2 — Light-cone universality (c direction-independent at k→0; cold-birefringence)
- Is c(θ,φ) direction-independent at k→0 exactly (cubic symmetry forces rank-2 tensors
  isotropic — this should be symmetry-automatic; the QUESTION is the correction order/size)?
  Report the k→0 cross-direction speed spread (→0 = isotropic, machine precision).
- **Do the two transverse branches share c?** (Birefringence of the cold lattice itself =
  zero?) Report c_T1(k→0) − c_T2(k→0) along each direction and averaged. **Any splitting is
  load-bearing for the Letter's baseline** — surface immediately if nonzero.

### Step 3 — The chiral correction (k-linear rotatory / optical-activity term)
- Does the handedness introduce **k-linear** (rotatory / optical-activity) terms in the
  photon sector? Point group **432 PERMITS gyrotropy** (it is one of the 15 gyrotropic
  classes; unlike m3̄m which forbids it by centrosymmetry).
- Compute the **acoustical-activity coefficient** for the u-branches (the `B_signed` /
  `M_tr`-trace acoustic-gyrotropy scalar from `micropolar_bloch`; connects to the micropolar
  B of the Stage-2 srs-chiral-micropolar arc, `research/2026-07-04_srs-chiral-micropolar_result.md`).
- **State its size at optical / X-ray scales HONESTLY** (likely negligible — quantify in
  dimensionless (qℓ_node) units, don't wave). Report the enantiomorph sign-flip
  (parity-odd falsifier: coefficient(left) = −coefficient(right)).

### Step 4 — Diamond reference (validate-on-known + the honest migration comparison)
- Run the IDENTICAL extraction on the **diamond stencil** (`build_diamond_net`,
  instrument-scoped per the carrier guard: `instrument_scope="Lorentz-on-srs P1 gate: the
  diamond validate-on-known / the corpus's claimed (qℓ)⁴ story reproduction"`).
- Does it reproduce the corpus's claimed **(qℓ)⁴** story (leading anisotropy quartic,
  Ξ-form, first cubic harmonic)? This is the validate-on-known: the corpus's OWN carrier
  must read its OWN claimed order, or the instrument is broken.
- **Diamond has NO chiral term** (centrosymmetric Fd3̄m forbids gyrotropy) — the diamond
  chiral coefficient MUST be ≈0 (a second null control, mirroring the srs-micropolar M1).

### Step 5 — VALIDATION (harness guards on every readout)
- **Planted anisotropic reference:** push a KNOWN-order-n anisotropic dispersion (a
  synthetic ω²/c²k² = 1 + c_n·Ξ·(kℓ)ⁿ for a planted n∈{2,4}) through the SAME fit pipeline;
  assert the readout recovers the planted n. (The `srs_bloch_dispersion.py` §2 caveat proves
  the fit returns 4.0 on a synthetic quartic — I generalize: plant BOTH n=2 and n=4, assert
  the reader distinguishes them; this is the `planted_source`-pattern for the order-reader.)
- **Structural-degeneracy check on the direction-sphere fit:** assert the cubic-harmonic
  design matrix on the direction set is NOT rank-deficient (the fit is not reading a
  degeneracy). Assert the chiral (parity-odd) coefficient is NOT symmetry-forced-zero on a
  NON-symmetric field (via `detect_symmetry_forced_zero`: it IS forced to 0 on a
  parity-symmetric input, and the diamond null confirms the reader is not hallucinating).
- **Both-enantiomorph slope invariance:** the anisotropy order n and c-isotropy must be
  IDENTICAL for right vs left (parity-even); only the chiral k-linear term flips sign.

---

## 3. FROZEN BINS (verbatim from the standing order)

- **[ISOTROPY-EMERGES]** — leading-order c isotropic (cross-direction spread → machine
  precision), the leading anisotropic correction is (qℓ)ⁿ with **n ≥ 2** stated +
  coefficient reported; the symmetry-allowed form (432) is matched. **P1 gate CLEARS — the
  migration proceeds; the Letter's emergent-Lorentz stance is reinforced (now carrier-native,
  not diamond-borrowed).**
- **[COLD-BIREFRINGENCE]** — the two photon (transverse) branches split at k→0 (c_T1 ≠ c_T2).
  A **load-bearing finding for the Letter baseline** — surface immediately.
- **[LEADING-ORDER-ANISOTROPY]** — c direction-dependent at k→0 (would contradict cubic
  symmetry). **Treat as instrument bug FIRST** (run the planted-reference + symmetry checks);
  physics ONLY if it survives every guard.
- **[P1-FAILS]** — the correction is parametrically **LARGER on srs than the corpus's
  diamond-based claims assumed** (e.g. leading anisotropy at n < 4 in a way the diamond did
  NOT have, or a chiral k-linear term of a magnitude that pushes above an SME bound). **The
  migration policy's STOP condition** — book honestly, enumerate the exposed SME/Letter
  statements (S1–S5), surface to Grant.
- **[STUCK-FRAMING]** → Grant (a plumber-physical reframe needed before a verdict).

---

## 4. FALLOUT MAP (frozen BEFORE any srs number — the exposed statements per bin)

| Bin | S1 `clm-k4d4ph` | S2 SME leaf `clm-yr6tu4` | S3 foreword | S4 abandoned-interior seam | S5 c′ list |
|:--|:--|:--|:--|:--|:--|
| **ISOTROPY-EMERGES** | RE-CLEARED on srs: the FORM (isotropy + leading-anisotropy order) is carrier-native, not diamond-borrowed. The 🟡 weak-C demotion is UNCHANGED (srs slope was already 1.9999 — a₄ subdominant; the quartic stays conditional on weak-C). Add a carrier-declaration line (432/srs). | RE-CLEARED: the (qℓ)ⁿ suppression + SME-bound comparison survives on srs (re-state n + coefficient for 432, note the diamond was an equivalent-order INSTRUMENT). Add carrier line. | ok (the diamond-crystal ANALOGY stays valid — a chiral-cubic crystal is equally optically isotropic at O(k⁰)); optionally re-word "diamond crystal" → "cubic crystal". | the crystalline-vs-amorphous seam PARTIALLY closed on the crystalline side (the srs crystal delivers the cubic averaging on the ratified carrier); the amorphous trace-reversal side stays a separate open item. | the Fd3̄m-averaging c′ site is CLEARED for migration (srs delivers equivalent isotropy). |
| **COLD-BIREFRINGENCE** | the "no birefringence of the cold lattice" implicit baseline is BROKEN — surface; the (qℓ)⁴ FORM is a separate axis (may still hold for one branch). | the SME baseline (δ_aniso as the ONLY optical anisotropy) gains a NEW channel (cold birefringence) — a NEW load-bearing forward statement for the Letter. | re-word needed. | the isotropy-defense gains a new exposed channel. | flag. |
| **LEADING-ORDER-ANISOTROPY** | if it SURVIVES the guards: the (qℓ)⁴ FORM is FALSIFIED on srs (leading anisotropy at O(k⁰/k²)) — but this contradicts 432 cubic symmetry, so almost certainly instrument bug. HALT + planted-ref first. | S2 exposed only if it survives guards. | — | — | — |
| **P1-FAILS** | the FORM claim is worse on srs than diamond — enumerate exactly which order/coefficient. | the SME-bound comparison MUST be re-stated with the srs number; if above a bound, the falsifiable-surface statement is EXPOSED. | exposed. | the isotropy defense STOPS on the crystalline side — the seam WIDENS. | the c′ Fd3̄m site is a STOP for migration; diamond retained as documented α/Lorentz instrument (per migration policy P1 gate escape). |
| **STUCK-FRAMING** | no change until Grant. | — | — | — | — |

---

## 5. VALIDATE-ON-KNOWN GATES (HALT if any fails — no verdict on a broken instrument)

| # | Gate | Target | HALT-on |
|:--:|:--|:--|:--|
| **V0** | srs acoustic speed recovers c₀; Z₀ recovered | isotropic v_lat, Z rel-err → 0 | fail ⇒ the model is wrong (mirrors `srs_bloch_dispersion.py` §0) |
| **V1** | diamond validate-on-known reproduces the corpus (qℓ)⁴ claim | diamond leading anisotropy = quartic, Ξ-form | if diamond does NOT read its OWN claimed order, the instrument is broken (HALT before trusting the srs read) |
| **V2** | planted n=2 and n=4 references read back their planted order | order-reader recovers 2 and 4 | fail ⇒ the fit floor is contaminated (the exact §2-caveat trap) |
| **V3** | diamond chiral term ≈ 0 (centrosymmetry null) | diamond gyrotropy coefficient < 1e-8 | fail ⇒ the chiral extractor is hallucinating (mirrors srs-micropolar M1) |
| **V4** | enantiomorph parity: n + c isotropic even; chiral term odd | R/L: n,c identical; chiral sign-flips | fail ⇒ a parity-odd term leaked into an even observable (or vice versa) |

---

## 6. CARRIER DECLARATION (migration policy rule 3)

**This arc's verdict is rendered on the srs-z3 production carrier** (the whole point of the
P1 gate). The diamond reference (#4/V1) is explicitly **instrument-scoped** via
`ave.core.carrier.require_instrument_scope(..., instrument_scope="…")` — a validate-on-known
+ honest-comparison consumption of the non-canonical instrument, acknowledged, not a verdict
carrier. The verdict box of the result doc states `carrier: srs-z3`.

---

## 7. EE-CANON / UPSTREAM POINTERS (verified at HEAD)

- Parent driver: `src/scripts/vol_4_engineering/srs_bloch_dispersion.py` (P1b.3, merged
  `19a31836`) — the 24×24 srs eigensolve; measured slope 1.9999, a₂=+0.0556 (isotropic
  zone-edge) dominant over a₄=−0.0017; c(k→0)=1/√3 isotropic, cross-axis spread 2.75e-5.
  **This arc extends it; it does NOT re-open its slope verdict (that stays weak-C-conditional).**
- Stage-2 micropolar: `research/2026-07-04_srs-chiral-micropolar_result.md` — B parity-odd,
  σ^A/lever channel, diamond null M1, enantiomorph sign-flip M2. The chiral k-linear term
  of #3 is the k-space dispersion face of this same B pseudo-tensor.
- The demoted (qℓ)⁴ claim: `clm-k4d4ph` (already 🟡 demoted; weak-C gate `wejkhvnfb` OPEN).
- Migration policy: `_orchestration/2026-07-03_srs-migration-policy.md` (P1 acceptance gate).
- Engine-upgrade tracker: `_orchestration/2026-07-04_engine-upgrade-program.md` (item-3).
</content>
</invoke>

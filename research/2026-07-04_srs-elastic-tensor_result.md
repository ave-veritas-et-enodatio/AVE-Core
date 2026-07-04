# RESULT — The srs Elastic-Tensor Arc: the crystalline srs-z3 does NOT force ν=2/7

**Date:** 2026-07-04 · **Lane:** implementer · **Branch:** `analysis/srs-elastic-tensor`
**Driver:** `src/scripts/vol_1_foundations/srs_elastic_tensor.py`
**Output:** `_output/srs_elastic_tensor.json` (driver-regenerable; D3 gitignored)
**Prereg (FROZEN):** `research/2026-07-04_srs-elastic-tensor_prereg_FROZEN.md`
**Carrier declaration (D1 policy 3):** RATIFIED chiral **srs-z3** (`build_srs_net`,
I4₁32, Wyckoff-8a, 8 sublattices, z=3). NOT the diamond-z4 instrument.

---

## VERDICT BOX

> **PRIMARY BIN: [ANISOTROPIC-BREAKDOWN]**, compound with **[DIFFERENT-ν]**.
>
> The Cauchy-grade elastic tensor of the chiral **srs-z3** net, computed from the
> engine-native BORN rank-2 bond model `Φ_b = k_a·d̂⊗d̂ + k_s·(I−d̂⊗d̂)` via the
> Born-Huang method of long waves (internal-strain relaxed), is a **ONE-PARAMETER
> FAMILY in ρ = k_a/k_s** — exactly the Maxwell sub-isostatic structure (z=3 < 2d=6:
> shear rigidity is a bond-bend object; K/G is a free stiffness ratio). It does
> **NOT force ν = 2/7**. ν_Hill = 2/7 is reached **only** at an externally-supplied
> `ρ* ≈ 9.7734`, and at that ρ* **K/G_Hill = 2.0000 exactly** — i.e. ν=2/7 appears
> precisely because K=2G there (the algebraic consequent ν=2/7 ⟺ K=2G), NOT as an
> independent lattice determination. At that ρ* the **Zener anisotropy A = 1.229**
> (materially anisotropic, like z=4 diamond's 1.21) — so "a single ν" is an averaging
> choice, not a lattice output. The only Zener-isotropic point (ρ=1, A=1) is
> **mechanically unstable** (bulk modulus K < 0). This **mirrors and STRENGTHENS** the
> z=4 diamond K=2G-provenance finding (PR#261) on the RATIFIED z=3 carrier:
> **K=2G stays GR-IMPORTED; the crystalline substrate does not select ν=2/7.**

**The seam (the-abandoned-interior.md:183) does NOT close in favor of the crystalline
picture subsuming the amorphous ν=2/7.** The amorphous-EMT averaging (z₀≈51.25) that
produces ν=2/7 does **not** transfer to the crystalline srs carrier — the crystalline
calc gives a one-parameter family with the same GR-imported-ρ* structure as z=4.

> **↗ CROSS-LINK (2026-07-04, PR #518 MERGED — the matter-stiffening derivation): the GR-imported
> cold ρ*≈9.77 here is APPROACHED IN DIRECTION by a saturated ρ_eff mechanism, but reaching the
> same ν=2/7 tensor from the saturated bonds is UNTESTED.** A follow-on arc runs the canon-forced
> composition **ρ_eff = ρ_cold·(S_axial/S_shear)** (ρ_cold=1, Ax3-forced): under asymmetric
> shear-channel loading, the SATURATED effective ratio ρ_eff rises (STIFFENS) off the cold ρ=1
> point and crosses this result's ρ*=9.77 — so the DIRECTION toward the matter Poisson point is a
> canon-forced Ax4 mechanism. **But (mandatory honest framing) it does NOT derive the /7 value:**
> the crossing is at an arbitrary wall-amplitude (A_wall=0.99479, not canon-distinguished), the
> electron's actual wall OVERSHOOTS ρ_eff→∞, and — the load-bearing regime caveat carried verbatim
> (flag-don't-fix) — **the ρ*=9.77 of THIS result is a COLD bond ratio** (per the §"SUBSTRATE-FIRST
> SECTOR HEADER (as run)" REGIME line, verbatim: "cold linear, sub-yield, saturation OFF"), whereas
> ρ_eff is a **SATURATED** effective ratio; the RATIO
> VARIABLE (k_a/k_s) is the same, but **driving the saturated ρ_eff to 9.77 is NOT proven to land
> the same ν=2/7 / K=2G elastic tensor** as setting the cold ρ=9.77 here — that would require a
> Born-Huang run on the saturated Φ_b, which is UNTESTED (a running arc tests exactly this
> cold-vs-saturated gap; this cross-link does NOT pre-judge it). **K=2G / the /7 value stays
> GR-imported** (PR #506, this result). Provenance:
> `research/2026-07-04_matter-stiffening-rho_result.md` (VERDICT BOX + §6 + §8). *(This result body
> is a frozen record; banner-append only.)*

---

## SUBSTRATE-FIRST SECTOR HEADER (as run)

- **SECTOR:** translational (Cauchy-grade) sector of chiral srs-z3 (24×24 D(k),
  8 Wyckoff-8a sublattices × 3 DOF). BORN rank-2 bond tensor on the z=3 bonds. Cosserat
  couple-stress = Stage 2, NOT invoked (Cauchy answer is not ambiguous — the family is
  clean, see §5).
- **REGIME:** cold linear, sub-yield, saturation OFF. Handedness saturation-only ⇒
  cold C_ij parity-symmetric (both enantiomorphs identical to 2e-9; §3).
- **COORDS (A46):** real-space / spatial-Brillouin (acoustic slopes → C_ij → ν, Zener,
  K/G). The ν=2/7 claim is itself a real-space moduli ratio. Coordinates match.
- **CLASS:** CONSISTENCY. α-CLEAN (no α/CODATA/Q_TANK on the verdict path; ratios only).
  **NO tuning of ρ toward 2/7** — the fallout map was frozen FIRST (prereg), the guard.

---

## 1. VALIDATE-ON-KNOWN (all PASS, HALT-gated) — the pipeline is trustworthy

The numeric Born-Huang long-wave → C_ij pipeline was validated against known lattices
BEFORE the srs numbers were read. All on the SAME extraction the srs uses.

| # | Known lattice | Target | Recovered | Verdict |
|---|---|---|---|---|
| V1 | simple-cubic central-force (k_a on 6 axial, k_s=0) | C11=k_a, C12=0, C44=0, ν=0 | C11=1.00000, C12=−9e−10, C44=9e−10 (resid 1.1e−8) | **PASS** |
| V2 | z=4 diamond Born vs SYMBOLIC-verified analytic (3 cases ρ=1,1.52,2) | C44/C11 & C12/C11 = the symbolic Born ratios | numeric = symbolic to **< 2e−9** | **PASS** |
| V3 | isotropy sanity (SC, k_a=k_s) | Zener A = 1 | A = 1.00000 | **PASS** |

**V2 is the load-bearing cross-check.** The z=4 diamond Born-model C_ij were derived
SYMBOLICALLY (sympy long-wave with internal-strain elimination):
`C11 ∝ (k_a+2k_s)/24`, `C44 ∝ k_s(2k_a+k_s)/(8(k_a+2k_s))`, `C12 ∝ (k_a−4k_s)/24`. The
numeric pipeline reproduces these to < 2e−9 — the extraction is the same model's
analytic answer, computed numerically. This is what licenses the srs number.

**Resolution + robustness (Rule 10):** the finite-difference step h is converged to ~7
digits for h ∈ [1e−2, 1e−4] (degrades only at 1e−6 roundoff; default h=1e−4). The cubic
fit is identical to 5 digits across 3 / 10 / 15 direction sets (residual ~1e−8). An
**independent direct-eigensolve** of the small-k acoustic branches along [100] recovers
the same C11=0.72786, C44=0.24876 at ρ*=9.77 — cross-validating the long-wave method.

---

## 2. THE THREE READOUTS (frozen; reported whatever they say)

### Readout 1 — ν vs 2/7: a one-parameter family; ν=2/7 only at K=2G-imported ρ*

The full ν(ρ) curve (right enantiomorph; ρ = k_a/k_s, k_s=1):

| ρ | C11 | C12 | C44 | K = (C11+2C12)/3 | Zener A | ν_Hill |
|---|---|---|---|---|---|---|
| 0.500 | +0.1237 | −0.1945 | +0.1473 | **−0.0884** | 0.926 | +2.51 |
| 1.000 | +0.1768 | −0.1768 | +0.1768 | **−0.0589** | 1.000 | (K=0 pole) |
| 1.520 | +0.2184 | −0.1516 | +0.1950 | **−0.0283** | 1.054 | −2.20 |
| **2.000** | +0.2525 | −0.1263 | +0.2062 | **0.0000** | 1.089 | −1.00 |
| 3.000 | +0.3182 | −0.0707 | +0.2210 | +0.0589 | 1.136 | −0.31 |
| 5.000 | +0.4419 | +0.0442 | +0.2357 | +0.1768 | 1.185 | +0.06 |
| 5.305 | +0.4604 | +0.0619 | +0.2371 | +0.1948 | 1.190 | +0.09 |
| 7.000 | +0.5625 | +0.1607 | +0.2431 | +0.2946 | 1.210 | +0.20 |
| **9.7734** | +0.7279 | +0.3232 | +0.2488 | +0.4308 | **1.229** | **+0.2857 = 2/7** |
| 10.000 | +0.7413 | +0.3364 | +0.2491 | +0.4714 | 1.231 | +0.29 |

- **K (bulk modulus) is NEGATIVE for ρ < 2** — mechanically unstable (the lattice would
  collapse under hydrostatic pressure). **K = 0 EXACTLY at ρ = 2** (bisection-located to
  1e−6). Stable (K>0) only for ρ > 2.
- **ν diverges through the K=0 pole** at ρ=2; a raw "ν crosses 2/7" is a divergence
  artifact. The honest, K>0-gated read: **ν_Hill = 2/7 is reached only at ρ* ≈ 9.7734**
  (in the stable branch), an externally-supplied value.

### Readout 2 — Zener isotropy: materially anisotropic where it matters

- Zener A = 2C44/(C11−C12). **The only A = 1 point is ρ = 1**, where **K < 0
  (unstable)** — ν is undefined (diverges).
- **At the ν=2/7 point (ρ*≈9.77), A = 1.2293** — materially anisotropic, essentially
  identical to z=4 diamond's A=1.21. So "a single ν" is a Voigt/Reuss/Hill averaging
  choice, not a bare lattice output (the [ANISOTROPIC-BREAKDOWN] condition). The VRH
  ν-spread at ρ* is small (ν_Voigt=0.2848, ν_Reuss=0.2867, ν_Hill=0.2857) but the
  underlying Zener anisotropy A=1.23 is real and direction-resolved (§4 slope table).

### Readout 3 — K=2G: not forced; where ν=2/7, K/G=2 exactly (the consequent)

- 2G/K = 1 is **NOT forced at any geometrically-distinguished ρ** — K/G(ρ) is a smooth
  one-parameter family (K/G_Hill sweeps from negative, through the K=0 pole, up through
  2 and beyond as ρ grows).
- **At the ν=2/7 point (ρ*≈9.77), K/G_Hill = 2.0000 exactly.** This is the algebraic
  identity ν=2/7 ⟺ K=2G (`vacuum-poisson-ratio.md`, `clm-x19btt`) confirming itself:
  ρ* is located precisely where K=2G, i.e. **ρ* is K=2G RE-IMPORTED, not an independent
  crystalline determination.** Same structure as z=4 (`k2g-crystalline-provenance:60`:
  "geometry fixes the form; it cannot fix the value; to land on K=2G you must supply ρ*
  from outside").

---

## 3. Enantiomorph parity (the cold-spectrum falsifier)

Both enantiomorphs ('right' I4₁32, 'left' I4₃32) give **identical cold C_ij** (max
relative hand-difference **2.15e−9**). This confirms the header substrate fact: the
4₁-screw handedness is saturation-only (`cosserat_field_3d.py:562`), so the cold elastic
tensor is parity-symmetric. A nonzero hand-difference would have signalled a bond-operator
bug. No chiral chord lives in the cold Cauchy tensor — CORRECT, as pre-registered.

---

## 4. Per-direction acoustic-slope table (the deliverable Born-Huang table)

`ρ·c² = ρ(ω/k)²` acoustic eigenvalues along the symmetry directions (right enantiomorph):

**At ρ = 3 (stable representative):**

| Direction | T (low) | T (mid/high) | L |
|---|---|---|---|
| [100] | 0.22097 | 0.22097 | 0.31820 |
| [110] | 0.19445 | 0.22097 | 0.34471 |
| [111] | 0.20329 | 0.20329 | 0.35355 |

**At ρ* = 9.7734 (the ν=2/7 / K=2G point):**

| Direction | T (low) | T (mid/high) | L |
|---|---|---|---|
| [100] | 0.24876 | 0.24876 | 0.72786 |
| [110] | 0.20235 | 0.24876 | 0.77426 |
| [111] | 0.21782 | 0.21782 | 0.78973 |

The directional split of the transverse slopes ([100]_T = 0.2488 vs [110]_T1 = 0.2024
vs [111]_T = 0.2178) **IS the Zener anisotropy** (A = 1.229), direction-resolved. At the
iso-bond point (ρ=1) all directions collapse to 0.17678 (A=1, but K<0 unstable).

---

## 5. Scope: Cauchy grade is sufficient — Cosserat Stage 2 NOT needed

The Cauchy answer is **not ambiguous** (the ρ-family is clean, the K=0 floor and the
ν=2/7 ρ* are sharply located, both hands agree, resolution converged). Per the prereg's
scope declaration and `axiom4-moduli:24` (`ℓ_c²=γ/G` is a within-bend-sector ratio,
ORTHOGONAL to ρ=k_a/k_s at the k→0 Cauchy slopes), the Cosserat couple-stress (`G_c, γ`)
does NOT enter the k→0 elastic tensor. **Stage 2 is declared unnecessary, not skipped.**

---

## 6. FALLOUT MAP EXECUTION — [DIFFERENT-ν] status-demotions (flag-don't-fix)

The frozen fallout map (prereg §FALLOUT MAP) executes as HONEST status-demotions. **These
are SURFACED for auditor + Grant adjudication, NOT landed by this implementer lane.** The
verdict does NOT break GR agreement (the /7 PPN numbers are calibrated in independently at
the deflection-integral level, `predictions.yaml` P10 `type: consistency_check`); it
removes the *crystalline substrate grounding* for WHY ν=2/7.

| Fallout site | Rides ν=2/7 how | Status-demotion under [DIFFERENT-ν] |
|---|---|---|
| `trace-reversal-mechanism.md` (`clm-rd9cjm`) | amorphous-EMT z₀≈51.25 crossing at K/G=2 | THE SEAM: the amorphous averaging does NOT transfer to the crystalline srs carrier. The crystalline calc gives a one-param family, not a forced ν=2/7. The "geometric consequence of the network topology" reading (already Rule-12'd out 2026-06-21) is FURTHER confirmed: neither z=4 NOR z=3 forces K=2G. |
| `vacuum-poisson-ratio.md` (`clm-x19btt`) | ν=2/7 ⟺ K=2G algebraic identity | UNCHANGED (the identity holds; the srs calc confirms it — where ν=2/7, K=2G exactly). This is the "one firm link" and it is NOT demoted. |
| `constants.py:573 NU_VAC=2/7`, `:356 N_NU`, `:570 ISOTROPIC_PROJECTION=1/7` | the value / its projections | value UNCHANGED (GR-imported via K=2G); the *provenance claim* that it is amorphous-network-derived is the demotion target. |
| `constants.py:717 V_LONG=√(2G/ρ)` "From K=2G (EMT)" | longitudinal speed hard-set by K=2G | the "(EMT)" attribution is now doubly-superseded: K=2G is GR-imported (not EMT-forced), and the crystalline srs calc gives a one-param family. Re-attribute to GR-imported K=2G. |
| the three /7 PPN couplings (`gravity-ppn-coherence-result.md`) | (2/7) transverse index, (9/7) label, temporal | UNCHANGED at the GR-number level (calibrated independently); the ν_vac=2/7 "axiom-derived (K=2G trace-reversal)" tag (`:138`) is CONFIRMED as GR-imported, NOT crystalline-derived. |

**No rewrites performed.** The claims-register update (§7) proposes status-demotion /
strengthen ROWS only; the auditor lane lands the manual entries.

## 7. Claims-register proposal (rows ONLY; auditor lands)

Proposed for `research/` cross-ref + the auditor's manuscript queue (NOT landed here):

1. **STRENGTHEN** the K=2G "GR-imported" grade (`k2g-crystalline-provenance_result.md`,
   PR#261): now confirmed on the RATIFIED z=3 srs carrier (not just z=4 diamond). The
   crystalline substrate — at BOTH coordinations the axiom has named — does not force
   ν=2/7 / K=2G. New forward evidence: `srs_elastic_tensor.py`.
2. **STATUS-DEMOTE** the implication (if any leaf carries it) that the crystalline srs
   carrier grounds ν=2/7 by subsuming the amorphous averaging. It does not (the-abandoned-
   interior.md:183 seam stays OPEN on the crystalline side; the amorphous EMT and the
   crystalline family give different structures, both needing K=2G supplied externally).
3. **FLAG (new)** the three-way bond-model discrepancy (§8) for adjudication.

---

## 8. flag-don't-fix — the three-way bond-model discrepancy (SURFACED, not resolved)

A substrate-native tension surfaced at validate-on-known time that I do NOT resolve
unilaterally (flag-don't-fix; a bond-model framing question for auditor + Grant):

**The engine-native BORN 2-body bond model gives DIFFERENT elastic constants than BOTH
the Keating angle-bend model AND the corpus `clm-bjceop` form — on the same lattice.**

- **The engine's srs machinery** (`srs_bloch_dispersion.py:80`) uses the BORN rank-2
  tensor `Φ_b = k_a·d̂⊗d̂ + k_s·(I−d̂⊗d̂)` — a 2-body central + non-central spring per bond.
  This is what I used (it is the engine-native carrier model).
- **The K=2G-provenance driver** (`k2g_crystalline_provenance.py:9-13`) used the KEATING
  angle-bending model (3-body: penalizes bond-ANGLE changes). On z=4 diamond this gives
  ν≈0.067 (C12/C11=+0.20 at ρ=2).
- **The pure BORN model on z=4 diamond gives ν=−1, K=0 at k_a=2k_s** (C12/C11=−0.50) —
  auxetic, zero bulk modulus. Verified symbolically (§1 V2).
- **The corpus `clm-bjceop:1073`** states `K_0=4k_a+8k_s, G_0=8k_s ⟹ K=2G ⟺ k_a=2k_s` —
  which keeps K finite at k_a=2k_s, so it is NEITHER the pure Born NOR the Keating
  normalization I can reproduce.

**These are three different force models giving three different C_ij.** The srs verdict
above uses the engine-native Born model (the honest choice for the ratified carrier). But
**which bond model is canonical for the substrate's Cauchy grade is a physics framing
question** the axioms alone do not settle — surfaced to Grant / the auditor lane. The
verdict's ROBUST content is model-independent: on ALL of {Born-srs, Born-diamond,
Keating-diamond}, the elastic tensor is a **one-parameter family in the stretch/bend
ratio**, and hitting K=2G / ν=2/7 requires an externally-supplied ρ* — the GR-imported
value. The three-way discrepancy affects WHICH ρ* and the shape of the family, NOT the
"K=2G is imported, not lattice-forced" conclusion.

---

## Cross-references (verified at HEAD 2026-07-04)

- Driver: `src/scripts/vol_1_foundations/srs_elastic_tensor.py`
- Prereg (FROZEN): `research/2026-07-04_srs-elastic-tensor_prereg_FROZEN.md`
- Carrier: `src/ave/core/chiral_lattice.py` `build_srs_net`
- srs Bloch machinery (Born bond model): `src/scripts/vol_4_engineering/srs_bloch_dispersion.py:80`
- z=4 analytic template (Keating): `src/scripts/verify/k2g_crystalline_provenance.py`
- K=2G GR-imported (PR#261): `research/2026-06-15_k2g-crystalline-provenance_result.md`
- Bond stiffness ρ=k_a/k_s: `research/2026-07-02_axiom4-moduli-hierarchy_result.md`
- The seam: `manuscript/ave-kb/common/the-abandoned-interior.md:183`
- ν=2/7 ⟺ K=2G identity: `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md`
- amorphous provenance (z₀≈51.25): `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/trace-reversal-mechanism.md:18-22`
- D1 migration policy: `_orchestration/2026-07-03_srs-migration-policy.md`

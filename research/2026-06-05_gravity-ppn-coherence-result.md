# RESULT — AVE gravity PPN internal-coherence audit

**Status:** COMPLETE, 2026-06-05. Implementor session, branch `analysis/gravity-ppn-coherence`.
**Prereg (frozen):** [`2026-06-05_gravity-ppn-coherence-prereg.md`](2026-06-05_gravity-ppn-coherence-prereg.md)
**Verification script:** `src/scripts/verify/gravity_ppn_coherence.py` (+ `_results.json`)
**Class:** Consistency-class **internal-coherence** audit. NOT an emergence test, NOT an AVE-distinctness claim. The corpus already classifies gravitational lensing/Shapiro/perihelion as "AVE = GR at O(GM/c²r), no AVE-distinct observable" (Class C). This audit asks only whether AVE's gravity sector is *internally coherent* across its coefficient-bearing statements.

## Verdict (one line)

**Internally INCONSISTENT — walk-back needed.** The canonical "`n_spatial = 1 + (9/7)ε₁₁` *controls light deflection*" statement is the **outlier**: taken literally it gives a deflection **4.5× GR** and a perihelion **3.33× GR**, contradicting the corpus's own light-deflection derivation (4GM/bc²) and Ch 14 perihelion (43″). The surviving coherent chain uses the **(2/7) transverse index** for the photon, which gives γ=1, δ=4GM/bc², and (with β=1) the 43″ perihelion — all consistent with GR and with each other.

---

## 1. The canonical structures (verbatim, verify-before-cite 2026-06-05 @ HEAD)

The audit touches **four** coefficient-bearing gravity statements (the brief named three; reading the actual deflection derivation surfaced a fourth, the Gordon-form lensing index, which matters for the normalization caveat in §7).

**(S1) One-strain-field two-index decomposition.** `manuscript/common_equations/eq_gravity_derived.tex:50-54` and `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md:14-19` (clm-rd9cjm):
> `ε₁₁ = 7GM/(c²r)` … `n_temporal = 1 + (2/7)ε₁₁` (controls clock rate, redshift); `n_spatial = 1 + (9/7)ε₁₁` (controls light deflection)

Restated in `manuscript/ave-kb/common/translation-tables/translation-gravity.md:16`:
> Temporal: `n_t(r) = 1 + (2/7)ε₁₁ = 1 + 2GM/(rc²)` (clock rate, redshift); Spatial: `n_s(r) = 1 + (9/7)ε₁₁` (light deflection).

**(S2) The actual light-deflection derivation.** `manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex:185-206` (§`sec:double_deflection`), cross-validated `03_macroscopic_relativity.tex:146-153`, indexed `predictions.yaml` P10 (clm-zf8eah):
> Light (transverse coupling). A photon is a purely transverse Cosserat shear wave … couples … to the transverse cross-sectional strain … `n_⊥(r) = 1 + ν_vac χ_vol(r) = 1 + (2/7)χ_vol(r)` … With `χ_vol(r) = 7GM/(c²r)` … `δ_light = 4GM/bc²` (Einstein 1915).

**This derivation uses the (2/7) transverse index for the photon — NOT the (9/7) "spatial" index.** Op19 (`operators.md:59`) likewise pins the canonical gravity refractive index as `n(r) = 1 + ν_vac·ε₁₁ = 1 + 2GM/(rc²)`.

**(S3) Ch 14 hand-set perihelion potential.** `manuscript/vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex:66-77`:
> `V_tidal(r) = −GM/r(1 + 3GM/c²r)` … `Δφ = 6πGM/(c²a(1−e²))` … ≈ 43 arcseconds per century — the identical result obtained by General Relativity.

**(S4) Gordon-form lensing index.** `manuscript/ave-kb/common/translation-tables/translation-gravity.md:23` + `02_general_relativity_and_gravity.tex:137`:
> Gravitational lensing | Optical refraction (n>1) | `n(r) = (1+r_s/2r)³/(1−r_s/2r)`.

This is the **full GR isotropic optical index** (it already encodes both the temporal and spatial metric sectors); weak-field it expands to `n ≈ 1 + 2r_s/r = 1 + 4GM/c²r`. See §7 for why this does NOT mean "deflection = 8GM/bc²".

## 2. Phase 1 — light deflection + PPN γ

**Symbolic core (verified by `symbolic_refraction_deflection_coeff`).** For a static radial index `n(r) = 1 + K·GM/(c²r)`, the weak-field geometric-optics (Snell-gradient) deflection is the transverse-gradient integral along the unperturbed path:

  δ = −∫ (∂n/∂b) dz = **2K · GM/(bc²)**  (sympy-closed-form; numerically reconfirmed via `scipy.quad`).

(The along-path derivative ∂n/∂z is odd in z and integrates to zero — the physical bending is the transverse gradient.) This is exactly the kernel the corpus invokes ("Integrating Snell's Law through this specific refractive gradient", `03_macroscopic_relativity.tex:147`).

Feeding each canonical index through this **same kernel** (grazing Sun, b = R_⊙):

| Photon index | slope K | δ (Snell-gradient) | δ numeric | ratio to GR | implied PPN γ |
|---|---|---|---|---|---|
| **(2/7)** `n_⊥ = 1 + 2GM/c²r` (S2, Op19) | 2 | **4GM/bc²** | **1.7517″** | **1.0000** | **γ = 1** ✓ |
| **(9/7)** `n_spatial = 1 + 9GM/c²r` (S1 label) | 9 | **18GM/bc²** | **7.8827″** | **4.5000** | γ = 8 (standalone) / 9/2 (as g_ij coeff) ✗ |

- **The (2/7) reading reproduces GR exactly** (γ=1, 4GM/bc² = 1.7517″ = observed 1.75″). This IS the corpus's canonical deflection derivation (S2). Coherent.
- **The (9/7) reading overshoots by 4.5×** (18GM/bc² = 7.8827″). The factor 4.5 = (9/7)/(2/7) is **kernel-independent**: whatever deflection kernel you adopt, the (9/7) index bends light 4.5× as much as the (2/7) index. Since the (2/7) index is what gives GR's 4GM/bc², the (9/7) index cannot also give 4GM/bc². The S1 label "`n_spatial` … controls light deflection" is therefore **inconsistent with S2's 4GM/bc²**.

**PPN-γ phrasing of the prereg's H1.** The prereg's leading prior estimated "γ ≈ 4.5 → ~11GM/bc² (~2.75×)". The clean derivation refines this: if `n_spatial` (the (9/7) index, = 1 + 9U with U=GM/c²r) is read as the PPN spatial metric `g_ij = (1+2γ_eff U)` *relative to* the temporal sector `n_temporal = 1 + 2U`, then γ_eff = (9/7)/(2/7) = **9/2 = 4.5**; PPN deflection 2(1+γ) would then be in units of the temporal scale. Read instead as a **standalone refractive index of slope 9**, the Snell deflection is 18GM/bc² (γ-equivalent 8). Both readings are large mismatches with GR's 4GM/bc²; the prereg's qualitative H1 (the (9/7) label cannot coexist with 4GM/bc²) is **confirmed**, with the exact multiple depending on how literally the (9/7) index is interpreted as a metric coefficient vs a refractive index.

## 3. Phase 2 — perihelion + PPN β

The PPN perihelion advance per orbit is `Δφ = F · 6πGM/(c²a(1−e²))` with `F = (2 − β + 2γ)/3` (GR: β=γ=1 → F=1). Mercury elements (a=5.79×10¹⁰ m, e=0.2056, T=87.969 d) are external observational inputs; M=M_⊙ imported from `ave.core.constants`.

| Perihelion source | PPN factor F | Δφ (″/century) | ratio to GR/43″ |
|---|---|---|---|
| **(S3) Ch 14 coeff-3** `V_tidal ~ 1+3GM/c²r` | F=1 (= GR) | **42.9996″** | **1.0000** ✓ |
| metric with **γ=9/2** (S1 9/7 reading), β=1 | F = (2−1+9)/3 = **10/3** | **143.33″** | **3.3333** ✗ |
| metric with **γ=1** (S2 2/7 reading), β=1 | F = (2−1+2)/3 = 1 | 42.9996″ | 1.0000 ✓ |

- **Ch 14's coeff-3 V_tidal gives exactly GR's 43″** (42.9996″ with these elements; the famous 42.98″). The "3" in `(1 + 3GM/c²r)` is the standard GR effective-potential `1/r³` coefficient — it IS the GR result, hand-written as a static potential. Ch 14 makes **no independent statement of γ**; the coeff-3 potential is equivalent to PPN (2γ+2−β)/3 with β=γ=1.
- **If the (9/7)-spatial γ=4.5 were fed into the perihelion**, F=10/3 → 143.33″ (3.33× GR). This is the same (9/7) inconsistency propagating into the orbital sector.
- **The metric does NOT independently fix β.** No canonical AVE statement derives β; the corpus's perihelion (S3) is the GR value by construction. So Phase 2 cannot, on its own, *test* AVE's β — it can only check that the coeff-3 potential equals GR (it does) and that the (9/7) γ, if used, would break it (it would).

**Does the metric-derived perihelion equal Ch 14's hand-set value?** Only under the **(2/7)/γ=1 reading** (both give 42.9996″). Under the **(9/7) reading** it does not (143.33″ vs 43″). So S3 is consistent with S2's index but not with S1's (9/7) label.

## 4. Phase 3 — coherence verdict + the outlier

**Do Phases 1+2 follow from ONE ε₁₁ calibration?** ε₁₁ = 7GM/(c²r) is **canonical, not a free calibration** (`03_macroscopic_relativity.tex:45`, decomposition leaf:14) — it is fixed by the Poisson Green's-function solve. The (2/7) and (9/7) projections of that *one* ε₁₁ are what diverge: (2/7)ε₁₁ = 2GM/c²r and (9/7)ε₁₁ = 9GM/c²r.

**Coherence matrix** (all four structures fed through matched coordinates / matched kernel):

| | implied γ | deflection | perihelion (β=1) | coheres with GR? |
|---|---|---|---|---|
| (S2) (2/7) transverse index | 1 | 4GM/bc² ✓ | 43″ ✓ | **YES** |
| (S3) Ch 14 coeff-3 V_tidal | (=1) | — | 43″ ✓ | **YES** |
| (S4) Gordon isotropic index | 1 | 4GM/bc² ✓ (see §7) | — | **YES** |
| (S1) (9/7) "spatial" index | 9/2 | 18GM/bc² ✗ (4.5×) | 143″ ✗ (3.33×) | **NO** |

**Classification: internally-INCONSISTENT-needs-walkback.**

**The outlier is (S1)'s `n_spatial = 1 + (9/7)ε₁₁` "controls light deflection" statement.** Three of the four structures (the actual deflection derivation S2, Op19, Ch 14's perihelion S3, and the Gordon lensing index S4) cohere at γ=1 / 4GM/bc² / 43″. Only the (9/7) "controls light deflection" label is the odd one out — and it is contradicted *within the same file that states it*: `eq_gravity_derived.tex` carries BOTH `eq:gravity_refraction` (`n(r) = 1 + 2GM/rc²`, line 26 — the (2/7) photon index) AND `eq:lattice_decomposition` (`n_spatial = 1 + (9/7)ε₁₁ … controls light deflection`, line 54). These cannot both be the index the photon refracts through.

**Why (9/7) is the outlier and not the others:**
- S2 is a *full derivation* (Cosserat transverse-shear coupling → 2/7 Poisson projection → Snell integral → 4GM/bc²), cross-validated against the K4-TLM lattice simulator (`02_general_relativity_and_gravity.tex:220-229`), and is the entry indexed in `predictions.yaml` (P10). It is load-bearing and exercised.
- S1's (9/7) "controls light deflection" is a **one-line label** in a decomposition table; no derivation in the corpus takes the (9/7) index through a deflection integral. The (9/7) value also has no cited origin — `axiom-homologation.md:210` merely restates it; `Δn = n_spatial − n_temporal = ε₁₁` (the eq_gravity_derived comment) is the only structural constraint, i.e. n_spatial is *defined* as n_temporal + ε₁₁ = 1 + (2/7)ε₁₁ + ε₁₁ = 1 + (9/7)ε₁₁. That makes the (9/7) a bookkeeping sum, not a deflection-calibrated coefficient.
- S3 and S4 independently land on the GR value.

**Secondary inconsistency (temporal sector, factor of 2).** `n_temporal = 1 + (2/7)ε₁₁ = 1 + 2GM/c²r` implies a redshift z = n_t − 1 = **2GM/c²r**, but the same files (`eq_gravity_derived.tex:63`, decomposition leaf:24) state the redshift is "z ≈ **GM/(c²r)**" — the GR value, which is HALF. So even the (2/7) temporal index over-predicts the *redshift* by 2× relative to the corpus's own stated z ≈ GM/c²r, even though it gives the *deflection* correctly (because deflection only cares about the index gradient through the Snell kernel, and the 4GM/bc² number is reproduced by K=2). This is a separate normalization knot in the temporal sector — flagged, not resolved (see §7, §8).

**The (2/7) index is the correct GR photon index — not a coincidence.** A leading-order check confirms `√(g_ij/−g₀₀)` for the GR isotropic metric (−g₀₀=1−2U, g_ij=1+2U) is exactly `1 + 2U = 1 + 2GM/c²r` — i.e. AVE's (2/7) transverse index. So S2 reproduces GR's deflection *honestly* (right index, right kernel), strengthening the verdict that the (9/7) statement is the outlier rather than S2 being a fluke.

**Every natural way of folding the (9/7) spatial index into the photon path mismatches GR** (all fed through the Snell kernel δ=2K·GM/bc²):

| photon-index reading | K (slope in U) | deflection | × GR |
|---|---|---|---|
| (2/7) index alone = √(g_ij/−g₀₀)_GR | 2 | 4GM/bc² | **1.00 ✓** |
| (9/7) index alone | 9 | 18GM/bc² | 4.50 ✗ |
| √(n_s · n_t) [n_s→g_ij, n_t→−g₀₀] | 11/2 | 11GM/bc² | 2.75 ✗ |
| (n_s + n_t)/2 | 11/2 | 11GM/bc² | 2.75 ✗ |
| √(n_s / n_t) | 7/2 | 7GM/bc² | 1.75 ✗ |

The prereg's H1 "(9/7) → ~11GM/bc² (~2.75×)" corresponds exactly to the **√(n_s·n_t)** / mean reading; the standalone-(9/7) reading gives 4.5×. **No reading using the (9/7) value reproduces 4GM/bc²; only the (2/7) value does.**

## 5. Verification-script numbers (AVE-derived vs GR/observed, side by side)

Source: `src/scripts/verify/gravity_ppn_coherence.py` → `gravity_ppn_coherence_results.json`. Imports `G=6.674300e-11`, `C_0=2.997925e+08`, `M_SUN=1.989000e+30` from `ave.core.constants`. External inputs: Mercury a=5.79×10¹⁰ m, e=0.2056, T=87.969 d (NASA JPL); R_⊙=6.957×10⁸ m (IAU 2015). No hard-coded GR targets — GR values recomputed from the same imported constants.

**Phase 1 — light deflection (grazing Sun):**
```
GR (4GM/bc^2)                     : 1.7517 arcsec   (observed ~1.75")
AVE (2/7) transverse index n_perp : 1.7517 arcsec   ratio 1.0000   PPN gamma=1.000  COHERES
AVE (9/7) spatial index n_spatial : 7.8827 arcsec   ratio 4.5000   PPN gamma=8.000  MISMATCH
```

**Phase 2 — Mercury perihelion:**
```
GR / Ch 14 coeff-3 (F=1)          : 42.9996 arcsec/century   (observed/GR ~43")
metric IF gamma=9/2, beta=1 (F=10/3): 143.3322 arcsec/century  ratio 3.3333  MISMATCH
metric IF gamma=1,   beta=1 (F=1)   : 42.9996 arcsec/century  ratio 1.0000  COHERES
```

**Symbolic:** refraction-deflection coefficient = 2K (verified, sympy); PPN deflection coeff = 2(γ+1); PPN perihelion factor = (2−β+2γ)/3.

## 6. consistency-vs-emergence classification (load-bearing — Phase 3)

**Skill fired:** `consistency-vs-emergence` v1.3, **Trigger 5** (compare a computed AVE observable to another framework's prediction — GR deflection/perihelion — with overlapping inputs). The skill body explicitly names "solar deflection via lattice refraction recovering 4GM/bc²" and "perihelion precession recovering GR weak-field result" as **canonical Class C** examples.

**Inputs traced (Step 2):**
- `G` — CODATA-derived (constants.py); the deflection/perihelion derivations route through G via the standard weak-field formulae. Removing G destroys the prediction → **Class C structural dependence**.
- `C_0` — defined SI value; `M_SUN` — IAU observational; Mercury a/e/T — JPL observational.
- `ν_vac = 2/7` — axiom-derived (K=2G trace-reversal), with the `trace-reversal-mechanism.md:22` honest-α caveat that the K/G=2 crossing sits at α by construction.

**Class designation (Step 3 / Step 7 / Step 8):**
- The underlying observables (deflection, perihelion) are **Class C consistency checks** — exactly as `predictions.yaml` P10 already tags P10 `type: consistency_check` and the corpus's "AVE = GR at O(GM/c²r)" classification states. Agreement (where it holds) is **structural, not predictive**: the (2/7) index is calibrated such that its weak-field reduction equals √(g_ij/−g₀₀)_GR.
- **This audit is one level meta:** it does not assert "AVE reproduces GR" (already Class C); it asks whether AVE's *internal statements* of that Class-C reproduction are mutually coherent. The deliverable is a **coherence fact about the corpus**, not a physics claim. **No promotion past any canonical ceiling occurs (Step 8 clean): nothing here is reclassified upward.** The finding is a flag (one canonical statement contradicts three others), surfaced for adjudication — NOT a fix applied in this session.
- **Honest framing:** the (2/7) chain's reproduction of GR is **consistency-class** — NOT AVE-distinct (`ave-discrimination-check`: there is no SM/GR-counterfactual-distinguishing observable here; AVE = GR at this order by construction). The result must NOT be headlined as an emergence or distinctness claim.

## 7. pre-test-physics-check — surfaced framing questions (did NOT halt; question is well-posed)

The prereg flagged: STOP if a mid-derivation framing question makes the question ill-posed. Two load-bearing framing questions surfaced; **neither makes the question ill-posed** (the 4.5× / 2.75× mismatches are kernel-invariant in the relevant sense), so per the scope guard I completed both phases and surface them here rather than halting:

1. **Which index does the photon actually use — (2/7) or (9/7)?** The corpus is internally contradictory: S1/translation-table say "n_spatial=(9/7) controls light deflection"; S2/Op19/the actual derivation use n_⊥=(2/7). **Resolved by the derivation:** the (2/7) index is √(g_ij/−g₀₀)_GR and gives 4GM/bc²; the (9/7) cannot. The question is well-posed and answered — the (9/7) label is wrong/outlier.

2. **Kernel normalization — Snell-gradient (δ=2K·GM/bc²) vs the full-isotropic-index relativistic kernel.** The Gordon full isotropic index (S4) weak-field expands to 1+4GM/c²r (slope 4); naively fed through the Snell kernel that would give 8GM/bc². But the full isotropic index already double-counts temporal+spatial, so it must be used with the relativistic photon-orbit kernel, which gives 4GM/bc². **This does not affect the verdict** because the (9/7)-vs-(2/7) comparison is done with the *same* kernel, and the ratio 4.5 = (9/7)/(2/7) is kernel-independent. Flagged so the auditor is not tripped by "S4 expands to slope-4 — doesn't that contradict the (2/7) slope-2 photon index?" Answer: no — S4 is the √(g_ij/−g₀₀)-style *full* index in a different normalization convention (it equals `(1+r_s/2r)³/(1−r_s/2r)`, whose proper-kernel deflection is 4GM/bc² = γ=1, consistent with S2).

**A third question for Grant (framing-level, queued — not for me to resolve):** the temporal-sector factor-of-2 (n_temporal−1 = 2GM/c²r vs the stated redshift z ≈ GM/c²r). Is `n_temporal` intended as the clock index (slope should be 1) or as something else (e.g. the g₀₀-perturbation magnitude 2U, with the clock index being √ of it)? The corpus maps n_temporal directly to redshift and states z≈GM/c²r, so as written there is a 2× internal tension in the temporal sector independent of the (9/7) spatial issue. This is a **plumber-physical** question: *if `n_temporal` is the "how slow does a clock tick" index, its slope should be 1 (to give z = GM/c²r), but the corpus writes slope 2/7·7 = 2 — are these two different quantities wearing the same `n_temporal` hat?*

## 8. Walk-back queue (NOT applied here — for a separate adjudicated session)

Per scope guards, no canonical leaf or Ch 14 is edited in this session. Queued for adjudication:

- **W1 (primary):** The "`n_spatial = 1 + (9/7)ε₁₁` … *controls light deflection*" label is the outlier. Candidate resolutions for Grant/auditor: (a) the (9/7) index is correct for *frame-dragging / a different observable* but the "controls light deflection" annotation is wrong and should point at the (2/7) transverse index; (b) (9/7) is a bookkeeping artifact (n_temporal + ε₁₁) with no deflection role and the annotation should be removed. Affected leaves: `temporal-spatial-lattice-decomposition.md:19`, `eq_gravity_derived.tex:54+64`, `translation-gravity.md:16` (all carry the same "(light deflection)" label on the (9/7) index).
- **W2 (secondary):** temporal-sector factor-of-2 (n_temporal slope 2 vs redshift z ≈ GM/c²r slope 1). Needs Grant framing adjudication (§7 Q3) before any edit.
- **W3 (redundancy, low-priority):** Ch 14's coeff-3 V_tidal is the GR result hand-written as a static potential; it is consistent with the (2/7) metric (both → 43″) but is NOT *derived from* n_temporal/n_spatial. If the unifying-law framing is pursued, V_tidal could be re-derived from the metric rather than stated independently. This is a *redundancy*, not an inconsistency — Ch 14 cohere with the (2/7) chain.

**Per Rule 12 (substitution-not-retraction):** these are flags for adjudication, not retractions. No slot is refilled; no new hypothesis is asserted. The auditor lands any manual/matrix entries; this implementor session only surfaces the finding.

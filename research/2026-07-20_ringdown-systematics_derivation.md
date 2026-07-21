# Ringdown-Systematics Organizers — DERIVATION + data confrontation (beyond-Kerr deviation analyses from the BH soft-mode transition)

**Date:** 2026-07-20 · **Lane:** RINGDOWN-SYSTEMATICS (`research/ringdown-systematics`) · **FORWARD-PREDICTION class**
**Prereg (FROZEN, pushed ALONE first):** [`research/2026-07-20_ringdown-systematics_prereg-FROZEN.md`](2026-07-20_ringdown-systematics_prereg-FROZEN.md) (commit `f22d0b2d`, pushed before this doc — frozen-first proof).
**Checks:** [`research/2026-07-20_ringdown-systematics_checks.py`](2026-07-20_ringdown-systematics_checks.py) (`math`-only; `ave` byte-untouched; every AVE number traces to a cited corpus formula, every GR number tagged `[import]` and cross-checked against the in-repo Berti anchor).
**Registered candidate:** `research/2026-07-20_vacuum-metallurgy_kz-relic-and-instruments.md` D4a (★CANDIDATE FORWARD CONTENT — surfaced-not-derived; this doc derives it).

> **★ KERR-WORDING FENCE (rides every claim below).** GR quasinormal modes are **(M, a)-determined** (the no-hair theorem — not disputed). Every statement here is an organizer for **beyond-Kerr DEVIATION analyses** (the δf/δτ frameworks a ringdown test already runs), **never** a replacement for the Kerr spectrum. *IF* the ringdown deviates from Kerr, the substrate soft-mode picture predicts the deviation has this STRUCTURE. A null deviation (pure Kerr) is consistent with the substrate at current sensitivity.

---

## §0 — REGIME / SECTOR / PHASE-STATE header (as run)

- **MODE.** Post-merger BH remnant ringing down — the fundamental (and sub-dominant) resonance of the saturation cavity at `r_sat = 7GM/c² = 3.5 r_s`. Contrast column: LIGO/Virgo ringdown modes (ω_R, ω_I/τ) and their beyond-Kerr deviation constraints (δf, δτ).
- **REGIME.** Far-field GW = Regime I (linear lossless shear wave). Cavity boundary = Regime III↔IV **soft-mode transition** (`G_shear → 0`, "topology melts"), quantified as the srs `C_44` collapse `0.17661 → 0.02536 → 4×10⁻⁵` (`research/2026-07-04_saturated-elastic-tensor_result.md` §4 `[canon]`, PR#521).
- **PHASE-STATE.** Cold-reactive far field (Ax3 lossless-reactive; a radiating shear mode is a legal port). Saturated soft boundary (Op14 ON; `Γ_shear = −1` perfect shear reflector, `Γ_EM = 0` — the horizon is black to light: the two-channel instrument, `electron-bh-isomorphism.md:24-47` `[canon]`).
- **COORDS (A46).** All comparisons are in **matching real-space / dimensionless-frequency coordinates**: AVE `ω_R M_g` (dimensionless) vs GR `M ω_R` (dimensionless); mode RATIOS are pure dimensionless numbers. No phase-space vs real-space mismatch — the whole confrontation lives in the dimensionless-eigenvalue register both theories share.
- **CLASS (consistency-vs-emergence).** The banked v2 ω_R/τ MATCH is **CONSISTENCY** (recovering GR Kerr; `lattice-extreme-bh-rationality.md` §4 `[canon]`) — this lane does **not** upgrade it. The two organizers are **forward DEVIATION predictions** (chord-surface): they say what a departure from Kerr would look like. No VALUE is emergence-claimed; ν_vac=2/7 is the corpus input, not re-derived here.

---

## §1 — ORG-1: MODE-RATIO LOCKING (full derivation)

### §1.1 — The chain

The AVE merger-ringdown eigenvalue (`ave-merger-ringdown-eigenvalue.md` resultbox `[canon]`):

$$\omega_R(\ell)\, M_g = \frac{\ell\,(1+\nu_{vac})}{x_{sat}(a_*)}, \qquad \nu_{vac} = \tfrac{2}{7}.$$

The two non-ℓ factors are **properties of the cavity/lattice, not of the multipole**:
- `(1+ν_vac) = 9/7` — a **frozen dimensionless elastic ratio** of the K4 lattice. Per the saturated-elastic-tensor result, ν (and Zener, K/G) are homogeneous **degree-0** in the bond stiffnesses — they do NOT shift with the saturation magnitude (`saturated-elastic-tensor_result.md` §1/§4 `[canon]`: *"a soft region with locked proportions"*).
- `x_sat(a*)` — the cavity radius, **common to all multipoles** (it is the reflecting-boundary geometry, carries no ℓ).

Therefore the multipole frequency RATIO cancels `x_sat` and `(1+ν_vac)` entirely:

$$\boxed{\;\frac{\omega_R(\ell')}{\omega_R(\ell)} = \frac{\ell'}{\ell}\quad\text{EXACTLY, INDEPENDENT of spin }a_*\;}$$

Damping locks the same way: `Q_ℓ = ℓ` (`qnm-quality-factor.md` `[canon]`, the single-channel Op21 mode-count) ⇒ `Q_{ℓ'}/Q_ℓ = ℓ'/ℓ`, so the decay-time ratio `τ_ℓ/τ_{ℓ'} = (Q_ℓ ω_{ℓ'})/(Q_{ℓ'} ω_ℓ)` is likewise set by frozen ratios, not by (M,a).

### §1.2 — The numbers (checks-script output)

Linear-ℓ reading (the corpus form `ω_R = ℓ·c/r_eff`, `ave-merger-ringdown-eigenvalue.md:16`):

| pair | AVE (linear-ℓ) | AVE (√ℓ(ℓ+1) fork) | GR Schwarzschild `[import]` | AVE-lin vs GR | AVE-sph vs GR |
|---|---|---|---|---|---|
| ω(3)/ω(2) | **1.5000** | 1.4142 | 1.6042 | **−6.50%** | −11.84% |
| ω(4)/ω(2) | 2.0000 | 1.8257 | 2.1655 | −7.64% | −15.69% |
| ω(4)/ω(3) | 1.3333 | 1.2910 | 1.3499 | −1.23% | −4.36% |

GR Schwarzschild (a=0) gravitational QNM real parts `[import — Leaver / Berti-Cardoso-Will 2006]`: `Mω(2,0)=0.373672`, `Mω(3,0)=0.599443`, `Mω(4,0)=0.809178`. **Two-method check:** the imported `(2,0)` value 0.373672 agrees with the in-repo canonical Berti table anchor (`ligo_ringdown_driver.py:122`, `a*=0 → 0.37368`) to `2.1×10⁻⁵` relative — so the ℓ=3,4 imports ride the same verified source as the in-repo table.

### §1.3 — The falsifiable signature (fork-independent robust statement)

> **ORG-1 (robust, both forks):** the AVE multipole ratio is **BELOW the Kerr ratio** (1.41–1.50 vs Kerr 1.60 for ℓ=3/ℓ=2) **AND spin-independent (frozen)** — whereas Kerr's ratio is a\*-dependent. The exact point-value (1.500 linear-ℓ vs 1.414 spherical) is UNDETERMINED (§4 fork), but the *below-Kerr + spin-locked* content survives the fork.

The cleanest single test: a higher-mode measurement of `ω_330/ω_220`. Kerr puts it at ≈1.60 (weakly a\*-drifting); AVE puts it at ≤1.50 and *fixed*. A next-gen measurement at ≲5% would separate them.

### §1.4 — Scope honesty (what is NOT derived)

- **Overtone ladder (n≥1):** the corpus derives `ω_R ∝ ℓ` and `Q=ℓ` only for the **fundamental** (n=0). It supplies **no** overtone spectrum. So **overtone-ratio locking is FORM-ONLY-NO-NUMBER** — AVE has no derived `ω_221/ω_220`. This is load-bearing for the confrontation (§3): the best-constrained current test (GW150914 220/221) probes exactly the axis AVE cannot predict.
- **ℓ≥3 extension:** the corpus validated `ω_R ∝ ℓ` only at ℓ=2; ℓ≥3 is a forward reading of the corpus's own membrane-mode form (a corollary), tagged as such — not an independently-validated in-corpus number.

---

## §2 — ORG-2: ARRESTED CRITICAL SLOWING (full derivation)

### §2.1 — The soft-mode scaling law

A displacive transition's soft mode softens as `ω² ∝ (restoring modulus)`. In the substrate the shear-wave speed is `c_shear = c₀√S` (`master-equation`/INVARIANT-S2 `[canon]`), and the absolute moduli scale by the overall saturation factor `S` (`saturated-elastic-tensor_result.md` §4 `[canon]`), so `C_44 ∝ S` and

$$\omega_R \sim \frac{c_{shear}}{r_{eff}} \propto \sqrt{S} \propto \sqrt{C_{44}}.$$

The `C_44` collapse `0.17661 → 0.02536 → 4×10⁻⁵` gives `√(C_44/C_44,cold) = 1.000 → 0.379 → 0.015` — the soft-mode absolute-scale slide. **This is the mechanism**; it is not an independently-measurable observable (C_44 is inferred from the same strain field that sets everything), so on its own it is FORM. It becomes testable through the observable it controls: the spin dependence.

### §2.2 — The rigid-skeleton floor (why the slowing is ARRESTED)

As `a* → extremal` the prograde reflecting boundary moves inward toward the yield wall (where `C_44` is most collapsed) — naively the mode should soften toward zero. But the **rigid `ν_vac=2/7` Cosserat skeleton fraction never softens** (its share of the restoring force is degree-0, the "locked proportions"). The v2 cavity radius (`ave-merger-ringdown-eigenvalue.md` v2 resultbox `[canon]`):

$$x_{sat}(a_*) = 2 + 5\cdot\frac{r_{ph}^+(a_*)}{3M}, \qquad r_{ph}^+ = 2M\left(1+\cos\left[\tfrac{2}{3}\arccos(-a_*)\right]\right)$$

floors at `x_sat → 2 + 5/3 = 11/3` at extremal (never → 2, the pure photon sphere). So:

$$\boxed{\;\omega_R M_g \to \frac{2(9/7)}{11/3} = \frac{54}{77} = 0.7013\ (\ell=2)\quad\text{— the soft mode never softens below the skeleton floor}\;}$$

### §2.3 — The observable systematic (checks-script output)

AVE v2 `ω_R M` vs the in-repo Berti (2,2,0) Kerr table:

| a\* | x_sat | AVE ω_R M | Kerr ω_R M `[import]` | AVE − Kerr |
|---|---|---|---|---|
| 0.00 | 7.000 | 0.3673 | 0.3737 | −1.69% |
| 0.60 | 5.648 | 0.4553 | 0.4638 | −1.84% |
| 0.70 | 5.356 | 0.4801 | 0.4827 | −0.52% |
| 0.80 | 5.019 | 0.5124 | 0.5047 | **+1.53%** |
| 0.90 | 4.596 | 0.5594 | 0.5304 | **+5.48%** |
| 0.95 | 4.311 | 0.5966 | 0.5465 | **+9.16%** |

> **ORG-2 (form + sign, robust):** near-extremal, `ω_R` sits **ABOVE** Kerr (positive excess), growing with spin, floored by the skeleton at `54/77`. The SIGN and FLOOR follow structurally from the rigid `ν_vac=2/7` fraction.

**★ v2-EXTRAPOLATION CAVEAT (load-bearing honesty).** The `+5.5%`/`+9.2%` MAGNITUDES are the v2 formula **extrapolated into `a* ≥ 0.90`**, which the corpus itself flags as the **Option-B regime** (`ligo-ringdown-driver-design.md` §9 `[canon]`: v2 PASSES vs GR only for `a* ≤ 0.85`; "divergence onset a\* ≥ 0.90"). So the exact excess is **Option-B-revisable** — the SIGN/FLOOR are the frozen testable content; the magnitude is carried as an extrapolation, not a validated number.

**Not-a-discriminator (consensus-knife):** `ω_R ∝ 1/M` is IDENTICAL in AVE and Kerr. Mass scaling is NOT where any deviation lives — recorded so a mass-scaling "match" is not miscredited.

---

## §3 — RANK-1 UNIFICATION + DATA CONFRONTATION

### §3.1 — Rank-1 (the two organizers are one deformation)

$$\omega_R(\ell, a_*)\, M_g = \underbrace{[\,\ell\,(1+\nu_{vac})\,]}_{\text{frozen ratios (ORG-1)}} \times \underbrace{[\,1/x_{sat}(a_*)\,]}_{\text{one scale, common to all modes (ORG-2)}}$$

⇒ the AVE beyond-Kerr deviation across the whole multipole spectrum is **RANK-1** (single-parameter). This is the substrate's *most* distinctive and *most* restrictive forward statement: it is MORE predictive than generic beyond-Kerr phenomenology (which allows free per-mode δf, δτ). **FALSIFIER:** a spectroscopy analysis resolving statistically-INDEPENDENT per-mode deviations (δf_220, δf_330 uncorrelated, not a common scale) rules out the soft-mode organizer.

### §3.2 — Confrontation table (current constraints, `[import]`-tagged)

| Current constraint `[import]` | Axis it probes | Sensitivity `[import]` | Organizer it bears on | Verdict |
|---|---|---|---|---|
| **GW150914 220/221 overtone** (Isi+2019 no-hair test) | overtone (n) | postinspiral no-hair ~10%; first-overtone frequency ~20% | ORG-1 **overtone** (FORM-ONLY — AVE has no ω_221 number) | orthogonal — AVE makes no overtone prediction; not a test of ORG-1 |
| **Higher-mode / subdominant events** (GW190521-class, resolved ℓ=3 content) | multipole (ℓ) | ω_330/ω_220 pinned only to ~tens-of-% | ORG-1 **multipole locking** (ratio ≤1.50, spin-independent) | CONSISTENT-UNTESTED — current precision coarser than the 6–12% AVE−Kerr gap |
| **GWTC-3 TGR population** (δf_220, δτ_220) | overall scale (a\*) | δf_220 ~few-%-to-~10%; all events a\*<0.85 | ORG-2 **arrested slowing** (excess only at a\*≳0.9) | CONSISTENT-UNTESTED — the near-extremal regime is UNATTESTED |

**Two-method note on the imports:** the GR Kerr reference values are two-method (in-repo Berti table + independent Leaver values, cross-checked to 2×10⁻⁵ at the anchor). The current-CONSTRAINT levels (Isi+2019 ~10%/~20%; GWTC-3 few-%-to-tens-of-%) are `[import — abstract-level]`: the primary-source *abstracts* were fetched this session (Isi+2019 confirms the ~10% postinspiral / ~20% first-overtone levels); the exact per-event 90% CI widths require the full-PDF tables, **not retrieved this session** — flagged as a citation-completeness limit (verify-before-cite honesty), and the confrontation only load-bears on the *level* (tens-of-%), which is robust across sources.

### §3.3 — Where the organizers sit vs current data

**Neither organizer is ALREADY-EXCLUDED.** Both sit at or below current sensitivity:
- ORG-1 predicts a −6% to −12% multipole-ratio deviation from Kerr, spin-locked; current higher-mode precision (~tens-of-%) cannot resolve it → CONSISTENT-UNTESTED.
- ORG-2 predicts a positive near-extremal excess (+5–9% at a\*≥0.9); the current catalog has no a\*≥0.9 event → CONSISTENT-UNTESTED.
- Next-gen ringdown precision (LISA / Einstein Telescope / Cosmic Explorer, ~1% QNM-deviation sensitivity `[import — forecast-level]`) WOULD test both → both are ORGANIZER-DERIVED-AND-TESTABLE with a stated sensitivity.

---

## §4 — FROZEN-BIN OUTCOME

Per the four bins frozen in the prereg §2:

| Organizer | BIN | Basis |
|---|---|---|
| **ORG-1 multipole-ratio locking** (robust: ratio<Kerr AND spin-independent) | **ORGANIZER-DERIVED-AND-TESTABLE** | derived from `ω_R∝ℓ` + frozen elastic ratios; falsifiable via higher-mode ω_330/ω_220 at ≲5%; CONSISTENT-UNTESTED now |
| **ORG-1 exact point-value** (1.500 vs 1.414) | **UNDETERMINED** | the linear-ℓ vs √(ℓ(ℓ+1)) surface-dispersion fork (§4 prereg) is open; corpus asserts linear-ℓ but does not derive the dispersion |
| **ORG-1 overtone-ratio** (ω_221/ω_220) | **FORM-ONLY-NO-NUMBER** | corpus supplies no n≥1 spectrum; the organizer is structurally real but numberless |
| **ORG-2 arrested critical slowing** (form + sign: ω_R floored above Kerr near extremal) | **ORGANIZER-DERIVED-AND-TESTABLE** | floor/sign follow from the rigid ν_vac=2/7 skeleton; falsifiable via a resolved a\*≳0.9 ringdown; CONSISTENT-UNTESTED now |
| **ORG-2 excess MAGNITUDE** (+5.5%/+9.2%) | **carried as v2-EXTRAPOLATION** (not frozen as a testable number) | Option-B-revisable; the corpus flags a\*≥0.9 as the Option-B regime |
| **RANK-1 unification** (single-parameter deviation) | **ORGANIZER-DERIVED-AND-TESTABLE** (form-level) | falsifiable via multi-mode deviation-correlation; the substrate's most restrictive forward statement |
| `ω ∝ √C_44` scaling law | **FORM-ONLY-NO-NUMBER** (mechanism of ORG-2) | C_44 not independently observable; testable only through the spin dependence it controls |
| mass scaling `ω∝1/M` | **not-a-discriminator** | identical AVE/Kerr |

**Headline (honest):** two beyond-Kerr deviation organizers derived, both DIMENSIONLESS and FALSIFIABLE, both **CONSISTENT-UNTESTED** against current data (neither excluded, neither confirmed), both testable at next-gen ringdown precision. **No bankable negative fired** (nothing is already-excluded); no consistency-class result upgraded (the banked v2 ω_R/τ match stays CONSISTENCY). The distinctive substrate content is the **rank-1 / locked-ratio structure** — a more restrictive deviation shape than free-per-mode phenomenology.

---

## §5 — flag-don't-fix (surfaced, NOT resolved)

1. **The linear-ℓ vs √(ℓ(ℓ+1)) surface-mode dispersion fork (Grant/auditor).** The corpus writes the membrane mode as `ω_R = ℓ·c/r_eff` (LINEAR-ℓ, `ave-merger-ringdown-eigenvalue.md:16`), which gives ORG-1 ratio 1.500. The physical default for a mode on a 2-sphere is `ω ∝ √(ℓ(ℓ+1))` → 1.414. Both are below Kerr (so ORG-1's robust content is safe), but the **exact** number needs a substrate derivation of the surface-mode dispersion the corpus never did. Surfaced, not resolved.

2. **The banked τ-outperformance deserves an error-bar scrutiny (Grant/auditor).** The corpus banks that v2 τ (mean −0.47%) *outperforms* GR Kerr QNM (mean −6.94%) at reproducing the 3 LIGO τ values (`ave-merger-ringdown-eigenvalue.md:64`). This is a genuinely AVE-distinct-looking claim — BUT the LIGO τ values it beats GR on (4.0/3.0/1.4 ms) are quoted to ~1 sig fig; if their measurement uncertainty is ≳10–20%, GR's −7% "miss" and AVE's −0.5% are BOTH consistent with the data and the "outperformance" is within noise. This does not touch the organizers (which live in the a\*≥0.9 and higher-mode regimes), but the τ-outperformance should not be headlined as AVE-distinct without the LIGO τ error bars. Consensus-knife: SM/GR would get the same scrutiny — a −7% offset on a ~15%-error measurement is a match, not a miss.

3. **ORG-2 magnitude is a v2-extrapolation into the Option-B regime (already flagged in-line §2.3).** The sign/floor are robust; the exact +5.5%/+9.2% await the Option-B (full spheroidal cavity) derivation the corpus defers.

---

## §6 — consistency-vs-emergence classification + auditor-queue (implementer SURFACES; auditor LANDS)

**Classification.** The two organizers are **forward DEVIATION predictions** (chord-surface), NOT emergence claims: ν_vac=2/7 and the ringdown eigenvalue are corpus INPUTS, not re-derived here; no VALUE is claimed emergent. The banked v2 ω_R/τ match is CONSISTENCY (recovering GR) and is NOT upgraded. The distinctive content (rank-1 locked-ratio deviation structure) is a **forward falsifiable prediction**, which is where the corpus locates any real chord (`state_of_ave` memory: "chord lives ONLY in forward predictions").

**Auditor-queue (surfaced, NOT landed — no KB/matrix edit in this lane):**
| Site | Proposed disposition (auditor-gated) |
|---|---|
| `lattice-extreme-bh-rationality.md` §4 (ringdown CONSISTENCY row) | **candidate cross-link:** add a pointer to these organizers as the soft-mode DEVIATION forward-content companion to the CONSISTENCY match (no number moves; the match stays consistency-class) |
| `divergence-test-substrate-map.md` C1-BH-RING row | **candidate strengthen:** the "Option B deferrable until a\*>0.90 detection" note now has a *derived deviation organizer* (ORG-2 sign/floor) for that regime; and a higher-mode organizer (ORG-1) orthogonal to the current a\*<0.85 tests |
| `ave-merger-ringdown-eigenvalue.md` | **candidate forward-content note:** the multipole-ratio + rank-1 structure as beyond-Kerr organizers (deviation-scoped, Kerr-wording fence) |
| the τ-outperformance headline (`ave-merger-ringdown-eigenvalue.md:64`) | **candidate scrutiny flag:** error-bar the LIGO τ values before headlining "outperforms GR" (flag-don't-fix item 2) |

No leaf touched; no `clm-` minted; canonical-propagation is a gated follow-on.

---

## §7 — Cross-references (verified at branch HEAD)

- Prereg (FROZEN): `research/2026-07-20_ringdown-systematics_prereg-FROZEN.md` (commit `f22d0b2d`)
- Checks: `research/2026-07-20_ringdown-systematics_checks.py` (`math`-only; `ave` untouched)
- Registered candidate: `research/2026-07-20_vacuum-metallurgy_kz-relic-and-instruments.md` D4a
- Banked ringdown match (CONSISTENCY): `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md` (v2 resultbox, lines 62/64); `research/ligo-ringdown-driver-design.md` §8–§10; `manuscript/ave-kb/common/divergence-test-substrate-map.md` C1-BH-RING row — three-source consistent, no walk-back
- Soft-mode C_44 collapse: `research/2026-07-04_saturated-elastic-tensor_result.md` §4 (PR#521); `electron-bh-isomorphism.md:38`
- Q=ℓ (single-channel Op21): `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/qnm-quality-factor.md`; `op21-multi-mode-mode-counting.md` §1 (BH-ringdown = single-channel row)
- GR Kerr (2,2,0) reference table (in-repo, canonical): `src/scripts/vol_3_macroscopic/ligo_ringdown_driver.py:122` (Berti-Cardoso-Will 2006 Leaver)
- Classification (CONSISTENCY, not emergence): `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md` §4

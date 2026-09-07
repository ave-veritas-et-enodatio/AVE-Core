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
- **CLASS (consistency-vs-emergence).** The banked v2 ω_R/τ MATCH is **CONSISTENCY** (recovering GR Kerr; `lattice-extreme-bh-rationality.md` §4 `[canon]`) — this lane does **not** upgrade it. The two organizers are **forward DEVIATION predictions** (chord-surface): they say what a departure from Kerr would look like. No VALUE is emergence-claimed; `ν_vac=2/7` is a corpus input, not re-derived here — **and its VALUE is `GR-IMPORTED` via `K=2G`** (`form-deriving-value-importing.md:87`/`:407` `[canon]`, PR#261 MERGED: the substrate forces the *form* `K/G=f(ρ)`; the *value* `2/7` is the GR trace-reversal identity, FORM-derived only). So every non-pure-ratio ORG-2 number that rides `ν_vac` — `(1+ν_vac)=9/7`, the `54/77` floor, the `0.3673` cold eigenvalue — inherits a **GR-imported value**; the prereg-header phrase "substrate-derived from the canonical chain (ν_vac=2/7…)" is corrected to **corpus-input, VALUE GR-imported via K=2G, FORM-derived only** (the frozen prereg is byte-untouched; this rider carries the correction). ORG-1's flagship ratio content is `ν_vac`-free (the `(1+ν_vac)` cancels), so it is unaffected.
- **CLAIM-GRADE (K3 / clm-395gps).** Both load-bearing leaves — `ave-merger-ringdown-eigenvalue.md` and `qnm-quality-factor.md` — carry the single claim id **`clm-395gps`** (`claims.jsonl:17`): **solidity `0.55`, `build_status` "use as input only, don't build deeper", `build_band` input-only.** The register holds it below 0.9 because the **Kerr extension is a disclosed phenomenological photon-sphere shift + Cosserat back-reaction fit (v2, refined POST-HOC against LIGO)**, and `Q=ℓ` disagrees with GR overtone structure for `ℓ>2`. The clean core is only the Schwarzschild `ℓ=2` eigenvalue `18/49≈0.3673`; the spinning-remnant comparisons are the disclosed weak edge. **Consequence for this lane:** the two organizers are built on an *input-only, don't-build-deeper* claim, so — even independent of the retracted Kerr-table error — **they cannot grade above input-only**: ORG-1's robust below-Kerr+spin-frozen statement and ORG-2's (now-retracted) sign/floor both **inherit solidity ≤0.55**. The `[canon]` tags on the leaves below are cited WITH this grade wherever they are load-bearing.

---

## §1 — ORG-1: MODE-RATIO LOCKING (full derivation)

### §1.1 — The chain

The AVE merger-ringdown eigenvalue (`ave-merger-ringdown-eigenvalue.md` resultbox `[canon, clm-395gps solidity 0.55, build_status "use as input only, don't build deeper"]` — see §0 CLAIM-GRADE):

$$\omega_R(\ell)\, M_g = \frac{\ell\,(1+\nu_{vac})}{x_{sat}(a_*)}, \qquad \nu_{vac} = \tfrac{2}{7}.$$

The two non-ℓ factors are **properties of the cavity/lattice, not of the multipole**:
- `(1+ν_vac) = 9/7` — a **frozen dimensionless elastic ratio** of the K4 lattice. Per the saturated-elastic-tensor result, ν (and Zener, K/G) are homogeneous **degree-0** in the bond stiffnesses — they do NOT shift with the saturation magnitude (`saturated-elastic-tensor_result.md` §1/§4 `[canon]`: *"a soft region with locked proportions"*).
- `x_sat(a*)` — the cavity radius, **common to all multipoles** (it is the reflecting-boundary geometry, carries no ℓ).

Therefore the multipole frequency RATIO cancels `x_sat` and `(1+ν_vac)` entirely:

$$\boxed{\;\frac{\omega_R(\ell')}{\omega_R(\ell)} = \frac{\ell'}{\ell}\;\big[\text{linear-}\ell\text{ form}\big],\quad\text{spin-independent EXACTLY}\;(x_{sat}\text{ cancels})\;}$$

> **★ Conditionality of "EXACTLY" (review R3 / finding 7).** Two claims are packed here and they have **different** epistemic status. **(i) Spin-independence is EXACTLY true, fork-robust** — `x_sat(a*)` and `(1+ν_vac)` cancel in the ratio for BOTH dispersion forks. **(ii) The point-VALUE `= ℓ'/ℓ` (=1.500 for ℓ=3/2) is EXACT only within the corpus's asserted-not-derived linear-ℓ form** (`ave-merger-ringdown-eigenvalue.md:16`); under the spherical-membrane fork `ω ∝ √(ℓ(ℓ+1))` the ratio is `1.4142`, not `1.5`. That value is binned **UNDETERMINED** (§4, the open linear-ℓ vs √(ℓ(ℓ+1)) fork). The honest headline is therefore **"ratio locked (fork-banded 1.41–1.50), spin-independent EXACTLY"** — the unconditional "= ℓ'/ℓ EXACTLY" must NOT be quoted at any headline site without the linear-ℓ conditionality rider.

Damping locks the same way **at the Schwarzschild anchor**: `Q_ℓ = ℓ` (`qnm-quality-factor.md` `[canon, clm-395gps solidity 0.55 input-only]`, the single-channel Op21 mode-count) ⇒ `Q_{ℓ'}/Q_ℓ = ℓ'/ℓ`.

> **★ Damping-lock spin caveat (review R4 / finding 3 — reconciled with canon).** `Q_ℓ = ℓ` is derived (not asserted) **only at `a*=0`** — it is the `mΩ=0` limit of the corpus's own v2 Kerr-Q section (`ave-merger-ringdown-eigenvalue.md:49,52` `[canon]`: `ω_I = (ω_R − mΩ)/(2ℓ)`, "the quality factor `Q = ω_R/(2ω_I)` **increases with spin**"). Within that model `Q_ℓ = ℓ/(1 − mΩ/ω_R)`, so `Q_{ℓ'}/Q_ℓ` is **`a*`-dependent (through `Ω`, and `m`)** and equals `ℓ'/ℓ` **only at `Ω=0`**. Therefore the all-spin claim "`τ`-ratio set by frozen ratios, not by (M,a)" **over-extends a Schwarzschild-only identity** and is un-reconciled with the corpus's own Kerr-Q formula. Honest frozen statement: **frequency ratios are spin-locked; damping/τ ratios are spin-locked only at `a*=0`, spin-dependent through `Ω` otherwise.** The topological-integer reading `Q=ℓ` (Op21 mode-count) vs the physical observable `Q=ω_R/2ω_I` is a **fork, flagged UNDETERMINED** (flag-don't-fix, alongside the ℓ-dispersion fork §4) — the τ-observable is governed by the physical `Q`, so the topological reading does not rescue the all-spin claim. A `τ`-ratio measurement at moderate spin matching Kerr's drift must NOT be scored against the (Schwarzschild-anchored) organizer.

The frequency-ratio organizer above (`ω_R(ℓ')/ω_R(ℓ)`) is untouched by this caveat — it is genuinely exact and spin-independent (the `x_sat` and `(1+ν_vac)` cancellation holds at all spins for ORG-1); only the damping/τ rider is Schwarzschild-anchored.

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

The cleanest single test: a higher-mode measurement of `ω_330/ω_220`. AVE puts it at ≤1.50 and *fixed*; **Kerr is NOT a single number — its ratio drifts TOWARD the AVE value with spin** (review R3 / finding 6, `qnm` two-method):

| a\* | 0.00 | 0.60 | 0.70 | 0.80 | 0.90 | 0.95 | 0.99 |
|---|---|---|---|---|---|---|---|
| Kerr (3,3,0)/(2,2,0) | 1.6042 | 1.5914 | 1.5841 | 1.5731 | 1.5554 | 1.5409 | 1.5192 |
| **linear-ℓ fork (1.500)** sep | −6.50% | −5.74% | −5.31% | −4.65% | −3.56% | −2.65% | −1.26% |
| **spherical fork (1.4142)** sep | −11.84% | −11.13% | −10.73% | −10.10% | −9.08% | −8.22% | −6.91% |

**Honest, spin-conditioned separability (per fork):**
- **Linear-ℓ fork (1.500):** the gap is only `−6.5%` at `a*=0` and **drops below the ~5% testability threshold for a\*≳0.75**, reaching `−1.3%` at `a*=0.99` (exact degeneracy at extremal — the `l=m` ZDM limit `ω→mΩ_H` gives Kerr `(3/2)/(2/2)=1.500`, identical to the AVE linear fork). At realistic remnant spins (`a*≈0.7`) the linear-fork gap is `−5.3%` — borderline, NOT comfortably `≲5%`-separable.
- **Spherical fork (1.4142):** stays `−8%` to `−12%` across the whole physical range (`−6.9%` even at `a*=0.99`) — robustly separable.

So the frozen "≈6–12% gap / pinned to Kerr 1.60 to ~6% / ≲5% would separate them" criteria (prereg §2 ORG-1 row) are **`a*=0`-anchored and overstate separability**; they need spin-conditioning before any high-spin high-precision confrontation is banked. The load-bearing *robust* ORG-1 content (ratio BELOW Kerr AND spin-frozen) survives because the **frozenness axis sharpens with spin** (Kerr drifts, AVE does not) and the spherical fork keeps a clean gap; only the exact-point-value separability threshold is spin-fragile.

### §1.4 — Scope honesty (what is NOT derived)

- **Overtone ladder (n≥1):** the corpus derives `ω_R ∝ ℓ` and `Q=ℓ` only for the **fundamental** (n=0). It supplies **no** overtone spectrum. So **overtone-ratio locking is FORM-ONLY-NO-NUMBER** — AVE has no derived `ω_221/ω_220`. This is load-bearing for the confrontation (§3): the best-constrained current test (GW150914 220/221) probes exactly the axis AVE cannot predict.
- **ℓ≥3 extension:** the corpus validated `ω_R ∝ ℓ` only at ℓ=2; ℓ≥3 is a forward reading of the corpus's own membrane-mode form (a corollary), tagged as such — not an independently-validated in-corpus number.

---

## §2 — ORG-2: ARRESTED CRITICAL SLOWING (full derivation)

> ### 🔴 RETRACTED 2026-07-20 (PR #772 adversarial review — Rule-11 discard, NO substitution-refill)
>
> **ORG-2 as frozen is FALSE as derived. Its central falsifiable content — the SIGN — inverts against a correct Kerr reference.** The GR Kerr column used throughout §2.3 below (the in-repo `BERTI_220_OMEGA_R` table, `ligo_ringdown_driver.py:122` mirrored into the checks script) is **wrong at non-zero spin**: it reads `−9.4%/−13.9%/−21.0%/−26.8%` LOW at `a*=0.70/0.80/0.90/0.95` (only the `a*=0` anchor is correct). Verified two independent ways this review — a from-scratch Leaver continued-fraction solve **and** the `qnm` package (Stein 2019), mutually agreeing to all digits and corroborated by the Berti-Cardoso-Will 2006 fitting formula — plus the decisive physical anchor that the co-rotating `(2,2,0)` real frequency **rises toward** `m·Ω_H·M = 1.0` at extremal (`qnm` at `a*=0.999` gives `0.9559`), it never plateaus at `~0.55`. **True Kerr `(2,2,0)` `M·ω_R`:** `0.53260 / 0.58602 / 0.67161 / 0.74632` at `a*=0.70/0.80/0.90/0.95` (review-produced; see §2.3-CORRECTED).
>
> Against the true reference, AVE v2 sits **BELOW** Kerr at every spin — `−9.9%` (`a*=0.70`) → `−16.7%` (`0.90`) → `−20.1%` (`0.95`) — the **opposite sign** of the frozen "positive excess / **ABOVE** Kerr for `a*≳0.8`, growing with spin". The prereg's codified ORG-2 falsifier (`prereg §2`: *"a resolved a\*≳0.9 ringdown shows ω_220 AT or BELOW Kerr ⇒ ALREADY-EXCLUDED"*) therefore describes **exactly what AVE actually predicts** against real Kerr — a resolved below-Kerr near-extremal ringdown would have been scored as "falsifying" an organizer AVE never implied. The "arrested-slowing → positive excess / Kerr geometrically softens" observable is an **artifact of the corrupted reference**: true Kerr `ω_R` does NOT geometrically soften (it is `ω_I`, the damping, that softens), so the `54/77` floor sits **below** extremal Kerr, not above it.
>
> **The `x_sat→11/3` skeleton floor and the AVE-side eigenvalue `54/77 = 0.7013` survive independently** (they are corpus-internal, untouched by the Kerr-table error). They are noted as a **POSSIBLE FUTURE below-Kerr organizer** — a hard `ω_R M_g = 0.7013` ceiling that sits below extremal Kerr's `→1.0` — but that requires a **fresh frozen derivation confronted against a corrected Kerr reference AFTER the upstream canon fix lands** (the `ligo_ringdown_driver.py` table correction is the **canon-correction lane's** job, running separately). **Per Rule-12 substitution-not-retraction, the slot is NOT refilled here** — no new below-Kerr organizer is banked in this doc; the original §2.1–§2.3 text is **preserved verbatim below** for the audit trail, and the corrected numbers are appended as §2.3-CORRECTED (evidence only, not a new frozen organizer).  <!-- rule12-freeze: base=b4ccdffc764dfd31f9a50f6c77f23c11708d2f60 region=below offset=0 lines=74 bytes=6759 sha256=f0e3a1eef9231abbc66b6a42b86cb14a678063220f8bb868a9abce672f44194e -->
>
> *Fence: this retraction lives in the derivation doc only; `_prereg-FROZEN.md` is byte-untouched (the frozen falsifier stands on the record as frozen — the docket correction note records that it inverted). The upstream `ligo_ringdown_driver.py` table is NOT edited by this lane (canon-correction lane, routed).*

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

### §2.3-CORRECTED (added 2026-07-20 review — the true Kerr reference; evidence only, NOT a new frozen organizer)

The §2.3 table above uses the corrupted in-repo `BERTI_220_OMEGA_R` Kerr column. Banking the correct reference with full provenance:

> **GR Kerr `(2,2,0)` `M·ω_R` — CORRECTED reference `[review-produced — two-method]`.** From-scratch Leaver continued-fraction solve **and** the `qnm` package (Stein 2019), agreeing to all quoted digits; corroborated by the Berti-Cardoso-Will 2006 fitting formula (`ω_R = 1.5251 − 1.1568(1−a)^{0.1292}`, agrees to `<1%`); the `a*=0` anchor `0.373672` matches the (correct) in-repo row `0.37368`. Exact ZDM constraint respected: `l=m=2` → `M·ω_R → m·Ω_H·M = 1.0` at extremal (`qnm` at `a*=0.999`: `0.9559`).

| a\* | x_sat | AVE ω_R M | Kerr ω_R M `[corrected — review]` | in-repo (WRONG) | AVE − Kerr(corr) |
|---|---|---|---|---|---|
| 0.00 | 7.000 | 0.3673 | 0.373672 | 0.37368 | −1.69% |
| 0.30 | 6.383 | 0.4028 | 0.41953 | 0.41442 | −3.98% |
| 0.60 | 5.648 | 0.4553 | 0.49404 | 0.46378 | −7.85% |
| 0.70 | 5.356 | 0.4801 | 0.53260 | 0.48267 | **−9.85%** |
| 0.80 | 5.019 | 0.5124 | 0.58602 | 0.50465 | **−12.56%** |
| 0.90 | 4.596 | 0.5594 | 0.67161 | 0.53039 | **−16.70%** |
| 0.95 | 4.311 | 0.5966 | 0.74632 | 0.54652 | **−20.07%** |

**AVE v2 sits monotonically BELOW true Kerr, deviation growing with spin** — the sign inverts vs the retracted §2.3. The AVE extremal floor `54/77 = 0.7013` sits **below** extremal Kerr (`→1.0`). This corrected table is the evidence R2 (§3.3) re-grades against; it is NOT re-frozen as an organizer here (Rule-11 discard, no refill — a fresh below-Kerr organizer would need its own frozen derivation after the upstream canon fix).

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
| **GWTC-3 TGR population** (δf_220, δτ_220) | overall scale (a\*) | δf_220 ~few-%-to-~10%; all events a\*<0.85 | ORG-2 (**RETRACTED §2**) / the surviving AVE v2 eigenvalue deviation | **🔴 UNSAFE-PENDING-UPSTREAM-FIX — POTENTIAL LIVE TENSION** (against corrected Kerr, AVE v2 deviates −4% to −13% at the attested catalog spins a\*=0.30–0.80 — AT/ABOVE this sensitivity; determination is contaminated, see below) |

> **★ 🔴 CORRECTED two-method note (2026-07-20 review — supersedes the below):** the GR Kerr reference used in the §2.3/§3.2 tables was **NOT two-method** where it was load-bearing. The shipped "cross-checked to 2×10⁻⁵" receipt validated **only the `a*=0` anchor** — the one row where the in-repo Berti table is correct; the load-bearing **spinning** rows were single-method on a table that is `−9.4%` to `−26.8%` wrong. The corrected two-method Kerr reference (from-scratch Leaver + `qnm` package + BCW corroboration) is banked in §2.3-CORRECTED. The current-CONSTRAINT *levels* below (Isi+2019 ~10%/~20%; GWTC-3 few-%-to-~10%) remain `[import — abstract-level]` with the full-PDF-CI-width completeness limit unchanged.

**Two-method note on the imports `[SUPERSEDED — see corrected note above]`:** the GR Kerr reference values are two-method (in-repo Berti table + independent Leaver values, cross-checked to 2×10⁻⁵ at the anchor). The current-CONSTRAINT levels (Isi+2019 ~10%/~20%; GWTC-3 few-%-to-tens-of-%) are `[import — abstract-level]`: the primary-source *abstracts* were fetched this session (Isi+2019 confirms the ~10% postinspiral / ~20% first-overtone levels); the exact per-event 90% CI widths require the full-PDF tables, **not retrieved this session** — flagged as a citation-completeness limit (verify-before-cite honesty), and the confrontation only load-bears on the *level* (tens-of-%), which is robust across sources.

### §3.3 — Where the organizers sit vs current data `[🔴 RE-GRADED 2026-07-20 review — R2]`

> **The original verdict of this section — "Neither organizer is ALREADY-EXCLUDED / No bankable negative fired / CONSISTENT-UNTESTED" — is WITHDRAWN.** It was computed against the corrupted in-repo Kerr table (§2 retraction), which made the AVE−Kerr offset look `≤2%` for `a*≤0.85`. Against the corrected two-method Kerr reference (§2.3-CORRECTED) the AVE v2 eigenvalue deviation at the spins the catalog **actually contains** (all events `a*<0.85`) is spin-dependent and NOT rank-1-small:

| a\* (attested catalog range) | 0.30 | 0.50 | 0.60 | 0.70 | 0.80 |
|---|---|---|---|---|---|
| AVE v2 − corrected Kerr | −4.0% | −6.3% | −7.9% | −9.9% | −12.6% |

These deviations are **AT or ABOVE the PR's own imported δf_220 sensitivity** (§3.2: GWTC-3 TGR δf_220 ~few-% to ~10%). So the axis this section exists to protect — a Rule-11 bankable NEGATIVE — **cannot be honestly binned CONSISTENT-UNTESTED**. Honest re-grade:

- **ORG-1** (multipole ratio): still CONSISTENT-UNTESTED on the *robust* content — current higher-mode `ω_330/ω_220` precision (~tens-of-%) cannot resolve the (spin-conditioned) AVE−Kerr gap; the ratio side does not load-bear on the corrupted `(2,2,0)` spin table. See §1.3 for the spin-conditioned separation.
- **The AVE v2 eigenvalue vs Kerr (the axis ORG-2 fed off)**: **🔴 POTENTIAL LIVE TENSION — UNSAFE-PENDING-UPSTREAM-FIX.** The determination is contaminated by **two** open items, **both routed to the canon-correction lane (running separately)**: (i) the corrupted in-repo `BERTI_220_OMEGA_R` canon table (`ligo_ringdown_driver.py:122`); and (ii) a **detector-vs-source-frame mass question** in the banked `−0.45%` v2 cold-ringdown match (the leaf tables source-frame `M_final`, but LVC's 251 Hz `f_220` is detector-frame — the banked `<1%` match may be two compensating ~9–10% errors, frame-factor × table-error). **This lane does NOT fire a negative and does NOT presume its outcome** — asserting ALREADY-EXCLUDED would require the actual per-event δf_220 posteriors (imported here at abstract level only) evaluated against the fixed canon. The confrontation is **UNSAFE to bank in either direction** until the upstream fix lands.
- Next-gen ringdown precision (LISA / Einstein Telescope / Cosmic Explorer, ~1% QNM-deviation sensitivity `[import — forecast-level]`) would sharpen either determination.

**Consensus-knife:** this is an objective numerical error against the repo's own cited source — any framework compared to a `~20%`-wrong reference yields a wrong verdict; the GR side would be equally faulted. No AVE-lenient standard is applied, and no negative is banked against AVE on contaminated inputs.

---

## §4 — FROZEN-BIN OUTCOME `[🔴 RE-GRADED 2026-07-20 review]`

Per the four bins frozen in the prereg §2, with the review re-grades applied (the frozen prereg is byte-untouched; these outcomes supersede the pre-review bins). Every organizer inherits the `clm-395gps` input-only grade (§0 CLAIM-GRADE, solidity ≤0.55):

| Organizer | BIN `[re-graded]` | Basis |
|---|---|---|
| **ORG-1 multipole-ratio locking** (robust: ratio<Kerr AND spin-frozen) | **ORGANIZER-DERIVED-AND-TESTABLE — with REDUCED separation** | derived from `ω_R∝ℓ` + frozen elastic ratios; but Kerr DRIFTS toward AVE with spin (§1.3): the linear-fork gap drops below ~5% for `a*≳0.75` (degenerate at extremal), the spherical fork stays −8% to −12% robust. Falsifiable via higher-mode `ω_330/ω_220`, **spin-conditioned**; the robust below-Kerr+spin-frozen content survives (frozenness axis sharpens with spin). CONSISTENT-UNTESTED now. |
| **ORG-1 exact point-value** (1.500 vs 1.414) | **UNDETERMINED** | the linear-ℓ vs √(ℓ(ℓ+1)) surface-dispersion fork (§4 prereg) is open; "= ℓ'/ℓ EXACTLY" is exact only within the linear-ℓ form — spin-independence is the fork-robust EXACT half (§1.1 conditionality) |
| **ORG-1 overtone-ratio** (ω_221/ω_220) | **FORM-ONLY-NO-NUMBER** | corpus supplies no n≥1 spectrum; structurally real but numberless |
| **ORG-1 damping/τ-ratio lock** | **DERIVED-AND-TESTABLE at `a*=0` ONLY; spin-behavior UNDETERMINED** | `Q=ℓ` is the Schwarzschild anchor; the all-spin τ-lock over-extends it (leaf: `Q` increases with spin). Topological-Q vs physical-Q fork flagged (§1.1 R4 caveat) |
| **ORG-2 arrested critical slowing** (form + sign: ω_R floored ABOVE Kerr near extremal) | **🔴 RETRACTED-WRONG-REFERENCE** (Rule-11 discard, no refill) | the frozen SIGN inverts against corrected Kerr (§2 retraction): AVE sits −10% to −20% BELOW, the codified falsifier describes what AVE predicts. The `54/77` skeleton floor survives corpus-internally as a POSSIBLE FUTURE **below-Kerr** organizer needing a fresh frozen derivation AFTER the upstream canon fix — NOT refilled here |
| **ORG-2 excess MAGNITUDE** (+5.5%/+9.2%) | **🔴 VOID (retracted with ORG-2)** | rode the corrupted Kerr column; the true AVE−Kerr magnitudes are −16.7%/−20.1% (below, not above) |
| **RANK-1 unification** (single-parameter deviation) | **ORGANIZER-DERIVED-AND-TESTABLE** (form-level, input-only grade) | falsifiable via multi-mode deviation-correlation; the substrate's most restrictive forward statement — unaffected by the Kerr-table error (it is a within-AVE structural claim) |
| the AVE-eigenvalue-vs-Kerr data confrontation | **🔴 UNSAFE-PENDING-UPSTREAM-FIX** (POTENTIAL LIVE TENSION) | against corrected Kerr the deviation is −4% to −13% at attested catalog spins, AT/ABOVE δf_220 sensitivity; contaminated by the corrupted canon table + a frame question, both routed to the canon-correction lane; no negative fired, outcome not presumed (§3.3) |
| `ω ∝ √C_44` scaling law | **FORM-ONLY-NO-NUMBER** (mechanism of retracted ORG-2) | C_44 not independently observable; testable only through the spin dependence it controls |
| mass scaling `ω∝1/M` | **not-a-discriminator** | identical AVE/Kerr |

**Headline (honest, post-review):** ORG-1 survives as a properly-graded (input-only) forward organizer, **DERIVED-AND-TESTABLE with reduced, spin-conditioned separation**; its exact point-value stays UNDETERMINED and its damping/τ spin-lock is Schwarzschild-anchored-only. **ORG-2 is RETRACTED** — its frozen "positive excess / above Kerr" sign inverted against a correct Kerr reference (the in-repo canon table is `−9%` to `−27%` wrong at spin); Rule-11 discard, slot NOT refilled (the `54/77` floor is noted as a possible FUTURE below-Kerr organizer pending the upstream fix). The data confrontation is **UNSAFE-PENDING-UPSTREAM-FIX** (potential live tension, not the pre-review "no bankable negative fired / CONSISTENT-UNTESTED"). RANK-1 structure survives. No consistency-class result is upgraded; the banked v2 ω_R/τ match itself now carries an open frame-audit flag (routed). The distinctive substrate content remains the **rank-1 / locked-ratio** structure — but it inherits the `clm-395gps` input-only grade and must not be headlined above that.

---

## §5 — flag-don't-fix (surfaced, NOT resolved)

1. **The linear-ℓ vs √(ℓ(ℓ+1)) surface-mode dispersion fork (Grant/auditor).** The corpus writes the membrane mode as `ω_R = ℓ·c/r_eff` (LINEAR-ℓ, `ave-merger-ringdown-eigenvalue.md:16`), which gives ORG-1 ratio 1.500. The physical default for a mode on a 2-sphere is `ω ∝ √(ℓ(ℓ+1))` → 1.414. Both are below Kerr (so ORG-1's robust content is safe), but the **exact** number needs a substrate derivation of the surface-mode dispersion the corpus never did. Surfaced, not resolved.

2. **The banked τ-outperformance deserves an error-bar scrutiny (Grant/auditor).** The corpus banks that v2 τ (mean −0.47%) *outperforms* GR Kerr QNM (mean −6.94%) at reproducing the 3 LIGO τ values (`ave-merger-ringdown-eigenvalue.md:64`). This is a genuinely AVE-distinct-looking claim — BUT the LIGO τ values it beats GR on (4.0/3.0/1.4 ms) are quoted to ~1 sig fig; if their measurement uncertainty is ≳10–20%, GR's −7% "miss" and AVE's −0.5% are BOTH consistent with the data and the "outperformance" is within noise. This does not touch the organizers (which live in the a\*≥0.9 and higher-mode regimes), but the τ-outperformance should not be headlined as AVE-distinct without the LIGO τ error bars. Consensus-knife: SM/GR would get the same scrutiny — a −7% offset on a ~15%-error measurement is a match, not a miss.

3. **~~ORG-2 magnitude is a v2-extrapolation into the Option-B regime~~ `[🔴 SUPERSEDED by the §2 retraction]`.** The pre-review flag hedged only the MAGNITUDE while freezing the SIGN/FLOOR as robust — but the SIGN itself inverts against corrected Kerr. ORG-2 is retracted, not merely magnitude-revisable.

4. **`[NEW — R1/R2 review]` The upstream in-repo Kerr `(2,2,0)` canon table is wrong at spin (Grant/auditor → canon-correction lane).** `src/scripts/vol_3_macroscopic/ligo_ringdown_driver.py:122` `BERTI_220_OMEGA_R` is `−9.4%` to `−26.8%` LOW at `a*=0.70–0.95` (only `a*=0` correct), against its own cited source (Berti-Cardoso-Will 2006 / Leaver). Verified two-method (from-scratch Leaver + `qnm`; BCW fit + ZDM limit corroborate). **This lane does NOT edit the canon table** (fence) — routed to the **canon-correction lane** (running separately), which owns the upstream fix and the re-validation of everything downstream of that table (including the banked v2 spin-validation and the `divergence-test-substrate-map` C1-BH-RING row).

5. **`[NEW — R2 review]` The banked `−0.45%` v2 cold-ringdown match may carry a detector-vs-source-frame mass error (Grant/auditor → canon-correction lane).** The leaf tables source-frame `M_final` (e.g. GW150914 `62.0 M⊙`) against `f_obs=251 Hz`, but LVC's 251 Hz `f_220` is **detector-frame** (`M≈67.6 M⊙`, `z≈0.09`). The banked `<1%` match may be two compensating `~9–10%` errors (frame-factor × the corrupted table error) — needs a frame audit before the "three-source consistent" claim (§7) is relied on. Routed to the canon-correction lane; NOT resolved or presumed here.

---

## §6 — consistency-vs-emergence classification + auditor-queue (implementer SURFACES; auditor LANDS)

**Classification.** The surviving organizer (ORG-1) is a **forward DEVIATION prediction** (chord-surface), NOT an emergence claim: `ν_vac=2/7` and the ringdown eigenvalue are corpus INPUTS, not re-derived here — and `ν_vac`'s VALUE is itself GR-imported via K=2G (§0 CLAIM-GRADE); no VALUE is claimed emergent. The banked v2 ω_R/τ match is CONSISTENCY (recovering GR) and is NOT upgraded — and it now carries an open frame-audit flag (§5 item 5, routed). The distinctive content (rank-1 locked-ratio deviation structure) is a **forward falsifiable prediction** at the `clm-395gps` input-only grade (solidity ≤0.55). ORG-2 is RETRACTED (§2) — nothing about it propagates.

**Auditor-queue (surfaced, NOT landed — no KB/matrix edit in this lane; re-graded post-review):**
| Site | Proposed disposition (auditor-gated) |
|---|---|
| **`ligo_ringdown_driver.py:122` `BERTI_220_OMEGA_R` — the corrupted canon table** | **★PRIMARY — routed to the canon-correction lane (separate).** Correct the `(2,2,0)` spin rows to the two-method Leaver/`qnm` values (§2.3-CORRECTED); re-validate everything downstream (banked v2 spin-validation, `divergence-test-substrate-map` C1-BH-RING, `lattice-extreme-bh-rationality` §4). This is upstream of, and gates, the items below. |
| `lattice-extreme-bh-rationality.md` §4 (ringdown CONSISTENCY row) | **candidate cross-link (post-fix):** point to ORG-1 as the surviving soft-mode DEVIATION companion; the CONSISTENCY match itself is pending the frame audit (§5 item 5) |
| `divergence-test-substrate-map.md` C1-BH-RING row | **~~candidate strengthen with ORG-2~~ RE-GRADED:** ORG-2 is retracted — do NOT add it as a derived deviation organizer for the `a*>0.90` regime. ORG-1 (higher-mode, spin-conditioned) remains an orthogonal organizer; the row's own numbers ride the corrupted table (canon-correction lane) |
| `ave-merger-ringdown-eigenvalue.md` | **candidate forward-content note (input-only grade):** the multipole-ratio + rank-1 structure as beyond-Kerr organizers (deviation-scoped, Kerr-wording fence, solidity ≤0.55) — ORG-1 only |
| the τ-outperformance headline (`ave-merger-ringdown-eigenvalue.md:64`) | **candidate scrutiny flag:** error-bar the LIGO τ values AND resolve the detector-vs-source-frame mass question (§5 items 2+5) before relying on "outperforms GR" / "three-source consistent" |

No leaf touched; no `clm-` minted; canonical-propagation is a gated follow-on. **The canon-table fix is NOT this lane's to land — it is routed to the canon-correction lane.**

---

## §7 — Cross-references (verified at branch HEAD)

- Prereg (FROZEN): `research/2026-07-20_ringdown-systematics_prereg-FROZEN.md` (commit `f22d0b2d`)
- Checks: `research/2026-07-20_ringdown-systematics_checks.py` (`math`-only; `ave` untouched)
- Registered candidate: `research/2026-07-20_vacuum-metallurgy_kz-relic-and-instruments.md` D4a
- Banked ringdown match (CONSISTENCY): `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md` (v2 resultbox, lines 62/64); `research/ligo-ringdown-driver-design.md` §8–§10; `manuscript/ave-kb/common/divergence-test-substrate-map.md` C1-BH-RING row — ~~three-source consistent, no walk-back~~ `[🔴 the "three-source consistency" is NOT independent: all three ride the same corrupted `(2,2,0)` Kerr table AND the same frame convention (§5 items 4+5). Frame audit + canon-table fix routed to the canon-correction lane before this consistency is relied on.]`
- Soft-mode C_44 collapse: `research/2026-07-04_saturated-elastic-tensor_result.md` §4 (PR#521); `electron-bh-isomorphism.md:38`
- Q=ℓ (single-channel Op21): `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/qnm-quality-factor.md`; `op21-multi-mode-mode-counting.md` §1 (BH-ringdown = single-channel row)
- GR Kerr (2,2,0) reference table (in-repo): `src/scripts/vol_3_macroscopic/ligo_ringdown_driver.py:122` `[🔴 WRONG AT SPIN — −9% to −27% at a*=0.70–0.95; corrected two-method values in §2.3-CORRECTED; upstream fix routed to the canon-correction lane]`
- Classification (CONSISTENCY, not emergence): `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md` §4

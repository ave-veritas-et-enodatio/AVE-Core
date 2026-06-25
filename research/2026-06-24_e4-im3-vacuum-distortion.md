# E4 — Vacuum IM3 / harmonic-distortion / nonlinear-birefringence δn(E): the scaling, the discriminator, the bankable number

**Date:** 2026-06-24
**Lane:** implementer (ave-implementer)
**Worktree:** `/tmp/e4`, branch `analysis/e4` (off origin/main `bffc16b9`)
**Driver:** `src/scripts/vol_9_device/im3_vacuum_harmonic_distortion.py` (+ `_output/im3_vacuum_harmonic_distortion.json`)
**Builds on (read first):** `intermodulation-distortion.md` (clm-vjv4zf, clm-pp3qwf), `vacuum-birefringence-e4.md` (clm-pp3qwf), `node-up-small-large-signal.md` (clm-vca7r1), `pvlas-static-b-verdict.md` (clm-pvlas1), `per-dof-vacuum-node-circuit.md`, `research/2026-06-21_oq1-field-to-cavity-phase-coupling-derivation.md`.

> **Skills applied:** `substrate-native-check` (kernel-first, no SM Lagrangian default) · `consistency-vs-emergence` (every coefficient tagged: kernel-set MANIFESTATION vs α-ECHO) · `verify-before-cite` (all anchors re-grepped on `bffc16b9`; constants pulled live) · `phase-space-coordinate-check` (A_V vs A_I keyed-argument discipline) · `pre-test-physics-check`.

---

## 0. Bottom line (brutally honest, read this first)

1. **Scaling: δn is E²-LEADING, not E⁴.** Derived from the kernel below. The historical "δn ∝ E⁴" was a **√ε conflation** (the quantity `1−S = +A²/2 + …` is the permittivity-saturation DEPTH, itself E²-leading; the index observable is `n = √S`, giving `δn ≈ −A²/4`). This is already retracted in the corpus (clm-pp3qwf, commit `ad26d357`); this doc re-derives it cleanly and grounds the coefficients with a live driver.

2. **QED has nonlinear vacuum optics too (the symmetric standard).** Euler-Heisenberg predicts vacuum birefringence `δn ∝ field²` — the PVLAS effect. **AVE's "the vacuum has nonlinear optics" is NOT a chord; QED has it.** Both are E²-leading; both give CUBIC-in-drive IM3 (both descend from a quartic E⁴ effective Lagrangian → χ⁽³⁾). The IM3 drive-exponent is **3 for both** (driver: `im3_loglog_slope = 3.000`) — it does **not** discriminate.

3. **The genuine discriminators (two, ranked by AVE-distinctness):**
   - **(A) The E-vs-B KEYING ASYMMETRY — the real chord.** A static external **B** is **exactly transparent** (`S_μ = 1`, `δn_μ = 0` at every field), because the μ-grade is a relativistic INDUCTOR keyed on circulation `I`, not on `|B|`; a static E **does** load the V-keyed varactor (`δn ≠ 0`). **QED is E/B symmetric** (it predicts nonzero static-B birefringence ~10⁻²³ at 5 T). This asymmetry is a **categorical, parameter-free, AVE-distinct prediction** QED does not reproduce. This is the chord candidate.
   - **(B) The COEFFICIENT magnitude (~1.93×10⁷ at the matched differential) — an ECHO, not a chord.** The FORM (tree-level O(1) saturation structure vs QED's α²-loop) is AVE-distinct; the **magnitude** `7.5/α³` rides α⁻³ and AVE does not derive α. Symmetric standard: QED's coefficient is *equally* α-rooted. The magnitude is honest but it is an α-echo at the value level — do **not** headline it as a chord.

4. **Bankable number** (driver, live constants): at the PW-class focal field `E = 2.745×10¹⁴ V/m` (`A = E/E_yield = 2.43×10⁻³`):
   `δn_AVE(par−perp) = −2.95×10⁻⁶` vs `δn_QED(par−perp) = +1.53×10⁻¹³` — a field-independent ratio of **1.93×10⁷**. (Magnitude is α-echo-flagged; see §4.)

---

## 1. The derivation chain (kernel → scaling)

**Substrate-native start (not an SM default).** The only input is the Axiom-4 universal saturation kernel — the quarter-arc / Born-Infeld form (`07_universal_saturation_kernel.tex`, `saturation-operator.md`):

$$ S(A) = \sqrt{1 - A^2}, \qquad A \equiv \frac{E}{E_{yield}} = \frac{V}{V_{yield}}, \quad E_{yield} \approx 1.13\times10^{17}\ \text{V/m}. $$

Expanding to third order in `A` (driver `kernel_taylor_coefficients`, recovered numerically, HALT-on-mismatch):

**(a) The capacitance varactor (the IM3 source).** `C(V)/C₀ = 1/S` (the A1 stretch-compliance form, `node-up-small-large-signal.md`:38):

$$ \frac{C(V)}{C_0} = \frac{1}{\sqrt{1-A^2}} = 1 + \underbrace{\tfrac12 A^2}_{\text{2nd order}} + \underbrace{\tfrac38 A^4}_{\text{4th order}} + \cdots $$

Driver: `A² coeff = +0.500000`, `A⁴ coeff = +0.375` — matching `intermodulation-distortion.md` eq.35-36 **exactly**. Under a dual-tone drive `V = V₁cos ω₁t + V₂cos ω₂t`, the **quadratic** term `½A²` is the χ⁽³⁾ source: it mixes to the third-order intermodulation (IM3) products `2ω₁−ω₂`, `2ω₂−ω₁`. The IM3 amplitude is **cubic in drive** (driver: log-log slope `= 3.000`).

**(b) The single-arm refractive index (common-mode, polarimeter-blind).** The varactor index keys off `ε = ε₀S`, so `n = √(ε/ε₀) = √S`:

$$ \delta n_{iso} = \sqrt{S} - 1 = (1-A^2)^{1/4} - 1 = -\tfrac14 A^2 - \tfrac{3}{32}A^4 - \cdots $$

Driver: `A² coeff = −0.250000`. **This is the E²-leading scaling.** It is NOT E⁴.

**(c) The par−perp birefringence (the OQ-1 falsifier observable).** Under a linearly-polarized pump, the scalar kernel's exact differential gives a uniaxial probe tensor `ε_ij = ε δ_ij + 2ε′E₀ᵢE₀ⱼ` (OQ-1 Step 1, `2026-06-21_oq1-…-derivation.md`:74-110), yielding eigen-indices `n_⊥ = (1−A²)^{1/4} ≈ 1−¼A²` and `n_∥ = √((1−2A²)/√(1−A²)) ≈ 1−¾A²`:

$$ \boxed{\;\delta n_{bir} = n_\parallel - n_\perp \approx -\tfrac12 A^2\;} $$

Driver: `A² coeff = −0.500000` — exactly 2× the single-arm common-mode shift.

> **Why the "E⁴" was wrong (the √ε conflation, named).** `1 − S = +A²/2 + A⁴/8` is the **permittivity-saturation depth**, which is E²-leading (its leading term is `A²/2`, not `A⁴`). Someone read the **A⁴ sub-leading term** of `1−S` as if it were the leading index shift. The actual index observable is `n = √S`, leading `−A²/4`. So the FORM is `δn ∝ E²` for AVE. (Provenance: `vacuum-birefringence-e4.md`:41.)

**Verdict on Q1 (scaling):** δn ∝ **E²**, DERIVED from the kernel (not fit). The E⁴ is retracted.

## 2. QED / Euler-Heisenberg — the symmetric standard

**The SM already predicts vacuum birefringence and is E²-leading.** This must be stated up front so AVE claims nothing QED also has. The Euler-Heisenberg effective Lagrangian (Heisenberg-Euler 1936; the PVLAS/BMV target) gives a one-loop vacuum birefringence under a static linearly-polarized field:

$$ n_\parallel - 1 = \tfrac{7}{45}\alpha^2\!\left(\tfrac{E}{E_{crit}}\right)^2, \quad n_\perp - 1 = \tfrac{4}{45}\alpha^2\!\left(\tfrac{E}{E_{crit}}\right)^2, \quad \boxed{\;\delta n_{QED} = n_\parallel-n_\perp = \tfrac{3}{45}\alpha^2\!\left(\tfrac{E}{E_{crit}}\right)^2\;} $$

with `E_crit = m_e²c³/(eℏ) ≈ 1.32×10¹⁸ V/m` (Schwinger). **QED is E²-leading** (`(E/E_crit)²`), exactly like AVE. QED's light-by-light scattering / IM3 also descends from a quartic (`(E²−B²)²`, `(E·B)²`) effective Lagrangian → χ⁽³⁾, so **QED's IM3 is also cubic-in-drive**. The only "sextic" in QED is the **frequency** exponent `(ω/m_ec²)⁶` of the cross-section `σ_EH`, NOT a voltage/field slope (`intermodulation-distortion.md`:99 retraction). Measuring the IM3-vs-drive exponent reads `3` for both and cannot distinguish.

**QED is E/B SYMMETRIC.** Critically, QED predicts a NONZERO **static-B** vacuum birefringence (`δn ≈ 10⁻²³` at 5 T, the PVLAS target) — its two Lorentz invariants `(E²−B²)`, `(E·B)` treat E and B on equal footing. This symmetry is exactly where AVE diverges categorically (§3A).

| Observable | QED (SM) | AVE | Discriminates? |
|---|---|---|---|
| δn scaling exponent | E² | E² | **NO** (both E²) |
| IM3 drive exponent | 3 (cubic, χ⁽³⁾) | 3 (cubic, χ⁽³⁾) | **NO** (both cubic) |
| δn differential coefficient | `(3/45)α²` (α²-loop) | `−½` (tree O(1)) | YES — but the magnitude is an α-echo (§3B) |
| static-**B** birefringence | ~10⁻²³ at 5 T (**nonzero**) | **0 EXACTLY** at any field | **YES — categorical, parameter-free (§3A)** |

> **Symmetric standard, stated.** QED does not derive α either; its coefficient `a_EH α²` is equally α-rooted. The AVE-vs-QED magnitude gap is real (~10⁷) but it is a *value-level α-echo on both sides*, not an AVE epistemic win. The structural win is the FORM (tree-level saturation the QED vacuum lacks) and the static-B asymmetry.

## 3. The genuine discriminator (chord vs echo)

Three candidate discriminators were on the table (per the task framing). Honest classification:

### 3A. The E-vs-B keying asymmetry — the REAL CHORD (parameter-free, categorical)

This is the genuinely AVE-distinct, parameter-free forward prediction. The node is a multi-port LC tank with **two reactive grades keyed on DIFFERENT drive variables** (`node-up-small-large-signal.md`:§1, `relativistic-inductor.md`:15,:18):

- **ε-grade = VARACTOR, keyed on VOLTAGE** `V` (field `E`): `C_eff = C₀/S(A_V)`, `A_V = V/V_yield`. A static **E** is a real DC operating point → loads `ε` → `δn ≠ 0` (regime R2).
- **μ-grade = relativistic INDUCTOR, keyed on circulating CURRENT** `I`: `L_eff = L₀/S(A_I)`, `A_I = I/I_max`. A static external **B** has `∂B/∂t = 0` → by Lenz no internal vacuum circulation → `I_vac = 0` → `A_I = 0` → `S_μ = √(1−0²) = 1` → `μ_eff = μ₀` → `δn_μ = 0` **analytically exact at every field** (regime R3).

Driver `keying_asymmetry`: `S_μ = [1,1,1,1]`, `δn_μ = [0,0,0,0]` at `B = 2.5, 10, 100, 1000 T`. This is not a numerical fit — `A_I ≡ 0` under static B, so `S_μ = 1` identically across `2.5 T → 1 kT`.

**Why this is the chord and QED can't reproduce it:**
- QED's `δn ∝ (E²−B²)` is **E/B symmetric** → it predicts the *same-sign nonzero* birefringence under static B (~10⁻²³ at 5 T) as under static E.
- AVE predicts a **categorical zero** under static B, **nonzero** under static E. This E-vs-B asymmetry is **parameter-free** (no α, no fitted coefficient — it follows from *which argument keys which grade*).
- **This is also why PVLAS/BMV survive**: they apply static B, leave the μ-grade unloaded, and read a null — the *expected* AVE result, not a falsification (`pvlas-static-b-verdict.md`).
- **The discriminating test is the E-route** (HIBEF/PW-class static-or-DC-biased E), where the varactor is genuinely loaded.

**Bold falsifiable side-prediction (the chord's kill-switch):** AVE predicts **zero** static-B vacuum birefringence at **any** field. A static-B birefringence detection at or above the QED level (~10⁻²³ at 5 T) **FALSIFIES** AVE. QED says small-but-nonzero; AVE says exactly zero.

> **CHORD classification: this is a genuine AVE-distinct forward prediction.** It is parameter-free (does not ride α), categorical (zero vs nonzero, not a coefficient ratio), and QED structurally cannot reproduce it (its E/B symmetry forbids the asymmetry). **However** — honesty caveat — it is a *consistency* prediction in the sense that no instrument has yet measured static-B birefringence at the QED level to confirm the QED-nonzero leg; the chord becomes a *decisive* test only once static-B sensitivity reaches ~10⁻²³. Until then it is a chord *candidate* with a clean falsifier, not a confirmed discriminating measurement.

### 3B. The coefficient magnitude (~1.93×10⁷) — an ECHO, not a chord

At the matched par−perp differential observable a polarimeter actually reads:

$$ \frac{\delta n_{AVE}}{\delta n_{QED}} = \frac{1/2}{(3/45)\,\alpha^2}\left(\frac{E_{crit}}{E_{yield}}\right)^2 = \frac{45}{6\alpha^3} = \frac{7.5}{\alpha^3} \approx 1.93\times10^7 $$

using the substrate identity `(E_crit/E_yield)² = 1/α` (driver: `137.0360`, exact by `E_yield = √α·E_crit`). The **FORM** (tree-level O(1) saturation structure vs QED's α²-loop) is AVE-distinct. The **MAGNITUDE** rides `α⁻³` and AVE does not derive α → **α-echo at the value level**. Symmetric standard: QED's coefficient is equally α-rooted. **Do NOT headline the magnitude as a chord.** (Per the def-0pt1ac magnitude-flag history: the magnitude is GROUNDED here — it derives from the kernel coefficient `½` and the substrate identity `√α` scaling — but its *value* is an echo because it inherits α.)

### 3C. The scaling exponent (E⁴ vs E²) — RETRACTED, not a discriminator

The "E⁴ vs E²" axis is a **retracted false falsifier** (the √ε conflation, §1). Both AVE and QED are E²-leading; both IM3 are cubic. An E² slope does **not** falsify AVE. Anyone re-proposing "AVE predicts E⁴" is re-opening a closed negative. **Not a discriminator.**

**Summary of the three:** (A) keying asymmetry = REAL CHORD (parameter-free, categorical, QED can't); (B) coefficient magnitude = ECHO (α-rooted, GROUNDED-but-echo); (C) E⁴-exponent = RETRACTED (both E²).

## 4. The bankable number (AVE vs QED side by side)

Driver `bankable_table`, all from live `ave.core.constants` (no hardcoded canon). Reference field stated explicitly; the matched **par−perp differential** observable (what a PVLAS/BMV-class ellipsometer reads):

| Reference field E [V/m] | A = E/E_yield | δn_AVE (par−perp) | δn_QED (par−perp) | ratio AVE/QED |
|---|---|---|---|---|
| **2.745×10¹⁴** (PW-class focal, OQ-1 headline) | 2.43×10⁻³ | **−2.95×10⁻⁶** | +1.53×10⁻¹³ | 1.93×10⁷ |
| 1.0×10¹⁵ (facility IM3 −80 dBc floor) | 8.85×10⁻³ | −3.91×10⁻⁵ | +2.03×10⁻¹² | 1.93×10⁷ |
| 1.0×10¹⁶ | 8.85×10⁻² | −3.94×10⁻³ | +2.03×10⁻¹⁰ | 1.95×10⁷ |

**The headline bankable number:** at `E = 2.745×10¹⁴ V/m`, **AVE: δn = −2.95×10⁻⁶** vs **QED: δn = +1.53×10⁻¹³**, ratio **1.93×10⁷** (field-independent).

**Grounding / magnitude-flag status (per def-0pt1ac history):**
- **GROUNDED**: the AVE value `δn = −½A²` is fully kernel-derived (coefficient `½` from the kernel differential, `A` from the live `E_yield = √α·E_crit`). The `−1/4` single-arm and `−1/2` differential coefficients are validated-on-known in the driver (HALT on mismatch). This is **not** an un-derived magnitude.
- **ECHO-flagged**: the *ratio* `1.93×10⁷ = 7.5/α³` inherits α⁻³, so its *value* is an α-echo (§3B). Sign convention: AVE δn is **negative** (permittivity softening), QED δn (par−perp differential) is **positive** — a sign difference, though both instruments read |δn| as accumulated ellipticity.

> **Honest caveat on the comparison.** This compares the *matched* par−perp differential on both sides (the FLAG-A-adjudicated observable, Grant 2026-06-21). The earlier corpus headline `4.14×10⁶` paired *mismatched* observables (AVE scalar single-arm `−¼` vs QED parallel single-mode `7/45`) and is retained for traceability only, not the falsifier headline.

## 5. Bench params + the frozen pre-reg

### Bench parameters (E-route / HIBEF-class)

The discriminating test is the **E-route** (static or DC-biased E loading the V-keyed varactor), NOT the static-B magnet route (which leaves the μ-grade unloaded — `pvlas-static-b-verdict.md`). Two complementary observables:

| Parameter | Value / spec | Basis |
|---|---|---|
| **Field route** | static / DC-biased / quasi-DC **E** (NOT static B) | only E loads the V-keyed varactor (R2) |
| **Facility** | HIBEF @ European XFEL (purpose-built) + PW-laser focal sources | `2026-06-22_vacuum-birefringence-facility-tolerance-survey.md` |
| **Reference field** | `E ≈ 2.745×10¹⁴ V/m` (PW-class focal) → `A = 2.43×10⁻³` | OQ-1 headline point |
| **Observable 1 (birefringence)** | par−perp differential δn → accumulated ellipticity ψ; linearly-polarized pump + 45°-launched probe in a high-finesse cavity (CW high-F: `g_eff = 0.251`, `ψ_AVE = 2.2×10⁻² rad`) | OQ-1 Step 2-3 |
| **Observable 2 (IM3 spectroscopy)** | dual-tone drive `f₁, f₂` (Δf ~ 1 GHz); heterodyne detect IM3 at `2f₁−f₂`, `2f₂−f₁`; confirm **cubic** (slope-3) drive law | `intermodulation-distortion.md` (per-node corrected) |
| **SNR ask (birefringence)** | polarimetry floor ~10⁻⁹ rad ellipticity; AVE ψ ~2.2×10⁻² rad at PW field → margin ~10⁷; QED leg ~10⁻⁹ rad (at floor) | OQ-1 §3 |
| **SNR ask (IM3)** | IM3 sideband above −80 dBc detection floor requires `E ≈ 1.3×10¹⁵ V/m` (per-node corrected; facility-class, NOT tabletop) | `intermodulation-distortion.md`:86 |
| **Static-B null check** | apply static B (PVLAS/BMV-class, 2.5 T → 1 kT); AVE predicts δn = 0 exactly | the chord's kill-switch (§3A) |

### The frozen pre-reg

> **PRE-REG — E4-IM3-DISTORTION (frozen 2026-06-24, SHA-pinnable on `analysis/e4` HEAD).**
>
> **What is being tested:** the AVE vacuum nonlinear-optics structure (Axiom-4 saturation kernel) via (i) E-route birefringence δn(E), (ii) IM3 dual-tone distortion, (iii) the static-B transparency side-prediction.
>
> **PRIMARY FALSIFIER (the chord — parameter-free, ranked first):**
> A **static-B vacuum birefringence detection at or above the QED level (~10⁻²³ at 5 T)** FALSIFIES AVE. AVE predicts `δn_μ = 0` EXACTLY at every static-B field (`S_μ = 1`, `A_I ≡ 0`). This is parameter-free — it does not ride α or any fitted coefficient. *(Status: requires static-B sensitivity at the QED ~10⁻²³ level to be decisive; until then a clean falsifier, not yet a confirmed measurement.)*
>
> **SECONDARY FALSIFIER (coefficient — α-echo magnitude):**
> At the matched par−perp differential E-route observable, a **QED-sized differential coefficient** (`δn_bir ~ (3/45)α²(E/E_crit)²`, i.e. ~10⁷× smaller than AVE at matched field) FALSIFIES AVE; an AVE-sized coefficient (`δn_bir ≈ −½(E/E_yield)²`) falsifies QED. *Magnitude ratio `7.5/α³ ≈ 1.93×10⁷` is α-echo-flagged — the FORM (tree O(1) vs α²-loop) is the AVE-distinct content, the value rides α⁻³.*
>
> **NON-FALSIFIERS (explicitly excluded — do not re-open):**
> - An **E² slope** does NOT falsify AVE (both AVE and QED are E²-leading; the "E⁴ vs E²" axis is RETRACTED, clm-pp3qwf).
> - An **IM3 cubic (slope-3) drive law** does NOT discriminate (both AVE and QED IM3 are cubic-in-drive / χ⁽³⁾; QED's "sextic" is the frequency exponent, not a drive slope).
>
> **Parameter-free where possible:** the static-B null (PRIMARY) is fully parameter-free. The coefficient (SECONDARY) is field-independent but α-rooted.
>
> **Frozen values (live from `ave.core.constants`, `bffc16b9`):** `E_yield = 1.130×10¹⁷ V/m`, `E_crit = 1.323×10¹⁸ V/m`, `(E_crit/E_yield)² = 1/α = 137.036`, `δn_bir = −½A²`, `δn_iso = −¼A²`, IM3 drive slope = 3, ratio_diff = `7.5/α³ = 1.930×10⁷`.

## 6. Consistency-vs-emergence ledger

| Element | Class | Status |
|---|---|---|
| `S(A) = √(1−A²)` kernel | input | Axiom-4 (canonical) |
| `C(V)/C₀ = 1/S = 1 + ½A² + ⅜A⁴` | **MANIFESTATION** | DERIVED — kernel Taylor (driver, HALT-on-mismatch); matches `intermodulation-distortion.md` eq.35-36 |
| `δn_iso = √S − 1 = −¼A²` (E²-leading) | **MANIFESTATION** | DERIVED — kernel-set O(1) coefficient `−¼`; the E² SCALING is DERIVED not fit |
| `δn_bir = n∥−n⊥ = −½A²` | **MANIFESTATION** | DERIVED — uniaxial probe tensor = exact kernel differential (OQ-1) |
| IM3 cubic-in-drive (slope 3) | **MANIFESTATION** | DERIVED — χ⁽³⁾ from the quartic kernel term; SHARED with QED (not a discriminator) |
| Static-B `δn_μ = 0` exactly (E-vs-B asymmetry) | **CHORD candidate** | DERIVED + parameter-free — the genuine AVE-distinct forward prediction |
| Ratio `7.5/α³ ≈ 1.93×10⁷` | **ECHO** (value) / CHORD (form) | FORM (tree O(1) vs α²-loop) DERIVED; MAGNITUDE rides α⁻³ = α-echo |
| `α`, `E_yield` value via `√α·E_crit` | **ECHO** | AVE does not derive α; `E_yield = √α·E_crit` is α-rooted |
| QED `(3/45)α²`, Euler-Heisenberg legs | non-AVE literature baseline | not fit; labeled SM (symmetric-standard) |

**No-α-hiding check:** the α-dependence is explicit everywhere it enters — the magnitude ratio `7.5/α³`, the substrate identity `E_yield = √α·E_crit`, the QED `α²` legs. Nothing α-rooted is presented as α-free. The static-B chord (PRIMARY falsifier) is the one genuinely α-free prediction.

**Consistency-vs-emergence verdict:** the SCALING (E²) and the COEFFICIENTS (`−¼`, `−½`, `½`, `⅜`) are DERIVED MANIFESTATIONS of the kernel (not fit — driver validates-on-known with HALT). The static-B transparency is a DERIVED, parameter-free CHORD candidate. The magnitude `1.93×10⁷` is GROUNDED in form but its value is an α-ECHO. Honest split throughout.

---

## 7. Where this homes in Vol-9 (the P2 IM3/harmonic gap)

The IM3 / harmonic-distortion characterization is a **Vol-9 device-datasheet** observable (the executable-textbook layer), distinct from the Vol-4 falsifier framing:
- **Vol-9 Ch.3 (Pin/Port Configuration)** already hosts `per-dof-vacuum-node-circuit.md` (the node-constitutive tensor) and `node-up-small-large-signal.md` lives in Vol-4 Ch.1 circuit-theory. The IM3 *characterization* (the χ⁽³⁾ Taylor expansion + the cubic drive law + the bankable δn table) is the **small-signal-distortion datasheet entry** beneath the multi-port LC node — it characterizes the node's nonlinear-reactance spectral signature.
- **Proposed Vol-9 home:** a characterization leaf under Ch.3 (or the Vol-9 device chapter that owns the node datasheet), titled e.g. *"Vacuum-node IM3 / harmonic-distortion datasheet"*, containing: (1) the kernel-Taylor χ⁽³⁾ derivation, (2) the cubic-in-drive IM3 law (with the shared-with-QED caveat), (3) the per-node-vs-apparatus A correction (the −360 dBc per-node honest figure), (4) the bankable δn(E) table, (5) the static-B-transparent keying note cross-linking `node-up-small-large-signal.md`. This is **CONSISTENCY-class** (re-expresses the kernel + the canonical IM3 leaf as a device datasheet; originates no new number).
- **The auditor lands the Vol-9 leaf** (lane discipline); this doc + driver are the implementer substrate.

---

## 8. Open forks

1. **Static-B sensitivity gap (chord-decisiveness).** The static-B chord is parameter-free and falsifiable but becomes a *decisive* discriminator only when static-B birefringence sensitivity reaches the QED ~10⁻²³ level. Until then it's a clean falsifier without a confirming measurement. (Tracked: the QED-nonzero leg is itself unmeasured.)
2. **B-scale inconsistency (~5×, flagged not fixed).** The corpus carries two magnetic yield-scales disagreeing by ~5× (`B_SNAP = 1.89×10⁹ T` energy-density vs `E_yield/c ≈ 3.77×10⁸ T` ε-proxy; `pvlas-static-b-verdict.md`:56-64). Does NOT touch the R3 static-B verdict (`A_I = 0` regardless of which B-scale), but flagged per flag-don't-fix; awaits Grant adjudication.
3. **OQ-1 residual R-3 (polarimetry floor validate-on-known).** The polarimetry/detector floor (~10⁻⁹/10⁻¹¹ rad) is still owed a validate-on-known against a specific published cavity (`2026-06-21_oq1-…-derivation.md`:§7). Does NOT touch the coefficient (g cancels in the ratio).
4. **R-1 / R-2 (single-invariant modeling choice).** AVE's `u = |E|²` single-invariant kernel collapses QED's two Lorentz invariants `(E²−B², E·B)`; this is a substrate-native choice, not a derived necessity (the reason AVE's par−perp factor `½` is not independently tensor-structured the way QED's `7/45` vs `4/45` is). Carried, not resolved.

---

## 9. Verify-before-cite audit log (2026-06-24, HEAD `bffc16b9`)

| Cited anchor | Verification |
|---|---|
| `vacuum-birefringence-e4.md`:31,:37,:41 (δn_bir = −½A², 7.5/α³, √ε-conflation provenance) | grep ✓ |
| `intermodulation-distortion.md`:35-36 (C(V) Taylor ½A², ⅜A⁴), :99 (sextic = freq not drive) | grep ✓ |
| `node-up-small-large-signal.md`:§1,:38 (varactor/inductor keyed args), R1/R2/R3 table | grep ✓ |
| `pvlas-static-b-verdict.md`:38 (δn_μ=0 exact), :56-64 (B-scale ~5× flag) | grep ✓ |
| `divergence-test-substrate-map.md`:450 (B1 row, E⁴ strikethrough → coefficient) | grep ✓ |
| `ave.core.constants` (E_YIELD, E_CRIT, ALPHA, (E_crit/E_yield)²=1/α) | live ✓ (driver) |
| `ave.bench.birefringence` (delta_n_ave_differential_exact, delta_n_ave_exact) | live ✓ (driver) |
| Kernel Taylor coefficients (½, ⅜, −¼, −½), IM3 slope 3 | driver HALT-on-mismatch ✓ |

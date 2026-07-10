[↑ Ch.3 Pin/Port Configuration](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: "Vol-9 Class-C CONSISTENCY characterization datasheet — the vacuum-node IM3 / harmonic-distortion / nonlinear-birefringence δn(E) spectral signature. Re-expresses the Axiom-4 saturation kernel S(A)=√(1−A²) and the canonical Vol-4 IM3 leaf (intermodulation-distortion.md, clm-vjv4zf/clm-pp3qwf) as a node-level small-signal-distortion datasheet entry beneath the multi-port LC node. Originates NO new substrate primitive and NO value-prediction: the χ⁽³⁾ Taylor coefficients (½, ⅜, −¼, −½) are kernel-set O(1) (validate-on-known, HALT-on-mismatch in the driver); the bankable δn ratio 7.5/α³ is an α-ECHO at the value level. The ONE parameter-free AVE-distinct content is the E-vs-B keying asymmetry, surfaced here as a chord CANDIDATE with a clean falsifier, not a confirmed/bankable chord."
-->

> 🔴 **QED-NORMALIZATION CORRECTION (2026-07-03; Rule-12 — body preserved below, git is the trail).**
> Every "7.5/α³ ≈ 1.93×10⁷" bankable-δn-ratio below carries an understated QED denominator ((3/45)α² is too
> small by 1/(2πα) ≈ 21.8 vs the PVLAS-anchored magnetic leg). **Corrected (v3 headline, single instantaneous
> footing — OPTION-B re-freeze 2026-07-07): 3.75π/α² ≈ 2.2×10⁵** (the 2026-07-03 QED-normalization step gave the
> propagating/mixed-footing 7.5π/α² ≈ 4.42×10⁵, exactly double via the ⟨cos²⟩=½ carrier average; 15π/α² ≈ 8.85×10⁵
> static-E; no order of magnitude or falsifier verdict changes). The χ⁽³⁾ kernel coefficients, the α-ECHO grade, and the E-vs-B
> keying chord-candidate are UNAFFECTED. Canonical:
> [`../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md`](../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md);
> reconciliation `research/2026-07-03_birefringence-qed-normalization-correction.md`.

## Vacuum-Node IM3 / Harmonic-Distortion Datasheet (δn(E) spectral signature, characterization leaf)

**Classification:** Class C — CONSISTENCY characterization. This leaf is the **device-datasheet** companion to the Vol-4 falsifiers [`intermodulation-distortion.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md) (clm-vjv4zf, clm-pp3qwf) and [`vacuum-birefringence-e4.md`](../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md) (clm-pp3qwf). It characterizes the **nonlinear-reactance spectral signature** of the multi-port LC vacuum node ([`device-circuit-models.md`](device-circuit-models.md), [`per-dof-vacuum-node-circuit.md`](per-dof-vacuum-node-circuit.md)) — the χ⁽³⁾ intermodulation, the cubic-in-drive IM3 law, and the field-dependent index shift δn(E) — as one Axiom-4-kernel characterization. It originates no new number; the kernel coefficients are validate-on-known, the bankable magnitude is an α-echo.

**Skills applied (2026-06-24 pass):** `substrate-native-check` (kernel-first, no SM Lagrangian default) · `consistency-vs-emergence` v1.3 (Class-C tag; every coefficient classed kernel-MANIFESTATION vs α-ECHO; structural-vs-asserted table §5) · `verify-before-cite` (anchors re-grepped) · `phase-space-coordinate-check` (A_V vs A_I keyed-argument discipline) · `pre-test-physics-check`.

**Discipline:** This leaf is the **source of truth** for the vacuum-node IM3 / harmonic-distortion datasheet characterization. The CODE demonstration is `src/scripts/vol_9_device/im3_vacuum_harmonic_distortion.py` (results `src/scripts/vol_9_device/_output/im3_vacuum_harmonic_distortion.json`), all constants pulled live from `ave.core.constants` (no hardcoded canon), kernel-Taylor coefficients validate-on-known with HALT-on-mismatch. Research provenance: [`research/2026-06-24_e4-im3-vacuum-distortion.md`](../../../../research/2026-06-24_e4-im3-vacuum-distortion.md).

> ↗ See also: [`intermodulation-distortion.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md) (the Vol-4 falsifier this re-expresses; per-node correction); [`vacuum-birefringence-e4.md`](../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md) (the COEFFICIENT falsifier; the δn_bir differential); [`node-up-small-large-signal.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md) (the varactor/inductor keyed-argument duality; E-route scope); [`per-dof-vacuum-node-circuit.md`](per-dof-vacuum-node-circuit.md) (the node this characterizes); [`k4-bloch-dispersion-quartic.md`](../../vol4/falsification/ch12-falsifiable-predictions/k4-bloch-dispersion-quartic.md) (the **distinct** (qℓ)⁴ wavevector-quartic, NOT this field-E² shift).

---

### 1. The kernel-Taylor characterization (χ⁽³⁾ source + the scaling verdict)

The single input is the Axiom-4 universal saturation kernel (the quarter-arc / Born-Infeld form):

$$S(A) = \sqrt{1 - A^2}, \qquad A \equiv \frac{E}{E_{yield}} = \frac{V}{V_{yield}}, \quad E_{yield} = \sqrt\alpha\,E_{crit} \approx 1.13\times10^{17}\ \text{V/m}.$$

Three node-level observables, each a Taylor expansion of the one kernel — the driver recovers the small-$A$ coefficients NUMERICALLY and HALTs if they miss the analytic value (validate-on-known; the coefficients are kernel-set O(1), NOT fit):

| Observable | Expansion | Leading coeff | Driver (HALT-on-mismatch) |
|---|---|---|---|
| **Capacitance varactor** (IM3 source) $C(V)/C_0 = 1/S$ | $1 + \tfrac12 A^2 + \tfrac38 A^4 + \cdots$ | $+\tfrac12 A^2$ | $+0.500000$ ($A^2$), $+0.3751$ ($A^4$) |
| **Single-arm index** (common-mode, polarimeter-blind) $\delta n_{iso}=\sqrt S-1$ | $-\tfrac14 A^2 - \tfrac{3}{32}A^4 - \cdots$ | $-\tfrac14 A^2$ | $-0.250000$ ($A^2$) |
| **Par−perp birefringence** (OQ-1 falsifier observable) $\delta n_{bir}=n_\parallel - n_\perp$ | $-\tfrac12 A^2 + \cdots$ | $-\tfrac12 A^2$ | $-0.500000$ ($A^2$) |

The varactor's $A^4$ Taylor coefficient ($+\tfrac38$) matches [`intermodulation-distortion.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md):35-36 exactly. Under a dual-tone drive $V = V_1\cos\omega_1 t + V_2\cos\omega_2 t$, the **quadratic** $\tfrac12 A^2$ term is the χ⁽³⁾ source that mixes to the third-order intermodulation (IM3) products $2\omega_1-\omega_2$, $2\omega_2-\omega_1$; the IM3 amplitude is **cubic in drive** (driver log-log slope $= 3.000$).

> **SCALING VERDICT — δn is $E^2$-leading, NOT $E^4$ (the √ε conflation, named).** The historical "$\delta n\propto E^4$" was a $\sqrt\varepsilon$ conflation: the quantity $1-S = +\tfrac12 A^2 + \tfrac18 A^4$ is the **permittivity-saturation DEPTH** — itself $E^2$-leading (leading term $\tfrac12 A^2$, NOT $A^4$). The **index observable** is $n=\sqrt S$, giving $\delta n_{iso}=\sqrt S-1\approx-\tfrac14 A^2$ — $E^2$-leading. Someone read the **$A^4$ sub-leading term of $1-S$** as if it were the leading index shift. This is retracted corpus-wide (clm-pp3qwf, commit `ad26d357`; [`vacuum-birefringence-e4.md`](../../vol4/falsification/ch12-falsifiable-predictions/vacuum-birefringence-e4.md):41). **The (genuinely $E^4$) energy-density / Lagrangian quartic** of the Euler-Heisenberg structure ([`nonlinear-telegrapher.md`](../../vol1/dynamics/ch3-quantum-signal-dynamics/nonlinear-telegrapher.md):33-39) is a DIFFERENT observable and is correct — do not re-import it as an index scaling.

### 2. The shared-with-QED non-falsifiers (symmetric standard, stated up front)

QED (Euler-Heisenberg) **already** predicts vacuum nonlinear optics. This must be stated so the datasheet claims nothing QED also has. Two AVE signatures here are **SHARED** with QED and **do NOT discriminate**:

| Observable | QED (Euler-Heisenberg) | AVE (Axiom-4 kernel) | Discriminates? |
|---|---|---|---|
| δn field-scaling exponent | $E^2$ ($(E/E_{crit})^2$) | $E^2$ ($-\tfrac12 A^2$) | **NO** — both $E^2$-leading |
| IM3 drive exponent | 3 (cubic, χ⁽³⁾ from the quartic $(E^2-B^2)^2$ Lagrangian) | 3 (cubic, χ⁽³⁾ from the quartic kernel term) | **NO** — both cubic-in-drive |

> **The QED "sextic" is a frequency exponent, NOT a drive slope.** The only "$^6$" in QED is the **frequency** exponent $(\omega/m_ec^2)^6$ of the Euler-Heisenberg light-by-light cross-section $\sigma_{EH}$ ([`intermodulation-distortion.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md):99 retraction) — measuring the IM3-vs-DRIVE exponent reads $3$ for both. **Anyone re-proposing "AVE predicts $E^4$ / $V^6$" is re-opening a closed negative** (clm-pp3qwf). An $E^2$ slope and a cubic IM3 are NON-FALSIFIERS.

### 3. The bankable δn table (AVE vs QED, the sign-flip)

The matched **par−perp differential** observable (what a PVLAS/BMV-class ellipsometer reads) at stated reference fields, all from live `ave.core.constants` (driver `bankable_table`). AVE $\delta n_{bir}=-\tfrac12 A^2$ vs QED differenced Euler-Heisenberg $\delta n_{QED}=\tfrac{3}{45}\alpha^2(E/E_{crit})^2$:

| Reference field $E$ [V/m] | $A=E/E_{yield}$ | $\delta n_{AVE}$ (par−perp) | $\delta n_{QED}$ (par−perp) | ratio AVE/QED |
|---|---|---|---|---|
| $2.745\times10^{14}$ (PW-class focal, OQ-1 headline) | $2.43\times10^{-3}$ | $\mathbf{-2.95\times10^{-6}}$ | $+1.53\times10^{-13}$ | $1.93\times10^7$ |
| $1.0\times10^{15}$ (facility IM3 $-80$ dBc floor) | $8.85\times10^{-3}$ | $-3.91\times10^{-5}$ | $+2.03\times10^{-12}$ | $1.93\times10^7$ |
| $1.0\times10^{16}$ | $8.85\times10^{-2}$ | $-3.94\times10^{-3}$ | $+2.03\times10^{-10}$ | $1.95\times10^7$ |

**Two genuine signatures** (NOT the exponent):
- **SIGN FLIP.** AVE $\delta n$ is **negative** (permittivity softening, $-\tfrac12 A^2$); QED's par−perp differential is **positive** ($+\tfrac{3}{45}\alpha^2$). The instrument reads $|\delta n|$ as accumulated ellipticity, but the sign is a structural difference.
- **MAGNITUDE ratio $7.5/\alpha^3\approx1.93\times10^7$** (field-independent), using the substrate identity $(E_{crit}/E_{yield})^2=1/\alpha$. The **FORM** (tree-level O(1) saturation vs QED's $\alpha^2$-loop) is AVE-distinct; the **MAGNITUDE** rides $\alpha^{-3}$ and AVE does not derive $\alpha$ → **α-ECHO at the value level**. Symmetric standard: QED's coefficient $a_{EH}\alpha^2$ is *equally* α-rooted. **Do NOT headline the magnitude as a chord.**

> **Headline bankable number:** at $E=2.745\times10^{14}$ V/m, **AVE $\delta n=-2.95\times10^{-6}$** vs **QED $\delta n=+1.53\times10^{-13}$**, ratio $1.93\times10^7$. GROUNDED in form (kernel coefficient $\tfrac12$ + the substrate $\sqrt\alpha$ scaling, validate-on-known with HALT) but the *value* of the ratio is an α-echo.

### 4. The E-vs-B keying asymmetry (chord CANDIDATE) + the E-route bench

The one genuinely AVE-distinct, parameter-free content is the **E-vs-B keying asymmetry** — surfaced here as a **chord CANDIDATE with a clean falsifier, NOT a confirmed/bankable chord**. The node carries two reactive grades keyed on DIFFERENT drive variables ([`node-up-small-large-signal.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/node-up-small-large-signal.md):§1):

- **ε-grade = VARACTOR, keyed on VOLTAGE** $V$ (field $E$): $C_{eff}=C_0/S(A_V)$, $A_V=V/V_{yield}$. A static **E** is a real DC operating point → loads ε → $\delta n\neq0$ (regime R2).
- **μ-grade = relativistic INDUCTOR, keyed on circulating CURRENT** $I$: $L_{eff}=L_0/S(A_I)$, $A_I=I/I_{max}$. A static external **B** has $\partial B/\partial t=0$ → by Lenz no internal vacuum circulation → $I_{vac}=0$ → $A_I=0$ → $S_\mu=\sqrt{1-0^2}=1$ → $\mu_{eff}=\mu_0$ → $\delta n_\mu=0$ **analytically exact at every field** (regime R3). Driver `keying_asymmetry`: $S_\mu=[1,1,1,1]$, $\delta n_\mu=[0,0,0,0]$ at $B=2.5,10,100,1000$ T.

QED's $\delta n\propto(E^2-B^2)$ is **E/B symmetric** → it predicts the same-sign nonzero static-B birefringence (~$10^{-23}$ at 5 T) as static-E. AVE predicts a **categorical zero** under static B, **nonzero** under static E. This follows from *which argument keys which grade* — **parameter-free** (no α, no fitted coefficient).

> **Chord-CANDIDATE status (no over-claim).** This is a genuine AVE-distinct forward prediction, but a **chord candidate with a clean falsifier**, NOT a confirmed/bankable chord. **The honest ceiling:** the static-B null that PVLAS/BMV *already return* is the AVE-EXPECTED result — it **discriminates nothing** against QED until static-B sensitivity reaches the QED ~$10^{-23}$ level (no instrument has yet measured static-B birefringence at the QED level to confirm the QED-nonzero leg). The clean falsifier: a static-B birefringence detection at/above ~$10^{-23}$ (5 T) FALSIFIES AVE. Canonical static-B verdict: [`pvlas-static-b-verdict.md`](../../vol4/falsification/ch11-experimental-bench-falsification/pvlas-static-b-verdict.md).

**The E-route bench (the discriminating test).** The discriminating measurement is the **E-route** (static / DC-biased / quasi-DC **E**, loading the V-keyed varactor), NOT the static-B magnet route:

| Parameter | Value / spec | Basis |
|---|---|---|
| **Field route** | static / DC-biased **E** (NOT static B) | only E loads the V-keyed varactor (R2) |
| **Facility** | HIBEF @ European XFEL + PW-laser focal sources | `research/2026-06-22_vacuum-birefringence-facility-tolerance-survey.md` |
| **Reference field** | $E\approx2.745\times10^{14}$ V/m → $A=2.43\times10^{-3}$ | OQ-1 headline point |
| **Observable 1 (birefringence)** | par−perp differential δn → ellipticity ψ; linearly-polarized pump + 45°-launched probe in a high-finesse cavity | OQ-1 Step 2-3 |
| **Observable 2 (IM3 spectroscopy)** | dual-tone $f_1,f_2$ (Δf ~ 1 GHz); heterodyne detect IM3 at $2f_1-f_2$; confirm **cubic** (slope-3) drive law | [`intermodulation-distortion.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md) (per-node corrected) |
| **SNR ask (IM3)** | IM3 sideband above $-80$ dBc requires $E\approx1.3\times10^{15}$ V/m (per-node corrected; facility-class, NOT tabletop) | [`intermodulation-distortion.md`](../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/intermodulation-distortion.md):86 |
| **Static-B null check** | apply static B (2.5 T → 1 kT); AVE predicts δn = 0 exactly | the chord candidate's clean falsifier |

### 5. What is structurally-derived vs echo (consistency-vs-emergence)

| Element | Class | Status |
|---|---|---|
| $S(A)=\sqrt{1-A^2}$ kernel | input | Axiom-4 (canonical) |
| $C(V)/C_0 = 1/S = 1+\tfrac12 A^2+\tfrac38 A^4$ | **MANIFESTATION** | DERIVED — kernel Taylor (driver, HALT-on-mismatch); matches intermodulation-distortion.md eq.35-36 |
| $\delta n_{iso}=\sqrt S-1=-\tfrac14 A^2$ ($E^2$-leading) | **MANIFESTATION** | DERIVED — kernel-set O(1); the $E^2$ SCALING is DERIVED not fit |
| $\delta n_{bir}=n_\parallel-n_\perp=-\tfrac12 A^2$ | **MANIFESTATION** | DERIVED — uniaxial probe tensor = exact kernel differential (OQ-1) |
| IM3 cubic-in-drive (slope 3) | **MANIFESTATION** | DERIVED — χ⁽³⁾ from the quartic kernel term; **SHARED with QED** (NOT a discriminator) |
| $E^2$ field-scaling exponent | — | **SHARED with QED** (NOT a discriminator); the "$E^4$" was the √ε conflation, RETRACTED |
| Static-B $\delta n_\mu=0$ exactly (E-vs-B asymmetry) | **CHORD CANDIDATE** | DERIVED + parameter-free; clean falsifier, NOT a confirmed/bankable chord (§4) |
| Ratio $7.5/\alpha^3\approx1.93\times10^7$ | **ECHO** (value) / FORM (structure) | FORM (tree O(1) vs α²-loop) DERIVED; MAGNITUDE rides α⁻³ = α-echo |
| $\alpha$, $E_{yield}$ value via $\sqrt\alpha\,E_{crit}$ | **ECHO** | AVE does not derive α |
| QED $\tfrac{3}{45}\alpha^2$ legs | non-AVE baseline | not fit; labeled SM (symmetric-standard) |

**Bottom line:** the datasheet is a CONSISTENCY characterization. The SCALING ($E^2$) and the COEFFICIENTS ($-\tfrac14$, $-\tfrac12$, $\tfrac12$, $\tfrac38$) are DERIVED kernel manifestations (validate-on-known, HALT). The static-B transparency is a DERIVED parameter-free CHORD CANDIDATE (clean falsifier, not confirmed). The magnitude $1.93\times10^7$ is GROUNDED in form but its value is an α-ECHO. It originates no new substrate primitive and no new value.

### 6. The frozen pre-reg

The frozen pre-registration for this characterization (E-route birefringence δn(E), IM3 dual-tone distortion, static-B transparency side-prediction, with PRIMARY/SECONDARY falsifiers and the explicit NON-FALSIFIER list) is frozen at:

> → [`research/2026-06-24_e4-im3-vacuum-distortion.md`](../../../../research/2026-06-24_e4-im3-vacuum-distortion.md) §5 (PRE-REG E4-IM3-DISTORTION, frozen 2026-06-24, SHA-pinnable on `analysis/e4` HEAD) — and the companion pre-reg [`research/2026-06-24_e4-im3-vacuum-distortion_prereg.md`](../../../../research/2026-06-24_e4-im3-vacuum-distortion_prereg.md).

**NON-FALSIFIERS (do not re-open):** an $E^2$ slope does NOT falsify AVE (both $E^2$-leading; the "$E^4$ vs $E^2$" axis is RETRACTED, clm-pp3qwf); a cubic (slope-3) IM3 drive law does NOT discriminate (both AVE and QED IM3 are cubic / χ⁽³⁾).

---

### Verify-before-cite audit log (2026-06-24)

| Cited anchor | Verification |
|---|---|
| `intermodulation-distortion.md`:35-36 (C(V) Taylor ½A², ⅜A⁴), :86 (−80 dBc field), :99 (sextic = freq not drive) | grep ✓ |
| `vacuum-birefringence-e4.md`:31,:37,:41 (δn_bir = −½A², 7.5/α³, √ε-conflation provenance) | grep ✓ |
| `node-up-small-large-signal.md`:§1 (varactor/inductor keyed args), R2/R3 keying | grep ✓ |
| `pvlas-static-b-verdict.md` (δn_μ=0 exact static-B verdict) | grep ✓ |
| `nonlinear-telegrapher.md`:33-39 (energy-density E⁴ vs index E² — the distinct correct quartic) | grep ✓ |
| `k4-bloch-dispersion-quartic.md` ((qℓ)⁴ wavevector-quartic = distinct mechanism, stands) | grep ✓ |
| `ave.core.constants` (E_YIELD, E_CRIT, ALPHA, (E_crit/E_yield)²=1/α=137.036) | live ✓ (driver) |
| Kernel Taylor coeffs (½, ⅜, −¼, −½), IM3 slope 3 | driver HALT-on-mismatch ✓ |

---

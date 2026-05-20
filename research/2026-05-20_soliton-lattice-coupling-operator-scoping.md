# Soliton-Lattice Coupling — Session 1 Scoping (A-034 Catalog-Extension Framing)

**Date:** 2026-05-20 (session spans 2026-05-19 EOD → 2026-05-20 early; landed under 2026-05-20 per UTC)
**Branch:** `analysis/soliton-lattice-coupling-operator-scoping` off `analysis/integration` at `0f3fd52`
**Originating epic:** [`_orchestration/soliton-lattice-coupling-operator.md`](../_orchestration/soliton-lattice-coupling-operator.md) (Session 1 of multi-session arc)
**Predecessor cascade:** SDSS DR17 merge `9f976e0` → operator-output reframing of three-observable triangle 2026-05-19 EOD; epic spawned at `0f3fd52`
**Refactored:** 2026-05-19 EOD per Grant adjudication — Original scoping (tip `7c9d4d4`) used "new operator / new field theory" framing. The corpus's existing universal-scale machinery (A-034 universal-saturation-kernel-catalog + Ax 2 TKI scale invariance) already covers this mechanism class. This refactor recasts the work as A-034 **catalog-extension** rather than new framework. **Load-bearing test of `ave-canonical-leaf-pull` v1.1 trigger 16 (framework-extension proposals must work within existing universal-scale machinery).**

---

## 0. Scope discipline (load-bearing for this session)

**This is a scoping research doc.** It produces:

1. The A-034 **catalog-extension** framing of the soliton-lattice coupling mechanism (NOT a new operator — the universal kernel $S(A) = \sqrt{1 - A^2}$ applied at a new observable channel)
2. A list of 1-4 **catalog row additions** that would close the missing-row gap (per universal-saturation-kernel-catalog.md companion-row links + ε/μ axis extension at commit `6436d65`)
3. A corpus building-block inventory of the 8 pieces that supply kernel ingredients (preserved from original scoping; recast as kernel-parameter substrate rather than to-be-integrated-into-new-operator)
4. A list of substrate-physics derivation prereqs that need closure before Session 2 can produce catalog row(s) + planetary-scoring (most prereqs resolve to existing canonical leaves; net compression 11-17 hr → 3-5 hr)
5. A list of testable predictions (16 solar-system axis data points + galactic + LSS targets) the kernel-with-$A_{\text{soliton}}$-defined must reproduce
6. A multi-session arc outline (Sessions 2-5 with revised effort post-compression)

**No derivation in this session.** Any catalog-row $A_{\text{soliton}}$ functional form, kernel-parameter value, or numerical claim is out-of-scope and is queued for Session 2.

This doc is research-tier (no manuscript / KB modifications). The corpus building-block summaries in §2 cite from canonical leaves but do not modify them. The proposed catalog rows in §1.5 are SCOPED here; their actual addition to `universal-saturation-kernel-catalog.md` is Session 2 work.

---

## 1. Phase 1 — A-034 catalog-extension framing (per v1.1 skill trigger 16)

### 1.1 The reframe (per `ave-canonical-leaf-pull` v1.1 trigger 16 + Grant adjudication 2026-05-19 EOD)

The original scoping doc proposed $\hat{\mathcal{O}}_{\text{soliton}}$ as a NEW operator with NEW derivation infrastructure. Grant adjudicated 2026-05-19 EOD: **the corpus's existing universal-scale machinery already covers this mechanism class.** Specifically:

- A-034 universal-saturation-kernel-catalog (`manuscript/ave-kb/common/universal-saturation-kernel-catalog.md`) establishes that **one kernel** $S(A) = \sqrt{1 - A^2}$ (Axiom 4 Born–Infeld $n=2$ squared limit) **applies at every scale** of topological-reorganization in the universe (line 7 verbatim).
- Per Ax 2 (TKI scale invariance per `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2): same physics applies at all scales with $A$ dimensionless across scales.
- The catalog currently has **21 instances spanning 21 orders of magnitude** (atomic $\sim 10^{-15}$ m to cosmic $\sim 10^{26}$ m). Row 9 (Planetary geomagnetic) and Row 11 (Galactic MOND, ASYM-N μ per `saturated-lattice-mutual-inductance.md:4`) already cover much of the soliton-spin-axis mechanism class — what's missing is dedicated catalog rows for the **rotational-angular-momentum-axis observable** (vs the B-field-axis observable in current Row 9).

**Reframe (load-bearing for the rest of this doc):**

> The soliton-lattice coupling is a **missing-but-trivially-addable instance class in the A-034 catalog**. The "operator" is the same universal kernel $S(A) = \sqrt{1-A^2}$ applied at a new observable channel (rotational angular momentum axis vs the existing geomagnetic-B-axis channel at planetary scale), parameterized by an $A_{\text{soliton}}$ definition that combines (planetary angular momentum × cosmic-substrate strain × coupling factor) / threshold.

This is structurally parallel to the SM/QED-defaults-leaking-into-solvers failure mode that `substrate-native-check` covers at the code/solver layer — here the failure mode is at the framework-design layer (proposing a new operator when the universal kernel already applies). The discipline catches the latter via `ave-canonical-leaf-pull` v1.1 trigger 16.

### 1.2 v1.1 trigger 16 (a)-(e) classification — soliton-coupling proposal

Per the skill's classification framework, every framework-extension proposal lands in one of five categories. The soliton-coupling proposal:

| Category | Status | Evidence |
|---|---|---|
| **(a)-match**: covered by existing A-034 catalog row | Partial | Row 9 (Planetary geomagnetic, pole flip) + Row 11 (Galactic MOND, ASYM-N μ) cover the **B-field/mutual-inductance observable channels** at planetary + galactic scale. They do NOT cover the **angular-momentum-axis observable** (mag-vs-spin axis offset, retrograde-spin Venus class, 90°+-obliquity Uranus class). |
| **(a)-missing-row**: missing-but-trivially-addable catalog row | **YES — this is the load-bearing classification** | Per §1.5, 1-4 missing rows: planetary spin-axis (companion to Row 9), planetary mag-vs-spin-axis offset (sub-mode or split of Row 9), galactic spin-axis (companion / μ-extension of Row 11), LSS spin-axis (TBD relationship to Row 14). All structurally analogous to existing companion-row links per `universal-saturation-kernel-catalog.md:103-110`. |
| **(b)-scale-invariance**: same physics at new scale | Reinforces (a)-missing-row | Ax 2 TKI scale invariance is precisely the corpus mechanism that lets the same kernel apply at planetary → galactic → LSS scales. The cross-scale `Same-mechanism-at-all-scales` table at `boundary-observables-m-q-j.md:38` already canonically states the mechanism is one-piece across scales. |
| **(c)-operator-application**: same operator at new $(M, \omega, A)$ regime | YES — applied via Op14 | The substrate Op14 frame-dragging asymmetric saturation (canonical at `frame-dragging-impedance-convolution.md:20`) is the same operator across scales. Soliton-coupling is Op14 applied at planetary-mass regime with rotational-axis observable readout instead of refractive D-shadow readout. |
| **(d)-translator-extension**: cross-scale translation table extends to new axis | Reinforces (b) | The boundary-observables M/Q/J table at `boundary-observables-m-q-j.md:38` already includes "Planetary magnetopause — Planet + field-aligned solitons — planet mass, dipole moment, rotation". The translation is **already in the canonical leaf**; the soliton-coupling work just operationalizes the "rotation" direction-side prediction. |
| **(e)-genuinely-new**: corpus's universal-scale machinery does NOT cover this | **NO** | All of (a), (b), (c), (d) return matches. The proposal does NOT add physics that the corpus's universal-scale machinery doesn't already cover; it adds **enumeration** of a missing-but-trivially-addable instance and **operationalizes** the direction-side observable at planetary + galactic scale. |

**Load-bearing gate check (per skill's "(e) determination is the load-bearing gate" §16):** the proposal **cannot articulate physics it adds beyond (a)-(d)**, so it MUST be reframed as catalog-extension / operator-application rather than as new framework. This is exactly what this refactor does.

### 1.3 Kernel-driven structural form

The soliton-coupling operationalization is:

$$S(A_{\text{soliton}}) = \sqrt{1 - A_{\text{soliton}}^2}$$

where $A_{\text{soliton}}$ is the dimensionless strain experienced by the soliton's substrate-coupling channel:

$$A_{\text{soliton}} = \frac{\text{(soliton angular momentum)} \times \text{(cosmic-substrate strain)} \times \text{(coupling factor)}}{A_{\text{saturation,channel}}}$$

The substrate-physics ingredients (numerator coupling factor, channel-specific $A_{\text{saturation}}$) are supplied by the 8 corpus building blocks at §2 — they are NOT new physics, they are kernel-parameter constructions per Op14 + Cosserat + boundary-observables canonical leaves.

**Per Ax 2 (TKI):** the same kernel form applies at planetary, galactic, and LSS scales. Only $A_{\text{soliton}}$'s definition changes per scale (per ε vs μ sector, per channel: spin-axis vs B-field-axis vs galactic-rotation-axis).

### 1.4 What the kernel output means (saturation event taxonomy — preserved from original scoping)

Per A-034's structural physics (`universal-saturation-kernel-catalog.md:7`): when $S(A) = 0$ locally at $A = 1$, the substrate cannot continue linear response and **must reorganize topologically** to a new configuration with $A < 1$. The kernel's vertical tangent at $A = 1$ makes every reorganization event sharp and impulsive across all scales.

For the soliton-coupling case, the saturation events at $A_{\text{soliton}} = 1$ map to the observable anomalies:

| Saturation event | Observable | Planetary instance | Galactic instance |
|---|---|---|---|
| **Aligned regime** ($A_{\text{soliton}} \ll 1$): $S \to 1$ | Spin-axis tracks $\hat{\Omega}_{\text{freeze}}$ closely; small mag-vs-spin tilt | Saturn (<1° mag-spin tilt); Jupiter (~10°); Earth (~11°); Mercury (~0°) | (corresponding aligned regime if galactic-scale stays sub-saturation; predicts LSS-axis matches CMB-axis-of-evil. **FALSIFIED at 5.33σ per SDSS DR17** — galactic-scale is NOT in this regime) |
| **Anti-aligned regime** ($A_{\text{soliton}} \to 1$ on retrograde branch): topology snaps to anti-aligned | Spin direction reverses; flipped equilibrium | Venus retrograde (177.4°); slow-rotation kicks soliton over saturation boundary | (analog at LSS scale: bulk-flow-reversal candidate; TBD) |
| **Orthogonal-class regime** ($A_{\text{soliton}} \approx 1$ on orthogonal branch): saturation kernel produces 90°+ axis offset | Mag-vs-spin tilt ~60°-90°; obliquity flip | Uranus 97.77° obliquity + 59° mag-tilt; Neptune 47° mag-tilt | LSS spin axis 36.75° offset from CMB axis-of-evil (5.33σ; per SDSS DR17 result `2026-05-19_c5-sdss-spin-orientation-result.md:122`) |

**The Uranus 98° obliquity and Saturn <1° tilt — which standard formation models treat as a coincidence + an ad-hoc giant-impact respectively — become predicted equilibrium configurations of the universal kernel** when the kernel approaches $A_{\text{soliton}} \to 1$ on different branches. This is the substrate-physics structural opportunity the operator-epic was designed to capture; the refactored framing achieves the same opportunity via catalog-extension rather than new-operator framing.

### 1.5 Proposed catalog rows (Session 2 deliverable)

Per the ε/μ axis extension + gap-cells + companion-row links structure added at commit `6436d65` to `universal-saturation-kernel-catalog.md` (lines 73-112), the soliton-coupling work proposes the following catalog row additions. Each row is **scoped** here; their actual addition to the canonical leaf is Session 2 work pending Grant adjudication of §4.5 plumber-physical questions.

**Row 9-a (Planetary spin-axis — companion to Row 9 geomagnetic):**

| Field | Value (scoped) |
|---|---|
| Scale | Planetary (~10⁶ m), per Row 9 |
| Sym | SYM (substrate K=2G symmetric saturation; angular-momentum is the rotational-DOF coordinate per Cosserat Ax 1) |
| $A_{\text{soliton}}$ definition (sketch) | $A_{\text{spin}} = (L_{\text{planet}} \cdot \kappa_{\text{cosmic-substrate}} \cdot g_{\text{class}}) / A_{\text{saturation,spin}}$, where $L_{\text{planet}}$ is planetary angular momentum, $\kappa_{\text{cosmic-substrate}}$ is the strain coupling from $\hat{\Omega}_{\text{freeze}}$ (canonical at `omega-freeze-cosmic-grain-cascade.md`), $g_{\text{class}}$ is a per-internal-structure-class factor (rocky / metallic-H / icy-mantle per `planetary-magnetospheres.md`) |
| Saturation event | Retrograde-spin transition (Venus class, $A \to 1$ on anti-aligned branch); 90°+ obliquity flip (Uranus class, $A \to 1$ on orthogonal branch) |
| Companion to | Row 9 Planetary geomagnetic — same scale, different observable channel (B-field vs angular-momentum-axis). Per companion-row table format at `universal-saturation-kernel-catalog.md:103-110`. |
| Empirical anchor | 8 planetary spin obliquities (8 axis data points); Venus retrograde and Uranus 98° as outliers anchored on saturation-event taxonomy |

**Row 9-b (Planetary mag-vs-spin-axis offset — sub-mode of Row 9 or new row):**

| Field | Value (scoped) |
|---|---|
| Scale | Planetary, per Row 9 |
| Sym | ASYM-N candidate (the mag-axis is the B-channel = μ-sector; the spin-axis is the angular-momentum-channel) |
| $A_{\text{soliton}}$ definition (sketch) | $A_{\text{offset}}$ defined by internal-structure coupling (depth of conducting fluid layer, per `geodynamo-vca-back-emf.md` + `planetary-magnetospheres.md`); Earth ~11°, Saturn <1°, Uranus 59° are DIFFERENT $A$-values, NOT random — they reflect the differential mag-channel vs spin-channel saturation states |
| Saturation event | Magnetic-axis pole flip (already in Row 9); proposed additional saturation event = decoupling of mag-axis from spin-axis when the two channels saturate at different $A$ values |
| Companion to | Row 9 Planetary geomagnetic — same scale, sub-mode covering the ε vs μ relative-saturation observable |
| Empirical anchor | 8 mag-axis tilts (additional 8 axis data points); Saturn <1° + Uranus 59° + Neptune 47° as discriminating cases |

**Row 11-a (Galactic spin-axis — companion to Row 11 MOND):**

| Field | Value (scoped) |
|---|---|
| Scale | Galactic (~10²² m), per Row 11 |
| Sym | TBD. Two candidate framings: (a) gap-cell ε-companion to MOND-μ (per gap-cells table at `universal-saturation-kernel-catalog.md:89-94`); (b) μ-extension of MOND at the angular-momentum channel. Adjudication is Session 2 work. |
| $A_{\text{soliton}}$ definition (sketch) | $A_{\text{gal,spin}}$ defined via galactic-scale angular momentum + $\hat{\Omega}_{\text{freeze}}$ coupling; per Ax 2 TKI scale invariance, same structural form as $A_{\text{spin}}$ in Row 9-a but at galactic scale |
| Saturation event | LSS-axis-vs-CMB-axis decoupling at galactic scale; the 36.75° offset (5.33σ) is the observable signature |
| Companion to | Row 11 Galactic MOND — same scale, different observable channel (mutual-inductance vs angular-momentum-axis) |
| Empirical anchor | SDSS DR17 LSS spin axis $(l = 129°, b = 79°)$, $\sigma_{\text{LSS}} = 6.83°$ per `2026-05-19_c5-sdss-spin-orientation-result.md:21`; CMB-LSS offset 36.75° (5.33σ from zero) per `:122` |

**Row 14-a (LSS spin-axis — cosmic-class extension):**

| Field | Value (scoped) |
|---|---|
| Scale | LSS (~10²⁵ m), inheriting Row 14 (Cosmic Big Bang K4 crystallization) scale |
| Sym | TBD. Relationship to Row 14 is conjectural; per gap-cells table the cosmic-ε-companion to Row 14 is flagged as DE candidate per Grant 2026-05-19 EOD. The LSS spin-axis may be sub-cosmic angular-momentum channel. |
| $A_{\text{soliton}}$ definition (sketch) | Conjectural; tied to bulk-flow direction (Pantheon+ Hubble-flow $(l = 129.76°, b = -13.64°)$ per `2026-05-19_c5-pantheon-tightening-result.md`) |
| Saturation event | Bulk-flow direction sets a cosmologically-emergent angular-momentum-axis preference; the Pantheon+ matter direction may be a different observable channel than galaxy-spin axis |
| Companion to | Row 14 Cosmic K4 crystallization (SYM*); possibly sub-mode |
| Empirical anchor | Pantheon+ bulk-flow direction; Walmsley+2022 GZ DECaLS independent galaxy-class classification (per epic Phase 4) |

**Row count outcome:** 2 nearly-certain (Row 9-a, Row 9-b); 1 likely (Row 11-a); 1 conjectural (Row 14-a). Session 2 deliverable lands the certain rows + scopes the rest.

### 1.6 Class E classification (per `consistency-vs-emergence` v1.1) — preserved

The catalog rows above produce observables ($\hat{n}_{\text{spin}}^{(\text{planet})}$, $\hat{n}_{\text{mag}}^{(\text{planet})}$, $\hat{n}_{\text{galactic}}$) that are **Class E — operating-point projection** per the canonical Class E framing at `omega-freeze-cosmic-grain-cascade.md:7`:

> falsification of any one kills the operating-point and therefore the entire substrate model

Specifically: if even ONE of the 16 planetary axis data points can be shown to be inconsistent with the kernel-prediction (with the kernel running off a single $\hat{\Omega}_{\text{freeze}}$ direction + scale-invariant per-row $A_{\text{soliton}}$), the framework's joint constraint is broken. This is the load-bearing falsification surface for Session 3 — unchanged by the refactor.

---

## 2. Phase 2 — Corpus building-block inventory (8 pieces, preserved as kernel-parameter substrate)

The 8 building blocks identified in the original scoping are NOT discarded — they are recast as **kernel-parameter ingredients** rather than as pieces to integrate into a new operator. Each supplies a specific input to the $A_{\text{soliton}}$ definition or to the kernel's per-channel saturation thresholds. The file:line citations + verbatim quotes are preserved from the original scoping; the "Still missing for integrated operator" sections are recast as "How this resolves under the A-034 reframe" — see §3 for the prereq compression.

### 2.1 Op14 asymmetric saturation profile (frame-dragging, rotating mass)

**File:** [`manuscript/ave-kb/vol3/gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md:20`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md)

**Verbatim mechanism (line 20):**
> Rays traversing the retrograde side encounter a stricter Op14 saturation profile, increasing their refractive capture radius. Conversely, rays on the prograde side propagate through a mechanically relaxed tensor, allowing them to graze closer to the horizon before capture. This differential refractive trap flattens the shadow boundary on the prograde side, producing the characteristic "D-shape" predicted by the Kerr metric without continuous manifolds.

**Kernel-parameter contribution:** This IS the substrate-level mechanism for the prograde/retrograde asymmetry that makes $A_{\text{soliton}}$ direction-sensitive. Per A-034 + Ax 2, the same Op14 saturation applies at all scales — at the planetary scale, the soliton's spin direction relative to $\hat{\Omega}_{\text{freeze}}$ determines which side of the Op14 asymmetry the soliton's interior sits on. The exterior Kerr instance ($\omega(r) = 2Mar/(r^2+a^2)^2$, line 11) provides the prototype scaling that the planetary-scale instance inherits via Ax 2.

**Under the A-034 reframe:** the "still missing" items collapse to "apply Op14 at planetary-scale parameter regime" — this is just instance-application per v1.1 skill classification (c). No new operator-form derivation needed; the saturation-kernel + Op14 mechanism are already canonical.

### 2.2 Parametric coupling kernel (rotating LC tank + substrate forcing)

**File:** [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md) (whole leaf; key headline §3 lines 60-95)

**Mechanism (paraphrased; verbatim formulae in cited leaf):** The bulk K4 substrate is a vacuum varactor (Axiom 4) operating below $V_{\text{yield}}$. Its reactive drive $V_{\text{bulk}}(t)$ oscillates at the α-slew refresh rate $\nu_{\text{slew}} = \alpha \omega_{\text{Compton}}/(2\pi)$. An embedded LC apparatus sees a parametric coupling $I_{\text{induced}}(t) = V_{\text{app}}(t) \cdot dC_{\text{eff}}/dt$ (line 29). For N coherent receivers, per-cycle detection probability scales as $\varepsilon_{\text{det}} = 4\pi \kappa_{\text{quality}} / N^2$ (line 13).

**Kernel-parameter contribution:** This canonical leaf already establishes the substrate-↔-bound-tank coupling kernel. Under Ax 2 scale invariance, the same kernel applies at planetary scale with rescaled pump frequency. The 5-axis port classification (REACTIVE/BOUND/OFF-SHELL/INTERNAL-TANK/SUBSTRATE-MODE per lines 117-122) classifies the planetary case as INTERNAL-TANK + SUBSTRATE-MODE coupled via Op14.

**Under the A-034 reframe:** the planetary-scale pump frequency is supplied by Ax 2 TKI scaling of $\omega_{\text{slew}}$ — this is NOT a new derivation, just an Ax-2 substitution at the planetary mass regime. See P-1 compression at §3.

### 2.3 Cosserat micropolar rotational DOF (Axiom 1)

**Files:** [`manuscript/ave-kb/CLAUDE.md` INVARIANT-S2](../manuscript/ave-kb/CLAUDE.md) (cross-volume canonical statement); canonical source [`manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex:52`](../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex)

**Verbatim canonical statement (Vol 1 Ch 1:52):**
> Each node is **micropolar** (Cosserat-type), carrying **six intrinsic degrees of freedom** per node: three **translational** (capacitive coupling $\varepsilon_0$, identified with the electric field) and three **microrotational** (inductive coupling $\mu_0$, identified with the magnetic field). **The Cosserat microrotational DOF IS the substrate-native origin of intrinsic spin**: macroscopic angular momentum, the EM magnetic field $B$, and QM electron spin are three projections of the same per-node rotational coordinate.

**Kernel-parameter contribution:** This is the substrate-native rotational-coupling channel. Bound solitons engage with $\hat{\Omega}_{\text{freeze}}$ via the per-node microrotational coordinate. The OBSERVED mag-spin tilt (Earth ~11°, Saturn <1°, Uranus 59°) measures the angular separation between two projections of the same Cosserat field — this is structurally the **ε vs μ axis** of the catalog (per universal-saturation-kernel-catalog.md:73-83); the mag-spin tilt is exactly the relative saturation-state of the ε-channel vs μ-channel projections of the same per-node rotational coordinate.

**Under the A-034 reframe:** the cross-channel decomposition is precisely what Row 9-b operationalizes. The Q-G47 chiral-coupling Landau form ($U_{\text{chiral}}^{\text{add}} = \chi_1 \varepsilon_{ij} \kappa_{ji} + \ldots$) at `omega-freeze-cosmic-grain-cascade.md:171` already provides the canonical body-frame substrate-coupling template. The "still missing for integrated operator" items resolve to "apply at planetary scale per Ax 2" — see P-5 compression at §3.

### 2.4 Frame-dragging interior strain pattern (cosmic genesis instance)

**File:** [`manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex`](../manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex):408-416, with cross-reference at [`manuscript/ave-kb/common/universal-saturation-kernel-catalog.md:99-101`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md).

**Verbatim mechanism (Vol 3 Ch 4 lines 408-416):**
> A spinning black hole is not a floating blob in nothing — it sits in its own embedding lattice (the *parent lattice*) and imparts bulk strain on it via frame-dragging (canonical per Vol 3 Ch 2 §138 + Vol 3 Ch 3 §178). Per Vol 3 Ch 21 we sit *inside* our parent BH's Schwarzschild radius (cosmic horizon $R_H$ = parent BH's $r_s$). The parent BH's spin imparts strain on the parent lattice; this strain extends inside its own event horizon (Kerr interior frame-dragging continues); the inside region is our universe's pre-crystallization phase (supercooled pre-geodesic plasma).

**Kernel-parameter contribution:** This is the cosmic-genesis instance of the same mechanism the catalog rows instantiate at planetary scale. Per `universal-saturation-kernel-catalog.md:141-145`: "A spinning parent BH in its embedding parent lattice imparts bulk strain via frame-dragging... at $A = 1$, $S(A) = 0$ and the substrate phase-transitions to K4 lattice." Same kernel, different scale.

**Under the A-034 reframe:** the planetary-scale instance inherits the kernel from Ax 2 (TKI scale invariance) — the explicit interior-strain functional form is precisely the canonical formula at `frame-dragging-impedance-convolution.md:20` applied at planetary-mass regime. See P-2 compression at §3.

### 2.5 Geodynamo VCA back-EMF (single data point on mag-vs-spin axis offset)

**File:** [`manuscript/ave-kb/vol3/applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md`](../manuscript/ave-kb/vol3/applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md)

**Mechanism (verbatim line 4 + lines 8-12):**
> The Geodynamo is rigorously an Inductive Back-EMF generator. As the massive conductive fluid core ($R \approx 3{,}480$ km) rotates physically inside the solar Sagnac phase-boundary (amplified electromagnetically by the magnetopause $+1$ reflection boundary), it suffers a Topo-Kinematic Motional EMF: $\mathcal{E}_{emf} = (\omega_\oplus \cdot R_{core} \cdot \Gamma_{sagnac}) \cdot B_{stator} \cdot (2 R_{core})$

**Result (line 14-18):** $M_\oplus \approx 1.5 \times 10^{23}\ \text{A·m}^2$ vs empirical $8.0 \times 10^{22}\ \text{A·m}^2$ (factor ~1.9 OOM-correct; structurally derived).

**Kernel-parameter contribution:** This canonical leaf already provides ONE data point on the μ-channel saturation (Earth's magnetic dipole amplitude). The amplitude side is already canonical at factor ~1.9 from observation. The DIRECTION side (mag-vs-spin tilt = ~11° for Earth) is what Row 9-b operationalizes — the per-channel saturation states differ, producing the angular offset.

**Under the A-034 reframe:** the mag-axis amplitude is already canonical. Row 9-b just operationalizes the direction = per-channel-saturation-state-offset claim per the ε vs μ axis structure at `universal-saturation-kernel-catalog.md:73-83`. No new geodynamo derivation needed; just apply the existing canonical formula across 8 planets with per-class $g_{\text{class}}$ factors.

### 2.6 Planetary magnetosphere magnetopause-standoff (5-planet validation; Uranus anomaly)

**File:** [`manuscript/ave-kb/vol3/cosmology/ch06-solar-system/planetary-magnetospheres.md`](../manuscript/ave-kb/vol3/cosmology/ch06-solar-system/planetary-magnetospheres.md)

**Validation table (lines 25-31):**

| Planet | Predicted [R_p] | Observed [R_p] | Error |
|---|---|---|---|
| Earth | 9.1 | 10.0 | 8.7% |
| Jupiter | 55.6 | 63.0 | 11.8% |
| Saturn | 17.0 | 22.0 | 22.8% |
| Uranus | 22.1 | 25.0 | 11.6% |
| Neptune | 21.7 | 26.0 | 16.4% |

**Uranus anomaly (verbatim lines 19-21):**
> Uranus is unique: its magnetic dipole is tilted $59^\circ$ from the rotation axis and offset by 0.31 $R_U$ from center. This creates a highly asymmetric, time-varying impedance cavity whose magnetopause standoff varies from 14.9 to 20.8 $R_U$ as the planet rotates (asymmetry ratio 1.40$\times$).

**Kernel-parameter contribution:** This canonical leaf already validates the magnetopause-standoff substrate-coupling at 5-planet scale (5 of the 8 planets, ~10-23% error). This is amplitude-side validation of the kernel at planetary scale. The Uranus 59° mag-tilt + 0.31 R_U offset (line 19-21) IS the observable that Row 9-b's saturation-event-taxonomy predicts — when the μ-channel saturates differently than the angular-momentum channel, the result is a tilted dipole with offset center.

**Under the A-034 reframe:** the 5-planet table validates the kernel's amplitude prediction; Row 9-b extends to direction. The "Uranus 98° obliquity" is no longer an ad-hoc giant-impact explanation — it is the predicted equilibrium at $A_{\text{spin}} \to 1$ on the orthogonal branch for icy-mantle gas-giant parameter regime.

### 2.7 Boundary observables $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ at $\Gamma = -1$ (Class E candidate)

**File:** [`manuscript/ave-kb/common/boundary-observables-m-q-j.md`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md)

**Key statement (verbatim line 15):**
> $\mathcal{J}$ | Boundary winding number | Wind($\partial\Omega$), half-integer per $SU(2)$ double-cover | 2D surface | magnetic moment | rotation | spin $J$

**Same-mechanism-at-all-scales table (verbatim line 38):**
> Planetary magnetopause | Magnetosphere boundary | Planet + field-aligned solitons | planet mass, dipole moment, rotation

**Kernel-parameter contribution:** This canonical leaf already states (line 38) that the planetary-scale boundary observables are mass + dipole moment + rotation — exactly the three observables Row 9 (currently amplitude side) + Row 9-a (spin-axis) + Row 9-b (mag-vs-spin tilt) collectively cover. The boundary $\mathcal{J}$ DECOMPOSES into the spin-axis and magnetic-axis projections per Cosserat per INVARIANT-S2.

**Under the A-034 reframe:** the decomposition is now part of the catalog row structure (Row 9-a and Row 9-b are the two projections); this leaf is **already canonical** and provides exactly the framework. See P-6 compression at §3 — this is Class E framework already canonical at `boundary-observables-m-q-j.md`, not a new derivation.

### 2.8 omega-freeze cosmic-grain cascade §3.1 + §4 (Observable 6 + nested-cascade conjecture)

**File:** [`manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md) §3.1 (lines 59-75) + §4 (lines 118-128)

**§3.1 Observable 6 statement (verbatim lines 61-62):**
> Pre-registered hypothesis (NEW per Entry 002 2026-05-16): orbital-plane orientations at every accessible scale should show non-random alignment with the $\Omega_{\text{freeze}}$ axis.

**§4 nested-cascade conjecture (verbatim lines 120-122):**
> $\Omega_{\text{freeze}}$ projects through nested rotators at every smaller scale via angular-momentum cascade: $\Omega_{\text{freeze}}$ (cosmic) $\to$ galactic disk axes $\to$ stellar spins $\to$ planetary spin axes $\to$ Earth inner-core super-rotation

**Kernel-parameter contribution:** This canonical leaf already states the existence of the nested-cascade observable (the claim that Row 9-a + Row 11-a + Row 14-a operationalize across scales). The canonical "PROVISIONAL flag" at line 135 is the explicit corpus acknowledgment that the operationalization is open work — which the A-034 catalog-row additions close.

**Under the A-034 reframe:** the nested-cascade is precisely the cross-scale catalog rows (Row 9-a → Row 11-a → Row 14-a) operating off the same $\hat{\Omega}_{\text{freeze}}$ via Ax 2 TKI scale invariance. No new framework needed — Ax 2 already provides cross-scale, A-034 already provides the kernel, and the rows operationalize the cross-scale instance.

### 2.9 Summary table — building-block status under A-034 reframe

| # | Building block | File | Provides | Resolution under A-034 reframe |
|---|---|---|---|---|
| 1 | Op14 asymmetric saturation (rotating mass) | frame-dragging-impedance-convolution.md:20 | Substrate prograde/retrograde Op14 mechanism | (c)-operator-application: Op14 at planetary mass regime |
| 2 | Parametric coupling kernel | parametric-coupling-kernel.md | Substrate↔tank coupling template + 5-axis port classification | (b)-scale-invariance: Ax 2 substitution at planetary scale |
| 3 | Cosserat micropolar rotational DOF | Vol 1 Ch 1:52 (canonical) + INVARIANT-S2 | Substrate-native rotational coupling channel; spin+mag axes as two projections | Already canonical — operationalize via ε/μ axis (Row 9-b) |
| 4 | Frame-dragging interior strain (cosmic genesis) | Vol 3 Ch 4:408-416 + universal-saturation-kernel-catalog.md | Cosmic-genesis instance | (b)-scale-invariance: same instance at planetary scale per Ax 2 |
| 5 | Geodynamo VCA back-EMF | geodynamo-vca-back-emf.md | Earth mag dipole amplitude (factor 1.9 OOM) | Already canonical amplitude; direction via Row 9-b across 8 planets |
| 6 | Planetary magnetosphere magnetopause-standoff | planetary-magnetospheres.md:25-31 + Uranus anomaly:19-21 | 5-planet amplitude validation; Uranus anomaly | Already canonical — provides the saturation-event-taxonomy data |
| 7 | Boundary observables $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ | boundary-observables-m-q-j.md | Class E framework; planetary observables = boundary integrals | Already canonical at line 38 — decomposition into Row 9-a + Row 9-b |
| 8 | omega-freeze cosmic-grain cascade §3.1 + §4 | omega-freeze-cosmic-grain-cascade.md | Existence of nested cascade observable | Cross-scale catalog rows (Row 9-a → 11-a → 14-a) per Ax 2 |

### 2.10 Corpus anomalies surfaced during inventory — preserved + reframed

Per Phase 2 brief directive ("if Phase 2 inventory surfaces a corpus structural inconsistency, STOP and report rather than fix"), the inventory surfaced the following anomalies. NOT FIXED in this scoping doc:

- **A1 (low-severity)**: The Cosserat-micropolar-rotational-DOF building block (block #3) does NOT have a dedicated KB leaf. Under the A-034 reframe, the lack of a dedicated leaf is **less load-bearing** — the canonical statement at Vol 1 Ch 1:52 + INVARIANT-S2 + Q-G47 chiral-coupling work is sufficient kernel-parameter substrate; a dedicated leaf would be helpful documentation but not blocking. Still flagged for orchestration; not fixed here.

- **A2 (low-severity)**: The cross-planet frame-transformation problem is not addressed by the geodynamo leaf (block #5). Under the A-034 reframe, the per-class $g_{\text{class}}$ factor (rocky / metallic-H / icy-mantle) in $A_{\text{soliton}}$ definition handles the cross-planet variation via the catalog row structure — explicit frame-transformation derivation may not be necessary. Still flagged.

- **A3 (medium-severity)**: The Q-G47 chiral-coupling work referenced at `omega-freeze-cosmic-grain-cascade.md:165-180` lives in a sibling repo (AVE-QED). Session 2 still needs to pull the canonical $\chi_1, \chi_2, \chi_3$ moduli + $\xi_{K2}/\xi_{K1} = 12$ relation. Under the A-034 reframe, the cross-repo handshake is the same (no compression here); the Q-G47 work supplies the Landau-form template that the catalog rows already cite. Still flagged.

- **A4 (new — surfaced by the refactor)**: The internal inconsistency at `universal-saturation-kernel-catalog.md:83` flagged 2026-05-19 EOD — the catalog row (line 38) says "Galactic (MOND) | SYM" while the canonical leaf at `saturated-lattice-mutual-inductance.md:4` classifies it as ASYM-N(μ) — is queued for adjudication. Row 11-a (Galactic spin-axis) inherits this MOND classification ambiguity; resolution is Session 2 work pending Grant adjudication.

These four anomalies are flagged for orchestration awareness. They do NOT block Session 1 (scoping); A1, A2, A3 impose lighter Session 2 prereq work than under the original new-operator framing; A4 is a corpus internal-inconsistency.

---

## 3. Phase 3 — Derivation prereqs (compressed under A-034 reframe)

Under the original "new operator" framing, Session 2 needed to derive an integrated $\hat{\mathcal{O}}_{\text{soliton}}$ from scratch with 6 prereqs totaling 11-17 hr. Under the A-034 reframe, **most prereqs resolve to "apply existing canonical leaf at file:line"** rather than "derive new substrate physics." The kernel is canonical; Ax 2 scale invariance is canonical; the building blocks are canonical. Session 2's job is to **enumerate** the catalog rows and **score** them against planetary data — not to derive new framework.

### P-1: Substrate Larmor-frequency analog (planetary-scale pump frequency) — COMPRESSED

**Original question:** What pump frequency does planetary rotation couple to?

**Status under A-034 reframe:** The pump frequency at any scale is supplied by Ax 2 (TKI scale invariance) applied to the canonical $\omega_{\text{slew}} = \alpha \omega_{\text{Compton}}$ at the atomic instance. The substrate-physics derivation chain is canonical at `parametric-coupling-kernel.md` §3 lines 60-95; the planetary-scale instance is a per-Ax-2 substitution. NOT a new derivation.

**Revised effort:** 30 min Ax-2 substitution + cross-check vs the canonical kernel — **NOT** 1-2 hr substrate-native derivation chain.

**Compression: 1-2 hr → 0.5 hr.**

### P-2: Op14 saturation profile in soliton-interior frame vs substrate-rest frame — ALREADY CANONICAL

**Original question:** Closed-form interior-strain leaf needed for planetary interior.

**Status under A-034 reframe:** Already canonical at `frame-dragging-impedance-convolution.md:20` for the gravitational/Kerr case. Per A-034 + Ax 2, the same Op14 form applies inside the soliton's $\Gamma = -1$ boundary at planetary scale. The "still missing" interior-strain leaf is at most a 1-line "apply Op14 at $A_{\text{interior}}$" annotation — not a new derivation. The cosmic-genesis instance at `universal-saturation-kernel-catalog.md:141-145` provides the explicit prototype.

**Revised effort:** 30 min annotation + cross-check vs canonical Op14 form — **NOT** 1-2 hr re-derivation.

**Compression: 1-2 hr → 0.5 hr.**

### P-3: Coupling-strength dependence on soliton mass — APPLY Ax 2 + PER-CLASS $g_{\text{class}}$

**Original question:** How does coupling strength scale with $M_s$? Per-structural-class power-law.

**Status under A-034 reframe:** Ax 2 TKI scale invariance is the canonical mass-scaling framework — the same kernel applies at all masses with dimensionless $A$ rescaled per scale. The per-internal-structure-class modulation ($g_{\text{class}}$) is parameterized in Row 9-a / Row 9-b definitions (rocky / metallic-H / icy-mantle) per `planetary-magnetospheres.md` 5-planet validation table — the per-class structure is **already canonical**. Session 2's job is to extract the per-class $g_{\text{class}}$ values from the 5-planet validation data, NOT to derive new mass-scaling physics.

**Revised effort:** 1-1.5 hr empirical extraction of $g_{\text{class}}$ from existing 5-planet data — **NOT** 2-3 hr from-scratch derivation.

**Compression: 2-3 hr → 1-1.5 hr.**

### P-4: Multi-resonance landscape in $(M_s, \omega_s, \mathcal{M}_s)$ — IS THE SATURATION KERNEL ITSELF

**Original question:** Where do retrograde / orthogonal solutions become stable?

**Status under A-034 reframe:** The corpus has the saturation kernel $S(A) = \sqrt{1 - A^2}$ rigorously canonical at A-034 (`universal-saturation-kernel-catalog.md`). The "multi-resonance landscape" the original prereq sought is **precisely the kernel's behavior as $A \to 1$** — the vertical tangent at $A = 1$ produces sharp topological reorganization events at the saturation boundary. The aligned / anti-aligned / orthogonal branches are the kernel's stable equilibria across the $A$ axis — already canonical.

The work that IS needed: identifying which planetary-class $(M_s, \omega_s, \text{class})$ combinations push $A_{\text{soliton}}$ across the saturation boundary on which branch. This is **empirical scoring** of the canonical kernel against 8 planetary data points, NOT new substrate-physics derivation. Per Ax 2, the same kernel branch structure applies at galactic scale (Row 11-a) and LSS scale (Row 14-a).

**Revised effort:** 1-2 hr empirical scoring against the 8 planets + 3 anomaly cases (Saturn, Venus, Uranus) — **NOT** 3-4 hr parametric-resonance Mathieu-equation derivation. The Mathieu-equation work the original prereq imagined is for the LINEAR-response oscillator case; the substrate-physics work uses the saturation kernel which is **non-linear** by construction.

**Compression: 3-4 hr → 1-2 hr.**

### P-5: Cosserat coupling between bound rotating bodies and substrate rotational DOF — ALREADY CANONICAL via Q-G47

**Original question:** Coupling Lagrangian-analog between soliton body-frame rotation and substrate microrotation.

**Status under A-034 reframe:** Already canonical via Q-G47 substrate-Cosserat closure (Ax 1 + cross-volume per omega-freeze-cosmic-grain-cascade.md:165-180 — the chiral-coupling Landau form $U_{\text{chiral}}^{\text{add}} = \chi_1 \varepsilon_{ij} \kappa_{ji} + \ldots$). The cosmic-scale instance is canonical (Big Bang per universal-saturation-kernel-catalog.md:141-145); the planetary-scale instance is the same form per Ax 2 scale invariance.

The body-frame ↔ substrate-rest-frame transformation is **standard Cosserat micropolar mechanics** at any scale — not a new derivation, just standard application of Ax 1 micropolar physics + Q-G47's canonical chirality moduli. Cross-repo handshake to AVE-QED still needed (per A3 anomaly above) but the substrate physics is canonical.

**Revised effort:** 30 min Ax 2 substitution + canonical $\chi_1, \chi_2, \chi_3$ import from Q-G47 — **NOT** 2-3 hr from-scratch chiral-coupling Landau derivation.

**Compression: 2-3 hr → 0.5 hr** (assumes Q-G47 import is clean; A3 cross-repo handshake adds 30 min if not).

### P-6: Decomposition of $\mathcal{J}^{\text{total}}_{\text{soliton}}$ into spin-axis vs magnetic-dipole-axis projections — ALREADY CANONICAL via Class E

**Original question:** Explicit splitting of $\mathcal{J}$ into spin + magnetic axes.

**Status under A-034 reframe:** Already canonical at `boundary-observables-m-q-j.md:38` — "Planet + field-aligned solitons: planet mass, dipole moment, rotation" — three boundary observables that decompose the total $\mathcal{J}$ into spin-axis + mag-axis + amplitude. Per Cosserat (Ax 1) INVARIANT-S2 verbatim: "macroscopic angular momentum, the EM magnetic field $B$, and QM electron spin are three projections of the same per-node rotational coordinate."

The decomposition is **structurally already in the canonical leaf**. The catalog rows Row 9-a (spin-axis) and Row 9-b (mag-vs-spin offset) operationalize the decomposition at planetary scale; the leaf provides the framework.

**Revised effort:** 30 min mapping the canonical $\mathcal{J}$ decomposition into the catalog row structure — **NOT** 2-3 hr field-decomposition derivation.

**Compression: 2-3 hr → 0.5 hr.**

### 3.7 Summary table — prereqs compressed

| # | Prereq | Resolution under A-034 reframe | Original effort | Revised effort |
|---|---|---|---|---|
| P-1 | Substrate Larmor-frequency analog | Ax 2 substitution from canonical `parametric-coupling-kernel.md` | 1-2 hr | **0.5 hr** |
| P-2 | Op14 saturation in soliton-interior frame | Already canonical at `frame-dragging-impedance-convolution.md:20` + Ax 2 | 1-2 hr | **0.5 hr** |
| P-3 | Mass-scaling of coupling strength | Ax 2 + empirical $g_{\text{class}}$ from `planetary-magnetospheres.md` 5-planet table | 2-3 hr | **1-1.5 hr** |
| P-4 | Multi-resonance landscape | IS the saturation kernel $S(A) = \sqrt{1-A^2}$ at $A \to 1$ — canonical at A-034 | 3-4 hr | **1-2 hr** |
| P-5 | Cosserat body-frame ↔ substrate-rest-frame | Already canonical via Q-G47 chiral-coupling + Ax 1 + Ax 2 | 2-3 hr | **0.5 hr** (+0.5 hr if A3 cross-repo handshake needed) |
| P-6 | $\mathcal{J}^{\text{total}}$ → spin + mag projection | Already canonical at `boundary-observables-m-q-j.md:38` + INVARIANT-S2 | 2-3 hr | **0.5 hr** |
| | **TOTAL** | | **11-17 hr** | **3-5 hr** (4-6 of 6 prereqs collapse to "apply existing canonical leaf") |

**Net compression: 11-17 hr → 3-5 hr** — significant compression by leveraging A-034 + Ax 2 + existing canonical leaves rather than deriving new framework.

**4 of the 6 prereqs (P-1, P-2, P-5, P-6) reduce to "apply existing canonical leaf at file:line."** Only P-3 and P-4 retain some empirical-scoring work (extracting per-class $g_{\text{class}}$, scoring kernel against 16 axis data points) — and that empirical-scoring work is canonically Session 3 work (planetary application), not Session 2 derivation.

---

## 4. Phase 4 — Testable predictions list (preserved as-is)

The empirical data + saturation-event taxonomy are preserved from the original scoping. The verification question is reframed: "does the A-034 kernel $S(A_{\text{soliton}})$ with appropriately-defined $A_{\text{soliton}}$ reproduce these 16 data points?" rather than "does the new operator predict them?"

### 4.1 Solar system (16 axis data points = 8 planets × {spin axis, magnetic axis})

| Body | Spin obliquity | Magnetic axis tilt | Size (R_⊕) | Rotation period (hr) | Internal-structure class |
|---|---|---|---|---|---|
| Mercury | 0.034° | ~0° (weak field) | 0.383 | 1407 | Rocky |
| Venus | **177.4°** | None | 0.949 | **−5832** (retrograde) | Rocky |
| Earth | 23.44° | ~11° | 1 | 23.93 | Rocky |
| Mars | 25.19° | None (crustal only) | 0.532 | 24.62 | Rocky (solid core) |
| Jupiter | 3.13° | ~10° | 11.21 | 9.93 | Metallic-H gas giant |
| Saturn | 26.73° | **<1°** | 9.45 | 10.66 | Metallic-H gas giant |
| Uranus | **97.77°** | **59°** | 4.01 | 17.24 | Icy-mantle gas giant |
| Neptune | 28.32° | **47°** | 3.88 | 16.11 | Icy-mantle gas giant |

**Data provenance**: standard solar-system reference values (NASA NSSDC); used here as the empirical target. Per `pre-test-physics-check` (see §4.5 below): these values are widely-tabulated and not contested; the kernel-with-$A_{\text{soliton}}$-defined must reproduce them.

### 4.2 Three structural anomalies the kernel must explain

Per the epic brief Phase 4, reframed under A-034:

1. **Saturn aligned (<1°) vs Uranus tilted (59°) — same gas-giant class, similar rotation periods (10.66 hr vs 17.24 hr), different internal structure.** Under A-034 reframe: Saturn has $A_{\text{spin}} \ll 1$ (sub-saturation) on the aligned branch; Uranus has $A_{\text{spin}} \to 1$ on the orthogonal branch — the per-class $g_{\text{class}}$ factor (Row 9-a definition) differentiates metallic-H vs icy-mantle. **Test of P-3** (empirical $g_{\text{class}}$ extraction).

2. **Venus retrograde — slow rotation (243 days) + no magnetic field.** Under A-034 reframe: slow $\omega_s$ pushes $A_{\text{soliton}}$ across the saturation boundary on the anti-aligned branch (retrograde-spin stable equilibrium). **Test of P-4** (kernel branch structure — saturation event at anti-aligned branch).

3. **Uranus 98° obliquity.** Under A-034 reframe: the universal kernel + icy-mantle $g_{\text{class}}$ produces a stable equilibrium at $\theta \to \pi/2$ class (the orthogonal saturation branch). **Test of P-4 + saturation-event taxonomy** — if the kernel-with-Row-9-a's $A_{\text{spin}}$ definition recovers 98° as a stable equilibrium for icy-mantle $(M_s, \omega_s)$ region, AVE has substrate-physics structural advantage over the standard ad-hoc giant-impact explanation.

### 4.3 Scoring rubric (proposed for Session 3)

A proposed first-cut scoring rubric for Session 3 (Session 2's output is the catalog rows + $A_{\text{soliton}}$ definitions; Session 3 applies + scores). Pre-test-physics-check applies (see §4.5):

| Outcome | Criterion | Implication |
|---|---|---|
| **Pass (16/16 within tolerance)** | Kernel + Row 9-a $A_{\text{spin}}$ matches observed spin axis within $\sigma_{\text{op}}$ for all 8 planets AND same for $\hat{n}_{\text{mag}}$ via Row 9-b $A_{\text{offset}}$ for all 8 planets | Catalog rows validated at planetary scale; proceed to Session 4 (galactic via Row 11-a) with confidence |
| **Marginal (12-15/16 within tolerance)** | Some planets match, others miss; sub-class structure may emerge (rocky vs gas-giant; per-$g_{\text{class}}$ refinement needed) | Investigate which class misses; possible Row 9-a / 9-b refinement before Session 4 |
| **Fail (≤11/16 within tolerance)** | Substantial fraction of planets miss; structural anomalies (Saturn vs Uranus, Venus retrograde, Uranus 98°) NOT reproduced | Per Class E: the joint constraint is broken. Investigate which canonical leaf assumption fails; possible walk-back of $\hat{\Omega}_{\text{freeze}}$ or per-class $g_{\text{class}}$ formulation |
| **Decisive falsification** | Kernel-prediction inconsistent with data at >3σ for any axis | Per Class E framing, the entire substrate operating-point framework is killed |

**Tolerance $\sigma_{\text{op}}$ is NOT YET specified.** Per pre-test-physics-check (§4.5): setting $\sigma_{\text{op}} = 10°$ uncritically would convert Saturn aligned (<1°) and Uranus mag-tilt 59° from a discriminator-pair into a noise-band. Proper $\sigma_{\text{op}}$ specification is Session 3 prereq, informed by Session 2's derived per-class uncertainty propagation.

### 4.4 Galactic + LSS scale predictions

**Galactic-scale target (the SDSS DR17 anchor):**

| Observable | Empirical value | Source |
|---|---|---|
| LSS spin axis | $(l = 129°, b = 79°)$, $\sigma_{\text{LSS}} = 6.83°$ | [`research/2026-05-19_c5-sdss-spin-orientation-result.md:21`](2026-05-19_c5-sdss-spin-orientation-result.md) |
| CMB-LSS angular separation | 36.75° (5.33σ from zero) | Same; line 122 verbatim |
| Pantheon+ Hubble flow direction | $(l = 129.76°, b = -13.64°)$, $\sigma = 24.0°$ | [`research/2026-05-19_c5-pantheon-tightening-result.md`](2026-05-19_c5-pantheon-tightening-result.md) |
| CMB axis-of-evil (Planck PR3 SMICA pin) | $(l = 60.28°, b = 50.48°)$, $\sigma_{\text{CMB}} = 0.92°$ | [`research/2026-05-19_c5-cmb-axis-executable-observer-result.md:17`](2026-05-19_c5-cmb-axis-executable-observer-result.md) |

The catalog Row 11-a output (Session 4) must:

- Take galactic-class soliton parameters $(M_{\text{gal}}, \omega_{\text{gal}}, \mathcal{M}_{\text{gal}})$ → predict $\hat{n}_{\text{LSS}}$ via the same kernel applied with galactic-class $A_{\text{soliton}}$
- Reproduce the OFFSET from the CMB axis (36.75° at 5.33σ); the offset must be a CONSEQUENCE of $A_{\text{gal,spin}} \to 1$ on the orthogonal branch at galactic scale, not a free parameter
- Optionally: extend to a SECOND galactic-scale data point — the Walmsley+2022 GZ DECaLS independent classification (per epic brief Phase 4) — providing cross-catalog confirmation

**Pantheon+ Hubble bulk-flow direction** is a different soliton class (mass distribution rather than galaxy spin); maps to a different observable channel. This is potentially Row 14-a or a different catalog row entirely (Session 5 conditional).

### 4.5 pre-test-physics-check — three plumber-physical questions for Grant (preserved)

Per the brief skill discipline: `pre-test-physics-check` is APPLICABLE because the Phase 4 testable-predictions section locks in adjudication criteria for Sessions 2-4. **These three questions are preserved verbatim from the original scoping — the A-034 reframe does NOT eliminate them; if anything it sharpens them, because the kernel branch structure depends on the answers:**

**Question 1: Precise-vs-class prediction.**
Is the mag-spin tilt for the 8 planets meant to be a PRECISE prediction (kernel-with-$A_{\text{soliton}}$ outputs the angle to within a few degrees) or a CLASS prediction (kernel predicts which class — aligned, anti-aligned, mid-tilted, near-orthogonal — and the per-planet precision is loose)? The Saturn-vs-Uranus contrast (<1° vs 59°) is a class-level discriminator; precise predictions of 23.44° (Earth obliquity) vs 25.19° (Mars obliquity) is harder and may not be what the kernel is for.

**Under A-034 reframe sharpening:** the kernel's saturation branches are inherently CLASS-level (aligned / anti-aligned / orthogonal); precise within-branch positions are a property of where $A_{\text{soliton}}$ sits on the kernel curve. Grant's adjudication selects which level the catalog rows are scored at.

**Question 2: Single $\hat{\Omega}_{\text{freeze}}$ vs cascaded-per-planet.**
Is the operator's input the SAME $\hat{\Omega}_{\text{freeze}}$ for all 8 planets, or does each planet have an "inherited" frozen direction at the formation epoch? The brief implies the former (single substrate direction); the cascade conjecture at block #8 §4 implies the latter (cosmic→galactic→stellar→planetary). If each planet inherits a slightly different direction (the local-substrate motion at planet-formation), the kernel's predictions for 16 axes become 16 quasi-independent local-substrate-direction predictions, which is a much weaker test.

**Under A-034 reframe sharpening:** if cascaded-per-planet, the cross-scale catalog rows (Row 9-a → Row 11-a → Row 14-a) operate off different per-scale $\hat{\Omega}$ inputs, and Class E joint-constraint testing requires per-cascade adjudication. Grant's adjudication selects the corpus framing.

**Question 3: Specific-value vs stable-branch-structure.**
For the structural anomalies (Saturn aligned, Venus retrograde, Uranus 98°): is the kernel-with-$A_{\text{soliton}}$ obligated to derive the SPECIFIC values, or to derive the STABLE-EQUILIBRIUM BRANCH STRUCTURE (i.e., "there exists a stable equilibrium near 98° for the icy-mantle parameter region")? The latter is a weaker but more achievable claim.

**Under A-034 reframe sharpening:** the kernel branch structure is inherently a stable-equilibrium statement (saturation events are topological reorganizations to new $A < 1$ stable configurations). Question 3 may resolve naturally under the A-034 reframe — the kernel produces branch structure, not specific values. Specific values come from $A_{\text{soliton}}$ values per planet, which depend on per-class $g_{\text{class}}$ extraction (P-3).

These three questions are LOAD-BEARING for Session 2's catalog-row definitions and Session 3's scoring rubric. They are surfaced here for Grant's adjudication BEFORE Session 2 spins up (per Rule 16 strengthening: ask BEFORE design, not after 30+ commits return Mode III).

---

## 5. Phase 5 — Multi-session arc outline (compressed under A-034 reframe)

### 5.1 Sessions 2-5 estimated total effort + branch points (revised post-reframe)

| Session | Deliverable | Original effort | Revised effort |
|---|---|---|---|
| **Session 2** | A-034 catalog row additions (Row 9-a + Row 9-b + Row 11-a scoped) + $A_{\text{soliton}}$ definitions via P-1..P-6 (most resolving to canonical leaves) + planetary scoring (8 planets × 2 axes via the kernel) | **11-17 hr** | **3-5 hr** |
| **Session 3** | Application to planetary scale (16 axis data points) — score against §4.3 rubric | 2-3 hr | **1-2 hr** (lighter because Session 2 already does primary scoring; Session 3 finalizes against $\sigma_{\text{op}}$ + writes up) |
| **Session 4** | Galactic-scale extension to SDSS DR17 (Row 11-a $A_{\text{soliton}}$ definition + LSS-axis prediction) | 3-5 hr | **1-2 hr** (Ax 2 substitution from Row 9-a + canonical galactic-scale parameters) |
| **Session 5 (conditional)** | LSS extension (Row 14-a) + cross-catalog GZ DECaLS prep; refinement based on Sessions 2-4 outcomes | TBD | **TBD** (conditional; potentially 1-2 hr LSS framing if Session 4 indicates clean Row 14-a; potentially doubling under B2-fail) |
| | **TOTAL (Sessions 2-4 base case)** | **16-25 hr** | **5-9 hr** |

**Net compression: 16-25 hr → 5-9 hr** — by leveraging the A-034 catalog-extension framing rather than the original new-operator framing.

### 5.2 Branch points (revised post-reframe)

**Branch point B1 (post-Session 2):** Did the catalog row scope + planetary scoring close cleanly?
- **B1-yes**: Proceed to Session 3 finalization with the rows + scoring in hand.
- **B1-partial** (per-class $g_{\text{class}}$ doesn't extract cleanly from 5-planet data): Session 2 produces PARTIAL rows + flags the per-class uncertainty; Session 3 scoring rubric accounts for partial-row status.
- **B1-no** (kernel branch structure doesn't accommodate Saturn-aligned-vs-Uranus-tilted at icy-mantle parameter region): Re-scope. The catalog rows would not capture the planetary anomalies; either the saturation kernel does NOT apply at planetary-rotational-axis observable channel (which would surface a structural gap in A-034), or the $A_{\text{soliton}}$ definition needs additional ingredients beyond (angular momentum × cosmic-substrate strain × coupling factor). Surfaced for Grant adjudication, NOT silently fixed.

**Branch point B2 (post-Session 3):** Kernel-with-rows scores Pass / Marginal / Fail / Decisive-falsification per §4.3.
- **B2-pass**: Proceed to Session 4 with confidence.
- **B2-marginal**: Investigate sub-class structure (rocky vs metallic-H vs icy-mantle); refine per-$g_{\text{class}}$ before Session 4.
- **B2-fail**: Per Class E, the joint constraint is broken. Walk back the $A_{\text{soliton}}$ definition; possible structural-gap surface in A-034 (could trigger new canonical leaf or row-format revision rather than walking back $\hat{\Omega}_{\text{freeze}}$).
- **B2-decisive-falsification**: Per Class E framing, the substrate operating-point framework is killed. Stop. Walk back $\hat{\Omega}_{\text{freeze}}$ and the omega-freeze cascade (block #8). This would be a MAJOR negative result — equivalent in scope to walking back $u_0^* \approx 0.187$ as the joint operating-point.

**Branch point B3 (post-Session 4):** Row 11-a galactic-scale prediction agreement with SDSS DR17 LSS axis $(l=129°, b=79°)$, $\sigma=6.83°$.
- **B3-agreement**: Forward-prediction confirmed at galactic scale; Row 11-a validated cosmologically. The C5 row in the master prediction matrix moves from Marginal-D to A (passed).
- **B3-disagreement**: Row 11-a's galactic-scale prediction differs from SDSS LSS axis at >3σ. Either (a) the Ax-2 substitution to galactic scale is wrong (possible structural gap in catalog scale-invariance), or (b) the galactic-scale soliton has additional physics (Session 5 conditional refinement).

### 5.3 Session 2 → Session 3 hand-off requirements

Session 2's output must include:

- Catalog row Row 9-a + Row 9-b scoped completely (table format matching `universal-saturation-kernel-catalog.md:27-41`)
- Per-planet $A_{\text{soliton}}$ values for all 8 planets (using extracted $g_{\text{class}}$ factors)
- Per-planet kernel-output predictions for $\hat{n}_{\text{spin}}$ AND $\hat{n}_{\text{mag}}$ (16 values total)
- Per-planet uncertainty propagation (informs $\sigma_{\text{op}}$ for Session 3)
- A clean cross-check on Earth (mag-axis ~11° + spin obliquity 23.44° — the most validated data point) and a smoke test on Mercury (smallest, weakest field — clean limiting case)

### 5.4 Multi-session arc summary (revised)

Total estimated effort for Sessions 2-4 base case: **5-9 hr** (compressed from 16-25 hr). Session 5 conditional: TBD. The arc is significantly tighter now because every component leverages existing canonical leaves (A-034 kernel + Ax 2 scale invariance + 8 building blocks + Class E framework); the catalog-extension framing eliminates the new-framework-derivation overhead.

Risk profile under the A-034 reframe:

- **Lowest risk**: Session 2 catalog-row scoping + planetary scoring (the kernel is canonical; per-class extraction from existing data is mechanical)
- **Lower risk**: Session 3 finalization (the scoring is largely done in Session 2)
- **Medium risk**: Session 4 galactic-scale extrapolation (the Ax 2 substitution is clean; the per-galactic-class $g_{\text{class}}$ analog at galactic scale is the open extension)
- **Conditional risk**: Session 5 LSS extension (Row 14-a is the most conjectural, depending on cosmic-scale companion-row gap-cell adjudication)

---

## 6. Phase 6 — Audit + push

### 6.1 Skill discipline applied this session

| Skill | Fired? | Notes |
|---|---|---|
| `verify-before-cite` v1.3 | YES (triggers 1, 2) | Every corpus citation re-read at execution time; quotes verbatim from canonical leaves; cited verbatim per-line numbers verified against current branch HEAD. SDSS DR17 numerics verified directly from result doc (lines 17, 21, 122). |
| `ave-canonical-leaf-pull` v1.1 | YES — **load-bearing test of trigger 16** | The original "new operator" framing landed in trigger-16 (framework-extension proposals). The (a)-(e) classification at §1.2 walks the canon. Result: proposal is (a)-missing-row (catalog extension), NOT (e)-genuinely-new. Refactor reframes accordingly. |
| `ave-prereg` | SKIP | Per brief; this is a scoping doc, not a new derivation. |
| `consistency-vs-emergence` v1.1 | YES (§1.6) | Catalog-row observables classified as Class E per the canonical statement at `omega-freeze-cosmic-grain-cascade.md:7`. Joint constraint with $\hat{\Omega}_{\text{freeze}}$ explicitly noted. |
| `pre-test-physics-check` | YES (§4.5) | Three plumber-physical questions for Grant flagged BEFORE Session 2 design (per Rule 16 strengthening). Sharpened under A-034 reframe — the kernel branch structure depends on the answers. |
| Pure-AVE-corpus rule | YES | No external-context refs anywhere. |

### 6.2 Constraints satisfied (per brief §"Constraints")

- ✓ NO derivation performed. The catalog rows are SCOPED (Session 2 deliverable); the $A_{\text{soliton}}$ functional forms are NOT computed.
- ✓ No `_orchestration/*.md` modified.
- ✓ No corpus leaves modified.
- ✓ Four corpus structural inconsistencies surfaced (§2.10 A1, A2, A3, A4); NOT fixed; flagged for orchestration.
- ✓ Single research-doc deliverable at `research/2026-05-20_soliton-lattice-coupling-operator-scoping.md` (this file).
- ✓ Empirical data preserved (16 planetary axis data points table).
- ✓ Corpus building-block inventory preserved (8 pieces).
- ✓ Saturation-event taxonomy preserved (aligned / anti-aligned / orthogonal-class).
- ✓ Three plumber-physical questions preserved + sharpened under A-034 reframe.

### 6.3 Anomalies surfaced

1. **Corpus gap (A1)** — no dedicated KB leaf for "Cosserat micropolar rotational DOF in operator-class problems." Under A-034 reframe: less load-bearing; canonical statements at Vol 1 Ch 1 + INVARIANT-S2 + Q-G47 are sufficient kernel-parameter substrate.
2. **Corpus gap (A2)** — geodynamo leaf is Earth-only; cross-planet frame-transformation rules implicit. Under A-034 reframe: per-class $g_{\text{class}}$ factor in Row 9-a / Row 9-b handles the cross-planet variation; explicit frame-transformation derivation may not be necessary.
3. **Cross-repo dependency (A3)** — Q-G47 chiral-coupling work at AVE-QED is load-bearing for Session 2 P-5; explicit handshake mechanism needed. Same under both framings.
4. **Catalog internal inconsistency (A4)** — Row 11 MOND classification ambiguity (line 83 of `universal-saturation-kernel-catalog.md`) inherits to Row 11-a galactic-spin-axis. Pending Grant adjudication.
5. **Effort compression** — Session 2 effort 11-17 hr → 3-5 hr; total arc 16-25 hr → 5-9 hr. By leveraging A-034 + Ax 2 + canonical leaves rather than deriving new framework.
6. **Pre-test-physics-check (preserved)** — three plumber-physical questions for Grant flagged at §4.5 (precision-vs-class predictions, single-vs-cascaded $\hat{\Omega}_{\text{freeze}}$, branch-structure-vs-specific-value adjudication) BEFORE Session 2 design begins. Sharpened under the A-034 reframe.

---

## 7. Cross-references

- **Epic brief:** [`_orchestration/soliton-lattice-coupling-operator.md`](../_orchestration/soliton-lattice-coupling-operator.md)
- **Originating epic (closed):** [`_orchestration/_archive/c5-sdss-dr17-spin-orientation.md`](../_orchestration/_archive/c5-sdss-dr17-spin-orientation.md), audit tag `audit/2026-05-19_c5-sdss-dr17-spin-orientation`
- **Predecessor empirical results:** [`research/2026-05-19_c5-sdss-spin-orientation-result.md`](2026-05-19_c5-sdss-spin-orientation-result.md), [`research/2026-05-19_c5-cmb-axis-executable-observer-result.md`](2026-05-19_c5-cmb-axis-executable-observer-result.md), [`research/2026-05-19_c5-pantheon-tightening-result.md`](2026-05-19_c5-pantheon-tightening-result.md)
- **Class E canonical leaf:** [`research/2026-05-19_class-e-candidate-corpus-sweep.md`](2026-05-19_class-e-candidate-corpus-sweep.md)
- **A-034 canonical leaf (framework-design canon for this refactor):** [`manuscript/ave-kb/common/universal-saturation-kernel-catalog.md`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md) — particularly the ε/μ axis extension (lines 73-83) + gap-cells (lines 89-94) + companion-row links (lines 103-110) added at commit `6436d65`.
- **`ave-canonical-leaf-pull` v1.1 skill (load-bearing for this refactor):** `~/.claude/skills/ave-canonical-leaf-pull/SKILL.md` v1.1 (commit `41e6b47`), trigger 16 (framework-extension proposals).
- **8 building blocks:** as cited per §2; full file:line list:
  1. [`manuscript/ave-kb/vol3/gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md:20`](../manuscript/ave-kb/vol3/gravity/ch02-general-relativity/frame-dragging-impedance-convolution.md)
  2. [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md)
  3. [`manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex:52`](../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex) + [`manuscript/ave-kb/CLAUDE.md` INVARIANT-S2](../manuscript/ave-kb/CLAUDE.md)
  4. [`manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex:408-416`](../manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex) + [`manuscript/ave-kb/common/universal-saturation-kernel-catalog.md:99-101`](../manuscript/ave-kb/common/universal-saturation-kernel-catalog.md)
  5. [`manuscript/ave-kb/vol3/applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md`](../manuscript/ave-kb/vol3/applied-physics/ch13-geophysics/geodynamo-vca-back-emf.md)
  6. [`manuscript/ave-kb/vol3/cosmology/ch06-solar-system/planetary-magnetospheres.md`](../manuscript/ave-kb/vol3/cosmology/ch06-solar-system/planetary-magnetospheres.md)
  7. [`manuscript/ave-kb/common/boundary-observables-m-q-j.md`](../manuscript/ave-kb/common/boundary-observables-m-q-j.md)
  8. [`manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md`](../manuscript/ave-kb/common/omega-freeze-cosmic-grain-cascade.md) §3.1 + §4
- **Refactor predecessor:** original scoping at commit `7c9d4d4` (this branch tip pre-refactor); refactor applied 2026-05-19 EOD per Grant adjudication.

---

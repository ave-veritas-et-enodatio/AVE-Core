# Q-G42 RESUME — Tree-Level V²-Coefficient SIGN Test: Phase-0 Result

**Status:** PHASE-0 COMPLETE (2026-06-03). Resume of `AVE-QED/docs/analysis/2026-05-13_Q-G42_v_yield_apparatus_scaling_prereg.md` §4 (Q1–Q3) under the reframe frozen in `research/2026-06-03_yield-knee-map-prereg.md` (grep-RESULT §). **Verdict: GO** — the V²-coefficient SIGN test is buildable and AVE-distinct at the **resonant-Q autoresonant** architecture (Method B); marginal at cryo-lock-in (optimistic geometry only); below floor at the precision-bridge.
**Lane:** implementer (experimental-protocol revamp).
**Calc script:** `src/scripts/vol_4_engineering/qg42_vsign_phase0.py` (all numbers below regenerate from it; constants from `ave.core.constants` only).
**Discipline applied:** `verify-before-cite` (every reuse citation re-checked to source this session) · `substrate-native-check` (Method-B framing is the Ax-4 varactor-bias mechanism, not an SM nonlinear-optics analogy) · `ave-fundamental-ground-up-implementation` (autoresonant number derived from canonical chain, not engineering-defaulted) · `ave-discrimination-check` (vacuum-vs-material separator) · `ave-canonical-source` (script imports `constants.py`) · `flag-don't-fix` (three contradictions surfaced, §6).

---

## 0. The reframe (settled — carried from the prereg, not re-litigated)

The literal saturation knee at V_yield is **bench-unreachable**: V_yield = 43.65 kV is the **per-node** voltage (across ℓ_node = 3.86×10⁻¹³ m), not per-apparatus. The best a bench reaches is a *local* saturation amplitude A ≈ few×10⁻³ at the field-concentration hot spot. So the bench measures the **small-A tree-level kernel**, not the knee. The recoverable AVE-distinct observable — and it is *cleaner* than the knee — is the **SIGN of the V² coefficient**:

| Framework | δε/ε₀ at small A | Sign | Physical |
|---|---|---|---|
| **AVE** | √(1−A²) − 1 ≈ −A²/2 | **negative** | vacuum **softens** (tree-level, Ax-4 kernel) |
| **QED (Euler–Heisenberg + Kerr)** | +(4α²/9)(E/E_S)² | **positive** | vacuum **stiffens** (one-loop) |

The two-sided binary (does the vacuum soften or stiffen under field?) discriminates **without** the knee or a magnitude match. The discrimination ratio is **8.381×10¹²** on the reflectance (V⁴) observable, **2.895×10⁶** on the resonance-shift (V², δε-linear) observable — both geometry-invariant, both arithmetically exact from `constants.py` (re-verified this session; matches IVIM adversarial doc 2026-06-03).

---

## 1. THE AUTORESONANT Δf₀/f₀ SMALL-SIGNAL NUMBER (deliverable 1 — the green-field gap)

Ch 15 treats the PLL only as a *rupture-driver* (ring-up toward V_snap); it carries **no** small-signal bulk-resonator Δf₀/f₀ number. This is the gap. Derived ground-up from `constants.py`:

### 1.1 The chain (substrate-native: Ax-4 varactor-bias of the bond-LC tank)

1. **Local kernel** (Ax-4, exact): δε/ε₀ = S(A) − 1 = √(1−A²) − 1. Negative for all 0 < A < 1.
2. **Local hot-spot amplitude:** A_hot = Q_build · β · V_app / (d_gap · E_YIELD), with E_YIELD = V_YIELD/ℓ_node = 1.130×10¹⁷ V/m (canonical).
3. **Saturated-volume-fraction dilution** (the load-bearing bulk factor). The hot spot fills a tiny fraction of the resonator. Away from it the tip-dipole field falls as E ∝ 1/r², so A² ∝ 1/r⁴ and δε ∝ 1/r⁴ — steeply localized (the 1/r⁴ integrand converges within a few feature-scales). The **bulk** eigenfrequency shift is the volume-weighted local shift:
   $$\langle \delta\varepsilon/\varepsilon_0\rangle_{\text{bulk}} = \frac{1}{V_{\text{res}}}\int \frac{\delta\varepsilon}{\varepsilon_0}\,dV = -\tfrac12 A_{\text{hot}}^2\,\eta_{\text{eff}},\qquad \eta_{\text{eff}} \equiv \frac{1}{V_{\text{res}}}\int \frac{A(r)^2}{A_{\text{hot}}^2}\,dV \sim \left(\frac{r_{\text{feat}}}{L_{\text{res}}}\right)^3.$$
   η_eff is the effective **field-filling fraction** — the geometry-dependent dilution. Bracketed over a defensible range (§4).
4. **Resonator relation:** for an LC resonator f₀ = 1/(2π√(LC)) with C ∝ ε, **Δf₀/f₀ = −½·⟨Δε/ε⟩_bulk**. Since ⟨Δε/ε⟩_bulk < 0 (softening), **Δf₀/f₀ > 0 — the resonance RISES** (the AVE-distinct sign at the bulk observable).
5. **Resonator-Q — the subtlety (see §6 flag-2):** Q does **not** multiply the signal Δf₀/f₀. Δf₀/f₀ is fixed entirely by ⟨Δε/ε⟩_bulk. Q sets the **minimum resolvable** fractional shift (≈ 1/(Q·SNR_loop), the line-Q / Allan-floor argument). The three architectures differ by their *resolvable-Δf₀/f₀ floor*, not by a signal gain.

### 1.2 The numbers (canonical bench: V=30 kV, d=1 mm, β=10³, Q_build=10⁴)

- **Local hot-spot:** A_hot = **2.654×10⁻³** (RMS), δε/ε₀ = **−3.52×10⁻⁶** (= A_hot²/2; PONDER ch1 quotes the **peak** A_peak = √2·A_hot ≈ 3.8×10⁻³ with peak (1−S) ≈ 7×10⁻⁶ — see §6 flag-1 [RESOLVED]: the factor is the √2 peak-vs-RMS convention, both on canonical E_YIELD = 1.130×10¹⁷ V/m, not a superseded E_yield).
- **Bulk Δf₀/f₀ (the headline gap-fill), per dilution bracket:**

| η_eff (field-filling) | geometry | ⟨δε/ε⟩_bulk | **Δf₀/f₀** |
|---|---|---|---|
| 10⁻⁶ | optimistic (r_feat/L_res ~ 10⁻²) | −3.52×10⁻¹² | **+1.76×10⁻¹²** |
| 10⁻⁹ | nominal (r_feat/L_res ~ 10⁻³) | −3.52×10⁻¹⁵ | **+1.76×10⁻¹⁵** |
| 10⁻¹² | conservative (r_feat/L_res ~ 10⁻⁴) | −3.52×10⁻¹⁸ | **+1.76×10⁻¹⁸** |

**This is the number Ch 15 lacks.** The bulk autoresonant signal sits at Δf₀/f₀ ≈ **10⁻¹² (optimistic) to 10⁻¹⁵ (nominal)**. It is **positive** (resonance rises) — the AVE-distinct sign.

### 1.3 Against the three Q-G42 §4-Q3 architectures

| Architecture | resolvable Δf₀/f₀ floor | SNR (nominal η=10⁻⁹) | SNR (optimistic η=10⁻⁶) | Verdict |
|---|---|---|---|---|
| precision-bridge | 10⁻⁹ | 1.76×10⁻⁶ | 1.76×10⁻³ | **below floor** |
| cryo-lock-in | 10⁻¹² | 1.76×10⁻³ | **1.76** | marginal (optimistic only) |
| resonant-Q | 10⁻¹⁵ | **1.76** | 1.76×10³ | **DETECT** |

The signal clears the floor at the **resonant-Q** architecture for the nominal geometry (SNR ≈ 1.8), and at **cryo-lock-in** only for the optimistic tight-resonator geometry (SNR ≈ 1.8). The precision-bridge is 3–6 OOM short — consistent with the prereg's expectation that the bridge is the *characterization* tool, not the *discovery* tool for the vacuum component.

---

## 2. VACUUM-vs-MATERIAL SEPARATION DESIGN (deliverable 2 — the load-bearing systematic)

`ave-discrimination-check`. A real dielectric's electrostriction / Kerr / material-saturation also shifts ε(E) — **either sign**, and often *larger* than the vacuum term. A raw Δf₀/f₀ cannot be attributed to the vacuum. The separator rests on **what is universal vs material-specific**:

| Property | Vacuum (AVE Ax-4) | Material (electrostriction/Kerr) |
|---|---|---|
| Coefficient | **fixed −½** (in A² = (E/E_YIELD)²); zero free parameters | material-specific, fitted, sign varies |
| E-scale | **E_YIELD = 1.130×10¹⁷ V/m** (universal, from constants.py) | material breakdown / Kerr scale (10⁸–10¹⁰ V/m) |
| Geometry dependence | enters **only** through the field map (A_hot, η_eff); coefficient invariant | bulk material property; tracks the *material* fill, not the field hot spot |
| Sign | **always negative** (softens), every geometry, every material | set by the material; not constrained |
| Temperature | **none** (substrate kernel) | strong (electrostriction, Kerr both T-dependent) |

### 2.1 The protocol (material/geometry variation isolating the universal component)

The vacuum term scales as A_hot² · η_eff = [β V/(d E_YIELD)]² · η_eff — it tracks the **field hot spot** with a **fixed coefficient and a fixed E-scale (E_YIELD)**. The material term tracks the **material's volume fill** with a **material-specific coefficient and E-scale**. Vary the two independently:

1. **Material swap at fixed geometry.** Run the *same* electrode/resonator geometry with the vacuum gap (a) bare-vacuum, (b) low-Kerr dielectric (fused silica), (c) high-Kerr (BaTiO₃). The vacuum δε(E) component is **identical** across all three (same field hot spot, same E_YIELD-scaled coefficient); the material component scales with the material's Kerr coefficient. **Extrapolate the material series to zero Kerr → the residual is the universal vacuum term.** AVE predicts a *non-zero negative* residual with coefficient −½ at E-scale E_YIELD; pure-material physics predicts the residual → 0.
2. **Geometry/β variation at fixed material.** Sweep β (tip radius / array density) at fixed bulk material. The vacuum term scales as β² (through A_hot²) and concentrates at the hot spot; the bulk material term is β-independent (it fills the bulk, not the tip). **The β²-scaling component localized at the hot spot is the vacuum; the β-flat bulk component is the material.**
3. **E_YIELD-scale signature.** The vacuum coefficient is pinned to E_YIELD = 1.130×10¹⁷ V/m: plot δε vs (E/E_YIELD)² and the vacuum slope is exactly −½, *independent of material*. A material Kerr term plotted on the same axis has a material-specific (and generally enormous, since E_Kerr ≪ E_YIELD) slope. The **−½ slope at the E_YIELD scale, invariant under material swap, IS the vacuum fingerprint.**
4. **Temperature null.** Cool the resonator: the vacuum term is T-invariant; electrostriction/Kerr are strongly T-dependent. The **T-invariant residual** is the vacuum component. (This doubles as the cryo-architecture's native control.)
5. **Sign + polarity controls (carry from IVIM hardening 2026-06-03 §4.2):** the vacuum term is polarity-symmetric (∝E²) and single-valued in slow-DC (no hysteresis). Field-emission/charging confounds are polarity-asymmetric / hysteretic. Reverse polarity and ramp up-vs-down; the invariant, single-valued, **negative** δε is the vacuum.

**Separability verdict:** the vacuum component is isolable **because its coefficient (−½) and its E-scale (E_YIELD) are both universal and both fixed by `constants.py`** — three independent knobs (material, geometry/β, temperature) each leave it invariant while moving the material background. This is the discrimination the knee-vs-smooth shape was supposed to provide, recovered without the knee. **Caveat (honest):** the residual-extrapolation requires the vacuum term to clear the *post-subtraction* noise floor; at the nominal bulk Δf₀/f₀ ~10⁻¹⁵ this demands the resonant-Q architecture AND material subtraction good to ≲10⁻¹⁵ — the load-bearing feasibility constraint (§5).

---

## 3. DETECTION-ARCHITECTURE RECOMMENDATION (deliverable 3 — answers Q-G42 §4 Q1–Q3)

### Q1 (modality) + Q3 (target): **Method B — autoresonant PLL Δf₀(V) at the resonant-Q architecture, resolution floor 10⁻¹⁵.**

The resonant-Q autoresonant reaches the bulk V²-sign signal (Δf₀/f₀ ≈ +1.76×10⁻¹⁵ nominal, SNR ≈ 1.8) above the material background **provided** the vacuum-vs-material separation (§2) is executed (the material term is generally larger and must be subtracted/extrapolated, not just noise-floored). The cryo-lock-in (10⁻¹²) reaches it only for an optimistic tight-resonator geometry (η_eff ~10⁻⁶). The precision-bridge (10⁻⁹) is the *characterization* tool (Method A small-signal C-V) but is 3–6 OOM short of the vacuum *discovery* signal.

- **Co-primary even-2ω harmonic (Method A / parametric):** the canonical δC = ¼C₀(V/V_yield)² rides at **2ω** (cos² → ½(1+cos2ωt)). At a *bulk* sub-yield pump this is large (4.6% at V/V_yield=0.428, 11.8% at 0.687 — but those are **bulk-pump operating points** reaching a large fraction of V_yield in a macroscopic-pump cavity, not the diluted small-A hot-spot bench). The even-2ω is the AVE-distinct *harmonic* fingerprint (corpus elsewhere emphasizes odd-IM3); it provides a frequency-domain background-rejection channel co-primary with the Δf₀ sign. **Flag-3 (§6):** the 4.57% reuse figure is at V/V_yield=0.428, NOT the bench A≈2.7×10⁻³ — do not conflate the bulk-pump 2ω amplitude with the diluted bench shift.

### Q2 (realistic β) — reconcile the catalog {30, 10³, 10⁵}:

| β | geometry | defensible? | use |
|---|---|---|---|
| **30** | single hemispherical tip, curvature-only (bench-VM ch09:140) | **YES** — standard EM curvature enhancement | conservative floor |
| **10³** | tip-array **× Q_build=10⁴ resonant field build-up** (PONDER ch1:51) | **YES — the defensible operating point** | nominal (used above) |
| **10⁵** | combined geom × resonant × ferro (App F caption) | **NO derivation; do NOT headline** | upper-bound only |

**Recommendation: adopt β=10³ with Q_build=10⁴ as the defensible nominal** (the PONDER operating point, verified to source). β=10⁵ is an und'erived App-F caption assertion — usable only as an optimistic upper bound, never as the pre-registered prediction. The G_ferro~3000 BaTiO₃ interface concentration (Q-G42 §2.5) is a *legitimate* additional ×ε_r factor at a ferroelectric-vacuum interface and is the most plausible *derived* route toward the high-β end — but it belongs in the material-swap protocol (§2.1, step 1) as a *signal-boosting variation*, not folded silently into β. At β=10³·Q_build=10⁴ the canonical RMS A_hot = 2.654×10⁻³ (note §6 flag-1 [RESOLVED]: PONDER's 3.8×10⁻³ is the **peak** ratio A_peak = √2·A_hot, both on canonical E_YIELD; this script's RMS from-constants value is A_hot = 2.654×10⁻³).

---

## 4. SNR + dilution sensitivity (the magnitude gate)

The decisive sensitivity is **η_eff** (field-filling fraction), which spans the GO/NO-GO boundary:

- η_eff ~10⁻⁶ (optimistic, tight resonator, hot feature ~1% of resonator scale): Δf₀/f₀ ~10⁻¹² → cryo-lock-in **detects** (SNR 1.8), resonant-Q with margin (SNR 1.8×10³).
- η_eff ~10⁻⁹ (nominal): Δf₀/f₀ ~10⁻¹⁵ → only resonant-Q detects (SNR 1.8).
- η_eff ~10⁻¹² (conservative, large resonator): Δf₀/f₀ ~10⁻¹⁸ → **below all current floors** (3 OOM short of resonant-Q).

The build therefore lives or dies on **maximizing η_eff** — i.e. making the resonator as *small* as the field hot spot permits (high r_feat/L_res), the opposite of the usual "big high-Q cavity" instinct. This is the single most important design lever and the honest risk: a conservative large-resonator geometry kills the signal even at the resonant-Q floor.

---

## 5. EE-INTUITION SUMMARY (deliverable — `ave-ee-intuition-summary`, the 5-beat on the sign-test)

1. **The vacuum is a varactor.** Bias the bond-LC tank with a static field and its capacitance moves — same as a DC-biased semiconductor varactor. The bias variable is A = E/E_YIELD, the operating point on the Ax-4 quarter-arc.
2. **AVE says it softens; QED says it stiffens.** Under field, the AVE vacuum's ε goes *down* (the varactor's C goes *up*, its resonance goes *up*); the QED vacuum's ε goes *up*. The **sign of the V² coefficient** is the whole discriminator — no knee, no magnitude match needed.
3. **You can't reach the knee, but you don't need to.** V_yield is per-node (43.65 kV across a 0.4-pm node), not per-apparatus; the bench gets to A~10⁻³ at the tip, a tree-level wiggle, not the cliff. The *sign of the wiggle* is still AVE-vs-QED, and the ratio is 12 OOM (reflectance) / 6 OOM (resonance shift).
4. **Put it in a resonator and the resonator-Q lets you read a 10⁻¹⁵ frequency wiggle** — but Q buys *resolution*, not *signal*: the wiggle Δf₀/f₀ ~10⁻¹² to 10⁻¹⁵ is set by how much of the resonator volume the hot spot fills (the dilution), and Q just sets how small a Δf₀ you can resolve.
5. **A real dielectric also wiggles, so you separate by universality:** swap the material, sweep the tip, cool it — the vacuum term has a *fixed −½ slope at the E_YIELD scale* and doesn't care; the material term moves. The invariant, polarity-symmetric, single-valued, **negative** residual is the vacuum.

---

## 6. FLAG-DON'T-FIX (surfaced, not silently reconciled — Grant adjudication)

1. **[RESOLVED 2026-06-03 — peak/RMS convention difference, NOT a superseded E_yield.]** PONDER ch1 quotes the **peak** hot-spot ratio A_peak = βQ·E_macro·√2 / E_YIELD = 4.24×10¹⁴ / 1.13×10¹⁷ = 3.75×10⁻³ (≈ "3.8×10⁻³"), peak deficit (1−S)_peak = A_peak²/2 ≈ 7×10⁻⁶. This script's `a_hot()` uses the **RMS** ratio A_hot = βQ·E_macro / E_YIELD = 2.654×10⁻³ (no √2), (1−S) = A_hot²/2 = 3.52×10⁻⁶. **A_peak/A_hot = √2 exactly — both on the canonical E_YIELD = 1.130×10¹⁷ V/m** (PONDER ch1:26,30). The load-bearing cycle-averaged shift agrees: PONDER's δ = A_peak²/4 = 3.52×10⁻⁶ (ch1:128/159) = this script's A_hot²/2. The canonical AC convention (`parametric-coupling-kernel.md` §3: δC = ¼C₀(V_pump/V_yield)² with **peak** V_pump) is the peak form PONDER uses. **Resolution: PONDER ch1 is arithmetically correct and needs no E_YIELD walk-back** (companion clarifier: AVE-PONDER PR #2). Corrections landed in AVE-Core: this script's comments (lines 12/99/186) and `claim-quality.md:203` now label peak-vs-RMS, and `claim-quality.md`'s erroneous "fix exponent 10¹⁴→10¹⁷" strengthen-by (which would have corrupted PONDER's correct value) was removed. Verified: `7.89×10¹⁶` never existed in `constants.py` history (`git log -S '7.89' -- src/ave/core/constants.py` empty). (The separate App-F obsolete-E_yield claim cited from Q-G42 §2.4 is out of scope here and unverified.)

   > _Originally flagged 2026-06-03 (superseded diagnosis, preserved per `ave-walk-back` Rule 12):_ "**Canonical A_hot = 2.654×10⁻³, PONDER ch1:51 quotes 3.8×10⁻³ (factor 1.43).** … PONDER's value back-implies E_yield≈7.89×10¹⁶ V/m — a ~1.43× lower, superseded E_yield (cf. Q-G42 §2.4: App F used an obsolete ~10¹⁴–10¹⁶ E_yield). … Impact: factor-1.43 in A, factor-2 in (1−S) and hence in Δf₀/f₀. … walk PONDER ch1:51 forward to canonical E_YIELD per `ave-walk-back`." **Why it was wrong:** the factor 1.43 is the √2 peak-vs-RMS convention difference (√2 = 1.4142, rounded from 3.753/2.654), not a stale E_yield; PONDER uses canonical 1.13×10¹⁷ throughout (ch1:26).
2. **"Resonator-Q amplification" (prereg deliverable-1(b)) is physically the resolution-floor mechanism, not a signal gain.** The prereg wording ("the resonator Q amplifies a tiny ε change into a measurable f₀ shift") reads as multiplicative signal gain. Physically Δf₀/f₀ = −½⟨Δε/ε⟩_bulk is **independent of Q**; Q sets the *minimum resolvable* Δf₀/f₀ (≈1/(Q·SNR_loop)). The two are numerically reconciled by the three architecture floors (which encode Q-dependent resolution), so the prereg's conclusion is preserved — but the *mechanism* is resolution, not amplification. Surfaced so the pre-reg-freeze uses the correct mechanism. *No corpus edit; this doc states the resolved physics.*
3. **The 4.57% δC/C reuse figure is at V/V_yield=0.428 (18.7 kV bulk pump), NOT the bench A≈2.7×10⁻³.** `parametric-coupling-kernel.md:70` boxes δC=¼C₀(V/V_yield)² and quotes δC/C₀=4.57% — but at the canonical 18.7 kV pump (V/V_yield=0.428), a *bulk-pump* operating point reaching ~43% of V_yield in a macroscopic pump cavity. At the *diluted small-A bench hot spot* the 2ω modulation is ~A²/4-class, vastly smaller. The formula is canonical and reused correctly; the *4.57% number* must not be quoted as the bench-reachable 2ω shift. *Flagged so the architecture-rec §3 Q1 does not over-claim the even-2ω amplitude.*

---

## 7. GO / NO-GO VERDICT

**GO — the V²-sign test is buildable AND AVE-distinct, at the resonant-Q autoresonant architecture (Method B), conditional on geometry (η_eff) and on executing the vacuum-vs-material separation (§2).**

- **Buildable?** YES at resonant-Q (floor 10⁻¹⁵): nominal bulk Δf₀/f₀ ≈ +1.76×10⁻¹⁵, SNR ≈ 1.8. Marginal at cryo-lock-in (optimistic geometry only). Below floor at precision-bridge. **Hard risk:** a conservative large-resonator geometry (η_eff ≲10⁻¹²) kills it even at resonant-Q — the build must *maximize* field-filling fraction (small resonator, sharp hot spot).
- **AVE-distinct?** YES — the **sign** (soften/Δf₀>0 vs stiffen/Δf₀<0) is a two-sided binary with a 6-OOM (resonance) / 12-OOM (reflectance) discrimination ratio, geometry- and material-invariant, exact from `constants.py`. Separable from material electrostriction/Kerr by the §2 universality protocol (fixed −½ slope at E_YIELD, invariant under material/β/T variation).
- **Architecture:** **resonant-Q autoresonant PLL**, β=10³·Q_build=10⁴ (PONDER operating point), Δf₀(V) sign + even-2ω co-primary, with the material-swap / β-sweep / cryo separation as the load-bearing systematic control.
- **The autoresonant number (the deliverable Ch 15 lacked):** **Δf₀/f₀ ≈ +1.76×10⁻¹² (optimistic η_eff=10⁻⁶) to +1.76×10⁻¹⁵ (nominal η_eff=10⁻⁹)**, positive (resonance rises = vacuum softens).

**NOT a clean unconditional GO:** the verdict is gated on (i) η_eff (geometry — the dominant sensitivity), (ii) material-background subtraction to ≲ the vacuum signal, (iii) reaching the 10⁻¹⁵ resolution floor. All three are engineering-hard but not physics-blocked. The pre-reg can be frozen around the resonant-Q Δf₀-sign observable with these three as the named feasibility risks.

---

## 8. Reuse ledger (every citation re-verified to source this session — `verify-before-cite`)

| Reuse | Source (verified 2026-06-03) | Status |
|---|---|---|
| C–V table (C_eff/C0 = 1.155/2.294/7.089 @ V/V_yield=0.5/0.9/0.99) | `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/nonlinear-vacuum-capacitance.md:32-39` | ✓ exact |
| PONDER-05 C–V (27.4% ε-collapse, C_eff +37.7% @ V_DC/V_yield=0.687, ~30 kV) | `manuscript/backmatter/07_universal_saturation_kernel.tex:107` | ✓ exact |
| δC = ¼C₀(V/V_yield)², δC/C₀=4.57% @ 2ω | `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/parametric-coupling-kernel.md:70` | ✓ exact (caveat: 4.57% @ V/V_yield=0.428, flag-3) |
| 8.381×10¹² ratio + V⁴/V² + (4α²/9) QED kernel | `AVE-Bench-VacuumMirror/docs/analysis/2026-06-03_ivim_adversarial_reverification.md` §1.2, §5 | ✓ reproduced exactly from constants.py |
| 8.3×10¹² structural-invariant + tree-vs-loop framing | `AVE-QED/manuscript/vol_qed_replacement/chapters/00_intro.tex:88-92` | ✓ exact |
| β catalog {30, 10³, 10⁵}, G_ferro~3000, A≈3.8×10⁻³ operating pt | Q-G42 §2.3/§2.5; `AVE-PONDER/.../01_topological_thrust_mechanics.tex:51,122` | ✓ (3.8×10⁻³ is PONDER's peak ratio; canonical RMS A_hot=2.654×10⁻³ — §6 flag-1 RESOLVED) |
| E_YIELD/V_YIELD/E_CRIT/L_NODE/ALPHA | `src/ave/core/constants.py:382/393/387/234/133` | ✓ imported by script |

---

## Cross-references

- Prereg (reframe spec): `research/2026-06-03_yield-knee-map-prereg.md` (grep-RESULT §)
- Prior Phase-0 (resumed): `AVE-QED/docs/analysis/2026-05-13_Q-G42_v_yield_apparatus_scaling_prereg.md` §4 Q1–Q3
- Phase-0 calc script: `src/scripts/vol_4_engineering/qg42_vsign_phase0.py`
- IVIM adversarial re-verification (discrimination ratio source): `AVE-Bench-VacuumMirror/docs/analysis/2026-06-03_ivim_adversarial_reverification.md`
- Canonical constants: `src/ave/core/constants.py`

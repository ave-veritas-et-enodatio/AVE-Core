# Q-G42 Phase-1 RESULT — V²-Sign Autoresonant Δf₀/f₀: Closed Form, Vacuum-vs-Material, Architecture, β-Reconcile

**Status:** PHASE-1 COMPLETE (2026-06-04). Hardening of the tree-level V²-coefficient SIGN test. Resumes Phase-0 (`research/2026-06-03_qg42-resume-vsign-phase0-result.md`, GO verdict) per the orchestration resumption paragraph (`_orchestration/2026-06-03_experimental-protocol-revamp-orchestration.md` §10).
**Lane:** implementer (experimental-protocol revamp).
**Prereg:** `research/2026-06-04_qg42-phase1-prereg.md` (corpus-grep + classification + dimensional pre-freeze).
**Calc script:** `src/scripts/vol_4_engineering/qg42_vsign_deltaf.py` (all numbers below regenerate from it; physics imported from `ave.core.constants`; FORWARD-prediction only — no fit-to-target, ave-driver-script-honesty).
**Discipline applied:** `ave-prereg` (grep-before-derive) · `ave-canonical-source` (constants.py imports) · `ave-canonical-leaf-pull` (A-034 + four-regimes + temporal-classifier) · `consistency-vs-emergence` (Δf₀/f₀ classified §0) · `ave-driver-script-honesty` (forward-only driver) · `flag-don't-fix` (reachability fork + FN-contradiction surfaced §2/§5, NOT resolved) · `verify-before-cite` (every cite re-checked to source this session) · `ave-evidence-framing-discipline` (sign-vs-magnitude framing §0).

---

## 0. The classification, up front (consistency-vs-emergence)

The Δf₀/f₀ observable has a **two-tier classification** that must headline everything below, because it is the whole epistemic point of the Q-G42 program:

- **MAGNITUDE |Δf₀/f₀|: Class B (axiom manifestation).** It *is* the Axiom-4 saturation kernel (A-034 row 1) expressed at the bench resonator scale. It routes through E_YIELD = √α·E_CRIT, so per the 2026-06-02 honest-α relabel (α is a *named geometric identification*, not independently derived) the magnitude is **Class-B-at-one-identification**. We do NOT headline the magnitude as an emergence-class prediction.
- **SIGN of Δf₀/f₀: the load-bearing AVE-distinct content, ROBUST to the √α magnitude uncertainty.** AVE: Δf₀/f₀ > 0 (resonance RISES, vacuum softens). QED: Δf₀/f₀ < 0 (resonance falls, vacuum stiffens). The sign is fixed by the *form* of the kernel — S(A) < 1, monotone-decreasing, ∀ 0<A<1 — which is Axiom 4 itself, **independent of the value of the √α scale**. Against QED's rigorously-positive Euler-Heisenberg coefficient, this is a genuine two-sided forward discriminator. **The sign sidesteps the Class-B magnitude uncertainty: it is a forward yes/no the inputs do not predetermine.**

**Honest one-liner for any downstream citation:** *"AVE predicts the resonance RISES under field; QED predicts it FALLS. The SIGN is a forward discriminator robust to the √α kernel-magnitude uncertainty; the MAGNITUDE is a Class-B axiom-manifestation."*

---

## 1. DELIVERABLE 1 — the closed-form small-signal autoresonant Δf₀/f₀

### 1.1 The chain (substrate-native: Ax-4 varactor-bias of the bond-LC tank, all from constants.py)

The vacuum bond-LC tank is a varactor: a static/AC field biases its capacitance along the Axiom-4 quarter-arc. The small-signal fractional resonance shift derives in four steps:

1. **Local kernel (Ax 4, exact):** δε/ε₀ = S(A) − 1 = √(1−A²) − 1, where A = E_local/E_YIELD. Negative ∀ 0<A<1 (softens). Small-A leading term: **−½A²**.
2. **Local hot-spot amplitude:** A_RMS = G_geom·V_app/(d_gap·E_YIELD), with G_geom = β·Q_build the total field-concentration factor and E_YIELD = 1.13041×10¹⁷ V/m (canonical).
3. **Bulk volume-weighted dilution** (the load-bearing bulk factor). The hot spot fills a tiny fraction of the resonator; the tip-dipole field falls as E ∝ 1/r², so δε ∝ A² ∝ 1/r⁴ (steeply localized, integral converges within a few feature scales). The bulk eigenfrequency shift is the volume-weighted local shift:
   $$\langle \delta\varepsilon/\varepsilon_0\rangle_{\text{bulk}} = -\tfrac12 A_{\text{RMS}}^2\,\eta_{\text{eff}}, \qquad \eta_{\text{eff}} \sim (r_{\text{feat}}/L_{\text{res}})^3$$
   η_eff is the **field-filling fraction** (geometry-dependent dilution, bracketed §1.3).
4. **LC resonator relation:** f₀ = 1/(2π√(LC)), C ∝ ε ⟹ **Δf₀/f₀ = −½·⟨δε/ε₀⟩_bulk**. Since ⟨δε/ε₀⟩_bulk < 0 (softening), the resonance RISES:

> **CLOSED FORM (the deliverable Ch 15 lacks):**
> $$\boxed{\;\frac{\Delta f_0}{f_0} = +\tfrac14\,A_{\text{RMS}}^2\,\eta_{\text{eff}} = +\frac{1}{4}\left(\frac{G_{\text{geom}}\,V_{\text{app}}}{d_{\text{gap}}\,E_{\text{YIELD}}}\right)^{\!2}\eta_{\text{eff}}\;}$$
> **Positive (resonance RISES) — the AVE-distinct sign. Scaling: ∝ G_geom²·V_app²·η_eff/(d²·E_YIELD²).**

**Q is NOT a signal multiplier (carried + re-confirmed from Phase-0 §6 flag-2).** Δf₀/f₀ is fixed entirely by ⟨δε/ε₀⟩_bulk. The resonator line-Q sets the *minimum resolvable* fractional shift (≈1/(Q·SNR_loop), the Allan-floor argument), not a signal gain. The three architectures differ by their resolvable-Δf₀/f₀ floor, not by amplification. (Distinct from Q_build, the resonant *field* build-up that raises A_RMS — that DOES enter the signal.)

### 1.2 Why this is genuinely green-field (Ch 15 confirmed rupture-only AND invalidated)

`vol4/simulation/ch15-autoresonant-breakdown/theory.md` treats the autoresonant PLL ONLY as a *rupture-driver* (ring-up toward V_snap to shatter the vacuum). Worse, it carries a ⛔ **INVALIDATED** banner (`theory.md:8`): its entire numerical content rests on a wrong 60 kV threshold (the D-T ion-collision strain from `tokamak-paradox.md`, not the canonical 43.65 kV V_yield) and "should be disregarded until recomputed." **There is no small-signal bulk-resonator Δf₀/f₀ anywhere in the manuscript.** The boxed closed form above is the gap-fill, in the *small-signal lossless-reactive* regime (NOT the rupture regime), pinned to constants.py.

### 1.3 The numbers (honest-camp PONDER operating point; regenerate from the script)

Canonical bench: V=30 kV, d=1 mm, G_geom = β·Q_build = 10³·10⁴ = 10⁷ (PONDER ch1:116,122).

- **A_RMS = 2.6539×10⁻³** (RMS); peak A_peak = √2·A_RMS = 3.7532×10⁻³ ≈ PONDER ch1:122's quoted 3.8×10⁻³ (peak convention). LOCAL δε/ε₀ = −3.522×10⁻⁶.
- **Bulk Δf₀/f₀ per dilution bracket:**

| η_eff (field-filling) | geometry | **Δf₀/f₀** (closed form) | exact-kernel |
|---|---|---|---|
| 10⁻⁶ | optimistic (r_feat/L_res ~ 10⁻²) | **+1.761×10⁻¹²** | +1.761×10⁻¹² |
| 10⁻⁹ | nominal (r_feat/L_res ~ 10⁻³) | **+1.761×10⁻¹⁵** | +1.761×10⁻¹⁵ |
| 10⁻¹² | conservative (r_feat/L_res ~ 10⁻⁴) | **+1.761×10⁻¹⁸** | +1.761×10⁻¹⁸ |

The closed form and the exact-kernel form agree to <0.01% at this A_RMS (small-A regime). **Δf₀/f₀ ≈ +1.76×10⁻¹² (optimistic) to +1.76×10⁻¹⁵ (nominal), positive — resonance rises.** Reproduces Phase-0 exactly. This is the green-field number.

**Temporal-regime tag (temporal-saturation-regime-classifier):** δ_AVE = t_sat/t_period ≪ 1 — the small-signal AC drive is in the **lossless/cyclic** regime (the field wiggles on the linear part of the arc, never reaching saturation within a cycle). This confirms the observable is **reactive-power** (the C-state of the LC tank), categorically distinct from the lossy real-power dissipation at rupture (Ch 15). The autoresonant-PLL reads the reactive Δf₀, not a dissipative loss.

---

## 2. DELIVERABLE 4 (taken before 2/3 because it gates them) — the β/G_geom reconciliation

The prior runs disagreed on the geometric prefactor: the catalog is {30, 10³, 10⁵}. **Resolution: the catalog is not three competing values of one quantity — it is two SEPARATE factors (geometric β and resonant Q_build) plus an underived upper bound, and a canonical Fowler-Nordheim destruction limit that hard-bounds the DC-equivalent.**

### 2.1 The decomposition (β and Q_build are separate, verified to source)

| Symbol | Meaning | Canonical value | Source (verified 2026-06-04) |
|---|---|---|---|
| **β** (geometric tip) | hyperboloid-on-plane curvature concentration β = h_tip/r_tip | **10³** (1 µm tip, 1 mm standoff) | PONDER ch1:116 |
| **Q_build** (resonant) | RF field build-up in the cavity | **10⁴** | PONDER ch1:122 |
| **G_geom = β·Q_build** | total field-concentration | **10⁷** | PONDER ch1:122 (E_local^peak = β·Q·E_macro·√2 ≈ 4.2×10¹⁴ V/m) |
| β = 30 | single hemispherical tip, curvature-only | curvature floor | bench-VM Paschen ch09 |
| β = 10⁵ | combined geom×resonant×ferro | **underived** (App-F caption) | use as upper bound ONLY, never headline |

So "β = 30" is the bare-curvature floor, "β = 10³" is the geometric tip alone (NOT including Q), and "10⁵" conflates β×Q×ferro into one symbol without derivation. **The {30, 10³, 10⁵} confusion was a symbol-overloading artifact: β=10³ is the tip factor and the resonant build-up Q=10⁴ is a separate multiplicative factor; G_geom = β·Q_build = 10⁷ is the total. The "10⁵" upper bound is β·Q·ferro folded into one symbol, underived.** This reconciles the catalog.

### 2.2 The HARD constraint the reconcile surfaces — Fowler-Nordheim electrode destruction (FLAG)

`17_noise_floor_boundary.tex:39,49,54` makes **β_crit ≈ 6 the field-emission DESTRUCTION boundary**: above a local surface field of ~1.3×10⁹ V/m (electropolished β≈3), the Fowler-Nordheim dark current exceeds 10⁻⁹ A and the electrode self-destructs. The script reproduces the canonical table exactly:

| β | E_local [V/m] | J_FN [A/m²] | Status (tex) |
|---|---|---|---|
| 3 | 1.31×10⁹ | 1.4×10⁻¹⁰ | SAFE |
| 6 | 2.62×10⁹ | 3.6×10¹ | MARGINAL |
| 50 | 2.18×10¹⁰ | 8.2×10¹² | DESTRUCTIVE |

**The FN-safe DC surface-field ceiling is ~1.31×10⁹ V/m, which corresponds to a maximum FN-safe local A_max ≈ 1.16×10⁻⁸.** But the PONDER operating point needs A_RMS ≈ 2.65×10⁻³, requiring a local field E_local = G_geom·E_macro = **3.0×10¹⁴ V/m — that is 2.3×10⁵× the FN-safe DC ceiling.** A *static* tip producing that field would have field-emitted catastrophically (J_FN ~ 10¹² A/m²) before any measurement.

**⚑ FLAG-DON'T-FIX (load-bearing, surfaced NOT resolved):** the PONDER β·Q operating point and the canonical FN-destruction limit CONTRADICT — both are in the corpus. The corpus's own partial reconciliation: PONDER ch1:126 argues the tips are **"regime-bouncing"** — the local field is a *transient RF peak* rising from zero each half-cycle, NOT a *sustained DC* field, so DC FN-destruction (computed for the sustained-field case in ch17) "may be evaded" per-half-cycle. **But PONDER ch1:168 itself flags this as an OPEN engineering question** (*"Whether 10,000 tips can be driven coherently at Q=10⁴ is an open engineering question"*). So the β-reconcile resolves the SYMBOL confusion ({30,10³,10⁵} = β, β, β·Q·ferro) but surfaces a genuine, corpus-acknowledged-open feasibility gap: **whether the resonant regime-bouncing architecture actually evades the FN-destruction limit that forbids the equivalent DC field.** This is escalated, not resolved — it requires either (a) a transient-FN integration the corpus does not yet have, or (b) Grant's engineering call. It is a NAMED feasibility risk, not a physics blocker on the sign.

---

## 3. DELIVERABLE 2 — vacuum-vs-material separation (the load-bearing systematic)

A real dielectric's electrostriction / Kerr / material-saturation also shifts ε(E) — either sign, often *larger* than the vacuum term (PONDER-05's 27.4% ε-collapse in quartz raised exactly this consistency-vs-emergence question: is it the vacuum kernel or quartz's ordinary voltage-coefficient-of-capacitance?). A raw Δf₀/f₀ cannot be attributed to the vacuum. The separator rests on **what is universal vs material-specific:**

| Property | Vacuum (AVE Ax-4) | Material (electrostriction/Kerr) |
|---|---|---|
| Coefficient | **fixed −½** (in A²); zero free parameters | material-specific, fitted, sign varies |
| E-scale | **E_YIELD = 1.13×10¹⁷ V/m** (universal, constants.py) | material breakdown / Kerr (10⁸–10¹⁰ V/m) |
| Sign | **always negative** (softens), every geometry, every material | set by the material; not constrained |
| Temperature | **none** (substrate kernel) | strong (electrostriction, Kerr both T-dependent) |
| Geometry | enters ONLY through the field map; coefficient invariant | tracks the *material* fill, not the field hot spot |

### 3.1 The protocol — three orthogonal knobs each leave the vacuum invariant while moving the material background

1. **Material swap at fixed geometry.** Run the same resonator with the gap (a) bare-vacuum, (b) low-Kerr (fused silica), (c) high-Kerr (BaTiO₃). The vacuum δε(E) component is identical across all three (same field hot spot, same E_YIELD-scaled −½ coefficient); the material component scales with the material's Kerr coefficient. **Extrapolate the material series to zero Kerr → the residual is the universal vacuum term.** AVE predicts a non-zero *negative* residual at E-scale E_YIELD; pure-material physics predicts the residual → 0.
2. **Geometry/β sweep at fixed material.** Sweep β (tip radius / array density). The vacuum term scales as β² (through A_RMS²) and concentrates at the hot spot; the bulk material term is β-independent (fills the bulk, not the tip). **The β²-scaling component localized at the hot spot is the vacuum; the β-flat bulk component is the material.**
3. **E_YIELD-scale + temperature signatures.** Plot δε vs (E/E_YIELD)²: the vacuum slope is exactly **−½, independent of material**; a material Kerr term has a material-specific (and generally enormous, since E_Kerr ≪ E_YIELD) slope. Cool the resonator: the vacuum term is T-invariant; electrostriction/Kerr are strongly T-dependent. The **T-invariant, −½-slope-at-E_YIELD, polarity-symmetric (∝E²), single-valued (no hysteresis) residual is the vacuum.** (Field-emission/charging confounds are polarity-asymmetric / hysteretic — reverse polarity and ramp up-vs-down to reject them.)

**Separability verdict:** the vacuum component is isolable **because its coefficient (−½) and E-scale (E_YIELD) are both universal and both fixed by constants.py** — three independent knobs (material, β, temperature) each leave it invariant while moving the material background. **Caveat (honest):** the residual-extrapolation requires the vacuum term to clear the *post-subtraction* noise floor; in the honest camp at Δf₀/f₀ ~10⁻¹⁵ this demands the resonant-Q architecture AND material subtraction good to ≲10⁻¹⁵ — the load-bearing feasibility constraint. **The PONDER-05 quartz question is exactly resolved by knob 1: if the 27.4% ε-collapse persists with the SAME −½ coefficient at the SAME E_YIELD scale after extrapolating quartz→vacuum, it is the universal vacuum kernel; if it scales with quartz's Kerr coefficient and vanishes on extrapolation, it is the material.** (Which it is depends on the reachability fork §5 — in the honest camp quartz at 30 kV is Regime I, so a 27.4% collapse would be material-dominated.)

---

## 4. DELIVERABLE 3 — detection-architecture recommendation

Among the three Phase-0 options (precision-bridge 10⁻⁹ / cryo-lock-in 10⁻¹² / resonant-Q autoresonant 10⁻¹⁵), which reaches the derived Δf₀/f₀? Per-architecture SNR against the honest-camp closed-form signal (script §4):

| Architecture | resolvable Δf₀/f₀ floor | SNR (nominal η=10⁻⁹) | SNR (optimistic η=10⁻⁶) | Verdict |
|---|---|---|---|---|
| precision-bridge | 10⁻⁹ | 1.76×10⁻⁶ | 1.76×10⁻³ | **below floor** (3–6 OOM short) |
| cryo-lock-in | 10⁻¹² | 1.76×10⁻³ | **1.76** | marginal (optimistic geometry only) |
| resonant-Q | 10⁻¹⁵ | **1.76** | 1.76×10³ | **DETECT** |

**RECOMMENDATION: resonant-Q autoresonant PLL (floor 10⁻¹⁵).** In the honest camp it is the only architecture that reaches the bulk Δf₀/f₀ ≈ +1.76×10⁻¹⁵ (nominal geometry, SNR ≈ 1.8) above the floor. The cryo-lock-in reaches it ONLY for an optimistic tight-resonator geometry (η_eff ~10⁻⁶, SNR ≈ 1.8). The precision-bridge is 3–6 OOM short of the vacuum *discovery* signal — it is the *characterization* tool (Method-A small-signal C-V), not the discovery tool. **The decisive sensitivity is η_eff (field-filling fraction):** the build must *maximize* η_eff (small resonator, sharp hot spot, high r_feat/L_res) — the opposite of the usual "big high-Q cavity" instinct. A conservative large-resonator geometry (η_eff ≲10⁻¹²) kills the signal even at the resonant-Q floor (Δf₀/f₀ ~10⁻¹⁸, 3 OOM short). This is the single most important design lever and the honest risk.

**Co-primary even-2ω harmonic channel:** the canonical δC = ¼C₀(V/V_yield)² rides at 2ω (cos²→½(1+cos2ωt), `parametric-coupling-kernel.md:70`). It is the AVE-distinct *harmonic* fingerprint (corpus elsewhere emphasizes odd-IM3) and provides a frequency-domain background-rejection channel co-primary with the Δf₀ sign. **Caveat (carried from Phase-0 flag-3):** the canonical 4.57% δC/C₀ figure is at V/V_yield=0.428 (an 18.7 kV *bulk-pump* operating point), NOT the diluted small-A bench hot spot — do NOT quote 4.57% as the bench-reachable 2ω amplitude.

**Architecture verdict is CONDITIONAL on the reachability camp (§5):** the above is the honest-camp answer. In the conflated camp (apparatus V reaches 0.85 V_yield), ΔC/C₀ ~90% is macroscopic and ANY commercial LCR meter / precision-bridge reaches it — the architecture question collapses. The recommendation is therefore: **resonant-Q autoresonant IF the honest camp holds; precision-bridge suffices IF the conflated camp holds. The camp must be adjudicated (Grant) before the architecture is final.**

---

## 5. ⚑ FLAG-DON'T-FIX — the corpus-wide reachability contradiction (surfaced, NOT resolved)

This is the load-bearing flag (Rule 6). The orchestration §10 flag (`_orchestration/...:173`) already named a corpus-wide per-node-V_yield/apparatus conflation as BLOCKING corpus surgery pending Grant; this grep sharpened it with verbatim both-sides evidence.

**Honest camp — bench in Regime I, E/E_yield ≈ 2.7×10⁻¹⁰:**
- `regimes-of-operation.md:32` (clm-trgqtf): *"An asymmetric capacitor driven at 30 kV with a 1 mm gap produces E ≈ 3×10⁷ V/m. The saturation ratio E/E_yield ≈ 2.7×10⁻¹⁰ places the device firmly in Regime I (linear vacuum)... bulk ε-saturation is not the operative thrust mechanism."*
- `vol4/claim-quality.md:158`: *"Regime III/IV are reached only at sub-femtometer separations... This places the bulk-yielding limit far from any lab apparatus."*

**Conflated camp — bench reaches V/V_yield = 0.687–0.85 at 30–43 kV:**
- `measurement-hierarchy-snr.md:66`: *"detects 27.4% ε_eff collapse at V_DC/V_yield = 0.687 (bench-measurable at ~30 kV bias per Vol 4 Ch 1)."*
- `vol_4_engineering/chapters/17_noise_floor_boundary.tex:79-84`: *"The AVE-predicted signal at V/V_yield = 0.85... ΔC/C0 ≈ 90%... measurable by any commercial LCR meter. The signal-to-noise ratio exceeds 10⁹."*

**Root (canonically diagnosed):** `claim-quality.md:51` + `regimes-of-operation.md:11` both state V_yield = 43.65 kV is **per lattice node** (across ℓ_node = 0.386 pm), NOT per apparatus. The conflated camp reads 30–43 kV *across a macroscopic gap* as if it were the per-node value. `claim-quality.md:51`: *"Conflating them... is the most common Vol 4 reading error."* The two camps differ by **~12 OOM** in the predicted signal.

**Why I do NOT resolve it:** adjudicating requires deciding whether per-node V_yield can be reached as an apparatus voltage — the foundational physics question, Grant's call. Per flag-don't-fix, silently picking one camp could mask a cross-domain signal only Grant sees. **BUT the SIGN of the V²-coefficient is identical in both camps** (the vacuum softens either way — Δf₀/f₀ > 0), so the forward-discriminator survives the fork. The fork bears on the MAGNITUDE / architecture / feasibility, not on the discriminator's existence or direction.

**Two named feasibility risks the fork + FN-limit produce (NOT physics blockers on the sign):**
1. **Reachability fork (§5):** honest camp → 10⁻¹⁵ resonant-Q build; conflated camp → macroscopic LCR. ~12 OOM apart. Needs Grant.
2. **FN-destruction vs PONDER β·Q (§2.2):** the local field needed for A~10⁻³ is 2.3×10⁵× the FN-safe DC ceiling; the regime-bouncing-RF evasion is corpus-acknowledged-open (PONDER ch1:168). Needs a transient-FN integration or Grant's engineering call.

---

## 6. EE-intuition summary (ave-ee-intuition-summary — the 5-beat)

1. **The vacuum is a varactor.** Bias the bond-LC tank with a field and its capacitance moves — same as a DC-biased semiconductor varactor. The bias variable is A = E/E_YIELD on the Axiom-4 quarter-arc.
2. **AVE says it softens; QED says it stiffens.** Under field the AVE vacuum's ε goes *down* (C up, resonance up); the QED vacuum's ε goes *up*. The **sign of the V² coefficient** is the whole discriminator — no knee, no magnitude match. 6 OOM (resonance) / 12 OOM (reflectance).
3. **You read the wiggle as a frequency shift, and Q buys resolution not signal.** Δf₀/f₀ = +¼A²η_eff is set by how much resonator volume the hot spot fills (the dilution); the line-Q just sets how small a Δf₀ you can resolve. The wiggle is +1.76×10⁻¹² (tight) to +1.76×10⁻¹⁵ (nominal).
4. **β and Q_build are two different amplifiers — and field-emission caps the static one.** β=10³ (tip curvature) and Q=10⁴ (resonant build-up) multiply to G_geom=10⁷; the {30,10³,10⁵} "catalog" was symbol-overloading (β, β, β·Q·ferro). But a *static* tip at that local field would field-emit and self-destruct (2.3×10⁵× the FN-safe ceiling) — the RF "regime-bouncing" evasion is the open engineering bet.
5. **A real dielectric also wiggles, so separate by universality.** Swap the material, sweep the tip, cool it — the vacuum term has a *fixed −½ slope at the E_YIELD scale* and doesn't care; the material term moves. The invariant, polarity-symmetric, single-valued, **negative** residual is the vacuum. (This is the exact knob that decides the PONDER-05 quartz question.)

---

## 7. VERDICT

**FORWARD-DISCRIMINATOR-READY-TO-SCAFFOLD (conditional) — the V²-sign autoresonant test is a clean forward discriminator; its existence and direction are robust, but its magnitude/architecture/feasibility are gated on two named, Grant-adjudicable items.**

- **Closed form (the green-field deliverable):** **Δf₀/f₀ = +¼·A_RMS²·η_eff = +¼·(G_geom·V_app/(d·E_YIELD))²·η_eff**, positive (resonance RISES = vacuum softens). Numerically **+1.76×10⁻¹² (optimistic η_eff=10⁻⁶) to +1.76×10⁻¹⁵ (nominal η_eff=10⁻⁹)** at the honest-camp PONDER operating point (G_geom=10⁷, 30 kV, 1 mm). Reproduces Phase-0; regenerates from `qg42_vsign_deltaf.py` (forward-only).
- **Sign = forward discriminator (Class-D-like discriminating power), robust to the √α magnitude (Class-B) uncertainty.** AVE +, QED −, opposite by kernel form. Discrimination ratio 2.895×10⁶ (V²) / 8.381×10¹² (V⁴), exact from constants.py.
- **Detection architecture: resonant-Q autoresonant PLL (10⁻¹⁵ floor)** reaches the nominal Δf₀/f₀ (SNR ≈ 1.8) IN THE HONEST CAMP; cryo-lock-in reaches it only for optimistic tight-resonator geometry; precision-bridge is the characterization tool, 3–6 OOM short of discovery. *(Conditional: if the conflated camp holds, ΔC/C₀ ~90% macroscopic → precision-bridge suffices.)*
- **Vacuum-vs-material separation:** three orthogonal knobs (material swap → zero-Kerr extrapolation; β² hot-spot vs β-flat bulk; T-invariant −½-slope-at-E_YIELD) isolate the universal vacuum term. Resolves the PONDER-05 quartz consistency-vs-emergence question.
- **β/G_geom reconciled:** {30, 10³, 10⁵} = {bare-curvature floor, geometric tip β, β·Q·ferro upper-bound} — symbol-overloading, now decomposed (G_geom = β·Q_build = 10⁷). The "10⁵" is an underived App-F caption; use as upper bound only.

**Two named feasibility risks (Grant-adjudicable; flag-don't-fix, NOT resolved here):**
1. **Reachability fork** — honest camp (Regime I, A~10⁻³, needs resonant-Q) vs conflated camp (0.85 V_yield, macroscopic LCR); ~12 OOM apart; corpus-wide; already flagged BLOCKING in orchestration §10. The SIGN survives the fork; the magnitude/architecture do not.
2. **FN-destruction vs PONDER β·Q** — the A~10⁻³ local field is 2.3×10⁵× the FN-safe DC ceiling; PONDER's regime-bouncing-RF evasion is corpus-acknowledged-open (ch1:168).

**NOT a clean unconditional GO** — the discriminator is real and AVE-distinct, but the build's magnitude, architecture, and electrode-survival are gated on the two flags. **The discriminator's value does not depend on resolving them**: the sign test (does the vacuum soften or stiffen?) is buildable and two-sided regardless of which reachability camp holds. Recommend: scaffold the resonant-Q autoresonant build under the honest-camp assumption, with the reachability fork + FN-evasion surfaced to Grant as the two load-bearing pre-build decisions.

---

## 8. Reuse + verification ledger (every citation re-verified to source this session — verify-before-cite)

| Item | Source (verified 2026-06-04) | Status |
|---|---|---|
| Kernel S(A), δε/ε₀=−A²/2 | `common/universal-saturation-kernel-catalog.md:20` | ✓ exact |
| Four-regime map | `vol4/.../regimes-of-operation.md:23-30` | ✓ exact |
| Bench Regime I, E/E_yield=2.7×10⁻¹⁰ (honest camp) | `regimes-of-operation.md:32` | ✓ exact |
| Bulk-yield sub-femtometer-only (honest camp) | `regimes-of-operation.md:34` + `claim-quality.md:158` | ✓ exact |
| 27.4% @ 0.687, bench@30kV (conflated camp) | `measurement-hierarchy-snr.md:66` | ✓ exact |
| 0.85 V_yield, ΔC/C₀~90%, LCR (conflated camp) | `17_noise_floor_boundary.tex:79-84` | ✓ exact |
| per-node V_yield = most-common reading error | `claim-quality.md:51` + `regimes-of-operation.md:11` | ✓ exact |
| β=10³ tip, Q=10⁴, E_local^peak=4.2×10¹⁴ | PONDER ch1:116,122 + `chiral-thrust-derivation.md:75` | ✓ exact |
| regime-bouncing RF, open-engineering-Q caveat | PONDER ch1:126,168 | ✓ exact |
| FN: A_FN/B_FN/φ, β_crit≈6, β=3/6/50 SAFE/MARG/DESTR | `17_noise_floor_boundary.tex:32,39,49,54` | ✓ reproduced exactly |
| δC=¼C₀(V/V_yield)², 4.57%@0.428 @ 2ω | `parametric-coupling-kernel.md:70` | ✓ exact |
| Ch 15 autoresonant INVALIDATED (60 kV) | `ch15-autoresonant-breakdown/theory.md:8` | ✓ exact |
| 8.381×10¹² / 2.895×10⁶ ratios + √α·E_CRIT=E_YIELD | reproduced from constants.py this session | ✓ exact |
| temporal-classifier (δ_AVE lossless/cyclic) | `common/temporal-saturation-regime-classifier.md` | ✓ applied |

## Cross-references

- Phase-1 prereg: `research/2026-06-04_qg42-phase1-prereg.md`
- Phase-0 result: `research/2026-06-03_qg42-resume-vsign-phase0-result.md`
- Reframe spec: `research/2026-06-03_yield-knee-map-prereg.md`
- Orchestration + reachability flag: `_orchestration/2026-06-03_experimental-protocol-revamp-orchestration.md` §10
- Calc scripts: `src/scripts/vol_4_engineering/qg42_vsign_deltaf.py` (Phase-1), `qg42_vsign_phase0.py` (Phase-0)
- Canonical: `regimes-of-operation.md`, `universal-saturation-kernel-catalog.md`, `17_noise_floor_boundary.tex`, `src/ave/core/constants.py`

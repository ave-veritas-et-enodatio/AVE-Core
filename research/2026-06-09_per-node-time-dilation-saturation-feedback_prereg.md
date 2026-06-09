# PREREG — Per-node TIME DILATION from the saturation feedback (rectified AC clock-slow)

**Date:** 2026-06-09 · **Branch:** `analysis/2026-06-09-saturation-temporal-preregs` (off `main` @ f1f927c8)
**Status:** FROZEN pre-registration (corpus-grep done; no derivation run yet).
**Origin:** Grant 2026-06-09 — *"a derivation for per-node time dilation should be a feedback from local saturation/rectification."* The phased-coil time-dilation thread, made substrate-native.
**Companion prereg:** `2026-06-09_thixotropy-amplitude-dependent-tau_prereg.md`.

---

## 1. Target (one sentence)

Derive per-node **time dilation** as the self-consistent steady-state local saturation under a **symmetric AC drive**, with **Jensen rectification** of the concave clock-kernel as the steady (DC) clock-slow mechanism — replacing the naive `A=E/E_yield` fixed-ratio — resolving (a) the macroscopic-field → per-node-A **feedback fixed point**, (b) the **clock-speed exponent** (a live canonical contradiction, §2a), (c) **ρ̄_cav** as the rarefaction-side fixed point of the same feedback, and predict (d) the **clock-shift-vs-field magnitude** and whether it is a benchtop GR-discriminator.

## 1.5 Physical picture (mechanical, no equations)

- A node under a symmetric AC field A(t)=A₀cos ωt. The clock-kernel is **concave** in A, so the *time-averaged* clock rate sits **below** the unstrained rate — **Jensen's inequality is the rectifier.** An AC coil drive produces a steady DC clock-slow. (A phased toroidal array doesn't need a static field; it rectifies its own AC.)
- **Scalar, not vectorial — and that is the whole point.** The same ⟨S⟩-deficit machinery the corpus built for *thrust* (clm-7tynm2) **failed as thrust** because thrust needs a *direction* and the deficit is even/scalar. Time dilation needs only ⟨S⟩<1 — a scalar. So the deficit that was wasted on thrust is correctly spent on the clock. The refutation of the thrust and the viability of the clock are the **same fact** seen from two sides.
- **Feedback, not a ratio.** As S drops, c_EM=c₀/S rises and the field redistributes (refraction) → local A is the **fixed point** of a loop, not an imposed ratio. This loop *is* the macroscopic→per-node-A mapping.
- **ρ̄_cav = the rarefaction-side fixed point** of the same saturation feedback (companion to the A=1 compression ceiling).
- **Symmetric loading required.** Both ε,μ sectors loaded equally → Z=Z₀ invariant → the gravity-class **clock** (reflectionless); single-sector → Z changes → the asymmetric **Meissner mirror** (a different observable). INVARIANT-S2.

## 2. Corpus state — PARTIAL (with one live contradiction + two green-field pins)

Per the 2026-06-09 corpus-grep:

### 2a. THE CLOCK-SPEED EXPONENT IS CONTRADICTED AT HEAD — flag-for-Grant, resolution-gating

Three disagreeing exponents live in canon simultaneously (clock ∝ (1−A²)^p):

| source | statement | p |
|---|---|---|
| `manuscript/ave-kb/CLAUDE.md` **INVARIANT-S2** (authoritative, cross-volume; clm-8nkvwy) | gravitational time-dilation / Schwarzschild reduction uses **c_shear = c₀√S**; c_EM=c₀/S is the α-speed and must NOT be the clock | **¼** |
| `op14-local-clock-modulation.md:17,31` (A-010 leaf, ON MAIN) | `ω_local = ω_global·√(1−A²) = ω·S` (worked nums at `:83` confirm bare-S) | **½** |
| `op14-local-clock-modulation.md:29` (SAME leaf) | `c_eff = c₀√S`, and `:27` derives the clock from this → ω∝√S | **¼** (self-contradicts `:17`) |
| `04_superluminal_transit.tex:41` (Sleep Pod) | clock set by `c = 1/√(με)` = c_EM = c₀/S | **−½** (inverted; the c_EM error S2 warns against, Pitfall #5) |

**This is corpus-coherence debt, surfaced not resolved here (flag-don't-fix).** My recommendation: **INVARIANT-S2 wins** (highest authority, documents the logged Phase-3-A3 walk-back 2026-05-28 where misusing c_shear in α gave the wrong answer) → **the time-dilation clock tracks c_shear = c₀√S, p=¼**. The op14-leaf self-contradiction (`:17` bare-S vs `:29` √S) and the Sleep-Pod c_EM error are a **separate reconciliation/walk-back** (logged for orchestration). **The derivation cannot commit a magnitude until Grant confirms p.**

### 2b. Jensen rectification — CLOSED, but built for thrust (re-point is the new work)

`chiral-thrust-derivation.md:20,28,45` (clm-7tynm2, confidence 0.55, ON MAIN) + `ch2…/index.md:18`: *"For any AC-driven field E(t)=E₀sin(ωt), Jensen's inequality guarantees ⟨S(E(t))⟩ < S(0)=1 … the deficit δ = 1−⟨S⟩ is the rectification factor … δ = A_peak²/4 = A_RMS²/2."* The δ=A²/4 coefficient is the **p=½ (⟨S⟩) result**; re-pointing to ⟨clock⟩ with p=¼ gives δ=A²/8. **The ¼-vs-⅛ coefficient is gated on §2a.** Classification: structural-ingredient — the engine exists; re-pointing it from ⟨ε_eff⟩(thrust) to ⟨clock⟩(dilation) + fixing the coefficient is new.

### 2c. Closed / partial / green-field map

- ρ̄_cav rarefaction relation `c_eff² = c₀²(1+ρ̄/(1−ρ̄²))`, ρ̄∈[−1,1], Z_eff=Z₀/S(ρ̄): **CLOSED** (`04_superluminal_transit.tex:86,89`, Ax4-derived). The **ρ̄_cav=−1/φ fixed-point value: GREEN-FIELD** (not in canon anywhere — raising it is new work).
- macro→per-node-A self-consistent feedback fixed point: **GREEN-FIELD**.
- per-node-vs-apparatus + E_yield≈1.13×10¹⁷ V/m: **CLOSED, recently hardened** (2026-06-04 walk-back; `op14-local-clock-modulation.md:106`: 30 kV across quartz → vacuum per-node A₀=10⁻⁷–10⁻¹⁰ → ~0 modulation; appreciable needs facility ~8×10¹⁶ V/m).
- Sleep Pod cavity + symmetric/Meissner loading: **CLOSED** (`04_superluminal_transit.tex:38-56`; INVARIANT-S2).
- existing null: **Δc/c < 10⁻¹⁸** cavity comparisons (`sagnac-parallax.md:30`) — a hard constraint the prediction must respect.

## 3. substrate-native-check (FIRST)

- **Dynamics/sector:** time-averaged saturation of the LC tank under AC drive; the clock is the **shear/mechanical** oscillator (c_shear sector, pending §2a). Symmetric loading keeps Z=Z₀ (SYM-class, reflectionless gravity); the drive must be symmetric-both-sector, else it's the Meissner-mirror observable.
- **Objective:** ⟨clock-kernel⟩ over a drive cycle (the rectified DC offset) + the self-consistent A fixed point — NOT energy minimization.
- **Coordinate system:** real-space per-node strain A; clock is real-space time-domain. The per-node strain (NOT apparatus field) is load-bearing — the 2026-06-04 walk-back is the cautionary anchor.
- **Reactance + local clock:** Checkpoints 5 (saturation-modulated local clock) + 6 (reactance pair) both fire; report ω_local at the load-bearing site vs A²_local.

## 3.5 Dimensional analysis (mandatory — magnitude prereg, ave-prereg v1.1 Step 3.5)

**Ingredients (canonical primitives, from `src/ave/core/constants.py` + cited leaves):**
- E_yield ≈ 1.13×10¹⁷ V/m, V_yield ≈ 43.65 kV, ℓ_node ≈ 0.386 pm; per-node `A₀ = E_local·ℓ_node/V_yield` (`op14-local-clock-modulation.md:106`).
- Clock deficit (leading order, clock ∝ (1−A²)^p, AC A(t)=A₀cosωt): `⟨(1−A²)^p⟩ ≈ 1 − p·⟨A²⟩ = 1 − p·A₀²/2`, so **δ_clock ≈ p·A₀²/2**.
  - p=½ (bare-S): δ = A₀²/4 (matches the corpus ⟨S⟩-deficit).
  - p=¼ (c_shear, recommended): δ = A₀²/8.
- β·Q amplification chain (`chiral-thrust-derivation.md:45`): β=10³ (geometric tip concentration), Q=10⁴ (cavity) → `E_local^peak = βQE_macro√2 ≈ 4.24×10¹⁴` V/m (from E_macro~4×10⁷) → **A_peak = 3.75×10⁻³**.

**Numerical evaluation:**
- δ_clock(p=¼) = A_peak²/8 = (3.75×10⁻³)²/8 ≈ **1.8×10⁻⁶** (≈ 1.8 ppm).
- δ_clock(p=½) = A_peak²/4 ≈ **3.5×10⁻⁶** (≈ 3.5 ppm) — matches the corpus thrust δ.

**Sanity-check vs anchors + the load-bearing caveat:**
- vs detection floor Δc/c < 10⁻¹⁸ (`sagnac-parallax.md:30`): a ppm shift is **~10¹²** above floor.
- vs GR: a few-T / ~10⁸ V/m field's energy density gives GR time-dilation ~G·u/c⁴ ~ **10⁻⁴³** → AVE-vs-GR discriminator of **~37 OOM** *if* the per-node loading is real.
- **CRUX caveat (per-node-vs-apparatus):** the 2026-06-04 walk-back established that an apparatus field gives vacuum per-node A₀=10⁻⁷–10⁻¹⁰ *without* amplification, and re-classified the PONDER-05 "0.687" as the **material's** coefficient, NOT the vacuum's. So the ppm prediction **hinges on whether the β·Q-amplified field loads the VACUUM per-node strain or merely the material** — the exact trap that walk-back closed. This is the make-or-break check, not a footnote.
- **Existing-null consistency:** standard cavity comparisons already bound Δc/c<10⁻¹⁸; if AVE predicted ppm at fields *those* experiments used, it would already be falsified. It isn't — because standard cavities don't engineer the β·Q tip+cavity amplification to 4×10¹⁴ V/m. The null bounds, but doesn't kill, the prediction; it pushes the honest answer toward "needs deliberately-engineered fields" (which is the testable regime).

## 4. Prediction (pre-committed)

With p=¼ (pending Grant): the per-node time-dilation clock-slow is `δ_clock ≈ A₀²/8`, where A₀ is the **fixed point** of the field↔saturation feedback (not E_local/E_yield naïvely). I predict (i) the feedback fixed point is *self-limiting* (refraction defocuses as S drops, capping A₀ below the naive value) → the achievable δ is **at or below** the β·Q estimate; (ii) ρ̄_cav=−1/φ emerges as the rarefaction-branch fixed point of the same map; (iii) the magnitude lands in **Outcome A (benchtop discriminator)** *only if* the β·Q-amplified field genuinely loads vacuum per-node strain — otherwise **Outcome B (facility-only)**.

## 5. Discriminating outcomes

- **A — REAL, benchtop GR-discriminator:** exponent pinned; feedback fixed point gives a per-node A from achievable β·Q fields yielding δ_clock ≫ 10⁻¹⁸; AVE predicts ppm-to-detectable where GR predicts ~10⁻⁴³ → a clean bench falsification test. The chord: a real novel prediction, distinct from the refuted thrust (scalar clock, not vectorial thrust).
- **B — REAL but facility-only:** per-node-vs-apparatus (the 0.687 walk-back) means achievable fields give vacuum A₀~10⁻⁷ → δ~10⁻¹⁴ or below; real effect, no bench discriminator without facility fields ~8×10¹⁶ V/m.
- **C — NOT AVE-distinct:** at the achievable magnitude the predicted shift reduces to standard QED vacuum birefringence / nonlinear-optics clock-pulling already measured and SM-consistent → discrimination-check fails.

## 6. Falsifier

A cavity clock-comparison in a deliberately β·Q-engineered resonant field showing **no** shift at the AVE-predicted level (with per-node loading established) falsifies AVE per-node time dilation. The existing Δc/c<10⁻¹⁸ null already constrains the model toward B/facility unless engineered tip+cavity fields are used.

## 7. Guards

- **Resolve §2a (exponent) before any magnitude.** Hard gate; Grant adjudicates p.
- **Per-node-vs-apparatus discipline** (the 0.687 / 2026-06-04 walk-back) — do NOT claim vacuum loading from a material field; this is the make-or-break check.
- **Symmetric loading** (Z=Z₀ clock, not the Meissner mirror) — else it's a different observable.
- **discrimination-check vs QED vacuum birefringence + standard cavity nonlinearity**, and **respect the Δc/c<10⁻¹⁸ null** as a constraint.
- ρ̄_cav, the rarefaction relation, E_yield, β·Q all from canon — not tuned.

## 8. Skills + deliverables

- **Skills:** substrate-native-check (FIRST) · ave-canonical-leaf-pull (Saturation + Power + Boundary + Propagation-speed classes) · ave-canonical-source (E_yield, V_yield, ℓ_node, ρ̄_cav, c from constants.py) · ave-analytical-tool-selection (Saturation §3 + Power §5 + Mode §6) · ave-driver-script-honesty (the per-node-vs-apparatus + ⟨S⟩-deficit reported) · **ave-engineering-program-rigor** (figures + amplitude/frequency/Q sensitivity sweep — the sweep IS the rescue-fill discriminator for the magnitude claim) · ave-discrimination-check (vs QED birefringence) · consistency-vs-emergence.
- **Deliverables:** `2026-06-09_per-node-time-dilation-saturation-feedback_result.md` (A/B/C + the feedback fixed-point + ρ̄_cav + the magnitude with the per-node-vs-apparatus verdict + DERIVED/VERIFIED/BLOCKED); analytic derivation (Jensen re-point + feedback fixed point) → driver (sweep A₀, ω, Q; plot δ_clock response surface + the field↔A fixed point + locate ρ̄_cav) per ave-engineering-program-rigor. Commit on this branch; do NOT push/merge.

---

### Appendix — the two-sided fact (why this prereg and the clm-7tynm2 walk-back are one event)

The Jensen ⟨S⟩-deficit (`chiral-thrust-derivation.md`) is **even in A → scalar**. A scalar cannot be a net force (thrust needs odd/directional) → the thrust is refuted (Phases 1–5). A scalar **is** exactly a clock rate (dilation needs only ⟨S⟩<1) → the clock effect is viable. Same mechanism, opposite verdicts, because thrust and dilation have opposite tensor rank. The clm-7tynm2 walk-back should therefore **retire the thrust observable while preserving the Jensen-rectification mechanism**, which this prereg re-homes onto the clock.

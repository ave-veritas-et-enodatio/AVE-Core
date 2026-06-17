# FROZEN FORWARD PRE-REGISTRATION — BH Mode-Dependent-Horizon Shear-Echo Discriminator

**Status:** FROZEN. SHA-pinned to `main` @ `04bcb4ac` (post #277/#278).
**Frozen:** 2026-06-17.
**Branch:** `analysis/2026-06-17-bh-shear-echo-prereg`.
**Discipline:** `ave-prereg` (frozen bins + SHA-pin + falsifiers) · `ave-discrimination-check` (GR/SM counterfactual per prong) · substrate-first (every number DERIVES from the canonical chain OR is TAGGED engineering/fit) · `consistency-vs-emergence`.

> **PURPOSE.** Stake AVE's mode-dependent-horizon black-hole discriminator as a SHA-pinned forward pre-registration with parameter-free derivations and per-prong falsifiers, and HONESTLY adjudicate — PER PRONG — whether each prediction is **FORCED** (parameter-free → a *chord*) or **FIT** (calibration-tuned → an *echo*). The adjudication is the deliverable. A fit tagged as forced is the failure mode this document exists to avoid.

---

## 0. Physics basis (settled — cited, not re-derived here)

AVE's black-hole horizon is **mode-dependent**: the same radius reflects differently in different substrate channels.

- **EM / light channel — transparent, `Γ_EM = 0`.** Under SYM gravity both `μ'(r)` and `ε'(r)` scale identically with `n(r)`, so `Z_EM(r) = √(μ'/ε') = Z₀` is invariant at all radii. No EM impedance mismatch, no EM reflection. Light is *index-captured* (refracted), not reflected; the photon sphere stays at the GR location `r_ph = 3GM/c²`. Canonical: [`electron-bh-isomorphism.md:24,77`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md), [`ave-bh-horizon-area-theorem.md:77`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md).
- **Shear / GW channel + bulk channel — perfect reflector, `Γ_shear = Γ_bulk = −1`.** At the saturation boundary the topology melts: `G_shear → 0 ⟹ Z_shear = ρ·c_shear → 0 ⟹ Op3 short ⟹ Γ_shear = −1`. Gravitational waves (transverse shear modes) cannot propagate in the ruptured interior; they reflect totally. Canonical: [`electron-bh-isomorphism.md:30-36`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md) (clm-ir8h78).

**Two radii.**

| Radius | Value | Role | Channel |
|---|---|---|---|
| `r_s` | `2GM/c²` | EM / light horizon (Schwarzschild) | EM (`Γ_EM = 0`, transparent) |
| `r_sat` | `7GM/c² = 3.5·r_s = r_s/ν_vac` | shear + bulk reflector | shear+bulk (`Γ = −1`) |

with `ν_vac = 2/7` the K4 Poisson ratio, so `r_sat/r_s = 1/ν_vac = 3.5` and the coefficient `7 = 2/ν_vac`. Canonical: [`ave-bh-horizon-area-theorem.md:16,20`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md) (clm-law1ho).

**Strain profile + shear speed (load-bearing for Prong 1).**

- Principal radial strain: `ε₁₁(r) = 7GM/(c²r) = r_sat/r`, so `ε₁₁(r_sat) = 1` exactly. Canonical: [`electron-bh-isomorphism.md:19`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md).
- Shear group velocity: `c_shear(r) = c·(1 − ε₁₁²)^(1/4) → 0` at `r = r_sat`. Canonical: [`electron-bh-isomorphism.md:33`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md).

**CODATA-derived constants are INPUTS, not outputs (substrate-first tag).** `G`, `c`, `M_remnant` are taken from CODATA / the LIGO catalog. Per `consistency-vs-emergence`, any number computed from them is at best **consistency-class** unless it is a pure dimensionless ratio forced by the substrate. `ν_vac = 2/7` is the one parameter-free substrate quantity entering below.

---

## 1. PRONG 1 — GW post-merger echo delay

### (i) Prediction

After the prompt ringdown, GW energy that crosses inward reflects off the `Γ_shear = −1` saturation wall at `r_sat = 7GM/c²` and re-emerges, producing a post-merger **echo train**. The pre-registered observable is the round-trip echo delay `Δt` for a remnant of mass `M`.

**Frozen numeric prediction (GW150914 remnant, `M = 62 M_⊙`, the corpus value at [`ave-merger-ringdown-eigenvalue.md:58`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md)):**

$$\boxed{\;\Delta t_{\rm AVE}\;\approx\;3\text{–}10\ \text{ms}\quad(\text{order }2r_{\rm sat}/c = 4.28\ \text{ms})\;}$$

### (ii) Derivation — parameter-free, done properly (the slow region matters)

A shear wave propagates at the *local* speed `c_shear(r) = c·(1 − ε₁₁²)^(1/4)` with `ε₁₁(r) = r_sat/r`. The round-trip ("tortoise") delay between the inner reflector `r_sat` and an outer turning point `r_out` is

$$\Delta t \;=\; 2\int_{r_{\rm sat}}^{r_{\rm out}}\frac{dr}{c_{\rm shear}(r)} \;=\; \frac{2}{c}\int_{r_{\rm sat}}^{r_{\rm out}}\frac{dr}{\bigl(1-(r_{\rm sat}/r)^2\bigr)^{1/4}}.$$

**The integrand diverges at `r = r_sat` (because `c_shear → 0`) — but the integral is FINITE.** Near the wall set `r = r_sat(1+x)`, `x → 0⁺`: then `1 − ε₁₁² ≈ 2x`, so the integrand `∝ x^(−1/4)`, exponent `> −1` ⟹ integrable. The wall-slowdown is a real, finite *enhancement* over the flat light-crossing time `2r_sat/c`, **not** a divergence. This is the non-trivial point the task flagged: the slow region near the wall contributes but does not blow up.

Evaluating numerically (`G, c` CODATA; `M = 62 M_⊙`; `r_sat = 7GM/c² = 6.41×10⁵ m`; driver `src/scripts/vol_3_macroscopic/bh_shear_echo_delay.py`):

| `r_out / r_sat` | `Δt` (ms) | comment |
|---|---|---|
| `1.1` | `0.87` | thin wall skin |
| `1.5` | `3.06` | |
| `2.0` | `5.42` | |
| `3.0` | `9.90` | |
| flat light-crossing `2r_sat/c` | `4.28` | reference scale |

The natural near-horizon cavity (inner wall `r_sat`, outer turning point at a few `r_sat`) gives **`Δt ~ 3–10 ms`, parameter-free** from `r_sat = 7GM/c²` + the `c_shear` profile + `M`. Both candidate parameter-free outer reflectors in the corpus — the GR photon-sphere barrier `r_ph = 3GM/c² = 3r_g` and the ringdown cavity dimension `r_eff = 49M_g/9 = 5.44r_g` — lie **inside** `r_sat = 7r_g`, so there is no parameter-free outer reflector *outside* `r_sat`; the delay scale is set by the wall vicinity, i.e. the few-ms band.

### (iii) CRUX — does `Δt` match the observed ~0.29 s parameter-free? NO.

The Abedi–Dykaar–Afshordi echo spacing is `~290 ms` ([`existing-experimental-signatures.md:42`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/existing-experimental-signatures.md)). AVE's parameter-free near-horizon delay is `~4 ms`. **The observed value is ~68× larger than the AVE forced prediction.**

To reach `0.29 s` with the AVE `c_shear` profile, the outer reflector would have to sit at `r_out ≈ 68·r_sat ≈ 479·r_g ≈ 4.4×10⁷ m` — deep in the GW wave zone, where there is no reflector. There is no parameter-free way to put it there.

**Contrast with standard GR exotic-compact-object (ECO) echo models** — the decisive `ave-discrimination-check`. In ECO models the reflector sits a *tunable* proper distance `δ` just **outside** `r_s`, and the tortoise delay is **logarithmically divergent**, `Δt ≈ (2r_s/c)·|ln(δ/r_s)| + const`, so `δ` is a free knob that can be tuned to reproduce *any* delay including 0.29 s. **AVE has no such knob:** its reflector is at the *fixed, parameter-free* radius `r_sat = 7GM/c²`, **outside** `r_s`, with no log-divergence. AVE's `Δt` is sharply predicted at `~4 ms` and **cannot be tuned to 0.29 s**. This is exactly what makes Prong 1 a clean falsifier rather than a fittable curve — and what makes the ~0.29 s number, if real, a *problem* for AVE rather than a confirmation of it.

**Disambiguation (do not confuse with the ringdown `τ`).** The AVE echo *delay* `~4 ms` is numerically close to — but physically distinct from — the GW150914 ringdown *damping time* `τ ≈ 4.0 ms` ([`ave-merger-ringdown-eigenvalue.md:64`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md), `τ_v2 = 3.95 ms`). `τ` is the e-folding decay time of the *prompt* QNM; `Δt` is the *spacing between successive echo bursts*. That they land in the same band for a `62 M_⊙` remnant means an echo at the AVE-predicted delay would arrive *within roughly one damping time of the prompt ringdown* — i.e. it would overlap the late ringdown and be hard to resolve as a *separate* echo, which is itself an observational caveat on F1a. (The Abedi+ 0.29 s sits at `~73 τ`, cleanly separated — and `~68×` beyond the AVE delay.)

### (iv) FALSIFIER (frozen)

- **F1a (positive-detection bin):** A confirmed post-merger GW echo train at `Δt = 3–10 ms` (scaling `∝ M`) for a stellar-mass BBH remnant **CONFIRMS** Prong 1.
- **F1b (the live tension):** A confirmed echo at `Δt ≈ 0.29 s` (the Abedi+ spacing), with **no** companion echo in the `3–10 ms` band, **FALSIFIES** the AVE parameter-free echo-delay prediction — the `~68×` gap is not bridgeable without a free parameter AVE does not have.
- **F1c (null bin):** No echo at any delay (clean LIGO/Virgo O4–O5 stacked null at the required sensitivity) is **consistent with** GR-Kerr absorption and **disfavors** the `Γ_shear = −1` reflector (the wall should produce *some* echo); it weakens but does not by itself kill the mode-dependent-horizon picture (the echo amplitude depends on the prompt-ringdown energy fraction that crosses inward, not derived here).

### (v) VERDICT — FORCED (chord), and the forced value currently FAILS the retrospective 0.29 s

**FORCED / parameter-free — this is a chord at the level of *being a genuine zero-knob prediction*.** The delay `Δt ~ 4 ms` falls out of `r_sat = 7GM/c²`, the `c_shear` profile, and `M`, with `ν_vac = 2/7` the only substrate input. There is no calibration knob.

**But the honest result is that the forced value DISAGREES with the retrospective ~0.29 s by ~68×.** The previously-asserted "AVE predicts the LIGO echoes" framing (corrected in §0 and in the overclaim fix below) **conflated AVE's mechanism (a shear reflector exists) with AVE's *quantity* (the delay).** AVE's mechanism predicts echoes; AVE's parameter-free *delay* is `~4 ms`, not `0.29 s`. Banking the 0.29 s as an AVE confirmation would have been a **fit-masquerading-as-forced** error — the exact failure mode this prereg exists to catch. The chord is real (zero-knob prediction); whether it *survives* is a live empirical question that the ~4 ms band, not 0.29 s, must be tested against.

---

## 2. PRONG 2 — Iron-Kα / accretion-disk inner edge at 7GM (not GR ISCO 6GM)

### (i) Prediction

Accreting matter cannot exist inside `r_sat = 7GM/c²` (Regime-IV ruptured topology — matter is unsupported by the melted lattice). So the **inner edge of an accretion disk sits at or just outside `r_sat = 7GM/c²`**, not at the GR ISCO. For a Schwarzschild (zero-spin) hole this is a sharp, parameter-free discriminator:

$$\boxed{\;r_{\rm in}^{\rm AVE}\;=\;r_{\rm sat}\;=\;\frac{7GM}{c^2}\;=\;7\,r_g\qquad\text{vs}\qquad r_{\rm ISCO}^{\rm GR,\,a_*=0}\;=\;6\,r_g.\;}$$

Observable via X-ray reflection spectroscopy of the inner-disk **Fe-Kα** line profile and via continuum-fitting; both infer `r_in` from the relativistic broadening / disk temperature. Canonical basis: [`ave-bh-horizon-area-theorem.md:84`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md), [`lattice-extreme-bh-rationality.md:75,91`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md), [`ave-compactness-limit.md`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-compactness-limit.md).

### (ii) Derivation — the radius is parameter-free, `7 = 2/ν_vac`

`r_sat` is fixed by the saturation condition `ε₁₁(r_sat) = 7GM/(c²r_sat) = 1`, i.e. `r_sat = (2/ν_vac)·(GM/c²) = 7GM/c²` with `ν_vac = 2/7` the K4 Poisson ratio (Buchdahl-bound derivation, [`ave-bh-horizon-area-theorem.md:20,35`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md)). The **ratio** `7/6 = 1.167` (AVE inner edge vs GR `a_*=0` ISCO) is a pure dimensionless number, free of `G`, `M`, CODATA — **parameter-free**. There is no calibration step.

### (iii) CAVEAT — the GR ISCO is spin-dependent; the discriminator is clean only with known spin

The GR Kerr ISCO is **not** fixed at `6 r_g`; it runs with spin `a_*` (Bardeen–Press–Teukolsky):

| `a_*` | GR ISCO prograde (`r_g`) | GR ISCO retrograde (`r_g`) |
|---|---|---|
| `0.0` | `6.00` | `6.00` |
| `0.5` | `4.23` | `7.56` |
| `0.67` (GW150914-like) | `3.53` | `8.06` |
| `0.9` | `2.32` | `8.72` |
| `0.998` | `1.24` | `8.99` |

**AVE's `r_sat = 7 r_g` is NOT a universal floor above all GR ISCOs.** It sits *above* every **prograde** GR ISCO (6 → 1.2 `r_g`), but **below** the GR **retrograde** ISCO for `a_* ≳ 0.45` (which reaches ~9 `r_g`). So:

- **Prograde / low-spin discs:** the AVE 7 `r_g` edge lies clearly *outside* the GR ISCO (gap 1–6 `r_g`, growing with spin) — clean discriminator.
- **Retrograde high-spin discs:** GR puts the inner edge *outside* 7 `r_g`, so the sign of the AVE–GR offset flips — the discriminator is degenerate or inverted unless spin and disc sense are independently known.

**Open sub-question (flagged, not resolved here): does `r_sat` itself co-vary with spin?** The Kerr-corrected *ringdown* cavity `x_sat(a_*) = 2 + 5·r_ph⁺/(3M)` ([`ave-merger-ringdown-eigenvalue.md:33`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md)) shrinks the *shear cavity* with spin — but that is the QNM eigenmode cavity, **not** the matter-floor `r_sat`. The matter floor is set by `ε₁₁ = 1`, and whether frame-dragging shifts the *strain = 1 surface* (making the matter `r_sat` spin-dependent like the shear cavity) is **not derived in the corpus**. This prereg therefore freezes the discriminator only for the **`a_* = 0` / low-spin / independently-known-spin** case, where `r_sat = 7 r_g` is unambiguous. Driver: `src/scripts/vol_3_macroscopic/bh_disk_inner_edge_isco.py`.

### (iv) FALSIFIER (frozen)

- **F2 (kill):** For a BH with **independently measured low/zero spin** (or jointly fit `a_*` + `r_in`), a measured Fe-Kα / continuum-fitting inner edge **consistent with the GR Kerr ISCO and inconsistent with `7 r_g`** FALSIFIES the AVE matter-floor at `r_sat`. Concretely: an `a_* ≈ 0` system with `r_in = 6 r_g` (GR) vs `7 r_g` (AVE) — the `7/6` offset is the frozen signature.
- **F2-degenerate bin (excluded from the kill):** retrograde high-spin systems, where GR ISCO `> 7 r_g`, are NOT scored as falsifiers (the offset sign flips; the discriminator is uninformative there).

### (v) VERDICT — FORCED (chord) in radius; discriminating power is conditional on spin knowledge

**The radius `r_sat = 7GM/c²` and the ratio `7/6` are FORCED / parameter-free** (`7 = 2/ν_vac`, `ν_vac = 2/7` substrate-derived). This is a genuine chord at the level of the predicted number.

**But the *discriminator's* power is conditional**, not the prediction's parameter-freedom: because the GR comparison target (the ISCO) is spin-dependent and the AVE 7 `r_g` is not universally outside it, the clean test requires independently-known (or jointly-fit) spin, and is degenerate for retrograde high-spin systems. Honest scope: a parameter-free *radius* (chord), wrapped in a *spin-conditional* discrimination window. Not an echo — but not an unconditional kill-shot either.

---

## 3. PRONG 3 — Information return (CONDITIONAL — pending task-#15 entropy-channel adjudication)

> **STATUS: CANDIDATE / conditional-pending-task-#15. NOT a frozen falsifier.** This prong is recorded as a *candidate* prediction, explicitly gated on an unresolved adjudication. It is NOT banked as a chord, and no falsifier bin is frozen for it.

### (i) Candidate prediction

In GR, matter crossing the horizon is causally lost (information paradox). In AVE the shear/bulk reflector is `|Γ_shear| = 1` — a **lossless, total reflection**, not an absorbing sink. A lossless reflector returns the wave; the matter/shear-sector information modulating the in-going shear wave is **reflected back out** (carried on the echo train of Prong 1), not erased. So AVE *candidate*-predicts **no shear-sector information loss at a BH horizon**.

### (ii) Why this is CONDITIONAL, not forced — the entropy-channel fork (task-#15)

The horizon entropy in AVE is the geometric operator `Ŝ = −k_B Σ_i ln(1 − |Γ_i|²)` ([`four-entropy-distinction.md:27`](../manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/four-entropy-distinction.md), clm-4o0f0h). **The value of `Ŝ` — and hence whether information is erased, preserved, or the operator even converges — depends entirely on WHICH channel's `Γ` enters at the horizon, and that is unadjudicated.** The corpus already exhibits three mutually inconsistent answers at the *same* surface `r_sat`:

| Channel / picture | `|Γ|²` at horizon | `Ŝ` per cell | Information verdict |
|---|---|---|---|
| EM / symmetric (`Γ_EM = 0`) | `0` | `−ln(1) = 0` | no structure; "erased / dissipative sink" ([`four-entropy-distinction.md:21,51`](../manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/four-entropy-distinction.md)) |
| A-B sublattice interface | `1/2` | `−ln(1/2) = ln 2` | area-law `S = A ln2 / ℓ_node²` (one bit/cell) |
| **shear / bulk (`Γ_shear = −1`, this prereg's reflector)** | `1` | `−ln(1 − 1) = +∞` | **operator DIVERGES** |

The info-return claim rides on reading the **shear channel** (`|Γ| = 1`), where the entropy operator **`−k_B ln(1 − |Γ|²)` diverges**. A divergent per-boundary entropy is not a finished result — it signals the operator needs a regularization / a different channel assignment at the horizon, which is the open work. Picking the shear channel to bank "information returns" while the *same* channel makes `Ŝ → ∞` would be circular. The corpus first-law `T·dS = dE` is itself flagged open (A-002, [`ave-bh-horizon-area-theorem.md:91`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md): "first-law-style `T·dS = dE` requires importing standard equipartition that AVE rejects"), and the four-entropy adjudication ("which of the 3 `Ŝ` values is the physical horizon entropy") is unresolved.

**Task-#15 is precisely: which channel's `Γ` enters the horizon entropy operator?** Until that is adjudicated, the information-return prediction has no determinate sign and no frozen falsifier.

### (iii) FALSIFIER

**None frozen.** A falsifier would require the entropy-channel adjudication first. Recorded as a candidate only, per Rule 11 (do not bank a chord on an unresolved adjudication) and the substitution-not-retraction discipline (Rule 12 / A47 v11b — no refilling the slot with an unverified mechanism).

### (iv) VERDICT — UNDECIDED (neither chord nor echo); blocked on task-#15

Not classifiable as forced or fit. The *mechanism* (lossless `|Γ|=1` reflection ⟹ no absorption) is consistent with the rest of the framework, but the *information-return prediction* and any horizon-entropy number depend on the unadjudicated entropy-channel assignment, where the operative channel (`shear`, `|Γ|=1`) currently makes `Ŝ` diverge. **Held open. Do not headline.**

---

## 4. What the corpus already had vs what this prereg adds

**Already in the corpus (cited + built on, NOT re-derived):**

- `r_sat = 7GM/c² = 3.5·r_s = r_s/ν_vac`, `ε₁₁(r_sat) = 1`, factor `7 = 2/ν_vac`, `ν_vac = 2/7` — [`ave-bh-horizon-area-theorem.md`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md) (clm-law1ho).
- Mode-dependent horizon: `Γ_shear = Γ_bulk = −1` (reflector) while `Γ_EM = 0` (transparent); `c_shear(r) = c(1−ε₁₁²)^(1/4)`; strain profile `ε₁₁(r) = 7GM/(c²r)` — [`electron-bh-isomorphism.md`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/electron-bh-isomorphism.md) (clm-ir8h78).
- LIGO ringdown closure: `ω_R M_g = 18/49`, Kerr-corrected `x_sat(a_*)`, three-event PASS — [`ave-merger-ringdown-eigenvalue.md`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-merger-ringdown-eigenvalue.md) (clm-395gps). **Note: ringdown is already closed; this prereg does NOT touch it.**
- Iron-Kα inner-edge at `7GM` listed as a *surviving discriminator* — [`ave-bh-horizon-area-theorem.md:84`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md), [`lattice-extreme-bh-rationality.md:91`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md).
- GW echoes mentioned as a candidate — [`ave-bh-horizon-area-theorem.md:85`](../manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md) ("worth scoping if LIGO O4-O5 reaches sensitivity") — and as a retrospective signature in [`existing-experimental-signatures.md:40-48`](../manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/existing-experimental-signatures.md).
- The geometric entropy operator `Ŝ = −k_B Σ ln(1−|Γ_i|²)` and its three-valued horizon ambiguity — [`four-entropy-distinction.md`](../manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/four-entropy-distinction.md) (clm-4o0f0h).

**What this prereg ADDS (new):**

1. **The first parameter-free derivation of the GW echo *delay*** (Prong 1) — the tortoise round-trip through the `c_shear → 0` wall. No such derivation existed anywhere in the corpus; the GW echo was only ever mentioned as a *mechanism* ("echoes are predicted"), never with a *quantity*. The honest result — `~4 ms`, ~68× short of the retrospective 0.29 s — converts a vague "AVE predicts the LIGO echoes" claim into a sharp, falsifiable, and currently-failing forward number.
2. **The frozen SHA-pinned forward stake** with per-prong falsifier bins (F1a/F1b/F1c, F2) — moving the echo + Iron-Kα from "surviving discriminator" prose to pre-registered, dated, hash-pinned predictions.
3. **The forced-vs-fit adjudication per prong** (the consistency-vs-emergence classification applied to BH observables): Prong 1 FORCED-but-failing, Prong 2 FORCED-radius / spin-conditional-discrimination, Prong 3 UNDECIDED-pending-task-#15.
4. **The explicit GR-counterfactual** per prong (ECO log-divergent tunable delay vs AVE fixed `r_sat`; spin-dependent Kerr ISCO vs AVE `7 r_g`) — the `ave-discrimination-check` that the corpus prose lacked.
5. **The overclaim fix** (§6 below): correcting the live "phenomenal empirical validation" wording that treated the retrospective 0.29 s as a confirmation.

---

## 5. Summary table — forced-vs-fit verdicts + falsifiers

| Prong | Prediction | Forced or Fit? | Falsifier (frozen) | Status |
|---|---|---|---|---|
| **1 — GW echo delay** | `Δt ~ 3–10 ms` (`∝ M`; GW150914 `≈ 4 ms`) | **FORCED** (parameter-free from `r_sat = 7GM/c²` + `c_shear` profile; no knob) | F1b: confirmed echo at `0.29 s` with no `3–10 ms` companion ⟹ FALSIFIED | **Chord (zero-knob), but forced value DISAGREES with retrospective 0.29 s by ~68×** |
| **2 — Disk inner edge** | `r_in = r_sat = 7 r_g` (vs GR ISCO; `7/6` at `a_*=0`) | **FORCED radius** (`7 = 2/ν_vac`); **discrimination spin-conditional** | F2: known-low-spin BH with `r_in` consistent with GR ISCO, not `7 r_g` ⟹ FALSIFIED | Chord in radius; clean only for known/low spin (degenerate retrograde high-spin) |
| **3 — Information return** | shear info reflected, not erased | **UNDECIDED** — gated on task-#15 entropy-channel | none frozen | **CANDIDATE / conditional. Do not bank.** |

### Frozen-bin discipline note

The single mechanism — a fixed, parameter-free `Γ_shear = −1` reflector at `r_sat = 7GM/c²` with no tunable wall location — is what makes Prong 1 a *clean* falsifier (it cannot be fit to 0.29 s) and simultaneously what makes the current ~68× disagreement a genuine tension rather than a free-parameter mismatch. Per Rule 11 (honest closure): the right reaction to the ~4 ms-vs-0.29 s gap is to record it as a live tension and freeze the `3–10 ms` band as the thing to test — **not** to introduce a wall-location free parameter to rescue the 0.29 s match.

---

## 6. Overclaim fix (Rule 12) — `existing-experimental-signatures.md:48`

The live leaf calls the LIGO echo "phenomenal empirical validation of the `Γ = −1` tensor bounds" — treating the *retrospective, contested* ~0.29 s echo as a *validated confirmation*. Corrected to **predicted-not-validated** per this prereg's finding (the AVE parameter-free delay is `~4 ms`, not 0.29 s; the 0.29 s is retrospective and, at face value, in *tension* with the forced AVE delay, not a validation of it). A Rule-12 banner preserves the original prose and points here. See §6 propagation in the commit.

---

## Drivers (Rule 10 — empirical, run at freeze time)

- `src/scripts/vol_3_macroscopic/bh_shear_echo_delay.py` — Prong 1 tortoise round-trip (reproduces the `3–10 ms` band + the `68×` / `479 r_g` figures).
- `src/scripts/vol_3_macroscopic/bh_disk_inner_edge_isco.py` — Prong 2 AVE `7 r_g` floor vs GR Kerr ISCO spin sweep (reproduces the clean/degenerate spin windows).

Both import `G`, `C_0`, `M_SUN`, `NU_VAC` from `ave.core.constants` (`ave-canonical-source`: no hard-coded constants).


---

## 5. Summary table — forced-vs-fit verdicts + falsifiers

<!-- skeleton -->

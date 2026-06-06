# PRE-REGISTRATION (FROZEN) — Gravity sign via reactive LC frequency-modulation

**Date:** 2026-06-05
**Branch:** `analysis/gravity-sign-freq-modulation` (off `origin/main` @ `0e3890df`)
**Class:** Internal-COHERENCE + intuition-correction (Class C). **NOT** a distinctness claim — the corpus already classifies weak-field gravity (lensing / Shapiro / perihelion) as "AVE = GR at O(GM/c²r), no AVE-distinct observable." This work asks only whether Grant's reactive-frequency-modulation framing yields the correct lensing SIGN, the canonical factor-2, and per-sector bench/gravity consistency — and whether it is internally coherent with the existing canonical gravity sector.
**Companion:** `research/2026-06-05_gravity-ppn-coherence-result.md` (on `origin/analysis/gravity-ppn-coherence`) — separate internal-coherence audit of the same gravity sector (PPN γ/β). This prereg reuses its verified citations and re-queues its W2 (redshift slope) as our W2.

---

## GRANT'S PRINCIPLE (the lever — hypothesis to CONFIRM; derive cleanly either way)

Saturation modulates the per-node LC frequency ω = 1/√(L_eff·C_eff) **reactively** — a frequency/phase re-tuning of a *lossless tank at INVARIANT impedance* Z = √(L_eff/C_eff) — **NOT** a vacuum energy-density change. Gravity = reactance re-tuning (local LC rings slower ⟹ time dilation), NOT a "denser / higher-impedance medium."

## WHAT TO CONFIRM (frozen hypotheses)

**H1 — SIGN.** Gravitational loading drops node frequency → product L_eff·C_eff increases → signal speed c = 1/√(L_eff·C_eff) drops → n = c₀/c > 1 → light slows → bends toward mass (CORRECT). Resolve S-vs-1/S: c_EM = c₀/S (INVARIANT-S2) is the PHASE velocity (may exceed c₀, irrelevant to bending); the SIGNAL / group velocity (c_shear side) is the lensing observable and it drops. Confirm which canonical speed is the ray observable; show n > 1 from it. State plainly whether the principle yields the correct sign.

**H2 — TWO-REACTANCE / factor-2.** Matter couples to ONE sector → n_matter ≈ 1/√S (slope 1, Soldner 2GM/bc²); light to BOTH (the L·C product) → n_light ≈ 1/S (slope 2, Einstein 4GM/bc²); (n−1) ratio = 2. Z = √(L/C) invariant under symmetric loading → reflectionless. Map c_EM = c₀/S, c_shear = c₀√S to the 1/S, 1/√S indices exactly.

**H3 — BENCH per-sector validity.** Static external E (no ∂B/∂t) loads C only (flywheel-spring, μ_local = μ₀ under DC, Ch 01 §5 + `02_general_relativity_and_gravity.tex`) → asymmetric → Z-step → reflection (bench signal valid); mass = soliton (Beltrami standing wave, internal E+B, Vol 2 Ch 1) loads BOTH → symmetric → reflectionless gravity. Confirm asymmetric-bench / symmetric-gravity are consistent under per-sector loading (no contradiction).

**H4 — LANGUAGE.** Ch 14 ("denser, higher-impedance medium", `14_macroscopic_orbital_mechanics.tex:63`) is the energy-density framing; under the principle Z is INVARIANT (reactance re-tuned at constant Z). QUEUE W4 (Ch 14 density-language) + revisit W2 (redshift slope z = GM/c²r vs n_temporal − 1 = 2GM/c²r). **QUEUE only — do NOT edit canonical.**

---

## CANONICAL CITATIONS (verify-before-cite @ HEAD 0e3890df — verbatim, grepped in this worktree before freeze)

**[C1] INVARIANT-S2 two-speed (`manuscript/ave-kb/CLAUDE.md:64-65`):**
> `c_EM(A_0) = 1/√(μ_eff ε_eff) = c_0/S(A_0)` — **Maxwell phase velocity** … Canonical at clm-8nkvwy:111.
> `c_shear(A_0) = c_0√S(A_0)` — **substrate mechanical / group / rest-mass velocity** (oscillator-frequency × ℓ_node; energy-transport speed; tracks Schwarzschild `c√(1−r_s/r)` in the SYM-class weak-field limit). Canonical at clm-8nkvwy:113.

**[C2] SYM-class invariant-Z + α-invariance (`CLAUDE.md:69`):**
> Under SYM-class scaling (gravity-class realization) — μ(r) and ε(r) scale together by the same factor so Z_0 stays invariant — the asymmetry between c_EM and c_shear makes α EXACTLY invariant … SYM scaling produces gravitational time-dilation via c_shear tracking √S (Schwarzschild reduction) WHILE simultaneously preserving α exactly.

**[C3] Ax 4 dielectric specialization (`CLAUDE.md:58`) — BOTH sectors scale (load-bearing for H3 tension):**
> Dielectric specialization (atomic / bench scale, A = Δφ/α): `C_eff = C_0/S`, `ε_eff = ε_0 S`, `μ_eff = μ_0 S`.

**[C4] Op14 small-signal varactor-bias modulation (`CLAUDE.md:60`) — DC bias scales BOTH μ and ε (tension with H3):**
> Small-signal transverse propagation through a region at operating point A_0 sees modulated effective parameters `ε_eff = ε_0 S(A_0)`, `μ_eff = μ_0 S(A_0)`, `C_eff = C_0/S(A_0)` — the same varactor-bias mechanism producing refractive-index gradients across all scales (Op14 local clock modulation, Op16 universal wave speed).

**[C5] LC-tank node frequency (`manuscript/vol_9_vacuum_datasheet/chapters/10_magnetic_microrotational_characteristics.tex:41`):**
> oscillator `ω_C = 1/√(L_cell C_cell) = c_0/ℓ_node`, per Ch. AC characteristic frequency
> with (`:36`) `L_cell = μ_0 ℓ_node`, `C_cell = ε_0 ℓ_node`.

**[C6] Gravity refractive index + symmetric Z-invariance (`manuscript/common_equations/eq_gravity_derived.tex:24-32`):**
> `n(r) = 1 + 2GM/(rc²)` … `μ_eff = μ_0·n(r)`, `ε_eff = ε_0·n(r)`, `Z = Z_0` (invariant).

**[C7] Temporal/spatial decomposition (`eq_gravity_derived.tex:50-64`):**
> `ε₁₁ = 7GM/(c²r)` … `n_temporal = 1 + (2/7)ε₁₁` (controls clock rate, redshift); `n_spatial = 1 + (9/7)ε₁₁` (controls light deflection) … The temporal component governs gravitational redshift (`z ≈ GM/(c²r)`).
> **NOTE (W2 seed):** `n_temporal − 1 = (2/7)·7GM/c²r = 2GM/c²r`, but the same file states `z ≈ GM/c²r`. Factor-2 tension — re-queued as W2 (companion PPN audit W2).

**[C8] Double-deflection 2/7:1/7 Poisson projection (`manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex:179-206`):**
> Matter (scalar coupling) … `n_scalar(r) = 1 + (1/7)χ_vol(r)`. Light (transverse coupling) … `n_⊥(r) = 1 + ν_vac χ_vol(r) = 1 + (2/7)χ_vol(r)`. … `δ_light/δ_matter = (n_⊥−1)/(n_scalar−1) = (2/7)/(1/7) = 2`. With `χ_vol(r) = 7GM/(c²r)`: `δ_matter = 2GM/bc²` (Soldner), `δ_light = 4GM/bc²` (Einstein).

**[C9] Symmetric-vs-asymmetric Z, RF stealth (`manuscript/vol_4_engineering/chapters/01_vacuum_circuit_analysis.tex:438-447`):**
> gravity scales μ and ε *symmetrically* (n×n), preserving Z_0 and producing zero reflection. Topological saturation (particles, event horizons) drives both to zero *asymmetrically* via Axiom 4, collapsing Z and creating perfect mirrors (Γ = −1). … `Z_local(r) = √(n(r)μ_0 / n(r)ε_0) = √(μ_0/ε_0) ≡ Z_0`. … `S_11` Return Loss of −∞ dB.

**[C10] Soliton = Beltrami standing wave, internal E+B (`manuscript/vol_2_subatomic/chapters/01_topological_matter.tex:35,40`):**
> Mass is the stored inductive energy required to maintain the topological integrity of the standing wave … (`:40`) This is a Beltrami standing wave where the continuous E and B field lines are mutually orthogonal and feed into each other in a closed topological loop (∇×A = kA), permanently trapping the energy … The internal electrodynamic circulation of this resonant LC loop.

**[C11] Ch 14 density-language (W4 target) (`manuscript/vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex:63`):**
> the inner edge of an orbit is travelling through a *denser, higher-impedance* topological medium than the outer edge.

**[C12] Asymmetric-electrode bench → reflection (`manuscript/vol_4_engineering/chapters/11_experimental_falsification.tex:185-189`):**
> The vacuum LC network acts identically to a Transient Voltage Suppression (TVS) Zener diode … rigid Z_0 ≈ 377 Ω until V_yield ≈ 43.65 kV, at which point its inductive capacity saturates and it undergoes Absolute Impedance Rupture (Γ = −1).

## METHOD (phases)

- **Phase 0** — write this prereg, verify-before-cite all citations @ HEAD, commit.
- **Phase 1 (sign)** — derive n(loading) from ω = 1/√(L_eff C_eff); confirm loading → freq down → n > 1; reconcile phase (c_EM) vs signal (c_shear).
- **Phase 2 (two-reactance)** — n_matter ≈ 1/√S, n_light ≈ 1/S, factor-2, Z invariant; exact c_EM/c_shear ↔ index map.
- **Phase 3 (bench per-sector)** — static-E → C-only, mass-soliton → both; consistency.
- **Phase 4 (verdict)** — is the sign crack SETTLED by frequency-modulation? consistency-vs-emergence classify (Class C). Queue W2, W4 (do NOT apply). Verification script (ave-canonical-source: import G, C_0, L_NODE from `ave.core.constants`; compute n_light, n_matter, sign; NO hard-coded GR targets). Result doc. Commit; push branch; remove worktree; **DO NOT MERGE.**

## SCOPE GUARDS

Weak-field only. Internal-coherence + intuition-correction, NOT distinctness. Do NOT edit canonical leaves or Ch 14 — result + prereg only; walk-backs queued. Work ONLY in the `/tmp` worktree off `origin/main`; never touch shared local main.

## PRE-TEST-PHYSICS-CHECK STOP CONDITION

If frequency-modulation does NOT cleanly give the sign, or the c_EM/c_shear ↔ index mapping resists, STOP and report — do not force it.

---

## ADJUDICATION CRITERIA (frozen — set BEFORE running, per Rule 7 honest-closure)

- **H1 PASS** iff a single, consistently-signed loading knob makes the *signal* (group / energy-transport) speed drop and yields n > 1 (light bends toward mass), with the phase-velocity (c_EM) behavior explicitly reconciled (allowed to exceed c₀ without affecting the ray observable). **FAIL** iff the sign is ambiguous or requires opposite conventions for matter vs light.
- **H2 PASS** iff there is an *exact* algebraic map from the canonical {c_EM = c₀/S, c_shear = c₀√S} to indices whose (n−1) ratio is exactly 2, AND that map is consistent with the canonical photon index (2/7 → slope 2 → 4GM/bc²) established in the companion PPN audit. **FAIL / FLAG** iff the brief's {1/S, 1/√S} mechanism gives a different (n−1) ratio than 2, or contradicts the canonical 2/7:1/7 Poisson mechanism (flag-don't-fix; do not reframe either to match).
- **H3 PASS** iff static-E (C-only, asymmetric, Z-step, reflective bench) and mass-soliton (E+B, symmetric, Z-invariant, reflectionless) are mutually consistent under per-sector loading with no contradiction.
- **H4** is QUEUE-ONLY (W2, W4). No PASS/FAIL — these are walk-back candidates for separate adjudication.
- **Overall SETTLED** iff H1 PASS and H3 PASS and (H2 PASS OR H2-FLAG cleanly explained as "frequency-modulation gives the *sign + invariant-Z*, the canonical factor-2 is carried by the 2/7:1/7 Poisson projection, and the two are compatible"). Otherwise NOT-SETTLED with the obstruction named.

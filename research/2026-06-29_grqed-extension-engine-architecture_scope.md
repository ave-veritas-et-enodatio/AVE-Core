# Scoping / Design: GR/QED-Extension Engine Architecture

**Status:** DESIGN/SCOPING pass (workflow wzsihu09x → resumed wylik72bq; 13 agents). No build, no repo writes beyond this doc. Verified against HEAD `75d35c4d`.
**Verdict:** **BUILDABLE-WITH-FIXES — but as scoped it is a CONSISTENCY-ENGINE-PLUS-A-THIN-CHORD-SET, not a "fully capable engine" and not a "replacement" of GR/QED.** It becomes AVE-distinct only when the two-way back-reaction (#86) lands.

---

## 0. Architecture (substrate-native framing)

AVE = a mature **GR/QED tensor solver (the LINEAR continuum core)** + the **AVE hardware-correction shell** (the Axiom-4 saturation kernel `S(A)` + the finite lattice `ℓ_node`). The n_eff/transfer-equation verdict established that `g` (the metric) **is** the lattice's linear strain, and that linear core is **GR/QED-equivalent** (FORM-derived, VALUE-imported; the linear identities clm-rd9cjm/y9old1/zf8eah sit at solidity 0.55). So AVE does **not** re-derive the core — it inherits it and adds corrections that are **dormant where the theories work** (`S→1`, `qℓ→0`) and **activate at the blow-up**.

**Why "extend," not "from-scratch":** the from-scratch lattice sim was **already run and FALSIFIED** (Cartesian bulk self-trap, `master_equation_fdtd.py:21-31`). The correction-layer-on-a-GR/QED-solver is the **only live route** — a fact, not a preference.

**FORM-vs-VALUE asymmetry (load-bearing — do not paper over):**
- The **`ℓ_node` cutoff is genuinely FORM-DERIVED** — the discrete-Hilbert commutator `[x,p]=iℏcos(kℓ)=iℏ√(1−(ℓp/ℏ)²)` follows from Axiom-1's lattice pitch (`dcve-specification.md:36-42`, clm-nq2kcc). A physical Brillouin band-limit is a *real* first-principles cutoff — strictly more principled than dimensional regularization.
- The **`S(A)` modulus is FORM-POSTULATED** — it *is* Axiom 4 (Born–Infeld n=2). 
- The two halves sit at **different rungs**; they must **not** be presented as co-equally substrate-native. And every *scale* (`G`, `α`, `ℓ_node`, `m_e`, the yield) is imported.

---

## 1. The GR-extension

**Inherited linear core (do NOT re-derive):** `−(c⁴/7G)∇²ε₁₁ = T₀₀ → ε₁₁ = 7GM/c²r`; `n = 1 + ν_vac·ε₁₁ = 1 + 2GM/rc²`, `ν_vac = 2/7` (`gordon-optical-metric.md:24` + Op19). `C₀ = c⁴/7G` is the GR-imported bulk modulus (embeds imported `G`; K=2G GR-imported, PR#261).

**The correction (divergence form, channel-resolved):**
`−∇·[ (c⁴/7G)·D(A(r))·∇ε₁₁ ] = T₀₀`, with `A = ε₁₁/ε_yield`, `ε_yield = 1`, `S(A)=(1−A²)^p`.

**Per-channel sign (INVARIANT-S2, sign-lock w35sn2bq3 — NEVER a uniform `C·S`):**
- **bulk STIFFENS:** `D = 1/S(A)` (`stiffness_profile:248`, `c_eff²=c₀²/S`) → the medium goes rigid and halts collapse;
- **shear/constitutive moduli SOFTEN:** `G_shear = G₀·S`, `c_shear = c₀√S → 0` at A=1 (the rupture; `scale_invariant.py:164-221`);
- **EM stays MATCHED:** `ε_eff = μ_eff = ε₀·n` → `Z_EM = Z₀`, `Γ_EM = 0` (light sees plain GR).

**Recovers (validate-on-known, consistency-class):** `r ≫ r_sat ⇒ ε₁₁≪1 ⇒ S→1 ⇒ D→1` → exact linear elastic-Poisson → Schwarzschild / Gordon / Shapiro / redshift / lensing `4GM/bc²`. Keep the FOUR index projections distinct (Shapiro 2/7, redshift slope-1, parallax 9/7, deflection-transverse 2/7) per W1/W2.

**Regularizes:** `ε₁₁` grows inward, hits A=1 at `r_sat = 7GM/c² = 3.5 r_s` (factor 7 = 2/ν_vac), **OUTSIDE** the classical horizon; shear+bulk SHORT (`Γ=−1` reflector) while EM matched.

**★ HONESTY (pressure-test):** the singularity is **NOT removed — it is RELOCATED.** The strain `ε₁₁` is capped at 1, but the divergence moves into the inertial-density invariant: canon states `ρ_eff = ρ₀/S_topo³ → ∞` at the shell (`interior-singularity-resolution.md:14,23`); no leaf asserts a finite curvature/Kretschmann invariant; and the "saturation" is **currently a numerical clip** (`np.minimum(...,1.0)`), not the physics reaching A=1. Honest headline: **"point singularity → a strain-saturated SHELL at r_sat=3.5 r_s,"** NOT "no infinity."

**Host:** `gw_propagation.py` — add `saturated_radial_strain()` on the **radial/shear ε₁₁ channel only** (reuse `graded_vacuum_network.saturation_kernel:222` + `stiffness_profile:248`; α-clean; do NOT mint a 2nd kernel); add `saturation_radius()=3.5·r_s`; **leave `refractive_index():84` UNCHANGED** (EM spectator). Finite-core demo = static elliptic relaxation on the native tetrahedral stencil (`_native_laplacian_with_stiffness:255`), NOT a damped time-march. **Gate:** clip/`S_min`-INDEPENDENCE of `M_eff` over [1e-4,1e-2] (else the clamp set the wall). Source must be a **distributed `T₀₀`**, not the inherited δ-source.

---

## 2. The QED-extension

**Inherited core:** continuum Maxwell/QED (`S→1`, `qℓ→0`; `fdtd_3d.py`). Three corrections, all dormant in the QED regime:

1. **Lattice-cutoff propagator (the FORM-derived half):** from `p_disc=(ℏ/iℓ)sin(kℓ)`, the propagator denominator `k² → (2/ℓ²)Σ_b(1−cos(k·b̂·ℓ)) − ω²/c²`; every loop integral over the **first Brillouin zone** `|k|≤π/ℓ_node`, **no counterterm**. Vacuum-pol `Π(q²)` and self-energy converge **by construction**.
2. **Saturating-ε (the bankable E-route):** `ε_ij = ε₀[S(A)δ_ij + diff]`, `A=E/E_yield`; `n_⊥=(1−A²)^{1/4}`, `n_∥=√[(1−2A²)/√(1−A²)]`, differential `δn_bir = n_∥−n_⊥ ≈ −½A²`.
3. **Dispersive-μ(ω) temporal cutoff (FLAGGED-UNBUILT stub):** `μ_eff(ω)=μ₀√(1−(ω/ω_C)²)`, `ω_C=c₀/ℓ_node`, `ℏω_C=m_ec²=511 keV` — circulation-keyed (saturates on ω, NOT |B|; static-B null `S_μ=1`).

**Distinct-cutoff discipline (`constants.py:286-294`):** spatial `k_max=π/ℓ_node` (loop bound) vs temporal `ω_C=c/ℓ_node` (μ bound), ratio exactly π — **must NOT conflate**; the prereg must DECLARE which is the loop-integral bound.

**Recovers:** `ω≪ω_C ⇒ μ→μ₀`; `qℓ≪1 ⇒` continuum propagator; `Π(q²)` RT-equivalent to QED (structural tautology, same U(1) content).

**Regularizes:** UV loop → BZ edge (finite mode count); Landau pole → bounded α; dielectric rupture → `S(A)` cap at `E_yield`.

**★ HONESTY (pressure-test):** the cutoff is finite + pinned (good), **but the dominant Lamb self-energy MAGNITUDE is MATCHED, not predicted** — the AVE "Bethe-log" 9.84 is exactly `ln(1/α²)=2ln(1/α)` (= the **log of the cutoff ratio**, not a dynamical Bethe logarithm); it lands **3.5× off** QED's dynamical 2.81, "papered over" (`vol2/claim-quality.md:1529`). The Lamb leaf also carries an internal **137× contradiction** — asserts BOTH `1/ℓ_node=m_ec` AND `1/ℓ_node=m_ec/α` (off by 1/α). Walk-back item.

**Host:** `fdtd_3d.py` (the saturating-ε E-route is already at `_compute_local_epsilon:189`; the dispersive-μ stub at `:241-242`); the BZ-cutoff propagator is the new loop-regulator layer.

---

## 3. The chord (post-pressure-test) — NARROW

Never in the inherited linear core (peer-with-GR/QED by construction, solidity 0.55); never in any imported magnitude. Surviving, ranked by honesty:

1. **★ E-route vacuum birefringence EXISTENCE** (clm-pp3qwf, solidity 0.8) — **the only near-term bankable chord.** The chord = *the vacuum saturates at all*: a **tree-level O(1)** birefringence-bearing structure QED lacks (QED's is an α²-loop effect); **QED-with-a-cutoff does NOT reproduce it.** The MAGNITUDE `7.5/α³` is an **α-echo** (symmetric-standard: QED's `a_EH α²` is equally α-rooted). Static-B null = corroborative-null (μ circulation-keyed, `S_μ=1`, PVLAS-consistent), **NOT** the falsifier; the discriminator is the **E-route**.
2. **GW echoes** at the `Γ_shear=−1` reflector, `r_sat=3.5 r_s` — **genuine but THIN:** GR's horizon absorbs, AVE reflects; but corpus carries **no quantitative delay/amplitude** (only "scope at O4–O5"); it is a sup-class re-analysis of public data; at-or-below current sensitivity. (The brief's delay formula was a non-canonical embellishment — struck.)
3. The **chord-form** of the strong-field channel-split interior (a 3.5-r_s shear wall while EM stays matched) — but matter/shear-only and the interior is **observationally inaccessible**.

**DEMOTED OUT of the chord set:** the finite core itself (shared with every regular-BH model; interior inaccessible; EHT silent); the **2/7 compactness limit** (FALSIFIED — PSR J0740+6620 gives `2GM/c²R=0.495 > 2/7=0.286`; register as CONSISTENCY); Iron-Kα **7GM** (spin-uncomputed; 7GM is the a*=0 value only); the **(q·ℓ)⁴ dispersion** (slope measured 1.9999, magnitude 2e-22 below LIV bounds); the 511 keV cutoff value (definitional); RT-equivalent loops + Landau-pole removal (consistency/untestable).

**★ The genuine prize** that would make this AVE-distinct rather than a consistency engine is the **UNBUILT two-way back-reaction (#86)** — `T_μν → A(r)` emergent `M_eff` — **absent from every host (grep-confirmed zero files).** The architecture is the right vehicle; it stays a consistency engine until #86 lands.

---

## 4. Build plan (staged)

- **Stage 0 (forks):** Grant rulings on the open forks (§5) + ratify "extend/regularize," not "replace."
- **Stage 1 — GR-extension:** `saturated_radial_strain()` on `gw_propagation.py` (radial/shear channel; EM spectator unchanged); static elliptic relaxation; **gate:** recover Schwarzschild at `r≫r_sat` AND `M_eff` clip/`S_min`-independent (else the clamp set the wall); distributed `T₀₀`.
- **Stage 2 — QED-extension:** the BZ-cutoff propagator (loop regulator) + the saturating-ε E-route (the bankable birefringence chord); **gate:** recover QED at low energy; cutoff pinned-not-tuned; the E-route δn computed (not the matched-magnitude Lamb).
- **Stage 3 — coupled + back-reaction (#86):** the gravity-graded-medium pipeline (bulk-strain `A(r)` → per-cell medium → EM/QED) closed by `T_μν^EM → A(r)`. **This is the make-or-break** that lifts the engine from consistency-shell to AVE-distinct.

---

## 5. Forks for Grant (reconstructed from the specs + pressure-test)

- **F1 — the `p` exponent** (`S(A)=(1−A²)^p`, p∈{1/2,1/4}). The DEC-1 fork; ties to the §3-of-#87 single-source `S^0.5` decision. *Lean: p=1/2 primary.*
- **F2 — "replace" → "extend/regularize" reframe.** Strike "replaces GR/QED" and "fully capable engine" everywhere (doctrine + memory + README). *Pressure-test mandate; ratify.*
- **F3 — the regularization honesty.** Adopt "point singularity → strain-saturated SHELL at r_sat (ρ_eff relocated; strain-cap is a clip)," NOT "infinity removed." *Ratify.*
- **F4 — the Lamb-leaf walk-back.** Fix the 137× internal contradiction (`1/ℓ_node=m_ec` vs `m_ec/α`); flag the Bethe-log 9.84 = cutoff-ratio-log (matched-not-predicted, 3.5× off). *Flag-don't-fix vs walk-back — your call.*
- **F5 — the chord demotions.** Demote 2/7-compactness (FALSIFIED), Iron-Kα-7GM (spin-uncomputed), finite-core-as-chord; keep E-route birefringence (bankable) + thin GW-echo. *Ratify.*

---

## 6. KB / manuscript update register (Grant's explicit ask)

| # | doc | kind | what | gated on |
|---|---|---|---|---|
| R1 | `engine-capability-map.md` + `unified-engine-design-doctrine.md` | doctrine | soften "QED+GR replacement" → "GR/QED-equivalent core + hardware-correction shell"; strike "fully capable engine"; record the FORM-derived (`ℓ_node`) vs FORM-postulated (`S(A)`) asymmetry | F2 ratify |
| R2 | `project_engine_architecture_qed_gr_replacement.md` (memory) | memory | same replace→extend reframe; the consistency-engine-plus-thin-chord verdict; chord = E-route birefringence existence + thin GW-echo; AVE-distinct only when #86 lands | F2 |
| R3 | NEW leaf: GR/QED-extension architecture (vol3/vol4 or engine-doctrine) | new-leaf | the saturating-modulus + `ℓ_node`-cutoff correction layer; the regularization honesty; the chord set; the FORM/VALUE ledger | F2/F3 |
| R4 | `interior-singularity-resolution.md` | update-leaf | honesty: ρ_eff relocated; strain-cap is a clip; "strain-saturated shell at r_sat"; no finite-Kretschmann claim | F3 |
| R5 | the Lamb-shift leaf (`vol2/claim-quality.md:1529` + the Lamb leaf) | update-leaf | fix the 137× `1/ℓ_node` contradiction; flag Bethe-log 9.84 = cutoff-ratio-log (matched-not-predicted, 3.5× off) | F4 |
| R6 | the BH-chord leaves | update-leaf | demote 2/7-compactness (FALSIFIED by PSR J0740), Iron-Kα-7GM (spin-uncomputed), finite-core-as-chord; keep GW-echo thin (strike non-canonical delay formula) | F5 |
| R7 | `clm-pp3qwf` (E-route birefringence) | update-leaf | affirm the EXISTENCE chord (bankable, tree-level O(1) QED lacks); magnitude = α-echo (symmetric-standard) | F5 |
| R8 | `constants.py:286-294` (distinct-cutoff discipline) | update-leaf | the `k_max=π/ℓ_node` (loop) vs `ω_C=c/ℓ_node` (μ) ratio-π discipline; declare the loop bound | — |
| R9 | vol3 gravity (manuscript) | manuscript-volume | the GR-extension (saturating elastic-Poisson, the r_sat shell) once Stage-1 lands | Stage 1 |
| R10 | vol2/vol4 (manuscript) | manuscript-volume | the QED-extension (BZ cutoff, E-route birefringence) once Stage-2 lands | Stage 2 |

---

## 7. Honest scope statement

This is a **FORM-extension that imports its scales.** It does NOT derive gravity, α, or the linear core — it inherits a GR/QED-equivalent core and wraps it in a hardware-correction shell whose `ℓ_node` half is genuinely substrate-derived and whose `S(A)` half is the postulated Axiom-4 kernel. As scoped, it is a **consistency engine + one near-term EM chord (E-route birefringence existence) + one thin future GR chord (GW echoes).** It becomes an AVE-distinct *engine* only when the two-way back-reaction (#86) lands. "Replaces GR/QED" and "fully capable engine" are struck.

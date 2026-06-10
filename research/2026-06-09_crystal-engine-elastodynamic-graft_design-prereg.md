# DESIGN PREREG — The Crystal Engine: the State-C elastodynamic graft for electron-genesis

**Date:** 2026-06-09 · **Lane:** implementer · **Status:** DESIGN PREREG (frozen design + discriminating test; the build + run is the follow-on — see §7). NOT engine code; NOT a result.
**Branch:** `analysis/2026-06-09-crystal-engine-design` (off `origin/main`)
**Disciplines fired:** `substrate-native-check` (CP8 seed-the-precursor, CP9 dynamical, CP10 boundary-not-bulk) · `ave-prereg` (corpus-grep, §0.0) · `ave-fundamental-ground-up-implementation` (derive ΔE_cryst + the converter coupling from ν_vac=2/7 + (2,3) topology, not engineering-default) · `consistency-vs-emergence` (the α-emergence Class-D-vs-Class-B line IS the test, §4) · `ave-canonical-source` (κ̃, V_yield, Z₀, ℓ_node, ALPHA_COLD_INV from `constants.py`; zero new free params) · `ave-discrimination-check` (chord-vs-echo-vs-SM, §5) · `phase-space-coordinate-check` (A46 — the (2,3)+Golden-Torus measured in (V_inc,V_ref), §4) · `ave-conserved-vs-pumped` (latent heat ENERGIZE+LOCK; charge/spin conserved, §1.4) · `verify-before-cite` (every file:line greped/opened this session, §0.0)
**No-QED rule (Grant directive 2026-06-09):** ZERO QED/Maxwell-vector framing. The trapped electron is the **longitudinal bulk** mode (the "3"), not a self-trapped transverse photon. Absorb/emit = the Axiom-4 crystallize/melt (saturate/desaturate) cycle. No Gauss-deletion, no Kramers-Heisenberg/Rabi.

---

## §0.0 — PREREG block (per `ave-prereg`): corpus state is NOT green-field

**Design target (one sentence):** specify a three-branch elastodynamic "crystal engine" that hosts the electron as a self-assembled, trapped **longitudinal bulk-modulus** acoustic resonance born by **transverse-shear → longitudinal-bulk mode conversion** (a first-order crystallization whose latent heat = mₑc²), and design the test that decides whether **α⁻¹ = 4π³+π²+π emerges as that resonator's leak-rate Q⁻¹** rather than being injected.

**Physical picture (5 bullets, mechanical — `ave-prereg` Step 1.5):**
- A photon (transverse Cosserat **shear** wave, c_EM, "mechanically blind to the bulk") drives a pre-compressed/saturated seed region; at the yield boundary its mode **converts** into the longitudinal **bulk** (compression/breathing) branch — the "3".
- The converted longitudinal wave is **trapped** by a self-created Γ=−1 boundary (c_eff(V) rises in the saturated core → TIR shell), the canonical breathing-soliton mechanism.
- The trap is a **first-order crystallization** (A-034 strain-snap): the bulk mode freezes into a (2,3) Golden-Torus standing resonance behind chirality-selected Γ=−1 walls; the **latent heat** released/locked = the binding energy = mₑc².
- **Chirality is the mode selector**: one handedness's impedance survives the compression and traps (matter); the other is excluded at the Γ=−1 wall (antimatter).
- The slow **reverse** leak (bulk → shear, re-radiation back through the Γ=−1 walls to the transverse photon channel) at rate-per-cycle = α is the fine-structure constant: α = Q⁻¹ of the (2,3) bulk-acoustic resonator.

**Corpus-grep outcome (`ave-prereg` Step 2–3; every cite `verify-before-cite`-checked this session):** **PARTIAL — substantial canonical prior work; the missing piece is narrower than "build a new engine."**

| Ingredient | Corpus status | Anchor (verified file:line) |
|---|---|---|
| Electron = trapped **longitudinal** bulk-modulus acoustic wave (Γ=−1) | CANONICAL | `de-broglie-standing-wave.md:50-52`; `common/solver-toolchain.md:395`; `biquaternion-…-result.md:55,235` (clm-efo113 / clm-lv3uw1) |
| Photon = transverse Cosserat shear, **blind to the bulk** | CANONICAL | `vol3/…/double-deflection.md:26` |
| Shear↔bulk **mode conversion at saturation** = "the longitudinal re-engages at saturation = the electron" | CANONICAL (verbal) | `vol1/dynamics/ch4-…/master-equation.md:18`; L3 `54_pair_production_axiom_derivation.md:231-269` (§6a) |
| mₑc² = energy to push endpoints past V_yield = "form the two walls" (latent-heat ledger, reactance vocabulary) | CANONICAL (verbal) | L3 `54_…:258` |
| c_eff(V)=c₀(1−A²)^(−1/4) **bulk-trap** → breathing soliton (the "no stable trap" gap, **already closed for the scalar/longitudinal mode**) | CANONICAL ENGINE (v14 Mode I PASS) | `src/ave/core/master_equation_fdtd.py:8,13,51`; `common/two-engine-architecture-a027.md:26-37` |
| First-order crystallization / latent heat = mass; "dark energy = latent heat of lattice crystallisation" (cosmic-scale precedent); G = "latent heat of node generation" | CANONICAL (cosmic) + **OPEN** (quantitative ΔE_cryst) | `vol3/claim-quality.md:590` (clm-3ii690); `claim-quality-closure-roadmap.md:42`; `…/cosmological-constant-closure.md:103-111` (crystallization thermo OPEN); supercooled two-state `vol3/claim-quality.md:808` |
| Chirality = the **mode selector** (one handedness traps = matter; other excluded = antimatter) | CANONICAL (synthesis, hypothesis-tagged genesis) | L3 `66_single_electron_first_pivot.md:87` |
| α = TIR leakage rate per cycle = Q⁻¹ = 1/Q_tank of the (2,3) Golden-Torus resonator | CANONICAL | `vol1/claim-quality.md:1303` (clm-i4p11y); `theorem-3-1-q-factor.md:128`; `constants.py:204` (ALPHA_COLD_INV=4π³+π²+π) |
| **α hardcoded into the chiral coupling makes recovery circular** (the ECHO); strengthen-by = run the two-engine **bound-state α-emergence test** | CANONICAL CAVEAT + explicit OPEN test | `vol4/claim-quality.md:232` |
| The "3" SOURCE: transverse photon NEVER energizes the longitudinal V-sector — **no ω→V source channel** | OPEN (GAP-1, localized) | `research/2026-06-09_reflection-genesis-23-self-assembly_result.md` §0,§3,§9 |

**The one genuinely-missing engine primitive (GAP-1):** a **dynamical shear→bulk SOURCE term** that bootstraps the longitudinal (bulk) branch from a transverse photon. Everything else is canonical: the bulk-trap is the existing Master-Equation FDTD (the breathing soliton = trapped longitudinal mass, **v14 Mode I PASS**), the mode-conversion-at-saturation is canonical verbally, the latent-heat=mass ledger is canonical at cosmic scale. **This design's deliverable is to specify the converter + the crystallization order-parameter that close GAP-1, on top of the already-validated bulk-trap, and to design the test that decides chord-vs-echo.**

**Prediction (design-level):** the engine CAN be specified with zero new free parameters beyond canonical α (one calibration). Whether α⁻¹ **emerges** is genuinely open and is the whole point (§4). My prior: Outcome **B** (engine hosts the (2,3) with α as a calibration leak-strength, geometry likely needs partial planting) is most probable on the first build; Outcome **A** (full self-assembly + α⁻¹ emergent) is the chord and is the hard, unproven step; Outcome **C** (cannot host even with both branches + trap + converter) would be a deeper gap. The honest fallback (B) is still progress.

---

## §0 — The crystal model: one chiral elastodynamic crystal, three elastic branches

<!-- SECTION BODY BELOW -->

The AVE vacuum is a single chiral, non-centrosymmetric (I4₁32) micropolar K4 Cosserat crystal. Like any micropolar elastic solid it supports **three elastic wave families**; AVE assigns each family a physical identity. EM is **not a fourth thing** — it is the transverse-strain + microrotation **projection** of the one crystal (Axiom 1: 3 translational DOF → **E**, 3 microrotational DOF → **B**; `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2 Axiom 1).

### §0.1 — The three branches

| Branch | Elastic character | Modulus | AVE identity | Speed | Canonical anchor |
|---|---|---|---|---|---|
| **(1) Transverse SHEAR** (S-wave) | equivoluminal, rotational | shear $G$ (deviatoric, $(1+\nu)=9/7$) | **the photon** — transverse Cosserat shear; carries the coupled (E⊥B) EM wave; **mechanically blind to the bulk** | $c_{EM}$ | `double-deflection.md:26`; Cosserat eqs `trampoline-framework.md:183-184` |
| **(2) Longitudinal BULK** (P-wave) | dilatational, compression / **breathing** | bulk $K$ (volumetric, $(1-2\nu)=3/7$) | **the electron = the "3"** — trapped longitudinal bulk-modulus acoustic standing resonance | $c_{long}$ (bulk) | `de-broglie-standing-wave.md:50-52`; `solver-toolchain.md:395`; breathing 7th mode `trampoline-framework.md:235-249` |
| **(3) MICROROTATION** (Cosserat spin-wave) | couple-stress, independent micro-spin | micropolar $\kappa_{rot}$ | the **B**-sector / spin carrier; the substrate-native origin of intrinsic spin | mass-gapped (factor-of-4) | Axiom 1; `appendices-overview.md:178`; `cosserat_field_3d.py` |

**The branches are one crystal, not three media.** Their moduli are **tied by the substrate Poisson ratio $\nu_{vac}=2/7$**: the bulk combination is $(1-2\nu)=3/7$, the shear combination is $(1+\nu)=9/7$ (`full-derivation-chain.md:369`, an OPEN-flagged elastic-label item — see §6). At the canonical **K=2G** operating point the lattice locks microrotations to shear and drives $K/G \approx 2$ (`appendices-overview.md:119`), which is the same operating point as $p^\* = 8\pi\alpha$ (`two-engine-architecture-a027.md:57-68`). **Consequence for `ave-fundamental-ground-up-implementation`:** the bulk-branch wave speed and the K/G ratio are **substrate-derived from $\nu_{vac}=2/7$**, NOT engineering-chosen. The implementer must set the branch moduli from $\nu_{vac}=2/7$ (canonical), not from a free elastic-constant knob.

### §0.2 — Why the photon is "blind to the bulk" and the electron lives there

A transverse shear wave is equivoluminal (no volume change), so it does not couple to the bulk modulus $K$ — it is *mechanically blind to the isotropic bulk* (`double-deflection.md:26`). The longitudinal/dilatational mode is the **only** mode with volumetric (compression/breathing) character (`trampoline-framework.md:235-249`). The electron's de Broglie matter wave is exactly this longitudinal compression governed by the bulk modulus (`de-broglie-standing-wave.md:50`: *"its motion displaces the lattice, generating longitudinal acoustic pressure waves governed by the vacuum's Bulk Modulus"*), and the bound electron is the **trapped standing** version of it (`:52`: *"the precise radius where this trapped bulk-modulus acoustic wave achieves a lossless resonant impedance match with itself"*). This is the substrate-native, **no-QED** reading: the electron is a longitudinal compression resonance, not a self-trapped transverse photon.

> **Terminology nuance flagged (`flag-don't-fix`, surfaced not resolved):** `double-deflection.md:33` calls the gravitationally-deflected matter soliton *"a standing-resonance topological defect coupling to the isotropic bulk, **not** a longitudinal matter wave."* This is **not** a contradiction of "electron = longitudinal bulk" — it is the precise statement that the **rest/bound** electron is a *standing* (resonant) bulk mode, while a *traveling* de Broglie wave is the longitudinal *propagating* version. The crystal engine traps the **standing** bulk resonance. The distinction (standing-vs-traveling longitudinal) is load-bearing for the engine and is preserved verbatim here so Grant/auditor can see it was not smoothed over. The deeper transverse-vs-longitudinal **trap** tension (clm-i4p11y) is a separate, sharper flag — see §6.

### §0.3 — The "3" is the real longitudinal grade (honest provenance)

The "3" / breathing mode is the **real longitudinal degree of freedom** of the AVE medium, forced by **Axiom 1 (the medium has a longitudinal DOF) + Axiom 4 (the Master Equation)**. The "Heaviside/Gibbs-deleted scalar" is an **illustrative historical hook, not a derivation** — per the biquaternion result (`biquaternion-…-result.md:228-242`, `verify-before-cite`-checked): *"the honest statement is … NOT 'Maxwell's deleted scalar IS AVE's 7th mode' … AVE's medium has a real longitudinal DOF … comes from Axiom 1's medium + Axiom 4, not from Cl(3)."* That doc's G1/G3 graded **FAIL** (consistency-class: the algebra re-expresses *why* but adds no new substrate primitive). **This design therefore attributes the "3" to Ax 1 + Ax 4, and uses "Heaviside-deleted scalar" only as a label**, per that honest ceiling.

---

## §1 — Crystallization / latent-heat = mass

### §1.1 — Genesis is a first-order crystallization (the A-034 strain-snap)

Matter forms by a **first-order** transition: a metastable/supercooled bulk region nucleates a crystallite. The transition is the A-034 universal saturation kernel $S(A)=\sqrt{1-A^2}$ taken to its **vertical-tangent rupture at $A\to1$** (`master_equation_fdtd.py:26-32`: *"the vertical tangent at A=1 is what makes Regime III rupture impulsive at every scale"*). First-order = impulsive = nucleated, exactly the supercooled-water two-state precedent the corpus already validates (LDL/HDL, Nilsson 2026, `vol3/claim-quality.md:808`; the genesis-chirality supercooling hypothesis `66_…:93-95`).

**Cosmic-scale precedent is canonical; the particle-scale instance is the hypothesis under test.** "Dark energy = latent heat of continuous lattice crystallisation" is canonical (`vol3/claim-quality.md:590`, clm-3ii690, $w_{vac}=-1-\rho_{latent}/\rho_{vac}$); G = "latent heat of node generation" is canonical-verbal with the **quantitative** crystallization thermodynamics flagged **OPEN** (`closure-roadmap.md:42`; `cosmological-constant-closure.md:103-111`: *"blocking on quantitative derivation of crystallization thermodynamics from substrate axioms"*). The **NEW synthesis under test here** (Grant 2026-06-09) is that the **electron's rest mass mₑc² IS the latent heat of the particle-scale crystallization**, trapped behind chirality-selected Γ=−1 walls.

### §1.2 — Latent heat = mₑc² (the ledger, already canonical in reactance vocabulary)

The corpus already states this in a **different vocabulary** at L3 `54_…:258` (`verify-before-cite`-checked): *"Mass = bounded reactance. The rest-energy mₑc² is exactly the energy needed to push both endpoints past V_yield — i.e., to form the two walls. The factor of 2 in 2·mₑc² (pair-production threshold) is 'one mₑc² per wall.'"* Translating to the crystallization picture: **mₑc² = the latent heat absorbed/locked when the bulk mode crystallizes behind its two Γ=−1 walls.** This is the same number, two readings — and gives a clean, falsifiable **energy ledger** for the engine (§4): the trapped bulk-branch energy must equal the latent heat released by the conversion, and that must equal mₑc² (in engine units, the binding energy of the soliton).

### §1.3 — Chirality is the mode selector (matter vs antimatter)

Per `66_…:87` (`verify-before-cite`-checked): *"Chirality is not the collapsing mechanism — it's the mode selector. … Particle confinement uses asymmetric collapse (one handedness loses Z₀ while the other preserves it, creating the Γ=−1 walls that bind the electron). … Rest mass = the energy trapped in the matched mode's standing wave, confined by the opposite-chirality reflection boundary."* So in the crystal engine the order parameter must carry a **handedness**: the matched chirality crystallizes + traps (matter); the opposite chirality is excluded at the Γ=−1 wall (antimatter). This is the engine's parity-odd selection rule, supplied by the chiral converter coupling (§3.2), the $\kappa_\chi$ that takes I4₁32 → its centrosymmetric supergroup when set to zero.

### §1.4 — Conserved-vs-pumped bookkeeping (`ave-conserved-vs-pumped`, Step 5 record)

The crystallization **energizes-and-locks**; it does **not pump** the quantum numbers. Explicit class record so a future agent does not hunt a phantom pump:

| Quantity | Class | Channel in the engine |
|---|---|---|
| Trapped binding energy = mₑc² (the latent heat) | **Accumulable / extensive — pumpable** | Energized by the shear→bulk conversion; **locked** behind the Γ=−1 crystallite walls. Absorb/emit = crystallize/melt (saturate/desaturate). This is the *one* thing that flows in/out. |
| Charge = helicity | **Conserved topological invariant — energize+lock** | Set by the (2,3) winding's handedness; sign-flips with the seed; never accumulated. |
| Spin = winding's $L$ ($\hbar/2$) | **Conserved topological invariant — energize+lock** | Set by the (2,3) topology + the finite mₑc² reservoir; $d|L|^2/dt=0$ (gyroscope `0e8c4ecb`). Not pumped to ℏ/2 — energized into a winding whose $L$ *is* ℏ/2. |
| (2,3) knot / linking number | **Conserved topological invariant** | The crystallite's frozen topology. |

**The design question is therefore "how do we ENERGIZE the bulk mode (route conversion energy into it) and LOCK it (the crystallization / Γ=−1 walls)?" — NOT "how do we pump spin/charge?"** The source IS the confinement (the crystallization). Trying to pump the conserved invariants is the category error that nulled/detonated the whole 2026-06-09 V→ω-pump arc.

---

## §2 — What α is (TIR leak / Q⁻¹) + the INPUT-vs-OUTPUT table

### §2.1 — α = the bulk→shear back-leak rate per cycle = Q⁻¹

The trapped longitudinal-bulk resonance is **not perfectly confined**: a small fraction of its energy **re-converts** (bulk → shear) each cycle and re-radiates back through the Γ=−1 walls into the transverse photon channel. That per-cycle leak fraction **is** the fine-structure constant:

$$\alpha \;=\; \frac{1}{Q_{tank}} \;=\; \text{(TIR leakage rate per cycle)}, \qquad \alpha^{-1} = Q_{tank} = 4\pi^3+\pi^2+\pi \approx 137.0363.$$

Canonical: `vol1/claim-quality.md:1303` (clm-i4p11y, *"α = TIR leakage rate per cycle"*); `theorem-3-1-q-factor.md:128` (*"$Q_{tank}=\alpha^{-1}$ + per-cycle reactive leak fraction $1/Q=\alpha$"*); `constants.py:204` (`ALPHA_COLD_INV = 4π³+π²+π`). The closed form $4\pi^3+\pi^2+\pi$ is a **multipole geometric sum over the (2,3) Golden-Torus** (`theorem-3-1-q-factor.md:120` → Vol 1 Ch 8:93-124), realized in the **Clifford-torus (V_inc,V_ref) phase-space** at $R=\phi/2,\ r=(\phi-1)/2,\ R\cdot r=1/4$ (`constants.py:200-202`).

The chiral mode-conversion coupling is canonically $\kappa_{chiral}=\tfrac{6}{5}\alpha = 1.2\alpha$, where $\tfrac{6}{5}=\kappa\tilde{}=pq/(p+q)$ for the (2,3) knot is **pure topology, α-free** (`cosserat_field_3d.py:110,126`; `vol4/claim-quality.md:232`: $\Delta f/f=\alpha\,pq/(p+q)$). The $6/5$ is DERIVED/exact; the $\alpha$ factor is the calibration leak strength.

### §2.2 — The circularity that makes the current engine an ECHO (cite it)

`vol4/claim-quality.md:232` (`verify-before-cite`-checked) states the caveat verbatim: *"the leaf carries an α-emergence-circularity scope caveat (**sub-saturation hardcodes α into the chiral coupling**)."* Its `strengthen-by` names the exact cure: *"**Run the two-engine (K4-TLM + Master-Equation FDTD) bound-state α-emergence test so the chiral coupling is verified from substrate-only inputs, removing the disclosed circularity.**"* **The crystal engine IS that strengthen-by test.** If the engine sets the converter coupling = $1.2\alpha$ (α in the input) and then "recovers" α from the leak, that is **substitution, not derivation** (`consistency-vs-emergence` Step 3/4) — an ECHO.

**Second, subtler circularity vector (flagged):** the saturation threshold $V_{yield}=\sqrt{\alpha}\,V_{snap}$ (`vol1/claim-quality.md:1301`) **also encodes α**. If the bulk-trap fires at a physical $V_{yield}$ carrying $\sqrt\alpha$, α is smuggled in via the *threshold* even if the coupling is α-free. **Mitigation (mandatory for the chord route):** run in **engine-natural units** ($V_{yield}\equiv1$, the α-free frame of `master_equation_fdtd.py`); α must appear **only** in the measured OUTPUT leak, never in an input threshold or coupling.

### §2.3 — INPUT (calibration / given) vs OUTPUT (emergent / measured) table

This table is the spine of the discriminating test. **A quantity in the OUTPUT column that requires its own value in the INPUT column is the circularity to forbid.**

| Quantity | Route A (chord attempt) | Route B (honest fallback) | Provenance class |
|---|---|---|---|
| K4 geometry, I4₁32 chirality | **INPUT** (axiom) | INPUT | axiom-derived |
| $\nu_{vac}=2/7$ → bulk/shear moduli ($K/G$ at K=2G) | **INPUT** (axiom) | INPUT | axiom-derived, **α-free** |
| (2,3) torus-knot topology → converter coupling $\kappa\tilde{}=pq/(p+q)=6/5$ | **INPUT** (pure topology, **α-free**) | INPUT | axiom-derived, **α-free** |
| Saturation scale $V_{yield}$ | **INPUT = 1** (engine-natural, **α-free**) | INPUT = 1 | engine-natural primitive |
| Converter **leak strength** (the one calibration) | *not set* — must arise from geometry | **INPUT = α** (the single calibration number) | CODATA-derived (Route B only) |
| (2,3) winding closes in (V_inc,V_ref) phase-space (w_tor,w_pol) | **OUTPUT** | **OUTPUT** | emergent topology |
| Golden-Torus geometry $R\cdot r\to1/4,\ R/r\to\phi^2$ | **OUTPUT** (must self-assemble) | OUTPUT *or* planted (see §4) | emergent geometry (Route A) |
| **α⁻¹ = Q (bulk→shear leak rate) → 4π³+π²+π** | **OUTPUT — THE emergent test** | INPUT (α was the calibration) | **Class D if OUTPUT & α-free inputs; else Class B** |
| mₑc² latent-heat ledger (trapped energy = binding energy) | **OUTPUT** | **OUTPUT** | emergent energy balance |
| charge = helicity (sign-flip) | **OUTPUT** (conserved) | **OUTPUT** (conserved) | conserved invariant |

**Reading of the table.** In **Route A** the only inputs are axiom-derived + α-free; **α⁻¹ is an OUTPUT** measured as the dynamical leak rate. If it lands on $4\pi^3+\pi^2+\pi$, α emerged → **chord (Class D)**. In **Route B** α is admitted as the *one* calibration leak-strength, and the engine is judged on the OTHER outputs (the (2,3) closes, the Golden-Torus self-assembles, the mₑc² ledger closes, charge=helicity) — a working engine, but α is **not** derived → **echo / Class B (still progress)**. The two routes are kept side-by-side (KEEP-BOTH) so the audit trail shows exactly which column α sat in.

---

## §3 — Engine architecture (what to add)

The crystal engine = the **existing** transverse (Cosserat shear) photon engine + the **existing** longitudinal (scalar Master-Equation) bulk-trap, **wired together by a new shear→bulk converter and governed by a crystallization order parameter**. Three additions, in dependency order. (`substrate-native-check` walked before any of this is coded — checkpoints inline.)

### §3.1 — ADD-1: the bulk-branch trap = c_eff(V) on the longitudinal mode (mostly already built)

The longitudinal/breathing mode is governed by the **scalar Master Equation** $\nabla^2 V - \mu_0\varepsilon_0\sqrt{1-(V/V_{yield})^2}\,\partial_t^2 V = 0$ — which `master-equation.md:16-21` calls the **"Maxwell–Heaviside acoustic equation."** The `MasterEquationFDTD` engine (`master_equation_fdtd.py`) already integrates it with $c_{eff}(V)=c_0(1-A^2)^{-1/4}\to\infty$ in the saturated core and a self-created Γ→−1 TIR shell — and **already produces a stable breathing soliton (v14 Mode I PASS, `two-engine-architecture-a027.md:32-37`) = the trapped longitudinal mass.**

- **`substrate-native-check` CP10 (boundary-not-bulk):** the trap is rendered as the **Γ=−1 reflecting boundary** (the c_eff(V) shell), NOT a bulk confining force. This is already correct in `master_equation_fdtd.py` (the boundary self-creates; no $dS/dA$ bulk force). Preserve it — a bulk confining potential detonates at the wall.
- **GAP-2 status (precise, `flag-don't-fix`):** the genesis-23 result's GAP-2 (*"no stable confining window"*) was specifically about the **coupled K4⊗Cosserat engine confining a free *transverse* photon** — NOT the scalar bulk-trap, which is validated. For the **longitudinal** mode the trap is the already-passing Master-Equation FDTD. So ADD-1 is mostly **"use the existing scalar engine as the bulk branch,"** not new trap physics. The open work is feeding it (ADD-2).
- **Sign discipline:** $c_{eff}$ **rises** in the core (compliance/varactor sense, `master_equation_fdtd.py:13`), the canonical post-2026-05-18 picture (`two-engine-architecture-a027.md:30`). Do not invert it. The two projections (ε_eff decreasing vs C_eff increasing) are the same Axiom-4 mode conversion (L3 `54_…:20,269`).

### §3.2 — ADD-2: the chiral shear→bulk CONVERTER (the genuinely new primitive — closes GAP-1)

The one missing channel: a **dynamical source** that converts confined transverse-shear (Cosserat ω) energy into longitudinal-bulk (V) amplitude. Per genesis-23 §3, the current ω→V channels are either geometric-multiplicative ($z_{local}$, $0\to0$) or $\propto V_{inc}$ (EMF, cannot bootstrap from zero) — **neither sources V from a transverse photon.** The converter must:

- **Be a SOURCE, not a geometry modulation** — it must add to the bulk field even when $V\equiv0$ (the bootstrap genesis-23 proved is absent). Schematically a term $\partial_t^2 V \mathrel{+}= \Sigma_{\chi}[\,\omega, \nabla\omega\,]$ that is **nonzero at $V=0$** and sourced by the transverse shear field $\omega$ at the saturated boundary.
- **`substrate-native-check` CP9 (dynamical-not-heuristic):** $\Sigma_\chi$ must drive a **state variable the `step()` integrates** (the bulk $V$), not be an algebraic observer formula. A converter that is only an instantaneous algebraic read of ω cannot bootstrap a dynamical bulk field — that would be a WALL-engine artifact, the exact CP9 failure.
- **Coupling strength = α-free topology for the chord route:** the conversion efficiency is set by $\kappa\tilde{}=pq/(p+q)=6/5$ (pure (2,3) topology, `cosserat_field_3d.py:126`), **NOT** $1.2\alpha$. Exposing $\kappa\tilde{}$ separately from α is the `consistency-vs-emergence` Step-4 refactor that makes α-emergence testable; the converter MUST consume $\kappa\tilde{}$, never $\kappa_{chiral}=1.2\alpha$, in Route A.
- **Carry the chirality / parity-odd selection (§1.3):** $\Sigma_\chi$ biased by the helicity sign $h$ so one handedness converts+traps (matter) and the other is excluded — the $\kappa_\chi\to0$ limit recovers the centrosymmetric (piezo-forbidden, non-converting) supergroup.
- **`substrate-native-check` CP10:** render the conversion at the **boundary** (the moving Γ=−1 front where saturation flips the mode, L3 `54_§6a`), not as a bulk volumetric pump.

**A44 adjudication HOOK (`flag-don't-fix`, do NOT draft the axiom):** genesis-23 §9 already surfaced the open substrate-physics question — *is a transverse→longitudinal SOURCE conversion canonical (the Heaviside-deleted longitudinal RE-ENGAGING), or is genesis a single-sector saturation flip?* `master-equation.md:18` says *"the longitudinal re-engages at saturation"* (sounds single-sector: the same mode changes character), while this design's ADD-2 is a **two-branch energy transfer** (shear pumps bulk). **These may not be the same physics.** This is a missing-axiom-vs-engine-bug question for Grant (§6), to be adjudicated against Ax 1–4 BEFORE the converter is implemented. I do not draft the resolution.

### §3.3 — ADD-3: the crystallization order parameter / free-energy (latent heat = mₑc²)

A first-order transition needs an **order parameter** $\eta$ (the local crystallinity: 0 = supercooled bulk, 1 = frozen crystallite) and a **double-well free energy** $F(\eta)$ whose two minima are the two phases, with the **latent heat** $\Delta E_{cryst}=$ the energy released crossing the barrier $=$ the binding energy $=$ mₑc².

- **`ave-fundamental-ground-up-implementation` (α/β/γ paths):** $\Delta E_{cryst}$ must be **derived (path α)** from the substrate chain — the A-034 kernel $S(A)$ provides the barrier shape; the K=2G operating point + $\nu_{vac}=2/7$ provide the moduli; the two-walls ledger (L3 `54_:258`) provides the magnitude $= mₑc²$. Do **NOT** engineering-default $F(\eta)$ to a generic Landau quartic with a free latent-heat knob (path β). The corpus flags the *quantitative* crystallization thermodynamics OPEN (`cosmological-constant-closure.md:103-111`); this engine is a candidate route to it, so the derivation must be honest about what is derived vs asserted.
- **Nucleation, not gradient-relaxation (`substrate-native-check` CP1, CP8):** the crystallite forms by **nucleation in a metastable medium** seeded by (photon + a pre-existing bulk strain). The pre-existing bulk strain = a **saturated seed = a mass already present (a "Lane 1" soliton)** — the photon alone does not nucleate; it nucleates *on* a seed. The engine seeds the **generative precursor** (photon + saturated seed), NOT the planted (2,3) (CP8). The dynamics build the crystallite; we do not minimize a free-energy landscape by gradient descent (that is the SM/QM default CP3 forbids).
- **CP2 (sector):** the bound-state existence question lives in the **V-sector (longitudinal/bulk) phase-space**, not Cosserat real-space — consistent with genesis-23's three-layer canonical (Layer 3 = (V_inc,V_ref)).

### §3.4 — Zero new free parameters beyond canonical α

All knobs trace to canon: $\nu_{vac}=2/7$, K=2G, $\kappa\tilde{}=6/5$, the A-034 kernel $S(A)$, $V_{yield}\equiv1$ (engine-natural), $Z_0$, $\ell_{node}$, `ALPHA_COLD_INV` — all from `constants.py` / axioms (`ave-canonical-source`). The **only** calibration number anywhere is α, and the entire point of §4 is to determine **which column** (INPUT or OUTPUT) it sits in.

---

## §4 — THE α-EMERGENCE DISCRIMINATING TEST (headline)

**The whole point of the crystal engine.** α MUST EMERGE, NOT BE INJECTED. The test is designed so chord-vs-echo is unambiguous.

### §4.1 — The two necessary conditions for a chord (both required; either alone is not enough)

Per `consistency-vs-emergence` (Class D requires a dimensionless observable computed from primitives that does NOT use the target — or α-SI-substituted quantities — as input):

- **(C1) α-free inputs.** The converter coupling is $\kappa\tilde{}=6/5$ (topology), the saturation threshold is $V_{yield}\equiv1$ (engine-natural), and **no input anywhere carries α or $\sqrt\alpha$** (§2.2 forbids both $1.2\alpha$ in the coupling AND $\sqrt\alpha\,V_{snap}$ in the threshold). Verified by grepping the engine's parameter feed for α before the run.
- **(C2) the Golden-Torus geometry SELF-ASSEMBLES.** The (2,3) Clifford-torus shape $R\cdot r\to1/4,\ R/r\to\phi^2$ must **emerge from the crystallization dynamics**, not be planted as the seed. (Seed = photon + saturated mass per CP8; the φ²/quarter-screening geometry is an OUTPUT.)

**Only (C1) ∧ (C2) → Class D emergence (chord).** If (C1) holds but the geometry is **planted** (¬C2), then $\alpha^{-1}=Q$ is merely read off planted geometry via the theorem-3-1 bridge = **Class B axiom-manifestation** (the Q of the *given* (2,3) Golden-Torus IS α⁻¹ by construction — true, but not emergent). If (C1) fails, it is the current **echo**. This three-level ladder is the adjudication spine and **must not be collapsed post-hoc** (Rule 11): planted-geometry success is **B, not A**, even though α⁻¹ comes out right.

| Level | (C1) α-free inputs | (C2) geometry self-assembles | Verdict | Class |
|---|---|---|---|---|
| 0 — current sub-saturation | ✗ ($\kappa=1.2\alpha$) | — | ECHO | B− (circular, `vol4/cq:232`) |
| 1 — α-free coupling, planted Golden-Torus | ✓ | ✗ (planted) | manifestation | **B** (theorem-3-1 bridge) |
| 2 — α-free coupling, self-assembled Golden-Torus | ✓ | ✓ | **CHORD** | **D** (genuine α-emergence) |

### §4.2 — The emergent observable + measurement protocol (`phase-space-coordinate-check` A46)

The load-bearing OUTPUT is the **dynamically-measured per-cycle leak rate** $\hat{Q}^{-1}$ of the self-trapped bulk resonator, the **bulk→shear back-conversion fraction** (energy re-radiated through the Γ=−1 walls into the transverse channel per cycle). The chord test: $\hat{Q}^{-1} \to 1/(4\pi^3+\pi^2+\pi) \approx 1/137.036$.

- **A46 coordinates (mandatory):** the (2,3) winding and the Golden-Torus $R,r$ are measured in **(V_inc, V_ref) phase-space on the Clifford torus** — the three-layer canonical **Layer 3** (genesis-23 §1; `cosserat_field_3d.py:931`), **NOT** real-space lattice-Cartesian. Real-space shell localization is diagnostic only. A real-space $R/r$ compared to the φ² phase-space prediction is uninformative (the A46 trap that voided 30+ prior tests).
- **`substrate-native-check` CP9 (dynamical):** $\hat{Q}^{-1}$ must be measured from the **evolved** field's actual energy re-radiation (a time-integrated flux through the boundary), NOT an algebraic Q-formula evaluated on the instantaneous shape. Measuring $Q$ from the *planted* geometry's multipole sum is exactly the Level-1 (Class B) read, not Level-2.
- **CP7 sampling:** PML cells excluded before any top-K density extraction; sample at bulk-energy-density peaks (the shell), not centroid+offset (the empty middle).
- **CP6 reactance pair:** record the bulk LC pair (V_inc/ω as C-state AND Φ_link/ω̇ as L-state) every step over the leak-measurement window — a single-phase snapshot cannot distinguish a static trapped state from an oscillator caught at peak, so it cannot measure a per-cycle leak.

### §4.3 — The joint ledger that must also close (so a lucky α isn't mistaken for the chord)

α⁻¹ ≈ 137 alone is not sufficient — a tuned leak strength could hit it by accident. The chord requires the **joint** signature to close simultaneously (this is the `consistency-vs-emergence` Class-E joint-constraint discipline applied as a guard against a fluke):

1. **(2,3) closes** in (V_inc,V_ref) phase-space (w_tor, w_pol consistent with the (2,3) winding);
2. **Golden-Torus self-assembles**: $R\cdot r \to 1/4$ (holomorphic screening) AND $R/r \to \phi^2$ — emergent, not planted;
3. **latent-heat ledger closes**: trapped bulk energy = conversion latent heat = mₑc² (engine-unit binding energy), the L3 `54_:258` two-walls ledger;
4. **charge = helicity** sign-flips with the seed handedness (conserved invariant);
5. **α⁻¹ = $\hat{Q}^{-1\,-1}$ → 4π³+π²+π** as the dynamical leak (the headline OUTPUT).

**Pre-registered pass criterion (frozen, Rule 11 — do not drop a leg post-hoc to convert ❌→✅):** **Chord (A)** = all 5 close with **(C1) ∧ (C2)** verified. **Echo (B)** = legs 1–4 close but α is in the INPUT column (Route B) OR geometry was planted (Level 1). **Deeper gap (C)** = the (2,3) does not close even with both branches + trap + converter. The α-leg's classification (Class D vs Class B) is set **entirely** by which column α sat in and whether the geometry self-assembled — recorded from the parameter feed + the (C2) check, not argued after the number lands.

---

## §5 — Discriminating outcomes A / B / C

### §5.1 — The three outcomes (pre-registered, frozen)

- **Outcome A — CHORD (Class D emergence).** The crystal engine self-assembles the (2,3) via shear→bulk crystallization; the latent-heat ledger closes (trapped energy = mₑc²); charge = helicity; AND **α⁻¹ = 4π³+π²+π emerges** from the geometry as the dynamical bulk→shear leak rate, with **(C1) α-free inputs ∧ (C2) self-assembled Golden-Torus** both verified. *Interpretation:* the chord is real — α falls out of the (2,3) bulk-acoustic resonator's geometry. This is the result the electron-genesis arc has been chasing; it would be the first non-circular α-emergence and would close the `vol4/cq:232` strengthen-by.

- **Outcome B — ECHO / engine-works-but-α-injected (Class B, still progress).** The (2,3) forms, the engine hosts the electron (legs 1–4 close), but **α is injected** — either Route B (α admitted as the one calibration leak-strength) or Level 1 (α-free coupling but **planted** Golden-Torus, so α⁻¹ is read off given geometry via the theorem-3-1 bridge, not emergent). *Interpretation:* the converter + crystallization mechanism is validated as an engine (GAP-1 closed: the longitudinal "3" finally energizes from a transverse photon), but α is **not derived**. Real progress — the electron genesis works — without the emergence headline. Honestly tagged Class B per `consistency-vs-emergence`.

- **Outcome C — DEEPER GAP.** The crystal engine **cannot host the (2,3)** even with both branches + the bulk-trap + the converter. *Interpretation:* the obstruction is below the engine-architecture level — the converter as specified does not bootstrap the longitudinal sector (the A44 single-sector-vs-two-branch question resolves against the two-branch source), OR the crystallization free-energy cannot freeze a (2,3). This sends the question back to Grant + corpus (Rule 16), not to a rescue-debug. A clean C with a named mechanism is an honest negative (Rule 11), not a failure to paper over.

### §5.2 — SM / interpretive counterfactual (`ave-discrimination-check`)

- **SM-counterfactual:** the Standard Model has **no geometric origin for α** at all — it is a measured input. So *any* outcome where α⁻¹ traces to the (2,3) Golden-Torus geometry (even Level-1 Class B) is **AVE-distinct in mechanism**. But mechanism-distinctness is **not** emergence: only Outcome A (Level 2, Class D) is a genuine *prediction* of α from substrate primitives; Outcome B is an AVE-distinct *consistency* framing. The discrimination that matters for the chord is **internal** (A vs B), and it is decided by the INPUT/OUTPUT column + (C2), not by distinctness from SM.
- **Interpretive alternative to rule out:** a tuned leak strength hitting 1/137 by accident — ruled out by the §4.3 joint-ledger requirement (the Golden-Torus must *also* self-assemble and the mₑc² ledger must *also* close at the same operating point; a fluke α won't carry the joint set).
- **`ave-evidence-framing-discipline`:** Outcome B must NOT be headlined as "α emergence" or "the chord." It is "the engine hosts the electron; α is a calibration." The emergence headline is reserved for Outcome A with both conditions verified.

---

## §6 — Guards, skills, and the corpus tensions surfaced (flag-don't-fix)

### §6.1 — Corpus-internal tensions surfaced (`flag-don't-fix` — NOT silently resolved)

Both surfaced with verbatim evidence + both file paths; I did **not** reframe one to match the other. These are for Grant adjudication.

**TENSION 1 — is the trapped electron TRANSVERSE or LONGITUDINAL?** The canonical leaf clm-i4p11y says transverse; the no-QED design (+ three other canonical anchors) says longitudinal:
- `vol1/claim-quality.md:1298,1303` (clm-i4p11y): *"The electron is a self-trapped photon … The **trapped transverse standing wave** is the electron."*
- vs `de-broglie-standing-wave.md:50` (*"longitudinal acoustic pressure waves governed by the vacuum's Bulk Modulus"*) + `solver-toolchain.md:395` (*"traps a longitudinal wave"*) + `biquaternion-…-result.md:55,235` (*"electron = trapped longitudinal wave"*) + the Grant 2026-06-09 no-QED directive.
- **Candidate reconciliation (NOT adjudicated):** clm-i4p11y describes the **seed + trap mechanism** (a transverse photon is what arrives, TIR is what catches it), while the no-QED design describes the **trapped end-state** (longitudinal bulk), with genesis = the transverse→longitudinal **conversion** in between. Under that reading both are right about different stages. **But clm-i4p11y's literal "the trapped transverse standing wave IS the electron" is in direct tension with "the electron is the longitudinal bulk."** Does the crystal-engine longitudinal-trap **supersede** clm-i4p11y (Rule 12 retraction of the transverse-end-state wording), or **coexist** (clm-i4p11y = seed/mechanism, design = end-state)? **Load-bearing for what the engine traps on the bulk branch. → Grant.**

**TENSION 2 — is genesis a SINGLE-sector saturation flip or a TWO-branch energy transfer?** (the A44 missing-axiom-vs-engine-bug question, already half-surfaced by genesis-23 §9):
- `master-equation.md:18`: *"the longitudinal **re-engages** at saturation = the electron"* — reads **single-sector** (one mode changes character at V_yield; L3 `54_§6a:246` *"single-sector mode conversion"*).
- vs this design's ADD-2 converter = **two-branch** transfer (transverse shear *pumps* the longitudinal bulk).
- genesis-23 §3 empirically found **no ω→V source** in the coupled engine — consistent with "the corpus mode-conversion is single-sector, and a two-branch source is a NEW primitive that may or may not be canonical." **Is the two-branch shear→bulk SOURCE an Ax-1–4 consequence (engine-completeness gap) or a new postulate?** Must be adjudicated against the axioms BEFORE the converter is built. **→ Grant.** (Per `ave-fundamental-ground-up-implementation`: if it traces to Ax 1+4, derive it; if it needs a new postulate, that is a separate versioned hypothesis, not a silent engine add.)

### §6.2 — Third open framing question (the emergence ceiling)

**Q3 — can the Golden-Torus geometry self-assemble at all?** (C2) is the hard, unproven step. genesis-23 GAP-1 found the longitudinal sector never even *energizes* from a transverse photon (let alone self-organizes its φ²/quarter-screening geometry). The honest prior: **(C2) is the most likely point of failure**, which is why Outcome B (planted geometry, Class B) is my modal prediction and Outcome A (self-assembled, Class D) is the genuine long shot. The design does not pre-suppose (C2) succeeds; it makes (C2) the explicit discriminator. **No methodology pivot is proposed here** (Rule 16) — if (C2) fails, that is a clean Outcome-B/C result to return to Grant + corpus.

### §6.3 — Skill-application ledger (this design)

| Skill | Where applied |
|---|---|
| `substrate-native-check` | CP1 wave-not-minimization (§3.3); CP2 V-sector bound-state (§3.3); CP8 seed precursor=photon+saturated-seed not planted (2,3) (§3.3); CP9 dynamical converter + dynamical leak (§3.2, §4.2); CP10 trap+conversion as boundary not bulk (§3.1, §3.2) |
| `ave-prereg` | corpus-grep §0.0 (PARTIAL, not green-field; GAP-1 the lone missing primitive); physical picture in 5 bullets; dimensional/elastic provenance from ν_vac=2/7 |
| `ave-fundamental-ground-up-implementation` | ΔE_cryst derived (path α) not Landau-defaulted (§3.3); branch moduli from ν_vac=2/7 not free knobs (§0.1); converter coupling from (2,3) topology (§3.2) |
| `consistency-vs-emergence` | the Class-D-vs-Class-B ladder IS the test (§4.1); Step-3/4 circularity (α in coupling AND in $V_{yield}$, §2.2); Class-E joint-constraint as fluke-guard (§4.3); honest framing of Outcome B (§5.2) |
| `ave-canonical-source` | all knobs from `constants.py`/axioms; zero new free params (§3.4) |
| `ave-discrimination-check` | SM-counterfactual + fluke-α alternative (§5.2) |
| `phase-space-coordinate-check` (A46) | (2,3)+Golden-Torus measured in (V_inc,V_ref) Layer 3, not real-space (§4.2) |
| `ave-conserved-vs-pumped` | latent heat = the one pumpable/energize+lock channel; charge/spin/winding conserved (§1.4) |
| `verify-before-cite` | every file:line opened/greped this session (§0.0 table + inline); two tensions caught by reading the actual leaves |
| `flag-don't-fix` | TENSION 1 + TENSION 2 + the double-deflection:33 terminology nuance surfaced verbatim, not resolved |

---

## §7 — What to build (the implementer task that follows this design)

This is a DESIGN. The build + run is the follow-on. **Blocking gate:** the two §6.1 tensions (esp. TENSION 2, the A44 single-sector-vs-two-branch question) should be put to Grant **before** ADD-2 is coded — per Rule 16, ask before design-freeze of the converter, not after 30 commits return Mode III.

### §7.1 — Build order (each step gated on the prior)

1. **Bulk branch (ADD-1, lowest risk):** wrap/reuse `MasterEquationFDTD` as the longitudinal branch. Confirm the v14 Mode I breathing soliton reproduces (the trapped longitudinal mass) in engine-natural units ($V_{yield}=1$). *Exit:* stable breathing bound state, α-free.
2. **Transverse branch (exists):** the Cosserat ω-photon seed (`CosseratField3D`, `initialize_gaussian_wavepacket_omega`, helicity ±1) — the genesis-23 precursor. *Exit:* clean transverse photon, Z₀-matched, V-sector silent at $t=0$.
3. **The converter (ADD-2, the load-bearing new primitive — GATED on Grant TENSION-2 adjudication):** implement $\Sigma_\chi$ as a **dynamical, boundary-localized, α-free ($\kappa\tilde{}=6/5$) source** that adds to bulk $V$ even at $V\equiv0$, chirality-biased by $h$. *Exit (the GAP-1 closure check):* $\max|V_{inc}| > 0$ from a transverse photon seed (genesis-23's machine-precision-zero must become nonzero) — the single empirical fact that says the longitudinal "3" finally energizes.
4. **Crystallization order parameter (ADD-3):** $F(\eta)$ double-well with $\Delta E_{cryst}$ derived (path α) from the A-034 kernel + two-walls ledger; nucleate on (photon + saturated seed). *Exit:* a frozen crystallite forms (first-order, not gradient-relaxed).
5. **Run the §4 discriminating test:** verify (C1) by grepping the parameter feed for α/√α; measure the (2,3) winding + Golden-Torus $R,r$ in (V_inc,V_ref) phase-space (A46); measure the bulk→shear leak $\hat{Q}^{-1}$ dynamically (CP9) with the reactance pair recorded (CP6) and PML excluded (CP7); check (C2) self-assembly vs planted; close the §4.3 joint ledger. *Exit:* Outcome A / B / C with the α-column + (C2) recorded from the run, not argued after.

### §7.2 — Pre-registered artifacts the build session must produce

- a driver `src/scripts/vol_1_foundations/crystal_engine_alpha_emergence.py` writing a results JSON + phase-space figures;
- a result doc `research/2026-06-09_crystal-engine-alpha-emergence_result.md` reporting A/B/C with the §4.1 level (0/1/2), the INPUT/OUTPUT column α sat in, and the (C1)/(C2) verification verbatim;
- DERIVED / VERIFIED / BLOCKED ledger (genesis-23 format);
- **no genesis claim** unless the full §4.3 joint signature closes with (C1)∧(C2) (`ave-evidence-framing-discipline`).

### §7.3 — Corpus-state updates this design queues (auditor lane LANDS these; implementer SURFACES)

- `vol4/claim-quality.md:232` strengthen-by — when the build runs, it either discharges (Outcome A) or refines (Outcome B/C) the α-emergence-circularity caveat; the auditor updates clm-... accordingly.
- TENSION 1 (clm-i4p11y transverse-vs-longitudinal) — pending Grant; if he rules "supersede," that is a Rule-12 retraction on clm-i4p11y's transverse-end-state wording (auditor lands; I do not edit the leaf here).
- TENSION 2 (A44 single-sector-vs-two-branch) — pending Grant; gates ADD-2; may become a new versioned hypothesis (own verification chain) rather than an engine add.
- the `closure-roadmap.md:42` $\Delta E_{cryst}$ OPEN closure path — the crystal engine is a candidate route; status update only after the run.

### §7.4 — What this design does NOT do (lane discipline)

- Does **not** build the engine (design only).
- Does **not** draft the Ax-5 / new-postulate resolution of TENSION 2 (A44: adjudicate vs Ax 1–4 first; `flag-don't-fix`).
- Does **not** edit clm-i4p11y or any KB leaf (auditor lane lands corpus changes).
- Does **not** drop any of the 5 joint-ledger legs or the (C1)/(C2) conditions to ease a pass (Rule 11).

---

### Provenance footer

All file:line citations in this doc were opened or greped during the 2026-06-09 authoring session (`verify-before-cite`). Engine + constants anchors: `src/ave/core/master_equation_fdtd.py`, `src/ave/core/constants.py:200-205`, `src/ave/topological/cosserat_field_3d.py`. Canonical KB anchors: `manuscript/ave-kb/{CLAUDE.md, common/two-engine-architecture-a027.md, common/solver-toolchain.md:395, common/trampoline-framework.md, vol1/claim-quality.md:1303, vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md:18, vol2/quantum-orbitals/ch07-quantum-mechanics/de-broglie-standing-wave.md:50-52, vol3/gravity/ch02-general-relativity/double-deflection.md:26,33, vol3/claim-quality.md:590,808, vol4/claim-quality.md:232, vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:128, claim-quality-closure-roadmap.md:42}`. Research anchors: `research/2026-06-09_reflection-genesis-23-self-assembly_result.md`, `research/2026-06-08_vacuum-as-chiral-piezoelectric.md`, `research/2026-06-06_biquaternion-node-algebra-result.md`, `research/_archive/L3_electron_soliton/{54_pair_production_axiom_derivation.md, 66_single_electron_first_pivot.md}`.

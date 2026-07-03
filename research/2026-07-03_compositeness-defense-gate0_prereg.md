# FROZEN PREREG — Compositeness-Defense Gate-0 (analytic)

**Docket:** B2 (COMPOSITENESS-DEFENSE arc), Grant-commissioned 2026-07-03.
**Lane:** research / analytic derivation (bounded). HOLD canonization. NO self-merge — push + report.
**Branch:** `analysis/compositeness-defense` (off `origin/main` @ `e06b6e9d`, post PR #470).
**Prereg status:** FROZEN at first commit. Bins + bounds table + robustness ladder do not move post-freeze.
**Companion result doc (gated):** `research/2026-07-03_compositeness-defense-gate0_result.md` (written AFTER this freezes).

**Disciplines applied (declared up front):**
`substrate-native-check` (walk below, §0) · `pre-test-physics-check` (Trigger 8 ontology gut-check + Trigger 9 fork-to-computable — question surfaced to Grant at dispatch, adjudication recorded §1.4) · `phase-space-coordinate-check` (§0 CP4) · `consistency-vs-emergence` (bin classification §5) · `verify-before-cite` (every file:line re-verified against `origin/main` @ `e06b6e9d` this session) · `flag-don't-fix` (contradictions surfaced, none resolved) · `ave-prereg` Step 3.7 (robustness ladder §3) · `ave-discrimination-check` Step 2.7 (dictionary-translated counterfactual §4).

---

## 0. SUBSTRATE-NATIVE WALK (before any derivation)

Per `substrate-native-check`. This is an analytic Gate-0; the "code" is the scattering-amplitude / form-factor derivation, walked substrate-natively so SM/QED defaults (a charge-density ρ(r) with a Fourier form factor by default; a continuum-Helmholtz probe; an energy-basin electron) do not leak in.

- **CP1/CP2 — sector.** The observable is a scattering form factor F(q²) for a hard EM probe. The probe is a transverse EM wave living in the **EM-transverse channel** (Z_EM ≡ Z₀). Three distinct substrate objects carry the three candidate observables, and they live in **different sectors** — do not cross-wire (sector-ownership discipline):
  - Charge 𝓠 = Link(∂Ω, F) ∈ ℤ — a **1D boundary line-integral integer** (`boundary-observables-m-q-j.md:20`), NOT a bulk density ρ(r). Couples to the EM probe through the **matched, gapless** EM channel (Γ_EM = 0, massless ⇒ pure 1/r).
  - The Γ=−1 confinement wall — a **bulk/shear-channel** boundary (Z_bulk, Z_shear → 0). The **EM channel is impedance-matched at the wall** (Γ_EM = 0; `electron-bh-isomorphism.md:24`, `bulk-impedance-at-saturation-boundary.md:71`).
  - The moment 𝓙 / winding circulation — the magnetic form factor F₂, mediated by the **gapped ω (Cosserat rotation) sector** (`clm-wcoul2`; Yukawa, short-range, `claim-quality.md:1624`).
- **CP3 — AVE-native objective.** The form factor is the exterior EM readout of the boundary source, NOT an energy-minimization of a charge cloud. F₁(q²) is fixed by whether the **exterior EM field of the boundary integer is exactly Coulombic (1/r)** — the substrate-native question, not a ρ(r)-Fourier-transform question.
- **CP4 — phase-space vs real-space (`phase-space-coordinate-check`).** The (2,3) is the **phase-space** (Clifford-torus) winding label; the real-space body is the 0₁ unknot at loop 2π·ℓ_node ≈ 2.4e-12 m. A scattering form factor is a **real-space** quantity (Fourier conjugate to momentum transfer q). The corpus claim being defended (no-hair, F-channel behavior) must be measured in the **exterior real-space field profile**, not in phase-space φ² coordinates. The (2,3) phase-space label does NOT by itself answer compositeness (synthesis A4) and must not be quoted as if it did.
- **CP10 — boundary-not-bulk.** The confinement is a **boundary condition** (Γ at a surface), not a bulk confining potential. The wall is bulk/shear; the EM probe sees the matched channel. Render the wall as Γ(q) at a surface if the engine leg runs, never as a bulk energy term.

**Walk verdict:** the derivation lives in the **EM-transverse channel** (for F₁, charge) and the **gapped-ω channel** (for F₂, moment), on the **real-space exterior field** of a **boundary-integer** source. The wall channel (bulk/shear) is largely settled by the corpus (Γ_EM = 0, §1.3) and enters only as "is the EM channel exactly matched at all q, or does the wall's finite thickness imprint at qℓ_node ≳ 1."

---

## 1. THE ONTOLOGY FORK (for adjudication by derivation)

### 1.1 The three candidate channels (dispatch's ontology fork)

The dispatch surfaced three candidate couplings for a hard probe. Substrate-native, they are NOT exclusive — they are **three different sectors carrying three different observables**:

- **(i) Charge = boundary linking integer 𝓠 ∈ ℤ.** Topological, scale-free. Candidate conclusion: F₁(q²) ≡ 1 at all q² (pointlike by construction) — the probe cannot resolve a distributed ρ(r) because the substrate has none.
- **(ii) The Γ=−1 wall as a geometric scatterer.** Candidate conclusion: geometric structure imprints at qℓ_node ≳ 1.
- **(iii) The winding circulation (moment).** NOT topologically protected. Candidate conclusion: deviations live in F₂, bounded by g−2 at ~1e-12.

### 1.2 Channel (ii) is largely PRE-SETTLED by the corpus (verify — DEFENSE-DERIVED at the impedance level)

**Verified verbatim this session** (`verify-before-cite`, `origin/main` @ `e06b6e9d`):
- `electron-bh-isomorphism.md:24`: *"gravity is Symmetric in the EM-transverse channel: the characteristic impedance Z_EM(r) = √(μ'(r)/ε'(r)) = Z₀ is invariant at all radii, because both μ' and ε' scale identically with n(r). There is no EM impedance mismatch and no EM reflection coefficient (Γ_EM = 0 everywhere under SYM scaling)."*
- `bulk-impedance-at-saturation-boundary.md:71` (electron row): *"EM channel: Z_EM = Z₀ (matched vacuum); confinement is not EM-short."*
- `three-channel-impedances.md:20`: EM-transverse row, *"Γ_EM = 0 (SYM gravity)."*
- `translation-circuit.md:541` (δ↔Γ conjugate): matched (Γ=0, photon) → δ → ∞ (transparent); *"the evanescent tail leaking out is the long-range (~ℓ_node/r Coulomb) field, i.e. how a trapped soliton couples to the outside vacuum."*

**Consequence:** a transverse EM hard probe does **not** see the electron's Γ=−1 wall as a mirror. The EM channel is impedance-matched (transparent, δ→∞), so candidate (ii) does **not** produce a wall-reflection form factor. The wall is a bulk/shear object; the EM probe is in the matched channel. **Candidate (ii) collapses at the impedance level** — this is DEFENSE-DERIVED and corpus-cited, not something Gate-0 must re-derive. Gate-0's job on (ii) is only the residual: *does the finite EM channel matching hold exactly at all q, or does the wall's finite thickness / the tail's departure from exact 1/r imprint at qℓ_node ≳ 1?* — which folds into channel (i)'s tail question below.

### 1.3 The narrowed fork (the one thing the derivation must settle) — SHARPENED

The fork is NOT "(a) integer-count vs (b) tail-readout." A form factor measures the **SOURCE's departure from a point**, not the field's extent. An exactly-1/r exterior tail **IS** the point-charge field and gives F₁ ≡ 1 identically (Rutherford off pure Coulomb has F = 1). So the fork is narrower:

- **(a) Exterior EM readout is exactly Coulombic (1/r) at all r ≥ ℓ_node.** ⇒ F₁(q²) ≡ 1 exactly, all q². The boundary integer's field reaches the far zone as a pure point-charge Coulomb field; the 1/r shape carries no form-factor structure. DEFENSE-DERIVED in the charge channel.
- **(b) Exterior EM readout carries a derived ℓ_node-scale DEPARTURE from exact 1/r** (e.g. the tail is (ℓ_node/r)·[1 + f(ℓ_node/r)] with f ≠ 0, or the boundary source has a resolved finite profile). ⇒ F₁(q²) = 𝓕[departure profile], deviating from unity at qℓ_node ≳ 1.

**The corpus asserts the 1/r shape but has NOT derived it is EXACTLY Coulombic.** Flag (`flag-don't-fix`): `translation-circuit.md:541` gives the tail as "~ℓ_node/r" (1/r shape), but `claim-quality.md:1311` records an **open item**: *"WHY topological strain equals ℓ_node/r rather than α·ℓ_node/r from first principles is an open multi-week analytical item."* So the exact-Coulombic property (a) is **asserted-not-derived** in the corpus. Gate-0 must formalize whether the exterior charge readout is exactly Coulombic ⇒ (a) derived, defense closes; or carries a derived ℓ_node-scale departure ⇒ (b), compute F₁(q²) and check the bounds table.

### 1.4 Adjudication (recorded per pre-test-physics-check Step 5)

**Ontology question surfaced to Grant at dispatch** (Trigger 8/9): *is the electron's charge a counted boundary integer whose exterior field is exactly Coulombic (⇒ F₁ ≡ 1), or is it read off a leaking-tail profile that departs from 1/r at ℓ_node scale (⇒ F₁ deviates)?*

**Standing adjudication (Grant-ratified fork-to-computable pattern, coordinator-relayed 2026-07-03, Grant retains mid-flight veto):** proceed with **both readings frozen as bins**, with a **validate-on-known anchor** deciding which earns canon. Grant's demonstrated standing preference is (b)-in-the-skill-sense = "adjudicated by engine, not fiat." Three sharpenings baked in (this prereg §1.3, §2 asymmetric stakes, §0 CP2 channel-separation).

---

## 2. THE ASYMMETRIC-STAKES PRE-REGISTRATION (bake in before running)

Pre-registered so a (b)-with-departure outcome is not mis-framed as a chord:

Any O(1) ℓ_node-scale structure in the **charge channel** is a shell-like form factor (sinc(qR)-class) that deviates at q ≳ m_e — a region measured to α-precision and contact-interaction-bounded to **Λ ≳ 10 TeV ≈ 10⁵ × (1/ℓ_node)**. Therefore:

- **(b)+departure in F₁ → run the bounds table EXPECTING EXCLUSION.** The chord room in the charge channel is ~zero: any ℓ_node-scale F₁ departure is already ~5 orders inside the LEP contact bound. A (b) outcome lands in **EXPOSURE-CONFIRMED** almost automatically, NOT chord territory.
- **The honest chord room lives in the MOMENT channel (F₂)** — a sub-g−2 correction with a specific q²-shape — and in any **sub-bound tail correction** to F₁ (a departure so small it sits below the contact bound). Not in an O(1) F₁ departure.

This is pre-registered so the result doc cannot retroactively re-label an F₁ exclusion as a chord.

---

## 3. THE ROBUSTNESS LADDER (declared BEFORE freezing, per ave-prereg Step 3.7)

Under honest knives observables dissolve downward: **magnitude → ratio → sign/shape → existence**. Declared per channel, form-end primary:

| Channel | PRIMARY (gating) rung | Secondary | Last |
|---|---|---|---|
| F₁ (charge) | **EXISTENCE/SIGN** of any deviation from the dictionary-translated QED prediction (QED tree-level: F₁ ≡ 1) | q²-shape of any departure | magnitude of departure |
| F₂ (moment) | **EXISTENCE/SIGN** of any deviation from QED's Schwinger a_e = α/2π (dictionary-translated) | q²-shape | magnitude (ω_gap = host-knob ⇒ magnitude BLOCKED, per clm-wcoul2 — pre-declared) |
| Wall (ii) | **EXISTENCE** of any EM-channel reflection Γ_EM(q) ≠ 0 at high q (primary is: does Γ_EM stay 0?) | Γ(q) shape | magnitude |

**Pre-declared demotion survivors:** if F₂ magnitude proves knob-ridden (ω_gap is a host knob, not Ω_C — `claim-quality.md:1624`), the surviving claim is the **sign/existence** of the moment correction and its **channel** (gapped-ω, electric-not-magnetic), NOT any magnitude. This is pre-registered so the demotion is not discovered mid-arc.

**Gate-floor consistency (Step 3.7b):** the bounds-table comparison (§below) is a magnitude check; it gates only on channels where a magnitude is derivable. For channels where magnitude is BLOCKED (F₂ moment, per ω_gap host-knob), the gate reads existence/sign only and does NOT demand a magnitude verdict — no gate asks a blocked-magnitude cell for a number.

---

## 4. THE PRIOR-ART BOUNDS TABLE (frozen up front; auditor-supplied physics, marked as such)

**Auditor-supplied external physics** (not corpus content; standard-model / experimental literature, marked as scaffolding per synthesis B4 discipline). Every derived deviation checks against this table BEFORE any chord language (survival-before-opportunity). Values are order-of-magnitude literature figures for the derivation to compare against; the derivation does not re-derive them.

| # | Bound (observable) | Value / scale | Channel it constrains | Notes |
|---|---|---|---|---|
| B1 | g−2 / F₂(0) anomaly agreement | electron a_e matches QED+experiment to ~1e-12 (the SHARPEST) | F₂ (moment) | The tightest knife. Any AVE F₂ deviation must sit below ~1e-12 fractional. |
| B2 | LEP contact-interaction scale Λ (eeℓℓ / eeqq) | Λ ≳ 10 TeV ⇒ probed structure ≲ ~1e-19 m ≈ 10⁵ × (1/ℓ_node) | F₁ (charge), 4-fermion effective operator | 4-fermion EFT limit; translation to a topological-soliton extent is non-trivial (synthesis A1). |
| B3 | LEP/SLC Bhabha + e⁺e⁻→e⁺e⁻ dσ/dΩ | agreement with QED to sub-% across √s up to ~200 GeV | F₁ + F₂ (differential cross-section) | Tests the full q²-dependence, not a single scale. |
| B4 | Low-q² Møller (E158-class) | parity-violating asymmetry matches SM to ~% | ee correction (incl. any short-range ω-mediated term) | Where a short-range gapped-ω e-e correction would live (future-work note, §6). |
| B5 | Electron "radius" as usually quoted | r_e < ~1e-18–1e-22 m (from g−2 / high-energy scattering) | F₁ / F₂ extent | The naive "size" bounds; ℓ_node ≈ 3.86e-13 m is ~5–9 OOM larger (the naive tension). |

**Reference scales (corpus-verified, `constants.py`):** ℓ_node = ℏ/(m_e c) ≈ 3.86e-13 m (`:282`); loop length 2π·ℓ_node ≈ 2.4e-12 m; ω_C = c/ℓ_node ≈ 7.76e20 rad/s with ℏω_C = m_e c² = 511 keV EXACTLY (`:294`). The Compton frequency ω_C IS the wall's bandwidth scale — "above the wall's bandwidth" = "above m_e" = where QED's own structure (pair production) turns on. Gate-0 tests whether this coincidence is a derived consistency or a coincidence.

### 4.1 The dictionary-translated counterfactual (per ave-discrimination-check Step 2.7)

Before any AVE-distinct verdict, translate QED's prediction through AVE's own identification map (Ax2 winding=charge, TKI [Q]≡[L], spin=rotation-DOF) and compare against THAT:

- **QED's electron is NOT pointlike-at-all-scales in observables** — it has Compton-scale structure: the Compton cross-section, Schwinger a_e = α/2π. "Pointlike" experimentally = agrees with QED's PREDICTED q²-dependence (Dirac + radiative). The question is never "does AVE have structure at 2.4e-12 m" (QED does too) but "does AVE's soliton scattering DEVIATE from QED's prediction at any measured q²."
- **Dictionary-translated F₁:** QED tree-level F₁(q²) ≡ 1 (Dirac point charge). Under Ax2 (charge = boundary integer), the topological argument ALSO gives F₁ ≡ 1. **If AVE's F₁ ≡ 1, that MATCHES QED — COULOMB-RECOVERY consistency, NOT a chord** (same lesson as clm-wcoul2: a match to the dictionary-translated competitor is consistency, not distinctness). Booking F₁≡1 as an AVE chord would mint a "chord" QED already predicts.
- **Dictionary-translated F₂:** QED gives a_e = α/2π + higher order. Under AVE's map the moment lives on the winding circulation (gapped-ω). An AVE F₂ that reproduces α/2π is CONSISTENCY (echo — the α is baked, per the g−2 coverage-matrix row `clm-stgx1i`); an AVE F₂ that adds a DISTINCT sub-bound q²-shape QED does not predict is the only chord candidate.

**Pre-registered discrimination verdict shape:** F₁ ≡ 1 → consistency (defense, not chord). F₂ = α/2π → consistency (echo). The ONLY chord room = a distinct, sub-bound, q²-shaped F₂ correction (or sub-bound F₁ tail correction) with a named future sensitivity.

---

## 5. FROZEN BINS

Classification per `consistency-vs-emergence`. Bins do not move post-freeze.

- **[DEFENSE-DERIVED]** — the charge channel is topologically pointlike (F₁ ≡ 1 by the boundary-integer argument, made rigorous: the exterior EM readout is derived exactly Coulombic) AND the wall channel stays EM-matched (Γ_EM(q) = 0 up to the relevant scale) AND the moment channel's deviation falls below all bounds (B1 sharpest). ⇒ the compositeness gap CLOSES with a derivation. Update the coverage-matrix compositeness row + `boundary-observables-m-q-j.md` with the q²-conditioned no-hair statement. Class: DEFENSE / CONSISTENCY (F₁≡1 matches dictionary-translated QED).
- **[CHORD-CANDIDATE]** — a channel's derived deviation (realistically only F₂, or a sub-bound F₁ tail correction) has a specific q²-shape sitting BELOW current bounds but ABOVE a named future sensitivity. ⇒ survival + a forward prediction. Register-entry drafted (UNBUILT class). Must survive the dictionary-translated counterfactual (§4.1) to be called a chord.
- **[EXPOSURE-CONFIRMED]** — a derived deviation exceeds a measured bound. Per §2 asymmetric stakes, an O(1) ℓ_node-scale F₁ departure (reading (b)) lands here almost automatically (5 OOM inside B2). ⇒ the extended-electron model is in live falsification territory at that observable. Book honestly, no rescue (Rule 11).
- **[ILL-DEFINED]** — the wall-probe / tail-departure interaction isn't derivable at current corpus grade (e.g. the exact-Coulombic-vs-departure question needs the held engine leg to pin Γ(q) / the tail profile numerically). ⇒ named blocker + what's missing; the engine leg (§7) is triggered.

---

## 6. THE DERIVATION PLAN (what the result doc works)

Three channels, substrate-native, dictionary-translated at every step:

- **(i) Charge / F₁ — the topological-charge argument.** Make it rigorous or break it: under what assumptions does "the probe couples only to the boundary linking number" hold? Does Link enter as a delta-normalized integer (⇒ F₁ ≡ 1) or convolved with a wall/tail profile (⇒ F₁ = 𝓕[profile])? Formalize whether the exterior EM readout is exactly Coulombic (reading (a)) or carries a derived ℓ_node-scale departure (reading (b)). Use the boundary-observability rule + the substrate-observability derivation; state what it does NOT cover (the moment).
- **(ii) Wall / Γ_EM(q).** The Γ=−1 surface as a scatterer to a transverse EM probe of λ ≪ ℓ_node. Confirm/challenge Γ_EM(q) ≈ 0 (matched) at high q from the SYM-scaling mechanism. Test the ω_C = c/ℓ_node = Compton-frequency coincidence: is "above the wall's bandwidth = above m_e = where QED pair-production structure turns on" a DERIVED consistency or asserted? Derive, don't assert.
- **(iii) Moment / F₂.** The winding circulation's contribution to F₂. Order-of-magnitude against B1 (g−2). Does AVE's Compton-scale circulation reproduce Dirac g=2 + α/2π (consistency/echo) or fight it? Cite the existing g=2 + g−2 Petermann rows (`electron-identification.md:57–59`, verified this session: g=2 is POSITED-not-derived per 2026-06-21 Rule-12 re-scope; g−2 Petermann is +4.0% parameter-free / 50ppm postulate-conditional). Keep the gapped-ω (F₂) channel SEPARATE from the gapless-EM (F₁) channel — the Yukawa screening must NOT leak into the EM charge readout (§0 CP2, sector-ownership).

**Channel-coherence consistency gate (per sharpening #3):** verify the derivation keeps EM (matched, gapless, 1/r, F₁) and ω (gapped, Yukawa, short-range, F₂) channels separate. e-e interaction = long-range EM Coulomb + short-range gapped-ω correction, coexisting. If the substrate says the Yukawa leaks into the EM readout, that is a FINDING to surface (`flag-don't-fix`), not smooth over.

---

## 7. HELD — the engine scattering leg (gated successor; DO NOT START)

The engine leg (probe-wave-on-seeded-knot in the writhe-campaign machinery host) is **HELD** pending the analytic Gate-0 verdict. It is triggered ONLY if the analytics land **ILL-DEFINED** or need numerical confirmation of a specific Γ(q) / tail-profile claim.

**Its own frozen bins (declared now so the successor doesn't reframe):**
- **[TAIL-EXACT-COULOMB]** — the seeded-0₁ exterior EM field is 1/r to numerical tolerance at r ≥ ℓ_node ⇒ confirms reading (a), F₁ ≡ 1. DEFENSE-DERIVED numerically.
- **[TAIL-DEPARTS]** — a resolved ℓ_node-scale departure from 1/r ⇒ reading (b); extract F₁(q²), run bounds table (expect exclusion per §2).
- **[GAMMA-EM-NONZERO]** — Γ_EM(q) departs from 0 at high q ⇒ the wall is not EM-transparent at all scales; extract the reflection form factor, run bounds table.
- **[ENGINE-BLOCKED]** — the writhe host cannot resolve the exterior tail at the required r/q (screening / overlap / host-knob ω_gap, per clm-wcoul2 caveats) ⇒ named engine-capability gap, not a physics verdict.

Host: `src/scripts/vol_4_engineering/writhe_gate0_pair_feasibility.py` machinery + the clm-wcoul2 seeded-knot / self-subtracted T⁰ⁱ tooling. Substrate-native-check trigger 8 (emergence/hosting) + CP10 (Γ boundary, not bulk force) apply IF it runs.

---

## 8. REPORTING SPEC (per dispatch)

Final message reports: the bin fired, the three-channel verdicts (F₁/charge, wall/Γ_EM, F₂/moment), the bounds-table comparison, the ontology-fork resolution (which candidate the derivation selected), PR number, blockers. If a framing-level fork the derivation cannot settle surfaces (pre-test-physics-check trigger 9), STOP and surface with the fork-to-computable option rather than picking.

**PR title:** `research(compositeness): Gate-0 analytic defense derivation — [bin fired]`.

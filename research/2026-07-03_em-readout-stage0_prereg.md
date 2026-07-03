# FROZEN PREREG — EM-readout derivation, Stage 0 (analytic)

**Epic:** EM-readout derivation — Axiom-2's last underived leg.
**Charter:** [`_orchestration/2026-07-03_em-readout-derivation-charter.md`](../_orchestration/2026-07-03_em-readout-derivation-charter.md) (canonized this branch, commit `240cd1e2`).
**Lane:** research / analytic derivation (bounded). HOLD canonization. NO self-merge — push + open PR.
**Branch:** `analysis/em-readout-stage0` (off `origin/main` @ `5bdc8d41`, post PR #472).
**Prereg status:** FROZEN at this commit. The question statement, investigation lanes, robustness ladder, ledger format, bins, and validate-on-known anchors do NOT move post-freeze. The result doc is written AFTER this freezes.
**Companion result doc (gated):** `research/2026-07-03_em-readout-stage0_result.md`.

**Grant's ontology ruling (verbatim, charter §3):** *"let the derivation find it, come to me if you get stuck."* No mechanism is pre-committed. The four candidate classes below are INVESTIGATION lanes, not a menu to pick from before deriving. Framing-level stuck-points route to Grant (the [STUCK] bin + the plumber-question formulation).

**Disciplines applied (declared up front):**
`substrate-native-check` (walk §0) · `ave-canonical-leaf-pull` (leaf enumeration §0.1 — this is a coupling-class problem) · `consistency-vs-emergence` (every step tagged; class declared §6) · `ave-discrimination-check` Step 2.7 (dictionary-translated counterfactual §5) · `verify-before-cite` (every file:line re-verified against `origin/main` @ `5bdc8d41` this session) · `flag-don't-fix` (contradictions surfaced, none resolved) · `pre-test-physics-check` trigger 9 (fork-to-computable if a framing fork surfaces mid-derivation → [STUCK]) · `phase-space-coordinate-check` (§0 CP4) · `ave-prereg` Step 3.7 (robustness ladder §3) · INVARIANT-N1 (substrate nouns prose-only).

---

## 0. SUBSTRATE-NATIVE WALK (before any derivation)

Per `substrate-native-check`. This is an analytic Stage-0; the "code" is the field-derivation, walked substrate-natively so SM/QED defaults do not leak in. The defaults that leak by construction on THIS problem:

- **the SM charge-density default** — a bulk charge density ρ(r) with a Fourier form factor. AVE has NO ρ(r): charge is a boundary linking integer 𝓠, a 1D line-integral observable (`boundary-observables-m-q-j.md:20`), not a distributed density. Do NOT insert ρ = 𝓠·δ³(r) and Poisson-solve — that inserts the answer (see §4 the un-riggability trap).
- **the continuum-Helmholtz / Poisson-solver default** — reaching for ∇²φ = −ρ/ε₀ as the field equation. AVE's field equation is Axiom 3's action (§0.2 below), which as-written is TRANSVERSE (curl-only); whether it even CONTAINS the electrostatic sector is part of what Stage-0 must settle, not assume.
- **the energy-basin default** — treating the electron's exterior field as the minimizer of an electrostatic energy functional of a charge cloud. AVE's electron is a self-trapped standing wave (a boundary-condition object at a Γ=−1 surface, `electron-identification.md:24-29`), not a charge cloud in a potential well.

### 0.1 Canonical-leaf enumeration (the coupling-class leaf-pull — done BEFORE deriving)

Per `ave-canonical-leaf-pull` (coupling-class: winding→field). The load-bearing canonical leaves, verified verbatim this session @ `5bdc8d41`:

| # | Leaf | What it fixes | verified line(s) |
|---|---|---|---|
| L1 | `vol1/…/axiom-definitions.md` | Ax1 6-DOF per node: 3 translational (ε₀/E, capacitive) ⊥ 3 microrotational (μ₀/B, inductive), LC-coupled; Ax3 action `L = ½ε₀\|∂ₜA\|² − ½μ₀⁻¹\|∇×A\|²` (transverse/curl-only) | :16, :38–48 |
| L2 | `common/boundary-observables-m-q-j.md` | 𝓠 = Link(∂Ω, F) ∈ ℤ, a 1D line/loop integral, EE-projection = charge Q; no-hair (interior invisible; only 𝓜, 𝓠, 𝓙 externally measurable) | :20, :31–37 |
| L3 | `vol1/…/k4-port-irrep-decomposition.md` | K4 4-port = A₁ ⊕ T₂. A₁ (common-mode, +1 eigenvalue) = translational u, longitudinal, propagates c√2, DISSIPATES (Op3 destructive interference; "Gauss's law forbids longitudinal EM"). T₂ (−1 triplet) = microrotational ω = the photon, transverse | :11, :22–29, :108–112, :120–123 |
| L4 | `common/historical-precedents.md` | The Heaviside excision + the DECISIVE Rule-12 precision note: "Gauss forbids longitudinal EM" is precise only for a *propagating* longitudinal WAVE — the **static Coulomb-longitudinal E is KEPT by Gauss's law itself** (∇·E = ρ/ε₀ is a longitudinal component). "The electron is where it returns: saturation is a volumetric/longitudinal effect… the longitudinal scalar re-engages as the confined state." | :20–22 |
| L5 | `common/the-abandoned-interior.md` | The MYTH-GUARD: in *standard* Maxwell the scalar/longitudinal modes are GAUGE (not physical in vacuum) — "Heaviside deleted a physical mode" is FALSE for standard EM. AVE's longitudinal mode is a DIFFERENT object: a real acoustic/volumetric-breathing DOF — AVE *ADDS* a medium with a genuine longitudinal DOF. The biquaternion scalar slot IDENTIFIES, does not DERIVE — physics comes from Ax1+Ax4. | :22, myth-guard block |
| L6 | `vol1/…/master-equation.md` | The two "3"s (A1 ⊥ T2): A1 dilatation-MASS "3" = the Heaviside-excised longitudinal compression scalar (mₑc² = trapped acoustic compression energy) ⊥ T2 Cosserat (2,3) WINDING "3" = charge (= Beltrami helicity H_bel = ∫ω·(∇×ω)). "Never wire the winding into the breather's own phasor." Master eq is the Maxwell-Heaviside transverse wave eq + Ax4 saturation. | :20, :24, :36–39 |
| L7 | `common/translation-tables/translation-circuit.md` (Leaf A) | δ↔Γ conjugate; "the evanescent tail leaking out IS the long-range (~ℓ_node/r Coulomb) field, i.e. how a trapped soliton couples to the outside vacuum" | :541 |
| L8 | `vol2/…/substrate-perspective-electron.md` (Leaf B) | "Outside the loop (Regime I, vacuum): ‖ω‖², ‖V_inc‖² decay rapidly (hedgehog tail; exponentially-suppressed in saturation regime)"; the ONLY stated long-range survivor is the 1/r² Op14 GRAVITATIONAL refractive tail, NOT a Coulomb 1/r electric tail | :109, :113 |
| L9 | `vol4/claim-quality.md` clm-4r4jiy (Q-G22) | The strain-convention split: A_geom(r) = ℓ_node/r (∝1/r, the geometric confinement ratio — a POTENTIAL-shaped quantity, used in all kernel applications) vs A_field(r) = E·ℓ_node/V_yield (∝1/r², the Coulomb FIELD ratio). Both internally consistent. The 1/r-vs-α·1/r shape is a flagged open multi-week item (:1311) | clm-4r4jiy, :1311 |
| L10 | `vol2/…/electron-identification.md` | 4-property definition (0₁ unknot real-space; (2,3) phase-space winding; Γ=−1 TIR cavity at V_yield; T₂-only Cosserat core). Charge e = Ax2 winding (axiom-derived); the (2,3) winding RIDES the cage as STATIC charge Link(∂Ω,F)∈ℤ | :24–29, :55, §2 |
| L11 | `research/2026-07-03_compositeness-defense_engine-leg_result.md` + `_gate0_result.md` | The engine-leg host audit: `fdtd_3d` is curl-only (Ampère only), NO charge-source term, NO Gauss sector; a planted Coulomb field is NOT a fixed point (p: −2.000 → −1.957, 10% energy loss). The Gate-0 bounds table + the ILL-DEFINED verdict + the sector-conflation ruling (UNDECIDED-BY-ENGINE) | engine-leg §1–§3; gate0 §4 |
| L12 | `vol1/…/master-equation.md` clm-wcoul2 refs + Gate-0 §3 | The gapped ω channel (Yukawa, ξ≈0.548 cells, clm-wcoul2) — the DIFFERENT sector the EM-readout derivation must keep distinct (sector-ownership) | master-eq :24; gate0 §3 |

### 0.2 Sector map (sector-ownership discipline — the load-bearing checkpoint)

Three distinct sectors carry three distinct objects; do NOT cross-wire (per the two-"3"s orthogonality, L6):

- **A1 (translational u / longitudinal / ε₀ / E-sector)** — the compression/dilatation "breather." Longitudinal, propagates c√2. Owns **mass** (mₑc² = trapped acoustic compression, `master-equation.md:20`). In free vacuum it DISSIPATES (Op3, L3). The **static Coulomb-longitudinal E** — if AVE has one — lives HERE (∇·E ≠ 0 is an A1-sector / longitudinal object, L4).
- **T2 (microrotational ω / transverse / μ₀ / B-sector)** — the photon (free) AND the (2,3) winding = **charge** (bound). Transverse, propagates c. Owns **charge** (𝓠 = Link, = Beltrami helicity) and **spin/moment** (𝓙).
- **The gapped-ω interaction channel** (clm-wcoul2) — the winding→winding force, Yukawa-screened (ξ≈0.548 cells). SEPARATE from the gapless EM channel. The EM-readout derivation must NOT let this Yukawa leak into the EM readout (charter standing context; Gate-0 §5 channel-separation requirement).

**The core substrate tension Stage-0 must confront (surfaced, not resolved — `flag-don't-fix`):** charge lives on **T2** (the winding); a static exterior E-field is an **A1/longitudinal** object (∇·E ≠ 0). These are the two ORTHOGONAL "3"s. So the EM-readout question is literally: *how does a T2-sector winding source an A1-sector static longitudinal field, across the A1 ⊥ T2 grade orthogonality the corpus enforces?* This cross-sector coupling is exactly the "intra-node LC coupling" the charter §3.1 names as "the only axiom-native place a rotational winding can push the translational sector." Whether that coupling delivers a static 1/r field is the derivation.

### 0.3 CP4 — phase-space vs real-space (`phase-space-coordinate-check`)

The (2,3) is the **phase-space** (Clifford-torus, (V_inc, V_ref)) winding label; the real-space body is the 0₁ unknot at loop 2π·ℓ_node ≈ 2.4e-12 m. The exterior field E(r) is a **real-space** quantity (the observable a test charge feels; Fourier-conjugate to momentum transfer q). Match coordinates: the derivation's TARGET is the real-space exterior E(r); the phase-space (2,3) label enters only as the source's topological content (𝓠 = Link, which is coordinate-agnostic as an integer). Do NOT quote a phase-space φ² falloff as if it were the real-space exterior field.

### 0.4 CP10 — boundary-not-bulk

𝓠 is a BOUNDARY integer (no-hair, L2): the interior is invisible; only the boundary observables reach the exterior. The mechanism must read the BOUNDARY (∂Ω), not the interior. Any candidate that sources the exterior field from an interior bulk profile violates no-hair and is suspect (the derivation must show the exterior field depends only on the boundary integer, not on interior plumbing — this is itself a check).

**Walk verdict:** the derivation lives in the **cross-sector T2(winding)→A1(longitudinal-E) coupling**, targeting the **real-space exterior E(r)** of a **boundary-integer** source, keeping the **gapped-ω channel separate**. The load-bearing physics questions (staticness, masslessness, boundary-locality, superposition) are enumerated in §7.

---

## 1. THE QUESTION, STATED PRECISELY

**How does the boundary-charge integer 𝓠 = Link(∂Ω, F) ∈ ℤ source the massless EM channel's static, exact-1/r exterior electric field — derived from Axiom 1's 6-DOF node structure + Axiom 3 (lossless action) + the canonical winding definition, with no Gauss's-law-with-ρ-from-the-winding insertion (§4)?**

Two sub-questions Stage-0 answers analytically (the primary observables, §3):

1. **Does the coupling EXIST at derivation grade?** — Is there an axiom-native mechanism (traceable to Ax1's intra-node translational⊥rotational LC coupling) by which a persistent (2,3) winding produces a *static* exterior field in the translational (A1/longitudinal) sector at all? Or does every candidate mechanism die on a named contradiction (staticness / masslessness / boundary-locality / cross-sector orthogonality)?

2. **IF it exists, what is the exterior falloff EXPONENT?** — Is the exterior potential ∝ 1/r (⇒ field ∝ 1/r², Coulomb, F₁ ≡ 1) or does it carry an ℓ_node-scale departure (⇒ F₁ = 𝓕[departure]) or a gap (⇒ Yukawa e^{−r/ξ}/r, which would contradict atoms-exist)?

**The empirically-required answer (anchor, charter §2, pre-registered asymmetric):** atoms exist ⇒ exact 1/r potential. The question is whether AVE can *derive* it. This anchor does NOT enter the derivation as an input (that would rig it); it enters as the validate-on-known target the derivation is measured against (§8).

---

## 2. THE FOUR CANDIDATE MECHANISM CLASSES (INVESTIGATION lanes — no pre-commitment)

Per Grant's ruling: these are lanes to INVESTIGATE, each either derived-with-ledger OR killed-with-named-contradiction. Not a menu. The derivation works each honestly.

### Lane (a) — DYNAMIC PUMPING
**The picture:** the node LC rotation↔translation coupling, driven by the winding's persistent circulation. The (2,3) winding is a persistent circulation in the ω (T2) sector; via the intra-node LC coupling (rotation drives translation, μ↔ε), it drives the translational (A1) sector, which radiates/pushes an exterior field.
**Predicts:** a field sourced by the circulation. Falloff depends on the driving mechanism.
**What would distinguish it / the crux it must survive:** **STATICNESS.** The LC coupling is OSCILLATORY (∂ₜ). A persistent circulation at frequency ω_C would drive an oscillating, not static, exterior field. The lane survives ONLY if a derived rectification / DC-offset / time-averaging mechanism yields a NON-ZERO static residual. If the time-average of the oscillatory drive is zero (as the Cleave pump computed — clm-clvchn, the pump = null), this lane dies on staticness. **Distinguisher:** does ⟨drive⟩_time ≠ 0 from a derived rectifier, or = 0 (null, like the pump)?

### Lane (b) — STATIC STRAIN / DC-OFFSET
**The picture:** the winding shifts neighboring nodes' LC operating points (a quiescent-point displacement). The persistent winding imposes a static strain on the surrounding lattice — a DC offset in the translational sector that equilibrates outward with some falloff.
**Predicts:** a static displacement field u(r) with a derivable falloff from the equilibration (a Laplace-like / Green's-function decay of a static source in the translational sector).
**What would distinguish it / the crux:** **the FALLOFF EXPONENT + MASSLESSNESS.** Does the static strain equilibrate as a massless (gapless) harmonic field (∇²u = 0 exterior ⇒ 1/r potential) or a gapped one (Yukawa, if the A1 sector has a mass gap ⇒ e^{−r/ξ}/r, which would contradict atoms-exist)? **Distinguisher:** is the exterior equilibration equation Laplace (∇²u = 0, massless, 1/r) or Helmholtz-with-mass (∇²u − m²u = 0, Yukawa)? And does the source enter as the boundary integer (no-hair) or the interior profile?

### Lane (c) — BOUNDARY / TOPOLOGICAL
**The picture:** the linking integer 𝓠 as a BOUNDARY CONDITION on the translational sector's solution space. The exterior is source-free; the integer 𝓠 forces a specific harmonic (a topologically-required monopole term) in the source-free exterior solution, like a residue / flux-quantization condition.
**Predicts:** a source-free exterior (∇²φ = 0) with a monopole harmonic whose coefficient is 𝓠 (Gauss-like counting EMERGENT from topology). Falloff = the lowest harmonic = 1/r potential, IF the sector is massless.
**What would distinguish it / the crux:** **does the boundary integer force a NON-ZERO monopole, and does it do so WITHOUT inserting Gauss's law?** This lane is the most un-riggability-exposed: it must derive the monopole coefficient from Link(∂Ω,F) via the sector's own solution structure (a flux/residue argument), NOT by writing ∮E·dA = 𝓠/ε₀. **Distinguisher:** is there a derived reason the exterior harmonic expansion's monopole term is non-zero and equals 𝓠 (topological forcing), or is the monopole zero (the winding is a higher-multipole / dipole source, no net monopole ⇒ no 1/r)?

### Lane (d) — OTHER, DERIVED
Any mechanism the derivation finds that is not (a)–(c). Held open per Grant's ruling. If a mechanism surfaces that is a hybrid or a distinct fourth route (e.g. a saturation-boundary rectification specific to the Γ=−1 wall; a genesis-frozen DC condensate), it is developed here with the same per-term ledger.

**Cross-lane note (not a pre-commitment):** the candidates are NOT mutually exclusive. The corpus's own leading hypothesis (charter §1.8, the sector-conflation ruling) is that the "~ℓ_node/r Coulomb leak" (Leaf A, L7) is the massless matched EM channel and the "exponential hedgehog" (Leaf B, L8) is the gapped ω sector — which, if the derivation confirms it, would make the EM readout a lane-(b)-or-(c)-massless-A1 object and the hedgehog a separate T2/ω-sector object. The derivation tests this, does not assume it.

---

## 3. THE OBSERVABLE-ROBUSTNESS LADDER (declared BEFORE freezing, per ave-prereg Step 3.7)

Under honest knives observables dissolve downward: **magnitude → ratio → sign/shape → existence**. Declared form-end-primary:

| Rung | Observable | Status |
|---|---|---|
| **PRIMARY (gating)** | (i) whether the winding→exterior-EM coupling EXISTS at derivation grade (a mechanism traceable to Ax1, surviving staticness+masslessness+boundary-locality), AND (ii) the derived exterior falloff EXPONENT (1/r potential vs departure vs gapped) | the derivation's headline |
| Secondary | the F₁(q²) magnitude consequence (the form-factor departure amplitude, if the exponent departs from 1/r) | computed only IF the exponent departs |
| Last | any numerical coefficient (e.g. the 1/r-vs-α·1/r coefficient, the clm-4r4jiy open item) | reported if derivable, NOT gating |

**Pre-declared demotion survivors:** if the magnitude / coefficient proves knob-ridden or un-derivable at Stage-0 grade (as the clm-4r4jiy :1311 open item suggests the 1/r-vs-α·1/r coefficient may be), the SURVIVING claim is the **existence of the coupling + the exponent class** (1/r vs departure vs gapped vs absent), NOT any coefficient. This is pre-registered so the demotion is not discovered mid-derivation and mis-framed.

**Gate-floor consistency (Step 3.7b):** the F₁ magnitude / bounds-table check (§5) is a magnitude gate; it applies ONLY if the primary rung lands MECHANISM-DERIVED + non-1/r. If the primary lands MECHANISM-DERIVED + 1/r, F₁ ≡ 1 is stated and no magnitude gate fires (there is no departure to bound). If the primary lands MECHANISM-AMBIGUOUS or STUCK, no magnitude is derivable and no gate demands one.

---

## 4. THE UN-RIGGABILITY LEDGER (charter §3.1 format — every load-bearing term tagged)

**The trap (charter §3):** adding Gauss's law with ρ defined from the winding INSERTS the answer (Gauss forces 1/r by construction). The circular code-convenience coupling was refused three times this month (Cleave pump, impedance-probe Phase-A, compositeness engine leg). Therefore every load-bearing term in any derivation or update equation carries a per-term ledger row with one of three tags:

- **AXIOM-DERIVED (cite)** — the term traces to Axiom 1's own node structure (the 6-DOF, the intra-node translational⊥rotational LC coupling), or Axiom 3 (the action), or Axiom 4 (saturation), or the canonical winding definition (𝓠 = Link). Cite the leaf:line.
- **ENGINEERING-CHOICE (rationale)** — a modeling choice not forced by the axioms (a boundary shape, a linearization, a coordinate). State the rationale + what it would take to make it axiom-derived.
- **FORBIDDEN-INSERTION (reject)** — a term that references the winding as a charge source by DECLARATION (Gauss with ρ = 𝓠·δ³; ∮E·dA = 𝓠/ε₀ as a constraint; a hand-wired winding→E coupling). REJECTED on sight. Gauss is a DIAGNOSTIC (measure ∇·E of what emerges), NEVER a constraint (charter §3.2).

**Ledger table format (the result doc fills one per candidate mechanism):**

| Term | Role in the derivation | Tag | Cite / rationale / rejection |
|---|---|---|---|
| (e.g.) intra-node LC coupling ∂ₜu ↔ ∇×ω | drives translational from rotational | AXIOM-DERIVED | `axiom-definitions.md:16` (rotation↔B, translation↔E, LC-coupled) |
| (e.g.) ρ = 𝓠·δ³(r) then ∇²φ = −ρ/ε₀ | would source 1/r | FORBIDDEN-INSERTION | inserts the answer; Gauss-with-winding-ρ is the refused coupling (charter §3.1) |

**The completeness gate:** a mechanism counts as MECHANISM-DERIVED only if EVERY load-bearing term is AXIOM-DERIVED or a justified ENGINEERING-CHOICE, and ZERO terms are FORBIDDEN-INSERTION. One FORBIDDEN-INSERTION term ⇒ the mechanism is rigged ⇒ it does NOT count as derived (it is either killed or demoted to MECHANISM-AMBIGUOUS pending a non-inserted replacement).

---

## 5. THE DICTIONARY-TRANSLATED COMPARISON (ave-discrimination-check Step 2.7)

Before any AVE-distinct verdict, translate what standard EM says about the SAME construction at matched observables:

- **Standard EM on "a bounded region with total charge integer n, exterior field":** Gauss's law gives ∮E·dA = n·e/ε₀ ⇒ the monopole term of the exterior field is exactly Coulomb (1/r potential), INDEPENDENT of the interior charge distribution, by the shell theorem / multipole expansion. A finite-size source with net charge n still has a 1/r monopole tail; form-factor structure appears only at q·R ≳ 1 (R = source extent). **So standard EM ALREADY predicts 1/r-from-a-counted-integer** — via Gauss + the multipole monopole term.
- **The discrimination consequence:** if AVE's derivation lands MECHANISM-DERIVED + 1/r with F₁ ≡ 1, that **MATCHES dictionary-translated standard EM** — it is **COULOMB-RECOVERY / CONSISTENCY, NOT an AVE-distinct chord.** Booking "AVE derives 1/r" as a chord would mint a result standard EM already predicts. What IS a genuine AVE result at that outcome: the *internal closure* (Ax2's last leg derived from Ax1+Ax3, F₁≡1 earned not posited) — a FORM-EXISTENCE / consistency win, the framework's deepest internal result (charter §2), but a consistency-class result, not a chord.
- **The one place AVE could be DISTINCT:** if the derivation lands MECHANISM-DERIVED + **non-1/r** (an ℓ_node-scale departure standard EM does NOT predict), THAT is an AVE-distinct prediction — but per the compositeness Gate-0 asymmetric stakes (L11), an O(1) ℓ_node-scale F₁ departure lands ~5 OOM inside the LEP contact bound (B2, EXPOSURE-CONFIRMED), i.e. a falsification-territory result, not a chord. The only chord room is a sub-bound departure.
- **The other place AVE could be DISTINCT (negative):** if the derivation lands SCREENED/ABSENT (the winding sources NO massless 1/r field, or only a gapped Yukawa), that is a framework-level NEGATIVE (charge-as-winding cannot reach the far zone; collides with electrostatics existing) — the highest-stakes negative branch (charter §2). Standard EM has no analog (it has no "charge that fails to source a Coulomb field"); this would be an AVE-distinct failure.

**Pre-registered discrimination verdict shape:** 1/r → CONSISTENCY (internal closure, not chord). non-1/r O(1) → EXPOSURE. SCREENED/ABSENT → framework-negative. This is pre-registered so the result doc cannot retroactively re-label a consistency-class 1/r closure as a chord.

---

## 6. FROZEN BINS

Classification per `consistency-vs-emergence`. Bins do not move post-freeze.

- **[MECHANISM-DERIVED + 1/r]** — a mechanism (one of lanes a–d) is derived with a clean un-riggability ledger (every term AXIOM-DERIVED or justified ENGINEERING-CHOICE, zero FORBIDDEN-INSERTION), the exterior potential is ∝ 1/r (field ∝ 1/r²), massless (no gap), boundary-local (reads 𝓠 not the interior), and delivers Gauss-like counting EMERGENTLY (superposition + ∮E·dA counting total Link, not inserted). ⇒ **the readout leg closes analytically.** Stage-1/Stage-2 become VERIFICATION of an already-derived result. **F₁ ≡ 1 consequence stated** (the compositeness charge-channel DEFENSE completes end-to-end, F₁≡1 EARNED not posited). Class: CONSISTENCY (internal closure; matches dictionary-translated EM per §5) — the framework's deepest internal result, but NOT a chord.

- **[MECHANISM-DERIVED + non-1/r]** — a mechanism is derived (clean ledger) but the exterior falloff is NOT exact 1/r (an ℓ_node-scale departure, or a resolved finite-profile monopole). ⇒ **the pre-registered exposure path:** compute F₁(q²) from the departure profile, check it against the compositeness bounds table (Gate-0 prereg §4, reproduced §5.1 below), and book honestly (per §5, an O(1) departure ⇒ EXPOSURE-CONFIRMED, ~5 OOM inside B2; a sub-bound departure ⇒ survival + a named forward sensitivity). No rescue (Rule 11).

- **[MECHANISM-AMBIGUOUS]** — two or more candidate lanes survive to derivation grade but the analytics cannot decide between them (e.g. lane (b) static-strain and lane (c) topological-boundary both yield a plausible mechanism with different exponents, and the deciding term is not analytically settleable). ⇒ **fork-to-computable:** specify EXACTLY what Stage-1 (the 6-DOF engine) and Stage-2 (the seeded 0₁+(2,3) readout) must measure to decide between the surviving candidates — the precise observable, the coordinate, the tolerance, the discriminating prediction of each surviving lane. Per pre-test-physics-check trigger 9.

- **[STUCK]** — the derivation hits a framing-level fork it cannot settle and that is not a fork-to-computable (a physical-picture ambiguity, a missing-mechanism question that no Stage-1/2 measurement resolves without a prior framing decision). ⇒ **STOP, per Grant's standing instruction.** The final message formulates the stuck-point as a one-paragraph plumber-physical question for Grant: what physical picture is missing, what the fork options are, what each implies. Do NOT guess past it. This is Grant's explicit standing invitation ("come to me if you get stuck," charter §3).

### 5.1 The compositeness bounds table (Gate-0 prereg §4 — for the [MECHANISM-DERIVED + non-1/r] path)

Reproduced frozen (auditor-supplied external physics, marked as scaffolding — NOT corpus content, NOT re-derived):

| # | Bound (observable) | Value / scale | Channel | Notes |
|---|---|---|---|---|
| B1 | g−2 / F₂(0) anomaly | electron a_e matches QED+expt to ~1e-12 (sharpest) | F₂ (moment) | not the EM-readout channel (that's F₂/ω-sector) |
| B2 | LEP contact-interaction Λ | Λ ≳ 10 TeV ⇒ structure ≲ ~1e-19 m ≈ 10⁵×(1/ℓ_node) | F₁ (charge) | **the EM-readout channel bound.** Any O(1) ℓ_node-scale F₁ departure is ~5 OOM inside this |
| B3 | LEP/SLC Bhabha dσ/dΩ | QED agreement sub-% to √s ~200 GeV | F₁ + F₂ | full q²-dependence |
| B4 | Møller (E158) | parity asymmetry matches SM ~% | ee corr. | gapped-ω, future-work |
| B5 | electron "radius" | r_e < ~1e-18–1e-22 m | F₁/F₂ extent | ℓ_node ≈ 3.86e-13 m is ~5–9 OOM larger (naive tension, dissolved by wall-channel Γ_EM=0) |

**Reference scales (corpus-verified, `constants.py`):** ℓ_node = ℏ/(mₑc) ≈ 3.86e-13 m; loop 2π·ℓ_node ≈ 2.4e-12 m; ω_C = c/ℓ_node ≈ 7.76e20 rad/s, ℏω_C = mₑc² = 511 keV.

---

## 7. THE PHYSICS CHECKPOINTS (the derivation must pass all four; charter Stage-0 + dispatch)

Every candidate mechanism is tested against these four. A mechanism that fails any one is either killed or demoted to MECHANISM-AMBIGUOUS/STUCK with the failure named.

1. **STATICNESS.** A static exterior field from a *dynamic* winding needs a derived rectification / DC mechanism or a static source. The LC coupling is oscillatory (∂ₜ). **Checkpoint:** what survives time-averaging? Is ⟨exterior field⟩_time ≠ 0 by a derived mechanism, or does it time-average to zero (the pump-null failure mode, clm-clvchn)?

2. **MASSLESSNESS.** The EM channel is matched/gapless (Γ_EM = 0). The mechanism must NOT smuggle a gap into the readout — else it reproduces the ω-channel Yukawa (e^{−r/ξ}/r, ξ≈0.548 cells, clm-wcoul2) and contradicts atoms-exist (a gapped Coulomb ⇒ no long-range electrostatics ⇒ no atoms). **Checkpoint:** is the exterior equation massless (Laplace ∇²φ=0 exterior ⇒ 1/r) or gapped (Helmholtz-with-mass ⇒ Yukawa)? Which sector's dispersion sets it?

3. **LOCALITY-TO-BOUNDARY.** 𝓠 is a boundary integer (no-hair, L2); the interior is invisible. **Checkpoint:** does the mechanism read the BOUNDARY (∂Ω) or the INTERIOR? A mechanism sourcing the exterior from an interior bulk profile violates no-hair. The exterior field must depend only on the boundary integer 𝓠, not on interior plumbing.

4. **SUPERPOSITION / CHARGE-CONSERVATION.** Two windings' fields must ADD; ∮E·dA must count TOTAL Link. **Checkpoint:** does the derived mechanism deliver Gauss-like counting EMERGENTLY (two 𝓠=1 windings ⇒ exterior monopole 2, ∮E·dA = 2 by superposition of the derived single-winding fields), NOT by insertion (writing ∮E·dA = 𝓠_total/ε₀ is FORBIDDEN)? Charge conservation = Link conservation (Ax2, topological) must reproduce emergently.

---

## 8. VALIDATE-ON-KNOWN ANCHORS (which knowns gate which claims)

Per charter §3.4 (Maxwell-recovery) + dispatch (f). Any derived mechanism must, in the appropriate limit, reproduce known electromagnetism BEFORE any AVE-distinct claim counts:

| Known (the anchor) | What it gates | The limit / test |
|---|---|---|
| **A test charge's field is 1/r² (potential 1/r)** | the [MECHANISM-DERIVED + 1/r] bin | in the linear / far-zone limit, the derived exterior field of a single 𝓠=1 winding must reduce to the point-charge Coulomb field. IF it does not (departs, or is gapped, or absent), the claim is NOT "AVE derives Coulomb" — it is the honest non-1/r / SCREENED / ABSENT branch. |
| **Superposition** (two charges' fields add linearly) | the SUPERPOSITION checkpoint (§7.4) + any F₁ claim | the derived mechanism must be linear in 𝓠 (two windings ⇒ additive fields) in the far zone. A mechanism nonlinear in 𝓠 that only accidentally gives 1/r for one winding fails this gate. |
| **Charge conservation** (∮E·dA counts total enclosed charge, frame-independent) | the Gauss-like-counting-EMERGENT claim | the derived ∮E·dA over an exterior surface must equal 𝓠_total (the sum of enclosed Links) EMERGENTLY, as a measured diagnostic (Gauss as diagnostic, §4), not as an inserted constraint. If ∮E·dA ≠ 𝓠 for the derived field, the mechanism does NOT recover charge conservation ⇒ it is not the EM readout. |
| **Masslessness** (electrostatics is long-range; atoms exist) | the MASSLESSNESS checkpoint (§7.2) | the derived exterior must be gapless (1/r, not e^{−r/ξ}/r). A gapped result is measured against this known and booked as a CONTRADICTION with atoms-exist (SCREENED branch, framework-negative). |

**The gating rule:** no AVE-distinct or closure claim is made until the relevant known-EM anchor is reproduced in the appropriate limit. A mechanism that gives 1/r for one static winding but fails superposition or charge-conservation is NOT the EM readout (it is an accidental single-source coincidence). The anchors are checked in the result doc §validate-on-known before the bin fires.

---

## 9. REPORTING SPEC

Final message reports: the mechanism verdict PER candidate class (a/b/c/d — derived-with-ledger or killed-with-contradiction); the derived exponent (if any); the bin fired; the ledger summary (how many terms AXIOM-DERIVED vs ENGINEERING-CHOICE vs FORBIDDEN-INSERTION-rejected); the PR number. If [STUCK] fires: STOP, and the final message formulates the stuck-point as a one-paragraph plumber-physical question for Grant (what physical picture is missing, the fork options, what each implies) — no guessing past it.

**PR title:** `research(em-readout): Stage-0 analytic derivation — [bin fired]`.

**Corpus updates (surfaced for the auditor to LAND, implementer does NOT land manual entries):** IF [MECHANISM-DERIVED + 1/r], the sector-conflation ruling (charter §1.8) resolves (Leaf A = massless EM = the derived 1/r; Leaf B = gapped ω) and the Ax2 derived-legs table (axiom-register) updates — surfaced, not landed. IF non-1/r or SCREENED, the honest negative is surfaced. IF STUCK/AMBIGUOUS, the Stage-1/2 fork-to-computable spec is surfaced.

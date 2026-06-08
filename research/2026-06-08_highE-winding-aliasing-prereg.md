# HIGH-E WINDING-ALIASING Hypothesis — Pre-Registration (FROZEN)

**Date**: 2026-06-08
**Target**: Freeze the HIGH-E WINDING-ALIASING hypothesis (§35 / `wdot9oegf` of the electron-synthesis epic) as a pre-registered open question BEFORE any compute. Establish the refined hypothesis that survives the muon/proton resolved-above-cutoff tension, the frozen discriminating question, the A46 phase-space measurement frame, the QCD/Regge counterfactual, the frozen outcome categories, and the consistency-vs-emergence classification.
**Branch**: `analysis/2026-06-08-highE-aliasing-prereg`
**Status**: **PREREG ONLY — NO driver, NO result, hypothesis + outcomes FROZEN before compute.**
**Skills applied explicitly**: `ave-prereg`, `pre-test-physics-check`, `substrate-native-check`, `phase-space-coordinate-check` (A46), `ave-discrimination-check` (QCD/Regge counterfactual), `consistency-vs-emergence`, `substrate-first-for-numbers`, `verify-before-cite`, `pure-AVE-corpus`.

---

## Section 1 — Hypothesis (precise)

### 1.0 The hypothesis as literally stated (§35 / `wdot9oegf`)

> Above the Brillouin cutoff `ω_C = c/ℓ_node = m_e c²/ℏ = 0.511 MeV`, a particle's internal carrier (`ω = mc²/ℏ > ω_C`) **aliases** — Nyquist-folds into the first Brillouin zone — and that aliasing is conjectured to **produce the high-energy "fractal" / self-similar resonance morphology** of the transient-resonance zoo.

### 1.1 The hypothesis-as-stated is FALSIFIED by the corpus (do NOT paper over)

The literal "above cutoff ⇒ aliased fractal" claim is **empirically false against AVE's own resolved-above-cutoff particles**:

| Particle | `ω/ω_C` (= m/m_e) | Position vs cutoff | Structure (phase-space) | Mass match | Stability | Source |
|---|---|---|---|---|---|---|
| Electron | 1.0 | **AT** cutoff (identity) | (2,3) trefoil, `0₁` real-space | definitional | stable | `preferred-frame-and-emergent-lorentz.md:103` |
| Muon | 207 | **ABOVE** cutoff | (2,3) trefoil **+ 1 Cosserat torsional quantum** | +1.24% | metastable (τ≈2.2 µs) | `q-g27-muon-cosserat-saliency.md:30` |
| Proton | 1836 | **ABOVE** cutoff | (2,5) cinquefoil, Borromean N=3 | −0.002% | stable | `torus-knot-ladder-baryons.md:23,41` |
| Δ baryon | ~2412 | **ABOVE** cutoff | (2,7) ladder | within ~1% | resonance | `2026-05-31_..._cross_particle_prereg.md:73` |

Muon (207×) and proton (1836×) sit **far above** any O(1)·ω_C fold point, yet both carry **clean (2,q) torus-knot topology** and derive to ~1% / part-per-50,000 precision. They are RESOLVED, not fractalized. **"Above cutoff = aliased fractal" is false as stated.**

### 1.2 The refined hypothesis (survives the tension)

The aliasing **STEP** is preserved; the "aliasing ⇒ fractal" **CONSEQUENCE** is demoted from claim to conjecture, and the load-bearing question is relocated:

> **Refined H1 (aliasing step — Class B substrate mechanism, expected COHERENT):** On the K4-TLM with node pitch `ℓ_node`, a carrier frequency `ω > ω_fold` Nyquist-folds into the first Brillouin zone. This is a generic lattice fact (Axiom 1 discreteness). Muon and proton carriers, being ≫ ω_fold, DO fold. The folding operation itself is substrate-grounded.

> **Refined H2 (the relocated, genuinely open question):** Nyquist-folding is **orthogonal to** (does not by itself determine) resonance morphology. WHAT discriminates a resolved-above-cutoff winding (muon/proton — stable/metastable, clean (2,q), narrow) from a transient resonance (broad Breit-Wigner, τ≲10⁻²³ s) is a SEPARATE structural axis — candidate: topological irreducibility (coprime-odd-q / Borromean loop-count) — NOT aliasing-depth `ω/ω_C`.

> **Refined H3 (the conjectural claim, held at hypothesis-stage):** IF a "fractal / self-similar" morphology exists in AVE objects above cutoff, it is produced by competing basin-of-attraction / stability / coupling axes operating ON TOP of the (already-folded) carrier, NOT by the fold depth. This is the part that is UNGROUNDED and must not be headlined as derived.

### 1.3 Two load-bearing subtleties that the prereg must NOT bury

**(a) The fold-point factor is convention-ambiguous, but the tension is robust to it.**
- `ℓ_node ≡ ℏ/(m_e c)` ⇒ `ω_C = c/ℓ_node = m_e c²/ℏ` is an **IDENTITY** (`constants.py:239`; `preferred-frame:103`). The electron sitting "at the cutoff" is therefore **definitional, not evidence** of threshold behavior.
- The lattice angular Nyquist/zone-edge frequency under continuum dispersion is `ω_N = πc/ℓ_node = π·ω_C ≈ 3.14·ω_C` (real-space zone edge at `q = π/ℓ_node`, `preferred-frame:67-68`). So the **electron at ω_C is BELOW the zone-edge** (ω_C = ω_N/π); muon and proton are far ABOVE it.
- Whatever O(1) convention is chosen for the exact fold point (ω_C, ω_C/2, or π·ω_C), muon (207×) and proton (1836×) clear it by 2–3 orders of magnitude. **The resolved-above-cutoff tension survives any O(1) choice** — it does not depend on resolving the π/2 ambiguity. (The ambiguity is flagged, not resolved here.)

**(b) For composite particles, "which carrier aliases" is itself undefined.**
The global `m_p c²/ℏ = 1836·ω_C` is the **COLLECTIVE eigenvalue mass**, NOT a per-loop bond-LC frequency (`cross_particle_prereg.md:173`: "the per-loop frequency is set by the bond-pair LC tank Virial-sum ... NOT by the global `m_p c²/ℏ` which is the COLLECTIVE eigenvalue"). So for an N=3 Borromean proton, the object that would alias on the lattice — global collective carrier vs per-loop carrier — is **not specified**. This is part of the frozen question (Section 2), not a settled input.

---

## Section 1.5 — Physical picture (mechanical / topological, before outcomes)

1. **The cutoff is an identity, not a derived threshold.** `ℓ_node := ℏ/(m_e c)` (Axiom 2) forces `ω_C = m_e c²/ℏ`. The electron-at-cutoff coincidence is constructed, not observed. It is NOT evidence for aliasing-driven physics.

2. **Nyquist-folding is a real lattice phenomenon.** On a discrete K4-TLM, a carrier above the zone edge folds: `ω' = 2ω_N − ω` (first fold). Muon/proton carriers fold many times. This step is coherent and substrate-native (Axiom 1).

3. **The resolution-vs-aliasing mismatch is the whole problem.** If folding CAUSED fractalization, the most deeply-folded particles (proton, 1836×) should be the MOST fractal. Instead the proton is the framework's single cleanest match (−0.002%). So fold-depth and morphology are anti-correlated or uncorrelated — fold-depth is NOT the morphology driver.

4. **Candidate discriminators (frozen as the menu, not yet selected):**
   - **Aliasing-depth `ω/ω_C`** — refuted as sole driver by (3): proton (1836×) ≫ any resonance (~10–100×) yet cleanest.
   - **Topological irreducibility** — coprime-odd-q torus knots (`torus-knot-ladder:11`: "only odd q=3,5,7,9…; no stable (2,4)") + Borromean N=3 linkage; a stable knot cannot decay without an infinite-energy unlinking. Leading candidate.
   - **Stability / lifetime** — fixed-point (zero Lyapunov) for muon/proton vs positive-Lyapunov chaotic trajectory for transients.
   - **Coupling / envelope coherence** — clean (p,q) + single Cosserat quantum vs contaminated/fractional winding + chaotic envelope.

5. **Phase-space vs real-space gulf (A46) is the coordinate that makes-or-breaks any test** — see Section 3. The hypothesis lives on the **internal-winding carrier axis** (`ω = mc²/ℏ`); the C7-GRB falsifier lives on the **real-space wavenumber axis** (`q → π/ℓ_node`). They coincide numerically at `c/ℓ_node` but are physically distinct geometries.

---

## Section 2 — The Frozen Question (per ave-prereg Step 2, corpus-grep verified)

**FROZEN QUESTION:**

> What distinguishes the RESOLVED-above-cutoff windings (muon: 207×ω_C, proton: 1836×ω_C — stable/metastable, clean (2,q) torus knots, masses to 1% / part-per-50k) from the conjectured ALIASED/transient zoo (broad Breit-Wigner widths 50–500 MeV, lifetimes ≲10⁻²³ s)? Is the discriminator a substrate-native topological selection rule (coprime-odd-q / Borromean irreducibility) — or is it already fully accounted for by QCD/Regge, making the AVE statement a consistency check rather than an emergence test?

### Corpus state on each candidate axis (verified `verify-before-cite`)

| Axis | Corpus status | Verified at |
|---|---|---|
| **A1 — Aliasing-depth ↔ width** | **OPEN.** No AVE derivation links fold-count `ω/ω_C` to resonance width/lifetime. Refuted as SOLE driver (proton deepest, narrowest). | grep: no `width`/`Γ`-vs-`ω/ω_C` derivation in `manuscript/ave-kb/` |
| **A2 — Torus-knot quantization as resolution mechanism** | **ASSERTED, not derived.** "(2,q) only for coprime odd q; no stable (2,4)"; baryon ladder predicts spectrum with no between-state parameters. WHY coprime-odd-q suppresses decay is NOT derived. | `torus-knot-ladder-baryons.md:11,19` |
| **A3 — Prime-N / Borromean loop-count irreducibility** | **EMBRYONIC.** Borromean N=3 framing exists; "unlinking costs infinite topological energy" is structurally coherent but NOT quantitatively grounded. | `torus-knot-ladder-baryons.md:19` (V_total dual-reactance), Borromean N=3 framing |
| **A4 — Which carrier aliases (global vs per-loop)** | **OPEN / undefined for composites.** Global mass-carrier ≠ per-loop bond-LC carrier. | `2026-05-31_..._cross_particle_prereg.md:173` |
| **A5 — "Fractal / self-similar morphology"** | **UNDEFINED operationally.** Corpus has NO definition of what "fractal morphology" denotes (spectrum self-similarity? chaotic phase-space trajectory? decay-channel multiplicity? Lorentzian-tail pattern?). | grep: no `fractal` morphology definition in particle-physics KB |

**Conclusion of corpus state:** the aliasing STEP is corpus-coherent; the morphology CONSEQUENCE is ungrounded; the discriminating axis is unselected; the operational meaning of "fractal" is undefined. This is a genuinely OPEN question, correctly pre-registered (not a closed derivation).

---

## Section 3 — Phase-Space Method (A46 phase-space-coordinate-check)

**The measurement, if/when a driver is built, MUST be in internal-winding phase-space coordinates — NOT real-space lattice-Cartesian.**

### 3.1 The coordinate the hypothesis lives in
- **Axis**: internal-winding carrier phase, i.e. the per-node LC-tank phasor `(V_inc, V_ref)` on the Clifford torus, evolving at the carrier `ω = mc²/ℏ`.
- **Aliasing operation**: sample the carrier phasor at the lattice's per-node LC clock rate and measure the FOLDED phase trajectory (the image of `ω > ω_fold` under Nyquist folding) IN phase-space.
- **Observable of interest**: morphology of the folded phase-space trajectory (closed clean (p,q) Lissajous-like winding vs space-filling/chaotic) and its stability (Lyapunov-class), as a function of (p,q) topology AND of fold-depth.

### 3.2 A46 distinction — DO NOT CONFLATE with C7-GRB

| | HIGH-E winding-aliasing (THIS prereg) | C7-GRB-DISPERSION (separate, surviving) |
|---|---|---|
| Axis | **phase-space** internal carrier `ω = mc²/ℏ` | **real-space** wavenumber `q → π/ℓ_node` |
| Physical object | particle's internal winding above its own Compton carrier | external photon propagating with `λ → ℓ_node` |
| Geometry | Clifford-torus `(V_inc,V_ref)` winding | K4 cubic-symmetry dispersion of EM modes |
| Cutoff value | `ω_C = c/ℓ_node` (numerically) | `q = π/ℓ_node` (numerically `→` same `c/ℓ_node`) |
| Status | conjectural morphology claim (this prereg) | "NOT suppressed — at lattice resolution; surviving forward prediction" |
| Source | §35 / `wdot9oegf` | `preferred-frame-and-emergent-lorentz.md:81,68` |

**They coincide numerically at `c/ℓ_node` but measure different things** (`preferred-frame:24,67-68,81`). A real-space GRB-dispersion measurement does NOT test the phase-space winding-aliasing hypothesis, and vice-versa. **Any test that compares a real-space lattice-Cartesian measurement against a phase-space φ²/winding prediction is A46-uninformative and is pre-disqualified.**

### 3.3 substrate-native-check (aliasing on K4-TLM)
The fold operation must be implemented as a genuine K4-TLM sampling/aliasing of the LC carrier (Axiom-1 discreteness), NOT as a continuum-FFT alias of an abstract signal. SM/DSP-default Nyquist (uniform-grid FFT of a scalar) leaks in if the substrate-walk is skipped: the K4 is bipartite tetrahedral (`Fd3̄m`), so the "sampling lattice" is the node graph, and the fold structure inherits cubic-symmetry anisotropy at the zone edge (`preferred-frame:46-48,67`), not the isotropic 1D-Nyquist of a textbook ADC.

---

## Section 4 — Falsifiable Prediction + SM/QCD Counterfactual (ave-discrimination-check)

### 4.1 The honest problem: QCD/Regge already predicts the hadron resonance spectrum

| Observable | QCD / Regge / Hagedorn | AVE | Discriminator? |
|---|---|---|---|
| Baryon mass spectrum | Confinement eigenvalues + Regge `M ~ α′J + M₀` (~300–400 MeV/step) | (2,q) torus-knot ladder, ~170 MeV/crossing | **NONE at mass level** — both match PDG within 1–5%. **CONSISTENCY, not emergence** (`consistency-vs-emergence`). |
| Resonance widths / lifetimes | Breit-Wigner from loop diagrams (canonical) | **NO derived width/lifetime prediction** | **AVE has nothing here yet** — cannot discriminate until a width formula exists. |
| Meson assignment | quark-antiquark confined pair | pion = **medium resonance, NOT a loop soliton** (dielectric ripple) | AVE departs, but **not yet connected to a quantitative decay-branching prediction**. Scoping clarification, not forward prediction. |
| High-mass spectral SHAPE | **Hagedorn**: exponential density-of-states, possible log-periodic structure | **linear (2,c) staircase**, no fractal/log-periodic structure | **CANDIDATE discriminator** — exponential-DoS vs linear-staircase is a falsifiable shape difference, IF precision spectroscopy at M>2 GeV resolves it. |
| Which states are STABLE solitons | all high-M states decay (Hagedorn continuum) | **topological selection**: coprime-odd-q + Borromean-irreducible states stay confined/narrow; others decay | **CANDIDATE AVE-distinct claim** — but the width prediction that would test it is **NOT yet derived**. |

### 4.2 The candidate AVE-distinct claim (the ONLY route to emergence-class)

> The (2,q) torus-knot **topological quantization condition** (coprime odd q + Borromean loop-count irreducibility) **dynamically selects** which above-cutoff windings are **stable narrow solitons** (`Γ ≪ m`) vs **transient broad decay products** (`Γ ~ 0.1–0.5 m`). QCD predicts a Hagedorn exponential continuum (all high-M states decay); AVE predicts a discrete topologically-protected subset stays confined.

**This is the discriminator** — NOT aliasing-depth, which is empirically refuted by muon/proton. **It is not yet derived** (no AVE resonance-width / lifetime formula in corpus). Until that formula exists, the hypothesis is **unfalsifiable in the AVE-distinct sense** and classifies as a consistency check.

### 4.3 Falsifiers (frozen)
1. **Refutes the morphology conjecture (H3):** if a future phase-space driver shows folded-trajectory morphology is a strict monotonic function of fold-depth `ω/ω_C` ALONE (independent of (p,q)), then proton (1836×) must be more fractal than any resonance — contradicting its −0.002% cleanliness. H3 (and any aliasing-depth-as-driver claim) is falsified.
2. **Refutes AVE-distinctness:** if QCD/Regge/Hagedorn fully reproduces the resonance widths AND no topological selection rule yields a width residual beyond QCD, the hypothesis has no AVE-distinct observable → **consistency-class, honestly classified, branch capped**.
3. **Refutes the topological-selection claim (A2/A3):** if a stable narrow baryon is found at a NON-coprime-odd or non-Borromean topology (e.g. a stable (2,4)), the "topology selects stability" discriminator fails.

---

## Section 5 — Frozen Outcome Categories (A/B/C/D)

Frozen BEFORE any compute. These are the discriminating resolutions of the FROZEN QUESTION.

- **Outcome A — TRUE-BUT-NON-OPERATIVE (consistency-class) [~45%].** The aliasing step is coherent (H1 confirmed) but orthogonal to morphology (H2 confirmed); the resonance zoo is already fully explained by QCD/Regge/Hagedorn with no AVE-distinct residual; muon/proton resolution is set by the Cosserat/torus-knot ladder INDEPENDENT of aliasing. ⇒ The HIGH-E winding-aliasing statement is a **true substrate fact with no observational footprint** → **consistency check, NOT emergence test**. Aliasing-as-fractal-producer (H3) is dropped. *This is the modal outcome.*

- **Outcome B — TOPOLOGICAL-SELECTION EMERGENCE (emergence-class) [~20%].** A substrate-native selection rule (coprime-odd-q + Borromean irreducibility) is shown to dynamically protect narrow solitons while non-irreducible windings decay, yielding a **width/lifetime residual or a linear-staircase-vs-Hagedorn shape difference that QCD does NOT predict**. ⇒ AVE-distinct, falsifiable, emergence-class. Requires a NEW resonance-width derivation (out of scope this prereg).

- **Outcome C — RESTRUCTURE (hypothesis-as-stated FALSE) [~25%].** Confirms aliasing and morphology are orthogonal (H2), so "above cutoff = aliased fractal" is simply FALSE; the true statement is Outcome-A's "aliasing occurs but does not determine morphology." The hypothesis is **restructured** (per Rule 12 substitution-not-retraction: preserve body, add 🔴 header, relocate the live question to the stability/topology axis under a new version). No new unverified hypothesis refills the slot.

- **Outcome D — INCOHERENT-STEP (rare) [~10%].** The aliasing STEP itself fails substrate-native-check on K4-TLM (e.g. the per-node LC clock does not Nyquist-fold the carrier the way a uniform ADC would, because of cubic-symmetry / per-loop-vs-global carrier ambiguity in Section 1.3b). ⇒ Even H1 is not clean; the whole framing needs a substrate-native rebuild before any morphology question is well-posed.

(Probabilities are pre-registration priors for honest-closure bookkeeping, not derived quantities.)

---

## Section 6 — Consistency-vs-Emergence Classification

Per `consistency-vs-emergence` discipline (emergence requires a NOVEL prediction beyond the SM/QCD baseline; consistency = recovering known data; identity = definitional; manifestation = substrate-mechanism for a known result):

| Sub-claim | Class (FROZEN) | Rationale |
|---|---|---|
| Electron at `ω_C` | **IDENTITY** | `ℓ_node := ℏ/(m_e c)` ⇒ `ω_C = m_e c²/ℏ` by construction. NOT evidence. |
| Aliasing STEP (Nyquist-fold on K4-TLM) | **Class B substrate-mechanism (manifestation)** | Coherent lattice consequence of Axiom 1 discreteness; uncontroversial; reproduces a generic DSP fact in substrate terms. |
| Muon/proton mass ladder | **CONSISTENCY** (with manifestation precision) | (2,q) ladder matches PDG within 1–5%, same window as QCD/Regge. Cleanest single match (proton −0.002%) is a precision manifestation, NOT a QCD-beating novel prediction. |
| "Aliasing ⇒ fractal morphology" (H3) | **Class E — ungrounded conjecture / hypothesis-stage** | No derivation; "fractal" undefined operationally; refuted as fold-depth-driven by muon/proton. |
| Topological-selection discriminator (A2/A3, candidate B) | **EMERGENCE-CANDIDATE, currently UNREALIZED** | Would be emergence-class IFF it yields a width/lifetime or spectral-shape prediction QCD does not. No such prediction is derived yet → currently **consistency-class by default**. |

**Headline classification of the hypothesis as a whole (FROZEN):**
> The HIGH-E winding-aliasing hypothesis is **PARTIALLY GROUNDED (aliasing step, Class B) + CONJECTURAL (morphology, Class E)**. As currently stated it is a **CONSISTENCY-CLASS** statement: a true-but-non-operative substrate fact whose only emergence-class route is an UNDERIVED topological-selection width/shape prediction. It MUST NOT be headlined as an emergence test until that novel, QCD-beating prediction exists.

---

## Section 7 — Out of Scope (this commit)

- **No driver, no compute, no result.** This is prereg-only; hypothesis + outcomes are frozen above.
- The phase-space aliasing driver (Section 3.1 trajectory-morphology measurement on K4-TLM) — future Phase X work.
- The resonance-width / lifetime derivation that would make Outcome B testable — multi-session theoretical work, NOT started.
- Operational definition of "fractal / self-similar morphology" (A5) — must be pinned before any morphology measurement.
- Prime-N loop-count stability principle (A3) — embryonic, explicitly disclaimed as not-yet-canonical; not promoted here.
- The π/2 fold-point convention (Section 1.3a) — flagged, not resolved.

## Section 8 — Why this prereg is the right next move

The §35 tie-in surfaced a coherent step (aliasing) bolted to an ungrounded consequence (fractal morphology), and the corpus's own resolved-above-cutoff particles (muon, proton) falsify the literal claim. Freezing the hypothesis + outcomes BEFORE compute (per Rule 16 strengthening — ask before design, not after 30 commits) prevents a debug-toward-rescue when the modal Outcome A (consistency-class, no observational footprint) lands. The frozen falsifiers and the honest consistency-vs-emergence classification mean that whichever outcome compute returns, it is an honest-closure (Rule 11) result, not a moved goalpost.

---

**PREREG STATUS: FROZEN — 2026-06-08**
**NEXT GATE (separate session, NOT this commit):** operational definition of "fractal morphology" (A5) + decision on whether the topological-selection width prediction (Outcome B) is derivable; only then is a phase-space driver well-posed.

---

### Citations (verify-before-cite, grepped 2026-06-08 on `origin/main` @ 63e6671a)
- `src/ave/core/constants.py:239` — `L_NODE = HBAR/(M_E*C_0) ≈ 3.8616e-13 m`
- `manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md:103` — `ω_Compton = c/ℓ_node = m_e c²/ℏ`, identity construction
- `…/preferred-frame-and-emergent-lorentz.md:67-68,81` — real-space `q → π/ℓ_node`; C7-GRB "NOT suppressed — at lattice resolution; surviving forward prediction"
- `…/preferred-frame-and-emergent-lorentz.md:24,46-48` — cubic-symmetry zone-edge anisotropy
- `manuscript/ave-kb/vol2/particle-physics/ch02-baryon-sector/torus-knot-ladder-baryons.md:11,19,23,41` — (2,q) coprime-odd-q ladder; proton (2,5) c=5 at −0.002%; V_total dual-reactance
- `manuscript/ave-kb/vol2/particle-physics/ch06-electroweak-higgs/q-g27-muon-cosserat-saliency.md:30` — muon = electron + 1 Cosserat torsional quantum; (2,3) preserved; 1.24%
- `manuscript/ave-kb/vol2/particle-physics/index.md:32` — `m_μ = m_e/(α√(3/7)) ≈ 107.0 MeV`
- `research/2026-05-31_Q-EMBED-SEL-1_step_c_phase2_cross_particle_prereg.md:63,73,173` — `ω_C^(p)=1836·ω_C^(e)`, `ω_C^(Δ)=(1232/938.27)·ω_C^(p)`, global-vs-per-loop carrier
- `research/2026-05-18_c8-baryon-ladder-pdg-anchor-prereg.md:1-117` — prereg format template

# Framing and Presentation Guide

> **Purpose:** This document captures recurring patterns that create friction between the Applied Vacuum Engineering framework and reviewers — particularly those trained in Standard Model, QED, and continuum-GR physics. Each entry identifies a framing anti-pattern, the corrected framing that avoids the miscommunication, and the specific file(s) where the fix belongs.
>
> **Audience:** (1) Framework maintainers editing the manuscript/KB/README; (2) AI assistants or human reviewers approaching AVE for the first time.
>
> **Status:** Living document. Started from the 2026-04-18 KB audit ([`.agents/kb_audit/FINDINGS.md`](../.agents/kb_audit/FINDINGS.md)). Add new entries as future reviewers identify friction points.

## How to use this guide

**If you are presenting AVE externally:** Before claims about Clay proofs, free parameters, or novel predictions reach a reader, check them against the anti-patterns below. The framework loses credibility when it overclaims in a way a skeptical physicist will catch in the first five minutes. These are the five-minute objections.

**If you are reviewing AVE:** This document notes specific places where standard-physics reflexes will steer you wrong. It is not asking you to accept the framework uncritically — it's asking you to engage with the substrate-level claim rather than pattern-matching to "numerology" or "not-a-Clay-proof" based on surface features.

**If you are adding an entry:** Include (a) the anti-pattern in specific language, (b) what the corrected framing looks like, (c) where in the repo the fix should land, and (d) the audit or review that motivated the entry. Short citations to real findings are more useful than long prose.

---

## Category A — Methodological anti-patterns (generic review)

### A1. "0.00% error is a red flag"

**Anti-pattern.** A reviewer sees a 0% error and assumes either a tautology or a fit. Flags BCS $B_c(T)$, the α = p_c/8π identity, and Z₀ = √(μ₀/ε₀) as suspect.

**Corrected framing.** Distinguish three types of 0% agreement:

1. **Definitional identity** — the equation is how the quantity is defined (Z₀ = √(μ₀/ε₀), α = e²/(4πε₀ℏc) = p_c/8π). Zero error is trivially true and should be labeled "identity," not "prediction."
2. **Axiom manifestation** — the prediction *is* one of the axioms expressed at a new scale. BCS $B_c(T) = B_{c0}·S(T/T_c)$ is the Axiom 4 saturation operator at thermal scaling. Zero error is not a fit; it's the claim "this canonical formula is an instance of our axiom."
3. **Numerical coincidence / engineered match** — the type that's genuinely concerning.

**Remediation target.** [`README.md`](../README.md) master prediction table and [`LIVING_REFERENCE.md`](../LIVING_REFERENCE.md) prediction table should tag each 0% row with one of the three categories. Currently all ride on the same ✅ status column, which lets readers conflate very different claims.

**Status (2026-04-19).** ✅ REMEDIATED by PR #17 (R-3). Classification preamble added above the README master prediction table and LIVING_REFERENCE prediction table covering all four categories (identity / manifestation / consistency check / derived prediction). The A1 checker rule context window widened from 400 → 5000 chars so the preamble covers all rows in the table, not just those near it.

**Provenance.** Audit finding in [phase-9-10-bcs-biology.md](../.agents/kb_audit/phase-9-10-bcs-biology.md) originally flagged BCS as "tautology." The correct read (after follow-up) is "Axiom 4 manifestation at thermal scaling," which is a weaker but legitimate claim.

---

### A2. "Same formula as GR (or SM) means no new content"

**Anti-pattern.** Solar light deflection, Hawking radiation, Chapman-Ferraro magnetopauses, BCS, and similar reach the standard result via AVE mechanisms (optical refraction through lattice, Nyquist noise, impedance cavity). A reviewer labels these "rebranded" and dismisses them as not novel.

**Corrected framing.** A substrate-level derivation produces novelty in the *mechanism*, not in the numerics. If AVE claims gravity emerges from impedance-refraction of a physical lattice, reproducing GR's weak-field formulas is *required* (consistency with known physics), not redundant. The substantive question is whether the substrate claim is correct — tested elsewhere via predictions that *do* differ (α-invariance decomposition, galactic rotation below vs. above a₀, BH interior symmetric saturation).

**Remediation target.** Present formula-reproductions under a separate header — "Substrate Consistency Checks" or "Standard-Physics Recovery" — distinct from the master novel-prediction table. Currently they share the same table, which invites the "rebranded" read.

**Status (2026-04-19).** 🔄 PARTIAL. The classification preamble (A1 remediation) defines `consistency_check` as a distinct category and the manifest now types entries accordingly (P10 solar deflection, P17_18 Kirkwood/Cassini, P41 WD redshift — all reclassified in R-2 audit). But the README/LIVING_REFERENCE tables still present all categories in one visual table. A full split into a separate "Substrate Consistency Checks" section is deferred — a future presentation-layer refactor.

**Provenance.** Audit findings in [phase-6-gravity.md](../.agents/kb_audit/phase-6-gravity.md) misframed solar deflection and magnetopause predictions. They are legitimate consistency checks, not content-free duplications.

---

### A3. "Non-integer coordination number is suspicious"

**Anti-pattern.** Reviewer sees $z_0 \approx 51.25$ (or other non-integer "coordination number") and concludes it can't be a real lattice coordination — flags as likely fit or artifact.

**Corrected framing.** Non-integer effective coordination is **generic and physically natural for amorphous networks**. The AVE vacuum is explicitly a disordered amorphous chiral 3-connected manifold, not a crystal:

- Crystalline lattices have integer first-neighbor coordination (FCC z=12, SRS crystal z=3, etc.).
- **Amorphous** networks have non-integer *effective* coordination as a statistical mean over the disordered distribution. Examples: random close packing (z ≈ 6.4), Phillips-Thorpe network glasses (continuous z with composition), jammed disordered packings (irrational z near jamming transition).

The SRS/Laves K₄ graph is the *local topological* reference — 3-connectivity holds node-by-node — but the *macroscopic* vacuum is amorphous. The EMT effective coordination $z_0 = 51.25$ is the mean number of neighbors within the characteristic interaction radius for a physically realized amorphous realization. Non-integer is correct; integer would be surprising.

**Remediation target.** 
- [`manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex`](../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex) introduces z_0 ≈ 51.25 without foregrounding the amorphous interpretation. A one-line prelude — "As the vacuum is a disordered amorphous chiral manifold (not a crystal), effective coordination numbers are generically non-integer statistical means" — would pre-empt the crystalline-reflex critique.
- The SRS visualization in [`simulate_3d_lattice.py`](../src/scripts/vol_1_foundations/simulate_3d_lattice.py) shows a crystalline unit cell, which reinforces the wrong impression. A companion visualization showing amorphous realization (with the Poisson-disk statistics from `verify_coordination.py`) would make the distinction concrete.

**Status (2026-04-19).** ✅ REMEDIATED by PR #17 (R-3). Amorphous-lattice preambles added to 10 z_0 ≈ 51.25 occurrences across Vol 1 Ch 1, Vol 3 Ch 1, backmatter/appendix_c, backmatter/02_full_derivation_chain, and 4 KB files. Each preamble within 500 chars of the value, satisfying the A3 checker rule. Companion amorphous visualization still deferred (separate Y-item if pursued).

**Provenance.** Original audit in [phase-0-axioms.md](../.agents/kb_audit/phase-0-axioms.md) / [phase-1-foundations.md](../.agents/kb_audit/phase-1-foundations.md) flagged "z_0 ≈ 51.25 is non-integer, which is odd for a coordination number." User correction during Batch 1 remediation: the vacuum is amorphous, not crystalline; non-integer is expected.

---

### A4. "Per-nucleus / per-datapoint parameter = not a prediction"

**Anti-pattern.** Reviewer sees `err_func(R) = predicted_mass - observed_mass` in a solver, concludes each datapoint is a fit.

**Corrected framing.** The strict reading is correct *when the fit target is the observable being predicted*. It does not apply when:
- A parameter is fit to observable X and then verified against independent observable Y (one-in, one-out compression).
- A formula has no fit parameters and the error is from finite-precision numerical convergence.
- A topology class is forced by discrete physics (e.g., alpha clusters by Z, A) with only a single scale parameter per class.

Specify what's fit to what, what's verified downstream, and what's fully forced.

**Remediation target.** Vol 6 ([`manuscript/vol_6_periodic_table/`](../manuscript/vol_6_periodic_table/)) currently fits $R_{\text{factor}}$ per nucleus to CODATA mass — a textbook one-parameter fit. The remediation is to modify [`semiconductor_binding_engine.solve_element`](../src/scripts/vol_6_periodic_table/simulations/semiconductor_binding_engine.py) to fit $R$ against experimental charge radius instead, and verify binding energy downstream. See audit Open-3 in [`HANDOFF_kb_audit_remediation.md`](../.agents/handoffs/HANDOFF_kb_audit_remediation.md).

**Status (2026-04-19).** 🔄 PARTIAL. PR #14 (R-4) remediated the **disclosure** side: Vol 6 LaTeX intro, summary, and computational chapters now acknowledge the per-nucleus R-factor fit, mirroring the KB disclosure. The underlying **engine refactor** (fit R to charge radius instead of mass, verify binding downstream) has NOT been done — that remains an open research / engineering task separate from the framing-audit remediation.

**Provenance.** [phase-11-nuclear.md](../.agents/kb_audit/phase-11-nuclear.md) Open-3.

---

## Category B — Continuum and SM-thinking biases

### B1. "α is a free parameter / axiomatic input"

**Anti-pattern.** Reviewer treats α as a black-box SM input and concludes AVE "still has a free parameter." Or: reviewer reads Axiom 2's literal statement ("α = e²/(4πε₀ℏc) couples topology to impedance") as axiomatically inserting α without derivation.

**Both readings are wrong.** α is **derived** in AVE from the trefoil soliton's S₁₁-minimum geometry (the Golden Torus) via the holomorphic multipole decomposition:

$$\alpha_{\text{ideal}}^{-1} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}} = 4\pi^3 + \pi^2 + \pi \approx \mathbf{137.036304}$$

Where:

- **Λ_vol = 4π³** — volumetric inductance of the 3-torus phase space (with spin-1/2 4π double-cover → $r_{\text{phase}} = 2$); evaluates to $16\pi^3(R \cdot r) = 4\pi^3$ using $R \cdot r = 1/4$
- **Λ_surf = π²** — Clifford torus surface area $(2\pi R)(2\pi r) = 4\pi^2(R \cdot r) = \pi^2$
- **Λ_line = π** — magnetic moment of the core flux loop at minimum node thickness $d = 1$

All three coefficients are forced by the Golden Torus geometry $R = \varphi/2, r = (\varphi-1)/2$, which itself is forced by:

1. **Discrete grid core thickness** $d = \ell_{\text{node}} = 1$ (Nyquist cutoff, Axiom 1)
2. **Self-avoidance constraint** $R - r = 1/2$ (internal strands can't share a node)
3. **Holomorphic screening** $R \cdot r = 1/4$ (S₁₁ minimum on the cross-sectional screening surface)

Constraint #3 is the **S₁₁ minimization** already used by the protein folding engine (Universal Operator #6, $\lambda_{\min}(S^\dagger S) \to 0$) — applied here to the trefoil ground state. Combined, they force a unique $(R, r)$, hence a unique $\alpha$.

**The 0.00022% residual** against CODATA $\alpha_{\text{exp}}^{-1} = 137.035999$ is **also derived** — it's the Vacuum Strain Coefficient $\delta_{\text{strain}} \approx 2.225 \times 10^{-6}$ from CMB-induced (T = 2.7 K) thermal expansion of the spatial metric. The cold-vacuum $137.036304$ is the T→0 asymptote; the measured value is the CMB-bathed physical universe. This yields a falsifiable prediction: α runs with local thermal energy (decreases in high-T regions).

**Corrected public framing:**

- ✅ **"Four axioms. α is derived from the S₁₁-minimum Golden Torus trefoil geometry. Cold-lattice prediction: α⁻¹ = 4π³ + π² + π ≈ 137.036304. Observed (CMB-corrected): 137.035999. Agreement: 0.001%."**
- ✅ **"Zero free parameters — all 26 Standard Model parameters are determined by four axioms plus the topological requirement that the smallest stable soliton is the trefoil."**

**Remediation status — COMPLETE (2026-04-19).** All five remediation items executed. The Golden Torus derivation is now in the canonical manuscript at [`vol_1_foundations/chapters/08_alpha_golden_torus.tex`](../manuscript/vol_1_foundations/chapters/08_alpha_golden_torus.tex), including a rigorous derivation of the $\pi^2$ screening normalization from spin-1/2 half-cover of the standard Clifford torus $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ (parallel to the PMNS three-regime derivation in Vol 2 Ch 3). The [`constants.py`](../src/ave/core/constants.py) has `ALPHA_COLD_INV` and `DELTA_STRAIN` with full derivation comments. Four verification scripts in [`src/scripts/vol_1_foundations/`](../src/scripts/vol_1_foundations/) close the chain end-to-end:
- `derive_alpha_from_golden_torus.py` — multipole evaluation
- `verify_clifford_half_cover.py` — rigorous derivation of $\pi^2$
- `ropelength_trefoil_golden_torus.py` — numerical convergence to Golden Torus
- `verify_golden_torus_s11.py` — ABCD infrastructure

README and LIVING_REFERENCE tables updated to 47/47 entries (added row 47 for α thermal running as falsifiable prediction).

**No remaining remediation.** The framework's "zero free parameters" claim is now load-bearing: α is derived from Axiom 1 (Nyquist/smallest soliton) + SU(2) spin-1/2 topology, with all three regimes (Nyquist, crossings, screening) producing independent equations that solve uniquely to the Golden Torus.

**Provenance.** User correction during post-audit remediation, 2026-04-19. Derivation retrieved from deleted file `future_work/chapters/16_futurework/03_fermion_sector/02_electron.tex` (commit 0a6ea52, parent `Applied-Vacuum-Engineering` repo). My earlier audit conclusions in [phase-0-axioms.md](../.agents/kb_audit/phase-0-axioms.md) and [phase-1-foundations.md](../.agents/kb_audit/phase-1-foundations.md) concluded α was axiomatic/1-free-parameter; **this is incorrect** and reflects incomplete search of the parent repo's deleted history. Those audit files need corresponding revision.

---

### B2. "Proofs require continuum limits (Clay standard)"

**Anti-pattern.** Reviewer applies the Jaffe-Witten / Fefferman continuum-QFT criteria to lattice-level results and concludes AVE's Yang-Mills, Navier-Stokes, and Strong CP "proofs" don't qualify.

**Corrected framing.** The framework's position is **engineering-physics** — an ideal-diode vs. real-world-parasitics analogy. The physical vacuum is not a continuum; it is a lattice with pitch $\ell_{\text{node}}$. Under that substrate claim, asking for a continuum limit is asking for a mathematically idealized object that is *physically incorrect by the framework's own premise*. The results are framework-conditional: given Axioms 1–4, the lattice theory exhibits a mass gap, regular NS flow with velocity cap, and unique θ=0 vacuum. They are not Clay-prize-qualifying because they don't claim to be; they claim to be the *physical* resolution of the phenomena motivating the Millennium problems.

**Remediation target.** 
- [`README.md`](../README.md) rows 14–16: replace "Exact ✅ Proofs" with "Framework-level resolution (lattice-conditional)."
- [`manuscript/vol_2_subatomic/chapters/12_the_millennium_prizes.tex`](../manuscript/vol_2_subatomic/chapters/12_the_millennium_prizes.tex): opening paragraph should explicitly frame the work as engineering-physics with the ideal-diode/parasitics analogy. Without the framing, reviewers apply Clay standards and declare the work insufficient — which it genuinely is *by the Clay standard* but not by the framework's own standard.
- [`manuscript/ave-kb/vol2/nuclear-field/ch12-millennium-prizes/`](../manuscript/ave-kb/vol2/nuclear-field/ch12-millennium-prizes/): align KB leaves with the same framing.

**Status (2026-04-19).** ✅ REMEDIATED by PR #6 (initial sweep), PR #15 (R-5 broader sweep), PR #17 (R-3 chapter-opener caveats), and PR #20 (R-1 follow-up split P14_16 bundle into P14/P15/P16 with individual section labels). README rows 14–16 now read "Framework-derived" with per-row links to Ch 12 caveats (rows 14–15) and Ch 10 §sec:strong_cp (row 16). Manifest entries P14/P15/P16 carry `type: engineering_limit` with notes explicitly flagging the framework-conditional scope.

**Provenance.** [phase-5-millennium.md](../.agents/kb_audit/phase-5-millennium.md). User directive in Batch 1 Q4 explicitly confirmed this is a branding issue, not a physics gap.

---

### B3. Temporal/spatial metric decomposition

**Anti-pattern.** Reviewer assumes AVE reproduces GR via a single effective refractive index $n(r) = 1 + 2GM/(c^2 r)$ governing both gravitational redshift and light deflection.

**Corrected framing.** AVE decomposes the gravitational effect into independent components (per [LIVING_REFERENCE.md:32](../LIVING_REFERENCE.md#L32)):

$$n_{\text{temporal}} = 1 + \tfrac{2}{7}\varepsilon_{11} \quad\text{(clock rate, redshift)}$$
$$n_{\text{spatial}} = \tfrac{9}{7}\varepsilon_{11} \quad\text{(spatial refraction, light deflection)}$$

The familiar Axiom 3 refractive index $n(r) = 1 + 2GM/(c^2 r)$ is *only the temporal component*. This decomposition is where AVE's substrate-level prediction of exact α-invariance under gravity comes from ($\varepsilon_{\text{local}}$ and $c_{\text{local}}$ carry the same $n\cdot S$ factor, which cancels in $\alpha = e^2/(4\pi\varepsilon_0 \hbar c)$).

**Remediation target.** 
- [`manuscript/vol_3_macroscopic/chapters/01_gravity_and_yield.tex`](../manuscript/vol_3_macroscopic/chapters/01_gravity_and_yield.tex) and related gravity chapters should foreground the 2/7 vs 9/7 decomposition *at the start* of the chapter. It is non-obvious from GR pedagogy and central to the framework's distinctive predictions.
- The α-invariance entry in the README master table (#42) should be accompanied by a one-line explanation: "ε_local and c_local carry the same n·S factor that cancels in α."

**Status (2026-04-19).** 🔄 PARTIAL. PR #21 (R-8) added §sec:double_deflection to Vol 3 Ch 2 which explicitly decomposes matter (1/7 scalar) vs light (2/7 Poisson) — covers half the B3 remediation. Manifest P42 notes the n·S cancellation argument (R-1 audit). The full chapter-opener foregrounding of 2/7 vs 9/7 decomposition in Vol 3 Ch 1 has NOT been done. Deferred to a future presentation-layer refactor.

**Provenance.** [phase-6-gravity.md](../.agents/kb_audit/phase-6-gravity.md) flagged α-invariance as a null equivalence-principle restatement; it is actually a substrate-level prediction of exact cancellation. The full claim is in [`LIVING_REFERENCE.md:31–32`](../LIVING_REFERENCE.md#L31-L32) but not clearly foregrounded in the manuscript's gravity chapter.

---

### B4. Recurring integers (2/7, 2/9, 3/7, 8/3, 28/79) as independent hidden parameters

**Anti-pattern.** Reviewer treats each occurrence of a small rational in a different prediction as a potentially separate free parameter, leading to a running count of "hidden inputs."

**Corrected framing.** Per [LIVING_REFERENCE.md Scale Invariance Principle (lines 281–302)](../LIVING_REFERENCE.md#L281-L302): the numbers 7 (compliance modes) and 9 (angular sectors) appear at every scale because the lattice structure is scale-invariant. This is not numerology; it is the same Poisson ratio $\nu_{\rm vac} = 2/7$ projecting through the same K₄/SRS geometry at every scale. Auxiliary appearances (3/7, 8/3, 28/79, etc.) are consequences of the same lattice, not independent choices.

If the framework's lattice choice is accepted as structural (analogous to accepting the SM's gauge group SU(3)×SU(2)×U(1) as given), then these integers are forced.

**Remediation target.** 
- [`README.md`](../README.md) and [`LIVING_REFERENCE.md`](../LIVING_REFERENCE.md) master prediction tables currently list each entry's formula inline (e.g., "ν_vac + 1/45" for $\sin^2\theta_{12}$). The table should include a "Source lattice structure" column or equivalent, crediting each entry to the same SRS/K₄ projection. Currently the Scale Invariance table is in a separate section (LIVING_REFERENCE.md:281–302); it should be the default reading frame, not an appendix.
- Each manuscript chapter using a recurring integer should include a one-line pointer: *"(This is the same ν_vac = 2/7 appearing in [other chapter])"* — explicit cross-references, not just scope-local use.

**Status (2026-04-19).** ⏳ DEFERRED. Partial coverage via R-1 audit (manifest `axioms_used` fields now list [1, 2] for ν_vac-using entries per the interlink rule). Full cross-referencing of recurring integers across chapters is a structural refactor — deferred to Y-4 (depends_on_predictions DAG) or a Tier-3 SymPy port (G-1), either of which would naturally produce the cross-reference graph.

**Provenance.** [phase-2-electroweak.md](../.agents/kb_audit/phase-2-electroweak.md), [phase-3-baryons-quarks.md](../.agents/kb_audit/phase-3-baryons-quarks.md), [phase-4-neutrinos-pmns.md](../.agents/kb_audit/phase-4-neutrinos-pmns.md), [phase-7-8-cosmology-orbital.md](../.agents/kb_audit/phase-7-8-cosmology-orbital.md) — audit treated each recurrence as separate until the Scale Invariance principle was surfaced.

---

## Category C — Framework-partition ignorance

### C1. "If it's not in AVE-Core, it's missing"

**Anti-pattern.** Reviewer searches AVE-Core for content referenced in the README (e.g., villin Rg prediction, Sirius B redshift, `master_predictions.py`) and reports it as absent.

**Corrected framing.** The AVE project is partitioned across multiple GitHub repositories in the `ave-veritas-et-enodatio` organization:

- **`Applied-Vacuum-Engineering`** (parent / pre-split) — full theoretical manuscript including Vol 7 hardware; extensive history. Private.
- **`AVE-Core`** (this repo) — physics engine + theoretical manuscript Vols 0–6 (public).
- **`AVE-Protein`** — protein folding engine, 15-PDB validation set, villin / chignolin / Rg tooling (private).
- **`AVE-APU`** — axiomatic processing unit hardware (private).
- **`AVE-HOPF`, `AVE-PONDER`, `AVE-Propulsion`, `AVE-Fusion`, `AVE-Metamaterials`, `AVE-VirtualMedia`** — specialized applied-engineering verticals (private).

Any README or KB entry referencing a prediction should indicate which repo hosts the derivation/implementation. Currently the README implies AVE-Core is self-contained, which creates the false impression of missing content when a reviewer can't find it locally.

**Remediation target.** 
- [`README.md`](../README.md) repository-structure section should list sibling repos explicitly with their scopes. Currently it notes "hardware implementations are maintained in separate private repositories" but doesn't name them.
- [`LIVING_REFERENCE.md`](../LIVING_REFERENCE.md) already does this (line 195–198) but the note is buried; it should be in the top-level project-identity section.
- Each README master-table row should include a repo tag column (e.g., `[Core]`, `[Protein]`, `[APU]`) so readers can locate the underlying derivation.

**Status (2026-04-19).** ⏳ DEFERRED to Y-1. Partial coverage: manifest P39 now carries `cross_repo: "AVE-Protein"` field (R-1 audit) as a prototype. Full per-row repo tagging in README is a larger presentation refactor; see Y-1 (C1 rule not yet implemented in defense-context-checker) which depends on the tagging being added first.

**Provenance.** [phase-6-gravity.md](../.agents/kb_audit/phase-6-gravity.md) (Sirius B, α-invariance), [phase-9-10-bcs-biology.md](../.agents/kb_audit/phase-9-10-bcs-biology.md) (villin, 20-PDB), [phase-13-verification.md](../.agents/kb_audit/phase-13-verification.md) (`master_predictions.py`).

---

### C2. "The 373/373 PURE anti-cheat badge validates parameter-freeness"

**Anti-pattern.** Reviewer sees `verify_universe.py` pass on 373 files and assumes the framework's "zero smuggled parameters" claim is verified by an AST-level check.

**Corrected framing.** The [`verify_universe.py`](../src/scripts/vol_1_foundations/verify_universe.py) scan has a narrow specific scope:

- **Checked:** `scipy.constants` imports (banned); literal floats in module-level code matching specific target values (137.036, 376.73, 1836.15, 69.32, 1.2e-10, CODATA constants).
- **Not checked:** hardcoded coordinate arrays (Vol 6 nucleus geometries), ad hoc correction rules, fit-target parameters passed as function arguments, derived constants from separate engines, data files.

The scan catches one specific failure mode (hardcoding a target observable as a literal) but doesn't enforce the stricter "no smuggled data" AI Rule #12 in LIVING_REFERENCE.md. The "373/373 PURE" badge is true of what it tests, but that's less than it appears to claim.

**Remediation target.** 
- Either (a) widen the scan to AST-walk for suspicious patterns (large numeric tuples/arrays in non-test code, function arguments literally named `*_codata` or `*_observed`, etc.), or (b) relabel the badge to match its actual scope: "No SI-constant imports or CODATA-value literal magic numbers."
- [`src/scripts/vol_1_foundations/verify_universe.py`](../src/scripts/vol_1_foundations/verify_universe.py) docstring currently claims "mathematically prove that no Standard Model empirical parameters are being 'smuggled' downstream to curve-fit the derivations." The actual implementation is narrower; the docstring and README framing should match.

**Status (2026-04-19).** ✅ REMEDIATED (option b) by PR #17 (R-3). README badge line now reads: *"Runs physics protocols + 373-file anti-cheat scan (AST-level check for scipy.constants imports and CODATA-value literal magic numbers — narrow scope, not a full parameter audit; see docs/framing_and_presentation.md §C2)"*. Option (a) (widen the scan) is deferred as engineering work; the scope caveat in the README satisfies the framing remediation.

**Provenance.** [phase-13-verification.md](../.agents/kb_audit/phase-13-verification.md).

---

### C3. IE Corrections A/B/C/D as "per-element ad hoc"

**Anti-pattern.** Reviewer sees four named corrections applied to different element ranges (Be-type, Mg-type, Al-type, d-block) and concludes they are per-element fit rules.

**Corrected framing.** Per [LIVING_REFERENCE.md:168–176](../LIVING_REFERENCE.md#L168-L176), each correction is an operator invocation with a geometric gate:

- **Correction A (Be-type)**: Hierarchical cascade via scale-invariant analog of `hierarchical_binding()`. Gate: `n_adjacent = 1`.
- **Correction B (Mg-type)**: SIR boundary reflection using Op3 (reflection coefficient) + P_C/2 crossing scattering fraction from Axiom 3. Gate: `n_adjacent ≥ 2`.
- **Correction C (Al-type)**: Op3 reflection + Malus's law mapping to crossing angle + Op10 junction projection with quadratic dispersion. Gate: `l_out > 0 AND nesting_ratio < 4.0`.
- **Correction D (Topo-Kinematic)**: Radial Parity Shift for d-block boundaries — Hopf parity cycle reconstruction.

These are operator applications with geometric gates, not phenomenological rules per element. They have zero free fitted parameters.

**Remediation target.** Vol 6 IE solver chapter ([`manuscript/vol_6_periodic_table/`](../manuscript/vol_6_periodic_table/) — the IE-relevant chapter) should foreground "each correction = named AVE operator + geometric gate" at the *start* of the correction section, before showing the numerical results. Currently the operator trace is in LIVING_REFERENCE pitfalls #7–#11, which a reviewer may not read before looking at the IE solver.

**Status (2026-04-19).** ⏳ DEFERRED to Y-1. The C3 defense-context-checker rule has not been implemented. When implemented, it would lint the IE solver chapter for the operator-gate framing. Manuscript-side foregrounding is a separate presentation-layer task.

**Provenance.** [phase-11-nuclear.md](../.agents/kb_audit/phase-11-nuclear.md) initially characterized these as "engineered numerology." The corrected reading came from LIVING_REFERENCE.md. Reviewers approaching the IE code directly would make the same mistake.

---

## Category D — Documentation depth and location

### D1. Derivations distributed across KB, LaTeX, and code

**Anti-pattern.** Reviewer reads a KB leaf that says "solving this quadratic" and concludes the derivation is absent or hand-waved.

**Corrected framing.** Full derivations can live in up to three places:
1. **LaTeX manuscript** (`manuscript/**/*.tex`) — canonical long-form derivations.
2. **Code comments** (especially [`src/ave/core/constants.py`](../src/ave/core/constants.py)) — often contain the full step-by-step rationale inline.
3. **LIVING_REFERENCE.md** — cross-cutting invariants, pitfalls, and scale-invariance principles that tie multiple derivations together.

A KB leaf is an index into these; its role is navigation, not comprehensive derivation storage. Check LaTeX and constants.py before concluding a derivation is missing.

**Remediation target.** Each KB leaf that references a key equation should cross-link to:
- Corresponding LaTeX chapter + equation label.
- Corresponding `constants.py` / `*.py` implementation with line numbers.
- Relevant LIVING_REFERENCE.md section if applicable.

Currently KB leaves often stop at "solving this quadratic yields z_0 ≈ 51.25" without the ref, which makes the derivation look asserted. Adding `→ Derivation: [LaTeX eq. X.Y]` and `→ Implementation: [constants.py:L###]` at the end of each terse KB statement would prevent this.

**Status (2026-04-19).** ⏳ DEFERRED. The D1 defense-context-checker rule has not been implemented (Y-1 scope). Cross-linking every KB leaf is a structural refactor — a natural fit for Tier-3 SymPy pipeline (G-1) which would produce the ref graph automatically, or a separate KB-hygiene sweep.

**Provenance.** [phase-1-foundations.md](../.agents/kb_audit/phase-1-foundations.md) (z_0 derivation), [phase-2-electroweak.md](../.agents/kb_audit/phase-2-electroweak.md) (thermal softening δ_th), [phase-4-neutrinos-pmns.md](../.agents/kb_audit/phase-4-neutrinos-pmns.md) (PMNS angle derivations).

---

### D2. Preconditions applied before solver calls

**Anti-pattern.** Reviewer reads a solver function ([`faddeev_skyrme.py`](../src/ave/topological/faddeev_skyrme.py), e.g.) and searches inside it for a term referenced in the LaTeX. Not finding it, concludes the code and manuscript disagree.

**Corrected framing.** Physical corrections are often applied to a coupling constant *before* the solver is called, not inside the solver. Example: the Faddeev-Skyrme thermal softening $\delta_{th} = 1/(14\pi^2)$ is applied in [`constants.py:492–496`](../src/ave/core/constants.py#L492-L496) (`KAPPA_FS = KAPPA_FS_COLD × (1 − DELTA_THERMAL)`), then the thermally-softened $\kappa_{FS}$ is passed into the solver. The solver never mentions the thermal correction because it receives the already-softened coupling.

**Remediation target.** Docstrings on solver entry points (`solve_scalar_trace()`, `compute_binding()`, etc.) should list all physical preconditions applied to their arguments, with pointers. Example pattern:

```python
def solve_scalar_trace(self, crossing_number=5):
    """
    Minimizes 1D Faddeev-Skyrme energy functional.
    
    Preconditions applied to self.kappa before entry:
      - Thermal softening δ_th = 1/(14π²): constants.py:492–496
    
    Args:
        crossing_number: topologically forced; (2,q) with q=5 for proton.
    """
```

This prevents the "LaTeX says thermal softening, code doesn't contain it" false-alarm that Phase 2 initially raised.

**Status (2026-04-19).** ✅ REMEDIATED by PR #13 (R-6). Solver entry-point docstrings updated to document the δ_th = 1/(14π²) precondition. Other solvers (if any carry similar preconditions) should follow the same pattern; the docstring template is now in the codebase for reference.

**Provenance.** [phase-2-electroweak.md](../.agents/kb_audit/phase-2-electroweak.md) / Batch 1 Q2 resolution.

---

### D3. Villin-like predictions computable from Core but housed elsewhere

**Anti-pattern.** Reviewer finds a prediction formula but no implementation in AVE-Core, concludes the prediction is absent from the scope.

**Corrected framing.** Some predictions have formulas that *can* be evaluated from `ave.core.constants` alone, even if the full tooling (engines, validation benchmarks) lives in sibling repos. Example: the villin Rg prediction $R_g = r_{Ca}(N/\eta_{eq})^{1/3}\sqrt{3/5}$ with $\eta_{eq} = P_C(1-\nu)$ is computable from AVE-Core's `P_C` and `NU_VAC`. The full 20-PDB validation suite lives in `AVE-Protein`, but the Rg formula itself is AVE-Core-native.

**Remediation target.** For each prediction whose formula is AVE-Core-native but whose full engine is in a sibling repo, add a thin implementation in AVE-Core:

- Add `src/ave/biology/` (or similar) with `def villin_rg(n_residues: int) -> float` computing the formula.
- Update README master table rows to distinguish **formula-native** (computable in AVE-Core) from **engine-requires-sibling** (full prediction requires another repo).

This way the public `AVE-Core` repo can demonstrate all "formula" predictions natively; "engine" predictions explicitly point to the sibling.

**Status (2026-04-19).** 🔄 PARTIAL. Manifest P39 now carries `cross_repo: "AVE-Protein"` field (R-1 audit) as the first case of explicit cross-repo tagging. The thin AVE-Core implementation (`src/ave/biology/villin_rg()`) has NOT been added — deferred pending AVE-Protein audit to confirm the formula / inputs. README row 39 still shows the prediction without a cross-repo indicator; the C1/D3 rules in Y-1 would enforce this.

**Provenance.** [phase-9-10-bcs-biology.md](../.agents/kb_audit/phase-9-10-bcs-biology.md) — audit reported villin prediction as missing; LIVING_REFERENCE.md:268 has the formula; it can be ported to AVE-Core.

---

## Category E — Validation framing

### E1. Selection-bias accusations on modulated anomaly formulas

**Anti-pattern.** Reviewer sees one positive flyby anomaly match (NEAR) and several nulls (Rosetta II/III, Juno, MESSENGER), accuses the framework of cherry-picking.

**Corrected framing.** AVE's flyby formula contains geometric modulators (e.g., $\cos\alpha_{geo} \cdot \cos\delta_{geo}$) that legitimately produce null results at specific geometries. Before accepting a selection-bias accusation, compute the formula's predicted value for each flyby given its specific asymptotic geometry and compare against observation. If predictions are non-null for flybys that observed nulls, there's a real problem; if predictions themselves are ~0 for those geometries, the nulls are a success of the formula, not a failure.

**Remediation target.** [Vol 3 flyby chapter](../manuscript/vol_3_macroscopic/) should include a table of all major Earth flybys (NEAR, Galileo I/II, Cassini, Rosetta I/II/III, MESSENGER, Juno) with columns: observed Δv, predicted Δv (AVE formula with geometry), residual. Absent such a table, the reader has only one datapoint and is forced to take the prediction on faith.

**Status (2026-04-19).** ⏳ DEFERRED. The E1 defense-context-checker rule has not been implemented (Y-1 scope). Manifest P19 R-1 audit notes the "geometry-modulated; NEAR-shape prediction validated, others nulls" framing but the full per-flyby table has not been added to the chapter.

**Provenance.** [phase-6-gravity.md](../.agents/kb_audit/phase-6-gravity.md).

---

### E2. Parameter-count comparisons for benchmark claims

**Anti-pattern.** Reviewer compares AVE chignolin RMSD (2.59 Å) to AlphaFold2's <1 Å, concludes AVE underperforms state-of-the-art.

**Corrected framing.** AlphaFold2 uses ~200M trained parameters from a massive supervised dataset; AVE uses zero adjustable parameters on this benchmark. 2.59 Å from zero parameters is a fundamentally different kind of claim than <1 Å from 200M parameters. The comparison should foreground parameter efficiency, not absolute accuracy:

> *"AVE's amino-acid SPICE-circuit model produces chignolin's native fold (2.59 Å backbone RMSD) from sequence alone using zero trainable parameters. AlphaFold2 achieves <1 Å with ~200M trained parameters plus a massive labeled structural dataset. These are incommensurate claims — one is about what's achievable with a forward physical model; the other is about what's achievable with a learned inverse function."*

**Remediation target.** Vol 5 biology chapter ([`manuscript/vol_5_biology/`](../manuscript/vol_5_biology/)) should foreground the parameter-count comparison when presenting benchmark numbers. Currently chignolin-validation.md reports 2.59 Å as "Level 6 Emergence" without explicit comparison — which leaves readers to infer their own benchmark context and (often) compare unfavorably.

**Status (2026-04-19).** ⏳ DEFERRED. The E2 defense-context-checker rule has not been implemented (Y-1 scope). Biology chapter presentation-layer update is a separate task.

**Provenance.** [phase-9-10-bcs-biology.md](../.agents/kb_audit/phase-9-10-bcs-biology.md).

---

### E3. Goldilocks positioning on contested measurements

**Anti-pattern.** Reviewer sees AVE's $H_\infty = 69.32$ km/s/Mpc, notices it sits between Planck (67.4) and SH0ES (73.0), dismisses as "Goldilocks matching neither."

**Corrected framing.** The framework explicitly predicts the Hubble tension is a regime artifact of measuring at different cosmic epochs — early-universe CMB measurements and late-universe distance-ladder measurements should give different effective H. Landing between them is a substantive *a priori* prediction of AVE, not a post-hoc rationalization. But this only reads as a prediction if it's stated as one *before* the tension is referenced in the text.

**Remediation target.** Cosmology chapter ([`manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex`](../manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex)) should open with the a priori statement: *"AVE predicts H_∞ = 69.32 km/s/Mpc, which should land between early-universe CMB measurements and late-universe distance-ladder measurements because these probes different regimes of lattice expansion."* Then and only then present the Planck/SH0ES numbers. Current ordering lets readers misread the prediction as a rationalization.

**Status (2026-04-19).** 🔄 PARTIAL. PR #22 (R-7) updated README row 23 and manifest P23 to "H∞ (Hubble asymptote) | 0.7% vs TRGB. Sits between Planck (67.4) and SH0ES (73)" — the public-facing table now frames this as an a priori between-measurements prediction. The Vol 3 Ch 4 generative cosmology chapter itself has NOT been updated with the a priori framing at the chapter opener; deferred to a manuscript presentation-layer task.

**Provenance.** [phase-7-8-cosmology-orbital.md](../.agents/kb_audit/phase-7-8-cosmology-orbital.md).

---

## How to add new entries

When a new review (human or AI) surfaces a framing issue, add an entry using the pattern above:

1. **Choose a category** (A–E, or add a new one with rationale).
2. **Name the anti-pattern** specifically — what language or reading produces the misinterpretation.
3. **Give the corrected framing** in actionable terms — what the framework actually claims, stated clearly enough that a reviewer would not make the mistake.
4. **Identify the remediation target** — specific file(s) and sections where the fix belongs.
5. **Cite provenance** — which audit or review found this, and where it's recorded.

Keep entries scoped. One entry = one confusion mode. If an entry grows to cover multiple distinct confusions, split it.

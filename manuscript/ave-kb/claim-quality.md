# AVE Claim Quality

<!-- path-stable: referenced from CLAUDE.md INVARIANT-S7 and from every volN/index.md bootstrap directive -->

> **Canonicality preamble.** Leaves are canonical. Intermediate, index, and entry-point nodes are derived summaries and may suggest implications not supported by the leaves. Each entry below identifies a principle the AVE framework asserts and bounds it precisely: what is claimed, and what is NOT claimed even though a summary or external reading might suggest it.

> **Status:** active. Initially seeded with the four most prominent cross-cutting tripwires; enriched in Dispatch 11 with five more (V_SNAP ≠ V_YIELD, ξ_topo, Hubble derivation, Framework-Derived vs Clay-Rigorous, Derived-as-Given hazard discipline) drawn from tripwires surfaced across two or more per-volume sidecars during Dispatch 9. Future enrichment: any new tripwire appearing in 2+ volume sidecars is migrated up here per the routing rule in `CONVENTIONS.md` (INVARIANT-S7).

## Quality Convention (per-entry assessment format)

> **Status:** new — applied to entries as they are reviewed; back-filled across existing entries during ongoing claim-quality sweeps. The format is described here once; per-entry Quality sections appear in this file and in per-volume `claim-quality.md` files.

Each claim entry carries a `## Quality` section that records the entry's current assessment. Format:

```markdown
## Quality
- confidence: 0.X
- depends-on:
  - <id> — Other Entry Title (solidity 0.X)
  - [...]
- solidity: 0.X (build-status phrase)
- rationale: one-sentence statement of why
- strengthen-by:
  - [specific derivation, proof, simulation run, or experimental validation that would raise confidence or close a dependency]
  - [...]
```

`depends-on` is omitted when there are no entry-level dependencies; in that case `solidity = confidence`.

### Entry identifiers (stable IDs)

Each claim entry carries a stable 6-character lowercase-alphanumeric identifier on the line immediately following the heading, in an HTML comment matching the existing `path-stable` convention pattern:

```markdown
## Some Entry Title
<!-- id: 52de10 -->

(... entry body ...)
```

IDs are randomly generated (`LC_ALL=C tr -dc 'a-z0-9' </dev/urandom | head -c 6`) and never derived from the entry title — this makes them stable across title revisions and prose drift. The $36^6 \approx 2.18$ billion namespace is far more than sufficient for the project's lifetime.

`depends-on` references must lead with the dependency's ID. The ID is the canonical reference; the title is for human readability (and may drift); the solidity is for audit at write-time. To find an entry's canonical home, grep for its ID across the KB. To find all references TO an entry, grep for its ID and inspect the depends-on contexts.

A new entry assigns its ID at creation time and never changes it. If an entry is split, retired, or merged, the git change history records the lineage; new IDs are generated for new sub-entries, never reused.

### Confidence rubric

`confidence` is **local quality only** — how well does this entry do its own work, ignoring whether the claims it depends on are themselves solid? Bands are anchor points; intermediate values are permitted (e.g., 0.65, 0.85).

| Confidence | Meaning |
|------------|---------|
| **1.0** | Identity / definition / by construction (no derivation in scope) |
| **0.9** | Derived end-to-end from axioms; canonical chain present in leaf; matches measurement within stated tolerance |
| **0.7** | Derived with disclosed methodology bound (one fitted scalar, identification step) but core mechanism sound |
| **0.5** | Derived with substantive open dependency (e.g., Gaussian ansatz, identification step not derived from axioms) |
| **0.3** | Asserted with partial justification; key step open |
| **0.1** | Asserted without supporting derivation |
| **0.0** | Refuted |

### Solidity computation

`solidity` is the effective quality for downstream build decisions. It captures the "weakest link in the chain" property — building on a claim is only as safe as its weakest dependency.

**Rule**: `solidity = confidence × min(dependency_solidity_values)`. For an entry with no entry-level dependencies, `solidity = confidence`.

**Framework inputs** ($m_e$, $\hbar$, $c$, $e$, $\mu_0$, $\varepsilon_0$, $T_{CMB}$, plus the four axioms) are treated as `solidity 1.0` — they are the framework's accepted baseline. Open questions about whether any of these can themselves be derived from deeper principles (e.g., $m_e$ closure via Nyquist independence) are tracked in the Zero-Parameter Closure Status entry's strengthen-by list, **not** as recurring dependencies on every entry that uses them. This avoids double-counting.

**Dependencies** are other entries (in this file or in per-volume `claim-quality.md` files) whose claims this entry's claims rely on. List them by name with their current solidity values for audit. When a dependency's solidity changes, downstream entries' solidity values must be recomputed.

**Confidence vs solidity**: confidence is "how well does this entry do its own work?" — local only. Solidity is "how safely can this be built on?" — local quality bounded by the weakest dependency. They coincide for entries with no entry-level dependencies; they diverge when an entry's claims rest on other entries' claims.

### Build-status legend (mapped from solidity)

The build-status phrase is mechanically derivable from the `solidity` value (NOT from confidence). If a reviewer feels the operational status doesn't match the band, that signals either local-confidence miscalibration or a dependency's solidity shift — not that the legend should be overridden.

| Solidity range | Build-status phrasing |
|----------------|-----------------------|
| 0.85 ≤ solidity ≤ 1.00 | `(ok to build on)` |
| 0.65 ≤ solidity < 0.85 | `(ok to build on, see caveats)` |
| 0.45 ≤ solidity < 0.65 | `(use as input only, don't build deeper)` |
| 0.20 ≤ solidity < 0.45 | `(do not build on, rework needed)` |
| 0.00 ≤ solidity < 0.20 | `(refuted, do not use)` |

### Reading the Quality section

The Quality section is the operational decision layer over an entry's existing Specific Claims / Specific Non-Claims and Caveats. The boundary text remains canonical for *what is claimed* and *what is bounded*; the Quality section adds *how confident we are locally*, *how solid the claim is for downstream building given its dependencies*, and *what would close any open gaps*.

Consumers (humans, agents, kb-docent) building on a claim should read the Quality section's build-status phrase first. The `solidity` value calibrates that decision; `confidence` plus the dependency chain reveal where any weakness comes from; the `strengthen-by` list specifies the work that would raise solidity (either by raising local confidence or by strengthening a dependency).

A high-confidence entry with low solidity tells you the entry's own work is sound but its dependency chain is the weakness — the highest-leverage work is closing the weakest dependency, not improving this entry. A low-confidence entry tells you the entry's own work is the weakness, regardless of its dependency status.

`strengthen-by` items are the same kind of work-item that `common/mathematical-closure.md` "Outstanding Rigour Gaps" enumerates; over time, that document can become a derived index over all open `strengthen-by` items across boundary entries rather than a parallel register.

---

## Reading Conventions for the Master Prediction Table (Project-Wide Meta-Tripwire)

The Master Prediction Table in `LIVING_REFERENCE.md` (47 entries) and the Key Results tables in volume indexes mix **four kinds of claim** under uniform "Δ%" and ✅ formatting. The classification matters for what each entry actually asserts.

- _Specific Claims_
  - **(i) Identities** — entries where 0.00% or "Exact" is definitionally true. Example: $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ is how $Z_0$ is defined; the 0.00% is not a derivation result.
  - **(ii) Axiom manifestations** — entries where the prediction IS one of the four axioms expressed at a new scale. Example: BCS $B_c(T) = B_{c,0} \cdot S(T/T_c)$ IS Axiom 4 applied at thermal scaling. The 0.00% match is the same operator, not a fit.
  - **(iii) Consistency checks** — entries where the framework reproduces a standard result via an alternative mechanism. Example: solar deflection reproducing the GR value via metric-refraction.
  - **(iv) Derived predictions** — entries where the framework outputs a novel numerical value not taken as input. Example: W/Z masses, neutrino mass, $\sin^2\theta_W = 2/9$, $H_\infty$.
  - The classification of any specific row lives with the leaf; the table summary does not surface it.
- _Specific Non-Claims and Caveats_
  - A global "AVE achieves N predictions at low Δ%" claim is meaningless without the per-row classification. (i) and (ii) and (iii) and (iv) cohabiting under the same Δ% column **collapses meaningful distinctions**.
  - "0.00%" or "Exact" entries do NOT all mean the same thing. An identity (i) is definitionally exact; an axiom-manifestation (ii) is the same operator at a new scale, not a fit; a consistency check (iii) reproduces a standard value via a different mechanism; a derived prediction (iv) at "0.00%" would be a substantive zero-parameter match.
  - Reviewers and summarizers must consult the per-row classification before treating any prediction-table cell as evidence of a specific claim type.
  - This meta-tripwire is documented in the LIVING_REFERENCE.md Master Prediction Table classification note ("Classification note") and in `docs/framing_and_presentation.md` §A1, §A2.

> **Leaf references:** see `LIVING_REFERENCE.md` Master Prediction Table classification note; per-row classification lives in the leaf for each entry.

---

## Symmetric vs Asymmetric Saturation

The Universal Saturation Kernel $S(A) = \sqrt{1 - (A/A_{yield})^2}$ (Axiom 4) is applied in two distinct symmetry cases. Confusing them is the most common source of error in summary-derived claims about AVE.

- _Specific Claims_
  - In **SYMMETRIC** saturation (gravity, BH interior, particle confinement): both $\mu$ and $\varepsilon$ scale by $S$. Result: $Z_{sym} = Z_0$ (impedance invariant); $c_{EM,sym} = c_0/S \to \infty$ (EM phase velocity rises); $c_{shear} = c_0\sqrt{S} \to 0$ (GW/soliton group velocity freezes → rest mass).
  - In **ASYMMETRIC** saturation (strong EM field only): only $\varepsilon$ scales by $S$. Result: $Z_{asym} = Z_0/\sqrt{S} \to \infty$ (medium opaque); $c_{EM,asym} = c_0/\sqrt{S} \to \infty$ (EM evanescent, no energy transport); $c_{shear} = c_0\sqrt{S} \to 0$ (same shear freeze in both cases).
  - $c_{shear} = c_0\sqrt{S}$ is symmetric across both cases — this is the "wave packet freezes (mass)" quantity.
  - Which symmetry applies is determined by what is saturating: gravity (mass-energy) saturates both $\mu$ and $\varepsilon$; strong EM saturates only $\varepsilon$.
- _Specific Non-Claims and Caveats_
  - Does NOT claim that EM phase velocity goes to ZERO at saturation. In both symmetry cases EM phase velocity goes to **infinity**.
  - Does NOT claim that the impedance always goes to infinity at saturation. In **symmetric** saturation, $Z = Z_0$ is **invariant** — the medium is a perfect absorber, not opaque.
  - Does NOT claim symmetric vs asymmetric is a free-parameter distinction. The symmetry case is determined by physics, not chosen.
  - LIVING_REFERENCE.md Pitfall #5: any framework summary suggesting "AVE predicts $\Delta\alpha/\alpha \neq 0$ from gravity" reads symmetric-cancellation steps as predictions; the actual derivation result under symmetric gravity is **invariance**.

> **Leaf references:** Axiom 4 statement leaves in `vol1/`; symmetric-case mapping in `vol3/gravity/` (BH interior, GW propagation); asymmetric-case mapping in `vol4/circuit-theory/` (nonlinear constitutive); particle-confinement in `vol2/particle-physics/`.

---

## α Invariance Under Symmetric Gravity

Axiom 3 sets $G = \hbar c / (7\xi \cdot m_e^2)$. Under Symmetric Gravity, $\varepsilon_{local}$ and $c_{local}$ both carry the same $n \cdot S$ factor.

- $\alpha = e^2/(4\pi \varepsilon_0 \hbar c)$
- _Specific Claims_
  - Under Symmetric Gravity, $\alpha$ is **exactly invariant**: $\varepsilon$ and $c$ carry compensating $n \cdot S$ factors that cancel in the $\alpha$ expression.
  - Multi-species $\Delta\alpha/\alpha = 0$ across gravitational potentials.
  - Lattice decomposition: $n_{temporal} = 1 + (2/7)\varepsilon_{11}$ governs clock rate / redshift; $n_{spatial} = (9/7)\varepsilon_{11}$ governs light deflection. Axiom 3's $n(r) = 1 + 2GM/(c^2 r)$ is the temporal component only.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the framework predicts $\Delta\alpha \neq 0$ in any gravitational regime.
  - Does NOT claim $\alpha$ invariance under arbitrary saturation — invariance is specifically under **symmetric** saturation. Asymmetric saturation breaks the $n \cdot S$ cancellation.
  - The $\alpha$ thermal-running prediction ($\delta_{strain} \approx 2.2 \times 10^{-6}$ at $T = 2.7$ K, master prediction #47) is a **separate** effect — CMB-induced spatial metric expansion, not a gravitational effect. Any summary conflating gravitational $\Delta\alpha$ with thermal $\Delta\alpha$ is wrong.
  - LIVING_REFERENCE.md Pitfall #5 explicitly: any framework summary suggesting "AVE predicts multi-species $\Delta\alpha/\alpha$ from gravity" is **wrong**.

> **References:** Canonical leaf for the bound: [`vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md`](vol3/gravity/ch01-gravity-yield/alpha-invariance-symmetric-gravity.md) (Derived Consequence 1 of Axiom 3, verbatim from `manuscript/common_equations/eq_axiom_3.tex`). Companion leaf for the temporal/spatial decomposition: [`vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md`](vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md) (Derived Consequence 2). Cross-volume invariant restatement: `LIVING_REFERENCE.md` Axiom 3 entry ("α invariance" and "Lattice decomposition" sub-bullets); LIVING_REFERENCE.md Pitfall #5 for the contamination warning. Note: [`CLAUDE.md`](./CLAUDE.md) INVARIANT-S2 lists the four AVE axioms in their bare form; the derived-consequence sub-bullets under Axiom 3 are in LIVING_REFERENCE.md, not in CLAUDE.md. The α thermal-running effect derivation is in [`vol1/ch8-alpha-golden-torus.md`](vol1/ch8-alpha-golden-torus.md).

---

## BCS Critical Field $B_c(T)$ — Axiom Manifestation, Not Curve Fit

Master Prediction Table entry #43: BCS $B_c(T)$ at 0.00% match, marked ✅. The "0.00%" reads like a numerical fit but is not — it indicates that the BCS empirical curve **is** the AVE saturation operator at thermal scaling.

- $B_c(T) = B_{c,0} \cdot S(T/T_c)$ where $S$ is the Universal Saturation Kernel $\sqrt{1 - (A/A_c)^2}$ (Axiom 4)
- _Specific Claims_
  - The BCS critical-field temperature dependence $B_c(T)$ **is** the Universal Saturation Kernel applied to thermal scaling. The 0.00% match is not a numerical fit — it is the same operator at a different scale.
  - The match holds for Al, Pb, Nb, MgB$_2$.
  - Per the Master Prediction Table classification: this is an **"axiom manifestation"** (category ii), not a "derived prediction" (category iv).
- _Specific Non-Claims and Caveats_
  - The 0.00% in the prediction table does NOT mean a curve fit was performed.
  - Does NOT claim $B_{c,0}$ (the material-specific zero-temperature critical field) is derived from AVE. $B_{c,0}$ is taken as input per material.
  - Does NOT claim any of the four BCS materials' $B_{c,0}$ values are AVE-derived. Only the temperature dependence is the axiom manifestation.
  - This is one specific instance of the project-wide meta-tripwire ("Reading Conventions for the Master Prediction Table" above): "0.00%" or "Exact" entries elsewhere may belong to different classification categories. Each row's classification matters; a global "AVE achieves 0.00% on N predictions" claim collapses meaningful distinctions.

> **Leaf references:** Axiom 4 statement leaves in `vol1/`; BCS mapping leaves in `vol3/condensed-matter/`.

---

## V_SNAP ≠ V_YIELD

LIVING_REFERENCE.md "Critical Distinctions" #1. Surfaces in vol1 and vol4 sidecars; relevant wherever lab-scale dielectric breakdown is being discussed.

- $V_{snap} = m_e c^2 / e \approx 511$ kV (absolute dielectric destruction)
- $V_{yield} = \sqrt{\alpha} \cdot V_{snap} = \sqrt{\alpha} \cdot m_e c^2/e \approx 43.65$ kV (kinetic onset of measurable nonlinearity)
- _Specific Claims_
  - $V_{snap}$ marks absolute breakdown — the voltage at which the lattice topology ruptures.
  - $V_{yield}$ marks the onset of measurable nonlinear response in laboratory-scale fields. Lab experiments operate near $V_{yield}$, not $V_{snap}$.
  - The relation $V_{yield} = \sqrt{\alpha} \cdot V_{snap}$ comes from Axiom 2 (fine-structure constant sets the saturation threshold).
- _Specific Non-Claims and Caveats_
  - Does NOT claim laboratory experiments at "kV-scale fields" automatically encounter Axiom-4 saturation. Sub-$V_{yield}$ operation is in Regime I (linear Maxwell recovered).
  - Does NOT claim $V_{snap}$ has been experimentally observed; 511 kV remains beyond standard lab capability.
  - LIVING_REFERENCE.md Critical Distinction #1 explicitly: confusing $V_{snap}$ and $V_{yield}$ leads to mis-classifying lab regimes (e.g., a 30 kV experiment is in Regime II below $V_{yield}$, not approaching $V_{snap}$).

> **References:** Vol 4 leaves ($V_{snap}$ definition, lab regime classification); Vol 1 leaves ($V_{yield}$ derivation from Axiom 2); LIVING_REFERENCE.md "Critical Distinctions" #1.

---

## Topological Conversion Constant ξ_topo (Not a Free Parameter)

CLAUDE.md INVARIANT-C2: $\xi_{topo} \equiv e/\ell_{node}$ (units: C/m). The bridge between AVE lattice parameters and mechanical/biological/circuit quantities. Surfaces in vol2 (atomic orbitals), vol4 (VCA derivations), vol5 (mass-to-inductance, bond stiffness-to-capacitance), vol6 (heavy-element coupling).

- $\xi_{topo} = e / \ell_{node}$ where $\ell_{node} = \hbar/(m_e c)$ (reduced Compton wavelength)
- _Specific Claims_
  - $\xi_{topo}$ is an **algebraic identity** built from four CODATA constants ($e$, $\hbar$, $m_e$, $c$): $\xi_{topo} = e/\ell_{node} = e\, m_e\, c/\hbar$. Once those CODATA inputs are fixed, $\xi_{topo}$ is determined; no fitting is involved.
  - Used as a **dimensional conversion constant** that maps electrical quantities to mechanical/topological ones (and vice versa) consistently across all volumes that invoke it.
  - Volume-specific manifestations: see vol4 (`circuit-theory/topological-conversion-constant.md`), vol5 (`organic-circuitry/electromechanical-transduction-constant.md` — canonical definition leaf per INVARIANT-C2), vol6 (heavy-element coupling), vol2 (atomic-orbital mapping).
- _Specific Non-Claims and Caveats_
  - Does NOT claim $\xi_{topo}$ is a free parameter that can be tuned; it is a derived constant.
  - Does NOT claim $\xi_{topo}$ alone derives the engineering predictions in vol4 — those derivations also require regime classification, geometry, and the constitutive relations.
  - Do NOT confuse $\xi_{topo}$ (electromechanical transduction, C/m) with $\xi$ (Machian hierarchy coupling, dimensionless ≈ 8.15×10⁴³ from Axiom 3). Distinct quantities sharing a Greek letter; CLAUDE.md and LIVING_REFERENCE.md Axiom 3 entry both call this out.

> **References:** CLAUDE.md INVARIANT-C2; canonical definition leaf in `vol5/molecular-foundations/organic-circuitry/electromechanical-transduction-constant.md`; vol4/vol6 manifestations cited in their respective sidecars.

---

## Hubble Constant Derivation — Consistency Proof, Not Independent Prediction

$H_\infty \approx 69.32$ km/s/Mpc (Master Prediction Table #23). Surfaces as a "Key Result" in vol1, vol2, and vol3 indexes.

- $H_{\infty} = 28\pi m_{e}^{3} c G / (\hbar^{2} \alpha^{2})$
- _Specific Claims_
  - The relation between $G$ and $H_\infty$ is a **geometric self-consistency relation**, because the Machian coupling $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ embeds $R_H \equiv c/H_\infty$ in the definition of $G$. Substituting CODATA $G$ recovers $H_\infty$ numerically; rearranging is structurally an identity.
  - Numerical value $\sim 69.32$ km/s/Mpc lies between Planck (67.4) and SH0ES (73.0), within $\sim 1\sigma$ of TRGB (69.8).
  - The framework's Hubble Tension claim is that both Planck and SH0ES measurements are compatible with the same geometric constraint at different thermodynamic regimes — NOT that AVE outputs $H_0$ ab initio.
- _Specific Non-Claims and Caveats_
  - Does NOT claim a parameter-free derivation of $H_0$ from axioms 1–4 alone. The lattice-genesis leaf (`vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md`) explicitly flags this as a self-consistency check; "Outstanding Rigour Gaps" in `common/mathematical-closure.md` lists promotion to a true downstream prediction as an open problem (deriving $G$ from a local thermodynamic balance independent of $R_H$).
  - Does NOT claim AVE resolves the Hubble Tension by selecting one measurement over the other.
  - The volume index Key Results entries that show "$H_\infty \approx 69.32$ km/s/Mpc" without qualifier are summary-conflation pattern — followups logged for index refresh.

> **References:** Master Prediction Table #23; canonical leaf `vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md`. Vol1 sidecar carries an "Asymptotic Hubble Constant $H_\infty$ and MOND $a_0$" entry; vol3 sidecar carries the full "Asymptotic Hubble Constant $H_\infty$" entry. Vol2 sidecar does not currently carry a Hubble entry — vol2 leaves do touch $H_\infty$ in cosmology framing, so a vol2 entry that cross-references back here would be appropriate (logged as followup, not blocking).

---

## Framework-Derived vs Clay-Rigorous (Yang-Mills, Navier-Stokes, Strong CP)

Master Prediction Table entries #14 (Yang-Mills mass gap), #15 (Navier-Stokes smoothness), #16 (Strong CP) are marked ✅ but with explicit "framework-derived (lattice-conditional; not Clay-rigorous)" caveats. Surfaces in vol2 (Yang-Mills, NS, Strong CP) and vol3 (Kolmogorov spectral cutoff cites NS).

- _Specific Claims_
  - Within the AVE discrete-lattice framework, the three Millennium-class results follow from explicit constructions: lattice cutoff and Picard-Lindelöf for NS; vacuum topology for Strong CP; lattice + boundary conditions for Yang-Mills mass gap.
  - The lattice cutoff $k_{\max} = \pi/\ell_{node}$ provides a constructive enstrophy bound for NS; the saturation envelope rolls the inertial spectrum smoothly to zero. Within this framework, global regularity is structural.
  - Yang-Mills mass gap is positive within the framework's lattice-conditional construction.
  - Strong CP $\theta = 0$ is exact within the framework's unique-vacuum-topology construction.
- _Specific Non-Claims and Caveats_
  - Does NOT claim Clay-Prize-rigorous proofs in any of the three cases. The proofs are framework-derived (lattice-conditional and reliant on AVE's specific operator structure), not continuum-rigorous in the formal-mathematics sense the Clay Mathematics Institute requires.
  - Does NOT claim equivalence between AVE's lattice-conditional construction and a continuum proof; promotion to continuum-rigorous standing is an open problem.
  - LIVING_REFERENCE.md Master Prediction Table entries #14, #15, #16 carry the same caveat language; vol2 sidecar covers Yang-Mills/NS/Strong CP individually with these caveats; vol3 sidecar's Kolmogorov entry references it.

> **References:** Master Prediction Table #14, #15, #16; KB leaves under `vol2/nuclear-field/ch12-millennium-prizes/` (e.g., `yang-mills-steps1-2.md`, `yang-mills-steps3-5.md`, `navier-stokes-prize.md`, `index.md`); vol2 sidecar entries for Yang-Mills, Navier-Stokes, Strong CP carry the volume-scoped versions of these caveats; vol3 sidecar's Kolmogorov entry references the NS lattice-conditional construction. Underlying source material: `manuscript/common_equations/the_millennium_prizes.tex` and `10_open_problems.tex` (LaTeX origin, not a KB leaf — content is distilled into the listed KB leaves).

---

## Derived-as-Given Hazard Discipline (QM Vocabulary, Bohr Formula, σ-Arithmetic)

LIVING_REFERENCE.md Pitfalls #8–#11 catalogue project-wide contamination patterns where reasoners (or summaries) introduce derived quantities as if they were given. Surfaces in vol2 (atomic IE, methodological contamination) and vol6 (Bohr radius, IE correction stack).

- _Specific Claims_
  - The framework derives quantities that **correspond to** standard physics constants and concepts (GR, QM, standard model). It does **not** take them as inputs.
  - Atomic ionization energy is solved by the AVE radial eigenvalue solver (`radial_eigenvalue.py`) — ODE cavity eigenvalue + Hopf mode split + corrections A/B/C/D — NOT by the Bohr formula $E = Z_{eff}^2 Ry/n^2$.
  - Pairwise interactions are computed from Op4 ($U = -K/r \times (T^2 - \Gamma^2)$), NOT from ad-hoc energy formulas.
  - The lattice defect dispersion is named "$n_{dB}(r)$" (de Broglie refractive index), distinct from the medium impedance $Z_0 = 377\,\Omega$.
- _Specific Non-Claims and Caveats_
  - Does NOT claim the framework reproduces QM by importing Schrödinger / Bohr / Hartree-Fock. Where QM-corresponding results appear, they are derived from AVE operators; importing the QM derivation IS the failure mode being warned against.
  - Does NOT claim "any framework summary using QM vocabulary is wrong" — vocabulary used in the *source's* framing is fine. The hazard is summaries that introduce QM vocabulary the source does not use, which makes the framework appear to assume what it derives.
  - Pitfall #8: $E = Z_{eff}^2 Ry/n^2$ is the Bohr formula, not AVE — using it is contamination.
  - Pitfall #9: $V_{ee} = J \times Z \times Ry$ is ad-hoc — must come from Op4.
  - Pitfall #10: De Broglie defect dispersion is NOT the lattice impedance.
  - Pitfall #11: A Pauli-saturated inner shell creates a discrete impedance step the smooth CDF misses; SIR correction required for shells with p-subshells.

> **References:** LIVING_REFERENCE.md Pitfalls #8, #9, #10, #11; LIVING_REFERENCE.md §"Red flags for QM contamination"; vol2 sidecar (atomic IE solver entry); vol6 sidecar (Bohr radius entry, IE correction stack).

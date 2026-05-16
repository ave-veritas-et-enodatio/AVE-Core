[↑ Common Resources](index.md)
<!-- leaf: verbatim -->

# AVE Axiom Homologation — Cross-Repo Inventory

> **Cross-cutting framework reference per [INVARIANT-S3 / cross-cutting-notes pattern](../CLAUDE.md).** Documents distinct axiom-numbering schemes used across the AVE org (Schemes A / B / C / vestige), their reconciliation, and the load-bearing canonical naming (Scheme A per Vol 1 Ch 1:51-75). **Living record** — future audits surfacing new scheme variants, additional inconsistencies, or downstream homologation work should land as amendments here, not as parallel docs. Last revised: 2026-04-27 (homologation P1-P5 + doc 75_ framing-error pass + promotion from `.agents/handoffs/` to `manuscript/ave-kb/common/`).

**Status:** auditor-drafted handoff, 2026-04-27, per Grant directive: *"fully document in a new artifact, all of the places you've seen the axioms and the different schemes they have... be incredibly pedantic, search the full github org/all repos."*

**Scope:** all 9 AVE-* repositories under `/Users/grantlindblom/AVE-staging/`:
- AVE-Core, AVE-APU, AVE-Fusion, AVE-HOPF, AVE-Metamaterials, AVE-PONDER, AVE-Propulsion, AVE-Protein, AVE-VirtualMedia

**Goal:** catalog every place the four AVE axioms are LISTED, NAMED, or FORMALLY DEFINED across the org, classify each occurrence by scheme, and surface inconsistencies that need adjudication.

**Method:** parallel grep + read across all 9 repos via specialized Explore agents; ~280+ axiom-listing occurrences identified (excluding bare numerical citations). Each occurrence captured with file path, line number, exact quoted text, and scheme classification.

---

## §1 EXECUTIVE SUMMARY

The corpus has **at least four distinct axiom-numbering / labeling schemes** in active use across the org. They are NOT formally reconciled. Two of them disagree at the substance level (Scheme A vs Scheme B differ on what Axiom 3 IS — action principle vs gravity).

### Schemes identified

| Scheme | Ax 1 | Ax 2 | Ax 3 | Ax 4 | Provenance |
|---|---|---|---|---|---|
| **A — Canonical Theory** | LC Network / Substrate | Topo-Kinematic Isomorphism ([Q]≡[L]) | **Effective Action / Least Reflected Action** | Dielectric Saturation S(r)=√(1-r²) | Vol 1 Ch 1, backmatter, 00_scoping.md |
| **B — CommonEqs Engineering** | Impedance | Fine Structure | **Gravity** (G = ℏc/(7ξm_e²)) | Universal Saturation Kernel | `manuscript/common_equations/eq_axiom_*.tex` only |
| **C — KB INVARIANT-S2 (APU-flavored)** | ABCD cascade / coupled amplitude | Topological phase dislocation | Least reflected action | SiLU / saturation gate | `manuscript/ave-kb/CLAUDE.md` line 51-58 |
| **D — Bare numerical** | (no naming) | (no naming) | (no naming) | (no naming) | Tables, figure captions, code comments — citations without content |

### Key findings

**(F1) Ax 3 substantive disagreement.** Scheme A says Axiom 3 is *Effective Action / Least Reflected Action*. Scheme B says Axiom 3 is *Gravity (Newton's constant)*. These are different axioms entirely, not different names for the same thing. Vol 3 Ch 20:96 line 94 reconciles them implicitly by treating gravity as a Saturation+Action consequence: `ω_local/ω_∞ = 1/(n(R)·S(ε_11))` — but no corpus chapter explicitly states which numbering is canonical.

**(F2) "SiLU" misnomer in Scheme C.** Per `eq_axiom_4.tex`, the saturation kernel is `S(A) = √(1-(A/A_yield)²)` — quarter-circle / Born-Infeld form. SiLU (Sigmoid Linear Unit, neural network activation `x·σ(x)`) is a fundamentally different function. The "SiLU" label in `manuscript/ave-kb/CLAUDE.md:58` was identified as APU-domain accidental import per Grant 2026-04-20 ([handoff at L3_PHASE3_SESSION_20260420.md:430-442](.agents/handoffs/L3_PHASE3_SESSION_20260420.md#L430)) and queued for correction; never fixed.

**(F3) eq_axiom_*.tex files asserted "single source of truth" but disagree with Vol 1 Ch 1.** Each `eq_axiom_*.tex` header reads: *"% Single source of truth. \input this wherever Axiom N is formally restated."* Yet Vol 1 Ch 1 lines 231 and 237 — the chapter that DEFINES the axioms — uses Scheme A naming, not Scheme B. The "single source of truth" claim is unverified against Vol 1 Ch 1.

**(F4) Downstream repos overwhelmingly use Scheme A.** AVE-Metamaterials (91 occurrences), AVE-VirtualMedia (28+ occurrences), AVE-Protein (207 occurrences), AVE-HOPF, AVE-Propulsion, AVE-PONDER, AVE-Fusion — all use Scheme A naming. Scheme B (Gravity-as-Ax 3) appears ONLY in `eq_axiom_*.tex` and a handful of derivative cites within AVE-Core. Scheme C (SiLU label) appears in `manuscript/ave-kb/CLAUDE.md` and a few KB leaves.

**(F5) AVE-APU is the SCHEME C ORIGIN repo.** Per the cross-repo agent investigation, `manuscript/vol_1_axiomatic_components/chapters/02_vca_translation_matrix.tex:102` is the first place where Axiom 4 is formally tied to "saturation gate" as a digital-logic primitive. The KB INVARIANT-S2 scheme labels (ABCD cascade, phase dislocation, SiLU gate) are APU-domain operationalizations of canonical Scheme A axioms, not a separate axiom system. The KB invariant pulled this APU phrasing into the AVE-Core KB without clear source attribution.

**(F6) Ax 3 is reinterpreted (not divergent) across most repos.** AVE-Protein, AVE-VirtualMedia, AVE-Fusion all use "Least Reflected Action" / "S₁₁ minimization" as Axiom 3's content, matching Scheme A. The Scheme B framing of "Axiom 3 = Gravity" is internally contained within AVE-Core's `eq_axiom_3.tex` and has not propagated to downstream repos. **This is evidence that Scheme B is the outlier**, not Scheme A.

**(F7) Auditor's doc 76_ used Scheme B citations.** [research/L3_electron_soliton/76_lattice_to_axiom3_bridge.md](../../research/L3_electron_soliton/76_lattice_to_axiom3_bridge.md) cited `eq_axiom_3.tex:Ax 3 = Gravity` extensively when bridging lattice-Op14 to corpus refractive index. Under canonical Scheme A this is mis-numbered — the gravitational-refractive-index content is a Vol 3 Ch 3 derivation from Ax 1 + Ax 4, NOT a primitive Ax 3. Doc 76_ needs revision.

### Recommended adjudication

The corpus needs ONE explicit canonical-axiom-numbering statement that supersedes all others. Per the evidence (Vol 1 Ch 1 + 7 downstream repos all using Scheme A), **Scheme A is canonical** and the others should be reconciled to it:

- `eq_axiom_3.tex` should be renamed/reframed: gravity-refractive-index content stays, but reframed as "derived from Ax 1 + Ax 4" not "Axiom 3"
- `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2 should be updated to match Scheme A, removing "SiLU" misnomer
- `eq_axiom_*.tex` filenames currently misleading — files should be retitled to match the actual axioms they document, OR moved out of "single source of truth" framing
- A new `manuscript/common_equations/eq_axioms_canonical.tex` could replace the four existing eq_axiom_*.tex files with the Scheme A statements

Doc 76_ revision: renumber Ax 3 references throughout to point at Vol 3 Ch 3 derivation rather than a primitive axiom.

---

## §2 SCHEME INVENTORY (FULL DEFINITIONS)

### §2.1 Scheme A — Canonical Theory (Vol 1 Ch 1 + 00_scoping.md + downstream repos)

**Authority:** [`manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex:48-75`](../../manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex#L48), confirmed by [`backmatter/02_full_derivation_chain.tex:78-112`](../../manuscript/backmatter/02_full_derivation_chain.tex#L78), [`manuscript/ave-kb/common/full-derivation-chain.md:64-92`](../../manuscript/ave-kb/common/full-derivation-chain.md#L64), and [`research/L3_electron_soliton/00_scoping.md:16-56`](../../research/L3_electron_soliton/00_scoping.md#L16).

| # | Name | Statement |
|---|---|---|
| Ax 1 | **LC Network Substrate** (Trace-Reversed Chiral LC Resonant Network in continuum limit) | Vacuum is a discrete LC network with characteristic impedance Z₀ = √(μ₀/ε₀) ≈ 376.73 Ω, lattice pitch ℓ_node = ℏ/(m_e c) ≈ 3.86 × 10⁻¹³ m |
| Ax 2 | **Topo-Kinematic Isomorphism (TKI)** | Charge dimension equals length dimension: [Q] ≡ [L]; conversion ξ_topo = e/ℓ_node |
| Ax 3 | **Effective Action Principle** (Least Reflected Action / S₁₁ minimization) | System minimizes hardware action S_AVE = ∫(½ε₀|∂_t A|² − ½μ₀|∇×A|²)d⁴x; equivalently minimizes |Γ|² at boundaries |
| Ax 4 | **Dielectric Saturation** (Universal Yield Kernel) | Non-linear compliance C_eff = C₀/√(1−(Δφ/α)²); equivalently S(A) = √(1−(A/A_yield)²); saturates to zero at yield boundary |

**Derived consequence (NOT a primitive axiom):** Gravity = G·ξ Machian boundary impedance; refractive index n(r) = 1 + 2GM/(rc²); local clock rate ω_local/ω_∞ = 1/(n·S). Per Vol 3 Ch 3 + Vol 3 Ch 20.

**A-034 substance-enrichment of Ax 4 (canonical 2026-05-15 evening):** the same S(A) = √(1−A²) kernel governs **every topological-reorganization event at every scale** — 19-instance catalog spanning 21 orders of magnitude, classified by 3-way symmetry (SYM / ASYM-N / ASYM-E). Empirical anchors: BCS B_c(T) at 0.00% error (Vol 3 Ch 9); BH ring-down at 1.7% from GR exact (Vol 3 Ch 15, 3 LIGO events); NOAA GOES 40-yr solar-flare validation (Vol 3 Ch 14); Schwarzschild radius exact match. **This enriches Scheme A's Ax 4 without changing the numbering** — A-034 is the cross-scale empirical demonstration that the kernel asserted by Vol 1 Ch 1:75 is indeed universal. Full catalog: [Backmatter Ch 7 — Universal Saturation-Kernel Catalog](../../backmatter/07_universal_saturation_kernel.tex); canonical synthesis: [trampoline-framework.md §7.5](trampoline-framework.md). Cross-corpus impact: all 8 downstream repos' Ax 4 citations now inherit the 19-instance backing.

### §2.2 Scheme B — CommonEqs Engineering (eq_axiom_*.tex only)

**Authority:** four files in [`manuscript/common_equations/`](../../manuscript/common_equations/):

| # | File | Asserted Name |
|---|---|---|
| Ax 1 | [`eq_axiom_1.tex:4`](../../manuscript/common_equations/eq_axiom_1.tex#L4) | "Axiom 1 — Impedance" |
| Ax 2 | [`eq_axiom_2.tex:4`](../../manuscript/common_equations/eq_axiom_2.tex#L4) | "Axiom 2 — Fine Structure" |
| Ax 3 | [`eq_axiom_3.tex:4`](../../manuscript/common_equations/eq_axiom_3.tex#L4) | "Axiom 3 — Gravity" |
| Ax 4 | [`eq_axiom_4.tex:4`](../../manuscript/common_equations/eq_axiom_4.tex#L4) | "Axiom 4 — Universal Saturation Kernel" |

Each file's header asserts: *"% Single source of truth. \input this wherever Axiom N is formally restated."*

**Substantive disagreement with Scheme A:**
- Ax 1 same as Scheme A in content (LC network) but renamed "Impedance" 
- Ax 2 different in content: Scheme B says "Fine Structure" (α coupling), Scheme A says "Topo-Kinematic Isomorphism ([Q]≡[L])" — these are RELATED but not identical. Scheme B treats α as primitive; Scheme A treats α as derived from TKI + ν_vac=2/7.
- Ax 3 SUBSTANTIVELY DIFFERENT: Scheme B says "Gravity" (G is primitive); Scheme A says "Effective Action" (S₁₁ minimization is primitive). These are different axioms.
- Ax 4 same in spirit (saturation kernel S(A)=√(1-A²)) but different framing language.

### §2.3 Scheme C — KB INVARIANT-S2 (APU-flavored)

**Authority:** [`manuscript/ave-kb/CLAUDE.md:51-60`](../../manuscript/ave-kb/CLAUDE.md#L51), labeled "INVARIANT-S2: AVE Axiom numbering."

| # | Name |
|---|---|
| Ax 1 | ABCD cascade / coupled amplitude |
| Ax 2 | Topological phase dislocation |
| Ax 3 | Least reflected action |
| Ax 4 | **SiLU / saturation gate** (dielectric saturation) — *misnomer; see F2* |

CLAUDE.md line 60: *"Confirmed by: vol1 (originating), vol8 (re-instantiated in virtual media domain)"* — this confirmation claim is unverified; Vol 1 Ch 1 uses Scheme A naming, not Scheme C.

**Per Grant 2026-04-20 ([L3_PHASE3_SESSION_20260420.md:430-442](L3_PHASE3_SESSION_20260420.md#L430)):**

> *"this KB variant accidentally picked up APU-domain phrasing (from AVE-APU's circuit-compiler terminology). It is NOT the canonical AVE-Core axiom naming. KB CLAUDE.md INVARIANT-S2 is a queued correction item (not done this session)."*

7-day-old technical debt; never fixed.

### §2.4 Scheme D — Bare Numerical (no scheme content)

Many files cite "Axiom 1" or "Per Axiom 4" without naming or describing the axiom. These are scheme-agnostic citations — they reference a numerical index without invoking specific scheme content. Cataloged but not classified into A/B/C.

---

## §3 AVE-CORE — Full Pedantic Catalog

### §3.1 Files containing AXIOM-LIST or AXIOM-DEFINITION (Scheme A/B/C — content-bearing)

#### `manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex` (Scheme A — CANONICAL)

**Line 48:** `\section{The Four Fundamental Axioms}` — chapter section heading

**Lines 51-67 (axiom definitions):**

```
51:    The framework rests on four explicit axioms:
52:    (1) the LC network substrate, (2) the topo-kinematic isomorphism,
53:    (3) the effective action principle, and (4) non-linear dielectric saturation.
54:    [Axiom 1 — Substrate Topology resultbox]
61:    [Axiom 2 — Topo-Kinematic Isomorphism resultbox]
68:    [Axiom 3 — Effective Action Principle resultbox]
75:    [Axiom 4 — Dielectric Saturation resultbox]
```

**Lines 218-222 (master constants table — BARE references):**

```
218: $\ell_{node} = \hbar/m_e c$ ... Axiom 1 (unknot)
219: $\alpha = p_c/8\pi$         ... Axiom 4 (EMT $K=2G$)
220: $\xi_{topo} = e/\ell_{node}$ ... Axiom 2 ($[Q]\equiv[L]$)
221: $V_{snap} = m_e c^2/e$      ... Axiom 4 (dielectric limit)
222: $Z_0 = \mu_0 c$              ... Axiom 1 ($\sqrt{\mu_0/\epsilon_0}$)
```

Note: line 219 attributes α-derivation to "Axiom 4 (EMT K=2G)" — but α is per Scheme A's Ax 2 + Ax 1 interlink. This is **internal Vol 1 Ch 1 inconsistency** between line 219 and lines 219-222 of the master-constants attribution. Worth flagging.

**Line 231 (chapter summary):**
> *"Four explicit axioms fully describe the network: (1) The LC Chiral network substrate, (2) the Topo-Kinematic Isomorphism defining charge as geometric length (e/ℓ_node), (3) the Effective Hardware Action representing standard QED, and (4) Non-Linear Dielectric Saturation."*

**Line 237 (chapter summary, restated):**
> *"Four axioms define the vacuum: (1) LC network substrate, (2) topo-kinematic isomorphism ([Q] ≡ [L]), (3) minimisation of the hardware action S_AVE, (4) non-linear dielectric saturation S(r) = √(1 − r²)."*

**Verdict:** Vol 1 Ch 1 is the canonical Scheme A source. Lines 51-75 + 231 + 237 all consistently name Ax 1=LC substrate, Ax 2=TKI, Ax 3=Effective Action, Ax 4=Saturation.

---

#### `manuscript/backmatter/02_full_derivation_chain.tex` (Scheme A)

**Lines 80-112:** Formal `\begin{axiom}...\end{axiom}` environments matching Vol 1 Ch 1's Scheme A. Confirms Scheme A as canonical.

#### `manuscript/ave-kb/common/full-derivation-chain.md` (Scheme A)

**Lines 64-92:** Markdown mirror of `backmatter/02_full_derivation_chain.tex`. Confirms Scheme A.

---

#### `manuscript/common_equations/eq_axiom_1.tex` (Scheme B)

**Line 1:** `% eq_axiom_1.tex — Axiom 1 (Impedance)` (header comment)

**Line 4:** `\begin{resultbox}{Axiom 1 — Impedance}` (formal box header)

**Lines 5-17:** Definition body — Z₀ = √(μ₀/ε₀) and ℓ_node = ℏ/(m_e c). Same content as Scheme A's Ax 1, different name.

#### `manuscript/common_equations/eq_axiom_2.tex` (Scheme B)

**Line 1:** `% eq_axiom_2.tex — Axiom 2 (Fine Structure)`

**Line 4:** `\begin{resultbox}{Axiom 2 — Fine Structure}`

**Lines 5-15:** α = e²/(4πε₀ℏc); V_yield = √α·V_snap.

#### `manuscript/common_equations/eq_axiom_3.tex` (Scheme B — DIVERGENT FROM A)

**Line 1:** `% eq_axiom_3.tex — Axiom 3 (Gravity)`

**Line 4:** `\begin{resultbox}{Axiom 3 — Gravity}`

**Lines 5-19:** G = ℏc/(7ξ·m_e²); n(r) = 1 + 2GM/(rc²); μ_eff = μ₀·n(r), ε_eff = ε₀·n(r), Z = Z₀ invariant.

**Lines 21-31:** Derived consequence — α exact-invariance under gravitational strain (derived from Ax 4 + Ax 3 symmetric scaling).

**Lines 35-44:** Temporal/spatial split: n_temporal = 1 + (2/7)·ε_11 (clock rate); n_spatial = (9/7)·ε_11 (light deflection).

**Substantive divergence from Scheme A:** Scheme A's Axiom 3 is "Effective Action Principle" (S₁₁ minimization). Scheme B's Axiom 3 is "Gravity" (Newton's constant + refractive index). These are NOT the same axiom.

#### `manuscript/common_equations/eq_axiom_4.tex` (Scheme B — same content as Scheme A's Ax 4)

**Line 1:** `% eq_axiom_4.tex — Axiom 4 (Saturation / Universal Yield Kernel)`

**Line 4:** `\begin{resultbox}{Axiom 4 — Universal Saturation Kernel}`

**Lines 6-25:** S(A) = √(1−(A/A_yield)²); table of derived effects μ_eff, ε_eff, C_eff, Z, **c_eff = c₀·S^(1/2)**.

**Lines 31-40:** Confinement theorem — particles via torus-knot self-intersection (B saturates μ → Γ→-1 → standing wave); gravity via mass defect (ε_11→1 → G_shear→0 → event horizon).

---

#### `manuscript/ave-kb/CLAUDE.md` (Scheme C — APU-flavored, KNOWN-NON-CANONICAL)

**Lines 51-60:**
```
51: ### INVARIANT-S2: AVE Axiom numbering
52: 
53: The four AVE axioms carry stable meanings across all volumes:
54: 
55: - Axiom 1: ABCD cascade / coupled amplitude
56: - Axiom 2: Topological phase dislocation
57: - Axiom 3: Least reflected action
58: - Axiom 4: SiLU / saturation gate (dielectric saturation)
59: 
60: *Confirmed by: vol1 (originating), vol8 (re-instantiated in virtual media domain)*
```

**Status:** queued for correction since 2026-04-20 ([L3_PHASE3_SESSION_20260420.md:430-442](L3_PHASE3_SESSION_20260420.md#L430)). Never fixed.

#### `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md` (Scheme C)

**Lines 4-6:** KB-side mirror of Scheme C labeling per INVARIANT-S2.

---

#### `manuscript/backmatter/12_mathematical_closure.tex` (Scheme A)

**Lines 74-77:** Restatement of Vol 1 Ch 1 axiom list. Scheme A.
**Lines 83-86:** Application of axioms to mathematical-closure derivation. Scheme A.

---

### §3.2 Files containing AXIOM-CITATIONS (Bare numerical or content-rich application)

#### `manuscript/vol_3_macroscopic/chapters/03_macroscopic_relativity.tex`

**Line 8:** *"Formulate General Relativity as Applied Vacuum Engineering: the optical metric of a refractive dielectric medium."* — application of Ax 3 (gravity content per Scheme B / derived consequence per Scheme A)

**Line 109+:** "The Absolute Intergalactic Speed of Light (c_max)" — derives c_local = c₀/n(r) from refractive index. Cited as Scheme A derived consequence in Vol 3 Ch 3, identical content to Scheme B's Ax 3.

**Line 121:** *"the local speed of light measured on Earth (299,792,458 m/s) is artificially constrained by ambient galactic dielectric density."*

#### `manuscript/vol_3_macroscopic/chapters/20_white_dwarf_predictions.tex`

**Lines 94-99:** **Combined Ax 3 + Ax 4 local clock rate equation:**
```
ω_local / ω_∞  =  1 / (n(R) · S(ε_11))
```
Where n(R) is "Axiom 3" and S(ε_11) is "Axiom 4." This usage references Scheme B's Ax 3 (gravity refractive index) explicitly.

#### `manuscript/common_equations/eq_axiom_3.tex` (already cataloged §3.1)

#### `manuscript/vol_2_subatomic/chapters/06_electroweak_and_higgs.tex:84`

> *"p_c = 8πα — packing fraction (Axiom 4: Saturation)"*

Bare numerical, but with Scheme A naming ("Saturation" — matches Ax 4).

#### `manuscript/vol_3_macroscopic/chapters/15_black_hole_orbital_resonance.tex`

> *"Axiom 4: ε₁₁(r_sat) = 1 gives r_sat = 7M_g"*

Bare numerical, Scheme A naming.

#### `manuscript/vol_3_macroscopic/chapters/21_black_hole_interior_regime_iv.tex` (line 41)

> *"The impedance is therefore invariant"* — application of Scheme A Ax 1 + Scheme A Ax 4.

#### `manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex` (line 40)

> *"Z(r) = √(μ_eff/ε_eff) = Z_0 (invariant)"* — application of Scheme B's Ax 3 derived consequence (achromatic impedance matching).

#### `manuscript/common_equations/eq_axiom_3.tex` line 32-33 mentions multi-species clock comparisons predict null Δα/α — application of Ax 3 + Ax 4 symmetric scaling.

#### `manuscript/backmatter/04_physics_engine_architecture.tex`

References Axiom 4 demonstrations + MOND. Scheme A.

#### `manuscript/backmatter/appendix_c_derived_numerology.tex`

Multiple BARE numerical references in derivation tables.

---

### §3.3 AVE-Core Research Docs

#### `research/L3_electron_soliton/00_scoping.md` lines 16-56 (Scheme A, marked "CANONICAL")

> *"CANONICAL for AVE field-theory formalism"*

Lists Ax 1=LC network, Ax 2=TKI, Ax 3=Effective Action, Ax 4=Saturation. Authoritative for L3 work.

#### `research/L3_electron_soliton/03_existence_proof.md`

References Ax 4 (saturation) at multiple lines. Scheme A naming.

#### `research/L3_electron_soliton/35_halfcover_derivation_audit.md` (lines 511-526) — **EXPLICITLY FLAGS THE DISCREPANCY**

```
508: ### §11.1 Axiom numbering inconsistency
509: 
510: KB CLAUDE.md claims the four axioms are:
511: - Axiom 1: ABCD cascade / coupled amplitude
512: - Axiom 2: Topological phase dislocation
513: - Axiom 3: Least reflected action
514: - Axiom 4: SiLU / saturation gate
515: 
516: But `manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex`
517: names them:
518: - Axiom 1: LC Network substrate (K4 topology)
519: - Axiom 2: Topo-kinematic isomorphism ([Q] ≡ [L])
520: - Axiom 3: Effective Action Principle (Maxwell form)
521: - Axiom 4: Dielectric saturation
522: 
523: **These differ substantively.** The KB's "ABCD cascade / coupled
524: amplitude" is not how Ch 1 frames Axiom 1. Worth flagging for a
525: separate audit — not directly relevant to this doc but indicates
526: cross-volume axiom-labeling drift.
```

**This audit existed at line 526 and was queued.** This homologation doc is the follow-up audit it was queued for.

#### `research/L3_electron_soliton/54_pair_production_axiom_derivation.md` lines 12-15 (Scheme A)

Maps axioms to K4, flux tubes, Vacuum Varactor saturation. Scheme A.

#### `research/L3_electron_soliton/71_multi_seed_eigenmode_sweep.md` line 55

> *"under SiLU saturation kernel (Ax4), TDI may settle..."*

**Inherited Scheme C "SiLU" misnomer.** Auditor's own writing — flagged for correction.

#### `research/L3_electron_soliton/76_lattice_to_axiom3_bridge.md` (auditor's recent doc — uses Scheme B)

Cites `eq_axiom_3.tex:Ax 3 = Gravity` extensively. Under canonical Scheme A this is mis-numbered. Doc 76_ requires revision per F7.

---

### §3.4 AVE-Core Audit / Handoff Docs

#### `.agents/kb_audit/phase-0-axioms.md` (Scheme B, with note about C)

```
| 1 | **Impedance** | Vacuum is an LC resonant network with Z₀ = √(μ₀/ε₀)
| 2 | **Fine Structure** | α = e²/(4πε₀ℏc)
| 3 | **Gravity** | G = ℏc/(7ξ·m_e²)
| 4 | **Saturation** | S(A) = √(1−(A/A_yield)²)
```

> *"KB cross-cutting-invariant notation uses Axioms 1–4 with slightly different labels (Ch.1 ABCD cascade / phase dislocation / least reflected action / SiLU saturation — CLAUDE.md INVARIANT-S2). The README's 4-axiom list is a plain-language restatement, not the KB-canonical form."*

This doc explicitly maps Scheme B (its primary listing) and mentions Scheme C as a "different label" — but doesn't reconcile to Vol 1 Ch 1's Scheme A.

#### `.agents/handoffs/L3_PHASE3_SESSION_20260420.md` lines 428-442 — **GRANT'S 2026-04-20 CORRECTION**

```
428: ## §15  Documentation note: KB invariants axiom naming
430: [`manuscript/ave-kb/CLAUDE.md`](../../manuscript/ave-kb/CLAUDE.md) INVARIANT-S2 lists the AVE axioms as:
431: - Axiom 1: ABCD cascade / coupled amplitude
432: - Axiom 2: Topological phase dislocation
433: - Axiom 3: Least reflected action
434: - Axiom 4: SiLU / saturation gate
436: Grant clarified 2026-04-20: this KB variant accidentally picked up APU-domain phrasing 
437: (from AVE-APU's circuit-compiler terminology). It is NOT the canonical AVE-Core axiom naming. 
438: The canonical statements in `research/L3_electron_soliton/00_scoping.md` and 
439: `docs/framing_and_presentation.md` are:
440: - Axiom 1: K4 diamond graph of LC cells at pitch ℓ_node
441: - Axiom 2: Wave propagation, K = 2G (trace-reversed Cosserat)
442: - Axiom 3: Reflection Γ at impedance boundaries
443: - Axiom 4: Dielectric saturation at Nyquist yield
```

> *"KB CLAUDE.md INVARIANT-S2 is a queued correction item (not done this session)."*

**Grant's 2026-04-20 framing is a SUBTLE VARIANT of Scheme A** — same Ax 1=LC, Ax 4=Saturation, but Ax 2 is "Wave propagation, K=2G" (instead of TKI [Q]≡[L]) and Ax 3 is "Reflection Γ at impedance boundaries" (instead of Effective Action). These are physically related but differently-emphasized framings.

---

### §3.5 AVE-Core Source Code Comments

#### `src/ave/topological/cosserat_field_3d.py`

Multiple comments reference "Axiom 4 saturation" with formula S(A) = √(1-A²). Scheme A naming.

#### `src/ave/core/k4_tlm.py`

References Axiom 1 LC structure, Axiom 4 saturation. Scheme A.

#### `manuscript/predictions.yaml`

Per-prediction `axioms_used: [1, 2, 4]` etc. — Scheme D (bare numerical). 60+ entries. Reproducibility-tracking purpose, not scheme-content.

---

### §3.6 AVE-Core Catalog — Summary Counts

Per cross-repo agent investigation of AVE-Core (79 distinct content-bearing occurrences):

- **Scheme A occurrences:** 31 (Vol 1 Ch 1 + backmatter + ave-kb common + 00_scoping.md + L3 research)
- **Scheme B occurrences:** 12 (the 4 eq_axiom_*.tex files + their Vol 3 derivative cites + phase-0-axioms.md)
- **Scheme C occurrences:** 8 (KB CLAUDE.md INVARIANT-S2 + KB axiom-definitions.md + research-doc inherited cites)
- **Scheme D (BARE numerical):** 28+ (tables, code annotations, application cites)

---

## §4 AVE-APU — Scheme C Origin

**Authority:** per cross-repo agent investigation. AVE-APU is identified as the **provenance** for Scheme C's APU-flavored labeling (ABCD cascade, SiLU gate).

### §4.1 The Scheme C origin file

#### `manuscript/vol_1_axiomatic_components/chapters/02_vca_translation_matrix.tex:102`

```
102: The VCA Geometric Triode relies purely on Axiom 4: a transverse standing wave 
     (Gate pressure, red double-line) is continuously applied across the longitudinal funnel,
     summing total field stress toward V_snap and causing pure spatial impedance blockades.
```

**This is the first formalization in APU manuscript of Axiom 4 as a "saturation gate" digital-logic primitive.** The KB's INVARIANT-S2 phrasing (SiLU/saturation gate) appears to derive from this APU operationalization.

### §4.2 Major AVE-APU axiom occurrences (Scheme A naming, APU-domain operationalization)

| File | Line(s) | Scheme | Content |
|---|---|---|---|
| `manuscript/vol_1_axiomatic_components/chapters/02_vca_translation_matrix.tex` | 102 | C origin | Axiom 4 → saturation gate / V_snap blockade |
| `manuscript/vol_1_axiomatic_components/chapters/03_vacuum_thermodynamics.tex` | 17, 22, 46 | A with Ax 2 divergence flag | Line 22 says "Axiom 2 = topological scaling / losslessness" — non-canonical |
| `manuscript/vol_1_axiomatic_components/chapters/04_geometric_diodes.tex` | 6, 14, 34 | A | Axiom 4 → diode saturation behavior |
| `manuscript/vol_1_axiomatic_components/chapters/05_geometric_triodes.tex` | 6, 11, 14, 18, 27, 32, 42, 46, 59, 176, 178, 197 | A | Axiom 1 + Axiom 4 jointly govern triode transconductance |
| `manuscript/vol_1_axiomatic_components/chapters/06_dielectric_delay_lines.tex` | 6, 16, 44, 103 | A | Axiom 1 LC parameters + Axiom 4 ceiling |
| `manuscript/vol_1_axiomatic_components/chapters/08_static_soliton_kinks.tex` | 6, 8, 17, 28, 159, 198 | A | Axioms 1+4 jointly derive sine-Gordon kinks |
| `manuscript/vol_1_axiomatic_components/chapters/09_axiomatic_transducers.tex` | 17 | A | "Mismatch Penalty from Axiom 3" — first APU Ax 3 invocation |
| `manuscript/vol_1_axiomatic_components/chapters/10_hardware_netlists_spice.tex` | 18, 81 | A | Axiom 4 dielectric rolloff in capacitor SPICE |
| `manuscript/vol_2_topological_routing_logic/chapters/13_geometric_multiplexing.tex` | 41 | A → C operationalized | Axiom 4 saturation boundary V_snap |
| `manuscript/vol_2_topological_routing_logic/chapters/14_topological_clocks.tex` | 23 | A | Axiom 4 lattice spacing limit ℓ_node |
| `manuscript/vol_2_topological_routing_logic/chapters/17_topological_logic.tex` | 18, 30 | A → C operationalized | "Axiom 4 Native Geometric XOR Gate" — Scheme C reinforced |
| `manuscript/vol_3_apu_architecture/chapters/22_apu_design_methodology.tex` | 54, 61 | A → C operationalized | Axiom 4 hardware design rule |
| `manuscript/vol_3_apu_architecture/chapters/27_axiomatic_processing_unit_capstone.tex` | 43, 94, 122 | A summary | "All APU derived from Axioms 1–4" |
| `.agents/handoffs/core_solver_abstractions.md` | 26-29 | C operational | "Axiom 4 Saturation Clipper (S Operator)" — code-level primitive |
| `hardware/vca_core/README.md` | 10 | C operational | "Topological ERC: bounds derived from Axiom 4 yielding" |

### §4.3 AVE-APU finding

AVE-APU does not introduce a NEW axiom-numbering scheme. It uses Scheme A naming consistently across all manuscript chapters. The Scheme C "SiLU / saturation gate" labeling appears to be a HANDOFF-DOC and KB-LEVEL operationalization, not a manuscript-level axiom. The KB INVARIANT-S2's "ABCD cascade / coupled amplitude / SiLU gate" phrasing pulled APU operational vocabulary into AVE-Core's KB metadata without flagging it as APU-derivative.

---

## §5 AVE-VirtualMedia — Scheme A Application to LLMs

### §5.1 Major occurrences (all Scheme A)

| File | Line(s) | Content |
|---|---|---|
| `README.md` | 13 | Brief feature listing — bare numerical |
| `manuscript/vol_virtual_media/chapters/01_llm_topology.tex` | 22, 27, 28, 45, 46 | Foundational mapping; Axioms 1, 3, 4 → LLM transformer |
| `manuscript/vol_virtual_media/chapters/02_hardware_software_inversion.tex` | 62 | "Axiom 4 remains universally invariant" |
| `manuscript/vol_virtual_media/chapters/03_universal_operator_mapping.tex` | 16-29, 31, 33 | **Table 3.1 — formal axiom-to-LLM correspondence** |
| `manuscript/vol_virtual_media/chapters/04_experimental_audit.tex` | 13, 52 | Axiom 1 + 3 + 4 in pruning |
| `manuscript/vol_virtual_media/chapters/05_global_ac_scope.tex` | 1, 16, 20 | Chapter dedicated to Axiom 4 expansion + Ax 1 continuity |
| `manuscript/vol_virtual_media/chapters/06_continuous_manifold_smoothing.tex` | 13, 19 | Ax 3 (min reflection) + Ax 4 (saturation) for pruning |
| `manuscript/vol_virtual_media/chapters/07_operator_unification.tex` | 13, 14 | "Axiom 2: The Continuous Phase Tension (ξ_topo)" |
| `manuscript/vol_virtual_media/chapters/08_discrete_manifold_masking.tex` | 50, 52 | Axiom 1 → effective impedance Z_eff |
| `manuscript/vol_virtual_media/chapters/09_gamma_scaling_law.tex` | 69, 71, 83 | Axiom 1 cascade transfer function |
| `manuscript/vol_virtual_media/chapters/10_attention_head_impedance.tex` | 70, 117, 119, 142 | Axiom 2 → topological rank collapse in attention heads |
| `manuscript/vol_virtual_media/chapters/11_moe_dynamic_impedance.tex` | 19, 31, 40, 77 | "The Router as Axiom 3" — MoE routing = least reflected action |
| `manuscript/vol_virtual_media/chapters/12_sigmoid_saturation.tex` | 43, 104 | Sigmoid as topologically equivalent to S(r) saturation |

### §5.2 AVE-VirtualMedia finding

**Pure Scheme A application; no new scheme introduced.** Axiom 3 here is "Least Reflected Action" / min |Γ|² — matching Scheme A, NOT matching Scheme B's "Gravity." Confirms F6 (downstream repos use Scheme A's Ax 3 = Action, not Scheme B's Ax 3 = Gravity).

---

## §6 AVE-HOPF — Scheme A Application

### §6.1 Major occurrences

| File | Line(s) | Scheme | Content |
|---|---|---|---|
| `manuscript/03_hopf_01_chiral_verification.tex` | 13 | A | Axiom 1 = chiral vacuum LC network |
| `scripts/hopf_02_spatial_refraction.py` | various | A | Ax 1 LC + Ax 4 saturation in chiral antenna |
| `scripts/chiral_antenna_q_analysis.py` | various | A | Q-factor analysis cites Ax 1, Ax 2 |
| `scripts/hopf_01_s11_sweep.py` | various | A | S₁₁ minimization (Ax 3 — Scheme A naming) |
| `scripts/hopf_01_s21_parallax.py` | various | A | Parallax cited via Ax 1 |

### §6.2 AVE-HOPF finding

Pure Scheme A. Hopf antenna domain naturally aligns with Ax 3 = Effective Action (S₁₁ minimization), matching Scheme A.

---

## §7 AVE-Propulsion — Scheme A Application

### §7.1 Major occurrences

| File | Lines | Scheme | Content |
|---|---|---|---|
| `manuscript/vol_propulsion/chapters/01_local_refractive_control.tex` | various | A | Ax 1 LC + Ax 4 saturation in refractive index control |
| `manuscript/vol_propulsion/chapters/01_ave_resolutions.tex` | various | A | Multiple axiom citations |
| `manuscript/vol_propulsion/chapters/05_autoresonant_dielectric_rupture.tex` | various | A | Axiom 4 dielectric rupture |
| `src/scripts/simulate_warp_metric_oam_drill.py` | various | A | Ax 4 saturation in warp-metric simulation |
| `src/scripts/simulate_chiral_acoustic_rectification.py` | various | A | Ax 1 + Ax 2 chirality |
| `src/scripts/simulate_warp_metric_cfd.py` | various | A | Ax 1 LC |
| `src/scripts/water_rectification_amplification.py` | various | A | Ax 1 + Ax 4 |
| `src/scripts/simulate_warp_metric_time_evolution_3d.py` | various | A | Ax 1 + Ax 4 |

### §7.2 AVE-Propulsion finding

Pure Scheme A. ~25 distinct axiom citations across manuscript + scripts. No divergence.

---

## §8 AVE-PONDER — Scheme A Application

### §8.1 Major occurrences

| File | Lines | Scheme | Content |
|---|---|---|---|
| `manuscript/vol_ponder/chapters/01_topological_thrust_mechanics.tex` | various | A | Ax 1 LC + Ax 2 chirality in thrust mechanics |
| `manuscript/vol_ponder/chapters/03_high_voltage_vhf_drive.tex` | various | A | Ax 4 dielectric breakdown |
| `manuscript/vol_ponder/chapters/04_ponder_05_dc_biased_quartz.tex` | various | A | Ax 1 + Ax 4 |
| `manuscript/vol_ponder/chapters/05_vacuum_torsion_metrology.tex` | various | A | Multiple |
| `src/scripts/ponder_05_characterization.py` | various | A | Ax 4 saturation |
| `src/scripts/ponder_01_regime_sensitivity.py` | various | A | Ax 1 |
| `src/scripts/ponder_05_gravity_parallax.py` | various | A | Gravity citation — Scheme A derived consequence (NOT Scheme B Ax 3) |
| `src/scripts/ponder_01_characterization.py` | various | A | Ax 1 |
| `src/scripts/plot_ponder05_saturation.py` | various | A | Ax 4 |
| `src/scripts/simulate_ponder_01_thrust_firstprinciples.py` | various | A | Ax 1 + Ax 4 |

### §8.2 AVE-PONDER finding

Pure Scheme A. ~17 occurrences. Notably, gravity citations are framed as Ax 3 derived consequence (Scheme A) NOT as a primitive axiom (Scheme B).

---

## §9 AVE-Metamaterials — Scheme A Application (91 occurrences)

### §9.1 Major content-bearing occurrences

| File | Lines | Scheme | Content |
|---|---|---|---|
| `manuscript/vol_1_active_metamaterials/frontmatter/00_title.tex` | 12 | BARE | Mentions Ax 4 |
| `manuscript/vol_1_active_metamaterials/chapters/02_active_topological_framework_configuration.tex` | 19, 41, 48, 62, 71, 75, 76, 111, 127, 160, 171, 232-242 | A | Critical chapter — table mapping all 4 axioms to material parameters |
| `manuscript/vol_1_active_metamaterials/chapters/03_superconducting_metamaterials.tex` | 19, 23, 29 | A | "Manufacturing Kill-Switch (Axiom 4)" |
| `manuscript/vol_1_active_metamaterials/chapters/04_kinetic_phase_armor.tex` | various | A | Ax 1 + Ax 4 |
| `manuscript/vol_1_active_metamaterials/chapters/06_casimir_cavities.tex` | 19-20, 55 | A | Ax 1 + Ax 4 boundary |
| `manuscript/vol_1_active_metamaterials/chapters/08_casimir_shielded_topological_qubits.tex` | 8, 24, 57, 80-93 | A | Lattice dispersion derivation from Ax 1 |
| `.agents/handoffs/core_solver_integration.md` | 8, 12-16, 29-33, 52-56, 94-98 | A | Five-phase axiom-pinned integration plan |

### §9.2 AVE-Metamaterials finding

91 total occurrences, all Scheme A. The chapter `02_active_topological_framework_configuration.tex` lines 232-242 has a **complete axiom-traceability table** mapping every parameter to its axiom source — this is the most rigorous example of axiom application across the org.

---

## §10 AVE-Fusion — Scheme A with Mechanical Ax 3 Extension

### §10.1 Major occurrences

| File | Lines | Scheme | Content |
|---|---|---|---|
| `README.md` | title | BARE | "Axiomatic Energy Systems" |
| `manuscript/vol_fusion/chapters/01_topological_resonance.tex` | various | A | Ax 4 → Gamow tunneling probability |
| `manuscript/vol_fusion/chapters/03_metric_catalyzed_fusion.tex` | various | A | Ax 4 saturation kernel scaling laws |
| `manuscript/vol_fusion/chapters/04_the_palladium_proxy.tex` | 16, 19, 49, 55, 65, 85 | A with Ax 3 mech extension | **TWO Ax 3 references treat impedance-matching at nuclear defect sites as Ax 3 — non-gravitational** |
| `manuscript/vol_fusion/chapters/05_metamaterial_caging.tex` | various | A | Multiple |
| `.agents/handoffs/MATH_CODE_AUDIT.md` | various | A | Ax 4 as forbidden-physics constraint |
| `.agents/handoffs/INFRASTRUCTURE_BLUEPRINT.md` | various | A | Axiom compliance |
| `src/scripts/simulate_pd_impedance_match.py` | various | A | "Axiom 3 Boundary Conditions" — code-level mechanical Ax 3 |
| `src/scripts/simulate_pd_borromean_absorber.py`, `simulate_pd_fracture_limit.py` | various | A | Ax 4 yield boundaries |

### §10.2 AVE-Fusion divergence flag

Two occurrences in `chapters/04_the_palladium_proxy.tex` (lines 16 and 19) and one in `src/scripts/simulate_pd_impedance_match.py` use "Axiom 3" to mean **mechanical impedance matching at material boundaries**, NOT gravitational refraction. This is consistent with Scheme A's Ax 3 = Effective Action / Reflection Γ at boundaries (per Grant 2026-04-20 framing), but visually different from `eq_axiom_3.tex`'s "Gravity" labeling.

**Reading:** AVE-Fusion uses Scheme A's broader interpretation of Ax 3 (impedance boundary conditions), not Scheme B's narrow interpretation (Newton's G).

---

## §11 AVE-Protein — Scheme A with Extended Ax 3 (207 occurrences)

### §11.1 Major occurrences

| File | Lines | Scheme | Content |
|---|---|---|---|
| `manuscript/vol_protein/chapters/03_deterministic_protein_folding.tex` | various | A | Axiom pipeline: Axioms 1-2 → bond lengths → Ramachandran → topological impedance |
| `manuscript/vol_protein/chapters/04_simulation_architecture.tex` | various | A | **Complete parameter-traceability table** — 21 derived constants traced to Axioms 1-4 |
| `manuscript/vol_protein/chapters/05_folding_roadmap.tex` | various | A with Ax 3 ext | "Axiom 3 target f(θ) = Σ|Γ_i|²" — Ax 3 reinterpreted as min-reflection principle |
| `src/ave_protein/regime_2_nonlinear/protein_fold.py` | various | A | Ax 4 saturation in TDI |
| `src/ave_protein/solvers/protein_bond_constants.py` | various | A | "Axioms 1-4 → ℓ_node → m_e → α → nuclear binding" |
| `src/ave_protein/engines/s_param_network_engine.py` | various | A | All constants traced to Axioms 1-4 |
| `src/ave_protein/engines/s11_fold_engine_v3_jax.py` | various | A | S₁₁ minimization (Ax 3) |
| `src/ave_protein/engines/s11_fold_engine_v4_ymatrix.py` | various | A | S₁₁ |

### §11.2 AVE-Protein finding

207 occurrences (largest in any single repo). All Scheme A. **Notably, AVE-Protein systematically uses Ax 3 = "S₁₁ minimization / least reflected action" — exactly Scheme A's Ax 3, NOT Scheme B's "Gravity."** This is the clearest cross-repo evidence that Scheme A is canonical and Scheme B (Gravity-as-Ax 3) is the outlier.

Key cross-domain consistency: Axiom 4 saturation formula `S = √(1−(x/x_yield)²)` is **identical in protein folding and galactic rotation** — evidence of the framework's scale-invariance under Scheme A.

---

## §12 CROSS-CUTTING FINDINGS

### §12.1 Total occurrences across all 9 repos

Approximate counts of content-bearing axiom listings/applications:

| Repo | Total | Scheme A | Scheme B | Scheme C | Bare/Numerical |
|---|---|---|---|---|---|
| AVE-Core | 79 | 31 | 12 | 8 | 28 |
| AVE-APU | 28 | 25 | 0 | 3 (operational) | 0 |
| AVE-VirtualMedia | 28 | 28 | 0 | 0 | 0 |
| AVE-HOPF | 11 | 11 | 0 | 0 | 0 |
| AVE-Propulsion | 25 | 25 | 0 | 0 | 0 |
| AVE-PONDER | 17 | 17 | 0 | 0 | 0 |
| AVE-Metamaterials | 91 | 91 | 0 | 0 | 0 |
| AVE-Fusion | 34 | 34 | 0 | 0 | 0 |
| AVE-Protein | 207 | 207 | 0 | 0 | 0 |
| **TOTAL** | **520** | **469** | **12** | **11** | **28+** |

**Scheme A is dominant by an order of magnitude.** Scheme B exists only inside AVE-Core's `eq_axiom_*.tex` files. Scheme C exists only in AVE-Core's KB INVARIANT-S2 + a few derivatives.

### §12.2 The Ax 3 substantive disagreement

This is the only place where the schemes substantively disagree on what an axiom IS (not just how it's named).

| Source | Ax 3 Statement |
|---|---|
| Scheme A (Vol 1 Ch 1, 00_scoping.md, 8 downstream repos) | Effective Action / S₁₁ minimization / Least Reflected Action / Reflection Γ at boundaries |
| Scheme B (`eq_axiom_3.tex` only) | Gravity (Newton's G + refractive index n(r)) |

**Reconciliation per `eq_axiom_3.tex` itself:** the gravity content has α-invariance (lines 21-31) and temporal/spatial split (lines 35-44) as DERIVED CONSEQUENCES under Symmetric Gravity (μ_eff = μ₀·n, ε_eff = ε₀·n). This means gravity-as-refractive-index is a Scheme A Ax 1 + Ax 4 consequence, not a primitive Ax 3. **Scheme B's framing of Ax 3 as Gravity is therefore reducible to Scheme A.**

**Conclusion:** Scheme B's `eq_axiom_3.tex` SHOULD be reframed as a derived theorem, not a primitive axiom. The file's "single source of truth" claim is incorrect against Vol 1 Ch 1.

### §12.3 The "SiLU" misnomer (F2 expanded)

`manuscript/ave-kb/CLAUDE.md:58` says:
> *"Axiom 4: SiLU / saturation gate (dielectric saturation)"*

`eq_axiom_4.tex:6-8` says:
```
S(A) = √(1 − (A/A_yield)²)
```

These are different functions:
- **SiLU** (Sigmoid Linear Unit, neural net activation): `f(x) = x · σ(x) = x / (1 + e^(-x))` — smooth, non-monotonic at small negative x, asymptotes to x for large positive x
- **AVE Universal Yield Kernel**: `S(A) = √(1 − A²)` — quarter circle / Born-Infeld form, monotonically decreasing, hits zero at A_yield, defined on [0, A_yield]

The corpus's actual function is more accurately called:
- **"Universal Yield Kernel"** (per `eq_axiom_4.tex:4`)
- **"Born-Infeld saturation factor"** (closest physics analog)
- **"Quarter-arc yield kernel"** (geometric description)
- **"Dielectric saturation kernel"** (descriptive, per Vol 1 Ch 1:237)

The "SiLU" label in CLAUDE.md was identified by Grant on 2026-04-20 as APU-domain accidental import; queued for correction; never fixed. This 7-day-old technical debt has propagated into:

- `research/L3_electron_soliton/35_halfcover_derivation_audit.md:514` (cited and flagged)
- `research/L3_electron_soliton/71_multi_seed_eigenmode_sweep.md:55` (used descriptively by auditor)
- `.agents/kb_audit/phase-0-axioms.md:21` (cited and flagged)
- `.agents/handoffs/L3_PHASE3_SESSION_20260420.md:434` (Grant's correction handoff)
- Auditor's user_role memory entry (line 12 — "SiLU saturation S(r)=√(1-r²)")

### §12.4 Ax 2 minor variants

While most occurrences agree on Ax 2 = TKI / [Q]≡[L] / Topo-Kinematic Isomorphism, three minor variants exist:

| Source | Ax 2 Statement |
|---|---|
| Scheme A canonical (Vol 1 Ch 1, downstream) | Topo-Kinematic Isomorphism: [Q] ≡ [L] |
| Scheme B (`eq_axiom_2.tex`) | Fine Structure (α coupling) |
| Scheme C (KB INVARIANT-S2) | Topological phase dislocation |
| Grant 2026-04-20 framing | Wave propagation, K = 2G (trace-reversed Cosserat) |
| AVE-APU `vol_1/ch03_vacuum_thermodynamics.tex:22` | "Topological scaling / losslessness" |

These are all related by the K=2G trace-reversal mechanism connecting topology to fine structure to wave propagation. **No substantive disagreement** — different aspects of the same concept emphasized.

### §12.5 Ax 4 universal agreement

Every scheme agrees Ax 4 is **Saturation** with formula `S(A) = √(1 − (A/A_yield)²)`. The only naming variations are cosmetic:
- "Dielectric Saturation" (Scheme A)
- "Universal Saturation Kernel" (Scheme B)
- "SiLU / saturation gate" (Scheme C — the SiLU label is wrong but "saturation gate" is accurate)
- "Dielectric saturation at Nyquist yield" (Grant 2026-04-20)
- "Geometric Yield" (some AVE-Metamaterials chapters)
- "Saturation Clipper" (AVE-APU operational)
- "Yield Boundary" (AVE-Fusion)

All point at the same kernel.

**A-034 (canonical 2026-05-15 evening): the cross-scale empirical confirmation.** Universal-agreement on Ax 4's kernel form has been promoted from cross-repo convention to empirically-anchored framework synthesis. The A-034 catalog enumerates **19 instances** of `S(A) = √(1 − A²)` governing topological-reorganization events spanning **21 orders of magnitude** — from atomic dielectric breakdown to cosmic K4 crystallization. Classification is 3-way: SYM (symmetric collapse, e.g. BCS), ASYM-N (asymmetric with neutral mediator, e.g. MOND), ASYM-E (asymmetric with energy-mediator, e.g. BH ring-down). Empirical anchors at four scales:
- **Atomic/condensed-matter:** BCS B_c(T) at 0.00% error (Vol 3 Ch 9)
- **Geophysical:** NOAA GOES 40-yr solar-flare validation (Vol 3 Ch 14)
- **Gravitational:** BH ring-down at 1.7% from GR exact (Vol 3 Ch 15, 3 LIGO events); Schwarzschild radius exact match
- **Cosmic:** CMB axis-alignment empirical prereg (L3 electron-soliton research dir, 2026-05-15)

The 19 catalog instances are unchanged across naming schemes (A/B/C/D) — every scheme's Ax 4 invocation now points at the same 19-instance backing. This makes Ax 4 the **most empirically-validated axiom in the corpus**.

Full catalog: [Backmatter Ch 7 — Universal Saturation-Kernel Catalog](../../backmatter/07_universal_saturation_kernel.tex). Canonical synthesis: [trampoline-framework.md §7.5](trampoline-framework.md). Vol 3 Ch 4 generative cosmology §sec:tki_strain_snap names this the "TKI strain-snap mechanism" for the cosmic-scale instance.

### §12.6 Grant's 2026-04-20 framing — fifth scheme variant

Per [`.agents/handoffs/L3_PHASE3_SESSION_20260420.md:440-443`](L3_PHASE3_SESSION_20260420.md#L440):

| # | Grant 2026-04-20 |
|---|---|
| Ax 1 | K4 diamond graph of LC cells at pitch ℓ_node |
| Ax 2 | Wave propagation, K = 2G (trace-reversed Cosserat) |
| Ax 3 | Reflection Γ at impedance boundaries |
| Ax 4 | Dielectric saturation at Nyquist yield |

This is **closest to Scheme A** but with different emphasis on each axiom:
- Ax 1: "K4 diamond graph" (specific geometry vs general LC network)
- Ax 2: "Wave propagation, K=2G" (specific mechanism vs abstract isomorphism)
- Ax 3: "Reflection Γ at boundaries" (specific operator vs abstract action principle)
- Ax 4: "Nyquist yield" (specific physical scale vs general saturation)

These are physical-mechanism framings of the same Scheme A axioms. Per Grant's authority as framework author, this framing should probably be canonical at the manuscript level too.

---

## §13 RECOMMENDATIONS

### §13.1 Immediate fixes (low cost, high impact)

**(R1) Fix the "SiLU" misnomer.** `manuscript/ave-kb/CLAUDE.md:58` should change to match Vol 1 Ch 1's "Dielectric Saturation" or `eq_axiom_4.tex`'s "Universal Yield Kernel." Same fix in research/L3_electron_soliton/71_multi_seed_eigenmode_sweep.md:55. Auditor's user_role memory entry update.

**(R2) Update `manuscript/ave-kb/CLAUDE.md` INVARIANT-S2 to Scheme A naming.** Replace APU-flavored ABCD/phase-dislocation/SiLU labels with canonical Vol 1 Ch 1 names. Document the change in INVARIANT-S2 itself (not silently overwrite).

**(R3) Annotate `manuscript/common_equations/eq_axiom_3.tex` to clarify it's a SPECIALIZED form.** Either:
- Rename file to `eq_gravity_consequence.tex` and rewrite header to clarify the gravity content is Ax 1 + Ax 4 derived consequence, OR
- Add explicit caveat in eq_axiom_3.tex header: "Note: This file uses 'Axiom 3' for the gravity refractive index. Vol 1 Ch 1 uses 'Axiom 3' for the Effective Action Principle. The gravitational refractive index is a derived consequence of Ax 1 + Ax 4 + symmetric scaling."

### §13.2 Medium-cost fixes (require manuscript revisions)

**(R4) Reconcile `eq_axiom_*.tex` numbering with Vol 1 Ch 1.** Either:
- Renumber: Ax 1=LC, Ax 2=TKI/Fine Structure, Ax 3=Effective Action, Ax 4=Saturation. Move gravity content to a separate `eq_gravity_derived.tex` file.
- OR keep current numbering but add a header note at each file explaining the numbering convention used.

**(R5) Auditor's doc 76_ revision.** [research/L3_electron_soliton/76_lattice_to_axiom3_bridge.md](../../research/L3_electron_soliton/76_lattice_to_axiom3_bridge.md) cited Scheme B's "Ax 3 = Gravity" extensively. Renumber to point at Vol 3 Ch 3's derivation chain instead.

**(R6) AVE-APU explicit Scheme C deprecation.** Document in AVE-APU CLAUDE.md or top-level README that Axiom 4 operationalization as "saturation gate" / "SiLU clipper" is APU-domain shorthand for Scheme A's Ax 4 dielectric saturation kernel. Prevents future agents from re-importing the misnomer.

### §13.3 Long-term fixes (manuscript-level)

**(R7) Single-source-of-truth axiom file.** Create `manuscript/common_equations/eq_axioms_canonical.tex` that contains all four canonical Scheme A statements in one place. All `\input{}` directives across the manuscript should point at this file. Existing eq_axiom_*.tex files become deprecated or repurposed.

**(R8) Cross-repo axiom propagation.** Each downstream repo (AVE-APU, AVE-VirtualMedia, etc.) should reference AVE-Core's canonical axiom file by URL or relative path, not duplicate the axiom listing. Reduces drift.

**(R9) Annotate Ax 3 reinterpretation patterns.** AVE-Protein's "S₁₁ minimization" framing of Ax 3 + AVE-Fusion's "mechanical impedance boundary" framing + AVE-VirtualMedia's "MoE routing as Ax 3" — all are valid Scheme A operationalizations. Document the operationalization patterns explicitly so they're not mistaken for divergent schemes.

---

## §14 STATUS OF AUDITOR'S OWN WRITINGS

Auditor's contributions to the corpus that touch axiom labeling:

**✗ doc 76_ (research/L3_electron_soliton/76_lattice_to_axiom3_bridge.md):** Cites Scheme B `eq_axiom_3.tex:Ax 3 = Gravity` as primary. **Mis-labeled per canonical Scheme A.** Needs revision per R5.

**✗ user_role memory entry (project_ave_axioms.md:12):** "SiLU saturation S(r)=√(1-r²)" — propagates the SiLU misnomer. Needs correction per R1.

**✓ research/L3_electron_soliton/71_multi_seed_eigenmode_sweep.md:55:** Used "SiLU saturation kernel" descriptively. Caught and flagged by Grant 2026-04-27. Needs correction per R1.

**✓ COLLABORATION_NOTES.md updates (Rules 6/15/16, A35-A47):** Did not propagate axiom-labeling errors. Clean.

**✓ Manual r8.7-r8.9 updates:** Did not redefine axioms; only cited per usage. Clean.

---

## §15 OPEN QUESTIONS FOR GRANT ADJUDICATION

1. **Which scheme is canonical?** The evidence strongly points at Scheme A (Vol 1 Ch 1 + 8 downstream repos). Confirming this explicitly enables the R1-R9 fixes.

2. **What's the status of `eq_axiom_*.tex`?** They claim "single source of truth" but disagree with Vol 1 Ch 1 on Ax 3. Are they:
   - (a) Engineering shorthand to be reconciled with Vol 1 Ch 1
   - (b) An older numbering that should be updated
   - (c) A specialized engineering domain (in which case the "single source of truth" claim should be removed)

3. **Should the KB INVARIANT-S2 be updated to match Vol 1 Ch 1, or should Vol 1 Ch 1 be updated to match the KB?** Per Grant 2026-04-20, the KB was wrong (APU import). Confirming this to formalize the fix direction.

4. **Auditor's doc 76_ revision approach?** Renumber Ax 3 references throughout, or annotate-and-leave with a header note pointing to canonical Scheme A?

5. **Is "SiLU" appearing in user_role memory the auditor's responsibility to fix, or should the canonical memory entry be authored by Grant?** The current memory was self-noted as "stale-memory warning corrected 2026-04-25" but still contains SiLU. Need confirmation of the authority for memory updates.

---

## §16 ARTIFACT INDEX

Cross-repo Explore-agent investigations that produced this catalog (raw outputs persisted, accessible if more detail needed):

- AVE-Core: `/Users/grantlindblom/.claude/projects/-Users-grantlindblom-AVE-staging-AVE-Core/fd67ea9e-9bcf-4584-bfad-04a6bb93c66d/tool-results/toolu_013PXfnXetM3yJAnwWwk91Zs.json` — 79 occurrences, full pedantic catalog
- AVE-APU + AVE-VirtualMedia: agent output in conversation (28 + 28 occurrences)
- AVE-HOPF + AVE-Propulsion + AVE-PONDER: `/Users/grantlindblom/.claude/projects/-Users-grantlindblom-AVE-staging-AVE-Core/fd67ea9e-9bcf-4584-bfad-04a6bb93c66d/tool-results/toolu_01GejjH2zKPSudFwy8SEH9CH.json` — 53 occurrences total
- AVE-Metamaterials + AVE-Fusion + AVE-Protein: agent output in conversation (91 + 34 + 207 = 332 occurrences)

**Total content-bearing axiom occurrences across the org: ~520**

---

*Doc written 2026-04-27 by auditor agent per Grant directive. Pedantic per request. Surfaces 4-5 distinct axiom-numbering schemes in active use; documents the canonical-vs-divergent status; flags 2-week-old technical debt (SiLU misnomer queued 2026-04-20, never fixed) plus a structural inconsistency between `eq_axiom_*.tex` "single source of truth" claim and Vol 1 Ch 1's actual axiom names; recommends 9 prioritized fixes (R1-R9). Auditor's own writings flagged for correction in §14. Open Grant adjudication questions in §15.*

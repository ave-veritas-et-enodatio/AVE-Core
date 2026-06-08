# 2026-06-07 Session Reframes → EE / Fluids / Vocab Canonical Mapping

**Author:** implementer lane (Claude Opus 4.8) · **Date:** 2026-06-07
**Branch:** `analysis/2026-06-07-session-reframes-mapping`
**Skills fired:** `ave-prereg`, `ave-ee-first-mapping`, `consistency-vs-emergence`,
`ave-evidence-framing-discipline`, `substrate-native-check`, `ave-canonical-leaf-pull`,
`ave-canonical-source`.

This doc maps six conceptual reframes that lived only in chat + the orchestration
epic (PR #120 sec14) into the canonical AVE structures. **Discipline call up front:
every reframe below is CONSISTENCY-CLASS (a re-framing / translation / lens onto
already-canonical substrate physics), NOT a new derivation. The one genuine open
derivation — the value of α — STAYS OPEN.** The EE-mapping is a framing lens, not a
derivation of α; the Golden-Torus audit + the screening-factor route are the open
tests, named below and NOT claimed as closed.

---

## §0 — ave-prereg: structures that ALREADY EXIST (do NOT create; ADD to)

The corpus already carries canonical homes for all six reframes. Nothing here is
green-field; the work is consolidation + classification + ONE flagged tension.

| Target structure | Canonical home (EXISTS) | What it already carries |
|---|---|---|
| AVE↔EE translation | [`manuscript/ave-kb/common/translation-tables/translation-circuit.md`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md) | §1 ξ_topo identity (L=μ₀, C=ε₀, R=η/loss); §4 catalog (c₀, Z₀, α=Q-factor rows); §4.5 EE-tool tracker (FOC/Park row); §6 means-test corpus |
| Constants (two wave speeds, operating-point) | INVARIANT-S2 in [`manuscript/ave-kb/CLAUDE.md`](../manuscript/ave-kb/CLAUDE.md); [`manuscript/common_equations/eq_calibration_constants.tex`](../manuscript/common_equations/eq_calibration_constants.tex) | c_EM=c₀/S, c_shear=c₀√S; "calibration constants are DERIVED from axioms, not axioms themselves" |
| Lorentz = emergent | [`…/preferred-frame-and-emergent-lorentz.md`](../manuscript/ave-kb/vol1/dynamics/ch4-continuum-electrodynamics/preferred-frame-and-emergent-lorentz.md) (clm-yr6tu4/ce8dg1) | "Strict Lorentz invariance at observable scales is an EMERGENT consequence of K4 cubic symmetry, not an axiom" |
| α as cold-lattice Q-factor | [`…/theorem-3-1-q-factor.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md) | α⁻¹ = Q_tank = 4π³+π²+π (cold-lattice value) |
| Loss tangent (tan δ) | [`…/temporal-saturation-regime-classifier.md`](../manuscript/ave-kb/common/temporal-saturation-regime-classifier.md) | substrate-native loss tangent δ_AVE; tan δ = σ/(ωε) |
| Spinor double-cover / Cosserat spin | [`…/spin-half-paradox.md`](../manuscript/ave-kb/vol2/appendices/app-b-paradoxes/spin-half-paradox.md) :12-14 | Finkelstein-Misner kink / Dirac belt trick; Cosserat microrotation DOF IS spin origin |
| FOC / Park (d/q) | [`manuscript/backmatter/05_universal_solver_toolchain.tex`](../manuscript/backmatter/05_universal_solver_toolchain.tex) :120-136 (d/q), :401 (pole-pairs ↔ mode ℓ) | Park transform ≡ co-rotating-frame decomposition; pole pairs row |
| Glossary / vocab | [`docs/glossary.md`](../docs/glossary.md) | substrate-native vs EE/ME projection table; §1.6 lattice/crystal/phases |
| AVE↔fluids | [`research/2026-06-07_entrainment-vortex-trapping-deep-dive.md`](2026-06-07_entrainment-vortex-trapping-deep-dive.md); [`manuscript/common/translation_fluidics.tex`](../manuscript/common/translation_fluidics.tex) | Camassa-McLaughlin trap→genesis (§2), entrainment→dark-wake (§3), stratification→A₀(r) (§4) |
| Water / z=4 | [`…/water-anomaly-lc-partition.md`](../manuscript/ave-kb/vol3/condensed-matter/ch11-thermodynamics/water-anomaly-lc-partition.md) :36 | "z=4 represents the tetrahedral network symmetry"; tetrahedral diamond-like State-I |

**Created NEW (only):** this summary doc + a new §10 in `translation-circuit.md` + a
new §1.7 vocab subsection in `docs/glossary.md` + a new §8 in the entrainment doc.
No new claim-quality IDs minted; all KB additions tag under the existing
`clm-eemap1` (EE-as-substrate-native META framework).

---

## §1 — The six reframes, mapped + classified

### Reframe 1 — Constants are transmission-line properties, not fundamental

**Statement.** The AVE vacuum IS a K4-TLM transmission-line network. The "fundamental
constants" are EE properties of that line: c = line velocity (1/√(μ₀ε₀); operating-point
dependent — c_EM = c₀/S, c_shear = c₀√S); Z₀ = characteristic impedance (√(μ₀/ε₀));
α = the line coupling/loss; L = μ₀, C = ε₀, R = loss. Lorentz invariance (c constant)
is EMERGENT — the cold-lattice limit S→1.

**Classification:** CONSISTENCY-CLASS lens over identities (Class A) + one Class-B
manifestation.
- c₀ = 1/√(μ₀ε₀), Z₀ = √(μ₀/ε₀): **Class A identity** (translation-circuit.md §6 #2,#3;
  0.00% by definition — not predictions).
- L↔μ₀ (mass↔inductance), C↔ε₀ (compliance↔capacitance), R↔η (resistance↔viscosity/loss):
  **Class A identity** via the ξ_topo six-row table (translation-circuit.md §1).
- Operating-point dependence c_EM = c₀/S, c_shear = c₀√S: already canonical (INVARIANT-S2).
- "c constant ⇒ Lorentz invariance is EMERGENT (cold-lattice S→1)": **Class B axiom-
  manifestation**, already a canonical leaf (preferred-frame-and-emergent-lorentz.md) —
  Lorentz isotropy emerges from K4 cubic symmetry, anisotropy suppressed (qℓ_node)⁴.

**Landed:** translation-circuit.md §10.1 (consolidation row + Lorentz-emergent cross-ref).

### Reframe 2 — α = the screened effective precession angle

**Statement.** α is the electron's per-orbit spin-slip (the g−2 anomaly direction); its
VALUE 1/137 is the *screened effective* coupling — the bare coupling reduced by the
lattice dielectric/chiral SCREENING (S(A), Δc_crit) down to the low-energy residual
(the running of α). The screening is what explains the SMALLNESS.

**Classification:** CONSISTENCY-CLASS framing; **α-DERIVATION OPEN — do NOT claim α is
derived.** The cold-lattice value α⁻¹ = 4π³+π²+π is a geometric Q-factor result
(Theorem 3.1, structural), but the *screening-explains-smallness* story is a LENS, not a
closed derivation. Per the honest-α Class-B verdict (clm-0ktpcn, 2026-06-02): the
substrate does NOT independently select the value. **Open tests named:**
- the **Golden-Torus audit** (the S₁₁-minimum geometry route);
- the **screening-factor route** (bare → screened residual via S(A)/Δc_crit).

**Landed:** translation-circuit.md §10.2 (framed explicitly as OPEN; no derivation claim).

### Reframe 3 — α = 1/Q = tan δ = the loss tangent / slip angle (~0.42°)

**Statement.** α is the line's loss tangent: α = Q⁻¹ = tan δ ≈ 1/137, i.e. a slip
angle δ ≈ arctan(1/137.036) ≈ 0.418°.

**Classification:** **Class A / EE-identity** (consistency-class). Given the canonical
identification Q_tank = α⁻¹ (Theorem 3.1) and the canonical substrate loss tangent
δ_AVE (temporal-saturation-regime-classifier.md), α = 1/Q = tan δ is definitional once
Q = α⁻¹ is accepted. The numeric slip angle arctan(α) ≈ 0.418° is an EE re-expression,
NOT an independent prediction. Consistent with the honest-α Class-B verdict: the IDENTITY
is definitional; the VALUE stays open (Reframe 2).

**Landed:** translation-circuit.md §10.3 + means-test note.

### Reframe 4 — FOC: the electron is a self-commutating 3-phase machine

**Statement.** Field-Oriented-Control (Park d/q) maps onto the electron rotor. The
"½ phase-pair commutation" is the SPINOR DOUBLE-COVER (Finkelstein-Misner / Dirac belt
trick — SU(2)→SO(3) 2:1), NOT a half-pole-pair machine. The pole-pairs are the (2,3)
WINDING numbers (already canonical: toolchain :401 pole-pairs row; translation-circuit.md
§4 (2,3) Clifford-torus row). The electron is SELF-COMMUTATING: the Compton-clock spinor
rotation IS the de Broglie propagation drive. **g = 2 is POSITED, not derived.**

**Classification:** CONSISTENCY-CLASS structural isomorphism (Class B manifestation for
the Cosserat-spin part, already canonical at spin-half-paradox.md:14; the FOC/Park
mapping is structural). g=2 honest-tagged as posited.

**Landed:** translation-circuit.md §10.4 (FOC self-commutation; cross-ref toolchain
:129-130,:401 + spin-half-paradox.md + §4 (2,3) row) + §4.5(c) FOC tracker row note.

### Reframe 5 — Water: z=4 ACHIRAL diamond substrate; chirality = Cosserat microrotation

**Statement.** The substrate is a z=4 tetrahedral (diamond-like) network; spin/chirality
is the COSSERAT MICROROTATION, NOT net bond-graph chirality. Water is a tetrahedral fluid
that crystallizes (latent-heat homeostasis, constant density) — a material-scale
confirmation of the z=4 tetrahedral substrate motif.

**Classification:** z=4 tetrahedral = **Class B manifestation, ALREADY canonical**
(water-anomaly-lc-partition.md:36 "z=4 represents the tetrahedral network symmetry";
glossary §1.6 tetrahedral diamond-like). Cosserat-microrotation-as-spin-origin = **already
canonical** (Axiom 1; spin-half-paradox.md:14). **The achiral-vs-chiral half of the reframe
is a FLAGGED TENSION — see §2. NOT silently landed.**

### Reframe 6 — Paper #4 (Camassa-McLaughlin vortex-ring) genesis extension

**Statement.** Electron genesis = vortex-ring-TRAP (paper #4) + FREEZE-IN (water
crystallization) → the electron soliton. The parametric threshold = the trap. Entrainment
= the dark-wake (near-field mass + far-field loss). Fission = decay/shower.

**Classification:** CONSISTENCY-CLASS guided-analogy (the entrainment doc is itself
tagged consistency/guided-analogy). Each leg is a LENS:
- trap → genesis confinement: already mapped (entrainment doc §2);
- freeze-in → water crystallization: ties to water-anomaly-lc-partition.md (Axiom-4 yield,
  √(1−A²) kernel — the SAME first-order crystallization mechanism class);
- entrainment → dark-wake split (near-field mass Σ_near + far-field loss τ^far_zx):
  already canonical (translation-circuit.md §4 dark-wake / dark-resonance rows);
- fission → decay/shower: lens, not derived.

**Landed:** entrainment-vortex-trapping-deep-dive.md §8 (consolidated genesis-extension
mapping table).

---

## §2 — FLAGGED TENSION (flag-don't-fix; for Grant adjudication)

Reframe 5 says the substrate is **z=4 ACHIRAL diamond** with chirality living only in the
Cosserat microrotation sector ("NOT net chirality"). This sits in tension with the
canonical Axiom-1 wording. I am NOT resolving it — surfacing both verbatim, per
flag-don't-fix + the missing-axiom-vs-engine-bug discipline (do not draft a new axiom or
silently rewrite Axiom 1).

- **Axiom 1 (CHIRAL):** INVARIANT-S2, `manuscript/ave-kb/CLAUDE.md` — *"vacuum is a 3D
  **chiral** Laves K4 Cosserat crystal 𝓜_A … I4₁32 **chiral** space group."*
- **Preferred-frame leaf (ACHIRAL diamond-cubic):**
  `preferred-frame-and-emergent-lorentz.md` — *"The diamond-cubic (**Fd-3m**) symmetry of
  the K4-bipartite tetrahedral lattice suppresses observable anisotropy…"*
- Reframe 5: substrate is **z=4 achiral diamond**; chirality = Cosserat microrotation,
  not net chirality.

`Fd-3m` (diamond-cubic, used in the Lorentz leaf) is **achiral**; `I4₁32` (Axiom 1) is a
**chiral** space group. These are two different space groups already coexisting in the
corpus. Reframe 5 lands squarely on this pre-existing tension and offers a candidate
reconciliation: the bond-graph connectivity is tetrahedral/achiral (z=4, diamond-like),
and the chirality is carried by the Cosserat micropolar (microrotation) sector, not by a
chiral bond arrangement. **This is a framing-level substrate-topology question — it is
Grant's call, not the implementer's.** No edit to Axiom 1 or to any lattice leaf has been
made. Surfaced to the auditor/Grant queue.

---

## §3 — Confirmation: α-derivation NOT over-claimed

Stated explicitly for the audit trail:
- The cold-lattice α⁻¹ = 4π³+π²+π is a **geometric Q-factor result** (Theorem 3.1),
  classified structural; it is NOT re-claimed as a from-scratch value-derivation here.
- The screening / running-of-α / "smallness explained" story (Reframe 2) is a **LENS**,
  flagged OPEN, with the Golden-Torus audit + screening-factor route named as the open
  tests.
- α = 1/Q = tan δ (Reframe 3) is an **EE IDENTITY** given Q = α⁻¹; the numeric value
  (1/137, slip angle 0.418°) is NOT independently predicted by it.
- This is consistent with the standing honest-α **Class-B** verdict (the substrate does
  NOT independently select α's value). Nothing here promotes α to Class-2 emergence.

---

## §4 — Skill-application ledger

| Skill | Where applied |
|---|---|
| `ave-prereg` | §0 — located every existing structure before editing; no green-field |
| `ave-ee-first-mapping` | Reframes 1–4 routed through the EE-as-substrate-native META leaf; new rows landed per Step 6 |
| `consistency-vs-emergence` | Every reframe tagged (Class A identity / Class B manifestation / consistency lens); α kept OPEN per Step 8c canonical-ceiling-stays-Class-B |
| `ave-evidence-framing-discipline` | No over-claims: α OPEN, g=2 POSITED, slip-angle = re-expression not prediction |
| `substrate-native-check` | Reframe 5/6 — tetrahedral/Cosserat structure walked; achiral tension surfaced not resolved |
| `ave-canonical-leaf-pull` | Found preferred-frame-and-emergent-lorentz, temporal-saturation-regime-classifier, spin-half-paradox, water-anomaly leaves before deriving |
| `ave-canonical-source` | c₀/Z₀/α treated as derived-from-axioms calibration constants, not hard-coded |

---

## §5 — Surfaced for the auditor / Grant queue (I surface; the auditor lands)

1. The **achiral-diamond vs chiral-Laves** tension (§2) — needs Grant adjudication; may
   warrant a reconciliation note in Axiom 1 / the preferred-frame leaf, OR a correction to
   one of them. Implementer did NOT touch Axiom 1.
2. Reframe 2's α-screening route — candidate to open a tracked derivation question
   (Golden-Torus audit + screening-factor) if Grant wants it pursued; currently OPEN/lens.
3. The translation-circuit.md §10 additions are tagged `clm-eemap1` (consistency-class) —
   auditor to confirm classification ceiling stays Class B (no Class-2 promotion).

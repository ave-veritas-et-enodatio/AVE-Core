# Pre-registration — clm-zuf7g1 Phase 3a: Z₀ ≈ 377 Ω substrate-mechanism derivation

**Workstream**: clm-zuf7g1 strengthening epic Phase 3a (substrate-impedance Z₀ structural identification)
**Epic doc**: [`_orchestration/clm-zuf7g1-strengthen.md`](../_orchestration/clm-zuf7g1-strengthen.md) §"Phase 3a prereg — lossless-LC-resonator Z₀ structural identification"
**Date**: 2026-05-26
**Branch**: `analysis/clm-zuf7g1-phase-3a-Z0-derivation` off `main` @ `cf3c913e`
**Implementor**: AVE-Core implementor session (worktree-isolated spawn)

## Scope

Phase 3a addresses the one remaining open derivation-gap strengthen-by item on clm-zuf7g1 (CHSH Violation $|S|_{\max} = 2\sqrt{2}$, current confidence 0.65 / solidity 0.65):

> Derive the structural identification "phase-locked topological thread = lossless short-short LC resonator with $Z_0 \approx 377\,\Omega$, $Q = \infty$" from first principles (currently asserted as a constructive identification of the Bell-correlation carrier).

This Phase 3a focuses on the Z₀ ≈ 377 Ω substrate-impedance derivation only. Q = ∞ (topological dissipationless invariant) is Phase 3b, separate workstream. The "phase-locked thread mode inherits substrate Z by lattice-continuity" step is the load-bearing structural identification connecting the substrate impedance to the topological-thread mode; whether that step is the gap, or the gap is in the Z₀ derivation itself, is the RESCOPE question this prereg surfaces.

## Pre-survey corpus state (ave-prereg discipline; ave-canonical-leaf-pull discipline)

**Skill firings before any derivation work**:

1. `ave-prereg` — pre-derivation corpus-grep across `manuscript/ave-kb/`, `src/ave/core/`, `research/`
2. `ave-canonical-leaf-pull` — pulled Z₀-named leaves + clm-zuf7g1 leaf + Vol 4 ch1 substrate-circuit-theory
3. `ave-canonical-source` — checked `src/ave/core/constants.py` for canonical Z₀ definition site
4. `verify-before-cite` — every file:line citation below grep-verified live during prereg drafting
5. `consistency-vs-emergence` v1.2 — dual-axis classification machinery loaded (substrate-mechanism axis + observable axis)
6. `phase-space-coordinate-check` — substrate-impedance Z₀ lives in V/I phasor (impedance-plane); topological-thread mode is real-space lattice-defect on the K4 graph — coordinate-system check at derivation time
7. `substrate-native-check` — K4-TLM lattice structure walk (Ax 1 chiral Laves K4 Cosserat crystal; LC-tank-per-node; bond-coupling-between-nodes)
8. `ave-analytical-tool-selection` — substrate-impedance / boundary-impedance problem class
9. `ave-discipline-translate` v1.1 trigger 6 — substrate-native prose vocabulary mandated (substrate-impedance Z₀ is primary; "Maxwell vacuum impedance" appears only as parenthetical translation)
10. `ave-discrimination-check` — Class 2 substrate-mechanism emergence vs Class 4 substrate-agnostic consistency BEFORE asserting solidity lift
11. `ave-evidence-framing-discipline` — "derives from substrate primitives" vs "identifies with standard-physics name" vs "consistent-with continuum-limit value" precision check

### Already-canonical Z₀ corpus state (load-bearing for adjudication)

**A. The Z₀ derivation already has a canonical leaf**: [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md) (clm-i9l284 + clm-kezk9z).

The chain stated there:

> **Per-Cell Lumped Elements** (lines 18–20):
> $L_{\text{cell}} = \mu_0\, \ell_{\text{node}}, \qquad C_{\text{cell}} = \epsilon_0\, \ell_{\text{node}}$
>
> **Scale-Invariant Characteristic Impedance** (lines 36–38):
> $Z_{\text{cell}} = \sqrt{L_{\text{cell}}/C_{\text{cell}}} = \sqrt{\mu_0 \ell_{\text{node}} / (\epsilon_0 \ell_{\text{node}})} = \sqrt{\mu_0/\epsilon_0} \equiv Z_0 \approx 376.73\;\Omega$
>
> "The lattice pitch cancels identically. This is the fundamental reason $Z_0$ is a universal constant: it is a property of the node-to-node impedance ratio of the lattice, independent of the absolute scale $\ell_{\text{node}}$."

**B. The substrate-impedance Z₀ has an explicit existing dual-leaf classification**:

[`manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) (clm-nxc9gy + clm-k6quve) lines 11, 44–50:

> "Numerical equality of $Z_{\text{cell}} = Z_0$ is from cancellation of $\ell_{\text{node}}$; conceptual distinction matters for engine implementation and dimensional analysis."
>
> "NUMERICALLY equal to classical $Z_0$ because the lattice pitch $\ell_{\text{node}}$ cancels (appears in both $L_{\text{cell}}$ and $C_{\text{cell}}$); CONCEPTUALLY distinct because $Z_{\text{cell}}$ refers to a physical bond, $Z_0$ refers to a continuum field ratio. The numerical equality is the substrate's signature of being 'internally consistent at every scale' — Axiom 2 (TKI) scale invariance."

**C. The substrate-impedance Z₀ is canonically classified as Class A identity in the existing claim-quality entry**:

[`manuscript/ave-kb/vol4/claim-quality.md`](../manuscript/ave-kb/vol4/claim-quality.md) clm-kezk9z (line 104):

> "Per Master Prediction Table classification, $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ is a category (i) identity — definitionally true (the 0.00% in row #2 of the prediction table is not a fit)."

And clm-kezk9z rationale (line 118):

> "the leaf is honest that the $Z_0$ identity carries zero predictive content."

**D. The engine canonical-source defines Z₀ by SI substitution**:

[`src/ave/core/constants.py`](../src/ave/core/constants.py):
- Line 78: `C_0: float = 299_792_458.0  # Speed of light [m/s]` (SI exact)
- Line 79: `MU_0: float = 4.0 * pi * 1e-7  # Vacuum permeability [H/m]` (SI definitional, pre-2019; held as code-level constant)
- Line 80: `EPSILON_0: float = 1.0 / (MU_0 * C_0**2)  # Vacuum permittivity [F/m]`
- Line 81: `Z_0: float = np.sqrt(MU_0 / EPSILON_0)  # Characteristic impedance [Ω] ≈ 376.73`

`MU_0` and `EPSILON_0` are taken as SI/CODATA primitives; `Z_0` is derived from them via SI substitution. **The value 376.73 Ω is entirely fixed by μ₀ and ε₀ as engineering input, not by K4-TLM lattice parameters.**

**E. Vol 1 Ch 1 axiom-definitions explicitly lists Z₀ as a derived calibration constant, not an axiom**:

[`manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md) line 14:

> "The numerical calibration constants ($\ell_{node}$, $Z_0$, $\alpha$, $\xi_{topo}$, $V_{snap}$, $V_{yield}$, $G$) are *derived* from these axioms — they are not themselves axioms."

But the only existing derivation of the *numerical value* 376.73 Ω is via μ₀/ε₀ (z0-derivation.md). The lattice-pitch-cancellation argument shows the value is *scale-invariant*; it does not produce the numerical value from K4-TLM lattice primitives independent of μ₀ and ε₀.

**F. The translation-stochastics row already names the substrate-native term**:

[`manuscript/ave-kb/common/translation-tables/translation-stochastics.md`](../manuscript/ave-kb/common/translation-tables/translation-stochastics.md) line 24 (Nyquist row):

> "$\langle V^2_{vac}(f)\rangle = 4 k_B T Z_0 \Delta f$ at the substrate's characteristic impedance $Z_0 = \sqrt{\mu_0/\varepsilon_0} \approx 376.73$ Ω"

Substrate-native vocabulary already established: "substrate-impedance Z₀" / "substrate's characteristic impedance" is the canonical prose form; "Maxwell vacuum impedance" is a parenthetical translation.

## What I expect to find (forward pre-registration, per ave-prereg discipline)

### Dual-axis classification before deriving (consistency-vs-emergence v1.2 Step 7)

**Substrate-mechanism axis**: trace the master-equation-derivation-path for "AVE's Z₀ ≈ 377 Ω is a substrate-mechanism consequence of K4-TLM lattice primitives."

Candidate derivation chain, step by step:

| Step | Content | Status (pre-derivation expectation) |
|---|---|---|
| 1 | Axiom 1: chiral Laves K4 Cosserat crystal with per-node LC tank | Derived-from-master-eq (canonical Vol 1 Ch 1 axiom-definitions) |
| 2 | Ax 1 specialization: each K4 bond carries distributed inductance $L_{\text{cell}}$ and node-capacitance $C_{\text{cell}}$ per unit length | Derived-from-master-eq (canonical z0-derivation.md §1) IF $L_{\text{cell}} = \mu_0\,\ell_{\text{node}}$ and $C_{\text{cell}} = \epsilon_0\,\ell_{\text{node}}$ are themselves derived from substrate primitives; **REQUIRES-ADDITIONAL-POSTULATE if μ₀ and ε₀ are taken as SI engineering inputs** (which they are in constants.py) |
| 3 | Characteristic impedance of each lattice bond: $Z_{\text{bond}} = \sqrt{L_{\text{cell}}/C_{\text{cell}}}$ | Definitional-given-prior-steps (transmission-line characteristic impedance formula applies to any LC ladder) |
| 4 | Substitute step 2 into step 3: $Z_{\text{bond}} = \sqrt{\mu_0/\epsilon_0}$; lattice pitch $\ell_{\text{node}}$ cancels | Definitional-given-prior-steps |
| 5 | Numerical value: 376.73 Ω | Definitional-given-prior-steps once μ₀ and ε₀ are pinned; **value comes from μ₀ and ε₀ as inputs, not from substrate primitives** |
| 6 | Topological-thread mode inherits substrate-impedance Z₀ by lattice-continuity (the thread is a bound mode on the K4 lattice, its mode-impedance equals the lattice transverse-mode eigenvalue) | Likely needs to be made explicit — this is the structural identification step asserted in phase-locked-topological-thread.md line 27 without derivation |

**Pre-derivation expectation about substrate-mechanism axis**: Step 2's status decides the outcome. If μ₀ and ε₀ can be derived from K4-TLM lattice primitives (per-node geometric capacitance + per-bond geometric inductance produced by lattice geometry alone, independent of SI), the chain earns Class 2 substrate-mechanism emergence. If μ₀ and ε₀ are taken as engineering inputs (constants.py confirms they are), the chain reduces to "Class A identity once μ₀ and ε₀ are stipulated; scale-invariance under ℓ_node is the substrate-mechanism content, value is not."

**Observable axis**: AVE's Z₀ derivation predicts numerical value 376.73 Ω which exactly matches standard-physics Maxwell vacuum impedance. No experimentally distinguishable behavior vs standard physics in the canonical regime. → Class 4 consistency on observable axis.

### Expected dual-axis outcome (pre-derivation honest estimate)

**Most likely** (≥ 80% probability based on corpus pre-survey): **Class B substrate-mechanism manifestation + Class 4 observable consistency**. The substrate-mechanism content is real (scale-invariance under ℓ_node cancellation is a substrate-distinct structural claim) but it doesn't *produce the numerical value* from substrate primitives — μ₀ and ε₀ are taken as SI inputs at step 2. The value 376.73 Ω comes from μ₀ and ε₀, not from K4-TLM lattice geometry.

**Less likely** (≤ 20% probability): **Class 2 substrate-mechanism emergence + Class 4 observable consistency**. This requires that μ₀ and ε₀ themselves derive from substrate primitives — i.e., there exists a substrate-mechanical derivation of $\mu_0 = 4\pi \times 10^{-7}$ H/m and $\epsilon_0 = 1/(\mu_0 c^2)$ from K4-TLM lattice geometry independent of SI. The corpus pre-survey did NOT surface such a derivation; both μ₀ and ε₀ are SI/CODATA primitives in `src/ave/core/constants.py`. If a separate substrate-mechanism derivation of μ₀ from substrate primitives exists elsewhere in corpus and I missed it during pre-survey, the chain closes Class 2.

### Pre-registered adjudication criteria (verbatim from epic brief)

- **PASS** (≤ 20% pre-survey probability): Z₀ derivation closes Class 2 substrate-mechanism emergence end-to-end with no circularity, KB integration clean. Solidity-lift target: clm-zuf7g1 0.65 → 0.70.

- **WALK-BACK** (≥ 60% pre-survey probability): derivation bottoms out in Class B substrate-mechanism manifestation + Class 4 observable consistency. The scale-invariance argument is genuine substrate-distinct content but doesn't lift to substrate-mechanism emergence of the numerical value. Document honestly per `ave-walk-back` v1.1 Type B propagation; no solidity lift; refine Phase 3 scope by surfacing Q-LCR-1.
  - **Q-LCR-1**: Is the substrate-impedance Z₀ numerical value derivable as substrate-mechanism emergence from Ax 1 + Ax 2 lattice parameters (per-bond geometric inductance + per-node geometric capacitance from K4 geometry alone), or is it definitionally fixed by the μ₀/ε₀ canonical-source link to standard continuum-electrodynamics values?

- **RESCOPE** (≤ 20% pre-survey probability): gap is not in the Z₀ derivation itself but in the "topological-thread mode inherits substrate-impedance Z by lattice-continuity" step. Spin out as separate Phase 3a-mode workstream; Z₀-from-Ax 1 + Ax 2 lands as a leaf-completion via the existing z0-derivation.md anchor.

### What would discriminate (per ave-discrimination-check)

For Phase 3a to land as **PASS** (Class 2 substrate-mechanism emergence), the derivation must:

1. **Produce 376.73 Ω from K4-TLM lattice primitives WITHOUT inputting μ₀ or ε₀ as SI engineering values.** This means: derive μ₀ and ε₀ themselves from substrate-mechanical content (e.g., per-node geometric capacitance from chiral Laves K4 unit-cell geometry; per-bond geometric inductance from K4 bond-length × topological flux quantum). The value 376.73 Ω must come out independently, and *then* be compared with the SI value, NOT be derived BY substituting μ₀ and ε₀ values.

2. **Show that the topological-thread mode's characteristic impedance Z equals the substrate-impedance Z₀ by lattice-eigenvalue continuity, NOT by tuned external coupling.** The thread is a bound mode on the K4 lattice; its mode-impedance comes from the same K4 lattice that supports Z₀ transverse modes, so the values must equal by substrate-eigenvalue structure, not by accident.

3. **Master-equation-derivation-path: every step traces to derived-from-master-eq or definitional-given-prior-steps. NO step labeled requires-additional-postulate.** If μ₀ or ε₀ remain as additional postulates, Step 2 above is requires-additional-postulate and the chain closes Class B at best.

For **WALK-BACK** outcome, the honest finding is: the scale-invariance under ℓ_node cancellation is genuine substrate-mechanical content (the substrate's K4-TLM topology DOES produce a characteristic impedance that is universal across the lattice, AND the value of that impedance is invariant under coarse-graining of the lattice pitch). But the *numerical value* 376.73 Ω is set by μ₀ and ε₀ as inputs at step 2, not by lattice geometry. So the substrate-mechanism axis lifts only partially: AVE-distinct claim is "Z₀ is scale-invariant under ℓ_node by Ax 2 TKI"; AVE-non-distinct claim is "the value of Z₀ is 376.73 Ω."

For **RESCOPE** outcome, the honest finding is: Z₀-from-Ax 1 + Ax 2 is *already* canonically derived (with the Class B caveats above) in vol4/z0-derivation.md, and what's actually missing on the clm-zuf7g1 side is the topological-thread mode inheritance step. The leaf-completion is small; the structural-identification work is separate.

## Skills compliance check (implementor session kickoff, already partial)

- [x] `ave-prereg` — pre-derivation corpus-grep complete; canonical leaves identified above
- [x] `ave-canonical-leaf-pull` — vol4/z0-derivation.md + vol1/lattice-impedance-decomposition.md + vol1/impedance-operator.md + clm-zuf7g1 entry + clm-kezk9z + clm-i9l284 + clm-nxc9gy entries all pulled
- [x] `ave-canonical-source` — `src/ave/core/constants.py` Z_0 definition site identified at line 81; MU_0 and EPSILON_0 at lines 79–80 confirmed as SI engineering inputs
- [x] `verify-before-cite` — every file:line citation in this prereg grep-verified live during drafting
- [ ] `consistency-vs-emergence` v1.2 — dual-axis classification applied during derivation (substrate-mechanism axis via master-equation-derivation-path tracing; observable axis via experimentally-distinguishable-from-standard-X check). Pre-derivation expectation documented above.
- [ ] `phase-space-coordinate-check` — substrate-impedance Z₀ lives in impedance-plane (V/I phasor coordinates); topological-thread mode lives in real-space lattice. Coordinate-system check at derivation time when bridging via the lattice-eigenvalue continuity argument.
- [ ] `substrate-native-check` — K4-TLM lattice walk (Ax 1 chiral Laves K4 + LC tank per node + bond coupling between nodes) BEFORE deriving the Z_bond = √(L_cell/C_cell) chain.
- [ ] `ave-analytical-tool-selection` — substrate-impedance / boundary-impedance problem class; Op4 boundary-impedance + Op17 mode-matching candidate tools per epic brief.
- [ ] `ave-discipline-translate` v1.1 trigger 6 — substrate-native prose vocabulary enforced during result-doc composition; "Maxwell vacuum impedance" appears only as parenthetical translation reference to substrate-impedance Z₀.
- [ ] `ave-discrimination-check` — Class 2 vs Class B vs Class 4 discrimination BEFORE asserting solidity lift.
- [ ] `ave-evidence-framing-discipline` — "derives from substrate primitives" vs "identifies with standard-physics name" vs "scale-invariant under lattice pitch but value comes from SI inputs" precision in result framing.
- [ ] `ave-walk-back` v1.1 — if WALK-BACK outcome adjudicated, Type B propagation checklist applied (low-impact for this case since strengthen-by item retires rather than a Predictions matrix row).

## Falsifiable expectations registered before deriving

If a PASS chain exists, it must satisfy:

1. **Derivation of μ₀ from K4-TLM lattice geometry without SI input.** I expect to find this in corpus; pre-survey did NOT surface it. If grep on `\\mu_0\\b.*derive\\|derive.*\\mu_0\\|per-bond inductance.*K4` across corpus returns a canonical leaf I missed, that's the closure path. If not, the chain bottoms out at Class B.

2. **Derivation of ε₀ from K4-TLM lattice geometry without SI input.** Same as above for ε₀.

3. **A canonical leaf or research-tier doc somewhere asserting μ₀ and ε₀ are themselves derived from lattice primitives.** If absent, Class 2 closure is not available in current corpus.

If the chain CANNOT be closed at Class 2 (because μ₀ and ε₀ remain SI inputs), I will document the finding as WALK-BACK and surface Q-LCR-1 as a separate research question for Grant adjudication, NOT attempt to derive μ₀ and ε₀ post-hoc to rescue the PASS classification (Rule 11 honest closure; Rule 12 substitution-not-retraction).

## Branch + deliverables

**Branch**: `analysis/clm-zuf7g1-phase-3a-Z0-derivation` off `main` @ `cf3c913e`. Push branch, do not merge — orchestration session merges via `--no-ff` + audit-tag.

**Expected deliverables**:

1. This prereg doc (pre-derivation discipline lock-in)
2. Result doc at `research/2026-05-26_clm-zuf7g1-phase-3a-Z0-derivation-result.md` — derivation chain with explicit master-equation-derivation-path tracing, dual-axis classification, adjudication
3. KB integration only if PASS — update `phase-locked-topological-thread.md` and bump clm-zuf7g1 confidence 0.65 → 0.70
4. Auditor pass via `ave-auditor` BEFORE finalizing result doc and BEFORE push
5. Commit messages following project pattern (audit + what + why + follow-up queued + Co-Authored-By footer)

## Cross-references

- **Epic doc**: [`_orchestration/clm-zuf7g1-strengthen.md`](../_orchestration/clm-zuf7g1-strengthen.md) Phase 3a section
- **Target claim**: [`manuscript/ave-kb/vol1/claim-quality.md`](../manuscript/ave-kb/vol1/claim-quality.md) clm-zuf7g1 (line 337)
- **Phase-locked thread leaf** (current home of the constructive identification): [`manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md`](../manuscript/ave-kb/vol1/dynamics/ch3-quantum-signal-dynamics/phase-locked-topological-thread.md) (line 27)
- **Z₀ canonical derivation leaf**: [`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md`](../manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/z0-derivation.md) (clm-i9l284 + clm-kezk9z)
- **Lattice impedance decomposition leaf**: [`manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) (clm-nxc9gy + clm-k6quve)
- **Universal impedance operator leaf**: [`manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/impedance-operator.md`](../manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/impedance-operator.md) (clm-gdd70j)
- **Engine canonical source**: [`src/ave/core/constants.py`](../src/ave/core/constants.py) lines 78–81
- **Translation reference (substrate-native vocabulary)**: [`manuscript/ave-kb/common/translation-tables/translation-stochastics.md`](../manuscript/ave-kb/common/translation-tables/translation-stochastics.md) (Nyquist row line 24) + [`translation-circuit.md`](../manuscript/ave-kb/common/translation-tables/translation-circuit.md)
- **Discipline anchors**: `consistency-vs-emergence` v1.2 (dual-axis classification); `ave-discipline-translate` v1.1 trigger 6 (substrate-native vocabulary); `ave-walk-back` v1.1 Type B (if WALK-BACK adjudicated)

# clm-0ktpcn Phase 3-A2 — Schur Orthogonality (Sum-Decomposition Functional-Orthogonality) — Pre-Registration

**Date**: 2026-05-26
**Branch**: `analysis/clm-0ktpcn-phase-3-A2-schur-orthogonality` off `main` @ `453c335e` (post combined merges + ax4-saturation epic update)
**Epic**: `_orchestration/clm-0ktpcn-golden-torus-alpha-strengthen.md`, Phase 3a-A2 brief (implementor sub-agent B — standalone, parallel-safe)
**Scope-class**: green-field derivation attempt; honest-closure probability ~40% PASS / ~60% WALK-BACK per epic brief

---

## What is the deliverable?

A pre-registered attempt at establishing **functional orthogonality** of the three-regime sum-decomposition

$$
\alpha^{-1}_{\text{ideal}} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}} = 4\pi^3 + \pi^2 + \pi
$$

via Schur orthogonality of irreducible representations of the substrate's symmetry group, or via an alternative orthogonal-basis argument that vindicates the additive (no-cross-term) assembly without resorting to "obvious" / "by inspection".

The work product is one of three outcomes per the epic brief adjudication criteria:

- **PASS** — Schur (or alternative) derives the additive assembly rigorously; close strengthen-by item; bump confidence 0.60 → 0.65; potentially originate a new canonical leaf.
- **WALK-BACK** — Schur orthogonality not derivable from substrate primitives; reframe chapter prose to label the additive assembly as a *substrate-mechanism manifestation pointing at the standard-physics target* (Class B / Class 4) rather than rigorously derived; confidence stays at 0.60.
- **RESCOPE** — derivation gets stuck on identifying the load-bearing substrate symmetry group (or its action on the relevant mode space); spin out a sub-prereg.

---

## Pre-survey corpus-grep findings (`ave-prereg`)

Surveyed `manuscript/ave-kb/`, `research/`, `research/_archive/L3_electron_soliton/` for Schur / Peter-Weyl / orthogonality / representation-theory work. Key findings:

### Existing substrate-symmetry-group infrastructure

1. **`manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md`** (clm-j550uh + clm-9kd2t3) — canonical 4-port amplitude space decomposition under $T_d$: $V_{\text{4-port}} = A_1 \oplus T_2$. The S-matrix $S = (1/2)\mathbf{1} - I$ has eigenvalues $\{+1, -1, -1, -1\}$ with $A_1$ → +1, $T_2$ → −1 (triply degenerate). Group-theoretic foundation for photon identification, Cosserat sector mapping, $A_1$ vs $T_2$ propagation-speed split. **This is the canonical substrate group-action on the K4 port basis** but it operates on the 4-port LOCAL node amplitude space, not on the (2,3) Clifford-torus phase-space mode space directly.

2. **`manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/k4-rotation-group.md`** (clm-ys0xl1 + clm-7pvh9i + clm-rkisb8) — K4 lattice rotation group $T = A_4$ (order 12); full symmetry $T_d = S_4$ (order 24, adds A↔B mirror swap); double cover $2T \subset SU(2)$ (order 24) is the substrate-native source of spin-½ via Finkelstein-Misner. This is the SAME group as in (1) but described as a group on space rather than a representation on port amplitudes.

3. **`manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/tetrahedral-t-universality.md`** — $|T| = 12$ universality across four routes (coordination / Cosserat dimensional / magic-angle multiplicity / axiom-level constitutive ratio).

### Existing canonical reframes of the additive assembly

4. **`manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md`** (clm-rtdmsn) — the electron's $\alpha^{-1}$ as **Q-factor of the LC tank at TIR boundary**, identifying $\Lambda_{\text{vol}}/\Lambda_{\text{surf}}/\Lambda_{\text{line}}$ with $\mathcal{M}/\mathcal{J}/\mathcal{Q}$ boundary observables. Two independent paths (LC-tank ratio + multipole geometric sum) agree to $\delta_{\text{strain}} = 2.225 \times 10^{-6}$.

   Critical observation: **Path A (LC-tank) computes $Q_{\text{tank}} = \omega_C L_e / R = 1/\alpha$ as a SINGLE impedance ratio**, NOT as a sum of three pieces. The decomposition into $4\pi^3 + \pi^2 + \pi$ is only visible in Path B (the multipole / codimensional split). The agreement to $\delta_{\text{strain}}$ between Path A and Path B is itself the strongest empirical signal that the codimensional split IS the correct decomposition of the same underlying tank Q-factor.

5. **`manuscript/ave-kb/common/boundary-observables-m-q-j.md`** (clm-ze4clw + clm-ofys5v + clm-vnp57s + clm-sjjvhf + clm-3bwhad) — the substrate's three boundary-observable invariants $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ at every $\Gamma = -1$ saturation surface, organized by Stokes-theorem dimensional structure (3D / 2D / 1D). The Vol 1 Ch 8 sum-decomposition is presented here as the electron-scale realization of the substrate's natural three-integral boundary-observability structure.

6. **`manuscript/ave-kb/vol2/nuclear-field/ch12-millennium-prizes/yang-mills-steps3-5.md`** — uses "irreducible representations of $SU(N)$" in a different context (gauge-group emergence from $(2, q)$ torus knots); not a direct precedent for sum-decomposition orthogonality.

### Prior orthogonality work

7. **`research/_archive/L3_electron_soliton/30_photon_identification.md`** — uses "$A_1$-orthogonal" exactly per the canonical $T_d$ irrep decomposition; precursor to the canonical leaf (1).

8. **`research/_archive/L3_electron_soliton/54_pair_production_axiom_derivation.md`** — Pythagorean vacuum strain theorem `V_total² = V_lon² + V_gate²` orthogonal-DoF energy decomposition; canonical home is `AVE-APU/manuscript/vol_1_axiomatic_components/chapters/05_geometric_triodes.tex:26-37`. This is energy-additivity-from-orthogonal-projection, which is structurally relevant to the present question (separable orthogonal DoFs give additive energy contributions; this is the simplest "orthogonality → additive sum" pattern in the corpus).

9. **No prior canonical or research-doc attempt at Schur orthogonality for the three-regime sum** found. This is genuine green-field.

### Existing claim-level acknowledgment of the open question

10. The clm-0ktpcn rationale block (line 93 of `manuscript/ave-kb/vol1/claim-quality.md`) explicitly states: *"the leaf's own forms give $\Lambda_{\text{vol}} = 16\pi^3 (R \cdot r)$ and $\Lambda_{\text{surf}} = 4\pi^2 (R \cdot r)$, i.e. $\Lambda_{\text{vol}} \equiv 4\pi \cdot \Lambda_{\text{surf}}$, so the $(R, r, d) \to \Lambda$ map has only 2-dimensional image and 'orthogonality' cannot mean parameter-independence."* This $(R, r)$-collinearity issue is the FIRST hurdle any Schur argument must address.

11. The current chapter `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md` (Phase 3-A1 reframed form) carries the open caveat verbatim in the §"Additive assembly of the shape factors (open structural element)" subsection, explicitly cross-linking to "Phase 3-A2 of the `clm-0ktpcn` strengthening workstream" — the work this prereg is registering.

12. The Phase 3-A1+Q2 result doc (`research/2026-05-26_clm-0ktpcn-phase-3-A1-Q2-prose-reframe-result.md`) explicitly states the prose-reframe **does NOT close** the Schur orthogonality question and preserves the strengthen-by item verbatim.

---

## Pre-test physics walk (`pre-test-physics-check` + `substrate-native-check` + `phase-space-coordinate-check`)

### What does "the sum is orthogonal" mean physically?

The claim is that

$$
\alpha^{-1}_{\text{ideal}} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}}
$$

is additive with no cross-terms. For this to be **substrate-derived** rather than asserted, the three $\Lambda_i$ must be:

(i) Distinct sectors of some substrate object (a kernel, a Hilbert space, a stored-energy functional) whose total is $\alpha^{-1}$; AND
(ii) Sectors that are pairwise orthogonal under some substrate-physical inner product, so that the kernel's norm-squared decomposes as a sum of sector contributions without cross-terms.

Schur orthogonality is the canonical theorem in compact-group representation theory that gives this kind of decomposition for free, IF the substrate object lives in a Hilbert space carrying a group representation that decomposes into irreducible representations.

### What is the substrate object?

Per the Vol 4 Ch 1 / Q-factor framing (canonical `theorem-3-1-q-factor.md`): the substrate object is the **LC tank's stored reactive energy at the TIR boundary**, evaluated per spinor cycle. Path A gives the tank Q-factor as a single ratio $\omega_C L_e / R = 1/\alpha$. Path B (Vol 1 Ch 8) gives the same number as a codimensional split.

Per the boundary-observables framing (canonical `boundary-observables-m-q-j.md`): the substrate object is the **total integrated invariant content of the electron's $\Gamma = -1$ saturation surface**, organized into $\mathcal{M}$ (3D-volume), $\mathcal{J}$ (2D-surface), $\mathcal{Q}$ (1D-loop). Each invariant uses one fewer integration dimension than the substrate's 3D bulk.

These two framings are equivalent at Golden Torus geometry: $\Lambda_{\text{vol}}$ measures the 3D phase-volume reactance ($\leftrightarrow \mathcal{M}$); $\Lambda_{\text{surf}}$ measures the 2D Clifford-torus surface reactance ($\leftrightarrow \mathcal{J}$); $\Lambda_{\text{line}}$ measures the 1D cross-section perimeter reactance ($\leftrightarrow \mathcal{Q}$).

### What is the substrate symmetry group?

Two candidate groups operate in this problem:

(a) **K4 tetrahedral group $T_d = S_4$** (order 24, with rotation subgroup $T = A_4$ of order 12) — acts on the 4-port amplitude space at each node, gives $A_1 \oplus T_2$ decomposition (1 + 3). This is the canonical AVE-substrate-native group per `k4-port-irrep-decomposition.md`.

(b) **$U(1) \times U(1)$ on the Clifford-torus phase-space angles $(\theta_1, \theta_2)$** — Peter-Weyl decomposition gives orthogonal modes $e^{i(m \theta_1 + n \theta_2)}$ labeled by $(m, n) \in \mathbb{Z}^2$. The $(2, 3)$ electron winding is one such mode.

### The geometric (not representation-theoretic) framing

Critical observation from the corpus survey: the three $\Lambda_i$ are not "components of a single kernel in a single Hilbert space decomposed into irreps." They are **integrals of unit measure over three sub-manifolds of different codimensions of the Clifford-torus embedding $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$**:

- $\Lambda_{\text{vol}}$: 3-volume measure of a "phase volume" inside $S^3$ — proportional to $(2\pi R)(2\pi r)(2\pi \cdot 2)$
- $\Lambda_{\text{surf}}$: 2-area measure of the Clifford torus inside $S^3$ — proportional to $(2\pi R)(2\pi r)$ (half-covered)
- $\Lambda_{\text{line}}$: 1-length measure of the tube cross-section — equals $\pi d$

The fact that the integrals are over **disjoint codimensional strata** (a 3-volume, a 2-surface, a 1-loop) is a **dimensional-orthogonality** statement, not a representation-theoretic Schur orthogonality. In the language of differential forms on $S^3$: 3-forms, 2-forms, and 1-forms live in different graded components of the de Rham complex $\Omega^*(S^3)$; the dimensional separation IS the orthogonality.

This is the most likely substrate-native answer. The question becomes: **does the substrate-mechanism content uniquely select this codimensional decomposition over alternative decompositions (e.g. radial-vs-angular split, $T_d$ irrep split, $U(1) \times U(1)$ harmonic split) — and if so, why?**

---

## Forward-pre-registered argument structure

I will attempt to derive the additive assembly via four progressively-more-rigorous routes, in order from strongest-to-weakest hope of closure:

### Route 1 — Stokes-graded de Rham decomposition on $S^3$

**Claim**: The electron-scale substrate object is the integrated Q-factor density on the electron's saturation surface inside $S^3$. The integration decomposes naturally as a sum of integrals over the codimension-3, codimension-2, codimension-1 strata of the Clifford-torus embedding $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$.

**Substrate-mechanism content**: Each codimensional stratum measures one of $\mathcal{M} / \mathcal{J} / \mathcal{Q}$ (via the canonical `boundary-observables-m-q-j.md` mapping). The integration measures on the strata are mutually exclusive — a 3-volume, a 2-area, a 1-length — and integrate independently. **Additivity is forced by the graded-dimensional structure of the de Rham complex on $S^3$**: 1-forms, 2-forms, 3-forms live in $\Omega^1, \Omega^2, \Omega^3$ respectively; these are direct-sum-orthogonal in the Hodge decomposition $\Omega^k \perp \Omega^j$ for $k \neq j$ under the $L^2$ pairing $\langle \omega_k, \omega_j \rangle = \int_{S^3} \omega_k \wedge *\omega_j$ (which vanishes by degree-counting whenever $k \neq j$).

**Status check**: This is structural orthogonality of differential-form degree, a substrate-mathematics theorem on $S^3$ (and indeed on any oriented Riemannian manifold). The substrate-mechanism content per Stokes-theorem dimensional structure (`boundary-observables-m-q-j.md`) is that each integrated invariant uses one fewer integration dimension than the substrate's 3D bulk — this IS the substrate-mechanism specialization of the de Rham grading.

**Honest assessment** (`ave-evidence-framing-discipline`): if accepted, this is a substrate-mechanism manifestation of de Rham orthogonality on $S^3$ acting on a substrate-derived 3-D / 2-D / 1-D integral structure. It is **not** Schur orthogonality (which would be representation-theoretic on a group, not de Rham on a manifold). The naming-substitution is honest only if I label it as **dimensional-grading orthogonality via Hodge decomposition**, not as "Schur orthogonality of irreducible representations of the substrate's tetrahedral group."

**Pre-registered verdict at this route**: if this route closes, the result is **a substrate-mechanism derivation of the additive assembly via the substrate's natural three-integral boundary-observability structure (canonical at `boundary-observables-m-q-j.md`), justified by Hodge orthogonality on $S^3$.** This is genuinely substrate-derived (the three-integral structure IS Stokes-theorem dimensional reduction at the $\Gamma = -1$ saturation surface), but it is **not Schur orthogonality of group irreps**.

### Route 2 — $T_d$ irrep decomposition on the substrate 4-port amplitude space (canonical Schur)

**Claim**: The K4 4-port amplitude space carries $V_{\text{4-port}} = A_1 \oplus T_2$ under $T_d$ (canonical at `k4-port-irrep-decomposition.md`). If the three $\Lambda$'s could be identified with $T_d$-irreducible sector contributions to a single substrate kernel, Schur orthogonality would apply directly.

**Substrate-mechanism content**: $A_1$ (1D, scalar/longitudinal) maps to Cosserat translational $u$; $T_2$ (3D, vector-like/transverse) maps to Cosserat microrotational $\omega$. The dimensional count is $1 + 3 = 4$, not $1 + 2 + 3 = 6$. **There is no canonical three-irrep decomposition of $V_{\text{4-port}}$ under $T_d$** — the decomposition is two pieces ($A_1$ + $T_2$), not three.

**Pre-registered verdict at this route**: Route 2 fails at the symmetry-group / irrep-count level. $T_d$ on K4 4-port gives 2 irreps, not 3. To rescue Route 2 would require either (i) a different substrate group whose irrep count is 3, or (ii) further refinement of the $T_2$ irrep (e.g. by splitting under $T_2 \supset C_3$ or $T_2 \supset C_2$, but these subgroup restrictions don't have substrate-mechanism justification as Schur sectors of the $\alpha^{-1}$ decomposition).

### Route 3 — $U(1) \times U(1)$ Peter-Weyl on the Clifford-torus phase-space angles

**Claim**: The two Clifford-torus angles $(\theta_1, \theta_2) \in [0, 2\pi)^2$ carry $U(1) \times U(1)$, with Peter-Weyl decomposition $L^2(\mathbb{T}^2) = \bigoplus_{m, n \in \mathbb{Z}} \mathbb{C} e^{i(m \theta_1 + n \theta_2)}$. Schur orthogonality $\int_{\mathbb{T}^2} e^{i(m \theta_1 + n \theta_2)} \cdot \overline{e^{i(m' \theta_1 + n' \theta_2)}} \frac{d\theta_1 d\theta_2}{(2\pi)^2} = \delta_{mm'} \delta_{nn'}$ holds.

**Substrate-mechanism content**: The $(2, 3)$ electron winding is the single mode $(m, n) = (2, 3)$ on $\mathbb{T}^2$. Peter-Weyl on $L^2(\mathbb{T}^2)$ decomposes functions into mode contributions, NOT integrals into codimensional contributions. The substrate object whose Peter-Weyl decomposition the three $\Lambda$'s could be is the **square-amplitude of the soliton wave-mode on $\mathbb{T}^2$**, integrated over the torus — but this is a 2D integral with a single dimensional structure, not a sum of 3D + 2D + 1D integrals.

**Pre-registered verdict at this route**: Route 3 fails at the substrate-object-identification level. Peter-Weyl on $\mathbb{T}^2$ decomposes a single 2D integral into mode-by-mode contributions all of which are 2D integrals; it does NOT decompose a multi-dimensional measurement into a 3D + 2D + 1D sum.

### Route 4 — Op21 multi-mode geometric mode-counting (per `theorem-3-1-q-factor.md` §"Op21 multi-mode generalization")

**Claim**: At the saturation boundary, each mode with $\ell$ wavelengths around a 1D circumference releases $\sim 1/\ell$ of energy per cycle, giving $Q = \ell$ per mode. The Nyquist mode-count identity (single-cell-per-natural-unit) makes mode counts equal geometric measures: 1D circumference $L$ → cell-count $L$; 2D area $A$ → cell-count $A$; 3D volume $V$ → cell-count $V$. The three-$\Lambda$ sum is then the Op21 multi-mode generalization at Golden Torus geometry.

**Substrate-mechanism content**: Op21 is a canonical AVE substrate operator (multi-mode Q-factor at saturation boundary). The mode-counting argument gives the SUM as a substrate-derived fact at Golden Torus geometry, without needing Schur orthogonality at the representation-theoretic level — it is instead an **additive mode-count via dimensional cell-counting at Nyquist scale**.

**Pre-registered verdict at this route**: Route 4 reuses the dimensional-grading argument of Route 1 with mode-count language instead of de Rham language. The substrate-mechanism content is the same — modes count by integration dimension, integrations of different dimension don't algebraically mix. Worth presenting as a parallel substrate-mechanism path to Route 1.

---

## What would PASS look like?

A PASS outcome would be a substrate-derivation document that:

(P1) Identifies a single substrate-mechanism object whose total content the three $\Lambda_i$'s decompose, with citations into the existing canonical leaves (`theorem-3-1-q-factor.md` Q-factor framing + `boundary-observables-m-q-j.md` $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ framing).

(P2) Names a **mathematical orthogonality theorem** that forces the additive (no-cross-term) assembly — preferably with substrate-mechanism justification for why that theorem applies to that object.

(P3) Honestly distinguishes between **Schur orthogonality** (representation-theoretic, requires a group acting on a Hilbert space with the kernel decomposing into irreps) and **dimensional-grading orthogonality** (de Rham / Hodge, requires only the substrate-mechanism dimensional-reduction structure at the boundary).

(P4) Per `consistency-vs-emergence` v1.2 dual-axis classification: classifies the orthogonality argument as Class 2 substrate-mechanism if it traces to substrate primitives (Ax 1 + boundary-observability structure); Class B substrate-mechanism-manifestation if it traces only to general-mathematics structure imported from outside the framework.

(P5) Per `ave-evidence-framing-discipline`: explicit precision — "Schur orthogonality" is NOT the load-bearing theorem if the actual mechanism is Hodge orthogonality; misnaming inflates the load-bearing-rigor claim. The honest label, if PASS goes through, is likely "dimensional-grading orthogonality via Hodge decomposition on $S^3$" or "codimensional-stratum orthogonality via Stokes-theorem dimensional structure at the $\Gamma = -1$ saturation surface."

(P6) The result lifts confidence on clm-0ktpcn by closing the strengthen-by item (line 95: *"Close the sum-decomposition rule: establish functional orthogonality of the self-impedance kernel (e.g. SU(2)×SU(2) irrep separation by Schur), since the nested supports (1-cycle ⊂ Clifford torus ⊂ 3-volume) defeat domain-disjointness arguments."*).

   Critical: the strengthen-by item EXPLICITLY anticipates and rejects "domain-disjointness" arguments because "the nested supports (1-cycle ⊂ Clifford torus ⊂ 3-volume) defeat domain-disjointness arguments." This is the load-bearing objection any PASS argument must address.

   A PASS argument must show **either**:
   - (P6a) that the three $\Lambda_i$ are NOT actually integrals over nested supports in the way the strengthen-by item assumes (e.g. they are differential-form integrals on different graded components $\Omega^k$ of de Rham, which IS dimensionally orthogonal regardless of whether the underlying point-set is nested);
   - **or** (P6b) genuine Schur-style representation-theoretic orthogonality (per the strengthen-by item's example "SU(2)×SU(2) irrep separation").

(P7) Confidence bump from 0.60 → 0.65 per the epic brief expected lift; solidity tracks via `min(confidence, dep-solidities)` to whatever the binding constraint is.

(P8) Per `ave-discrimination-check`: SM-counterfactual + interpretive-alternatives enumeration BEFORE asserting "AVE-substrate-distinct derivation". Question: does this argument depend on substrate primitives that the SM does not share? If yes, the result is AVE-distinct. If the argument is purely substrate-agnostic (e.g. "de Rham on $S^3$"), the result is consistency-class, not emergence-class.

---

## What would WALK-BACK look like?

A WALK-BACK outcome would be a result document that:

(W1) Documents the failure of each pre-registered route (Routes 1-4) to close the additive assembly as a substrate-derived Class 2 axiom-manifestation step. The substrate-mechanism path stops short of a fully rigorous orthogonality argument.

(W2) Edits the chapter prose at `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md` to honestly reframe the additive assembly as "additive at leading order with the codimensional decomposition pointing at the substrate's $\mathcal{M}/\mathcal{Q}/\mathcal{J}$ boundary-observability structure, but without a fully rigorous group-theoretic orthogonality derivation." This preserves the existing dual-axis classification (Class 2 axiom-manifestation on $(R, r, d)$, Class B + Class 4 on additive assembly) and removes any prose that suggested "Schur orthogonality" was achievable as a near-term closure.

(W3) Type D walk-back per `ave-walk-back` v1.1 (mechanism re-scope, not retraction): the framework continues to point at the additive assembly as a structural fact at Golden Torus geometry (the empirical numerical match to CODATA at $\delta_{\text{strain}}$ precision IS a substrate signal, just not a substrate-mechanism derivation).

(W4) The strengthen-by item is reframed: "establish functional orthogonality" is reformulated as "derive the codimensional-stratum decomposition of the electron-scale Q-factor kernel from the substrate's boundary-observability structure at the $\Gamma = -1$ saturation surface." This is a deeper substrate-mechanism question than Schur-irrep separation; it may close in future work but is not Phase 3-A2's deliverable.

(W5) Confidence stays at 0.60 (no derivation closure); solidity stays at 0.60. Honest negative result.

(W6) Per `ave-evidence-framing-discipline` Rule 11 (honest closure): a clean WALK-BACK is the discipline working at full strength. Don't drop adjudication criteria post-hoc to convert ❌ to ✅.

---

## What would RESCOPE look like?

A RESCOPE outcome would surface a sub-question whose closure is prerequisite to the orthogonality argument, with a sub-prereg spinning out the work. Likely sub-questions:

(R1) Identifying THE substrate symmetry group whose irreps the three $\Lambda_i$ would correspond to (since K4's $T_d$ gives only 2 irreps, not 3). If no canonical such group exists in the corpus, that's a corpus gap to surface.

(R2) Identifying the substrate-mechanism kernel whose graded-norm-squared the three $\Lambda_i$ would compute. The Q-factor framing of `theorem-3-1-q-factor.md` and the boundary-observables framing of `boundary-observables-m-q-j.md` both gesture at this but neither writes the kernel explicitly as a tensorial object on $S^3$ whose Hodge-graded $L^2$-norm decomposes as the sum.

(R3) Whether the Op21 multi-mode generalization mentioned in `theorem-3-1-q-factor.md` §"Op21 multi-mode generalization" already constitutes the substrate-mechanism derivation, in which case the work is *closing the cross-reference loop* rather than originating new derivation.

---

## Methodology

1. **Walk Routes 1-4 in order**, document the substrate-mechanism / standard-mathematics status of each, identify the strongest closure path.
2. **Substrate-native vocabulary throughout** per `ave-discipline-translate` v1.1 trigger 6 — "Schur orthogonality" is a standard-physics-community theorem name; use only as parenthetical translation reference. Substrate-native primary form is "additive-via-graded-dimensional-decomposition" or "additive-via-codimensional-stratum-orthogonality" depending on which Route closes.
3. **Honest classification per `consistency-vs-emergence` v1.2** — Class 2 substrate-mechanism vs Class B substrate-mechanism-manifestation vs Class 4 substrate-agnostic-consistency. The classification axis is whether the orthogonality theorem traces back to substrate primitives or only to general-mathematics structure.
4. **`ave-independence-check` for the "three regimes are independent" claim** — verify the three substrate-mechanism contributions are functionally independent (vs algebraically derivable from each other). The $(R \cdot r)$-collinearity issue (line 93 of `claim-quality.md`) is the canonical objection that must be addressed.
5. **`phase-space-coordinate-check`** — confirm the substrate-mechanism kernel and the orthogonality argument both operate on phase-space (Clifford-torus / $S^3$) coordinates, not real-space lattice coordinates.
6. **`ave-discrimination-check`** — before asserting "AVE-substrate-distinct" framing of any PASS result, enumerate SM-counterfactual and interpretive-alternatives. If the orthogonality theorem is substrate-agnostic mathematics (de Rham, Peter-Weyl), the AVE-distinct content is in the substrate-mechanism identification of the kernel, not in the orthogonality theorem itself.
7. **Audit pass per `ave-audit` discipline** before push — self-audit the result document for honesty in classification, precision in framing, and absence of post-hoc rescue.

---

## Skill firings registered for this work

- `ave-prereg` — corpus-grep completed in this prereg; 12 anchors identified.
- `ave-canonical-leaf-pull` — 5 canonical leaves pulled (ch8 + k4-port-irrep + k4-rotation-group + theorem-3-1-q-factor + boundary-observables-m-q-j).
- `ave-analytical-tool-selection` — Mode-class (per §6 toolkit-index); irrep-decomposition tool unrepresented in toolkit but adjacent to Mode class.
- `ave-discipline-translate` v1.1 trigger 6 — substrate-native vocabulary throughout; "Schur orthogonality" as parenthetical translation reference only.
- `substrate-native-check` — symmetry-group candidates ($T_d$, $U(1) \times U(1)$) both substrate-derivable from K4 + Clifford-torus structure.
- `consistency-vs-emergence` v1.2 — dual-axis classification at Route-resolution time.
- `phase-space-coordinate-check` — three-$\Lambda$ measurement lives on phase-space ($S^3 / \mathbb{T}^2 / \mathbb{C}^2$), not real-space lattice.
- `ave-independence-check` — the $(R \cdot r)$-collinearity issue handled explicitly per the claim's own caveat.
- `ave-evidence-framing-discipline` — "Schur" vs "Hodge" vs "consistency" precision is the central editorial discipline.
- `ave-walk-back` v1.1 Type D — likely fires if WALK-BACK; chapter prose reframed without retracting the additive assembly itself.
- `verify-before-cite` v1.4 — every file:line citation grep-verified.
- `ave-discrimination-check` — SM-counterfactual enumeration before any Class 2 emergence claim.
- `ave-audit` — self-audit pre-push.

---

## Expected confidence-lift trajectory

- **PASS** (Route 1 closes via Hodge dimensional grading, with substrate-mechanism justification): 0.60 → 0.65. New canonical leaf at `vol1/operators-and-regimes/ch6-universal-operators/` for the kernel-decomposition theorem; or appended sub-section to `theorem-3-1-q-factor.md` if natural fit there. Strengthen-by item (line 95) closes.
- **WALK-BACK** (Routes 1-4 all fail to close as rigorous substrate-derivations): 0.60 stays. Chapter prose at ch8-alpha-golden-torus.md edited to reframe "orthogonal sum" framing as "additive at leading order with documented sub-leading-substrate-mechanism gap." Strengthen-by item reframed.
- **RESCOPE**: 0.60 stays. Sub-prereg surfaces the prerequisite substrate-symmetry-group identification question.

Per epic brief honest closure probability: ~40% PASS / ~60% WALK-BACK. My pre-survey leaning is slightly more pessimistic than this on Schur-strict but more optimistic on Hodge-graded — that is, I expect a HALF-PASS where the dimensional-grading argument closes but the explicitly-Schur framing does NOT. Whether this is recorded as PASS or WALK-BACK depends on Grant's calibration of "rigorous substrate-derivation" — clean substrate-mechanism story via Hodge decomposition + Stokes-theorem dimensional reduction (PASS-class) versus failure-to-Schur (WALK-BACK-class). I will write the result honestly and let the auditor pass judge.

---

## Branch + commit plan

- **Branch**: `analysis/clm-0ktpcn-phase-3-A2-schur-orthogonality` off `main` @ `453c335e` ✓ created
- **Push but DO NOT merge** — orchestration session opens PR for coworker review per session conventions
- **Commits expected**:
  1. `research(clm-0ktpcn): Phase 3-A2 pre-registration — Schur orthogonality attempt for sum-decomposition`
  2. `research(clm-0ktpcn): Phase 3-A2 result — <outcome>`
  3. (conditional on PASS) `kb(vol1): close Phase 3-A2 strengthen-by item + confidence lift on clm-0ktpcn` OR
     (conditional on WALK-BACK) `kb(vol1/ch8-alpha-golden-torus): reframe additive-assembly framing — Phase 3-A2 walk-back closure`
  4. `orch(clm-0ktpcn): Phase 3-A2 execution log + epic doc update`

- **Audit tag (orchestration session, not implementor)**: `audit/2026-05-26_clm-0ktpcn-phase-3-A2-schur-orthogonality` at branch tip pre-merge.

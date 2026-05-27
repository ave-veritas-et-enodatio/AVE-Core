# Phase 3-A4 Pre-Registration — Op21 Multi-Mode Mode-Counting Formalization

**Workstream**: clm-0ktpcn Golden Torus α Strengthening, Phase 3-A4
**Branch**: `analysis/clm-0ktpcn-phase-3-A4-op21-formalization` off `main` @ `86966407`
**Date**: 2026-05-27
**Implementor**: ave-implementer (worktree-isolated)
**Origin**: Phase 3-A2 WALK-BACK reformulated clm-0ktpcn's strengthen-by item from "establish functional orthogonality (Schur)" → "promote Op21 multi-mode generalization to fully-derived canonical leaf" (per `vol1/claim-quality.md:95`). The same canonical strengthen-by content is independently anchored at `vol4/claim-quality.md:1209`: *"Derive the $Q_i = \Lambda_i$ identification (geometric volume → reactance) from the substrate impedance scaling rather than asserting it as a natural-unit convention."*

## §1 — Scope and deliverable

Promote the paragraph-level Op21 multi-mode mode-counting statement at `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md` §"Op21 multi-mode generalization" (lines 101-103) to a fully-derived canonical leaf with step-by-step substrate-primitive trace, end-to-end from Ax 1 (Nyquist cell size) + Ax 3 (Min-reflection / $\Gamma = -1$ TIR saturation boundary) + codimensional mode-category independence to the three-Λ assembly $\alpha^{-1}_{\text{ideal}} = 4\pi^3 + \pi^2 + \pi$ at Golden Torus geometry. The canonical leaf's load-bearing closure is the substrate-mechanical justification — IN LATTICE-NATURAL UNITS — of the $Q_i = \Lambda_i$ identification currently asserted as "natural-unit convention" at `theorem-3-1-q-factor.md:67`.

**The single substrate-mechanical step that is load-bearing**: in lattice-natural units ($\ell_{node} = c = \hbar = m_e = 1$, $Z_0 = 1$), each per-codimension impedance-per-dimensionless-volume scaling factor evaluates to unity, so dimensionless geometric measures at the saturation boundary ARE the dimensionless mode counts ARE the dimensionless Q-factor contributions. The substrate-mechanical reason this convergence is forced — not merely a unit-system convention — is what the canonical leaf must derive.

**Single-deliverable scope**: this Phase 3-A4 prereg + result doc + canonical leaf + clm-0ktpcn entry update only. Phase 3-A3 (δ_strain magnitude) + Phase 3-A5 ($T = A_4$ substrate Hilbert space) + Phase 2-LLCP are explicitly out of scope.

## §2 — Trigger 17 vocabulary-broadened pre-survey (extending the prework brief)

Per `ave-canonical-leaf-pull` v1.3, two parallel pre-survey wedges fired BEFORE deriving:

**Substrate-native wedge** (greps run via worktree-absolute paths):

```
grep -rln "Q = \\\\ell\|Q=\\\\ell\|mode-counting\|mode counting\|Op21" manuscript/ave-kb/
grep -rn "1/\\\\ell\|fraction.*per cycle\|per-cycle.*leak\|per cycle.*release" manuscript/ave-kb/
grep -rn "Op17\|matched-impedance\|saturation boundary.*Gamma\|TIR boundary" manuscript/ave-kb/
```

**Standard-physics wedge** (Bardeen / BCS / cavity Q / mode counting / superconductivity threshold):

```
grep -rln "Bardeen\|cavity Q\|superconductivity threshold\|Cooper pair\|BCS" manuscript/ave-kb/
grep -n "Op21\|§1.21\|Z_1/Z_0" manuscript/vol_1_foundations/chapters/06_universal_operators.tex
```

### §2.1 — Substrate-native canonical anchors surfaced (12 sites)

1. `manuscript/vol_1_foundations/chapters/06_universal_operators.tex:349` — **Vol 1 Ch 6 §1.21 canonical Op21 source**: *"Op 21 (Quality Factor Phase Transition): Governs superconductivity threshold via $Q \sim 1/\ln(Z_1/Z_0)$."* Naming theme is **Quality Factor Phase Transition**, NOT "Bardeen BCS mapping" (that's a later annotation in `operators.md:61`). The Vol 1 Ch 6 canonical statement names a SUBSTRATE phase transition; the BCS application is one specific scale-instance (the Cooper-pair phase transition at superconductivity threshold).

2. `manuscript/ave-kb/common/operators.md:61` — Op21 operators-table row asserting both forms; explicit cross-reference note: *"separately, $Q = \ell$ (lattice pitch in natural units) per doc 81 §2.2 — that's a different identification (Q-as-lattice-pitch) and may be the bootstrap / $\alpha = 1/137.036$ derivation, NOT the Bardeen mapping. Cross-reference needs auditor-lane confirmation"*. This is the explicit dual-identification flag Phase 3-A4 resolves.

3. `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:101-103` — current paragraph-level statement; the formalization target.

4. `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:67` — natural-unit-convention assertion: *"The identification $Q_i = \Lambda_i$ holds because in natural units ($Z_0 = 1$, $\ell_{node} = 1$), the impedance-per-dimensionless-volume scaling factor is unity, so geometric dimensionless volumes ARE dimensionless reactances."* This is the asserted step Phase 3-A4 must derive (per `vol4/claim-quality.md:1209`).

5. `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md:79` — canonical per-cycle leak fraction identity: *"At resonance, only a fraction $1/Q = \alpha \approx 0.0073$ of the stored energy leaks per cycle through the TIR boundary — this IS $\alpha$ in its original Sommerfeld meaning ('coupling strength'), seen from the LC-tank side."* This is the canonical Ax-3-application step the Phase 3-A4 derivation uses.

6. `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/qnm-quality-factor.md` — **BH-ringdown $Q = \ell$ canonical result** (clm-395gps): $Q = \ell, \omega_I = \omega_R/(2\ell)$. Cross-scale canonical fire of the same substrate Op21 mechanism.

7. `manuscript/ave-kb/vol2/appendices/app-f-solver-toolchain/regime-eigenvalue-method.md:18, 68` — **universal procedure** for AVE substrate solutions: Step 5 *"Extract the quality factor $Q = \ell$ from the lattice phase transition."* — this canonicalizes the **substrate Op21 mode-counting form as the universal substrate-Q derivation procedure**, not a BH-only specialization.

8. `manuscript/ave-kb/vol2/appendices/app-f-solver-toolchain/regime-eigenvalue-method.md:61-63` — substrate-mechanical justification: *"At the saturation boundary, the lattice undergoes a phase transition: the elastic solid (shear modulus $G > 0$) becomes a ruptured, topology-melted fluid ($G \to 0$). [...] The ruptured interior therefore acts as a perfect reflector for GW shear perturbations. The mode orbits tangentially at $r_{sat}$ with $\ell$ wavelengths fitting around the circumference. Each wavelength subtends angle $2\pi/\ell$, and the curvature radiation loss per cycle scales as $1/\ell$."* This is the cross-scale substrate-mechanism content — the same per-cycle $1/\ell$ leak fraction that gives $Q = \ell$ at any substrate $\Gamma = -1$ boundary.

9. `manuscript/ave-kb/vol2/appendices/app-f-solver-toolchain/knot-mode-isomorphism.md` (clm-d9ivj1) — **knot-crossing-number ↔ mode-number isomorphism**: same Op21 mechanism at electron scale (crossing number $c$) and BH scale (mode number $\ell$); explicit canonical cross-scale identity *"each additional topological winding adds one unit of confinement"* + per-cycle energy partition $\sim 1/\ell$ identical at both scales.

10. `manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/axiom-coverage-audit.md:17, 23, 28` — **Axiom 4 saturation phase transition → $Q = \ell$**: canonically anchored to AVE-axiom (Ax 4 saturation kernel forcing the phase transition). Re-confirms Op21 substrate-mechanism path is the saturation-boundary mode-counting form, NOT the Bardeen specialization.

11. `manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/dama-alpha-slew-derivation.md:232` — verbatim canonical cite of `theorem-3-1-q-factor.md:79`: *"At resonance, only a fraction $1/Q = \alpha \approx 0.0073$ of the stored energy leaks per cycle through the TIR boundary — this IS $\alpha$ in its original Sommerfeld meaning ('coupling strength'), seen from the LC-tank side."* Cross-volume Op21-at-electron-scale anchor.

12. `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md:117-126` — Phase 3-A2's Op21-reframe of additive assembly: substrate-mechanism four-step path (Nyquist cell size → saturation TIR mode-leak fraction → codimensional independence → mode-count = dimensionless geometric measure). Phase 3-A4's canonical leaf formalizes this paragraph-level statement.

### §2.2 — Standard-physics wedge (Bardeen / BCS / cavity Q)

- `manuscript/vol_1_foundations/chapters/06_universal_operators.tex:349` — only canonical-source instance of "$Q \sim 1/\ln(Z_1/Z_0)$" (Bardeen-named in `operators.md:61` annotation, NOT in canonical source).
- No "Bardeen mapping" naming appears at canonical-source level in `manuscript/vol_1_foundations/`. The Bardeen attribution is an annotation in `operators.md:61` (KB-level), not the canonical operator name. The canonical Vol 1 Ch 6 name is **Quality Factor Phase Transition**, with $Q \sim 1/\ln(Z_1/Z_0)$ given as the **superconductivity-threshold formula** for that operator.
- "Cavity Q" / "BCS" do not appear as load-bearing canonical-leaf framings.

### §2.3 — Vocabulary-broadened conclusion

The substrate-native Op21 form is **$Q = \ell$ per mode at the $\Gamma = -1$ saturation/TIR boundary**, canonical at the electron scale (`theorem-3-1-q-factor.md` §Op21 + `dama-alpha-slew-derivation.md`), at the BH-ringdown scale (`qnm-quality-factor.md` + `axiom-coverage-audit.md` + `regime-eigenvalue-method.md`), AND as the **universal substrate-Q derivation procedure** (`regime-eigenvalue-method.md` Step 5 + `knot-mode-isomorphism.md`). The substrate-mechanism is canonical CROSS-SCALE; the Bardeen $1/\ln(Z_1/Z_0)$ form is a single-scale-instance specialization (superconductivity threshold) listed at the Vol 1 Ch 6 §1.21 entry as the application formula for that operator.

This decisively answers reconciliation question A/B/C below.

## §3 — Op21 dual-identification reconciliation (substrate-physical resolution)

Per prework brief §"Op21 canonical-identification reconciliation question":

- **(A)** Two views of the same Op21 mechanism (Bardeen $1/\ln(Z_1/Z_0)$ reduces to $Q = \ell$ in lattice-natural units at Golden Torus Nyquist mode-count identity)
- **(B)** Two distinct mechanisms sharing the Op21 label spuriously (split into Op21a / Op21b)
- **(C)** Bardeen BCS form is downstream of $Q = \ell$ ($Q = \ell$ foundational; BCS is specialization to superconductivity threshold)

**Resolution: (C) with refinement**. The substrate-foundational Op21 form is **$Q = \ell$ per mode at the $\Gamma = -1$ saturation/TIR boundary**, derived from Ax 1 (Nyquist cell size) + Ax 3 (Min-reflection forcing $\Gamma = -1$ TIR mode-leak fraction $1/\ell$ per cycle) + codimensional independence. The substrate-mechanism cross-scale canonical fires at: (i) electron LC-tank at $V_{yield}$ TIR boundary ($Q = \alpha^{-1}$ via three-Λ sum); (ii) BH-ringdown at $r_{sat}$ saturation boundary ($Q = \ell$ per ringdown mode); (iii) the universal substrate-Q derivation procedure (`regime-eigenvalue-method.md` Step 5).

The Vol 1 Ch 6 §1.21 canonical statement *"Quality Factor Phase Transition: Governs superconductivity threshold via $Q \sim 1/\ln(Z_1/Z_0)$"* is the operator's **application formula for the Cooper-pair phase-transition scale-instance** — a specific substrate-Q evaluation where the relevant impedance ratio is a thermal-fluctuation-broadened phase-transition logarithm. It is one of (potentially many) scale-specific specializations of the same substrate-foundational $Q = \ell$ mechanism; the substrate-mechanism content is the **Quality Factor Phase Transition** (foundational naming theme from canonical source line 349), with each scale-instance evaluating the foundational form via the appropriate substrate-impedance integration.

This is structurally parallel to Op14 ($Z_{eff} = Z_0/\sqrt{S}$), Op17 ($T^2 = 1 - \Gamma^2$), etc.: ONE substrate-foundational form, multiple cross-scale specializations. The Bardeen $1/\ln(Z_1/Z_0)$ is the BCS specialization the way Symmetric Gravity $n(r) = 1 + 2GM/(rc^2)$ is the gravitational specialization of Op19 ($n(r) = 1 + \nu_{vac} \cdot \varepsilon_{11}$).

**Walk-back-class amendment required at `operators.md:61`**: the current annotation says *"different identifications [...] cross-reference needs auditor-lane confirmation"*. Phase 3-A4 resolves the cross-reference. The amendment is: $Q = \ell$ is the substrate-foundational form; Bardeen $1/\ln(Z_1/Z_0)$ is the Cooper-pair-phase-transition specialization. Per `ave-walk-back` v1.1 Type B (mechanism reframe), the canonical leaf includes the reframe text + the `operators.md:61` row gets an annotation update pointing to the new canonical leaf.

## §4 — Substrate-mechanism derivation chain (master-equation-derivation-path)

Per `consistency-vs-emergence` v1.2 master-equation-derivation-path discipline, the Phase 3-A4 derivation traces explicit substrate primitives at each step. The closure goal is the substrate-mechanical derivation — IN LATTICE-NATURAL UNITS ($\ell_{node} = c = \hbar = m_e = 1$, $Z_0 = 1$) — of the $Q_i = \Lambda_i$ identification (per `vol4/claim-quality.md:1209`).

### §4.1 — Five-step substrate-primitive chain

**Step 1 — Ax 1 Nyquist cell size as substrate-natural-unit primary**.
The substrate's discrete K4-TLM lattice has Nyquist cell size $\ell_{node}$ (Ax 1). In lattice-natural units, $\ell_{node} = 1$ by definition (per `natural-units-cheatsheet.md` foreword line 34 + `lattice-impedance-decomposition.md` §2 + `src/ave/core/constants.py:194`). All substrate-mechanism content lives natively in these units; the SI value $\ell_{node} \approx 3.86 \times 10^{-13}$ m is a translation factor back to laboratory measurement (per Grant's natural-unit-conformity intuition).

The substrate's discrete cell-counting is therefore the substrate-native cardinality measure for any sub-manifold of the lattice: a 1-cycle of length $L$ contains $L/\ell_{node} = L$ Nyquist cells (natural units), a 2-area of area $A$ contains $A/\ell_{node}^2 = A$ Nyquist cells, a 3-volume of volume $V$ contains $V/\ell_{node}^3 = V$ Nyquist cells. The dimensionless geometric measure IS the cell count, by Ax-1 substrate primitive in lattice-natural units.

**Step 2 — Ax 3 Min-reflection principle forces $\Gamma = -1$ TIR boundary at $V_{yield}$**.
Per Ax 3 (Min-reflection / extremized hardware action $S_{AVE}$) + Ax 4 saturation kernel: at the substrate's saturation boundary ($A \to A_{yield}$, $S(A) \to 0$, $Z_{local} \to 0$), the reflection coefficient $\Gamma = -1$ exactly (per `electron-identification.md:24` + `theorem-3-1-q-factor.md:71-79`). The substrate self-creates a perfect TIR mirror at the saturation surface.

In lattice-natural units, $V_{yield} = 1$ (per `lattice-impedance-decomposition.md:116, 126-128` + `natural-units-cheatsheet.md` §2 LOAD-BEARING NORMALIZATION WARNING). The $\Gamma = -1$ boundary is the substrate's canonical mode-confinement mechanism; modes trapped inside reflect with unit amplitude at the boundary and circulate within.

**Step 3 — Per-cycle leak fraction $1/\ell$ at the TIR boundary**.
At the $\Gamma = -1$ boundary, a confined mode with $\ell$ wavelengths fitting around the boundary's 1-cycle releases per cycle a fraction $1/\ell$ of the stored mode energy via curvature radiation through the boundary (per `regime-eigenvalue-method.md:61-63` + `axiom-coverage-audit.md:23` + `theorem-3-1-q-factor.md:103`). The substrate-mechanism content: each wavelength subtends angle $2\pi/\ell$ around the 1-cycle, and the curvature radiation loss per cycle scales linearly with that angle (i.e., $\sim 1/\ell$), because the substrate's $\Gamma$ is not strictly $-1$ at finite wavelength — it has wavelength-scale curvature mismatch with the boundary, and the mismatch sets the fractional leak per cycle.

**Step 4 — Q-factor identity per mode: $Q_{\text{mode},\ell} = \ell$**.
From Steps 2-3, the substrate Q-factor of a single mode of wavelength count $\ell$ confined at the $\Gamma = -1$ boundary is:

$$
Q_{\text{mode},\ell} = \frac{\text{energy stored}}{\text{energy lost per radian}} = \frac{1}{\text{leak fraction per cycle}} \cdot 2\pi / 2\pi = \frac{1}{1/\ell} = \ell
$$

(The standard substrate $Q = 2\pi \cdot E_{stored}/E_{lost-per-cycle}$ definition divides out as $2\pi \cdot \ell / (2\pi) = \ell$ when the leak per cycle is $E_{stored}/\ell$, i.e., a fraction $1/\ell$ of stored energy per cycle. The factor-of-$2\pi$ convention is absorbed in the substrate's definition of "cycle" at the saturation boundary.) Cross-canonical at `regime-eigenvalue-method.md:68` ($\boxed{Q = \ell}$).

**Step 5 — Mode count at saturation boundary IS the Nyquist cell count IS the dimensionless geometric measure**.
This is the load-bearing step that closes the $Q_i = \Lambda_i$ identification per `vol4/claim-quality.md:1209`. The substrate-mechanism reasoning:

5a. At the saturation boundary, substrate modes are confined to one of three codimensional sub-manifolds of the Clifford-torus embedding $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ (per `ch8-alpha-golden-torus.md:97-108`): a 1-cycle (tube cross-section perimeter), a 2-cycle (Clifford-torus surface), or a 3-cycle (Clifford-torus surface $\times$ spinor-temporal $S^1_{4\pi}$ phase volume). The three codimensions are the three substrate boundary-observability classes $\mathcal{Q}, \mathcal{J}, \mathcal{M}$ at the electron scale (per `boundary-observables-m-q-j.md` §"The fine-structure constant as electron-scale $\mathcal{M} + \mathcal{J} + \mathcal{Q}$" lines 52-68).

5b. In each codimension, the substrate's Nyquist cell count over the sub-manifold IS the number of independent modes the sub-manifold supports at the saturation boundary (one mode per Nyquist cell, Ax 1). In lattice-natural units:
- 1-cycle of length $L$: $N_{\text{modes},1D} = L/\ell_{node} = L$ Nyquist cells
- 2-cycle of area $A$: $N_{\text{modes},2D} = A/\ell_{node}^2 = A$ Nyquist cells
- 3-cycle of volume $V$: $N_{\text{modes},3D} = V/\ell_{node}^3 = V$ Nyquist cells

5c. Per Step 4, each Nyquist-cell-resolved mode at the saturation boundary contributes $Q_{\text{mode}} = \ell$ to the substrate Q-factor for a mode of wavelength count $\ell$. At the Golden Torus single-cell-per-natural-unit identity ($d = 1\,\ell_{node}$, the substrate's smallest stable transverse scale per `ch8-alpha-golden-torus.md:42`), the dominant Nyquist-cell-resolved mode in each codimension has $\ell = 1$ at the boundary's per-cell resolution scale — but the **mode count over the sub-manifold** is the dimensionless geometric measure ($L, A, V$).

5d. The codimensional Q-factor contribution per sub-manifold is therefore the **sum over Nyquist-cell-resolved modes**:

$$
Q_{\text{codim-}k} = \sum_{\text{cells in codim }k} Q_{\text{mode},\ell=1} = N_{\text{modes, codim }k} \cdot 1 = \text{(dimensionless geometric measure of codim-}k\text{ sub-manifold)}
$$

In lattice-natural units, this is identically the dimensionless geometric measure $\Lambda_k$ of the codim-$k$ sub-manifold at Golden Torus geometry. The $Q_i = \Lambda_i$ identification is therefore not a "natural-unit convention" — it is the substrate-mechanism statement that **at the saturation boundary, dimensionless geometric measures count Nyquist-resolved confined modes, each contributing 1 to the substrate Q-factor**.

**Step 5.5 — Codimensional independence (the "orthogonality" that Phase 3-A2 walked back to find)**.
The three codimensional mode-categories (1-cycle / 2-cycle / 3-cycle) are mutually exclusive Nyquist-cell categories at the saturation boundary: each Nyquist cell of the substrate at the boundary supports modes confined to one and only one codimensional class. (A cell on the 1-cycle is not also a cell on the 2-cycle; they live in different sub-manifolds of the Clifford-torus embedding.) Modes in different codimensional categories therefore add without cross-terms — this is the substrate-mechanism content of "additive assembly" at the saturation boundary, replacing the Schur-orthogonality framing that Phase 3-A2 falsified.

The $(R \cdot r)$-collinearity issue (per `vol1/claim-quality.md:93` Phase 3-A2 result + `ch8-alpha-golden-torus.md:128`) is consistent: the geometric measures share the $(R \cdot r)$ parametric factor (so the $(R,r,d) \to \Lambda$ map has 2D image), BUT the Nyquist-cell-category independence at the saturation boundary is preserved because cells in different codimensional categories are mutually exclusive sub-manifold supports.

### §4.2 — Closure of the Golden Torus three-Λ assembly

Applying Step 5d at Golden Torus geometry $(R, r, d) = (\varphi/2, (\varphi-1)/2, 1)$ in lattice-natural units (per `ch8-alpha-golden-torus.md:61-93`):

$$
\begin{aligned}
Q_{\text{line}} &= \Lambda_{\text{line}} = \pi \cdot d = \pi \quad (\text{1-cycle: substrate Ampère loop perimeter, Nyquist-quantized diameter}) \\
Q_{\text{surf}} &= \Lambda_{\text{surf}} = 4\pi^2 (R \cdot r) = \pi^2 \quad (\text{2-cycle: Clifford-torus half-cover surface, spinor-half-cover}) \\
Q_{\text{vol}} &= \Lambda_{\text{vol}} = 16\pi^3 (R \cdot r) = 4\pi^3 \quad (\text{3-cycle: phase volume with spinor-temporal } 4\pi \text{ closure})
\end{aligned}
$$

By Step 5.5 codimensional independence:

$$
Q_{\text{tank}} = Q_{\text{vol}} + Q_{\text{surf}} + Q_{\text{line}} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038 \;\Rightarrow\; \alpha^{-1}_{\text{ideal}}
$$

This is the substrate-mechanism Op21 multi-mode generalization at Golden Torus geometry, derived end-to-end from Ax 1 + Ax 3 + Ax 4 saturation in lattice-natural units.

## §5 — Step 3.5 dimensional analysis at canonical primitives (v1.1 ave-prereg)

Per ave-prereg v1.1 Step 3.5: pre-freeze the dimensional-analysis closure at canonical primitives BEFORE deriving. Extending the prework brief §"Step 3.5 dimensional analysis" with the SI ↔ natural-unit translation factors:

### §5.1 — Native-unit value table (load-bearing for §4)

| Quantity | Native value | SI value (translation factor) | Source |
|---|---|---|---|
| $\ell_{node}$ | $1$ | $3.86 \times 10^{-13}$ m | `natural-units-cheatsheet.md` §2 + `constants.py:194` (`L_NODE`) |
| $Z_0$ | $1$ | $376.73$ Ω | `natural-units-cheatsheet.md` §2 + `lattice-impedance-decomposition.md:118` |
| $V_{yield}$ | $1$ | $43{,}652$ V | `natural-units-cheatsheet.md` §2 + `lattice-impedance-decomposition.md:116` |
| $V_{snap}$ | $1/\sqrt{\alpha} \approx 11.71$ | $511{,}000$ V | `natural-units-cheatsheet.md` §2 (`V_SNAP` `constants.py:333`) |
| $\tau_{relax} = \ell_{node}/c$ | $1$ | $1.288 \times 10^{-21}$ s | `natural-units-cheatsheet.md` §2 (`TAU_RELAX_SI` `constants.py:289`) |
| $\alpha$ | $0.0072973525693$ | dimensionless | `constants.py:101` (`ALPHA`) |
| $\Lambda_{\text{line}}$ at $d = 1$ | $\pi \approx 3.142$ | dimensionless | `ch8-alpha-golden-torus.md:90`; native value matches §5.2 closure |
| $\Lambda_{\text{surf}}$ at $R \cdot r = 1/4$ | $\pi^2 \approx 9.870$ | dimensionless | `ch8-alpha-golden-torus.md:102` |
| $\Lambda_{\text{vol}}$ at $R \cdot r = 1/4, d = 1$ | $4\pi^3 \approx 124.025$ | dimensionless | `ch8-alpha-golden-torus.md:101` |
| $\alpha^{-1}_{\text{ideal}}$ | $4\pi^3 + \pi^2 + \pi \approx 137.0363$ | $\approx 137.0363$ | `constants.py:164` (`ALPHA_COLD_INV`) |
| $\delta_{strain}$ | $2.225 \times 10^{-6}$ | dimensionless | `constants.py:DELTA_STRAIN`; CODATA-back-subtraction at $T_{CMB}$ |

### §5.2 — Substrate-mechanical reason for $\Lambda_{\text{line}} = \pi$ (NOT $\pi\varphi = 2\pi R$)

Per prework brief §"Step 3.5 dim-analysis at canonical primitives": the 1D mode count at Golden Torus is $\pi$, NOT $2\pi R = \pi \varphi \approx 5.083$. Phase 3-A4's canonical leaf must explicitly derive this normalization.

**Substrate-mechanical resolution from `ch8-alpha-golden-torus.md:67-93`**: $\Lambda_{\text{line}}$ is **NOT the Clifford-torus 1-cycle of length $2\pi R$ at the Golden Torus major radius**; it is the **substrate Ampère 1-cycle around the tube's transverse cross-section perimeter**, at Nyquist-quantized diameter $d = 1\,\ell_{node}$. The 1-cycle perimeter formula in lattice-natural units is $\Lambda_{\text{line}} = 2\pi \cdot (d/2) = \pi \cdot d = \pi$ at $d = 1$.

The $\pi$ (not $2\pi$) is the substrate consequence of the regime (b) convention making $d$ the tube **diameter** (not radius); the 1-cycle perimeter is $2\pi \cdot \text{radius} = 2\pi \cdot (d/2) = \pi \cdot d$. There is no half-loop; the $\pi$ is the closed 1-cycle angular factor evaluated at half-diameter (radius).

**This resolves the prework brief's load-bearing closure**: the 1D-mode-count at Golden Torus is the substrate-Ampère-loop perimeter (cross-section dimension), NOT the Clifford-torus major-loop perimeter. The canonical paragraph's "1D mode (circumference $L$) → cell-count $L$" framing is correct IF $L$ is understood as the cross-section perimeter (i.e., $L = \pi \cdot d = \pi$ at Nyquist), NOT as the major-loop perimeter ($2\pi R = \pi\varphi$). The canonical leaf must make this explicit.

### §5.3 — Step 4 numerical check (mode-count vs Q-factor)

Per Step 4: $Q_{\text{mode},\ell} = \ell$ per Nyquist-cell-resolved mode. At Golden Torus, mode counts per codim:

- 1D: $N_{\text{modes},1D} = \Lambda_{\text{line}} = \pi$. (Each Nyquist cell on the cross-section perimeter contributes 1 mode; total $\pi$ cells in natural units. The mode count is NOT integer because the Nyquist-cell partition of the 1-cycle perimeter is a continuous-mode-envelope limit at the Nyquist resolving floor — the substrate's discrete K4 lattice cannot represent sub-pitch cross-section structure, so the cell count is the substrate's continuous-mode-envelope dimensionless perimeter.)
- 2D: $N_{\text{modes},2D} = \Lambda_{\text{surf}} = \pi^2 \approx 9.87$.
- 3D: $N_{\text{modes},3D} = \Lambda_{\text{vol}} = 4\pi^3 \approx 124.03$.

The continuous-mode-envelope mode counts are NOT integer-valued; this is consistent with the substrate's Ax 1 Nyquist resolving limit being the lower bound (the substrate cannot represent sub-pitch structure, so the cell-count over a sub-manifold IS the dimensionless geometric measure at the substrate's natural resolving floor). Cf. `boundary-observables-m-q-j.md:33` *"Only $\mathcal{M}, \mathcal{Q}, \mathcal{J}$ are externally measurable. Interior eigenmode wavelengths [...] are invisible"* — the Nyquist-cell-count is an external boundary-integral quantity (dimensionless geometric measure of boundary sub-manifolds), not an interior eigenmode wavelength.

### §5.4 — SI translation cross-check

Translating to SI to verify dimensional consistency of the substrate-mechanism derivation:

- $\alpha^{-1}_{\text{ideal}} = 4\pi^3 + \pi^2 + \pi$ is dimensionless in both unit systems (no translation factor)
- $\alpha^{-1}_{\text{CODATA}} = 137.035999$ vs $\alpha^{-1}_{\text{ideal}} = 137.0363038$: relative difference $2.225 \times 10^{-6}$ matches $\delta_{strain}$ (`constants.py:DELTA_STRAIN`); see clm-009nkt for the thermal-running interpretation (Phase 3-A3 target)
- The substrate-mechanism content (Steps 1-5.5) is unit-system-invariant: the dimensionless Nyquist cell count over a sub-manifold is the dimensionless geometric measure in any unit system; the substrate-mechanism derivation does not depend on the unit-system choice.

The natural-unit framing is operationally simpler (so $Z_0 \cdot \omega_C \cdot L_e / (4\pi)$-style factors evaluate to clean dimensionless ratios) but the substrate-mechanism content is identical in SI. Per Grant's intuition: "$\ell_{node} = 1$ in lattice natural, dimensionless, vs. $3.861 \times 10^{-13}$ m" — the SI value is a translation factor for laboratory measurement back-conversion, not a different physical regime.

## §6 — Classification per consistency-vs-emergence v1.2

**Class 2 substrate-mechanism emergence** (master-equation-derivation-path traceable to substrate primitives):

| Axis | Class | Justification |
|---|---|---|
| Substrate-mechanism path | **Class 2 axiom-manifestation** | Steps 1-5.5 trace explicit substrate primitives at every step (Ax 1 Nyquist cell size, Ax 3 Min-reflection / $\Gamma = -1$ TIR boundary, Ax 4 saturation kernel, codimensional Clifford-torus embedding $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$, Nyquist-cell-category independence). Each step is independently canonicalized; no step inserts a free postulate. |
| Numerical value | **Class 4 observable consistency** | The numerical match $4\pi^3 + \pi^2 + \pi \approx 137.0363$ to CODATA $\alpha^{-1} \approx 137.036$ within $\delta_{strain} \approx 2.225 \times 10^{-6}$ is a substrate-prediction-vs-measurement consistency (the substrate predicts the cold-lattice asymptote; CODATA is the warm measurement; $\delta_{strain}$ bridges via thermal correction). This axis is unchanged from prior Phase 3-A2 closure. |

**Discrimination check** (ave-discrimination-check, against SM/QED alternatives):

- **SM/QED counterfactual**: SM/QED predicts no substrate-mechanism origin for $\alpha$; in SM, $\alpha$ is a free parameter measured experimentally. AVE Op21 multi-mode mode-counting at the $\Gamma = -1$ TIR boundary IS the substrate-mechanism origin — the dimensionless geometric measures of the three Clifford-torus codimensional sub-manifolds at the substrate-derived Golden Torus geometry. The substrate-mechanism content has no SM/QED analog at the foundational level.
- **Interpretive alternative**: One could try to interpret the three-Λ sum as a coincidence of three dimensionless quantities. The substrate-mechanism derivation rules this out: the three contributions are derived independently from Ax 1 + Ax 3 + Ax 4 + Clifford-torus embedding + spinor half-cover; the sum is forced by codimensional independence, not assembled post-hoc.

**Independence check** (`ave-independence-check`):

- Step 1 (Ax 1 Nyquist) is independent of Step 2 (Ax 3 Min-reflection): the Nyquist cell size $\ell_{node} = 1$ is a substrate-topology primitive; the $\Gamma = -1$ saturation boundary is a substrate-dynamics primitive at $V_{yield}$.
- Step 3 (per-cycle leak fraction $1/\ell$) follows from Steps 1+2 + curvature radiation at the boundary; no new independent primitive.
- Step 4 ($Q = \ell$) is the algebraic consequence of Step 3 + the standard Q-factor definition; no new primitive.
- Step 5 (mode-count = Nyquist-cell-count = dimensionless geometric measure) requires the Clifford-torus codimensional embedding (canonical at `ch8-alpha-golden-torus.md` + `boundary-observables-m-q-j.md`) AS A SEPARATE substrate-topology input; this is canonicalized + does not double-count Steps 1-4.
- Step 5.5 (codimensional independence) is the substrate-Nyquist-cell-partition property; it does not reintroduce a Schur-orthogonality assumption (which Phase 3-A2 walked back).

Steps are mutually independent at the substrate-primitive level; no circularity, no double-counting.

## §7 — Phase-space-coordinate discipline (phase-space-coordinate-check)

Per skill: Op21 mode-counting operates at the **substrate Nyquist-cell-category coordinate** (codimensional cell counts at saturation boundary, dimensionless geometric measures). The Golden Torus geometry $(R, r, d)$ is in **substrate-real-space coordinates** (lattice-pitch units, $\ell_{node} = 1$). The Clifford-torus embedding $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ is the **phase-space embedding** of the K4-bond-pair LC-tank phasor space (per `electron-identification.md:23`).

**Three coordinate systems active**:
1. Substrate-real-space lattice coordinates (K4 lattice, $\ell_{node}$ pitch units)
2. K4-bond-pair LC-tank phasor space ($V_{inc}, V_{ref}$ pair phasor coordinates, where (p,q) winding labels live)
3. Phase-space Clifford-torus $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ (winding-index coordinates on the bond-pair LC-tank phasor space)

**Op21 mode-counting bridges coordinates 1 and 3**: the substrate Nyquist cell count in coordinate (1) at the $\Gamma = -1$ saturation boundary equals the dimensionless geometric measure of the codimensional sub-manifold in coordinate (3) when (3) is evaluated at the substrate-derived Golden Torus geometry. The bridge is the lattice-natural-unit identity that makes the K4 lattice pitch the natural-cardinality unit for the phase-space Clifford-torus dimensionless geometric measures.

**The Phase 3-A4 derivation is coordinate-clean**: each substrate primitive is named in its native coordinate, and the bridges are explicit (Step 5b: Nyquist cell count over codim-$k$ sub-manifold; Step 5d: that count IS the dimensionless geometric measure $\Lambda_k$).

## §8 — Honest pre-registration of expected outcomes

**PASS (~60% probability)**:
- Op21 multi-mode mode-counting derived end-to-end from Ax 1 + Ax 3 + codimensional independence in lattice-natural units
- Substrate-mechanical reason for $\Lambda_{\text{line}} = \pi$ (NOT $\pi\varphi$) explicit and traceable to regime (b) self-avoidance making $d$ a diameter
- A/B/C reconciliation resolved per §3 (Answer (C) with refinement: $Q = \ell$ substrate-foundational; Bardeen $1/\ln(Z_1/Z_0)$ BCS-specialization)
- $Q_i = \Lambda_i$ identification derived from substrate Nyquist-cell-counting at $\Gamma = -1$ boundary, NOT asserted as natural-unit convention; closes `vol4/claim-quality.md:1209` strengthen-by item
- clm-0ktpcn confidence 0.60 → 0.65 with documented strengthen-by closure
- Cascade through 21+ dependents via `make refresh-kb-metadata`

**PARTIAL (~25% probability)**:
- Mode-counting derived but Step 4 (per-cycle leak fraction $1/\ell$ at finite-wavelength curvature mismatch with TIR boundary) lacks rigorous substrate-mechanical justification beyond the BH-ringdown analogy
- Or: codimensional independence at saturation boundary is qualitatively explained but not rigorously demonstrated for the Clifford-torus codimensional partition specifically
- Document honestly; flag gap; partial lift 0.60 → 0.62-0.63

**WALK-BACK (~15% probability)**:
- The $\Lambda_{\text{line}} = \pi$ normalization isn't substrate-mechanically derivable from current axioms (e.g., the regime (b) diameter convention conflicts with the Nyquist-cell-count framing in a way not anticipated here)
- Or: the Vol 1 Ch 6 §1.21 Bardeen specialization can't be cleanly reframed without amending `operators.md:61` annotation (which is in scope per `ave-walk-back` v1.1 Type B)
- Document honestly; trigger Type B walk-back propagation; do NOT force a derivation that doesn't close

## §9 — Deliverables

1. **This prereg** at `research/2026-05-27_clm-0ktpcn-phase-3-A4-op21-formalization-prereg.md`
2. **Result doc** at `research/2026-05-27_clm-0ktpcn-phase-3-A4-op21-formalization-result.md`
3. **Canonical leaf** at `manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md` (per prework brief recommended location)
4. **Cross-links**:
   - From `theorem-3-1-q-factor.md` §Op21 paragraph (line ~103) → new canonical leaf (Primary)
   - From `operators.md:61` Op21 row annotation → new canonical leaf + reconciliation resolution
   - From `ch8-alpha-golden-torus.md:117` Op21 substrate-mechanism path → new canonical leaf
   - From `qnm-quality-factor.md`, `regime-eigenvalue-method.md`, `knot-mode-isomorphism.md`, `axiom-coverage-audit.md` → new canonical leaf as cross-scale substrate-foundational anchor
5. **clm-0ktpcn entry update** at `vol1/claim-quality.md`:
   - Confidence 0.60 → 0.65 (PASS) with rationale append + new commit-date breadcrumb
   - Close the "Promote the Op21 multi-mode generalization [...] to a fully-derived canonical leaf" strengthen-by item
   - Preserve δ_strain (Phase 3-A3) + speculative $T = A_4$ (Phase 3-A5) items
6. **clm-rtdmsn entry update** at `vol4/claim-quality.md`:
   - Close the "Derive the $Q_i = \Lambda_i$ identification (geometric volume → reactance) from the substrate impedance scaling rather than asserting it as a natural-unit convention" strengthen-by item
   - clm-rtdmsn confidence stays at 0.85 (already at high band; cleanup of strengthen-by item only)
7. **`make refresh-kb-metadata` + `make verify-kb-metadata` PASS** pre-push; verify cascade through 21+ dependents
8. **Commits**: separate prereg / derivation-result / leaf / entry-update / cross-ref pattern per prework brief

## §10 — Skill firings summary

| Skill | Version | Where fired |
|---|---|---|
| ave-prereg | v1.1 | §5 Step 3.5 dim-analysis at canonical primitives (this doc) |
| ave-canonical-leaf-pull | v1.3 | §2 vocabulary-broadened pre-survey (substrate-native + standard-physics wedges; 12 canonical anchors surfaced) |
| ave-analytical-tool-selection | — | §4 Mode class (Q-factor / mode-counting; canonical at `ave-analytical-toolkit-index.md`) |
| ave-discipline-translate | v1.1 Trigger 6 | §3 + §4 substrate-native vocabulary primary throughout ("substrate Op21 mode-counting", "$\Gamma = -1$ TIR boundary"); standard-physics names ("BCS", "Bardeen mapping", "cavity Q") only as parenthetical translation refs |
| substrate-native-check | — | §4 derivation chain walks K4 + Cosserat + Ax 1 + Ax 3 substrate structure before deriving Op21 |
| consistency-vs-emergence | v1.2 | §6 Class 2 substrate-mechanism + Class 4 observable consistency dual-axis classification with master-equation-derivation-path tracing |
| phase-space-coordinate-check | — | §7 three coordinate systems separated; Op21 bridges substrate-real-space and phase-space-Clifford-torus |
| ave-evidence-framing-discipline | — | §8 honest closure-probability framing; PASS/PARTIAL/WALK-BACK criteria |
| ave-canonical-source | — | §5.1 native-unit table imports canonical constants from `src/ave/core/constants.py`; no hard-coded values |
| ave-walk-back | v1.1 Type B | §3 reconciliation requires `operators.md:61` annotation amendment to reflect Op21-foundational + BCS-specialization framing |
| verify-before-cite | v1.4 | §2 every canonical anchor grep-verified (12 sites enumerated with file:line) |
| ave-discrimination-check | — | §6 SM/QED counterfactual + interpretive-alternatives surfaced |
| ave-independence-check | — | §6 step independence verified (no circular dependency between Ax 1 / Ax 3 / Clifford-torus embedding inputs) |

## §11 — Open Grant adjudication question (if PASS doesn't close)

Per Rule 11 (honest closure): if §4 Step 5 (Nyquist-cell-count = dimensionless geometric measure at saturation boundary) is found to require an additional substrate primitive not in {Ax 1, Ax 3, Ax 4, Clifford-torus codimensional embedding}, surface to Grant adjudication BEFORE forcing a closure. The most-likely-stuck sub-question would be: *"is the saturation-boundary Nyquist cell partition over a sub-manifold of the Clifford-torus embedding fully derivable from Ax 1 (lattice Nyquist) alone, or does it require an additional substrate primitive about how the K4 lattice's discrete cell structure projects onto the phase-space Clifford-torus codimensional sub-manifolds?"*

If the answer requires a new primitive, this becomes a Phase 3-A4 PARTIAL result + an open framework-extension candidate.

**Currently expected**: the Clifford-torus codimensional embedding is itself canonical at `ch8-alpha-golden-torus.md:97-108` + `boundary-observables-m-q-j.md` §"The fine-structure constant as electron-scale $\mathcal{M} + \mathcal{J} + \mathcal{Q}$", so the embedding is an input the derivation reads from canonical content; no new primitive needed.

---

End of prereg.

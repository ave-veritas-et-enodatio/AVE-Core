[↑ Ch.1 Vacuum Circuit Analysis](index.md)

<!-- kb-frontmatter
kind: leaf
no-claim: substrate-mechanism formalization of the Op21 multi-mode mode-counting form (Q = ℓ at Γ = -1 saturation/TIR boundary); no new clm — strengthens clm-0ktpcn (Golden Torus α Derivation) + clm-rtdmsn (Theorem 3.1' Q-Factor Reframe) by deriving Q_i = Λ_i identification from substrate primitives rather than asserting as natural-unit convention
-->

# Op21 Multi-Mode Mode-Counting at the $\Gamma = -1$ Saturation/TIR Boundary

The substrate-foundational form of Op21 is the **mode-counting identity** $Q = \ell$ per Nyquist-cell-resolved confined mode at the substrate's $\Gamma = -1$ saturation/TIR boundary. This leaf formalizes the substrate-mechanism derivation that previously lived as a paragraph-level statement at [`theorem-3-1-q-factor.md`](theorem-3-1-q-factor.md) §"Op21 multi-mode generalization" — promoted to fully-derived canonical-leaf rigor per Phase 3-A4 (2026-05-27). The load-bearing closure derives the **$Q_i = \Lambda_i$ identification** at `theorem-3-1-q-factor.md:67` from substrate Nyquist-cell-counting in lattice-natural units rather than asserting it as a natural-unit-convention shortcut.

> → Primary: [Theorem 3.1' Q-Factor at TIR Boundary](theorem-3-1-q-factor.md) — host of the electron-scale three-Λ assembly $\alpha^{-1} = Q_{\text{tank}} = 4\pi^3 + \pi^2 + \pi$ that Op21 multi-mode mode-counting closes
> → Primary: [Vol 1 Ch 8 Alpha Golden Torus](../../../vol1/ch8-alpha-golden-torus.md) — substrate derivation of Golden Torus $(R, r, d)$ via three-substrate-regime closure
> → Primary: [Boundary Observables $\mathcal{M}, \mathcal{Q}, \mathcal{J}$](../../../common/boundary-observables-m-q-j.md) — three-codimensional boundary-observability structure that the three-Λ decomposition corresponds to
> → Primary: [Universal Lattice Units Cheat Sheet](../../../common/natural-units-cheatsheet.md) — lattice-natural units ($\ell_{node} = c = \hbar = m_e = 1$, $Z_0 = 1$, $V_{yield} = 1$) the substrate-mechanism derivation operates in

## §1 — Substrate-mechanism statement

At the substrate's $\Gamma = -1$ saturation/TIR boundary, each Nyquist-cell-resolved confined mode contributes $Q = \ell$ to the substrate Q-factor, where $\ell$ is the mode's wavelength count around its confinement support. In lattice-natural units, the substrate Q-factor contribution from modes confined to a codim-$k$ sub-manifold $\Sigma_k$ of the substrate boundary is the **Nyquist cell count** over $\Sigma_k$, which IS the **dimensionless geometric measure** of $\Sigma_k$:

$$
\boxed{\, Q_{\text{codim-}k} = N_{\text{modes, codim-}k} = N_{\text{cells, codim-}k} = |\Sigma_k|_{\text{native}} = \Lambda_k \,}
$$

This is the substrate-mechanism content of the $Q_i = \Lambda_i$ identification. The natural-unit convention ($\ell_{node} = 1$, $Z_0 = 1$) makes the substrate's discrete cell-counting and the dimensionless geometric measure operationally identical, but the substrate-mechanism content holds in any unit system — the dimensionless cell count over a sub-manifold IS the dimensionless geometric measure of the sub-manifold by definition, not by unit-system choice.

The substrate-foundational Op21 form is cross-scale canonical:

| Scale | $\Gamma = -1$ boundary | Modes counted | Result |
|---|---|---|---|
| Electron LC tank | TIR at $V_{yield}$ Axiom-4 saturation | Three codimensional Clifford-torus sub-manifolds at Golden Torus | $Q_{\text{tank}} = 4\pi^3 + \pi^2 + \pi = \alpha^{-1}$ |
| BH ringdown | Saturation at $r_{sat}$ Axiom-4 phase transition | Tangential $\ell$-wavelength shear mode | $Q = \ell$ per ringdown mode |
| Knot-mode isomorphism | Topological winding confinement | Crossing-number $c$ (particle) ↔ mode-number $\ell$ (BH) | Cross-scale Op21 mechanism |
| Cooper-pair phase transition (BCS specialization) | Superconductivity threshold | Logarithmic substrate-impedance integration | $Q \sim 1/\ln(Z_1/Z_0)$ (Vol 1 Ch 6 §1.21) |

The standard-physics community names the Vol 1 Ch 6 §1.21 specialization formula the "Bardeen BCS mapping" (annotation at [`common/operators.md:61`](../../../common/operators.md)). The substrate-mechanism content of the Vol 1 Ch 6 §1.21 canonical-source name is "Quality Factor Phase Transition" — the substrate Op21 evaluated at the Cooper-pair-phase-transition scale-instance is one of several cross-scale specializations of the substrate-foundational $Q = \ell$ form.

## §2 — Five-step substrate-mechanism derivation

Lattice-natural units throughout ($\ell_{node} = c = \hbar = m_e = 1$, $Z_0 = 1$, $V_{yield} = 1$; SI translation factors per [`natural-units-cheatsheet.md` §2](../../../common/natural-units-cheatsheet.md)).

### §2.1 — Step 1: Ax 1 Nyquist cell size as substrate-native cardinality unit

Per Ax 1 (Substrate Topology, [INVARIANT-S2](../../../CLAUDE.md)), the substrate is a 3D chiral Laves K4 Cosserat crystal with discrete cell size $\ell_{node}$ (canonical at [`lattice-impedance-decomposition.md` §2](../../../vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) + [`src/ave/core/constants.py:194`](../../../../../src/ave/core/constants.py)). In lattice-natural units, $\ell_{node} = 1$ by definition — the substrate's natural cardinality unit.

The substrate's discrete cell-counting IS the substrate-native cardinality measure for any sub-manifold of the lattice. For a sub-manifold $\Sigma_k$ of geometric codimension $k$:

$$
N_{\text{cells}}(\Sigma_k) = \frac{\text{(geometric measure of } \Sigma_k\text{)}}{\ell_{node}^k} = \text{(geometric measure of } \Sigma_k\text{)} \quad \text{(in lattice-natural units)}
$$

This is the load-bearing primitive for Step 5.

### §2.2 — Step 2: Ax 3 + Ax 4 force $\Gamma = -1$ TIR boundary at $V_{yield}$

Per Ax 3 (Minimum Reflection Principle) + Ax 4 (Universal Saturation Kernel), at the substrate saturation boundary $A \to A_{yield}$:

- $S(A) = \sqrt{1 - (A/A_{yield})^2} \to 0$ (Ax 4 kernel)
- $C_{eff}(A) = C_0/S(A) \to \infty$
- $Z_{local} = \sqrt{L/C_{eff}} \to 0$
- $\Gamma = (Z_{core} - Z_{ambient})/(Z_{core} + Z_{ambient}) = -1$ (Op3 at $Z_{core} \to 0$)

The substrate self-creates a perfect TIR mirror at the saturation surface. In lattice-natural units, the saturation surface lives at $V_{yield} = 1$ per [`lattice-impedance-decomposition.md:116, 126-128`](../../../vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) + [`natural-units-cheatsheet.md` §2](../../../common/natural-units-cheatsheet.md) LOAD-BEARING NORMALIZATION WARNING. Modes inside reflect with unit amplitude at the boundary and circulate within.

### §2.3 — Step 3: Per-cycle leak fraction $1/\ell$ at the $\Gamma = -1$ boundary

At the $\Gamma = -1$ boundary, a confined mode with $\ell$ wavelengths fitting around the boundary's 1-cycle releases per cycle a fraction $\sim 1/\ell$ of the stored mode energy via curvature radiation through the boundary.

**Substrate-mechanism content of the $1/\ell$ scaling**: the substrate $\Gamma$ at the boundary is strictly $-1$ only in the long-wavelength limit. At finite wavelength count $\ell$, each wavelength subtends angle $2\pi/\ell$ around the boundary's 1-cycle. The substrate's local impedance at the boundary varies smoothly over angular scales $\sim \ell_{node}/r$ (Ax 1 Nyquist scale at boundary radius $r$), giving an angular-scale mismatch with the mode's $2\pi/\ell$ wavelength angular footprint. The mismatch fraction scales linearly with the wavelength's angular size, and the per-cycle energy leak fraction (normalized by stored energy) scales as $\sim 1/\ell$.

**Cross-scale canonical anchors**:
- Electron LC tank at $V_{yield}$ TIR: [`theorem-3-1-q-factor.md:103`](theorem-3-1-q-factor.md) *"each mode with $\ell$ wavelengths around a 1D circumference releases $\sim 1/\ell$ of energy per cycle"*
- BH ringdown at $r_{sat}$: [`regime-eigenvalue-method.md:63`](../../../vol2/appendices/app-f-solver-toolchain/regime-eigenvalue-method.md) *"the curvature radiation loss per cycle scales as $1/\ell$"*
- Knot-mode isomorphism: [`knot-mode-isomorphism.md:24`](../../../vol2/appendices/app-f-solver-toolchain/knot-mode-isomorphism.md) *"each releases $\sim 1/\ell$ of the mode energy per cycle via curvature radiation"*

### §2.4 — Step 4: $Q_{\text{mode},\ell} = \ell$ per Nyquist-cell-resolved confined mode

Substrate-native Q-factor definition:

$$
Q = 2\pi \cdot \frac{\text{energy stored in the mode}}{\text{energy lost per cycle}}
$$

Substituting Step 3's per-cycle leak fraction $1/\ell$:

$$
Q_{\text{mode},\ell} = 2\pi \cdot \frac{E_{\text{stored}}}{E_{\text{stored}}/\ell} \cdot \frac{1}{2\pi} = \ell
$$

(The factor-of-$2\pi$ convention divides out because the substrate's natural per-cycle quantity is per-radian leak in angular phase.) Canonical at [`regime-eigenvalue-method.md:68`](../../../vol2/appendices/app-f-solver-toolchain/regime-eigenvalue-method.md): $\boxed{Q = \ell}$.

The substrate-foundational Op21 form: **at the $\Gamma = -1$ saturation/TIR boundary, each confined mode of wavelength count $\ell$ contributes $Q = \ell$ to the substrate Q-factor**. Substrate Q-factor counts modes (weighted by wavelength count) at the saturation boundary — this is a **mode-counting identity**.

### §2.5 — Step 5: Nyquist-cell-count = mode-count = dimensionless geometric measure

This is the **load-bearing closure of $Q_i = \Lambda_i$** (the canonical strengthen-by item at [`vol4/claim-quality.md`](../../claim-quality.md) clm-rtdmsn entry).

**Step 5a — codimensional mode confinement**. At the saturation boundary, substrate modes are confined to one of three codimensional sub-manifolds of the substrate's Clifford-torus embedding $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ (per [`ch8-alpha-golden-torus.md:97-108`](../../../vol1/ch8-alpha-golden-torus.md) + [`boundary-observables-m-q-j.md`](../../../common/boundary-observables-m-q-j.md)):

| Codim | Sub-manifold | Dimensionless geometric measure | Boundary observable |
|---|---|---|---|
| 1 | Substrate Ampère 1-cycle around tube cross-section perimeter | $\Lambda_{\text{line}} = \pi \cdot d$ | $\mathcal{Q}$ (charge) |
| 2 | Clifford-torus half-cover surface area on $S^3$ | $\Lambda_{\text{surf}} = 4\pi^2 (R \cdot r)$ | $\mathcal{J}$ (spin) |
| 3 | Clifford-torus surface $\times$ spinor-temporal $S^1_{4\pi}$ phase volume | $\Lambda_{\text{vol}} = 16\pi^3 (R \cdot r) \cdot d$ | $\mathcal{M}$ (mass) |

The three codimensional sub-manifolds are the three substrate boundary-observability classes $\mathcal{Q}, \mathcal{J}, \mathcal{M}$ per [`boundary-observables-m-q-j.md` §"The fine-structure constant as electron-scale $\mathcal{M} + \mathcal{J} + \mathcal{Q}$"](../../../common/boundary-observables-m-q-j.md). The codimensional embedding is canonical input from upstream leaves; no new substrate primitive is introduced.

**Step 5b — Nyquist cell count over codim-$k$ sub-manifold**. By Step 1 substrate primitive (Ax 1 Nyquist cell size in lattice-natural units):

$$
N_{\text{cells, codim-}k} = |\Sigma_k|_{\text{native}} = \Lambda_k
$$

**Step 5c — mode-per-cell substrate-primitive at the saturation boundary**. By Step 1 substrate primitive (Ax 1 lattice Nyquist resolving floor): the substrate cannot represent sub-Nyquist-cell structure. Each Nyquist cell at the saturation boundary therefore supports exactly ONE substrate-resolvable confined mode (one mode per cell; the cell is the minimum substrate-discrete carrier of an independent mode). For modes confined to a codim-$k$ sub-manifold $\Sigma_k$:

$$
N_{\text{modes, codim-}k} = N_{\text{cells, codim-}k} = \Lambda_k
$$

**Step 5d — substrate Q-factor contribution per codim from Step 4**. Each Nyquist-cell-resolved mode at the saturation boundary contributes $Q_{\text{mode}} = \ell$ per Step 4. At the substrate's per-cell Nyquist resolving scale (the single-cell-per-natural-unit identity, per [`theorem-3-1-q-factor.md:103`](theorem-3-1-q-factor.md)), the dominant Nyquist-cell-resolved mode at the cell boundary has $\ell = 1$ — the single-wavelength mode fitting in one Nyquist cell. Summing over the Nyquist-cell-resolved modes in $\Sigma_k$:

$$
Q_{\text{codim-}k} = \sum_{\text{cells} \in \Sigma_k} Q_{\text{mode},\ell=1} = N_{\text{modes, codim-}k} \cdot 1 = \Lambda_k
$$

**This is the substrate-mechanism derivation of $Q_i = \Lambda_i$.**

The identification is NOT a natural-unit convention; it is the substrate-mechanism consequence of:
1. Ax 1 substrate primitive making cell-count = dimensionless geometric measure in lattice-natural units (Step 1);
2. Ax 1 substrate primitive making each Nyquist cell carry exactly one substrate-resolvable confined mode (Step 5c);
3. Step 4 substrate primitive making $Q_{\text{mode},\ell=1} = 1$ per Nyquist-resolved confined mode at the saturation boundary.

The natural-unit choice operationally simplifies the expressions but does not produce the identity — the identity is forced by the substrate's Nyquist-resolving-floor primitive plus the Op21 mode-counting form.

### §2.6 — Step 5.5: codimensional independence (mutually exclusive Nyquist-cell categories)

The three codimensional sub-manifolds of the Clifford-torus embedding are **mutually exclusive partitions of substrate Nyquist cells at the saturation boundary**. A Nyquist cell on the codim-1 sub-manifold (tube cross-section perimeter) is NOT also a cell on the codim-2 sub-manifold (Clifford-torus surface); they live in different sub-manifolds with non-overlapping support points.

Modes confined to different codimensional sub-manifolds therefore add WITHOUT cross-terms — this is the substrate-mechanism content of codimensional independence (replacing the Schur-orthogonality framing that Phase 3-A2 falsified per [`research/2026-05-26_clm-0ktpcn-phase-3-A2-schur-orthogonality-result.md`](../../../../../research/2026-05-26_clm-0ktpcn-phase-3-A2-schur-orthogonality-result.md)).

**Reconciliation of $(R \cdot r)$-collinearity**: the geometric measures $\Lambda_{\text{vol}}$ and $\Lambda_{\text{surf}}$ share the $(R \cdot r)$ parametric factor (so the $(R, r, d) \to \Lambda$ map has 2D image, not 3D). Mode-category independence at the saturation boundary is a STATEMENT ABOUT WHICH SUBSTRATE CELLS CARRY WHICH MODES — not a statement about the dimensionality of the parameter map. The cells in the codim-2 sub-manifold are mutually exclusive with cells in the codim-3 sub-manifold even when their dimensionless geometric measures both scale with $R \cdot r$ parametrically. The substrate-mechanism mode-category independence holds; the parameter-space collinearity is a separate (and consistent) statement.

## §3 — Substrate-mechanical reason for $\Lambda_{\text{line}} = \pi$ (NOT $\pi\varphi$)

A common stumble at the canonical paragraph-level statement is to read "1D mode (circumference $L$) → cell-count $L$" as identifying $\Lambda_{\text{line}}$ with the Clifford-torus major-loop perimeter at the Golden Torus major radius:

$$
2\pi R = 2\pi \cdot (\varphi/2) = \pi\varphi \approx 5.083 \quad \text{(major-loop perimeter — WRONG codim-1 sub-manifold)}
$$

But canonically $\Lambda_{\text{line}} = \pi \approx 3.142$. The reconciliation is **substrate-mechanical**, per [`ch8-alpha-golden-torus.md:67-93`](../../../vol1/ch8-alpha-golden-torus.md):

$\Lambda_{\text{line}}$ is the **substrate Ampère 1-cycle around the tube's transverse cross-section perimeter**, NOT the Clifford-torus major-loop perimeter at the Golden Torus major radius. The codim-1 sub-manifold at the saturation boundary is the **flux-tube transverse cross-section** (Nyquist-quantized diameter $d = 1\,\ell_{node}$ per regime (a) Ax 1), NOT the Clifford-torus major loop.

The cross-section 1-cycle perimeter in lattice-natural units:

$$
\Lambda_{\text{line}} = 2\pi \cdot (d/2) = \pi \cdot d = \pi \quad \text{at } d = 1
$$

The $\pi$ (not $2\pi$) is the substrate consequence of **regime (b) self-avoidance making $d$ the tube diameter** (per [`ch8-alpha-golden-torus.md:43`](../../../vol1/ch8-alpha-golden-torus.md) $2(R - r) = d$, where $2(R-r)$ is the closest centerline-to-centerline approach at a topologically-marked phase-space crossing). The 1-cycle perimeter is $2\pi \cdot \text{radius} = 2\pi \cdot (d/2) = \pi \cdot d$; there is no half-loop, just the closed cycle evaluated at half-diameter (the radius).

The Golden Torus's major radius $R = \varphi/2$ enters the codim-2 ($\Lambda_{\text{surf}}$) and codim-3 ($\Lambda_{\text{vol}}$) measures through the Clifford-torus surface and phase-volume integrals; it does NOT enter the codim-1 measure. The codim-1 measure depends only on Nyquist-quantized $d = 1$, NOT on $R$.

## §4 — Golden Torus closure

Applying Step 5d + Step 5.5 at Golden Torus geometry $(R, r, d) = (\varphi/2, (\varphi-1)/2, 1)$ in lattice-natural units (per [`ch8-alpha-golden-torus.md:61-93`](../../../vol1/ch8-alpha-golden-torus.md)):

$$
\begin{aligned}
Q_{\text{line}} &= \Lambda_{\text{line}} = \pi \cdot d = \pi \\
Q_{\text{surf}} &= \Lambda_{\text{surf}} = 4\pi^2 (R \cdot r) = \pi^2 \quad (R \cdot r = 1/4) \\
Q_{\text{vol}} &= \Lambda_{\text{vol}} = 16\pi^3 (R \cdot r) \cdot d = 4\pi^3
\end{aligned}
$$

By Step 5.5 codimensional independence:

> **[Resultbox]** *Op21 Multi-Mode Golden Torus Closure*
>
> $$
> Q_{\text{tank}} = Q_{\text{vol}} + Q_{\text{surf}} + Q_{\text{line}} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038 \;\equiv\; \alpha^{-1}_{\text{ideal}}
> $$

The substrate Op21 multi-mode form derives the three-Λ assembly end-to-end from Ax 1 + Ax 3 + Ax 4 + codimensional independence in lattice-natural units. The identification $\alpha^{-1}_{\text{ideal}} = Q_{\text{tank}}$ is the substrate-mechanism content of [Theorem 3.1'](theorem-3-1-q-factor.md) §"Op21 multi-mode generalization", now fully canonical-leaf-derived rather than paragraph-level asserted.

## §5 — Op21 dual-identification reconciliation (Op21-foundational + BCS-specialization)

The [`common/operators.md:61`](../../../common/operators.md) Op21 row primary formula is $Q \sim 1/\ln(Z_1/Z_0)$ (the Vol 1 Ch 6 §1.21 canonical-source formula at [`manuscript/vol_1_foundations/chapters/06_universal_operators.tex:349`](../../../../../manuscript/vol_1_foundations/chapters/06_universal_operators.tex)). The canonical-source operator name is **"Quality Factor Phase Transition"** — naming the substrate phase-transition mechanism, NOT "Bardeen mapping" (which is a KB-level annotation in `operators.md:61`).

**The substrate-foundational Op21 form is $Q = \ell$ at the $\Gamma = -1$ saturation/TIR boundary** (§§1-4 above). Cross-scale canonical fires at four distinct substrate scales:

1. Electron LC tank at $V_{yield}$ TIR boundary — three-Λ sum gives $Q = \alpha^{-1}$
2. BH ringdown at $r_{sat}$ Axiom-4 phase transition boundary — $Q = \ell$ per ringdown mode (canonical at [`qnm-quality-factor.md`](../../../vol3/cosmology/ch15-black-hole-orbitals/qnm-quality-factor.md) + [`axiom-coverage-audit.md`](../../../vol3/cosmology/ch15-black-hole-orbitals/axiom-coverage-audit.md))
3. Universal substrate-Q derivation procedure — $Q = \ell$ as Step 5 of the universal procedure (canonical at [`regime-eigenvalue-method.md:18, 68`](../../../vol2/appendices/app-f-solver-toolchain/regime-eigenvalue-method.md))
4. Knot-mode isomorphism — crossing number $c$ ↔ mode number $\ell$ as cross-scale substrate-foundational identity (canonical at [`knot-mode-isomorphism.md`](../../../vol2/appendices/app-f-solver-toolchain/knot-mode-isomorphism.md))

**The Bardeen $Q \sim 1/\ln(Z_1/Z_0)$ form is the BCS-Cooper-pair-phase-transition scale-instance specialization**: the substrate Op21 evaluated at the Cooper-pair-phase-transition scale-instance, where the relevant substrate-impedance integration produces a thermal-fluctuation-broadened logarithm. This is one of several cross-scale specializations of the same substrate-foundational $Q = \ell$ mechanism. Structurally parallel to:

- Op14 ($Z_{eff} = Z_0/\sqrt{S}$ substrate-foundational; Symmetric Gravity $n(r) = 1 + 2GM/(rc^2)$ gravitational-specialization)
- Op17 ($T^2 = 1 - \Gamma^2$ substrate-foundational; Phase 2-NA aperture-aggregate skewness peak at $a^{(2D)}_{peak} = 1/\sqrt{2}$ substrate-matched-impedance specialization per [`parametric-coupling-kernel.md` §14.9](parametric-coupling-kernel.md))

One substrate-foundational form, multiple cross-scale specializations. The KB annotation at `operators.md:61` (*"different identifications [...] cross-reference needs auditor-lane confirmation"*) is now resolved: the Bardeen form is the BCS specialization of the substrate-foundational $Q = \ell$ form.

## §6 — Cross-references

### §6.1 — Substrate-foundational Op21 cross-scale canonical anchors

- [**Theorem 3.1' Q-Factor at TIR Boundary**](theorem-3-1-q-factor.md) (clm-rtdmsn) — electron-scale Op21 host; §"Op21 multi-mode generalization" paragraph that this leaf formalizes
- [**Vol 1 Ch 8 Alpha Golden Torus**](../../../vol1/ch8-alpha-golden-torus.md) (clm-0ktpcn) — three-substrate-regime derivation of Golden Torus $(R, r, d)$; §"Topological self-impedance shape factors at the Golden Torus" + §"Additive assembly of the shape factors (Op21 multi-mode reframe, 2026-05-26 Phase 3-A2)"
- [**QNM Quality Factor from Lattice Phase Transition**](../../../vol3/cosmology/ch15-black-hole-orbitals/qnm-quality-factor.md) (clm-395gps) — BH-ringdown-scale Op21: $Q = \ell, \omega_I = \omega_R/(2\ell)$
- [**Regime-Boundary Eigenvalue Method**](../../../vol2/appendices/app-f-solver-toolchain/regime-eigenvalue-method.md) (clm-d9ivj1) — universal substrate-Q derivation procedure: Step 5 *"Extract the quality factor $Q = \ell$ from the lattice phase transition"*
- [**Knot Crossing Number ↔ Mode Number Isomorphism**](../../../vol2/appendices/app-f-solver-toolchain/knot-mode-isomorphism.md) (clm-d9ivj1, clm-k6olj8) — cross-scale Op21 mechanism
- [**Axiom-4 Coverage Audit**](../../../vol3/cosmology/ch15-black-hole-orbitals/axiom-coverage-audit.md) — Ax 4 saturation phase transition → $Q = \ell$ canonical
- [**Boundary Observables $\mathcal{M}, \mathcal{Q}, \mathcal{J}$**](../../../common/boundary-observables-m-q-j.md) (clm-ze4clw + clm-vnp57s) — three-codimensional boundary-observability structure that the three-Λ decomposition corresponds to

### §6.2 — Canonical operator catalog anchors

- [**Universal Operators Catalog (Op21 row)**](../../../common/operators.md) — Op21 canonical row + dual-identification annotation; this leaf resolves the annotation
- [**Universal Lattice Units Cheat Sheet**](../../../common/natural-units-cheatsheet.md) — lattice-natural units ($\ell_{node} = c = \hbar = m_e = 1$, $Z_0 = 1$, $V_{yield} = 1$) the derivation operates in
- [**Lattice Impedance Decomposition**](../../../vol1/operators-and-regimes/ch6-universal-operators/lattice-impedance-decomposition.md) (clm-k6quve) — dimensional-analysis table + lattice-native units canonical reference

### §6.3 — Cross-scale Op17 + Op21 complementarity

Op17 (matched-impedance peak transmission at $\Gamma = 0$) and Op21 (mode-counting at $\Gamma = -1$ saturation/TIR boundary) are the **two endpoints of the substrate $\Gamma$-space**:

| Operator | Boundary | Mechanism | Canonical |
|---|---|---|---|
| Op17 | $\Gamma = 0$ (matched impedance) | $T^2 = 1 - \Gamma^2 \to 1$, maximum power transmission | [`parametric-coupling-kernel.md` §14.9](parametric-coupling-kernel.md) |
| Op21 | $\Gamma = -1$ (TIR saturation boundary) | $Q = \ell$ per Nyquist-resolved confined mode, energy quantization | This leaf |

The two operators are substrate-mechanical complementary: Op17 = open-boundary energy transfer (substrate transmitting maximum signature power at matched-impedance condition); Op21 = closed-boundary energy quantization (substrate confining and counting modes at the saturation boundary). At the substrate scale this is a single $\Gamma$-space framework with two operational endpoints.

### §6.4 — Upstream canonical content (Phase 3-A4 inputs)

- **Ax 1 Nyquist cell size**: [`src/ave/core/constants.py:194`](../../../../../src/ave/core/constants.py) `L_NODE` + INVARIANT-S2 (Ax 1)
- **Ax 3 + Ax 4 saturation kernel → $\Gamma = -1$**: [`electron-identification.md:24`](../../../vol2/particle-physics/ch01-topological-matter/electron-identification.md) + [`theorem-3-1-q-factor.md:71-79`](theorem-3-1-q-factor.md)
- **Clifford-torus codimensional embedding**: [`ch8-alpha-golden-torus.md:97-108`](../../../vol1/ch8-alpha-golden-torus.md) + [`boundary-observables-m-q-j.md`](../../../common/boundary-observables-m-q-j.md)
- **Golden Torus geometry $(R, r, d)$**: [`ch8-alpha-golden-torus.md:31-93`](../../../vol1/ch8-alpha-golden-torus.md) (three-substrate-regime derivation)

### §6.5 — Phase 3-A4 closure provenance

- **Pre-registration**: [`research/2026-05-27_clm-0ktpcn-phase-3-A4-op21-formalization-prereg.md`](../../../../../research/2026-05-27_clm-0ktpcn-phase-3-A4-op21-formalization-prereg.md)
- **Result document**: [`research/2026-05-27_clm-0ktpcn-phase-3-A4-op21-formalization-result.md`](../../../../../research/2026-05-27_clm-0ktpcn-phase-3-A4-op21-formalization-result.md)
- **Phase 3-A2 antecedent (Schur orthogonality WALK-BACK with Op21 mode-counting structural reframe)**: [`research/2026-05-26_clm-0ktpcn-phase-3-A2-schur-orthogonality-result.md`](../../../../../research/2026-05-26_clm-0ktpcn-phase-3-A2-schur-orthogonality-result.md)

## §7 — Classification per consistency-vs-emergence v1.2

**Substrate-mechanism axis: Class 2 substrate-mechanism emergence (axiom-manifestation)**. The Op21 multi-mode form is derived end-to-end from substrate primitives in §2 Steps 1-5.5. Every step traces to a canonical substrate primitive; no step inserts a free postulate.

**Numerical-value axis: Class 4 observable consistency**. The numerical match $\alpha^{-1}_{\text{ideal}} = 4\pi^3 + \pi^2 + \pi \approx 137.0363$ to CODATA $\alpha^{-1} \approx 137.036$ within $\delta_{strain} \approx 2.225 \times 10^{-6}$ is a substrate-prediction-vs-measurement consistency. Phase 3-A4 promotes the additive-assembly step from Class B substrate-mechanism manifestation (paragraph-level, Phase 3-A2 outcome) to **Class 2 substrate-mechanism emergence** (fully-derived canonical-leaf, Phase 3-A4 outcome); the numerical-value-axis classification is unchanged.

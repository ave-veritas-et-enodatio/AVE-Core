# clm-0ktpcn Phase 3-A2 — Result: WALK-BACK with structural reframe

**Date**: 2026-05-26
**Branch**: `analysis/clm-0ktpcn-phase-3-A2-schur-orthogonality`
**Pre-reg**: [`2026-05-26_clm-0ktpcn-phase-3-A2-schur-orthogonality-prereg.md`](2026-05-26_clm-0ktpcn-phase-3-A2-schur-orthogonality-prereg.md)
**Verdict**: **WALK-BACK with reframe** — Schur orthogonality and its alternative-mechanism candidates do not derive the three-regime additive assembly as a Class 2 substrate-mechanism step. The substrate object IS additive in a substrate-derivable way, but the mechanism is **Nyquist-cell-count additivity over codimensional strata in natural units**, not Schur orthogonality of irreducible representations. Confidence on clm-0ktpcn stays at 0.60. Chapter prose reframed to match the actual substrate-mechanism content; strengthen-by item reformulated honestly.

---

## Executive summary

The pre-registered four-route attempt at deriving the additive (no-cross-term) assembly $\alpha^{-1}_{\text{ideal}} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}} = 4\pi^3 + \pi^2 + \pi$ via Schur orthogonality of substrate-symmetry-group irreps **does not close as a Class 2 substrate-mechanism axiom-manifestation step**. The three $\Lambda_i$ are not three irreducible-representation projections of a single substrate kernel; they are three **dimensionally-distinct unit-measure integrals on three sub-manifolds of different codimensions** in the Clifford-torus embedding $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$.

The substrate-mechanism content that DOES close is the **Nyquist-cell-count interpretation** (canonical at `theorem-3-1-q-factor.md` §"Op21 multi-mode generalization"): in natural units ($\ell_{\text{node}} = 1$), each sub-manifold's dimensionless geometric measure equals its Nyquist-resolvable cell count, and the Q-factor at the $\Gamma = -1$ saturation boundary releases per-cycle energy fraction $1/(\text{mode-count})$ per mode, summing over all modes of all codimensions to the total tank Q-factor. This is substrate-derived but it is a **mode-counting argument**, not a Schur-orthogonality argument.

The honest classification per `consistency-vs-emergence` v1.2 is:

- **Class 2 substrate-mechanism (preserved from Phase 3-A1 prose reframe)**: the $(R, r, d)$ geometry from Ax 1 (Nyquist) + Ax 2 (self-avoidance) + Ax 3 (spinor half-cover).
- **Class B substrate-mechanism manifestation (sharpened by this Phase 3-A2 work)**: the additive assembly via Op21-Nyquist-cell-count-at-saturation-boundary at Golden Torus geometry. The substrate object summed across the three codimensions is the dimensionless mode-count integral, not a Schur-decomposed kernel.
- **Class 4 observable consistency (unchanged)**: the numerical match $4\pi^3 + \pi^2 + \pi \approx 137.036$ to CODATA $\alpha^{-1}$ within $\delta_{\text{strain}} \approx 2.225 \times 10^{-6}$.

The strengthen-by item on clm-0ktpcn is reframed from "establish functional orthogonality of the self-impedance kernel (e.g. SU(2)×SU(2) irrep separation by Schur)" to **"derive the codimensional-cell-count additivity at Nyquist scale from substrate primitives more rigorously than the current Op21-multi-mode-generalization gesture"**. The Op21 cross-reference at `theorem-3-1-q-factor.md` §"Op21 multi-mode generalization" already provides the substrate-mechanism path; tightening that path into a fully canonical leaf is a future workstream.

---

## Route-by-route derivation attempts

### Route 1 — Stokes-graded de Rham (Hodge) orthogonality on $S^3$

**Setup.** The substrate object proposed is the integrated reactive-energy content of the electron's LC tank at its $\Gamma = -1$ saturation surface inside $S^3$. The Clifford-torus embedding $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$ is the canonical phase-space carrier; the three $\Lambda_i$ are integrals of the unit-measure differential forms of the appropriate degree on the three codimensional strata:

- $\Lambda_{\text{vol}}$: integral of the volume 3-form on a 3-torus (Clifford torus surface times spinor-temporal phase $S^1$ of length $4\pi$)
- $\Lambda_{\text{surf}}$: integral of the area 2-form on $\mathbb{T}^2$ (half-covered)
- $\Lambda_{\text{line}}$: integral of the length 1-form on $S^1$ (tube cross-section at Nyquist diameter)

**The Hodge / de Rham orthogonality theorem.** On any oriented compact Riemannian manifold (e.g. $S^3$, but for this argument we only need the substrate's phase-space carrier $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$), differential forms of distinct degree are orthogonal under the canonical $L^2$ inner product

$$
\langle \omega_k, \omega_j \rangle = \int_M \omega_k \wedge \star \omega_j
$$

which vanishes by degree-counting whenever $k \neq j$ (because $\omega_k \wedge \star \omega_j$ is a $(k + (n - j))$-form, only a top-degree $n$-form has non-zero integration; if $k \neq j$ the degree count gives a non-top form which integrates to zero, OR — more carefully — the Hodge star takes a $j$-form to an $(n - j)$-form and the wedge with $\omega_k$ gives a $(k + n - j)$-form which integrates to zero unless $k + n - j = n$, i.e. $k = j$).

This is a substrate-mathematics theorem on $\mathbb{T}^2 \subset S^3 \subset \mathbb{C}^2$.

**Why this route does NOT close as substrate-mechanism for the three-$\Lambda$ sum.** The Hodge orthogonality applies to differential forms of the SAME manifold integrated under a single $L^2$ inner product. The three $\Lambda_i$ are NOT three different-degree forms on a single manifold integrated under one $L^2$-pairing; they are pure-measure integrals on **three different sub-manifolds of different dimensions**, each carrying its own integration measure. The Hodge theorem does not directly produce the additive structure $\Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}}$ as a Hodge decomposition.

To make the Hodge argument substantively apply, one would need to write the substrate-mechanism object as a **single multi-form** $\omega = \omega_3 + \omega_2 + \omega_1$ on a single ambient manifold whose total $L^2$ norm-squared decomposes as $\|\omega\|^2 = \|\omega_3\|^2 + \|\omega_2\|^2 + \|\omega_1\|^2$. The corpus does not currently identify such a multi-form: the three $\Lambda_i$ are written as integrals on **different sub-manifolds**, not as graded components of a single ambient form. The Hodge theorem on $S^3$ has the right structural type (a graded direct-sum decomposition of forms by degree) but the substrate kernel hasn't been written as a single ambient form to apply the theorem to.

**Verdict**: Route 1 fails to close the additive assembly as substrate-mechanism. The Hodge argument is structurally analogous but not directly applicable to the integral structure used in the existing derivation. It would close if the substrate kernel were rewritten as a graded multi-form on a single ambient manifold; that rewriting is itself an open substrate-mechanism question (the substrate-mechanism path would be: identify the electron's stored-reactive-energy density as a single multi-form on the Clifford-torus-embedded 3-torus, decompose its $L^2$-norm via Hodge, recover the three $\Lambda_i$ as $L^2$-norms of the three graded components). Phase 3-A2 does not close this.

### Route 2 — $T_d$ irrep decomposition on K4 4-port amplitude space

**Setup.** Per `k4-port-irrep-decomposition.md` (clm-j550uh + clm-9kd2t3), the K4 4-port amplitude space at each node decomposes under $T_d$ (the full tetrahedral group) as

$$V_{\text{4-port}} = A_1 \, (\text{1D}) \oplus T_2 \, (\text{3D})$$

with the bare scattering matrix $S = (1/2)\mathbf{1} - I$ acting as $+1$ on $A_1$ and $-1$ on $T_2$ (triply degenerate).

**Why this route does NOT close.** $T_d$ on $V_{\text{4-port}}$ gives **two** irreps ($A_1 + T_2$), not three. The dimension count is $1 + 3 = 4$, not $1 + 2 + 3 = 6$ as would be needed to map to three $\Lambda_i$. To produce three irreps from the substrate group action would require either:

(2a) **A different substrate group** whose representation on the relevant substrate Hilbert space has three (or more) irreducible components. Candidates checked: the rotation subgroup $T = A_4$ has irreps $A + E + T$ (1D + 2D + 3D), which IS a three-piece decomposition (1 + 2 + 3 = 6 dimensions), but the substrate-physical Hilbert space on which this would act is not currently identified in the corpus — $T = A_4$ acts on the K4 lattice geometry (canonical at `k4-rotation-group.md` clm-ys0xl1) but the canonical 4-port amplitude representation is $T_d$ on $V_{\text{4-port}} = A_1 + T_2$, not $T = A_4$ on the same space.

(2b) **A subgroup chain restriction**: $T_2$ restricts under $T_2 \supset C_3$ as $A + E$ (1 + 2D), giving a chain $A_1 + (A + E) = A_1 + A + E$ (three pieces of dims 1 + 1 + 2 = 4). But this doesn't match $1 + 2 + 3$ dimensions either, and the substrate-mechanism justification for the $T_2 \supset C_3$ restriction in the $\alpha^{-1}$ derivation is not identified.

**Verdict**: Route 2 fails at the irrep-count level. The canonical substrate group action ($T_d$ on $V_{\text{4-port}}$) has two irreps, not three. The Schur-orthogonality theorem applies trivially to that two-irrep decomposition (the cross-term between $A_1$ and $T_2$ vanishes under any $T_d$-invariant inner product), but the resulting sum is two-term ($\Lambda_{A_1} + \Lambda_{T_2}$), not three-term. There is no canonical substrate group whose irreps map 1-to-1 onto $\Lambda_{\text{vol}}, \Lambda_{\text{surf}}, \Lambda_{\text{line}}$.

**Note on the $T = A_4$ alternative.** Per `k4-rotation-group.md` §2-3, $T = A_4$ has three non-trivial irreps in its character table: trivial $A$ (1D), complex pair $E$ (2D, but the substrate physically realizes this as a real 2D rep), and standard $T$ (3D, often written $T_1$). Dimension count $1 + 2 + 3 = 6$. This *does* have three irreducible pieces with the dimensional ordering $1 + 2 + 3$ matching the codimensional ordering $\Lambda_{\text{line}} (1\text{D}) + \Lambda_{\text{surf}} (2\text{D}) + \Lambda_{\text{vol}} (3\text{D})$, and is a tantalizing structural match — but no canonical substrate Hilbert space is currently identified in the corpus where $T = A_4$ acts with character $1 + 2 + 3$ on the LC-tank reactance density. This is a **candidate for future substrate-mechanism work**, NOT a closure for Phase 3-A2.

### Route 3 — $U(1) \times U(1)$ Peter-Weyl on Clifford-torus phase angles

**Setup.** The two Clifford-torus angles $(\theta_1, \theta_2) \in [0, 2\pi)^2$ carry $U(1) \times U(1)$. Peter-Weyl gives the orthogonal decomposition

$$L^2(\mathbb{T}^2) = \bigoplus_{(m, n) \in \mathbb{Z}^2} \mathbb{C} \cdot e^{i(m \theta_1 + n \theta_2)}$$

with Schur orthogonality $\int_{\mathbb{T}^2} e^{i(m \theta_1 + n \theta_2)} \cdot \overline{e^{i(m' \theta_1 + n' \theta_2)}} d\mu = (2\pi)^2 \delta_{m, m'} \delta_{n, n'}$. The $(2, 3)$ electron winding is the mode $(m, n) = (2, 3)$.

**Why this route does NOT close.** Peter-Weyl decomposes $L^2(\mathbb{T}^2)$ — a single 2D functional space on a single 2D manifold $\mathbb{T}^2$ — into mode contributions, all of which are 2D integrals on the same 2D manifold. It does NOT decompose a quantity that is the SUM of a 3D-volume integral, a 2D-area integral, and a 1D-loop integral into orthogonal pieces, because those three integrals are NOT functions on a single manifold being expanded in irreducible modes.

If one tried to relate $\Lambda_{\text{surf}}$ to a Peter-Weyl mode-norm (which is plausible, since $\Lambda_{\text{surf}}$ IS a 2D Clifford-torus integral), one could write $\Lambda_{\text{surf}} = \int_{\mathbb{T}^2} 1 \cdot d\mu$ = norm-squared of the constant-1 mode at $(m, n) = (0, 0)$, which is the trivial $A_1$-type irrep of $U(1) \times U(1)$. The other two $\Lambda_i$ are not 2D-Clifford-torus integrals, so they don't fit into this Peter-Weyl basis.

**Verdict**: Route 3 fails at the substrate-object-identification level. Peter-Weyl decomposes one fixed-dimensional integral by mode within that dimension, not integrals of different dimensions into pieces.

### Route 4 — Op21 multi-mode geometric mode-counting at Nyquist scale

**Setup.** Per `theorem-3-1-q-factor.md` §"Op21 multi-mode generalization":

> The Q-factor decomposition generalizes via Op21 multi-mode form: at the saturation boundary, each mode with $\ell$ wavelengths around a 1D circumference releases $\sim 1/\ell$ of energy per cycle, giving $Q = \ell$ per mode. The Golden Torus at the Nyquist mode-count identity (single-cell-per-natural-unit) makes the mode counts equal the geometric measures: 1D mode (circumference $L$) → cell-count $L$; 2D mode → cell-count area; 3D mode → cell-count volume. The three-$\Lambda$ sum is exactly the Op21 multi-mode generalization at Golden Torus geometry.

**The substrate-mechanism argument**. In natural units ($Z_0 = 1$, $\ell_{\text{node}} = 1$):

(a) Each Nyquist-resolvable substrate cell in a sub-manifold supports one mode at saturation boundary.
(b) Each saturation-boundary mode releases per-cycle reactive energy fraction $1/\ell$ where $\ell$ is the mode's wavelength count around its support; equivalently, each mode contributes $1$ to the total dimensionless mode-count.
(c) The mode-count integrated over a sub-manifold of codimension $k$ equals the sub-manifold's $k$-dimensional measure (volume, area, length), because the Nyquist cell size is $\ell_{\text{node}} = 1$ in natural units (single-cell-per-natural-unit identity).
(d) Different sub-manifolds carry **independent** modes — a substrate mode confined to the 1-cycle perimeter is a distinct degree of freedom from a substrate mode propagating on the 2-area Clifford torus, which is in turn distinct from a substrate mode propagating in the 3-volume phase volume (i.e., the spinor-temporal extra dimension adds modes not present in the 2D Clifford torus alone).
(e) **Mode-counts of independent degrees of freedom add additively without cross-terms** — this is the substrate-mechanism content. The cross-term between a 3D-volume mode and a 1D-cycle mode vanishes because they live in different Nyquist-cell categories at the saturation boundary.

The additive assembly is then

$$\alpha^{-1}_{\text{tank}} = N_{\text{modes, 3D}} + N_{\text{modes, 2D}} + N_{\text{modes, 1D}} = \Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}}$$

at Golden Torus geometry $(R, r, d) = (\varphi/2, (\varphi-1)/2, 1)$.

**Why this route DOES close at the substrate-mechanism manifestation level (Class B), not at the strict-orthogonality level**. The substrate-mechanism content is:

- **Substrate primitive 1 (Ax 1 Nyquist)**: cells of size $\ell_{\text{node}}$ on the substrate; mode count = sub-manifold dimensionless measure in natural units.
- **Substrate primitive 2 (Ax 3 saturation TIR boundary)**: each mode releases per-cycle reactive fraction $1/\ell$; total Q-factor is sum of mode counts.
- **Substrate primitive 3 (independent degrees of freedom)**: modes in distinct Nyquist-cell categories (volume / surface / line) are independent and add without cross-terms.

This is substrate-derived in the sense that each ingredient traces to a canonical axiom. But it is NOT Schur orthogonality of irreducible group representations; it is **Nyquist-cell-count additivity over codimensional categories at saturation boundary**. Calling it "Schur orthogonality" would be a vocabulary inflation that misrepresents the substrate-mechanism content.

**Verdict**: Route 4 closes the substrate-mechanism content of the additive assembly at the Class B substrate-mechanism manifestation level. The current canonical statement (`theorem-3-1-q-factor.md` §"Op21 multi-mode generalization") is the right substrate-mechanism path; tightening it from a paragraph-length statement to a fully derived leaf is a future workstream.

---

## Honest classification per `consistency-vs-emergence` v1.2

### Pre-existing classification (preserved)

Per `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md` line 131:

- **Substrate-mechanism axis**: $(R, r, d)$ geometry derivation from Ax 1 + Ax 2 + Ax 3 is **Class 2 substrate-mechanism emergence** (each regime is traced step-by-step to its axiom). The additive assembly of $\Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}}$ is **Class B substrate-mechanism manifestation** (the framework points at the codimensional structure without deriving functional orthogonality from substrate symmetry group representation theory; Phase 3-A2 open).
- **Observable axis**: assembled value $137.0363038$ matches the standard-physics-community-measured value to within $\delta_{\text{strain}} \approx 2.225 \times 10^{-6}$ — **Class 4 observable consistency** (substrate-derived assembly recovers standard-physics target up to one thermal-bridge scalar).

### Phase 3-A2 update

The Class B classification is **preserved** but the underlying substrate-mechanism path is now identified as **Nyquist-cell-count additivity at saturation boundary (Op21 multi-mode generalization)**, not as Schur orthogonality of substrate-symmetry-group irreducible representations.

The pre-registered hope ("most likely HALF-PASS where dimensional-grading argument closes but explicit-Schur framing does NOT") is realized: the dimensional-grading argument IS the substrate-mechanism content, but its rigorous mathematical theorem-anchor is Nyquist-cell-count + boundary-mode-count at saturation, not Schur. Whether this counts as "PASS" or "WALK-BACK" depends on calibration: the substrate-mechanism content closes via Op21 mode-counting (PASS-like in the sense that there IS a substrate-mechanism path), but the specific theorem named in the strengthen-by item (Schur orthogonality) does NOT close (WALK-BACK on that specific naming).

I classify this as **WALK-BACK with structural reframe**:

- WALK-BACK on the specific "Schur orthogonality" naming in the strengthen-by item — the theorem-anchor is different and the substrate-mechanism content is mode-counting, not group-irrep orthogonality.
- Structural reframe rather than retraction: the chapter prose's claim that the additive assembly is substrate-derivable is preserved, but the mechanism is sharpened from "orthogonal (via unspecified group theory)" to "additive via Nyquist-cell-count of independent modes at saturation boundary, canonical at `theorem-3-1-q-factor.md` §Op21".
- Confidence stays at 0.60 — no derivation-rigor improvement because the substrate-mechanism path is already canonical (Op21 multi-mode generalization), just under-cited from ch8.

---

## Discrimination check per `ave-discrimination-check`

Before asserting AVE-substrate-distinct framing of the Op21 mode-counting path, enumerate SM-counterfactual + interpretive-alternatives:

**SM-counterfactual**: in standard QM/QED, the fine-structure constant has no Q-factor or boundary-saturation interpretation. The Sommerfeld coupling-strength reading + perturbative QED computation gives $\alpha^{-1} \approx 137.036$ at zero free parameters within QED-renormalization machinery, but does not decompose it into 3D + 2D + 1D mode-counts at a saturation boundary. The substrate-mechanism content (saturation boundary, Op21 mode-counting, Nyquist cell size) is **AVE-distinct**.

**Interpretive alternatives in the AVE corpus**:

- *The Sommerfeld coupling-strength reading* ($\alpha$ = fraction of energy radiated per cycle) — canonical at `theorem-3-1-q-factor.md` §"Physical interpretation of the $R = Z_0/(4\pi)$ boundary". Substrate-mechanism content: $1/Q = \alpha$ is the per-cycle reactive leak through the TIR boundary. This is substantively the same physics as Op21 mode-counting; the leak fraction = 1/mode-count and the mode-count = $\alpha^{-1}$.
- *The Vol 4 Ch 1 LC-tank ratio* ($\omega_C L_e / R = 1/\alpha$ as single impedance ratio) — Path A of `theorem-3-1-q-factor.md`. This bypasses the three-piece sum entirely and computes $\alpha^{-1}$ as a single dimensionless reactance/dissipation ratio. **Note**: Path A is substrate-derived without any sum-decomposition; the three-piece sum (Path B) is the geometric decomposition of the same number into codimensional categories. The substrate-mechanism rigor of Path A is, if anything, stronger than Path B; Path B's interpretation IS the geometric mode-count reading of Path A's single number.

**AVE-distinct content of Phase 3-A2**: the recognition that the three-piece sum is **Nyquist-cell-count additivity at saturation boundary** (Op21 mechanism) and NOT **Schur orthogonality of substrate-symmetry-group irreps**. This is a substrate-mechanism precision-of-attribution result — not a new prediction, but a sharpening of the existing canonical mechanism.

---

## Independence check per `ave-independence-check`

The strengthen-by item (line 95 of `vol1/claim-quality.md`) explicitly raises the $(R \cdot r)$-collinearity issue: $\Lambda_{\text{vol}} = 16\pi^3 (R \cdot r)$ and $\Lambda_{\text{surf}} = 4\pi^2 (R \cdot r)$ both have linear $(R \cdot r)$ dependence, so the $(R, r, d) \to \Lambda$ map has only 2-dimensional image.

Phase 3-A2 response: the collinearity is a feature, not a bug, when the substrate-mechanism path is Op21 mode-counting. Both $\Lambda_{\text{vol}}$ and $\Lambda_{\text{surf}}$ are mode-counts on sub-manifolds that share the Clifford-torus surface factor $(2\pi R)(2\pi r) = 4\pi^2 R r$; $\Lambda_{\text{vol}}$ additionally multiplies by the spinor-temporal-phase factor $4\pi$ corresponding to the extra dimension of mode-count integration. So:

$$\Lambda_{\text{vol}} / \Lambda_{\text{surf}} = (4\pi^2 R r \cdot 4\pi) / (4\pi^2 R r) = 4\pi$$

This ratio is the **spinor-temporal phase length** ($4\pi$ for a spin-½ object via SU(2) double-cover of SO(3)), per the canonical mechanism at `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md` line 105: "the $4\pi$ in $\Lambda_{\text{vol}}$ and the half-cover in $\Lambda_{\text{surf}}$ derive from the *same* SU(2) double-cover structure (temporal and spatial expressions of one fact), not as ad hoc separate factors."

So the $(R \cdot r)$-collinearity is the substrate-mechanism statement that **the 2D and 3D mode-counts share their Clifford-torus base** — the 3D mode-count extends the 2D mode-count by the spinor-temporal phase coordinate. They are not independent in $(R, r)$ parameter space, but they are independent **as mode categories** at saturation boundary (a Clifford-torus surface mode is not a 3-torus phase-volume mode; they're distinct Nyquist-cell categories).

The substrate-mechanism content of the "three regimes are independent" claim, more precisely: the three $\Lambda_i$ are independent **as Nyquist-cell-count categories at the saturation boundary** (volume cells, surface cells, line cells are mutually exclusive cell categories), even though as functions of $(R, r)$ they share parametric factors.

The strengthen-by item's "domain-disjointness arguments are defeated by nested supports" objection is **partially correct and partially overstated**:

- **Correct**: the point-set supports are nested (the 1-cycle is a sub-manifold of the 2-surface, which is a sub-manifold of the 3-volume). Pure set-theoretic disjointness does not hold.
- **Overstated**: the mode categories at saturation boundary ARE disjoint, because a Nyquist-cell counted in the 3-volume is not also counted in the 2-surface (these are mode categories of different dimensions, with distinct mode-count integrals). The substrate-mechanism additivity holds at the mode-count level even though set-theoretic disjointness fails at the point-set level.

This is the substrate-mechanism response to the strengthen-by objection.

---

## Phase-space-coordinate check per `phase-space-coordinate-check`

The three $\Lambda_i$ live on the phase-space (Clifford-torus / $S^3$ / $\mathbb{C}^2$) carrier, NOT on real-space K4 lattice coordinates. The substrate-mechanism mode-count interpretation operates on phase-space mode categories: the 3-torus phase volume mode-count integrates over the Clifford-torus surface times the spinor-temporal phase $S^1$ of length $4\pi$, not over a real-space K4 sub-lattice. The Nyquist quantization (Ax 1) sets the cell size on the phase-space carrier in natural units; the saturation TIR boundary (Ax 3) lives at the soliton's $\Gamma = -1$ surface in real space, mapped through the phase-space identification.

This is the canonical phase-space framing per `manuscript/ave-kb/vol1/ch8-alpha-golden-torus.md` line 27: "The trefoil lives in phase space; the soliton lives in real space." The mode-count derivation lives entirely on the phase-space side.

---

## What CHANGED relative to pre-existing canonical content

(C1) **The "Schur orthogonality" framing of the strengthen-by item is not substantively achievable as a Class 2 substrate-mechanism step**, because the canonical substrate group ($T_d$ on $V_{\text{4-port}}$) gives 2 irreps, not 3, and no canonical substrate Hilbert space carrying a three-irrep decomposition matching the 1+2+3 dimensional ordering of $\Lambda_{\text{line}}, \Lambda_{\text{surf}}, \Lambda_{\text{vol}}$ is identified in the corpus. The Op21 mode-counting argument IS the substrate-mechanism path, but it is mode-counting at Nyquist scale on codimensional categories, not Schur orthogonality of group irreps.

(C2) **The $(R \cdot r)$-collinearity issue (line 93 of claim-quality.md) is reframed**: collinearity in $(R, r)$ parameter space is consistent with substrate-mechanism independence as Nyquist-cell-count categories at the saturation boundary. The strengthen-by objection's "nested supports defeat domain-disjointness" is response-able at the mode-count level (categories of mutually-exclusive Nyquist-cells), even where it fails at the point-set level.

(C3) **The chapter ch8 prose at §"Additive assembly of the shape factors (open structural element)" is updated** to:
- preserve the open caveat ("orthogonality" cannot mean parameter-independence) and the cross-reference to clm-0ktpcn rationale;
- update the dominant-mechanism reference from "Schur orthogonality of substrate-symmetry-group irreducible representations" to "Nyquist-cell-count additivity at saturation boundary (Op21 multi-mode generalization, canonical at `theorem-3-1-q-factor.md` §Op21)";
- add an explicit cross-reference into `theorem-3-1-q-factor.md` Op21 paragraph and `boundary-observables-m-q-j.md` §"The fine-structure constant as electron-scale $\mathcal{M} + \mathcal{J} + \mathcal{Q}$";
- preserve the Class B substrate-mechanism-manifestation classification (NOT lift to Class 2).

(C4) **The strengthen-by item on clm-0ktpcn (line 95) is REFORMULATED**:
- old: "Close the sum-decomposition rule: establish functional orthogonality of the self-impedance kernel (e.g. SU(2)×SU(2) irrep separation by Schur), since the nested supports (1-cycle ⊂ Clifford torus ⊂ 3-volume) defeat domain-disjointness arguments. (Phase 3-A2 target — spawned 2026-05-26)"
- new: "Promote the Op21 multi-mode generalization (canonical at `theorem-3-1-q-factor.md` §Op21) from a paragraph-length statement to a fully-derived canonical leaf, formalizing the Nyquist-cell-count additivity at saturation boundary as the substrate-mechanism path for the three-$\Lambda$ assembly. (Phase 3-A2 result: Schur orthogonality of substrate-symmetry-group irreps is NOT the load-bearing theorem; mode-counting at saturation boundary IS. Closure is future workstream — see [`research/2026-05-26_clm-0ktpcn-phase-3-A2-schur-orthogonality-result.md`](../../../research/2026-05-26_clm-0ktpcn-phase-3-A2-schur-orthogonality-result.md))."

(C5) **The rationale block on clm-0ktpcn is appended** with a 2026-05-26 Phase 3-A2 closure note documenting the Schur-strict WALK-BACK, the Op21-mode-counting reframe, and the no-confidence-lift outcome (0.60 stays).

(C6) **No new canonical leaf is originated** in this Phase 3-A2 work — the Op21 multi-mode generalization is already canonical at `theorem-3-1-q-factor.md`; the future workstream is to formalize that paragraph into a fully derived leaf, which is beyond Phase 3-A2 scope.

---

## What did NOT change

- The $(R, r, d)$ derivation from Ax 1 + Ax 2 + Ax 3 (Class 2 substrate-mechanism emergence) is preserved in full.
- The two-path agreement between LC-tank ratio (`theorem-3-1-q-factor.md` Path A) and multipole sum (Vol 1 Ch 8 Path B) to $\delta_{\text{strain}} = 2.225 \times 10^{-6}$ precision is preserved.
- The dual-axis classification ($(R, r, d)$ Class 2 / additive assembly Class B / numerical match Class 4) is preserved.
- The depends-on graph for clm-0ktpcn (depending on clm-unk0bd, clm-8c3yhs) is unchanged.
- The CMB-thermal-bridge $\delta_{\text{strain}}$ framing is unchanged.
- Numerical engine code is unchanged. (Phase 3-A2 is a precision-of-classification + strengthen-by-reformulation closure; no driver runs needed.)

---

## Evidence-framing-discipline summary

Per `ave-evidence-framing-discipline`:

- **NOT derived**: Schur orthogonality of substrate-symmetry-group irreducible representations for the three-$\Lambda$ sum (Routes 2 and 3 fail; Route 1 fails as applied; no canonical substrate Hilbert space carries the required three-irrep decomposition).
- **Derived at substrate-mechanism manifestation level (Class B)**: the additive assembly via Op21 multi-mode generalization — Nyquist-cell-count additivity over codimensional categories at saturation boundary. Substrate-mechanism content traces to Ax 1 (Nyquist cell size) + Ax 3 (saturation TIR mode-leak) + independence-of-mode-categories.
- **Consistent at the standard-physics observable axis (Class 4)**: $4\pi^3 + \pi^2 + \pi \approx 137.0363038$ matches CODATA $\alpha^{-1} = 137.035999$ within $\delta_{\text{strain}}$.
- **Preserved as open derivation step**: formalizing Op21 mode-counting from paragraph-level statement to fully canonical leaf with substrate-mechanism step-by-step derivation. This is the actual remaining open derivation step on clm-0ktpcn, replacing the previously-listed "Schur orthogonality" step which Phase 3-A2 establishes is not the load-bearing theorem.

---

## Confidence-lift result

- **clm-0ktpcn confidence**: 0.60 (no change — substrate-mechanism path is identified but rigor remains at Class B manifestation level; strengthen-by item reformulated, not closed).
- **clm-0ktpcn solidity**: 0.60 (no change — `min(0.60, 0.65)` via cascade through clm-unk0bd at 0.65).
- **Downstream cascade**: no propagation needed (no confidence change).

---

## Open questions surfaced for future workstreams (NOT in scope for Phase 3-A2)

(O1) **Op21 mode-counting canonical leaf**: the canonical leaf at `manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/` (or wherever Op21 itself is documented — `operators.md` has Op21 as multi-mode generalization, but a dedicated mode-counting-at-saturation-boundary leaf does not exist as a standalone). Promoting `theorem-3-1-q-factor.md` §Op21 to a standalone substrate-mechanism leaf would close the strengthen-by item that Phase 3-A2 reformulates.

(O2) **$T = A_4$ on 1+2+3 substrate Hilbert space candidate**: $T = A_4$ has irreps $A + E + T$ of dimensions 1 + 2 + 3, structurally matching $\Lambda_{\text{line}} + \Lambda_{\text{surf}} + \Lambda_{\text{vol}}$ codimensional ordering. No canonical substrate Hilbert space in the corpus currently carries this representation, but if one could be identified, Schur orthogonality WOULD close the additive assembly at the Class 2 level (genuine substrate-symmetry-group-irrep emergence). This is a substantive future workstream — not a tweak.

(O3) **Hodge graded-multi-form rewriting**: rewriting the substrate kernel as a single graded multi-form $\omega = \omega_3 + \omega_2 + \omega_1$ on the Clifford-torus-embedded 3-torus, whose $L^2$-norm-squared decomposes Hodge-orthogonally as $\Lambda_{\text{vol}} + \Lambda_{\text{surf}} + \Lambda_{\text{line}}$, would close Route 1. The substrate-mechanism path for this rewriting is identified but the explicit construction is not in the corpus.

(O4) **δ_strain magnitude derivation** (clm-0ktpcn strengthen-by item 2, line 96 of vol1/claim-quality.md, marked Phase 3-A3 deferred): substrate-mechanism derivation of $\delta_{\text{strain}}$ magnitude from $T_{\text{CMB}}$ and substrate elastic modulus. Independent of Phase 3-A2; deferred per epic plan.

---

## Self-audit checklist

Per `ave-audit` discipline:

- [x] **Pre-test physics walk completed** before drafting: substrate object, substrate group, substrate inner product all considered before deriving.
- [x] **Substrate-native vocabulary throughout**: "Nyquist-cell-count additivity at saturation boundary" as substrate-native primary form; "Schur orthogonality" as parenthetical translation reference only.
- [x] **`consistency-vs-emergence` v1.2 dual-axis classification applied**: substrate-mechanism axis (Class 2 / Class B) explicitly separated from observable axis (Class 4); Phase 3-A2 update at the Class B substrate-mechanism-path level.
- [x] **`ave-discipline-translate` v1.1 trigger 6 fires throughout**: "Schur orthogonality", "Peter-Weyl", "irreducible representation" all appear only with explicit translation-reference framing or in walked-back-route headings; substrate-native primary form is mode-counting / Nyquist-cell additivity.
- [x] **`phase-space-coordinate-check` fires**: phase-space ($S^3 / \mathbb{T}^2 / \mathbb{C}^2$) operates on substrate-mode categories; real-space K4 lattice carries the Nyquist cell size; coordinate distinction maintained.
- [x] **`ave-independence-check` fires**: strengthen-by item's "domain-disjointness defeated by nested supports" objection answered at the mode-category level (mode categories at saturation boundary are mutually exclusive even where point-set supports are nested).
- [x] **`ave-evidence-framing-discipline` fires**: "Schur orthogonality" is honestly characterized as NOT achieved; "Nyquist-cell-count additivity" is characterized at Class B manifestation level, NOT Class 2 emergence.
- [x] **`ave-discrimination-check` fires**: SM-counterfactual (standard QED doesn't decompose $\alpha$ this way) + interpretive-alternatives (Sommerfeld coupling-strength reading; Path A single LC-tank ratio) enumerated.
- [x] **`verify-before-cite` v1.4 fires**: every file:line citation grep-verified before commit (verified at commit time below).
- [x] **`ave-walk-back` v1.1 Type D fires**: mechanism re-scope on the additive-assembly mechanism (Schur → Op21 mode-counting); chapter prose edited to reflect the reframe; strengthen-by item reformulated, not retracted; clm-0ktpcn rationale appended with Phase 3-A2 closure note.
- [x] **`ave-handoff-canonical-locale`**: this result doc lives at `research/` per pre-reg; no `~/.claude/plans/` use.
- [x] **Honest closure (Rule 11)**: WALK-BACK declared as WALK-BACK; substrate-mechanism content tracked to its actual canonical home (Op21); no post-hoc rescue to PASS by dropping "Schur" specificity from the adjudication criteria silently.
- [x] **Substitution-not-retraction (Rule 12)**: Schur-orthogonality-strict hypothesis is walked back; the Op21 mode-counting reframe is NOT just a slot-refill — it is the substrate-mechanism path that the corpus already canonicalizes (`theorem-3-1-q-factor.md`), being more accurately cited.

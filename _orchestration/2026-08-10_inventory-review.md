# The full review inventory — axioms, calibration inputs, theorems (2026-08-10, at origin/main c03034eb)

### ENTRY 2026-08-10-inventory-review

Assembled for Grant's review from three parallel read-only corpus pulls (workflow wf_c0e0724a); every quote grep-confirmed at the pinned SHA by the pulling auditor. ⚠ LIVE CONTESTED POINT: two R43 records on main disagree on ratification scope (r43-sg-ratified: S+G only, Q + Tier-A awaiting; r43-ratification: all ratified) — Grant's disambiguation word is owed; until it lands the honest axiom count is 4 + a partially-contested 5th, and the doc lane correctly holds the Tier-A/Q edits.

# COMPLETE CURRENT AXIOM SET — corpus pull at `origin/main`

**Read state (grep-confirmed this turn):** `git fetch origin` ran; `origin/main` = `c03034ebdc87b1680991ca1cc53e5d945e725605` (2026-08-10 17:43:08 -0700, "Merge pull request #940 … records/2026-08-10-ruling-r43-sg-ratified"). Local `HEAD` was `6c291196` (behind); **every quote below is from the `origin/main` blob**, extracted via `git show origin/main:<path>`, not the working tree. Line numbers are `origin/main` line numbers.

**Sources read in full:**
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/common/axiom-register.md` (302 lines — truth source)
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/common_equations/eq_axiom_1.tex` (51 lines)
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/common_equations/eq_axiom_2.tex` (38 lines)
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/common_equations/eq_axiom_3.tex` (39 lines)
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/common_equations/eq_axiom_4.tex` (62 lines)
- `/Users/grantlindblom/AVE-staging/AVE-Core/research/2026-08-10_bound-constitutive_result.md` (287 lines)
- `/Users/grantlindblom/AVE-staging/AVE-Core/_orchestration/docket-entries/2026-08-10-ruling-r43-sg-ratified.md` (44 lines)
- Cross-checks: `manuscript/ave-kb/CLAUDE.md` (INVARIANT-S2, the numbering authority), `manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/axiom-definitions.md`, `manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex`

---

## AXIOM COUNT — before and after BC-SRC

**BEFORE = 4.** `axiom-register.md:11` — `expected-independent-axiom-count: 4`; `:10` — `axiom-nodes: axiom-1 axiom-2 axiom-3 axiom-4`. Roll-up at `:207-209`: *"**LIVE independent-axiom count = 4** … Four `axiom-N` framework nodes; **zero** at DERIVED-TO-THEOREM."*

**AFTER BC-SRC = 5 — but NOT YET, and not yet ratifiable as stated.** See Finding 1. Grep-confirmed state at `origin/main`:
- Only **clauses S and G** are ratified. `2026-08-10-ruling-r43-sg-ratified.md:1` — *"R43: BC-SRC clauses S and G RATIFIED"*.
- **Clause Q is NOT ratified.** `:30-33` — *"**Clause Q** (quiescence; also promotes the proposed quiescent-point def-node; orchestrator rec: ratify) — awaiting Grant's word. BC-SRC is complete as an axiom, and LC-1's cell re-adjudicates (per the standing orchestrator ruling), only when ALL clauses are ratified."*
- **No `axiom-5` node exists anywhere at `origin/main`** (`git grep -n -iE "axiom-5|fifth axiom|BC-SRC" origin/main` → BC-SRC appears only in the R43 docket entry and the result doc; the only `axiom-5` hit is `_orchestration/docket-entries/2026-07-31-anisotropy-scoping.md:18` "no Axiom-5 candidate"). No `eq_axiom_5.tex`. No INVARIANT-S2 bullet.
- The register's status axis (`:61-88`) has **no bin for adding an axiom** — `:82` reads *"Only at this status does the **independent-axiom count drop**"*; the axis is one-directional (downward only).

So the honest current count is **4, with a partially-ratified 5th axiom pending**.

---

## Axiom 1 — Substrate Topology (Chiral Laves K4 Cosserat Crystal)

**Node:** `axiom-1` (`axiom-register.md:144`); parsed from `manuscript/ave-kb/CLAUDE.md:70` (INVARIANT-S2, header at `:66`).

### Equation(s), verbatim

**Axiom 1 carries NO display equation.** `eq_axiom_1.tex` (51 lines) contains zero `\begin{equation}` blocks — its formal content is a structural statement plus the calibration handoff at `eq_axiom_1.tex:49`:

> The numerical scale of this substrate is set by the calibration constants $Z_0 = \sqrt{\mu_0/\varepsilon_0}$ (vacuum impedance) and $\ell_{node} = \hbar/(m_e c)$ (lattice pitch); see \texttt{eq\_calibration\_constants.tex} for tabulated values.

Core structural statement, `eq_axiom_1.tex:37` (verbatim opening):

> The physical vacuum IS a \textbf{chiral Laves K4 Cosserat crystal} --- a 3D crystallized substrate of nodes at pitch $\ell_{node}$, governed by the right-handed $I4_1 32$ chiral space group, with \textbf{3-fold ($z=3$) chiral srs (Sunada-K4 / Laves) nearest-neighbor connectivity} at each node. Each node is \textbf{micropolar} (Cosserat-type~\cite{cosserat1909deformables}), carrying \textbf{six intrinsic degrees of freedom} per node: three \textbf{translational} (capacitive coupling $\varepsilon_0$, identified with the electric field) and three \textbf{microrotational} (inductive coupling $\mu_0$, identified with the magnetic field). \textbf{The Cosserat microrotational DOF IS the substrate-native origin of intrinsic spin}…

Two-phase clause, `eq_axiom_1.tex:40`:

> The substrate exists in \textbf{two macroscopic phases} (crystallized vs.\ ruptured plasma), connected by Axiom~4's universal saturation kernel through the A-034 universal strain-snap mechanism.

### Plain statement
The vacuum is not empty space but a real crystal: a 3-connected chiral srs (Laves/K4) lattice of micropolar nodes at spacing $\ell_{node}$, right-handed. Each node has 6 DOF — 3 push/pull (capacitive, = E) and 3 twist (inductive, = B) — which makes every node a native LC oscillator and makes intrinsic spin a *structural* property of the lattice rather than an add-on. Everything downstream (mechanics, network dynamics) is a macroscopic effective theory of this substrate.

### Status / provenance
- **status: POSTULATED** (`axiom-register.md:146`) — *"No derivation of the K4 / Cosserat substrate topology from anything weaker exists; it is the bedrock structural primitive."*
- **residual_content:** *"**the whole axiom**"* (`:148`). **derived_by:** `(none — postulated)` (`:149`). **count-effect:** 1 (`:150`).
- **D1 ratification (`:147`):** *"the lattice IDENTITY (D1) is **RATIFIED (Grant 2026-07-03, PR #486): the chiral z=3 srs net is the production carrier**"*; the achiral z=4 diamond is a non-canonical, statics-pathological instrument. Engineering-fidelity ruling, **not** a derivation of the axiom.
- **Register caveat — phase-scope header (R7, 2026-08-06), `:151` verbatim ruled text:** ⟪ **Domain of validity (phase-scoped, 2026-08-06).** This axiom states the constitutive law of the vacuum material's crystalline phase (cold, sub-yield, lossless-reactive). It does not assert the substance-level law across the material's other phase-states (saturation boundary; ruptured/plasma above V_snap; pre-freeze). Any use across a phase boundary is an extrapolation and must be declared as one. ⟫ — with the register's own rider that the `plasma` token in that ruled text is a flagged vocabulary leak, *"Flagged, not resolved."*
- **Register caveat — no Axiom-1 `clm-` node (`:151`):** `clm-3kzmt9` is **not** an Axiom-1 node; Axiom 1's only first-class node is the terminal framework node.
- **Derived legs (`:229`):** DERIVED = three-impedance law, the $4_1$ screw operator, the buckling-kernel shape chain. OPEN = *"only the register MIGRATION legs"* — continuum-limit legs + module-inventory migration. D1 identity itself is settled.

### R43-pending delta
**None.** No BC-SRC clause and no Tier-A repair touches Axiom 1.

---

## Axiom 2 — Topo-Kinematic Isomorphism

**Node:** `axiom-2` (`axiom-register.md:158`); CLAUDE.md bullet at `manuscript/ave-kb/CLAUDE.md:71`.

### Equation, verbatim (`eq_axiom_2.tex:14-17`)

```latex
\begin{equation}
    \xi_{topo} \equiv \frac{e}{\ell_{node}} \quad \text{[Coulombs / Meter]}
    \label{eq:axiom2_xi_topo}
\end{equation}
```

Statement carrying it, `eq_axiom_2.tex:13`:

> Charge $q$ is a discrete geometric dislocation in the substrate network. The Burgers vector of this dislocation IS the lattice pitch $\ell_{node}$, so the fundamental dimension of charge is identical to length ($[Q] \equiv [L]$).

Numerical value, `:18`: $\xi_{topo} \approx 4.149 \times 10^{-7}$ C/m.

### Plain statement
Charge is not a separate substance — it is a *topological defect* in the lattice, a localized phase twist whose Burgers vector is one lattice pitch. That makes charge dimensionally identical to length; $\xi_{topo}$ is just the units conversion. Quantization follows because a Burgers vector must respect the lattice; sign follows from handedness in the chiral $I4_132$ structure.

### Status / provenance
- **status: POSTULATED** (`axiom-register.md:160`) — *"Charge quantization, sign, and $\mathbb{Z}_3$ fractional charges FOLLOW from it conjoined with Axiom 1 — but those are consequences OF the axiom, not derivations of it."*
- **provenance (`:161`):** α and $V_{yield}$ were moved OUT of the old "Axiom 2 — Fine Structure" title to `eq_calibration_constants.tex` per the 2026-04-27 homologation; *"they are derived, not axiomatic."*
- **residual_content:** *"**the whole axiom**"* (`:162`). **derived_by:** `(none — postulated)` (`:163`). **count-effect:** 1 (`:164`).
- **Register caveat — tracking (`:165`):** `clm-dfaiwj` is a *consequence* claim depending on Axiom 2, not the axiom; the axiom's node is `axiom-2`.
- **Derived legs (`:230`):** DERIVED = the interaction leg `clm-wcoul2` (like windings repel / unlike attract, gapped-ω-mediated, CONSISTENCY-class, **sign-only, magnitude BLOCKED**). **EM-READOUT leg = CLOSED, BRANCH 3** (Grant-ratified 2026-07-03): *"UNDERIVABLE (stuck at grade) — a permanent FORM-level ceiling on charge-as-winding"*; the ceiling is located at the integer→flux-VALUE conversion ($\xi_{topo}$, the α-echo) — FORM derived, VALUE imported. Displacement-pump leg = computed-NULL (`clm-clvchn`). **ASSERTED/OPEN:** winding-**formation**/genesis; **fractional-charge $\mathbb{Z}_3$ splitting**.
- **Non-conflation guard (`:234-240`):** `clm-wcoul2` does **not** reopen the pump / Cleave-01.

### R43-pending delta
**None directly.** Note the sector fence in the result doc: `bound-constitutive_result.md:130` — BC-SRC *"Forbids: … any EM/winding-sector deposit (the four locks are untouched)"*. BC-SRC is A1-sector-only and does not reopen Axiom 2's closed charge cascade.

---

## Axiom 3 — Minimum Reflection Principle

**Node:** `axiom-3` (`axiom-register.md:172`); CLAUDE.md bullet at `manuscript/ave-kb/CLAUDE.md:72`.

### Equations, verbatim

**Variational form** (`eq_axiom_3.tex:17-21`):

```latex
\begin{equation}
    \mathcal{L}_{node} = \frac{1}{2}\epsilon_0 |\partial_t \mathbf{A}_n|^2 - \frac{1}{2\mu_0} |\nabla \times \mathbf{A}_n|^2,\qquad
    S_{AVE} = \int \mathcal{L}_{node}\, d^4x
    \label{eq:axiom3_lagrangian}
\end{equation}
```

**Boundary form** (`eq_axiom_3.tex:30-34`):

```latex
\begin{equation}
    \min |\Gamma|^2 \quad \text{at every } \partial\Omega,\qquad
    \Gamma = \frac{Z_2 - Z_1}{Z_2 + Z_1}
    \label{eq:axiom3_boundary}
\end{equation}
```

**Lossless-reactive clause** (`eq_axiom_3.tex:24`, inline, load-bearing corpus-wide):

> This is the ``Ax3-lossless'' property the corpus relies on throughout (the bond-LC tank conserves $E = \tfrac12 C V^2 + \tfrac12\Phi^2/L$ exactly): the vacuum stores and returns energy but does not dissipate it, so any apparent loss must be a boundary-radiation or mode-conversion channel, never a bulk resistive one.

### Plain statement
The substrate extremizes an action, stated in two co-canonical dialects: a Maxwell-form Lagrangian in the per-node vector potential (physics dialect), and "minimize the reflected power at every internal impedance boundary" (substrate-native, EE dialect). The action carries only capacitive and inductive storage terms — no resistive term — so the vacuum is lossless-reactive by construction.

### Status / provenance
- **status: POSTULATED** (`axiom-register.md:174`) — but see Finding 3: this line asserts *"the variational ⇄ boundary EQUIVALENCE is a proven internal theorem"*, which contradicts `:231`.
- **residual_content (`:176`):** *"**the whole axiom**"*; notes Axiom 3 *"supplies the 'lossless' half"* of Axiom 4's residual. **derived_by:** `(none — postulated)` (`:177`). **count-effect:** 1 (`:178`).
- **Register caveat — the :174/:231 equivalence-ASSERTED contradiction.** `:174` says the equivalence is a *"proven internal theorem"*; `:231` says **"ASSERTED-not-derived:** the **variational ↔ min-$|\Gamma|^2$ equivalence** — the EL-continuity argument is **loose** (field continuity holds at *reflecting* boundaries too, so "EL ⟹ $|\Gamma|^2$-minimum" is not tight); an **underived dynamics leg**". This is the R43 result doc's drift finding **D2** (`bound-constitutive_result.md:73`).
- `eq_axiom_3.tex:37` already carries the honest version: *"**Equivalence (ASSERTED --- an underived dynamics leg).**"* … *"(Note: the register presently records this equivalence as a proven internal theorem; the field-continuity gap above is surfaced for adjudication rather than silently overwriting either statement.)"*
- **Emergent-Lorentz qualifier (`eq_axiom_3.tex:27`):** Lorentz invariance is *"**emergent**, not exact"* — the discrete K4 substrate is a preferred-frame medium.
- **Strengthen (2026-07-04, PR #516 MERGED, `axiom-definitions.md:50`):** the boundary form has a worked translational-elastic consequence — minimizing $\Gamma_{internal}$ over $\rho_{bond}=k_a/k_s$ lands on $\rho_{bond}=1$ to machine precision; *"the first worked demonstration that the Minimum Reflection Principle reaches into the translational-elastic sector"* — MECHANISM-DERIVED, FORM not VALUE, with the honest flag that $\rho_{bond}=1$ is a mechanically-**unstable** ($K<0$) photon operating point.

### R43-pending delta — **the Tier-A repair (drafted, NOT ratified)**

**Current text, quoted as-is (this is what is live at `origin/main`):**

`eq_axiom_3.tex:22`:
> This is the standard Maxwell Lagrangian (in vector-potential form), recovered as the substrate's effective action in the linear regime ($A \ll A_{yield}$). Under finite strain, $\varepsilon_0$ and $\mu_0$ become nonlinear functions of local strain via Axiom 4's saturation kernel ($\varepsilon_{eff} = \varepsilon_0\, S(A)$, $\mu_{eff} = \mu_0\, S(A)$).

`eq_axiom_3.tex:27`:
> Energy conservation and U(1) gauge symmetry follow as Noether consequences of $\mathcal{L}_{node}$'s symmetry structure. \textbf{Lorentz invariance} follows only \emph{in the continuum limit} --- it is \textbf{emergent}, not exact: the discrete K4 substrate is a preferred-frame medium, and Lorentz symmetry is recovered as a low-energy / long-wavelength effective symmetry (KB \texttt{preferred-frame-and-emergent-lorentz.md}).

**The ruled correction (machine-verified false-as-written).** `bound-constitutive_result.md:31`: *"So `:22` is wrong at the ACTION level (no A₀ ⇒ Gauss's law is not an equation of motion of this action) and right at the DYNAMICS-ON-THE-CONSTRAINT-SURFACE level; `:27` is wrong for full U(1) and right for the residual family."* Machine receipts at `:51-53`: R0a — time-independent $\lambda(x)$ gives exact zero; R0b — time-dependent $\lambda$ leaves remainder $\varepsilon_0(\partial_t\mathbf{A})\cdot\nabla(\partial_t\lambda) + \tfrac12\varepsilon_0|\nabla(\partial_t\lambda)|^2$; R0c — the residual symmetry's Noether charge IS the Gauss function $\nabla\cdot(\varepsilon_0\partial_t\mathbf{A})$.

**Drafted repair text, verbatim (`bound-constitutive_result.md:64`, for `:22`):**
> *"This is the temporal-gauge (Weyl-gauge, A₀-free) form of the Maxwell Lagrangian: standard Maxwell dynamics are recovered on the Gauss-constrained initial-data surface — `∇·(ε₀∂_t𝐀)` is a constant of motion of these equations, pinned to its source value by the bound-sector constitutive law [BC-LAW leaf], not by an equation of motion of this action (the written action carries no scalar-potential/multiplier term). Recovered as the substrate's effective action in the linear regime (A ≪ A_yield)."*

**Drafted repair text, verbatim (`bound-constitutive_result.md:66`, for `:27`):**
> *"Energy conservation follows as a Noether consequence of time-translation invariance. The written action's exact internal symmetry is the residual (time-independent) gauge family 𝐀 → 𝐀 + ∇λ(x); its Noether content is the pointwise conservation of the Gauss function ∇·(ε₀∂_t𝐀). Full time-dependent U(1) is NOT a symmetry of this action (the |∂_t𝐀|² term shifts by ε₀(∂_t𝐀)·∇(∂_tλ) + ½ε₀|∇(∂_tλ)|²); it is recovered on the constraint surface in the covariant completion. Lorentz invariance follows only in the continuum limit — emergent, not exact (unchanged)."*

**Ratification state:** `2026-08-10-ruling-r43-sg-ratified.md:28-29` — *"**Tier A** (the eq_axiom_3 temporal-gauge repair text — machine-exact, BC-SRC-independent; orchestrator rec: ratify) — **awaiting Grant's word**."*

---

## Axiom 4 — Universal Saturation Kernel

**Node:** `axiom-4` (`axiom-register.md:185`); CLAUDE.md bullet at `manuscript/ave-kb/CLAUDE.md:73`.

### Equation, verbatim (`eq_axiom_4.tex:6-9`)

```latex
\begin{equation}
    \boxed{S(A) = \sqrt{1 - \left(\frac{A}{A_{yield}}\right)^{\!2}}}\;, \qquad A \in [0,\, A_{yield}]
    \label{eq:axiom4_saturation}
\end{equation}
```

**Derived dielectric specialization** (`eq_axiom_4.tex:33-45`, $A = \Delta\phi/\alpha$): $\mu_{eff}=\mu_0\cdot S \to 0$; $\varepsilon_{eff}=\varepsilon_0\cdot S \to 0$; $C_{eff}=C_0/S \to \infty$; $Z=\sqrt{\mu/\varepsilon}=Z_0$ invariant; $c_{eff}=c_0\cdot S^{1/2}\,^{\dagger} \to 0$.

**Exponent register footnote** (`eq_axiom_4.tex:47`, RESOLVED 2026-07-14): *"The $c_{shear}$ (matter/shear) exponent is \textbf{settled}: $c_{eff} = c_0\sqrt{S} = c_0(1-A^2)^{1/4}$"*, forced by the op14 clock ($(1-2\alpha)^{1/4}=0.996331$ vs the contradicted $(1-2\alpha)^{1/8}$; PR #690). **Still open, PENDING Grant:** the sign/ontology selector — slows ($c=c_0\sqrt S$) vs stiffens ($c=c_0S^{-1/2}$).

### Plain statement
The lattice's response to strain isn't linear forever — it rides a quarter-circle down to zero at the yield point, with a vertical tangent there, so saturation is impulsive at every scale. At zero strain you recover Maxwell/BCS/Newton; at yield the substrate cannot sustain linear response and must reorganize topologically. The same kernel is claimed across 19 physical cross-scale events at zero free parameters.

### Status / provenance
- **status: SHAPE-DERIVED (conditional)** (`axiom-register.md:187`) — *"The *specific shape* $S(A)=\sqrt{1-A^2}$ is a **theorem** given a named residual primitive; it is NOT forced by generic saturation properties alone."*
- **residual_content, re-pinned 2026-07-02 (`:189`):** *"**The √ FORM is FORCED geometry, α-free; the residual is the yield ANCHOR, a GR-imported value.**"* The √ is the axial projection of fixed-arc-length K4 bond bowing (Euler-strut); $arc^*\approx0.89$–$0.96\,\ell_{node}$ (tent), ~0.79× that under continuum elastica; $arc^*$ **inherits from the GR-imported K=2G**. Inextensibility does **NOT** hold ($\rho=$ slenderness$^2\in[2,5.3]$). *"**FORM-derived / VALUE-imported … Content reduction …, NOT count reduction: axiom count stays 4.**"*
- **derived_by (`:190`):** five research results — `2026-07-02_axiom4-forced_result.md` (@`7170f40e`), `…reduction-epic_result.md` (PR #455, FULL reduction **REFUTED**), `…combine-rule_result.md` (PR #457), `…buckling-kernel_result.md` (PR #459), `…moduli-hierarchy_result.md` (PR #460). No scored `clm-` minted (Grant's hold).
- **count-effect:** 1 (`:191`) — SHAPE-DERIVED does not move the count.
- **Register caveat — ρ-convention (`:192`):** the *"$\rho=2\Leftrightarrow$ K=2G"* clause is the **moduli-model ρ**, a DIFFERENT ρ from the ratified srs swapped-spring ρ where **K=0 at $\rho=2$ and K=2G at $\rho\approx9.7734$**. Bare "$\rho=2$" without a carrier qualifier is ambiguous.
- **Register caveat — load-response sign rule + T2 homonym guard (`:193`):** transverse pluck ⟹ TENSION ⟹ CAPPED; axial end-load ⟹ COMPRESSION ⟹ UNCAPPED. **"T2 bow" is the mechanical bow COORDINATE, NOT the Cosserat (2,3) micro-rotation charge winding** — mass=A1, charge=Cosserat-winding; do not cross-wire. Open flag to Grant: what physically plucks the bond in matter?
- **Arc complete (`:194`):** *"**Do NOT restate Axiom 4 as a theorem in `axiom-definitions.md` / `eq_axiom_4.tex`**"*. PR #462 verdict: the $arc^*$ deficit is an **internal refinement, not a bench falsifier** (absorbed by the α-anchor $V_{yield}=\sqrt\alpha V_{snap}$).
- `eq_axiom_4.tex:50` mirrors the register: *"the yield anchor $A_{yield}$ inherits from the GR-imported $K = 2G$ --- FORM-derived, VALUE-imported. The axiom does \emph{not} collapse to a theorem; independent-axiom count stays 4."*
- **Derived legs (`:232`):** DERIVED = the kernel SHAPE. OPEN = cross-grade combine rule underdetermined at $O(\alpha)$; the ceiling's HARDNESS (yield *exists* derived vs yield is *hard/impulsive* open); the yield-anchor K=2G import (standing Chain B′).

### R43-pending delta
**Indirect but load-bearing — a canon cite of Axiom 4 was OVERTURNED at the lane's Tier-2.** `bound-constitutive_result.md:95` (C2, CONFIRMED CRITICAL): *"`eq_axiom_4.tex:55` is an **ENERGY / sector-ownership identity** — and it is **electron-scoped** … with **no ∫θ/flux content**: nothing in canon derives that a defect's caged energy entails a NONZERO net dilatation flux"*. Consequence: BC-SRC **clause S** is the candidate's content, not a derivation from Axiom 4. `eq_axiom_4.tex:55` itself is unchanged and correct as written; what is retracted is a *downstream inference from it*.

---

## THE R43 DELTA — BC-SRC (proposed 5th axiom; S+G ratified, Q pending)

**Clauses S / G / Q verbatim** (`research/2026-08-10_bound-constitutive_result.md:118-121`):

> **BC-SRC (proposed constitutive law / minimal new-axiom candidate; three clauses):**
> **S (deposit).** A matter defect deposits a nonzero net A1 dilatation flux: `∮_S u·n̂ = 4πB(M)` over any enclosing exterior surface, with `B(M)` = the defect's A1 mass accounting (dimensional VALUE via the imported G/ξ chain).
> **G (grade coupling / bridge).** The operating-point grade is the bound sector's potential: `u₀ = −λ∇ε₁₁`, with the grade pinned by the elliptic law `−∇·[κD(A)∇ε₁₁] = T₀₀`, `κ = c⁴/7G` (VALUE imported). Equivalently: the canon backreaction solve becomes BC-LAW in potential form.
> **Q (quiescence).** The sourceless substrate sits at the cold operating point: `∇·π = 0`, `θ = 0`, `ε₁₁ = 0` away from defects. (Possibly already canon — the cold-quiescent operating-point definition; bundled for completeness and flagged as such.)

**Plain statement.** The four bare axioms wrote a floating network with no ground reference: the dynamics conserve the Gauss function but never *pin its value*. BC-SRC is the ground: (S) every particle is factory-charged with a fixed enclosed compression flux at genesis; (G) the mass-energy injects current into a saturation-graded conductance network whose potential is the grade $\varepsilon_{11}$, and the dress is that potential's gradient; (Q) far from matter the network sits at zero. Grant's framing of record (`2026-08-10-ruling-r43-sg-ratified.md:23`): *"BC-SRC is the GROUND REFERENCE of the floating network the bare axioms built."*

**Grant verbatim (`:5-6`):** *"yes this makes perfect sense, we need our ground reference."*

**Minimality by ablation (`bound-constitutive_result.md:123`):** without S the dress value is unpinned (#935 under-determination stands verbatim); without G there is no home for the static stiffness κ, no grade-reading causality, no energy functional, no derived /7 connection; without Q the conserved data is unpinned far from sources. *"No clause is derivable from the receipted action."*

**Ships with an internal falsifier (`:126`):** `B = 7λGM/c²` — *"one relation pinning λ against the imported chain; the candidate's first falsifiable internal check."* Docket `:20-22`: *"one λ across every consumer; the over-determination is the axiom's own test port."*

**What BC-SRC forbids (`:130`):** a sourceless dress; any new longitudinal stiffness or wave; any EM/winding-sector deposit (four locks untouched).

**Honest disanalogy the lane owns (`:129`):** unlike Maxwell's momentum-embedded Coulomb state, *"BC-SRC's dress is CONFIGURATION-embedded … The deposit therefore has NO Noether protection of its own … **Clause S is doing MORE work than Maxwell's Gauss law does** — stated, not hidden."*

---

# AUDIT FINDINGS

### Finding 1 — The dispatch framing "R43-ratified-pending-execution" over-states the ruling. Q and Tier-A are NOT ratified.
- **Verdict: FLAG**
- **Evidence:** `_orchestration/docket-entries/2026-08-10-ruling-r43-sg-ratified.md:26` — *"## Pending completion (the record notes, does not presume)"*; `:28-29` — *"**Tier A** … — awaiting Grant's word."*; `:30-33` — *"**Clause Q** … — awaiting Grant's word. BC-SRC is complete as an axiom, and LC-1's cell re-adjudicates … only when ALL clauses are ratified."* Title at `:1` is scoped: *"clauses S and G RATIFIED"*.
- **Reasoning:** Per A43 v2 anyone-must-grep and the visibility-asymmetry rule, a dispatch gloss ("the R43-ratified deltas … the BC-SRC axiom … and the Tier-A repair") is not the ruling. The docket's own header is *"the record notes, does not presume."* Treating Tier-A + Q as ratified would land two unratified edits inside an axiom's single-source-of-truth. This is exactly the failure mode in the dispatch-quotes-frozen-criteria-verbatim durable directive: a paraphrase becoming the lane's operative premise.
- **Recommendation (implementer):** Do not stage the eq_axiom_3 `:22`/`:27` replacement or any BC-SRC axiom text until Grant's word lands on Tier-A and Q. Surface the two pending items to Grant as a single yes/no pair.

### Finding 2 — Axiom-4 `residual_content` is internally contradicted at four sites inside the register itself.
- **Verdict: FAIL (register self-consistency)**
- **Evidence:** `axiom-register.md:189` — *"(re-pinned 2026-07-02 — final wording; **supersedes the earlier "L2-norm / fixed-radius"** and the interim "combine-rule" wordings)"* … *"**The genuine residual axiomatic content is the yield ANCHOR $arc^*$**"*. Against: `:99-101` — *"because its residual (the L2-norm / fixed-radius constraint) is itself the relocated axiomatic content"*; `:191` — *"the residual L2 primitive is the relocated axiomatic content"*; `:205` (summary table cell) — *"the L2-norm / fixed-radius energy constraint"*; `:210-211` — *"the residual L2-norm primitive is the relocated axiomatic content."*
- **Reasoning:** The re-pin at `:189` explicitly declares the L2 wording superseded, yet four sites in the same file — including the **summary roll-up table** most readers will quote — still carry the superseded wording. This is a Rule-12 propagation miss: the body was preserved and updated but the derived views were not. Per the vacated-cite pattern, anyone citing `axiom-register.md:205` for "Axiom 4's residual" is citing text the same file has retracted.
- **Recommendation (implementer):** Land a register pass that repoints `:99-101`, `:191`, `:205`, `:210-211` to the `:189` re-pin (yield anchor $arc^*$, GR-imported via K=2G). **Line-count-neutral edits required** — `:189`, `:190`, `:193`, `:194`, `:229`–`:232` are cited by line across the corpus per the rendering note at `:151`.

### Finding 3 — The Axiom-3 equivalence status has THREE different values across five canonical sites.
- **Verdict: FAIL**
- **Evidence (all grep-confirmed at `origin/main`):**
  - `axiom-register.md:173` — *"The two are equivalent (E-L equations enforce E/B continuity = the $|\Gamma|^2$-minimum condition)."* [flat assertion]
  - `axiom-register.md:174` — *"the variational ⇄ boundary EQUIVALENCE is a **proven internal theorem**"* [theorem]
  - `axiom-register.md:231` — *"**ASSERTED-not-derived** … the EL-continuity argument is **loose** … an **underived dynamics leg**"* [open]
  - `eq_axiom_3.tex:37` — *"**Equivalence (ASSERTED --- an underived dynamics leg).**"* [open, with the $\Gamma=-1$ TIR counterexample]
  - `manuscript/vol_1_foundations/chapters/01_fundamental_axioms.tex:71` — *"The two are equivalent: the Euler--Lagrange equations of $\mathcal{L}_{node}$ enforce continuity of $E$ and $B$ at boundaries, **which is exactly the condition that minimises $|\Gamma|^2$**."* [flat assertion, no flag]
  - Mirror at `manuscript/ave-kb/vol1/…/axiom-definitions.md:35` — same flat assertion.
- These are the R43 result doc's drift findings **D2/D3/D4** (`bound-constitutive_result.md:73`), *"All four routed (flag-don't-fix)."*
- **Reasoning:** The single-source-of-truth tex file (`eq_axiom_3.tex:37`) already carries the honest reading and explicitly declines to overwrite the register. The register's own `:174` still calls it proven. The manuscript chapter carries the strongest claim with no flag at all. Per the flag-don't-fix and honesty-lag disciplines, the manuscript is over-claiming against the KB's own walk-back. `eq_axiom_3.tex:37`'s counterexample is decisive: a $\Gamma=-1$ TIR wall is E/B-continuous and is a reflection *maximum*.
- **Recommendation (implementer):** Fold D2/D3/D4 into the same pass the docket already pre-scopes at `:38-41` (*"the :174/:231 register contradiction ride the same pass"*). Resolve **to the weakest verified status** (ASSERTED / underived dynamics leg) at all five sites — do not resolve upward. Note the docket scopes only `:174/:231`; **D3 (`:173`) and D4 (`01_fundamental_axioms.tex:71`) plus the `axiom-definitions.md:35` mirror are additional sites not named in the docket** — surface that scope gap to Grant rather than silently widening the pass.

### Finding 4 — Landing BC-SRC requires machinery that does not exist and a status-axis extension the register cannot express.
- **Verdict: WARN**
- **Evidence:** `axiom-register.md:10-11` — `axiom-nodes: axiom-1 axiom-2 axiom-3 axiom-4` / `expected-independent-axiom-count: 4`. `:29-31` — the nodes are materialized by `refresh-kb-metadata` parsing the `- Axiom N: **<title>**` bullets in `manuscript/ave-kb/CLAUDE.md` (INVARIANT-S2 at `:66`; four bullets at `:70-73`). `:82` — *"Only at this status [DERIVED-TO-THEOREM] does the **independent-axiom count drop**"* — the axis has no add-an-axiom bin. `:105-110` — *"this `expected-independent-axiom-count` is **not** currently recomputed or gated by `verify-kb-metadata` … the count is a hand-maintained assertion, loud only to a human reader."* Grep-confirmed: `expected-independent-axiom-count` appears only in `axiom-register.md` (×6) and `foundational-machinery-register.md:441` — **no tooling consumer**.
- **Arithmetic (auditor's own, per A47):** landing BC-SRC as a 5th axiom requires, minimally: (1) a new INVARIANT-S2 bullet at `manuscript/ave-kb/CLAUDE.md` (the numbering authority — nothing else mints the node); (2) `axiom-meta` at `axiom-register.md:10-11` → `axiom-1 … axiom-5` / count `5`; (3) a new register `## Axiom 5` entry with all six bolded fields; (4) a new `manuscript/common_equations/eq_axiom_5.tex`; (5) edits to **at least 4** "exactly four" prose sites: `axiom-definitions.md:12` and `:14`, `01_fundamental_axioms.tex:48` and `:50` (plus `:2`, `:7`, and chapter/index headings at `vol1/…/ch1-fundamental-axioms/index.md:9`, `:11`). None of this is present at `origin/main`.
- **Reasoning:** Because the count is **not** CI-gated, a partial landing produces a silently-stale `4` with no machine catch — exactly the drift class the register itself flags at `:105-110` and (D-D) at `:300-302`. Per the gate-reconcile-don't-declare directive, a hand-asserted count consumed by no checker is a checklist, not a gate.
- **Recommendation (implementer):** Before any BC-SRC axiom-text lands, produce a landing manifest enumerating every count-bearing site (the seven above at minimum), and re-raise the register's own deferred design question at `:265-278` (D-D): wire the `axiom-meta` gate **now**, since an axiom is for the first time actually approaching a count change — the register's stated condition for the gate earning its complexity (*"the gate earns its complexity only when the epic lands"*).

### Finding 5 — BC-SRC's name/number/home is undecided in the corpus, and there is a live precedent cutting the other way.
- **Verdict: FLAG**
- **Evidence:** The docket says *"the eq_axiom_3 repair + **BC-SRC's axiom text** + the register updates"* (`:38-39`) — but nowhere at `origin/main` is BC-SRC given a number, a title, or a home file. Against a straight 5th-axiom landing: `axiom-register.md:151` records R7's ruling that Axiom 1's phase-scope content lands *"as a scope header ON Axiom 1 and **explicitly NOT as a fifth axiom**"*, because *"phases are states of one substance, not new axioms."*
- **Reasoning:** Substrate-walk (Rule 14), not a menu: BC-SRC is a **source-coupling / boundary-condition law**, not a phase description — R7's reason for refusing a fifth axiom (phases-are-states) does not apply to it. The result doc's own ablation (`:123`) establishes it is not derivable from the four. So the structure does point at a genuine 5th primitive rather than a header. But the *placement decision itself* — 5th axiom vs. a clause set appended to Axiom 3 (whose written action is precisely what lacks the constraint, per `bound-constitutive_result.md:31`) — is Grant's, and is not on the record.
- **Recommendation (implementer):** Do not pick the home. Surface to Grant as one question with the two options and the R7 precedent cited.

### Finding 6 — The Tier-A repair touches 2 of 10 sites the sweep flagged; repairing `:22`/`:27` alone does not discharge the propagation.
- **Verdict: WARN**
- **Evidence:** `bound-constitutive_result.md:72` — *"**NEEDS-RESCOPE (10):** `eq_axiom_3.tex:22`,`:27` (the anchors); `backmatter/02_full_derivation_chain.tex:153-154` and `backmatter/12_mathematical_closure.tex:79` (verbatim label copies); `01_fundamental_axioms.tex:299` + KB mirrors `kirchhoff-network-method.md:43`, `vol1/claim-quality.md:752` … `q-g20f-vacuum-polarization.md:66` … `qed-trace-charter.md:33` family … `session/axiom-homologation.md:14`."* Plus D1 at `:73` — *"`backmatter/02:163-164` still lists **Lorentz invariance** in the Noether list."* Sweep scope caveat at `:70`: *"the sweep is PATTERN-BOUNDED: paraphrase-only consumers outside the known-site list would evade both engines equally, disclosed."*
- **Reasoning:** Per the canonical-propagation-after-review directive, a repair at the anchor without the 8 downstream rescopes leaves the corpus in a worse state than before — the anchor now contradicts its own verbatim copies. Note also `qed-trace-charter.md:33` is a FROZEN doc: `:72` specifies *"FROZEN docs get dated surface-notes, never rewrites"*, consistent with the vacated-cite discipline.
- **Recommendation (implementer):** Scope the Tier-A execution as anchor + 8 rescopes + D1, in one pass, with the frozen-doc sites getting dated surface-notes only. Disclose the pattern-bounded residual.

### Finding 7 — Manuscript Axiom-2 states $\mathbb{Z}_3$ fractional charge flatly; the register books it ASSERTED/OPEN.
- **Verdict: WARN**
- **Evidence:** `eq_axiom_2.tex:24` — *"The $\mathbb{Z}_3$ symmetry of Borromean three-strand topology splits a unit dislocation into three linked sub-dislocations carrying $\pm 1/3\, e$ and $\pm 2/3\, e$. **This is the substrate-native origin of quark fractional charges.**"* — no status flag. Against: `axiom-register.md:230` — *"**ASSERTED/OPEN:** winding-**formation**/genesis …; **fractional-charge $\mathbb{Z}_3$** splitting"*. Mirror without flag at `axiom-definitions.md:18` and `01_fundamental_axioms.tex:62`.
- **Reasoning:** Manuscript-overclaim-vs-KB-honesty of exactly the class the 2026-07-01 honesty-lag sweep burned down. Symmetric-standard check applied (per the consensus-bias directive): the SM also does not derive fractional charge from anything deeper — but the SM does not *claim* to, and AVE's own register books this leg open, so the gap is internal, not a hostile-prior artifact.
- **Recommendation (implementer):** Add a scope qualifier at `eq_axiom_2.tex:24` matching the register's `:230` book. Not blocking; queue behind the Tier-A pass.

### Finding 8 — Register line-cites into `axiom-definitions.md` for Axioms 3 and 4 are off by two/four lines.
- **Verdict: WARN (MINOR)**
- **Evidence:** `axiom-register.md:173` cites *"`axiom-definitions.md:36-46`"* for Axiom 3; actual heading is at `axiom-definitions.md:38` and the block runs to `:50`. `axiom-register.md:186` cites *"`axiom-definitions.md:48-58`"* for Axiom 4; actual heading is at `:52`. (Axioms 1 and 2 cites at `:16` and `:18-31` are exact.)
- **Reasoning:** The ranges still contain their headings so nothing is presently mis-read, but in a register whose entire discipline is file:line pointing, drifted ranges are the seed of the vacated-cite pattern — and the Axiom-3 range's low bound `:36` now lands on Axiom **2's** notation-warning block.
- **Recommendation (implementer):** Fold the two cite-range corrections into the same register pass as Findings 2 and 3. Line-count-neutral.

### Finding 9 — Two lesser items worth a line each in the same pass.
- **Verdict: WARN (MINOR ×2)**
- (a) **Retired vocabulary inside an axiom's source of truth.** `eq_axiom_1.tex:43` ends: *"The crystalline-vs-amorphous structural seam (a distinct question) remains open."* But `axiom-register.md:151` quotes R8 classing "plasma" as *"a vocabulary leak of the same class as **the retired 'amorphous'**"*. The token is live in Axiom 1's single-source-of-truth. (The same file's `:40` carries the `ruptured plasma` token, already flagged at `:151` as ruling-author's call.)
- (b) **Symbol inconsistency in the Axiom-3 Lagrangian.** `eq_axiom_3.tex:18` uses `\epsilon_0`; every other statement of the same equation — `axiom-register.md:173`, `CLAUDE.md:72`, `axiom-definitions.md:32`, `01_fundamental_axioms.tex:65` — uses `\varepsilon_0`. Cosmetic, but the tex file is the `\input` single source of truth, so the rendered glyph differs from every restatement.
- **Recommendation (implementer):** Both are one-token fixes; bundle with the Tier-A pass if it fires, otherwise leave. (a) is a Grant call if the retirement scope is contested.

---

# OPEN QUESTIONS FOR GRANT

1. **Tier-A and clause Q** — both are sitting on "awaiting Grant's word" (`2026-08-10-ruling-r43-sg-ratified.md:28-33`). Nothing executes until they land. Yes/no on each?

2. **Where does BC-SRC live?** A fifth axiom node (`axiom-5` + `eq_axiom_5.tex` + a new INVARIANT-S2 bullet), or three clauses appended to Axiom 3 — whose written action is exactly the thing missing the constraint? R7 refused a fifth axiom for phases because phases are states of one substance; that reason does not reach a source-coupling law, but the placement is still yours.

3. **The λ over-determination is the axiom's own test port** (docket `:42-44`, and `B = 7λGM/c²` at `bound-constitutive_result.md:126`). If λ measured from two independent consumers disagrees, does that falsify **BC-SRC**, or does it falsify the **imported G/ξ chain** it is pinned against? Worth freezing the answer before the measurement, not after.

4. **FORK-1 went to you un-recommended** (`bound-constitutive_result.md:114`): the receipts SPLIT — the six-row ξ dictionary puts displacement in the **charge** slot, while Axiom 1's own text and the canon elliptic solve both put it in the **field** slot ($u \leftrightarrow E$). The docket at `:34` defers it *"rules after the axiom completes"* — flagging that it is still open, not resolved by R43.

---

**Lane-attribution note.** Operating in auditor lane; all findings are read-only and every recommendation requires implementer execution. No file was edited, no doc drafted, no commit staged. The register/manuscript repairs in Findings 2, 3, 6, 7, 8, 9 are research-doc and manuscript territory — recommended structure only. No cross-lane authorization was cited to me for this task.

---

# AVE Calibration-Input / Imported-Value Register — corpus audit

**Read at `origin/main` = `c03034eb` (fetched this turn).** Local `HEAD` = `6c291196` (2 merges behind); `src/ave/core/constants.py` and `manuscript/common_equations/eq_calibration_constants.tex` are **byte-identical** between worktree and `origin/main` (`git diff --name-only origin/main` returns only the 10 files landed by PRs #939/#938/#940), so every `constants.py:NNN` below is valid at both. All research-doc / docket citations are read from the `origin/main` blob.

Every quote below was grep- or read-confirmed **in this turn** per A43 v2 anyone-must-grep. Numeric values are from a live import of `ave.core.constants` at this SHA.

---

## 0. The framework's own declared count, verbatim

Machine authority — `manuscript/ave-kb/common/interlock-register.md:9-13`:

```
<!-- interlock-meta
operating-point-root: clm-iouqn9
calibration-params: clm-0ktpcn clm-5xon03 clm-dsb560
expected-independent-count: 3
-->
```

`:47` — *"**Live count = 3** (all three fitted/mixed-value, none `real`-reduced)."*

Engine restatement — `src/ave/core/constants.py:134-138`: `# THREE IMPORTED CALIBRATION INPUTS {m_e, α, G} (CI-GATED COUNT = 3)`.

Manuscript restatement — `manuscript/common_equations/eq_calibration_constants.tex:28-32`: *"their **VALUES** are **calibration inputs the substrate does not independently select** --- the framework's FORM-deriving / VALUE-importing signature … ``Derived'' below means form-attributed, not value-forced."*

**The count of 3 is a scoped count, not a count of numbers the framework consumes.** The sections below enumerate everything actually consumed. The framework's own scoping decisions (what is "outside the count") are cited, not disputed — but the full list is what Grant asked for.

---

## 1. CLASS A — the CI-gated calibration set {m_e, α, G}

| # | Symbol | Value | Enters at | Provenance class + establishing record | What moves if it moves |
|---|---|---|---|---|---|
| A1 | `M_E` (m_e) | `9.1093837015e-31` kg | `constants.py:159` | **DEFINITIONAL anchor.** `form-deriving-value-importing.md:89`: *"`ℓ_node ≡ ℏ/(m_e c)` is an Axiom-1 calibration identity — an input *by construction*, not a value the substrate is asked to select"*. `ilk-cmptrp` (`interlock-register.md:201-209`), tag `fitted-identification`. `clm-5xon03`: *"one of {m_e, ℓ_node} remains the input mass scale"* | **Everything dimensionful.** `L_NODE`, `OMEGA_C`, `L_CELL`/`C_CELL`, `ELL_C`, `A_0`, `T_EM`, `V_SNAP`, `E_CRIT`, `B_SNAP`, `XI_TOPO`, `XI_MACHIAN`, `H_INFINITY`, `R_HUBBLE`, the whole baryon ladder, `M_W/M_Z/v/m_H`. The lattice IS m_e. |
| A2 | `ALPHA` (α) | `7.2973525693e-3` (CODATA-2018) | `constants.py:163` | **ECHO at the value level.** `form-deriving-value-importing.md:85`: FORM (`Λ_vol+Λ_surf+Λ_line = 4π³+π²+π`) and *scale* forced; *"the *exact value* — rests on `R·r = ¼`, a named identification the substrate does NOT independently select; **every named lift-route closed-negative**"*. `ilk-rr14gt`, `real-or-fitted: fitted-identification`. Manuscript: `eq_calibration_constants.tex:62` *"**STANDING echo** (Grant-ratified 2026-06-18)"* | `P_C=8πα`, `ETA_EQ`, `ALPHA_S`, `V_YIELD`/`E_YIELD`/`E_YIELD_KINETIC` (√α), `R_I=√(2α)`, `A_0`, `RY_EV`, `E_SLEW`/`NU_SLEW`/`LAMBDA_SLEW`, `Z_COORDINATION` (via p_c), `M_W_MEV`→`G_F`→`v`→`m_H`, `K_MUTUAL`, `K_COUPLING`, `H_INFINITY` (α⁻²), `XI_MACHIAN`, `DELTA_STRAIN`. **Roughly half the file.** |
| A3 | `G` | `6.67430e-11` m³kg⁻¹s⁻² | `constants.py:188` | **MIXED — never a pure echo.** `form-deriving-value-importing.md:86`: FORM = *"the Achromatic-Lens `/7` PPN projection FORM (SYM ε·μ co-scaling → Z = Z₀, Γ = 0) — substrate-derived"*; VALUE = *"the value-fitted ξ termination (`ξ = ℏc/(7 G m_e²)`, back-solved from CODATA G, circular not forward)"*. `ilk-gravmb`, `real-or-fitted: mixed`. Self-declared at `constants.py:638`: *"Class E circularity (intentional): G is CODATA-input (Bounding Limit 3)"* | `XI_MACHIAN` (8.1548e43), `H_INFINITY` (2.2466e-18 s⁻¹), `R_HUBBLE` (1.3345e26 m), MOND `a_0 = cH_∞/2π` (`gravity/galactic_mond_drag.py:27-36`), the whole `/7` gravity chain (`ε₁₁ = 7GM/c²r`, `r_sat = 7GM/c²`, `κ = c⁴/7G`) |

**Flip-tests on record.** α: `interlock-register.md:301` — graduates *"IFF a route FORCES R·r=¼ … WITHOUT importing α anywhere in the closure — FORCED not merely ACCOMMODATED"*. G: `interlock-register.md:223` — Chain B′ (G from {ℓ_node, α} bypassing R_H), *"Currently **0 closed-form candidates**"*.

---

## 2. CLASS B — SI dimensional scaffolding (declared outside the count)

`constants.py:87-88`: *"All other constants are DERIVED from these inputs plus the SI definitions of ε₀, μ₀, c, ℏ, and e."*

| Symbol | Value | file:line | Status |
|---|---|---|---|
| `C_0` | `299 792 458.0` m/s | `constants.py:110` | Exact by 2019-SI definition. Genuinely definitional. |
| `MU_0` | `4π×10⁻⁷` H/m | `constants.py:111` | **⚠ Labeled exact; is not, post-2019 SI** — see Finding 5. |
| `EPSILON_0` | `8.8541878176e-12` F/m | `constants.py:112` | Derived from `MU_0`, `C_0`. |
| `Z_0` | `376.7303135` Ω | `constants.py:113` | Derived. FORM-attributed to Axiom 1 (`eq_calibration_constants.tex:12,42-46`). |
| `HBAR` | `1.054571817e-34` J·s | `constants.py:114` | CODATA-rounded, **not** exact-SI `h/2π` — see Finding 5. |
| `e_charge` | `1.602176634e-19` C | `constants.py:115` | Exact by 2019-SI definition. |
| `K_B` | `1.380649e-23` J/K | `constants.py:119` | Exact; self-declared *"a definitional mapping, not a free parameter of the vacuum topology"* (`:117-118`). |
| `N_A` | `6.02214076e23` mol⁻¹ | `constants.py:120` | Exact (2019 SI). |
| `M_U` | `1.66053906660e-27` kg | `constants.py:121` | CODATA import (chemistry unit conversion). |

---

## 3. CLASS C — experimental anchors (comparison-only, not calibration)

| Symbol | Value | file:line | Role |
|---|---|---|---|
| `M_PROTON` | `1.67262192369e-27` kg | `constants.py:122` | CODATA 2018 anchor. |
| `M_MUON` | `1.883531627e-28` kg | `constants.py:131` | Explicitly fenced at `:126-130`: *"it is a probe mass, NOT a substrate calibration input (the three imported inputs remain {m_e, alpha, G})"*. |
| `M_SUN` | `1.989e30` kg | `constants.py:132` | IAU nominal. |
| `M_P_MEV_CODATA` | `938.272088` MeV | `constants.py:1137` | Validation anchor; paired with the prediction `M_P_MEV_AVE` (`:1136`) per the intent-split at `:1121-1135`. |
| `M_N_MEV_TARGET` | `939.565420` MeV | `constants.py:1138` | **Un-replaced import.** `:1134-1135`: *"M_N_MEV_TARGET remains a CODATA anchor; no framework derivation has yet been adopted for the neutron mass."* |

---

## 4. CLASS D — structural / relation imports (the ones that are NOT in the count)

### D1. `K = 2G` ⟺ `ν_vac = 2/7` — GR-imported FORM edge

| | |
|---|---|
| **Value** | `N_NU = NU_VAC = 2/7 = 0.2857142857…` |
| **Enters at** | `constants.py:397` (`N_NU`), `constants.py:626` (`NU_VAC`), `constants.py:614` (`ISOTROPIC_PROJECTION = 1/7`), `constants.py:781` (`V_LONG = √(2G_vac/ρ)`) |
| **Class** | **GR-IMPORTED (echo for the value).** `form-deriving-value-importing.md:87`: *"the substrate forces the *form* of the elastic response `K/G = f(ρ)`"* / *"the *value* 2/7 — the GR trace-reversal identity, not crystalline-forced nor constitutively-forced"*. PR #261 (MERGED). Re-confirmed at z=3 srs by PR #506: `research/2026-07-04_srs-elastic-tensor_result.md:159` — *"ρ\* is located precisely where K=2G, i.e. **ρ\* is K=2G RE-IMPORTED, not an independent lattice determination**"* |
| **Count treatment** | Grant ruling 2026-08-03, `form-deriving-value-importing.md:98-113`: a *"separately-tagged constitutive-FORM import edge"*, **not** a fourth calibration input; *"It mints no `ilk-` node and moves no `real_or_fitted` tag, so the count machinery is byte-untouched."* |
| **Carries with it** | `ρ* ≈ 9.7734` (the externally-supplied `k_a/k_s` bond-stiffness ratio at which ν_Hill = 2/7; `srs-elastic-tensor_result.md:132`), and Zener anisotropy `A ≈ 1.229` at that point — i.e. 2/7 is an **isotropic Voigt-Reuss-Hill average over a materially anisotropic tensor** (`constants.py:392-396`, `:623-625`) |
| **If it moves** | `ISOTROPIC_PROJECTION`, `AVALANCHE_N_3D` (38/21), `ETA_EQ`, `SIN2_THETA_W = 2/9` → the **entire** CKM block (`LAMBDA_CKM`, `A_CKM`, `RHO_ETA_MAG`, `V_US/V_CB/V_UB`) → `M_Z_MEV`, `G_F`, `HIGGS_VEV_MEV`, `M_HIGGS_MEV`; `SIN2_THETA_12`; `V_LONG = √2·c`; `r_sat = 7GM/c²`; `ε₁₁ = 7GM/c²r`; `κ = c⁴/7G`; `D_NN_EIGENVALUE`; `B_DEUTERON_PREDICTED`; `DELTA_THERMAL` (built from 2/7). **This is the single highest-fan-out import in the corpus.** |
| **★ CURRENT STATUS** | **See Finding 1 — the dispatch's "NOW KILLED" is an over-read.** |

### D2. `ξ_M` (Machian hierarchy coupling) — back-solved out of G

- **Value** `8.154833696927648e43` (dimensionless).
- **Enters at** `constants.py:650`: `XI_MACHIAN = HBAR * C_0 / (7.0 * G * M_E**2)`.
- **Class: BACK-SOLVED / Class-E circular, self-declared.** `constants.py:638-641`: *"Class E circularity (intentional): G is CODATA-input (Bounding Limit 3); ξ_M is inverted out of G via the closed-form above; ξ_M is then used downstream in derivations that re-route through H_∞ via R_H ≡ c/H_∞."* Register: `interlock-register.md:216` — *"ξ ≈ 8.15×10⁴³ is NOT forward-derived: it is back-solved from CODATA G … circular by construction."*
- **Homonym guard (live, correct):** ξ_M ≠ `XI_TOPO`; and ξ_M ≠ `R_H/ℓ_node ≈ 3.46e38` (`interlock-register.md:225-226`).
- **If it moves:** nothing independently — it *is* G re-expressed. Its only escape is Chain B′.

### D3. `u₀* ≈ 0.187` (K4 magic-angle operating point) — asserted / back-fit

- **Not in `constants.py`.** Lives in KB: `omega-freeze-cosmic-grain-cascade.md:34` — *"the value `u_0^* ≈ 0.187` is **asserted / back-fit** to CODATA α and G, not forward-derived (2026-06-14 walk-back)"*; `claim-quality.md:1101` — *"`u_0^* ≈ 0.187` is **asserted, not exhibited**"*.
- **Retraction on the record** (`constants.py:19-27`): the earlier reduction to *"one scale (ℓ_node) + one cosmological initial-data parameter (Ω_freeze)"* is **RETRACTED**; *"Do not refill 0.187 with 4/21."*
- **Testing consequence** (`constants.py:52-56`): Routes 1 & 2 (α, G) are the fit inputs — *"their agreement is guaranteed by construction"*; only Route 3 (𝒥_cosmic) independently tests. **This is the framework's one live chord/echo discriminator on the calibration set.**

### D4. `z₀ ≈ 51.25` (effective coordination) + `p_G ≈ 0.117` — α-inverted, on a retired substrate word

- **Values** `Z_COORDINATION = 51.2481655…`, `P_RIGIDITY = 0.11708…`.
- **Enters at** `constants.py:597-607`.
- **Comment claims** (`:596`): *"This is **NOT** a fitted parameter — it follows uniquely from p\* = 8πα."* True as arithmetic; but the KB's own open item (`common/claim-quality.md:440`) reads: *"Derive z₀≈51.25 from first-principles K4 amorphous-network geometry (flagged still-open) so the K4-TLM route stops depending on inverting the EMT quadratic given α"*. So z₀ **inherits both** the α echo and the K=2G import (the quadratic is the `K/G = 2` crossing condition, `:587`).
- **⚠ Vocabulary + carrier flag:** `constants.py:591` still reads *"Derived from the Feng-Thorpe-Garboczi EMT for a 3D **amorphous** central-force network"* — the word retired 2026-06-18 (INVARIANT-N1 geometry-leak), and `constants.py:770-773` in the *same file* already re-attributes the EMT story as *"doubly-superseded"*. **Internal inconsistency inside one file.**

### D5. `δ_th = 1/(14π²)` — calibration-not-prediction, on the record

- **Value** `DELTA_THERMAL = 0.007237227403…`; feeds `KAPPA_FS = 8π(1−δ_th) = 24.95085` → `I_SCALAR_1D` → `PROTON_ELECTRON_RATIO = 1836.11704`.
- **Enters at** `constants.py:924`.
- **Class: RESIDUAL-FIT, explicitly.** `constants.py:869-885` (🔴 Rule-12, Grant-approved 2026-07-14): *"the VALUE is CALIBRATION-NOT-PREDICTION … the chronology of this number is residual-first / fitted-after"*; introduced as `1/(28π)` at archive `deba5edb`, recalibrated to `1/(14π²)` at `879aa801` when the m_p/m_e error moved 0.34% → 0.002%, *"and the paper-trail for that pinning was removed at recalibration."* Also on record: *"α-ADJACENCY IS COINCIDENCE"* (`:887-890`). Full audit: `research/2026-07-13_mp-me-mass-ratio-audit.md` (PR #677).
- **If it moves:** the proton/baryon ladder (`BARYON_LADDER` c=5…13, `constants.py:1033-1059`), `T_NUC`, `D_PROTON`, `D_INTRA_ALPHA`, `D_NN_EIGENVALUE`, `B_DEUTERON_PREDICTED`, `M_P_MEV_AVE`.

### D6. `p_c` residual + `V_total = 2` — the ladder's honest status

- `P_C = 8πα = 0.1834025` (`constants.py:478`); `V_TOROIDAL_HALO = 2.0` (`constants.py:982`).
- `constants.py:973-975` (Grant-adjudicated 2026-06-01): *"the count-2 is CLOSED (forced reactance count, mass-confirmed at exactly 2.000); the per-channel coupling p_c = 8πα is a RESIDUAL (canonical-packing-plausible, not line-by-line) — so the ladder is "1-residual Skyrme", NOT "zero-parameter"."*
- Same file records the **retraction of four false geometric derivations** of the "2" (`:963-970`), including a signed crossing integral that *"VANISHES by antisymmetry … evaluating to 0, not 2."* Good discipline; noted as a model for D4/D5.

### D7. `ξ_topo` — a definition, riding the α echo

- **Value** `4.1490047447e-7` C/m; `constants.py:356`: `XI_TOPO = e_charge / L_NODE`.
- **Class: DEFINITION whose value rides α.** `form-deriving-value-importing.md:90`: *"the conversion of the geometric linking integer into the charge `e` routes through `ξ_topo ≡ e/ℓ_node` (`axiom-definitions.md:28`, a *definition*), whose value rides the α-echo … → **[DOORWAY-NO-PINNING]**"*. The London-leg sharpening at `:185-200`: single-valuedness pins the **integer**, *"the integer never becomes a pinned flux **VALUE**."*
- **If it moves:** the entire EE↔topo conversion block (`constants.py:462-471`), `RHO_BULK` → `G_VAC` → `V_LONG`, `G_STRING`.

### D8. `I_SCALAR_1D` and `BARYON_LADDER` — solver-output literals

- `I_SCALAR_1D = 1161.9870305252678` (`constants.py:941`); `BARYON_LADDER` dict (`constants.py:1033-1059`).
- **Class: DERIVED, CI-gated literals** — `constants.py:936-940` names the gate: `tests/test_constants_literals.py::test_i_scalar_1d_matches_computation` re-runs `_compute_i_scalar_dynamic()` and asserts equality. This is the *correct* pattern; cited here as the standard the D4/D5 rows do not meet.

---

## 5. CLASS E — the NEW inputs minted by ratified BC-SRC clauses S + G (2026-08-10)

**Record:** `_orchestration/docket-entries/2026-08-10-ruling-r43-sg-ratified.md`, Grant verbatim `:5-6` — *"yes this makes perfect sense, we need our ground reference."*

**Clause text, verbatim** (`research/2026-08-10_bound-constitutive_result.md:119-120`):

> **S (deposit).** A matter defect deposits a nonzero net A1 dilatation flux: `∮_S u·n̂ = 4πB(M)` … with `B(M)` = the defect's A1 mass accounting (dimensional VALUE via the imported G/ξ chain).
> **G (grade coupling / bridge).** The operating-point grade is the bound sector's potential: `u₀ = −λ∇ε₁₁`, with the grade pinned by the elliptic law `−∇·[κD(A)∇ε₁₁] = T₀₀`, `κ = c⁴/7G` (VALUE imported).

| # | Symbol | Value at this SHA | Enters at | Class | If it moves |
|---|---|---|---|---|---|
| E1 | `λ` (dress↔grade bridge) | **NONE — un-valued.** No numeric literal exists anywhere in `src/ave`, `research/`, or the manuscript (grep for `λ =`, `lambda_bridge`, `LAMBDA_BRIDGE` at `origin/main`: zero hits) | Clause text only: `bound-constitutive_result.md:120` | **MEASURED-THEN-CHECKED (new).** R43 `:20-21`: *"The internal falsifier B = 7λGM/c² ships with the clause — one λ across every consumer; the over-determination is the axiom's own test port."* R43 `:42-44`: *"**The λ over-determination lane** — measure λ from two independent consumers; the repaired sector's first forward test"* — **pre-scoped, NOT run** | Everything the bound A1 sector hosts: the dress `u₀ = B/r²`, mass-as-enclosed-compression-charge, the gravimeter-causality argument (`:128`), the energy functional (`:175`) |
| E2 | `κ` (bias-sector permittivity) | `c⁴/7G = 1.7325e44` Pa (my arithmetic from `constants.py:110,188`) | `bound-constitutive_result.md:120`; implemented at `src/ave/gravity/backreaction.py:12` — `−∇·[ (c⁴/7G)·D(A)·∇ε₁₁ ] = T₀₀^src` | **VALUE-IMPORTED, unchanged.** `bound-constitutive_result.md:175`: *"The `κ` VALUE stays imported (#261 unchanged)"* — i.e. it rides G **and** the `/7` from K=2G | Every gravity statics number the engine produces |
| E3 | `B(M)` (per-defect A1 deposit) | Not independently specified | `bound-constitutive_result.md:119` | **IMPORT-ROUTED** — *"dimensional VALUE via the imported G/ξ chain"* | Pinned to λ by `B = 7λGM/c²` (`:126`) — one relation, two objects |

**Auditor arithmetic on E1 (mine, per A47).** From `u₀ = −λ∇ε₁₁` with ε₁₁ dimensionless (ε₁₁ = 7GM/c²r checks out dimensionless) and ∇ carrying `[m⁻¹]`, λ carries `[u]·[m]`. From clause S, `∮u·n̂ dS = 4πB` gives `[B] = [u]·[m²]`; substituting into `B = 7λGM/c²` is dimensionally consistent for **any** `[u]`. So:
- if the dress `u` is a **displacement** `[m]` → λ is an **area** `[m²]`;
- if `u` is a dimensionless strain → λ is a **length** `[m]`.

**Which one is not settled at this SHA.** `bound-constitutive_result.md:114` executes FORK-1 and lands: *"the receipts SPLIT (R-a vs R-b/R-c) → per the frozen procedure the fork **GOES TO GRANT UN-RECOMMENDED**"*; R43 `:34`: *"**FORK-1** — DEFERRED per the standing rec; rules after the axiom completes."* **λ's dimension rides an open fork.** That is a concrete reason to run the over-determination lane *after* FORK-1, not before.

---

## 6. CLASS F — numerical-policy constants (no physics; listed for completeness)

`EPS_NUMERICAL = 1e-12` (`:556`), `EPS_CLIP = 1e-15` (`:557`), `EPS_DIVZERO = 1e-30` (`:558`), `EPS_SAT_RATIO = 1e-12` (`:578`). Self-declared at `:553-554`: *"these constants are DIMENSIONLESS ratios applied to already-normalised quantities. They carry no units and no physics."* Correctly fenced; `EPS_CLIP` vs `EPS_SAT_RATIO` distinction is documented at `:567-577`.

---

## 7. CLASS G — derived-from-the-above (the FORM half; not inputs)

Listed compactly so the register is complete. All of these are algebra over Classes A–E and mint no new number:

`Z_0`, `L_NODE`, `OMEGA_C`, `L_CELL`/`C_CELL`, `ELL_C = √6·ℓ_node`, `A_0`, `RY_EV`, `PHI`/`R_GOLDEN_TORUS`/`RR_GOLDEN_TORUS`, `ALPHA_COLD_INV = 4π³+π²+π`, `DELTA_STRAIN`, `N_*` native block, `N_Y_LOSS_90 = 1/2π²`, `AVALANCHE_N_3D = 38/21`, `C_K_KOLMOGOROV = 4/3`, `N_PHI_PACK = π√2/6`, `NATIVE_TO_SI_*`, `TAU_RELAX_*`, `EE_TO_TOPO_*`, `P_C`, `ETA_EQ`, `T_EM`, `V_SNAP`, `E_YIELD_KINETIC`, `V_YIELD`, `E_CRIT`, `E_YIELD`, `B_SNAP`, `R_I`/`R_II`/`R_III`, `ALPHA_S`, `SIN2_THETA_W`, `M_W_MEV`, `M_Z_MEV`, `G_F`, `HIGGS_VEV_MEV`, `N_K4=4`, `LAMBDA_HIGGS=1/8`, `M_HIGGS_MEV`, CKM block, PMNS block, `H_INFINITY`, `R_HUBBLE`, `RHO_BULK`, `G_STRING`, `G_VAC`, `V_LONG`, `NU_KIN`, `E_SLEW`/`NU_SLEW`/`LAMBDA_SLEW`, `Z_RADIATION`, `KAPPA_FS_COLD = 8π`, `CROSSING_NUMBER_PROTON = 5`, `PROTON_ELECTRON_RATIO`, `T_NUC`, `ALPHA_HBAR_C`, `HBAR_C_MEV_FM`, `K_MUTUAL`, `M_P_MEV_AVE`, `D_PROTON`, `D_INTRA_ALPHA`, `D_NN_EIGENVALUE`, `ALPHA_HC`, `B_DEUTERON_PREDICTED`, `OMEGA_0_NUCLEAR`, `E_0_NUCLEAR`, `K_COUPLING`.

Three flags inside Class G:

- **`R_II = √3/2` (`constants.py:526`) is sector-specific, unlabeled.** `vol1/claim-quality.md:588,592`: *"`r_2 = √3/2` is **sector-dependent**, not universal … Citations of `r_2 = √3/2` without sector qualification implicitly assume spin-2."* The `constants.py` line carries no sector tag while its siblings `R_I` and `V_YIELD` did get criterion tags in commit `545ca97e`. **Asymmetric tagging.**
- **`N_PHI_PACK = π√2/6` (FCC)** is justified at `:422` by *"The K=2G lattice (Axiom 2) selects FCC close-packing"* — an FCC selection routed through the GR-imported K=2G, on a corpus whose ratified carrier is z=3 srs.
- **`K_MUTUAL = 11.337 MeV·fm` (`:1116`)** is a derived form that `:1100` states *"matching the He-4 calibrated value to within 0.005%"* — a derivation-replacing-a-calibration. Correct direction; noted so the ancestry isn't lost.

---

# FINDINGS

### Finding 1 — The dispatch's "K=2G … NOW KILLED by the arc" over-reads #935. What was killed is a *reading*, and no label has moved.

**Verdict: FLAG (dispatch-premise correction).**

**Evidence.** `research/2026-08-09_bound-response_result.md:19` (headline, verbatim):

> **🔴 VERDICT AS RE-CUT AT THIS LANE'S OWN TIER-2 (2026-08-10, pre-presentation; the original DERIVED verdict below is PRESERVED per Rule 12 and OVERTURNED): `NOT-DERIVABLE` — the adjudicating structure is missing; enumerated.**

The "kill flips polarity / it was the falsification of the IMPORT" reading is in the **preserved-and-overturned** block at `:21`, not the live verdict. What survives is stated at `:19` item (2):

> **the premise-localization receipts** (G-RECON, unchallenged): #761/#919/#927/#930 all consumed the #261-closed K-import — the kill chain's premise is the import, with receipts, and **the pulsar exclusion binds the IMPORTED reading**

And `research/2026-08-09_screening-theorem_result.md:212`: *"**VERDICT (RE-CUT AT TIER-2): `SEAL-DERIVED + RESIDUE-EXCEEDS`** … the kill re-fires on the residue … The frozen LC-1 kill cell … **remains SOURCED exactly as #919 left it**."*

**Reasoning.** Three distinct objects are being collapsed by "killed": (a) the *propagating-P-branch reading* of K=2G — excluded observationally at `F_res = 0.032863` = 252.8× the DP bound / 20.5σ HT; (b) the *static* consumption of ν=2/7 — explicitly untouched, `bound-constitutive_result.md:198`: *"Every /7 ingredient consumes ν as a STATIC input; the ν VALUE stays GR-imported (#261, byte-unchanged)"*; (c) the *corpus labels* — untouched, because R40's demotion sweep has not executed (Finding 2). Reporting (a) as "K=2G killed" would license removing ν=2/7 from the CKM/EW/PMNS chain, which nothing in the arc supports. This is the substitution-not-retraction guard (A47 v11b) applied pre-emptively.

**Recommendation (implementer).** State the K=2G row's live status in three lines wherever it is quoted: *dynamic/propagating reading excluded by pulsars (#930/#919); static value 2/7 still GR-imported and still consumed (#261 byte-unchanged); replacement is BC-SRC clause G, which re-homes κ but does not un-import it (`bound-constitutive_result.md:175`).*

---

### Finding 2 — Every artifact Grant asked for carries **pre-#930/#935 provenance text**. The demotion sweep is verified but not executed.

**Verdict: WARN (staleness, tracked and expected — but load-bearing for this register).**

**Evidence.**
- `git show --stat 4cb4049b` (PR #938, R40 sweep): touches exactly two files — `_orchestration/2026-08-10_r40-sweep-scope-verification.md` and `research/drivers/r40_sweep_worklist_verified.json`. **Zero manuscript/KB/engine demotions landed.** The doc self-states: *"demotes nothing — it verifies the worklist the demotions will run against."*
- Last commit touching `constants.py`: `545ca97e` (2026-07-17). Last touching `form-deriving-value-importing.md`: `7a6f4ba6` (2026-08-03). Last substantive touch to `eq_calibration_constants.tex`: `918b1adf` (2026-07-03).
- The worklist **already names `constants.py` rows**: `src/ave/core/constants.py:778` → bin **`DIES-WITH-THE-PHANTOM`** (quote: *"the full compressional (P) wave is c_L = √((K + 4G/3)/ρ) = √(10/3)·c ≈ 1.83c"*); `constants.py:775` → **`NEEDS-RE-DERIVATION`** (`V_LONG` label *"Longitudinal wave speed"* / *"port-mode"*); `constants.py:485` → `SURVIVES-AS-RESPONSE`.

**Reasoning.** Per A43 v2, a register assembled from these three sources without the arc overlay would propagate stale beliefs. The `constants.py` header still reads *"Q-G47 Sessions 9-18 … closed Q-G47 at substrate level: K(u_0\*) = 2 G(u_0\*)"* (`:63-65`) with no post-#930 note.

**Recommendation.** The engine-lane demotion of `constants.py:768-781` is the *only* Class-A/D item on the R40 worklist that touches this register; it should be sequenced with (not after) the manuscript sweep, because `V_LONG` is imported by downstream drivers. Note the file's own coordination convention at `:239` — *"[doc-lane edit; engine lane owns constants.py — coordinate on merge]"*.

---

### Finding 3 — λ is a new un-valued parameter and the count machinery has not been asked about it.

**Verdict: FLAG (open adjudication, surfaced not resolved).**

**Evidence.** `interlock-register.md:12` `expected-independent-count: 3`, recomputed by `make verify-kb-metadata` from `compute_independent_parameter_count` (`manuscript/ave-kb/tools/kb_index_lib.py:2989`), asserted at `:47-53`. `form-deriving-value-importing.md:102-103`: *"the calibration set stays `{m_e, α, G}` with `expected-independent-count: 3`"*. The R43 record (`2026-08-10-ruling-r43-sg-ratified.md`) ratifies clauses S and G and pre-scopes five follow-ons at `:38-44` — **the count is not among them**.

**Reasoning.** λ is not derived from {m_e, α, G}; it is to be *measured* from a consumer and *checked* against a second (`R43:42-44`). That is the same epistemic shape as α before its lift-routes closed — a value-fitted identification with a live falsifier. The K=2G precedent (`form-deriving-value-importing.md:98-113`) shows the corpus has a machinery for "imported but count-neutral" — but that ruling turned on K=2G being a **relation between two moduli**, not a value. λ is a **value**. The two cases are not obviously the same edge class, and treating them as the same by default is exactly the drift A47 v13 warns about.

**Recommendation.** Before the R43 `:38` axiom-landing execution fires, get an explicit ruling on one question: does λ mint a fourth `calibration-params` entry (count 3→4), or a new edge class? If the latter, it needs a named tag in `interlock-register.md` the way K=2G got one, or the CI gate will silently stay at 3 while a fourth fitted value is live in the physics.

---

### Finding 4 — `interlock-register.md`'s `constants.py` and `.tex` line citations have drifted.

**Verdict: FAIL (cross-tree citation integrity).**

**Evidence (all verified at `origin/main` this turn).**

| Register cite | Claimed content | Actual line at HEAD | Actual content at cited line |
|---|---|---|---|
| `constants.py:589` (`:216`, `:222`, `:225`, `:227`) | `XI_MACHIAN = HBAR*C_0/(7.0*G*M_E**2)` | **`:650`** | `:589` is **blank** |
| `constants.py:177` (`:216`, `:222`) | `G = 6.67430e-11` | **`:188`** | `:177` is a blank comment line inside the α derivation block |
| `constants.py:577` (`:216`, `:222`) | tag *"CODATA-input (Bounding Limit 3)"* | **`:638`** | `:577` = `# clamp itself (subtractive bound on r²)` |
| `constants.py:583-588` (`:223`) | Chain B′ *"currently OPEN"* prose | **`:644-649`** | `:583-588` = the `P_C` / EMT-operating-point comment |
| `eq_calibration_constants.tex:31-35` (`:284`) | *"the two anchor identities"* | ℓ_node eq is at **`:36-40`** | `:31-35` = prose + `\medskip` |

(`eq_calibration_constants.tex:57-61` for α **is correct**.)

**Reasoning.** Five of six cross-tree line cites in the machine-authority register for the calibration count resolve to the wrong content. Per A47 v11c, a numerical claim against a manuscript/engine-quoted value requires the cite to actually pin the value. These do not. The R40 sweep's own method finding (`2026-08-10_r40-sweep-scope-verification.md`, the probe table: 115 → 32 → 11 → 5 ABSENT across three probe generations, *"A single-probe site check on this table has roughly a 20× false-drift rate"*) shows the repo already knows this failure mode — but that machinery was pointed at the #935 worklist, not at the interlock register.

**Recommendation.** Run the R40 sweep's v3 hard-reduction probe over `interlock-register.md`'s cite set and repair. This is a doc-lane edit; the register is the CI-gated home for the count, so drifted cites there are higher-severity than elsewhere.

---

### Finding 5 — Two SI-scaffolding literals are over-determined against the imported α, un-flagged.

**Verdict: WARN (small magnitude; real).**

**Evidence.** `constants.py:107-108` heads the block *"SI ELECTROMAGNETIC CONSTANTS (Exact or CODATA 2018)"*; `:111` `MU_0: float = 4.0 * pi * 1e-7  # Vacuum permeability [H/m]`; `:114` `HBAR: float = 1.054571817e-34`.

My arithmetic at this SHA:
- Post-2019 SI, μ₀ is *derived* from α: `μ₀ = 2αh/(e²c)`. With the file's own `ALPHA`, `HBAR`, `e_charge`, `C_0`: `μ₀ = 1.256637061353872e-06` vs hard-coded `1.2566370614359173e-06` → **relative disagreement 6.53e-11**.
- SI-exact `h = 6.62607015e-34` ⇒ `ℏ = h/2π`. The file's literal gives `h = 6.62607014594e-34` → **relative disagreement 6.13e-10**.

**Reasoning.** Neither number is large enough to move any published AVE result. But the file asserts a 3-input calibration set and then supplies a fourth and fifth number (μ₀, ℏ) that the 2019 SI makes *dependent* on the already-imported α and on exact `h`. Per `consistency-vs-emergence`, this is the definitional-identity-masquerading-as-independent-input pattern in miniature: `Z_0 = √(μ₀/ε₀)` is presented as Axiom-1-derived (`eq_calibration_constants.tex:12,42-46`) while its value silently carries a 6.5e-11 inconsistency with the α the same file imports. The honest statement is "μ₀ is the pre-2019 conventional value, retained; it agrees with α-derived μ₀ to 7e-11."

**Recommendation.** Comment-only: add the derivation note at `:111` and the exact-`h` note at `:114`, with the two residuals stated. No value change (changing `MU_0` would move `Z_0` and every impedance receipt).

---

### Finding 6 — `Z_COORDINATION`'s provenance comment contradicts a correction already present in the same file.

**Verdict: FAIL (intra-file contradiction).**

**Evidence.** `constants.py:591-596`: *"Derived from the Feng-Thorpe-Garboczi EMT for a 3D amorphous central-force network … This is NOT a fitted parameter — it follows uniquely from p\* = 8πα."*

`constants.py:769-773` (same file, later, dated 2026-07-04 / PR#506): *"the "(Effective Medium Theory)" attribution is **doubly-superseded** — K=2G is GR-IMPORTED (not EMT-forced; PR#261), and the crystalline srs Cauchy tensor is a one-parameter family (PR#506), so **neither the amorphous EMT nor the z=3 crystal forces K=2G**."*

Plus: "amorphous" is a retired substrate word (INVARIANT-N1, 2026-06-18 — `cosmic-axes-and-frames-glossary.md:9` records the glyph retirement and the reason: *"the "A" carried the closed geometry-leak "amorphous""*), and the KB's own open item concedes the α-inversion dependency (`common/claim-quality.md:440`).

**Reasoning.** Rule 12 says preserve the body and add the header; here the correction was added at one site (`:769`) and not propagated to the site that *originates* the EMT claim (`:591`). A reader arriving at `Z_COORDINATION` gets the superseded story with a "NOT a fitted parameter" assurance attached.

**Recommendation.** Dated note at `constants.py:590-596` pointing to the `:769-773` re-attribution and to `common/claim-quality.md:440`; retire the word "amorphous" per INVARIANT-N1. Value unchanged (`51.248165500275775`).

---

### Finding 7 — Register hygiene that is working, recorded so it isn't lost.

**Verdict: PASS.**

Three patterns in `constants.py` are the standard the weaker rows should be held to, and they should be cited as precedent rather than re-invented:

1. **`DELTA_THERMAL`** (`:869-898`) — a value that failed audit got a 🔴 Rule-12 provenance header naming the archive commits (`deba5edb`, `879aa801`), the residual it closed, the deleted paper-trail, and an explicit *"α-ADJACENCY IS COINCIDENCE (on the record)"*. Body preserved, no substitution.
2. **`V_TOROIDAL_HALO`** (`:943-981`) — four false geometric derivations retracted by name, including the antisymmetry argument showing the claimed integral *"evaluat[es] to 0, not 2"*, plus the honest downgrade *"1-residual Skyrme", NOT "zero-parameter"*.
3. **`I_SCALAR_1D` / `BARYON_LADDER`** (`:936-940`, `:1025-1032`) — literals gated by a named test that re-runs the solver and asserts equality. This is the A47 v11d CI-gate-at-claimed-tolerance pattern, already implemented.

---

# OPEN QUESTIONS FOR GRANT

1. **λ's dimension rides FORK-1.** λ is a length or an area depending on whether the dress `u` is a displacement or a dimensionless strain — and FORK-1 (`bound-constitutive_result.md:114`) went to you un-recommended and is DEFERRED (`R43:34`). Does the λ over-determination lane (`R43:42-44`) run before or after FORK-1 rules?

2. **Does λ move `expected-independent-count` 3→4?** The K=2G ruling made an *imported relation* count-neutral; λ is an imported *value*. Same edge class or new one?

---

**Lane-attribution note.** Operating in auditor lane; every item above is a recommendation requiring implementer execution. I hold no Edit/Write tool by harness design and staged nothing. No cross-lane authorization was cited in this dispatch, so the `constants.py` comment repairs (Findings 5, 6), the `interlock-register.md` cite repairs (Finding 4), and the K=2G status-line propagation (Finding 1) all go through the implementer lane. Two dispatch premises were corrected rather than adopted: "K=2G NOW KILLED" (Finding 1) and the implicit assumption that the three named sources carry post-#930/#935 state (Finding 2).

---

# NAMED THEOREM / DERIVED-RESULT INVENTORY

**Read-state pin.** All content read at `origin/main` = `c03034eb` (merge of PR #940). Local `HEAD` was `6c291196` — **behind origin/main by 5 commits** — so the working tree was NOT read; the tree was extracted from `origin/main` via `git archive` and every line number below is an `origin/main` line number. Every verbatim quote was grep-confirmed in this turn.

**ROOT** = `/Users/grantlindblom/AVE-staging/AVE-Core`

---

## §1 — OPERATOR / IDENTITY CLASS (`$ROOT/manuscript/ave-kb/common/operators.md`)

Catalog owner is `clm-sysqaf` (**DEFINITIONAL** — a naming register, not a derivation).

| Op | Statement | Licenses | Status / class | file:line |
|---|---|---|---|---|
| **Op14** Dynamic Impedance | $Z_{eff}=Z_0/\sqrt S$ | Local-clock modulation $\omega_{local}=\omega_{global}\sqrt{1-A^2}$; graded-index BC; cross-sector trading | **CANONICAL**, explicit eq. Vol1 Ch6 §1.13. Owner claim `clm-1eg13f` **DERIVED** from axiom-4, solidity **0.80** `ok-with-caveats` | `operators.md:54` |
| **Op16** Universal Wave Speed | $c_{shear}=c_0\sqrt S$ | (would license) local clock, Schwarzschild analog, Op13 $c_{eff}$ | 🔴 **VACATED CITE (2026-08-07)** — *"the two vol-2 ch-7 cross-citations in this cell do NOT carry $c_0\sqrt S$ at HEAD, and three mutually-inconsistent forms are in play. The Op16 form is NOT adjudicated here."* Disposition **ROUTED, NOT RULED** | `operators.md:56`; fence `operators.md:212–235` (§8 FLAG-CEFF-CITE) |
| **Op17** Power Transmission | $T^2=1-\Gamma^2$ | Active energy-transfer coefficient at any Γ boundary; also an imported theorem-identity (translation-circuit §6 row #4) | **CANONICAL** — explicit eq. Vol1 Ch6 §1.16 | `operators.md:57` |
| **Op21** Q-Factor Phase Transition | Substrate-foundational: $Q=\ell$ per Nyquist-cell-resolved confined mode at the $\Gamma=-1$ saturation/TIR boundary. Specialization $Q\sim1/\ln(Z_1/Z_0)$ | Mode-counting at 4 substrate scales; three-Nyquist-category sum to $\alpha^{-1}$; BH-ringdown $Q=\ell$ | **CANONICAL**, $Q=\ell$ **derived end-to-end** (Class-B substrate-mechanism rigor). The $Q\to1/\ln(Z_1/Z_0)$ reduction is **conjectured-not-derived** (`Q-OP21-BARDEEN-1`). BH-ringdown instance **spin-scoped to cold $a_*=0$** (Grant B1) | `operators.md:61`; leaf `.../op21-multi-mode-mode-counting.md:10`, `:19`, `:31` |
| **Op22** Avalanche Factor | $M=1/S^2=1/(1-r^2)$ | Nonlinear cascading metric yield; from Ax4 power conservation | **CANONICAL**. ⚑ A43 v11: doc-81's $M=1/(1-S)$ is a **different formula** — diverges opposite as $S\to0$ | `operators.md:62` |
| **Op15 / Op18 / Op20** | $r_{virtual}=\sqrt{1-\sigma^2}$ / $\omega_c=\omega_0/\sqrt{1-\lambda k}$ / $\omega_{regime}=\ell c_{wave}/r_{eff}$ | — | **SYNTHESIS-LABELLED / SYNTHESIS.** Op20 has **no canonical formula** in Vol1 Ch6 (narrative only) — A43 v10 instance | `operators.md:55`, `:58`, `:60` |

> **FLAG.** Op16 is the most-consumed "derived result" in this class and its receipt is dead. Per the vacated-cite pattern the *argument* is dead, not the *form*. Until a derivation lane returns, **no inventory row may cite $c_{shear}=c_0\sqrt S$ as a derived structure**; `operators.md:56` forbids treating the row and its two vol-2 cites as mutually supporting. Propagates: Op13 (`:53`) says it "uses local saturated $c_{eff}$ … per Op16", and `clm-1eg13f`'s solidity caveat is *"the $c_{eff}=c_0\sqrt S$ step is asserted from the kernel rather than re-derived in-leaf"* (`foundational-machinery-register.md:294`).

---

## §2 — NAMED THEOREMS WITH `clm-` PROVENANCE

Source: `$ROOT/manuscript/ave-kb/common/foundational-machinery-register.md` — 10 members, **7 DERIVED / 3 DEFINITIONAL** (`:393`).

| Theorem | Statement | Licenses | Status | file:line |
|---|---|---|---|---|
| **Theorem 3.1′ — Electron Q-Factor from LC Tank at TIR Boundary** (`clm-rtdmsn`) | $\alpha^{-1}=Q_{tank}=Q_{vol}+Q_{surf}+Q_{line}=4\pi^3+\pi^2+\pi=137.036$ at Golden Torus $R=\varphi/2,\ r=(\varphi-1)/2$ | The Q-factor reading of α; $Z_{radiation}=Z_0/4\pi$ inheritance (consumed by `clm-6t3p6x`) | **DERIVED (in FORM) / VALUE-ECHO.** deps axiom-1,2,3; solidity **0.85 `ok-to-build`** — highest-solidity member. **Class-B named geometric identification**: scale ~1/137 forced, exact value rests on $R\cdot r=1/4$, *"which the substrate does not independently select"* (both lift-routes closed). Echo tag `ilk-rr14gt`, `real_or_fitted = fitted-identification`. Cite as IDENTITY, never derivation | `foundational-machinery-register.md:303–312`; leaf `.../theorem-3-1-q-factor.md:15` (boxed), `:19` (value-scoped status), `:164` (Q-object table) |
| **Mass-Closure Theorem** (`clm-ka5zdx`) | $mc^2=E_{\text{reactive}}$ | mass↔reactive-energy identity | **DERIVED**; only member reaching all four axioms directly. Solidity **0.50 `input-only`** — softest theorem member; possible application-tier demotion **surfaced not decided** | `foundational-machinery-register.md:314–323` |
| **Substrate-Observability Rule (Universal No-Hair Theorem)** (`clm-ofys5v`) | A $\Gamma=-1$ boundary totally traps the interior; only $M,Q,J$ externally measurable at every scale | Boundary-observability electron → nucleus → magnetopause → BH → horizon | **DEFINITIONAL** — corpus's own rationale: *"Internally coherent as a definitional rule; the trapping mechanism is asserted, not derived."* No `depends-on` edges. Solidity **0.55**. ⚑ naming-vs-provenance mismatch | `foundational-machinery-register.md:325–334` |
| **AVE BH Horizon + Area Theorem** (`clm-law1ho`) | $r_{sat}=7GM/c^2$ + area law | entropy/area reuse | **DERIVED (borderline)**; solidity **0.55**. Register's own *"single strongest exclusion candidate"* — machinery only in the Area-Theorem facet | `foundational-machinery-register.md:336–345`, flag `:153–162` |
| **Parametric Coupling Kernel** (`clm-6t3p6x`) | $\varepsilon_{det}=4\pi\kappa_{quality}/N^2$, $C_{eff}(V)=C_0/\sqrt{1-(V/V_{yield})^2}$ | DAMA / detector-network predictions | **DERIVED** (axiom-4 + Thm 3.1′ + `clm-vjv4zf`); solidity **0.60 `input-only`** | `foundational-machinery-register.md:354–363` |
| **A-034 Single-Kernel Unification** (`clm-gz7ryg`) | One $S(A)=\sqrt{1-A^2}$ at all scales, inherited not re-postulated | The 26-instance saturation-kernel catalog | **DEFINITIONAL** — *"Does NOT derive Axiom 4 itself."* Solidity **0.62** | `foundational-machinery-register.md:365–374` |

> **FLAG (staleness).** The register's footer: *"Numbers are as-of `origin/main` @ f556dcdc"* (`:555`, `:243`); *"Gated against `origin/main` @ f556dcdc: … 406 nodes UNCHANGED"* (`:562`). At the current pin every solidity / `citation_count` above is a stale read. Implementer should re-run `make verify-kb-metadata` before print.

---

## §3 — STRUCTURAL / TOPOLOGICAL DERIVED RESULTS

| Result | Statement | Licenses | Status | file:line |
|---|---|---|---|---|
| **K4 port-irrep decomposition** | Under $T_d$: $V_{\text{4-port}}=A_1(\text{1D})\oplus T_2(\text{3D})$. $A_1$ = common-mode scalar/longitudinal (dilatation, mass); $T_2$ = traceless triplet (shear, photon/GW). Basis $(1,1,1,1)/2$ | **The sector-ownership spine.** Channel subscripts on every reflection/port statement; the four-channel register; A1⊥T2 no-cross-wiring | **CANONICAL** `[canon]`, `clm-j550uh` / `clm-9kd2t3` | `port-register.md:37`; leaf `.../k4-port-irrep-decomposition.md:38–46` |
| **TKI-transformer** (`def-tk1xfm`) | Axiom 2 read as the **ideal, lossless, gain-1, pole-less, INVERTIBLE** electromechanical dictionary ($u$/strain↔E, $\omega$/curl↔B) with the six-row $\xi_{topo}$ identity table $Q=\xi x,\ I=\xi v,\ V=\xi^{-1}F,\ L=\xi^{-2}m,\ C=\xi^{2}\kappa,\ R=\xi^{-2}\eta$ | Unit-bridging mechanical↔electrical | **SOLID — ★Grant-ratified 2026-07-21**, REGIME-SCOPED below the band edge ($\omega\tau\ll1$). ★**Ceiling STANDS**: *"identity-by-translation, NOT emerges-from / NOT a derivation."* SOLID ratifies the node, not a mechanism. Ceiling reaffirmed by Cleave-01 Chern null $C=0$ (`clm-clvchn`) | `vocabulary-register.md:435`, `:438`, `:441`, `:445` |
| **Sourced-charge no-go cascade — conservation leg** (`clm-nogo4l`) | $\partial_1\partial_2=0$ (boundary-of-boundary) on the srs 2-complex ⇒ $\mathrm{div}\circ\mathrm{curl}_{adj}\equiv0$; hence for the axiom-native curl drive $J=\nabla\times(g(A)\omega)$: $\partial_t(\nabla\cdot\varepsilon_{eff}E)=0$ ⇒ **enclosed charge is a conserved constant of motion, set by initial data, not emergent** | Kills the sourced-static-monopole route in statics AND curl-coupled dynamics — *"one theorem operating twice"* | **DERIVATION GRADE** (upgraded 2026-07-03 from LEAN). J-mixed escape closed: A44 converter sources $\nabla\cdot J\neq0$ **only locally**, $\sum(\nabla\cdot J)=0$ exactly ⇒ neutral texture. Chirality candidate **CLOSED-NEGATIVE**. Honest count **~2 physical closures + 2 instrument gates**, not "four locks" | `the-sourced-charge-no-go-cascade.md:107–154`, `:156–174`; operator `src/ave/topological/srs_dec.py:242` |
| **FR-braid spin-statistics** | Two-loop exchange holonomy $=-I$ ($2T$ central element, $q_w=-1.0$) by A4-only reflection-free port-permutation transport; **same** element as the single-particle $2\pi$ | Spin-statistics derived where SM imposes it by axiom | **PASS — derived, ahead-of-SM-axiom — BUT chord-vs-peer = PEER-ahead (generic-FR), NOT an AVE-distinct chord.** Non-A4 control (generic-axis $2\pi$) **also** reaches $-I$: the chain is a property of $\pi_1(SO(3))=\mathbb{Z}_2$ shared by every double-cover framework | `research/2026-06-20_fr-braid-spin-statistics_result.md:13`, `:22–28`, `:43`; ceiling `physics-lineage-map.md:434` |
| **Electron $\pi_1$ / spin-½ selection** | $\pi_1$ carries a genuine $\mathbb{Z}_2$ from SO(3)'s own $\pi_1$; loop class is winding-INDEPENDENT, $\mathrm{Hom}(\mathbb{Z}_2,U(1))$ has two elements | Spin-½ ADMITTED and representable | **`[SPIN-HALF-POSITED]`** — selection into the fermion sector **NOT forced** by (2,3) parity; the half-angle lift is hand-choosing $-1$. Symmetric-standard: SM also posits spin-½ ⇒ **peer** | `research/2026-07-08_electron-pi1-spinhalf_result.md:14–26` |

---

## §4 — ARC-GENERATED DERIVED RESULTS (Aug 2026)

### 4.1 Kernel-collapse self-termination, CHANNEL-SCOPED (#897-v2 + correction)
**Ruled text, verbatim:** *"Kernel-collapse self-termination, channel-scoped (2026-08-05; member-fenced 2026-08-06): at any strain-saturation wall, every transport coupling riding the strain kernel — G, K (both fork branches), and the u↔φ coupling G_c — disconnects at the last bond: total reflection, phase computed from the branch-derived row at the declared plane, density-profile-independent (receipts: PR #888, #890, both Tier-2-verified). The rotational channel's transport (γ·S_κ) is carved out: unwalled at r_sat, its own wall being a κ-amplitude surface."*
- **Licenses:** BH-echo mirror as a *channel* question; Regime IV fenced out for mirrored channels; shear→rotation conversion confined to the graded approach.
- **Grade:** three disconnection theorems **measured EXACT** — last-bond stiffness `0.0`, $|\Gamma_{LB}+1|$ `0.0`, beyond-wall spread `0.0` over 48 groups ($10^{-30}$–$10^{+30}$), RHO-A−RHO-B separation `0.0`. *"Not a tolerance. Zero."*
- **Certification:** TASK 2 **`ROW-CERTIFIED`** (G-RHO2 repaired, PR #902 @ `b06cbeb1`); TASK 3 CERTIFIED, `BIN-C-DISJOINT` adjudicated; **TASK 1 `SCAN-NOT-CERTIFIED`, no premise bin adjudicated.**
- **★ Standing conditionality (pre-arc, unchanged):** rides the **per-grade (L∞-across-grades)** member of an **open** fork; canon records cross-grade combine as *underdetermined at $O(\alpha)$*; under **normalized-L2-across-grades** the rotational transport collapses with the shared kernel. Engine receipt is **STRUCTURAL not numerical** — at $\kappa=0$ the members are numerically degenerate.
- **file:line:** `wall-taxonomy.md:499` (ruled text), `:454` (§10.2), `:528` (engine-residence correction); `research/2026-08-05_last-bond-kernel-collapse_result.md:24–33`; `_orchestration/docket-entries/2026-08-06-ruling-kernel-collapse-rescope-v2.md:13–29` + `-v2-correction.md` C1/C2.

### 4.2 NO-TWIST — srs point group 432 (PR #890)
**Statement.** Homogeneous squeeze of the chiral srs-z3 cell induces **no macroscopic micro-rotation**: $\tau=|\bar\varphi|/\varepsilon=3.3\times10^{-33}$ (isotropic), $1.2\times10^{-17}$ (uniaxial [001]). *"This is not a small number, it is a symmetry theorem: point group **432** is the one non-centrosymmetric crystal class that is not piezoelectric, and because 432 contains only proper rotations its axial rank-3 tensor $d_{ijk}\varepsilon_{ij}\varphi_k$ vanishes with its polar one. No homogeneous strain of any symmetry can turn the srs carrier."*
- **Surviving law two gradient orders down:** $\kappa/\varepsilon=\hat c_2 q^2/\ell_{node}$, $\hat c_2^{[001]}=+6.3377\times10^{-3}$; exponent **fitted not assumed** (2.0009/1.9983/1.9869); $\hat c_2$ sign-flips exactly under enantiomorph swap (5.6e-12 residual), **identically 0.0** on achiral diamond control.
- **Licenses:** $S_\kappa(\text{wall})=1$ — the leak number the kernel-collapse ruling needs; fills the fourth-channel row at $r_{sat}$.
- **Kills:** `LOCKSTEP-EXACT` and `LOCKSTEP-APPROX` both **REJECTED**.
- **file:line:** `research/2026-08-05_srs-twist-coefficient_result.md:12–34`, `:318`, `:325`; consumed at `.../bulk-impedance-at-saturation-boundary.md:53`, `:57`.

### 4.3 Two-band k·p — the photon-at-$c$ cancellation (#884)
Exact isotropic $O(k^2)$ branch table (verified as a characteristic-polynomial identity in 5 directions): $\omega\!\parallel\!k$: $2\gamma/I_\omega$ (mult 2) · $\omega\!\perp\!k$: $2\gamma/I_\omega+G_c/\rho$ (mult 4) · **transverse $u$ (photon): $G/\rho\equiv c_{EM}^2$** (mult 4) · longitudinal $u$: $10G/3\rho$ (mult 2).
- **Cancellation theorem:** *"The photon's $c_{EM}$ is protected, and the protection is a k·p cancellation."* Direct micropolar stiffness contributes $(G+G_c)/\rho$; level repulsion from the gapped $\omega$ manifold subtracts **exactly** $G_c/\rho$ ⇒ $v^2=G/\rho$ **for all moduli**, no tuning.
- **Co-result (kill-condition class):** $v_\perp^2-v_\parallel^2=G_c/\rho=(I_\omega/4\rho)m^2$ ⇒ a *massive* carrier cannot have a single limiting velocity, nor $c_{EM}$, for any positive moduli; both requires $G_c=0$ ⇒ gap closes.
- **Status:** BIN `FORM-REPRODUCED-V-MISMATCH`; provenance axis frozen pre-derivation as **FACTOR DERIVED / VALUE IMPORTED**. §6 qualifier: validity window closes before the relativistic regime opens ($k_{break}/k_{rel}=0.387,0.424$); full-BZ group velocity never exceeds $c_{EM}$ (0.612 vs 1) — mismatch is in the effective theory's invariant speed, **not** observed superluminal transport.
- **file:line:** `research/2026-08-05_two-band-kinematics_result.md:14–31`, `:95–130`, `:141`.

### 4.4 A-008 — the half-cover factor
**Statement.** $E_g=\hbar\omega_m$ (not $2\hbar\omega_m$); $\hbar\omega_m=2m_ec^2=1.022$ MeV = pair-creation threshold. Medium's rotational gap is the **higher** frequency; observable is the half-cover, $m_e=\text{medium}/2$, $\omega_m=2\omega_C$.
- **Corollary (RULED not ENG-CHOICE):** $\omega_m^2=4G_c/I_\omega$ and $\omega_m=2\omega_C\Rightarrow \boxed{G_c/I_\omega=\omega_C^2=1}$. *(Auditor re-derived independently; it closes.)*
- **Canonical A-008 resolution (Grant 2026-04-27):** $m_{\text{Cosserat}}=2$ = **frame** (medium full-cover SO(3)) twist rate; $\omega_C=m_e=1$ = **field** (spin-½ projection) frequency; the 2 IS the half-cover.
- **Status:** BIN `FACTOR-CLOSED-BY-A008`. Rival $G_c/I_\omega=1/4$ **ruled out by name** ("Reconciliation A", struck SUPERSEDED on the same adjudication). Corpus reconciliation total: all 14 non-lane $\omega_m\sim1$ MeV sites already read $\omega_m=2\omega_C$; $E_g=2.044$ MeV appears at exactly three sites, all the two-band FLAG-1 text + its two landings.
- **file:line:** `research/2026-08-05_a008-factor-propagation_note.md:19–34`, `:167`, `:170–175`, `:362–364` (FLAG-P), `:383`; canon `trampoline-framework.md:224–227`.

### 4.5 Cancellation / composition theorem — $p=(a+b)/2$ (iΩ lane)
**Statement.** $\omega_m(r)=2\omega_C S(r)^p$, $p=(a+b)/2$ ($a$ = $G_c(A)$ exponent, $b$ = $I_\omega(A)$ exponent). **Exact knife-edge at $p=2$**: $p<2$ ⇒ no intact cell ever open; $p>2$ ⇒ cells open; $p=2$ ⇒ verdict **mass-independent**, decided by pure numbers $\Omega,\theta$ (criterion $\Omega<4\theta$).
- **Delivered law (`LAW-CERTIFIED`):** conditional, factorized over ONE named canon-internal fork — **`b=0`** on the carve-out/disidentification arm, **`b=-1`** on the SYM-loading∧identification arm. *"No receipted-or-conditional reading reaches the `p = 2` knife."* Only flip route = the un-receipted CH-R transfer — **excluded from receipted structure, not disproven**.
- **⚠ Carved out of the closure (Tier-2 D2):** the **per-element pitch channel** ($g_c(\ell)$, $j(\ell)$) is a $b>0$ route no keying reason touches and canon defines neither dependence ⇒ **ABSENCE-OF-COVERAGE, NOT CLOSURE**; the bound $-1\le b\le0$ and every bin are conditional on it contributing zero.
- **Two-method absence receipt:** *"canon states no $I_\omega(A)$ grading law at all"* — P3/P4 zero hits on `git grep -P` and Python `re` across 4418 files.
- **file:line:** `research/2026-08-06_iomega-law_result.md:1`, `:26–58`, `:337–348`; knife `research/2026-08-05_approach-leak_result.md:44–68`; superseding certification `research/2026-08-06_approach-leak-v2_result.md:31–40` (`LEAK-CERTIFIED-V2`, `GAP-CLOSED` co-firing with `UNDERDETERMINED-CANON`).

### 4.6 Count-ratio lemma (D2)
**Statement.** On one intact sub-yield lattice, any COMMON POPULATION factor $n(A)\propto S^{-d}$ enters $G_c$ and $I_\omega$ identically and **cancels in the gap**: $(a,b)\to(a_c-d,\ b_j+d)$ leaves $p$ invariant, exactly (machine-checked at `G-PAIR` as a symbolic identity).
- **$z$-INDEPENDENT** (Tier-2 A8): any fixed coordination gives bonds-per-node $z/2$ into both slots; the $3/2$ is quoted only because $z=3$ is the ratified production carrier (`def-4b1a2c`).
- **Domain fence:** cold crystalline sub-yield; **premise (intact bond network) fails in Regime IV.** Boundary cell falls below $3/2$ by $O(1)$ — cannot flip any $p<2$ member.
- **NOT claimed:** per-element pitch does **not** cancel; FLAG-PITCH stays open. **Pairing rule:** a density factor cannot enter one slot only ⇒ $b=3$-with-$a=2$ has no CH-G reading and must route as CH-R.
- **file:line:** `research/2026-08-06_iomega-law_result.md:364–399`.

### 4.7 $\ell=2\to E\oplus T_2$ branching + `OVERLAP-NONZERO(2)` (#927)
**Statement (constructed by the lane; appears nowhere in corpus prior).** Under the point group **432 (O, chiral octahedral)**: $\ell=0\to A_1$, $\ell=1\to T_1$, **$\ell=2\to E\oplus T_2$ (5 = 2+3 ✓)**.
- **Licenses the selection-rule test:** a matrix element vanishes structurally iff the pattern's irrep is ABSENT from the propagating modes' shell restriction. The propagating longitudinal set is 432-invariant and contains the full $\ell$-tower, both $\ell=2$ irreps with weight $\propto j_2'(kR)\neq0$. **No irrep missing ⇒ no selection rule exists.**
- **Kills D1:** *"the common mode is a 1-D $A_1$ irrep so it cannot carry $\ell=2$"* crosses **Object A** (per-node port-amplitude space, what `clm-j550uh` decomposes) onto **Object B** (spatial fields). **G-CONFLATE: PASS.**
- **Verdict `OVERLAP-NONZERO(n=2)`**; matches continuum $|j_2'(kR)/j_0'(kR)|^2$ to 1.1–12.8 % with deviation tracking declared $O((k\ell_{site})^2)$ — the lattice **converges to** the continuum. #761 §2's imported "standard acoustic multipole radiation" step **CONFIRMED lattice-natively, import-tag DISCHARGED**.
- **Bankable shape:** $F(e)/F(0)=f_{PM}(e)+(5/96)e^2[1+O(e^2)]$; circularity gives **no** suppression. **Amplitude NOT-DERIVABLE** (inherited #919 R23).
- **file:line:** `research/2026-08-08_overlap-integral_result.md:19`, `:32–33`, `:145`, `:163`, `:179`.

### 4.8 Multipole ladder / Fork-F3 (the enclosed-charge ladder, #767 → #919 → #927)
**Statement.** With `mass = A1-dilatation`: monopole $\int\nabla\!\cdot\!u\propto M$, $\dot M=0$ ⇒ dead; dipole $\int x\nabla\!\cdot\!u\propto MX_{cm}$, $\ddot X_{cm}=0$ ⇒ dead; quadrupole $\int x_ix_j\nabla\!\cdot\!u=Q_{ij}$, $\dddot Q^{TL}\neq0$ ⇒ radiates. **Compression starts at quadrupole — SAME order as shear — $\Delta\ell=0$**, no $(\Omega/\omega_{ref})^{2\Delta\ell}$ suppression.
- **Licenses:** $\kappa_{env}^2=A_{ang}(c_S/c_P)^5$; the *order* leg of the pulsar exclusion chain.
- **Status:** ladder legs **`[derived]` + `[canon-read]`**; the coefficient $A_{ang}=2/3$ is the **q1-inherited ASSUMED symmetric-coupling normalization**, NOT from the K4/Ax4 Lagrangian. Lane verdict **BIN-1-CONDITIONAL**; `def-pndenv` **proposed, NOT SOLID**. Reproduced verbatim at #919 (`G-LADDER`); #919's verdict re-cut by Grant R23 to **`RADIATIVE(2)-on-the-order / NOT-DERIVABLE-on-the-amplitude`**.
- **file:line:** `research/2026-07-20_envelope-sector-reduction_result.md:12`, `:37`, `:126`; `research/2026-08-07_a1-port-sourcing_result.md:142–162`; `vocabulary-register.md:1083–1091`.

### 4.9 Domain-of-dependence theorem + residual-symmetry / Noether–Gauss (#939)
**(a) Residual-symmetry / Noether–Gauss (item 0, ADJUDICATED).** $\mathcal L=\tfrac12\varepsilon_0|\partial_t\mathbf A|^2-\tfrac{1}{2\mu_0}|\nabla\times\mathbf A|^2$ (`eq_axiom_3.tex:18`) is the **temporal-gauge (Weyl) Maxwell system taken literally**:
- R0a: exact residual symmetry $\mathbf A\to\mathbf A+\nabla\lambda(x)$ (time-independent) — machine-verified, exact zero.
- R0b: full time-dependent U(1) **FAILS**, exact remainder $\varepsilon_0(\partial_t\mathbf A)\cdot\nabla(\partial_t\lambda)+\tfrac12\varepsilon_0|\nabla(\partial_t\lambda)|^2$.
- R0c: the residual symmetry's Noether content is **precisely pointwise conservation of the Gauss function** $\nabla\cdot(\varepsilon_0\partial_t\mathbf A)$; on-shell by $\mathrm{div}\circ\mathrm{curl}\circ\mathrm{curl}\equiv0$.
- **Ontology split dissolving the corpus straddle:** the longitudinal *configuration* $A_L$ is gauge-soft; the longitudinal *momentum* $\Pi_L=\varepsilon_0\partial_tA_L=-\varepsilon_0E_L$ is residual-gauge-INVARIANT and physical. Both *"∇·A is gauge"* and *"the flat direction is a real state variable"* are true — of configuration and momentum respectively.
- Consequence: `:22` wrong at ACTION level / right on the constraint surface; `:27` wrong for full U(1) / right for the residual family. Repair text drafted §1.3 — **PROPOSAL, not an edit**.

**(b) Domain-of-dependence / no-signalling (item ii).** T1: local evolution with ONE finite characteristic speed $c$ (transverse; measured $0.9959c$) and **ZERO longitudinal characteristic speed** (static to $1.6\times10^{-19}$). T2: BC-LAW constraint conserved causally. T3: $|\mathbf S|=|-\rho c^2\dot u\times(\nabla\times u)|\le c\cdot(\text{energy density})$, longitudinal sector contributing **no flux term** ⇒ **no energy or information crosses outside the $c$-cone, at any frequency, and the bound sector's own transport speed is zero.** Retarded-fields control RUN: front $1.004c$, energy outside cone $\le1.1\times10^{-14}$. T4: the bound sector is **not an energy-carrying inter-event channel at ANY speed**.
- **★ CLASS.** Verdict RE-CUT at the lane's own Tier-2: the four-tuple is **`DERIVED-VIA-NEW-AXIOM(BC-SRC)` ×4**, not `DERIVED`. Three load-bearing pieces are **UNWRITTEN structure with no axiom preimage** (C2 deposit, C1 dress↔grade bridge, C5 grade-sector $\kappa$); the §4.2 EL identity was **machine-false as written** (C3/C14), repaired to the Kirchhoff $D^2$ form.
- **Ratification (R43, PR #940):** **clause S RATIFIED** ($\oint u\cdot\hat n=4\pi B(M)$ at genesis — *"particles are factory-charged"*); **clause G RATIFIED** ($u_0=-\lambda\nabla\varepsilon_{11}$ + κ-stiffened elliptic law; `backreaction.py`'s solve becomes axiom-licensed; falsifier $B=7\lambda GM/c^2$). **Tier A + clause Q PENDING**; LC-1's cell re-adjudicates *"only when ALL clauses are ratified."*
- **file:line:** `research/2026-08-10_bound-constitutive_result.md:19–29`, `:40–46`, `:52–56`; `_orchestration/docket-entries/2026-08-10-ruling-r43-sg-ratified.md:1–40`.

---

## §5 — WHAT CHANGED UNDER THE ARC

**Kernel-collapse: UNAFFECTED — verified.** Its conditionality (cross-grade combine member) predates the bound-sector arc and is untouched by #935/#939/#940. The only status motion is upward and pre-arc (`ROW-NOT-CERTIFIED` → `ROW-CERTIFIED` via #902).

**#935 consumer table, verbatim:** *"349 consumer rows — 59 DIES-WITH-THE-PHANTOM · 185 NEEDS-RE-DERIVATION · 105 SURVIVES-AS-RESPONSE · 0 BOUND-RESPONSE-INCONSISTENT candidates survived adjudication."* (`research/2026-08-09_bound-response_result.md:113`)

| Named structure | Bin | Consequence |
|---|---|---|
| $\sqrt{10/3}\,c$ radiative P-wave (`port-register.md:49`, `cosserat-mass-gap.md:132`, `constants.py:778`, `srs-band-structure.md:116`) | **DIES** | Channel-3 radiative column + four-speeds table lose derived status |
| `sup-3kq9w7` "propagating longitudinal-BULK compression mode IS REAL" **[CHORD tag]** | **DIES (chord content)** — top routed item | A tagged **chord** dies; its own text already read *"the DOF is added-by-design"*, quality `*pending*` |
| Seismological P/S far-field partition (`translation-circuit.md:157`, `translation-elastodynamics.md:19`) + `translation-circuit.md:974` acoustic-multipole incumbent | **DIES** | §4.8 keeps its *order* leg; the *partition* leg loses its substrate-side member |
| `def-pndenv` ponderomotive envelope coupling | **DIES (partition-consuming half)** | §4.8 coefficient leg |
| $\sqrt2\,c$ PORT/impedance speed + halo P9 near-field | **SURVIVES** — *"the roles ARE the bound-response roles"* | Op14/Op3 boundary machinery intact |
| $\Gamma_{bulk}\to-1$ at the wall (`bulk-impedance-at-saturation-boundary.md:39-42`) | **SURVIVES** in sign-invariant $|\Gamma|=1$ form | Explicit non-interaction with kernel-collapse's mirror |
| $V_{snap}$ = A1 bond-compliance normalizer | **SURVIVES** (*"a reactance of the BOUND sector — reactance without a wave"*) | Theorem 3.1′ / `clm-6t3p6x` inputs intact |
| `def-l0ngdu` *"∇·u propagates; ∇·A is gauge"* (**SOLID**) | **NEEDS-RE-DERIVATION** → *"∇·u is **bound**; ∇·A is gauge"* | A SOLID def-node's operative verb is under re-derivation; §4.9(a) supplies the replacement |
| `clm-uu1qbo` A1 row ($K=2G$ magic angle, $\sqrt2c_0$) | **NEEDS-RE-DERIVATION** | A1 identity survives; speed/modulus wiring is the import |
| MYTH-GUARD *"a genuine longitudinal DOF"* | **NEEDS-RE-DERIVATION** | anti-deletion point survives INTACT |
| The $/7$ static chain ($\nu=2/7$, $\kappa=c^4/7G$) | **SURVIVES byte-identical** (#939 item iv; every consumer static-only) | Op19 $\nu_{vac}=2/7$ unmoved |

> 🔴 **FAIL — the completeness framing on this table is WITHDRAWN by the lane itself.** `G-CONSUMER-2M` **RE-SCORED AT TIER-2: FAIL-AS-FROZEN, then REPAIRED**: 58 of 308 union files (100 hits) never classified; *"the two 'engines' consumed ONE shared pattern set (coverage-independence was never real)"*; a counter-sweep found 5 canon + 1 coded sites missed outright, **including two byte-twins of rows the audit itself classified**. Verbatim: *"The enumeration is PATTERN-BOUNDED, not exhaustive — the completeness framing is withdrawn; the demotion sweep should treat union+supplement as a floor."* (`:170`) **No inventory row may be marked "safe" on the strength of its absence from the 349.**

> **Arc-execution state.** R40 demotion sweep has run **batch 0 only** (`85e93cf5`): *"DEMOTES NOTHING — it verifies the worklist the demotions will run against."* Split reconciles exactly (349 = 59+185+105, three independent statements); 338 VERIFIED / 6 near / 5 real drifts. Banked method finding: **a single-probe site check on this table has a ~20× false-drift rate** (v1 115 ABSENT → v3 + hand-read 5 real).

---

## §6 — AUDITOR FINDINGS

**F1 — WARN: three arc theorems have no corpus home.** Two-method grep at the pin: **zero** manuscript/KB hits for `BC-SRC`, `domain-of-dependence`, `OVERLAP-NONZERO`, `count-ratio`. They live only in `research/` + `_orchestration/docket-entries/`. `NO-TWIST` and the two-band lane **do** have KB homes (`wall-taxonomy.md`, `bulk-impedance-at-saturation-boundary.md`, `translation-circuit.md:311` §4.6.4, `common/claim-quality.md:1633`). Per A47 v11c/v11d a research-doc-only result is not corpus-citable as canon. **Recommendation (implementer):** propagate with claim-IDs + solidity per the canonical-propagation gate, or tag research-grade in whatever inventory ships.

**F2 — FAIL: Op16 is inventory-ineligible as stated.** `operators.md:56` carries a live VACATED-CITE with an explicit prohibition. **Recommendation:** list with the vacated marker + §8 pointer, or omit; do not reconcile the three competing forms.

**F3 — WARN: foundational-machinery-register numbers pinned to `f556dcdc`, not `c03034eb`.** Every solidity / citation_count in §2 is a stale read by the register's own declaration. **Recommendation:** re-run `make verify-kb-metadata`, re-read claim records before print.

**F4 — WARN: A-008's generating argument survives the strike.** The leaf itself: *"the struck clause's own antecedent … — 'the time-averaged envelope completes a cycle per LOBE-VISIT' — is the reasoning that GENERATED the backwards direction. R16 struck the clause, not the lobe-counting argument; the argument stands as written and its re-derivation is routed, not performed here."* Also R16's stated rationale **did not reproduce at HEAD** and was corrected by R21 with a provenance correction. **Recommendation:** carry the routed re-derivation; do not present the direction as settled-with-mechanism.

**F5 — FLAG: provenance-tag collision on $G_c/I_\omega$.** A-008 derives it **RULED** ($=\omega_C^2=1$) and files `FLAG-P — provenance-tag understatement`; two-band `:53` tags values **`ENG-CHOICE placeholder`**; `last-bond-kernel-collapse_result.md:120` records *"NO GRADING LAW STATED"* with values *"separately ENG-CHOICE placeholder"*. Three tags, one quantity; R1 routes to *"auditor / doc lane"*. Surfaced, not resolved.

**F6 — FLAG: `def-l0ngdu` is SOLID and its operative verb is NEEDS-RE-DERIVATION.** A corpus-state contradiction (SOLID node under re-derivation by a merged lane; replacement wording proposed, not landed).

---

## §7 — OPEN QUESTIONS FOR GRANT

1. **`clm-law1ho` membership** — the register calls it *"the single strongest exclusion candidate"* and asks whether the Area-Theorem facet alone is machinery. Affects the 7/3 DERIVED/DEFINITIONAL headline.
2. **The cross-grade combine member** — kernel-collapse's row-4 carve-out and the iΩ lane's ARM-0 both ride the L∞ member of a fork canon calls *underdetermined at $O(\alpha)$*. Two independent arc results share one unresolved antecedent. Lane, or stay open?
3. **Does `DERIVED-VIA-NEW-AXIOM(BC-SRC)` count as "DERIVED-class"?** #939 flags this as needing an orchestrator ruling before LC-1's cell re-adjudicates; R43 confirms LC-1 fires only when **all** clauses ratify (Tier A + clause Q outstanding). Until then the domain-of-dependence theorem's class is `DERIVED-VIA-NEW-AXIOM`, not `DERIVED`.

---

## Key files (absolute)

- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/common/operators.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/common/foundational-machinery-register.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/common/theorem-thesaurus.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/common/port-register.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/common/wall-taxonomy.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/common/the-sourced-charge-no-go-cascade.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/common/vocabulary-register.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/common/interlock-register.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/common/trampoline-framework.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/theorem-3-1-q-factor.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/vol4/circuit-theory/ch1-vacuum-circuit-analysis/op21-multi-mode-mode-counting.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/vol1/operators-and-regimes/ch6-universal-operators/k4-port-irrep-decomposition.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/manuscript/ave-kb/vol3/cosmology/ch15-black-hole-orbitals/bulk-impedance-at-saturation-boundary.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/research/2026-08-05_last-bond-kernel-collapse_result.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/research/2026-08-05_srs-twist-coefficient_result.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/research/2026-08-05_two-band-kinematics_result.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/research/2026-08-05_a008-factor-propagation_note.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/research/2026-08-06_iomega-law_result.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/research/2026-08-08_overlap-integral_result.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/research/2026-08-09_bound-response_result.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/research/2026-08-10_bound-constitutive_result.md`
- `/Users/grantlindblom/AVE-staging/AVE-Core/_orchestration/docket-entries/2026-08-10-ruling-r43-sg-ratified.md`

---

**Lane-attribution note.** Operating in auditor lane; read-only. Every recommendation above (propagation of the four homeless arc theorems, the `verify-kb-metadata` refresh, the Op16 row disposition, the `def-l0ngdu` verb repair) requires implementer execution. No cross-lane authorization was cited; I have not drafted the inventory *document* — this is the audit-lane briefing from which the implementer would write it.
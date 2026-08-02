[↑ Ch.1 — Topological Matter](index.md)

<!-- kb-frontmatter
kind: leaf
claims: [clm-cmtwst]
-->

# The Common-Mode Twist-Ledger Theorem — the ground-$(2,3)$ twist cancels from every mass DIFFERENCE, iff it is generation-independent

> **Class tag (read this first).** **Derived algebraic identity, CONDITIONAL** — the theorem in §2 is exact algebra on a term list the corpus already carries, and its content lives entirely in (i) whose terms those are and (ii) the status of its one condition, which is **OPEN and forked** (§4). **This leaf resolves nothing.** It mints **one** claim (`clm-cmtwst`) for the conditional identity; everything else here is cited, not claimed. Per `ave-discrimination-check`: this is a **bookkeeping instrument** over in-corpus structure — **not** a chord, **not** a discriminating connection, **not** an emergence result, and it originates **no** numerical commitment.
>
> **Provenance.** Grant, 2026-08-02, verbatim `[sic]`: *"this sounds incredibly important to document and derive/cannonize for the paperclip/common mode"*. The **picture** is Grant's (§5); the **derivation below is this lane's**.

> **★ FENCE — branch-pending cites.** Two of this leaf's anchors are **not on `origin/main` at writing time** and are marked `[branch:#NNN]` at every use:
>
> - **`[branch:#833]`** — `research/2026-08-02_twist-ledger-audit.md` *(deliberately NOT a Markdown link: the path does not resolve on `main` yet, and a link that dangles is worse than a path that announces itself; wire it at merge)*, the twist-energy ledger audit whose verdict (**UNACCOUNTED**) supplies the *existence-in-question* status of this leaf's $E_{\text{twist}}$ term and the 12-order magnitude bracket. That doc is **implementer-lane and NOT adversarially reviewed**; its verdict is **pending its own audit**. Nothing here upgrades it.
> - **`[branch:#832]`** — the paperclip analogy at [`common/electron-plumbing-primer.md`](../../../common/electron-plumbing-primer.md) **Step 3.5**, the walk-ratified physical picture §5 connects to. That section mints no claim and carries its own fence on the same open item.
>
> **Finalization note (post-merge, owed by whoever lands second).** When #832 and #833 merge, (a) drop the `[branch:#NNN]` tags here and date the currency touch; (b) land the **reciprocal pointer** from the primer's Step 3.5 to this leaf; (c) add the **item-13 tracker note** recording that the bookkeeping instrument now exists. (b) and (c) are recorded as post-merge follow-ons in this lane's docket fragment — they are **not** performed here, because #832 owns both files.

---

## §1 — The ledger, per generation

Write the rest-energy budget of charged lepton generation $i \in \{e, \mu, \tau\}$, all three of which the corpus places on the **same** ground $(2,3)$:

$$\boxed{\; m_i c^2 \;=\; E_{\text{slosh},i} \;+\; E_{\text{twist},i} \;+\; n_i\,\varepsilon_{\text{torsion}} \;}$$

Every term is the corpus's own object, with its own status:

| Term | What it is | Canon anchor | Status |
|---|---|---|---|
| $E_{\text{slosh},i}$ | the reactive LC store — the standing wave's magnetic⊕electric slosh, $\tfrac12 L_{\text{tube}}I_{\max}^2 = \tfrac12 C_{\text{tube}}V_{\text{peak}}^2$, closed as $E_L = E_C = \tfrac12 m_ec^2$ | [`mass-closure-theorem.md`](mass-closure-theorem.md):52,:54; [`relativistic-inductor-newtonian-limit.md`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor-newtonian-limit.md):24 | **the term canon actually has.** Class A (definitional identity) — the closing step is *"reached by identifying … (no quantity computed)"* (`clm-ka5zdx` rationale, [`vol2/claim-quality.md`](../../claim-quality.md):1256) |
| $E_{\text{twist},i}$ | the couple-stress energy of the **ground** $(2,3)$ winding on the Cosserat T2 grade | the grade is real and *"COSTLY (couple-stress energy via $G_c$)"* ([`trampoline-framework.md`](../../../common/trampoline-framework.md):559); the ground twist is geometrically nonzero, $\mathrm{Tw}=q/p$ = $540°$/rev ([`research/2026-06-07_vacuum-characterization-program.md`](../../../../../research/2026-06-07_vacuum-characterization-program.md):59); the energy form is the engine's `gamma kappa · kappa` ([`cosserat_field_3d.py`](../../../../../src/ave/topological/cosserat_field_3d.py):713) | **EXISTENCE-IN-THE-BUDGET IS THE OPEN QUESTION.** `[branch:#833]` returns **UNACCOUNTED** — pending its own audit. Canon's sharpest statement is an **exclusion-by-declaration** of a nonzero quantity: the winding sector's gapped mechanical mass is *"NOT the electron's rest-energy store"* ([`master-equation.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):41) |
| $n_i\,\varepsilon_{\text{torsion}}$ | the Cosserat torsional **excitation** ladder: $n_e = 0$, $n_\mu = 1$, $n_\tau$ unfixed | *"$(2,3)$ trefoil + 0 Cosserat torsion quanta"* / *"+ 1 Cosserat torsion quantum"* ([`torus-knot-uniqueness.md`](torus-knot-uniqueness.md):106,:107); *"The lepton family climbs a Cosserat-torsion ladder on fixed (2,3) topology"* (`:102`) | **Class C** — canon's own tag: *"matched closed-form CONSISTENCY — NO solver"* ([`lepton-spectrum.md`](../ch06-electroweak-higgs/lepton-spectrum.md):84); the sector→generation identification is *"asserted, not derived from the four axioms"* (`clm-zw6mut`, [`vol1/claim-quality.md`](../../../vol1/claim-quality.md):544; id home `:521`) |

**Why the three generations share one ground.** *"Higher-mass leptons stay at (2,3) topology — they don't climb the (p,q) torus-knot ladder; they climb the Cosserat-torsion excitation ladder"* ([`torus-knot-uniqueness.md`](torus-knot-uniqueness.md):110), and the muon *"possesses the same real-space unknot topology and the same $(2, 3)$ phase-space winding pattern as the electron, but with one quantum of Cosserat torsional excitation added on top"* ([`vol4/…/ch14/theory.md`](../../../vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md):43). **Shared ground $(2,3)$ is the premise the whole leaf turns on**, and it is canon's, not this lane's.

> **★ Honesty carve on the third term (this lane's, surfaced not smoothed).** Writing the excitation term as $n_i\,\varepsilon_{\text{torsion}}$ presumes **equal rung spacing** $\varepsilon_{\text{torsion}}$. **Canon's actual bookings are multiplicative closed forms and are NOT equally spaced**: $m_\mu = m_e/(\alpha\sqrt{3/7})$ and $m_\tau = m_e\,p_c/\alpha^2$ ([`lepton-spectrum.md`](../ch06-electroweak-higgs/lepton-spectrum.md):39,:61) — adjacent ratios $209.3$ and $16.45$ (`:70`). The honest general form is therefore $E_{\text{exc}}(n_i)$ with $E_{\text{exc}}(0) = 0$ (canon's own $n_e = 0$, `:21`: *"The electron is the $0_1$ unknot ground state. No torsional excitation is present"*), of which the linear writing is one special case. **The theorem below does not need equal spacing** — it needs only that the excitation term be a function of $n$ alone. The boxed linear form is retained because it is the form the ordering asks for and the form the paperclip picture renders (§5); read $n_i\varepsilon_{\text{torsion}} \equiv E_{\text{exc}}(n_i)$ wherever the equal-spacing reading would do work it has not earned.

> **Scope of "$m_ic^2 = \ldots$".** The ledger is the **hypothesis-form** of the budget: *if* the ground twist is priced into the invariant mass at all, this is the slot it occupies. It is **not** an assertion that it is. Canon's own position — that the winding-sector mechanical mass sits **outside** $m_ec^2$ by grade-orthogonality declaration ([`master-equation.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):41,:42; `A1 ⊥ T2`, `:20`) — is the $E_{\text{twist},i} \equiv 0\ \forall i$ reading of the same ledger, and §3 shows the theorem's conclusion covers that reading too.

> **⚑ FLAG (surfaced, NOT repaired) — the ledger has three slots; canon's closure has two, and they already sum to the whole.** [`relativistic-inductor-newtonian-limit.md`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor-newtonian-limit.md):24 writes the budget as a **closed** sum over named sectors: *"$E_L = E_C = \frac{m_e c^2}{2}, \qquad E_L + E_C = m_e c^2.$"* — inductive ⊕ capacitive, $\tfrac12 + \tfrac12 = 1$, **no third slot remains**. The §1 ledger's second and third terms therefore have **no home in canon's own closure as written**. Both sides are quoted here with their paths and **neither is edited to match the other** (flag-don't-fix): either the closure is a two-sector *identification* that was never evaluated as a sum — which is exactly what its own claim-quality rationale says, *"reached by identifying … (no quantity computed)"* ([`vol2/claim-quality.md`](../../claim-quality.md):1256) — or the extra terms are genuinely zero, which no site derives. **This leaf does not choose.** It is recorded because a reader who takes canon's closure at face value should see immediately that the §1 ledger is a *hypothesis-form* extension of it, not a restatement.

## §2 — The theorem (derived, algebraic, conditional)

> **[Resultbox]** *Common-Mode Twist-Ledger Theorem*
>
> Let $i, j$ be any two members of a family sharing the ground $(2,3)$, each budgeted as in §1. Then **identically**
> $$\Delta m_{ji}\,c^2 \;\equiv\; (m_j - m_i)c^2 \;=\; \underbrace{\Delta E_{\text{slosh}}}_{\text{LC store}} \;+\; \underbrace{\Delta n\,\varepsilon_{\text{torsion}}}_{\text{excitation ladder}} \;+\; \underbrace{\big(E_{\text{twist},j} - E_{\text{twist},i}\big)}_{\text{ground-twist bracket}}$$
> and the ground-twist bracket vanishes **for every pair** *if and only if* $E_{\text{twist}}$ is **generation-independent**:
> $$\textbf{(C)}\qquad E_{\text{twist},i} = E_{\text{twist}}^{(2,3)} \quad\text{for all } i \text{ sharing the ground } (2,3).$$
> Under **(C)**:
> $$\boxed{\;\Delta m_{ji}\,c^2 \;=\; \Delta E_{\text{slosh}} \;+\; \Delta n\,\varepsilon_{\text{torsion}}\;}$$
> — **the ground-twist term is absent from the difference, exactly.**

**Proof.** Subtract the §1 ledger for $i$ from the ledger for $j$; the three brackets are the three term-wise differences. Sufficiency of **(C)**: if $E_{\text{twist},j} = E_{\text{twist},i}$ the third bracket is $0$. Necessity: a real-valued function on a finite set has *all* pairwise differences zero **iff** it is constant; so if the bracket vanishes for every pair, $E_{\text{twist}}$ is constant across the family. $\blacksquare$

**Robustness to the §1 carve.** The proof never uses equal rung spacing. Replacing $n_i\varepsilon_{\text{torsion}}$ by a general $E_{\text{exc}}(n_i)$ gives $\Delta m_{ji}c^2 = \Delta E_{\text{slosh}} + [E_{\text{exc}}(n_j) - E_{\text{exc}}(n_i)] + (\text{twist bracket})$, and the theorem is word-for-word the same.

> **Class (consistency-vs-emergence): CLASS-A/derived-algebraic, CONDITIONAL — deliberately the lowest interesting tier.** The algebra is a subtraction; nobody should read it as a result. Its **content** is entirely in the two things the algebra is *about*: (i) the ledger's term list is **canon's own** and canon's own closure carries **no third slot** (T3's $\tfrac12 + \tfrac12 = 1$, [`relativistic-inductor-newtonian-limit.md`](../../../vol4/circuit-theory/ch1-vacuum-circuit-analysis/relativistic-inductor-newtonian-limit.md):24), and (ii) the condition **(C)** is an **open physical question**, not a lemma (§4). **No solver. No numerical commitment. No CODATA input. Nothing measured, nothing predicted.**

## §3 — Corollary: the ground twist is the corpus's structural blind spot

**COROLLARY (blind spot).** Under **(C)**, every observable that is a function of **mass differences within the $(2,3)$ family** is **structurally blind** to $E_{\text{twist}}^{(2,3)}$ — its value cannot appear, at any magnitude, with any sign. Concretely this covers:

- the ladder's **rung spacings** $m_\mu - m_e$, $m_\tau - m_\mu$;
- **decay energetics** inside the family — e.g. $\mu^- \to e^-\bar\nu_e\nu_\mu$ releases $Q = (m_\mu - m_e)c^2$ up to neutrino masses.

**And the blindness covers BOTH ways the term can be innocuous.** The corollary is not one branch of a fork; it absorbs two:

| If the ground twist is… | then the bracket is… | differences see… |
|---|---|---|
| **outside** the invariant (canon's grade-orthogonality exclusion, [`master-equation.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):41) — i.e. $E_{\text{twist},i}\equiv 0\ \forall i$ | $0$, trivially | nothing |
| **inside** and generation-**independent** (**C**) | $0$, by the theorem | nothing |
| **inside** and generation-**dependent** | $\neq 0$ | **the term** — this is the only case in which differences are a probe |

**★ Why the hole could persist unnoticed (explanation offered, tagged — not a claim).** The `[branch:#833]` audit's UNACCOUNTED verdict is about a term that *hides exactly where the corpus looks*. The empirical checks that bear on the lepton sector concentrate on the ladder and on decay energetics — the **difference** face — and the theorem says that face cannot see the term under either innocuous reading. This is a **consistency-class historical explanation**, not evidence for or against the term's existence; the audit's verdict stands or falls on its own review.

> ### ★ The carve the corollary needs — DIFFERENCES are blind, RATIOS are NOT
>
> **Recorded as a refinement of this lane's own dispatch wording, flag-don't-fix.** The ordering called the generation ladder a mass-**difference** observable. That is right for one of its two faces and wrong for the other, and the distinction is load-bearing:
>
> - **Rung-SPACING face (a difference): BLIND.** $m_\mu - m_e$ etc. — the theorem applies.
> - **Rung-RATIO face (canon's ACTUAL booking): SIGHTED.** Canon books the ladder **multiplicatively** — $m_\mu/m_e = 1/(\alpha\sqrt{3/7})$ ([`lepton-spectrum.md`](../ch06-electroweak-higgs/lepton-spectrum.md):39), $m_\tau = m_e\,p_c/\alpha^2$, adjacent ratios $209.3$ / $16.45$ (`:70`). **A common additive term does not cancel from a ratio:**
>   $$\frac{m_j}{m_i} \;=\; \frac{E_{\text{slosh},j} + E_{\text{exc}}(n_j) + E_{\text{twist}}^{(2,3)}}{E_{\text{slosh},i} + E_{\text{twist}}^{(2,3)}}.$$
>
> **What the ratio face is actually sensitive to (stated precisely, so it is not over-read).** The *measured* ratio is whatever it is; the twist term cannot change a measurement. What the ratio face exposes is **canon's mechanism attribution**: the phrase *"No torsional excitation is present"* for the electron ([`lepton-spectrum.md`](../ch06-electroweak-higgs/lepton-spectrum.md):21) is exact as a statement about the **quantum count** ($n_e = 0$, [`torus-knot-uniqueness.md`](torus-knot-uniqueness.md):106) and is **not** a statement about **energy** unless $E_{\text{twist}}^{(2,3)} \ll m_ec^2$. If the ground twist is inside and not small, "torsion-free anchor" is an energy misnomer even though the quantum-count booking is untouched. **That magnitude question is `[branch:#833]`'s and Grant's, not this leaf's** — the audit's §4.2(b) argues it; nothing here adopts, strengthens, or extends that argument.

## §4 — The condition fork: what **(C)** actually requires, and what canon says

### 4.1 The condition reduces to one geometric question

$E_{\text{twist}}$ has exactly three inputs, and two of them are already generation-common:

- $\gamma_c$ — a **substrate modulus** (couple-stress stiffness). A property of the vacuum, not of the particle: **common by construction**.
- $\mathrm{Tw}$ — the twist number, fixed by the shared ground $(2,3)$ at $q/p = 3/2$ turns $= 540°$ per toroidal revolution ([`research/2026-06-07_vacuum-characterization-program.md`](../../../../../research/2026-06-07_vacuum-characterization-program.md):59): **common because the ground is shared**.
- the configuration's **real-space metric scale** — the only place a generation index can enter.

So **(C) holds iff the $(2,3)$ configuration's real-space scale is generation-common** (or, weaker, iff $E_{\text{twist}}$ happens to be scale-invariant). Evaluating the corpus's energy form $E = \int \gamma_c\,|\kappa|^2\,dV$ (the engine's `gamma kappa · kappa`, [`cosserat_field_3d.py`](../../../../../src/ave/topological/cosserat_field_3d.py):713 — no $\tfrac12$, the engine's convention) on canon's own tube geometry — loop circumference $C_{\text{loop}}$, tube radius $r_0 = C_{\text{loop}}/2\pi$ ([`electron-unknot.md`](electron-unknot.md):13), $\kappa = 2\pi\,\mathrm{Tw}/C_{\text{loop}}$, $V_{\text{tube}} = \pi r_0^2 C_{\text{loop}} = C_{\text{loop}}^3/4\pi$ — gives the closed form

$$E_{\text{twist}} \;=\; \gamma_c\,\kappa^2 V_{\text{tube}} \;=\; \frac{\gamma_c\,(2\pi\mathrm{Tw})^2}{4\pi}\,C_{\text{loop}} \;\;\overset{\mathrm{Tw}=3/2}{=}\;\; \frac{9\pi}{4}\,\gamma_c\,C_{\text{loop}}\,.$$

**$E_{\text{twist}}$ is LINEAR in the configuration's loop circumference.** Equivalently, under isotropic rescaling by $s$ at fixed twist number: $\kappa \to \kappa/s$, $V \to s^3V$, so $E \to s\,E$. **It is not scale-invariant; it rides the scale.**

> **Two caveats on the exponent, both surfaced.** (a) The $\propto C_{\text{loop}}^{+1}$ law assumes the tube's cross-section scales **with** the loop, which is canon's own electron geometry ($r_0 = C_{\text{loop}}/2\pi$). Holding the cross-sectional **area** fixed instead gives the textbook torsion-spring $E \propto 1/C_{\text{loop}}$ — **opposite sign of exponent**. Canon does not state which reading applies to a heavier lepton, so **both exponents are live**; what is *not* live is scale-invariance, which neither reading gives. (b) The evaluation is a **real-space couple-stress integral**, so it inherits the A46 coordinate question: the $(2,3)$ is a **phase-space** winding ([`electron-identification.md`](electron-identification.md):31), while canon separately assigns it a **real-space mechanical-ω image on the couple-stress/curvature grade** ([`master-equation.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):24). `[branch:#833]` §3.4 ran `phase-space-coordinate-check` on exactly this and reported PASS — **cited as pending, not adopted**. **§2's theorem is coordinate-agnostic** (pure algebra on a term list) and does **not** depend on that check; **only this §4 scaling analysis does.**

**Independent cross-check of the closed form (arithmetic, not a claim).** At the lattice-scale $\gamma_c = G_{\text{vac}}\,\ell_c^2$ with $\ell_c = \sqrt6\,\ell_{node}$ ([`constants.py`](../../../../../src/ave/core/constants.py) `ELL_C`) and $C_{\text{loop}} = \ell_{node}$, the closed form gives $\tfrac{9\pi}{4}\gamma_c\ell_{node} = 1.7361\times10^{-12}$ J $= 21.206\,m_ec^2$ — **reproducing `[branch:#833]`'s R1a driver row to every digit that doc reports** ($1.736\times10^{-12}$ J, $2.12\times10^{1}\,m_ec^2$), reached here **analytically** where that doc reached it **numerically**. Recorded as a **consistency receipt between two independent evaluations of the same integrand**, carrying that doc's pending status; it is **not** an endorsement of the magnitude, which is gated (§6).

### 4.2 What canon says about the muon's real-space scale — the sweep

**Two-method, run at base `50da2eda`.** Canon is **silent on the load-bearing input**, and its two relevant *general* statements pull in **opposite** directions.

**Scale-COMMON evidence (Branch A):**

| Cite | Verbatim / content | Weight |
|---|---|---|
| [`lepton-spectrum.md`](../ch06-electroweak-higgs/lepton-spectrum.md):17 | *"In all three lepton generations, the geometric deformation (twist, curvature) describes a pattern of **dielectric saturation density** … The nodes themselves remain fixed at $l_{node}$ spacing (Axiom 1). The muon's 'twist' is a helical modulation of impedance density wound around the unknot loop … **Neither involves physical displacement of lattice nodes.**"* | **Strongest.** Explicitly *all three generations*; lattice fixed; the excitation is impedance-density, not geometry |
| [`scale-invariance.md`](../../../vol1/operators-and-regimes/ch5-universal-spatial-tension/scale-invariance.md):18 | muon and tau *"are excitations of this **same unknot geometry** into higher Cosserat coupling sectors"* | Strong, but "geometry" is not disambiguated shape-vs-metric |
| [`vol4/…/ch14/theory.md`](../../../vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md):43 | *"the **same real-space unknot topology** and the same $(2, 3)$ phase-space winding pattern"* | **Topology only** — strictly silent on metric scale |

**Scale-RIDES-THE-MASS evidence (Branch B):**

| Cite | Verbatim / content | Weight |
|---|---|---|
| [`electron-unknot.md`](electron-unknot.md):19,:22,:28 | the general law: *"The topological energy of a **scale-invariant** $1/r$ loop is given by $E = T_{max,g} / C_{loop}$"* with $T_{max,g} = \hbar/c$, solved as $m_ec^2 = (\hbar/c)/C_{loop} \Rightarrow C_{loop} = \hbar/(m_ec)$ | **Strongest.** If the law is general — and [`scale-invariance.md`](../../../vol1/operators-and-regimes/ch5-universal-spatial-tension/scale-invariance.md):11 asserts *"the identical $1/r$ tensor calculates the mass of an elementary particle and the mass of a complex atomic nucleus"* — then $C_{\text{loop},\mu} = \hbar/(m_\mu c) = \ell_{node}/206.77$ |
| [`proton-identification.md`](../ch02-baryon-sector/proton-identification.md):46 | *"Charge radius $D_p = 4\lambda_p = 0.841$ fm … $\lambda_p = \hbar/(m_p c)$ = proton Compton wavelength \| ✅ axiom-derived"* | **Sector precedent:** canon *does* scale a real-space body size inversely with mass, elsewhere |
| [`proton-identification.md`](../ch02-baryon-sector/proton-identification.md):23 | the resulting object is **sub-node**: *"$\approx 460\times$ smaller than one $\ell_{node} = 386$ fm"*, and *"The real-space sub-node geometry (why a $0.841$ fm body) is an OPEN item"* | Shows the same collision is **already open** in the baryon sector |

**★ The collision, stated plainly.** Canon's $1/r$ law says *heavier ⇒ smaller loop*. Canon's Axiom-1 floor says *"The minimum discrete diameter of the flux tube is normalised to one fundamental lattice pitch ($d \equiv 1 l_{node}$)"* ([`electron-unknot.md`](electron-unknot.md):59) — the electron sits **at** that floor. A muon loop at $\ell_{node}/207$ would be **below** it. **A Branch-B muon therefore inherits exactly the sub-node open item canon already carries for the proton** — it is not a new problem, it is the lepton-sector face of an existing one.

**Absence result (two-method, commands shown).** No corpus site states the muon's real-space loop circumference, ring radius, or tube size, and none writes $\lambda_\mu = \hbar/(m_\mu c)$ as a geometric size.

```
# Method A (git grep on the tracked tree, base 50da2eda), cwd = repo root:
git grep -n -I -iE '(muon|mu-lepton).{0,120}(ring|loop|tube).{0,40}(size|radius|circumference|smaller|larger)' \
  -- manuscript/ research/ src/                                     -> 0 hits
git grep -n -I -E 'lambda_\\?mu|\\lambda_\{?\\mu' -- manuscript/ research/   -> 0 hits
# Method B (filesystem grep, same cwd):
grep -rn -iE 'muon.{0,80}(reduced compton|compton wavelength|ring radius|loop radius)' manuscript/ research/ src/
  -> 1 hit: research/2026-07-10_x42-atomic-eigencavity_prereg_FROZEN.md:92 — the muonic-hydrogen ORBIT,
     not the muon's own body. Does not bear on the question.
```

### 4.3 The two branches and their consequences — **neither is adopted here**

> **BRANCH A — scale-common (or otherwise scale-invariant $E_{\text{twist}}$).**
> **(C) holds exactly.** The ground-twist bracket vanishes identically; **every mass difference in the family is blind to it, at any magnitude.** The generation ladder's **rung spacings** are undisturbed whatever the term turns out to be worth.
> **Item 13 reduces to a GROUND-LEDGER question only** — is the single common $E_{\text{twist}}^{(2,3)}$ inside or outside $m_ec^2$? — with **no ladder consequence**.
> **What Branch A does NOT protect:** the **ratio face** (§3 carve). Under Branch A with the term *inside* and not small, *"torsion-free ground state"* remains an accurate **quantum-count** statement and an inaccurate **energy** statement. That residue is gated on the magnitude (§6), not on the fork.

> **BRANCH B — $E_{\text{twist}}$ rides the scale** (the derived $\propto C_{\text{loop}}^{\pm1}$ behaviour of §4.1, e.g. a $\gamma_c/\ell^2$-class stiffness on a Compton-scaled loop).
> **(C) fails; the twist term PARTICIPATES in mass differences.** With the Compton reading $C_{\text{loop},\mu} = C_{\text{loop},e}/206.77$ and the isotropic $\propto C_{\text{loop}}$ law:
> $$E_{\text{twist},\mu} - E_{\text{twist},e} \;=\; -\,E_{\text{twist},e}\left(1 - \tfrac{1}{206.77}\right) \;=\; -0.9952\;E_{\text{twist},e}.$$
> The first rung's spacing then carries a term of magnitude $\approx E_{\text{twist},e}$ with a **minus** sign — i.e. **the ladder's booking would need re-examination**, since canon's closed form is fitted against the *measured* spacing with no such term in it.
>
> **★ The $\pm1$ exponent ambiguity is NOT symmetric in consequence — do not read the isotropic number as a bound.** The line above uses the **isotropic** $\propto C_{\text{loop}}$ reading, which is the *gentle* one: the heavier lepton's twist store **shrinks**, so the term is bounded by $E_{\text{twist},e}$. The **fixed-cross-section** reading ($\propto 1/C_{\text{loop}}$, §4.1 caveat (a)) runs the other way and is **violent**: $E_{\text{twist},\mu} = 206.77\,E_{\text{twist},e}$, giving $+205.77\,E_{\text{twist},e}$ in the same rung — two orders larger than the isotropic case and **positive**. Both exponents are live because canon does not state whether a heavier lepton's tube radius tracks its loop. **The exponent question is therefore load-bearing in its own right and is part of what §4.3's routing asks Grant**, not a detail downstream of the branch call.

**★ The fork and the magnitude gate MULTIPLY — they do not add.** Branch B's teeth are entirely conditional on the **already-open** $\ell_c$ adjudication (§6). Carrying `[branch:#833]`'s bracket through the factor above, **with that doc's pending status attached to every number**:

| $\gamma_c$ reading `[branch:#833]` | $E_{\text{twist},e}$ | Branch-B contribution to the $n=0\to1$ spacing | vs. the measured $\approx 205.8\,m_ec^2$ |
|---|---|---|---|
| **lattice-scale** ($\ell_c = \sqrt6\,\ell_{node}$) | $2\times10^{1}$ – $2\times10^{2}\ m_ec^2$ | $-(21$ to $225)\,m_ec^2$ | **$10\%$ – $110\%$ of the spacing — the booking needs re-examination** |
| **weak-scale** ($\ell_c \approx 10^{-18}$ m) | $\approx 2.4\times10^{-11}\ m_ec^2$ | $\approx -2.4\times10^{-11}\,m_ec^2$ | **invisible** |

*(Third column uses the **isotropic** exponent. On the fixed-cross-section exponent the lattice-scale row grows by a further $\times206.77$ and flips sign — see the asymmetry note above. The weak-scale row stays invisible on either exponent, $\lesssim 5\times10^{-9}\,m_ec^2$.)*

**Read this table as a conditional structure, not a result.** Every entry inherits (i) `[branch:#833]`'s pending verdict, (ii) an unadjudicated $\ell_c$ referent, and (iii) an unadopted branch. **The one durable statement is the multiplication itself:** *the ladder is disturbed only if **Branch B holds AND the lattice-scale $\ell_c$ is the electron's**. Either one alone leaves the ladder undisturbed.* That is the leaf's most useful output after the theorem, and it is what routes the fork.

**★ ROUTED TO GRANT (fork open, neither branch adopted).** *When the clip is smaller, does the metal notice over the same distance?* Canon says the lattice nodes stay put and the muon's excitation is impedance-density modulation (Branch A); canon also says the loop's circumference is set by $\hbar/(mc)$ through a law it calls scale-invariant and universal (Branch B). **Which one owns the heavy lepton's body?** Adopting either here would silently refill a slot Rule 12 says stays empty.

## §5 — The paperclip connection

The walk-ratified physical picture is the **paperclip** — canonized as a *pedagogical analogy, no claim minted* at [`common/electron-plumbing-primer.md`](../../../common/electron-plumbing-primer.md) **Step 3.5** `[branch:#832]`. The picture is **Grant's**, recorded there verbatim `[sic]`; the ordering that produced *this* leaf is Grant's too, verbatim `[sic]`: *"this sounds incredibly important to document and derive/cannonize for the paperclip/common mode"*. **The derivation in §§1–4 is this lane's.**

The ledger's three terms are the clip's three parts:

| Paperclip | Ledger term | §4 status |
|---|---|---|
| the **base pre-load** — the spring tension already in the wire once the ends catch | $E_{\text{twist}}^{(2,3)}$ | existence-in-the-budget **open** `[branch:#833]`; magnitude **gated** (§6) |
| the **crankable quanta** — turns you wind in on top | $n_i\,\varepsilon_{\text{torsion}}$ | canon's ladder; Class C ([`lepton-spectrum.md`](../ch06-electroweak-higgs/lepton-spectrum.md):84) |
| the **catch** that will not release | the $(2,3)$ / $\mathrm{Lk}$ integer — *"$\mathrm{Lk} = \mathrm{Tw} + \mathrm{Wr}$ … two lawful readings of the one conserved linking number $\mathrm{Lk}$ (= charge)"* ([`chirality-and-antimatter.md`](chirality-and-antimatter.md):10, Grant-adjudicated R1) | canonical; untouched here |

**The common-mode statement, in the picture:** *every clip in the family carries the same base pre-load.* **That is Branch A's physical reading** — and §2 says that if it is true, no amount of weighing one clip against another can ever tell you what the pre-load is worth.

**Branch B, in the picture:** *bigger clips hold **more** pre-load* — and §4.1 makes that quantitative rather than metaphorical: for a tube whose cross-section scales with its loop, $E_{\text{twist}} \propto C_{\text{loop}}$, so the **electron** (the biggest clip in the family) holds the **most**, and a Compton-scaled muon holds $\approx 1/207$ as much. *(The dispatch's wording left the direction open as "less/more"; the derived isotropic law picks **more-for-bigger**, and the fixed-cross-section alternative picks **less-for-bigger** — §4.1 caveat (a). The direction is a **consequence of which tube-scaling reading is right**, not a free choice.)*

**What the picture does NOT decide.** It is pedagogically live under both branches, and it was ratified on that basis: Step 3.5's own `★ THE FENCE` block states that whether the base twist's spring energy sits inside $m_ec^2$ is **OPEN under item 13** and is not pre-empted `[branch:#832]`. **This leaf changes the ledger, not the picture.**

## §6 — Fences

1. **The $E_{\text{twist}}$ MAGNITUDE is UNADJUDICATED — by twelve orders.** Canon carries **two** Cosserat lengths under one symbol, both written $\ell_c = \sqrt{\text{couple-stress}/\text{shear}}$, and flags the collision **in code**, verbatim ([`src/ave/core/constants.py`](../../../../../src/ave/core/constants.py):331-337):
   > *"⚠ DISAMBIGUATION (two-objects-one-symbol — flag-don't-fix): this ELL_C (≈ 9.46e-13 m, the K4 LATTICE-scale Cosserat coupling length, ≈ 2.45 node spacings) is NOT the weak-force-range "l_c = √(γ_c/G_vac) ≈ 1e-18 m" used in vol9 ch9/ch10 + gauge-boson-masses.md:39. Same symbol and same formula STRUCTURE (√(couple-stress/shear)), but ~6 orders of magnitude apart and a different physical referent. Surfaced for auditor adjudication (vol9 ch9/ch10 carry the disambiguation footnote); not silently merged."*

   Since $E_{\text{twist}} \propto \gamma_c \propto \ell_c^2$, the two readings are **12 orders apart** — the bracket `[branch:#833]` reports. **This leaf adjudicates nothing about it** and takes no position on which referent is the electron's. The weak-scale referent's home is [`gauge-boson-masses.md`](../ch05-electroweak-mechanics/gauge-boson-masses.md):39.
2. **`[branch:#833]`'s UNACCOUNTED verdict is PENDING ITS OWN AUDIT.** It is implementer-lane, not adversarially reviewed. This leaf uses it **only** to mark the $E_{\text{twist}}$ term's existence-in-the-budget as *in question* — the exact status that makes a conditional theorem the right instrument. **If that audit is overturned, §2 is unaffected** (the theorem is conditional on **(C)**, not on the audit) and only §1's status column and §4.3's magnitude table change.
3. **Nothing here resolves open item 13** (sector-of-storage; `⚑ OPEN-IN-WALK`, Grant is walking it). **This leaf gives item 13 its bookkeeping instrument**: the theorem says which observables can and cannot bear on it, and §4.3's multiplication says what would have to be true *jointly* for the ladder to be disturbed. **That is a narrowing of the search space, not a ruling.**
4. **No new axiom (A44).** The diagnosis in this space is unbuilt-ledger plus unadjudicated-symbol-collision — bookkeeping/engine-class, not axiom-class. **Do not draft an Ax 5 off this leaf.**
5. **No slot refilled (Rule 12).** `clm-ka5zdx`'s open strengthen-by ([`vol2/claim-quality.md`](../../claim-quality.md):1258) stays exactly as canon wrote it. No existing claim's solidity is flipped by this leaf.
6. **Sector-ownership held (`A1 ⊥ T2` cross-wiring watch).** Mass is booked on A1 dilatation; the $(2,3)$ winding is booked on the Cosserat T2 grade ([`master-equation.md`](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20). This leaf **does not cross-wire them**: it writes a budget with *both* grades' stores as named slots and proves an algebraic property of differences. Whether a T2 store belongs inside the A1-labelled invariant is precisely the question it declines to answer.

## §7 — What this leaf does NOT do

- It does **not** assert that $E_{\text{twist}} \neq 0$, that it is inside $m_ec^2$, or that it has any particular magnitude.
- It does **not** adopt Branch A or Branch B, and it does not rank them.
- It does **not** claim the ladder is wrong. Under Branch A the ladder's rung spacings are untouched; under Branch B **with** the weak-scale $\ell_c$ they are untouched too.
- It does **not** re-derive, strengthen, or extend `[branch:#833]`'s magnitude argument, and it does **not** headline that doc's recorded-and-disclaimed near-coincidence.
- It mints **no** experiment, **no** definition, **no** support node, and **no** second claim. §4.1's closed form and its cross-check are **arithmetic**, not claims.

## Cross-references

> → Primary: [Torus-Knot Uniqueness](torus-knot-uniqueness.md):102,:106-110 — the shared ground $(2,3)$ and the Cosserat-torsion excitation ladder this leaf's ledger books.
>
> → Primary: [The Three-Generation Lepton Spectrum](../ch06-electroweak-higgs/lepton-spectrum.md):17,:21,:39,:84 — the generation bookings, the *"nodes remain fixed at $l_{node}$"* Branch-A anchor, and canon's own Class-C tag on the lepton table.
>
> → Primary: [Mass-Closure Theorem](mass-closure-theorem.md):52,:54 — the $E_{\text{slosh}}$ term and the identity-class status of the closure the ledger extends.
>
> → Primary: [Electron Unknot ($0_1$)](electron-unknot.md):13,:19,:28,:59 — the tube geometry §4.1 integrates over, the $1/r$ law that is Branch B's strongest anchor, and the Axiom-1 pitch floor it collides with.
>
> ↗ See also: [Master Equation](../../../vol1/dynamics/ch4-continuum-electrodynamics/master-equation.md):20,:24,:41 — `A1 ⊥ T2`, the $(2,3)$'s mechanical-ω image on the couple-stress grade, and the exclusion-by-declaration this leaf's ledger writes as a slot rather than a zero.
>
> ↗ See also: [Proton Identification](../ch02-baryon-sector/proton-identification.md):23,:46 — the sector precedent for Compton-scaled real-space size, and the sub-node OPEN item a Branch-B muon would inherit.
>
> ↗ See also: [Scale Invariance across the Framework](../../../vol1/operators-and-regimes/ch5-universal-spatial-tension/scale-invariance.md):11,:18 — the universality claim for the $1/r$ law and the *"same unknot geometry"* Branch-A anchor, in one leaf, pulling opposite ways.
>
> ↗ See also: [Chirality and Antimatter](chirality-and-antimatter.md):10 — $\mathrm{Lk} = \mathrm{Tw} + \mathrm{Wr}$, the catch the paperclip cannot slip.
>
> ↗ See also: [Leaky-Cavity Particle Decay — theory](../../../vol4/simulation/ch14-leaky-cavity-particle-decay/theory.md):43 — *"the same real-space unknot topology and the same $(2,3)$ phase-space winding"*, the shared-ground premise stated for the muon.
>
> **Branch-pending (do not cite as canon until merged):** `research/2026-08-02_twist-ledger-audit.md` `[branch:#833]` — **unlinked on purpose**, the path does not resolve on `main`; link it at merge · [`common/electron-plumbing-primer.md`](../../../common/electron-plumbing-primer.md) **Step 3.5** `[branch:#832]` — the file resolves on `main`, the **section does not yet**, which is why it is cited by section name and not by line.
>
> **Cite discipline.** All file:line anchors in this leaf were verified **two-method** (`sed -n Np` on the worktree ⊕ `git show origin/main:<f> | sed -n Np`, byte-compared) at base `50da2eda`; the absence claims in §4.2 show their commands inline. The ledger of receipts is in this lane's docket fragment (`_orchestration/docket-entries/2026-08-02-common-mode-canonization.md`).

---

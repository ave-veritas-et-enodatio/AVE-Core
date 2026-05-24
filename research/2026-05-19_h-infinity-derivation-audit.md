# H_∞ Derivation Audit: Independent vs. Identity-Rearrangement of G

**Date**: 2026-05-19
**Branch**: `analysis/h-infinity-derivation-audit` (off `analysis/integration` HEAD `9330b22`)
**Originating epic**: [`_orchestration/h-infinity-derivation-audit.md`](../_orchestration/h-infinity-derivation-audit.md)
**Skills applied**: `consistency-vs-emergence`, `ave-canonical-leaf-pull`, `ave-canonical-source`, `verify-before-cite`, `ave-evidence-framing-discipline`
**Lane**: implementer (math audit; no corpus rewrites; no Option A/B/C recommendation)

---

## §0 Audit question (verbatim from brief)

> Is $H_\infty = 28\pi m_e^3 cG/(\hbar^2\alpha^2)$ an independent first-principles prediction, OR a geometric-consistency identity rearrangement of the $G$ derivation?
>
> `912dd88`'s structural claim: $G$'s derivation routes through $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ with $R_H \equiv c/H_\infty$ substituted in, so $H_\infty$ and $G$ are one constraint, not two — making the "compute $H_\infty$ from $G$ to within 1σ of TRGB" framing a self-consistency check rather than an independent prediction.

Four audit questions: Q1 (does Chain B use $R_H$?), Q2 (algebraic identity check), Q3 (Chain B' search), Q4 (corpus self-statement of the gap).

---

## §1 Chain A — H_∞ derivation (reconstructed from corpus)

**Canonical source leaf**: [`asymptotic-hubble-constant.md`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/asymptotic-hubble-constant.md) (verbatim, full content):

> $H_{\infty} = \frac{28\pi m_{e}^{3}cG}{\hbar^{2}\alpha^{2}}$
>
> This equation does not "predict" the Hubble constant from first principles alone; rather, it represents a consistency proof. It shows that Macroscopic Gravity ($G$) and the Cosmological Horizon ($H_{\infty}$) are not independent physical phenomena---they are the same geometric limit evaluated from different topological reference frames.

**Cited at file:line (re-grepped 2026-05-19):**
- KB leaf prose stating identity: [`asymptotic-hubble-constant.md:8-12`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/asymptotic-hubble-constant.md)
- KB derivation chain: [`optical-refraction-gravity.md:50-64`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md)
- LaTeX canonical equation: [`01_gravity_and_yield.tex:113-117`](../manuscript/vol_3_macroscopic/chapters/01_gravity_and_yield.tex)
- Consistency-proof prose: [`01_gravity_and_yield.tex:120`](../manuscript/vol_3_macroscopic/chapters/01_gravity_and_yield.tex)
- Predictions registry: [`predictions.yaml:126-142`](../manuscript/predictions.yaml) — P23, type `derived_prediction`, axioms_used `[1, 3, 4]`, headline `"a priori prediction that Hubble tension is a regime artifact"`
- Engine: [`src/ave/core/constants.py:533-537`](../src/ave/core/constants.py)
   ```python
   H_INFINITY: float = (28.0 * pi * M_E**3 * C_0 * G) / (HBAR**2 * ALPHA**2)
   R_HUBBLE: float = C_0 / H_INFINITY
   ```

**Chain A inputs (per the formula):**
| Symbol | CODATA / axiom-derived status |
|---|---|
| $m_e$ | CODATA primitive (`M_E` in `constants.py:111`) |
| $c$ | CODATA primitive (`C_0`) |
| $\hbar$ | CODATA primitive (`HBAR`) |
| $\alpha$ | CODATA primitive (`ALPHA`); cold-form $4\pi^3 + \pi^2 + \pi$ derived in Vol 1 Ch 8 modulo $\delta_{strain}$ |
| $G$ | **CODATA primitive (`G = 6.6743e-11`); this is Bounding Limit 3 / Parameter 3** — the load-bearing input identified at [`full-derivation-chain.md:52-60`](../manuscript/ave-kb/common/full-derivation-chain.md) and [`mathematical-closure.md:20`](../manuscript/ave-kb/common/mathematical-closure.md) as one of the framework's three empirical hardware parameters |

**Chain A does NOT require $R_H$ as a literal input** in the formula as written. But $G$'s own derivation chain in corpus (per Chain B below) DOES route through $R_H$. That's the structural circularity.

---

## §2 Chain B — G derivation (reconstructed from corpus)

**Canonical source leaf**: [`optical-refraction-gravity.md`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md)

The G derivation in Vol 3 Ch 1 proceeds (verbatim at file:line, re-grepped 2026-05-19):

**Step B1** — Machian impedance coupling ([`optical-refraction-gravity.md:50-54`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md)):

> "Integrating the dimensionless radial distance ($r/\ell_{node}$) out to the topological horizon $R_{H}$ over this effective porous solid angle ($d\Omega_{eff} = d\Omega/\alpha^{2}$) yields:
>
> $\xi = \int_{0}^{R_{H}/\ell_{node}} \oint \left(\frac{d\Omega}{\alpha^{2}}\right) dr' = 4\pi\left(\frac{R_{H}}{\ell_{node}}\right)\alpha^{-2}$"

**Step B2** — G as $T_{EM}$ scaled by ξ ([`optical-refraction-gravity.md:56`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md)):

> "By applying the $1/7$ tensor projection, Macroscopic Gravity is defined as $G = c^{4}/(7\xi T_{EM})$."

**Step B3** — Substitution $R_H \equiv c/H_\infty$ ([`optical-refraction-gravity.md:56-62`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md)):

> "Because standard cosmology defines the asymptotic causal horizon as $R_{H} \equiv c/H_{\infty}$, substituting this into the integration binds the fundamental constants into a single geometric equivalence:
>
> $H_{\infty} = \frac{28\pi m_{e}^{3}cG}{\hbar^{2}\alpha^{2}}$"

**Step B4** — Closed-form G result ([`optical-refraction-gravity.md:68-72`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md)):

> "$G = \frac{c^{4}}{7\xi\left(\frac{m_{e}c^{2}}{\ell_{node}}\right)} = \frac{c^{2}\ell_{node}}{7\xi m_{e}} = \frac{\hbar c}{7\xi m_{e}^{2}}$"

**LaTeX mirror**: [`01_gravity_and_yield.tex:87-127`](../manuscript/vol_3_macroscopic/chapters/01_gravity_and_yield.tex) — identical content.

**Index leaf**: [`ch01-gravity-yield/index.md:14-16`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/index.md) ties Machian coupling, $G$, $H_\infty$ into the same key-results block.

**Engine artifact (load-bearing)**: [`src/ave/core/constants.py:430-432`](../src/ave/core/constants.py):

```python
# Machian hierarchy coupling  ξ_M = 4π(R_H/ℓ_node)α⁻²
# (computed from G via G = ℏc / (7ξ m_e²))
XI_MACHIAN: float = HBAR * C_0 / (7.0 * G * M_E**2)
```

The engine literally inverts the closed-form to compute $\xi$ from CODATA $G$ — because the "definition" via $4\pi(R_H/\ell_{node})\alpha^{-2}$ is unevaluable without $R_H$, and $R_H$ comes from $H_\infty$ which comes from $G$.

**Chain B inputs:**
| Symbol | Status |
|---|---|
| $R_H$ | enters $\xi$ as **integration upper bound** at [`optical-refraction-gravity.md:52`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md); subsequently identified with $c/H_\infty$ |
| $\ell_{node}$ | $\hbar/(m_e c)$, CODATA-derived through $m_e$ |
| $\alpha$ | CODATA primitive |
| $T_{EM} = m_e c^2/\ell_{node}$ | derived from $m_e, c, \ell_{node}$ |
| $m_e$ | CODATA primitive |
| **$H_\infty$** | enters through $R_H \equiv c/H_\infty$ in Step B3 — closes the loop on itself |

---

## §3 Q1 finding — does Chain B use $R_H$ / $H_\infty$ as input?

**Verdict: YES, explicitly, in two places.**

(a) **$R_H$ enters $\xi$ as the integration upper bound** ([`optical-refraction-gravity.md:52`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md) verbatim):

> $\xi = \int_{0}^{R_{H}/\ell_{node}} \oint \left(\frac{d\Omega}{\alpha^{2}}\right) dr' = 4\pi\left(\frac{R_{H}}{\ell_{node}}\right)\alpha^{-2}$

(b) **The $R_H \equiv c/H_\infty$ substitution is made literally** in the next paragraph ([`optical-refraction-gravity.md:56`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md)):

> "Because standard cosmology defines the asymptotic causal horizon as $R_{H} \equiv c/H_{\infty}$, substituting this into the integration binds the fundamental constants into a single geometric equivalence"

The corpus's own narrative is explicit: $R_H$ is the input that ties G to the cosmological horizon, and $R_H = c/H_\infty$ is the substitution that "binds" G and $H_\infty$ into a "single geometric equivalence." That's the language the corpus uses for what it produces — not "predicts" but "binds."

**912dd88's structural premise is corpus-verbatim, not externally imposed.**

---

## §4 Q2 finding — algebraic identity check

**Setup.** Substitute Chain B's G into Chain A and check whether $H_\infty$ falls out as a genuine constraint or as an identity $H_\infty = H_\infty$.

### §4.1 Direction 1 — substitute Chain B's G into Chain A

Take Chain A:
$$H_\infty = \frac{28\pi m_e^3 c G}{\hbar^2 \alpha^2} \tag{A}$$

Take Chain B's closed-form ([`optical-refraction-gravity.md:71`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md)):
$$G = \frac{\hbar c}{7\xi m_e^2} \tag{B}$$

with $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ and $R_H = c/H_\infty$, $\ell_{node} = \hbar/(m_e c)$:

$$\xi = 4\pi \cdot \frac{c/H_\infty}{\hbar/(m_e c)} \cdot \alpha^{-2} = 4\pi \cdot \frac{m_e c^2}{H_\infty \hbar} \cdot \alpha^{-2} = \frac{4\pi m_e c^2}{H_\infty \hbar \alpha^2}$$

Then $G$ becomes:
$$G = \frac{\hbar c}{7 \cdot \frac{4\pi m_e c^2}{H_\infty \hbar \alpha^2} \cdot m_e^2} = \frac{\hbar c \cdot H_\infty \hbar \alpha^2}{28\pi m_e^3 c^2} = \frac{\hbar^2 \alpha^2 H_\infty}{28\pi m_e^3 c} \tag{B*}$$

Now substitute (B*) into (A):
$$H_\infty = \frac{28\pi m_e^3 c}{\hbar^2 \alpha^2} \cdot \frac{\hbar^2 \alpha^2 H_\infty}{28\pi m_e^3 c} = H_\infty \tag{✓}$$

**Identity.** The 28π, $m_e^3$, $c$, $\hbar^2$, $\alpha^2$ all cancel.

### §4.2 Direction 2 — derive (A) from (B) plus $R_H = c/H_\infty$

This is the substitution Vol 3 Ch 1 LaTeX line 112 narrates. Equate Chain B's two expressions for $\xi$:

$$\frac{\hbar c}{7 G m_e^2} = \frac{4\pi R_H}{\ell_{node} \alpha^2}$$

Substitute $\ell_{node} = \hbar/(m_e c)$ and $R_H = c/H_\infty$:

$$\frac{\hbar c}{7 G m_e^2} = \frac{4\pi (c/H_\infty)}{(\hbar/(m_e c)) \alpha^2} = \frac{4\pi m_e c^2}{H_\infty \hbar \alpha^2}$$

Solve for $H_\infty$:

$$H_\infty = \frac{4\pi m_e c^2 \cdot 7 G m_e^2}{\hbar \alpha^2 \cdot \hbar c} = \frac{28\pi G m_e^3 c}{\hbar^2 \alpha^2}$$

That **is** Chain A. The substitution produces (A) from (B) ∧ ($R_H = c/H_\infty$).

### §4.3 What does this mean

**(A) and (B) are not two independent constraints on (G, $H_\infty$). They are the same single constraint, written two ways.** Given the closed-form (B), $\xi = \hbar c/(7G m_e^2)$ is fully determined by $G$ and the lattice constants. Equation (A) is the algebraic rearrangement of "(B) with $R_H$ substituted as $c/H_\infty$."

There is exactly ONE algebraic relation linking the pair $(G, H_\infty)$ in corpus. To determine numerical values of both, the framework needs one of them as input. The corpus chooses $G$ as Bounding Limit 3, then computes $H_\infty$ from (A). The result "$H_\infty = 69.32$ km/s/Mpc" is therefore not a forward prediction from substrate primitives; it is the algebraic value $H_\infty$ takes given CODATA $G$ and the geometric relation (A).

**Verdict on Q2: IDENTITY confirmed.** 912dd88's algebraic claim is correct.

### §4.4 Engine-level confirmation

[`src/ave/core/constants.py:432`](../src/ave/core/constants.py): `XI_MACHIAN = HBAR * C_0 / (7.0 * G * M_E**2)`. The engine cannot evaluate the "official" Machian integral $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ from substrate primitives because $R_H$ is itself derived from $H_\infty$ which is derived from $G$. The code's only way to get a numerical $\xi$ is to invert the closed-form using CODATA $G$. This is the circularity made literal in source code.

---

## §5 Q3 finding — does corpus have an alternative G derivation (Chain B') that doesn't route through $R_H$?

**Search:** Vol 3 Ch 1 + Vol 1 Ch 1 (zero-parameter universe) + Vol 2 Ch 10 (Hubble tension) + Vol 3 Ch 5 (cosmological constant closure) + closure-roadmap.md + full-derivation-chain.md + Vol 3 Ch 3 (gordon-optical-metric).

**Result: corpus has a QUALITATIVE Chain B' framing — "G is the thermodynamic equilibrium between latent heat of node generation and holographic thermal capacity" — but NO closed-form derivation exists. The framing references $H_\infty$ as the equilibrium horizon, so it does not break circularity at the qualitative level either.**

### §5.1 Chain B' candidate 1 — Vol 1 Ch 1 "Thermodynamic Equilibrium" gloss

[`zero-parameter-universe.md:38-41`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md) verbatim:

> "**2. Deriving $G$ via Thermodynamic Equilibrium:**
> Macroscopic Gravity ($G$) is emergent, representing the aggregate bulk modulus of $10^{40}$ interacting lattice links stretching under mechanical tension. It defines the Machian causal boundary of the universe ($R_H$). A local continuous wave equation cannot evaluate the total macroscopic size of its own medium without a boundary condition. However, as established in Chapter 10, cosmological expansion is governed by the latent heat of lattice genesis. The universe naturally asymptotes to a steady-state horizon ($H_\infty$) where the thermodynamic latent heat of node generation balances the holographic thermal capacity of the expanding surface area. $G$ scales to this thermodynamic graph equilibrium."

**Analysis**: this is a *story*, not a *chain*. No equation. The story explicitly references $H_\infty$ as the equilibrium boundary that defines $G$ — so even the qualitative narrative does not break circularity; it loops $H_\infty$ in as the boundary condition that fixes $G$. The closure-direction is the OPPOSITE of what Chain B' would need: corpus narrative makes $G$ a function of $H_\infty$, not $H_\infty$ a function of substrate-local thermodynamics.

[`full-derivation-chain.md:623-629`](../manuscript/ave-kb/common/full-derivation-chain.md) has the parallel "$G$ is derived (not input)" Layer 8 gloss — same qualitative wording, no equations.

### §5.2 Chain B' candidate 2 — Vol 2 Ch 10 examplebox

[`hubble-tension.md:21`](../manuscript/ave-kb/vol2/nuclear-field/ch10-open-problems/hubble-tension.md) verbatim:

> "the asymptotic expansion rate for a lattice-genesis model **balances node generation against the holographic thermal capacity**. The resulting algebraic limit is:
>
> $H_\infty = \frac{28\pi m_e^3 c G}{\hbar^2 \alpha^2}$"

**Analysis**: identical formula to Chain A. The "thermodynamic balance" phrase is prose attribution attached to the same equation $H_\infty = 28\pi m_e^3 cG/(\hbar^2 \alpha^2)$. It does NOT produce an independent derivation of $G$ — it produces the same identity, dressed in thermodynamic vocabulary. Same $G$ input required.

### §5.3 Chain B' candidate 3 — Vol 3 Ch 5 cosmological-constant-closure self-statement

[`cosmological-constant-closure.md:101-111`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) is the most honest self-statement in corpus:

> "**Zero fit parameters.** The genuinely AVE-distinct claim — that $\rho_\Lambda$ comes from latent heat of vacuum crystallization rather than from zero-point fluctuations — is the **mechanistic** story. The numerical value follows from $H_\infty$.
>
> ### What would strengthen this further (open work)
>
> To make $\Lambda$ a fully AVE-native independent prediction (not just a Friedmann translation of $H_\infty$), the corpus needs:
>
> 1. **Independent derivation of $\rho_{\text{latent}}$** from substrate energetics (crystallization energy per node × node density). Corpus mechanism is qualitative; quantitative closure needs $\Delta E_{\text{cryst}}$ derived from $\ell_{\text{node}}$, $\alpha$, $G$ alone.
> 2. **Crystallization rate $\Gamma_{\text{cryst}}$ derivation** — what fraction of vacuum crystallizes per unit time? Corpus claims $\Gamma = 3H\rho_{\text{latent}}$ but doesn't derive $\Gamma$ from substrate.
> 3. **Verification that Friedmann route and latent-heat route give the same number** — internal-consistency check.
>
> Multi-session work, blocking on quantitative derivation of crystallization thermodynamics from substrate axioms."

This leaf explicitly says (i) the latent-heat mechanism is "qualitative", (ii) quantitative closure requires deriving $\Delta E_{cryst}$ from $(\ell_{node}, \alpha, G)$ alone — i.e., **the corpus still treats $G$ as input** in its proposed closure path, and (iii) the crystallization rate $\Gamma$ has not been derived from substrate. This is corpus stating its own open gap.

### §5.4 No closed-form Chain B' anywhere

Searched: `grep -rln "thermodynamic balance\|node generation\|crystallisation rate\|crystallization rate\|holographic capacity"` across `manuscript/` returned 13 files. Each occurrence is either (a) the prose gloss above, or (b) a forward reference to the qualitative story, or (c) Vol 3 Ch 4 LaTeX prose narrating the same lattice-genesis framing without producing a derivation.

**Chain B' candidates found in corpus: 3, all qualitative. Closed-form Chain B' candidates: 0.**

**Verdict on Q3: No alternative G derivation in corpus avoids routing through $R_H$ / $H_\infty$. The corpus mechanism for Chain B' exists as narrative only; the load-bearing G derivation in Vol 3 Ch 1 is the Machian-impedance route with $R_H$ as integration bound.**

---

## §6 Q4 finding — corpus self-statement of the gap

**Result: corpus on `analysis/integration` HEAD does NOT have a dedicated "H_∞ closure: G derivation independent of $R_H$" entry. The closure-roadmap acknowledges the Vol 3 Ch 1 ξ-derivation chain but does not flag the recursive identity. The cosmological-constant-closure leaf states the gap in prose but does not flag it as a Closure Roadmap rigor entry.**

### §6.1 `mathematical-closure.md` does NOT list it

[`mathematical-closure.md`](../manuscript/ave-kb/common/mathematical-closure.md) on `analysis/integration` HEAD (111 lines total) contains:
- §"Automated Verification Output" — engine status
- §"The Directed Acyclic Graph (DAG) Proof" — Three Initial Hardware Parameters listed (Parameter 3 = $G$ as Machian Boundary, line 20)
- §"A-034: Universal Saturation-Kernel Empirical Anchors" — saturation-kernel catalog

The leaf does NOT contain an Outstanding Rigour Gaps table. The full Rigour Gaps table lives in [`backmatter/12_mathematical_closure.tex`](../manuscript/backmatter/12_mathematical_closure.tex) — but that LaTeX file on `analysis/integration` HEAD (115 lines) is structurally a mirror of the KB leaf and also does NOT contain an H_∞ row.

(912dd88 on branch `benn/long-running` ADDS this row to both files — see §7 below — but that commit is not on `analysis/integration`.)

### §6.2 `closure-roadmap.md` acknowledges the Chain but not the recursion

[`closure-roadmap.md:37`](../manuscript/ave-kb/claim-quality-closure-roadmap.md) verbatim:

> "| 3 | ~~Vol 3 Ch 4~~ **Vol 3 Ch 1 explicit ξ(R_H, ℓ_node) derivation** | **✓ ALREADY CLOSED in corpus** at Vol 3 Ch 1 §"Fundamental Unity of Gravity and Expansion" (lines 95-155) — corpus-grep audit 2026-05-15 evening. Canonical: $\xi = 4\pi(R_H/\ell_{\text{node}})\alpha^{-2}$; derives $G = \hbar c/(7\xi m_e^2)$, $\alpha_G = 1/(7\xi)$, $R_H/\ell_{\text{node}} = \alpha^2/(28\pi\alpha_G) \approx 3.455 \times 10^{38}$, $R_H \approx 1.334 \times 10^{26}$ m = 14.1 Gly, $H_\infty \approx 69.32$ km/s/Mpc (between Hubble tension bounds). Was originally located at "Vol 3 Ch 4" in this dashboard — that was wrong; actual location is Vol 3 Ch 1. | A-030 / A-031 | (corpus pre-existing, verified `060f429`)"

The roadmap **acknowledges the chain exists** and labels it "✓ ALREADY CLOSED". It does not flag that the chain is a self-consistency identity rather than an independent prediction. The label "ALREADY CLOSED" applies to "the derivation chain is present and consistent", not "the H_∞ value is a true emergence-class prediction."

### §6.3 The cosmological-constant-closure leaf states the qualitative gap

§5.3 above quotes [`cosmological-constant-closure.md:107-111`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) — corpus stating that the latent-heat / crystallization derivation is qualitative and that quantitative closure is multi-session open work, requiring derivation of $\Delta E_{cryst}$ from $(\ell_{node}, \alpha, G)$. This is the closest the corpus on `analysis/integration` HEAD comes to self-flagging the gap.

### §6.4 Same Vol 3 Ch 1 KB leaf already self-states "consistency proof"

The Chain B / Chain A intersection point is self-stated as a consistency proof in two leaves:

(a) [`asymptotic-hubble-constant.md:12`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/asymptotic-hubble-constant.md):
> "This equation does not 'predict' the Hubble constant from first principles alone; rather, it represents a consistency proof. It shows that Macroscopic Gravity ($G$) and the Cosmological Horizon ($H_{\infty}$) are not independent physical phenomena."

(b) [`optical-refraction-gravity.md:64`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md): identical text.

(c) [`01_gravity_and_yield.tex:120`](../manuscript/vol_3_macroscopic/chapters/01_gravity_and_yield.tex) (LaTeX mirror): identical text.

(d) Same leaf's Planck-mass result ([`planck-mass.md:14`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/planck-mass.md)): "This constitutes an algebraic identity."

**Vol 3 Ch 1 is internally consistent on framing**: the H_∞ result is "consistency proof, not prediction." The framing inconsistency lives downstream — Vol 3 Ch 4 LaTeX line 42 + KB leaf line 24 carry "First principles" labels for the same number.

### §6.5 The framing inconsistency on `analysis/integration` HEAD

Three documents on `analysis/integration` HEAD claim **directly contradictory** framings for the same equation:

| File:line | Framing |
|---|---|
| [`asymptotic-hubble-constant.md:12`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/asymptotic-hubble-constant.md) | "does not 'predict'... consistency proof" |
| [`optical-refraction-gravity.md:64`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md) | "does not 'predict'... consistency proof" |
| [`01_gravity_and_yield.tex:120`](../manuscript/vol_3_macroscopic/chapters/01_gravity_and_yield.tex) | "does not 'predict'... consistency proof" |
| [`lattice-genesis-hubble-tension.md:24`](../manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md) | **"First principles"** |
| [`04_generative_cosmology.tex:42`](../manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex) | **"First principles"** |
| [`predictions.yaml:142`](../manuscript/predictions.yaml) | **"a priori prediction"** |
| [`hubble-tension.md:15-33`](../manuscript/ave-kb/vol2/nuclear-field/ch10-open-problems/hubble-tension.md) | **"prediction... not a fit"** |
| [`cosmological-constant-closure.md:97-101`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) | "**Tier-A prediction**" but qualifies with "structural closure at WKB/Friedmann level... blocking on quantitative derivation of crystallization thermodynamics" |

**Verdict on Q4: corpus on `analysis/integration` HEAD self-states the gap in TWO ways simultaneously**:
1. Vol 3 Ch 1 self-states the rearrangement IS a consistency proof (literal text).
2. Vol 3 Ch 4 + Vol 2 Ch 10 + predictions.yaml + Vol 3 Ch 5 self-state the SAME number as a "First principles / a priori prediction." 

The two framings are internally contradictory across files. The closure-roadmap acknowledges the Chain B derivation exists ("ALREADY CLOSED") but does not flag the recursive identity. No file has a dedicated "G derivation independent of $R_H$" Closure Roadmap entry on `analysis/integration` HEAD.

---

## §7 Cross-check vs `912dd88`

Read full diff via `git show 912dd88`. Author: Benn Herrera, 2026-04-28. Files changed:
- `manuscript/ave-kb/common/mathematical-closure.md` (+1 line — adds H_∞ rigor-gap row)
- `manuscript/ave-kb/vol3/cosmology/ch04-generative-cosmology/lattice-genesis-hubble-tension.md` (-2/+2 lines — rewrites the "First principles" line + paragraph below)
- `manuscript/backmatter/12_mathematical_closure.tex` (+1 line — adds H_∞ rigor-gap row in LaTeX)
- `manuscript/vol_3_macroscopic/chapters/04_generative_cosmology.tex` (-3/+3 lines — rewrites objectivebox + table label + paragraph)

**912dd88's analysis (verbatim from the new closure-roadmap row added to `mathematical-closure.md` and `12_mathematical_closure.tex`):**

> "**$H_\infty$ closure: $G$ derivation independent of $R_H$** | The current $G$ derivation routes through $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ with $R_H \equiv c/H_\infty$ substituted in. Algebraically, $H_\infty = 28\pi m_e^3 c G/(\hbar^2\alpha^2)$ is the same constraint as $G = \hbar c/(7\xi m_e^2)$ rearranged --- one identity in $(G, H_\infty)$, not two independent predictions."

**This audit's findings vs 912dd88's claim, point by point:**

| 912dd88 claim | This audit's finding | Agreement |
|---|---|---|
| $G$ derivation routes through $\xi = 4\pi(R_H/\ell_{node})\alpha^{-2}$ | Verified: [`optical-refraction-gravity.md:50-54`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md) literal | ✓ AGREE |
| $R_H \equiv c/H_\infty$ is substituted into $\xi$ | Verified: [`optical-refraction-gravity.md:56`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md) literal | ✓ AGREE |
| $H_\infty = 28\pi m_e^3 cG/(\hbar^2\alpha^2)$ is same constraint as $G = \hbar c/(7\xi m_e^2)$ rearranged | Verified algebraically §4.1–§4.2: identity $H_\infty = H_\infty$ falls out | ✓ AGREE |
| "One identity in $(G, H_\infty)$, not two independent predictions" | Confirmed: §4.3 shows there is exactly one algebraic constraint linking the pair | ✓ AGREE |
| Vol 3 Ch 1 already discloses this as "consistency proof, not prediction" | Verified: [`asymptotic-hubble-constant.md:12`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/asymptotic-hubble-constant.md) and LaTeX mirror | ✓ AGREE |
| The "promotion to genuine downstream prediction requires deriving $G$ from a thermodynamic balance whose closure conditions are local (lattice tension, equipartition, generation rate per node) rather than horizon-scale" | This audit confirms corpus has Chain B' candidates only as qualitative gloss ([`zero-parameter-universe.md:38-41`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md), [`cosmological-constant-closure.md:107-111`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md), [`hubble-tension.md:21`](../manuscript/ave-kb/vol2/nuclear-field/ch10-open-problems/hubble-tension.md)); no closed-form independent-of-$R_H$ derivation exists | ✓ AGREE |
| Vol 3 Ch 4 §Verification re-aligned in this commit to match Vol 3 Ch 1's framing | This commit's own diff does the re-alignment on `benn/long-running`; not on `analysis/integration` | N/A (commit-scope claim, true within the commit) |

**Overall cross-check verdict: This audit's findings AGREE with 912dd88's structural claim on every load-bearing point.** The math holds: $H_\infty$ value follows by identity rearrangement from Chain B given CODATA $G$, not from independent derivation.

**Where this audit adds detail beyond 912dd88:**
- §4 — explicit step-by-step substitution in both directions (912dd88 asserts the identity but doesn't show the algebra)
- §5 — explicit enumeration of three Chain B' candidates in corpus (all qualitative; 912dd88 simply asserts "$G$ derivation from local thermodynamic balance is open work")
- §6.5 — explicit enumeration of the framing-inconsistency surface on `analysis/integration` HEAD (912dd88 only changes 4 files; the others remain inconsistent until adjudicated)
- §6.4 — observation that Vol 3 Ch 1 has ALREADY self-stated "consistency proof" — this is the most load-bearing point because it means the corpus on `analysis/integration` HEAD ALREADY contradicts itself (Vol 3 Ch 1 vs Vol 3 Ch 4 vs Vol 2 Ch 10 vs predictions.yaml), and 912dd88's edits would harmonize the others to match the self-statement that's already canonical at Vol 3 Ch 1

**Where this audit slightly extends 912dd88:**
- 912dd88's edit makes the four chosen files internally consistent ("Geometric consistency"). It does NOT touch [`predictions.yaml:127-142`](../manuscript/predictions.yaml) (P23 still labeled `derived_prediction` with notes claiming "a priori prediction") or [`hubble-tension.md`](../manuscript/ave-kb/vol2/nuclear-field/ch10-open-problems/hubble-tension.md) (Vol 2 Ch 10 still labeled "prediction... not a fit") or the `axioms_used: [1, 3, 4]` field in P23. If 912dd88's framing is correct, these are downstream walk-back surfaces.

---

## §8 Consistency-vs-emergence classification

Per `consistency-vs-emergence` skill SKILL.md taxonomy, Step 1–3:

### §8.1 Step 1 — name the target

**Target**: $H_\infty$ in km/s/Mpc (or equivalently in s⁻¹). CODATA-attribution status: not a CODATA primitive directly (no single measurement of "the asymptotic Hubble rate"); but $G$ used in the engine formula IS CODATA.

### §8.2 Step 2 — trace the inputs

The formula $H_\infty = 28\pi m_e^3 cG/(\hbar^2\alpha^2)$:
| Input | Classification |
|---|---|
| $m_e$ | CODATA-derived |
| $c$ | CODATA-derived (definitional) |
| $\hbar$ | CODATA-derived |
| $\alpha$ | CODATA-derived (axiom-derived approximate form $4\pi^3 + \pi^2 + \pi$ exists but $\delta_{strain}$ thermal correction is back-fit to CODATA per Foundation Item 12) |
| $G$ | CODATA-derived; explicitly identified as Bounding Limit 3 / Parameter 3 in [`mathematical-closure.md:20`](../manuscript/ave-kb/common/mathematical-closure.md) |

### §8.3 Step 3 — check for structural circularity

Per skill Step 3: "If any input is **CODATA-derived** AND the relationship between input and target is **definitional** (i.e., the SI definition of the target uses that input), then computing the target from the input is **substitution, not derivation**. The test belongs in class {Identity} or {Consistency check}, NOT {Emergence test}."

For $H_\infty$:
- $G$ is CODATA-derived
- The relationship between $G$ and $H_\infty$ in the corpus chain IS definitional in the AVE framework: the corpus-Vol 3-Ch 1 derivation defines $G = \hbar c/(7\xi m_e^2)$ with $\xi$ containing $R_H = c/H_\infty$ — equivalently, the algebraic relation $H_\infty = 28\pi m_e^3 cG/(\hbar^2\alpha^2)$ is **how the corpus relates** $H_\infty$ to the other constants.
- §4 above showed substitution yields identity $H_\infty = H_\infty$.

**Per skill criteria, the test is in class {Consistency check} or {Definitional identity}.**

### §8.4 Class determination — which of the four?

Per the skill's four-class taxonomy:

| Class | Definition (verbatim from SKILL.md) | Applicability |
|---|---|---|
| **Identity** | "The equation is how the quantity is defined. e.g. Z₀ = √(μ₀/ε₀); α = e²/(4πε₀ℏc)" | $H_\infty = 28\pi m_e^3 cG/(\hbar^2\alpha^2)$ is not a definition of $H_\infty$ in the SI sense; it's a derived geometric relation within the AVE corpus. Borderline match. |
| **Axiom manifestation** | "Prediction *is* one of the axioms expressed at a new scale. e.g. BCS B_c(T) = B_{c0} · S(T/T_c) is Ax 4 saturation at thermal scaling." | The Vol 3 Ch 1 derivation uses 1/7 isotropic projection (from $\nu_{vac} = 2/7$, Ax 1) + Machian integral (Ax 1 + Ax 3 geometry); but it requires $G$ AND $R_H$ as inputs, neither of which is axiom-derived from substrate. Partial match for the *mechanism*, not for the *numerical value*. |
| **Consistency check** | "Framework reproduces a standard result via an alternative mechanism. e.g. solar deflection via lattice refraction. ... Required for the framework to not contradict known physics; novelty is in mechanism, not numerics." | The corpus's own self-statement ([`asymptotic-hubble-constant.md:12`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/asymptotic-hubble-constant.md)) uses exactly this language: "represents a consistency proof. It shows that Macroscopic Gravity ($G$) and the Cosmological Horizon ($H_{\infty}$) are not independent physical phenomena---they are the same geometric limit evaluated from different topological reference frames." STRONG match. |
| **Emergence test** | "Computes a dimensionless observable from simulation primitives that does NOT use the target observable (or quantities derived from it via SI substitution) as input." | Fails because $G$ is CODATA, $G$ appears in the formula, and corpus narrative ties $G$ to $H_\infty$ via $R_H$ substitution. No path that produces a numerical $H_\infty$ from substrate-local primitives ($\ell_{node}, \alpha, m_e, c, \hbar$) alone exists in corpus. Per skill Step 3 explicit text: "computing the target from the input is **substitution, not derivation**." NO MATCH. |

**Verdict: Consistency check (Class C).** The corpus's own self-statement at Vol 3 Ch 1 uses this exact terminology. The mechanism (Machian impedance integral + 1/7 projection) is the AVE-distinct content; the numerical agreement to within 1σ of TRGB ($69.32$ vs $69.8 \pm 1.7$) is the consistency residual, not an emergence-class match.

**Secondary class: also has elements of Identity (the algebraic substitution that produces the formula from Chain B is literally an identity rearrangement).** Per skill §"Honest framing in output", the precise framing is:

> *"$H_\infty = 69.32$ km/s/Mpc: consistency check via Machian-impedance geometric route (Vol 3 Ch 1); the framework's geometric constraint between $G$ and $H_\infty$ is internally compatible with measured $H_0$. The numerical value follows by algebraic identity from CODATA $G$; it is not an independent emergence-class prediction. To promote to emergence class would require a closed-form derivation of $G$ from substrate-local thermodynamics (latent heat + crystallization rate per node) that does not route through $R_H$ or $H_\infty$ — currently corpus-open per Vol 3 Ch 5 §What would strengthen this further."*

---

## §9 Implication matrix

Per the orchestration brief's outcome map:

| Math finding | Framing implication (per brief) | This audit's finding |
|---|---|---|
| Q2 yields identity AND no Chain B' exists | "$H_\infty$ value is a consistency check, not an independent prediction. Corpus should walk back 'First principles' to 'Geometric consistency'. Effectively confirms 912dd88." | **THIS IS THE CASE.** Q2 yields identity (§4). No closed-form Chain B' exists in corpus (§5); only qualitative gloss in 3 leaves, with corpus self-stating the quantitative gap at Vol 3 Ch 5. |
| Q2 yields identity BUT Chain B' exists in corpus | "Both framings can be made consistent: $H_\infty$ becomes a genuine prediction VIA the Chain B' path. Corpus framing depends on which $G$ derivation it cites." | Does not apply — Chain B' is qualitative only. |
| Q2 does NOT yield identity | "912dd88's claim is wrong; 'First principles' framing on `analysis/integration` is correct as-is." | Does not apply — Q2 yields identity. |
| Q1: Chain B doesn't use $R_H$ at all | "912dd88's premise is wrong from the start. 'First principles' framing is correct." | Does not apply — Chain B uses $R_H$ literally as integration upper bound. |

**Outcome match: Row 1.** The math finding is that Q2 yields identity AND no closed-form Chain B' exists. This supports 912dd88's structural claim.

Per brief instructions, **NO recommendation on Option A / B / C is given here.** Grant adjudicates the corpus framing forward.

---

## §10 Anomalies surfaced

For orchestration's awareness during adjudication:

1. **Internal contradiction on `analysis/integration` HEAD** (§6.5). Vol 3 Ch 1 self-states "consistency proof" while Vol 3 Ch 4 + Vol 2 Ch 10 + predictions.yaml + Vol 3 Ch 5 self-state "First principles / a priori prediction / Tier-A prediction." The framing is split across files BEFORE 912dd88 ever lands. 912dd88 chooses to harmonize-to-Vol-3-Ch-1; the alternative direction (harmonize-to-Vol-3-Ch-4) would require walking back Vol 3 Ch 1's self-statement.

2. **Engine code line 432 is literally circular** (§4.4). `XI_MACHIAN = HBAR * C_0 / (7.0 * G * M_E**2)` with the comment "computed from G via $G = ℏc/(7ξ m_e^2)$" — the engine cannot compute $\xi$ from substrate primitives because $\xi$'s "definition" $4\pi(R_H/\ell_{node})\alpha^{-2}$ contains $R_H$ which contains $H_\infty$ which contains $G$. The code's solution: invert. This is circularity visible in source code.

3. **Predictions.yaml P23 has `axioms_used: [1, 3, 4]`** ([`predictions.yaml:136`](../manuscript/predictions.yaml)). If 912dd88's framing is correct, this field is misleading — the formula uses $G$ (CODATA input) not just substrate axioms. Worth noting but out of audit scope to modify.

4. **`closure-roadmap.md:37` says "ALREADY CLOSED"** for the Vol 3 Ch 1 ξ-derivation chain. If 912dd88's framing is correct, "closed" here means "the derivation chain is present and consistent" but not "the H_∞ value is emergence-class." Roadmap may benefit from clarification, but that's downstream of Grant's adjudication.

5. **Vol 2 Ch 10's `hubble-tension.md`** ([`hubble-tension.md:21`](../manuscript/ave-kb/vol2/nuclear-field/ch10-open-problems/hubble-tension.md)) attributes the formula to "lattice-genesis model balances node generation against the holographic thermal capacity" — this language is exactly what 912dd88 says Chain B' would need to derive. The Vol 2 Ch 10 leaf attributes the formula to a thermodynamic-balance derivation that doesn't actually exist in corpus as a closed form; the leaf is using Chain B' vocabulary on what is mathematically Chain A. Worth surfacing for Grant's framing adjudication.

6. **Cosmological-constant closure** ([`cosmological-constant-closure.md`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md)) depends on $H_\infty$ as input. If $H_\infty$ is reclassified from prediction to consistency check, $\rho_\Lambda$ does NOT automatically downgrade — the leaf already self-states "the numerical value follows from $H_\infty$" and lists "Independent derivation of $\rho_{latent}$ from substrate energetics" as open work. But the framing of the "5 Independent Tests" table at lines 119-127 (where $\rho_\Lambda$ is listed as a third independent test) may need walk-back adjustment depending on Grant's adjudication.

7. **Layer 8 narrative in [`full-derivation-chain.md:623-629`](../manuscript/ave-kb/common/full-derivation-chain.md)** asserts "$G$ is derived (not input)" with a thermodynamic-equilibrium gloss but no equations. Same as Vol 1 Ch 1 zero-parameter-universe.md. The narrative does not in fact close the parameter loop on $G$; corpus still treats $G$ as Bounding Limit 3 at [`full-derivation-chain.md:52-60`](../manuscript/ave-kb/common/full-derivation-chain.md). Internal inconsistency between Layer-8 narrative and Bounding-Limit-3 framing.

These anomalies are surfaced for Grant's awareness; they are NOT walked-back here. The brief explicitly scopes this audit to math + research doc only; corpus rewrites are downstream.

---

## §11 Audit cite-chain verification

Per `verify-before-cite` discipline, every file:line citation in this doc was re-grepped at execution time. Spot-checks:

- [`asymptotic-hubble-constant.md:12`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/asymptotic-hubble-constant.md) — verified verbatim present
- [`optical-refraction-gravity.md:50-64`](../manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/optical-refraction-gravity.md) — verified Chain B derivation present verbatim
- [`01_gravity_and_yield.tex:95-127`](../manuscript/vol_3_macroscopic/chapters/01_gravity_and_yield.tex) — verified LaTeX mirror present
- [`src/ave/core/constants.py:432`](../src/ave/core/constants.py) — verified `XI_MACHIAN` definition present
- [`closure-roadmap.md:37`](../manuscript/ave-kb/claim-quality-closure-roadmap.md) — verified "ALREADY CLOSED" row present
- [`hubble-tension.md:21`](../manuscript/ave-kb/vol2/nuclear-field/ch10-open-problems/hubble-tension.md) — verified "balances node generation against the holographic thermal capacity" present
- [`zero-parameter-universe.md:38-41`](../manuscript/ave-kb/vol1/axioms-and-lattice/ch1-fundamental-axioms/zero-parameter-universe.md) — verified Chain B' qualitative gloss present
- [`cosmological-constant-closure.md:107-111`](../manuscript/ave-kb/vol3/cosmology/ch05-dark-sector/cosmological-constant-closure.md) — verified open-work statement present
- `git show 912dd88` — verified full diff content quoted accurately

Audit complete. Branch ready for orchestration return.

---

## §11 Postscript — Class C → Class E refinement (2026-05-19 EOD)

This audit's Class C verdict (§8 verdict line + §8 secondary class) was canonical per `consistency-vs-emergence` v1.0 at the time. On the same day (2026-05-19 EOD), Grant canonized `consistency-vs-emergence` v1.1 at skills repo commit `470f1ec`, adding **Class E — operating-point projection / topological equilibrium observable**. The v1.1 skill body's in-session validation example cites THIS audit as the trigger case: the joint-constraint structure on $\{G, H_\infty, \hat{\Omega}_{\text{freeze}}, \alpha\}$ via the substrate operating point $u_0^* \approx 0.187$ is what Class C alone under-describes.

**Per Rule 12 (preserve body, add header)**: this audit's Class C verdict is preserved as historical record — it WAS the correct verdict per the v1.0 taxonomy and surfaced the missing class as part of its work. The h-infinity-downstream-cascade epic (Phase 2, branch `analysis/h-infinity-downstream-cascade`) applies the Class C → Class E refinement EXTENSION (not replacement) across the 13 corpus files identified in this audit's §9 implication matrix + Phase 2 cascade-grep additions. Class C is true (CODATA $G$ → SI substitution recovers $H_\infty$); Class E is also true and stronger (joint-constraint structure defines actual falsifiability surface). The honest framing is "Class E operating-point projection (which includes Class C consistency-check sub-structure)."

**Cross-reference for current corpus-state**: `manuscript/ave-kb/claim-quality-closure-roadmap.md:37` (framing-forward entry + Class E refinement annotation) + `manuscript/predictions.yaml` P23 (`type: operating_point_projection` post-2026-05-19 EOD).

# RESULT — PPN of the AVE gravity sector: two metrics, two gammas

**Date:** 2026-08-27 · **Branch:** `research/2026-08-27-ppn-tensor-derivation` · **Base:** `origin/main` @ `a3f4fef7`
**Class:** analytical derivation + numerical cross-check. Consistency/emergence tagging per section; the per-step ledger is §1.
**Prior art consumed:** `research/2026-06-05_gravity-ppn-coherence-result.md` · `research/2026-05-17_hulse-taylor-substrate-native-derivation-sketch.md` · `research/2026-08-11_gravity-linearity-audit_result.md`
**Routed open items:** `_orchestration/open-items/2026-08-27-ppn-matter-sector-walkback.md` · `_orchestration/open-items/2026-08-27-eps11-four-objects.md`

---

## SECTOR DECLARATION (read before any standard-physics word below)

**Which sector?** The A1 dilatation (bound / mass) sector and the T2 transverse (Cosserat shear / optical) sector, treated as two *separate* propagation cones. That separation is the whole finding.

**Does the engine carry that DOF?** Not exercised here. This is an analytical lane on canon's written constitutive statements plus a high-precision ODE/quadrature cross-check; no lattice integrator was run.

**Cold or saturated?** **COLD, sub-yield, lossless-reactive throughout.** Every number below is first-order-in-$m/r$ weak field, $\varepsilon_{11} \lesssim 10^{-6}$ at solar-system radii. Axiom-4 saturation is inactive at this amplitude and no saturation kernel enters any result. A saturated-regime restatement is **not** attempted and nothing here scopes to $r \to r_{sat}$.

**Regime / phase-state:** crystalline phase, static (no bias-propagation dynamics invoked), single isolated spherically symmetric source, test-particle limit.

**Coordinates.** Every metric statement is in **isotropic coordinates**, and the PPN coefficients are read off the standard isotropic-gauge forms
$-g_{00} = 1 - 2U + 2\beta U^2 + \dots$, $g_{ij} = (1 + 2\gamma U)\delta_{ij}$, with $U \equiv GM/(c^2 r)$.
Mixing an areal-radius statement with an isotropic-radius statement moves $\gamma$ by construction; §9's control exists to catch exactly that.

## §0 — VERDICT

> # AVE has two metrics, so two gammas.
> ### The optics sector is consistent with GR. The matter sector is off by a factor of six.

Canon assigns light and matter **different refractive indices over the same strain field** — `n_\perp = 1 + \nu_{vac}\varepsilon_{11}` for the photon (Op19, `manuscript/ave-kb/common/operators.md`:59) and `n_{scalar} = 1 + \varepsilon_{11}/7` for a massive defect (`manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/ponderomotive-equivalence.md`:14). Fed through canon's own Gordon metric, those are two different spacetimes, and only one of them is GR.

| quantity | AVE derived here | measured (external import) | tension |
|---|---|---|---|
| $\gamma$ (light) | $1$ | Cassini $1 \pm 2.3\times10^{-5}$ | **pass** |
| solar-limb deflection | $1.7517''$ | $1.75''$ | **pass** |
| $\gamma$ (matter) | **$0$ exactly** | $1$ | $\sim4.3\times10^{4}\sigma$ |
| $\beta$ (matter) | **$3/2$ exactly** | LLR $1 \pm 1.1\times10^{-4}$ | $\sim4.5\times10^{3}\sigma$ |
| Mercury perihelion | **$7.163''$/century** | $42.98 \pm 0.04$ | $895\sigma$ |
| Hulse-Taylor periastron | **$0.7044^\circ$/yr** | $4.226595(5)$ | short by $3.522^\circ$/yr |

$$F \;=\; \frac{2-\beta+2\gamma}{3} \;=\; \frac{2 - 3/2 + 0}{3} \;=\; \frac{1}{6}.$$

**Independently confirmed by direct geodesic integration** (§9): apsidal-angle quadrature in the AVE matter metric returns $0.1666666632$ of the GR baseline $6\pi x$, while the same integrator on an isotropic-Schwarzschild **control** returns $1.000000289$ of it. The control is what makes the AVE number a measurement of the metric rather than of the integrator.

### THE STRUCTURAL REASON — stated here, not only in §2

A refractive index is **one** scalar function of $r$. A weak-field metric needs **two** independent functions, and $\gamma$ *is* the second one. Canon's own Gordon metric,
`manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/gordon-optical-metric.md`:17 verbatim
$g_{\mu\nu}^{AVE} = \eta_{\mu\nu} + \left(1 - \frac{1}{n^{2}(r)}\right)u_{\mu}u_{\nu}$,
gives $g_{00} = -1/n^2$ and $g_{ij} = \delta_{ij}$ **exactly**, for any $n$ and any slope. A metric whose spatial part is flat has $\gamma = 0$ identically. No coefficient choice inside the $/7$ family can move it, because the family never enters $g_{ij}$ at all.

**Stated one level deeper (§2.5):** the two functions a graded medium really has are the local characteristic speed $c_{eff}=1/\sqrt{LC}$ and the local internal rest frequency $\Omega=\sqrt{S/C}$, and a scalar index wires **one knob into both slots** — forcing the speed slope and the clock slope equal, which is $\gamma$ set to zero by construction.

### ⚠ WHAT THIS IS, AND WHAT IT IS NOT — read before quoting any number above

- **This is not a new falsification of AVE's optics.** $\gamma_{light} = 1$ and $1.7517''$ hold. §6 argues they are a *calibrated consistency check* and not an emergence-class result, which is a downgrade of a claim's **class**, not of its truth.
- **This is not an engine bug.** No engine ran. It is a property of two written constitutive statements and the metric canon writes for them.
- **This does not adjudicate the fix.** §7 names the cheapest repair inside the framework. Naming a repair is not performing one, and this lane edits no canonical file.
- **The matter-sector numbers are only as good as the assignment that produces them.** They follow from taking `ponderomotive-equivalence.md`:14 literally as the metric a massive test body moves in. Canon's own quality record calls that assignment *"asserted by mechanical analogy rather than derived from a wave-equation projection"* (`manuscript/ave-kb/vol3/claim-quality.md`:1158). **If that assignment falls, these numbers fall with it** — which is the point of §7.


### ★ FORWARD POINTER (added 2026-08-27, after the derivation above was frozen) — this is not a dead end

A repair has since been derived on the sibling branch **`research/2026-08-27-two-knob-gravity-repair`**, by a route sharing no assumptions with anything above: a lossless graded LC ladder, WKB, Hamiltonian ray tracing on $H = \omega(k,r)$, **no metric anywhere**. It reproduces $F = 1/6$ exactly, with its own $60$-digit ray quadrature and its own GR isotropic-Schwarzschild control returning the textbook $6\pi x$.

**Nothing above softens.** The number is now confirmed from two framings, and the sibling route locates the defect one level deeper than "a scalar index has no spatial part":

> **The precession is set by three exponents of TWO independent constitutive functions** — the local characteristic speed $c_{eff} = 1/\sqrt{LC}$ and the local internal rest frequency $\Omega = \sqrt{S/C}$:
> $$c_{eff} = c\,(1 - a_1U + a_2U^2),\qquad \Omega = \Omega_\infty(1 - b_1U + b_2U^2),\qquad U \equiv GM/c^2r$$
> $$\Delta\phi = \frac{\pi GM}{c^2 \ell_p}\left(4a_1 - b_1 - \frac{2b_2}{b_1}\right).$$

**The Gordon construction with a scalar index wires ONE knob into BOTH slots.** $n$ sets the speed *and* the clock: $c_{eff} = c/n$ **and** $\Omega = \Omega_\infty/n$. So $a_1 = b_1 = q$ is forced, $b_2 = q^2$, and

$$4q - q - \frac{2q^2}{q} = q$$

— the bracket **collapses to the bare index slope**. At $q = 1$ that is $\Delta\phi = \pi GM/(c^2\ell_p)$, exactly one sixth of GR's $6\pi$. **That identity is the $1/6$**, and it is a sharper statement of the same defect than "$\gamma = 0$ because $g_{ij} = \delta_{ij}$."

**Verified against this document's own frame** (not carried on trust — the bridge is exact):

$$\beta = \tfrac12 + b_2,\qquad \gamma = a_1 - b_1 \;\Longrightarrow\; F = \frac{2a_1 - b_2 - \tfrac12}{3},$$

which reproduces $\Delta\phi = \pi(4a_1 - b_1 - 2b_2/b_1)\,m/\ell_p$ at $b_1 = 1$ identically. Checked at both endpoints: $(a_1,b_1,b_2) = (1,1,1)$ — the one-knob Gordon case — gives $\gamma = 0$, $\beta = 3/2$, $F = 1/6$; and $(2,1,\tfrac12)$ gives $\gamma = 1$, $\beta = 1$, $F = 1$, i.e. **GR at $O(m)$**, with the sibling branch reporting Mercury at $42.9801''$/century ($+0.0\sigma$).

**And canon already carries both numbers, in one leaf.** `temporal-spatial-lattice-decomposition.md`:24 calls $n_{temporal} = 1 + 2U$ the *"**bulk/coordinate-time** temporal propagation index"* — that is $a_1 = 2$ — and in the same sentence calls the *"proper tick of a clock sitting at $r$"* $\sqrt{g_{00}} = \sqrt{S} \approx 1 - GM/(c^2r)$ — that is $b_1 = 1$. **So the $1/7$ projection is the CLOCK grading, and the error was feeding it into a Gordon optical index that then overwrote the SPEED slot with the same number.**

> ### ⚠ CARRY THIS CAVEAT WITH EQUAL WEIGHT
> **$(a_1, b_1, b_2) = (2, 1, \tfrac12)$ currently WORKS. Nothing yet FORCES it.**
> Whether the substrate's constitutive map compels those three exponents, or merely admits them, is **the difference between a derivation and a fit**, and it is **OPEN**. Until it closes, the repair is a demonstration that the framework has room for GR — not a demonstration that the framework predicts GR. Read §6: this lane's verdict on *calibrated-vs-derived* applies to the repair exactly as it applies to $Q=2$.

---

## §1 — THE DERIVED-vs-IMPORTED LEDGER

**This is the most load-bearing section in the document.** A reproduction that imports its coefficients is a consistency check, not a derivation — so every step in both chains carries a tag. `DERIVED` = follows by algebra/calculus from the row above it. `IMPORTED` = its VALUE (or its truth) comes from outside the substrate chain, whether from GR, from a mechanical analogy, from CODATA/IAU, or from an observation.

### §1.1 — The shared trunk (both sectors)

| # | step | tag | basis / where the import enters |
|---|---|---|---|
| T1 | Vacuum is a linear elastic continuum with bulk $K$ and shear $G$; trace-reversal fixes $K = 2G$ | **IMPORTED** | $K=2G$ is GR-imported. `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/one-seventh-impedance-projection.md`:18 verbatim: *"the **value** $\nu=2/7$ is **GR-imported** via $K=2G$ (PR#261)"*; re-confirmed at the ratified $z=3$ srs carrier (PR#506) — *"not crystalline/network-derived"* |
| T2 | $\nu_{vac} = \dfrac{3K-2G}{2(3K+G)} = \dfrac{2}{7}$ at $K = 2G$ | **DERIVED** | pure algebra on T1. `vacuum-poisson-ratio.md`:13. Re-run this lane: sympy returns $2/7$ exactly. **Only the FORM is derived — the value rides T1.** |
| T3 | $\kappa \equiv c^4/(7G)$, the bias-law stiffness | **IMPORTED** | `gordon-optical-metric.md`:20 ($T_{max,g}=\xi T_{EM}=c^4/7G$); re-ratified `manuscript/common_equations/eq_axiom_5.tex`:76-77. The file's own derivation-grade note :134 verbatim: *"kappa = c^4/7G and nu = 2/7 stay GR-imported (#261 untouched)"* |
| T4 | the coefficient $7$ in $\varepsilon_{11} = 7GM/c^2r$ is $2/\nu_{vac}$ | **IMPORTED** | stated at four sites (§11 row C7). `manuscript/ave-kb/vol3/claim-quality.md`:1131 verbatim: *"the factor $7 = 2/\nu_{vac}$"*. It is not an independent number; it is $\nu_{vac}$ inverted and doubled. |
| T5 | $-\left(\frac{c^{4}}{7G}\right)\nabla^{2}\varepsilon_{11}(r) = 4\pi Mc^{2}\delta^{3}(r)$ | **IMPORTED** (posited law) | `gordon-optical-metric.md`:25, canonical; `eq_axiom_5.tex`:76 clause G. `eq_axiom_5.tex`:127-135 grades the source law **POSTULATED**, *"not a theorem of Axioms 1–4"* |
| T6 | $\varepsilon_{11}(r) = 7GM/(c^2 r)$ | **DERIVED** | convolution of T5 with the 3D Laplacian Green's function $-1/4\pi r$. **Re-derived this lane and it reproduces exactly**: $\nabla^2\varepsilon = -(28\pi GM/c^2)\delta^3 \Rightarrow \varepsilon = 7GM/c^2r$ |
| T7 | the Gordon optical metric $g_{\mu\nu} = \eta_{\mu\nu} + (1-1/n^2)u_\mu u_\nu$ | **IMPORTED** | Gordon 1923. `gordon-optical-metric.md`:12 verbatim: *"As established historically by the Gordon Optical Metric"* |
| T8 | $\Rightarrow g_{00} = -1/n^2$ and $g_{ij} = \delta_{ij}$ **exactly** | **DERIVED** | one matrix line from T7 with $u_\mu = (-1,0,0,0)$, $\eta = \mathrm{diag}(-1,1,1,1)$. Verified symbolically (§9.1) |

### §1.2 — The light branch

| # | step | tag | basis |
|---|---|---|---|
| L1 | the photon is transverse and couples to $\nu_{vac}\varepsilon_{11}$, not to the bulk | **IMPORTED** (assertion) | `manuscript/ave-kb/vol3/claim-quality.md`:1149 verbatim: *"is asserted by **mechanical analogy**, not derived from a wave-equation projection. This is the one soft joint in the derivation."* |
| L2 | $n_\perp = 1 + \nu_{vac}\varepsilon_{11} = 1 + 2GM/c^2r$ | **DERIVED** | Op19, `manuscript/ave-kb/common/operators.md`:59, status CANONICAL |
| L3 | $\;Q \equiv \nu_{vac}\cdot 7 = \nu_{vac}\cdot(2/\nu_{vac}) = 2$ | **DERIVED — and $\nu$-BLIND** | the two factors are reciprocal by T4, so $Q=2$ for **any** $\nu_{vac}$. Canon states the cancellation itself: `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/geo-synchronous-impedance.md`:20 verbatim — *"The factor 7 from the K4 Poisson ratio $\nu_{vac} = 2/7$ cancels the factor 2/7 from the AVE-modified strain coupling, recovering exactly the GR $2GM/c^2 r$ Schwarzschild form."* |
| L4 | eikonal deflection $\delta = 2Q\,GM/(bc^2)$ | **DERIVED** | transverse-gradient integral; matches the 2026-06-05 audit's symbolic kernel (`research/2026-06-05_gravity-ppn-coherence-result.md`:41) |
| L5 | $\gamma_{light} = Q - 1 = 1$ | **DERIVED** | comparing L4 to the PPN form $\delta = (1+\gamma)\,2GM/(bc^2)$ |
| L6 | solar-limb $\delta = 1.7517''$ | **DERIVED** ← **IMPORTED inputs** | $G$, $M_\odot$, $c$ from `src/ave/core/constants.py`; $R_\odot$ from `src/ave/gravity/solar_impedance.py`:68. Constant-choice sensitivity is real and reported in §6 |
| L7 | Cassini $\gamma - 1 = (2.1\pm2.3)\times10^{-5}$ | **IMPORTED** | external observational datum (Bertotti–Iess–Tortora 2003). Not re-fetched by this lane — see §11 |

### §1.3 — The matter branch

| # | step | tag | basis |
|---|---|---|---|
| M1 | a massive defect is an isotropic 3D volumetric packet and couples to the spherical part of the strain | **IMPORTED** (assertion) | the same soft joint as L1, same cite `claim-quality.md`:1149 |
| M2 | spherical part $=\frac{1}{3}\theta = \frac{1}{3}\!\left(\frac{3}{7}\varepsilon_{11}\right) = \frac{1}{7}\varepsilon_{11}$ | **DERIVED** | `one-seventh-impedance-projection.md`:13; re-derived here from $\varepsilon_{tt} = -\nu\varepsilon_{rr}$ at $\nu = 2/7$ |
| M3 | $n_{scalar} = 1 + \varepsilon_{11}/7 = 1 + GM/c^2r$ | **DERIVED** | `ponderomotive-equivalence.md`:14, canonical |
| M4 | matter moves on the Gordon metric built from $n_{scalar}$ | **IMPORTED** (assertion) | the ponderomotive Lagrangian $L = -mc^2\sqrt{1-n^2v^2/c^2}/n$; `research/2026-05-17_hulse-taylor-substrate-native-derivation-sketch.md`:33. **This is the load-bearing assignment.** |
| M5 | $\gamma_{matter} = 0$ **exactly** | **DERIVED** | immediate from T8: $g_{ij} = \delta_{ij}$, so $2\gamma U \equiv 0$. Holds for **any** $n$ and any coefficient |
| M6 | $\beta_{matter} = 3/2$ **exactly** | **DERIVED — and coefficient-BLIND** | $-g_{00} = (1+c_mU)^{-2} = 1 - 2c_mU + 3c_m^2U^2$; against $1 - 2W + 2\beta W^2$ with $W = c_mU$ this is $\beta = 3/2$ **for every $c_m$**. Verified symbolically |
| M7 | $F = (2-\beta+2\gamma)/3 = 1/6$ | **DERIVED** | standard PPN perihelion factor; the same function the 2026-06-05 verify script already ships (`src/scripts/verify/gravity_ppn_coherence.py`:142) |
| M8 | Mercury $7.163''$/century | **DERIVED** ← **IMPORTED inputs** | orbital elements $a,e,P$ are external observational inputs; $GM_\odot$ imported. GR baseline reproduces $42.98''$ |
| M9 | Hulse-Taylor $0.7044^\circ$/yr | **DERIVED** ← **IMPORTED baseline** | $F\times4.226595$; the $4.226595(5)$ is the measured/GR value, imported |
| M10 | LLR $\lvert\beta-1\rvert \lesssim 1.1\times10^{-4}$ | **IMPORTED** | external observational datum. Not re-fetched by this lane — see §11 |

### §1.4 — What the ledger says out loud

- **The light branch has exactly one number in it, and that number is an identity.** $Q = 2$ is $\nu_{vac}$ times its own reciprocal-times-two. Both factors are GR-imported *and* they cancel, so the branch is insensitive to the imported value: it would return $Q = 2$ for $\nu_{vac} = 1/3$, for $\nu_{vac} = 1/5$, for anything. **Solar-system light bending therefore constrains $\nu_{vac}$ not at all.**
- **The matter branch's coefficient is the only $\nu$-sensitive quantity in the chain**: $c_m(\nu) = \frac{2(1-2\nu)}{3\nu}$, which is $1$ at $\nu = 2/7$. But $\gamma = 0$ and $\beta = 3/2$ are **both** independent of $c_m$, so even the $\nu$-sensitive branch reports nothing about $\nu$ in the PPN observables. $c_m$ would have to be $2$ (i.e. $\nu = 1/5$) for matter and light to share a coefficient — and even then $\gamma$ would still be $0$, because $\gamma=0$ comes from the metric's FORM, not from any coefficient.
- **Neither branch is emergence-class.** The light branch is CONSISTENCY (calibrated identity reproducing GR). The matter branch is a genuine forward derivation whose forward prediction is **refuted**.

## §2 — Two metrics, two gammas: the derivation chain

### §2.1 — One strain field, two indices — canon's own words

`manuscript/ave-kb/vol3/gravity/ch02-general-relativity/double-deflection.md`:39 states the split as a *feature*:

$$\frac{\delta_{\text{light}}}{\delta_{\text{matter}}} = \frac{n_{\perp}-1}{n_{\text{scalar}}-1} = \frac{2/7}{1/7} = 2$$

and `:44` names the matter value explicitly: $\delta_{\text{matter}} = 2GM/(bc^2)$, **"(Newton / Soldner 1801)"**. That is the *pre-relativistic* value. The matter sector's disagreement with GR is therefore not hidden anywhere — **it is the headline of canon's flagship gravity derivation**, stated as the thing that makes the framework interesting. What was never done is carry it into the orbital sector, where "matter gets the Newtonian coefficient" stops being a charming reframing of 1801 and starts being $895\sigma$ on Mercury.

### §2.2 — Feed each index through canon's own metric

Gordon (T7/T8), with $u_\mu$ the static observer:

$$g_{\mu\nu} = \eta_{\mu\nu} + \left(1 - \tfrac{1}{n^2}\right)u_\mu u_\nu
\;\Longrightarrow\;
g_{00} = -\frac{1}{n^2},\qquad g_{ij} = \delta_{ij}.$$

Verified symbolically — the full matrix comes back `[[-1/n**2,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]`. **The spatial block is the identity, exactly, with no $n$ in it.** Against the isotropic PPN form $g_{ij} = (1+2\gamma U)\delta_{ij}$ that is $\gamma = 0$, and it is $\gamma = 0$ for *every* index the framework might assign — $n_\perp$, $n_{scalar}$, $n_{temporal}$, $n_{spatial}$, all of them.

For the matter index $n_{scalar} = 1 + U$:

$$-g_{00} = \frac{1}{(1+U)^2} = 1 - 2U + 3U^2 + O(U^3)$$

against $-g_{00} = 1 - 2U + 2\beta U^2$, giving $2\beta = 3$, i.e.

$$\boxed{\;\gamma = 0,\qquad \beta = \tfrac32,\qquad F = \frac{2-\beta+2\gamma}{3} = \frac{1}{6}\;}$$

**Both are structural, not numerical.** $\gamma = 0$ survives any coefficient because the spatial metric is flat. $\beta = 3/2$ survives any coefficient because $(1+cU)^{-2}$ has the same $W^2/W$ ratio for every $c$ once $W \equiv cU$ is the effective potential. There is no knob in the $/7$ family that reaches either one.

### §2.3 — The perihelion factor, and where it is already in the tree

The PPN advance per orbit is $\Delta\phi = F\cdot 6\pi GM/(c^2a(1-e^2))$ with $F = (2-\beta+2\gamma)/3$. That function is **already shipped in the repository**, at `src/scripts/verify/gravity_ppn_coherence.py`:142 —

```python
    return sp.simplify((2 - beta + 2 * gamma) / 3)
```

— and the 2026-06-05 audit fed it $\gamma$ from the two *photon-candidate* indices while pinning $\beta = 1$ by hand. Feeding it the matter sector's own $(\gamma,\beta) = (0, 3/2)$ is a one-line change to an existing, merged instrument, and it returns $1/6$.

### §2.4 — Why "$1/6$" and not "some correction"

$1/6$ is not a perturbation. Written out:

| contribution to $F$ | GR | AVE matter sector |
|---|---|---|
| $2/3$ (the Newtonian-limit piece) | $0.667$ | $0.667$ |
| $-\beta/3$ | $-0.333$ | $-0.500$ |
| $+2\gamma/3$ | $+0.667$ | $0.000$ |
| **total $F$** | **$1.000$** | **$0.167$** |

**Five sixths of GR's perihelion advance is the $\gamma$ term.** A theory with $\gamma = 0$ does not get a slightly-wrong perihelion; it loses the dominant contribution and then over-subtracts on $\beta$. The two errors do not cancel — they compound, $-0.500$ instead of $-0.333$ on top of $0$ instead of $+0.667$.


### §2.5 — Sharpened: one knob, two slots

"A refractive index is one scalar function and the metric needs two" is correct but under-specific. **The two functions a lossless graded medium actually has are the local characteristic speed and the local internal rest frequency**, and they are independent:

$$c_{eff}(r) = \frac{1}{\sqrt{L(r)C(r)}},\qquad \Omega(r) = \sqrt{\frac{S(r)}{C(r)}}.$$

$c_{eff}$ is what a *signal crossing* the region does; $\Omega$ is what a *resonator sitting* in it does. In a general graded LC ladder $L$, $C$ and $S$ grade independently, so $c_{eff}$ and $\Omega$ carry **two** independent slopes. That is exactly the two functions the weak-field metric needs.

**A scalar refractive index wires one knob into both slots.** Writing $n(r)$ and building the Gordon metric from it forces

$$c_{eff} = \frac{c}{n}\quad\textbf{and}\quad \Omega = \frac{\Omega_\infty}{n}$$

from the *same* $n$. In the $(a_1,b_1,b_2)$ language of the forward pointer that is $a_1 = b_1 = q$, $b_2 = q^2$, and the precession bracket collapses:

$$4a_1 - b_1 - \frac{2b_2}{b_1} \;=\; 4q - q - 2q \;=\; q.$$

**The precession degenerates to the bare index slope.** In this document's own coordinates the same collapse reads $\gamma = a_1 - b_1 = 0$: $\gamma$ *is* the gap between the speed slope and the clock slope, and a one-knob model sets that gap to zero by construction.

So the three statements below are one statement seen three ways, and they are all exact:

| framing | the defect |
|---|---|
| metric | $g_{ij} = \delta_{ij}$, so $\gamma \equiv 0$ |
| constitutive | $a_1 = b_1$, so the speed slope and the clock slope cannot differ |
| circuit | one graded parameter cannot set $\sqrt{LC}$ and $\sqrt{S/C}$ independently |

**Plumber-physical:** the substrate is being modelled as a transmission line where changing the dielectric loading is the *only* thing gravity does. Then the wave slows and the tank detunes by the same factor, necessarily. GR says the tank detunes by $U$ while the wave slows by $2U$ — **the line's series and shunt elements do not grade together**, and the factor-of-two between them is $\gamma$.

---

## §3 — Why the tensor repair failed

The obvious repair, once $\gamma = 0$ is on the table, is: *stop using a scalar index; build the genuine rank-2 strain tensor the substrate is supposed to have, and let its anisotropy grade $g_{ij}$.* That repair was attempted and it does not close. Three independent reasons, each fatal on its own.

### §3.1 — $\varepsilon_{11} = 7GM/c^2r$ is not an elastic equilibrium field

Canon's profile comes from a **scalar Poisson equation** — `gordon-optical-metric.md`:25, re-ratified as clause G at `eq_axiom_5.tex`:76:

$$-\left(\frac{c^{4}}{7G}\right)\nabla^{2}\varepsilon_{11}(r) = 4\pi Mc^{2}\delta^{3}(r)
\;\Longrightarrow\;
\varepsilon_{11}(r) = \frac{7GM}{c^{2}r}$$

(reproduced exactly this lane from the $-1/4\pi r$ Green's function). But **static elastic equilibrium is a different equation.** For a purely radial displacement $u_r(r)$ the Navier equation reduces to

$$(\lambda+2\mu)\left[u'' + \frac{2u'}{r} - \frac{2u}{r^2}\right] = 0,$$

and `sympy.dsolve` returns the **complete** solution space:

```
dsolve -> Eq(u(r), C1/r**2 + C2*r)
eps_rr = -2*C1/r**3 + C2
eps_tt =    C1/r**3 + C2
```

The spherically symmetric exterior strain field is $\{A,\; B/r^3\}$. **$1/r$ is not in that space.** A $1/r$ strain is not a solution of static elasticity around a point source at any moduli and any coupling — it is a solution of a *potential* problem that has been given a strain's name.

### §3.2 — $\lambda$ and $\nu$ drop out entirely, so no $\nu$-dependent projection can arise

Because $(\lambda + 2\mu) \neq 0$ divides out, the exterior solution space carries **no moduli at all**. Checked explicitly: the free symbols of $\varepsilon_{rr}$ and $\varepsilon_{tt}$ intersected with $\{\lambda,\mu\}$ is the **empty set**. So the anisotropy ratio of a genuine exterior elastic field is

$$\frac{\varepsilon_{tt}}{\varepsilon_{rr}}\bigg|_{\text{decaying}} = \frac{B/r^3}{-2B/r^3} = -\frac{1}{2}\quad\textbf{independent of }\nu.$$

**No $\nu$-dependent $/7$ projection can arise from exterior elasticity at any coefficient.** The $/7$ family is a Poisson-ratio family; the exterior elastic field has no Poisson ratio in it.

### §3.3 — Following clause G forward gives a real tensor, at the wrong order and with the wrong trace

Clause G's bound response is $\mathbf{u}_0 = -\mathcal{A}_g\nabla\varepsilon_{11}$ (`eq_axiom_5.tex`:75). Evaluated on the canon profile:

$$u_0(r) = \frac{7\mathcal{A}_g GM}{c^2 r^2}\hat{r}.$$

This **is** an exact static-equilibrium solution — the Navier residual on it is identically $0$, checked symbolically. It is the $B/r^2$ branch with $B = 7\mathcal{A}_gGM/c^2$. Its strain tensor is genuinely anisotropic, with ratio exactly $-1/2$. But:

1. **It falls as $1/r^3$**, i.e. tidal order. A $1/r^3$ field cannot source a $1/r$ metric coefficient at *any* coupling constant — this is a scaling statement, not a magnitude statement, so no choice of $\mathcal{A}_g$ rescues it.
2. **It is exactly trace-free.** $\theta_{\text{decaying}} = \varepsilon_{rr} + 2\varepsilon_{tt} = -2B/r^3 + 2B/r^3 = 0$, checked symbolically. The whole trace of $\{A r,\,B/r^2\}$ is $3A$ — it comes only from the uniform-dilatation branch, which is not localized and is not sourced by a point mass.

Point 2 is worth stating in plumber terms: **an exterior static elastic field around a point source is volume-preserving.** Squeeze a shell inward radially and it fattens tangentially by exactly the amount that keeps the volume fixed; that is what $-1/2$ means. So the *isotropic* projection — the $\frac{1}{3}\theta$ that the $1/7$ coupling projects, `one-seventh-impedance-projection.md`:13 — is **identically zero** on a genuine exterior elastic field. If $\varepsilon_{11}$ were a mechanical strain, $n_{scalar}$ would be $1$ exactly and there would be **no gravity on matter at all.**

### §3.4 — Canon already says this, in its own words

That is not a lane-authored objection. `eq_axiom_5.tex`:145-149 records it:

> `⚑ NON-CIRCULARITY OBSERVATION (R48 walk note; ROUTED to the residence-lane family,`
> `recorded not adjudicated). Clause G is non-circular only if the bias eps_11 is a`
> `DISTINCT object from mechanical strain (grad u). The A_g = c*l_node^2 hypothesis's`
> `57-order miss is evidence FOR that distinctness — one object would have made`
> `A_g ~ l_node^2 work. Stated as an observation with its routing, not as a finding.`

and R55 renamed the object accordingly — `:45` verbatim: *"eps_11's canonical name is THE BIAS"*; `:73` verbatim: *"The operating-point **bias** $\varepsilon_{11}$ is the bound sector's potential"*.

**The consequence canon has not drawn.** Op19 — `n(r) = 1 + \nu_{vac}\cdot\varepsilon_{11}$, `operators.md`:59, status **CANONICAL** — applies an **elastic Poisson contraction** ($\nu_{vac}$ is literally the ratio of transverse to axial *strain*) to an object canon's own newest ruling declares **is not an elastic strain**. The same holds for the $1/7$ isotropic projection at `one-seventh-impedance-projection.md`:13, which computes $\frac{1}{3}\theta$ from $\varepsilon_{11}$ using the uniaxial-strain relation $\varepsilon_{tt} = -\nu\varepsilon_{rr}$.

This is surfaced, **not resolved** — the resolution is Grant's and is routed at `_orchestration/open-items/2026-08-27-eps11-four-objects.md`.

## §4 — `eps_11` is four objects across canon

The symbol $\varepsilon_{11}$ (also written $\epsilon_{11}$, and aliased $\chi_{vol}$) carries **four mutually inconsistent ontologies** across canon at HEAD. All four are simultaneously live; each is load-bearing for something. The sites below are the ones **this lane opened and read**; the method and its blind spots are §10.

### Object A — a principal *component* of a rank-2 strain tensor

| site | verbatim |
|---|---|
| `manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/gordon-optical-metric.md`:20 | *"the localised **1D principal radial polarisation strain** ($\epsilon_{11}$) field generates the $1/r$ Newtonian potential"* |
| `manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/transverse-refractive-index.md`:14 | *"it exerts a radial pull, acting as the continuous source of the principal radial tensile strain ($\epsilon_{11} > 0$)"* |
| `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md`:14 | *"The principal radial strain $\varepsilon_{11} = 7GM/(c^2 r)$ compresses the lattice asymmetrically."* |
| `manuscript/common_equations/eq_gravity_derived.tex`:50 | *"The principal radial strain $\varepsilon_{11} = 7GM/(c^2 r)$ compresses the lattice asymmetrically."* |

Under Object A the Poisson contraction is legitimate: `transverse-refractive-index.md`:16 uses $h_\perp = -\nu_{vac}\cdot\epsilon_{11}$, which is exactly the uniaxial-strain relation, and it needs $\varepsilon_{11}$ to be $\varepsilon_{rr}$.

### Object B — a *volumetric trace*

| site | verbatim |
|---|---|
| `manuscript/ave-kb/vol3/gravity/ch02-general-relativity/double-deflection.md`:22 | $n_{\text{scalar}}(\mathbf{r}) = 1 + \tfrac{1}{7}\chi_{vol}(\mathbf{r})$ |
| `…double-deflection.md`:28 | $n_{\perp}(\mathbf{r}) = 1 + \nu_{vac}\,\chi_{vol}(\mathbf{r}) = 1 + \tfrac{2}{7}\chi_{vol}(\mathbf{r})$ |
| `…double-deflection.md`:42 | *"With $\chi_{vol}(r) = 7GM/(c^2 r)$"* |
| `manuscript/ave-kb/vol3/claim-quality.md`:1141 | *"with $\chi_{vol} = 7GM/(c^2 r)$"* |

**Objects A and B are set numerically equal** ($\chi_{vol} = \varepsilon_{11} = 7GM/c^2r$) while being named differently — and canon's own trace formula says they cannot be equal. `one-seventh-impedance-projection.md`:13:

$$\text{Isotropic Projection} = \frac{1}{3}\theta = \frac{1}{3}\left(\frac{3}{7}\epsilon_{11}\right) \equiv \frac{1}{7}\epsilon_{11}$$

i.e. **$\theta = \frac{3}{7}\varepsilon_{11}$**. If $\chi_{vol}$ is the volumetric trace $\theta$, then $\chi_{vol} = \frac37\varepsilon_{11}$, and every coupling written against $\chi_{vol}$ is off by $3/7$ from the same coupling written against $\varepsilon_{11}$. Canon writes both spellings and equates the numbers.

> **The discrepancy is exactly $3/7$**, i.e. $\approx 0.4286$. It is not a small print issue; it is a factor of $2.33$.

`double-deflection.md`:24 makes the collision explicit in one sentence: *"This is the projection a 1D uniaxial stress makes onto the isotropic spherical bulk tensor $\tfrac{1}{3}\theta\delta_{ij}$"* — the argument is being **called** volumetric while being **used** as the 1D uniaxial component.

### Object C — a scalar field solving a scalar Poisson equation

| site | verbatim |
|---|---|
| `gordon-optical-metric.md`:25 | $-\left(\frac{c^{4}}{7G}\right)\nabla^{2}\epsilon_{11}(r) = 4\pi Mc^{2}\delta^{3}(r)$ |
| `manuscript/common_equations/eq_axiom_5.tex`:76 | $-\nabla\cdot\!\left[\kappa\, D(A)\,\nabla\varepsilon_{11}\right] = 4\pi\,T_{00},\quad \kappa = \frac{c^4}{7G}$ |

A single scalar obeying a single scalar elliptic equation. It has **one degree of freedom**, and §5 is the consequence.

### Object D — a *potential*, explicitly NOT mechanical strain

| site | verbatim |
|---|---|
| `eq_axiom_5.tex`:45 | `eps_11's canonical name is THE BIAS. "grade" demotes to informal use.` |
| `eq_axiom_5.tex`:73 | *"The operating-point **bias** $\varepsilon_{11}$ is the bound sector's potential, and the **bound response** $\mathbf{u}_0$ is its gradient"* |
| `eq_axiom_5.tex`:146-147 | `Clause G is non-circular only if the bias eps_11 is a` / `DISTINCT object from mechanical strain (grad u).` |

Object D is the **newest** ruling in the set (R55, 2026-08-24) and it is the one that breaks the others: if $\varepsilon_{11}$ is a potential whose *gradient* is the displacement, then $\varepsilon_{11}$ has the dimensions and the role of $\phi$, not of $\partial u/\partial x$ — and every Poisson-ratio contraction applied to it (Op19, the $1/7$ projection, $h_\perp = -\nu\epsilon_{11}$) is applying a strain-to-strain relation to a non-strain.

### What this does to the PPN result

**Nothing.** $\gamma = 0$ follows from the Gordon metric's *form*, and $\beta = 3/2$ from the clock's *form*; both are blind to which object $\varepsilon_{11}$ is and to the coefficient in front of it (§1.4). The four-objects question does not rescue the matter sector — it is a separate, and separately serious, coherence defect that this lane surfaced while working the PPN chain. It is routed at `_orchestration/open-items/2026-08-27-eps11-four-objects.md` and **not adjudicated here**.

## §5 — The /7 family is five contractions of one rank-2 tensor

### §5.1 — The identities

Take **one** uniaxial strain tensor: a radial principal component $\varepsilon_{rr} = \varepsilon_{11}$ with the Poisson-contracted tangential components $\varepsilon_{tt} = -\nu_{vac}\varepsilon_{11}$, at $\nu_{vac} = 2/7$. Every member of the $/7$ family is a standard contraction of that one object. Verified symbolically:

| number | contraction | value in $\varepsilon_{11}$ | canon's own name for it |
|---|---|---|---|
| $1/7$ | spherical part per direction, $\theta/3$ | $\varepsilon_{11}/7$ | *"The $1/7$ Isotropic Impedance Projection"*, `one-seventh-impedance-projection.md`:13 |
| $2/7$ | tangential magnitude $\lvert\varepsilon_{tt}\rvert$ — which is $\nu_{vac}$ itself | $2\varepsilon_{11}/7$ | the vacuum Poisson ratio, `vacuum-poisson-ratio.md`:13 |
| $3/7$ | the trace $\theta = (1-2\nu)\varepsilon_{11}$ | $3\varepsilon_{11}/7$ | implicit in `one-seventh-impedance-projection.md`:13; the $\sqrt{3/7}=\sqrt{1-2\nu_{vac}}$ dilatational signature at `manuscript/ave-kb/common/full-derivation-chain.md`:370 |
| $9/7$ | von Mises equivalent of the deviator, $\sqrt{\tfrac32 e_{ij}e_{ij}}$ | $9\varepsilon_{11}/7$ | $n_{spatial}$, `temporal-spatial-lattice-decomposition.md`:19 |
| $11/7$ | $2\varepsilon_{rr}-\theta$ (equivalently $\tfrac27+\tfrac97$) | $11\varepsilon_{11}/7$ | *"full lattice density"*, `LIVING_REFERENCE.md`:162 |

with the deviator $e_{rr} = \tfrac67\varepsilon_{11}$, $e_{tt} = -\tfrac37\varepsilon_{11}$ giving
$\sqrt{\tfrac32\left(\tfrac{36}{49}+2\cdot\tfrac{9}{49}\right)} = \sqrt{\tfrac{81}{49}} = \tfrac97$ **exactly**.

And the denominator is not a free integer either:

$$\nu = \frac{3K-2G}{2(3K+G)} \;\Longrightarrow\; \text{denominator} = 3\frac{K}{G}+1 \;\overset{K=2G}{=}\; 7.$$

**"7" is identically $3K/G + 1$.** One imported ratio, $K=2G$, writes the whole family.

> **⚑ HONEST SCOPE on this table.** Canon *derives* the $1/7$, $2/7$ and $3/7$ rows from the strain tensor explicitly at the cited sites. The $9/7$-as-von-Mises and $11/7$-as-$(2\varepsilon_{rr}-\theta)$ readings are **identifications made by this lane**, verified arithmetically; **I did not find a first-principles derivation of $9/7$ from the strain tensor at the sites I read** (`temporal-spatial-lattice-decomposition.md`, `eq_gravity_derived.tex`, `ch01-gravity-yield/index.md`, `translation-gravity.md` all *state* it as a decomposition component). Canon's own provenance for $11/7$ is the sum $\tfrac27+\tfrac97$, which is numerically the same thing. The table is offered as a unification observation, **not** as a claim that canon derived it this way.

### §5.2 — One object, five views — and one degree of freedom

The family is not five independent couplings that happen to share a denominator. It is one rank-2 tensor seen five ways, and that tensor is fixed by a **single scalar** $\varepsilon_{11}(r)$ through $\varepsilon_{tt} = -\nu\varepsilon_{rr}$ with $\nu$ imported.

**That is the structural reason a scalar-index model results.** With one degree of freedom you can write one refractive index. You cannot write two independent metric functions, and the weak-field metric needs two. Everything in §2 follows from the object's rank, before any coefficient is chosen.

### §5.3 — And solar-system gravity gives ZERO support to the $\nu_{vac}$ triangulation

Two independent statements, both verified:

1. **The light branch is $\nu$-blind by identity.** $Q = \nu_{vac}\cdot(2/\nu_{vac}) = 2$ (§1.2 L3). The deflection is $2Q\,GM/bc^2 = 4GM/bc^2$ for *any* $\nu_{vac}$. Canon states this cancellation itself at `geo-synchronous-impedance.md`:20. **A measurement that returns the same answer for every value of a parameter constrains that parameter not at all.**
2. **The matter branch's PPN coefficients are coefficient-blind.** $\gamma = 0$ is forced by $g_{ij}=\delta_{ij}$ and $\beta = 3/2$ by the $1/n^2$ clock, for every $c_m$ (§1.3 M5/M6). The $\nu$-sensitive quantity $c_m(\nu) = \frac{2(1-2\nu)}{3\nu}$ never reaches an observable.

So neither Cassini, nor solar-limb deflection, nor Mercury, nor LLR carries information about which member of the $/7$ family is right. **If $\nu_{vac} = 2/7$ is to be triangulated, it must be triangulated somewhere other than solar-system gravity.**

> **⚑ FLAG — a handed-down phrasing I could reproduce only in part; flag-don't-fix.**
> The reconciliation that commissioned this document stated the point as *"the $/7$ family is gauge at PPN order — the radial grading is absorbed by a constant areal shift with $dR/dr = 1$ identically at $O(m)$."*
> **The Jacobian half reproduces exactly.** For a graded isotropic spatial metric $B(r) = 1+\kappa\varepsilon_{11}$ with $\varepsilon_{11}=7m/r$, the areal radius is $R = r\sqrt{B} = r + \tfrac{7\kappa}{2}m + O(m^2)$ — an **$r$-independent constant shift** — and sympy returns $dR/dr - 1 = 0$ at $O(m)$, identically.
> **The inference half does not.** Carrying that same metric into Schwarzschild-form coordinates, I get $g_{RR} = 1 + 7\kappa\,m/R$, i.e. $\gamma = 7\kappa/2 \neq 0$. So a graded spatial metric is **not** gauge-removable, and "the $/7$ family is gauge" is not a statement I can reproduce in that form.
> **The conclusion survives on stronger and different footing** — items 1 and 2 above — which is why it is stated that way in this section. The zero-support finding does not rest on the gauge argument. Recorded as a partial reproduction rather than silently restated, per flag-don't-fix.

## §6 — The light result is a consistency check, not a derivation

### §6.1 — What is genuinely good here

Two things, and they are not nothing:

1. **The metric emerged rather than being posited.** AVE does not start from a spacetime metric. It starts from a medium with an index, and the Gordon form *delivers* a Lorentzian metric whose null cone is the light cone. That is a real structural result and it is the reason the framework can talk about lensing at all.
2. **A single non-birefringent light cone.** The transverse sector carries one index, so both polarizations see the same cone — the framework predicts **no vacuum birefringence from a static mass**, which is a genuine forward statement and is consistent with observation.

### §6.2 — What is calibrated

The deflection is $\delta = 2Q\,GM/(bc^2)$ with $Q$ the slope of the photon index. Everything observational rides on $Q$, and

$$Q \;=\; \nu_{vac}\cdot c_1 \;=\; \frac{2}{7}\cdot 7 \;=\; 2,$$

with **both factors GR-imported**:

- $\nu_{vac} = 2/7$: value imported via $K=2G$. `one-seventh-impedance-projection.md`:18 verbatim — *"the *value* $\nu=2/7$ is **GR-imported** via $K=2G$ (PR#261), re-confirmed at the ratified $z=3$ srs carrier by PR#506"*.
- $c_1 = 7$: canon identifies it as $2/\nu_{vac}$ (`claim-quality.md`:1131, and three further sites at §11 row C7); the $\kappa = c^4/7G$ that generates it is graded imported at `eq_axiom_5.tex`:134 — *"kappa = c^4/7G and nu = 2/7 stay GR-imported"*.

**And they are reciprocal, so the product is an identity.** Canon says this in its own voice at `geo-synchronous-impedance.md`:20: *"The factor 7 from the K4 Poisson ratio $\nu_{vac} = 2/7$ **cancels** the factor 2/7 from the AVE-modified strain coupling, recovering exactly the GR $2GM/c^2 r$ Schwarzschild form."*

> ### The honest sentence
> **AVE derives that a single non-birefringent light cone exists and that its deflection is $2Q\,GM/(bc^2)$. The value $Q = 2$ is calibrated.**

That sentence should replace any phrasing that presents $1.75''$ as an AVE output. It is not a retraction — the number is right and the mechanism is a real alternative mechanism — it is a **class** statement, and the corpus already has the machinery for it: `manuscript/consistency-manifest.yaml`:652 grades P10 `type: consistency_check`, and the leaf itself carries the 2026-05-17 scope correction (`einstein-lensing-deflection.md`:8) saying the recovery *"is therefore a **consistency check** … NOT an emergence test"*.

### §6.3 — Constant-choice sensitivity, reported not hidden

The limb deflection is a four-constant product and the corpus's constants are not all the IAU nominal set. Measured this lane:

| $M_\odot$ source | $\delta_{limb}$ |
|---|---|
| `src/ave/core/constants.py`:132, `M_SUN = 1.989e30` (with `G = 6.6743e-11`) | $1.751710''$ |
| $M_\odot = 1.98892\times10^{30}$ | $1.751640''$ |
| IAU nominal $GM_\odot = 1.3271244\times10^{20}$ (bypasses $G$) | $1.751190''$ |

with $R_\odot = 6.957\times10^8$ m from `src/ave/gravity/solar_impedance.py`:68 throughout. The spread is $\sim5\times10^{-4}$ arcsec, i.e. $\sim0.03\%$ — which is the same order as the $0.03\%$ error already booked for P10 in `manuscript/consistency-manifest.yaml`:654 and `README.md`:228. **The headline number is quoted here as $1.7517''$ from the in-tree constants.** A reconciliation that reports $1.7516''$ is using a slightly different $M_\odot$; the difference is bookkeeping, not physics, and it is stated rather than smoothed.

The same sensitivity applies to Mercury: with the in-tree `M_SUN` the GR baseline is $42.9934''$/century and $F=1/6$ gives $7.1656''$; with IAU $GM_\odot$ the baseline is $42.9807''$ and $F=1/6$ gives $7.1634''$. **The verdict is $895\sigma$ either way** — the constant choice moves the third decimal of a number that is wrong by a factor of six.

## §7 — The fix is cheap and inside the framework

### §7.1 — The mechanism of the defect, exactly

Take GR's own metric in isotropic coordinates ($m \equiv GM/c^2$):

$$ds^2 = -\underbrace{\left(\frac{1-m/2R}{1+m/2R}\right)^{2}}_{A}c^2dt^2 + \underbrace{\left(1+\frac{m}{2R}\right)^{4}}_{B}\left(dR^2+R^2d\Omega^2\right)$$

and define its optical index $n_{opt} \equiv \sqrt{B/A} = \dfrac{(1+m/2R)^3}{1-m/2R}$. Then, **exactly and not merely to leading order** (verified symbolically, `B/n_opt**2 - A == 0` returns `True`):

$$g^{\text{GR}}_{\mu\nu} \;=\; B(R)\cdot g^{\text{Gordon}}_{\mu\nu}\big[n_{opt}\big].$$

**GR's metric and the Gordon metric are conformally related, with conformal factor $\Omega^2 = B = 1 + 2U + O(U^2)$ — which is precisely $1 + 2\gamma U$ at $\gamma = 1$.**

Null geodesics are conformally invariant. Timelike geodesics are not.

> **That one sentence is the whole finding.** The Gordon optical metric is the *right* object for light and the *wrong* object for matter, by exactly the conformal factor. Light cannot see $\Omega^2$, so AVE's optics is correct. Matter can, so AVE's matter sector is missing exactly $\gamma$. And $\Omega^2$ is not a small correction — §2.4 shows it carries five sixths of the perihelion advance.

Weak-field, $n_{opt} = 1 + 2m/R + O(m^2)$ — **slope 2, the same $Q=2$ AVE's transverse sector already has.** So the light sectors of the two theories coincide by construction, and the entire disagreement is the conformal factor that AVE's flat $g_{ij} = \delta_{ij}$ throws away.

### §7.2 — The repair

**Put matter on the same T2 cone the light is on** — i.e. treat the physical metric as $\Omega^2\times$(the optical metric) rather than as the optical metric — and everything is Schwarzschild at $O(m)$:

$$-g_{00} = 1 - 2U + 2U^2,\qquad g_{ij} = (1+2U)\delta_{ij} \;\Longrightarrow\; \beta = 1,\;\gamma = 1,\;F = 1$$

(verified symbolically; the series returns exactly those coefficients). In areal coordinates that is $g_{00} = -(1-2m/R)$, $g_{RR} = 1 + 2m/R$ at $O(m)$ — Schwarzschild, and with it Cassini, LLR, Mercury and Hulse-Taylor.

**What must go is the separate scalar index assigned to matter.** $n_{scalar} = 1 + \varepsilon_{11}/7$ is the object that puts matter on a different cone from light, and it is exactly the assignment canon's own quality record grades as soft. `manuscript/ave-kb/vol3/claim-quality.md`:1158 verbatim:

> *"The single soft joint is the coupling-selection step (massive packet → scalar $1/7$ bulk only; photon → transverse $2/7$ sector only), asserted by mechanical analogy rather than derived from a wave-equation projection."*

and its own strengthen-by, `:1160`:

> *"Derive the coupling selection (matter→scalar-bulk, light→transverse-shear) from a wave-equation projection of the massive vs massless dispersion onto the Cosserat strain tensor, replacing the mechanical-analogy assertion."*

> ### **You are not missing a mechanism; you are missing a derivation of a coupling you asserted.**
> The repair does not require a new axiom, a new sector, a new field or a new constant. It requires that the strengthen-by written at `claim-quality.md`:1160 in the framework's own hand be carried out — and it requires being willing to lose the $2:1$ *matter-vs-light* deflection ratio, which is what the two-cone assignment buys.

### §7.3 — What the repair costs

Stated plainly, because a repair whose cost is not stated is a rescue:

- **The Double Deflection loses its headline framing.** `double-deflection.md`:39-46 sells $\delta_{light}/\delta_{matter} = (2/7)/(1/7) = 2$ with $\delta_{matter} = 2GM/(bc^2)$ **"(Newton / Soldner 1801)"**. On one cone there is no such ratio: a relativistic massive particle grazing the Sun deflects by the *same* $4GM/bc^2$ as light in the $v\to c$ limit, and the $2:1$ ratio is recovered only against the *non-relativistic* Newtonian corpuscle, which is a statement about $v \ll c$ rather than about two coupling channels.
- **The $1/7$ isotropic projection loses its consumer.** Its only PPN-facing role is $n_{scalar}$. It may well survive elsewhere (it is also the $7$ in $G = \hbar c/7\xi m_e^2$), but the deflection-ratio consumer goes.
- **It does not, by itself, make anything emergence-class.** Restoring $\Omega^2$ makes AVE agree with GR; §6's verdict on the light sector is unchanged and would extend to the matter sector. **The repair buys correctness, not distinctness.**

**This lane does not perform the repair and takes no position on whether Grant wants it.** It is named because §0 would be dishonest without stating that the defect is local and cheap rather than structural and fatal.

## §8 — Two things logged for months and never named

Neither of these is a new observation. Both were written into the tree, correctly, by earlier lanes — and neither was ever named as the thing it is.

### §8.1 — The $\gamma$ deficit was written down on 2026-05-17

`research/2026-05-17_hulse-taylor-substrate-native-derivation-sketch.md`:49, verbatim:

> ⚠️ **Rigor-pass annotation #1**: the angular momentum modification factor $(1 + \phi/c^2)$ is the AVE Gordon-form's specific structural prediction. In GR Schwarzschild isotropic coordinates, the corresponding factor is $(1 + GM/2c^2r)^4 / (1 - GM/2c^2r)^2 \approx 1 + 3GM/c^2r$ at leading order (cubed factor from spatial metric). **The factor 1 (AVE) vs factor 3 (Schwarzschild) difference at leading order is the substrate-vs-GR structural difference.**

That factor is $1 + (1+2\gamma)U$ — the product of the lapse factor $(1+U)$ and the spatial factor $(1+2\gamma U)$. **AVE's "1" is $\gamma = 0$; Schwarzschild's "3" is $\gamma = 1$.** The annotation is the $\gamma$ deficit, correctly derived, correctly flagged as *"the substrate-vs-GR structural difference"* — and then not costed. The same document's `:80` says why:

> ⚠️ **Rigor-pass annotation #2**: a full PPN-1 comparison requires deriving the substrate-native equivalent of GR's spatial-metric contribution to the orbit. … **This is the load-bearing computation that's been deferred for rigor pass.**

**The deferred computation is the one performed in §2.** The reason the deferral looked cheap is `:73`, which observed that the $-GML^2/(mc^2r^3)$ coefficient is $1$ in both — true, and not sufficient: the $L_z$-modification factor at `:49` enters the *same* orbit integral, and it is where the $\gamma$ term lives. The document's own two annotations, read together, already contain the result. Fifteen months.


#### §8.1a — Why the sketch's "coefficient 1 in both ✓" did not catch it — VERIFIED, and one part NOT verified

The sketch's own Lagrangian at `:33`, $L_{test} = -mc^2\sqrt{1-n_{scalar}^2v^2/c^2}\,/\,n_{scalar}$, **is** the geodesic Lagrangian of the Gordon scalar metric $ds^2 = -c^2dt^2/n^2 + d\mathbf{x}^2$ — confirmed by direct construction. So the sketch and §2 are describing the same dynamics, and they reach opposite conclusions. Two defects were found, and they are reported at different confidence.

**(i) A chart-slot mismatch — VERIFIED, and it is the substantive one.** Writing the orbit equation as $(du/d\varphi)^2 = c_0 + c_1u + c_2u^2 + c_3u^3$, sympy returns, exactly:

| chart | $c_2$ | $c_3$ | where the precession lives |
|---|---|---|---|
| **Gordon / AVE**, $A = 1/n^2$, $B=1$ | $E^2m^2/L^2 - 1$ | $\mathbf{0}$ | entirely in $c_2$: $\delta = m/\ell_p \Rightarrow \Delta\phi = \pi m/\ell_p$ |
| **Schwarzschild, areal** | $\mathbf{-1}$ *(exactly)* | $2m$ | entirely in $c_3$: $\Delta\phi = 3\pi c_3/\ell_p = 6\pi m/\ell_p$ |
| **Schwarzschild, isotropic** | $-1 + 6m^2/L^2$ | $O(m^3/L^2)$, negligible | entirely in $c_2$: $\delta = 6m/\ell_p \Rightarrow 6\pi m/\ell_p$ |

**In the Gordon chart the $u^3$ slot is empty and the $u^2$ slot carries everything; in the areal chart it is exactly the other way round.** The sketch matched its own chart's $1/r^3$ term against the *areal* textbook $V_{eff}^{Schw}$ (`:71`) and concluded *"coefficient **1** in both ✓"* (`:73`). It matched **the slot that carries nothing in its chart against the slot that carries everything in the other**, and never compared the $u^2$ coefficients — which is where its own theory's entire precession sits. The two-chart comparison is the error; there is no disagreement about the textbook Schwarzschild value.

**(ii) An arithmetic slip at `:37` — VERIFIED, but not load-bearing.** The weak-field expansion of that same Lagrangian, taken jointly in $\phi/c^2$ and $v^2/c^2$ at virial order, returns

$$L \approx m\left(-c^2 + \phi + \frac{v^2}{2} - \frac{\phi^2}{c^2} + \frac{\phi v^2}{2c^2} + \frac{v^4}{8c^2}\right),$$

with the $\phi^2/c^2$ coefficient $\mathbf{-1}$. The sketch's `:37` writes $-\tfrac12$. The $\phi v^2/2c^2$ and $v^4/8c^2$ terms match. **Recorded as a numeric discrepancy in a document its own header grades `Status: SKETCHED, not rigorous` (`:7`) — not as an accusation against ratified canon**, and the verdict does not rest on it: §9's geodesic integration never uses that expansion.

> **⚠ WHAT I COULD NOT VERIFY.** The commissioning amendment stated this defect as *"its 'coefficient is 1' reads $q/2 = 1/2$ in its own chart where GR reads $3/2$."* **I could not reproduce the numerals $1/2$ and $3/2$** under any normalisation I tried, so **this document does not carry them.** What is carried is the table above, which is exact and reproducible. If the $1/2$-vs-$3/2$ reading is the sibling lane's own and is sound in its own normalisation, it belongs in that lane's document, not restated here on trust.

### §8.2 — The $\beta$ question was written down on 2026-08-11

`research/2026-08-11_gravity-linearity-audit_result.md`:432, verbatim:

> | **R13** | site 15 vs lapse: **same** leading term `ε₁₁/7`, **different** functions — `C₃ − C₁ = −3ε₁₁²/98 ≠ 0`. Distinct clocks, not one clock twice. …

That residual is not a curiosity. With $U = \varepsilon_{11}/7$:

$$\frac{3\varepsilon_{11}^2}{98} \;=\; \frac{3}{2}\cdot\frac{\varepsilon_{11}^2}{49} \;=\; \frac{3}{2}U^2 \quad\textbf{exactly}$$

(verified symbolically; `match: True`). And $\tfrac32 U^2$ is $\beta U^2$ at $\beta = 3/2$. **The unexplained residual IS the $\beta$ question**, written in a different variable.

The two candidate clocks the audit was choosing between are the two candidate $\beta$'s:

| candidate clock | $-g_{00}$ | $\beta$ |
|---|---|---|
| $C_1 = 1/(1+U)$ — the ponderomotive / index clock | $1-2U+3U^2$ | $\mathbf{3/2}$ |
| $C_3 = \sqrt{1-2U}$ — the lapse clock as canon writes it | $1-2U$ | $\mathbf{0}$ |
| GR | $1-2U+2U^2$ | $1$ |

**GR sits precisely between AVE's two candidate clocks and equals neither.** The audit's §7 stuck-point — *"Is the gravitational clock a MODULUS effect or a BIAS-POINT effect?"* (`:566`) — is, in PPN coordinates, *"is $\beta$ equal to $3/2$ or to $0$?"*, and the answer observation gives is *neither*.

That reframing does **not** resolve the stuck-point; §7 of that audit correctly refused to pick, and this lane does not pick either. What it does is tell the stuck-point what it costs: **both branches of a two-way fork fail LLR**, one at $4.5\times10^3\sigma$ and the other at $9.1\times10^3\sigma$. A fork whose two arms both miss by thousands of sigma is not a fork about which arm is right; it is evidence that the object being forked over — a single scalar clock with no spatial partner — is the wrong shape. Which is §7.

## §9 — Independent cross-check: direct geodesic integration

The PPN algebra of §2 is a series expansion. A series expansion can be right about the coefficients and wrong about the observable if the coefficients were read off in the wrong gauge. So the perihelion factor was **also** obtained by direct orbit integration, with a GR control.

### §9.1 — Method

For a static isotropic metric $ds^2 = -A(R)c^2dt^2 + B(R)(dR^2+R^2d\Omega^2)$, a timelike equatorial geodesic with $u = 1/R$ obeys

$$\left(\frac{du}{d\varphi}\right)^2 \;=\; f(u) \;\equiv\; \frac{B(u)}{L^2}\!\left(\frac{E^2}{A(u)} - 1\right) - u^2 ,$$

with $E^2$ and $L^2$ fixed **linearly** by requiring $f(u_1) = f(u_2) = 0$ at the chosen apsides. The apsidal angle is $\Phi = \int_{u_1}^{u_2} du/\sqrt{f(u)}$ and the precession per orbit is $2\Phi - 2\pi$. The endpoint inverse-square-root singularities are removed exactly by $u = \bar u + \Delta u\sin\psi$, which turns $(u-u_1)(u_2-u)$ into $\Delta u^2\cos^2\psi$.

**Two implementation notes, because they were both failure modes here:**

1. **float64 is not enough.** At $x = m/p \sim 10^{-6}$, $f(u)$ is a difference of $O(1)$ quantities whose result is $O(10^{-12})$; the first attempt returned `nan` for every model including the GR control. Run at `mpmath.mp.dps = 60`.
2. **The quadrature must not sample the endpoints.** Tanh-sinh (`mp.quad`) evaluates at $\psi = \pm\pi/2$ exactly and divides by zero on the removable singularity. Gauss-Legendre (`mp.quadgl`) never does.

Both are reported because a reader who reruns this with `numpy` and `scipy.quad` will get `nan` and conclude the metric is pathological. It is not; the integrator was.

### §9.2 — Results

Eccentricity $0.2$; $x \equiv m/p$ with $p$ the semi-latus rectum; ratio is to the **GR baseline** $6\pi x$.

| metric | $x$ | precession/orbit [rad] | $\div\,6\pi x$ | PPN prediction |
|---|---|---|---|---|
| **GR isotropic Schwarzschild** *(CONTROL)* | $8.333\times10^{-6}$ | $1.57084175053\times10^{-4}$ | $1.000028918$ | $1$ |
| **GR isotropic Schwarzschild** *(CONTROL)* | $8.333\times10^{-7}$ | $1.57080086903\times10^{-5}$ | $1.000002892$ | $1$ |
| **GR isotropic Schwarzschild** *(CONTROL)* | $8.333\times10^{-8}$ | $1.57079678102\times10^{-6}$ | $1.000000289$ | $1$ |
| GR PPN form $(\gamma{=}\beta{=}1)$ | $8.333\times10^{-8}$ | $1.57079651791\times10^{-6}$ | $1.000000122$ | $1$ |
| **AVE matter** $g_{00}{=}-1/(1{+}U)^2$, $g_{ij}{=}\delta$ | $8.333\times10^{-6}$ | $2.61798842386\times10^{-5}$ | $\mathbf{0.1666663194}$ | $1/6 = 0.1\overline{6}$ |
| **AVE matter** | $8.333\times10^{-7}$ | $2.61799333258\times10^{-6}$ | $\mathbf{0.1666666319}$ | $1/6$ |
| **AVE matter** | $8.333\times10^{-8}$ | $2.61799382345\times10^{-7}$ | $\mathbf{0.1666666632}$ | $1/6$ |
| AVE alt-clock $g_{00}{=}-(1{-}2U)$, $g_{ij}{=}\delta$ | $8.333\times10^{-8}$ | $1.04719798753\times10^{-6}$ | $0.6666669444$ | $2/3$ |

Every row converges to its PPN prediction as $x\to0$ with residual $\propto x$, which is the expected $O(U^2)$ PPN-2 contamination and is the same size on the control as on the AVE rows.

### §9.3 — Why the control is the point

**`UNRUN ≠ PASSED`, and `NO-CONTROL ≠ MEASURED`.** An integrator that returns $1/6$ on the AVE metric proves nothing on its own — it could be an integrator that returns $1/6$ on everything. The GR row is the same code, the same quadrature, the same precision, the same apsides, changing only $A(R)$ and $B(R)$, and it returns the textbook $6\pi x$ to $2.9\times10^{-7}$ relative. **The fourth row is a second control**: the PPN-form metric $(1-2U+2U^2,\,1+2U)$ truncated at $O(U^2)$ also returns $1$, confirming the reader is a PPN reader and not a Schwarzschild reader.

The alt-clock row is a **planted-defect positive control**: it is a metric with a *different* known $(\beta,\gamma) = (0,0)$, and the integrator returns its $F = 2/3$ rather than either $1$ or $1/6$. The instrument discriminates.

### §9.4 — Reproduction

Self-contained; no repository imports, no engine, ~2 s.

```python
import mpmath as mp
mp.mp.dps = 60

def AB(model):
    if model == "GR_isotropic":  # CONTROL
        return (lambda u: ((1-u/2)/(1+u/2))**2, lambda u: (1+u/2)**4)
    if model == "AVE_matter":    # Gordon: g00 = -1/n^2, g_ij = delta, n = 1+u
        return (lambda u: 1/(1+u)**2, lambda u: mp.mpf(1))
    raise ValueError(model)

def precession(model, u1, u2):
    A, B = AB(model)                       # units G = M = c = 1
    sol = mp.lu_solve(mp.matrix([[B(u1)/A(u1), -u1**2],
                                 [B(u2)/A(u2), -u2**2]]), mp.matrix([B(u1), B(u2)]))
    X, Y = sol[0], sol[1]                  # X = E^2, Y = L^2
    f = lambda u: (B(u)/Y)*(X/A(u) - 1) - u**2
    g = lambda u: f(u)/((u-u1)*(u2-u))     # removable at both endpoints
    um, du = (u1+u2)/2, (u2-u1)/2
    val = mp.quadgl(lambda s: 1/mp.sqrt(g(um + du*mp.sin(s))),
                    [-mp.pi/2, 0, mp.pi/2], maxdegree=8)
    return 2*val - 2*mp.pi

rp, ecc = mp.mpf("1e7"), mp.mpf("0.2")
a = rp/(1-ecc); u2 = 1/rp; u1 = 1/(a*(1+ecc)); x = 1/(a*(1-ecc**2))
for m in ["GR_isotropic", "AVE_matter"]:
    print(m, mp.nstr(precession(m, u1, u2)/(6*mp.pi*x), 10))
# GR_isotropic 1.000000289
# AVE_matter   0.1666666632
```

## §10 — METHOD, and its blind spots

Every enumeration in this document — §4's four objects, §11's cite ledger, §12's flags, and the walk-back list in the routed open item — is **a statement about the searches and reads performed by this lane, not a statement about the corpus.** This section says what those were so a reader can judge the gap.

### §10.1 — What was read

Twenty-eight files were opened. Of those, twenty were read end to end: the eleven `vol3/gravity` KB leaves under `ch01-gravity-yield` and `ch02`/`ch03` that carry $\varepsilon_{11}$ or a refractive index, `manuscript/common_equations/eq_axiom_5.tex`, `anomalous-perihelion-advance.md`, `ponderomotive-equivalence.md`, and the four research docs named in the header. Eight were read only in the neighbourhoods returned by search: `manuscript/ave-kb/vol3/claim-quality.md` (two claim blocks), `manuscript/ave-kb/common/operators.md` (the operator table), `src/scripts/verify/gravity_ppn_coherence.py` (three regions), `manuscript/common_equations/eq_gravity_derived.tex` (first 80 lines), `manuscript/vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex` (the precession section), `manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex` (the index section), `manuscript/consistency-manifest.yaml` (the P10 entry), and `LIVING_REFERENCE.md` (the pitfall table).

### §10.2 — What was searched, and with what

Search patterns run across `manuscript/`, `research/`, `_orchestration/`, `src/`, `README.md` and `LIVING_REFERENCE.md`:
`IDENTICAL to GR Schwarzschild` · `derivation gap CLOSED` · `identical to GR` · `identical result obtained by General Relativity` · `Exact match with GR` · `recovered exactly` · `substrate-native at leading PPN-1` · `gives 3 exactly` · `\beta = \gamma = 1` · `4.226` · `42.98` · `43''` · `arcseconds per century` · `n_scalar` / `n_{scalar}` · `ponderomotive` (case-insensitive) · `clm-zf8eah` · `clm-qyn8t0` · `11/7` · `9/7` · `3/7` · `2/7` · `1/7` · `7 = 2/\nu_{vac}` · `r_sat = 7GM`.

### §10.3 — ★ A measured tool hazard, and the second method

**The session's `grep` is a wrapper around `ugrep` invoked with `--ignore-files`**, which honours ignore-file rules, and its `--include=*.md` handling emitted `No such file or directory` warnings on this tree. Both are false-negative generators.

**So every enumeration below was re-run under `/usr/bin/grep`, a different binary with different ignore semantics.** Where the two agreed the count is reported; where a claim is "absent", a *second, non-grep* method was used as well:

| claim | method 1 | method 2 | agree? |
|---|---|---|---|
| `IDENTICAL to GR Schwarzschild` appears at 3 places | wrapper `grep -rn` | `/usr/bin/grep -rn` | ✅ same 3 |
| the ponderomotive $1/7$ matter index is **absent** from the 2026-06-05 PPN audit and its prereg | `/usr/bin/grep` for `1/7`, `ponderomotive`, `n_scalar`, `scalar index` → exit 1 on both files | **read** the audit's §1, which enumerates its structure list as S1–S4 and names each; the $1/7$ matter index is not among the four | ✅ |
| the same index is absent from `gravity_ppn_coherence.py` | `grep -n "scalar\|1/7\|ponderomotive\|Rational(1"` → no hits | enumerate **every** `sp.Rational(` call in the file: `Rational(2,7)`, `Rational(9,7)`, `Rational(ns,nt)`, `Rational(9,2)` — and read the module docstring, which declares *"two refractive indices"* | ✅ |

### §10.4 — Blind spots, named

1. **This is a search, not a census.** No end-to-end read of `manuscript/` was performed. Sites that state the perihelion/deflection claim in wording none of §10.2's patterns match are **not** covered — and the open-items README's own measured lesson applies here: *"Items that announce themselves are the ones already tracked."* A site that says "AVE recovers the observed precession" without any of my tokens is invisible to this method.
2. **Line-wrapped phrases.** Several of the patterns are long. A site that breaks `IDENTICAL to GR Schwarzschild` across a line would not match either grep. No wrap-tolerant (whitespace-normalising) pass was run.
3. **Rendered PDF / figure text / notebook outputs** were not searched at all.
4. **Downstream repositories.** Only `AVE-Core` was searched. Whether the claim propagated into other workspace repos is **unknown to this lane**.
5. **The matter-sector result is conditional on M4** (`§1.3`), the assignment that a massive body moves on the Gordon metric built from $n_{scalar}$. That assignment is canon's, and it is graded soft by canon. If Grant rules it wrong, §0's matter rows are void — which is the *point* of §7, not a hedge against it.
6. **No engine ran.** Nothing here is an empirical result about the lattice. `substrate-native-check` was fired (§13) and returned "no solver to scaffold"; the numerical work is quadrature on written metrics.
7. **The external data are not re-derived and not re-fetched.** Cassini, LLR, the Mercury residual and the Hulse-Taylor rate are carried forward from the commissioning reconciliation and from the tree; see §11 rows U1–U4.

## §11 — Cite verification ledger

**Provenance honesty.** The reconciliation that commissioned this document did **not** re-verify its four source lanes' `file:line` citations. Every cite carried forward was therefore re-opened on this branch at `a3f4fef7`. This table is the receipt.

### §11.1 — Verified on this branch (opened, read, content matches the cited line)

| # | cite | what it carries |
|---|---|---|
| C1 | `manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/gordon-optical-metric.md`:12, :17, :20, :25, :33 | Gordon-as-historical-import; the metric form; *"1D principal radial polarisation strain"*; the scalar Poisson equation; $\varepsilon_{11}=7GM/c^2r$ |
| C2 | `manuscript/common_equations/eq_axiom_5.tex`:45, :73, :75, :76, :127-135, :145-149 | THE BIAS naming; bound-sector potential; $\mathbf u_0=-\mathcal A_g\nabla\varepsilon_{11}$; clause-G elliptic law with $\kappa=c^4/7G$; POSTULATED grade + *"kappa = c^4/7G and nu = 2/7 stay GR-imported"*; the non-circularity observation |
| C3 | `manuscript/ave-kb/common/operators.md`:59 | Op19 $n(r)=1+\nu_{vac}\varepsilon_{11}$, status **CANONICAL**, $\nu_{vac}=2/7$ |
| C4 | `manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/ponderomotive-equivalence.md`:14, :19 | $n_{scalar}(r)=1+\epsilon_{11}/7=1+GM/c^2r$ via *"the $1/7$ Lagrangian isotropic projection"*; $U_{wave}=m_ic^2/n_{scalar}$ |
| C5 | `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/one-seventh-impedance-projection.md`:13, :18 | $\frac13\theta=\frac13(\frac37\epsilon_{11})\equiv\frac17\epsilon_{11}$; the GR-imported provenance note |
| C6 | `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/vacuum-poisson-ratio.md`:13 | $\nu_{vac}=\frac{3K-2G}{2(3K+G)}=\frac{4}{14}=\frac27$ |
| C7 | `7 = 2/\nu_{vac}` at **five line-hits across four files**: `manuscript/ave-kb/vol3/claim-quality.md`:1131 · `…/vol3/gravity/ch03-macroscopic-relativity/dielectric-rupture-event-horizon.md`:34 · `…/vol3/cosmology/ch15-black-hole-orbitals/lattice-extreme-bh-rationality.md`:99 · `…/vol3/cosmology/ch15-black-hole-orbitals/ave-bh-horizon-area-theorem.md`:20 and :35 | the $7$ is $\nu_{vac}$ inverted and doubled, not an independent constant. *(Found by pattern search; §10.4 blind spots apply — this is five hits my patterns reached, not a census.)* |
| C8 | `manuscript/ave-kb/vol3/claim-quality.md`:1141, :1143-1146, :1149, :1158, :1160 | clm-zf8eah body, the *"asserted by **mechanical analogy**"* non-claim, the identical rationale sentence, and the strengthen-by that names the missing derivation |
| C9 | `manuscript/ave-kb/vol3/gravity/ch02-general-relativity/double-deflection.md`:22, :24, :28, :39, :42, :44-46 | the two indices over $\chi_{vol}$; the *"isotropic spherical bulk tensor $\frac13\theta\delta_{ij}$"* sentence; $\chi_{vol}=7GM/c^2r$; Soldner/Einstein values |
| C10 | `manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex`:183-206 | the manuscript twin of C9 — **confirms the 2026-06-05 audit's S2 cite `:185-206` resolves correctly** |
| C11 | `manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/anomalous-perihelion-advance.md`:10, :20, :44 | the two identical closure paragraphs and *"the identical result obtained by General Relativity"* |
| C12 | `manuscript/vol_3_macroscopic/chapters/14_macroscopic_orbital_mechanics.tex`:23, :70-72, :81 | regime-table row; the provenance warningbox asserting $\beta=\gamma=1$; the $43''$ paragraph |
| C13 | `research/2026-05-17_hulse-taylor-substrate-native-derivation-sketch.md`:7, :33, :49, :73, :80, :93, :99 | `Status: SKETCHED, not rigorous`; the ponderomotive Lagrangian; annotation #1 (factor 1 vs 3); the coefficient-1 observation; annotation #2 (the deferred computation) |
| C14 | `research/2026-05-17_hulse-taylor-substrate-native-derivation-result.md`:143, :145, :151 | the **Outcome C** finding: recovery *"structurally limited to OPTICS"*, mechanics *"asserted-via-borrowing, not derived"* |
| C15 | `research/2026-08-11_gravity-linearity-audit_result.md`:432, :504-507, :566 | R13's $-3\varepsilon_{11}^2/98$; the four-clock table incl. the site-15 ponderomotive row; the MODULUS-vs-BIAS-POINT question |
| C16 | `research/2026-06-05_gravity-ppn-coherence-result.md`:16, :18-35, :41, :69, :151 | *"touches **four** … statements"* + the S1–S4 list; the $\delta=2K\,GM/bc^2$ kernel; *"No canonical AVE statement derives β"*; the kernel-normalization caveat |
| C17 | `src/scripts/verify/gravity_ppn_coherence.py`:142, :145-200, :349, :351, :367 | $F=(2-\beta+2\gamma)/3$; the *"two refractive indices"* docstring; the `beta=1` comment and the two `sp.Integer(1)` pins |
| C18 | `manuscript/ave-kb/vol4/falsification/ch11-experimental-bench-falsification/geo-synchronous-impedance.md`:20 | canon's own statement of the $7\times\frac27$ cancellation |
| C19 | `manuscript/common_equations/eq_gravity_derived.tex`:20, :26, :50-56, :72-77 | $G=\hbar c/7\xi m_e^2$; $n(r)=1+2GM/rc^2$; the $(2/7,9/7)$ decomposition; the W1 walk-back comment |
| C20 | `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/temporal-spatial-lattice-decomposition.md`:14, :19, :26 | *"The principal radial strain"*; $n_{spatial}$; the W1 walk-back |
| C21 | `manuscript/ave-kb/vol3/gravity/ch03-macroscopic-relativity/transverse-refractive-index.md`:14, :16, :23 | principal radial tensile strain; $h_\perp=-\nu_{vac}\epsilon_{11}$ |
| C22 | `manuscript/ave-kb/vol3/gravity/ch01-gravity-yield/gravitational-coupling-constant.md`:10 | the $G$-ruling: form-derived, value calibrated; *"the $1/7$ trace-reversed bulk projection"* |
| C23 | `manuscript/consistency-manifest.yaml`:649-663 | P10 `type: consistency_check`, `error_percent: 0.03`, and the note naming the $1/7$ matter coupling |
| C24 | `manuscript/ave-kb/vol3/claim-quality.md`:287-310 | clm-qyn8t0: *"identical to GR"*, and the rationale claiming the `"3"` recovered exactly |
| C25 | `manuscript/ave-kb/claim-quality-closure-roadmap.md`:205 | the Foundation-Item-5 changelog entry |
| C26 | `manuscript/ave-kb/vol3/cosmology/ch14-orbital-mechanics/orbital-regime-table.md`:16 | *"Exact match with GR"* |
| C27 | `LIVING_REFERENCE.md`:162 · `manuscript/ave-kb/vol3/claim-quality.md`:48 | the $11/7$ *"full lattice density"* |
| C28 | `manuscript/ave-kb/common/full-derivation-chain.md`:370 | $\sqrt{3/7}=\sqrt{1-2\nu_{vac}}$, the dilatational signature — corroborates $\theta=\frac37\varepsilon_{11}$ |
| C29 | `src/ave/core/constants.py`:132 · `src/ave/gravity/solar_impedance.py`:68 | `M_SUN = 1.989e30`; `R_SUN = 6.957e8` |
| C30 | `research/2026-07-20_q1-pulsar-hardening.md`:84 | *"The corpus already claims GR-consistency for periastron advance (the ponderomotive `n_scalar` derivation, structurally identical to GR)"* |

### §11.2 — ⚠ Cites and numbers I could NOT confirm

| # | item | status |
|---|---|---|
| **U1** | **Cassini $\gamma-1 = (2.1\pm2.3)\times10^{-5}$** | **NOT IN TREE as a PPN bound.** Searched `bertotti`, `tortora`, `iess`, `cassini` (excluding the ring-division and flyby uses): the only Bertotti–Iess–Tortora reference is `research/2026-07-20_scalar-gw-bulk-channel_derivation.md`:115, and it cites Cassini for the **Brans-Dicke $\omega_{BD}>4\times10^4$** bound, not for $\gamma$. Carried from the commissioning reconciliation. **Not re-fetched by this lane.** |
| **U2** | **LLR $\lvert\beta-1\rvert\lesssim1.1\times10^{-4}$** | **NOT IN TREE.** `lunar laser` returns one hit, `…-derivation-result.md`:143, which names LLR as a *test class*, not a bound. Carried from the commissioning reconciliation. **Not re-fetched.** |
| **U3** | **Mercury residual $42.98\pm0.04$ arcsec/century** | the $42.98$ appears in-tree at `research/2026-06-05_gravity-ppn-coherence-result.md`:67; **the $\pm0.04$ uncertainty does not.** Carried. The $895\sigma$ therefore inherits an unverified error bar — the *ratio* $6\times$ does not. |
| **U4** | **Hulse-Taylor $\dot\omega = 4.226595(5)^\circ$/yr** | in-tree at `…-sketch.md`:140 and :169; the external primary source was **not re-fetched**. |
| **U5** | **the handed-down $1.7516''$** | **could not be reproduced from any in-tree constant set.** Nearest is $1.751640''$ at $M_\odot=1.98892\times10^{30}$; in-tree `M_SUN` gives $1.751710''$ and IAU $GM_\odot$ gives $1.751190''$. This document quotes $\mathbf{1.7517''}$ and shows the spread (§6.3) rather than adopting a figure it cannot source. |
| **U6** | **the handed-down $7.163''$/century** | reproduces at $7.1634''$ **only** with IAU nominal $GM_\odot$; the in-tree `M_SUN`/`G` pair gives $7.1656''$. Both are reported in §6.3. |
| **U7** | `research/2026-07-20_q1-pulsar-hardening.md`:84 cites `claim-quality-closure-roadmap.md`**:204** | **stale by one line.** `:204` is blank at HEAD; the Foundation-Item-5 content it points at is `:205`. Pure line-drift, content correct at the real site. Recorded, not fixed. |
| **U8** | *"at least four canonical sites"* claiming coefficient-1 closure | I found the claim at **more than four** places and enumerate what I found in the routed open item. I do not know whether that enumeration is complete; §10.4 states why. |

## §12 — Flags surfaced (NOT fixed by this lane)

**Nothing in `manuscript/`, `src/` or any prior research doc was edited by this lane.** Flag-don't-fix throughout; two items are routed as open-item files, the rest are recorded here.

| # | flag | route |
|---|---|---|
| **F1 ★** | **The matter-sector walk-backs.** Multiple canonical and research sites state that the perihelion derivation gap is CLOSED and that AVE's coefficient is *"1, IDENTICAL to GR Schwarzschild"*. Under §2 they are wrong by $6\times$. **Do not edit them.** Full enumeration with verbatim text in the routed item. | `_orchestration/open-items/2026-08-27-ppn-matter-sector-walkback.md` → **Grant** |
| **F2 ★** | **`\varepsilon_{11}` is four objects** (§4), and Op19 applies an elastic Poisson contraction to an object R55 declares is not an elastic strain. | `_orchestration/open-items/2026-08-27-eps11-four-objects.md` → **Grant** |
| **F3** | **The 2026-06-05 PPN audit's $\beta$ statement is scope-limited and reads as general.** `research/2026-06-05_gravity-ppn-coherence-result.md`:69 verbatim: *"**The metric does NOT independently fix β.** No canonical AVE statement derives β"*, and `src/scripts/verify/gravity_ppn_coherence.py`:349 pins $\beta$ by hand under the comment *"the standard PPN beta=1 (no canonical AVE statement sets beta independently)"*. **True of the pair the audit examined; false once the ponderomotive matter index is in scope.** That index sets $\beta=3/2$ (§2.2), and the audit's structure list (S1–S4, `:16-35`) does not contain it — verified two ways (§10.3). The audit is not wrong about what it examined; its **scope statement** is broader than its **structure list**. | auditor lane — the audit is frozen-class; a dated surface-note, never a rewrite |
| **F4** | **The instrument would return the right answer today.** `gravity_ppn_coherence.py` already ships $F=(2-\beta+2\gamma)/3$ at `:142`. Adding a third scenario row with $(\gamma,\beta)=(0,3/2)$ from `ponderomotive-equivalence.md`:14 is a few lines and returns $1/6$. **This lane did not add it** — touching a merged verify script that `make verify` consumes is not an implementer-lane call on a research branch. | orchestrator / auditor lane |
| **F5** | **The correct finding is already in the tree and was superseded by a sketch.** `research/2026-05-17_hulse-taylor-substrate-native-derivation-result.md`:143 verbatim: *"The framework's PPN-1 weak-field gravity recovery via Gordon optical-metric isomorphism is **structurally limited to OPTICS** (light propagation); for MECHANICS (massive-particle orbital dynamics), the substrate-native PPN-1 coefficient **has NOT been derived**"*, and `:145`: *"The mechanics-sector PPN-1 recovery is currently **asserted-via-borrowing, not derived**."* That Outcome-C result was superseded **the same night** by `…-sketch.md`, whose own header at `:7` reads `**Status**: SKETCHED, not rigorous` and whose annotations `:49` and `:80` contain the counter-evidence. **§2 re-derives Outcome C's conclusion and sharpens it from "not derived" to "derived, and it is $1/6$."** | **Grant** — this is a substitution-not-retraction question about which of two 2026-05-17 documents is standing |
| **F6** | **`LIVING_REFERENCE.md`:162 carries a statement W1 walked back on 2026-06-05.** Verbatim at HEAD: *"Spatial part (9/7)ε₁₁ → light deflection only"*. The W1 walk-back landed in `temporal-spatial-lattice-decomposition.md`:26 and in `eq_gravity_derived.tex`:72-77 but **not** here. Unrelated to the PPN result; found while enumerating the $/7$ family. | auditor lane — stale-propagation repair |
| **F7** | **A factor of 2 in the Gordon lensing index's argument, at two sites.** `manuscript/ave-kb/common/translation-tables/translation-gravity.md`:23 and `manuscript/vol_3_macroscopic/chapters/02_general_relativity_and_gravity.tex`:137 both write $n(r)=(1+r_s/2r)^3/(1-r_s/2r)$, and `:140` places the pole at $r\to r_s/2$. The isotropic-Schwarzschild optical index is $n_{opt}=(1+m/2R)^3/(1-m/2R)$ with $m=GM/c^2=r_s/2$, so its pole is the isotropic horizon $R=m/2=r_s/4$ and its weak-field slope is **2**, not 4. **This matters because the audit's own §7 caveat is downstream of it**: `research/2026-06-05_gravity-ppn-coherence-result.md`:151 explains away the resulting slope-4 by saying the full index *"must be used with the relativistic photon-orbit kernel"*. With the correct argument no such special kernel is needed — $n_{opt}$ has slope 2, the same Snell kernel gives $4GM/bc^2$, and $n_{opt}\equiv n_\perp$ at weak field, which is a *tighter* coherence than the audit could report. **⚑ Flagged, not fixed, and stated as a candidate**: I verified the algebra, not the intended convention, and a convention in which $r_s$ denotes $GM/c^2$ would make the sites correct as written. | auditor lane / **Grant** |
| **F8** | **The Soldner cost is not currently disclosed anywhere I read.** `double-deflection.md`:44 and `02_general_relativity_and_gravity.tex`:202 present $\delta_{matter}=2GM/(bc^2)$ *"(Newton / Soldner 1801)"* as a derived AVE result. It is the $\gamma=0$ matter sector, stated as a feature. Whatever Grant rules on F1, the *relationship* between the Double Deflection's $2{:}1$ ratio and the matter sector's PPN failure should be stated at one of those sites, because they are the same fact. | routed inside the F1 open item |
| **F10** | **The repair exists, and the walk-back debt does not shrink.** The sibling branch `research/2026-08-27-two-knob-gravity-repair` reaches GR at $O(m)$ with $(a_1,b_1,b_2)=(2,1,\tfrac12)$. **The canonical sites in F1 are wrong under BOTH readings** — under the old one because $\gamma=0$, under the new one because they claim a *derivation* of a coefficient the repair shows is currently *chosen*. If anything the repair sharpens the debt: the sites assert closure, and what exists is an admissible parameter point whose forcing is open. **Grant's ruling on F1 should be taken with the repair in view, not instead of it.** | folded into the F1 open item |
| **F11** | **Two defects verified in `…-sketch.md`, reported at sketch grade.** The chart-slot mismatch (§8.1a(i)) and the $\phi^2/c^2$ coefficient at `:37` (§8.1a(ii)). That document self-grades `Status: SKETCHED, not rigorous` at `:7`, so these are **not** accusations against ratified canon — but four canonical sites and one changelog entry (F1) rest on its conclusion, which is the reason they are recorded at all. **The numeral pair $q/2=1/2$ vs $3/2$ offered by the commissioning amendment is NOT carried** — see the box at the end of §8.1a. | **Grant**, inside F1/F5 |
| **F9** | **Partial reproduction of a handed-down argument.** The *"the /7 family is gauge at PPN order"* phrasing reproduces on its Jacobian half ($dR/dr=1$ at $O(m)$, exact) and not on its inference half (a graded $g_{ij}$ gives $\gamma=7\kappa/2\neq0$). Recorded in §5.3; the conclusion is re-derived on different and stronger grounds and does not depend on the disputed step. | recorded; no action proposed |

## §13 — Skill-selection retro-pass

| skill | fired | where |
|---|---|---|
| `substrate-native-check` | ✅ | walked before any numerical work. **Returned "no solver to scaffold"** — this lane writes no operator, observer or eigsolver. The checkpoint that did bite is the K4/Cosserat one: it is what surfaced that $\varepsilon_{11}$'s ontology (§4) is unsettled *before* the elastic-repair attempt, which is why §3 tested the Navier solution space rather than assuming a strain |
| `pre-test-physics-check` | ✅ | the plumber-physical question surfaced to Grant is §2.5's: *does the substrate's series impedance and its shunt impedance grade together under gravity, or by a factor of two?* That is $\gamma$, in EE terms, and it is routed inside the F1 item |
| `phase-space-coordinate-check` | ✅ | the corpus claim is in real-space orbital coordinates and the test is in real-space orbital coordinates. The **gauge** analogue of the check is what §0's coordinate declaration and §9's control exist for: PPN $\gamma$ is not gauge-invariant between areal and isotropic radius, and §8.1a shows a prior lane lost exactly that way |
| `consistency-vs-emergence` | ✅ | tagged per branch in §1.4: the light branch is **CONSISTENCY** (a calibrated identity), the matter branch is a **refuted forward derivation**. Neither is headlined as emergence |
| `verify-before-cite` | ✅ | §11. Thirty cite groups re-opened on this branch; eight items marked **unconfirmed**, including two external PPN bounds that are not in the tree at all |
| `ave-canonical-source` | ✅ | $G$, $M_\odot$, $R_\odot$ taken from `src/ave/core/constants.py` and `src/ave/gravity/solar_impedance.py`, and the constant-choice spread reported (§6.3) rather than a single number quoted |
| `flag-don't-fix` | ✅ | eleven flags, zero edits to `manuscript/`, `src/`, or any prior research doc. Two routed as open-item files |
| `ave-discrimination-check` | ✅ | §6.2: the light branch's one number is $\nu_{vac}\cdot(2/\nu_{vac})$, which is an identity — so the branch is **not** AVE-distinct and cannot be, and §5.3 says what that costs the $\nu_{vac}$ triangulation |
| `ave-mechanism-claims-discipline` | ✅ | §7's conformal-factor mechanism is stated **with** its solidity: verified exactly (`B/n_opt**2 - A == 0` returns `True`), and its consequence for the framework is routed to Grant, not asserted |
| `structural-null-needs-a-stencil-lens` | ✅ | $\gamma = 0$ is a null. It was checked against a **planted-defect positive control** (§9.3's alt-clock row returning its own $F = 2/3$) so that a null produced by a broken integrator could not pass as physics |
| `stop-and-ask` | ✅ (1 stuck-point, handled inside the 2-attempt cap) | reconstructing the handed-down *"the $/7$ family is gauge at PPN order"* argument. Two attempts; the Jacobian half reproduced and the inference half did not. **Stopped**, recorded both halves in §5.3, and re-derived the conclusion on independent grounds rather than spiralling |
| `read-don't-grep-for-completeness` | ✅ | §10. Twenty files read end to end; every absence claim carries a second, non-grep method; the enumerations are stated as products of a search |
| `grep-completeness-false-negatives` | ✅ | measured on this session: the shell `grep` is `ugrep --ignore-files` and warned on `--include`. Every enumeration re-run under `/usr/bin/grep` (§10.3) |

**Drift from the plan.** Two skills fired unplanned. `structural-null-needs-a-stencil-lens` fired when it became clear the headline is a **null** ($\gamma = 0$) and therefore owed a control — that is what put §9.3's positive control in. `ave-discrimination-check` fired on the light branch once the $Q = 2$ identity surfaced; it was planned only for the matter branch. No planned skill went unfired.

**Retro-pass addendum (2026-08-27, post-freeze — the two-knob amendment).** A repair was derived on a sibling branch after §0–§13 were frozen, and the instruction was *"a pointer plus a sharpening, both additive."* Three skills fired on that pass:

- `verify-before-cite` — the amendment carried a specific accusation (*"reads $q/2 = 1/2$ … where GR reads $3/2$"*) against a corpus document. **Verified before writing, per the instruction.** Two defects reproduced exactly (§8.1a); the numeral pair did not reproduce and **is not carried**.
- `consistency-vs-emergence` — the repair's caveat is carried at equal weight in the forward pointer: $(2,1,\tfrac12)$ **works**, nothing yet **forces** it, and that is the derivation-vs-fit line this document already draws for $Q = 2$.
- `flag-don't-fix` — the repair was **not** allowed to soften §0, and F10 records explicitly that it does **not** reduce the walk-back debt.

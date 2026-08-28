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

### ⚠ WHAT THIS IS, AND WHAT IT IS NOT — read before quoting any number above

- **This is not a new falsification of AVE's optics.** $\gamma_{light} = 1$ and $1.7517''$ hold. §6 argues they are a *calibrated consistency check* and not an emergence-class result, which is a downgrade of a claim's **class**, not of its truth.
- **This is not an engine bug.** No engine ran. It is a property of two written constitutive statements and the metric canon writes for them.
- **This does not adjudicate the fix.** §7 names the cheapest repair inside the framework. Naming a repair is not performing one, and this lane edits no canonical file.
- **The matter-sector numbers are only as good as the assignment that produces them.** They follow from taking `ponderomotive-equivalence.md`:14 literally as the metric a massive test body moves in. Canon's own quality record calls that assignment *"asserted by mechanical analogy rather than derived from a wave-equation projection"* (`manuscript/ave-kb/vol3/claim-quality.md`:1158). **If that assignment falls, these numbers fall with it** — which is the point of §7.

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

<!-- SECTION: light -->

## §7 — The fix is cheap and inside the framework

<!-- SECTION: fix -->

## §8 — Two things logged for months and never named

<!-- SECTION: logged -->

## §9 — Independent cross-check: direct geodesic integration

<!-- SECTION: geodesic -->

## §10 — METHOD, and its blind spots

<!-- SECTION: method -->

## §11 — Cite verification ledger

<!-- SECTION: cites -->

## §12 — Flags surfaced (NOT fixed by this lane)

<!-- SECTION: flags -->

## §13 — Skill-selection retro-pass

<!-- SECTION: retro -->

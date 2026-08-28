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

<!-- SECTION: chain -->

## §3 — Why the tensor repair failed

<!-- SECTION: tensor-repair -->

## §4 — `eps_11` is four objects across canon

<!-- SECTION: four-objects -->

## §5 — The /7 family is five contractions of one rank-2 tensor

<!-- SECTION: seven-family -->

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
